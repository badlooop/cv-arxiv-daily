[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]

## Updated on 2024.05.31
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
|**2024-05-30**|**A Pixel Is Worth More Than One 3D Gaussians in Single-View 3D Reconstruction**|从单视图图像中学习3D场景表示是计算机视觉中一个长期存在的基本问题，在预测输入视图中看不到的内容时存在固有的模糊性。Splatter Image方法建立在最近提出的3D高斯Splatting（3DGS）的基础上，通过基于输入图像的U-Net特征图为每个像素学习单个3D高斯，在快速单图像新视图合成方面取得了有希望的进展。然而，表示在输入视图中无法观察到的遮挡组件的表达能力有限。为了解决这个问题，本文提出了一种分层飞溅图像方法，其中一个像素值超过一个三维高斯。具体地，每个像素由父3D高斯和少量子3D高斯表示。父3D高斯像在香草飞溅图像中一样学习。通过轻量级多层感知器（MLP）学习子3D高斯，MLP将父3D高斯的投影图像特征和目标相机视图的嵌入作为输入。父母和孩子的3D高斯都是以阶段性的方式端到端学习的。来自父母高斯人眼睛的输入图像特征和目标相机位置的联合条件有助于学习分配子高斯人“看不见的东西”，恢复父母高斯人经常错过的被遮挡的细节。在实验中，所提出的方法在ShapeNet SRN和CO3D数据集上进行了测试，获得了最先进的性能，特别是显示了在输入视图中重建被遮挡内容的良好能力。 et.al.|[2405.20310](http://arxiv.org/abs/2405.20310)|null|
|**2024-05-29**|**EvaGaussians: Event Stream Assisted Gaussian Splatting from Blurry Images**|三维高斯散射（3D-GS）在三维场景重建和新视图合成方面表现出了非凡的能力。然而，它的训练在很大程度上取决于高质量、清晰的图像和准确的相机姿势。在非理想的现实世界场景中，满足这些要求可能具有挑战性，在这些场景中，运动模糊图像通常会出现在高速移动的相机或需要长曝光时间的弱光环境中。为了应对这些挑战，我们引入了事件流辅助高斯散射（EvaGaussians），这是一种新的方法，它集成了事件相机捕获的事件流，以帮助从模糊图像中重建高质量的3D-GS。利用事件相机提供的高时间分辨率和动态范围，我们利用事件流对运动模糊图像的形成过程进行显式建模，并指导3D-GS的去模糊重建。通过联合优化3D-GS参数和恢复曝光时间内的相机运动轨迹，我们的方法可以有力地促进具有复杂纹理细节的高保真新视图的获取。我们全面评估了我们的方法，并将其与以前最先进的去模糊渲染方法进行了比较。定性和定量比较都表明，我们的方法在从模糊图像中恢复精细细节和生成高保真新颖视图方面优于现有技术。 et.al.|[2405.20224](http://arxiv.org/abs/2405.20224)|null|
|**2024-05-30**|**NeRF View Synthesis: Subjective Quality Assessment and Objective Metrics Evaluation**|神经辐射场（NeRF）是一种开创性的计算机视觉技术，能够从多个视点生成高质量、身临其境的视觉内容。这种能力在虚拟/增强现实、3D建模以及电影和娱乐行业的内容创作等应用中具有显著优势。然而，NeRF方法的评估带来了一些挑战，包括缺乏全面的数据集、可靠的评估方法和客观的质量指标。本文通过进行严格的主观质量评估测试，全面解决了NeRF质量评估的问题，该测试考虑了几个场景类别和最近提出的NeRF视图合成方法。此外，根据主观研究的主观得分来评估各种最先进的传统和基于学习的全参考2D图像和视频质量评估指标的性能。对实验结果进行了深入分析，对不同类别的视觉场景中的几种NeRF方法和客观质量指标进行了比较评估，包括正面和360度相机轨迹的真实和合成内容。 et.al.|[2405.20078](http://arxiv.org/abs/2405.20078)|null|
|**2024-05-30**|**IReNe: Instant Recoloring in Neural Radiance Fields**|NERF的进步已经允许3D场景重建和新颖的视图合成。然而，在保持照片真实性的同时有效地编辑这些表示是一个新出现的挑战。最近的方法面临三个主要限制：交互使用速度慢，对象边界缺乏精度，难以确保多视图的一致性。我们引入IReNe来解决这些限制，从而在NeRF中实现快速、接近实时的颜色编辑。利用预先训练的NeRF模型和带有用户应用的颜色编辑的单个训练图像，IReNe可以在几秒钟内快速调整网络参数。这种调整允许模型生成新的场景视图，准确地表示训练图像的颜色变化，同时控制对象边界和视图特定效果。通过将可训练分割模块集成到模型中来实现对象边界控制。该过程通过仅重新训练最后一个网络层的权重来提高效率。我们观察到，这一层的神经元可以分为负责视觉依赖性外观的神经元和有助于扩散外观的神经元。我们引入了一种自动分类方法来识别这些神经元类型，并专门微调扩散神经元的权重。这进一步加速了训练，并确保在不同视图中进行一致的颜色编辑。在经过编辑的对象颜色的新数据集上进行的彻底验证显示，与竞争对手相比，在数量和质量上都取得了显著进步，速度提高了5倍至500倍。 et.al.|[2405.19876](http://arxiv.org/abs/2405.19876)|null|
|**2024-05-30**|**GaussianPrediction: Dynamic 3D Gaussian Prediction for Motion Extrapolation and Free View Synthesis**|在动态环境中预测未来场景对于智能决策和导航至关重要，这是计算机视觉和机器人领域尚未完全实现的挑战。传统的方法，如视频预测和新颖的视图合成，要么缺乏从任意视点进行预测的能力，要么缺乏预测时间动态的能力。在本文中，我们介绍了GaussianPrediction，这是一种新的框架，它使3D高斯表示能够在动态环境中进行动态场景建模和未来场景合成。GaussianPrediction可以使用动态场景的视频观测，从任何角度预测未来的状态。为此，我们首先提出了一个具有变形建模的3D高斯正则空间，以捕捉动态场景的外观和几何结构，并将生命周期特性集成到高斯中以实现不可逆变形。为了使预测变得可行和高效，提出了一种通过提取关键点的场景运动来提取同心运动的方法。最后，使用图卷积网络来预测关键点的运动，从而能够绘制出未来场景的真实感图像。我们的框架在合成数据集和真实世界数据集上都表现出出色的性能，证明了它在预测和渲染未来环境方面的功效。 et.al.|[2405.19745](http://arxiv.org/abs/2405.19745)|null|
|**2024-05-30**|**GaussianRoom: Improving 3D Gaussian Splatting with SDF Guidance and Monocular Cues for Indoor Scene Reconstruction**|近年来，三维高斯散射（3DGS）以其高质量的渲染和实时速度彻底改变了神经渲染。然而，当涉及到具有大量无纹理区域的室内场景时，由于点云的初始化较差和优化受限，3DGS产生了不完整和有噪声的重建结果。受符号距离场（SDF）连续性的启发，我们提出了一个将神经SDF与3DGS相结合的统一优化框架，符号距离场在曲面建模中自然具有优势。该框架结合了一个可学习的神经SDF字段来指导高斯的加密和修剪，使高斯即使在初始化较差的点云情况下也能准确地对场景进行建模。同时，高斯表示的几何图形通过试点点采样提高了SDF场的效率。此外，我们使用法线和边缘先验对优化进行正则化，以消除无纹理区域中的几何模糊性并改进细节。在ScanNet和ScanNet++中进行的大量实验表明，我们的方法在表面重建和新视图合成方面都达到了最先进的性能。 et.al.|[2405.19671](http://arxiv.org/abs/2405.19671)|null|
|**2024-05-30**|**Uncertainty-guided Optimal Transport in Depth Supervised Sparse-View 3D Gaussian**|3D高斯飞溅在实时新颖视图合成中表现出了令人印象深刻的性能。然而，实现从RGB图像的成功重建通常需要在静态条件下捕获多个输入视图。为了解决稀疏输入视图的挑战，以前的方法已经将深度监督纳入3D高斯的训练中，以减轻过拟合，使用来自预训练的深度网络的密集预测作为伪地面实况。然而，单目深度估计模型的深度预测在特定区域固有地表现出显著的不确定性。仅仅依赖像素L2损失可能会无意中包含来自这些不确定区域的有害噪声。在这项工作中，我们介绍了一种新的方法来监督三维高斯的深度分布，利用深度先验和集成的不确定性估计。为了解决深度预测中的这些局部误差，我们集成了一种逐片优化传输策略，以补充深度监督中的传统L2损失。在LLFF、DTU和Blender数据集上进行的大量实验表明，我们的方法UGOT实现了卓越的新视图合成，并始终优于最先进的方法。 et.al.|[2405.19657](http://arxiv.org/abs/2405.19657)|null|
|**2024-05-29**|**Neural Radiance Fields for Novel View Synthesis in Monocular Gastroscopy**|从预先捕获的单目胃镜图像中合成患者胃内任意新颖的视点图像是胃诊断中一个很有前途的课题。实现这一目标的典型方法集成了传统的三维重建技术，包括运动结构（SfM）和泊松曲面重建。这些方法产生显式的3D表示，例如点云和网格，从而能够从新的视点渲染图像。然而，胃内低纹理和非朗伯区域的存在往往会导致点云和网格重建的噪声和不完整，阻碍了高质量图像渲染的实现。本文将新兴的神经辐射场（NeRF）技术应用于单目胃镜数据，以合成新视点的照片逼真图像。为了解决单眼胃镜检查局部区域中由于视图稀疏而导致的性能下降问题，我们将来自预重建点云的几何先验纳入NeRF的训练中，这为预捕获的观察到的视图和生成的未观察到的图像引入了一种新的基于几何的损失。与最近的其他NeRF方法相比，我们的方法在定性和定量上都展示了从胃内新视角进行的高保真图像渲染。 et.al.|[2405.18863](http://arxiv.org/abs/2405.18863)|null|
|**2024-05-29**|**LP-3DGS: Learning to Prune 3D Gaussian Splatting**|近年来，三维高斯散射（3DGS）以其高质量和快速的渲染速度成为新视图合成（NVS）的主流方法之一。然而，作为一种基于点的场景表示，3DGS可能会生成大量高斯来适应场景，从而导致高内存使用率。已经提出的改进需要经验和预设的修剪比率或重要性得分阈值来修剪点云。这样的超参数需要多轮训练来优化和实现最大修剪率，同时保持每个场景的渲染质量。在这项工作中，我们提出了学习修剪3DGS（LP-3DGS），其中将可训练的二进制掩码应用于重要性得分，可以自动找到最佳修剪率。我们没有使用传统的直通估计器（STE）方法来近似二进制掩模梯度，而是重新设计了掩模函数，以利用Gumbel-Sigmoid方法，使其可微并与现有的3DGS训练过程兼容。大量实验表明，LP-3DGS始终能产生高效且高质量的良好平衡。 et.al.|[2405.18784](http://arxiv.org/abs/2405.18784)|null|
|**2024-05-29**|**Zero-to-Hero: Enhancing Zero-Shot Novel View Synthesis via Attention Map Filtering**|基于单一源图像从任意视图生成逼真图像仍然是计算机视觉中的一个重大挑战，其应用范围从电子商务到沉浸式虚拟体验。扩散模型的最新进展，特别是Zero-1-to-3模型，已被广泛用于生成看似合理的视图、视频和3D模型。然而，这些模型在新视图生成中仍然存在不一致和不可信的问题，尤其是在具有挑战性的观点变化中。在这项工作中，我们提出了Zero-to-Hero，这是一种新的测试时间方法，通过在Zero-1-3的去噪过程中操纵注意力图来增强视图合成。通过将去噪过程与随机梯度下降（SGD）进行类比，我们实现了一种聚合注意力图的过滤机制，增强了生成的可靠性和真实性。这个过程提高了几何一致性，而不需要重新训练或大量的计算资源。此外，我们修改了自注意机制，以整合来自源代码的信息，减少形状失真。这些过程得到了专门的采样计划的进一步支持。实验结果表明，在一组不同的分布对象上验证了保真度和一致性的显著提高。 et.al.|[2405.18677](http://arxiv.org/abs/2405.18677)|null|

<p align=right>(<a href=#updated-on-20240531>back to top</a>)</p>

## 3D Reconstruction

|Publish Date|Title|Abstract|PDF|Code|
|---|---|---|---|---|
|**2024-05-30**|**$\textit{S}^3$Gaussian: Self-Supervised Street Gaussians for Autonomous Driving**|真实感街道场景的三维重建是开发自动驾驶真实世界模拟器的关键技术。尽管神经辐射场（NeRF）对驾驶场景很有效，但3D高斯散射（3DGS）由于其更快的速度和更明确的表示而成为一个有前途的方向。然而，大多数现有的街道3DGS方法需要跟踪的3D车辆边界框来分解静态和动态元素以进行有效的重建，这限制了它们在野外场景中的应用。为了在没有昂贵注释的情况下促进高效的3D场景重建，我们提出了一种自监督街道高斯（$\textit{S}^3$Gaussian）方法来从4D一致性分解动态和静态元素。我们用3D高斯表示每个场景，以保持其明确性，并进一步用时空场网络对其进行紧凑建模。我们在具有挑战性的Waymo Open数据集上进行了广泛的实验，以评估我们方法的有效性。我们的$\textit｛S｝^3$ Gaussian演示了分解静态和动态场景的能力，并在不使用3D注释的情况下实现了最佳性能。代码位于：https://github.com/nnanhuang/S3Gaussian/. et.al.|[2405.20323](http://arxiv.org/abs/2405.20323)|**[link](https://github.com/nnanhuang/s3gaussian)**|
|**2024-05-30**|**A Pixel Is Worth More Than One 3D Gaussians in Single-View 3D Reconstruction**|从单视图图像中学习3D场景表示是计算机视觉中一个长期存在的基本问题，在预测输入视图中看不到的内容时存在固有的模糊性。Splatter Image方法建立在最近提出的3D高斯Splatting（3DGS）的基础上，通过基于输入图像的U-Net特征图为每个像素学习单个3D高斯，在快速单图像新视图合成方面取得了有希望的进展。然而，表示在输入视图中无法观察到的遮挡组件的表达能力有限。为了解决这个问题，本文提出了一种分层飞溅图像方法，其中一个像素值超过一个三维高斯。具体地，每个像素由父3D高斯和少量子3D高斯表示。父3D高斯像在香草飞溅图像中一样学习。通过轻量级多层感知器（MLP）学习子3D高斯，MLP将父3D高斯的投影图像特征和目标相机视图的嵌入作为输入。父母和孩子的3D高斯都是以阶段性的方式端到端学习的。来自父母高斯人眼睛的输入图像特征和目标相机位置的联合条件有助于学习分配子高斯人“看不见的东西”，恢复父母高斯人经常错过的被遮挡的细节。在实验中，所提出的方法在ShapeNet SRN和CO3D数据集上进行了测试，获得了最先进的性能，特别是显示了在输入视图中重建被遮挡内容的良好能力。 et.al.|[2405.20310](http://arxiv.org/abs/2405.20310)|null|
|**2024-05-30**|**TetSphere Splatting: Representing High-Quality Geometry with Lagrangian Volumetric Meshes**|我们介绍了TetSphere splatting，这是一种显式的拉格朗日表示，用于重建具有高质量几何结构的3D形状。传统的对象重建方法主要使用欧拉表示，包括神经隐式（如NeRF、NeuS）和显式表示（如DMET），并且经常难以满足高计算要求和次优网格质量，与此相反，TetSphere splating使用了一种未充分使用但高效的几何基元——四面体网格。这种方法直接产生优越的网格质量，而不依赖于神经网络或后处理。它通过可微分渲染和几何能量优化的组合，使多个初始四面体球体变形，以准确重建3D形状，从而提高计算效率。作为一种强大而通用的几何表示，Tet Sphere splatting无缝集成到各种应用程序中，包括单视图3D重建、图像/文本到3D内容生成。实验结果表明，TetSphere飞溅优于现有的表示，提供了更快的优化速度、增强的网格质量和可靠的薄结构保存。 et.al.|[2405.20283](http://arxiv.org/abs/2405.20283)|null|
|**2024-05-30**|**Object-centric Reconstruction and Tracking of Dynamic Unknown Objects using 3D Gaussian Splatting**|可泛化感知是空间机器人高级自主的支柱之一。在动态环境中估计未知物体的结构和运动是这种自治系统的基础。传统上，解决方案依赖于目标对象的先验知识、多个不同的表示或不适合机器人操作的低保真度输出。这项工作提出了一种新的方法，使用统一的表示——一组描述其几何结构和外观的3D高斯斑点——来逐步重建和跟踪动态未知对象。可微分的三维高斯散射框架适用于动态的以对象为中心的设置。流水线的输入是一组连续的RGB-D图像。使用基于一阶梯度的优化来处理3D重建和6-DoF姿态跟踪任务。该公式简单，不需要预先训练，不假设物体或其运动的先验知识，适合在线应用。在10个不同几何形状和纹理的未知航天器在任意相对运动下的数据集上验证了所提出的方法。实验证明了在短到中等持续时间内，在邻近操作中成功地进行了目标物体的3D重建和精确的6-DoF跟踪。讨论了跟踪漂移的原因，并概述了可能的解决方案。 et.al.|[2405.20104](http://arxiv.org/abs/2405.20104)|null|
|**2024-05-29**|**Learning Mixture-of-Experts for General-Purpose Black-Box Discrete Optimization**|实际应用涉及各种离散优化问题。为这些问题中的每一个设计专门的优化器都是具有挑战性的，通常需要大量的领域知识和人力。因此，开发通用优化器作为解决一系列问题的现成工具一直是一个长期的研究目标。本文介绍了MEGO，这是一种通过完全数据驱动的学习优化（L2O）方法训练的新型通用神经优化器。MEGO由根据解决训练问题的经验训练的专家组成，可以被视为具有二元决策变量的优化问题的基础模型。当遇到需要解决的问题时，MEGO会主动选择相关的专家模型来生成高质量的解决方案。MEGO可以用作独立的高效样本优化器，也可以与现有的搜索方法一起用作初始解决方案生成器。在六个问题类中验证了MEGO的通用性，包括三个经典问题类和三个由编译器、网络分析和三维重建中的真实应用程序产生的问题类。仅在经典问题类上进行过培训，MEGO在所有六个问题类上都表现出色，在解决方案质量和效率方面显著超过了广泛使用的通用优化器。在某些情况下，MEGO甚至超越了最先进的专业优化器。此外，MEGO提供了问题之间的相似性度量，为问题分类提供了一个新的视角。在通过L2O追求通用优化器的过程中，MEGO代表了向前迈出的第一步，但意义重大。 et.al.|[2405.18884](http://arxiv.org/abs/2405.18884)|null|
|**2024-05-29**|**Neural Radiance Fields for Novel View Synthesis in Monocular Gastroscopy**|从预先捕获的单目胃镜图像中合成患者胃内任意新颖的视点图像是胃诊断中一个很有前途的课题。实现这一目标的典型方法集成了传统的三维重建技术，包括运动结构（SfM）和泊松曲面重建。这些方法产生显式的3D表示，例如点云和网格，从而能够从新的视点渲染图像。然而，胃内低纹理和非朗伯区域的存在往往会导致点云和网格重建的噪声和不完整，阻碍了高质量图像渲染的实现。本文将新兴的神经辐射场（NeRF）技术应用于单目胃镜数据，以合成新视点的照片逼真图像。为了解决单眼胃镜检查局部区域中由于视图稀疏而导致的性能下降问题，我们将来自预重建点云的几何先验纳入NeRF的训练中，这为预捕获的观察到的视图和生成的未观察到的图像引入了一种新的基于几何的损失。与最近的其他NeRF方法相比，我们的方法在定性和定量上都展示了从胃内新视角进行的高保真图像渲染。 et.al.|[2405.18863](http://arxiv.org/abs/2405.18863)|null|
|**2024-05-28**|**FreeSplat: Generalizable 3D Gaussian Splatting Towards Free-View Synthesis of Indoor Scenes**|赋予3D高斯飞溅以泛化能力是很有吸引力的。然而，现有的可推广的3D高斯散点方法由于其主干较重，在很大程度上局限于立体图像之间的窄范围插值，因此缺乏准确定位3D高斯并支持宽视野范围内的自由视野合成的能力。在本文中，我们提出了一种新的框架FreeSplat，它能够从长序列输入到自由视图合成重建几何一致的3D场景。具体而言，我们首先介绍了低成本跨视图聚合，该聚合通过在附近视图之间构建自适应成本体积并使用多尺度结构聚合特征来实现。随后，我们提出了逐像素三元组融合，以消除重叠视图区域中3D高斯的冗余，并聚合在多个视图中观察到的特征。此外，我们提出了一种简单但有效的自由视图训练策略，无论视图的数量如何，都能确保在更广泛的视图范围内进行稳健的视图合成。我们的经验结果表明，在不同数量的输入视图中，新视图渲染的颜色图质量和深度图精度都具有最先进的新视图合成性能。我们还表明，FreeSplat可以更有效地执行推理，并可以有效地减少冗余高斯，为无深度先验的前馈大场景重建提供了可能性。 et.al.|[2405.17958](http://arxiv.org/abs/2405.17958)|**[link](https://github.com/wangys16/freesplat)**|
|**2024-05-28**|**A Refined 3D Gaussian Representation for High-Quality Dynamic Scene Reconstruction**|近年来，神经辐射场（NeRF）以其隐式表示方式彻底改变了三维重建。基于NeRF，3D高斯飞溅（3D-GS）已经脱离了神经网络的隐式表示，而是直接将场景表示为具有高斯形状分布的点云。虽然这种转变显著提高了辐射场的渲染质量和速度，但不可避免地导致了内存使用量的显著增加。此外，在3D-GS中有效地渲染动态场景已经成为一个紧迫的挑战。为了解决这些问题，本文提出了一种用于高质量动态场景重建的精细3D高斯表示。首先，我们使用可变形多层感知器（MLP）网络来捕捉高斯点的动态偏移，并通过哈希编码和微小的MLP来表达点的颜色特征，以减少存储需求。随后，我们引入了一种可学习的去噪掩模，结合去噪损失来消除场景中的噪声点，从而进一步压缩3D高斯模型。最后，通过静态约束和运动一致性约束来减轻点的运动噪声。实验结果表明，我们的方法在渲染质量和速度方面优于现有方法，同时显著减少了与3D-GS相关的内存使用，使其非常适合于各种任务，如新颖的视图合成和动态映射。 et.al.|[2405.17891](http://arxiv.org/abs/2405.17891)|null|
|**2024-05-29**|**Memorize What Matters: Emergent Scene Decomposition from Multitraverse**|人类自然会保留对永恒元素的记忆，而短暂的时刻往往会从记忆的缝隙中溜走。这种选择性保留对于机器人感知、定位和绘图至关重要。为了赋予机器人这种能力，我们引入了3D高斯映射（3DGM），这是一种基于3D高斯飞溅的自监督、仅限相机的离线映射框架。3DGM将来自同一区域的多遍历RGB视频转换为基于高斯的环境图，同时执行2D短暂对象分割。我们的主要观察结果是，环境在遍历中保持一致，而对象经常发生变化。这使我们能够利用重复遍历的自我监督来实现环境对象分解。更具体地说，3DGM将多遍历环境映射公式化为一个鲁棒的可微渲染问题，将环境和对象的像素分别视为内值和外值。3DGM使用稳健特征提取、特征残差挖掘和稳健优化，在没有人工干预的情况下联合执行2D分割和3D映射。我们建立了Mapverse基准，来源于伊萨卡365和nuPlan数据集，以评估我们在无监督二维分割、三维重建和神经渲染中的方法。大量结果验证了我们的方法在自动驾驶和机器人方面的有效性和潜力。 et.al.|[2405.17187](http://arxiv.org/abs/2405.17187)|**[link](https://github.com/nvlabs/3dgm)**|
|**2024-05-27**|**SDL-MVS: View Space and Depth Deformable Learning Paradigm for Multi-View Stereo Reconstruction in Remote Sensing**|基于遥感图像的多视角立体研究促进了大规模城市三维重建的发展。然而，遥感多视点图像数据在获取过程中存在遮挡和视点之间亮度不均匀的问题，这导致了深度估计中细节模糊的问题。为了解决上述问题，我们重新审视了多视图立体任务中的可变形学习方法，并提出了一种基于视图空间和深度可变形学习（SDL-MVS）的新范式，旨在学习不同视图空间中特征的可变形交互，并对深度范围和区间进行可变形建模，以实现高精度的深度估计。具体来说，为了解决遮挡和亮度不均匀导致的视图噪声问题，我们提出了一种渐进空间可变形采样（PSS）机制，该机制以渐进的方式对3D截头体空间和2D图像空间中的采样点进行可变形学习，以自适应地将源特征嵌入到参考特征中。为了进一步优化深度，我们引入了深度假设可变形离散化（DHD），它通过自适应调整深度范围假设和对深度区间假设进行可变形离散来实现深度先验的精确定位。最后，我们的SDL-MVS通过视图空间和深度的可变形学习范式，实现了多视图立体中遮挡和亮度不均的显式建模，实现了精确的多视图深度估计。在珞珈MVS和WHU数据集上进行的大量实验表明，我们的SDL-MVS达到了最先进的性能。值得注意的是，在三个视图作为输入的前提下，我们的SDL-MVS在珞珈MVS数据集上实现了0.086的MAE误差，<0.6米的准确率为98.9%，<3区间的准确度为98.9%。 et.al.|[2405.17140](http://arxiv.org/abs/2405.17140)|null|

<p align=right>(<a href=#updated-on-20240531>back to top</a>)</p>

## Diffusion

|Publish Date|Title|Abstract|PDF|Code|
|---|---|---|---|---|
|**2024-05-30**|**Unique3D: High-Quality and Efficient 3D Mesh Generation from a Single Image**|在这项工作中，我们介绍了Unique3D，这是一种新颖的图像到3D框架，用于从单视图图像高效生成高质量的3D网格，具有最先进的生成保真度和强大的可推广性。以前基于分数蒸馏采样（SDS）的方法可以通过从大型二维扩散模型中提取三维知识来产生多样化的三维结果，但它们通常每种情况的优化时间很长，存在不一致的问题。最近的工作解决了这个问题，并通过微调多视图扩散模型或训练快速前馈模型来生成更好的3D结果。然而，由于不一致性和生成的分辨率有限，它们仍然缺乏复杂的纹理和复杂的几何形状。为了在单图像到三维图像中同时实现高保真度、一致性和效率，我们提出了一种新的框架Unique3D，该框架包括一个多视图扩散模型和相应的法线扩散模型，以生成具有法线图的多视图图像，一个多级升级过程，以逐步提高生成的正交多视图的分辨率，以及一种称为ISOMER的即时一致网格重建算法，该算法将颜色和几何先验完全集成到网格结果中。大量实验表明，我们的Unique3D在几何和纹理细节方面显著优于其他图像到3D基线。 et.al.|[2405.20343](http://arxiv.org/abs/2405.20343)|null|
|**2024-05-30**|**OccSora: 4D Occupancy Generation Models as World Simulators for Autonomous Driving**|了解3D场景的演变对于有效的自动驾驶非常重要。传统的方法通过单个实例的运动来模拟场景开发，而世界模型则成为描述一般场景动力学的生成框架。然而，大多数现有的方法都采用自回归框架来执行下一个令牌预测，这在建模长期时间演变方面效率低下。为了解决这一问题，我们提出了一个基于扩散的4D占用生成模型OccSora，以模拟自动驾驶3D世界的发展。我们使用4D场景标记器来获得4D占用输入的紧凑离散时空表示，并实现长序列占用视频的高质量重建。然后，我们学习时空表示上的扩散变换器，并生成以轨迹提示为条件的4D占用。我们在广泛使用的具有Occ3D占用注释的nuScenes数据集上进行了广泛的实验。OccSora可以生成具有真实3D布局和时间一致性的16s视频，展示了其理解驾驶场景的空间和时间分布的能力。凭借轨迹感知4D生成，OccSora有潜力成为自动驾驶决策的世界模拟器。代码位于：https://github.com/wzzheng/OccSora. et.al.|[2405.20337](http://arxiv.org/abs/2405.20337)|**[link](https://github.com/wzzheng/occsora)**|
|**2024-05-30**|**VividDream: Generating 3D Scene with Ambient Dynamics**|我们介绍了VividDream，这是一种从单个输入图像或文本提示生成具有环境动力学的可探索4D场景的方法。VividDream首先通过迭代修复和几何合并将输入图像扩展为静态3D点云。然后使用具有质量细化技术的视频扩散模型生成动画视频的集合，并以来自采样的相机轨迹的静态3D场景的渲染为条件。然后，我们使用动画视频集成优化规范的4D场景表示，并使用每视频运动嵌入和可见性遮罩来减轻不一致性。所得到的4D场景使得能够以合理的环境场景动力学对3D场景进行自由视图探索。实验表明，VividDream可以为人类观众提供基于各种真实图像和文本提示生成的引人注目的4D体验。 et.al.|[2405.20334](http://arxiv.org/abs/2405.20334)|null|
|**2024-05-30**|**MotionFollower: Editing Video Motion via Lightweight Score-Guided Diffusion**|尽管基于扩散的视频编辑模型在改变视频属性方面取得了令人印象深刻的进步，但在保留原始主角的外观和背景的同时修改运动信息的探索有限。在本文中，我们提出了MotionFollower，一种用于视频运动编辑的轻量级分数引导扩散模型。为了将条件控制引入去噪过程，MotionFollower利用了我们提出的两个轻量级信号控制器，一个用于姿态，另一个用于外观，这两个控制器都由卷积块组成，而不涉及大量注意力计算。此外，我们设计了一种基于两个分支架构的分数引导原则，包括重建和编辑分支，显著增强了纹理细节和复杂背景的建模能力。具体来说，我们在分数估计过程中强制使用几个一致性正则化子和损失。由此产生的梯度为中间潜伏期注入了适当的指导，迫使模型在不干扰运动修改的情况下保留原始背景细节和主角的外观。实验从定性和定量两个方面展示了MotionFollower的竞技运动编辑能力。与最先进的运动编辑模型MotionEditor相比，MotionFollower可将GPU内存减少约80%，同时提供卓越的运动编辑性能，并专门支持大型相机的运动和动作。 et.al.|[2405.20325](http://arxiv.org/abs/2405.20325)|null|
|**2024-05-30**|**Don't drop your samples! Coherence-aware training benefits Conditional diffusion**|条件扩散模型是强大的生成模型，可以利用各种类型的条件信息，如类标签、分段掩码或文本标题。然而，在许多真实世界的场景中，由于人为注释错误或弱对齐，条件信息可能是有噪声的或不可靠的。在本文中，我们提出了相干感知扩散（CAD），这是一种将条件信息中的相干集成到扩散模型中的新方法，允许它们在不丢弃数据的情况下从有噪声的注释中学习。我们假设每个数据点都有一个相关的连贯性分数，该分数反映了条件信息的质量。然后，我们根据条件信息和连贯性得分来调节扩散模型。通过这种方式，当一致性较低时，模型学会忽略或忽略条件反射。我们表明，CAD在各种条件生成任务上理论上是健全的，并且在经验上是有效的。此外，我们还表明，利用一致性可以生成真实多样的样本，这些样本比在干净的数据集上训练的模型更尊重条件信息，而在这些数据集上，具有低一致性的样本被丢弃了。 et.al.|[2405.20324](http://arxiv.org/abs/2405.20324)|null|
|**2024-05-30**|**Improving the Training of Rectified Flows**|扩散模型在图像和视频生成方面显示出了巨大的前景，但从最先进的模型中采样需要昂贵的生成ODE的数值集成。解决这个问题的一种方法是整流流，它迭代地学习平滑的ODE路径，这些路径不太容易受到截断误差的影响。然而，整流流仍然需要相对大量的功能评估（NFE）。在这项工作中，我们提出了改进的训练整流流的技术，使其即使在低NFE环境中也能与知识提取方法竞争。我们的主要见解是，在现实环境下，用于训练整流流的回流算法的一次迭代就足以学习几乎笔直的轨迹；因此，当前使用多次回流迭代的做法是不必要的。因此，我们提出了改进整流流的一轮训练的技术，包括U形时间步长分布和LPIPS Huber预度量。利用这些技术，我们在CIFAR-10上的1 NFE设置中，将先前2整流流的FID提高了高达72%。在ImageNet 64 $\times$ 64上，我们改进的整流流在一步和两步设置中都优于最先进的蒸馏方法，如稠度蒸馏和渐进蒸馏，并与FID中改进的稠度训练（iCT）的性能相媲美。代码位于https://github.com/sangyun884/rfpp. et.al.|[2405.20320](http://arxiv.org/abs/2405.20320)|**[link](https://github.com/sangyun884/rfpp)**|
|**2024-05-30**|**DITTO-2: Distilled Diffusion Inference-Time T-Optimization for Music Generation**|可控的音乐生成方法对于以人为中心的基于人工智能的音乐创作至关重要，但目前受到速度、质量和控制设计权衡的限制。特别是，扩散推理时间T优化（DITTO）提供了最先进的结果，但比实时速度慢了10倍以上，限制了实际使用。我们提出了提取扩散推理时间T-优化（DITTO-2），这是一种新的方法，可以加快基于推理时间优化的控制，并比实时生成更快地解锁，用于音乐修复、画外画、强度、旋律和音乐结构控制等广泛的应用。我们的方法通过（1）通过高效、改进的一致性或一致性轨迹蒸馏过程提取预训练的扩散模型以进行快速采样（2）使用我们的蒸馏模型进行推理时间优化，将一步采样作为有效的替代优化任务，以及（3）使用我们估计的噪声潜伏时间运行最终的多步采样生成（解码），以实现最佳质量、快速、可控的生成。通过彻底的评估，我们发现我们的方法不仅加快了10倍以上的生成速度，而且同时提高了控制依从性和生成质量。此外，我们将我们的方法应用于最大化文本依从性（CLAP分数）的新应用，并表明我们可以将没有文本输入的无条件扩散模型转换为产生最先进文本控制的模型。可以在上找到合理的示例https://ditto-music.github.io/ditto2/. et.al.|[2405.20289](http://arxiv.org/abs/2405.20289)|null|
|**2024-05-30**|**SemFlow: Binding Semantic Segmentation and Image Synthesis via Rectified Flow**|语义分割和语义图像合成是视觉感知和生成中两个具有代表性的任务。虽然现有的方法将它们视为两个不同的任务，但我们提出了一个统一的基于扩散的框架（SemFlow），并将它们建模为一对反向问题。具体来说，在整流流理论的激励下，我们训练了一个常微分方程（ODE）模型来在真实图像和语义掩码的分布之间进行传输。由于训练对象是对称的，属于图像和语义掩码这两种分布的样本可以毫不费力地可逆地传输。对于语义分割，我们的方法解决了扩散输出的随机性和分割结果的唯一性之间的矛盾。对于图像合成，我们提出了一种有限扰动方法，在不改变语义类别的情况下增强生成结果的多样性。实验表明，我们的SemFlow在语义分割和语义图像合成任务上取得了有竞争力的结果。我们希望这个简单的框架能激励人们重新思考低层次和高层次愿景的统一。项目页面：https://github.com/wang-chaoyang/SemFlow. et.al.|[2405.20282](http://arxiv.org/abs/2405.20282)|**[link](https://github.com/wang-chaoyang/semflow)**|
|**2024-05-30**|**CV-VAE: A Compatible Video VAE for Latent Generative Video Models**|利用变分自动编码器（VAE）等网络对视频进行时空压缩，在OpenAI的SORA和许多其他视频生成模型中发挥着至关重要的作用。例如，许多类似LLM的视频模型学习从VQVAE框架内的3D VAE导出的离散令牌的分布，而大多数基于扩散的视频模型在没有量化的情况下捕获由2D VAE提取的连续潜在令牌的分布。时间压缩简单地通过均匀的帧采样来实现，这导致连续帧之间的不平滑运动。目前，研究界缺乏用于基于潜在扩散的视频模型的常用连续视频（3D）VAE。此外，由于当前基于扩散的方法通常使用预先训练的文本到图像（T2I）模型来实现，因此在不考虑与现有T2I模型的兼容性的情况下直接训练视频VAE将导致它们之间的潜在空间间隙，这将花费巨大的计算资源来进行训练以弥合间隙，即使将T2I模型作为初始化。为了解决这个问题，我们提出了一种用于训练潜在视频模型的视频VAE的方法，即CV-VAE，其潜在空间与给定图像VAE的潜在空间兼容，例如，稳定扩散（SD）的图像VAE。兼容性是通过所提出的新的潜在空间正则化来实现的，该正则化包括使用图像VAE来公式化正则化损失。得益于潜在空间兼容性，视频模型可以在真正时空压缩的潜在空间中从预先训练的T2I或视频模型无缝地训练，而不是简单地以相等的间隔对视频帧进行采样。使用我们的CV-VAE，现有的视频模型可以在最小的微调下生成四倍多的帧。进行了大量的实验来证明所提出的视频VAE的有效性。 et.al.|[2405.20279](http://arxiv.org/abs/2405.20279)|**[link](https://github.com/ailab-cvc/cv-vae)**|
|**2024-05-30**|**KerasCV and KerasNLP: Vision and Language Power-Ups**|我们展示了Keras域包KerasCV和KerasNLP，它们是Keras API的扩展，用于计算机视觉和自然语言处理工作流，能够在JAX、TensorFlow或PyTorch上运行。这些领域包旨在实现快速实验，重点关注易用性和性能。我们采用模块化分层设计：在库的最低抽象级别，我们提供用于创建模型和数据预处理管道的构建块，在库的最高抽象级别，为Stable Diffusion、YOLOv8、GPT2、BERT、Mistral、CLIP、Gemma、T5等流行架构提供预训练的“任务”模型。任务模型具有内置的预处理、预训练的权重，可以对原始输入进行微调。为了实现高效训练，我们支持所有模型的XLA编译，并通过使用tf.data API编译的TensorFlow操作图运行所有预处理。这些库是完全开源的（Apache 2.0许可证）。可在GitHub上获得。 et.al.|[2405.20247](http://arxiv.org/abs/2405.20247)|null|

<p align=right>(<a href=#updated-on-20240531>back to top</a>)</p>

## NeRF

|Publish Date|Title|Abstract|PDF|Code|
|---|---|---|---|---|
|**2024-05-30**|**Gated Fields: Learning Scene Reconstruction from Gated Videos**|根据时间观测重建户外3D场景是一项挑战，最近在神经领域的工作为其提供了一条新的途径。然而，仅从RGB捕获恢复场景属性（如几何体、外观或辐射）的现有方法在处理光线不足或纹理不足的区域时往往会失败。同样，使用扫描激光雷达传感器恢复场景也很困难，因为它们的角采样率较低，这使得恢复广阔的真实世界场景变得困难。为了解决这些差距，我们介绍了门控场——一种利用主动门控视频序列的神经场景重建方法。为此，我们提出了一种无缝结合时间门控捕获和照明的神经渲染方法。我们的方法利用了门控视频中的内在深度线索，无论环境照明条件如何，都能实现精确而密集的几何重建。我们在昼夜场景中验证了该方法，并发现门控场与RGB和激光雷达重建方法相比是有利的。我们的代码和数据集可在https://light.princeton.edu/gatedfields/. et.al.|[2405.19819](http://arxiv.org/abs/2405.19819)|null|
|**2024-05-27**|**Extreme Compression of Adaptive Neural Images**|隐式神经表示（INRs）和神经场是一种新的信号表示范式，从图像和音频到3D场景和视频。其基本思想是将信号表示为连续且可微分的神经网络。这一思想提供了前所未有的优势，如连续分辨率和存储效率，从而实现了新的压缩技术。然而，将数据表示为神经网络带来了新的挑战。例如，给定一个2D图像作为神经网络，我们如何进一步压缩这样的神经图像？。在这项工作中，我们提出了一种新的压缩神经场的分析，重点是图像。我们还介绍了自适应神经图像（ANI），这是一种有效的神经表示，能够适应不同的推理或传输要求。我们提出的方法可以将神经图像的每像素比特数（bpp）减少4倍，而不会丢失敏感细节或损害保真度。我们之所以能做到这一点，是因为我们成功地实现了4位神经表示。我们的工作为开发压缩神经场提供了一个新的框架。 et.al.|[2405.16807](http://arxiv.org/abs/2405.16807)|null|
|**2024-05-24**|**Blaze3DM: Marry Triplane Representation with Diffusion for 3D Medical Inverse Problem Solving**|解决图像恢复和重建等三维医学逆问题在现代医学领域至关重要。然而，3D医疗数据中的维度诅咒导致主流的体积方法遭受高资源消耗，并挑战模型成功捕捉自然分布，导致不可避免的体积不一致和伪影。最近的一些工作试图简化潜在空间中的生成，但缺乏对复杂图像细节进行有效建模的能力。为了解决这些局限性，我们提出了Blaze3DM，这是一种新的方法，通过集成紧凑的三平面神经场和强大的扩散模型，实现了快速高保真的生成。在技术上，Blaze3DM首先同时优化数据相关的三平面嵌入和共享解码器，将每个三平面重建回相应的3D体积。为了进一步增强3D一致性，我们引入了一个轻量级的3D感知模块来对三个垂直平面的相关性进行建模。然后，在潜在的三平面嵌入上训练扩散模型，并实现无条件和有条件的三平面生成，最终解码为任意大小的体积。对零样本三维医学逆问题求解的大量实验，包括稀疏视图CT、有限角度CT、压缩传感MRI和MRI各向同性超分辨率，表明Blaze3DM不仅实现了最先进的性能，而且显著提高了现有方法的计算效率（比以前的工作快22~40倍）。 et.al.|[2405.15241](http://arxiv.org/abs/2405.15241)|null|
|**2024-05-17**|**SNF-ROM: Projection-based nonlinear reduced order modeling with smooth neural fields**|降阶建模通过从数据中学习低阶空间表示并使用控制方程的流形投影动态演化这些表示，降低了求解偏微分方程的计算成本。虽然通常使用线性子空间降阶模型（ROM），但对于Kolmogorov $n$ -宽度缓慢衰减的问题，例如高雷诺数下以平流为主的流体流动，通常是次优的。人们对非线性ROM越来越感兴趣，它使用最先进的表示学习技术以较少的自由度准确地捕捉这种现象。我们提出了光滑神经场ROM（SNF-ROM），这是一种将无网格简化表示与Galerkin投影相结合的非线性简化建模框架。SNF-ROM体系结构将学习到的ROM轨迹约束为平滑变化的路径，这在根据支配PDE遍历简化流形时的动力学评估中是有益的。此外，我们设计了鲁棒正则化方案，以确保学习的神经场是光滑和可微的。这使我们能够使用自动微分来非侵入地计算简化系统的基于物理的动力学，并使用经典时间积分器来演化简化系统。SNF-ROM可以实现快速的离线训练，并提高在线动力学评估的准确性和稳定性。我们证明了SNF-ROM在一系列平流主导的线性和非线性PDE问题上的有效性，在这些问题上，我们始终优于最先进的ROM。 et.al.|[2405.14890](http://arxiv.org/abs/2405.14890)|null|
|**2024-05-23**|**NeuroGauss4D-PCI: 4D Neural Fields and Gaussian Deformation Fields for Point Cloud Interpolation**|点云插值面临着点稀疏性、复杂的时空动力学以及从稀疏的时间信息中导出完整的三维点云的困难等挑战。本文介绍了NeuroGauss4D PCI，它擅长在各种动态场景中建模复杂的非刚性变形。该方法从迭代高斯云软聚类模块开始，提供结构化的时间点云表示。所提出的时间径向基函数高斯残差利用高斯参数随时间插值，实现平滑的参数转换并捕获高斯分布的时间残差。此外，4D高斯变形场跟踪这些参数的演变，创建连续的时空变形场。4D神经场将低维时空坐标（ $x，y，z，t$ ）转换为高维潜在空间。最后，我们自适应有效地融合了来自神经场的潜在特征和来自高斯变形场的几何特征。NeuroGauss4D PCI在点云帧插值方面优于现有方法，在对象级（DHB）和大规模自动驾驶数据集（NL Drive）上都提供了领先的性能，并可扩展到自动标记和点云加密任务。源代码发布于https://github.com/jiangchaokang/NeuroGauss4D-PCI. et.al.|[2405.14241](http://arxiv.org/abs/2405.14241)|null|
|**2024-05-23**|**Multi-view Remote Sensing Image Segmentation With SAM priors**|遥感中的多视图分割（RS）寻求从场景内的不同视角对图像进行分割。最近的方法利用了从隐式神经场（INF）中提取的3D信息，增强了多个视图的结果一致性，同时使用有限的标签（甚至在3-5个标签内）来简化劳动力。尽管如此，由于不充分的全场景监督和INF中不充分的语义特征，在有限视图标签的约束下实现卓越性能仍然具有挑战性。我们建议将视觉基础模型Segment Anything（SAM）的先验注入INF，以在有限的训练数据下获得更好的结果。具体而言，我们对比测试视图和训练视图之间的SAM特征，以导出每个测试视图的伪标签，增强场景范围的标签信息。随后，我们通过转换器将SAM特征引入场景的INF中，补充语义信息。实验结果表明，我们的方法优于主流方法，证实了SAM作为INF的补充对该任务的有效性。 et.al.|[2405.14171](http://arxiv.org/abs/2405.14171)|null|
|**2024-05-22**|**Bridging Operator Learning and Conditioned Neural Fields: A Unifying Perspective**|算子学习是机器学习的一个新兴领域，旨在学习无穷维函数空间之间的映射。在这里，我们从计算机视觉中揭示了算子学习架构和条件神经场之间的联系，为研究流行的算子学习模型之间的差异提供了一个统一的视角。我们发现，许多常用的算子学习模型可以被视为神经场，其条件机制仅限于点和/或全局信息。受此启发，我们提出了连续视觉转换器（CViT），这是一种新的神经算子架构，它使用视觉转换器编码器，并使用交叉注意力来调制由可训练的基于网格的查询坐标位置编码构建的基场。尽管它很简单，但CViT在气候建模和流体动力学的挑战性基准中取得了最先进的结果。我们的贡献可以被视为在物理科学中适应先进的计算机视觉架构以构建更灵活、更准确的机器学习模型的第一步。 et.al.|[2405.13998](http://arxiv.org/abs/2405.13998)|**[link](https://github.com/predictiveintelligencelab/cvit)**|
|**2024-05-21**|**Unsupervised Searches for Cosmological Parity Violation: Improving Detection Power with the Neural Field Scattering Transform**|最近使用四点相关性的研究表明，星系分布中存在宇称破坏，尽管这些探测的重要性对用于模拟星系分布噪声特性的模拟的选择很敏感。在最近的一篇论文中，我们介绍了一种无监督学习方法，该方法提供了一种替代方法，通过直接从观测数据中学习奇偶性违反，避免了对模拟目录的依赖。然而，我们以前的无监督方法所使用的卷积神经网络（CNN）模型很难扩展到数据有限的更现实的场景。我们提出了一种新的方法，即神经场散射变换（NFST），它通过添加可训练滤波器来增强小波散射变换（WST）技术，该滤波器被参数化为神经场。我们首先调整NFST模型，以在简化的数据集中检测奇偶校验违规，然后在不同的训练集大小下，将其性能与WST和CNN基准进行比较。我们发现，NFST可以检测奇偶校验违规，数据比CNN少4倍，比WST少32倍。此外，在数据有限的情况下，NFST可以检测到高达 $6\sigma$ 置信度的奇偶校验违规，其中WST和CNN无法进行任何检测。我们发现，与基准模型相比，NFST增加的灵活性，特别是学习不对称滤波器的能力，以及NFST架构中内置的特定对称性，有助于提高其性能。我们进一步证明了NFST是易于解释的，这对于物理应用（如奇偶校验违反的检测）是有价值的。 et.al.|[2405.13083](http://arxiv.org/abs/2405.13083)|null|
|**2024-05-21**|**Implicit-ARAP: Efficient Handle-Guided Deformation of High-Resolution Meshes and Neural Fields via Local Patch Meshing**|在这项工作中，我们提出了神经符号距离场的局部补丁网格表示。该技术允许通过仅使用SDF信息及其梯度将平面面片网格投影和变形到标高集曲面上来离散输入SDF的标高集的局部区域。我们的分析表明，这种方法比标准的行进立方体算法更准确地逼近隐式曲面。然后，我们将这种表示应用于手柄引导变形的设置：我们引入了两个不同的管道，它们利用3D神经场来计算在给定约束集下高分辨率网格和神经场的“尽可能刚性”变形。我们对我们的方法和神经场和网格变形的各种基线进行了全面评估，结果表明，这两条管道在结果质量和稳健性方面都取得了令人印象深刻的效率和显著的改进。通过我们的新型流水线，我们引入了一种可扩展的方法来解决高分辨率网格上公认的几何处理问题，并为通过局部面片网格将其他几何任务扩展到隐式曲面领域铺平了道路。 et.al.|[2405.12895](http://arxiv.org/abs/2405.12895)|null|
|**2024-05-16**|**Single-shot volumetric fluorescence imaging with neural fields**|与需要在多个轴向平面上扫描的传统成像方法相比，单次体积荧光（SVF）成像提供了显著的优势，因为它可以在大视场上以高时间分辨率捕获生物过程。现有的SVF成像方法通常需要大的、复杂的点扩展函数（PSF）来满足压缩传感的多路复用要求，这限制了信噪比、分辨率和/或视场。在本文中，我们介绍了QuadraPol-PSF与神经场相结合，这是一种新的SVF成像方法。该方法在后焦平面利用成本效益高的定制偏振器和偏振相机来检测荧光，在紧凑的PSF内有效地编码3D场景，而没有深度模糊。此外，我们提出了一种基于神经场技术的重建算法，该算法解决了用于校正成像系统像差的相位检索方法的不精确性。该算法将实验PSF的准确性与计算生成的检索PSF的长景深相结合。QuadraPol PSF与神经场相结合，可将传统荧光显微镜的采集时间显著缩短约20倍，并可一次性捕获100 mm $^3$ 立方体积。我们通过对沙子表面细菌菌落的全聚焦成像和植物根系形态的可视化，验证了我们的硬件和算法的有效性。我们的方法为推进生物学研究和生态学研究提供了强有力的工具。 et.al.|[2405.10463](http://arxiv.org/abs/2405.10463)|null|

<p align=right>(<a href=#updated-on-20240531>back to top</a>)</p>

[contributors-shield]: https://img.shields.io/github/contributors/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[contributors-url]: https://github.com/Vincentqyw/cv-arxiv-daily/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[forks-url]: https://github.com/Vincentqyw/cv-arxiv-daily/network/members
[stars-shield]: https://img.shields.io/github/stars/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[stars-url]: https://github.com/Vincentqyw/cv-arxiv-daily/stargazers
[issues-shield]: https://img.shields.io/github/issues/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[issues-url]: https://github.com/Vincentqyw/cv-arxiv-daily/issues

