[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]

## Updated on 2023.12.27
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
|**2023-12-21**|**PlatoNeRF: 3D Reconstruction in Plato's Cave via Single-View Two-Bounce Lidar**|由于单目线索的模糊性和缺乏关于遮挡区域的信息，从单个视图进行3D重建是具有挑战性的。神经辐射场（NeRF）虽然在视图合成和3D重建中很受欢迎，但通常依赖于多视图图像。现有的使用NeRF进行单视图3D重建的方法要么依赖于数据先验来幻觉被遮挡区域的视图，这在物理上可能不准确，要么依赖于RGB相机观察到的阴影，这在环境光和低反照率背景中很难检测到。我们建议使用单光子雪崩二极管捕获的飞行时间数据来克服这些限制。我们的方法使用NeRF对两个反弹光路进行建模，使用激光雷达瞬态数据进行监督。通过利用激光雷达测量的NeRF和双反射光的优势，我们证明了我们可以在没有数据先验或依赖受控环境照明或场景反照率的情况下重建可见和遮挡的几何结构。此外，我们还展示了在传感器空间和时间分辨率的实际约束下改进的泛化能力。我们相信，随着单光子激光雷达在手机、平板电脑和耳机等消费设备上无处不在，我们的方法是一个很有前途的方向。 et.al.|[2312.14239](http://arxiv.org/abs/2312.14239)|null|
|**2023-12-21**|**SyncDreamer for 3D Reconstruction of Endangered Animal Species with NeRF and NeuS**|本研究的主要目的是演示如何使用创新的视图合成和3D重建技术，使用单目RGB图像创建濒危物种的模型。为了实现这一点，我们使用SyncDreamer来产生独特的视角，并使用NeuS和NeRF来重建3D表示。我们选择了四种不同的动物，包括东方鹳、青蛙、蜻蜓和老虎，作为我们的研究对象。我们的研究结果表明，SyncDreamer、NeRF和NeuS技术的结合可以成功创建濒危动物的3D模型。然而，我们也观察到NeuS产生了模糊的图像，而NeRF产生了更清晰但更嘈杂的图像。这项研究突出了模拟濒危动物的潜力，并为该领域的未来研究提供了新的方向。通过展示这些先进技术的有效性，我们希望鼓励进一步探索和发展保护和研究濒危物种的技术。 et.al.|[2312.13832](http://arxiv.org/abs/2312.13832)|null|
|**2023-12-21**|**DyBluRF: Dynamic Deblurring Neural Radiance Fields for Blurry Monocular Video**|视频视图合成允许从任意视点和时间创建具有视觉吸引力的帧，提供身临其境的观看体验。神经辐射场，特别是最初为静态场景开发的NeRF，刺激了视频视图合成的各种方法的产生。然而，视频视图合成的挑战来自运动模糊，这是物体或相机在曝光过程中移动的结果，阻碍了清晰的时空视图的精确合成。作为回应，我们提出了一种用于模糊单目视频的新的动态去模糊NeRF框架，称为DyBluRF，由Interleave Ray Refinement（IRR）阶段和基于运动分解的去模糊（MDD）阶段组成。我们的DyBluRF是第一个解决和处理模糊单目视频的新型视图合成的公司。IRR阶段联合重建动态3D场景，并细化不准确的相机姿态信息，以对抗从给定模糊帧中提取的不准确姿态信息。MDD阶段是一种新的增量潜在锐射线预测（ILSP）方法，用于模糊单目视频帧，将潜在锐射线分解为全局相机运动和局部对象运动分量。大量的实验结果表明，我们的DyBluRF在质量和数量上都优于最新的最先进的方法。我们的项目页面包括源代码和预训练模型，可在https://kaist-viclab.github.io/dyblurf-site/. et.al.|[2312.13528](http://arxiv.org/abs/2312.13528)|null|
|**2023-12-20**|**NeRF-VO: Real-Time Sparse Visual Odometry with Neural Radiance Fields**|我们介绍了一种新的单目视觉里程计（VO）系统NeRF VO，该系统集成了用于低延迟相机跟踪的基于学习的稀疏视觉里程计和用于复杂密集重建和新颖视图合成的神经辐射场景表示。我们的系统使用稀疏视觉里程计初始化相机姿态，并从单目深度预测网络中获得与视图相关的密集几何先验。我们协调姿势的尺度和密集的几何体，将它们视为训练神经隐式场景表示的监督线索。NeRF VO通过联合优化关键帧姿势的滑动窗口和底层密集几何体，在场景表示的光度和几何保真度方面表现出非凡的性能，这是通过使用体渲染训练辐射场来实现的。我们在各种合成和真实世界数据集的姿态估计精度、新颖的视图合成保真度和密集的重建质量方面超过了最先进的方法，同时实现了更高的相机跟踪频率和更少的GPU内存消耗。 et.al.|[2312.13471](http://arxiv.org/abs/2312.13471)|null|
|**2023-12-20**|**SWAGS: Sampling Windows Adaptively for Dynamic 3D Gaussian Splatting**|最近，新的视图合成显示出快速的进展，其方法能够产生越来越逼真的结果。3D高斯飞溅已成为一种特别有前途的方法，可以产生高质量的静态场景渲染，并实现实时帧率的交互式观看。然而，它目前仅限于静态场景。在这项工作中，我们扩展了三维高斯飞溅来重建动态场景。我们使用可调MLP对场景的动力学进行建模，该MLP学习从规范空间到每帧一组3D高斯的变形场。为了理清场景的静态和动态部分，我们为每个高斯学习一个可调谐的参数，该参数对各自的MLP参数进行加权，以将注意力集中在动态部分上。这提高了模型在静态区域与动态区域不平衡的场景中捕捉动态的能力。为了处理任意长度的场景，同时保持高渲染质量，我们引入了一种自适应窗口采样策略，根据序列中的移动量将序列划分为多个窗口。我们为每个窗口训练一个单独的动态高斯飞溅模型，允许规范表示发生变化，从而能够重建具有显著几何或拓扑变化的场景。在随机采样的新视图上，使用具有自监督一致性损失的微调步骤来增强时间一致性。因此，我们的方法可以生成具有竞争性定量性能的一般动态场景的高质量渲染图，可以使用我们的动态交互式查看器实时查看。 et.al.|[2312.13308](http://arxiv.org/abs/2312.13308)|null|
|**2023-12-22**|**DiffPortrait3D: Controllable Diffusion for Zero-Shot Portrait View Synthesis**|我们提出了DiffPortrait3D，这是一种条件扩散模型，能够从野生肖像中的一张照片中合成3D一致的照片逼真的新颖视图。具体来说，在给定单个RGB输入的情况下，我们的目标是合成从新颖的相机视图中呈现的看似合理但一致的面部细节，同时保留身份和面部表情。除了耗时的优化和微调外，我们的零样本方法很好地推广到任意面部肖像，具有无污染的相机视图、极端的面部表情和多样化的艺术描绘。其核心是，我们利用在大规模图像数据集上预先训练的2D扩散模型的生成先验作为我们的渲染骨干，而去噪是通过对外观和相机姿态的细致控制来指导的。为了实现这一点，我们首先将参考图像的外观上下文注入冻结的UNets的自关注层。然后利用新颖的条件控制模块来操纵渲染视图，该条件控制模块通过从同一视图观看交叉对象的条件图像来解释相机姿态。此外，我们插入了一个可训练的跨视图注意力模块来增强视图一致性，在推理过程中，通过一个新颖的3D感知噪声生成过程进一步增强了视图一致性。我们在野外和多视图基准测试中展示了最先进的定性和定量结果。 et.al.|[2312.13016](http://arxiv.org/abs/2312.13016)|**[link](https://github.com/FreedomGu/DiffPortrait3D)**|
|**2023-12-20**|**Radar Fields: An Extension of Radiance Fields to SAR**|辐射场是多视图图像采集中复杂场景的反向渲染、新颖视图合成和3D建模领域的一个重大突破。自从它们被引入以来，已经表明它们可以扩展到其他模式，如激光雷达、射频、X射线或超声波。在本文中，我们表明，尽管光学和合成孔径雷达（SAR）图像形成模型之间存在重要差异，但有可能将辐射场扩展到雷达图像，从而呈现第一个“雷达场”。这使我们能够仅使用雷达图像的集合来学习表面模型，类似于规则辐射场的学习方式，并且平均具有相同的计算复杂度。由于这两个领域的定义方式相似，这项工作也显示了将光学图像和SAR图像相结合的混合方法的潜力。 et.al.|[2312.12961](http://arxiv.org/abs/2312.12961)|null|
|**2023-12-21**|**pixelSplat: 3D Gaussian Splats from Image Pairs for Scalable Generalizable 3D Reconstruction**|我们介绍了pixelSplat，这是一种前馈模型，它学习从成对的图像中重建由3D高斯基元参数化的3D辐射场。我们的模型具有实时和内存高效的渲染功能，可进行可扩展训练，并在推理时进行快速3D重建。为了克服稀疏和局部支持表示固有的局部极小值，我们预测了三维上的稠密概率分布，并根据该概率分布对高斯均值进行采样。我们通过重新参数化技巧使这种采样操作可微分，允许我们通过高斯飞溅表示反向传播梯度。我们在真实世界的RealEstate10k和ACID数据集上以宽基线新视图合成为基准，在那里我们优于最先进的光场变换器，并将渲染加速2.5个数量级，同时重建可解释和可编辑的3D辐射场。 et.al.|[2312.12337](http://arxiv.org/abs/2312.12337)|null|
|**2023-12-20**|**MixRT: Mixed Neural Representations For Real-Time NeRF Rendering**|神经辐射场（NeRF）由于其令人印象深刻的真实感重建和渲染能力，已成为新型视图合成的领先技术。然而，在大规模场景中实现实时NeRF渲染带来了挑战，通常导致采用具有大量三角形的复杂烘焙网格表示或烘焙表示中的资源密集型光线行进。我们对这些约定提出了质疑，注意到由具有实质三角形的网格表示的高质量几何体对于实现照片级真实感渲染质量是不必要的。因此，我们提出了MixRT，这是一种新的NeRF表示，包括低质量网格、视图相关位移图和压缩的NeRF模型。这种设计有效地利用了现有图形硬件的功能，从而实现了边缘设备上的实时NeRF渲染。利用高度优化的基于WebGL的渲染框架，我们提出的MixRT在边缘设备上实现了实时渲染速度（在MacBook M1 Pro笔记本电脑上以1280 x 720的分辨率超过30 FPS）、更好的渲染质量（在Unboundd-360数据集的室内场景中高出0.2 PSNR）和更小的存储大小（与最先进的方法相比，小于80%）。 et.al.|[2312.11841](http://arxiv.org/abs/2312.11841)|null|
|**2023-12-18**|**GauFRe: Gaussian Deformation Fields for Real-time Dynamic Novel View Synthesis**|我们提出了一种使用可变形3D高斯进行动态场景重建的方法，该方法适用于单目视频。在高斯飞溅效率的基础上，我们的方法通过位于规范空间中的可变形高斯集和由多层感知器（MLP）定义的时间相关变形场来扩展表示以适应动态元素。此外，在大多数自然场景都有保持静态的大区域的假设下，我们允许MLP通过额外包括静态高斯点云来集中其代表能力。串联的动态和静态点云形成高斯飞溅光栅化器的输入，从而实现实时渲染。在自监督渲染损失的情况下，对可微管道进行端到端优化。我们的方法获得的结果与最先进的动态神经辐射场方法相当，同时允许更快的优化和渲染。项目网站：https://lynl7130.github.io/gaufre/index.html et.al.|[2312.11458](http://arxiv.org/abs/2312.11458)|null|

<p align=right>(<a href=#updated-on-20231227>back to top</a>)</p>

## 3D Reconstruction

|Publish Date|Title|Abstract|PDF|Code|
|---|---|---|---|---|
|**2023-12-22**|**Enhanced Latent Multi-view Subspace Clustering**|潜在多视图子空间聚类已被证明具有理想的聚类性能。然而，原始的潜在表示方法沿着维度方向将来自多个视图的数据矩阵垂直连接到单个矩阵中，以恢复潜在表示矩阵，这可能导致不完整的信息恢复。为了完全恢复潜在空间表示，我们在本文中提出了一种增强的潜在多视图子空间聚类（ELMSC）方法。ELMSC方法包括构建增强数据矩阵，该矩阵增强多视图数据的表示。具体来说，我们将来自不同视图的数据矩阵堆叠到增广矩阵的块对角位置，以利用互补信息。同时，基于不同视图之间的相似性来组合非块对角条目，以获取一致的信息。此外，我们对增广自表示矩阵的非对角块强制执行稀疏正则化，以避免一致性信息的冗余计算。最后，基于交替方向乘法器（ADMM）的框架，提出了一种新的迭代算法来解决ELMSC的优化问题。在真实世界数据集上的大量实验表明，我们提出的ELMSC能够实现比一些现有技术的多视图聚类方法更高的聚类性能。 et.al.|[2312.14763](http://arxiv.org/abs/2312.14763)|**[link](https://github.com/caolei2000/elmsc-code)**|
|**2023-12-22**|**BonnBeetClouds3D: A Dataset Towards Point Cloud-based Organ-level Phenotyping of Sugar Beet Plants under Field Conditions**|未来几十年，农业生产面临着气候变化和可持续性需求带来的严峻挑战，从而减少其对环境的影响。通过机器人的非化学除草，结合自动无人机对作物的监测，以及培育新的、更具弹性的作物品种，在田间管理方面取得了进展，这有助于应对这些挑战。植物性状的分析，即表型分析，是植物育种中的一项重要活动，但它需要大量的体力劳动。通过这篇论文，我们解决了精确表型所需的自动细粒度器官级几何分析的问题。由于该领域的真实世界数据相对较少，我们提出了一个新的数据集，该数据集是使用无人机获取的，该无人机捕捉了包含48个植物品种的真实育种试验的高分辨率图像，因此涵盖了巨大的形态和外观多样性。这使得自主表型的方法能够很好地推广到不同的品种。基于多个视角的重叠高分辨率图像，我们计算了摄影测量密集点云，并为植物、叶子和作为尖端和底部的突出点提供了详细准确的逐点标签。此外，我们还包括德国联邦植物品种办公室的专家对真实植物进行的表型性状测量，从而不仅可以评估分割和关键点检测方面的新方法，还可以直接评估下游任务。所提供的标记点云能够进行细粒度的植物分析，并支持自动表型方法开发的进一步进展，但也能够在表面重建、点云完成和点云的语义解释方面进行进一步研究。 et.al.|[2312.14706](http://arxiv.org/abs/2312.14706)|null|
|**2023-12-22**|**Pola4All: survey of polarimetric applications and an open-source toolkit to analyze polarization**|光的偏振信息可以为计算机视觉和场景理解任务提供丰富的线索，例如物体的材料类型、姿势和形状。随着新的廉价偏振传感器的出现，这种成像方式越来越容易被更广泛的公众所使用，以解决诸如姿态估计、3D重建、水下导航和深度估计等问题。然而，我们观察到这种感觉模态的使用存在一些局限性，并且缺乏分析偏振图像的标准和公开可用的工具。此外，尽管偏振相机制造商通常提供采集工具来与他们的相机接口，但他们很少包括利用偏振信息的处理算法。在这篇论文中，我们回顾了偏振成像应用的最新进展，包括对视觉和机器人感知任务的偏振最新进展的全面调查。我们还介绍了一个完整的软件工具包，该工具包提供了与市场上大多数现有微栅格偏振相机通信和处理信息的通用标准。该工具包还为这种模式实现了几种图像处理算法，并在GitHub上公开提供：https://github.com/vibot-lab/pola4all_jei_2023. et.al.|[2312.14697](http://arxiv.org/abs/2312.14697)|null|
|**2023-12-22**|**Scalable 3D Reconstruction From Single Particle X-Ray Diffraction Images Based on Online Machine Learning**|X射线自由电子激光器（XFEL）为测量生物分子的结构和动力学提供了独特的能力，帮助我们理解生命的基本组成部分。值得注意的是，高重复率XFEL实现了单粒子成像（X射线SPI），其中单个弱散射生物分子在接近生理条件下成像，有机会进入在低温或结晶条件下无法捕获的短暂状态。现有的X射线SPI重建算法估计每个捕获图像中粒子的未知方向及其共享的3D结构，不足以处理这些新兴XFEL生成的海量数据集。在这里，我们介绍了X-RAI，这是一种在线重建框架，可以从大型X射线SPI数据集中估计3D大分子的结构。X-RAI由卷积编码器和基于物理的解码器组成，卷积编码器在大型数据集上分摊姿态估计，解码器采用隐式神经表示，以端到端、自监督的方式实现高质量的3D重建。我们证明了X-RAI在模拟和具有挑战性的实验环境中为小规模数据集实现了最先进的性能，并证明了其以在线方式处理包含数百万衍射图像的大型数据集的前所未有的能力。这些能力意味着X射线SPI向实时捕获和重建的范式转变。 et.al.|[2312.14432](http://arxiv.org/abs/2312.14432)|null|
|**2023-12-22**|**Towards an Exploratory Visual Analytics System for Griefer Identification in MOBA Games**|多人在线战斗竞技场（MOBA）在全球范围内获得了大量玩家，年游戏收入超过20亿美元。然而，故意激怒和骚扰游戏中其他玩家的骗子的存在可能会对玩家的体验产生不利影响，损害游戏的公平性，并可能导致灰色产业的出现。不幸的是，由于缺乏标准化的标准，以及缺乏高质量的标记和注释数据，检测灰蝶的存在具有挑战性。考虑到MOBA游戏的多变量时空数据的复杂性，游戏开发者在很大程度上依赖于对整个游戏视频记录的手动审查来标记和注释griefers，这是一个耗时的过程。为了缓解这个问题，我们与游戏专家团队合作开发了一个名为GrieferLens的交互式视觉分析界面。它概述了球员的行为分析，并综合了他们的关键比赛事件。通过呈现多个信息视图，GrieferLens可以帮助游戏设计团队有效识别和标记MOBA游戏中的Griefer，并为创造更愉快、更公平的游戏环境奠定基础。 et.al.|[2312.14401](http://arxiv.org/abs/2312.14401)|null|
|**2023-12-21**|**PlatoNeRF: 3D Reconstruction in Plato's Cave via Single-View Two-Bounce Lidar**|由于单目线索的模糊性和缺乏关于遮挡区域的信息，从单个视图进行3D重建是具有挑战性的。神经辐射场（NeRF）虽然在视图合成和3D重建中很受欢迎，但通常依赖于多视图图像。现有的使用NeRF进行单视图3D重建的方法要么依赖于数据先验来幻觉被遮挡区域的视图，这在物理上可能不准确，要么依赖于RGB相机观察到的阴影，这在环境光和低反照率背景中很难检测到。我们建议使用单光子雪崩二极管捕获的飞行时间数据来克服这些限制。我们的方法使用NeRF对两个反弹光路进行建模，使用激光雷达瞬态数据进行监督。通过利用激光雷达测量的NeRF和双反射光的优势，我们证明了我们可以在没有数据先验或依赖受控环境照明或场景反照率的情况下重建可见和遮挡的几何结构。此外，我们还展示了在传感器空间和时间分辨率的实际约束下改进的泛化能力。我们相信，随着单光子激光雷达在手机、平板电脑和耳机等消费设备上无处不在，我们的方法是一个很有前途的方向。 et.al.|[2312.14239](http://arxiv.org/abs/2312.14239)|null|
|**2023-12-21**|**3D Pose Estimation of Two Interacting Hands from a Monocular Event Camera**|由于手的相互作用、遮挡、左右手模糊和快速运动，单目视频中的3D手跟踪是一个非常具有挑战性的问题。大多数现有的方法都依赖于RGB输入，而RGB输入在弱光条件下具有严重的局限性，并且存在运动模糊。相比之下，事件相机捕捉局部亮度变化而不是完整的图像帧，并且不会受到所描述的效果的影响。不幸的是，由于数据模态的显著差异，现有的基于图像的技术不能直接应用于事件。为了应对这些挑战，本文介绍了第一个从单目事件相机对两个快速移动和相互作用的手进行3D跟踪的框架。我们的方法使用一种新颖的半监督特征式注意力机制来解决左右手模糊问题，并集成交叉点损失来修复手碰撞。为了促进这一研究领域的进展，我们发布了一个由两只相互作用的手组成的新的合成大规模数据集Ev2Hands-S，以及一个具有真实事件流和地面实况3D注释的新的真实基准Ev2Hands-R。在3D重建精度方面，我们的方法优于现有方法，并在恶劣的光照条件下推广到真实数据。 et.al.|[2312.14157](http://arxiv.org/abs/2312.14157)|null|
|**2023-12-21**|**DUSt3R: Geometric 3D Vision Made Easy**|野外的多视角立体重建（MVS）需要首先估计相机参数，例如内在和外在参数。这些通常是乏味和繁琐的，但它们必须在3D空间中对相应的像素进行三角测量，这是所有性能最好的MVS算法的核心。在这项工作中，我们采取了相反的立场，并引入了DUSt3R，这是一种对任意图像集合进行密集和无约束立体3D重建的全新范式，即在没有关于相机校准或视点姿态的先验信息的情况下操作。我们将成对重建问题视为点图的回归，放松了通常投影相机模型的硬约束。我们证明了这个公式平滑地统一了单目和双目重建的情况。在提供两个以上图像的情况下，我们进一步提出了一种简单而有效的全局对齐策略，该策略在公共参考系中表达所有成对的点图。我们的网络架构基于标准的Transformer编码器和解码器，使我们能够利用强大的预训练模型。我们的公式直接提供了场景的3D模型以及深度信息，但有趣的是，我们可以从中无缝恢复，像素匹配，相对和绝对相机。对所有这些任务的详尽实验表明，所提出的DUSt3R可以统一各种3D视觉任务，并在单目/多视角深度估计和相对姿态估计上设置新的SoTA。总之，DUSt3R使许多几何三维视觉任务变得容易。 et.al.|[2312.14132](http://arxiv.org/abs/2312.14132)|null|
|**2023-12-21**|**Anatomical basis of sex differences in human post-myocardial infarction ECG phenotypes identified by novel automated torso-cardiac 3D reconstruction**|心电图（ECG）在心脏病学中经常使用，尽管其解释因解剖变异而混淆。一种新颖的自动计算管道能够从磁共振成像中量化躯干心室解剖指标，并与心电图特征进行比较。基于英国生物银行的1051名健康受试者和425名心肌梗死后受试者，研究了性别和心肌梗死的差异。女性较小的心室比男性解释了约50%的QRS持续时间较短，并导致女性STJ振幅较低（也是由于更靠上和靠后的位置）。在女性中，躯干心室解剖结构，特别是来自较大BMI的解剖结构，比男性更能调节MI后T波振幅降低和左偏R轴角。因此，女性MI表型较少反映病理，基线STJ振幅和QRS持续时间离临床阈值更远。因此，量化解剖性别差异及其对健康和疾病心电图的影响对于避免临床性别偏见至关重要。 et.al.|[2312.13976](http://arxiv.org/abs/2312.13976)|null|
|**2023-12-21**|**SyncDreamer for 3D Reconstruction of Endangered Animal Species with NeRF and NeuS**|本研究的主要目的是演示如何使用创新的视图合成和3D重建技术，使用单目RGB图像创建濒危物种的模型。为了实现这一点，我们使用SyncDreamer来产生独特的视角，并使用NeuS和NeRF来重建3D表示。我们选择了四种不同的动物，包括东方鹳、青蛙、蜻蜓和老虎，作为我们的研究对象。我们的研究结果表明，SyncDreamer、NeRF和NeuS技术的结合可以成功创建濒危动物的3D模型。然而，我们也观察到NeuS产生了模糊的图像，而NeRF产生了更清晰但更嘈杂的图像。这项研究突出了模拟濒危动物的潜力，并为该领域的未来研究提供了新的方向。通过展示这些先进技术的有效性，我们希望鼓励进一步探索和发展保护和研究濒危物种的技术。 et.al.|[2312.13832](http://arxiv.org/abs/2312.13832)|null|

<p align=right>(<a href=#updated-on-20231227>back to top</a>)</p>

## Diffusion

|Publish Date|Title|Abstract|PDF|Code|
|---|---|---|---|---|
|**2023-12-22**|**MACS: Mass Conditioned 3D Hand and Object Motion Synthesis**|物体的物理特性，如质量，会显著影响我们用手操纵它的方式。令人惊讶的是，到目前为止，这一方面在3D运动合成的现有工作中被忽视了。为了提高合成的三维手-物运动的自然度，本文提出了MACS——第一种基于MAss条件的三维手和物运动合成方法。我们的方法基于级联扩散模型，并生成可能根据物体质量和相互作用类型进行调整的相互作用。MACS还接受手动绘制的3D对象轨迹作为输入，并合成由对象质量调节的自然3D手部运动。这种灵活性使MACS能够用于各种下游应用，例如为ML任务生成合成训练数据，为图形工作流生成手部的快速动画，以及为计算机游戏生成角色交互。我们通过实验表明，小规模的数据集足以使MACS合理地推广到训练过程中看不见的插值和外推物体质量。此外，由于我们的表面接触合成模型ConNet生成的质量条件接触标签，MACS对看不见的物体表现出适度的泛化。我们的全面用户研究证实，合成的3D手-物交互是高度可信和逼真的。 et.al.|[2312.14929](http://arxiv.org/abs/2312.14929)|null|
|**2023-12-22**|**Sampling and estimation on manifolds using the Langevin diffusion**|使用具有不变测度 $d\mu_\phi\propto e^｛-\phi｝\mathrm的固有定义Langevin扩散的离散化，导出了采样和估计的误差界{dvol}_g$在紧致黎曼流形上。考虑了基于离散马尔可夫过程的$\mu_\phi$线性泛函的两个估计量：基于单个轨迹的时间平均估计量和基于多个独立轨迹的集合平均估计量。在$\phi$上不施加超过标称平滑水平的限制，导出了离散化步长中两个估计量的偏差和方差的一阶误差界。误差阶数与欧几里得空间和平坦空间中的最优速率相匹配，并导致不变测度$\mu_\phi$ 和离散马尔可夫过程的平稳测度之间的距离的一阶界。证明技术的一般性利用了两个偏微分方程和对应于Langevin扩散的算子半群之间的联系，使其适用于研究与Langevin散射相关的更一般的一类采样算法。讨论了将分析推广到非紧流形情形的条件。正曲率和负曲率流形上的对数凹分布和其他分布的数值说明了导出的边界，并证明了采样算法的实用性。 et.al.|[2312.14882](http://arxiv.org/abs/2312.14882)|null|
|**2023-12-22**|**BrainVis: Exploring the Bridge between Brain and Visual Signals via Image Reconstruction**|从大脑信号中分析和重建视觉刺激有效地促进了对人类视觉系统的理解。然而，EEG信号是复杂的并且包含大量的噪声。这导致了现有的从EEG重建视觉刺激的工作存在很大的局限性，例如难以将EEG嵌入与细粒度语义信息对齐，以及严重依赖额外的大型自收集数据集进行训练。为了应对这些挑战，我们提出了一种称为BrainVis的新方法。首先，我们将脑电信号划分为多个单元，并对其应用自监督方法来获得脑电时域特征，试图减轻训练难度。此外，我们还建议利用频域特征来增强EEG表示。然后，我们将EEG时频嵌入与CLIP空间中的粗语义和细粒度语义的插值同时对齐，以突出主要视觉分量并降低跨模态对齐的难度。最后，我们采用级联扩散模型来重建图像。我们提出的BrainVis在语义保真度重建和生成质量方面都优于现有技术。值得注意的是，我们将训练数据规模减少到之前工作的10%。 et.al.|[2312.14871](http://arxiv.org/abs/2312.14871)|null|
|**2023-12-22**|**Neural-network-based regularization methods for inverse problems in imaging**|这篇综述介绍并概述了用于成像逆问题的基于神经网络的正则化方法的现状。它旨在向具有扎实应用数学知识和神经网络基本理解的读者介绍应用神经网络正则化成像中逆问题的不同概念。这篇综述的区别性特征包括，对逆问题的学习生成器和学习先验，特别是扩散模型的简单介绍，以及在这方面明确关注基于神经网络的方法的函数空间分析中的现有结果的部分。 et.al.|[2312.14849](http://arxiv.org/abs/2312.14849)|null|
|**2023-12-22**|**Dreaming of Electrical Waves: Generative Modeling of Cardiac Excitation Waves using Diffusion Models**|在危及生命的心律失常（如心房颤动或心室颤动）期间，心脏中的电波形成旋转的螺旋波或涡旋波。波动动力学通常使用耦合偏微分方程进行建模，该方程描述了可激发介质中的反应扩散动力学。最近，数据驱动的生成建模已经成为在物理和生物系统中生成时空模式的一种替代方案。在这里，我们探索用于心脏组织中电波模式的生成建模的去噪扩散概率模型。我们用模拟的电波模式训练了扩散模型，以便能够在无条件和有条件的生成任务中生成这样的电波模式。例如，我们探索了修复任务，例如从表面的二维测量中重建三维波浪动力学，以及进化和生成特定参数的动力学。我们对扩散生成的解决方案与生物物理模型获得的解决方案进行了表征和比较，发现扩散模型能够很好地复制螺旋波和涡旋波动力学，因此可以作为心脏组织中激励波建模的替代数据驱动方法。例如，我们发现可以立即启动心室颤动（VF）动力学，而不必应用起搏协议来诱导波断。VF动力学可以在任意心室几何形状中创建，并且可以随着时间的推移而演变。然而，我们也发现，当约束条件不足时，扩散模型会产生“幻觉”波形。不管这些局限性如何，扩散模型是一种有趣而强大的工具，在心律失常研究和诊断中有许多潜在的应用。 et.al.|[2312.14830](http://arxiv.org/abs/2312.14830)|null|
|**2023-12-22**|**Neural network models for preferential concentration of particles in two-dimensional turbulence**|团簇和空穴的形成是含颗粒湍流动力学中的关键过程。在这项工作中，我们评估了各种神经网络模型在合成湍流中粒子优先浓度场方面的性能。使用具有单向耦合惯性点粒子的均匀各向同性二维湍流的直接数值模拟数据库，使用涡度作为输入来训练模型，以预测粒子数密度场。我们比较了自动编码器、U-Net、生成对抗性网络（GAN）和扩散模型方法，并评估了生成的粒子数密度场的统计特性。我们发现，GANs在预测团簇和空隙方面具有优越性，因此具有最佳性能。此外，我们探讨了“超级采样”的一个概念“，其中神经网络可以用于仅使用少数粒子的信息来预测全粒子数据，这为通过避免跟踪数百万粒子来降低昂贵的DNS计算的计算成本提供了有前景的前景t个不同的Stokes数。因此，我们的研究还表明，神经网络有可能利用惯性粒子的实验测量来预测湍流统计数据。 et.al.|[2312.14829](http://arxiv.org/abs/2312.14829)|null|
|**2023-12-22**|**Plan, Posture and Go: Towards Open-World Text-to-Motion Generation**|传统的文本到运动生成方法通常在有限的文本-运动对上进行训练，这使得它们很难推广到开放世界场景中。一些作品使用CLIP模型来对齐运动空间和文本空间，旨在实现从自然语言运动描述中生成运动。但是，它们仍然被限制为生成有限且不切实际的原地运动。为了解决这些问题，我们提出了一个名为PRO Motion的分而治之的框架，该框架由运动规划器、姿势扩散器和go扩散器三个模块组成。运动规划器指示大型语言模型（LLM）生成描述目标运动中的关键姿势的脚本序列。与自然语言不同，脚本可以按照非常简单的文本模板描述所有可能的姿势。这大大降低了姿势扩散器的复杂性，它将脚本转换为姿势，为生成开放世界铺平了道路。最后，作为另一个扩散模型实现的go diffuser估计所有姿势的全身平移和旋转，从而产生逼真的运动。实验结果表明了我们的方法与其他方法相比的优越性，并证明了它能够从复杂的开放世界提示中生成多样化和逼真的运动，如“体验深刻的快乐感”。项目页面位于https://moonsliu.github.io/pro-motion. et.al.|[2312.14828](http://arxiv.org/abs/2312.14828)|null|
|**2023-12-22**|**Disorder-induced non-linear growth of viscously-unstable immiscible two-phase flow fingers in porous media**|一种流体在多孔介质内被另一种流体不混溶的驱替根据毛细管数Ca和粘度比M产生不同类型的模式。在高Ca下，由流体-流体界面之间的粘性不稳定性产生的粘性指状物被认为表现出与Saffman和Taylor[1]在Hele-Shaw细胞中观察到的粘性不稳定指状物或扩散限制聚集体（DLA）[2]相同的拉普拉斯生长行为。即，界面速度线性地取决于驱动生长过程的物理场的局部梯度（对于两相流，压力场）。然而，众所周知，由于孔喉处毛细管屏障的紊乱，多孔介质中的稳态两相流表现出流速作为非线性幂律依赖于整体压降的状态。20年前，二维多孔介质中粘性不稳定排水的实验也证明了类似的非线性增长机制[3]。在这里，我们使用动态孔隙网络模型重新审视这种流动状态，并探索生长特性中的非线性。我们描述了统计指宽和非线性生长定律指数对Ca的先前未研究的依赖性，并基于理论论点定量讨论了毛细管屏障中的无序如何控制生长过程的非线性，以及为什么在足够高的Ca下流动状态会过渡到拉普拉斯生长。此外，将手指模式的统计特性与Saffman-Taylor手指的统计特性、DLA生长模式以及上述先前实验研究的结果进行比较。 et.al.|[2312.14799](http://arxiv.org/abs/2312.14799)|null|
|**2023-12-22**|**Cross-Age and Cross-Site Domain Shift Impacts on Deep Learning-Based White Matter Fiber Estimation in Newborn and Baby Brains**|深度学习模型在根据有限的扩散磁共振成像数据估计组织微观结构方面显示出巨大的前景。然而，当测试和训练数据来自不同的扫描仪和协议时，或者当模型应用于具有固有变化的数据时，例如在不同年龄扫描的婴儿和儿童的发育中的大脑时，这些模型面临着领域转移的挑战。已经提出了几种技术来解决其中的一些挑战，例如成人大脑中的数据协调或领域自适应。然而，对于快速发育的婴儿大脑中纤维定向分布函数的估计，这些技术尚未探索。在这项工作中，我们使用矩量法和微调策略，广泛调查了201名新生儿和165名婴儿的两个不同队列内部和之间的年龄效应和领域转移。我们的研究结果表明，与新生儿相比，婴儿微观结构发育变化的减少直接影响了深度学习模型的跨年龄表现。我们还证明了少量的目标域样本可以显著缓解域偏移问题。 et.al.|[2312.14773](http://arxiv.org/abs/2312.14773)|null|
|**2023-12-22**|**Diffusion Maps for Signal Filtering in Graph Learning**|本文探讨了扩散图作为图移位算子在理解图信号的基本几何结构中的应用。该研究评估了当使用扩散图生成的滤波器来解决马尔可夫变异最小化问题时，图学习的改进。本文通过综合生成和真实世界温度传感器数据的例子展示了这种方法的有效性。这些例子还将扩散图图信号模型与其他常用的图信号算子进行比较。这些结果为分析和理解复杂的非欧几里得数据结构提供了新的方法。 et.al.|[2312.14758](http://arxiv.org/abs/2312.14758)|null|

<p align=right>(<a href=#updated-on-20231227>back to top</a>)</p>

## NeRF

|Publish Date|Title|Abstract|PDF|Code|
|---|---|---|---|---|
|**2023-12-22**|**Fluid Simulation on Neural Flow Maps**|我们介绍了神经流图，这是一种新的模拟方法，将新兴的隐式神经表示范式与基于流图理论的流体模拟相结合，以实现最先进的无粘流体现象模拟。我们设计了一种新的混合神经场表示，空间稀疏神经场（SSNF），它将小型神经网络与重叠、多分辨率和空间稀疏网格的金字塔相融合，以高精度紧凑地表示长期时空速度场。有了这个神经速度缓冲器，我们以机械对称的方式计算长期双向流图及其雅可比矩阵，以促进对现有解决方案的大幅精度提高。这些长程双向流图实现了低耗散的高平流精度，进而促进了高保真度的不可压缩流模拟，显示了复杂的旋涡结构。我们展示了我们的神经流体模拟在各种具有挑战性的模拟场景中的有效性，包括跳跃涡流、碰撞涡流、涡流重新连接，以及移动障碍物和密度差异产生的涡流。我们的例子表明，在能量守恒、视觉复杂性、对实验观测的遵守以及详细旋涡结构的保存方面，与现有方法相比，性能有所提高。 et.al.|[2312.14635](http://arxiv.org/abs/2312.14635)|null|
|**2023-12-21**|**Geometric Awareness in Neural Fields for 3D Human Registration**|将模板与三维人体点云对齐是一个长期存在的问题，对于动画、重建和启用监督学习管道等任务至关重要。最近的数据驱动方法利用了预测的表面对应关系；然而，它们对不同的姿态或分布并不鲁棒。相比之下，工业解决方案往往依赖于昂贵的手动注释或多视图捕获系统。最近，神经场已经显示出有希望的结果，但它们纯粹的数据驱动性质缺乏几何意识，通常导致模板配准的微小错位。在这项工作中，我们提出了两种解决方案：LoVD，一种新的神经场模型，它预测朝向目标表面上的局部SMPL顶点的方向；和INT，这是第一个专门用于神经领域的自监督任务，在测试时，它利用目标几何结构来细化主干。我们将它们组合到INLoVD中，这是一个在大型MoCap数据集上训练的强大的3D人体注册管道。INLoVD是高效的（不到一分钟），在公共基准上稳定地达到了最先进的水平，并对分布外的数据提供了前所未有的概括。我们将在\url｛url｝中发布代码和检查点。 et.al.|[2312.14024](http://arxiv.org/abs/2312.14024)|null|
|**2023-12-20**|**Neural feels with neural fields: Visuo-tactile perception for in-hand manipulation**|为了实现人类水平的灵活性，机器人必须从多模式感知推断空间意识，以推理接触互动。在新物体的手操作过程中，这种空间意识包括估计物体的姿势和形状。手内感知的现状主要采用视觉，并局限于跟踪先验已知对象。此外，在操作过程中，手上物体的视觉遮挡迫在眉睫，这阻止了当前系统在没有遮挡的情况下超越任务。我们将多指手的视觉和触摸传感相结合，在手内操作过程中估计物体的姿势和形状。我们的方法NeuralFeels通过在线学习神经场来编码对象几何，并通过优化姿态图问题来联合跟踪它。我们研究了模拟和现实世界中的多模式手部感知，通过本体感觉驱动的策略与不同的物体进行交互。我们的实验显示，使用已知的CAD模型，最终重建F分数为 $81$%，平均姿势漂移为$4.7\，\text｛mm｝$，进一步降低到$2.3\，\text{mm｝$。此外，我们观察到，与仅使用视觉的方法相比，在严重的视觉遮挡下，我们可以实现高达94$ %的跟踪改进。我们的研究结果表明，在手部操作过程中，触摸至少可以改善视觉估计，并在最好的情况下消除视觉估计的歧义。我们发布了70个实验的评估数据集FeelSight，作为在该领域进行基准测试的一步。我们由多模态感知驱动的神经表示可以作为提高机器人灵活性的感知支柱。视频可以在我们的项目网站上找到https://suddhu.github.io/neural-feels/ et.al.|[2312.13469](http://arxiv.org/abs/2312.13469)|null|
|**2023-12-20**|**Deep Learning on 3D Neural Fields**|近年来，神经场（NFs）已成为编码各种连续信号（如图像、视频、音频和3D形状）的有效工具。当应用于3D数据时，NFs提供了一种解决方案来解决与流行的离散表示相关的碎片化和局限性。然而，鉴于神经网络本质上是神经网络，目前尚不清楚它们是否以及如何无缝集成到深度学习管道中，以解决下游任务。本文解决了这一研究问题，并介绍了nf2vec，这是一个能够在单个推理过程中为输入NF生成紧凑的潜在表示的框架。我们证明了nf2vec有效地嵌入了由输入NF表示的3D对象，并展示了如何在深度学习管道中使用由此产生的嵌入来成功地处理各种任务，同时只处理NF。我们在几个用于表示3D曲面的NFs上测试了这个框架，例如无符号/有符号距离和占用字段。此外，我们用更复杂的NFs证明了我们的方法的有效性，这些NFs包括3D对象的几何形状和外观，如神经辐射场。 et.al.|[2312.13277](http://arxiv.org/abs/2312.13277)|null|
|**2023-12-16**|**How to Train Neural Field Representations: A Comprehensive Study and Benchmark**|神经场（NeFs）最近已成为一种用于对各种模态（包括图像、形状和场景）的信号进行建模的通用方法。随后，许多工作探索了使用NeF作为下游任务的表示，例如，根据适合的NeF的参数对图像进行分类。然而，NeF超参数对其作为下游表示的质量的影响很少被理解，而且在很大程度上仍未被探索。这在一定程度上是由于拟合神经场数据集所需的大量时间造成的。在这项工作中，我们提出了 $\verb|fit-a-nef|$ ，这是一个基于JAX的库，它利用并行化来实现大规模nef数据集的快速优化，从而显著加快速度。有了这个库，我们进行了一项全面的研究，研究了不同超参数——包括初始化、网络架构和优化策略——对下游任务的NeF拟合的影响。我们的研究为如何训练NeF提供了宝贵的见解，并为优化其在下游应用中的有效性提供了指导。最后，基于所提出的库和我们的分析，我们提出了Neural Field Arena，这是一个由流行视觉数据集的神经场变体组成的基准，包括MNIST、CIFAR、ImageNet和ShapeNetv2的变体。我们的图书馆和神经领域竞技场将是开源的，以引入标准化的基准测试，并促进对神经领域的进一步研究。 et.al.|[2312.10531](http://arxiv.org/abs/2312.10531)|**[link](https://github.com/samuelepapa/fit-a-nef)**|
|**2023-12-18**|**LatentEditor: Text Driven Local Editing of 3D Scenes**|虽然神经领域在视图合成和场景重建方面取得了重大进展，但由于其对来自多视图输入的几何和纹理信息的隐式编码，编辑它们带来了巨大的挑战。在本文中，我们介绍了\textsc｛LatentEditor｝，这是一个创新的框架，旨在让用户能够使用文本提示对神经字段进行精确和本地控制的编辑。利用去噪扩散模型，我们成功地将真实世界的场景嵌入到潜在空间中，与传统方法相比，产生了更快、更具适应性的NeRF主干进行编辑。为了提高编辑精度，我们引入了一个delta分数来计算潜在空间中的2D掩模，该分数可以作为局部修改的指南，同时保留不相关的区域。我们新颖的像素级评分方法利用InstructPix2Pix（IP2P）的能力来辨别潜在空间中IP2P条件和无条件噪声预测之间的差异。然后在训练集中迭代地更新以2D掩码为条件的编辑的潜伏时间，以实现3D局部编辑。与现有的3D编辑模型相比，我们的方法实现了更快的编辑速度和卓越的输出质量，弥合了文本指令和潜在空间中高质量3D场景编辑之间的差距。我们在LLFF、IN2N、NeRFStudio和NeRFArt四个基准3D数据集上展示了我们的方法的优势。 et.al.|[2312.09313](http://arxiv.org/abs/2312.09313)|**[link](https://github.com/umarkhalidAI/LatentEditor)**|
|**2023-12-14**|**ZeroRF: Fast Sparse View 360° Reconstruction with Zero Pretraining**|我们提出了ZeroRF，这是一种新的每场景优化方法，解决了神经场表示中稀疏视图360重建的挑战。目前的突破，如神经辐射场（NeRF）已经证明了高保真度的图像合成，但难以处理稀疏的输入视图。现有的方法，如可泛化的NeRF和每场景优化方法，在数据依赖性、计算成本和跨不同场景的泛化方面面临限制。为了克服这些挑战，我们提出了ZeroRF，其关键思想是将定制的深度图像先验集成到因子分解的NeRF表示中。与传统方法不同，ZeroRF使用神经网络生成器对特征网格进行参数化，从而实现高效的稀疏视图360重建，而无需任何预训练或额外的正则化。大量实验展示了ZeroRF在质量和速度方面的多功能性和优势，在基准数据集上取得了最先进的结果。ZeroRF的意义延伸到3D内容生成和编辑的应用。项目页面：https://sarahweiii.github.io/zerorf/ et.al.|[2312.09249](http://arxiv.org/abs/2312.09249)|null|
|**2023-12-12**|**SMERF: Streamable Memory Efficient Radiance Fields for Real-Time Large-Scene Exploration**|最近的实时视图合成技术在保真度和速度上迅速进步，现代方法能够以交互式帧速率渲染接近照片级真实感的场景。与此同时，在易于光栅化的显式场景表示和基于射线行进的神经场之间出现了紧张关系，后者的最先进实例在质量上超过了前者，同时对于实时应用来说成本高得令人望而却步。在这项工作中，我们介绍了SMERF，这是一种视图合成方法，在占地面积高达3亿 $^2$、体积分辨率为3.5毫米$^3$ 的大型场景中，它实现了实时方法中最先进的精度。我们的方法建立在两个主要贡献之上：一个是分层模型划分方案，它在限制计算和内存消耗的同时增加了模型容量，另一个是蒸馏训练策略，它同时产生高保真度和内部一致性。我们的方法能够在网络浏览器中实现全六自由度（6DOF）导航，并在商品智能手机和笔记本电脑上实时渲染。大量实验表明，我们的方法在实时新视图合成方面，在标准基准上超过了当前最先进的0.78 dB，在大型场景上超过了1.78 dB，渲染帧的速度比最先进的辐射场模型快三个数量级，并在包括智能手机在内的各种商品设备上实现了实时性能。我们鼓励读者在我们的项目网站上亲自探索这些模型：https://smerf-3d.github.io. et.al.|[2312.07541](http://arxiv.org/abs/2312.07541)|null|
|**2023-12-11**|**Representing stimulus motion with waves in adaptive neural fields**|神经活动的行波在皮层网络中自发出现，并对刺激做出反应。波的时空结构可以指示它们编码的信息以及维持它们的生理过程。在这里，我们研究了作为视觉运动处理模型的自适应神经场中出现的行波的刺激响应关系。神经场方程将皮层组织的活动建模为连续的可兴奋介质，自适应过程提供负反馈，产生局部活动模式。在我们的模型中，突触连接由一个积分核来描述，该积分核由于依赖于活动的突触抑制而动态减弱，导致边缘稳定的行进前沿（具有衰减的后部）或固定速度的脉冲。我们的分析量化了弱刺激如何随着时间的推移改变这些波的相对位置，其特征是我们扰动地获得的波响应函数。持续和连续可见的刺激模拟移动的视觉对象。在视觉空间中跳跃的间歇性闪光可以产生流畅的视觉运动体验。我们的理论和数值模拟很好地描述了波对两种运动刺激的夹带，提供了视觉运动感知的机制描述。 et.al.|[2312.06100](http://arxiv.org/abs/2312.06100)|null|
|**2023-12-11**|**Nuvo: Neural UV Mapping for Unruly 3D Representations**|现有的UV映射算法被设计为在性能良好的网格上操作，而不是由最先进的3D重建和生成技术产生的几何表示。因此，将这些方法应用于由神经辐射场和相关技术（或从这些场三角化的网格）恢复的体积密度会导致纹理图谱过于分散，无法用于视图合成或外观编辑等任务。我们提出了一种UV映射方法，旨在对通过3D重建和生成技术产生的几何体进行操作。我们的方法Nuvo不是计算在网格顶点上定义的映射，而是使用神经场来表示连续的UV映射，并将其优化为仅针对一组可见点（即仅影响场景外观的点）的有效且性能良好的映射。我们展示了我们的模型对不良几何体带来的挑战是稳健的，并且它生成了可以表示详细外观的可编辑UV映射。 et.al.|[2312.05283](http://arxiv.org/abs/2312.05283)|null|

<p align=right>(<a href=#updated-on-20231227>back to top</a>)</p>

[contributors-shield]: https://img.shields.io/github/contributors/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[contributors-url]: https://github.com/Vincentqyw/cv-arxiv-daily/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[forks-url]: https://github.com/Vincentqyw/cv-arxiv-daily/network/members
[stars-shield]: https://img.shields.io/github/stars/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[stars-url]: https://github.com/Vincentqyw/cv-arxiv-daily/stargazers
[issues-shield]: https://img.shields.io/github/issues/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[issues-url]: https://github.com/Vincentqyw/cv-arxiv-daily/issues

