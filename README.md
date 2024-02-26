[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]

## Updated on 2024.02.26
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
|**2024-02-22**|**FrameNeRF: A Simple and Efficient Framework for Few-shot Novel View Synthesis**|我们提出了一种新的框架，称为FrameNeRF，旨在将现成的快速高保真NeRF模型应用于少镜头的新颖视图合成任务，该模型具有快速训练速度和高渲染质量。快速高保真度模型的训练稳定性通常局限于密集视图，这使得它们不适合于少镜头的新颖视图合成任务。为了解决这一限制，我们利用正则化模型作为数据生成器，从稀疏输入中生成密集视图，从而促进快速高保真模型的后续训练。由于这些密集视图是由正则化模型生成的伪地面实况，因此使用原始稀疏图像来微调快速高保真度模型。这个过程有助于模型学习真实的细节，并更正早期阶段引入的工件。通过利用现成的正则化模型和快速高保真度模型，我们的方法在各种基准数据集上实现了最先进的性能。 et.al.|[2402.14586](http://arxiv.org/abs/2402.14586)|null|
|**2024-02-22**|**TaylorGrid: Towards Fast and High-Quality Implicit Field Learning via Direct Taylor-based Grid Optimization**|基于坐标的神经隐式表示或隐式场已被广泛研究用于3D几何表示或新颖视图合成。近年来，人们致力于加快基于坐标的内隐场学习的速度和提高其质量。代替学习重MLP来预测查询坐标的神经隐式值，已经提出了与浅MLP相结合的神经体素或网格来实现具有减少的优化时间的高质量隐式场学习。另一方面，为了进一步提高学习速度，已经提出了诸如线性网格之类的轻量级场表示。在本文中，我们的目标是快速和高质量的隐场学习，并提出了TaylorGrid，这是一种新的隐场表示，可以在2D或3D网格上通过直接泰勒展开优化有效地计算。一般来说，TaylorGrid可以适用于不同的内隐场学习任务，如SDF学习或NeRF。通过广泛的定量和定性比较，TaylorGrid实现了线性网格和神经体素之间的平衡，显示了其在快速和高质量的内隐场学习中的优势。 et.al.|[2402.14415](http://arxiv.org/abs/2402.14415)|null|
|**2024-02-20**|**Improving Robustness for Joint Optimization of Camera Poses and Decomposed Low-Rank Tensorial Radiance Fields**|在本文中，我们提出了一种算法，该算法允许仅使用2D图像作为监督，对由分解的低秩张量表示的相机姿态和场景几何进行联合细化。首先，我们基于1D信号进行了一项试点研究，并将我们的发现与3D场景联系起来，在3D场景中，基于体素的NeRF上的初始关节姿态优化可以很容易地导致次优解。此外，基于频谱分析，我们建议在2D和3D辐射场上应用卷积高斯滤波器，以实现从粗到细的训练计划，从而实现联合相机姿态优化。利用分解后的低秩张量中的分解特性，我们的方法实现了与强力3D卷积等效的效果，只需很少的计算开销。为了进一步提高联合优化的鲁棒性和稳定性，我们还提出了平滑的2D监督、随机缩放的核参数和边缘引导的损失掩模技术。广泛的定量和定性评估表明，我们提出的框架在新的视图合成方面取得了卓越的性能，并实现了快速收敛的优化。 et.al.|[2402.13252](http://arxiv.org/abs/2402.13252)|**[link](https://github.com/nemo1999/joint-tensorf)**|
|**2024-02-20**|**Real-time High-resolution View Synthesis of Complex Scenes with Explicit 3D Visibility Reasoning**|绘制复杂场景的照片逼真的新颖视图图像一直是计算机图形学中的一个长期挑战。近年来，在视图合成领域，在提高渲染质量和加快渲染速度方面取得了很大的研究进展。然而，当使用稀疏视图渲染复杂的动态场景时，由于遮挡问题，渲染质量仍然有限。此外，对于在动态场景中渲染高分辨率图像，渲染速度仍远未达到实时性。在这项工作中，我们提出了一种可推广的视图合成方法，该方法可以从稀疏视图实时渲染复杂静态和动态场景的高分辨率新视图图像。为了解决由输入视图的稀疏性和捕获场景的复杂性引起的遮挡问题，我们引入了一种显式3D可见性推理方法，该方法可以有效地估计采样的3D点对输入视图的可见性。所提出的可见性推理方法是完全可微分的，可以很好地适应体绘制管道，使我们能够在训练网络时只使用多视图图像作为监督，同时细化几何体和纹理。此外，我们管道中的每个模块都经过精心设计，以绕过耗时的MLP查询过程，提高高分辨率图像的渲染质量，使我们能够实时渲染高分辨率的新视图图像。实验结果表明，我们的方法在渲染质量和速度上都优于以前的视图合成方法，尤其是在处理具有稀疏视图的复杂动态场景时。 et.al.|[2402.12886](http://arxiv.org/abs/2402.12886)|null|
|**2024-02-20**|**MVDiffusion++: A Dense High-resolution Multi-view Diffusion Model for Single or Sparse-view 3D Object Reconstruction**|本文提出了一种用于3D对象重建的神经结构MVDiffusion++，该结构在给定一张或几张没有相机姿势的图像的情况下合成对象的密集和高分辨率视图。MVDiffusion++通过两个令人惊讶的简单想法实现了卓越的灵活性和可扩展性：1）“无姿势架构”，其中2D潜在特征之间的标准自关注在任意数量的条件视图和生成视图中学习3D一致性，而无需显式使用相机姿势信息；和2）一种“视图丢弃策略”，在训练期间丢弃大量输出视图，这减少了训练时间内存占用，并在测试时实现了密集和高分辨率的视图合成。我们使用Ob厌恶对象进行训练，使用谷歌扫描对象进行评估，并使用标准的新视图合成和3D重建指标，其中MVDiffusion++显著优于当前的技术状态。我们还通过将MVDiffusion++与文本到图像生成模型相结合，展示了一个文本到3D应用程序示例。 et.al.|[2402.12712](http://arxiv.org/abs/2402.12712)|null|
|**2024-02-19**|**Binary Opacity Grids: Capturing Fine Geometric Detail for Mesh-Based View Synthesis**|虽然基于表面的视图合成算法由于其低计算要求而很有吸引力，但它们往往难以再现薄结构。相比之下，将场景的几何体建模为体积密度场（例如NeRF）的更昂贵的方法擅长于重建精细的几何细节。然而，密度场通常以“模糊”的方式表示几何体，这阻碍了曲面的精确定位。在这项工作中，我们修改了密度场，以鼓励它们向表面会聚，而不影响它们重建薄结构的能力。首先，我们使用离散的不透明度网格表示，而不是连续的密度场，这允许不透明度值在曲面上从零不连续地过渡到一。其次，我们通过每个像素投射多条光线来消除混叠，这允许在不使用半透明体素的情况下对遮挡边界和亚像素结构进行建模。第三，我们最小化不透明度值的二元熵，这通过鼓励不透明度值在训练结束时进行二元化来促进表面几何的提取。最后，我们开发了一种基于融合的网格划分策略，然后进行网格简化和外观模型拟合。与现有的基于网格的方法相比，我们的模型生成的紧凑网格可以在移动设备上实时渲染，并实现显著更高的视图合成质量。 et.al.|[2402.12377](http://arxiv.org/abs/2402.12377)|null|
|**2024-02-15**|**GES: Generalized Exponential Splatting for Efficient Radiance Field Rendering**|3D高斯散射的进步显著加速了3D重建和生成。然而，它可能需要大量的高斯，这会产生大量的内存占用。本文介绍了GES（Generalized Exponential Splatting），这是一种利用广义指数函数（GEF）对3D场景进行建模的新表示，需要更少的粒子来表示场景，因此在效率上显著优于高斯飞溅方法，并具有基于高斯的实用程序的即插即用替换能力。GES在原理性1D设置和逼真的3D场景中都得到了理论和实证验证。它被证明可以更准确地表示具有尖锐边缘的信号，由于其固有的低通特性，这对高斯人来说通常是具有挑战性的。我们的实证分析表明，GEF在拟合自然发生的信号（如正方形、三角形和抛物线信号）方面优于高斯，从而减少了对增加高斯飞溅的内存占用的广泛拆分操作的需要。借助调频损耗，GES在新的视图合成基准中实现了有竞争力的性能，同时所需的内存存储量不到高斯飞溅的一半，并将渲染速度提高了39%。代码可在项目网站上获得https://abdullahamdi.com/ges . et.al.|[2402.10128](http://arxiv.org/abs/2402.10128)|**[link](https://github.com/ajhamdi/ges-splatting)**|
|**2024-02-14**|**PC-NeRF: Parent-Child Neural Radiance Fields Using Sparse LiDAR Frames in Autonomous Driving Environments**|大规模的3D场景重建和新颖的视图合成对于自动驾驶汽车至关重要，尤其是利用时间稀疏的激光雷达帧。然而，传统的显式表示仍然是以无限分辨率表示重建和合成场景的一个重要瓶颈。尽管最近开发的神经辐射场（NeRF）在隐式表示中显示出令人信服的结果，但使用稀疏激光雷达帧进行大规模3D场景重建和新的视图合成的问题仍未得到探索。为了弥补这一差距，我们提出了一种3D场景重建和新的视图合成框架，称为父子神经辐射场（PC NeRF）。该框架基于父NeRF和子NeRF两个模块，实现了分层空间划分和多级场景表示，包括场景、分段和点级别。多级场景表示增强了稀疏激光雷达点云数据的有效利用，并能够快速获取近似体积场景表示。经过大量实验，PC NeRF被证明可以在大规模场景中实现高精度的新型激光雷达视图合成和三维重建。此外，PC NeRF可以有效地处理稀疏激光雷达帧的情况，并在有限的训练时期内表现出较高的部署效率。我们的方法实施和预先培训的模型可在https://github.com/biter0088/pc-nerf. et.al.|[2402.09325](http://arxiv.org/abs/2402.09325)|**[link](https://github.com/biter0088/pc-nerf)**|
|**2024-02-11**|**BioNeRF: Biologically Plausible Neural Radiance Fields for View Synthesis**|本文介绍了BioNeRF，这是一种生物学上合理的架构，它以3D表示对场景进行建模，并通过辐射场合成新的视图。由于NeRF依赖于网络权重来存储场景的三维表示，BioNeRF实现了一种受认知启发的机制，该机制将来自多个来源的输入融合到类似记忆的结构中，提高了存储容量，并提取了更多内在和相关的信息。BioNeRF还模拟了在锥体细胞中观察到的与上下文信息有关的行为，其中记忆作为上下文提供，并与两个后续神经模型的输入相结合，一个负责产生体积密度，另一个负责渲染场景所用的颜色。实验结果表明，BioNeRF在两个数据集（真实世界图像和合成数据）中对人类感知进行编码的质量测量方面优于最先进的结果。 et.al.|[2402.07310](http://arxiv.org/abs/2402.07310)|**[link](https://github.com/leandropassosjr/bionerf)**|
|**2024-02-11**|**3D Gaussian as a New Vision Era: A Survey**|3D高斯散射（3D-GS）已成为计算机图形学领域的一个重大进步，它提供了明确的场景表示和新颖的视图合成，而不依赖于神经网络，如神经辐射场（NeRF）。这项技术在机器人、城市地图、自主导航和虚拟现实/增强现实等领域有着不同的应用。鉴于三维高斯散射的日益流行和研究的不断扩展，本文对过去一年的相关论文进行了全面的综述。我们根据特征和应用对分类法进行了调查，介绍了3D高斯飞溅的理论基础。我们通过这项调查的目标是让新的研究人员熟悉3D高斯飞溅，为该领域的开创性工作提供宝贵的参考，并启发未来的研究方向，正如我们的结论部分所讨论的那样。 et.al.|[2402.07181](http://arxiv.org/abs/2402.07181)|null|

<p align=right>(<a href=#updated-on-20240226>back to top</a>)</p>

## 3D Reconstruction

|Publish Date|Title|Abstract|PDF|Code|
|---|---|---|---|---|
|**2024-02-22**|**Cameras as Rays: Pose Estimation via Ray Diffusion**|估计相机姿态是3D重建的一项基本任务，并且在稀疏视图（<10）的情况下仍然具有挑战性。与现有的对相机外部全局参数化进行自上而下预测的方法不同，我们提出了一种相机姿态的分布式表示，将相机视为一束光线。该表示允许与空间图像特征的紧密耦合，从而提高姿态精度。我们观察到，这种表示自然适合于设置级别的变换器，并开发了一种基于回归的方法，将图像块映射到相应的射线。为了捕捉稀疏视图姿态推断中固有的不确定性，我们采用这种方法来学习去噪扩散模型，该模型允许我们对合理的模式进行采样，同时提高性能。我们提出的方法，包括基于回归和扩散的方法，在CO3D上展示了最先进的相机姿态估计性能，同时推广到看不见的物体类别和野外捕捉。 et.al.|[2402.14817](http://arxiv.org/abs/2402.14817)|null|
|**2024-02-22**|**Workspace Analysis for Laparoscopic Rectal Surgery : A Preliminary Study**|医学成像、计算分析和机器人技术的集成为微创外科手术带来了重大变革，尤其是在腹腔镜直肠手术（LRS）领域。这种专门的外科技术旨在解决直肠癌症，需要深入理解骨盆狭窄空间内的空间动力学。本研究利用磁共振成像（MRI）扫描作为基础数据集，将其纳入计算机辅助设计（CAD）软件，以生成患者解剖结构的精确三维（3D）重建。这项研究的核心是对手术工作空间的分析，这是机器人干预优化的一个关键方面。复杂的计算算法在CAD环境中处理MRI数据，仔细计算骨盆内部区域的尺寸和轮廓。结果是，考虑到曲率、直径变化和潜在障碍等因素，对LRS期间的可行区域和限制区域进行了细致的理解。本文深入研究了机器人LRS工作空间分析的复杂性，说明了医学成像、CAD软件和外科机器人之间的无缝协作。通过这种跨学科的方法，这项研究旨在超越传统的手术方法，为在复杂的骨盆环境中优化机器人干预的范式转变提供新的见解。 et.al.|[2402.14386](http://arxiv.org/abs/2402.14386)|null|
|**2024-02-22**|**MVD $^2$: Efficient Multiview 3D Reconstruction for Multiview Diffusion**|多视点扩散（MVD）作为一种很有前途的三维生成技术，由于其在可推广性、质量和效率方面的优势而受到广泛关注。通过用3D数据微调预训练的大图像扩散模型，MVD方法首先基于图像或文本提示生成3D对象的多个视图，然后用多视图3D重建来重建3D形状。然而，生成的图像中的稀疏视图和不一致的细节使得3D重建具有挑战性。我们提出了一种有效的多视点扩散（MVD）图像三维重建方法MVD$^2$。MVD$^2$通过投影和卷积将图像特征聚合为3D特征体积，然后将体积特征解码为3D网格。我们使用3D形状集合和由3D形状的渲染视图提示的MVD图像来训练MVD$^2$。为了解决生成的多视点图像和3D形状的真实视图之间的差异，我们设计了一种简单而有效的视图相关训练方案。MVD$^2$提高了MVD的3D生成质量，并且对各种MVD方法快速且稳健。经过训练后，它可以在一秒内有效地从多视点图像中解码3D网格。我们使用Zero-123++和ObjectVerse LVIS 3D数据集训练MVD$^2$ ，并展示了其在使用合成图像和真实图像作为提示，从不同MVD方法生成的多视点图像生成3D模型方面的卓越性能。 et.al.|[2402.14253](http://arxiv.org/abs/2402.14253)|null|
|**2024-02-20**|**MVDiffusion++: A Dense High-resolution Multi-view Diffusion Model for Single or Sparse-view 3D Object Reconstruction**|本文提出了一种用于3D对象重建的神经结构MVDiffusion++，该结构在给定一张或几张没有相机姿势的图像的情况下合成对象的密集和高分辨率视图。MVDiffusion++通过两个令人惊讶的简单想法实现了卓越的灵活性和可扩展性：1）“无姿势架构”，其中2D潜在特征之间的标准自关注在任意数量的条件视图和生成视图中学习3D一致性，而无需显式使用相机姿势信息；和2）一种“视图丢弃策略”，在训练期间丢弃大量输出视图，这减少了训练时间内存占用，并在测试时实现了密集和高分辨率的视图合成。我们使用Ob厌恶对象进行训练，使用谷歌扫描对象进行评估，并使用标准的新视图合成和3D重建指标，其中MVDiffusion++显著优于当前的技术状态。我们还通过将MVDiffusion++与文本到图像生成模型相结合，展示了一个文本到3D应用程序示例。 et.al.|[2402.12712](http://arxiv.org/abs/2402.12712)|null|
|**2024-02-19**|**Real-time 3D Semantic Scene Perception for Egocentric Robots with Binocular Vision**|在室内移动时感知具有多个对象的三维（3D）场景对于基于视觉的移动机器人至关重要，尤其是对于增强其操作任务而言。在这项工作中，我们为具有双目视觉的以自我为中心的机器人提出了一种具有实例分割、特征匹配和点集配准的端到端流水线，并通过所提出的流水线展示了机器人的抓取能力。首先，我们设计了一种用于单视图3D语义场景分割的基于RGB图像的分割方法，利用2D数据集中的常见对象类，通过相应的深度图将3D点封装到对象实例的点云中。接下来，基于来自先前步骤的RGB图像中的感兴趣对象之间的匹配关键点来提取两个连续分割的点云的3D对应关系。此外，为了了解3D特征分布的空间变化，我们还使用核密度估计（KDE）基于估计的分布对每个3D点对进行加权，这随后在解决点云之间的刚性变换的同时，提供了具有较少中心对应性的鲁棒性。最后，我们在安装了Intel RealSense D435i RGB-D相机的7自由度双臂Baxter机器人上测试了我们提出的管道。结果表明，我们的机器人可以分割感兴趣的对象，在移动时配准多个视图，并抓住目标对象。源代码位于https://github.com/mkhangg/semantic_scene_perception. et.al.|[2402.11872](http://arxiv.org/abs/2402.11872)|**[link](https://github.com/mkhangg/semantic_scene_perception)**|
|**2024-02-18**|**A Robust Error-Resistant View Selection Method for 3D Reconstruction**|为了解决在运动结构（SFM）视图选择中选择具有小相机基线的视图导致三角测量不确定性增加的问题，本文提出了一种稳健的抗误差视图选择方法。该方法利用基于三角测量的计算来获得抗误差模型，然后用于构建抗误差矩阵。抗误差矩阵中每行的排序结果确定每个视图的候选视图集。通过遍历所有视图的候选视图集，并基于容错矩阵完成缺失的视图，确保了三维重建的完整性。根据重建结果中的平均重投影误差和绝对轨迹误差，将该方法与COLMAP程序中精度最高的穷举方法进行了实验比较。所提出的方法在TUM数据集和DTU数据集上的重投影误差精度平均降低了29.40%，绝对轨迹误差平均降低了5.07%。 et.al.|[2402.11431](http://arxiv.org/abs/2402.11431)|null|
|**2024-02-17**|**Dense Matchers for Dense Tracking**|光流是各种应用的有用输入，包括3D重建、姿态估计、跟踪和运动结构。尽管它很有用，但密集的长期跟踪领域，特别是在宽基线上，尚未得到广泛探索。本文扩展了MFT提出的在对数间隔上组合多个光流的概念。我们展示了MFT与不同光流网络的兼容性，产生的结果超过了它们各自的性能。此外，我们在MFT框架内提出了这些网络的简单而有效的组合。在位置预测精度方面，这种方法被证明与更复杂的非因果方法具有竞争力，突出了MFT在增强长期跟踪应用方面的潜力。 et.al.|[2402.11287](http://arxiv.org/abs/2402.11287)|null|
|**2024-02-17**|**DiffPoint: Single and Multi-view Point Cloud Reconstruction with ViT Based Diffusion Model**|随着二维到三维重建的任务在各种现实场景中获得了极大的关注，能够生成高质量的点云变得至关重要。尽管最近深度学习模型在生成点云方面取得了成功，但由于图像和点云之间的差异，在生成高保真度结果方面仍然存在挑战。虽然视觉变换器（ViT）和扩散模型在各种视觉任务中显示出了前景，但它们在从图像重建点云方面的好处尚未得到证明。在本文中，我们首先提出了一种称为DiffPoint的简洁而强大的架构，该架构将ViT和扩散模型相结合，用于点云重建任务。在每个扩散步骤，我们将有噪声的点云划分为不规则的斑块。然后，使用将所有输入视为标记（包括时间信息、图像嵌入和噪声补丁）的标准ViT主干，我们训练我们的模型以基于输入图像预测目标点。我们在单视图和多视图重建任务上对DiffPoint进行了评估，并取得了最先进的结果。此外，我们还引入了一个统一灵活的特征融合模块，用于聚合来自单个或多个输入图像的图像特征。此外，我们的工作证明了跨语言和图像应用统一架构以改进3D重建任务的可行性。 et.al.|[2402.11241](http://arxiv.org/abs/2402.11241)|null|
|**2024-02-15**|**Evaluating NeRFs for 3D Plant Geometry Reconstruction in Field Conditions**|我们评估了不同的神经辐射场（NeRF）技术，用于在从室内环境到室外环境的不同环境中重建（3D）植物。传统技术往往难以捕捉植物的复杂细节，这对植物学和农业理解至关重要。我们评估了三种日益复杂的场景，并将结果与使用激光雷达作为地面实况数据获得的点云进行了比较。在最现实的现场场景中，NeRF模型在GPU上进行30分钟的训练，获得了74.65%的F1成绩，突出了NeRF在具有挑战性的环境中的效率和准确性。这些发现不仅证明了NeRF在详细逼真的3D植物建模中的潜力，而且为提高3D重建过程的速度和效率提供了实用的方法。 et.al.|[2402.10344](http://arxiv.org/abs/2402.10344)|null|
|**2024-02-15**|**GES: Generalized Exponential Splatting for Efficient Radiance Field Rendering**|3D高斯散射的进步显著加速了3D重建和生成。然而，它可能需要大量的高斯，这会产生大量的内存占用。本文介绍了GES（Generalized Exponential Splatting），这是一种利用广义指数函数（GEF）对3D场景进行建模的新表示，需要更少的粒子来表示场景，因此在效率上显著优于高斯飞溅方法，并具有基于高斯的实用程序的即插即用替换能力。GES在原理性1D设置和逼真的3D场景中都得到了理论和实证验证。它被证明可以更准确地表示具有尖锐边缘的信号，由于其固有的低通特性，这对高斯人来说通常是具有挑战性的。我们的实证分析表明，GEF在拟合自然发生的信号（如正方形、三角形和抛物线信号）方面优于高斯，从而减少了对增加高斯飞溅的内存占用的广泛拆分操作的需要。借助调频损耗，GES在新的视图合成基准中实现了有竞争力的性能，同时所需的内存存储量不到高斯飞溅的一半，并将渲染速度提高了39%。代码可在项目网站上获得https://abdullahamdi.com/ges . et.al.|[2402.10128](http://arxiv.org/abs/2402.10128)|**[link](https://github.com/ajhamdi/ges-splatting)**|

<p align=right>(<a href=#updated-on-20240226>back to top</a>)</p>

## Diffusion

|Publish Date|Title|Abstract|PDF|Code|
|---|---|---|---|---|
|**2024-02-23**|**Seamless Human Motion Composition with Blended Positional Encodings**|有条件的人体运动生成是一个重要的主题，在虚拟现实、游戏和机器人技术中有许多应用。虽然先前的工作专注于生成由文本、音乐或场景引导的运动，但这些通常会导致局限于短持续时间的孤立运动。相反，我们通过一系列不同的文本描述来处理长的、连续的序列的生成。在这种情况下，我们介绍了FlowMDM，这是第一个基于扩散的模型，它可以在没有任何后处理或冗余去噪步骤的情况下生成无缝的人体运动合成（HMC）。为此，我们介绍了混合位置编码，这是一种在去噪链中利用绝对和相对位置编码的技术。更具体地说，全局运动相干性在绝对阶段恢复，而平滑和逼真的过渡在相对阶段建立。因此，我们在Babel和HumanML3D数据集上实现了准确性、真实性和平滑性方面的最先进结果。FlowMDM在每个运动序列仅使用单个描述进行训练时表现出色，这要归功于其以姿势为中心的交叉注意力，这使其在推理时对不同的文本描述具有鲁棒性。最后，为了解决现有HMC度量的局限性，我们提出了两个新的度量：峰值抖动和抖动下面积，以检测突变。 et.al.|[2402.15509](http://arxiv.org/abs/2402.15509)|null|
|**2024-02-23**|**Gen4Gen: Generative Data Pipeline for Generative Multi-Concept Composition**|最近的文本到图像扩散模型能够学习和合成包含新颖、个性化概念（例如，他们自己的宠物或特定物品）的图像，只需几个训练示例。本文解决了个性化文本到图像扩散模型领域中的两个相互关联的问题。首先，当前的个性化技术无法可靠地扩展到多个概念——我们假设这是由于预训练数据集中复杂场景和简单文本描述之间的不匹配（例如，LAION）。其次，给定一个包含多个个性化概念的图像，缺乏一个整体指标来评估性能，该指标不仅评估个性化概念的相似程度，还评估图像中是否存在所有概念，以及图像是否准确反映了整个文本描述。为了解决这些问题，我们介绍了Gen4Gen，这是一个半自动化的数据集创建管道，利用生成模型将个性化概念与文本描述结合到复杂的组合中。使用它，我们创建了一个名为MyCanvas的数据集，该数据集可用于对多概念个性化任务进行基准测试。此外，我们设计了一个包括两个分数（CP-CLIP和TI-CLIP）的综合指标，以更好地量化多概念个性化文本到图像扩散方法的性能。我们提供了一个简单的基线，建立在自定义扩散的基础上，并提供了经验提示策略，供未来的研究人员在MyCanvas上进行评估。我们表明，通过提高数据质量和提示策略，我们可以显著提高多概念个性化图像生成质量，而无需对模型架构或训练算法进行任何修改。 et.al.|[2402.15504](http://arxiv.org/abs/2402.15504)|null|
|**2024-02-23**|**Length and Velocity Scales in Protoplanetary Disk Turbulence**|在原行星盘湍流理论中，一个被广泛采用的假设是，最大湍流涡的翻转频率 $\Omega_L$是局部开普勒频率$\Omega_K$。就量化湍流粘度或扩散率的标准无量纲Shakura Sunyaev$\alpha$参数而言，这一假设导致特征长度和速度尺度分别由$\sqrt｛\alpha｝H$和$\sqr｛\aalpha｝c$给出，其中$H$和$c$是局部气体尺度高度和声速。然而，当湍流受到数值强迫或由一些自然过程（如垂直剪切失稳）驱动时，这一假设不适用。在这里，我们探索了$\Omega_L\ge\Omega_K$的更一般的情况，并证明在这些条件下，特征长度和速度尺度分别为$\sqrt｛\alpha/R’｝H$和$\scrt｛\AlphaR’｝c$，其中$R'\equiv\Omega_L/\Omega_K$是Rossby数的两倍。由此得出$\alpha=\alphat/R'$，其中$\sqrt｛\alphat｝c$是湍流速度的均方根平均值。适当考虑到这种效应，自然地解释了在强迫湍流中粒子的剪切盒模拟中产生的粒子尺度高度的降低，并可能有助于解释最近的边缘-盘上观测；还提出了对观测的更一般的含义。对于$R'>1$ ，有效粒子斯托克斯数增加，这对粒子碰撞动力学和生长以及星子的形成都有影响。 et.al.|[2402.15475](http://arxiv.org/abs/2402.15475)|null|
|**2024-02-23**|**Solute transport due to periodic loading in a soft porous material**|在软多孔介质中，变形通过流体流动和孔隙结构重排之间的内在耦合驱动溶质迁移。特别是，由周期性负载驱动的溶质传输在从地下污染物的地质力学到活体组织中营养物传输的生物力学、组织工程支架和生物医学应用的水凝胶的应用中具有重要意义。然而，这一过程的基本特征此前尚未得到系统的研究。在这里，我们在1D模型问题的上下文中填补这个漏洞。我们通过扩展配套研究的结果来做到这一点，在该研究中，我们通过引入和分析由此产生的流体和固体运动对溶质传输的影响，探索了周期性变形的孔隙力学。我们首先通过研究溶质在一个加载循环中对溶质浓度分布的影响，表征了溶质在多孔介质中传输的三种主要机制——平流、分子扩散和流体动力学扩散——的独立作用。接下来，我们将探讨传输参数的影响，展示这些参数如何改变扩散和分散的相对重要性。然后，我们通过考虑一系列加载周期（相对于孔隙弹性时间尺度，从慢到快）和从无穷小到大的振幅来探索加载参数。 et.al.|[2402.15451](http://arxiv.org/abs/2402.15451)|null|
|**2024-02-23**|**ProTIP: Probabilistic Robustness Verification on Text-to-Image Diffusion Models against Stochastic Perturbation**|文本到图像（T2I）扩散模型（DM）在基于简单文本描述生成高质量图像方面表现出了令人印象深刻的能力。然而，正如许多深度学习（DL）模型所常见的那样，DM缺乏鲁棒性。虽然有人试图将T2I DM的鲁棒性评估为一个二进制或最坏情况的问题，但无论何时发现对抗性示例（AE），他们都无法回答模型的总体鲁棒性。在这项研究中，我们首先引入了T2I-DM鲁棒性的概率概念；然后建立一个有效的框架ProTIP，以在统计保证的情况下对其进行评估。主要挑战源于：一）生成过程的高计算成本；以及ii）确定扰动输入是否是AE涉及比较两个输出分布，这与其他DL任务（如分类）相比从根本上更困难，在分类中，AE是在标签的错误预测时识别的。为了应对这些挑战，我们在识别AE的统计测试中使用了具有有效性和徒劳性的序列分析早期停止规则，以及自适应浓度不等式，以在满足验证目标时动态确定“恰好”数量的随机扰动。经验实验验证了ProTIP在常见T2I DM上的有效性和效率。最后，我们展示了ProTIP在常用防御方法排名中的应用。 et.al.|[2402.15429](http://arxiv.org/abs/2402.15429)|**[link](https://github.com/wellzline/protip)**|
|**2024-02-23**|**Dendrites with corners**|建立了能够处理高度各向异性界面的扩散受限晶体生长的相场模型。它使用Willmore正则化，产生有限大小的角。渐近分析表明，对于前进的表面，赫林定律是可恢复的。通过对低各向异性的树枝状生长进行模拟并将结果与文献中的数据进行比较，验证了该模型。该模型可以模拟标准相场模型不适定的高各向异性枝晶。在这种情况下，枝晶侧面的赫林不稳定性和角部正则化之间的相互作用产生Z字形波纹，并导致尖端速度作为各向异性强度的函数的非单调趋势。 et.al.|[2402.15394](http://arxiv.org/abs/2402.15394)|null|
|**2024-02-23**|**Understanding Oversmoothing in Diffusion-Based GNNs From the Perspective of Operator Semigroup Theory**|本文对基于扩散的图神经网络中的过度光滑问题进行了一项新的研究。与现有的基于随机游动分析或粒子系统的方法不同，我们通过算子半群理论来处理这个问题。这个理论框架使我们能够严格证明过度光滑与扩散算子的遍历性有内在联系。这一发现进一步提出了一个普遍而温和的遍历性破坏条件，包括之前提供的各种特定解决方案，从而为缓解基于扩散的GNN中的过度光滑提供了一种更通用且有理论依据的方法。此外，我们对我们的理论进行了概率解释，与先前的工作建立了联系，拓宽了理论视野。我们的实验结果表明，这种遍历性破坏项有效地缓解了由狄利克雷能量测量的过度平滑，同时提高了节点分类任务的性能。 et.al.|[2402.15326](http://arxiv.org/abs/2402.15326)|null|
|**2024-02-23**|**Ubiquitous short-range order in multi-principal element alloys**|近年来，多主元素合金（MPEAs）的研究越来越集中于探索和开发短程有序（SRO）来提高材料性能。然而，人们对SRO的形成及其在MPEA中的精确调节仍知之甚少，这限制了人们对其对材料性能影响的理解，并阻碍了SRO工程的发展。在这里，利用先进的增材制造技术，生产具有广泛冷却速率（高达10^7 K/s）的样品以及一种改进的定量电子显微镜方法，我们对三种CoCrNi基MPEA中的SRO进行了表征，以揭示加工路线和热历史对SRO的作用。令人惊讶的是，无论采用何种工艺和热处理，所有样品都表现出相似的SRO水平，这表明在固化过程中可能会形成普遍的SRO。凝固的原子模拟证实，即使在10^11 K/s的极端冷却速率下，液固界面（凝固前沿）也会出现局部化学有序。这种现象源于过冷液体中原子的快速扩散，这与凝固速率相匹配甚至超过了凝固速率。因此，SRO是大多数MPEA的固有特征，对实验中典型的冷却速率和退火处理的变化不敏感。将热处理与机械变形和辐照等其他策略相结合，可能是利用SRO实现受控材料性能的更有效方法。 et.al.|[2402.15305](http://arxiv.org/abs/2402.15305)|null|
|**2024-02-23**|**Let's Rectify Step by Step: Improving Aspect-based Sentiment Analysis with Diffusion Models**|基于方面的情感分析（ABSA）是预测与文本中已识别的方面相关的情感极性的关键任务。然而，由于用户的口语表达，ABSA中的一个显著挑战在于精确确定方面的边界（开始和结束索引），尤其是对于长方面。我们提出了DiffusionABSA，这是一种为ABSA量身定制的新的扩散模型，它逐步提取各个方面。特别地，DiffusionABSA在训练过程中逐渐向方面项添加噪声，随后学习去噪过程，该过程以相反的方式逐渐恢复这些项。为了估计边界，我们设计了一个通过语法感知的时间注意力机制增强的去噪神经网络，以按时间顺序捕捉方面和周围文本之间的相互作用。在八个基准数据集上进行的实证评估强调了与稳健的基线模型相比，DiffusionABSA提供的令人信服的优势。我们的代码公开于https://github.com/Qlb6x/DiffusionABSA. et.al.|[2402.15289](http://arxiv.org/abs/2402.15289)|**[link](https://github.com/qlb6x/diffusionabsa)**|
|**2024-02-23**|**Generative Modelling with Tensor Train approximations of Hamilton--Jacobi--Bellman equations**|在不确定性量化（UQ）和生成建模（GM）等领域，从概率密度采样是一个常见的挑战。特别是在GM中，根据Ornstein-Uhlenbeck正演过程的对数密度使用逆时间扩散过程是一种流行的采样工具。在Berner等人[2022]中，作者指出，这些对数密度可以通过求解随机最优控制中已知的Hamilton-Jacobi-Bellman（HJB）方程来获得。虽然该HJB方程通常用间接方法处理，如策略迭代和神经网络等黑匣子架构的无监督训练，但我们建议通过直接时间积分来求解HJB方程，使用张量序列（TT）格式表示的压缩多项式进行空间离散化。至关重要的是，这种方法是无样本的，对归一化常数不可知，并且可以避免TT压缩造成的维数灾难。我们提供了HJB方程对张量序列多项式的作用的完整推导，并证明了所提出的时间步长、秩和度自适应积分方法在20维非线性采样任务中的性能。 et.al.|[2402.15285](http://arxiv.org/abs/2402.15285)|null|

<p align=right>(<a href=#updated-on-20240226>back to top</a>)</p>

## NeRF

|Publish Date|Title|Abstract|PDF|Code|
|---|---|---|---|---|
|**2024-02-21**|**Geometry-Informed Neural Networks**|我们引入了几何知情神经网络（GINN）的概念，它包括（i）在几何约束下的学习，（ii）作为适当表示的神经场，以及（iii）为几何任务中经常遇到的不确定系统生成不同的解决方案。值得注意的是，GINN公式不需要训练数据，因此可以被视为纯粹由约束驱动的生成建模。我们添加了一个明确的多样性损失来缓解模式崩溃。我们考虑了几个约束，特别是分量的连通性，我们通过Morse理论将其转化为可微损失。在实验上，我们展示了GINN学习范式在一系列二维和三维场景中的有效性，这些场景的复杂性不断增加。 et.al.|[2402.14009](http://arxiv.org/abs/2402.14009)|null|
|**2024-02-18**|**Pattern Recognition Facilities of Extended Kalman Filtering in Stochastic Neural Fields**|在数学神经科学中，人们特别关注在存在模型不确定性的情况下，由动态神经场（DNF）建模的神经组织中的工作记忆机制。工作记忆设施意味着，由于网络中反复的相互作用，在去除外部刺激后，神经元的活动保持自我维持，并允许系统处理丢失的传感器信息。在我们之前的工作中，我们已经根据传感器提供的不完整数据开发了两种神经膜电位的重建方法。这些方法是在扩展卡尔曼滤波方法中通过使用Euler Maruyama方法和\^{o}-Taylor订单1.5的扩展。它表明\^{o}-Taylor基于EKF的恢复过程比基于Euler Maruyama的替代方案更准确。在传感器信息不完整的情况下，它提高了膜电位重建的质量。本文的目的是研究它们的模式识别功能，即在模型不确定和信息不完整的情况下，模式形成重建的质量。数值实验是以神经组织中出现多个活动区的随机DNF为例提供的。 et.al.|[2402.11551](http://arxiv.org/abs/2402.11551)|null|
|**2024-02-15**|**Reg-NF: Efficient Registration of Implicit Surfaces within Neural Fields**|神经场，即基于坐标的神经网络，最近因隐含地表示场景而广受欢迎。与基于点云等显式表示的经典方法相比，神经场提供了连续的场景表示，能够以紧凑且理想的机器人应用方式表示3D几何结构和外观。然而，有限的现有方法已经研究了通过直接利用这些连续的隐式表示来配准多个神经场。在本文中，我们提出了Reg-NF，这是一种基于神经场的配准，它优化了两个任意神经场之间的相对6-DoF变换，即使这两个场具有不同的比例因子。Reg NF的关键组成部分包括双向配准损失、多视图表面采样和体积符号距离函数（SDF）的利用。我们在一个新的神经场数据集上展示了我们的方法，用于评估配准问题。我们提供了一组详尽的实验和消融研究，以确定我们的方法的性能，同时也讨论了局限性，为研究界在无约束环境中利用神经场的开放挑战提供了未来的方向。 et.al.|[2402.09722](http://arxiv.org/abs/2402.09722)|null|
|**2024-02-12**|**Unsupervised Discovery of Object-Centric Neural Fields**|我们研究从单个图像中推断3D以对象为中心的场景表示。虽然最近的方法在从简单的合成图像中无监督地发现3D对象方面显示出了潜力，但它们未能推广到具有视觉丰富和多样化对象的真实世界场景。这种限制源于它们的对象表示，它将对象的内在属性（如形状和外观）与外在的、以观察者为中心的属性（如3D位置）纠缠在一起。为了解决这一瓶颈，我们提出了以对象为中心的神经场的无监督发现（uOCF）。uOCF专注于学习对象的内在，并分别对外在进行建模。我们的方法显著提高了系统泛化能力，从而能够从稀疏的真实世界图像中无监督地学习高保真的以对象为中心的场景表示。为了评估我们的方法，我们收集了三个新的数据集，包括两个真实的厨房环境。大量实验表明，uOCF能够在无监督的情况下从单个真实图像中发现视觉丰富的对象，从而实现3D对象分割和场景操作等应用。值得注意的是，uOCF演示了对单个真实图像中看不见的物体的零样本泛化。项目页面：https://red-fairy.github.io/uOCF/ et.al.|[2402.07376](http://arxiv.org/abs/2402.07376)|null|
|**2024-02-06**|**Improved Generalization of Weight Space Networks via Augmentations**|在深度权重空间（DWS）中学习，神经网络处理其他神经网络的权重，是一个新兴的研究方向，应用于2D和3D神经领域（INRs、NeRFs），以及对其他类型的神经网络进行推断。不幸的是，权重空间模型往往存在严重的过拟合问题。我们实证分析了这种过拟合的原因，发现一个关键原因是DWS数据集缺乏多样性。虽然给定的对象可以用许多不同的权重配置来表示，但典型的INR训练集无法捕捉表示同一对象的INR之间的可变性。为了解决这一问题，我们探索了在权重空间中增加数据的策略，并提出了一种适用于权重空间的MixUp方法。我们在两个设置中展示了这些方法的有效性。在分类方面，它们可以提高性能，类似于拥有10倍以上的数据。在自我监督的对比学习中，它们在下游分类中产生了5-10%的显著收益。 et.al.|[2402.04081](http://arxiv.org/abs/2402.04081)|null|
|**2024-01-31**|**BlockFusion: Expandable 3D Scene Generation using Latent Tri-plane Extrapolation**|我们介绍了BlockFusion，这是一种基于扩散的模型，它将3D场景生成为单元块，并无缝地合并新的块来扩展场景。BlockFusion使用从完整的3D场景网格中随机裁剪的3D块的数据集进行训练。通过逐块拟合，所有训练块都被转换为混合神经场：具有包含几何特征的三平面，然后是用于解码有符号距离值的多层感知器（MLP）。采用变分自动编码器将三平面压缩到潜在的三平面空间中，在该空间上进行去噪扩散处理。应用于潜在表示的扩散允许高质量和多样化的3D场景生成。要在生成过程中扩展场景，只需附加空块以与当前场景重叠，并外推现有的潜在三平面以填充新块。外推是通过在去噪迭代过程中使用来自重叠三平面的特征样本来调节生成过程来完成的。潜在的三平面外推法产生语义和几何上有意义的过渡，与现有场景和谐融合。2D布局调节机制用于控制场景元素的放置和布置。实验结果表明，BlockFusion能够在室内和室外场景中生成具有前所未有的高质量形状的多样化、几何一致和无边界的大型3D场景。 et.al.|[2401.17053](http://arxiv.org/abs/2401.17053)|null|
|**2024-01-26**|**Learning Neural Radiance Fields of Forest Structure for Scalable and Fine Monitoring**|这项工作利用神经辐射场和遥感技术用于林业应用。在这里，我们展示了神经辐射场为改进森林监测中现有的遥感方法提供了广泛的可能性。我们提出的实验证明了它们的潜力：（1）表达森林三维结构的精细特征，（2）融合可用的遥感模式，（3）改进三维结构衍生的森林指标。总之，这些特性使神经场成为一种有吸引力的计算工具，具有进一步提高森林监测程序的可扩展性和准确性的巨大潜力。 et.al.|[2401.15029](http://arxiv.org/abs/2401.15029)|null|
|**2024-01-25**|**Learning Robust Generalizable Radiance Field with Visibility and Feature Augmented Point Representation**|本文介绍了广义神经辐射场（NeRF）的一种新范式。以前的通用NeRF方法将多视点立体技术与基于图像的神经渲染相结合进行泛化，产生了令人印象深刻的结果，同时存在三个问题。首先，遮挡常常导致不一致的特征匹配。然后，由于采样点和粗略特征聚合的单独过程，它们在几何不连续性和局部尖锐形状中传递失真和伪影。第三，当源视图离目标视图不够近时，它们基于图像的表示会发生严重退化。为了应对挑战，我们提出了第一个基于点而不是基于图像的渲染构建可泛化神经场的范式，我们称之为可泛化神经点场（GPF）。我们的方法通过几何先验显式地建模可见性，并用神经特征增强它们。我们提出了一种新的非均匀对数采样策略，以提高渲染速度和重建质量。此外，我们提出了一种可学习的内核，该内核在空间上增加了用于特征聚合的特征，减轻了几何结构急剧变化的地方的失真。此外，我们的表现很容易被操纵。实验表明，在泛化和微调设置中，我们的模型可以在三个数据集上提供比所有对应模型和基准更好的几何结构、视图一致性和渲染质量，初步证明了可泛化NeRF新范式的潜力。 et.al.|[2401.14354](http://arxiv.org/abs/2401.14354)|null|
|**2024-01-24**|**Unified neural field theory of brain dynamics underlying oscillations in Parkinson's disease and generalized epilepsies**|通过皮质丘脑基底神经节（CTBG）系统的神经场模型，联合探讨了帕金森病（PD）和全身性癫痫的病理同步神经振荡的机制。基底神经节（BG）被近似为一个单一的有效群体，并分析了它们在调节振荡皮质丘脑（CT）动力学中的作用，反之亦然。除了正常的脑电图节律外，模型中还存在4 Hz和20 Hz左右的增强活动，这与PD的特征频率一致。这些节律是由BG和CT人群之间回路中的共振引起的，类似于先前CT模型中潜在的癫痫振荡。多巴胺耗竭被认为削弱了对PD中这些共振的抑制，网络连接解释了在4-8Hz和20Hz左右BG、丘脑和皮层活动之间的显著一致性。丘脑网状核（TRN）和BG的传入和传出连接位点之间的相似性预测低多巴胺对应于强直-阵挛（大发作）癫痫发作的可能性降低，这与实验结果一致。此外，该模型预测，与实验结果相匹配的低多巴胺水平会增加缺席（轻微）癫痫发作的可能性。与其他CTBG建模研究一致，当传入和传出BG与CT系统的连接增强时，表现出对缺席发作活动的抑制。BG被证明在强直-阵挛发作状态附近抑制CTBG系统的活性，从而深入了解BG回路中目前治疗的疗效。TRN的睡眠状态也被发现可以抑制病理性PD活动匹配观察。总的来说，这些发现证明了广泛性癫痫和帕金森病的相干振荡之间有很强的相似性，并为可能的合并症提供了见解。 et.al.|[2401.13467](http://arxiv.org/abs/2401.13467)|null|
|**2024-01-17**|**Reproducibility via neural fields of visual illusions induced by localized stimuli**|本文研究了Billock和Tsou[PNAS，2007]使用Amari型神经场的可控性对初级视皮层（V1）皮层活动进行建模的实验复制，重点关注中央凹或外周视野中的规则漏斗模式。其目的是理解和模拟在这些实验中观察到的视觉现象，强调其非线性性质。这项研究包括设计模拟Billock和Tsou实验中视觉刺激的感官输入。然后从理论和数值上研究这些输入引起的后图像，以确定它们复制实验观察到的视觉效果的能力。这项研究的一个关键方面是研究神经反应的非线性性质所引起的影响。特别是，通过强调兴奋性和抑制性神经元在某些视觉现象出现中的重要性，这项研究表明，这两种类型的神经元活动的相互作用在视觉过程中发挥着重要作用，挑战了后者主要由兴奋性活动单独驱动的假设。 et.al.|[2401.09108](http://arxiv.org/abs/2401.09108)|null|

<p align=right>(<a href=#updated-on-20240226>back to top</a>)</p>

[contributors-shield]: https://img.shields.io/github/contributors/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[contributors-url]: https://github.com/Vincentqyw/cv-arxiv-daily/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[forks-url]: https://github.com/Vincentqyw/cv-arxiv-daily/network/members
[stars-shield]: https://img.shields.io/github/stars/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[stars-url]: https://github.com/Vincentqyw/cv-arxiv-daily/stargazers
[issues-shield]: https://img.shields.io/github/issues/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[issues-url]: https://github.com/Vincentqyw/cv-arxiv-daily/issues

