[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]

## Updated on 2023.12.14
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
|**2023-12-13**|**FoundationPose: Unified 6D Pose Estimation and Tracking of Novel Objects**|我们介绍了FoundationPose，这是一个用于6D物体姿态估计和跟踪的统一基础模型，支持基于模型和无模型的设置。我们的方法可以在测试时立即应用于新物体，而无需微调，只要给出其CAD模型，或者捕获少量参考图像。我们用神经隐式表示弥合了这两种设置之间的差距，该表示允许有效的新视图合成，在相同的统一框架下保持下游姿态估计模块不变。在大型语言模型（LLM）、一种新颖的基于转换器的架构和对比学习公式的帮助下，通过大规模的合成训练实现了强大的可推广性。对涉及挑战性场景和对象的多个公共数据集的广泛评估表明，我们的统一方法在很大程度上优于专门用于每项任务的现有方法。此外，尽管减少了假设，但它甚至实现了与实例级方法相当的结果。项目页面：https://nvlabs.github.io/foundationpose/ et.al.|[2312.08344](http://arxiv.org/abs/2312.08344)|null|
|**2023-12-13**|**Global Latent Neural Rendering**|在可推广的新视图合成方法中，最近的一个趋势是学习对单个相机射线起作用的渲染算子。这种方法很有前途，因为它消除了对显式体积渲染的需求，但它有效地将目标图像视为独立像素的集合。在这里，我们建议学习一个全局渲染操作符，该操作符联合作用于所有摄影机光线。我们展示了实现这种渲染的正确表示是5维平面扫描体积，该体积由输入图像在面向目标相机的一组平面上的投影组成。基于这一理解，我们介绍了我们的卷积全局潜在渲染器（ConvGLR），这是一种高效的卷积架构，可在低分辨率潜在空间中全局执行渲染操作。在稀疏和可推广设置下的各种数据集上的实验表明，我们的方法始终显著优于现有方法。 et.al.|[2312.08338](http://arxiv.org/abs/2312.08338)|null|
|**2023-12-13**|**Neural Radiance Fields for Transparent Object Using Visual Hull**|与不透明物体不同，透明物体的新颖视图合成是一项具有挑战性的任务，因为透明物体折射背景光，导致透明物体表面沿着视点变化产生视觉失真。最近引入的神经辐射场（NeRF）是一种视图合成方法。由于其显著的性能改进，基于NeRF的以下应用在各个主题中都得到了开发。然而，如果具有不同折射率的对象被包括在诸如透明对象之类的场景中，则NeRF表现出有限的性能，因为没有适当地考虑透明对象表面处的折射光线。为了解决这个问题，我们提出了一种基于NeRF的方法，该方法由以下三个步骤组成：首先，我们使用视觉外壳重建透明物体的三维形状。其次，我们根据Snell定律模拟了透明物体内部光线的折射。最后，我们通过折射光线对点进行采样，并将它们放入NeRF中。实验评估结果表明，我们的方法解决了传统NeRF对透明物体的限制。 et.al.|[2312.08118](http://arxiv.org/abs/2312.08118)|null|
|**2023-12-13**|**Novel View Synthesis with View-Dependent Effects from a Single Image**|在本文中，我们首先将视图相关效应考虑到基于单图像的新视图合成（NVS）问题中。为此，我们建议利用NVS中的相机运动先验来将依赖于视图的外观或效果（VDE）建模为场景中的负视差。通过识别“跟随”相机运动的镜面反射性，我们通过沿着核线的负深度区域聚集输入像素颜色，将VDE注入输入图像。此外，我们提出了一种“松弛体积渲染”近似方法，该方法允许在单次通过中计算密度，从而提高单图像NVS的效率。我们的方法只能从图像序列中学习单个图像的NVS，这是一种完全自监督的学习方法，首次不需要深度和相机姿态标注。我们给出了大量的实验结果，并表明我们提出的方法可以用VDE学习NVS，在RealEstate10k和MannequinChallenge数据集上优于SOTA单视图NVS方法。 et.al.|[2312.08071](http://arxiv.org/abs/2312.08071)|null|
|**2023-12-13**|**DrivingGaussian: Composite Gaussian Splatting for Surrounding Dynamic Autonomous Driving Scenes**|我们提出了DrivingGaussian，这是一个高效、有效的动态自动驾驶场景框架。对于具有移动对象的复杂场景，我们首先使用增量静态3D高斯对整个场景的静态背景进行顺序和渐进的建模。然后，我们利用复合动态高斯图来处理多个移动对象，分别重建每个对象，并恢复它们在场景中的准确位置和遮挡关系。我们进一步使用激光雷达先验进行高斯散射，以重建具有更大细节的场景并保持全景一致性。DrivingGaussian在驱动场景重建方面优于现有方法，能够实现高保真度和多相机一致性的真实感环绕视图合成。将发布源代码和经过训练的模型。 et.al.|[2312.07920](http://arxiv.org/abs/2312.07920)|null|
|**2023-12-12**|**SMERF: Streamable Memory Efficient Radiance Fields for Real-Time Large-Scene Exploration**|最近的实时视图合成技术在保真度和速度上迅速进步，现代方法能够以交互式帧速率渲染接近照片级真实感的场景。与此同时，在易于光栅化的显式场景表示和基于射线行进的神经场之间出现了紧张关系，后者的最先进实例在质量上超过了前者，同时对于实时应用来说成本高得令人望而却步。在这项工作中，我们介绍了SMERF，这是一种视图合成方法，在占地面积高达3亿 $^2$、体积分辨率为3.5毫米$^3$ 的大型场景中，它实现了实时方法中最先进的精度。我们的方法建立在两个主要贡献之上：一个是分层模型划分方案，它在限制计算和内存消耗的同时增加了模型容量，另一个是蒸馏训练策略，它同时产生高保真度和内部一致性。我们的方法能够在网络浏览器中实现全六自由度（6DOF）导航，并在商品智能手机和笔记本电脑上实时渲染。大量实验表明，我们的方法在实时新视图合成方面，在标准基准上超过了当前最先进的0.78 dB，在大型场景上超过了1.78 dB，渲染帧的速度比最先进的辐射场模型快三个数量级，并在包括智能手机在内的各种商品设备上实现了实时性能。我们鼓励读者在我们的项目网站上亲自探索这些模型：https://smerf-3d.github.io. et.al.|[2312.07541](http://arxiv.org/abs/2312.07541)|null|
|**2023-12-12**|**COLMAP-Free 3D Gaussian Splatting**|虽然神经渲染在场景重建和新颖的视图合成方面取得了令人印象深刻的进展，但它在很大程度上依赖于精确预计算的相机姿态。为了放松这一限制，已经做出了多项努力来训练神经辐射场（NeRF），而不需要预处理相机姿势。然而，NeRF的隐式表示为同时优化3D结构和相机姿态提供了额外的挑战。另一方面，鉴于其明确的点云表示，最近提出的3D高斯飞溅提供了新的机会。本文利用输入视频流的显式几何表示和连续性来执行新的视图合成，而无需任何SfM预处理。我们以顺序的方式处理输入帧，并通过一次获取一个输入帧来逐步增长3D高斯集，而无需预先计算相机姿势。在大的运动变化下，我们的方法在视图合成和相机姿态估计方面比以前的方法有了显著的改进。我们的项目页面是https://oasisyang.github.io/colmap-free-3dgs et.al.|[2312.07504](http://arxiv.org/abs/2312.07504)|null|
|**2023-12-12**|**NVS-Adapter: Plug-and-Play Novel View Synthesis from a Single Image**|大规模文本到图像（T2I）模型的迁移学习最近在从单个图像中对不同对象进行新视图合成（NVS）方面显示出了令人印象深刻的潜力。虽然以前的方法通常在NVS的多视图数据集上训练大型模型，但微调T2I模型的整个参数不仅需要高成本，而且降低了T2I模型在新领域中生成不同图像的泛化能力。在这项研究中，我们提出了一种有效的方法，称为NVS适配器，它是T2I模型的即插即用模块，在充分利用T2I模型泛化能力的同时，合成视觉对象的新颖多视图。NVS适配器由两个主要组件组成；视图一致性交叉注意学习视觉对应关系以对齐视图特征的局部细节，全局语义条件将生成的视图的语义结构与参考视图对齐。实验结果表明，NVS适配器可以有效地合成几何一致的多视图，并且在不完全微调T2I模型的情况下在基准测试上实现高性能。代码和数据可在~\href中公开获取{https://postech-cvlab.github.io/nvsadapter/}{https://postech-cvlab.github.io/nvsadapter/}。 et.al.|[2312.07315](http://arxiv.org/abs/2312.07315)|null|
|**2023-12-12**|**Unifying Correspondence, Pose and NeRF for Pose-Free Novel View Synthesis from Stereo Pairs**|这项工作深入研究了从立体对合成无姿势的新颖视图的任务，这是3D视觉中一项具有挑战性和开创性的任务。与以往任何框架不同，我们的创新框架无缝集成了2D对应匹配、相机姿态估计和NeRF渲染，促进了这些任务的协同增强。我们通过设计一种利用共享表示的架构来实现这一点，该架构是增强3D几何理解的基础。利用任务之间固有的相互作用，我们的统一框架使用所提出的训练策略进行端到端训练，以提高整体模型的准确性。通过对来自两个真实世界数据集的不同室内和室外场景的广泛评估，我们证明了我们的方法比以前的方法有了实质性的改进，特别是在以极端视角变化和缺乏准确相机姿势为特征的场景中。 et.al.|[2312.07246](http://arxiv.org/abs/2312.07246)|**[link](https://github.com/KU-CVLAB/CoPoNeRF)**|
|**2023-12-11**|**UpFusion: Novel View Diffusion from Unposed Sparse View Observations**|我们提出了UpFusion，这是一种在没有相应姿态信息的情况下，在给定稀疏参考图像集的情况下可以执行新颖的视图合成并推断对象的3D表示的系统。当前的稀疏视图3D推理方法通常依赖于相机姿态来几何地聚合来自输入视图的信息，但当这种信息不可用/不准确时，这种方法在野外并不稳健。相反，UpFusion通过学习在条件生成模型中隐含地利用可用图像作为上下文来合成新视图，从而避开了这一要求。我们将两种互补的条件反射形式结合到扩散模型中，以利用输入视图：a）通过使用场景级变换器推断与查询视图对齐的特征，b）通过可以直接观察输入图像标记的中间注意力层。我们表明，这种机制允许生成高保真度的新视图，同时在给定额外（未着色）图像的情况下提高合成质量。我们在Co3Dv2和Google Scanned Objects数据集上评估了我们的方法，并展示了与依赖姿势的稀疏视图方法以及无法利用其他视图的单视图方法相比，我们的方法的优势。最后，我们还表明，我们学习的模型可以超越训练类别进行推广，甚至可以从野外通用对象的自捕获图像中进行重建。 et.al.|[2312.06661](http://arxiv.org/abs/2312.06661)|null|

<p align=right>(<a href=#updated-on-20231214>back to top</a>)</p>

## 3D Reconstruction

|Publish Date|Title|Abstract|PDF|Code|
|---|---|---|---|---|
|**2023-12-13**|**ProNeRF: Learning Efficient Projection-Aware Ray Sampling for Fine-Grained Implicit Neural Radiance Fields**|神经渲染的最新进展表明，尽管速度较慢，但隐式紧凑模型可以从多个视图中学习场景的几何图形和视图相关外观。为了保持如此小的内存占用，但实现更快的推理时间，最近的工作采用了“采样器”网络，该网络自适应地对隐式神经辐射场中沿每条射线的一小部分点进行采样。尽管这些方法在渲染时间上减少了10美元\倍，但与香草NeRF相比，它们的质量仍有相当大的下降。相反，我们提出了ProNeRF，它在内存占用（类似于NeRF）、速度（比HyperReel快）和质量（比K-Planes好）之间提供了最佳折衷。ProNeRF配备了一种新的投影感知采样（PAS）网络，以及一种用于射线探测和利用的新训练策略，从而实现高效的细粒度粒子采样。我们的ProNeRF产生了最先进的指标，比NeRF快15-23倍，PSNR比NeRF高0.65dB，比已发表的最佳基于采样器的方法HyperReel高0.95dB。我们的探索和开发训练策略使ProNeRF能够学习完整场景的颜色和密度分布，同时学习聚焦于最高密度区域的高效光线采样。我们提供了广泛的实验结果，分别在广泛采用的前向和360数据集LLFF和Blender上支持我们的方法的有效性。 et.al.|[2312.08136](http://arxiv.org/abs/2312.08136)|null|
|**2023-12-13**|**Denoising diffusion-based synthetic generation of three-dimensional (3D) anisotropic microstructures from two-dimensional (2D) micrographs**|集成计算材料工程（ICME）显著增强了对微观结构与材料性能之间关系的系统分析，为高性能材料的发展铺平了道路。然而，由于缺乏三维（3D）微观结构数据集，分析微观结构敏感材料的行为仍然具有挑战性。此外，如果微观结构是各向异性的，这一挑战会被放大，因为这也会导致材料的各向异性。在本文中，我们提出了一种仅基于二维（2D）显微照片使用基于条件扩散的生成模型（DGM）重建各向异性微观结构的框架。所提出的框架涉及多个2D条件DGM的空间连接，每个条件DGM都经过训练以生成三个不同正交平面的2D微观结构样本。连接的多个反向扩散过程使得能够对马尔可夫链进行有效建模，以将噪声转换为3D微观结构样本。此外，采用改进的协调采样来提高样本质量，同时在3D空间中保持各向异性微观结构样本切片之间的空间连接。为了验证所提出的框架，根据空间相关函数和物理材料行为对二维到三维重建的各向异性微观结构样品进行了评估。结果表明，该框架不仅能够再现材料相的统计分布，而且能够再现三维空间中的材料性质。这突出了所提出的二维到三维重建框架在建立微观结构-性能联系方面的潜在应用，这可能有助于未来研究的高通量材料设计 et.al.|[2312.07832](http://arxiv.org/abs/2312.07832)|null|
|**2023-12-12**|**Adaptive Confidence Multi-View Hashing for Multimedia Retrieval**|多视图哈希方法将多个视图中的异构数据转换为二进制哈希码，是多媒体检索的关键技术之一。然而，目前的方法主要探讨多个观点之间的互补性，而缺乏信心学习和融合。此外，在实际应用场景中，单视图数据包含冗余噪声。为了进行置信度学习并消除不必要的噪声，我们提出了一种新的自适应置信度多视图哈希（ACMVH）方法。首先，开发了置信网络来从各种单视图特征中提取有用信息并去除噪声信息。此外，采用自适应置信度多视图网络来测量每个视图的置信度，然后通过加权求和来融合多视图特征。最后，设计了一个扩展网络来进一步增强融合特征的特征表示。据我们所知，我们率先将置信学习应用于多媒体检索领域。在两个公共数据集上进行的大量实验表明，所提出的ACMVH比最先进的方法性能更好（最大增加了3.24%）。源代码可在https://github.com/hackerhyper/acmvh. et.al.|[2312.07327](http://arxiv.org/abs/2312.07327)|**[link](https://github.com/hackerhyper/acmvh)**|
|**2023-12-11**|**Gaussian Splatting SLAM**|我们首次将3D高斯散射应用于使用单个移动单目或RGB-D相机的增量3D重建。我们的同步定位和映射（SLAM）方法以3fps实时运行，使用高斯作为唯一的3D表示，统一了所需的表示，以实现准确、高效的跟踪、映射和高质量渲染。需要一些创新来从现场摄像机连续重建具有高保真度的3D场景。首先，为了超越最初的3DGS算法，该算法需要来自离线运动结构（SfM）系统的精确姿态，我们使用针对3D高斯的直接优化来制定3DGS的相机跟踪，并表明这能够实现快速而稳健的跟踪，并具有广泛的收敛范围。其次，通过利用高斯的显式性质，我们引入了几何验证和正则化来处理增量三维密集重建中出现的模糊性。最后，我们介绍了一个完整的SLAM系统，它不仅在新的视图合成和轨迹估计方面取得了最先进的结果，而且还重建了微小甚至透明的物体。 et.al.|[2312.06741](http://arxiv.org/abs/2312.06741)|null|
|**2023-12-10**|**UNeR3D: Versatile and Scalable 3D RGB Point Cloud Generation from 2D Images in Unsupervised Reconstruction**|在从2D图像进行3D重建的领域中，一个持续的挑战是在不依赖3D地面实况数据的情况下实现高精度重建。我们介绍了UNeR3D，这是一种开创性的无监督方法，为仅从2D视图生成详细的3D重建设定了新标准。我们的模型显著降低了与监督方法相关的训练成本，并将RGB着色引入3D点云，丰富了视觉体验。UNeR3D采用反向距离加权技术进行颜色渲染，可确保无缝的颜色转换，增强视觉逼真度。我们的模型的灵活架构支持使用任何数量的视图进行训练，唯一的是，在执行重建时，它不受训练期间使用的视图数量的限制。它可以在推理过程中使用任意数量的视图进行推理，提供了无与伦比的多功能性。此外，该模型的连续空间输入域允许以任何所需分辨率生成点云，从而能够创建高分辨率的3D RGB点云。我们用一种新颖的多视图几何损失和颜色损失来巩固重建过程，证明我们的模型在单视图输入及其他方面都很出色，从而重塑了3D视觉中无监督学习的范式。我们的贡献标志着3D视觉的巨大飞跃，为各种应用程序的内容创作提供了新的视野。代码位于https://github.com/hongbinlin3589/uner3d. et.al.|[2312.06706](http://arxiv.org/abs/2312.06706)|null|
|**2023-12-10**|**SuperPrimitive: Scene Reconstruction at a Primitive Level**|由于其计算复杂性和固有的视觉模糊性，从一组图像或单目视频中进行联合相机姿态和密集几何估计仍然是一个具有挑战性的问题。大多数密集增量重建系统直接对图像像素进行操作，并使用多视图几何提示来求解其3D位置。这种像素级方法存在模糊性或违反多视图一致性的问题（例如，由无纹理或镜面引起）。我们用一种新的图像表示来解决这个问题，我们称之为超原始。超基元是通过将图像分割成语义相关的局部区域并用估计的表面法线方向对其进行增强来获得的，这两者都是由最先进的单图像神经网络预测的。这提供了每个SuperPrimitive的局部几何体估计，而它们的相对位置是基于多视图观测进行调整的。我们通过解决三个3D重建任务来展示我们新表示的多功能性：深度完成、运动中的少量视图结构和单目密集视觉里程计。 et.al.|[2312.05889](http://arxiv.org/abs/2312.05889)|null|
|**2023-12-09**|**Light detection and Cosmic Rejection in the ICARUS LArTPC at Fermilab**|ICARUS-T600探测器是一个760吨的液氩时间投影室（LArPC），目前在费米实验室作为短基线中微子（SBN）计划中的远探测器运行。SBN计划由三个LArPC组成，其中心目标是测试无菌中微子假说。在Gran Sasso地下实验室工作了3年后，ICARUS探测器被运往欧洲核子研究中心，在那里它配备了360个8“光电倍增管用于新的光学检测系统。PMT系统检测来自液氩中相互作用的带电粒子的快速闪烁光，为全探测器生成触发信号，并允许对事件进行3D重建。现在探测器在浅层运行，暴露在高通量的宇宙射线中，这些宇宙射线可以伪造中微子的相互作用。为了减轻这种影响，安装了宇宙射线标记仪（CRT）和3米厚的混凝土。来自PMT和CRT子系统的精确定时信息可以帮助识别相互作用是来自ICARUS低温恒温器内部还是外部。本文综述了ICARUS中CRT和PMT光探测系统的宇宙成因背景减少和定时校准方法。 et.al.|[2312.05684](http://arxiv.org/abs/2312.05684)|null|
|**2023-12-08**|**Multi-view Inversion for 3D-aware Generative Adversarial Networks**|当前用于人类头部的3D GAN反演方法通常仅使用一个单个正面图像来重建整个3D头部模型。当多视图数据或动态视频可用时，这会遗漏有意义的信息。我们的方法建立在现有最先进的3D GAN反演技术的基础上，以实现同一主题的多个视图的一致和同时反演。我们使用多潜在扩展来处理动态人脸视频中存在的不一致性，以从序列中重新合成一致的3D表示。由于我们的方法使用了有关目标对象的额外信息，我们观察到几何精度和图像质量都有显著提高，尤其是在从宽视角进行渲染时。此外，我们展示了我们的反向3D渲染的可编辑性，这将它们与基于NeRF的场景重建区分开来。 et.al.|[2312.05330](http://arxiv.org/abs/2312.05330)|null|
|**2023-12-11**|**Nuvo: Neural UV Mapping for Unruly 3D Representations**|现有的UV映射算法被设计为在性能良好的网格上操作，而不是由最先进的3D重建和生成技术产生的几何表示。因此，将这些方法应用于由神经辐射场和相关技术（或从这些场三角化的网格）恢复的体积密度会导致纹理图谱过于分散，无法用于视图合成或外观编辑等任务。我们提出了一种UV映射方法，旨在对通过3D重建和生成技术产生的几何体进行操作。我们的方法Nuvo不是计算在网格顶点上定义的映射，而是使用神经场来表示连续的UV映射，并将其优化为仅针对一组可见点（即仅影响场景外观的点）的有效且性能良好的映射。我们展示了我们的模型对不良几何体带来的挑战是稳健的，并且它生成了可以表示详细外观的可编辑UV映射。 et.al.|[2312.05283](http://arxiv.org/abs/2312.05283)|null|
|**2023-12-08**|**Fine Dense Alignment of Image Bursts through Camera Pose and Depth Estimation**|本文介绍了一种新的方法来对手持相机拍摄的突发图像进行精细对准。与估计帧对之间的二维变换或依赖于离散对应关系的传统技术相比，所提出的算法通过优化每个像素的相机运动和表面深度和方向来建立密集的对应关系。这种方法改进了对齐，特别是在具有视差挑战的场景中。以小基线甚至微小基线为特征的合成爆发的广泛实验表明，在这种情况下，它的性能优于目前可用的最佳光流方法，而不需要任何训练。除了增强对齐之外，我们的方法还为简单图像恢复之外的任务开辟了途径，如深度估计和3D重建，这得到了有希望的初步结果的支持。这将我们的方法定位为用于各种突发图像处理应用的通用工具。 et.al.|[2312.05190](http://arxiv.org/abs/2312.05190)|null|

<p align=right>(<a href=#updated-on-20231214>back to top</a>)</p>

## Diffusion

|Publish Date|Title|Abstract|PDF|Code|
|---|---|---|---|---|
|**2023-12-13**|**Anti-Diffusion in an Algae-Bacteria Microcosm: Photosynthesis, Chemotaxis, and Expulsion**|在自然界中，来自两个生命王国的微生物之间存在着显著的关系，例如细菌向藻类提供维生素B $_{12}$。这种相互作用促使人们对代谢物交换的时空动力学进行一般性研究。在这里，我们通过实验和理论研究了一个模型系统：细菌$B的共培养。枯草杆菌$，一种对氧具有趋化性的专性需氧菌，以及藻类$C的非运动突变体。reinhardtii$ ，光照时可光合作用产生氧气。引人注目的是，当一束光照射到两者最初均匀的薄悬浮液时，细菌向光合作用活性区域的趋化性流入导致藻类从该区域排出。这种影响源于细菌在空间上变化的集体行为导致的藻类迁移，在数学上与恒星中磁通量排出相关的“湍流抗磁性”有关。 et.al.|[2312.08346](http://arxiv.org/abs/2312.08346)|null|
|**2023-12-13**|**PnPNet: Pull-and-Push Networks for Volumetric Segmentation with Boundary Confusion**|体积图像的精确边界分割是图像引导诊断和计算机辅助干预的关键任务，尤其是在临床实践中边界混淆的情况下。然而，由于缺乏边界形状约束，U形网络无法有效解决这一挑战。此外，现有的细化边界的方法过于强调细长结构，由于网络对微小物体建模的能力有限，导致了过拟合现象。在本文中，我们通过包含与相邻区域的相互作用动力学，重新定义了边界生成的机制。此外，我们提出了一个称为PnPNet的统一网络来模拟混淆边界区域的形状特征。PnPNet的核心成分包括推拉分支。具体来说，基于扩散理论，我们从推送分支设计了语义差分模块（SDM）来挤压边界区域。SDM内部的显式和隐式差分信息显著提高了类间边界的表示能力。此外，在K-means算法的激励下，引入了来自拉分支的类聚类模块（CCM）来拉伸相交的边界区域。因此，推分支和拉分支将分别缩小和扩大边界的不确定性。它们提供了两种对抗性的力量来促进模型输出更精确的边界描绘。我们在三个具有挑战性的公共数据集和一个内部数据集上进行了实验，其中包含模型预测中的三种类型的边界混淆。实验结果表明，PnPNet优于其他分割网络，尤其是在HD和ASSD的评估指标上。此外，推拉分支可以作为即插即用模块来增强经典的U形基线模型。代码可用。 et.al.|[2312.08323](http://arxiv.org/abs/2312.08323)|null|
|**2023-12-13**|**PhenDiff: Revealing Invisible Phenotypes with Conditional Diffusion Models**|在过去的五年里，深度生成模型逐渐被用于生物学研究的各种任务。值得注意的是，图像到图像的翻译方法在揭示人眼看不见的细微表型细胞变异方面显示出有效性。目前实现这一目标的方法主要依赖于生成对抗性网络（GANs）。然而，众所周知，这些模型存在一些缺点，如训练不稳定和模式崩溃。此外，缺乏将真实图像转换为训练的GAN的潜在图像的鲁棒性，阻碍了对真实图像的灵活编辑。在这项工作中，我们提出了PhenDiff，这是一种基于条件扩散模型的图像到图像的翻译方法，用于识别显微镜图像中的细微表型。我们在生物数据集上对这种方法进行了评估，并与之前的工作（如CycleGAN）进行了对比。我们表明，PhenDiff在生成图像的质量和多样性方面优于该基线。然后，我们应用这种方法在类器官的显微镜图像上显示由一种罕见的神经发育障碍引发的不可见的表型变化。总之，我们证明了PhenDiff能够进行高质量的生物图像到图像的翻译，从而在真实图像上发现细微的表型变化。 et.al.|[2312.08290](http://arxiv.org/abs/2312.08290)|**[link](https://github.com/warmongeringbeaver/phendiff)**|
|**2023-12-13**|**Revisiting the stochastic QCD axion window: departure from equilibrium during inflation**|如果暗物质是由QCD轴子组成的，其丰度由轴子场在膨胀过程中获得的真空期望值决定。轴子通常被认为遵循膨胀过程中量子扩散产生的平衡分布。这导致了所谓的随机窗口，在该窗口下，QCD轴子可以构成所有的暗物质。它的特征是 $10^｛10.4｝\mathrm｛GeV｝\leq f\leq 10^｝｛17.2｝\mathrm｝$和$H_。然而，在现实的通货膨胀潜力中，我们证明轴子在通货膨胀结束时永远不会达到均衡分布。这是因为轴子的放松时间远大于通货膨胀期间H$变化的典型时间尺度。因此，只要轴子在膨胀过程中保持较轻，轴子就会获得准平坦分布。这导致我们重新评估随机轴子窗口，我们发现$10^｛10.3｝\mathrm｛GeV｝\leq f\leq 10^｛14.1｝\math rm｛GeV｝$和$ H_。 et.al.|[2312.08231](http://arxiv.org/abs/2312.08231)|null|
|**2023-12-13**|**Black-box Membership Inference Attacks against Fine-tuned Diffusion Models**|随着基于扩散的图像生成模型的快速发展，生成的图像质量变得越来越逼真。此外，随着高质量的预训练图像生成模型的发布，越来越多的用户正在下载这些预训练模型，以将其与下游数据集进行微调，用于各种图像生成任务。然而，在下游任务中使用这种强大的预训练模型会带来显著的隐私泄露风险。在本文中，我们提出了第一个基于重构的成员推断攻击框架，该框架针对最近的扩散模型进行了定制，并在更严格的黑匣子访问设置中进行了定制。考虑到四种不同的攻击场景和三种类型的攻击，该框架能够针对任何流行的条件生成器模型，实现高精度，0.95美元的AUC令人印象深刻。 et.al.|[2312.08207](http://arxiv.org/abs/2312.08207)|null|
|**2023-12-13**|**SPD-DDPM: Denoising Diffusion Probabilistic Models in the Symmetric Positive Definite Space**|对称正定矩阵在统计学和机器学习中显示出重要的价值和应用，如FMRI分析和交通预测。先前关于SPD矩阵的工作主要集中在判别模型上，其中直接对 $E（X|y）$进行预测，其中$y$是向量，$X$是SPD矩阵。然而，这些方法在处理大规模数据时具有挑战性，因为它们需要访问和处理整个数据。在本文中，受去噪扩散概率模型~（DDPM）的启发，我们提出了一种新的生成模型，称为SPD-DDPM，通过在SPD空间中引入高斯分布来估计$E（X|y）$。此外，我们的模型能够无条件、灵活地估计$p（X）$，而不需要给出$y$。一方面，该模型有条件地学习$p（X|y）$，并利用样本的平均值来获得$E（X|y）$作为预测。另一方面，模型无条件地学习数据$p（X）$ 的概率分布，并生成符合该分布的样本。此外，我们提出了一种新的SPD网络，它比以前的网络更深，并允许包含条件因素。对玩具数据和真实出租车数据的实验结果表明，我们的模型有效地无条件和无条件地拟合了数据分布，并提供了准确的预测。 et.al.|[2312.08200](http://arxiv.org/abs/2312.08200)|null|
|**2023-12-13**|**Concept-centric Personalization with Large-scale Diffusion Priors**|尽管大规模的扩散模型能够高度生成多样化的开放世界内容，但它们仍然难以与特定概念生成器的真实感和保真度相匹配。在这项工作中，我们提出了为特定概念定制大规模扩散先验的任务，作为以概念为中心的个性化。我们的目标是生成高质量的以概念为中心的图像，同时保持开放世界模型固有的多功能可控性，使其能够应用于各种任务，如以概念为核心的风格化和图像翻译。为了应对这些挑战，我们将从扩散先验中灾难性地忘记引导预测确定为根本问题。因此，我们开发了一个专门为解决这一任务而设计的引导解耦个性化框架。我们提出了广义无分类器制导（GCFG）作为我们框架的基础理论。这种方法扩展了无分类器制导（CFG），以适应来自各种条件和模型的任意数量的制导。采用GCFG使我们能够将条件制导分为两个不同的组成部分：保真度的概念制导和可控性的控制制导。这一划分使得训练概念制导的专门模型变得可行，同时确保控制和无条件制导保持不变。然后，我们提出了一个以空文本概念为中心的扩散模型，作为特定概念的生成器，在不需要文本注释的情况下学习概念指导。代码将在https://github.com/priv-creation/concept-centric-personalization. et.al.|[2312.08195](http://arxiv.org/abs/2312.08195)|**[link](https://github.com/priv-creation/concept-centric-personalization)**|
|**2023-12-13**|**$ρ$-Diffusion: A diffusion-based density estimation framework for computational physics**|在物理学中，密度$\rho（\cdot）$是一个非常重要的标量函数，因为它描述了控制物理过程的标量场或概率密度函数。然而，建模$\rho（\cdot）$通常与参数空间的比例关系很差，并且很快变得非常困难和计算成本高昂。绕过这一点的一个有希望的途径是利用高保真图像生成中常用的去噪扩散模型的能力，从现有的科学数据中参数化$\rho（\cdot）$，从这些数据中可以轻松地对新样本进行采样。在本文中，我们提出了$\rho$-Diffusion，这是一种用于物理多维密度估计的去噪-扩散概率模型的实现，目前正在积极开发中，从我们的结果来看，它在物理激励的2D和3D密度函数上表现良好。此外，我们提出了一种新的哈希技术，该技术允许$\rho$ -扩散受到任意数量的感兴趣物理参数的约束。 et.al.|[2312.08153](http://arxiv.org/abs/2312.08153)|null|
|**2023-12-13**|**A cross-diffusion system modelling rivaling gangs: global existence of bounded solutions and FCT stabilization for numerical simulation**|对于帮派属地模型\beggin｛align*｝\begon｛cases｝u_t=D_u\Delta u+\chi_u\nabla\cdot（u\nabla w），\\v_t=D_v\Delta v+\chi_v\nabla/cdot（v\nabla z），\\w_t=-w+\frac｛v｝｛1+v｝，\\z_t=-z+\frac｛u｝{1+u｝，\end{cases}\end{align*}其中 $u$和$v$表示两个相互竞争的帮派的密度，这两个帮派喷射涂鸦（密度分别为$z$和$w$）并部分远离另一帮派的涂鸦，我们构建了全局的、有界的经典解。通过使用定量全局估计，我们证明了如果$\|u_0\|_{L^\infty（\Omega）}$和$\|v_0\|_{L^\ infty（\ Omega）}$ 足够小，这些解收敛到齐次稳态。此外，我们进行的数值实验表明，对于不同的参数选择，系统可能会变成扩散或对流主导的，其中在前一种情况下，解收敛于恒定稳态，而在后一种情况中，观察到非平凡的渐近行为，如偏析。为了进行这些实验，我们应用了一种保正的非线性有限元通量校正传输方法（FEM-FCT）。然后，我们使用不定点迭代同时处理系统和所提出的非线性方案中的非线性。 et.al.|[2312.08147](http://arxiv.org/abs/2312.08147)|null|
|**2023-12-13**|**Clockwork Diffusion: Efficient Generation With Model-Step Distillation**|这项工作旨在提高文本到图像扩散模型的效率。虽然扩散模型在每个生成步骤中都使用计算成本高昂的基于UNet的去噪操作，但我们发现，并非所有操作都与最终输出质量同等相关。特别是，我们观察到，在高分辨率特征图上操作的UNet层对小扰动相对敏感。相反，低分辨率特征图会影响最终图像的语义布局，并且通常会受到干扰，而输出没有明显变化。基于这一观察结果，我们提出了Clockwork Diffusion，这是一种周期性地重复使用先前去噪步骤的计算，以在一个或多个后续步骤中近似低分辨率特征图的方法。对于多个基线，以及文本到图像的生成和图像编辑，我们证明了Clockwork可以显著降低计算复杂度，从而获得可比或改进的感知分数。例如，对于带有8个DPM++步骤的Stable Diffusion v1.5，我们节省了32%的FLOP，而FID和CLIP的变化可以忽略不计。 et.al.|[2312.08128](http://arxiv.org/abs/2312.08128)|null|

<p align=right>(<a href=#updated-on-20231214>back to top</a>)</p>

## NeRF

|Publish Date|Title|Abstract|PDF|Code|
|---|---|---|---|---|
|**2023-12-12**|**SMERF: Streamable Memory Efficient Radiance Fields for Real-Time Large-Scene Exploration**|最近的实时视图合成技术在保真度和速度上迅速进步，现代方法能够以交互式帧速率渲染接近照片级真实感的场景。与此同时，在易于光栅化的显式场景表示和基于射线行进的神经场之间出现了紧张关系，后者的最先进实例在质量上超过了前者，同时对于实时应用来说成本高得令人望而却步。在这项工作中，我们介绍了SMERF，这是一种视图合成方法，在占地面积高达3亿 $^2$、体积分辨率为3.5毫米$^3$ 的大型场景中，它实现了实时方法中最先进的精度。我们的方法建立在两个主要贡献之上：一个是分层模型划分方案，它在限制计算和内存消耗的同时增加了模型容量，另一个是蒸馏训练策略，它同时产生高保真度和内部一致性。我们的方法能够在网络浏览器中实现全六自由度（6DOF）导航，并在商品智能手机和笔记本电脑上实时渲染。大量实验表明，我们的方法在实时新视图合成方面，在标准基准上超过了当前最先进的0.78 dB，在大型场景上超过了1.78 dB，渲染帧的速度比最先进的辐射场模型快三个数量级，并在包括智能手机在内的各种商品设备上实现了实时性能。我们鼓励读者在我们的项目网站上亲自探索这些模型：https://smerf-3d.github.io. et.al.|[2312.07541](http://arxiv.org/abs/2312.07541)|null|
|**2023-12-09**|**Robo360: A 3D Omnispective Multi-Material Robotic Manipulation Dataset**|长期以来，制造能够自动化劳动密集型任务的机器人一直是计算机视觉和机器人界进步的核心动力。最近人们对利用3D算法，特别是神经领域的兴趣，导致了机器人在操作场景中的感知和物理理解方面的进步。然而，现实世界的复杂性带来了重大挑战。为了应对这些挑战，我们提出了Robo360，这是一个以机器人操作为特征的数据集，具有密集的视图覆盖范围，能够实现高质量的3D神经表示学习，以及一组具有各种物理和光学特性的不同对象，有助于各种对象操作和物理世界建模任务的研究。我们使用现有的动态NeRF来确认我们的数据集的有效性，并评估其在学习多视图策略方面的潜力。我们希望Robo360能够在理解3D物理世界和机器人控制的交叉点上开辟新的研究方向。 et.al.|[2312.06686](http://arxiv.org/abs/2312.06686)|null|
|**2023-12-11**|**Representing stimulus motion with waves in adaptive neural fields**|神经活动的行波在皮层网络中自发出现，并对刺激做出反应。波的时空结构可以指示它们编码的信息以及维持它们的生理过程。在这里，我们研究了作为视觉运动处理模型的自适应神经场中出现的行波的刺激响应关系。神经场方程将皮层组织的活动建模为连续的可兴奋介质，自适应过程提供负反馈，产生局部活动模式。在我们的模型中，突触连接由一个积分核来描述，该积分核由于依赖于活动的突触抑制而动态减弱，导致边缘稳定的行进前沿（具有衰减的后部）或固定速度的脉冲。我们的分析量化了弱刺激如何随着时间的推移改变这些波的相对位置，其特征是我们扰动地获得的波响应函数。持续和连续可见的刺激模拟移动的视觉对象。在视觉空间中跳跃的间歇性闪光可以产生流畅的视觉运动体验。我们的理论和数值模拟很好地描述了波对两种运动刺激的夹带，提供了视觉运动感知的机制描述。 et.al.|[2312.06100](http://arxiv.org/abs/2312.06100)|null|
|**2023-12-10**|**Accurate Differential Operators for Hybrid Neural Fields**|神经场已广泛应用于从形状表示到神经渲染以及求解偏微分方程（PDE）的各个领域。随着混合神经场表示的出现，如利用小MLP和显式表示的即时NGP，这些模型训练迅速，可以适应大型场景。然而，在渲染和模拟等许多应用中，混合神经场可能会导致明显且不合理的伪影。这是因为它们不能产生这些下游应用所需的精确的空间导数。在这项工作中，我们提出了两种规避这些挑战的方法。我们的第一种方法是一种事后算子，它使用局部多项式拟合从预先训练的混合神经场中获得更准确的导数。此外，我们还提出了一种自监督微调方法，该方法在保留初始信号的同时，对神经场进行细化，以直接产生准确的导数。我们展示了我们的方法在渲染、碰撞模拟和求解偏微分方程中的应用。我们观察到，使用我们的方法可以产生更准确的导数，减少伪影，并在下游应用中实现更准确的模拟。 et.al.|[2312.05984](http://arxiv.org/abs/2312.05984)|null|
|**2023-12-11**|**Nuvo: Neural UV Mapping for Unruly 3D Representations**|现有的UV映射算法被设计为在性能良好的网格上操作，而不是由最先进的3D重建和生成技术产生的几何表示。因此，将这些方法应用于由神经辐射场和相关技术（或从这些场三角化的网格）恢复的体积密度会导致纹理图谱过于分散，无法用于视图合成或外观编辑等任务。我们提出了一种UV映射方法，旨在对通过3D重建和生成技术产生的几何体进行操作。我们的方法Nuvo不是计算在网格顶点上定义的映射，而是使用神经场来表示连续的UV映射，并将其优化为仅针对一组可见点（即仅影响场景外观的点）的有效且性能良好的映射。我们展示了我们的模型对不良几何体带来的挑战是稳健的，并且它生成了可以表示详细外观的可编辑UV映射。 et.al.|[2312.05283](http://arxiv.org/abs/2312.05283)|null|
|**2023-12-08**|**Dynamic LiDAR Re-simulation using Compositional Neural Fields**|我们介绍了DyNFL，这是一种新的基于神经场的方法，用于动态驾驶场景中激光雷达扫描的高保真度重新模拟。DyNFL处理来自动态环境的激光雷达测量，并伴随着移动物体的边界框，以构建可编辑的神经场。该字段包括单独重建的静态背景和动态对象，允许用户在重新模拟的场景中修改视点、调整对象位置以及无缝添加或删除对象。我们方法的一个关键创新是神经场合成技术，该技术通过光线下降测试有效地集成了来自各种场景的重建神经资产，考虑到了遮挡和透明表面。我们对合成和真实世界环境的评估表明，\ShortName大大改进了基于激光雷达扫描的动态场景模拟，提供了物理保真度和灵活编辑功能的组合。 et.al.|[2312.05247](http://arxiv.org/abs/2312.05247)|null|
|**2023-12-08**|**TriHuman : A Real-time and Controllable Tri-plane Representation for Detailed Human Geometry and Appearance Synthesis**|仅从视频数据中创建可控、逼真和几何细节的真人数字替身是计算机图形学和视觉领域的一个关键挑战，尤其是在需要实时性能的情况下。最近的方法将神经辐射场（NeRF）连接到关节结构，例如身体模型或骨骼，以将点映射到姿势规范空间中，同时将NeRF调节在骨骼姿势上。这些方法通常使用多层感知器（MLP）对神经场进行参数化，导致运行时间缓慢。为了解决这一缺点，我们提出了一种新的人体定制、可变形和高效的三平面表示TriHuman，它实现了实时性能、最先进的姿态可控几何合成以及逼真的渲染质量。在核心，我们将全局光线样本非刚性地扭曲到未变形的三平面纹理空间中，这有效地解决了全局点映射到相同三平面位置的问题。然后，我们展示了如何将这种三平面特征表示以骨骼运动为条件，以考虑动态外观和几何结构的变化。我们的研究结果表明，在人类的几何形状和外观建模以及运行时性能方面，朝着更高质量迈出了明确的一步。 et.al.|[2312.05161](http://arxiv.org/abs/2312.05161)|null|
|**2023-12-08**|**GIR: 3D Gaussian Inverse Rendering for Relightable Scene Factorization**|本文提出了一种用于可重照明场景分解的三维高斯逆绘制方法GIR。与利用离散网格或神经隐式场进行反向渲染的现有方法相比，我们的方法利用3D高斯从多视图图像中估计对象的材料特性、照明和几何结构。我们的研究动机是有证据表明，在性能、多功能性和效率方面，3D高斯是比神经领域更有前途的主干。在本文中，我们旨在回答以下问题：“如何应用3D高斯来提高反向渲染的性能？”为了解决基于离散且通常在均匀分布的3D高斯表示中估计法线的复杂性，我们提出了一种高效的自正则化方法，该方法有助于在不需要额外监督的情况下对曲面法线进行建模。为了重建间接照明，我们提出了一种模拟光线跟踪的方法。大量实验证明，在反向渲染中，我们提出的GIR在各种广泛使用的数据集上跨多个任务的性能优于现有方法。这证实了它的功效和广泛的适用性，突出了它作为重新照明和重建中有影响力的工具的潜力。项目页面：https://3dgir.github.io et.al.|[2312.05133](http://arxiv.org/abs/2312.05133)|null|
|**2023-12-06**|**Gaussian-Flow: 4D Reconstruction with Dynamic 3D Gaussian Particle**|我们介绍了高斯流，这是一种新的基于点的方法，用于快速动态场景重建和多视图和单目视频的实时渲染。与因训练和渲染速度缓慢而受到阻碍的流行的基于NeRF的方法相比，我们的方法利用了基于点的3D高斯散射（3DGS）的最新进展。具体而言，提出了一种新的双域变形模型（DDDM）来显式地对每个高斯点的属性变形进行建模，其中通过时域中的多项式拟合和频域中的傅立叶级数拟合来捕获每个属性的时间相关残差。所提出的DDDM能够对长视频镜头中的复杂场景变形进行建模，消除了为每帧训练单独的3DGS的需要，或者引入了额外的隐式神经场来对3D动力学进行建模。此外，离散高斯点的显式变形建模确保了4D场景的超快速训练和渲染，这与为静态3D重建设计的原始3DGS相当。我们提出的方法展示了显著的效率提高，与每帧3DGS建模相比，训练速度快了5倍。此外，定量结果表明，所提出的高斯流在新视图渲染质量方面显著优于以前的主流方法。项目页面：https://nju-3dv.github.io/projects/gaussian-flow et.al.|[2312.03431](http://arxiv.org/abs/2312.03431)|null|
|**2023-12-06**|**Artist-Friendly Relightable and Animatable Neural Heads**|创建照片逼真数字化身的一种越来越常见的方法是通过使用体积神经场。当在一组多视图图像上训练时，原始神经辐射场（NeRF）允许静态头部进行令人印象深刻的新颖视图合成，后续方法表明，这些神经表示可以扩展到动态化身。最近，新的变体也超过了神经表示中烘焙照明的常见缺点，表明静态神经化身可以在任何环境中重新发光。在这项工作中，我们同时解决了运动和照明问题，为可重新照明和可动画化的神经头提出了一种新方法。我们的方法建立在一种已验证的动态化身方法的基础上，该方法基于体积基元的混合，结合最近提出的用于可重新照明神经场的轻量级硬件设置，并包括一种新的架构，该架构允许重新照明动态神经化身在任何环境中执行看不见的表情，即使是在近场照明和视点的情况下。 et.al.|[2312.03420](http://arxiv.org/abs/2312.03420)|null|

<p align=right>(<a href=#updated-on-20231214>back to top</a>)</p>

[contributors-shield]: https://img.shields.io/github/contributors/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[contributors-url]: https://github.com/Vincentqyw/cv-arxiv-daily/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[forks-url]: https://github.com/Vincentqyw/cv-arxiv-daily/network/members
[stars-shield]: https://img.shields.io/github/stars/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[stars-url]: https://github.com/Vincentqyw/cv-arxiv-daily/stargazers
[issues-shield]: https://img.shields.io/github/issues/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[issues-url]: https://github.com/Vincentqyw/cv-arxiv-daily/issues

