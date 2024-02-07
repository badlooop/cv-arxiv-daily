[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]

## Updated on 2024.02.07
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
|**2024-02-05**|**4D Gaussian Splatting: Towards Efficient Novel View Synthesis for Dynamic Scenes**|我们考虑动态场景的新视图合成（NVS）问题。最近的神经方法已经为静态3D场景实现了异常的NVS结果，但对4D时变场景的扩展仍然是不平凡的。先前的工作通常通过学习规范空间加上隐式或显式变形场来编码动力学，这些变形场在突发运动或捕捉高保真渲染等具有挑战性的场景中很困难。在本文中，我们介绍了4D高斯散射（4DGS），这是一种用各向异性4D XYZT高斯表示动态场景的新方法，其灵感来自于3D高斯散射在静态场景中的成功。我们通过对4D高斯进行时间切片来对每个时间戳的动力学进行建模，4D高斯自然构成动态3D高斯，并可以无缝投影到图像中。作为一种明确的时空表示，4DGS展示了对复杂动力学和精细细节建模的强大能力，尤其是对于具有突然运动的场景。我们在高度优化的CUDA加速框架中进一步实现了我们的时间切片和飞溅技术，在RTX 3090 GPU上实现了高达277 FPS的实时推理渲染速度，在RTX4090 GPU上达到了583 FPS的实时推断渲染速度。对不同运动场景的严格评估显示了4DGS的卓越效率和有效性，它在数量和质量上都始终优于现有方法。 et.al.|[2402.03307](http://arxiv.org/abs/2402.03307)|null|
|**2024-02-05**|**ViewFusion: Learning Composable Diffusion Models for Novel View Synthesis**|深度学习为新视图合成的老问题提供了丰富的新方法，从基于神经辐射场（NeRF）的方法到端到端风格的架构。每种方法都有特定的优势，但在适用性方面也有特定的局限性。这项工作介绍了ViewFusion，这是一种最先进的端到端生成新视图合成方法，具有无与伦比的灵活性。ViewFusion包括同时将扩散去噪步骤应用于场景的任意数量的输入视图，然后将为每个视图获得的噪声梯度与（推断的）像素加权掩码相结合，确保对于目标场景的每个区域，只考虑信息量最大的输入视图。我们的方法通过以下方式解决了先前方法的几个局限性：（1）可在多个场景和对象类中进行训练和推广，（2）在训练和测试时自适应地获取可变数量的无姿态视图，（3）即使在严重不确定的条件下也能生成合理的视图（由于其生成性）——同时生成质量与最先进的方法相当甚至更好的视图。局限性包括没有生成场景的3D嵌入，导致推理速度相对较慢，并且我们的方法仅在相对较小的数据集NMR上进行测试。代码可用。 et.al.|[2402.02906](http://arxiv.org/abs/2402.02906)|**[link](https://github.com/bronemos/view-fusion)**|
|**2024-02-02**|**GaMeS: Mesh-Based Adapting and Modification of Gaussian Splatting**|近年来，已经引入了一系列基于神经网络的图像渲染方法。例如，广泛研究的神经辐射场（NeRF）依赖于神经网络来表示3D场景，从而允许从少量2D图像中合成逼真的视图。然而，大多数NeRF模型都受到长训练和推理时间的限制。相比之下，高斯散射（GS）是一种新颖的、最先进的技术，用于通过高斯分布近似点对图像像素的贡献来渲染3D场景中的点，从而保证快速训练和快速实时渲染。GS的一个缺点是，由于需要对几十万个高斯分量进行调节，因此缺乏定义明确的方法来进行调节。为了解决这个问题，我们引入了高斯网格飞溅（GaMeS）模型，这是网格和高斯分布的混合，它将所有高斯飞溅物固定在物体表面（网格）上。我们的方法的独特贡献是仅根据高斯飞溅在网格上的位置来定义高斯飞溅，从而允许在动画过程中自动调整位置、比例和旋转。因此，我们在实时生成高质量视图的过程中获得了高质量的渲染图。此外，我们证明，在没有预定义网格的情况下，可以在学习过程中微调初始网格。 et.al.|[2402.01459](http://arxiv.org/abs/2402.01459)|**[link](https://github.com/waczjoan/gaussian-mesh-splatting)**|
|**2024-02-01**|**360-GS: Layout-guided Panoramic Gaussian Splatting For Indoor Roaming**|近年来，三维高斯散射（3D-GS）以其实时性和照片真实性的渲染引起了人们的极大关注。这项技术通常将透视图像作为输入，并通过将一组3D椭圆高斯分布到图像平面上来优化它们，从而产生2D高斯。然而，将3D-GS应用于全景输入在使用2D高斯有效地将投影建模到 ${360^\circ}$图像的球面上方面存在挑战。在实际应用中，输入全景图往往是稀疏的，导致3D高斯图的初始化不可靠，并导致3D-GS质量下降。此外，由于无纹理平面（例如，墙和地板）的几何约束不足，3D-GS难以用椭圆高斯对这些平坦区域进行建模，导致在新视图中出现显著的浮动。为了解决这些问题，我们提出了360-GS，这是一种针对有限的全景输入集的新的$360^{\circ}$ 高斯飞溅。360-GS不是将3D高斯直接泼洒到球面上，而是将其投影到单位球体的切平面上，然后将其映射到球面投影。这种自适应使得能够使用高斯表示投影。我们通过利用全景图中的布局先验来指导360-GS的优化，这些先验易于获得，并包含关于室内场景的强大结构信息。我们的实验结果表明，360-GS允许全景渲染，并在新的视图合成中以更少的伪影优于最先进的方法，从而在室内场景中提供身临其境的漫游。 et.al.|[2402.00763](http://arxiv.org/abs/2402.00763)|null|
|**2024-02-01**|**StopThePop: Sorted Gaussian Splatting for View-Consistent Real-time Rendering**|高斯散射已经成为从不同领域的图像构建3D表示的一个突出模型。然而，3D高斯飞溅渲染管道的效率依赖于几个简化。值得注意的是，使用单个视图空间深度将高斯飞溅减少到2D会在视图旋转过程中引入爆裂和混合伪影。解决这个问题需要精确的每像素深度计算，但与全局排序操作相比，完整的每像素排序成本过高。在本文中，我们提出了一种新的分层光栅化方法，该方法以最小的处理开销系统地处理和剔除飞溅。我们的软件光栅化器有效地消除了弹出的伪影和视图不一致，通过定量和定性测量都证明了这一点。同时，我们的方法通过弹出来减少欺骗视图相关效果的可能性，确保了更真实的表示。尽管消除了作弊，但我们的方法在测试图像中获得了可比的定量结果，同时提高了运动中新视图合成的一致性。由于其设计，我们的分层方法平均只比原始的高斯飞溅慢4%。值得注意的是，强制执行一致性可以将Gaussian的数量减少大约一半，同时具有几乎相同的质量和视图一致性。因此，渲染性能几乎翻了一番，使我们的方法比原始的高斯Splatting快1.6倍，同时减少了50%的内存需求。 et.al.|[2402.00525](http://arxiv.org/abs/2402.00525)|null|
|**2024-01-31**|**Advances in 3D Generation: A Survey**|生成三维模型是计算机图形学的核心，也是几十年来研究的焦点。随着先进的神经表示和生成模型的出现，3D内容生成领域正在迅速发展，能够创建越来越高质量和多样化的3D模型。这一领域的快速发展使得我们很难跟上最近的所有发展。在这项调查中，我们旨在介绍3D生成方法的基本方法，并建立一个结构化的路线图，包括3D表示、生成方法、数据集和相应的应用程序。具体来说，我们介绍了用作3D生成主干的3D表示。此外，我们全面概述了快速增长的生成方法文献，按算法范式的类型进行分类，包括前馈生成、基于优化的生成、过程生成和生成新视图合成。最后，我们讨论了可用的数据集、应用程序和开放的挑战。我们希望这项调查能帮助读者探索这个令人兴奋的话题，并促进3D内容生成领域的进一步发展。 et.al.|[2401.17807](http://arxiv.org/abs/2401.17807)|null|
|**2024-01-27**|**Gaussian Splashing: Dynamic Fluid Synthesis with Gaussian Splatting**|我们展示了将基于物理的固体和流体动画与3D高斯飞溅（3DGS）相结合的可行性，以在使用3DGS重建的虚拟场景中创建新的效果。利用底层表示中高斯飞溅和基于位置的动力学（PBD）的一致性，我们以内聚的方式管理渲染、视图合成以及固体和流体的动力学。与高斯着色器类似，我们使用添加的法线增强每个高斯内核，将内核的方向与曲面法线对齐，以优化PBD模拟。这种方法有效地消除了由固体中的旋转变形引起的尖锐噪声。它还允许我们集成基于物理的渲染，以增强流体上的动态曲面反射。因此，我们的框架能够真实地再现动态流体上的曲面高光，并促进场景对象和新视图中流体之间的交互。有关更多信息，请访问我们的项目页面\url{https://amysteriouscat.github.io/GaussianSplashing/}. et.al.|[2401.15318](http://arxiv.org/abs/2401.15318)|null|
|**2024-01-26**|**3D Reconstruction and New View Synthesis of Indoor Environments based on a Dual Neural Radiance Field**|同时实现室内环境的3D重建和新视图合成具有广泛的应用，但在技术上非常具有挑战性。基于隐式神经函数的现有技术方法可以获得极好的三维重建结果，但它们在新视图合成方面的性能可能不令人满意。神经辐射场（NeRF）的令人兴奋的发展彻底改变了新的视图合成，然而，基于NeRF的模型可能无法重建干净的几何表面。我们开发了一种双神经辐射场（Du-NeRF），以同时实现高质量的几何重建和视图渲染。Du-NeRF包含两个几何场，一个从SDF场导出以便于几何重建，另一个从密度场导出以促进新视图合成。Du NeRF的一个创新特征是，它将视图无关分量与密度场解耦，并将其用作标签来监督SDF场的学习过程。这减少了形状辐射模糊性，并使几何图形和颜色在学习过程中相互受益。大量实验表明，Du-NeRF可以显著提高室内环境下新视图合成和3D重建的性能，并且在构建包含不服从多视图颜色一致性的精细几何图形的区域时尤其有效。 et.al.|[2401.14726](http://arxiv.org/abs/2401.14726)|null|
|**2024-01-23**|**IRIS: Inverse Rendering of Indoor Scenes from Low Dynamic Range Images**|尽管许多3D重建和新颖的视图合成方法允许从消费者相机轻松捕捉的多视图图像中真实地渲染场景，但它们在表示中烘焙照明，无法支持高级应用程序，如材质编辑、重新照明和虚拟对象插入。通过反向渲染重建基于物理的材料特性和照明有望实现此类应用。然而，大多数反向渲染技术都需要高动态范围（HDR）图像作为输入，这是大多数用户无法访问的设置。我们提出了一种方法，从多视图、低动态范围（LDR）图像中恢复场景的基于物理的材料特性和空间变化的HDR照明。我们在反向渲染管道中对LDR图像形成过程进行建模，并提出了一种新的材料、照明和相机响应模型的优化策略。与采用LDR或HDR输入的最先进的反向渲染方法相比，我们使用合成场景和真实场景来评估我们的方法。我们的方法优于以LDR图像作为输入的现有方法，并允许高度逼真的重新照明和对象插入。 et.al.|[2401.12977](http://arxiv.org/abs/2401.12977)|null|
|**2024-01-24**|**RGBD Objects in the Wild: Scaling Real-World 3D Object Learning from RGB-D Videos**|我们介绍了一种新的在野外捕获的RGB-D对象数据集，称为WildRGB-D。与大多数现有的仅带有RGB捕获的以对象为中心的真实世界数据集不同，深度通道的直接捕获允许更好的3D注释和更广泛的下游应用。WildRGB-D包括大型类别级RGB-D对象视频，这些视频是用iPhone 360度环绕对象拍摄的。它包含大约8500个记录对象和近20000个RGB-D视频，涉及46个常见对象类别。这些视频是在三种设置的不同杂乱背景下拍摄的，以覆盖尽可能多的真实世界场景：（i）一个视频中的单个对象；（ii）一个视频中的多个对象；以及（iii）在一个视频中具有静止手的对象。该数据集由对象遮罩、真实世界比例的相机姿态和RGBD视频中重建的聚合点云进行注释。我们用WildRGB-D对四个任务进行了基准测试，包括新颖的视图合成、相机姿态估计、物体6d姿态估计和物体表面重建。我们的实验表明，RGB-D对象的大规模捕获为推进3D对象学习提供了巨大的潜力。我们的项目页面是https://wildrgbd.github.io/. et.al.|[2401.12592](http://arxiv.org/abs/2401.12592)|null|

<p align=right>(<a href=#updated-on-20240207>back to top</a>)</p>

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

<p align=right>(<a href=#updated-on-20240207>back to top</a>)</p>

## Diffusion

|Publish Date|Title|Abstract|PDF|Code|
|---|---|---|---|---|
|**2024-02-05**|**Do Diffusion Models Learn Semantically Meaningful and Efficient Representations?**|扩散模型能够通过不同寻常的并置实现令人印象深刻的图像生成壮举，例如宇航员在月球上骑马，阴影放置得当。这些输出表明了执行组合泛化的能力，但模型是如何做到这一点的？我们在条件DDPM学习上进行对照实验，以生成以指定 $x$-和$y$-位置为中心的二维球面高斯凸点。我们的结果表明，语义上有意义的潜在表示的出现是实现高性能的关键。在成功实现过度学习的过程中，该模型经历了潜在表示的三个不同阶段：（阶段A）没有潜在结构，（阶段B）无序状态的2D流形，以及（阶段C）2D有序流形。对应于这些阶段中的每一个，我们确定了定性不同的生成行为：1）生成多个凸起，2）生成一个凸起，但在不准确的$x$和$y$位置，3）在正确的$x$y位置生成凸起。此外，我们还表明，即使在特征（$x$-与$y$-位置）以偏斜的频率表示的不平衡数据集下，$x$和$y$的学习过程也是耦合的，而不是因子分解的，这表明简单的香草味扩散模型无法学习将$x$与$y$ 中的本地化因子分解为单独的1D任务的有效表示。这些发现表明，未来的工作需要找到归纳偏差，这将推动生成模型在其输入中发现和利用可分解的独立结构，这将是将这些模型挖掘到更高效的数据机制中所必需的。 et.al.|[2402.03305](http://arxiv.org/abs/2402.03305)|null|
|**2024-02-05**|**Zero-shot Object-Level OOD Detection with Context-Aware Inpainting**|机器学习算法越来越多地作为黑匣子云服务或预训练模型提供，而无需访问其训练数据。这激发了零样本分布外（OOD）检测的问题。具体来说，我们的目标是检测不属于分类器的标签集，但被错误地分类为分布中（ID）对象的OOD对象。我们的方法RONIN使用现成的扩散模型来用修复来替换检测到的对象。RONIN用预测的ID标签来调整修复过程，将输入对象绘制得更接近分布域。因此，在ID的情况下，重建的对象非常接近原始对象，而在OOD的情况下则非常远离原始对象，这使得RONIN能够有效地区分ID和OOD样本。在整个广泛的实验中，我们证明了与之前的方法相比，RONIN在几个数据集上实现了具有竞争力的结果，无论是在零样本还是非零热设置中。 et.al.|[2402.03292](http://arxiv.org/abs/2402.03292)|null|
|**2024-02-05**|**InstanceDiffusion: Instance-level Control for Image Generation**|文本到图像的扩散模型产生高质量的图像，但不提供对图像中的单个实例的控制。我们介绍了InstanceDiffusion，它为文本到图像的扩散模型添加了精确的实例级别控制。InstanceDiffusion支持每个实例的自由形式语言条件，并允许以灵活的方式指定实例位置，如简单的单点、涂鸦、边界框或复杂的实例分割遮罩及其组合。我们建议对文本到图像模型进行三个主要更改，以实现精确的实例级别控制。我们的UniFusion块为文本到图像模型提供了实例级条件，ScaleU块提高了图像保真度，我们的多实例采样器提高了多个实例的生成。InstanceDiffusion在每个位置条件下都大大超过了专门的最先进的模型。值得注意的是，在COCO数据集上，框输入的AP $_｛50｝^\text｛box｝$ 和掩码输入的IoU分别比以前的先进技术高出20.4%和25.4%。 et.al.|[2402.03290](http://arxiv.org/abs/2402.03290)|null|
|**2024-02-05**|**Estimating position-dependent and anisotropic diffusivity tensors from molecular dynamics trajectories: Existing methods and future outlook**|约束可以通过打破平移各向同性并使所有物理性质与位置相关，从而显著改变材料的物理化学性质。分子动力学（MD）模拟已被证明有助于表征这种空间不均匀性，并探讨限制对材料性能的影响。对于静态属性，这是一项简单的任务，可以通过简单的空间装箱来实现。然而，由于缺乏用于批量计算的自相关的自然扩展，这种方法不能容易地应用于传输系数。这一挑战的主要例子是扩散率，在总体上，可以很容易地根据粒子的迁移率统计来估计扩散率，这满足了福克-普朗克方程。然而，在限制条件下，这些统计数据将遵循Smoluchowski方程，该方程缺乏闭合形式的分析解。这篇简短的综述探讨了从MD模拟中估计扩散张量轮廓的丰富历史，并讨论了为此目的开发的各种近似方法和算法。除了讨论批量方法的启发式扩展外，我们还概述了更严格的算法，包括基于核的方法、贝叶斯方法和算子离散化技术。此外，我们还概述了基于对示踪粒子施加偏置电势或施加约束的方法。最后，我们讨论了根据平均首次通过时间或提交人概率分布来估计扩散率的方法，这是一个最初在描述计算化学和生物学中罕见事件的集体变量空间背景下开发的概念框架。总之，本文简要介绍了从MD轨迹估计扩散率的各种方法，强调了该领域的挑战和机遇。 et.al.|[2402.03285](http://arxiv.org/abs/2402.03285)|null|
|**2024-02-05**|**Organic or Diffused: Can We Distinguish Human Art from AI-generated Images?**|生成性人工智能图像的出现彻底颠覆了艺术世界。从人类艺术中识别人工智能生成的图像是一个具有挑战性的问题，其影响随着时间的推移而不断扩大。未能解决这一问题使得不良行为者能够欺诈为人类艺术支付溢价的个人，以及那些声明政策禁止人工智能图像的公司。这对人工智能模型训练者来说也是至关重要的，他们需要过滤训练数据以避免潜在的模型崩溃。有几种不同的方法可以将人类艺术与人工智能图像区分开来，包括通过监督学习训练的分类器、针对扩散模型的研究工具，以及专业艺术家利用其艺术技术知识进行识别。在本文中，我们试图了解这些方法在良性和对抗性环境中与当今的现代生成模型相比能有多好的表现。我们策划了7种风格的真实人类艺术，从5个生成模型中生成匹配的图像，并应用了8个检测器（5个自动检测器和3个不同的人类群体，包括180名众筹工作者、4000多名专业艺术家和13名在检测人工智能方面经验丰富的专家艺术家）。Hive和专家艺术家都做得很好，但会以不同的方式犯错误（Hive对对抗性扰动的抵抗力较弱，而专家艺术家会产生更高的误报）。我们相信，随着模型的不断发展，这些弱点将继续存在，并利用我们的数据来证明为什么人工和自动检测器的组合团队能够提供准确度和稳健性的最佳组合。 et.al.|[2402.03214](http://arxiv.org/abs/2402.03214)|null|
|**2024-02-05**|**Light and Optimal Schrödinger Bridge Matching**|Schr“odinger Bridges（SB）作为经典扩散模型的一个很有前途的扩展，最近引起了ML界的注意，该模型也与熵最优输运（EOT）相关联SB的最新求解器利用了普遍的桥接匹配过程。这样的程序旨在恢复仅给定分布之间的运输计划的分布之间运输质量的随机过程。特别是，考虑到EOT计划，这些程序可以适用于求解SB。最近的工作大量利用了这一事实，将铆钉提供给基于匹配的SB求解器。这里的基石是恢复EOT计划：最近的工作要么使用启发式近似（例如，迷你批次OT），要么建立迭代匹配程序，通过设计在训练过程中积累误差。我们解决了这些限制，并提出了一种新的学习SB的过程，我们称之为\textbf｛最优Schr“odinger桥匹配｝。它利用了扩散过程的最优参数化，并通过单个桥匹配步骤和\textbf｛（b）｝可证明地恢复了SB过程以任意的运输计划作为输入。此外，我们还表明，最优桥梁匹配目标与最近发现的基于能量的建模（EBM）目标一致，以学习EOT/SB。受这一观察结果的启发，我们开发了一种光求解器（我们称之为LightSB-M），以使用Schr“odinger势的高斯混合参数化在实践中实现最佳匹配。我们通过实验展示了我们的求解器在一系列实际任务中的性能。LightSB-M求解器的代码可在\url中找到{https://github.com/SKholkin/LightSB-Matching}. et.al.|[2402.03207](http://arxiv.org/abs/2402.03207)|null|
|**2024-02-05**|**Guidance with Spherical Gaussian Constraint for Conditional Diffusion**|扩散模型的最新进展试图通过利用可微损失函数进行指导来处理条件生成任务，而不需要额外的训练。虽然这些方法取得了一定的成功，但它们往往会影响样本质量，并且需要较小的指导步骤，从而导致更长的采样过程。本文揭示了当采用损失引导时，采样过程中的歧管偏差是根本问题。通过建立损失制导估计误差的一定下界，从理论上证明了流形偏差的存在。为了缓解这个问题，我们从高维高斯分布中的集中现象中获得了灵感，提出了具有球面高斯约束的扩散（DSG）。DSG通过优化有效地将引导步骤约束在中间数据流形内，并允许使用更大的引导步骤。此外，我们还提出了一个具有球面高斯约束的DSG去噪的闭式解。值得注意的是，DSG可以作为插件模块无缝集成到现有的无训练条件扩散方法中。实现DSG只需要几行额外的代码，几乎没有额外的计算开销，但它会显著提高性能。在各种条件生成任务中的综合实验结果验证了DSG在样本质量和时间效率方面的优越性和适应性。 et.al.|[2402.03201](http://arxiv.org/abs/2402.03201)|null|
|**2024-02-05**|**Direct-a-Video: Customized Video Generation with User-Directed Camera Movement and Object Motion**|最近的文本到视频扩散模型取得了令人印象深刻的进展。在实践中，用户通常希望能够独立地控制对象运动和相机移动以进行定制视频创建。然而，目前的方法缺乏以解耦的方式分别控制对象运动和相机运动的重点，这限制了文本到视频模型的可控性和灵活性。在本文中，我们介绍了Direct-a-Video，这是一个允许用户独立指定一个或多个对象的运动和/或相机运动的系统，就像指导视频一样。我们提出了一种简单而有效的策略，用于对象运动和相机运动的解耦控制。使用模型的固有先验，通过空间交叉注意力调制来控制对象运动，不需要额外的优化。对于相机运动，我们引入了新的时间交叉注意力层来解释定量的相机运动参数。我们进一步采用了一种基于增强的方法，在小规模数据集上以自监督的方式训练这些层，消除了对显式运动注释的需要。这两个组件都独立运行，允许单独或组合控制，并且可以推广到开放域场景。大量实验证明了我们方法的优越性和有效性。项目页面：https://direct-a-video.github.io/. et.al.|[2402.03162](http://arxiv.org/abs/2402.03162)|null|
|**2024-02-05**|**Nonlinear feedback of the electrostatic instability on the blazar-induced pair beam and GeV cascade**|来自blazars的TeV伽马射线在宇宙空隙中产生的相对论对光束预计将产生观测中缺失的可探测的GeV级级联。这种次级级联的抑制意味着星系间磁场对光束的偏转，或者，光束等离子体不稳定性导致的光束能量损失。在这里，我们使用真实的二维光束分布来研究光束等离子体不稳定性如何反馈到光束上。我们发现，这种不稳定性显著拓宽了光束开口角，而没有任何显著的能量损失，从而证实了最近对简化的一维光束分布的反馈研究。然而，洛伦兹因子小于 $10^6$ 的束粒子的变窄扩散反馈可能会变得相关，即使最初它可以忽略不计。最后，当考虑TeV对的连续产生时，我们发现光束分布和波谱达到了一个新的准稳态，其中光束粒子的散射持续存在，光束开口角可能增加数百倍。了解GeV级联发射的影响需要考虑逆康普顿冷却。 et.al.|[2402.03127](http://arxiv.org/abs/2402.03127)|null|
|**2024-02-05**|**DARTS: Diffusion Approximated Residual Time Sampling for Low Variance Time-of-flight Rendering in Homogeneous Scattering Medium**|飞行时间（ToF）设备极大地推动了各种多模态感知应用的发展。然而，由于采样路径构建和时域顶点连接的复杂性，在ToF设备模拟中准确渲染时间分辨信息极具挑战性，尤其是在涉及复杂几何结构、不同材料和体积散射介质的场景中。现有作品要么在ToF渲染任务中表现出显著的偏差或差异，要么在涉及参与媒体和相机扭曲设置的场景中被证明是无效的。为了应对这一挑战，在本文中，我们将瞬态扩散理论集成到路径构建中，以生成时间分辨辐射的无偏全传输。此外，我们设计了一种椭圆采样方法，以提供满足任何所需光子遍历时间的可控顶点连接。据我们所知，我们的工作首次探索了根据瞬态辐射的重要性采样，从而能够在多个散射设置中构建更高质量的时间路径。大量实验表明，我们的采样方法可以在路径跟踪和基于光子的框架内显著提高ToF渲染的质量和效率，在相同的渲染时间内，与SOTA方法相比，MSE至少降低了5倍。与速度的提高相比，我们的方法没有引入内存开销和可忽略不计的额外计算，为各种现有的渲染框架提供了一个简单的插件。 et.al.|[2402.03106](http://arxiv.org/abs/2402.03106)|null|

<p align=right>(<a href=#updated-on-20240207>back to top</a>)</p>

## NeRF

|Publish Date|Title|Abstract|PDF|Code|
|---|---|---|---|---|
|**2024-01-31**|**BlockFusion: Expandable 3D Scene Generation using Latent Tri-plane Extrapolation**|我们介绍了BlockFusion，这是一种基于扩散的模型，它将3D场景生成为单元块，并无缝地合并新的块来扩展场景。BlockFusion使用从完整的3D场景网格中随机裁剪的3D块的数据集进行训练。通过逐块拟合，所有训练块都被转换为混合神经场：具有包含几何特征的三平面，然后是用于解码有符号距离值的多层感知器（MLP）。采用变分自动编码器将三平面压缩到潜在的三平面空间中，在该空间上进行去噪扩散处理。应用于潜在表示的扩散允许高质量和多样化的3D场景生成。要在生成过程中扩展场景，只需附加空块以与当前场景重叠，并外推现有的潜在三平面以填充新块。外推是通过在去噪迭代过程中使用来自重叠三平面的特征样本来调节生成过程来完成的。潜在的三平面外推法产生语义和几何上有意义的过渡，与现有场景和谐融合。2D布局调节机制用于控制场景元素的放置和布置。实验结果表明，BlockFusion能够在室内和室外场景中生成具有前所未有的高质量形状的多样化、几何一致和无边界的大型3D场景。 et.al.|[2401.17053](http://arxiv.org/abs/2401.17053)|null|
|**2024-01-26**|**Learning Neural Radiance Fields of Forest Structure for Scalable and Fine Monitoring**|这项工作利用神经辐射场和遥感技术用于林业应用。在这里，我们展示了神经辐射场为改进森林监测中现有的遥感方法提供了广泛的可能性。我们提出的实验证明了它们的潜力：（1）表达森林三维结构的精细特征，（2）融合可用的遥感模式，（3）改进三维结构衍生的森林指标。总之，这些特性使神经场成为一种有吸引力的计算工具，具有进一步提高森林监测程序的可扩展性和准确性的巨大潜力。 et.al.|[2401.15029](http://arxiv.org/abs/2401.15029)|null|
|**2024-01-25**|**Learning Robust Generalizable Radiance Field with Visibility and Feature Augmented Point Representation**|本文介绍了广义神经辐射场（NeRF）的一种新范式。以前的通用NeRF方法将多视点立体技术与基于图像的神经渲染相结合进行泛化，产生了令人印象深刻的结果，同时存在三个问题。首先，遮挡常常导致不一致的特征匹配。然后，由于采样点和粗略特征聚合的单独过程，它们在几何不连续性和局部尖锐形状中传递失真和伪影。第三，当源视图离目标视图不够近时，它们基于图像的表示会发生严重退化。为了应对挑战，我们提出了第一个基于点而不是基于图像的渲染构建可泛化神经场的范式，我们称之为可泛化神经点场（GPF）。我们的方法通过几何先验显式地建模可见性，并用神经特征增强它们。我们提出了一种新的非均匀对数采样策略，以提高渲染速度和重建质量。此外，我们提出了一种可学习的内核，该内核在空间上增加了用于特征聚合的特征，减轻了几何结构急剧变化的地方的失真。此外，我们的表现很容易被操纵。实验表明，在泛化和微调设置中，我们的模型可以在三个数据集上提供比所有对应模型和基准更好的几何结构、视图一致性和渲染质量，初步证明了可泛化NeRF新范式的潜力。 et.al.|[2401.14354](http://arxiv.org/abs/2401.14354)|null|
|**2024-01-24**|**Unified neural field theory of brain dynamics underlying oscillations in Parkinson's disease and generalized epilepsies**|通过皮质丘脑基底神经节（CTBG）系统的神经场模型，联合探讨了帕金森病（PD）和全身性癫痫的病理同步神经振荡的机制。基底神经节（BG）被近似为一个单一的有效群体，并分析了它们在调节振荡皮质丘脑（CT）动力学中的作用，反之亦然。除了正常的脑电图节律外，模型中还存在4 Hz和20 Hz左右的增强活动，这与PD的特征频率一致。这些节律是由BG和CT人群之间回路中的共振引起的，类似于先前CT模型中潜在的癫痫振荡。多巴胺耗竭被认为削弱了对PD中这些共振的抑制，网络连接解释了在4-8Hz和20Hz左右BG、丘脑和皮层活动之间的显著一致性。丘脑网状核（TRN）和BG的传入和传出连接位点之间的相似性预测低多巴胺对应于强直-阵挛（大发作）癫痫发作的可能性降低，这与实验结果一致。此外，该模型预测，与实验结果相匹配的低多巴胺水平会增加缺席（轻微）癫痫发作的可能性。与其他CTBG建模研究一致，当传入和传出BG与CT系统的连接增强时，表现出对缺席发作活动的抑制。BG被证明在强直-阵挛发作状态附近抑制CTBG系统的活性，从而深入了解BG回路中目前治疗的疗效。TRN的睡眠状态也被发现可以抑制病理性PD活动匹配观察。总的来说，这些发现证明了广泛性癫痫和帕金森病的相干振荡之间有很强的相似性，并为可能的合并症提供了见解。 et.al.|[2401.13467](http://arxiv.org/abs/2401.13467)|null|
|**2024-01-17**|**Reproducibility via neural fields of visual illusions induced by localized stimuli**|本文研究了Billock和Tsou[PNAS，2007]使用Amari型神经场的可控性对初级视皮层（V1）皮层活动进行建模的实验复制，重点关注中央凹或外周视野中的规则漏斗模式。其目的是理解和模拟在这些实验中观察到的视觉现象，强调其非线性性质。这项研究包括设计模拟Billock和Tsou实验中视觉刺激的感官输入。然后从理论和数值上研究这些输入引起的后图像，以确定它们复制实验观察到的视觉效果的能力。这项研究的一个关键方面是研究神经反应的非线性性质所引起的影响。特别是，通过强调兴奋性和抑制性神经元在某些视觉现象出现中的重要性，这项研究表明，这两种类型的神经元活动的相互作用在视觉过程中发挥着重要作用，挑战了后者主要由兴奋性活动单独驱动的假设。 et.al.|[2401.09108](http://arxiv.org/abs/2401.09108)|null|
|**2024-01-12**|**Motion2VecSets: 4D Latent Vector Set Diffusion for Non-rigid Shape Reconstruction and Tracking**|我们介绍了Motion2VecSets，这是一种用于从点云序列进行动态曲面重建的4D扩散模型。虽然现有的最先进的方法已经证明在使用神经场表示重建非刚性对象方面取得了成功，但传统的前馈网络遇到了来自噪声、部分或稀疏点云的模糊观测的挑战。为了应对这些挑战，我们引入了一种扩散模型，该模型通过压缩潜在表示的迭代去噪过程来显式学习非刚性对象的形状和运动分布。当处理模糊输入时，基于扩散的先验能够进行更合理和概率的重建。我们用潜在向量集参数化4D动力学，而不是使用全局潜在。这种新颖的4D表示使我们能够学习局部表面形状和变形模式，从而实现更准确的非线性运动捕捉，并显著提高对看不见的运动和身份的可推广性。对于更具时间连贯性的目标跟踪，我们同步地对变形潜集进行去噪，并在多个帧之间交换信息。为了避免计算开销，我们设计了一个交错的空间和时间注意力块，以沿着空间和时间域交替聚集变形潜伏期。与最先进的方法进行了广泛的比较，证明了我们的Motion2VenSets在从各种不完美的观测进行4D重建方面的优势，特别是在从DeformingThings4D Animals数据集上的稀疏点云重建看不见的个体方面，与CaDex相比，交集优于并集（IoU）提高了19%。更多详细信息，请访问https://vveicao.github.io/projects/Motion2VecSets/. et.al.|[2401.06614](http://arxiv.org/abs/2401.06614)|null|
|**2024-01-05**|**Denoising Vision Transformers**|我们深入研究了视觉转换器（ViTs）固有的一个细微但重大的挑战：这些模型的特征图显示出网格状的伪影，这对ViTs在下游任务中的性能造成了不利影响。我们的研究将这个基本问题追溯到输入阶段的位置嵌入。为了解决这一问题，我们提出了一种新的噪声模型，该模型普遍适用于所有的ViT。具体来说，噪声模型将ViT输出分解为三个部分：一个没有噪声伪影的语义术语和两个以像素位置为条件的伪影相关术语。这种分解是通过在每幅图像的基础上加强与神经场的交叉视图特征一致性来实现的。这种逐图像优化过程从原始ViT输出中提取无伪影特征，为离线应用程序提供干净的特征。扩大了我们的解决方案的范围，以支持在线功能，我们引入了一种可学习的去噪器，直接从未处理的ViT输出中预测无伪影特征，这显示出对新数据的显著泛化能力，而无需对每张图像进行优化。我们的两阶段方法，称为去噪视觉转换器（DVT），不需要重新训练现有的预先训练的ViT，并且立即适用于任何基于转换器的架构。我们在各种具有代表性的ViT（DINO、MAE、DeiT III、EVA02、CLIP、DINOv2、DINOv2-reg）上评估了我们的方法。广泛的评估表明，我们的DVT在多个数据集（例如+3.84mIoU）的语义和几何任务中持续显著地改进了现有的最先进的通用模型。我们希望我们的研究将鼓励对ViT设计进行重新评估，特别是关于位置嵌入的天真使用。 et.al.|[2401.02957](http://arxiv.org/abs/2401.02957)|null|
|**2023-12-30**|**PlanarNeRF: Online Learning of Planar Primitives with Neural Radiance Fields**|从视觉数据中识别空间完整的平面基元是计算机视觉中的一项关键任务。现有的方法在很大程度上局限于2D片段恢复或简化3D结构，即使具有广泛的平面注释。我们提出了PlanarNeRF，这是一种能够通过在线学习检测密集3D平面的新框架。PlanarNeRF利用神经场表示，带来了三个主要贡献。首先，它利用并行的外观和几何知识增强了三维平面检测。其次，提出了一种轻量级的平面拟合模块来估计平面参数。第三，引入了一种具有更新机制的新的全局内存库结构，确保了跨帧一致性。PlanarNeRF的灵活架构使其能够在二维监督和自监督解决方案中发挥作用，在每种解决方案中，它都可以有效地从稀疏的训练信号中学习，显著提高训练效率。通过广泛的实验，我们证明了PlanarNeRF在各种场景下的有效性，并比现有工作有了显著的改进。 et.al.|[2401.00871](http://arxiv.org/abs/2401.00871)|null|
|**2024-01-01**|**Deblurring 3D Gaussian Splatting**|最近对辐射场的研究为具有照片级真实感渲染质量的新颖视图合成铺平了坚实的道路。然而，它们通常使用神经网络和体积绘制，这两种方法的训练成本很高，并且由于绘制时间长，阻碍了它们在各种实时应用中的广泛使用。最近，人们提出了一种基于3D高斯散射的方法来对3D场景进行建模，并在实时渲染图像的同时实现了显著的视觉质量。然而，如果训练图像模糊，则渲染质量会严重下降。模糊通常是由于镜头散焦、物体运动和相机抖动而产生的，它不可避免地会干扰干净图像的获取。先前的几项研究试图使用神经场从模糊的输入图像中渲染干净清晰的图像。然而，这些工作中的大多数仅设计用于基于体积渲染的神经辐射场，并不直接适用于基于光栅化的3D高斯散射方法。因此，我们提出了一种新的实时去模糊框架，即去模糊3D高斯散点，使用小型多层感知器（MLP）来操纵每个3D高斯的协方差来对场景模糊度进行建模。虽然去模糊的3D高斯飞溅仍然可以享受实时渲染，但它可以从模糊的图像中重建精细和清晰的细节。在该基准上进行了各种实验，结果显示了我们的去模糊方法的有效性。定性结果可在https://benhenryl.github.io/Deblurring-3D-Gaussian-Splatting/ et.al.|[2401.00834](http://arxiv.org/abs/2401.00834)|null|
|**2023-12-22**|**Fluid Simulation on Neural Flow Maps**|我们介绍了神经流图，这是一种新的模拟方法，将新兴的隐式神经表示范式与基于流图理论的流体模拟相结合，以实现最先进的无粘流体现象模拟。我们设计了一种新的混合神经场表示，空间稀疏神经场（SSNF），它将小型神经网络与重叠、多分辨率和空间稀疏网格的金字塔相融合，以高精度紧凑地表示长期时空速度场。有了这个神经速度缓冲器，我们以机械对称的方式计算长期双向流图及其雅可比矩阵，以促进对现有解决方案的大幅精度提高。这些长程双向流图实现了低耗散的高平流精度，进而促进了高保真度的不可压缩流模拟，显示了复杂的旋涡结构。我们展示了我们的神经流体模拟在各种具有挑战性的模拟场景中的有效性，包括跳跃涡流、碰撞涡流、涡流重新连接，以及移动障碍物和密度差异产生的涡流。我们的例子表明，在能量守恒、视觉复杂性、对实验观测的遵守以及详细旋涡结构的保存方面，与现有方法相比，性能有所提高。 et.al.|[2312.14635](http://arxiv.org/abs/2312.14635)|null|

<p align=right>(<a href=#updated-on-20240207>back to top</a>)</p>

[contributors-shield]: https://img.shields.io/github/contributors/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[contributors-url]: https://github.com/Vincentqyw/cv-arxiv-daily/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[forks-url]: https://github.com/Vincentqyw/cv-arxiv-daily/network/members
[stars-shield]: https://img.shields.io/github/stars/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[stars-url]: https://github.com/Vincentqyw/cv-arxiv-daily/stargazers
[issues-shield]: https://img.shields.io/github/issues/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[issues-url]: https://github.com/Vincentqyw/cv-arxiv-daily/issues

