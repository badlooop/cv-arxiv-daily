[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]

## Updated on 2025.01.02
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
|**2024-12-30**|**KeyGS: A Keyframe-Centric Gaussian Splatting Method for Monocular Image Sequences**|从稀疏的2D图像重建高质量的3D模型在计算机视觉领域引起了广泛关注。最近，3D高斯散斑（3DGS）因其具有高效训练速度和实时渲染能力的显式表示而受到关注。然而，现有的方法仍然严重依赖于精确的相机姿态进行重建。尽管最近的一些方法试图在没有单目视频数据集的运动结构（SfM）预处理的情况下训练3DGS模型，但这些方法训练时间较长，使其在许多应用中不切实际。在本文中，我们提出了一种无需任何深度或匹配模型即可运行的高效框架。我们的方法最初使用SfM在几秒钟内快速获得粗略的相机姿态，然后通过利用3DGS中的密集表示来细化这些姿态。该框架有效地解决了训练时间长的问题。此外，我们将致密化过程与接头细化相结合，提出了一种从粗到细的频率感知致密化方法，以重建不同层次的细节。这种方法可以防止相机姿态估计因高频信号而陷入局部最小值或漂移。与之前的方法相比，我们的方法将训练时间从数小时显著缩短到数分钟，同时实现了更准确的新视图合成和相机姿态估计。 et.al.|[2412.20767](http://arxiv.org/abs/2412.20767)|null|
|**2024-12-30**|**Dialogue Director: Bridging the Gap in Dialogue Visualization for Multimodal Storytelling**|人工智能驱动的故事讲述的最新进展增强了视频生成和故事可视化。然而，由于剧本细节有限、对物理背景的理解不足以及整合电影原则的复杂性，将以对话为中心的剧本翻译成连贯的故事板仍然是一个重大挑战。为了应对这些挑战，我们提出了对话可视化，这是一项将对话脚本转换为动态多视图故事板的新任务。我们介绍Dialogue Director，这是一个无需培训的多模式框架，由脚本导演、摄影师和故事板制作人组成。该框架利用大型多模态模型和基于扩散的架构，采用思维链推理、检索增强生成和多视图合成等技术来提高脚本理解、物理上下文理解和电影知识集成。实验结果表明，对话导演在剧本解读、物理世界理解和电影原理应用方面优于最先进的方法，显著提高了基于对话的故事可视化的质量和可控性。 et.al.|[2412.20725](http://arxiv.org/abs/2412.20725)|null|
|**2024-12-30**|**4D Gaussian Splatting: Modeling Dynamic Scenes with Native 4D Primitives**|动态3D场景表示和从捕获的视频中合成新颖的视图对于实现AR/VR和元宇宙应用程序所需的沉浸式体验至关重要。然而，由于不受约束的现实世界场景及其时间动态的复杂性，这项任务具有挑战性。在本文中，我们将动态场景构建为一个时空4D体积学习问题，提供了一个对运动假设最小的原生显式重新表述，这是一个通用的动态场景学习框架。具体来说，我们使用一组具有显式几何和外观特征的4D高斯基元来表示目标动态场景，称为4D高斯飞溅（4DGS）。这种方法可以通过拟合底层时空体积来捕获空间和时间中的相关信息。使用由各向异性椭圆参数化的4D高斯模型将时空建模为一个整体，这些椭圆可以在空间和时间上任意旋转，我们的模型可以自然地学习具有4D球谐函数的视图相关和时间演化外观。值得注意的是，我们的4DGS模型是第一个支持实时渲染复杂动态场景的高分辨率、照片级真实感新颖视图的解决方案。为了提高效率，我们推出了几个紧凑的变体，有效地减少了内存占用，降低了过拟合的风险。广泛的实验验证了4DGS在一系列动态场景相关任务（如新颖的视图合成、4D生成、场景理解）和场景（如单个对象、室内场景、驾驶环境、合成和真实数据）的视觉质量和效率方面的优越性。 et.al.|[2412.20720](http://arxiv.org/abs/2412.20720)|null|
|**2024-12-29**|**MaskGaussian: Adaptive 3D Gaussian Representation from Probabilistic Masks**|虽然3D高斯散点（3DGS）在新颖的视图合成和实时渲染方面表现出了卓越的性能，但由于使用了数百万高斯分布而导致的高内存消耗限制了它的实用性。为了缓解这个问题，通过手工制定标准或使用学习到的掩码来修剪不必要的高斯分布，从而做出了改进。然而，这些方法基于修剪时刻的快照确定性地去除高斯分布，从长远来看，导致重建性能次优。为了解决这个问题，我们引入了MaskGaussian，它将高斯模型建模为概率实体，而不是永久删除它们，并根据它们的存在概率来使用它们。为了实现这一点，我们提出了一种掩码光栅化技术，该技术使未使用但概率上存在的高斯人能够接收梯度，从而动态评估他们对不断发展的场景的贡献，并调整他们的存在概率。因此，高斯分布的重要性会迭代变化，修剪后的高斯分布会被不同地选择。大量实验证明，与之前的修剪方法相比，所提出的方法在减少高斯分布的情况下实现了更好的渲染质量，平均修剪了60%以上的高斯分布，PSNR仅下降了0.02。我们的代码可以在以下网址找到：https://github.com/kaikai23/MaskGaussian et.al.|[2412.20522](http://arxiv.org/abs/2412.20522)|null|
|**2024-12-27**|**Dust to Tower: Coarse-to-Fine Photo-Realistic Scene Reconstruction from Sparse Uncalibrated Images**|在实践中，从稀疏视图、未校准的图像重建逼真的场景是非常必要的。尽管已经取得了一些成功，但现有的方法要么是稀疏视图，但需要精确的相机参数（即内在和外在参数），要么是无SfM，但需要密集捕获的图像。为了结合这两种方法的优点，同时解决各自的弱点，我们提出了Dust To Tower（D2T），这是一种准确有效的粗到细框架，可以从稀疏和未校准的图像中同时优化3DGS和图像姿态。我们的关键思想是首先有效地构建一个粗略的模型，然后在新的视角下使用扭曲和修复的图像对其进行细化。为此，我们首先引入了一个粗略构造模块（CCM），该模块利用快速的多视图立体模型来初始化3D高斯散点（3DGS）并恢复初始相机姿态。为了在新的视角下优化3D模型，我们提出了一个置信度感知深度对齐（CADA）模块，通过将置信度部分与单深度模型的估计深度对齐来优化粗略的深度图。然后，提出了一种扭曲图像引导内涂（WIGI）模块，通过精细的深度图将训练图像扭曲到新的视点，并应用修复来填补由视图方向变化引起的扭曲图像中的“洞”，提供高质量的监督，以进一步优化3D模型和相机姿态。广泛的实验和消融研究证明了D2T及其设计选择的有效性，在保持高效率的同时，在新的视图合成和姿态估计任务中实现了最先进的性能。代码将公开可用。 et.al.|[2412.19518](http://arxiv.org/abs/2412.19518)|null|
|**2024-12-27**|**Learning Radiance Fields from a Single Snapshot Compressive Image**|本文探讨了快照压缩成像（SCI）技术从单个时间压缩图像中恢复底层3D场景结构的潜力。SCI是一种经济高效的方法，它能够使用低成本的2D成像传感器将高维数据（如高光谱或时间信息）记录到单个图像中。为了实现这一点，通常会采用一系列专门设计的2D掩模，降低存储和传输要求，并提供潜在的隐私保护。受此启发，我们进一步利用神经辐射场（NeRF）强大的3D场景表示能力来恢复编码的3D场景信息。具体来说，我们提出了SCINeRF，其中我们将SCI的物理成像过程作为NeRF训练的一部分，使我们能够利用其在捕捉复杂场景结构方面的出色性能。此外，我们进一步整合了流行的3D高斯散点（3DGS）框架，并提出了SCISplat，通过将点云明确优化为3D高斯表示来提高3D场景重建质量和训练/渲染速度。为了评估我们方法的有效性，我们使用SCI系统捕获的合成数据和真实数据进行了广泛的评估。实验结果表明，我们提出的方法在图像重建和新颖的视图合成方面超越了最先进的方法。此外，我们的方法还通过利用SCI和3DGS的渲染能力，实时渲染高帧率多视图一致图像。代码可在以下网址获得：https://github.com/WU-CVGL/SICSPLAT。 et.al.|[2412.19483](http://arxiv.org/abs/2412.19483)|null|
|**2024-12-30**|**DriveEditor: A Unified 3D Information-Guided Framework for Controllable Object Editing in Driving Scenes**|以视觉为中心的自动驾驶系统需要多样化的数据进行稳健的训练和评估，可以通过操纵现有场景捕获中的对象位置和外观来增强。虽然扩散模型的最新进展在视频编辑方面显示出了希望，但由于位置控制不精确和难以保持高保真对象外观，它们在驾驶场景中的对象操纵应用仍然具有挑战性。为了解决位置和外观控制方面的这些挑战，我们引入了DriveEditor，这是一个基于扩散的框架，用于驾驶视频中的对象编辑。DriveEditor为全面的对象编辑操作提供了一个统一的框架，包括重新定位、替换、删除和插入。这些不同的操作都是通过一组共享的不同输入来实现的，这些输入由相同的位置控制和外观维护模块处理。位置控制模块在保留深度信息的同时投影给定的3D边界框，并将其分层注入扩散过程中，从而能够精确控制对象的位置和方向。外观维护模块通过采用三层方法来保持与单个参考图像的一致属性：低级细节保留、高级语义维护和来自新颖视图合成模型的3D先验的集成。对nuScenes数据集的广泛定性和定量评估表明，DriveEditor在生成各种驾驶场景编辑方面具有出色的保真度和可控性，并且具有促进下游任务的显著能力。项目页面：https://yvanliang.github.io/DriveEditor. et.al.|[2412.19458](http://arxiv.org/abs/2412.19458)|**[link](https://github.com/yvanliang/DriveEditor)**|
|**2024-12-26**|**BeSplat -- Gaussian Splatting from a Single Blurry Image and Event Stream**|辐射场方法的发展极大地增强了新的视图合成。3D高斯散斑（3DGS）的引入有效地解决了关键挑战，如训练时间长和渲染速度慢，这通常与神经辐射场（NeRF）有关，同时保持了高质量的重建。在这项工作（BeSplat）中，我们演示了从单个运动模糊图像及其相应的事件流中恢复清晰的辐射场（高斯斑点）。我们的方法通过高斯散斑联合学习场景表示，并通过贝塞尔SE（3）公式有效地恢复相机运动，最大限度地减少模糊图像和相应事件流的合成测量值与真实世界测量值之间的差异。我们在合成和真实数据集上评估了我们的方法，展示了它从学习到的辐射场和估计的相机轨迹中渲染视图一致、清晰图像的能力。据我们所知，我们的工作是第一个在高斯散布框架中解决这一极具挑战性的病态问题的工作，该框架有效地结合了使用事件流捕获的时间信息。 et.al.|[2412.19370](http://arxiv.org/abs/2412.19370)|null|
|**2024-12-26**|**Reflective Gaussian Splatting**|由于基于NeRF和3DGS的方法越来越强大，新型视图合成技术取得了重大进展。然而，反射对象重建仍然具有挑战性，缺乏一种适当的解决方案来实现实时、高质量的渲染，同时适应相互反射。为了填补这一空白，我们引入了一个反射高斯飞溅（\textbf{Ref-Gausian}）框架，该框架由两个部分组成：（I）基于物理的延迟渲染}，通过公式化分裂和近似，为渲染方程赋予像素级材质属性；（II） {\em高斯接地互反射}首次在高斯溅射范式内实现了所需的互反射功能。为了增强几何建模，我们进一步引入了材料感知的法线传播和初始的每高斯着色阶段，以及2D高斯基元。在标准数据集上进行的大量实验表明，Ref-Gassian在定量指标、视觉质量和计算效率方面优于现有方法。此外，我们表明，我们的方法可以作为反射和非反射场景的统一解决方案，超越了之前只关注反射场景的替代方案。此外，我们还说明了Ref-Gassian支持更多的应用程序，如重新照明和编辑。 et.al.|[2412.19282](http://arxiv.org/abs/2412.19282)|null|
|**2024-12-25**|**GSAVS: Gaussian Splatting-based Autonomous Vehicle Simulator**|现代自动驾驶汽车模拟器具有不断增长的资产库，包括车辆、建筑物、道路、行人等。虽然这种程度的定制在创建虚拟城市环境时被证明是有益的，但当打算在数字孪生或真实场景的复制品中训练时，这个过程会变得很麻烦。高斯飞溅技术是一种强大的场景重建和新颖的视图合成技术，具有高保真度和渲染速度。本文介绍了GSAVS，一种支持自动驾驶汽车模型创建和开发的自动驾驶汽车模拟器。模拟器中的每个资产都是一个3D高斯平面图，包括车辆和环境。然而，模拟器在经典的3D引擎中运行，实时渲染3D高斯斑点。这使得模拟器能够利用3D高斯飞溅所拥有的真实感，同时提供经典3D引擎的定制和易用性。 et.al.|[2412.18816](http://arxiv.org/abs/2412.18816)|null|

<p align=right>(<a href=#updated-on-20250102>back to top</a>)</p>

## 3D Reconstruction

|Publish Date|Title|Abstract|PDF|Code|
|---|---|---|---|---|
|**2024-12-30**|**FPGA-based Acceleration of Neural Network for Image Classification using Vitis AI**|近年来，卷积神经网络（CNN）在计算机视觉中得到了广泛的应用。在CPU或GPU上运行的复杂CNN架构要么吞吐量不足，要么功耗过高。因此，需要有专用硬件来加速计算工作负载，以解决这些限制。本文在Xilinx Zynq UltraScale+MPSoC ZCU104 FPGA评估板上使用Vitis AI，使用CIFAR-10数据集加速CNN进行图像分类。该工作实现了比CPU和GPU基线高3.33-5.82倍的吞吐量和3.39-6.30倍的能效。它显示了为下游任务提取2D特征的潜力，如深度估计和3D重建。 et.al.|[2412.20974](http://arxiv.org/abs/2412.20974)|null|
|**2024-12-27**|**Not all Views are Created Equal: Analyzing Viewpoint Instabilities in Vision Foundation Models**|在本文中，我们分析了基础模型的视点稳定性，特别是它们对视点变化的敏感性，并将不稳定性定义为视角微小变化导致的显著特征变化，从而导致3D推理任务中的泛化差距。我们研究了九个基本模型，重点研究了它们对视点变化的反应，包括经常被忽视的偶然视点，即特定的相机方向掩盖了物体的真实3D结构。我们的方法能够仅使用特征表示来识别和分类非分布（OOD）、偶然和稳定的视点，而无需访问实际图像。我们的研究结果表明，虽然基础模型一致地编码了偶然的观点，但由于固有的偏见，它们对OOD观点的解释各不相同，有时会导致基于几何相似性的对象错误分类。通过对三个下游任务（分类、VQA和3D重建）的定量和定性评估，我们说明了视点不稳定性的影响，并强调了特征鲁棒性在不同观察条件下的重要性。 et.al.|[2412.19920](http://arxiv.org/abs/2412.19920)|null|
|**2024-12-30**|**WeatherGS: 3D Scene Reconstruction in Adverse Weather Conditions via Gaussian Splatting**|3D高斯散斑（3DGS）在3D场景重建方面受到了广泛关注，但仍然受到复杂室外环境的影响，尤其是在恶劣天气下。这是因为3DGS将恶劣天气造成的伪影视为场景的一部分，并将直接重建它们，大大降低了重建场景的清晰度。为了应对这一挑战，我们提出了WeatherGS，这是一种基于3DGS的框架，用于在不同天气条件下从多视图图像重建清晰的场景。具体来说，我们明确地将多天气伪影分为具有非常不同特征的密集颗粒和镜头遮挡，其中前者是由空气中的雪花和雨滴引起的，后者是由相机镜头上的降水引起的。鉴于此，我们提出了一种从密集到稀疏的预处理策略，该策略通过大气效应滤波器（AEF）顺序去除密集粒子，然后使用透镜效应检测器（LED）提取相对稀疏的遮挡掩模。最后，我们通过处理后的图像和生成的掩模来训练一组3D高斯分布，以排除遮挡区域，并通过高斯飞溅准确恢复底层清晰场景。我们进行了一个多样化且具有挑战性的基准测试，以促进在复杂天气场景下对3D重建的评估。对这一基准的广泛实验表明，我们的WeatherGS在各种天气场景中始终如一地生成高质量、干净的场景，优于现有的最先进的方法。请参阅项目页面：https://jumponthemoon.github.io/weather-gs. et.al.|[2412.18862](http://arxiv.org/abs/2412.18862)|**[link](https://github.com/Jumponthemoon/WeatherGS)**|
|**2024-12-29**|**PartGen: Part-level 3D Generation and Reconstruction with Multi-View Diffusion Models**|文本或图像到3D生成器和3D扫描仪现在可以生成具有高质量形状和纹理的3D资产。这些资产通常由一个单一的融合表示组成，如隐式神经场、高斯混合或网格，没有任何有用的结构。然而，大多数应用程序和创意工作流程都要求资产由几个可以独立操作的有意义的部分组成。为了解决这一差距，我们引入了PartGen，这是一种新颖的方法，可以从文本、图像或非结构化3D对象生成由有意义的部分组成的3D对象。首先，给定生成或渲染的3D对象的多个视图，多视图扩散模型提取一组合理且视图一致的零件分割，将对象划分为零件。然后，第二个多视图扩散模型分别获取每个部分，填充遮挡，并通过将这些完成的视图馈送到3D重建网络来使用它们进行3D重建。这个完成过程考虑了整个对象的上下文，以确保各部分紧密结合。生成完成模型可以弥补因遮挡而丢失的信息；在极端情况下，它可以根据输入的3D资源产生完全不可见的部分的幻觉。我们在生成的和真实的3D资产上评估了我们的方法，并表明它在很大程度上优于分割和零件提取基线。我们还展示了3D零件编辑等下游应用程序。 et.al.|[2412.18608](http://arxiv.org/abs/2412.18608)|null|
|**2024-12-24**|**Resolution-Robust 3D MRI Reconstruction with 2D Diffusion Priors: Diverse-Resolution Training Outperforms Interpolation**|由于3D训练数据的可用性有限，基于深度学习的3D成像，特别是磁共振成像（MRI）具有挑战性。因此，在2D切片上训练的2D扩散模型开始被用于3D MRI重建。然而，正如我们在本文中所展示的，现有的方法适用于固定的体素大小，当体素大小变化时，性能会下降，这在临床实践中经常发生。本文提出并研究了几种利用二维扩散先验进行分辨率鲁棒三维MRI重建的方法。作为这项研究的结果，我们获得了一种基于随机采样二维切片扩散引导正则化的简单分辨率鲁棒变分三维重建方法。与后验采样基线相比，该方法提供了有竞争力的重建质量。为了解决分辨率偏移的敏感性，我们研究了最先进的基于模型的方法，包括高斯飞溅、神经表示和无限维扩散模型，以及一种简单的以数据为中心的方法，在多种分辨率上训练扩散模型。我们的实验表明，基于模型的方法无法缩小3D MRI的性能差距。相比之下，以数据为中心的方法在各种分辨率上训练扩散模型，有效地提供了一种分辨率鲁棒的方法，而不会影响准确性。 et.al.|[2412.18584](http://arxiv.org/abs/2412.18584)|null|
|**2024-12-24**|**Sharper Error Bounds in Late Fusion Multi-view Clustering Using Eigenvalue Proportion**|多视图聚类（MVC）旨在整合来自多个视图的互补信息，以提高聚类性能。后期融合多视图聚类（LFMVC）通过将不同的聚类结果合成为统一的共识，展现出了巨大的潜力。然而，当前的LFMVC方法在噪声和冗余分区方面很困难，并且经常无法捕获视图之间的高阶相关性。为了解决这些局限性，我们提出了一种新的理论框架，利用局部Rademacher复杂性和主特征值比例来分析多核 $k$-means的泛化误差界。我们的分析建立了$\mathcal{O}（1/n）$的收敛率，在$\mathal{O}。基于这一认识，我们提出了一种在多重线性$k$ -means框架内的低通图滤波策略，以减轻噪声和冗余，进一步细化主特征值比例并提高聚类精度。在基准数据集上的实验结果证实，我们的方法在聚类性能和鲁棒性方面优于最先进的方法。相关代码可在以下网址获得https://github.com/csliangdu/GMLKM . et.al.|[2412.18207](http://arxiv.org/abs/2412.18207)|null|
|**2024-12-24**|**A Review of 3D Particle Tracking and Flow Diagnostics Using Digital Holography**|先进的三维（3D）跟踪方法对于研究各种复杂系统中的粒子动力学至关重要，包括多相流、环境和大气科学、胶体科学、生物和医学研究以及工业制造过程。本综述全面总结了使用数字全息术（DH）的3D粒子跟踪和流动诊断。我们首先介绍了DH的原理，并详细讨论了数值重建。然后，该综述探讨了DH中使用的各种硬件设置，包括内联、离轴和双视图或多视图配置，概述了它们的优点和局限性。我们还深入研究了不同的全息图处理方法，分为传统的多步、逆向和基于机器学习的方法，深入了解了它们在多个研究中用于3D粒子跟踪和流动诊断的应用。该综述最后讨论了未来前景，强调了机器学习在实现制造、环境监测和生物科学等不同领域的基于DH的精确粒子跟踪和流动诊断技术方面的重要作用。 et.al.|[2412.18094](http://arxiv.org/abs/2412.18094)|null|
|**2024-12-23**|**Cross-View Referring Multi-Object Tracking**|参考多目标跟踪（RMOT）是当前跟踪领域的一个重要课题。它的任务形式是引导跟踪器跟踪与语言描述匹配的对象。目前的研究主要集中在单视图下的多目标跟踪，指的是一个视图序列或多个不相关的视图序列。然而，在单一视图中，对象的某些外观很容易不可见，导致对象与语言描述的不正确匹配。在这项工作中，我们提出了一个新的任务，称为交叉视图参考多目标跟踪（CRMOT）。它引入了交叉视图来从多个视图中获取对象的外观，避免了RMOT任务中对象外观不可见的问题。CRMOT是一项更具挑战性的任务，即准确跟踪与语言描述匹配的对象，并保持每个交叉视图中对象的身份一致性。为了推进CRMOT任务，我们构建了一个基于CAMPUS和DIVOTrack数据集的交叉视图参考多目标跟踪基准，称为CRTrack。具体来说，它提供了13个不同的场景和221种语言描述。此外，我们提出了一种端到端的交叉视图参考多目标跟踪方法，称为CRTracker。在CRTrack基准上进行的大量实验验证了我们方法的有效性。数据集和代码可在https://github.com/chen-si-jia/CRMOT. et.al.|[2412.17807](http://arxiv.org/abs/2412.17807)|**[link](https://github.com/chen-si-jia/crmot)**|
|**2024-12-21**|**EasyVis2: A Real Time Multi-view 3D Visualization for Laparoscopic Surgery Training Enhanced by a Deep Neural Network YOLOv8-Pose**|EasyVis2是一个专为腹腔镜手术中的免提实时3D可视化而设计的系统。它包含一个配备有一组微型摄像头的手术套管针，这些摄像头插入体腔以提供扩大的视野和手术过程的3D透视图。YOLOv8-Pose是一种复杂的深度神经网络算法，专门用于估计每个单独相机视图中手术器械的位置和方向。随后，使用跨多个视图的相关2D关键点进行3D手术工具姿态估计。这使得能够渲染覆盖在观察到的背景场景上的手术工具的3D表面模型，以实现实时可视化。在这项研究中，我们解释了为新的手术工具开发训练数据集的过程，以定制YoLOv8姿势，同时最大限度地减少标记工作。进行了广泛的实验，将EasyVis2与原始EasyVis进行了比较，结果表明，在相同数量的相机下，新系统提高了3D重建精度并缩短了计算时间。此外，在真实动物组织上进行的3D渲染实验通过显示虚拟侧视图直观地展示了手术工具和组织之间的距离，表明了未来在真实手术中的潜在应用。 et.al.|[2412.16742](http://arxiv.org/abs/2412.16742)|null|
|**2024-12-21**|**LUCES-MV: A Multi-View Dataset for Near-Field Point Light Source Photometric Stereo**|最近，光度立体（PS）领域最大的改进来自于采用可微分体绘制技术，如NeRF或神经SDF，在DiLiGenT MV基准上实现了0.2mm的令人印象深刻的重建误差。然而，虽然有相当大的环境照明对象数据集，如数字孪生目录（DTS），但只有几个小的光度立体数据集，它们往往缺乏具有挑战性的对象（简单、平滑、无纹理）和实用的小形状因子（近场）光设置。为了解决这个问题，我们提出了LUCES-MV，这是第一个为近场点光源光度立体设计的真实世界多视图数据集。我们的数据集包括15个具有不同材料的物体，每个物体都是在不同的光照条件下从距离相机中心30到40厘米的15个LED阵列中成像的。为了促进透明的端到端评估，我们的数据集不仅提供地面真实法线和地面真实对象网格和姿态，还提供灯光和相机校准图像。我们评估了最先进的近场光度立体算法，强调了它们在不同材料和形状复杂性方面的优势和局限性。LUCES-MV数据集为开发更稳健、准确和可扩展的基于光度立体的真实世界3D重建方法提供了重要的基准。 et.al.|[2412.16737](http://arxiv.org/abs/2412.16737)|null|

<p align=right>(<a href=#updated-on-20250102>back to top</a>)</p>

## Diffusion

|Publish Date|Title|Abstract|PDF|Code|
|---|---|---|---|---|
|**2024-12-30**|**Sparse chaos in cortical circuits**|神经冲动是大脑中信息流动的货币，是由神经元膜电位动力学的不稳定性产生的。神经元回路表现出集体混乱，这对学习、记忆、感觉处理和运动控制至关重要。然而，控制神经元回路中集体混沌的性质和强度的因素尚不清楚。在这里，我们使用计算遍历理论来证明神经脉冲产生的基本特征深刻地影响了神经元回路中的集体混沌。李雅普诺夫谱、柯尔莫哥洛夫-西奈熵和吸引子维数上下限的数值精确计算表明，单个神经元中神经冲动产生的变化会适度影响信息编码率，但会定性地改变相空间结构。具体来说，我们发现不稳定流形的数量、Kolmogorov-Sinai熵和吸引子维数急剧减少。超过一个临界点，以扩散近似的同时崩溃、最大李雅普诺夫指数的峰值和领先协变李雅普诺向量的局部化转变为标志，网络表现出稀疏混沌：长时间的接近稳定的动力学被短时间的强混沌中断。对大型、结构更现实的网络的分析支持了这些发现的普遍性。在皮层回路中，生物物理特性似乎与这种稀疏混沌状态相匹配。我们的研究结果揭示了单神经元生物物理学的基本方面与皮质回路的集体动力学之间的密切联系，表明神经冲动产生机制适于增强回路可控性和信息流。 et.al.|[2412.21188](http://arxiv.org/abs/2412.21188)|null|
|**2024-12-30**|**Downscaling of non van der Waals Semimetallic W5N6 with Resistivity Preservation**|过渡金属氮化物（TMNs）的体相长期以来一直是广泛研究的主题，因为它们具有高导电性和耐火性，可用作涂层材料、电催化剂和扩散阻挡层。将TMN缩减为二维（2D）形式将为现有的2D材料库提供有价值的成员，并在各种应用中具有潜在的增强作用。此外，计算预计在二维极限下TMN中会出现不常见的物理现象。在这项研究中，我们使用原子替代方法合成了厚度可从几十纳米到2.9纳米的2D W5N6。所获得的薄片显示出高结晶度和光滑的表面。对15个样品的电学测量显示，平均电导率为161.1 S/cm，当厚度从45.6 nm减小到2.9 nm时，电导率仍保持不变。观察到的弱栅极调谐效应表明合成的2D W5N6具有半金属性质。对转化机理的进一步研究阐明了硫族空位在前驱体中引发反应的关键作用，以及应变在传播转化过程中的关键作用。我们的工作将所需的半金属晶体引入二维材料库，为未来的合成设计提供了力学见解。 et.al.|[2412.21184](http://arxiv.org/abs/2412.21184)|null|
|**2024-12-30**|**Perfect stationary solutions of reaction-diffusion equations on lattices and regular graphs**|无限图上的反应扩散方程可以有无穷多个稳态解。这些解通常被描述为可数代数方程组的根。作为周期平稳解的推广，我们提出了完美平稳解，这是一类具有有限范围的特殊解，其中邻域值由中心顶点的值精确确定。对获得有限值的解的关注使我们能够将可数代数系统重写为有限代数系统。在这项工作中，我们定义了完美定常解的概念，并展示了它的基本性质。我们进一步展示了完美着色理论的结果，以证明正方形、三角形和六边形网格中解的存在性；作为副产品，证明了这些网格上存在不可数个二值平稳解。这两个值的解可以形成高度非周期性和高度不规则的模式。最后，本文介绍了在方形网格上双稳反应扩散方程的应用。 et.al.|[2412.21168](http://arxiv.org/abs/2412.21168)|null|
|**2024-12-30**|**Systematic Benchmarking of Macrosegregation: The Performance of a Modified Hybrid Model**|最近，一种名为AFRODITE的新合金凝固基准已经出现，该基准具有明确的设置和最先进的测量方法，能够对宏观偏析（MS）求解器进行全面评估，特别是在预测MS图不同特征的能力方面。在这项研究中，我们首先开发了合金凝固Stefan问题的解析解，该问题涉及熔体、固体和糊状区域。这个新的解析解扩展了之前的解（S.Cho和J.Sunderland，“熔化或冻结的热传导问题”，J.Heat Transfer，第91卷，第421-426页，1969年），引入了作为温度函数的线性微偏析定律来代替空间坐标。然后，我们采用该解决方案在仅存在热扩散的限制条件下验证OpenFOAM MS求解器。随后，为了捕获Sn-3%Pb AFRODITE基准的MS图，使用标准Blake-Kozeny-Carman渗透率定律及其混合变体之一合并求解器，在这项工作中稍作修改，以通过确保特征从浆料到糊状物多孔区域的连续过渡，更好地与物理相一致。结果表明，混合模型预测了MS图的主要特征，包括堆积效应引起的通道偏析形态和峰值偏析程度，与实验观察结果更为一致。对结果的仔细分析表明，这些改进的预测源于混合模型对再熔化、平行熔体流动平流和垂直于凝固前沿的平流的更准确估计。 et.al.|[2412.21143](http://arxiv.org/abs/2412.21143)|null|
|**2024-12-30**|**Prometheus: 3D-Aware Latent Diffusion Models for Feed-Forward Text-to-3D Scene Generation**|在这项工作中，我们介绍了Prometheus，这是一种3D感知的潜在扩散模型，用于在几秒钟内在对象和场景级别生成文本到3D。我们将3D场景生成表述为潜在扩散范式内的多视图、前馈、像素对齐的3D高斯生成。为了确保可推广性，我们在预训练的文本到图像生成模型的基础上构建模型，只需进行最小的调整，并使用来自单视图和多视图数据集的大量图像对其进行进一步训练。此外，我们在3D高斯生成中引入了RGB-D潜在空间，以解纠缠外观和几何信息，从而能够高效地前馈生成具有更好保真度和几何形状的3D高斯。大量的实验结果证明了我们的方法在前馈3D高斯重建和文本到3D生成方面的有效性。项目页面：https://freemty.github.io/project-prometheus/ et.al.|[2412.21117](http://arxiv.org/abs/2412.21117)|null|
|**2024-12-30**|**Positional information trade-offs in boundary-driven reaction-diffusion systems**|更大系统中的单个组件，如细胞、粒子或试剂，通常需要详细了解它们的相对位置才能相应地发挥作用，使整个系统能够以有组织和高效的方式运行。通过位置信息的概念，这些组件能够指定它们的位置，以便例如创建稳健的空间模式或协调特定的功能。这种复杂的行为通常发生在远离热力学平衡的地方，因此需要耗散自由能来维持功能。我们证明，在具有位置依赖朗缪尔动力学的边界驱动简单排阻系统中，位置信息、重新缩放的熵产生率和全局反应电流之间存在非平凡的帕累托最优权衡。因此，在调整系统边界密度的最优协议中出现了相变，这表明不同的协议能够交换全局最优性，类似于液气相变中的相共存，并且在考虑增加耗散时，增加位置信息可能会导致收益递减。 et.al.|[2412.21113](http://arxiv.org/abs/2412.21113)|null|
|**2024-12-30**|**Lyapunov-Based Deep Neural Networks for Adaptive Control of Stochastic Nonlinear Systems**|当动力学包含未知和非结构化的非线性状态相关项时，控制非线性随机动力系统涉及大量挑战。对于如此复杂的系统，深度神经网络可以作为未知漂移和扩散过程的强大黑盒近似器。最近的发展构建了基于李雅普诺夫的深度神经网络（Lb-DNN）控制器，以使用自适应权重更新律来补偿确定性的不确定性，该自适应权重更新定律是基于基于对DNN架构组成结构的洞察的李雅普诺夫分析得出的。然而，这些Lb DNN控制器没有考虑非确定性的不确定性。本文开发了Lb-DNN，以自适应地补偿非线性随机动态系统的漂移和扩散不确定性。通过基于李雅普诺夫的稳定性分析，构建了基于DNN的近似和相应的DNN权重自适应律，以消除非线性扩散和漂移过程中产生的未知状态相关项。跟踪误差被证明在概率上最终是均匀有界的。对非线性随机动力系统进行了仿真，以证明所提出方法的有效性。 et.al.|[2412.21095](http://arxiv.org/abs/2412.21095)|null|
|**2024-12-30**|**Co-diffusion of hydrogen and oxygen for dense oxyhydride synthesis**|氢化物因其多样化的功能而受到关注。然而，评估电子、离子和声子输运特性并理解其机制仍然具有挑战性，因为氧氢化物合成存在困难，需要在实现密度烧结和防止氢气析出之间进行权衡。高温处理通常是降低晶间电阻所必需的，通常会在充分烧结之前导致氢气析出。这项研究展示了一种新的合成技术，该技术将预烧结的块状氧化物转化为氢氧化合物，同时保持致密状态，而不是旨在实现氢氧化合物颗粒之间强化学连接的后退火工艺。该工艺采用高压扩散控制方法，促进氢化物和氧化物离子的共扩散。 et.al.|[2412.21086](http://arxiv.org/abs/2412.21086)|null|
|**2024-12-30**|**Quantum Diffusion Model for Quark and Gluon Jet Generation**|扩散模型在图像生成方面取得了显著的成功，但它们的计算量很大，训练也很耗时。在本文中，我们介绍了一种新的扩散模型，该模型受益于量子计算技术，以减轻计算挑战并提高高能物理数据中的生成性能。全量子扩散模型在正向过程中用随机酉矩阵代替高斯噪声，并在去噪架构的U-Net中引入变分量子电路。我们对大型强子对撞机的结构复杂的夸克和胶子射流数据集进行了评估。结果表明，全量子和混合模型在射流生成方面与类似的经典模型具有竞争力，突显了使用量子技术解决机器学习问题的潜力。 et.al.|[2412.21082](http://arxiv.org/abs/2412.21082)|**[link](https://github.com/mashathepotato/GSoC-Quantum-Diffusion-Model)**|
|**2024-12-30**|**Edicho: Consistent Image Editing in the Wild**|作为一种经过验证的需求，在野外图像中进行一致的编辑仍然是一项技术挑战，这是由各种无法管理的因素引起的，如物体姿态、照明条件和摄影环境。Edicho提出了一种基于扩散模型的无训练解决方案，其基本设计原则是使用显式图像对应进行直接编辑。具体来说，关键组件包括一个注意力操纵模块和一个精心改进的无分类器引导（CFG）去噪策略，两者都考虑了预先估计的对应关系。这种推理时间算法具有即插即用的特性，与大多数基于扩散的编辑方法兼容，如ControlNet和BrushNet。广泛的结果证明了Edicho在不同环境下进行一致交叉图像编辑的有效性。我们将发布该代码，以方便未来的研究。 et.al.|[2412.21079](http://arxiv.org/abs/2412.21079)|**[link](https://github.com/ezioby/edicho)**|

<p align=right>(<a href=#updated-on-20250102>back to top</a>)</p>

## NeRF

|Publish Date|Title|Abstract|PDF|Code|
|---|---|---|---|---|
|**2024-12-30**|**Hierarchical Pose Estimation and Mapping with Multi-Scale Neural Feature Fields**|机器人应用需要对场景有全面的了解。近年来，基于神经场的参数化整个环境的方法已经变得流行。由于其连续性和学习场景先验的能力，这些方法很有前景。然而，当处理未知的传感器姿态和连续测量时，在机器人中使用神经场变得具有挑战性。本文主要研究大规模神经隐式SLAM的传感器姿态估计问题。我们从概率的角度研究了隐式映射，并提出了具有相应神经网络架构的分层姿态估计。我们的方法非常适合大规模隐式映射表示。所提出的方法在连续的室外LiDAR扫描上运行，实现了精确的姿态估计，同时保持了短轨迹和长轨迹的稳定映射质量。我们在适合大规模重建的结构化稀疏隐式表示上构建了我们的方法，并使用KITTI和MaiCity数据集对其进行了评估。我们的方法在未知姿态的映射方面优于基线，并实现了最先进的定位精度。 et.al.|[2412.20976](http://arxiv.org/abs/2412.20976)|null|
|**2024-12-26**|**Humans as a Calibration Pattern: Dynamic 3D Scene Reconstruction from Unsynchronized and Uncalibrated Videos**|最近关于动态神经场重建的工作假设输入来自具有已知姿势的同步多视图视频。这些输入约束在现实世界的设置中经常得不到满足，使得这种方法不切实际。我们证明，如果视频捕捉到人体运动，则姿态未知的非同步视频可以生成动态神经场。人类是最常见的动态主体之一，其姿势可以使用最先进的方法进行估计。在有噪声的情况下，估计的人体形状和姿态参数为训练一致的动态神经表示的高度非凸和欠约束问题提供了一个不错的初始化。给定人类的姿势和形状序列，我们估计视频之间的时间偏移，然后通过分析3D关节位置进行相机姿势估计。然后，我们使用多分辨率脊训练动态NeRF，同时细化时间偏移和相机姿态。该设置仍然涉及优化许多参数，因此，我们引入了一种鲁棒的渐进学习策略来稳定该过程。实验表明，我们的方法在具有挑战性的条件下实现了精确的时空校准和高质量的场景重建。 et.al.|[2412.19089](http://arxiv.org/abs/2412.19089)|null|
|**2024-12-29**|**PartGen: Part-level 3D Generation and Reconstruction with Multi-View Diffusion Models**|文本或图像到3D生成器和3D扫描仪现在可以生成具有高质量形状和纹理的3D资产。这些资产通常由一个单一的融合表示组成，如隐式神经场、高斯混合或网格，没有任何有用的结构。然而，大多数应用程序和创意工作流程都要求资产由几个可以独立操作的有意义的部分组成。为了解决这一差距，我们引入了PartGen，这是一种新颖的方法，可以从文本、图像或非结构化3D对象生成由有意义的部分组成的3D对象。首先，给定生成或渲染的3D对象的多个视图，多视图扩散模型提取一组合理且视图一致的零件分割，将对象划分为零件。然后，第二个多视图扩散模型分别获取每个部分，填充遮挡，并通过将这些完成的视图馈送到3D重建网络来使用它们进行3D重建。这个完成过程考虑了整个对象的上下文，以确保各部分紧密结合。生成完成模型可以弥补因遮挡而丢失的信息；在极端情况下，它可以根据输入的3D资源产生完全不可见的部分的幻觉。我们在生成的和真实的3D资产上评估了我们的方法，并表明它在很大程度上优于分割和零件提取基线。我们还展示了3D零件编辑等下游应用程序。 et.al.|[2412.18608](http://arxiv.org/abs/2412.18608)|null|
|**2024-12-23**|**S-INF: Towards Realistic Indoor Scene Synthesis via Scene Implicit Neural Field**|基于学习的方法在3D室内场景合成（ISS）中越来越受欢迎，显示出优于传统基于优化的方法的性能。这些基于学习的方法通常使用生成模型在简单但明确的场景表示上对分布进行建模。然而，由于过于简单的显式表示忽略了详细信息，并且缺乏场景内多模态关系的指导，大多数基于学习的方法都难以生成具有逼真对象排列和风格的室内场景。本文介绍了一种新的室内场景合成方法——场景隐式神经场（S-INF），旨在学习多模态关系的有意义表示，以提高室内场景合成的真实感。S-INF假设场景布局通常与对象详细信息有关。它将多模态关系分解为场景布局关系和详细对象关系，然后通过隐式神经场（INF）将它们融合在一起。通过学习专门的场景布局关系并将其投影到S-INF中，我们实现了场景布局的真实生成。此外，S-INF通过可微分渲染捕获密集而详细的对象关系，确保对象之间的风格一致性。通过在基准3D-FRONT数据集上的广泛实验，我们证明了我们的方法在不同类型的ISS下始终达到最先进的性能。 et.al.|[2412.17561](http://arxiv.org/abs/2412.17561)|**[link](https://github.com/zixiliang/s-inf)**|
|**2024-12-22**|**HyperNet Fields: Efficiently Training Hypernetworks without Ground Truth by Learning Weight Trajectories**|为了有效地适应大型模型或训练神经表示的生成模型，超网络引起了人们的兴趣。虽然超级网络工作良好，但训练它们很麻烦，而且通常需要为每个样本进行地面实况优化的权重。然而，获得这些权重中的每一个都是一个需要训练的训练问题，例如，适应权重，甚至是超网络回归的整个神经场。在这项工作中，我们提出了一种训练超网络的方法，而不需要任何每个样本的地面真实值。我们的关键思想是学习一个超网络“场”，并估计网络权重训练的整个轨迹，而不是简单地估计其收敛状态。换句话说，我们向超网络引入了一个额外的输入，即收敛状态，这使它成为一个神经场，对任务网络的整个收敛路径进行建模。这样做的一个关键好处是，在任何收敛状态下，估计权重的梯度都必须与原始任务的梯度相匹配——仅此约束就足以训练超网络场。我们通过个性化图像生成和从图像和点云进行3D形状重建的任务来证明我们的方法的有效性，在没有任何样本地面真实性的情况下展示了具有竞争力的结果。 et.al.|[2412.17040](http://arxiv.org/abs/2412.17040)|null|
|**2024-12-20**|**CCNDF: Curvature Constrained Neural Distance Fields from 3D LiDAR Sequences**|神经距离场（NDF）已成为解决3D计算机视觉和图形下游问题的有力工具。虽然在从各种传感器数据中学习NDF方面取得了重大进展，但需要注意的一个关键方面是在训练过程中对神经场的监督，因为地面真实NDF不适用于大规模户外场景。以往的工作利用各种形式的预期符号距离来指导模型学习。然而，这些方法通常需要更多地关注表面几何形状的关键考虑因素，并且仅限于小规模实施。为此，我们提出了一种利用带符号距离场的二阶导数来改进神经场学习的新方法。我们的方法通过准确估计符号距离来解决局限性，从而更全面地了解底层几何。为了评估我们的方法的有效性，我们对NDF的主要应用领域——测绘和定位任务的流行方法进行了比较评估。我们的结果证明了所提出方法的优越性，突出了其在计算机视觉和图形应用中提高神经距离场能力的潜力。 et.al.|[2412.15909](http://arxiv.org/abs/2412.15909)|null|
|**2024-12-19**|**SolidGS: Consolidating Gaussian Surfel Splatting for Sparse-View Surface Reconstruction**|高斯飞溅在新颖的视图合成和多视图图像的表面重建方面都取得了令人印象深刻的改进。然而，目前的方法仍然难以使用高斯飞溅从稀疏的视图输入图像中重建高质量的表面。在本文中，我们提出了一种名为SolidGS的新方法来解决这个问题。我们观察到，由于几何渲染中高斯函数的特性，重建的几何在多个视图之间可能会严重不一致。这促使我们通过采用更坚实的核函数来整合所有高斯函数，从而有效地提高了曲面重建质量。在几何正则化和单目法线估计的额外帮助下，我们的方法在稀疏视图曲面重建方面取得了比广泛使用的DTU、Tanks和Temples以及LLFF数据集上的所有高斯溅射方法和神经场方法更优越的性能。 et.al.|[2412.15400](http://arxiv.org/abs/2412.15400)|null|
|**2024-12-19**|**LiftRefine: Progressively Refined View Synthesis from 3D Lifting with Volume-Triplane Representations**|我们提出了一种新的视图合成方法，通过从单个或少数视图输入图像合成3D神经场。为了解决图像到3D生成问题的不适定性质，我们设计了一种两阶段方法，该方法涉及重建模型和用于视图合成的扩散模型。我们的重建模型首先将一个或多个输入图像从体积提升到3D空间，作为粗尺度3D表示，然后是三平面作为细尺度3D表示。为了减轻遮挡区域的模糊性，我们的扩散模型会在三个平面的渲染图像中产生缺失细节的幻觉。然后，我们引入了一种新的渐进式细化技术，该技术迭代地应用重建和扩散模型来逐步合成新的视图，提高了3D表示及其渲染的整体质量。实证评估表明，我们的方法在合成SRN-Car数据集、野外CO3D数据集和大规模Objaverse数据集上优于最先进的方法，同时实现了采样效率和多视图一致性。 et.al.|[2412.14464](http://arxiv.org/abs/2412.14464)|null|
|**2024-12-18**|**Level-Set Parameters: Novel Representation for 3D Shape Analysis**|3D形状分析主要集中在点云和网格的传统3D表示上，但这些数据的离散性使得分析容易受到输入分辨率变化的影响。神经场的最新发展从带符号距离函数中引入了水平集参数，作为3D形状的新颖、连续和数值表示，其中形状表面被定义为这些函数的零水平集。这促使我们将形状分析从传统的3D数据扩展到这些新的参数数据。由于水平集参数不是类似欧几里德的点云，我们通过将它们表示为伪正态分布来建立不同形状之间的相关性，并从相应的数据集中预先学习分布。为了进一步探索具有形状变换的水平集参数，我们建议将这些参数的子集设置在旋转和平移上，并使用超网络生成它们。与使用传统数据相比，这简化了与姿势相关的形状分析。我们通过在形状分类（任意姿态）、检索和6D对象姿态估计中的应用，展示了新表示法的前景。本研究中的代码和数据见https://github.com/EnyaHermite/LevelSetParamData. et.al.|[2412.13502](http://arxiv.org/abs/2412.13502)|null|
|**2024-12-13**|**Neural Vector Tomography for Reconstructing a Magnetization Vector Field**|矢量断层重建的离散化技术容易在重建中产生伪影。随着噪声量的增加，这些重建的质量可能会进一步恶化。在这项工作中，我们使用平滑神经场对底层向量场进行建模。由于神经网络中的激活函数可以被选择为平滑的，并且域不再像素化，因此即使在存在噪声的情况下，该模型也能得到高质量的重建。在我们具有潜在的全局连续对称性的情况下，我们发现神经网络比现有技术大大提高了重建的准确性。 et.al.|[2412.09927](http://arxiv.org/abs/2412.09927)|null|

<p align=right>(<a href=#updated-on-20250102>back to top</a>)</p>

[contributors-shield]: https://img.shields.io/github/contributors/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[contributors-url]: https://github.com/Vincentqyw/cv-arxiv-daily/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[forks-url]: https://github.com/Vincentqyw/cv-arxiv-daily/network/members
[stars-shield]: https://img.shields.io/github/stars/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[stars-url]: https://github.com/Vincentqyw/cv-arxiv-daily/stargazers
[issues-shield]: https://img.shields.io/github/issues/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[issues-url]: https://github.com/Vincentqyw/cv-arxiv-daily/issues

