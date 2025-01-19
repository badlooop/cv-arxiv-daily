[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]

## Updated on 2025.01.19
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
|**2025-01-14**|**3D Gaussian Splatting with Normal Information for Mesh Extraction and Improved Rendering**|可区分的3D高斯飞溅已成为一种高效灵活的渲染技术，用于从2D视图集合中表示复杂场景，并实现高质量的实时新颖视图合成。然而，它对光度损失的依赖可能会导致重建的几何结构和提取的网格不精确，特别是在具有高曲率或精细细节的区域。我们提出了一种新的正则化方法，该方法使用从高斯估计的带符号距离函数的梯度来提高渲染质量，同时提取表面网格。规范化的常规监督有助于更好的渲染和网格重建，这对于视频生成、动画、AR-VR和游戏中的下游应用至关重要。我们展示了我们的方法在Mip-NeRF360、坦克和神庙以及深度混合等数据集上的有效性。与其他网格提取渲染方法相比，我们的方法在真实感度量上得分更高，而不会影响网格质量。 et.al.|[2501.08370](http://arxiv.org/abs/2501.08370)|null|
|**2025-01-14**|**VINGS-Mono: Visual-Inertial Gaussian Splatting Monocular SLAM in Large Scenes**|VINGS Mono是一个专为大型场景设计的单目（惯性）高斯散斑（GS）SLAM框架。该框架由四个主要组件组成：VIO前端、2D高斯映射、NVS环路闭合和动态擦除器。在VIO前端中，RGB帧通过密集束调整和不确定性估计进行处理，以提取场景几何形状和姿态。基于该输出，映射模块递增地构建和维护2D高斯映射。2D高斯映射的关键组件包括基于样本的光栅化器、分数管理器和姿态细化，它们共同提高了映射速度和定位精度。这使得SLAM系统能够处理多达5000万个高斯椭球的大规模城市环境。为了确保大规模场景中的全局一致性，我们设计了一个环路闭合模块，该模块创新性地利用高斯散点的新颖视图合成（NVS）功能进行环路闭合检测和高斯图的校正。此外，我们提出了一种动态橡皮擦，以解决现实世界户外场景中动态对象不可避免的存在问题。在室内和室外环境中进行的广泛评估表明，我们的方法实现了与视觉惯性里程表相当的定位性能，同时超越了最近的GS/NeRF SLAM方法。在映射和渲染质量方面，它也明显优于所有现有方法。此外，我们开发了一款移动应用程序，并验证了我们的框架可以仅使用智能手机摄像头和低频IMU传感器实时生成高质量的高斯地图。据我们所知，VINGS Mono是第一种能够在室外环境中运行并支持公里级大型场景的单目高斯SLAM方法。 et.al.|[2501.08286](http://arxiv.org/abs/2501.08286)|null|
|**2025-01-13**|**Evaluating Human Perception of Novel View Synthesis: Subjective Quality Assessment of Gaussian Splatting and NeRF in Dynamic Scenes**|高斯散斑（GS）和神经辐射场（NeRF）是两项突破性的技术，它们彻底改变了新视图合成（NVS）领域，通过从一组稀疏视图的图像中合成多个视点，实现了沉浸式真实感渲染和用户体验。NVS的潜在应用，如高质量的虚拟和增强现实、详细的3D建模和逼真的医学器官成像，强调了从人类感知的角度对NVS方法进行质量评估的重要性。尽管之前的一些研究已经探索了NVS技术的主观质量评估，但它们仍然面临着一些挑战，特别是在NVS方法选择、场景覆盖和评估方法方面。为了应对这些挑战，我们进行了两个主观实验，对NVS技术进行质量评估，包括基于GS和基于NeRF的方法，重点关注动态和现实世界的场景。本研究涵盖了360度、正面和单视点视频，同时提供了更丰富、更多的真实场景。同时，这是首次探索NVS方法在具有运动物体的动态场景中的影响。这两种主观实验有助于从人类感知的角度充分理解不同观察路径的影响，并为未来开发全参考和无参考质量指标铺平道路。此外，我们在拟议的数据库上建立了各种最先进的客观指标的综合基准，强调现有方法仍然难以准确捕捉主观质量。这些结果让我们对现有NVS方法的局限性有了一些了解，并可能促进新NVS方法发展。 et.al.|[2501.08072](http://arxiv.org/abs/2501.08072)|null|
|**2025-01-13**|**Motion Tracks: A Unified Representation for Human-Robot Transfer in Few-Shot Imitation Learning**|教机器人自主完成日常任务仍然是一个挑战。模仿学习（IL）是一种强大的方法，通过演示向机器人灌输技能，但受到收集远程操作机器人数据的劳动密集型过程的限制。人类视频提供了一种可扩展的替代方案，但由于缺乏机器人动作标签，仍然很难直接从中训练IL策略。为了解决这个问题，我们建议将动作表示为图像上的短程2D轨迹。这些动作或运动轨迹捕捉人手或机器人末端执行器的预测运动方向。我们实例化了一个名为运动轨迹策略（MT-pi）的IL策略，该策略接收图像观测值并将运动轨迹作为动作输出。通过利用这种统一的跨实施例动作空间，MT-pi在只需几分钟的人类视频和有限的额外机器人演示的情况下，就可以成功完成任务。在测试时，我们从两个相机视图预测运动轨迹，通过多视图合成恢复6DoF轨迹。MT pi在4个现实世界任务中的平均成功率为86.5%，比不利用人类数据或我们的动作空间的最先进的IL基线高出40%，并推广到仅在人类视频中看到的场景。代码和视频可在我们的网站上找到https://portal-cornell.github.io/motion_track_policy/. et.al.|[2501.06994](http://arxiv.org/abs/2501.06994)|null|
|**2025-01-11**|**MapGS: Generalizable Pretraining and Data Augmentation for Online Mapping via Novel View Synthesis**|在线地图减少了自动驾驶汽车对高清地图的依赖，显著提高了可扩展性。然而，最近的进展往往忽视了跨传感器配置的通用性，导致当模型部署在具有不同摄像头内部和外部的车辆上时，性能下降。随着新型视图合成方法的快速发展，我们研究了这些技术在多大程度上可以用来解决传感器配置泛化挑战。我们提出了一种新的框架，利用高斯飞溅来重建场景，并在目标传感器配置中渲染相机图像。目标配置传感器数据以及映射到目标配置的标签用于训练在线映射模型。我们在nuScenes和Argoverse 2数据集上提出的框架通过有效的数据集增强实现了18%的性能提升，实现了更快的收敛和高效的训练，并且在仅使用25%的原始训练数据时超过了最先进的性能。这实现了数据重用，并减少了对繁琐的数据标记的需求。项目页面位于https://henryzhangzhy.github.io/mapgs. et.al.|[2501.06660](http://arxiv.org/abs/2501.06660)|null|
|**2025-01-11**|**NVS-SQA: Exploring Self-Supervised Quality Representation Learning for Neurally Synthesized Scenes without References**|神经视图合成（NVS），如NeRF和3D高斯散斑，有效地从稀疏视点创建逼真的场景，通常通过PSNR、SSIM和LPIPS等质量评估方法进行评估。然而，这些将合成视图与参考视图进行比较的完整参考方法可能无法完全捕捉神经合成场景（NSS）的感知质量，特别是由于密集参考视图的可用性有限。此外，获取人类感知标签的挑战阻碍了广泛标记数据集的创建，有模型过拟合和泛化能力降低的风险。为了解决这些问题，我们提出了NVS-SQA，这是一种NSS质量评估方法，通过自我监督学习无参考质量表示，而不依赖于人类标签。传统的自监督学习主要依赖于“相同实例，相似表示”的假设和广泛的数据集。然而，鉴于这些条件不适用于NSS质量评估，我们采用启发式线索和质量分数作为学习目标，并采用专门的对比配对准备过程来提高学习的有效性和效率。结果表明，NVS-SQA在很大程度上优于17种无参考方法（即，在SRCC中平均为109.5%，在PLCC中为98.6%，在KRCC中为91.5%，排名第二），甚至在所有评估指标上超过了16种完全参考方法（例如，SRCC为22.9%，PLCC为19.1%，KRCC中排名第二的为18.6%）。 et.al.|[2501.06488](http://arxiv.org/abs/2501.06488)|**[link](https://github.com/vincentqqu/nvs-sqa)**|
|**2025-01-11**|**Aug3D: Augmenting large scale outdoor datasets for Generalizable Novel View Synthesis**|最近的真实感新视图合成（NVS）进展越来越受到人们的关注。然而，这些方法仍然局限于小型室内场景。虽然基于优化的NVS模型试图解决这个问题，但提供显著优势的通用前馈方法仍然没有得到充分的探索。在这项工作中，我们在大规模UrbanScene3D数据集上训练前馈NVS模型PixelNeRF。我们提出了四种训练策略来对这个数据集进行聚类和训练，强调了有限的视图重叠会阻碍性能。为了解决这个问题，我们引入了Aug3D，这是一种利用传统运动结构（SfM）重建场景的增强技术。Aug3D通过网格和语义采样生成条件良好的新视图，以增强前馈NVS模型学习。我们的实验表明，将每个集群的视图数量从20个减少到10个，PSNR提高了10%，但性能仍然不是最优的。Aug3D通过将新生成的新视图与原始数据集相结合，进一步解决了这一问题，证明了其在提高模型预测新视图的能力方面的有效性。 et.al.|[2501.06431](http://arxiv.org/abs/2501.06431)|null|
|**2025-01-09**|**Scaffold-SLAM: Structured 3D Gaussians for Simultaneous Localization and Photorealistic Mapping**|3D高斯散斑（3DGS）最近彻底改变了同步定位和映射（SLAM）中的新颖视图合成。然而，利用3DGS的现有SLAM方法未能同时为单眼、立体和RGB-D相机提供高质量的新颖视图渲染。值得注意的是，一些方法在RGB-D相机上表现良好，但在单眼相机的渲染质量方面却严重下降。在本文中，我们提出了脚手架SLAM，它可以在单目、立体和RGB-D相机上同时进行定位和高质量的真实感映射。我们引入了两项关键创新，以实现这种最先进的视觉质量。首先，我们提出了运动中的外观嵌入，使3D高斯模型能够更好地模拟不同相机姿态下的图像外观变化。其次，我们引入了一个频率正则化金字塔来引导高斯分布，使模型能够有效地捕捉场景中更精细的细节。对单眼、立体和RGB-D数据集的广泛实验表明，脚手架SLAM在真实感映射质量方面明显优于最先进的方法，例如，单眼相机的TUM RGB-D数据集中的PSNR高出16.76%。 et.al.|[2501.05242](http://arxiv.org/abs/2501.05242)|null|
|**2025-01-08**|**FatesGS: Fast and Accurate Sparse-View Surface Reconstruction using Gaussian Splatting with Depth-Feature Consistency**|最近，高斯散斑在计算机视觉领域引发了一种新的趋势。除了新颖的视图合成外，它还被扩展到多视图重建领域。最新的方法有助于完成详细的表面重建，同时确保快速的训练速度。然而，这些方法仍然需要密集的输入视图，并且它们的输出质量会随着稀疏视图的出现而显著降低。我们观察到高斯基元倾向于过拟合少数训练视图，导致有噪声的浮点运算和不完整的重建曲面。在本文中，我们提出了一种创新的稀疏视图重建框架，该框架利用视图内深度和多视图特征一致性来实现非常精确的表面重建。具体来说，我们利用单眼深度排名信息来监督斑块内深度分布的一致性，并采用平滑度损失来增强分布的连续性。为了实现更精细的表面重建，我们通过多视图投影特征优化了深度的绝对位置。在DTU和BlenedMVS上进行的大量实验表明，我们的方法优于最先进的方法，速度提高了60倍至200倍，实现了快速和细粒度的网格重建，而不需要昂贵的预训练。 et.al.|[2501.04628](http://arxiv.org/abs/2501.04628)|null|
|**2025-01-07**|**NeRFs are Mirror Detectors: Using Structural Similarity for Multi-View Mirror Scene Reconstruction with 3D Surface Primitives**|虽然神经辐射场（NeRF）在真实感新颖的视图合成方面取得了突破，但处理镜像表面仍然是一个特别的挑战，因为它们在场景表示中引入了严重的不一致性。之前的尝试要么侧重于重建单个反射物体，要么依赖于强有力的监督指导，即用户提供的镜子可见图像区域的额外注释，从而限制了实际可用性。相比之下，在本文中，我们提出了NeRF-MD，该方法表明NeRFs可以被视为镜像检测器，并且能够重建包含镜像表面的场景的神经辐射场，而不需要事先注释。为此，我们首先通过使用深度重投影损失训练标准NeRF来计算场景几何形状的初始估计。我们的关键见解在于，与镜像表面对应的场景部分仍将表现出明显的光度不一致，而其余部分已经以合理的方式重建。这使我们能够在训练的初始阶段通过将几何图元拟合到这种不一致的区域来检测镜面。利用这些信息，我们在第二个训练阶段联合优化辐射场和镜子几何形状，以提高其质量。我们展示了我们的方法能够忠实地检测场景中的镜子，并重建单个一致的场景表示，并展示了与基线和镜子感知方法相比的潜力。 et.al.|[2501.04074](http://arxiv.org/abs/2501.04074)|**[link](https://github.com/vc-bonn/nerfs-are-mirror-detectors)**|

<p align=right>(<a href=#updated-on-20250119>back to top</a>)</p>

## 3D Reconstruction

|Publish Date|Title|Abstract|PDF|Code|
|---|---|---|---|---|
|**2025-01-16**|**UVRM: A Scalable 3D Reconstruction Model from Unposed Videos**|大型重建模型（LRM）最近已成为创建3D基础模型的流行方法。传统上，使用2D视觉数据训练3D重建模型需要事先了解训练样本的相机姿态，这一过程既耗时又容易出错。因此，3D重建训练仅限于合成3D数据集或具有注释姿势的小规模数据集。在这项研究中，我们研究了使用各种物体的未经处理的视频数据进行3D重建的可行性。我们介绍了UVRM，这是一种新型的3D重建模型，能够在单眼视频上进行训练和评估，而不需要任何关于姿势的信息。UVRM使用变换器网络将视频帧隐式聚合到姿势不变的潜在特征空间中，然后将其解码为三平面3D表示。为了避免在训练过程中需要地面真实姿态注释，UVRM采用了分数蒸馏采样（SDS）方法和综合分析方法的组合，使用预训练的扩散模型逐步合成伪新视图。我们在不依赖姿态信息的情况下，对UVRM在G-Objaverse和CO3D数据集上的性能进行了定性和定量评估。大量实验表明，UVRM能够有效和高效地从未经处理的视频中重建各种3D对象。 et.al.|[2501.09347](http://arxiv.org/abs/2501.09347)|null|
|**2025-01-16**|**OpticFusion: Multi-Modal Neural Implicit 3D Reconstruction of Microstructures by Fusing White Light Interferometry and Optical Microscopy**|白光干涉术（WLI）是一种精确的光学工具，用于测量微结构的3D形貌。然而，传统的WLI无法捕捉样品表面的自然颜色，这对于许多需要3D几何和颜色信息的微型研究应用至关重要。以前的方法试图通过修改WLI硬件和分析软件来克服这一局限性，但这些解决方案通常成本很高。在这项工作中，我们首次从计算机视觉多模态重建的角度解决了这一挑战。我们介绍了OpticFusion，这是一种新方法，它使用额外的数字光学显微镜（OM），使用多视图WLI和OM图像实现自然颜色纹理的3D重建。我们的方法采用两步数据关联过程来获得WLI和OM数据的姿态。通过利用神经隐式表示，我们融合了多模态数据，并应用颜色分解技术来提取样本的自然颜色。OpticFusion在我们的各种微尺度样本的多模态数据集上进行了测试，实现了具有颜色纹理的详细3D重建。我们的方法为众多微尺度研究领域的实际应用提供了一种有效的工具。源代码和我们的真实世界数据集可在https://github.com/zju3dv/OpticFusion. et.al.|[2501.09259](http://arxiv.org/abs/2501.09259)|**[link](https://github.com/zju3dv/opticfusion)**|
|**2025-01-15**|**Unified Few-shot Crack Segmentation and its Precise 3D Automatic Measurement in Concrete Structures**|视觉空间系统在混凝土裂缝检测中变得越来越重要。然而，现有的方法往往缺乏对不同场景的适应性，在基于图像的方法中表现出有限的鲁棒性，并且难以处理弯曲或复杂的几何形状。为了解决这些局限性，本研究通过整合计算机视觉技术和多模态同步定位和映射（SLAM），提出了一种用于二维（2D）裂纹检测、三维（3D）重建和3D自动裂纹测量的创新框架。首先，在DeepLabv3+分割模型的基础上，并利用基础模型Segment Anything model（SAM）进行具体改进，我们开发了一种裂纹分割方法，该方法在不熟悉的场景中具有很强的泛化能力，能够生成精确的2D裂纹掩模。为了提高3D重建的准确性和鲁棒性，光探测和测距（LiDAR）点云与图像数据和分割掩模一起使用。通过利用图像和激光雷达SLAM，我们开发了一个多帧和多模态融合框架，该框架可以生成密集的彩色点云，有效地在3D现实世界尺度上捕获裂纹语义。此外，裂纹几何属性在三维密集点云空间内自动直接测量，超越了传统二维图像测量的局限性。这一进步使该方法适用于具有弯曲和复杂3D几何形状的结构部件。各种混凝土结构的实验结果突出了所提出方法的显著改进和独特优势，证明了其在现实应用中的有效性、准确性和鲁棒性。 et.al.|[2501.09203](http://arxiv.org/abs/2501.09203)|null|
|**2025-01-15**|**Multi-Class Traffic Assignment using Multi-View Heterogeneous Graph Attention Networks**|当使用传统的基于优化的方法时，解决大型网络的流量分配问题在计算上具有挑战性。在我们的研究中，我们为涉及多级车辆的交通分配开发了一种创新的替代模型。我们通过采用异构图神经网络来实现这一点，该网络使用针对不同车辆类别量身定制的多视图图注意力机制，以及连接起点-终点对的额外链接。我们还将基于节点的流量守恒定律整合到损失函数中。因此，我们的模型坚持流量守恒，同时对链路流量和利用率进行高度准确的预测。通过在城市交通网络上进行的数值实验，我们证明我们的模型在用户均衡和系统最优交通分配版本的收敛速度和预测精度方面都优于传统的神经网络方法。 et.al.|[2501.09117](http://arxiv.org/abs/2501.09117)|null|
|**2025-01-15**|**Scalable and High-Quality Neural Implicit Representation for 3D Reconstruction**|最近提出了各种基于SDF的神经隐式曲面重建方法，并表现出显著的建模能力。然而，由于单个网络的全局性和有限的表示能力，现有的方法仍然存在许多缺点，例如重建的精度和规模有限。在本文中，我们提出了一种通用、可扩展和高质量的神经隐式表示来解决这些问题。我们将分而治之的方法整合到基于神经SDF的重建中。具体来说，我们将对象或场景建模为具有重叠区域的多个独立局部神经SDF的融合。我们表示的构建涉及三个关键步骤：（1）基于对象结构或数据分布构建局部辐射场的分布和重叠关系，（2）相邻局部SDF的相对姿态配准，以及（3）SDF混合。由于每个局部区域的独立表示，我们的方法不仅可以实现高保真的表面重建，还可以实现可扩展的场景重建。大量的实验结果证明了我们提出的方法的有效性和实用性。 et.al.|[2501.08577](http://arxiv.org/abs/2501.08577)|null|
|**2025-01-13**|**3DGS-to-PC: Convert a 3D Gaussian Splatting Scene into a Dense Point Cloud or Mesh**|3D高斯散斑（3DGS）擅长生成高度详细的3D重建，但这些场景通常需要专门的渲染器才能进行有效的可视化。相比之下，点云是一种广泛使用的3D表示，与大多数流行的3D处理软件兼容，但将3DGS场景转换为点云是个复杂的挑战。在这项工作中，我们将3DGS引入PC，这是一个灵活且高度可定制的框架，能够将3DGS场景转换为密集、高精度的点云。我们将每个高斯分布的点作为3D密度函数进行概率采样。我们还使用到高斯中心的马氏距离来阈值化新点，以防止极端异常值。结果是一个点云，它非常接近编码到3D高斯场景中的形状。单个高斯人使用球面调和来根据视图调整颜色，每个点可能只会为最终渲染的场景提供微妙的颜色提示。为了避免与最终点云不匹配的虚假或不正确的颜色，我们通过定制的图像渲染方法重新计算高斯颜色，为每个高斯颜色分配其在所有视图中贡献最大的像素的颜色。3DGS到PC还支持通过泊松曲面重建生成网格，该重建应用于从预测的曲面高斯中采样的点。这允许从3DGS场景生成彩色网格，而无需重新训练。该软件包具有高度的可定制性，能够简单地集成到现有的3DGS管道中。3DGS to PC提供了一个强大的工具，用于将3DGS数据转换为基于点云和曲面的格式。 et.al.|[2501.07478](http://arxiv.org/abs/2501.07478)|**[link](https://github.com/lewis-stuart-11/3dgs-to-pc)**|
|**2025-01-16**|**PO-GVINS: Tightly Coupled GNSS-Visual-Inertial Integration with Pose-Only Representation**|准确可靠的定位对于自动驾驶、无人机和智能机器人中的感知、决策和其他高级应用至关重要。鉴于独立传感器的固有局限性，将具有互补功能的异构传感器集成是实现这一目标的最有效方法之一。本文提出了一种基于滤波的紧密耦合全球导航卫星系统（GNSS）-视觉惯性定位框架，该框架仅应用于视觉惯性系统（VINS），称为PO-GVINS。具体来说，当前VINS中使用的多视图成像需要先验的3D特征，然后联合估计相机姿态和3D特征位置，这不可避免地会引入特征的线性化误差以及面对维度爆炸。然而，仅姿态（PO）公式被证明与多视图成像等效，并已应用于视觉重建，它使用两个相机姿态表示特征深度，从而从状态向量中去除3D特征位置，避免了上述困难。受此启发，我们首先在VINS中应用PO配方，即PO-VINS。然后将GNSS原始测量值与解决的整周模糊度相结合，以实现准确和无漂移的估计。大量实验表明，所提出的PO-VINS明显优于多状态约束卡尔曼滤波器（MSCKF）。通过结合GNSS测量，PO-GVINS实现了准确、无漂移的状态估计，使其成为在具有挑战性的环境中进行定位的稳健解决方案。 et.al.|[2501.07259](http://arxiv.org/abs/2501.07259)|null|
|**2025-01-13**|**Representation Learning of Point Cloud Upsampling in Global and Local Inputs**|近年来，点云上采样在三维重建等领域得到了广泛的应用。我们的研究通过表示学习在全球和局部层面调查了影响点云上采样的因素。具体来说，本文将同一点云模型对象的全局和局部信息输入到两个编码器中，以提取这些特征，融合它们，然后将组合的特征馈送到上采样解码器中。目标是通过利用来自全局和局部输入的先验知识来解决点云中的稀疏性和噪声问题。所提出的框架可以应用于任何最先进的点云上采样神经网络。在一系列基于自动编码器的模型上进行了实验，利用深度学习，对全局和局部输入都产生了可解释性，结果证明，我们提出的框架可以进一步改善先前SOTA工作中的上采样效果。同时，显著性图反映了全局和局部特征输入之间的差异，以及同时使用这两种输入进行训练的有效性。 et.al.|[2501.07076](http://arxiv.org/abs/2501.07076)|null|
|**2025-01-14**|**SplatMAP: Online Dense Monocular SLAM with 3D Gaussian Splatting**|由于运动结构（SfM）和单眼SLAM等传统方法在准确捕捉场景细节方面的固有局限性，从单眼视频中实现高保真3D重建仍然具有挑战性。虽然神经辐射场（NeRF）等可微分渲染技术解决了其中一些挑战，但它们的高计算成本使其不适合实时应用。此外，现有的3D高斯散斑（3DGS）方法通常侧重于光度一致性，忽略了几何精度，并且未能利用SLAM的动态深度和姿态更新进行场景细化。我们提出了一种将密集SLAM与3DGS集成在一起的框架，用于实时、高保真的密集重建。我们的方法引入了SLAM知情自适应加密，通过利用SLAM的密集点云动态更新和加密高斯模型。此外，我们还引入了几何引导优化，该优化结合了边缘感知几何约束和光度一致性，共同优化3DGS场景表示的外观和几何，实现了详细准确的SLAM映射重建。在Replica和TUM-RGBD数据集上的实验证明了我们的方法的有效性，在单眼系统中取得了最先进的结果。具体来说，我们的方法在Replica上实现了36.864的PSNR、0.985的SSIM和0.040的LPIPS，分别比之前的SOTA提高了10.7%、6.4%和49.4%。在TUM-RGBD上，我们的方法在相同的指标上比最接近的基线高出10.2%、6.6%和34.7%。这些结果突显了我们的框架在弥合光度和几何密集3D场景表示之间的差距方面的潜力，为实用和高效的单眼密集重建铺平了道路。 et.al.|[2501.07015](http://arxiv.org/abs/2501.07015)|null|
|**2025-01-12**|**CULTURE3D: Cultural Landmarks and Terrain Dataset for 3D Applications**|在这篇论文中，我们使用从世界各地捕获的高分辨率图像，提出了一个大规模的细粒度数据集。与现有数据集相比，我们的数据集提供了更大的大小，并包含了更高级别的细节，使其特别适合细粒度的3D应用程序。值得注意的是，我们的数据集是使用无人机捕获的航空图像构建的，这为捕获真实世界的场地布局和建筑结构提供了更准确的视角。通过使用这些详细的图像重建环境，我们的数据集支持高斯散斑的COLMAP格式和运动结构（SfM）方法等应用。它与广泛使用的技术兼容，包括SLAM、多视图立体和神经辐射场（NeRF），可实现精确的3D重建和点云。这使其成为重建和分割任务的基准。该数据集能够与多模态数据无缝集成，支持从建筑重建到虚拟旅游的一系列3D应用。它的灵活性促进了创新，促进了3D建模和分析的突破。 et.al.|[2501.06927](http://arxiv.org/abs/2501.06927)|null|

<p align=right>(<a href=#updated-on-20250119>back to top</a>)</p>

## Diffusion

|Publish Date|Title|Abstract|PDF|Code|
|---|---|---|---|---|
|**2025-01-16**|**SynthLight: Portrait Relighting with Diffusion Model by Learning to Re-render Synthetic Faces**|我们介绍SynthLight，一种用于肖像再照明的扩散模型。我们的方法将图像重新照明视为一个重新渲染问题，其中像素会根据环境照明条件的变化而变化。使用基于物理的渲染引擎，我们合成了一个数据集，在不同的光照条件下用3D头部资产模拟这种光照条件转换。我们提出了两种训练和推理策略来弥合合成图像域和真实图像域之间的差距：（1）利用没有照明标签的真实人体肖像进行多任务训练；（2） 基于无分类器引导的推理时间扩散采样过程，该过程利用输入肖像来更好地保留细节。我们的方法可以推广到各种真实照片，并产生逼真的照明效果，包括镜面高光和投射阴影，同时保留主体的身份。我们对Light Stage数据的定量实验表明，其结果与最先进的再照明方法相当。我们对野外图像的定性结果展示了丰富而前所未有的照明效果。项目页面：\url{https://vrroom.github.io/synthlight/} et.al.|[2501.09756](http://arxiv.org/abs/2501.09756)|null|
|**2025-01-16**|**Learnings from Scaling Visual Tokenizers for Reconstruction and Generation**|通过自动编码的视觉标记化通过将像素压缩到潜在空间中，为最先进的图像和视频生成模型提供了支持。尽管缩放基于Transformer的生成器是最近进展的核心，但标记器组件本身很少被缩放，这就留下了关于自动编码器设计选择如何影响其重建目标和下游生成性能的悬而未决的问题。我们的工作旨在探索自动编码器的缩放，以填补这一空白。为了促进这一探索，我们用增强的视觉变换器架构（ViTok）替换了典型的卷积骨干网，用于令牌化。我们在远远超过ImageNet-1K的大规模图像和视频数据集上训练ViTok，消除了标记器缩放的数据限制。我们首先研究了缩放自动编码器瓶颈如何影响重建和生成，发现虽然它与重建高度相关，但它与生成的关系更为复杂。接下来，我们探讨了分别缩放自动编码器的编码器和解码器对重建和生成性能的影响。至关重要的是，我们发现缩放编码器对重建或生成的增益都很小，而缩放解码器可以促进重建，但对生成的好处是喜忧参半的。基于我们的探索，我们将ViTok设计为一种轻量级的自动编码器，它在ImageNet-1K和COCO重建任务（256p和512p）上与最先进的自动编码器实现了具有竞争力的性能，同时在UCF-101的16帧128p视频重建上优于现有的自动编码器。当与扩散变换器集成时，ViTok在ImageNet-1K的图像生成方面表现出了具有竞争力的性能，并为UCF-101上的类条件视频生成设定了新的最先进的基准。 et.al.|[2501.09755](http://arxiv.org/abs/2501.09755)|null|
|**2025-01-16**|**FAST: Efficient Action Tokenization for Vision-Language-Action Models**|自回归序列模型，如基于Transformer的视觉语言动作（VLA）策略，对于捕捉复杂和可推广的机器人行为非常有效。然而，这样的模型要求我们选择连续动作信号的标记化，这决定了模型预测的离散符号如何映射到连续的机器人动作。我们发现，目前基于简单的每维、每时间步分箱方案的机器人动作标记化方法在从高频机器人数据中学习灵巧技能时通常表现不佳。为了应对这一挑战，我们提出了一种基于离散余弦变换的新的基于压缩的机器人动作标记化方案。我们的标记化方法，频率空间动作序列标记化（FAST），使我们能够为标准离散化方法完全失败的高度灵巧和高频任务训练自回归VLAs。基于FAST，我们发布了FAST+，这是一个通用的机器人动作标记器，在1M真实机器人动作轨迹上训练。它可以用作各种机器人动作序列的黑盒标记器，具有不同的动作空间和控制频率。最后，我们表明，当与pi0 VLA结合时，我们的方法可以扩展到在10k小时的机器人数据上进行训练，并与扩散VLA的性能相匹配，同时将训练时间减少了5倍。 et.al.|[2501.09747](http://arxiv.org/abs/2501.09747)|null|
|**2025-01-16**|**Inference-Time Scaling for Diffusion Models beyond Scaling Denoising Steps**|生成模型在各个领域都产生了重大影响，这主要是由于它们在训练过程中能够通过增加数据、计算资源和模型大小来扩展，这是一种以缩放规律为特征的现象。最近的研究已经开始探索大型语言模型（LLM）中的推理时间缩放行为，揭示了如何在推理过程中通过额外的计算进一步提高性能。与LLM不同，扩散模型固有地具有通过去噪步骤数量调整推理时间计算的灵活性，尽管性能增益通常在几十个步骤后趋于平稳。在这项工作中，我们探索了扩散模型在增加去噪步骤之外的推理时间缩放行为，并研究了生成性能如何随着计算量的增加而进一步提高。具体来说，我们考虑了一个搜索问题，旨在为扩散采样过程识别更好的噪声。我们沿着两个轴构建设计空间：用于提供反馈的验证器和用于找到更好噪声候选的算法。通过对类条件和文本条件图像生成基准的广泛实验，我们的发现表明，增加推理时间计算可以显著提高扩散模型生成的样本的质量，并且由于图像的复杂性，可以专门选择框架中组件的组合来符合不同的应用场景。 et.al.|[2501.09732](http://arxiv.org/abs/2501.09732)|null|
|**2025-01-16**|**Reward-Guided Controlled Generation for Inference-Time Alignment in Diffusion Models: Tutorial and Review**|本教程提供了关于推理时间指导和对齐方法的深入指南，用于优化扩散模型中的下游奖励函数。虽然扩散模型以其生成建模能力而闻名，但在生物学等领域的实际应用中，通常需要生成最大化特定指标（例如稳定性、蛋白质亲和力、与靶结构的接近度）的样本。在这些场景中，扩散模型不仅可以生成逼真的样本，还可以在推理时明确地最大化所需的度量，而无需进行微调。本教程探讨了此类推理时间算法的基础方面。我们从统一的角度回顾了这些方法，证明了当前的技术——如基于序贯蒙特卡洛（SMC）的指导、基于值的采样和分类器指导——旨在近似软最优去噪过程（也称为RL中的策略），该过程将预训练的去噪过程与作为前瞻函数的值函数相结合，该函数从中间状态预测到最终奖励。在此框架内，我们提出了文献中尚未涉及的几种新算法。此外，我们讨论了（1）与推理时间技术相结合的微调方法，（2）基于蒙特卡洛树搜索等搜索算法的推理时间算法，这些算法在当前的研究中受到的关注有限，以及（3）语言模型和扩散模型中推理时间算法之间的联系。本教程关于蛋白质设计的代码可在以下网址获得https://github.com/masa-ue/AlignInversePro et.al.|[2501.09685](http://arxiv.org/abs/2501.09685)|null|
|**2025-01-16**|**Optimal paths and dynamical symmetry breaking in the current fluctuations of driven diffusive media**|大偏差理论为从微观动力学角度理解多体非平衡系统中的宏观波动和集体现象提供了一个框架。在这些讲义中，我们讨论了电流的大偏差统计，这是一种中心可观测的不平衡现象，主要使用宏观波动理论（MFT），也使用微观光谱方法。特别强调描述导致罕见波动的最佳路径，以及在波动水平上出现的不同动力学对称性破缺现象。我们首先概述了MFT所描述的驱动扩散系统中的轨迹统计。我们讨论了可加性原理，这是一种计算一维非平衡系统中电流分布的简化猜想，并将这一想法扩展到更高的维度，在那里，最优电流矢量场的非局部结构变得至关重要。接下来，我们探讨电流波动中的动态相变（DPTs），这在轨迹统计中表现为对称性破缺事件。这些包括开放通道中的粒子-空穴对称性破缺DPTs，为此我们提出了朗道理论以及电流和序参数的联合统计。还讨论了周期系统中的时间平移对称破缺DPTs，其中相干行进凝聚体出现以促进电流偏差。我们还讨论了导致这些DPT的微观光谱机制，这与主导本征空间的新简并有关。利用这种光谱视角，我们发现了行波DPTs中最近发现的物质时间晶体相的特征，并使用Doob变换提出了一种堆积场机制，以在驱动系统中创建可编程的时间晶体。最后，我们讨论了这一快速发展领域的开放挑战和未来方向。 et.al.|[2501.09629](http://arxiv.org/abs/2501.09629)|null|
|**2025-01-16**|**A simple model of a sequence-reading diffusion: non-self-averaging and self-averaging properties**|受结扩散运动对给定DNA上核苷酸实际序列的敏感性问题的启发，我们在这里研究了一个简单的序列读取扩散模型，该模型涉及具有不同相互作用能的“字母” $a$和$B$的冷冻序列的拉伸链。这条链包含一个变形——疝气——它将底部的两个字母连接在一起，使它们相互作用。由于与溶剂的相互作用，疝气沿着链进行随机跳跃运动，过渡速率取决于其实际位置。我们的两个焦点问题是a）各种输运性质对字母相互作用能的依赖性，以及b）这些性质是否对序列的不同实现具有自平均性。我们证明了通过有限区间的电流、该区间的电阻和该区间上的分裂概率缺乏自平均性。相反，通过具有$N$个位点的有限区间的平均首次通过时间和周期链中的扩散系数在$N\to\infty$的极限内是自平均的。同时，正如数值模拟所证明的那样，后两个属性在有限的$N$ 下表现出样本间的波动。 et.al.|[2501.09583](http://arxiv.org/abs/2501.09583)|null|
|**2025-01-16**|**Existence of weak solutions for fast diffusion equation with a divergence type of drift term**|本文研究了具有散度型漂移项的快速扩散方程。在假设漂移的某些类别与多孔介质方程中的漂移不同的情况下，我们建立了非负 $L^q$ -弱解的存在性，该弱解满足Wasserstein空间中的能量估计，甚至进一步满足速度估计。当漂移具有无散度结构时，我们在漂移的较弱条件下构造弱解。此外，同样的技术部分扩展到多孔介质方程。作为应用，我们还讨论了快速扩散型粘性Boussinesq系统。 et.al.|[2501.09539](http://arxiv.org/abs/2501.09539)|null|
|**2025-01-16**|**VanGogh: A Unified Multimodal Diffusion-based Framework for Video Colorization**|视频着色旨在将灰度视频转换为生动的颜色表示，同时保持时间一致性和结构完整性。现有的视频着色方法往往存在颜色渗出的问题，缺乏全面的控制，特别是在复杂的运动或多样化的语义线索下。为此，我们介绍了VanGogh，这是一个统一的基于多模态扩散的视频着色框架。VanGogh使用Dual Qformer来对齐和融合来自多种模态的特征，并辅以深度引导生成过程和光流损失来解决这些挑战，这有助于减少颜色溢出。此外，还实施了颜色注入策略和亮度通道替换，以提高泛化能力并减轻闪烁伪影。得益于这种设计，用户可以对生成过程进行全局和局部控制，从而获得更高质量的彩色视频。广泛的定性和定量评估以及用户研究表明，梵高实现了卓越的时间一致性和色彩保真度。项目页面：https://becauseimbatman0.github.io/VanGogh. et.al.|[2501.09499](http://arxiv.org/abs/2501.09499)|null|
|**2025-01-16**|**Pruning for Sparse Diffusion Models based on Gradient Flow**|扩散模型（DM）在生成模型中具有令人印象深刻的能力，但仅限于较慢的推理速度和较高的计算成本。以前的工作利用单次结构修剪从预训练的DM中导出轻量级DM，但这种方法通常会导致生成质量的显著下降，并可能导致关键权重的删除。因此，我们提出了一种基于梯度流的迭代修剪方法，包括梯度流修剪过程和梯度流修剪准则。我们采用渐进式软修剪策略来保持掩模矩阵的连续性，并基于稀疏空间中的修剪准则沿能量函数的梯度流引导掩模矩阵，从而避免了单次修剪通常会导致的突然信息丢失。基于梯度流的准则修剪参数，去除这些参数会增加损失函数的梯度范数，并且可以在迭代修剪阶段使修剪后的模型快速收敛。我们在广泛使用的数据集上进行的广泛实验表明，我们的方法在效率和与预训练模型的一致性方面取得了卓越的性能。 et.al.|[2501.09464](http://arxiv.org/abs/2501.09464)|null|

<p align=right>(<a href=#updated-on-20250119>back to top</a>)</p>

## NeRF

|Publish Date|Title|Abstract|PDF|Code|
|---|---|---|---|---|
|**2025-01-15**|**CityDreamer4D: Compositional Generative Model of Unbounded 4D Cities**|近年来，3D场景生成引起了越来越多的关注，并取得了重大进展。生成4D城市比3D场景更具挑战性，因为存在结构复杂、视觉多样的物体，如建筑物和车辆，并且人类对城市环境中的扭曲更加敏感。为了解决这些问题，我们提出了CityDreamer4D，这是一个专门为生成无界4D城市而定制的组合生成模型。我们的主要见解是1）4D城市生成应该将动态对象（如车辆）与静态场景（如建筑物和道路）分开，2）4D场景中的所有对象都应该由建筑物、车辆和背景材料的不同类型的神经场组成。具体来说，我们提出了交通场景生成器和无边界布局生成器，使用高度紧凑的BEV表示生成动态交通场景和静态城市布局。4D城市中的对象是通过结合面向对象和面向实例的神经场来生成的，用于背景材料、建筑物和车辆。为了适应背景材料和实例的不同特征，神经场采用定制的生成哈希网格和周期性位置嵌入作为场景参数化。此外，我们还为城市生成提供了一套全面的数据集，包括OSM、GoogleEarth和CityTopia。OSM数据集提供了各种真实世界的城市布局，而谷歌地球和CityTopia数据集则提供了大规模、高质量的城市图像，并附有3D实例注释。利用其组合设计，CityDreamer4D支持一系列下游应用程序，如实例编辑、城市风格化和城市模拟，同时在生成逼真的4D城市方面提供最先进的性能。 et.al.|[2501.08983](http://arxiv.org/abs/2501.08983)|**[link](https://github.com/hzxie/CityDreamer4D)**|
|**2025-01-15**|**Score-based 3D molecule generation with neural fields**|我们介绍了一种基于连续原子密度场的3D分子的新表示方法。使用这种表示法，我们提出了一种基于步跳采样的新模型，用于使用神经场在连续空间中无条件生成3D分子。我们的模型FuncMol使用条件神经场将分子场编码为潜码，使用Langevin MCMC从高斯平滑分布中采样噪声码（walk），在一步中对这些样本进行去噪（jump），最后将它们解码为分子场。与大多数方法不同，FuncMol可以在不假设分子结构的情况下进行3D分子的全原子生成，并且可以很好地与分子的大小进行缩放。我们的方法在类药物分子上取得了具有竞争力的结果，并且很容易扩展到大环肽，采样速度至少快一个数量级。该代码可在以下网址获得https://github.com/prescient-design/funcmol. et.al.|[2501.08508](http://arxiv.org/abs/2501.08508)|**[link](https://github.com/prescient-design/funcmol)**|
|**2025-01-10**|**Nonlinear partial differential equations in neuroscience: from modelling to mathematical theory**|许多偏微分方程组已被提出作为大型神经元网络中复杂集体行为的简化表示。在这项调查中，我们简要讨论了它们的推导，然后回顾了为处理这些模型的独特特征而开发的数学方法，这些模型通常是非线性和非局部的。第一部分重点介绍抛物型福克-普朗克方程：非线性噪声泄漏积分和火神经元模型，PDE形式的随机神经场及其在网格单元中的应用，以及基于速率的决策模型。第二部分涉及双曲线输运方程，即自上次排放以来经过的时间模型和基于跳跃的泄漏积分和火灾模型。最后一部分介绍了一些动力学介观模型，特别关注动力学电压电导模型和FitzHugh-Nagumo动力学福克-普朗克系统。 et.al.|[2501.06015](http://arxiv.org/abs/2501.06015)|null|
|**2025-01-10**|**Locality-aware Gaussian Compression for Fast and High-quality Rendering**|我们提出了LocoGS，这是一种局部感知的3D高斯散斑（3DGS）框架，它利用3D高斯的空间相干性对体积场景进行紧凑建模。为此，我们首先分析了3D高斯属性的局部相干性，并提出了一种新的局部感知3D高斯表示，该表示使用具有最小存储要求的神经场表示对局部相干高斯属性进行有效编码。除了新颖的表示方法外，LocoGS还经过精心设计，添加了密集初始化、自适应球面谐波带宽方案和针对不同高斯属性的不同编码方案等附加组件，以最大限度地提高压缩性能。实验结果表明，对于代表性的真实世界3D数据集，我们的方法优于现有的紧凑高斯表示的渲染质量，同时实现了从54.6美元到96.6美元的压缩存储大小，以及从2.1美元到2.4美元的渲染速度。甚至我们的方法也证明了平均渲染速度比最先进的压缩方法高2.4倍，具有相当的压缩性能。 et.al.|[2501.05757](http://arxiv.org/abs/2501.05757)|null|
|**2025-01-08**|**KN-LIO: Geometric Kinematics and Neural Field Coupled LiDAR-Inertial Odometry**|激光雷达惯性测距（LIO）的最新进展推动了大量应用。然而，传统的LIO系统往往更侧重于定位而不是映射，映射主要由稀疏的几何元素组成，这对于下游任务来说并不理想。最近新兴的神经场技术在密集测绘方面具有巨大的潜力，但纯激光雷达测绘很难在高动态车辆上进行。为了缓解这一挑战，我们提出了一种新的解决方案，将几何运动学与神经场紧密耦合，以增强同时状态估计和密集映射能力。我们提出了半耦合和紧耦合的运动学神经LIO（KN-LIO）系统，该系统利用在线SDF解码和迭代误差状态卡尔曼滤波来融合激光和惯性数据。我们的KN-LIO最大限度地减少了信息丢失，提高了状态估计的准确性，同时也适应了异步多LiDAR输入。对各种高动态数据集的评估表明，我们的KN-LIO在姿态估计方面的性能与现有最先进的解决方案相当或更优，并且与纯基于LiDAR的方法相比，提供了更高的密集映射精度。相关代码和数据集将在https://**上提供。 et.al.|[2501.04263](http://arxiv.org/abs/2501.04263)|null|
|**2025-01-06**|**NeuroPMD: Neural Fields for Density Estimation on Product Manifolds**|我们提出了一种新的深度神经网络方法，用于在乘积黎曼流形域上进行密度估计。在我们的方法中，网络直接参数化未知密度函数，并使用惩罚最大似然框架进行训练，惩罚项使用流形微分算子形成。网络架构和估计算法经过精心设计，以应对高维积流形域的挑战，有效地减轻了限制传统核和基展开估计器的维数灾难，并克服了非专用神经网络方法遇到的收敛问题。广泛的模拟和对大脑结构连接数据的实际应用突显了我们的方法相对于竞争对手的明显优势。 et.al.|[2501.02994](http://arxiv.org/abs/2501.02994)|**[link](https://github.com/will-consagra/neuropmd)**|
|**2025-01-03**|**Fusion DeepONet: A Data-Efficient Neural Operator for Geometry-Dependent Hypersonic Flows on Arbitrary Grids**|设计再入飞行器需要准确预测其几何形状周围的高超音速流动。对这种流动的快速预测可以彻底改变车辆设计，特别是对于变形几何形状。我们评估了先进的神经算子模型，如深度算子网络（DeepONet）、参数条件U-Net、傅里叶神经算子（FNO）和MeshGraphNet，目的是解决在有限数据下学习依赖几何的高超音速流场的挑战。具体来说，我们比较了两种网格类型的这些模型的性能：均匀笛卡尔网格和不规则网格。为了训练这些模型，我们使用36个独特的椭圆几何体，使用高阶熵稳定的DGSEM求解器生成高保真模拟，强调了使用稀缺数据集的挑战。我们评估并比较了四种基于算子的模型在预测椭圆体周围高超音速流场方面的有效性。此外，我们开发了一个名为Fusion DeepONet的新框架，该框架利用了神经场概念，并在不同的几何结构中有效地进行了推广。尽管训练数据稀缺，Fusion DeepONet在均匀网格上的性能与参数条件U-Net相当，而在不规则、任意网格上的表现优于MeshGraphNet和vanilla DeepONnet。与U-Net、MeshGraphNet和FNO相比，Fusion DeepONet需要更少的可训练参数，使其计算效率更高。我们还使用奇异值分解分析了Fusion DeepONet模型的基函数。该分析表明，Fusion DeepONet能够有效地推广到看不见的解决方案，并适应不同的几何形状和网格点，证明了其在训练数据有限的情况下的鲁棒性。 et.al.|[2501.01934](http://arxiv.org/abs/2501.01934)|null|
|**2024-12-30**|**Hierarchical Pose Estimation and Mapping with Multi-Scale Neural Feature Fields**|机器人应用需要对场景有全面的了解。近年来，基于神经场的参数化整个环境的方法已经变得流行。由于其连续性和学习场景先验的能力，这些方法很有前景。然而，当处理未知的传感器姿态和连续测量时，在机器人中使用神经场变得具有挑战性。本文主要研究大规模神经隐式SLAM的传感器姿态估计问题。我们从概率的角度研究了隐式映射，并提出了具有相应神经网络架构的分层姿态估计。我们的方法非常适合大规模隐式映射表示。所提出的方法在连续的室外LiDAR扫描上运行，实现了精确的姿态估计，同时保持了短轨迹和长轨迹的稳定映射质量。我们在适合大规模重建的结构化稀疏隐式表示上构建了我们的方法，并使用KITTI和MaiCity数据集对其进行了评估。我们的方法在未知姿态的映射方面优于基线，并实现了最先进的定位精度。 et.al.|[2412.20976](http://arxiv.org/abs/2412.20976)|null|
|**2024-12-26**|**Humans as a Calibration Pattern: Dynamic 3D Scene Reconstruction from Unsynchronized and Uncalibrated Videos**|最近关于动态神经场重建的工作假设输入来自具有已知姿势的同步多视图视频。这些输入约束在现实世界的设置中经常得不到满足，使得这种方法不切实际。我们证明，如果视频捕捉到人体运动，则姿态未知的非同步视频可以生成动态神经场。人类是最常见的动态主体之一，其姿势可以使用最先进的方法进行估计。在有噪声的情况下，估计的人体形状和姿态参数为训练一致的动态神经表示的高度非凸和欠约束问题提供了一个不错的初始化。给定人类的姿势和形状序列，我们估计视频之间的时间偏移，然后通过分析3D关节位置进行相机姿势估计。然后，我们使用多分辨率脊训练动态NeRF，同时细化时间偏移和相机姿态。该设置仍然涉及优化许多参数，因此，我们引入了一种鲁棒的渐进学习策略来稳定该过程。实验表明，我们的方法在具有挑战性的条件下实现了精确的时空校准和高质量的场景重建。 et.al.|[2412.19089](http://arxiv.org/abs/2412.19089)|null|
|**2024-12-29**|**PartGen: Part-level 3D Generation and Reconstruction with Multi-View Diffusion Models**|文本或图像到3D生成器和3D扫描仪现在可以生成具有高质量形状和纹理的3D资产。这些资产通常由一个单一的融合表示组成，如隐式神经场、高斯混合或网格，没有任何有用的结构。然而，大多数应用程序和创意工作流程都要求资产由几个可以独立操作的有意义的部分组成。为了解决这一差距，我们引入了PartGen，这是一种新颖的方法，可以从文本、图像或非结构化3D对象生成由有意义的部分组成的3D对象。首先，给定生成或渲染的3D对象的多个视图，多视图扩散模型提取一组合理且视图一致的零件分割，将对象划分为零件。然后，第二个多视图扩散模型分别获取每个部分，填充遮挡，并通过将这些完成的视图馈送到3D重建网络来使用它们进行3D重建。这个完成过程考虑了整个对象的上下文，以确保各部分紧密结合。生成完成模型可以弥补因遮挡而丢失的信息；在极端情况下，它可以根据输入的3D资源产生完全不可见的部分的幻觉。我们在生成的和真实的3D资产上评估了我们的方法，并表明它在很大程度上优于分割和零件提取基线。我们还展示了3D零件编辑等下游应用程序。 et.al.|[2412.18608](http://arxiv.org/abs/2412.18608)|null|

<p align=right>(<a href=#updated-on-20250119>back to top</a>)</p>

[contributors-shield]: https://img.shields.io/github/contributors/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[contributors-url]: https://github.com/Vincentqyw/cv-arxiv-daily/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[forks-url]: https://github.com/Vincentqyw/cv-arxiv-daily/network/members
[stars-shield]: https://img.shields.io/github/stars/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[stars-url]: https://github.com/Vincentqyw/cv-arxiv-daily/stargazers
[issues-shield]: https://img.shields.io/github/issues/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[issues-url]: https://github.com/Vincentqyw/cv-arxiv-daily/issues

