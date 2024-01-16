[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]

## Updated on 2024.01.16
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
|**2024-01-11**|**TRIPS: Trilinear Point Splatting for Real-Time Radiance Field Rendering**|基于点的辐射场渲染在新颖的视图合成中表现出了令人印象深刻的结果，提供了令人信服的渲染质量和计算效率的结合。然而，这一领域的最新方法也并非没有缺点。3D高斯飞溅[Kerbl和Kopanas等人2023]在渲染高度详细的场景时，由于模糊和模糊的伪影，会遇到困难。另一方面ADOP[R\“uckert et al.2022]可以容纳更清晰的图像，但神经重建网络会降低性能，它会处理时间不稳定性，并且无法有效地解决点云中的大间隙。在本文中，我们提出了TRIPS（Trilinear point Splatting），一种结合了Gaussian Splatting和ADOP思想的方法。我们的新技术背后的基本概念包括将点光栅化为屏幕空间图像金字塔，金字塔层的选择由投影点的大小决定。这种方法允许使用单个三线性写入来渲染任意大的点。然后使用轻量级神经网络来重建包括超出飞溅分辨率的细节的无孔图像。重要的是，我们的渲染管道是完全可微分的，允许点大小和位置的自动优化。我们的评估表明，TRIPS在渲染质量方面超过了现有的最先进的方法，同时在现成的硬件上保持了每秒60帧的实时帧速率。这种性能扩展到具有挑战性的场景，例如具有复杂几何形状、广阔景观和自动曝光镜头的场景。 et.al.|[2401.06003](http://arxiv.org/abs/2401.06003)|null|
|**2024-01-10**|**Diffusion Priors for Dynamic View Synthesis from Monocular Videos**|动态新颖视图合成旨在捕捉视频中视觉内容的时间演变。现有的方法很难区分运动和结构，特别是在相机姿态与对象运动相比未知或受约束的情况下。此外，仅使用来自参考图像的信息，对在给定视频中被遮挡或部分观察到的看不见的区域产生幻觉是极具挑战性的。为了解决这些问题，我们首先使用定制技术在视频帧上微调预训练的RGB-D扩散模型。随后，我们将微调模型中的知识提取为包括动态和静态神经辐射场（NeRF）分量的4D表示。所提出的流水线在保持场景同一性的同时实现了几何一致性。我们进行了深入的实验，以定性和定量地评估所提出方法的有效性。我们的结果证明了我们的方法在具有挑战性的情况下的稳健性和实用性，进一步推进了动态新视图合成。 et.al.|[2401.05583](http://arxiv.org/abs/2401.05583)|null|
|**2024-01-09**|**Morphable Diffusion: 3D-Consistent Diffusion for Single-image Avatar Creation**|生成扩散模型的最新进展已经实现了从单个输入图像或文本提示生成3D资产的先前不可行的能力。在这项工作中，我们的目标是提高这些模型的质量和功能，以完成创建可控、照片真实感的人类化身的任务。我们通过将3D可变形模型集成到最先进的多视角一致扩散方法中来实现这一点。我们证明了生成管道在关节式3D模型上的精确调节增强了基线模型在从单个图像合成新视图任务中的性能。更重要的是，这种集成有助于将面部表情和身体姿势控制无缝准确地结合到生成过程中。据我们所知，我们提出的框架是第一个扩散模型，能够从看不见的物体的单个图像中创建完全3D一致、可动画化和照片真实感的人类化身；大量的定量和定性评估证明了我们的方法在新视角和新表情合成任务上优于现有的最先进的化身创建模型。 et.al.|[2401.04728](http://arxiv.org/abs/2401.04728)|null|
|**2024-01-07**|**See360: Novel Panoramic View Interpolation**|我们介绍了See360，它是一种使用潜在空间视点估计进行360全景插值的通用且高效的框架。大多数现有的视图渲染方法只关注室内或合成三维环境，并渲染小对象的新视图。相反，我们建议将以相机为中心的视图合成作为2D仿射变换来处理，而不使用点云或深度图，这使得能够实现有效的360？全景场景探索。给定一对参考图像，See360模型通过提出的新颖的多尺度仿射变换器（MSAT）来学习渲染新颖的视图，从而实现从粗到细的特征渲染。我们还提出了一种条件潜在空间自动编码器（C-LAE）来实现任意角度的视图插值。为了展示我们方法的多功能性，我们引入了四个训练数据集，即UrbanCity360、Archinterior360、HungHom360和Lab360，它们是从室内和室外环境中收集的，用于真实和合成渲染。实验结果表明，该方法具有足够的通用性，可以实现四个数据集任意视图的实时绘制。此外，我们的See360模型可以应用于野外的视图合成：只需很短的额外训练时间（约10分钟），并且能够渲染未知的真实世界场景。See360的卓越性能为以相机为中心的视图渲染和360全景视图插值开辟了一个很有前途的方向。 et.al.|[2401.03431](http://arxiv.org/abs/2401.03431)|**[link](https://github.com/Holmes-Alan/See360)**|
|**2024-01-06**|**RustNeRF: Robust Neural Radiance Field with Low-Quality Images**|最近在神经辐射场（NeRF）方面的工作利用了多视图三维一致性，在三维场景建模和高保真新颖视图合成方面取得了令人印象深刻的结果。然而，也有局限性。首先，现有方法假设有足够的高质量图像可用于训练NeRF模型，忽略了真实世界的图像退化。其次，由于不同视图之间未建模的不一致性，以前的方法在训练集中难以解决模糊性问题。在这项工作中，我们为真实世界的高质量NeRF提供了RustNeRF。为了提高NeRF在真实世界输入下的鲁棒性，我们训练了一个包含真实世界退化建模的3D感知预处理网络。我们提出了一种新的隐式多视图引导来解决图像退化和恢复过程中的信息丢失问题。大量实验证明了RustNeRF在实际退化情况下优于现有方法。代码将被发布。 et.al.|[2401.03257](http://arxiv.org/abs/2401.03257)|null|
|**2024-01-02**|**Street Gaussians for Modeling Dynamic Urban Scenes**|本文旨在解决从单目视频中建模动态城市街道场景的问题。最近的方法扩展了NeRF，将跟踪车辆姿态纳入车辆动画，实现了动态城市街道场景的照片逼真视图合成。然而，它们的显著局限性在于训练和渲染速度慢，再加上履带车辆姿态对高精度的迫切需求。我们介绍了Street Gaussians，一种新的明确的场景表示，它解决了所有这些限制。具体地说，动态城市街道被表示为一组点云，这些点云配备有语义logits和3D Gaussians，每一个都与前景车辆或背景相关联。为了对前景对象车辆的动力学进行建模，使用可优化的跟踪姿态以及动态外观的动态球面谐波模型对每个对象点云进行优化。显式表示允许容易地合成目标车辆和背景，这反过来又允许在半小时的训练内以133 FPS（1066 $\times$ 1600分辨率）进行场景编辑操作和渲染。所提出的方法在多个具有挑战性的基准上进行了评估，包括KITTI和Waymo Open数据集。实验表明，在所有数据集上，所提出的方法始终优于最先进的方法。此外，尽管仅依赖于现成跟踪器的姿态，但所提出的表示提供的性能与使用精确的地面实况姿态所实现的性能不相上下。代码位于https://zju3dv.github.io/street_gaussians/. et.al.|[2401.01339](http://arxiv.org/abs/2401.01339)|null|
|**2024-01-01**|**Deblurring 3D Gaussian Splatting**|最近对辐射场的研究为具有照片级真实感渲染质量的新颖视图合成铺平了坚实的道路。然而，它们通常使用神经网络和体积绘制，这两种方法的训练成本很高，并且由于绘制时间长，阻碍了它们在各种实时应用中的广泛使用。最近，人们提出了一种基于3D高斯散射的方法来对3D场景进行建模，并在实时渲染图像的同时实现了显著的视觉质量。然而，如果训练图像模糊，则渲染质量会严重下降。模糊通常是由于镜头散焦、物体运动和相机抖动而产生的，它不可避免地会干扰干净图像的获取。先前的几项研究试图使用神经场从模糊的输入图像中渲染干净清晰的图像。然而，这些工作中的大多数仅设计用于基于体积渲染的神经辐射场，并不直接适用于基于光栅化的3D高斯散射方法。因此，我们提出了一种新的实时去模糊框架，即去模糊3D高斯散点，使用小型多层感知器（MLP）来操纵每个3D高斯的协方差来对场景模糊度进行建模。虽然去模糊的3D高斯飞溅仍然可以享受实时渲染，但它可以从模糊的图像中重建精细和清晰的细节。在基准上进行了各种实验，结果表明了我们的去模糊方法的有效性。定性结果可在https://benhenryl.github.io/Deblurring-3D-Gaussian-Splatting/ et.al.|[2401.00834](http://arxiv.org/abs/2401.00834)|null|
|**2024-01-01**|**Sharp-NeRF: Grid-based Fast Deblurring Neural Radiance Fields Using Sharpness Prior**|神经辐射场（NeRF）在基于神经渲染的新视图合成中表现出了显著的性能。然而，当输入图像是在不完美的条件下拍摄的时，NeRF会遭受严重的视觉质量下降，例如照明不良、散焦模糊和透镜像差。特别是，当通常使用相机拍摄图像时，散焦模糊在图像中非常常见。尽管最近很少有研究提出渲染相当高质量的清晰图像，但它们仍然面临许多关键挑战。特别地，这些方法采用了基于多层感知器（MLP）的NeRF，这需要大量的计算时间。为了克服这些缺点，本文提出了一种新的技术Sharp-NeRF——一种基于网格的NeRF，它可以在半小时的训练内从输入的模糊图像中渲染干净清晰的图像。为此，我们使用了几个基于网格的内核来准确地对场景的清晰度/模糊度进行建模。计算像素的清晰度水平以学习空间变化的模糊核。我们在由模糊图像组成的基准上进行了实验，并评估了完全参考和非参考指标。定性和定量的结果表明，我们的方法以生动的色彩和精细的细节呈现出尖锐的新颖观点，并且它比以前的作品具有更快的训练时间。我们的项目页面位于https://benhenryl.github.io/SharpNeRF/ et.al.|[2401.00825](http://arxiv.org/abs/2401.00825)|**[link](https://github.com/benhenryl/sharpnerf)**|
|**2024-01-02**|**GD^2-NeRF: Generative Detail Compensation via GAN and Diffusion for One-shot Generalizable Neural Radiance Fields**|在本文中，我们专注于单镜头新颖视图合成（O-NVS）任务，该任务的目标是在每个场景只有一个参考图像的情况下合成照片逼真的新颖视图。先前的一次性可泛化神经辐射场（OG-NeRF）方法以无推理时间微调的方式解决了这一任务，但由于仅编码器的架构高度依赖于有限的参考图像，因此存在模糊问题。另一方面，最近的基于扩散的图像到3d方法通过将预先训练的2D扩散模型提取到3d表示中显示出生动可信的结果，但需要繁琐的逐场景优化。针对这些问题，我们提出了GD $^2$-NeRF，这是一个通过GAN和Diffusion的生成细节补偿框架，既不需要推理时间微调，又具有生动可信的细节。详细地说，遵循从粗到细的策略，GD$^2$-NeRF主要由一级并行流水线（OPP）和3D一致细节增强器（Diff3DE）组成。在粗略阶段，OPP首先将GAN模型有效地插入到现有的OG-NeRF管道中，以主要缓解从训练数据集中捕获的分布内先验的模糊问题，实现清晰度（LPIPS、FID）和保真度（PSNR、SSIM）之间的良好平衡。然后，在精细阶段，Diff3DE进一步利用预先训练的图像扩散模型来补充丰富的分布细节，同时保持良好的3D一致性。在合成数据集和真实世界数据集上进行的大量实验表明，GD$^2$ -NeRF在没有每场景微调的情况下显著改善了细节。 et.al.|[2401.00616](http://arxiv.org/abs/2401.00616)|null|
|**2023-12-28**|**iFusion: Inverting Diffusion for Pose-Free Reconstruction from Sparse Views**|我们提出了iFusion，这是一种新颖的3D对象重建框架，只需要两个具有未知相机姿态的视图。虽然单视图重建会产生视觉上吸引人的结果，但它可能会与实际对象有很大的偏差，尤其是在看不见的一侧。附加视图提高了重建保真度，但需要已知的摄影机姿势。然而，假设姿态的可用性可能是不现实的，并且现有的姿态估计器在稀疏视图场景中失败。为了解决这一问题，我们利用了一个预先训练的新颖视图合成扩散模型，该模型嵌入了关于不同对象的几何形状和外观的隐含知识。我们的策略分为三个步骤：（1）我们反转用于相机姿态估计的扩散模型，而不是合成新的视图。（2） 使用提供的视图和估计的姿态对扩散模型进行微调，使其成为为目标对象量身定制的新型视图合成器。（3） 利用配准的视图和微调的扩散模型，我们重建了3D对象。实验表明，在姿态估计和新视图合成方面都有很强的性能。此外，iFusion与各种重建方法无缝集成，并对其进行了增强。 et.al.|[2312.17250](http://arxiv.org/abs/2312.17250)|**[link](https://github.com/chinhsuanwu/ifusion)**|

<p align=right>(<a href=#updated-on-20240116>back to top</a>)</p>

## 3D Reconstruction

|Publish Date|Title|Abstract|PDF|Code|
|---|---|---|---|---|
|**2024-01-12**|**3D Reconstruction of Interacting Multi-Person in Clothing from a Single Image**|本文介绍了一种新的管道，用于从单个图像在全局相干的场景空间上重建服装中多人交互的几何结构。主要的挑战来自遮挡：由于他人或自身的遮挡，人体的一部分在单个视图中是不可见的，这会导致几何结构缺失和物理上的不可置信性（例如穿透）。我们通过利用两个人类先验来完成3D几何和表面接触，克服了这一挑战。对于几何先验，编码器学习将身体部位缺失的人的图像回归到潜在向量；解码器对这些矢量进行解码以产生相关联的几何形状的3D特征；并且隐式网络将这些特征与表面法线图相结合以重建完整且详细的3D人。对于接触先验，我们开发了一种图像空间接触检测器，该检测器输出3D中人与人之间表面接触的概率分布。我们使用这些先验来全局细化身体姿势，从而能够在场景空间中无穿透、准确地重建穿着衣服的多人互动。结果表明，与现有方法相比，我们的方法是完整的、全局一致的，并且在物理上是合理的。 et.al.|[2401.06415](http://arxiv.org/abs/2401.06415)|null|
|**2024-01-12**|**SD-MVS: Segmentation-Driven Deformation Multi-View Stereo with Spherical Refinement and EM optimization**|在本文中，我们介绍了分割驱动变形多视图立体（SD-MVS），这是一种可以有效解决无纹理区域三维重建挑战的方法。我们是第一个采用Segment Anything Model（SAM）来区分场景中的语义实例的公司，并进一步利用这些约束条件对匹配成本和传播进行逐像素补丁变形。同时，我们提出了一种独特的细化策略，将球面坐标和法线上的梯度下降与深度上的逐像素搜索间隔相结合，显著提高了重建三维模型的完整性。此外，我们采用期望最大化（EM）算法交替优化总匹配成本和超参数，有效地缓解了参数过度依赖经验调整的问题。对ETH3D高分辨率多视图立体基准和Tanks and Temples数据集的评估表明，我们的方法可以用更少的时间获得最先进的结果。 et.al.|[2401.06385](http://arxiv.org/abs/2401.06385)|null|
|**2024-01-12**|**Surgical-DINO: Adapter Learning of Foundation Models for Depth Estimation in Endoscopic Surgery**|目的：机器人手术中的深度估计在三维重建、手术导航和增强现实可视化中至关重要。尽管基础模型在许多视觉任务中表现出出色的性能，包括深度估计（例如，DINOv2），但最近的工作观察到其在医学和外科领域特定应用中的局限性。这项工作提出了一种用于手术深度估计的基础模型的低阶自适应（LoRA）。方法：我们设计了一种基于基础模型的深度估计方法，称为Surgical DINO，这是对DINOv2的低阶自适应，用于内窥镜手术中的深度估计。我们构建了LoRA层，并将其集成到DINO中，以适应手术特定领域的知识，而不是传统的微调。在训练过程中，我们冻结了显示出出色视觉表示能力的DINO图像编码器，并仅优化了LoRA层和深度解码器，以集成来自手术场景的特征。结果：我们的模型在SCARED的MICCAI挑战数据集上得到了广泛验证，该数据集是从达芬奇Xi内窥镜手术中收集的。我们的经验表明，外科DINO在内窥镜深度估计任务中显著优于所有最先进的模型。消融研究的分析表明，我们的LoRA层和适应具有显著效果。结论：外科DINO为基础模型成功适应外科领域进行深度估计提供了一些启示。结果中有明确证据表明，对计算机视觉数据集中预先训练的权重进行零样本预测或简单微调不足以直接在外科领域使用基础模型。代码位于https://github.com/BeileiCui/SurgicalDINO. et.al.|[2401.06013](http://arxiv.org/abs/2401.06013)|**[link](https://github.com/beileicui/surgicaldino)**|
|**2024-01-10**|**Structure from Duplicates: Neural Inverse Graphics from a Pile of Objects**|我们的世界充满了相同的物体（例如，可乐罐、同一型号的汽车）。当这些重复出现在一起时，为我们有效地推理3D提供了额外而有力的线索。受这一观察结果的启发，我们引入了“重复结构”（SfD），这是一种新颖的逆图形框架，可以从包含多个相同对象的单个图像中重建几何体、材料和照明。SfD首先识别图像中对象的多个实例，然后联合估计所有实例的6DoF姿势。随后使用反向图形管道来联合推理对象的形状、材质和环境光，同时遵守实例之间的共享几何图形和材质约束。我们的主要贡献包括利用对象副本作为单图像逆图形的鲁棒先验，并提出用于联合6-DoF对象姿态估计的平面内旋转鲁棒运动结构（SfM）公式。通过利用来自单个图像的多视图线索，SfD生成了更真实、更详细的3D重建，显著优于具有相似或更多观测值的现有单个图像重建模型和多视图重建方法。 et.al.|[2401.05236](http://arxiv.org/abs/2401.05236)|**[link](https://github.com/tianhang-cheng/sfd)**|
|**2024-01-07**|**RHOBIN Challenge: Reconstruction of Human Object Interaction**|对人与物体之间的相互作用进行建模是近年来新兴的研究方向。然而，由于严重的遮挡和复杂的动力学，捕捉人与物体的相互作用是一项非常具有挑战性的任务，这不仅需要了解三维人体姿态和物体姿态，还需要了解它们之间的相互作用。长期以来，三维人和物体的重建一直是计算机视觉中两个独立的研究领域。因此，我们提出了RHOBIN的第一个挑战：结合RHOBIN研讨会重建人-物交互。它旨在将人类和物体重建以及交互建模的研究团体聚集在一起，讨论技术和交换思想。我们的挑战包括从单目RGB图像进行3D重建的三个轨道，重点是处理具有挑战性的交互场景。我们的挑战吸引了100多名参与者，提交了300多份材料，表明了研究界的广泛兴趣。本文介绍了我们挑战赛的设置，并更详细地讨论了每条赛道的获胜方法。我们观察到，即使在严重遮挡的情况下，人类重建任务也正在变得成熟，而物体姿态估计和关节重建仍然是具有挑战性的任务。随着人们对交互建模越来越感兴趣，我们希望这份报告能提供有用的见解，并促进未来在这个方向上的研究。我们的研讨会网站位于\ href{https://rhobin-challenge.github.io/}{https://rhobin-challenge.github.io/}. et.al.|[2401.04143](http://arxiv.org/abs/2401.04143)|null|
|**2024-01-08**|**AGG: Amortized Generative 3D Gaussians for Single Image to 3D**|考虑到对自动3D内容创建管道的日益增长的需求，已经研究了各种3D表示来从单个图像生成3D对象。由于其优越的渲染效率，基于3D高斯飞溅的模型最近在3D重建和生成方面都表现出色。用于图像到3D生成的3D高斯飞溅方法通常是基于优化的，需要许多计算昂贵的分数提取步骤。为了克服这些挑战，我们引入了一种分期生成的3D高斯框架（AGG），该框架可以从单个图像中立即生成3D高斯，无需按实例优化。AGG利用中间混合表示分解3D高斯位置和其他外观属性的生成，用于联合优化。此外，我们提出了一种级联流水线，该流水线首先生成3D数据的粗略表示，然后使用3D高斯超分辨率模块对其进行上采样。我们的方法是根据现有的基于优化的3D高斯框架和利用其他3D表示的基于采样的管道进行评估的，其中AGG在质量和数量上都表现出有竞争力的生成能力，同时速度快几个数量级。项目页面：https://ir1d.github.io/AGG/ et.al.|[2401.04099](http://arxiv.org/abs/2401.04099)|null|
|**2024-01-08**|**A Survey on 3D Gaussian Splatting**|三维高斯散射（3DGS）是近年来在显式辐射场和计算机图形学领域出现的一种变革性技术。这种创新方法的特点是使用了数百万个3D高斯，这与神经辐射场（NeRF）方法有很大的不同，后者主要使用隐式的基于坐标的模型将空间坐标映射到像素值。3D GS凭借其明确的场景表示和可微分的渲染算法，不仅保证了实时渲染能力，而且引入了前所未有的控制和编辑水平。这将3D GS定位为下一代3D重建和表示的潜在游戏规则改变者。在本文中，我们首次系统地概述了3D GS领域的最新发展和关键贡献。我们首先详细探索了3D GS出现的基本原理和驱动力，为理解其意义奠定了基础。我们讨论的一个焦点是3D GS的实用性。通过促进实时性能，3D GS开辟了大量应用，从虚拟现实到交互式媒体等等。此外，还对领先的3D GS模型进行了比较分析，并在各种基准任务中进行了评估，以突出其性能和实用性。该调查的结论是确定了当前的挑战，并提出了该领域未来研究的潜在途径。通过这项调查，我们旨在为新来者和经验丰富的研究人员提供宝贵的资源，促进在适用和明确的辐射场表示方面的进一步探索和进步。 et.al.|[2401.03890](http://arxiv.org/abs/2401.03890)|null|
|**2024-01-01**|**BIBench: Benchmarking Data Analysis Knowledge of Large Language Models**|大型语言模型（LLM）已经在广泛的任务中展示了令人印象深刻的功能。然而，他们在数据分析专业领域的熟练程度和可靠性，特别是在注重数据驱动思维的情况下，仍然不确定。为了弥补这一差距，我们引入了BIBench，这是一个全面的基准测试，旨在评估商业智能（BI）背景下LLM的数据分析能力。BIBench从三个维度评估LLM：1）BI基础知识，评估模型的数字推理和对金融概念的熟悉程度；2） BI知识应用，确定模型快速理解文本信息和从多个视图生成分析问题的能力；以及3）BI技术技能，检查模型对技术知识的使用，以应对现实世界的数据分析挑战。BIBench包含11个子任务，涵盖三类任务类型：分类、提取和生成。此外，我们还开发了BIChat，这是一个具有超过一百万个数据点的特定领域数据集，用于微调LLM。我们将在\url上发布BIBenchmark、BIChat和评估脚本{https://github.com/cubenlp/BIBench}.该基准旨在为LLM能力的深入分析提供一种衡量标准，并促进LLM在数据分析领域的进步。 et.al.|[2401.02982](http://arxiv.org/abs/2401.02982)|**[link](https://github.com/cubenlp/BIBench)**|
|**2024-01-03**|**S3Net: Innovating Stereo Matching and Semantic Segmentation with a Single-Branch Semantic Stereo Network in Satellite Epipolar Imagery**|立体匹配和语义分割是双目卫星三维重建中的重要任务。然而，先前的研究主要将这些视为独立的并行任务，缺乏一个综合的多任务学习框架。本文介绍了一种解决方案，即单分支语义立体网络（S3Net），它创新地使用自融合和互融合模块将语义分割和立体匹配相结合。与之前独立利用语义或视差信息的方法不同，我们的方法识别并利用了这两个任务之间的内在联系，从而更准确地理解了语义信息和视差估计。在US3D数据集上的对比测试证明了我们的S3Net的有效性。我们的模型将语义分割中的mIoU从61.38提高到67.39，并将视差估计中的D1误差和平均端点误差（EPE）分别从10.051降低到9.579和1.439降低到1.403，超过了现有的竞争方法。我们的代码位于：https://github.com/CVEO/S3Net. et.al.|[2401.01643](http://arxiv.org/abs/2401.01643)|null|
|**2024-01-02**|**PAC-Bayesian Domain Adaptation Bounds for Multi-view learning**|本文提出了一系列在多视角学习环境中进行领域自适应的新结果。在以往的研究中，将多种观点纳入领域适应性的研究很少得到重视。通过这种方式，我们提出了用Pac贝叶斯理论分析泛化界限，以巩固目前分别处理的两种范式。首先，在Germain等人先前工作的基础上，我们利用多视图学习的概念将Germain等人提出的分布之间的距离用于领域自适应。因此，我们引入了一种新的距离，它是为多视图域自适应设置量身定制的。然后，我们给出了估计引入的散度的Pac贝叶斯界。最后，我们将不同的新边界与先前的研究进行了比较。 et.al.|[2401.01048](http://arxiv.org/abs/2401.01048)|null|

<p align=right>(<a href=#updated-on-20240116>back to top</a>)</p>

## Diffusion

|Publish Date|Title|Abstract|PDF|Code|
|---|---|---|---|---|
|**2024-01-12**|**Efficient Parallel Algorithms for Inpainting-Based Representations of 4K Images -- Part II: Spatial and Tonal Data Optimization**|均匀扩散修复可以从已知像素的稀疏子集高质量地重建缺失的图像区域，前提是它们的位置以及它们的灰度或颜色值得到了很好的优化。这种特性在基于修复的图像压缩中得到了利用，这是JPEG和JPEG2000等经典的基于变换的编解码器的一种很有前途的替代方案。然而，优化修复数据是一项具有挑战性的任务。目前的方法要么相当缓慢，要么不能产生高质量的结果。作为补救措施，我们提出了用于均匀扩散修复的快速空间和色调优化算法，该算法有效地利用了GPU并行性，并对一些最成功的数值概念进行了仔细的调整。我们提出了一种使用误差图抖动和Delaunay三角测量相结合的思想进行空间优化的加密策略。对于音调优化，我们设计了一个域分解求解器，以无矩阵的方式求解相应的正规方程，并用基于Voronoi的初始化策略进行补充。利用我们提出的方法，我们能够在运行时生成高质量的修复掩模，用于均匀扩散和优化色调值，其性能大大优于现有技术。 et.al.|[2401.06747](http://arxiv.org/abs/2401.06747)|null|
|**2024-01-12**|**Efficient Parallel Algorithms for Inpainting-Based Representations of 4K Images -- Part I: Homogeneous Diffusion Inpainting**|近年来，基于修复的压缩方法已被证明是经典编解码器（如JPEG和JPEG2000）的可行替代方案。与在变换域中存储系数的基于变换的编解码器不同，基于修复的方法存储原始图像像素的一小部分，并通过使用合适的修复算子从这些像素重建图像。这种修复算子的一个很好的候选者是均匀扩散修复，因为它简单，理论上有很好的动机，并且可以实现优化数据的良好重建质量。然而，一个主要的挑战是设计用于均匀扩散修复的快速解算器，该解算器可扩展到4K图像分辨率（3840\乘以2160$像素）并具有实时功能。我们通过对数值分析中两个最有效的概念——多重网格和域分解——的仔细改编和融合来克服这一问题。我们的域分解算法通过解决小重叠块上的修复问题，有效地利用了GPU的并行性。与JPEG中的简单块分解策略不同，我们的方法产生了无块伪影的重建。此外，在完全多重网格方案中嵌入域分解提供了全局相互作用，并允许我们通过以相同的速率减少低频和高频误差来实现最优收敛。即使是从非常稀疏的数据中，我们也能够以每秒60美元以上的帧数实现4K彩色图像重建——这在以前是不可行的。 et.al.|[2401.06744](http://arxiv.org/abs/2401.06744)|null|
|**2024-01-12**|**A deep implicit-explicit minimizing movement method for option pricing in jump-diffusion models**|我们开发了一种新颖的深度学习方法，用于对遵循跳跃-扩散动力学的资产上的欧洲篮子期权进行定价。期权定价问题被公式化为一个偏积分微分方程，通过一种新的隐显最小化运动时间步长方法进行近似，包括对每个时间步长使用深度残差型人工神经网络（Ann）进行近似。积分算子通过两种不同的方法离散化：a）遵循奇异值分解产生的局部坐标轴的稀疏网格高斯-埃尔米特近似，以及b）基于人工神经网络的高维专用求积规则。至关重要的是，所提出的人工神经网络的构建是为了确保大值的基础解的渐近行为，并且还导致关于解的先验已知定性性质的一致输出。在涉及默顿跳跃扩散模型的一系列数值实验中，评估了这些方法在维度方面的性能和稳健性。 et.al.|[2401.06740](http://arxiv.org/abs/2401.06740)|null|
|**2024-01-12**|**Adjoint chromoelectric and -magnetic correlators with gradient flow**|当用非相对论有效场论描述QCD时，在夸克物理的描述中经常会出现由两个色电场或-磁场的胶子相关器组成的算子。在零T时，这些相关器给出了胶洗脱子的质量，并且这些相关器的矩可以用来理解夸克的包容性P波衰变。在有限的T下，这些相关器定义了重夸克的扩散。然而，这些相关器在晶格间距中有一个发散项，需要注意。我们用梯度流涂抹法在纯规范理论中检查这些相关器，这应该使我们能够更仔细地减少和消除发散。在这些过程中，我们重点关注梯度流对这些相关器的影响以及这种分歧的减少。 et.al.|[2401.06733](http://arxiv.org/abs/2401.06733)|null|
|**2024-01-12**|**Equity auction dynamics: latent liquidity models with activity acceleration**|与连续交易相比，股权拍卖显示出几个明显的特点。随着拍卖时间的临近，事件的速度加快，导致围绕指示性价格的流动性大幅增加。这反过来又减少了对价格的影响，降低了指示性价格的波动性。在这项研究中，我们将潜在/揭示的订单簿框架适应股权拍卖的具体情况。我们提供模型参数的精确测量，包括订单提交、取消和扩散率。我们的设置使我们能够描述巴黎泛欧交易所拍卖结束时平均订单的全部动态。这些发现支持了潜在流动性框架在描述限额订单簿动态方面的相关性。最后，我们分析了导致次扩散指示性价格的因素，并证明了指示性价格缺乏可预测性。 et.al.|[2401.06724](http://arxiv.org/abs/2401.06724)|null|
|**2024-01-12**|**Confinement determines transport of a reaction-diffusion active matter front**|生物化学和机械过程之间的耦合对胚胎发育有着深远的影响。然而，能够量化这些相互作用的体外研究仍然难以捉摸。在这里，我们研究了一个合成系统，其中DNA反应扩散（RD）前沿被活性物质（AM）在准一维几何中流动产生的湍流平流。尽管简单RD前沿的动力学仅取决于反应和扩散速率，但我们表明RD-AM前沿的传播也受到约束几何结构的影响。我们首先通过消除反应或平流，实验性地剖析了反应-扩散-平流过程的不同组成部分，并观察了RD-AM如何允许在大距离上更快地传输，避免稀释。然后，我们展示了约束如何影响活性物质流：而瞬时流速的变化很小；相关时间随着限制的减少而显著增加。结果，与RD相比，RD-AM的前部速度增加了3到9倍。这个RD-AM实验模型为在生命系统中观察到的复杂时空过程的合理工程提供了一个框架。它将加强我们对宏观尺度模式和结构如何从非平衡系统中的微观成分中产生的理解。 et.al.|[2401.06674](http://arxiv.org/abs/2401.06674)|null|
|**2024-01-12**|**Decoupling Pixel Flipping and Occlusion Strategy for Consistent XAI Benchmarks**|特征去除是可扩展人工智能（XAI）的核心构建块，既用于基于遮挡的解释（Shapley值），也用于其评估（像素翻转，PF）。然而，从简单的平均值替换到使用最先进的扩散模型进行修复，遮挡策略可能会有很大的不同。这种模糊性限制了基于遮挡的方法的有用性。例如，PF基准导致排名矛盾。这被相互竞争的PF措施放大了：特征要么从最具影响力的第一个（MIF）开始删除，要么从最不具影响力的第二个（LIF）开始删除。本研究提出了两个互补的视角来解决这一分歧问题。首先，我们解决了基于遮挡的XAI的常见批评，即人工样本导致不可靠的模型评估。我们建议通过R（参考）-超出模型范围（OMS）得分来衡量可靠性。R-OMS评分能够对遮挡策略进行系统比较，并通过对一致的PF排名进行分组来解决分歧问题。其次，我们发现MIF和LIF的洞察力反过来取决于R-OMS得分。为了利用这一点，我们将MIF和LIF度量合并为对称相关性增益（SRG）度量。这打破了与基础遮挡策略的固有联系，并导致了一致的排名。这解决了分歧问题，我们对一组40种不同的遮挡策略进行了验证。 et.al.|[2401.06654](http://arxiv.org/abs/2401.06654)|null|
|**2024-01-12**|**Adversarial Examples are Misaligned in Diffusion Model Manifolds**|近年来，扩散模型（DM）因其在近似数据分布方面的成功而引起了人们的极大关注，产生了最先进的生成结果。然而，这些模型的多功能性超出了它们的生成能力，涵盖了各种视觉应用，如图像修复、分割、对抗性鲁棒性等。本研究致力于通过扩散模型的视角研究对抗性攻击。然而，我们的目标并不涉及增强图像分类器的对抗性鲁棒性。相反，我们的重点在于利用扩散模型来检测和分析这些对图像的攻击所引入的异常。为此，我们系统地检查了当使用扩散模型进行转换过程时，对抗性示例的分布的一致性。该方法的有效性在CIFAR-10和ImageNet数据集上进行了评估，包括后者中不同的图像大小。结果表明，在良性图像和受攻击图像之间具有显著的有效区分能力，提供了令人信服的证据，证明对抗性实例与DM的学习流形不一致。 et.al.|[2401.06637](http://arxiv.org/abs/2401.06637)|null|
|**2024-01-12**|**Motion2VecSets: 4D Latent Vector Set Diffusion for Non-rigid Shape Reconstruction and Tracking**|我们介绍了Motion2VenSets，这是一种用于从点云序列进行动态曲面重建的4D扩散模型。虽然现有的最先进的方法已经证明在使用神经场表示重建非刚性对象方面取得了成功，但传统的前馈网络遇到了来自噪声、部分或稀疏点云的模糊观测的挑战。为了应对这些挑战，我们引入了一种扩散模型，该模型通过压缩潜在表示的迭代去噪过程来显式学习非刚性对象的形状和运动分布。当处理模糊输入时，基于扩散的先验能够进行更合理和概率的重建。我们用潜在向量集参数化4D动力学，而不是使用全局潜在。这种新颖的4D表示使我们能够学习局部表面形状和变形模式，从而实现更准确的非线性运动捕捉，并显著提高对看不见的运动和身份的可推广性。对于更具时间连贯性的目标跟踪，我们同步地对变形潜集进行去噪，并在多个帧之间交换信息。为了避免计算开销，我们设计了一个交错的空间和时间注意力块，以沿着空间和时间域交替聚集变形潜伏期。与最先进的方法进行了广泛的比较，证明了我们的Motion2VenSets在从各种不完美的观测进行4D重建方面的优势，特别是在从DeformingThings4D Animals数据集上的稀疏点云重建看不见的个体方面，与CaDex相比，交集优于并集（IoU）提高了19%。更多详细信息，请访问https://vveicao.github.io/projects/Motion2VecSets/. et.al.|[2401.06614](http://arxiv.org/abs/2401.06614)|null|
|**2024-01-12**|**360DVD: Controllable Panorama Video Generation with 360-Degree Video Diffusion Model**|360度全景视频最近吸引了人们对研究和应用的更多兴趣，因为它们带来了更高的沉浸式体验。由于捕捉360度全景视频的昂贵成本，迫切需要通过给定提示生成所需的全景视频。最近，新兴的文本到视频（T2V）扩散方法在标准视频生成中表现出显著的有效性。然而，由于全景视频和标准视频之间在内容和运动模式方面存在显著差距，这些方法在产生令人满意的360度全景视频方面遇到了挑战。在本文中，我们提出了一种可控的全景视频生成管道，称为360度视频扩散模型（360DVD），用于根据给定的提示和运动条件生成全景视频。具体来说，我们介绍了一个名为360适配器的轻量级模块和辅助360增强技术，以转换预训练的T2V模型，用于360度视频生成。我们进一步提出了一个名为WEB360的新全景数据集，该数据集由360度视频-文本对组成，用于训练360DVD，解决了缺乏字幕全景视频数据集的问题。大量实验证明了360DVD在全景视频生成中的优越性和有效性。代码和数据集将很快发布。 et.al.|[2401.06578](http://arxiv.org/abs/2401.06578)|null|

<p align=right>(<a href=#updated-on-20240116>back to top</a>)</p>

## NeRF

|Publish Date|Title|Abstract|PDF|Code|
|---|---|---|---|---|
|**2024-01-12**|**Motion2VecSets: 4D Latent Vector Set Diffusion for Non-rigid Shape Reconstruction and Tracking**|我们介绍了Motion2VenSets，这是一种用于从点云序列进行动态曲面重建的4D扩散模型。虽然现有的最先进的方法已经证明在使用神经场表示重建非刚性对象方面取得了成功，但传统的前馈网络遇到了来自噪声、部分或稀疏点云的模糊观测的挑战。为了应对这些挑战，我们引入了一种扩散模型，该模型通过压缩潜在表示的迭代去噪过程来显式学习非刚性对象的形状和运动分布。当处理模糊输入时，基于扩散的先验能够进行更合理和概率的重建。我们用潜在向量集参数化4D动力学，而不是使用全局潜在。这种新颖的4D表示使我们能够学习局部表面形状和变形模式，从而实现更准确的非线性运动捕捉，并显著提高对看不见的运动和身份的可推广性。对于更具时间连贯性的目标跟踪，我们同步地对变形潜集进行去噪，并在多个帧之间交换信息。为了避免计算开销，我们设计了一个交错的空间和时间注意力块，以沿着空间和时间域交替聚集变形潜伏期。与最先进的方法进行了广泛的比较，证明了我们的Motion2VenSets在从各种不完美的观测进行4D重建方面的优势，特别是在从DeformingThings4D Animals数据集上的稀疏点云重建看不见的个体方面，与CaDex相比，交集优于并集（IoU）提高了19%。更多详细信息，请访问https://vveicao.github.io/projects/Motion2VecSets/. et.al.|[2401.06614](http://arxiv.org/abs/2401.06614)|null|
|**2024-01-05**|**Denoising Vision Transformers**|我们深入研究了视觉转换器（ViTs）固有的一个细微但重大的挑战：这些模型的特征图显示出网格状的伪影，这对ViTs在下游任务中的性能造成了不利影响。我们的研究将这个基本问题追溯到输入阶段的位置嵌入。为了解决这一问题，我们提出了一种新的噪声模型，该模型普遍适用于所有的ViT。具体来说，噪声模型将ViT输出分解为三个部分：一个没有噪声伪影的语义术语和两个以像素位置为条件的伪影相关术语。这种分解是通过在每幅图像的基础上加强与神经场的交叉视图特征一致性来实现的。这种逐图像优化过程从原始ViT输出中提取无伪影特征，为离线应用程序提供干净的特征。扩大了我们的解决方案的范围，以支持在线功能，我们引入了一种可学习的去噪器，直接从未处理的ViT输出中预测无伪影特征，这显示出对新数据的显著泛化能力，而无需对每张图像进行优化。我们的两阶段方法，称为去噪视觉转换器（DVT），不需要重新训练现有的预先训练的ViT，并且立即适用于任何基于转换器的架构。我们在各种具有代表性的ViT（DINO、MAE、DeiT III、EVA02、CLIP、DINOv2、DINOv2-reg）上评估了我们的方法。广泛的评估表明，我们的DVT在多个数据集（例如+3.84mIoU）的语义和几何任务中持续显著地改进了现有的最先进的通用模型。我们希望我们的研究将鼓励对ViT设计进行重新评估，特别是关于位置嵌入的天真使用。 et.al.|[2401.02957](http://arxiv.org/abs/2401.02957)|null|
|**2023-12-30**|**PlanarNeRF: Online Learning of Planar Primitives with Neural Radiance Fields**|从视觉数据中识别空间完整的平面基元是计算机视觉中的一项关键任务。现有的方法在很大程度上局限于2D片段恢复或简化3D结构，即使具有广泛的平面注释。我们提出了PlanarNeRF，这是一种能够通过在线学习检测密集3D平面的新框架。PlanarNeRF利用神经场表示，带来了三个主要贡献。首先，它利用并行的外观和几何知识增强了三维平面检测。其次，提出了一种轻量级的平面拟合模块来估计平面参数。第三，引入了一种具有更新机制的新的全局内存库结构，确保了跨帧一致性。PlanarNeRF的灵活架构使其能够在二维监督和自监督解决方案中发挥作用，在每种解决方案中，它都可以有效地从稀疏的训练信号中学习，显著提高训练效率。通过广泛的实验，我们证明了PlanarNeRF在各种场景下的有效性，并比现有工作有了显著的改进。 et.al.|[2401.00871](http://arxiv.org/abs/2401.00871)|null|
|**2024-01-01**|**Deblurring 3D Gaussian Splatting**|最近对辐射场的研究为具有照片级真实感渲染质量的新颖视图合成铺平了坚实的道路。然而，它们通常使用神经网络和体积绘制，这两种方法的训练成本很高，并且由于绘制时间长，阻碍了它们在各种实时应用中的广泛使用。最近，人们提出了一种基于3D高斯散射的方法来对3D场景进行建模，并在实时渲染图像的同时实现了显著的视觉质量。然而，如果训练图像模糊，则渲染质量会严重下降。模糊通常是由于镜头散焦、物体运动和相机抖动而产生的，它不可避免地会干扰干净图像的获取。先前的几项研究试图使用神经场从模糊的输入图像中渲染干净清晰的图像。然而，这些工作中的大多数仅设计用于基于体积渲染的神经辐射场，并不直接适用于基于光栅化的3D高斯散射方法。因此，我们提出了一种新的实时去模糊框架，即去模糊3D高斯散点，使用小型多层感知器（MLP）来操纵每个3D高斯的协方差来对场景模糊度进行建模。虽然去模糊的3D高斯飞溅仍然可以享受实时渲染，但它可以从模糊的图像中重建精细和清晰的细节。在基准上进行了各种实验，结果表明了我们的去模糊方法的有效性。定性结果可在https://benhenryl.github.io/Deblurring-3D-Gaussian-Splatting/ et.al.|[2401.00834](http://arxiv.org/abs/2401.00834)|null|
|**2023-12-22**|**Fluid Simulation on Neural Flow Maps**|我们介绍了神经流图，这是一种新的模拟方法，将新兴的隐式神经表示范式与基于流图理论的流体模拟相结合，以实现最先进的无粘流体现象模拟。我们设计了一种新的混合神经场表示，空间稀疏神经场（SSNF），它将小型神经网络与重叠、多分辨率和空间稀疏网格的金字塔相融合，以高精度紧凑地表示长期时空速度场。有了这个神经速度缓冲器，我们以机械对称的方式计算长期双向流图及其雅可比矩阵，以促进对现有解决方案的大幅精度提高。这些长程双向流图实现了低耗散的高平流精度，进而促进了高保真度的不可压缩流模拟，显示了复杂的旋涡结构。我们展示了我们的神经流体模拟在各种具有挑战性的模拟场景中的有效性，包括跳跃涡流、碰撞涡流、涡流重新连接，以及移动障碍物和密度差异产生的涡流。我们的例子表明，在能量守恒、视觉复杂性、对实验观测的遵守以及详细旋涡结构的保存方面，与现有方法相比，性能有所提高。 et.al.|[2312.14635](http://arxiv.org/abs/2312.14635)|null|
|**2023-12-21**|**Geometric Awareness in Neural Fields for 3D Human Registration**|将模板与三维人体点云对齐是一个长期存在的问题，对于动画、重建和启用监督学习管道等任务至关重要。最近的数据驱动方法利用了预测的表面对应关系；然而，它们对不同的姿态或分布并不鲁棒。相比之下，工业解决方案往往依赖于昂贵的手动注释或多视图捕获系统。最近，神经场已经显示出有希望的结果，但它们纯粹的数据驱动性质缺乏几何意识，通常导致模板配准的微小错位。在这项工作中，我们提出了两种解决方案：LoVD，一种新的神经场模型，它预测朝向目标表面上的局部SMPL顶点的方向；和INT，这是第一个专门用于神经领域的自监督任务，在测试时，它利用目标几何结构来细化主干。我们将它们组合到INLoVD中，这是一个在大型MoCap数据集上训练的强大的3D人体注册管道。INLoVD是高效的（不到一分钟），在公共基准上稳定地达到了最先进的水平，并对分布外的数据提供了前所未有的概括。我们将在\url｛url｝中发布代码和检查点。 et.al.|[2312.14024](http://arxiv.org/abs/2312.14024)|null|
|**2023-12-20**|**Neural feels with neural fields: Visuo-tactile perception for in-hand manipulation**|为了实现人类水平的灵活性，机器人必须从多模式感知推断空间意识，以推理接触互动。在新物体的手操作过程中，这种空间意识包括估计物体的姿势和形状。手内感知的现状主要采用视觉，并局限于跟踪先验已知对象。此外，在操作过程中，手上物体的视觉遮挡迫在眉睫，这阻止了当前系统在没有遮挡的情况下超越任务。我们将多指手的视觉和触摸传感相结合，在手内操作过程中估计物体的姿势和形状。我们的方法NeuralFeels通过在线学习神经场来编码对象几何，并通过优化姿态图问题来联合跟踪它。我们研究了模拟和现实世界中的多模式手部感知，通过本体感觉驱动的策略与不同的物体进行交互。我们的实验显示，使用已知的CAD模型，最终重建F分数为 $81$%，平均姿势漂移为$4.7\，\text｛mm｝$，进一步降低到$2.3\，\text{mm｝$。此外，我们观察到，与仅使用视觉的方法相比，在严重的视觉遮挡下，我们可以实现高达94$ %的跟踪改进。我们的研究结果表明，在手部操作过程中，触摸至少可以改善视觉估计，并在最好的情况下消除视觉估计的歧义。我们发布了70个实验的评估数据集FeelSight，作为在该领域进行基准测试的一步。我们由多模态感知驱动的神经表示可以作为提高机器人灵活性的感知支柱。视频可以在我们的项目网站上找到https://suddhu.github.io/neural-feels/ et.al.|[2312.13469](http://arxiv.org/abs/2312.13469)|null|
|**2023-12-20**|**Deep Learning on 3D Neural Fields**|近年来，神经场（NFs）已成为编码各种连续信号（如图像、视频、音频和3D形状）的有效工具。当应用于3D数据时，NFs提供了一种解决方案来解决与流行的离散表示相关的碎片化和局限性。然而，鉴于神经网络本质上是神经网络，目前尚不清楚它们是否以及如何无缝集成到深度学习管道中，以解决下游任务。本文解决了这一研究问题，并介绍了nf2vec，这是一个能够在单个推理过程中为输入NF生成紧凑的潜在表示的框架，同时专门处理NFs。我们在几个用于表示3D曲面的NFs上测试了这个框架，例如无符号/有符号距离和占用字段。此外，我们用更复杂的NFs证明了我们的方法的有效性，这些NFs包括3D对象的几何形状和外观，如神经辐射场。 et.al.|[2312.13277](http://arxiv.org/abs/2312.13277)|null|
|**2023-12-16**|**How to Train Neural Field Representations: A Comprehensive Study and Benchmark**|神经场（NeFs）最近已成为一种用于对各种模态（包括图像、形状和场景）的信号进行建模的通用方法。随后，许多工作探索了使用NeF作为下游任务的表示，例如，根据适合的NeF的参数对图像进行分类。然而，NeF超参数对其作为下游表示的质量的影响很少被理解，而且在很大程度上仍未被探索。这在一定程度上是由于拟合神经场数据集所需的大量时间造成的。在这项工作中，我们提出了 $\verb|fit-a-nef|$ ，这是一个基于JAX的库，它利用并行化来实现大规模nef数据集的快速优化，从而显著加快速度。有了这个库，我们进行了一项全面的研究，研究了不同超参数——包括初始化、网络架构和优化策略——对下游任务的NeF拟合的影响。我们的研究为如何训练NeF提供了宝贵的见解，并为优化其在下游应用中的有效性提供了指导。最后，基于所提出的库和我们的分析，我们提出了Neural Field Arena，这是一个由流行视觉数据集的神经场变体组成的基准，包括MNIST、CIFAR、ImageNet和ShapeNetv2的变体。我们的图书馆和神经领域竞技场将是开源的，以引入标准化的基准测试，并促进对神经领域的进一步研究。 et.al.|[2312.10531](http://arxiv.org/abs/2312.10531)|**[link](https://github.com/samuelepapa/fit-a-nef)**|
|**2023-12-18**|**LatentEditor: Text Driven Local Editing of 3D Scenes**|虽然神经领域在视图合成和场景重建方面取得了重大进展，但由于其对来自多视图输入的几何和纹理信息的隐式编码，编辑它们带来了巨大的挑战。在本文中，我们介绍了\textsc｛LatentEditor｝，这是一个创新的框架，旨在让用户能够使用文本提示对神经字段进行精确和本地控制的编辑。利用去噪扩散模型，我们成功地将真实世界的场景嵌入到潜在空间中，与传统方法相比，产生了更快、更具适应性的NeRF主干进行编辑。为了提高编辑精度，我们引入了一个delta分数来计算潜在空间中的2D掩模，该分数可以作为局部修改的指南，同时保留不相关的区域。我们新颖的像素级评分方法利用InstructPix2Pix（IP2P）的能力来辨别潜在空间中IP2P条件和无条件噪声预测之间的差异。然后在训练集中迭代地更新以2D掩码为条件的编辑的潜伏时间，以实现3D局部编辑。与现有的3D编辑模型相比，我们的方法实现了更快的编辑速度和卓越的输出质量，弥合了文本指令和潜在空间中高质量3D场景编辑之间的差距。我们在LLFF、IN2N、NeRFStudio和NeRFArt四个基准3D数据集上展示了我们的方法的优势。 et.al.|[2312.09313](http://arxiv.org/abs/2312.09313)|**[link](https://github.com/umarkhalidAI/LatentEditor)**|

<p align=right>(<a href=#updated-on-20240116>back to top</a>)</p>

[contributors-shield]: https://img.shields.io/github/contributors/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[contributors-url]: https://github.com/Vincentqyw/cv-arxiv-daily/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[forks-url]: https://github.com/Vincentqyw/cv-arxiv-daily/network/members
[stars-shield]: https://img.shields.io/github/stars/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[stars-url]: https://github.com/Vincentqyw/cv-arxiv-daily/stargazers
[issues-shield]: https://img.shields.io/github/issues/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[issues-url]: https://github.com/Vincentqyw/cv-arxiv-daily/issues

