[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]

## Updated on 2024.07.03
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
|**2024-06-28**|**ASSR-NeRF: Arbitrary-Scale Super-Resolution on Voxel Grid for High-Quality Radiance Fields Reconstruction**|基于NeRF的方法通过构建具有隐式或显式表示的辐射场来重建3D场景。虽然基于NeRF的方法可以在任意尺度上执行新视图合成（NVS），但在具有低分辨率（LR）优化的高分辨率新视图综合（HRNVS）中的性能往往导致过度平滑。另一方面，单图像超分辨率（SR）旨在将LR图像增强到HR图像，但缺乏多视点一致性。为了应对这些挑战，我们提出了任意尺度超分辨率NeRF（ASSR-NeRF），这是一种用于超分辨率新视图合成（SRNVS）的新框架。我们提出了一种基于注意力的VoxelGridSR模型来直接对优化的体积执行3D超分辨率（SR）。我们的模型在不同的场景中进行了训练，以确保可推广性。对于用LR视图训练的看不见的场景，我们可以直接应用我们的VoxelGridSR来进一步细化体积并实现多视图一致SR。我们从数量和质量上证明了所提出的方法在SRNVS中取得了显著的性能。 et.al.|[2406.20066](http://arxiv.org/abs/2406.20066)|null|
|**2024-06-27**|**360 in the Wild: Dataset for Depth Prediction and View Synthesis**|大量的透视相机数据集促进了用于各种任务的新的基于学习的策略的出现，如相机定位、单图像深度估计或视图合成。然而，全景或全向图像数据集，包括姿势和深度等基本信息，大多是用合成场景制作的。在这项工作中，我们介绍了一个大规模的野外360 $^｛\circ｝$ 视频数据集。这个数据集是从互联网上仔细收集的，并从世界各地捕获。因此，该数据集展示了非常多样化的环境（例如，室内和室外）和上下文（例如，有和没有移动物体）。构成我们数据集的25K幅图像中的每一幅都提供了其各自相机的姿势和深度图。我们说明了我们的数据集与两个主要任务的相关性，即单图像深度估计和视图合成。 et.al.|[2406.18898](http://arxiv.org/abs/2406.18898)|null|
|**2024-06-26**|**Dynamic Gaussian Marbles for Novel View Synthesis of Casual Monocular Videos**|高斯散射已经成为新视图合成的一种流行表现，在效率、光度质量和成分可食性方面表现出明显的优势。在其成功之后，许多工作已经将高斯扩展到4D，表明动态高斯保持了这些优势，同时也比替代表示更好地跟踪场景几何。然而，这些方法假设密集的多视图视频作为监督，限制了它们在受控捕捉设置中的使用。在这项工作中，我们将高斯场景表示的能力扩展到随意捕捉的单目视频。我们表明，现有的4D高斯方法在这种设置中显著失败，因为单目设置约束不足。基于这一发现，我们提出了动态高斯大理石（DGMarbles），由三个核心修改组成，针对单目设置的困难。首先，DGMarbles使用各向同性的高斯“弹珠”，减少每个高斯的自由度，并将优化约束为关注局部形状的运动和外观。其次，DGMarbles采用分层分治学习策略来引导优化朝着具有连贯运动的解决方案前进。最后，DGMarbles将图像级和几何级先验添加到优化中，包括利用点跟踪的最新进展的跟踪损失。通过以这些方式约束优化，DGMarbles学习高斯轨迹，从而实现新颖的视图渲染并准确捕捉场景元素的3D运动。我们在（单眼）Nvidia Dynamic Scenes数据集和Dycheck iPhone数据集上进行了评估，结果表明DGMarbles在质量上显著优于其他高斯基线，与非高斯表示不相上下，同时保持了高斯的效率、合成性、可编辑性和跟踪优势。 et.al.|[2406.18717](http://arxiv.org/abs/2406.18717)|null|
|**2024-06-26**|**MultiDiff: Consistent Novel View Synthesis from a Single Image**|我们介绍了MultiDiff，这是一种从单个RGB图像中对场景进行一致新颖视图合成的新方法。从单个参考图像合成新视图的任务是自然造成的，因为对未观察到的区域存在多种看似合理的解释。为了解决这个问题，我们以单目深度预测器和视频扩散模型的形式结合了强先验。单目深度使我们能够根据目标视图的扭曲参考图像来调整模型，从而提高几何稳定性。视频扩散先验为3D场景提供了强大的代理，允许模型学习生成图像之间的连续和像素精确的对应关系。与依赖于易于漂移和误差累积的自回归图像生成的方法不同，MultiDiff联合合成一系列帧，从而产生高质量和多视图一致的结果——即使是对于具有大相机移动的长期场景生成，同时将推理时间减少一个数量级。为了进一步提高一致性和图像质量，我们引入了一种新颖的结构化噪声分布。我们的实验结果表明，MultiDiff在具有挑战性的真实世界数据集RealEstate10K和ScanNet上优于最先进的方法。最后，我们的模型自然支持多视图一致性编辑，而无需进一步调整。 et.al.|[2406.18524](http://arxiv.org/abs/2406.18524)|null|
|**2024-06-27**|**XLD: A Cross-Lane Dataset for Benchmarking Novel Driving View Synthesis**|彻底测试自动驾驶系统对于追求安全的自动驾驶汽车至关重要。这就需要创建超出现实世界数据安全收集范围的安全关键场景，因为其中许多场景在公共道路上很少发生。然而，大多数现有NVS方法的评估依赖于对来自训练数据的图像帧的零星采样，使用度量将渲染图像与真实图像进行比较。遗憾的是，该评估协议不能满足闭环仿真的实际要求。具体而言，真正的应用程序需要渲染超出原始轨迹的新颖视图（如跨车道视图）的能力，而这些视图在现实世界中很难捕捉。为了解决这一问题，本文提出了一种专门为自动驾驶模拟设计的新型驾驶视图合成数据集和基准。该数据集是独特的，因为它包括通过偏离训练轨迹1-4米而捕获的测试图像。它包括六个序列，包括不同的时间和天气条件。每个序列包含450个训练图像、150个测试图像以及它们对应的相机姿态和固有参数。利用这一新颖的数据集，我们建立了第一个现实的基准，用于在仅前置和多摄像头设置下评估现有的NVS方法。实验结果强调了当前方法中存在的显著差距，揭示了它们不足以满足跨车道或闭环模拟的苛刻先决条件。我们的数据集在项目页面上公开发布：https://3d-aigc.github.io/XLD/. et.al.|[2406.18360](http://arxiv.org/abs/2406.18360)|null|
|**2024-06-26**|**VDG: Vision-Only Dynamic Gaussian for Driving Simulation**|动态高斯飞溅已经在新颖的视图中带来了令人印象深刻的场景重建和图像合成进展。然而，现有的方法在很大程度上依赖于预先计算的姿态和通过运动结构（SfM）算法或昂贵的传感器进行的高斯初始化。本文首次通过将自监督VO集成到我们的无姿态动态高斯方法（VDG）中来解决这个问题，以促进姿态和深度初始化以及静态动态分解。此外，与无姿态动态视图合成方法相比，VDG可以仅使用RGB图像输入，以更快的速度和更大的场景构建动态场景。我们通过大量的定量和定性实验证明了我们的方法的稳健性。与最先进的动态视图合成方法相比，我们的结果显示出良好的性能。其他视频和源代码将发布在我们的项目页面上https://3d-aigc.github.io/VDG. et.al.|[2406.18198](http://arxiv.org/abs/2406.18198)|null|
|**2024-06-26**|**View-Invariant Pixelwise Anomaly Detection in Multi-object Scenes with Adaptive View Synthesis**|基础设施资产的检查和监控通常需要识别随着时间的推移定期拍摄的场景中的视觉异常。手动或使用机器人（如无人机）在不同时间点从同一场景收集的图像通常不会完全对齐。有监督的分割方法可以用于识别已知问题，但当出现未知异常时，需要无监督的异常检测方法。当前的无监督像素级异常检测方法主要是针对相机位置已知且恒定的工业环境开发的。然而，我们发现这些方法不能推广到图像没有完全对齐的情况。我们将两组不完全对齐的图像之间的无监督异常检测问题称为场景异常检测（Scene AD）。我们提出了一种称为OmniAD的新型网络来解决场景AD问题。具体来说，我们改进了异常检测方法反向蒸馏，以实现像素级异常检测性能提高40%。提出了两种新的数据增强策略，利用新颖的视图合成和相机定位来提高泛化能力，进一步证明了网络的性能得到了改善。我们在新的数据集ToyCity上验证了我们的方法，ToyCity是第一个具有多个对象的场景广告数据集，以及在已建立的以单个对象为中心的数据集MAD上验证了定性和定量结果。https://drags99.github.io/OmniAD/ et.al.|[2406.18012](http://arxiv.org/abs/2406.18012)|null|
|**2024-06-25**|**NerfBaselines: Consistent and Reproducible Evaluation of Novel View Synthesis Methods**|新颖的视图合成是许多应用中的一个重要问题，包括AR/VR、游戏和机器人模拟。随着神经辐射场（NeRF）和3D高斯散射（3DGS）方法的快速发展，由于使用不同评估协议的方法、难以安装和使用的代码库以及不能很好地推广到新的3D场景的方法，跟踪当前技术状态（SoTA）变得越来越困难。我们的实验支持了这一说法，表明各种方法的评估协议之间的微小差异可能导致报告的指标不一致。为了解决这些问题，我们提出了一个名为NerfBaselines的框架，它简化了各种方法的安装，提供了一致的基准测试工具，并确保了可重复性。我们通过复制原始论文中报告的数字来实验验证我们的实现。为了进一步提高可访问性，我们发布了一个网络平台，在标准基准上对常用方法进行比较。网状物https://jkulhanek.com/nerfbaselines et.al.|[2406.17345](http://arxiv.org/abs/2406.17345)|null|
|**2024-06-24**|**Reducing the Memory Footprint of 3D Gaussian Splatting**|3D高斯飞溅为新颖的视图合成提供了卓越的视觉质量，具有快速训练和实时渲染；不幸的是，这种方法对存储和传输的内存要求非常高。我们首先分析了原因，确定了可以减少存储的三个主要区域：用于表示场景的3D高斯基元的数量、用于表示方向辐射的球面谐波的系数数量以及存储高斯基元属性所需的精度。我们提出了每一个问题的解决方案。首先，我们提出了一种高效的、具有分辨率意识的原始修剪方法，将原始计数减少一半。其次，我们引入了一种自适应调整方法来选择用于表示每个高斯基元的方向辐射的系数数量，最后引入了一个基于码本的量化方法，以及用于进一步减少内存的半浮点表示。总之，这三个组件使我们测试的标准数据集的磁盘总大小减少了27，同时渲染速度加快了1.7。我们在标准数据集上演示了我们的方法，并展示了在移动设备上使用该方法时，我们的解决方案如何显著缩短下载时间。 et.al.|[2406.17074](http://arxiv.org/abs/2406.17074)|null|
|**2024-06-24**|**Articulate your NeRF: Unsupervised articulated object modeling via conditional view synthesis**|我们提出了一种新的无监督方法来学习具有刚性零件的关节对象的姿态和零件分割。给定一个物体在不同关节状态下的两个观察结果，我们的方法通过使用第一个观察结果的隐式模型来学习物体零件的几何形状和外观，从第二个观察结果中提取零件分割和关节，同时呈现后一个观察结果。此外，为了解决零件分割和连接联合优化的复杂性，我们提出了一种基于体素网格的初始化策略和解耦优化程序。与先前的无监督工作相比，我们的模型获得了显著更好的性能，并推广到具有多个部分的对象，同时它可以有效地从少数视图进行后期观察。 et.al.|[2406.16623](http://arxiv.org/abs/2406.16623)|null|

<p align=right>(<a href=#updated-on-20240703>back to top</a>)</p>

## 3D Reconstruction

|Publish Date|Title|Abstract|PDF|Code|
|---|---|---|---|---|
|**2024-06-28**|**Odd-One-Out: Anomaly Detection by Comparing with Neighbors**|本文介绍了一种新的异常检测（AD）问题，该问题的重点是识别相对于场景中其他实例的“奇怪的”对象。与传统的AD基准不同，在我们的设置中，这种情况下的异常是特定于场景的，由占大多数的常规实例定义。由于对象实例通常从单个视点部分可见，因此我们的设置提供每个场景的多个视图作为输入。为了为未来的研究提供一个试验台，我们介绍了两个基准，ToysAD-8K和PartsAD-15K。我们提出了一种新的方法，该方法为每个实例生成以对象为中心的3D表示，并通过实例之间的交叉检查来检测异常表示。我们在给出的基准中对我们的方法进行了严格的定量和定性分析。 et.al.|[2406.20099](http://arxiv.org/abs/2406.20099)|**[link](https://github.com/VICO-UoE/OddOneOutAD)**|
|**2024-06-28**|**SpotlessSplats: Ignoring Distractors in 3D Gaussian Splatting**|三维高斯散射（3DGS）是一种很有前途的三维重建技术，它提供了高效的训练和渲染速度，适用于实时应用。然而，当前的方法需要高度受控的环境（没有移动的人或风吹的元素，以及一致的照明）来满足3DGS的视图间一致性假设。这使得真实世界捕捉的重建成为问题。我们提出了SpotlessSplats，这是一种利用预先训练的通用功能与稳健优化相结合的方法，可以有效地忽略瞬态干扰因素。我们的方法在随意捕捉的情况下，在视觉和数量上都达到了最先进的重建质量。 et.al.|[2406.20055](http://arxiv.org/abs/2406.20055)|null|
|**2024-06-28**|**Deep Learning-based Depth Estimation Methods from Monocular Image and Videos: A Comprehensive Survey**|由于其在自动驾驶、3D重建、数字娱乐和机器人等许多领域的应用，从单个RGB图像和视频中估计深度引起了广泛的兴趣。在过去的10年里，已经发表了500多篇基于深度学习的论文，这表明人们对这项任务的兴趣越来越大。本文对现有的基于深度学习的方法、它们所面临的挑战以及它们在架构和监督方法方面的发展进行了全面的调查。它提供了一种分类法，用于根据输入和输出模式、网络架构和学习方法对当前工作进行分类。它还讨论了单目深度估计历史上的主要里程碑，以及现有方法中使用的不同管道、数据集和评估指标。 et.al.|[2406.19675](http://arxiv.org/abs/2406.19675)|null|
|**2024-06-28**|**LiverUSRecon: Automatic 3D Reconstruction and Volumetry of the Liver with a Few Partial Ultrasound Scans**|肝脏体积测量的三维重建对于定性分析和疾病诊断非常重要。使用超声（US）扫描的肝脏容量测定虽然由于采集时间和安全性较短而具有优势，但由于超声扫描固有的噪声、边界模糊和部分肝脏可见性，因此具有挑战性。我们通过使用肝脏的一些不完全矢状面US扫描的分割掩模，以及使用一组肝脏CT扫描建立的统计形状模型（SSM）来解决这些挑战。我们通过参数回归网络计算扭曲该标准SSM以拟合US扫描所需的形状参数。由此产生的3D肝脏重建是准确的，并导致自动肝脏体积计算。我们使用RMSE评估估计的肝脏体积相对于CT分割体积的准确性。我们的体积计算在统计学上更接近于使用CT扫描估计的体积，而不是放射科医生使用Childs方法计算的体积：p值0.094（>0.05）表明，与Childs方法相比，CT分割体积与我们的体积之间没有显著差异。我们通过对US图像分辨率、用于SSM的CT扫描次数、主成分数量和输入US扫描次数的调查（消融研究）验证了我们的方法。据我们所知，这是第一个使用一些不完整的US扫描的自动肝脏容量测定系统，给出了一组SSM的肝脏CT扫描。 et.al.|[2406.19336](http://arxiv.org/abs/2406.19336)|null|
|**2024-06-26**|**On Scaling Up 3D Gaussian Splatting Training**|三维高斯散射（3DGS）以其优越的视觉质量和渲染速度在三维重建中越来越受欢迎。然而，3DGS训练目前发生在单个GPU上，由于内存限制，限制了其处理高分辨率和大规模3D重建任务的能力。我们介绍了Grendel，这是一个分布式系统，旨在划分3DGS参数并在多个GPU之间并行计算。由于每个高斯影响渲染像素的一个小的动态子集，Grendel采用稀疏的全对全通信将必要的高斯传输到像素分区，并执行动态负载平衡。与一次使用一个相机视图图像进行训练的现有3DGS系统不同，Grendel支持使用多个视图进行批量训练。我们探索了各种优化超参数缩放策略，发现一个简单的sqrt（批量大小）缩放规则是非常有效的。使用大规模、高分辨率场景的评估表明，Grendel通过在多个GPU上放大3DGS参数来提高渲染质量。在Rubble数据集上，我们通过在16个GPU上分布4040万高斯实现了27.28的测试PSNR，而在单个GPU上使用1120万高斯实现的PSNR为26.28。Grendel是一个开源项目，位于：https://github.com/nyu-systems/Grendel-GS et.al.|[2406.18533](http://arxiv.org/abs/2406.18533)|**[link](https://github.com/nyu-systems/grendel-gs)**|
|**2024-06-26**|**Repeat and Concatenate: 2D to 3D Image Translation with 3D to 3D Generative Modeling**|本文研究了一种具有直接技术的2D到3D图像转换方法，使相关的2D X射线到3D CT类重建成为可能。我们观察到，现有的方法在潜在空间中集成多个2D视图的信息，在潜在编码过程中会丢失有价值的信号信息。相反，我们只是简单地重复2D视图并将其连接到更高的通道3D体积中，并将3D重建挑战作为一个简单的3D到3D生成建模问题来解决，从而避开了几个复杂的建模问题。这种方法使重建的3D体积能够保留来自2D输入的有价值的信息，这些信息在Swin UNETR主干中的信道状态之间传递。我们的方法应用了神经最优传输，它快速稳定地进行训练，有效地集成了多个视图中的信号信息，而不需要精确对齐；它产生了即使在有限的训练之后也高度忠实于2D视图的非塌陷重建。我们在单个数据集上训练了我们的模型，并评估了其在六个数据集（包括分布外样本）上的泛化能力，从而展示了定性和定量的相关结果。 et.al.|[2406.18422](http://arxiv.org/abs/2406.18422)|**[link](https://github.com/abrilcf/3d-3d_repeat-concatenate)**|
|**2024-06-26**|**GS-Octree: Octree-based 3D Gaussian Splatting for Robust Object-level 3D Reconstruction Under Strong Lighting**|3D高斯散射技术显著推进了多视图图像辐射场的构建，实现了实时渲染。虽然基于点的光栅化有效地减少了渲染的计算需求，但它往往难以准确重建目标对象的几何结构，尤其是在强光下。为了应对这一挑战，我们引入了一种新的方法，将基于八叉树的隐式曲面表示与高斯飞溅相结合。我们的方法包括四个阶段。最初，它通过体积渲染重建有符号距离场（SDF）和辐射场，并将它们编码在低分辨率八叉树中。初始SDF表示目标对象的粗略几何图形。随后，它引入了3D高斯作为附加自由度，这些自由度由SDF引导。在第三阶段，优化的高斯进一步提高了SDF的精度，与第一阶段获得的初始SDF相比，可以恢复更精细的几何细节。最后，它采用了精细的SDF，通过飞溅进一步优化3D高斯，消除了对视觉外观贡献不大的高斯。实验结果表明，我们的方法利用了具有SDF的3D高斯分布，重建了更精确的几何体，特别是在具有由强光引起的镜面高光的图像中。 et.al.|[2406.18199](http://arxiv.org/abs/2406.18199)|null|
|**2024-06-25**|**Unified Auto-Encoding with Masked Diffusion**|在成功的生成和自我监督表示学习模型的核心，都有一个包含某种形式的图像腐败的重建目标。扩散模型通过预定的高斯破坏过程来实现这种方法，而掩蔽的自动编码器模型则通过掩蔽图像的块来实现。尽管它们的方法不同，但它们方法的潜在相似性为能够同时执行去噪任务的自动编码器提供了一条很有前途的途径。我们提出了一个统一的自监督目标，称为统一掩蔽扩散（UMD），它将基于补丁和基于噪声的破坏技术结合在一个单独的自动编码框架内。具体而言，UMD通过在扩散噪声调度中引入额外的无噪声、高掩蔽表示步骤来修改扩散变换器（DiT）训练过程，并将掩蔽和噪声的混合图像用于后续的时间步长。通过集成对扩散建模和预测屏蔽补丁令牌有用的特征，UMD在下游生成和表示学习任务中实现了强大的性能，包括线性探测和类条件生成。这是在不需要大量数据扩充、多视图或额外编码器的情况下实现的。此外，UMD在总训练时间上提高了先前基于扩散的方法的计算效率。我们在发布代码https://github.com/philippe-eecs/small-vision. et.al.|[2406.17688](http://arxiv.org/abs/2406.17688)|**[link](https://github.com/philippe-eecs/small-vision)**|
|**2024-06-25**|**Test-Time Generative Augmentation for Medical Image Segmentation**|在本文中，我们提出了一种在测试期间增强医学图像分割的新方法。我们主张使用高级域微调生成模型（GM），例如稳定扩散（SD）来增加测试时间，而不是在输入测试图像上使用手工制作的变换或函数来创建多个视图以增加测试时间。考虑到GM已经被训练来理解和封装全面的领域数据知识，它在表示数据特征和分布方面优于分割模型。因此，通过将GM集成到测试时间扩充中，我们可以有效地生成给定测试样本的多个视图，与样本的内容和外观特征以及相关的局部数据分布保持一致。与传统的手工转换相比，这种方法使增强过程更具适应性和弹性。在三个医学图像分割任务（九个数据集）上进行的综合实验证明了所提出的TTGA在增强分割结果方面的有效性和多功能性。此外，TTGA显著提高了像素误差估计，从而有助于部署更可靠的分割系统。代码将在以下位置发布：https://github.com/maxiao0234/TTGA. et.al.|[2406.17608](http://arxiv.org/abs/2406.17608)|**[link](https://github.com/maxiao0234/ttga)**|
|**2024-06-25**|**SyncNoise: Geometrically Consistent Noise Prediction for Text-based 3D Scene Editing**|基于文本的二维扩散模型在图像生成和编辑方面表现出了令人印象深刻的能力。同时，2D扩散模型也表现出用于3D编辑任务的巨大潜力。然而，如何在多个视点之间实现一致的编辑仍然是一个挑战。虽然迭代数据集更新方法能够实现全局一致性，但它存在收敛缓慢和纹理过度平滑的问题。我们提出了SyncNoise，这是一种新颖的几何引导的多视图一致性噪声编辑方法，用于高保真3D场景编辑。SyncNoise使用2D扩散模型同步编辑多个视图，同时强制多视图噪声预测保持几何一致，从而确保语义结构和低频外观的全局一致性。为了进一步增强高频细节的局部一致性，我们设置了一组锚视图，并通过跨视图重投影将它们传播到相邻的帧。为了提高多视图对应的可靠性，我们在训练过程中引入了深度监督，以增强精确几何形状的重建。我们的方法通过增强噪声和像素级别的几何一致性，在尊重文本指令的情况下，特别是在具有复杂纹理的场景中，实现了高质量的3D编辑结果。 et.al.|[2406.17396](http://arxiv.org/abs/2406.17396)|null|

<p align=right>(<a href=#updated-on-20240703>back to top</a>)</p>

## Diffusion

|Publish Date|Title|Abstract|PDF|Code|
|---|---|---|---|---|
|**2024-06-28**|**Auto Cherry-Picker: Learning from High-quality Generative Data Driven by Language**|基于扩散的模型在生成具有各种布局的高质量图像方面显示出巨大的潜力，这有利于下游感知任务。然而，仅由语言驱动的全自动布局生成和用于测量多个生成实例的合适度量尚未得到很好的探索。在这项工作中，我们提出了Auto Cherry Picker（ACP），这是一种新的框架，可以生成高质量的多模式训练示例，以增强感知和多模式训练。从一个简单的自然语言概念列表开始，我们提示大型语言模型（LLM）生成详细的描述并设计合理的布局。接下来，我们使用现成的文本到图像模型来生成多个图像。然后，使用综合设计的度量对生成的数据进行细化，以确保质量。特别地，我们提出了一个新的度量标准，复合布局和图像得分（CLIS），以公平地评估生成的图像。我们的合成高质量示例通过自定义初始概念列表来提高各种场景中的性能，特别是在解决与长尾分布和不平衡数据集相关的挑战方面。对下游任务的实验结果表明，Auto Cherry Picker可以显著提高现有模型的性能。此外，我们还深入研究了CLIS与下游任务中性能提升之间的相关性，发现CLIS得分越高，性能越好。这一发现显示了评估指标作为各种视觉感知和MLLM任务的作用的潜力。代码将可用。 et.al.|[2406.20085](http://arxiv.org/abs/2406.20085)|null|
|**2024-06-28**|**HouseCrafter: Lifting Floorplans to 3D Scenes with 2D Diffusion Model**|我们介绍了HouseCrafter，这是一种新颖的方法，可以将平面图提升到一个完整的大型3D室内场景（例如，房子）中。我们的关键见解是调整在网络规模图像上训练的2D扩散模型，以在场景的不同位置生成一致的多视图颜色（RGB）和深度（D）图像。具体地，RGB-D图像是基于平面布置图沿着采样位置以分批方式自回归生成的，其中先前生成的图像被用作扩散模型的条件，以在附近位置生成图像。扩散模型中的全局布局和注意力设计确保了生成图像的一致性，可以从中重建3D场景。通过对3D Front数据集的广泛评估，我们证明了HouseCraft可以生成高质量的房屋规模的3D场景。消融研究也验证了不同设计选择的有效性。我们将发布我们的代码和模型权重。项目页面：https://neu-vi.github.io/houseCrafter/ et.al.|[2406.20077](http://arxiv.org/abs/2406.20077)|null|
|**2024-06-28**|**Neural Differentiable Modeling with Diffusion-Based Super-resolution for Two-Dimensional Spatiotemporal Turbulence**|由于其复杂的多尺度性质和令人望而却步的计算需求，高保真度模拟时空湍流仍然是计算流体动力学（CFD）中的一个基石挑战。传统方法通常使用闭包模型，该模型试图以未解决的方式表示小规模特征。然而，这些方法往往会牺牲精度并丢失高频/波数信息，尤其是在涉及复杂流动物理的场景中。在本文中，我们介绍了一种创新的神经可微建模框架，旨在提高时空湍流模拟的可预测性和效率。我们的方法以可微混合建模技术为特色，在可微编程框架内将深度神经网络与数值PDE求解器无缝集成，将深度学习与基于物理的CFD建模协同。具体而言，在较粗糙的网格上构建混合可微神经求解器，以捕捉大规模湍流现象，然后应用贝叶斯条件扩散模型，该模型以大规模流量预测为条件生成小规模湍流。研究了两种创新的混合架构设计，并通过与传统的大涡模拟技术（基于物理的子网格尺度闭包和纯数据驱动的神经求解器）的比较分析来评估其性能。这些发现强调了神经可微建模框架在显著提高湍流模拟的准确性和计算效率方面的潜力。这项研究不仅证明了将深度学习与基于物理的数值求解器相结合的有效性，还为先进的CFD建模技术开创了新的先例，突出了可微规划在科学计算中的变革性影响。 et.al.|[2406.20047](http://arxiv.org/abs/2406.20047)|null|
|**2024-06-28**|**HAITCH: A Framework for Distortion and Motion Correction in Fetal Multi-Shell Diffusion-Weighted MRI**|扩散磁共振成像（dMRI）是探测快速发育的胎儿大脑微观结构的关键。然而，扫描过程中的胎儿运动及其与磁场不均匀性的相互作用会导致伪影和数据在空间和角度域上散射。在信噪比非常低的高角度分辨率胎儿dMRI中，这些伪影的影响更为明显。这些影响导致了有偏差的估计，并损害了dMRI分析的一致性和可靠性。这项工作介绍了HAITCH，这是第一个也是唯一一个公开可用的工具来校正和重建多外壳高角度分辨率胎儿dMRI数据。HAITCH提供了多项技术进步，包括用于动态失真校正的光点反向双回波采集、用于无模型和稳健重建的高级运动校正、用于增强信息捕获和增加运动容忍度的优化多外壳设计，以及用于提高重建保真度的异常值检测。该框架是开源的、灵活的，可用于处理任何类型的胎儿dMRI数据，包括单回声或单壳采集，但当与任何现有工具都无法处理的多壳多回声胎儿dMRI信息一起使用时，该框架最有效。对真实胎儿dMRI扫描的验证实验表明，在不同的胎儿年龄和运动水平下，有显著的改善和准确的校正。HAITCH成功地去除了伪影，并重建了适用于高级扩散建模的高保真胎儿dMRI数据，包括纤维取向分布函数估计。这些进展为在具有挑战性的成像条件下更可靠地分析胎儿大脑微观结构和纤维束成像铺平了道路。 et.al.|[2406.20042](http://arxiv.org/abs/2406.20042)|null|
|**2024-06-28**|**Kinetics of Quantum Reaction-Diffusion systems**|在量子主方程的Keldysh路径积分公式中，我们讨论了在任意空间维度 $d$中受到耗散粒子损失的多体费米子和玻色子系统。这种开放量子动力学代表了经典反应扩散动力学到量子领域的推广。我们首先展示了如何通过边界项在Keldysh路径积分中引入初始条件。然后，我们研究了二元湮灭反应$A+A\\emptyset$，为此我们导出了类似玻尔兹曼的动力学方程。粒子密度随时间的代数衰减取决于粒子统计。为了对冷原子的可能实验实现进行建模，对于$d=1$ 中的费米子，我们进一步讨论了涉及陷阱势存在的非均匀情况。在这种情况下，我们量化了动力学的不可逆性，研究了捕获势不同猝灭时系统熵的时间演化。我们发现，系统熵在约束猝灭下具有代数衰减的特征，而在去约束场景下则饱和。 et.al.|[2406.20028](http://arxiv.org/abs/2406.20028)|null|
|**2024-06-28**|**Information Entropy of the Financial Market: Modelling Random Processes Using Open Quantum Systems**|我们讨论了信息熵在随机过程行为中的作用，以及这可能如何在金融市场价格动态中发挥作用。然后，我们继续展示开放量子系统方法如何在建模随机过程的熵增益方面作为经典方法的更灵活的替代方案。我们首先描述一个可用于模拟金融市场状态的开放量子系统。然后，我们继续展示如何在这个框架中表示本质上经典的扩散。最后，我们展示了如何通过放松某些假设，产生有趣的、本质上非经典的结果，这些结果通过数值模拟得到强调。 et.al.|[2406.20027](http://arxiv.org/abs/2406.20027)|null|
|**2024-06-28**|**Learning glass transition temperatures via dimensionality reduction with data from computer simulations: Polymers as the pilot case**|机器学习（ML）方法为理解大型复杂数据集中的固有模式提供了高级手段。在这里，我们使用主成分分析（PCA）和扩散图（DM）技术来评估聚乳酸（PLA）和聚（3-羟基丁酸酯）（PHB）的全原子分子动力学（MD）模拟的低维表示的玻璃化转变温度（ $T_\mathrm{g}$）。考虑了四种分子描述符：径向分布函数（RDF）、均方位移（MSD）、相对方位移（RSD）和二面角（DA）。通过应用高斯混合模型（GMM）来分析PCA和DM投影，并通过将它们的对数似然量化为基于密度的度量，揭示了对应于熔融态和玻璃态的两个群体的明显分离。这种分离使$T_\mathrm｛g｝$能够从冷却引起的不同温度下对数似然分布之间重叠的急剧增加中进行评估$使用DM从RDF和MSD描述符导出的T_\mathrm｛g｝$值与PLA和PHB模型的基于标准计算机模拟的膨胀度量和动态$T_\mathrm{g｝$值非常匹配。PCA的情况并非如此。DM转换的DA和RSD数据产生的$T_\mathrm{g}$值与实验值一致。总的来说，原子模拟和扩散图与高斯混合模型的融合为计算$T_\mathrm{g}$ 和以统一的方式研究玻璃形成材料的各种分子描述符的玻璃化转变提供了一个很有前途的框架。 et.al.|[2406.20018](http://arxiv.org/abs/2406.20018)|null|
|**2024-06-28**|**On the Trade-off between Flatness and Optimization in Distributed Learning**|本文提出了一个理论框架来评估和比较分布式学习的梯度下降算法的性能，以及它们在非凸环境中围绕局部极小值的行为。先前的工作已经注意到，向平坦局部极小值的收敛往往会增强学习算法的泛化能力。这项工作发现了两个有趣的结果。首先，它表明，在大批量训练机制中，与集中式解决方案相比，分散学习策略能够更快地逃离局部极小值，并有利于收敛到更平坦的极小值。其次，也是重要的一点，最终的分类精度不仅取决于局部极小值的平坦度，还取决于学习算法接近该极小值的程度。换句话说，分类精度是平坦性和优化性能的函数。本文仔细研究了平面度和优化误差这两个指标之间的相互作用。一个重要的结论是，扩散型的分散策略提高了分类精度，因为它在平坦性和优化性能之间取得了更有利的平衡。 et.al.|[2406.20006](http://arxiv.org/abs/2406.20006)|null|
|**2024-06-28**|**The $L_μ-L_τ$ solution to the IceCube UHE neutrino deficit in light of NA64**|在这项工作中，我们分析了MeV尺度$L_\mu-L_\tau$规范玻色子可以解释在冰立方中观测到的扩散超高能（UHE）天体物理中微子光谱的缺陷，以及实验和$e^+e^-$色散数据驱动的μ子异常磁矩SM计算之间的差异的情况。我们绘制了模型的参数空间，在这里，由新的Z’介导的具有宇宙中微子背景的UHE中微子的弹性共振s通道散射可以改善对观测到的级联和轨道光谱的描述，而不是无散射假设。与最近的NA64$\mu$结果相比，我们发现参数空间的某些部分仍未被探索，但在目标NA64$\ mu$上的数据量为$10^｛11｝$ muons时，将完全探测该区域。 et.al.|[2406.19968](http://arxiv.org/abs/2406.19968)|null|
|**2024-06-28**|**RealMAN: A Real-Recorded and Annotated Microphone Array Dataset for Dynamic Speech Enhancement and Localization**|由于缺乏大规模的真实记录数据集，基于深度学习的多通道语音增强和源定位系统的训练在很大程度上依赖于房间脉冲响应和多通道扩散噪声的模拟。然而，当应用于真实世界场景时，模拟数据和真实世界数据之间的声学不匹配可能会降低模型性能。为了将这种模拟与实际差距联系起来，本文提出了一个新的相对大规模的真实记录和注释麦克风阵列语音和噪声（RealMAN）数据集。所提出的数据集在两个方面有价值：1）在真实场景中对语音增强和定位算法进行基准测试；2） 提供大量的真实世界训练数据，以潜在地提高真实世界应用程序的性能。具体地，使用具有高保真度麦克风的32通道阵列进行记录。扬声器用于播放源语音信号。在32个不同的场景中总共记录了83小时的语音信号（静态扬声器为48小时，移动扬声器为35小时），在31个不同场景中记录了144小时的背景噪声。语音和噪声记录场景都覆盖了各种常见的室内、室外、半室外和交通环境，这使得通用语音增强和源定位网络的训练成为可能。为了获得特定任务的注释，通过自动检测扬声器，用全向鱼眼相机对扬声器的方位角进行注释。直接路径信号被设置为用于语音增强的目标干净语音，该目标干净语音是通过用估计的直接路径传播滤波器对源语音信号进行滤波而获得的。 et.al.|[2406.19959](http://arxiv.org/abs/2406.19959)|null|

<p align=right>(<a href=#updated-on-20240703>back to top</a>)</p>

## NeRF

|Publish Date|Title|Abstract|PDF|Code|
|---|---|---|---|---|
|**2024-07-01**|**3D Feature Distillation with Object-Centric Priors**|将自然语言与物理世界联系起来是一个普遍存在的话题，在计算机视觉和机器人领域有着广泛的应用。最近，像CLIP这样的2D视觉语言模型已经被广泛普及，因为它们在2D图像中具有令人印象深刻的开放词汇基础能力。最近的工作旨在通过特征提取将2D CLIP特征提升到3D，但要么学习特定于场景的神经场，因此缺乏泛化能力，要么专注于需要访问多个相机视图的室内房间扫描数据，这在机器人操作场景中是不现实的。此外，相关方法通常在像素级融合特征，并假设所有相机视图的信息量相等。在这项工作中，我们证明了这种方法在基础精度和分割清晰度方面都会导致次优的3D特征。为了缓解这种情况，我们提出了一种多视图特征融合策略，该策略采用以对象为中心的先验来消除基于语义信息的无信息视图，并通过实例分割掩码在对象级别融合特征。为了提取我们以对象为中心的3D特征，我们生成了一个杂乱桌面场景的大规模合成多视图数据集，从3300多个独特的对象实例中生成了15k个场景，并将其公开。我们表明，我们的方法在从单视图RGB-D重建3D CLIP特征的同时，具有改进的接地能力和空间一致性，从而偏离了测试时多个相机视图的假设。最后，我们证明了我们的方法可以推广到新的桌面领域，并在不进行微调的情况下重新用于3D实例分割，并证明了它在语言引导的机器人抓取中的实用性 et.al.|[2406.18742](http://arxiv.org/abs/2406.18742)|null|
|**2024-06-25**|**Masked Generative Extractor for Synergistic Representation and 3D Generation of Point Clouds**|在2D图像生成建模和表示学习领域，掩模生成编码器（MAGE）已经证明了生成建模与表示学习之间的协同潜力。受此启发，我们提出了Point MAGE，将这一概念扩展到点云数据。具体而言，该框架首先利用矢量量化变分自动编码器（VQVAE）来重建3D形状的神经场表示，从而学习点块的离散语义特征。随后，通过将掩蔽模型与可变掩蔽比相结合，我们实现了生成和表示学习的同步训练。此外，我们的框架与现有的点云自监督学习（SSL）模型无缝集成，从而提高了它们的性能。我们广泛评估了Point MAGE的表示学习和生成能力。在形状分类任务中，Point MAGE在ModelNet40数据集上的准确率为94.2%，在ScanObjectNN数据集上达到92.9%（+1.3%）。此外，它在少量镜头学习和零件分割任务中实现了最先进的性能。实验结果还证实，点MAGE可以在无条件和有条件的设置中生成详细和高质量的3D形状。 et.al.|[2406.17342](http://arxiv.org/abs/2406.17342)|null|
|**2024-06-17**|**DistillNeRF: Perceiving 3D Scenes from Single-Glance Images by Distilling Neural Fields and Foundation Model Features**|我们提出了DistilleNeRF，这是一种自监督学习框架，解决了在自动驾驶中从有限的2D观测中理解3D环境的挑战。我们的方法是一个可推广的前馈模型，它从稀疏的单帧多视图相机输入中预测丰富的神经场景表示，并通过可微分渲染进行自监督训练，以重建RGB、深度或特征图像。我们的第一个见解是通过生成密集的深度和虚拟相机目标进行训练，利用每场景优化的神经辐射场（NeRF），从而帮助我们的模型从稀疏的非重叠图像输入中学习3D几何。其次，为了学习语义丰富的3D表示，我们建议从预先训练的2D基础模型（如CLIP或DINOv2）中提取特征，从而实现各种下游任务，而不需要昂贵的3D人工注释。为了利用这两个见解，我们引入了一种新的模型架构，该架构具有两级提升-飞溅-拍摄编码器和参数化稀疏分层体素表示。在NuScenes数据集上的实验结果表明，DistilleNeRF在场景重建、新视图合成和深度估计方面显著优于现有的可比自监督方法；并且它允许竞争性的零样本3D语义占用预测，以及通过提取的基础模型特征来理解开放世界场景。演示和代码将在https://distillnerf.github.io/. et.al.|[2406.12095](http://arxiv.org/abs/2406.12095)|null|
|**2024-06-18**|**Effective Rank Analysis and Regularization for Enhanced 3D Gaussian Splatting**|从多视图图像中进行三维重建是计算机视觉和图形学的基本挑战之一。近年来，三维高斯散射（3DGS）已经成为一种很有前途的技术，能够实时渲染和高质量的三维重建。该方法利用了三维高斯表示和基于瓦片的飞溅技术，绕过了昂贵的神经场查询。尽管3DGS具有潜力，但由于高斯收敛为具有一个主导方差的各向异性高斯，3DGS仍面临挑战，包括针状伪影、次优几何结构和不准确法线。我们建议使用有效秩分析来检查3D高斯基元的形状统计，并识别高斯确实收敛为有效秩为1的针状形状。为了解决这个问题，我们引入了有效秩作为正则化，它约束高斯的结构。我们的新正则化方法增强了法线和几何重建，同时减少了针状伪影。该方法可以作为附加模块集成到其他3DGS变体中，在不影响视觉逼真度的情况下提高其质量。 et.al.|[2406.11672](http://arxiv.org/abs/2406.11672)|null|
|**2024-06-13**|**Well-posedness and regularity of solutions to neural field problems with dendritic processing**|我们研究了最近提出的神经场模型的解决方案，在该模型中，树突被建模为源自体细胞层的垂直纤维的连续体。由于电压通过具有非局部源的电缆方程沿树枝状方向传播，因此该模型具有各向异性扩散算子以及突触耦合的积分项。因此，相应的柯西问题与经典的神经场方程明显不同。我们证明了问题的弱公式允许一个唯一的解，嵌入估计类似于非线性局部反应扩散方程的嵌入估计。我们的分析依赖于无扩散问题的扰动弱解，即标准神经场，迄今为止尚未对其弱问题进行研究。我们找到了有扩散和无扩散问题的严格渐近估计，并证明了这两个模型的解在有限时间间隔上在适当的范数下保持接近。我们提供了微扰结果的数值证据。 et.al.|[2406.09222](http://arxiv.org/abs/2406.09222)|null|
|**2024-06-13**|**Preserving Identity with Variational Score for General-purpose 3D Editing**|我们提出了Piva（用变分分数蒸馏保持同一性），这是一种新的基于优化的方法，用于编辑基于扩散模型的图像和3D模型。具体来说，我们的方法受到了最近提出的2D图像编辑方法——德尔塔去噪分数（DDS）的启发。我们指出了DDS在二维和三维编辑中的局限性，这会导致细节丢失和过饱和。为了解决这一问题，我们提出了一个额外的分数提取术语，以强制执行身份保护。这导致了更稳定的编辑过程，逐步优化NeRF模型以匹配目标提示，同时保留关键的输入特征。我们证明了我们的方法在零样本图像和神经场编辑中的有效性。我们的方法成功地改变了视觉属性，添加了微妙和实质性的结构元素，转换了形状，并在标准的2D和3D编辑基准上取得了有竞争力的结果。此外，我们的方法没有施加任何约束，如掩蔽或预训练，使其与广泛的预训练扩散模型兼容。这允许进行多功能编辑，而不需要神经场到网格的转换，提供更用户友好的体验。 et.al.|[2406.08953](http://arxiv.org/abs/2406.08953)|null|
|**2024-06-12**|**Category-level Neural Field for Reconstruction of Partially Observed Objects in Indoor Environment**|通过各种成功案例，神经隐式表示在三维重建中引起了人们的关注。对于进一步的应用，如场景理解或编辑，一些作品已经显示出在对象组成重建方面的进展。尽管它们在观测区域具有优越的性能，但在重建部分观测到的对象时，它们的性能仍然有限。为了更好地处理这个问题，我们引入了类别级神经场，该神经场在场景中属于同一类别的对象之间学习有意义的公共3D信息。我们的主要想法是根据观察到的形状对对象进行子分类，以便更好地训练类别级模型。然后，我们利用神经场，通过选择基于射线的不确定性选择的代表性对象并与之对齐，来执行配准部分观测对象的挑战性任务。在模拟和真实世界数据集上的实验表明，我们的方法改进了几个类别的未观察零件的重建。 et.al.|[2406.08176](http://arxiv.org/abs/2406.08176)|**[link](https://github.com/Taekbum/category-nerf-reconstruction-official)**|
|**2024-06-12**|**OpenObj: Open-Vocabulary Object-Level Neural Radiance Fields with Fine-Grained Understanding**|近年来，人们对由视觉语言模型（VLM）促进的开放词汇三维场景重建产生了浓厚的兴趣，VLM在开放集检索中展示了非凡的能力。然而，现有的方法面临一些局限性：它们要么专注于学习逐点特征，导致语义理解模糊，要么只处理对象级重建，从而忽略对象内部的复杂细节。为了应对这些挑战，我们引入了OpenObj，这是一种创新的方法，用于构建具有细粒度理解的开放词汇表对象级神经辐射场（NeRF）。从本质上讲，OpenObj建立了一个健壮的框架，用于在对象级别进行高效和严密的场景建模和理解。此外，我们将零件级特征融入神经领域，从而实现物体内部的细致入微的表示。这种方法捕获对象级实例，同时保持细粒度的理解。在多个数据集上的结果表明，OpenObj在零样本语义分割和检索任务中取得了优异的性能。此外，OpenObj支持多尺度的真实世界机器人任务，包括全局移动和局部操纵。 et.al.|[2406.08009](http://arxiv.org/abs/2406.08009)|**[link](https://github.com/BIT-DYN/OpenObj)**|
|**2024-06-11**|**Image Neural Field Diffusion Models**|扩散模型在对复杂数据分布建模方面表现出了令人印象深刻的能力，与GANs相比具有几个关键优势，例如稳定的训练、更好地覆盖训练分布的模式，以及在没有额外训练的情况下解决反问题的能力。然而，大多数扩散模型学习固定分辨率图像的分布。我们建议通过在图像神经场上训练扩散模型来学习连续图像的分布，该模型可以以任何分辨率渲染，并显示出其相对于固定分辨率模型的优势。为了实现这一点，一个关键的挑战是获得一个代表真实感图像神经场的潜在空间。受最近几项技术的启发，我们提出了一种简单有效的方法，但有一些关键的变化，使图像神经场具有真实感。我们的方法可以用于将现有的潜在扩散自动编码器转换为图像神经场自动编码器。我们证明，图像神经场扩散模型可以使用混合分辨率图像数据集进行训练，优于固定分辨率扩散模型和超分辨率模型，并且可以有效地解决不同尺度条件下的逆问题。 et.al.|[2406.07480](http://arxiv.org/abs/2406.07480)|null|
|**2024-06-10**|**Space-Time Continuous PDE Forecasting using Equivariant Neural Fields**|最近，条件神经场（NeF）通过将解学习为条件NeF的潜在空间中的流，已成为偏微分方程的强大建模范式。尽管受益于NeFs的有利特性，如网格不可知性和时空连续动力学建模，但这种方法限制了将PDE的已知约束强加给解决方案的能力，例如对称性或边界条件，有利于建模的灵活性。相反，我们提出了一种基于时空连续NeF的求解框架，该框架通过在潜在空间中保留几何信息，尊重PDE的已知对称性。我们表明，将解建模为感兴趣组 $G$ 上的点云流，可以提高泛化和数据效率。我们验证了我们的框架很容易推广到看不见的空间和时间位置，以及初始条件的几何变换——在其他基于NeF的PDE预测方法失败的地方——并在一些具有挑战性的几何结构中超过基线进行改进。 et.al.|[2406.06660](http://arxiv.org/abs/2406.06660)|null|

<p align=right>(<a href=#updated-on-20240703>back to top</a>)</p>

[contributors-shield]: https://img.shields.io/github/contributors/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[contributors-url]: https://github.com/Vincentqyw/cv-arxiv-daily/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[forks-url]: https://github.com/Vincentqyw/cv-arxiv-daily/network/members
[stars-shield]: https://img.shields.io/github/stars/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[stars-url]: https://github.com/Vincentqyw/cv-arxiv-daily/stargazers
[issues-shield]: https://img.shields.io/github/issues/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[issues-url]: https://github.com/Vincentqyw/cv-arxiv-daily/issues

