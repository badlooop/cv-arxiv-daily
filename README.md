[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]

## Updated on 2024.07.13
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
|**2024-07-10**|**Generative Image as Action Models**|图像生成扩散模型已经过微调，以解锁图像编辑和新颖的视图合成等新功能。我们能否同样解锁用于视觉运动控制的图像生成模型？我们介绍了GENIMA，这是一种行为克隆代理，可以微调稳定扩散，在RGB图像上“绘制联合动作”作为目标。这些图像被输入控制器，该控制器将视觉目标映射到一系列关节位置。我们在25个RLBench和9个真实操作任务上研究了GENIMA。我们发现，通过将动作提升到图像空间，互联网预训练的扩散模型可以生成优于最先进的视觉运动方法的策略，特别是在对场景扰动的鲁棒性和对新对象的泛化方面。我们的方法也与3D代理竞争，尽管缺乏深度、关键点或运动规划等先验知识。 et.al.|[2407.07875](http://arxiv.org/abs/2407.07875)|null|
|**2024-07-10**|**Controlling Space and Time with Diffusion Models**|我们提出了4DiM，这是一种用于4D新颖视图合成（NVS）的级联扩散模型，以一般场景的一个或多个图像以及一组相机姿态和时间戳为条件。为了克服由于4D训练数据可用性有限而带来的挑战，我们提倡对3D（有相机姿势）、4D（姿势+时间）和视频（时间但没有姿势）数据进行联合训练，并提出了一种新的架构来实现这一点。我们进一步主张使用单目度量深度估计器对SfM姿态数据进行校准，以实现度量尺度相机控制。对于模型评估，我们引入了新的度量来丰富和克服当前评估方案的缺点，与现有的3D NVS扩散模型相比，在保真度和姿态控制方面展示了最先进的结果，同时增加了处理时间动态的能力。4DiM还用于改进全景拼接、姿势调节的视频到视频翻译以及其他一些任务。有关概述，请参阅https://4d-diffusion.github.io et.al.|[2407.07860](http://arxiv.org/abs/2407.07860)|null|
|**2024-07-09**|**Reference-based Controllable Scene Stylization with Gaussian Splatting**|基于内容对齐的参考图像编辑外观的基于参考的场景样式化是一个新兴的研究领域。从预训练的神经辐射场（NeRF）开始，现有的方法通常会学习与给定风格相匹配的新颖外观。尽管它们很有效，但它们固有地存在耗时的体绘制问题，因此对于许多实时应用程序来说是不切实际的。在这项工作中，我们提出了ReGS，它将3D高斯散点（3DGS）应用于基于参考的风格化，以实现实时风格化的视图合成。编辑预训练3DGS的外观具有挑战性，因为它使用离散高斯作为3D表示，将外观与几何体紧密结合。像现有方法那样简单地优化外观通常不足以在给定的参考图像中对连续纹理进行建模。为了应对这一挑战，我们提出了一种新的纹理引导控制机制，该机制自适应地将局部负责的高斯分布调整为新的几何排列，以获得所需的纹理细节。所提出的过程以纹理线索为指导，进行有效的外观编辑，并根据场景深度进行正则化，以保持原始几何结构。通过这些新颖的设计，我们证明ReG可以产生最先进的风格化结果，这些结果尊重参考纹理，同时为自由视图导航提供实时渲染速度。 et.al.|[2407.07220](http://arxiv.org/abs/2407.07220)|null|
|**2024-07-08**|**RRM: Relightable assets using Radiance guided Material extraction**|在过去几年中，在任意光照下合成NeRF已成为一个具有开创性的问题。最近的努力通过提取基于物理的参数来解决这个问题，这些参数可以在任意光照下渲染，但它们在可以处理的场景范围内是有限的，通常是对光滑场景的处理不当。我们提出了RRM，这是一种即使在存在高反射物体的情况下也可以提取场景的材质、几何形状和环境照明的方法。我们的方法包括一个基于物理参数的物理感知辐射场表示，以及一个基于拉普拉斯金字塔的富有表现力的环境光结构。我们证明，我们的贡献在参数检索任务上优于最先进的技术，从而在表面场景上实现了高保真的重新照明和新颖的视图合成。 et.al.|[2407.06397](http://arxiv.org/abs/2407.06397)|null|
|**2024-07-08**|**PanDORA: Casual HDR Radiance Acquisition for Indoor Scenes**|大多数新颖的视图合成方法，如NeRF，都无法捕捉场景的真实高动态范围（HDR）辐射，因为它们通常是在用标准低动态范围（LDR）相机捕获的照片上训练的。虽然以不同曝光捕获多幅图像的传统曝光包围方法最近已被应用于多视图情况，但我们发现这些方法无法捕获室内场景的全部动态范围，其中包括非常明亮的光源。本文介绍了PanDORA：一种全景双观察者辐射采集系统，用于在高动态范围内随意捕捉室内场景。我们提出的系统包括两个固定在便携式三脚架上的360度相机。摄像机同时采集两个360度视频：一个以常规曝光，另一个以非常快的曝光，使用户可以在几分钟内随意地在场景中挥动设备。生成的图像被馈送到基于NeRF的算法，该算法重建场景的完整高动态范围。与之前工作的HDR基线相比，我们的方法在不牺牲视觉质量的情况下重建了室内场景的完整HDR辐射，同时保留了最近类似NeRF的方法的易捕获性。 et.al.|[2407.06150](http://arxiv.org/abs/2407.06150)|null|
|**2024-07-08**|**PerlDiff: Controllable Street View Synthesis Using Perspective-Layout Diffusion Models**|可控生成被认为是解决注释3D数据挑战的一种潜在的重要方法，在自动驾驶数据生产的背景下，这种可控生成的精度变得尤为重要。现有的方法侧重于将各种生成信息整合到控制输入中，利用GLIGEN或ControlNet等框架，在可控生成中产生值得称赞的结果。然而，这种方法本质上将生成性能限制在预定义网络架构的学习能力上。本文探讨了控制信息的集成，并介绍了PerlDiff（透视布局扩散模型），这是一种充分利用透视3D几何信息的有效街景图像生成方法。我们的PerlDiff采用3D几何先验来指导街道视图图像的生成，并在网络学习过程中进行精确的对象级控制，从而产生更稳健和可控的输出。此外，与其他布局控制方法相比，它表现出更优的可控性。实证结果证明，我们的PerlDiff显著提高了NuScenes和KITTI数据集的生成精度。我们的代码和模型可在以下网址公开获取https://github.com/LabShuHangGU/PerlDiff. et.al.|[2407.06109](http://arxiv.org/abs/2407.06109)|**[link](https://github.com/labshuhanggu/perldiff)**|
|**2024-07-08**|**OSN: Infinite Representations of Dynamic 3D Scenes from Monocular Videos**|长期以来，从单眼RGB视频中恢复底层动态3D场景表示一直是一个挑战。现有的工作将这个问题表述为通过添加各种约束（如深度先验和强几何约束）来找到一个最合理的解决方案，忽略了一个动态视频可能对应无限多个3D场景表示的事实。在本文中，我们的目标是学习与输入视频匹配的所有合理的3D场景配置，而不仅仅是推断一个特定的配置。为了实现这一宏伟目标，我们引入了一个名为OSN的新框架。我们方法的关键是一个简单而创新的对象比例网络，以及一个联合优化模块，为每个动态3D对象学习精确的比例范围。这使我们能够对尽可能多的忠实3D场景配置进行采样。大量实验表明，我们的方法超越了所有基线，在多个合成和真实世界数据集上的动态新视图合成中取得了卓越的精度。最值得注意的是，我们的方法在学习细粒度3D场景几何方面具有明显的优势。我们的代码和数据可在https://github.com/vLAR-group/OSN et.al.|[2407.05615](http://arxiv.org/abs/2407.05615)|**[link](https://github.com/vlar-group/osn)**|
|**2024-07-08**|**GeoNLF: Geometry guided Pose-Free Neural LiDAR Fields**|尽管最近的努力将神经辐射场（NeRF）扩展到了LiDAR点云合成中，但大多数现有工作都表现出对预先计算的姿态的强烈依赖。然而，点云配准方法难以实现精确的全局姿态估计，而之前的无姿态NeRF在全局重建中忽略了几何一致性。鉴于此，我们探索了点云的几何见解，为重建提供了明确的配准先验。基于此，我们提出了几何引导神经激光雷达场（GeoNLF），这是一种交替执行全局神经重建和纯几何姿态优化的混合框架。此外，在稀疏视图输入下，NeRF倾向于过拟合单个帧，很容易陷入局部最小值。为了解决这个问题，我们开发了一种选择性重新加权策略，并引入了用于鲁棒优化的几何约束。在NuScenes和KITTI-360数据集上的广泛实验证明了GeoNLF在低频大尺度点云的新颖视图合成和多视图配准方面的优越性。 et.al.|[2407.05597](http://arxiv.org/abs/2407.05597)|null|
|**2024-07-08**|**Dynamic Neural Radiance Field From Defocused Monocular Video**|最近，单眼视频的动态神经辐射场（NeRF）被探索用于时空新颖视图合成，并取得了优异的结果。然而，在视频捕获中经常会出现由深度变化引起的散焦模糊，这会影响动态重建的质量，因为缺乏清晰的细节会干扰输入视图之间的建模时间一致性。为了解决这个问题，我们提出了D2RF，这是第一种动态NeRF方法，旨在从散焦单眼视频中恢复清晰新颖的视图。我们引入分层景深（DoF）体绘制来模拟散焦模糊，并在散焦视图的监督下重建清晰的NeRF。模糊模型的灵感来自DoF渲染和体绘制之间的联系。体绘制中的不透明度与DoF渲染中的层可见性相一致。为了执行模糊，我们将分层模糊核修改为基于光线的核，并采用优化的稀疏核来有效地收集输入光线，并使用我们的分层DoF体绘制渲染优化的光线。我们为我们的任务合成了一个具有散焦动态场景的数据集，对我们的数据集进行的广泛实验表明，我们的方法在从散焦模糊合成所有聚焦新视图方面优于现有方法，同时保持场景中的时空一致性。 et.al.|[2407.05586](http://arxiv.org/abs/2407.05586)|null|
|**2024-07-07**|**GaussReg: Fast 3D Registration with Gaussian Splatting**|点云配准是大规模三维场景扫描和重建的一个基本问题。在深度学习的帮助下，注册方法已经有了显著的发展，达到了近乎成熟的阶段。随着神经辐射场（NeRF）的引入，它以其强大的视图合成能力成为最受欢迎的3D场景表示。关于NeRF表示，大规模场景重建也需要对其进行注册。然而，这个话题却极度缺乏探索。这是由于用隐式表示对两个场景之间的几何关系进行建模的固有挑战。现有的方法通常将隐式表示转换为显式表示，以便进一步注册。最近，引入了高斯散斑（GS），采用显式3D高斯。这种方法显著提高了渲染速度，同时保持了高渲染质量。给定两个具有显式GS表示的场景，在这项工作中，我们探索了它们之间的3D配准任务。为此，我们提出了GaussReg，这是一种新颖的从粗到细的框架，既快速又准确。粗略阶段遵循现有的点云配准方法，并从GS中估计点云的粗略对齐。我们进一步提出了一种图像引导的精细配准方法，该方法渲染GS中的图像，为精确对齐提供更详细的几何信息。为了支持全面评估，我们仔细构建了一个名为ScanNet GSReg的场景级数据集，其中包含从ScanNet数据集中获得的1379个场景，并收集了一个称为GSReg。实验结果表明，我们的方法在多个数据集上实现了最先进的性能。我们的GaussReg比HLoc（SuperPoint作为特征提取器，SuperGlue作为匹配器）快44倍，精度相当。 et.al.|[2407.05254](http://arxiv.org/abs/2407.05254)|null|

<p align=right>(<a href=#updated-on-20240713>back to top</a>)</p>

## 3D Reconstruction

|Publish Date|Title|Abstract|PDF|Code|
|---|---|---|---|---|
|**2024-07-10**|**Chat-Edit-3D: Interactive 3D Scene Editing via Text Prompts**|最近基于视觉语言预训练模型的图像内容操纵工作已有效地扩展到文本驱动的3D场景编辑。然而，现有的3D场景编辑方案仍然存在某些缺点，阻碍了它们的进一步交互设计。这种方案通常遵循固定的输入模式，限制了用户在文本输入方面的灵活性。此外，它们的编辑能力受到单个或几个2D视觉模型的限制，需要复杂的管道设计将这些模型集成到3D重建过程中。为了解决上述问题，我们提出了一种基于对话的3D场景编辑方法，称为CE3D，它以一个大型语言模型为中心，允许用户任意输入文本并解释他们的意图，从而促进相应视觉专家模型的自主调用。此外，我们设计了一种利用哈希图集来表示3D场景视图的方案，该方案将3D场景的编辑转移到2D图集图像上。该设计实现了2D编辑和3D重建过程之间的完全解耦，使CE3D能够灵活地集成各种现有的2D或3D视觉模型，而不需要复杂的融合设计。实验结果表明，CE3D有效地整合了多种视觉模型，实现了多样化的编辑视觉效果，具有很强的场景理解能力和多轮对话能力。该代码可在以下网址获得https://sk-fun.fun/CE3D. et.al.|[2407.06842](http://arxiv.org/abs/2407.06842)|null|
|**2024-07-09**|**Computer vision tasks for intelligent aerospace missions: An overview**|计算机视觉任务对于航空航天任务至关重要，因为它们帮助航天器理解和解释空间环境，例如估计位置和方向、重建3D模型和识别物体，这些任务已被广泛研究以成功执行任务。然而，卡尔曼滤波、运动结构和多视图立体等传统方法不足以处理恶劣条件，导致结果不可靠。近年来，基于深度学习（DL）的感知技术显示出巨大的潜力，并优于传统方法，特别是在对不断变化的环境的鲁棒性方面。为了进一步推进基于DL的航空航天感知，已经提出了各种框架、数据集和策略，表明未来应用的巨大潜力。在这项调查中，我们旨在探索感知任务中使用的有前景的技术，并强调基于DL的航空航天感知的重要性。我们首先概述了航空航天感知，包括近年来开发的经典空间项目、常用传感器和传统感知方法。随后，我们深入研究了航空航天任务中的三个基本感知任务：姿态估计、3D重建和识别，因为它们对后续的决策和控制至关重要。最后，我们讨论了当前研究的局限性和可能性，并对未来的发展进行了展望，包括使用有限数据集的挑战、改进算法的必要性以及多源信息融合的潜在好处。 et.al.|[2407.06513](http://arxiv.org/abs/2407.06513)|null|
|**2024-07-09**|**LuSNAR:A Lunar Segmentation, Navigation and Reconstruction Dataset based on Muti-sensor for Autonomous Exploration**|随着月球探测任务的复杂性，月球需要更高的自主性。环境感知和导航算法是月球车实现自主探索的基础。算法的开发和验证需要高度可靠的数据支持。现有的月球数据集大多针对单一任务，缺乏多样化的场景和高精度的地面实况标签。为了解决这个问题，我们提出了一个多任务、多场景和多标签的月球基准数据集LuSNAR。该数据集可用于全面评估自主感知和导航系统，包括高分辨率立体图像对、全景语义标签、密集深度图、激光雷达点云和漫游车的位置。为了提供更丰富的场景数据，我们基于虚幻引擎构建了9个月球模拟场景。每个场景根据地形起伏和物体密度进行划分。为了验证数据集的可用性，我们评估和分析了语义分割、3D重建和自主导航的算法。实验结果证明，本文提出的数据集可用于自主环境感知和导航等任务的地面验证，并为测试算法度量的可访问性提供了月球基准数据集。我们在以下网址公开提供LuSNAR：https://github.com/autumn999999/LuSNAR-dataset. et.al.|[2407.06512](http://arxiv.org/abs/2407.06512)|**[link](https://github.com/autumn999999/lusnar-dataset)**|
|**2024-07-08**|**Tailor3D: Customized 3D Assets Editing and Generation with Dual-Side Images**|3D AIGC的最新进展表明，它有望直接从文本和图像创建3D对象，从而在动画和产品设计方面节省大量成本。然而，3D资源的详细编辑和定制仍然是一个长期存在的挑战。具体来说，3D生成方法缺乏像2D图像创建方法那样精确地遵循精细详细指令的能力。想象一下，你可以通过3D AIGC获得一个玩具，但带有不需要的配件和服装。为了应对这一挑战，我们提出了一种名为Tailor3D的新型管道，它可以从可编辑的双面图像中快速创建定制的3D资产。我们的目标是模仿裁缝在局部更改对象或执行整体风格转换的能力。与从多个视图创建3D资源不同，使用双面图像消除了编辑单个视图时发生的重叠区域冲突。具体来说，它首先编辑前视图，然后通过多视图扩散生成对象的后视图。之后，它继续编辑后视图。最后，提出了一种双面LRM，将正面和背面的3D特征无缝缝合在一起，类似于裁缝将衣服的正面和背面缝合在一起。双面LRM纠正了前后视图之间不完美的一致性，增强了编辑能力，减轻了内存负担，同时将它们与LoRA Triple Plane Transformer无缝集成到统一的3D表示中。实验结果证明了Tailor3D在各种3D生成和编辑任务中的有效性，包括3D生成填充和样式转换。它为编辑3D资源提供了一种用户友好、高效的解决方案，每个编辑步骤只需几秒钟即可完成。 et.al.|[2407.06191](http://arxiv.org/abs/2407.06191)|null|
|**2024-07-06**|**Incremental Multiview Point Cloud Registration**|本文提出了一种新的多视点云配准方法。与之前通常采用全局方案进行多视图配准的研究不同，我们建议采用增量流水线将扫描逐步对齐到规范坐标系中。具体来说，从基于图像的3D重建中汲取灵感，我们的方法首先通过扫描检索和几何验证构建稀疏扫描图。然后，我们通过初始化、下一次扫描选择和注册、轨道创建和继续以及捆绑调整来执行增量注册。此外，对于无检测器的匹配器，我们引入了Track细化过程。此过程主要构建粗略的多视图配准，并通过调整轨迹上关键点的位置来细化模型。实验证明，在三个基准数据集上，所提出的框架优于现有的多视图配准方法。该代码可在以下网址获得https://github.com/Choyaa/IncreMVR. et.al.|[2407.05021](http://arxiv.org/abs/2407.05021)|null|
|**2024-07-05**|**LaRa: Efficient Large-Baseline Radiance Fields**|辐射场方法实现了逼真的新颖视图合成和几何重建。但它们主要应用于每场景优化或小基线设置。虽然最近的几项工作利用变压器研究了具有大基线的前馈重建，但它们都使用标准的全局注意力机制进行操作，因此忽略了3D重建的局部性质。我们提出了一种在变压器层中统一局部和全局推理的方法，从而提高了质量并加快了收敛速度。我们的模型将场景表示为高斯体积，并将其与图像编码器和组注意力层相结合，以实现高效的前馈重建。实验结果表明，我们的模型在四个GPU上训练了两天，在重建360度辐射场时表现出了高保真度，并对零样本和域外测试表现出了鲁棒性。 et.al.|[2407.04699](http://arxiv.org/abs/2407.04699)|null|
|**2024-07-05**|**Rethinking Data Input for Point Cloud Upsampling**|近年来，点云上采样在三维重建和曲面生成等领域得到了广泛的应用。然而，现有的点云上采样输入都是基于补丁的，没有研究讨论点云模型全输入和基于补丁的输入之间的差异和原理。为了与基于补丁的点云输入进行比较，本文提出了一种新的数据输入方法，该方法在训练PU-GCN时对完整的点云模型进行划分以确保形状完整性。本文在PU1K和ABC数据集上进行了验证，但结果表明，基于补丁的性能优于基于模型的全输入，即平均分段输入。因此，本文探讨了影响点云上采样结果的数据输入因素和模型模块。 et.al.|[2407.04476](http://arxiv.org/abs/2407.04476)|null|
|**2024-07-10**|**GSD: View-Guided Gaussian Splatting Diffusion for 3D Reconstruction**|我们提出了GSD，这是一种基于高斯散斑（GS）表示的扩散模型方法，用于从单个视图重建3D对象。先前的作品因不正确的表示而遭受不一致的3D几何或平庸的渲染质量。我们通过利用最近最先进的3D显式表示、高斯散斑和无条件扩散模型，朝着解决这些缺点迈出了一步。该模型学习生成由GS椭球体集表示的3D对象。有了这些强大的生成性3D先验，尽管无条件学习，扩散模型已经准备好进行视图引导重建，而无需进一步的模型微调。这是通过高效而灵活的飞溅函数和引导去噪采样过程传播细粒度2D特征来实现的。此外，还采用2D扩散模型来提高渲染保真度，并通过抛光和重用渲染图像来提高重建的GS质量。最终重建的对象具有高质量的3D结构和纹理，可以在任意视图中高效渲染。在具有挑战性的真实世界CO3D数据集上的实验证明了我们方法的优越性。项目页面： $\href{https://yxmu.foo/GSD/}｛\text｛此https URL｝｝$ et.al.|[2407.04237](http://arxiv.org/abs/2407.04237)|null|
|**2024-07-04**|**SfM on-the-fly: Get better 3D from What You Capture**|在过去的二十年里，运动结构（SfM）一直是摄影测量、计算机视觉、机器人等领域的研究热点，而实时性能只是最近人们越来越感兴趣的话题。这项工作建立在原始的动态SfM（Zhan等人，2024）的基础上，并提出了一个更新版本，其中有三个新的进步，可以从您捕获的内容中获得更好的3D：（i）通过采用分层可导航小世界（HNSW）图，进一步提高了实时图像匹配，从而更快地识别出更真实的正重叠图像候选者；（ii）提出了一种自适应加权策略，用于鲁棒的分层局部束调整，以改善SfM结果；（iii）包括多个代理用于支持协作SfM，并在出现共同注册的图像时将多个3D重建无缝合并到一个完整的3D场景中。各种综合实验表明，所提出的SfM方法（称为即时SfMv2）可以以高效的方式生成更完整、更稳健的3D重建。代码可在以下网址获得http://yifeiyu225.github.io/on-the-flySfMv2.github.io/. et.al.|[2407.03939](http://arxiv.org/abs/2407.03939)|null|
|**2024-07-04**|**Beyond Viewpoint: Robust 3D Object Recognition under Arbitrary Views through Joint Multi-Part Representation**|现有的基于视图的方法擅长从预定义的视点识别3D对象，但它们在任意视图下的识别探索是有限的。这是一个具有挑战性和现实性的设置，因为每个对象都有不同的视点位置和数量，并且它们的姿势没有对齐。然而，大多数基于视图的方法，即聚合多个视图特征以获得全局特征表示，很难解决任意视图下的3D对象识别问题。由于来自任意视图的未对齐输入，很难稳健地聚合特征，从而导致性能下降。本文介绍了一种新的基于零件表示的零件感知网络（PANet）来解决这些问题。这种基于零件的表示旨在定位和理解3D对象的不同部分，如飞机机翼和尾翼。它具有视点不变性和旋转鲁棒性等特性，这使其在解决任意视图下的3D对象识别问题方面具有优势。我们在基准数据集上的结果清楚地表明，我们提出的方法在任意视图下的3D对象识别任务中优于现有的基于视图的聚合基线，甚至超过了大多数固定视点方法。 et.al.|[2407.03842](http://arxiv.org/abs/2407.03842)|null|

<p align=right>(<a href=#updated-on-20240713>back to top</a>)</p>

## Diffusion

|Publish Date|Title|Abstract|PDF|Code|
|---|---|---|---|---|
|**2024-07-10**|**Generative Image as Action Models**|图像生成扩散模型已经过微调，以解锁图像编辑和新颖的视图合成等新功能。我们能否同样解锁用于视觉运动控制的图像生成模型？我们介绍了GENIMA，这是一种行为克隆代理，可以微调稳定扩散，在RGB图像上“绘制联合动作”作为目标。这些图像被输入控制器，该控制器将视觉目标映射到一系列关节位置。我们在25个RLBench和9个真实操作任务上研究了GENIMA。我们发现，通过将动作提升到图像空间，互联网预训练的扩散模型可以生成优于最先进的视觉运动方法的策略，特别是在对场景扰动的鲁棒性和对新对象的泛化方面。我们的方法也与3D代理竞争，尽管缺乏深度、关键点或运动规划等先验知识。 et.al.|[2407.07875](http://arxiv.org/abs/2407.07875)|null|
|**2024-07-10**|**Dynamical Measure Transport and Neural PDE Solvers for Sampling**|从概率密度中采样的任务可以看作是将可处理的密度函数传输到目标，称为动态测量传输。在这项工作中，我们使用偏微分方程（PDE）描述的确定性或随机演化，通过一个有原则的统一框架来解决这个问题。该框架结合了先前的基于轨迹的采样方法，如扩散模型或薛定谔桥，而不依赖于时间反转的概念。此外，它允许我们提出新的数值方法来解决传输任务，从而从复杂的目标中采样，而不需要归一化常数或数据样本。我们使用物理信息神经网络（PINN）来近似相应的PDE解，这意味着概念和计算上的优势。特别是，PINN允许无模拟和离散化的优化，并且可以非常有效地训练，与替代方法相比，可以在采样任务中显著提高模式覆盖率。此外，它们可以很容易地用高斯-牛顿方法进行微调，以实现采样的高精度。 et.al.|[2407.07873](http://arxiv.org/abs/2407.07873)|null|
|**2024-07-10**|**Controlling Space and Time with Diffusion Models**|我们提出了4DiM，这是一种用于4D新颖视图合成（NVS）的级联扩散模型，以一般场景的一个或多个图像以及一组相机姿态和时间戳为条件。为了克服由于4D训练数据可用性有限而带来的挑战，我们提倡对3D（有相机姿势）、4D（姿势+时间）和视频（时间但没有姿势）数据进行联合训练，并提出了一种新的架构来实现这一点。我们进一步主张使用单目度量深度估计器对SfM姿态数据进行校准，以实现度量尺度相机控制。对于模型评估，我们引入了新的度量来丰富和克服当前评估方案的缺点，与现有的3D NVS扩散模型相比，在保真度和姿态控制方面展示了最先进的结果，同时增加了处理时间动态的能力。4DiM还用于改进全景拼接、姿势调节的视频到视频翻译以及其他一些任务。有关概述，请参阅https://4d-diffusion.github.io et.al.|[2407.07860](http://arxiv.org/abs/2407.07860)|null|
|**2024-07-10**|**Generic Numerical Analysis of Stochastic Reaction Diffusion Model with applications in excitable media**|研究了乘性噪声驱动的随机反应扩散模型。我们构建了梯度离散化方法（GDM），这是一个结合了几个数值方法族的抽象框架。本文提供了离散化，并使用在数据自然假设下工作的紧致性论证证明了近似方案的收敛性。我们还使用有限体积法，即混合混合模拟（HMM）方法，研究了乘性噪声对模型显示的可激发介质中行波动力学的影响。特别是，我们考虑了足够高的噪声如何导致波回火或无法传播。 et.al.|[2407.07834](http://arxiv.org/abs/2407.07834)|null|
|**2024-07-10**|**Dynamical signatures of discontinuous phase transitions: How phase coexistence determines exponential versus power-law scaling**|文献中关于Liouvillian间隙的有限尺寸标度和不连续相变的动力学波动存在相互矛盾的报道，各种研究报告了指数或幂律行为。我们采用大偏差理论来澄清这个问题。我们区分了两类具有不同动力学性质的不连续相变。第一类与相位共存有关，即在相变点周围的有限相图区域中存在系统动力学的多个稳定吸引子（例如自由能泛函的局部最小值）。在这种情况下，人们观察到与吸引子之间的随机切换相关的渐近指数标度（尽管指数标度的开始有时可能发生在非常大的系统规模上）。在第二类中，远离相变点没有相位共存，而在相变点本身有无限多个吸引子。在这种情况下，人们观察到与系统弛豫到稳态的扩散性质相关的幂律标度。 et.al.|[2407.07832](http://arxiv.org/abs/2407.07832)|null|
|**2024-07-10**|**Universal and non-universal signatures in the scaling functions of critical variables**|关键统计变量的概率密度函数（PDF）按大小或时间异常缩放，可以提供普遍行为的标志，这与这种密度明显依赖于非普遍特征的情况形成鲜明对比。我们通过证明大偏差函数中领先临界奇点的非普适振幅和普适指数都由PDF尾部决定来解决这一明显矛盾，PDF尾部的形式在可拓性上有所争论。这一未探索的场景暗示了临界时中心极限定理的普遍形式，并通过平衡中的平均场伊辛模型和异常扩散模型的精确计算得到了证实。 et.al.|[2407.07782](http://arxiv.org/abs/2407.07782)|null|
|**2024-07-10**|**Correlation of srf performance to oxygen diffusion length of medium temperature heat treated cavities**|这项综合研究是欧洲XFEL研发工作的一部分，阐明了250℃至350℃之间的中温（mid-T）热处理对1.3~GHz超导射频（SRF）铌腔性能的影响。利用DESY配备有内部真空室和低温泵的翻新铌蒸馏炉，我们开始了一项研究，以加强最先进的SRF腔技术。我们的研究表明，中T热处理显著提高了腔体的品质因数（ $Q_0$），在场强约为16~MV/m时，达到了2\cdot10^{10}$至5\cdot1^{10}$ 之间的值，而最大场强限制在25-35~MV/m，并且观察到对捕获磁通量的敏感性增强。此外，我们深入研究了表面杂质浓度变化的影响，特别是氧含量的扩散及其对性能增强的影响。通过使用整个温度分布基于计算的扩散长度对处理进行分类，我们识别出了有助于优化腔体性能的最佳扩散长度的模式。在大多数情况下，样品的SIMS结果证实了计算出的氧扩散长度。偏差主要归因于细晶粒材料中的晶界，需要对单晶材料进行重复测量以进一步研究这一现象。对冷却速率和由此产生的整个腔体的空间温度梯度（范围为0.04至0.2K/mm）的研究表明，在中T热处理后，与性能没有显著相关性。然而，由于对磁卫生的要求越来越严格，对捕获磁通量的敏感性增加给寻求下一代加速器技术带来了新的挑战。 et.al.|[2407.07779](http://arxiv.org/abs/2407.07779)|null|
|**2024-07-10**|**Challenges in modeling the dark matter halo of NGC 1052-DF2: Cored versus cuspy halo models**|NGC 1052-DF2的发现和随后的建模表明，NGC 1052-DF2缺乏暗物质，与标准的恒星与晕质量比相冲突。在这项工作中，我们的目标是解决NGC 1052-DF2质量估计的动力学模型之间的退化问题。我们使用具有径向变化各向异性参数的各向异性分布函数构建了NGC 1052-DF2的质量模型，并研究了各种模型参数对暗物质估计的影响。我们使用观测到的恒星光度作为输入参数来构建分布函数，并采用马尔可夫链蒙特卡罗（MCMC）方法来估计暗物质模型参数。我们发现，具有尖峰暗物质晕的质量模型与具有零暗物质的模型具有可比性。此外，松软的暗物质晕无法始终如一地解释星系内外区域观测到的速度色散。因此，我们排除了描述NGC 1052-DF2质量模型时出现尖峰暗物质晕的可能性。我们的研究表明，总质量为 $\log（M_{DM}/M_{\odot}）=10.5$ 的核心暗物质晕模型解释了观测到的运动学，但需要非常大的尺度长度（20kpc）和外截止半径（26kpc）。虽然核心质量模型提供了相对更好的拟合，但我们的研究结果强调，质量模型在很大程度上不受可用运动学数据的约束。我们的结果表明，NGC 1052-DF2不仅可能具有超漫射恒星分布，而且在现有运动学数据的不确定性范围内，它可能拥有与星系形成和演化模型预测的标准恒星与晕质量关系（SHMR）兼容的超漫射暗物质分布 et.al.|[2407.07770](http://arxiv.org/abs/2407.07770)|null|
|**2024-07-10**|**Feasibility Study on Active Learning of Smart Surrogates for Scientific Simulations**|高性能科学模拟对于理解复杂系统非常重要，尤其是在探索广泛的参数空间时，会遇到计算挑战。人们对开发深度神经网络（DNN）作为能够加速模拟的替代模型越来越感兴趣。然而，现有的训练这些DNN替代物的方法依赖于大量的模拟数据，这些数据是通过启发式选择和昂贵的计算生成的，这是文献中未充分探讨的挑战。本文探讨了将主动学习融入DNN替代训练的潜力。这允许对训练模拟进行智能和客观的选择，减少了生成大量模拟数据的需要，以及DNN代理的性能对预定义训练模拟的依赖性。在构建具有源的扩散方程的DNN替代物的问题背景下，我们研究了基于多样性和不确定性的策略在选择训练模拟方面的有效性，考虑了两种不同的DNN架构。这些结果为开发智能代理的高性能计算基础设施奠定了基础，该基础设施支持由主动学习策略引导的动态生成模拟数据，从而有可能提高科学模拟的效率。 et.al.|[2407.07674](http://arxiv.org/abs/2407.07674)|null|
|**2024-07-10**|**VEnhancer: Generative Space-Time Enhancement for Video Generation**|我们提出了一种生成式时空增强框架VEnhancer，它通过在空间域中添加更多细节和在时间域中添加合成细节运动来改进现有的文本到视频结果。给定生成的低质量视频，我们的方法可以通过统一的视频扩散模型，在任意上采样空间和时间尺度下同时提高其空间和时间分辨率。此外，VEnhancer有效地消除了生成的视频的空间伪影和时间闪烁。为了实现这一点，基于预训练的视频扩散模型，我们训练了一个视频ControlNet，并将其作为低帧率和低分辨率视频的条件注入扩散模型。为了有效地训练这个视频控制网，我们设计了时空数据增强和视频感知调节。受益于上述设计，VEnhancer在训练过程中保持稳定，并采用优雅的端到端训练方式。大量实验表明，VEnhancer在增强人工智能生成的视频方面超越了现有的最先进的视频超分辨率和时空超分辨率方法。此外，借助VEnhancer，现有的开源最先进的文本到视频方法VideoCrafter-2在视频生成基准测试中达到了最高水平——VBench。 et.al.|[2407.07667](http://arxiv.org/abs/2407.07667)|null|

<p align=right>(<a href=#updated-on-20240713>back to top</a>)</p>

## NeRF

|Publish Date|Title|Abstract|PDF|Code|
|---|---|---|---|---|
|**2024-07-10**|**Neural Localizer Fields for Continuous 3D Human Pose and Shape Estimation**|随着可用训练数据的爆炸性增长，单图像3D人体建模领先于向以数据为中心的范式过渡。成功利用数据规模的关键是设计灵活的模型，这些模型可以从不同研究人员或供应商生产的各种异构数据源进行监督。为此，我们提出了一种简单而强大的范式，用于无缝统一不同的人体姿势和形状相关的任务和数据集。我们的公式侧重于在训练和测试时查询人体体积的任意点并在3D中获得其估计位置的能力。我们通过学习身体点定位器函数的连续神经场来实现这一点，每个函数都是基于不同参数化的3D热图卷积点定位器（检测器）。为了生成参数输出，我们提出了一种高效的后处理步骤，用于将SMPL族身体模型拟合到非参数关节和顶点预测中。通过这种方法，我们可以自然地利用不同注释的数据源，包括网格、2D/3D骨架和密集姿势，而无需在它们之间进行转换，从而训练出大规模的3D人体网格和骨架估计模型，这些模型在3DPW、EMDB和SSP-3D等几个公共基准上的表现远远优于最先进的水平。 et.al.|[2407.07532](http://arxiv.org/abs/2407.07532)|null|
|**2024-07-03**|**Cerebral cortex inspired representation of neural field network**|进化及其智能元素在探索中带来了刺激和挑战。然而，物种如何拥有记忆、检索记忆并保持连续性是根本问题。大多数现象只能由研究人员假设，通过实验验证它们是一个很大的挑战。将大脑视为理想的智能机器并对其进行建模，为计算算法开辟了新的维度。本文提出了一个假设，即类似于大脑皮层的记忆创造。大脑皮层的区域隐含着特定功能的特异性，构成了一维的矢量形式的神经场。整个皮层的神经场相互连接形成了一个网络。这些网络与生存本能、情绪和奖励相关联，构成了对暴露环境的记忆，或者说学习。具有多维控制点的图形工具NURBS被隐式地用于将这些网络表示为一组三次方程。通过数据学习是智能系统的主要模块，本文试图将数据转换为低维模式，而不是实时智能系统的现有绝对形式。 et.al.|[2407.04741](http://arxiv.org/abs/2407.04741)|null|
|**2024-07-01**|**Fast and Efficient: Mask Neural Fields for 3D Scene Segmentation**|理解3D场景是计算机视觉研究中的一个关键挑战，其应用跨越多个领域。最近在将2D视觉语言基础模型提取到神经领域（如NeRF和3DGS）方面取得的进展，使3D场景能够从2D多视图图像中进行开放式词汇分割，而不需要精确的3D注释。然而，虽然有效，但高维CLIP特征的每像素蒸馏会引入模糊性，并需要复杂的正则化策略，从而在训练过程中增加效率。本文介绍了MaskField，它能够在弱监督下利用神经场实现快速高效的3D开放式分词。与以前的方法不同，MaskField提取掩模而不是密集的高维CLIP特征。MaskFields使用神经场作为二进制掩模生成器，并使用SAM生成的掩模对其进行监督，并通过粗略的CLIP特征进行分类。MaskField通过在训练过程中自然引入SAM分割的对象形状而无需额外的正则化来克服模糊的对象边界。通过在训练过程中避免直接处理高维CLIP特征，MaskField与3DGS等显式场景表示特别兼容。我们广泛的实验表明，MaskField不仅超越了现有的最先进的方法，而且实现了非常快的收敛速度，仅需5分钟的训练就超越了以前的方法。我们希望MaskField能够激发对如何训练神经场以从2D模型中理解3D场景的进一步探索。 et.al.|[2407.01220](http://arxiv.org/abs/2407.01220)|null|
|**2024-07-01**|**3D Feature Distillation with Object-Centric Priors**|将自然语言与物理世界联系起来是一个无处不在的话题，在计算机视觉和机器人技术中有着广泛的应用。最近，CLIP等二维视觉语言模型因其在二维图像中具有令人印象深刻的开放词汇基础能力而得到了广泛推广。最近的工作旨在通过特征提取将2D CLIP特征提升到3D，但要么学习特定于场景的神经场，因此缺乏泛化能力，要么专注于需要访问多个摄像头视图的室内房间扫描数据，这在机器人操作场景中是不可行的。此外，相关方法通常在像素级融合特征，并假设所有相机视图都具有相同的信息量。在这项工作中，我们表明这种方法在接地精度和分割清晰度方面都会导致次优的3D特征。为了缓解这一问题，我们提出了一种多视图特征融合策略，该策略采用以对象为中心的先验来消除基于语义信息的无信息视图，并通过实例分割掩码在对象级别融合特征。为了提取我们以对象为中心的3D特征，我们生成了一个大规模的合成多视图数据集，其中包含杂乱的桌面场景，从3300多个独特的对象实例中生成了15k个场景，我们将其公之于众。我们表明，我们的方法在从单视图RGB-D重建3D CLIP特征的同时，提高了接地容量和空间一致性，从而偏离了测试时多个相机视图的假设。最后，我们证明了我们的方法可以推广到新的桌面领域，并可以在不进行微调的情况下重新用于3D实例分割，并证明了它在混乱中的语言引导机器人抓取中的实用性 et.al.|[2406.18742](http://arxiv.org/abs/2406.18742)|null|
|**2024-06-25**|**Masked Generative Extractor for Synergistic Representation and 3D Generation of Point Clouds**|在二维图像生成建模和表示学习领域，掩模生成编码器（MAGE）已经证明了生成建模与表示学习之间的协同潜力。受此启发，我们提出Point MAGE将这一概念扩展到点云数据。具体来说，该框架首先利用矢量量化变分自编码器（VQVAE）重建3D形状的神经场表示，从而学习点补丁的离散语义特征。随后，通过将掩蔽模型与可变掩蔽比相结合，我们实现了生成和表示学习的同步训练。此外，我们的框架与现有的点云自监督学习（SSL）模型无缝集成，从而提高了它们的性能。我们广泛评估了Point MAGE的表示学习和生成能力。在形状分类任务中，Point MAGE在ModelNet40数据集上的准确率达到94.2%，在ScanObjectNN数据集上达到92.9%（+1.3%）。此外，它在少数镜头学习和零件分割任务中取得了最新的性能。实验结果还证实，Point MAGE可以在无条件和有条件的设置下生成详细和高质量的3D形状。 et.al.|[2406.17342](http://arxiv.org/abs/2406.17342)|null|
|**2024-06-17**|**DistillNeRF: Perceiving 3D Scenes from Single-Glance Images by Distilling Neural Fields and Foundation Model Features**|我们提出了DistillNeRF，这是一个自监督学习框架，解决了在自动驾驶中从有限的2D观察中理解3D环境的挑战。我们的方法是一种可推广的前馈模型，它从稀疏的单帧多视图相机输入中预测丰富的神经场景表示，并通过可微渲染进行自我监督训练，以重建RGB、深度或特征图像。我们的第一个见解是通过生成密集的深度和虚拟相机目标进行训练，利用每场景优化的神经辐射场（NeRF），从而帮助我们的模型从稀疏的非重叠图像输入中学习3D几何。其次，为了学习语义丰富的3D表示，我们建议从预先训练的2D基础模型（如CLIP或DINOv2）中提取特征，从而实现各种下游任务，而不需要昂贵的3D人工注释。为了利用这两个见解，我们引入了一种新的模型架构，该架构具有两级提升-飞溅-射击编码器和参数化的稀疏分层体素表示。NuScenes数据集的实验结果表明，DistillNeRF在场景重建、新颖视图合成和深度估计方面明显优于现有的可比自监督方法；并且它允许竞争性的零样本3D语义占用预测，以及通过提取的基础模型特征来理解开放世界场景。演示和代码将在https://distillnerf.github.io/. et.al.|[2406.12095](http://arxiv.org/abs/2406.12095)|null|
|**2024-06-18**|**Effective Rank Analysis and Regularization for Enhanced 3D Gaussian Splatting**|从多视图图像进行3D重建是计算机视觉和图形学中的基本挑战之一。最近，3D高斯散斑（3DGS）已经成为一种有前景的技术，能够实时渲染高质量的3D重建。该方法利用3D高斯表示和基于图块的飞溅技术，绕过了昂贵的神经场查询。尽管3DGS具有潜力，但由于高斯收敛为具有一个主要方差的各向异性高斯，它遇到了挑战，包括针状伪影、次优几何形状和不准确的法线。我们建议使用有效秩分析来检查3D高斯基元的形状统计，并识别高斯真的收敛到有效秩为1的针状形状。为了解决这个问题，我们引入了有效秩作为正则化，它约束了高斯的结构。我们的新正则化方法增强了法线和几何重建，同时减少了针状伪影。该方法可以作为附加模块集成到其他3DGS变体中，在不损害视觉保真度的情况下提高其质量。 et.al.|[2406.11672](http://arxiv.org/abs/2406.11672)|null|
|**2024-06-13**|**Well-posedness and regularity of solutions to neural field problems with dendritic processing**|我们研究了最近提出的神经场模型的解决方案，其中树突被建模为源自体细胞层的垂直纤维连续体。由于电压通过具有非局域源的电缆方程沿树突方向传播，该模型具有各向异性扩散算子和突触耦合的积分项。因此，相应的柯西问题与经典神经场方程明显不同。我们证明了该问题的弱公式具有唯一解，其嵌入估计类似于非线性局部反应扩散方程的嵌入估计。我们的分析依赖于扰动无扩散问题的弱解，即一个标准的神经场，迄今为止还没有研究过弱问题。我们找到了有和没有扩散问题的严格渐近估计，并证明了这两个模型的解在有限时间间隔内以适当的范数保持接近。我们提供了微扰结果的数值证据。 et.al.|[2406.09222](http://arxiv.org/abs/2406.09222)|null|
|**2024-06-13**|**Preserving Identity with Variational Score for General-purpose 3D Editing**|我们提出了Piva（用变分分数蒸馏保持身份），这是一种基于优化的新方法，用于编辑基于扩散模型的图像和3D模型。具体来说，我们的方法受到了最近提出的二维图像编辑方法——增量去噪分数（DDS）的启发。我们指出了DDS在2D和3D编辑中的局限性，这会导致细节损失和过饱和。为了解决这个问题，我们提出了一个额外的分数蒸馏术语来强制身份保留。这使得编辑过程更加稳定，逐步优化NeRF模型以匹配目标提示，同时保留关键的输入特性。我们证明了我们的方法在零样本图像和神经场编辑中的有效性。我们的方法成功地改变了视觉属性，添加了微妙和实质性的结构元素，转换了形状，并在标准的2D和3D编辑基准上取得了有竞争力的结果。此外，我们的方法没有施加掩蔽或预训练等约束，使其与各种预训练的扩散模型兼容。这允许进行多功能编辑，而不需要神经场到网格的转换，从而提供更用户友好的体验。 et.al.|[2406.08953](http://arxiv.org/abs/2406.08953)|null|
|**2024-06-12**|**Category-level Neural Field for Reconstruction of Partially Observed Objects in Indoor Environment**|神经隐式表示通过各种成功案例在3D重建中引起了人们的关注。对于场景理解或编辑等进一步的应用，一些作品已经显示出在对象组成重建方面的进展。尽管它们在观测区域表现出色，但在重建部分观测到的物体方面，它们的性能仍然有限。为了更好地处理这个问题，我们引入了类别级神经场，在场景中属于同一类别的对象之间学习有意义的共同3D信息。我们的核心思想是根据观察到的形状对对象进行子分类，以便更好地训练类别级模型。然后，我们利用神经场进行具有挑战性的任务，通过选择和对齐基于射线的不确定性选择的代表性对象来注册部分观察到的对象。在模拟和真实世界数据集上的实验表明，我们的方法改善了几个类别中未观察到的部分的重建。 et.al.|[2406.08176](http://arxiv.org/abs/2406.08176)|**[link](https://github.com/Taekbum/category-nerf-reconstruction-official)**|

<p align=right>(<a href=#updated-on-20240713>back to top</a>)</p>

[contributors-shield]: https://img.shields.io/github/contributors/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[contributors-url]: https://github.com/Vincentqyw/cv-arxiv-daily/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[forks-url]: https://github.com/Vincentqyw/cv-arxiv-daily/network/members
[stars-shield]: https://img.shields.io/github/stars/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[stars-url]: https://github.com/Vincentqyw/cv-arxiv-daily/stargazers
[issues-shield]: https://img.shields.io/github/issues/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[issues-url]: https://github.com/Vincentqyw/cv-arxiv-daily/issues

