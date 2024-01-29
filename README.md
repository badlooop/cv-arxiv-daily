[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]

## Updated on 2024.01.29
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
|**2024-01-26**|**3D Reconstruction and New View Synthesis of Indoor Environments based on a Dual Neural Radiance Field**|同时实现室内环境的3D重建和新视图合成具有广泛的应用，但在技术上非常具有挑战性。基于隐式神经函数的现有技术方法可以获得极好的三维重建结果，但它们在新视图合成方面的性能可能不令人满意。神经辐射场（NeRF）的令人兴奋的发展彻底改变了新的视图合成，然而，基于NeRF的模型可能无法重建干净的几何表面。我们开发了一种双神经辐射场（Du-NeRF），以同时实现高质量的几何重建和视图渲染。Du-NeRF包含两个几何场，一个从SDF场导出以便于几何重建，另一个从密度场导出以促进新视图合成。Du NeRF的一个创新特征是，它将视图无关分量与密度场解耦，并将其用作标签来监督SDF场的学习过程。这减少了形状辐射模糊性，并使几何图形和颜色在学习过程中相互受益。大量实验表明，Du-NeRF可以显著提高室内环境下新视图合成和3D重建的性能，并且在构建包含不服从多视图颜色一致性的精细几何图形的区域时尤其有效。 et.al.|[2401.14726](http://arxiv.org/abs/2401.14726)|null|
|**2024-01-23**|**IRIS: Inverse Rendering of Indoor Scenes from Low Dynamic Range Images**|尽管许多3D重建和新颖的视图合成方法允许从消费者相机轻松捕捉的多视图图像中真实地渲染场景，但它们在表示中烘焙照明，无法支持高级应用程序，如材质编辑、重新照明和虚拟对象插入。通过反向渲染重建基于物理的材料特性和照明有望实现此类应用。然而，大多数反向渲染技术都需要高动态范围（HDR）图像作为输入，这是大多数用户无法访问的设置。我们提出了一种方法，从多视图、低动态范围（LDR）图像中恢复场景的基于物理的材料特性和空间变化的HDR照明。我们在反向渲染管道中对LDR图像形成过程进行建模，并提出了一种新的材料、照明和相机响应模型的优化策略。与采用LDR或HDR输入的最先进的反向渲染方法相比，我们使用合成场景和真实场景来评估我们的方法。我们的方法优于以LDR图像作为输入的现有方法，并允许高度逼真的重新照明和对象插入。 et.al.|[2401.12977](http://arxiv.org/abs/2401.12977)|null|
|**2024-01-24**|**RGBD Objects in the Wild: Scaling Real-World 3D Object Learning from RGB-D Videos**|我们介绍了一种新的在野外捕获的RGB-D对象数据集，称为WildRGB-D。与大多数现有的仅带有RGB捕获的以对象为中心的真实世界数据集不同，深度通道的直接捕获允许更好的3D注释和更广泛的下游应用。WildRGB-D包括大型类别级RGB-D对象视频，这些视频是用iPhone 360度环绕对象拍摄的。它包含大约8500个记录对象和近20000个RGB-D视频，涉及46个常见对象类别。这些视频是在三种设置的不同杂乱背景下拍摄的，以覆盖尽可能多的真实世界场景：（i）一个视频中的单个对象；（ii）一个视频中的多个对象；以及（iii）在一个视频中具有静止手的对象。该数据集由对象遮罩、真实世界比例的相机姿态和RGBD视频中重建的聚合点云进行注释。我们用WildRGB-D对四个任务进行了基准测试，包括新颖的视图合成、相机姿态估计、物体6d姿态估计和物体表面重建。我们的实验表明，RGB-D对象的大规模捕获为推进3D对象学习提供了巨大的潜力。我们的项目页面是https://wildrgbd.github.io/. et.al.|[2401.12592](http://arxiv.org/abs/2401.12592)|null|
|**2024-01-23**|**Methods and strategies for improving the novel view synthesis quality of neural radiation field**|神经辐射场（NeRF）技术可以从2D图像中学习场景的3D隐式模型，并合成逼真的新视图图像。该技术得到了业界的广泛关注，具有良好的应用前景。针对NeRF图像渲染质量需要提高的问题，近三年来，许多研究人员提出了各种方法来提高渲染质量。对最新的相关论文进行了分类和综述，分析了质量改进背后的技术原理，并讨论了质量改进方法的未来发展方向。这项研究可以帮助研究人员快速了解该领域技术的现状和发展脉络，有助于激发更高效算法的发展，促进NeRF技术在相关领域的应用。 et.al.|[2401.12451](http://arxiv.org/abs/2401.12451)|null|
|**2024-01-22**|**HG3-NeRF: Hierarchical Geometric, Semantic, and Photometric Guided Neural Radiance Fields for Sparse View Inputs**|神经辐射场（NeRF）作为一种通过从离散观测中学习场景表示的新型视图合成范式，已经引起了人们的极大关注。然而，当面对稀疏视图输入时，NeRF表现出明显的性能退化，从而限制了其进一步的适用性。在这项工作中，我们介绍了层次几何、语义和光度引导的NeRF（HG3-NeRF），这是一种新的方法，可以解决上述限制，并增强不同视图中几何、语义内容和外观的一致性。我们提出了分层几何制导（HGG），将运动结构的附加（SfM），即稀疏深度先验，纳入场景表示中。与直接深度监督不同，HGG从局部几何区域到全局几何区域对体积点进行采样，减轻了深度先验中固有偏差引起的偏差。此外，我们从不同分辨率的图像中观察到的语义一致性的显著变化中获得了灵感，并提出了层次语义引导（HSG）来学习粗到细的语义内容，该内容对应于粗到细场景表示。实验结果表明，HG3-NeRF可以在不同的标准基准上优于其他最先进的方法，并实现稀疏视图输入的高保真度合成结果。 et.al.|[2401.11711](http://arxiv.org/abs/2401.11711)|null|
|**2024-01-18**|**Explaining the Implicit Neural Canvas: Connecting Pixels to Neurons by Tracing their Contributions**|隐式神经表示（INRs）的许多变体，其中神经网络被训练为信号的连续表示，对于下游任务具有巨大的实用性，包括新颖的视图合成、视频压缩和图像超分辨率。不幸的是，对这些网络的内部运作方式的研究严重不足。我们的工作，即解释隐式神经画布（XINC），是一个统一的框架，用于通过检查每个神经元对每个输出像素的贡献强度来解释INRs的特性。我们将这些贡献图的集合称为隐式神经画布，并使用这一概念来证明我们研究的INR学会了以令人惊讶的方式“观察”它们所代表的帧。例如，INR往往具有高度分布的表示。虽然缺乏高级对象语义，但它们对颜色和边缘有很大的偏见，而且几乎完全是空间不可知的。我们通过研究视频INR中对象在时间上的表现方式得出了我们的结论，使用聚类来可视化跨层和架构的相似神经元，并表明这是由运动主导的。这些见解证明了我们的分析框架的普遍有用性。我们的项目页面位于https://namithap10.github.io/xinc. et.al.|[2401.10217](http://arxiv.org/abs/2401.10217)|null|
|**2024-01-18**|**GPAvatar: Generalizable and Precise Head Avatar from Image(s)**|头部化身重建对于虚拟现实、在线会议、游戏和电影行业的应用至关重要，在计算机视觉界引起了极大的关注。该领域的基本目标是忠实地再现头部化身，并精确地控制表情和姿势。现有的方法分为基于2D的扭曲、基于网格和神经渲染方法，在保持多视图一致性、结合非面部信息和推广到新身份方面存在挑战。在本文中，我们提出了一个名为GPAvatar的框架，该框架可以在单个前向通道中从一个或多个图像重建3D头部化身。这项工作的关键思想是引入一个由点云驱动的动态基于点的表情场，以精确有效地捕捉表情。此外，我们在三平面规范场中使用多三平面注意力（MTA）融合模块来利用来自多个输入图像的信息。所提出的方法实现了忠实的身份重建、精确的表达控制和多视图一致性，在自由视点渲染和新颖视图合成方面显示了良好的效果。 et.al.|[2401.10215](http://arxiv.org/abs/2401.10215)|**[link](https://github.com/xg-chu/gpavatar)**|
|**2024-01-17**|**Objects With Lighting: A Real-World Dataset for Evaluating Reconstruction and Rendering for Object Relighting**|从照片中重建对象并将其虚拟地放置在新环境中超出了标准的新颖视图合成任务，因为对象的外观不仅要适应新颖的视点，还要适应新的照明条件，而且反向渲染方法的评估依赖于新颖的视图合成数据或用于定量分析的简单合成数据集。这项工作提供了一个真实世界的数据集，用于测量重新照明对象的重建和渲染。为此，我们捕获了多个环境中相同对象的环境照明和地面实况图像，从而可以从一个环境中拍摄的图像中重建对象，并量化看不见的照明环境的渲染视图的质量。此外，我们介绍了一个由现成方法组成的简单基线，并在重新照明任务中测试了几种最先进的方法，表明新的视图合成不是衡量性能的可靠指标。代码和数据集可在https://github.com/isl-org/objects-with-lighting . et.al.|[2401.09126](http://arxiv.org/abs/2401.09126)|**[link](https://github.com/isl-org/objects-with-lighting)**|
|**2024-01-17**|**ICON: Incremental CONfidence for Joint Pose and Radiance Field Optimization**|在给定一组2D图像的情况下，神经辐射场（NeRF）在新视图合成（NVS）中表现出显著的性能。然而，NeRF训练需要每个输入视图的精确相机姿势，通常通过运动结构（SfM）管道获得。最近的作品试图放松这种限制，但它们仍然经常依赖于可以改进的体面的初始姿势。在这里，我们旨在消除姿势初始化的要求。我们提出了增量置信（ICON），这是一种从2D视频帧中训练NeRF的优化过程。ICON仅假设相机运动平滑，以估计姿势的初始猜测。此外，ICON引入了“置信度”：一种用于动态重加权梯度的模型质量自适应度量。ICON依赖于高置信度姿势来学习NeRF，并依赖于高置信度3D结构（由NeRF编码）来学习姿势。我们表明，与使用SfM姿势的方法相比，ICON在没有预先初始化姿势的情况下，在CO3D和HO3D中都实现了卓越的性能。 et.al.|[2401.08937](http://arxiv.org/abs/2401.08937)|null|
|**2024-01-16**|**Fast Dynamic 3D Object Generation from a Single-view Video**|由于缺乏4D标记的数据，从单视图视频生成动态三维（3D）对象是具有挑战性的。现有方法通过传输现成的图像生成模型（如分数蒸馏采样）来扩展文本到3D管道，但由于需要通过大型预训练模型反向传播信息有限的监督信号，这些方法的扩展速度慢且成本高（例如，每个对象150分钟）。为了解决这一限制，我们提出了一种高效的视频到4D对象生成框架，称为Efficient4D。它在不同的相机视图下生成高质量的时空一致图像，然后将其用作标记数据，直接训练具有显式点云几何结构的新型4D高斯飞溅模型，实现在连续相机轨迹下的实时渲染。对合成视频和真实视频的广泛实验表明，与现有技术的替代方案相比，Efficient4D的速度显著提高了10倍，同时保持了相同水平的创新视图合成质量。例如，Efficient4D只需14分钟即可对动态对象进行建模。 et.al.|[2401.08742](http://arxiv.org/abs/2401.08742)|null|

<p align=right>(<a href=#updated-on-20240129>back to top</a>)</p>

## 3D Reconstruction

|Publish Date|Title|Abstract|PDF|Code|
|---|---|---|---|---|
|**2024-01-26**|**Straight versus Spongy -- Effect of Tortuosity on Polymer Imbibition into Nanoporous Matrices Assessed by Segmentation-Free Analysis of 3D Sample Reconstructions**|通过X射线计算机断层扫描和EDX光谱，我们比较分析了聚苯乙烯（PS）在两个互补孔模型中的吸胀作用，这两个模型具有约380nm的孔径和羟基封端的无机氧化物孔壁，即可控多孔玻璃（CPG）和自有序多孔氧化铝（AAO）。CPG包含连续的海绵状曲折孔隙系统。包含孤立直圆柱形孔隙阵列的AAO是具有接近1的弯曲度的参考孔隙模型。时空自吸前沿演化的比较评估产生了关于被探测的弯曲基质（如CPG）的孔隙形态和自吸机制的重要信息。为此，将渗透的AAO和CPG样品的断层摄影3D重建和2D EDX图中的像素亮度分散浓缩为垂直于膜表面的1D亮度分散轮廓。他们的统计分析得出了渗吸前沿的位置和宽度，而没有对孔隙位置进行分割或确定。吸收前沿运动相对于AAO参考样品的延迟可以用作测试多孔基质的弯曲度的描述符。CPG中自吸前缘运动的速度等于AAO中自吸锋运动速度的三分之二。此外，自吸前沿加宽的动力学揭示了多孔基质是由圆柱形颈状孔段主导还是由节点主导。圆柱形AAO孔中的独立单个弯月面运动导致比CPG更快的自吸前沿加宽，其中由节点主导的形态导致涉及几个弯月面的较慢的协同自吸前沿运动。 et.al.|[2401.14950](http://arxiv.org/abs/2401.14950)|null|
|**2024-01-26**|**3D Reconstruction and New View Synthesis of Indoor Environments based on a Dual Neural Radiance Field**|同时实现室内环境的3D重建和新视图合成具有广泛的应用，但在技术上非常具有挑战性。基于隐式神经函数的现有技术方法可以获得极好的三维重建结果，但它们在新视图合成方面的性能可能不令人满意。神经辐射场（NeRF）的令人兴奋的发展彻底改变了新的视图合成，然而，基于NeRF的模型可能无法重建干净的几何表面。我们开发了一种双神经辐射场（Du-NeRF），以同时实现高质量的几何重建和视图渲染。Du-NeRF包含两个几何场，一个从SDF场导出以便于几何重建，另一个从密度场导出以促进新视图合成。Du NeRF的一个创新特征是，它将视图无关分量与密度场解耦，并将其用作标签来监督SDF场的学习过程。这减少了形状辐射模糊性，并使几何图形和颜色在学习过程中相互受益。大量实验表明，Du-NeRF可以显著提高室内环境下新视图合成和3D重建的性能，并且在构建包含不服从多视图颜色一致性的精细几何图形的区域时尤其有效。 et.al.|[2401.14726](http://arxiv.org/abs/2401.14726)|null|
|**2024-01-25**|**TIFu: Tri-directional Implicit Function for High-Fidelity 3D Character Reconstruction**|基于隐函数的方法的最新进展在从单个RGB图像进行3D人体重建方面显示出了有希望的结果。但是，这些方法不足以扩展到更一般的情况，通常会生成拖动或断开连接的身体部位，特别是对于动画角色。我们认为，这些限制源于使用现有的点级三维形状表示，该表示缺乏对三维上下文的整体理解。基于体素的重建方法更适合于一次捕获整个3D空间，然而，这些方法由于其过度的内存使用而不适用于高分辨率重建。为了应对这些挑战，我们引入了三向隐函数（TIFu），这是一种矢量级表示，与体素表示相比，它可以提高全局3D一致性，同时显著减少内存使用。我们还介绍了一种新的算法，通过沿三个正交轴聚合向量，在任意分辨率下进行三维重建，解决了向量固定维回归的固有问题。我们的方法在我们的自策划角色数据集和基准3D人体数据集中都实现了最先进的性能。我们提供了定量和定性分析来支持我们的发现。 et.al.|[2401.14565](http://arxiv.org/abs/2401.14565)|null|
|**2024-01-25**|**Range-Agnostic Multi-View Depth Estimation With Keyframe Selection**|从姿势帧进行3D重建的方法需要关于场景度量范围的先验知识，通常是为了恢复沿着核线的匹配线索并缩小搜索范围。然而，在真实场景中（例如，从视频序列进行户外3D重建），这种先验可能无法直接获得或估计不准确，因此严重阻碍了性能。在本文中，我们通过提出RAMDepth来专注于多视图深度估计，而不需要关于场景的度量范围的先验知识，RAMDepth是一种高效的纯2D框架，可以颠倒深度估计和匹配步骤的顺序。此外，我们展示了我们的框架提供有关用于预测的视图质量的丰富见解的能力。其他材料可以在我们的项目页面上找到https://andreaconti.github.io/projects/range_agnostic_multi_view_depth. et.al.|[2401.14401](http://arxiv.org/abs/2401.14401)|**[link](https://github.com/andreaconti/ramdepth)**|
|**2024-01-25**|**pix2gestalt: Amodal Segmentation by Synthesizing Wholes**|我们介绍了pix2gestalt，这是一种用于零样本amodal分割的框架，它可以学习估计在遮挡后仅部分可见的整个对象的形状和外观。通过利用大规模扩散模型并将其表示转移到这项任务中，我们学习了一个条件扩散模型，用于在具有挑战性的零样本情况下重建整个对象，包括打破自然和物理先验的例子，如艺术。作为训练数据，我们使用了一个综合策划的数据集，其中包含与整个对象配对的遮挡对象。实验表明，我们的方法在已建立的基准上优于监督基线。我们的模型还可以用于显著提高现有对象识别和3D重建方法在存在遮挡的情况下的性能。 et.al.|[2401.14398](http://arxiv.org/abs/2401.14398)|**[link](https://github.com/cvlab-columbia/pix2gestalt)**|
|**2024-01-25**|**GauU-Scene: A Scene Reconstruction Benchmark on Large Scale 3D Reconstruction Dataset Using Gaussian Splatting**|我们在扩展的U-scene数据集上，使用新开发的3D表示方法高斯飞溅，引入了一种新的大规模场景重建基准。U-Scene占地超过1.5平方公里，拥有一个综合的RGB数据集和激光雷达地面实况。在数据采集方面，我们使用了配备高精度Zenmuse L1激光雷达的Matrix 300无人机，实现了精确的屋顶数据采集。该数据集为超过1.5公里的高级空间分析转换提供了城市和学术环境的独特混合。我们对高斯飞溅U-Scene的评估包括对各种新颖视角的详细分析。我们还将这些结果与我们精确的点云数据集得出的结果并置，强调了显著的差异，强调了组合多模态信息的重要性 et.al.|[2401.14032](http://arxiv.org/abs/2401.14032)|null|
|**2024-01-24**|**EndoGaussians: Single View Dynamic Gaussian Splatting for Deformable Endoscopic Tissues Reconstruction**|在VR手术和医学图像分析等医学应用中，从内窥镜视频中精确重建可变形的软组织是一个关键挑战。现有的方法往往难以准确和模糊产生幻觉的组织部分，限制了它们的实用性。在这项工作中，我们介绍了EndoGaussians，这是一种利用高斯散射进行动态内窥镜三维重建的新方法。该方法标志着首次在这种情况下使用高斯散射，克服了以前基于NeRF的技术的局限性。我们的方法设定了新的最先进的标准，如对各种内窥镜数据集的定量评估所示。这些进步使我们的方法成为医学专业人员的一种很有前途的工具，为医学领域的实际应用提供更可靠、更高效的3D重建。 et.al.|[2401.13352](http://arxiv.org/abs/2401.13352)|null|
|**2024-01-23**|**IRIS: Inverse Rendering of Indoor Scenes from Low Dynamic Range Images**|尽管许多3D重建和新颖的视图合成方法允许从消费者相机轻松捕捉的多视图图像中真实地渲染场景，但它们在表示中烘焙照明，无法支持高级应用程序，如材质编辑、重新照明和虚拟对象插入。通过反向渲染重建基于物理的材料特性和照明有望实现此类应用。然而，大多数反向渲染技术都需要高动态范围（HDR）图像作为输入，这是大多数用户无法访问的设置。我们提出了一种方法，从多视图、低动态范围（LDR）图像中恢复场景的基于物理的材料特性和空间变化的HDR照明。我们在反向渲染管道中对LDR图像形成过程进行建模，并提出了一种新的材料、照明和相机响应模型的优化策略。与采用LDR或HDR输入的最先进的反向渲染方法相比，我们使用合成场景和真实场景来评估我们的方法。我们的方法优于以LDR图像作为输入的现有方法，并允许高度逼真的重新照明和对象插入。 et.al.|[2401.12977](http://arxiv.org/abs/2401.12977)|null|
|**2024-01-23**|**Consistency Enhancement-Based Deep Multiview Clustering via Contrastive Learning**|多视图聚类（MVC）通过综合多个视图中的信息，将数据样本分离成有意义的聚类。此外，基于深度学习的方法已经在MVC场景中展示了强大的特征学习能力。然而，在保持一致性的同时有效地泛化特征表示仍然是一个棘手的问题。此外，大多数现有的基于对比学习的深度聚类方法在聚类过程中忽视了聚类表示的一致性。在本文中，我们展示了如何克服上述问题，并通过对比学习（CCEC）提出了一种基于一致增强的深度MVC方法。具体而言，语义连接块被合并到特征表示中，以保持多个视图之间的一致信息。此外，通过光谱聚类增强了聚类的表示过程，并提高了多个视图之间的一致性。在五个数据集上进行的实验证明了与最先进的（SOTA）方法相比，我们的方法的有效性和优越性。此方法的代码可以访问https://anonymous.4open.science/r/CCEC-E84E/. et.al.|[2401.12648](http://arxiv.org/abs/2401.12648)|null|
|**2024-01-21**|**A Survey on African Computer Vision Datasets, Topics and Researchers**|计算机视觉包括一系列任务，如对象检测、语义分割和3D重建。尽管它与非洲社区有关，但在过去十年中，非洲国内这一领域的研究仅占顶级出版物的0.06%。这项研究对2012年至2022年来自非洲的63000份Scopus索引的计算机视觉出版物进行了彻底分析。其目的是提供对非洲计算机视觉主题、数据集和研究人员的调查。我们研究的一个关键方面是使用自动解析这些出版物摘要的大型语言模型对非洲计算机视觉数据集进行识别和分类。我们还提供了通过挑战或数据托管平台分发的非官方非洲计算机视觉数据集的汇编，并提供了数据集类别的完整分类。我们的调查还指出了不同非洲地区的计算机视觉主题趋势，表明了它们独特的关注领域。此外，我们进行了一项广泛的调查，以了解非洲研究人员对非洲大陆计算机视觉研究现状的看法，以及他们认为迫切需要关注的结构性障碍。总之，这项研究对非洲机构贡献或发起的计算机视觉数据集和主题进行了编目和分类，并确定了在顶级计算机视觉场所出版的障碍。这项调查强调了鼓励非洲研究人员和机构推进非洲大陆计算机视觉研究的重要性。它还强调研究主题需要与非洲社区的需求更加一致。 et.al.|[2401.11617](http://arxiv.org/abs/2401.11617)|null|

<p align=right>(<a href=#updated-on-20240129>back to top</a>)</p>

## Diffusion

|Publish Date|Title|Abstract|PDF|Code|
|---|---|---|---|---|
|**2024-01-26**|**Annotated Hands for Generative Models**|诸如GANs和扩散模型之类的生成模型已经展示了令人印象深刻的图像生成能力。尽管取得了这些成功，但这些系统在用手创建图像方面却出奇地差。我们为生成模型提出了一种新的训练框架，该框架大大提高了此类系统创建手部图像的能力。我们的方法是用三个额外的通道来增强训练图像，这些通道为图像中的手提供注释。这些注释提供了附加结构，该附加结构诱使生成模型产生更高质量的手部图像。我们在两个不同的生成模型上演示了这种方法：生成对抗性网络和扩散模型。我们在一个新的手部图像合成数据集和包含手的真实照片上展示了我们的方法。我们通过使用现成的手部检测器对手指关节识别进行更高的置信度来测量生成的手部的改进质量。 et.al.|[2401.15075](http://arxiv.org/abs/2401.15075)|**[link](https://github.com/YY-GX/Annotated-Hands-Dataset)**|
|**2024-01-26**|**Emulating Complex Synapses Using Interlinked Proton Conductors**|就能效和计算速度而言，基于非易失性存储设备的神经形态电子有望成为未来人工智能（AI）最有前途的硬件候选者之一。然而，灾难性遗忘，即网络在学习新任务时迅速覆盖先前学习的权重，仍然是数字或模拟人工智能芯片释放类脑计算真正力量的关键障碍。为了解决在线记忆存储中的灾难性遗忘问题，最近提出了一种复杂的突触模型（Benna Fusi模型）[1]，其突触权重和内部变量遵循扩散动力学演化。在这项工作中，我们通过设计一个带有一系列电荷扩散控制存储元件的质子晶体管，实验实现了Benna Fusi人工复杂突触。数值模拟和实验观察都揭示了耦合存储组件的内存整合。复杂突触的不同记忆时间尺度是由电荷载流子的扩散长度、耦合存储组件的容量和数量设计的。通过人脸熟悉度检测的神经网络模拟，揭示了所展示的复杂突触在记忆能力和记忆巩固方面的优势。我们对复杂突触的实验实现表明，这是一种提高记忆能力和实现持续学习的有前景的方法。 et.al.|[2401.15045](http://arxiv.org/abs/2401.15045)|null|
|**2024-01-26**|**Machine learning-based analysis of glioma tissue sections: a review**|近年来，胶质瘤的诊断变得越来越复杂。使用现代机器学习技术对神经胶质瘤组织进行组织学评估为支持诊断和结果预测提供了新的机会。为了概述研究现状，这篇综述考察了70项公开的基于机器学习的人类胶质瘤染色组织切片分析研究，涵盖了分型（16/70）、分级（23/70）、分子标记预测（13/70）和生存预测（27/70）的诊断任务。对所有研究的方法学方面以及临床适用性进行了回顾。研究发现，目前的研究重点是评估成人型弥漫性胶质瘤的苏木精和伊红染色组织切片。大多数研究（49/70）基于癌症基因组图谱（TCGA）中公开可用的胶质母细胞瘤和低级别胶质瘤数据集，只有少数研究单独使用了其他数据集（10/70）或除TCGA数据集（11/70）外使用了其他数据集。目前的方法主要依靠卷积神经网络（53/70）在20倍放大率（30/70）下分析组织。一个新的研究领域是临床数据、组学数据或磁共振成像的整合（27/70）。到目前为止，基于机器学习的方法已经取得了很有希望的结果，但尚未在实际的临床环境中使用。未来的工作应侧重于在更大的多站点数据集上对方法进行独立验证，这些数据集具有高质量和最新的临床和分子病理学注释，以证明常规的适用性。 et.al.|[2401.15022](http://arxiv.org/abs/2401.15022)|null|
|**2024-01-26**|**Volterra equations with affine drift: looking for stationarity**|我们研究了缩放Volterra方程（即具有仿射均值回归漂移）的解在有限水平和长期上的平稳性性质。特别地，我们证明了这样的方程从不具有平稳状态，除非核是常数（即方程是标准布朗扩散）或在一些完全退化的病理环境中。我们引入了与核相关的确定性稳定器 $\varsigma$，该稳定器在所有边际共享相同期望和方差的意义上产生｛\em假平稳状态｝。我们还证明，随着时间的无穷大，从开始各种初始值时开始的这种过程的边际在$L^2$中汇合。我们建立了对于某些类扩散系数（正二次多项式的平方根），此类Volterra方程的时移解弱函数收敛于共享相同协方差函数的$L^2$平稳过程族。我们将这些结果应用于（稳定的）粗糙波动率模型（当核$K（t）=t^{H-\frac12}$，$0<H<\frac12$ ），这导致产生伪平稳二次粗糙Heston模型。 et.al.|[2401.15021](http://arxiv.org/abs/2401.15021)|null|
|**2024-01-26**|**Accelerated relaxation enhancing flows cause total dissipation**|我们证明，通过“加速”弛豫增强流，可以构造一个在 $[0,1）\times\mathb{T}^d$上光滑但在$T=1$上高度奇异的流，因此对于任何正扩散率，与加速流相关的平流-扩散方程完全耗散解，将任意初始数据取为$ T=1美元处的常数函数。 et.al.|[2401.15001](http://arxiv.org/abs/2401.15001)|null|
|**2024-01-26**|**DAM: Diffusion Activation Maximization for 3D Global Explanations**|近年来，点云模型的性能得到了快速提高。然而，由于相关可解释性研究的数量有限，这些黑匣子模型的不可靠性和不透明性可能会在危及人类生命的应用中导致潜在风险，例如自动驾驶或医疗保健。这项工作提出了一种基于DDPM的点云全局可解释性方法（DAM），该方法利用点扩散变换器（PDT），一种新的点对称模型，具有双分类器指导，以生成高质量的全局解释。此外，还提出了一种适用于DAM的路径梯度积分方法，该方法不仅提供了点云类别显著性图的全局概览，而且揭示了解释的属性在生成过程中是如何变化的。大量实验表明，我们的方法在可感知性、代表性和多样性方面优于现有方法，显著缩短了生成时间。我们的代码位于：https://github.com/Explain3D/DAM et.al.|[2401.14938](http://arxiv.org/abs/2401.14938)|null|
|**2024-01-26**|**Characterisation of FG-type stars with an improved transport of chemical elements**|上下文化学输运机制的建模对于恒星的精确表征至关重要。原子扩散就是其中一个过程，它通常包含在恒星模型中。然而，对于F型或更大质量的恒星来说，它通常被忽略，因为它会产生不切实际的表面丰度变化。因此，必须考虑抵消原子扩散的其他机制。已经证明，湍流混合可以防止表面丰度的过度变化，也可以校准以模拟辐射加速度对铁的影响。目的。我们的目的是评估校准的湍流混合对F型恒星样本特征的影响，以及这些估计与忽略化学传输机制时获得的估计相比如何。方法。我们从两个样本中选择了恒星——一个来自开普勒LEGACY样本，另一个来自一个开普勒行星宿主恒星样本。我们使用两个网格来推断它们的恒星性质。第一个网格只在没有显示恒星表面化学过度变化的模型中考虑原子扩散。第二个网格包括所有恒星模型中的原子扩散和校准的湍流混合，以避免不切实际的表面丰度。后果比较两个网格的推导结果，我们发现，由于其中一个网格中没有原子扩散，我们样本中质量较大的恒星的质量、半径和年龄的推断值会有更高的色散。这可能导致单个恒星的相对不确定性，质量高达5%，半径高达2%，年龄高达20%。结论。这项工作表明，对微观输运过程进行适当的建模，不仅对G型恒星，而且对F型恒星，都是准确估计其基本性质的关键。 et.al.|[2401.14924](http://arxiv.org/abs/2401.14924)|null|
|**2024-01-26**|**Advanced iontronic spiking modes with multiscale diffusive dynamics in a fluidic circuit**|流体离子电子学正在成为实现神经形态电路的一个独特平台，其特点是依赖与大脑相同的水介质和离子信号载体。利用离子电子尖峰电路和水性电解质通过锥形离子通道（形成流体忆阻器）的动态传输的最新理论进展，我们扩展了离子电子电路中提出的神经元尖峰动力学的范围。通过一个包含携带双极表面电荷的通道的模拟电路，我们提取了相位爆发、混合模式尖峰、强直性爆发和阈值可变性，所有这些尖峰电压和频率都在哺乳动物神经元的典型范围内。这些特征是可能的，因为典型的电导记忆保持时间对通道长度的强烈依赖性，使得时间尺度能够在单个电路内从单个尖峰到多个尖峰的突发变化。这些高级形式的神经元样尖峰支持水离子电子学作为神经形态回路的有趣平台的探索。 et.al.|[2401.14921](http://arxiv.org/abs/2401.14921)|null|
|**2024-01-26**|**Social norms and cooperation in higher-order networks**|最近的研究重点是了解如何通过认知环境中的各种机制，特别是通过成对的互动来促进合作。然而，现实世界中的相互作用往往超越了简单的二元体，包括具有成对和高阶相互作用的多个派系。这些复杂的互动影响着个人如何根据社会规范来感知和调整他们的策略。我们在这里介绍了一个模型，该模型探讨了在异质环境中集体策略和社会规范的演变，包括二元和三体互动。我们发现，与简单地模仿最成功的邻居相比，社会规范在促进合作方面发挥着至关重要的作用。我们还表明，亲社会规范的兴起导致了在各种社会困境中的合作增加，通常导致从有缺陷的行为转变为合作行为。此外，我们观察到，适度的信息隐私有助于维持亲社会规范，减少反社会倾向，即使在相互叛逃似乎有利的情况下也是如此。因此，我们的研究通过高阶网络中的社会规范扩散的视角，对合作的演变提供了见解。 et.al.|[2401.14905](http://arxiv.org/abs/2401.14905)|null|
|**2024-01-26**|**Convergence analysis of the adaptive stochastic collocation finite element method**|本文主要研究具有参数系数的平稳扩散方程的自适应随机配置算法的收敛性分析。该算法在参数域中采用稀疏网格配置，在空间域中采用有限元近似，自适应性由最近提出的参数和空间后验误差指标驱动。我们证明了对于具有有限维参数化的一般扩散系数，该算法将潜在的误差估计驱动为零。因此，我们的分析涵盖了仿射和非仿射参数系数相关的问题。 et.al.|[2401.14894](http://arxiv.org/abs/2401.14894)|null|

<p align=right>(<a href=#updated-on-20240129>back to top</a>)</p>

## NeRF

|Publish Date|Title|Abstract|PDF|Code|
|---|---|---|---|---|
|**2024-01-26**|**Learning Neural Radiance Fields of Forest Structure for Scalable and Fine Monitoring**|这项工作利用神经辐射场和遥感技术用于林业应用。在这里，我们展示了神经辐射场为改进森林监测中现有的遥感方法提供了广泛的可能性。我们提出的实验证明了它们的潜力：（1）表达森林三维结构的精细特征，（2）融合可用的遥感模式，以及（3）改进三维结构衍生的森林指标。总之，这些特性使神经场成为一种有吸引力的计算工具，具有进一步提高森林监测程序的可扩展性和准确性的巨大潜力。 et.al.|[2401.15029](http://arxiv.org/abs/2401.15029)|null|
|**2024-01-25**|**Learning Robust Generalizable Radiance Field with Visibility and Feature Augmented Point Representation**|本文介绍了广义神经辐射场（NeRF）的一种新范式。以前的通用NeRF方法将多视点立体技术与基于图像的神经渲染相结合进行泛化，产生了令人印象深刻的结果，同时存在三个问题。首先，遮挡常常导致不一致的特征匹配。然后，由于采样点和粗略特征聚合的单独过程，它们在几何不连续性和局部尖锐形状中传递失真和伪影。第三，当源视图离目标视图不够近时，它们基于图像的表示会发生严重退化。为了应对挑战，我们提出了第一个基于点而不是基于图像的渲染构建可泛化神经场的范式，我们称之为可泛化神经点场（GPF）。我们的方法通过几何先验显式地建模可见性，并用神经特征增强它们。我们提出了一种新的非均匀对数采样策略，以提高渲染速度和重建质量。此外，我们提出了一种可学习的内核，该内核在空间上增加了用于特征聚合的特征，减轻了几何结构急剧变化的地方的失真。此外，我们的表现很容易被操纵。实验表明，在泛化和微调设置中，我们的模型可以在三个数据集上提供比所有对应模型和基准更好的几何结构、视图一致性和渲染质量，初步证明了可泛化NeRF新范式的潜力。 et.al.|[2401.14354](http://arxiv.org/abs/2401.14354)|null|
|**2024-01-24**|**Unified neural field theory of brain dynamics underlying oscillations in Parkinson's disease and generalized epilepsies**|通过皮质丘脑基底神经节（CTBG）系统的神经场模型，联合探讨了帕金森病（PD）和全身性癫痫的病理同步神经振荡的机制。基底神经节（BG）被近似为一个单一的有效群体，并分析了它们在调节振荡皮质丘脑（CT）动力学中的作用，反之亦然。除了正常的脑电图节律外，模型中还存在4 Hz和20 Hz左右的增强活动，这与PD的特征频率一致。这些节律是由BG和CT人群之间回路中的共振引起的，类似于先前CT模型中潜在的癫痫振荡。多巴胺耗竭被认为削弱了对PD中这些共振的抑制，网络连接解释了在4-8Hz和20Hz左右BG、丘脑和皮层活动之间的显著一致性。丘脑网状核（TRN）和BG的传入和传出连接位点之间的相似性预测低多巴胺对应于强直-阵挛（大发作）癫痫发作的可能性降低，这与实验结果一致。此外，该模型预测，与实验结果相匹配的低多巴胺水平会增加缺席（轻微）癫痫发作的可能性。与其他CTBG建模研究一致，当传入和传出BG与CT系统的连接增强时，表现出对缺席发作活动的抑制。BG被证明在强直-阵挛发作状态附近抑制CTBG系统的活性，从而深入了解BG回路中目前治疗的疗效。TRN的睡眠状态也被发现可以抑制病理性PD活动匹配观察。总的来说，这些发现证明了广泛性癫痫和帕金森病的相干振荡之间有很强的相似性，并为可能的合并症提供了见解。 et.al.|[2401.13467](http://arxiv.org/abs/2401.13467)|null|
|**2024-01-17**|**Reproducibility via neural fields of visual illusions induced by localized stimuli**|本文研究了Billock和Tsou[PNAS，2007]使用Amari型神经场的可控性对初级视皮层（V1）的皮层活动进行建模的实验复制，重点关注中央凹或外周视野中的规则漏斗模式。其目的是理解和模拟在这些实验中观察到的视觉现象，强调其非线性性质。这项研究包括设计模拟Billock和Tsou实验中视觉刺激的感官输入。然后从理论和数值上研究这些输入引起的后图像，以确定它们复制实验观察到的视觉效果的能力。这项研究的一个关键方面是研究神经反应的非线性性质所引起的影响。特别是，通过强调兴奋性和抑制性神经元在某些视觉现象出现中的重要性，这项研究表明，这两种类型的神经元活动的相互作用在视觉过程中发挥着重要作用，挑战了后者主要由兴奋性活动单独驱动的假设。 et.al.|[2401.09108](http://arxiv.org/abs/2401.09108)|null|
|**2024-01-12**|**Motion2VecSets: 4D Latent Vector Set Diffusion for Non-rigid Shape Reconstruction and Tracking**|我们介绍了Motion2VecSets，这是一种用于从点云序列进行动态曲面重建的4D扩散模型。虽然现有的最先进的方法已经证明在使用神经场表示重建非刚性对象方面取得了成功，但传统的前馈网络遇到了来自噪声、部分或稀疏点云的模糊观测的挑战。为了应对这些挑战，我们引入了一种扩散模型，该模型通过压缩潜在表示的迭代去噪过程来显式学习非刚性对象的形状和运动分布。当处理模糊输入时，基于扩散的先验能够进行更合理和概率的重建。我们用潜在向量集参数化4D动力学，而不是使用全局潜在。这种新颖的4D表示使我们能够学习局部表面形状和变形模式，从而实现更准确的非线性运动捕捉，并显著提高对看不见的运动和身份的可推广性。对于更具时间连贯性的目标跟踪，我们同步地对变形潜集进行去噪，并在多个帧之间交换信息。为了避免计算开销，我们设计了一个交错的空间和时间注意力块，以沿着空间和时间域交替聚集变形潜伏期。与最先进的方法进行了广泛的比较，证明了我们的Motion2VenSets在从各种不完美的观测进行4D重建方面的优势，特别是在从DeformingThings4D Animals数据集上的稀疏点云重建看不见的个体方面，与CaDex相比，交集优于并集（IoU）提高了19%。更多详细信息，请访问https://vveicao.github.io/projects/Motion2VecSets/. et.al.|[2401.06614](http://arxiv.org/abs/2401.06614)|null|
|**2024-01-05**|**Denoising Vision Transformers**|我们深入研究了视觉转换器（ViTs）固有的一个细微但重大的挑战：这些模型的特征图显示出网格状的伪影，这对ViTs在下游任务中的性能造成了不利影响。我们的研究将这个基本问题追溯到输入阶段的位置嵌入。为了解决这一问题，我们提出了一种新的噪声模型，该模型普遍适用于所有的ViT。具体来说，噪声模型将ViT输出分解为三个部分：一个没有噪声伪影的语义术语和两个以像素位置为条件的伪影相关术语。这种分解是通过在每幅图像的基础上加强与神经场的交叉视图特征一致性来实现的。这种逐图像优化过程从原始ViT输出中提取无伪影特征，为离线应用程序提供干净的特征。扩大了我们的解决方案的范围，以支持在线功能，我们引入了一种可学习的去噪器，直接从未处理的ViT输出中预测无伪影特征，这显示出对新数据的显著泛化能力，而无需对每张图像进行优化。我们的两阶段方法，称为去噪视觉转换器（DVT），不需要重新训练现有的预先训练的ViT，并且立即适用于任何基于转换器的架构。我们在各种具有代表性的ViT（DINO、MAE、DeiT III、EVA02、CLIP、DINOv2、DINOv2-reg）上评估了我们的方法。广泛的评估表明，我们的DVT在多个数据集（例如+3.84mIoU）的语义和几何任务中持续显著地改进了现有的最先进的通用模型。我们希望我们的研究将鼓励对ViT设计进行重新评估，特别是关于位置嵌入的天真使用。 et.al.|[2401.02957](http://arxiv.org/abs/2401.02957)|null|
|**2023-12-30**|**PlanarNeRF: Online Learning of Planar Primitives with Neural Radiance Fields**|从视觉数据中识别空间完整的平面基元是计算机视觉中的一项关键任务。现有的方法在很大程度上局限于2D片段恢复或简化3D结构，即使具有广泛的平面注释。我们提出了PlanarNeRF，这是一种能够通过在线学习检测密集3D平面的新框架。PlanarNeRF利用神经场表示，带来了三个主要贡献。首先，它利用并行的外观和几何知识增强了三维平面检测。其次，提出了一种轻量级的平面拟合模块来估计平面参数。第三，引入了一种具有更新机制的新的全局内存库结构，确保了跨帧一致性。PlanarNeRF的灵活架构使其能够在二维监督和自监督解决方案中发挥作用，在每种解决方案中，它都可以有效地从稀疏的训练信号中学习，显著提高训练效率。通过广泛的实验，我们证明了PlanarNeRF在各种场景下的有效性，并比现有工作有了显著的改进。 et.al.|[2401.00871](http://arxiv.org/abs/2401.00871)|null|
|**2024-01-01**|**Deblurring 3D Gaussian Splatting**|最近对辐射场的研究为具有照片级真实感渲染质量的新颖视图合成铺平了坚实的道路。然而，它们通常使用神经网络和体积绘制，这两种方法的训练成本很高，并且由于绘制时间长，阻碍了它们在各种实时应用中的广泛使用。最近，人们提出了一种基于3D高斯散射的方法来对3D场景进行建模，并在实时渲染图像的同时实现了显著的视觉质量。然而，如果训练图像模糊，则渲染质量会严重下降。模糊通常是由于镜头散焦、物体运动和相机抖动而产生的，它不可避免地会干扰干净图像的获取。先前的几项研究试图使用神经场从模糊的输入图像中渲染干净清晰的图像。然而，这些工作中的大多数仅设计用于基于体积渲染的神经辐射场，并不直接适用于基于光栅化的3D高斯散射方法。因此，我们提出了一种新的实时去模糊框架，即去模糊3D高斯散点，使用小型多层感知器（MLP）来操纵每个3D高斯的协方差来对场景模糊度进行建模。虽然去模糊的3D高斯飞溅仍然可以享受实时渲染，但它可以从模糊的图像中重建精细和清晰的细节。在基准上进行了各种实验，结果表明了我们的去模糊方法的有效性。定性结果可在https://benhenryl.github.io/Deblurring-3D-Gaussian-Splatting/ et.al.|[2401.00834](http://arxiv.org/abs/2401.00834)|null|
|**2023-12-22**|**Fluid Simulation on Neural Flow Maps**|我们介绍了神经流图，这是一种新的模拟方法，将新兴的隐式神经表示范式与基于流图理论的流体模拟相结合，以实现最先进的无粘流体现象模拟。我们设计了一种新的混合神经场表示，空间稀疏神经场（SSNF），它将小型神经网络与重叠、多分辨率和空间稀疏网格的金字塔相融合，以高精度紧凑地表示长期时空速度场。有了这个神经速度缓冲器，我们以机械对称的方式计算长期双向流图及其雅可比矩阵，以促进对现有解决方案的大幅精度提高。这些长程双向流图实现了低耗散的高平流精度，进而促进了高保真度的不可压缩流模拟，显示了复杂的旋涡结构。我们展示了我们的神经流体模拟在各种具有挑战性的模拟场景中的有效性，包括跳跃涡流、碰撞涡流、涡流重新连接，以及移动障碍物和密度差异产生的涡流。我们的例子表明，在能量守恒、视觉复杂性、对实验观测的遵守以及详细旋涡结构的保存方面，与现有方法相比，性能有所提高。 et.al.|[2312.14635](http://arxiv.org/abs/2312.14635)|null|
|**2023-12-21**|**Geometric Awareness in Neural Fields for 3D Human Registration**|将模板与三维人体点云对齐是一个长期存在的问题，对于动画、重建和启用监督学习管道等任务至关重要。最近的数据驱动方法利用了预测的表面对应关系；然而，它们对不同的姿态或分布并不鲁棒。相比之下，工业解决方案往往依赖于昂贵的手动注释或多视图捕获系统。最近，神经场已经显示出有希望的结果，但它们纯粹的数据驱动性质缺乏几何意识，通常导致模板配准的微小错位。在这项工作中，我们提出了两种解决方案：LoVD，一种新的神经场模型，它预测朝向目标表面上的局部SMPL顶点的方向；和INT，这是第一个专门用于神经领域的自监督任务，在测试时，它利用目标几何结构来细化主干。我们将它们组合到INLoVD中，这是一个在大型MoCap数据集上训练的强大的3D人体注册管道。INLoVD是高效的（不到一分钟），在公共基准上稳定地达到了最先进的水平，并对分布外的数据提供了前所未有的概括。我们将在\url｛url｝中发布代码和检查点。 et.al.|[2312.14024](http://arxiv.org/abs/2312.14024)|null|

<p align=right>(<a href=#updated-on-20240129>back to top</a>)</p>

[contributors-shield]: https://img.shields.io/github/contributors/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[contributors-url]: https://github.com/Vincentqyw/cv-arxiv-daily/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[forks-url]: https://github.com/Vincentqyw/cv-arxiv-daily/network/members
[stars-shield]: https://img.shields.io/github/stars/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[stars-url]: https://github.com/Vincentqyw/cv-arxiv-daily/stargazers
[issues-shield]: https://img.shields.io/github/issues/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[issues-url]: https://github.com/Vincentqyw/cv-arxiv-daily/issues

