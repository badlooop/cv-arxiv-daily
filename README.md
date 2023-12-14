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
|**2023-12-12**|**SMERF: Streamable Memory Efficient Radiance Fields for Real-Time Large-Scene Exploration**|最近的实时视图合成技术在保真度和速度上迅速进步，现代方法能够以交互式帧速率渲染接近照片级真实感的场景。与此同时，在易于光栅化的显式场景表示和基于射线行进的神经场之间出现了紧张关系，后者的最先进实例在质量上超过了前者，同时对于实时应用来说成本高得令人望而却步。在这项工作中，我们介绍了SMERF，这是一种视图合成方法，在占地面积高达3亿 $^2$、体积分辨率为3.5毫米$^3$ 的大型场景中，它实现了实时方法中最先进的精度。我们的方法建立在两个主要贡献之上：一个是分层模型划分方案，它在限制计算和内存消耗的同时增加了模型容量，另一个是蒸馏训练策略，它同时产生高保真度和内部一致性。我们的方法能够在网络浏览器中实现全六自由度（6DOF）导航，并在商品智能手机和笔记本电脑上实时渲染。大量实验表明，我们的方法在实时新视图合成方面，在标准基准上超过了当前最先进的0.78 dB，在大型场景上超过了1.78 dB，渲染帧的速度比最先进的辐射场模型快三个数量级，并在包括智能手机在内的各种商品设备上实现了实时性能。我们鼓励读者在我们的项目网站上亲自探索这些模型：https://smerf-3d.github.io. et.al.|[2312.07541](http://arxiv.org/abs/2312.07541)|null|
|**2023-12-12**|**COLMAP-Free 3D Gaussian Splatting**|虽然神经渲染在场景重建和新颖的视图合成方面取得了令人印象深刻的进展，但它在很大程度上依赖于精确预计算的相机姿态。为了放松这一限制，已经做出了多项努力来训练神经辐射场（NeRF），而不需要预处理相机姿势。然而，NeRF的隐式表示为同时优化3D结构和相机姿态提供了额外的挑战。另一方面，鉴于其明确的点云表示，最近提出的3D高斯飞溅提供了新的机会。本文利用输入视频流的显式几何表示和连续性来执行新的视图合成，而无需任何SfM预处理。我们以顺序的方式处理输入帧，并通过一次获取一个输入帧来逐步增长3D高斯集，而无需预先计算相机姿势。在大的运动变化下，我们的方法在视图合成和相机姿态估计方面比以前的方法有了显著的改进。我们的项目页面是https://oasisyang.github.io/colmap-free-3dgs et.al.|[2312.07504](http://arxiv.org/abs/2312.07504)|null|
|**2023-12-12**|**NVS-Adapter: Plug-and-Play Novel View Synthesis from a Single Image**|大规模文本到图像（T2I）模型的迁移学习最近在从单个图像中对不同对象进行新视图合成（NVS）方面显示出了令人印象深刻的潜力。虽然以前的方法通常在NVS的多视图数据集上训练大型模型，但微调T2I模型的整个参数不仅需要高成本，而且降低了T2I模型在新领域中生成不同图像的泛化能力。在这项研究中，我们提出了一种有效的方法，称为NVS适配器，它是T2I模型的即插即用模块，在充分利用T2I模型泛化能力的同时，合成视觉对象的新颖多视图。NVS适配器由两个主要组件组成；视图一致性交叉注意学习视觉对应关系以对齐视图特征的局部细节，全局语义条件将生成的视图的语义结构与参考视图对齐。实验结果表明，NVS适配器可以有效地合成几何一致的多视图，并且在不完全微调T2I模型的情况下在基准测试上实现高性能。代码和数据可在~\href中公开获取{https://postech-cvlab.github.io/nvsadapter/}{https://postech-cvlab.github.io/nvsadapter/}。 et.al.|[2312.07315](http://arxiv.org/abs/2312.07315)|null|
|**2023-12-12**|**Unifying Correspondence, Pose and NeRF for Pose-Free Novel View Synthesis from Stereo Pairs**|这项工作深入研究了从立体对合成无姿势的新颖视图的任务，这是3D视觉中一项具有挑战性和开创性的任务。与以往任何框架不同，我们的创新框架无缝集成了2D对应匹配、相机姿态估计和NeRF渲染，促进了这些任务的协同增强。我们通过设计一种利用共享表示的架构来实现这一点，该架构是增强3D几何理解的基础。利用任务之间固有的相互作用，我们的统一框架使用所提出的训练策略进行端到端训练，以提高整体模型的准确性。通过对来自两个真实世界数据集的不同室内和室外场景的广泛评估，我们证明了我们的方法比以前的方法有了实质性的改进，特别是在以极端视角变化和缺乏准确相机姿势为特征的场景中。 et.al.|[2312.07246](http://arxiv.org/abs/2312.07246)|**[link](https://github.com/KU-CVLAB/CoPoNeRF)**|
|**2023-12-11**|**Gaussian Splatting SLAM**|我们首次将3D高斯散射应用于使用单个移动单目或RGB-D相机的增量3D重建。我们的同步定位和映射（SLAM）方法以3fps实时运行，使用高斯作为唯一的3D表示，统一了所需的表示，以实现准确、高效的跟踪、映射和高质量渲染。需要一些创新来从现场摄像机连续重建具有高保真度的3D场景。首先，为了超越最初的3DGS算法，该算法需要来自离线运动结构（SfM）系统的精确姿态，我们使用针对3D高斯的直接优化来制定3DGS的相机跟踪，并表明这能够实现快速而稳健的跟踪，并具有广泛的收敛范围。其次，通过利用高斯的显式性质，我们引入了几何验证和正则化来处理增量三维密集重建中出现的模糊性。最后，我们介绍了一个完整的SLAM系统，它不仅在新的视图合成和轨迹估计方面取得了最先进的结果，而且还重建了微小甚至透明的物体。 et.al.|[2312.06741](http://arxiv.org/abs/2312.06741)|null|
|**2023-12-11**|**UpFusion: Novel View Diffusion from Unposed Sparse View Observations**|我们提出了UpFusion，这是一种在没有相应姿态信息的情况下，在给定稀疏参考图像集的情况下可以执行新颖的视图合成并推断对象的3D表示的系统。当前的稀疏视图3D推理方法通常依赖于相机姿态来几何地聚合来自输入视图的信息，但当这种信息不可用/不准确时，这种方法在野外并不稳健。相反，UpFusion通过学习在条件生成模型中隐含地利用可用图像作为上下文来合成新视图，从而避开了这一要求。我们将两种互补的条件反射形式结合到扩散模型中，以利用输入视图：a）通过使用场景级变换器推断与查询视图对齐的特征，b）通过可以直接观察输入图像标记的中间注意力层。我们表明，这种机制允许生成高保真度的新视图，同时在给定额外（未着色）图像的情况下提高合成质量。我们在Co3Dv2和Google Scanned Objects数据集上评估了我们的方法，并展示了与依赖姿势的稀疏视图方法以及无法利用其他视图的单视图方法相比，我们的方法的优势。最后，我们还表明，我们学习的模型可以超越训练类别进行推广，甚至可以从野外通用对象的自捕获图像中进行重建。 et.al.|[2312.06661](http://arxiv.org/abs/2312.06661)|null|
|**2023-12-11**|**Learning Naturally Aggregated Appearance for Efficient 3D Editing**|将3D场景表示为颜色场和密度场的神经辐射场在新视图合成方面取得了巨大进展，但由于其隐含性，不利于编辑。鉴于这种不足，我们建议用显式的2D外观聚合（也称为规范图像）来代替颜色场，用户可以通过2D图像处理轻松地自定义他们的3D编辑。为了避免失真效应并便于编辑，我们用投影场来补充规范图像，该投影场将3D点映射到2D像素上以进行纹理查找。该字段使用伪规范相机模型仔细初始化，并使用偏移规则性进行优化，以确保聚合外观的自然度。在三个数据集上的大量实验结果表明，我们称为AGAP的表示很好地支持各种3D编辑方式（例如，风格化、交互式绘图和内容提取），而无需对每种情况进行重新优化，证明了其可推广性和效率。项目页面位于https://felixcheng97.github.io/agap/. et.al.|[2312.06657](http://arxiv.org/abs/2312.06657)|**[link](https://github.com/felixcheng97/agap)**|
|**2023-12-11**|**CorresNeRF: Image Correspondence Priors for Neural Radiance Fields**|神经辐射场（NeRFs）在新的视图合成和表面重建任务中取得了令人印象深刻的结果。然而，在具有稀疏输入视图的具有挑战性的场景下，它们的性能会受到影响。我们提出了CorresNeRF，这是一种利用现有方法计算的图像对应先验来监督NeRF训练的新方法。我们设计了用于增强和滤波的自适应过程，以生成密集和高质量的对应关系。然后，通过对应像素重投影和深度损失项，使用对应来正则化NeRF训练。我们在不同的数据集上使用基于密度和基于SDF的NeRF模型评估了我们在新的视图合成和表面重建任务中的方法。我们的方法在光度和几何度量方面都优于以前的方法。我们表明，这种使用对应先验的简单而有效的技术可以作为即插即用模块应用于不同的NeRF变体。项目页面位于https://yxlao.github.io/corres-nerf. et.al.|[2312.06642](http://arxiv.org/abs/2312.06642)|**[link](https://github.com/yxlao/corres-nerf)**|
|**2023-12-11**|**NVFi: Neural Velocity Fields for 3D Physics Learning from Dynamic Videos**|在本文中，我们的目标是从多视图视频中对3D场景动力学进行建模。与大多数现有工作通常专注于训练时间段内的新视图合成这一常见任务不同，我们建议仅从视频帧中同时学习3D场景的几何、外观和物理速度，从而可以支持多种理想的应用，包括未来的帧外推、无监督的3D语义场景分解，以及动态运动传递。我们的方法由三个主要组成部分组成，1）关键帧动态辐射场，2）帧间速度场，以及3）联合关键帧和帧间优化模块，这是我们框架的核心，可以有效地训练两个网络。为了验证我们的方法，我们进一步引入了两个动态3D数据集：1）动态对象数据集和2）动态室内场景数据集。我们在多个数据集上进行了广泛的实验，证明了我们的方法在所有基线上的优越性能，特别是在未来的帧外推和无监督三维语义场景分解的关键任务中。 et.al.|[2312.06398](http://arxiv.org/abs/2312.06398)|null|
|**2023-12-11**|**Nuvo: Neural UV Mapping for Unruly 3D Representations**|现有的UV映射算法被设计为在性能良好的网格上操作，而不是由最先进的3D重建和生成技术产生的几何表示。因此，将这些方法应用于由神经辐射场和相关技术（或从这些场三角化的网格）恢复的体积密度会导致纹理图谱过于分散，无法用于视图合成或外观编辑等任务。我们提出了一种UV映射方法，旨在对通过3D重建和生成技术产生的几何体进行操作。我们的方法Nuvo不是计算在网格顶点上定义的映射，而是使用神经场来表示连续的UV映射，并将其优化为仅针对一组可见点（即仅影响场景外观的点）的有效且性能良好的映射。我们展示了我们的模型对不良几何体带来的挑战是稳健的，并且它生成了可以表示详细外观的可编辑UV映射。 et.al.|[2312.05283](http://arxiv.org/abs/2312.05283)|null|

<p align=right>(<a href=#updated-on-20231214>back to top</a>)</p>

## 3D Reconstruction

|Publish Date|Title|Abstract|PDF|Code|
|---|---|---|---|---|
|**2023-12-12**|**Adaptive Confidence Multi-View Hashing for Multimedia Retrieval**|多视图哈希方法将多个视图中的异构数据转换为二进制哈希码，是多媒体检索的关键技术之一。然而，目前的方法主要探讨多个观点之间的互补性，而缺乏信心学习和融合。此外，在实际应用场景中，单视图数据包含冗余噪声。为了进行置信度学习并消除不必要的噪声，我们提出了一种新的自适应置信度多视图哈希（ACMVH）方法。首先，开发了置信网络来从各种单视图特征中提取有用信息并去除噪声信息。此外，采用自适应置信度多视图网络来测量每个视图的置信度，然后通过加权求和来融合多视图特征。最后，设计了一个扩展网络来进一步增强融合特征的特征表示。据我们所知，我们率先将置信学习应用于多媒体检索领域。在两个公共数据集上进行的大量实验表明，所提出的ACMVH比最先进的方法性能更好（最大增加了3.24%）。源代码可在https://github.com/hackerhyper/acmvh. et.al.|[2312.07327](http://arxiv.org/abs/2312.07327)|**[link](https://github.com/hackerhyper/acmvh)**|
|**2023-12-11**|**Gaussian Splatting SLAM**|我们首次将3D高斯散射应用于使用单个移动单目或RGB-D相机的增量3D重建。我们的同步定位和映射（SLAM）方法以3fps实时运行，使用高斯作为唯一的3D表示，统一了所需的表示，以实现准确、高效的跟踪、映射和高质量渲染。需要一些创新来从现场摄像机连续重建具有高保真度的3D场景。首先，为了超越最初的3DGS算法，该算法需要来自离线运动结构（SfM）系统的精确姿态，我们使用针对3D高斯的直接优化来制定3DGS的相机跟踪，并表明这能够实现快速而稳健的跟踪，并具有广泛的收敛范围。其次，通过利用高斯的显式性质，我们引入了几何验证和正则化来处理增量三维密集重建中出现的模糊性。最后，我们介绍了一个完整的SLAM系统，它不仅在新的视图合成和轨迹估计方面取得了最先进的结果，而且还重建了微小甚至透明的物体。 et.al.|[2312.06741](http://arxiv.org/abs/2312.06741)|null|
|**2023-12-10**|**UNeR3D: Versatile and Scalable 3D RGB Point Cloud Generation from 2D Images in Unsupervised Reconstruction**|在从2D图像进行3D重建的领域中，一个持续的挑战是在不依赖3D地面实况数据的情况下实现高精度重建。我们介绍了UNeR3D，这是一种开创性的无监督方法，为仅从2D视图生成详细的3D重建设定了新标准。我们的模型显著降低了与监督方法相关的训练成本，并将RGB着色引入3D点云，丰富了视觉体验。UNeR3D采用反向距离加权技术进行颜色渲染，可确保无缝的颜色转换，增强视觉逼真度。我们的模型的灵活架构支持使用任何数量的视图进行训练，唯一的是，在执行重建时，它不受训练期间使用的视图数量的限制。它可以在推理过程中使用任意数量的视图进行推理，提供了无与伦比的多功能性。此外，该模型的连续空间输入域允许以任何所需分辨率生成点云，从而能够创建高分辨率的3D RGB点云。我们用一种新颖的多视图几何损失和颜色损失来巩固重建过程，证明我们的模型在单视图输入及其他方面都很出色，从而重塑了3D视觉中无监督学习的范式。我们的贡献标志着3D视觉的巨大飞跃，为各种应用程序的内容创作提供了新的视野。代码位于https://github.com/hongbinlin3589/uner3d. et.al.|[2312.06706](http://arxiv.org/abs/2312.06706)|null|
|**2023-12-10**|**SuperPrimitive: Scene Reconstruction at a Primitive Level**|由于其计算复杂性和固有的视觉模糊性，从一组图像或单目视频中进行联合相机姿态和密集几何估计仍然是一个具有挑战性的问题。大多数密集增量重建系统直接对图像像素进行操作，并使用多视图几何提示来求解其3D位置。这种像素级方法存在模糊性或违反多视图一致性的问题（例如，由无纹理或镜面引起）。我们用一种新的图像表示来解决这个问题，我们称之为超原始。超基元是通过将图像分割成语义相关的局部区域并用估计的表面法线方向对其进行增强来获得的，这两者都是由最先进的单图像神经网络预测的。这提供了每个SuperPrimitive的局部几何体估计，而它们的相对位置是基于多视图观测进行调整的。我们通过解决三个3D重建任务来展示我们新表示的多功能性：深度完成、运动中的少量视图结构和单目密集视觉里程计。 et.al.|[2312.05889](http://arxiv.org/abs/2312.05889)|null|
|**2023-12-09**|**Light detection and Cosmic Rejection in the ICARUS LArTPC at Fermilab**|ICARUS-T600探测器是一个760吨的液氩时间投影室（LArPC），目前在费米实验室作为短基线中微子（SBN）计划中的远探测器运行。SBN计划由三个LArPC组成，其中心目标是测试无菌中微子假说。在格兰萨索地下实验室运行了3年后，ICARUS探测器被运送到欧洲核子研究中心，在那里它配备了360个8“光电倍增管（PMT），用于一个新的光学探测系统。PMT系统探测来自液氩中相互作用的带电粒子的快速闪烁光，为整个探测器产生触发信号，并允许对事件进行3D重建。现在在浅层运行，探测器暴露在高通量的宇宙射线中，这些宇宙射线可以伪造中微子的相互作用。为了减轻这种影响，安装了一个宇宙射线标记器（CRT）和一个3米厚的混凝土。来自PMT和CRT子系统的精确定时信息可以帮助识别相互作用是来自内部还是外部。本文综述了ICARUS中CRT和PMT光探测系统的宇宙背景减少和定时校准方法。 et.al.|[2312.05684](http://arxiv.org/abs/2312.05684)|null|
|**2023-12-08**|**Multi-view Inversion for 3D-aware Generative Adversarial Networks**|当前用于人类头部的3D GAN反演方法通常仅使用一个单个正面图像来重建整个3D头部模型。当多视图数据或动态视频可用时，这会遗漏有意义的信息。我们的方法建立在现有最先进的3D GAN反演技术的基础上，以实现同一主题的多个视图的一致和同时反演。我们使用多潜在扩展来处理动态人脸视频中存在的不一致性，以从序列中重新合成一致的3D表示。由于我们的方法使用了有关目标对象的额外信息，我们观察到几何精度和图像质量都有显著提高，尤其是在从宽视角进行渲染时。此外，我们展示了我们的反向3D渲染的可编辑性，这将它们与基于NeRF的场景重建区分开来。 et.al.|[2312.05330](http://arxiv.org/abs/2312.05330)|null|
|**2023-12-11**|**Nuvo: Neural UV Mapping for Unruly 3D Representations**|现有的UV映射算法被设计为在性能良好的网格上操作，而不是由最先进的3D重建和生成技术产生的几何表示。因此，将这些方法应用于由神经辐射场和相关技术（或从这些场三角化的网格）恢复的体积密度会导致纹理图谱过于分散，无法用于视图合成或外观编辑等任务。我们提出了一种UV映射方法，旨在对通过3D重建和生成技术产生的几何体进行操作。我们的方法Nuvo不是计算在网格顶点上定义的映射，而是使用神经场来表示连续的UV映射，并将其优化为仅针对一组可见点（即仅影响场景外观的点）的有效且性能良好的映射。我们展示了我们的模型对不良几何体带来的挑战是稳健的，并且它生成了可以表示详细外观的可编辑UV映射。 et.al.|[2312.05283](http://arxiv.org/abs/2312.05283)|null|
|**2023-12-08**|**Fine Dense Alignment of Image Bursts through Camera Pose and Depth Estimation**|本文介绍了一种新的方法来对手持相机拍摄的突发图像进行精细对准。与估计帧对之间的二维变换或依赖于离散对应关系的传统技术相比，所提出的算法通过优化每个像素的相机运动和表面深度和方向来建立密集的对应关系。这种方法改进了对齐，特别是在具有视差挑战的场景中。以小基线甚至微小基线为特征的合成爆发的广泛实验表明，在这种情况下，它的性能优于目前可用的最佳光流方法，而不需要任何训练。除了增强对齐之外，我们的方法还为简单图像恢复之外的任务开辟了途径，如深度估计和3D重建，这得到了有希望的初步结果的支持。这将我们的方法定位为用于各种突发图像处理应用的通用工具。 et.al.|[2312.05190](http://arxiv.org/abs/2312.05190)|null|
|**2023-12-08**|**SuperNormal: Neural Surface Reconstruction via Multi-View Normal Integration**|我们介绍了SuperNormal，这是一种使用曲面法线贴图进行多视图三维重建的快速高保真方法。只需几分钟，SuperNormal就可以生成与3D扫描仪不相上下的详细曲面。我们利用体绘制来优化由多分辨率哈希编码提供支持的神经符号距离函数（SDF）。为了加速训练，我们提出了方向有限差分和基于补丁的射线行进来数值逼近SDF梯度。在不影响重建质量的同时，该策略的效率几乎是分析梯度的两倍，比轴对齐有限差分快约三倍。在基准数据集上的实验表明，与现有的多视图光度立体方法相比，SuperNormal在效率和准确性方面具有优势。在我们捕获的对象上，SuperNormal比最近的神经3D重建方法产生了更细粒度的几何体。 et.al.|[2312.04803](http://arxiv.org/abs/2312.04803)|null|
|**2023-12-07**|**FitDiff: Robust monocular 3D facial shape and reflectance estimation using Diffusion Models**|三维人脸重建的显著进展已经产生了高细节和逼真的人脸表示。最近，扩散模型实现了比GANs更好的性能，从而彻底改变了生成方法的能力。在这项工作中，我们提出了FitDiff，一个基于扩散的三维人脸化身生成模型。该模型利用从“野外”2D面部图像中提取的身份嵌入，准确地生成可重新点亮的面部化身。我们的多模式漫射模型同时输出面部反射率图（漫射和镜面反照率和法线）和形状，显示出强大的泛化能力。它只在公共面部数据集的注释子集上进行训练，并与3D重建相结合。我们通过使用感知和人脸识别损失来引导反向扩散过程，重新审视典型的3D人脸拟合方法。FitDiff是第一个以人脸识别嵌入为条件的LDM，它重建了可重新照明的人类化身，可以像在普通渲染引擎中一样使用，只从不受约束的面部图像开始，并实现了最先进的性能。 et.al.|[2312.04465](http://arxiv.org/abs/2312.04465)|null|

<p align=right>(<a href=#updated-on-20231214>back to top</a>)</p>

## Diffusion

|Publish Date|Title|Abstract|PDF|Code|
|---|---|---|---|---|
|**2023-12-12**|**FreeInit: Bridging Initialization Gap in Video Diffusion Models**|尽管基于扩散的视频生成取得了快速进展，但现有模型的推理结果仍然表现出不令人满意的时间一致性和不自然的动态性。在本文中，我们深入研究了视频扩散模型的噪声初始化，并发现了一个隐含的训练推理缺口，该缺口归因于不令人满意的推理质量。我们的主要发现是：1）推断时初始潜在值的时空频率分布与训练时的频率分布有本质的不同，2）去噪过程受到初始噪声低频分量的显著影响。受这些观察结果的启发，我们提出了一种简洁而有效的推理采样策略FreeInit，它显著提高了扩散模型生成的视频的时间一致性。FreeInit通过在推理过程中迭代细化初始潜伏的时空低频分量，能够补偿训练和推理之间的初始化间隙，从而有效提高生成结果的主体外观和时间一致性。大量实验表明，FreeInit在没有额外训练的情况下持续增强了各种文本到视频生成模型的生成结果。 et.al.|[2312.07537](http://arxiv.org/abs/2312.07537)|**[link](https://github.com/tianxingwu/freeinit)**|
|**2023-12-12**|**FreeControl: Training-Free Spatial Control of Any Text-to-Image Diffusion Model with Any Condition**|最近的方法，如ControlNet，为用户提供了对文本到图像（T2I）扩散模型的细粒度空间控制。然而，辅助模块必须针对每种类型的空间条件、模型架构和检查点进行训练，这与人类设计师在内容创建过程中希望传达给人工智能模型的不同意图和偏好不一致。在这项工作中，我们提出了FreeControl，这是一种用于可控T2I生成的无训练方法，同时支持多个条件、架构和检查点。FreeControl设计了结构引导以便于结构与引导图像对齐，并设计了外观引导以实现使用相同种子生成的图像之间的外观共享。大量的定性和定量实验证明了FreeControl在各种预先训练的T2I模型中的卓越性能。特别是，FreeControl便于对许多不同的体系结构和检查点进行方便的无训练控制，允许大多数现有的无训练方法失败的具有挑战性的输入条件，并通过基于训练的方法实现有竞争力的综合质量。 et.al.|[2312.07536](http://arxiv.org/abs/2312.07536)|null|
|**2023-12-12**|**Cosmological Field Emulation and Parameter Inference with Diffusion Models**|宇宙学模拟在阐明物理参数对场的统计和给定密度场信息的约束参数的影响方面发挥着至关重要的作用。我们利用扩散生成模型来解决宇宙学的两个重要任务——作为以输入宇宙学参数 $\Omega_m$和$\sigma_8$ 为条件的冷暗物质密度场的模拟器，以及作为可以返回对输入场的宇宙学参数的约束的参数推断模型。我们表明，该模型能够生成功率谱与模拟目标分布一致的场，并捕捉到每个参数对功率谱调制的微妙影响。我们还探索了它们作为参数推断模型的效用，发现我们可以获得宇宙学参数的严格约束。 et.al.|[2312.07534](http://arxiv.org/abs/2312.07534)|null|
|**2023-12-12**|**PEEKABOO: Interactive Video Generation via Masked-Diffusion**|最近，在文本到视频的生成方面取得了很大进展，最先进的模型能够生成高质量、逼真的视频。然而，这些模型缺乏用户交互控制和生成视频的能力，这可能会解锁新的应用领域。作为实现这一目标的第一步，我们解决了赋予基于扩散的视频生成模型对其输出的交互式时空控制的问题。为此，我们从分割文献的最新进展中获得灵感，提出了一种新颖的时空掩蔽注意力模块——Peekaboo。该模块是对现成的视频生成模型的无训练、无推理开销的补充，能够实现时空控制。我们还提出了交互式视频生成任务的评估基准。通过广泛的定性和定量评估，我们确定Peekaboo能够生成控制视频，甚至在mIoU上获得了比基线模型高达3.8倍的增益。 et.al.|[2312.07509](http://arxiv.org/abs/2312.07509)|null|
|**2023-12-12**|**MinD-3D: Reconstruct High-quality 3D objects in Human Brain**|在本文中，我们介绍了Recon3DMind，这是一项开创性的任务，专注于从功能磁共振成像（fMRI）信号重建3D视觉效果。这代表着认知神经科学和计算机视觉向前迈出了重要一步。为了支持这项任务，我们提出了fMRI形状数据集，利用3D对象的360度视图视频进行全面的fMRI信号捕获。该数据集包含55类日常生活中的常见物体，将支持未来的研究工作。我们还提出了MinD-3D，这是一种新颖有效的三阶段框架，可以从fMRI信号中解码和重建大脑的3D视觉信息。该方法首先使用神经融合编码器从fMRI帧中提取和聚集特征，然后使用特征桥扩散模型来生成相应的视觉特征，并最终通过生成变换器解码器来恢复3D对象。我们的实验表明，该方法有效地提取了fMRI信号中有效且与感兴趣视觉区域（ROI）高度相关的特征。值得注意的是，它不仅重建了具有高语义相关性和空间相似性的3D对象，而且显著加深了我们对人脑3D视觉处理能力的理解。项目页面位于：https://jianxgao.github.io/mind-3d. et.al.|[2312.07485](http://arxiv.org/abs/2312.07485)|null|
|**2023-12-12**|**Turning Earth into Venus: A Stochastic Model of Possible Evolutions of Terrestrial Topography**|金星可能在其历史的很长一段时间内既有类似地球的气候，也有广阔的海洋和活跃的（或早期的）板块构造。金星的地形功率谱为金星过去的演化提供了重要线索。通过与地球的强低阶奇数- $l$主导的全球地形进行详细对比，我们证明了相对平坦的金星地形可以被解释为是由活跃的类地板块构造到当前停滞的盖构造的转变引起的，此时$\tau=544^｛+886｝_｛-193｝$是在现在之前的百万年。如果海洋的消失和随之而来的向以CO$_2$为主的大气的转变伴随着大陆规模的快速侵蚀，然后熔岩以1公里$^{3}$yr$^{-1}$的流出率逐渐重新浮出水面，这种情况是合理的。我们用一个类似全球扩散的模型来研究金星提出的地形松弛，该模型采用了陆地侵蚀率，并对降雨量和温度的增加进行了调整，这将伴随着全球范围内从类似地球的气候向失控的温室气候的转变，最终可能产生今天的金星，如果全球侵蚀与地球上典型的基岩河流流域一样有效，估计为5.1 ^{+1.8}_{-1.1}$ Myr。 et.al.|[2312.07483](http://arxiv.org/abs/2312.07483)|null|
|**2023-12-12**|**Origin of correlated diffuse scattering in the hexagonal manganites**|我们结合第一性原理密度函数计算和自旋动力学模拟，解释了六方多铁性钇锰酸盐YMnO $_3$中不寻常的扩散非弹性中子散射。利用对称性考虑，我们用密度函数计算得出的参数构建了一个模型自旋哈密顿量，并表明它捕捉了测量的行为。然后，我们证明了在动量空间中观察到的结构漫散射的方向性是三角形几何的标志，并且它在N’eel温度T$_\text{N}$以上和以下的宽温度范围内的持续性是强磁挫折的结果。我们预测，这种漫散射存在于一个尚未观察到的调制能量连续体中，其相关的自旋激发具有不同的平面内和平面外特性，并且挫败感影响N’eel温度以下的磁性。最后，我们表明，用复合三聚体磁电单极子和超环面矩而不是单个自旋来可视化磁序，可以深入了解真实的空间波动，揭示顺磁状态下出现的有序团簇，以及有序反铁磁相中的集体短程激发。我们对在T$_\text｛N｝$ 以下和以上的如此宽的温度范围内的这种定向扩散散射的理解，为了解受抑系统中的磁相变提供了新的见解。 et.al.|[2312.07449](http://arxiv.org/abs/2312.07449)|null|
|**2023-12-12**|**DiffMorpher: Unleashing the Capability of Diffusion Models for Image Morphing**|扩散模型已经实现了显著的图像生成质量，超过了以前的生成模型。然而，与GANs相比，扩散模型的一个显著限制是，由于其高度非结构化的潜在空间，它们很难在两个图像样本之间平滑插值。这种平滑插值很有趣，因为它自然地可以作为许多应用程序的图像变形任务的解决方案。在这项工作中，我们提出了DiffMorpher，这是第一种使用扩散模型实现平滑和自然图像插值的方法。我们的关键思想是通过将两个LoRA分别拟合到两个图像来捕获它们的语义，并在LoRA参数和潜在噪声之间进行插值，以确保平滑的语义转换，其中对应关系自动出现，而无需注释。此外，我们提出了一种注意力插值和注入技术以及一种新的采样时间表，以进一步增强连续图像之间的平滑度。大量实验表明，DiffMorpher在各种对象类别中实现了比以前的方法更好的图像变形效果，弥合了区分扩散模型和GANs的关键功能差距。 et.al.|[2312.07409](http://arxiv.org/abs/2312.07409)|null|
|**2023-12-12**|**Boosting Latent Diffusion with Flow Matching**|最近，在视觉合成和潜在的生成模型方面取得了巨大的进展。在这里，扩散模型（DM）特别突出，但最近，流匹配（FM）也引起了人们的极大兴趣。尽管DM擅长提供多样化的图像，但它们的训练时间长，生成速度慢。随着潜在的扩散，这些问题只得到部分缓解。相反，FM提供了更快的训练和推理，但在合成中表现出较少的多样性。我们证明，在扩散模型和卷积解码器之间引入FM可以提供高分辨率的图像合成，同时降低了计算成本和模型大小。扩散可以有效地提供必要的世代多样性。FM补偿了较低的分辨率，将小的潜在空间映射到高维空间。随后，LDM的卷积解码器将这些延迟映射到高分辨率图像。通过结合DM的多样性、FM的效率和卷积解码器的有效性，我们以最小的计算成本以1024^2$的价格实现了最先进的高分辨率图像合成。重要的是，我们的方法与底层DM的最新近似和加速策略正交，使其易于集成到各种DM框架中。 et.al.|[2312.07360](http://arxiv.org/abs/2312.07360)|**[link](https://github.com/compvis/fm-boosting)**|
|**2023-12-12**|**Momentum Particle Maximum Likelihood**|潜变量模型的最大似然估计（MLE）通常被重新定义为参数和概率分布的扩展空间上的优化问题。例如，期望最大化（EM）算法可以被解释为应用于该空间上的适当自由能函数的坐标下降。最近，这一观点与最优输运和Wasserstein梯度流的见解相结合，开发了适用于比标准EM更广泛的模型类别的基于粒子的算法。从先前将“动量富集”优化算法解释为常微分方程离散化的工作中汲取灵感，我们提出了一种类似的动力学系统启发的方法来最小化参数和概率分布的扩展空间上的自由能泛函。结果是一个混合了Nesterov加速梯度法、欠阻尼Langevin扩散法和粒子法元素的动态系统。在适当的假设下，我们建立了所提出的系统在连续时间内与函数的唯一极小值的定量收敛性。然后，我们提出了该系统的数值离散化，使其能够应用于潜变量模型中的参数估计。通过数值实验，我们证明了所得到的算法比现有方法收敛得更快，并且与其他（近似）MLE算法相比是有利的。 et.al.|[2312.07335](http://arxiv.org/abs/2312.07335)|null|

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

