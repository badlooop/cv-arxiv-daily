[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]

## Updated on 2024.11.20
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
|**2024-11-18**|**GPS-Gaussian+: Generalizable Pixel-wise 3D Gaussian Splatting for Real-Time Human-Scene Rendering from Sparse Views**|微分渲染技术最近在字符的自由视点视频合成方面显示出了有前景的结果。然而，无论是高斯散点还是神经隐式渲染，这些方法通常都需要针对每个主题进行优化，这不符合交互式应用程序中实时渲染的要求。我们提出了一种可推广的高斯散斑方法，用于稀疏视图相机设置下的高分辨率图像渲染。为此，我们引入了在源视图上定义的高斯参数映射，并直接回归高斯属性，用于即时新视图合成，而无需任何微调或优化。我们在纯人类数据或人类场景数据上训练高斯参数回归模块，并与深度估计模块联合将2D参数图提升到3D空间。所提出的框架在深度和渲染监督或仅渲染监督方面都是完全可区分的。我们进一步引入了正则化项和极线注意机制，以保持两个源视图之间的几何一致性，特别是在忽略深度监督的情况下。在几个数据集上的实验表明，我们的方法优于最先进的方法，同时实现了超高的渲染速度。 et.al.|[2411.11363](http://arxiv.org/abs/2411.11363)|null|
|**2024-11-17**|**Direct and Explicit 3D Generation from a Single Image**|当前的图像到3D方法存在计算成本高和缺乏高分辨率输出的可扩展性的问题。相比之下，我们引入了一种新的框架，使用多视图2D深度和RGB图像以及使用重新调整用途的稳定扩散模型的3D高斯特征直接生成显式的表面几何和纹理。我们在U-Net中引入了一个深度分支，用于高效和高质量的多视图、跨域生成，并将极线注意力纳入潜在的像素级多视图一致性解码器中。通过将生成的深度像素反向投影到3D空间中，我们创建了一个结构化的3D表示，该表示可以通过高斯散点渲染或提取到高质量网格中，从而利用额外的新颖视图合成损失来进一步提高我们的性能。大量实验表明，我们的方法在几何和纹理质量方面超越了现有的基线，同时实现了显著更快的生成时间。 et.al.|[2411.10947](http://arxiv.org/abs/2411.10947)|null|
|**2024-11-16**|**DGS-SLAM: Gaussian Splatting SLAM in Dynamic Environment**|我们介绍了动态高斯散斑SLAM（DGS-SLAM），这是第一个建立在高斯散斑基础上的动态SLAM框架。虽然密集SLAM的最新进展利用高斯散斑来增强场景表示，但大多数方法都假设是静态环境，这使得它们容易受到动态对象引起的光度和几何不一致的影响。为了应对这些挑战，我们将高斯散斑SLAM与稳健的滤波过程相结合，以处理整个管道中的动态对象，包括高斯插入和关键帧选择。在此框架内，为了进一步提高动态对象去除的准确性，我们引入了一种鲁棒的掩模生成方法，该方法在关键帧之间强制实现光度一致性，减少了不准确分割和阴影等伪影的噪声。此外，我们提出了循环感知窗口选择机制，该机制利用3D高斯的唯一关键帧ID来检测当前帧和过去帧之间的循环，从而促进当前相机姿态和高斯图的联合优化。DGS-SLAM在各种动态SLAM基准上实现了最先进的相机跟踪和新颖的视图合成性能，证明了其在处理现实世界动态场景方面的有效性。 et.al.|[2411.10722](http://arxiv.org/abs/2411.10722)|null|
|**2024-11-15**|**The Oxford Spires Dataset: Benchmarking Large-Scale LiDAR-Visual Localisation, Reconstruction and Radiance Field Methods**|本文介绍了一个使用定制的多传感器感知单元在牛津著名地标及其周围捕获的大规模多模态数据集，以及来自陆地激光雷达扫描仪（TLS）的毫米级精确地图。感知单元包括三个同步的全局快门彩色相机、一个汽车3D激光雷达扫描仪和一个惯性传感器，所有这些都经过精确校准。我们还为涉及定位、重建和新颖视图合成的任务建立了基准，这些任务能够评估同步定位和映射（SLAM）方法、运动结构（SfM）和多视图立体（MVS）方法，以及神经辐射场（NeRF）和3D高斯散射等辐射场方法。为了评估3D重建，TLS 3D模型被用作地面实况。通过将移动LiDAR扫描注册到TLS 3D模型来计算本地化地面实况。辐射场方法不仅使用从输入轨迹采样的姿态进行评估，还使用来自远离训练姿态的轨迹的视点进行评估。我们的评估表明了最先进的辐射场方法的一个关键局限性：我们表明，它们往往对训练姿势/图像过拟合，并且不能很好地泛化到无序姿势。与使用相同视觉输入的MVS系统相比，它们在3D重建方面也表现不佳。我们的数据集和基准旨在促进辐射场方法和SLAM系统的更好集成。原始和处理后的数据，以及用于解析和评估的软件，可以在以下网址访问https://dynamic.robots.ox.ac.uk/datasets/oxford-spires/. et.al.|[2411.10546](http://arxiv.org/abs/2411.10546)|null|
|**2024-11-15**|**Efficient Density Control for 3D Gaussian Splatting**|3D高斯散斑（3DGS）在新颖的视图合成方面表现出色，在高级渲染质量和实时性能之间取得了平衡。然而，在训练过的场景中，大量低不透明度的高斯分布显著增加了渲染成本。这个问题是由于致密化过程中分割和克隆操作中的缺陷引起的，这些缺陷导致了广泛的高斯重叠和随后的不透明度降低。为了提高高斯利用率，我们改进了3DGS的自适应密度控制。首先，我们引入了一种更有效的长轴分割操作来代替原始的克隆和分割，这减轻了高斯重叠并提高了致密化效率。其次，我们提出了一种简单的自适应修剪技术来减少低不透明度高斯分布的数量。最后，通过动态降低分割阈值和应用重要性加权，进一步提高了高斯利用率。我们在各种具有挑战性的现实世界数据集上评估了我们提出的方法。实验结果表明，我们的高效密度控制（EDC）可以提高渲染速度和质量。 et.al.|[2411.10133](http://arxiv.org/abs/2411.10133)|null|
|**2024-11-14**|**DyGASR: Dynamic Generalized Exponential Splatting with Surface Alignment for Accelerated 3D Mesh Reconstruction**|3D高斯散斑（3DGS）的最新进展带来了高质量的新颖视图合成和加速渲染，显著提高了辐射场重建的质量。然而，从大量微小的3D高斯点中提取网格仍然是一个巨大的挑战，因为高斯分布的体积很大，并且由于其固有的低通特性而难以表示尖锐的信号。为了解决这个问题，我们提出了DyGASR，它利用广义指数函数而不是传统的3D高斯函数来减少粒子数量，并动态优化捕获信号的表示。此外，我们观察到，在不进行修改的情况下，使用广义指数散布（GES）重建网格经常会导致失败，因为广义指数分布质心可能无法与场景表面精确对齐。为了克服这一点，我们采用Sugar的方法并引入了广义表面正则化（GSR），该方法将每个点云的最小缩放向量减少到零，并确保垂直于表面的法线对齐，从而便于后续的泊松表面网格重建。此外，我们提出了一种动态分辨率调整策略，该策略利用余弦调度在训练阶段从低到高逐渐提高图像分辨率，从而避免了恒定的全分辨率，这大大提高了重建速度。我们的方法超越了现有的基于3DGS的网格重建方法，对各种场景数据集的广泛评估证明了这一点，速度提高了25%，内存使用减少了30%。 et.al.|[2411.09156](http://arxiv.org/abs/2411.09156)|null|
|**2024-11-14**|**Mono2Stereo: Monocular Knowledge Transfer for Enhanced Stereo Matching**|由于现有合成数据集的域间隙和真实数据集中GT标签的稀疏性，立体匹配网络的泛化和性能受到限制。相比之下，单目深度估计已经取得了重大进展，受益于大规模深度数据集和自我监督策略。为了弥合单目深度估计和立体匹配之间的性能差距，我们提出利用单目知识转移来增强立体匹配，即Mono2Stereo。我们引入了两阶段训练过程的知识转移，包括合成数据预训练和现实世界数据微调。在预训练阶段，我们设计了一个数据生成管道，从单眼图像中合成立体训练数据。该流水线利用单眼深度进行扭曲和新颖的视图合成，并采用我们提出的边缘感知（EA）修复模块来填充生成图像中缺失的内容。在微调阶段，我们引入了稀疏到密集知识蒸馏（S2DKD）策略，鼓励预测的分布与密集的单眼深度对齐。该策略缓解了稀疏现实标签中的边缘模糊问题，并提高了整体一致性。实验结果表明，我们的预训练模型表现出强大的零样本泛化能力。此外，使用我们的预训练模型和S2DKD策略进行特定领域的微调，可以显著提高领域性能。代码将很快提供。 et.al.|[2411.09151](http://arxiv.org/abs/2411.09151)|null|
|**2024-11-13**|**4D Gaussian Splatting in the Wild with Uncertainty-Aware Regularization**|动态场景的新颖视图合成在各种应用中变得越来越重要，包括增强现实和虚拟现实。我们提出了一种新的4D高斯散斑（4DGS）算法，用于随机记录的单眼视频中的动态场景。为了克服这些真实世界视频的现有工作的过拟合问题，我们引入了一种不确定性感知正则化，该正则化可以识别具有很少观测值的不确定区域，并基于扩散模型和深度平滑度在这些区域上选择性地施加额外的先验。该方法提高了新颖视图合成的性能和训练图像重建的质量。我们还发现了快速移动动态区域中4DGS的初始化问题，其中运动结构（SfM）算法无法提供可靠的3D地标。为了在这些区域中初始化高斯基元，我们提出了一种使用估计的深度图和场景流的动态区域致密化方法。我们的实验表明，所提出的方法提高了从手持单目相机捕获的视频中重建4DGS的性能，并且在少镜头静态场景重建中也显示出有前景的结果。 et.al.|[2411.08879](http://arxiv.org/abs/2411.08879)|null|
|**2024-11-13**|**BillBoard Splatting (BBSplat): Learnable Textured Primitives for Novel View Synthesis**|我们提出了一种基于纹理几何图元的3D场景表示新方法——广告牌飞溅（BBSplat）。BBSplat将场景表示为一组可优化的纹理平面图元，具有可学习的RGB纹理和阿尔法贴图来控制其形状。BBSplat基元可用于任何高斯Splatting管道中，作为高斯分布的插入式替换。当BBSplat达到1200 FPS以上时，当使用较少的基元时，我们的方法对3D和2D高斯的定性和定量改进最为明显。我们新颖的正则化项鼓励纹理具有更稀疏的结构，从而实现了高效的压缩，减少了模型的存储空间。我们的实验表明，BBSplat在真实室内和室外场景的标准数据集（如坦克和寺庙、DTU和Mip-NeRF-360）上的效率很高。与最新技术相比，我们展示了PSNR、SSIM和LPIPS指标的改进，特别是在使用较少基元的情况下，另一方面，在相同的渲染质量下，推理速度提高了2倍。 et.al.|[2411.08508](http://arxiv.org/abs/2411.08508)|null|
|**2024-11-13**|**DG-SLAM: Robust Dynamic Gaussian Splatting SLAM with Hybrid Pose Optimization**|在动态场景中实现鲁棒和精确的姿态估计是视觉同步定位和映射（SLAM）领域的一个重大研究挑战。最近将高斯散斑集成到SLAM系统中的进展已被证明在使用显式3D高斯模型创建高质量渲染方面是有效的，显著提高了环境重建的保真度。然而，这些方法依赖于静态环境假设，并且由于对几何和光度的不一致观测，在动态环境中面临挑战。为了解决这个问题，我们提出了DG-SLAM，这是第一个基于3D高斯的鲁棒动态视觉SLAM系统，它提供了精确的相机姿态估计和高保真重建。具体而言，我们提出了有效的策略，包括运动掩模生成、自适应高斯点管理和混合相机跟踪算法，以提高姿态估计的准确性和鲁棒性。大量实验表明，DG-SLAM在动态场景中的相机姿态估计、地图重建和新颖的视图合成方面具有最先进的性能，在保持实时渲染能力的同时优于现有方法。 et.al.|[2411.08373](http://arxiv.org/abs/2411.08373)|null|

<p align=right>(<a href=#updated-on-20241120>back to top</a>)</p>

## 3D Reconstruction

|Publish Date|Title|Abstract|PDF|Code|
|---|---|---|---|---|
|**2024-11-18**|**Towards Degradation-Robust Reconstruction in Generalizable NeRF**|跨场景的广义神经辐射场（GNeRF）已被证明是一种有效的方法，通过用源图像的深度图像特征表示场景来避免每场景优化。然而，尽管GNeRF具有现实应用的潜力，但关于其对源图像中存在的不同类型退化的鲁棒性的研究有限。缺乏此类研究的主要原因是缺乏适合训练退化鲁棒可推广NeRF模型的大规模数据集。为了解决这一差距并促进对3D重建任务退化鲁棒性的研究，我们构建了Objaverse模糊数据集，该数据集包含来自1000多个设置的50000张图像，具有多个级别的模糊退化。此外，我们设计了一个简单且与模型无关的模块，用于增强GNeRF的退化鲁棒性。具体而言，通过轻量级深度估计器和去噪器提取3D感知特征，所提出的模块在不同退化类型和水平下，在定量和视觉质量方面都比GNeRF中的不同流行方法有所改进。我们的数据集和代码将公开。 et.al.|[2411.11691](http://arxiv.org/abs/2411.11691)|null|
|**2024-11-18**|**VLN-Game: Vision-Language Equilibrium Search for Zero-Shot Semantic Navigation**|遵循人类指令在陌生环境中探索和搜索指定目标是移动服务机器人的一项关键技能。之前关于目标导航的大部分工作通常都集中在单一输入模态作为目标上，这可能会导致对包含详细属性和空间关系的语言描述的考虑有限。为了解决这一限制，我们提出了VLN-Game，这是一种新的用于视觉目标导航的零样本框架，可以有效地处理对象名称和描述性语言目标。更精确地说，我们的方法通过将预训练的视觉语言特征与物理环境的3D重建相结合，构建了一个以3D对象为中心的空间地图。然后，该框架确定了最有希望探索的领域，以寻找潜在的目标候选者。采用博弈论视觉语言模型来确定哪个目标与给定的语言描述最匹配。在Habitat Matterport 3D（HM3D）数据集上进行的实验表明，所提出的框架在目标导航和基于语言的导航任务中都达到了最先进的性能。此外，我们证明了VLN Game可以很容易地部署在现实世界的机器人上。VLN-Game的成功凸显了使用博弈论方法和紧凑的视觉语言模型来提高机器人系统决策能力的巨大潜力。可以通过以下链接访问补充视频和代码：https://sites.google.com/view/vln-game. et.al.|[2411.11609](http://arxiv.org/abs/2411.11609)|null|
|**2024-11-17**|**BVI-CR: A Multi-View Human Dataset for Volumetric Video Compression**|沉浸式技术和3D重建的进步使得能够创建具有精细细节的现实世界物体和环境的数字复制品。这些过程会生成大量的3D数据，需要更有效的压缩方法来满足与数据存储和传输相关的内存和带宽限制。然而，有效的3D数据压缩方法的开发和验证受到缺乏全面和高质量的体视频数据集的限制，与2D图像和视频数据库相比，这通常需要付出更多的努力来获取和消耗更多的资源。为了弥合这一差距，我们提出了一个开放的多视图体积人体数据集，称为BVI-CR，其中包含18个多视图RGB-D捕获及其相应的纹理多边形网格，描绘了一系列不同的人体动作。每个视频序列包含10个1080p分辨率的视图，持续时间为10-15秒，帧率为30FPS。使用BVI-CR，我们按照MPEG MIV通用测试条件，对三种传统的基于神经坐标的多视图视频压缩方法进行了基准测试，并根据各种质量指标报告了它们的速率质量性能。结果表明，与传统的视频编码方法相比，基于神经表示的方法在体视频压缩中具有巨大的潜力（PSNR平均编码增益高达38%）。该数据集为各种任务提供了一个开发和验证平台，包括体积重建、压缩和质量评估。数据库将在\url公开共享{https://github.com/fan-aaron-zhang/bvi-cr}. et.al.|[2411.11199](http://arxiv.org/abs/2411.11199)|null|
|**2024-11-16**|**ARM: Appearance Reconstruction Model for Relightable 3D Generation**|最近的图像到3D重建模型极大地改进了几何生成，但它们仍然难以忠实地生成逼真的外观。为了解决这个问题，我们引入了ARM，这是一种从稀疏视图图像重建高质量3D网格和逼真外观的新方法。ARM的核心在于将几何与外观解耦，在UV纹理空间内处理外观。与以前的方法不同，ARM通过明确地将测量值反向投影到纹理贴图上，并在具有全局感受野的UV空间模块中对其进行处理，从而提高了纹理质量。为了解决输入图像中材质和光照之间的歧义，ARM引入了一种材质先验，对语义外观信息进行编码，增强了外观分解的鲁棒性。仅在8个H100 GPU上训练，ARM在数量和质量上都优于现有方法。 et.al.|[2411.10825](http://arxiv.org/abs/2411.10825)|null|
|**2024-11-16**|**Poster: Reliable 3D Reconstruction for Ad-hoc Edge Implementations**|支持实时复杂视频处理应用程序（如多视图3D重建）的自组织边缘部署通常会受到时空系统中断的影响，这会极大地影响重建质量。在这篇海报论文中，我们提出了一种受投资组合理论启发的边缘资源管理策略，通过考虑可能的系统中断来确保可靠的多视图3D重建。 et.al.|[2411.10705](http://arxiv.org/abs/2411.10705)|null|
|**2024-11-15**|**The Oxford Spires Dataset: Benchmarking Large-Scale LiDAR-Visual Localisation, Reconstruction and Radiance Field Methods**|本文介绍了一个使用定制的多传感器感知单元在牛津著名地标及其周围捕获的大规模多模态数据集，以及来自陆地激光雷达扫描仪（TLS）的毫米级精确地图。感知单元包括三个同步的全局快门彩色相机、一个汽车3D激光雷达扫描仪和一个惯性传感器，所有这些都经过精确校准。我们还为涉及定位、重建和新颖视图合成的任务建立了基准，这些任务能够评估同步定位和映射（SLAM）方法、运动结构（SfM）和多视图立体（MVS）方法，以及神经辐射场（NeRF）和3D高斯散射等辐射场方法。为了评估3D重建，TLS 3D模型被用作地面实况。通过将移动LiDAR扫描注册到TLS 3D模型来计算本地化地面实况。辐射场方法不仅使用从输入轨迹采样的姿态进行评估，还使用来自远离训练姿态的轨迹的视点进行评估。我们的评估表明了最先进的辐射场方法的一个关键局限性：我们表明，它们往往对训练姿势/图像过拟合，并且不能很好地泛化到无序姿势。与使用相同视觉输入的MVS系统相比，它们在3D重建方面也表现不佳。我们的数据集和基准旨在促进辐射场方法和SLAM系统的更好集成。原始和处理后的数据，以及用于解析和评估的软件，可以在以下网址访问https://dynamic.robots.ox.ac.uk/datasets/oxford-spires/. et.al.|[2411.10546](http://arxiv.org/abs/2411.10546)|null|
|**2024-11-15**|**USP-Gaussian: Unifying Spike-based Image Reconstruction, Pose Correction and Gaussian Splatting**|Spike相机作为一种创新的神经形态相机，以40kHz的0-1比特流捕获场景，越来越多地通过神经辐射场（NeRF）或3D高斯散斑（3DGS）用于3D重建任务。以前基于尖峰的3D重建方法通常采用案例管道：从基于既定尖峰的尖峰流到图像重建算法的高质量图像重建开始，然后进行相机姿态估计和3D重建。然而，这种级联方法存在大量累积误差，其中初始图像重建的质量限制对姿态估计产生负面影响，最终降低了3D重建的保真度。为了解决这些问题，我们提出了一个协同优化框架\textbf{USP Gaussian}，该框架将基于尖峰的图像重建、姿态校正和高斯叠加统一到一个端到端的框架中。利用3DGS提供的多视图一致性和尖峰相机的运动捕捉能力，我们的框架实现了联合迭代优化，将尖峰到图像网络和3DGS之间的信息无缝集成。在具有精确姿态的合成数据集上的实验表明，我们的方法通过有效地消除级联误差，超越了以前的方法。此外，我们整合了姿态优化，以在初始姿态不准确的真实场景中实现鲁棒的3D重建，通过有效降低噪声和保留精细纹理细节，优于其他方法。我们的代码、数据和训练模型将在\url上提供{https://github.com/chenkang455/USP-Gaussian}. et.al.|[2411.10504](http://arxiv.org/abs/2411.10504)|**[link](https://github.com/chenkang455/usp-gaussian)**|
|**2024-11-14**|**MFP3D: Monocular Food Portion Estimation Leveraging 3D Point Clouds**|食物份量估计对于监测健康和跟踪饮食摄入至关重要。基于图像的饮食评估，包括使用计算机视觉技术分析饮食场合图像，正越来越多地取代传统方法，如24小时召回。然而，由于在投影到2D图像平面时丢失了3D信息，因此从图像中准确估计营养含量仍然具有挑战性。现有的部分估计方法由于依赖于特定要求，如物理参考对象、高质量深度信息或多视图图像和视频，在现实世界场景中部署具有挑战性。本文介绍了MFP3D，这是一种仅使用单眼图像进行精确食物份量估计的新框架。具体来说，MFP3D由三个关键模块组成：（1）3D重建模块，从2D图像中生成食物的3D点云表示；（2）特征提取模块，从3D点云和2D RGB图像中提取并连接特征；（3）部分回归模块，使用深度回归模型根据提取的特征估计食物的体积和能量含量。我们的MFP3D在MetaFood3D数据集上进行了评估，证明了它在准确估计部分方面比现有方法有了显著提高。 et.al.|[2411.10492](http://arxiv.org/abs/2411.10492)|null|
|**2024-11-15**|**Uncertainty-Weighted Mutual Distillation for Multi-View Fusion**|多视图学习在有效利用从不同角度和位置捕获的图像方面经常面临挑战。在解决观点之间的不一致和不确定性时，这一挑战尤为明显。本文提出了一种新的多视图不确定性加权互蒸馏（MV-UWMD）方法。我们的方法通过在所有可能的视图组合（包括单视图、部分多视图和完全多视图预测）中执行分层相互蒸馏来增强预测一致性。这通过相互蒸馏引入了一种基于不确定性的加权机制，允许有效利用来自每个视图的独特信息，同时减轻不确定预测的影响。我们扩展了CNN-Transformer混合架构，以促进跨多个视图组合的稳健特征学习和集成。我们使用从各种非固定视角捕获的大型非结构化数据集进行了广泛的实验。结果表明，与现有的多视图学习方法相比，MV-UWMD提高了预测的准确性和一致性。 et.al.|[2411.10077](http://arxiv.org/abs/2411.10077)|null|
|**2024-11-14**|**CropCraft: Inverse Procedural Modeling for 3D Reconstruction of Crop Plants**|从图像中自动构建植物的3D数字双胞胎的能力在农业、环境科学、机器人技术和其他领域有着无数的应用。然而，由于严重的遮挡和复杂的几何形状，目前的3D重建方法无法恢复植物的完整形状。在这项工作中，我们提出了一种基于逆过程建模优化植物形态参数模型的农作物三维重建新方法。我们的方法首先通过拟合神经辐射场来估计深度图，然后采用贝叶斯优化来估计植物形态参数，从而得到一致的深度渲染。由此产生的3D模型是完整的，在生物学上是合理的。我们在农田真实图像的数据集上验证了我们的方法，并证明了重建可用于各种监测和模拟应用。 et.al.|[2411.09693](http://arxiv.org/abs/2411.09693)|null|

<p align=right>(<a href=#updated-on-20241120>back to top</a>)</p>

## Diffusion

|Publish Date|Title|Abstract|PDF|Code|
|---|---|---|---|---|
|**2024-11-18**|**Equivariant spatio-hemispherical networks for diffusion MRI deconvolution**|扩散MRI（dMRI）图像中的每个体素都包含一个与大脑中水扩散的方向和强度相对应的球形信号。本文通过开发与 $\mathbf{E（3）\times SO（3）}$ 群等价的卷积网络层，并考虑dMRI的物理对称性，包括旋转、平移和空间反射以及体素旋转，推进了对这种空间球面数据的分析。此外，神经元纤维通常是对映对称的，我们利用这一事实构建高效的空间半球图卷积，以加速高维dMRI数据的分析。在稀疏球形纤维反卷积以恢复白质微观结构的背景下，我们提出的等变网络层产生了实质性的性能和效率提升，从而为交叉神经元纤维和纤维束成像提供了更好、更实用的分辨率。这些增益在模拟和体内人体数据集中都是实验一致的。 et.al.|[2411.11819](http://arxiv.org/abs/2411.11819)|**[link](https://github.com/axelelaldi/fast-equivariant-deconv)**|
|**2024-11-18**|**Fabrication of Hierarchical Sapphire Nanostructures using Ultrafast Laser Induced Morphology Change**|蓝宝石在光子、光电子和透明陶瓷应用中是一种有吸引力的材料，可以从微/纳米结构的表面功能化效应中受益。在这里，我们通过探索辐照参数、形态变化和选择性蚀刻之间的关系，研究了使用超快激光在蓝宝石中制造纳米结构。在这种方法中，超快激光脉冲聚焦在蓝宝石基板上，将晶体形态改变为非晶或多晶，其特征是使用拉曼光谱检查不同的振动模式。然后使用氢氟酸中的后续湿法蚀刻去除照射区域。蚀刻过程前后进行的激光共焦测量量化了选择性蚀刻的程度。结果表明，发生选择性蚀刻需要阈值激光脉冲强度。该工艺可用于在大面积上制备具有增强疏水性的分级蓝宝石纳米结构，其表现出140度的表观接触角和高滚转角，这是玫瑰花瓣效应的特征。此外，所制备的结构具有高达81.8%的宽带漫透射率和低损耗，可用于光学漫射器。我们的发现为光-物质相互作用之间的相互作用提供了新的见解，其中与不同振动模式相关的拉曼位移可以用作选择性蚀刻的预测指标。这些结果推动了蓝宝石纳米结构制造的发展，可以在红外光学、防护窗和消费电子产品中得到应用。 et.al.|[2411.11817](http://arxiv.org/abs/2411.11817)|null|
|**2024-11-18**|**Open Catalyst Experiments 2024 (OCx24): Bridging Experiments and Computational Models**|寻找低成本、耐用和有效的催化剂对于绿色氢气生产和二氧化碳升级回收至关重要，有助于缓解气候变化。目前，新催化剂的发现受到人工智能加速计算模型预测与实验研究结果之间差距的限制。为了取得进展，需要大规模和多样化的实验数据集，这些数据集是可重复的，并在工业相关条件下进行测试。我们通过利用全面的高通量表征和实验管道来创建Open Catalyst Experiments 2024（OCX24）数据集，以满足这些需求。该数据集包含572个使用湿法和干法合成的样品，具有X射线荧光和X射线衍射特征。我们制备了441个气体扩散电极，包括复制品，并使用零间隙电解在高达300 $mA/cm^2$的电流密度下对其进行了二氧化碳还原（CO$_2$ RR）和析氢反应（HER）的评估。为了找到与实验结果的相关性并进行计算筛选，在需要6.85亿AI加速弛豫的20000美元无机材料上计算了六种吸附质的DFT验证吸附能。值得注意的是，从这一大组材料中，一座数据驱动的萨巴蒂尔火山独立地将Pt确定为HER的首选，而没有对Pt或Pt合金样品进行任何实验测量。我们预计，专门为人工智能训练生成的实验数据（如OCX24）的可用性将显著提高计算模型在选择实验筛选材料方面的实用性。 et.al.|[2411.11783](http://arxiv.org/abs/2411.11783)|null|
|**2024-11-18**|**Milstein-type schemes for McKean-Vlasov SDEs driven by Brownian motion and Poisson random measure (with super-linear coefficients)**|在这项工作中，我们提出了一个通用的Milstein型方案，用于求解由布朗运动和泊松随机测度驱动的McKean-Vlasov随机微分方程（SDEs）以及相关的相互作用粒子系统，其中漂移、扩散和跳跃系数可以在状态变量中超线性增长，在测度分量中线性增长。在系数的适当正则性假设下，所提出的方案的强数学{L}^2$-收敛率被证明任意接近1。为了推导Milstein格式并展示其强收敛速度，我们提供了一个与布朗运动和泊松随机测度驱动的McKean-Vlasov SDE相关的相互作用粒子系统的Ito公式。此外，我们使用狮子导数的概念来检验我们的结果。通过识别和利用适当的矫顽力类型条件，解决了由于经验测量和跳跃系数的超线性而产生的双重挑战。 et.al.|[2411.11759](http://arxiv.org/abs/2411.11759)|null|
|**2024-11-18**|**Correlated emission lasing in a single quantum dot embedded inside a bimodal photonic crystal cavity**|我们利用主方程描述系统动力学，研究了耦合到双模光子晶体腔的相干驱动单量子点中的相关发射激光现象。为了解释激子-声子相互作用，我们通过极化子变换的主方程引入了非微扰方法。通过分析与相对和平均相位相关的厄米算子的波动，我们推导出了福克-普朗克方程来评估相位漂移和扩散系数，证明了在低温下存在激子-声子相互作用的情况下，相关发射抑制了量子噪声。此外，我们计算了进入腔模的单光子和双光子过量发射率（发射率和吸收率之间的差异），并探索了这些模之间连续可变纠缠的产生。 et.al.|[2411.11744](http://arxiv.org/abs/2411.11744)|null|
|**2024-11-18**|**Aligning Few-Step Diffusion Models with Dense Reward Difference Learning**|将扩散模型与下游目标对齐对于其实际应用至关重要。然而，当直接应用于少步扩散模型时，标准对齐方法往往难以实现步泛化，导致不同去噪步骤场景的性能不一致。为了解决这个问题，我们引入了逐步扩散策略优化（SDPO），这是一种为少步扩散模型量身定制的新型对齐方法。与之前仅依赖于每个去噪轨迹最后一步的单个稀疏奖励进行轨迹级优化的方法不同，SDPO在每个中间步骤都包含了密集的奖励反馈。通过学习成对样本之间密集奖励的差异，SDPO有助于逐步优化几步扩散模型，确保所有去噪步骤的一致对齐。为了促进稳定高效的训练，SDPO引入了一个在线强化学习框架，该框架采用了几种新颖的策略，旨在有效地利用密集奖励的逐步粒度。实验结果表明，SDPO在跨不同步长配置的基于奖励的对齐方面始终优于现有方法，突显了其强大的步长泛化能力。代码可在以下网址获得https://github.com/ZiyiZhang27/sdpo. et.al.|[2411.11727](http://arxiv.org/abs/2411.11727)|**[link](https://github.com/ziyizhang27/sdpo)**|
|**2024-11-18**|**Robust Reinforcement Learning under Diffusion Models for Data with Jumps**|强化学习（RL）已被证明在解决各种领域的复杂决策任务方面是有效的，但在连续时间设置中仍然存在挑战，特别是当状态动力学由具有跳跃分量的随机微分方程（SDE）控制时。在本文中，我们通过引入均方双功率变化误差（MSBVE）算法来解决这一挑战，该算法在涉及显著随机噪声和跳跃的情况下增强了鲁棒性和收敛性。我们首先重新审视了连续时间RL中常用的均方TD误差（MSTDE）算法，并强调了它在处理状态动力学跳跃方面的局限性。所提出的MSBVE算法最小化了均方二次变化误差，在具有跳跃的SDE特征的环境中提供了优于MSTDE的性能。仿真和形式化证明表明，MSBVE算法在复杂环境中可靠地估计了值函数，在面对跳跃过程时超过了MSTDE的性能。这些发现强调了替代错误度量对于提高连续时间框架中RL算法的弹性和有效性的重要性。 et.al.|[2411.11697](http://arxiv.org/abs/2411.11697)|null|
|**2024-11-18**|**Active droplets controlled by enzymatic reactions**|冷凝物的形成现在被认为是真核细胞的主要组织原理。最近的几项研究表明，这些冷凝物的性质受到酶反应的影响。我们在这里提出了一个简单的通用模型来研究两个酶群和一个双态蛋白质之间的相互作用。在一种状态下，蛋白质通过吸引的相互作用形成凝聚的液滴，而在另一种状态中，蛋白质保持分散。每种酶只有在反应物在其附近时才会催化这两种蛋白质状态之一的产生。我们模型的一个关键特征是酶轨迹的显式表示，捕捉其局部浓度的波动。液滴的空间依赖性生长速率自然源于这些明确建模的酶的随机运动。使用两种互补的数值方法，（1）布朗动力学模拟，以及（2）将Cahn-Hilliard-Cook扩散方程与酶的布朗动力学相结合的混合方法，我们研究了酶浓度和动力学如何影响随时间的演变，以及液滴的稳态数量和大小。我们的结果表明，酶的浓度和扩散系数控制着生物冷凝物的形成和大小选择。 et.al.|[2411.11696](http://arxiv.org/abs/2411.11696)|null|
|**2024-11-18**|**Hamiltonian Monte Carlo vs. event-chain Monte Carlo: an appraisal of sampling strategies beyond the diffusive regime**|我们讨论了具有调和相互作用的一维粒子链的哈密顿蒙特卡罗（HMC）和事件链蒙特卡罗（ECMC），并将其与局部可逆Metropolis算法进行了比较。虽然HMC相对于局部可逆蒙特卡洛算法实现了相当大的加速，但其全局可观测值的自相关函数（如结构因子）随系统大小的缩放速度比ECMC（一种提升的不可逆马尔可夫链）慢。这可以追溯到ECMC对谐波能量参数（平衡距离）的依赖性，当评估能量差或梯度时，平衡距离会下降。我们回顾了最近的文献，并提供了伪代码和Python程序。最后，我们讨论了一维粒子系统之外的相关模型和推广。 et.al.|[2411.11690](http://arxiv.org/abs/2411.11690)|null|
|**2024-11-18**|**Conceptwm: A Diffusion Model Watermark for Concept Protection**|扩散模型的个性化技术成功地生成了特定的概念，但也对版权保护和非法使用构成了威胁。模型水印是一种有效的方法，可以防止未经授权使用主题驱动或风格驱动的图像生成，保护概念版权。然而，在面向概念的保护目标下，当前的水印方案通常会向所有图像添加水印，而不是以针对特定概念的精细方式应用它们。此外，扩散模型的个性化技术可以很容易地去除水印。现有的水印方法难以通过少量特定概念的图像实现细粒度的水印嵌入，并通过个性化微调来防止水印的去除。因此，我们引入了一种新的面向概念的水印框架，该框架将不可察觉的水印无缝地嵌入到扩散模型的概念中。我们进行了广泛的实验和消融研究来验证我们的框架。我们的代码可在https://anonymous.4open.science/r/Conceptwm-4EB3/. et.al.|[2411.11688](http://arxiv.org/abs/2411.11688)|null|

<p align=right>(<a href=#updated-on-20241120>back to top</a>)</p>

## NeRF

|Publish Date|Title|Abstract|PDF|Code|
|---|---|---|---|---|
|**2024-11-14**|**The Hydrodynamic Limit of Hawkes Processes on Adaptive Stochastic Networks**|我们确定了自适应网络上相互作用的霍克斯过程网络的大尺寸限制。节点变量的翻转被认为具有由传入边缘和节点的平均场给出的强度。边缘变量的翻转是传入节点变量的函数。边变量可以是对称的，也可以是不对称的。该模型受到社会学、神经科学和流行病学应用的启发。一般来说，极限概率律可以表示为具有强度函数的自洽泊松过程的不动点，该强度函数（i）是延迟的，（ii）取决于其自身的概率律。在边缘翻转仅由突触前神经元的状态决定的特定情况下（如神经科学中），证明了可以获得突触增强和神经增强双重进化的自主神经场型方程。 et.al.|[2411.09260](http://arxiv.org/abs/2411.09260)|null|
|**2024-11-09**|**Epi-NAF: Enhancing Neural Attenuation Fields for Limited-Angle CT with Epipolar Consistency Conditions**|神经场方法最初在逆渲染领域取得了成功，最近已扩展到CT重建，标志着传统技术的范式转变。虽然这些方法在稀疏视图CT重建中提供了最先进的结果，但它们在有限的角度设置中很难实现，在有限的视角范围内捕获输入投影。我们提出了一种基于X射线投影图像中相应极线之间一致性条件的新损失项，旨在规范神经衰减场优化。通过强制执行这些一致性条件，我们的方法Epi NAF将监督从有限角度范围内的输入视图传播到整个锥束CT范围内的预测投影。与基线方法相比，这种损失导致重建的定性和定量改进。 et.al.|[2411.06181](http://arxiv.org/abs/2411.06181)|null|
|**2024-11-07**|**LoFi: Scalable Local Image Reconstruction with Implicit Neural Representation**|神经场或隐式神经表示（INR）因其对图像和3D体积的有效连续表示而在机器学习和信号处理中引起了广泛关注。在这项工作中，我们以INR为基础，引入了一种基于坐标的局部处理框架来解决成像逆问题，称为LoFi（局部场）。与传统的图像重建方法不同，LoFi通过多层感知器（MLP）分别处理每个坐标处的局部信息，在该特定坐标处恢复对象。与INR类似，LoFi可以在任何连续坐标下恢复图像，从而实现多分辨率的图像重建。LoFi在图像重建方面的性能与标准CNN相当或更好，几乎与图像分辨率无关，对分布外数据和内存使用具有出色的泛化能力。值得注意的是，对1024美元×1024美元的图像进行训练只需要3GB的内存，比标准CNN通常需要的内存少20多倍。此外，LoFi的局部设计使其能够在小于10个样本的极小数据集上进行训练，而不会过拟合或需要正则化或提前停止。最后，我们使用LoFi作为即插即用框架中的去噪先验，用于解决一般的逆问题，以受益于其连续的图像表示和强大的泛化能力。尽管在低分辨率图像上进行了训练，但LoFi可以用作低维先验，以解决任何分辨率的逆问题。我们通过各种成像方式验证了我们的框架，从低剂量计算机断层扫描到无线电干涉成像。 et.al.|[2411.04995](http://arxiv.org/abs/2411.04995)|null|
|**2024-11-04**|**Physically Based Neural Bidirectional Reflectance Distribution Function**|我们介绍了基于物理的神经双向反射分布函数（PBNBRDF），这是一种基于神经场的材料外观的新颖连续表示。我们的模型准确地重建了真实世界的材料，同时独特地增强了现实BRDF的物理特性，特别是通过重新参数化的亥姆霍兹互易性和通过高效分析积分的能量无源性。我们进行了系统分析，证明了遵守这些物理定律对重建材料的视觉质量的好处。此外，我们通过引入色度强制监督RGB通道的规范来提高神经BRDF的颜色精度。通过在多个测量的真实BRDF数据库上进行定性和定量实验，我们表明，遵守这些物理约束可以使神经场更忠实、更稳定地表示原始数据，并实现更高的渲染质量。 et.al.|[2411.02347](http://arxiv.org/abs/2411.02347)|null|
|**2024-11-01**|**Intensity Field Decomposition for Tissue-Guided Neural Tomography**|锥束计算机断层扫描（CBCT）通常需要数百次X射线投影，这引起了人们对辐射暴露的担忧。虽然稀疏视图重建通过使用更少的投影来减少曝光，但它很难达到令人满意的图像质量。为了应对这一挑战，本文介绍了一种新的稀疏视图CBCT重建方法，该方法为神经场赋予了人体组织正则化的能力。我们的方法被称为组织引导神经断层扫描（TNT），其动机是CBCT中骨骼和软组织之间明显的强度差异。直观地说，分离这些成分可能有助于神经场的学习过程。更确切地说，TNT包括一个异构的四重网络和相应的训练策略。该网络将强度场表示为软组织和硬组织成分及其各自纹理的组合。我们在估计的组织投影的指导下训练网络，从而能够有效地学习网络头所需的模式。大量实验表明，所提出的方法显著改善了稀疏视图CBCT重建，投影数量从10到60不等。与最先进的基于神经渲染的方法相比，我们的方法以更少的投影和更快的收敛实现了相当的重建质量。 et.al.|[2411.00900](http://arxiv.org/abs/2411.00900)|null|
|**2024-10-26**|**Neural Fields in Robotics: A Survey**|神经场已经成为计算机视觉和机器人技术中3D场景表示的一种变革性方法，能够从姿势的2D数据中准确推断几何、3D语义和动力学。利用可微分渲染，神经场包括连续隐式和显式神经表示，实现了高保真3D重建、多模态传感器数据的集成和新视点的生成。这项调查探讨了它们在机器人技术中的应用，强调了它们在增强感知、规划和控制方面的潜力。它们的紧凑性、内存效率和可微性，以及与基础模型和生成模型的无缝集成，使其成为实时应用的理想选择，提高了机器人的适应性和决策能力。本文基于200多篇论文，对机器人中的神经场进行了全面的回顾，对各个领域的应用进行了分类，并评估了它们的优势和局限性。首先，我们介绍了四个关键的神经场框架：占用网络、有符号距离场、神经辐射场和高斯散斑。其次，我们详细介绍了神经场在五个主要机器人领域的应用：姿态估计、操纵、导航、物理和自动驾驶，重点介绍了关键工作，并讨论了要点和公开挑战。最后，我们概述了神经场在机器人技术中的局限性，并为未来的研究提出了有前景的方向。项目页面：https://robonerf.github.io et.al.|[2410.20220](http://arxiv.org/abs/2410.20220)|**[link](https://github.com/zubair-irshad/Awesome-Implicit-NeRF-Robotics)**|
|**2024-10-24**|**3D-Adapter: Geometry-Consistent Multi-View Diffusion for High-Quality 3D Generation**|多视图图像扩散模型显著推进了开放域3D对象生成。然而，大多数现有模型依赖于缺乏固有3D偏差的2D网络架构，导致几何一致性受损。为了应对这一挑战，我们引入了3D Adapter，这是一个插件模块，旨在将3D几何感知注入预训练的图像扩散模型中。我们方法的核心是3D反馈增强的思想：对于采样循环中的每个去噪步骤，3D Adapter将中间的多视图特征解码为连贯的3D表示，然后对渲染的RGBD视图进行重新编码，通过特征添加来增强预训练的基础模型。我们研究了3D Adapter的两种变体：一种是基于高斯飞溅的快速前馈版本，另一种是利用神经场和网格的通用无训练版本。我们广泛的实验表明，3D Adapter不仅大大提高了文本到多视图模型（如Instant3D和Zero123++）的几何质量，而且还使用纯文本到图像的稳定扩散实现了高质量的3D生成。此外，我们通过在文本到3D、图像到3D、文本到纹理和文本到化身任务中呈现高质量的结果，展示了3D适配器的广泛应用潜力。 et.al.|[2410.18974](http://arxiv.org/abs/2410.18974)|**[link](https://github.com/Lakonik/MVEdit)**|
|**2024-10-22**|**Cortical Dynamics of Neural-Connectivity Fields**|皮质组织的宏观研究揭示了振荡活动的普遍性，这反映了神经相互作用的微调。本研究通过将广义振荡动力学纳入先前关于保守或半保守神经场动力学的工作中，扩展了神经场理论。先前的研究在很大程度上假设了神经单元之间的各向同性连接；然而，这项研究表明，广泛的各向异性和波动连接仍然可以维持振荡。使用拉格朗日场方法，我们研究了不同类型的连接、它们的动力学以及与神经场的潜在相互作用。基于这一理论基础，我们推导出了一个框架，该框架通过连接场的概念将Hebbian和非Hebbian学习（即可塑性）纳入神经场的研究中。 et.al.|[2410.16852](http://arxiv.org/abs/2410.16852)|null|
|**2024-10-15**|**Deep vectorised operators for pulsatile hemodynamics estimation in coronary arteries from a steady-state prior**|心血管血流动力学场为冠状动脉疾病提供了有价值的医学决策标志。计算流体动力学（CFD）是体内准确、无创评估这些量的金标准。在这项工作中，我们提出了一种基于机器学习的时间高效替代模型，用于基于稳态先验估计脉动血流动力学。我们引入了深度矢量化算子，这是一种用于在无限维函数空间上进行离散化独立学习的建模框架。基础神经结构是一个以血流动力学边界条件为条件的神经场。重要的是，我们展示了如何将逐点动作的要求放宽到置换等变，从而产生一系列可以通过消息传递和自我关注层进行参数化的模型。我们在从冠状动脉计算机断层扫描血管造影（CCTA）中提取的74条狭窄冠状动脉的数据集上评估了我们的方法，并将患者特异性脉动CFD模拟作为基本事实。我们证明，我们的模型能够准确估计脉动速度和压力，同时不受源域重新采样的影响（离散化独立性）。这表明，深度矢量化算子是冠状动脉及其他动脉心血管血流动力学估计的强大建模工具。 et.al.|[2410.11920](http://arxiv.org/abs/2410.11920)|null|
|**2024-10-07**|**Fast Training of Sinusoidal Neural Fields via Scaling Initialization**|神经场是一种新兴的范式，它将数据表示为由神经网络参数化的连续函数。尽管有许多优点，但神经场通常具有较高的训练成本，这阻碍了更广泛的采用。在本文中，我们关注一个流行的神经场家族，称为正弦神经场（SNF），并研究如何初始化它以最大限度地提高训练速度。我们发现，基于信号传播原理设计的SNF标准初始化方案是次优的。特别是，我们证明，通过简单地将每个权重（最后一层除外）乘以一个常数，我们可以将SNF训练加速10 $\times$。这种方法被称为$\textit{weight scaling}$ ，在各种数据域上持续提供显著的加速，使SNF的训练速度比最近提出的架构更快。为了理解为什么权重缩放效果良好，我们进行了广泛的理论和实证分析，结果表明，权重缩放不仅有效地解决了频谱偏差，而且具有良好的优化轨迹。 et.al.|[2410.04779](http://arxiv.org/abs/2410.04779)|null|

<p align=right>(<a href=#updated-on-20241120>back to top</a>)</p>

[contributors-shield]: https://img.shields.io/github/contributors/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[contributors-url]: https://github.com/Vincentqyw/cv-arxiv-daily/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[forks-url]: https://github.com/Vincentqyw/cv-arxiv-daily/network/members
[stars-shield]: https://img.shields.io/github/stars/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[stars-url]: https://github.com/Vincentqyw/cv-arxiv-daily/stargazers
[issues-shield]: https://img.shields.io/github/issues/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[issues-url]: https://github.com/Vincentqyw/cv-arxiv-daily/issues

