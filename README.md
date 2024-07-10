[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]

## Updated on 2024.07.10
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
|**2024-07-08**|**RRM: Relightable assets using Radiance guided Material extraction**|在过去的几年里，在任意照明下合成NeRF已经成为一个开创性的问题。最近的努力通过提取基于物理的参数来解决这个问题，然后这些参数可以在任意照明下渲染，但它们所能处理的场景范围有限，通常是对光泽场景的处理不当。我们提出了RRM，这是一种即使在存在高反射物体的情况下也可以提取场景的材质、几何体和环境照明的方法。我们的方法包括一个物理感知的辐射场表示，它通知基于物理的参数，以及一个基于拉普拉斯金字塔的表达环境光结构。我们证明，我们在参数检索任务上的贡献优于最先进的技术，从而在表面场景上实现了高保真重照明和新颖的视图合成。 et.al.|[2407.06397](http://arxiv.org/abs/2407.06397)|null|
|**2024-07-08**|**PanDORA: Casual HDR Radiance Acquisition for Indoor Scenes**|大多数新颖的视图合成方法（如NeRF）无法捕捉场景的真正高动态范围（HDR）辐射，因为它们通常是在用标准低动态范围（LDR）相机捕捉的照片上训练的。虽然以不同曝光拍摄多幅图像的传统曝光包围方法最近已适用于多视图情况，但我们发现这种方法无法拍摄包括非常明亮光源在内的室内场景的全动态范围。在本文中，我们提出了PanDORA：一种用于在高动态范围内随意捕捉室内场景的PANoramic双观察者辐射采集系统。我们提出的系统包括两个360度摄像机，它们固定在便携式三脚架上。摄像机同时获取两个360｛\deg｝视频：一个定期曝光，另一个快速曝光，使用户可以在几分钟内随意地在场景中挥动设备。生成的图像被馈送到基于NeRF的算法，该算法重建场景的全高动态范围。与之前工作中的HDR基线相比，我们的方法在不牺牲视觉质量的情况下重建了室内场景的全HDR辐射，同时保留了最近类似NeRF方法的易于捕捉性。 et.al.|[2407.06150](http://arxiv.org/abs/2407.06150)|null|
|**2024-07-08**|**PerlDiff: Controllable Street View Synthesis Using Perspective-Layout Diffusion Models**|可控生成被认为是解决3D数据注释挑战的一种潜在的重要方法，在自动驾驶数据生成的背景下，这种可控生成的精度变得尤为重要。现有方法侧重于利用GLIGEN或ControlNet等框架将各种生成信息集成到控制输入中，以在可控生成中产生值得称赞的结果。然而，这种方法本质上将生成性能限制为预定义网络架构的学习能力。在本文中，我们探索了控制信息的集成，并介绍了PerlDiff（透视布局扩散模型），这是一种充分利用透视三维几何信息的有效街景图像生成方法。我们的PerlDiff采用3D几何先验，在网络学习过程中通过精确的对象级控制来指导街景图像的生成，从而产生更稳健和可控的输出。此外，与其他布局控制方法相比，它表现出优越的可控性。经验结果证明，我们的PerlDiff显著提高了NuScenes和KITTI数据集的生成精度。我们的代码和型号可在https://github.com/LabShuHangGU/PerlDiff. et.al.|[2407.06109](http://arxiv.org/abs/2407.06109)|**[link](https://github.com/labshuhanggu/perldiff)**|
|**2024-07-08**|**OSN: Infinite Representations of Dynamic 3D Scenes from Monocular Videos**|长期以来，从单目RGB视频中恢复底层动态3D场景表示一直是一项挑战。现有的工作将这个问题公式化为通过添加各种约束（如深度先验和强几何约束）来找到一个最合理的解决方案，忽略了可能有无限多个3D场景表示对应于单个动态视频的事实。在本文中，我们的目标是学习与输入视频匹配的所有合理的3D场景配置，而不仅仅是推断特定的场景配置。为了实现这一宏伟目标，我们引入了一个新的框架，称为OSN。我们方法的关键是一个简单而创新的对象比例网络，以及一个联合优化模块，以学习每个动态3D对象的准确比例范围。这使我们能够对尽可能多的忠实3D场景配置进行采样。大量实验表明，我们的方法在多个合成和真实世界数据集上的动态新视图合成中超过了所有基线，并实现了卓越的精度。最值得注意的是，我们的方法在学习细粒度3D场景几何体方面显示出明显的优势。我们的代码和数据可在https://github.com/vLAR-group/OSN et.al.|[2407.05615](http://arxiv.org/abs/2407.05615)|**[link](https://github.com/vlar-group/osn)**|
|**2024-07-08**|**GeoNLF: Geometry guided Pose-Free Neural LiDAR Fields**|尽管最近的工作已经将神经辐射场（NeRF）扩展到激光雷达点云合成中，但大多数现有工作都表现出对预计算姿态的强烈依赖性。然而，点云配准方法难以实现精确的全局姿态估计，而以前的无姿态NeRF忽略了全局重建中的几何一致性。有鉴于此，我们探索了点云的几何见解，它为重建提供了明确的配准先验。基于此，我们提出了几何引导的神经激光雷达场（GeoNLF），这是一种交替执行全局神经重建和纯几何姿态优化的混合框架。此外，在稀疏视图输入下，NeRF倾向于过度拟合单个帧，并且容易陷入局部极小值。为了解决这个问题，我们开发了一种选择性的重新加权策略，并引入了鲁棒优化的几何约束。在NuScenes和KITTI-360数据集上的大量实验证明了GeoNLF在低频大尺度点云的新视图合成和多视图配准方面的优越性。 et.al.|[2407.05597](http://arxiv.org/abs/2407.05597)|null|
|**2024-07-08**|**Dynamic Neural Radiance Field From Defocused Monocular Video**|单目视频的动态神经辐射场（NeRF）最近被用于时空新视图合成，并取得了良好的结果。然而，在视频捕获中经常会出现由深度变化引起的散焦模糊，这会影响动态重建的质量，因为缺乏清晰的细节会干扰输入视图之间的建模时间一致性。为了解决这个问题，我们提出了D2RF，这是第一种动态NeRF方法，旨在从散焦单目视频中恢复清晰新颖的视图。我们引入了分层景深（DoF）体绘制来对散焦模糊进行建模，并重建由散焦视图监督的清晰NeRF。模糊模型的灵感来自DoF渲染和体绘制之间的联系。体绘制中的不透明度与DoF渲染中的层可见性一致。为了执行模糊，我们将分层模糊内核修改为基于光线的内核，并使用优化的稀疏内核来有效地收集输入光线，并使用分层DoF体绘制渲染优化的光线。我们为我们的任务合成了一个具有散焦动态场景的数据集，在数据集上的大量实验表明，我们的方法在从散焦模糊合成所有聚焦新视图方面优于现有方法，同时保持场景的时空一致性。 et.al.|[2407.05586](http://arxiv.org/abs/2407.05586)|null|
|**2024-07-07**|**GaussReg: Fast 3D Registration with Gaussian Splatting**|点云配准是大规模三维场景扫描和重建的一个基本问题。在深度学习的帮助下，注册方法有了显著的发展，达到了接近成熟的阶段。随着神经辐射场（NeRF）的引入，它以其强大的视图合成能力成为最受欢迎的3D场景表示。关于NeRF表示，大规模场景重建也需要其注册。然而，这一主题极缺乏探索。这是由于对具有隐含表示的两个场景之间的几何关系进行建模的固有挑战。现有的方法通常将隐式表示转换为显式表示以进行进一步的注册。最近，引入了高斯散射（GS），采用了显式三维高斯。此方法在保持高渲染质量的同时显著提高了渲染速度。给定两个具有显式GS表示的场景，在这项工作中，我们探索了它们之间的3D配准任务。为此，我们提出了GaussReg，一种新的从粗到细的框架，既快速又准确。粗略阶段遵循现有的点云配准方法，并从GS中估计点云的粗略对齐。我们进一步提出了一种图像引导的精细配准方法，该方法渲染GS中的图像，为精确对齐提供更详细的几何信息。为了支持全面评估，我们仔细构建了一个名为ScanNet GSReg的场景级数据集，其中包括从ScanNet数据集获得的1379个场景，并收集了一个称为GSReg。实验结果表明，我们的方法在多个数据集上实现了最先进的性能。我们的GaussReg比HLoc（SuperPoint作为特征提取器，SuperGlue作为匹配器）快44倍，精度相当。 et.al.|[2407.05254](http://arxiv.org/abs/2407.05254)|null|
|**2024-07-05**|**LaRa: Efficient Large-Baseline Radiance Fields**|辐射场方法已经实现了真实感的新视图合成和几何重建。但它们大多应用于逐场景优化或小基线设置。虽然最近的几项工作研究了通过利用变换器进行大基线的前馈重建，但它们都是以标准的全局注意力机制进行操作的，因此忽略了3D重建的局部性质。我们提出了一种在转换器层中统一局部和全局推理的方法，从而提高了质量和更快的收敛速度。我们的模型将场景表示为高斯体积，并将其与图像编码器和组注意力层相结合，以实现高效的前馈重建。实验结果表明，我们的模型在四个GPU上训练了两天，在重建360度辐射场时表现出了高保真度，并对零样本和域外测试表现出了鲁棒性。 et.al.|[2407.04699](http://arxiv.org/abs/2407.04699)|null|
|**2024-07-04**|**VEGS: View Extrapolation of Urban Scenes in 3D Gaussian Splatting using Learned Priors**|基于神经渲染的城市场景重建方法通常依赖于从驾驶车辆中收集的图像，其中摄像机面向前方并向前移动。尽管这些方法可以成功地从与训练相机轨迹相似的视图进行合成，但将新视图引导到训练相机分布之外并不能保证达到标准的性能。在本文中，我们通过评估关于训练相机分布的视图重建（如向左、向右或向下看）来解决外推视图合成（EVS）问题。为了提高EVS的渲染质量，我们通过构建密集的激光雷达图来初始化我们的模型，并提出利用先验场景知识，如表面法线估计器和大规模扩散模型。定性和定量比较证明了我们的方法在EVS上的有效性。据我们所知，我们是第一个解决城市场景重建中EVS问题的人。链接到我们的项目页面：https://vegs3d.github.io/. et.al.|[2407.02945](http://arxiv.org/abs/2407.02945)|null|
|**2024-07-03**|**Free-SurGS: SfM-Free 3D Gaussian Splatting for Surgical Scene Reconstruction**|手术场景的实时3D重建在计算机辅助手术中发挥着至关重要的作用，有望提高外科医生的可视性。3D高斯散射（3DGS）的最新进展显示出在一般场景的实时新颖视图合成方面的巨大潜力，该合成依赖于由运动结构（SfM）生成的精确姿态和点云进行初始化。然而，由于纹理最小和光度不一致的挑战，带有SfM的3DGS无法在手术场景中恢复准确的相机姿势和几何结构。为了解决这个问题，在本文中，我们提出了第一种基于无SfM的3DGS的手术场景重建方法，通过联合优化相机姿态和场景表示。基于视频连续性，我们的方法的关键是利用即时光流先验来引导从3D高斯导出的投影流。与以前大多数只依赖光度损失的方法不同，我们将姿态估计问题公式化为最小化投影流和光流之间的流量损失。进一步引入了一致性检查，通过检测满足核极几何的刚性可靠点来过滤流量异常值。在3D高斯优化过程中，我们随机采样帧以优化场景表示，从而逐步增长3D高斯。在SCARED数据集上的实验表明，与现有方法相比，我们在高效的新视图合成和姿态估计方面具有优越的性能。代码位于https://github.com/wrld/Free-SurGS. et.al.|[2407.02918](http://arxiv.org/abs/2407.02918)|**[link](https://github.com/wrld/free-surgs)**|

<p align=right>(<a href=#updated-on-20240710>back to top</a>)</p>

## 3D Reconstruction

|Publish Date|Title|Abstract|PDF|Code|
|---|---|---|---|---|
|**2024-07-09**|**Chat-Edit-3D: Interactive 3D Scene Editing via Text Prompts**|最近基于视觉语言预训练模型的图像内容处理工作已有效扩展到文本驱动的3D场景编辑。然而，现有的3D场景编辑方案仍然存在一定的缺陷，阻碍了其进一步的交互设计。这种方案通常坚持固定的输入模式，限制了用户在文本输入中的灵活性。此外，它们的编辑能力受到单个或几个2D视觉模型的约束，并且需要复杂的管道设计来将这些模型集成到3D重建过程中。为了解决上述问题，我们提出了一种基于对话的3D场景编辑方法，称为CE3D，该方法以一个大型语言模型为中心，该模型允许用户进行任意文本输入并解释他们的意图，从而促进相应视觉专家模型的自主调用。此外，我们设计了一种利用Hash Atlas来表示3D场景视图的方案，该方案将3D场景的编辑转移到2D Atlas图像上。这种设计实现了2D编辑和3D重建过程之间的完全解耦，使CE3D能够灵活地集成各种现有的2D或3D视觉模型，而无需复杂的融合设计。实验结果表明，CE3D有效地集成了多种视觉模型，实现了多样化的编辑视觉效果，具有较强的场景理解能力和多轮对话能力。代码可在<a href=“https://sk-fun.fun/CE3D“>此https URL</a> et.al.|[2407.06842](http://arxiv.org/abs/2407.06842)|null|
|**2024-07-09**|**Computer vision tasks for intelligent aerospace missions: An overview**|计算机视觉任务对航空航天任务至关重要，因为它们有助于航天器理解和解释空间环境，如估计位置和方向、重建3D模型和识别物体，这些都已被广泛研究以成功执行任务。然而，卡尔曼滤波、运动结构和多视图立体等传统方法不足以处理恶劣的条件，导致结果不可靠。近年来，基于深度学习（DL）的感知技术显示出巨大的潜力，并优于传统方法，尤其是在其对不断变化的环境的鲁棒性方面。为了进一步推进基于DL的航空航天感知，已经提出了各种框架、数据集和策略，表明了未来应用的巨大潜力。在这项调查中，我们旨在探索感知任务中使用的有前景的技术，并强调基于DL的航空航天感知的重要性。我们首先概述了航空航天感知，包括近年来开发的经典太空计划、常用传感器和传统感知方法。随后，我们深入研究了航空航天任务中的三个基本感知任务：姿态估计、三维重建和识别，因为它们对后续决策和控制至关重要。最后，我们讨论了当前研究的局限性和可能性，并展望了未来的发展，包括使用有限数据集的挑战、改进算法的必要性以及多源信息融合的潜在好处。 et.al.|[2407.06513](http://arxiv.org/abs/2407.06513)|null|
|**2024-07-09**|**LuSNAR:A Lunar Segmentation, Navigation and Reconstruction Dataset based on Muti-sensor for Autonomous Exploration**|随着月球探测任务的复杂性，月球需要有更高水平的自主性。环境感知和导航算法是月球车实现自主探测的基础。算法的开发和验证需要高度可靠的数据支持。现有的月球数据集大多针对单一任务，缺乏多样化的场景和高精度的地面实况标签。为了解决这个问题，我们提出了一个多任务、多场景、多标签的月球基准数据集LuSNAR。该数据集可用于自主感知和导航系统的综合评估，包括高分辨率立体图像对、全景语义标签、密集深度图、激光雷达点云和漫游车位置。为了提供更丰富的场景数据，我们基于虚幻引擎构建了9个月球模拟场景。每个场景都根据地形起伏和对象密度进行划分。为了验证数据集的可用性，我们评估和分析了语义分割、三维重建和自主导航的算法。实验结果证明，本文提出的数据集可用于自主环境感知和导航等任务的地面验证，并为测试算法指标的可访问性提供了月球基准数据集。我们将LuSNAR公开发布在：https://github.com/autumn999999/LuSNAR-dataset. et.al.|[2407.06512](http://arxiv.org/abs/2407.06512)|**[link](https://github.com/autumn999999/lusnar-dataset)**|
|**2024-07-08**|**Tailor3D: Customized 3D Assets Editing and Generation with Dual-Side Images**|3D AIGC的最新进展表明，它有望直接从文本和图像中创建3D对象，从而在动画和产品设计中显著节省成本。然而，3D资产的详细编辑和定制仍然是一个长期存在的挑战。具体而言，3D生成方法缺乏像2D图像创建方法那样精确地遵循精细详细指令的能力。想象一下，你可以通过3D AIGC获得一个玩具，但有不需要的配件和服装。为了应对这一挑战，我们提出了一种名为Tailor3D的新型管道，它可以从可编辑的双面图像中快速创建定制的3D资产。我们的目标是模仿裁缝局部更改对象或执行整体风格转换的能力。与从多个视图创建三维资源不同，使用双面图像可以消除编辑单个视图时出现的重叠区域冲突。具体来说，它首先编辑前视图，然后通过多视图扩散生成对象的后视图。之后，它继续编辑背面视图。最后，提出了一种双面LRM，将正面和背面的3D特征无缝缝合在一起，类似于裁缝将衣服的正面和背面缝合在一起。双面LRM纠正了前视图和后视图之间不完美的一致性，增强了编辑功能，减少了内存负担，同时将它们与LoRA Triplane Transformer无缝集成到统一的3D表示中。实验结果证明了Tailor3D在各种3D生成和编辑任务中的有效性，包括3D生成填充和样式转换。它为编辑三维资源提供了一个用户友好、高效的解决方案，每个编辑步骤只需几秒钟即可完成。 et.al.|[2407.06191](http://arxiv.org/abs/2407.06191)|null|
|**2024-07-06**|**Incremental Multiview Point Cloud Registration**|在本文中，我们提出了一种新的多视点云配准方法。与以往通常采用全局方案进行多视点配准的研究不同，我们建议采用增量流水线将扫描逐步对准到规范坐标系中。具体来说，我们的方法从基于图像的三维重建中获得灵感，首先通过扫描检索和几何验证构建稀疏扫描图。然后，我们通过初始化、下一次扫描选择和注册、Track create and continue以及Bundle Adjustment执行增量注册。此外，对于无检测器匹配器，我们引入了Track细化过程。该过程主要构建粗略的多视点配准，并通过调整轨迹上关键点的位置来细化模型。实验表明，该框架在三个基准数据集上的性能优于现有的多视点配准方法。代码位于https://github.com/Choyaa/IncreMVR. et.al.|[2407.05021](http://arxiv.org/abs/2407.05021)|null|
|**2024-07-05**|**LaRa: Efficient Large-Baseline Radiance Fields**|辐射场方法已经实现了真实感的新视图合成和几何重建。但它们大多应用于逐场景优化或小基线设置。虽然最近的几项工作研究了通过利用变换器进行大基线的前馈重建，但它们都是以标准的全局注意力机制进行操作的，因此忽略了3D重建的局部性质。我们提出了一种在转换器层中统一局部和全局推理的方法，从而提高了质量和更快的收敛速度。我们的模型将场景表示为高斯体积，并将其与图像编码器和组注意力层相结合，以实现高效的前馈重建。实验结果表明，我们的模型在四个GPU上训练了两天，在重建360度辐射场时表现出了高保真度，并对零样本和域外测试表现出了鲁棒性。 et.al.|[2407.04699](http://arxiv.org/abs/2407.04699)|null|
|**2024-07-05**|**Rethinking Data Input for Point Cloud Upsampling**|近年来，点云上采样在三维重建和曲面生成等领域得到了广泛的应用。然而，现有的点云上采样输入都是基于补丁的，并且没有研究讨论点云模型全输入和基于补丁的输入之间的差异和原理。为了与基于补丁的点云输入进行比较，本文提出了一种新的数据输入方法，该方法在训练PU-GCN时划分全点云模型以确保形状完整性。本文在PU1K和ABC数据集上进行了验证，但结果表明，基于补丁的性能优于基于模型的全输入，即平均分段输入。因此，本文探讨了影响点云上采样结果的数据输入因素和模型模块。 et.al.|[2407.04476](http://arxiv.org/abs/2407.04476)|null|
|**2024-07-05**|**GSD: View-Guided Gaussian Splatting Diffusion for 3D Reconstruction**|我们提出了一种基于高斯散射（GS）表示的扩散模型方法GSD，用于从单个视图重建3D对象。先前的作品由于不正确的表示而遭受不一致的3D几何结构或平庸的渲染质量。我们通过利用最近最先进的3D显式表示、高斯散射和无条件扩散模型，朝着解决这些缺点迈出了一步。该模型学习生成由GS椭球集合表示的3D对象。有了这些强大的生成3D先验，尽管无条件地学习，但扩散模型可以在没有进一步模型微调的情况下进行视图引导重建。这是通过高效而灵活的飞溅函数和引导的去噪采样过程传播细粒度的2D特征来实现的。此外，还采用2D扩散模型来增强渲染保真度，并通过抛光和重新使用渲染图像来提高重建的GS质量。最终重建的对象明确地具有高质量的3D结构和纹理，并且可以在任意视图中有效地渲染。在具有挑战性的真实世界CO3D数据集上的实验证明了我们方法的优越性。 et.al.|[2407.04237](http://arxiv.org/abs/2407.04237)|null|
|**2024-07-04**|**SfM on-the-fly: Get better 3D from What You Capture**|在过去的二十年里，运动结构（SfM）一直是摄影测量、计算机视觉、机器人等领域的研究热点，而实时性能正是最近人们越来越感兴趣的话题。这项工作建立在原始的动态SfM（Zhan et al.，2024）的基础上，并提出了一个更新版本，其中包含三个新的进步，以从您捕获的图像中获得更好的3D效果：（i）通过使用分层导航小世界（HNSW）图，进一步增强了实时图像匹配，从而更快地识别出更多真实的正重叠图像候选者；（ii）提出了一种自适应加权策略，用于鲁棒的分层局部束调整，以改进SfM结果；（iii）包括多个代理用于支持协作SfM，并且当出现共同注册的图像时将多个3D重建无缝地合并到完整的3D场景中。各种综合实验表明，所提出的SfM方法（实时命名为SfMv2）可以以高效的方式生成更完整、更稳健的3D重建。代码位于http://yifeiyu225.github.io/on-the-flySfMv2.github.io/. et.al.|[2407.03939](http://arxiv.org/abs/2407.03939)|null|
|**2024-07-04**|**Beyond Viewpoint: Robust 3D Object Recognition under Arbitrary Views through Joint Multi-Part Representation**|现有的基于视图的方法擅长于从预定义的视点识别3D对象，但它们在任意视图下的识别探索是有限的。这是一个具有挑战性和现实性的设置，因为每个对象都有不同的视点位置和数量，并且它们的姿势不对齐。然而，大多数基于视图的方法，即聚合多个视图特征以获得全局特征表示，很难解决任意视图下的三维对象识别问题。由于来自任意视图的未对齐输入，稳健地聚合特征是一项挑战，导致性能下降。在本文中，我们介绍了一种新的部件感知网络（PANet），它是一种基于部件的表示，以解决这些问题。这种基于零件的表示旨在定位和理解3D对象的不同零件，如飞机机翼和尾部。它具有视点不变性和旋转鲁棒性等特性，这使它在解决任意视图下的三维对象识别问题时具有优势。我们在基准数据集上的结果清楚地表明，对于任意视图下的3D对象识别任务，我们提出的方法优于现有的基于视图的聚合基线，甚至超过了大多数固定视点方法。 et.al.|[2407.03842](http://arxiv.org/abs/2407.03842)|null|

<p align=right>(<a href=#updated-on-20240710>back to top</a>)</p>

## Diffusion

|Publish Date|Title|Abstract|PDF|Code|
|---|---|---|---|---|
|**2024-07-09**|**ConceptExpress: Harnessing Diffusion Models for Single-image Unsupervised Concept Extraction**|虽然个性化的文本到图像生成使得能够从多个图像中学习单个概念，但更实用但更具挑战性的场景涉及在单个图像中学习多个概念。然而，处理这种情况的现有工作在很大程度上依赖于大量的人工注释。在本文中，我们介绍了一个名为无监督概念提取（UCE）的新任务，该任务考虑了一个没有任何人类概念知识的无监督环境。给定一个包含多个概念的图像，该任务旨在仅依靠预训练的扩散模型中的现有知识来提取和重新创建单个概念。为了实现这一点，我们提出了ConceptExpress，它通过在两个方面释放预训练扩散模型的固有能力来解决UCE问题。具体而言，概念定位方法通过利用扩散自注意的空间对应关系，自动定位和解开显著概念；并且基于概念和概念令牌之间的查找关联，概念优化过程学习表示每个单独概念的判别令牌。最后，我们建立了一个针对UCE任务量身定制的评估协议。大量实验表明，ConceptExpress是UCE任务的一个很有前途的解决方案。我们的代码和数据可在以下网址获取：https://github.com/haoosz/ConceptExpress et.al.|[2407.07077](http://arxiv.org/abs/2407.07077)|**[link](https://github.com/haoosz/conceptexpress)**|
|**2024-07-09**|**Category-level Object Detection, Pose Estimation and Reconstruction from Stereo Images**|我们研究了3D对象理解任务，用于操纵具有不同材质特性（漫反射、镜面反射、透明和混合）的日常对象。现有的单目和RGB-D方法由于缺少或不精确的深度测量而存在尺度模糊性。我们提出了CODERS，这是一种从立体图像中进行类别级目标检测、姿态估计和重建的一阶段方法。我们的流水线的基础是一个隐式立体匹配模块，它将立体图像特征与3D位置信息相结合。将该模块与下面的变换解码器架构连接起来，可以实现机器人操作所需的多个任务的端到端学习。我们的方法显著优于公共TOD数据集中的所有竞争方法。此外，在模拟数据上训练后，CODERS可以很好地推广到真实世界机器人操纵实验中看不见的类别级对象实例。我们的数据集、代码和演示将在我们的项目页面上提供。 et.al.|[2407.06984](http://arxiv.org/abs/2407.06984)|null|
|**2024-07-09**|**RodinHD: High-Fidelity 3D Avatar Generation with Diffusion Models**|我们介绍了RodinHD，它可以从肖像图像中生成高保真度的3D化身。现有的方法无法捕捉复杂的细节，例如我们在本文中处理的发型。我们首先确定了一个被忽视的灾难性遗忘问题，该问题是由MLP解码器共享方案引起的，当在许多化身上顺序拟合三条线时出现的。为了克服这个问题，我们提出了一种新的数据调度策略和权重合并正则项，它提高了解码器渲染更清晰细节的能力。此外，我们通过计算捕捉丰富2D纹理线索的细粒度层次表示，并通过交叉关注将其注入多层3D扩散模型，来优化肖像图像的引导效果。当在46K个具有针对三平面优化的噪声调度的化身上进行训练时，所得到的模型可以生成具有比以前的方法明显更好的细节的3D化身，并且可以推广到狂野的肖像输入。 et.al.|[2407.06938](http://arxiv.org/abs/2407.06938)|null|
|**2024-07-09**|**HumanRefiner: Benchmarking Abnormal Human Generation and Refining with Coarse-to-fine Pose-Reversible Guidance**|文本到图像的扩散模型在条件图像生成方面有了显著的进步。然而，这些模型通常难以准确渲染以人类为特征的图像，导致四肢扭曲和其他异常。这个问题主要源于扩散模型中对肢体质量的识别和评估不足。为了解决这个问题，我们介绍了AbHuman，这是第一个专注于解剖异常的大规模合成人体基准。该基准由56K幅合成的人类图像组成，每幅图像都用详细的边界框级标签进行注释，识别出18个不同类别中的147K幅人类异常。基于此，可以建立对人类异常的识别，从而通过负面提示和引导等传统技术增强图像生成。为了进一步推动改进，我们提出了HumanRefiner，这是一种新的即插即用方法，用于在文本到图像生成中对人类异常进行粗略到精细的细化。具体而言，HumanRefiner利用自诊断程序来检测和纠正与粗粒度异常人体姿势和细粒度异常水平相关的问题，从而促进姿势可逆扩散的生成。AbHuman基准的实验结果表明，HumanRefiner显著减少了生成差异，与最先进的开源生成器SDXL相比，肢体质量提高了2.9倍，在人体评估中比DALL-E 3提高了1.4倍。我们的数据和代码可在https://github.com/Enderfga/HumanRefiner. et.al.|[2407.06937](http://arxiv.org/abs/2407.06937)|**[link](https://github.com/enderfga/humanrefiner)**|
|**2024-07-09**|**Dissipation enhancing properties for a class of Hamiltonian flows with closed streamlines**|我们研究了在二维有界域上受分子扩散和不可压缩速度场平流的被动标量的演化。速度场是 $u=\nabla^\perpH$，其中H是一个自治的哈密顿量，其水平集是对域进行叶化的Jordan曲线。我们专注于高P\’clet数制度（$Pe:=\nu^｛-1｝\gg 1$），其中两个不同的过程在分离良好的时间尺度上展开：流线平均和标准扩散。对于一类具有一个非退化椭圆点的哈密顿量（包括扰动径向流），我们证明了解在次扩散时间尺度$T_\nu\ll\nu^{-1}$上对其流线平均值的指数收敛性，直到与流线形状相关的小校正。时间尺度$T_\nu$ 由椭圆点周围的周期函数的行为决定。为了建立这一结果，我们引入了一个模型问题，该问题自然产生于解与其流线平均值之间的差异。我们使用伪谱估计来推断模型问题中的衰变，事实上，这种分析扩展到更广泛的一类哈密顿流。最后，我们对全解进行了渐近展开，揭示了前导项由流线平均值和模型问题的解组成。 et.al.|[2407.06884](http://arxiv.org/abs/2407.06884)|null|
|**2024-07-09**|**Relation between asymptotic $L_p$-convergence and some classical modes of convergence**|渐近$L_p$-收敛类似于$L_p$中的收敛，是在cite｛alves2024模式｝中引入的，其动机是扩散松弛中的一个问题。本文的主要目的是比较渐近$L_p$-收敛性与弱$L_p$空间和测度上的收敛性。所得到的结果之一提供了有限测度空间上测度收敛的渐近$L_p$ -收敛性的特征。 et.al.|[2407.06830](http://arxiv.org/abs/2407.06830)|null|
|**2024-07-09**|**AstroSpy: On detecting Fake Images in Astronomy via Joint Image-Spectral Representations**|人工智能生成图像的流行引发了人们对天文图像真实性的担忧，尤其是在稳定扩散等先进的文本到图像模型产生高度逼真的合成样本的情况下。现有的检测方法，主要基于卷积神经网络（CNNs）或频谱分析，在独立使用时具有局限性。我们介绍了AstroSpy，这是一个综合了光谱和图像特征的混合模型，用于区分真实天文图像和合成天文图像。AstroSpy在一个由NASA真实图像和人工智能生成的赝品（约18k个样本）组成的独特数据集上进行训练，利用双路径架构融合空间和光谱信息。这种方法使AstroSpy能够在识别真实天文图像方面实现卓越的性能。广泛的评估证明了AstroSpy的有效性和稳健性，在域内和跨域任务中都显著优于基线模型，突出了其打击天文学错误信息的潜力。 et.al.|[2407.06817](http://arxiv.org/abs/2407.06817)|null|
|**2024-07-09**|**A reaction-diffusion model for relapsing-remitting multiple sclerosis with a treatment term**|我们提出了一项基于反应扩散系统的多发性硬化症发展的数学研究。该模型描述了不同人群的人类细胞之间的相互作用、细胞因子刺激的免疫细胞的运动、异常活化的淋巴细胞导致的髓鞘消耗以及少突胶质细胞对髓鞘的修复。接下来，我们介绍了一个代表注射低剂量IL-2白细胞介素的治疗术语。一个自然的步骤是研究系统，通过对问题的图灵不稳定性分析来研究空间模式的形成。特别是，在非治疗和治疗的情况下，我们得到了随时间振荡的空间模式，这些模式可能会再现病理早期的脑损伤特征。 et.al.|[2407.06802](http://arxiv.org/abs/2407.06802)|null|
|**2024-07-09**|**Investigating the Kinetic Effects on Current Gradient-Driven Instabilities of Electron Current Layers via Particle-in-Cell Simulations**|电子电流层在各种自然等离子体和实验室等离子体中形成，并且容易受到几种不稳定性的影响。由电流梯度驱动的撕裂是这些层中一个突出的不稳定性，被认为是无碰撞状态下磁重联的潜在机制。电子惯性是导致磁力线断裂并随后重新连接的非理想因素。另一种由电流梯度驱动的模式，称为表面保持模式，保持磁场拓扑。我们使用二维粒子细胞模拟（使用OSIRIS代码库实现）研究了在有限电子温度存在的情况下对这些模式的动力学影响。除了在低温下，由于电子拉莫尔半径的增加和随后的磁场扩散，温度在很大程度上稳定了撕裂模式。引入均匀引导场表明，由于等离子体β的减少，生长速率在更高的温度下降低。相反，对于表面保护模式，生长速率随着温度的升高而增加，这可能是由于电子流速度的提高。撕裂模和保表面模共存的混合模表现出不对称磁重联的不对称结构特征。最后，我们在研究结果的基础上提出了未来的研究方向。 et.al.|[2407.06799](http://arxiv.org/abs/2407.06799)|null|
|**2024-07-09**|**Extinction profiles for the Sobolev critical fast diffusion equation in bounded domains. I. One bubble dynamics**|本文研究了具有Dirichlet零边界条件的有界光滑域中Sobolev临界快速扩散方程非负解的消光行为。在对初始数据的两个气泡能量阈值假设下，我们证明了一个二分法，即每个解在相对误差方面一致收敛于稳态或鼓泡。 et.al.|[2407.06757](http://arxiv.org/abs/2407.06757)|null|

<p align=right>(<a href=#updated-on-20240710>back to top</a>)</p>

## NeRF

|Publish Date|Title|Abstract|PDF|Code|
|---|---|---|---|---|
|**2024-07-03**|**Cerebral cortex inspired representation of neural field network**|进化论及其智力元素在探索中带来了刺激和挑战。然而，物种如何拥有记忆、恢复记忆并保持连续性是根本问题。大多数现象只能由研究人员进行假设，通过实验验证这些现象是一个巨大的挑战。将大脑视为理想的智能机器并对其进行建模，为计算算法开辟了新的维度。本文提出了一个类似大脑皮层记忆创造的假说。大脑皮层的区域隐含着特定的功能，构成了一维的矢量形式的神经场。整个皮层的神经场相互连接，形成了一个网络。这些网络与生存本能、情绪和奖励相关联，构成了对暴露环境的记忆，比如学习。具有多维控制点的图形工具NURBS隐含地用于将这些网络表示为一组三次方程。通过数据进行学习是智能系统的主要组成部分，本文试图将数据转换为低维模式，而不是现有的绝对形式，以实现实时智能系统。 et.al.|[2407.04741](http://arxiv.org/abs/2407.04741)|null|
|**2024-07-01**|**Fast and Efficient: Mask Neural Fields for 3D Scene Segmentation**|理解3D场景是计算机视觉研究中的一个关键挑战，其应用涉及多个领域。在将2D视觉语言基础模型提取到神经领域（如NeRF和3DGS）方面的最新进展，使得能够从2D多视图图像中对3D场景进行开放式词汇分割，而无需精确的3D注释。然而，虽然有效，但高维CLIP特征的每像素提取引入了模糊性，并需要复杂的正则化策略，从而增加了训练过程中的低效率。本文提出了MaskField，它可以在弱监督下使用神经场实现快速高效的三维开放词汇分割。与以前的方法不同，MaskField提取的是遮罩，而不是密集的高维CLIP特征。MaskFields使用神经场作为二进制掩码生成器，并使用SAM生成的掩码对其进行监督，并根据粗略的CLIP特征进行分类。MaskField通过在训练过程中自然引入SAM分割的对象形状而无需额外的正则化，克服了模糊的对象边界。通过避免在训练过程中直接处理高维CLIP特征，MaskField与3DGS等显式场景表示特别兼容。我们的大量实验表明，MaskField不仅超越了现有的最先进的方法，而且实现了显著的快速收敛，仅需5分钟的训练就超过了以前的方法。我们希望MaskField将激励人们进一步探索如何训练神经场来从2D模型中理解3D场景。 et.al.|[2407.01220](http://arxiv.org/abs/2407.01220)|null|
|**2024-07-01**|**3D Feature Distillation with Object-Centric Priors**|将自然语言与物理世界联系起来是一个普遍存在的话题，在计算机视觉和机器人领域有着广泛的应用。最近，像CLIP这样的2D视觉语言模型已经被广泛普及，因为它们在2D图像中具有令人印象深刻的开放词汇基础能力。最近的工作旨在通过特征提取将2D CLIP特征提升到3D，但要么学习特定于场景的神经场，因此缺乏泛化能力，要么专注于需要访问多个相机视图的室内房间扫描数据，这在机器人操作场景中是不现实的。此外，相关方法通常在像素级融合特征，并假设所有相机视图的信息量相等。在这项工作中，我们证明了这种方法在基础精度和分割清晰度方面都会导致次优的3D特征。为了缓解这种情况，我们提出了一种多视图特征融合策略，该策略采用以对象为中心的先验来消除基于语义信息的无信息视图，并通过实例分割掩码在对象级别融合特征。为了提取我们以对象为中心的3D特征，我们生成了一个杂乱桌面场景的大规模合成多视图数据集，从3300多个独特的对象实例中生成了15k个场景，并将其公开。我们表明，我们的方法在从单视图RGB-D重建3D CLIP特征的同时，具有改进的接地能力和空间一致性，从而偏离了测试时多个相机视图的假设。最后，我们证明了我们的方法可以推广到新的桌面领域，并在不进行微调的情况下重新用于3D实例分割，并证明了它在语言引导的机器人抓取中的实用性 et.al.|[2406.18742](http://arxiv.org/abs/2406.18742)|null|
|**2024-06-25**|**Masked Generative Extractor for Synergistic Representation and 3D Generation of Point Clouds**|在2D图像生成建模和表示学习领域，掩模生成编码器（MAGE）已经证明了生成建模与表示学习之间的协同潜力。受此启发，我们提出了Point MAGE，将这一概念扩展到点云数据。具体而言，该框架首先利用矢量量化变分自动编码器（VQVAE）来重建3D形状的神经场表示，从而学习点块的离散语义特征。随后，通过将掩蔽模型与可变掩蔽比相结合，我们实现了生成和表示学习的同步训练。此外，我们的框架与现有的点云自监督学习（SSL）模型无缝集成，从而提高了它们的性能。我们广泛评估了Point MAGE的表示学习和生成能力。在形状分类任务中，Point MAGE在ModelNet40数据集上的准确率为94.2%，在ScanObjectNN数据集上达到92.9%（+1.3%）。此外，它在少量镜头学习和零件分割任务中实现了最先进的性能。实验结果还证实，点MAGE可以在无条件和有条件的设置中生成详细和高质量的3D形状。 et.al.|[2406.17342](http://arxiv.org/abs/2406.17342)|null|
|**2024-06-17**|**DistillNeRF: Perceiving 3D Scenes from Single-Glance Images by Distilling Neural Fields and Foundation Model Features**|我们提出了DistilleNeRF，这是一种自监督学习框架，解决了在自动驾驶中从有限的2D观测中理解3D环境的挑战。我们的方法是一个可推广的前馈模型，它从稀疏的单帧多视图相机输入中预测丰富的神经场景表示，并通过可微分渲染进行自监督训练，以重建RGB、深度或特征图像。我们的第一个见解是通过生成密集的深度和虚拟相机目标进行训练，利用每场景优化的神经辐射场（NeRF），从而帮助我们的模型从稀疏的非重叠图像输入中学习3D几何。其次，为了学习语义丰富的3D表示，我们建议从预先训练的2D基础模型（如CLIP或DINOv2）中提取特征，从而实现各种下游任务，而不需要昂贵的3D人工注释。为了利用这两个见解，我们引入了一种新的模型架构，该架构具有两级提升-飞溅-拍摄编码器和参数化稀疏分层体素表示。在NuScenes数据集上的实验结果表明，DistilleNeRF在场景重建、新视图合成和深度估计方面显著优于现有的可比自监督方法；并且它允许竞争性的零样本3D语义占用预测，以及通过提取的基础模型特征来理解开放世界场景。演示和代码将在https://distillnerf.github.io/. et.al.|[2406.12095](http://arxiv.org/abs/2406.12095)|null|
|**2024-06-18**|**Effective Rank Analysis and Regularization for Enhanced 3D Gaussian Splatting**|从多视图图像中进行三维重建是计算机视觉和图形学的基本挑战之一。近年来，三维高斯散射（3DGS）已经成为一种很有前途的技术，能够实时渲染和高质量的三维重建。该方法利用了三维高斯表示和基于瓦片的飞溅技术，绕过了昂贵的神经场查询。尽管3DGS具有潜力，但由于高斯收敛为具有一个主导方差的各向异性高斯，3DGS仍面临挑战，包括针状伪影、次优几何结构和不准确法线。我们建议使用有效秩分析来检查3D高斯基元的形状统计，并识别高斯确实收敛为有效秩为1的针状形状。为了解决这个问题，我们引入了有效秩作为正则化，它约束高斯的结构。我们的新正则化方法增强了法线和几何重建，同时减少了针状伪影。该方法可以作为附加模块集成到其他3DGS变体中，在不影响视觉逼真度的情况下提高其质量。 et.al.|[2406.11672](http://arxiv.org/abs/2406.11672)|null|
|**2024-06-13**|**Well-posedness and regularity of solutions to neural field problems with dendritic processing**|我们研究了最近提出的神经场模型的解决方案，在该模型中，树突被建模为源自体细胞层的垂直纤维的连续体。由于电压通过具有非局部源的电缆方程沿树枝状方向传播，因此该模型具有各向异性扩散算子以及突触耦合的积分项。因此，相应的柯西问题与经典的神经场方程明显不同。我们证明了问题的弱公式允许一个唯一的解，嵌入估计类似于非线性局部反应扩散方程的嵌入估计。我们的分析依赖于无扩散问题的扰动弱解，即标准神经场，迄今为止尚未对其弱问题进行研究。我们找到了有扩散和无扩散问题的严格渐近估计，并证明了这两个模型的解在有限时间间隔上在适当的范数下保持接近。我们提供了微扰结果的数值证据。 et.al.|[2406.09222](http://arxiv.org/abs/2406.09222)|null|
|**2024-06-13**|**Preserving Identity with Variational Score for General-purpose 3D Editing**|我们提出了Piva（用变分分数蒸馏保持同一性），这是一种新的基于优化的方法，用于编辑基于扩散模型的图像和3D模型。具体来说，我们的方法受到了最近提出的2D图像编辑方法——德尔塔去噪分数（DDS）的启发。我们指出了DDS在二维和三维编辑中的局限性，这会导致细节丢失和过饱和。为了解决这一问题，我们提出了一个额外的分数提取术语，以强制执行身份保护。这导致了更稳定的编辑过程，逐步优化NeRF模型以匹配目标提示，同时保留关键的输入特征。我们证明了我们的方法在零样本图像和神经场编辑中的有效性。我们的方法成功地改变了视觉属性，添加了微妙和实质性的结构元素，转换了形状，并在标准的2D和3D编辑基准上取得了有竞争力的结果。此外，我们的方法没有施加任何约束，如掩蔽或预训练，使其与广泛的预训练扩散模型兼容。这允许进行多功能编辑，而不需要神经场到网格的转换，提供更用户友好的体验。 et.al.|[2406.08953](http://arxiv.org/abs/2406.08953)|null|
|**2024-06-12**|**Category-level Neural Field for Reconstruction of Partially Observed Objects in Indoor Environment**|通过各种成功案例，神经隐式表示在三维重建中引起了人们的关注。对于进一步的应用，如场景理解或编辑，一些作品已经显示出在对象组成重建方面的进展。尽管它们在观测区域具有优越的性能，但在重建部分观测到的对象时，它们的性能仍然有限。为了更好地处理这个问题，我们引入了类别级神经场，该神经场在场景中属于同一类别的对象之间学习有意义的公共3D信息。我们的主要想法是根据观察到的形状对对象进行子分类，以便更好地训练类别级模型。然后，我们利用神经场，通过选择基于射线的不确定性选择的代表性对象并与之对齐，来执行配准部分观测对象的挑战性任务。在模拟和真实世界数据集上的实验表明，我们的方法改进了几个类别的未观察零件的重建。 et.al.|[2406.08176](http://arxiv.org/abs/2406.08176)|**[link](https://github.com/Taekbum/category-nerf-reconstruction-official)**|
|**2024-06-12**|**OpenObj: Open-Vocabulary Object-Level Neural Radiance Fields with Fine-Grained Understanding**|近年来，人们对由视觉语言模型（VLM）促进的开放词汇三维场景重建产生了浓厚的兴趣，VLM在开放集检索中展示了非凡的能力。然而，现有的方法面临一些局限性：它们要么专注于学习逐点特征，导致语义理解模糊，要么只处理对象级重建，从而忽略对象内部的复杂细节。为了应对这些挑战，我们引入了OpenObj，这是一种创新的方法，用于构建具有细粒度理解的开放词汇表对象级神经辐射场（NeRF）。从本质上讲，OpenObj建立了一个健壮的框架，用于在对象级别进行高效和严密的场景建模和理解。此外，我们将零件级特征融入神经领域，从而实现物体内部的细致入微的表示。这种方法捕获对象级实例，同时保持细粒度的理解。在多个数据集上的结果表明，OpenObj在零样本语义分割和检索任务中取得了优异的性能。此外，OpenObj支持多尺度的真实世界机器人任务，包括全局移动和局部操纵。 et.al.|[2406.08009](http://arxiv.org/abs/2406.08009)|**[link](https://github.com/BIT-DYN/OpenObj)**|

<p align=right>(<a href=#updated-on-20240710>back to top</a>)</p>

[contributors-shield]: https://img.shields.io/github/contributors/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[contributors-url]: https://github.com/Vincentqyw/cv-arxiv-daily/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[forks-url]: https://github.com/Vincentqyw/cv-arxiv-daily/network/members
[stars-shield]: https://img.shields.io/github/stars/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[stars-url]: https://github.com/Vincentqyw/cv-arxiv-daily/stargazers
[issues-shield]: https://img.shields.io/github/issues/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[issues-url]: https://github.com/Vincentqyw/cv-arxiv-daily/issues

