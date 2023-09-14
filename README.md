[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]

## Updated on 2023.09.14
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
|**2023-09-13**|**Dynamic NeRFs for Soccer Scenes**|新颖视角合成这个长期存在的问题有很多应用，尤其是在体育广播中。特别是足球动作的逼真新颖视角合成，引起了广播业的极大兴趣。然而，只有少数几个工业解决方案被提出，甚至很少能达到合成回放的近广播质量。除了在操场周围设置多个静态摄像头外，最好的专有系统几乎没有透露任何关于其内部工作的信息。由于缺乏公共数据集，利用多个静态相机执行这样的任务确实是一个文献中很少解决的挑战：用小而快速的元素重建大规模的、主要是静态的环境。最近，神经辐射场的出现在许多新颖的视图合成应用中取得了惊人的进展，利用深度学习原理在最具挑战性的环境中产生逼真的结果。在这项工作中，我们研究了基于动态NeRF的任务解决方案的可行性，即旨在重建一般动态内容的神经模型。我们构建了合成足球环境，并使用它们进行了多项实验，确定了有助于用动态NeRF重建足球场景的关键组件。我们表明，尽管这种方法不能完全满足目标应用程序的质量要求，但它为实现成本效益高的自动解决方案提供了有希望的途径。我们还公开了我们的工作数据集和代码，目的是鼓励研究界进一步致力于动态足球场景的新颖视图合成任务。有关代码、数据和视频结果，请参阅https://soccernerfs.isach.be. et.al.|[2309.06802](http://arxiv.org/abs/2309.06802)|null|
|**2023-09-13**|**SAMPLING: Scene-adaptive Hierarchical Multiplane Images Representation for Novel View Synthesis from a Single Image**|最近的新颖视图合成方法对于相对较小的场景（例如，室内环境和具有少数对象的场景）获得了有希望的结果，但对于具有单个图像作为输入的无边界室外场景往往失败。在本文中，我们介绍了SAMPLING，这是一种基于改进的多平面图像（MPI）的场景自适应分层多平面图像表示，用于从单个图像合成新视图。观察到无边界户外场景的深度分布变化很大，我们为MPI采用了自适应仓策略，根据每个场景图像排列平面。为了表示复杂的几何结构和多尺度细节，我们进一步引入了一个层次细化分支，它可以产生高质量的合成新视图。我们的方法在KITTI数据集上使用单个图像合成大规模无界户外场景时表现出了相当大的性能提升，并很好地推广到了看不见的Tanks和Temples数据集。代码和模型将很快提供。 et.al.|[2309.06323](http://arxiv.org/abs/2309.06323)|null|
|**2023-09-11**|**FlowIBR: Leveraging Pre-Training for Efficient Neural Image-Based Rendering of Dynamic Scenes**|我们介绍了一种用于动态场景的单目新颖视图合成的新方法。现有技术已经显示出令人印象深刻的渲染质量，但倾向于在不利用先验知识的情况下专注于单个场景内的优化。这种限制主要归因于缺乏可用于训练的动态场景数据集以及场景动力学的多样性。我们的方法FlowIBR通过集成基于神经图像的渲染方法来规避这些问题，该方法在广泛可用的静态场景的大型语料库上进行了预训练，并具有每个场景优化的场景流场。利用该流场，我们弯曲摄影机光线以抵消场景动力学，从而将动态场景呈现为渲染网络的静态场景。所提出的方法将每个场景的优化时间减少了一个数量级，实现了与现有方法相当的结果——所有这些都在单个消费级GPU上。 et.al.|[2309.05418](http://arxiv.org/abs/2309.05418)|null|
|**2023-09-11**|**Towards Viewpoint Robustness in Bird's Eye View Segmentation**|自动驾驶汽车（AV）要求用于感知的神经网络对不同的视点具有鲁棒性，如果它们要部署在许多类型的车辆上，而不需要为每种车辆重复数据收集和标记的成本。AV公司通常专注于从不同的场景和地点收集数据，但由于成本原因，不关注摄像机设备配置。因此，大多数震源组中只存在少量的钻机变体。在本文中，我们研究了AV感知模型如何受到摄像机视点变化的影响，并提出了一种在不重复数据收集和标记的情况下跨车辆类型缩放它们的方法。使用鸟瞰图（BEV）分割作为一项激励任务，我们通过大量实验发现，现有的感知模型对相机视点的变化非常敏感。当使用来自一个相机装备的数据进行训练时，在推断时相机的俯仰、偏航、深度或高度的微小变化会导致性能大幅下降。我们引入了一种新的视图合成技术，并使用它将收集的数据转换为目标钻机的视点，使我们能够为不同的目标钻机训练BEV分割模型，而无需任何额外的数据收集或标记成本。为了分析观点变化的影响，我们利用合成数据来缓解其他差距（内容、ISP等）。然后，我们的方法在真实数据上进行训练，并在合成数据上进行评估，从而能够对不同的目标钻机进行评估。我们发布所有数据以供未来工作使用。我们的方法能够回收部署到新钻机时损失的IoU的平均14.7%。 et.al.|[2309.05192](http://arxiv.org/abs/2309.05192)|null|
|**2023-09-10**|**SC-NeRF: Self-Correcting Neural Radiance Field with Sparse Views**|在最近的研究中，神经辐射场的泛化在新的视图合成任务中得到了广泛的探索。然而，现有的方法仅限于对象和室内场景。在这项工作中，我们将泛化任务扩展到户外场景，仅在对象级数据集上进行训练。这种方法提出了两个挑战。首先，训练和测试场景之间的显著分布变化导致渲染结果中出现黑色伪影。其次，室外场景中的视点变化会导致渲染图像中出现重影或区域丢失。为了应对这些挑战，我们提出了一个基于多头注意力机制的几何校正模块和外观校正模块。我们将渲染深度标准化，并将其与光方向组合，作为注意力机制中的查询。我们的网络有效地纠正了户外场景中不同的场景结构和几何特征，从物体层面很好地推广到看不见的户外场景。此外，我们使用外观校正模块来校正外观特征，防止由于视点更改而导致的渲染伪影，如空白边界和重影。通过结合这些模块，我们的方法成功地解决了户外场景泛化的挑战，产生了高质量的渲染结果。当在四个数据集（Blender、DTU、LLFF、Spaces）上进行评估时，我们的网络优于以前的方法。值得注意的是，与MVSNeRF相比，我们的网络将Spaces户外场景的平均PSNR从19.369提高到25.989，SSIM从0.838提高到0.889，并将LPIPS从0.265降低到0.224。 et.al.|[2309.05028](http://arxiv.org/abs/2309.05028)|null|
|**2023-09-07**|**SimpleNeRF: Regularizing Sparse Input Neural Radiance Fields with Simpler Solutions**|神经辐射场（NeRF）在场景的真实感自由视图渲染中表现出令人印象深刻的性能。然而，NeRF需要对给定场景中的图像进行密集采样，并且当只有稀疏的视图集可用时，其性能会显著下降。研究人员发现，监督NeRF估计的深度有助于用更少的视图有效地训练它。深度监督是使用经典方法或在大型数据集上预先训练的神经网络来获得的。前者可能只提供稀疏的监督，而后者可能存在泛化问题。与早期的方法不同，我们试图通过设计增强模型并将其与NeRF一起训练来学习深度监督。我们设计了增强模型，通过探索位置编码和视图相关辐射在训练少镜头NeRF中的作用，鼓励更简单的解决方案。由这些更简单的模型估计的深度用于监督NeRF深度估计。由于增强模型在某些区域可能不准确，我们设计了一种机制，只选择可靠的深度估计进行监督。最后，我们在NeRF的粗糙和精细多层感知器之间添加了一致性损失，以确保更好地利用分层采样。通过采用上述正则化，我们在两个流行的数据集上实现了最先进的视图合成性能。我们模型的源代码可以在我们的项目页面上找到：https://nagabhushansn95.github.io/publications/2023/SimpleNeRF.html et.al.|[2309.03955](http://arxiv.org/abs/2309.03955)|null|
|**2023-09-07**|**BluNF: Blueprint Neural Field**|神经辐射场（NeRF）彻底改变了场景新颖的视图合成，提供了视觉逼真、精确和稳健的隐式重建。虽然最近的方法允许NeRF编辑，例如对象删除、3D形状修改或材料特性操纵，但在这种编辑之前的手动注释使该过程变得乏味。此外，传统的2D交互工具缺乏对3D空间的准确感知，阻碍了对场景的精确操作和编辑。在本文中，我们介绍了一种新的方法，称为蓝图神经场（BluNF），以解决这些编辑问题。BluNF提供了一个强大且用户友好的2D蓝图，实现了直观的场景编辑。通过利用隐式神经表示，BluNF使用先前的语义和深度信息构建场景的蓝图。生成的蓝图可以轻松编辑和操作NeRF表示。我们通过直观的点击和更改机制展示了BluNF的可编辑性，实现了3D操作，如遮罩、外观修改和对象移除。我们的方法对视觉内容创作做出了重大贡献，为该领域的进一步研究铺平了道路。 et.al.|[2309.03933](http://arxiv.org/abs/2309.03933)|null|
|**2023-09-07**|**SyncDreamer: Generating Multiview-consistent Images from a Single-view Image**|在本文中，我们提出了一种新的扩散模型，称为，从单视图图像生成多视图一致图像。最近的工作Zero123使用预先训练的大规模2D扩散模型，展示了从物体的单视图图像生成看似新颖的视图的能力。然而，为生成的图像保持几何图形和颜色的一致性仍然是一个挑战。为了解决这个问题，我们提出了一种同步多视点扩散模型，该模型对多视点图像的联合概率分布进行建模，从而能够在单个反向过程中生成多视点一致图像。SyncDreamer通过3D感知特征注意力机制在反向过程的每一步同步所有生成图像的中间状态，该机制将不同视图中的相应特征关联起来。实验表明，SyncDreamer生成的图像在不同视图之间具有高度一致性，因此非常适合各种3D生成任务，如新颖的视图合成、文本到3D和图像到3D。 et.al.|[2309.03453](http://arxiv.org/abs/2309.03453)|null|
|**2023-09-06**|**Bayes' Rays: Uncertainty Quantification for Neural Radiance Fields**|神经辐射场（NeRF）在视图合成和深度估计等应用中显示出了前景，但从多视图图像中学习面临着固有的不确定性。目前量化它们的方法要么是启发式的，要么是计算要求很高的。我们引入了BayesRays，这是一个事后框架，用于在不修改训练过程的情况下评估任何预先训练的NeRF中的不确定性。我们的方法使用空间扰动和贝叶斯拉普拉斯近似来建立体积不确定性场。我们从统计角度推导了我们的算法，并在关键指标和应用中展示了其卓越的性能。其他结果可在：https://bayesrays.github.io. et.al.|[2309.03185](http://arxiv.org/abs/2309.03185)|null|
|**2023-09-05**|**TiAVox: Time-aware Attenuation Voxels for Sparse-view 4D DSA Reconstruction**|四维数字减影血管造影（4D DSA）在许多医学疾病的诊断中起着至关重要的作用，如动静脉畸形（AVM）和动静脉瘘（AVF）。尽管4D DSA的重建具有重要的应用价值，但它需要大量的视图来有效地模拟复杂的血管和放射造影流，从而意味着显著的辐射剂量。为了解决这个高辐射问题，我们提出了一种用于稀疏视图4D DSA重建的时间感知衰减体素（TiAVox）方法，为高质量的4D成像铺平了道路。此外，可以从重建的4D DSA图像生成2D和3D DSA成像结果。TiAVox引入了4D衰减体素网格，从空间和时间维度反映衰减特性。它通过最小化渲染图像和稀疏2D DSA图像之间的差异来进行优化。在没有任何神经网络参与的情况下，TiAVox享有特定的物理可解释性。每个可学习体素的参数表示衰减系数。我们在临床和模拟数据集上验证了TiAVox方法，在临床来源的数据集上仅使用30个视图，就实现了31.23的新视图合成峰值信噪比（PSNR），而传统的Feldkamp-Davis-Kress方法需要133个视图。类似地，在合成数据集中只有10个视图的情况下，TiAVox对于新视图合成产生了34.32的PSNR，对于3D重建产生了41.40的PSNR。我们还进行了消融研究，以证实TiAVox的主要成分。该代码将公开提供。 et.al.|[2309.02318](http://arxiv.org/abs/2309.02318)|null|

<p align=right>(<a href=#updated-on-20230914>back to top</a>)</p>

## 3D Reconstruction

|Publish Date|Title|Abstract|PDF|Code|
|---|---|---|---|---|
|**2023-09-13**|**Exploiting Multiple Priors for Neural 3D Indoor Reconstruction**|神经隐式建模允许在小物体上实现令人印象深刻的3D重建结果，而在大型室内场景中表现出显著的局限性。在这项工作中，我们提出了一种新的神经隐式建模方法，该方法利用多种正则化策略来实现大型室内环境的更好重建，同时仅依赖于图像。稀疏但准确的深度先验用于将场景锚定到初始模型。还引入了密集但不太准确的深度先验，它足够灵活，仍然可以让模型偏离它，以改进估计的几何结构。然后，提出了一种新的自监督策略来正则化估计的曲面法线。最后，可学习的曝光补偿方案允许应对具有挑战性的照明条件。实验结果表明，我们的方法在具有挑战性的室内场景中产生了最先进的3D重建。 et.al.|[2309.07021](http://arxiv.org/abs/2309.07021)|null|
|**2023-09-12**|**Semantic and Articulated Pedestrian Sensing Onboard a Moving Vehicle**|由于车辆的大的向前运动，很难从车载采集的视频执行3D重建。与标准基准相比，即使是物体检测和人体感应模型在板载视频上的表现也明显较差，因为与标准物体检测基准相比，物体经常出现在远离相机的地方，图像质量经常因运动模糊而降低，并且经常发生遮挡。这导致了交通数据特定基准的普及。最近，光探测和测距（LiDAR）传感器已经变得流行起来，可以直接估计深度，而无需执行3D重建。然而，与基于图像的方法相比，基于激光雷达的方法仍然缺乏远距离的关节式人体检测。我们假设，从激光雷达数据中针对关节式人体感知的基准可以增加对交通中人体感知和预测的研究，并可以改善行人的交通安全。 et.al.|[2309.06313](http://arxiv.org/abs/2309.06313)|null|
|**2023-09-12**|**SoccerNet 2023 Challenges Results**|SoccerNet 2023挑战赛是SoccerNet团队组织的第三届年度视频理解挑战赛。在第三版中，挑战由七项基于愿景的任务组成，分为三个主题。第一个主题，广播视频理解，由三个与描述视频广播中发生的事件相关的高级任务组成：（1）动作识别，专注于检索与足球全局动作相关的所有时间戳，专注于用自然语言和锚定时间戳描述广播。第二个主题，场理解，涉及（4）相机校准的单一任务，重点是从图像中检索内在和外在的相机参数。第三个也是最后一个主题，球员理解，由三个与提取球员信息相关的低级任务组成：（5）重新识别，重点是在多个视图中检索相同的球员，（6）多对象跟踪，重点是通过未经编辑的视频流跟踪球员和球，以及（7）球衣号码识别，专注于从tracklets中识别球员的球衣号码。与以前版本的SoccerNet挑战相比，任务（2-3-7）是新颖的，包括新的注释和数据，任务（4）用更多的数据和注释进行了增强，任务（6）现在专注于端到端方法。有关任务、挑战和排行榜的更多信息，请访问https://www.soccer-net.org.基线和开发工具包可在https://github.com/SoccerNet. et.al.|[2309.06006](http://arxiv.org/abs/2309.06006)|**[link](https://github.com/spiideo/soccersegcal)**|
|**2023-09-11**|**A survey on real-time 3D scene reconstruction with SLAM methods in embedded systems**|同时定位和映射（SLAM）的3D重建是无人机、服务机器人和移动AR/VR设备等运输系统领域的一个重要课题。与点云表示相比，基于网格和体素的3D重建对于高级功能特别有用，如避障或与物理环境的交互。本文介绍了在资源受限的硬件平台上实现基于视觉的三维场景重建流水线。实时性能、内存管理和低功耗对嵌入式系统至关重要。描述了从传感器到3D重建的传统SLAM管道，包括深度学习的潜在用途。详细介绍了在资源有限的情况下执行高级功能的情况。最近的系统提出了具有不同粒度的3D重建方法的嵌入式实现。实时定位和重建所需的精度和资源消耗之间的权衡是本文确定和讨论的开放研究问题之一。 et.al.|[2309.05349](http://arxiv.org/abs/2309.05349)|null|
|**2023-09-09**|**Cryo-Electron Ptychography: Applications and Potential in Biological Characterisation**|显然需要发展表征技术，提供生物学中结构-功能关系的详细信息。使用电子显微镜在保持宽视场的同时实现高分辨率仍然是一个挑战，特别是对于辐射敏感样品，其中保持结构完整性所需的信噪比受到低电子注量的限制。在这篇综述中，我们探索了低温电子ptychography作为一种在低通量条件下表征生物系统的替代方法的潜力。使用这种方法，增加了来自多个感兴趣采样区域的信息含量，有可能使用比传统冷冻电子显微镜所需更少的粒子进行3D重建。这对于难以获得均匀单粒子分布的系统实现更高的分辨率是重要的。我们讨论了这种方法在单粒子分析和异构大型物体应用中的进展、局限性和未来发展的潜在领域。 et.al.|[2309.04881](http://arxiv.org/abs/2309.04881)|null|
|**2023-09-07**|**A Food Package Recognition and Sorting System Based on Structured Light and Deep Learning**|基于视觉算法的机械臂抓取系统是一种可以应用于各种场景的机械臂系统。它使用算法自动识别目标的位置，并引导机械臂抓取目标，这比可教的机械臂抓取系统具有更灵活的特点。然而，对于一些食品包装来说，其透明包装或反射材料给视觉算法的识别带来了挑战，传统的视觉算法无法实现这些包装的高精度。此外，在机械臂抓取过程中，在z轴高度上的定位仍然需要手动设置参数，这可能会导致错误。基于上述两个问题，我们使用深度学习算法和结构光三维重建技术设计了一个食品包装分拣系统。使用预先训练好的MASK-R-CNN模型识别图像中物体的类别并获得其二维坐标，然后使用结构光三维重建技术计算其三维坐标，最后经过坐标系转换来引导机械臂进行抓取。经过测试表明，该方法可以实现对不同种类食品包装的全自动识别和抓取，具有较高的精度。使用这种方法，可以帮助食品制造商降低生产成本，提高生产效率。 et.al.|[2309.03704](http://arxiv.org/abs/2309.03704)|null|
|**2023-09-06**|**SADIR: Shape-Aware Diffusion Models for 3D Image Reconstruction**|从有限数量的2D图像重建3D图像一直是计算机视觉和图像分析中的一个长期挑战。虽然基于深度学习的方法在这一领域取得了令人印象深刻的性能，但现有的深度网络往往无法有效利用图像中呈现的对象的形状结构。因此，重建对象的拓扑结构可能无法很好地保存，导致不同部分之间存在诸如不连续性、孔洞或不匹配连接之类的伪影。在本文中，我们提出了一种基于扩散模型的三维图像重建形状感知网络，称为SADIR，以解决这些问题。与之前主要依赖图像强度的空间相关性进行3D重建的方法不同，我们的模型利用从训练数据中学习的形状先验来指导重建过程。为了实现这一点，我们开发了一个联合学习网络，该网络可以同时学习变形模型下的平均形状。然后，每个重建的图像被认为是平均形状的变形变体。我们在大脑和心脏磁共振成像（MRI）上验证了我们的模型SADIR。实验结果表明，我们的方法优于基线，具有更低的重建误差和更好地保留图像中物体的形状结构。 et.al.|[2309.03335](http://arxiv.org/abs/2309.03335)|null|
|**2023-09-06**|**Sparse 3D Reconstruction via Object-Centric Ray Sampling**|我们提出了一种新的方法，用于从360度校准的摄像机设备捕获的稀疏视图集重建3D对象。我们通过使用基于MLP的神经表示和三角形网格的混合模型来表示物体表面。我们工作中的一个关键贡献是一种新的以对象为中心的神经表示采样方案，其中光线在所有视图中共享。这有效地集中并减少了在每次迭代时用于更新神经模型的样本数量。此采样方案依赖于网格表示，以确保样本沿其法线良好分布。然后通过可微分渲染器有效地执行渲染。我们证明，这种采样方案可以更有效地训练神经表示，不需要对分割掩模进行额外监督，可以进行最先进的3D重建，并且可以在谷歌的扫描对象、坦克和寺庙以及MVMC汽车数据集上使用稀疏视图。 et.al.|[2309.03008](http://arxiv.org/abs/2309.03008)|null|
|**2023-09-06**|**Multi-log grasping using reinforcement learning and virtual visual servoing**|我们探索了使用强化学习和虚拟视觉伺服进行自动转发的多日志抓取。森林过程的自动化是一个重大挑战，由于非结构化和恶劣的户外环境，许多关于机器人控制的技术带来了不同的挑战。抓取多个原木涉及动力学和路径规划问题，其中抓斗、原木、地形和障碍物之间的交互需要视觉信息。为了解决这些挑战，我们将图像分割与起重机控制分离，并利用虚拟相机从3D重建数据中提供图像流。我们使用笛卡尔控制来简化域转移。由于原木桩是静态的，使用桩及其周围环境的3D重建进行视觉伺服相当于使用真实的相机数据直到抓取点。这放宽了图像分割挑战的计算资源和时间限制，并允许在原木堆未被遮挡的情况下收集数据。缺点是在抓取过程中缺乏信息。我们证明了这个问题是可以控制的，并且提供了一种代理，该代理在从具有挑战性的2-5根原木堆中挑选一根或几根原木时成功率为95%。 et.al.|[2309.02997](http://arxiv.org/abs/2309.02997)|null|
|**2023-09-06**|**Designing Situated Dashboards: Challenges and Opportunities**|情境可视化是一个新兴领域，它将可视化、增强现实、人机交互和物联网等多个领域结合在一起，以支持无处不在的世界中的人类数据活动。同样，仪表板广泛用于通过多个视图简化复杂数据。然而，仪表板仅适用于桌面设置，并且需要视觉策略来支持情境性。我们提出了基于AR的定位仪表盘的概念，并介绍了在与专家的访谈中提出的设计考虑因素和挑战。这些挑战旨在为促进定位仪表板的有效设计和创作提供方向和机会。 et.al.|[2309.02945](http://arxiv.org/abs/2309.02945)|null|

<p align=right>(<a href=#updated-on-20230914>back to top</a>)</p>

## Diffusion

|Publish Date|Title|Abstract|PDF|Code|
|---|---|---|---|---|
|**2023-09-13**|**UnifiedGesture: A Unified Gesture Synthesis Model for Multiple Skeletons**|协同语音手势的自动生成在计算机动画中备受关注。先前的工作在单个数据集上设计了网络结构，这导致了不同运动捕捉标准之间缺乏数据量和可推广性。此外，由于语音和手势之间的相关性较弱，这是一项具有挑战性的任务。为了解决这些问题，我们提出了UnifiedGesture，这是一种基于扩散模型的语音驱动手势合成方法，在具有不同骨架的多个手势数据集上进行训练。具体来说，我们首先提出了一个重定目标网络，以学习不同运动捕捉标准的潜在同胚图，在扩展数据集的同时统一各种手势的表示。然后，我们基于扩散模型架构，使用跨局部注意力和自我注意力来捕捉语音和手势之间的相关性，以生成更好的语音匹配和逼真的手势。为了进一步调整语音和手势并增加多样性，我们将离散手势单元的强化学习与学习的奖励函数结合起来。大量实验表明，UnifiedGesture在CCA、FGD和人像方面优于最近的语音驱动手势生成方法。所有代码、预先训练的模型、数据库和演示都可在https://github.com/YoungSeng/UnifiedGesture. et.al.|[2309.07051](http://arxiv.org/abs/2309.07051)|null|
|**2023-09-13**|**Experimental Study on the Detection of Frozen Diffused Ammonia Blockage in the Inactive Section of a Variable Conductance Heat Pipe**|可变导热热管（VCHP）主要用于航天器应用中的电子系统冷却，因为它们可以处理冷源中的高温波动，从而防止系统损坏。这些波动以及超低温总是存在于外太空中，因此，VCHP设计的关键步骤之一是确保它们能够承受这些条件。然而，关于它们在长期暴露于低于冰点的条件（即低于工作流体冰点的温度）期间和之后的弹性，没有太多的报道。在本文中，我们实现并验证了一种基于改进的平面方法的计算程序，以预测VCHP温度分布并确定气体蒸汽锋的位置。然后，我们将氨/不锈钢VCHP连续暴露在低于氨凝固点的温度下211小时，以随后检查扩散到热管冷凝器的非活性部分的冷冻氨的薄块的形成和随后的动力学。我们还描述了在发生（或不存在）冷冻氨堵塞时，绝热段和储层温度之间的强相关性是如何保持（或打破）的。 et.al.|[2309.06936](http://arxiv.org/abs/2309.06936)|null|
|**2023-09-13**|**VRDMG: Vocal Restoration via Diffusion Posterior Sampling with Multiple Guidance**|恢复降级的音乐信号对于提高下游音乐操作的音频质量至关重要。最近基于扩散的音乐恢复方法表现出了令人印象深刻的性能，其中，扩散后验采样（DPS）因其固有特性而脱颖而出，使其在各种恢复任务中具有通用性。在本文中，我们发现存在会降低当前基于DPS的方法性能的潜在问题，并介绍了缓解各种扩散制导技术（包括RePaint（RP）策略和伪逆制导扩散模型（ $\Pi$ GDM））带来的问题的方法。我们分别演示了在不同失真和截止频率水平下执行人声去噪和带宽扩展任务的方法。在这两项任务中，我们的方法都优于当前基于DPS的音乐恢复基准。我们参考\url{http://carlosholivan.github.io/demos/audio-restoration-2023.html}例如恢复的音频样本。 et.al.|[2309.06934](http://arxiv.org/abs/2309.06934)|null|
|**2023-09-13**|**DreamStyler: Paint by Style Inversion with Text-to-Image Diffusion Models**|近年来，大规模文本到图像模型的研究取得了显著成果，在艺术领域有着各种各样的应用。然而，由于语言描述的固有限制，仅用文本提示来表达艺术品的独特特征（如笔触、色调或构图）可能会受到限制。为此，我们介绍了DreamStyler，这是一个为艺术图像合成而设计的新颖框架，精通文本到图像的合成和风格转换。DreamStyler通过上下文感知的文本提示优化了多阶段文本嵌入，从而提高了图像质量。此外，通过内容和风格指导，DreamStyler展示了灵活性，以适应一系列风格参考。实验结果表明，它在多个场景中都有出色的性能，这表明它在艺术产品创作中有着巨大的潜力。 et.al.|[2309.06933](http://arxiv.org/abs/2309.06933)|null|
|**2023-09-13**|**MagiCapture: High-Resolution Multi-Concept Portrait Customization**|包括Stable Diffusion在内的大规模文本到图像模型能够生成高保真逼真的人像图像。有一个活跃的研究领域致力于个性化这些模型，旨在使用提供的参考图像集综合特定的主题或风格。然而，尽管这些个性化方法产生了看似合理的结果，但它们往往产生的图像往往不够真实，而且还不具备商业可行性。这在肖像图像生成中尤为明显，由于我们固有的人类偏见，人脸上的任何非自然伪影都很容易被识别。为了解决这一问题，我们引入了MagiCapture，这是一种个性化方法，用于集成主题和风格概念，仅使用少数主题和风格参考即可生成高分辨率人像图像。例如，给定少量随机自拍，我们的微调模型可以生成特定风格的高质量人像图像，如护照或个人资料照片。这项任务的主要挑战是，组成的概念缺乏基本事实，导致最终输出的质量下降，源主题的身份发生转变。为了解决这些问题，我们提出了一种新的注意力重聚焦损失与辅助先验相结合，这两种方法都有助于在这种弱监督学习环境中进行稳健学习。我们的管道还包括额外的后处理步骤，以确保创建高度逼真的输出。MagiCapture在定量和定性评估方面都优于其他基线，也可以推广到其他非人类对象。 et.al.|[2309.06895](http://arxiv.org/abs/2309.06895)|null|
|**2023-09-13**|**Spin-orbital correlations from complex orbital order in MgV $_{2}$O$_{4}$**|MgV$_{2}$O$_{4}$是一种基于磁性V$^{3+}$离子的尖晶石，其同时具有自旋（$S=1$）和轨道（$l_{eff}=1$）矩。由于磁性位点潜在的烧绿石配位，一旦$Fd\overline施加了令人沮丧的相互作用，MgV$_{2}$O$_{4}$中的自旋仅为反铁磁有序{3}m$lattice在T$_{S}$\simeq$60K处通过轨道驱动的结构畸变而被破坏。因此，在T$_{N}$\sim eq$40K处发生N’eel跃迁。电子轨道的低温空间有序性对结构和磁性都是基本的，然而，关于它是否可以用复轨道序或实轨道序来描述的大量讨论是模糊的。我们应用中子光谱学来解析轨道基态的性质，并使用x射线和中子衍射来表征滞后自旋轨道相关性。中子光谱学发现了多个激发带，我们根据基于轨道简并基态的多能级（或激子）理论对这些激发带进行了参数化。对轨道基态有意义的是，我们报道了高能下的“类光学”模式，我们将其归因于从自旋轨道$j_{eff}$=2基态流形到激发的$j_｛eff}$=1能级的类晶体场激发。我们根据具有自旋轨道耦合的哈密顿量和由V$^{3+}$离子周围的完美八面体的偏差引起的局部晶体电场畸变来参数化磁激发。我们认为这为MgV$_{2}$O$_{4}$中的复杂轨道阶提供了令人信服的证据。然后，我们应用该模型的结果来理解磁扩散散射中的滞后效应，其中我们提出MgV$_{2}$O$_{4}$ 显示低温自旋级的高温轨道记忆。 et.al.|[2309.06853](http://arxiv.org/abs/2309.06853)|null|
|**2023-09-13**|**Computing solubility and thermodynamics properties of H2O2 in water**|过氧化氢在许多环境和工业化学过程中起着关键作用。我们进行了经典的分子动力学和连续分数组分蒙特卡罗模拟，以计算H2O2在水溶液中的热力学性质。对Orabi&English和Cordeiro开发的H2O2可用力场的质量进行了系统评估。为了评估哪种水力场适合于预测H2O2在水溶液中的性质，使用了四种水力，即TIP3P、TIP4P/2005、TIP5P-E和改良的TIP3P力场。虽然Orabi&English使用力场计算的253-353K温度范围内纯H2O2的密度与实验结果非常一致，但Cordeiro使用力场的密度被低估了3%。TIP4P/2005力场与Orabi&English开发的H2O2力场相结合，可以预测整个H2O2摩尔分数范围内H2O2水溶液的密度，与实验结果非常一致。TIP4P/2005力场与任一H2O2力场相结合，可以预测整个H2O2摩尔分数范围内H2O2水溶液的粘度，与实验结果非常一致。对于H2O2摩尔分数的整个范围，使用具有任一H2O2力场的TIP4P/2005力场的H2O2和水分子的扩散系数几乎是恒定的。与Orabi&English的力场相比，H2O2的Cordeiro力场与任一水力场相结合可以预测水中H2O2的Henry系数，与实验值更为一致。 et.al.|[2309.06796](http://arxiv.org/abs/2309.06796)|null|
|**2023-09-13**|**DCTTS: Discrete Diffusion Model with Contrastive Learning for Text-to-speech Generation**|在文本到语音（TTS）任务中，潜在扩散模型具有良好的保真度和泛化能力，但其昂贵的资源消耗和缓慢的推理速度一直是一个挑战。本文提出了一种基于对比学习的文本-语音生成离散扩散模型（DCTTS）。DCTTS做出了以下贡献：1）基于离散空间的TTS扩散模型显著降低了扩散模型的计算消耗，提高了采样速度；2） 采用基于离散空间的对比学习方法，增强语音与文本的对齐连接，提高采样质量；3）它使用了一个高效的文本编码器来简化模型的参数并提高计算效率。实验结果表明，本文提出的方法在显著降低扩散模型资源消耗的同时，具有出色的语音合成质量和采样速度。合成样品可在https://github.com/lawtherWu/DCTTS. et.al.|[2309.06787](http://arxiv.org/abs/2309.06787)|null|
|**2023-09-13**|**High throughput sampling of phase space with deep learning potentials: $δ$-AlOOH at geophysical conditions**|含水和名义无水矿物（NAMs）是一类对地球物理学具有重大意义的基本固体。它们是深层地质水循环中的水载体。它们影响地球形成的聚集体（岩石）的结构、弹性、塑性和热力学性质以及相关系。它们在塑造地球的地球化学和地球物理过程中发挥着关键作用。它们的复杂性阻碍了对其性质的预测计算，但机器学习潜力带来的材料模拟进展正在改变这种状况。在这里，我们采用了一种混合方法，将深度学习电位（DP）与SCAN元GGA函数相结合，以模拟原型含水系统。我们说明了这种方法模拟$\delta$-AlOOH（$\delta$ ）的可行性、成功性和必要性，这是一个能够在俯冲板块中将水输送到地球核幔边界附近（约2900公里深和约135 GPa）的阶段。使用DP势的分子动力学模拟对相空间进行高通量采样，提供了地球物理条件下氢键行为和质子扩散的全景。这些模拟为深入了解这些塑造地球内部状态的关键组成部分提供了途径。 et.al.|[2309.06712](http://arxiv.org/abs/2309.06712)|null|
|**2023-09-13**|**Generalizable improvement of the Spalart-Allmaras model through assimilation of experimental data**|本研究的重点是使用模型和数据融合来改进分离流雷诺平均Navier-Stokes解的Spalart-Allmaras（SA）闭合模型。特别是，我们的目标是开发模型，不仅吸收稀疏的实验数据来提高计算模型的性能，而且通过恢复经典的SA行为来推广到看不见的情况。我们使用数据同化，即集合卡尔曼滤波方法（EnKF）来校准分离流的SA模型的系数，从而实现我们的目标。通过生产、扩散和销毁项的参数化来实施整体校准策略。这种校准依赖于对分离流的速度剖面、表面摩擦和压力系数收集的实验数据的同化。尽管使用了来自后向台阶（BFS）周围单个流动条件的观测数据，但重新校准的SA模型证明了对其他分离流动的推广，包括2D凸起和修改的BFS等情况。在感兴趣的量方面观察到显著的改善，即每个测试流的皮肤摩擦系数（ $C_f$）和压力系数（$C_p$ ）。最后，还证明了新提出的模型恢复了外部未分离流动的SA熟练度，例如NACA-0012翼型周围的流动，而没有任何外推的危险，并且SA模型中的单独校准的项针对特定的流动物理，其中校准的生产项改善再循环区，而破坏改善回收区。 et.al.|[2309.06679](http://arxiv.org/abs/2309.06679)|null|

<p align=right>(<a href=#updated-on-20230914>back to top</a>)</p>

## NeRF

|Publish Date|Title|Abstract|PDF|Code|
|---|---|---|---|---|
|**2023-09-13**|**Generalizable Neural Fields as Partially Observed Neural Processes**|神经场将信号表示为由神经网络参数化的函数，是传统离散矢量或基于网格的表示的一种很有前途的替代方案。与离散表示相比，神经表示既能很好地扩展分辨率，又是连续的，并且可以是多次可微的。然而，给定我们想要表示的信号数据集，必须为每个信号优化单独的神经场是低效的，并且不能利用信号之间的共享信息或结构。现有的泛化方法将其视为元学习问题，并采用基于梯度的元学习来学习初始化，然后通过测试时间优化对初始化进行微调，或者学习超网络来产生神经场的权重。相反，我们提出了一种新的范式，将神经表征的大规模训练视为部分观察到的神经过程框架的一部分，并利用神经过程算法来解决这一任务。我们证明，这种方法优于最先进的基于梯度的元学习方法和超网络方法。 et.al.|[2309.06660](http://arxiv.org/abs/2309.06660)|null|
|**2023-09-08**|**Single View Refractive Index Tomography with Neural Fields**|折射率层析成像是一个反问题，我们试图从2D投影图像测量中重建场景的3D折射场。折射场本身是不可见的，而是影响光线在空间中传播时路径的连续弯曲。折射场出现在各种各样的科学应用中，从显微镜中的半透明细胞样本到弯曲来自遥远星系的光的暗物质场。这个问题带来了一个独特的挑战，因为折射场直接影响光的路径，使其恢复成为一个非线性问题。此外，与传统的层析成像相比，我们试图通过利用散射在整个介质中的光源的知识，仅从单个视点使用投影图像来恢复折射场。在这项工作中，我们介绍了一种使用基于坐标的神经网络对场景中潜在的连续折射场进行建模的方法。然后，我们使用射线三维空间曲率的显式建模来优化该网络的参数，通过综合分析方法重建折射场。通过在模拟中恢复折射场，并分析光源分布对恢复的影响，证明了我们方法的有效性。然后，我们在模拟暗物质映射问题上测试了我们的方法，在该问题中，我们恢复了真实模拟暗物质分布下的折射场。 et.al.|[2309.04437](http://arxiv.org/abs/2309.04437)|null|
|**2023-09-07**|**BluNF: Blueprint Neural Field**|神经辐射场（NeRF）彻底改变了场景新颖的视图合成，提供了视觉逼真、精确和稳健的隐式重建。虽然最近的方法允许NeRF编辑，例如对象删除、3D形状修改或材料特性操纵，但在这种编辑之前的手动注释使该过程变得乏味。此外，传统的2D交互工具缺乏对3D空间的准确感知，阻碍了对场景的精确操作和编辑。在本文中，我们介绍了一种新的方法，称为蓝图神经场（BluNF），以解决这些编辑问题。BluNF提供了一个强大且用户友好的2D蓝图，实现了直观的场景编辑。通过利用隐式神经表示，BluNF使用先前的语义和深度信息构建场景的蓝图。生成的蓝图可以轻松编辑和操作NeRF表示。我们通过直观的点击和更改机制展示了BluNF的可编辑性，实现了3D操作，如遮罩、外观修改和对象移除。我们的方法对视觉内容创作做出了重大贡献，为该领域的进一步研究铺平了道路。 et.al.|[2309.03933](http://arxiv.org/abs/2309.03933)|null|
|**2023-09-07**|**SimNP: Learning Self-Similarity Priors Between Neural Points**|用于3D对象重建的现有神经场表示要么（1）利用对象级表示，但由于对全局潜在代码的限制而遭受低质量细节，要么（2）能够完美地重建观测，但未能利用对象级先验知识来推断未观察到的区域。我们提出了一种学习类别级自相似性的方法SimNP，它通过将神经点辐射场与类别级自类似性表示相连接，结合了两个世界的优点。我们的贡献是双重的。（1） 我们利用相干点云的概念设计了第一个类别级别的神经点表示。由此产生的神经点辐射场为局部支持的对象区域存储了高级别的细节。（2） 我们了解了如何以无约束和无监督的方式在神经点之间共享信息，这允许在重建过程中根据给定的观测值导出对象的未观察区域。我们表明，SimNP在重建对称的看不见物体区域方面优于以前的方法，超过了建立在类别级或像素对齐辐射场上的方法，同时提供了实例之间的语义对应 et.al.|[2309.03809](http://arxiv.org/abs/2309.03809)|null|
|**2023-09-06**|**CoNeS: Conditional neural fields with shift modulation for multi-sequence MRI translation**|多序列磁共振成像（MRI）在现代临床研究和深度学习研究中都有广泛的应用。然而，在临床实践中，由于患者的不同图像采集协议或造影剂禁忌症，经常会出现一个或多个MRI序列缺失的情况，这限制了在多序列数据上训练的深度学习模型的使用。一种很有前途的方法是利用生成模型来合成缺失的序列，这可以作为替代获取。解决这一问题的最先进方法是基于卷积神经网络（CNN），该网络通常存在频谱偏差，导致高频精细细节的重建较差。在本文中，我们提出了具有移位调制的条件神经场（CoNeS），这是一种以体素坐标为输入并学习用于多序列MRI平移的目标图像的表示的模型。所提出的模型使用多层感知器（MLP）代替CNN作为像素到像素映射的解码器。因此，每个目标图像被表示为神经场，该神经场通过利用学习的潜码的移位调制而被调节在源图像上。在BraTS 2018和前庭神经鞘瘤患者的内部临床数据集上进行的实验表明，所提出的方法在视觉和定量上都优于最先进的多序列MRI翻译方法。此外，我们进行了光谱分析，表明CoNeS能够克服传统CNN模型中常见的光谱偏差问题。为了进一步评估合成图像在临床下游任务中的使用，我们在推理时使用合成图像测试了分割网络。 et.al.|[2309.03320](http://arxiv.org/abs/2309.03320)|**[link](https://github.com/cyjdswx/cones)**|
|**2023-09-06**|**ResFields: Residual Neural Fields for Spatiotemporal Signals**|神经场是一类被训练来表示高频信号的神经网络，近年来由于其在复杂三维数据建模方面的出色性能，特别是通过单个多层感知器（MLP）的大神经符号距离（SDFs）或辐射场（NeRFs），而受到了极大的关注。然而，尽管用MLP表示信号的能力和简单性很强，但由于MLP的容量有限，这些方法在建模大而复杂的时间信号时仍然面临挑战。在本文中，我们提出了一种有效的方法来解决这一限制，将时间残差层纳入神经场，称为ResFields，这是一类专门设计用于有效表示复杂时间信号的新型网络。我们对ResFields的性质进行了全面的分析，并提出了一种矩阵分解技术来减少可训练参数的数量并增强泛化能力。重要的是，我们的公式与现有技术无缝集成，并在各种具有挑战性的任务中持续改进结果：2D视频近似、通过时间SDF的动态形状建模和动态NeRF重建。最后，我们通过展示ResFields在从轻量级捕捉系统的稀疏感官输入捕捉动态3D场景方面的有效性，展示了它的实用性。 et.al.|[2309.03160](http://arxiv.org/abs/2309.03160)|**[link](https://github.com/markomih/ResFields)**|
|**2023-09-01**|**GNFactor: Multi-Task Real Robot Learning with Generalizable Neural Feature Fields**|开发能够在非结构化现实世界环境中通过视觉观察执行各种操作任务的代理是机器人技术中的一个长期问题。为了实现这一目标，机器人需要对场景的3D结构和语义有全面的了解。在这项工作中，我们提出了 $\textbf｛GNFactor｝$，一种用于多任务机器人操作的视觉行为克隆代理，具有$\textbf｛G｝$通用$\textbf｛N｝$eural功能$\textbf｛F｝$字段。GNFactor联合优化了作为重建模块的可推广神经场（GNF）和作为决策模块的感知转换器，利用了共享的深度3D体素表示。为了在3D中结合语义，重建模块利用视觉语言基础模型（$\textit｛例如｝$ ，Stable Diffusion）将丰富的语义信息提取到深度3D体素中。我们在3个真实机器人任务中评估了GNFactor，并在10个RLBench任务中进行了详细的消融，演示次数有限。我们观察到GNFactor在可见和不可见任务中比当前最先进的方法有了实质性的改进，证明了GNFactor强大的泛化能力。我们的项目网站是https://yanjieze.com/GNFactor/。 et.al.|[2308.16891](http://arxiv.org/abs/2308.16891)|**[link](https://github.com/YanjieZe/GNFactor)**|
|**2023-08-30**|**Active Neural Mapping**|我们用不断学习的神经场景表示来解决主动映射的问题，即主动神经映射。关键在于通过有效的代理移动积极找到要探索的目标空间，从而最大限度地减少在以前看不见的环境中飞行中的地图不确定性。在本文中，我们检验了连续学习神经场的权重空间，并从经验上表明，神经变异性，即对随机权重扰动的预测鲁棒性，可以直接用于测量神经映射的瞬时不确定性。结合神经映射中继承的连续几何信息，可以引导agent找到一条可遍历的路径，以逐渐获得环境知识。我们首次提出了一种用于在线场景重建的具有基于坐标的隐式神经表示的主动映射系统。在视觉逼真的Gibson和Matterport3D环境中的实验证明了所提出方法的有效性。 et.al.|[2308.16246](http://arxiv.org/abs/2308.16246)|null|
|**2023-08-29**|**Canonical Factors for Hybrid Neural Fields**|因子特征量提供了一种简单的方法来构建更紧凑、高效和可积分的神经场，但也引入了对真实世界数据不一定有益的偏差。在这项工作中，我们（1）描述了这些架构对轴对准信号的不希望有的偏差——它们可能导致高达2 PSNR的辐射场重建差异——以及（2）探索了学习一组规范化变换如何通过消除这些偏差来改进表示。我们在二维模型问题中证明，同时学习这些变换和场景外观是成功的，效率大大提高。我们使用图像、符号距离和辐射场重建任务验证了最终的架构，我们称之为TILTED，在这些任务中，我们观察到了质量、稳健性、紧凑性和运行时间方面的改进。结果表明，TILTED可以实现比基线大2倍的能力，同时突出神经场评估程序的弱点。 et.al.|[2308.15461](http://arxiv.org/abs/2308.15461)|null|
|**2023-08-30**|**NSF: Neural Surface Fields for Human Modeling from Monocular Depth**|从单眼相机获得个性化的3D可动画化化身在游戏、虚拟试穿、动画和VR/XR等领域有几个现实世界的应用。然而，从这种稀疏的数据中建模动态和细粒度的服装变形是非常具有挑战性的。现有的从深度数据建模3D人类的方法在计算效率、网格一致性以及分辨率和拓扑结构的灵活性方面具有局限性。例如，使用隐式函数重建形状和每帧提取显式网格在计算上是昂贵的，并且不能确保跨帧的连贯网格。此外，在具有离散表面的预先设计的人类模板上预测每个顶点的变形在分辨率和拓扑结构上缺乏灵活性。为了克服这些局限性，我们提出了一种新的方法“关键特征：神经表面场”，用于从单目深度对穿着3D衣服的人类进行建模。NSF仅在基面上定义了一个神经场，该神经场对连续和灵活的位移场进行建模。NSF可以适应不同分辨率和拓扑结构的基面，而无需在推理时进行重新训练。与现有方法相比，我们的方法在保持网格一致性的同时消除了昂贵的每帧表面提取，并且能够在不重新训练的情况下重建任意分辨率的网格。为了促进这方面的研究，我们在项目页面上发布了我们的代码：https://yuxuan-xue.com/nsf. et.al.|[2308.14847](http://arxiv.org/abs/2308.14847)|null|

<p align=right>(<a href=#updated-on-20230914>back to top</a>)</p>

[contributors-shield]: https://img.shields.io/github/contributors/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[contributors-url]: https://github.com/Vincentqyw/cv-arxiv-daily/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[forks-url]: https://github.com/Vincentqyw/cv-arxiv-daily/network/members
[stars-shield]: https://img.shields.io/github/stars/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[stars-url]: https://github.com/Vincentqyw/cv-arxiv-daily/stargazers
[issues-shield]: https://img.shields.io/github/issues/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[issues-url]: https://github.com/Vincentqyw/cv-arxiv-daily/issues

