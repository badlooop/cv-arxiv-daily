[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]

## Updated on 2024.10.14
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
|**2024-10-11**|**Look Gauss, No Pose: Novel View Synthesis using Gaussian Splatting without Accurate Pose Initialization**|3D高斯散斑最近已经成为一种强大的工具，可以从一组摆姿势的输入图像中快速准确地合成新的视图。然而，与大多数新颖的视图合成方法一样，它依赖于精确的相机姿态信息，这限制了它在真实世界场景中的适用性，在这些场景中，获取准确的相机姿态可能具有挑战性，甚至是不可能的。我们提出了一种对3D高斯散斑框架的扩展，通过优化与光度残差相关的外部相机参数。我们推导了分析梯度，并将其计算与现有的高性能CUDA实现相结合。这使得下游任务成为可能，如6-DoF相机姿态估计以及联合重建和相机细化。特别是，我们实现了真实场景中姿态估计的快速收敛和高精度。我们的方法通过联合优化几何和相机姿态，实现了快速重建3D场景，而不需要精确的姿态信息，同时在新颖的视图合成中实现了最先进的结果。我们的方法比大多数竞争方法优化速度快得多，渲染速度也快几倍。我们通过模拟环境在真实场景和复杂轨迹上显示结果，在LLFF上实现了最先进的结果，同时与最有效的竞争方法相比，运行时间缩短了两到四倍。源代码将在https://github.com/Schmiddo/noposegs . et.al.|[2410.08743](http://arxiv.org/abs/2410.08743)|**[link](https://github.com/schmiddo/noposegs)**|
|**2024-10-10**|**DifFRelight: Diffusion-Based Facial Performance Relighting**|我们提出了一种使用基于扩散的图像到图像转换的自由视点面部表现再照明的新框架。利用包含在各种照明条件下捕获的不同面部表情的特定主题数据集，包括平面照明和一次一光（OLAT）场景，我们训练了一个用于精确照明控制的扩散模型，从而能够从平面照明输入中获得高保真度的面部图像。我们的框架包括平面光捕获和随机噪声的空间对齐调节，以及用于全局控制的集成照明信息，利用预训练的稳定扩散模型的先验知识。然后将该模型应用于在一致的平面照明环境中捕获的动态面部表现，并使用可扩展的动态3D高斯散斑方法进行重建，以保持重新照明结果的质量和一致性，从而进行新的视图合成。此外，我们通过将新颖的区域照明表示与定向照明集成，引入了统一的照明控制，允许对灯光大小和方向进行联合调整。我们还使用多个方向光实现高动态范围成像（HDRI）合成，以在复杂的照明条件下产生动态序列。我们的评估表明，模型在实现精确的照明控制和跨各种面部表情的泛化方面非常有效，同时保留了皮肤纹理和头发等详细特征。该模型准确地再现了复杂的照明效果，如眼睛反射、次表面散射、自阴影和半透明，在我们的框架内推进了照片真实感。 et.al.|[2410.08188](http://arxiv.org/abs/2410.08188)|null|
|**2024-10-10**|**IncEventGS: Pose-Free Gaussian Splatting from a Single Event Camera**|用于新颖视图合成的隐式神经表示和显式3D高斯散斑（3D-GS）最近在基于帧的相机（如RGB和RGB-D相机）方面取得了显著进展。与基于帧的相机相比，一种新型的仿生视觉传感器，即事件相机，在高时间分辨率、高动态范围、低功耗和低延迟方面具有优势。由于其独特的异步和不规则的数据捕获过程，将神经表示或3D高斯飞溅应用于事件相机的工作有限。在这项工作中，我们提出了IncEventGS，这是一种使用单事件相机的增量3D高斯散斑重建算法。为了逐步恢复3D场景表示，我们利用了IncEventGS的传统SLAM管道的跟踪和映射范式。给定传入的事件流，跟踪器首先基于先前重建的3D-GS场景表示来估计初始相机运动。然后，映射器基于来自跟踪器的先前估计的运动轨迹，联合细化3D场景表示和相机运动。实验结果表明，与之前的基于NeRF的方法和其他相关基线相比，IncEventGS具有更优的性能，即使我们没有地面实况相机姿态。此外，与最先进的事件视觉里程计方法相比，我们的方法在相机运动估计方面也可以提供更好的性能。代码可在以下网址公开获取：https://github.com/wu-cvgl/IncEventGS. et.al.|[2410.08107](http://arxiv.org/abs/2410.08107)|**[link](https://github.com/wu-cvgl/inceventgs)**|
|**2024-10-11**|**Fast Feedforward 3D Gaussian Splatting Compression**|随着3D高斯散斑（3DGS）推进了用于新颖视图合成的实时和高保真渲染，存储要求对其广泛采用提出了挑战。尽管已经提出了各种压缩技术，但现有技术存在一个共同的局限性：对于任何现有的3DGS，都需要按场景优化来实现压缩，这使得压缩缓慢而缓慢。为了解决这个问题，我们引入了3D高斯散布的快速压缩（FCGS），这是一种无需优化的模型，可以在一次前馈过程中快速压缩3DGS表示，从而将压缩时间从几分钟缩短到几秒钟。为了提高压缩效率，我们提出了一种多路径熵模块，该模块将高斯属性分配给不同的熵约束路径，以实现大小和保真度之间的平衡。我们还仔细设计了高斯间和高斯内上下文模型，以消除非结构化高斯斑点之间的冗余。总体而言，FCGS在保持保真度的同时实现了超过20倍的压缩比，超越了大多数基于每场景SOTA优化的方法。我们的代码可在以下网址获得：https://github.com/YihangChen-ee/FCGS. et.al.|[2410.08017](http://arxiv.org/abs/2410.08017)|**[link](https://github.com/yihangchen-ee/fcgs)**|
|**2024-10-08**|**BEVLoc: Cross-View Localization and Matching via Birds-Eye-View Synthesis**|地对空匹配是户外机器人技术中一项至关重要且具有挑战性的任务，特别是在GPS缺失或不可靠的情况下。建筑物或大型茂密森林等结构会产生干扰，需要GNSS替代全球定位估计。真正的困难在于调和地面和空中图像之间的视角差异，以实现可接受的定位。从自动驾驶社区获得灵感，我们提出了一种新的框架，用于合成鸟瞰图（BEV）场景表示，以在越野环境中与航空地图进行匹配和定位。我们利用对比学习和特定领域的硬负挖掘来训练网络，以学习合成BEV和航空地图之间的相似表示。在推理过程中，BEVLoc通过从粗到细的匹配策略引导识别航空地图中最可能的位置。我们的研究结果表明，在语义多样性有限的极其困难的森林环境中，初步结果很有希望。我们分析了模型的粗匹配和细匹配性能，评估了模型的原始匹配能力及其作为GNSS替代品的性能。我们的工作深入研究了越野地图本地化，同时为本地化的未来发展建立了基础基线。我们的代码可在以下网址获得：https://github.com/rpl-cmu/bevloc et.al.|[2410.06410](http://arxiv.org/abs/2410.06410)|null|
|**2024-10-08**|**HiSplat: Hierarchical 3D Gaussian Splatting for Generalizable Sparse-View Reconstruction**|从多个视点重建3D场景是立体视觉中的一项基本任务。最近，可推广的3D高斯散斑技术的进步通过前馈预测每像素高斯参数而无需额外优化，实现了从稀疏输入视图中为看不见的场景进行高质量的新颖视图合成。然而，现有的方法通常生成单尺度3D高斯分布，缺乏对大规模结构和纹理细节的表示，导致定位错误和伪影。本文提出了一种新的框架HiSplat，该框架在可推广的3D高斯散点中引入了一种分层方式，通过从粗到细的策略构建分层的3D高斯分布。具体来说，HiSplat生成大的粗粒度高斯分布来捕捉大规模结构，然后生成细粒度高斯分布来增强精细的纹理细节。为了促进尺度间的相互作用，我们提出了一个用于高斯补偿的误差感知模块和一个用于Gaussian修复的调制融合模块。我们的方法实现了分层表示的联合优化，允许仅使用两个视图参考图像进行新颖的视图合成。对各种数据集的综合实验表明，与之前的单尺度方法相比，HiSplat显著提高了重建质量和跨数据集泛化能力。对不同尺度三维高斯分布的相应消融研究和分析揭示了有效性背后的机制。项目网站：https://open3dvlab.github.io/HiSplat/ et.al.|[2410.06245](http://arxiv.org/abs/2410.06245)|null|
|**2024-10-08**|**Comparative Analysis of Novel View Synthesis and Photogrammetry for 3D Forest Stand Reconstruction and extraction of individual tree parameters**|准确高效的树木三维重建对于森林资源评估和管理至关重要。近景摄影测量（CRP）通常用于重建森林场景，但面临着效率低、质量差等挑战。最近，包括神经辐射场（NeRF）和3D高斯散斑（3DGS）在内的新型视图合成（NVS）技术已显示出在有限图像下进行3D植物重建的前景。然而，现有的研究主要集中在果园或单株树木中的小型植物上，这给它们在更大、更复杂的林分中的应用带来了不确定性。在这项研究中，我们收集了具有不同复杂性的森林地块的连续图像，并使用NeRF和3DGS进行了密集重建。将得到的点云与摄影测量和激光扫描的点云进行了比较。结果表明，NVS方法显著提高了重建效率。摄影测量难以处理复杂的林分，导致点云的树冠噪声过大，树木重建不正确，如树干重复。NeRF虽然对树冠区域更好，但在视野有限的地面区域可能会产生误差。3DGS方法生成更稀疏的点云，特别是在主干区域，影响胸径（DBH）精度。这三种方法都可以提取树高信息，其中NeRF的精度最高；然而，摄影测量在DBH精度方面仍然具有优势。这些发现表明，NVS方法在林分三维重建方面具有巨大潜力，为复杂的森林资源清查和可视化任务提供了宝贵支持。 et.al.|[2410.05772](http://arxiv.org/abs/2410.05772)|null|
|**2024-10-07**|**PH-Dropout: Prctical Epistemic Uncertainty Quantification for View Synthesis**|使用神经辐射场（NeRF）和高斯散斑（GS）的视图合成在渲染现实世界场景时表现出了令人印象深刻的保真度。然而，在视图综合中缺乏准确有效的认知不确定性量化（UQ）的实用方法。现有的NeRF方法要么引入了大量的计算开销（例如，“训练时间增加10倍”或“重复训练10倍”），要么仅限于特定的不确定性条件或模型。值得注意的是，GS模型缺乏全面认知UQ的系统方法。这种能力对于提高神经视图合成的鲁棒性和可扩展性至关重要，可以实现主动模型更新、误差估计和基于不确定性的可扩展集成建模。本文从函数近似的角度重新审视了基于NeRF和GS的方法，确定了3D表示学习中的关键差异和联系。基于这些见解，我们介绍了PH Dropout（事后Dropout），这是第一种直接在预训练的NeRF和GS模型上进行认知不确定性估计的实时准确方法。广泛的评估验证了我们的理论发现，并证明了PH Dropout的有效性。 et.al.|[2410.05468](http://arxiv.org/abs/2410.05468)|**[link](https://github.com/thanostriantafyllou3/ph-dropout)**|
|**2024-10-07**|**DreamSat: Towards a General 3D Model for Novel View Synthesis of Space Objects**|新颖的视图合成（NVS）能够生成场景的新图像或将一组2D图像转换为全面的3D模型。在空间领域意识的背景下，由于空间变得越来越拥挤，NVS可以准确地绘制空间物体和碎片的地图，提高空间操作的安全性和效率。同样，在会合和近距离作战任务中，3D模型可以提供目标物体的形状、大小和方向的详细信息，从而更好地规划和预测目标的行为。在这项工作中，我们探索了这些重建技术的泛化能力，旨在通过在190个高质量航天器模型的高质量数据集上微调最先进的单视图重建模型Zero123 XL，并将其集成到DreamGaussian框架中，提出一种从单视图图像重建3D航天器的新方法DreamSat，从而避免对每个新场景进行再训练的必要性。我们展示了在多个指标上重建质量的一致改进，包括对比语言图像预训练（CLIP）得分（+0.33%）、峰值信噪比（PSNR）（+2.53%）、结构相似性指数（SSIM）（+2.38%）和学习感知图像补丁相似性（LPIPS）（+0.16%）。%）在30张以前从未见过的航天器图像的测试集上。我们的方法通过利用最先进的扩散模型和3D高斯溅射技术，解决了航天工业中缺乏特定领域的3D重建工具的问题。这种方法保持了DreamGaussian框架的效率，同时提高了航天器重建的准确性和细节。这项工作的代码可以在GitHub上访问(https://github.com/ARCLab-MIT/space-nvs). et.al.|[2410.05097](http://arxiv.org/abs/2410.05097)|**[link](https://github.com/arclab-mit/space-nvs)**|
|**2024-10-10**|**6DGS: Enhanced Direction-Aware Gaussian Splatting for Volumetric Rendering**|随着神经辐射场（NeRF）和3D高斯散射（3DGS）的发展，新型视图合成技术取得了显著进步。然而，在不影响实时渲染的情况下实现高质量仍然具有挑战性，特别是对于具有视图相关效果的基于物理的光线跟踪。最近，N维高斯（N-DG）引入了6D空间角度表示，以更好地结合视图相关的效果，但高斯表示和控制方案都是次优的。在本文中，我们重新审视了6D高斯分布，并引入了6D高斯散斑（6DGS），它增强了颜色和不透明度表示，并利用6D空间中的额外方向信息来优化高斯控制。我们的方法与3DGS框架完全兼容，并通过更好地建模视图相关效果和精细细节，显著提高了实时辐射场渲染。实验证明，6DGS明显优于3DGS和N-DG，与3DGS相比，PSNR提高了15.73dB，高斯点减少了66.5%。项目页面为：https://gaozhongpai.github.io/6dgs/ et.al.|[2410.04974](http://arxiv.org/abs/2410.04974)|null|

<p align=right>(<a href=#updated-on-20241014>back to top</a>)</p>

## 3D Reconstruction

|Publish Date|Title|Abstract|PDF|Code|
|---|---|---|---|---|
|**2024-10-11**|**Ego3DT: Tracking Every 3D Object in Ego-centric Videos**|对具身智能日益增长的兴趣为当代研究带来了以自我为中心的视角。这个领域的一个重大挑战是在以自我为中心的视频中准确定位和跟踪物体，这主要是由于视角的巨大变化。针对这个问题，本文介绍了一种新的零样本方法，用于自中心视频中所有对象的三维重建和跟踪。我们提出了Ego3DT，这是一个新颖的框架，最初可以识别和提取自我环境中对象的检测和分割信息。利用来自相邻视频帧的信息，Ego3DT使用预训练的3D场景重建模型动态构建自我视图的3D场景。此外，我们还创新了一种动态层次关联机制，用于在以自我为中心的视频中创建稳定的物体3D跟踪轨迹。此外，我们的方法的有效性得到了两个新编译的数据集的广泛实验的证实，HOTA为1.04x-2.90x，展示了我们的方法在各种自我中心场景中的鲁棒性和准确性。 et.al.|[2410.08530](http://arxiv.org/abs/2410.08530)|null|
|**2024-10-10**|**FusionSense: Bridging Common Sense, Vision, and Touch for Robust Sparse-View Reconstruction**|人类毫不费力地将常识知识与视觉和触觉的感官输入相结合，以了解周围的环境。为了模拟这种能力，我们引入了FusionSense，这是一种新颖的3D重建框架，使机器人能够将基础模型的先验与视觉和触觉传感器的高度稀疏观测融合在一起。FusionSense解决了三个关键挑战：（i）机器人如何有效地获取周围场景和物体的鲁棒全局形状信息？（ii）机器人如何使用几何和常识先验来战略性地选择物体上的触摸点？（iii）触觉信号等局部观察如何改善物体的整体表现？我们的框架采用3D高斯散布作为核心表示，并结合了涉及全局结构构建、对象视觉外壳修剪和局部几何约束的分层优化策略。这一进步在传统上具有挑战性的透明、反射或黑暗物体的环境中实现了快速而稳健的感知，从而实现了更多的下游操纵或导航任务。对真实世界数据的实验表明，我们的框架优于以前最先进的稀疏视图方法。所有代码和数据都在项目网站上开源。 et.al.|[2410.08282](http://arxiv.org/abs/2410.08282)|null|
|**2024-10-10**|**Efficient Perspective-Correct 3D Gaussian Splatting Using Hybrid Transparency**|3D高斯散斑（3DGS）已被证明是一种通用的渲染图元，既可用于反向渲染，也可用于场景的实时探索。在这些应用中，相机帧和多个视图之间的连贯性至关重要，无论是场景重建的鲁棒收敛还是无伪影的飞行。最近的工作开始减轻破坏多视图一致性的伪影，包括由于不一致的透明度排序和（2D）斑点的透视校正轮廓而产生的爆裂伪影。与此同时，实时要求迫使这些实现在如何解决大型3D高斯组件的透明度方面做出妥协，从而以其他方式破坏了一致性。在我们的工作中，我们的目标是通过渲染完全透视正确的3D高斯分布，同时在每个像素级别使用精确混合的高质量近似值，混合透明度，以保持实时帧率，从而实现最大的连贯性。我们用于评估3D高斯分布的快速且透视准确的方法不需要矩阵求逆，从而确保了数值稳定性，消除了对退化斑点进行特殊处理的需要，混合透明度公式以渲染成本的一小部分保持了与完全分辨的每像素透明度相似的质量。我们进一步证明，这两个组件中的每一个都可以独立地集成到高斯溅射系统中。结合起来，与常见基准上的传统3DGS相比，它们实现了高达2美元/倍的帧率，2美元/秒的优化速度，以及相同或更好的图像质量，渲染伪影更少。 et.al.|[2410.08129](http://arxiv.org/abs/2410.08129)|null|
|**2024-10-10**|**UW-SDF: Exploiting Hybrid Geometric Priors for Neural SDF Reconstruction from Underwater Multi-view Monocular Images**|由于水下环境的独特性，水下物体的精确三维重建在水下勘探和测绘等任务中是一个具有挑战性的问题。依赖于多个传感器数据进行3D重建的传统方法非常耗时，并且在水下场景的数据采集中面临挑战。我们提出了UW-SDF，这是一种基于神经SDF的多视点水下图像重建目标对象的框架。我们引入混合几何先验来优化重建过程，显著提高了神经SDF重建的质量和效率。此外，为了解决多视图图像中分割一致性的挑战，我们提出了一种使用通用分割模型（SAM）的新的少镜头多视图目标分割策略，能够快速自动分割看不见的物体。通过对不同数据集进行广泛的定性和定量实验，我们证明我们提出的方法在水下3D重建领域优于传统的水下3D重构方法和其他神经渲染方法。 et.al.|[2410.08092](http://arxiv.org/abs/2410.08092)|null|
|**2024-10-10**|**Fine-detailed Neural Indoor Scene Reconstruction using multi-level importance sampling and multi-view consistency**|最近，室内场景中的神经隐式3D重建因其简单性和令人印象深刻的性能而变得流行。以前的工作可以利用正常或深度的单眼先验产生完整的结果。然而，由于无偏采样和不准确的单眼先验，它们可能会遭受过度平滑的重建和长期优化。在这篇论文中，我们提出了一种新的神经隐式表面重建方法，称为FD-NeuS，使用多级重要性采样策略和多视图一致性方法来学习精细详细的3D模型。具体来说，我们利用分割先验来指导基于区域的射线采样，并使用分段指数函数作为权重来引导沿射线的3D点采样，从而确保对重要区域的更多关注。此外，我们分别引入多视图特征一致性和多视图正态一致性作为监督和不确定性，进一步改善了细节的重建。大量的定量和定性结果表明，FD NeuS在各种场景中都优于现有方法。 et.al.|[2410.07597](http://arxiv.org/abs/2410.07597)|null|
|**2024-10-10**|**3D Vision-Language Gaussian Splatting**|3D重建方法和视觉语言模型的最新进展推动了多模态3D场景理解的发展，这在机器人、自动驾驶和虚拟/增强现实中具有重要应用。然而，当前的多模态场景理解方法天真地将语义表示嵌入到3D重建方法中，而没有在视觉和语言模态之间取得平衡，这导致半透明或反射对象的语义光栅化不令人满意，以及对颜色模态的过拟合。为了缓解这些局限性，我们提出了一种解决方案，充分处理不同的视觉和语义模态，即用于场景理解的3D视觉语言高斯飞溅模型，以强调语言模态的表示学习。我们提出了一种新的跨模态光栅化器，使用模态融合和平滑的语义指示符来增强语义光栅化。我们还采用相机视图混合技术来提高现有视图和合成视图之间的语义一致性，从而有效地减轻过拟合。大量实验表明，我们的方法在开放式词汇语义切分方面取得了最先进的性能，远远超过了现有的方法。 et.al.|[2410.07577](http://arxiv.org/abs/2410.07577)|null|
|**2024-10-09**|**3D2M Dataset: A 3-Dimension diverse Mesh Dataset**|三维（3D）重建已成为一个突出的研究领域，引起了学术界和工业界的广泛关注。在3D重建的各种应用中，面部重建带来了一些最艰巨的挑战。此外，每个人的面部结构都是独一无二的，需要算法足够稳健，以处理这种变化，同时保持对原始特征的保真度。本文介绍了一个全面的3D网格数据集，其中包含各种面部结构和相应的面部标志。该数据集包括188个3D面部网格，其中73个来自女性候选人，114个来自男性候选人。它涵盖了广泛的种族背景，有来自45个不同种族的贡献，确保了面部特征的丰富多样性。每个面部网格都有关键点，可以准确地注释相关特征，便于精确分析和操作。该数据集对于面部重新定位、面部结构成分研究和视频流中的实时人物表示等应用特别有价值。通过为研究人员和开发人员提供强大的资源，它旨在推进3D面部重建和相关技术领域的发展。 et.al.|[2410.07415](http://arxiv.org/abs/2410.07415)|**[link](https://github.com/sohomd/3D2M-Dataset)**|
|**2024-10-09**|**Z-upscaling: Optical Flow Guided Frame Interpolation for Isotropic Reconstruction of 3D EM Volumes**|我们提出了一种新的基于光流的方法来提高各向异性3D EM体积的轴向分辨率，以实现各向同性3D重建。假设在对齐良好的EM体积中3D生物结构的空间连续性，我们推断可以利用通常用于视频时间分辨率增强的光流估计技术。像素级运动是在沿z的相邻2D切片之间估计的，使用空间梯度流估计来插值和生成新的2D切片，从而得到各向同性体素。我们利用最新的最先进的学习方法进行视频帧插值和迁移学习技术，并在公开的超微结构EM体积上证明了我们的方法的成功。 et.al.|[2410.07043](http://arxiv.org/abs/2410.07043)|**[link](https://github.com/fisseha21/z-upscaling)**|
|**2024-10-09**|**ES-Gaussian: Gaussian Splatting Mapping via Error Space-Based Gaussian Completion**|准确且经济实惠的室内3D重建对于有效的机器人导航和交互至关重要。传统的基于激光雷达的测绘提供了高精度，但成本高、重量重、功耗大，新颖的视图渲染能力有限。基于视觉的测绘虽然经济高效，能够捕获视觉数据，但由于点云稀疏，往往难以进行高质量的3D重建。我们提出了ES Gaussian，这是一种端到端系统，使用低空相机和单线LiDAR进行高质量的3D室内重建。我们的系统具有视觉误差构造（VEC）功能，通过识别和校正二维误差图中几何细节不足的区域来增强稀疏点云。此外，我们介绍了一种由单线LiDAR引导的新型3DGS初始化方法，克服了传统多视图设置的局限性，并在资源受限的环境中实现了有效的重建。我们新的Dreame SR数据集和公开数据集的大量实验结果表明，ES Gaussian优于现有方法，特别是在具有挑战性的场景中。项目页面可在https://chenlu-china.github.io/ES-Gaussian/. et.al.|[2410.06613](http://arxiv.org/abs/2410.06613)|null|
|**2024-10-08**|**Comparative Analysis of Novel View Synthesis and Photogrammetry for 3D Forest Stand Reconstruction and extraction of individual tree parameters**|准确高效的树木三维重建对于森林资源评估和管理至关重要。近景摄影测量（CRP）通常用于重建森林场景，但面临着效率低、质量差等挑战。最近，包括神经辐射场（NeRF）和3D高斯散斑（3DGS）在内的新型视图合成（NVS）技术已显示出在有限图像下进行3D植物重建的前景。然而，现有的研究主要集中在果园或单株树木中的小型植物上，这给它们在更大、更复杂的林分中的应用带来了不确定性。在这项研究中，我们收集了具有不同复杂性的森林地块的连续图像，并使用NeRF和3DGS进行了密集重建。将得到的点云与摄影测量和激光扫描的点云进行了比较。结果表明，NVS方法显著提高了重建效率。摄影测量难以处理复杂的林分，导致点云的树冠噪声过大，树木重建不正确，如树干重复。NeRF虽然对树冠区域更好，但在视野有限的地面区域可能会产生误差。3DGS方法生成更稀疏的点云，特别是在主干区域，影响胸径（DBH）精度。这三种方法都可以提取树高信息，其中NeRF的精度最高；然而，摄影测量在DBH精度方面仍然具有优势。这些发现表明，NVS方法在林分三维重建方面具有巨大潜力，为复杂的森林资源清查和可视化任务提供了宝贵支持。 et.al.|[2410.05772](http://arxiv.org/abs/2410.05772)|null|

<p align=right>(<a href=#updated-on-20241014>back to top</a>)</p>

## Diffusion

|Publish Date|Title|Abstract|PDF|Code|
|---|---|---|---|---|
|**2024-10-11**|**SceneCraft: Layout-Guided 3D Scene Generation**|使用传统的3D建模工具，创建根据用户规范定制的复杂3D场景一直是一项乏味而具有挑战性的任务。尽管一些开创性的方法已经实现了自动文本到3D的生成，但它们通常仅限于对形状和纹理控制有限的小规模场景。我们介绍了SceneKraft，这是一种根据用户提供的文本描述和空间布局偏好生成详细室内场景的新方法。我们方法的核心是基于渲染的技术，它将3D语义布局转换为多视图2D代理地图。此外，我们设计了一个语义和深度条件的扩散模型来生成多视图图像，这些图像用于学习神经辐射场（NeRF）作为最终的场景表示。没有全景图像生成的限制，我们在支持单个房间之外的复杂室内空间生成方面超越了以前的方法，即使是像形状和布局不规则的整个多卧室公寓一样复杂。通过实验分析，我们证明我们的方法在复杂的室内场景生成方面明显优于现有的方法，具有不同的纹理、一致的几何形状和逼真的视觉质量。代码和更多结果可在以下网址获得：https://orangesodahub.github.io/SceneCraft et.al.|[2410.09049](http://arxiv.org/abs/2410.09049)|**[link](https://github.com/orangesodahub/scenecraft)**|
|**2024-10-11**|**Linear Convergence of Diffusion Models Under the Manifold Hypothesis**|分数匹配生成模型已被证明在从复杂的高维数据分布中采样方面是成功的。在许多应用中，这种分布被认为集中在嵌入 $d$维空间的更低$d$维数流形上；这被称为流形假说。目前最著名的收敛保证要么是$D$中的线性保证，要么是$D$中的多项式（超线性）保证。后者为后向SDE开发了一种新的集成方案。我们采取了两全其美的方法，证明扩散模型在Kullback-Leibler~（KL）散度中收敛所需的步数在内在维度$d$ 上是线性的（最多对数项）。此外，我们证明了这种线性依赖性是尖锐的。 et.al.|[2410.09046](http://arxiv.org/abs/2410.09046)|null|
|**2024-10-11**|**Semantic Score Distillation Sampling for Compositional Text-to-3D Generation**|从文本描述生成高质量的3D资产仍然是计算机图形学和视觉研究中的一个关键挑战。由于3D数据的稀缺性，最先进的方法利用预先训练的2D扩散先验，通过分数蒸馏采样（SDS）进行优化。尽管取得了进展，但制作具有多个对象或复杂交互的复杂3D场景仍然很困难。为了解决这个问题，最近的方法结合了方框或布局指导。然而，这些布局指导的组合方法往往难以提供细粒度的控制，因为它们通常很粗糙，缺乏表现力。为了克服这些挑战，我们引入了一种新的SDS方法，语义分数蒸馏采样（SemanticSDS），旨在有效提高合成文本到3D生成的表现力和准确性。我们的方法集成了新的语义嵌入，这些嵌入可以保持不同渲染视图之间的一致性，并清楚地区分各种对象和部分。这些嵌入被转化为语义图，指导特定区域的SDS过程，实现精确的优化和组合生成。通过利用明确的语义指导，我们的方法释放了现有预训练扩散模型的合成能力，从而在3D内容生成中实现了卓越的质量，特别是对于复杂的对象和场景。实验结果表明，我们的SemanticSDS框架对于生成最先进的复杂3D内容非常有效。代码：https://github.com/YangLing0818/SemanticSDS-3D et.al.|[2410.09009](http://arxiv.org/abs/2410.09009)|**[link](https://github.com/yangling0818/semanticsds-3d)**|
|**2024-10-11**|**Macrotransport of active particles in periodic channels and fields: rectification and dispersion**|活性颗粒在波纹通道和多孔介质等结构化环境中的运输和分散对于理解天然和工程活性系统非常重要。由于其持续的自推进，活性粒子在空间不对称约束下表现出整流输运。虽然在实验和基于粒子的模拟方面取得了进展，但对空间周期性几何中有效长时间输运动力学的理论理解仍然不够深入。本文应用广义泰勒色散理论（GTDT）分析了活动布朗粒子（ABPs）在周期性通道和场中的长期有效输运动力学。我们表明，长期输运行为受有效平流扩散方程的控制。推导出的宏观输运方程使我们能够表征平均漂移和有效色散系数。对于ABP在通道壁处受到无通量边界条件的情况，我们表明，无论活动如何，平均漂移都由沿通道的净扩散通量给出。对于ABP来说，它们的活动是维持密度梯度的驱动机制，最终导致沿通道的纠正运动。我们的连续体理论针对控制每个ABP运动的朗之万方程的直接布朗动力学模拟进行了验证。 et.al.|[2410.09007](http://arxiv.org/abs/2410.09007)|null|
|**2024-10-11**|**WaveDiffusion: Exploring Full Waveform Inversion via Joint Diffusion in the Latent Space**|全波形反演（FWI）是从地震波形数据重建高分辨率地下速度图的重要技术，由模拟波传播的偏微分方程（PDE）控制。传统的机器学习方法通常通过将地震波形编码为潜在嵌入并将其解码为速度图，将地震数据映射到速度图。本文介绍了一种新的框架，将FWI重构为共享潜在空间中的联合扩散过程，桥接地震波形数据和速度图。我们的方法有两个关键组成部分：首先，我们使用矢量量化将两个单独的自动编码器（一个用于地震数据，一个用于速度图）的瓶颈合并到一个统一的潜在空间中，以建立共享的码本。其次，我们在这个潜在空间中训练一个扩散模型，通过对潜在表示进行采样和去噪，然后用各自的解码器对每种模态进行解码，从而能够同时生成地震和速度图对。值得注意的是，我们联合生成的地震速度对在没有任何额外约束的情况下近似满足控制PDE，为FWI提供了新的几何解释。扩散过程学习根据其与PDE的偏差对潜在空间进行评分，得分越高，与真实解的偏差越小。通过遵循这一扩散过程，该模型追踪了从随机初始化到控制PDE的有效解的路径。我们在OpenFWI数据集上的实验表明，生成的地震和速度图对不仅表现出高保真度和多样性，而且遵守了控制PDE施加的物理约束。 et.al.|[2410.09002](http://arxiv.org/abs/2410.09002)|null|
|**2024-10-11**|**Revised Point-Spread Functions for the Atmospheric Imaging Assembly onboard the Solar Dynamics Observatory**|我们为太阳动力学天文台（SDO）上的大气成像组件（AIA）提出了修订后的点扩散函数（PSF）。这些PSF提供了对由保持入口和焦平面滤光片的网格衍射的光以及由镜子的微观粗糙度在中到长距离上漫散射的光的稳健估计。我们首先使用耀斑图像校准衍射光。我们对衍射光的建模提供了网格参数的可靠测定，并发现根据AIA通道，约24%至33%的收集光被衍射。然后，我们使用部分月球遮挡图像来拟合漫散射光。我们发现，漫射散射光可以被建模为两个幂律函数的叠加，这两个函数在探测器的整个长度上散射光。漫射散射光的量在10%到35%之间，具体取决于AIA通道。总的来说，AIA在中长距离上衍射和散射约40%至60%的收集光。当对此进行校正时，明亮的图像区域的强度增加了约30%，黑暗的图像区域强度降低了高达90%，太阳特征的相关差分发射测量分析也受到了相应的影响。最后，我们将使用我们新的PSF进行的图像重建与使用AIA团队PSF和Poduval等人（2013）的PSF的图像重建进行了比较。我们发现，我们的PSF优于其他PSF；我们的PSF很好地校正了耀斑衍射模式，并准确预测了月球掩星中的长距离散射光。 et.al.|[2410.08967](http://arxiv.org/abs/2410.08967)|null|
|**2024-10-11**|**DiffPO: A causal diffusion model for learning distributions of potential outcomes**|根据观察数据预测干预措施的潜在结果对于医学决策至关重要，但由于因果推理的基本问题，这项任务具有挑战性。现有方法主要局限于对潜在结果的点估计，没有不确定的量化；因此，关于潜在结果分布的完整信息通常被忽略。在这篇论文中，我们提出了一种新的因果扩散模型，称为DiffPO，该模型经过精心设计，通过学习潜在结果的分布，在医学中进行可靠的推理。在我们的DiffPO中，我们利用量身定制的条件去噪扩散模型来学习复杂的分布，通过一种新的正交扩散损失来解决选择偏差问题。我们的DiffPO方法的另一个优点是它非常灵活（例如，它也可以用于估计不同的因果量，如CATE）。在广泛的实验中，我们表明我们的方法达到了最先进的性能。 et.al.|[2410.08924](http://arxiv.org/abs/2410.08924)|null|
|**2024-10-11**|**An End-to-End Deep Learning Method for Solving Nonlocal Allen-Cahn and Cahn-Hilliard Phase-Field Models**|我们提出了一种高效的端到端深度学习方法，用于求解非局部Allen-Cahn（AC）和Cahn-Hilliard（CH）相场模型。这一努力的一个动机源于这样一个事实，即基于离散化偏微分方程的交流或CH相场模型会导致相之间的扩散界面，唯一的补救措施是严格细化真正移动尖锐界面附近的空间网格，该界面的宽度由一个与网格无关的参数决定，该参数远大于局部网格尺寸。在这项工作中，我们引入了具有规则、对数或障碍双阱势的非质量守恒非局域交流或CH相场模型。由于非局部性，其中一些模型具有完全尖锐的界面来分隔相位。这种模型的离散化可以导致宽度仅为单个网格单元宽度的相位之间的过渡。另一个动机是使用深度学习方法来改善求解离散化非局部相场模型的高成本。为此，使用AC或CH模型的完全离散近似的残差来定义定制神经网络的损失函数，该残差是应用傅里叶配点法和时间半隐式近似得到的。为了解决模型中的远程交互问题，我们通过将非局部内核作为神经网络模型的输入通道来定制神经网络的架构。然后，我们提供了大量计算实验的结果，以说明所提出方法的准确性、结构保持特性、预测能力和成本降低。 et.al.|[2410.08914](http://arxiv.org/abs/2410.08914)|null|
|**2024-10-11**|**Conditional Generative Models for Contrast-Enhanced Synthesis of T1w and T1 Maps in Brain MRI**|钆基造影剂（GBCA）的对比增强是神经放射学中肿瘤诊断的重要工具。基于钆给药前后胶质母细胞瘤的脑MRI扫描，我们提出了神经网络增强预测的两个新贡献。首先，我们研究了生成模型的潜力，更精确地说是条件扩散和流匹配，用于虚拟增强中的不确定性量化。其次，我们检查了定量MRI与T1加权扫描的T1扫描性能。与T1加权扫描相比，这些扫描的优点是具有物理意义，从而具有可比的体素范围。为了比较这两种模式在灰度不兼容的情况下的网络预测性能，我们建议使用Dice和Jaccard评分来评估对比增强感兴趣区域的分割。在所有模型中，我们观察到T1扫描比T1加权扫描具有更好的分割效果。 et.al.|[2410.08894](http://arxiv.org/abs/2410.08894)|null|
|**2024-10-11**|**Simulating anisotropic diffusion processes with smoothed particle hydrodynamics**|具有各向异性特征的扩散问题出现在科学和工程领域的各个领域。作为一种拉格朗日无网格方法，SPH在解决扩散问题方面具有特殊优势，因为它有利于处理平流项。但它在求解各向异性扩散中的应用仍然有限，因为需要一个稳健和通用的SPH公式来获得二阶导数的精确近似值。本文中，我们基于SPH公式修改了一个二阶导数模型，以获得由拉普拉斯算子元素组成的Hessian矩阵的完整版本。为了验证所提出的SPH方案，首先，通过使用各向异性分辨率耦合各向异性核，在薄结构内执行遵循预函数分布的标量的扩散。在各种各向异性比下，与理论解达到了很好的一致性。然后，模拟了污染物在流体中的各向异性扩散。仿真结果与相应的解析解非常一致，表明该算法可以获得光滑的解，而不会出现具有不连续性的污染物传输问题的寄生振荡，并达到二阶精度。随后，我们利用这种新开发的SPH公式来解决通过薄多孔膜的流体扩散和左心室内跨膜电位的各向异性传输问题，展示了所提出的SPH框架在解决复杂各向异性问题方面的能力。 et.al.|[2410.08888](http://arxiv.org/abs/2410.08888)|null|

<p align=right>(<a href=#updated-on-20241014>back to top</a>)</p>

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

<p align=right>(<a href=#updated-on-20241014>back to top</a>)</p>

[contributors-shield]: https://img.shields.io/github/contributors/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[contributors-url]: https://github.com/Vincentqyw/cv-arxiv-daily/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[forks-url]: https://github.com/Vincentqyw/cv-arxiv-daily/network/members
[stars-shield]: https://img.shields.io/github/stars/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[stars-url]: https://github.com/Vincentqyw/cv-arxiv-daily/stargazers
[issues-shield]: https://img.shields.io/github/issues/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[issues-url]: https://github.com/Vincentqyw/cv-arxiv-daily/issues

