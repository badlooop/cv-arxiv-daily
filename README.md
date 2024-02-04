[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]

## Updated on 2024.02.04
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
|**2024-02-01**|**360-GS: Layout-guided Panoramic Gaussian Splatting For Indoor Roaming**|近年来，三维高斯散射（3D-GS）以其实时性和照片真实性的渲染引起了人们的极大关注。这项技术通常将透视图像作为输入，并通过将一组3D椭圆高斯分布到图像平面上来优化它们，从而产生2D高斯。然而，将3D-GS应用于全景输入在使用2D高斯有效地将投影建模到 ${360^\circ}$图像的球面上方面存在挑战。在实际应用中，输入全景图往往是稀疏的，导致3D高斯图的初始化不可靠，并导致3D-GS质量下降。此外，由于无纹理平面（例如，墙和地板）的几何约束不足，3D-GS难以用椭圆高斯对这些平坦区域进行建模，导致在新视图中出现显著的浮动。为了解决这些问题，我们提出了360-GS，这是一种针对有限的全景输入集的新的$360^{\circ}$ 高斯飞溅。360-GS不是将3D高斯直接泼洒到球面上，而是将其投影到单位球体的切平面上，然后将其映射到球面投影。这种自适应使得能够使用高斯表示投影。我们通过利用全景图中的布局先验来指导360-GS的优化，这些先验易于获得，并包含关于室内场景的强大结构信息。我们的实验结果表明，360-GS允许全景渲染，并在新的视图合成中以更少的伪影优于最先进的方法，从而在室内场景中提供身临其境的漫游。 et.al.|[2402.00763](http://arxiv.org/abs/2402.00763)|null|
|**2024-02-01**|**StopThePop: Sorted Gaussian Splatting for View-Consistent Real-time Rendering**|高斯散射已经成为从不同领域的图像构建3D表示的一个突出模型。然而，3D高斯飞溅渲染管道的效率依赖于几个简化。值得注意的是，使用单个视图空间深度将高斯飞溅减少到2D会在视图旋转过程中引入爆裂和混合伪影。解决这个问题需要精确的每像素深度计算，但与全局排序操作相比，完整的每像素排序成本过高。在本文中，我们提出了一种新的分层光栅化方法，该方法以最小的处理开销系统地处理和剔除飞溅。我们的软件光栅化器有效地消除了弹出的伪影和视图不一致，通过定量和定性测量都证明了这一点。同时，我们的方法通过弹出来减少欺骗视图相关效果的可能性，确保了更真实的表示。尽管消除了作弊，但我们的方法在测试图像中获得了可比的定量结果，同时提高了运动中新视图合成的一致性。由于其设计，我们的分层方法平均只比原始的高斯飞溅慢4%。值得注意的是，强制执行一致性可以将Gaussian的数量减少大约一半，同时具有几乎相同的质量和视图一致性。因此，渲染性能几乎翻了一番，使我们的方法比原始的高斯Splatting快1.6倍，同时减少了50%的内存需求。 et.al.|[2402.00525](http://arxiv.org/abs/2402.00525)|null|
|**2024-01-31**|**Advances in 3D Generation: A Survey**|生成三维模型是计算机图形学的核心，也是几十年来研究的焦点。随着先进的神经表示和生成模型的出现，3D内容生成领域正在迅速发展，能够创建越来越高质量和多样化的3D模型。这一领域的快速发展使得我们很难跟上最近的所有发展。在这项调查中，我们旨在介绍3D生成方法的基本方法，并建立一个结构化的路线图，包括3D表示、生成方法、数据集和相应的应用程序。具体来说，我们介绍了用作3D生成主干的3D表示。此外，我们全面概述了快速增长的生成方法文献，按算法范式的类型进行分类，包括前馈生成、基于优化的生成、过程生成和生成新视图合成。最后，我们讨论了可用的数据集、应用程序和开放的挑战。我们希望这项调查能帮助读者探索这个令人兴奋的话题，并促进3D内容生成领域的进一步发展。 et.al.|[2401.17807](http://arxiv.org/abs/2401.17807)|null|
|**2024-01-27**|**Gaussian Splashing: Dynamic Fluid Synthesis with Gaussian Splatting**|我们展示了将基于物理的固体和流体动画与3D高斯飞溅（3DGS）相结合的可行性，以在使用3DGS重建的虚拟场景中创建新的效果。利用底层表示中高斯飞溅和基于位置的动力学（PBD）的一致性，我们以内聚的方式管理渲染、视图合成以及固体和流体的动力学。与高斯着色器类似，我们使用添加的法线增强每个高斯内核，将内核的方向与曲面法线对齐，以优化PBD模拟。这种方法有效地消除了由固体中的旋转变形引起的尖锐噪声。它还允许我们集成基于物理的渲染，以增强流体上的动态曲面反射。因此，我们的框架能够真实地再现动态流体上的曲面高光，并促进场景对象和新视图中流体之间的交互。有关更多信息，请访问我们的项目页面\url{https://amysteriouscat.github.io/GaussianSplashing/}. et.al.|[2401.15318](http://arxiv.org/abs/2401.15318)|null|
|**2024-01-26**|**3D Reconstruction and New View Synthesis of Indoor Environments based on a Dual Neural Radiance Field**|同时实现室内环境的3D重建和新视图合成具有广泛的应用，但在技术上非常具有挑战性。基于隐式神经函数的现有技术方法可以获得极好的三维重建结果，但它们在新视图合成方面的性能可能不令人满意。神经辐射场（NeRF）的令人兴奋的发展彻底改变了新的视图合成，然而，基于NeRF的模型可能无法重建干净的几何表面。我们开发了一种双神经辐射场（Du-NeRF），以同时实现高质量的几何重建和视图渲染。Du-NeRF包含两个几何场，一个从SDF场导出以便于几何重建，另一个从密度场导出以促进新视图合成。Du NeRF的一个创新特征是，它将视图无关分量与密度场解耦，并将其用作标签来监督SDF场的学习过程。这减少了形状辐射模糊性，并使几何图形和颜色在学习过程中相互受益。大量实验表明，Du-NeRF可以显著提高室内环境下新视图合成和3D重建的性能，并且在构建包含不服从多视图颜色一致性的精细几何图形的区域时尤其有效。 et.al.|[2401.14726](http://arxiv.org/abs/2401.14726)|null|
|**2024-01-23**|**IRIS: Inverse Rendering of Indoor Scenes from Low Dynamic Range Images**|尽管许多3D重建和新颖的视图合成方法允许从消费者相机轻松捕捉的多视图图像中真实地渲染场景，但它们在表示中烘焙照明，无法支持高级应用程序，如材质编辑、重新照明和虚拟对象插入。通过反向渲染重建基于物理的材料特性和照明有望实现此类应用。然而，大多数反向渲染技术都需要高动态范围（HDR）图像作为输入，这是大多数用户无法访问的设置。我们提出了一种方法，从多视图、低动态范围（LDR）图像中恢复场景的基于物理的材料特性和空间变化的HDR照明。我们在反向渲染管道中对LDR图像形成过程进行建模，并提出了一种新的材料、照明和相机响应模型的优化策略。与采用LDR或HDR输入的最先进的反向渲染方法相比，我们使用合成场景和真实场景来评估我们的方法。我们的方法优于以LDR图像作为输入的现有方法，并允许高度逼真的重新照明和对象插入。 et.al.|[2401.12977](http://arxiv.org/abs/2401.12977)|null|
|**2024-01-24**|**RGBD Objects in the Wild: Scaling Real-World 3D Object Learning from RGB-D Videos**|我们介绍了一种新的在野外捕获的RGB-D对象数据集，称为WildRGB-D。与大多数现有的仅带有RGB捕获的以对象为中心的真实世界数据集不同，深度通道的直接捕获允许更好的3D注释和更广泛的下游应用。WildRGB-D包括大型类别级RGB-D对象视频，这些视频是用iPhone 360度环绕对象拍摄的。它包含大约8500个记录对象和近20000个RGB-D视频，涉及46个常见对象类别。这些视频是在三种设置的不同杂乱背景下拍摄的，以覆盖尽可能多的真实世界场景：（i）一个视频中的单个对象；（ii）一个视频中的多个对象；以及（iii）在一个视频中具有静止手的对象。该数据集由对象遮罩、真实世界比例的相机姿态和RGBD视频中重建的聚合点云进行注释。我们用WildRGB-D对四个任务进行了基准测试，包括新颖的视图合成、相机姿态估计、物体6d姿态估计和物体表面重建。我们的实验表明，RGB-D对象的大规模捕获为推进3D对象学习提供了巨大的潜力。我们的项目页面是https://wildrgbd.github.io/. et.al.|[2401.12592](http://arxiv.org/abs/2401.12592)|null|
|**2024-01-23**|**Methods and strategies for improving the novel view synthesis quality of neural radiation field**|神经辐射场（NeRF）技术可以从2D图像中学习场景的3D隐式模型，并合成逼真的新视图图像。该技术得到了业界的广泛关注，具有良好的应用前景。针对NeRF图像渲染质量需要提高的问题，近三年来，许多研究人员提出了各种方法来提高渲染质量。对最新的相关论文进行了分类和综述，分析了质量改进背后的技术原理，并讨论了质量改进方法的未来发展方向。这项研究可以帮助研究人员快速了解该领域技术的现状和发展脉络，有助于激发更高效算法的发展，促进NeRF技术在相关领域的应用。 et.al.|[2401.12451](http://arxiv.org/abs/2401.12451)|null|
|**2024-01-22**|**HG3-NeRF: Hierarchical Geometric, Semantic, and Photometric Guided Neural Radiance Fields for Sparse View Inputs**|神经辐射场（NeRF）作为一种通过从离散观测中学习场景表示的新型视图合成范式，已经引起了人们的极大关注。然而，当面对稀疏视图输入时，NeRF表现出明显的性能退化，从而限制了其进一步的适用性。在这项工作中，我们介绍了层次几何、语义和光度引导的NeRF（HG3-NeRF），这是一种新的方法，可以解决上述限制，并增强不同视图中几何、语义内容和外观的一致性。我们提出了分层几何制导（HGG），将运动结构的附加（SfM），即稀疏深度先验，纳入场景表示中。与直接深度监督不同，HGG从局部几何区域到全局几何区域对体积点进行采样，减轻了深度先验中固有偏差引起的偏差。此外，我们从不同分辨率的图像中观察到的语义一致性的显著变化中获得了灵感，并提出了层次语义引导（HSG）来学习粗到细的语义内容，该内容对应于粗到细场景表示。实验结果表明，HG3-NeRF可以在不同的标准基准上优于其他最先进的方法，并实现稀疏视图输入的高保真度合成结果。 et.al.|[2401.11711](http://arxiv.org/abs/2401.11711)|null|
|**2024-01-18**|**Explaining the Implicit Neural Canvas: Connecting Pixels to Neurons by Tracing their Contributions**|隐式神经表示（INRs）的许多变体，其中神经网络被训练为信号的连续表示，对于下游任务具有巨大的实用性，包括新颖的视图合成、视频压缩和图像超分辨率。不幸的是，对这些网络的内部运作方式的研究严重不足。我们的工作，即解释隐式神经画布（XINC），是一个统一的框架，用于通过检查每个神经元对每个输出像素的贡献强度来解释INRs的特性。我们将这些贡献图的集合称为隐式神经画布，并使用这一概念来证明我们研究的INR学会了以令人惊讶的方式“观察”它们所代表的帧。例如，INR往往具有高度分布的表示。虽然缺乏高级对象语义，但它们对颜色和边缘有很大的偏见，而且几乎完全是空间不可知的。我们通过研究视频INR中对象在时间上的表现方式得出了我们的结论，使用聚类来可视化跨层和架构的相似神经元，并表明这是由运动主导的。这些见解证明了我们的分析框架的普遍有用性。我们的项目页面位于https://namithap10.github.io/xinc. et.al.|[2401.10217](http://arxiv.org/abs/2401.10217)|null|

<p align=right>(<a href=#updated-on-20240204>back to top</a>)</p>

## 3D Reconstruction

|Publish Date|Title|Abstract|PDF|Code|
|---|---|---|---|---|
|**2024-02-01**|**Diffusion-based Light Field Synthesis**|光场（LFs）有助于在角度维度上记录全面的场景辐射，在3D重建、虚拟现实和计算摄影中有着广泛的应用。然而，由于主流的采集策略涉及手动采集或费力的软件合成，LF采集不可避免地耗时且资源密集。鉴于这一挑战，我们引入了LFdiff，这是一种简单而有效的基于扩散的生成框架，专门用于LF合成，它只采用单个RGB图像作为输入。LFdiff利用单目深度估计网络估计的视差，并结合了两个独特的组件：一个新的条件方案和一个为LF数据量身定制的噪声估计网络。具体来说，我们设计了一种位置感知扭曲条件方案，通过鲁棒的条件信号增强视图间几何学习。然后，我们提出了DistgUnet，一种基于解纠缠的噪声估计网络，以利用综合的LF表示。大量实验表明，LFdiff在合成视觉愉悦和视差可控的光场方面表现出色，具有增强的泛化能力。此外，综合结果证实了生成的LF数据的广泛适用性，涵盖了LF超分辨率和重新聚焦等应用。 et.al.|[2402.00575](http://arxiv.org/abs/2402.00575)|null|
|**2024-02-01**|**DARCS: Memory-Efficient Deep Compressed Sensing Reconstruction for Acceleration of 3D Whole-Heart Coronary MR Angiography**|三维冠状动脉磁共振血管造影术（CMRA）需要能够显著抑制严重欠采样采集的伪影的重建算法。虽然基于展开的深度重建方法在2D图像重建方面取得了最先进的性能，但它们在3D重建中的应用受到训练展开的网络所需的大量内存的阻碍。在这项研究中，我们提出了一种基于预训练的伪影估计网络的稀疏化变换的高效记忆深度压缩传感方法。其动机是，当输入图像没有伪影时，由训练有素的网络估计的伪影图像是稀疏的，而当输入图像受伪影影响时，稀疏度较低。因此，伪影估计网络可以用作固有的稀疏化变换。将所提出的方法称为基于去混叠正则化的压缩传感（DARCS），与传统的压缩传感方法、去混叠生成对抗性网络（DAGAN）、基于模型的深度学习（MoDL）和即插即用的三维CMRA加速方法进行了比较。结果表明，相对于比较方法，所提出的方法在重建质量上有很大的提高。此外，对于不同的欠采样率和噪声水平，所提出的方法得到了很好的推广。所提出的方法的内存使用量仅为MoDL所需内存使用量的63%。总之，所提出的方法在降低存储器负担的情况下提高了三维CMRA的重建质量。 et.al.|[2402.00320](http://arxiv.org/abs/2402.00320)|null|
|**2024-01-31**|**Local Feature Matching Using Deep Learning: A Survey**|局部特征匹配在计算机视觉领域有着广泛的应用，包括图像检索、三维重建和物体识别等领域。然而，由于视点和照明变化等因素，在提高匹配的准确性和稳健性方面仍然存在挑战。近年来，深度学习模型的引入引发了对局部特征匹配技术的广泛探索。这项工作的目的是提供局部特征匹配方法的全面概述。根据探测器的存在，这些方法分为两个关键部分。基于检测器的类别包括检测然后描述、联合检测和描述、描述然后检测以及基于图的技术等模型。相比之下，无检测器类别包括基于CNN、基于转换器和基于补丁的方法。我们的研究超越了方法分析，结合了对流行数据集和指标的评估，以促进对最先进技术的定量比较。本文还探讨了局部特征匹配在运动结构、遥感图像配准和医学图像配准等不同领域的实际应用，强调了其在各个领域的通用性和意义。最终，我们努力概述该领域当前面临的挑战，并提供未来的研究方向，从而为参与局部特征匹配及其互连领域的研究人员提供参考。 et.al.|[2401.17592](http://arxiv.org/abs/2401.17592)|null|
|**2024-01-30**|**Self-Supervised Representation Learning for Nerve Fiber Distribution Patterns in 3D-PLI**|要全面了解人脑的组织原理，除其他因素外，还需要对神经纤维结构进行可量化的描述。三维偏振光成像（3D-PLI）是一种显微镜成像技术，能够以高分辨率深入了解有髓神经纤维的细粒度组织。表征在3D-PLI中观察到的纤维结构的描述符将实现下游分析任务，如多模式相关性研究、聚类和映射。然而，在3D-PLI中对光纤结构进行独立于观察者的表征的最佳实践尚不可用。为此，我们提出应用一种完全数据驱动的方法，使用自监督表示学习来表征3D-PLI图像中的神经纤维结构。我们介绍了一种3D上下文对比学习（CL-3D）目标，该目标利用3D重建体积的组织学脑切片中纹理示例的空间邻域来对正配对进行采样以进行对比学习。我们将这种采样策略与专门设计的图像增强相结合，以获得对3D-PLI参数图中典型变化的鲁棒性。该方法已在一只vervet猴子大脑的3D重建枕叶中进行了演示。我们发现，提取的特征对神经纤维的不同配置高度敏感，但对组织学处理引起的连续脑切片之间的变化很强。我们展示了它们在检索同质光纤架构的集群和对光纤架构的特定组件（如U型光纤）的交互式选择模板执行数据挖掘方面的实际适用性。 et.al.|[2401.17207](http://arxiv.org/abs/2401.17207)|null|
|**2024-01-30**|**Physical Priors Augmented Event-Based 3D Reconstruction**|三维神经隐式表示在许多机器人应用中起着重要的作用。然而，当只有事件流可用时，由于稀疏性和信息缺乏，从真实的事件数据重建神经辐射场（NeRF）仍然是一个挑战。在本文中，我们利用事件数据背后的运动、几何和密度先验来施加强大的物理约束，以增强NeRF训练。所提出的新管道可以直接受益于这些先验，以在没有额外输入的情况下重建3D场景。此外，我们提出了一种新的基于密度引导的基于补丁的采样策略，用于鲁棒和高效的学习，它不仅加速了训练过程，而且有助于局部几何的表达。更重要的是，我们建立了第一个用于基于事件的3D重建的大型数据集，其中包含101个具有各种材料和几何形状的对象，以及所有相机视点的图像和深度图的基本情况，这大大促进了相关领域的其他研究。代码和数据集将在https://github.com/Mercerai/PAEv3d. et.al.|[2401.17121](http://arxiv.org/abs/2401.17121)|**[link](https://github.com/mercerai/paev3d)**|
|**2024-01-30**|**OmniSCV: An Omnidirectional Synthetic Image Generator for Computer Vision**|全方位和360度图像在工业和消费社会中越来越普遍，引起了全方位计算机视觉的关注。它们的宽视场允许仅从图像中收集大量关于环境的信息。然而，这些图像的失真需要开发特定的算法来进行处理和解释。此外，大量的图像对于基于学习的计算机视觉算法的正确训练是必不可少的。在本文中，我们提出了一种用于生成具有语义和深度信息的全向图像数据集的工具。这些图像是从在虚幻引擎4的真实虚拟环境中通过接口插件获取的一组捕获中合成的。我们收集了各种著名的投影模型，如等矩形和圆柱形全景图、不同的鱼眼透镜、折反射系统和经验模型。此外，在我们的工具中，我们将真实感非中心投影系统包括为非中心全景和非中心折反射系统。据我们所知，这是文献中第一个报道的生成真实感非中心图像的工具。此外，由于全向图像是虚拟制作的，我们提供了关于语义和深度的像素信息，以及相机校准参数的完美知识。这允许创建具有像素精度的地面实况信息，用于训练学习算法和测试3D视觉方法。为了验证所提出的工具，测试了不同的计算机视觉算法，如从屈光和折反射中心图像中提取线，使用等矩形全景进行3D布局恢复和SLAM，以及从非中心全景进行3D重建。 et.al.|[2401.17061](http://arxiv.org/abs/2401.17061)|**[link](https://github.com/sbrunoberenguel/omniscv)**|
|**2024-01-29**|**SuNeRF: 3D reconstruction of the solar EUV corona using Neural Radiance Fields**|为了了解其演变及其喷发事件的影响，太阳受到多个卫星任务的永久监测。太阳等离子体的光学薄发射和有限的视点数量使得重建太阳大气的几何形状和结构具有挑战性；然而，这些信息是理解太阳的缺失环节：一颗三维演化的恒星。我们提出了一种方法，能够在极紫外（EUV）光中观察到最上层太阳层（日冕）的完整3D表示。我们使用深度学习方法进行三维场景表示，考虑到辐射传输，通过三次同时观测绘制整个太阳大气层的地图。我们证明，我们的方法提供了前所未有的太阳极重建，并直接实现了对日冕结构、太阳丝、日冕空洞轮廓和日冕物质抛射的高度估计。我们使用模型生成的合成EUV图像验证了该方法，发现我们的方法即使从有限的32个黄道视点（ $|\text｛latitude｝|\leq 7^\circ$ ）也能准确地捕捉到太阳的3D几何结构。我们使用集成方法量化模型的不确定性，该方法允许我们在缺乏基本事实的情况下估计模型性能。我们的方法能够对我们最近的恒星进行新的观察，是有效利用多仪器数据集的突破性技术，为未来的集群任务铺平了道路。 et.al.|[2401.16388](http://arxiv.org/abs/2401.16388)|null|
|**2024-01-29**|**Reconstructing Close Human Interactions from Multiple Views**|本文解决了一项具有挑战性的任务，即重建由多台校准相机拍摄的参与亲密互动的多个人的姿势。困难源于由于人与人之间的遮挡而导致的噪声或错误的2D关键点检测、由于密切的交互而导致的将关键点与个体相关联的严重模糊性以及训练数据的稀缺性，因为在拥挤的场景中收集和注释运动数据是资源密集型的。我们引入了一种新颖的系统来应对这些挑战。我们的系统集成了一个基于学习的姿态估计组件及其相应的训练和推理策略。姿态估计组件采用多视图2D关键点热图作为输入，并使用3D条件体积网络重建每个个体的姿态。由于网络不需要图像作为输入，我们可以利用测试场景中的已知相机参数和大量现有的运动捕捉数据来合成模拟测试场景中真实数据分布的大量训练数据。大量实验表明，我们的方法在姿态精度方面显著优于以前的方法，并且可以在各种相机设置和人群规模中推广。代码可在我们的项目页面上获得：https://github.com/zju3dv/CloseMoCap. et.al.|[2401.16173](http://arxiv.org/abs/2401.16173)|**[link](https://github.com/zju3dv/closemocap)**|
|**2024-01-29**|**Domain adaptation strategies for 3D reconstruction of the lumbar spine using real fluoroscopy data**|这项研究解决了在骨科手术中采用手术导航的关键障碍，包括时间、成本、辐射和工作流程集成方面的挑战。最近，我们的工作X23D展示了一种仅从少数术中荧光透视图像生成脊柱三维解剖模型的方法。这通过创建解剖结构的直接术中3D重建来否定了对传统的基于配准的外科导航的需要。尽管取得了这些进步，但X23D的实际应用受到合成训练数据和真实术中图像之间的领域差距的限制。作为回应，我们为配对数据集设计了一种新的数据收集协议，该数据集由来自相同视角的合成和真实荧光透视图像组成。利用这个数据集，我们通过迁移学习完善了我们的深度学习模型，有效地弥合了合成和真实X射线数据之间的领域差距。一种新型的传输机制还允许我们转换真实的X射线以反映合成域，使我们的计算机训练X23D模型能够在现实世界中实现高精度。我们的研究结果表明，精确的模型可以通过三次术中荧光镜检查快速生成整个腰椎的精确3D重建。它获得了84%的F1分数，与我们之前基于合成数据的研究的准确性相匹配。此外，由于计算时间仅为81.1ms，我们的方法提供了手术集成所必需的实时功能。通过检查理想的成像设置和视角相关性，我们进一步证实了我们的系统在临床环境中的实用性和可靠性。我们的研究标志着术中3D重建向前迈出了重要一步，增强了手术计划、导航和机器人技术。 et.al.|[2401.16027](http://arxiv.org/abs/2401.16027)|null|
|**2024-01-29**|**2L3: Lifting Imperfect Generated 2D Images into Accurate 3D**|从单个图像重建3D对象是一个有趣但具有挑战性的问题。一个有前途的解决方案是利用多视图（MV）3D重建将生成的MV图像融合成一致的3D对象。然而，生成的图像通常存在照明不一致、几何体错位和视图稀疏的问题，导致重建质量较差。为了解决这些问题，我们提出了一种新的3D重建框架，该框架利用固有分解引导、瞬态单先验引导和视图增强来分别解决这三个问题。具体来说，我们首先利用阴影信息从生成的图像中解耦，以减少不一致照明的影响；然后，我们引入了具有视点相关瞬态编码的单声道先验来增强重构的法线；最后，我们设计了一种视图增强融合策略，最大限度地减少生成的稀疏视图中的像素级损失和增强的随机视图中的语义损失，从而获得视图一致的几何结构和详细的纹理。因此，我们的方法能够集成预先训练的MV图像生成器和基于神经网络的体积有符号距离函数（SDF）表示，用于单个图像到3D对象的重建。我们在各种数据集上评估了我们的框架，并证明了其在定量和定性评估中的卓越性能，这意味着3D对象重建方面取得了重大进展。与最新的同步梦想家方法相比，我们将倒角距离误差降低了约36%，PSNR提高了约30%。 et.al.|[2401.15841](http://arxiv.org/abs/2401.15841)|null|

<p align=right>(<a href=#updated-on-20240204>back to top</a>)</p>

## Diffusion

|Publish Date|Title|Abstract|PDF|Code|
|---|---|---|---|---|
|**2024-02-01**|**AToM: Amortized Text-to-Mesh using 2D Diffusion**|我们介绍了摊销文本到网格（AToM），这是一种同时在多个文本提示中优化的前馈文本到网格框架。现有的文本到3D方法通常需要耗时的每次提示优化，并且通常输出多边形网格以外的表示，与此相反，AToM在不到1秒的时间内直接生成高质量的纹理网格，训练成本降低了约10倍，并推广到看不见的提示。我们的关键思想是一种新颖的基于三平面的文本到网格架构，该架构具有两阶段摊销优化策略，可确保稳定的训练并实现可扩展性。通过在各种即时基准上进行广泛的实验，AToM显著优于最先进的摊销方法，精度高出4倍多（在DF415数据集中），并产生更可区分和更高质量的3D输出。AToM表现出强大的可推广性，与每提示解决方案不同，它为看不见的插值提示提供了细粒度的3D资产，而无需在推理过程中进行进一步优化。 et.al.|[2402.00867](http://arxiv.org/abs/2402.00867)|null|
|**2024-02-01**|**ViCA-NeRF: View-Consistency-Aware 3D Editing of Neural Radiance Fields**|我们介绍了ViCA NeRF，这是第一种使用文本指令进行三维编辑的视图一致性感知方法。除了隐式神经辐射场（NeRF）建模外，我们的关键见解是利用两种正则化源，在不同视图之间显式传播编辑信息，从而确保多视图的一致性。对于几何正则化，我们利用从NeRF导出的深度信息来建立不同视图之间的图像对应关系。对于学习的正则化，我们在编辑和未编辑的图像之间对齐2D扩散模型中的潜在代码，使我们能够编辑关键视图并在整个场景中传播更新。结合这两种策略，我们的ViCA NeRF分两个阶段运作。在初始阶段，我们混合来自不同视图的编辑以创建初步的三维编辑。接下来是NeRF训练的第二阶段，致力于进一步完善场景的外观。实验结果表明，与现有技术相比，ViCA NeRF提供了更灵活、高效（速度快3倍）的编辑，具有更高的一致性和细节水平。我们的代码是公开的。 et.al.|[2402.00864](http://arxiv.org/abs/2402.00864)|**[link](https://github.com/dongjiahua/vica-nerf)**|
|**2024-02-01**|**An Analysis of the Variance of Diffusion-based Speech Enhancement**|扩散模型被证明是生成语音增强的强大模型。在最近的SGMSE+方法中，训练涉及扩散过程的随机微分方程，逐渐将高斯噪声和环境噪声添加到干净的语音信号中。语音增强性能随着随机微分方程的选择而变化，当添加环境噪声和高斯噪声时，随机微分方程控制均值和方差沿扩散过程的演变。在这项工作中，我们强调了方差的规模是语音增强性能的主要参数，并表明它控制了噪声衰减和语音失真之间的权衡。更具体地说，我们表明，更大的方差增加了噪声衰减，并允许减少计算足迹，因为生成估计所需的函数评估更少。 et.al.|[2402.00811](http://arxiv.org/abs/2402.00811)|null|
|**2024-02-01**|**Distilling Conditional Diffusion Models for Offline Reinforcement Learning through Trajectory Stitching**|深度生成模型最近成为离线强化学习的一种有效方法。然而，它们的大模型尺寸给计算带来了挑战。我们通过提出一种基于数据扩充的知识提取方法来解决这个问题。特别是，高回报轨迹是从条件扩散模型中生成的，并通过利用新奖励生成器的新颖缝合算法将其与原始轨迹混合。将所得数据集应用于行为克隆，在几个D4RL基准上，学习到的小得多的浅层策略优于或几乎匹配深度生成规划者。 et.al.|[2402.00807](http://arxiv.org/abs/2402.00807)|null|
|**2024-02-01**|**AnimateLCM: Accelerating the Animation of Personalized Diffusion Models and Adapters with Decoupled Consistency Learning**|视频扩散模型由于其产生连贯和高保真视频的能力而越来越受到关注。然而，迭代去噪过程使其计算密集且耗时，从而限制了其应用。受一致性模型（CM）的启发，我们提出了AnimateLCM，允许在最小步骤内生成高保真视频。一致性模型提取预训练的图像扩散模型，以最小步骤加速采样，并成功扩展了条件图像生成的潜在一致性模型。我们没有直接对原始视频数据集进行一致性学习，而是提出了一种解耦的一致性学习策略，将图像生成先验和运动生成先验的提取解耦，提高了训练效率，提高了生成视觉质量。此外，为了使即插即用适配器能够在稳定的扩散社区中组合，以实现各种功能（例如，用于可控生成的ControlNet）。我们提出了一种有效的策略，使现有适配器适应我们提取的文本条件视频一致性模型，或者在不影响采样速度的情况下从头开始训练适配器。我们在图像条件视频生成和布局条件视频生成中验证了所提出的策略，所有这些都实现了最佳性能。实验结果验证了我们提出的方法的有效性。代码和重量将公开。更多详细信息，请访问https://github.com/G-U-N/AnimateLCM. et.al.|[2402.00769](http://arxiv.org/abs/2402.00769)|**[link](https://github.com/g-u-n/animatelcm)**|
|**2024-02-01**|**The Sonora Substellar Atmosphere Models. IV. Elf Owl: Atmospheric Mixing and Chemical Disequilibrium with Varying Metallicity and C/O Ratios**|由于许多棕矮星和巨型系外行星大气中的垂直混合，导致的不平衡化学现象已经得到了证实。这些物体的大气模型通常用高度不确定的 $K_｛\rm-zz｝$扩散参数来参数化混合。混合在改变含C-N-O分子丰度中的作用主要是针对太阳成分大气进行的探索。然而，大气金属性和C/O比也会影响大气化学。因此，我们为JWST观测提供了自洽无云1D辐射对流平衡模型大气的\texttt｛Sonora Elf Owl｝网格，其中包括几个数量级的$K_｛\rm zz｝$变化，还包括亚太阳系与超太阳系的金属量和C/O比。我们发现$K_｛\rm-zz｝$对$T（P）$轮廓和光谱的影响是$T_｛\ rm-eff｝$和金属性的强函数。与富含金属的大气相比，对于贫金属的物体$K_｛\rm-zz｝$在显著较高的$T_｛\ rm-eff｝$下对大气有很大影响，其中$K_。我们在多个波长窗口中，特别是在3-5$\mu$m处，确定了变化的$K_｛\rm-zz｝$和金属性之间的显著光谱退化。我们使用\texttt｛Sonora Elf Owl｝大气网格来拟合从$T_｛\rm eff｝＝550-1150$ K的9个早期到晚期T型天体样本的观测光谱。使用自洽模型，我们发现这种缓慢的垂直混合是由于对这些大气中深层分离辐射区混合的探测。 et.al.|[2402.00756](http://arxiv.org/abs/2402.00756)|null|
|**2024-02-01**|**Neutral carbon in diffuse interstellar medium: abundance matching with H2 for DLAs at high redshifts**|本文研究了扩散冷中性介质中CI/H $_2$的相对丰度。利用化学和热平衡模型，我们计算了CI/H$_2$与介质的主要参数：氢数密度、金属性、紫外线场强度和宇宙线电离率（CRIR）的相关性。我们表明，假设扩散冷中性介质（CNM）中的典型预期条件，在我们的模型中可以再现阻尼莱曼-α系统（DLA）中在高红移下观察到的相对CI和H$_2$柱密度。利用额外观察到的关于金属性、HI柱密度和CI精细结构能级激发的信息，以及温度，我们估计了在高红移下CNM中的宽范围金属性，CRIR在$\sim10^{-16}$到$\rm几次10^{-15}\rm s^{-1}$的范围内，氢数密度在$\sim 10-10^3$cm$^{-3}$范围内，UV场在从$10^{-2}$到$\rm的范围内是Mathis场的10^2$的几倍。我们认为，由于这项工作中使用的观测量是相当均匀的，并且受辐射传输效应的影响要小得多（与例如HD的离解和H$_2$ 旋转能级的UV泵浦相比），我们的估计相对于云的精确几何模型和UV场的局部源的假设是相当稳健的。 et.al.|[2402.00714](http://arxiv.org/abs/2402.00714)|null|
|**2024-02-01**|**Cylindrically symmetric diffusion model for relativistic heavy-ion collisions**|基于非平衡统计考虑，导出了一个具有圆柱对称性的相对论扩散模型，该模型基于量子色动力学将初始状态在时间上传播到热平衡极限：对代表相对论相空间轨迹的马尔可夫随机过程的现有框架进行适配，获得了粒子数分布函数相对于横向和纵向快度的时间演化的Fokker-Planck方程。由此产生的部分演化分布函数被转换到横向动量和伪速度空间，并与欧洲核子研究中心大型强子对撞机（LHC）的带电强子数据进行比较。 et.al.|[2402.00628](http://arxiv.org/abs/2402.00628)|null|
|**2024-02-01**|**CapHuman: Capture Your Moments in Parallel Universes**|我们专注于一种新颖的以人为中心的图像合成任务，即，仅给定一张参考面部照片，就可以在不同的背景下生成具有不同头部位置、姿势和面部表情的特定个体图像。为了实现这一目标，我们认为我们的生成模型应该能够具有以下有利的特征：（1）对我们的世界和人类社会有强烈的视觉和语义理解，用于基本对象和人类图像的生成。（2） 可推广的身份保护能力。（3） 灵活且细粒度的头部控制。最近，大型预训练的文本到图像扩散模型已经显示出显著的结果，成为强大的生成基础。作为基础，我们的目标是释放预训练模型的上述两种能力。在这项工作中，我们提出了一个名为CapHuman的新框架。我们接受“编码”，然后学会对齐“范式，它能够为新个体提供可推广的身份保护，而无需繁琐的推理调整。CapHuman对身份特征进行编码，然后学会将其与潜在空间对齐。此外，我们在为我们的模型配备灵活和3D一致的控制人头的3D面部之前引入了3D面部。广泛的定性和定量分析trate我们的CapHuman可以制作出保存完好、照片逼真、高保真的肖像，具有内容丰富的表现和各种头部呈现，优于已建立的基线。代码和检查点将在发布https://github.com/VamosC/CapHuman. et.al.|[2402.00627](http://arxiv.org/abs/2402.00627)|**[link](https://github.com/vamosc/caphuman)**|
|**2024-02-01**|**Diffusion-based Light Field Synthesis**|光场（LFs）有助于在角度维度上记录全面的场景辐射，在3D重建、虚拟现实和计算摄影中有着广泛的应用。然而，由于主流的采集策略涉及手动采集或费力的软件合成，LF采集不可避免地耗时且资源密集。鉴于这一挑战，我们引入了LFdiff，这是一种简单而有效的基于扩散的生成框架，专门用于LF合成，它只采用单个RGB图像作为输入。LFdiff利用单目深度估计网络估计的视差，并结合了两个独特的组件：一个新的条件方案和一个为LF数据量身定制的噪声估计网络。具体来说，我们设计了一种位置感知扭曲条件方案，通过鲁棒的条件信号增强视图间几何学习。然后，我们提出了DistgUnet，一种基于解纠缠的噪声估计网络，以利用综合的LF表示。大量实验表明，LFdiff在合成视觉愉悦和视差可控的光场方面表现出色，具有增强的泛化能力。此外，综合结果证实了生成的LF数据的广泛适用性，涵盖了LF超分辨率和重新聚焦等应用。 et.al.|[2402.00575](http://arxiv.org/abs/2402.00575)|null|

<p align=right>(<a href=#updated-on-20240204>back to top</a>)</p>

## NeRF

|Publish Date|Title|Abstract|PDF|Code|
|---|---|---|---|---|
|**2024-01-31**|**BlockFusion: Expandable 3D Scene Generation using Latent Tri-plane Extrapolation**|我们介绍了BlockFusion，这是一种基于扩散的模型，它将3D场景生成为单元块，并无缝地合并新的块来扩展场景。BlockFusion使用从完整的3D场景网格中随机裁剪的3D块的数据集进行训练。通过逐块拟合，所有训练块都被转换为混合神经场：具有包含几何特征的三平面，然后是用于解码有符号距离值的多层感知器（MLP）。采用变分自动编码器将三平面压缩到潜在的三平面空间中，在该空间上进行去噪扩散处理。应用于潜在表示的扩散允许高质量和多样化的3D场景生成。要在生成过程中扩展场景，只需附加空块以与当前场景重叠，并外推现有的潜在三平面以填充新块。外推是通过在去噪迭代过程中使用来自重叠三平面的特征样本来调节生成过程来完成的。潜在的三平面外推法产生语义和几何上有意义的过渡，与现有场景和谐融合。2D布局调节机制用于控制场景元素的放置和布置。实验结果表明，BlockFusion能够在室内和室外场景中生成具有前所未有的高质量形状的多样化、几何一致和无边界的大型3D场景。 et.al.|[2401.17053](http://arxiv.org/abs/2401.17053)|null|
|**2024-01-26**|**Learning Neural Radiance Fields of Forest Structure for Scalable and Fine Monitoring**|这项工作利用神经辐射场和遥感技术用于林业应用。在这里，我们展示了神经辐射场为改进森林监测中现有的遥感方法提供了广泛的可能性。我们提出的实验证明了它们的潜力：（1）表达森林三维结构的精细特征，（2）融合可用的遥感模式，以及（3）改进三维结构衍生的森林指标。总之，这些特性使神经场成为一种有吸引力的计算工具，具有进一步提高森林监测程序的可扩展性和准确性的巨大潜力。 et.al.|[2401.15029](http://arxiv.org/abs/2401.15029)|null|
|**2024-01-25**|**Learning Robust Generalizable Radiance Field with Visibility and Feature Augmented Point Representation**|本文介绍了广义神经辐射场（NeRF）的一种新范式。以前的通用NeRF方法将多视点立体技术与基于图像的神经渲染相结合进行泛化，产生了令人印象深刻的结果，同时存在三个问题。首先，遮挡常常导致不一致的特征匹配。然后，由于采样点和粗略特征聚合的单独过程，它们在几何不连续性和局部尖锐形状中传递失真和伪影。第三，当源视图离目标视图不够近时，它们基于图像的表示会发生严重退化。为了应对挑战，我们提出了第一个基于点而不是基于图像的渲染构建可泛化神经场的范式，我们称之为可泛化神经点场（GPF）。我们的方法通过几何先验显式地建模可见性，并用神经特征增强它们。我们提出了一种新的非均匀对数采样策略，以提高渲染速度和重建质量。此外，我们提出了一种可学习的内核，该内核在空间上增加了用于特征聚合的特征，减轻了几何结构急剧变化的地方的失真。此外，我们的表现很容易被操纵。实验表明，在泛化和微调设置中，我们的模型可以在三个数据集上提供比所有对应模型和基准更好的几何结构、视图一致性和渲染质量，初步证明了可泛化NeRF新范式的潜力。 et.al.|[2401.14354](http://arxiv.org/abs/2401.14354)|null|
|**2024-01-24**|**Unified neural field theory of brain dynamics underlying oscillations in Parkinson's disease and generalized epilepsies**|通过皮质丘脑基底神经节（CTBG）系统的神经场模型，联合探讨了帕金森病（PD）和全身性癫痫的病理同步神经振荡的机制。基底神经节（BG）被近似为一个单一的有效群体，并分析了它们在调节振荡皮质丘脑（CT）动力学中的作用，反之亦然。除了正常的脑电图节律外，模型中还存在4 Hz和20 Hz左右的增强活动，这与PD的特征频率一致。这些节律是由BG和CT人群之间回路中的共振引起的，类似于先前CT模型中潜在的癫痫振荡。多巴胺耗竭被认为削弱了对PD中这些共振的抑制，网络连接解释了在4-8Hz和20Hz左右BG、丘脑和皮层活动之间的显著一致性。丘脑网状核（TRN）和BG的传入和传出连接位点之间的相似性预测低多巴胺对应于强直-阵挛（大发作）癫痫发作的可能性降低，这与实验结果一致。此外，该模型预测，与实验结果相匹配的低多巴胺水平会增加缺席（轻微）癫痫发作的可能性。与其他CTBG建模研究一致，当传入和传出BG与CT系统的连接增强时，表现出对缺席发作活动的抑制。BG被证明在强直-阵挛发作状态附近抑制CTBG系统的活性，从而深入了解BG回路中目前治疗的疗效。TRN的睡眠状态也被发现可以抑制病理性PD活动匹配观察。总的来说，这些发现证明了广泛性癫痫和帕金森病的相干振荡之间有很强的相似性，并为可能的合并症提供了见解。 et.al.|[2401.13467](http://arxiv.org/abs/2401.13467)|null|
|**2024-01-17**|**Reproducibility via neural fields of visual illusions induced by localized stimuli**|本文研究了Billock和Tsou[PNAS，2007]使用Amari型神经场的可控性对初级视皮层（V1）皮层活动进行建模的实验复制，重点关注中央凹或外周视野中的规则漏斗模式。其目的是理解和模拟在这些实验中观察到的视觉现象，强调其非线性性质。这项研究包括设计模拟Billock和Tsou实验中视觉刺激的感官输入。然后从理论和数值上研究这些输入引起的后图像，以确定它们复制实验观察到的视觉效果的能力。这项研究的一个关键方面是研究神经反应的非线性性质所引起的影响。特别是，通过强调兴奋性和抑制性神经元在某些视觉现象出现中的重要性，这项研究表明，这两种类型的神经元活动的相互作用在视觉过程中发挥着重要作用，挑战了后者主要由兴奋性活动单独驱动的假设。 et.al.|[2401.09108](http://arxiv.org/abs/2401.09108)|null|
|**2024-01-12**|**Motion2VecSets: 4D Latent Vector Set Diffusion for Non-rigid Shape Reconstruction and Tracking**|我们介绍了Motion2VecSets，这是一种用于从点云序列进行动态曲面重建的4D扩散模型。虽然现有的最先进的方法已经证明在使用神经场表示重建非刚性对象方面取得了成功，但传统的前馈网络遇到了来自噪声、部分或稀疏点云的模糊观测的挑战。为了应对这些挑战，我们引入了一种扩散模型，该模型通过压缩潜在表示的迭代去噪过程来显式学习非刚性对象的形状和运动分布。当处理模糊输入时，基于扩散的先验能够进行更合理和概率的重建。我们用潜在向量集参数化4D动力学，而不是使用全局潜在。这种新颖的4D表示使我们能够学习局部表面形状和变形模式，从而实现更准确的非线性运动捕捉，并显著提高对看不见的运动和身份的可推广性。对于更具时间连贯性的目标跟踪，我们同步地对变形潜集进行去噪，并在多个帧之间交换信息。为了避免计算开销，我们设计了一个交错的空间和时间注意力块，以沿着空间和时间域交替聚集变形潜伏期。与最先进的方法进行了广泛的比较，证明了我们的Motion2VenSets在从各种不完美的观测进行4D重建方面的优势，特别是在从DeformingThings4D Animals数据集上的稀疏点云重建看不见的个体方面，与CaDex相比，交集优于并集（IoU）提高了19%。更多详细信息，请访问https://vveicao.github.io/projects/Motion2VecSets/. et.al.|[2401.06614](http://arxiv.org/abs/2401.06614)|null|
|**2024-01-05**|**Denoising Vision Transformers**|我们深入研究了视觉转换器（ViTs）固有的一个细微但重大的挑战：这些模型的特征图显示出网格状的伪影，这对ViTs在下游任务中的性能造成了不利影响。我们的研究将这个基本问题追溯到输入阶段的位置嵌入。为了解决这一问题，我们提出了一种新的噪声模型，该模型普遍适用于所有的ViT。具体来说，噪声模型将ViT输出分解为三个部分：一个没有噪声伪影的语义术语和两个以像素位置为条件的伪影相关术语。这种分解是通过在每幅图像的基础上加强与神经场的交叉视图特征一致性来实现的。这种逐图像优化过程从原始ViT输出中提取无伪影特征，为离线应用程序提供干净的特征。扩大了我们的解决方案的范围，以支持在线功能，我们引入了一种可学习的去噪器，直接从未处理的ViT输出中预测无伪影特征，这显示出对新数据的显著泛化能力，而无需对每张图像进行优化。我们的两阶段方法，称为去噪视觉转换器（DVT），不需要重新训练现有的预先训练的ViT，并且立即适用于任何基于转换器的架构。我们在各种具有代表性的ViT（DINO、MAE、DeiT III、EVA02、CLIP、DINOv2、DINOv2-reg）上评估了我们的方法。广泛的评估表明，我们的DVT在多个数据集（例如+3.84mIoU）的语义和几何任务中持续显著地改进了现有的最先进的通用模型。我们希望我们的研究将鼓励对ViT设计进行重新评估，特别是关于位置嵌入的天真使用。 et.al.|[2401.02957](http://arxiv.org/abs/2401.02957)|null|
|**2023-12-30**|**PlanarNeRF: Online Learning of Planar Primitives with Neural Radiance Fields**|从视觉数据中识别空间完整的平面基元是计算机视觉中的一项关键任务。现有的方法在很大程度上局限于2D片段恢复或简化3D结构，即使具有广泛的平面注释。我们提出了PlanarNeRF，这是一种能够通过在线学习检测密集3D平面的新框架。PlanarNeRF利用神经场表示，带来了三个主要贡献。首先，它利用并行的外观和几何知识增强了三维平面检测。其次，提出了一种轻量级的平面拟合模块来估计平面参数。第三，引入了一种具有更新机制的新的全局内存库结构，确保了跨帧一致性。PlanarNeRF的灵活架构使其能够在二维监督和自监督解决方案中发挥作用，在每种解决方案中，它都可以有效地从稀疏的训练信号中学习，显著提高训练效率。通过广泛的实验，我们证明了PlanarNeRF在各种场景下的有效性，并比现有工作有了显著的改进。 et.al.|[2401.00871](http://arxiv.org/abs/2401.00871)|null|
|**2024-01-01**|**Deblurring 3D Gaussian Splatting**|最近对辐射场的研究为具有照片级真实感渲染质量的新颖视图合成铺平了坚实的道路。然而，它们通常使用神经网络和体积绘制，这两种方法的训练成本很高，并且由于绘制时间长，阻碍了它们在各种实时应用中的广泛使用。最近，人们提出了一种基于3D高斯散射的方法来对3D场景进行建模，并在实时渲染图像的同时实现了显著的视觉质量。然而，如果训练图像模糊，则渲染质量会严重下降。模糊通常是由于镜头散焦、物体运动和相机抖动而产生的，它不可避免地会干扰干净图像的获取。先前的几项研究试图使用神经场从模糊的输入图像中渲染干净清晰的图像。然而，这些工作中的大多数仅设计用于基于体积渲染的神经辐射场，并不直接适用于基于光栅化的3D高斯散射方法。因此，我们提出了一种新的实时去模糊框架，即去模糊3D高斯散点，使用小型多层感知器（MLP）来操纵每个3D高斯的协方差来对场景模糊度进行建模。虽然去模糊的3D高斯飞溅仍然可以享受实时渲染，但它可以从模糊的图像中重建精细和清晰的细节。在基准上进行了各种实验，结果表明了我们的去模糊方法的有效性。定性结果可在https://benhenryl.github.io/Deblurring-3D-Gaussian-Splatting/ et.al.|[2401.00834](http://arxiv.org/abs/2401.00834)|null|
|**2023-12-22**|**Fluid Simulation on Neural Flow Maps**|我们介绍了神经流图，这是一种新的模拟方法，将新兴的隐式神经表示范式与基于流图理论的流体模拟相结合，以实现最先进的无粘流体现象模拟。我们设计了一种新的混合神经场表示，空间稀疏神经场（SSNF），它将小型神经网络与重叠、多分辨率和空间稀疏网格的金字塔相融合，以高精度紧凑地表示长期时空速度场。有了这个神经速度缓冲器，我们以机械对称的方式计算长期双向流图及其雅可比矩阵，以促进对现有解决方案的大幅精度提高。这些长程双向流图实现了低耗散的高平流精度，进而促进了高保真度的不可压缩流模拟，显示了复杂的旋涡结构。我们展示了我们的神经流体模拟在各种具有挑战性的模拟场景中的有效性，包括跳跃涡流、碰撞涡流、涡流重新连接，以及移动障碍物和密度差异产生的涡流。我们的例子表明，在能量守恒、视觉复杂性、对实验观测的遵守以及详细旋涡结构的保存方面，与现有方法相比，性能有所提高。 et.al.|[2312.14635](http://arxiv.org/abs/2312.14635)|null|

<p align=right>(<a href=#updated-on-20240204>back to top</a>)</p>

[contributors-shield]: https://img.shields.io/github/contributors/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[contributors-url]: https://github.com/Vincentqyw/cv-arxiv-daily/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[forks-url]: https://github.com/Vincentqyw/cv-arxiv-daily/network/members
[stars-shield]: https://img.shields.io/github/stars/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[stars-url]: https://github.com/Vincentqyw/cv-arxiv-daily/stargazers
[issues-shield]: https://img.shields.io/github/issues/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[issues-url]: https://github.com/Vincentqyw/cv-arxiv-daily/issues

