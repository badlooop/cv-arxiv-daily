[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]

## Updated on 2024.02.28
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
|**2024-02-26**|**CMC: Few-shot Novel View Synthesis via Cross-view Multiplane Consistency**|神经辐射场（NeRF）由于其连续表示场景的能力，在新颖的视图合成中，特别是在虚拟现实（VR）和增强现实（AR）中，显示出了令人印象深刻的结果。然而，当只有几个输入视图图像可用时，NeRF倾向于过度拟合给定视图，从而使像素的估计深度共享几乎相同的值。与以前通过引入复杂的先验或额外的监督来进行正则化的方法不同，我们提出了一种简单而有效的方法，该方法明确地在输入视图之间建立深度感知一致性，以应对这一挑战。我们的关键见解是，通过强制在不同的输入视图中重复采样相同的空间点，我们能够加强视图之间的相互作用，从而缓解过拟合问题。为了实现这一点，我们在分层表示（\textit｛即｝多平面图像）上建立神经网络，因此可以在多个离散平面上对采样点进行重新采样。此外，为了正则化看不见的目标视图，我们将不同输入视图的渲染颜色和深度约束为相同。尽管简单，但大量的实验表明，与最先进的方法相比，我们提出的方法可以获得更好的合成质量。 et.al.|[2402.16407](http://arxiv.org/abs/2402.16407)|null|
|**2024-02-26**|**FrameNeRF: A Simple and Efficient Framework for Few-shot Novel View Synthesis**|我们提出了一种新的框架，称为FrameNeRF，旨在将现成的快速高保真NeRF模型应用于少镜头的新颖视图合成任务，该模型具有快速训练速度和高渲染质量。快速高保真度模型的训练稳定性通常局限于密集视图，这使得它们不适合于少镜头的新颖视图合成任务。为了解决这一限制，我们利用正则化模型作为数据生成器，从稀疏输入中生成密集视图，从而促进快速高保真模型的后续训练。由于这些密集视图是由正则化模型生成的伪地面实况，因此使用原始稀疏图像来微调快速高保真度模型。这个过程有助于模型学习真实的细节，并更正早期阶段引入的工件。通过利用现成的正则化模型和快速高保真度模型，我们的方法在各种基准数据集上实现了最先进的性能。 et.al.|[2402.14586](http://arxiv.org/abs/2402.14586)|null|
|**2024-02-22**|**TaylorGrid: Towards Fast and High-Quality Implicit Field Learning via Direct Taylor-based Grid Optimization**|基于坐标的神经隐式表示或隐式场已被广泛研究用于3D几何表示或新颖视图合成。近年来，人们致力于加快基于坐标的内隐场学习的速度和提高其质量。代替学习重MLP来预测查询坐标的神经隐式值，已经提出了与浅MLP相结合的神经体素或网格来实现具有减少的优化时间的高质量隐式场学习。另一方面，为了进一步提高学习速度，已经提出了诸如线性网格之类的轻量级场表示。在本文中，我们的目标是快速和高质量的隐场学习，并提出了TaylorGrid，这是一种新的隐场表示，可以在2D或3D网格上通过直接泰勒展开优化有效地计算。一般来说，TaylorGrid可以适用于不同的内隐场学习任务，如SDF学习或NeRF。通过广泛的定量和定性比较，TaylorGrid实现了线性网格和神经体素之间的平衡，显示了其在快速和高质量的内隐场学习中的优势。 et.al.|[2402.14415](http://arxiv.org/abs/2402.14415)|null|
|**2024-02-20**|**Improving Robustness for Joint Optimization of Camera Poses and Decomposed Low-Rank Tensorial Radiance Fields**|在本文中，我们提出了一种算法，该算法允许仅使用2D图像作为监督，对由分解的低秩张量表示的相机姿态和场景几何进行联合细化。首先，我们基于1D信号进行了一项试点研究，并将我们的发现与3D场景联系起来，在3D场景中，基于体素的NeRF上的初始关节姿态优化可以很容易地导致次优解。此外，基于频谱分析，我们建议在2D和3D辐射场上应用卷积高斯滤波器，以实现从粗到细的训练计划，从而实现联合相机姿态优化。利用分解后的低秩张量中的分解特性，我们的方法实现了与强力3D卷积等效的效果，只需很少的计算开销。为了进一步提高联合优化的鲁棒性和稳定性，我们还提出了平滑的2D监督、随机缩放的核参数和边缘引导的损失掩模技术。广泛的定量和定性评估表明，我们提出的框架在新的视图合成方面取得了卓越的性能，并实现了快速收敛的优化。 et.al.|[2402.13252](http://arxiv.org/abs/2402.13252)|**[link](https://github.com/nemo1999/joint-tensorf)**|
|**2024-02-20**|**Real-time High-resolution View Synthesis of Complex Scenes with Explicit 3D Visibility Reasoning**|绘制复杂场景的照片逼真的新颖视图图像一直是计算机图形学中的一个长期挑战。近年来，在视图合成领域，在提高渲染质量和加快渲染速度方面取得了很大的研究进展。然而，当使用稀疏视图渲染复杂的动态场景时，由于遮挡问题，渲染质量仍然有限。此外，对于在动态场景中渲染高分辨率图像，渲染速度仍远未达到实时性。在这项工作中，我们提出了一种可推广的视图合成方法，该方法可以从稀疏视图实时渲染复杂静态和动态场景的高分辨率新视图图像。为了解决由输入视图的稀疏性和捕获场景的复杂性引起的遮挡问题，我们引入了一种显式3D可见性推理方法，该方法可以有效地估计采样的3D点对输入视图的可见性。所提出的可见性推理方法是完全可微分的，可以很好地适应体绘制管道，使我们能够在训练网络时只使用多视图图像作为监督，同时细化几何体和纹理。此外，我们管道中的每个模块都经过精心设计，以绕过耗时的MLP查询过程，提高高分辨率图像的渲染质量，使我们能够实时渲染高分辨率的新视图图像。实验结果表明，我们的方法在渲染质量和速度上都优于以前的视图合成方法，尤其是在处理具有稀疏视图的复杂动态场景时。 et.al.|[2402.12886](http://arxiv.org/abs/2402.12886)|null|
|**2024-02-20**|**MVDiffusion++: A Dense High-resolution Multi-view Diffusion Model for Single or Sparse-view 3D Object Reconstruction**|本文提出了一种用于3D对象重建的神经结构MVDiffusion++，该结构在给定一张或几张没有相机姿势的图像的情况下合成对象的密集和高分辨率视图。MVDiffusion++通过两个令人惊讶的简单想法实现了卓越的灵活性和可扩展性：1）“无姿势架构”，其中2D潜在特征之间的标准自关注在任意数量的条件视图和生成视图中学习3D一致性，而无需显式使用相机姿势信息；和2）一种“视图丢弃策略”，在训练期间丢弃大量输出视图，这减少了训练时间内存占用，并在测试时实现了密集和高分辨率的视图合成。我们使用Ob厌恶对象进行训练，使用谷歌扫描对象进行评估，并使用标准的新视图合成和3D重建指标，其中MVDiffusion++显著优于当前的技术状态。我们还通过将MVDiffusion++与文本到图像生成模型相结合，展示了一个文本到3D应用程序示例。 et.al.|[2402.12712](http://arxiv.org/abs/2402.12712)|null|
|**2024-02-19**|**Binary Opacity Grids: Capturing Fine Geometric Detail for Mesh-Based View Synthesis**|虽然基于表面的视图合成算法由于其低计算要求而很有吸引力，但它们往往难以再现薄结构。相比之下，将场景的几何体建模为体积密度场（例如NeRF）的更昂贵的方法擅长于重建精细的几何细节。然而，密度场通常以“模糊”的方式表示几何体，这阻碍了曲面的精确定位。在这项工作中，我们修改了密度场，以鼓励它们向表面会聚，而不影响它们重建薄结构的能力。首先，我们使用离散的不透明度网格表示，而不是连续的密度场，这允许不透明度值在曲面上从零不连续地过渡到一。其次，我们通过每个像素投射多条光线来消除混叠，这允许在不使用半透明体素的情况下对遮挡边界和亚像素结构进行建模。第三，我们最小化不透明度值的二元熵，这通过鼓励不透明度值在训练结束时进行二元化来促进表面几何的提取。最后，我们开发了一种基于融合的网格划分策略，然后进行网格简化和外观模型拟合。与现有的基于网格的方法相比，我们的模型生成的紧凑网格可以在移动设备上实时渲染，并实现显著更高的视图合成质量。 et.al.|[2402.12377](http://arxiv.org/abs/2402.12377)|null|
|**2024-02-15**|**GES: Generalized Exponential Splatting for Efficient Radiance Field Rendering**|3D高斯散射的进步显著加速了3D重建和生成。然而，它可能需要大量的高斯，这会产生大量的内存占用。本文介绍了GES（Generalized Exponential Splatting），这是一种利用广义指数函数（GEF）对3D场景进行建模的新表示，需要更少的粒子来表示场景，因此在效率上显著优于高斯飞溅方法，并具有基于高斯的实用程序的即插即用替换能力。GES在原理性1D设置和逼真的3D场景中都得到了理论和实证验证。它被证明可以更准确地表示具有尖锐边缘的信号，由于其固有的低通特性，这对高斯人来说通常是具有挑战性的。我们的实证分析表明，GEF在拟合自然发生的信号（如正方形、三角形和抛物线信号）方面优于高斯，从而减少了对增加高斯飞溅的内存占用的广泛拆分操作的需要。借助调频损耗，GES在新的视图合成基准中实现了有竞争力的性能，同时所需的内存存储量不到高斯飞溅的一半，并将渲染速度提高了39%。代码可在项目网站上获得https://abdullahamdi.com/ges . et.al.|[2402.10128](http://arxiv.org/abs/2402.10128)|**[link](https://github.com/ajhamdi/ges-splatting)**|
|**2024-02-14**|**PC-NeRF: Parent-Child Neural Radiance Fields Using Sparse LiDAR Frames in Autonomous Driving Environments**|大规模的3D场景重建和新颖的视图合成对于自动驾驶汽车至关重要，尤其是利用时间稀疏的激光雷达帧。然而，传统的显式表示仍然是以无限分辨率表示重建和合成场景的一个重要瓶颈。尽管最近开发的神经辐射场（NeRF）在隐式表示中显示出令人信服的结果，但使用稀疏激光雷达帧进行大规模3D场景重建和新的视图合成的问题仍未得到探索。为了弥补这一差距，我们提出了一种3D场景重建和新的视图合成框架，称为父子神经辐射场（PC NeRF）。该框架基于父NeRF和子NeRF两个模块，实现了分层空间划分和多级场景表示，包括场景、分段和点级别。多级场景表示增强了稀疏激光雷达点云数据的有效利用，并能够快速获取近似体积场景表示。经过大量实验，PC NeRF被证明可以在大规模场景中实现高精度的新型激光雷达视图合成和三维重建。此外，PC NeRF可以有效地处理稀疏激光雷达帧的情况，并在有限的训练时期内表现出较高的部署效率。我们的方法实施和预先培训的模型可在https://github.com/biter0088/pc-nerf. et.al.|[2402.09325](http://arxiv.org/abs/2402.09325)|**[link](https://github.com/biter0088/pc-nerf)**|
|**2024-02-11**|**BioNeRF: Biologically Plausible Neural Radiance Fields for View Synthesis**|本文介绍了BioNeRF，这是一种生物学上合理的架构，它以3D表示对场景进行建模，并通过辐射场合成新的视图。由于NeRF依赖于网络权重来存储场景的三维表示，BioNeRF实现了一种受认知启发的机制，该机制将来自多个来源的输入融合到类似记忆的结构中，提高了存储容量，并提取了更多内在和相关的信息。BioNeRF还模拟了在锥体细胞中观察到的与上下文信息有关的行为，其中记忆作为上下文提供，并与两个后续神经模型的输入相结合，一个负责产生体积密度，另一个负责渲染场景所用的颜色。实验结果表明，BioNeRF在两个数据集（真实世界图像和合成数据）中对人类感知进行编码的质量测量方面优于最先进的结果。 et.al.|[2402.07310](http://arxiv.org/abs/2402.07310)|**[link](https://github.com/leandropassosjr/bionerf)**|

<p align=right>(<a href=#updated-on-20240228>back to top</a>)</p>

## 3D Reconstruction

|Publish Date|Title|Abstract|PDF|Code|
|---|---|---|---|---|
|**2024-02-26**|**Self Supervised Correlation-based Permutations for Multi-View Clustering**|融合来自不同模式的信息可以增强数据分析任务，包括聚类。然而，现有的多视图聚类（MVC）解决方案仅限于特定领域，或者依赖于次优且计算要求高的两阶段表示和聚类过程。我们提出了一种基于端到端深度学习的通用数据（图像、表格等）MVC框架。我们的方法包括使用一个新的基于排列的正则相关目标来学习有意义的融合数据表示。同时，我们通过在多个视图中识别一致的伪标签来学习集群分配。我们使用十个MVC基准数据集展示了我们的模型的有效性。从理论上讲，我们证明了我们的模型近似于监督线性判别分析（LDA）表示。此外，我们还提供了由伪标签注释引起的错误边界。 et.al.|[2402.16383](http://arxiv.org/abs/2402.16383)|null|
|**2024-02-26**|**DreamUp3D: Object-Centric Generative Models for Single-View 3D Scene Understanding and Real-to-Sim Transfer**|机器人应用的3D场景理解呈现出一组独特的要求，包括实时推理、以对象为中心的潜在表示学习、精确的6D姿态估计和对象的3D重建。当前的场景理解方法通常依赖于训练的模型与显式或学习的体积表示的组合，所有这些方法都有自己的缺点和局限性。我们介绍了DreamUp3D，这是一种新颖的以对象为中心的生成模型（OCGM），专门设计用于对仅由单个RGB-D图像通知的3D场景执行推理。DreamUp3D是一个端到端训练的自监督模型，能够分割对象，提供3D对象重建，生成以对象为中心的潜在表示和精确的每个对象6D姿势估计。在一系列任务中，我们将DreamUp3D与基线进行了比较，包括NeRF、预训练的CLIP特征、ObSurf和ObPose，包括3D场景重建、对象匹配和对象姿态估计。我们的实验表明，我们的模型在现实世界场景中显著优于所有基线，这表明它适用于3D场景理解任务，同时满足机器人应用中的严格要求。 et.al.|[2402.16308](http://arxiv.org/abs/2402.16308)|null|
|**2024-02-25**|**GenNBV: Generalizable Next-Best-View Policy for Active 3D Reconstruction**|尽管神经辐射领域的最新进展使大规模场景的数字化变得现实，但图像捕获过程仍然耗时耗力。以前的工作试图使用次最佳视图（NBV）策略自动进行主动三维重建。然而，现有的NBV策略在很大程度上依赖于手工制定的标准、有限的动作空间或每场景优化的表示。这些约束限制了其跨数据集的可推广性。为了克服这些问题，我们提出了GenNBV，一种端到端可推广的NBV策略。我们的策略采用了基于强化学习（RL）的框架，并将典型的有限动作空间扩展到5D自由空间。它使我们的代理无人机能够从任何角度进行扫描，甚至在训练过程中与看不见的几何形状进行交互。为了提高跨数据集的可推广性，我们还提出了一种新的多源状态嵌入，包括几何、语义和动作表示。我们使用Isaac Gym模拟器与House3K和OmniObject3D数据集建立了一个基准，以评估该NBV策略。实验表明，我们的策略在这些数据集中对看不见的建筑规模对象的覆盖率分别达到98.26%和97.12%，优于先前的解决方案。 et.al.|[2402.16174](http://arxiv.org/abs/2402.16174)|null|
|**2024-02-24**|**A Generative Machine Learning Model for Material Microstructure 3D Reconstruction and Performance Evaluation**|从二维切片重建三维微观结构被认为在预测材料的空间结构和物理性质方面具有重要价值。从当前的技术角度来看，从2D到3D的尺寸扩展被视为一个极具挑战性的反问题。近年来，基于生成对抗性网络的方法得到了广泛的关注。然而，它们仍然受到许多限制的阻碍，包括模型过于简化、需要大量的训练样本，以及在训练过程中难以实现模型收敛。有鉴于此，提出了一种新的生成模型，该模型将U-net的多尺度特性与GAN的生成能力相结合。基于此，创新构建多尺度通道聚合模块、多尺度层次特征聚合模块和卷积块注意力机制，可以更好地捕捉材料微观结构的特性，提取图像信息。通过将图像正则化损失与Wasserstein距离损失相结合，进一步提高了模型的精度。此外，本研究利用各向异性指数准确区分图像的性质，可以清楚地确定图像的各向同性和各向异性。这也是首次评估来自不同领域的材料样本的生成质量，并比较模型本身的性能。实验结果表明，该模型不仅在生成的三维结构和真实样本之间显示出非常高的相似性，而且在统计数据分析方面与真实数据高度一致。 et.al.|[2402.15815](http://arxiv.org/abs/2402.15815)|null|
|**2024-02-22**|**Cameras as Rays: Pose Estimation via Ray Diffusion**|估计相机姿态是3D重建的一项基本任务，并且在稀疏视图（<10）的情况下仍然具有挑战性。与现有的对相机外部全局参数化进行自上而下预测的方法不同，我们提出了一种相机姿态的分布式表示，将相机视为一束光线。该表示允许与空间图像特征的紧密耦合，从而提高姿态精度。我们观察到，这种表示自然适合于设置级别的变换器，并开发了一种基于回归的方法，将图像块映射到相应的射线。为了捕捉稀疏视图姿态推断中固有的不确定性，我们采用这种方法来学习去噪扩散模型，该模型允许我们对合理的模式进行采样，同时提高性能。我们提出的方法，包括基于回归和扩散的方法，在CO3D上展示了最先进的相机姿态估计性能，同时推广到看不见的物体类别和野外捕捉。 et.al.|[2402.14817](http://arxiv.org/abs/2402.14817)|null|
|**2024-02-22**|**Workspace Analysis for Laparoscopic Rectal Surgery : A Preliminary Study**|医学成像、计算分析和机器人技术的集成为微创外科手术带来了重大变革，尤其是在腹腔镜直肠手术（LRS）领域。这种专门的外科技术旨在解决直肠癌症，需要深入理解骨盆狭窄空间内的空间动力学。本研究利用磁共振成像（MRI）扫描作为基础数据集，将其纳入计算机辅助设计（CAD）软件，以生成患者解剖结构的精确三维（3D）重建。这项研究的核心是对手术工作空间的分析，这是机器人干预优化的一个关键方面。复杂的计算算法在CAD环境中处理MRI数据，仔细计算骨盆内部区域的尺寸和轮廓。结果是，考虑到曲率、直径变化和潜在障碍等因素，对LRS期间的可行区域和限制区域进行了细致的理解。本文深入研究了机器人LRS工作空间分析的复杂性，说明了医学成像、CAD软件和外科机器人之间的无缝协作。通过这种跨学科的方法，这项研究旨在超越传统的手术方法，为在复杂的骨盆环境中优化机器人干预的范式转变提供新的见解。 et.al.|[2402.14386](http://arxiv.org/abs/2402.14386)|null|
|**2024-02-22**|**MVD $^2$: Efficient Multiview 3D Reconstruction for Multiview Diffusion**|多视点扩散（MVD）作为一种很有前途的三维生成技术，由于其在可推广性、质量和效率方面的优势而受到广泛关注。通过用3D数据微调预训练的大图像扩散模型，MVD方法首先基于图像或文本提示生成3D对象的多个视图，然后用多视图3D重建来重建3D形状。然而，生成的图像中的稀疏视图和不一致的细节使得3D重建具有挑战性。我们提出了一种有效的多视点扩散（MVD）图像三维重建方法MVD$^2$。MVD$^2$通过投影和卷积将图像特征聚合为3D特征体积，然后将体积特征解码为3D网格。我们使用3D形状集合和由3D形状的渲染视图提示的MVD图像来训练MVD$^2$。为了解决生成的多视点图像和3D形状的真实视图之间的差异，我们设计了一种简单而有效的视图相关训练方案。MVD$^2$提高了MVD的3D生成质量，并且对各种MVD方法快速且稳健。经过训练后，它可以在一秒内有效地从多视点图像中解码3D网格。我们使用Zero-123++和ObjectVerse LVIS 3D数据集训练MVD$^2$ ，并展示了其在使用合成图像和真实图像作为提示，从不同MVD方法生成的多视点图像生成3D模型方面的卓越性能。 et.al.|[2402.14253](http://arxiv.org/abs/2402.14253)|null|
|**2024-02-20**|**MVDiffusion++: A Dense High-resolution Multi-view Diffusion Model for Single or Sparse-view 3D Object Reconstruction**|本文提出了一种用于3D对象重建的神经结构MVDiffusion++，该结构在给定一张或几张没有相机姿势的图像的情况下合成对象的密集和高分辨率视图。MVDiffusion++通过两个令人惊讶的简单想法实现了卓越的灵活性和可扩展性：1）“无姿势架构”，其中2D潜在特征之间的标准自关注在任意数量的条件视图和生成视图中学习3D一致性，而无需显式使用相机姿势信息；和2）一种“视图丢弃策略”，在训练期间丢弃大量输出视图，这减少了训练时间内存占用，并在测试时实现了密集和高分辨率的视图合成。我们使用Ob厌恶对象进行训练，使用谷歌扫描对象进行评估，并使用标准的新视图合成和3D重建指标，其中MVDiffusion++显著优于当前的技术状态。我们还通过将MVDiffusion++与文本到图像生成模型相结合，展示了一个文本到3D应用程序示例。 et.al.|[2402.12712](http://arxiv.org/abs/2402.12712)|null|
|**2024-02-19**|**Real-time 3D Semantic Scene Perception for Egocentric Robots with Binocular Vision**|在室内移动时感知具有多个对象的三维（3D）场景对于基于视觉的移动机器人至关重要，尤其是对于增强其操作任务而言。在这项工作中，我们为具有双目视觉的以自我为中心的机器人提出了一种具有实例分割、特征匹配和点集配准的端到端流水线，并通过所提出的流水线展示了机器人的抓取能力。首先，我们设计了一种用于单视图3D语义场景分割的基于RGB图像的分割方法，利用2D数据集中的常见对象类，通过相应的深度图将3D点封装到对象实例的点云中。接下来，基于来自先前步骤的RGB图像中的感兴趣对象之间的匹配关键点来提取两个连续分割的点云的3D对应关系。此外，为了了解3D特征分布的空间变化，我们还使用核密度估计（KDE）基于估计的分布对每个3D点对进行加权，这随后在解决点云之间的刚性变换的同时，提供了具有较少中心对应性的鲁棒性。最后，我们在安装了Intel RealSense D435i RGB-D相机的7自由度双臂Baxter机器人上测试了我们提出的管道。结果表明，我们的机器人可以分割感兴趣的对象，在移动时配准多个视图，并抓住目标对象。源代码位于https://github.com/mkhangg/semantic_scene_perception. et.al.|[2402.11872](http://arxiv.org/abs/2402.11872)|**[link](https://github.com/mkhangg/semantic_scene_perception)**|
|**2024-02-25**|**A Robust Error-Resistant View Selection Method for 3D Reconstruction**|为了解决在运动结构（SFM）视图选择中选择具有小相机基线的视图导致三角测量不确定性增加的问题，本文提出了一种稳健的抗误差视图选择方法。该方法利用基于三角测量的计算来获得抗误差模型，然后用于构建抗误差矩阵。抗误差矩阵中每行的排序结果确定每个视图的候选视图集。通过遍历所有视图的候选视图集，并基于容错矩阵完成缺失的视图，确保了三维重建的完整性。根据重建结果中的平均重投影误差和绝对轨迹误差，将该方法与COLMAP程序中精度最高的穷举方法进行了实验比较。所提出的方法在TUM数据集和DTU数据集上的重投影误差精度平均降低了29.40%，绝对轨迹误差平均降低了5.07%。 et.al.|[2402.11431](http://arxiv.org/abs/2402.11431)|null|

<p align=right>(<a href=#updated-on-20240228>back to top</a>)</p>

## Diffusion

|Publish Date|Title|Abstract|PDF|Code|
|---|---|---|---|---|
|**2024-02-27**|**Stochastic Conditional Diffusion Models for Semantic Image Synthesis**|语义图像合成（SIS）是生成与语义图（标签）相对应的真实图像的任务。它可以应用于不同的现实世界实践，如照片编辑或内容创建。然而，在现实应用中，SIS经常遇到嘈杂的用户输入。为了解决这一问题，我们提出了随机条件扩散模型（SCDM），这是一种稳健的条件扩散模型，具有为带有噪声标签的SIS量身定制的新的前向和生成过程。它通过标签扩散随机干扰语义标签图来增强鲁棒性，标签扩散以离散扩散的方式扩散标签。通过标签的扩散，随着时间步长的增加，嘈杂和干净的语义图变得相似，最终在 $t=t$ 时变得相同。这有助于生成接近干净图像的图像，从而实现稳健的生成。此外，我们提出了一种按类别的噪声调度，以根据类别差异地扩散标签。我们证明，所提出的方法通过在基准数据集上进行广泛的实验和分析来生成高质量的样本，包括模拟真实世界应用中人为错误的新实验设置。 et.al.|[2402.16506](http://arxiv.org/abs/2402.16506)|null|
|**2024-02-26**|**Outline-Guided Object Inpainting with Diffusion Models**|实例分割数据集在训练准确和稳健的计算机视觉模型方面发挥着至关重要的作用。然而，获得准确的掩码注释以生成高质量的分割数据集是一个成本高昂且劳动密集的过程。在这项工作中，我们展示了如何通过从小型带注释的实例分割数据集开始，并对其进行扩充，以有效地获得相当大的带注释的数据集，来缓解这一问题。我们通过以保留所提供的掩码注释的方式创建可用注释对象实例的变体来实现这一点，从而导致将新的图像掩码对添加到注释图像集。具体来说，我们使用基于扩散的修复模型来生成新的图像，通过引导扩散穿过对象轮廓，用所需的对象类别填充掩模区域。我们表明，对象轮廓为底层修复模型提供了一个简单但可靠且方便的无训练指导信号，该信号通常足以在没有进一步文本指导的情况下用正确类别的对象填充掩模，并以高精度保持生成的图像与掩模注释之间的对应关系。我们的实验结果表明，我们的方法成功地生成了对象实例的真实变化，保留了它们的形状特征，同时在增强区域内引入了多样性。我们还表明，所提出的方法可以自然地与文本引导和其他图像增强技术相结合。 et.al.|[2402.16421](http://arxiv.org/abs/2402.16421)|null|
|**2024-02-26**|**Renormalisation Group Methods for Effective Epidemiological Models**|流行病学模型描述了传染病在人群中的传播。他们捕捉了疾病如何以各种不同方式在个体之间传播的微观细节，同时对整个人群的状态进行了预测。然而，所考虑的特定模型的类型和结构通常取决于所考虑的人口规模。为了分析这种影响，我们研究了一系列有效的流行病学模型，这些模型在空间和时间上通过尺度变换相互关联。受扩散过程类似处理的启发，我们将后者解释为重标准化群变换，无论是在基本微分方程及其解的水平上。我们表明，在大尺度极限下，感染过程的微观细节变得无关紧要，对于一个简单的实数来说是安全的，它在基本的房室模型中起着感染率的作用。 et.al.|[2402.16409](http://arxiv.org/abs/2402.16409)|null|
|**2024-02-26**|**Entropy production for diffusion processes across a semipermeable interface**|随机热力学的新兴领域将熵、热和功的经典思想扩展到非平衡系统。一个值得注意的发现是，热力学第二定律通常只有在对随机轨迹集合取适当的平均值后才成立。由此产生的熵产生的平均速率量化了偏离热力学平衡的程度。在本文中，我们研究了半渗透界面的存在如何增加单个扩散粒子的平均熵产生。从粒子概率密度的吉布斯-香农熵开始，我们表明半渗透界面或膜 $\calS$使平均熵产生率增加了一个量，该量等于通过界面的通量与界面两侧概率密度之比的对数的乘积，沿$\calS$ 积分。熵产生率因此在热力学平衡时消失，但在弛豫到平衡的过程中，或者如果存在非零平稳平衡态（NESS），熵产生率可能是非零的。我们用圆上随机重置的扩散例子来说明后者，并表明界面熵产生的平均速率是重置速率和渗透率的非单调函数。最后，我们使用所谓的弹出布朗运动给出了界面熵产生率的概率解释。这也使我们能够构建熵产生的随机版本。 et.al.|[2402.16403](http://arxiv.org/abs/2402.16403)|null|
|**2024-02-26**|**Quantitative Propagation of Chaos for Mean Field Interacting Particle System**|本文推导了平均场相互作用粒子系统在 $L^\eta$（$\eta\In（0,1）$）-Wasserstein距离中混沌的定量传播，其中扩散系数被允许相互作用，并且相互作用粒子的初始分布收敛于$L^1$ -Wassertein距离中的极限方程的初始分布。分别研究了非退化和退化情况，主要工具依赖于解耦SDE的梯度估计。 et.al.|[2402.16400](http://arxiv.org/abs/2402.16400)|null|
|**2024-02-26**|**Placing Objects in Context via Inpainting for Out-of-distribution Segmentation**|当将语义分割模型部署到现实世界中时，它将不可避免地面临在训练过程中看不到的语义类。因此，为了安全地部署此类系统，准确评估和提高其异常分割能力至关重要。然而，获取和标记语义分割数据是昂贵的，并且出乎意料的情况是长尾的，并且具有潜在的危险性。事实上，现有的异常分割数据集捕获的异常数量有限，缺乏真实性或具有强烈的域偏移。在本文中，我们提出了在上下文中放置对象（POC）管道，以通过扩散模型将任何对象逼真地添加到任何图像中。POC可用于轻松扩展具有任意数量对象的任何数据集。在我们的实验中，我们基于POC生成的数据提供了不同的异常分割数据集，并表明POC可以在几个标准化基准中提高最近最先进的异常微调方法的性能。POC对学习新课程也很有效。例如，我们使用它通过添加Pascal类的子集来编辑Cityscapes样本，并表明在这些数据上训练的模型实现了与Pascal训练的基线相当的性能。这证实了在POC生成的图像上训练的模型的低模拟-真实差距。 et.al.|[2402.16392](http://arxiv.org/abs/2402.16392)|**[link](https://github.com/naver/poc)**|
|**2024-02-26**|**Generative AI in Vision: A Survey on Models, Metrics and Applications**|生成型人工智能模型通过能够创建真实多样的数据样本，彻底改变了各个领域。在这些模型中，扩散模型已成为生成高质量图像、文本和音频的强大方法。这篇调查论文全面概述了生成人工智能扩散和遗留模型，重点介绍了它们的底层技术、不同领域的应用及其挑战。我们深入研究了扩散模型的理论基础，包括去噪扩散概率模型（DDPM）和基于分数的生成模型等概念。此外，我们探索了这些模型在文本到图像、图像修复和图像超分辨率等方面的各种应用，展示了它们在创造性任务和数据扩充方面的潜力。通过综合现有研究并突出该领域的关键进展，这项调查旨在让研究人员和从业者全面了解生成人工智能的传播和遗留模型，并激励未来在人工智能这一令人兴奋的领域进行创新。 et.al.|[2402.16369](http://arxiv.org/abs/2402.16369)|null|
|**2024-02-26**|**Feedback Efficient Online Fine-Tuning of Diffusion Models**|扩散模型擅长模拟复杂的数据分布，包括图像、蛋白质和小分子的数据分布。然而，在许多情况下，我们的目标是对分布中最大化某些特性的部分进行建模：例如，我们可能希望生成具有高美学质量的图像，或具有高生物活性的分子。很自然地，将其定义为强化学习（RL）问题，其中的目标是微调扩散模型，以使与某些属性相对应的奖励函数最大化。即使可以访问基本事实奖励函数的在线查询，有效地发现高奖励样本也可能具有挑战性：它们在初始分布中的概率可能很低，并且可能有许多不可行的样本甚至没有明确的奖励（例如，不自然的图像或物理上不可能的分子）。在这项工作中，我们提出了一种新的强化学习程序，可以有效地探索可行样本的流形。我们提出了一个理论分析，提供了遗憾的保证，以及三个领域的经验验证：图像、生物序列和分子。 et.al.|[2402.16359](http://arxiv.org/abs/2402.16359)|null|
|**2024-02-26**|**Referee Can Play: An Alternative Approach to Conditional Generation via Model Inversion**|作为文本到图像生成任务中的主导力量，扩散概率模型（DPM）在可控性方面面临着关键挑战，难以严格遵守复杂的多方面指令。在这项工作中，我们的目标是解决条件生成任务的这种对齐挑战。首先，我们提供了最先进的DPM的另一种观点，作为反转高级视觉语言模型（VLM）的一种方式。有了这个公式，我们自然提出了一种无需训练的方法，该方法绕过了与DPM相关的传统采样过程。通过在判别VLM的监督下直接优化图像，所提出的方法可以潜在地实现更好的文本图像对齐。作为概念验证，我们用预训练的BLIP-2模型演示了流水线，并确定了改进图像生成的几个关键设计。为了进一步提高图像保真度，引入了稳定扩散的分数蒸馏采样模块。通过在优化过程中仔细平衡这两个组件，我们的方法可以在T2I Compbench上生成性能接近最先进的高质量图像。 et.al.|[2402.16305](http://arxiv.org/abs/2402.16305)|null|
|**2024-02-26**|**Graph Diffusion Policy Optimization**|最近的研究在优化特定下游目标的扩散模型方面取得了重大进展，这是药物设计图生成等领域的重要追求。然而，将这些模型直接应用于图扩散会带来挑战，导致性能不理想。本文介绍了图扩散策略优化（GDPO），这是一种使用强化学习优化任意（例如，不可微）目标的图扩散模型的新方法。GDPO基于为图扩散模型量身定制的热切的策略梯度，通过细致的分析开发，有望提高性能。实验结果表明，GDPO在各种目标复杂多样的图生成任务中都取得了最先进的性能。代码位于https://github.com/sail-sg/GDPO. et.al.|[2402.16302](http://arxiv.org/abs/2402.16302)|**[link](https://github.com/sail-sg/gdpo)**|

<p align=right>(<a href=#updated-on-20240228>back to top</a>)</p>

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

<p align=right>(<a href=#updated-on-20240228>back to top</a>)</p>

[contributors-shield]: https://img.shields.io/github/contributors/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[contributors-url]: https://github.com/Vincentqyw/cv-arxiv-daily/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[forks-url]: https://github.com/Vincentqyw/cv-arxiv-daily/network/members
[stars-shield]: https://img.shields.io/github/stars/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[stars-url]: https://github.com/Vincentqyw/cv-arxiv-daily/stargazers
[issues-shield]: https://img.shields.io/github/issues/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[issues-url]: https://github.com/Vincentqyw/cv-arxiv-daily/issues

