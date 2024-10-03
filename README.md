[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]

## Updated on 2024.10.03
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
|**2024-10-02**|**EVER: Exact Volumetric Ellipsoid Rendering for Real-time View Synthesis**|我们提出了精确体积椭球体渲染（EVER），这是一种用于实时可微发射的纯体积渲染的方法。与最近3D高斯散斑（3DGS）的基于光栅化的方法不同，我们的基于基元的表示允许精确的体积渲染，而不是阿尔法合成3D高斯广告牌。因此，与3DGS不同，我们的公式不会受到爆裂伪影和视图依赖密度的影响，但仍然实现了$\sim\！在NVIDIA RTX4090上，720p分辨率下的帧率为30美元。由于我们的方法是建立在光线追踪的基础上的，因此它能够实现散焦模糊和相机失真（例如鱼眼相机）等效果，而这些效果很难通过光栅化来实现。我们证明，我们的方法比3DGS更准确，混合问题更少，并且在视图一致性渲染方面进行了后续工作，特别是在Zip-NeRF数据集中具有挑战性的大规模场景上，它在实时技术中取得了最清晰的结果。 et.al.|[2410.01804](http://arxiv.org/abs/2410.01804)|null|
|**2024-10-02**|**3DGS-DET: Empower 3D Gaussian Splatting with Boundary Guidance and Box-Focused Sampling for 3D Object Detection**|神经辐射场（NeRF）被广泛用于新颖的视图合成，并已被应用于3D对象检测（3DOD），通过视图合成表示为3DOD提供了一种有前景的方法。然而，NeRF面临着固有的局限性：（i）由于其隐式特性，3DOD的表示能力有限，以及（ii）渲染速度较慢。最近，3D高斯散斑（3DGS）已经成为解决这些局限性的显式3D表示。受这些优点的启发，本文首次将3DGS引入3DOD，确定了两个主要挑战：（i）高斯斑点的模糊空间分布：3DGS主要依赖于2D像素级监督，导致高斯斑点的3D空间分布不清楚，对象和背景之间的区分差，阻碍了3DOD；（ii）背景斑点过多：2D图像通常包含大量背景像素，导致重建的3DGS密度很高，其中许多噪声高斯斑点代表背景，对检测产生负面影响。为了应对挑战（i），我们利用3DGS重建来自2D图像的事实，并通过结合2D边界引导来显著增强高斯斑点的空间分布，从而更清晰地区分物体及其背景，提出了一种优雅高效的解决方案。为了应对挑战（ii），我们提出了一种使用2D框在3D空间中生成对象概率分布的框聚焦采样策略，允许在3D中进行有效的概率采样，以保留更多的对象斑点并减少噪声背景斑点。得益于我们的设计，我们的3DGS-DET明显优于基于SOTA NeRF的方法NeRF-DET，在mAP@0.25+8.1开始mAP@0.5ScanNet数据集，令人印象深刻的+31.5mAP@0.25ARKITCenes数据集。 et.al.|[2410.01647](http://arxiv.org/abs/2410.01647)|**[link](https://github.com/yangcaoai/3dgs-det)**|
|**2024-10-02**|**Gaussian Splatting in Mirrors: Reflection-Aware Rendering via Virtual Camera Optimization**|3D高斯散斑（3D-GS）的最新进展彻底改变了新的视图合成，促进了实时、高质量的图像渲染。然而，在涉及反射表面（特别是镜子）的场景中，3D-GS经常将反射误解为虚拟空间，导致镜子内的多视图渲染模糊和不一致。我们提出了一种新方法，旨在通过将反射建模为基于物理的虚拟相机来获得高质量的多视图一致反射渲染。我们使用3D-GS的深度和法线估计来估计镜面，并定义围绕镜面对称放置的虚拟相机。然后，这些虚拟相机用于解释场景中的镜面反射。为了解决镜面估计中的缺陷，我们提出了一种简单而有效的虚拟相机优化方法来提高反射质量。我们收集了一个新的镜像数据集，其中包括三个真实世界的场景，以进行更多样化的评估。Mirror-Nerf和我们的真实世界数据集上的实验验证证明了我们方法的有效性。与之前的最先进技术相比，我们在显著减少训练时间的同时，取得了相当或更优的结果。 et.al.|[2410.01614](http://arxiv.org/abs/2410.01614)|null|
|**2024-10-02**|**EVA-Gaussian: 3D Gaussian-based Real-time Human Novel View Synthesis under Diverse Camera Settings**|基于前馈的3D高斯散点方法在实时人类新颖视图合成方面表现出了卓越的能力。然而，现有的方法仅限于密集的视点设置，这限制了它们在各种相机视角差异的自由视点渲染中的灵活性。为了解决这一局限性，我们提出了一种名为EVA-Gassian的实时流水线，用于跨不同相机设置的3D人体新颖视图合成。具体来说，我们首先引入了一个高效的交叉视图注意力（EVA）模块，以准确估计源图像中每个3D高斯的位置。然后，我们将源图像与估计的高斯位置图进行整合，以预测3D高斯图像的属性和特征嵌入。此外，我们采用循环特征细化器来校正位置估计中由几何误差引起的伪影，并提高视觉保真度。为了进一步提高合成质量，我们为3D高斯属性和人脸地标引入了强大的锚丢失函数。THuman2.0和THumansit数据集的实验结果展示了我们的EVA高斯方法在不同相机设置下的渲染质量方面的优越性。项目页面：https://zhenliuzju.github.io/huyingdong/EVA-Gaussian. et.al.|[2410.01425](http://arxiv.org/abs/2410.01425)|null|
|**2024-10-02**|**AniSDF: Fused-Granularity Neural Surfaces with Anisotropic Encoding for High-Fidelity 3D Reconstruction**|神经辐射场最近彻底改变了新颖的视图合成，并实现了高保真渲染。然而，这些方法为了渲染质量而牺牲了几何体，限制了它们的进一步应用，包括重新照明和变形。如何在重建精确几何的同时合成照片级真实感渲染仍然是一个未解决的问题。在这项工作中，我们提出了AniSDF，这是一种新的方法，通过基于物理的编码来学习融合粒度的神经表面，以实现高保真度的3D重建。与之前的神经曲面不同，我们的融合粒度几何结构平衡了整体结构和精细的几何细节，产生了精确的几何重建。为了将几何体与反射外观区分开来，我们引入了混合辐射场，按照各向异性球面高斯编码（一种基于物理的渲染管道）对漫反射和镜面反射进行建模。通过这些设计，AniSDF可以重建具有复杂结构的对象，并生成高质量的渲染图。此外，我们的方法是一个统一的模型，不需要对特定对象进行复杂的超参数调整。大量实验表明，我们的方法在几何重建和新颖的视图合成方面都大大提高了基于SDF的方法的质量。 et.al.|[2410.01202](http://arxiv.org/abs/2410.01202)|null|
|**2024-10-01**|**GMT: Enhancing Generalizable Neural Rendering via Geometry-Driven Multi-Reference Texture Transfer**|新视图合成（NVS）旨在使用多视图图像在任意视点生成图像，神经辐射场（NeRF）的最新见解为显著改进做出了贡献。最近，对可推广NeRF（G-NeRF）的研究解决了NeRF中每场景优化的挑战。G-NeRF中动态构建辐射场简化了NVS过程，使其非常适合实际应用。同时，由于缺乏每个场景的优化，即使使用纹理丰富的多视图源输入，G-NeRF仍然难以表示特定场景的精细细节。作为补救措施，我们提出了一种几何驱动的多参考纹理传输网络（GMT），作为专为G-NeRF设计的即插即用模块。具体来说，我们提出了光线施加的可变形卷积（RayDCN），它对齐反映场景几何的输入和参考特征。此外，所提出的纹理保持变换器（TP Former）在保留纹理信息的同时聚合了多视图源特征。因此，我们的模块能够在图像增强过程中实现相邻像素之间的直接交互，这在每个像素具有独立渲染过程的G-NeRF模型中是不足的。这解决了阻碍捕获高频细节的限制。实验表明，我们的即插即用模块在各种基准数据集上持续改进了G-NeRF模型。 et.al.|[2410.00672](http://arxiv.org/abs/2410.00672)|**[link](https://github.com/yh-yoon/gmt)**|
|**2024-10-01**|**Cafca: High-quality Novel View Synthesis of Expressive Faces from Casual Few-shot Captures**|体积建模和神经辐射场表示彻底改变了3D人脸捕捉和逼真的新颖视图合成。然而，这些方法通常需要数百个多视图输入图像，因此不适用于输入少于少数的情况。我们提出了一种新的人脸体积先验，该先验允许从野外捕获的三个输入视图中进行高保真的表情人脸建模。我们的关键见解是，仅在合成数据上训练的隐式先验可以推广到极具挑战性的现实世界身份和表情，并呈现具有皱纹和睫毛等精细细节的新颖视图。我们利用3D可变形人脸模型来合成一个大型训练集，用不同的表情、头发、衣服和其他资产渲染每个身份。然后，我们在这个合成数据集上训练一个条件神经辐射场先验，并在推理时，在单个对象的一组非常稀疏的真实图像上微调模型。平均而言，微调只需要三个输入即可跨越合成域到实际域的差距。由此产生的个性化3D模型重建了强烈的特异性面部表情，在感知和照片度量质量方面，在稀疏输入的高质量新颖面部视图合成方面优于最先进的技术。 et.al.|[2410.00630](http://arxiv.org/abs/2410.00630)|null|
|**2024-09-30**|**RoCoTex: A Robust Method for Consistent Texture Synthesis with Diffusion Models**|文本到纹理生成最近引起了越来越多的关注，但现有的方法经常遇到视图不一致、明显接缝以及纹理和底层网格之间错位的问题。在本文中，我们提出了一种鲁棒的文本到纹理方法，用于生成与网格对齐良好的一致无缝纹理。我们的方法利用最先进的2D扩散模型，包括SDXL和多个ControlNet，来捕捉生成纹理中的结构特征和复杂细节。该方法还采用了一种对称的视图合成策略，并结合了区域提示，以提高视图的一致性。此外，它还引入了新的纹理混合和软修复技术，显著减少了接缝区域。大量实验表明，我们的方法优于现有的最先进的方法。 et.al.|[2409.19989](http://arxiv.org/abs/2409.19989)|null|
|**2024-10-01**|**RNG: Relightable Neural Gaussians**|3D高斯散斑（3DGS）在新颖的视图合成中显示出令人印象深刻的力量。然而，创建可重新点燃的3D资产，特别是对于形状不明确的对象（如毛发），仍然是一项具有挑战性的任务。对于这些场景，灯光、几何体和材质之间的分解更加模糊，因为曲面约束和分析着色模型都不成立。为了解决这个问题，我们提出了RNG，这是一种可重新照亮的神经高斯的新表示，能够重新照亮具有硬表面或蓬松边界的物体。我们避免了着色模型中的任何假设，但在每个高斯点中保留了特征向量，这些特征向量可以由MLP进一步解码为颜色。在前期工作的基础上，我们利用点光源来减少模糊性，并在网络中引入阴影感知条件。我们还提出了一种深度细化网络，以帮助3DGS框架下的阴影计算，从而在点光源下获得更好的阴影效果。此外，为了避免3DGS中阿尔法混合带来的模糊性，我们设计了一种混合前向延迟优化策略。因此，与之前基于神经辐射场的工作相比，我们在训练方面的速度提高了约20倍，在渲染方面的速度也提高了约600倍，RTX4090的每秒帧数为60美元。 et.al.|[2409.19702](http://arxiv.org/abs/2409.19702)|null|
|**2024-09-28**|**GS-EVT: Cross-Modal Event Camera Tracking based on Gaussian Splatting**|可靠的自我定位是许多智能移动平台的基本技能。本文探讨了使用事件相机进行运动跟踪，从而在困难的动态和光照条件下提供了一种具有固有鲁棒性的解决方案。为了规避基于事件相机的映射的挑战，该解决方案以交叉模态的方式构建。它跟踪直接来自基于帧的相机的地图表示。具体来说，所提出的方法在高斯飞溅之上运行，高斯飞溅是一种最先进的表示方法，可以实现高效和逼真的新颖视图合成。我们方法的关键在于一种新的姿态参数化，该参数化使用参考姿态加一阶动力学进行局部差分图像渲染。然后，在交错的粗到细优化方案中，将后者与集成事件的图像进行比较。正如我们的结果所证明的那样，高斯飞溅的真实视图渲染能力可以在各种公开可用和新记录的数据序列中实现稳定和准确的跟踪。 et.al.|[2409.19228](http://arxiv.org/abs/2409.19228)|null|

<p align=right>(<a href=#updated-on-20241003>back to top</a>)</p>

## 3D Reconstruction

|Publish Date|Title|Abstract|PDF|Code|
|---|---|---|---|---|
|**2024-10-02**|**GaussianBlock: Building Part-Aware Compositional and Editable 3D Scene by Primitives and Gaussians**|近年来，随着神经辐射场和高斯散斑技术的发展，三维重建技术已经达到了非常高的保真度。然而，通过这些方法学习的潜在表征是高度纠缠的，缺乏可解释性。在这篇论文中，我们提出了一种新的部分感知组合重建方法，称为GaussianBlock，它能够实现语义连贯和解纠缠的表示，允许类似于构建块的精确和物理编辑，同时保持高保真度。我们的GaussianBlock引入了一种混合表示法，该表示法利用了以灵活的可操作性和可编辑性而闻名的基元和在重建质量方面表现出色的3D Gaussian的优点。具体来说，我们通过一种新的注意力引导的中心丢失来实现语义连贯的原语，该丢失来自2D语义先验，并辅以动态分割和融合策略。此外，我们利用与基元杂交的3D高斯分布来细化结构细节并提高保真度。此外，采用绑定继承策略来加强和维护两者之间的连接。事实证明，我们重建的场景在不同的基准测试中表现出了解纠缠、构图和紧凑的特点，实现了无缝、直接和精确的编辑，同时保持了高质量。 et.al.|[2410.01535](http://arxiv.org/abs/2410.01535)|null|
|**2024-10-02**|**SurgPointTransformer: Vertebrae Shape Completion with RGB-D Data**|最先进的计算机和机器人辅助手术系统在很大程度上依赖于CT和荧光透视等术中成像技术来生成患者解剖结构的详细3D可视化。虽然成像技术非常准确，但它们基于电离辐射，使患者和临床医生暴露在外。本研究介绍了一种使用RGB-D数据重建3D脊柱解剖结构的无辐射替代方法。从外科医生在手术过程中形成的3D“心理图”中汲取灵感，我们介绍了SurgPointTransformer，这是一种用于手术应用的形状完成方法，可以从暴露表面的稀疏观察中准确重建未暴露的脊柱区域。我们的方法包括两个主要步骤：分割和形状完成。分割步骤包括脊柱定位和分割，然后是脊椎分割。然后，对分割的脊椎点云进行SurgPointTransformer处理，该处理利用注意力机制来学习可见表面特征和底层解剖结构之间的模式。为了进行评估，我们使用了九个样本的离体数据集。他们的CT数据用于建立地面实况数据，这些数据用于与我们的方法的输出进行比较。我们的方法明显优于最先进的基线，平均倒角距离为5.39，F分数为0.85，地球移动器距离为0.011，信噪比为22.90 dB。这项研究展示了我们的重建方法在3D椎体形状完成方面的潜力。它能够在没有电离辐射或侵入性成像的情况下对整个腰椎进行3D重建和手术指导。我们的工作有助于计算机辅助和机器人辅助手术，提高这些系统的感知和智能。 et.al.|[2410.01443](http://arxiv.org/abs/2410.01443)|null|
|**2024-10-02**|**AniSDF: Fused-Granularity Neural Surfaces with Anisotropic Encoding for High-Fidelity 3D Reconstruction**|神经辐射场最近彻底改变了新颖的视图合成，并实现了高保真渲染。然而，这些方法为了渲染质量而牺牲了几何体，限制了它们的进一步应用，包括重新照明和变形。如何在重建精确几何的同时合成照片级真实感渲染仍然是一个未解决的问题。在这项工作中，我们提出了AniSDF，这是一种新的方法，通过基于物理的编码来学习融合粒度的神经表面，以实现高保真度的3D重建。与之前的神经曲面不同，我们的融合粒度几何结构平衡了整体结构和精细的几何细节，产生了精确的几何重建。为了将几何体与反射外观区分开来，我们引入了混合辐射场，按照各向异性球面高斯编码（一种基于物理的渲染管道）对漫反射和镜面反射进行建模。通过这些设计，AniSDF可以重建具有复杂结构的对象，并生成高质量的渲染图。此外，我们的方法是一个统一的模型，不需要对特定对象进行复杂的超参数调整。大量实验表明，我们的方法在几何重建和新颖的视图合成方面都大大提高了基于SDF的方法的质量。 et.al.|[2410.01202](http://arxiv.org/abs/2410.01202)|null|
|**2024-10-02**|**Flex3D: Feed-Forward 3D Generation With Flexible Reconstruction Model And Input View Curation**|从文本、单幅图像或稀疏视图图像生成高质量的3D内容仍然是一项具有广泛应用的具有挑战性的任务。现有的方法通常采用多视图扩散模型来合成多视图图像，然后进行前馈过程进行3D重建。然而，这些方法往往受到少量固定数量的输入视图的限制，限制了它们捕获不同观点的能力，更糟糕的是，如果合成视图的质量较差，则会导致次优的生成结果。为了解决这些局限性，我们提出了Flex3D，这是一种新颖的两阶段框架，能够利用任意数量的高质量输入视图。第一阶段包括候选视图生成和管理管道。我们采用微调的多视图图像扩散模型和视频扩散模型来生成候选视图池，从而能够丰富地表示目标3D对象。随后，视图选择管道根据质量和一致性过滤这些视图，确保只有高质量和可靠的视图用于重建。在第二阶段，将策划的视图输入到灵活重建模型（FlexRM）中，该模型基于可以有效处理任意数量输入的变压器架构。FlemRM利用三平面表示直接输出3D高斯点，实现高效和详细的3D生成。通过对设计和培训策略的广泛探索，我们优化了FlexRM，以在重建和生成任务中实现卓越的性能。我们的结果表明，Flex3D实现了最先进的性能，与几种最新的前馈3D生成模型相比，在3D生成任务中的用户研究获胜率超过92%。 et.al.|[2410.00890](http://arxiv.org/abs/2410.00890)|null|
|**2024-10-01**|**A Low-Cost, High-Speed, and Robust Bin Picking System for Factory Automation Enabled by a Non-Stop, Multi-View, and Active Vision Scheme**|工厂自动化中的拣选系统通常面临由金属物体的稀疏和嘈杂的3D数据引起的鲁棒性问题。利用多个视图，特别是使用单次3D传感器和“手头传感器”配置，由于其有效性、灵活性和低成本而越来越受欢迎。在移动3D传感器以获取多个视图进行3D融合、关节优化或主动视觉时，会遇到低速问题。这是因为传感被视为一个与运动任务解耦的模块，而不是专门为垃圾箱拣选系统设计的。为了解决这些问题，我们设计了一个垃圾箱拣选系统，该系统将多视图、主动视觉方案与“手头传感器”配置中的运动任务紧密结合。它不仅通过将高速传感方案与机器人的位置动作并行化来加速系统，而且还决定了下一个传感路径，以保持整个拾取过程的连续性。与其他只关注传感评估的人不同，我们还通过在5种不同类型的物体上进行实验来评估我们的设计，而不需要人为干预。我们的实验表明，整个传感方案在CPU上可以在1.682秒内（最大）完成，平均拾取完成率超过97.75%。由于与机器人运动的并行化，传感方案的平均节拍时间仅为0.635秒。 et.al.|[2410.00706](http://arxiv.org/abs/2410.00706)|null|
|**2024-10-01**|**An Illumination-Robust Feature Extractor Augmented by Relightable 3D Reconstruction**|视觉特征的描述通常依赖于局部强度和梯度方向，近年来在机器人导航和定位中得到了广泛的应用。然而，视觉特征的提取通常会受到光照条件变化的干扰，这使得它在现实世界的应用中具有挑战性。以前的工作已经通过建立具有光照条件变化的数据集来解决这个问题，但可能成本高昂且耗时。本文提出了一种光照鲁棒特征提取器的设计过程，其中采用了最近开发的可重新照亮的3D重建技术，在不同的光照条件下快速直接地生成数据。提出了一种自监督框架，用于提取特征，该框架在关键点的可重复性和描述符在良好和不良光照条件下的相似性方面具有优势。实验证明了所提出的鲁棒特征提取方法的有效性。消融研究也表明了自我监督框架设计的有效性。 et.al.|[2410.00629](http://arxiv.org/abs/2410.00629)|null|
|**2024-10-01**|**3DGR-CAR: Coronary artery reconstruction from ultra-sparse 2D X-ray views with a 3D Gaussians representation**|重建三维冠状动脉对于冠状动脉疾病的诊断、治疗计划和手术导航非常重要。传统的重建技术通常需要多次投影，而从稀疏视图X射线投影进行重建是减少辐射剂量的一种潜在方法。然而，冠状动脉在3D体积中的极端稀疏性和超有限数量的投影对高效准确的3D重建构成了重大挑战。为此，我们提出了3DGR-CAR，这是一种用于从超稀疏X射线投影重建冠状动脉的3D高斯表示。我们利用3D高斯表示来避免冠状动脉数据极度稀疏造成的效率低下，并提出了一种高斯中心预测器来克服超稀疏视图投影中的噪声高斯初始化。所提出的方案仅需2个视图即可实现快速准确的3D冠状动脉重建。在两个数据集上的实验结果表明，所提出的方法在体素精度和冠状动脉视觉质量方面明显优于其他方法。该代码将在https://github.com/windrise/3DGR-CAR. et.al.|[2410.00404](http://arxiv.org/abs/2410.00404)|**[link](https://github.com/windrise/3dgr-car)**|
|**2024-10-01**|**Seamless Augmented Reality Integration in Arthroscopy: A Pipeline for Articular Reconstruction and Guidance**|关节镜是一种用于诊断和治疗关节问题的微创手术。关节镜的临床工作流程通常涉及通过小切口将关节镜插入关节，在此过程中，外科医生主要依靠关节镜的视觉评估进行导航和操作。然而，关节镜有限的视野和缺乏深度感知给在手术过程中导航复杂的关节结构和实现手术精度带来了挑战。为了提高术中意识，我们提出了一种强大的管道，该管道结合了同时定位和映射、深度估计和3D高斯飞溅，仅基于单眼关节镜视频即可真实地重建关节内结构。将3D重建扩展到增强现实（AR）应用，我们的解决方案以人体在环方式为关节切迹测量和注释锚定提供AR辅助。与传统的基于运动和神经辐射场的结构方法相比，我们的流水线平均在7分钟内实现了密集的3D重建和具有竞争力的渲染保真度，并具有显式的3D表示。当在四个体模数据集上进行评估时，我们的方法平均实现了RMSE=2.21mm的重建误差、PSNR=32.86和SSIM=0.89。由于我们的管道能够直接从单眼关节镜进行AR重建和引导，而无需任何额外的数据和/或硬件，因此我们的解决方案可能有助于提高关节镜手术中的意识和手术精度。我们的AR测量工具的精度在1.59+/-1.81mm以内，AR注释工具的mIoU为0.721。 et.al.|[2410.00386](http://arxiv.org/abs/2410.00386)|null|
|**2024-10-01**|**Revisiting the Role of Texture in 3D Person Re-identification**|本研究介绍了一种新的3D人物重新识别（re-ID）框架，该框架利用3D重建中现成的高分辨率纹理数据来提高人物重新识别任务的性能和可解释性。我们提出了一种通过结合UVTexture映射来强调3D人物重新识别模型中纹理的方法，该方法可以更好地区分人类主体。我们的方法独特地将UVTexture及其热图与3D模型相结合，以可视化和解释人的重新识别过程。特别是，可视化和解释是通过激活图和基于属性的注意力图来实现的，这些图突出了有助于人员重新识别决策的重要区域和特征。我们的贡献包括：（1）一种使用UVTexture处理在3D模型中强调纹理的新技术，（2）一种通过3D模型和UVTexture映射的组合来解释人重新ID匹配的创新方法，以及（3）在3D人重新ID方面实现了最先进的性能。我们通过公开所有数据、代码和模型来确保结果的可重复性。 et.al.|[2410.00348](http://arxiv.org/abs/2410.00348)|null|
|**2024-09-30**|**DressRecon: Freeform 4D Human Reconstruction from Monocular Video**|我们提出了一种从单目视频中重建时间一致的人体模型的方法，重点是极其宽松的衣服或手持物体的交互。之前在人体重建方面的工作要么局限于没有物体交互的紧身衣服，要么需要校准的多视图捕捉或个性化的模板扫描，而大规模收集这些数据成本很高。我们对高质量但灵活的重建的关键见解是，将关于关节体形状的通用人类先验（从大规模训练数据中学习）与视频特定的关节“骨骼袋”变形（通过测试时间优化适合单个视频）仔细结合。我们通过学习一个神经隐式模型来实现这一点，该模型将身体和衣服的变形作为单独的运动模型层来解开。为了捕捉服装的微妙几何形状，我们在优化过程中利用了基于图像的先验，如人体姿势、表面法线和光流。由此产生的神经场可以提取到时间一致的网格中，或进一步优化为显式3D高斯分布，以实现高保真交互式渲染。在具有高度挑战性的服装变形和物体交互的数据集上，DressReston可以产生比现有技术更高保真的3D重建。项目页面：https://jefftan969.github.io/dressrecon/ et.al.|[2409.20563](http://arxiv.org/abs/2409.20563)|null|

<p align=right>(<a href=#updated-on-20241003>back to top</a>)</p>

## Diffusion

|Publish Date|Title|Abstract|PDF|Code|
|---|---|---|---|---|
|**2024-10-02**|**A Catalog of Pulsar X-ray Filaments**|我们展示了首个钱德拉X射线天文台（CXO）的“脉冲星X射线细丝”或“错位外流”目录。这些是线性同步辐射特征，由从弓形激波脉冲星逃逸的超相对论电子和正电子提供动力。细丝与（大）脉冲星速度不对齐，将其与脉冲星风星云（PWN）轨迹区分开来，后者在CXO ACIS图像中也经常可见。使用统一方法提取了五根安全细丝和三根候选细丝的光谱拟合和形态特性。我们在CXO档案数据中搜索线性扩散特征；恢复已知的示例，并识别出一些额外的弱候选。我们还报告了CXO ACIS对脉冲星的快照调查，这些脉冲星的性质与细丝生产者相似，没有发现新的细丝，但有一些漫射发射，包括一条PWN尾迹。最后，我们根据这些新的观测结果，为创建细丝所需的脉冲星特性提供了一个更新的模型。 et.al.|[2410.01807](http://arxiv.org/abs/2410.01807)|null|
|**2024-10-02**|**FabricDiffusion: High-Fidelity Texture Transfer for 3D Garments Generation from In-The-Wild Clothing Images**|我们介绍了FabricDiffusion，这是一种将织物纹理从单个服装图像转移到任意形状的3D服装的方法。现有的方法通常通过2D到3D纹理映射或通过生成模型进行深度感知修复来合成服装表面的纹理。不幸的是，这些方法往往难以捕捉和保存纹理细节，特别是由于输入图像中具有挑战性的遮挡、失真或姿态。受时尚行业中大多数服装都是通过缝合具有平坦、可重复纹理的缝制图案来构建的观察结果的启发，我们将服装纹理转移的任务定义为提取无失真、可平铺的纹理材料，然后将其映射到服装的UV空间上。基于这一认识，我们使用大规模合成数据集训练去噪扩散模型，以纠正输入纹理图像中的失真。此过程产生了一个平面纹理贴图，可以与现有的基于物理的渲染（PBR）材质生成管道紧密耦合，从而在各种照明条件下对服装进行逼真的重新照明。我们证明FabricDiffusion可以从单个服装图像中传递各种特征，包括纹理图案、材料属性以及详细的印花和徽标。广泛的实验表明，我们的模型在合成数据和现实世界中的野生服装图像上明显优于最先进的方法，同时推广到看不见的纹理和服装形状。 et.al.|[2410.01801](http://arxiv.org/abs/2410.01801)|null|
|**2024-10-02**|**Bellman Diffusion: Generative Modeling as Learning a Linear Operator in the Distribution Space**|深度生成模型（DGM），包括基于能量的模型（EBM）和基于分数的生成模型（SGM），具有先进的高保真数据生成和复杂的连续分布近似。然而，它们在马尔可夫决策过程（MDP）中的应用，特别是在分布式强化学习（RL）中，仍然没有得到充分的探索，传统的基于直方图的方法在该领域占据主导地位。本文严格强调，这种应用差距是由现代DGM的非线性引起的，这与MDP中Bellman方程所要求的线性相冲突。例如，EBM涉及非线性操作，如能量函数的指数化和常数的归一化。为了解决这个问题，我们引入了贝尔曼扩散，这是一种新的DGM框架，通过梯度和标量场建模来保持MDP的线性。通过基于散度的训练技术优化神经网络代理和一种新型的随机微分方程（SDE）进行采样，贝尔曼扩散保证收敛到目标分布。我们的实证结果表明，Bellman Diffusion实现了精确的场估计，并且是一个功能强大的图像生成器，在分布式RL任务中，其收敛速度比传统的基于直方图的基线快1.5倍。这项工作使DGM能够有效地集成到MDP应用程序中，为高级决策框架开辟了新的途径。 et.al.|[2410.01796](http://arxiv.org/abs/2410.01796)|null|
|**2024-10-02**|**Dynamical-generative downscaling of climate model ensembles**|区域高分辨率气候预测对于农业、水文和自然灾害风险评估等许多应用至关重要。动态降尺度是产生本地化未来气候信息的最先进方法，涉及运行由地球系统模型（ESM）驱动的区域气候模型（RCM），但计算成本太高，无法应用于大型气候预测集。我们提出了一种将动态降尺度与生成人工智能相结合的新方法，以降低降尺度气候预测的成本并提高其不确定性估计。在我们的框架中，RCM动态地将ESM输出缩减到中间分辨率，然后是生成扩散模型，进一步将分辨率细化到目标尺度。这种方法利用了基于物理的模型的通用性和扩散模型的采样效率，实现了大型多模型集成的降尺度。我们根据CMIP6集合的动态降尺度气候预测来评估我们的方法。我们的结果表明，与较小集合的动态降尺度或传统的经验统计降尺度方法等替代方案相比，它能够为未来的区域气候提供更准确的不确定性界限。我们还表明，动态生成降尺度导致的误差明显低于偏差校正和空间分解（BCSD），并且更准确地捕获了气象场的光谱和多元相关性。这些特征使动态生成框架成为一种灵活、准确和有效的方法，用于缩减大规模的气候预测，目前纯动态缩减是无法实现的。 et.al.|[2410.01776](http://arxiv.org/abs/2410.01776)|null|
|**2024-10-02**|**Integrable Matrix Probabilistic Diffusions and the Matrix Stochastic Heat Equation**|我们引入了随机热方程MSHE的矩阵版本，并获得了其在空间维度 $D=1$上的显式不变测度。我们证明，在弱噪声区域，它是经典可积的，这是根据虚时$1D$ 非线性薛定谔方程的矩阵扩展，这使我们能够通过逆散射研究其短时大偏差。MSHE可以被视为最近引入的方形晶格上矩阵对数Gamma聚合物的连续极限。我们还展示了该离散模型的经典可积性，以及半离散矩阵O'Connell-Yor聚合物和矩阵严格弱聚合物的其他扩展。对于所有这些模型，我们通过对动态作用进行涨落-耗散变换，得到了它们弱噪声区的Lax对，以及不变测度。 et.al.|[2410.01764](http://arxiv.org/abs/2410.01764)|null|
|**2024-10-02**|**ImageFolder: Autoregressive Image Generation with Folded Tokens**|图像标记器对于视觉生成模型至关重要，例如扩散模型（DM）和自回归（AR）模型，因为它们构建了建模的潜在表示。增加标记长度是提高图像重建质量的常用方法。然而，令牌长度较长的令牌化器并不能保证实现更好的生成质量。在令牌长度方面，重建和生成质量之间存在权衡。本文研究了标记长度对图像重建和生成的影响，并为折衷提供了一种灵活的解决方案。我们提出了ImageFolder，这是一种语义标记器，它提供空间对齐的图像标记，可以在自回归建模过程中折叠，以提高生成效率和质量。为了在不增加令牌长度的情况下增强代表性能力，我们利用双分支乘积量化来捕获图像的不同上下文。具体来说，在一个分支中引入语义正则化来鼓励压缩语义信息，而另一个分支则被设计用于捕获剩余的像素级细节。大量实验证明，ImageFolder标记器具有卓越的图像生成质量和更短的标记长度。 et.al.|[2410.01756](http://arxiv.org/abs/2410.01756)|**[link](https://github.com/lxa9867/imagefolder)**|
|**2024-10-02**|**VitaGlyph: Vitalizing Artistic Typography with Flexible Dual-branch Diffusion Models**|艺术排版是一种以可想象和可读的方式将输入字符的含义可视化的技术。借助强大的文本到图像扩散模型，现有方法直接设计输入字符的整体几何形状和纹理，这使得确保创造力和易读性变得具有挑战性。在本文中，我们介绍了一种双分支和免训练的方法，即VitaGlyph，它能够实现灵活的艺术排版以及可控的几何变化，以保持可读性。VitaGlyph的关键见解是将输入角色视为由主体和周围组成的场景，然后在不同程度的几何变换下渲染它们。主体灵活地表达了输入字符的基本概念，而周围环境在不改变形状的情况下丰富了相关背景。具体来说，我们通过一个三阶段框架来实现VitaGlyph：（i）知识获取利用大型语言模型来设计主题和周围环境的文本描述。（ii）区域分解检测与主题描述最匹配的部分，并将输入字形图像划分为主题和周围区域。（iii）排版风格化首先通过语义排版细化主题区域的结构，然后通过可控合成生成分别渲染主题和周围区域的纹理。实验结果表明，VitaGlyph不仅具有更好的艺术性和可读性，而且能够描绘多种定制概念，从而促进更具创造性和令人愉悦的艺术排版生成。我们的代码将在https://github.com/Carlofkl/VitaGlyph. et.al.|[2410.01738](http://arxiv.org/abs/2410.01738)|**[link](https://github.com/carlofkl/vitaglyph)**|
|**2024-10-02**|**HarmoniCa: Harmonizing Training and Inference for Better Feature Cache in Diffusion Transformer Acceleration**|扩散变换器（DiTs）因其出色的可扩展性和在生成任务中的卓越性能而备受瞩目。然而，它们相当大的推理成本阻碍了实际部署。特征缓存机制涉及跨时间步存储和检索冗余计算，有望减少扩散模型中的每一步推理时间。大多数现有的DiT缓存方法都是手动设计的。尽管基于学习的方法试图自适应地优化策略，但它存在训练和推理之间的差异，这阻碍了性能和加速比。经过详细分析，我们发现这些差异主要源于两个方面：（1）先验时间步长忽略，训练忽略了早期时间步长缓存使用的影响，以及（2）目标不匹配，训练目标（在每个时间步长中对齐预测噪声）偏离了推理目标（生成高质量图像）。为了缓解这些差异，我们提出了HarmoniCa，这是一种将训练和推理与基于逐步去噪训练（SDT）和图像错误代理引导目标（IEPO）的新型基于学习的缓存框架相协调的新方法。与传统的训练范式相比，新提出的SDT保持了去噪过程的连续性，使模型能够在训练过程中利用先前时间步长的信息，类似于它在推理过程中的操作方式。此外，我们设计了IEPO，它集成了一种高效的代理机制来近似重用缓存特征引起的最终图像错误。因此，IEPO有助于平衡最终图像质量和缓存利用率，解决了只考虑缓存使用对每个时间步预测输出的影响的训练问题。 et.al.|[2410.01723](http://arxiv.org/abs/2410.01723)|null|
|**2024-10-02**|**COMUNI: Decomposing Common and Unique Video Signals for Diffusion-based Video Generation**|由于视频记录了连贯移动的对象，因此相邻的视频帧具有共性（对象外观相似）和唯一性（姿势略有变化）。为了防止常见视频信号的冗余建模，我们提出了一种新的基于扩散的框架，称为COMUNI，它分解common和UNIque视频信号，以实现高效的视频生成。我们的方法将视频信号的分解与视频生成任务分开，从而降低了生成模型的计算复杂度。特别是，我们引入了CU-VAE来分解视频信号并将其编码为潜在特征。为了以自监督的方式训练CU-VAE，我们使用级联合并模块来重建视频信号，并使用时间无关的视频解码器来重建视频帧。然后，我们提出了CU-LDM来对视频生成的潜在特征进行建模，该模型采用两个特定的扩散流来同时对共同和独特的潜在特征建模。我们进一步利用额外的联合模块对共同和独特的潜在特征进行交叉建模，并采用一种新的位置嵌入方法来确保生成视频的内容一致性和运动连贯性。位置嵌入方法将空间和时间绝对位置信息合并到关节模块中。大量实验证明了分解常见和独特视频信号以生成视频的必要性，以及我们提出的方法的有效性和效率。 et.al.|[2410.01718](http://arxiv.org/abs/2410.01718)|null|
|**2024-10-02**|**COSMIC: Compress Satellite Images Efficiently via Diffusion Compensation**|随着太空中卫星数量的迅速增加及其能力的增强，卫星收集的地球观测图像数量正在超过卫星到地面链路的传输限制。尽管现有的学习图像压缩解决方案通过使用复杂的编码器提取富有成效的特征作为压缩并使用解码器进行重建来实现显著的性能，但仍然很难将这些复杂的编码器直接部署在当前计算能力和电源有限的卫星嵌入式GPU上，以在轨道上压缩图像。在本文中，我们提出了一种简单而有效的学习压缩解决方案COSMIC，用于传输卫星图像。我们首先在卫星上设计了一个轻量级的编码器（即将FLOP降低2.6美元/平方米5倍），以实现高图像压缩比，从而节省卫星到地面的链路。然后，对于地面重建，为了处理由于简化编码器而导致的特征提取能力下降，我们提出了一种基于扩散的模型来补偿解码时的图像细节。我们的见解是，卫星的地球观测照片不仅仅是图像，而且是具有文本到图像配对性质的多模态数据，因为它们是用丰富的传感器数据（如坐标、时间戳等）收集的，这些数据可以用作扩散生成的条件。大量实验表明，COSMIC在感知和失真度量方面都优于最先进的基线。 et.al.|[2410.01698](http://arxiv.org/abs/2410.01698)|**[link](https://github.com/joanna-0421/cosmic)**|

<p align=right>(<a href=#updated-on-20241003>back to top</a>)</p>

## NeRF

|Publish Date|Title|Abstract|PDF|Code|
|---|---|---|---|---|
|**2024-09-30**|**DressRecon: Freeform 4D Human Reconstruction from Monocular Video**|我们提出了一种从单目视频中重建时间一致的人体模型的方法，重点是极其宽松的衣服或手持物体的交互。之前在人体重建方面的工作要么局限于没有物体交互的紧身衣服，要么需要校准的多视图捕捉或个性化的模板扫描，而大规模收集这些数据成本很高。我们对高质量但灵活的重建的关键见解是，将关于关节体形状的通用人类先验（从大规模训练数据中学习）与视频特定的关节“骨骼袋”变形（通过测试时间优化适合单个视频）仔细结合。我们通过学习一个神经隐式模型来实现这一点，该模型将身体和衣服的变形作为单独的运动模型层来解开。为了捕捉服装的微妙几何形状，我们在优化过程中利用了基于图像的先验，如人体姿势、表面法线和光流。由此产生的神经场可以提取到时间一致的网格中，或进一步优化为显式3D高斯分布，以实现高保真交互式渲染。在具有高度挑战性的服装变形和物体交互的数据集上，DressReston可以产生比现有技术更高保真的3D重建。项目页面：https://jefftan969.github.io/dressrecon/ et.al.|[2409.20563](http://arxiv.org/abs/2409.20563)|null|
|**2024-09-25**|**TalkinNeRF: Animatable Neural Fields for Full-Body Talking Humans**|我们介绍了一种新的框架，该框架从单眼视频中学习全身说话的人的动态神经辐射场（NeRF）。之前的工作只代表身体姿势或面部。然而，人类通过全身进行交流，结合身体姿势、手势和面部表情。在这项工作中，我们提出了TalkinNeRF，这是一个基于NeRF的统一网络，代表了整体4D人体运动。给定一个受试者的单眼视频，我们学习身体、面部和手的相应模块，这些模块结合在一起生成最终结果。为了捕捉复杂的手指关节，我们学习了手的额外变形场。我们的多身份表示能够同时训练多个科目，以及在完全看不见的姿势下进行强大的动画。只要输入一段短视频，它也可以推广到新的身份。我们展示了最先进的性能，用于为全身说话的人类制作动画，具有精细的手部发音和面部表情。 et.al.|[2409.16666](http://arxiv.org/abs/2409.16666)|null|
|**2024-09-24**|**Generative 3D Cardiac Shape Modelling for In-Silico Trials**|我们提出了一种深度学习方法，基于将形状表示为神经有符号距离场的零级集，对合成主动脉形状进行建模和生成，该方法受一系列可训练的嵌入向量的约束，并对每个形状的几何特征进行编码。通过使神经场在采样表面点上消失并强制其空间梯度具有单位范数，在从CT图像重建的主动脉根部网格数据集上训练网络。实证结果表明，我们的模型可以高保真地表示主动脉形状。此外，通过从学习到的嵌入向量中采样，我们可以生成类似于真实患者解剖结构的新形状，可用于计算机模拟试验。 et.al.|[2409.16058](http://arxiv.org/abs/2409.16058)|null|
|**2024-09-21**|**MOSE: Monocular Semantic Reconstruction Using NeRF-Lifted Noisy Priors**|由于缺乏几何指导和不完美的视图相关2D先验，从单眼图像中精确重建密集和语义注释的3D网格仍然是一项具有挑战性的任务。尽管我们已经见证了隐式神经场景表示的最新进展，能够简单地从多视图图像中进行精确的2D渲染，但很少有研究仅使用单眼先验来解决3D场景理解问题。在本文中，我们提出了MOSE，这是一种神经场语义重建方法，可以将推断的图像级噪声先验提升到3D，在3D和2D空间中产生精确的语义和几何。我们方法的关键动机是利用通用类不可知的分段掩码作为指导，在训练过程中促进渲染语义的局部一致性。在语义的帮助下，我们进一步将平滑正则化应用于无纹理区域，以获得更好的几何质量，从而实现几何和语义的互惠互利。在ScanNet数据集上的实验表明，我们的MOSE在3D语义分割、2D语义分割和3D表面重建任务的所有指标上都优于相关基线。 et.al.|[2409.14019](http://arxiv.org/abs/2409.14019)|null|
|**2024-09-17**|**SplatFields: Neural Gaussian Splats for Sparse 3D and 4D Reconstruction**|从多视图图像中数字化3D静态场景和4D动态事件长期以来一直是计算机视觉和图形学领域的一个挑战。最近，3D高斯散斑（3DGS）已经成为一种实用且可扩展的重建方法，由于其令人印象深刻的重建质量、实时渲染能力以及与广泛使用的可视化工具的兼容性而越来越受欢迎。然而，该方法需要大量的输入视图来实现高质量的场景重建，这引入了一个重大的实际瓶颈。在捕捉动态场景时，这一挑战尤为严峻，因为部署广泛的相机阵列的成本可能高得令人望而却步。在这项工作中，我们发现斑点特征缺乏空间自相关性是导致3DGS技术在稀疏重建环境中性能不佳的因素之一。为了解决这个问题，我们提出了一种优化策略，通过将splat特征建模为相应隐式神经场的输出，有效地正则化splat特征。这导致在各种场景中重建质量的一致提高。我们的方法有效地处理了静态和动态情况，这在不同设置和场景复杂性的广泛测试中得到了证明。 et.al.|[2409.11211](http://arxiv.org/abs/2409.11211)|null|
|**2024-09-17**|**Neural Fields for Adaptive Photoacoustic Computed Tomography**|光声计算机断层扫描（PACT）是一种具有广泛医学应用的非侵入性成像技术。传统的PACT图像重建算法受到组织中声速不均匀（SOS）引起的波前失真的影响，导致图像质量下降。考虑到这些影响可以提高图像质量，但测量SOS分布的实验成本很高。另一种方法是仅使用PA信号对初始压力图像和SOS进行联合重建。现有的关节重建方法存在局限性：计算成本高，无法直接恢复SOS，以及依赖于不准确的简化假设。隐式神经表示或神经场是计算机视觉中的一种新兴技术，用于通过基于坐标的神经网络学习物理场的有效和连续表示。在这项工作中，我们介绍了NF-APACT，这是一种高效的自监督框架，利用神经场来估计SOS，以实现准确和鲁棒的多通道解卷积。我们的方法比现有方法更快、更准确地消除了SOS像差。我们在一个新的数值体模以及实验收集的体模和体内数据上证明了我们的方法的成功。我们的代码和数字幻影可在https://github.com/Lukeli0425/NF-APACT. et.al.|[2409.10876](http://arxiv.org/abs/2409.10876)|null|
|**2024-09-09**|**Lagrangian Hashing for Compressed Neural Field Representations**|我们提出了拉格朗日散列，这是一种神经场的表示，结合了依赖于欧拉网格（即~InstantNGP）的快速训练NeRF方法的特征，以及使用配备有特征的点作为表示信息的方法（例如3D高斯散点或PointNeRF）。我们通过将基于点的表示合并到InstantNGP表示的分层哈希表的高分辨率层中来实现这一点。由于我们的点具有影响域，我们的表示可以被解释为哈希表中存储的高斯混合。我们提出的损失鼓励我们的高斯人向需要更多代表预算才能充分代表的地区移动。我们的主要发现是，我们的表示允许使用更紧凑的表示来重建信号，而不会影响质量。 et.al.|[2409.05334](http://arxiv.org/abs/2409.05334)|null|
|**2024-09-08**|**Exploring spectropolarimetric inversions using neural fields. Solar chromospheric magnetic field under the weak-field approximation**|全斯托克斯偏振数据集来源于狭缝光谱仪或窄带滤光片图，如今已被常规采集。随着二维光谱偏振仪和允许长时间高质量观测序列的观测技术的出现，数据速率正在增加。在光谱偏振反演中，显然需要通过利用推断物理量的时空相干性来超越传统的逐像素策略。我们探索了神经网络作为时间和空间（也称为神经场）上物理量的连续表示的潜力，用于光谱极化反演。我们已经实现并测试了一个神经场，以在弱场近似（WFA）下执行磁场矢量的推理（也称为物理知情神经网络的方法）。通过使用神经场来描述磁场矢量，我们可以通过假设物理量是坐标的连续函数来在空间和时间域中正则化解。我们研究了Ca II 8542 A谱线的合成和真实观测结果。我们还探讨了其他显式正则化的影响，例如使用外推磁场的信息或色球原纤维的取向。与传统的逐像素反演相比，神经场方法提高了磁场矢量重建的保真度，特别是横向分量。这种隐式正则化是一种提高观测值有效信噪比的方法。虽然它比逐像素WFA估计慢，但这种方法通过减少自由参数的数量并在解决方案中引入时空约束，显示出深度分层反演的巨大潜力。 et.al.|[2409.05156](http://arxiv.org/abs/2409.05156)|**[link](https://github.com/cdiazbas/neural_wfa)**|
|**2024-09-04**|**MDNF: Multi-Diffusion-Nets for Neural Fields on Meshes**|我们提出了一种在三角形网格上表示神经场的新框架，该框架在空间和频率域上都是多分辨率的。受神经傅里叶滤波器组（NFFB）的启发，我们的架构通过将更精细的空间分辨率级别与更高的频带相关联来分解空间和频率域，而将更粗糙的分辨率映射到较低的频率。为了实现几何感知的空间分解，我们利用了多个扩散网络组件，每个组件都与不同的空间分辨率级别相关联。随后，我们应用傅里叶特征映射来鼓励更精细的分辨率水平与更高的频率相关联。最终信号是使用正弦激活的MLP以小波激励的方式组成的，将高频信号聚集在低频信号之上。我们的架构在学习复杂神经场方面具有很高的精度，并且对目标场的不连续性、指数尺度变化和网格修改具有鲁棒性。我们通过将我们的方法应用于不同的神经领域，如合成RGB函数、UV纹理坐标和顶点法线，展示了其有效性，并说明了不同的挑战。为了验证我们的方法，我们将其性能与两种替代方案进行了比较，展示了我们的多分辨率架构的优势。 et.al.|[2409.03034](http://arxiv.org/abs/2409.03034)|null|
|**2024-09-03**|**GraspSplats: Efficient Manipulation with 3D Feature Splatting**|机器人对物体部件进行高效和零样本抓取的能力对于实际应用至关重要，并且随着视觉语言模型（VLM）的最新进展而变得普遍。为了弥合二维到三维表示的差距以支持这种能力，现有的方法依赖于神经场（NeRF），通过可微渲染或基于点的投影方法。然而，我们证明了NeRF由于其隐含性而不适合场景变化，并且基于点的方法对于没有基于渲染的优化的零件定位是不准确的。为了修正这些问题，我们提出了“把握辉煌”。使用深度监督和一种新的参考特征计算方法，GraspSplats在60秒内生成高质量的场景表示。我们进一步验证了基于高斯表示法的优势，表明GraspSplats中的显式和优化几何足以原生支持（1）实时抓取采样和（2）使用点跟踪器进行动态和铰接对象操作。通过在Franka机器人上进行的广泛实验，我们证明了在不同的任务设置下，GraspSplats的表现明显优于现有的方法。特别是，GraspSplats的性能优于基于NeRF的方法，如F3RM和LERF-TOGO，以及2D检测方法。 et.al.|[2409.02084](http://arxiv.org/abs/2409.02084)|null|

<p align=right>(<a href=#updated-on-20241003>back to top</a>)</p>

[contributors-shield]: https://img.shields.io/github/contributors/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[contributors-url]: https://github.com/Vincentqyw/cv-arxiv-daily/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[forks-url]: https://github.com/Vincentqyw/cv-arxiv-daily/network/members
[stars-shield]: https://img.shields.io/github/stars/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[stars-url]: https://github.com/Vincentqyw/cv-arxiv-daily/stargazers
[issues-shield]: https://img.shields.io/github/issues/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[issues-url]: https://github.com/Vincentqyw/cv-arxiv-daily/issues

