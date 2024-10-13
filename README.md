[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]

## Updated on 2024.10.13
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
|**2024-10-10**|**DifFRelight: Diffusion-Based Facial Performance Relighting**|我们提出了一种使用基于扩散的图像到图像转换的自由视点面部表现再照明的新框架。利用包含在各种照明条件下捕获的不同面部表情的特定主题数据集，包括平面照明和一次一光（OLAT）场景，我们训练了一个用于精确照明控制的扩散模型，从而能够从平面照明输入中获得高保真度的面部图像。我们的框架包括平面光捕获和随机噪声的空间对齐调节，以及用于全局控制的集成照明信息，利用预训练的稳定扩散模型的先验知识。然后将该模型应用于在一致的平面照明环境中捕获的动态面部表现，并使用可扩展的动态3D高斯散斑方法进行重建，以保持重新照明结果的质量和一致性，从而进行新的视图合成。此外，我们通过将新颖的区域照明表示与定向照明集成，引入了统一的照明控制，允许对灯光大小和方向进行联合调整。我们还使用多个方向光实现高动态范围成像（HDRI）合成，以在复杂的照明条件下产生动态序列。我们的评估表明，模型在实现精确的照明控制和跨各种面部表情的泛化方面非常有效，同时保留了皮肤纹理和头发等详细特征。该模型准确地再现了复杂的照明效果，如眼睛反射、次表面散射、自阴影和半透明，在我们的框架内推进了照片真实感。 et.al.|[2410.08188](http://arxiv.org/abs/2410.08188)|null|
|**2024-10-10**|**IncEventGS: Pose-Free Gaussian Splatting from a Single Event Camera**|用于新颖视图合成的隐式神经表示和显式3D高斯散斑（3D-GS）最近在基于帧的相机（如RGB和RGB-D相机）方面取得了显著进展。与基于帧的相机相比，一种新型的仿生视觉传感器，即事件相机，在高时间分辨率、高动态范围、低功耗和低延迟方面具有优势。由于其独特的异步和不规则的数据捕获过程，将神经表示或3D高斯飞溅应用于事件相机的工作有限。在这项工作中，我们提出了IncEventGS，这是一种使用单事件相机的增量3D高斯散斑重建算法。为了逐步恢复3D场景表示，我们利用了IncEventGS的传统SLAM管道的跟踪和映射范式。给定传入的事件流，跟踪器首先基于先前重建的3D-GS场景表示来估计初始相机运动。然后，映射器基于来自跟踪器的先前估计的运动轨迹，联合细化3D场景表示和相机运动。实验结果表明，与之前的基于NeRF的方法和其他相关基线相比，IncEventGS具有更优的性能，即使我们没有地面实况相机姿态。此外，与最先进的事件视觉里程计方法相比，我们的方法在相机运动估计方面也可以提供更好的性能。代码可在以下网址公开获取：https://github.com/wu-cvgl/IncEventGS. et.al.|[2410.08107](http://arxiv.org/abs/2410.08107)|**[link](https://github.com/wu-cvgl/inceventgs)**|
|**2024-10-10**|**Fast Feedforward 3D Gaussian Splatting Compression**|随着3D高斯散斑（3DGS）推进了用于新颖视图合成的实时和高保真渲染，存储要求对其广泛采用提出了挑战。尽管已经提出了各种压缩技术，但现有技术存在一个共同的局限性：对于任何现有的3DGS，都需要按场景优化来实现压缩，这使得压缩缓慢而缓慢。为了解决这个问题，我们引入了3D高斯散布的快速压缩（FCGS），这是一种无需优化的模型，可以在一次前馈过程中快速压缩3DGS表示，从而将压缩时间从几分钟缩短到几秒钟。为了提高压缩效率，我们提出了一种多路径熵模块，该模块将高斯属性分配给不同的熵约束路径，以实现大小和保真度之间的平衡。我们还仔细设计了高斯间和高斯内上下文模型，以消除非结构化高斯斑点之间的冗余。总体而言，FCGS在保持保真度的同时实现了超过20倍的压缩比，超越了大多数基于每场景SOTA优化的方法。我们的代码可在以下网址获得：https://github.com/YihangChen-ee/FCGS. et.al.|[2410.08017](http://arxiv.org/abs/2410.08017)|**[link](https://github.com/yihangchen-ee/fcgs)**|
|**2024-10-08**|**BEVLoc: Cross-View Localization and Matching via Birds-Eye-View Synthesis**|地对空匹配是户外机器人技术中一项至关重要且具有挑战性的任务，特别是在GPS缺失或不可靠的情况下。建筑物或大型茂密森林等结构会产生干扰，需要GNSS替代全球定位估计。真正的困难在于调和地面和空中图像之间的视角差异，以实现可接受的定位。从自动驾驶社区获得灵感，我们提出了一种新的框架，用于合成鸟瞰图（BEV）场景表示，以在越野环境中与航空地图进行匹配和定位。我们利用对比学习和特定领域的硬负挖掘来训练网络，以学习合成BEV和航空地图之间的相似表示。在推理过程中，BEVLoc通过从粗到细的匹配策略引导识别航空地图中最可能的位置。我们的研究结果表明，在语义多样性有限的极其困难的森林环境中，初步结果很有希望。我们分析了模型的粗匹配和细匹配性能，评估了模型的原始匹配能力及其作为GNSS替代品的性能。我们的工作深入研究了越野地图本地化，同时为本地化的未来发展建立了基础基线。我们的代码可在以下网址获得：https://github.com/rpl-cmu/bevloc et.al.|[2410.06410](http://arxiv.org/abs/2410.06410)|null|
|**2024-10-08**|**HiSplat: Hierarchical 3D Gaussian Splatting for Generalizable Sparse-View Reconstruction**|从多个视点重建3D场景是立体视觉中的一项基本任务。最近，可推广的3D高斯散斑技术的进步通过前馈预测每像素高斯参数而无需额外优化，实现了从稀疏输入视图中为看不见的场景进行高质量的新颖视图合成。然而，现有的方法通常生成单尺度3D高斯分布，缺乏对大规模结构和纹理细节的表示，导致定位错误和伪影。本文提出了一种新的框架HiSplat，该框架在可推广的3D高斯散点中引入了一种分层方式，通过从粗到细的策略构建分层的3D高斯分布。具体来说，HiSplat生成大的粗粒度高斯分布来捕捉大规模结构，然后生成细粒度高斯分布来增强精细的纹理细节。为了促进尺度间的相互作用，我们提出了一个用于高斯补偿的误差感知模块和一个用于Gaussian修复的调制融合模块。我们的方法实现了分层表示的联合优化，允许仅使用两个视图参考图像进行新颖的视图合成。对各种数据集的综合实验表明，与之前的单尺度方法相比，HiSplat显著提高了重建质量和跨数据集泛化能力。对不同尺度三维高斯分布的相应消融研究和分析揭示了有效性背后的机制。项目网站：https://open3dvlab.github.io/HiSplat/ et.al.|[2410.06245](http://arxiv.org/abs/2410.06245)|null|
|**2024-10-08**|**Comparative Analysis of Novel View Synthesis and Photogrammetry for 3D Forest Stand Reconstruction and extraction of individual tree parameters**|准确高效的树木三维重建对于森林资源评估和管理至关重要。近景摄影测量（CRP）通常用于重建森林场景，但面临着效率低、质量差等挑战。最近，包括神经辐射场（NeRF）和3D高斯散斑（3DGS）在内的新型视图合成（NVS）技术已显示出在有限图像下进行3D植物重建的前景。然而，现有的研究主要集中在果园或单株树木中的小型植物上，这给它们在更大、更复杂的林分中的应用带来了不确定性。在这项研究中，我们收集了具有不同复杂性的森林地块的连续图像，并使用NeRF和3DGS进行了密集重建。将得到的点云与摄影测量和激光扫描的点云进行了比较。结果表明，NVS方法显著提高了重建效率。摄影测量难以处理复杂的林分，导致点云的树冠噪声过大，树木重建不正确，如树干重复。NeRF虽然对树冠区域更好，但在视野有限的地面区域可能会产生误差。3DGS方法生成更稀疏的点云，特别是在主干区域，影响胸径（DBH）精度。这三种方法都可以提取树高信息，其中NeRF的精度最高；然而，摄影测量在DBH精度方面仍然具有优势。这些发现表明，NVS方法在林分三维重建方面具有巨大潜力，为复杂的森林资源清查和可视化任务提供了宝贵支持。 et.al.|[2410.05772](http://arxiv.org/abs/2410.05772)|null|
|**2024-10-07**|**PH-Dropout: Prctical Epistemic Uncertainty Quantification for View Synthesis**|使用神经辐射场（NeRF）和高斯散斑（GS）的视图合成在渲染现实世界场景时表现出了令人印象深刻的保真度。然而，在视图综合中缺乏准确有效的认知不确定性量化（UQ）的实用方法。现有的NeRF方法要么引入了大量的计算开销（例如，“训练时间增加10倍”或“重复训练10倍”），要么仅限于特定的不确定性条件或模型。值得注意的是，GS模型缺乏全面认知UQ的系统方法。这种能力对于提高神经视图合成的鲁棒性和可扩展性至关重要，可以实现主动模型更新、误差估计和基于不确定性的可扩展集成建模。本文从函数近似的角度重新审视了基于NeRF和GS的方法，确定了3D表示学习中的关键差异和联系。基于这些见解，我们介绍了PH Dropout（事后Dropout），这是第一种直接在预训练的NeRF和GS模型上进行认知不确定性估计的实时准确方法。广泛的评估验证了我们的理论发现，并证明了PH Dropout的有效性。 et.al.|[2410.05468](http://arxiv.org/abs/2410.05468)|**[link](https://github.com/thanostriantafyllou3/ph-dropout)**|
|**2024-10-07**|**DreamSat: Towards a General 3D Model for Novel View Synthesis of Space Objects**|新颖的视图合成（NVS）能够生成场景的新图像或将一组2D图像转换为全面的3D模型。在空间领域意识的背景下，由于空间变得越来越拥挤，NVS可以准确地绘制空间物体和碎片的地图，提高空间操作的安全性和效率。同样，在会合和近距离作战任务中，3D模型可以提供目标物体的形状、大小和方向的详细信息，从而更好地规划和预测目标的行为。在这项工作中，我们探索了这些重建技术的泛化能力，旨在通过在190个高质量航天器模型的高质量数据集上微调最先进的单视图重建模型Zero123 XL，并将其集成到DreamGaussian框架中，提出一种从单视图图像重建3D航天器的新方法DreamSat，从而避免对每个新场景进行再训练的必要性。我们展示了在多个指标上重建质量的一致改进，包括对比语言图像预训练（CLIP）得分（+0.33%）、峰值信噪比（PSNR）（+2.53%）、结构相似性指数（SSIM）（+2.38%）和学习感知图像补丁相似性（LPIPS）（+0.16%）。%）在30张以前从未见过的航天器图像的测试集上。我们的方法通过利用最先进的扩散模型和3D高斯溅射技术，解决了航天工业中缺乏特定领域的3D重建工具的问题。这种方法保持了DreamGaussian框架的效率，同时提高了航天器重建的准确性和细节。这项工作的代码可以在GitHub上访问(https://github.com/ARCLab-MIT/space-nvs). et.al.|[2410.05097](http://arxiv.org/abs/2410.05097)|**[link](https://github.com/arclab-mit/space-nvs)**|
|**2024-10-10**|**6DGS: Enhanced Direction-Aware Gaussian Splatting for Volumetric Rendering**|随着神经辐射场（NeRF）和3D高斯散射（3DGS）的发展，新型视图合成技术取得了显著进步。然而，在不影响实时渲染的情况下实现高质量仍然具有挑战性，特别是对于具有视图相关效果的基于物理的光线跟踪。最近，N维高斯（N-DG）引入了6D空间角度表示，以更好地结合视图相关的效果，但高斯表示和控制方案都是次优的。在本文中，我们重新审视了6D高斯分布，并引入了6D高斯散斑（6DGS），它增强了颜色和不透明度表示，并利用6D空间中的额外方向信息来优化高斯控制。我们的方法与3DGS框架完全兼容，并通过更好地建模视图相关效果和精细细节，显著提高了实时辐射场渲染。实验证明，6DGS明显优于3DGS和N-DG，与3DGS相比，PSNR提高了15.73dB，高斯点减少了66.5%。项目页面为：https://gaozhongpai.github.io/6dgs/ et.al.|[2410.04974](http://arxiv.org/abs/2410.04974)|null|
|**2024-10-07**|**TeX-NeRF: Neural Radiance Fields from Pseudo-TeX Vision**|神经辐射场（NeRF）因其卓越的视觉效果而受到广泛关注。然而，大多数现有的NeRF方法都是从可见光相机捕获的RGB图像中重建3D场景。在黑暗、低光照或恶劣天气等实际情况下，可见光摄像头会变得无效。因此，我们提出了TeX-NeRF，这是一种仅使用红外图像的3D重建方法，它先验地引入了物体材料的发射率，使用伪TeX视觉对红外图像进行预处理，并将场景的温度（T）、发射率（e）和纹理（X）分别映射到HSV颜色空间的饱和度（S）、色调（H）和值（V）通道中。使用处理后的图像的新颖视图合成产生了优异的结果。此外，我们介绍了3D TeX数据集，这是第一个包含红外图像及其相应的伪TeX视觉图像的数据集。实验证明，我们的方法不仅与高质量RGB图像实现的场景重建质量相匹配，而且为场景中的对象提供了准确的温度估计。 et.al.|[2410.04873](http://arxiv.org/abs/2410.04873)|null|

<p align=right>(<a href=#updated-on-20241013>back to top</a>)</p>

## 3D Reconstruction

|Publish Date|Title|Abstract|PDF|Code|
|---|---|---|---|---|
|**2024-10-10**|**Efficient Perspective-Correct 3D Gaussian Splatting Using Hybrid Transparency**|3D高斯散斑（3DGS）已被证明是一种通用的渲染图元，既可用于反向渲染，也可用于场景的实时探索。在这些应用中，相机帧和多个视图之间的连贯性至关重要，无论是场景重建的鲁棒收敛还是无伪影的飞行。最近的工作开始减轻破坏多视图一致性的伪影，包括由于不一致的透明度排序和（2D）斑点的透视校正轮廓而产生的爆裂伪影。与此同时，实时要求迫使这些实现在如何解决大型3D高斯组件的透明度方面做出妥协，从而以其他方式破坏了一致性。在我们的工作中，我们的目标是通过渲染完全透视正确的3D高斯分布，同时在每个像素级别使用精确混合的高质量近似值，混合透明度，以保持实时帧率，从而实现最大的连贯性。我们用于评估3D高斯分布的快速且透视准确的方法不需要矩阵求逆，从而确保了数值稳定性，消除了对退化斑点进行特殊处理的需要，混合透明度公式以渲染成本的一小部分保持了与完全分辨的每像素透明度相似的质量。我们进一步证明，这两个组件中的每一个都可以独立地集成到高斯溅射系统中。结合起来，与常见基准上的传统3DGS相比，它们实现了高达2美元/倍的帧率，2美元/秒的优化速度，以及相同或更好的图像质量，渲染伪影更少。 et.al.|[2410.08129](http://arxiv.org/abs/2410.08129)|null|
|**2024-10-10**|**UW-SDF: Exploiting Hybrid Geometric Priors for Neural SDF Reconstruction from Underwater Multi-view Monocular Images**|由于水下环境的独特性，水下物体的精确三维重建在水下勘探和测绘等任务中是一个具有挑战性的问题。依赖于多个传感器数据进行3D重建的传统方法非常耗时，并且在水下场景的数据采集中面临挑战。我们提出了UW-SDF，这是一种基于神经SDF的多视点水下图像重建目标对象的框架。我们引入混合几何先验来优化重建过程，显著提高了神经SDF重建的质量和效率。此外，为了解决多视图图像中分割一致性的挑战，我们提出了一种使用通用分割模型（SAM）的新的少镜头多视图目标分割策略，能够快速自动分割看不见的物体。通过对不同数据集进行广泛的定性和定量实验，我们证明我们提出的方法在水下3D重建领域优于传统的水下3D重构方法和其他神经渲染方法。 et.al.|[2410.08092](http://arxiv.org/abs/2410.08092)|null|
|**2024-10-10**|**Fine-detailed Neural Indoor Scene Reconstruction using multi-level importance sampling and multi-view consistency**|最近，室内场景中的神经隐式3D重建因其简单性和令人印象深刻的性能而变得流行。以前的工作可以利用正常或深度的单眼先验产生完整的结果。然而，由于无偏采样和不准确的单眼先验，它们可能会遭受过度平滑的重建和长期优化。在这篇论文中，我们提出了一种新的神经隐式表面重建方法，称为FD-NeuS，使用多级重要性采样策略和多视图一致性方法来学习精细详细的3D模型。具体来说，我们利用分割先验来指导基于区域的射线采样，并使用分段指数函数作为权重来引导沿射线的3D点采样，从而确保对重要区域的更多关注。此外，我们分别引入多视图特征一致性和多视图正态一致性作为监督和不确定性，进一步改善了细节的重建。大量的定量和定性结果表明，FD NeuS在各种场景中都优于现有方法。 et.al.|[2410.07597](http://arxiv.org/abs/2410.07597)|null|
|**2024-10-10**|**3D Vision-Language Gaussian Splatting**|3D重建方法和视觉语言模型的最新进展推动了多模态3D场景理解的发展，这在机器人、自动驾驶和虚拟/增强现实中具有重要应用。然而，当前的多模态场景理解方法天真地将语义表示嵌入到3D重建方法中，而没有在视觉和语言模态之间取得平衡，这导致半透明或反射对象的语义光栅化不令人满意，以及对颜色模态的过拟合。为了缓解这些局限性，我们提出了一种解决方案，充分处理不同的视觉和语义模态，即用于场景理解的3D视觉语言高斯飞溅模型，以强调语言模态的表示学习。我们提出了一种新的跨模态光栅化器，使用模态融合和平滑的语义指示符来增强语义光栅化。我们还采用相机视图混合技术来提高现有视图和合成视图之间的语义一致性，从而有效地减轻过拟合。大量实验表明，我们的方法在开放式词汇语义切分方面取得了最先进的性能，远远超过了现有的方法。 et.al.|[2410.07577](http://arxiv.org/abs/2410.07577)|null|
|**2024-10-09**|**3D2M Dataset: A 3-Dimension diverse Mesh Dataset**|三维（3D）重建已成为一个突出的研究领域，引起了学术界和工业界的广泛关注。在3D重建的各种应用中，面部重建带来了一些最艰巨的挑战。此外，每个人的面部结构都是独一无二的，需要算法足够稳健，以处理这种变化，同时保持对原始特征的保真度。本文介绍了一个全面的3D网格数据集，其中包含各种面部结构和相应的面部标志。该数据集包括188个3D面部网格，其中73个来自女性候选人，114个来自男性候选人。它涵盖了广泛的种族背景，有来自45个不同种族的贡献，确保了面部特征的丰富多样性。每个面部网格都有关键点，可以准确地注释相关特征，便于精确分析和操作。该数据集对于面部重新定位、面部结构成分研究和视频流中的实时人物表示等应用特别有价值。通过为研究人员和开发人员提供强大的资源，它旨在推进3D面部重建和相关技术领域的发展。 et.al.|[2410.07415](http://arxiv.org/abs/2410.07415)|**[link](https://github.com/sohomd/3D2M-Dataset)**|
|**2024-10-09**|**Z-upscaling: Optical Flow Guided Frame Interpolation for Isotropic Reconstruction of 3D EM Volumes**|我们提出了一种新的基于光流的方法来提高各向异性3D EM体积的轴向分辨率，以实现各向同性3D重建。假设在对齐良好的EM体积中3D生物结构的空间连续性，我们推断可以利用通常用于视频时间分辨率增强的光流估计技术。像素级运动是在沿z的相邻2D切片之间估计的，使用空间梯度流估计来插值和生成新的2D切片，从而得到各向同性体素。我们利用最新的最先进的学习方法进行视频帧插值和迁移学习技术，并在公开的超微结构EM体积上证明了我们的方法的成功。 et.al.|[2410.07043](http://arxiv.org/abs/2410.07043)|**[link](https://github.com/fisseha21/z-upscaling)**|
|**2024-10-09**|**ES-Gaussian: Gaussian Splatting Mapping via Error Space-Based Gaussian Completion**|准确且经济实惠的室内3D重建对于有效的机器人导航和交互至关重要。传统的基于激光雷达的测绘提供了高精度，但成本高、重量重、功耗大，新颖的视图渲染能力有限。基于视觉的测绘虽然经济高效，能够捕获视觉数据，但由于稀疏的点云，往往难以进行高质量的3D重建。我们提出了ES Gaussian，这是一种端到端系统，使用低空相机和单线LiDAR进行高质量的3D室内重建。我们的系统具有视觉误差构造（VEC）功能，通过识别和校正二维误差图中几何细节不足的区域来增强稀疏点云。此外，我们介绍了一种由单线LiDAR引导的新型3DGS初始化方法，克服了传统多视图设置的局限性，并在资源受限的环境中实现了有效的重建。我们新的Dreame SR数据集和公开数据集的大量实验结果表明，ES Gaussian优于现有方法，特别是在具有挑战性的场景中。项目页面可在https://chenlu-china.github.io/ES-Gaussian/. et.al.|[2410.06613](http://arxiv.org/abs/2410.06613)|null|
|**2024-10-08**|**Comparative Analysis of Novel View Synthesis and Photogrammetry for 3D Forest Stand Reconstruction and extraction of individual tree parameters**|准确高效的树木三维重建对于森林资源评估和管理至关重要。近景摄影测量（CRP）通常用于重建森林场景，但面临着效率低、质量差等挑战。最近，包括神经辐射场（NeRF）和3D高斯散斑（3DGS）在内的新型视图合成（NVS）技术已显示出在有限图像下进行3D植物重建的前景。然而，现有的研究主要集中在果园或单株树木中的小型植物上，这给它们在更大、更复杂的林分中的应用带来了不确定性。在这项研究中，我们收集了具有不同复杂性的森林地块的连续图像，并使用NeRF和3DGS进行了密集重建。将得到的点云与摄影测量和激光扫描的点云进行了比较。结果表明，NVS方法显著提高了重建效率。摄影测量难以处理复杂的林分，导致点云的树冠噪声过大，树木重建不正确，如树干重复。NeRF虽然对树冠区域更好，但在视野有限的地面区域可能会产生误差。3DGS方法生成更稀疏的点云，特别是在主干区域，影响胸径（DBH）精度。这三种方法都可以提取树高信息，其中NeRF的精度最高；然而，摄影测量在DBH精度方面仍然具有优势。这些发现表明，NVS方法在林分三维重建方面具有巨大潜力，为复杂的森林资源清查和可视化任务提供了宝贵支持。 et.al.|[2410.05772](http://arxiv.org/abs/2410.05772)|null|
|**2024-10-08**|**Single picture single photon single pixel 3D imaging through unknown thick scattering medium**|通过厚散射介质成像带来了重大挑战，特别是对于三维（3D）应用。这份手稿展示了一种通过这种介质实现单图像3D成像的新方案，将散射介质视为透镜。这种方法可以捕获包含隐藏在不同深度的物体信息的综合图像。通过利用离焦深度和散射介质厚度的减小进行单像素成像，所提出的方法确保了强大的3D成像能力。我们开发了传统的基于度量和基于深度学习的方法来提取每个像素的深度信息，使我们能够探索正面和负面物体的位置，无论是浅层还是深层。值得注意的是，该方案能够同时对隐藏在散射介质中的目标进行3D重建。具体来说，我们成功地重建了埋在5毫米和30毫米深处的目标，总介质厚度为60毫米。此外，我们可以有效地区分三个不同深度的目标。值得注意的是，该方案不需要散射介质的先验知识，也不需要侵入性程序、参考测量或校准。 et.al.|[2410.05607](http://arxiv.org/abs/2410.05607)|null|
|**2024-10-07**|**SharpSLAM: 3D Object-Oriented Visual SLAM with Deblurring for Agile Drones**|本文重点研究了通过提高RGB图像质量来提高DSP-SLAM中3D重建和分割质量的算法。我们开发的SharpSLAM算法旨在通过图像去模糊来减少高动态运动对视觉面向对象SLAM的影响，改进面向对象SLPM的各个方面，包括定位、映射和对象重建。实验结果表明，由于特征和相应地图点的数量增加，目标检测质量显著提高，F评分从82.9%提高到86.2%。有符号距离函数的RMSE也从17.2厘米降低到15.4厘米。此外，我们的解决方案增强了对象定位，IoU从74.5%增加到75.7%。SharpSLAM算法有可能大大提高DSP-SLAM中3D重建和分割的质量，并影响广泛的领域，包括机器人、自动驾驶汽车和增强现实。 et.al.|[2410.05405](http://arxiv.org/abs/2410.05405)|null|

<p align=right>(<a href=#updated-on-20241013>back to top</a>)</p>

## Diffusion

|Publish Date|Title|Abstract|PDF|Code|
|---|---|---|---|---|
|**2024-10-10**|**Emerging Pixel Grounding in Large Multimodal Models Without Grounding Supervision**|当前的大型多模态模型（LMM）在基础方面面临挑战，这要求模型将语言组件与视觉实体联系起来。与通常通过额外的接地监督来微调LMM的做法相反，我们发现，在没有明确接地监督的情况下，经过训练的LMM实际上可以产生接地能力。为了揭示这一新兴的基础，我们引入了一种“参与和分割”方法，该方法利用标准LMM中的注意力图进行像素级分割。此外，为了增强接地能力，我们提出了DIFFLMM，这是一种利用基于扩散的视觉编码器的LMM，与标准CLIP视觉编码器相反，并使用相同的弱监督进行训练。在不受偏见和特定监管数据规模限制的情况下，我们的方法更具普遍性和可扩展性。与基础LMM和通才LMM相比，我们在基础特定和一般视觉问答基准上都取得了具有竞争力的性能。值得注意的是，在没有任何接地监督的情况下，我们在接地对话生成上实现了44.2的接地掩码召回，表现优于广泛监督模型GLaMM。项目页面：https://groundLMM.github.io. et.al.|[2410.08209](http://arxiv.org/abs/2410.08209)|null|
|**2024-10-10**|**DICE: Discrete Inversion Enabling Controllable Editing for Multinomial Diffusion and Masked Generative Models**|离散扩散模型在图像生成和掩码语言建模等任务中取得了成功，但在受控内容编辑方面面临局限性。我们介绍了DICE（可控编辑的离散反演），这是第一种实现离散扩散模型精确反演的方法，包括多项式扩散和掩码生成模型。通过在反向扩散过程中记录噪声序列和掩蔽模式，DICE能够准确重建和灵活编辑离散数据，而不需要预定义的掩蔽或注意力操纵。我们在VQ Diffusion、Paella和RoBERTa等模型上评估了DICE在图像和文本领域的有效性。我们的结果表明，DICE在增强编辑能力的同时保持了高数据保真度，为离散空间中的细粒度内容操作提供了新的机会。有关项目网页，请参阅https://hexiaoxiao-cs.github.io/DICE/. et.al.|[2410.08207](http://arxiv.org/abs/2410.08207)|null|
|**2024-10-10**|**HybridBooth: Hybrid Prompt Inversion for Efficient Subject-Driven Generation**|文本到图像扩散模型的最新进展表明，文本提示具有非凡的创造性，但基于特定主题生成个性化实例，即主题驱动生成，仍然具有挑战性。为了解决这个问题，我们提出了一个新的混合框架HybridBooth，它融合了基于优化和直接回归方法的优点。HybridBooth分两个阶段运行：单词嵌入探测，使用微调编码器生成稳健的初始单词嵌入；单词嵌入细化，通过优化关键参数进一步使编码器适应特定的主题图像。这种方法允许将视觉概念有效快速地转化为文本嵌入，即使是从单个图像中，同时保持模型的泛化能力。 et.al.|[2410.08192](http://arxiv.org/abs/2410.08192)|null|
|**2024-10-10**|**DifFRelight: Diffusion-Based Facial Performance Relighting**|我们提出了一种使用基于扩散的图像到图像转换的自由视点面部表现再照明的新框架。利用包含在各种照明条件下捕获的不同面部表情的特定主题数据集，包括平面照明和一次一光（OLAT）场景，我们训练了一个用于精确照明控制的扩散模型，从而能够从平面照明输入中获得高保真度的面部图像。我们的框架包括平面光捕获和随机噪声的空间对齐调节，以及用于全局控制的集成照明信息，利用预训练的稳定扩散模型的先验知识。然后将该模型应用于在一致的平面照明环境中捕获的动态面部表现，并使用可扩展的动态3D高斯散斑方法进行重建，以保持重新照明结果的质量和一致性，从而进行新的视图合成。此外，我们通过将新颖的区域照明表示与定向照明集成，引入了统一的照明控制，允许对灯光大小和方向进行联合调整。我们还使用多个方向光实现高动态范围成像（HDRI）合成，以在复杂的照明条件下产生动态序列。我们的评估表明，模型在实现精确的照明控制和跨各种面部表情的泛化方面非常有效，同时保留了皮肤纹理和头发等详细特征。该模型准确地再现了复杂的照明效果，如眼睛反射、次表面散射、自阴影和半透明，在我们的框架内推进了照片真实感。 et.al.|[2410.08188](http://arxiv.org/abs/2410.08188)|null|
|**2024-10-10**|**Scaling Laws For Diffusion Transformers**|扩散变换器（DiT）已经在内容娱乐中实现了吸引人的合成和缩放特性，例如图像和视频生成。然而，DiT的缩放定律探索较少，在给定特定计算预算的情况下，这些定律通常可以提供关于最佳模型大小和数据要求的精确预测。因此，在从1e17到6e18的广泛计算预算范围内进行了实验，以首次确认DiT中存在缩放定律。具体来说，预训练DiT的损失也与所涉及的计算呈幂律关系。基于缩放定律，我们不仅可以确定最佳模型大小和所需数据，还可以在给定1B参数和1e21 FLOP计算预算的模型下准确预测文本到图像的生成损失。此外，我们还证明，即使在各种数据集上，预训练损失的趋势也与生成性能（如FID）相匹配，这补充了从计算到合成质量的映射，从而提供了一个可预测的基准，以较低的成本评估模型性能和数据质量。 et.al.|[2410.08184](http://arxiv.org/abs/2410.08184)|null|
|**2024-10-10**|**ZeroComp: Zero-shot Object Compositing from Image Intrinsics via Diffusion**|我们提出了ZeroComp，这是一种有效的零样本3D对象合成方法，在训练过程中不需要成对的合成场景图像。我们的方法利用ControlNet从内在图像中进行调节，并将其与稳定扩散模型相结合，以利用其场景先验，共同作为一个有效的渲染引擎运行。在训练过程中，ZeroComp使用基于几何、反照率和蒙版着色的固有图像，所有这些都不需要有和没有合成对象的场景的成对图像。经过训练后，它可以将虚拟3D对象无缝集成到场景中，调整着色以创建逼真的合成效果。我们开发了一个高质量的评估数据集，并证明ZeroComp在定量和人类感知基准测试中优于使用显式照明估计和生成技术的方法。此外，ZeroComp扩展到真实和室外图像合成，即使仅在合成室内数据上进行训练，也能展示其在图像合成中的有效性。 et.al.|[2410.08168](http://arxiv.org/abs/2410.08168)|null|
|**2024-10-10**|**DART: Denoising Autoregressive Transformer for Scalable Text-to-Image Generation**|扩散模型已成为视觉生成的主要方法。它们是通过对马尔可夫过程进行去噪来训练的，该过程会逐渐向输入中添加噪声。我们认为，马尔可夫性质限制了模型充分利用生成轨迹的能力，导致训练和推理过程中效率低下。在本文中，我们提出了DART，这是一种基于变换器的模型，在非马尔可夫框架内统一了自回归（AR）和扩散。DART使用与标准语言模型具有相同架构的AR模型在空间和光谱上迭代去噪图像块。DART不依赖于图像量化，在保持灵活性的同时实现了更有效的图像建模。此外，DART在统一模型中使用文本和图像数据进行无缝训练。我们的方法在类条件和文本到图像生成任务上表现出了具有竞争力的性能，为传统的扩散模型提供了一种可扩展、高效的替代方案。通过这个统一的框架，DART为可扩展的高质量图像合成设定了新的基准。 et.al.|[2410.08159](http://arxiv.org/abs/2410.08159)|null|
|**2024-10-10**|**Progressive Autoregressive Video Diffusion Models**|当前的前沿视频扩散模型在生成高质量视频方面取得了显著成果。然而，由于训练过程中的计算限制，它们只能生成短视频片段，通常约为10秒或240帧。在这项工作中，我们表明，现有的模型可以自然地扩展到自回归视频扩散模型，而无需改变架构。我们的关键思想是为潜在帧分配逐渐增加的噪声水平，而不是单个噪声水平，这允许延迟之间的细粒度条件和注意力窗口之间的大重叠。这种渐进式视频去噪使我们的模型能够自回归地生成视频帧，而不会出现质量下降或突然的场景变化。我们展示了1分钟长视频生成（1440帧，24 FPS）的最新结果。本文的视频可在https://desaixie.github.io/pa-vdm/. et.al.|[2410.08151](http://arxiv.org/abs/2410.08151)|**[link](https://github.com/desaixie/pa_vdm)**|
|**2024-10-10**|**Steering Masked Discrete Diffusion Models via Discrete Denoising Posterior Prediction**|离散数据的生成建模是重要应用的基础，从基于文本的代理（如ChatGPT）到蛋白质序列中生命构建块的设计。然而，应用程序域需要通过引导生成过程（通常是通过RLHF）来控制生成的数据，以满足指定的属性、奖励或亲和力度量。在本文中，我们研究了操纵掩蔽扩散模型（MDMs）的问题，这是一类最近的离散扩散模型，为传统的自回归模型提供了一种令人信服的替代方案。我们引入了离散去噪后验预测（DDPP），这是一种新的框架，通过学习从目标贝叶斯后验中采样，将指导预训练的MDM的任务转化为概率推理问题。我们的DDPP框架产生了一个由三个新目标组成的家族，这些目标都是无模拟的，因此在应用于一般不可微的奖励函数时是可扩展的。根据经验，我们通过引导MDMs执行类条件像素级图像建模、使用基于文本的奖励对MDMs进行基于RLHF的比对，以及微调蛋白质语言模型以生成更多样化的二级结构和更短的蛋白质来实例化DDPP。我们通过湿实验室验证来证实我们的设计，在那里我们观察到奖励优化蛋白序列的瞬时表达。 et.al.|[2410.08134](http://arxiv.org/abs/2410.08134)|null|
|**2024-10-10**|**CrackSegDiff: Diffusion Probability Model-based Multi-modal Crack Segmentation**|在道路检查机器人中集成灰度和深度数据可以提高道路状况评估的准确性、可靠性和全面性，从而改善维护策略和更安全的基础设施。然而，这些数据源经常受到路面显著背景噪声的影响。扩散概率模型（DPM）的最新进展在图像分割任务中取得了显著成功，展示了强大的去噪能力，如SegDiff\cite{amit2021segdiff}等研究所证明的那样。尽管取得了这些进步，但目前基于DPM的分割器并没有充分利用原始图像数据的潜力。本文提出了一种新的基于DPM的裂纹分割方法，称为CrackSegDiff，它独特地融合了灰度和距离/深度图像。该方法通过增强DPM局部特征提取和全局特征提取之间的相互作用来增强反向扩散过程。与利用变换器进行全局特征的传统方法不同，我们的方法采用Vm unet \cite{ruan2024vm}来有效地捕获原始数据的远程信息。通过两个创新模块进一步完善了特征的集成：信道融合模块（CFM）和浅层特征补偿模块（SFCM）。我们对FIND数据集中三类裂纹图像分割任务的实验评估表明，CrackSegDiff优于最先进的方法，特别是在检测浅裂纹方面。代码可在以下网址获得https://github.com/sky-visionX/CrackSegDiff. et.al.|[2410.08100](http://arxiv.org/abs/2410.08100)|**[link](https://github.com/sky-visionx/cracksegdiff)**|

<p align=right>(<a href=#updated-on-20241013>back to top</a>)</p>

## NeRF

|Publish Date|Title|Abstract|PDF|Code|
|---|---|---|---|---|
|**2024-10-07**|**Fast Training of Sinusoidal Neural Fields via Scaling Initialization**|神经场是一种新兴的范式，它将数据表示为由神经网络参数化的连续函数。尽管有许多优点，但神经场通常具有较高的训练成本，这阻碍了更广泛的采用。在本文中，我们关注一个流行的神经场家族，称为正弦神经场（SNF），并研究如何初始化它以最大限度地提高训练速度。我们发现，基于信号传播原理设计的SNF标准初始化方案是次优的。特别是，我们证明，通过简单地将每个权重（最后一层除外）乘以一个常数，我们可以将SNF训练加速10 $\times$。这种方法被称为$\textit{weight scaling}$ ，在各种数据域上持续提供显著的加速，使SNF的训练速度比最近提出的架构更快。为了理解为什么权重缩放效果良好，我们进行了广泛的理论和实证分析，结果表明，权重缩放不仅有效地解决了频谱偏差，而且具有良好的优化轨迹。 et.al.|[2410.04779](http://arxiv.org/abs/2410.04779)|null|
|**2024-10-04**|**End-to-End Reaction Field Energy Modeling via Deep Learning based Voxel-to-voxel Transform**|在计算生物化学和生物物理学中，理解静电相互作用的作用对于阐明生物分子的结构、动力学和功能至关重要。泊松-玻尔兹曼（PB）方程是通过描述带电分子内部和周围的静电势来模拟这些相互作用的基础工具。然而，由于生物分子表面的复杂性和需要考虑可移动离子，求解PB方程带来了重大的计算挑战。虽然求解PB方程的传统数值方法是准确的，但它们的计算成本很高，并且随着系统规模的增加而扩展性较差。为了应对这些挑战，我们引入了PBNeF，这是一种新的机器学习方法，灵感来自基于神经网络的偏微分方程求解器的最新进展。我们的方法将PB方程的输入和边界静电条件转化为可学习的体素表示，使神经场变换器能够预测PB解，进而预测反应场势能。大量实验表明，与传统的PB求解器相比，PBNeF的速度提高了100倍以上，同时保持了与广义玻恩（GB）模型相当的精度。 et.al.|[2410.03927](http://arxiv.org/abs/2410.03927)|null|
|**2024-10-08**|**DressRecon: Freeform 4D Human Reconstruction from Monocular Video**|我们提出了一种从单目视频中重建时间一致的人体模型的方法，重点是极其宽松的衣服或手持物体的交互。之前在人体重建方面的工作要么局限于没有物体交互的紧身衣服，要么需要校准的多视图捕捉或个性化的模板扫描，而大规模收集这些数据成本很高。我们对高质量但灵活的重建的关键见解是，将关于关节体形状的通用人类先验（从大规模训练数据中学习）与视频特定的关节“骨骼袋”变形（通过测试时间优化适合单个视频）仔细结合。我们通过学习一个神经隐式模型来实现这一点，该模型将身体和衣服的变形作为单独的运动模型层来解开。为了捕捉服装的微妙几何形状，我们在优化过程中利用了基于图像的先验，如人体姿势、表面法线和光流。由此产生的神经场可以提取到时间一致的网格中，或进一步优化为显式3D高斯分布，以实现高保真交互式渲染。在具有高度挑战性的服装变形和物体交互的数据集上，DressReston可以产生比现有技术更高保真的3D重建。项目页面：https://jefftan969.github.io/dressrecon/ et.al.|[2409.20563](http://arxiv.org/abs/2409.20563)|null|
|**2024-09-25**|**TalkinNeRF: Animatable Neural Fields for Full-Body Talking Humans**|我们介绍了一种新的框架，该框架从单眼视频中学习全身说话的人的动态神经辐射场（NeRF）。之前的工作只代表身体姿势或面部。然而，人类通过全身进行交流，结合身体姿势、手势和面部表情。在这项工作中，我们提出了TalkinNeRF，这是一个基于NeRF的统一网络，代表了整体4D人体运动。给定一个受试者的单眼视频，我们学习身体、面部和手的相应模块，这些模块结合在一起生成最终结果。为了捕捉复杂的手指关节，我们学习了手的额外变形场。我们的多身份表示能够同时训练多个科目，以及在完全看不见的姿势下进行强大的动画。只要输入一段短视频，它也可以推广到新的身份。我们展示了最先进的性能，用于为全身说话的人类制作动画，具有精细的手部发音和面部表情。 et.al.|[2409.16666](http://arxiv.org/abs/2409.16666)|null|
|**2024-09-24**|**Generative 3D Cardiac Shape Modelling for In-Silico Trials**|我们提出了一种深度学习方法，基于将形状表示为神经有符号距离场的零级集，对合成主动脉形状进行建模和生成，该方法受一系列可训练的嵌入向量的约束，并对每个形状的几何特征进行编码。通过使神经场在采样表面点上消失并强制其空间梯度具有单位范数，在从CT图像重建的主动脉根部网格数据集上训练网络。实证结果表明，我们的模型可以高保真地表示主动脉形状。此外，通过从学习到的嵌入向量中采样，我们可以生成类似于真实患者解剖结构的新形状，可用于计算机模拟试验。 et.al.|[2409.16058](http://arxiv.org/abs/2409.16058)|null|
|**2024-09-21**|**MOSE: Monocular Semantic Reconstruction Using NeRF-Lifted Noisy Priors**|由于缺乏几何指导和不完美的视图相关2D先验，从单眼图像中精确重建密集和语义注释的3D网格仍然是一项具有挑战性的任务。尽管我们已经见证了隐式神经场景表示的最新进展，能够简单地从多视图图像中进行精确的2D渲染，但很少有研究仅使用单眼先验来解决3D场景理解问题。在本文中，我们提出了MOSE，这是一种神经场语义重建方法，可以将推断的图像级噪声先验提升到3D，在3D和2D空间中产生精确的语义和几何。我们方法的关键动机是利用通用类不可知的分段掩码作为指导，在训练过程中促进渲染语义的局部一致性。在语义的帮助下，我们进一步将平滑正则化应用于无纹理区域，以获得更好的几何质量，从而实现几何和语义的互惠互利。在ScanNet数据集上的实验表明，我们的MOSE在3D语义分割、2D语义分割和3D表面重建任务的所有指标上都优于相关基线。 et.al.|[2409.14019](http://arxiv.org/abs/2409.14019)|null|
|**2024-09-17**|**SplatFields: Neural Gaussian Splats for Sparse 3D and 4D Reconstruction**|从多视图图像中数字化3D静态场景和4D动态事件长期以来一直是计算机视觉和图形学领域的一个挑战。最近，3D高斯散斑（3DGS）已经成为一种实用且可扩展的重建方法，由于其令人印象深刻的重建质量、实时渲染能力以及与广泛使用的可视化工具的兼容性而越来越受欢迎。然而，该方法需要大量的输入视图来实现高质量的场景重建，这引入了一个重大的实际瓶颈。在捕捉动态场景时，这一挑战尤为严峻，因为部署广泛的相机阵列的成本可能高得令人望而却步。在这项工作中，我们发现斑点特征缺乏空间自相关性是导致3DGS技术在稀疏重建环境中性能不佳的因素之一。为了解决这个问题，我们提出了一种优化策略，通过将splat特征建模为相应隐式神经场的输出，有效地正则化splat特征。这导致在各种场景中重建质量的一致提高。我们的方法有效地处理了静态和动态情况，这在不同设置和场景复杂性的广泛测试中得到了证明。 et.al.|[2409.11211](http://arxiv.org/abs/2409.11211)|null|
|**2024-10-02**|**Neural Fields for Adaptive Photoacoustic Computed Tomography**|光声计算机断层扫描（PACT）是一种具有广泛医学应用的非侵入性成像技术。传统的PACT图像重建算法受到组织中声速不均匀（SOS）引起的波前失真的影响，导致图像质量下降。考虑到这些影响可以提高图像质量，但测量SOS分布的实验成本很高。另一种方法是仅使用PA信号对初始压力图像和SOS进行联合重建。现有的关节重建方法存在局限性：计算成本高，无法直接恢复SOS，以及依赖于不准确的简化假设。隐式神经表示或神经场是计算机视觉中的一种新兴技术，用于通过基于坐标的神经网络学习物理场的有效和连续表示。在这项工作中，我们介绍了NF-APACT，这是一种高效的自监督框架，利用神经场来估计SOS，以实现准确和鲁棒的多通道解卷积。我们的方法比现有方法更快、更准确地消除了SOS像差。我们在一个新的数值体模以及实验收集的体模和体内数据上证明了我们的方法的成功。我们的代码和数字幻影可在https://github.com/Lukeli0425/NF-APACT. et.al.|[2409.10876](http://arxiv.org/abs/2409.10876)|null|
|**2024-09-09**|**Lagrangian Hashing for Compressed Neural Field Representations**|我们提出了拉格朗日散列，这是一种神经场的表示，结合了依赖于欧拉网格（即~InstantNGP）的快速训练NeRF方法的特征，以及使用配备有特征的点作为表示信息的方法（例如3D高斯散点或PointNeRF）。我们通过将基于点的表示合并到InstantNGP表示的分层哈希表的高分辨率层中来实现这一点。由于我们的点具有影响域，我们的表示可以被解释为哈希表中存储的高斯混合。我们提出的损失鼓励我们的高斯人向需要更多代表预算才能充分代表的地区移动。我们的主要发现是，我们的表示允许使用更紧凑的表示来重建信号，而不会影响质量。 et.al.|[2409.05334](http://arxiv.org/abs/2409.05334)|null|
|**2024-09-08**|**Exploring spectropolarimetric inversions using neural fields. Solar chromospheric magnetic field under the weak-field approximation**|全斯托克斯偏振数据集来源于狭缝光谱仪或窄带滤光片图，如今已被常规采集。随着二维光谱偏振仪和允许长时间高质量观测序列的观测技术的出现，数据速率正在增加。在光谱偏振反演中，显然需要通过利用推断物理量的时空相干性来超越传统的逐像素策略。我们探索了神经网络作为时间和空间（也称为神经场）上物理量的连续表示的潜力，用于光谱极化反演。我们已经实现并测试了一个神经场，以在弱场近似（WFA）下执行磁场矢量的推理（也称为物理知情神经网络的方法）。通过使用神经场来描述磁场矢量，我们可以通过假设物理量是坐标的连续函数来在空间和时间域中正则化解。我们研究了Ca II 8542 A谱线的合成和真实观测结果。我们还探讨了其他显式正则化的影响，例如使用外推磁场的信息或色球原纤维的取向。与传统的逐像素反演相比，神经场方法提高了磁场矢量重建的保真度，特别是横向分量。这种隐式正则化是一种提高观测值有效信噪比的方法。虽然它比逐像素WFA估计慢，但这种方法通过减少自由参数的数量并在解决方案中引入时空约束，显示出深度分层反演的巨大潜力。 et.al.|[2409.05156](http://arxiv.org/abs/2409.05156)|**[link](https://github.com/cdiazbas/neural_wfa)**|

<p align=right>(<a href=#updated-on-20241013>back to top</a>)</p>

[contributors-shield]: https://img.shields.io/github/contributors/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[contributors-url]: https://github.com/Vincentqyw/cv-arxiv-daily/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[forks-url]: https://github.com/Vincentqyw/cv-arxiv-daily/network/members
[stars-shield]: https://img.shields.io/github/stars/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[stars-url]: https://github.com/Vincentqyw/cv-arxiv-daily/stargazers
[issues-shield]: https://img.shields.io/github/issues/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[issues-url]: https://github.com/Vincentqyw/cv-arxiv-daily/issues

