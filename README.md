[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]

## Updated on 2024.01.31
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
|**2024-01-27**|**Gaussian Splashing: Dynamic Fluid Synthesis with Gaussian Splatting**|我们展示了将基于物理的固体和流体动画与3D高斯飞溅（3DGS）相结合的可行性，以在使用3DGS重建的虚拟场景中创建新的效果。利用底层表示中高斯飞溅和基于位置的动力学（PBD）的一致性，我们以内聚的方式管理渲染、视图合成以及固体和流体的动力学。与高斯着色器类似，我们使用添加的法线增强每个高斯内核，将内核的方向与曲面法线对齐，以优化PBD模拟。这种方法有效地消除了由固体中的旋转变形引起的尖锐噪声。它还允许我们集成基于物理的渲染，以增强流体上的动态曲面反射。因此，我们的框架能够真实地再现动态流体上的曲面高光，并促进场景对象和新视图中流体之间的交互。有关更多信息，请访问我们的项目页面\url{https://amysteriouscat.github.io/GaussianSplashing/}. et.al.|[2401.15318](http://arxiv.org/abs/2401.15318)|null|
|**2024-01-26**|**3D Reconstruction and New View Synthesis of Indoor Environments based on a Dual Neural Radiance Field**|同时实现室内环境的3D重建和新视图合成具有广泛的应用，但在技术上非常具有挑战性。基于隐式神经函数的现有技术方法可以获得极好的三维重建结果，但它们在新视图合成方面的性能可能不令人满意。神经辐射场（NeRF）的令人兴奋的发展彻底改变了新的视图合成，然而，基于NeRF的模型可能无法重建干净的几何表面。我们开发了一种双神经辐射场（Du-NeRF），以同时实现高质量的几何重建和视图渲染。Du-NeRF包含两个几何场，一个从SDF场导出以便于几何重建，另一个从密度场导出以促进新视图合成。Du NeRF的一个创新特征是，它将视图无关分量与密度场解耦，并将其用作标签来监督SDF场的学习过程。这减少了形状辐射模糊性，并使几何图形和颜色在学习过程中相互受益。大量实验表明，Du-NeRF可以显著提高室内环境下新视图合成和3D重建的性能，并且在构建包含不服从多视图颜色一致性的精细几何图形的区域时尤其有效。 et.al.|[2401.14726](http://arxiv.org/abs/2401.14726)|null|
|**2024-01-23**|**IRIS: Inverse Rendering of Indoor Scenes from Low Dynamic Range Images**|尽管许多3D重建和新颖的视图合成方法允许从消费者相机轻松捕捉的多视图图像中真实地渲染场景，但它们在表示中烘焙照明，无法支持高级应用程序，如材质编辑、重新照明和虚拟对象插入。通过反向渲染重建基于物理的材料特性和照明有望实现此类应用。然而，大多数反向渲染技术都需要高动态范围（HDR）图像作为输入，这是大多数用户无法访问的设置。我们提出了一种方法，从多视图、低动态范围（LDR）图像中恢复场景的基于物理的材料特性和空间变化的HDR照明。我们在反向渲染管道中对LDR图像形成过程进行建模，并提出了一种新的材料、照明和相机响应模型的优化策略。与采用LDR或HDR输入的最先进的反向渲染方法相比，我们使用合成场景和真实场景来评估我们的方法。我们的方法优于以LDR图像作为输入的现有方法，并允许高度逼真的重新照明和对象插入。 et.al.|[2401.12977](http://arxiv.org/abs/2401.12977)|null|
|**2024-01-24**|**RGBD Objects in the Wild: Scaling Real-World 3D Object Learning from RGB-D Videos**|我们介绍了一种新的在野外捕获的RGB-D对象数据集，称为WildRGB-D。与大多数现有的仅带有RGB捕获的以对象为中心的真实世界数据集不同，深度通道的直接捕获允许更好的3D注释和更广泛的下游应用。WildRGB-D包括大型类别级RGB-D对象视频，这些视频是用iPhone 360度环绕对象拍摄的。它包含大约8500个记录对象和近20000个RGB-D视频，涉及46个常见对象类别。这些视频是在三种设置的不同杂乱背景下拍摄的，以覆盖尽可能多的真实世界场景：（i）一个视频中的单个对象；（ii）一个视频中的多个对象；以及（iii）在一个视频中具有静止手的对象。该数据集由对象遮罩、真实世界比例的相机姿态和RGBD视频中重建的聚合点云进行注释。我们用WildRGB-D对四个任务进行了基准测试，包括新颖的视图合成、相机姿态估计、物体6d姿态估计和物体表面重建。我们的实验表明，RGB-D对象的大规模捕获为推进3D对象学习提供了巨大的潜力。我们的项目页面是https://wildrgbd.github.io/. et.al.|[2401.12592](http://arxiv.org/abs/2401.12592)|null|
|**2024-01-23**|**Methods and strategies for improving the novel view synthesis quality of neural radiation field**|神经辐射场（NeRF）技术可以从2D图像中学习场景的3D隐式模型，并合成逼真的新视图图像。该技术得到了业界的广泛关注，具有良好的应用前景。针对NeRF图像渲染质量需要提高的问题，近三年来，许多研究人员提出了各种方法来提高渲染质量。对最新的相关论文进行了分类和综述，分析了质量改进背后的技术原理，并讨论了质量改进方法的未来发展方向。这项研究可以帮助研究人员快速了解该领域技术的现状和发展脉络，有助于激发更高效算法的发展，促进NeRF技术在相关领域的应用。 et.al.|[2401.12451](http://arxiv.org/abs/2401.12451)|null|
|**2024-01-22**|**HG3-NeRF: Hierarchical Geometric, Semantic, and Photometric Guided Neural Radiance Fields for Sparse View Inputs**|神经辐射场（NeRF）作为一种通过从离散观测中学习场景表示的新型视图合成范式，已经引起了人们的极大关注。然而，当面对稀疏视图输入时，NeRF表现出明显的性能退化，从而限制了其进一步的适用性。在这项工作中，我们介绍了层次几何、语义和光度引导的NeRF（HG3-NeRF），这是一种新的方法，可以解决上述限制，并增强不同视图中几何、语义内容和外观的一致性。我们提出了分层几何制导（HGG），将运动结构的附加（SfM），即稀疏深度先验，纳入场景表示中。与直接深度监督不同，HGG从局部几何区域到全局几何区域对体积点进行采样，减轻了深度先验中固有偏差引起的偏差。此外，我们从不同分辨率的图像中观察到的语义一致性的显著变化中获得了灵感，并提出了层次语义引导（HSG）来学习粗到细的语义内容，该内容对应于粗到细场景表示。实验结果表明，HG3-NeRF可以在不同的标准基准上优于其他最先进的方法，并实现稀疏视图输入的高保真度合成结果。 et.al.|[2401.11711](http://arxiv.org/abs/2401.11711)|null|
|**2024-01-18**|**Explaining the Implicit Neural Canvas: Connecting Pixels to Neurons by Tracing their Contributions**|隐式神经表示（INRs）的许多变体，其中神经网络被训练为信号的连续表示，对于下游任务具有巨大的实用性，包括新颖的视图合成、视频压缩和图像超分辨率。不幸的是，对这些网络的内部运作方式的研究严重不足。我们的工作，即解释隐式神经画布（XINC），是一个统一的框架，用于通过检查每个神经元对每个输出像素的贡献强度来解释INRs的特性。我们将这些贡献图的集合称为隐式神经画布，并使用这一概念来证明我们研究的INR学会了以令人惊讶的方式“观察”它们所代表的帧。例如，INR往往具有高度分布的表示。虽然缺乏高级对象语义，但它们对颜色和边缘有很大的偏见，而且几乎完全是空间不可知的。我们通过研究视频INR中对象在时间上的表现方式得出了我们的结论，使用聚类来可视化跨层和架构的相似神经元，并表明这是由运动主导的。这些见解证明了我们的分析框架的普遍有用性。我们的项目页面位于https://namithap10.github.io/xinc. et.al.|[2401.10217](http://arxiv.org/abs/2401.10217)|null|
|**2024-01-18**|**GPAvatar: Generalizable and Precise Head Avatar from Image(s)**|头部化身重建对于虚拟现实、在线会议、游戏和电影行业的应用至关重要，在计算机视觉界引起了极大的关注。该领域的基本目标是忠实地再现头部化身，并精确地控制表情和姿势。现有的方法分为基于2D的扭曲、基于网格和神经渲染方法，在保持多视图一致性、结合非面部信息和推广到新身份方面存在挑战。在本文中，我们提出了一个名为GPAvatar的框架，该框架可以在单个前向通道中从一个或多个图像重建3D头部化身。这项工作的关键思想是引入一个由点云驱动的动态基于点的表情场，以精确有效地捕捉表情。此外，我们在三平面规范场中使用多三平面注意力（MTA）融合模块来利用来自多个输入图像的信息。所提出的方法实现了忠实的身份重建、精确的表达控制和多视图一致性，在自由视点渲染和新颖视图合成方面显示了良好的效果。 et.al.|[2401.10215](http://arxiv.org/abs/2401.10215)|**[link](https://github.com/xg-chu/gpavatar)**|
|**2024-01-17**|**Objects With Lighting: A Real-World Dataset for Evaluating Reconstruction and Rendering for Object Relighting**|从照片中重建对象并将其虚拟地放置在新环境中超出了标准的新颖视图合成任务，因为对象的外观不仅要适应新颖的视点，还要适应新的照明条件，而且反向渲染方法的评估依赖于新颖的视图合成数据或用于定量分析的简单合成数据集。这项工作提供了一个真实世界的数据集，用于测量重新照明对象的重建和渲染。为此，我们捕获了多个环境中相同对象的环境照明和地面实况图像，从而可以从一个环境中拍摄的图像中重建对象，并量化看不见的照明环境的渲染视图的质量。此外，我们介绍了一个由现成方法组成的简单基线，并在重新照明任务中测试了几种最先进的方法，表明新的视图合成不是衡量性能的可靠指标。代码和数据集可在https://github.com/isl-org/objects-with-lighting . et.al.|[2401.09126](http://arxiv.org/abs/2401.09126)|**[link](https://github.com/isl-org/objects-with-lighting)**|
|**2024-01-17**|**ICON: Incremental CONfidence for Joint Pose and Radiance Field Optimization**|在给定一组2D图像的情况下，神经辐射场（NeRF）在新视图合成（NVS）中表现出显著的性能。然而，NeRF训练需要每个输入视图的精确相机姿势，通常通过运动结构（SfM）管道获得。最近的作品试图放松这种限制，但它们仍然经常依赖于可以改进的体面的初始姿势。在这里，我们旨在消除姿势初始化的要求。我们提出了增量置信（ICON），这是一种从2D视频帧中训练NeRF的优化过程。ICON仅假设相机运动平滑，以估计姿势的初始猜测。此外，ICON引入了“置信度”：一种用于动态重加权梯度的模型质量自适应度量。ICON依赖于高置信度姿势来学习NeRF，并依赖于高置信度3D结构（由NeRF编码）来学习姿势。我们表明，与使用SfM姿势的方法相比，ICON在没有预先初始化姿势的情况下，在CO3D和HO3D中都实现了卓越的性能。 et.al.|[2401.08937](http://arxiv.org/abs/2401.08937)|null|

<p align=right>(<a href=#updated-on-20240131>back to top</a>)</p>

## 3D Reconstruction

|Publish Date|Title|Abstract|PDF|Code|
|---|---|---|---|---|
|**2024-01-30**|**Self-Supervised Representation Learning for Nerve Fiber Distribution Patterns in 3D-PLI**|要全面了解人脑的组织原理，除其他因素外，还需要对神经纤维结构进行可量化的描述。三维偏振光成像（3D-PLI）是一种显微镜成像技术，能够以高分辨率深入了解有髓神经纤维的细粒度组织。表征在3D-PLI中观察到的纤维结构的描述符将实现下游分析任务，如多模式相关性研究、聚类和映射。然而，在3D-PLI中对光纤结构进行独立于观察者的表征的最佳实践尚不可用。为此，我们提出应用一种完全数据驱动的方法，使用自监督表示学习来表征3D-PLI图像中的神经纤维结构。我们介绍了一种3D上下文对比学习（CL-3D）目标，该目标利用3D重建体积的组织学脑切片中纹理示例的空间邻域来对正配对进行采样以进行对比学习。我们将这种采样策略与专门设计的图像增强相结合，以获得对3D-PLI参数图中典型变化的鲁棒性。该方法已在一只vervet猴子大脑的3D重建枕叶中进行了演示。我们发现，提取的特征对神经纤维的不同配置高度敏感，但对组织学处理引起的连续脑切片之间的变化很强。我们展示了它们在检索同质光纤架构的集群和对光纤架构的特定组件（如U型光纤）的交互式选择模板执行数据挖掘方面的实际适用性。 et.al.|[2401.17207](http://arxiv.org/abs/2401.17207)|null|
|**2024-01-30**|**Physical Priors Augmented Event-Based 3D Reconstruction**|三维神经隐式表示在许多机器人应用中起着重要的作用。然而，当只有事件流可用时，由于稀疏性和信息缺乏，从真实的事件数据重建神经辐射场（NeRF）仍然是一个挑战。在本文中，我们利用事件数据背后的运动、几何和密度先验来施加强大的物理约束，以增强NeRF训练。所提出的新型流水线可以直接受益于这些先验，以在没有额外输入的情况下重建3D场景。此外，我们提出了一种新的基于密度引导的基于补丁的采样策略，用于鲁棒和高效的学习，它不仅加速了训练过程，而且有助于局部几何的表达。更重要的是，我们建立了第一个用于基于事件的3D重建的大型数据集，其中包含101个具有各种材料和几何形状的对象，以及所有相机视点的图像和深度图的基本情况，这大大促进了相关领域的其他研究。代码和数据集将在https://github.com/Mercerai/PAEv3d. et.al.|[2401.17121](http://arxiv.org/abs/2401.17121)|null|
|**2024-01-30**|**OmniSCV: An Omnidirectional Synthetic Image Generator for Computer Vision**|全方位和360度图像在工业和消费社会中越来越普遍，引起了全方位计算机视觉的关注。它们的宽视场允许仅从图像中收集大量关于环境的信息。然而，这些图像的失真需要开发特定的算法来进行处理和解释。此外，大量的图像对于基于学习的计算机视觉算法的正确训练是必不可少的。在本文中，我们提出了一种用于生成具有语义和深度信息的全向图像数据集的工具。这些图像是从在虚幻引擎4的真实虚拟环境中通过接口插件获取的一组捕获中合成的。我们收集了各种著名的投影模型，如等矩形和圆柱形全景图、不同的鱼眼透镜、折反射系统和经验模型。此外，在我们的工具中，我们将真实感非中心投影系统包括为非中心全景和非中心折反射系统。据我们所知，这是文献中第一个报道的生成真实感非中心图像的工具。此外，由于全向图像是虚拟制作的，我们提供了关于语义和深度的像素信息，以及相机校准参数的完美知识。这允许创建具有像素精度的地面实况信息，用于训练学习算法和测试3D视觉方法。为了验证所提出的工具，测试了不同的计算机视觉算法，如从屈光和折反射中心图像中提取线，使用等矩形全景进行3D布局恢复和SLAM，以及从非中心全景进行3D重建。 et.al.|[2401.17061](http://arxiv.org/abs/2401.17061)|**[link](https://github.com/sbrunoberenguel/omniscv)**|
|**2024-01-29**|**SuNeRF: 3D reconstruction of the solar EUV corona using Neural Radiance Fields**|为了了解其演变及其喷发事件的影响，太阳受到多个卫星任务的永久监测。太阳等离子体的光学薄发射和有限的视点数量使得重建太阳大气的几何形状和结构具有挑战性；然而，这些信息是理解太阳的缺失环节：一颗三维演化的恒星。我们提出了一种方法，能够在极紫外（EUV）光中观察到最上层太阳层（日冕）的完整3D表示。我们使用深度学习方法进行三维场景表示，考虑到辐射传输，通过三次同时观测绘制整个太阳大气层的地图。我们证明，我们的方法提供了前所未有的太阳极重建，并直接实现了对日冕结构、太阳丝、日冕空洞轮廓和日冕物质抛射的高度估计。我们使用模型生成的合成EUV图像验证了该方法，发现我们的方法即使从有限的32个黄道视点（ $|\text｛latitude｝|\leq 7^\circ$ ）也能准确地捕捉到太阳的3D几何结构。我们使用集成方法量化模型的不确定性，该方法允许我们在缺乏基本事实的情况下估计模型性能。我们的方法能够对我们最近的恒星进行新的观察，是有效利用多仪器数据集的突破性技术，为未来的集群任务铺平了道路。 et.al.|[2401.16388](http://arxiv.org/abs/2401.16388)|null|
|**2024-01-29**|**Reconstructing Close Human Interactions from Multiple Views**|本文解决了一项具有挑战性的任务，即重建由多台校准相机拍摄的参与亲密互动的多个人的姿势。困难源于由于人与人之间的遮挡而导致的噪声或错误的2D关键点检测、由于密切的交互而导致的将关键点与个体相关联的严重模糊性以及训练数据的稀缺性，因为在拥挤的场景中收集和注释运动数据是资源密集型的。我们引入了一种新颖的系统来应对这些挑战。我们的系统集成了一个基于学习的姿态估计组件及其相应的训练和推理策略。姿态估计组件采用多视图2D关键点热图作为输入，并使用3D条件体积网络重建每个个体的姿态。由于网络不需要图像作为输入，我们可以利用测试场景中的已知相机参数和大量现有的运动捕捉数据来合成模拟测试场景中真实数据分布的大量训练数据。大量实验表明，我们的方法在姿态精度方面显著优于以前的方法，并且可以在各种相机设置和人群规模中推广。代码可在我们的项目页面上获得：https://github.com/zju3dv/CloseMoCap. et.al.|[2401.16173](http://arxiv.org/abs/2401.16173)|null|
|**2024-01-29**|**Domain adaptation strategies for 3D reconstruction of the lumbar spine using real fluoroscopy data**|这项研究解决了在骨科手术中采用手术导航的关键障碍，包括时间、成本、辐射和工作流程集成方面的挑战。最近，我们的工作X23D展示了一种仅从少数术中荧光透视图像生成脊柱三维解剖模型的方法。这通过创建解剖结构的直接术中3D重建来否定了对传统的基于配准的外科导航的需要。尽管取得了这些进步，但X23D的实际应用受到合成训练数据和真实术中图像之间的领域差距的限制。作为回应，我们为配对数据集设计了一种新的数据收集协议，该数据集由来自相同视角的合成和真实荧光透视图像组成。利用这个数据集，我们通过迁移学习完善了我们的深度学习模型，有效地弥合了合成和真实X射线数据之间的领域差距。一种新型的传输机制还允许我们转换真实的X射线以反映合成域，使我们的计算机训练X23D模型能够在现实世界中实现高精度。我们的研究结果表明，精确的模型可以通过三次术中荧光镜检查快速生成整个腰椎的精确3D重建。它获得了84%的F1分数，与我们之前基于合成数据的研究的准确性相匹配。此外，由于计算时间仅为81.1ms，我们的方法提供了手术集成所必需的实时功能。通过检查理想的成像设置和视角相关性，我们进一步证实了我们的系统在临床环境中的实用性和可靠性。我们的研究标志着术中3D重建向前迈出了重要一步，增强了手术计划、导航和机器人技术。 et.al.|[2401.16027](http://arxiv.org/abs/2401.16027)|null|
|**2024-01-29**|**2L3: Lifting Imperfect Generated 2D Images into Accurate 3D**|从单个图像重建3D对象是一个有趣但具有挑战性的问题。一个有前途的解决方案是利用多视图（MV）3D重建将生成的MV图像融合成一致的3D对象。然而，生成的图像通常存在照明不一致、几何体错位和视图稀疏的问题，导致重建质量较差。为了解决这些问题，我们提出了一种新的3D重建框架，该框架利用固有分解引导、瞬态单先验引导和视图增强来分别解决这三个问题。具体来说，我们首先利用阴影信息从生成的图像中解耦，以减少不一致照明的影响；然后，我们引入了具有视点相关瞬态编码的单声道先验来增强重构的法线；最后，我们设计了一种视图增强融合策略，最大限度地减少生成的稀疏视图中的像素级损失和增强的随机视图中的语义损失，从而获得视图一致的几何结构和详细的纹理。因此，我们的方法能够集成预先训练的MV图像生成器和基于神经网络的体积有符号距离函数（SDF）表示，用于单个图像到3D对象的重建。我们在各种数据集上评估了我们的框架，并证明了其在定量和定性评估中的卓越性能，这意味着3D对象重建方面取得了重大进展。与最新的同步梦想家方法相比，我们将倒角距离误差降低了约36%，PSNR提高了约30%。 et.al.|[2401.15841](http://arxiv.org/abs/2401.15841)|null|
|**2024-01-28**|**One for all: A novel Dual-space Co-training baseline for Large-scale Multi-View Clustering**|本文提出了一种新的多视图聚类模型，称为双空间协同训练大规模多视图聚类（DSCMC）。我们方法的主要目标是通过在两个不同的空间中利用联合训练来提高集群性能。在原始空间中，我们学习一个投影矩阵，以获得来自不同视图的潜在一致锚图。这个过程包括捕捉每个视图中数据点之间的固有关系和结构。同时，我们使用特征转换矩阵将来自不同视图的样本映射到共享的潜在空间。这种转换有助于从多个视图调整信息，从而能够全面了解底层数据分布。我们共同优化潜在一致锚图的构建和特征变换，以生成判别锚图。该锚图有效地捕捉了多视图数据的基本特征，并作为后续聚类分析的可靠基础。此外，还提出了基于元素的方法，以避免不同视图之间不同信息的影响。我们的算法具有近似线性的计算复杂度，这保证了它在大规模数据集上的成功应用。通过实验验证，我们证明了与现有方法相比，我们的方法显著降低了计算复杂度，同时产生了优越的聚类性能。 et.al.|[2401.15691](http://arxiv.org/abs/2401.15691)|null|
|**2024-01-28**|**Multi-Person 3D Pose Estimation from Multi-View Uncalibrated Depth Cameras**|我们从有限数量的未校准深度相机中处理多视图、多人3D人体姿态估计的任务。最近，已经提出了许多从多视图RGB相机进行3D人体姿态估计的方法。然而，这些工作（1）假设RGB相机视图的数量足够大以用于3D重建，（2）相机被校准，以及（3）依赖于真实的3D姿态来训练其回归模型。在这项工作中，我们建议利用提供RGBD视频流的稀疏、未校准的深度相机进行3D人体姿态估计。我们提出了一种用于多视图深度人体姿态估计（MVD-HPE）的简单管道，用于在不训练深度3D人体姿态回归模型的情况下联合预测相机姿态和3D人体姿态。与仅使用RGB特征相比，该框架利用来自RGBD图像的3D Re-ID外观特征来制定更准确的对应关系（用于推导相机位置）。我们进一步提出（1）通过利用3D刚性变换作为引导来进行深度引导的相机姿态估计，以及（2）通过利用深度投影的3D点作为优化的替代目标来进行深度约束的3D人体姿态估计。为了评估我们提出的管道，我们收集了从多个稀疏视图深度相机记录的RGBD视频的三个视频集，并手动注释了地面实况3D姿态。实验表明，我们提出的方法在相机姿态估计和三维人体姿态估计方面都优于当前的无三维人体姿态回归管道。 et.al.|[2401.15616](http://arxiv.org/abs/2401.15616)|null|
|**2024-01-26**|**Straight versus Spongy -- Effect of Tortuosity on Polymer Imbibition into Nanoporous Matrices Assessed by Segmentation-Free Analysis of 3D Sample Reconstructions**|通过X射线计算机断层扫描和EDX光谱，我们比较分析了聚苯乙烯（PS）在两个互补孔模型中的吸胀作用，这两个模型具有约380nm的孔径和羟基封端的无机氧化物孔壁，即可控多孔玻璃（CPG）和自有序多孔氧化铝（AAO）。CPG包含连续的海绵状曲折孔隙系统。包含孤立直圆柱形孔隙阵列的AAO是具有接近1的弯曲度的参考孔隙模型。时空自吸前沿演化的比较评估产生了关于被探测的弯曲基质（如CPG）的孔隙形态和自吸机制的重要信息。为此，将渗透的AAO和CPG样品的断层摄影3D重建和2D EDX图中的像素亮度分散浓缩为垂直于膜表面的1D亮度分散轮廓。他们的统计分析得出了渗吸前沿的位置和宽度，而没有对孔隙位置进行分割或确定。吸收前沿运动相对于AAO参考样品的延迟可以用作测试多孔基质的弯曲度的描述符。CPG中自吸前缘运动的速度等于AAO中自吸锋运动速度的三分之二。此外，自吸前沿加宽的动力学揭示了多孔基质是由圆柱形颈状孔段主导还是由节点主导。圆柱形AAO孔中的独立单个弯月面运动导致比CPG更快的自吸前沿加宽，其中由节点主导的形态导致涉及几个弯月面的较慢的协同自吸前沿运动。 et.al.|[2401.14950](http://arxiv.org/abs/2401.14950)|null|

<p align=right>(<a href=#updated-on-20240131>back to top</a>)</p>

## Diffusion

|Publish Date|Title|Abstract|PDF|Code|
|---|---|---|---|---|
|**2024-01-30**|**Study of X-ray emission from the S147 nebula with SRG/eROSITA: X-ray imaging, spectral characterization and a multiwavelength picture**|Simeis 147（S147，G180.0-0.17，“意大利面星云”）是一种超新星遗迹，广泛研究了从无线电到GeV $\gamma$-射线的整个电磁波谱，但X射线除外。在这项研究中，我们报告了首次从整个SNR中检测到显著的X射线发射。在这里，以及在一篇配套论文中，我们使用俄罗斯-德国伦琴伽马射线望远镜（SRG）上的扩展伦琴巡天成像望远镜阵列（eROSITA）的数据，对S147星云的X射线发射进行了研究。该物体位于银河系的反中心，其3度的大小使其成为有史以来在X射线中探测到的最大SNR之一。总的来说，用eROSITA观察到的X射线发射形态完全限制在无线电同步加速器和H$\alpha$发射的边界内，除了遗迹的西部边缘，在那里，与X射线相比，无线电和H$\alpha$的发射似乎进一步向西部延伸。X射线发射主要是软的，在0.5-1.0keV之间具有强检测，使得S147在2.3keV以上未被检测到。X射线发射是纯热的，表现出强烈的O、Ne和Mg线，而它缺乏较重的Z元素。气体温度为$kT=0.22的非平衡碰撞等离子体模型^{-0.03}_｛+0.02｝$~keV，吸收柱密度为$N_\mathrm｛｛H｝｝＝0.30_｛-0.03｝^｛+0.04｝\cdot10^｛22｝~\mathrm{cm^｛-2｝}$（$\tau＝4.27^｛+1.87｝_｛-0.99｝~\ mathrm｛\cdot10^{10}s~cm^｛-3｝｝$）比具有$kT＝0.11\pm0.01$~keV和$N_\mathrm{｛H｝}＝0.51\pm0.02\cdot10^｛22｝~\mathrm｛cm^{-2｝}$的平衡碰撞等离子体模型更可取。通过使用$\sim$ 14.5年的费米LAT数据，我们的研究证实了残余物与空间一致的扩散GeV过剩的关联，即4FGL J0540.3+2756e或FGES J0537.6+2751。根据eROSITA的数据，还报告了残余物的年龄和距离估计。 et.al.|[2401.17312](http://arxiv.org/abs/2401.17312)|null|
|**2024-01-30**|**G321.3-3.9: a new supernova remnant observed with multi-band radio data and in the SRG/eROSITA All-Sky Surveys**|沿着银河平面探测超新星遗迹（SNR）可能相当具有挑战性。任何新的探测都会减少预期残余物数量与已知残余物数量之间的差异。在本文中，我们展示了覆盖G321.3-3.9位置的大量无线电和X射线数据的结果。我们使用几次无线电调查收集的数据，将G321.3-3.9确定为一种新的SNR，频率范围从200 MHz到2300 MHz。来自四次连续的全天巡天（eRASS:4）的叠加eROSITA数据提供了0.2-8.0 keV能带中的光谱成像信息。G321.3-3.9具有椭圆形状，长轴和短轴约为1.7°x 1.1°。根据CHIPASS和S-PASS数据，我们计算出光谱指数-0.8+-0.4，与Sedov-Taylor相膨胀壳层的同步辐射一致。eROSITA的数据显示，X射线散射结构几乎填满了整个无线电外壳。根据测试的光谱模型，可以拟合0.2keV（VAPEC）和0.7keV（NEI）之间的等离子体温度。X射线光谱分析使我们能够估计G321.3-3.9的柱吸收，通过与光学消光图的比较，这表明残余距离约为1kpc。 et.al.|[2401.17294](http://arxiv.org/abs/2401.17294)|null|
|**2024-01-30**|**Discovery of the Goat Horn complex: a $\sim 1000$ deg$^2$ diffuse X-ray source connected to radio loop XII**|在天空中的无线电频率上观察到十几个以相干和静止环的形式跨越数十度的偏振无线电发射斑块。它们的起源通常与附近的冲击有关，可能是由近距离超新星爆炸引起的。到目前为止，无线电回路XII的起源仍然未知。我们报道了回路XII的无线电极化发射与SRG/eROSITA在同一区域发现的超过背景表面亮度的大块软X射线发射的反相关性。超过背景发射的软X射线似乎相干的斑块，我们称之为山羊角复合体，延伸到$\sim 1000$deg$^2$ 的显著区域，并包括可能追踪冷锋的弧形增强。还观察到X射线强度与负责X射线发射的等离子体温度的反相关性。X射线亮弧似乎在一定程度上预测了天空中的无线电回路XII。这种行为可以根据X射线表面亮度和无线电去极化之间的相关性来重新定义。我们探索并讨论了山羊角复合体中扩散发射源的不同可能场景：一个大型超新星遗迹；从附近银河旋臂的活跃恒星形成区域流出；大麦哲伦星云周围的高温大气。为了进一步探索这些场景，需要对热气的速度进行更详细的表征。 et.al.|[2401.17291](http://arxiv.org/abs/2401.17291)|null|
|**2024-01-30**|**A new understanding of the Gemini-Monoceros X-ray enhancement from discoveries with eROSITA**|双子座单核星系的X射线增强是研究扩散X射线发射和超新星遗迹（SNR）的丰富领域。随着eROSITA于2019年在SRG平台上推出，我们现在能够全面研究这些来源。附近的许多SNR被怀疑是非常古老的残余物，由于许多观测挑战，X射线对其研究严重不足。此外，识别新的微弱的大型SNR可能有助于解决银河系SNR观测数量和预期数量之间长期存在的差异。我们对整个漫射结构进行了详细的X射线光谱分析，并对附近区域进行了详细背景分析。我们还利用多波长数据来更好地了解形态，并限制到不同来源的距离。我们估计了源的等离子体特性，并计算了模型SNR的网格，以确定单个SNR特性。单宝石环SNR的大多数扩散等离子体由单个非平衡电离（NEI）组分很好地描述，其平均温度为 $kT=0.14\pm 0.03$keV。我们获得的年龄为$\approxy 1.2\cdot 10^5$yr，与PSR B0656+14一致。在东南部，我们发现了更热的第二等离子体成分和可能的新SNR候选者的证据，其价格约为300美元/个，新候选者的年龄约为50000美元/年。我们还能够改进之前对更远的Monoceros Loop和PKS 0646+06 SNR的研究。我们获得的温度明显高于先前的研究，对于PKS 0646+06，SNR的估计年龄要低得多。我们还发现了一个新的SNR候选者G190.4+12.5，它很可能位于$D>1.5$kpc，在距离银河系平面很远的地方扩展到低密度介质中，估计年龄为40000-6000$ yr。 et.al.|[2401.17289](http://arxiv.org/abs/2401.17289)|null|
|**2024-01-30**|**Probing the physical properties of the IGM using SRG/eROSITA spectra from blazars**|大多数重子物质存在于星系间介质（IGM）中，这是一种主要由电离的氢和氦组成的扩散气体，充满了星系之间的空间。对这种环境的观测对于更好地理解这种环境中涉及的物理过程至关重要。我们使用首次eROSITA全天巡天（eRASS1）的blazar光谱对IGM吸收进行了分析，该巡天是在光谱伦琴伽马射线任务（SRG）和XMM牛顿X射线观测的船上进行的。首先，我们使用对数抛物线光谱模型拟合了连续谱，并固定了银河系的吸收。然后，我们包括了一个碰撞电离平衡模型，即｛\tt IONeq｝，以解释IGM吸收。柱密度 $N（｛\rm H｝）$和金属性（$Z$）被设置为自由参数。同时，吸收体的红移固定为blazar红移的一半，作为全视线吸收体的近似值。我们测量了SRG的147个源和XMM-Newton的10个源的IGM-$N（｛\rm-H｝）$。我们发现IGM-$N（｛\rm H｝）$和blazar红移之间有明显的趋势，其标度为$（1+z）^｛1.63\pm 0.12｝$。在$z＝0$处的平均氢密度为$N_｛0｝＝（2.75\pm 0.63）\乘以10^｛-7｝$cm$^｛-3｝$。红移范围内的平均温度为$\log（T/K）=5.6\pm 0.6$，而平均金属量为$Z=0.16\pm 0.09$ 。我们使用幂律模型对温度或金属量作为红移的函数没有发现可接受的拟合。这些结果表明IGM对blazar光谱中所见的总吸收有很大贡献。 et.al.|[2401.17283](http://arxiv.org/abs/2401.17283)|null|
|**2024-01-30**|**You Only Need One Step: Fast Super-Resolution with Stable Diffusion via Scale Distillation**|在本文中，我们介绍了YONOS-SR，这是一种新的基于稳定扩散的图像超分辨率方法，仅使用单个DDIM步骤即可获得最先进的结果。我们提出了一种新的规模蒸馏方法来训练我们的SR模型。我们不是直接在感兴趣的比例因子上训练我们的SR模型，而是从在较小的放大比例上训练教师模型开始，从而使SR问题对教师来说更简单。然后，我们在训练过程中以教师的预测为目标，训练一个放大倍率更高的学生模型。迭代地重复这个过程，直到我们达到最终模型的目标比例因子。我们的标度提取背后的原理是，教师通过以下方式帮助学生扩散模型训练：i）提供适合当前噪声水平的目标，而不是使用来自所有噪声水平的地面实况数据的相同目标；以及ii）提供准确的目标，因为教师有更简单的任务要解决。我们的经验表明，提取的模型显著优于直接针对高尺度训练的模型，特别是在推理过程中只需很少的步骤。拥有一个只需要一个步骤的强扩散模型，可以冻结U-Net并在其上微调解码器。我们表明，空间提取U-Net和微调解码器的组合优于只需要200个步骤的最先进方法。 et.al.|[2401.17258](http://arxiv.org/abs/2401.17258)|null|
|**2024-01-30**|**Stochastic motions of the two-dimensional many-body delta-Bose gas**|为了表示任意整数 $N\geq2$的二维$N$ 体delta玻色气体，我们构造了一个满足强Markov性质的It｛o｝扩散，并建立了一个相关的Feynman-Kac型公式。在几个性质中，扩散对于布朗运动是奇异的，因为它显示出粒子几乎肯定的接触，并且具有Ladyzhenskaya-Prodi-Serrin型条件意义上的超临界漂移系数。尽管存在超临界性，但通过局部变换两体相互作用中的相对运动和必要的自由运动，获得了Feynman-Kac型公式的扩散过程的构造和相关的分布性质。使这种减少为两体相互作用成为可能的中心机制是粒子的“无三重接触”，这在早期的二维delta玻色气体的函数积分中观察到，现在扩展到随机过程水平。 et.al.|[2401.17243](http://arxiv.org/abs/2401.17243)|null|
|**2024-01-30**|**ContactGen: Contact-Guided Interactive 3D Human Generation for Partners**|在人类之间的各种互动中，如眼神交流和手势，通过接触进行的身体互动可以成为理解人类行为的重要时刻。受这一事实的启发，给定一个具有所需交互标签的3D伙伴人类，我们引入了一项在身体接触方面生成3D人类的新任务。与以前与静态对象或场景交互的工作不同，给定的人类伙伴可以根据交互类型具有不同的姿势和不同的接触区域。为了应对这一挑战，我们提出了一种基于引导扩散框架为给定的伙伴人类生成交互式3D人类的新方法。具体而言，我们新提出了一种接触预测模块，该模块根据交互标签自适应地估计两个输入人类之间的潜在接触区域。使用估计的潜在接触区域作为补充指导，我们动态地强制ContactGen在引导扩散模型内为给定的伙伴人类生成交互式3D人类。我们在CHI3D数据集上演示了ContactGen，与比较方法相比，我们的方法生成了物理上合理且多样的姿势。 et.al.|[2401.17212](http://arxiv.org/abs/2401.17212)|null|
|**2024-01-30**|**Quantum dynamics in one and two dimensions via recursion method**|我们报告了递归方法的实现，该方法解决了非扰动状态下的量子多体动力学问题。该实现有两个关键组成部分：用于嵌套交换子符号计算的计算机代数例程和根据通用算子增长假设外推Lanczos系数序列的过程。我们将该方法应用于一维和二维晶格上自旋- $1/2$ 系统的无限温度相关函数的计算。在二维中，可访问的时间尺度足够大，基本上可以包含到平衡的松弛。该方法允许精确地计算传输系数。作为例子，我们计算了方晶格上横向场Ising模型的扩散常数。 et.al.|[2401.17211](http://arxiv.org/abs/2401.17211)|null|
|**2024-01-30**|**Transfer Learning for Text Diffusion Models**|在本报告中，我们探讨了文本扩散取代自回归（AR）解码用于大型语言模型（LLM）的训练和部署的潜力。我们特别感兴趣的是，通过我们称之为“AR2Diff”的轻量级自适应过程，是否可以将预训练的AR模型转换为文本扩散模型。我们首先为训练文本扩散模型建立一个强大的基线设置。通过在多个体系结构和预训练目标之间进行比较，我们发现在几个任务中，训练具有前缀LM目标的仅解码器模型是最好的或接近最好的。基于这一发现，我们测试了文本扩散模型的各种迁移学习设置。在机器翻译方面，我们发现文本扩散不如标准的AR方法。然而，在代码合成和提取QA方面，我们发现从头开始训练的扩散模型在许多情况下优于AR模型。我们还观察到AR2Diff的质量增益——将AR模型调整为使用扩散解码。这些结果是有希望的，因为文本扩散相对未被充分开发，并且对于长文本生成来说，可以明显快于AR解码。 et.al.|[2401.17181](http://arxiv.org/abs/2401.17181)|null|

<p align=right>(<a href=#updated-on-20240131>back to top</a>)</p>

## NeRF

|Publish Date|Title|Abstract|PDF|Code|
|---|---|---|---|---|
|**2024-01-30**|**BlockFusion: Expandable 3D Scene Generation using Latent Tri-plane Extrapolation**|我们介绍了BlockFusion，这是一种基于扩散的模型，它将3D场景生成为单元块，并无缝地合并新的块来扩展场景。BlockFusion使用从完整的3D场景网格中随机裁剪的3D块的数据集进行训练。通过逐块拟合，所有训练块都被转换为混合神经场：具有包含几何特征的三平面，然后是用于解码有符号距离值的多层感知器（MLP）。采用变分自动编码器将三平面压缩到潜在的三平面空间中，在该空间上进行去噪扩散处理。应用于潜在表示的扩散允许高质量和多样化的3D场景生成。要在生成过程中扩展场景，只需附加空块以与当前场景重叠，并外推现有的潜在三平面以填充新块。外推是通过在去噪迭代过程中使用来自重叠三平面的特征样本来调节生成过程来完成的。潜在的三平面外推法产生语义和几何上有意义的过渡，与现有场景和谐融合。2D布局调节机制用于控制场景元素的放置和布置。实验结果表明，BlockFusion能够在室内和室外场景中生成具有前所未有的高质量形状的多样化、几何一致和无边界的大型3D场景。 et.al.|[2401.17053](http://arxiv.org/abs/2401.17053)|null|
|**2024-01-26**|**Learning Neural Radiance Fields of Forest Structure for Scalable and Fine Monitoring**|这项工作利用神经辐射场和遥感技术用于林业应用。在这里，我们展示了神经辐射场为改进森林监测中现有的遥感方法提供了广泛的可能性。我们提出的实验证明了它们的潜力：（1）表达森林三维结构的精细特征，（2）融合可用的遥感模式，以及（3）改进三维结构衍生的森林指标。总之，这些特性使神经场成为一种有吸引力的计算工具，具有进一步提高森林监测程序的可扩展性和准确性的巨大潜力。 et.al.|[2401.15029](http://arxiv.org/abs/2401.15029)|null|
|**2024-01-25**|**Learning Robust Generalizable Radiance Field with Visibility and Feature Augmented Point Representation**|本文介绍了广义神经辐射场（NeRF）的一种新范式。以前的通用NeRF方法将多视点立体技术与基于图像的神经渲染相结合进行泛化，产生了令人印象深刻的结果，同时存在三个问题。首先，遮挡常常导致不一致的特征匹配。然后，由于采样点和粗略特征聚合的单独过程，它们在几何不连续性和局部尖锐形状中传递失真和伪影。第三，当源视图离目标视图不够近时，它们基于图像的表示会发生严重退化。为了应对挑战，我们提出了第一个基于点而不是基于图像的渲染构建可泛化神经场的范式，我们称之为可泛化神经点场（GPF）。我们的方法通过几何先验显式地建模可见性，并用神经特征增强它们。我们提出了一种新的非均匀对数采样策略，以提高渲染速度和重建质量。此外，我们提出了一种可学习的内核，该内核在空间上增加了用于特征聚合的特征，减轻了几何结构急剧变化的地方的失真。此外，我们的表现很容易被操纵。实验表明，在泛化和微调设置中，我们的模型可以在三个数据集上提供比所有对应模型和基准更好的几何结构、视图一致性和渲染质量，初步证明了可泛化NeRF新范式的潜力。 et.al.|[2401.14354](http://arxiv.org/abs/2401.14354)|null|
|**2024-01-24**|**Unified neural field theory of brain dynamics underlying oscillations in Parkinson's disease and generalized epilepsies**|通过皮质丘脑基底神经节（CTBG）系统的神经场模型，联合探讨了帕金森病（PD）和全身性癫痫的病理同步神经振荡的机制。基底神经节（BG）被近似为一个单一的有效群体，并分析了它们在调节振荡皮质丘脑（CT）动力学中的作用，反之亦然。除了正常的脑电图节律外，模型中还存在4 Hz和20 Hz左右的增强活动，这与PD的特征频率一致。这些节律是由BG和CT人群之间回路中的共振引起的，类似于先前CT模型中潜在的癫痫振荡。多巴胺耗竭被认为削弱了对PD中这些共振的抑制，网络连接解释了在4-8Hz和20Hz左右BG、丘脑和皮层活动之间的显著一致性。丘脑网状核（TRN）和BG的传入和传出连接位点之间的相似性预测低多巴胺对应于强直-阵挛（大发作）癫痫发作的可能性降低，这与实验结果一致。此外，该模型预测，与实验结果相匹配的低多巴胺水平会增加缺席（轻微）癫痫发作的可能性。与其他CTBG建模研究一致，当传入和传出BG与CT系统的连接增强时，表现出对缺席发作活动的抑制。BG被证明在强直-阵挛发作状态附近抑制CTBG系统的活性，从而深入了解BG回路中目前治疗的疗效。TRN的睡眠状态也被发现可以抑制病理性PD活动匹配观察。总的来说，这些发现证明了广泛性癫痫和帕金森病的相干振荡之间有很强的相似性，并为可能的合并症提供了见解。 et.al.|[2401.13467](http://arxiv.org/abs/2401.13467)|null|
|**2024-01-17**|**Reproducibility via neural fields of visual illusions induced by localized stimuli**|本文研究了Billock和Tsou[PNAS，2007]使用Amari型神经场的可控性对初级视皮层（V1）的皮层活动进行建模的实验复制，重点关注中央凹或外周视野中的规则漏斗模式。其目的是理解和模拟在这些实验中观察到的视觉现象，强调其非线性性质。这项研究包括设计模拟Billock和Tsou实验中视觉刺激的感官输入。然后从理论和数值上研究这些输入引起的后图像，以确定它们复制实验观察到的视觉效果的能力。这项研究的一个关键方面是研究神经反应的非线性性质所引起的影响。特别是，通过强调兴奋性和抑制性神经元在某些视觉现象出现中的重要性，这项研究表明，这两种类型的神经元活动的相互作用在视觉过程中发挥着重要作用，挑战了后者主要由兴奋性活动单独驱动的假设。 et.al.|[2401.09108](http://arxiv.org/abs/2401.09108)|null|
|**2024-01-12**|**Motion2VecSets: 4D Latent Vector Set Diffusion for Non-rigid Shape Reconstruction and Tracking**|我们介绍了Motion2VecSets，这是一种用于从点云序列进行动态曲面重建的4D扩散模型。虽然现有的最先进的方法已经证明在使用神经场表示重建非刚性对象方面取得了成功，但传统的前馈网络遇到了来自噪声、部分或稀疏点云的模糊观测的挑战。为了应对这些挑战，我们引入了一种扩散模型，该模型通过压缩潜在表示的迭代去噪过程来显式学习非刚性对象的形状和运动分布。当处理模糊输入时，基于扩散的先验能够进行更合理和概率的重建。我们用潜在向量集参数化4D动力学，而不是使用全局潜在。这种新颖的4D表示使我们能够学习局部表面形状和变形模式，从而实现更准确的非线性运动捕捉，并显著提高对看不见的运动和身份的可推广性。对于更具时间连贯性的目标跟踪，我们同步地对变形潜集进行去噪，并在多个帧之间交换信息。为了避免计算开销，我们设计了一个交错的空间和时间注意力块，以沿着空间和时间域交替聚集变形潜伏期。与最先进的方法进行了广泛的比较，证明了我们的Motion2VenSets在从各种不完美的观测进行4D重建方面的优势，特别是在从DeformingThings4D Animals数据集上的稀疏点云重建看不见的个体方面，与CaDex相比，交集优于并集（IoU）提高了19%。更多详细信息，请访问https://vveicao.github.io/projects/Motion2VecSets/. et.al.|[2401.06614](http://arxiv.org/abs/2401.06614)|null|
|**2024-01-05**|**Denoising Vision Transformers**|我们深入研究了视觉转换器（ViTs）固有的一个细微但重大的挑战：这些模型的特征图显示出网格状的伪影，这对ViTs在下游任务中的性能造成了不利影响。我们的研究将这个基本问题追溯到输入阶段的位置嵌入。为了解决这一问题，我们提出了一种新的噪声模型，该模型普遍适用于所有的ViT。具体来说，噪声模型将ViT输出分解为三个部分：一个没有噪声伪影的语义术语和两个以像素位置为条件的伪影相关术语。这种分解是通过在每幅图像的基础上加强与神经场的交叉视图特征一致性来实现的。这种逐图像优化过程从原始ViT输出中提取无伪影特征，为离线应用程序提供干净的特征。扩大了我们的解决方案的范围，以支持在线功能，我们引入了一种可学习的去噪器，直接从未处理的ViT输出中预测无伪影特征，这显示出对新数据的显著泛化能力，而无需对每张图像进行优化。我们的两阶段方法，称为去噪视觉转换器（DVT），不需要重新训练现有的预先训练的ViT，并且立即适用于任何基于转换器的架构。我们在各种具有代表性的ViT（DINO、MAE、DeiT III、EVA02、CLIP、DINOv2、DINOv2-reg）上评估了我们的方法。广泛的评估表明，我们的DVT在多个数据集（例如+3.84mIoU）的语义和几何任务中持续显著地改进了现有的最先进的通用模型。我们希望我们的研究将鼓励对ViT设计进行重新评估，特别是关于位置嵌入的天真使用。 et.al.|[2401.02957](http://arxiv.org/abs/2401.02957)|null|
|**2023-12-30**|**PlanarNeRF: Online Learning of Planar Primitives with Neural Radiance Fields**|从视觉数据中识别空间完整的平面基元是计算机视觉中的一项关键任务。现有的方法在很大程度上局限于2D片段恢复或简化3D结构，即使具有广泛的平面注释。我们提出了PlanarNeRF，这是一种能够通过在线学习检测密集3D平面的新框架。PlanarNeRF利用神经场表示，带来了三个主要贡献。首先，它利用并行的外观和几何知识增强了三维平面检测。其次，提出了一种轻量级的平面拟合模块来估计平面参数。第三，引入了一种具有更新机制的新的全局内存库结构，确保了跨帧一致性。PlanarNeRF的灵活架构使其能够在二维监督和自监督解决方案中发挥作用，在每种解决方案中，它都可以有效地从稀疏的训练信号中学习，显著提高训练效率。通过广泛的实验，我们证明了PlanarNeRF在各种场景下的有效性，并比现有工作有了显著的改进。 et.al.|[2401.00871](http://arxiv.org/abs/2401.00871)|null|
|**2024-01-01**|**Deblurring 3D Gaussian Splatting**|最近对辐射场的研究为具有照片级真实感渲染质量的新颖视图合成铺平了坚实的道路。然而，它们通常使用神经网络和体积绘制，这两种方法的训练成本很高，并且由于绘制时间长，阻碍了它们在各种实时应用中的广泛使用。最近，人们提出了一种基于3D高斯散射的方法来对3D场景进行建模，并在实时渲染图像的同时实现了显著的视觉质量。然而，如果训练图像模糊，则渲染质量会严重下降。模糊通常是由于镜头散焦、物体运动和相机抖动而产生的，它不可避免地会干扰干净图像的获取。先前的几项研究试图使用神经场从模糊的输入图像中渲染干净清晰的图像。然而，这些工作中的大多数仅设计用于基于体积渲染的神经辐射场，并不直接适用于基于光栅化的3D高斯散射方法。因此，我们提出了一种新的实时去模糊框架，即去模糊3D高斯散点，使用小型多层感知器（MLP）来操纵每个3D高斯的协方差来对场景模糊度进行建模。虽然去模糊的3D高斯飞溅仍然可以享受实时渲染，但它可以从模糊的图像中重建精细和清晰的细节。在基准上进行了各种实验，结果表明了我们的去模糊方法的有效性。定性结果可在https://benhenryl.github.io/Deblurring-3D-Gaussian-Splatting/ et.al.|[2401.00834](http://arxiv.org/abs/2401.00834)|null|
|**2023-12-22**|**Fluid Simulation on Neural Flow Maps**|我们介绍了神经流图，这是一种新的模拟方法，将新兴的隐式神经表示范式与基于流图理论的流体模拟相结合，以实现最先进的无粘流体现象模拟。我们设计了一种新的混合神经场表示，空间稀疏神经场（SSNF），它将小型神经网络与重叠、多分辨率和空间稀疏网格的金字塔相融合，以高精度紧凑地表示长期时空速度场。有了这个神经速度缓冲器，我们以机械对称的方式计算长期双向流图及其雅可比矩阵，以促进对现有解决方案的大幅精度提高。这些长程双向流图实现了低耗散的高平流精度，进而促进了高保真度的不可压缩流模拟，显示了复杂的旋涡结构。我们展示了我们的神经流体模拟在各种具有挑战性的模拟场景中的有效性，包括跳跃涡流、碰撞涡流、涡流重新连接，以及移动障碍物和密度差异产生的涡流。我们的例子表明，在能量守恒、视觉复杂性、对实验观测的遵守以及详细旋涡结构的保存方面，与现有方法相比，性能有所提高。 et.al.|[2312.14635](http://arxiv.org/abs/2312.14635)|null|

<p align=right>(<a href=#updated-on-20240131>back to top</a>)</p>

[contributors-shield]: https://img.shields.io/github/contributors/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[contributors-url]: https://github.com/Vincentqyw/cv-arxiv-daily/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[forks-url]: https://github.com/Vincentqyw/cv-arxiv-daily/network/members
[stars-shield]: https://img.shields.io/github/stars/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[stars-url]: https://github.com/Vincentqyw/cv-arxiv-daily/stargazers
[issues-shield]: https://img.shields.io/github/issues/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[issues-url]: https://github.com/Vincentqyw/cv-arxiv-daily/issues

