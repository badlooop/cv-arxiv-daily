[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]

## Updated on 2024.11.24
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
|**2024-11-21**|**Novel View Extrapolation with Video Diffusion Priors**|由于辐射场方法的发展，新颖视图合成领域取得了重大进展。然而，大多数辐射场技术在新视图插值方面比新视图外推要好得多，在新视图外推中，合成的新视图远远超出了观察到的训练视图。我们设计了ViewExtrapolator，这是一种新颖的视图合成方法，利用稳定视频扩散（SVD）的生成先验进行逼真的新颖视图外推。通过重新设计SVD去噪过程，ViewExtrapolator细化了辐射场渲染的易产生伪影的视图，大大提高了合成新视图的清晰度和真实感。ViewExtrapolator是一种通用的新型视图外推器，可以处理不同类型的3D渲染，例如当只有单个视图或单眼视频可用时从点云渲染的视图。此外，ViewExtrapolator不需要对SVD进行微调，使其既具有数据效率，又具有计算效率。大量实验证明了ViewExtrapolator在新的视图外推中的优越性。项目页面：\url{https://kunhao-liu.github.io/ViewExtrapolator/}. et.al.|[2411.14208](http://arxiv.org/abs/2411.14208)|null|
|**2024-11-21**|**Image Compression Using Novel View Synthesis Priors**|实时视觉反馈对于远程操作车辆的无远程控制至关重要，特别是在检查和操作任务期间。尽管声通信是水下中程通信的首选，但其有限的带宽使得实时传输图像或视频变得不切实际。为了解决这个问题，我们提出了一种基于模型的图像压缩技术，该技术利用了先前的任务信息。我们的方法采用经过训练的基于机器学习的新颖视图合成模型，并使用梯度下降优化来细化潜在表示，以帮助生成相机图像和渲染图像之间的可压缩差异。我们使用来自人工海洋盆地的数据集评估了所提出的压缩技术，证明了其优于现有技术的压缩比和图像质量。此外，我们的方法对场景中新对象的引入表现出鲁棒性，突出了其推进无遥控车辆操作的潜力。 et.al.|[2411.13862](http://arxiv.org/abs/2411.13862)|null|
|**2024-11-20**|**Sparse Input View Synthesis: 3D Representations and Reliable Priors**|新颖视点合成是指从几个视点合成给定图像的场景的新颖视点的问题。这是计算机视觉和图形学中的一个基本问题，它支持各种各样的应用程序，如元宇宙、事件的免费观看、视频游戏、视频稳定和视频压缩。最近的3D表示，如辐射场和多平面图像，显著提高了从新视点渲染的图像的质量。然而，这些模型需要对输入视图进行密集采样，以获得高质量的渲染。当只有少数输入视图可用时，它们的性能会显著下降。本文主要研究静态和动态场景的稀疏输入新视图合成问题。 et.al.|[2411.13631](http://arxiv.org/abs/2411.13631)|null|
|**2024-11-19**|**PR-ENDO: Physically Based Relightable Gaussian Splatting for Endoscopy**|内窥镜手术对癌症的诊断至关重要，三维重建环境以实时合成新视图可以显著提高诊断水平。我们提出了PR-ENDO，这是一个在基于物理的、可重新照明的模型中利用3D高斯散斑的框架，该模型专为内窥镜中的复杂采集条件而定制，例如受限的相机旋转和强烈的视图依赖照明。通过利用相机和光源之间的连接，我们的方法引入了一个重新照明模型，使用基于物理的渲染和MLP来捕捉光和组织之间的复杂相互作用。现有的方法在这些条件下通常会产生伪影和不一致性，PR-ENDO通过结合利用光角度和法向量的专用漫反射MLP来克服这些问题，即使在有限的训练相机旋转下也能实现稳定的重建。我们使用公开可用的数据集和新引入的具有更宽相机旋转的数据集对我们的框架进行了基准测试。与基线方法相比，我们的方法显示出卓越的图像质量。 et.al.|[2411.12510](http://arxiv.org/abs/2411.12510)|**[link](https://github.com/SanoScience/PR-ENDO)**|
|**2024-11-20**|**Beyond Gaussians: Fast and High-Fidelity 3D Splatting with Linear Kernels**|3D高斯散斑（3DGS）的最新进展大大改善了新颖的视图合成，实现了高质量的重建和实时渲染。然而，模糊伪影，如浮动基元和过度重建，仍然具有挑战性。当前的方法通过细化场景结构、增强几何表示、解决训练图像中的模糊、提高渲染一致性和优化密度控制来解决这些问题，但内核设计的作用仍未得到充分探索。我们确定高斯椭球体的软边界是这些伪影的原因之一，限制了高频区域的细节捕捉。为了弥合这一差距，我们引入了3D线性散布（3DLS），它用线性核替换高斯核，以获得更清晰、更精确的结果，特别是在高频区域。通过对三个数据集的评估，3DLS展示了最先进的保真度和准确性，以及比基线3DGS提高30%的FPS。该实施将在接受后公开。 et.al.|[2411.12440](http://arxiv.org/abs/2411.12440)|null|
|**2024-11-20**|**DGTR: Distributed Gaussian Turbo-Reconstruction for Sparse-View Vast Scenes**|新的视图合成（NVS）方法在大规模场景重建中起着至关重要的作用。然而，这些方法严重依赖于密集的图像输入和长时间的训练，使得它们不适合计算资源有限的地方。此外，在广阔的环境中，很少有拍摄方法会遇到重建质量差的问题。本文提出了DGTR，这是一种新的分布式框架，用于稀疏视图广阔场景的高效高斯重建。我们的方法将场景划分为多个区域，由具有稀疏图像输入的无人机独立处理。使用前馈高斯模型，我们预测高质量的高斯基元，然后使用全局对齐算法来确保几何一致性。综合视图和深度先验被纳入以进一步增强训练，而基于蒸馏的模型聚合机制能够实现高效的重建。我们的方法在显著减少的训练时间内实现了高质量的大规模场景重建和新颖的视图合成，在速度和可扩展性方面都优于现有方法。我们在广阔的空中场景中展示了我们的框架的有效性，在几分钟内实现了高质量的结果。代码将在我们的[https://3d-aigc.github.io/DGTR]. et.al.|[2411.12309](http://arxiv.org/abs/2411.12309)|null|
|**2024-11-19**|**LiV-GS: LiDAR-Vision Integration for 3D Gaussian Splatting SLAM in Outdoor Environments**|我们介绍了LiV GS，这是一种户外环境中的LiDAR视觉SLAM系统，它利用3D高斯作为可微分的空间表示。值得注意的是，LiV-GS是第一种在大规模室外场景中直接将离散和稀疏LiDAR数据与连续可微高斯地图对齐的方法，克服了传统LiDAR测绘中固定分辨率的局限性。该系统使用共享的协方差属性进行前端跟踪，将点云与高斯图对齐，并将法线方向整合到损失函数中以细化高斯图。为了在激光雷达视场外可靠稳定地更新高斯分布，我们引入了一种新的条件高斯约束，将这些高斯分布与最近的可靠分布紧密对齐。目标调整使LiV GS能够以7.98 FPS的速率通过新颖的视图合成实现快速准确的映射。广泛的对比实验证明了LiV-GS在SLAM、图像渲染和映射方面的卓越性能。成功的跨模态雷达LiDAR定位突显了LiV GS在跨模态语义定位和高斯图对象分割中的应用潜力。 et.al.|[2411.12185](http://arxiv.org/abs/2411.12185)|null|
|**2024-11-18**|**SpatialDreamer: Self-supervised Stereo Video Synthesis from Monocular Input**|单目输入的立体视频合成是空间计算和虚拟现实领域的一项艰巨任务。这项任务的主要挑战在于用于训练的高质量配对立体视频不足，以及难以保持帧之间的时空一致性。现有的方法主要通过将新颖的视图合成（NVS）技术直接应用于视频来解决这些问题，同时面临着无法有效地表示动态场景和需要大量训练数据等局限性。本文介绍了一种新的通过视频扩散模型的自监督立体视频合成范式，称为SpatialDreamer，它正面应对了挑战。首先，为了解决立体视频数据不足的问题，我们提出了一种基于深度的视频生成模块DVG，该模块采用前向后向渲染机制生成具有几何和时间先验的配对视频。利用DVG生成的数据，我们提出了RefinerNet以及一个自我监督的综合框架，旨在促进高效和专门的培训。更重要的是，我们设计了一个一致性控制模块，该模块由立体偏差强度度量和时间交互学习模块TIL组成，分别用于几何和时间一致性保证。我们根据各种基准方法对提出的方法进行了评估，结果显示了其优越的性能。 et.al.|[2411.11934](http://arxiv.org/abs/2411.11934)|null|
|**2024-11-18**|**GPS-Gaussian+: Generalizable Pixel-wise 3D Gaussian Splatting for Real-Time Human-Scene Rendering from Sparse Views**|微分渲染技术最近在字符的自由视点视频合成方面显示出了有前景的结果。然而，无论是高斯散点还是神经隐式渲染，这些方法通常都需要针对每个主题进行优化，这不符合交互式应用程序中实时渲染的要求。我们提出了一种可推广的高斯散斑方法，用于稀疏视图相机设置下的高分辨率图像渲染。为此，我们引入了在源视图上定义的高斯参数映射，并直接回归高斯属性，用于即时新视图合成，而无需任何微调或优化。我们在纯人类数据或人类场景数据上训练高斯参数回归模块，并与深度估计模块联合将2D参数图提升到3D空间。所提出的框架在深度和渲染监督或仅渲染监督方面都是完全可区分的。我们进一步引入了正则化项和极线注意机制，以保持两个源视图之间的几何一致性，特别是在忽略深度监督的情况下。在几个数据集上的实验表明，我们的方法优于最先进的方法，同时实现了超高的渲染速度。 et.al.|[2411.11363](http://arxiv.org/abs/2411.11363)|null|
|**2024-11-17**|**Direct and Explicit 3D Generation from a Single Image**|当前的图像到3D方法存在计算成本高和缺乏高分辨率输出的可扩展性的问题。相比之下，我们引入了一种新的框架，使用多视图2D深度和RGB图像以及使用重新调整用途的稳定扩散模型的3D高斯特征直接生成显式的表面几何和纹理。我们在U-Net中引入了一个深度分支，用于高效和高质量的多视图、跨域生成，并将极线注意力纳入潜在的像素级多视图一致性解码器中。通过将生成的深度像素反向投影到3D空间中，我们创建了一个结构化的3D表示，该表示可以通过高斯散点渲染或提取到高质量网格中，从而利用额外的新颖视图合成损失来进一步提高我们的性能。大量实验表明，我们的方法在几何和纹理质量方面超越了现有的基线，同时实现了显著更快的生成时间。 et.al.|[2411.10947](http://arxiv.org/abs/2411.10947)|null|

<p align=right>(<a href=#updated-on-20241124>back to top</a>)</p>

## 3D Reconstruction

|Publish Date|Title|Abstract|PDF|Code|
|---|---|---|---|---|
|**2024-11-21**|**EasyHOI: Unleashing the Power of Large Models for Reconstructing Hand-Object Interactions in the Wild**|我们的工作旨在从单视图图像重建手与物体的相互作用，这是一项基本但不适定的任务。与从视频、多视图图像或预定义的3D模板重建的方法不同，由于固有的模糊性和遮挡，单视图重建面临着重大挑战。手部姿势的多样性以及物体形状和大小的多样性进一步放大了这些挑战。我们的关键见解是，目前用于分割、修复和3D重建的基础模型可以稳健地推广到野外图像，这可以为重建手部对象交互提供强大的视觉和几何先验。具体来说，给定一张图像，我们首先设计了一个新的管道，使用现成的大型模型来估计潜在的手部姿势和物体形状。此外，在初始重建中，我们采用了一种先验引导优化方案，该方案优化了手部姿势，以符合3D物理约束和2D输入图像内容。我们在多个数据集上进行了实验，结果表明我们的方法始终优于基线，并忠实地重建了一组不同的手-物体交互。以下是我们项目页面的链接：https://lym29.github.io/EasyHOI-page/ et.al.|[2411.14280](http://arxiv.org/abs/2411.14280)|null|
|**2024-11-20**|**Open-World Amodal Appearance Completion**|理解和重建被遮挡的对象是一个具有挑战性的问题，特别是在类别和背景多样且不可预测的开放世界场景中。然而，传统方法通常仅限于封闭的对象类别集，限制了它们在复杂的开放世界场景中的使用。我们介绍了Open World Amodal Appearance Completion，这是一个无需训练的框架，通过接受灵活的文本查询作为输入来扩展Amodal补全功能。我们的方法推广到由直接项和抽象查询指定的任意对象。我们将这种能力推理称为amodal完成，其中系统根据提供的图像和语言查询重建查询对象的完整外观。我们的框架统一了分割、遮挡分析和修复，以处理复杂的遮挡，并将完成的对象生成为RGBA元素，从而能够无缝集成到3D重建和图像编辑等应用程序中。广泛的评估证明了我们的方法在推广到新物体和遮挡物方面的有效性，为开放世界环境中的无模完成建立了新的基准。代码和数据集将在论文验收后发布。 et.al.|[2411.13019](http://arxiv.org/abs/2411.13019)|null|
|**2024-11-20**|**M3D: Dual-Stream Selective State Spaces and Depth-Driven Framework for High-Fidelity Single-View 3D Reconstruction**|在复杂场景中从单个RGB图像精确重建3D对象是虚拟现实、自动驾驶和机器人技术的一个关键挑战。现有的神经隐式3D表示方法在平衡全局和局部特征的提取方面面临着重大困难，特别是在多样化和复杂的环境中，导致重建精度和质量不足。我们提出了M3D，一种新颖的单视图3D重建框架，以应对这些挑战。该框架采用基于选择性状态空间的双流特征提取策略，有效地平衡了全局和局部特征的提取，从而提高了场景理解和表示精度。此外，并行分支提取深度信息，有效地整合视觉和几何特征，以提高重建质量并保留复杂的细节。实验结果表明，通过双分支特征提取将多尺度特征与深度信息融合，显著提高了几何一致性和保真度，实现了最先进的重建性能。 et.al.|[2411.12635](http://arxiv.org/abs/2411.12635)|**[link](https://github.com/AnnnnnieZhang/M3D)**|
|**2024-11-19**|**3D Reconstruction by Looking: Instantaneous Blind Spot Detector for Indoor SLAM through Mixed Reality**|室内SLAM经常遇到场景漂移、双墙和盲点等问题，特别是在重建任务中物体靠近传感器（如LiDAR和摄像头）的密闭空间中。数据收集期间点云注册的实时可视化可能有助于缓解这些问题，但无法将扫描数据与实际物理环境进行深入比较仍然是一个重大限制。这些挑战阻碍了重建产品的质量，经常需要重新审视和重新扫描。为此，我们开发了LiMRSF（LiDAR MR RGB传感器融合）系统，允许用户通过混合现实（MR）耳机查看来感知现场点云注册。这个定制的框架将点云网格可视化为全息图，与透视眼镜上的实时场景无缝匹配，并自动突出显示重叠时检测到的错误。这种全息元素通过TCP服务器传输到MR耳机，在那里进行校准，使其与世界坐标、物理位置对齐。这允许用户即时查看本地化的重建产品，使他们能够快速识别盲点和错误，并在现场迅速采取行动。我们的盲点检测器实现了错误检测精度，F1分数为75.76%，通过LiMRSF系统实现了可接受的高保真度监测（在简化网格模型的五个不同部分中，最高SSIM为0.5619，PSNR为14.1004，最低MSE为0.0389，用户通过LiMRSF设备透过眼镜进行可视化）。这种方法可确保为3D模型创建详细、高质量的数据集，在建筑信息建模（BIM）中具有潜在的应用，但不仅限于此。 et.al.|[2411.12514](http://arxiv.org/abs/2411.12514)|null|
|**2024-11-19**|**Target Height Estimation Using a Single Acoustic Camera for Compensation in 2D Seabed Mosaicking**|这封信提出了一种补偿二维海底拼接中目标高度数据的新方法，用于低能见度水下感知。由于其高分辨率成像能力和对黑暗和浑浊的鲁棒性，声相机是感知海洋环境的有效传感器。然而，成像过程中仰角的损失导致原始声相机图像中缺乏目标高度信息，导致海底拼接的二维表示过于简单。在感知杂乱和未经探索的海洋环境时，目标高度数据对于避免与海洋机器人碰撞至关重要。本研究提出了一种使用单个声相机估计海底目标高度的新方法，并将高度数据整合到二维海底拼接中，以补偿海底目标缺失的三维维度。与模拟仰角损失以实现海底三维重建的经典方法不同，本研究侧重于利用可用的声投射阴影线索和简单的传感器运动来快速估计目标高度。通过水箱实验和模拟实验验证了我们建议的可行性。 et.al.|[2411.12338](http://arxiv.org/abs/2411.12338)|null|
|**2024-11-19**|**MTFusion: Reconstructing Any 3D Object from Single Image Using Multi-word Textual Inversion**|从单视图图像重建3D模型是计算机视觉中一个长期存在的问题。单图像3D重建的最新进展是从输入图像中提取文本描述，并进一步利用它来合成3D模型。然而，现有的方法侧重于捕捉图像的单个关键属性（例如，对象类型、艺术风格），而没有考虑到精确3D重建所需的多视角信息，如对象形状和材料属性。此外，对神经辐射场的依赖阻碍了它们重建复杂表面和纹理细节的能力。在这项工作中，我们提出了MTFusion，它利用图像数据和文本描述进行高保真3D重建。我们的方法包括两个阶段。首先，我们采用了一种新颖的多词文本反转技术来提取捕获图像特征的详细文本描述。然后，我们使用此描述和图像使用FlexiCubes生成3D模型。此外，MTFusion通过为有符号距离函数采用特殊的解码器网络来增强FlexiCubes，从而实现更快的训练和更精细的表面表示。广泛的评估表明，我们的MTFusion在广泛的合成和现实世界图像上超越了现有的图像到3D方法。此外，消融研究证明了我们网络设计的有效性。 et.al.|[2411.12197](http://arxiv.org/abs/2411.12197)|null|
|**2024-11-18**|**Towards Degradation-Robust Reconstruction in Generalizable NeRF**|跨场景的广义神经辐射场（GNeRF）已被证明是一种有效的方法，通过用源图像的深度图像特征表示场景来避免每场景优化。然而，尽管GNeRF具有现实应用的潜力，但关于其对源图像中存在的不同类型退化的鲁棒性的研究有限。缺乏此类研究的主要原因是缺乏适合训练退化鲁棒可推广NeRF模型的大规模数据集。为了解决这一差距并促进对3D重建任务退化鲁棒性的研究，我们构建了Objaverse模糊数据集，该数据集包含来自1000多个设置的50000张图像，具有多个级别的模糊退化。此外，我们设计了一个简单且与模型无关的模块，用于增强GNeRF的退化鲁棒性。具体而言，通过轻量级深度估计器和去噪器提取3D感知特征，所提出的模块在不同退化类型和水平下，在定量和视觉质量方面都比GNeRF中的不同流行方法有所改进。我们的数据集和代码将公开。 et.al.|[2411.11691](http://arxiv.org/abs/2411.11691)|null|
|**2024-11-18**|**VLN-Game: Vision-Language Equilibrium Search for Zero-Shot Semantic Navigation**|遵循人类指令在陌生环境中探索和搜索指定目标是移动服务机器人的一项关键技能。之前关于目标导航的大部分工作通常都集中在单一输入模态作为目标上，这可能会导致对包含详细属性和空间关系的语言描述的考虑有限。为了解决这一限制，我们提出了VLN-Game，这是一种新的用于视觉目标导航的零样本框架，可以有效地处理对象名称和描述性语言目标。更精确地说，我们的方法通过将预训练的视觉语言特征与物理环境的3D重建相结合，构建了一个以3D对象为中心的空间地图。然后，该框架确定了最有希望探索的领域，以寻找潜在的目标候选者。采用博弈论视觉语言模型来确定哪个目标与给定的语言描述最匹配。在Habitat Matterport 3D（HM3D）数据集上进行的实验表明，所提出的框架在目标导航和基于语言的导航任务中都达到了最先进的性能。此外，我们证明了VLN Game可以很容易地部署在现实世界的机器人上。VLN-Game的成功凸显了使用博弈论方法和紧凑的视觉语言模型来提高机器人系统决策能力的巨大潜力。可以通过以下链接访问补充视频和代码：https://sites.google.com/view/vln-game. et.al.|[2411.11609](http://arxiv.org/abs/2411.11609)|null|
|**2024-11-17**|**BVI-CR: A Multi-View Human Dataset for Volumetric Video Compression**|沉浸式技术和3D重建的进步使得能够创建具有精细细节的现实世界物体和环境的数字复制品。这些过程会生成大量的3D数据，需要更有效的压缩方法来满足与数据存储和传输相关的内存和带宽限制。然而，有效的3D数据压缩方法的开发和验证受到缺乏全面和高质量的体视频数据集的限制，与2D图像和视频数据库相比，这通常需要付出更多的努力来获取和消耗更多的资源。为了弥合这一差距，我们提出了一个开放的多视图体积人体数据集，称为BVI-CR，其中包含18个多视图RGB-D捕获及其相应的纹理多边形网格，描绘了一系列不同的人体动作。每个视频序列包含10个1080p分辨率的视图，持续时间为10-15秒，帧率为30FPS。使用BVI-CR，我们按照MPEG MIV通用测试条件，对三种传统的基于神经坐标的多视图视频压缩方法进行了基准测试，并根据各种质量指标报告了它们的速率质量性能。结果表明，与传统的视频编码方法相比，基于神经表示的方法在体视频压缩中具有巨大的潜力（PSNR平均编码增益高达38%）。该数据集为各种任务提供了一个开发和验证平台，包括体积重建、压缩和质量评估。数据库将在\url公开共享{https://github.com/fan-aaron-zhang/bvi-cr}. et.al.|[2411.11199](http://arxiv.org/abs/2411.11199)|null|
|**2024-11-16**|**ARM: Appearance Reconstruction Model for Relightable 3D Generation**|最近的图像到3D重建模型极大地改进了几何生成，但它们仍然难以忠实地生成逼真的外观。为了解决这个问题，我们引入了ARM，这是一种从稀疏视图图像重建高质量3D网格和逼真外观的新方法。ARM的核心在于将几何与外观解耦，在UV纹理空间内处理外观。与以前的方法不同，ARM通过明确地将测量值反向投影到纹理贴图上，并在具有全局感受野的UV空间模块中对其进行处理，从而提高了纹理质量。为了解决输入图像中材质和光照之间的歧义，ARM引入了一种材质先验，对语义外观信息进行编码，增强了外观分解的鲁棒性。仅在8个H100 GPU上训练，ARM在数量和质量上都优于现有方法。 et.al.|[2411.10825](http://arxiv.org/abs/2411.10825)|null|

<p align=right>(<a href=#updated-on-20241124>back to top</a>)</p>

## Diffusion

|Publish Date|Title|Abstract|PDF|Code|
|---|---|---|---|---|
|**2024-11-21**|**Stable Flow: Vital Layers for Training-Free Image Editing**|扩散模型彻底改变了内容合成和编辑领域。最近的模型用扩散变换器（DiT）取代了传统的UNet架构，并采用流匹配来改进训练和采样。然而，他们表现出有限的代际多样性。在这项工作中，我们利用这一限制，通过选择性注入注意力特征来执行一致的图像编辑。主要的挑战是，与基于UNet的模型不同，DiT缺乏从粗到细的合成结构，因此不清楚在哪些层进行注射。因此，我们提出了一种自动方法来识别DiT中对图像形成至关重要的“重要层”，并演示了这些层如何使用相同的机制促进一系列受控的稳定编辑，从非刚性修改到对象添加。接下来，为了实现真实的图像编辑，我们介绍了一种改进的流模型图像反演方法。最后，我们通过定性和定量比较以及用户研究来评估我们的方法，并证明其在多个应用程序中的有效性。项目页面可在https://omriavrahami.com/stable-flow et.al.|[2411.14430](http://arxiv.org/abs/2411.14430)|null|
|**2024-11-21**|**Low-Field Regime of Magnon Transport in Yttrium Iron Garnet**|自旋波及其量子磁振子在原型磁绝缘体钇铁石榴石（YIG）中的扩散传播是低功耗和低损耗数据通信研究的热点。然而，在外部磁场下操作会缩短磁振子扩散长度，衰减测量端子处的电压振幅，并使磁振子器件的架构复杂化。在这里，我们探索了YIG薄膜中扩散磁振子输运的低场和无场状态。我们证明，只有在零场极限下，才能完全抑制场诱导的磁振子扩散长度的抑制。即使是10mT的适度磁场，在长度为1 $mu$m的传输通道中，也会使非局域自旋电压衰减20$%$ 。通过Stoner-Wohlfarth宏观pin模拟，我们发现一个经常被忽视的平面内单轴各向异性成为控制磁振子器件无场运行的关键参数。我们进一步证明了与低温下YIG薄膜的平面内单轴各向异性相关的有效场增强了十倍，这是磁振子器件在低温条件下无场操作的关键发现。 et.al.|[2411.14428](http://arxiv.org/abs/2411.14428)|null|
|**2024-11-21**|**Unleashing the Potential of Multi-modal Foundation Models and Video Diffusion for 4D Dynamic Physical Scene Simulation**|动态场景的真实模拟需要准确捕捉各种材料属性，并基于物理原理对复杂的对象交互进行建模。然而，现有的方法仅限于具有有限可预测参数的基本材料类型，不足以表示现实世界材料的复杂性。我们介绍了一种新方法，该方法利用多模态基础模型和视频扩散来实现增强的4D动态场景模拟。我们的方法利用多模态模型来识别材质类型，并通过图像查询初始化材质参数，同时推断3D高斯斑点以进行详细的场景表示。我们使用可微分材料点法（MPM）和光流引导的视频扩散进一步细化这些材料参数，而不是渲染损失或分数蒸馏采样（SDS）损失。该集成框架能够准确预测和真实模拟现实世界场景中的动态交互，提高基于物理的模拟的准确性和灵活性。 et.al.|[2411.14423](http://arxiv.org/abs/2411.14423)|null|
|**2024-11-21**|**Baking Gaussian Splatting into Diffusion Denoiser for Fast and Scalable Single-stage Image-to-3D Generation**|现有的前馈图像到3D方法主要依赖于2D多视图扩散模型，无法保证3D的一致性。这些方法在更改提示视图方向时很容易崩溃，主要处理以对象为中心的提示图像。本文提出了一种新的单级3D扩散模型DiffusionGS，用于从单个视图生成对象和场景。DiffusionGS在每个时间步直接输出3D高斯点云，以增强视图一致性，并允许模型在以对象为中心的输入之外，生成任何方向的稳健提示视图。此外，为了提高DiffusionGS的能力和泛化能力，我们通过开发场景-对象混合训练策略来扩展3D训练数据。实验表明，我们的方法具有更好的生成质量（PSNR高2.20 dB，FID低23.25 dB），速度比SOTA方法快5倍以上（在A100 GPU上约6秒）。用户研究和文本到3D应用也揭示了我们方法的实用价值。我们的项目页面位于https://caiyuanhao1998.github.io/project/DiffusionGS/显示视频和交互式生成结果。 et.al.|[2411.14384](http://arxiv.org/abs/2411.14384)|null|
|**2024-11-21**|**CoNFiLD-inlet: Synthetic Turbulence Inflow Using Generative Latent Diffusion Models with Neural Fields**|涡流解析湍流模拟需要随机流入条件，以准确复制复杂的多尺度湍流结构。传统的基于再循环的方法依赖于计算昂贵的前体模拟，而现有的合成流入发生器往往无法再现真实的湍流相干结构。深度学习（DL）的最新进展为流入湍流生成开辟了新的可能性，但许多基于DL的方法依赖于确定性、自回归框架，容易产生误差累积，导致长期预测的鲁棒性较差。在这项工作中，我们提出了CoNFiLD入口，这是一种基于DL的新型流入湍流发生器，它将扩散模型与条件神经场（CNF）编码的潜在空间相结合，以产生逼真的随机流入湍流。通过使用雷诺数对流入条件进行参数化，CoNFiLD入口在很宽的雷诺数范围内（ $Re_tau$在$10^3$和$10^4$ 之间）有效地推广，而不需要重新训练或参数调整。通过直接数值模拟（DNS）和壁模型大涡模拟（WMLES）中的先验和后验测试进行的全面验证证明了其高保真度、鲁棒性和可扩展性，使其成为流入湍流合成的高效和通用解决方案。 et.al.|[2411.14378](http://arxiv.org/abs/2411.14378)|null|
|**2024-11-21**|**Anomalous transport in U(1)-symmetric quantum circuits**|在这项工作中，我们研究了在一系列不同动力学状态下调谐的通用U（1）对称无序模型中的离散时间输运。我们开发了一个总量，一个圆形统计矩，它是磁化分布的简单函数，可以很好地捕捉系统的输运特性。从这个量中，我们提取了输运指数，揭示了相图中与局域、扩散和超扩散状态一致的行为，最有趣的是，对于无序系统来说，这是超扩散状态。对这种超扩散机制的研究表明，存在一种离散时间系统特有的预热“swappy”机制，在这种机制中，激励相干传播；即使在存在严重混乱的情况下。 et.al.|[2411.14357](http://arxiv.org/abs/2411.14357)|null|
|**2024-11-21**|**Enhancing Medical Image Segmentation with Deep Learning and Diffusion Models**|医学图像分割对于准确的临床诊断至关重要，但它面临着病变和正常组织之间对比度低、边界不清、患者之间差异大等挑战。深度学习提高了分割的准确性和效率，但它仍然严重依赖专家注释，并与医学图像的复杂性作斗争。医学图像数据集的小尺寸和数据采集的高成本进一步限制了分割网络的性能。扩散模型及其迭代去噪过程为分割中更好的细节捕获提供了一种有前景的替代方案。然而，它们在精确分割小目标和保持边界细节的精度方面面临困难。本文讨论了医学图像分割的重要性、当前深度学习方法的局限性以及扩散模型解决这些挑战的潜力。 et.al.|[2411.14353](http://arxiv.org/abs/2411.14353)|null|
|**2024-11-21**|**Generalized Finite Difference Method for Solving Stochastic Diffusion Equations**|随机扩散方程对于模拟受不确定性影响的一系列物理现象至关重要。我们介绍了求解这些方程的广义有限差分法。然后，我们检验了它的一致性、稳定性和均方收敛性，表明所提出的方法在适当的假设下保持了稳定性，并表现出良好的收敛特性。为了验证该方法，我们在一维、二维和三维空间域中给出了数值结果。 et.al.|[2411.14333](http://arxiv.org/abs/2411.14333)|null|
|**2024-11-21**|**StereoCrafter-Zero: Zero-Shot Stereo Video Generation with Noisy Restart**|生成模仿人类双眼视觉的高质量立体视频需要在帧之间保持一致的深度感知和时间连贯性。虽然扩散模型具有先进的图像和视频合成技术，但由于难以保持左右视图之间一致的时间和空间连贯性，生成高质量的立体视频仍然具有挑战性。我们介绍\textit｛StereoCrafter-Zero｝，这是一种用于零样本立体视频生成的新框架，它利用视频扩散先验而不需要成对的训练数据。关键创新包括一种噪声重启策略，用于初始化立体声感知延迟，以及一个迭代细化过程，逐步协调潜在空间，解决时间闪烁和视图不一致等问题。综合评估，包括定量指标和用户研究，表明\textit{StereoCrafter Zero}即使在深度估计不完美的情况下，也能产生具有改进的深度一致性和时间平滑性的高质量立体视频。我们的框架在各种扩散模型中都具有强大的适应性，为零样本立体视频生成树立了新的基准，并实现了更身临其境的视觉体验。我们的代码可以在~\url中找到{https://github.com/shijianjian/StereoCrafter-Zero}. et.al.|[2411.14295](http://arxiv.org/abs/2411.14295)|null|
|**2024-11-21**|**Guided MRI Reconstruction via Schrödinger Bridge**|磁共振成像（MRI）是一种多对比度成像技术，其中不同的对比度图像共享相似的结构信息。然而，传统的扩散模型很难有效地利用这种结构相似性。最近，薛定谔桥（SB）是扩散模型的非线性扩展，被提出用于在任何分布之间建立扩散路径，允许引入引导先验。本研究提出了一种基于SB的多对比度图像引导重建框架，在引导和目标图像分布之间建立扩散桥。通过在采样过程中使用引导图像和数据一致性，可以更准确地重建目标图像。为了更好地解决图像之间的结构差异，我们引入了一种来自图像编辑领域的反演策略，称为 $\mathbf{I}^2$SB反演。在配对的T1和T2-FLAIR数据集上的实验表明，$\mathbf{I}^ 2$ SB的反演实现了高精度。加速度高达14.4，在重建精度和稳定性方面都优于现有方法。 et.al.|[2411.14269](http://arxiv.org/abs/2411.14269)|null|

<p align=right>(<a href=#updated-on-20241124>back to top</a>)</p>

## NeRF

|Publish Date|Title|Abstract|PDF|Code|
|---|---|---|---|---|
|**2024-11-21**|**CoNFiLD-inlet: Synthetic Turbulence Inflow Using Generative Latent Diffusion Models with Neural Fields**|涡流解析湍流模拟需要随机流入条件，以准确复制复杂的多尺度湍流结构。传统的基于再循环的方法依赖于计算昂贵的前体模拟，而现有的合成流入发生器往往无法再现真实的湍流相干结构。深度学习（DL）的最新进展为流入湍流生成开辟了新的可能性，但许多基于DL的方法依赖于确定性、自回归框架，容易产生误差累积，导致长期预测的鲁棒性较差。在这项工作中，我们提出了CoNFiLD入口，这是一种基于DL的新型流入湍流发生器，它将扩散模型与条件神经场（CNF）编码的潜在空间相结合，以产生逼真的随机流入湍流。通过使用雷诺数对流入条件进行参数化，CoNFiLD入口在很宽的雷诺数范围内（ $Re_tau$在$10^3$和$10^4$ 之间）有效地推广，而不需要重新训练或参数调整。通过直接数值模拟（DNS）和壁模型大涡模拟（WMLES）中的先验和后验测试进行的全面验证证明了其高保真度、鲁棒性和可扩展性，使其成为流入湍流合成的高效和通用解决方案。 et.al.|[2411.14378](http://arxiv.org/abs/2411.14378)|null|
|**2024-11-20**|**FAST-Splat: Fast, Ambiguity-Free Semantics Transfer in Gaussian Splatting**|我们提出了FAST Splat，用于快速、无歧义的语义高斯Splatting，旨在解决现有语义高斯Splatting方法的主要局限性，即：训练和渲染速度慢；内存使用率高；语义对象定位模糊。在推导FAST Splat时，我们将开放词汇语义高斯Splatting表述为将闭集语义蒸馏扩展到开放集（开放词汇）设置的问题，使FAST Splat能够提供精确的语义对象定位结果，即使在用户提供的模糊自然语言查询提示时也是如此。此外，通过最大限度地利用高斯散斑场景表示的显式形式，FAST Splat保留了高斯散斑的显著训练和渲染速度。具体来说，虽然现有的语义高斯散斑方法将语义提取到一个单独的神经场中或利用神经模型进行降维，但FAST Splat直接用特定的语义代码增强每个高斯分布，保留了高斯散斑相对于神经场方法的训练、渲染和内存使用优势。与先前的方法不同，这些高斯特定的语义代码以及哈希表使语义相似性能够通过开放词汇表用户提示进行测量，并进一步使FAST Splat能够用明确的语义对象标签和3D掩码进行响应。在实验中，我们证明，与最好的竞争语义高斯Splatting方法相比，FAST Splat的训练速度快4倍至6倍，数据预处理步骤快13倍，渲染速度快18倍至75倍，所需GPU内存大约小3倍。此外，与现有方法相比，FAST Splat实现了相对相似或更好的语义分割性能。审查期结束后，我们将提供项目网站和代码库的链接。 et.al.|[2411.13753](http://arxiv.org/abs/2411.13753)|null|
|**2024-11-20**|**GazeGaussian: High-Fidelity Gaze Redirection with 3D Gaussian Splatting**|在处理分布外数据时，凝视估计遇到了泛化挑战。为了解决这个问题，最近的方法使用神经辐射场（NeRF）来生成增强数据。然而，基于NeRF的现有方法计算成本高昂，缺乏面部细节。三维高斯散斑（3DGS）已成为神经场的主流表示。虽然3DGS已经在头部化身中得到了广泛的研究，但它面临着在不同受试者之间进行精确视线控制和泛化的挑战。在这项工作中，我们提出了GazeGaussian，这是一种高保真的视线重定向方法，它使用双流3DGS模型分别表示面部和眼睛区域。通过利用3DGS的非结构化特性，我们开发了一种基于目标凝视方向的刚性眼睛旋转的新眼睛表示。为了增强各种主题的综合泛化能力，我们集成了一个表达式条件模块来指导神经渲染器。综合实验表明，GazeGaussian在渲染速度、视线重定向精度和跨多个数据集的面部合成方面优于现有方法。我们还证明，现有的凝视估计方法可以利用GazeGaussian来提高其泛化性能。该代码将在以下网址提供：https://ucwxb.github.io/GazeGaussian/. et.al.|[2411.12981](http://arxiv.org/abs/2411.12981)|null|
|**2024-11-18**|**NeuMaDiff: Neural Material Synthesis via Hyperdiffusion**|高质量的材料合成对于复制复杂的表面特性以创建逼真的数字场景至关重要。然而，现有的方法往往在时间和内存方面效率低下，需要领域专业知识，或者需要大量的训练数据，而高维材料数据进一步限制了性能。此外，大多数方法缺乏多模态制导能力和标准化的评估指标，限制了综合任务的控制和可比性。为了解决这些局限性，我们提出了NeuMaDiff，这是一种利用超扩散的新型神经材料合成框架。我们的方法采用神经场作为低维表示，并结合了多模态条件超扩散模型来学习材料重量的分布。这使得通过材料类型、文本描述或参考图像等输入进行灵活指导成为可能，从而对合成提供了更大的控制。为了支持未来的研究，我们贡献了两个新的材料数据集，并引入了两个BRDF分布度量，以进行更严格的评估。我们通过广泛的实验证明了NeuMaDiff的有效性，包括一种新的基于统计的约束合成方法，该方法能够生成所需类别的材料。 et.al.|[2411.12015](http://arxiv.org/abs/2411.12015)|null|
|**2024-11-14**|**The Hydrodynamic Limit of Hawkes Processes on Adaptive Stochastic Networks**|我们确定了自适应网络上相互作用的霍克斯过程网络的大尺寸限制。节点变量的翻转被认为具有由传入边缘和节点的平均场给出的强度。边缘变量的翻转是传入节点变量的函数。边变量可以是对称的，也可以是不对称的。该模型受到社会学、神经科学和流行病学应用的启发。一般来说，极限概率律可以表示为具有强度函数的自洽泊松过程的不动点，该强度函数（i）是延迟的，（ii）取决于其自身的概率律。在边缘翻转仅由突触前神经元的状态决定的特定情况下（如神经科学中），证明了可以获得突触增强和神经增强双重进化的自主神经场型方程。 et.al.|[2411.09260](http://arxiv.org/abs/2411.09260)|null|
|**2024-11-09**|**Epi-NAF: Enhancing Neural Attenuation Fields for Limited-Angle CT with Epipolar Consistency Conditions**|神经场方法最初在逆渲染领域取得了成功，最近已扩展到CT重建，标志着传统技术的范式转变。虽然这些方法在稀疏视图CT重建中提供了最先进的结果，但它们在有限的角度设置中很难实现，在有限的视角范围内捕获输入投影。我们提出了一种基于X射线投影图像中相应极线之间一致性条件的新损失项，旨在规范神经衰减场优化。通过强制执行这些一致性条件，我们的方法Epi NAF将监督从有限角度范围内的输入视图传播到整个锥束CT范围内的预测投影。与基线方法相比，这种损失导致重建的定性和定量改进。 et.al.|[2411.06181](http://arxiv.org/abs/2411.06181)|null|
|**2024-11-07**|**LoFi: Scalable Local Image Reconstruction with Implicit Neural Representation**|神经场或隐式神经表示（INR）因其对图像和3D体积的有效连续表示而在机器学习和信号处理中引起了广泛关注。在这项工作中，我们以INR为基础，引入了一种基于坐标的局部处理框架来解决成像逆问题，称为LoFi（局部场）。与传统的图像重建方法不同，LoFi通过多层感知器（MLP）分别处理每个坐标处的局部信息，在该特定坐标处恢复对象。与INR类似，LoFi可以在任何连续坐标下恢复图像，从而实现多分辨率的图像重建。LoFi在图像重建方面的性能与标准CNN相当或更好，几乎与图像分辨率无关，对分布外数据和内存使用具有出色的泛化能力。值得注意的是，对1024美元×1024美元的图像进行训练只需要3GB的内存，比标准CNN通常需要的内存少20多倍。此外，LoFi的局部设计使其能够在小于10个样本的极小数据集上进行训练，而不会过拟合或需要正则化或提前停止。最后，我们使用LoFi作为即插即用框架中的去噪先验，用于解决一般的逆问题，以受益于其连续的图像表示和强大的泛化能力。尽管在低分辨率图像上进行了训练，但LoFi可以用作低维先验，以解决任何分辨率的逆问题。我们通过各种成像方式验证了我们的框架，从低剂量计算机断层扫描到无线电干涉成像。 et.al.|[2411.04995](http://arxiv.org/abs/2411.04995)|null|
|**2024-11-04**|**Physically Based Neural Bidirectional Reflectance Distribution Function**|我们介绍了基于物理的神经双向反射分布函数（PBNBRDF），这是一种基于神经场的材料外观的新颖连续表示。我们的模型准确地重建了真实世界的材料，同时独特地增强了现实BRDF的物理特性，特别是通过重新参数化的亥姆霍兹互易性和通过高效分析积分的能量无源性。我们进行了系统分析，证明了遵守这些物理定律对重建材料的视觉质量的好处。此外，我们通过引入色度强制监督RGB通道的规范来提高神经BRDF的颜色精度。通过在多个测量的真实BRDF数据库上进行定性和定量实验，我们表明，遵守这些物理约束可以使神经场更忠实、更稳定地表示原始数据，并实现更高的渲染质量。 et.al.|[2411.02347](http://arxiv.org/abs/2411.02347)|null|
|**2024-11-01**|**Intensity Field Decomposition for Tissue-Guided Neural Tomography**|锥束计算机断层扫描（CBCT）通常需要数百次X射线投影，这引起了人们对辐射暴露的担忧。虽然稀疏视图重建通过使用更少的投影来减少曝光，但它很难达到令人满意的图像质量。为了应对这一挑战，本文介绍了一种新的稀疏视图CBCT重建方法，该方法为神经场赋予了人体组织正则化的能力。我们的方法被称为组织引导神经断层扫描（TNT），其动机是CBCT中骨骼和软组织之间明显的强度差异。直观地说，分离这些成分可能有助于神经场的学习过程。更确切地说，TNT包括一个异构的四重网络和相应的训练策略。该网络将强度场表示为软组织和硬组织成分及其各自纹理的组合。我们在估计的组织投影的指导下训练网络，从而能够有效地学习网络头所需的模式。大量实验表明，所提出的方法显著提高了稀疏视图CBCT重建的效率，投影数量从10到60不等。与最先进的基于神经渲染的方法相比，我们的方法以更少的投影和更快的收敛实现了相当的重建质量。 et.al.|[2411.00900](http://arxiv.org/abs/2411.00900)|null|
|**2024-10-26**|**Neural Fields in Robotics: A Survey**|神经场已经成为计算机视觉和机器人技术中3D场景表示的一种变革性方法，能够从姿势的2D数据中准确推断几何、3D语义和动力学。利用可微分渲染，神经场包括连续隐式和显式神经表示，实现了高保真3D重建、多模态传感器数据的集成和新视点的生成。这项调查探讨了它们在机器人技术中的应用，强调了它们在增强感知、规划和控制方面的潜力。它们的紧凑性、内存效率和可微性，以及与基础模型和生成模型的无缝集成，使其成为实时应用的理想选择，提高了机器人的适应性和决策能力。本文基于200多篇论文，对机器人中的神经场进行了全面的回顾，对各个领域的应用进行了分类，并评估了它们的优势和局限性。首先，我们介绍了四个关键的神经场框架：占用网络、有符号距离场、神经辐射场和高斯散斑。其次，我们详细介绍了神经场在五个主要机器人领域的应用：姿态估计、操纵、导航、物理和自动驾驶，重点介绍了关键工作，并讨论了要点和公开挑战。最后，我们概述了神经场在机器人技术中的局限性，并为未来的研究提出了有前景的方向。项目页面：https://robonerf.github.io et.al.|[2410.20220](http://arxiv.org/abs/2410.20220)|**[link](https://github.com/zubair-irshad/Awesome-Implicit-NeRF-Robotics)**|

<p align=right>(<a href=#updated-on-20241124>back to top</a>)</p>

[contributors-shield]: https://img.shields.io/github/contributors/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[contributors-url]: https://github.com/Vincentqyw/cv-arxiv-daily/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[forks-url]: https://github.com/Vincentqyw/cv-arxiv-daily/network/members
[stars-shield]: https://img.shields.io/github/stars/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[stars-url]: https://github.com/Vincentqyw/cv-arxiv-daily/stargazers
[issues-shield]: https://img.shields.io/github/issues/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[issues-url]: https://github.com/Vincentqyw/cv-arxiv-daily/issues

