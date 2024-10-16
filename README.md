[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]

## Updated on 2024.10.16
> Usage instructions: [here](./docs/README.md#usage)

<details>
  <summary>Table of Contents</summary>
  <ol>
    <li><a href=#3d>3D</a></li>
    <li><a href=#3d-reconstruction>3D Reconstruction</a></li>
    <li><a href=#diffusion>Diffusion</a></li>
    <li><a href=#nerf>NeRF</a></li>
  </ol>
</details>

## 3D

|Publish Date|Title|Abstract|PDF|Code|
|---|---|---|---|---|
|**2024-10-15**|**LoGS: Visual Localization via Gaussian Splatting with Fewer Training Images**|视觉定位涉及估计查询图像的6-DoF（自由度）相机姿态，这是各种计算机视觉和机器人任务中的基本组成部分。本文介绍了LoGS，这是一种基于视觉的定位流水线，利用3D高斯散点（GS）技术作为场景表示。这种新颖的表示允许高质量的新颖视图合成。在映射阶段，首先应用运动结构（SfM），然后生成GS图。在定位过程中，通过图像检索、局部特征匹配和PnP求解器获得初始位置，然后在GS地图上通过综合分析的方式实现高精度姿态。在四个大规模数据集上的实验结果证明了所提出的方法在估计相机姿态方面的SoTA准确性和在具有挑战性的少镜头条件下的鲁棒性。 et.al.|[2410.11505](http://arxiv.org/abs/2410.11505)|null|
|**2024-10-15**|**GS^3: Efficient Relighting with Triple Gaussian Splatting**|我们提出了一种基于空间和角度高斯的表示和三重叠加过程，用于从多视点照明输入图像中实时、高质量地进行新颖的照明和视图合成。为了描述复杂的外观，我们采用朗伯加角高斯混合作为每个空间高斯的有效反射函数。为了生成自阴影，我们将所有空间高斯分布向光源投射以获得阴影值，这些值由一个小型多层感知器进一步细化。为了补偿全局照明等其他影响，训练另一个网络来计算并添加每个空间的高斯RGB元组。我们的表示方法的有效性在30个几何形状（从实心到蓬松）和外观（从半透明到各向异性）变化很大的样本上得到了证明，并使用了不同形式的输入数据，包括合成/重建物体的渲染图像、用手持相机和闪光灯拍摄的照片，或来自专业光台的照片。我们在单个商品GPU上实现了40-70分钟的训练时间和90 fps的渲染速度。我们的结果在质量/性能方面与最先进的技术相比毫不逊色。我们的代码和数据可在以下网址公开获取https://GSrelight.github.io/. et.al.|[2410.11419](http://arxiv.org/abs/2410.11419)|null|
|**2024-10-15**|**MCGS: Multiview Consistency Enhancement for Sparse-View 3D Gaussian Radiance Fields**|由3D高斯表示的辐射场擅长合成新颖的视图，提供了高训练效率和快速渲染。然而，在稀疏输入视图的情况下，缺乏多视图一致性约束会导致点云初始化不佳，优化和致密化的启发式方法不可靠，从而导致性能不佳。现有的方法通常包含来自密集估计网络的深度先验，但忽略了输入图像中固有的多视图一致性。此外，它们依赖于基于多视图立体（MVS）的初始化，这限制了场景表示的效率。为了克服这些挑战，我们提出了一种基于3D高斯散斑的视图合成框架，称为MCGS，能够从稀疏输入视图中重建出逼真的场景。MCGS在增强多视图一致性方面的关键创新如下：i）我们引入了一种初始化方法，该方法利用稀疏匹配器结合随机填充策略，产生了一组紧凑但足够的初始点。这种方法增强了初始几何先验，促进了高效的场景表示。ii）我们开发了一种多视图一致性引导的渐进修剪策略，通过增强一致性和消除低贡献高斯分布来细化高斯场。这些模块化的即插即用策略增强了对稀疏输入视图的鲁棒性，加速了渲染，减少了内存消耗，使MCGS成为3D高斯散斑的实用高效框架。 et.al.|[2410.11394](http://arxiv.org/abs/2410.11394)|null|
|**2024-10-15**|**Scalable Indoor Novel-View Synthesis using Drone-Captured 360 Imagery with 3D Gaussian Splatting**|对于大型、复杂、多层的室内场景，场景重建和新颖的视图合成是一项具有挑战性和耗时的任务。先前的方法利用无人机进行数据采集，利用辐射场进行场景重建，这两种方法都存在一定的挑战。首先，为了用无人机的前置摄像头捕捉不同的视角，一些方法以不稳定的锯齿形方式飞行无人机，这阻碍了无人机的驾驶，并在捕获的数据中产生了运动模糊。其次，大多数辐射场方法不容易扩展到任意数量的图像。本文提出了一种高效且可扩展的管道，用于使用3D高斯散斑从无人机捕获的360度视频中合成室内新颖的视图。360度摄像头可以捕捉到广泛的视点，从而在简单直接的无人机轨迹下进行全面的场景捕捉。为了将我们的方法扩展到大型场景，我们设计了一种分而治之的策略，将场景自动分割成可以单独和并行重建的较小块。我们还提出了一种从粗到细的对齐策略，将这些块无缝匹配在一起，组成整个场景。我们的实验表明，与现有方法相比，重建质量（即PSNR和SSIM）和计算时间都有显著提高。 et.al.|[2410.11285](http://arxiv.org/abs/2410.11285)|null|
|**2024-10-14**|**Few-shot Novel View Synthesis using Depth Aware 3D Gaussian Splatting**|3D高斯溅射在新颖的视图合成中已经超越了神经辐射场方法，实现了更低的计算成本和实时高质量的渲染。虽然它可以在大量输入视图的情况下产生高质量的绘制，但当只有少数视图可用时，其性能会显著下降。在这项工作中，我们通过提出一种用于少镜头新颖视图合成的深度感知高斯飞溅方法来解决这个问题。我们使用单目深度预测作为先验，并结合尺度不变的深度损失，在少数输入视图下约束3D形状。我们还使用低阶球谐函数对颜色进行建模，以避免过拟合。此外，我们观察到，像在原始作品中那样，定期删除不透明度较低的斑点会导致点云非常稀疏，从而降低渲染质量。为了减轻这种情况，我们保留了所有斑点，从而在一些视图设置中实现了更好的重建。实验结果表明，我们的方法在峰值信噪比、结构相似性指数和感知相似性方面分别提高了10.5%、6%和14.1%，优于传统的3D高斯飞溅方法，从而验证了我们方法的有效性。该代码将在以下网址提供：https://github.com/raja-kumar/depth-aware-3DGS et.al.|[2410.11080](http://arxiv.org/abs/2410.11080)|null|
|**2024-10-14**|**FlexGen: Flexible Multi-View Generation from Text and Image Inputs**|在这项工作中，我们介绍了FlexGen，这是一个灵活的框架，旨在生成可控和一致的多视图图像，以单个视图图像或文本提示为条件，或两者兼而有之。FlexGen通过对3D感知文本注释进行额外调节，解决了可控多视图合成的挑战。我们利用GPT-4V的强大推理能力来生成3D感知文本注释。通过分析作为平铺多视图图像排列的对象的四个正交视图，GPT-4V可以生成包含具有空间关系的3D感知信息的文本注释。通过将控制信号与所提出的自适应双控制模块集成，我们的模型可以生成与指定文本相对应的多视图图像。FlexGen支持多种可控功能，允许用户修改文本提示以生成合理且相应的看不见的部分。此外，用户可以影响外观和材料属性等属性，包括金属和粗糙度。大量实验表明，我们的方法提供了增强的多重可控性，标志着比现有多视图扩散模型的重大进步。这项工作对需要快速灵活的3D内容创建的领域具有重大意义，包括游戏开发、动画和虚拟现实。项目页面：https://xxu068.github.io/flexgen.github.io/. et.al.|[2410.10745](http://arxiv.org/abs/2410.10745)|null|
|**2024-10-13**|**FAMOUS: High-Fidelity Monocular 3D Human Digitization Using View Synthesis**|深度隐式建模和铰接模型的进步显著增强了从单一图像中数字化3D人体形象的过程。虽然最先进的方法大大提高了几何精度，但准确推断纹理的挑战仍然存在，特别是在正面图像中人的背部等模糊区域。纹理预测的这种局限性在很大程度上源于大规模和多样化的3D数据集的稀缺，而它们的2D数据集则丰富且易于访问。为了解决这个问题，我们的论文提出利用广泛的2D时尚数据集来增强3D人体数字化中的纹理和形状预测。我们整合了时尚数据集中的2D先验来学习遮挡的后视图，并用我们提出的域对齐策略进行了改进。然后，我们将这些信息与输入图像融合，以获得给定人的完全纹理网格。通过在标准3D人体基准上的广泛实验，我们展示了我们的方法在纹理和几何方面的卓越性能。代码和数据集可在https://github.com/humansensinglab/FAMOUS. et.al.|[2410.09690](http://arxiv.org/abs/2410.09690)|null|
|**2024-10-11**|**Look Gauss, No Pose: Novel View Synthesis using Gaussian Splatting without Accurate Pose Initialization**|3D高斯散斑最近已经成为一种强大的工具，可以从一组摆姿势的输入图像中快速准确地合成新的视图。然而，与大多数新颖的视图合成方法一样，它依赖于精确的相机姿态信息，这限制了它在真实世界场景中的适用性，在这些场景中，获取准确的相机姿态可能具有挑战性，甚至是不可能的。我们提出了一种对3D高斯散斑框架的扩展，通过优化与光度残差相关的外部相机参数。我们推导了分析梯度，并将其计算与现有的高性能CUDA实现相结合。这使得下游任务成为可能，如6-DoF相机姿态估计以及联合重建和相机细化。特别是，我们实现了真实场景中姿态估计的快速收敛和高精度。我们的方法通过联合优化几何和相机姿态，实现了快速重建3D场景，而不需要精确的姿态信息，同时在新颖的视图合成中实现了最先进的结果。我们的方法比大多数竞争方法优化速度快得多，渲染速度也快几倍。我们通过模拟环境在真实场景和复杂轨迹上显示结果，在LLFF上实现了最先进的结果，同时与最有效的竞争方法相比，运行时间缩短了两到四倍。源代码将在https://github.com/Schmiddo/noposegs . et.al.|[2410.08743](http://arxiv.org/abs/2410.08743)|**[link](https://github.com/schmiddo/noposegs)**|
|**2024-10-10**|**DifFRelight: Diffusion-Based Facial Performance Relighting**|我们提出了一种使用基于扩散的图像到图像转换的自由视点面部表现再照明的新框架。利用包含在各种照明条件下捕获的不同面部表情的特定主题数据集，包括平面照明和一次一光（OLAT）场景，我们训练了一个用于精确照明控制的扩散模型，从而能够从平面照明输入中获得高保真度的面部图像。我们的框架包括平面光捕获和随机噪声的空间对齐调节，以及用于全局控制的集成照明信息，利用预训练的稳定扩散模型的先验知识。然后将该模型应用于在一致的平面照明环境中捕获的动态面部表现，并使用可扩展的动态3D高斯散斑方法进行重建，以保持重新照明结果的质量和一致性，从而进行新的视图合成。此外，我们通过将新颖的区域照明表示与定向照明集成，引入了统一的照明控制，允许对灯光大小和方向进行联合调整。我们还使用多个方向光实现高动态范围成像（HDRI）合成，以在复杂的照明条件下产生动态序列。我们的评估表明，模型在实现精确的照明控制和跨各种面部表情的泛化方面非常有效，同时保留了皮肤纹理和头发等详细特征。该模型准确地再现了复杂的照明效果，如眼睛反射、次表面散射、自阴影和半透明，在我们的框架内推进了照片真实感。 et.al.|[2410.08188](http://arxiv.org/abs/2410.08188)|null|
|**2024-10-10**|**IncEventGS: Pose-Free Gaussian Splatting from a Single Event Camera**|用于新颖视图合成的隐式神经表示和显式3D高斯散斑（3D-GS）最近在基于帧的相机（如RGB和RGB-D相机）方面取得了显著进展。与基于帧的相机相比，一种新型的仿生视觉传感器，即事件相机，在高时间分辨率、高动态范围、低功耗和低延迟方面具有优势。由于其独特的异步和不规则的数据捕获过程，将神经表示或3D高斯飞溅应用于事件相机的工作有限。在这项工作中，我们提出了IncEventGS，这是一种使用单事件相机的增量3D高斯散斑重建算法。为了逐步恢复3D场景表示，我们利用了IncEventGS的传统SLAM管道的跟踪和映射范式。给定传入的事件流，跟踪器首先基于先前重建的3D-GS场景表示来估计初始相机运动。然后，映射器基于来自跟踪器的先前估计的运动轨迹，联合细化3D场景表示和相机运动。实验结果表明，与之前的基于NeRF的方法和其他相关基线相比，IncEventGS具有更优的性能，即使我们没有地面实况相机姿态。此外，与最先进的事件视觉里程计方法相比，我们的方法在相机运动估计方面也可以提供更好的性能。代码可在以下网址公开获取：https://github.com/wu-cvgl/IncEventGS. et.al.|[2410.08107](http://arxiv.org/abs/2410.08107)|**[link](https://github.com/wu-cvgl/inceventgs)**|

<p align=right>(<a href=#updated-on-20241016>back to top</a>)</p>

## 3D Reconstruction

|Publish Date|Title|Abstract|PDF|Code|
|---|---|---|---|---|
|**2024-10-15**|**Robotic Arm Platform for Multi-View Image Acquisition and 3D Reconstruction in Minimally Invasive Surgery**|微创手术（MIS）具有显著的优势，如缩短恢复时间和最大限度地减少患者创伤，但在可见性和可及性方面存在挑战，使精确的3D重建成为手术规划和导航的重要工具。这项工作介绍了一种机器人手臂平台，用于在MIS环境中进行高效的多视图图像采集和精确的3D重建。我们将腹腔镜改装成机器人手臂，并在不同的照明条件（手术室和腹腔镜）和轨迹（球形和腹腔镜）下捕获了几个绵羊器官的离体图像。我们采用了最近发布的基于学习的特征匹配器与COLMAP相结合来生成我们的重建。通过高精度激光扫描对重建进行定量评估。我们的结果表明，虽然重建在真实的MIS照明和轨迹下遭受的损失最大，但我们的管道的许多版本都达到了接近亚毫米的精度，平均均方根误差为1.05毫米，倒角距离为0.82毫米。我们最好的重建结果发生在手术室照明和球形轨迹上。我们的机器人平台为MIS环境中的3D生成提供了一种受控、可重复的多视图数据采集工具，我们希望这能为训练基于学习的模型带来新的数据集。 et.al.|[2410.11703](http://arxiv.org/abs/2410.11703)|null|
|**2024-10-15**|**Simultaneous Diffusion Sampling for Conditional LiDAR Generation**|通过捕获反映周围环境几何形状的3D点云，LiDAR已成为自主系统的主要传感器。如果激光雷达扫描太稀疏、被障碍物遮挡或范围太小，在尊重场景几何形状的同时增强点云扫描对下游任务很有用。在视觉生成方法兴趣爆炸式增长的推动下，条件激光雷达生成开始兴起。本文提出了一种新的同时扩散采样方法，用于生成基于多视角场景三维结构的点云。关键思想是对生成过程施加多视图几何约束，利用互信息来增强结果。我们的方法首先将输入扫描重新转换为扫描周围的多个新视点，从而创建多个合成激光雷达扫描。然后，根据我们的方法，合成和输入的激光雷达扫描同时进行条件生成。结果表明，我们的方法可以对点云扫描产生准确和几何一致的增强，使其在各种基准测试中大大优于现有方法。 et.al.|[2410.11628](http://arxiv.org/abs/2410.11628)|null|
|**2024-10-15**|**Depth Estimation From Monocular Images With Enhanced Encoder-Decoder Architecture**|由于需要通常提供深度信息的立体或多视图数据，因此从单个2D图像估计深度是一项具有挑战性的任务。本文通过引入一种使用编码器-解码器架构的基于深度学习的新方法来应对这一挑战，其中Inception-ResNet-v2模型被用作编码器。根据现有文献，这是首次使用Inception-ResNet-v2作为单目深度估计的编码器，表明其性能优于之前的模型。Inception-ResNet-v2的使用使我们的模型能够有效地捕获通常难以预测的复杂对象和细粒度细节。此外，我们的模型结合了多尺度特征提取，以提高不同类型对象大小和距离的深度预测精度。我们提出了一种由深度损失、梯度边缘损失和SSIM损失组成的复合损失函数，其中对权重进行微调以优化加权和，确保深度估计不同方面的更好平衡。纽约大学深度V2数据集的实验结果表明，我们的模型达到了最先进的性能，ARE为0.064，RMSE为0.228，准确率（ $\delta$<1.25$ ）为89.3%。这些指标表明，即使在具有挑战性的情况下，我们的模型也能有效地预测深度，为机器人、3D重建和增强现实等现实世界的应用提供可扩展的解决方案。 et.al.|[2410.11610](http://arxiv.org/abs/2410.11610)|null|
|**2024-10-15**|**Multiview Scene Graph**|适当的场景表示是追求空间智能的核心，智能体可以稳健地重建并有效地理解3D场景。场景表示可以是度量，如3D重建中的地标图、对象检测中的3D边界框或占用预测中的体素网格，也可以是拓扑，如SLAM中具有循环闭包的姿态图或SfM中的可见性图。在这项工作中，我们建议从未涂胶的图像构建多视图场景图（MSG），用互连的位置和对象节点在拓扑上表示场景。构建MSG的任务对现有的表示学习方法来说是具有挑战性的，因为它需要联合解决视觉位置识别、对象检测和来自视野有限和潜在大视点变化的图像的对象关联问题。为了评估任何解决这一任务的方法，我们开发了一个基于公共3D数据集的MSG数据集和注释。我们还提出了一种基于MSG边联合得分交集的评估度量。此外，我们开发了一种基于主流预训练视觉模型的新基线方法，将视觉位置识别和对象关联结合到一个Transformer解码器架构中。实验证明，与现有的相关基线相比，我们的方法具有更优的性能。 et.al.|[2410.11187](http://arxiv.org/abs/2410.11187)|null|
|**2024-10-14**|**Cultural Heritage 3D Reconstruction with Diffusion Networks**|本文探讨了使用最新的生成式人工智能算法修复文化遗产，利用一个旨在有效重建3D点云的条件扩散模型。我们的研究评估了该模型在一般和文化遗产特定环境中的表现。结果表明，在考虑对象变异性的情况下，扩散模型可以准确地再现文化遗产的几何形状。尽管遇到了数据多样性和异常敏感性等挑战，但该模型在伪影恢复研究中显示出巨大的潜力。这项工作为使用人工智能技术推进古代文物的修复方法奠定了基础。 et.al.|[2410.10927](http://arxiv.org/abs/2410.10927)|null|
|**2024-10-14**|**3DArticCyclists: Generating Simulated Dynamic 3D Cyclists for Human-Object Interaction (HOI) and Autonomous Driving Applications**|人机交互（HOI）和人场景交互（HSI）对于体现人工智能（EAI）、机器人和增强现实（AR）中以人为中心的场景理解应用至关重要。这些研究领域面临的一个共同限制是数据稀缺问题：输入图像上标记的人类场景对象对不足，它们之间的交互复杂性和粒度有限。最近的HOI和HSI方法通过生成与刚性对象的动态交互来解决这个问题。但更复杂的动态交互，如人类骑手踩着铰接式自行车，尚未得到探索。为了解决这一局限性，并能够研究复杂的动态人体关节对象交互，本文提出了一种生成模拟的3D动态自行车手资产和交互的方法。我们设计了一种方法，用于创建一个新的基于零件的多视图铰接合成3D自行车数据集，我们称之为3DArticBikes，可用于训练基于NeRF和3DGS的3D重建方法。然后，我们提出了一种基于3DGS的参数化自行车组合模型，用于组装8自由度姿态可控的3D自行车。最后，使用来自骑车人视频的动态信息，我们通过重新设置一个可选择的合成3D人的姿势，同时使用提出的基于3D关键点优化的逆运动学姿势细化将骑车人自动放置在我们新的铰接式3D自行车上，从而构建一个完整的合成动态3D骑车人（骑自行车的骑车人）。我们展示了定性和定量结果，将我们生成的自行车与最近稳定的基于扩散的方法生成的自行车进行了比较。 et.al.|[2410.10782](http://arxiv.org/abs/2410.10782)|null|
|**2024-10-13**|**Magnituder Layers for Implicit Neural Representations in 3D**|提高3D中隐式神经表示的效率和性能，特别是神经辐射场（NeRF）和有符号距离场（SDF），对于在实时应用中使用它们至关重要。这些模型虽然能够生成逼真的新颖视图和详细的3D重建，但往往存在计算成本高和推理速度慢的问题。为了解决这个问题，我们引入了一种名为“magnituder”的新型神经网络层，旨在减少这些模型中的训练参数数量，同时不牺牲其表达能力。通过将放大器集成到标准前馈层堆栈中，我们提高了推理速度和适应性。此外，我们的方法通过无反向传播的分层知识转移，能够提高训练的隐式神经表示模型的零样本性能，从而在动态环境中实现更高效的场景重建。 et.al.|[2410.09771](http://arxiv.org/abs/2410.09771)|null|
|**2024-10-13**|**EchoPrime: A Multi-Video View-Informed Vision-Language Model for Comprehensive Echocardiography Interpretation**|超声心动图是使用最广泛的心脏成像技术，通过捕获超声视频数据来评估心脏的结构和功能。超声心动图中的人工智能（AI）有可能简化手动任务，提高再现性和准确性。然而，大多数超声心动图人工智能模型都是单视图、单任务系统，不能从全面检查期间捕获的多个视图中合成互补信息，从而导致性能和应用范围有限。为了解决这个问题，我们引入了EchoPrime，这是一个多视图、视图知情、基于视频的视觉语言基础模型，在1200多万个视频报告对上进行了训练。EchoPrime使用对比学习为全面的超声心动图研究中的所有标准视图训练一个统一的嵌入模型，同时表示罕见和常见的疾病和诊断。然后，EchoPrime利用视图分类和视图通知的解剖注意力模型来加权视频特定的解释，这些解释准确地映射了超声心动图视图和解剖结构之间的关系。通过检索增强解释，EchoPrime将所有超声心动图视频中的信息整合到一项综合研究中，并进行全面的临床超声心动图解释。在来自两个独立医疗保健系统的数据集中，EchoPrime在23个不同的心脏形态和功能基准上实现了最先进的性能，超过了特定任务方法和先前基础模型的性能。经过严格的临床评估，EchoPrime可以帮助医生对综合超声心动图进行自动化的初步评估。 et.al.|[2410.09704](http://arxiv.org/abs/2410.09704)|null|
|**2024-10-12**|**Improving 3D Finger Traits Recognition via Generalizable Neural Rendering**|手指特征的3D生物识别技术已成为一种新趋势，并展现出强大的识别和防伪能力。现有的方法遵循一个明确的3D管道，该管道首先重建模型，然后从3D模型中提取特征。然而，这些显式的3D方法存在以下问题：1）在3D重建过程中不可避免地会丢失信息；2） 特定硬件和3D重建算法之间的紧密耦合。这就引出了一个问题：在识别任务中明确重建3D信息是必不可少的吗？因此，我们以一种隐含的方式考虑这个问题，在神经辐射场（NeRFs）的帮助下，将神经损伤的3D重建问题留给可学习的神经网络。我们提出了FingerNeRF，这是一种用于3D手指生物识别的新型通用NeRF。为了处理可能导致不正确3D几何的形状辐射模糊问题，我们的目标是基于指纹或手指静脉等二元手指特征的对应关系引入额外的几何先验。首先，我们提出了一种新的特征引导变换器（TGT）模块，以增强手指特征引导的特征对应性。其次，我们通过提出的深度蒸馏损失和特征引导渲染损失对体绘制损失进行了额外的几何约束。为了评估所提出的方法在不同模态上的性能，我们收集了两个新的数据集：带有手指图像的SCUT-Finger-3D和带有手指静脉图像的SCUT FingerVein-3D。此外，我们还利用带有指纹图像的UNSW-3D数据集进行评估。在实验中，我们的FingerNeRF在SCUT-Phenger-3D数据集上可以实现4.37%的EER，在SCUT-FhengerVein-3D数据集上实现8.12%的EER和在UNSW-3D数据集中实现2.90%的EER。这表明了所提出的隐式方法在3D手指生物识别中的优越性。 et.al.|[2410.09582](http://arxiv.org/abs/2410.09582)|null|
|**2024-10-12**|**Neurally Integrated Finite Elements for Differentiable Elasticity on Evolving Domains**|我们提出了一种用于定义为演化隐函数的域的弹性模拟器，该模拟器在形状和材料方面都是高效、鲁棒和可微的。该模拟器的动机是3D重建中的应用：从观察到的图像中恢复几何体作为隐式函数越来越有效，但物理应用需要精确模拟和优化这些形状在变形下的行为，这仍然具有挑战性。我们的关键技术创新是训练一个小型神经网络来拟合交点，以便在隐式网格单元上进行鲁棒的数值积分。当与混合有限元公式结合时，这会产生一个平滑、完全可微的模拟模型，将下伏隐式表面的演变与其弹性响应联系起来。我们展示了我们的方法在隐式正向模拟、编辑过程中直接模拟3D形状以及结合可微渲染的新型基于物理的形状和拓扑优化方面的有效性。 et.al.|[2410.09417](http://arxiv.org/abs/2410.09417)|null|

<p align=right>(<a href=#updated-on-20241016>back to top</a>)</p>

## Diffusion

|Publish Date|Title|Abstract|PDF|Code|
|---|---|---|---|---|
|**2024-10-15**|**High-Resolution Frame Interpolation with Patch-based Cascaded Diffusion**|尽管最近取得了进展，但现有的帧插值方法仍然难以处理极高分辨率的输入和处理重复纹理、薄对象和大运动等具有挑战性的情况。为了解决这些问题，我们引入了一种基于补丁的级联像素扩散模型HiFI用于帧插值，该模型在这些场景中表现出色，同时在标准基准测试中实现了具有竞争力的性能。级联可以生成从低到高分辨率的一系列图像，可以显著帮助处理大型或复杂的运动，这些运动既需要粗略解决方案的全局上下文，也需要高分辨率输出的详细上下文。然而，与先前关于级联扩散模型的工作相反，级联扩散模型在越来越大的分辨率下执行扩散，我们使用一个始终以相同分辨率执行扩散的单一模型，并通过处理输入和先验解的补丁来进行上采样。我们证明，这种技术大大减少了推理时的内存使用，也允许我们在测试时使用单个模型，解决了帧插值和空间上采样问题，节省了训练成本。我们发现，HiFI对需要全局上下文的高分辨率和复杂重复纹理有显著帮助。HiFI在多个基准测试（Vimeo、Xiph、X-Test、SEPE-8K）上表现出相当或超越最先进的性能。在我们新推出的专注于特别具有挑战性的案例的数据集上，HiFI在这些案例上也明显优于其他基线。请访问我们的项目页面查看视频结果：https://hifi-diffusion.github.io et.al.|[2410.11838](http://arxiv.org/abs/2410.11838)|null|
|**2024-10-15**|**On the Effectiveness of Dataset Alignment for Fake Image Detection**|随着潜在扩散模型（LDM）使图像生成能力民主化，检测假图像的需求越来越大。一个好的检测器应该专注于生成模型指纹，而忽略图像属性，如语义内容、分辨率、文件格式等。假图像检测器通常是以数据驱动的方式构建的，其中模型被训练来区分真实图像和假图像。现有工作主要研究网络架构选择和训练配方。在这项工作中，我们认为，除了这些算法选择外，我们还需要一个对齐良好的真实/虚假图像数据集来训练一个强大的检测器。对于LDM家族，我们提出了一种非常简单的方法来实现这一点：我们使用LDM自动编码器重建所有真实图像，而无需任何去噪操作。然后，我们训练一个模型，将这些真实图像与其重建图像分开。以这种方式创建的假货在几乎所有方面（例如大小、纵横比、语义内容）都与真实假货极其相似，这迫使模型寻找LDM解码器伪影。我们实证表明，这种创建对齐的真实/虚假数据集的方法，也避开了计算上昂贵的去噪过程，有助于构建一个不太关注虚假相关性的检测器，这是一种非常流行的现有方法容易受到的影响。最后，为了证明数据集中的对齐有多有效，我们使用非自然物体的图像构建了一个检测器，并呈现了有希望的结果。总的来说，我们的工作确定了训练假图像检测器时出现的微妙但重要的问题，并提出了一种简单而廉价的解决方案来解决这些问题。 et.al.|[2410.11835](http://arxiv.org/abs/2410.11835)|null|
|**2024-10-15**|**Bayesian Experimental Design via Contrastive Diffusions**|贝叶斯最优实验设计（BOED）是一种强大的工具，可以降低运行一系列实验的成本。当基于预期信息增益（EIG）时，设计优化对应于先验和后验分布之间一些难以处理的预期对比度的最大化。由于BOED固有的计算复杂性，将这种最大化扩展到高维和复杂的设置一直是一个问题。在这项工作中，我们引入了一种具有成本效益采样特性的{\it expected posterior}分布，并通过新的EIG梯度表达式提供了一种易于处理的EIG对比度最大化方法。基于扩散的采样器用于计算预期后验的动力学，并利用双层优化的思想来推导一个有效的联合采样优化循环，而无需诉诸EIG的下限近似。由此产生的效率增益允许将BOED扩展到经过充分测试的扩散模型的生成能力。通过将生成模型纳入BOED框架，我们扩大了其范围，并在以前不切实际的场景中使用。数值实验和与最新方法的比较表明了该方法的潜力。 et.al.|[2410.11826](http://arxiv.org/abs/2410.11826)|null|
|**2024-10-15**|**Improving Long-Text Alignment for Text-to-Image Diffusion Models**|文本到图像（T2I）扩散模型的快速发展使它们能够从给定的文本中生成前所未有的结果。然而，随着文本输入变得更长，现有的编码方法（如CLIP）面临局限性，将生成的图像与长文本对齐变得具有挑战性。为了解决这些问题，我们提出了LongAlign，它包括一种用于处理长文本的分段级编码方法和一种用于有效对齐训练的分解偏好优化方法。对于分段级编码，长文本被划分为多个分段并分别处理。该方法克服了预训练编码模型的最大输入长度限制。为了优化偏好，我们提供了基于CLIP的分解偏好模型来微调扩散模型。具体来说，为了利用基于CLIP的偏好模型进行T2I比对，我们深入研究了它们的评分机制，发现偏好评分可以分解为两个部分：一个是衡量T2I比对的文本相关部分，另一个是评估人类偏好的其他视觉方面的文本无关部分。此外，我们发现文本无关部分在微调过程中会导致一个常见的过拟合问题。为了解决这个问题，我们提出了一种重新加权策略，为这两个组件分配不同的权重，从而减少过拟合并增强对齐。在使用我们的方法对512 $稳定扩散（SD）v1.5进行约20小时的微调后，微调后的SD在T2I对齐方面表现优于更强的基础模型，如PixArt-$\alpha$ 和Kandinsky v2.2。该代码可在以下网址获得https://github.com/luping-liu/LongAlign. et.al.|[2410.11817](http://arxiv.org/abs/2410.11817)|null|
|**2024-10-15**|**SGEdit: Bridging LLM with Text2Image Generative Model for Scene Graph-based Image Editing**|场景图提供了一种结构化的、层次化的图像表示，节点和边象征着对象及其之间的关系。它可以作为图像编辑的自然界面，大大提高了精度和灵活性。利用这一优势，我们引入了一个新的框架，将大型语言模型（LLM）与Text2Image生成模型集成在一起，用于基于场景图的图像编辑。这种集成可以在对象级别进行精确修改，并在不损害整体图像完整性的情况下对场景进行创造性重组。我们的方法包括两个主要阶段：1）利用LLM驱动的场景解析器，我们构建图像的场景图，捕获关键对象及其相互关系，以及解析对象掩码和描述等细粒度属性。这些注释通过微调的扩散模型促进概念学习，用优化的令牌和详细的描述提示表示每个对象。2） 在图像编辑阶段，LLM编辑控制器将编辑引导到特定区域。然后，这些编辑由注意力调制扩散编辑器实现，利用微调模型执行对象添加、删除、替换和调整。通过广泛的实验，我们证明我们的框架在编辑精度和场景美学方面明显优于现有的图像编辑方法。 et.al.|[2410.11815](http://arxiv.org/abs/2410.11815)|null|
|**2024-10-15**|**Random walks with long-range memory on networks**|我们研究了任意网络上具有长程记忆的精确可解随机游走模型。步行者对最近的邻居节点执行无偏的随机步骤，并以优先的方式间歇地重置为之前访问过的节点，这样访问最多的节点按比例有更高的概率被选择重新访问。占用概率可以表示为网络标准随机游走矩阵的本征模之和，其中振幅在大时间内按照幂律缓慢衰减，而不是呈指数衰减。静止状态与没有记忆时相同，并且实现了详细的平衡。然而，瞬态部分的弛豫在后期变得非常自组织，因为它由一个幂律主导，该幂律的指数取决于第二大特征值和重置概率。我们将我们的发现应用于有限网络，如环、全图、Watts Strogatz和Barab’asi-Albert随机网络或Barbell图。我们的研究将之前考虑一维受限扩散粒子的优先模型扩展到网络几何，并可能对模拟复杂系统中的传输现象感兴趣，如人类流动、流行病传播或动物觅食。 et.al.|[2410.11814](http://arxiv.org/abs/2410.11814)|null|
|**2024-10-15**|**Efficient Diffusion Models: A Comprehensive Survey from Principles to Practices**|作为近年来最受欢迎和追捧的生成模型之一，扩散模型凭借其密集的理论原理和可靠的应用实践，引发了许多研究人员的兴趣，并在图像合成、视频生成、分子设计、3D场景渲染和多模态生成等各种生成任务中稳步显示出优异的优势。最近在扩散模型方面取得的显著成功主要来自渐进式设计原则和高效的架构、训练、推理和部署方法。然而，还没有对这些原则和实践进行全面深入的总结，以帮助快速理解和应用扩散模型。在这项调查中，我们为这些现有的努力提供了一个新的以效率为导向的视角，主要关注架构设计、模型训练、快速推理和可靠部署中的深刻原则和有效实践，以读者友好的方式指导新场景的进一步理论研究、算法迁移和模型应用。\url{https://github.com/ponyzym/Efficient-DMs-Survey} et.al.|[2410.11795](http://arxiv.org/abs/2410.11795)|null|
|**2024-10-15**|**Solving The Dynamic Volatility Fitting Problem: A Deep Reinforcement Learning Approach**|波动率拟合是股票衍生品业务的核心问题之一。通过一组确定性规则，定义了隐含波动率表面编码（参数化、密度、扩散）的自由度。虽然这种方法非常有效，但在行业中广泛使用的这种方法并不是为从市场制度的变化中学习并发现未被怀疑的最佳行为而量身定制的。本文改变了经典范式，应用深度强化学习（DRL）的最新进展来解决拟合问题。特别是，我们证明了深度确定性策略梯度（DDPG）和软行动者批判（SAC）的变体至少可以实现与标准拟合算法一样好的效果。此外，我们解释了为什么强化学习框架适合处理复杂的目标函数，并且天生适用于在线学习。 et.al.|[2410.11789](http://arxiv.org/abs/2410.11789)|null|
|**2024-10-15**|**Measure estimation on a manifold explored by a diffusion process**|从无边界紧连接 $d$维流形$M$上的扩散路径$（X_t）_{t\in[0，t]}$的观察出发，我们考虑了估计过程平稳测度$mu$的问题。Wang和Zhu（2023）表明，对于Wasserstein度量$W_2$和$d\ge 5$，当$（X_T）_{T\in[0，T]}$是朗之万扩散时，路径$（X_ T）_{T\in[0]，T]}的占用度量达到了$T^{-1/（d-2）}$的收敛速度。我们在几个方向上扩展了他们的结果。首先，我们证明了收敛速度适用于一大类扩散路径，其生成器是一致椭圆的。其次，可以利用平稳测度$\mu$的密度$p$相对于体积测度$M$的规律性来获得更快的估计值：当$p$属于阶数$\ell>0$的Sobolev空间时，通过与核卷积平滑占用测度会得到一个收敛速度为$T^{-（\ell+1）/（2\ell+d-2）}$ 的估计值。我们进一步证明，该速率是该问题的最小最大估计速率。 et.al.|[2410.11777](http://arxiv.org/abs/2410.11777)|null|
|**2024-10-15**|**Probabilistic Principles for Biophysics and Neuroscience: Entropy Production, Bayesian Mechanics & the Free-Energy Principle**|本文主要研究生物系统的三个基本方面；即熵产生、贝叶斯力学和自由能原理。贡献有三方面：1）我们计算了比以前更大一类系统的熵产生，包括几乎任何平稳的扩散过程，例如退化扩散，其中驱动噪声不会作用于系统的所有坐标。重要的是，这类系统包括由有色噪声驱动的随机微分方程的马尔可夫近似，这一点很重要，因为宏观和中观尺度的生物系统通常会受到有色波动的影响。2） 我们为与环境相互作用的生物和物理实体开发了一种贝叶斯力学，在这种力学中，我们给出了事物内部状态推断其外部状态的充分必要条件，这与统计学和理论神经科学中的变分贝叶斯推断相一致。3） 我们改进了贝叶斯力学的约束，以获得更具体的生物系统描述，称为自由能原理。这表明，生物系统的活跃状态和内部状态表现为自由能的最小化。这里提出的自由能原理的数学基础，通过在外部和感觉状态的生成模型下最小化自由能，解锁了神经生物学和人工智能中建模和模拟行为的第一原理方法。 et.al.|[2410.11735](http://arxiv.org/abs/2410.11735)|null|

<p align=right>(<a href=#updated-on-20241016>back to top</a>)</p>

## NeRF

|Publish Date|Title|Abstract|PDF|Code|
|---|---|---|---|---|
|**2024-10-07**|**Fast Training of Sinusoidal Neural Fields via Scaling Initialization**|神经场是一种新兴的范式，它将数据表示为由神经网络参数化的连续函数。尽管有许多优点，但神经场通常具有较高的训练成本，这阻碍了更广泛的采用。在本文中，我们关注一个流行的神经场家族，称为正弦神经场（SNF），并研究如何初始化它以最大限度地提高训练速度。我们发现，基于信号传播原理设计的SNF标准初始化方案是次优的。特别是，我们证明，通过简单地将每个权重（最后一层除外）乘以一个常数，我们可以将SNF训练加速10 $\times$。这种方法被称为$\textit{weight scaling}$ ，在各种数据域上持续提供显著的加速，使SNF的训练速度比最近提出的架构更快。为了理解为什么权重缩放效果良好，我们进行了广泛的理论和实证分析，结果表明，权重缩放不仅有效地解决了频谱偏差，而且具有良好的优化轨迹。 et.al.|[2410.04779](http://arxiv.org/abs/2410.04779)|null|
|**2024-10-04**|**End-to-End Reaction Field Energy Modeling via Deep Learning based Voxel-to-voxel Transform**|在计算生物化学和生物物理学中，理解静电相互作用的作用对于阐明生物分子的结构、动力学和功能至关重要。泊松-玻尔兹曼（PB）方程是通过描述带电分子内部和周围的静电势来模拟这些相互作用的基础工具。然而，由于生物分子表面的复杂性和需要考虑可移动离子，求解PB方程带来了重大的计算挑战。虽然求解PB方程的传统数值方法是准确的，但它们的计算成本很高，并且随着系统规模的增加而扩展性较差。为了应对这些挑战，我们引入了PBNeF，这是一种新的机器学习方法，灵感来自基于神经网络的偏微分方程求解器的最新进展。我们的方法将PB方程的输入和边界静电条件转化为可学习的体素表示，使神经场变换器能够预测PB解，进而预测反应场势能。大量实验表明，与传统的PB求解器相比，PBNeF的速度提高了100倍以上，同时保持了与广义玻恩（GB）模型相当的精度。 et.al.|[2410.03927](http://arxiv.org/abs/2410.03927)|null|
|**2024-10-08**|**DressRecon: Freeform 4D Human Reconstruction from Monocular Video**|我们提出了一种从单目视频中重建时间一致的人体模型的方法，重点是极其宽松的衣服或手持物体的交互。之前在人体重建方面的工作要么局限于没有物体交互的紧身衣服，要么需要校准的多视图捕捉或个性化的模板扫描，而大规模收集这些数据成本很高。我们对高质量但灵活的重建的关键见解是，将关于关节体形状的通用人类先验（从大规模训练数据中学习）与视频特定的关节“骨骼袋”变形（通过测试时间优化适合单个视频）仔细结合。我们通过学习一个神经隐式模型来实现这一点，该模型将身体和衣服的变形作为单独的运动模型层来解开。为了捕捉服装的微妙几何形状，我们在优化过程中利用了基于图像的先验，如人体姿势、表面法线和光流。由此产生的神经场可以提取到时间一致的网格中，或进一步优化为显式3D高斯分布，以实现高保真交互式渲染。在具有高度挑战性的服装变形和物体交互的数据集上，DressReston可以产生比现有技术更高保真的3D重建。项目页面：https://jefftan969.github.io/dressrecon/ et.al.|[2409.20563](http://arxiv.org/abs/2409.20563)|null|
|**2024-09-25**|**TalkinNeRF: Animatable Neural Fields for Full-Body Talking Humans**|我们介绍了一种新的框架，该框架从单眼视频中学习全身说话的人的动态神经辐射场（NeRF）。之前的工作只代表身体姿势或面部。然而，人类通过全身进行交流，结合身体姿势、手势和面部表情。在这项工作中，我们提出了TalkinNeRF，这是一个基于NeRF的统一网络，代表了整体4D人体运动。给定一个受试者的单眼视频，我们学习身体、面部和手的相应模块，这些模块结合在一起生成最终结果。为了捕捉复杂的手指关节，我们学习了手的额外变形场。我们的多身份表示能够同时训练多个科目，以及在完全看不见的姿势下进行强大的动画。只要输入一段短视频，它也可以推广到新的身份。我们展示了最先进的性能，用于为全身说话的人类制作动画，具有精细的手部发音和面部表情。 et.al.|[2409.16666](http://arxiv.org/abs/2409.16666)|null|
|**2024-09-24**|**Generative 3D Cardiac Shape Modelling for In-Silico Trials**|我们提出了一种深度学习方法，基于将形状表示为神经有符号距离场的零级集，对合成主动脉形状进行建模和生成，该方法受一系列可训练的嵌入向量的约束，并对每个形状的几何特征进行编码。通过使神经场在采样表面点上消失并强制其空间梯度具有单位范数，在从CT图像重建的主动脉根部网格数据集上训练网络。实证结果表明，我们的模型可以高保真地表示主动脉形状。此外，通过从学习到的嵌入向量中采样，我们可以生成类似于真实患者解剖结构的新形状，可用于计算机模拟试验。 et.al.|[2409.16058](http://arxiv.org/abs/2409.16058)|null|
|**2024-09-21**|**MOSE: Monocular Semantic Reconstruction Using NeRF-Lifted Noisy Priors**|由于缺乏几何指导和不完美的视图相关2D先验，从单眼图像中精确重建密集和语义注释的3D网格仍然是一项具有挑战性的任务。尽管我们已经见证了隐式神经场景表示的最新进展，能够简单地从多视图图像中进行精确的2D渲染，但很少有研究仅使用单眼先验来解决3D场景理解问题。在本文中，我们提出了MOSE，这是一种神经场语义重建方法，可以将推断的图像级噪声先验提升到3D，在3D和2D空间中产生精确的语义和几何。我们方法的关键动机是利用通用类不可知的分段掩码作为指导，在训练过程中促进渲染语义的局部一致性。在语义的帮助下，我们进一步将平滑正则化应用于无纹理区域，以获得更好的几何质量，从而实现几何和语义的互惠互利。在ScanNet数据集上的实验表明，我们的MOSE在3D语义分割、2D语义分割和3D表面重建任务的所有指标上都优于相关基线。 et.al.|[2409.14019](http://arxiv.org/abs/2409.14019)|null|
|**2024-09-17**|**SplatFields: Neural Gaussian Splats for Sparse 3D and 4D Reconstruction**|从多视图图像中数字化3D静态场景和4D动态事件长期以来一直是计算机视觉和图形学领域的一个挑战。最近，3D高斯散斑（3DGS）已经成为一种实用且可扩展的重建方法，由于其令人印象深刻的重建质量、实时渲染能力以及与广泛使用的可视化工具的兼容性而越来越受欢迎。然而，该方法需要大量的输入视图来实现高质量的场景重建，这引入了一个重大的实际瓶颈。在捕捉动态场景时，这一挑战尤为严峻，因为部署广泛的相机阵列的成本可能高得令人望而却步。在这项工作中，我们发现斑点特征缺乏空间自相关性是导致3DGS技术在稀疏重建环境中性能不佳的因素之一。为了解决这个问题，我们提出了一种优化策略，通过将splat特征建模为相应隐式神经场的输出，有效地正则化splat特征。这导致在各种场景中重建质量的一致提高。我们的方法有效地处理了静态和动态情况，这在不同设置和场景复杂性的广泛测试中得到了证明。 et.al.|[2409.11211](http://arxiv.org/abs/2409.11211)|null|
|**2024-10-02**|**Neural Fields for Adaptive Photoacoustic Computed Tomography**|光声计算机断层扫描（PACT）是一种具有广泛医学应用的非侵入性成像技术。传统的PACT图像重建算法受到组织中声速不均匀（SOS）引起的波前失真的影响，导致图像质量下降。考虑到这些影响可以提高图像质量，但测量SOS分布的实验成本很高。另一种方法是仅使用PA信号对初始压力图像和SOS进行联合重建。现有的关节重建方法存在局限性：计算成本高，无法直接恢复SOS，以及依赖于不准确的简化假设。隐式神经表示或神经场是计算机视觉中的一种新兴技术，用于通过基于坐标的神经网络学习物理场的有效和连续表示。在这项工作中，我们介绍了NF-APACT，这是一种高效的自监督框架，利用神经场来估计SOS，以实现准确和鲁棒的多通道解卷积。我们的方法比现有方法更快、更准确地消除了SOS像差。我们在一个新的数值体模以及实验收集的体模和体内数据上证明了我们的方法的成功。我们的代码和数字幻影可在https://github.com/Lukeli0425/NF-APACT. et.al.|[2409.10876](http://arxiv.org/abs/2409.10876)|null|
|**2024-09-09**|**Lagrangian Hashing for Compressed Neural Field Representations**|我们提出了拉格朗日散列，这是一种神经场的表示，结合了依赖于欧拉网格（即~InstantNGP）的快速训练NeRF方法的特征，以及使用配备有特征的点作为表示信息的方法（例如3D高斯散点或PointNeRF）。我们通过将基于点的表示合并到InstantNGP表示的分层哈希表的高分辨率层中来实现这一点。由于我们的点具有影响域，我们的表示可以被解释为哈希表中存储的高斯混合。我们提出的损失鼓励我们的高斯人向需要更多代表预算才能充分代表的地区移动。我们的主要发现是，我们的表示允许使用更紧凑的表示来重建信号，而不会影响质量。 et.al.|[2409.05334](http://arxiv.org/abs/2409.05334)|null|
|**2024-09-08**|**Exploring spectropolarimetric inversions using neural fields. Solar chromospheric magnetic field under the weak-field approximation**|全斯托克斯偏振数据集来源于狭缝光谱仪或窄带滤光片图，如今已被常规采集。随着二维光谱偏振仪和允许长时间高质量观测序列的观测技术的出现，数据速率正在增加。在光谱偏振反演中，显然需要通过利用推断物理量的时空相干性来超越传统的逐像素策略。我们探索了神经网络作为时间和空间（也称为神经场）上物理量的连续表示的潜力，用于光谱极化反演。我们已经实现并测试了一个神经场，以在弱场近似（WFA）下执行磁场矢量的推理（也称为物理知情神经网络的方法）。通过使用神经场来描述磁场矢量，我们可以通过假设物理量是坐标的连续函数来在空间和时间域中正则化解。我们研究了Ca II 8542 A谱线的合成和真实观测结果。我们还探讨了其他显式正则化的影响，例如使用外推磁场的信息或色球原纤维的取向。与传统的逐像素反演相比，神经场方法提高了磁场矢量重建的保真度，特别是横向分量。这种隐式正则化是一种提高观测值有效信噪比的方法。虽然它比逐像素WFA估计慢，但这种方法通过减少自由参数的数量并在解决方案中引入时空约束，显示出深度分层反演的巨大潜力。 et.al.|[2409.05156](http://arxiv.org/abs/2409.05156)|**[link](https://github.com/cdiazbas/neural_wfa)**|

<p align=right>(<a href=#updated-on-20241016>back to top</a>)</p>

[contributors-shield]: https://img.shields.io/github/contributors/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[contributors-url]: https://github.com/Vincentqyw/cv-arxiv-daily/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[forks-url]: https://github.com/Vincentqyw/cv-arxiv-daily/network/members
[stars-shield]: https://img.shields.io/github/stars/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[stars-url]: https://github.com/Vincentqyw/cv-arxiv-daily/stargazers
[issues-shield]: https://img.shields.io/github/issues/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[issues-url]: https://github.com/Vincentqyw/cv-arxiv-daily/issues

