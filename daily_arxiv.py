import os
import re
import json
import arxiv
import yaml
import logging
import argparse
import datetime
import requests
from googletrans import Translator

logging.basicConfig(format='[%(asctime)s %(levelname)s] %(message)s',
                    datefmt='%m/%d/%Y %H:%M:%S',
                    level=logging.INFO)

github_url = "https://api.github.com/search/repositories"
arxiv_url = "http://arxiv.org/"

def load_config(config_file:str) -> dict:
    '''
    config_file: input config file path
    return: a dict of configuration
    '''
    def pretty_filters(**config) -> dict:
        keywords = dict()
        EXCAPE = '\"'
        QUOTA = '' 
        OR = 'OR'
        def parse_filters(filters:list):
            ret = ''
            for idx in range(0,len(filters)):
                filter = filters[idx]
                if len(filter.split()) > 1:
                    ret += (EXCAPE + filter + EXCAPE)
                else:
                    ret += (QUOTA + filter + QUOTA)
                if idx != len(filters) - 1:
                    ret += f' {OR} '
            return ret
        for k,v in config['keywords'].items():
            keywords[k] = parse_filters(v['filters'])
        return keywords
        
    with open(config_file,'r') as f:
        config = yaml.load(f,Loader=yaml.FullLoader)
        config['kv'] = pretty_filters(**config)
        logging.info(f'config = {config}')
    return config

def get_authors(authors, first_author = False):
    output = str()
    if first_author == False:
        output = ", ".join(str(author) for author in authors)
    else:
        output = authors[0]
    return output

def sort_papers(papers):
    output = dict()
    keys = list(papers.keys())
    keys.sort(reverse=True)
    for key in keys:
        output[key] = papers[key]
    return output

def translate_text(text, dest='zh-CN'):
    try:
        translator = Translator()
        translation = translator.translate(text, dest=dest)
        return translation.text
    except:
        return text

def get_code_link(qword:str) -> str:
    query = f"{qword}"
    params = {
        "q": query,
        "sort": "stars",
        "order": "desc"
    }
    try:
        r = requests.get(github_url, params=params)
        results = r.json()
        code_link = None
        if results.get("total_count", 0) > 0:
            if results['items'][0]['score'] > 1.0: 
                code_link = results["items"][0]["html_url"]
        return code_link
    except Exception as e:
        logging.error(f"GitHub API error: {e}")
        return None

def get_daily_papers(topic,query="slam", max_results=2):
    content = dict()
    content_to_web = dict()
    search_engine = arxiv.Search(
        query = query,
        max_results = max_results,
        sort_by = arxiv.SortCriterion.SubmittedDate
    )

    for result in search_engine.results():
        paper_id = result.get_short_id()
        paper_title = result.title
        paper_url = result.entry_id
        paper_abstract = result.summary.replace("\n"," ")
        paper_authors = get_authors(result.authors)
        paper_first_author_name = get_authors(result.authors,first_author = True)
        primary_category = result.primary_category
        publish_time = result.published.date()
        update_time = result.updated.date()
        comments = result.comment

        translated_abstract = translate_text(paper_abstract)

        logging.info(f"Time = {update_time} title = {paper_title} author = {paper_first_author_name}")

        ver_pos = paper_id.find('v')
        if ver_pos == -1:
            paper_key = paper_id
        else:
            paper_key = paper_id[0:ver_pos]
        paper_url = arxiv_url + 'abs/' + paper_key

        try:
            repo_url = get_code_link(paper_title)
            # 注意：这里保持原来的存储格式 |...|，方便 update_paper_links 解析
            # 我们将在 json_to_md 中改变呈现方式
            if repo_url is not None:
                content[paper_key] = "|**{}**|**{}**|{}|[{}]({})|**[link]({})**|\n".format(
                    update_time, paper_title, translated_abstract, paper_key, paper_url, repo_url)
                content_to_web[paper_key] = "- {}, **{}**, {} et.al., Paper: [{}]({}), Code: **[{}]({})**".format(
                    update_time, paper_title, paper_first_author_name, paper_url, paper_url, repo_url, repo_url)
            else:
                content[paper_key] = "|**{}**|**{}**|{}|[{}]({})|null|\n".format(
                    update_time, paper_title, translated_abstract, paper_key, paper_url)
                content_to_web[paper_key] = "- {}, **{}**, {} et.al., Paper: [{}]({})".format(
                    update_time, paper_title, paper_first_author_name, paper_url, paper_url)

            if comments:
                content_to_web[paper_key] += f", {comments}\n"
            else:
                content_to_web[paper_key] += f"\n"

        except Exception as e:
            logging.error(f"exception: {e} with id: {paper_key}")

    data = {topic:content}
    data_web = {topic:content_to_web}
    return data,data_web

def update_paper_links(filename):
    '''
    weekly update paper links in json file
    '''
    def parse_arxiv_string(s):
        parts = s.split("|")
        date = parts[1].strip()
        title = parts[2].strip()
        authors = parts[3].strip() 
        arxiv_id_part = parts[4].strip()
        match = re.search(r'\[(.*?)]', arxiv_id_part)
        arxiv_id = match.group(1) if match else arxiv_id_part
        code = parts[5].strip()
        arxiv_id = re.sub(r'v\d+', '', arxiv_id)
        return date,title,authors,arxiv_id,code

    with open(filename,"r", encoding="utf-8") as f:
        content = f.read()
        if not content:
            m = {}
        else:
            m = json.loads(content)
        json_data = m.copy()

    for keywords,v in json_data.items():
        logging.info(f'keywords = {keywords}')
        for paper_id,contents in v.items():
            contents = str(contents)
            if '|null|' not in contents:
                continue
                
            update_time, paper_title, paper_abstract_translated, _, code_url = parse_arxiv_string(contents)
            
            repo_url = None
            try:
                repo_url = get_code_link(paper_title)
            except Exception as e:
                logging.error(f"exception during link update: {e} with id: {paper_id}")
            
            paper_url_md = f"[{paper_id}]({arxiv_url}abs/{paper_id})"
            if repo_url is not None:
                new_cont = "|{}|**{}**|{}|{}|**[link]({})**|\n".format(
                    update_time, paper_title, paper_abstract_translated, paper_url_md, repo_url)
                logging.info(f'Found code for {paper_id}: {repo_url}')
                json_data[keywords][paper_id] = str(new_cont)

    with open(filename,"w", encoding="utf-8") as f:
        json.dump(json_data,f, indent=4, ensure_ascii=False)

def update_json_file(filename, data_dict):
    '''
    daily update json file using data_dict, and remove data older than 7 days
    '''
    try:
        with open(filename, "r", encoding="utf-8") as f:
            content = f.read()
            if not content:
                m = {}
            else:
                m = json.loads(content)
    except FileNotFoundError:
        m = {}
    
    json_data = m.copy()

    # 1. Merge new data
    for data in data_dict:
        for keyword, papers in data.items():
            if keyword in json_data:
                json_data[keyword].update(papers)
            else:
                json_data[keyword] = papers

    # 2. Filter out papers older than 7 days
    DateNow = datetime.date.today()
    days_to_keep = 7
    
    filtered_json_data = {}
    
    for keyword, papers in json_data.items():
        filtered_papers = {}
        for paper_key, paper_content in papers.items():
            try:
                # Extract date from the markdown string format: |**YYYY-MM-DD**|...
                match = re.search(r'\|\*\*(\d{4}-\d{2}-\d{2})\*\*\|', paper_content)
                if match:
                    date_str = match.group(1)
                    paper_date = datetime.datetime.strptime(date_str, "%Y-%m-%d").date()
                    
                    # Keep if within last 7 days
                    if (DateNow - paper_date).days < days_to_keep:
                        filtered_papers[paper_key] = paper_content
                else:
                    # If date parsing fails, strictly speaking we might want to keep or drop.
                    # Assuming valid format, we skip bad data.
                    pass
            except Exception as e:
                logging.error(f"Error parsing date for {paper_key}: {e}")
        
        if filtered_papers:
            filtered_json_data[keyword] = filtered_papers

    # 3. Write back to file
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(filtered_json_data, f, indent=4, ensure_ascii=False)

def json_to_md(filename, md_filename,
               task = '',
               to_web = False,
               use_title = True,
               use_tc = True,
               show_badge = True,
               use_b2t = True):
    """
    @param filename: str
    @param md_filename: str
    @return None
    """
    def pretty_math(s:str) -> str:
        ret = ''
        match = re.search(r"\$.*\$", s)
        if match == None:
            return s
        math_start,math_end = match.span()
        space_trail = space_leading = ''
        if s[:math_start][-1] != ' ' and '*' != s[:math_start][-1]: space_trail = ' '
        if s[math_end:][0] != ' ' and '*' != s[math_end:][0]: space_leading = ' '
        ret += s[:math_start]
        ret += f'{space_trail}${match.group()[1:-1].strip()}${space_leading}'
        ret += s[math_end:]
        return ret

    DateNow = datetime.date.today()
    DateNow = str(DateNow)
    DateNow = DateNow.replace('-','.')

    with open(filename,"r", encoding="utf-8") as f:
        content = f.read()
        if not content:
            data = {}
        else:
            data = json.loads(content)

    with open(md_filename,"w", encoding="utf-8") as f:
        pass

    with open(md_filename,"a+", encoding="utf-8") as f:
        if (use_title == True) and (to_web == True):
            f.write("---\n" + "layout: default\n" + "---\n\n")

        if show_badge == True:
            f.write(f"[![Contributors][contributors-shield]][contributors-url]\n")
            f.write(f"[![Forks][forks-shield]][forks-url]\n")
            f.write(f"[![Stargazers][stars-shield]][stars-url]\n")
            f.write(f"[![Issues][issues-shield]][issues-url]\n\n")

        if use_title == True:
            f.write("## Updated on " + DateNow + "\n")
        else:
            f.write("> Updated on " + DateNow + "\n")

        f.write("> Usage instructions: [here](./docs/README.md#usage)\n\n")

        if use_tc == True:
            f.write("<details>\n")
            f.write("  <summary>Table of Contents</summary>\n")
            f.write("  <ol>\n")
            for keyword in data.keys():
                day_content = data[keyword]
                if not day_content:
                    continue
                kw = keyword.replace(' ','-')
                f.write(f"    <li><a href=#{kw.lower()}>{keyword}</a></li>\n")
            f.write("  </ol>\n")
            f.write("</details>\n\n")

        for keyword in data.keys():
            day_content = data[keyword]
            if not day_content:
                continue
            f.write(f"## {keyword}\n\n")

            # NOTE: Removed table header here to support custom layout

            day_content = sort_papers(day_content)

            for _,v in day_content.items():
                if v is not None:
                    # Parse the stored string to reformat it
                    # Original format in JSON: |**Date**|**Title**|Abstract|PDF|Code|
                    content_str = str(v)
                    try:
                        if '|' in content_str:
                            parts = content_str.split('|')
                            # parts[1]=Date, parts[2]=Title, parts[3]=Abstract, parts[4]=PDF, parts[5]=Code
                            if len(parts) >= 6:
                                date = parts[1].strip()
                                title = parts[2].strip()
                                abstract = parts[3].strip()
                                pdf_link = parts[4].strip()
                                code_link = parts[5].strip()
                                
                                # 第一行：日期 | 标题 | PDF链接 | 代码链接(若有)
                                line1 = f"- {date} {title} {pdf_link}"
                                if code_link and 'null' not in code_link:
                                    line1 += f" {code_link}"
                                
                                # 第二行：中文概要 (使用引用块或缩进)
                                line2 = f"  > {abstract}"
                                
                                f.write(pretty_math(line1) + "\n")
                                f.write(pretty_math(line2) + "\n\n")
                            else:
                                f.write(pretty_math(content_str)) # Fallback
                        else:
                            f.write(pretty_math(content_str))
                    except Exception as e:
                        logging.warning(f"Parse error for content: {e}")
                        f.write(pretty_math(content_str))

            f.write(f"\n")

            if use_b2t:
                top_info = f"#Updated on {DateNow}"
                top_info = top_info.replace(' ','-').replace('.','')
                f.write(f"<p align=right>(<a href={top_info.lower()}>back to top</a>)</p>\n\n")

        if show_badge == True:
            f.write((f"[contributors-shield]: https://img.shields.io/github/"
                     f"contributors/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge\n"))
            f.write((f"[contributors-url]: https://github.com/Vincentqyw/"
                     f"cv-arxiv-daily/graphs/contributors\n"))
            f.write((f"[forks-shield]: https://img.shields.io/github/forks/Vincentqyw/"
                     f"cv-arxiv-daily.svg?style=for-the-badge\n"))
            f.write((f"[forks-url]: https://github.com/Vincentqyw/"
                     f"cv-arxiv-daily/network/members\n"))
            f.write((f"[stars-shield]: https://img.shields.io/github/stars/Vincentqyw/"
                     f"cv-arxiv-daily.svg?style=for-the-badge\n"))
            f.write((f"[stars-url]: https://github.com/Vincentqyw/"
                     f"cv-arxiv-daily/stargazers\n"))
            f.write((f"[issues-shield]: https://img.shields.io/github/issues/Vincentqyw/"
                     f"cv-arxiv-daily.svg?style=for-the-badge\n"))
            f.write((f"[issues-url]: https://github.com/Vincentqyw/"
                     f"cv-arxiv-daily/issues\n\n"))

    logging.info(f"{task} finished")

def demo(**config):
    data_collector = []
    data_collector_web= []

    keywords = config['kv']
    max_results = config['max_results']
    publish_readme = config['publish_readme']
    publish_gitpage = config['publish_gitpage']
    publish_wechat = config['publish_wechat']
    show_badge = config['show_badge']

    b_update = config['update_paper_links']
    logging.info(f'Update Paper Link = {b_update}')
    if config['update_paper_links'] == False:
        logging.info(f"GET daily papers begin")
        for topic, keyword in keywords.items():
            logging.info(f"Keyword: {topic}, Query: {keyword}")
            data, data_web = get_daily_papers(topic, query = keyword,
                                              max_results = max_results)
            data_collector.append(data)
            data_collector_web.append(data_web)
            print("\n")
        logging.info(f"GET daily papers end")

    if publish_readme:
        json_file = config['json_readme_path']
        md_file = config['md_readme_path']
        if config['update_paper_links']:
            update_paper_links(json_file)
        else:
            update_json_file(json_file,data_collector)
        json_to_md(json_file,md_file, task ='Update Readme', \
                   show_badge = show_badge)

    if publish_gitpage:
        json_file = config['json_gitpage_path']
        md_file = config['md_gitpage_path']
        if config['update_paper_links']:
            update_paper_links(json_file)
        else:
            update_json_file(json_file,data_collector)
        json_to_md(json_file, md_file, task ='Update GitPage', \
                   to_web = True, show_badge = show_badge, \
                   use_tc=False, use_b2t=False)

    if publish_wechat:
        json_file = config['json_wechat_path']
        md_file = config['md_wechat_path']
        if config['update_paper_links']:
            update_paper_links(json_file)
        else:
            update_json_file(json_file, data_collector_web)
        json_to_md(json_file, md_file, task ='Update Wechat', \
                   to_web=False, use_title= False, show_badge = show_badge)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--config_path',type=str, default='config.yaml',
                        help='configuration file path')
    parser.add_argument('--update_paper_links', default=False,
                        action="store_true",help='whether to update paper links etc.')
    args = parser.parse_args()
    config = load_config(args.config_path)
    config = {**config, 'update_paper_links':args.update_paper_links}
    demo(**config)
