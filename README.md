[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]

## Updated on 2025.01.16
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
|**2025-01-13**|**Motion Tracks: A Unified Representation for Human-Robot Transfer in Few-Shot Imitation Learning**|教机器人自主完成日常任务仍然是一个挑战。模仿学习（IL）是一种强大的方法，通过演示向机器人灌输技能，但受到收集远程操作机器人数据的劳动密集型过程的限制。人类视频提供了一种可扩展的替代方案，但由于缺乏机器人动作标签，仍然很难直接从中训练IL策略。为了解决这个问题，我们建议将动作表示为图像上的短程2D轨迹。这些动作或运动轨迹捕捉人手或机器人末端执行器的预测运动方向。我们实例化了一个名为运动轨迹策略（MT-pi）的IL策略，该策略接收图像观测值并将运动轨迹作为动作输出。通过利用这种统一的跨实施例动作空间，MT-pi在只需几分钟的人类视频和有限的额外机器人演示的情况下，就可以成功完成任务。在测试时，我们从两个相机视图预测运动轨迹，通过多视图合成恢复6DoF轨迹。MT pi在4个真实世界的任务中实现了86.5%的平均成功率，超过了不利用人类数据或我们的动作空间的最先进的IL基线40%，并推广到仅在人类视频中看到的场景。代码和视频可在我们的网站上找到https://portal-cornell.github.io/motion_track_policy/. et.al.|[2501.06994](http://arxiv.org/abs/2501.06994)|null|
|**2025-01-11**|**MapGS: Generalizable Pretraining and Data Augmentation for Online Mapping via Novel View Synthesis**|在线地图减少了自动驾驶汽车对高清地图的依赖，显著提高了可扩展性。然而，最近的进展往往忽视了跨传感器配置的通用性，导致当模型部署在具有不同摄像头内部和外部的车辆上时，性能下降。随着新型视图合成方法的快速发展，我们研究了这些技术在多大程度上可以用来解决传感器配置泛化挑战。我们提出了一种新的框架，利用高斯飞溅来重建场景，并在目标传感器配置中渲染相机图像。目标配置传感器数据以及映射到目标配置的标签用于训练在线映射模型。我们在nuScenes和Argoverse 2数据集上提出的框架通过有效的数据集增强实现了18%的性能提升，实现了更快的收敛和高效的训练，并且在仅使用25%的原始训练数据时超过了最先进的性能。这实现了数据重用，并减少了对繁琐的数据标记的需求。项目页面位于https://henryzhangzhy.github.io/mapgs. et.al.|[2501.06660](http://arxiv.org/abs/2501.06660)|null|
|**2025-01-11**|**NVS-SQA: Exploring Self-Supervised Quality Representation Learning for Neurally Synthesized Scenes without References**|神经视图合成（NVS），如NeRF和3D高斯散斑，有效地从稀疏视点创建逼真的场景，通常通过PSNR、SSIM和LPIPS等质量评估方法进行评估。然而，这些将合成视图与参考视图进行比较的完整参考方法可能无法完全捕捉神经合成场景（NSS）的感知质量，特别是由于密集参考视图的可用性有限。此外，获取人类感知标签的挑战阻碍了广泛标记数据集的创建，有模型过拟合和泛化能力降低的风险。为了解决这些问题，我们提出了NVS-SQA，这是一种NSS质量评估方法，通过自我监督学习无参考质量表示，而不依赖于人类标签。传统的自监督学习主要依赖于“相同实例，相似表示”的假设和广泛的数据集。然而，鉴于这些条件不适用于NSS质量评估，我们采用启发式线索和质量分数作为学习目标，并采用专门的对比配对准备过程来提高学习的有效性和效率。结果表明，NVS-SQA在很大程度上优于17种无参考方法（即，在SRCC中平均为109.5%，在PLCC中为98.6%，在KRCC中为91.5%，排名第二），甚至在所有评估指标上超过了16种完全参考方法（例如，SRCC为22.9%，PLCC为19.1%，KRCC中排名第二的为18.6%）。 et.al.|[2501.06488](http://arxiv.org/abs/2501.06488)|**[link](https://github.com/vincentqqu/nvs-sqa)**|
|**2025-01-11**|**Aug3D: Augmenting large scale outdoor datasets for Generalizable Novel View Synthesis**|最近的真实感新视图合成（NVS）进展越来越受到人们的关注。然而，这些方法仍然局限于小型室内场景。虽然基于优化的NVS模型试图解决这个问题，但提供显著优势的通用前馈方法仍然没有得到充分的探索。在这项工作中，我们在大规模UrbanScene3D数据集上训练前馈NVS模型PixelNeRF。我们提出了四种训练策略来对这个数据集进行聚类和训练，强调了有限的视图重叠会阻碍性能。为了解决这个问题，我们引入了Aug3D，这是一种利用传统运动结构（SfM）重建场景的增强技术。Aug3D通过网格和语义采样生成条件良好的新视图，以增强前馈NVS模型学习。我们的实验表明，将每个集群的视图数量从20个减少到10个，PSNR提高了10%，但性能仍然不是最优的。Aug3D通过将新生成的新视图与原始数据集相结合，进一步解决了这一问题，证明了其在提高模型预测新视图的能力方面的有效性。 et.al.|[2501.06431](http://arxiv.org/abs/2501.06431)|null|
|**2025-01-09**|**Scaffold-SLAM: Structured 3D Gaussians for Simultaneous Localization and Photorealistic Mapping**|3D高斯散斑（3DGS）最近彻底改变了同步定位和映射（SLAM）中的新颖视图合成。然而，利用3DGS的现有SLAM方法未能同时为单眼、立体和RGB-D相机提供高质量的新颖视图渲染。值得注意的是，一些方法在RGB-D相机上表现良好，但在单眼相机的渲染质量方面却严重下降。在本文中，我们提出了脚手架SLAM，它可以在单目、立体和RGB-D相机上同时进行定位和高质量的真实感映射。我们引入了两项关键创新，以实现这种最先进的视觉质量。首先，我们提出了运动中的外观嵌入，使3D高斯模型能够更好地模拟不同相机姿态下的图像外观变化。其次，我们引入了一个频率正则化金字塔来引导高斯分布，使模型能够有效地捕捉场景中更精细的细节。对单眼、立体和RGB-D数据集的广泛实验表明，脚手架SLAM在真实感映射质量方面明显优于最先进的方法，例如，单眼相机的TUM RGB-D数据集中的PSNR高出16.76%。 et.al.|[2501.05242](http://arxiv.org/abs/2501.05242)|null|
|**2025-01-08**|**FatesGS: Fast and Accurate Sparse-View Surface Reconstruction using Gaussian Splatting with Depth-Feature Consistency**|最近，高斯散斑在计算机视觉领域引发了一种新的趋势。除了新颖的视图合成外，它还被扩展到多视图重建领域。最新的方法有助于完成详细的表面重建，同时确保快速的训练速度。然而，这些方法仍然需要密集的输入视图，并且它们的输出质量会随着稀疏视图的出现而显著降低。我们观察到高斯基元倾向于过拟合少数训练视图，导致有噪声的浮点运算和不完整的重建曲面。在本文中，我们提出了一种创新的稀疏视图重建框架，该框架利用视图内深度和多视图特征一致性来实现非常精确的表面重建。具体来说，我们利用单眼深度排名信息来监督斑块内深度分布的一致性，并采用平滑度损失来增强分布的连续性。为了实现更精细的表面重建，我们通过多视图投影特征优化了深度的绝对位置。在DTU和BlenedMVS上进行的大量实验表明，我们的方法优于最先进的方法，速度提高了60倍至200倍，实现了快速和细粒度的网格重建，而不需要昂贵的预训练。 et.al.|[2501.04628](http://arxiv.org/abs/2501.04628)|null|
|**2025-01-07**|**NeRFs are Mirror Detectors: Using Structural Similarity for Multi-View Mirror Scene Reconstruction with 3D Surface Primitives**|虽然神经辐射场（NeRF）在真实感新颖的视图合成方面取得了突破，但处理镜像表面仍然是一个特别的挑战，因为它们在场景表示中引入了严重的不一致性。之前的尝试要么侧重于重建单个反射物体，要么依赖于强有力的监督指导，即用户提供的镜子可见图像区域的额外注释，从而限制了实际可用性。相比之下，在本文中，我们提出了NeRF-MD，该方法表明NeRFs可以被视为镜像检测器，并且能够重建包含镜像表面的场景的神经辐射场，而不需要事先注释。为此，我们首先通过使用深度重投影损失训练标准NeRF来计算场景几何形状的初始估计。我们的关键见解在于，与镜像表面对应的场景部分仍将表现出明显的光度不一致，而其余部分已经以合理的方式重建。这使我们能够在训练的初始阶段通过将几何图元拟合到这种不一致的区域来检测镜面。利用这些信息，我们在第二个训练阶段联合优化辐射场和镜子几何形状，以提高其质量。我们展示了我们的方法能够忠实地检测场景中的镜子，并重建单个一致的场景表示，并展示了与基线和镜子感知方法相比的潜力。 et.al.|[2501.04074](http://arxiv.org/abs/2501.04074)|**[link](https://github.com/vc-bonn/nerfs-are-mirror-detectors)**|

<p align=right>(<a href=#updated-on-20250116>back to top</a>)</p>

## 3D Reconstruction

|Publish Date|Title|Abstract|PDF|Code|
|---|---|---|---|---|
|**2025-01-15**|**Scalable and High-Quality Neural Implicit Representation for 3D Reconstruction**|最近提出了各种基于SDF的神经隐式曲面重建方法，并表现出显著的建模能力。然而，由于单个网络的全局性和有限的表示能力，现有的方法仍然存在许多缺点，例如重建的精度和规模有限。在本文中，我们提出了一种通用、可扩展和高质量的神经隐式表示来解决这些问题。我们将分而治之的方法整合到基于神经SDF的重建中。具体来说，我们将对象或场景建模为具有重叠区域的多个独立局部神经SDF的融合。我们表示的构建涉及三个关键步骤：（1）基于对象结构或数据分布构建局部辐射场的分布和重叠关系，（2）相邻局部SDF的相对姿态配准，以及（3）SDF混合。由于每个局部区域的独立表示，我们的方法不仅可以实现高保真的表面重建，还可以实现可扩展的场景重建。大量的实验结果证明了我们提出的方法的有效性和实用性。 et.al.|[2501.08577](http://arxiv.org/abs/2501.08577)|null|
|**2025-01-13**|**3DGS-to-PC: Convert a 3D Gaussian Splatting Scene into a Dense Point Cloud or Mesh**|3D高斯散斑（3DGS）擅长生成高度详细的3D重建，但这些场景通常需要专门的渲染器才能进行有效的可视化。相比之下，点云是一种广泛使用的3D表示，与大多数流行的3D处理软件兼容，但将3DGS场景转换为点云是个复杂的挑战。在这项工作中，我们将3DGS引入PC，这是一个灵活且高度可定制的框架，能够将3DGS场景转换为密集、高精度的点云。我们将每个高斯分布的点作为3D密度函数进行概率采样。我们还使用到高斯中心的马氏距离来阈值化新点，以防止极端异常值。结果是一个点云，它非常接近编码到3D高斯场景中的形状。单个高斯人使用球面调和来根据视图调整颜色，每个点可能只会为最终渲染的场景提供微妙的颜色提示。为了避免与最终点云不匹配的虚假或不正确的颜色，我们通过定制的图像渲染方法重新计算高斯颜色，为每个高斯颜色分配其在所有视图中贡献最大的像素的颜色。3DGS到PC还支持通过泊松曲面重建生成网格，该重建应用于从预测的曲面高斯中采样的点。这允许从3DGS场景生成彩色网格，而无需重新训练。该软件包具有高度的可定制性，能够简单地集成到现有的3DGS管道中。3DGS to PC提供了一个强大的工具，用于将3DGS数据转换为基于点云和曲面的格式。 et.al.|[2501.07478](http://arxiv.org/abs/2501.07478)|**[link](https://github.com/lewis-stuart-11/3dgs-to-pc)**|
|**2025-01-13**|**PO-GVINS: Tightly Coupled GNSS-Visual-Inertial Integration with Pose-Only Representation**|准确可靠的定位对于自动驾驶、无人机和智能机器人中的感知、决策和其他高级应用至关重要。鉴于独立传感器的固有局限性，将具有互补功能的异构传感器集成是实现这一目标的最有效方法之一。本文提出了一种基于滤波的紧密耦合全球导航卫星系统（GNSS）-视觉惯性定位框架，该框架仅应用于视觉惯性系统（VINS），称为PO-GVINS。具体来说，当前VINS中使用的多视图成像需要先验的3D特征，然后联合估计相机姿态和3D特征位置，这不可避免地会引入特征的线性化误差以及面对维度爆炸。然而，仅姿态（PO）公式被证明与多视图成像等效，并已应用于视觉重建，它使用两个相机姿态表示特征深度，从而从状态向量中去除3D特征位置，避免了上述困难。受此启发，我们首先在VINS中应用PO配方，即PO-VINS。然后将GNSS原始测量值与解决的整周模糊度相结合，以实现准确和无漂移的估计。大量实验表明，所提出的PO-VINS明显优于多状态约束卡尔曼滤波器（MSCKF）。通过结合GNSS测量，PO-GVINS实现了准确、无漂移的状态估计，使其成为在具有挑战性的环境中进行定位的稳健解决方案。 et.al.|[2501.07259](http://arxiv.org/abs/2501.07259)|null|
|**2025-01-13**|**Representation Learning of Point Cloud Upsampling in Global and Local Inputs**|近年来，点云上采样在三维重建等领域得到了广泛的应用。我们的研究通过表示学习在全球和局部层面调查了影响点云上采样的因素。具体来说，本文将同一点云模型对象的全局和局部信息输入到两个编码器中，以提取这些特征，融合它们，然后将组合的特征馈送到上采样解码器中。目标是通过利用来自全局和局部输入的先验知识来解决点云中的稀疏性和噪声问题。所提出的框架可以应用于任何最先进的点云上采样神经网络。在一系列基于自动编码器的模型上进行了实验，利用深度学习，对全局和局部输入都产生了可解释性，结果证明，我们提出的框架可以进一步改善先前SOTA工作中的上采样效果。同时，显著性图反映了全局和局部特征输入之间的差异，以及同时使用这两种输入进行训练的有效性。 et.al.|[2501.07076](http://arxiv.org/abs/2501.07076)|null|
|**2025-01-14**|**SplatMAP: Online Dense Monocular SLAM with 3D Gaussian Splatting**|由于运动结构（SfM）和单眼SLAM等传统方法在准确捕捉场景细节方面的固有局限性，从单眼视频中实现高保真3D重建仍然具有挑战性。虽然神经辐射场（NeRF）等可微分渲染技术解决了其中一些挑战，但它们的高计算成本使其不适合实时应用。此外，现有的3D高斯散斑（3DGS）方法通常侧重于光度一致性，忽略了几何精度，并且未能利用SLAM的动态深度和姿态更新进行场景细化。我们提出了一种将密集SLAM与3DGS集成在一起的框架，用于实时、高保真的密集重建。我们的方法引入了SLAM知情自适应加密，通过利用SLAM的密集点云动态更新和加密高斯模型。此外，我们还引入了几何引导优化，该优化结合了边缘感知几何约束和光度一致性，共同优化3DGS场景表示的外观和几何，实现了详细准确的SLAM映射重建。在Replica和TUM-RGBD数据集上的实验证明了我们的方法的有效性，在单眼系统中取得了最先进的结果。具体来说，我们的方法在Replica上实现了36.864的PSNR、0.985的SSIM和0.040的LPIPS，分别比之前的SOTA提高了10.7%、6.4%和49.4%。在TUM-RGBD上，我们的方法在相同的指标上比最接近的基线高出10.2%、6.6%和34.7%。这些结果突显了我们的框架在弥合光度和几何密集3D场景表示之间的差距方面的潜力，为实用和高效的单眼密集重建铺平了道路。 et.al.|[2501.07015](http://arxiv.org/abs/2501.07015)|null|
|**2025-01-12**|**CULTURE3D: Cultural Landmarks and Terrain Dataset for 3D Applications**|在这篇论文中，我们使用从世界各地捕获的高分辨率图像，提出了一个大规模的细粒度数据集。与现有数据集相比，我们的数据集提供了更大的大小，并包含了更高级别的细节，使其特别适合细粒度的3D应用程序。值得注意的是，我们的数据集是使用无人机捕获的航空图像构建的，这为捕获真实世界的场地布局和建筑结构提供了更准确的视角。通过使用这些详细的图像重建环境，我们的数据集支持高斯散斑的COLMAP格式和运动结构（SfM）方法等应用。它与广泛使用的技术兼容，包括SLAM、多视图立体和神经辐射场（NeRF），可实现精确的3D重建和点云。这使其成为重建和分割任务的基准。该数据集能够与多模态数据无缝集成，支持从建筑重建到虚拟旅游的一系列3D应用。它的灵活性促进了创新，促进了3D建模和分析的突破。 et.al.|[2501.06927](http://arxiv.org/abs/2501.06927)|null|
|**2025-01-10**|**MEt3R: Measuring Multi-View Consistency in Generated Images**|我们引入了MEt3R，这是一种用于生成图像中多视图一致性的度量。用于多视图图像生成的大规模生成模型正在迅速推进稀疏观测的3D推理领域。然而，由于生成建模的性质，传统的重建度量不适合衡量生成输出的质量，迫切需要独立于采样过程的度量。在这项工作中，我们专门解决了生成的多视图图像之间的一致性问题，这些图像可以独立于特定场景进行评估。我们的方法使用DUSt3R以前馈方式从图像对中获得密集的3D重建，这些重建用于将图像内容从一个视图扭曲到另一个视图。然后，比较这些图像的特征图，以获得对视图相关效果不变的相似性得分。使用MEt3R，我们评估了大量先前新视图和视频生成方法的一致性，包括我们的开放式多视图潜在扩散模型。 et.al.|[2501.06336](http://arxiv.org/abs/2501.06336)|null|
|**2025-01-09**|**Identifiability of Controlled Open Quantum Systems**|开放量子系统是量子力学和随机分析交叉领域的一个丰富研究领域。我们在双线性动力系统的框架内统一了受控开放量子系统的多种观点。我们从量子态层析成像的结果中定义了相应的可识别性概念，该结果是在不同长度控制信号的子序列下，在初始量子态的许多副本中获得的。我们解释并扩展了使用谱准则、基于Hankel矩阵的准则和频域准则对双线性系统可识别性的研究，并将其扩展到开放量子系统主方程的参数估计。这为识别开放量子系统的一些建设性方法奠定了基础。 et.al.|[2501.05270](http://arxiv.org/abs/2501.05270)|null|
|**2025-01-09**|**A Systematic Literature Review on Deep Learning-based Depth Estimation in Computer Vision**|深度估计（DE）提供关于场景的空间信息，并实现诸如3D重建、对象检测和场景理解等任务。最近，人们对使用基于深度学习（DL）的方法进行DE的兴趣越来越大。传统技术依赖于手工制作的特征，这些特征往往难以推广到不同的场景，需要大量的手动调整。然而，DE的DL模型可以从输入数据中自动提取相关特征，适应各种场景条件，并很好地泛化到看不见的环境。已经开发了许多基于DL的方法，因此有必要调查和综合最新技术（SOTA）。之前关于DE的综述主要集中在单眼或基于立体的技术上，而不是全面综述DE。此外，据我们所知，还没有全面关注DE的系统文献综述（SLR）。因此，正在进行这项SLR研究。最初，在电子数据库中搜索相关出版物，得到1284份出版物。使用定义的排除和质量标准，筛选出128篇出版物，并进一步筛选出59篇高质量的初步研究。对这些研究进行分析，以提取数据并回答定义的研究问题。基于这些结果，DL方法主要针对三种不同类型的DE：单眼、立体和多视图。20个公开可用的数据集用于训练、测试和评估DE的DL模型，其中KITTI、NYU Depth V2和Make 3D是使用最多的数据集。使用29个评估指标来评估DE的性能。初步研究中报告了35个基础模型，使用最多的前五个基础模型是ResNet-50、ResNet-18、ResNet-101、U-Net和VGG-16。最后，缺乏地面实况数据是主要研究报告的最重大挑战之一。 et.al.|[2501.05147](http://arxiv.org/abs/2501.05147)|null|
|**2025-01-07**|**Materialist: Physically Based Editing Using Single-Image Inverse Rendering**|为了基于单视图、基于逆物理的渲染进行图像编辑，我们提出了一种将基于学习的方法与渐进可微渲染相结合的方法。对于给定的图像，我们的方法利用神经网络来预测初始材料属性。然后，使用渐进可微渲染来优化环境贴图并细化材质属性，目标是使渲染结果与输入图像紧密匹配。我们只需要一张图像，而基于渲染方程的其他逆渲染方法需要多个视图。与依赖神经渲染器的单视图方法相比，我们的方法实现了更逼真的光与材质交互、精确的阴影和全局照明。此外，通过优化材质属性和照明，我们的方法可以执行各种任务，包括基于物理的材质编辑、对象插入和重新照明。我们还提出了一种材质透明度编辑方法，该方法无需全场景几何即可有效操作。与基于稳定扩散的方法相比，我们的方法基于经验结果提供了更强的可解释性和更真实的光折射。 et.al.|[2501.03717](http://arxiv.org/abs/2501.03717)|**[link](https://github.com/lez-s/materialist)**|

<p align=right>(<a href=#updated-on-20250116>back to top</a>)</p>

## Diffusion

|Publish Date|Title|Abstract|PDF|Code|
|---|---|---|---|---|
|**2025-01-15**|**Ouroboros-Diffusion: Exploring Consistent Content Generation in Tuning-free Long Video Diffusion**|基于预训练的文本到视频模型的先进先出（FIFO）视频扩散最近已成为一种无需调谐的长视频生成的有效方法。该技术保持了一个噪声逐渐增加的视频帧队列，在队列的头部连续产生干净的帧，而高斯噪声在尾部排队。然而，由于缺乏跨帧的对应建模，FIFO扩散通常难以在生成的视频中保持长距离的时间一致性。在本文中，我们提出了Ouroboros Diffusion，这是一种新颖的视频去噪框架，旨在增强结构和内容（主题）的一致性，从而生成任意长度的一致视频。具体来说，我们在队列尾部引入了一种新的潜在采样技术，以提高结构一致性，确保帧之间的感知平滑过渡。为了提高受试者的一致性，我们设计了一种受试者感知跨帧注意力（SACFA）机制，该机制在短片段内跨帧对齐受试者，以实现更好的视觉连贯性。此外，我们引入了自循环指导。该技术利用队列前部所有先前更干净帧的信息来指导末尾噪声帧的去噪，从而促进丰富的上下文全局信息交互。在VBench基准上进行的长视频生成的广泛实验证明了我们的Ouroboros扩散的优越性，特别是在主题一致性、运动平滑性和时间一致性方面。 et.al.|[2501.09019](http://arxiv.org/abs/2501.09019)|null|
|**2025-01-15**|**How Do Generative Models Draw a Software Engineer? A Case Study on Stable Diffusion Bias**|生成模型如今被广泛用于生成用于多种目的的图形内容，例如网络、艺术、广告。然而，研究表明，这些模型生成的图像可能会强化特定背景下已经存在的社会偏见。在本文中，我们重点了解当生成与各种软件工程任务相关的图像时，是否会出现这种情况。事实上，软件工程（SE）社区也不能免受性别和种族差异的影响，这些差异可能会因使用这些模型而放大。因此，如果在没有意识的情况下使用，人工生成的图像可能会强化SE领域的这些偏见。具体来说，我们对稳定扩散（SD）模型（一种非常流行的开源文本到图像模型）的三个版本（SD 2、SD XL和SD 3）在SE任务中暴露的性别和种族偏见进行了广泛的实证评估。我们通过向每个模型提供两组描述不同软件相关任务的提示来获得6720张图像：一组包含软件工程师关键字，另一组不包含执行任务的人员的任何说明。接下来，我们评估生成图像中的性别和种族差异。结果显示，在代表软件工程师时，所有模型都明显偏向于男性。相反，虽然SD 2和SD XL对白人数字有强烈的偏见，但SD 3对亚洲数字的偏见略大。然而，无论使用何种风格，所有模特都明显低估了黑人和阿拉伯人的形象。我们的分析结果突显了人们对采用这些模型为SE任务生成内容的严重担忧，并为未来在这种情况下对偏见缓解的研究开辟了领域。 et.al.|[2501.09014](http://arxiv.org/abs/2501.09014)|**[link](https://github.com/giordanodaloisio/sd-bias)**|
|**2025-01-15**|**SimGen: A Diffusion-Based Framework for Simultaneous Surgical Image and Segmentation Mask Generation**|获取和注释手术数据通常是资源密集型的、道德约束的，需要大量的专家参与。虽然文本到图像等生成性人工智能模型可以缓解数据稀缺，但结合分割掩模等空间注释对于精确驱动的手术应用、模拟和教育至关重要。本研究介绍了一种新的任务和方法SimGen，用于同时生成图像和掩模。SimGen是一种基于DDPM框架和残差U-Net的扩散模型，旨在联合生成高保真手术图像及其相应的分割掩模。该模型利用互相关先验来捕捉连续图像和离散掩模分布之间的依赖关系。此外，采用规范斐波那契晶格（CFL）来增强掩模RGB空间中的类可分离性和均匀性。SimGen提供高保真图像和精确的分割掩模，在基于图像和语义起始距离度量评估的六个公共数据集上表现优于基线。烧蚀研究表明，CFL提高了掩模质量和空间分离。下游实验表明，如果法规限制人类数据发布用于研究，则生成的图像掩模对是可用的。这项工作为生成成对的手术图像和复杂的标签提供了一种经济高效的解决方案，通过减少对昂贵的手动注释的需求来推进手术人工智能的发展。 et.al.|[2501.09008](http://arxiv.org/abs/2501.09008)|null|
|**2025-01-15**|**CrystalGRW: Generative Modeling of Crystal Structures with Targeted Properties via Geodesic Random Walks**|确定候选晶体材料是否热力学稳定取决于确定其真实的基态结构，这是计算材料科学的一个核心挑战。我们介绍了CrystalGRW，这是一种基于黎曼流形的扩散生成模型，提出了新的晶体结构，可以预测密度泛函理论验证的稳定相。晶体性质，如分数坐标、原子类型和晶格矩阵，在合适的黎曼流形上表示，确保通过扩散过程产生的新预测保持晶体结构的周期性。我们引入了一个等变图神经网络，以解释生成过程中的旋转和平移对称性。CrystalGRW展示了生成接近基态的真实晶体结构的能力，其精度与现有模型相当，同时还实现了条件控制，例如指定所需的晶体学点群。这些特征通过为实验验证提供稳定、对称一致的晶体候选者，有助于加速材料发现和逆向设计。 et.al.|[2501.08998](http://arxiv.org/abs/2501.08998)|null|
|**2025-01-15**|**RepVideo: Rethinking Cross-Layer Representation for Video Generation**|随着扩散模型的引入，视频生成取得了显著进展，显著提高了生成视频的质量。然而，最近的研究主要集中在扩大模型训练，同时对表示对视频生成过程的直接影响提供了有限的见解。在本文中，我们初步研究了中间层特征的特征，发现不同层的注意力图存在实质性差异。这些变化导致语义表示不稳定，并导致特征之间的累积差异，最终降低相邻帧之间的相似性，并对时间连贯性产生负面影响。为了解决这个问题，我们提出了RepVideo，这是一个用于文本到视频扩散模型的增强表示框架。通过累积相邻层的特征以形成丰富的表示，这种方法可以捕获更稳定的语义信息。然后，这些增强的表示被用作注意力机制的输入，从而提高了语义表达能力，同时确保了相邻帧之间的特征一致性。大量实验表明，我们的RepVideo不仅显著增强了生成准确空间外观的能力，例如捕获多个对象之间的复杂空间关系，而且提高了视频生成的时间一致性。 et.al.|[2501.08994](http://arxiv.org/abs/2501.08994)|null|
|**2025-01-15**|**CityLoc: 6 DoF Localization of Text Descriptions in Large-Scale Scenes with Gaussian Representation**|在大规模3D场景中本地化文本描述本质上是一项模糊的任务。尽管如此，在描述一般概念时，例如城市中的所有交通信号灯，仍会出现这种情况。为了促进基于这些概念的推理，需要以分布的形式进行文本本地化。在本文中，我们根据文本描述生成了相机姿态的分布。为了促进这种生成，我们提出了一种基于扩散的架构，该架构有条件地将嘈杂的6DoF相机姿态扩散到它们的合理位置。使用预训练的文本编码器从文本描述中导出条件信号。文本描述和姿态分布之间的联系是通过预训练的视觉语言模型（CLIP）建立的。此外，我们证明，通过使用3D高斯飞溅渲染潜在姿势，通过视觉推理将姿势不正确的样本引导到与文本描述更好地对齐的位置，可以进一步细化分布的候选姿势。我们通过与标准检索方法和基于学习的方法进行比较，证明了我们的方法的有效性。我们提出的方法在所有五个大规模数据集中始终优于这些基线。我们的源代码和数据集将公开。 et.al.|[2501.08982](http://arxiv.org/abs/2501.08982)|null|
|**2025-01-15**|**On idealized models of turbulent condensation in clouds**|各种微物理模型试图通过湍流环境中凝结引起的随机液滴增长的近似表示来解释云中宽液滴尺寸分布（DSD）的发生。这项工作分析了特定的理想化模型，其中液滴生长条件的可变性主要来自携带这些液滴的空气的湍流垂直速度的可变性。例如，在绝热包裹中运行的随机涡流跳跃模型和某些类型的DNS类模型。我们发现，这些模型产生的液滴尺寸统计数据在垂直方向上是空间不均匀的，导致预测的DSD取决于DSD空间采样尺度 $\Delta$。在这些模型中，$\Delta$隐含地与液滴湍流扩散的空间范围有关（近似于布朗偏移），因此像$t^{1/2}$一样增长。这导致了虚假的连续DSD加宽，因为液滴平方半径标准偏差的时间增长（也像$t^{1/2}$）基本上是由采样尺度$\Delta$ 的增长引起的。此外，本文讨论的模型预测的DSD不一定在局部范围内很宽（从某种意义上说，大小液滴可能无法在足够小的体积内很好地混合），因此不一定表明重力诱导液滴凝结的概率增加。为了为子网格参数化建立坚实的物理基础，本研究提出了一个框架来解释理想化模型的优点和局限性，并指出如何明智地评估和使用它们作为云大涡模拟中湍流凝结的子网格表示。 et.al.|[2501.08968](http://arxiv.org/abs/2501.08968)|null|
|**2025-01-15**|**Compositional dependence of magnetic damping in sputter-deposited CoxFe1-x thin films**|Co25Fe75铁磁薄膜表现出超低磁阻尼。本文报道了钴铁薄膜对钴成分（23%至36%）的磁阻尼依赖性。薄膜结构在环境温度下溅射沉积，利用平面内和平面外几何形状的FMR测量来测量磁阻尼参数，包括固有阻尼和自旋泵浦的贡献。阻尼参数随着Co含量的增加而降低，但Co31Fe69除外。阻尼的最小值对应于表现出界面垂直磁各向异性的合金。Co36Fe64的值为0.00091，而Co31Fe69的值为0.002，这种成分表现出最大的平面内各向异性。对Co36Fe64薄膜堆叠的HAADF-STEM横截面分析显示，Cu相互扩散到磁性层中。发现与大部分多晶晶粒相比，晶界处的相互扩散程度高达7倍。将Cu掺入铁磁层会对磁阻尼产生不利影响。通过提高生长室基底压力来减少磁性层中的杂质，导致磁阻尼降低了18%。衍射分析表明，Co36Fe64的主要生长方向为[101]，Cu缓冲层的主要生长趋势为[111]，这些平面垂直于它们各自的[101]平面，对于这种组成，晶格失配被确定为0.9325%。晶格失配随着Co含量的增加而减少，因此晶格应变也随之增加。铜扩散到铁磁体中会产生磁振子散射中心和磁性的局部变化。这两个因素都会对磁阻尼产生负面影响。 et.al.|[2501.08948](http://arxiv.org/abs/2501.08948)|null|
|**2025-01-15**|**Enhanced Multi-Scale Cross-Attention for Person Image Generation**|本文提出了一种新的基于交叉注意力的生成对抗网络（GAN），用于具有挑战性的人物图像生成任务。交叉注意是一种新颖直观的多模态融合方法，其中在不同模态的两个特征图之间计算注意/相关矩阵。具体来说，我们提出了小说《兴感》（或《交感》），它由两个分别捕捉人的外表和形状的世代分支组成。此外，我们提出了两种新颖的交叉注意力块，可以有效地转移和更新人的形状和外观嵌入，以实现相互改进。这是其他基于GAN的图像生成工作尚未考虑到的。为了进一步了解不同尺度和子区域上不同人物姿势之间的长程相关性，我们提出了两种新的多尺度交叉注意力块。为了解决交叉注意力机制中独立相关计算导致噪声和模糊注意力权重的问题，这阻碍了性能的提高，我们提出了一个称为增强注意力（EA）的模块。最后，我们引入了一种新的密集连接的共同注意力模块，可以有效地融合不同阶段的外观和形状特征。在两个公共数据集上进行的广泛实验表明，所提出的方法优于当前基于GAN的方法，并且与基于扩散的方法性能相当。然而，我们的方法在训练和推理方面都比基于扩散的方法快得多。 et.al.|[2501.08900](http://arxiv.org/abs/2501.08900)|null|
|**2025-01-15**|**Helicity effect on turbulent passive and active scalar diffusivities**|众所周知，湍流会产生增强的有效磁和被动标量扩散率，这可以通过数值方法相当准确地确定。现在已知，如果流动也是螺旋形的，则有效磁扩散率相对于非螺旋值会降低。通常的二阶相关近似和各种 $\tau$ 方法都无法捕捉到这一点。在这里，我们表明螺旋度对湍流被动标量扩散率的影响是相反的，并导致增强。这种效果以前从未见过。我们还证明了湍流速度场的相关时间随着动力学螺旋度的增加而增加。这是对所得数值结果进行理论解释的关键点。分层旋转湍流自洽产生螺旋度的模拟结果表明，湍流被动标量扩散率随着转速的增加而降低。 et.al.|[2501.08879](http://arxiv.org/abs/2501.08879)|null|

<p align=right>(<a href=#updated-on-20250116>back to top</a>)</p>

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

<p align=right>(<a href=#updated-on-20250116>back to top</a>)</p>

[contributors-shield]: https://img.shields.io/github/contributors/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[contributors-url]: https://github.com/Vincentqyw/cv-arxiv-daily/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[forks-url]: https://github.com/Vincentqyw/cv-arxiv-daily/network/members
[stars-shield]: https://img.shields.io/github/stars/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[stars-url]: https://github.com/Vincentqyw/cv-arxiv-daily/stargazers
[issues-shield]: https://img.shields.io/github/issues/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[issues-url]: https://github.com/Vincentqyw/cv-arxiv-daily/issues

