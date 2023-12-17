[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]

## Updated on 2023.12.17
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
|**2023-12-14**|**ColNeRF: Collaboration for Generalizable Sparse Input Neural Radiance Field**|神经辐射场（NeRF）在从密集输入合成新视图方面表现出了令人印象深刻的潜力，然而，在处理稀疏输入时，其有效性受到了挑战。现有的方法结合了额外的深度或语义监督，可以在一定程度上缓解这一问题。然而，监督收集的过程不仅成本高昂，而且可能不准确，导致在不同场景下的表现和泛化能力较差。在我们的工作中，我们介绍了一种新的模型：协作神经辐射场（ColNeRF），设计用于处理稀疏输入。ColNeRF中的协作包括稀疏输入图像之间的协作和神经辐射场的输出之间的协作。通过这一点，我们构建了一个新的协作模块，该模块将来自不同视图的信息对齐，同时施加自监督约束，以确保多视图在几何和外观上的一致性。提出了一种协作跨视图体积集成模块（CCVI）来捕捉复杂的遮挡并隐含地推断对象的空间位置。此外，我们引入了对多个方向上投影的目标射线的自监督，以确保相邻区域的几何和颜色一致性。得益于输入端和输出端的协作，ColNeRF能够捕捉更丰富、更通用的场景表示，从而促进新视图合成的更高质量结果。大量实验表明，ColNeRF优于最先进的稀疏输入可推广NeRF方法。此外，与基于场景优化的NeRF方法相比，我们的方法在微调以适应新场景方面表现出优势，实现了有竞争力的性能，同时显著降低了计算成本。我们的代码位于：https://github.com/eezkni/colnerf. et.al.|[2312.09095](http://arxiv.org/abs/2312.09095)|**[link](https://github.com/eezkni/colnerf)**|
|**2023-12-14**|**ProSGNeRF: Progressive Dynamic Neural Scene Graph with Frequency Modulated Auto-Encoder in Urban Scenes**|隐式神经表示在大型复杂场景的视图合成中已经显示出有希望的结果。然而，现有的方法要么无法捕捉快速移动的对象，要么需要在没有相机自我运动的情况下构建场景图，导致场景的合成视图质量低。我们旨在共同解决大规模城市场景和快速移动车辆的视图合成问题，这更具实用性和挑战性。为此，我们首先利用图结构来学习动态对象和背景的局部场景表示。然后，我们设计了一个渐进方案，该方案动态地分配用时间窗口内的帧训练的新的局部场景图，允许我们将表示放大到任意大的场景。此外，城市场景的训练视图相对稀疏，这导致动态对象的重建精度显著下降。因此，我们设计了一个频率自动编码器网络来对潜在代码进行编码，并正则化对象的频率范围，这可以增强动态对象的表示，解决图像输入稀疏的问题。此外，我们使用激光雷达点投影来保持大规模城市场景中的几何一致性。实验结果表明，我们的方法实现了最先进的视图合成精度、对象操纵和场景漫游能力。该代码将在论文验收后开源。 et.al.|[2312.09076](http://arxiv.org/abs/2312.09076)|null|
|**2023-12-14**|**Scene 3-D Reconstruction System in Scattering Medium**|随着新模型和扩展的发展，用于新视图合成的神经辐射场研究经历了爆炸式增长。适用于水下场景或散射介质的NERF算法也在不断发展。现有的水下三维重建系统仍然面临训练时间长、渲染效率低等挑战。本文提出了一种改进的水下三维重建系统来解决这些问题，并实现快速、高质量的三维重建。首先，我们增强了单眼相机拍摄的水下视频，以纠正水介质物理特性造成的图像质量差的问题，同时确保相邻帧增强的一致性。随后，我们对视频帧进行关键帧选择，以优化资源利用率，消除动态对象对重建结果的影响。所选关键帧在使用COLMAP进行姿态估计后，使用基于多分辨率哈希编码的神经辐射场进行三维重建改进过程，用于模型构建和渲染。 et.al.|[2312.09005](http://arxiv.org/abs/2312.09005)|null|
|**2023-12-14**|**VaLID: Variable-Length Input Diffusion for Novel View Synthesis**|新视图合成（NVS）是3D视觉中的一个基本问题，它试图在给定源视图图像及其相应姿态的情况下，在目标视图上生成逼真的图像。由于这项任务严重受限，最近的一些工作，如Zero123，试图通过生成建模来解决这个问题，特别是使用预先训练的扩散模型。尽管这种策略很好地适用于新场景，但与基于神经辐射场的方法相比，它提供的灵活性很低。例如，尽管现实应用程序通常提供多个输入图像，但它只能接受单个视图图像作为输入。这是因为源视图图像和相应的姿势是单独处理的，并在不同阶段注入到模型中。因此，一旦模型可用，将其推广到多视图源图像中并非易事。为了解决这个问题，我们试图分别处理每个姿势图像对，然后将它们融合为统一的视觉表示，将其注入模型中，以指导目标视图的图像合成。然而，不一致性和计算成本随着输入源视图图像的数量的增加而增加。为了解决这些问题，提出了多视图交叉形成器模块，该模块将可变长度的输入数据映射到固定大小的输出数据。为了进一步提高训练时间的效率，引入了两阶段训练策略。在多个数据集上进行的定性和定量评估证明了所提出的方法相对于以前的方法的有效性。代码将根据验收结果发布。 et.al.|[2312.08892](http://arxiv.org/abs/2312.08892)|null|
|**2023-12-14**|**CF-NeRF: Camera Parameter Free Neural Radiance Fields with Incremental Learning**|神经辐射场（NeRF）在新的视图合成中表现出了令人印象深刻的性能。然而，NeRF及其大多数变体仍然依赖于传统的复杂管道来提供外在和内在的相机参数，如COLMAP。最近的工作，如NeRFmm、BARF和L2G NeRF，直接将相机参数视为可学习的，并通过差分体绘制进行估计。然而，这些方法适用于具有轻微运动的前瞻性场景，在实践中无法解决旋转场景。为了克服这一限制，我们提出了一种新颖的下划线{c}amera参数\下划线{f}ree神经辐射场（CF NeRF），其增量重建3D表示并从运动中恢复受增量结构启发的相机参数（SfM）。给定一系列图像，CF-NeRF逐个估计图像的相机参数，并通过初始化、隐式定位和隐式优化重建场景。为了评估我们的方法，我们使用了一个具有挑战性的真实世界数据集NeRFBuster，该数据集提供了复杂轨迹下的12个场景。结果表明，CF-NeRF对相机旋转具有鲁棒性，并且在不提供先验信息和约束的情况下实现了最先进的结果。 et.al.|[2312.08760](http://arxiv.org/abs/2312.08760)|null|
|**2023-12-13**|**NViST: In the Wild New View Synthesis from a Single Image with Transformers**|我们提出了NViST，这是一种基于变换器的模型，用于从单个图像进行新的视图合成，在具有复杂背景的野外图像的大规模数据集上进行训练。NViST采用可扩展的基于变压器的架构，将图像输入直接转换为辐射场。在实践中，NViST利用屏蔽自动编码器（MAE）学习的自监督特征，并学习一种新的解码器，该解码器通过交叉注意力和自适应层规范化将特征转换为3D标记。我们的模型在推理方面是有效的，因为与需要测试时间优化或采样的方法（如3D感知扩散模型）不同，预测3D表示只需要一次前向传递。我们进一步解决了当前新的视图合成模型的局限性。首先，与大多数以特定类别的方式训练的生成模型不同，通常在合成数据集或屏蔽输入上训练，我们的模型是在MVImgNet上训练的，这是一个真实世界的大规模数据集，包含数百个不同背景的对象类别。其次，我们的模型不需要训练数据的规范化，即将所有对象与正面视图对齐，只需要在训练时使用相对姿势，这消除了在随意捕获的数据集上使用相对姿势的巨大障碍。我们在MVImgNet上显示看不见的对象和类别的结果，甚至是随意的手机捕获。我们对MVImgNet和ShapeNet进行了定性和定量评估，以表明我们的模型朝着从单个图像实现真实的小说视角合成迈出了一步。 et.al.|[2312.08568](http://arxiv.org/abs/2312.08568)|null|
|**2023-12-13**|**FoundationPose: Unified 6D Pose Estimation and Tracking of Novel Objects**|我们介绍了FoundationPose，这是一个用于6D物体姿态估计和跟踪的统一基础模型，支持基于模型和无模型的设置。我们的方法可以在测试时立即应用于新物体，而无需微调，只要给出其CAD模型，或者捕获少量参考图像。我们用神经隐式表示弥合了这两种设置之间的差距，该表示允许有效的新视图合成，在相同的统一框架下保持下游姿态估计模块不变。在大型语言模型（LLM）、一种新颖的基于转换器的架构和对比学习公式的帮助下，通过大规模的合成训练实现了强大的可推广性。对涉及挑战性场景和对象的多个公共数据集的广泛评估表明，我们的统一方法在很大程度上优于专门用于每项任务的现有方法。此外，尽管减少了假设，但它甚至实现了与实例级方法相当的结果。项目页面：https://nvlabs.github.io/foundationpose/ et.al.|[2312.08344](http://arxiv.org/abs/2312.08344)|null|
|**2023-12-13**|**Global Latent Neural Rendering**|在可推广的新视图合成方法中，最近的一个趋势是学习对单个相机射线起作用的渲染算子。这种方法很有前途，因为它消除了对显式体积渲染的需求，但它有效地将目标图像视为独立像素的集合。在这里，我们建议学习一个全局渲染操作符，该操作符联合作用于所有摄影机光线。我们展示了实现这种渲染的正确表示是5维平面扫描体积，该体积由输入图像在面向目标相机的一组平面上的投影组成。基于这一理解，我们介绍了我们的卷积全局潜在渲染器（ConvGLR），这是一种高效的卷积架构，可在低分辨率潜在空间中全局执行渲染操作。在稀疏和可推广设置下的各种数据集上的实验表明，我们的方法始终显著优于现有方法。 et.al.|[2312.08338](http://arxiv.org/abs/2312.08338)|null|
|**2023-12-13**|**Neural Radiance Fields for Transparent Object Using Visual Hull**|与不透明物体不同，透明物体的新颖视图合成是一项具有挑战性的任务，因为透明物体折射背景光，导致透明物体表面沿着视点变化产生视觉失真。最近引入的神经辐射场（NeRF）是一种视图合成方法。由于其显著的性能改进，基于NeRF的以下应用在各个主题中都得到了开发。然而，如果具有不同折射率的对象被包括在诸如透明对象之类的场景中，则NeRF表现出有限的性能，因为没有适当地考虑透明对象表面处的折射光线。为了解决这个问题，我们提出了一种基于NeRF的方法，该方法由以下三个步骤组成：首先，我们使用视觉外壳重建透明物体的三维形状。其次，我们根据Snell定律模拟了透明物体内部光线的折射。最后，我们通过折射光线对点进行采样，并将它们放入NeRF中。实验评估结果表明，我们的方法解决了传统NeRF对透明物体的限制。 et.al.|[2312.08118](http://arxiv.org/abs/2312.08118)|null|
|**2023-12-13**|**Novel View Synthesis with View-Dependent Effects from a Single Image**|在本文中，我们首先将视图相关效应考虑到基于单图像的新视图合成（NVS）问题中。为此，我们建议利用NVS中的相机运动先验来将依赖于视图的外观或效果（VDE）建模为场景中的负视差。通过识别“跟随”相机运动的镜面反射性，我们通过沿着核线的负深度区域聚集输入像素颜色，将VDE注入输入图像。此外，我们提出了一种“松弛体积渲染”近似方法，该方法允许在单次通过中计算密度，从而提高单图像NVS的效率。我们的方法只能从图像序列中学习单个图像的NVS，这是一种完全自监督的学习方法，首次不需要深度和相机姿态标注。我们给出了大量的实验结果，并表明我们提出的方法可以用VDE学习NVS，在RealEstate10k和MannequinChallenge数据集上优于SOTA单视图NVS方法。 et.al.|[2312.08071](http://arxiv.org/abs/2312.08071)|null|

<p align=right>(<a href=#updated-on-20231217>back to top</a>)</p>

## 3D Reconstruction

|Publish Date|Title|Abstract|PDF|Code|
|---|---|---|---|---|
|**2023-12-14**|**Triplane Meets Gaussian Splatting: Fast and Generalizable Single-View 3D Reconstruction with Transformers**|生成模型的发展推动了从单个图像进行3D重建的最新进展。其中最突出的是基于分数蒸馏采样（SDS）的方法和3D域中扩散模型的自适应。尽管这些技术取得了进展，但由于优化或渲染过程缓慢，导致训练和优化时间过长，这些技术往往面临限制。在本文中，我们介绍了一种新的单视图重建方法，该方法通过前馈推理从单个图像有效地生成3D模型。我们的方法利用两个基于变换器的网络，即点解码器和三平面解码器，使用混合三平面高斯中间表示来重建3D对象。这种混合表示实现了平衡，与隐式表示相比，实现了更快的渲染速度，同时提供了比显式表示更高的渲染质量。点解码器被设计用于从单个图像生成点云，提供显式表示，然后由三平面解码器使用该显式表示来查询每个点的高斯特征。这种设计选择解决了与直接回归以其非结构性质为特征的显式三维高斯属性相关的挑战。随后，通过MLP对3D高斯进行解码，以实现通过飞溅的快速渲染。这两个解码器都建立在可扩展的、基于转换器的架构上，并在大规模3D数据集上进行了有效的训练。对合成数据集和真实世界图像进行的评估表明，与以前最先进的技术相比，我们的方法不仅实现了更高的质量，而且确保了更快的运行时间。请参阅我们的项目页面https://zouzx.github.io/triplanegaussian/. et.al.|[2312.09147](http://arxiv.org/abs/2312.09147)|null|
|**2023-12-14**|**Living Scenes: Multi-object Relocalization and Reconstruction in Changing 3D Environments**|对动态3D场景理解的研究主要集中在密集观测的短期变化跟踪上，而很少关注稀疏观测的长期变化。我们用MoRE解决了这一差距，MoRE是一种在进化环境中进行多对象重新定位和重建的新方法。我们将这些环境视为“真实场景”，并考虑将在不同时间点进行的扫描转换为对象实例的3D重建的问题，其准确性和完整性会随着时间的推移而提高。我们方法的核心是在合成数据上训练的单个编码器-解码器网络中的SE（3）-等变表示。这种表示使我们能够无缝地处理实例匹配、注册和重建。我们还引入了一种联合优化算法，该算法有助于在不同时间点进行的多次扫描中积累源自同一实例的点云。我们在合成和真实世界的数据上验证了我们的方法，并在端到端性能和单个子任务中展示了最先进的性能。 et.al.|[2312.09138](http://arxiv.org/abs/2312.09138)|null|
|**2023-12-14**|**Learned Fusion: 3D Object Detection using Calibration-Free Transformer Feature Fusion**|使用传感器融合的3D对象检测的现有技术在很大程度上依赖于校准质量，这在实验室环境之外的大规模部署中很难维持。我们提出了第一种用于三维物体检测的无校准方法。因此，消除了对复杂且昂贵的校准程序的需要。我们的方法使用转换器在多个抽象级别上映射不同传感器的多个视图之间的特征。在对物体检测的广泛评估中，我们不仅表明我们的方法在BEV mAP中比单模态设置好14.1%，而且转换器确实学习了映射。通过表明传感器融合不需要校准，我们希望激励其他研究人员遵循无校准融合的方向。此外，由此产生的方法对旋转和平移变化具有相当大的弹性。 et.al.|[2312.09082](http://arxiv.org/abs/2312.09082)|null|
|**2023-12-14**|**Scene 3-D Reconstruction System in Scattering Medium**|随着新模型和扩展的发展，用于新视图合成的神经辐射场研究经历了爆炸式增长。适用于水下场景或散射介质的NERF算法也在不断发展。现有的水下三维重建系统仍然面临训练时间长、渲染效率低等挑战。本文提出了一种改进的水下三维重建系统来解决这些问题，并实现快速、高质量的三维重建。首先，我们增强了单眼相机拍摄的水下视频，以纠正水介质物理特性造成的图像质量差的问题，同时确保相邻帧增强的一致性。随后，我们对视频帧进行关键帧选择，以优化资源利用率，消除动态对象对重建结果的影响。所选关键帧在使用COLMAP进行姿态估计后，使用基于多分辨率哈希编码的神经辐射场进行三维重建改进过程，用于模型构建和渲染。 et.al.|[2312.09005](http://arxiv.org/abs/2312.09005)|null|
|**2023-12-13**|**ProNeRF: Learning Efficient Projection-Aware Ray Sampling for Fine-Grained Implicit Neural Radiance Fields**|神经渲染的最新进展表明，尽管速度较慢，但隐式紧凑模型可以从多个视图中学习场景的几何图形和视图相关外观。为了保持如此小的内存占用，但实现更快的推理时间，最近的工作采用了“采样器”网络，该网络自适应地对隐式神经辐射场中沿每条射线的一小部分点进行采样。尽管这些方法在渲染时间上减少了10美元\倍，但与香草NeRF相比，它们的质量仍有相当大的下降。相反，我们提出了ProNeRF，它在内存占用（类似于NeRF）、速度（比HyperReel快）和质量（比K-Planes好）之间提供了最佳折衷。ProNeRF配备了一种新的投影感知采样（PAS）网络，以及一种用于射线探测和利用的新训练策略，从而实现高效的细粒度粒子采样。我们的ProNeRF产生了最先进的指标，比NeRF快15-23倍，PSNR比NeRF高0.65dB，比已发表的最佳基于采样器的方法HyperReel高0.95dB。我们的探索和开发训练策略使ProNeRF能够学习完整场景的颜色和密度分布，同时学习聚焦于最高密度区域的高效光线采样。我们提供了广泛的实验结果，分别在广泛采用的前向和360数据集LLFF和Blender上支持我们的方法的有效性。 et.al.|[2312.08136](http://arxiv.org/abs/2312.08136)|null|
|**2023-12-13**|**Denoising diffusion-based synthetic generation of three-dimensional (3D) anisotropic microstructures from two-dimensional (2D) micrographs**|集成计算材料工程（ICME）显著增强了对微观结构与材料性能之间关系的系统分析，为高性能材料的发展铺平了道路。然而，由于缺乏三维（3D）微观结构数据集，分析微观结构敏感材料的行为仍然具有挑战性。此外，如果微观结构是各向异性的，这一挑战会被放大，因为这也会导致材料的各向异性。在本文中，我们提出了一种仅基于二维（2D）显微照片使用基于条件扩散的生成模型（DGM）重建各向异性微观结构的框架。所提出的框架涉及多个2D条件DGM的空间连接，每个条件DGM都经过训练以生成三个不同正交平面的2D微观结构样本。连接的多个反向扩散过程使得能够对马尔可夫链进行有效建模，以将噪声转换为3D微观结构样本。此外，采用改进的协调采样来提高样本质量，同时在3D空间中保持各向异性微观结构样本切片之间的空间连接。为了验证所提出的框架，根据空间相关函数和物理材料行为对二维到三维重建的各向异性微观结构样品进行了评估。结果表明，该框架不仅能够再现材料相的统计分布，而且能够再现三维空间中的材料性质。这突出了所提出的二维到三维重建框架在建立微观结构-性能联系方面的潜在应用，这可能有助于未来研究的高通量材料设计 et.al.|[2312.07832](http://arxiv.org/abs/2312.07832)|null|
|**2023-12-12**|**Adaptive Confidence Multi-View Hashing for Multimedia Retrieval**|多视图哈希方法将多个视图中的异构数据转换为二进制哈希码，是多媒体检索的关键技术之一。然而，目前的方法主要探讨多个观点之间的互补性，而缺乏信心学习和融合。此外，在实际应用场景中，单视图数据包含冗余噪声。为了进行置信度学习并消除不必要的噪声，我们提出了一种新的自适应置信度多视图哈希（ACMVH）方法。首先，开发了置信网络来从各种单视图特征中提取有用信息并去除噪声信息。此外，采用自适应置信度多视图网络来测量每个视图的置信度，然后通过加权求和来融合多视图特征。最后，设计了一个扩展网络来进一步增强融合特征的特征表示。据我们所知，我们率先将置信学习应用于多媒体检索领域。在两个公共数据集上进行的大量实验表明，所提出的ACMVH比最先进的方法性能更好（最大增加了3.24%）。源代码可在https://github.com/hackerhyper/acmvh. et.al.|[2312.07327](http://arxiv.org/abs/2312.07327)|**[link](https://github.com/hackerhyper/acmvh)**|
|**2023-12-11**|**Gaussian Splatting SLAM**|我们首次将3D高斯散射应用于使用单个移动单目或RGB-D相机的增量3D重建。我们的同步定位和映射（SLAM）方法以3fps实时运行，使用高斯作为唯一的3D表示，统一了所需的表示，以实现准确、高效的跟踪、映射和高质量渲染。需要一些创新来从现场摄像机连续重建具有高保真度的3D场景。首先，为了超越最初的3DGS算法，该算法需要来自离线运动结构（SfM）系统的精确姿态，我们使用针对3D高斯的直接优化来制定3DGS的相机跟踪，并表明这能够实现快速而稳健的跟踪，并具有广泛的收敛范围。其次，通过利用高斯的显式性质，我们引入了几何验证和正则化来处理增量三维密集重建中出现的模糊性。最后，我们介绍了一个完整的SLAM系统，它不仅在新的视图合成和轨迹估计方面取得了最先进的结果，而且还重建了微小甚至透明的物体。 et.al.|[2312.06741](http://arxiv.org/abs/2312.06741)|null|
|**2023-12-10**|**UNeR3D: Versatile and Scalable 3D RGB Point Cloud Generation from 2D Images in Unsupervised Reconstruction**|在从2D图像进行3D重建的领域中，一个持续的挑战是在不依赖3D地面实况数据的情况下实现高精度重建。我们介绍了UNeR3D，这是一种开创性的无监督方法，为仅从2D视图生成详细的3D重建设定了新标准。我们的模型显著降低了与监督方法相关的训练成本，并将RGB着色引入3D点云，丰富了视觉体验。UNeR3D采用反向距离加权技术进行颜色渲染，可确保无缝的颜色转换，增强视觉逼真度。我们的模型的灵活架构支持使用任何数量的视图进行训练，唯一的是，在执行重建时，它不受训练期间使用的视图数量的限制。它可以在推理过程中使用任意数量的视图进行推理，提供了无与伦比的多功能性。此外，该模型的连续空间输入域允许以任何所需分辨率生成点云，从而能够创建高分辨率的3D RGB点云。我们用一种新颖的多视图几何损失和颜色损失来巩固重建过程，证明我们的模型在单视图输入及其他方面都很出色，从而重塑了3D视觉中无监督学习的范式。我们的贡献标志着3D视觉的巨大飞跃，为各种应用程序的内容创作提供了新的视野。代码位于https://github.com/hongbinlin3589/uner3d. et.al.|[2312.06706](http://arxiv.org/abs/2312.06706)|null|
|**2023-12-11**|**Nuvo: Neural UV Mapping for Unruly 3D Representations**|现有的UV映射算法被设计为在性能良好的网格上操作，而不是由最先进的3D重建和生成技术产生的几何表示。因此，将这些方法应用于由神经辐射场和相关技术（或从这些场三角化的网格）恢复的体积密度会导致纹理图谱过于分散，无法用于视图合成或外观编辑等任务。我们提出了一种UV映射方法，旨在对通过3D重建和生成技术产生的几何体进行操作。我们的方法Nuvo不是计算在网格顶点上定义的映射，而是使用神经场来表示连续的UV映射，并将其优化为仅针对一组可见点（即仅影响场景外观的点）的有效且性能良好的映射。我们展示了我们的模型对不良几何体带来的挑战是稳健的，并且它生成了可以表示详细外观的可编辑UV映射。 et.al.|[2312.05283](http://arxiv.org/abs/2312.05283)|null|

<p align=right>(<a href=#updated-on-20231217>back to top</a>)</p>

## Diffusion

|Publish Date|Title|Abstract|PDF|Code|
|---|---|---|---|---|
|**2023-12-14**|**LIME: Localized Image Editing via Attention Regularization in Diffusion Models**|随着文本到图像生成的最新进展，扩散模型（DM）因其生成高质量、多样化图像的能力而备受关注。现在的研究重点正在转向DM的可控性。该领域的一个重大挑战是本地化编辑，即在不影响其余内容的情况下修改图像的特定区域。本文介绍了LIME，用于扩散模型中的本地化图像编辑，该模型不需要用户指定的兴趣区域（RoI）或额外的文本输入。我们的方法使用来自预训练方法的特征和简单的聚类技术来获得精确的语义分割图。然后，通过利用交叉注意力映射，它可以细化这些片段进行本地化编辑。最后，我们提出了一种新的交叉注意力正则化技术，该技术在去噪步骤中惩罚RoI中不相关的交叉注意力分数，确保本地化编辑。我们的方法在没有重新训练和微调的情况下，在各种编辑基准中不断提高现有方法的性能。 et.al.|[2312.09256](http://arxiv.org/abs/2312.09256)|null|
|**2023-12-14**|**FineControlNet: Fine-level Text Control for Image Generation with Spatially Aligned Text Control Injection**|最近引入的ControlNet能够利用几何输入（如人类2D姿势或边缘特征）来引导文本驱动的图像生成过程。虽然ControlNet提供了对生成图像中实例几何形状的控制，但它缺乏规定每个实例的视觉外观的能力。我们提出了FineControlNet，以提供对每个实例外观的精细控制，同时保持精确的姿势控制能力。具体来说，我们开发并演示了FineControlNet，它通过人体姿势图像进行几何控制，并通过实例级文本提示进行外观控制。实例特定文本提示和二维姿势在潜在空间中的空间对齐使FineControlNet具有精细控制功能。我们通过与最先进的姿势条件文本到图像扩散模型的严格比较来评估FineControlNet的性能。与现有方法相比，FineControlNet在生成遵循用户提供的特定于实例的文本提示和姿势的图像方面实现了卓越的性能。项目网页：https://samsunglabs.github.io/finecontrolnet-project-page et.al.|[2312.09252](http://arxiv.org/abs/2312.09252)|null|
|**2023-12-14**|**Single Mesh Diffusion Models with Field Latents for Texture Generation**|我们介绍了一种直接在3D形状表面上操作的内在潜在扩散模型的框架，目的是合成高质量的纹理。我们的方法有两个贡献：场潜伏，一种将纹理编码为网格顶点上的离散矢量场的潜伏表示，以及场潜伏扩散模型，它学习对表面上学习到的潜伏空间中的扩散过程进行去噪。我们考虑一个单一纹理的网格范式，其中我们的模型被训练来生成网格上给定纹理的变化。我们表明，与现有的单纹理网格生成模型相比，合成的纹理具有更高的保真度。我们的模型还可以适用于用户控制的编辑任务，如修复和标签引导生成。我们方法的有效性部分归因于我们提出的框架在等距下的等方差，使我们的模型能够在局部相似区域无缝地再现细节，并为生成纹理转移的概念打开了大门。 et.al.|[2312.09250](http://arxiv.org/abs/2312.09250)|null|
|**2023-12-14**|**Text2Immersion: Generative Immersive Scene with 3D Gaussians**|我们介绍了Text2Immersion，这是一种通过文本提示生成高质量3D沉浸式场景的优雅方法。我们提出的管道通过使用预先训练的2D扩散和深度估计模型逐步生成高斯云来启动。接下来是对高斯云的细化阶段，对其进行插值和细化以增强生成场景的细节。与关注单个对象或室内场景或使用缩小轨迹的流行方法不同，我们的方法生成具有各种对象的不同场景，甚至扩展到创建想象场景。因此，Text2Commercion可以对各种应用程序产生广泛的影响，如虚拟现实、游戏开发和自动内容创建。广泛的评估表明，我们的系统在渲染质量和多样性方面优于其他方法，进一步朝着文本驱动的3D场景生成方向发展。我们将在项目页面上公开源代码。 et.al.|[2312.09242](http://arxiv.org/abs/2312.09242)|null|
|**2023-12-14**|**A framework for conditional diffusion modelling with applications in motif scaffolding for protein design**|许多蛋白质设计应用，如粘合剂或酶设计，需要高精度的结构基序支架。基于去噪扩散过程的生成建模范式成为解决这一基序支架问题的主要候选者，并在某些情况下显示出早期的实验成功。在扩散范式中，基序支架被视为条件生成任务，并且从计算机视觉文献中提出或引入了几个条件生成协议。然而，这些协议中的大多数都是启发式的，例如通过与Langevin动力学的类比，并且缺乏统一的框架，模糊了不同方法之间的联系。在这项工作中，我们将条件训练和条件采样过程统一在一个基于数学上理解良好的Doob h变换的通用框架下。这种新的视角使我们能够在现有方法之间建立联系，并对现有的条件训练协议提出新的变体。我们说明了这种新协议在图像外绘和主题支架方面的有效性，并发现它优于标准方法。 et.al.|[2312.09236](http://arxiv.org/abs/2312.09236)|null|
|**2023-12-14**|**Slant, Fan, and Narrow: the Response of Stellar Streams to a Tilting Galactic Disk**|恒星流是引力势的敏感示踪剂，通常认为引力势在银河系内部是静态的。然而，像盖亚-索萨奇-恩克拉多斯这样的大规模合并会给银河系的星盘带来扭矩，导致星盘以高达10-20度/Gyr的速度倾斜。在这里，我们展示了圆盘倾斜对恒星流形态和运动学的影响。通过一系列数值实验，我们发现具有附近apocenter $（r_｛\rm-apo}\lesssim 20～\rm{kpc}）$ 的流对圆盘倾斜敏感，主要影响是流在天空轨道和宽度上的变化。有趣的是，根据祖恒星的轨道倾角和圆盘倾斜的方向，圆盘倾斜可以产生更多的扩散流和更窄的流。我们的Pal 5潮汐尾倾斜率为15°/Gyr的模型与观测到的水流轨迹和宽度非常一致，并再现了尾流的极度狭窄。我们还发现，未能解释倾斜圆盘的原因可能会使银河系局部暗物质分布的形状参数受到5-10%的约束，不同流的偏置方向也会发生变化。因此，星盘倾斜可以解释使用不同流推断出的银河系暗物质晕形状的差异。 et.al.|[2312.09233](http://arxiv.org/abs/2312.09233)|null|
|**2023-12-14**|**Reliability in Semantic Segmentation: Can We Use Synthetic Data?**|评估感知模型对协变位移和分布外（OOD）检测的可靠性对于自动驾驶汽车等安全关键应用至关重要。然而，由于任务的性质，相关数据很难收集和注释。在本文中，我们挑战了前沿的生成模型，以自动合成数据来评估语义分割的可靠性。通过微调稳定扩散，我们在OOD域或用OOD对象修复的情况下执行合成数据的零样本生成。合成数据用于对预训练的分割器进行初步评估，从而在面对真实边缘情况时深入了解其性能。通过大量实验，我们证明了在合成数据上的性能与在真实OOD数据上的表现之间的高度相关性，表明了该方法的有效性。此外，我们还说明了如何利用合成数据来增强分割器的校准和OOD检测能力。 et.al.|[2312.09231](http://arxiv.org/abs/2312.09231)|null|
|**2023-12-14**|**Mosaic-SDF for 3D Generative Models**|当前用于3D形状的基于扩散或流的生成模型分为两类：提取预先训练的2D图像扩散模型，以及直接在3D形状上进行训练。当在3D形状上训练扩散或流动模型时，关键的设计选择是形状表示。有效的形状表示需要遵循三个设计原则：它应该允许将大型3D数据集高效转换为表示形式；它应该提供近似功率与参数数量之间的良好折衷；并且它应该具有与现有强大的神经架构兼容的简单张量形式。虽然标准的三维形状表示（如体积网格和点云）并不同时遵守所有这些原则，但我们在本文中提倡一种新的表示方式。我们介绍了Mosaic SDF（M-SDF）：一种简单的三维形状表示，通过使用分布在形状边界附近的一组局部网格来近似给定形状的符号距离函数（SDF）。M-SDF表示对于每个形状单独计算是快速的，使其易于并行化；它是参数有效的，因为它只覆盖形状边界周围的空间；它具有简单的矩阵形式，与基于Transformer的架构兼容。我们通过使用M-SDF表示来训练3D生成流模型来证明其有效性，包括使用3D Warehouse数据集的类条件生成，以及使用约600k个字幕形状对的数据集的文本到3D生成。 et.al.|[2312.09222](http://arxiv.org/abs/2312.09222)|null|
|**2023-12-14**|**Measurement in the Age of LLMs: An Application to Ideological Scaling**|许多社会科学都以“意识形态”或“权力”等术语为中心，这些术语通常无法准确定义，其上下文含义被困在周围的语言中。本文探讨了使用大型语言模型（LLM）来灵活处理社会科学测量任务所固有的概念混乱。我们依靠LLM非凡的语言流利性来引出立法者和文本的意识形态尺度，这与既定的方法和我们自己的判断非常一致。我们方法的一个关键方面是，我们直接得出这样的分数，指示LLM自己提供数字分数。这种方法提供了很大的灵活性，我们通过各种不同的案例研究来展示这一点。我们的研究结果表明，LLM可以用来描述政治意识形态在文本中高度微妙和分散的表现。 et.al.|[2312.09203](http://arxiv.org/abs/2312.09203)|null|
|**2023-12-14**|**Fast Sampling via De-randomization for Discrete Diffusion Models**|扩散模型已成为高质量数据生成（如图像生成）的强大工具。尽管离散扩散模型在连续空间中取得了成功，但适用于文本和自然语言等领域的离散扩散模型仍然研究不足，而且生成速度往往很慢。在本文中，我们提出了一种新的去随机化扩散过程，它导致了离散扩散模型的加速算法。我们的技术显著减少了函数求值（即对神经网络的调用）的数量，使采样过程更快。此外，我们引入了一种连续时间（即无限步）采样算法，该算法可以提供比其离散时间（有限步）对应算法更好的采样质量。在自然语言生成和机器翻译任务上的大量实验表明，与现有的离散扩散模型方法相比，我们的方法在生成速度和样本质量方面都具有优越的性能。 et.al.|[2312.09193](http://arxiv.org/abs/2312.09193)|null|

<p align=right>(<a href=#updated-on-20231217>back to top</a>)</p>

## NeRF

|Publish Date|Title|Abstract|PDF|Code|
|---|---|---|---|---|
|**2023-12-14**|**ZeroRF: Fast Sparse View 360° Reconstruction with Zero Pretraining**|我们提出了ZeroRF，这是一种新的每场景优化方法，解决了神经场表示中稀疏视图360重建的挑战。目前的突破，如神经辐射场（NeRF）已经证明了高保真度的图像合成，但难以处理稀疏的输入视图。现有的方法，如可泛化的NeRF和每场景优化方法，在数据依赖性、计算成本和跨不同场景的泛化方面面临限制。为了克服这些挑战，我们提出了ZeroRF，其关键思想是将定制的深度图像先验集成到因子分解的NeRF表示中。与传统方法不同，ZeroRF使用神经网络生成器对特征网格进行参数化，从而实现高效的稀疏视图360重建，而无需任何预训练或额外的正则化。大量实验展示了ZeroRF在质量和速度方面的多功能性和优势，在基准数据集上取得了最先进的结果。ZeroRF的意义延伸到3D内容生成和编辑的应用。项目页面：https://sarahweiii.github.io/zerorf/ et.al.|[2312.09249](http://arxiv.org/abs/2312.09249)|null|
|**2023-12-12**|**SMERF: Streamable Memory Efficient Radiance Fields for Real-Time Large-Scene Exploration**|最近的实时视图合成技术在保真度和速度上迅速进步，现代方法能够以交互式帧速率渲染接近照片级真实感的场景。与此同时，在易于光栅化的显式场景表示和基于射线行进的神经场之间出现了紧张关系，后者的最先进实例在质量上超过了前者，同时对于实时应用来说成本高得令人望而却步。在这项工作中，我们介绍了SMERF，这是一种视图合成方法，在占地面积高达3亿 $^2$、体积分辨率为3.5毫米$^3$ 的大型场景中，它实现了实时方法中最先进的精度。我们的方法建立在两个主要贡献之上：一个是分层模型划分方案，它在限制计算和内存消耗的同时增加了模型容量，另一个是蒸馏训练策略，它同时产生高保真度和内部一致性。我们的方法能够在网络浏览器中实现全六自由度（6DOF）导航，并在商品智能手机和笔记本电脑上实时渲染。大量实验表明，我们的方法在实时新视图合成方面，在标准基准上超过了当前最先进的0.78 dB，在大型场景上超过了1.78 dB，渲染帧的速度比最先进的辐射场模型快三个数量级，并在包括智能手机在内的各种商品设备上实现了实时性能。我们鼓励读者在我们的项目网站上亲自探索这些模型：https://smerf-3d.github.io. et.al.|[2312.07541](http://arxiv.org/abs/2312.07541)|null|
|**2023-12-09**|**Robo360: A 3D Omnispective Multi-Material Robotic Manipulation Dataset**|长期以来，制造能够自动化劳动密集型任务的机器人一直是计算机视觉和机器人界进步的核心动力。最近人们对利用3D算法，特别是神经领域的兴趣，导致了机器人在操作场景中的感知和物理理解方面的进步。然而，现实世界的复杂性带来了重大挑战。为了应对这些挑战，我们提出了Robo360，这是一个以机器人操作为特征的数据集，具有密集的视图覆盖范围，能够实现高质量的3D神经表示学习，以及一组具有各种物理和光学特性的不同对象，有助于各种对象操作和物理世界建模任务的研究。我们使用现有的动态NeRF来确认我们的数据集的有效性，并评估其在学习多视图策略方面的潜力。我们希望Robo360能够在理解3D物理世界和机器人控制的交叉点上开辟新的研究方向。 et.al.|[2312.06686](http://arxiv.org/abs/2312.06686)|null|
|**2023-12-11**|**Representing stimulus motion with waves in adaptive neural fields**|神经活动的行波在皮层网络中自发出现，并对刺激做出反应。波的时空结构可以指示它们编码的信息以及维持它们的生理过程。在这里，我们研究了作为视觉运动处理模型的自适应神经场中出现的行波的刺激响应关系。神经场方程将皮层组织的活动建模为连续的可兴奋介质，自适应过程提供负反馈，产生局部活动模式。在我们的模型中，突触连接由一个积分核来描述，该积分核由于依赖于活动的突触抑制而动态减弱，导致边缘稳定的行进前沿（具有衰减的后部）或固定速度的脉冲。我们的分析量化了弱刺激如何随着时间的推移改变这些波的相对位置，其特征是我们扰动地获得的波响应函数。持续和连续可见的刺激模拟移动的视觉对象。在视觉空间中跳跃的间歇性闪光可以产生流畅的视觉运动体验。我们的理论和数值模拟很好地描述了波对两种运动刺激的夹带，提供了视觉运动感知的机制描述。 et.al.|[2312.06100](http://arxiv.org/abs/2312.06100)|null|
|**2023-12-10**|**Accurate Differential Operators for Hybrid Neural Fields**|神经场已广泛应用于从形状表示到神经渲染以及求解偏微分方程（PDE）的各个领域。随着混合神经场表示的出现，如利用小MLP和显式表示的即时NGP，这些模型训练迅速，可以适应大型场景。然而，在渲染和模拟等许多应用中，混合神经场可能会导致明显且不合理的伪影。这是因为它们不能产生这些下游应用所需的精确的空间导数。在这项工作中，我们提出了两种规避这些挑战的方法。我们的第一种方法是一种事后算子，它使用局部多项式拟合从预先训练的混合神经场中获得更准确的导数。此外，我们还提出了一种自监督微调方法，该方法在保留初始信号的同时，对神经场进行细化，以直接产生准确的导数。我们展示了我们的方法在渲染、碰撞模拟和求解偏微分方程中的应用。我们观察到，使用我们的方法可以产生更准确的导数，减少伪影，并在下游应用中实现更准确的模拟。 et.al.|[2312.05984](http://arxiv.org/abs/2312.05984)|null|
|**2023-12-11**|**Nuvo: Neural UV Mapping for Unruly 3D Representations**|现有的UV映射算法被设计为在性能良好的网格上操作，而不是由最先进的3D重建和生成技术产生的几何表示。因此，将这些方法应用于由神经辐射场和相关技术（或从这些场三角化的网格）恢复的体积密度会导致纹理图谱过于分散，无法用于视图合成或外观编辑等任务。我们提出了一种UV映射方法，旨在对通过3D重建和生成技术产生的几何体进行操作。我们的方法Nuvo不是计算在网格顶点上定义的映射，而是使用神经场来表示连续的UV映射，并将其优化为仅针对一组可见点（即仅影响场景外观的点）的有效且性能良好的映射。我们展示了我们的模型对不良几何体带来的挑战是稳健的，并且它生成了可以表示详细外观的可编辑UV映射。 et.al.|[2312.05283](http://arxiv.org/abs/2312.05283)|null|
|**2023-12-08**|**Dynamic LiDAR Re-simulation using Compositional Neural Fields**|我们介绍了DyNFL，这是一种新的基于神经场的方法，用于动态驾驶场景中激光雷达扫描的高保真度重新模拟。DyNFL处理来自动态环境的激光雷达测量，并伴随着移动物体的边界框，以构建可编辑的神经场。该字段包括单独重建的静态背景和动态对象，允许用户在重新模拟的场景中修改视点、调整对象位置以及无缝添加或删除对象。我们方法的一个关键创新是神经场合成技术，该技术通过光线下降测试有效地集成了来自各种场景的重建神经资产，考虑到了遮挡和透明表面。我们对合成和真实世界环境的评估表明，\ShortName大大改进了基于激光雷达扫描的动态场景模拟，提供了物理保真度和灵活编辑功能的组合。 et.al.|[2312.05247](http://arxiv.org/abs/2312.05247)|null|
|**2023-12-08**|**TriHuman : A Real-time and Controllable Tri-plane Representation for Detailed Human Geometry and Appearance Synthesis**|仅从视频数据中创建可控、逼真和几何细节的真人数字替身是计算机图形学和视觉领域的一个关键挑战，尤其是在需要实时性能的情况下。最近的方法将神经辐射场（NeRF）连接到关节结构，例如身体模型或骨骼，以将点映射到姿势规范空间中，同时将NeRF调节在骨骼姿势上。这些方法通常使用多层感知器（MLP）对神经场进行参数化，导致运行时间缓慢。为了解决这一缺点，我们提出了一种新的人体定制、可变形和高效的三平面表示TriHuman，它实现了实时性能、最先进的姿态可控几何合成以及逼真的渲染质量。在核心，我们将全局光线样本非刚性地扭曲到未变形的三平面纹理空间中，这有效地解决了全局点映射到相同三平面位置的问题。然后，我们展示了如何将这种三平面特征表示以骨骼运动为条件，以考虑动态外观和几何结构的变化。我们的研究结果表明，在人类的几何形状和外观建模以及运行时性能方面，朝着更高质量迈出了明确的一步。 et.al.|[2312.05161](http://arxiv.org/abs/2312.05161)|null|
|**2023-12-08**|**GIR: 3D Gaussian Inverse Rendering for Relightable Scene Factorization**|本文提出了一种用于可重照明场景分解的三维高斯逆绘制方法GIR。与利用离散网格或神经隐式场进行反向渲染的现有方法相比，我们的方法利用3D高斯从多视图图像中估计对象的材料特性、照明和几何结构。我们的研究动机是有证据表明，在性能、多功能性和效率方面，3D高斯是比神经领域更有前途的主干。在本文中，我们旨在回答以下问题：“如何应用3D高斯来提高反向渲染的性能？”为了解决基于离散且通常在均匀分布的3D高斯表示中估计法线的复杂性，我们提出了一种高效的自正则化方法，该方法有助于在不需要额外监督的情况下对曲面法线进行建模。为了重建间接照明，我们提出了一种模拟光线跟踪的方法。大量实验证明，在反向渲染中，我们提出的GIR在各种广泛使用的数据集上跨多个任务的性能优于现有方法。这证实了它的功效和广泛的适用性，突出了它作为重新照明和重建中有影响力的工具的潜力。项目页面：https://3dgir.github.io et.al.|[2312.05133](http://arxiv.org/abs/2312.05133)|null|
|**2023-12-06**|**Gaussian-Flow: 4D Reconstruction with Dynamic 3D Gaussian Particle**|我们介绍了高斯流，这是一种新的基于点的方法，用于快速动态场景重建和多视图和单目视频的实时渲染。与因训练和渲染速度缓慢而受到阻碍的流行的基于NeRF的方法相比，我们的方法利用了基于点的3D高斯散射（3DGS）的最新进展。具体而言，提出了一种新的双域变形模型（DDDM）来显式地对每个高斯点的属性变形进行建模，其中通过时域中的多项式拟合和频域中的傅立叶级数拟合来捕获每个属性的时间相关残差。所提出的DDDM能够对长视频镜头中的复杂场景变形进行建模，消除了为每帧训练单独的3DGS的需要，或者引入了额外的隐式神经场来对3D动力学进行建模。此外，离散高斯点的显式变形建模确保了4D场景的超快速训练和渲染，这与为静态3D重建设计的原始3DGS相当。我们提出的方法展示了显著的效率提高，与每帧3DGS建模相比，训练速度快了5倍。此外，定量结果表明，所提出的高斯流在新视图渲染质量方面显著优于以前的主流方法。项目页面：https://nju-3dv.github.io/projects/gaussian-flow et.al.|[2312.03431](http://arxiv.org/abs/2312.03431)|null|

<p align=right>(<a href=#updated-on-20231217>back to top</a>)</p>

[contributors-shield]: https://img.shields.io/github/contributors/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[contributors-url]: https://github.com/Vincentqyw/cv-arxiv-daily/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[forks-url]: https://github.com/Vincentqyw/cv-arxiv-daily/network/members
[stars-shield]: https://img.shields.io/github/stars/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[stars-url]: https://github.com/Vincentqyw/cv-arxiv-daily/stargazers
[issues-shield]: https://img.shields.io/github/issues/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[issues-url]: https://github.com/Vincentqyw/cv-arxiv-daily/issues

