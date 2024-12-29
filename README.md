[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]

## Updated on 2024.12.29
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
|**2024-12-24**|**3DEnhancer: Consistent Multi-View Diffusion for 3D Enhancement**|尽管神经渲染取得了进展，但由于缺乏高质量的3D数据集和多视图扩散模型的固有局限性，视图合成和3D模型生成仅限于低分辨率和次优的多视图一致性。在这项研究中，我们提出了一种新的3D增强管道，称为3DEnhancer，它采用多视图潜在扩散模型来增强粗略的3D输入，同时保持多视图的一致性。我们的方法包括一个姿态感知编码器和一个基于扩散的去噪器，用于细化低质量的多视图图像，以及数据增强和一个具有极线聚合的多视图注意力模块，以保持视图之间一致的高质量3D输出。与现有的基于视频的方法不同，我们的模型支持无缝的多视图增强，提高了不同视角的连贯性。广泛的评估表明，3DEnhancer的性能明显优于现有的方法，可以增强多视图增强和每个实例的3D优化任务。 et.al.|[2412.18565](http://arxiv.org/abs/2412.18565)|null|
|**2024-12-24**|**RSGaussian:3D Gaussian Splatting with LiDAR for Aerial Remote Sensing Novel View Synthesis**|本研究提出了RSGaussian，这是一种用于航空遥感场景的创新型视图合成（NVS）方法，该方法将LiDAR点云作为约束纳入3D高斯散点法，确保高斯分布沿着几何基准生长和分裂，解决了过度生长和浮球问题。此外，该方法为相机模型引入了具有失真参数的坐标变换，以实现LiDAR点云和2D图像之间的像素级对齐，促进异构数据融合，实现航空遥感所需的高精度地理对齐。深度和平面一致性损失被纳入损失函数，以引导高斯向真实的深度和平面表示，显著提高了深度估计的准确性。实验结果表明，我们的方法实现了新的视图合成，在航空遥感数据集下平衡了照片级逼真的视觉质量和高精度的几何估计。最后，我们还建立并开源了一个密集的LiDAR点云数据集及其相应的航空多视图图像AIR-LONGYAN。 et.al.|[2412.18380](http://arxiv.org/abs/2412.18380)|null|
|**2024-12-23**|**FaceLift: Single Image to 3D Head with View Generation and GS-LRM**|我们介绍FaceLift，这是一种前馈方法，用于从单张图像中快速、高质量、360度重建头部。我们的管道首先采用多视图潜在扩散模型，该模型从单个面部输入生成一致的头部侧视图和后视图。这些生成的视图然后作为GS-LRM重建器的输入，该重建器使用高斯斑点生成全面的3D表示。为了训练我们的系统，我们使用合成的3D人头作为集合开发了一个多视图渲染数据集。基于扩散的多视图生成器仅在合成头部图像上进行训练，而GS-LRM重建器在Objaverse上进行初始训练，然后对合成头部数据进行微调。FaceLift擅长保护身份并保持视图之间的一致性。尽管FaceLift仅基于合成数据进行训练，但它对现实世界的图像表现出了出色的泛化能力。通过广泛的定性和定量评估，我们表明FaceLift在3D头部重建方面优于最先进的方法，突出了其在现实世界图像上的实用性和鲁棒性。除了单图像重建外，FaceLift还支持4D新颖视图合成的视频输入，并与2D复活技术无缝集成，以实现3D面部动画。项目页面：https://weijielyu.github.io/FaceLift. et.al.|[2412.17812](http://arxiv.org/abs/2412.17812)|null|
|**2024-12-23**|**Editing Implicit and Explicit Representations of Radiance Fields: A Survey**|近年来，神经辐射场（NeRF）通过提供一种新的体积表示法彻底改变了新颖的视图合成，这种表示法结构紧凑，可提供高质量的图像渲染。然而，编辑这些辐射场的方法比NeRF其他方面的许多改进发展得慢。随着受NeRF启发的基于辐射场的替代表示的最新发展，以及文本到图像模型在全球范围内的普及，出现了许多新的机会和策略来提供辐射场编辑。在本文中，我们对文献中NeRF和其他类似辐射场表示的不同编辑方法进行了全面的调查。我们提出了一种新的分类法，用于根据编辑方法对现有作品进行分类，回顾了开创性的模型，反思了辐射场编辑的当前和潜在的新应用，并在编辑选项和性能方面比较了最先进的方法。 et.al.|[2412.17628](http://arxiv.org/abs/2412.17628)|null|
|**2024-12-23**|**Exploring Dynamic Novel View Synthesis Technologies for Cinematography**|新视角合成（NVS）在电影制作中的应用显示出巨大的前景，特别是通过利用神经辐射场（NeRF）和高斯散斑（GS）。这些方法对真实的3D场景进行建模，能够创建由于设置拓扑或昂贵的设备要求而在现实世界中难以捕捉的新镜头。这项创新还提供了电影拍摄的优势，如平滑的相机运动、虚拟重新拍摄、慢动作效果等。本文探讨了动态NVS，旨在促进模型选择过程。我们通过使用各种NVS模型拍摄的短蒙太奇展示了它的潜力。 et.al.|[2412.17532](http://arxiv.org/abs/2412.17532)|null|
|**2024-12-22**|**GeoTexDensifier: Geometry-Texture-Aware Densification for High-Quality Photorealistic 3D Gaussian Splatting**|3D高斯散点（3DGS）因其逼真和高效的渲染性能，最近在3D导航、虚拟现实（VR）和3D模拟等各个领域引起了广泛关注。3DGS的高质量重建依赖于足够的斑点和这些斑点的合理分布，以适应真实的几何表面和纹理细节，这是一个具有挑战性的问题。我们提出了GeoTexDensifier，这是一种新的几何纹理感知致密化策略，用于重建高质量的高斯斑点，更好地符合场景的几何结构和纹理丰富性。具体来说，我们的GeoTexDensifier框架执行了一种辅助的纹理感知致密化方法，在完全纹理化的区域产生更密集的斑点分布，同时在低纹理区域保持稀疏性，以保持高斯点云的质量。同时，在深度比变化验证检查下，几何感知分割策略采用深度和法线先验来指导分割采样，并滤除初始位置远离其目标拟合的实际几何表面的噪声斑点。在相对单目深度先验的帮助下，这种几何感知验证可以有效地减少散射高斯对最终渲染质量的影响，特别是在纹理较弱或没有足够训练视图的区域。纹理感知致密化和几何感知分裂策略完全结合在一起，以获得一组高质量的高斯斑点。我们在各种数据集上实验了我们的GeoTexDensifier框架，并将我们的新视图合成结果与其他最先进的3DGS方法进行了比较，并进行了详细的定量和定性评估，以证明我们的方法在生成更逼真的3DGS模型方面的有效性。 et.al.|[2412.16809](http://arxiv.org/abs/2412.16809)|null|
|**2024-12-21**|**Topology-Aware 3D Gaussian Splatting: Leveraging Persistent Homology for Optimized Structural Integrity**|高斯散斑（GS）已成为表示离散体积辐射场的关键技术。它利用独特的参数化来减轻场景优化中的计算需求。这项工作引入了拓扑感知3D高斯散布（Topology GS），它解决了当前方法中的两个关键局限性：由于初始几何覆盖不完整而损害的像素级结构完整性，以及由于优化过程中拓扑约束不足而导致的特征级完整性不足。为了克服这些局限性，拓扑GS引入了一种新的插值策略，即局部持久沃罗诺伊插值（LPVI），以及一个基于持久条形码的拓扑聚焦正则化项，称为PersLoss。LPVI利用持久同源性来指导自适应插值，在保持拓扑结构的同时增强低曲率区域的点覆盖。PersLoss通过约束渲染图像拓扑特征之间的距离，将渲染图像的视觉感知相似性与地面真实性对齐。对三种新型视图合成基准的综合实验表明，拓扑GS在PSNR、SSIM和LPIPS指标方面优于现有方法，同时保持了高效的内存使用。本研究开创了拓扑与3D-GS的集成，为该领域的未来研究奠定了基础。 et.al.|[2412.16619](http://arxiv.org/abs/2412.16619)|**[link](https://github.com/amadeusstq/topology-gs)**|
|**2024-12-20**|**EGSRAL: An Enhanced 3D Gaussian Splatting based Renderer with Automated Labeling for Large-Scale Driving Scene**|3D高斯散点（3D GS）因其更快的渲染速度和高质量的新颖视图合成而广受欢迎。一些研究人员探索了使用3D GS重建驾驶场景。然而，这些方法通常依赖于各种数据类型，如深度图、3D框和运动物体的轨迹。此外，合成图像缺乏注释限制了它们在下游任务中的直接应用。为了解决这些问题，我们提出了EGSRAL，这是一种基于3D GS的方法，仅依赖于训练图像而不需要额外的注释。EGSRAL增强了3D GS对动态对象和静态背景建模的能力，并引入了一种用于自动标记的新型适配器，基于现有注释生成相应的注释。我们还为vanilla 3D GS提出了一种分组策略，以解决渲染大规模复杂场景时的透视问题。我们的方法在多个数据集上实现了最先进的性能，而无需任何额外的注释。例如，在nuScenes数据集上，PSNR度量达到29.04。此外，我们的自动标签可以显著提高2D/3D检测任务的性能。代码可在以下网址获得https://github.com/jiangxb98/EGSRAL. et.al.|[2412.15550](http://arxiv.org/abs/2412.15550)|**[link](https://github.com/jiangxb98/egsral)**|
|**2024-12-19**|**SolidGS: Consolidating Gaussian Surfel Splatting for Sparse-View Surface Reconstruction**|高斯飞溅在新颖的视图合成和多视图图像的表面重建方面都取得了令人印象深刻的改进。然而，目前的方法仍然难以使用高斯飞溅从稀疏的视图输入图像中重建高质量的表面。在本文中，我们提出了一种名为SolidGS的新方法来解决这个问题。我们观察到，由于几何渲染中高斯函数的特性，重建的几何在多个视图之间可能会严重不一致。这促使我们通过采用更坚实的核函数来整合所有高斯函数，从而有效地提高了曲面重建质量。在几何正则化和单目法线估计的额外帮助下，我们的方法在稀疏视图曲面重建方面取得了比广泛使用的DTU、Tanks和Temples以及LLFF数据集上的所有高斯溅射方法和神经场方法更优越的性能。 et.al.|[2412.15400](http://arxiv.org/abs/2412.15400)|null|
|**2024-12-19**|**EnvGS: Modeling View-Dependent Appearance with Environment Gaussian**|从2D图像重建现实世界场景中的复杂反射对于实现逼真的新颖视图合成至关重要。利用环境贴图对远距离照明的反射进行建模的现有方法往往难以处理高频反射细节，并且无法考虑近场反射。在这项工作中，我们介绍了EnvGS，这是一种新的方法，它采用一组高斯基元作为显式的3D表示来捕获环境的反射。这些环境高斯基元与基础高斯基元相结合，以对整个场景的外观进行建模。为了高效地渲染这些环境高斯基元，我们开发了一种基于光线跟踪的渲染器，该渲染器利用GPU的RT内核进行快速渲染。这使我们能够共同优化模型，以实现高质量的重建，同时保持实时渲染速度。来自多个真实世界和合成数据集的结果表明，我们的方法产生了更详细的反射，在实时新颖视图合成中实现了最佳的渲染质量。 et.al.|[2412.15215](http://arxiv.org/abs/2412.15215)|null|

<p align=right>(<a href=#updated-on-20241229>back to top</a>)</p>

## 3D Reconstruction

|Publish Date|Title|Abstract|PDF|Code|
|---|---|---|---|---|
|**2024-12-24**|**PartGen: Part-level 3D Generation and Reconstruction with Multi-View Diffusion Models**|文本或图像到3D生成器和3D扫描仪现在可以生成具有高质量形状和纹理的3D资产。这些资产通常由一个单一的融合表示组成，如隐式神经场、高斯混合或网格，没有任何有用的结构。然而，大多数应用程序和创意工作流程都要求资产由几个可以独立操作的有意义的部分组成。为了解决这一差距，我们引入了PartGen，这是一种新颖的方法，可以从文本、图像或非结构化3D对象生成由有意义的部分组成的3D对象。首先，给定生成或渲染的3D对象的多个视图，多视图扩散模型提取一组合理且视图一致的零件分割，将对象划分为零件。然后，第二个多视图扩散模型分别获取每个部分，填充遮挡，并通过将这些完成的视图馈送到3D重建网络来使用它们进行3D重建。这个完成过程考虑了整个对象的上下文，以确保各部分紧密结合。生成完成模型可以弥补因遮挡而丢失的信息；在极端情况下，它可以根据输入的3D资源产生完全不可见的部分的幻觉。我们在生成的和真实的3D资产上评估了我们的方法，并表明它在很大程度上优于分割和零件提取基线。我们还展示了3D零件编辑等下游应用程序。 et.al.|[2412.18608](http://arxiv.org/abs/2412.18608)|null|
|**2024-12-24**|**Resolution-Robust 3D MRI Reconstruction with 2D Diffusion Priors: Diverse-Resolution Training Outperforms Interpolation**|由于3D训练数据的可用性有限，基于深度学习的3D成像，特别是磁共振成像（MRI）具有挑战性。因此，在2D切片上训练的2D扩散模型开始被用于3D MRI重建。然而，正如我们在本文中所展示的，现有的方法适用于固定的体素大小，当体素大小变化时，性能会下降，这在临床实践中经常发生。本文提出并研究了几种利用二维扩散先验进行分辨率鲁棒三维MRI重建的方法。作为这项研究的结果，我们获得了一种基于随机采样二维切片扩散引导正则化的简单分辨率鲁棒变分三维重建方法。与后验采样基线相比，该方法提供了有竞争力的重建质量。为了解决分辨率偏移的敏感性，我们研究了最先进的基于模型的方法，包括高斯飞溅、神经表示和无限维扩散模型，以及一种简单的以数据为中心的方法，在多种分辨率上训练扩散模型。我们的实验表明，基于模型的方法无法缩小3D MRI的性能差距。相比之下，以数据为中心的方法在各种分辨率上训练扩散模型，有效地提供了一种分辨率鲁棒的方法，而不会影响准确性。 et.al.|[2412.18584](http://arxiv.org/abs/2412.18584)|null|
|**2024-12-24**|**Sharper Error Bounds in Late Fusion Multi-view Clustering Using Eigenvalue Proportion**|多视图聚类（MVC）旨在整合来自多个视图的互补信息，以提高聚类性能。后期融合多视图聚类（LFMVC）通过将不同的聚类结果合成为统一的共识，展现出了巨大的潜力。然而，当前的LFMVC方法在噪声和冗余分区方面很困难，并且经常无法捕获视图之间的高阶相关性。为了解决这些局限性，我们提出了一种新的理论框架，利用局部Rademacher复杂性和主特征值比例来分析多核 $k$-means的泛化误差界。我们的分析建立了$\mathcal{O}（1/n）$的收敛率，在$\mathal{O}。基于这一认识，我们提出了一种在多重线性$k$ -means框架内的低通图滤波策略，以减轻噪声和冗余，进一步细化主特征值比例并提高聚类精度。在基准数据集上的实验结果证实，我们的方法在聚类性能和鲁棒性方面优于最先进的方法。相关代码可在以下网址获得https://github.com/csliangdu/GMLKM . et.al.|[2412.18207](http://arxiv.org/abs/2412.18207)|null|
|**2024-12-24**|**A Review of 3D Particle Tracking and Flow Diagnostics Using Digital Holography**|先进的三维（3D）跟踪方法对于研究各种复杂系统中的粒子动力学至关重要，包括多相流、环境和大气科学、胶体科学、生物和医学研究以及工业制造过程。本综述全面总结了使用数字全息术（DH）的3D粒子跟踪和流动诊断。我们首先介绍了DH的原理，并详细讨论了数值重建。然后，该综述探讨了DH中使用的各种硬件设置，包括内联、离轴和双视图或多视图配置，概述了它们的优点和局限性。我们还深入研究了不同的全息图处理方法，分为传统的多步、逆向和基于机器学习的方法，深入了解了它们在多个研究中用于3D粒子跟踪和流动诊断的应用。该综述最后讨论了未来前景，强调了机器学习在实现制造、环境监测和生物科学等不同领域的基于DH的精确粒子跟踪和流动诊断技术方面的重要作用。 et.al.|[2412.18094](http://arxiv.org/abs/2412.18094)|null|
|**2024-12-23**|**Cross-View Referring Multi-Object Tracking**|参考多目标跟踪（RMOT）是当前跟踪领域的一个重要课题。它的任务形式是引导跟踪器跟踪与语言描述匹配的对象。目前的研究主要集中在单视图下的多目标跟踪，指的是一个视图序列或多个不相关的视图序列。然而，在单一视图中，对象的某些外观很容易不可见，导致对象与语言描述的不正确匹配。在这项工作中，我们提出了一个新的任务，称为交叉视图参考多目标跟踪（CRMOT）。它引入了交叉视图来从多个视图中获取对象的外观，避免了RMOT任务中对象外观不可见的问题。CRMOT是一项更具挑战性的任务，即准确跟踪与语言描述匹配的对象，并保持每个交叉视图中对象的身份一致性。为了推进CRMOT任务，我们构建了一个基于CAMPUS和DIVOTrack数据集的交叉视图参考多目标跟踪基准，称为CRTrack。具体来说，它提供了13个不同的场景和221种语言描述。此外，我们提出了一种端到端的交叉视图参考多目标跟踪方法，称为CRTracker。在CRTrack基准上进行的大量实验验证了我们方法的有效性。数据集和代码可在https://github.com/chen-si-jia/CRMOT. et.al.|[2412.17807](http://arxiv.org/abs/2412.17807)|**[link](https://github.com/chen-si-jia/crmot)**|
|**2024-12-21**|**EasyVis2: A Real Time Multi-view 3D Visualization for Laparoscopic Surgery Training Enhanced by a Deep Neural Network YOLOv8-Pose**|EasyVis2是一个专为腹腔镜手术中的免提实时3D可视化而设计的系统。它包含一个配备有一组微型摄像头的手术套管针，这些摄像头插入体腔以提供扩大的视野和手术过程的3D透视图。YOLOv8-Pose是一种复杂的深度神经网络算法，专门用于估计每个单独相机视图中手术器械的位置和方向。随后，使用跨多个视图的相关2D关键点进行3D手术工具姿态估计。这使得能够渲染覆盖在观察到的背景场景上的手术工具的3D表面模型，以实现实时可视化。在这项研究中，我们解释了为新的手术工具开发训练数据集的过程，以定制YoLOv8姿势，同时最大限度地减少标记工作。进行了广泛的实验，将EasyVis2与原始EasyVis进行了比较，结果表明，在相同数量的相机下，新系统提高了3D重建精度并缩短了计算时间。此外，在真实动物组织上进行的3D渲染实验通过显示虚拟侧视图直观地展示了手术工具和组织之间的距离，表明了未来在真实手术中的潜在应用。 et.al.|[2412.16742](http://arxiv.org/abs/2412.16742)|null|
|**2024-12-21**|**LUCES-MV: A Multi-View Dataset for Near-Field Point Light Source Photometric Stereo**|最近，光度立体（PS）领域最大的改进来自于采用可微分体绘制技术，如NeRF或神经SDF，在DiLiGenT MV基准上实现了0.2mm的令人印象深刻的重建误差。然而，虽然有相当大的环境照明对象数据集，如数字孪生目录（DTS），但只有几个小的光度立体数据集，它们往往缺乏具有挑战性的对象（简单、平滑、无纹理）和实用的小形状因子（近场）光设置。为了解决这个问题，我们提出了LUCES-MV，这是第一个为近场点光源光度立体设计的真实世界多视图数据集。我们的数据集包括15个具有不同材料的物体，每个物体都是在不同的光照条件下从距离相机中心30到40厘米的15个LED阵列中成像的。为了促进透明的端到端评估，我们的数据集不仅提供地面真实法线和地面真实对象网格和姿态，还提供灯光和相机校准图像。我们评估了最先进的近场光度立体算法，强调了它们在不同材料和形状复杂性方面的优势和局限性。LUCES-MV数据集为开发更稳健、准确和可扩展的基于光度立体的真实世界3D重建方法提供了重要的基准。 et.al.|[2412.16737](http://arxiv.org/abs/2412.16737)|null|
|**2024-12-21**|**Context-Aware Outlier Rejection for Robust Multi-View 3D Tracking of Similar Small Birds in An Outdoor Aviary**|本文提出了一种使用多摄像机系统对室外鸟舍中的多只鸟类进行鲁棒3D跟踪的新方法。我们的方法通过利用环境地标进行增强的特征匹配和3D重建，解决了视觉上相似的鸟类及其快速运动的挑战。在我们的方法中，异常值根据其最近的地标被拒绝。这使得精确的3D建模和同时跟踪多只鸟成为可能。通过利用环境背景，我们的方法显著提高了视觉上相似的鸟类之间的区分，这是现有跟踪系统中的一个关键障碍。实验结果证明了我们的方法的有效性，在3D重建过程中消除了20%的异常值，匹配精度为97%。3D建模的这种非凡精度转化为对多只鸟类的稳健可靠跟踪，即使在具有挑战性的室外条件下也是如此。我们的工作不仅推进了计算机视觉领域的发展，而且为研究自然环境中的鸟类行为和运动模式提供了宝贵的工具。我们还提供了一个大型的带注释的数据集，包含80只栖息在四个围栏中的鸟类，持续20小时，为计算机视觉、鸟类学家和生态学家的研究人员提供了丰富的试验平台。代码和数据集链接可在https://github.com/airou-lab/3D_Multi_Bird_Tracking et.al.|[2412.16511](http://arxiv.org/abs/2412.16511)|**[link](https://github.com/airou-lab/3d_multi_bird_tracking)**|
|**2024-12-19**|**Generative Multiview Relighting for 3D Reconstruction under Extreme Illumination Variation**|从不同环境中拍摄的照片中重建物体的几何形状和外观是困难的，因为照明和物体外观在捕获的图像中会有所不同。对于外观强烈依赖于观察方向的镜面反射物体来说，这尤其具有挑战性。一些先前的方法使用每图像嵌入向量来模拟图像之间的外观变化，而另一些方法则使用基于物理的渲染来恢复材质和每图像照明。考虑到输入光照的显著变化，这种方法无法忠实地恢复与视图相关的外观，并且往往会产生大部分漫反射结果。我们提出了一种从不同照明下拍摄的图像重建对象的方法，该方法首先使用多视图重新照明扩散模型在单个参考照明下重新照明图像，然后使用对重新照明图像之间剩余的小不一致性具有鲁棒性的辐射场架构重建对象的几何形状和外观。我们在合成和真实数据集上验证了我们提出的方法，并证明它在从极端光照变化下拍摄的图像重建高保真外观方面大大优于现有技术。此外，我们的方法在恢复视图相关的“闪亮”外观方面特别有效，这些外观无法通过现有方法重建。 et.al.|[2412.15211](http://arxiv.org/abs/2412.15211)|null|
|**2024-12-20**|**GURecon: Learning Detailed 3D Geometric Uncertainties for Neural Surface Reconstruction**|神经表面表示在新颖的视图合成和3D重建领域取得了显著的成功。然而，在没有地面真实网格的情况下评估3D重建的几何质量仍然是一个重大挑战，因为其基于渲染的优化过程以及外观和几何体与光度损失的纠缠学习。本文提出了一种新的框架，即GURecon，它基于几何一致性为神经曲面建立了一个几何不确定性场。与依赖于基于渲染的测量的现有方法不同，GURecon为重建表面建模了一个连续的3D不确定性场，并通过在线蒸馏方法学习，而无需引入真实的几何信息进行监督。此外，为了减轻光照对几何一致性的干扰，学习并利用解耦场来微调不确定性场。在各种数据集上的实验证明了GURecon在建模3D几何不确定性方面的优越性，以及它对各种神经表面表示的即插即用扩展和对增量重建等下游任务的改进。代码和补充材料可在项目网站上获得：https://zju3dv.github.io/GURecon/. et.al.|[2412.14939](http://arxiv.org/abs/2412.14939)|null|

<p align=right>(<a href=#updated-on-20241229>back to top</a>)</p>

## Diffusion

|Publish Date|Title|Abstract|PDF|Code|
|---|---|---|---|---|
|**2024-12-24**|**PartGen: Part-level 3D Generation and Reconstruction with Multi-View Diffusion Models**|文本或图像到3D生成器和3D扫描仪现在可以生成具有高质量形状和纹理的3D资产。这些资产通常由一个单一的融合表示组成，如隐式神经场、高斯混合或网格，没有任何有用的结构。然而，大多数应用程序和创意工作流程都要求资产由几个可以独立操作的有意义的部分组成。为了解决这一差距，我们引入了PartGen，这是一种新颖的方法，可以从文本、图像或非结构化3D对象生成由有意义的部分组成的3D对象。首先，给定生成或渲染的3D对象的多个视图，多视图扩散模型提取一组合理且视图一致的零件分割，将对象划分为零件。然后，第二个多视图扩散模型分别获取每个部分，填充遮挡，并通过将这些完成的视图馈送到3D重建网络来使用它们进行3D重建。这个完成过程考虑了整个对象的上下文，以确保各部分紧密结合。生成完成模型可以弥补因遮挡而丢失的信息；在极端情况下，它可以根据输入的3D资源产生完全不可见的部分的幻觉。我们在生成的和真实的3D资产上评估了我们的方法，并表明它在很大程度上优于分割和零件提取基线。我们还展示了3D零件编辑等下游应用程序。 et.al.|[2412.18608](http://arxiv.org/abs/2412.18608)|null|
|**2024-12-24**|**DrivingGPT: Unifying Driving World Modeling and Planning with Multi-modal Autoregressive Transformers**|基于世界模型的搜索和规划被广泛认为是实现人类物理智能的一条有前景的道路。然而，目前的驾驶世界模型主要依赖于视频扩散模型，该模型专门用于视觉生成，但缺乏将其他模式（如动作）结合起来的灵活性。相比之下，自回归变换器在建模多模态数据方面表现出了卓越的能力。我们的工作旨在将驾驶模型仿真和轨迹规划统一到一个单一的序列建模问题中。我们引入了一种基于交错图像和动作标记的多模式驾驶语言，并开发了DrivingGPT，通过标准的下一个标记预测来学习联合世界建模和规划。我们的DrivingGPT在动作条件视频生成和端到端规划方面表现出色，在大规模nuPlan和NAVSIM基准测试中表现优于强大的基线。 et.al.|[2412.18607](http://arxiv.org/abs/2412.18607)|null|
|**2024-12-24**|**Explaining in Diffusion: Explaining a Classifier Through Hierarchical Semantics with Text-to-Image Diffusion Models**|分类器是许多计算机视觉任务中的重要组成部分，是各种应用程序中使用的各种模型的基础支柱。然而，理解分类器的决策过程仍然是一个重大挑战。我们提出了DiffEx，这是一种利用文本到图像扩散模型的能力来解释分类器决策的新方法。与传统的基于GAN的可解释性模型不同，传统的GAN仅限于简单的单概念分析，通常需要为每个分类器训练一个新模型，我们的方法可以解释专注于单个概念（如人脸或动物）的分类器，以及处理涉及多个概念的复杂场景的分类器。DiffEx使用视觉语言模型来创建语义的层次列表，使用户不仅可以识别对分类器的总体语义影响（例如，面部分类器中的“胡须”语义），还可以识别它们的子类型，如“山羊胡子”或“巴尔博”胡子。我们的实验表明，与GAN对应物相比，DiffEx能够覆盖更广泛的语义范围，提供了一种分层工具，可以更详细、更细粒度地理解分类器决策。 et.al.|[2412.18604](http://arxiv.org/abs/2412.18604)|null|
|**2024-12-24**|**DiTCtrl: Exploring Attention Control in Multi-Modal Diffusion Transformer for Tuning-Free Multi-Prompt Longer Video Generation**|Sora类视频生成模型在多模扩散变换器MM-DiT架构方面取得了显著进展。然而，当前的视频生成模型主要关注单个提示，难以生成具有多个连续提示的连贯场景，以更好地反映现实世界的动态场景。虽然一些开创性的工作探索了多提示视频生成，但他们面临着重大挑战，包括严格的训练数据要求、弱提示跟踪和不自然的转换。为了解决这些问题，我们首次提出了在MM-DiT架构下无需训练的多提示视频生成方法DiTCtrl。我们的核心思想是将多提示视频生成任务视为具有平滑过渡的时间视频编辑。为了实现这一目标，我们首先分析了MM-DiT的注意力机制，发现3D全注意力的行为与UNet类扩散模型中的交叉/自我注意力块的行为相似，通过注意力共享实现了跨不同提示的掩模引导精确语义控制，以生成多提示视频。基于我们的精心设计，DiTCtrl生成的视频在无需额外训练的情况下，在多个连续提示下实现了平滑的过渡和一致的物体运动。此外，我们还介绍了MPVBench，这是一个专门为多提示视频生成设计的新基准，用于评估多提示生成的性能。大量实验表明，我们的方法无需额外训练即可实现最先进的性能。 et.al.|[2412.18597](http://arxiv.org/abs/2412.18597)|**[link](https://github.com/tencentarc/ditctrl)**|
|**2024-12-24**|**LatentCRF: Continuous CRF for Efficient Latent Diffusion**|潜在扩散模型（LDM）可以生成高质量、逼真的图像，然而，多次昂贵的推理迭代所产生的延迟可能会限制其适用性。我们引入了LatentCRF，这是一个连续的条件随机场（CRF）模型，作为神经网络层实现，对LDM中潜在向量之间的空间和语义关系进行建模。通过用我们的轻量级LatentCRAF替换一些计算密集型LDM推理迭代，我们实现了质量、速度和多样性之间的卓越平衡。与全LDM相比，我们在不损失图像质量或多样性的情况下将推理效率提高了33%。LatentCRF是一个简单的插件，不需要修改LDM。 et.al.|[2412.18596](http://arxiv.org/abs/2412.18596)|null|
|**2024-12-24**|**Resolution-Robust 3D MRI Reconstruction with 2D Diffusion Priors: Diverse-Resolution Training Outperforms Interpolation**|由于3D训练数据的可用性有限，基于深度学习的3D成像，特别是磁共振成像（MRI）具有挑战性。因此，在2D切片上训练的2D扩散模型开始被用于3D MRI重建。然而，正如我们在本文中所展示的，现有的方法适用于固定的体素大小，当体素大小变化时，性能会下降，这在临床实践中经常发生。本文提出并研究了几种利用二维扩散先验进行分辨率鲁棒三维MRI重建的方法。作为这项研究的结果，我们获得了一种基于随机采样二维切片扩散引导正则化的简单分辨率鲁棒变分三维重建方法。与后验采样基线相比，该方法提供了有竞争力的重建质量。为了解决分辨率偏移的敏感性，我们研究了最先进的基于模型的方法，包括高斯飞溅、神经表示和无限维扩散模型，以及一种简单的以数据为中心的方法，在多种分辨率上训练扩散模型。我们的实验表明，基于模型的方法无法缩小3D MRI的性能差距。相比之下，以数据为中心的方法在各种分辨率上训练扩散模型，有效地提供了一种分辨率鲁棒的方法，而不会影响准确性。 et.al.|[2412.18584](http://arxiv.org/abs/2412.18584)|null|
|**2024-12-24**|**Relativistic Lévy processes**|在这篇文章中，我们研究了如何在狭义相对论中正确描述独立和同分布随机速度之和。我们推导出了在相对论速度加法下稳定的一维速度概率分布。在给定的系统中，这允许根据分布在原点的凹度和测量相对论速度的概率来识别不同的物理状态。这些特征提供了一种在实际实验中评估随机相对论效应相关性的协议。作为例子，我们发现与之前关于重离子扩散的结果一致，并表明我们的发现与反质子冷却测量中观察到的动量偏差分布一致。 et.al.|[2412.18581](http://arxiv.org/abs/2412.18581)|null|
|**2024-12-24**|**A mathematical framework for modelling CLMM dynamics in continuous time**|本文开发了一个严格的数学框架，用于在连续时间内分析去中心化金融（DeFi）中的集中流动性做市商（CLMM）。我们将流动性状况的演变建模为度量值过程，并描述了其在连续交易下的动态。我们的分析包括CLMM的两个关键方面：集中流动性提供的机制和套利者的战略行为。我们研究了三种不同的套利模型——近视、有限期和具有折扣和遍历控制的无限期——并推导出了每种情况下最优套利策略的闭式解。重要的是，我们证明了交易费用的存在从根本上限制了可接受的价格过程，因为费用的包含排除了价格过程中扩散项的存在，以避免无限费用的产生。这一发现对CLMM设计和市场效率具有重要意义。 et.al.|[2412.18580](http://arxiv.org/abs/2412.18580)|null|
|**2024-12-24**|**3DEnhancer: Consistent Multi-View Diffusion for 3D Enhancement**|尽管神经渲染取得了进展，但由于缺乏高质量的3D数据集和多视图扩散模型的固有局限性，视图合成和3D模型生成仅限于低分辨率和次优的多视图一致性。在这项研究中，我们提出了一种新的3D增强管道，称为3DEnhancer，它采用多视图潜在扩散模型来增强粗略的3D输入，同时保持多视图的一致性。我们的方法包括一个姿态感知编码器和一个基于扩散的去噪器，用于细化低质量的多视图图像，以及数据增强和一个具有极线聚合的多视图注意力模块，以保持视图之间一致的高质量3D输出。与现有的基于视频的方法不同，我们的模型支持无缝的多视图增强，提高了不同视角的连贯性。广泛的评估表明，3DEnhancer的性能明显优于现有的方法，可以增强多视图增强和每个实例的3D优化任务。 et.al.|[2412.18565](http://arxiv.org/abs/2412.18565)|null|
|**2024-12-24**|**On the fractional approach to quadratic nonlinear parabolic systems**|我们介绍了一个由拉普拉斯算子的分数幂定义的具有二次非线性项和扩散项的抛物方程的一般耦合系统。我们开发了一种方法，在Sobolev空间的强拓扑中建立分数扩散情况到经典扩散情况的严格收敛性，其显式收敛率揭示了一些意想不到的现象。这些结果适用于一般系统中包含的几个相关的现实世界模型，如Navier-Stokes方程、磁流体动力学方程、Boussinesq系统和Keller-Segel系统。对于这些特定的模型，这种分数方法是由之前的数值和实验研究进一步推动的。 et.al.|[2412.18473](http://arxiv.org/abs/2412.18473)|null|

<p align=right>(<a href=#updated-on-20241229>back to top</a>)</p>

## NeRF

|Publish Date|Title|Abstract|PDF|Code|
|---|---|---|---|---|
|**2024-12-24**|**PartGen: Part-level 3D Generation and Reconstruction with Multi-View Diffusion Models**|文本或图像到3D生成器和3D扫描仪现在可以生成具有高质量形状和纹理的3D资产。这些资产通常由一个单一的融合表示组成，如隐式神经场、高斯混合或网格，没有任何有用的结构。然而，大多数应用程序和创意工作流程都要求资产由几个可以独立操作的有意义的部分组成。为了解决这一差距，我们引入了PartGen，这是一种新颖的方法，可以从文本、图像或非结构化3D对象生成由有意义的部分组成的3D对象。首先，给定生成或渲染的3D对象的多个视图，多视图扩散模型提取一组合理且视图一致的零件分割，将对象划分为零件。然后，第二个多视图扩散模型分别获取每个部分，填充遮挡，并通过将这些完成的视图馈送到3D重建网络来使用它们进行3D重建。这个完成过程考虑了整个对象的上下文，以确保各部分紧密结合。生成完成模型可以弥补因遮挡而丢失的信息；在极端情况下，它可以根据输入的3D资源产生完全不可见的部分的幻觉。我们在生成的和真实的3D资产上评估了我们的方法，并表明它在很大程度上优于分割和零件提取基线。我们还展示了3D零件编辑等下游应用程序。 et.al.|[2412.18608](http://arxiv.org/abs/2412.18608)|null|
|**2024-12-23**|**S-INF: Towards Realistic Indoor Scene Synthesis via Scene Implicit Neural Field**|基于学习的方法在3D室内场景合成（ISS）中越来越受欢迎，显示出优于传统基于优化的方法的性能。这些基于学习的方法通常使用生成模型在简单但明确的场景表示上对分布进行建模。然而，由于过于简单的显式表示忽略了详细信息，并且缺乏场景内多模态关系的指导，大多数基于学习的方法都难以生成具有逼真对象排列和风格的室内场景。本文介绍了一种新的室内场景合成方法——场景隐式神经场（S-INF），旨在学习多模态关系的有意义表示，以提高室内场景合成的真实感。S-INF假设场景布局通常与对象详细信息有关。它将多模态关系分解为场景布局关系和详细对象关系，然后通过隐式神经场（INF）将它们融合在一起。通过学习专门的场景布局关系并将其投影到S-INF中，我们实现了场景布局的真实生成。此外，S-INF通过可微分渲染捕获密集而详细的对象关系，确保对象之间的风格一致性。通过在基准3D-FRONT数据集上的广泛实验，我们证明了我们的方法在不同类型的ISS下始终达到最先进的性能。 et.al.|[2412.17561](http://arxiv.org/abs/2412.17561)|**[link](https://github.com/zixiliang/s-inf)**|
|**2024-12-22**|**HyperNet Fields: Efficiently Training Hypernetworks without Ground Truth by Learning Weight Trajectories**|为了有效地适应大型模型或训练神经表示的生成模型，超网络引起了人们的兴趣。虽然超级网络工作良好，但训练它们很麻烦，而且通常需要为每个样本进行地面实况优化的权重。然而，获得这些权重中的每一个都是一个需要训练的训练问题，例如，适应权重，甚至是超网络回归的整个神经场。在这项工作中，我们提出了一种训练超网络的方法，而不需要任何每个样本的地面真实值。我们的关键思想是学习一个超网络“场”，并估计网络权重训练的整个轨迹，而不是简单地估计其收敛状态。换句话说，我们向超网络引入了一个额外的输入，即收敛状态，这使它成为一个神经场，对任务网络的整个收敛路径进行建模。这样做的一个关键好处是，在任何收敛状态下，估计权重的梯度都必须与原始任务的梯度相匹配——仅此约束就足以训练超网络场。我们通过个性化图像生成和从图像和点云进行3D形状重建的任务来证明我们的方法的有效性，在没有任何样本地面真实性的情况下展示了具有竞争力的结果。 et.al.|[2412.17040](http://arxiv.org/abs/2412.17040)|null|
|**2024-12-20**|**CCNDF: Curvature Constrained Neural Distance Fields from 3D LiDAR Sequences**|神经距离场（NDF）已成为解决3D计算机视觉和图形下游问题的有力工具。虽然在从各种传感器数据中学习NDF方面取得了重大进展，但需要注意的一个关键方面是在训练过程中对神经场的监督，因为地面真实NDF不适用于大规模户外场景。以往的工作利用各种形式的预期符号距离来指导模型学习。然而，这些方法通常需要更多地关注表面几何形状的关键考虑因素，并且仅限于小规模实施。为此，我们提出了一种利用带符号距离场的二阶导数来改进神经场学习的新方法。我们的方法通过准确估计符号距离来解决局限性，从而更全面地了解底层几何。为了评估我们的方法的有效性，我们对NDF的主要应用领域——测绘和定位任务的流行方法进行了比较评估。我们的结果证明了所提出方法的优越性，突出了其在计算机视觉和图形应用中提高神经距离场能力的潜力。 et.al.|[2412.15909](http://arxiv.org/abs/2412.15909)|null|
|**2024-12-19**|**SolidGS: Consolidating Gaussian Surfel Splatting for Sparse-View Surface Reconstruction**|高斯飞溅在新颖的视图合成和多视图图像的表面重建方面都取得了令人印象深刻的改进。然而，目前的方法仍然难以使用高斯飞溅从稀疏的视图输入图像中重建高质量的表面。在本文中，我们提出了一种名为SolidGS的新方法来解决这个问题。我们观察到，由于几何渲染中高斯函数的特性，重建的几何在多个视图之间可能会严重不一致。这促使我们通过采用更坚实的核函数来整合所有高斯函数，从而有效地提高了曲面重建质量。在几何正则化和单目法线估计的额外帮助下，我们的方法在稀疏视图曲面重建方面取得了比广泛使用的DTU、Tanks和Temples以及LLFF数据集上的所有高斯溅射方法和神经场方法更优越的性能。 et.al.|[2412.15400](http://arxiv.org/abs/2412.15400)|null|
|**2024-12-19**|**LiftRefine: Progressively Refined View Synthesis from 3D Lifting with Volume-Triplane Representations**|我们提出了一种新的视图合成方法，通过从单个或少数视图输入图像合成3D神经场。为了解决图像到3D生成问题的不适定性质，我们设计了一种两阶段方法，该方法涉及重建模型和用于视图合成的扩散模型。我们的重建模型首先将一个或多个输入图像从体积提升到3D空间，作为粗尺度3D表示，然后是三平面作为细尺度3D表示。为了减轻遮挡区域的模糊性，我们的扩散模型会在三个平面的渲染图像中产生缺失细节的幻觉。然后，我们引入了一种新的渐进式细化技术，该技术迭代地应用重建和扩散模型来逐步合成新的视图，提高了3D表示及其渲染的整体质量。实证评估表明，我们的方法在合成SRN-Car数据集、野外CO3D数据集和大规模Objaverse数据集上优于最先进的方法，同时实现了采样效率和多视图一致性。 et.al.|[2412.14464](http://arxiv.org/abs/2412.14464)|null|
|**2024-12-18**|**Level-Set Parameters: Novel Representation for 3D Shape Analysis**|3D形状分析主要集中在点云和网格的传统3D表示上，但这些数据的离散性使得分析容易受到输入分辨率变化的影响。神经场的最新发展从带符号距离函数中引入了水平集参数，作为3D形状的新颖、连续和数值表示，其中形状表面被定义为这些函数的零水平集。这促使我们将形状分析从传统的3D数据扩展到这些新的参数数据。由于水平集参数不是类似欧几里德的点云，我们通过将它们表示为伪正态分布来建立不同形状之间的相关性，并从相应的数据集中预先学习分布。为了进一步探索具有形状变换的水平集参数，我们建议将这些参数的子集设置在旋转和平移上，并使用超网络生成它们。与使用传统数据相比，这简化了与姿势相关的形状分析。我们通过在形状分类（任意姿态）、检索和6D对象姿态估计中的应用，展示了新表示法的前景。本研究中的代码和数据见https://github.com/EnyaHermite/LevelSetParamData. et.al.|[2412.13502](http://arxiv.org/abs/2412.13502)|null|
|**2024-12-13**|**Neural Vector Tomography for Reconstructing a Magnetization Vector Field**|矢量断层重建的离散化技术容易在重建中产生伪影。随着噪声量的增加，这些重建的质量可能会进一步恶化。在这项工作中，我们使用平滑神经场对底层向量场进行建模。由于神经网络中的激活函数可以被选择为平滑的，并且域不再像素化，因此即使在存在噪声的情况下，该模型也能得到高质量的重建。在我们具有潜在的全局连续对称性的情况下，我们发现神经网络比现有技术大大提高了重建的准确性。 et.al.|[2412.09927](http://arxiv.org/abs/2412.09927)|null|
|**2024-12-12**|**PBR-NeRF: Inverse Rendering with Physics-Based Neural Fields**|我们使用基于物理的渲染（PBR）理论的神经辐射场（NeRF）方法来解决3D重建中的不适定逆渲染问题，称为PBR-NeRF。我们的方法解决了大多数NeRF和3D高斯散斑方法的一个关键局限性：它们在不建模场景材质和照明的情况下估计与视图相关的外观。为了解决这一局限性，我们提出了一种能够联合估计场景几何形状、材质和照明的逆渲染（IR）模型。我们的模型建立在最近基于NeRF的IR方法的基础上，但关键是引入了两种新的基于物理的先验，更好地约束了IR估计。我们的先验被严格地表述为直观的损失项，在不影响新颖视图合成质量的情况下实现了最先进的材料估计。我们的方法很容易适应其他需要材料估计的逆渲染和3D重建框架。我们展示了将当前的神经渲染方法扩展到完全建模场景属性的重要性，而不仅仅是几何和视图相关的外观。代码可在以下网址公开获取https://github.com/s3anwu/pbrnerf et.al.|[2412.09680](http://arxiv.org/abs/2412.09680)|**[link](https://github.com/s3anwu/pbrnerf)**|
|**2024-12-12**|**Mixture of neural fields for heterogeneous reconstruction in cryo-EM**|低温电子显微镜（Cryo-EM）是一种用于蛋白质结构测定的实验技术，可以在接近生理环境的情况下对大分子的集合进行成像。虽然最近的进展能够重建单个生物分子复合物的动态构象，但目前的方法并不能充分模拟具有混合构象和成分异质性的样品。特别是，包含多种蛋白质混合物的数据集需要联合推断结构、姿势、组成类别和构象状态以进行3D重建。在这里，我们提出了Hydra，这是一种通过参数化K个神经场之一产生的结构来完全从头计算模拟构象和组成异质性的方法。我们采用了一种新的基于似然的损失函数，并证明了我们的方法在由具有高度构象变异的蛋白质混合物组成的合成数据集上的有效性。我们还在含有不同蛋白质复合物混合物的细胞裂解物的实验数据集上演示了Hydra。Hydra扩展了非均匀重建方法的表现力，从而将冷冻EM的范围扩大到越来越复杂的样本。 et.al.|[2412.09420](http://arxiv.org/abs/2412.09420)|null|

<p align=right>(<a href=#updated-on-20241229>back to top</a>)</p>

[contributors-shield]: https://img.shields.io/github/contributors/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[contributors-url]: https://github.com/Vincentqyw/cv-arxiv-daily/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[forks-url]: https://github.com/Vincentqyw/cv-arxiv-daily/network/members
[stars-shield]: https://img.shields.io/github/stars/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[stars-url]: https://github.com/Vincentqyw/cv-arxiv-daily/stargazers
[issues-shield]: https://img.shields.io/github/issues/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[issues-url]: https://github.com/Vincentqyw/cv-arxiv-daily/issues

