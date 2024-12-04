[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]

## Updated on 2024.12.04
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
|**2024-11-29**|**DeSplat: Decomposed Gaussian Splatting for Distractor-Free Rendering**|高斯飞溅技术使静态3D环境中的快速新颖视图合成成为可能。然而，重建现实世界的环境仍然具有挑战性，因为干扰物或遮挡物打破了精确3D重建所需的多视图一致性假设。大多数现有方法依赖于来自预训练模型的外部语义信息，在预处理步骤或优化过程中引入了额外的计算开销。在这项工作中，我们提出了一种新的方法DeSplat，该方法纯粹基于高斯基元的体绘制直接分离干扰物和静态场景元素。我们在每个相机视图中初始化高斯分布，以重建视图特定的干扰物，从而在阿尔法合成阶段分别对静态3D场景和干扰物进行建模。DeSplat实现了静态元素和干扰物的明确场景分离，在不牺牲渲染速度的情况下，实现了与先前无干扰物方法相当的结果。我们在三个基准数据集上证明了DeSplat在无干扰的新颖视图合成中的有效性。请访问项目网站https://aaltoml.github.io/desplat/. et.al.|[2411.19756](http://arxiv.org/abs/2411.19756)|null|
|**2024-12-02**|**GausSurf: Geometry-Guided 3D Gaussian Splatting for Surface Reconstruction**|3D高斯散斑在具有实时渲染功能的新型视图合成中取得了令人印象深刻的性能。然而，使用3D高斯重建具有精细细节的高质量表面仍然是一项具有挑战性的任务。在这项工作中，我们介绍了GausSurf，这是一种新的高质量表面重建方法，在场景的纹理丰富区域采用多视图一致性的几何指导，在纹理较少的区域采用正常先验。我们观察到，一个场景主要可以分为两个主要区域：1）纹理丰富的区域和2）纹理较少的区域。为了在纹理丰富的区域加强多视图一致性，我们通过结合传统的基于补丁匹配的多视图立体（MVS）方法来指导迭代方案中的几何优化，从而提高重建质量。该方案允许高斯优化和补丁匹配细化之间的相互强化，从而显著提高了重建结果并加速了训练过程。同时，对于无纹理区域，我们利用预训练的正态估计模型中的正态先验来指导优化。对DTU和Tanks and Temples数据集的广泛实验表明，我们的方法在重建质量和计算时间方面超越了最先进的方法。 et.al.|[2411.19454](http://arxiv.org/abs/2411.19454)|null|
|**2024-11-28**|**AGS-Mesh: Adaptive Gaussian Splatting and Meshing with Geometric Priors for Indoor Room Reconstruction Using Smartphones**|几何先验通常用于增强3D重建。随着许多智能手机配备低分辨率深度传感器，以及现成的单目几何估计器的普及，将几何先验作为正则化信号在3D视觉任务中已变得普遍。然而，对于高度详细的几何形状，移动设备的深度估计的准确性通常很差，单目估计器的多视图一致性和精度也很差。在这项工作中，我们提出了一种高斯散斑法的联合表面深度和法线细化方法，用于室内场景的精确3D重建。我们开发了监督策略，通过在优化过程中比较先验的一致性，自适应地过滤低质量深度和正常估计。我们在先验估计具有高度不确定性或模糊性的区域减轻正则化。我们的滤波策略和优化设计表明，在具有挑战性的室内数据集上，基于3D和2D高斯散斑的方法在网格估计和新颖的视图合成方面都有显著改进。此外，我们还探索了使用替代网格策略进行更精细的几何提取。我们开发了一种受TSDF和基于八叉树的等值面提取启发的尺度感知网格策略，与其他常用的开源网格工具相比，该策略可以从高斯模型中恢复出更精细的细节。我们的代码发布于https://xuqianren.github.io/ags_mesh_website/. et.al.|[2411.19271](http://arxiv.org/abs/2411.19271)|null|
|**2024-11-28**|**Gaussians-to-Life: Text-Driven Animation of 3D Gaussian Splatting Scenes**|最先进的新颖视图合成方法在静态3D场景的多视图捕获中取得了令人印象深刻的结果。然而，重建的场景仍然缺乏“活力”，这是创造引人入胜的3D体验的关键组成部分。最近，新颖的视频扩散模型生成了具有复杂运动的逼真视频，并支持2D图像的动画，但由于缺乏多视图一致性，它们不能天真地用于3D场景的动画制作。为了给静态世界注入活力，我们提出了Gaussians2Life，这是一种在高斯散斑表示中为高质量3D场景的部分设置动画的方法。我们的主要想法是利用强大的视频扩散模型作为我们模型的生成组件，并将其与强大的技术相结合，将2D视频提升为有意义的3D运动。我们发现，与先前的工作相比，这可以实现复杂的、预先存在的3D场景的逼真动画，并进一步实现各种对象类的动画，而相关工作主要集中在基于先前的角色动画或单个3D对象上。我们的模型能够为任意场景创建一致的沉浸式3D体验。 et.al.|[2411.19233](http://arxiv.org/abs/2411.19233)|**[link](https://github.com/wimmerth/gaussians2life)**|
|**2024-12-02**|**Differentiable Voxel-based X-ray Rendering Improves Sparse-View 3D CBCT Reconstruction**|我们提出了DiffVox，这是一种用于锥束计算机断层扫描（CBCT）重建的自监督框架，通过使用基于物理的可微X射线渲染直接优化体素网格表示。此外，我们还研究了渲染器中X射线图像形成模型的不同实现如何影响3D重建和新视图合成的质量。当与我们的正则化基于体素的学习框架相结合时，我们发现在渲染器中使用离散比尔-朗伯定律进行X射线衰减的精确实现优于广泛使用的迭代CBCT重建算法和现代神经场方法，特别是在只有少数输入视图的情况下。因此，我们用更少的X射线重建高保真3D CBCT体积，从而可能减少电离辐射暴露并提高诊断实用性。我们的实施可在https://github.com/hossein-momeni/DiffVox. et.al.|[2411.19224](http://arxiv.org/abs/2411.19224)|**[link](https://github.com/hossein-momeni/diffvox)**|
|**2024-11-28**|**SuperGaussians: Enhancing Gaussian Splatting Using Primitives with Spatially Varying Colors**|高斯散点在基于高斯显式表示的多视图重建中显示出令人印象深刻的结果。然而，当前的高斯基元只有一个依赖于视图的颜色和不透明度来表示场景的外观和几何体，从而导致不紧凑的表示。本文介绍了一种称为超高斯的新方法，该方法利用单个高斯基元中空间变化的颜色和不透明度来提高其表示能力。我们已经实现了双线性插值、可移动核，甚至微小的神经网络作为空间变化函数。定量和定性实验结果表明，所有三个函数都优于基线，最好的可移动内核在多个数据集上实现了卓越的新颖视图合成性能，突显了空间变化函数的巨大潜力。 et.al.|[2411.18966](http://arxiv.org/abs/2411.18966)|**[link](https://github.com/Xrvitd/SuperGaussians)**|
|**2024-11-27**|**CAT4D: Create Anything in 4D with Multi-View Video Diffusion Models**|我们介绍了CAT4D，这是一种从单眼视频创建4D（动态3D）场景的方法。CAT4D利用在各种数据集组合上训练的多视图视频扩散模型，在任何指定的相机姿态和时间戳下实现新颖的视图合成。结合一种新颖的采样方法，该模型可以将单个单眼视频转换为多视图视频，通过优化可变形的3D高斯表示实现稳健的4D重建。我们在新颖的视图合成和动态场景重建基准上展示了具有竞争力的性能，并强调了从真实或生成的视频生成4D场景的创造性能力。有关结果和交互式演示，请参阅我们的项目页面：\url{cat-4d.github.io}。 et.al.|[2411.18613](http://arxiv.org/abs/2411.18613)|null|
|**2024-11-27**|**SmileSplat: Generalizable Gaussian Splats for Unconstrained Sparse Images**|稀疏多视图图像可以通过广义高斯散斑方法学习来预测显式辐射场，在不需要地面实况相机参数作为输入的情况下，可以在现实生活中实现更广泛的应用前景。本文提出了一种新的可推广高斯散斑方法SmileSplat，用于重建仅需要无约束稀疏多视图图像的不同场景的像素对齐高斯表面。首先，基于多头高斯回归解码器预测高斯曲面，该解码器可以用较少的自由度表示，但具有更好的多视图一致性。此外，基于高质量的法向量先验，高斯曲面的法向量得到了增强。其次，基于所提出的束调整高斯散斑模块，优化高斯和相机参数（包括外部和内部参数），以获得高质量的高斯辐射场，用于新的视图合成任务。在公共数据集上对新颖的视图渲染和深度图预测任务进行了广泛的实验，证明所提出的方法在各种3D视觉任务中达到了最先进的性能。更多信息可以在我们的项目页面上找到(https://yanyan-li.github.io/project/gs/smilesplat) et.al.|[2411.18072](http://arxiv.org/abs/2411.18072)|null|
|**2024-11-26**|**Geometry Field Splatting with Gaussian Surfels**|从图像中几何重建不透明表面是计算机视觉领域的一个长期挑战，使用辐射场的体积视图合成算法重新引起了人们的兴趣。我们利用最近工作中提出的随机不透明表面的几何场，然后将其转换为体积密度。我们采用高斯核或曲面来绘制几何场而不是体积，从而能够精确重建不透明固体。我们的第一个贡献是为高斯曲面参数化的几何场推导出一种高效且几乎精确的可微渲染算法，同时消除了涉及泰勒级数的当前近似值，并且没有自衰减。接下来，我们讨论了当曲面在几何体附近聚集时的不连续损失情况，展示了如何保证渲染的颜色是核颜色的连续函数，而不管顺序如何。最后，我们使用球面谐波编码反射矢量的潜在表示，而不是球面谐波编码颜色，以更好地解决镜面问题。我们在广泛使用的数据集上证明了重建的3D表面质量的显著提高。 et.al.|[2411.17067](http://arxiv.org/abs/2411.17067)|null|
|**2024-11-25**|**G2SDF: Surface Reconstruction from Explicit Gaussians with Implicit SDFs**|最先进的新颖视图合成方法，如3D高斯散斑（3DGS），实现了卓越的视觉质量。虽然3DGS及其变体可以使用光栅化有效地渲染，但许多任务需要访问底层3D表面，由于这种表示的稀疏和显式性质，提取仍然具有挑战性。本文介绍了G2SDF，这是一种通过将神经隐式有符号距离场（SDF）集成到高斯散斑框架中来解决这一局限性的新方法。我们的方法将高斯的不透明度值与其到表面的距离联系起来，确保高斯与场景表面更紧密地对齐。为了将这种方法扩展到不同尺度的无界场景，我们提出了一种将任何范围映射到固定间隔的归一化函数。为了进一步提高重建质量，我们在高斯散布优化过程中利用现成的深度估计器作为伪地面真值。通过在显式高斯分布和隐式SDF之间建立可微连接，我们的方法能够实现高质量的曲面重建和渲染。在几个真实世界数据集上的实验结果表明，G2SDF在保持3DGS效率的同时，实现了比先前工作更优的重建质量。 et.al.|[2411.16898](http://arxiv.org/abs/2411.16898)|null|

<p align=right>(<a href=#updated-on-20241204>back to top</a>)</p>

## 3D Reconstruction

|Publish Date|Title|Abstract|PDF|Code|
|---|---|---|---|---|
|**2024-11-29**|**DeSplat: Decomposed Gaussian Splatting for Distractor-Free Rendering**|高斯飞溅技术使静态3D环境中的快速新颖视图合成成为可能。然而，重建现实世界的环境仍然具有挑战性，因为干扰物或遮挡物打破了精确3D重建所需的多视图一致性假设。大多数现有方法依赖于来自预训练模型的外部语义信息，在预处理步骤或优化过程中引入了额外的计算开销。在这项工作中，我们提出了一种新的方法DeSplat，该方法纯粹基于高斯基元的体绘制直接分离干扰物和静态场景元素。我们在每个相机视图中初始化高斯分布，以重建视图特定的干扰物，从而在阿尔法合成阶段分别对静态3D场景和干扰物进行建模。DeSplat实现了静态元素和干扰物的明确场景分离，在不牺牲渲染速度的情况下，实现了与先前无干扰物方法相当的结果。我们在三个基准数据集上证明了DeSplat在无干扰的新颖视图合成中的有效性。请访问项目网站https://aaltoml.github.io/desplat/. et.al.|[2411.19756](http://arxiv.org/abs/2411.19756)|null|
|**2024-11-29**|**Gaussian Splashing: Direct Volumetric Rendering Underwater**|在水下图像中，大多数有用的特征都被水遮挡了。遮挡的程度取决于成像几何形状，甚至可以在一系列突发图像中变化。因此，在空中场景中鲁棒的3D重建方法，如神经辐射场方法（NeRF）或3D高斯散斑（3DGS），在水下场景中失败。虽然最近对NeRFs的水下改编取得了最先进的结果，但速度慢得不切实际：重建需要数小时，其渲染速率（每秒帧数）小于1。在这里，我们提出了一种只需几分钟重建的新方法，并以140 FPS的速度渲染出新颖的水下场景。我们的方法名为高斯飞溅，将3DGS的优势和速度与用于捕获散射的图像形成模型相结合，在渲染和深度估计过程以及3DGS损失函数中引入了创新。尽管水下适应的复杂性，我们的方法仍能以无与伦比的速度生成具有卓越细节的图像。此外，它比其他方法更清晰地显示了远处的场景细节，极大地改善了重建和渲染图像。我们展示了现有数据集和我们收集的新数据集的结果。其他视觉结果可在以下网址获得：https://bgu-cs-vil.github.io/gaussiansplashingUW.github.io/ . et.al.|[2411.19588](http://arxiv.org/abs/2411.19588)|null|
|**2024-11-28**|**SADG: Segment Any Dynamic Gaussian Without Object Trackers**|理解动态3D场景是各种应用的基础，包括扩展现实（XR）和自动驾驶。将语义信息有效地集成到3D重建中，可以实现整体表示，为沉浸式和交互式应用程序打开机会。我们介绍了SADG，Segment Any Dynamic Gaussian Without Object Trackers，这是一种新的方法，它将动态高斯散点表示和语义信息相结合，而不依赖于对象ID。与现有的工作相比，我们不依赖于基于对象身份的监督来实现动态3D对象的一致分割。为此，我们建议通过利用从Segment Anything Model（SAM）生成的掩码并利用我们基于硬像素挖掘的新颖对比学习目标来学习语义感知特征。学习到的高斯特征可以有效地聚类，而无需进一步的后处理。这使得能够快速计算以进行进一步的对象级编辑，例如通过操纵场景中的高斯分布进行对象删除、合成和样式转换。我们进一步扩展了几个具有分割基准的动态新视图数据集，以便从看不见的视角测试学习到的特征场。我们在拟议的基准上评估了SADG，并证明了我们的方法在分割动态场景中的对象方面的卓越性能，以及它对进一步下游编辑任务的有效性。 et.al.|[2411.19290](http://arxiv.org/abs/2411.19290)|**[link](https://github.com/yunjinli/SADG-SegmentAnyDynamicGaussian)**|
|**2024-11-28**|**AGS-Mesh: Adaptive Gaussian Splatting and Meshing with Geometric Priors for Indoor Room Reconstruction Using Smartphones**|几何先验通常用于增强3D重建。随着许多智能手机配备低分辨率深度传感器，以及现成的单目几何估计器的普及，将几何先验作为正则化信号在3D视觉任务中已变得普遍。然而，对于高度详细的几何形状，移动设备的深度估计的准确性通常很差，单目估计器的多视图一致性和精度也很差。在这项工作中，我们提出了一种高斯散斑法的联合表面深度和法线细化方法，用于室内场景的精确3D重建。我们开发了监督策略，通过在优化过程中比较先验的一致性，自适应地过滤低质量深度和正常估计。我们在先验估计具有高度不确定性或模糊性的区域减轻正则化。我们的滤波策略和优化设计表明，在具有挑战性的室内数据集上，基于3D和2D高斯散斑的方法在网格估计和新颖的视图合成方面都有显著改进。此外，我们还探索了使用替代网格策略进行更精细的几何提取。我们开发了一种受TSDF和基于八叉树的等值面提取启发的尺度感知网格策略，与其他常用的开源网格工具相比，该策略可以从高斯模型中恢复出更精细的细节。我们的代码发布于https://xuqianren.github.io/ags_mesh_website/. et.al.|[2411.19271](http://arxiv.org/abs/2411.19271)|null|
|**2024-12-02**|**Differentiable Voxel-based X-ray Rendering Improves Sparse-View 3D CBCT Reconstruction**|我们提出了DiffVox，这是一种用于锥束计算机断层扫描（CBCT）重建的自监督框架，通过使用基于物理的可微X射线渲染直接优化体素网格表示。此外，我们还研究了渲染器中X射线图像形成模型的不同实现如何影响3D重建和新视图合成的质量。当与我们的正则化基于体素的学习框架相结合时，我们发现在渲染器中使用离散比尔-朗伯定律进行X射线衰减的精确实现优于广泛使用的迭代CBCT重建算法和现代神经场方法，特别是在只有少数输入视图的情况下。因此，我们用更少的X射线重建高保真3D CBCT体积，从而可能减少电离辐射暴露并提高诊断实用性。我们的实施可在https://github.com/hossein-momeni/DiffVox. et.al.|[2411.19224](http://arxiv.org/abs/2411.19224)|**[link](https://github.com/hossein-momeni/diffvox)**|
|**2024-11-28**|**Track Anything Behind Everything: Zero-Shot Amodal Video Object Segmentation**|我们提出了Track Anything Behind Everything（TABE），这是一个新颖的数据集、管道和评估框架，用于从可见掩码完成零样本amodal。与需要预先训练的类标签的现有方法不同，我们的方法从对象可见的第一帧使用单个查询掩码，从而实现灵活的零样本推理。我们的数据集TABE-51提供了高度精确的地面真值amodal分割掩模，无需人工估计或3D重建。我们的TABE管道是专门为处理amodal完成而设计的，即使在对象完全被遮挡的情况下也是如此。我们还引入了一个专门的评估框架，该框架将amodal完成性能隔离开来，不受传统视觉分割指标的影响。 et.al.|[2411.19210](http://arxiv.org/abs/2411.19210)|null|
|**2024-11-28**|**360Recon: An Accurate Reconstruction Method Based on Depth Fusion from 360 Images**|与传统针孔相机相比，360度图像提供了更宽的视野，能够在低纹理环境中进行稀疏采样和密集的3D重建。这使得它们对于VR、AR和相关领域的应用至关重要。然而，宽视场引起的固有失真会影响特征提取和匹配，导致后续多视图重建中的几何一致性问题。在这项工作中，我们提出了360Recon，这是一种用于ERP图像的创新MVS算法。所提出的球形特征提取模块有效地减轻了失真效应，通过将构建的3D成本体与ERP图像的多尺度增强特征相结合，我们的方法在保持局部几何一致性的同时实现了高精度的场景重建。实验结果表明，360Recon在现有的公共全景重建数据集上实现了最先进的性能和高效的深度估计和3D重建。 et.al.|[2411.19102](http://arxiv.org/abs/2411.19102)|null|
|**2024-11-28**|**RIGI: Rectifying Image-to-3D Generation Inconsistency via Uncertainty-aware Learning**|给定目标对象的单个图像，图像到3D生成旨在重建其纹理和几何形状。最近的方法通常利用中间媒体，如多视图图像或视频，来弥合输入图像和3D目标之间的差距，从而指导形状和纹理的生成。然而，生成的多视图快照中的不一致性经常会沿对象边界引入噪声和伪影，从而破坏3D重建过程。为了应对这一挑战，我们利用3D高斯散斑（3DGS）进行3D重建，并明确地将不确定性感知学习集成到重建过程中。通过捕捉两个高斯模型之间的随机性，我们估计了一个不确定性映射，随后将其用于不确定性感知正则化，以纠正不一致的影响。具体来说，我们同时优化两个高斯模型，通过评估来自相同视点的渲染图像之间的差异来计算不确定性图。基于不确定性图，我们应用自适应像素损失加权来正则化模型，降低高不确定性区域的重建强度。这种方法可以动态检测和缓解多视图标签中的冲突，从而获得更平滑的结果并有效减少伪影。大量实验表明，我们的方法通过减少不一致和伪影来提高3D生成质量。 et.al.|[2411.18866](http://arxiv.org/abs/2411.18866)|null|
|**2024-11-27**|**Lifting Motion to the 3D World via 2D Diffusion**|从2D观测中估计3D运动是一个长期的研究挑战。之前的工作通常需要对包含地面实况3D运动的数据集进行训练，这限制了它们对现有运动捕捉数据中很好地表示的活动的适用性。这种依赖性特别阻碍了对分布外场景或主题的泛化，在这些场景或主题中，收集3D地面实况具有挑战性，例如复杂的运动动作或动物运动。我们介绍了MVLift，这是一种仅使用2D姿势序列进行训练来预测全局3D运动的新方法，包括世界坐标系中的关节旋转和根轨迹。我们的多阶段框架利用2D运动扩散模型在多个视图中逐步生成一致的2D姿势序列，这是恢复准确的全局3D运动的关键步骤。MVLift适用于各种领域，包括人体姿势、人体与物体的交互和动物姿势。尽管不需要3D监督，但它在五个数据集上的表现优于先前的工作，包括那些需要3D监督的方法。 et.al.|[2411.18808](http://arxiv.org/abs/2411.18808)|null|
|**2024-11-27**|**Reconstructing Animals and the Wild**|3D重建作为场景理解的概念是计算机视觉的基础。从2D视觉观察重建3D场景需要强大的先验来消除结构歧义。许多工作都集中在人类中心主义上，其特征是光滑的表面、连贯的法线和规则的边缘，允许整合强烈的几何归纳偏见。在这里，我们考虑了一个更具挑战性的问题，即重建包含树木、灌木、巨石和动物的自然场景。虽然许多作品试图解决在野外重建动物的问题，但它们只关注动物，忽视了环境背景。这限制了它们在分析任务中的有用性，因为动物固有地存在于3D世界中，当忽略环境因素时，信息就会丢失。我们提出了一种从单幅图像重建自然场景的方法。我们的方法基于最近的进展，利用大型语言模型中根深蒂固的强世界先验，并训练一个自回归模型来解码嵌入到结构化构图场景表示中的CLIP，包括动物和野生动物（RAW）。为了实现这一点，我们提出了一个由100万张图像和数千个资产组成的合成数据集。我们的方法仅在合成数据上进行了训练，可以推广到在现实世界图像中重建动物及其环境的任务。我们将发布我们的数据集和代码，以鼓励未来的研究https://raw.is.tue.mpg.de/ et.al.|[2411.18807](http://arxiv.org/abs/2411.18807)|null|

<p align=right>(<a href=#updated-on-20241204>back to top</a>)</p>

## Diffusion

|Publish Date|Title|Abstract|PDF|Code|
|---|---|---|---|---|
|**2024-11-29**|**Open source Differentiable ODE Solving Infrastructure**|常微分方程（ODE）在物理、化学和生物学中被广泛用于模拟动态系统，包括反应动力学、种群动力学和生物过程。在这项工作中，我们将GPU加速的ODE求解器集成到开源DeepChem框架中，使这些工具易于访问。这些求解器支持多种数值方法，并且是完全可微的，可以轻松集成到更复杂的可微程序中。我们通过Lotka-Volterra捕食者-猎物动力学、药代动力学室模型、神经ODE和使用反应扩散方程求解PDE的实验来证明我们的实现能力。我们的求解器实现了高精度，均方误差从10^{-4} $到10^{-6}$ 不等，并在求解多达100个隔间的大型系统时显示出可扩展性。 et.al.|[2411.19882](http://arxiv.org/abs/2411.19882)|null|
|**2024-11-29**|**Gravity's role in taming the Tayler instability in red giant cores**|恒星内部环形磁场的稳定性仍然是当代天体物理学中一个悬而未决的重要问题。在这项研究中，我们将非局部线性分析与3D直接数值模拟相结合，以检查球形几何中非旋转、稳定分层恒星内部环形场的不稳定性。这两种分析都从平衡洛伦兹力和流体压力的各向异性分量得出的平衡解开始，该各向异性分量对（非轴对称）泰勒不稳定性不稳定，并考虑了重力和热扩散的综合影响。数值模拟结合了有限的磁阻和流体粘度，同时达到了以前从未探索过的高度稳定的分层状态。在径向方向上具有全局性的线性分析表明，重力显著降低了不稳定性的增长率，并揭示了低纬度低径向波数不稳定模式的重要性。模拟追踪了不稳定性从线性阶段到非线性阶段的整个演变，并有力地证实了线性分析的结果。我们的结果表明，在高度分层的恒星内部，新配置的磁场仅在热扩散时间尺度上保持不稳定。将线性分析结果与低质量恒星的恒星演化模型相结合，我们发现红巨星核心泰勒不稳定性的极限环形场强随着恒星演化而降低。预测的场强与最近的星震观测结果一致，这表明观测到的场强可能是主层序向巨相过渡期间泰勒不稳定性的残余。 et.al.|[2411.19849](http://arxiv.org/abs/2411.19849)|null|
|**2024-11-29**|**Classical transport in a maximally chaotic chain**|最近介绍了一种耦合猫图网格模型。这种新的和具体的耦合选择使得描述变得特别容易和重要，因为李雅普诺夫指数是精确确定的。我们研究了局部扰动下沿这种链的动力学遍历性质。当扰动在弹道增长的前沿传播时，由于混沌导致相空间中的扩散输运，位置和动量分布显示出较大的波动。它提供了一个例子，可以从微观混沌中直接推断出扩散。 et.al.|[2411.19828](http://arxiv.org/abs/2411.19828)|null|
|**2024-11-29**|**Open and trapping channels in complex resonant media**|我们对由谐振器组成的无序介质中的传输和停留时间矩阵进行了统计研究，重点研究了频率失谐如何影响其特征值分布。我们的分析表明，随着频率接近粒子的共振频率，传输特征值的分布经历了从单峰到双峰分布，再回到单峰的转变。此外，在共振附近，驻留时间特征值的分布显著变宽，最长寿命超过中值几个数量级。通过研究频率 $\omega$如何影响光的输运平均自由程$\ell（\omega）$和能量输运速度$v_E（\omega-）$来解释这些结果，这反过来又塑造了观测到的分布。我们证明了波前整形在增强共振无序介质中的传输和能量存储方面的巨大潜力。在扩散状态下，系统厚度$L$超过平均自由程，当使用与最大特征值相关的波阵面而不是平面波时，传输和停留时间都可以提高$\varpropto L/\ell（\omega）\gg 1$。在本地化方案中，增强对于传输变为$\varpropto Ne^｛2L/\neneneba xi｝$，对于停留时间变为$\ varpropto N\nenenebb xi/L$，其中$\xi$是本地化长度，$N$ 是受控散射信道的数量。最后，我们表明，在扩散和局部区域，使用高Q值谐振器而不是低Q值谐振器可以将介质内的能量存储增加到Q/k（ω）的一倍。 et.al.|[2411.19818](http://arxiv.org/abs/2411.19818)|null|
|**2024-11-29**|**MoTe: Learning Motion-Text Diffusion Model for Multiple Generation Tasks**|近年来，由于去噪扩散模型和大型语言模型等生成模型的启发，人体运动分析得到了很大的改进。而现有的方法主要侧重于生成具有文本描述的运动，忽略了交互任务。在本文中，我们提出了~\textbf{MoTe}，这是一个统一的多模态模型，可以通过同时学习运动和文本的边缘、条件和联合分布来处理不同的任务。MoTe使我们能够通过简单地修改输入上下文来处理成对的文本运动生成、运动字幕和文本驱动的运动生成。具体来说，MoTe由三个部分组成：运动编解码器（MED）、文本编解码器（TED）和文本扩散模型上的Moti（MTDM）。特别是，MED和TED被训练用于提取潜在的嵌入，随后分别从提取的嵌入中重建运动序列和文本描述。另一方面，MTDM对输入上下文执行迭代去噪过程，以处理各种任务。在基准数据集上的实验结果表明，我们提出的方法在文本到运动生成方面具有优越的性能，在运动字幕方面具有竞争力。 et.al.|[2411.19786](http://arxiv.org/abs/2411.19786)|null|
|**2024-11-29**|**Riemannian Denoising Score Matching for Molecular Structure Optimization with Accurate Energy**|本研究介绍了一种改进的分数匹配方法，旨在以高能量精度生成分子结构。分数匹配或扩散模型的去噪过程反映了分子结构优化，其中分数就像引导粒子达到平衡状态的物理力场。为了实现能量精确的结构，使分数接近实际势能面的梯度可能是有利的。与简单地基于欧几里德空间中的结构差异设计目标分数的传统方法不同，我们提出了一种黎曼分数匹配方法。该方法表示由物理信息内部坐标定义的流形上的分子结构，以有效地模拟能量景观，并在该空间内进行噪声和去噪。我们的方法已经通过在QM9和GEOM数据集上精炼几种类型的起始结构进行了评估，证明所提出的黎曼分数匹配方法显著提高了生成的分子结构的准确性，达到了化学准确性。这项研究的意义扩展到计算化学中的各种应用，为精确的分子结构预测提供了一种强大的工具。 et.al.|[2411.19769](http://arxiv.org/abs/2411.19769)|null|
|**2024-11-29**|**Insensitizing controls of a volume-surface reaction-diffusion equation with dynamic boundary conditions**|本文研究了具有动态边界条件的拟线性抛物方程的不敏感可控性。这个问题可以重新表述为具有动态边界条件的级联拟线性系统的零可控性问题。为此，我们首先在非齐次线性化系统的框架内处理零能控性问题。接下来，我们推导出了控制和状态的新估计，使我们能够应用局部逆定理来获得拟线性系统的零可控性。 et.al.|[2411.19760](http://arxiv.org/abs/2411.19760)|null|
|**2024-11-29**|**TexGaussian: Generating High-quality PBR Material via Octree-based 3D Gaussian Splatting**|基于物理的渲染（PBR）材质在现代图形中起着至关重要的作用，可以在各种环境地图上实现逼真的渲染。开发一种有效且高效的算法，能够自动生成高质量的PBR材质，而不是3D网格的RGB纹理，可以显著简化3D内容创建。大多数现有方法利用预训练的2D扩散模型进行多视图图像合成，这通常会导致生成的纹理和输入的3D网格之间存在严重的不一致。本文介绍了TexGausian，这是一种使用八分体对齐的3D高斯散斑进行快速PBR材料生成的新方法。具体来说，我们将每个3D高斯分布放置在从输入的3D网格构建的八叉树的最精细叶子节点上，以渲染多视图图像，不仅用于反照率图，还用于粗糙度和金属性。此外，我们的模型是以回归方式训练的，而不是扩散去噪，能够在单个前馈过程中为3D网格生成PBR材料。在公开可用的基准上进行的广泛实验表明，我们的方法合成了更美观的PBR材料，在无条件和文本条件场景中比以前的方法运行得更快，这与给定的几何形状表现出更好的一致性。我们的代码和训练模型可在https://3d-aigc.github.io/TexGaussian. et.al.|[2411.19654](http://arxiv.org/abs/2411.19654)|null|
|**2024-11-29**|**Uniform Attention Maps: Boosting Image Fidelity in Reconstruction and Editing**|使用扩散模型的文本引导图像生成和编辑取得了显著进展。其中，免调优方法因其无需大量模型调整即可执行编辑的能力而受到关注，提供了简单性和效率。然而，现有的免调优方法往往难以平衡保真度和编辑精度。DDIM反演中的重建误差部分归因于U-Net中的交叉注意机制，该机制在反演和重建过程中引入了失准。为了解决这个问题，我们从结构的角度分析重建，并提出了一种新的方法，用统一的注意力图取代传统的交叉注意力，显著提高了图像重建的保真度。我们的方法有效地减少了噪声预测过程中不同文本条件引起的失真。为了补充这一改进，我们引入了一种自适应掩模引导编辑技术，该技术与我们的重建方法无缝集成，确保编辑任务的一致性和准确性。实验结果表明，我们的方法不仅在实现高保真图像重建方面表现出色，而且在真实的图像合成和编辑场景中表现稳健。这项研究强调了统一注意力图在提高基于扩散的图像处理方法的保真度和通用性方面的潜力。代码可在以下网址获得https://github.com/Mowenyii/Uniform-Attention-Maps. et.al.|[2411.19652](http://arxiv.org/abs/2411.19652)|**[link](https://github.com/mowenyii/uniform-attention-maps)**|
|**2024-11-29**|**CogACT: A Foundational Vision-Language-Action Model for Synergizing Cognition and Action in Robotic Manipulation**|大型视觉语言动作（VLA）模型的进步显著提高了机器人在语言引导任务执行和对未知场景的泛化方面的操纵能力。虽然从预训练的大型视觉语言模型（VLM）改编的现有VLA已经显示出有希望的泛化能力，但它们的任务性能仍然不令人满意，这可以从不同环境中的低任务成功率中看出。本文介绍了一种基于VLM的新型高级VLA架构。与之前通过简单的动作量化直接将VLM重新用于动作预测的工作不同，我们提出了一种组件化的VLA架构，该架构具有一个以VLM输出为条件的专用动作模块。我们系统地研究了动作模块的设计，并展示了扩散动作变换器在动作序列建模中的强大性能增强，以及它们良好的缩放行为。我们还进行了全面的实验和消融研究，以评估我们采用不同设计的模型的疗效。对5个机器人实施例在模拟和实际工作中的评估表明，我们的模型不仅在任务性能上显著优于现有的VLA，而且对新机器人的适应性和对看不见的物体和背景的泛化能力也很强。它在模拟评估中超过了OpenVLA的平均成功率35%以上，在真实机器人实验中超过了55%，OpenVLA与我们的模型尺寸（7B）相似。它在模拟中的绝对成功率也超过了大型RT-2-X模型（55B）18%。代码和模型可以在我们的项目页面上找到(https://cogact.github.io/). et.al.|[2411.19650](http://arxiv.org/abs/2411.19650)|null|

<p align=right>(<a href=#updated-on-20241204>back to top</a>)</p>

## NeRF

|Publish Date|Title|Abstract|PDF|Code|
|---|---|---|---|---|
|**2024-12-02**|**Differentiable Voxel-based X-ray Rendering Improves Sparse-View 3D CBCT Reconstruction**|我们提出了DiffVox，这是一种用于锥束计算机断层扫描（CBCT）重建的自监督框架，通过使用基于物理的可微X射线渲染直接优化体素网格表示。此外，我们还研究了渲染器中X射线图像形成模型的不同实现如何影响3D重建和新视图合成的质量。当与我们的正则化基于体素的学习框架相结合时，我们发现在渲染器中使用离散比尔-朗伯定律进行X射线衰减的精确实现优于广泛使用的迭代CBCT重建算法和现代神经场方法，特别是在只有少数输入视图的情况下。因此，我们用更少的X射线重建高保真3D CBCT体积，从而可能减少电离辐射暴露并提高诊断实用性。我们的实施可在https://github.com/hossein-momeni/DiffVox. et.al.|[2411.19224](http://arxiv.org/abs/2411.19224)|**[link](https://github.com/hossein-momeni/diffvox)**|
|**2024-11-27**|**Neural Image Unfolding: Flattening Sparse Anatomical Structures using Neural Fields**|断层成像揭示了3D物体的内部结构，对医学诊断至关重要。在断层体积的多个2D切片上，可视化非平面稀疏解剖结构的形态和外观本质上很困难，但对决策和报告很有价值。因此，存在各种器官特异性展开技术，将其密集采样的3D表面映射到失真最小化的2D表示。然而，目前还没有通用的框架来压平复杂的稀疏结构，包括血管、导管或骨骼系统。我们部署了一个神经场，将感兴趣的解剖结构转换为二维概览图像。我们进一步提出了失真正则化策略，并将几何损失公式与基于强度的损失公式相结合，以显示无注释和辅助目标。除了提高通用性外，我们的展开技术在稀疏结构的峰值失真方面优于基于网格的基线，与基于神经场的图像配准的雅可比公式相比，我们的正则化方案产生了更平滑的变换。 et.al.|[2411.18415](http://arxiv.org/abs/2411.18415)|null|
|**2024-11-25**|**The Radiance of Neural Fields: Democratizing Photorealistic and Dynamic Robotic Simulation**|随着机器人越来越多地与人类共存，它们必须在复杂、动态的环境中导航，这些环境富含视觉信息和隐含的社会动态，比如何时屈服或穿过人群。应对这些挑战需要在基于视觉的传感方面取得重大进展，并对社会动态因素有更深入的了解，特别是在导航等任务中。为了促进这一点，机器人研究人员需要先进的仿真平台，提供具有逼真演员的动态、逼真的环境。不幸的是，大多数现有的模拟器都达不到要求，将几何精度置于视觉保真度之上，并使用具有固定轨迹和低质量视觉效果的不切实际的代理。为了克服这些局限性，我们开发了一个模拟器，该模拟器结合了三个基本要素：（1）环境的逼真神经渲染，（2）具有行为管理的神经动画人类实体，以及（3）提供多传感器输出的以自我为中心的机器人代理。通过在双NeRF模拟器中利用先进的神经渲染技术，我们的系统可以生成环境和人体实体的高保真、逼真的渲染。此外，它还集成了最先进的社会力模型来模拟动态的人机和人机交互，创建了第一个由神经渲染驱动的逼真和可访问的人机模拟系统。 et.al.|[2411.16940](http://arxiv.org/abs/2411.16940)|null|
|**2024-11-21**|**CoNFiLD-inlet: Synthetic Turbulence Inflow Using Generative Latent Diffusion Models with Neural Fields**|涡流解析湍流模拟需要随机流入条件，以准确复制复杂的多尺度湍流结构。传统的基于再循环的方法依赖于计算昂贵的前体模拟，而现有的合成流入发生器往往无法再现真实的湍流相干结构。深度学习（DL）的最新进展为流入湍流生成开辟了新的可能性，但许多基于DL的方法依赖于确定性、自回归框架，容易产生误差累积，导致长期预测的鲁棒性较差。在这项工作中，我们提出了CoNFiLD入口，这是一种基于DL的新型流入湍流发生器，它将扩散模型与条件神经场（CNF）编码的潜在空间相结合，以产生逼真的随机流入湍流。通过使用雷诺数对流入条件进行参数化，CoNFiLD入口在很宽的雷诺数范围内（ $Re_tau$在$10^3$和$10^4$ 之间）有效地推广，而不需要重新训练或参数调整。通过直接数值模拟（DNS）和壁模型大涡模拟（WMLES）中的先验和后验测试进行的全面验证证明了其高保真度、鲁棒性和可扩展性，使其成为流入湍流合成的高效和通用解决方案。 et.al.|[2411.14378](http://arxiv.org/abs/2411.14378)|null|
|**2024-11-20**|**FAST-Splat: Fast, Ambiguity-Free Semantics Transfer in Gaussian Splatting**|我们提出了FAST Splat，用于快速、无歧义的语义高斯Splatting，旨在解决现有语义高斯Splatting方法的主要局限性，即：训练和渲染速度慢；内存使用率高；语义对象定位模糊。在推导FAST Splat时，我们将开放词汇语义高斯Splatting表述为将闭集语义蒸馏扩展到开放集（开放词汇）设置的问题，使FAST Splat能够提供精确的语义对象定位结果，即使在用户提供的模糊自然语言查询提示时也是如此。此外，通过最大限度地利用高斯散斑场景表示的显式形式，FAST Splat保留了高斯散斑的显著训练和渲染速度。具体来说，虽然现有的语义高斯散斑方法将语义提取到一个单独的神经场中或利用神经模型进行降维，但FAST Splat直接用特定的语义代码增强每个高斯分布，保留了高斯散斑相对于神经场方法的训练、渲染和内存使用优势。与先前的方法不同，这些高斯特定的语义代码以及哈希表使语义相似性能够通过开放词汇表用户提示进行测量，并进一步使FAST Splat能够用明确的语义对象标签和3D掩码进行响应。在实验中，我们证明，与最好的竞争语义高斯Splatting方法相比，FAST Splat的训练速度快4倍至6倍，数据预处理步骤快13倍，渲染速度快18倍至75倍，所需GPU内存大约小3倍。此外，与现有方法相比，FAST Splat实现了相对相似或更好的语义分割性能。审查期结束后，我们将提供项目网站和代码库的链接。 et.al.|[2411.13753](http://arxiv.org/abs/2411.13753)|null|
|**2024-11-20**|**GazeGaussian: High-Fidelity Gaze Redirection with 3D Gaussian Splatting**|在处理分布外数据时，凝视估计遇到了泛化挑战。为了解决这个问题，最近的方法使用神经辐射场（NeRF）来生成增强数据。然而，基于NeRF的现有方法计算成本高昂，缺乏面部细节。三维高斯散斑（3DGS）已成为神经场的主流表示。虽然3DGS已经在头部化身中得到了广泛的研究，但它面临着在不同受试者之间进行精确视线控制和泛化的挑战。在这项工作中，我们提出了GazeGaussian，这是一种高保真的视线重定向方法，它使用双流3DGS模型分别表示面部和眼睛区域。通过利用3DGS的非结构化特性，我们开发了一种基于目标凝视方向的刚性眼睛旋转的新眼睛表示。为了增强各种主题的综合泛化能力，我们集成了一个表达式条件模块来指导神经渲染器。综合实验表明，GazeGaussian在渲染速度、视线重定向精度和跨多个数据集的面部合成方面优于现有方法。我们还证明，现有的凝视估计方法可以利用GazeGaussian来提高其泛化性能。该代码将在以下网址提供：https://ucwxb.github.io/GazeGaussian/. et.al.|[2411.12981](http://arxiv.org/abs/2411.12981)|null|
|**2024-11-18**|**NeuMaDiff: Neural Material Synthesis via Hyperdiffusion**|高质量的材料合成对于复制复杂的表面特性以创建逼真的数字场景至关重要。然而，现有的方法往往在时间和内存方面效率低下，需要领域专业知识，或者需要大量的训练数据，而高维材料数据进一步限制了性能。此外，大多数方法缺乏多模态制导能力和标准化的评估指标，限制了综合任务的控制和可比性。为了解决这些局限性，我们提出了NeuMaDiff，这是一种利用超扩散的新型神经材料合成框架。我们的方法采用神经场作为低维表示，并结合了多模态条件超扩散模型来学习材料重量的分布。这使得通过材料类型、文本描述或参考图像等输入进行灵活指导成为可能，从而对合成提供了更大的控制。为了支持未来的研究，我们贡献了两个新的材料数据集，并引入了两个BRDF分布度量，以进行更严格的评估。我们通过广泛的实验证明了NeuMaDiff的有效性，包括一种新的基于统计的约束合成方法，该方法能够生成所需类别的材料。 et.al.|[2411.12015](http://arxiv.org/abs/2411.12015)|null|
|**2024-11-14**|**The Hydrodynamic Limit of Hawkes Processes on Adaptive Stochastic Networks**|我们确定了自适应网络上相互作用的霍克斯过程网络的大尺寸限制。节点变量的翻转被认为具有由传入边缘和节点的平均场给出的强度。边缘变量的翻转是传入节点变量的函数。边变量可以是对称的，也可以是不对称的。该模型受到社会学、神经科学和流行病学应用的启发。一般来说，极限概率律可以表示为具有强度函数的自洽泊松过程的不动点，该强度函数（i）是延迟的，（ii）取决于其自身的概率律。在边缘翻转仅由突触前神经元的状态决定的特定情况下（如神经科学中），证明了可以获得突触增强和神经增强双重进化的自主神经场型方程。 et.al.|[2411.09260](http://arxiv.org/abs/2411.09260)|null|
|**2024-11-09**|**Epi-NAF: Enhancing Neural Attenuation Fields for Limited-Angle CT with Epipolar Consistency Conditions**|神经场方法最初在逆渲染领域取得了成功，最近已扩展到CT重建，标志着传统技术的范式转变。虽然这些方法在稀疏视图CT重建中提供了最先进的结果，但它们在有限的角度设置中很难实现，在有限的视角范围内捕获输入投影。我们提出了一种基于X射线投影图像中相应极线之间一致性条件的新损失项，旨在规范神经衰减场优化。通过强制执行这些一致性条件，我们的方法Epi NAF将监督从有限角度范围内的输入视图传播到整个锥束CT范围内的预测投影。与基线方法相比，这种损失导致重建的定性和定量改进。 et.al.|[2411.06181](http://arxiv.org/abs/2411.06181)|null|
|**2024-11-07**|**LoFi: Scalable Local Image Reconstruction with Implicit Neural Representation**|神经场或隐式神经表示（INR）因其对图像和3D体积的有效连续表示而在机器学习和信号处理中引起了广泛关注。在这项工作中，我们以INR为基础，引入了一种基于坐标的局部处理框架来解决成像逆问题，称为LoFi（局部场）。与传统的图像重建方法不同，LoFi通过多层感知器（MLP）分别处理每个坐标处的局部信息，在该特定坐标处恢复对象。与INR类似，LoFi可以在任何连续坐标下恢复图像，从而实现多分辨率的图像重建。LoFi在图像重建方面的性能与标准CNN相当或更好，几乎与图像分辨率无关，对分布外数据和内存使用具有出色的泛化能力。值得注意的是，对1024美元×1024美元的图像进行训练只需要3GB的内存，比标准CNN通常需要的内存少20多倍。此外，LoFi的局部设计使其能够在小于10个样本的极小数据集上进行训练，而不会过拟合或需要正则化或提前停止。最后，我们使用LoFi作为即插即用框架中的去噪先验，用于解决一般的逆问题，以受益于其连续的图像表示和强大的泛化能力。尽管在低分辨率图像上进行了训练，但LoFi可以用作低维先验，以解决任何分辨率的逆问题。我们通过各种成像方式验证了我们的框架，从低剂量计算机断层扫描到无线电干涉成像。 et.al.|[2411.04995](http://arxiv.org/abs/2411.04995)|null|

<p align=right>(<a href=#updated-on-20241204>back to top</a>)</p>

[contributors-shield]: https://img.shields.io/github/contributors/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[contributors-url]: https://github.com/Vincentqyw/cv-arxiv-daily/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[forks-url]: https://github.com/Vincentqyw/cv-arxiv-daily/network/members
[stars-shield]: https://img.shields.io/github/stars/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[stars-url]: https://github.com/Vincentqyw/cv-arxiv-daily/stargazers
[issues-shield]: https://img.shields.io/github/issues/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[issues-url]: https://github.com/Vincentqyw/cv-arxiv-daily/issues

