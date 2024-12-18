[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]

## Updated on 2024.12.18
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
|**2024-12-16**|**PanSplat: 4K Panorama Synthesis with Feed-Forward Gaussian Splatting**|随着便携式360度摄像机的出现，全景在虚拟现实（VR）、虚拟旅游、机器人和自动驾驶等应用中受到了广泛关注。因此，宽基线全景视图合成已成为一项至关重要的任务，其中高分辨率、快速推理和内存效率至关重要。然而，由于要求苛刻的内存和计算要求，现有方法通常被限制在较低的分辨率（512美元×1024美元）。在本文中，我们介绍了PanSplat，这是一种可推广的前馈方法，可有效支持高达4K（2048美元×4096美元）的分辨率。我们的方法具有一个定制的球形3D高斯金字塔，具有斐波那契晶格排列，在减少信息冗余的同时提高了图像质量。为了满足高分辨率的需求，我们提出了一种管道，该管道将分层球形成本体积和高斯头与本地操作集成在一起，实现了两步延迟反向传播，以便在单个A100 GPU上进行内存高效训练。实验证明，PanSplat在合成和真实世界的数据集上都能以卓越的效率和图像质量获得最先进的结果。代码将在\url上提供{https://github.com/chengzhag/PanSplat}. et.al.|[2412.12096](http://arxiv.org/abs/2412.12096)|null|
|**2024-12-16**|**SweepEvGS: Event-Based 3D Gaussian Splatting for Macro and Micro Radiance Field Rendering from a Single Sweep**|3D高斯散斑（3D-GS）的最新进展已经证明了使用3D高斯基元从连续校准的输入视图进行高速、高保真和经济高效的新型视图合成的潜力。然而，传统方法需要高帧率、高密度和高质量的清晰图像，这不仅耗时，而且捕获效率低，尤其是在动态环境中。事件相机具有高时间分辨率和捕捉异步亮度变化的能力，为没有运动模糊的更可靠的场景重建提供了一种有前景的替代方案。在这篇论文中，我们提出了SweepEvGS，这是一种新的硬件集成方法，利用事件相机在单次扫描的各种成像设置中进行鲁棒和精确的新视图合成。SweepEvGS利用初始静态帧和在单个相机扫描期间捕获的密集事件流，有效地重建详细的场景视图。我们还介绍了不同的现实世界硬件成像系统，用于未来研究的现实世界数据收集和评估。我们通过在三种不同成像设置中的实验验证了SweepEvGS的鲁棒性和效率：合成对象、现实世界宏观级和现实世界微观级视图合成。我们的结果表明，SweepEvGS在视觉渲染质量、渲染速度和计算效率方面超越了现有的方法，突显了其在动态实际应用中的潜力。 et.al.|[2412.11579](http://arxiv.org/abs/2412.11579)|null|
|**2024-12-16**|**SpatialMe: Stereo Video Conversion Using Depth-Warping and Blend-Inpainting**|立体视频转换旨在将单眼视频转换为沉浸式立体格式。尽管在新颖的视图合成方面取得了进展，但它仍然存在两个主要挑战：i）难以实现高保真度和稳定的结果，ii）高质量立体视频数据不足。本文介绍了一种基于深度扭曲和混合修复的新型立体视频转换框架SpatialMe。具体而言，我们提出了一种基于掩模的层次特征更新（MHFU）细化器，该细化器使用特征更新单元（FUU）和掩模机制对设计的多分支修复模块的输出进行集成和细化。我们还提出了一种差异扩展策略来解决前景出血的问题。此外，我们还进行了一个高质量的真实世界立体视频数据集StereoV1K，以缓解数据短缺的问题。它包含1000个在真实世界中以1180 x 1180的分辨率拍摄的立体视频，涵盖了各种室内和室外场景。大量实验证明，我们的方法在生成立体视频方面比最先进的方法更优越。 et.al.|[2412.11512](http://arxiv.org/abs/2412.11512)|null|
|**2024-12-16**|**MOVIS: Enhancing Multi-Object Novel View Synthesis for Indoor Scenes**|重新利用预先训练的扩散模型已被证明对NVS有效。然而，这些方法大多局限于单个对象；直接将这些方法应用于组合多对象场景会产生较差的结果，特别是在新视图下对象放置不正确以及形状和外观不一致。如何增强和系统地评估此类模型的跨视图一致性仍有待探索。为了解决这个问题，我们提出MOVIS来增强多对象NVS的视图条件扩散模型在模型输入、辅助任务和训练策略方面的结构意识。首先，我们在去噪U-Net中注入结构感知特征，包括深度和对象掩码，以增强模型对对象实例及其空间关系的理解。其次，我们引入了一个辅助任务，要求模型同时预测新的视图对象掩码，进一步提高了模型区分和放置对象的能力。最后，我们对扩散采样过程进行了深入分析，并在训练过程中精心设计了一个结构引导的时间步采样调度器，该调度器平衡了全局对象放置的学习和细粒度细节恢复。为了系统地评估合成图像的合理性，我们建议在现有的图像级NVS度量的基础上评估交叉视图一致性和新的视图对象放置。在具有挑战性的合成和现实数据集上进行的广泛实验表明，我们的方法具有很强的泛化能力，并产生一致的新颖视图合成，突出了其指导未来3D感知多对象NVS任务的潜力。 et.al.|[2412.11457](http://arxiv.org/abs/2412.11457)|null|
|**2024-12-13**|**Probabilistic Inverse Cameras: Image to 3D via Multiview Geometry**|我们引入了一种从2D图像到多视图3D的分层概率方法：扩散“先验”对看不见的3D几何进行建模，然后调节扩散“解码器”以生成受试者的新视图。我们使用多视图图像格式的基于点图的几何表示来协调同时生成多个目标视图。我们通过假设固定的目标相机相对于源相机的姿态，并为每个目标构建可预测的几何特征分布，来促进视图之间的对应关系。我们的模块化、几何驱动的新颖视图合成方法（称为“unPIC”）在ObjaverseXL的伸出对象以及从谷歌扫描对象、亚马逊伯克利对象到数字孪生目录的现实世界对象上击败了CAT3D和One-2-3-45等SoTA基线。 et.al.|[2412.10273](http://arxiv.org/abs/2412.10273)|null|
|**2024-12-13**|**SuperGSeg: Open-Vocabulary 3D Segmentation with Structured Super-Gaussians**|3D高斯散点最近因其高效的训练和实时渲染而受到关注。虽然香草高斯散点表示主要是为视图合成而设计的，但最近的工作研究了如何通过场景理解和语言特征来扩展它。然而，现有的方法缺乏对场景的详细理解，限制了它们分割和解释复杂结构的能力。为此，我们引入了SuperGSeg，这是一种通过解纠缠分割和语言场蒸馏来促进连贯、上下文感知场景表示的新方法。SuperGSeg首先使用神经高斯模型，借助现成的2D掩模从多视图图像中学习实例和分层分割特征。然后利用这些特征创建一组稀疏的我们称之为超高斯分布。超高斯分布有助于将2D语言特征提取到3D空间中。通过超高斯分布，我们的方法可以在不大幅增加GPU内存的情况下实现高维语言特征渲染。大量实验表明，SuperGSeg在开放词汇对象定位和语义分割任务上都优于先前的工作。 et.al.|[2412.10231](http://arxiv.org/abs/2412.10231)|null|
|**2024-12-13**|**GAF: Gaussian Avatar Reconstruction from Monocular Videos via Multi-view Diffusion**|我们提出了一种新的方法，用于从智能手机等商品设备捕获的单眼视频中重建可动画化的3D高斯化身。由于观察有限，从这些记录中重建逼真的3D头部化身具有挑战性，这会使未观察到的区域受到限制，并可能导致新视图中的伪影。为了解决这个问题，我们引入了一种多视图头部扩散模型，利用其先验来填充缺失区域，并确保高斯飞溅渲染中的视图一致性。为了实现精确的视点控制，我们使用基于FLAME的头部重建渲染的法线贴图，该贴图提供像素对齐的感应偏置。我们还将从输入图像中提取的VAE特征作为扩散模型的条件，以保留面部身份和外观的细节。对于高斯化身重建，我们通过使用迭代去噪图像作为伪地面真相来提取多视图扩散先验，有效地缓解了过饱和问题。为了进一步提高照片真实感，我们在将其解码为图像之前，应用潜在上采样来细化去噪的潜在。我们在NeRSemble数据集上评估了我们的方法，结果表明，GAF在新视图合成方面比以前最先进的方法高出5.34%的SSIM得分。此外，我们展示了从商品设备上捕获的单眼视频中重建高保真度的化身。 et.al.|[2412.10209](http://arxiv.org/abs/2412.10209)|null|
|**2024-12-13**|**TSGaussian: Semantic and Depth-Guided Target-Specific Gaussian Splatting from Sparse Views**|高斯散斑技术的最新进展极大地推动了该领域的发展，实现了3D场景的全景和交互式分割。然而，现有的方法往往忽视了从稀疏视图重建具有复杂结构的指定目标的迫切需要。为了解决这个问题，我们引入了TSGaussian，这是一种新的框架，它将语义约束与深度先验相结合，以避免在具有挑战性的新视图合成任务中出现几何退化。我们的方法优先考虑指定目标上的计算资源，同时最小化背景分配。YOLOv9的边界框可作为Segment Anything模型生成2D掩码预测的提示，确保语义准确性和成本效益。TSGaussian通过为每个高斯椭球体引入紧凑的单位编码并结合3D空间一致性正则化，有效地对3D高斯进行聚类。利用这些模块，我们提出了一种修剪策略，以有效减少3D高斯分布中的冗余。大量实验表明，TSGaussian在三个标准数据集和我们收集的一个新的具有挑战性的数据集上优于最先进的方法，在特定对象的新颖视图合成中取得了优异的结果。代码可在以下网址获得：https://github.com/leon2000-ai/TSGaussian. et.al.|[2412.10051](http://arxiv.org/abs/2412.10051)|null|
|**2024-12-13**|**SplineGS: Robust Motion-Adaptive Spline for Real-Time Dynamic 3D Gaussians from Monocular Video**|由于场景动态和缺乏多视图线索，从野生单眼视频中合成新颖的视图具有挑战性。为了解决这个问题，我们提出了SplineGS，这是一个无COLMAP的动态3D高斯散斑（3DGS）框架，用于从单眼视频中进行高质量重建和快速渲染。其核心是一种新的运动自适应样条（MAS）方法，该方法使用具有少量控制点的三次Hermite样条来表示连续的动态3D高斯轨迹。对于MAS，我们引入了一种运动自适应控制点修剪（MACP）方法来模拟每个动态3D高斯在不同运动中的变形，在保持动态建模完整性的同时逐步修剪控制点。此外，我们提出了一种联合优化策略，用于相机参数估计和3D高斯属性，利用光度和几何一致性。这消除了对“运动中的结构”预处理的需要，并增强了SplineGS在现实世界条件下的鲁棒性。实验表明，SplineGS在单目视频动态场景的新颖视图合成质量方面明显优于最先进的方法，实现了数千倍的渲染速度。 et.al.|[2412.09982](http://arxiv.org/abs/2412.09982)|null|
|**2024-12-12**|**PBR-NeRF: Inverse Rendering with Physics-Based Neural Fields**|我们使用基于物理的渲染（PBR）理论的神经辐射场（NeRF）方法来解决3D重建中的不适定逆渲染问题，称为PBR-NeRF。我们的方法解决了大多数NeRF和3D高斯散斑方法的一个关键局限性：它们在不建模场景材质和照明的情况下估计与视图相关的外观。为了解决这一局限性，我们提出了一种能够联合估计场景几何形状、材质和照明的逆渲染（IR）模型。我们的模型建立在最近基于NeRF的IR方法的基础上，但关键是引入了两种新的基于物理的先验，更好地约束了IR估计。我们的先验被严格地表述为直观的损失项，在不影响新颖视图合成质量的情况下实现了最先进的材料估计。我们的方法很容易适应其他需要材料估计的逆渲染和3D重建框架。我们展示了将当前的神经渲染方法扩展到完全建模场景属性的重要性，而不仅仅是几何和视图相关的外观。代码可在以下网址公开获取https://github.com/s3anwu/pbrnerf et.al.|[2412.09680](http://arxiv.org/abs/2412.09680)|**[link](https://github.com/s3anwu/pbrnerf)**|

<p align=right>(<a href=#updated-on-20241218>back to top</a>)</p>

## 3D Reconstruction

|Publish Date|Title|Abstract|PDF|Code|
|---|---|---|---|---|
|**2024-12-16**|**Wonderland: Navigating 3D Scenes from a Single Image**|本文探讨了一个具有挑战性的问题：我们如何从单个任意图像中高效地创建高质量、宽范围的3D场景？现有的方法面临几个限制，例如需要多视图数据、耗时的每个场景优化、背景中的低视觉质量以及看不见区域中的失真重建。我们提出了一种新的管道来克服这些局限性。具体来说，我们引入了一种大规模重建模型，该模型使用视频扩散模型的延迟以前馈方式预测场景的3D高斯散点。视频扩散模型旨在创建精确遵循指定摄像机轨迹的视频，使其能够生成包含多视图信息的压缩视频延迟，同时保持3D一致性。我们采用渐进式训练策略训练3D重建模型对视频潜在空间进行操作，从而高效生成高质量、宽范围和通用的3D场景。对各种数据集的广泛评估表明，我们的模型在单视图3D场景生成方面明显优于现有方法，特别是在域外图像的情况下。我们首次证明，可以在扩散模型的潜在空间上有效地构建3D重建模型，以实现高效的3D场景生成。 et.al.|[2412.12091](http://arxiv.org/abs/2412.12091)|null|
|**2024-12-16**|**IDArb: Intrinsic Decomposition for Arbitrary Number of Input Views and Illuminations**|从图像中捕获几何和材料信息仍然是计算机视觉和图形学中的一个基本挑战。传统的基于优化的方法通常需要数小时的计算时间来从密集的多视图输入中重建几何体、材质属性和环境照明，同时仍在努力解决照明和材质之间固有的模糊问题。另一方面，基于学习的方法利用了现有3D对象数据集中的丰富素材先验，但在保持多视图一致性方面面临挑战。本文介绍了IDArb，这是一种基于扩散的模型，旨在在不同光照条件下对任意数量的图像进行内在分解。我们的方法实现了对表面法线和材料属性的准确和多视图一致估计。这是通过一种新颖的跨视图、跨域注意力模块和一种增强照明的视图自适应训练策略实现的。此外，我们引入了ARB Objaverse，这是一种新的数据集，可在不同的光照条件下提供大规模的多视图内在数据和渲染，支持稳健的训练。大量实验表明，IDArb在定性和定量方面都优于最先进的方法。此外，我们的方法有助于一系列下游任务，包括单图像重新照明、光度立体和3D重建，突出了其在逼真3D内容创建中的广泛应用。 et.al.|[2412.12083](http://arxiv.org/abs/2412.12083)|null|
|**2024-12-16**|**EGP3D: Edge-guided Geometric Preserving 3D Point Cloud Super-resolution for RGB-D camera**|当前RGB-D相机捕获的点云或深度图像通常分辨率低，不足以用于3D重建和机器人等应用。现有的点云超分辨率（PCSR）方法要么受到几何伪影的约束，要么缺乏对边缘细节的关注。为了解决这些问题，我们提出了一种为RGB-D相机量身定制的边缘引导几何保持3D点云超分辨率（EGP3D）方法。我们的方法创新性地优化了投影2D空间上具有边缘约束的点云，从而确保了3D PCSR任务中的高质量边缘保留。为了解决超分辨率点云中的几何优化挑战，特别是保持边缘形状和平滑度，我们引入了一个多面损失函数，该函数同时优化了切角距离、豪斯多夫距离和梯度平滑度。用于点云上采样的现有数据集主要是合成的，不能充分代表现实世界的场景，忽略了噪声和杂散光的影响。为了解决PCSR任务缺乏真实RGB-D数据的问题，我们构建了一个数据集来捕捉真实世界的噪声和杂散光效果，从而更准确地表示真实的环境。通过模拟和真实世界的实验验证，所提出的方法在保持边缘清晰度和几何细节方面表现出了卓越的性能。 et.al.|[2412.11680](http://arxiv.org/abs/2412.11680)|null|
|**2024-12-16**|**3D $^2$-Actor: Learning Pose-Conditioned 3D-Aware Denoiser for Realistic Gaussian Avatar Modeling**|神经隐式表示和可微分渲染的进步显著提高了从稀疏多视图RGB视频中学习可动画3D化身的能力。然而，目前将观测空间映射到规范空间的方法在捕捉与姿势相关的细节和推广到新姿势方面经常面临挑战。虽然扩散模型在2D图像生成中表现出了显著的零样本能力，但它们从2D输入创建可动画化3D化身的潜力仍有待开发。在这项工作中，我们介绍了3D$^2$-Actor，这是一种新颖的方法，具有姿势条件的3D感知人体建模管道，集成了迭代的2D去噪和3D校正步骤。2D去噪器在姿势提示的指导下生成详细的多视图图像，为高保真3D重建和姿势渲染提供所需的丰富特征集。作为补充，我们基于高斯的3D整流器通过两阶段投影策略和新颖的局部坐标表示来渲染具有增强3D一致性的图像。此外，我们提出了一种创新的采样策略，以确保视频合成中帧之间的平滑时间连续性。我们的方法有效地解决了传统数值解在处理病态映射、生成逼真和可动画化的3D人类化身方面的局限性。实验结果表明，3D$^2$ -Actor在高保真化身建模方面表现出色，并能稳健地推广到新的姿势。代码可在以下网址获得：https://github.com/silence-tang/GaussianActor. et.al.|[2412.11599](http://arxiv.org/abs/2412.11599)|**[link](https://github.com/silence-tang/gaussianactor)**|
|**2024-12-16**|**View Transformation Robustness for Multi-View 3D Object Reconstruction with Reconstruction Error-Guided View Selection**|视图变换鲁棒性（VTR）对于基于深度学习的多视图3D对象重建模型至关重要，它表明了方法在各种视图变换输入下的稳定性。然而，现有的研究很少关注多视图3D对象重建中的视图变换鲁棒性。提高模型VTR的一种直接方法是生成具有更多视图转换的数据，并将其添加到模型训练中。大型视觉模型，特别是稳定扩散模型的最新进展，为生成3D模型或仅用单个图像输入合成新的视图图像提供了巨大的潜力。在推理时直接部署这些模型会消耗大量的计算资源，并且也不能保证它们对视图转换的鲁棒性。为了在不增加额外推理计算负担的情况下充分利用稳定扩散模型的能力，我们建议使用稳定扩散模型生成新的视图，以提高视图转换的鲁棒性。我们提出了一种重建误差引导的视图选择方法，而不是合成随机视图，该方法考虑了3D预测的重建误差的空间分布，并选择了尽可能覆盖重建误差的视图。这些方法在具有大视图变换的集合上进行训练和测试，以验证3D重建模型对视图变换的鲁棒性。大量实验表明，所提出的方法可以优于最先进的3D重建方法和其他视图变换鲁棒性比较方法。 et.al.|[2412.11428](http://arxiv.org/abs/2412.11428)|null|
|**2024-12-15**|**VividFace: A Diffusion-Based Hybrid Framework for High-Fidelity Video Face Swapping**|视频人脸交换在各种应用中越来越受欢迎，但现有的方法主要侧重于静态图像，由于时间一致性和复杂的场景，在视频人脸交换方面存在困难。在本文中，我们提出了第一个专门为视频人脸交换设计的基于扩散的框架。我们的方法引入了一种新颖的图像-视频混合训练框架，该框架利用了丰富的静态图像数据和时间视频序列，解决了纯视频训练的固有局限性。该框架结合了一个专门设计的扩散模型和一个VidFaceVAE，该模型有效地处理了这两种类型的数据，以更好地保持生成视频的时间一致性。为了进一步分离身份和姿势特征，我们构建了属性身份分离三元组（AIDT）数据集，其中每个三元组有三张人脸图像，两张图像共享相同的姿势，两张共享相同的身份。通过全面的遮挡增强，该数据集还提高了对遮挡的鲁棒性。此外，我们将3D重建技术作为输入调节集成到我们的网络中，以处理大的姿态变化。大量实验表明，与现有方法相比，我们的框架在身份保持、时间一致性和视觉质量方面取得了卓越的性能，同时需要更少的推理步骤。我们的方法有效地缓解了视频人脸交换中的关键挑战，包括时间闪烁、身份保持以及对遮挡和姿态变化的鲁棒性。 et.al.|[2412.11279](http://arxiv.org/abs/2412.11279)|null|
|**2024-12-15**|**Volumetric Mapping with Panoptic Refinement via Kernel Density Estimation for Mobile Robots**|在许多机器人应用中，利用语义理解重建三维（3D）场景至关重要。机器人需要识别哪些物体，以及它们的位置和形状，以便在给定的任务中精确地操纵它们。特别是移动机器人，通常使用轻量级网络对RGB图像上的对象进行分割，然后通过深度图对其进行定位；然而，他们经常遇到分布外的情况，即蒙版覆盖了对象。本文通过使用非参数统计方法细化分割误差，解决了3D场景重建中的全景分割质量问题。为了提高掩模精度，我们将预测的掩模映射到深度帧中，通过核密度来估计它们的分布。然后，在不需要额外参数的情况下，以自适应的方式拒绝深度感知中的异常值，以适应分布外的场景，然后使用投影符号距离函数（SDF）进行3D重建。我们在合成数据集上验证了我们的方法，该数据集显示了全景成像定量和定性结果的改进。通过实际测试，结果进一步表明我们的方法可以部署在真实的机器人系统上。我们的源代码可在以下网址获得：https://github.com/mkhangg/refined全景成像。 et.al.|[2412.11241](http://arxiv.org/abs/2412.11241)|**[link](https://github.com/mkhangg/refined_panoptic_mapping)**|
|**2024-12-15**|**Multi-Graph Co-Training for Capturing User Intent in Session-based Recommendation**|基于会话的推荐侧重于根据匿名用户会话的序列预测用户将与之交互的下一个项目。该领域的一个重大挑战是由于典型的短期交互导致的数据稀疏性。大多数现有方法严重依赖用户当前的交互，忽略了可用的大量辅助信息。为了解决这个问题，我们提出了一种新的模型，即多图协同训练模型（MGCOT），它不仅利用了当前的会话图，还利用了类似的会话图和全局项目关系图。这种方法允许更全面地探索内在关系，并更好地从多个视图中捕捉用户意图，使会话表示能够相互补充。此外，MGCOT采用多头注意力机制来有效地捕捉相关的会话意图，并使用对比学习来形成准确和稳健的会话表示。在三个数据集上进行的广泛实验表明，MGCOT显著提高了基于会话的推荐的性能，特别是在Diginetica数据集上，在P@20和P@20上分别提高了2.00%和10.70%MRR@20.资源已在我们的GitHub存储库中公开可用https://github.com/liang-tian-tian/MGCOT. et.al.|[2412.11105](http://arxiv.org/abs/2412.11105)|**[link](https://github.com/liang-tian-tian/mgcot)**|
|**2024-12-15**|**Facial Surgery Preview Based on the Orthognathic Treatment Prediction**|正颌手术咨询对于帮助患者了解手术后面部外观的变化至关重要。然而，由于治疗前后数据有限以及治疗的复杂性，目前的可视化方法往往效率低下且不准确。为了克服这些挑战，本研究旨在开发一种全自动管道，为正颌治疗患者生成准确有效的术后面部外观3D预览，而不需要额外的医学图像。该研究引入了新的美学损失，如口腔凸起和不对称损失，以提高面部手术预测的准确性。此外，它还提出了一个专门的参数模型，用于患者的3D重建、指导潜在代码预测网络优化的医疗相关损失，以及解决数据不足问题的数据增强方案。该研究还采用了参数模型FLAME，通过提取面部潜在代码并在手术前后几何形状之间建立密集的对应关系来提高面部外观预览的质量。定量比较表明了该算法的有效性，定性结果突出了准确的面部轮廓和细节预测。一项用户研究证实，医生和公众无法区分机器学习预测和实际的术后结果。本研究旨在为正颌外科咨询提供一种实用、有效的解决方案，使医生和患者受益。 et.al.|[2412.11045](http://arxiv.org/abs/2412.11045)|null|
|**2024-12-15**|**AURORA: Automated Unleash of 3D Room Outlines for VR Applications**|创建逼真的VR体验具有挑战性，因为将现实世界的细节准确复制到虚拟场景中是一个劳动密集型的过程，这突显了对保持空间精度和提供设计灵活性的自动化方法的需求。在这篇论文中，我们提出了AURORA，这是一种利用RGB-D图像自动生成纯虚拟现实（VR）场景和结合现实世界元素的VR场景的新方法。这种方法可以简化将现实世界细节转换为虚拟场景的过程，从而使设计师受益。AURORA集成了图像处理、分割和3D重建方面的先进技术，可从现实环境中高效地创建逼真和详细的室内设计。这种集成的设计确保了最佳的性能和精度，通过独特地结合和利用基础模型的优势，解决了自动化室内设计生成中的关键挑战。我们通过实验证明了我们的方法的有效性，包括在自我捕获的数据和公共数据集上，展示了它通过提供符合现实世界定位的室内设计来增强虚拟现实（VR）应用的潜力。 et.al.|[2412.11033](http://arxiv.org/abs/2412.11033)|null|

<p align=right>(<a href=#updated-on-20241218>back to top</a>)</p>

## Diffusion

|Publish Date|Title|Abstract|PDF|Code|
|---|---|---|---|---|
|**2024-12-16**|**Causal Diffusion Transformers for Generative Modeling**|我们引入因果扩散作为扩散模型的自回归（AR）对应物。它是一个下一代代币预测框架，对离散和连续模式都很友好，并与LLaMA和GPT等现有的下一代令牌预测模型兼容。虽然最近的工作试图将扩散与AR模型相结合，但我们表明，在扩散模型中引入顺序因子分解可以大大提高其性能，并使AR和扩散生成模式之间能够平滑过渡。因此，我们提出了CausalFusion——一种仅限解码器的转换器，它对连续令牌和扩散噪声水平的数据进行双因子分解，从而在ImageNet生成基准上获得最先进的结果，同时还享有生成任意数量令牌用于上下文推理的AR优势。我们通过联合图像生成和字幕模型进一步展示了CausalFusion的多模式能力，并展示了CaesalFusion对零样本上下文图像操作的能力。我们希望这项工作能够为社区提供一个在离散和连续数据上训练多模态模型的新视角。 et.al.|[2412.12095](http://arxiv.org/abs/2412.12095)|**[link](https://github.com/causalfusion/causalfusion)**|
|**2024-12-16**|**CAP4D: Creating Animatable 4D Portrait Avatars with Morphable Multi-View Diffusion Models**|从图像中重建照片级真实感和动态肖像化身对于许多应用至关重要，包括广告、视觉效果和虚拟现实。根据应用程序的不同，化身重建涉及不同的捕捉设置和约束条件。例如，视觉效果工作室使用相机阵列捕捉数百张参考图像，而内容创作者可能会试图为从互联网下载的单个肖像图像制作动画。因此，有一个庞大而异构的化身重建方法生态系统。基于多视图立体或神经渲染的技术可以获得最高质量的结果，但需要数百张参考图像。最近的生成模型从单个参考图像中生成了令人信服的化身，但视觉保真度仍然落后于多视图技术。在这里，我们提出了CAP4D：一种使用可变形多视图扩散模型从任意数量的参考图像（即1到100）重建照片级4D（动态3D）肖像化身的方法，并实时对其进行动画和渲染。我们的方法展示了单图像、少图像和多图像4D肖像化身重建的最先进性能，并采取措施弥合单图像和多视图重建技术之间的视觉保真度差距。 et.al.|[2412.12093](http://arxiv.org/abs/2412.12093)|null|
|**2024-12-16**|**Wonderland: Navigating 3D Scenes from a Single Image**|本文探讨了一个具有挑战性的问题：我们如何从单个任意图像中高效地创建高质量、宽范围的3D场景？现有的方法面临几个限制，例如需要多视图数据、耗时的每个场景优化、背景中的低视觉质量以及看不见区域中的失真重建。我们提出了一种新的管道来克服这些局限性。具体来说，我们引入了一种大规模重建模型，该模型使用视频扩散模型的延迟以前馈方式预测场景的3D高斯散点。视频扩散模型旨在创建精确遵循指定摄像机轨迹的视频，使其能够生成包含多视图信息的压缩视频延迟，同时保持3D一致性。我们采用渐进式训练策略训练3D重建模型对视频潜在空间进行操作，从而高效生成高质量、宽范围和通用的3D场景。对各种数据集的广泛评估表明，我们的模型在单视图3D场景生成方面明显优于现有方法，特别是在域外图像的情况下。我们首次证明，可以在扩散模型的潜在空间上有效地构建3D重建模型，以实现高效的3D场景生成。 et.al.|[2412.12091](http://arxiv.org/abs/2412.12091)|null|
|**2024-12-16**|**IDArb: Intrinsic Decomposition for Arbitrary Number of Input Views and Illuminations**|从图像中捕获几何和材料信息仍然是计算机视觉和图形学中的一个基本挑战。传统的基于优化的方法通常需要数小时的计算时间来从密集的多视图输入中重建几何体、材质属性和环境照明，同时仍在努力解决照明和材质之间固有的模糊问题。另一方面，基于学习的方法利用了现有3D对象数据集中的丰富素材先验，但在保持多视图一致性方面面临挑战。本文介绍了IDArb，这是一种基于扩散的模型，旨在在不同光照条件下对任意数量的图像进行内在分解。我们的方法实现了对表面法线和材料属性的准确和多视图一致估计。这是通过一种新颖的跨视图、跨域注意力模块和一种增强照明的视图自适应训练策略实现的。此外，我们引入了ARB Objaverse，这是一种新的数据集，可在不同的光照条件下提供大规模的多视图内在数据和渲染，支持稳健的训练。大量实验表明，IDArb在定性和定量方面都优于最先进的方法。此外，我们的方法有助于一系列下游任务，包括单图像重新照明、光度立体和3D重建，突出了其在逼真3D内容创建中的广泛应用。 et.al.|[2412.12083](http://arxiv.org/abs/2412.12083)|null|
|**2024-12-16**|**A LoRA is Worth a Thousand Pictures**|扩散模型和参数高效微调（PEFT）的最新进展使文本到图像的生成和定制变得广泛可用，低阶自适应（LoRA）能够使用最少的数据和计算来复制艺术家的风格或主题。在本文中，我们研究了LoRA权重与艺术风格之间的关系，证明LoRA权重本身可以作为风格的有效描述符，而不需要额外的图像生成或原始训练集的知识。我们的研究结果表明，与传统的预训练特征（如CLIP和DINO）相比，LoRA权重在艺术风格聚类方面表现更好，定性和定量观察到基于LoRA和传统基于图像的嵌入之间存在很强的结构相似性。我们为不断增长的定制模型集合确定了各种检索场景，并表明我们的方法能够在真实世界的环境中进行更准确的检索，在这些环境中，训练图像的知识不可用，需要额外的生成。最后，我们讨论了未来的潜在应用，如零样本LoRA微调和模型归因。 et.al.|[2412.12048](http://arxiv.org/abs/2412.12048)|null|
|**2024-12-16**|**FSFM: A Generalizable Face Security Foundation Model via Self-Supervised Facial Representation Learning**|这项工作问：面对大量未标记的真实人脸，如何学习一种鲁棒且可转移的面部表示，以提高各种人脸安全任务的泛化性能？我们首次尝试并提出了一种自监督预训练框架，用于学习真实人脸图像的基本表示，FSFM，该框架利用了掩模图像建模（MIM）和实例判别（ID）之间的协同作用。我们探索了MIM的各种面部掩蔽策略，并提出了一种简单而强大的CRFR-P掩蔽方法，该方法明确地迫使模型捕获有意义的区域内一致性和具有挑战性的区域间一致性。此外，我们设计了与MIM自然耦合的ID网络，通过量身定制的自蒸馏建立底层的局部到全局的对应关系。这三个学习目标，即3C，授权对真实人脸的局部特征和全局语义进行编码。经过预训练后，vanilla ViT可作为下游人脸安全任务的通用视觉基础模型：跨数据集深度伪造检测、跨域人脸反欺骗和看不见的扩散人脸伪造检测。在10个公共数据集上进行的广泛实验表明，我们的模型比监督预训练、视觉和面部自我监督学习艺术更好，甚至优于任务专用的SOTA方法。 et.al.|[2412.12032](http://arxiv.org/abs/2412.12032)|null|
|**2024-12-16**|**The entropic optimal (self-)transport problem: Limit distributions for decreasing regularization with application to score function estimation**|Westudy光滑概率测度的各向异性动物（自）输运问题的统计性质。我们提供了熵（自）势的极限分布的精确描述和正则化参数收缩的计划，这与正则化参数保持不变的先前工作形成了鲜明对比。此外，我们证明了经验熵最优自输运计划的重心投影的重新缩放收敛到分数函数，分数函数是扩散模型的中心对象，并表征了逐点和L2中的渐近波动。最后，我们描述了在两种不同的度量和适当选择的收缩正则化参数的情况下，所使用的方法在什么条件下能够推导出经验熵最优输运势的（逐点）极限分布结果。这项工作需要更好地了解Sinkhorn运营商的组成，这是独立利益的结果。 et.al.|[2412.12007](http://arxiv.org/abs/2412.12007)|null|
|**2024-12-16**|**Controllable Shadow Generation with Single-Step Diffusion Models from Synthetic Data**|真实的阴影生成是高质量图像合成和视觉效果的关键组成部分，但现有的方法存在某些局限性：基于物理的方法需要3D场景几何体，而这通常是不可用的，而基于学习的技术则难以控制和视觉伪影。我们介绍了一种快速、可控、无背景的2D物体图像阴影生成新方法。我们使用3D渲染引擎创建了一个大型合成数据集，用于训练可控阴影生成的扩散模型，为不同的光源参数生成阴影图。通过广泛的消融研究，我们发现整流流量目标只需一个采样步骤即可实现高质量的结果，从而实现实时应用。此外，我们的实验表明，该模型对真实世界的图像具有很好的泛化能力。为了促进对阴影生成质量和可控性评估的进一步研究，我们发布了一个新的公共基准，其中包含各种设置下的各种对象图像和阴影图。项目页面可在https://gojasper.github.io/controllable-shadow-generation-project/ et.al.|[2412.11972](http://arxiv.org/abs/2412.11972)|null|
|**2024-12-16**|**Multiplexing in Networks and Diffusion**|社会和经济网络往往是多重的，这意味着人们通过不同类型的关系联系在一起，比如借东西和提供建议。我们对多路复用的研究做出了三项贡献。首先，我们记录了印度村庄数据中的经验复用模式：社交、咨询、帮助和借贷等关系是相互关联但不同的，而基于种族和地理的网络常用代理几乎与实际关系不相关。其次，我们在现场实验中研究了这些层及其重叠如何影响信息扩散。建议网络是扩散的最佳预测因素，但结合各层可以进一步提高预测效果。层间重叠较大（多路复用较多）的村庄整体扩散较少。这导致了我们的第三个贡献：开发了一个关于多路网络中扩散的模型和理论结果。多路复用可以减缓简单传染病（如疾病或基本信息）的传播，但根据其病毒性，可以阻碍或增强复杂传染病（如新技术）的传播。最后，我们确定了性别和连通性在多路复用方面的差异。这些因素对信息获取和规范遵守等传播中介结果的不平等产生了影响。 et.al.|[2412.11957](http://arxiv.org/abs/2412.11957)|null|
|**2024-12-16**|**DRUM: Diffusion-based runoff model for probabilistic flood forecasting**|由于持续低估洪峰流量和当前方法中不确定性量化不足，可靠的洪水预报仍然是一个关键挑战。我们提出了DRUM（基于扩散的径流模型），这是一种用于概率径流预测的生成式人工智能解决方案。DRUM构建了一个迭代优化过程，在过去的气象条件、当前的气象预报和静态集水区属性的指导下，从噪声中生成集合径流估计值。该框架允许学习复杂的水文行为，而无需强加明确的分布假设，特别有利于极端事件预测和不确定性量化。利用美国本土531个代表性流域的数据，DRUM在径流预测方面在确定性和概率性技能方面都优于最先进的深度学习方法，在极端流量（0.1%）预测方面尤其具有优势。DRUM在所有级别和交付周期（1-7天）内都表现出卓越的洪水预警技能，在完美预测下，极端事件的F1得分接近0.4，并在运营预测中保持稳健的性能，特别是对于较长的交付周期和高级别洪水。当应用于21世纪的气候预测时，DRUM显示，在各种排放情景下，47.8-57.1%的流域的洪水脆弱性日益增加，西海岸和东南部地区的风险尤其高。这些进展表明，在气候变化的情况下，改进洪水预报和长期风险评估具有巨大的潜力。 et.al.|[2412.11942](http://arxiv.org/abs/2412.11942)|null|

<p align=right>(<a href=#updated-on-20241218>back to top</a>)</p>

## NeRF

|Publish Date|Title|Abstract|PDF|Code|
|---|---|---|---|---|
|**2024-12-13**|**Neural Vector Tomography for Reconstructing a Magnetization Vector Field**|矢量断层重建的离散化技术容易在重建中产生伪影。随着噪声量的增加，这些重建的质量可能会进一步恶化。在这项工作中，我们使用平滑神经场对底层向量场进行建模。由于神经网络中的激活函数可以被选择为平滑的，并且域不再像素化，因此即使在存在噪声的情况下，该模型也能得到高质量的重建。在我们具有潜在的全局连续对称性的情况下，我们发现神经网络比现有技术大大提高了重建的准确性。 et.al.|[2412.09927](http://arxiv.org/abs/2412.09927)|null|
|**2024-12-12**|**PBR-NeRF: Inverse Rendering with Physics-Based Neural Fields**|我们使用基于物理的渲染（PBR）理论的神经辐射场（NeRF）方法来解决3D重建中的不适定逆渲染问题，称为PBR-NeRF。我们的方法解决了大多数NeRF和3D高斯散斑方法的一个关键局限性：它们在不建模场景材质和照明的情况下估计与视图相关的外观。为了解决这一局限性，我们提出了一种能够联合估计场景几何形状、材质和照明的逆渲染（IR）模型。我们的模型建立在最近基于NeRF的IR方法的基础上，但关键是引入了两种新的基于物理的先验，更好地约束了IR估计。我们的先验被严格地表述为直观的损失项，在不影响新颖视图合成质量的情况下实现了最先进的材料估计。我们的方法很容易适应其他需要材料估计的逆渲染和3D重建框架。我们展示了将当前的神经渲染方法扩展到完全建模场景属性的重要性，而不仅仅是几何和视图相关的外观。代码可在以下网址公开获取https://github.com/s3anwu/pbrnerf et.al.|[2412.09680](http://arxiv.org/abs/2412.09680)|**[link](https://github.com/s3anwu/pbrnerf)**|
|**2024-12-12**|**Mixture of neural fields for heterogeneous reconstruction in cryo-EM**|低温电子显微镜（Cryo-EM）是一种用于蛋白质结构测定的实验技术，可以在接近生理环境的情况下对大分子的集合进行成像。虽然最近的进展能够重建单个生物分子复合物的动态构象，但目前的方法并不能充分模拟具有混合构象和成分异质性的样品。特别是，包含多种蛋白质混合物的数据集需要联合推断结构、姿势、组成类别和构象状态以进行3D重建。在这里，我们提出了Hydra，这是一种通过参数化K个神经场之一产生的结构来完全从头计算模拟构象和组成异质性的方法。我们采用了一种新的基于似然的损失函数，并证明了我们的方法在由具有高度构象变异的蛋白质混合物组成的合成数据集上的有效性。我们还在含有不同蛋白质复合物混合物的细胞裂解物的实验数据集上演示了Hydra。Hydra扩展了非均匀重建方法的表现力，从而将冷冻EM的范围扩大到越来越复杂的样本。 et.al.|[2412.09420](http://arxiv.org/abs/2412.09420)|null|
|**2024-12-11**|**From MLP to NeoMLP: Leveraging Self-Attention for Neural Fields**|神经场（NeFs）最近已成为编码各种模态时空信号的最先进方法。尽管NeFs在重建单个信号方面取得了成功，但它们作为下游任务（如分类或分割）中的表示，除了缺乏强大和可扩展的调节机制外，还受到参数空间及其潜在对称性的复杂性的阻碍。在这项工作中，我们从连接主义的原则中汲取灵感，设计了一种基于MLP的新架构，我们称之为NeoMLP。我们从一个被视为图的MLP开始，将其从一个多部分图转换为一个包含输入、隐藏和输出节点的完整图，并配备了高维特征。我们在此图上执行消息传递，并在所有节点之间通过自我关注进行权重共享。NeoMLP具有通过隐藏和输出节点进行调节的内置机制，这些节点充当一组潜在代码，因此，NeoMLP可以直接用作条件神经场。我们通过拟合高分辨率信号（包括多模态视听数据）来证明我们的方法的有效性。此外，我们通过使用单个骨干架构学习特定于实例的潜在代码集来拟合神经表示的数据集，然后将它们用于下游任务，优于最近最先进的方法。源代码开源于https://github.com/mkofinas/neomlp. et.al.|[2412.08731](http://arxiv.org/abs/2412.08731)|**[link](https://github.com/mkofinas/neomlp)**|
|**2024-12-11**|**Combining Neural Fields and Deformation Models for Non-Rigid 3D Motion Reconstruction from Partial Data**|我们介绍了一种新的数据驱动方法，用于从非刚性变形形状的非结构化和潜在的部分观测中重建时间相干的3D运动。我们的目标是为经历近等距变形的形状（如穿着宽松衣服的人）实现高保真运动重建。我们工作的关键新颖之处在于它能够将隐式形状表示与显式基于网格的变形模型相结合，从而在不依赖于参数化形状模型或解耦形状和运动的情况下实现详细和时间连贯的运动重建。每一帧都表示为从特征空间解码的神经场，在特征空间中，随着时间的推移，观测值被融合在一起，从而保留了输入数据中存在的几何细节。时间连贯性是通过应用于神经场中基础表面的相邻帧之间的近等距变形约束来实现的。我们的方法优于最先进的方法，正如它在从单眼深度视频重建的人类和动物运动序列中的应用所证明的那样。 et.al.|[2412.08511](http://arxiv.org/abs/2412.08511)|null|
|**2024-12-08**|**Unsupervised Multi-Parameter Inverse Solving for Reducing Ring Artifacts in 3D X-Ray CBCT**|由于X射线探测器的非理想响应，环形伪影在3D锥束计算机断层扫描（CBCT）中很普遍，严重降低了成像质量和可靠性。当前最先进的（SOTA）环伪影减少（RAR）算法依赖于广泛的成对CT样本进行监督学习。虽然有效，但这些方法并不能完全捕捉到环形伪影的物理特征，导致应用于域外数据时性能明显下降。此外，它们在3D CBCT中的应用受到高内存需求的限制。在这项工作中，我们介绍了\textbf{Riner}，这是一种将3D CBCT RAR表述为多参数逆问题的无监督方法。我们的核心创新是将X射线探测器响应参数化为微分物理模型中的可解变量。通过联合优化神经场以表示无伪影的CT图像，并直接从原始测量值估计响应参数，Riner消除了对外部训练数据的需求。此外，它还可适应不同的CT几何形状，提高了实用性。在模拟和真实数据集上的实证结果表明，Riner在性能上优于现有的SOTA RAR方法。 et.al.|[2412.05853](http://arxiv.org/abs/2412.05853)|null|
|**2024-12-06**|**Physics-informed reduced order model with conditional neural fields**|本研究提出了用于降阶建模（CNF-ROM）框架的条件神经场，以近似参数化偏微分方程（PDE）的解。该方法将用于随时间建模潜在动力学的参数神经ODE（PNODE）与从相应潜在状态重建PDE解的解码器相结合。我们为CNF-ROM引入了一个物理知情学习目标，其中包括两个关键组成部分。首先，该框架使用基于坐标的神经网络通过自动微分计算空间导数并应用时间导数的链式规则来计算和最小化PDE残差。其次，使用近似距离函数（ADF）施加精确的初始和边界条件（IC/BC）[Sukumar和Srivastava，CMAME，2022]。然而，当ADFs的二阶或高阶导数在边界的连接点处变得不稳定时，ADFs引入了一种权衡。为了解决这个问题，我们引入了一个受[Gladstone等人，NeurIPS ML4PS研讨会，2022年]启发的辅助网络。我们的方法通过参数外推和插值、时间外推以及与解析解的比较得到了验证。 et.al.|[2412.05233](http://arxiv.org/abs/2412.05233)|null|
|**2024-12-06**|**Spatially-Adaptive Hash Encodings For Neural Surface Reconstruction**|位置编码是神经场景重建方法的一个常见组成部分，它提供了一种将神经场的学习偏向于更粗糙或更精细表示的方法。当前的神经表面重建方法使用“一刀切”的编码方法，在所有场景中选择一组固定的编码函数，从而产生偏差。当前最先进的表面重建方法利用基于网格的多分辨率哈希编码来恢复高细节几何。我们提出了一种学习方法，通过掩盖以单独网格分辨率存储的特征的贡献，允许网络根据空间选择其编码基础。由此产生的空间自适应方法允许网络在不引入噪声的情况下适应更宽的频率范围。我们在标准基准曲面重建数据集上测试了我们的方法，并在两个基准数据集上实现了最先进的性能。 et.al.|[2412.05179](http://arxiv.org/abs/2412.05179)|null|
|**2024-12-06**|**DNF: Unconditional 4D Generation with Dictionary-based Neural Fields**|虽然通过基于扩散的形状3D生成模型取得了显著成功，但由于物体变形的复杂性，4D生成建模仍然具有挑战性。我们提出了DNF，这是一种用于无条件生成建模的新4D表示，它有效地对具有解纠缠形状和运动的可变形形状进行建模，同时捕获变形对象中的高保真细节。为了实现这一点，我们提出了一种字典学习方法，将4D运动与形状作为神经场进行分离。形状和运动都表示为学习潜在空间，其中每个可变形形状由其形状和运动全局潜在码、形状特定系数向量和共享字典信息表示。这在学习词典中捕获了特定形状的细节和全局共享信息。我们基于字典的表示法很好地平衡了保真度、连续性和压缩性——结合基于变换器的扩散模型，我们的方法能够生成有效、高保真的4D动画。 et.al.|[2412.05161](http://arxiv.org/abs/2412.05161)|null|
|**2024-12-04**|**Sparse-view Pose Estimation and Reconstruction via Analysis by Generative Synthesis**|推断一组多视图图像背后的3D结构通常需要解决两个相互依赖的任务——精确的3D重建需要精确的相机姿态，预测相机姿态依赖于（隐式或显式）对底层3D进行建模。经典的综合分析框架将这一推断视为一种联合优化，旨在解释观察到的像素，最近的实例通过基于梯度下降的初始姿态估计的姿态细化来学习表达性的3D表示（例如神经场）。然而，给定一组稀疏的观测视图，观测可能无法提供足够的直接证据来获得完整准确的3D。此外，姿势估计中的大误差可能不容易纠正，并可能进一步降低推断的3D。为了在这种具有挑战性的设置中实现稳健的3D重建和姿态估计，我们提出了SparseAGS，这是一种通过以下方式调整这种综合分析方法的方法：a）将基于新视图合成的生成先验与光度目标结合起来，以提高推断的3D的质量，b）明确地推理异常值，并使用基于连续优化策略的离散搜索来纠正它们。我们结合几个现成的姿态估计系统，在真实世界和合成数据集中验证我们的框架作为初始化。我们发现，它显著提高了基础系统的姿态精度，同时产生了高质量的3D重建，其效果优于当前多视图重建基线的结果。 et.al.|[2412.03570](http://arxiv.org/abs/2412.03570)|null|

<p align=right>(<a href=#updated-on-20241218>back to top</a>)</p>

[contributors-shield]: https://img.shields.io/github/contributors/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[contributors-url]: https://github.com/Vincentqyw/cv-arxiv-daily/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[forks-url]: https://github.com/Vincentqyw/cv-arxiv-daily/network/members
[stars-shield]: https://img.shields.io/github/stars/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[stars-url]: https://github.com/Vincentqyw/cv-arxiv-daily/stargazers
[issues-shield]: https://img.shields.io/github/issues/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[issues-url]: https://github.com/Vincentqyw/cv-arxiv-daily/issues

