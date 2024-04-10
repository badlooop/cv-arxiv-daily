[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]

## Updated on 2024.04.10
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
|**2024-04-09**|**3D Geometry-aware Deformable Gaussian Splatting for Dynamic View Synthesis**|在本文中，我们提出了一种用于动态视图合成的3D几何感知可变形高斯散射方法。现有的基于神经辐射场（NeRF）的解决方案以隐含的方式学习变形，而这种方式不能结合3D场景几何。因此，所学习的变形不一定是几何相干的，这导致了不令人满意的动态视图合成和3D动态重建。最近，3D高斯飞溅提供了3D场景的新表示，在此基础上可以利用3D几何来学习复杂的3D变形。具体而言，场景被表示为3D高斯的集合，其中每个3D高斯被优化为随着时间的推移移动和旋转，以对变形进行建模。为了在变形过程中加强3D场景几何约束，我们显式地提取3D几何特征，并将其集成到学习3D变形中。通过这种方式，我们的解决方案实现了3D几何感知变形建模，从而改进了动态视图合成和3D动态重建。在合成数据集和真实数据集上的大量实验结果证明了我们的解决方案的优越性，它实现了最先进的性能。该项目位于https://npucvr.github.io/GaGS/ et.al.|[2404.06270](http://arxiv.org/abs/2404.06270)|null|
|**2024-04-09**|**HFNeRF: Learning Human Biomechanic Features with Neural Radiance Fields**|在新视图合成的最新进展中，应用于人类受试者的基于可推广神经辐射场（NeRF）的方法在从少量图像生成新视图方面显示出显著的结果。但是，这种泛化能力无法捕捉所有实例共享的骨架的基本结构特征。在此基础上，我们介绍了HFNeRF：一种新的可推广的人体特征NeRF，旨在使用预训练的图像编码器生成人体生物力学特征。尽管先前的人类NeRF方法在生成照片真实感虚拟化身方面显示出了有希望的结果，但这种方法缺乏对包括增强现实（AR）/虚拟现实（VR）在内的下游应用至关重要的潜在人类结构或生物力学特征，如骨骼或关节信息。HFNeRF利用2D预训练的基础模型，使用神经渲染在3D中学习人类特征，然后使用体积渲染生成2D特征图。我们通过预测热图作为特征来评估骨架估计任务中的HFNeRF。所提出的方法是完全可微的，可以同时成功地学习颜色、几何和人体骨骼。本文介绍了HFNeRF的初步结果，说明了它在使用NeRF生成具有生物力学特征的逼真虚拟化身方面的潜力。 et.al.|[2404.06152](http://arxiv.org/abs/2404.06152)|null|
|**2024-04-09**|**Gaussian Pancakes: Geometrically-Regularized 3D Gaussian Splatting for Realistic Endoscopic Reconstruction**|在结直肠癌癌症诊断中，传统的结肠镜检查技术面临着严重的局限性，包括视野有限和缺乏深度信息，这可能会阻碍癌前病变的检测。目前的方法难以提供全面准确的结肠表面3D重建，这有助于最大限度地减少缺失区域并重新检查癌前息肉。为此，我们介绍了“高斯煎饼”，这是一种利用3D高斯散射（3D GS）与基于递归神经网络的同时定位和映射（RNNSLAM）系统相结合的方法。通过在3D GS框架中引入几何和深度正则化，我们的方法确保了高斯与结肠表面的更准确对齐，从而实现更平滑的3D重建，并能新颖地查看详细的纹理和结构。对三个不同数据集的评估表明，高斯煎饼增强了新的视图合成质量，超过了当前领先的方法，PSNR提高了18%，SSIM提高了16%。它还提供了超过100倍的渲染速度和超过10倍的训练时间，使其成为实时应用程序的实用工具。因此，这有望实现临床转化，更好地检测和诊断结直肠癌癌症。 et.al.|[2404.06128](http://arxiv.org/abs/2404.06128)|**[link](https://github.com/smbonilla/gaussianpancakes)**|
|**2024-04-09**|**Revising Densification in Gaussian Splatting**|在本文中，我们解决了自适应密度控制（ADC）在三维高斯散射（3DGS）中的局限性，3DGS是一种为新视图合成实现高质量、真实感结果的场景表示方法。ADC已被引入用于自动3D点基元管理，控制致密化和修剪，然而，在致密化逻辑中存在一定的局限性。我们的主要贡献是为3DGS中的密度控制提供了一种更原则的、像素误差驱动的公式，利用辅助的每像素误差函数作为致密化的标准。我们进一步引入了一种机制来控制每个场景生成的基元的总数，并在克隆操作期间校正ADC当前不透明度处理策略中的偏差。我们的方法在不牺牲方法效率的情况下，在各种基准场景中实现了一致的质量改进。 et.al.|[2404.06109](http://arxiv.org/abs/2404.06109)|null|
|**2024-04-09**|**Incremental Joint Learning of Depth, Pose and Implicit Scene Representation on Monocular Camera in Large-scale Scenes**|用于照片真实感视图合成的密集场景重建具有多种应用，如VR/AR、自动驾驶汽车。然而，由于三个核心挑战，大多数现有方法在大规模场景中都存在困难：\textit｛（a）不准确的深度输入。｝在真实世界的大规模场景中不可能获得准确的深度输出。\textit｛（b）不准确的姿势估计。｝大多数现有方法都依赖于准确的预先估计的相机姿势。\textit｛（c）场景表示能力不足。｝单个全局辐射场缺乏有效扩展到大规模场景的能力。为此，我们提出了一种增量联合学习框架，可以实现精确的深度、姿态估计和大规模场景重建。采用基于视觉变换器的网络作为骨干，以提高尺度信息估计的性能。对于姿态估计，设计了一种特征度量束调整（FBA）方法，用于在大规模场景中精确和稳健的相机跟踪。在隐式场景表示方面，我们提出了一种增量场景表示方法，将整个大规模场景构建为多个局部辐射场，以增强3D场景表示的可扩展性。已经进行了扩展实验来证明我们的方法在深度估计、姿态估计和大规模场景重建中的有效性和准确性。 et.al.|[2404.06050](http://arxiv.org/abs/2404.06050)|null|
|**2024-04-08**|**Learning Topology Uniformed Face Mesh by Volume Rendering for Multi-view Reconstruction**|一致拓扑中的面网格是许多与面相关的应用程序的基础，例如3DMM约束的面重建和表达式重定目标。传统的方法通常通过两个独立的步骤来获取拓扑均匀的面网格：多视图立体（MVS）来重建形状，然后进行非刚性配准来对齐拓扑，但难以处理噪声和非朗伯曲面。近年来，神经体绘制技术发展迅速，在三维重建或新视图合成方面显示出巨大的优势。我们的目标是利用神经体积渲染的优势，以一致的拓扑结构对人脸网格进行多视图重建。我们提出了一种网格体绘制方法，该方法能够在保持拓扑的同时直接优化网格几何结构，并学习隐式特征来从多视图图像中建模复杂的面部外观。关键创新在于将稀疏网格特征扩展到周围空间，以模拟体绘制所需的辐射场，这有助于从图像到网格几何结构和隐含外观特征的梯度反向传播。我们提出的特征扩展模块具有变形不变性，能够在网格编辑后无缝进行真实感渲染。我们在多视图人脸图像数据集上进行了实验，以评估重建效果，并实现了动画人脸网格的真实感绘制应用程序。 et.al.|[2404.05606](http://arxiv.org/abs/2404.05606)|null|
|**2024-04-07**|**CodecNeRF: Toward Fast Encoding and Decoding, Compact, and High-quality Novel-view Synthesis**|神经辐射场（NeRF）在有效捕捉和表示3D物体和场景方面取得了巨大成功。然而，有几个因素阻碍了它作为下一代3D媒体的进一步扩散。为了在图像和视频等日常媒体格式中建立无处不在的存在，必须设计一种有效实现三个关键目标的解决方案：快速编码和解码时间、紧凑的模型尺寸和高质量的渲染。尽管取得了重大进展，但一种充分解决所有目标的综合算法尚未完全实现。在这项工作中，我们提出了CodecNeRF，这是一种用于NeRF表示的神经编解码器，由一种新颖的编码器和解码器架构组成，可以在单次前向通过中生成NeRF表示。此外，受最近参数高效微调方法的启发，我们开发了一种新的微调方法，可以有效地将生成的NeRF表示适应新的测试实例，从而实现高质量的图像渲染和紧凑的代码大小。所提出的CodecNeRF是一种新提出的用于NeRF的编码-解码微调流水线，它实现了前所未有的压缩性能，编码时间减少了150倍和20倍以上，同时在广泛使用的3D对象数据集（如ShapeNet和Objvisiver）上保持（或提高）图像质量。 et.al.|[2404.04913](http://arxiv.org/abs/2404.04913)|null|
|**2024-04-06**|**Z-Splat: Z-Axis Gaussian Splatting for Camera-Sonar Fusion**|可微分三维高斯散射（GS）是计算机视觉和图形学中重建三维场景的一种重要技术。GS将场景表示为具有变化的不透明度的3D高斯的集合，并且在给定从各种视点捕获的场景图像的情况下，使用计算高效的飞溅操作以及分析导数来计算3D高斯参数。不幸的是，在许多真实世界的成像场景中，包括水下成像、建筑物内的房间和自主导航，捕获环绕视图（ $360^{\circ}$ 视点）图像是不可能或不切实际的。在这些受限制的基线成像场景中，GS算法存在众所周知的“缺锥”问题，这导致沿深度轴的重建较差。在这份手稿中，我们证明了使用瞬态数据（来自声纳）可以通过沿深度轴采样高频数据来解决缺锥问题。我们对两种常用声纳的高斯散射算法进行了扩展，并提出了同时利用RGB相机数据和声纳数据的融合算法。通过在各种成像场景中的仿真、仿真和硬件实验，我们表明所提出的融合算法显著改善了新视图合成（PSNR提高了5 dB）和3D几何重建（倒角距离降低了60%）。 et.al.|[2404.04687](http://arxiv.org/abs/2404.04687)|null|
|**2024-04-07**|**RaFE: Generative Radiance Fields Restoration**|NeRF（Neural Radiance Fields，神经辐射场）在新型视图合成和3D重建中显示出巨大的潜力，但其性能对输入图像质量敏感，当提供低质量的稀疏输入视点时，难以实现高保真渲染。以前的NeRF恢复方法是针对特定的退化类型量身定制的，忽略了恢复的一般性。为了克服这一限制，我们提出了一种通用的辐射场恢复管道，名为RaFE，适用于各种类型的退化，如低分辨率、模糊、噪声、压缩伪影或它们的组合。我们的方法利用现成的2D恢复方法的成功来单独恢复多视图图像。我们引入了一种新的方法，使用生成对抗性网络（GANs）生成NeRF，以更好地适应多视图图像中存在的几何和外观不一致，而不是通过平均不一致来重建模糊的NeRF。具体而言，我们采用两级三平面架构，其中粗略水平保持固定以表示低质量NeRF，并且将添加到粗略水平的精细水平残差三平面建模为具有GAN的分布，以捕捉恢复中的潜在变化。我们在各种修复任务的合成和真实案例中验证了RaFE，在定量和定性评估中都表现出了卓越的性能，超过了其他特定于单个任务的3D修复方法。请查看我们的项目网站https://zkaiwu.github.io/RaFE-Project/. et.al.|[2404.03654](http://arxiv.org/abs/2404.03654)|null|
|**2024-04-04**|**The More You See in 2D, the More You Perceive in 3D**|人类可以根据过去的经验从物体的2D图像中推断出3D结构，并在看到更多图像时提高对3D的理解。受此行为的启发，我们介绍了SAP3D，这是一个用于从任意数量的未聚焦图像进行三维重建和新颖视图合成的系统。给定一个物体的一些未经处理的图像，我们通过测试时间微调来调整预先训练的视图条件扩散模型以及图像的相机姿态。然后，将自适应的扩散模型和获得的相机姿态用作3D重建和新颖视图合成的实例特定先验。我们表明，随着输入图像数量的增加，我们的方法的性能有所提高，弥补了基于优化的先验无3D重建方法和基于单图像到三维扩散的方法之间的差距。我们在真实图像和标准合成基准上演示了我们的系统。我们的消融研究证实，这种适应行为是更准确的3D理解的关键。 et.al.|[2404.03652](http://arxiv.org/abs/2404.03652)|null|

<p align=right>(<a href=#updated-on-20240410>back to top</a>)</p>

## 3D Reconstruction

|Publish Date|Title|Abstract|PDF|Code|
|---|---|---|---|---|
|**2024-04-09**|**Laue Indexing with Optimal Transport**|Laue层析成像实验从多个视角下记录的衍射图中检索多晶样品中晶粒的位置和取向。使用宽波长光谱光束可以大大减少实验时间，但对多晶样品中衍射峰的索引提出了困难的挑战；不存在关于这些布拉格峰的波长的信息，并且来自多个晶粒的衍射图案被叠加。到目前为止，还不存在能够有效地索引具有超过大约500个晶粒的样本的算法。为了满足这一需求，我们提出了一种新的方法：最优传输的Laue索引（LaueOT）。我们创建了多粒度索引问题的概率描述，并提出了一种基于辛霍恩期望最大化方法的解决方案，由于使用最优传输计算分配，该方法可以有效地找到可能性的最大值。这是一个非凸优化问题，其中粒子的方向和位置与粒子到点的分配同时优化，同时稳健地处理异常值。优化问题中要考虑的初始原型晶粒的选择也在最优传输框架内计算。LaueOT可以在不到30分钟的时间内在单个大内存GPU上快速有效地索引多达1000个晶粒。我们展示了LaueOT在具有可变晶粒数量、点位置测量噪声水平和异常分数的模拟上的性能。在我们的实验中，即使对于高噪声水平和高达70%的异常值，该算法也能恢复正确数量的颗粒。我们将LaueOT索引的结果与现有算法进行了比较，无论是对来自特征良好样品的合成中子衍射数据还是真实中子衍射数据。 et.al.|[2404.06478](http://arxiv.org/abs/2404.06478)|**[link](https://github.com/laueot/laueotx)**|
|**2024-04-09**|**Gaussian Pancakes: Geometrically-Regularized 3D Gaussian Splatting for Realistic Endoscopic Reconstruction**|在结直肠癌癌症诊断中，传统的结肠镜检查技术面临着严重的局限性，包括视野有限和缺乏深度信息，这可能会阻碍癌前病变的检测。目前的方法难以提供全面准确的结肠表面3D重建，这有助于最大限度地减少缺失区域并重新检查癌前息肉。为此，我们介绍了“高斯煎饼”，这是一种利用3D高斯散射（3D GS）与基于递归神经网络的同时定位和映射（RNNSLAM）系统相结合的方法。通过在3D GS框架中引入几何和深度正则化，我们的方法确保了高斯与结肠表面的更准确对齐，从而实现更平滑的3D重建，并能新颖地查看详细的纹理和结构。对三个不同数据集的评估表明，高斯煎饼增强了新的视图合成质量，超过了当前领先的方法，PSNR提高了18%，SSIM提高了16%。它还提供了超过100倍的渲染速度和超过10倍的训练时间，使其成为实时应用程序的实用工具。因此，这有望实现临床转化，更好地检测和诊断结直肠癌癌症。 et.al.|[2404.06128](http://arxiv.org/abs/2404.06128)|**[link](https://github.com/smbonilla/gaussianpancakes)**|
|**2024-04-09**|**Estimating the lateral speed of a fast shock driven by a coronal mass ejection at the location of solar radio emissions**|快速日冕物质抛射（CME）可以驱动能够将电子加速到高能的冲击波。这些冲击加速的电子充当电磁辐射源，通常以太阳射电暴的形式出现。最近的发现表明，太阳射电暴的无线电成像可以提供一种方法来估计低日冕中CME和相关冲击的横向扩展。我们的目标是使用多个视角的冲击波三维重建来估计日冕物质抛射驱动的冲击在无线电发射位置的膨胀速度。我们使用Nan\c的无线电成像来估计无线电发射的3D位置{c}ay日射图和冲击的3D位置。使用日地关系天文台、太阳动力学天文台以及太阳和日球层天文台的白光和极紫外CME图像重建了3D冲击。然后，使用冲击表面上无线电发射的近似3D位置来估计CME驱动的冲击在电子加速位置的横向膨胀速度。与CME相关的射电暴被发现位于CME驱动的不断扩大的冲击的侧面。我们在两个不同的位置确定了两个显著的无线电源，并发现在这些位置，冲击的横向速度在800-1000美元的范围内。在喷发的早期阶段，如此高的速度已经表明低日冕中存在快速冲击。我们还发现，与在电晕中获得的值相比，径向和横向膨胀速度之间的比率更大。所获得的高冲击速度指示在喷发的初始阶段期间的快速加速度。这种加速度很可能是导致公制无线电发射（如II型无线电爆发）存在的关键参数之一。 et.al.|[2404.06102](http://arxiv.org/abs/2404.06102)|null|
|**2024-04-08**|**3D-COCO: extension of MS-COCO dataset for image detection and 3D reconstruction modules**|我们介绍了3D-COCO，这是原始MS-COCO数据集的扩展，提供了3D模型和2D-3D对齐注释。3D-COCO旨在实现计算机视觉任务，如可通过文本、2D图像和3D CAD模型查询进行配置的3D重建或图像检测。我们用在ShapeNet和Objvisive上收集的28K 3D模型完成了现有的MS-COCO数据集。通过使用基于IoU的方法，我们将每个MS-COCO注释与最佳的3D模型进行匹配，以提供2D-3D对齐。3D-COCO的开源性质是首次亮相，应该为3D相关主题的新研究铺平道路。数据集及其源代码可在https://kalisteo.cea.fr/index.php/coco3d-object-detection-and-reconstruction/ et.al.|[2404.05641](http://arxiv.org/abs/2404.05641)|null|
|**2024-04-08**|**Learning Topology Uniformed Face Mesh by Volume Rendering for Multi-view Reconstruction**|一致拓扑中的面网格是许多与面相关的应用程序的基础，例如3DMM约束的面重建和表达式重定目标。传统的方法通常通过两个独立的步骤来获取拓扑均匀的面网格：多视图立体（MVS）来重建形状，然后进行非刚性配准来对齐拓扑，但难以处理噪声和非朗伯曲面。近年来，神经体绘制技术发展迅速，在三维重建或新视图合成方面显示出巨大的优势。我们的目标是利用神经体积渲染的优势，以一致的拓扑结构对人脸网格进行多视图重建。我们提出了一种网格体绘制方法，该方法能够在保持拓扑的同时直接优化网格几何结构，并学习隐式特征来从多视图图像中建模复杂的面部外观。关键创新在于将稀疏网格特征扩展到周围空间，以模拟体绘制所需的辐射场，这有助于从图像到网格几何结构和隐含外观特征的梯度反向传播。我们提出的特征扩展模块具有变形不变性，能够在网格编辑后无缝进行真实感渲染。我们在多视图人脸图像数据集上进行了实验，以评估重建效果，并实现了动画人脸网格的真实感绘制应用程序。 et.al.|[2404.05606](http://arxiv.org/abs/2404.05606)|null|
|**2024-04-07**|**3D Building Reconstruction from Monocular Remote Sensing Images with Multi-level Supervisions**|基于单目遥感图像的三维建筑重建是一个重要而具有挑战性的研究问题，由于其数据采集成本低且可用于大规模应用，近年来受到了越来越多的关注。然而，现有的方法依赖于昂贵的3D注释样本进行完全监督的训练，这限制了它们在大规模跨城市场景中的应用。在这项工作中，我们提出了MLS-BRN，这是一种多级监督建筑重建网络，可以灵活地利用不同注释级别的训练样本，以端到端的方式获得更好的重建结果。为了缓解对全3D监控的需求，我们设计了两个新模块，即伪建筑Bbox计算器和屋顶偏移引导的足迹提取器，以及针对不同类型样本的新任务和训练策略。在几个公共和新数据集上的实验结果表明，我们提出的MLS-BRN使用更少的3D注释样本实现了具有竞争力的性能，并与当前最先进的技术相比显著提高了足迹提取和3D重建性能。这项工作的代码和数据集将于https://github.com/opendatalab/MLS-BRN.git. et.al.|[2404.04823](http://arxiv.org/abs/2404.04823)|**[link](https://github.com/opendatalab/mls-brn)**|
|**2024-04-07**|**Joint Reconstruction of 3D Human and Object via Contact-Based Refinement Transformer**|人与物体的接触是理解人类如何与物体进行物理互动的有力线索。然而，利用人-物体接触信息从单个图像中联合重建3D人和物体并没有得到广泛的探索。在这项工作中，我们提出了一种新的联合三维人体-物体重建方法（CONTHO），该方法有效地利用了人与物体之间的接触信息。我们的系统有两个核心设计：1）3D引导的接触估计和2）基于接触的3D人和物体细化。首先，为了精确的人-物体接触估计，CONTHO最初重建3D人和物体，并将其用作接触估计的明确3D指导。其次，为了细化3D人和物体的初始重建，我们提出了一种新的基于接触的细化转换器，该转换器基于估计的人-物体接触有效地聚合人特征和物体特征。所提出的基于接触的细化防止了人和物体之间错误相关性的学习，从而实现了精确的3D重建。因此，我们的CONTHO在人-物体接触估计和3D人-物体的联合重建方面都实现了最先进的性能。该代码可在https://github.com/dqj5182/CONTHO_RELEASE. et.al.|[2404.04819](http://arxiv.org/abs/2404.04819)|**[link](https://github.com/dqj5182/contho_release)**|
|**2024-04-06**|**OmniColor: A Global Camera Pose Optimization Approach of LiDAR-360Camera Fusion for Colorizing Point Clouds**|彩色点云作为一种简单高效的三维表示方法，在机器人导航和场景重建等领域具有许多优点。这种表示现在通常用于依赖于相机和激光雷达的3D重建任务。然而，在许多现有框架中，融合来自这两种类型传感器的数据的性能较差，导致映射结果不令人满意，主要是由于相机姿态不准确。本文提出了OmniColor，这是一种使用独立的360度相机对点云进行着色的新的高效算法。给定基于激光雷达的点云和具有初始粗略相机姿态的全景图像序列，我们的目标是联合优化所有帧的姿态，以将图像映射到几何重建上。我们的管道以现成的方式工作，不需要任何特征提取或匹配过程。相反，我们通过直接最大化激光雷达地图的光度一致性来找到最佳姿态。在实验中，我们表明我们的方法可以克服全向图像的严重视觉失真，并极大地受益于360度相机的宽视场（FOV），以准确和稳定的方式重建各种场景。代码将在发布https://github.com/liubonan123/OmniColor/. et.al.|[2404.04693](http://arxiv.org/abs/2404.04693)|**[link](https://github.com/liubonan123/omnicolor)**|
|**2024-04-06**|**DATENeRF: Depth-Aware Text-based Editing of NeRFs**|扩散模型的最新进展已经显示出在基于文本提示编辑2D图像方面的显著熟练度。然而，将这些技术扩展到神经辐射场（NeRF）中的场景编辑是复杂的，因为编辑单个2D帧可能会导致多个视图之间的不一致。我们的关键见解是，NeRF场景的几何体可以作为集成这些2D编辑的桥梁。利用这种几何形状，我们使用深度条件控制网络来增强每个2D图像修改的一致性。此外，我们引入了一种修复方法，该方法利用NeRF场景的深度信息在不同的图像上分布2D编辑，确保了对错误和重新采样挑战的鲁棒性。我们的结果表明，与文本驱动的NeRF场景编辑的现有领先方法相比，这种方法实现了更一致、更逼真、更详细的编辑。 et.al.|[2404.04526](http://arxiv.org/abs/2404.04526)|null|
|**2024-04-04**|**MVD-Fusion: Single-view 3D via Depth-consistent Multi-view Generation**|我们提出了MVD融合：一种通过多视图一致RGB-D图像的生成建模进行单视图3D推理的方法。虽然最近追求3D推理的方法提倡学习新的视图生成模型，但这些生成不是3D一致的，并且需要蒸馏过程来生成3D输出。相反，我们将3D推理的任务视为直接生成相互一致的多个视图，并建立在额外推断深度可以提供增强这种一致性的机制的基础上。具体而言，在给定单个RGB输入图像的情况下，我们训练去噪扩散模型来生成多视图RGB-D图像，并利用（中等噪声）深度估计来获得基于重投影的条件，以保持多视图一致性。我们使用大规模合成数据集Obajverse以及由通用相机视点组成的真实世界CO3D数据集来训练我们的模型。我们证明，与最近的最先进技术相比，我们的方法可以产生更准确的合成，包括基于蒸馏的3D推理和先前的多视图生成方法。我们还评估了由我们的多视图深度预测引起的几何结构，并发现它比其他直接的3D推理方法产生了更准确的表示。 et.al.|[2404.03656](http://arxiv.org/abs/2404.03656)|null|

<p align=right>(<a href=#updated-on-20240410>back to top</a>)</p>

## Diffusion

|Publish Date|Title|Abstract|PDF|Code|
|---|---|---|---|---|
|**2024-04-09**|**Convergence analysis of novel discontinuous Galerkin methods for a convection dominated problem**|在本文中，我们提出并分析了对流主导区域中对流-扩散反应方程的一个数值稳定收敛格式。由于对流主导方程的标准有限元方法会引起杂散振荡，因此考虑了间断伽辽金（DG）方法。我们选择遵循冯等人（2016）提出的一种新的DG有限元微分学框架，并用有限维DG微分算子逼近方程中的无穷维算子。具体来说，我们通过使用扩散项的双风不连续伽辽金（DWDG）公式和对流项的平均离散梯度算子以及标准DG稳定来构造数值方法。我们证明了该方法在对流主导的区域最优收敛。提供了数值结果来支持理论发现。 et.al.|[2404.06490](http://arxiv.org/abs/2404.06490)|null|
|**2024-04-09**|**Uncovering Tidal Treasures: Automated Classification of Faint Tidal Features in DECaLS Data**|潮汐特征是星系形成层次模型的一个关键可观测预测，包含了关于星系性质和历史的丰富信息。LSST和欧几里得等现代广域调查将彻底改变潮汐特征的研究。然而，数据量将远远超过检查每个星系以直观识别特征的能力，从而迫切需要开发自动检测方法。本文对DECaLS调查中的2000个星系进行了视觉分类，将其分为不同的潮汐特征类别：臂、流、壳和漫射。使用这些标签，我们训练了卷积神经网络（CNN）来再现指定的视觉分类。总的来说，我们的网络表现良好，仅在20%的污染情况下，就获得了臂、流、壳和扩散特征实际实例的中值81.1^{+5.8}_{-6.5} $、65.7^{+5.0}_{-8.4}$、91.3^{+6.0}_｛-5.9}$和82.3^{+1.4}_{-7.9}$ 。我们通过使用梯度加权类激活映射分析来突出给定分类的图像上的重要区域，验证了网络对图像的正确分类。这是首次使用细胞神经网络将潮汐特征分类为子类别的演示，它将为识别即将进行的宽视场调查将提供的大量星系样本中不同类别的潮汐特征铺平道路。 et.al.|[2404.06487](http://arxiv.org/abs/2404.06487)|null|
|**2024-04-09**|**GeoDirDock: Guiding Docking Along Geodesic Paths**|这项工作介绍了GeoDirDock（GDD），这是一种新的分子对接方法，提高了配体对接预测的准确性和物理合理性。GDD沿着表示平移、旋转和扭转自由度的多个空间内的测地线路径指导扩散模型的去噪过程。我们的方法利用专家知识来指导生成建模过程，特别是靶向所需的蛋白质-配体相互作用区域。我们证明，GDD在RMSD精度和物理化学姿态逼真度方面显著优于现有的盲对接方法。我们的结果表明，将领域专业知识纳入扩散过程会导致更具生物学相关性的对接预测。此外，我们还通过最大共有亚结构（MCS）对接中的角度转移，探索了GDD在药物发现中进行先导优化的潜力，展示了其准确预测化学相似化合物配体取向的能力。 et.al.|[2404.06481](http://arxiv.org/abs/2404.06481)|null|
|**2024-04-09**|**Magic-Boost: Boost 3D Generation with Mutli-View Conditioned Diffusion**|得益于2D扩散模型的快速发展，3D内容创作最近取得了重大进展。一个有前景的解决方案涉及对预训练的2D扩散模型进行微调，以利用其产生多视图图像的能力，然后通过快速NeRF或大型重建模型等方法将多视图图像提升为精确的3D模型。然而，由于不一致性仍然存在，并且生成的分辨率有限，因此这种方法的生成结果仍然缺乏复杂的纹理和复杂的几何形状。为了解决这个问题，我们提出了Magic Boost，这是一个多视图条件扩散模型，通过短暂的SDS优化（ $\sim15$ min）显著细化了粗略的生成结果。与以前的基于文本或单图像的扩散模型相比，Magic Boost表现出从伪合成的多视图图像中生成高一致性图像的强大能力。它提供了精确的SDS指导，与输入图像的身份非常一致，丰富了初始生成结果的几何结构和纹理中的局部细节。大量实验表明，Magic Boost大大增强了粗略输入，并生成了具有丰富几何和纹理细节的高质量3D资产。（项目页面：https://magic-research.github.io/magic-boost/) et.al.|[2404.06429](http://arxiv.org/abs/2404.06429)|null|
|**2024-04-09**|**ZeST: Zero-Shot Material Transfer from a Single Image**|我们提出了ZeST，一种在给定材料示例图像的情况下将零样本材料转移到输入图像中的对象的方法。ZeST利用现有的扩散适配器从示例图像中提取隐含的材料表示。该表示用于使用预先训练的修复扩散模型在输入图像中的对象上传输材料，其中使用深度估计作为几何线索，使用灰度对象着色作为照明线索。该方法在没有任何训练的情况下在真实图像上工作，从而产生零样本方法。在真实数据集和合成数据集上的定性和定量结果都表明，ZeST输出具有转移材料的真实感图像。我们还展示了ZeST在不同照明下执行多重编辑和稳健材料分配的应用。项目页面：https://ttchengab.github.io/zest et.al.|[2404.06425](http://arxiv.org/abs/2404.06425)|null|
|**2024-04-09**|**Policy-Guided Diffusion**|在许多现实世界的设置中，代理必须从一些先前的行为策略收集的离线数据集中学习。这样的设置自然会导致行为政策和正在训练的目标政策之间的分布转变——需要政策保守主义来避免不稳定和高估偏差。自回归世界模型通过生成综合的政策经验来提供不同的解决方案。然而，在实践中，必须严格截断模型的推出，以避免复合误差。作为另一种选择，我们建议以政策为导向的扩散。我们的方法使用扩散模型来生成行为分布下的整个轨迹，应用目标政策的指导，将综合经验进一步转移到政策上。我们证明，政策引导的扩散模型是目标分布的正则化形式，它平衡了目标和行为政策下的行动可能性，导致了具有高目标政策概率的合理轨迹，同时保持了比离线世界模型基线更低的动力学误差。使用政策引导扩散的综合经验作为真实数据的替代品，我们展示了一系列标准离线强化学习算法和环境的性能显著提高。我们的方法为自回归离线世界模型提供了一种有效的替代方案，为可控生成合成训练数据打开了大门。 et.al.|[2404.06356](http://arxiv.org/abs/2404.06356)|**[link](https://github.com/emptyjackson/policy-guided-diffusion)**|
|**2024-04-09**|**Quantum State Generation with Structure-Preserving Diffusion Model**|本文考虑了量子系统状态的生成建模，提出了一种基于去噪扩散模型的方法。关键贡献是算法创新，它尊重量子态的物理性质。更确切地说，混合态的常用密度矩阵表示必须是复值埃尔米特、正半定和迹矩阵。通用扩散模型或其他生成方法可能无法生成严格满足这些结构约束的数据，即使所有训练数据都满足。为了开发一种具有物理硬连线的机器学习算法，我们利用镜像扩散模型的最新发展，设计了一个以前未考虑的镜像图，以实现严格的结构保持生成。无条件生成和通过无分类器引导的条件生成都被实验证明是有效的，后者甚至能够在看不见的标签上生成新的量子态。 et.al.|[2404.06336](http://arxiv.org/abs/2404.06336)|null|
|**2024-04-09**|**Compensating slice emittance growth in high brightness photoinjectors using sacrificial charge**|在光注入器中实现最大电子束亮度需要对3D束流形状的详细控制和束聚焦的精确调谐。即使在最先进的设计中，由于非线性空间电荷力和部分非污染性导致的片发射度增长通常也是不可忽略的。在这项工作中，我们引入了一种使横向切片相空间线性化的新方法：束流自身电荷分布的牺牲部分，通过枪内高度非线性的空间电荷力形成波裂激波阵面，其下游目的是使所需的束流芯动态线性化。我们证明，适当制备的束的线性化可以通过牺牲冲击前沿的强非层聚焦来实现，而内芯是层聚焦的。这导致了两种分布的自然空间分离：密集的核心被可以准直的牺牲电荷的扩散晕包围。超小型x射线自由电子激光器（UCXFEL）注入器的多目标遗传算法优化采用了这一概念，并用与模拟结果一致的分析模型对其进行了解释。在模拟中，我们展示了100 pC的最终团簇电荷、峰值电流 $\sim 30$a和150 pC的牺牲电荷（阴极发射的总电荷为250 pC），由于空间电荷，归一化发射度增长为$<20$ nm rad。这意味着可实现的最大亮度比现有的FEL注入器设计大大约一个数量级。 et.al.|[2404.06312](http://arxiv.org/abs/2404.06312)|null|
|**2024-04-09**|**NoiseNCA: Noisy Seed Improves Spatio-Temporal Continuity of Neural Cellular Automata**|神经细胞自动机（NCA）是一类细胞自动机，其中更新规则由可以使用梯度下降训练的神经网络参数化。在本文中，我们重点研究用于纹理合成的NCA模型，其中更新规则的灵感来自描述反应扩散系统的偏微分方程（PDE）。为了训练NCA模型，对时空域进行离散化，并使用欧拉积分对PDE进行数值模拟。然而，经过训练的NCA是否真的学习了相应PDE描述的连续动态，还是仅仅对训练中使用的离散化进行了过度拟合，仍然是一个悬而未决的问题。我们在时空离散化接近连续性的极限下研究NCA模型。我们发现，现有的NCA模型往往过于拟合训练离散化，尤其是在初始条件（也称为“种子”）附近。为了解决这个问题，我们提出了一种利用均匀噪声作为初始条件的解决方案。我们证明了我们的方法在保持NCA动力学在广泛的时空粒度上的一致性方面的有效性。我们改进的NCA模型通过允许连续控制模式形成的速度和合成模式的规模，实现了两种新的测试时间相互作用。我们在交互式在线演示中演示了NCA的这一新功能。我们的工作表明，NCA模型可以学习连续动力学，并从动力学系统的角度为NCA研究开辟了新的场所。 et.al.|[2404.06279](http://arxiv.org/abs/2404.06279)|null|
|**2024-04-09**|**A Large-Scale Simulation Method for Neuromorphic Circuits**|分裂算法在凸优化中是公认的，并且是为解决大规模问题而设计的。使用这样的算法来模拟非线性电路网络的行为为神经形态系统的模拟和设计提供了可扩展的方法。对于由具有非线性电阻元件的线性电容器和电感器组成的电路，我们提出了一种分裂，将网络分解为LTI无损分量和静态电阻分量。这种分割具有物理和算法优点，并允许在时域和频域中进行单独的计算。为了证明这种方法的可扩展性，模拟了一个由100个神经元组成的网络，该网络由著名的FitzHugh Nagumo电路建模，具有全扩散耦合。 et.al.|[2404.06255](http://arxiv.org/abs/2404.06255)|null|

<p align=right>(<a href=#updated-on-20240410>back to top</a>)</p>

## NeRF

|Publish Date|Title|Abstract|PDF|Code|
|---|---|---|---|---|
|**2024-04-03**|**A Coupled Neural Field Model for the Standard Consolidation Theory**|标准巩固理论指出，位于海马体的短期记忆能够巩固新皮层的长期记忆。换言之，新皮层在海马体的短暂支持下慢慢学习长期记忆，海马体会快速学习不稳定的记忆。然而，目前尚不清楚这些学习率和记忆时间尺度差异背后的神经生物学机制是什么。在这里，我们提出了一种新的标准巩固理论的建模方法，重点关注其潜在的神经生物学机制。除了突触可塑性和棘突频率适应外，我们的模型还结合了齿状回的成年神经发生以及新皮层和海马体之间的大小差异，我们将其与距离依赖性突触可塑性联系起来。我们还考虑了相关大脑区域的相互关联的空间结构，将上述神经生物学机制纳入耦合的神经场框架中，其中每个区域由具有区域内和区域间连接的单独神经场表示。据我们所知，这是将神经场应用于这一过程的首次尝试。使用数值模拟和数学分析，我们探索了在外部输入的海马重放和检索线索的相位交替时，模型的短期和长期动力学。该外部输入可被编码为单个神经场中的多凸点吸引器模式形式的记忆模式。在该模型中，由于海马记忆模式的突起之间的距离较小，海马记忆模式在新皮质记忆模式之前首先被编码。因此，在短时间尺度上检索新皮层中的输入模式需要由海马体的记忆模式提供额外的输入。新皮质记忆模式在较长的时间内逐渐巩固，直到它们的恢复不再需要海马体的支持。在较长的时间内，神经发生对海马神经场的扰动会抹去海马模式，导致记忆模式只在新皮层中唤起的最终状态。因此，我们模型的动力学成功地再现了标准固结理论的主要特征。这表明，海马体的神经发生和距离依赖性突触可塑性，再加上突触抑制和尖峰频率适应，确实是记忆巩固的关键神经生物学过程。 et.al.|[2404.02938](http://arxiv.org/abs/2404.02938)|null|
|**2024-04-03**|**LiDAR4D: Dynamic Neural Fields for Novel Space-time View LiDAR Synthesis**|尽管神经辐射场（NeRFs）在图像新视图合成（NVS）方面取得了成功，但激光雷达NVS在很大程度上仍未被探索。以前的激光雷达NVS方法采用了图像NVS方法的简单转变，同时忽略了激光雷达点云的动态特性和大规模重建问题。有鉴于此，我们提出了LiDAR4D，这是一种用于新的时空LiDAR视图合成的仅限LiDAR的可微分框架。考虑到稀疏性和大规模特征，我们设计了一种结合多平面和网格特征的4D混合表示，以实现从粗到细的有效重建。此外，我们引入了从点云导出的几何约束，以提高时间一致性。对于激光雷达点云的真实合成，我们结合了光线下降概率的全局优化，以保持跨区域模式。在KITTI-360和NuScenes数据集上进行的大量实验证明了我们的方法在实现几何感知和时间一致的动态重建方面的优越性。代码可在https://github.com/ispc-lab/LiDAR4D. et.al.|[2404.02742](http://arxiv.org/abs/2404.02742)|**[link](https://github.com/ispc-lab/lidar4d)**|
|**2024-04-04**|**Vestibular schwannoma growth prediction from longitudinal MRI by time conditioned neural fields**|前庭神经鞘瘤（VS）是一种良性肿瘤，通常通过MRI检查进行积极监测来治疗。为了进一步帮助临床决策并避免过度治疗，基于纵向成像的肿瘤生长的准确预测是非常可取的。在本文中，我们介绍了DeepGrowth，这是一种深度学习方法，它结合了神经场和递归神经网络，用于前瞻性肿瘤生长预测。在所提出的方法中，每个肿瘤都表示为以低维潜在码为条件的有符号距离函数（SDF）。与之前直接在图像空间中进行肿瘤形状预测的研究不同，我们预测潜在代码，然后从中重建未来的形状。为了处理不规则的时间间隔，我们引入了一个基于ConvLSTM的时间条件递归模块和一种新的时间编码策略，使所提出的模型能够输出随时间变化的肿瘤形状。在内部纵向VS数据集上的实验表明，所提出的模型显著提高了性能（ $\ge 1.6\%%$Dice评分和$\ge0.20$mm95\%Hausdorff距离），特别是对于生长或缩小最多的前20%肿瘤（$\ge4.6\%%$Dice评分和$\ge 0.73$ mm95\%Hausdoff距离）。我们的代码可在~\bull获得{https://github.com/cyjdswx/DeepGrowth} et.al.|[2404.02614](http://arxiv.org/abs/2404.02614)|**[link](https://github.com/cyjdswx/deepgrowth)**|
|**2024-04-02**|**NeRFCodec: Neural Feature Compression Meets Neural Radiance Fields for Memory-Efficient Scene Representation**|神经辐射场（NeRF）的出现极大地影响了三维场景建模和新颖的视图合成。作为一种用于三维场景表示的视觉媒体，具有高率失真性能的压缩是一个永恒的目标。受神经压缩和神经场表示进步的启发，我们提出了NeRFCodec，这是一种端到端的NeRF压缩框架，它集成了非线性变换、量化和熵编码，用于高效记忆的场景表示。由于直接在大规模的NeRF特征平面上训练非线性变换是不切实际的，我们发现，当添加内容特定参数时，可以使用预先训练的神经2D图像编解码器来压缩特征。具体来说，我们重用神经2D图像编解码器，但修改其编码器和解码器头，同时保持预训练解码器的其他部分冻结。这使我们能够通过监督渲染损失和熵损失来训练整个管道，通过更新特定于内容的参数来实现率失真平衡。在测试时，包含潜在代码、特征解码器头和其他辅助信息的比特流被发送用于通信。实验结果表明，我们的方法优于现有的NeRF压缩方法，能够在0.5MB的内存预算下实现高质量的新视图合成。 et.al.|[2404.02185](http://arxiv.org/abs/2404.02185)|null|
|**2024-04-01**|**NeRF-MAE : Masked AutoEncoders for Self Supervised 3D representation Learning for Neural Radiance Fields**|神经领域在计算机视觉和机器人领域表现出色，因为它们能够理解3D视觉世界，如推断语义、几何和动力学。考虑到神经场在从2D图像密集表示3D场景方面的能力，我们提出了一个问题：我们是否可以扩展它们的自监督预训练，特别是使用掩蔽的自动编码器，从姿态RGB图像中生成有效的3D表示。由于将转换器扩展到新型数据模式的惊人成功，我们采用了标准的3D视觉转换器来适应NeRF的独特配方。我们利用NeRF的体积网格作为变压器的密集输入，将其与其他3D表示（如点云）进行对比，在点云中，信息密度可能不均匀，并且表示不规则。由于将掩蔽的自动编码器应用于隐式表示（如NeRF）很困难，我们选择提取通过使用相机轨迹进行采样来规范化跨域场景的显式表示。我们的目标是通过从NeRF的辐射和密度网格中屏蔽随机补丁，并使用标准的3D Swin Transformer来重建屏蔽的补丁。通过这样做，模型可以学习完整场景的语义和空间结构。我们在我们提出的精心策划的姿势RGB数据上对这种表示进行了大规模的预训练，总共超过160万张图像。一旦经过预训练，编码器就用于有效的3D迁移学习。我们针对NeRF的新型自监督预训练NeRF-MAE可扩展性非常好，并提高了在各种具有挑战性的3D任务中的性能。利用未标记的姿态2D数据进行预训练，在Front3D和ScanNet数据集上，NeRF MAE显著优于自监督3D预训练和NeRF场景理解基线，在3D对象检测方面的绝对性能提高超过20%AP50和8%AP25。 et.al.|[2404.01300](http://arxiv.org/abs/2404.01300)|null|
|**2024-04-06**|**Grounding and Enhancing Grid-based Models for Neural Fields**|当代许多研究利用基于网格的模型来表示神经场，但仍然缺乏对基于网格模型的系统分析，阻碍了这些模型的改进。因此，本文介绍了一个基于网格的模型的理论框架。该框架指出，这些模型的逼近和泛化行为是由网格切线核（GTK）决定的，GTK是基于网格的模型的固有性质。所提出的框架有助于对各种基于网格的模型进行一致和系统的分析。此外，引入的框架推动了一种新的基于网格的模型的开发，该模型名为乘法傅立叶自适应网格（MulFAGrid）。数值分析表明，MulFAGrid表现出比其前身更低的泛化界，表明其具有鲁棒的泛化性能。实证研究表明，MulFAGrid在各种任务中都取得了最先进的性能，包括2D图像拟合、3D符号距离场（SDF）重建和新颖的视图合成，表现出了卓越的表示能力。项目网站位于https://sites.google.com/view/cvpr24-2034-submission/home. et.al.|[2403.20002](http://arxiv.org/abs/2403.20002)|null|
|**2024-04-01**|**Efficient 3D Instance Mapping and Localization with Neural Fields**|我们解决了从一系列摆姿势的RGB图像中学习用于3D实例分割的隐式场景表示的问题。为此，我们引入了3DIML，这是一种新的框架，可以有效地学习可以从新的视点渲染的标签字段，以产生视图一致的实例分割掩码。3DIML显著改进了现有的基于隐式场景表示的方法的训练和推理运行时。与现有技术相反，现有技术以自我监督的方式优化神经场，需要复杂的训练过程和损失函数设计，3DIML利用了两阶段过程。第一阶段InstanceMap将前端实例分割模型生成的图像序列的2D分割掩码作为输入，并将图像上的相应掩码与3D标签相关联。然后，在第二阶段InstanceLift中使用这些几乎视图一致的伪标签掩码来监督神经标签字段的训练，该字段对InstanceMap遗漏的区域进行插值并解决歧义。此外，我们介绍了InstanceLoc，它能够在给定训练过的标签字段和现成的图像分割模型的情况下，通过融合两者的输出，实现实例掩码的近实时定位。我们在Replica和ScanNet数据集的序列上评估了3DIML，并证明了在图像序列的温和假设下3DIML的有效性。与现有的质量相当的隐式场景表示方法相比，我们实现了巨大的实际加速，展示了其促进更快、更有效的3D场景理解的潜力。 et.al.|[2403.19797](http://arxiv.org/abs/2403.19797)|null|
|**2024-03-28**|**Neural Fields for 3D Tracking of Anatomy and Surgical Instruments in Monocular Laparoscopic Video Clips**|腹腔镜视频跟踪主要关注两种目标类型：手术器械和解剖结构。前者可用于技能评估，而后者对于虚拟覆盖的投影是必要的。在仪器和解剖跟踪通常被视为两个独立的问题的情况下，在本文中，我们提出了一种同时对所有结构进行联合跟踪的方法。基于单个2D单眼视频剪辑，我们训练神经场来表示连续的时空场景，用于创建至少一帧中可见的所有表面的3D轨迹。由于仪器尺寸较小，它们通常只覆盖图像的一小部分，导致跟踪精度下降。因此，我们建议增强类权重以改善仪器轨迹。我们评估了对腹腔镜胆囊切除术视频片段的跟踪，发现解剖结构和器械的平均跟踪准确率分别为92.4%和87.4%。此外，我们还评估了从该方法的场景重建中获得的深度图的质量。我们表明，这些伪深度具有与最先进的预训练深度估计器相当的质量。在SCARED数据集中的腹腔镜视频上，该方法预测深度的MAE为2.9 mm，相对误差为9.2%。这些结果表明了使用神经场进行腹腔镜场景的单目3D重建的可行性。 et.al.|[2403.19265](http://arxiv.org/abs/2403.19265)|null|
|**2024-03-28**|**From Activation to Initialization: Scaling Insights for Optimizing Neural Fields**|在计算机视觉领域，神经场作为一种利用神经网络进行信号表示的现代工具，已经获得了突出地位。尽管在调整这些网络以解决各种问题方面取得了显著进展，但该领域仍然缺乏一个全面的理论框架。本文旨在通过深入研究初始化和激活之间复杂的相互作用来解决这一差距，为神经领域的稳健优化提供基础。我们的理论见解揭示了网络初始化、架构选择和优化过程之间的深层次联系，强调在设计尖端神经场时需要整体方法。 et.al.|[2403.19205](http://arxiv.org/abs/2403.19205)|null|
|**2024-03-22**|**LATTE3D: Large-scale Amortized Text-To-Enhanced3D Synthesis**|最近的文本到3D生成方法产生了令人印象深刻的3D结果，但需要耗时的优化，每次提示可能需要一个小时。ATT3D等摊销方法同时优化多个提示以提高效率，实现快速的文本到三维合成。然而，它们无法捕捉高频几何体和纹理细节，并且难以缩放到大型提示集，因此泛化能力较差。我们引入LATTE3D，解决了这些限制，以在更大的提示集上实现快速、高质量的生成。我们方法的关键是1）构建可扩展的体系结构，2）在优化过程中通过3D感知扩散先验、形状正则化和模型初始化来利用3D数据，以实现对各种复杂训练提示的鲁棒性。LATTE3D对神经场和纹理表面生成进行摊销，以在单个正向过程中生成高度详细的纹理网格。LATTE3D在400ms内生成3D对象，并可通过快速测试时间优化进一步增强。 et.al.|[2403.15385](http://arxiv.org/abs/2403.15385)|null|

<p align=right>(<a href=#updated-on-20240410>back to top</a>)</p>

[contributors-shield]: https://img.shields.io/github/contributors/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[contributors-url]: https://github.com/Vincentqyw/cv-arxiv-daily/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[forks-url]: https://github.com/Vincentqyw/cv-arxiv-daily/network/members
[stars-shield]: https://img.shields.io/github/stars/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[stars-url]: https://github.com/Vincentqyw/cv-arxiv-daily/stargazers
[issues-shield]: https://img.shields.io/github/issues/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[issues-url]: https://github.com/Vincentqyw/cv-arxiv-daily/issues

