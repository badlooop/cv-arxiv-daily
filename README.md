[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]

## Updated on 2024.03.25
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
|**2024-03-22**|**WSCLoc: Weakly-Supervised Sparse-View Camera Relocalization**|尽管在相机重新定位任务的深度学习方面取得了进展，但获得训练过程所需的真实姿势标签仍然是一项代价高昂的工作。虽然当前的弱监督方法在轻量级标签生成方面表现出色，但在具有稀疏视图的场景中，它们的性能显著下降。为了应对这一挑战，我们引入了WSCLoc，这是一个能够针对各种基于深度学习的重定位模型进行定制的系统，以增强其在弱监督和稀疏视图条件下的性能。这分两个阶段实现。在初始阶段，WSCLoc使用一种称为WFT-NeRF的基于多层感知器的结构来共同优化图像重建质量和初始姿态信息。为了确保稳定的学习过程，我们将时间信息作为输入。此外，我们不优化SE（3），而是选择 $\mathfrak｛sim｝（3）$ 优化来显式地实施规模约束。在第二阶段，我们对预先训练的WFT-NeRF和WFT-Pose进行了联合优化。这种优化通过基于时间编码的随机视图合成来增强，并通过考虑姿态、深度和RGB信息的帧间几何约束来监督。我们在两个公开可用的数据集（一个室外数据集和一个室内数据集）上验证了我们的方法。我们的实验结果表明，与最先进的相机重定位方法相比，我们的弱监督重定位解决方案在稀疏视图场景中实现了卓越的姿态估计精度。我们将公开我们的代码。 et.al.|[2403.15272](http://arxiv.org/abs/2403.15272)|null|
|**2024-03-21**|**HAC: Hash-grid Assisted Context for 3D Gaussian Splatting Compression**|三维高斯散射（3DGS）以其快速、高保真的渲染速度成为一种很有前途的新型视图合成框架。然而，大量的高斯及其相关属性需要有效的压缩技术。然而，高斯点云（或我们论文中的锚点）的稀疏和无组织性质给压缩带来了挑战。为了解决这一问题，我们利用无组织锚和结构化哈希网格之间的关系，利用它们的相互信息进行上下文建模，并提出了一种用于高度紧凑的3DGS表示的哈希网格辅助上下文（HAC）框架。我们的方法引入了一个二进制哈希网格来建立连续的空间一致性，使我们能够通过精心设计的上下文模型揭示锚点的固有空间关系。为了便于熵编码，我们利用高斯分布来准确估计每个量化属性的概率，其中提出了自适应量化模块来实现这些属性的高精度量化，以提高保真度恢复。此外，我们结合了一种自适应掩蔽策略来消除无效的高斯和锚点。重要的是，我们的工作是探索3DGS表示基于上下文的压缩的先驱，与普通3DGS相比，其尺寸显著减少了75美元，同时提高了保真度，并与SOTA 3DGS压缩方法Scaffold GS相比，尺寸减少了11美元。我们的代码如下：https://github.com/YihangChen-ee/HAC et.al.|[2403.14530](http://arxiv.org/abs/2403.14530)|**[link](https://github.com/yihangchen-ee/hac)**|
|**2024-03-21**|**CombiNeRF: A Combination of Regularization Techniques for Few-Shot Neural Radiance Field View Synthesis**|当有足够多的视图可用时，神经辐射场（NeRF）在新的视图合成中显示出令人印象深刻的结果。当处理少量镜头设置时，即使用一小组输入视图时，训练可能会过度拟合这些视图，导致生成的渲染中出现伪影以及几何和颜色不一致。正则化是一种有效的解决方案，有助于NeRF的泛化。另一方面，每一种最新的NeRF正则化技术都旨在缓解特定的渲染问题。从这一观察出发，在本文中，我们提出了CombiNeRF，这是一个协同结合了几种正则化技术的框架，其中一些是新颖的，以统一每种技术的优点。特别地，我们正则化单个和相邻射线分布，并添加平滑项来正则化近几何体。在这些几何方法之后，我们建议将Lipschitz正则化应用于NeRF密度和颜色网络，并使用编码掩码进行输入特征正则化。我们展示了CombiNeRF在几个公开可用的数据集中以较少的镜头设置优于最先进的方法。我们还对LLFF和NeRF合成数据集进行了消融研究，以支持所做的选择。我们在本文中发布了我们框架的开源实现。 et.al.|[2403.14412](http://arxiv.org/abs/2403.14412)|**[link](https://github.com/sarroccoluigi/combinerf)**|
|**2024-03-21**|**Zero123-6D: Zero-shot Novel View Synthesis for RGB Category-level 6D Pose Estimation**|通过视觉估计物体的姿态对于使机器人平台与环境交互至关重要。然而，它带来了许多挑战，往往与最先进的解决方案缺乏灵活性和可推广性有关。扩散模型是一种转换二维和三维计算机视觉的前沿神经结构，概述了零样本新颖视图合成的显著性能。这样的用例对于重建3D对象来说特别有趣。然而，在非结构化环境中定位对象是相当未被探索的。为此，这项工作提出了Zero123-6D，以展示基于扩散模型的新型视图合成器在通过将其与特征提取技术集成来增强类别级别的RGB 6D姿态估计方面的实用性。所概述的方法利用这种新颖的视图合成器来扩展用于零样本6D姿态估计任务的仅RGB参考视图的稀疏集合。在CO3D数据集上对实验进行了定量分析，显示出与基线相比性能有所提高，数据需求大幅减少，并消除了深度信息的必要性。 et.al.|[2403.14279](http://arxiv.org/abs/2403.14279)|null|
|**2024-03-21**|**Isotropic Gaussian Splatting for Real-Time Radiance Field Rendering**|三维高斯飞溅方法由于其在训练中的高性能和渲染图像的高质量而引起了人们的广泛关注。但是，它使用各向异性高斯核来表示场景。尽管这种各向异性核在表示几何体方面具有优势，但它们在计算方面导致困难，例如分裂或合并两个核。在本文中，我们建议使用各向同性高斯核来避免计算中的这些困难，从而获得更高性能的方法。实验证实，所提出的方法在不损失几何表示精度的情况下大约快100X。所提出的方法可以应用于需要辐射场的大范围应用，如三维重建、视图合成和动态对象建模。 et.al.|[2403.14244](http://arxiv.org/abs/2403.14244)|null|
|**2024-03-21**|**Leveraging Thermal Modality to Enhance Reconstruction in Low-Light Conditions**|神经辐射场（NeRF）通过从多视图图像中学习场景的隐式体积表示来实现照片逼真的新视图合成，从而忠实地传达色度信息。然而，传感器噪声将污染低值像素信号，并且有损相机图像信号处理器将在极暗的情况下进一步去除接近零的强度，从而恶化合成性能。现有的方法从原始图像重建低光场景，但难以恢复暗区域中的纹理和边界细节。此外，它们不适用于依赖显式表示的高速模型。为了解决这些问题，我们提出了Thermal NeRF，它将热和可见原始图像作为输入，考虑到热相机对照明变化是鲁棒的，并且原始图像在黑暗中保留了任何可能的线索，以同时完成可见和热视图合成。此外，建立了第一个多视图热可见光数据集（MVTV），以支持多模式NeRF的研究。Thermal NeRF实现了细节保留和噪声平滑之间的最佳折衷，并提供了比以前更好的合成性能。最后，我们证明了这两种模式在3D重建中是有益的。 et.al.|[2403.14053](http://arxiv.org/abs/2403.14053)|null|
|**2024-03-20**|**RadSplat: Radiance Field-Informed Gaussian Splatting for Robust Real-Time Rendering with 900+ FPS**|视图合成和实时渲染的最新进展以令人印象深刻的渲染速度实现了照片级的真实感。虽然基于辐射场的方法在具有挑战性的场景（如野外捕捉和大规模场景）中实现了最先进的质量，但它们通常会受到与体积渲染相关的过高计算要求的影响。另一方面，基于高斯散射的方法依赖于光栅化，自然实现实时渲染，但在更具挑战性的环境中，其优化启发式效果较差。在这项工作中，我们提出了RadSplat，这是一种用于复杂场景的鲁棒实时渲染的轻量级方法。我们的主要贡献有三方面。首先，我们使用辐射场作为先验信号和监督信号来优化基于点的场景表示，从而提高质量和更稳健的优化。接下来，我们开发了一种新的修剪技术，在保持高质量的同时减少总点数，从而以更快的推理速度实现更小、更紧凑的场景表示。最后，我们提出了一种新的测试时间过滤方法，该方法可以进一步加速渲染，并允许缩放到更大的房屋大小的场景。我们发现，我们的方法能够以900+FPS的速度合成最先进的复杂捕获。 et.al.|[2403.13806](http://arxiv.org/abs/2403.13806)|null|
|**2024-03-20**|**Learning Novel View Synthesis from Heterogeneous Low-light Captures**|神经辐射场在从固定正常照明下捕获的具有相同亮度水平的输入视图合成新视图方面取得了基本成功。不幸的是，对于在弱光条件下捕获的具有异质亮度水平的输入视图来说，合成新视图仍然是一个挑战。这种情况在现实世界中很常见。它会导致低对比度图像，其中细节被隐藏在黑暗中，相机传感器噪声会显著降低图像质量。为了解决这个问题，我们建议学习根据反射率在异构视图中保持不变来分解输入视图中的照明、反射率和噪声。为了应对多视图之间的异质亮度和噪声水平，我们学习了照明嵌入，并为每个视图单独优化噪声图。为了能够直观地编辑照明，我们设计了一个照明调整模块，以使照明组件变亮或变暗。综合实验表明，与最先进的方法相比，该方法能够对弱光多视图噪声图像进行有效的内在分解，并在合成新视图方面实现了卓越的视觉质量和数值性能。 et.al.|[2403.13337](http://arxiv.org/abs/2403.13337)|null|
|**2024-03-20**|**Gaussian Splatting on the Move: Blur and Rolling Shutter Compensation for Natural Camera Motion**|基于高斯散射（3DGS）的高质量场景重建和新颖的视图合成通常需要稳定、高质量的照片，而手持相机通常无法捕捉到这些照片。我们提出了一种适应相机运动的方法，并允许使用遭受运动模糊和滚动快门失真的手持视频数据进行高质量的场景重建。我们的方法基于物理图像形成过程的详细建模，并利用视觉惯性里程计（VIO）估计的速度。在单个图像帧的曝光时间期间，摄像机姿态被认为是非静态的，并且在重建过程中进一步优化摄像机姿态。我们制定了一个可微分的渲染管道，利用屏幕空间近似将滚动快门和运动模糊效果有效地结合到3DGS框架中。我们对合成和真实数据的结果表明，与现有方法相比，我们在减轻相机运动方面表现出了卓越的性能，从而在自然环境中推进了3DGS。 et.al.|[2403.13327](http://arxiv.org/abs/2403.13327)|**[link](https://github.com/spectacularai/3dgs-deblur)**|
|**2024-03-19**|**HUGS: Holistic Urban 3D Scene Understanding via Gaussian Splatting**|基于RGB图像对城市场景的整体理解是一个具有挑战性但又很重要的问题。它包括理解几何图形和外观，以实现新颖的视图合成、解析语义标签和跟踪移动对象。尽管取得了相当大的进展，但现有的方法往往侧重于这项任务的特定方面，并需要额外的输入，如激光雷达扫描或手动注释的3D边界框。在本文中，我们介绍了一种新的管道，该管道利用3D高斯散射进行整体城市场景理解。我们的主要想法涉及使用静态和动态3D高斯的组合对几何、外观、语义和运动进行联合优化，其中运动对象姿态通过物理约束进行正则化。我们的方法提供了实时渲染新视点的能力，以高精度生成2D和3D语义信息，并重建动态场景，即使在3D边界框检测具有高噪声的场景中也是如此。在KITTI、KITTI-360和Virtual KITTI 2上的实验结果证明了我们方法的有效性。 et.al.|[2403.12722](http://arxiv.org/abs/2403.12722)|null|

<p align=right>(<a href=#updated-on-20240325>back to top</a>)</p>

## 3D Reconstruction

|Publish Date|Title|Abstract|PDF|Code|
|---|---|---|---|---|
|**2024-03-22**|**FastCAD: Real-Time CAD Retrieval and Alignment from Scans and Videos**|将3D世界数字化为一个干净的、基于CAD模型的表示在增强现实和机器人技术中有着重要的应用。当前最先进的方法是计算密集型的，因为它们分别对每个检测到的对象进行编码，并在第二阶段优化CAD对齐。在这项工作中，我们提出了FastCAD，这是一种实时方法，可以同时检索和对齐给定场景中所有对象的CAD模型。与之前的工作相比，我们直接预测对准参数和形状嵌入。我们通过在对比学习框架中学习CAD嵌入并将其提取到FastCAD中来实现高质量的形状检索。与其他RGB-D扫描方法相比，我们的单阶段方法将推理时间缩短了50倍，同时在具有挑战性的Scan2CAD比对基准上表现优于其他方法。此外，我们的方法与在线3D重建技术无缝协作。这使得能够从10 FPS的视频中实时生成精确的基于CAD模型的重建。通过这样做，我们显著提高了视频设置中Scan2CAD的对准精度，从43.0%提高到48.2%，重建精度从22.9%提高到29.6%。 et.al.|[2403.15161](http://arxiv.org/abs/2403.15161)|null|
|**2024-03-22**|**Recent Trends in 3D Reconstruction of General Non-Rigid Scenes**|重建真实世界的模型，包括真实场景的3D几何、外观和运动，对于计算机图形学和计算机视觉至关重要。它能够合成逼真的新颖视图，对电影行业和AR/VR应用非常有用。它还通过避免费力的手动设计过程，促进了计算机游戏和AR/VR中所需的内容创建。此外，这些模型是智能计算系统的基础，这些系统需要解释真实世界的场景和动作，以便与人类世界安全地行动和交互。值得注意的是，我们周围的世界是动态的，重建动态、非刚性移动场景的模型是一个严重缺乏约束和具有挑战性的问题。这份最先进的报告（STAR）为读者提供了单目和多视图输入的最先进技术的全面总结，如RGB和RGB-D传感器的数据等，传达了对不同方法及其潜在应用的理解，以及有希望的进一步研究方向。该报告涵盖了一般非刚性场景的3D重建，并进一步阐述了场景分解、编辑和控制以及可推广和生成建模的技术。更具体地说，我们首先回顾了理解和驾驭该领域所需的常见和基本概念，然后通过回顾使用传统和基于机器学习的神经表示的最新方法来讨论最先进的技术，包括对新启用的应用程序的讨论。STAR最后讨论了剩余的局限性和悬而未决的挑战。 et.al.|[2403.15064](http://arxiv.org/abs/2403.15064)|null|
|**2024-03-21**|**Hyperspectral Neural Radiance Fields**|高光谱成像（HSI）已在许多应用中用于无损测定样品的材料和/或化学成分。人们对创建3D高光谱重建越来越感兴趣，它可以提供空间和光谱信息，同时也可以缓解常见的HSI挑战，如非朗伯表面和半透明物体。然而，由于高光谱相机的技术限制，传统的HSI三维重建很困难。近年来，神经辐射场（NeRF）在创建由各种相机模型捕获的场景的高质量体积3D表示方面取得了广泛的成功。利用NeRFs的最新进展，我们提出计算一种高光谱3D重建，其中空间和视角方向上的每个点都由波长相关的辐射和透射光谱表征。为了评估我们的方法，收集了一个数据集，其中包含8个场景和2台相机的近2000幅高光谱图像。我们与传统的RGB NeRF基线进行比较，并使用替代频谱表示进行消融测试。最后，我们展示了高光谱NeRFs在高光谱超分辨率和成像传感器模拟方面的潜力。我们展示了我们的高光谱NeRF方法能够创建快速、准确的体积3D高光谱场景，并为未来的研究提供了几个新的应用和领域。 et.al.|[2403.14839](http://arxiv.org/abs/2403.14839)|null|
|**2024-03-21**|**GRM: Large Gaussian Reconstruction Model for Efficient 3D Reconstruction and Generation**|我们介绍了GRM，这是一种能够在大约0.1s内从稀疏视图图像中恢复3D资产的大规模重建器。GRM是一种基于前馈变换器的模型，它有效地结合了多视图信息，以将输入像素转换为像素对齐的高斯，这些高斯不被投影以创建一组代表场景的密集分布的3D高斯。我们的变压器架构和3D高斯的使用共同开启了一个可扩展且高效的重建框架。大量的实验结果表明，在重建质量和效率方面，我们的方法优于其他方法。我们还通过将GRM与现有的多视图扩散模型相集成，展示了它在生成任务（即文本到3D和图像到3D）中的潜力。我们的项目网站位于：https://justimyhxu.github.io/projects/grm/. et.al.|[2403.14621](http://arxiv.org/abs/2403.14621)|**[link](https://github.com/justimyhxu/grm)**|
|**2024-03-21**|**Isotropic Gaussian Splatting for Real-Time Radiance Field Rendering**|三维高斯飞溅方法由于其在训练中的高性能和渲染图像的高质量而引起了人们的广泛关注。但是，它使用各向异性高斯核来表示场景。尽管这种各向异性核在表示几何体方面具有优势，但它们在计算方面导致困难，例如分裂或合并两个核。在本文中，我们建议使用各向同性高斯核来避免计算中的这些困难，从而获得更高性能的方法。实验证实，所提出的方法在不损失几何表示精度的情况下大约快100X。所提出的方法可以应用于需要辐射场的大范围应用，如三维重建、视图合成和动态对象建模。 et.al.|[2403.14244](http://arxiv.org/abs/2403.14244)|null|
|**2024-03-21**|**Leveraging Thermal Modality to Enhance Reconstruction in Low-Light Conditions**|神经辐射场（NeRF）通过从多视图图像中学习场景的隐式体积表示来实现照片逼真的新视图合成，从而忠实地传达色度信息。然而，传感器噪声将污染低值像素信号，并且有损相机图像信号处理器将在极暗的情况下进一步去除接近零的强度，从而恶化合成性能。现有的方法从原始图像重建低光场景，但难以恢复暗区域中的纹理和边界细节。此外，它们不适用于依赖显式表示的高速模型。为了解决这些问题，我们提出了Thermal NeRF，它将热和可见原始图像作为输入，考虑到热相机对照明变化是鲁棒的，并且原始图像在黑暗中保留了任何可能的线索，以同时完成可见和热视图合成。此外，建立了第一个多视图热可见光数据集（MVTV），以支持多模式NeRF的研究。Thermal NeRF实现了细节保留和噪声平滑之间的最佳折衷，并提供了比以前更好的合成性能。最后，我们证明了这两种模式在3D重建中是有益的。 et.al.|[2403.14053](http://arxiv.org/abs/2403.14053)|null|
|**2024-03-20**|**T-Pixel2Mesh: Combining Global and Local Transformer for 3D Mesh Generation from a Single Image**|Pixel2Mesh（P2M）是一种通过粗网格到细网格变形从单色图像重建3D形状的经典方法。尽管P2M能够生成看似合理的全局形状，但其图形卷积网络（GCN）通常会产生过于平滑的结果，导致细粒度几何细节的丢失。此外，P2M为遮挡区域生成不可信的特征，并与从合成数据到真实世界图像的域差距作斗争，这是单视图3D重建方法的常见挑战。为了应对这些挑战，我们提出了一种新的Transformer增强架构，命名为T-Pixel2Mesh，其灵感来自P2M的从粗到细方法。具体而言，我们使用全局Transformer来控制整体形状，使用局部Transformer通过基于图的点上采样逐步细化局部几何细节。为了增强真实世界的重建，我们提出了简单而有效的线性尺度搜索（LSS），它在输入预处理过程中起到了及时调整的作用。我们在ShapeNet上的实验展示了最先进的性能，而在真实世界数据上的结果显示了泛化能力。 et.al.|[2403.13663](http://arxiv.org/abs/2403.13663)|null|
|**2024-03-20**|**MULAN-WC: Multi-Robot Localization Uncertainty-aware Active NeRF with Wireless Coordination**|本文提出了MULAN-WC，这是一种新颖的多机器人三维重建框架，利用了机器人和神经辐射场（NeRF）之间基于无线信号的协调。我们的方法解决了多机器人三维重建中的关键挑战，包括机器人间姿态估计、定位不确定性量化和主动最佳下一视图选择。我们介绍了一种使用无线到达角（AoA）和测距测量来估计机器人之间的相对姿态的方法，以及量化这些姿态估计的无线定位中嵌入的不确定性并将其纳入NeRF训练损失中，以减轻不准确的相机姿态的影响。此外，我们提出了一种主动视图选择方法，在确定下一个最佳视图时考虑机器人姿态的不确定性，以改进3D重建，从而通过智能视图选择实现更快的收敛。在合成数据集和真实世界数据集上进行的大量实验证明了我们的框架在理论和实践中的有效性。利用无线协调和定位不确定性感知训练，MULAN-WC可以实现高质量的三维重建，这接近于应用地面实况相机姿态。此外，通过向机器人推荐新的视图位置，对新视图的信息增益进行量化，可以在增量捕获图像的情况下实现一致的渲染质量改进。我们的硬件实验展示了将MULAN-WC部署到真实机器人系统的实用性。 et.al.|[2403.13348](http://arxiv.org/abs/2403.13348)|null|
|**2024-03-19**|**GVGEN: Text-to-3D Generation with Volumetric Representation**|近年来，3D高斯飞溅已成为一种强大的3D重建和生成技术，以其快速和高质量的渲染能力而闻名。为了解决这些缺点，本文介绍了一种新的基于扩散的框架GVGEN，旨在从文本输入中有效地生成3D高斯表示。我们提出了两种创新技术：（1）结构化体积表示。我们首先将无组织的三维高斯点排列为结构化形式的高斯体积。这种变换允许在由固定数量的高斯组成的体积内捕捉复杂的纹理细节。为了更好地优化这些细节的表示，我们提出了一种独特的修剪和加密方法，称为候选池策略，通过选择性优化提高细节保真度。（2） 粗至细发电管道。为了简化GaussianVolume的生成，并使模型能够生成具有详细三维几何结构的实例，我们提出了一种从粗到细的管道。它首先构建一个基本的几何结构，然后预测完整的高斯属性。与现有的3D生成方法相比，我们的框架GVGEN在定性和定量评估方面表现出卓越的性能。同时，它保持了快速的生成速度（ $\sim$ 7秒），有效地在质量和效率之间取得了平衡。 et.al.|[2403.12957](http://arxiv.org/abs/2403.12957)|null|
|**2024-03-19**|**PostoMETRO: Pose Token Enhanced Mesh Transformer for Robust 3D Human Mesh Recovery**|随着基于单图像的人体网格恢复的最新进展，人们对增强其在某些极端场景（如遮挡）中的性能越来越感兴趣，同时保持整体模型的准确性。尽管在遮挡条件下获得精确注释的3D人体姿势具有挑战性，但仍有大量丰富而精确的2D姿势注释可供利用。然而，现有的工作大多集中在直接利用二维姿态坐标来估计三维姿态和网格。在本文中，我们提出了PostoMETRO（ $\textbf｛Pos｝$e$\textbf｛to｝$ken-edvanced$\textbf｛ME｝$sh$\textbf｛TR｝$ansf$\textbf｛O｝$ rmer），它以令牌方式将遮挡弹性2D姿势表示集成到转换器中。利用专门的姿势标记器，我们有效地将2D姿势数据压缩为姿势标记的紧凑序列，并将它们与图像标记一起馈送到变换器。这一过程不仅确保了对图像纹理的丰富描述，而且促进了姿势和图像信息的强大集成。随后，通过顶点和关节令牌来查询这些组合令牌，以解码网格顶点和人体关节的3D坐标。在强大的姿势标记表示和有效组合的帮助下，即使在遮挡等极端情况下，我们也能够生成更精确的三维坐标。在标准和遮挡特定基准上的实验都证明了PostoMETRO的有效性。定性结果进一步说明了2D姿态如何帮助3D重建的清晰度。将提供代码。 et.al.|[2403.12473](http://arxiv.org/abs/2403.12473)|null|

<p align=right>(<a href=#updated-on-20240325>back to top</a>)</p>

## Diffusion

|Publish Date|Title|Abstract|PDF|Code|
|---|---|---|---|---|
|**2024-03-22**|**DiffusionMTL: Learning Multi-Task Denoising Diffusion Model from Partially Annotated Data**|最近，人们对从部分注释的数据中学习多个密集场景理解任务的实际问题越来越感兴趣，其中每个训练样本仅针对任务的子集进行标记。从最先进的方法中可以观察到，训练中任务标签的缺失会导致低质量和有噪声的预测。为了解决这个问题，我们将部分标记的多任务密集预测重新表述为像素级去噪问题，并提出了一种新的多任务去噪扩散框架DiffusionMTL。它设计了一种联合扩散和去噪范式，以对任务预测或特征图中的潜在噪声分布进行建模，并为不同任务生成校正输出。为了利用去噪中的多任务一致性，我们进一步引入了一种多任务条件调节策略，该策略可以隐含地利用任务的互补性来帮助学习未标记的任务，从而提高不同任务的去噪性能。大量的定量和定性实验表明，在两种不同的局部标记评估设置下，所提出的多任务去噪扩散模型可以显著改进多任务预测图，并在三个具有挑战性的多任务基准上优于最先进的方法。代码位于https://prismformore.github.io/diffusionmtl/. et.al.|[2403.15389](http://arxiv.org/abs/2403.15389)|null|
|**2024-03-22**|**LATTE3D: Large-scale Amortized Text-To-Enhanced3D Synthesis**|最近的文本到3D生成方法产生了令人印象深刻的3D结果，但需要耗时的优化，每次提示可能需要一个小时。ATT3D等摊销方法同时优化多个提示以提高效率，实现快速的文本到三维合成。然而，它们无法捕捉高频几何体和纹理细节，并且难以缩放到大型提示集，因此泛化能力较差。我们引入LATTE3D，解决了这些限制，以在更大的提示集上实现快速、高质量的生成。我们方法的关键是1）构建可扩展的体系结构，2）在优化过程中通过3D感知扩散先验、形状正则化和模型初始化来利用3D数据，以实现对各种复杂训练提示的鲁棒性。LATTE3D对神经场和纹理表面生成进行摊销，以在单个正向过程中生成高度详细的纹理网格。LATTE3D在400ms内生成3D对象，并可通过快速测试时间优化进一步增强。 et.al.|[2403.15385](http://arxiv.org/abs/2403.15385)|null|
|**2024-03-22**|**Energy-dependent Boosted Dark Matter from Diffuse Supernova Neutrino Background**|来自宇宙中过去超新星的扩散中微子为我们提供了一个测试暗物质（DM）相互作用的独特机会。这些中微子可以将银河系晕中的DM粒子散射并提升到相对论能量，使我们能够在陆地实验室中探测到它们。专注于由矢量或标量玻色子介导的DM中微子和电子相互作用的通用模型，我们实现了与能量相关的散射截面，并对在向地面实验传播时由于电子在介质中散射而导致的DM衰减进行了详细的数值分析。我们使用XENONnT、LUX-ZEPLIN和PandaX-4T直接探测实验的最新数据，为质量在 $\sim（0.1，10^4）~$ MeV范围内的DM设定了DM中微子和电子相互作用的新限制。我们证明，考虑DM相互作用的能量相关横截面会显著影响先前在恒定横截面假设下导出的约束，并将其修改多个数量级。 et.al.|[2403.15367](http://arxiv.org/abs/2403.15367)|null|
|**2024-03-22**|**Ultrasound Imaging based on the Variance of a Diffusion Restoration Model**|尽管今天超声成像在医学中很普遍，但超声信噪比仍然受到几种噪声和伪影来源的影响。此外，增强超声图像质量涉及到平衡同时存在的因素，如对比度、分辨率和斑点保持。最近，在解决超声图像重建问题的基于模型和基于学习的方法方面都取得了进展。综合考虑两个世界的优点，我们提出了一种混合重建方法，将超声线性直接模型与来自生成去噪扩散模型的基于学习的先验相结合。更具体地说，我们依赖于预训练的去噪扩散恢复模型（DDRM）的无监督微调。考虑到超声固有的乘性噪声的性质，本文提出了一个经验模型来表征超声图像扩散重建的随机性，并将其方差作为回声图估计器来显示其兴趣。我们对合成、体外和体内数据进行了实验，证明了我们的方差成像方法在通过单平面波采集实现高质量图像重建方面的有效性，并与最先进的方法进行了比较。 et.al.|[2403.15316](http://arxiv.org/abs/2403.15316)|null|
|**2024-03-22**|**Controlled Training Data Generation with Diffusion Models**|在这项工作中，我们提出了一种控制文本到图像生成模型的方法，以生成对监督学习特别“有用”的训练数据。与之前使用开环方法和预定义提示来使用语言模型或人类专业知识生成新数据的工作不同，我们开发了一个涉及两种反馈机制的自动闭环系统。第一种机制使用来自给定监督模型的反馈，并找到导致最大化模型损失的图像生成的对抗性提示。虽然这些对抗性提示导致模型提供不同的数据，但它们没有被告知目标分布，这可能是低效的。因此，我们引入了第二种反馈机制，该机制将生成过程引导到特定的目标分布。我们将这两种机制相结合的方法称为引导对抗提示。我们在不同的任务、数据集和架构上进行评估，具有不同类型的分布变化（虚假相关的数据、看不见的域），并证明了与开环方法相比，所提出的反馈机制的效率。 et.al.|[2403.15309](http://arxiv.org/abs/2403.15309)|null|
|**2024-03-22**|**Parametric PDE Control with Deep Reinforcement Learning and Differentiable L0-Sparse Polynomial Policies**|参数偏微分方程的最优控制在工程和科学的许多应用中至关重要。近年来，科学机器学习的进步为参数偏微分方程的控制开辟了新的领域。特别是，深度强化学习（DRL）有潜力在各种应用中解决高维和复杂的控制问题。大多数DRL方法依赖于深度神经网络（DNN）控制策略。然而，对于许多动态系统，基于DNN的控制策略往往过于参数化，这意味着它们需要大量的训练数据，表现出有限的鲁棒性，并且缺乏可解释性。在这项工作中，我们利用字典学习和可微L $_0$ 正则化来学习参数偏微分方程的稀疏、鲁棒和可解释的控制策略。我们的稀疏策略架构与DRL方法无关，可以用于不同的策略梯度和actor-critic DRL算法，而无需改变其策略优化过程。我们在控制参数Kuramoto Sivashinsky和对流扩散反应PDE的挑战性任务上测试了我们的方法。我们证明，我们的方法（1）优于基于基线DNN的DRL策略，（2）允许推导学习的最优控制律的可解释方程，以及（3）在不重新训练策略的情况下推广到PDE的看不见的参数。 et.al.|[2403.15267](http://arxiv.org/abs/2403.15267)|null|
|**2024-03-22**|**Spectral Motion Alignment for Video Motion Transfer using Diffusion Models**|扩散模型的演变极大地影响了视频的生成和理解。特别地，文本到视频扩散模型（VDM）显著促进了具有目标外观、运动等的输入视频的定制。尽管取得了这些进步，但在从视频帧中准确提取运动信息方面仍然存在挑战。虽然现有的工作利用连续帧残差作为目标运动向量，但它们天生缺乏全局运动上下文，并且容易受到逐帧失真的影响。为了解决这一问题，我们提出了谱运动对齐（SMA），这是一种使用傅立叶和小波变换来细化和对齐运动矢量的新框架。SMA通过结合频域正则化来学习运动模式，促进全帧全局运动动力学的学习，并减轻空间伪影。大量实验证明了SMA在改善运动传递方面的功效，同时保持了计算效率和各种视频定制框架之间的兼容性。 et.al.|[2403.15249](http://arxiv.org/abs/2403.15249)|null|
|**2024-03-22**|**Shadow Generation for Composite Image Using Diffusion model**|在图像合成领域，为插入的前景生成逼真的阴影仍然是一个艰巨的挑战。先前的工作已经开发了基于成对训练数据进行训练的图像到图像翻译模型。然而，由于数据稀缺和固有的任务复杂性，他们正在努力生成形状和强度准确的阴影。在本文中，我们求助于具有丰富的自然阴影图像先验知识的基础模型。具体来说，我们首先将ControlNet应用于我们的任务，然后提出强度调制模块来提高阴影强度。此外，我们使用一种新的数据采集管道将小规模的DESOBA数据集扩展到DESOBAv2。在DESOBA和DESOBAv2数据集以及真实合成图像上的实验结果证明了我们的模型在阴影生成任务中的优越能力。数据集、代码和模型发布于https://github.com/bcmi/Object-Shadow-Generation-Dataset-DESOBAv2. et.al.|[2403.15234](http://arxiv.org/abs/2403.15234)|**[link](https://github.com/bcmi/object-shadow-generation-dataset-desobav2)**|
|**2024-03-22**|**Broad Instantaneous Bandwidth Microwave Spectrum Analyzer with a Microfabricated Atomic Vapor Cell**|我们报道了在大磁场梯度下，用微制造的蒸气电池中的热原子Rb $进行宽瞬时带宽微波光谱分析。传感器是一个MEMS原子气相电池，充满同位素纯的$^｛87｝\mathrm｛Rb｝$和$\mathrm{N}_2$缓冲气体来定位原子的运动。感兴趣的微波信号通过共面波导耦合到细胞，在原子的光学泵浦基态之间引发自旋翻转跃迁。具有大梯度的静态磁场将输入微波信号的$\textit｛频谱｝$映射到用激光束记录到相机上的细胞吸收图像上的位置相关的$\text｛自旋翻转模式｝$。在我们的原理验证实验中，我们展示了一种微波频谱分析仪，该分析仪具有以13.165 GHz为中心的约1 GHz瞬时带宽、3 MHz频率分辨率、2 kHz刷新率和在1秒测量时间内的-23 dBm单音微波功率检测限值。通过考虑光泵浦、微波相互作用、$^{87}\mathrm{Rb}$ 原子的扩散和激光吸收的过程，建立了一个理论模型来模拟图像信号。我们希望在优化的设置中达到超过25 GHz的瞬时带宽，受外加磁场梯度的限制。我们的演示为基于电子外差检测的传统微波频谱分析仪提供了一种实用的替代方案。 et.al.|[2403.15155](http://arxiv.org/abs/2403.15155)|null|
|**2024-03-22**|**Oxygenation of CO and NO on Amorphous Solid Water**|\noindent\textit{Context.}以定量的方式研究了分子在无定形固体水上形成、弛豫、扩散和解吸的动力学。\noindent\textit{Aims.}我们的目标是在定量水平上表征原子+双原子复合反应后，CO $_2$和NO$_2$在冷无定形固体水上的形成概率、稳定性、能量弛豫和扩散动力学。\noindent\textit｛方法。｝使用精确的机器学习能量函数和波动电荷模型来研究原子氧与CO和NO在无定形固态水（ASW）上的扩散、相互作用和复合动力学。通过对振动态密度的分析，确定了ASW和水中内部自由度的能量弛豫。通过扩展和非平衡MD模拟研究了表面扩散和解吸的能量学。\noindent\textit｛结果。｝以定量的方式确定了纳秒时间尺度上的反应概率，并证明反应物的表面扩散导致初始分离高达20\AA\/的复合。复合后，CO$_2$和NO$_2$在皮秒时间尺度上通过向水的内部和表面声子模式的能量转移而稳定。平均扩散势垒和解吸能与实验结果一致。复合后，三原子产物容易扩散，这与CO$_2$和NO$_2$ 在多纳秒时间尺度上都是静止的平衡情况形成了鲜明对比。 et.al.|[2403.15141](http://arxiv.org/abs/2403.15141)|null|

<p align=right>(<a href=#updated-on-20240325>back to top</a>)</p>

## NeRF

|Publish Date|Title|Abstract|PDF|Code|
|---|---|---|---|---|
|**2024-03-22**|**LATTE3D: Large-scale Amortized Text-To-Enhanced3D Synthesis**|最近的文本到3D生成方法产生了令人印象深刻的3D结果，但需要耗时的优化，每次提示可能需要一个小时。ATT3D等摊销方法同时优化多个提示以提高效率，实现快速的文本到三维合成。然而，它们无法捕捉高频几何体和纹理细节，并且难以缩放到大型提示集，因此泛化能力较差。我们引入LATTE3D，解决了这些限制，以在更大的提示集上实现快速、高质量的生成。我们方法的关键是1）构建可扩展的体系结构，2）在优化过程中通过3D感知扩散先验、形状正则化和模型初始化来利用3D数据，以实现对各种复杂训练提示的鲁棒性。LATTE3D对神经场和纹理表面生成进行摊销，以在单个正向过程中生成高度详细的纹理网格。LATTE3D在400ms内生成3D对象，并可通过快速测试时间优化进一步增强。 et.al.|[2403.15385](http://arxiv.org/abs/2403.15385)|null|
|**2024-03-20**|**Visual Imitation Learning of Task-Oriented Object Grasping and Rearrangement**|面向任务的物体抓取和重排是机器人完成不同现实操作任务的关键技能。然而，由于对物体的部分观察和分类物体的形状变化，它们仍然具有挑战性。在本文中，我们提出了多特征隐式模型（MIMO），这是一种新的对象表示，它在隐式神经场中对点和对象之间的多个空间特征进行编码。在多个特征上训练这样的模型可以确保它在不同方面一致地嵌入物体形状，从而提高其在从局部观察、形状相似性测量和建模物体之间的空间关系的物体形状重建中的性能。基于MIMO，我们提出了一个从单个或多个人类演示视频中学习面向任务的对象抓取和重排的框架。仿真评估表明，我们的方法在多视图和单视图观测方面优于最先进的方法。真实世界的实验证明了我们的方法在操纵任务的单次和少次模仿学习中的有效性。 et.al.|[2403.14000](http://arxiv.org/abs/2403.14000)|null|
|**2024-03-18**|**LN3Diff: Scalable Latent Neural Fields Diffusion for Speedy 3D Generation**|随着生成模型和可微分绘制技术的进步，神经绘制领域取得了重大进展。尽管2D扩散已经取得了成功，但统一的3D扩散管道仍然悬而未决。本文介绍了一种称为LN3Diff的新框架来解决这一差距，并实现快速、高质量和通用的条件3D生成。我们的方法利用3D感知架构和变分自动编码器（VAE）将输入图像编码到结构化、紧凑和3D潜在空间中。潜像由基于变换器的解码器解码为高容量的3D神经场。通过在这个3D感知的潜在空间上训练扩散模型，我们的方法在ShapeNet上实现了最先进的3D生成性能，并在各种数据集的单目3D重建和条件3D生成中表现出卓越的性能。此外，它在推理速度方面超过了现有的3D扩散方法，不需要每实例优化。我们提出的LN3Diff在三维生成建模方面取得了重大进展，并有望在三维视觉和图形任务中应用。 et.al.|[2403.12019](http://arxiv.org/abs/2403.12019)|null|
|**2024-03-15**|**NeuralOCT: Airway OCT Analysis via Neural Fields**|光学相干断层扫描（OCT）是眼科中一种流行的模式，也用于血管内。我们对这项工作的兴趣是在婴儿和儿童气道异常的背景下进行OCT，其中OCT的高分辨率和无辐射的事实很重要。气道OCT的目标是提供气道几何形状的准确估计（2D和3D），以评估气道异常，如声门下狭窄。我们提出 $\texttt｛NeuralOCT｝$，这是一种基于学习的方法来处理气道OCT图像。具体而言，$\texttt｛NeuralOCT｝$通过稳健地桥接两个步骤从OCT扫描中提取3D几何形状：通过2D分割提取点云和通过神经场从点云中重建3D。我们的实验表明，$\texttt｛NeuralOCT｝$ 可以产生准确而稳健的3D气道重建，平均A线误差小于70微米。我们的代码将在GitHub上提供。 et.al.|[2403.10622](http://arxiv.org/abs/2403.10622)|null|
|**2024-03-15**|**NECA: Neural Customizable Human Avatar**|人类化身已经成为一种具有各种应用的新型3D资产。理想情况下，人类化身应该是完全可定制的，以适应不同的设置和环境。在这项工作中，我们介绍了NECA，这是一种能够从单目或稀疏视图视频中学习多功能人体表示的方法，能够在姿势、阴影、形状、照明和纹理等方面进行细粒度定制。我们方法的核心是在互补的双空间中表示人类，并预测几何、反照率、阴影以及外部照明的解开神经场，从中我们能够通过体积渲染获得具有高频细节的真实感渲染。大量实验证明了我们的方法在真实感渲染以及各种编辑任务（如新颖的姿势合成和重新照明）方面优于最先进的方法。代码位于https://github.com/iSEE-Laboratory/NECA. et.al.|[2403.10335](http://arxiv.org/abs/2403.10335)|**[link](https://github.com/isee-laboratory/neca)**|
|**2024-03-13**|**Representing Anatomical Trees by Denoising Diffusion of Implicit Neural Fields**|解剖树在临床诊断和治疗计划中起着核心作用。然而，由于解剖树的拓扑结构和几何形状多变且复杂，因此准确地表示解剖树具有挑战性。使用医学成像捕获的表示树状结构的传统方法虽然对可视化血管和支气管网络非常宝贵，但在分辨率、灵活性和效率方面存在缺陷。最近，隐式神经表示（INRs）已经成为准确有效地表示形状的强大工具。我们提出了一种使用INR表示解剖树的新方法，同时还通过INR空间中的去噪扩散来捕捉一组树的分布。我们以任何所需的分辨率准确捕捉解剖树的复杂几何形状和拓扑结构。通过广泛的定性和定量评估，我们展示了高保真度树重建，具有任意分辨率但紧凑的存储，以及跨解剖部位和树复杂性的多功能性。 et.al.|[2403.08974](http://arxiv.org/abs/2403.08974)|**[link](https://github.com/sinashish/treediffusion)**|
|**2024-03-12**|**Scalable Spatiotemporal Prediction with Bayesian Neural Fields**|时空数据集由空间参考的时间序列组成，在许多科学和商业智能应用中无处不在，如空气污染监测、疾病跟踪和云需求预测。随着现代数据集的规模和复杂性不断增加，人们越来越需要新的统计方法，这些方法足够灵活，可以捕捉复杂的时空动态，并且可以扩展，可以处理大型预测问题。这项工作提出了贝叶斯神经场（BayesNF），这是一种用于推断时空域上丰富概率分布的域通用统计模型，可用于数据分析任务，包括预测、插值和变差法。BayesNF将一种用于高容量函数估计的新型深度神经网络架构与用于鲁棒不确定性量化的分层贝叶斯推理相结合。通过通过一系列平滑可微变换定义先验，使用通过随机梯度下降训练的变量学习代理对大规模数据进行后验推理。我们根据突出的统计和机器学习基线评估BayesNF，显示出在气候和公共卫生数据集的各种预测问题上的显著改进，这些数据集包含数万到数十万个测量值。该论文附有一个开源软件包(https://github.com/google/bayesnf)它易于使用，并与JAX机器学习平台上的现代GPU和TPU加速器兼容。 et.al.|[2403.07657](http://arxiv.org/abs/2403.07657)|**[link](https://github.com/google/bayesnf)**|
|**2024-03-11**|**SiLVR: Scalable Lidar-Visual Reconstruction with Neural Radiance Fields for Robotic Inspection**|我们提出了一种基于神经场的大规模重建系统，该系统融合激光雷达和视觉数据，生成几何精度高的高质量重建，并捕捉照片逼真的纹理。该系统采用了最先进的神经辐射场（NeRF）表示，还结合了激光雷达数据，这对深度和表面法线增加了强大的几何约束。我们利用实时激光雷达SLAM系统的轨迹来引导运动结构（SfM）过程，以显著减少计算时间，并提供对激光雷达深度损失至关重要的度量尺度。我们使用子映射将系统缩放到长轨迹上捕获的大规模环境。我们用多摄像头、激光雷达传感器套件的数据演示了重建系统，该套件安装在腿式机器人上，手持扫描600米的建筑场景，并安装在空中机器人上，测量多层模拟灾难现场建筑。网站https://ori-drs.github.io/projects/silvr/ et.al.|[2403.06877](http://arxiv.org/abs/2403.06877)|null|
|**2024-03-15**|**CoNFiLD: Conditional Neural Field Latent Diffusion Model Generating Spatiotemporal Turbulence**|本研究介绍了条件神经场潜在扩散（CoNFiLD）模型，这是一种新的生成学习框架，旨在快速模拟三维不规则域内混沌和湍流系统中复杂的时空动力学。传统的涡解析数值模拟，尽管提供了详细的流量预测，但由于其广泛的计算需求，遇到了很大的局限性，限制了其在更广泛的工程环境中的应用。相比之下，基于深度学习的代理模型有望提供高效、数据驱动的解决方案。然而，它们的有效性往往因依赖确定性框架而受到损害，而确定性框架在准确捕捉湍流的混沌和随机性质方面存在不足。CoNFiLD模型通过将条件神经场编码与潜在扩散过程协同集成来解决这些挑战，从而能够在不同条件下高效且稳健地生成时空湍流。利用贝叶斯条件采样，该模型可以无缝适应各种湍流生成场景，而无需再训练，涵盖从使用稀疏传感器测量的零样本全场流重建到超分辨率生成和时空流数据恢复的应用。已经对各种具有不规则几何形状的非均匀、各向异性湍流进行了全面的数值实验，以评估该模型的多功能性和有效性，展示了其在湍流生成和更广泛的时空动力学建模领域的变革潜力。 et.al.|[2403.05940](http://arxiv.org/abs/2403.05940)|null|
|**2024-03-09**|**Learned 3D volumetric recovery of clouds and its uncertainty for climate analysis**|气候预测和云物理的重大不确定性与浅层散射云的观测差距有关。应对这些挑战需要对其三维（3D）异质体积散射内容进行遥感。这就需要无源散射计算机断层扫描（CT）。我们设计了一个基于学习的模型（ProbeCT）来实现这种云的CT，基于有噪声的多视图星载图像。ProbeCT首次推断出每个3D位置的异质消光系数的后验概率分布。这产生了任意有价值的统计数据，例如，最可能灭绝的3D场及其不确定性。ProbeCT使用神经场表示，进行本质上实时的推理。ProbeCT通过一个新的基于物理的云体积场及其相应图像的标记多类数据库进行监督训练。为了改进分布外推理，我们通过差分渲染引入了自监督学习。我们在模拟和真实世界的数据中演示了该方法，并指出了3D恢复和不确定性与降水和可再生能源的相关性。 et.al.|[2403.05932](http://arxiv.org/abs/2403.05932)|null|

<p align=right>(<a href=#updated-on-20240325>back to top</a>)</p>

[contributors-shield]: https://img.shields.io/github/contributors/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[contributors-url]: https://github.com/Vincentqyw/cv-arxiv-daily/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[forks-url]: https://github.com/Vincentqyw/cv-arxiv-daily/network/members
[stars-shield]: https://img.shields.io/github/stars/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[stars-url]: https://github.com/Vincentqyw/cv-arxiv-daily/stargazers
[issues-shield]: https://img.shields.io/github/issues/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[issues-url]: https://github.com/Vincentqyw/cv-arxiv-daily/issues

