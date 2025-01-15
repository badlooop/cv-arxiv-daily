[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]

## Updated on 2025.01.15
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
|**2025-01-13**|**Motion Tracks: A Unified Representation for Human-Robot Transfer in Few-Shot Imitation Learning**|教机器人自主完成日常任务仍然是一个挑战。模仿学习（IL）是一种强大的方法，通过演示向机器人灌输技能，但受到收集远程操作机器人数据的劳动密集型过程的限制。人类视频提供了一种可扩展的替代方案，但由于缺乏机器人动作标签，仍然很难直接从中训练IL策略。为了解决这个问题，我们建议将动作表示为图像上的短程2D轨迹。这些动作或运动轨迹捕捉人手或机器人末端执行器的预测运动方向。我们实例化了一个名为运动轨迹策略（MT-pi）的IL策略，该策略接收图像观测值并将运动轨迹作为动作输出。通过利用这种统一的跨实施例动作空间，MT-pi在只需几分钟的人类视频和有限的额外机器人演示的情况下，就可以成功完成任务。在测试时，我们从两个相机视图预测运动轨迹，通过多视图合成恢复6DoF轨迹。MT pi在4个现实世界任务中的平均成功率为86.5%，比不利用人类数据或我们的动作空间的最先进的IL基线高出40%，并推广到仅在人类视频中看到的场景。代码和视频可在我们的网站上找到https://portal-cornell.github.io/motion_track_policy/. et.al.|[2501.06994](http://arxiv.org/abs/2501.06994)|null|
|**2025-01-11**|**MapGS: Generalizable Pretraining and Data Augmentation for Online Mapping via Novel View Synthesis**|在线地图减少了自动驾驶汽车对高清地图的依赖，显著提高了可扩展性。然而，最近的进展往往忽视了跨传感器配置的通用性，导致当模型部署在具有不同摄像头内部和外部的车辆上时，性能下降。随着新型视图合成方法的快速发展，我们研究了这些技术在多大程度上可以用来解决传感器配置泛化挑战。我们提出了一种新的框架，利用高斯飞溅来重建场景，并在目标传感器配置中渲染相机图像。目标配置传感器数据以及映射到目标配置的标签用于训练在线映射模型。我们在nuScenes和Argoverse 2数据集上提出的框架通过有效的数据集增强实现了18%的性能提升，实现了更快的收敛和高效的训练，并且在仅使用25%的原始训练数据时超过了最先进的性能。这实现了数据重用，并减少了对繁琐的数据标记的需求。项目页面位于https://henryzhangzhy.github.io/mapgs. et.al.|[2501.06660](http://arxiv.org/abs/2501.06660)|null|
|**2025-01-11**|**NVS-SQA: Exploring Self-Supervised Quality Representation Learning for Neurally Synthesized Scenes without References**|神经视图合成（NVS），如NeRF和3D高斯散斑，有效地从稀疏视点创建逼真的场景，通常通过PSNR、SSIM和LPIPS等质量评估方法进行评估。然而，这些将合成视图与参考视图进行比较的完整参考方法可能无法完全捕捉神经合成场景（NSS）的感知质量，特别是由于密集参考视图的可用性有限。此外，获取人类感知标签的挑战阻碍了广泛标记数据集的创建，有模型过拟合和泛化能力降低的风险。为了解决这些问题，我们提出了NVS-SQA，这是一种NSS质量评估方法，通过自我监督学习无参考质量表示，而不依赖于人类标签。传统的自监督学习主要依赖于“相同实例，相似表示”的假设和广泛的数据集。然而，鉴于这些条件不适用于NSS质量评估，我们采用启发式线索和质量分数作为学习目标，并采用专门的对比配对准备过程来提高学习的有效性和效率。结果表明，NVS-SQA在很大程度上优于17种无参考方法（即，在SRCC中平均为109.5%，在PLCC中为98.6%，在KRCC中为91.5%，排名第二），甚至在所有评估指标上超过了16种完全参考方法（例如，SRCC为22.9%，PLCC为19.1%，KRCC中排名第二的为18.6%）。 et.al.|[2501.06488](http://arxiv.org/abs/2501.06488)|**[link](https://github.com/vincentqqu/nvs-sqa)**|
|**2025-01-11**|**Aug3D: Augmenting large scale outdoor datasets for Generalizable Novel View Synthesis**|最近的真实感新视图合成（NVS）进展越来越受到人们的关注。然而，这些方法仍然局限于小型室内场景。虽然基于优化的NVS模型试图解决这个问题，但提供显著优势的通用前馈方法仍然没有得到充分的探索。在这项工作中，我们在大规模UrbanScene3D数据集上训练前馈NVS模型PixelNeRF。我们提出了四种训练策略来对这个数据集进行聚类和训练，强调了有限的视图重叠会阻碍性能。为了解决这个问题，我们引入了Aug3D，这是一种利用传统运动结构（SfM）重建场景的增强技术。Aug3D通过网格和语义采样生成条件良好的新视图，以增强前馈NVS模型学习。我们的实验表明，将每个集群的视图数量从20个减少到10个，PSNR提高了10%，但性能仍然不是最优的。Aug3D通过将新生成的新视图与原始数据集相结合，进一步解决了这一问题，证明了其在提高模型预测新视图的能力方面的有效性。 et.al.|[2501.06431](http://arxiv.org/abs/2501.06431)|null|
|**2025-01-09**|**Scaffold-SLAM: Structured 3D Gaussians for Simultaneous Localization and Photorealistic Mapping**|3D高斯散斑（3DGS）最近彻底改变了同步定位和映射（SLAM）中的新颖视图合成。然而，利用3DGS的现有SLAM方法未能同时为单眼、立体和RGB-D相机提供高质量的新颖视图渲染。值得注意的是，一些方法在RGB-D相机上表现良好，但在单眼相机的渲染质量方面却严重下降。在本文中，我们提出了脚手架SLAM，它可以在单目、立体和RGB-D相机上同时进行定位和高质量的真实感映射。我们引入了两项关键创新，以实现这种最先进的视觉质量。首先，我们提出了运动中的外观嵌入，使3D高斯模型能够更好地模拟不同相机姿态下的图像外观变化。其次，我们引入了一个频率正则化金字塔来引导高斯分布，使模型能够有效地捕捉场景中更精细的细节。对单眼、立体和RGB-D数据集的广泛实验表明，脚手架SLAM在真实感映射质量方面明显优于最先进的方法，例如，单眼相机的TUM RGB-D数据集中的PSNR高出16.76%。 et.al.|[2501.05242](http://arxiv.org/abs/2501.05242)|null|
|**2025-01-08**|**FatesGS: Fast and Accurate Sparse-View Surface Reconstruction using Gaussian Splatting with Depth-Feature Consistency**|最近，高斯散斑在计算机视觉领域引发了一种新的趋势。除了新颖的视图合成外，它还被扩展到多视图重建领域。最新的方法有助于完成详细的表面重建，同时确保快速的训练速度。然而，这些方法仍然需要密集的输入视图，并且它们的输出质量会随着稀疏视图的出现而显著降低。我们观察到高斯基元倾向于过拟合少数训练视图，导致有噪声的浮点运算和不完整的重建曲面。在本文中，我们提出了一种创新的稀疏视图重建框架，该框架利用视图内深度和多视图特征一致性来实现非常精确的表面重建。具体来说，我们利用单眼深度排名信息来监督斑块内深度分布的一致性，并采用平滑度损失来增强分布的连续性。为了实现更精细的表面重建，我们通过多视图投影特征优化了深度的绝对位置。在DTU和BlenedMVS上进行的大量实验表明，我们的方法优于最先进的方法，速度提高了60倍至200倍，实现了快速和细粒度的网格重建，而不需要昂贵的预训练。 et.al.|[2501.04628](http://arxiv.org/abs/2501.04628)|null|
|**2025-01-07**|**NeRFs are Mirror Detectors: Using Structural Similarity for Multi-View Mirror Scene Reconstruction with 3D Surface Primitives**|虽然神经辐射场（NeRF）在真实感新颖的视图合成方面取得了突破，但处理镜像表面仍然是一个特别的挑战，因为它们在场景表示中引入了严重的不一致性。之前的尝试要么侧重于重建单个反射物体，要么依赖于强有力的监督指导，即用户提供的镜子可见图像区域的额外注释，从而限制了实际可用性。相比之下，在本文中，我们提出了NeRF-MD，该方法表明NeRFs可以被视为镜像检测器，并且能够重建包含镜像表面的场景的神经辐射场，而不需要事先注释。为此，我们首先通过使用深度重投影损失训练标准NeRF来计算场景几何形状的初始估计。我们的关键见解在于，与镜像表面对应的场景部分仍将表现出明显的光度不一致，而其余部分已经以合理的方式重建。这使我们能够在训练的初始阶段通过将几何图元拟合到这种不一致的区域来检测镜面。利用这些信息，我们在第二个训练阶段联合优化辐射场和镜子几何形状，以提高其质量。我们展示了我们的方法能够忠实地检测场景中的镜子，并重建单个一致的场景表示，并展示了与基线和镜子感知方法相比的潜力。 et.al.|[2501.04074](http://arxiv.org/abs/2501.04074)|null|
|**2025-01-14**|**DehazeGS: Seeing Through Fog with 3D Gaussian Splatting**|当前的新颖视图合成任务主要依赖于高质量和清晰的图像。然而，在雾蒙蒙的场景中，散射和衰减会显著降低重建和渲染质量。尽管已经开发了基于NeRF的去方位重建算法，但它们使用深度全连接神经网络和每条射线采样策略会导致高昂的计算成本。此外，NeRF的隐含表现很难从朦胧的场景中恢复出精细的细节。相比之下，3D高斯散斑技术的最新进展通过将点云明确建模为3D高斯模型来实现高质量的3D场景重建。在本文中，我们提出利用显式高斯表示通过物理精确的正向渲染过程来解释雾状图像的形成过程。我们介绍了DehazeGS，这是一种能够从参与媒体中分解和渲染无雾背景的方法，仅使用多视图雾图像作为输入。我们对每个高斯分布内的传输进行建模，以模拟雾的形成。在此过程中，我们共同学习大气光和散射系数，同时优化模糊场景的高斯表示。在推理阶段，我们消除了散射和衰减对高斯分布的影响，并将其直接投影到二维平面上以获得清晰的视图。在合成和真实世界雾天数据集上的实验表明，DehazeGS在渲染质量和计算效率方面都达到了最先进的性能。 et.al.|[2501.03659](http://arxiv.org/abs/2501.03659)|null|
|**2025-01-06**|**Pointmap-Conditioned Diffusion for Consistent Novel View Synthesis**|在本文中，我们提出了PointmapDiffusion，这是一种利用预训练的2D扩散模型进行单图像新视图合成（NVS）的新框架。我们的方法是第一个利用点图（即光栅化的3D场景坐标）作为调节信号，从参考图像中捕获几何先验来指导扩散过程的方法。通过嵌入参考注意力块和点图特征的ControlNet，我们的模型在生成能力和几何一致性之间取得了平衡，实现了跨不同视点的精确视图合成。对不同真实世界数据集的广泛实验表明，与单图像NVS任务的其他基线相比，PointmapDiffusion以更少的可训练参数实现了高质量、多视图一致的结果。 et.al.|[2501.02913](http://arxiv.org/abs/2501.02913)|null|
|**2025-01-05**|**GS-DiT: Advancing Video Generation with Pseudo 4D Gaussian Fields through Efficient Dense 3D Point Tracking**|4D视频控制在视频生成中至关重要，因为它可以使用复杂的镜头技术，如多摄像头拍摄和推车变焦，而现有方法目前不支持这些技术。直接训练视频扩散变换器（DiT）来控制4D内容需要昂贵的多视图视频。受单目动态新颖视图合成（MDVS）的启发，该方法优化了4D表示并根据不同的4D元素（如相机姿态和对象运动编辑）渲染视频，我们将伪4D高斯场引入视频生成。具体来说，我们提出了一种新的框架，该框架构建了一个具有密集3D点跟踪的伪4D高斯场，并为所有视频帧渲染高斯场。然后，我们微调预训练的DiT，以在渲染视频的指导下生成视频，称为GS DiT。为了增强GS-DiT的训练，我们还提出了一种高效的密集3D点跟踪（D3D-PT）方法，用于伪4D高斯场构建。我们的D3D-PT在精度上优于最先进的稀疏3D点跟踪方法SpatialTracker，并将推理速度提高了两个数量级。在推理阶段，GS DiT可以生成具有相同动态内容的视频，同时遵循不同的相机参数，解决了当前视频生成模型的一个重大局限性。GS DiT展示了强大的泛化能力，并将高斯飞溅的4D可控性扩展到视频生成，而不仅仅是相机姿态。它通过操纵高斯场和相机内部函数来支持高级电影效果，使其成为创意视频制作的强大工具。演示可在https://wkbian.github.io/Projects/GS-DiT/. et.al.|[2501.02690](http://arxiv.org/abs/2501.02690)|null|

<p align=right>(<a href=#updated-on-20250115>back to top</a>)</p>

## 3D Reconstruction

|Publish Date|Title|Abstract|PDF|Code|
|---|---|---|---|---|
|**2025-01-13**|**3DGS-to-PC: Convert a 3D Gaussian Splatting Scene into a Dense Point Cloud or Mesh**|3D高斯散斑（3DGS）擅长生成高度详细的3D重建，但这些场景通常需要专门的渲染器才能进行有效的可视化。相比之下，点云是一种广泛使用的3D表示，与大多数流行的3D处理软件兼容，但将3DGS场景转换为点云是个复杂的挑战。在这项工作中，我们将3DGS引入PC，这是一个灵活且高度可定制的框架，能够将3DGS场景转换为密集、高精度的点云。我们将每个高斯分布的点作为3D密度函数进行概率采样。我们还使用到高斯中心的马氏距离来阈值化新点，以防止极端异常值。结果是一个点云，它非常接近编码到3D高斯场景中的形状。单个高斯人使用球面调和来根据视图调整颜色，每个点可能只会为最终渲染的场景提供微妙的颜色提示。为了避免与最终点云不匹配的虚假或不正确的颜色，我们通过定制的图像渲染方法重新计算高斯颜色，为每个高斯颜色分配其在所有视图中贡献最大的像素的颜色。3DGS到PC还支持通过泊松曲面重建生成网格，该重建应用于从预测的曲面高斯中采样的点。这允许从3DGS场景生成彩色网格，而无需重新训练。该软件包具有高度的可定制性，能够简单地集成到现有的3DGS管道中。3DGS to PC提供了一个强大的工具，用于将3DGS数据转换为基于点云和曲面的格式。 et.al.|[2501.07478](http://arxiv.org/abs/2501.07478)|**[link](https://github.com/lewis-stuart-11/3dgs-to-pc)**|
|**2025-01-13**|**PO-GVINS: Tightly Coupled GNSS-Visual-Inertial Integration with Pose-Only Representation**|准确可靠的定位对于自动驾驶、无人机和智能机器人中的感知、决策和其他高级应用至关重要。鉴于独立传感器的固有局限性，将具有互补功能的异构传感器集成是实现这一目标的最有效方法之一。本文提出了一种基于滤波的紧密耦合全球导航卫星系统（GNSS）-视觉惯性定位框架，该框架仅应用于视觉惯性系统（VINS），称为PO-GVINS。具体来说，当前VINS中使用的多视图成像需要先验的3D特征，然后联合估计相机姿态和3D特征位置，这不可避免地会引入特征的线性化误差以及面对维度爆炸。然而，仅姿态（PO）公式被证明与多视图成像等效，并已应用于视觉重建，它使用两个相机姿态表示特征深度，从而从状态向量中去除3D特征位置，避免了上述困难。受此启发，我们首先在VINS中应用PO配方，即PO-VINS。然后将GNSS原始测量值与解决的整周模糊度相结合，以实现准确和无漂移的估计。大量实验表明，所提出的PO-VINS明显优于多状态约束卡尔曼滤波器（MSCKF）。通过结合GNSS测量，PO-GVINS实现了准确、无漂移的状态估计，使其成为在具有挑战性的环境中进行定位的稳健解决方案。 et.al.|[2501.07259](http://arxiv.org/abs/2501.07259)|null|
|**2025-01-13**|**Representation Learning of Point Cloud Upsampling in Global and Local Inputs**|近年来，点云上采样在三维重建等领域得到了广泛的应用。我们的研究通过表示学习在全球和局部层面调查了影响点云上采样的因素。具体来说，本文将同一点云模型对象的全局和局部信息输入到两个编码器中，以提取这些特征，融合它们，然后将组合的特征馈送到上采样解码器中。目标是通过利用来自全局和局部输入的先验知识来解决点云中的稀疏性和噪声问题。所提出的框架可以应用于任何最先进的点云上采样神经网络。在一系列基于自动编码器的模型上进行了实验，利用深度学习，对全局和局部输入都产生了可解释性，结果证明，我们提出的框架可以进一步改善先前SOTA工作中的上采样效果。同时，显著性图反映了全局和局部特征输入之间的差异，以及同时使用这两种输入进行训练的有效性。 et.al.|[2501.07076](http://arxiv.org/abs/2501.07076)|null|
|**2025-01-13**|**SplatMAP: Online Dense Monocular SLAM with 3D Gaussian Splatting**|由于运动结构（SfM）和单眼SLAM等传统方法在准确捕捉场景细节方面的固有局限性，从单眼视频中实现高保真3D重建仍然具有挑战性。虽然神经辐射场（NeRF）等可微分渲染技术解决了其中一些挑战，但它们的高计算成本使其不适合实时应用。此外，现有的3D高斯散斑（3DGS）方法通常侧重于光度一致性，忽略了几何精度，并且未能利用SLAM的动态深度和姿态更新进行场景细化。我们提出了一种将密集SLAM与3DGS集成在一起的框架，用于实时、高保真的密集重建。我们的方法引入了SLAM知情自适应加密，通过利用SLAM的密集点云动态更新和加密高斯模型。此外，我们还引入了几何引导优化，该优化结合了边缘感知几何约束和光度一致性，共同优化3DGS场景表示的外观和几何，实现了详细准确的SLAM映射重建。在Replica和TUM-RGBD数据集上的实验证明了我们的方法的有效性，在单眼系统中取得了最先进的结果。具体来说，我们的方法在Replica上实现了36.864的PSNR、0.985的SSIM和0.040的LPIPS，分别比之前的SOTA提高了10.7%、6.4%和49.4%。在TUM-RGBD上，我们的方法在相同的指标上比最接近的基线高出10.2%、6.6%和34.7%。这些结果突显了我们的框架在弥合光度和几何密集3D场景表示之间的差距方面的潜力，为实用和高效的单眼密集重建铺平了道路。 et.al.|[2501.07015](http://arxiv.org/abs/2501.07015)|null|
|**2025-01-12**|**CULTURE3D: Cultural Landmarks and Terrain Dataset for 3D Applications**|在这篇论文中，我们使用从世界各地捕获的高分辨率图像，提出了一个大规模的细粒度数据集。与现有数据集相比，我们的数据集提供了更大的大小，并包含了更高级别的细节，使其特别适合细粒度的3D应用程序。值得注意的是，我们的数据集是使用无人机捕获的航空图像构建的，这为捕获真实世界的场地布局和建筑结构提供了更准确的视角。通过使用这些详细的图像重建环境，我们的数据集支持高斯散斑的COLMAP格式和运动结构（SfM）方法等应用。它与广泛使用的技术兼容，包括SLAM、多视图立体和神经辐射场（NeRF），可实现精确的3D重建和点云。这使其成为重建和分割任务的基准。该数据集能够与多模态数据无缝集成，支持从建筑重建到虚拟旅游的一系列3D应用。它的灵活性促进了创新，促进了3D建模和分析的突破。 et.al.|[2501.06927](http://arxiv.org/abs/2501.06927)|null|
|**2025-01-10**|**MEt3R: Measuring Multi-View Consistency in Generated Images**|我们引入了MEt3R，这是一种用于生成图像中多视图一致性的度量。用于多视图图像生成的大规模生成模型正在迅速推进稀疏观测的3D推理领域。然而，由于生成建模的性质，传统的重建度量不适合衡量生成输出的质量，迫切需要独立于采样过程的度量。在这项工作中，我们专门解决了生成的多视图图像之间的一致性问题，这些图像可以独立于特定场景进行评估。我们的方法使用DUSt3R以前馈方式从图像对中获得密集的3D重建，这些重建用于将图像内容从一个视图扭曲到另一个视图。然后，比较这些图像的特征图，以获得对视图相关效果不变的相似性得分。使用MEt3R，我们评估了大量先前新视图和视频生成方法的一致性，包括我们的开放式多视图潜在扩散模型。 et.al.|[2501.06336](http://arxiv.org/abs/2501.06336)|null|
|**2025-01-09**|**Identifiability of Controlled Open Quantum Systems**|开放量子系统是量子力学和随机分析交叉领域的一个丰富研究领域。我们在双线性动力系统的框架内统一了受控开放量子系统的多种观点。我们从量子态层析成像的结果中定义了相应的可识别性概念，该结果是在不同长度控制信号的子序列下，在初始量子态的许多副本中获得的。我们解释并扩展了使用谱准则、基于Hankel矩阵的准则和频域准则对双线性系统可识别性的研究，并将其扩展到开放量子系统主方程的参数估计。这为识别开放量子系统的一些建设性方法奠定了基础。 et.al.|[2501.05270](http://arxiv.org/abs/2501.05270)|null|
|**2025-01-09**|**A Systematic Literature Review on Deep Learning-based Depth Estimation in Computer Vision**|深度估计（DE）提供关于场景的空间信息，并实现诸如3D重建、对象检测和场景理解等任务。最近，人们对使用基于深度学习（DL）的方法进行DE的兴趣越来越大。传统技术依赖于手工制作的特征，这些特征往往难以推广到不同的场景，需要大量的手动调整。然而，DE的DL模型可以从输入数据中自动提取相关特征，适应各种场景条件，并很好地泛化到看不见的环境。已经开发了许多基于DL的方法，因此有必要调查和综合最新技术（SOTA）。之前关于DE的综述主要集中在单眼或基于立体的技术上，而不是全面综述DE。此外，据我们所知，还没有全面关注DE的系统文献综述（SLR）。因此，正在进行这项SLR研究。最初，在电子数据库中搜索相关出版物，得到1284份出版物。使用定义的排除和质量标准，筛选出128篇出版物，并进一步筛选出59篇高质量的初步研究。对这些研究进行分析，以提取数据并回答定义的研究问题。基于这些结果，DL方法主要针对三种不同类型的DE：单眼、立体和多视图。20个公开可用的数据集用于训练、测试和评估DE的DL模型，其中KITTI、NYU Depth V2和Make 3D是使用最多的数据集。使用29个评估指标来评估DE的性能。初步研究中报告了35个基础模型，使用最多的前五个基础模型是ResNet-50、ResNet-18、ResNet-101、U-Net和VGG-16。最后，缺乏地面实况数据是主要研究报告的最重大挑战之一。 et.al.|[2501.05147](http://arxiv.org/abs/2501.05147)|null|
|**2025-01-07**|**Materialist: Physically Based Editing Using Single-Image Inverse Rendering**|为了基于单视图、基于逆物理的渲染进行图像编辑，我们提出了一种将基于学习的方法与渐进可微渲染相结合的方法。对于给定的图像，我们的方法利用神经网络来预测初始材料属性。然后，使用渐进可微渲染来优化环境贴图并细化材质属性，目标是使渲染结果与输入图像紧密匹配。我们只需要一张图像，而基于渲染方程的其他逆渲染方法需要多个视图。与依赖神经渲染器的单视图方法相比，我们的方法实现了更逼真的光与材质交互、精确的阴影和全局照明。此外，通过优化材质属性和照明，我们的方法可以执行各种任务，包括基于物理的材质编辑、对象插入和重新照明。我们还提出了一种材质透明度编辑方法，该方法无需全场景几何即可有效操作。与基于稳定扩散的方法相比，我们的方法基于经验结果提供了更强的可解释性和更真实的光折射。 et.al.|[2501.03717](http://arxiv.org/abs/2501.03717)|**[link](https://github.com/lez-s/materialist)**|
|**2025-01-07**|**ConcealGS: Concealing Invisible Copyright Information in 3D Gaussian Splatting**|随着三维重建技术的快速发展，三维数据的广泛分布已成为未来的趋势。虽然传统的视觉数据（如图像和视频）和基于NeRF的格式已经有了成熟的版权保护技术，但新兴的3D高斯散斑（3D-GS）格式的隐写技术尚未得到充分探索。为了解决这个问题，我们提出了ConcealGS，这是一种将隐式信息嵌入3D-GS的创新方法。通过引入基于3D-GS的知识蒸馏和梯度优化策略，ConcealGS克服了基于NeRF的模型的局限性，提高了隐式信息的鲁棒性和3D重建的质量。我们在各种潜在的应用场景中评估了ConcealGS，实验结果表明，ConcealGS不仅成功地恢复了隐式信息，而且对渲染质量几乎没有影响，为未来将不可见和可恢复的信息嵌入3D模型提供了一种新方法。 et.al.|[2501.03605](http://arxiv.org/abs/2501.03605)|**[link](https://github.com/zxk1212/concealgs)**|

<p align=right>(<a href=#updated-on-20250115>back to top</a>)</p>

## Diffusion

|Publish Date|Title|Abstract|PDF|Code|
|---|---|---|---|---|
|**2025-01-13**|**Training-Free Motion-Guided Video Generation with Enhanced Temporal Consistency Using Motion Consistency Loss**|在这篇论文中，我们解决了使用运动引导生成时间一致视频的挑战。虽然许多现有方法依赖于额外的控制模块或推理时间微调，但最近的研究表明，在不改变模型架构或需要额外训练的情况下，可以实现有效的运动制导。这种方法与各种视频生成基础模型具有很好的兼容性。然而，现有的无训练方法往往难以在帧之间保持一致的时间连贯性，或准确地跟随引导的运动。在这项工作中，我们提出了一种简单而有效的解决方案，将基于噪声的初始方法与新的运动一致性损失相结合，后者是我们的关键创新。具体来说，我们从视频扩散模型中捕获中间特征的帧间特征相关模式，以表示参考视频的运动模式。然后，我们设计了一个运动一致性损失，以在生成的视频中保持相似的特征相关模式，利用该损失在潜在空间中的梯度来指导生成过程，以实现精确的运动控制。这种方法提高了各种运动控制任务的时间一致性，同时保留了无训练设置的好处。大量实验表明，我们的方法为高效、时间相干的视频生成设定了新的标准。 et.al.|[2501.07563](http://arxiv.org/abs/2501.07563)|null|
|**2025-01-13**|**Confident Pseudo-labeled Diffusion Augmentation for Canine Cardiomegaly Detection**|犬心脏肥大，以心脏增大为特征，如果不被发现，会带来严重的健康风险，需要准确的诊断方法。当前的检测模型通常依赖于小的、注释不佳的数据集，并且难以在不同的成像条件下进行泛化，限制了它们在现实世界中的适用性。为了解决这些问题，我们提出了一种用于识别犬心脏肥大的自信伪标记扩散增强（CDA）模型。我们的方法通过使用扩散模型生成合成X射线图像并注释椎体心脏评分关键点，从而扩展数据集，解决了高质量训练数据有限的挑战。我们还采用蒙特卡洛Dropout的伪标签策略来选择高置信度标签，优化合成数据集，并提高准确性。迭代合并这些标签可以提高模型的性能，克服现有方法的局限性。实验结果表明，CDA模型优于传统方法，在犬心脏肥大检测中达到了最先进的准确性。代码实现可在以下网址获得https://github.com/Shira7z/CDA. et.al.|[2501.07533](http://arxiv.org/abs/2501.07533)|**[link](https://github.com/shira7z/cda)**|
|**2025-01-13**|**IP-FaceDiff: Identity-Preserving Facial Video Editing with Diffusion**|面部视频编辑对于内容创作者来说变得越来越重要，可以操纵面部表情和属性。然而，现有的模型面临着编辑质量差、计算成本高以及在各种编辑中难以保持面部身份等挑战。此外，这些模型通常仅限于编辑预定义的面部属性，这限制了它们对不同编辑提示的灵活性。为了应对这些挑战，我们提出了一种新的面部视频编辑框架，该框架利用预训练的文本到图像（T2I）扩散模型的丰富潜在空间，并专门针对面部视频编辑任务对其进行微调。我们的方法引入了一种有针对性的微调方案，可以实现高质量、本地化、文本驱动的编辑，同时确保跨视频帧的身份保留。此外，通过在推理过程中使用预训练的T2I模型，我们的方法显著减少了80%的编辑时间，同时保持了整个视频序列的时间一致性。我们通过在各种具有挑战性的场景中进行广泛的测试来评估我们方法的有效性，包括不同的头部姿势、复杂的动作序列和不同的面部表情。我们的方法始终优于现有技术，在广泛的指标和基准测试中表现出卓越的性能。 et.al.|[2501.07530](http://arxiv.org/abs/2501.07530)|null|
|**2025-01-13**|**PrecipDiff: Leveraging image diffusion models to enhance satellite-based precipitation observations**|世界气象组织（WMO）最近的一份报告强调，在过去50年里，与水有关的灾害在自然灾害中造成了最高的人员损失，超过91%的死亡发生在低收入国家。这种差异主要是由于缺乏足够的地面监测站，如安装成本高昂的天气监视雷达（WSR）。例如，虽然美国和欧洲加起来拥有600多个WSR，但非洲尽管拥有近1.5倍的陆地面积，却不到40个。为了解决这个问题，基于卫星的观测提供了一种全球性的、近乎实时的监测解决方案。然而，它们面临着一些挑战，如准确性、偏差和低空间分辨率。本研究利用扩散模型和残差学习的力量，在统一的框架内解决这些局限性。我们介绍了第一个用于纠正不同降水产品之间不一致的扩散模型。我们的方法证明了将卫星降水估计从10公里分辨率缩小到1公里分辨率的有效性。在西雅图地区进行的大量实验表明，在准确性、偏差减少和空间细节方面有了显著提高。重要的是，我们的方法仅使用降水数据就实现了这些结果，展示了纯计算机视觉方法在增强卫星降水产品方面的潜力，并为该领域的进一步发展铺平了道路。 et.al.|[2501.07447](http://arxiv.org/abs/2501.07447)|null|
|**2025-01-13**|**Diff-Ensembler: Learning to Ensemble 2D Diffusion Models for Volume-to-Volume Medical Image Translation**|尽管在医学图像的体积到体积转换方面取得了成功，但大多数现有模型都难以使用3D表示有效地捕捉固有的体积分布。当前最先进的方法通过加权平均将多个基于2D的网络组合在一起，从而忽略了3D空间结构。由于高计算需求和对大规模数据集的需求，在医学成像中直接训练3D模型面临着重大挑战。为了应对这些挑战，我们引入了Diff Ensembler，这是一种新型的混合2D-3D模型，通过在每个扩散步骤中将垂直训练的2D扩散模型与3D网络集成，实现高效和有效的体积平移。此外，我们的模型自然可以用于集成基于不同模态的扩散模型，从而灵活准确地融合输入条件。大量实验表明，Diff Ensembler在3D医学图像超分辨率和模态转换方面具有卓越的精度和体积真实感。我们使用肿瘤分割作为下游任务，进一步证明了我们模型的体积真实性的强度。 et.al.|[2501.07430](http://arxiv.org/abs/2501.07430)|null|
|**2025-01-13**|**OCORD: Open-Campus Object Removal Dataset**|生成模型的快速发展，特别是基于扩散的技术，通过生成高保真度和多样化的内容，彻底改变了图像修复任务。然而，作为修复的一个特定子集，对象移除仍然没有得到充分的探索，面临着语义理解不足和意外生成工件等挑战。用于对象删除的现有数据集通常依赖于合成数据，这与现实世界的场景不符，限制了模型性能。尽管一些现实世界的数据集部分地解决了这些问题，但它们存在可扩展性、注释效率低下以及光照和阴影等物理现象的真实性有限等问题。为了解决这些局限性，本文介绍了一种新的对象去除方法，通过固定相机设置的长时间视频捕获构建高分辨率的真实世界数据集。利用Grounding DINO、Segment Anything Model和MASA等高级工具进行自动注释，我们提供图像、背景和掩模对，同时显著减少注释时间和工作量。通过我们高效的注释管道，我们发布了第一个完全开放、高分辨率的真实世界数据集用于对象移除，并通过微调预训练的扩散模型提高了对象移除任务的性能。 et.al.|[2501.07397](http://arxiv.org/abs/2501.07397)|null|
|**2025-01-13**|**Bigger Isn't Always Better: Towards a General Prior for Medical Image Reconstruction**|扩散模型已成功应用于许多逆问题，包括MRI和CT重建。研究人员通常会重新使用最初为无条件采样而设计的模型，而不进行修改。使用两种不同的后验采样算法，我们经验地表明，这样大的网络是不必要的。我们最小的模型，实际上是一个ResNet，在分布重建中的表现几乎与注意力U-Net一样好，同时对分布变化的鲁棒性要高得多。此外，我们介绍了在自然图像上训练的模型，并证明了它们可以用于MRI和CT重建，在分布不均的情况下，其性能优于在医学图像上训练过的模型。根据我们的研究结果，我们强烈建议不要简单地重复使用非常大的网络，并鼓励研究人员根据各自的任务调整模型的复杂性。此外，我们认为，实现基于一般扩散的先验的关键一步是对自然图像进行训练。 et.al.|[2501.07376](http://arxiv.org/abs/2501.07376)|null|
|**2025-01-13**|**A multi-wavelength view of the isolated neutron star eRASSU J065715.3+260428**|在SRG/eROSITA全天巡天的搜索中，X射线源eRASSU J065715.3+260428被确定为一颗可能热发射的孤立中子星。我们通过使用XMM-Newton、NICER、FAST和ESO-VLT进行专门的多波长后续活动，并辅以对档案费米LAT观测的分析，研究了源的性质和演化状态。X射线观测揭示了源的旋转周期，P=261.085400（4） $ms，以及自旋下降率，P=6^{+11}_{-4}\times10^{-15}$s^{-1}$。在27.3 mag（5\sigma$，R波段）以下没有检测到光学对应物，这意味着X射线与光通量之比超过5200。源的X射线光谱最好由一个由两个热分量组成的复合现象学模型来描述，这两个热成分要么是温度为90 eV和220 eV的双黑体连续体，要么是温度$\log（T/\mathrm{K}）\sim 5.8$的氢中子星大气，再加上250 eV的热黑体，在这两种情况下都通过低能（$\sim0.3$keV）的吸收特征进行了修改。在源未吸收通量的$（2.1\pm1.8）$ %以上，排除了微弱的非热硬X射线尾的存在。使用FAST在1-1.5美元GHz的频率下进行无线电搜索，结果为阴性，脉冲通量的上限为1.4美元（10美元）。同样，在16年的费米LAT观测中没有检测到明显的空间或脉冲信号。该源极有可能是一颗中年自旋驱动的脉冲星，也可以确定为PSR J0657+2604。在当前限制范围内没有非热X射线、无线电或伽马射线发射，这表明要么是不利的观测几何形状，要么是异常的磁层特性。需要额外的观测来检查微弱的硬X射线尾部，调查脉冲星风星云是否存在漫发射，并获得更准确的采样时间解。 et.al.|[2501.07347](http://arxiv.org/abs/2501.07347)|null|
|**2025-01-13**|**Community Aware Temporal Network Generation**|时间网络在捕捉复杂动态（如扩散和传染）方面的优势，导致了现实世界系统在众多领域的突破。就人类行为而言，面对面的互动网络使我们能够了解社区如何通过互动及时出现和演变的动态，这在流行病、社会学研究和城市科学等领域至关重要。然而，最先进的数据集存在许多缺点，例如数据收集的时间跨度短，参与者人数少。此外，参与者的隐私和数据收集成本也引起了人们的担忧。在过去的几年里，已经提出了许多成功的静态网络生成算法，但它们往往没有解决交互的社会结构或时间方面的问题。在这项工作中，我们扩展了最近的网络生成方法，以捕捉不同社区之间互动的演变。我们的方法根据节点的社区隶属关系对节点进行标签，并构建代理网络，以反映具有不同标签的节点之间原始时间网络的交互。这使得能够生成复制现实行为的合成网络。我们通过比较多个面对面交互数据集中原始网络和生成网络之间的结构度量来验证我们的方法。 et.al.|[2501.07327](http://arxiv.org/abs/2501.07327)|null|
|**2025-01-13**|**Skip Mamba Diffusion for Monocular 3D Semantic Scene Completion**|3D语义场景完成对于自主系统中的多个下游任务至关重要。它估计所获取的场景数据中缺失的几何和语义信息。由于现实世界条件具有挑战性，这项任务通常需要复杂的模型来处理多模态数据，以实现可接受的性能。我们提出了一种独特的神经模型，利用状态空间和扩散生成建模的进步，在单眼图像输入下实现了卓越的3D语义场景完成性能。我们的技术在变分自编码器的条件潜在空间中处理数据，其中使用创新的状态空间技术进行扩散建模。我们神经网络的一个关键组成部分是所提出的Skinba（Skip-Mamba）去噪器，它擅长高效处理长序列数据。Skinba扩散模型是我们3D场景完成网络不可或缺的一部分，它结合了三重Mamba结构、维度分解残差和沿三个方向的不同膨胀。我们还将该网络的变体用于我们方法的后续语义分割阶段。对标准SemanticKITTI和SSCBench-KITTI360数据集的广泛评估表明，我们的方法不仅在很大程度上优于其他单目技术，而且在与立体方法的比较中也取得了有竞争力的性能。该代码可在以下网址获得https://github.com/xrkong/skimba et.al.|[2501.07260](http://arxiv.org/abs/2501.07260)|**[link](https://github.com/xrkong/skimba)**|

<p align=right>(<a href=#updated-on-20250115>back to top</a>)</p>

## NeRF

|Publish Date|Title|Abstract|PDF|Code|
|---|---|---|---|---|
|**2025-01-10**|**Nonlinear partial differential equations in neuroscience: from modelling to mathematical theory**|许多偏微分方程组已被提出作为大型神经元网络中复杂集体行为的简化表示。在这项调查中，我们简要讨论了它们的推导，然后回顾了为处理这些模型的独特特征而开发的数学方法，这些模型通常是非线性和非局部的。第一部分重点介绍抛物型福克-普朗克方程：非线性噪声泄漏积分和火神经元模型，PDE形式的随机神经场及其在网格单元中的应用，以及基于速率的决策模型。第二部分涉及双曲线输运方程，即自上次排放以来经过的时间模型和基于跳跃的泄漏积分和火灾模型。最后一部分介绍了一些动力学介观模型，特别关注动力学电压电导模型和FitzHugh-Nagumo动力学福克-普朗克系统。 et.al.|[2501.06015](http://arxiv.org/abs/2501.06015)|null|
|**2025-01-10**|**Locality-aware Gaussian Compression for Fast and High-quality Rendering**|我们提出了LocoGS，这是一种局部感知的3D高斯散斑（3DGS）框架，它利用3D高斯的空间相干性对体积场景进行紧凑建模。为此，我们首先分析了3D高斯属性的局部相干性，并提出了一种新的局部感知3D高斯表示，该表示使用具有最小存储要求的神经场表示对局部相干高斯属性进行有效编码。除了新颖的表示方法外，LocoGS还经过精心设计，添加了密集初始化、自适应球面谐波带宽方案和针对不同高斯属性的不同编码方案等附加组件，以最大限度地提高压缩性能。实验结果表明，对于代表性的真实世界3D数据集，我们的方法优于现有的紧凑高斯表示的渲染质量，同时实现了从54.6美元到96.6美元的压缩存储大小，以及从2.1美元到2.4美元的渲染速度。甚至我们的方法也证明了平均渲染速度比最先进的压缩方法高2.4倍，具有相当的压缩性能。 et.al.|[2501.05757](http://arxiv.org/abs/2501.05757)|null|
|**2025-01-08**|**KN-LIO: Geometric Kinematics and Neural Field Coupled LiDAR-Inertial Odometry**|激光雷达惯性测距（LIO）的最新进展推动了大量应用。然而，传统的LIO系统往往更侧重于定位而不是映射，映射主要由稀疏的几何元素组成，这对于下游任务来说并不理想。最近新兴的神经场技术在密集测绘方面具有巨大的潜力，但纯激光雷达测绘很难在高动态车辆上进行。为了缓解这一挑战，我们提出了一种新的解决方案，将几何运动学与神经场紧密耦合，以增强同时状态估计和密集映射能力。我们提出了半耦合和紧耦合的运动学神经LIO（KN-LIO）系统，该系统利用在线SDF解码和迭代误差状态卡尔曼滤波来融合激光和惯性数据。我们的KN-LIO最大限度地减少了信息丢失，提高了状态估计的准确性，同时也适应了异步多LiDAR输入。对各种高动态数据集的评估表明，我们的KN-LIO在姿态估计方面的性能与现有最先进的解决方案相当或更优，并且与纯基于LiDAR的方法相比，提供了更高的密集映射精度。相关代码和数据集将在https://**上提供。 et.al.|[2501.04263](http://arxiv.org/abs/2501.04263)|null|
|**2025-01-06**|**NeuroPMD: Neural Fields for Density Estimation on Product Manifolds**|我们提出了一种新的深度神经网络方法，用于在乘积黎曼流形域上进行密度估计。在我们的方法中，网络直接参数化未知密度函数，并使用惩罚最大似然框架进行训练，惩罚项使用流形微分算子形成。网络架构和估计算法经过精心设计，以应对高维积流形域的挑战，有效地减轻了限制传统核和基展开估计器的维数灾难，并克服了非专用神经网络方法遇到的收敛问题。广泛的模拟和对大脑结构连接数据的实际应用突显了我们的方法相对于竞争对手的明显优势。 et.al.|[2501.02994](http://arxiv.org/abs/2501.02994)|**[link](https://github.com/will-consagra/neuropmd)**|
|**2025-01-03**|**Fusion DeepONet: A Data-Efficient Neural Operator for Geometry-Dependent Hypersonic Flows on Arbitrary Grids**|设计再入飞行器需要准确预测其几何形状周围的高超音速流动。对这种流动的快速预测可以彻底改变车辆设计，特别是对于变形几何形状。我们评估了先进的神经算子模型，如深度算子网络（DeepONet）、参数条件U-Net、傅里叶神经算子（FNO）和MeshGraphNet，目的是解决在有限数据下学习依赖几何的高超音速流场的挑战。具体来说，我们比较了两种网格类型的这些模型的性能：均匀笛卡尔网格和不规则网格。为了训练这些模型，我们使用36个独特的椭圆几何体，使用高阶熵稳定的DGSEM求解器生成高保真模拟，强调了使用稀缺数据集的挑战。我们评估并比较了四种基于算子的模型在预测椭圆体周围高超音速流场方面的有效性。此外，我们开发了一个名为Fusion DeepONet的新框架，该框架利用了神经场概念，并在不同的几何结构中有效地进行了推广。尽管训练数据稀缺，Fusion DeepONet在均匀网格上的性能与参数条件U-Net相当，而在不规则、任意网格上的表现优于MeshGraphNet和vanilla DeepONnet。与U-Net、MeshGraphNet和FNO相比，Fusion DeepONet需要更少的可训练参数，使其计算效率更高。我们还使用奇异值分解分析了Fusion DeepONet模型的基函数。该分析表明，Fusion DeepONet能够有效地推广到看不见的解决方案，并适应不同的几何形状和网格点，证明了其在训练数据有限的情况下的鲁棒性。 et.al.|[2501.01934](http://arxiv.org/abs/2501.01934)|null|
|**2024-12-30**|**Hierarchical Pose Estimation and Mapping with Multi-Scale Neural Feature Fields**|机器人应用需要对场景有全面的了解。近年来，基于神经场的参数化整个环境的方法已经变得流行。由于其连续性和学习场景先验的能力，这些方法很有前景。然而，当处理未知的传感器姿态和连续测量时，在机器人中使用神经场变得具有挑战性。本文主要研究大规模神经隐式SLAM的传感器姿态估计问题。我们从概率的角度研究了隐式映射，并提出了具有相应神经网络架构的分层姿态估计。我们的方法非常适合大规模隐式映射表示。所提出的方法在连续的室外LiDAR扫描上运行，实现了精确的姿态估计，同时保持了短轨迹和长轨迹的稳定映射质量。我们在适合大规模重建的结构化稀疏隐式表示上构建了我们的方法，并使用KITTI和MaiCity数据集对其进行了评估。我们的方法在未知姿态的映射方面优于基线，并实现了最先进的定位精度。 et.al.|[2412.20976](http://arxiv.org/abs/2412.20976)|null|
|**2024-12-26**|**Humans as a Calibration Pattern: Dynamic 3D Scene Reconstruction from Unsynchronized and Uncalibrated Videos**|最近关于动态神经场重建的工作假设输入来自具有已知姿势的同步多视图视频。这些输入约束在现实世界的设置中经常得不到满足，使得这种方法不切实际。我们证明，如果视频捕捉到人体运动，则姿态未知的非同步视频可以生成动态神经场。人类是最常见的动态主体之一，其姿势可以使用最先进的方法进行估计。在有噪声的情况下，估计的人体形状和姿态参数为训练一致的动态神经表示的高度非凸和欠约束问题提供了一个不错的初始化。给定人类的姿势和形状序列，我们估计视频之间的时间偏移，然后通过分析3D关节位置进行相机姿势估计。然后，我们使用多分辨率脊训练动态NeRF，同时细化时间偏移和相机姿态。该设置仍然涉及优化许多参数，因此，我们引入了一种鲁棒的渐进学习策略来稳定该过程。实验表明，我们的方法在具有挑战性的条件下实现了精确的时空校准和高质量的场景重建。 et.al.|[2412.19089](http://arxiv.org/abs/2412.19089)|null|
|**2024-12-29**|**PartGen: Part-level 3D Generation and Reconstruction with Multi-View Diffusion Models**|文本或图像到3D生成器和3D扫描仪现在可以生成具有高质量形状和纹理的3D资产。这些资产通常由一个单一的融合表示组成，如隐式神经场、高斯混合或网格，没有任何有用的结构。然而，大多数应用程序和创意工作流程都要求资产由几个可以独立操作的有意义的部分组成。为了解决这一差距，我们引入了PartGen，这是一种新颖的方法，可以从文本、图像或非结构化3D对象生成由有意义的部分组成的3D对象。首先，给定生成或渲染的3D对象的多个视图，多视图扩散模型提取一组合理且视图一致的零件分割，将对象划分为零件。然后，第二个多视图扩散模型分别获取每个部分，填充遮挡，并通过将这些完成的视图馈送到3D重建网络来使用它们进行3D重建。这个完成过程考虑了整个对象的上下文，以确保各部分紧密结合。生成完成模型可以弥补因遮挡而丢失的信息；在极端情况下，它可以根据输入的3D资源产生完全不可见的部分的幻觉。我们在生成的和真实的3D资产上评估了我们的方法，并表明它在很大程度上优于分割和零件提取基线。我们还展示了3D零件编辑等下游应用程序。 et.al.|[2412.18608](http://arxiv.org/abs/2412.18608)|null|
|**2025-01-04**|**S-INF: Towards Realistic Indoor Scene Synthesis via Scene Implicit Neural Field**|基于学习的方法在3D室内场景合成（ISS）中越来越受欢迎，显示出优于传统基于优化的方法的性能。这些基于学习的方法通常使用生成模型在简单但明确的场景表示上对分布进行建模。然而，由于过于简单的显式表示忽略了详细信息，并且缺乏场景内多模态关系的指导，大多数基于学习的方法都难以生成具有逼真对象排列和风格的室内场景。本文介绍了一种新的室内场景合成方法——场景隐式神经场（S-INF），旨在学习多模态关系的有意义表示，以提高室内场景合成的真实感。S-INF假设场景布局通常与对象详细信息有关。它将多模态关系分解为场景布局关系和详细对象关系，然后通过隐式神经场（INF）将它们融合在一起。通过学习专门的场景布局关系并将其投影到S-INF中，我们实现了场景布局的真实生成。此外，S-INF通过可微分渲染捕获密集而详细的对象关系，确保对象之间的风格一致性。通过在基准3D-FRONT数据集上的广泛实验，我们证明了我们的方法在不同类型的ISS下始终达到最先进的性能。 et.al.|[2412.17561](http://arxiv.org/abs/2412.17561)|**[link](https://github.com/zixiliang/s-inf)**|
|**2024-12-22**|**HyperNet Fields: Efficiently Training Hypernetworks without Ground Truth by Learning Weight Trajectories**|为了有效地适应大型模型或训练神经表示的生成模型，超网络引起了人们的兴趣。虽然超级网络工作良好，但训练它们很麻烦，而且通常需要为每个样本进行地面实况优化的权重。然而，获得这些权重中的每一个都是一个需要训练的训练问题，例如，适应权重，甚至是超网络回归的整个神经场。在这项工作中，我们提出了一种训练超网络的方法，而不需要任何每个样本的地面真实值。我们的关键思想是学习一个超网络“场”，并估计网络权重训练的整个轨迹，而不是简单地估计其收敛状态。换句话说，我们向超网络引入了一个额外的输入，即收敛状态，这使它成为一个神经场，对任务网络的整个收敛路径进行建模。这样做的一个关键好处是，在任何收敛状态下，估计权重的梯度都必须与原始任务的梯度相匹配——仅此约束就足以训练超网络场。我们通过个性化图像生成和从图像和点云进行3D形状重建的任务来证明我们的方法的有效性，在没有任何样本地面真实性的情况下展示了具有竞争力的结果。 et.al.|[2412.17040](http://arxiv.org/abs/2412.17040)|null|

<p align=right>(<a href=#updated-on-20250115>back to top</a>)</p>

[contributors-shield]: https://img.shields.io/github/contributors/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[contributors-url]: https://github.com/Vincentqyw/cv-arxiv-daily/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[forks-url]: https://github.com/Vincentqyw/cv-arxiv-daily/network/members
[stars-shield]: https://img.shields.io/github/stars/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[stars-url]: https://github.com/Vincentqyw/cv-arxiv-daily/stargazers
[issues-shield]: https://img.shields.io/github/issues/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[issues-url]: https://github.com/Vincentqyw/cv-arxiv-daily/issues

