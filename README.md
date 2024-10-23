[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]

## Updated on 2024.10.23
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
|**2024-10-22**|**SpectroMotion: Dynamic 3D Reconstruction of Specular Scenes**|我们提出了SpectroMotion，这是一种将3D高斯散斑（3DGS）与基于物理的渲染（PBR）和变形场相结合的新方法，用于重建动态镜面场景。以前将3DGS扩展到动态场景建模的方法很难准确地表示镜面反射表面。我们的方法通过引入残差校正技术来解决这一局限性，该技术用于在变形过程中进行精确的表面法线计算，并辅以适应时变照明条件的可变形环境贴图。我们实施了一种从粗到细的训练策略，显著增强了场景几何和镜面颜色预测。我们证明，我们的模型在包含动态镜面对象的场景的视图合成方面优于现有的方法，并且它是唯一能够合成逼真的真实世界动态镜面场景的3DGS方法，在渲染复杂、动态和镜面场景方面优于最先进的方法。 et.al.|[2410.17249](http://arxiv.org/abs/2410.17249)|null|
|**2024-10-22**|**LVSM: A Large View Synthesis Model with Minimal 3D Inductive Bias**|我们提出了大视图合成模型（LVSM），这是一种基于变换器的新方法，用于从稀疏视图输入中进行可扩展和可推广的新视图合成。我们介绍了两种架构：（1）编码器-解码器LVSM，它将输入图像令牌编码为固定数量的1D潜在令牌，作为完全学习的场景表示，并从中解码出新的视图图像；以及（2）仅解码器LVSM，它直接将输入图像映射到新的视图输出，完全消除了中间场景表示。这两种模型都绕过了以前方法中使用的3D感应偏差——从3D表示（如NeRF、3DGS）到网络设计（如极线投影、平面扫描）——用完全数据驱动的方法解决了新颖的视图合成问题。虽然编码器-解码器模型由于其独立的潜在表示而提供了更快的推断，但仅解码器的LVSM实现了卓越的质量、可扩展性和零样本泛化，比以前最先进的方法高1.5至3.5 dB PSNR。对多个数据集的综合评估表明，这两种LVSM变体都达到了最先进的新颖视图合成质量。值得注意的是，即使计算资源减少（1-2个GPU），我们的模型也超越了所有以前的方法。请访问我们的网站了解更多详情：https://haian-jin.github.io/projects/LVSM/ . et.al.|[2410.17242](http://arxiv.org/abs/2410.17242)|null|
|**2024-10-22**|**VistaDream: Sampling multiview consistent images for single-view scene reconstruction**|本文中，我们提出了一种新的框架VistaDream，用于从单视图图像重建3D场景。最近的扩散模型能够从单个视图输入图像生成高质量的新颖视图图像。大多数现有的方法只专注于建立输入图像和生成图像之间的一致性，而失去了生成图像间的一致性。VistaDream通过两阶段管道解决了这个问题。在第一阶段，VistaDream从构建一个全局粗略的3D脚手架开始，通过缩小一小步来修复边界和估计深度图。然后，在这个全局支架上，我们使用基于迭代扩散的RGB-D修复来生成新的视图图像，以修复支架的孔。在第二阶段，我们通过一种新的无训练多视图一致性采样（MCS）进一步增强了生成的新视图图像之间的一致性，该MCS在扩散模型的反向采样过程中引入了多视图一致度约束。实验结果表明，在不训练或微调现有扩散模型的情况下，VistaDream仅使用单视图图像即可实现一致和高质量的新视图合成，并且远远优于基线方法。代码、视频和交互式演示可在以下网址获得https://vistadream-project-page.github.io/. et.al.|[2410.16892](http://arxiv.org/abs/2410.16892)|null|
|**2024-10-21**|**FrugalNeRF: Fast Convergence for Few-shot Novel View Synthesis without Learned Priors**|神经辐射场（NeRF）在少数拍摄场景中面临着重大挑战，主要是由于高保真渲染的过拟合和长训练时间。现有的方法，如FreeNeRF和SparseNeRF，使用频率正则化或预训练先验，但难以应对复杂的调度和偏差。我们介绍了FrugalNeRF，这是一种新颖的少镜头NeRF框架，它利用跨多个尺度的权重共享体素来有效地表示场景细节。我们的主要贡献是一种跨尺度几何自适应方案，该方案基于跨尺度的重投影误差来选择伪地面真值深度。这可以指导培训，而不依赖于外部学习的先验知识，从而充分利用培训数据。它还可以整合预先训练的先验，在不减缓收敛的情况下提高质量。在LLFF、DTU和RealEstate-10K上的实验表明，FrugalNeRF优于其他少镜头NeRF方法，同时显著减少了训练时间，使其成为高效准确的3D场景重建的实用解决方案。 et.al.|[2410.16271](http://arxiv.org/abs/2410.16271)|null|
|**2024-10-21**|**3DGS-Enhancer: Enhancing Unbounded 3D Gaussian Splatting with View-consistent 2D Diffusion Priors**|新颖的视图合成旨在从多个输入图像或视频中生成场景的新颖视图，最近的进步，如3D高斯飞溅（3DGS），在使用高效管道生成逼真的渲染方面取得了显著成功。然而，由于采样不足区域的信息不足，在稀疏输入视图等具有挑战性的设置下生成高质量的新颖视图仍然很困难，这通常会导致明显的伪影。本文介绍了一种用于提高3DGS表示质量的新型流水线3DGS增强器。我们利用2D视频扩散先验来解决具有挑战性的3D视图一致性问题，将其重新表述为在视频生成过程中实现时间一致性。3DGS增强器恢复渲染的新颖视图的视图一致性潜在特征，并通过时空解码器将其与输入视图集成。然后，增强的视图用于微调初始3DGS模型，显著提高其渲染性能。在无界场景的大规模数据集上进行的广泛实验表明，与最先进的方法相比，3DGS Enhancer具有更优的重建性能和高保真渲染结果。项目网页为https://xiliu8006.github.io/3DGS-Enhancer-project . et.al.|[2410.16266](http://arxiv.org/abs/2410.16266)|null|
|**2024-10-22**|**Fully Explicit Dynamic Gaussian Splatting**|3D高斯散斑通过利用密集的3D先验和显式表示，在静态场景中显示了快速高质量的渲染结果。不幸的是，先验和表示的好处并不涉及动态运动的新颖视图合成。具有讽刺意味的是，这是因为主要的障碍是对它们的依赖，这需要增加训练和渲染时间来解释动态运动。本文设计了一种显式4D高斯散斑（Ex4DGS）。我们的核心思想是在训练过程中首先分离静态和动态高斯分布，并在稀疏时间戳下明确采样动态高斯分布的位置和旋转。然后对采样的位置和旋转进行插值，以表示动态场景中对象在空间和时间上的连续运动，并降低计算成本。此外，我们引入了一种渐进式训练方案和一种点回溯技术，以提高Ex4DGS的收敛性。我们最初使用短时间戳训练Ex4DGS，并逐步扩展时间戳，这使得它在一些点云上运行良好。点回溯用于量化每个高斯函数随时间的累积误差，从而能够检测和去除动态场景中的错误高斯函数。在各种场景上的综合实验证明了我们的方法具有最先进的渲染质量，在单个2080Ti GPU上实现了62 fps的快速渲染。 et.al.|[2410.15629](http://arxiv.org/abs/2410.15629)|null|
|**2024-10-18**|**Learning autonomous driving from aerial imagery**|在这项工作中，我们考虑了仅从航拍图像中学习端到端感知以控制地面车辆的问题。摄影测量模拟器允许通过将预先生成的资产转换为新视图来合成新视图。然而，它们的设置成本很高，需要仔细收集数据，并且通常需要人工来创建可用的模拟器。我们使用神经辐射场（NeRF）作为中间表示，从地面车辆的角度合成新的视图。然后，这些新颖的观点可用于几个下游的自主导航应用。在这项工作中，我们通过应用从图像和深度数据中训练端到端学习策略，展示了新颖视图合成的实用性。在传统的真实到模拟到真实的框架中，收集的数据将被转换为视觉模拟器，然后可用于生成新的视图。相比之下，使用NeRF可以实现紧凑的表示，并能够在环境中收集更多数据时优化视觉模拟器的参数。我们通过在机器人汽车上部署模仿策略，证明了我们的方法在定制的迷你城市环境中的有效性。我们还考虑了位置定位的任务，并证明我们的方法能够在现实世界中重新定位汽车。 et.al.|[2410.14177](http://arxiv.org/abs/2410.14177)|null|
|**2024-10-18**|**DaRePlane: Direction-aware Representations for Dynamic Scene Reconstruction**|最近许多建模和重新渲染动态场景的方法都利用了基于平面的显式表示，解决了与神经辐射场（NeRF）和高斯飞溅（GS）等模型相关的训练时间慢的问题。然而，仅仅将4D动态场景分解为多个基于2D平面的表示不足以对具有复杂运动的场景进行高保真度重渲染。作为回应，我们提出了DaRePlane，这是一种新的方向感知表示方法，可以从六个不同的方向捕获场景动态。这种学习表示经过逆双树复小波变换（DTCWT）以恢复基于平面的信息。在NeRF管道中，DaRePlane通过融合来自这些恢复平面的向量来计算每个时空点的特征，然后传递给一个微小的MLP进行颜色回归。当应用于高斯飞溅时，DaRePlane计算高斯点的特征，然后使用微小的多头MLP进行时空变形预测。值得注意的是，为了解决六个实数和六个虚数方向感知小波系数引入的冗余问题，我们引入了一种可训练的掩蔽方法，在不显著降低性能的情况下缓解了存储问题。为了证明DaRePlane的通用性和效率，我们在常规和手术动态场景下对NeRF和GS系统进行了测试。大量实验表明，DaRePlane在各种复杂动态场景的新颖视图合成中具有最先进的性能。 et.al.|[2410.14169](http://arxiv.org/abs/2410.14169)|null|
|**2024-10-17**|**DepthSplat: Connecting Gaussian Splatting and Depth**|高斯散射和单/多视图深度估计通常是单独研究的。本文中，我们提出了DepthSplat来连接高斯溅射和深度估计，并研究了它们之间的相互作用。更具体地说，我们首先通过利用预先训练的单眼深度特征来贡献一个稳健的多视图深度模型，从而得到高质量的前馈3D高斯飞溅重建。我们还表明，高斯飞溅可以作为一种无监督的预训练目标，用于从大规模未标记的数据集中学习强大的深度模型。我们通过广泛的消融和跨任务转移实验验证了高斯溅射和深度估计之间的协同作用。我们的DepthSplat在ScanNet、RealEstate10K和DL3DV数据集上实现了深度估计和新颖视图合成方面的最先进性能，展示了连接这两个任务的互惠互利。我们的代码、模型和视频结果可在https://haofeixu.github.io/depthsplat/. et.al.|[2410.13862](http://arxiv.org/abs/2410.13862)|**[link](https://github.com/cvg/depthsplat)**|
|**2024-10-17**|**Hybrid bundle-adjusting 3D Gaussians for view consistent rendering with pose optimization**|新型视图合成在3D计算机视觉领域取得了重大进展。然而，从不完美的相机姿态渲染视图一致的新颖视图仍然具有挑战性。本文介绍了一种混合束调整3D高斯模型，该模型能够实现具有姿态优化的视图一致性渲染。该模型联合提取基于图像和神经的3D表示，以在面向前方的场景中同时生成视图一致的图像和相机姿态。我们的模型的有效性通过在真实和合成数据集上进行的广泛实验得到了证明。这些实验清楚地表明，我们的模型可以有效地优化神经场景表示，同时解决明显的相机姿态失准问题。源代码可在https://github.com/Bistu3DV/hybridBA. et.al.|[2410.13280](http://arxiv.org/abs/2410.13280)|**[link](https://github.com/bistu3dv/hybridba)**|

<p align=right>(<a href=#updated-on-20241023>back to top</a>)</p>

## 3D Reconstruction

|Publish Date|Title|Abstract|PDF|Code|
|---|---|---|---|---|
|**2024-10-22**|**SpectroMotion: Dynamic 3D Reconstruction of Specular Scenes**|我们提出了SpectroMotion，这是一种将3D高斯散斑（3DGS）与基于物理的渲染（PBR）和变形场相结合的新方法，用于重建动态镜面场景。以前将3DGS扩展到动态场景建模的方法很难准确地表示镜面反射表面。我们的方法通过引入残差校正技术来解决这一局限性，该技术用于在变形过程中进行精确的表面法线计算，并辅以适应时变照明条件的可变形环境贴图。我们实施了一种从粗到细的训练策略，显著增强了场景几何和镜面颜色预测。我们证明，我们的模型在包含动态镜面对象的场景的视图合成方面优于现有的方法，并且它是唯一能够合成逼真的真实世界动态镜面场景的3DGS方法，在渲染复杂、动态和镜面场景方面优于最先进的方法。 et.al.|[2410.17249](http://arxiv.org/abs/2410.17249)|null|
|**2024-10-22**|**E-3DGS: Gaussian Splatting with Exposure and Motion Events**|从最佳条件下捕获的图像中估计神经辐射场（NeRF）在视觉界得到了广泛的探索。然而，机器人应用经常面临运动模糊、照明不足和计算开销高等挑战，这些挑战对导航、检查和场景可视化等下游任务产生了不利影响。为了应对这些挑战，我们提出了E-3DGS，这是一种基于事件的新方法，将事件划分为运动（来自相机或物体运动）和曝光（来自相机曝光），使用前者来处理快速运动的场景，使用后者来重建灰度图像，以进行基于事件的3D高斯散斑（3DGS）的高质量训练和优化。我们介绍了一种将3DGS与曝光事件相结合的新方法，用于高质量重建显式场景表示。我们的多功能框架可以单独操作运动事件进行3D重建，使用曝光事件提高质量，或者采用混合模式，通过优化初始曝光事件和高速运动事件来平衡质量和有效性。我们还介绍了EME-3D，这是一个真实世界的3D数据集，包含曝光事件、运动事件、相机校准参数和稀疏点云。我们的方法比基于事件的NeRF更快，重建质量更好，同时比使用单个事件传感器组合事件和RGB数据的NeRF方法更具成本效益。通过结合运动和曝光事件，E-3DGS为基于事件的3D重建设定了新的基准，在具有挑战性的条件下和较低的硬件需求下具有强大的性能。源代码和数据集将在https://github.com/MasterHow/E-3DGS. et.al.|[2410.16995](http://arxiv.org/abs/2410.16995)|null|
|**2024-10-21**|**MvDrag3D: Drag-based Creative 3D Editing via Multi-view Generation-Reconstruction Priors**|在图像生成模型的推动下，基于拖动的编辑在2D内容创建中变得流行起来。然而，将这项技术扩展到3D仍然是一个挑战。现有的基于3D拖动的编辑方法，无论是采用显式空间变换还是依赖于有限容量3D生成模型中的隐式潜在优化，在处理重大拓扑变化或跨不同对象类别生成新纹理方面都存在不足。为了克服这些局限性，我们引入了MVDrag3D，这是一种利用多视图生成和重建先验进行更灵活、更有创意的基于拖动的3D编辑的新框架。我们方法的核心是使用多视图扩散模型作为强生成模型，然后在多个渲染视图上执行一致的拖动编辑，接着是重建模型，重建编辑对象的3D高斯分布。虽然初始的3D高斯分布可能会在不同视图之间出现错位，但我们通过视图特定的变形网络来解决这个问题，该网络可以调整高斯分布的位置以使其很好地对齐。此外，我们提出了一种多视图评分函数，从多个视图中提取生成先验，以进一步提高视图的一致性和视觉质量。大量实验表明，MVDrag3D为基于3D拖动的编辑提供了一种精确、生成和灵活的解决方案，支持各种对象类别和3D表示的更通用的编辑效果。 et.al.|[2410.16272](http://arxiv.org/abs/2410.16272)|null|
|**2024-10-22**|**LucidFusion: Generating 3D Gaussians with Arbitrary Unposed Images**|最近的大型重建模型在从单个图像生成高质量3D对象方面取得了显著进展。然而，这些方法往往难以控制，因为它们缺乏来自多个视图的信息，导致不完整或不一致的3D重建。为了解决这一局限性，我们引入了LucidFusion，这是一种灵活的端到端前馈框架，利用了相对坐标图（RCM）。与传统的通过姿势将图像与3D世界联系起来的方法不同，LucidFusion利用RCM在不同的视图中连贯地对齐几何特征，使其高度适用于从任意、未经处理的图像生成3D。此外，LucidFusion与原始的单图像到3D流水线无缝集成，以512美元乘以512美元的分辨率生成详细的3D高斯分布，使其非常适合广泛的应用。 et.al.|[2410.15636](http://arxiv.org/abs/2410.15636)|null|
|**2024-10-19**|**EndoMetric: Near-light metric scale monocular SLAM**|近年来，内窥镜图像的几何重建和SLAM取得了重大进展。在大多数医学专业中，使用的内窥镜是单眼的，所应用的算法通常是为外部环境设计的算法的扩展，从而产生高达未知比例因子的3D重建。在这篇论文中，我们利用了这样一个事实，即标准内窥镜配备了近光源，这些近光源位于距离相机较小但非零的基线处。通过利用光衰减的平方反比定律，我们首次实现了具有精确度量尺度的单眼重建。这为将任何内窥镜转换为公制设备铺平了道路，这对于测量息肉、狭窄或受疾病影响的组织范围等实际应用至关重要。 et.al.|[2410.15065](http://arxiv.org/abs/2410.15065)|null|
|**2024-10-17**|**Object Pose Estimation Using Implicit Representation For Transparent Objects**|物体姿态估计是计算机视觉中的一项重要任务。物体姿态给出了物体在现实空间中的方向和平移，这允许各种应用，如操纵、增强现实等。各种物体对光表现出不同的特性，如反射、吸收等。这使得理解物体在RGB和深度通道中的结构具有挑战性。最近的研究一直在向基于学习的方法发展，这些方法利用深度学习为对象姿态估计提供了一种更灵活、更通用的方法。一种这样的方法是渲染和比较方法，该方法从多个视图渲染对象并将其与给定的2D图像进行比较，这通常需要CAD模型形式的对象表示。我们认为CAD模型的合成纹理可能不适合渲染和比较操作。我们发现，如果对象以神经辐射场（NeRF）的形式表示为隐式（神经）表示，它会对实际场景进行更逼真的渲染，并保留关键的空间特征，这使得比较更加通用。我们在透明数据集上评估了渲染和比较方法的NeRF实现，发现它超过了当前最先进的结果。 et.al.|[2410.13465](http://arxiv.org/abs/2410.13465)|null|
|**2024-10-18**|**Context-Enhanced Multi-View Trajectory Representation Learning: Bridging the Gap through Self-Supervised Models**|使用通用密集表示对轨迹数据进行建模已成为各种下游应用的流行范式，如轨迹分类、行程时间估计和相似性计算。然而，现有的方法通常依赖于单一空间视图的轨迹，限制了它们捕获丰富上下文信息的能力，而丰富上下文信息对于深入了解不同地理空间背景下的运动模式至关重要。为此，我们提出了MVTraj，这是一种用于轨迹表示学习的新型多视图建模方法。MVTraj整合了从GPS到道路网络和兴趣点的各种背景知识，以更全面地了解轨迹数据。为了在多个视图之间对齐学习过程，我们利用GPS轨迹作为桥梁，并采用自我监督的借口任务来捕捉和区分不同空间视图之间的运动模式。在此之后，我们将来自不同视角的轨迹视为不同的模态，并应用分层跨模态交互模块来融合表示，从而丰富了从多个来源获得的知识。对真实世界数据集的广泛实验表明，MVTraj在与各种空间视图相关的任务中明显优于现有基线，验证了其在时空建模中的有效性和实用性。 et.al.|[2410.13196](http://arxiv.org/abs/2410.13196)|null|
|**2024-10-18**|**UniG: Modelling Unitary 3D Gaussians for View-consistent 3D Reconstruction**|在这项工作中，我们提出了UniG，这是一种视图一致的3D重建和新颖的视图合成模型，可以从稀疏图像中生成3D高斯的高保真表示。现有的基于3D高斯的方法通常对每个视图的每个像素进行高斯回归，分别为每个视图创建3D高斯，并通过点连接将其合并。这种与视图无关的重建方法通常会导致视图不一致问题，其中来自不同视图的同一3D点的预测位置可能存在差异。为了解决这个问题，我们开发了一个类似DETR（DEtect TRansformer）的框架，该框架将3D高斯视为解码器查询，并通过在多个输入图像上执行多视图交叉注意（MVDFA）来逐层更新其参数。通过这种方式，多个视图自然有助于对3D高斯的统一表示进行建模，从而使3D重建更加视图一致。此外，由于用作解码器查询的3D高斯数与输入视图的数量无关，因此允许任意数量的输入图像，而不会导致内存爆炸。大量的实验验证了我们的方法的优势，在定量和定性上展示了优于现有方法的性能（在Objaverse上训练并在GSO基准上测试时，PSNR提高了4.2 dB）。该代码将于https://github.com/jwubz123/UNIG. et.al.|[2410.13195](http://arxiv.org/abs/2410.13195)|**[link](https://github.com/jwubz123/UNIG)**|
|**2024-10-16**|**Configurable Embodied Data Generation for Class-Agnostic RGB-D Video Segmentation**|本文提出了一种生成大规模数据集的方法，以改善不同形状因子的机器人之间的类无关视频分割。具体来说，我们考虑的问题是，如果在数据生成过程中考虑了机器人的实施方式，那么在通用分割数据上训练的视频分割模型是否对特定的机器人平台更有效。为了回答这个问题，制定了一个管道，用于使用3D重建（例如来自HM3DSem）生成分段视频，这些视频可以根据机器人的实施例（例如传感器类型、传感器放置和照明源）进行配置。由此产生的大量RGB-D视频全景分割数据集（MVPd）被引入，用于与基础和视频分割模型进行广泛的基准测试，并支持视频分割中以实施例为重点的研究。我们的实验结果表明，在将基础模型转移到某些机器人实施例（如特定的相机放置）时，使用MVPd进行微调可以提高性能。这些实验还表明，使用3D模态（深度图像和相机姿态）可以提高视频分割的准确性和一致性。项目网页可在https://topipari.com/projects/MVPd et.al.|[2410.12995](http://arxiv.org/abs/2410.12995)|null|
|**2024-10-16**|**Cascade learning in multi-task encoder-decoder networks for concurrent bone segmentation and glenohumeral joint assessment in shoulder CT scans**|骨关节炎是一种影响骨骼和软骨的退行性疾病，通常导致骨赘形成、骨密度降低和关节间隙狭窄。恢复正常关节功能的治疗方案因病情的严重程度而异。这项工作引入了一种处理肩部CT扫描的创新深度学习框架。它具有肱骨近端和肩胛骨的语义分割、骨表面的3D重建、肩关节（GH）关节区域的识别以及三种常见骨关节炎相关病理的分期：骨赘形成（OS）、GH间隙缩小（JS）和肱骨肩胛骨对齐（HSA）。该流水线包括两个级联的CNN架构：用于分割的3D CEL-UNet和用于三重分类的3D Arthro-Net。使用571次CT扫描的回顾性数据集，对患有不同程度GH骨关节炎相关疾病的患者进行训练、验证和测试。肱骨三维重建的均方根误差和豪斯多夫距离中值分别为0.22mm和1.48mm，肩胛骨为0.24mm和1.48mm。其性能优于最先进的架构，可能适用于基于PSI的肩关节置换术前计划。OS、JS和HSA在所有三个类别中的分类准确率始终达到90%左右。推理管道的计算时间不到15秒，展示了该框架的效率和与骨科放射学实践的兼容性。这些结果代表了人工智能工具在医学翻译方面的一个有前景的进步。这一进展旨在简化术前计划流程，提供高质量的骨表面，并支持外科医生根据独特的患者关节状况选择最合适的手术方法。 et.al.|[2410.12641](http://arxiv.org/abs/2410.12641)|null|

<p align=right>(<a href=#updated-on-20241023>back to top</a>)</p>

## Diffusion

|Publish Date|Title|Abstract|PDF|Code|
|---|---|---|---|---|
|**2024-10-22**|**Ergodic Risk Sensitive Control of Markovian Multiclass Many-Server Queues with Abandonment**|我们研究了在Halfin-Whitt机制下，在长期平均（遍历）风险敏感成本准则下，具有放弃的马尔可夫多类排队网络的最优调度问题。目的是证明由极限扩散的遍历风险敏感控制（ERSC）问题引起的最优控制的渐近最优性。特别地，我们证明了与扩散尺度排队过程相关的最优ERSC值在渐近状态下收敛到极限扩散的值。ERSC带来的挑战是，与通常的长期平均（遍历）成本不同，人们不能将ERSC成本表示为对与排队过程相关的平均经验度量的期望。我们通过利用极限扩散和泊松驱动排队动力学的变分表示来开发一种新方法，这两种方法都涉及某些辅助控制。扩散缩放排队过程和限制扩散的ERSC成本可以表示为使用这些辅助控制的与相应扩展过程相关的平均经验度量上的扩展运行成本的积分。对于下界证明，我们利用了极限扩散的ERSC问题与两人零和随机微分博弈的联系。我们还利用了与扩展极限扩散和具有辅助控制的扩散标度过程相关的平均经验度量。下限和上限证明中的一个主要技术挑战是确定上述扩展过程的平均经验度量的严密性。我们在这两种情况下都适当地确定了接近最优的控制，从而可以使用极限扩散和扩散缩放排队过程的现有遍历性。 et.al.|[2410.17205](http://arxiv.org/abs/2410.17205)|null|
|**2024-10-22**|**Reinforcement learning on structure-conditioned categorical diffusion for protein inverse folding**|蛋白质反向折叠，即预测将折叠成所需3D结构的氨基酸序列，是基于结构的蛋白质设计的一个重要问题。基于机器学习的逆折叠方法通常使用恢复原始序列作为优化目标。然而，逆折叠是一个一对多的问题，其中几个序列可以折叠成相同的结构。此外，对于许多实际应用，通常希望有多个不同的序列折叠到目标结构中，因为它允许更多的候选序列用于下游优化。在这里，我们证明，尽管最近的逆折叠方法显示出序列恢复率的提高，但它们的“可折叠多样性”——即它们生成多个非相似序列的能力，这些序列折叠成与目标一致的结构——并没有提高。为了解决这个问题，我们提出了RL-DIF，这是一种用于逆折叠的分类扩散模型，在序列恢复方面进行了预训练，并通过结构一致性的强化学习进行了调整。我们发现RL-DIF实现了与基准模型相当的序列恢复和结构一致性，但显示出更大的可折叠多样性：实验表明，RL-DIF在CATH 4.2上可以实现29%的可折叠多样化，而在相同数据集上训练的模型则为23%。PyTorch模型权重和采样代码可以在GitHub上找到。 et.al.|[2410.17173](http://arxiv.org/abs/2410.17173)|null|
|**2024-10-22**|**On Lyapunov Conditions for the Well-Posedness of McKean-Vlasov Stochastic Differential Delay Equations**|这项工作的重点是McKean-Vlasov随机微分延迟方程的适定性。在漂移和扩散项的适当lipschitz条件下，以及分布相关的李雅普诺夫条件下，本文证明了分布相关随机微分延迟方程唯一解的存在性。 et.al.|[2410.17120](http://arxiv.org/abs/2410.17120)|null|
|**2024-10-22**|**Dust ring and gap formation by gas flow induced by low-mass planets embedded in protoplanetary disks $\rm II$. Time-dependent model**|观测到的尘埃环和原行星盘中的间隙可能是形成行星的印记。即使是地球质量为1到10的低质量行星，尚未形成深气隙，也可以通过驱动径向向外的气流来产生这样的尘埃环和间隙，如先前的工作所示。然而，由于尘埃漂移和扩散，理解这些尘埃结构的产生和演化是具有挑战性的，需要一种超越先前稳态模型的方法。在这里，我们基于后处理三维流体动力学模拟，研究了受行星诱导气流影响的尘埃表面密度的时间演化。我们发现，大于无量纲热质量$m=0.05$的行星，对应于1 au时的0.3个地球质量或10 au时的1.7个地球质量，会产生尘埃环和间隙，前提是固体具有较小的斯托克斯数}（${rm St}\lesssim10^{-2}$），并且圆盘中平面是弱湍流的（$\alpha_{rm diff}\lesssim10^{-4}$）。当尘埃颗粒堆积在行星轨道外时，当平流通量主导扩散时，内部间隙会随着时间的推移而扩大。尘埃间隙深度的范围从几倍到几个数量级不等，取决于行星质量和中平面粒子扩散的水平。我们构建了一个描述尘埃环和间隙宽度的半解析模型，然后将其与观测数据进行了比较。我们发现，假设$\alpha_{\rm diff}=10^{-5}$和$\rm St}=10^{-3}$，高达65%的观测到的宽轨道间隙可以解释为低质量行星的存在。然而，解释观测到的宽环更具挑战性，在我们的模型中，这需要存在一群小粒子（${rm St=10^{-4}$ ）。需要进一步的工作来探索卵石碎裂、行星迁移和多行星效应的作用。 et.al.|[2410.16996](http://arxiv.org/abs/2410.16996)|null|
|**2024-10-22**|**DiP-GO: A Diffusion Pruner via Few-step Gradient Optimization**|扩散模型因其出色的性能在图像生成领域取得了显著进展。然而，由于推理过程中的多步去噪过程，这些模型需要大量的计算资源。虽然传统的修剪方法被用来优化这些模型，但再训练过程需要大规模的训练数据集和大量的计算成本来保持泛化能力，这既不方便也不高效。最近的研究试图利用相邻去噪阶段特征的相似性，通过简单和静态的策略来降低计算成本。然而，这些策略无法充分利用相邻时间步中相似特征模式的潜力。在这项工作中，我们提出了一种新的剪枝方法，该方法通过一个更智能、更可微分的剪枝器推导出一个有效的扩散模型。我们方法的核心是将模型修剪过程转换为子网搜索过程。具体来说，我们首先通过添加一些基于类似功能构建的备份连接，引入了一个基于标准扩散的SuperNet。然后，我们构建了一个插件修剪器网络，并设计了优化损失来识别冗余计算。最后，我们的方法可以通过几步梯度优化和简单的后处理过程来识别最优的子网。我们对各种扩散模型进行了广泛的实验，包括稳定扩散系列和DiTs。我们的DiP-GO方法在SD-1.5上实现了4.4倍的加速，而没有任何精度损失，明显优于之前最先进的方法。 et.al.|[2410.16942](http://arxiv.org/abs/2410.16942)|null|
|**2024-10-22**|**Hierarchical Clustering for Conditional Diffusion in Image Generation**|找到具有相似特征的数据点集群并生成新的集群特定样本可以显著增强我们对复杂数据分布的理解。虽然使用变分自编码器对聚类进行了广泛的探索，但这些模型在现实世界的数据集中往往缺乏生成质量。本文通过引入TreeDiffusion来解决这一差距，TreeDiffusion是一种深度生成模型，它将扩散模型置于分层集群上，以获得高质量的、特定于集群的世代。所提出的管道由两个步骤组成：一个基于VAE的聚类模型，学习数据的层次结构；一个条件扩散模型，为每个聚类生成逼真的图像。我们提出了这个两阶段过程，以确保生成的样本保持其各自簇的代表性，并将图像保真度提高到扩散模型的水平。我们的方法的一个关键优势是它能够为每个聚类创建图像，通过聚类模型提供更好的学习表示可视化，如定性结果所示。该方法有效地解决了基于VAE的方法的生成局限性，同时保持了它们的聚类性能。从经验上讲，我们证明，在层次聚类上条件化扩散模型显著提高了生成性能，从而改善了生成聚类模型的状态。 et.al.|[2410.16910](http://arxiv.org/abs/2410.16910)|null|
|**2024-10-22**|**MBD: Multi b-value Denoising of Diffusion Magnetic Resonance Images**|我们提出了一种使用卷积神经网络对扩散磁共振图像（dMRI）进行去噪的新方法，该方法利用在多个b值处获取的数据的优点来抵消对许多冗余观测的需求。去噪在dMRI中尤其重要，因为噪声会对量化精度和图像预处理产生有害影响。迄今为止提出的最成功的方法，如Marchenko Pastur主成分分析（MPPCA）去噪，是针对许多编码方向重复的扩散加权而量身定制的。他们利用了数据集的高冗余性，对扩散编码方向空间进行过采样，因为许多方向都有共线分量。然而，有许多dMRI技术不需要大量的编码方向或重复，因此不太适合这种方法。例如，临床dMRI检查可能只包括三个编码方向，各个方向的数据冗余很低或可以忽略不计。此外，有前景的新dMRI方法，如球形b张量编码（STE），受益于高b值，同时使信号在单次拍摄中沿所有方向扩散。我们介绍了一种卷积神经网络方法，我们称之为基于多b值的去噪（MBD）。MBD利用了不同b值但沿相同扩散编码方向的扩散加权图像（DWI）的相似性。它允许对具有高噪声方差的扩散图像进行去噪，同时避免模糊，并且只使用少量输入图像。 et.al.|[2410.16898](http://arxiv.org/abs/2410.16898)|null|
|**2024-10-22**|**VistaDream: Sampling multiview consistent images for single-view scene reconstruction**|本文中，我们提出了一种新的框架VistaDream，用于从单视图图像重建3D场景。最近的扩散模型能够从单个视图输入图像生成高质量的新颖视图图像。大多数现有的方法只专注于建立输入图像和生成图像之间的一致性，而失去了生成图像间的一致性。VistaDream通过两阶段管道解决了这个问题。在第一阶段，VistaDream从构建一个全局粗略的3D脚手架开始，通过缩小一小步来修复边界和估计深度图。然后，在这个全局支架上，我们使用基于迭代扩散的RGB-D修复来生成新的视图图像，以修复支架的孔。在第二阶段，我们通过一种新的无训练多视图一致性采样（MCS）进一步增强了生成的新视图图像之间的一致性，该MCS在扩散模型的反向采样过程中引入了多视图一致度约束。实验结果表明，在不训练或微调现有扩散模型的情况下，VistaDream仅使用单视图图像即可实现一致和高质量的新视图合成，并且远远优于基线方法。代码、视频和交互式演示可在以下网址获得https://vistadream-project-page.github.io/. et.al.|[2410.16892](http://arxiv.org/abs/2410.16892)|null|
|**2024-10-22**|**Inverse first-passage problems of a diffusion with resetting**|我们从初始位置 $\mathcal X（0）=\eta开始，解决了具有随机重置的一维扩散过程$\mathal X（t）$的第一个通过位置和第一个通过时间的逆问题这种类型的扩散$\mathcal X（t）$的特征是，根据速率$R>0的齐次泊松过程，可以重置到位置$X_R$。关于逆第一通道位置问题，对于随机$\eta\in（0，b），\b<+\infty$（以及固定的$R$和$X_R\in（O，b））$，让$\tau_{0，b}$是$\mathal X（t 0，b}）=0）$从$（0，b）左端退出的概率；$给定概率$q\in（0,1），$逆第一通道位置问题在于找到$\eta，$的密度$g$（如果存在），使得$\pi_0=q$关于逆第一通道时间问题，对于随机$\eta\in（0，+\infty）$（固定$r$和$x_r>0）$，设$\tau$为$\mathcal x（t）$通过零的第一通道时间；对于正实轴上的给定分布函数$F（t）$，逆首次通过时间问题在于找到$\eta，$的密度$g$（如果存在），使得$P（\tau \le t）=F（t，\t＞0。$除了随机初始位置$\eta$的情况外，$我们还研究了初始位置$\eta$和重置率$r$固定，而重置位置$x_r$ 是随机的情况。对于所考虑的所有类型的逆问题，报告了几个显式的解的例子。 et.al.|[2410.16889](http://arxiv.org/abs/2410.16889)|null|
|**2024-10-22**|**Accelerated Quantum Circuit Monte-Carlo Simulation for Heavy Quark Thermalization**|夸克胶子等离子体（QGP）中的重夸克热化是理解强相互作用最有前景的现象之一，其中它们在低动量下的能量损失和动量加宽可以用具有阻力和扩散项的随机过程很好地描述。我们提出了一种加速量子电路蒙特卡罗（aQCMC）框架，该框架利用量子振幅估计（QAE）算法以较少的二次资源模拟重夸克热化。具体来说，我们使用理想的量子模拟器模拟了重夸克在1D和2D以及各向同性和各向异性介质中的热化，并将其与分析热预期进行了比较。 et.al.|[2410.16863](http://arxiv.org/abs/2410.16863)|null|

<p align=right>(<a href=#updated-on-20241023>back to top</a>)</p>

## NeRF

|Publish Date|Title|Abstract|PDF|Code|
|---|---|---|---|---|
|**2024-10-22**|**Cortical Dynamics of Neural-Connectivity Fields**|皮质组织的宏观研究揭示了振荡活动的普遍性，这反映了神经相互作用的微调。本研究通过将广义振荡动力学纳入先前关于保守或半保守神经场动力学的工作中，扩展了神经场理论。先前的研究在很大程度上假设了神经单元之间的各向同性连接；然而，这项研究表明，广泛的各向异性和波动连接仍然可以维持振荡。使用拉格朗日场方法，我们研究了不同类型的连接、它们的动力学以及与神经场的潜在相互作用。基于这一理论基础，我们推导出了一个框架，该框架通过连接场的概念将Hebbian和非Hebbian学习（即可塑性）纳入神经场的研究中。 et.al.|[2410.16852](http://arxiv.org/abs/2410.16852)|null|
|**2024-10-15**|**Deep vectorised operators for pulsatile hemodynamics estimation in coronary arteries from a steady-state prior**|心血管血流动力学场为冠状动脉疾病提供了有价值的医学决策标志。计算流体动力学（CFD）是体内准确、无创评估这些量的金标准。在这项工作中，我们提出了一种基于机器学习的时间高效替代模型，用于基于稳态先验估计脉动血流动力学。我们引入了深度矢量化算子，这是一种用于在无限维函数空间上进行离散化独立学习的建模框架。基础神经结构是一个以血流动力学边界条件为条件的神经场。重要的是，我们展示了如何将逐点动作的要求放宽到置换等变，从而产生一系列可以通过消息传递和自我关注层进行参数化的模型。我们在从冠状动脉计算机断层扫描血管造影（CCTA）中提取的74条狭窄冠状动脉的数据集上评估了我们的方法，并将患者特异性脉动CFD模拟作为基本事实。我们证明，我们的模型能够准确估计脉动速度和压力，同时不受源域重新采样的影响（离散化独立性）。这表明，深度矢量化算子是冠状动脉及其他动脉心血管血流动力学估计的强大建模工具。 et.al.|[2410.11920](http://arxiv.org/abs/2410.11920)|null|
|**2024-10-07**|**Fast Training of Sinusoidal Neural Fields via Scaling Initialization**|神经场是一种新兴的范式，它将数据表示为由神经网络参数化的连续函数。尽管有许多优点，但神经场通常具有较高的训练成本，这阻碍了更广泛的采用。在本文中，我们关注一个流行的神经场家族，称为正弦神经场（SNF），并研究如何初始化它以最大限度地提高训练速度。我们发现，基于信号传播原理设计的SNF标准初始化方案是次优的。特别是，我们证明，通过简单地将每个权重（最后一层除外）乘以一个常数，我们可以将SNF训练加速10 $\times$。这种方法被称为$\textit{weight scaling}$ ，在各种数据域上持续提供显著的加速，使SNF的训练速度比最近提出的架构更快。为了理解为什么权重缩放效果良好，我们进行了广泛的理论和实证分析，结果表明，权重缩放不仅有效地解决了频谱偏差，而且具有良好的优化轨迹。 et.al.|[2410.04779](http://arxiv.org/abs/2410.04779)|null|
|**2024-10-04**|**End-to-End Reaction Field Energy Modeling via Deep Learning based Voxel-to-voxel Transform**|在计算生物化学和生物物理学中，理解静电相互作用的作用对于阐明生物分子的结构、动力学和功能至关重要。泊松-玻尔兹曼（PB）方程是通过描述带电分子内部和周围的静电势来模拟这些相互作用的基础工具。然而，由于生物分子表面的复杂性和需要考虑可移动离子，求解PB方程带来了重大的计算挑战。虽然求解PB方程的传统数值方法是准确的，但它们的计算成本很高，并且随着系统规模的增加而扩展性较差。为了应对这些挑战，我们引入了PBNeF，这是一种新的机器学习方法，灵感来自基于神经网络的偏微分方程求解器的最新进展。我们的方法将PB方程的输入和边界静电条件转化为可学习的体素表示，使神经场变换器能够预测PB解，进而预测反应场势能。大量实验表明，与传统的PB求解器相比，PBNeF的速度提高了100倍以上，同时保持了与广义玻恩（GB）模型相当的精度。 et.al.|[2410.03927](http://arxiv.org/abs/2410.03927)|null|
|**2024-10-08**|**DressRecon: Freeform 4D Human Reconstruction from Monocular Video**|我们提出了一种从单目视频中重建时间一致的人体模型的方法，重点是极其宽松的衣服或手持物体的交互。之前在人体重建方面的工作要么局限于没有物体交互的紧身衣服，要么需要校准的多视图捕捉或个性化的模板扫描，而大规模收集这些数据成本很高。我们对高质量但灵活的重建的关键见解是，将关于关节体形状的通用人类先验（从大规模训练数据中学习）与视频特定的关节“骨骼袋”变形（通过测试时间优化适合单个视频）仔细结合。我们通过学习一个神经隐式模型来实现这一点，该模型将身体和衣服的变形作为单独的运动模型层来解开。为了捕捉服装的微妙几何形状，我们在优化过程中利用了基于图像的先验，如人体姿势、表面法线和光流。由此产生的神经场可以提取到时间一致的网格中，或进一步优化为显式3D高斯分布，以实现高保真交互式渲染。在具有高度挑战性的服装变形和物体交互的数据集上，DressReston可以产生比现有技术更高保真的3D重建。项目页面：https://jefftan969.github.io/dressrecon/ et.al.|[2409.20563](http://arxiv.org/abs/2409.20563)|null|
|**2024-09-25**|**TalkinNeRF: Animatable Neural Fields for Full-Body Talking Humans**|我们介绍了一种新的框架，该框架从单眼视频中学习全身说话的人的动态神经辐射场（NeRF）。之前的工作只代表身体姿势或面部。然而，人类通过全身进行交流，结合身体姿势、手势和面部表情。在这项工作中，我们提出了TalkinNeRF，这是一个基于NeRF的统一网络，代表了整体4D人体运动。给定一个受试者的单眼视频，我们学习身体、面部和手的相应模块，这些模块结合在一起生成最终结果。为了捕捉复杂的手指关节，我们学习了手的额外变形场。我们的多身份表示能够同时训练多个科目，以及在完全看不见的姿势下进行强大的动画。只要输入一段短视频，它也可以推广到新的身份。我们展示了最先进的性能，用于为全身说话的人类制作动画，具有精细的手部发音和面部表情。 et.al.|[2409.16666](http://arxiv.org/abs/2409.16666)|null|
|**2024-09-24**|**Generative 3D Cardiac Shape Modelling for In-Silico Trials**|我们提出了一种深度学习方法，基于将形状表示为神经有符号距离场的零级集，对合成主动脉形状进行建模和生成，该方法受一系列可训练的嵌入向量的约束，并对每个形状的几何特征进行编码。通过使神经场在采样表面点上消失并强制其空间梯度具有单位范数，在从CT图像重建的主动脉根部网格数据集上训练网络。实证结果表明，我们的模型可以高保真地表示主动脉形状。此外，通过从学习到的嵌入向量中采样，我们可以生成类似于真实患者解剖结构的新形状，可用于计算机模拟试验。 et.al.|[2409.16058](http://arxiv.org/abs/2409.16058)|null|
|**2024-09-21**|**MOSE: Monocular Semantic Reconstruction Using NeRF-Lifted Noisy Priors**|由于缺乏几何指导和不完美的视图相关2D先验，从单眼图像中精确重建密集和语义注释的3D网格仍然是一项具有挑战性的任务。尽管我们已经见证了隐式神经场景表示的最新进展，能够简单地从多视图图像中进行精确的2D渲染，但很少有研究仅使用单眼先验来解决3D场景理解问题。在本文中，我们提出了MOSE，这是一种神经场语义重建方法，可以将推断的图像级噪声先验提升到3D，在3D和2D空间中产生精确的语义和几何。我们方法的关键动机是利用通用类不可知的分段掩码作为指导，在训练过程中促进渲染语义的局部一致性。在语义的帮助下，我们进一步将平滑正则化应用于无纹理区域，以获得更好的几何质量，从而实现几何和语义的互惠互利。在ScanNet数据集上的实验表明，我们的MOSE在3D语义分割、2D语义分割和3D表面重建任务的所有指标上都优于相关基线。 et.al.|[2409.14019](http://arxiv.org/abs/2409.14019)|null|
|**2024-09-17**|**SplatFields: Neural Gaussian Splats for Sparse 3D and 4D Reconstruction**|从多视图图像中数字化3D静态场景和4D动态事件长期以来一直是计算机视觉和图形学领域的一个挑战。最近，3D高斯散斑（3DGS）已经成为一种实用且可扩展的重建方法，由于其令人印象深刻的重建质量、实时渲染能力以及与广泛使用的可视化工具的兼容性而越来越受欢迎。然而，该方法需要大量的输入视图来实现高质量的场景重建，这引入了一个重大的实际瓶颈。在捕捉动态场景时，这一挑战尤为严峻，因为部署广泛的相机阵列的成本可能高得令人望而却步。在这项工作中，我们发现斑点特征缺乏空间自相关性是导致3DGS技术在稀疏重建环境中性能不佳的因素之一。为了解决这个问题，我们提出了一种优化策略，通过将splat特征建模为相应隐式神经场的输出，有效地正则化splat特征。这导致在各种场景中重建质量的一致提高。我们的方法有效地处理了静态和动态情况，这在不同设置和场景复杂性的广泛测试中得到了证明。 et.al.|[2409.11211](http://arxiv.org/abs/2409.11211)|null|
|**2024-10-02**|**Neural Fields for Adaptive Photoacoustic Computed Tomography**|光声计算机断层扫描（PACT）是一种具有广泛医学应用的非侵入性成像技术。传统的PACT图像重建算法受到组织中声速不均匀（SOS）引起的波前失真的影响，导致图像质量下降。考虑到这些影响可以提高图像质量，但测量SOS分布的实验成本很高。另一种方法是仅使用PA信号对初始压力图像和SOS进行联合重建。现有的关节重建方法存在局限性：计算成本高，无法直接恢复SOS，以及依赖于不准确的简化假设。隐式神经表示或神经场是计算机视觉中的一种新兴技术，用于通过基于坐标的神经网络学习物理场的有效和连续表示。在这项工作中，我们介绍了NF-APACT，这是一种高效的自监督框架，利用神经场来估计SOS，以实现准确和鲁棒的多通道解卷积。我们的方法比现有方法更快、更准确地消除了SOS像差。我们在一个新的数值体模以及实验收集的体模和体内数据上证明了我们的方法的成功。我们的代码和数字幻影可在https://github.com/Lukeli0425/NF-APACT. et.al.|[2409.10876](http://arxiv.org/abs/2409.10876)|null|

<p align=right>(<a href=#updated-on-20241023>back to top</a>)</p>

[contributors-shield]: https://img.shields.io/github/contributors/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[contributors-url]: https://github.com/Vincentqyw/cv-arxiv-daily/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[forks-url]: https://github.com/Vincentqyw/cv-arxiv-daily/network/members
[stars-shield]: https://img.shields.io/github/stars/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[stars-url]: https://github.com/Vincentqyw/cv-arxiv-daily/stargazers
[issues-shield]: https://img.shields.io/github/issues/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[issues-url]: https://github.com/Vincentqyw/cv-arxiv-daily/issues

