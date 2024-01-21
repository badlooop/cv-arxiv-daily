[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]

## Updated on 2024.01.21
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
|**2024-01-18**|**Explaining the Implicit Neural Canvas: Connecting Pixels to Neurons by Tracing their Contributions**|隐式神经表示（INRs）的许多变体，其中神经网络被训练为信号的连续表示，对于下游任务具有巨大的实用性，包括新颖的视图合成、视频压缩和图像超分辨率。不幸的是，对这些网络的内部运作方式的研究严重不足。我们的工作，即解释隐式神经画布（XINC），是一个统一的框架，用于通过检查每个神经元对每个输出像素的贡献强度来解释INRs的特性。我们将这些贡献图的集合称为隐式神经画布，并使用这一概念来证明我们研究的INR学会了以令人惊讶的方式“观察”它们所代表的帧。例如，INR往往具有高度分布的表示。虽然缺乏高级对象语义，但它们对颜色和边缘有很大的偏见，而且几乎完全是空间不可知的。我们通过研究视频INR中对象在时间上的表现方式得出了我们的结论，使用聚类来可视化跨层和架构的相似神经元，并表明这是由运动主导的。这些见解证明了我们的分析框架的普遍有用性。我们的项目页面位于https://namithap10.github.io/xinc. et.al.|[2401.10217](http://arxiv.org/abs/2401.10217)|null|
|**2024-01-18**|**GPAvatar: Generalizable and Precise Head Avatar from Image(s)**|头部化身重建对于虚拟现实、在线会议、游戏和电影行业的应用至关重要，在计算机视觉界引起了极大的关注。该领域的基本目标是忠实地再现头部化身，并精确地控制表情和姿势。现有的方法分为基于2D的扭曲、基于网格和神经渲染方法，在保持多视图一致性、结合非面部信息和推广到新身份方面存在挑战。在本文中，我们提出了一个名为GPAvatar的框架，该框架可以在单个前向通道中从一个或多个图像重建3D头部化身。这项工作的关键思想是引入一个由点云驱动的动态基于点的表情场，以精确有效地捕捉表情。此外，我们在三平面规范场中使用多三平面注意力（MTA）融合模块来利用来自多个输入图像的信息。所提出的方法实现了忠实的身份重建、精确的表达控制和多视图一致性，在自由视点渲染和新颖视图合成方面显示了良好的效果。 et.al.|[2401.10215](http://arxiv.org/abs/2401.10215)|null|
|**2024-01-17**|**Objects With Lighting: A Real-World Dataset for Evaluating Reconstruction and Rendering for Object Relighting**|从照片中重建对象并将其虚拟地放置在新环境中超出了标准的新颖视图合成任务，因为对象的外观不仅要适应新颖的视点，还要适应新的照明条件，而且反向渲染方法的评估依赖于新颖的视图合成数据或用于定量分析的简单合成数据集。这项工作提供了一个真实世界的数据集，用于测量重新照明对象的重建和渲染。为此，我们捕获了多个环境中相同对象的环境照明和地面实况图像，从而可以从一个环境中拍摄的图像中重建对象，并量化看不见的照明环境的渲染视图的质量。此外，我们介绍了一个由现成方法组成的简单基线，并在重新照明任务中测试了几种最先进的方法，表明新的视图合成不是衡量性能的可靠指标。代码和数据集可在https://github.com/isl-org/objects-with-lighting. et.al.|[2401.09126](http://arxiv.org/abs/2401.09126)|**[link](https://github.com/isl-org/objects-with-lighting)**|
|**2024-01-17**|**ICON: Incremental CONfidence for Joint Pose and Radiance Field Optimization**|在给定一组2D图像的情况下，神经辐射场（NeRF）在新视图合成（NVS）中表现出显著的性能。然而，NeRF训练需要每个输入视图的精确相机姿势，通常通过运动结构（SfM）管道获得。最近的作品试图放松这种限制，但它们仍然经常依赖于可以改进的体面的初始姿势。在这里，我们旨在消除姿势初始化的要求。我们提出了增量置信（ICON），这是一种从2D视频帧中训练NeRF的优化过程。ICON仅假设相机运动平滑，以估计姿势的初始猜测。此外，ICON引入了“置信度”：一种用于动态重加权梯度的模型质量自适应度量。ICON依赖于高置信度姿势来学习NeRF，并依赖于高置信度3D结构（由NeRF编码）来学习姿势。我们表明，与使用SfM姿势的方法相比，ICON在没有预先初始化姿势的情况下，在CO3D和HO3D中都实现了卓越的性能。 et.al.|[2401.08937](http://arxiv.org/abs/2401.08937)|null|
|**2024-01-16**|**Fast Dynamic 3D Object Generation from a Single-view Video**|由于缺乏4D标记的数据，从单视图视频生成动态三维（3D）对象是具有挑战性的。现有方法通过传输现成的图像生成模型（如分数蒸馏采样）来扩展文本到3D管道，但由于需要通过大型预训练模型反向传播信息有限的监督信号，这些方法的扩展速度慢且成本高（例如，每个对象150分钟）。为了解决这一限制，我们提出了一种高效的视频到4D对象生成框架，称为Efficient4D。它在不同的相机视图下生成高质量的时空一致图像，然后将其用作标记数据，直接训练具有显式点云几何结构的新型4D高斯飞溅模型，实现在连续相机轨迹下的实时渲染。对合成视频和真实视频的广泛实验表明，与现有技术的替代方案相比，Efficient4D的速度显著提高了10倍，同时保持了相同水平的创新视图合成质量。例如，Efficient4D只需14分钟即可对动态对象进行建模。 et.al.|[2401.08742](http://arxiv.org/abs/2401.08742)|null|
|**2024-01-18**|**ProvNeRF: Modeling per Point Provenance in NeRFs as a Stochastic Process**|神经辐射场（NeRFs）在各种应用中越来越受欢迎。然而，它们在稀疏视图设置中面临挑战，缺乏来自体积渲染的足够约束。在具有多种应用的经典计算机视觉中，从稀疏和无约束的相机重建和理解3D场景是一个长期存在的问题。虽然最近的工作在稀疏、无约束的视图场景中探索了NeRF，但他们的重点主要是增强重建和新颖的视图合成。我们的方法从更广泛的角度出发，提出了一个问题：“从哪里看到了每个点？”——这决定了我们对它的理解和重建程度。换句话说，我们的目标是在稀疏、无约束的视图下确定每个3D点及其相关信息的起源或出处。我们介绍了ProvNeRF，这是一个模型，通过合并每个点的来源，为每个点的可能源位置建模，丰富了传统的NeRF表示。我们通过扩展随机过程的隐式最大似然估计（IMLE）来实现这一点。值得注意的是，我们的方法与任何预先训练的NeRF模型和相关的训练相机姿势兼容。我们证明，与最先进的方法相比，逐点源建模提供了几个优势，包括不确定性估计、基于标准的视图选择和改进的新视图合成。请访问我们的项目页面https://provnerf.github.io et.al.|[2401.08140](http://arxiv.org/abs/2401.08140)|null|
|**2024-01-11**|**TRIPS: Trilinear Point Splatting for Real-Time Radiance Field Rendering**|基于点的辐射场渲染在新颖的视图合成中表现出了令人印象深刻的结果，提供了令人信服的渲染质量和计算效率的结合。然而，这一领域的最新方法也并非没有缺点。3D高斯飞溅[Kerbl和Kopanas等人2023]在渲染高度详细的场景时，由于模糊和模糊的伪影，会遇到困难。另一方面ADOP[R\“uckert et al.2022]可以容纳更清晰的图像，但神经重建网络会降低性能，它会处理时间不稳定性，并且无法有效地解决点云中的大间隙。在本文中，我们提出了TRIPS（Trilinear point Splatting），一种结合了Gaussian Splatting和ADOP思想的方法。我们的新技术背后的基本概念包括将点光栅化为屏幕空间图像金字塔，金字塔层的选择由投影点的大小决定。这种方法允许使用单个三线性写入来渲染任意大的点。然后使用轻量级神经网络来重建包括超出飞溅分辨率的细节的无孔图像。重要的是，我们的渲染管道是完全可微分的，允许点大小和位置的自动优化。我们的评估表明，TRIPS在渲染质量方面超过了现有的最先进的方法，同时在现成的硬件上保持了每秒60帧的实时帧速率。这种性能扩展到具有挑战性的场景，例如具有复杂几何形状、广阔景观和自动曝光镜头的场景。 et.al.|[2401.06003](http://arxiv.org/abs/2401.06003)|null|
|**2024-01-10**|**Diffusion Priors for Dynamic View Synthesis from Monocular Videos**|动态新颖视图合成旨在捕捉视频中视觉内容的时间演变。现有的方法很难区分运动和结构，特别是在相机姿态与对象运动相比未知或受约束的情况下。此外，仅使用来自参考图像的信息，对在给定视频中被遮挡或部分观察到的看不见的区域产生幻觉是极具挑战性的。为了解决这些问题，我们首先使用定制技术在视频帧上微调预训练的RGB-D扩散模型。随后，我们将微调模型中的知识提取为包括动态和静态神经辐射场（NeRF）分量的4D表示。所提出的流水线在保持场景同一性的同时实现了几何一致性。我们进行了深入的实验，以定性和定量地评估所提出方法的有效性。我们的结果证明了我们的方法在具有挑战性的情况下的稳健性和实用性，进一步推进了动态新视图合成。 et.al.|[2401.05583](http://arxiv.org/abs/2401.05583)|null|
|**2024-01-09**|**Morphable Diffusion: 3D-Consistent Diffusion for Single-image Avatar Creation**|生成扩散模型的最新进展已经实现了从单个输入图像或文本提示生成3D资产的先前不可行的能力。在这项工作中，我们的目标是提高这些模型的质量和功能，以完成创建可控、照片真实感的人类化身的任务。我们通过将3D可变形模型集成到最先进的多视角一致扩散方法中来实现这一点。我们证明了生成管道在关节式3D模型上的精确调节增强了基线模型在从单个图像合成新视图任务中的性能。更重要的是，这种集成有助于将面部表情和身体姿势控制无缝准确地结合到生成过程中。据我们所知，我们提出的框架是第一个扩散模型，能够从看不见的物体的单个图像中创建完全3D一致、可动画化和照片真实感的人类化身；大量的定量和定性评估证明了我们的方法在新视角和新表情合成任务上优于现有的最先进的化身创建模型。 et.al.|[2401.04728](http://arxiv.org/abs/2401.04728)|null|
|**2024-01-07**|**See360: Novel Panoramic View Interpolation**|我们介绍了See360，它是一种使用潜在空间视点估计进行360全景插值的通用且高效的框架。大多数现有的视图渲染方法只关注室内或合成三维环境，并渲染小对象的新视图。相反，我们建议将以相机为中心的视图合成作为2D仿射变换来处理，而不使用点云或深度图，这使得能够实现有效的360？全景场景探索。给定一对参考图像，See360模型通过提出的新颖的多尺度仿射变换器（MSAT）来学习渲染新颖的视图，从而实现从粗到细的特征渲染。我们还提出了一种条件潜在空间自动编码器（C-LAE）来实现任意角度的视图插值。为了展示我们方法的多功能性，我们引入了四个训练数据集，即UrbanCity360、Archinterior360、HungHom360和Lab360，它们是从室内和室外环境中收集的，用于真实和合成渲染。实验结果表明，该方法具有足够的通用性，可以实现四个数据集任意视图的实时绘制。此外，我们的See360模型可以应用于野外的视图合成：只需很短的额外训练时间（约10分钟），并且能够渲染未知的真实世界场景。See360的卓越性能为以相机为中心的视图渲染和360全景视图插值开辟了一个很有前途的方向。 et.al.|[2401.03431](http://arxiv.org/abs/2401.03431)|**[link](https://github.com/Holmes-Alan/See360)**|

<p align=right>(<a href=#updated-on-20240121>back to top</a>)</p>

## 3D Reconstruction

|Publish Date|Title|Abstract|PDF|Code|
|---|---|---|---|---|
|**2024-01-17**|**POE: Acoustic Soft Robotic Proprioception for Omnidirectional End-effectors**|由于软机器人具有复杂的变形行为和无限的自由度，软机器人的形状估计和本体感觉具有挑战性。软机器人不断变形的身体使其难以集成刚性传感器并可靠地估计其形状。在这项工作中，我们提出了本体感知全向末端效应器（POE），它在肌腱驱动的软机器人表面上有六个嵌入式麦克风。我们首先介绍了先前提出的3D重建方法对来自麦克风的声学信号的新应用，用于软机器人形状本体感觉。为了提高本体感觉管道的训练效率和模型预测的一致性，我们提出了POE-M。POE-M首先利用嵌入式麦克风阵列从声学信号观测中预测关键点位置。然后，在给定估计的关键点的情况下，我们利用能量最小化方法来重建物理上可容许的高分辨率POE网格。我们用模拟数据评估了网格重建模块，并用真实世界的实验评估了完整的POE-M管道。我们证明，POE-M在网格重建过程中对关键点的明确指导为消融研究的管道提供了鲁棒性和稳定性。与最先进的端到端软机器人本体感觉模型相比，POE-M将最大倒角距离误差降低了23.10%，并在评估过程中实现了4.91mm的平均倒角距离误差。 et.al.|[2401.09382](http://arxiv.org/abs/2401.09382)|null|
|**2024-01-17**|**3D Scene Geometry Estimation from 360 $^\circ$ Imagery: A Survey**|本文对基于在全向光学系统下捕获的单个、两个或多个图像的先驱和最先进的3D场景几何估计方法进行了全面的综述。我们首先回顾了球面相机模型的基本概念，并回顾了适用于全向（也称为360$^\circ$ ，球面或全景）图像和视频的最常见的采集技术和表示格式。然后，我们调查了单目布局和深度推理方法，重点介绍了适用于球形数据的基于学习的解决方案的最新进展。然后在球面域上修改经典的立体匹配，其中检测和描述稀疏和密集特征的方法变得至关重要。然后，将立体匹配概念外推到多视图相机设置中，将其分类为光场、多视图立体和运动结构（或视觉同时定位和映射）。我们还汇编和讨论了常用的数据集和针对每种目的指出的优缺点，并列出了最新的结果以确保完整性。最后，我们指出了当前和未来的趋势。 et.al.|[2401.09252](http://arxiv.org/abs/2401.09252)|null|
|**2024-01-16**|**Learning Implicit Representation for Reconstructing Articulated Objects**|在没有关于物体结构的附加信息的情况下对运动的关节物体进行三维重建是一个具有挑战性的问题。当前的方法通过使用特定类别的骨架模型来克服这些挑战。因此，它们不能很好地推广到野外的铰接对象。我们将铰接物体视为未知的半刚性骨骼结构，由非刚性材料（如皮肤）包围。我们的方法在没有3D监督的情况下，根据对象视频中的运动线索，同时估计可见（显式）表示（3D形状、颜色、相机参数）和隐式骨架表示。我们的隐含表示由四个部分组成。（1） 骨架，用于指定半刚性零件的连接方式。（2） \textcolor｛black｝｛Skinning Weights｝，它将每个曲面顶点与半刚性零件概率关联起来。（3） 刚性系数，指定局部曲面的关节。（4） 时变变换，用于指定骨骼运动和曲面变形参数。我们介绍了一种使用物理约束作为正则化项并迭代估计隐式和显式表示的算法。我们的方法与类别无关，因此消除了对特定类别骨架的需求，我们表明我们的方法在标准视频数据集中优于最先进的方法。 et.al.|[2401.08809](http://arxiv.org/abs/2401.08809)|null|
|**2024-01-16**|**Real3D-Portrait: One-shot Realistic 3D Talking Portrait Synthesis**|一次拍摄3D会说话的肖像生成旨在从看不见的图像中重建3D化身，然后用参考视频或音频将其动画化，以生成会说话的人像视频。现有的方法无法同时实现准确的三维化身重建和稳定的人脸动画。此外，虽然现有的作品主要集中在合成头部，但生成自然的躯干和背景片段以获得逼真的说话肖像视频也是至关重要的。为了解决这些限制，我们提出了Real3D Potrait，该框架（1）通过从3D人脸生成模型中提取3D先验知识的大图像到平面模型提高了单次3D重建能力；（2） 利用高效的运动适配器促进精确的运动条件动画；（3） 使用头部-躯干背景超分辨率模型来合成具有自然躯干运动和可切换背景的逼真视频；以及（4）支持具有可推广的音频到运动模型的单镜头音频驱动的谈话面部生成。大量实验表明，与以前的方法相比，Real3D Portrait很好地概括了看不见的身份，并生成了更逼真的谈话肖像视频。 et.al.|[2401.08503](http://arxiv.org/abs/2401.08503)|null|
|**2024-01-16**|**S3M: Semantic Segmentation Sparse Mapping for UAVs with RGB-D Camera**|无人机在搜索和救援行动等关键应用中具有巨大潜力，在这些应用中，准确感知室内环境至关重要。然而，定位、3D重建和语义分割的同时融合是一个显著的障碍，尤其是在配备有限功率和计算资源的无人机的情况下。本文提出了一种新的方法来解决无人机作战中语义信息提取和利用方面的挑战。我们的系统集成了最先进的视觉SLAM来估计全面的6-DoF姿态，并在后端集成了先进的对象分割方法。为了提高框架的计算和存储效率，我们采用了一种简化的基于体素的三维地图表示——OctoMap来构建一个工作系统。此外，融合算法用于从前端SLAM任务中获得每个帧的语义信息和对应点。通过利用语义信息，我们的框架增强了无人机在室内空间感知和导航的能力，解决了姿态估计准确性和减少不确定性方面的挑战。通过Gazebo模拟，我们验证了我们提出的系统的有效性，并成功地将我们的方法嵌入到Jetson Xavier AGX单元中，用于真实世界的应用。 et.al.|[2401.08134](http://arxiv.org/abs/2401.08134)|null|
|**2024-01-12**|**3D Reconstruction of Interacting Multi-Person in Clothing from a Single Image**|本文介绍了一种新的管道，用于从单个图像在全局相干的场景空间上重建服装中多人交互的几何结构。主要的挑战来自遮挡：由于他人或自身的遮挡，人体的一部分在单个视图中是不可见的，这会导致几何结构缺失和物理上的不可置信性（例如穿透）。我们通过利用两个人类先验来完成3D几何和表面接触，克服了这一挑战。对于几何先验，编码器学习将身体部位缺失的人的图像回归到潜在向量；解码器对这些矢量进行解码以产生相关联的几何形状的3D特征；并且隐式网络将这些特征与表面法线图相结合以重建完整且详细的3D人。对于接触先验，我们开发了一种图像空间接触检测器，该检测器输出3D中人与人之间表面接触的概率分布。我们使用这些先验来全局细化身体姿势，从而能够在场景空间中无穿透、准确地重建穿着衣服的多人互动。结果表明，与现有方法相比，我们的方法是完整的、全局一致的，并且在物理上是合理的。 et.al.|[2401.06415](http://arxiv.org/abs/2401.06415)|null|
|**2024-01-12**|**SD-MVS: Segmentation-Driven Deformation Multi-View Stereo with Spherical Refinement and EM optimization**|在本文中，我们介绍了分割驱动变形多视图立体（SD-MVS），这是一种可以有效解决无纹理区域三维重建挑战的方法。我们是第一个采用Segment Anything Model（SAM）来区分场景中的语义实例的公司，并进一步利用这些约束条件对匹配成本和传播进行逐像素补丁变形。同时，我们提出了一种独特的细化策略，将球面坐标和法线上的梯度下降与深度上的逐像素搜索间隔相结合，显著提高了重建三维模型的完整性。此外，我们采用期望最大化（EM）算法交替优化总匹配成本和超参数，有效地缓解了参数过度依赖经验调整的问题。对ETH3D高分辨率多视图立体基准和Tanks and Temples数据集的评估表明，我们的方法可以用更少的时间获得最先进的结果。 et.al.|[2401.06385](http://arxiv.org/abs/2401.06385)|null|
|**2024-01-12**|**Surgical-DINO: Adapter Learning of Foundation Models for Depth Estimation in Endoscopic Surgery**|目的：机器人手术中的深度估计在三维重建、手术导航和增强现实可视化中至关重要。尽管基础模型在许多视觉任务中表现出出色的性能，包括深度估计（例如，DINOv2），但最近的工作观察到其在医学和外科领域特定应用中的局限性。这项工作提出了一种用于手术深度估计的基础模型的低阶自适应（LoRA）。方法：我们设计了一种基于基础模型的深度估计方法，称为Surgical DINO，这是对DINOv2的低阶自适应，用于内窥镜手术中的深度估计。我们构建了LoRA层，并将其集成到DINO中，以适应手术特定领域的知识，而不是传统的微调。在训练过程中，我们冻结了显示出出色视觉表示能力的DINO图像编码器，并仅优化了LoRA层和深度解码器，以集成来自手术场景的特征。结果：我们的模型在SCARED的MICCAI挑战数据集上得到了广泛验证，该数据集是从达芬奇Xi内窥镜手术中收集的。我们的经验表明，外科DINO在内窥镜深度估计任务中显著优于所有最先进的模型。消融研究的分析表明，我们的LoRA层和适应具有显著效果。结论：外科DINO为基础模型成功适应外科领域进行深度估计提供了一些启示。结果中有明确证据表明，对计算机视觉数据集中预先训练的权重进行零样本预测或简单微调不足以直接在外科领域使用基础模型。代码位于https://github.com/BeileiCui/SurgicalDINO. et.al.|[2401.06013](http://arxiv.org/abs/2401.06013)|**[link](https://github.com/beileicui/surgicaldino)**|
|**2024-01-10**|**Structure from Duplicates: Neural Inverse Graphics from a Pile of Objects**|我们的世界充满了相同的物体（例如，可乐罐、同一型号的汽车）。当这些重复出现在一起时，为我们有效地推理3D提供了额外而有力的线索。受这一观察结果的启发，我们引入了“重复结构”（SfD），这是一种新颖的逆图形框架，可以从包含多个相同对象的单个图像中重建几何体、材料和照明。SfD首先识别图像中对象的多个实例，然后联合估计所有实例的6DoF姿势。随后使用反向图形管道来联合推理对象的形状、材质和环境光，同时遵守实例之间的共享几何图形和材质约束。我们的主要贡献包括利用对象副本作为单图像逆图形的鲁棒先验，并提出用于联合6-DoF对象姿态估计的平面内旋转鲁棒运动结构（SfM）公式。通过利用来自单个图像的多视图线索，SfD生成了更真实、更详细的3D重建，显著优于具有相似或更多观测值的现有单个图像重建模型和多视图重建方法。 et.al.|[2401.05236](http://arxiv.org/abs/2401.05236)|**[link](https://github.com/tianhang-cheng/sfd)**|
|**2024-01-08**|**AGG: Amortized Generative 3D Gaussians for Single Image to 3D**|考虑到对自动3D内容创建管道的日益增长的需求，已经研究了各种3D表示来从单个图像生成3D对象。由于其优越的渲染效率，基于3D高斯飞溅的模型最近在3D重建和生成方面都表现出色。用于图像到3D生成的3D高斯飞溅方法通常是基于优化的，需要许多计算昂贵的分数提取步骤。为了克服这些挑战，我们引入了一种分期生成的3D高斯框架（AGG），该框架可以从单个图像中立即生成3D高斯，无需按实例优化。AGG利用中间混合表示分解3D高斯位置和其他外观属性的生成，用于联合优化。此外，我们提出了一种级联流水线，该流水线首先生成3D数据的粗略表示，然后使用3D高斯超分辨率模块对其进行上采样。我们的方法是根据现有的基于优化的3D高斯框架和利用其他3D表示的基于采样的管道进行评估的，其中AGG在质量和数量上都表现出有竞争力的生成能力，同时速度快几个数量级。项目页面：https://ir1d.github.io/AGG/ et.al.|[2401.04099](http://arxiv.org/abs/2401.04099)|null|

<p align=right>(<a href=#updated-on-20240121>back to top</a>)</p>

## Diffusion

|Publish Date|Title|Abstract|PDF|Code|
|---|---|---|---|---|
|**2024-01-18**|**A Simple Latent Diffusion Approach for Panoptic Segmentation and Mask Inpainting**|泛光学和实例分割网络通常使用专门的对象检测模块、复杂的损失函数和专门的后处理步骤来训练，以处理实例掩码的排列不变性。这项工作建立在稳定扩散的基础上，并提出了一种用于全景分割的潜在扩散方法，从而产生了一种省略这些复杂性的简单架构。我们的训练过程包括两个步骤：（1）训练浅层自动编码器，将分割掩模投影到潜在空间；（2） 训练扩散模型以允许在潜在空间中进行图像条件采样。生成模型的使用开启了掩模完成或修复的探索，这在交互式分割中有应用。实验验证为全景分割和掩模修复都产生了有希望的结果。虽然没有设定新的最先进技术，但我们的模型的简单性、通用性和掩模完成能力是理想的特性。 et.al.|[2401.10227](http://arxiv.org/abs/2401.10227)|**[link](https://github.com/segments-ai/latent-diffusion-segmentation)**|
|**2024-01-18**|**Towards Language-Driven Video Inpainting via Multimodal Large Language Models**|我们介绍了一种新的任务——语言驱动的视频修复，它使用自然语言指令来指导修复过程。这种方法克服了传统视频修复方法的局限性，这些方法依赖于手动标记的二进制掩模，这一过程通常是乏味和劳动密集的。我们展示了“按指令从视频中删除对象”（ROVI）数据集，其中包含5650个视频和9091个修复结果，以支持该任务的培训和评估。我们还提出了一种新的基于扩散的语言驱动的视频修复框架，这是该任务的第一个端到端基线，集成了多模式大型语言模型，以有效地理解和执行复杂的基于语言的修复请求。我们的综合结果展示了数据集的多功能性和模型在各种语言指导的修复场景中的有效性。我们将公开数据集、代码和模型。 et.al.|[2401.10226](http://arxiv.org/abs/2401.10226)|null|
|**2024-01-18**|**An Invariance Principle for a Random Walk Among Moving Traps via Thermodynamic Formalism**|我们考虑 $｛\mathbb Z｝^d$上移动陷阱的泊松云之间的随机游动，其中游动以与占据相同位置的陷阱数量成比例的速率被杀死。在维度$d=1$中，我们之前已经证明，在以生存到时间$t$为条件的随机游动的退火定律下，游动是亚扩散的。在这里，我们证明了在$d\geq6$ 和扩散标度下，如果杀伤率很小，则该退火定律满足具有正扩散常数的不变性原理。我们的证明是基于热力学形式论，其中我们将有限字母表和可和变分势的马尔可夫位移的一些经典结果推广到不可数非紧字母表的情况。 et.al.|[2401.10179](http://arxiv.org/abs/2401.10179)|null|
|**2024-01-18**|**Motion-Zero: Zero-Shot Moving Object Control Framework for Diffusion-Based Video Generation**|最近的大规模预训练扩散模型已经证明了从详细的文本描述中产生高质量视频的强大生成能力。然而，对由任何视频扩散模型生成的视频中的对象的运动施加控制是一个具有挑战性的问题。在本文中，我们提出了一种新的零样本运动物体轨迹控制框架Motion-zero，以实现边界-边界-目标-控制的文本到视频扩散模型。为此，初始噪声先验模块被设计为提供基于位置的先验，以提高移动物体的外观稳定性和位置精度。此外，基于U-net的注意力图，将空间约束直接应用于扩散模型的去噪过程，进一步确保了推理过程中运动对象的位置和空间一致性。此外，所提出的转移时间注意力机制保证了时间一致性。我们的方法可以灵活地应用于各种最先进的视频扩散模型，而无需任何训练过程。大量实验表明，我们提出的方法可以控制物体的运动轨迹，生成高质量的视频。 et.al.|[2401.10150](http://arxiv.org/abs/2401.10150)|null|
|**2024-01-18**|**Quantitative equilibrium fluctuations for interacting particle systems**|我们考虑了一类非梯度型连续空间中的相互作用粒子系统，该系统对于密度不变的泊松点过程是可逆的。对于这些模型，最近在10.1214/22-AOP1573中获得了体扩散矩阵的某些有限体积近似的收敛速度。在这里，我们展示了如何利用这一点来获得捕捉这些系统的大规模波动的许多结果的定量版本，例如两点相关函数的收敛性和Green Kubo公式。 et.al.|[2401.10080](http://arxiv.org/abs/2401.10080)|null|
|**2024-01-18**|**DiffusionGPT: LLM-Driven Text-to-Image Generation System**|扩散模型为图像生成领域开辟了新的途径，导致开源平台上共享的高质量模型激增。然而，一个主要挑战仍然存在于当前的文本到图像系统中，该系统通常无法处理不同的输入，或者仅限于单个模型结果。目前的统一尝试通常分为两个正交方面：一是在输入阶段解析不同的提示；ii）激活专家模型进行输出。为了将两者的优点结合起来，我们提出了DiffusionGPT，它利用大型语言模型（LLM）提供一个统一的生成系统，能够无缝地适应各种类型的提示并集成领域专家模型。DiffusionGPT基于先验知识为各种生成模型构建领域特定树。当提供输入时，LLM解析提示，并使用思想树来指导选择适当的模型，从而放松输入约束，确保跨不同领域的卓越性能。此外，我们引入了优势数据库，其中思想树富含人类反馈，使模型选择过程与人类偏好保持一致。通过广泛的实验和比较，我们展示了DiffusionGPT的有效性，展示了其在不同领域突破图像合成边界的潜力。 et.al.|[2401.10061](http://arxiv.org/abs/2401.10061)|null|
|**2024-01-18**|**Drift Control with Discretionary Stopping for a Diffusion Process**|我们考虑无限时间域上扩散过程漂移的具有任意停止的随机控制。目标是选择控制过程和停止时间，以在存在固定操作成本和每单位经过时间的控制相关运行成本的情况下最小化凸终端成本的期望。在控制扩散系数的适当条件下，证明了存在一对最优控制和停止规则。此外，在相同的假设下，证明了最优控制是一个可以相当明确地计算的常数；并且在第一次访问适当的间隔时停止是最佳的。我们还考虑了上述问题的一个约束版本，其中对可用停止时间的期望施加了上限；我们证明了这个有约束的问题可以简化为一个参数适当变化的无约束问题，从而用相似的自变量求解。 et.al.|[2401.10043](http://arxiv.org/abs/2401.10043)|null|
|**2024-01-18**|**FreGrad: Lightweight and Fast Frequency-aware Diffusion Vocoder**|本文的目标是用一种名为FreGrad的轻量级快速扩散声码器生成逼真的音频。我们的框架由以下三个关键组成部分组成：（1）我们采用离散小波变换，将复杂的波形分解为子带小波，这有助于FreGrad在简单简洁的特征空间上操作；（2）我们设计了一种频率感知的扩展卷积，提高了频率感知，从而生成具有准确频率信息的语音，以及（3）我们介绍了一系列提高所提出模型的生成质量的技巧。在我们的实验中，与基线相比，FreGrad实现了3.7倍的训练时间和2.2倍的推理速度，同时在不牺牲输出质量的情况下将模型大小减少了0.6倍（仅1.78M个参数）。音频样本位于：https://mm.kaist.ac.kr/projects/FreGrad. et.al.|[2401.10032](http://arxiv.org/abs/2401.10032)|null|
|**2024-01-18**|**CustomVideo: Customizing Text-to-Video Generation with Multiple Subjects**|定制的文本到视频生成旨在通过文本提示和主题参考生成高质量的视频。目前为单一主题设计的方法难以解决多个主题，这是一个更具挑战性和实用性的场景。在这项工作中，我们旨在促进多主题引导文本到视频定制。我们提出了CustomVideo，这是一个新的框架，可以在多个主题的指导下生成身份保护视频。具体来说，首先，我们通过将多个主体组合在一个图像中来鼓励它们的共同出现。此外，在一个基本的文本到视频扩散模型的基础上，我们设计了一种简单而有效的注意力控制策略来解开扩散模型潜在空间中的不同主体。此外，为了帮助模型聚焦于特定的对象区域，我们从给定的参考图像中分割对象，并为注意力学习提供相应的对象掩码。此外，我们收集了一个多主题文本到视频生成数据集作为综合基准，其中包括69个单独的主题和57个有意义的配对。大量的定性、定量和用户研究结果表明，与以前最先进的方法相比，我们的方法具有优越性。 et.al.|[2401.09962](http://arxiv.org/abs/2401.09962)|null|
|**2024-01-18**|**Consistent asset modelling with random coefficients and switches between regimes**|我们探索了一个随机模型，该模型能够以两种特定的方式捕捉外部影响。该模型允许在随机动力学的参数化中表达不确定性，并结合模式来解释不同时间或状态下的不同行为。为了建立我们的框架，我们首先构建了一个具有随机参数的模型，其中状态之间的切换可以由随机变量决定，也可以由确定性决定。这样的模型具有很强的可解释性。我们通过证明该框架可以通过采用标准跳跃扩散形式的局部波动率模型来优雅地表达，从而进一步确保数学一致性。此外，我们还考虑了一种马尔可夫调制方法，用于在以随机参数为特征的状态之间进行切换。对于所有考虑的模型，我们推导出特征函数，提供了一个具有广泛应用的通用工具。在一个数值实验中，我们将该框架应用于期权定价的财务问题。在两种制度模型中分析了参数不确定性的影响，其中资产过程在分别充满高不确定性和低不确定性的高波动期和低波动期之间切换。 et.al.|[2401.09955](http://arxiv.org/abs/2401.09955)|null|

<p align=right>(<a href=#updated-on-20240121>back to top</a>)</p>

## NeRF

|Publish Date|Title|Abstract|PDF|Code|
|---|---|---|---|---|
|**2024-01-17**|**Reproducibility via neural fields of visual illusions induced by localized stimuli**|本文研究了Billock和Tsou[PNAS，2007]使用Amari型神经场的可控性对初级视皮层（V1）皮层活动进行建模的实验复制，重点关注中央凹或外周视野中的规则漏斗模式。其目的是理解和模拟在这些实验中观察到的视觉现象，强调其非线性性质。这项研究包括设计模拟Billock和Tsou实验中视觉刺激的感官输入。然后从理论和数值上研究这些输入引起的后图像，以确定它们复制实验观察到的视觉效果的能力。这项研究的一个关键方面是研究神经反应的非线性性质所引起的影响。特别是，通过强调兴奋性和抑制性神经元在某些视觉现象出现中的重要性，这项研究表明，这两种类型的神经元活动的相互作用在视觉过程中发挥着重要作用，挑战了后者主要由兴奋性活动单独驱动的假设。 et.al.|[2401.09108](http://arxiv.org/abs/2401.09108)|null|
|**2024-01-12**|**Motion2VecSets: 4D Latent Vector Set Diffusion for Non-rigid Shape Reconstruction and Tracking**|我们介绍了Motion2VecSets，这是一种用于从点云序列进行动态曲面重建的4D扩散模型。虽然现有的最先进的方法已经证明在使用神经场表示重建非刚性对象方面取得了成功，但传统的前馈网络遇到了来自噪声、部分或稀疏点云的模糊观测的挑战。为了应对这些挑战，我们引入了一种扩散模型，该模型通过压缩潜在表示的迭代去噪过程来显式学习非刚性对象的形状和运动分布。当处理模糊输入时，基于扩散的先验能够进行更合理和概率的重建。我们用潜在向量集参数化4D动力学，而不是使用全局潜在。这种新颖的4D表示使我们能够学习局部表面形状和变形模式，从而实现更准确的非线性运动捕捉，并显著提高对看不见的运动和身份的可推广性。对于更具时间连贯性的目标跟踪，我们同步地对变形潜集进行去噪，并在多个帧之间交换信息。为了避免计算开销，我们设计了一个交错的空间和时间注意力块，以沿着空间和时间域交替聚集变形潜伏期。与最先进的方法进行了广泛的比较，证明了我们的Motion2VenSets在从各种不完美的观测进行4D重建方面的优势，特别是在从DeformingThings4D Animals数据集上的稀疏点云重建看不见的个体方面，与CaDex相比，交集优于并集（IoU）提高了19%。更多详细信息，请访问https://vveicao.github.io/projects/Motion2VecSets/. et.al.|[2401.06614](http://arxiv.org/abs/2401.06614)|null|
|**2024-01-05**|**Denoising Vision Transformers**|我们深入研究了视觉转换器（ViTs）固有的一个细微但重大的挑战：这些模型的特征图显示出网格状的伪影，这对ViTs在下游任务中的性能造成了不利影响。我们的研究将这个基本问题追溯到输入阶段的位置嵌入。为了解决这一问题，我们提出了一种新的噪声模型，该模型普遍适用于所有的ViT。具体来说，噪声模型将ViT输出分解为三个部分：一个没有噪声伪影的语义术语和两个以像素位置为条件的伪影相关术语。这种分解是通过在每幅图像的基础上加强与神经场的交叉视图特征一致性来实现的。这种逐图像优化过程从原始ViT输出中提取无伪影特征，为离线应用程序提供干净的特征。扩大了我们的解决方案的范围，以支持在线功能，我们引入了一种可学习的去噪器，直接从未处理的ViT输出中预测无伪影特征，这显示出对新数据的显著泛化能力，而无需对每张图像进行优化。我们的两阶段方法，称为去噪视觉转换器（DVT），不需要重新训练现有的预先训练的ViT，并且立即适用于任何基于转换器的架构。我们在各种具有代表性的ViT（DINO、MAE、DeiT III、EVA02、CLIP、DINOv2、DINOv2-reg）上评估了我们的方法。广泛的评估表明，我们的DVT在多个数据集（例如+3.84mIoU）的语义和几何任务中持续显著地改进了现有的最先进的通用模型。我们希望我们的研究将鼓励对ViT设计进行重新评估，特别是关于位置嵌入的天真使用。 et.al.|[2401.02957](http://arxiv.org/abs/2401.02957)|null|
|**2023-12-30**|**PlanarNeRF: Online Learning of Planar Primitives with Neural Radiance Fields**|从视觉数据中识别空间完整的平面基元是计算机视觉中的一项关键任务。现有的方法在很大程度上局限于2D片段恢复或简化3D结构，即使具有广泛的平面注释。我们提出了PlanarNeRF，这是一种能够通过在线学习检测密集3D平面的新框架。PlanarNeRF利用神经场表示，带来了三个主要贡献。首先，它利用并行的外观和几何知识增强了三维平面检测。其次，提出了一种轻量级的平面拟合模块来估计平面参数。第三，引入了一种具有更新机制的新的全局内存库结构，确保了跨帧一致性。PlanarNeRF的灵活架构使其能够在二维监督和自监督解决方案中发挥作用，在每种解决方案中，它都可以有效地从稀疏的训练信号中学习，显著提高训练效率。通过广泛的实验，我们证明了PlanarNeRF在各种场景下的有效性，并比现有工作有了显著的改进。 et.al.|[2401.00871](http://arxiv.org/abs/2401.00871)|null|
|**2024-01-01**|**Deblurring 3D Gaussian Splatting**|最近对辐射场的研究为具有照片级真实感渲染质量的新颖视图合成铺平了坚实的道路。然而，它们通常使用神经网络和体积绘制，这两种方法的训练成本很高，并且由于绘制时间长，阻碍了它们在各种实时应用中的广泛使用。最近，人们提出了一种基于3D高斯散射的方法来对3D场景进行建模，并在实时渲染图像的同时实现了显著的视觉质量。然而，如果训练图像模糊，则渲染质量会严重下降。模糊通常是由于镜头散焦、物体运动和相机抖动而产生的，它不可避免地会干扰干净图像的获取。先前的几项研究试图使用神经场从模糊的输入图像中渲染干净清晰的图像。然而，这些工作中的大多数仅设计用于基于体积渲染的神经辐射场，并不直接适用于基于光栅化的3D高斯散射方法。因此，我们提出了一种新的实时去模糊框架，即去模糊3D高斯散点，使用小型多层感知器（MLP）来操纵每个3D高斯的协方差来对场景模糊度进行建模。虽然去模糊的3D高斯飞溅仍然可以享受实时渲染，但它可以从模糊的图像中重建精细和清晰的细节。在基准上进行了各种实验，结果表明了我们的去模糊方法的有效性。定性结果可在https://benhenryl.github.io/Deblurring-3D-Gaussian-Splatting/ et.al.|[2401.00834](http://arxiv.org/abs/2401.00834)|null|
|**2023-12-22**|**Fluid Simulation on Neural Flow Maps**|我们介绍了神经流图，这是一种新的模拟方法，将新兴的隐式神经表示范式与基于流图理论的流体模拟相结合，以实现最先进的无粘流体现象模拟。我们设计了一种新的混合神经场表示，空间稀疏神经场（SSNF），它将小型神经网络与重叠、多分辨率和空间稀疏网格的金字塔相融合，以高精度紧凑地表示长期时空速度场。有了这个神经速度缓冲器，我们以机械对称的方式计算长期双向流图及其雅可比矩阵，以促进对现有解决方案的大幅精度提高。这些长程双向流图实现了低耗散的高平流精度，进而促进了高保真度的不可压缩流模拟，显示了复杂的旋涡结构。我们展示了我们的神经流体模拟在各种具有挑战性的模拟场景中的有效性，包括跳跃涡流、碰撞涡流、涡流重新连接，以及移动障碍物和密度差异产生的涡流。我们的例子表明，在能量守恒、视觉复杂性、对实验观测的遵守以及详细旋涡结构的保存方面，与现有方法相比，性能有所提高。 et.al.|[2312.14635](http://arxiv.org/abs/2312.14635)|null|
|**2023-12-21**|**Geometric Awareness in Neural Fields for 3D Human Registration**|将模板与三维人体点云对齐是一个长期存在的问题，对于动画、重建和启用监督学习管道等任务至关重要。最近的数据驱动方法利用了预测的表面对应关系；然而，它们对不同的姿态或分布并不鲁棒。相比之下，工业解决方案往往依赖于昂贵的手动注释或多视图捕获系统。最近，神经场已经显示出有希望的结果，但它们纯粹的数据驱动性质缺乏几何意识，通常导致模板配准的微小错位。在这项工作中，我们提出了两种解决方案：LoVD，一种新的神经场模型，它预测朝向目标表面上的局部SMPL顶点的方向；和INT，这是第一个专门用于神经领域的自监督任务，在测试时，它利用目标几何结构来细化主干。我们将它们组合到INLoVD中，这是一个在大型MoCap数据集上训练的强大的3D人体注册管道。INLoVD是高效的（不到一分钟），在公共基准上稳定地达到了最先进的水平，并对分布外的数据提供了前所未有的概括。我们将在\url｛url｝中发布代码和检查点。 et.al.|[2312.14024](http://arxiv.org/abs/2312.14024)|null|
|**2023-12-20**|**Neural feels with neural fields: Visuo-tactile perception for in-hand manipulation**|为了实现人类水平的灵活性，机器人必须从多模式感知推断空间意识，以推理接触互动。在新物体的手操作过程中，这种空间意识包括估计物体的姿势和形状。手内感知的现状主要采用视觉，并局限于跟踪先验已知对象。此外，在操作过程中，手上物体的视觉遮挡迫在眉睫，这阻止了当前系统在没有遮挡的情况下超越任务。我们将多指手的视觉和触摸传感相结合，在手内操作过程中估计物体的姿势和形状。我们的方法NeuralFeels通过在线学习神经场来编码对象几何，并通过优化姿态图问题来联合跟踪它。我们研究了模拟和现实世界中的多模式手部感知，通过本体感觉驱动的策略与不同的物体进行交互。我们的实验显示，使用已知的CAD模型，最终重建F分数为 $81$%，平均姿势漂移为$4.7\，\text｛mm｝$，进一步降低到$2.3\，\text{mm｝$。此外，我们观察到，与仅使用视觉的方法相比，在严重的视觉遮挡下，我们可以实现高达94$ %的跟踪改进。我们的研究结果表明，在手部操作过程中，触摸至少可以改善视觉估计，并在最好的情况下消除视觉估计的歧义。我们发布了70个实验的评估数据集FeelSight，作为在该领域进行基准测试的一步。我们由多模态感知驱动的神经表示可以作为提高机器人灵活性的感知支柱。视频可以在我们的项目网站上找到https://suddhu.github.io/neural-feels/ et.al.|[2312.13469](http://arxiv.org/abs/2312.13469)|null|
|**2023-12-20**|**Deep Learning on 3D Neural Fields**|近年来，神经场（NFs）已成为编码各种连续信号（如图像、视频、音频和3D形状）的有效工具。当应用于3D数据时，NFs提供了一种解决方案来解决与流行的离散表示相关的碎片化和局限性。然而，鉴于神经网络本质上是神经网络，目前尚不清楚它们是否以及如何无缝集成到深度学习管道中，以解决下游任务。本文解决了这一研究问题，并介绍了nf2vec，这是一个能够在单个推理过程中为输入NF生成紧凑的潜在表示的框架。我们证明了nf2vec有效地嵌入了由输入NF表示的3D对象，并展示了如何在深度学习管道中使用由此产生的嵌入来成功地处理各种任务，同时只处理NF。我们在几个用于表示3D曲面的NFs上测试了这个框架，例如无符号/有符号距离和占用字段。此外，我们用更复杂的NFs证明了我们的方法的有效性，这些NFs包括3D对象的几何形状和外观，如神经辐射场。 et.al.|[2312.13277](http://arxiv.org/abs/2312.13277)|null|
|**2023-12-16**|**How to Train Neural Field Representations: A Comprehensive Study and Benchmark**|神经场（NeFs）最近已成为一种用于对各种模态（包括图像、形状和场景）的信号进行建模的通用方法。随后，许多工作探索了使用NeF作为下游任务的表示，例如，根据适合的NeF的参数对图像进行分类。然而，NeF超参数对其作为下游表示的质量的影响很少被理解，而且在很大程度上仍未被探索。这在一定程度上是由于拟合神经场数据集所需的大量时间造成的。在这项工作中，我们提出了 $\verb|fit-a-nef|$ ，这是一个基于JAX的库，它利用并行化来实现大规模nef数据集的快速优化，从而显著加快速度。有了这个库，我们进行了一项全面的研究，研究了不同超参数——包括初始化、网络架构和优化策略——对下游任务的NeF拟合的影响。我们的研究为如何训练NeF提供了宝贵的见解，并为优化其在下游应用中的有效性提供了指导。最后，基于所提出的库和我们的分析，我们提出了Neural Field Arena，这是一个由流行视觉数据集的神经场变体组成的基准，包括MNIST、CIFAR、ImageNet和ShapeNetv2的变体。我们的图书馆和神经领域竞技场将是开源的，以引入标准化的基准测试，并促进对神经领域的进一步研究。 et.al.|[2312.10531](http://arxiv.org/abs/2312.10531)|**[link](https://github.com/samuelepapa/fit-a-nef)**|

<p align=right>(<a href=#updated-on-20240121>back to top</a>)</p>

[contributors-shield]: https://img.shields.io/github/contributors/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[contributors-url]: https://github.com/Vincentqyw/cv-arxiv-daily/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[forks-url]: https://github.com/Vincentqyw/cv-arxiv-daily/network/members
[stars-shield]: https://img.shields.io/github/stars/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[stars-url]: https://github.com/Vincentqyw/cv-arxiv-daily/stargazers
[issues-shield]: https://img.shields.io/github/issues/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[issues-url]: https://github.com/Vincentqyw/cv-arxiv-daily/issues

