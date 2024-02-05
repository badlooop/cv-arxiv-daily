[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]

## Updated on 2024.02.05
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
|**2024-02-02**|**GaMeS: Mesh-Based Adapting and Modification of Gaussian Splatting**|近年来，已经引入了一系列基于神经网络的图像渲染方法。例如，广泛研究的神经辐射场（NeRF）依赖于神经网络来表示3D场景，从而允许从少量2D图像中合成逼真的视图。然而，大多数NeRF模型都受到长训练和推理时间的限制。相比之下，高斯散射（GS）是一种新颖的、最先进的技术，用于通过高斯分布近似点对图像像素的贡献来渲染3D场景中的点，从而保证快速训练和快速实时渲染。GS的一个缺点是，由于需要对几十万个高斯分量进行调节，因此缺乏定义明确的方法来进行调节。为了解决这个问题，我们引入了高斯网格飞溅（GaMeS）模型，这是网格和高斯分布的混合，它将所有高斯飞溅物固定在物体表面（网格）上。我们的方法的独特贡献是仅根据高斯飞溅在网格上的位置来定义高斯飞溅，从而允许在动画过程中自动调整位置、比例和旋转。因此，我们在实时生成高质量视图的过程中获得了高质量的渲染图。此外，我们证明，在没有预定义网格的情况下，可以在学习过程中微调初始网格。 et.al.|[2402.01459](http://arxiv.org/abs/2402.01459)|**[link](https://github.com/waczjoan/gaussian-mesh-splatting)**|
|**2024-02-01**|**360-GS: Layout-guided Panoramic Gaussian Splatting For Indoor Roaming**|近年来，三维高斯散射（3D-GS）以其实时性和照片真实性的渲染引起了人们的极大关注。这项技术通常将透视图像作为输入，并通过将一组3D椭圆高斯分布到图像平面上来优化它们，从而产生2D高斯。然而，将3D-GS应用于全景输入在使用2D高斯有效地将投影建模到 ${360^\circ}$图像的球面上方面存在挑战。在实际应用中，输入全景图往往是稀疏的，导致3D高斯图的初始化不可靠，并导致3D-GS质量下降。此外，由于无纹理平面（例如，墙和地板）的几何约束不足，3D-GS难以用椭圆高斯对这些平坦区域进行建模，导致在新视图中出现显著的浮动。为了解决这些问题，我们提出了360-GS，这是一种针对有限的全景输入集的新的$360^{\circ}$ 高斯飞溅。360-GS不是将3D高斯直接泼洒到球面上，而是将其投影到单位球体的切平面上，然后将其映射到球面投影。这种自适应使得能够使用高斯表示投影。我们通过利用全景图中的布局先验来指导360-GS的优化，这些先验易于获得，并包含关于室内场景的强大结构信息。我们的实验结果表明，360-GS允许全景渲染，并在新的视图合成中以更少的伪影优于最先进的方法，从而在室内场景中提供身临其境的漫游。 et.al.|[2402.00763](http://arxiv.org/abs/2402.00763)|null|
|**2024-02-01**|**StopThePop: Sorted Gaussian Splatting for View-Consistent Real-time Rendering**|高斯散射已经成为从不同领域的图像构建3D表示的一个突出模型。然而，3D高斯飞溅渲染管道的效率依赖于几个简化。值得注意的是，使用单个视图空间深度将高斯飞溅减少到2D会在视图旋转过程中引入爆裂和混合伪影。解决这个问题需要精确的每像素深度计算，但与全局排序操作相比，完整的每像素排序成本过高。在本文中，我们提出了一种新的分层光栅化方法，该方法以最小的处理开销系统地处理和剔除飞溅。我们的软件光栅化器有效地消除了弹出的伪影和视图不一致，通过定量和定性测量都证明了这一点。同时，我们的方法通过弹出来减少欺骗视图相关效果的可能性，确保了更真实的表示。尽管消除了作弊，但我们的方法在测试图像中获得了可比的定量结果，同时提高了运动中新视图合成的一致性。由于其设计，我们的分层方法平均只比原始的高斯飞溅慢4%。值得注意的是，强制执行一致性可以将Gaussian的数量减少大约一半，同时具有几乎相同的质量和视图一致性。因此，渲染性能几乎翻了一番，使我们的方法比原始的高斯Splatting快1.6倍，同时减少了50%的内存需求。 et.al.|[2402.00525](http://arxiv.org/abs/2402.00525)|null|
|**2024-01-31**|**Advances in 3D Generation: A Survey**|生成三维模型是计算机图形学的核心，也是几十年来研究的焦点。随着先进的神经表示和生成模型的出现，3D内容生成领域正在迅速发展，能够创建越来越高质量和多样化的3D模型。这一领域的快速发展使得我们很难跟上最近的所有发展。在这项调查中，我们旨在介绍3D生成方法的基本方法，并建立一个结构化的路线图，包括3D表示、生成方法、数据集和相应的应用程序。具体来说，我们介绍了用作3D生成主干的3D表示。此外，我们全面概述了快速增长的生成方法文献，按算法范式的类型进行分类，包括前馈生成、基于优化的生成、过程生成和生成新视图合成。最后，我们讨论了可用的数据集、应用程序和开放的挑战。我们希望这项调查能帮助读者探索这个令人兴奋的话题，并促进3D内容生成领域的进一步发展。 et.al.|[2401.17807](http://arxiv.org/abs/2401.17807)|null|
|**2024-01-27**|**Gaussian Splashing: Dynamic Fluid Synthesis with Gaussian Splatting**|我们展示了将基于物理的固体和流体动画与3D高斯飞溅（3DGS）相结合的可行性，以在使用3DGS重建的虚拟场景中创建新的效果。利用底层表示中高斯飞溅和基于位置的动力学（PBD）的一致性，我们以内聚的方式管理渲染、视图合成以及固体和流体的动力学。与高斯着色器类似，我们使用添加的法线增强每个高斯内核，将内核的方向与曲面法线对齐，以优化PBD模拟。这种方法有效地消除了由固体中的旋转变形引起的尖锐噪声。它还允许我们集成基于物理的渲染，以增强流体上的动态曲面反射。因此，我们的框架能够真实地再现动态流体上的曲面高光，并促进场景对象和新视图中流体之间的交互。有关更多信息，请访问我们的项目页面\url{https://amysteriouscat.github.io/GaussianSplashing/}. et.al.|[2401.15318](http://arxiv.org/abs/2401.15318)|null|
|**2024-01-26**|**3D Reconstruction and New View Synthesis of Indoor Environments based on a Dual Neural Radiance Field**|同时实现室内环境的3D重建和新视图合成具有广泛的应用，但在技术上非常具有挑战性。基于隐式神经函数的现有技术方法可以获得极好的三维重建结果，但它们在新视图合成方面的性能可能不令人满意。神经辐射场（NeRF）的令人兴奋的发展彻底改变了新的视图合成，然而，基于NeRF的模型可能无法重建干净的几何表面。我们开发了一种双神经辐射场（Du-NeRF），以同时实现高质量的几何重建和视图渲染。Du-NeRF包含两个几何场，一个从SDF场导出以便于几何重建，另一个从密度场导出以促进新视图合成。Du NeRF的一个创新特征是，它将视图无关分量与密度场解耦，并将其用作标签来监督SDF场的学习过程。这减少了形状辐射模糊性，并使几何图形和颜色在学习过程中相互受益。大量实验表明，Du-NeRF可以显著提高室内环境下新视图合成和3D重建的性能，并且在构建包含不服从多视图颜色一致性的精细几何图形的区域时尤其有效。 et.al.|[2401.14726](http://arxiv.org/abs/2401.14726)|null|
|**2024-01-23**|**IRIS: Inverse Rendering of Indoor Scenes from Low Dynamic Range Images**|尽管许多3D重建和新颖的视图合成方法允许从消费者相机轻松捕捉的多视图图像中真实地渲染场景，但它们在表示中烘焙照明，无法支持高级应用程序，如材质编辑、重新照明和虚拟对象插入。通过反向渲染重建基于物理的材料特性和照明有望实现此类应用。然而，大多数反向渲染技术都需要高动态范围（HDR）图像作为输入，这是大多数用户无法访问的设置。我们提出了一种方法，从多视图、低动态范围（LDR）图像中恢复场景的基于物理的材料特性和空间变化的HDR照明。我们在反向渲染管道中对LDR图像形成过程进行建模，并提出了一种新的材料、照明和相机响应模型的优化策略。与采用LDR或HDR输入的最先进的反向渲染方法相比，我们使用合成场景和真实场景来评估我们的方法。我们的方法优于以LDR图像作为输入的现有方法，并允许高度逼真的重新照明和对象插入。 et.al.|[2401.12977](http://arxiv.org/abs/2401.12977)|null|
|**2024-01-24**|**RGBD Objects in the Wild: Scaling Real-World 3D Object Learning from RGB-D Videos**|我们介绍了一种新的在野外捕获的RGB-D对象数据集，称为WildRGB-D。与大多数现有的仅带有RGB捕获的以对象为中心的真实世界数据集不同，深度通道的直接捕获允许更好的3D注释和更广泛的下游应用。WildRGB-D包括大型类别级RGB-D对象视频，这些视频是用iPhone 360度环绕对象拍摄的。它包含大约8500个记录对象和近20000个RGB-D视频，涉及46个常见对象类别。这些视频是在三种设置的不同杂乱背景下拍摄的，以覆盖尽可能多的真实世界场景：（i）一个视频中的单个对象；（ii）一个视频中的多个对象；以及（iii）在一个视频中具有静止手的对象。该数据集由对象遮罩、真实世界比例的相机姿态和RGBD视频中重建的聚合点云进行注释。我们用WildRGB-D对四个任务进行了基准测试，包括新颖的视图合成、相机姿态估计、物体6d姿态估计和物体表面重建。我们的实验表明，RGB-D对象的大规模捕获为推进3D对象学习提供了巨大的潜力。我们的项目页面是https://wildrgbd.github.io/. et.al.|[2401.12592](http://arxiv.org/abs/2401.12592)|null|
|**2024-01-23**|**Methods and strategies for improving the novel view synthesis quality of neural radiation field**|神经辐射场（NeRF）技术可以从2D图像中学习场景的3D隐式模型，并合成逼真的新视图图像。该技术得到了业界的广泛关注，具有良好的应用前景。针对NeRF图像渲染质量需要提高的问题，近三年来，许多研究人员提出了各种方法来提高渲染质量。对最新的相关论文进行了分类和综述，分析了质量改进背后的技术原理，并讨论了质量改进方法的未来发展方向。这项研究可以帮助研究人员快速了解该领域技术的现状和发展脉络，有助于激发更高效算法的发展，促进NeRF技术在相关领域的应用。 et.al.|[2401.12451](http://arxiv.org/abs/2401.12451)|null|
|**2024-01-22**|**HG3-NeRF: Hierarchical Geometric, Semantic, and Photometric Guided Neural Radiance Fields for Sparse View Inputs**|神经辐射场（NeRF）作为一种通过从离散观测中学习场景表示的新型视图合成范式，已经引起了人们的极大关注。然而，当面对稀疏视图输入时，NeRF表现出明显的性能退化，从而限制了其进一步的适用性。在这项工作中，我们介绍了层次几何、语义和光度引导的NeRF（HG3-NeRF），这是一种新的方法，可以解决上述限制，并增强不同视图中几何、语义内容和外观的一致性。我们提出了分层几何制导（HGG），将运动结构的附加（SfM），即稀疏深度先验，纳入场景表示中。与直接深度监督不同，HGG从局部几何区域到全局几何区域对体积点进行采样，减轻了深度先验中固有偏差引起的偏差。此外，我们从不同分辨率的图像中观察到的语义一致性的显著变化中获得了灵感，并提出了层次语义引导（HSG）来学习粗到细的语义内容，该内容对应于粗到细场景表示。实验结果表明，HG3-NeRF可以在不同的标准基准上优于其他最先进的方法，并实现稀疏视图输入的高保真度合成结果。 et.al.|[2401.11711](http://arxiv.org/abs/2401.11711)|null|

<p align=right>(<a href=#updated-on-20240205>back to top</a>)</p>

## 3D Reconstruction

|Publish Date|Title|Abstract|PDF|Code|
|---|---|---|---|---|
|**2024-02-02**|**Di-NeRF: Distributed NeRF for Collaborative Learning with Unknown Relative Poses**|未知环境的协作映射可以比单个机器人更快、更稳健地完成。然而，协作方法需要一个可扩展的分布式范式来处理通信问题。这项工作提出了一种全分布式算法，使一组机器人能够共同优化神经辐射场（NeRF）的参数。该算法涉及每个机器人训练的NeRF参数在网状网络上的通信，在网状网络中，每个机器人训练其NeRF，并且只能访问自己的视觉数据。此外，所有机器人的相对姿态都与模型参数一起进行了联合优化，从而能够使用未知的相对相机姿态进行映射。我们证明了多机器人系统可以受益于从多个NeRF优化的可微分和鲁棒的3D重建。在真实世界和合成数据上的实验证明了所提出的算法的有效性。实验视频和补充材料见项目网站(https://sites.google.com/view/di-nerf/home). et.al.|[2402.01485](http://arxiv.org/abs/2402.01485)|null|
|**2024-02-02**|**SiMA-Hand: Boosting 3D Hand-Mesh Reconstruction by Single-to-Multi-View Adaptation**|从RGB图像中估计3D手部网格是一个长期存在的问题，其中遮挡是最具挑战性的问题之一。当遮挡在图像空间中占主导地位时，针对该任务的现有尝试往往失败。在本文中，我们提出了SiMA Hand，旨在通过单视图到多视图自适应来提高网格重建性能。首先，我们设计了一个多视图手动重建器，通过在图像、关节和顶点级别全面采用特征融合来融合多个视图之间的信息。然后，我们介绍了一种配备SiMA的单视图手动重建器。尽管在推理时仅将一个视图作为输入，但通过在训练时从额外的视图中学习非遮挡知识，可以丰富单个视图重构器中的形状和方向特征，提高遮挡区域的重构精度。我们在Dex-YCB和HanCo基准上对具有挑战性的物体和自身造成的遮挡情况进行了实验，表明SiMA Hand始终实现了优于现有技术的性能。代码将于发布https://github.com/JoyboyWang/SiMA-HandPytorch。 et.al.|[2402.01389](http://arxiv.org/abs/2402.01389)|**[link](https://github.com/JoyboyWang/SiMA-Hand_Pytorch)**|
|**2024-02-02**|**DeepAAT: Deep Automated Aerial Triangulation for Fast UAV-based Mapping**|自动空中三角测量（AAT）旨在恢复图像姿态和重建稀疏点，在对地观测中发挥着关键作用。AAT在摄影测量领域拥有数十年的丰富研究遗产，已发展成为一个广泛应用于大规模无人机测绘的基础过程。尽管取得了进步，但经典的AAT方法仍然面临着效率低和稳健性有限等挑战。本文介绍了DeepAAT，一个专门为无人机图像AAT设计的深度学习网络。DeepAAT考虑了图像的空间和光谱特征，增强了其解决错误匹配对和准确预测图像姿态的能力。DeepAAT标志着AAT效率的重大飞跃，确保了全面的场景覆盖和精度。其处理速度超过增量AAT方法数百倍，超过全局AAT方法数十倍，同时保持了相当水平的重建精度。此外，DeepAAT的场景聚类和合并策略有助于大规模无人机图像的快速定位和姿态确定，即使在计算资源有限的情况下也是如此。实验结果表明，DeepAAT比传统的AAT方法有了实质性的改进，突出了其在基于无人机的三维重建任务的效率和准确性方面的潜力。为了造福摄影测量学会，DeepAAT的代码将发布在：https://github.com/WHU-USI3DV/DeepAAT. et.al.|[2402.01134](http://arxiv.org/abs/2402.01134)|**[link](https://github.com/whu-usi3dv/deepaat)**|
|**2024-02-02**|**Learning Which Side to Scan: Multi-View Informed Active Perception with Side Scan Sonar for Autonomous Underwater Vehicles**|自动水下航行器通常执行捕获目标的多个视图的勘测，以便为人类操作员或自动目标识别算法提供更多信息。在这项工作中，我们解决了选择信息量最大的视图的问题，这些视图可以最大限度地减少调查时间，同时最大限度地提高分类器的准确性。我们介绍了一种新的主动感知框架，用于使用侧扫声纳图像进行多视图自适应测量和重新获取。我们的框架通过使用自适应调查任务的图形公式来应对这一挑战。然后，我们使用图神经网络（GNN）对获取的声纳视图进行分类，并根据收集的数据选择下一个最佳视图。我们使用高保真侧扫声纳模拟器中的模拟调查来评估我们的方法。我们的结果表明，我们的方法能够在分类精度和调查效率方面超越最先进的方法。该框架是一种很有前途的方法，可用于更高效的自主任务，包括侧扫声纳，如水下勘探、海洋考古和环境监测。 et.al.|[2402.01106](http://arxiv.org/abs/2402.01106)|null|
|**2024-02-01**|**Enhanced fringe-to-phase framework using deep learning**|在边缘投影轮廓术（FPP）中，用有限数量的边缘图案实现稳健和准确的3D重建仍然是结构光3D成像中的一个挑战。传统的方法需要一组条纹图像，但仅使用一个或两个图案会使相位恢复和展开变得复杂。在这项研究中，我们介绍了SFNet，一种将两个条纹图像转换为绝对相位的对称融合网络。为了提高输出可靠性，我们的框架通过结合来自与用作输入的频率不同的条纹图像的信息来预测精细相位。这使我们能够仅用两个图像实现高精度。对比实验和消融研究验证了我们提出的方法的有效性。数据集和代码可在我们的项目页面上公开访问https://wonhoe-kim.github.io/SFNet. et.al.|[2402.00977](http://arxiv.org/abs/2402.00977)|null|
|**2024-02-01**|**Diffusion-based Light Field Synthesis**|光场（LFs）有助于在角度维度上记录全面的场景辐射，在3D重建、虚拟现实和计算摄影中有着广泛的应用。然而，由于主流的采集策略涉及手动采集或费力的软件合成，LF采集不可避免地耗时且资源密集。鉴于这一挑战，我们引入了LFdiff，这是一种简单而有效的基于扩散的生成框架，专门用于LF合成，它只采用单个RGB图像作为输入。LFdiff利用单目深度估计网络估计的视差，并结合了两个独特的组件：一个新的条件方案和一个为LF数据量身定制的噪声估计网络。具体来说，我们设计了一种位置感知扭曲条件方案，通过鲁棒的条件信号增强视图间几何学习。然后，我们提出了DistgUnet，一种基于解纠缠的噪声估计网络，以利用综合的LF表示。大量实验表明，LFdiff在合成视觉愉悦和视差可控的光场方面表现出色，具有增强的泛化能力。此外，综合结果证实了生成的LF数据的广泛适用性，涵盖了LF超分辨率和重新聚焦等应用。 et.al.|[2402.00575](http://arxiv.org/abs/2402.00575)|null|
|**2024-02-02**|**DARCS: Memory-Efficient Deep Compressed Sensing Reconstruction for Acceleration of 3D Whole-Heart Coronary MR Angiography**|三维冠状动脉磁共振血管造影术（CMRA）需要能够显著抑制严重欠采样采集的伪影的重建算法。虽然基于展开的深度重建方法在2D图像重建方面取得了最先进的性能，但它们在3D重建中的应用受到训练展开的网络所需的大量内存的阻碍。在这项研究中，我们提出了一种基于预训练的伪影估计网络的稀疏化变换的高效记忆深度压缩传感方法。其动机是，当输入图像没有伪影时，由训练有素的网络估计的伪影图像是稀疏的，而当输入图像受伪影影响时，稀疏度较低。因此，伪影估计网络可以用作固有的稀疏化变换。将所提出的方法称为基于去混叠正则化的压缩传感（DARCS），与传统的压缩传感方法、去混叠生成对抗性网络（DAGAN）、基于模型的深度学习（MoDL）和即插即用的三维CMRA加速方法进行了比较。结果表明，相对于比较方法，所提出的方法在重建质量上有很大的提高。此外，对于不同的欠采样率和噪声水平，所提出的方法得到了很好的推广。所提出的方法的内存使用量仅为MoDL所需内存使用量的63%。总之，所提出的方法在降低存储器负担的情况下提高了三维CMRA的重建质量。 et.al.|[2402.00320](http://arxiv.org/abs/2402.00320)|null|
|**2024-01-31**|**Local Feature Matching Using Deep Learning: A Survey**|局部特征匹配在计算机视觉领域有着广泛的应用，包括图像检索、三维重建和物体识别等领域。然而，由于视点和照明变化等因素，在提高匹配的准确性和稳健性方面仍然存在挑战。近年来，深度学习模型的引入引发了对局部特征匹配技术的广泛探索。这项工作的目的是提供局部特征匹配方法的全面概述。根据探测器的存在，这些方法分为两个关键部分。基于检测器的类别包括检测然后描述、联合检测和描述、描述然后检测以及基于图的技术等模型。相比之下，无检测器类别包括基于CNN、基于转换器和基于补丁的方法。我们的研究超越了方法分析，结合了对流行数据集和指标的评估，以促进对最先进技术的定量比较。本文还探讨了局部特征匹配在运动结构、遥感图像配准和医学图像配准等不同领域的实际应用，强调了其在各个领域的通用性和意义。最终，我们努力概述该领域当前面临的挑战，并提供未来的研究方向，从而为参与局部特征匹配及其互连领域的研究人员提供参考。 et.al.|[2401.17592](http://arxiv.org/abs/2401.17592)|null|
|**2024-01-30**|**Self-Supervised Representation Learning for Nerve Fiber Distribution Patterns in 3D-PLI**|要全面了解人脑的组织原理，除其他因素外，还需要对神经纤维结构进行可量化的描述。三维偏振光成像（3D-PLI）是一种显微镜成像技术，能够以高分辨率深入了解有髓神经纤维的细粒度组织。表征在3D-PLI中观察到的纤维结构的描述符将实现下游分析任务，如多模式相关性研究、聚类和映射。然而，在3D-PLI中对光纤结构进行独立于观察者的表征的最佳实践尚不可用。为此，我们提出应用一种完全数据驱动的方法，使用自监督表示学习来表征3D-PLI图像中的神经纤维结构。我们介绍了一种3D上下文对比学习（CL-3D）目标，该目标利用3D重建体积的组织学脑切片中纹理示例的空间邻域来对正配对进行采样以进行对比学习。我们将这种采样策略与专门设计的图像增强相结合，以获得对3D-PLI参数图中典型变化的鲁棒性。该方法已在一只vervet猴子大脑的3D重建枕叶中进行了演示。我们发现，提取的特征对神经纤维的不同配置高度敏感，但对组织学处理引起的连续脑切片之间的变化很强。我们展示了它们在检索同质光纤架构的集群和对光纤架构的特定组件（如U型光纤）的交互式选择模板执行数据挖掘方面的实际适用性。 et.al.|[2401.17207](http://arxiv.org/abs/2401.17207)|null|
|**2024-01-30**|**Physical Priors Augmented Event-Based 3D Reconstruction**|三维神经隐式表示在许多机器人应用中起着重要的作用。然而，当只有事件流可用时，由于稀疏性和信息缺乏，从真实的事件数据重建神经辐射场（NeRF）仍然是一个挑战。在本文中，我们利用事件数据背后的运动、几何和密度先验来施加强大的物理约束，以增强NeRF训练。所提出的新管道可以直接受益于这些先验，以在没有额外输入的情况下重建3D场景。此外，我们提出了一种新的基于密度引导的基于补丁的采样策略，用于鲁棒和高效的学习，它不仅加速了训练过程，而且有助于局部几何的表达。更重要的是，我们建立了第一个用于基于事件的3D重建的大型数据集，其中包含101个具有各种材料和几何形状的对象，以及所有相机视点的图像和深度图的基本情况，这大大促进了相关领域的其他研究。代码和数据集将在https://github.com/Mercerai/PAEv3d. et.al.|[2401.17121](http://arxiv.org/abs/2401.17121)|**[link](https://github.com/mercerai/paev3d)**|

<p align=right>(<a href=#updated-on-20240205>back to top</a>)</p>

## Diffusion

|Publish Date|Title|Abstract|PDF|Code|
|---|---|---|---|---|
|**2024-02-02**|**Revealing crucial effects of reservoir environment and hydrocarbon fractions on fluid behaviour in kaolinite pores**|碳氢化合物（HC）和粘土表面的相互作用是页岩储层内流体行为的原因。这些相互作用受到HC成分多样性和环境条件变化的影响。本研究考察了具有两个不同基面的高岭石粘土与一系列HC之间的相互作用。我们评估了各种分子结构、官能团和环境条件（重点是储层温度和压力范围）对HC的吸附选择性、表面堆积、分子排列和取向以及扩散的影响。分子相互作用能的分析提供了HCs在不同高岭石表面吸附机制的定量说明。我们的研究结果表明，分子构型、官能团和空间效应决定了不同高岭石表面HCs的分布模式。不同碳氢化合物与高岭石相互作用能的差异揭示了不同碳氢化合物的吸附强度，其顺序为沥青质>杂原子碳氢化合物>饱和碳氢化合物>芳香碳氢化合物。此外，我们观察到吸附特性对温度高度敏感；随着温度的升高，吸附量显著减少。超过一定阈值后，压力升高对HCs流体行为的影响是不可忽略的，并且与分子堆积和迁移率降低有关。基于实际地质特征的模拟结果表明，受竞争吸附和粘土表面相互作用的影响，碳氢化合物组分在不同高岭石表面上的吸附差异显著。极性表面主要由异原子HC占据，而在非极性表面上，沥青质和重饱和HC形成多层吸附结构，分子与表面平行排列。 et.al.|[2402.01633](http://arxiv.org/abs/2402.01633)|null|
|**2024-02-02**|**NeuroCine: Decoding Vivid Video Sequences from Human Brain Activties**|为了理解人类大脑视觉处理的复杂性，从大脑活动中重建动态视觉体验是一项具有挑战性但引人入胜的努力。尽管最近的进展在从非侵入性大脑记录重建静态图像方面取得了成功，但将连续的大脑活动转换为视频格式的领域仍有待探索。在这项工作中，我们介绍了NeuroCine，这是一种新的双阶段框架，旨在解决解码fMRI数据的固有挑战，如噪声、空间冗余和时间滞后。该框架提出了用于对比学习的fMRI表示的基于空间掩蔽和时间插值的增强，以及用于视频生成的通过依赖先验噪声增强的扩散模型。在公开可用的功能磁共振成像数据集上进行测试，我们的方法显示出有希望的结果，在解码功能磁共振图像数据集中三名受试者的大脑活动方面，通过SSIM测量，分别以 ${20.97\%}、${31.00\%}和$ {12.30\%}的显著优势优于先前最先进的模型。此外，我们的注意力分析表明，该模型与现有的大脑结构和功能一致，表明其生物学合理性和可解释性。 et.al.|[2402.01590](http://arxiv.org/abs/2402.01590)|null|
|**2024-02-02**|**Transformation semigroups and their applications**|本章介绍了变换半群及其应用。我们从克莱因基于变换群不变量的几何方法开始。然后我们在化学和经典力学中介绍对称群。接下来我们介绍变换的单参数半群及其在遍历理论中的应用。我们主要研究算子的单参数半群，特别是随机半群。我们给出了关于它们的存在和长期行为的一般结果。我们还给出了与马尔可夫链、扩散和带跳过程有关的单参数半群的例子。我们着重讨论算子的半群在生物学中的应用。除其他外，我们研究的模型包括：DNA进化；红细胞数量增长；基因表达；细胞周期；细菌和昆虫的运动。我们还考虑了具有随机噪声的模型和不同的种群模型。 et.al.|[2402.01572](http://arxiv.org/abs/2402.01572)|null|
|**2024-02-02**|**Boximator: Generating Rich and Controllable Motions for Video Synthesis**|生成丰富可控的运动是视频合成中的一个关键挑战。我们提出了Boximator，一种新的细粒度运动控制方法。Boximator引入了两种约束类型：硬框和软框。用户使用硬框选择条件框中的对象，然后使用任意类型的框粗略或严格地定义对象在未来帧中的位置、形状或运动路径。Boximator的功能是作为现有视频扩散模型的插件。它的训练过程通过冻结原始权重和只训练控制模块来保留基本模型的知识。为了应对训练挑战，我们引入了一种新的自跟踪技术，该技术大大简化了盒对象相关性的学习。从经验上讲，Boximator实现了最先进的视频质量（FVD）分数，在两个基本模型的基础上进行了改进，并在引入盒子约束后进一步增强。通过边界框对齐度量的急剧增加验证了其鲁棒的运动可控性。人工评估还表明，用户更喜欢Boximator生成结果，而不是基本模型。 et.al.|[2402.01566](http://arxiv.org/abs/2402.01566)|null|
|**2024-02-02**|**Resolution dependence of most probable pathways with state-dependent diffusivity**|最近的实验通过观察时空中半径为 $R$的管道内的生存概率，探索了随机系统中轨迹的相对可能性。我们在这里测量了波纹通道中胶体颗粒的这种概率，对应于具有状态相关扩散率的双稳态势。与之前对状态无关噪声的研究结果相反，我们发现最可能的途径随着管道半径$R$的改变而发生质的变化。我们通过计算过阻尼Langevin动力学预测的生存概率来解释这一点。在足够高的分辨率（足够小的$R$）下，生存概率仅取决于扩散率的变化，与确定性力无关；有限的$R$修正产生了Onsager Machlup作用的推广。作为推论，生存概率的比率是奇异的，如$R\到0$ ，但变为正则的，并由经典的Onsager Machlup作用描述，仅在状态无关噪声的特殊情况下。 et.al.|[2402.01559](http://arxiv.org/abs/2402.01559)|null|
|**2024-02-02**|**The galactic bubbles of starburst galaxies The influence of galactic large-scale magnetic fields**|上下文星爆星系（SBG）的星系风在千秒差距尺度上产生了引人注目的结构。然而，这些巨大风气泡的演变和形状，以及它们产生的冲击的性质，还没有完全了解。目的。我们的目的是了解SBG的星系风的形状，特别关注大尺度磁场在星系风膨胀气泡的动力学演化中的作用。此外，我们的目标是探索在这些系统中，有效粒子加速的条件在哪里得到满足。方法。我们使用AMRVAC代码（自适应网格细化通用平流代码）对银河系介质密度剖面和磁化的各种配置进行了磁流体动力学模拟。后果我们观察到，星系风在其中膨胀的大尺度磁场会影响膨胀气泡的结构和演化。然而，在M82等星暴星系中观察到的典型结构不能仅仅用所考虑的磁场结构来解释。这突出了其他因素的重要性，如星系盘，在形成星系气泡。此外，在我们研究的所有磁化情况下，膨胀气泡产生的前向波只会产生压缩波，而风终止冲击具有高马赫数，使其成为扩散冲击加速度高达 $\sim 10^｛2｝$ PeV的一个有前途的场所。从我们的模型中生成的合成X射线图像揭示了气泡周围延伸至2kpc的包络，这可能对应于从M82的平面几何结构中观察到的偏振发射，以及气泡内部对应于震荡星系风的大结构。 et.al.|[2402.01541](http://arxiv.org/abs/2402.01541)|null|
|**2024-02-02**|**Low-Resource Cross-Domain Singing Voice Synthesis via Reduced Self-Supervised Speech Representations**|在本文中，我们提出了一种仅基于文本和语音数据训练的歌声合成模型Karaoker SSL，作为一种典型的多扬声器声学模型。它是一种低资源的管道，不使用任何端到端的歌唱数据，因为它的声码器也基于语音数据进行训练。Karaoker SSL以无监督的方式受到自监督语音表示的制约。我们通过只选择它们的任务相关维度的子集来预处理这些表示。调节模块在训练过程中通过多任务间接引导捕捉风格信息。这是通过基于Conformer的模块实现的，该模块根据声学模型的输出预测音高。因此，Karaoker SSL允许在不依赖手工制作和特定领域功能的情况下进行人声合成。对于文本对齐或歌词时间戳也没有要求。为了改进语音质量，我们使用了一个U-Net鉴别器，该鉴别器以目标说话者为条件，并遵循扩散GAN训练方案。 et.al.|[2402.01520](http://arxiv.org/abs/2402.01520)|null|
|**2024-02-02**|**Cross-view Masked Diffusion Transformers for Person Image Synthesis**|我们提出了X-MDPT（Cross-view Masked Diffusion Prediction Transformers），这是一种新的扩散模型，设计用于姿势引导的人体图像生成。X-MDPT通过使用在潜在斑块上操作的掩蔽扩散变压器来区分自己，这与现有作品中常用的Unet结构不同。该模型包括三个关键模块：1）去噪扩散转换器，2）将条件合并为扩散过程的单个向量的聚合网络，以及3）利用来自参考图像的语义信息增强表示学习的掩码交叉预测模块。X-MDPT展示了可扩展性，通过更大的模型改进了FID、SSIM和LPIPS。尽管设计简单，但我们的模型在DeepFashion数据集上优于最先进的方法，同时在训练参数、训练时间和推理速度方面表现出效率。我们的紧凑型33MB模型实现了7.42的FID，超过了之前的Unet潜在扩散方法（FID 8.07），只使用了11美元\倍的参数。我们的最佳模型使用 $\frac｛2｝｛3｝$的参数超过了基于像素的扩散，并实现了$5.43\times$ 更快的推理。 et.al.|[2402.01516](http://arxiv.org/abs/2402.01516)|null|
|**2024-02-02**|**Binomial-tree approximation for time-inconsistent stopping**|对于一维扩散设置中的时间不一致停止，我们研究了如何使用离散时间模型来近似原始问题。特别地，我们考虑由连续时间问题中的所有温和均衡引起的值函数 $V（\cdot）$，以及与时间步长为$h$的二项式树设置中的均衡相关的值$V^h（\cdot）$。我们证明了$\lim_｛h\rightarrow 0+｝V^h\leq V$。我们提供了一个例子，表明精确收敛可能会失败。然后，我们放松平衡集，并考虑二项式树模型中由$\varepsilon$-平衡引起的值$V^h｛\varepsilion｝（\cdot）$。我们证明了$ \lim_｛\varepsilon\rightarrow 0+｝\lim_。 et.al.|[2402.01482](http://arxiv.org/abs/2402.01482)|null|
|**2024-02-02**|**SVI solutions to stochastic nonlinear diffusion equations on general measure spaces**|我们建立了乘性噪声驱动的随机非线性（可能是多值）扩散方程解的存在性和唯一性的框架，其中漂移算子 $L$是有限测度空间$（E，\mathcal｛B｝，\mu）$上瞬态Dirichlet形式的生成元，并且初始值为$\mathcal{F}_e^*$，它是一个扩展的瞬态狄利克雷空间的对偶空间$L$和$\mathcal{F}_e^*在经典情况下，$分别替换拉普拉斯算子$\Delta$和$H^｛-1｝$。该框架包括随机快速扩散方程、随机分数阶快速扩散方程和张模型，并适用于$E$是流形、分形或图的情况。此外，我们的结果适用于运算符$-f（-L）$，其中$f$是Bernstein函数，例如$f（\lambda）=\lambda^\alpha$或$f（\llambda）=（\lambda+1）^\alpha-1$，$0<\alpha<1$ 。 et.al.|[2402.01479](http://arxiv.org/abs/2402.01479)|null|

<p align=right>(<a href=#updated-on-20240205>back to top</a>)</p>

## NeRF

|Publish Date|Title|Abstract|PDF|Code|
|---|---|---|---|---|
|**2024-01-31**|**BlockFusion: Expandable 3D Scene Generation using Latent Tri-plane Extrapolation**|我们介绍了BlockFusion，这是一种基于扩散的模型，它将3D场景生成为单元块，并无缝地合并新的块来扩展场景。BlockFusion使用从完整的3D场景网格中随机裁剪的3D块的数据集进行训练。通过逐块拟合，所有训练块都被转换为混合神经场：具有包含几何特征的三平面，然后是用于解码有符号距离值的多层感知器（MLP）。采用变分自动编码器将三平面压缩到潜在的三平面空间中，在该空间上进行去噪扩散处理。应用于潜在表示的扩散允许高质量和多样化的3D场景生成。要在生成过程中扩展场景，只需附加空块以与当前场景重叠，并外推现有的潜在三平面以填充新块。外推是通过在去噪迭代过程中使用来自重叠三平面的特征样本来调节生成过程来完成的。潜在的三平面外推法产生语义和几何上有意义的过渡，与现有场景和谐融合。2D布局调节机制用于控制场景元素的放置和布置。实验结果表明，BlockFusion能够在室内和室外场景中生成具有前所未有的高质量形状的多样化、几何一致和无边界的大型3D场景。 et.al.|[2401.17053](http://arxiv.org/abs/2401.17053)|null|
|**2024-01-26**|**Learning Neural Radiance Fields of Forest Structure for Scalable and Fine Monitoring**|这项工作利用神经辐射场和遥感技术用于林业应用。在这里，我们展示了神经辐射场为改进森林监测中现有的遥感方法提供了广泛的可能性。我们提出的实验证明了它们的潜力：（1）表达森林三维结构的精细特征，（2）融合可用的遥感模式，以及（3）改进三维结构衍生的森林指标。总之，这些特性使神经场成为一种有吸引力的计算工具，具有进一步提高森林监测程序的可扩展性和准确性的巨大潜力。 et.al.|[2401.15029](http://arxiv.org/abs/2401.15029)|null|
|**2024-01-25**|**Learning Robust Generalizable Radiance Field with Visibility and Feature Augmented Point Representation**|本文介绍了广义神经辐射场（NeRF）的一种新范式。以前的通用NeRF方法将多视点立体技术与基于图像的神经渲染相结合进行泛化，产生了令人印象深刻的结果，同时存在三个问题。首先，遮挡常常导致不一致的特征匹配。然后，由于采样点和粗略特征聚合的单独过程，它们在几何不连续性和局部尖锐形状中传递失真和伪影。第三，当源视图离目标视图不够近时，它们基于图像的表示会发生严重退化。为了应对挑战，我们提出了第一个基于点而不是基于图像的渲染构建可泛化神经场的范式，我们称之为可泛化神经点场（GPF）。我们的方法通过几何先验显式地建模可见性，并用神经特征增强它们。我们提出了一种新的非均匀对数采样策略，以提高渲染速度和重建质量。此外，我们提出了一种可学习的内核，该内核在空间上增加了用于特征聚合的特征，减轻了几何结构急剧变化的地方的失真。此外，我们的表现很容易被操纵。实验表明，在泛化和微调设置中，我们的模型可以在三个数据集上提供比所有对应模型和基准更好的几何结构、视图一致性和渲染质量，初步证明了可泛化NeRF新范式的潜力。 et.al.|[2401.14354](http://arxiv.org/abs/2401.14354)|null|
|**2024-01-24**|**Unified neural field theory of brain dynamics underlying oscillations in Parkinson's disease and generalized epilepsies**|通过皮质丘脑基底神经节（CTBG）系统的神经场模型，联合探讨了帕金森病（PD）和全身性癫痫的病理同步神经振荡的机制。基底神经节（BG）被近似为一个单一的有效群体，并分析了它们在调节振荡皮质丘脑（CT）动力学中的作用，反之亦然。除了正常的脑电图节律外，模型中还存在4 Hz和20 Hz左右的增强活动，这与PD的特征频率一致。这些节律是由BG和CT人群之间回路中的共振引起的，类似于先前CT模型中潜在的癫痫振荡。多巴胺耗竭被认为削弱了对PD中这些共振的抑制，网络连接解释了在4-8Hz和20Hz左右BG、丘脑和皮层活动之间的显著一致性。丘脑网状核（TRN）和BG的传入和传出连接位点之间的相似性预测低多巴胺对应于强直-阵挛（大发作）癫痫发作的可能性降低，这与实验结果一致。此外，该模型预测，与实验结果相匹配的低多巴胺水平会增加缺席（轻微）癫痫发作的可能性。与其他CTBG建模研究一致，当传入和传出BG与CT系统的连接增强时，表现出对缺席发作活动的抑制。BG被证明在强直-阵挛发作状态附近抑制CTBG系统的活性，从而深入了解BG回路中目前治疗的疗效。TRN的睡眠状态也被发现可以抑制病理性PD活动匹配观察。总的来说，这些发现证明了广泛性癫痫和帕金森病的相干振荡之间有很强的相似性，并为可能的合并症提供了见解。 et.al.|[2401.13467](http://arxiv.org/abs/2401.13467)|null|
|**2024-01-17**|**Reproducibility via neural fields of visual illusions induced by localized stimuli**|本文研究了Billock和Tsou[PNAS，2007]使用Amari型神经场的可控性对初级视皮层（V1）的皮层活动进行建模的实验复制，重点关注中央凹或外周视野中的规则漏斗模式。其目的是理解和模拟在这些实验中观察到的视觉现象，强调其非线性性质。这项研究包括设计模拟Billock和Tsou实验中视觉刺激的感官输入。然后从理论和数值上研究这些输入引起的后图像，以确定它们复制实验观察到的视觉效果的能力。这项研究的一个关键方面是研究神经反应的非线性性质所引起的影响。特别是，通过强调兴奋性和抑制性神经元在某些视觉现象出现中的重要性，这项研究表明，这两种类型的神经元活动的相互作用在视觉过程中发挥着重要作用，挑战了后者主要由兴奋性活动单独驱动的假设。 et.al.|[2401.09108](http://arxiv.org/abs/2401.09108)|null|
|**2024-01-12**|**Motion2VecSets: 4D Latent Vector Set Diffusion for Non-rigid Shape Reconstruction and Tracking**|我们介绍了Motion2VecSets，这是一种用于从点云序列进行动态曲面重建的4D扩散模型。虽然现有的最先进的方法已经证明在使用神经场表示重建非刚性对象方面取得了成功，但传统的前馈网络遇到了来自噪声、部分或稀疏点云的模糊观测的挑战。为了应对这些挑战，我们引入了一种扩散模型，该模型通过压缩潜在表示的迭代去噪过程来显式学习非刚性对象的形状和运动分布。当处理模糊输入时，基于扩散的先验能够进行更合理和概率的重建。我们用潜在向量集参数化4D动力学，而不是使用全局潜在。这种新颖的4D表示使我们能够学习局部表面形状和变形模式，从而实现更准确的非线性运动捕捉，并显著提高对看不见的运动和身份的可推广性。对于更具时间连贯性的目标跟踪，我们同步地对变形潜集进行去噪，并在多个帧之间交换信息。为了避免计算开销，我们设计了一个交错的空间和时间注意力块，以沿着空间和时间域交替聚集变形潜伏期。与最先进的方法进行了广泛的比较，证明了我们的Motion2VenSets在从各种不完美的观测进行4D重建方面的优势，特别是在从DeformingThings4D Animals数据集上的稀疏点云重建看不见的个体方面，与CaDex相比，交集优于并集（IoU）提高了19%。更多详细信息，请访问https://vveicao.github.io/projects/Motion2VecSets/. et.al.|[2401.06614](http://arxiv.org/abs/2401.06614)|null|
|**2024-01-05**|**Denoising Vision Transformers**|我们深入研究了视觉转换器（ViTs）固有的一个细微但重大的挑战：这些模型的特征图显示出网格状的伪影，这对ViTs在下游任务中的性能造成了不利影响。我们的研究将这个基本问题追溯到输入阶段的位置嵌入。为了解决这一问题，我们提出了一种新的噪声模型，该模型普遍适用于所有的ViT。具体来说，噪声模型将ViT输出分解为三个部分：一个没有噪声伪影的语义术语和两个以像素位置为条件的伪影相关术语。这种分解是通过在每幅图像的基础上加强与神经场的交叉视图特征一致性来实现的。这种逐图像优化过程从原始ViT输出中提取无伪影特征，为离线应用程序提供干净的特征。扩大了我们的解决方案的范围，以支持在线功能，我们引入了一种可学习的去噪器，直接从未处理的ViT输出中预测无伪影特征，这显示出对新数据的显著泛化能力，而无需对每张图像进行优化。我们的两阶段方法，称为去噪视觉转换器（DVT），不需要重新训练现有的预先训练的ViT，并且立即适用于任何基于转换器的架构。我们在各种具有代表性的ViT（DINO、MAE、DeiT III、EVA02、CLIP、DINOv2、DINOv2-reg）上评估了我们的方法。广泛的评估表明，我们的DVT在多个数据集（例如+3.84mIoU）的语义和几何任务中持续显著地改进了现有的最先进的通用模型。我们希望我们的研究将鼓励对ViT设计进行重新评估，特别是关于位置嵌入的天真使用。 et.al.|[2401.02957](http://arxiv.org/abs/2401.02957)|null|
|**2023-12-30**|**PlanarNeRF: Online Learning of Planar Primitives with Neural Radiance Fields**|从视觉数据中识别空间完整的平面基元是计算机视觉中的一项关键任务。现有的方法在很大程度上局限于2D片段恢复或简化3D结构，即使具有广泛的平面注释。我们提出了PlanarNeRF，这是一种能够通过在线学习检测密集3D平面的新框架。PlanarNeRF利用神经场表示，带来了三个主要贡献。首先，它利用并行的外观和几何知识增强了三维平面检测。其次，提出了一种轻量级的平面拟合模块来估计平面参数。第三，引入了一种具有更新机制的新的全局内存库结构，确保了跨帧一致性。PlanarNeRF的灵活架构使其能够在二维监督和自监督解决方案中发挥作用，在每种解决方案中，它都可以有效地从稀疏的训练信号中学习，显著提高训练效率。通过广泛的实验，我们证明了PlanarNeRF在各种场景下的有效性，并比现有工作有了显著的改进。 et.al.|[2401.00871](http://arxiv.org/abs/2401.00871)|null|
|**2024-01-01**|**Deblurring 3D Gaussian Splatting**|最近对辐射场的研究为具有照片级真实感渲染质量的新颖视图合成铺平了坚实的道路。然而，它们通常使用神经网络和体积绘制，这两种方法的训练成本很高，并且由于绘制时间长，阻碍了它们在各种实时应用中的广泛使用。最近，人们提出了一种基于3D高斯散射的方法来对3D场景进行建模，并在实时渲染图像的同时实现了显著的视觉质量。然而，如果训练图像模糊，则渲染质量会严重下降。模糊通常是由于镜头散焦、物体运动和相机抖动而产生的，它不可避免地会干扰干净图像的获取。先前的几项研究试图使用神经场从模糊的输入图像中渲染干净清晰的图像。然而，这些工作中的大多数仅设计用于基于体积渲染的神经辐射场，并不直接适用于基于光栅化的3D高斯散射方法。因此，我们提出了一种新的实时去模糊框架，即去模糊3D高斯散点，使用小型多层感知器（MLP）来操纵每个3D高斯的协方差来对场景模糊度进行建模。虽然去模糊的3D高斯飞溅仍然可以享受实时渲染，但它可以从模糊的图像中重建精细和清晰的细节。在基准上进行了各种实验，结果表明了我们的去模糊方法的有效性。定性结果可在https://benhenryl.github.io/Deblurring-3D-Gaussian-Splatting/ et.al.|[2401.00834](http://arxiv.org/abs/2401.00834)|null|
|**2023-12-22**|**Fluid Simulation on Neural Flow Maps**|我们介绍了神经流图，这是一种新的模拟方法，将新兴的隐式神经表示范式与基于流图理论的流体模拟相结合，以实现最先进的无粘流体现象模拟。我们设计了一种新的混合神经场表示，空间稀疏神经场（SSNF），它将小型神经网络与重叠、多分辨率和空间稀疏网格的金字塔相融合，以高精度紧凑地表示长期时空速度场。有了这个神经速度缓冲器，我们以机械对称的方式计算长期双向流图及其雅可比矩阵，以促进对现有解决方案的大幅精度提高。这些长程双向流图实现了低耗散的高平流精度，进而促进了高保真度的不可压缩流模拟，显示了复杂的旋涡结构。我们展示了我们的神经流体模拟在各种具有挑战性的模拟场景中的有效性，包括跳跃涡流、碰撞涡流、涡流重新连接，以及移动障碍物和密度差异产生的涡流。我们的例子表明，在能量守恒、视觉复杂性、对实验观测的遵守以及详细旋涡结构的保存方面，与现有方法相比，性能有所提高。 et.al.|[2312.14635](http://arxiv.org/abs/2312.14635)|null|

<p align=right>(<a href=#updated-on-20240205>back to top</a>)</p>

[contributors-shield]: https://img.shields.io/github/contributors/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[contributors-url]: https://github.com/Vincentqyw/cv-arxiv-daily/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[forks-url]: https://github.com/Vincentqyw/cv-arxiv-daily/network/members
[stars-shield]: https://img.shields.io/github/stars/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[stars-url]: https://github.com/Vincentqyw/cv-arxiv-daily/stargazers
[issues-shield]: https://img.shields.io/github/issues/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[issues-url]: https://github.com/Vincentqyw/cv-arxiv-daily/issues

