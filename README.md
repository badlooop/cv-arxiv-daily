[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]

## Updated on 2024.01.13
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
|**2024-01-09**|**Morphable Diffusion: 3D-Consistent Diffusion for Single-image Avatar Creation**|生成扩散模型的最新进展已经实现了从单个输入图像或文本提示生成3D资产的先前不可行的能力。在这项工作中，我们的目标是提高这些模型的质量和功能，以完成创建可控、照片真实感的人类化身的任务。我们通过将3D可变形模型集成到最先进的多视角一致扩散方法中来实现这一点。我们证明了生成管道在关节式3D模型上的精确调节增强了基线模型在从单个图像合成新视图任务中的性能。更重要的是，这种集成有助于将面部表情和身体姿势控制无缝准确地结合到生成过程中。据我们所知，我们提出的框架是第一个扩散模型，能够从看不见的物体的单个图像中创建完全3D一致、可动画化和照片真实感的人类化身；大量的定量和定性评估证明了我们的方法在新视角和新表情合成任务上优于现有的最先进的化身创建模型。 et.al.|[2401.04728](http://arxiv.org/abs/2401.04728)|null|
|**2024-01-07**|**See360: Novel Panoramic View Interpolation**|我们介绍了See360，它是一种使用潜在空间视点估计进行360全景插值的通用且高效的框架。大多数现有的视图渲染方法只关注室内或合成三维环境，并渲染小对象的新视图。相反，我们建议将以相机为中心的视图合成作为2D仿射变换来处理，而不使用点云或深度图，这使得能够实现有效的360？全景场景探索。给定一对参考图像，See360模型通过提出的新颖的多尺度仿射变换器（MSAT）来学习渲染新颖的视图，从而实现从粗到细的特征渲染。我们还提出了一种条件潜在空间自动编码器（C-LAE）来实现任意角度的视图插值。为了展示我们方法的多功能性，我们引入了四个训练数据集，即UrbanCity360、Archinterior360、HungHom360和Lab360，它们是从室内和室外环境中收集的，用于真实和合成渲染。实验结果表明，该方法具有足够的通用性，可以实现四个数据集任意视图的实时绘制。此外，我们的See360模型可以应用于野外的视图合成：只需很短的额外训练时间（约10分钟），并且能够渲染未知的真实世界场景。See360的卓越性能为以相机为中心的视图渲染和360全景视图插值开辟了一个很有前途的方向。 et.al.|[2401.03431](http://arxiv.org/abs/2401.03431)|**[link](https://github.com/Holmes-Alan/See360)**|
|**2024-01-06**|**RustNeRF: Robust Neural Radiance Field with Low-Quality Images**|最近在神经辐射场（NeRF）方面的工作利用了多视图三维一致性，在三维场景建模和高保真新颖视图合成方面取得了令人印象深刻的结果。然而，也有局限性。首先，现有方法假设有足够的高质量图像可用于训练NeRF模型，忽略了真实世界的图像退化。其次，由于不同视图之间未建模的不一致性，以前的方法在训练集中难以解决模糊性问题。在这项工作中，我们为真实世界的高质量NeRF提供了RustNeRF。为了提高NeRF在真实世界输入下的鲁棒性，我们训练了一个包含真实世界退化建模的3D感知预处理网络。我们提出了一种新的隐式多视图引导来解决图像退化和恢复过程中的信息丢失问题。大量实验证明了RustNeRF在实际退化情况下优于现有方法。代码将被发布。 et.al.|[2401.03257](http://arxiv.org/abs/2401.03257)|null|
|**2024-01-02**|**Street Gaussians for Modeling Dynamic Urban Scenes**|本文旨在解决从单目视频中建模动态城市街道场景的问题。最近的方法扩展了NeRF，将跟踪车辆姿态纳入车辆动画，实现了动态城市街道场景的照片逼真视图合成。然而，它们的显著局限性在于训练和渲染速度慢，再加上履带车辆姿态对高精度的迫切需求。我们介绍了Street Gaussians，一种新的明确的场景表示，它解决了所有这些限制。具体地说，动态城市街道被表示为一组点云，这些点云配备有语义logits和3D Gaussians，每一个都与前景车辆或背景相关联。为了对前景对象车辆的动力学进行建模，使用可优化的跟踪姿态以及动态外观的动态球面谐波模型对每个对象点云进行优化。显式表示允许容易地合成目标车辆和背景，这反过来又允许在半小时的训练内以133 FPS（1066 $\times$ 1600分辨率）进行场景编辑操作和渲染。所提出的方法在多个具有挑战性的基准上进行了评估，包括KITTI和Waymo Open数据集。实验表明，在所有数据集上，所提出的方法始终优于最先进的方法。此外，尽管仅依赖于现成跟踪器的姿态，但所提出的表示提供的性能与使用精确的地面实况姿态所实现的性能不相上下。代码位于https://zju3dv.github.io/street_gaussians/. et.al.|[2401.01339](http://arxiv.org/abs/2401.01339)|null|
|**2024-01-01**|**Deblurring 3D Gaussian Splatting**|最近对辐射场的研究为具有照片级真实感渲染质量的新颖视图合成铺平了坚实的道路。然而，它们通常使用神经网络和体积绘制，这两种方法的训练成本很高，并且由于绘制时间长，阻碍了它们在各种实时应用中的广泛使用。最近，人们提出了一种基于3D高斯散射的方法来对3D场景进行建模，并在实时渲染图像的同时实现了显著的视觉质量。然而，如果训练图像模糊，则渲染质量会严重下降。模糊通常是由于镜头散焦、物体运动和相机抖动而产生的，它不可避免地会干扰干净图像的获取。先前的几项研究试图使用神经场从模糊的输入图像中渲染干净清晰的图像。然而，这些工作中的大多数仅设计用于基于体积渲染的神经辐射场，并不直接适用于基于光栅化的3D高斯散射方法。因此，我们提出了一种新的实时去模糊框架，即去模糊3D高斯散点，使用小型多层感知器（MLP）来操纵每个3D高斯的协方差来对场景模糊度进行建模。虽然去模糊的3D高斯飞溅仍然可以享受实时渲染，但它可以从模糊的图像中重建精细和清晰的细节。在基准上进行了各种实验，结果表明了我们的去模糊方法的有效性。定性结果可在https://benhenryl.github.io/Deblurring-3D-Gaussian-Splatting/ et.al.|[2401.00834](http://arxiv.org/abs/2401.00834)|null|
|**2024-01-01**|**Sharp-NeRF: Grid-based Fast Deblurring Neural Radiance Fields Using Sharpness Prior**|神经辐射场（NeRF）在基于神经渲染的新视图合成中表现出了显著的性能。然而，当输入图像是在不完美的条件下拍摄的时，NeRF会遭受严重的视觉质量下降，例如照明不良、散焦模糊和透镜像差。特别是，当通常使用相机拍摄图像时，散焦模糊在图像中非常常见。尽管最近很少有研究提出渲染相当高质量的清晰图像，但它们仍然面临许多关键挑战。特别地，这些方法采用了基于多层感知器（MLP）的NeRF，这需要大量的计算时间。为了克服这些缺点，本文提出了一种新的技术Sharp-NeRF——一种基于网格的NeRF，它可以在半小时的训练内从输入的模糊图像中渲染干净清晰的图像。为此，我们使用了几个基于网格的内核来准确地对场景的清晰度/模糊度进行建模。计算像素的清晰度水平以学习空间变化的模糊核。我们在由模糊图像组成的基准上进行了实验，并评估了完全参考和非参考指标。定性和定量的结果表明，我们的方法以生动的色彩和精细的细节呈现出尖锐的新颖观点，并且它比以前的作品具有更快的训练时间。我们的项目页面位于https://benhenryl.github.io/SharpNeRF/ et.al.|[2401.00825](http://arxiv.org/abs/2401.00825)|**[link](https://github.com/benhenryl/sharpnerf)**|
|**2024-01-02**|**GD^2-NeRF: Generative Detail Compensation via GAN and Diffusion for One-shot Generalizable Neural Radiance Fields**|在本文中，我们专注于单镜头新颖视图合成（O-NVS）任务，该任务的目标是在每个场景只有一个参考图像的情况下合成照片逼真的新颖视图。先前的一次性可泛化神经辐射场（OG-NeRF）方法以无推理时间微调的方式解决了这一任务，但由于仅编码器的架构高度依赖于有限的参考图像，因此存在模糊问题。另一方面，最近的基于扩散的图像到3d方法通过将预先训练的2D扩散模型提取到3d表示中显示出生动可信的结果，但需要繁琐的逐场景优化。针对这些问题，我们提出了GD $^2$-NeRF，这是一个通过GAN和Diffusion的生成细节补偿框架，既不需要推理时间微调，又具有生动可信的细节。详细地说，遵循从粗到细的策略，GD$^2$-NeRF主要由一级并行流水线（OPP）和3D一致细节增强器（Diff3DE）组成。在粗略阶段，OPP首先将GAN模型有效地插入到现有的OG-NeRF管道中，以主要缓解从训练数据集中捕获的分布内先验的模糊问题，实现清晰度（LPIPS、FID）和保真度（PSNR、SSIM）之间的良好平衡。然后，在精细阶段，Diff3DE进一步利用预先训练的图像扩散模型来补充丰富的分布细节，同时保持良好的3D一致性。在合成数据集和真实世界数据集上进行的大量实验表明，GD$^2$ -NeRF在没有每场景微调的情况下显著改善了细节。 et.al.|[2401.00616](http://arxiv.org/abs/2401.00616)|null|
|**2023-12-28**|**iFusion: Inverting Diffusion for Pose-Free Reconstruction from Sparse Views**|我们提出了iFusion，这是一种新颖的3D对象重建框架，只需要两个具有未知相机姿态的视图。虽然单视图重建会产生视觉上吸引人的结果，但它可能会与实际对象有很大的偏差，尤其是在看不见的一侧。附加视图提高了重建保真度，但需要已知的摄影机姿势。然而，假设姿态的可用性可能是不现实的，并且现有的姿态估计器在稀疏视图场景中失败。为了解决这一问题，我们利用了一个预先训练的新颖视图合成扩散模型，该模型嵌入了关于不同对象的几何形状和外观的隐含知识。我们的策略分为三个步骤：（1）我们反转用于相机姿态估计的扩散模型，而不是合成新的视图。（2） 使用提供的视图和估计的姿态对扩散模型进行微调，使其成为为目标对象量身定制的新型视图合成器。（3） 利用配准的视图和微调的扩散模型，我们重建了3D对象。实验表明，在姿态估计和新视图合成方面都有很强的性能。此外，iFusion与各种重建方法无缝集成，并对其进行了增强。 et.al.|[2312.17250](http://arxiv.org/abs/2312.17250)|**[link](https://github.com/chinhsuanwu/ifusion)**|
|**2023-12-28**|**Spacetime Gaussian Feature Splatting for Real-Time Dynamic View Synthesis**|动态场景的新颖视图合成一直是一个有趣但具有挑战性的问题。尽管取得了最新进展，但同时实现高分辨率的真实照片效果、实时渲染和紧凑的存储仍然是一项艰巨的任务。为了应对这些挑战，我们提出了时空高斯特征飞溅作为一种新的动态场景表示，由三个关键组件组成。首先，我们通过增强具有时间不透明度和参数运动/旋转的3D高斯，来形成富有表现力的时空高斯。这使得时空高斯能够捕捉场景中的静态、动态以及瞬态内容。其次，我们介绍了飞溅特征渲染，它用神经特征代替了球面谐波。这些功能有助于在保持小尺寸的同时对视图和与时间相关的外观进行建模。第三，我们利用训练误差和粗略深度的指导，在难以与现有管道融合的区域对新的高斯采样。在几个已建立的真实世界数据集上的实验表明，我们的方法在保持紧凑存储的同时，实现了最先进的渲染质量和速度。在8K分辨率下，我们的lite版本模型可以在Nvidia RTX 4090 GPU上以60 FPS的速度渲染。 et.al.|[2312.16812](http://arxiv.org/abs/2312.16812)|null|
|**2023-12-26**|**fMPI: Fast Novel View Synthesis in the Wild with Layered Scene Representations**|在这项研究中，我们为基于分层场景表示的新视图合成（NVS）方法提出了两种新的输入处理范式，这两种方法在不影响质量的情况下显著提高了它们的运行时间。我们的方法识别并减轻了传统管道最耗时的两个方面：构建和处理所谓的平面扫描体积（PSV），这是输入相机视图的平面重新投影的高维张量。特别是，我们建议在并行组中处理该张量，以提高计算效率，并对相邻输入平面进行超采样，从而生成更密集、更准确的场景表示。所提出的增强提供了显著的灵活性，允许在性能和速度之间取得平衡，从而朝着实时应用迈出了实质性的步伐。此外，它们非常通用，因为任何基于PSV的方法都可以使用它们，包括使用多平面图像、多球体图像和分层深度图像的方法。在一组全面的实验中，我们证明了我们提出的范式能够设计出一种NVS方法，该方法在公共基准上达到最先进的水平，同时比现有的最先进的方法快50倍。它在速度方面也比目前的前辈高出3倍多，同时实现了明显更好的渲染质量。 et.al.|[2312.16109](http://arxiv.org/abs/2312.16109)|null|

<p align=right>(<a href=#updated-on-20240113>back to top</a>)</p>

## 3D Reconstruction

|Publish Date|Title|Abstract|PDF|Code|
|---|---|---|---|---|
|**2024-01-10**|**Structure from Duplicates: Neural Inverse Graphics from a Pile of Objects**|我们的世界充满了相同的物体（例如，可乐罐、同一型号的汽车）。当这些重复出现在一起时，为我们有效地推理3D提供了额外而有力的线索。受这一观察结果的启发，我们引入了“重复结构”（SfD），这是一种新颖的逆图形框架，可以从包含多个相同对象的单个图像中重建几何体、材料和照明。SfD首先识别图像中对象的多个实例，然后联合估计所有实例的6DoF姿势。随后使用反向图形管道来联合推理对象的形状、材质和环境光，同时遵守实例之间的共享几何图形和材质约束。我们的主要贡献包括利用对象副本作为单图像逆图形的鲁棒先验，并提出用于联合6-DoF对象姿态估计的平面内旋转鲁棒运动结构（SfM）公式。通过利用来自单个图像的多视图线索，SfD生成了更真实、更详细的3D重建，显著优于具有相似或更多观测值的现有单个图像重建模型和多视图重建方法。 et.al.|[2401.05236](http://arxiv.org/abs/2401.05236)|**[link](https://github.com/tianhang-cheng/sfd)**|
|**2024-01-07**|**RHOBIN Challenge: Reconstruction of Human Object Interaction**|对人与物体之间的相互作用进行建模是近年来新兴的研究方向。然而，由于严重的遮挡和复杂的动力学，捕捉人与物体的相互作用是一项非常具有挑战性的任务，这不仅需要了解三维人体姿态和物体姿态，还需要了解它们之间的相互作用。长期以来，三维人和物体的重建一直是计算机视觉中两个独立的研究领域。因此，我们提出了RHOBIN的第一个挑战：结合RHOBIN研讨会重建人-物交互。它旨在将人类和物体重建以及交互建模的研究团体聚集在一起，讨论技术和交换思想。我们的挑战包括从单目RGB图像进行3D重建的三个轨道，重点是处理具有挑战性的交互场景。我们的挑战吸引了100多名参与者，提交了300多份材料，表明了研究界的广泛兴趣。本文介绍了我们挑战赛的设置，并更详细地讨论了每条赛道的获胜方法。我们观察到，即使在严重遮挡的情况下，人类重建任务也正在变得成熟，而物体姿态估计和关节重建仍然是具有挑战性的任务。随着人们对交互建模越来越感兴趣，我们希望这份报告能提供有用的见解，并促进未来在这个方向上的研究。我们的研讨会网站位于\ href{https://rhobin-challenge.github.io/}{https://rhobin-challenge.github.io/}. et.al.|[2401.04143](http://arxiv.org/abs/2401.04143)|null|
|**2024-01-08**|**AGG: Amortized Generative 3D Gaussians for Single Image to 3D**|考虑到对自动3D内容创建管道的日益增长的需求，已经研究了各种3D表示来从单个图像生成3D对象。由于其优越的渲染效率，基于3D高斯飞溅的模型最近在3D重建和生成方面都表现出色。用于图像到3D生成的3D高斯飞溅方法通常是基于优化的，需要许多计算昂贵的分数提取步骤。为了克服这些挑战，我们引入了一种分期生成的3D高斯框架（AGG），该框架可以从单个图像中立即生成3D高斯，无需按实例优化。AGG利用中间混合表示分解3D高斯位置和其他外观属性的生成，用于联合优化。此外，我们提出了一种级联流水线，该流水线首先生成3D数据的粗略表示，然后使用3D高斯超分辨率模块对其进行上采样。我们的方法是根据现有的基于优化的3D高斯框架和利用其他3D表示的基于采样的管道进行评估的，其中AGG在质量和数量上都表现出有竞争力的生成能力，同时速度快几个数量级。项目页面：https://ir1d.github.io/AGG/ et.al.|[2401.04099](http://arxiv.org/abs/2401.04099)|null|
|**2024-01-08**|**A Survey on 3D Gaussian Splatting**|三维高斯散射（3DGS）是近年来在显式辐射场和计算机图形学领域出现的一种变革性技术。这种创新方法的特点是使用了数百万个3D高斯，这与神经辐射场（NeRF）方法有很大的不同，后者主要使用隐式的基于坐标的模型将空间坐标映射到像素值。3D GS凭借其明确的场景表示和可微分的渲染算法，不仅保证了实时渲染能力，而且引入了前所未有的控制和编辑水平。这将3D GS定位为下一代3D重建和表示的潜在游戏规则改变者。在本文中，我们首次系统地概述了3D GS领域的最新发展和关键贡献。我们首先详细探索了3D GS出现的基本原理和驱动力，为理解其意义奠定了基础。我们讨论的一个焦点是3D GS的实用性。通过促进实时性能，3D GS开辟了大量应用，从虚拟现实到交互式媒体等等。此外，还对领先的3D GS模型进行了比较分析，并在各种基准任务中进行了评估，以突出其性能和实用性。该调查的结论是确定了当前的挑战，并提出了该领域未来研究的潜在途径。通过这项调查，我们旨在为新来者和经验丰富的研究人员提供宝贵的资源，促进在适用和明确的辐射场表示方面的进一步探索和进步。 et.al.|[2401.03890](http://arxiv.org/abs/2401.03890)|null|
|**2024-01-01**|**BIBench: Benchmarking Data Analysis Knowledge of Large Language Models**|大型语言模型（LLM）已经在广泛的任务中展示了令人印象深刻的功能。然而，他们在数据分析专业领域的熟练程度和可靠性，特别是在注重数据驱动思维的情况下，仍然不确定。为了弥补这一差距，我们引入了BIBench，这是一个全面的基准测试，旨在评估商业智能（BI）背景下LLM的数据分析能力。BIBench从三个维度评估LLM：1）BI基础知识，评估模型的数字推理和对金融概念的熟悉程度；2） BI知识应用，确定模型快速理解文本信息和从多个视图生成分析问题的能力；以及3）BI技术技能，检查模型对技术知识的使用，以应对现实世界的数据分析挑战。BIBench包含11个子任务，涵盖三类任务类型：分类、提取和生成。此外，我们还开发了BIChat，这是一个具有超过一百万个数据点的特定领域数据集，用于微调LLM。我们将在\url上发布BIBenchmark、BIChat和评估脚本{https://github.com/cubenlp/BIBench}.该基准旨在为LLM能力的深入分析提供一种衡量标准，并促进LLM在数据分析领域的进步。 et.al.|[2401.02982](http://arxiv.org/abs/2401.02982)|**[link](https://github.com/cubenlp/BIBench)**|
|**2024-01-03**|**S3Net: Innovating Stereo Matching and Semantic Segmentation with a Single-Branch Semantic Stereo Network in Satellite Epipolar Imagery**|立体匹配和语义分割是双目卫星三维重建中的重要任务。然而，先前的研究主要将这些视为独立的并行任务，缺乏一个综合的多任务学习框架。本文介绍了一种解决方案，即单分支语义立体网络（S3Net），它创新地使用自融合和互融合模块将语义分割和立体匹配相结合。与之前独立利用语义或视差信息的方法不同，我们的方法识别并利用了这两个任务之间的内在联系，从而更准确地理解了语义信息和视差估计。在US3D数据集上的对比测试证明了我们的S3Net的有效性。我们的模型将语义分割中的mIoU从61.38提高到67.39，并将视差估计中的D1误差和平均端点误差（EPE）分别从10.051降低到9.579和1.439降低到1.403，超过了现有的竞争方法。我们的代码位于：https://github.com/CVEO/S3Net. et.al.|[2401.01643](http://arxiv.org/abs/2401.01643)|null|
|**2024-01-02**|**PAC-Bayesian Domain Adaptation Bounds for Multi-view learning**|本文提出了一系列在多视角学习环境中进行领域自适应的新结果。在以往的研究中，将多种观点纳入领域适应性的研究很少得到重视。通过这种方式，我们提出了用Pac贝叶斯理论分析泛化界限，以巩固目前分别处理的两种范式。首先，在Germain等人先前工作的基础上，我们利用多视图学习的概念将Germain等人提出的分布之间的距离用于领域自适应。因此，我们引入了一种新的距离，它是为多视图域自适应设置量身定制的。然后，我们给出了估计引入的散度的Pac贝叶斯界。最后，我们将不同的新边界与先前的研究进行了比较。 et.al.|[2401.01048](http://arxiv.org/abs/2401.01048)|null|
|**2023-12-29**|**Informative Rays Selection for Few-Shot Neural Radiance Fields**|神经辐射场（NeRF）最近已成为基于图像的3D重建的一种强大方法，但每个场景的漫长优化限制了其实际应用，尤其是在资源受限的环境中。现有的方法通过减少输入视图的数量并利用复杂的损失或来自其他模态的额外输入来正则化所学习的体积表示来解决这个问题。在本文中，我们提出了KeyNeRF，这是一种简单而有效的方法，通过聚焦关键信息射线，在少镜头场景中训练NeRF。这种射线首先在相机级别通过视图选择算法进行选择，该算法在保证场景覆盖的同时促进基线多样性，然后在像素级别通过基于局部图像熵的概率分布进行采样。我们的方法与最先进的方法相比表现良好，同时需要对现有NeRF代码库进行最小的更改。 et.al.|[2312.17561](http://arxiv.org/abs/2312.17561)|null|
|**2023-12-28**|**Toward Semantic Scene Understanding for Fine-Grained 3D Modeling of Plants**|由于全球人口增长以及对粮食和劳动力短缺的预期，农业机器人是一个活跃的研究领域。机器人可能有助于完成修剪、收割、表型分析和植物建模等任务。然而，农业自动化受到阻碍，因为难以在该领域创建高分辨率3D语义地图，从而实现安全操作和导航。在本文中，我们致力于解决这一问题，并展示了语义和环境先验的使用如何帮助为高粱的目标应用构建准确的3D地图。具体而言，我们1）使用高粱种子作为语义地标来构建视觉同步定位和映射（SLAM）系统，该系统使我们能够平均映射78%的高粱范围，而ORB-SLAM2的映射率为38%；和2）使用种子作为语义特征来改进由机器人手持相机拍摄的图像对完整高粱穗的3D重建。 et.al.|[2312.17110](http://arxiv.org/abs/2312.17110)|null|
|**2023-12-28**|**Geometry-Biased Transformer for Robust Multi-View 3D Human Pose Reconstruction**|我们解决了在遮挡和有限重叠视图下从多个视图估计3D人体姿态的挑战。我们将多视图、单人三维人体姿态重建作为一个回归问题，并提出了一种新的编码器-解码器-转换器架构，用于从多视图二维姿态序列中估计三维姿态。编码器对在不同视图和时间检测到的2D骨骼关节进行细化，通过全局自关注融合多视图和时间信息。我们通过结合有几何偏见的注意力机制来增强编码器，有效地利用视图之间的几何关系。此外，我们使用2D姿势检测器提供的检测分数来基于2D检测的可靠性进一步引导编码器的注意力。解码器随后使用针对每个关节的预定义查询，从这些细化的标记回归3D姿势序列。为了增强我们的方法对看不见的场景的泛化能力，并提高对缺失关节的恢复能力，我们实施了包括场景居中、合成视图和标记丢弃在内的策略。我们在三个基准公共数据集Human3.6M、CMU Panoptic和Occlusion Persons上进行了广泛的实验。我们的结果证明了我们的方法的有效性，特别是在遮挡场景和视图很少的情况下，这对于基于三角测量的方法来说是传统上具有挑战性的场景。 et.al.|[2312.17106](http://arxiv.org/abs/2312.17106)|null|

<p align=right>(<a href=#updated-on-20240113>back to top</a>)</p>

## Diffusion

|Publish Date|Title|Abstract|PDF|Code|
|---|---|---|---|---|
|**2024-01-10**|**InseRF: Text-Driven Generative Object Insertion in Neural 3D Scenes**|我们介绍了一种在3D场景的NeRF重建中插入生成对象的新方法InseRF。InseRF基于用户提供的文本描述和参考视点中的二维边界框，在三维场景中生成新对象。最近，由于在3D生成建模中使用了文本到图像扩散模型的强先验，3D场景编辑的方法已经发生了深刻的转变。现有方法在通过样式和外观更改或删除现有对象来编辑三维场景时最有效。然而，生成新对象仍然是这种方法的一个挑战，我们在本研究中对此进行了讨论。具体地，我们建议将3D对象插入固定到场景的参考视图中的2D对象插入。然后使用单视图对象重建方法将2D编辑提升到3D。然后，在单目深度估计方法的先验的引导下，将重建的对象插入到场景中。我们在各种3D场景上评估了我们的方法，并对所提出的组件进行了深入分析。我们在几个3D场景中生成插入对象的实验表明，与现有方法相比，我们的方法是有效的。InseRF能够在不需要明确的3D信息作为输入的情况下进行可控和3D一致的对象插入。请访问我们的项目页面https://mohamad-shahbazi.github.io/inserf. et.al.|[2401.05335](http://arxiv.org/abs/2401.05335)|null|
|**2024-01-10**|**Score Distillation Sampling with Learned Manifold Corrective**|分数蒸馏采样（SDS）是一种最近但已经广泛流行的方法，它依赖于图像扩散模型来使用文本提示控制优化问题。在本文中，我们对SDS损失函数进行了深入分析，确定了其公式中的一个固有问题，并提出了一个令人惊讶的简单但有效的解决方案。具体来说，我们将损失分解为不同的因素，并分离出导致噪声梯度的分量。在最初的配方中，使用了高文本指导来解释噪音，导致了不必要的副作用。相反，我们模拟图像扩散模型的时间步长相关去噪缺陷来训练浅层网络，以便有效地将其排除在外。我们通过几个定性和定量实验证明了我们新的损失公式的多功能性和有效性，包括基于优化的图像合成和编辑、零样本图像翻译网络训练和文本到3D合成。 et.al.|[2401.05293](http://arxiv.org/abs/2401.05293)|null|
|**2024-01-10**|**diffSph: a Python tool to compute diffuse signals from dwarf spheroidal galaxies**|到目前为止，还没有观测到银河系矮球状卫星的散射发射。考虑到矮星系主要由暗物质组成，这些信号的发现可能为理解暗物质的性质提供有价值的见解。我们介绍了“diffSph”，这是一种Python工具，在其当前版本中，它可以快速预测射频中的这种散射信号。它还具有一个非常全面的模块，用于计算与使用伽马射线间接探测暗物质相关的“J”和“D”因子。例程与最先进的运动学拟合中的部分子簇射算法和暗物质晕质量函数相耦合。该代码也有助于测试关于矮星系中宇宙射线电子/正电子源的一般假设（不一定与任何候选暗物质有关）。diffSph工具已经被用于使用LOw频率ARray（LOFAR）搜索矮球状星系的散射信号。 et.al.|[2401.05255](http://arxiv.org/abs/2401.05255)|**[link](https://github.com/mertio1/diffsph)**|
|**2024-01-10**|**PIXART-δ: Fast and Controllable Image Generation with Latent Consistency Models**|本技术报告介绍了PIXART-｛\delta｝，这是一种文本到图像合成框架，将潜在一致性模型（LCM）和ControlNet集成到高级PIXART-｛\alpha｝模型中。PIXART-｛\alpha｝因其通过非常有效的训练过程生成1024px分辨率的高质量图像的能力而受到认可。在PIXART-｛\delta｝中集成LCM显著加快了推理速度，仅需2-4步即可生成高质量图像。值得注意的是，PIXART-｛\delta｝在生成1024x1024像素图像方面实现了0.5秒的突破，这标志着比PIXART-｛\alpha｝提高了7倍。此外，PIXART-｛\delta｝被设计为可在一天内在32GB V100 GPU上有效训练。凭借其8位推理能力（von Platen et al.，2023），PIXART-｛\delta｝可以在8GB GPU内存限制内合成1024px的图像，大大提高了其可用性和可访问性。此外，结合类似ControlNet的模块可以实现对文本到图像扩散模型的细粒度控制。我们引入了一种新颖的ControlNet Transformer架构，专门为变压器量身定制，在生成高质量图像的同时实现了明确的可控性。作为一种最先进的开源图像生成模型，PIXART-｛\delta｝为稳定扩散模型家族提供了一种很有前途的替代方案，对文本到图像的合成做出了重大贡献。 et.al.|[2401.05252](http://arxiv.org/abs/2401.05252)|**[link](https://github.com/PixArt-alpha/PixArt-alpha)**|
|**2024-01-10**|**Escape from textured adsorbing surfaces**|尽管粘性颗粒从纹理表面逃逸的动力学在各个科学和技术领域都很重要，但人们对其了解甚少。在这项工作中，我们通过研究吸附质从普遍的表面形貌（包括孔/坑、柱和凹槽）中的逃逸时间来应对这一挑战。导出了概率密度函数和逃逸时间平均值的解析表达式。一个特别有趣的场景是地表内非常深和狭窄的封闭空间。在这种情况下，截留和粘性的共同作用延长了逸出时间，导致有效解吸速率显著低于未编织表面的解吸速率。该速率符合一个普遍的标度定律，该定律将吸附的平衡常数与相关的限制长度标度相耦合。虽然我们的结果是分析性的和精确的，但我们也基于一维扩散的有效描述，提出了深腔和窄腔的近似值，一维扩散被静止的吸附事件打断。这种简单且物理激励的近似在其有效范围内提供了高精度的预测，并且即使对于中等深度的空腔也相对良好地工作。所有的理论结果都得到了大量蒙特卡罗模拟的证实。 et.al.|[2401.05227](http://arxiv.org/abs/2401.05227)|null|
|**2024-01-10**|**Existence of global weak solutions to a Cahn-Hilliard cross-diffusion system in lymphangiogenesis**|在无通量边界条件的有界域上，证明了具有奇异势的退化Cahn-Hillard交叉扩散系统弱解的全局时间存在性。该模型由两个耦合的抛物型四阶偏微分方程组成，描述了纤维相体积分数和溶质浓度的演变，对淋巴管形态的预图案化进行了建模。如果这一点最初成立，则纤维相分数满足偏析性质。存在性证明基于三级近似方案和来自能量和熵不等式的先验估计。当自由能在时间上不增加时，由于交叉扩散耦合，熵只有界。 et.al.|[2401.05180](http://arxiv.org/abs/2401.05180)|null|
|**2024-01-10**|**Derm-T2IM: Harnessing Synthetic Skin Lesion Data via Stable Diffusion Models for Enhanced Skin Disease Classification using ViT and CNN**|本研究探讨了利用通过稳定扩散模型生成的皮肤镜合成数据作为增强机器学习模型训练稳健性的策略。合成数据生成在缓解与有限标记数据集相关的挑战方面发挥着关键作用，从而促进更有效的模型训练。在这种情况下，我们的目标是通过扩展最近在文本到图像潜在扩散模型中的少量镜头学习和少量数据表示的成功，来结合增强的数据转换技术。优化后的模型进一步用于渲染具有多样性和真实性特征的高质量皮肤损伤合成数据，为现有的训练数据提供了有价值的补充和多样性。我们研究了将新生成的合成数据纳入最先进的机器学习模型的训练管道的影响，评估其在增强模型性能和对看不见的真实世界数据的泛化方面的有效性。我们的实验结果表明，通过稳定扩散模型生成的合成数据的有效性有助于提高端到端CNN和视觉转换器模型在两个不同的真实世界皮肤损伤数据集上的稳健性和适应性。 et.al.|[2401.05159](http://arxiv.org/abs/2401.05159)|null|
|**2024-01-10**|**CrossDiff: Exploring Self-Supervised Representation of Pansharpening via Cross-Predictive Diffusion Model**|全色（PAN）图像和相应的多光谱（MS）图像的融合也被称为泛锐化，旨在将PAN的丰富空间细节和MS的光谱信息相结合。由于缺乏高分辨率的MS图像，可用的基于深度学习的方法通常遵循低分辨率训练和全分辨率测试的模式。当将原始MS和PAN图像作为输入时，由于尺度变化，它们总是获得次优结果。在本文中，我们建议通过设计一个名为CrossDiff的交叉预测扩散模型来探索泛锐化的自监督表示。它有两个阶段的训练。在第一阶段，我们引入了一个基于条件DDPM的交叉预测借口任务来预训练UNet结构，而在第二阶段，UNet的编码器被冻结以直接从PAN和MS中提取空间和光谱特征，并且仅训练融合头来适应泛锐化任务。大量实验表明，与最先进的有监督和无监督方法相比，所提出的模型具有有效性和优越性。此外，交叉传感器实验还验证了所提出的自监督表示学习器对其他卫星数据集的泛化能力。我们将发布我们的代码以实现再现性。 et.al.|[2401.05153](http://arxiv.org/abs/2401.05153)|null|
|**2024-01-10**|**Disorder-induced enhancement of lithium-ion transport in solid-state electrolytes**|增强固体电解质中的离子传导对于开发高性能全固态锂离子电池至关重要。硫代磷酸锂是最有前途的固体电解质之一，因为它们在室温下表现出超离子导电性。然而，缺乏对其离子传导机制的全面了解，特别是结构紊乱对离子传导的影响，是一个长期存在的问题，限制了全固态LIBs的进一步创新。在这里，我们通过建立和使用深度学习潜力来模拟具有不同无序水平的Li3PS4电解质系统来应对这一挑战。结果表明，无序驱动的扩散动力学显著提高了室温电导率。我们通过应用称为“柔软度”的基于机器学习的结构指纹，进一步在动力学特征、局部结构特征和原子重排之间建立了桥梁。该度量允许对无序诱导的“软”跳跃锂离子进行分类。我们的发现为复杂无序结构中的离子传导机制提供了见解，从而有助于开发用于LIBs的优质固态电解质。 et.al.|[2401.05151](http://arxiv.org/abs/2401.05151)|null|
|**2024-01-10**|**Self-similar solutions for the non-equilibrium nonlinear supersonic Marshak wave problem**|给出了具有时变辐射驱动源的非线性非平衡Marshak波问题的相似解。所使用的辐射传输模型是超音速区域中的灰色非平衡扩散近似。这些解构成了现有的线性非平衡超声速Marshak波解到非线性区域的扩展，非线性区域在现实的高能量密度系统中普遍存在。广义解假设材料模型具有幂律温度相关的不透明性和与辐射能量密度成比例的材料能量密度，以及服从时间幂律的表面辐射温度驱动。对这些解进行了详细的分析，结果表明，根据不透明度指数的值，它们在性质上采取了各种不同的形式。这些解决方案用于构建一组超声速非平衡辐射传热的标准化基准，这些基准虽然不平凡，但实施起来很简单。将这些解决方案与隐式蒙特卡罗和离散纵坐标输运模拟以及灰色扩散模拟进行了详细比较，显示出良好的一致性，这证明了这些解决方案作为代码验证测试问题的有用性。 et.al.|[2401.05138](http://arxiv.org/abs/2401.05138)|null|

<p align=right>(<a href=#updated-on-20240113>back to top</a>)</p>

## NeRF

|Publish Date|Title|Abstract|PDF|Code|
|---|---|---|---|---|
|**2024-01-05**|**Denoising Vision Transformers**|我们深入研究了视觉转换器（ViTs）固有的一个细微但重大的挑战：这些模型的特征图显示出网格状的伪影，这对ViTs在下游任务中的性能造成了不利影响。我们的研究将这个基本问题追溯到输入阶段的位置嵌入。为了解决这一问题，我们提出了一种新的噪声模型，该模型普遍适用于所有的ViT。具体来说，噪声模型将ViT输出分解为三个部分：一个没有噪声伪影的语义术语和两个以像素位置为条件的伪影相关术语。这种分解是通过在每幅图像的基础上加强与神经场的交叉视图特征一致性来实现的。这种逐图像优化过程从原始ViT输出中提取无伪影特征，为离线应用程序提供干净的特征。扩大了我们的解决方案的范围，以支持在线功能，我们引入了一种可学习的去噪器，直接从未处理的ViT输出中预测无伪影特征，这显示出对新数据的显著泛化能力，而无需对每张图像进行优化。我们的两阶段方法，称为去噪视觉转换器（DVT），不需要重新训练现有的预先训练的ViT，并且立即适用于任何基于转换器的架构。我们在各种具有代表性的ViT（DINO、MAE、DeiT III、EVA02、CLIP、DINOv2、DINOv2-reg）上评估了我们的方法。广泛的评估表明，我们的DVT在多个数据集（例如+3.84mIoU）的语义和几何任务中持续显著地改进了现有的最先进的通用模型。我们希望我们的研究将鼓励对ViT设计进行重新评估，特别是关于位置嵌入的天真使用。 et.al.|[2401.02957](http://arxiv.org/abs/2401.02957)|null|
|**2023-12-30**|**PlanarNeRF: Online Learning of Planar Primitives with Neural Radiance Fields**|从视觉数据中识别空间完整的平面基元是计算机视觉中的一项关键任务。现有的方法在很大程度上局限于2D片段恢复或简化3D结构，即使具有广泛的平面注释。我们提出了PlanarNeRF，这是一种能够通过在线学习检测密集3D平面的新框架。PlanarNeRF利用神经场表示，带来了三个主要贡献。首先，它利用并行的外观和几何知识增强了三维平面检测。其次，提出了一种轻量级的平面拟合模块来估计平面参数。第三，引入了一种具有更新机制的新的全局内存库结构，确保了跨帧一致性。PlanarNeRF的灵活架构使其能够在二维监督和自监督解决方案中发挥作用，在每种解决方案中，它都可以有效地从稀疏的训练信号中学习，显著提高训练效率。通过广泛的实验，我们证明了PlanarNeRF在各种场景下的有效性，并比现有工作有了显著的改进。 et.al.|[2401.00871](http://arxiv.org/abs/2401.00871)|null|
|**2024-01-01**|**Deblurring 3D Gaussian Splatting**|最近对辐射场的研究为具有照片级真实感渲染质量的新颖视图合成铺平了坚实的道路。然而，它们通常使用神经网络和体积绘制，这两种方法的训练成本很高，并且由于绘制时间长，阻碍了它们在各种实时应用中的广泛使用。最近，人们提出了一种基于3D高斯散射的方法来对3D场景进行建模，并在实时渲染图像的同时实现了显著的视觉质量。然而，如果训练图像模糊，则渲染质量会严重下降。模糊通常是由于镜头散焦、物体运动和相机抖动而产生的，它不可避免地会干扰干净图像的获取。先前的几项研究试图使用神经场从模糊的输入图像中渲染干净清晰的图像。然而，这些工作中的大多数仅设计用于基于体积渲染的神经辐射场，并不直接适用于基于光栅化的3D高斯散射方法。因此，我们提出了一种新的实时去模糊框架，即去模糊3D高斯散点，使用小型多层感知器（MLP）来操纵每个3D高斯的协方差来对场景模糊度进行建模。虽然去模糊的3D高斯飞溅仍然可以享受实时渲染，但它可以从模糊的图像中重建精细和清晰的细节。在基准上进行了各种实验，结果表明了我们的去模糊方法的有效性。定性结果可在https://benhenryl.github.io/Deblurring-3D-Gaussian-Splatting/ et.al.|[2401.00834](http://arxiv.org/abs/2401.00834)|null|
|**2023-12-22**|**Fluid Simulation on Neural Flow Maps**|我们介绍了神经流图，这是一种新的模拟方法，将新兴的隐式神经表示范式与基于流图理论的流体模拟相结合，以实现最先进的无粘流体现象模拟。我们设计了一种新的混合神经场表示，空间稀疏神经场（SSNF），它将小型神经网络与重叠、多分辨率和空间稀疏网格的金字塔相融合，以高精度紧凑地表示长期时空速度场。有了这个神经速度缓冲器，我们以机械对称的方式计算长期双向流图及其雅可比矩阵，以促进对现有解决方案的大幅精度提高。这些长程双向流图实现了低耗散的高平流精度，进而促进了高保真度的不可压缩流模拟，显示了复杂的旋涡结构。我们展示了我们的神经流体模拟在各种具有挑战性的模拟场景中的有效性，包括跳跃涡流、碰撞涡流、涡流重新连接，以及移动障碍物和密度差异产生的涡流。我们的例子表明，在能量守恒、视觉复杂性、对实验观测的遵守以及详细旋涡结构的保存方面，与现有方法相比，性能有所提高。 et.al.|[2312.14635](http://arxiv.org/abs/2312.14635)|null|
|**2023-12-21**|**Geometric Awareness in Neural Fields for 3D Human Registration**|将模板与三维人体点云对齐是一个长期存在的问题，对于动画、重建和启用监督学习管道等任务至关重要。最近的数据驱动方法利用了预测的表面对应关系；然而，它们对不同的姿态或分布并不鲁棒。相比之下，工业解决方案往往依赖于昂贵的手动注释或多视图捕获系统。最近，神经场已经显示出有希望的结果，但它们纯粹的数据驱动性质缺乏几何意识，通常导致模板配准的微小错位。在这项工作中，我们提出了两种解决方案：LoVD，一种新的神经场模型，它预测朝向目标表面上的局部SMPL顶点的方向；和INT，这是第一个专门用于神经领域的自监督任务，在测试时，它利用目标几何结构来细化主干。我们将它们组合到INLoVD中，这是一个在大型MoCap数据集上训练的强大的3D人体注册管道。INLoVD是高效的（不到一分钟），在公共基准上稳定地达到了最先进的水平，并对分布外的数据提供了前所未有的概括。我们将在\url｛url｝中发布代码和检查点。 et.al.|[2312.14024](http://arxiv.org/abs/2312.14024)|null|
|**2023-12-20**|**Neural feels with neural fields: Visuo-tactile perception for in-hand manipulation**|为了实现人类水平的灵活性，机器人必须从多模式感知推断空间意识，以推理接触互动。在新物体的手操作过程中，这种空间意识包括估计物体的姿势和形状。手内感知的现状主要采用视觉，并局限于跟踪先验已知对象。此外，在操作过程中，手上物体的视觉遮挡迫在眉睫，这阻止了当前系统在没有遮挡的情况下超越任务。我们将多指手的视觉和触摸传感相结合，在手内操作过程中估计物体的姿势和形状。我们的方法NeuralFeels通过在线学习神经场来编码对象几何，并通过优化姿态图问题来联合跟踪它。我们研究了模拟和现实世界中的多模式手部感知，通过本体感觉驱动的策略与不同的物体进行交互。我们的实验显示，使用已知的CAD模型，最终重建F分数为 $81$%，平均姿势漂移为$4.7\，\text｛mm｝$，进一步降低到$2.3\，\text{mm｝$。此外，我们观察到，与仅使用视觉的方法相比，在严重的视觉遮挡下，我们可以实现高达94$ %的跟踪改进。我们的研究结果表明，在手部操作过程中，触摸至少可以改善视觉估计，并在最好的情况下消除视觉估计的歧义。我们发布了70个实验的评估数据集FeelSight，作为在该领域进行基准测试的一步。我们由多模态感知驱动的神经表示可以作为提高机器人灵活性的感知支柱。视频可以在我们的项目网站上找到https://suddhu.github.io/neural-feels/ et.al.|[2312.13469](http://arxiv.org/abs/2312.13469)|null|
|**2023-12-20**|**Deep Learning on 3D Neural Fields**|近年来，神经场（NFs）已成为编码各种连续信号（如图像、视频、音频和3D形状）的有效工具。当应用于3D数据时，NFs提供了一种解决方案来解决与流行的离散表示相关的碎片化和局限性。然而，鉴于神经网络本质上是神经网络，目前尚不清楚它们是否以及如何无缝集成到深度学习管道中，以解决下游任务。本文解决了这一研究问题，并介绍了nf2vec，这是一个能够在单个推理过程中为输入NF生成紧凑的潜在表示的框架，同时专门处理NFs。我们在几个用于表示3D曲面的NFs上测试了这个框架，例如无符号/有符号距离和占用字段。此外，我们用更复杂的NFs证明了我们的方法的有效性，这些NFs包括3D对象的几何形状和外观，如神经辐射场。 et.al.|[2312.13277](http://arxiv.org/abs/2312.13277)|null|
|**2023-12-16**|**How to Train Neural Field Representations: A Comprehensive Study and Benchmark**|神经场（NeFs）最近已成为一种用于对各种模态（包括图像、形状和场景）的信号进行建模的通用方法。随后，许多工作探索了使用NeF作为下游任务的表示，例如，根据适合的NeF的参数对图像进行分类。然而，NeF超参数对其作为下游表示的质量的影响很少被理解，而且在很大程度上仍未被探索。这在一定程度上是由于拟合神经场数据集所需的大量时间造成的。在这项工作中，我们提出了 $\verb|fit-a-nef|$ ，这是一个基于JAX的库，它利用并行化来实现大规模nef数据集的快速优化，从而显著加快速度。有了这个库，我们进行了一项全面的研究，研究了不同超参数——包括初始化、网络架构和优化策略——对下游任务的NeF拟合的影响。我们的研究为如何训练NeF提供了宝贵的见解，并为优化其在下游应用中的有效性提供了指导。最后，基于所提出的库和我们的分析，我们提出了Neural Field Arena，这是一个由流行视觉数据集的神经场变体组成的基准，包括MNIST、CIFAR、ImageNet和ShapeNetv2的变体。我们的图书馆和神经领域竞技场将是开源的，以引入标准化的基准测试，并促进对神经领域的进一步研究。 et.al.|[2312.10531](http://arxiv.org/abs/2312.10531)|**[link](https://github.com/samuelepapa/fit-a-nef)**|
|**2023-12-18**|**LatentEditor: Text Driven Local Editing of 3D Scenes**|虽然神经领域在视图合成和场景重建方面取得了重大进展，但由于其对来自多视图输入的几何和纹理信息的隐式编码，编辑它们带来了巨大的挑战。在本文中，我们介绍了\textsc｛LatentEditor｝，这是一个创新的框架，旨在让用户能够使用文本提示对神经字段进行精确和本地控制的编辑。利用去噪扩散模型，我们成功地将真实世界的场景嵌入到潜在空间中，与传统方法相比，产生了更快、更具适应性的NeRF主干进行编辑。为了提高编辑精度，我们引入了一个delta分数来计算潜在空间中的2D掩模，该分数可以作为局部修改的指南，同时保留不相关的区域。我们新颖的像素级评分方法利用InstructPix2Pix（IP2P）的能力来辨别潜在空间中IP2P条件和无条件噪声预测之间的差异。然后在训练集中迭代地更新以2D掩码为条件的编辑的潜伏时间，以实现3D局部编辑。与现有的3D编辑模型相比，我们的方法实现了更快的编辑速度和卓越的输出质量，弥合了文本指令和潜在空间中高质量3D场景编辑之间的差距。我们在LLFF、IN2N、NeRFStudio和NeRFArt四个基准3D数据集上展示了我们的方法的优势。 et.al.|[2312.09313](http://arxiv.org/abs/2312.09313)|**[link](https://github.com/umarkhalidAI/LatentEditor)**|
|**2023-12-14**|**ZeroRF: Fast Sparse View 360° Reconstruction with Zero Pretraining**|我们提出了ZeroRF，这是一种新的每场景优化方法，解决了神经场表示中稀疏视图360重建的挑战。目前的突破，如神经辐射场（NeRF）已经证明了高保真度的图像合成，但难以处理稀疏的输入视图。现有的方法，如可泛化的NeRF和每场景优化方法，在数据依赖性、计算成本和跨不同场景的泛化方面面临限制。为了克服这些挑战，我们提出了ZeroRF，其关键思想是将定制的深度图像先验集成到因子分解的NeRF表示中。与传统方法不同，ZeroRF使用神经网络生成器对特征网格进行参数化，从而实现高效的稀疏视图360重建，而无需任何预训练或额外的正则化。大量实验展示了ZeroRF在质量和速度方面的多功能性和优势，在基准数据集上取得了最先进的结果。ZeroRF的意义延伸到3D内容生成和编辑的应用。项目页面：https://sarahweiii.github.io/zerorf/ et.al.|[2312.09249](http://arxiv.org/abs/2312.09249)|null|

<p align=right>(<a href=#updated-on-20240113>back to top</a>)</p>

[contributors-shield]: https://img.shields.io/github/contributors/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[contributors-url]: https://github.com/Vincentqyw/cv-arxiv-daily/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[forks-url]: https://github.com/Vincentqyw/cv-arxiv-daily/network/members
[stars-shield]: https://img.shields.io/github/stars/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[stars-url]: https://github.com/Vincentqyw/cv-arxiv-daily/stargazers
[issues-shield]: https://img.shields.io/github/issues/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[issues-url]: https://github.com/Vincentqyw/cv-arxiv-daily/issues

