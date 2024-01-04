[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]

## Updated on 2024.01.04
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
|**2024-01-02**|**Street Gaussians for Modeling Dynamic Urban Scenes**|本文旨在解决从单目视频中建模动态城市街道场景的问题。最近的方法扩展了NeRF，将跟踪车辆姿态纳入车辆动画，实现了动态城市街道场景的照片逼真视图合成。然而，它们的显著局限性在于训练和渲染速度慢，再加上履带车辆姿态对高精度的迫切需求。我们介绍了Street Gaussians，一种新的明确的场景表示，它解决了所有这些限制。具体地说，动态城市街道被表示为一组点云，这些点云配备有语义logits和3D Gaussians，每一个都与前景车辆或背景相关联。为了对前景对象车辆的动力学进行建模，使用可优化的跟踪姿态以及动态外观的动态球面谐波模型对每个对象点云进行优化。显式表示允许容易地合成目标车辆和背景，这反过来又允许在半小时的训练内以133 FPS（1066 $\times$ 1600分辨率）进行场景编辑操作和渲染。所提出的方法在多个具有挑战性的基准上进行了评估，包括KITTI和Waymo Open数据集。实验表明，在所有数据集上，所提出的方法始终优于最先进的方法。此外，尽管仅依赖于现成跟踪器的姿态，但所提出的表示提供的性能与使用精确的地面实况姿态所实现的性能不相上下。代码位于https://zju3dv.github.io/street_gaussians/. et.al.|[2401.01339](http://arxiv.org/abs/2401.01339)|null|
|**2024-01-01**|**Deblurring 3D Gaussian Splatting**|最近对辐射场的研究为具有照片级真实感渲染质量的新颖视图合成铺平了坚实的道路。然而，它们通常使用神经网络和体积绘制，这两种方法的训练成本很高，并且由于绘制时间长，阻碍了它们在各种实时应用中的广泛使用。最近，人们提出了一种基于3D高斯散射的方法来对3D场景进行建模，并在实时渲染图像的同时实现了显著的视觉质量。然而，如果训练图像模糊，则渲染质量会严重下降。模糊通常是由于镜头散焦、物体运动和相机抖动而产生的，它不可避免地会干扰干净图像的获取。先前的几项研究试图使用神经场从模糊的输入图像中渲染干净清晰的图像。然而，这些工作中的大多数仅设计用于基于体积渲染的神经辐射场，并不直接适用于基于光栅化的3D高斯散射方法。因此，我们提出了一种新的实时去模糊框架，即去模糊3D高斯散点，使用小型多层感知器（MLP）来操纵每个3D高斯的协方差来对场景模糊度进行建模。虽然去模糊的3D高斯飞溅仍然可以享受实时渲染，但它可以从模糊的图像中重建精细和清晰的细节。在基准上进行了各种实验，结果表明了我们的去模糊方法的有效性。定性结果可在https://benhenryl.github.io/Deblurring-3D-Gaussian-Splatting/ et.al.|[2401.00834](http://arxiv.org/abs/2401.00834)|null|
|**2024-01-01**|**Sharp-NeRF: Grid-based Fast Deblurring Neural Radiance Fields Using Sharpness Prior**|神经辐射场（NeRF）在基于神经渲染的新视图合成中表现出了显著的性能。然而，当输入图像是在不完美的条件下拍摄的时，NeRF会遭受严重的视觉质量下降，例如照明不良、散焦模糊和透镜像差。特别是，当通常使用相机拍摄图像时，散焦模糊在图像中非常常见。尽管最近很少有研究提出渲染相当高质量的清晰图像，但它们仍然面临许多关键挑战。特别地，这些方法采用了基于多层感知器（MLP）的NeRF，这需要大量的计算时间。为了克服这些缺点，本文提出了一种新的技术Sharp-NeRF——一种基于网格的NeRF，它可以在半小时的训练内从输入的模糊图像中渲染干净清晰的图像。为此，我们使用了几个基于网格的内核来准确地对场景的清晰度/模糊度进行建模。计算像素的清晰度水平以学习空间变化的模糊核。我们在由模糊图像组成的基准上进行了实验，并评估了完全参考和非参考指标。定性和定量的结果表明，我们的方法以生动的色彩和精细的细节呈现出尖锐的新颖观点，并且它比以前的作品具有更快的训练时间。我们的项目页面位于https://benhenryl.github.io/SharpNeRF/ et.al.|[2401.00825](http://arxiv.org/abs/2401.00825)|**[link](https://github.com/benhenryl/sharpnerf)**|
|**2024-01-02**|**GD^2-NeRF: Generative Detail Compensation via GAN and Diffusion for One-shot Generalizable Neural Radiance Fields**|在本文中，我们专注于单镜头新颖视图合成（O-NVS）任务，该任务的目标是在每个场景只有一个参考图像的情况下合成照片逼真的新颖视图。先前的一次性可泛化神经辐射场（OG-NeRF）方法以无推理时间微调的方式解决了这一任务，但由于仅编码器的架构高度依赖于有限的参考图像，因此存在模糊问题。另一方面，最近的基于扩散的图像到3d方法通过将预先训练的2D扩散模型提取到3d表示中显示出生动可信的结果，但需要繁琐的逐场景优化。针对这些问题，我们提出了GD $^2$-NeRF，这是一个通过GAN和Diffusion的生成细节补偿框架，既不需要推理时间微调，又具有生动可信的细节。详细地说，遵循从粗到细的策略，GD$^2$-NeRF主要由一级并行流水线（OPP）和3D一致细节增强器（Diff3DE）组成。在粗略阶段，OPP首先将GAN模型有效地插入到现有的OG-NeRF管道中，以主要缓解从训练数据集中捕获的分布内先验的模糊问题，实现清晰度（LPIPS、FID）和保真度（PSNR、SSIM）之间的良好平衡。然后，在精细阶段，Diff3DE进一步利用预先训练的图像扩散模型来补充丰富的分布细节，同时保持良好的3D一致性。在合成数据集和真实世界数据集上进行的大量实验表明，GD$^2$ -NeRF在没有每场景微调的情况下显著改善了细节。 et.al.|[2401.00616](http://arxiv.org/abs/2401.00616)|null|
|**2023-12-28**|**iFusion: Inverting Diffusion for Pose-Free Reconstruction from Sparse Views**|我们提出了iFusion，这是一种新颖的3D对象重建框架，只需要两个具有未知相机姿态的视图。虽然单视图重建会产生视觉上吸引人的结果，但它可能会与实际对象有很大的偏差，尤其是在看不见的一侧。附加视图提高了重建保真度，但需要已知的摄影机姿势。然而，假设姿态的可用性可能是不现实的，并且现有的姿态估计器在稀疏视图场景中失败。为了解决这一问题，我们利用了一个预先训练的新颖视图合成扩散模型，该模型嵌入了关于不同对象的几何形状和外观的隐含知识。我们的策略分为三个步骤：（1）我们反转用于相机姿态估计的扩散模型，而不是合成新的视图。（2） 使用提供的视图和估计的姿态对扩散模型进行微调，使其成为为目标对象量身定制的新型视图合成器。（3） 利用配准的视图和微调的扩散模型，我们重建了3D对象。实验表明，在姿态估计和新视图合成方面都有很强的性能。此外，iFusion与各种重建方法无缝集成，并对其进行了增强。 et.al.|[2312.17250](http://arxiv.org/abs/2312.17250)|**[link](https://github.com/chinhsuanwu/ifusion)**|
|**2023-12-28**|**Spacetime Gaussian Feature Splatting for Real-Time Dynamic View Synthesis**|动态场景的新颖视图合成一直是一个有趣但具有挑战性的问题。尽管最近取得了进展，但同时实现高分辨率的真实感、实时渲染和紧凑的存储仍然是一项艰巨的任务。为了应对这些挑战，我们提出了时空高斯特征飞溅作为一种新的动态场景表示，由三个关键组件组成。首先，我们通过增强具有时间不透明度和参数运动/旋转的3D高斯，来形成富有表现力的时空高斯。这使得时空高斯能够捕捉场景中的静态、动态以及瞬态内容。其次，我们介绍了飞溅特征渲染，它用神经特征代替了球面谐波。这些功能有助于在保持小尺寸的同时对视图和与时间相关的外观进行建模。第三，我们利用训练误差和粗略深度的指导，在难以与现有管道融合的区域对新的高斯采样。在几个已建立的真实世界数据集上的实验表明，我们的方法在保持紧凑存储的同时，实现了最先进的渲染质量和速度。在8K分辨率下，我们的lite版本模型可以在Nvidia RTX 4090 GPU上以60 FPS的速度渲染。 et.al.|[2312.16812](http://arxiv.org/abs/2312.16812)|null|
|**2023-12-29**|**DL3DV-10K: A Large-Scale Scene Dataset for Deep Learning-based 3D Vision**|我们见证了基于深度学习的3D视觉的重大进展，从基于神经辐射场（NeRF）的3D表示学习到在新视图合成（NVS）中的应用。然而，用于基于深度学习的3D视觉的现有场景级数据集，仅限于合成环境或现实世界场景的狭窄选择，是非常不足的。这种不足不仅阻碍了现有方法的全面基准，而且限制了在基于深度学习的3D分析中可以探索的内容。为了解决这一关键差距，我们展示了DL3DV-10K，这是一个大型场景数据集，其特征是从65种类型的兴趣点（POI）位置捕获的10510个视频中的5120万帧，涵盖了有界和无界场景，具有不同的反射、透明度和光照水平。我们在DL3DV-10K上对最近的NVS方法进行了全面的基准测试，为未来的NVS研究提供了宝贵的见解。此外，我们在一项从DL3DV-10K学习可推广NeRF的试点研究中获得了令人鼓舞的结果，这表明了大规模场景级数据集的必要性，以打造学习3D表示的基础模型。我们的DL3DV-10K数据集、基准测试结果和模型将在https://dl3dv-10k.github.io/DL3DV-10K/. et.al.|[2312.16256](http://arxiv.org/abs/2312.16256)|null|
|**2023-12-26**|**fMPI: Fast Novel View Synthesis in the Wild with Layered Scene Representations**|在这项研究中，我们为基于分层场景表示的新视图合成（NVS）方法提出了两种新的输入处理范式，这两种方法在不影响质量的情况下显著提高了它们的运行时间。我们的方法识别并减轻了传统管道最耗时的两个方面：构建和处理所谓的平面扫描体积（PSV），这是输入相机视图的平面重新投影的高维张量。特别是，我们建议在并行组中处理该张量，以提高计算效率，并对相邻输入平面进行超采样，从而生成更密集、更准确的场景表示。所提出的增强提供了显著的灵活性，允许在性能和速度之间取得平衡，从而朝着实时应用迈出了实质性的步伐。此外，它们非常通用，因为任何基于PSV的方法都可以使用它们，包括使用多平面图像、多球体图像和分层深度图像的方法。在一组全面的实验中，我们证明了我们提出的范式能够设计出一种NVS方法，该方法在公共基准上达到最先进的水平，同时比现有的最先进的方法快50倍。它在速度方面也比目前的前辈高出3倍多，同时实现了明显更好的渲染质量。 et.al.|[2312.16109](http://arxiv.org/abs/2312.16109)|null|
|**2023-12-25**|**Sparse-view CT Reconstruction with 3D Gaussian Volumetric Representation**|稀疏视图CT是减少传统CT扫描辐射剂量的一种很有前途的策略，但从不完整和有噪声的数据中重建高质量图像是一项挑战。最近，3D高斯已被应用于复杂自然场景的建模，与隐式神经表示（INRs）相比，它表现出快速收敛和更好的新颖视图渲染。我们从3D高斯在自然场景建模和新视图合成中的成功应用中获得灵感，研究了它们在稀疏视图CT重建中的潜力。我们利用来自滤波后的反投影重建图像的先验信息来初始化高斯；并且通过比较投影空间中的差异来更新它们的参数。自适应密度控制进一步提高了性能。与INRs相比，3D高斯从先验信息中受益更多，可以明确绕过空白空间中的学习，并有效地分配容量，加速收敛。3D高斯还可以有效地学习高频细节。3D高斯以自我监督的方式进行训练，避免了对大规模配对数据的需要。我们在AAPM-Mayo数据集上的实验表明，与基于INR的方法相比，3D高斯可以提供优越的性能。这项工作正在进行中，代码将公开。 et.al.|[2312.15676](http://arxiv.org/abs/2312.15676)|null|
|**2023-12-22**|**Deformable 3D Gaussian Splatting for Animatable Human Avatars**|神经辐射场的最新进展使得能够在动态设置中对照片真实感图像进行新颖的视图合成，这可以应用于具有人类动画的场景。然而，通常使用的隐式主干来建立准确的模型，需要许多输入视图和额外的注释，如人体遮罩、UV贴图和深度贴图。在这项工作中，我们提出了ParDy Human（参数化动态人类化身），这是一种完全明确的方法，可以从一个单一的单目序列中构建数字化身。ParDy Human在3D高斯飞溅中引入了参数驱动的动力学，其中通过人体姿势模型使3D高斯变形以使化身动画化。我们的方法由两个部分组成：第一个模块根据SMPL顶点使标准3D高斯变形，第二个模块进一步采用其设计的联合编码并预测每高斯变形，以处理SMPL顶点变形之外的动力学。然后通过光栅化器合成图像。ParDy Human构成了逼真动态人类化身的显式模型，其需要显著更少的训练视图和图像。我们的化身学习不需要额外的注释，如掩码，并且可以在可变背景下进行训练，同时即使在消费硬件上也能高效地推断出全分辨率图像。我们提供的实验证据表明，在ZJU MoCap和THUman4.0数据集上，ParDy-Human在数量和视觉上都优于最先进的方法。 et.al.|[2312.15059](http://arxiv.org/abs/2312.15059)|null|

<p align=right>(<a href=#updated-on-20240104>back to top</a>)</p>

## 3D Reconstruction

|Publish Date|Title|Abstract|PDF|Code|
|---|---|---|---|---|
|**2024-01-03**|**S3Net: Innovating Stereo Matching and Semantic Segmentation with a Single-Branch Semantic Stereo Network in Satellite Epipolar Imagery**|立体匹配和语义分割是双目卫星三维重建中的重要任务。然而，先前的研究主要将这些视为独立的并行任务，缺乏一个综合的多任务学习框架。本文介绍了一种解决方案，即单分支语义立体网络（S3Net），它创新地使用自融合和互融合模块将语义分割和立体匹配相结合。与之前独立利用语义或视差信息的方法不同，我们的方法识别并利用了这两个任务之间的内在联系，从而更准确地理解了语义信息和视差估计。在US3D数据集上的对比测试证明了我们的S3Net的有效性。我们的模型将语义分割中的mIoU从61.38提高到67.39，并将视差估计中的D1误差和平均端点误差（EPE）分别从10.051降低到9.579和1.439降低到1.403，超过了现有的竞争方法。我们的代码位于：https://github.com/CVEO/S3Net. et.al.|[2401.01643](http://arxiv.org/abs/2401.01643)|null|
|**2024-01-02**|**PAC-Bayesian Domain Adaptation Bounds for Multi-view learning**|本文提出了一系列在多视角学习环境中进行领域自适应的新结果。在以往的研究中，将多种观点纳入领域适应性的研究很少得到重视。通过这种方式，我们提出了用Pac贝叶斯理论分析泛化界限，以巩固目前分别处理的两种范式。首先，在Germain等人先前工作的基础上，我们利用多视图学习的概念将Germain等人提出的分布之间的距离用于领域自适应。因此，我们引入了一种新的距离，它是为多视图域自适应设置量身定制的。然后，我们给出了估计引入的散度的Pac贝叶斯界。最后，我们将不同的新边界与先前的研究进行了比较。 et.al.|[2401.01048](http://arxiv.org/abs/2401.01048)|null|
|**2023-12-29**|**Informative Rays Selection for Few-Shot Neural Radiance Fields**|神经辐射场（NeRF）最近已成为基于图像的3D重建的一种强大方法，但每个场景的漫长优化限制了其实际应用，尤其是在资源受限的环境中。现有的方法通过减少输入视图的数量并利用复杂的损失或来自其他模态的额外输入来正则化所学习的体积表示来解决这个问题。在本文中，我们提出了KeyNeRF，这是一种简单而有效的方法，通过聚焦关键信息射线，在少镜头场景中训练NeRF。这种射线首先在相机级别通过视图选择算法进行选择，该算法在保证场景覆盖的同时促进基线多样性，然后在像素级别通过基于局部图像熵的概率分布进行采样。我们的方法与最先进的方法相比表现良好，同时需要对现有NeRF代码库进行最小的更改。 et.al.|[2312.17561](http://arxiv.org/abs/2312.17561)|null|
|**2023-12-28**|**Toward Semantic Scene Understanding for Fine-Grained 3D Modeling of Plants**|由于全球人口增长以及对粮食和劳动力短缺的预期，农业机器人是一个活跃的研究领域。机器人可能有助于完成修剪、收割、表型分析和植物建模等任务。然而，农业自动化受到阻碍，因为难以在该领域创建高分辨率3D语义地图，从而实现安全操作和导航。在本文中，我们致力于解决这一问题，并展示了语义和环境先验的使用如何帮助为高粱的目标应用构建准确的3D地图。具体而言，我们1）使用高粱种子作为语义地标来构建视觉同步定位和映射（SLAM）系统，该系统使我们能够平均映射78%的高粱范围，而ORB-SLAM2的映射率为38%；和2）使用种子作为语义特征来改进由机器人手持相机拍摄的图像对完整高粱穗的3D重建。 et.al.|[2312.17110](http://arxiv.org/abs/2312.17110)|null|
|**2023-12-28**|**Geometry-Biased Transformer for Robust Multi-View 3D Human Pose Reconstruction**|我们解决了在遮挡和有限重叠视图下从多个视图估计3D人体姿态的挑战。我们将多视图、单人三维人体姿态重建作为一个回归问题，并提出了一种新的编码器-解码器-转换器架构，用于从多视图二维姿态序列中估计三维姿态。编码器对在不同视图和时间检测到的2D骨骼关节进行细化，通过全局自关注融合多视图和时间信息。我们通过结合有几何偏见的注意力机制来增强编码器，有效地利用视图之间的几何关系。此外，我们使用2D姿势检测器提供的检测分数来基于2D检测的可靠性进一步引导编码器的注意力。解码器随后使用针对每个关节的预定义查询，从这些细化的标记回归3D姿势序列。为了增强我们的方法对看不见的场景的泛化能力，并提高对缺失关节的恢复能力，我们实施了包括场景居中、合成视图和标记丢弃在内的策略。我们在三个基准公共数据集Human3.6M、CMU Panoptic和Occlusion Persons上进行了广泛的实验。我们的结果证明了我们的方法的有效性，特别是在遮挡场景和视图很少的情况下，这对于基于三角测量的方法来说是传统上具有挑战性的场景。 et.al.|[2312.17106](http://arxiv.org/abs/2312.17106)|null|
|**2023-12-28**|**Learning Spatially Collaged Fourier Bases for Implicit Neural Representation**|现有的隐式神经表示（INR）方法可以通过不同频率的傅立叶基的线性组合解释为全局场景表示。然而，这种通用基函数可能会限制不需要特定组件的局部区域的表示能力，从而导致令人不快的伪影。为此，我们引入了一种可学习的空间掩模，它可以有效地将不同的傅立叶基分派到各个区域中。这转化为拼贴傅立叶补丁，从而实现复杂信号的精确表示。综合实验证明，在各种INR任务中，包括图像拟合、视频表示和3D形状表示，所提出的方法的重建质量优于现有基线。我们的方法优于所有其他基线，将图像拟合PSNR提高了3dB以上，并将3D重建提高到98.81 IoU和0.0011倒角距离。 et.al.|[2312.17018](http://arxiv.org/abs/2312.17018)|null|
|**2023-12-27**|**In-Hand 3D Object Reconstruction from a Monocular RGB Video**|我们的工作旨在重建一只手在静态RGB相机前握住并旋转的3D物体。以前的方法使用隐式神经表示从多视图图像中恢复通用手持物体的几何结构，在物体的可见部分取得了令人信服的结果。然而，由于遮挡，这些方法在准确捕捉手-物体接触区域内的形状方面有困难。在本文中，我们提出了一种新的方法，通过结合二维遮挡说明的先验和物理接触约束来处理遮挡下的表面重建。对于前者，我们引入了一个对象阿莫尔完成网络来推断遮挡下对象的二维完全掩模。为了确保预测的2D变形掩模的准确性和视图一致性，我们设计了一种用于变形掩模细化和3D重建的联合优化方法。对于后者，我们对接触区域中的局部几何体施加穿透和吸引约束。我们在HO3D和HOD数据集上评估了我们的方法，并证明它在重建表面质量方面优于最先进的方法，在HO3D上提高了52美元，在HOD上提高了20美元。项目网页：https://east-j.github.io/ihor. et.al.|[2312.16425](http://arxiv.org/abs/2312.16425)|null|
|**2023-12-24**|**SUNDIAL: 3D Satellite Understanding through Direct, Ambient, and Complex Lighting Decomposition**|卫星图像的三维建模在环境科学、城市规划、农业和灾害应对领域至关重要。然而，传统的3D建模技术在遥感环境中面临着独特的挑战，包括大范围区域上有限的多视图基线，不同的直接、环境和复杂照明条件，以及不同捕获之间的时变场景变化。在这项工作中，我们介绍了SUNDIAL，这是一种使用神经辐射场进行卫星图像三维重建的综合方法。在这种单一模型方法中，我们共同学习了卫星场景几何结构、照明组件和太阳方向，并提出了一种二次阴影光线投射技术，以1）使用倾斜的太阳角来渲染阴影，改善场景几何结构，2）实现场景反照率和照明的物理解纠缠，以及3）确定来自直接环境（天空）的照明组件，以及复杂的来源。为了实现这一点，我们将遥感文献中的照明线索和几何先验纳入神经渲染方法，对卫星场景的物理特性进行建模，如阴影、散射天空照明以及植被和水的复杂照明和阴影。我们评估了SUNDIAL相对于现有基于NeRF的卫星场景建模技术的性能，并在具有小基线、稀疏输入和可变照明的具有挑战性的场景中展示了改进的场景和照明解纠缠、新颖的视图和照明渲染以及几何体和太阳方向估计。 et.al.|[2312.16215](http://arxiv.org/abs/2312.16215)|null|
|**2023-12-24**|**A theory of volumetric representations for opaque solids**|我们开发了一种将不透明固体表示为体积模型的理论。从不透明固体作为随机指示函数的随机表示开始，我们证明了可以使用指数体积输运对这种固体进行建模的条件。我们还导出了体积衰减系数的表达式，作为基本指标函数的概率分布的函数。我们将我们的理论推广到考虑固体不同部分的各向同性和各向异性散射，以及将不透明固体表示为隐式表面。我们从第一性原理推导出体积表示，这确保了它满足物理约束，如互易性和可逆性。我们使用我们的理论来解释、比较和纠正以前的体积表示，并提出有意义的扩展，从而提高3D重建任务的性能。 et.al.|[2312.15406](http://arxiv.org/abs/2312.15406)|null|
|**2023-12-23**|**WildScenes: A Benchmark for 2D and 3D Semantic Segmentation in Large-scale Natural Environments**|语义场景理解的最新进展主要得益于城市环境中语义注释的双模（相机和激光雷达）数据集的可用性。然而，自然、非结构化环境也需要这样的注释数据集，以实现应用程序的语义感知，包括保护、搜救、环境监测和农业自动化。因此，我们介绍了WildScenes，这是一个双模态基准数据集，由自然环境中的多个大规模遍历组成，包括高分辨率2D图像和密集3D激光雷达点云中的语义注释，以及精确的6-DoF姿态信息。数据（1）以轨迹为中心，具有精确的定位和全局对齐的点云，（2）校准和同步以支持双模态推理，以及（3）在6个月内包含不同的自然环境，以支持领域适应研究。我们的3D语义标签是通过一个高效的自动化过程获得的，该过程将人工注释的2D标签从多个视图转移到3D点云中，从而避免了在3D中进行昂贵且耗时的人工注释的需要。我们介绍了2D和3D语义分割的基准，并评估了最近的各种深度学习技术，以展示自然环境中语义分割的挑战。我们建议为标准基准和领域自适应基准训练val测试分割，并利用自动分割生成技术来确保类标签分布的平衡。数据、评估脚本和预训练模型将在https://csiro-robotics.github.io/WildScenes. et.al.|[2312.15364](http://arxiv.org/abs/2312.15364)|null|

<p align=right>(<a href=#updated-on-20240104>back to top</a>)</p>

## Diffusion

|Publish Date|Title|Abstract|PDF|Code|
|---|---|---|---|---|
|**2024-01-03**|**From Audio to Photoreal Embodiment: Synthesizing Humans in Conversations**|我们提出了一个框架，用于生成根据二元交互的会话动态进行手势的完整照片真实感化身。给定语音音频，我们为个人输出多种手势运动的可能性，包括面部、身体和手。我们的方法背后的关键是将矢量量化的样本多样性与通过扩散获得的高频细节相结合，以生成更动态、更具表现力的运动。我们使用高度逼真的化身来可视化生成的运动，这些化身可以表达手势中的关键细微差别（例如冷笑和假笑）。为了促进这一研究，我们引入了第一个允许照片真实感重建的多视图会话数据集。实验表明，我们的模型可以生成适当且多样化的手势，优于仅扩散和仅VQ的方法。此外，我们的感知评估强调了真实感（相对于网格）在准确评估会话手势中细微运动细节方面的重要性。在线提供代码和数据集。 et.al.|[2401.01885](http://arxiv.org/abs/2401.01885)|null|
|**2024-01-03**|**Dissipative fracton superfluids**|我们对具有偶极对称性的超流体的流体动力学理论进行了全面的研究。以扩散为例，我们系统地构建了一个流体动力学框架，该框架包含了固有的偶极自由度，类似于微极（有自旋）流体中的自旋密度。随后，我们研究了偶极凝聚相，并提出了一个捕捉 $U（1）$ 电荷自发断裂的模型。该理论解释了反希格斯约束对这类理论的作用，并自然产生了无间隙场。接下来，我们使用哈密顿形式引入有限温度理论，并研究理想分形超流体的流体动力学。最后，我们假设了一个导数计数方案，并使用不可逆热力学的方法结合耗散效应。我们验证了离散关系的一致性，并认为我们的计数是系统的。 et.al.|[2401.01877](http://arxiv.org/abs/2401.01877)|null|
|**2024-01-03**|**DGDNN: Decoupled Graph Diffusion Neural Network for Stock Movement Prediction**|由于随机股间动态和分层股内动态影响股价，预测未来股票趋势对学术界和工业界来说仍然具有挑战性。近年来，图神经网络通过将多只股票公式化为图结构数据，在这个问题上取得了显著的性能。然而，这些方法大多依赖于人工定义的因素来构建静态股票图，而静态股票图未能捕捉到快速演变的股票之间的内在相互依存关系。此外，这些方法往往忽略了股票的层次特征，并失去了内部的独特信息。在这项工作中，我们提出了一种在没有专家知识的情况下实现的新的图学习方法来解决这些问题。首先，从信号处理的角度来看，我们的方法通过熵驱动的边缘生成自动构建动态股票图。然后，我们通过在构造的股票图上的广义图扩散过程，进一步学习股票之间的任务最优相关性。最后，采用解耦的表示学习方案来捕捉不同层次的库存内特征。实验结果表明，在真实世界数据集上，与最先进的基线相比，有了实质性的改进。此外，消融研究和敏感性研究进一步说明了所提出的方法在建立股票间和股票内动态模型方面的有效性。 et.al.|[2401.01846](http://arxiv.org/abs/2401.01846)|null|
|**2024-01-03**|**Aggregation-diffusion phenomena: from microscopic models to free boundary problems**|本文回顾（并扩展）了最近在各种尺度上对聚集-扩散现象建模的一些结果，重点是由于吸引和排斥现象之间的竞争而出现的集体动力学，特别是（但不限于）在吸引趋化性现象的背景下。在微观尺度上，粒子（或其他试剂）由半径 $\delta>0$的球体表示，我们讨论了软球模型（压力项惩罚粒子的重叠）和硬球模型（其中禁止重叠）。第一种情况导致所谓的“”blob模型“最近作为一种近似粒子系统非线性扩散的工具受到了一些关注。硬球模型类似于拥挤人群运动的经典模型。我们回顾了这些模型的适定性结果，并讨论了它们与极限$\delta\to$ 下聚集扩散现象的经典连续体描述的关系：经典非线性drift扩散方程及其不可压缩对应方程。在论文的第二部分中，我们讨论了在适当的空间和时间尺度上考虑大量粒子时尖锐界面的出现和演化的最新结果：在一些中间时间尺度上，发生相分离，出现尖锐的界面，该界面根据Stefan自由边界问题演化（并且密度函数最终松弛到特征函数——原始问题的亚稳稳态）。在更大的时间尺度上，吸引力导致表面张力现象，尖锐界面的演化可以用具有表面张力的Hele-Shaw自由边界问题来描述。在同一时间尺度上，我们还将讨论有界域中集合问题的接触角条件的出现。 et.al.|[2401.01840](http://arxiv.org/abs/2401.01840)|null|
|**2024-01-03**|**Moonshot: Towards Controllable Video Generation and Editing with Multimodal Conditions**|大多数现有的视频扩散模型（VDM）仅限于文本条件。因此，他们通常缺乏对所生成视频的视觉外观和几何结构的控制。这项工作介绍了Moonshot，这是一种新的视频生成模型，它同时处理图像和文本的多模式输入。该模型建立在一个称为多模式视频块（MVB）的核心模块之上，该模块由用于表示视频特征的传统时空层和用于处理图像和文本输入以进行外观调节的解耦交叉注意力层组成。此外，我们仔细设计了模型架构，使其可以选择性地与预先训练的图像ControlNet模块集成，以适应几何视觉条件，而不需要与现有方法相比的额外训练开销。实验表明，与现有模型相比，Moonshot具有多种多模式调节机制，在视觉质量和时间一致性方面有了显著提高。此外，该模型可以很容易地重新用于各种生成应用，如个性化视频生成、图像动画和视频编辑，揭示了其作为可控视频生成的基本架构的潜力。模型将于公开https://github.com/salesforce/LAVIS. et.al.|[2401.01827](http://arxiv.org/abs/2401.01827)|**[link](https://github.com/salesforce/lavis)**|
|**2024-01-03**|**aMUSEd: An Open MUSE Reproduction**|我们提出了aMUSEd，这是一个开源的、轻量级的掩码图像模型（MIM），用于基于MUSE的文本到图像生成。aMUSEd拥有10%的MUSE参数，专注于快速图像生成。我们认为，与文本到图像生成的主流方法潜在扩散相比，MIM的探索不足。与潜在扩散相比，MIM需要更少的推理步骤，并且更易于解释。此外，可以对MIM进行微调，以便仅使用单个图像学习其他样式。我们希望通过展示MIM在大规模文本到图像生成和发布可复制训练代码方面的有效性，鼓励对其进行进一步探索。我们还发布了两种型号的检查点，它们直接生成256x256和512x512分辨率的图像。 et.al.|[2401.01808](http://arxiv.org/abs/2401.01808)|null|
|**2024-01-03**|**CoMoSVC: Consistency Model-based Singing Voice Conversion**|基于扩散的歌声转换（SVC）方法取得了显著的性能，产生了与目标音色高度相似的自然音频。然而，迭代采样过程导致推理速度慢，因此加速变得至关重要。在本文中，我们提出了CoMoSVC，这是一种基于一致性模型的SVC方法，旨在实现高质量的生成和高速采样。首先为SVC专门设计了一个基于扩散的教师模型，并在自洽性质下进一步提炼学生模型，实现一步采样。在单个NVIDIA GTX4090 GPU上的实验表明，尽管CoMoSVC的推理速度明显快于最先进的（SOTA）基于扩散的SVC系统，但基于主观和客观指标，它仍然实现了相当或优越的转换性能。音频样本和代码可在https://comosvc.github.io/. et.al.|[2401.01792](http://arxiv.org/abs/2401.01792)|null|
|**2024-01-03**|**Short-time expansion of one-dimensional Fokker-Planck equations with heterogeneous diffusion**|对于随机积分的离散化参数 $0\leq\alpha\leq1$的一般值，我们对从具有高斯白噪声的随机过程导出的具有空间相关扩散系数的一维Fokker-Planck方程进行了短时展开。福克-普朗克方程（传播子）的核可以表示为奇异项和正则项的乘积。虽然奇异项可以以闭合形式给出，但正则项可以从系数服从简单常微分方程的泰勒展开式计算。我们用统计物理学和生物物理学中的例子来说明我们的方法的应用。此外，我们还展示了我们的形式主义如何允许定义一类可以精确处理的随机方程。扩展的收敛性不能独立于离散化参数$\alpha$ 来保证。 et.al.|[2401.01765](http://arxiv.org/abs/2401.01765)|null|
|**2024-01-03**|**Necessary conditions for the formation of filaments and star clusters in the cold neutral medium**|恒星的形成发生在丝状分子云中，这些分子云是由冷中性介质（CNM）中发生的物理过程产生的。我们讨论了这种扩散（ $n\约30$cm$^｛-3｝$）、冷（T$\约60 K）、经过冲击波和超音速湍流的磁化气体产生能够分裂成团簇形成区域的丝状结构的必要条件。使用RAMSES和磁化CNM环境作为我们的初始条件，我们模拟了一个0.5 kpc的湍流箱，以模拟磁场强度为7$\mu G$的均匀气体，通过衰减湍流改变3D速度色散。我们使用320 M_｛\dot｝pc^｛-2｝$的表面密度，代表银河系和典型发光星系的内部4.0 kpc CMZ。丝状分子云是通过在5-10 km/s的CNM中的狭窄速度分散范围内的冲击动态形成的，优选值为8km/s。团簇汇粒子出现在超过其临界线质量的细丝中，最适合速度分散为8km/s。追踪磁场的演变，我们发现它们导致的恒星形成气体密度是纯水力运行的两倍。磁场和细丝之间的垂直方向可以增加细丝的吸积率，从而增加它们的线质量。因为磁场有助于支持气体，MHD运行导致平均温度比未磁化的对应物高一个数量级。最后，我们发现磁场将团簇形成的开始延迟$\pro至0.4$ Myr。 et.al.|[2401.01737](http://arxiv.org/abs/2401.01737)|null|
|**2024-01-03**|**An accurate reaction-diffusion limit to the spherical-symmetric Boltzmann equation**|我们解决了一个长期存在的问题，即球对称输运方程的适当有效扩散系数，它在很长一段时间内都是有效的。为此，我们推广了均匀介质的三维输运解，包括一般碰撞性质，包括出生-死亡事件和线性各向异性散射。这是通过引入一个精确的比例律来实现的，该比例律将纯散射情况下的格林函数与一般碰撞情况联系起来，并使用确定性和蒙特卡罗模拟进行了验证。重要的是，有效扩散系数是通过长时间检查传输溶液来确定的。 et.al.|[2401.01726](http://arxiv.org/abs/2401.01726)|null|

<p align=right>(<a href=#updated-on-20240104>back to top</a>)</p>

## NeRF

|Publish Date|Title|Abstract|PDF|Code|
|---|---|---|---|---|
|**2023-12-30**|**PlanarNeRF: Online Learning of Planar Primitives with Neural Radiance Fields**|从视觉数据中识别空间完整的平面基元是计算机视觉中的一项关键任务。现有的方法在很大程度上局限于2D片段恢复或简化3D结构，即使具有广泛的平面注释。我们提出了PlanarNeRF，这是一种能够通过在线学习检测密集3D平面的新框架。PlanarNeRF利用神经场表示，带来了三个主要贡献。首先，它利用并行的外观和几何知识增强了三维平面检测。其次，提出了一种轻量级的平面拟合模块来估计平面参数。第三，引入了一种具有更新机制的新的全局内存库结构，确保了跨帧一致性。PlanarNeRF的灵活架构使其能够在二维监督和自监督解决方案中发挥作用，在每种解决方案中，它都可以有效地从稀疏的训练信号中学习，显著提高训练效率。通过广泛的实验，我们证明了PlanarNeRF在各种场景下的有效性，并比现有工作有了显著的改进。 et.al.|[2401.00871](http://arxiv.org/abs/2401.00871)|null|
|**2024-01-01**|**Deblurring 3D Gaussian Splatting**|最近对辐射场的研究为具有照片级真实感渲染质量的新颖视图合成铺平了坚实的道路。然而，它们通常使用神经网络和体积绘制，这两种方法的训练成本很高，并且由于绘制时间长，阻碍了它们在各种实时应用中的广泛使用。最近，人们提出了一种基于3D高斯散射的方法来对3D场景进行建模，并在实时渲染图像的同时实现了显著的视觉质量。然而，如果训练图像模糊，则渲染质量会严重下降。模糊通常是由于镜头散焦、物体运动和相机抖动而产生的，它不可避免地会干扰干净图像的获取。先前的几项研究试图使用神经场从模糊的输入图像中渲染干净清晰的图像。然而，这些工作中的大多数仅设计用于基于体积渲染的神经辐射场，并不直接适用于基于光栅化的3D高斯散射方法。因此，我们提出了一种新的实时去模糊框架，即去模糊3D高斯散点，使用小型多层感知器（MLP）来操纵每个3D高斯的协方差来对场景模糊度进行建模。虽然去模糊的3D高斯飞溅仍然可以享受实时渲染，但它可以从模糊的图像中重建精细和清晰的细节。在基准上进行了各种实验，结果表明了我们的去模糊方法的有效性。定性结果可在https://benhenryl.github.io/Deblurring-3D-Gaussian-Splatting/ et.al.|[2401.00834](http://arxiv.org/abs/2401.00834)|null|
|**2023-12-22**|**Fluid Simulation on Neural Flow Maps**|我们介绍了神经流图，这是一种新的模拟方法，将新兴的隐式神经表示范式与基于流图理论的流体模拟相结合，以实现最先进的无粘流体现象模拟。我们设计了一种新的混合神经场表示，空间稀疏神经场（SSNF），它将小型神经网络与重叠、多分辨率和空间稀疏网格的金字塔相融合，以高精度紧凑地表示长期时空速度场。有了这个神经速度缓冲器，我们以机械对称的方式计算长期双向流图及其雅可比矩阵，以促进对现有解决方案的大幅精度提高。这些长程双向流图实现了低耗散的高平流精度，进而促进了高保真度的不可压缩流模拟，显示了复杂的旋涡结构。我们展示了我们的神经流体模拟在各种具有挑战性的模拟场景中的有效性，包括跳跃涡流、碰撞涡流、涡流重新连接，以及移动障碍物和密度差异产生的涡流。我们的例子表明，在能量守恒、视觉复杂性、对实验观测的遵守以及详细旋涡结构的保存方面，与现有方法相比，性能有所提高。 et.al.|[2312.14635](http://arxiv.org/abs/2312.14635)|null|
|**2023-12-21**|**Geometric Awareness in Neural Fields for 3D Human Registration**|将模板与三维人体点云对齐是一个长期存在的问题，对于动画、重建和启用监督学习管道等任务至关重要。最近的数据驱动方法利用了预测的表面对应关系；然而，它们对不同的姿态或分布并不鲁棒。相比之下，工业解决方案往往依赖于昂贵的手动注释或多视图捕获系统。最近，神经场已经显示出有希望的结果，但它们纯粹的数据驱动性质缺乏几何意识，通常导致模板配准的微小错位。在这项工作中，我们提出了两种解决方案：LoVD，一种新的神经场模型，它预测朝向目标表面上的局部SMPL顶点的方向；和INT，这是第一个专门用于神经领域的自监督任务，在测试时，它利用目标几何结构来细化主干。我们将它们组合到INLoVD中，这是一个在大型MoCap数据集上训练的强大的3D人体注册管道。INLoVD是高效的（不到一分钟），在公共基准上稳定地达到了最先进的水平，并对分布外的数据提供了前所未有的概括。我们将在\url｛url｝中发布代码和检查点。 et.al.|[2312.14024](http://arxiv.org/abs/2312.14024)|null|
|**2023-12-20**|**Neural feels with neural fields: Visuo-tactile perception for in-hand manipulation**|为了实现人类水平的灵活性，机器人必须从多模式感知推断空间意识，以推理接触互动。在新物体的手操作过程中，这种空间意识包括估计物体的姿势和形状。手内感知的现状主要采用视觉，并局限于跟踪先验已知对象。此外，在操作过程中，手上物体的视觉遮挡迫在眉睫，这阻止了当前系统在没有遮挡的情况下超越任务。我们将多指手的视觉和触摸传感相结合，在手内操作过程中估计物体的姿势和形状。我们的方法NeuralFeels通过在线学习神经场来编码对象几何，并通过优化姿态图问题来联合跟踪它。我们研究了模拟和现实世界中的多模式手部感知，通过本体感觉驱动的策略与不同的物体进行交互。我们的实验显示，使用已知的CAD模型，最终重建F分数为 $81$%，平均姿势漂移为$4.7\，\text｛mm｝$，进一步降低到$2.3\，\text{mm｝$。此外，我们观察到，与仅使用视觉的方法相比，在严重的视觉遮挡下，我们可以实现高达94$ %的跟踪改进。我们的研究结果表明，在手部操作过程中，触摸至少可以改善视觉估计，并在最好的情况下消除视觉估计的歧义。我们发布了70个实验的评估数据集FeelSight，作为在该领域进行基准测试的一步。我们由多模态感知驱动的神经表示可以作为提高机器人灵活性的感知支柱。视频可以在我们的项目网站上找到https://suddhu.github.io/neural-feels/ et.al.|[2312.13469](http://arxiv.org/abs/2312.13469)|null|
|**2023-12-20**|**Deep Learning on 3D Neural Fields**|近年来，神经场（NFs）已成为编码各种连续信号（如图像、视频、音频和3D形状）的有效工具。当应用于3D数据时，NFs提供了一种解决方案来解决与流行的离散表示相关的碎片化和局限性。然而，鉴于神经网络本质上是神经网络，目前尚不清楚它们是否以及如何无缝集成到深度学习管道中，以解决下游任务。本文解决了这一研究问题，并介绍了nf2vec，这是一个能够在单个推理过程中为输入NF生成紧凑的潜在表示的框架，同时专门处理NFs。我们在几个用于表示3D曲面的NFs上测试了这个框架，例如无符号/有符号距离和占用字段。此外，我们用更复杂的NFs证明了我们的方法的有效性，这些NFs包括3D对象的几何形状和外观，如神经辐射场。 et.al.|[2312.13277](http://arxiv.org/abs/2312.13277)|null|
|**2023-12-16**|**How to Train Neural Field Representations: A Comprehensive Study and Benchmark**|神经场（NeFs）最近已成为一种用于对各种模态（包括图像、形状和场景）的信号进行建模的通用方法。随后，许多工作探索了使用NeF作为下游任务的表示，例如，根据适合的NeF的参数对图像进行分类。然而，NeF超参数对其作为下游表示的质量的影响很少被理解，而且在很大程度上仍未被探索。这在一定程度上是由于拟合神经场数据集所需的大量时间造成的。在这项工作中，我们提出了 $\verb|fit-a-nef|$ ，这是一个基于JAX的库，它利用并行化来实现大规模nef数据集的快速优化，从而显著加快速度。有了这个库，我们进行了一项全面的研究，研究了不同超参数——包括初始化、网络架构和优化策略——对下游任务的NeF拟合的影响。我们的研究为如何训练NeF提供了宝贵的见解，并为优化其在下游应用中的有效性提供了指导。最后，基于所提出的库和我们的分析，我们提出了Neural Field Arena，这是一个由流行视觉数据集的神经场变体组成的基准，包括MNIST、CIFAR、ImageNet和ShapeNetv2的变体。我们的图书馆和神经领域竞技场将是开源的，以引入标准化的基准测试，并促进对神经领域的进一步研究。 et.al.|[2312.10531](http://arxiv.org/abs/2312.10531)|**[link](https://github.com/samuelepapa/fit-a-nef)**|
|**2023-12-18**|**LatentEditor: Text Driven Local Editing of 3D Scenes**|虽然神经领域在视图合成和场景重建方面取得了重大进展，但由于其对来自多视图输入的几何和纹理信息的隐式编码，编辑它们带来了巨大的挑战。在本文中，我们介绍了\textsc｛LatentEditor｝，这是一个创新的框架，旨在让用户能够使用文本提示对神经字段进行精确和本地控制的编辑。利用去噪扩散模型，我们成功地将真实世界的场景嵌入到潜在空间中，与传统方法相比，产生了更快、更具适应性的NeRF主干进行编辑。为了提高编辑精度，我们引入了一个delta分数来计算潜在空间中的2D掩模，该分数可以作为局部修改的指南，同时保留不相关的区域。我们新颖的像素级评分方法利用InstructPix2Pix（IP2P）的能力来辨别潜在空间中IP2P条件和无条件噪声预测之间的差异。然后在训练集中迭代地更新以2D掩码为条件的编辑的潜伏时间，以实现3D局部编辑。与现有的3D编辑模型相比，我们的方法实现了更快的编辑速度和卓越的输出质量，弥合了文本指令和潜在空间中高质量3D场景编辑之间的差距。我们在LLFF、IN2N、NeRFStudio和NeRFArt四个基准3D数据集上展示了我们的方法的优势。 et.al.|[2312.09313](http://arxiv.org/abs/2312.09313)|**[link](https://github.com/umarkhalidAI/LatentEditor)**|
|**2023-12-14**|**ZeroRF: Fast Sparse View 360° Reconstruction with Zero Pretraining**|我们提出了ZeroRF，这是一种新的每场景优化方法，解决了神经场表示中稀疏视图360重建的挑战。目前的突破，如神经辐射场（NeRF）已经证明了高保真度的图像合成，但难以处理稀疏的输入视图。现有的方法，如可泛化的NeRF和每场景优化方法，在数据依赖性、计算成本和跨不同场景的泛化方面面临限制。为了克服这些挑战，我们提出了ZeroRF，其关键思想是将定制的深度图像先验集成到因子分解的NeRF表示中。与传统方法不同，ZeroRF使用神经网络生成器对特征网格进行参数化，从而实现高效的稀疏视图360重建，而无需任何预训练或额外的正则化。大量实验展示了ZeroRF在质量和速度方面的多功能性和优势，在基准数据集上取得了最先进的结果。ZeroRF的意义延伸到3D内容生成和编辑的应用。项目页面：https://sarahweiii.github.io/zerorf/ et.al.|[2312.09249](http://arxiv.org/abs/2312.09249)|null|
|**2023-12-12**|**SMERF: Streamable Memory Efficient Radiance Fields for Real-Time Large-Scene Exploration**|最近的实时视图合成技术在保真度和速度上迅速进步，现代方法能够以交互式帧速率渲染接近照片级真实感的场景。与此同时，在易于光栅化的显式场景表示和基于射线行进的神经场之间出现了紧张关系，后者的最先进实例在质量上超过了前者，同时对于实时应用来说成本高得令人望而却步。在这项工作中，我们介绍了SMERF，这是一种视图合成方法，在占地面积高达3亿 $^2$、体积分辨率为3.5毫米$^3$ 的大型场景中，它实现了实时方法中最先进的精度。我们的方法建立在两个主要贡献之上：一个是分层模型划分方案，它在限制计算和内存消耗的同时增加了模型容量，另一个是蒸馏训练策略，它同时产生高保真度和内部一致性。我们的方法能够在网络浏览器中实现全六自由度（6DOF）导航，并在商品智能手机和笔记本电脑上实时渲染。大量实验表明，我们的方法在实时新视图合成方面，在标准基准上超过了当前最先进的0.78 dB，在大型场景上超过了1.78 dB，渲染帧的速度比最先进的辐射场模型快三个数量级，并在包括智能手机在内的各种商品设备上实现了实时性能。我们鼓励读者在我们的项目网站上亲自探索这些模型：https://smerf-3d.github.io. et.al.|[2312.07541](http://arxiv.org/abs/2312.07541)|null|

<p align=right>(<a href=#updated-on-20240104>back to top</a>)</p>

[contributors-shield]: https://img.shields.io/github/contributors/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[contributors-url]: https://github.com/Vincentqyw/cv-arxiv-daily/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[forks-url]: https://github.com/Vincentqyw/cv-arxiv-daily/network/members
[stars-shield]: https://img.shields.io/github/stars/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[stars-url]: https://github.com/Vincentqyw/cv-arxiv-daily/stargazers
[issues-shield]: https://img.shields.io/github/issues/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[issues-url]: https://github.com/Vincentqyw/cv-arxiv-daily/issues

