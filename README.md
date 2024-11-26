[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]

## Updated on 2024.11.26
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
|**2024-11-25**|**Quark: Real-time, High-resolution, and General Neural View Synthesis**|我们提出了一种新的神经算法，用于执行高质量、高分辨率、实时的新颖视图合成。我们的网络从一组稀疏的输入RGB图像或视频流中重建3D场景，并在NVIDIA A100上以1080p分辨率和30fps渲染新颖的视图。我们的前馈网络适用于各种数据集和场景，并为实时方法提供最先进的质量。我们的质量接近，在某些情况下甚至超过了一些顶级线下方法的质量。为了实现这些结果，我们使用了几个关键概念的新颖组合，并将它们联系在一起，形成一个连贯有效的算法。我们基于之前使用半透明层表示场景的工作，并使用迭代学习渲染和优化方法来改进这些层。我们的方法重建了分层深度图（LDM），而不是平面层，它有效地表示了具有复杂深度和遮挡的场景。迭代更新步骤嵌入在多尺度、UNet风格的架构中，以降低分辨率执行尽可能多的计算。在每个更新步骤中，为了更好地聚合来自多个输入视图的信息，我们使用了一个专门的基于Transformer的网络组件。与层空间相反，这允许在输入图像空间中执行大部分每输入图像处理，从而进一步提高了效率。最后，由于重建和渲染的实时性，我们为每一帧动态创建和丢弃内部3D几何体，为每个视图生成LDM。综上所述，这产生了一种新颖有效的视图合成算法。通过广泛的评估，我们证明我们以实时速率实现了最先进的质量。项目页面：https://quark-3d.github.io/ et.al.|[2411.16680](http://arxiv.org/abs/2411.16680)|null|
|**2024-11-25**|**SplatFlow: Multi-View Rectified Flow Model for 3D Gaussian Splatting Synthesis**|基于文本的3D场景生成和编辑具有通过直观的用户交互简化内容创建的巨大潜力。虽然最近的进展利用3D高斯散斑（3DGS）进行高保真和实时渲染，但现有的方法通常是专门的和以任务为中心的，缺乏生成和编辑的统一框架。在本文中，我们介绍了SplatFlow，这是一个全面的框架，通过实现直接的3DGS生成和编辑来解决这一差距。SplatFlow包括两个主要组件：多视图整流流（RF）模型和高斯散斑解码器（GSDecoder）。多视图RF模型在潜在空间中运行，根据文本提示同时生成多视图图像、深度和相机姿态，从而解决了现实世界中不同场景比例和复杂相机轨迹等挑战。然后，GSDecoder通过前馈3DGS方法有效地将这些潜在输出转换为3DGS表示。SplatFlow利用无需训练的反转和修复技术，实现了无缝的3DGS编辑，并在统一的框架内支持广泛的3D任务，包括对象编辑、新颖的视图合成和相机姿态估计，而不需要额外的复杂管道。我们在MVImgNet和DL3DV-7K数据集上验证了SplatFlow的功能，展示了它在各种基于3D生成、编辑和修复的任务中的多功能性和有效性。 et.al.|[2411.16443](http://arxiv.org/abs/2411.16443)|null|
|**2024-11-25**|**U2NeRF: Unsupervised Underwater Image Restoration and Neural Radiance Fields**|由于光吸收、折射、散射和恢复，水下图像会出现颜色偏移、对比度低和模糊等问题，因此这些图像值得关注。在这项工作中，我们提出了无监督水下神经辐射场U2NeRF，这是一种基于变换器的架构，可以学习同时渲染和恢复基于多视图几何的新视图。由于缺乏监督，我们试图将恢复能力隐式地烘焙到NeRF管道上，并将预测的颜色分解为几个分量——场景辐射、直接传输图、反向散射传输图和全局背景光，当组合在一起时，以自我监督的方式重建水下图像。此外，我们发布了一个由12个水下场景组成的水下视图合成UVS数据集，其中包含合成生成的数据和真实世界的数据。我们的实验表明，当在单个场景上进行优化时，U2NeRF的表现优于多个基线，LPIPS为11%，UIQM为5%，UCIQE为4%（平均），并展示了改进的渲染和恢复能力。代码将在验收后提供。 et.al.|[2411.16172](http://arxiv.org/abs/2411.16172)|null|
|**2024-11-25**|**MVGenMaster: Scaling Multi-View Generation from Any Image via 3D Priors Enhanced Diffusion Model**|我们介绍了MVGenMaster，这是一种用3D先验增强的多视图扩散模型，用于解决多功能的新视图合成（NVS）任务。MVGenMaster利用使用度量深度和相机姿态扭曲的3D先验，显著增强了NVS中的泛化能力和3D一致性。我们的模型具有一个简单而有效的管道，可以通过一个正向过程生成多达100个基于任意参考视图和相机姿态的新颖视图。此外，我们还开发了一个全面的大规模多视图图像数据集，包含多达120万个场景，并配备了对齐良好的度量深度。此外，我们提出了一些训练和模型修改，以用放大的数据集来加强模型。对域内和域外基准的广泛评估证明了我们提出的方法和数据公式的有效性。型号和代码将于https://github.com/ewrfcas/MVGenMaster/. et.al.|[2411.16157](http://arxiv.org/abs/2411.16157)|null|
|**2024-11-24**|**Fixing the Perspective: A Critical Examination of Zero-1-to-3**|新颖的视图合成是图像到3D生成中的一个基本挑战，需要从一组调节图像及其相对姿态生成目标视图图像。虽然最近的零-1到3等方法使用条件潜在扩散模型显示出有希望的结果，但它们在生成一致和准确的新视图方面面临着重大挑战，特别是在处理多个条件图像时。在这项工作中，我们对扩散2D条件UNet的空间变换器中的零-1到3的交叉注意机制进行了深入的研究。我们的分析揭示了Zero1-to-3的理论框架与其实现之间的关键差异，特别是在图像条件上下文的处理方面。我们提出了两个重大改进：（1）一个能够有效利用交叉注意力机制的纠正实现，以及（2）一个可以同时利用多个条件视图的增强架构。我们的理论分析和初步结果表明，在新颖的视图合成一致性和准确性方面有潜在的改进。 et.al.|[2411.15706](http://arxiv.org/abs/2411.15706)|null|
|**2024-11-23**|**SplatFlow: Self-Supervised Dynamic Gaussian Splatting in Neural Motion Flow Field for Autonomous Driving**|大多数现有的用于复杂动态城市场景的动态高斯散布方法都依赖于昂贵的手动标签的精确对象级监督，这限制了它们在现实世界应用中的可扩展性。在本文中，我们引入了SplatFlow，这是一种神经运动流场（NMFF）中的自监督动态高斯散点，可以学习4D时空表示，而不需要跟踪3D边界框，从而实现精确的动态场景重建和新颖的视图RGB、深度和流合成。SplatFlow设计了一个统一的框架，将时间依赖的4D高斯表示无缝集成到NMFF中，其中NMFF是一组隐式函数，用于将LiDAR点和高斯的时间运动建模为连续运动流场。利用NMFF，SplatFlow有效地分解静态背景和动态对象，分别用3D和4D高斯基元表示它们。NMFF还对每个4D高斯模型的状态对应关系进行建模，该模型聚合了时间特征，以提高动态组件的跨视图一致性。SplatFlow通过从2D基础模型中提取特征到4D时空表示中，进一步改进了动态场景识别。对Waymo开放数据集和KITTI数据集进行的综合评估验证了SplatFlow在动态城市场景中的图像重建和新颖视图合成方面的最先进（SOTA）性能。 et.al.|[2411.15482](http://arxiv.org/abs/2411.15482)|null|
|**2024-11-22**|**3D Convex Splatting: Radiance Field Rendering with 3D Smooth Convexes**|辐射场重建的最新进展，如3D高斯散斑（3DGS），通过用高斯基元的组合表示场景，实现了高质量的新颖视图合成和快速渲染。然而，3D高斯模型在场景重建方面存在一些局限性。在不显著增加高斯数的情况下准确捕捉硬边是具有挑战性的，这会产生大量的内存占用。此外，由于它们在空间中扩散，它们很难表示平面。如果没有手工制作的正则化器，它们往往会不规则地分散在实际表面周围。为了规避这些问题，我们引入了一种名为3D凸散斑（3DCS）的新方法，该方法利用3D平滑凸作为基元，从多视图图像中建模具有几何意义的辐射场。平滑凸形状比高斯形状提供了更大的灵活性，允许使用更少的图元更好地表示具有硬边缘和密集体积的3D场景。在我们高效的基于CUDA的光栅化器的支持下，3DCS在Mip-NeRF360、坦克和神庙以及深度混合等基准上实现了优于3DGS的性能。具体来说，与3DGS相比，我们的方法在PSNR方面提高了0.81，在LPIPS方面提高了0.026，同时保持了高渲染速度并减少了所需图元的数量。我们的研究结果突出了3D凸散斑技术成为高质量场景重建和新颖视图合成新标准的潜力。项目页面：www.convexsplating.com。 et.al.|[2411.14974](http://arxiv.org/abs/2411.14974)|**[link](https://github.com/convexsplatting/convex-splatting)**|
|**2024-11-21**|**Novel View Extrapolation with Video Diffusion Priors**|由于辐射场方法的发展，新颖视图合成领域取得了重大进展。然而，大多数辐射场技术在新视图插值方面比新视图外推要好得多，在新视图外推中，合成的新视图远远超出了观察到的训练视图。我们设计了ViewExtrapolator，这是一种新颖的视图合成方法，利用稳定视频扩散（SVD）的生成先验进行逼真的新颖视图外推。通过重新设计SVD去噪过程，ViewExtrapolator细化了辐射场渲染的易产生伪影的视图，大大提高了合成新视图的清晰度和真实感。ViewExtrapolator是一种通用的新型视图外推器，可以处理不同类型的3D渲染，例如当只有单个视图或单眼视频可用时从点云渲染的视图。此外，ViewExtrapolator不需要对SVD进行微调，使其既具有数据效率，又具有计算效率。大量实验证明了ViewExtrapolator在新的视图外推中的优越性。项目页面：\url{https://kunhao-liu.github.io/ViewExtrapolator/}. et.al.|[2411.14208](http://arxiv.org/abs/2411.14208)|null|
|**2024-11-21**|**Image Compression Using Novel View Synthesis Priors**|实时视觉反馈对于远程操作车辆的无远程控制至关重要，特别是在检查和操作任务期间。尽管声通信是水下中程通信的首选，但其有限的带宽使得实时传输图像或视频变得不切实际。为了解决这个问题，我们提出了一种基于模型的图像压缩技术，该技术利用了先前的任务信息。我们的方法采用经过训练的基于机器学习的新颖视图合成模型，并使用梯度下降优化来细化潜在表示，以帮助生成相机图像和渲染图像之间的可压缩差异。我们使用来自人工海洋盆地的数据集评估了所提出的压缩技术，证明了其优于现有技术的压缩比和图像质量。此外，我们的方法对场景中新对象的引入表现出鲁棒性，突出了其推进无遥控车辆操作的潜力。 et.al.|[2411.13862](http://arxiv.org/abs/2411.13862)|null|
|**2024-11-20**|**Sparse Input View Synthesis: 3D Representations and Reliable Priors**|新颖视点合成是指从几个视点合成给定图像的场景的新颖视点的问题。这是计算机视觉和图形学中的一个基本问题，它支持各种各样的应用程序，如元宇宙、事件的免费观看、视频游戏、视频稳定和视频压缩。最近的3D表示，如辐射场和多平面图像，显著提高了从新视点渲染的图像的质量。然而，这些模型需要对输入视图进行密集采样，以获得高质量的渲染。当只有少数输入视图可用时，它们的性能会显著下降。本文主要研究静态和动态场景的稀疏输入新视图合成问题。在这项工作的第一部分中，我们主要关注使用神经辐射场（NeRF）对静态场景进行稀疏输入新视图合成。我们研究了可靠和密集先验的设计，以便在这种情况下更好地正则化NeRF。特别是，我们提出了一种关于一对输入视图中像素可见性的先验方法。我们证明，这种与物体相对深度相关的可见性先验是密集的，比现有的绝对深度先验更可靠。我们使用平面扫描体积计算可见度先验，而不需要在大型数据集上训练神经网络。我们在多个数据集上评估了我们的方法，并表明我们的模型在稀疏输入新视图合成方面优于现有的方法。在第二部分中，我们的目标是通过学习一个不受泛化问题影响的场景特定先验来进一步改进正则化。我们通过在给定场景上单独学习先验知识来实现这一点，而无需在大型数据集上进行预训练。特别是，我们设计了增强型NeRF，以便在场景的某些区域为主NeRF提供更好的深度监控。此外，我们扩展了这一框架，使其也适用于更新、更快的辐射场模型，如TensoRF和ZipNeRF。通过在多个数据集上的广泛实验，我们展示了我们的方法在稀疏输入新视图合成方面的优越性。稀疏输入快速动态辐射场的设计受到缺乏合适的运动表示和可靠先验的严重限制。我们通过设计一个基于因子体积的显式运动模型来解决第一个挑战，该模型紧凑且快速优化。我们还引入了可靠的稀疏流先验来约束运动场，因为我们发现常用的密集光流先验是不可靠的。我们在多个数据集上展示了我们的运动表示和可靠先验的好处。在本文的最后一部分，我们研究了视图合成在视频游戏帧率上采样中的应用。具体来说，我们考虑时间视图合成的问题，其目标是在给定过去帧和相机运动的情况下预测未来帧。这里的关键挑战是通过估计物体的过去运动并对其进行外推来预测物体的未来运动。我们探索了使用多平面图像表示和场景深度来可靠地估计物体运动，特别是在遮挡区域。我们设计了一个新的数据库来有效地评估我们的动态场景时间视图合成方法，并表明我们达到了最先进的性能。 et.al.|[2411.13631](http://arxiv.org/abs/2411.13631)|null|

<p align=right>(<a href=#updated-on-20241126>back to top</a>)</p>

## 3D Reconstruction

|Publish Date|Title|Abstract|PDF|Code|
|---|---|---|---|---|
|**2024-11-25**|**Functionality understanding and segmentation in 3D scenes**|理解3D场景中的功能涉及解释自然语言描述，以在3D环境中定位功能交互对象，如手柄和按钮。功能理解极具挑战性，因为它既需要世界知识来解释语言，也需要空间感知来识别细粒度对象。例如，给定一个像“打开顶灯”这样的任务，一个嵌入式AI代理必须推断出它需要定位电灯开关，即使任务描述中没有明确提到开关。迄今为止，还没有针对这个问题开发出专门的方法。本文介绍了Fun3DU，这是第一种为3D场景中的功能理解而设计的方法。Fun3DU使用语言模型通过思维链推理解析任务描述，以识别感兴趣的对象。通过使用视觉和语言模型，在捕获场景的多个视图中分割识别的对象。来自每个视图的分割结果在3D中被提升，并使用几何信息聚合到点云中。Fun3DU是免费训练的，完全依赖于预先训练的模型。我们在SceneFun3D上评估了Fun3DU，这是最新也是唯一一个对这项任务进行基准测试的数据集，它包括230个场景的3000多个任务描述。我们的方法明显优于最先进的开放词汇3D分割方法。代码将公开发布。 et.al.|[2411.16310](http://arxiv.org/abs/2411.16310)|null|
|**2024-11-25**|**Event-boosted Deformable 3D Gaussians for Fast Dynamic Scene Reconstruction**|3D高斯散斑（3D-GS）可以实现实时渲染，但由于RGB相机的低时间分辨率，在快速运动方面遇到了困难。为了解决这个问题，我们介绍了第一种将捕获高时间分辨率连续运动数据的事件相机与可变形3D-GS相结合的方法，用于快速动态场景重建。我们观察到，事件的阈值建模在实现高质量重建方面起着至关重要的作用。因此，我们提出了一种GS阈值联合建模（GTJM）策略，创建了一个相辅相成的过程，大大改善了3D重建和阈值建模。此外，我们引入了一种动态静态分解（DSD）策略，该策略首先通过利用静态高斯模型无法表示运动来识别动态区域，然后应用基于缓冲区的软分解来分离动态和静态区域。此策略通过避免静态区域中不必要的变形来加速渲染，并侧重于动态区域以提高保真度。我们的方法在RTX 3090 GPU上实现了156 FPS的高保真动态重建，分辨率为400美元×400美元。 et.al.|[2411.16180](http://arxiv.org/abs/2411.16180)|null|
|**2024-11-24**|**Generalizable Single-view Object Pose Estimation by Two-side Generating and Matching**|本文提出了一种新的可推广的物体姿态估计方法，仅使用一幅RGB图像来确定物体姿态。与依赖于实例级对象姿态估计并需要大量训练数据的传统方法不同，我们的方法可以在不进行大量训练的情况下对看不见的对象进行泛化，使用对象的单个参考图像进行操作，并且不需要3D对象模型或对象的多个视图。这些特征是通过利用扩散模型生成新的视图图像并对这些生成的图像进行双面匹配来实现的。定量实验证明了我们的方法在合成和现实世界数据集上优于现有的姿态估计技术。值得注意的是，即使在视点发生重大变化的情况下，我们的方法也能保持强大的性能，突显了其在具有挑战性的条件下的鲁棒性和通用性。该代码将在以下时间重新发布https://github.com/scy639/Gen2SM. et.al.|[2411.15860](http://arxiv.org/abs/2411.15860)|**[link](https://github.com/scy639/gen2sm)**|
|**2024-11-24**|**ZeroGS: Training 3D Gaussian Splatting from Unposed Images**|神经辐射场（NeRF）和3D高斯散斑（3DGS）是重建和渲染照片级逼真图像的流行技术。然而，运行运动结构（SfM）以获取相机姿态的先决条件限制了它们的完整性。虽然以前的方法可以从一些未经滤波的图像中重建，但当图像无序或密集捕获时，它们不适用。在这项工作中，我们建议ZeroGS从数百张未经处理和无序的图像中训练3DGS。我们的方法利用预训练的基础模型作为神经场景表示。由于预测点图的精度不足以实现精确的图像配准和高保真图像渲染，我们建议通过从种子图像初始化和微调预训练模型来缓解这一问题。然后，图像被逐步注册并添加到训练缓冲区中，该缓冲区进一步用于训练模型。我们还建议通过最小化跨多个视图的点对相机光线一致性损失来优化相机姿态和点图。在LLFF数据集、MipNeRF360数据集和Tanks and Temples数据集上的实验表明，我们的方法比最先进的无姿态NeRF/3DGS方法恢复了更精确的相机姿态，甚至比具有COLMAP姿态的3DGS渲染了更高质量的图像。我们的项目页面可在https://aibluefisher.github.io/ZeroGS. et.al.|[2411.15779](http://arxiv.org/abs/2411.15779)|null|
|**2024-11-24**|**GSurf: 3D Reconstruction via Signed Distance Fields with Direct Gaussian Supervision**|从多视图图像中重建表面是3D视觉的一个核心挑战。最近的研究探索了神经辐射场（NeRF）中的符号距离场（SDF），以实现高保真表面重建。然而，与3D高斯飞溅（3DGS）相比，这些方法的训练和渲染速度通常较慢。当前最先进的技术试图融合深度信息以从3DGS中提取几何体，但经常导致重建不完整和表面破碎。本文介绍了GSurf，这是一种直接从高斯基元学习带符号距离场的新型端到端方法。SDF的连续性和平滑性解决了3DGS系列中的常见问题，例如由噪声或缺失的深度数据引起的孔洞。通过使用高斯散点进行渲染，GSurf避免了其他GS和SDF集成中通常需要的冗余体渲染。因此，GSurf实现了更快的训练和渲染速度，同时提供了与VolSDF和NeuS等神经隐式表面方法相当的3D重建质量。各种基准数据集的实验结果证明了我们的方法在生成高保真3D重建方面的有效性。 et.al.|[2411.15723](http://arxiv.org/abs/2411.15723)|**[link](https://github.com/xubaixinxbx/gsurf)**|
|**2024-11-23**|**An adversarial feature learning based semantic communication method for Human 3D Reconstruction**|随着人体3D重建技术在各个领域的广泛应用，对数据传输和处理效率的要求不断提高，特别是在网络带宽有限、需要低延迟的情况下。本文介绍了一种基于对抗特征学习的人体三维重建语义通信方法（AFLSC），该方法侧重于提取和传输对三维重建任务至关重要的语义信息，从而显著优化数据流并减轻带宽压力。在发送者端，我们提出了一种基于多任务学习的特征提取方法，从二维人体图像中捕获空间布局、关键点、姿势和深度信息，并设计了一种针对性特征学习的语义编码技术，将这些特征信息编码为语义数据。我们还开发了一种动态压缩技术来有效地传输这些语义数据，大大提高了传输效率并减少了延迟。在接收端，我们设计了一种高效的多级语义特征解码方法，将语义数据转换回关键图像特征。最后，采用改进的ViT扩散模型进行三维重建，生成人体三维网格模型。实验结果验证了我们的方法在数据传输效率和重建质量方面的优势，证明了它在带宽受限环境中的巨大应用潜力。 et.al.|[2411.15595](http://arxiv.org/abs/2411.15595)|null|
|**2024-11-23**|**Semi-supervised Single-view 3D Reconstruction via Multi Shape Prior Fusion Strategy and Self-Attention**|在单视图3D重建领域，传统技术经常依赖于昂贵且耗时的3D注释数据。面对注释获取的挑战，半监督学习策略提供了一种创新的方法来减少对标记数据的依赖。尽管有这些发展，但这种学习范式在3D重建任务中的应用仍然相对受限。在这项研究中，我们创建了一个创新的半监督3D重建框架，该框架独特地引入了多形状先验融合策略，旨在指导创建更逼真的对象结构。此外，为了提高形状生成的质量，我们在传统解码器中集成了一个自我关注模块。在ShapeNet数据集的基准测试中，我们的方法在1%、10%和20%的不同标记比率下大大优于现有的监督学习方法。此外，它在真实世界的Pix3D数据集上展示了出色的性能。通过在ShapeNet上的全面实验，我们的框架比基线性能提高了3.3%。此外，严格的消融研究进一步证实了我们方法的显著有效性。我们的代码已于发布https://github.com/NWUzhouwei/SSMP et.al.|[2411.15420](http://arxiv.org/abs/2411.15420)|**[link](https://github.com/nwuzhouwei/ssmp)**|
|**2024-11-22**|**OVO-SLAM: Open-Vocabulary Online Simultaneous Localization and Mapping**|本文介绍了第一个开放词汇在线3D语义SLAM管道，我们称之为OVO-SLAM。我们的主要贡献在于管道本身，特别是在映射线程中。给定一组摆姿势的RGB-D帧，我们检测并跟踪3D片段，我们使用CLIP向量对其进行描述，这些向量是通过从观察这些3D片段的视点进行新的聚合计算得出的。值得注意的是，与文献中的离线方法相比，我们的OVO-SLAM管道不仅更快，而且实现了更好的分割指标。除了卓越的分割性能外，我们还展示了与高斯SLAM集成的我们的贡献的实验结果，这是第一个展示端到端开放词汇在线3D重建而不依赖于地面真实相机姿态或场景几何形状的实验结果。 et.al.|[2411.15043](http://arxiv.org/abs/2411.15043)|null|
|**2024-11-21**|**EasyHOI: Unleashing the Power of Large Models for Reconstructing Hand-Object Interactions in the Wild**|我们的工作旨在从单视图图像重建手与物体的相互作用，这是一项基本但不适定的任务。与从视频、多视图图像或预定义的3D模板重建的方法不同，由于固有的模糊性和遮挡，单视图重建面临着重大挑战。手部姿势的多样性以及物体形状和大小的多样性进一步放大了这些挑战。我们的关键见解是，目前用于分割、修复和3D重建的基础模型可以稳健地推广到野外图像，这可以为重建手部对象交互提供强大的视觉和几何先验。具体来说，给定一张图像，我们首先设计了一个新的管道，使用现成的大型模型来估计潜在的手部姿势和物体形状。此外，在初始重建中，我们采用了一种先验引导优化方案，该方案优化了手部姿势，以符合3D物理约束和2D输入图像内容。我们在多个数据集上进行了实验，结果表明我们的方法始终优于基线，并忠实地重建了一组不同的手-物体交互。以下是我们项目页面的链接：https://lym29.github.io/EasyHOI-page/ et.al.|[2411.14280](http://arxiv.org/abs/2411.14280)|null|
|**2024-11-20**|**Open-World Amodal Appearance Completion**|理解和重建被遮挡的对象是一个具有挑战性的问题，特别是在类别和背景多样且不可预测的开放世界场景中。然而，传统方法通常仅限于封闭的对象类别集，限制了它们在复杂的开放世界场景中的使用。我们介绍了Open World Amodal Appearance Completion，这是一个无需训练的框架，通过接受灵活的文本查询作为输入来扩展Amodal补全功能。我们的方法推广到由直接项和抽象查询指定的任意对象。我们将这种能力推理称为amodal完成，其中系统根据提供的图像和语言查询重建查询对象的完整外观。我们的框架统一了分割、遮挡分析和修复，以处理复杂的遮挡，并将完成的对象生成为RGBA元素，从而能够无缝集成到3D重建和图像编辑等应用程序中。广泛的评估证明了我们的方法在推广到新物体和遮挡物方面的有效性，为开放世界环境中的无模完成建立了新的基准。代码和数据集将在论文验收后发布。 et.al.|[2411.13019](http://arxiv.org/abs/2411.13019)|null|

<p align=right>(<a href=#updated-on-20241126>back to top</a>)</p>

## Diffusion

|Publish Date|Title|Abstract|PDF|Code|
|---|---|---|---|---|
|**2024-11-25**|**The impact of resistivity on the variability of black hole accretion flows**|背景。磁化等离子体在黑洞上的吸积是一个复杂而动态的过程，其中磁场起着至关重要的作用。事件视界附近积累的磁通量对吸积流行为有显著影响。电阻率是衡量磁场消散难易程度的指标，被认为是影响这一过程的关键因素。这项工作探讨了电阻率对吸积流变化的影响。我们研究了达到磁制动盘（MAD）极限的模拟和具有初始多环磁场配置的模拟。方法。我们采用3D电阻广义相对论磁流体动力学（GRMHD）模拟来模拟不同制度下的吸积过程，其中电阻率具有全局均匀值。结果。我们的发现揭示了取决于电阻率的不同流动行为。高电阻率模拟从未达到MAD状态，表明磁通量累积过程受到干扰。相反，低电阻率模拟收敛到理想的MHD极限。主要结果是：i）对于标准MAD模型，电阻率在流量变化中的作用很小，表明通量喷发事件主导了动力学。ii）高电阻率模拟显示，强磁场扩散到磁盘中，重新排列了吸积流中有效的磁通量积累。iii）在多回路模拟中，电阻率显著降低了流量变化，这是出乎意料的。然而，由于在非常低的电阻率值下频繁发生重新连接事件，磁通量累积变得更加可变。结论。这项研究表明，电阻率会影响磁场耗散导致的流量失真程度。我们的发现为磁场积累、电阻率、可变性和黑洞吸积动力学之间的相互作用提供了新的见解。 et.al.|[2411.16684](http://arxiv.org/abs/2411.16684)|null|
|**2024-11-25**|**Generative Omnimatte: Learning to Decompose Video into Layers**|给定一个视频和一组输入对象掩码，omnimatte方法旨在将视频分解为语义上有意义的层，其中包含单个对象及其相关效果，如阴影和反射。现有的全向方法假设静态背景或精确的姿态和深度估计，当这些假设被违反时，会产生较差的分解。此外，由于自然视频缺乏生成先验，现有方法无法完成动态遮挡区域。我们提出了一种新的生成式分层视频分解框架来解决全向问题。我们的方法不假设一个静止的场景，也不需要相机姿态或深度信息，并产生干净、完整的层，包括令人信服的遮挡动态区域的完成。我们的核心思想是训练一个视频扩散模型来识别和消除由特定对象引起的场景效果。我们表明，该模型可以从现有的视频修复模型中进行微调，使用一个小的、精心策划的数据集，并为各种随意拍摄的视频演示高质量的分解和编辑结果，这些视频包含柔和的阴影、光滑的反射、飞溅的水等等。 et.al.|[2411.16683](http://arxiv.org/abs/2411.16683)|null|
|**2024-11-25**|**Diffusion Features for Zero-Shot 6DoF Object Pose Estimation**|零样本物体姿态估计能够从图像中检索物体姿态，而无需特定于物体的训练。在最近的方法中，视觉基础模型（VFM）促进了这一点，VFM是预训练的模型，是有效的通用特征提取器。这些VFM表现出的特征因训练数据、网络架构和训练范式而异。该领域的主流选择是自我监督的视觉转换器（ViT）。本研究评估了潜在扩散模型（LDM）主干对零样本姿态估计的影响。为了便于在共同点上对两个模型家族进行比较，我们采用并修改了最近的一种方法。因此，提出了一种基于模板的多阶段方法，用于使用LDM以零样本方式估计姿态。在三个标准数据集上对所提出方法的有效性进行了实证评估，用于特定对象的6DoF姿态估计。实验表明，与ViT基线相比，平均召回率提高了27%。源代码可在以下网址获得：https://github.com/BvG1993/DZOP. et.al.|[2411.16668](http://arxiv.org/abs/2411.16668)|null|
|**2024-11-25**|**LegoPET: Hierarchical Feature Guided Conditional Diffusion for PET Image Reconstruction**|正电子发射断层扫描（PET）由于其在体内可视化功能和生物过程的能力而被广泛用于癌症检测。PET图像通常使用传统的迭代技术（如OSEM、MLEM）从组织图原始数据（正弦图）中重建。最近，深度学习（DL）方法通过将原始正弦图数据直接映射到PET图像显示出希望。然而，基于回归或基于GAN的DL方法通常会产生过度平滑的图像或分别引入各种伪影。图像条件扩散概率模型（cDPMs）是另一类基于似然的DL技术，能够生成高度逼真和可控的图像。虽然cDPMs具有显著的优势，但它们仍然面临着挑战，例如当输入和输出图像来自不同的域（例如，正弦图与图像域）时，如何保持它们之间的对应性和一致性，以及收敛速度慢。为了解决这些局限性，我们引入了LegoPET，这是一种分层特征引导的条件扩散模型，用于从正弦图重建高感知质量的PET图像。我们进行了几项实验，证明LegoPET不仅提高了cDPM的性能，而且在视觉质量和像素级PSNR/SSIM指标方面也超越了最近基于DL的PET图像重建技术。我们的代码可在https://github.com/yransun/LegoPET. et.al.|[2411.16629](http://arxiv.org/abs/2411.16629)|null|
|**2024-11-25**|**Inference-Time Policy Steering through Human Interactions**|经过人类示范训练的生成性政策可以自主完成多模式、长期任务。然而，在推理过程中，人类往往被排除在策略执行循环之外，限制了在多个预测中引导预训练策略朝向特定子目标或轨迹形状的能力。天真的人为干预可能会无意中加剧分配转移，导致违反约束或执行失败。为了更好地使策略输出与人类意图保持一致，而不会导致分布外错误，我们提出了一种推理时间策略指导（ITPS）框架，该框架利用人类交互来偏置生成采样过程，而不是对交互数据的策略进行微调。我们在三个模拟和现实世界的基准上评估ITPS，测试三种形式的人机交互和相关的对齐距离度量。在六种采样策略中，我们提出的具有扩散策略的随机采样实现了对齐和分布偏移之间的最佳权衡。视频可在https://yanweiw.github.io/itps/. et.al.|[2411.16627](http://arxiv.org/abs/2411.16627)|null|
|**2024-11-25**|**Chat2SVG: Vector Graphics Generation with Large Language Models and Image Diffusion Models**|可缩放矢量图形（SVG）已成为数字设计中矢量图形的事实标准，提供分辨率独立性和对单个元素的精确控制。尽管有这些优势，但创建高质量的SVG内容仍然具有挑战性，因为它需要专业编辑软件的技术专长和大量时间来制作复杂的形状。最近的文本到SVG生成方法旨在使矢量图形创建更容易访问，但它们在形状规则性、泛化能力和表现力方面仍然存在局限性。为了应对这些挑战，我们引入了Chat2SVG，这是一个混合框架，结合了大型语言模型（LLM）和图像扩散模型的优势，用于文本到SVG的生成。我们的方法首先使用LLM从基本几何图元生成语义上有意义的SVG模板。在图像扩散模型的指导下，双级优化流水线细化潜在空间中的路径，并调整点坐标以提高几何复杂性。大量实验表明，Chat2SVG在视觉保真度、路径规则性和语义对齐方面优于现有方法。此外，我们的系统能够通过自然语言指令进行直观的编辑，使所有用户都可以访问专业的矢量图形创建。 et.al.|[2411.16602](http://arxiv.org/abs/2411.16602)|null|
|**2024-11-25**|**Unlocking The Potential of Adaptive Attacks on Diffusion-Based Purification**|基于扩散的净化（DBP）是一种针对对抗性实例（AE）的防御方法，因其能够以一种不受攻击的方式保护分类器，并能够抵抗具有防御能力的强大对手而广受欢迎。它的稳健性被认为是由于依赖于将AE投影到自然分布上的扩散模型（DM）。我们重新审视了这一说法，重点关注基于梯度的策略，通过防御反向传播损失梯度，通常称为“自适应攻击”“.分析表明，这种优化方法使DBP的核心基础无效，有效地针对DM而不是分类器，并将纯化输出限制在恶意样本的分布上。因此，我们重新评估了报告的经验稳健性，发现了迄今为止用于DBP的梯度反向传播技术中的实现缺陷。我们解决了这些问题，为DBP提供了第一个可靠的梯度库，并展示了自适应攻击如何大大降低其稳健性。然后，我们研究了一种效率较低但更严格的多数投票设置，其中分类器评估输入的多个纯化副本以做出决定。在这里，DBP的随机性使其能够对传统的范数有界AE保持部分稳健性。我们提出了一种对最近优化方法的新适应。针对在确保不可察觉性的同时制造系统性恶意干扰的深度伪造水印。当与自适应攻击相结合时，它完全即使在多数票的情况下，也击败了DBP。我们的研究结果证明，DBP在目前的状态下并不是一种有效的预防不良事件的方法。 et.al.|[2411.16598](http://arxiv.org/abs/2411.16598)|null|
|**2024-11-25**|**Sequential data assimilation for PDEs using shape-morphing solutions**|形状变形解（也称为进化深度神经网络、降阶非线性解和神经伽略金方案）是一类新的近似含时偏微分方程解的方法。在这里，我们介绍了一种顺序数据同化方法，用于将观测数据合并到形状变形解决方案（SMS）中。我们的方法采用预测校正方案的形式，其中观测值用于使用类牛顿迭代来校正SMS参数。在观测点之间，使用SMS方程（一组常微分方程）来及时推进解。我们证明，在一定条件下，数据同化SMS（DA-SMS）会均匀地收敛到系统的真实状态。我们通过三个例子证明了DA-SMS的有效性：非线性薛定谔方程、Kuramoto-Sivashinsky方程和二维平流扩散方程。我们的数值结果表明，DA-SMS在相对稀疏的观测值和类牛顿方法的单次迭代下收敛。 et.al.|[2411.16593](http://arxiv.org/abs/2411.16593)|null|
|**2024-11-25**|**Rethinking Diffusion for Text-Driven Human Motion Generation**|自2023年以来，基于矢量量化（VQ）的离散生成方法迅速主导了人体运动生成，主要在标准性能指标上超越了基于扩散的连续生成方法。然而，基于VQ的方法具有固有的局限性。将连续运动数据表示为有限的离散标记会导致不可避免的信息丢失，降低生成运动的多样性，并限制其作为运动先验或生成指导有效发挥作用的能力。相比之下，基于扩散的方法的连续空间生成特性使其非常适合解决这些局限性，甚至具有模型可扩展性的潜力。在这项工作中，我们系统地研究了为什么当前基于VQ的方法表现良好，并从运动数据表示和分布的角度探索了现有基于扩散的方法的局限性。基于这些见解，我们保留了基于扩散的人体运动生成模型的固有优势，并在基于VQ的方法的启发下逐步优化它。我们的方法引入了一种人体运动扩散模型，该模型能够执行双向掩蔽自回归，并通过改进的数据表示和分布进行了优化。此外，我们还提出了更稳健的评估方法，以公平地评估不同的方法。对基准人体运动生成数据集的广泛实验表明，我们的方法优于以前的方法，并实现了最先进的性能。 et.al.|[2411.16575](http://arxiv.org/abs/2411.16575)|null|
|**2024-11-25**|**Representation Collapsing Problems in Vector Quantization**|向量量化是机器学习中的一种技术，它将连续表示离散化为一组离散向量。它被广泛用于标记大型语言模型、扩散模型和其他生成模型的数据表示。尽管矢量量化在生成模型中普遍存在，但其特征和行为在很大程度上仍未得到充分探索。在这项研究中，我们研究了矢量量化中的表示崩溃——这是一种关键的退化，其中码本令牌或潜在嵌入由于收敛到有限的值子集而失去了判别能力。这种崩溃从根本上损害了模型捕获不同数据模式的能力。通过利用合成和真实数据集，我们确定了每种坍塌的严重程度和触发条件。我们的分析表明，受限的初始化和有限的编码器容量会导致令牌崩溃和嵌入崩溃。基于这些发现，我们提出了旨在减轻每次崩溃的潜在解决方案。据我们所知，这是首次对矢量量化中的表示折叠问题进行全面研究。 et.al.|[2411.16550](http://arxiv.org/abs/2411.16550)|null|

<p align=right>(<a href=#updated-on-20241126>back to top</a>)</p>

## NeRF

|Publish Date|Title|Abstract|PDF|Code|
|---|---|---|---|---|
|**2024-11-21**|**CoNFiLD-inlet: Synthetic Turbulence Inflow Using Generative Latent Diffusion Models with Neural Fields**|涡流解析湍流模拟需要随机流入条件，以准确复制复杂的多尺度湍流结构。传统的基于再循环的方法依赖于计算昂贵的前体模拟，而现有的合成流入发生器往往无法再现真实的湍流相干结构。深度学习（DL）的最新进展为流入湍流生成开辟了新的可能性，但许多基于DL的方法依赖于确定性、自回归框架，容易产生误差累积，导致长期预测的鲁棒性较差。在这项工作中，我们提出了CoNFiLD入口，这是一种基于DL的新型流入湍流发生器，它将扩散模型与条件神经场（CNF）编码的潜在空间相结合，以产生逼真的随机流入湍流。通过使用雷诺数对流入条件进行参数化，CoNFiLD入口在很宽的雷诺数范围内（ $Re_tau$在$10^3$和$10^4$ 之间）有效地推广，而不需要重新训练或参数调整。通过直接数值模拟（DNS）和壁模型大涡模拟（WMLES）中的先验和后验测试进行的全面验证证明了其高保真度、鲁棒性和可扩展性，使其成为流入湍流合成的高效和通用解决方案。 et.al.|[2411.14378](http://arxiv.org/abs/2411.14378)|null|
|**2024-11-20**|**FAST-Splat: Fast, Ambiguity-Free Semantics Transfer in Gaussian Splatting**|我们提出了FAST Splat，用于快速、无歧义的语义高斯Splatting，旨在解决现有语义高斯Splatting方法的主要局限性，即：训练和渲染速度慢；内存使用率高；语义对象定位模糊。在推导FAST Splat时，我们将开放词汇语义高斯Splatting表述为将闭集语义蒸馏扩展到开放集（开放词汇）设置的问题，使FAST Splat能够提供精确的语义对象定位结果，即使在用户提供的模糊自然语言查询提示时也是如此。此外，通过最大限度地利用高斯散斑场景表示的显式形式，FAST Splat保留了高斯散斑的显著训练和渲染速度。具体来说，虽然现有的语义高斯散斑方法将语义提取到一个单独的神经场中或利用神经模型进行降维，但FAST Splat直接用特定的语义代码增强每个高斯分布，保留了高斯散斑相对于神经场方法的训练、渲染和内存使用优势。与先前的方法不同，这些高斯特定的语义代码以及哈希表使语义相似性能够通过开放词汇表用户提示进行测量，并进一步使FAST Splat能够用明确的语义对象标签和3D掩码进行响应。在实验中，我们证明，与最好的竞争语义高斯Splatting方法相比，FAST Splat的训练速度快4倍至6倍，数据预处理步骤快13倍，渲染速度快18倍至75倍，所需GPU内存大约小3倍。此外，与现有方法相比，FAST Splat实现了相对相似或更好的语义分割性能。审查期结束后，我们将提供项目网站和代码库的链接。 et.al.|[2411.13753](http://arxiv.org/abs/2411.13753)|null|
|**2024-11-20**|**GazeGaussian: High-Fidelity Gaze Redirection with 3D Gaussian Splatting**|在处理分布外数据时，凝视估计遇到了泛化挑战。为了解决这个问题，最近的方法使用神经辐射场（NeRF）来生成增强数据。然而，基于NeRF的现有方法计算成本高昂，缺乏面部细节。三维高斯散斑（3DGS）已成为神经场的主流表示。虽然3DGS已经在头部化身中得到了广泛的研究，但它面临着在不同受试者之间进行精确视线控制和泛化的挑战。在这项工作中，我们提出了GazeGaussian，这是一种高保真的视线重定向方法，它使用双流3DGS模型分别表示面部和眼睛区域。通过利用3DGS的非结构化特性，我们开发了一种基于目标凝视方向的刚性眼睛旋转的新眼睛表示。为了增强各种主题的综合泛化能力，我们集成了一个表达式条件模块来指导神经渲染器。综合实验表明，GazeGaussian在渲染速度、视线重定向精度和跨多个数据集的面部合成方面优于现有方法。我们还证明，现有的凝视估计方法可以利用GazeGaussian来提高其泛化性能。该代码将在以下网址提供：https://ucwxb.github.io/GazeGaussian/. et.al.|[2411.12981](http://arxiv.org/abs/2411.12981)|null|
|**2024-11-18**|**NeuMaDiff: Neural Material Synthesis via Hyperdiffusion**|高质量的材料合成对于复制复杂的表面特性以创建逼真的数字场景至关重要。然而，现有的方法往往在时间和内存方面效率低下，需要领域专业知识，或者需要大量的训练数据，而高维材料数据进一步限制了性能。此外，大多数方法缺乏多模态制导能力和标准化的评估指标，限制了综合任务的控制和可比性。为了解决这些局限性，我们提出了NeuMaDiff，这是一种利用超扩散的新型神经材料合成框架。我们的方法采用神经场作为低维表示，并结合了多模态条件超扩散模型来学习材料重量的分布。这使得通过材料类型、文本描述或参考图像等输入进行灵活指导成为可能，从而对合成提供了更大的控制。为了支持未来的研究，我们贡献了两个新的材料数据集，并引入了两个BRDF分布度量，以进行更严格的评估。我们通过广泛的实验证明了NeuMaDiff的有效性，包括一种新的基于统计的约束合成方法，该方法能够生成所需类别的材料。 et.al.|[2411.12015](http://arxiv.org/abs/2411.12015)|null|
|**2024-11-14**|**The Hydrodynamic Limit of Hawkes Processes on Adaptive Stochastic Networks**|我们确定了自适应网络上相互作用的霍克斯过程网络的大尺寸限制。节点变量的翻转被认为具有由传入边缘和节点的平均场给出的强度。边缘变量的翻转是传入节点变量的函数。边变量可以是对称的，也可以是不对称的。该模型受到社会学、神经科学和流行病学应用的启发。一般来说，极限概率律可以表示为具有强度函数的自洽泊松过程的不动点，该强度函数（i）是延迟的，（ii）取决于其自身的概率律。在边缘翻转仅由突触前神经元的状态决定的特定情况下（如神经科学中），证明了可以获得突触增强和神经增强双重进化的自主神经场型方程。 et.al.|[2411.09260](http://arxiv.org/abs/2411.09260)|null|
|**2024-11-09**|**Epi-NAF: Enhancing Neural Attenuation Fields for Limited-Angle CT with Epipolar Consistency Conditions**|神经场方法最初在逆渲染领域取得了成功，最近已扩展到CT重建，标志着传统技术的范式转变。虽然这些方法在稀疏视图CT重建中提供了最先进的结果，但它们在有限的角度设置中很难实现，在有限的视角范围内捕获输入投影。我们提出了一种基于X射线投影图像中相应极线之间一致性条件的新损失项，旨在规范神经衰减场优化。通过强制执行这些一致性条件，我们的方法Epi NAF将监督从有限角度范围内的输入视图传播到整个锥束CT范围内的预测投影。与基线方法相比，这种损失导致重建的定性和定量改进。 et.al.|[2411.06181](http://arxiv.org/abs/2411.06181)|null|
|**2024-11-07**|**LoFi: Scalable Local Image Reconstruction with Implicit Neural Representation**|神经场或隐式神经表示（INR）因其对图像和3D体积的有效连续表示而在机器学习和信号处理中引起了广泛关注。在这项工作中，我们以INR为基础，引入了一种基于坐标的局部处理框架来解决成像逆问题，称为LoFi（局部场）。与传统的图像重建方法不同，LoFi通过多层感知器（MLP）分别处理每个坐标处的局部信息，在该特定坐标处恢复对象。与INR类似，LoFi可以在任何连续坐标下恢复图像，从而实现多分辨率的图像重建。LoFi在图像重建方面的性能与标准CNN相当或更好，几乎与图像分辨率无关，对分布外数据和内存使用具有出色的泛化能力。值得注意的是，对1024美元×1024美元的图像进行训练只需要3GB的内存，比标准CNN通常需要的内存少20多倍。此外，LoFi的局部设计使其能够在小于10个样本的极小数据集上进行训练，而不会过拟合或需要正则化或提前停止。最后，我们使用LoFi作为即插即用框架中的去噪先验，用于解决一般的逆问题，以受益于其连续的图像表示和强大的泛化能力。尽管在低分辨率图像上进行了训练，但LoFi可以用作低维先验，以解决任何分辨率的逆问题。我们通过各种成像方式验证了我们的框架，从低剂量计算机断层扫描到无线电干涉成像。 et.al.|[2411.04995](http://arxiv.org/abs/2411.04995)|null|
|**2024-11-04**|**Physically Based Neural Bidirectional Reflectance Distribution Function**|我们介绍了基于物理的神经双向反射分布函数（PBNBRDF），这是一种基于神经场的材料外观的新颖连续表示。我们的模型准确地重建了真实世界的材料，同时独特地增强了现实BRDF的物理特性，特别是通过重新参数化的亥姆霍兹互易性和通过高效分析积分的能量无源性。我们进行了系统分析，证明了遵守这些物理定律对重建材料的视觉质量的好处。此外，我们通过引入色度强制监督RGB通道的规范来提高神经BRDF的颜色精度。通过在多个测量的真实BRDF数据库上进行定性和定量实验，我们表明，遵守这些物理约束可以使神经场更忠实、更稳定地表示原始数据，并实现更高的渲染质量。 et.al.|[2411.02347](http://arxiv.org/abs/2411.02347)|null|
|**2024-11-01**|**Intensity Field Decomposition for Tissue-Guided Neural Tomography**|锥束计算机断层扫描（CBCT）通常需要数百次X射线投影，这引起了人们对辐射暴露的担忧。虽然稀疏视图重建通过使用更少的投影来减少曝光，但它很难达到令人满意的图像质量。为了应对这一挑战，本文介绍了一种新的稀疏视图CBCT重建方法，该方法为神经场赋予了人体组织正则化的能力。我们的方法被称为组织引导神经断层扫描（TNT），其动机是CBCT中骨骼和软组织之间明显的强度差异。直观地说，分离这些成分可能有助于神经场的学习过程。更确切地说，TNT包括一个异构的四重网络和相应的训练策略。该网络将强度场表示为软组织和硬组织成分及其各自纹理的组合。我们在估计的组织投影的指导下训练网络，从而能够有效地学习网络头所需的模式。大量实验表明，所提出的方法显著改善了稀疏视图CBCT重建，投影数量从10到60不等。与最先进的基于神经渲染的方法相比，我们的方法以更少的投影和更快的收敛实现了相当的重建质量。 et.al.|[2411.00900](http://arxiv.org/abs/2411.00900)|null|
|**2024-10-26**|**Neural Fields in Robotics: A Survey**|神经场已经成为计算机视觉和机器人技术中3D场景表示的一种变革性方法，能够从姿势的2D数据中准确推断几何、3D语义和动力学。利用可微分渲染，神经场包括连续隐式和显式神经表示，实现了高保真3D重建、多模态传感器数据的集成和新视点的生成。这项调查探讨了它们在机器人技术中的应用，强调了它们在增强感知、规划和控制方面的潜力。它们的紧凑性、内存效率和可微性，以及与基础模型和生成模型的无缝集成，使其成为实时应用的理想选择，提高了机器人的适应性和决策能力。本文基于200多篇论文，对机器人中的神经场进行了全面的回顾，对各个领域的应用进行了分类，并评估了它们的优势和局限性。首先，我们介绍了四个关键的神经场框架：占用网络、有符号距离场、神经辐射场和高斯散斑。其次，我们详细介绍了神经场在五个主要机器人领域的应用：姿态估计、操纵、导航、物理和自动驾驶，重点介绍了关键工作，并讨论了要点和公开挑战。最后，我们概述了神经场在机器人技术中的局限性，并为未来的研究提出了有前景的方向。项目页面：https://robonerf.github.io et.al.|[2410.20220](http://arxiv.org/abs/2410.20220)|**[link](https://github.com/zubair-irshad/Awesome-Implicit-NeRF-Robotics)**|

<p align=right>(<a href=#updated-on-20241126>back to top</a>)</p>

[contributors-shield]: https://img.shields.io/github/contributors/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[contributors-url]: https://github.com/Vincentqyw/cv-arxiv-daily/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[forks-url]: https://github.com/Vincentqyw/cv-arxiv-daily/network/members
[stars-shield]: https://img.shields.io/github/stars/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[stars-url]: https://github.com/Vincentqyw/cv-arxiv-daily/stargazers
[issues-shield]: https://img.shields.io/github/issues/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[issues-url]: https://github.com/Vincentqyw/cv-arxiv-daily/issues

