[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]

## Updated on 2025.09.25
> Usage instructions: [here](./docs/README.md#usage)

<details>
  <summary>Table of Contents</summary>
  <ol>
    <li><a href=#video-diffusion>Video Diffusion</a></li>
  </ol>
</details>

## Video Diffusion

|Publish Date|Title|Abstract|PDF|Code|
|---|---|---|---|---|
|**2025-09-23**|**Lyra: Generative 3D Scene Reconstruction via Video Diffusion Model Self-Distillation**|生成虚拟环境的能力对于从游戏到物理AI领域（例如机器人技术，自动驾驶和工业AI）等应用至关重要。当前基于学习的3D重建方法取决于捕获的现实世界多视图数据的可用性，这并不总是很容易获得。视频扩散模型的最新进展显示出了显着的想象力，但是它们的2D性质将应用程序限制为模拟机器人需要导航和与环境交互的模拟。在本文中，我们提出了一个自distillation框架，旨在将视频扩散模型中的隐式3D知识提炼成明显的3D高斯分裂（3DGS）表示，从而消除了对多视图训练数据的需求。具体来说，我们使用3DGS解码器增强了典型的RGB解码器，该解码器由RGB解码器的输出进行监督。在这种方法中，3DGS解码器可以通过视频扩散模型生成的合成数据纯粹训练。在推理时，我们的模型可以从文本提示或单个图像中合成3D场景以进行实时渲染。我们的框架进一步扩展到单眼输入视频的动态3D场景生成。实验结果表明，我们的框架在静态和动态的3D场景生成中实现了最先进的性能。|[2509.19296](http://arxiv.org/abs/2509.19296)|null|
|**2025-09-23**|**Flow marching for a generative PDE foundation model**|在大规模的PDE州时空轨迹上进行了预处理，最近显示出有望构建动态系统的可通用模型。然而，大多数现有的PDE基础模型都依赖于确定性的变压器体系结构，这些结构缺乏许多科学和工程应用程序的生成灵活性。我们提出了流程，这是一种算法，该算法将神经操作员学习与流动匹配，该流程匹配是通过分析物理动力学系统中错误积累的分析，并且我们在其上构建了生成的PDE基础模型。通过共同采样噪声水平和相邻状态之间的物理时间步长，该模型学习了一个统一的速度场，该速度场将嘈杂的当前状态传输到其干净的后继者，从而减少了长期的推出漂移，同时使不确定性吸引了一代。除了该核心算法外，我们还引入了物理学预言的变异自动编码器（P2VAE），将物理状态嵌入到一个紧凑的潜在空间中，并有效的流动变压器（FMT）结合了扩散式方案，该方案将扩散型方案与潜在的较大的较大的范围延伸到更大的范围，从而达到更大的计算范围，从而达到15x的良好范围，以达到15x的范围，以达到15x的范围，以达到15倍的范围。大大降低了成本。我们在12个不同的PDE家族中策划了约250万个轨迹的语料库，并在多个尺度上策划了P2VAES和FMT的套件。在下游评估中，我们基于看不见的kolmogorov湍流，几乎没有射击适应，证明了对确定性对应物的长期推出稳定性，并提出了不确定性分层的集合结果，强调了生成PDE基础模型对现实世界应用的重要性。|[2509.18611](http://arxiv.org/abs/2509.18611)|null|
|**2025-09-22**|**VideoFrom3D: 3D Scene Video Generation via Complementary Image and Video Diffusion Models**|在本文中，我们提出了Videofrom3D，这是一个新颖的框架，用于合成粗糙几何，摄像机轨迹和参考图像的高质量3D场景视频。我们的方法简化了3D图形设计工作流程，从而可以灵活设计探索并快速生产可交付成果。从粗几何形状中综合视频的直接方法可能会使视频扩散模型在几何结构上。但是，由于难以联合建模视觉质量，运动和时间一致性，因此现有的视频扩散模型难以为复杂场景产生高保真结果。为了解决这个问题，我们提出了一个生成框架，以利用图像和视频扩散模型的互补优势。具体而言，我们的框架由稀疏的锚定生成（SAG）和几何引导的生成式Inbetinging（GGI）模块组成。 SAG模块使用图像扩散模型生成高质量的，跨视图一致的锚点视图，并通过稀疏的外观引导采样的帮助。 GGI模块以这些锚点的视图为基础，使用视频扩散模型忠实地插入了中间帧，并通过基于流动的摄像机控制和结构指导增强了中间框架。值得注意的是，两个模块都没有任何配对的3D场景模型和自然图像的数据集，这非常困难。综合实验表明，我们的方法在多样化和挑战性的场景下产生高质量的风格场景视频，表现优于简单和扩展的基线。|[2509.17985](http://arxiv.org/abs/2509.17985)|null|
|**2025-09-22**|**I2VWM: Robust Watermarking for Image to Video Generation**|图像引导的视频生成（I2V）的快速进步引起了人们对其在错误信息和欺诈方面的潜在滥用的担忧，强调了迫切需要有效的数字水印。尽管现有的水印方法证明了单个模态内的鲁棒性，但它们无法在I2V设置中追踪源图像。为了解决这一差距，我们介绍了稳健的扩散距离的概念，该距离衡量了生成的视频中水印信号的时间持久性。在此基础上，我们提出了I2VWM，这是一种跨模式水印框架，旨在增强随时间的水印稳健性。 I2VWM在训练过程中利用视频模拟噪声层，并在推理过程中采用基于光学的对准模块。开源和商业I2V模型的实验表明，I2VWM在保持不可识别的同时显着提高了鲁棒性，在生成视频时代建立了新的跨模式水印范式。 \ href {https://github.com/mrcrims/i2vwm-robust-watermarking-for-image-to-video-generation} {代码发布。}|[2509.17773](http://arxiv.org/abs/2509.17773)|null|
|**2025-09-21**|**Echo-Path: Pathology-Conditioned Echo Video Generation**|心血管疾病（CVD）仍然是全球死亡率的主要原因，超声心动图对于诊断常见和先天性心脏状况至关重要。但是，某些病理的超声心动图数据稀缺，阻碍了强大的自动诊断模型的发展。在这项工作中，我们提出了Echo-Path，这是一种新型的生成框架，以生成以特定心脏病理为条件的超声心动图视频。 Echo-Path可以合成具有靶向异常的现实超声视频序列，重点是心房间隔缺陷（ASD）和肺动脉高压（PAH）。我们的方法将病理条件的机制引入了最新的回声视频发生器，从而使模型可以在心脏中学习和控制特定于疾病的结构和运动模式。定量评估表明，合成视频达到了低分布距离，表明视觉效果很高。在临床上，产生的回声表现出合理的病理标记。此外，经过培训的合成数据的分类器可以很好地推广到真实数据，并且在用于增强实际训练集的情况下，它将ASD和PAH的下游诊断分别提高了7 \％和8 \％。代码，权重和数据集可在此处提供https://github.com/marshall-mk/echopathv1|[2509.17190](http://arxiv.org/abs/2509.17190)|null|
|**2025-09-21**|**VidCLearn: A Continual Learning Approach for Text-to-Video Generation**|文本到视频生成是生成AI的新兴领域，从而从文本提示中创建了现实的，语义上准确的视频。尽管当前模型具有令人印象深刻的视觉质量和与输入文本的对齐，但它们通常依赖于静态知识，因此很难在不从头开始重新培训的新数据。为了解决这一限制，我们提出了Vidclearn，这是一个基于扩散的文本到视频生成的持续学习框架。 Vidclearn具有学生教师的体系结构，其中学生模型通过新的文本视频对进行了逐步更新，而教师模型可以通过生成重播来维护以前学习的知识。此外，我们引入了一种新型的时间一致性损失，以增强运动平滑度和视频检索模块，以提供推理结构指导。我们的体系结构还旨在在保持令人满意的生成性能的同时，比现有模型更有效地计算效率。实验结果表明，在视觉质量，语义比对和时间连贯性方面，Vidclearn优于基线方法。|[2509.16956](http://arxiv.org/abs/2509.16956)|null|
|**2025-09-21**|**$\mathtt{M^3VIR}$: A Large-Scale Multi-Modality Multi-View Synthesized Benchmark Dataset for Image Restoration and Content Creation**|游戏和娱乐业正在迅速发展，这是由沉浸式体验和生成AI（GAI）技术的整合驱动的。有效地培训此类模型需要大规模数据集来捕获游戏环境的多样性和背景。但是，现有数据集通常仅限于特定域或依赖人工降解，而人工降解并不能准确捕获游戏内容的独特特征。此外，仍缺乏可控视频的基准。   为了解决这些限制，我们介绍了$ \ mathtt {m^3vir} $，这是一种大规模的多模式，多视图数据集，专门设计用于克服当前资源的缺点。与现有数据集不同，$ \ mathtt {m^3vir} $提供了多样的，高保真的游戏内容，并用虚幻引擎5呈现，在8个类别的80个场景中提供了真实的地面LR-HR配对和多视图框架。它包括$ \ Mathtt {M^3vir \ _mr} $用于超分辨率（SR），新颖的视图合成（NVS）和组合的NVS+SR任务，以及$ \ Mathtt {M^3vir \ _ {MS}} $，首次进行多型式的“启用”启用，以下设置了启动的研究。此外，我们基于建立性能基准的几种最先进的SR和NVS方法。尽管没有现有的方法直接处理受控视频生成，但$ \ mathtt {m^3vir}$ 为推进此区域提供了基准。通过释放数据集，我们旨在促进下一代云游戏和娱乐的AI驱动恢复，压缩和可控内容的研究。|[2509.16873](http://arxiv.org/abs/2509.16873)|null|
|**2025-09-20**|**FG-Attn: Leveraging Fine-Grained Sparsity In Diffusion Transformers**|用扩散变压器生成逼真的视频需要大量的计算，而注意力层则是中央瓶颈。即使产生一个短剪辑也需要在很长的嵌入序列上运行变压器，例如5秒视频的嵌入超过30k的嵌入，从而产生了显着的延迟。先前的工作旨在通过利用注意层中的稀疏性来减少计算来减轻这种瓶颈。但是，这些作品通常依赖于块 - 帕克斯的注意，只有当注意力分数中的所有条目（对应于M Queries和M键，通常为M = 64）时，它才会跳过计算计算。这种对注意力评分的粗粒度跳过并不能完全利用注意图中的稀疏性，并为改进留出了空间。在这项工作中，我们提出了FG-ATTN，这是一种稀疏的关注机制，用于长期延伸变压器，以颗粒状的粒度利用稀疏性。与块状块的注意不同，它跳过了整个MXM块，我们的方法跳过了注意力图的MX1切片的粒度计算。每个切片都是通过查询向量和一个键之间的查询点点产生的。为了实施我们提出的稀疏注意机制，我们开发了一种新的有效的大量负载操作，称为异步聚会负载。此加载操作从内存中收集了一组稀疏的相关键值向量，并将它们安排到GPU共享内存中的包装瓷砖中。在计算查询块的关注时，仅将与这些查询相关的一组稀疏键将其加载到共享内存中，这与将键令的完整块中的整个块中的块加载到块中的注意力中。我们的细粒度稀疏注意力应用于视频扩散模型，平均达到1.55倍（高达1.65倍）的速度，持续5秒，480p视频和平均1.41倍（高达1.49倍），持续5秒，720p视频，在单个H100 GPU上。|[2509.16518](http://arxiv.org/abs/2509.16518)|null|
|**2025-09-20**|**RLGF: Reinforcement Learning with Geometric Feedback for Autonomous Driving Video Generation**|合成数据对于推进自动驾驶（AD）系统至关重要，但是当前最新的视频生成模型尽管具有视觉现实主义，但仍遭受了微妙的几何扭曲，这些扭曲限制了其对下游感知任务的效用。我们识别并量化了这个关键问题，在使用合成数据与实际数据时，证明了3D对象检测的显着性能差距。为了解决这个问题，我们通过几何反馈（RLGF）介绍了增强学习，RLGF通过纳入专门的潜在空间广告感知模型的奖励来独特地完善视频扩散模型。它的核心组件包括在扩散过程中针对目标反馈的有效的潜在空间窗口优化技术，以及一个分层的几何奖励（HGR）系统，为点线平面比对提供多级奖励以及场景占用连贯性。为了量化这些扭曲，我们提出了地质。 RLGF应用于潜水的模型，将几何误差（例如，VP误差降低21 \％，深度误差，57 \％）将3D对象检测图提高到12.7 \％，从而将差距缩小到实时数据范围。 RLGF提供了一种插件解决方案，用于生成几何声音和可靠的合成视频，以进行广告开发。|[2509.16500](http://arxiv.org/abs/2509.16500)|null|
|**2025-09-19**|**Lynx: Towards High-Fidelity Personalized Video Generation**|我们提出了Lynx，这是一种来自单个输入图像的个性化视频合成的高保真模型。 Lynx建立在开源扩散变压器（DIT）基础模型的基础上，引入了两个轻巧的适配器，以确保身份保真度。 ID-ADAPTER采用感知器的重新采样器将斜面衍生的面部嵌入转换为紧凑的身份代币进行调节，而Ref-Adapter则通过交叉注意从冻结的参考途径中整合了冷冻参考途径的密集VAE特征，从而在所有变压器层中注入细粒度的细节。这些模块共同实现了稳健的身份，同时保持时间连贯性和视觉现实主义。通过对40名受试者和20个无偏的提示的精心策划的基准进行评估，产生了800个测试用例，Lynx表现出了出色的面部相似之处，竞争性的提示和强大的视频质量，从而提高了个性化视频生成的状态。|[2509.15496](http://arxiv.org/abs/2509.15496)|null|

<p align=right>(<a href=#updated-on-20250925>back to top</a>)</p>

[contributors-shield]: https://img.shields.io/github/contributors/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[contributors-url]: https://github.com/Vincentqyw/cv-arxiv-daily/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[forks-url]: https://github.com/Vincentqyw/cv-arxiv-daily/network/members
[stars-shield]: https://img.shields.io/github/stars/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[stars-url]: https://github.com/Vincentqyw/cv-arxiv-daily/stargazers
[issues-shield]: https://img.shields.io/github/issues/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[issues-url]: https://github.com/Vincentqyw/cv-arxiv-daily/issues

