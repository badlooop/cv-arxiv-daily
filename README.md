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
|**2024-02-27**|**AlignMiF: Geometry-Aligned Multimodal Implicit Field for LiDAR-Camera Joint Synthesis**|神经隐式场已经成为新视图合成中事实上的标准。最近，有一些方法探索在一个领域内融合多个模态，旨在共享不同模态的隐含特征，以提高重建性能。然而，这些模态往往表现出错位行为：对一种模态（如激光雷达）进行优化可能会对另一种模态产生不利影响，如相机性能，反之亦然。在这项工作中，我们对激光雷达相机联合合成的多模式隐场进行了全面分析，揭示了潜在的问题在于不同传感器的错位。此外，我们还介绍了AlignMiF，这是一个几何对齐的多模式隐式场，具有两个拟议的模块：几何感知对齐（GAA）和共享几何初始化（SGI）。这些模块有效地调整了不同模态的粗略几何结构，显著增强了激光雷达和相机数据之间的融合过程。通过在各种数据集和场景中进行广泛的实验，我们证明了我们的方法在促进激光雷达和相机模态之间在统一的神经场中更好地交互方面的有效性。具体而言，我们提出的AlignMiF比最近的隐式融合方法（KITTI-360和Waymo数据集上的图像PSNR分别为+2.01和+3.11）实现了显著的改进，并始终超过单模态性能（在各自的数据集上，激光雷达切角距离分别减少了13.8%和14.2%）。 et.al.|[2402.17483](http://arxiv.org/abs/2402.17483)|**[link](https://github.com/tangtaogo/alignmif)**|
|**2024-02-26**|**GEA: Reconstructing Expressive 3D Gaussian Avatar from Monocular Video**|本文提出了GEA，这是一种基于3D高斯的身体和手的高保真重建来创建富有表现力的3D化身的新方法。关键贡献有两方面。首先，我们设计了一种两阶段姿态估计方法，以从输入图像中获得准确的SMPL-X姿态，从而在训练图像的像素和SMPL-X模型之间提供正确的映射。它使用注意力感知网络和优化方案来对齐图像中估计的SMPL-X身体和真实身体之间的法线和轮廓。其次，我们提出了一种迭代重新初始化策略来处理高斯表示所面临的不平衡聚合和初始化偏差。该策略迭代地重新分布化身的高斯点，通过应用网格划分、重采样和重高斯运算，使其均匀分布在人体表面附近。结果，可以实现更高质量的渲染。大量的实验分析验证了所提出的模型的有效性，表明它在逼真的新视图合成中实现了最先进的性能，同时提供了对人体和手部姿势的细粒度控制。项目页面：https://3d-aigc.github.io/GEA/. et.al.|[2402.16607](http://arxiv.org/abs/2402.16607)|null|
|**2024-02-26**|**CMC: Few-shot Novel View Synthesis via Cross-view Multiplane Consistency**|神经辐射场（NeRF）由于其连续表示场景的能力，在新颖的视图合成中，特别是在虚拟现实（VR）和增强现实（AR）中，显示出了令人印象深刻的结果。然而，当只有几个输入视图图像可用时，NeRF倾向于过度拟合给定视图，从而使像素的估计深度共享几乎相同的值。与以前通过引入复杂的先验或额外的监督来进行正则化的方法不同，我们提出了一种简单而有效的方法，该方法明确地在输入视图之间建立深度感知一致性，以应对这一挑战。我们的关键见解是，通过强制在不同的输入视图中重复采样相同的空间点，我们能够加强视图之间的相互作用，从而缓解过拟合问题。为了实现这一点，我们在分层表示（\textit｛即｝多平面图像）上建立神经网络，因此可以在多个离散平面上对采样点进行重新采样。此外，为了正则化看不见的目标视图，我们将不同输入视图的渲染颜色和深度约束为相同。尽管简单，但大量的实验表明，与最先进的方法相比，我们提出的方法可以获得更好的合成质量。 et.al.|[2402.16407](http://arxiv.org/abs/2402.16407)|null|
|**2024-02-26**|**FrameNeRF: A Simple and Efficient Framework for Few-shot Novel View Synthesis**|我们提出了一种新的框架，称为FrameNeRF，旨在将现成的快速高保真NeRF模型应用于少镜头的新颖视图合成任务，该模型具有快速训练速度和高渲染质量。快速高保真度模型的训练稳定性通常局限于密集视图，这使得它们不适合于少镜头的新颖视图合成任务。为了解决这一限制，我们利用正则化模型作为数据生成器，从稀疏输入中生成密集视图，从而促进快速高保真模型的后续训练。由于这些密集视图是由正则化模型生成的伪地面实况，因此使用原始稀疏图像来微调快速高保真度模型。这个过程有助于模型学习真实的细节，并更正早期阶段引入的工件。通过利用现成的正则化模型和快速高保真度模型，我们的方法在各种基准数据集上实现了最先进的性能。 et.al.|[2402.14586](http://arxiv.org/abs/2402.14586)|null|
|**2024-02-22**|**TaylorGrid: Towards Fast and High-Quality Implicit Field Learning via Direct Taylor-based Grid Optimization**|基于坐标的神经隐式表示或隐式场已被广泛研究用于3D几何表示或新颖视图合成。近年来，人们致力于加快基于坐标的内隐场学习的速度和提高其质量。代替学习重MLP来预测查询坐标的神经隐式值，已经提出了与浅MLP相结合的神经体素或网格来实现具有减少的优化时间的高质量隐式场学习。另一方面，为了进一步提高学习速度，已经提出了诸如线性网格之类的轻量级场表示。在本文中，我们的目标是快速和高质量的隐场学习，并提出了TaylorGrid，这是一种新的隐场表示，可以在2D或3D网格上通过直接泰勒展开优化有效地计算。一般来说，TaylorGrid可以适用于不同的内隐场学习任务，如SDF学习或NeRF。通过广泛的定量和定性比较，TaylorGrid实现了线性网格和神经体素之间的平衡，显示了其在快速和高质量的内隐场学习中的优势。 et.al.|[2402.14415](http://arxiv.org/abs/2402.14415)|null|
|**2024-02-20**|**Improving Robustness for Joint Optimization of Camera Poses and Decomposed Low-Rank Tensorial Radiance Fields**|在本文中，我们提出了一种算法，该算法允许仅使用2D图像作为监督，对由分解的低秩张量表示的相机姿态和场景几何进行联合细化。首先，我们基于1D信号进行了一项试点研究，并将我们的发现与3D场景联系起来，在3D场景中，基于体素的NeRF上的初始关节姿态优化可以很容易地导致次优解。此外，基于频谱分析，我们建议在2D和3D辐射场上应用卷积高斯滤波器，以实现从粗到细的训练计划，从而实现联合相机姿态优化。利用分解后的低秩张量中的分解特性，我们的方法实现了与强力3D卷积等效的效果，只需很少的计算开销。为了进一步提高联合优化的鲁棒性和稳定性，我们还提出了平滑的2D监督、随机缩放的核参数和边缘引导的损失掩模技术。广泛的定量和定性评估表明，我们提出的框架在新的视图合成方面取得了卓越的性能，并实现了快速收敛的优化。 et.al.|[2402.13252](http://arxiv.org/abs/2402.13252)|**[link](https://github.com/nemo1999/joint-tensorf)**|
|**2024-02-20**|**Real-time High-resolution View Synthesis of Complex Scenes with Explicit 3D Visibility Reasoning**|绘制复杂场景的照片逼真的新颖视图图像一直是计算机图形学中的一个长期挑战。近年来，在视图合成领域，在提高渲染质量和加快渲染速度方面取得了很大的研究进展。然而，当使用稀疏视图渲染复杂的动态场景时，由于遮挡问题，渲染质量仍然有限。此外，对于在动态场景中渲染高分辨率图像，渲染速度仍远未达到实时性。在这项工作中，我们提出了一种可推广的视图合成方法，该方法可以从稀疏视图实时渲染复杂静态和动态场景的高分辨率新视图图像。为了解决由输入视图的稀疏性和捕获场景的复杂性引起的遮挡问题，我们引入了一种显式3D可见性推理方法，该方法可以有效地估计采样的3D点对输入视图的可见性。所提出的可见性推理方法是完全可微分的，可以很好地适应体绘制管道，使我们能够在训练网络时只使用多视图图像作为监督，同时细化几何体和纹理。此外，我们管道中的每个模块都经过精心设计，以绕过耗时的MLP查询过程，提高高分辨率图像的渲染质量，使我们能够实时渲染高分辨率的新视图图像。实验结果表明，我们的方法在渲染质量和速度上都优于以前的视图合成方法，尤其是在处理具有稀疏视图的复杂动态场景时。 et.al.|[2402.12886](http://arxiv.org/abs/2402.12886)|null|
|**2024-02-20**|**MVDiffusion++: A Dense High-resolution Multi-view Diffusion Model for Single or Sparse-view 3D Object Reconstruction**|本文提出了一种用于3D对象重建的神经结构MVDiffusion++，该结构在给定一张或几张没有相机姿势的图像的情况下合成对象的密集和高分辨率视图。MVDiffusion++通过两个令人惊讶的简单想法实现了卓越的灵活性和可扩展性：1）“无姿势架构”，其中2D潜在特征之间的标准自关注在任意数量的条件视图和生成视图中学习3D一致性，而无需显式使用相机姿势信息；和2）一种“视图丢弃策略”，在训练期间丢弃大量输出视图，这减少了训练时间内存占用，并在测试时实现了密集和高分辨率的视图合成。我们使用Ob厌恶对象进行训练，使用谷歌扫描对象进行评估，并使用标准的新视图合成和3D重建指标，其中MVDiffusion++显著优于当前的技术状态。我们还通过将MVDiffusion++与文本到图像生成模型相结合，展示了一个文本到3D应用程序示例。 et.al.|[2402.12712](http://arxiv.org/abs/2402.12712)|null|
|**2024-02-19**|**Binary Opacity Grids: Capturing Fine Geometric Detail for Mesh-Based View Synthesis**|虽然基于表面的视图合成算法由于其低计算要求而很有吸引力，但它们往往难以再现薄结构。相比之下，将场景的几何体建模为体积密度场（例如NeRF）的更昂贵的方法擅长于重建精细的几何细节。然而，密度场通常以“模糊”的方式表示几何体，这阻碍了曲面的精确定位。在这项工作中，我们修改了密度场，以鼓励它们向表面会聚，而不影响它们重建薄结构的能力。首先，我们使用离散的不透明度网格表示，而不是连续的密度场，这允许不透明度值在曲面上从零不连续地过渡到一。其次，我们通过每个像素投射多条光线来消除混叠，这允许在不使用半透明体素的情况下对遮挡边界和亚像素结构进行建模。第三，我们最小化不透明度值的二元熵，这通过鼓励不透明度值在训练结束时进行二元化来促进表面几何的提取。最后，我们开发了一种基于融合的网格划分策略，然后进行网格简化和外观模型拟合。与现有的基于网格的方法相比，我们的模型生成的紧凑网格可以在移动设备上实时渲染，并实现显著更高的视图合成质量。 et.al.|[2402.12377](http://arxiv.org/abs/2402.12377)|null|
|**2024-02-15**|**GES: Generalized Exponential Splatting for Efficient Radiance Field Rendering**|3D高斯散射的进步显著加速了3D重建和生成。然而，它可能需要大量的高斯，这会产生大量的内存占用。本文介绍了GES（Generalized Exponential Splatting），这是一种利用广义指数函数（GEF）对3D场景进行建模的新表示，需要更少的粒子来表示场景，因此在效率上显著优于高斯飞溅方法，并具有基于高斯的实用程序的即插即用替换能力。GES在原理性1D设置和逼真的3D场景中都得到了理论和实证验证。它被证明可以更准确地表示具有尖锐边缘的信号，由于其固有的低通特性，这对高斯人来说通常是具有挑战性的。我们的实证分析表明，GEF在拟合自然发生的信号（如正方形、三角形和抛物线信号）方面优于高斯，从而减少了对增加高斯飞溅的内存占用的广泛拆分操作的需要。借助调频损耗，GES在新的视图合成基准中实现了有竞争力的性能，同时所需的内存存储量不到高斯飞溅的一半，并将渲染速度提高了39%。代码可在项目网站上获得https://abdullahamdi.com/ges . et.al.|[2402.10128](http://arxiv.org/abs/2402.10128)|**[link](https://github.com/ajhamdi/ges-splatting)**|

<p align=right>(<a href=#updated-on-20240228>back to top</a>)</p>

## 3D Reconstruction

|Publish Date|Title|Abstract|PDF|Code|
|---|---|---|---|---|
|**2024-02-27**|**Sora Generates Videos with Stunning Geometrical Consistency**|最近开发的索拉模型[1]在视频生成方面表现出了非凡的能力，引发了关于其模拟真实世界现象能力的激烈讨论。尽管它越来越受欢迎，但缺乏既定的指标来定量评估它对现实世界物理的保真度。在本文中，我们介绍了一种新的基准，该基准基于视频对真实世界物理原理的遵守程度来评估生成视频的质量。我们采用了一种将生成的视频转换为3D模型的方法，利用了3D重建的准确性在很大程度上取决于视频质量的前提。从3D重建的角度来看，我们使用所构建的3D模型所满足的几何约束的保真度作为代理来衡量生成的视频在多大程度上符合真实世界的物理规则。项目页面：https://sora-geometrical-consistency.github.io/ et.al.|[2402.17403](http://arxiv.org/abs/2402.17403)|null|
|**2024-02-27**|**CharNeRF: 3D Character Generation from Concept Art**|3D建模在AR/VR和游戏领域具有重要意义，既有艺术创意，也有实际应用。然而，这个过程往往很耗时，而且需要很高的技能水平。在本文中，我们提出了一种新的方法，从一致的周转概念艺术中创建3D角色的体积表示，这是3D建模行业的标准输入。虽然神经辐射场（NeRF）已经改变了基于图像的3D重建的游戏规则，但据我们所知，还没有已知的研究可以优化概念艺术的管道。为了利用概念艺术的潜力，通过其定义的身体姿势和特定的视角，我们建议将其编码为我们模型的先验。我们训练网络，通过可学习的视图方向关注的多头自注意层，将这些先验用于各种3D点。此外，我们还证明了射线采样和表面采样的结合增强了我们网络的推理能力。我们的模型能够生成高质量的360度字符视图。随后，我们提供了一个简单的指南，以更好地利用我们的模型来提取3D网格。需要注意的是，我们模型的推理能力受到训练数据特征的影响，主要集中在具有单头、双臂和双腿的角色上。尽管如此，我们的方法仍然是通用的，适用于来自不同主题的概念艺术，而不会对数据强加任何具体的假设。 et.al.|[2402.17115](http://arxiv.org/abs/2402.17115)|null|
|**2024-02-24**|**Reliable Conflictive Multi-View Learning**|多视图学习旨在结合多种特征，实现对数据的更全面描述。以前的大多数工作都假设多个视图是严格对齐的。然而，真实世界的多视图数据可能包含低质量的冲突实例，这些实例在不同的视图中显示冲突信息。以前解决这个问题的方法主要集中在通过删除或替换冲突的视图来消除冲突的数据实例。然而，现实世界中的应用程序通常需要为冲突实例做出决策，而不仅仅是消除它们。为了解决这个问题，我们提出了一个新的可靠冲突多视图学习（RCML）问题，该问题要求模型为冲突多视图数据提供决策结果和附加的可靠性。针对这个问题，我们开发了一种证据冲突多视角学习（ECML）方法。ECML首先学习视图特定的证据，可以称为从数据中收集的对每个类别的支持量。然后，我们可以构建由决策结果和可靠性组成的视图特定意见。在多视图融合阶段，我们提出了一种冲突性的意见聚合策略，并从理论上证明了该策略可以准确地建模多视图公共可靠性和视图特定可靠性的关系。在6个数据集上进行的实验验证了ECML的有效性。 et.al.|[2402.16897](http://arxiv.org/abs/2402.16897)|**[link](https://github.com/jiajunsi/rcml)**|
|**2024-02-26**|**Self Supervised Correlation-based Permutations for Multi-View Clustering**|融合来自不同模式的信息可以增强数据分析任务，包括聚类。然而，现有的多视图聚类（MVC）解决方案仅限于特定领域，或者依赖于次优且计算要求高的两阶段表示和聚类过程。我们提出了一种基于端到端深度学习的通用数据（图像、表格等）MVC框架。我们的方法包括使用一个新的基于排列的正则相关目标来学习有意义的融合数据表示。同时，我们通过在多个视图中识别一致的伪标签来学习集群分配。我们使用十个MVC基准数据集展示了我们的模型的有效性。从理论上讲，我们证明了我们的模型近似于监督线性判别分析（LDA）表示。此外，我们还提供了由伪标签注释引起的错误边界。 et.al.|[2402.16383](http://arxiv.org/abs/2402.16383)|null|
|**2024-02-26**|**DreamUp3D: Object-Centric Generative Models for Single-View 3D Scene Understanding and Real-to-Sim Transfer**|机器人应用的3D场景理解呈现出一组独特的要求，包括实时推理、以对象为中心的潜在表示学习、精确的6D姿态估计和对象的3D重建。当前的场景理解方法通常依赖于训练的模型与显式或学习的体积表示的组合，所有这些方法都有自己的缺点和局限性。我们介绍了DreamUp3D，这是一种新颖的以对象为中心的生成模型（OCGM），专门设计用于对仅由单个RGB-D图像通知的3D场景执行推理。DreamUp3D是一个端到端训练的自监督模型，能够分割对象，提供3D对象重建，生成以对象为中心的潜在表示和精确的每个对象6D姿势估计。在一系列任务中，我们将DreamUp3D与基线进行了比较，包括NeRF、预训练的CLIP特征、ObSurf和ObPose，包括3D场景重建、对象匹配和对象姿态估计。我们的实验表明，我们的模型在现实世界场景中显著优于所有基线，这表明它适用于3D场景理解任务，同时满足机器人应用中的严格要求。 et.al.|[2402.16308](http://arxiv.org/abs/2402.16308)|null|
|**2024-02-25**|**GenNBV: Generalizable Next-Best-View Policy for Active 3D Reconstruction**|尽管神经辐射领域的最新进展使大规模场景的数字化变得现实，但图像捕获过程仍然耗时耗力。以前的工作试图使用次最佳视图（NBV）策略自动进行主动三维重建。然而，现有的NBV策略在很大程度上依赖于手工制定的标准、有限的动作空间或每场景优化的表示。这些约束限制了其跨数据集的可推广性。为了克服这些问题，我们提出了GenNBV，一种端到端可推广的NBV策略。我们的策略采用了基于强化学习（RL）的框架，并将典型的有限动作空间扩展到5D自由空间。它使我们的代理无人机能够从任何角度进行扫描，甚至在训练过程中与看不见的几何形状进行交互。为了提高跨数据集的可推广性，我们还提出了一种新的多源状态嵌入，包括几何、语义和动作表示。我们使用Isaac Gym模拟器与House3K和OmniObject3D数据集建立了一个基准，以评估该NBV策略。实验表明，我们的策略在这些数据集中对看不见的建筑规模对象的覆盖率分别达到98.26%和97.12%，优于先前的解决方案。 et.al.|[2402.16174](http://arxiv.org/abs/2402.16174)|null|
|**2024-02-24**|**A Generative Machine Learning Model for Material Microstructure 3D Reconstruction and Performance Evaluation**|从二维切片重建三维微观结构被认为在预测材料的空间结构和物理性质方面具有重要价值。从当前的技术角度来看，从2D到3D的尺寸扩展被视为一个极具挑战性的反问题。近年来，基于生成对抗性网络的方法得到了广泛的关注。然而，它们仍然受到许多限制的阻碍，包括模型过于简化、需要大量的训练样本，以及在训练过程中难以实现模型收敛。有鉴于此，提出了一种新的生成模型，该模型将U-net的多尺度特性与GAN的生成能力相结合。基于此，创新构建多尺度通道聚合模块、多尺度层次特征聚合模块和卷积块注意力机制，可以更好地捕捉材料微观结构的特性，提取图像信息。通过将图像正则化损失与Wasserstein距离损失相结合，进一步提高了模型的精度。此外，本研究利用各向异性指数准确区分图像的性质，可以清楚地确定图像的各向同性和各向异性。这也是首次评估来自不同领域的材料样本的生成质量，并比较模型本身的性能。实验结果表明，该模型不仅在生成的三维结构和真实样本之间显示出非常高的相似性，而且在统计数据分析方面与真实数据高度一致。 et.al.|[2402.15815](http://arxiv.org/abs/2402.15815)|null|
|**2024-02-22**|**Cameras as Rays: Pose Estimation via Ray Diffusion**|估计相机姿态是3D重建的一项基本任务，并且在稀疏视图（<10）的情况下仍然具有挑战性。与现有的对相机外部全局参数化进行自上而下预测的方法不同，我们提出了一种相机姿态的分布式表示，将相机视为一束光线。该表示允许与空间图像特征的紧密耦合，从而提高姿态精度。我们观察到，这种表示自然适合于设置级别的变换器，并开发了一种基于回归的方法，将图像块映射到相应的射线。为了捕捉稀疏视图姿态推断中固有的不确定性，我们采用这种方法来学习去噪扩散模型，该模型允许我们对合理的模式进行采样，同时提高性能。我们提出的方法，包括基于回归和扩散的方法，在CO3D上展示了最先进的相机姿态估计性能，同时推广到看不见的物体类别和野外捕捉。 et.al.|[2402.14817](http://arxiv.org/abs/2402.14817)|null|
|**2024-02-22**|**Workspace Analysis for Laparoscopic Rectal Surgery : A Preliminary Study**|医学成像、计算分析和机器人技术的集成为微创外科手术带来了重大变革，尤其是在腹腔镜直肠手术（LRS）领域。这种专门的外科技术旨在解决直肠癌症，需要深入理解骨盆狭窄空间内的空间动力学。本研究利用磁共振成像（MRI）扫描作为基础数据集，将其纳入计算机辅助设计（CAD）软件，以生成患者解剖结构的精确三维（3D）重建。这项研究的核心是对手术工作空间的分析，这是机器人干预优化的一个关键方面。复杂的计算算法在CAD环境中处理MRI数据，仔细计算骨盆内部区域的尺寸和轮廓。结果是，考虑到曲率、直径变化和潜在障碍等因素，对LRS期间的可行区域和限制区域进行了细致的理解。本文深入研究了机器人LRS工作空间分析的复杂性，说明了医学成像、CAD软件和外科机器人之间的无缝协作。通过这种跨学科的方法，这项研究旨在超越传统的手术方法，为在复杂的骨盆环境中优化机器人干预的范式转变提供新的见解。 et.al.|[2402.14386](http://arxiv.org/abs/2402.14386)|null|
|**2024-02-22**|**MVD $^2$: Efficient Multiview 3D Reconstruction for Multiview Diffusion**|多视点扩散（MVD）作为一种很有前途的三维生成技术，由于其在可推广性、质量和效率方面的优势而受到广泛关注。通过用3D数据微调预训练的大图像扩散模型，MVD方法首先基于图像或文本提示生成3D对象的多个视图，然后用多视图3D重建来重建3D形状。然而，生成的图像中的稀疏视图和不一致的细节使得3D重建具有挑战性。我们提出了一种有效的多视点扩散（MVD）图像三维重建方法MVD$^2$。MVD$^2$通过投影和卷积将图像特征聚合为3D特征体积，然后将体积特征解码为3D网格。我们使用3D形状集合和由3D形状的渲染视图提示的MVD图像来训练MVD$^2$。为了解决生成的多视点图像和3D形状的真实视图之间的差异，我们设计了一种简单而有效的视图相关训练方案。MVD$^2$提高了MVD的3D生成质量，并且对各种MVD方法快速且稳健。经过训练后，它可以在一秒内有效地从多视点图像中解码3D网格。我们使用Zero-123++和ObjectVerse LVIS 3D数据集训练MVD$^2$ ，并展示了其在使用合成图像和真实图像作为提示，从不同MVD方法生成的多视点图像生成3D模型方面的卓越性能。 et.al.|[2402.14253](http://arxiv.org/abs/2402.14253)|null|

<p align=right>(<a href=#updated-on-20240228>back to top</a>)</p>

## Diffusion

|Publish Date|Title|Abstract|PDF|Code|
|---|---|---|---|---|
|**2024-02-27**|**Diffusion Meets DAgger: Supercharging Eye-in-hand Imitation Learning**|使用模仿训练的策略的一种常见失败模式是在测试时复合执行错误。当习得的策略遇到专家演示中不存在的状态时，策略失败，导致退化行为。解决这个问题的数据集聚合（DAgger）方法只是收集更多的数据来覆盖这些故障状态。然而，在实践中，这往往过于昂贵。在这项工作中，我们提出了Diffusion Meets DAgger（DMD），这是一种在不考虑手对眼模仿学习问题的情况下获得DAgger好处的方法。DMD没有收集新的样本来覆盖分布外的状态，而是使用扩散模型的最新进展来创建具有扩散模型的这些样本。这使得很少的演示就可以获得强健的性能。在对Franka Research 3进行的非抓握推送实验中，我们表明DMD可以在只有8次专家演示的情况下实现80%的成功率，而幼稚行为克隆仅达到20%。DMD还比竞争对手的基于NeRF的增强方案高出50%。 et.al.|[2402.17768](http://arxiv.org/abs/2402.17768)|null|
|**2024-02-27**|**Seeing and Hearing: Open-domain Visual-Audio Generation with Diffusion Latent Aligners**|视频和音频内容创作是电影行业和专业用户的核心技术。最近，现有的基于扩散的方法分别处理视频和音频生成，这阻碍了技术从学术界向工业界的转移。在这项工作中，我们旨在通过精心设计的基于优化的跨视觉音频和联合视觉音频生成框架来填补这一空白。我们观察到现成的视频或音频生成模型的强大生成能力。因此，我们建议用共享的潜在表示空间来桥接现有的强模型，而不是从头开始训练巨型模型。具体来说，我们提出了一种具有预训练的ImageBind模型的多模态潜在对准器。我们的潜在对准器与在推理时间指导扩散去噪过程的分类器指南共享相似的核心。通过精心设计的优化策略和损失函数，我们展示了我们的方法在视频-音频联合生成、视觉引导的音频生成和音频引导的视觉生成任务上的优越性能。项目网站位于https://yzxing87.github.io/Seeing-and-Hearing/ et.al.|[2402.17723](http://arxiv.org/abs/2402.17723)|null|
|**2024-02-27**|**Structure-Guided Adversarial Training of Diffusion Models**|扩散模型在各种生成应用中表现出了非凡的功效。虽然现有模型专注于最小化数据分布建模的去噪分数匹配损失的加权和，但它们的训练主要强调实例级优化，忽略了每个小批量中有价值的结构信息，这些信息指示了样本之间的成对关系。为了解决这一限制，我们引入了扩散模型的结构引导对抗训练（SADM）。在这种开创性的方法中，我们强迫模型学习每个训练批次中样本之间的流形结构。为了确保模型在数据分布中捕捉到真实的流形结构，我们主张对扩散生成器进行对抗性训练，以对抗极小极大游戏中的新结构鉴别器，将真实的流形和生成的流形区分开来。SADM大大改进了现有的扩散变换器（DiT），并在12个数据集的图像生成和跨域微调任务方面优于现有方法，在ImageNet上建立了1.58和2.11的新的最先进FID，用于分别以256x256和512x512的分辨率生成类条件图像。 et.al.|[2402.17563](http://arxiv.org/abs/2402.17563)|null|
|**2024-02-27**|**Fast Lithium Ion Diffusion in Brownmillerite $\mathrm{Li}_{x}\mathrm{{Sr}_{2}{Co}_{2}{O}_{5}}$**|离子导体通过离子液体门控和新型储能应用（如全固态锂电池），在有趣的可调物理性质方面具有巨大的潜力。特别是，低迁移势垒和高跳跃尝试频率是实现离子在固体中快速扩散的关键。利用$\mathrm中的氧空位通道{Li}_{x} \mathrm{{Sr}_2.{Co}_2.{O}_{5} }$，我们发现锂离子的迁移势垒小到0.28~0.17eV，这取决于锂的浓度速率。我们的第一性原理计算还研究了跳跃尝试频率，得出室温离子扩散率和离子电导率分别高达${10}^{-7}\sim{10}^{-6}~\mathrm{{cm}^{2}~s^{-1}}$和${10}^{-3}\sim{10}^{-2}~\mashrm{s\cdot{cm}^{-1}}$，优于大多数钙钛矿型、石榴石型和硫化物锂离子固体电解质。这项工作证明了$\mathrm{Li}_{x} \mathrm{{Sr}_2.{Co}_2.{O}_{5} }$ 作为一种有前途的固态电解质。 et.al.|[2402.17557](http://arxiv.org/abs/2402.17557)|null|
|**2024-02-27**|**Scribble Hides Class: Promoting Scribble-Based Weakly-Supervised Semantic Segmentation with Its Class Label**|使用稀疏涂鸦监督的基于涂鸦的弱监督语义分割越来越受欢迎，因为与完全注释的替代方案相比，它降低了注释成本。现有的方法主要通过将标记的像素扩散到具有局部线索的未标记像素来生成伪标签以进行监督。然而，这种扩散过程未能利用全局语义和类特定线索，这对语义分割很重要。在这项研究中，我们提出了一个类驱动的涂鸦推广网络，该网络利用图像级类和全局语义提供的涂鸦注释和伪标签进行监督。直接采用伪标签可能会误导分割模型，因此我们设计了一个定位校正模块来校正特征空间中的前景表示。为了进一步结合这两种监督的优势，我们还引入了一种用于减少不确定性的距离熵损失，该方法根据涂鸦和伪标签边界确定的可靠区域来调整每像素的置信度权重。在具有不同质量的scribleSup数据集上进行的实验优于之前的所有方法，证明了我们的方法的优越性和稳健性。代码位于https://github.com/Zxl19990529/Class-driven-Scribble-Promotion-Network. et.al.|[2402.17555](http://arxiv.org/abs/2402.17555)|**[link](https://github.com/zxl19990529/class-driven-scribble-promotion-network)**|
|**2024-02-27**|**Forming 1D Periodic J-aggregates by Mechanical Bending of BNNTs: Evidence of Activated Molecular Diffusion**|将分子组装驱动到微米级图案是定义各种领域感兴趣的先进材料的关键，包括生命科学、光伏和量子光子学。然而，驱动过程与其他力竞争，如布朗运动、成熟现象、毛细管力和非特异性吸附。在这里，我们报道了封装在氮化硼纳米管（BNNT）内的发光染料分子的引导扩散机制。BNNT弯曲和沿BNNT轴的分子位置之间的相关测量揭示了染料从纳米管的弯曲区域向直区域的有效和长程迁移。这种曲率激活的扩散以明确的间隔和长度的周期性模式形成明亮的J聚集体簇。使用弯曲BNNT中引导分子输运的唯象模型来描述BNNT内部的这种定向1D扩散。结果表明，它可以准确地预测作为纳米管长度函数的J聚集体的位置和形态。将拓扑刺激与纳米尺度的1D分子扩散耦合是一种有趣的工具，能够在介观尺度上重新配置功能分子的各种发射模式。 et.al.|[2402.17537](http://arxiv.org/abs/2402.17537)|null|
|**2024-02-27**|**Diffusion Model-Based Image Editing: A Survey**|去噪扩散模型已成为各种图像生成和编辑任务的强大工具，有助于以无条件或输入条件的方式合成视觉内容。它们背后的核心思想是学习扭转逐渐向图像添加噪声的过程，使它们能够从复杂的分布中生成高质量的样本。在这项调查中，我们对使用扩散模型进行图像编辑的现有方法进行了详尽的概述，涵盖了该领域的理论和实践两个方面。我们从多个角度深入分析和分类这些作品，包括学习策略、用户输入条件和可以完成的一系列特定编辑任务。此外，我们特别关注图像的修复和外绘，并探索了早期的传统上下文驱动和当前的多模式条件方法，对它们的方法进行了全面的分析。为了进一步评估文本引导图像编辑算法的性能，我们提出了一个系统的基准EditEval，该基准具有创新的指标LMM Score。最后，我们解决了目前的局限性，并展望了未来研究的一些潜在方向。随附的存储库发布于https://github.com/SiatMMLab/Awesome-Diffusion-Model-Based-Image-Editing-Methods. et.al.|[2402.17525](http://arxiv.org/abs/2402.17525)|**[link](https://github.com/siatmmlab/awesome-diffusion-model-based-image-editing-methods)**|
|**2024-02-27**|**Label-Noise Robust Diffusion Models**|条件扩散模型在各种生成任务中表现出了显著的性能，但训练它们需要大规模的数据集，这些数据集通常在条件输入中包含噪声，也称为噪声标签。这种噪声导致所生成的数据的条件失配和质量下降。本文提出了用于训练带有噪声标签的条件扩散模型的转移感知加权去噪分数匹配（TDSM），这是扩散模型领域的首次研究。TDSM目标包含分数网络的加权和，结合了实例和时间相关的标签转移概率。我们引入了一种转移感知权重估计器，该估计器利用了根据扩散过程独特定制的时间相关噪声标签分类器。通过在各种数据集和噪声标签设置上进行实验，TDSM提高了生成的与给定条件一致的样本的质量。此外，我们的方法甚至在流行的基准数据集上也提高了生成性能，这意味着潜在的噪声标签及其生成模型学习的风险。最后，我们展示了TDSM在传统噪声标签校正之上的改进性能，这从经验上证明了它作为标签噪声鲁棒生成模型的一部分的贡献。我们的代码位于：https://github.com/byeonghu-na/tdsm. et.al.|[2402.17517](http://arxiv.org/abs/2402.17517)|**[link](https://github.com/byeonghu-na/tdsm)**|
|**2024-02-27**|**The Unwanted Dissemination of Science: The Usage of Academic Articles as Ammunition in Contested Discursive Arenas on Twitter**|推特是一个常见的攻击性语言网站。先前的文献表明，在讨论政治话题时，推特的情感内容会严重影响其传播。我们将之前的工作扩展到研究链接到学术文章的攻击性推文。使用混合方法，我们发现了三个发现：首先，攻击性语言在引用学术文章的推文中很常见，并且因主题而异。其次，话语分析表明，攻击性推文通常使用学术文章来宣传或攻击政治意识形态。最后，我们发现，与非攻击性推文相比，攻击性推特的受众更少。我们对这些攻击性推文的分析揭示了学术文章是如何在推特上分享的，而不是为了传播新知识，而是作为有争议和好斗话语中的辩论工具。 et.al.|[2402.17495](http://arxiv.org/abs/2402.17495)|null|
|**2024-02-27**|**EMO: Emote Portrait Alive - Generating Expressive Portrait Videos with Audio2Video Diffusion Model under Weak Conditions**|在这项工作中，我们通过关注音频提示和面部动作之间的动态和微妙关系，来应对增强谈话头部视频生成的真实性和表现力的挑战。我们发现了传统技术的局限性，这些技术往往无法捕捉到人类表情的全方位和个人面部风格的独特性。为了解决这些问题，我们提出了EMO，这是一种利用直接音频到视频合成方法的新框架，绕过了对中间3D模型或面部标志的需求。我们的方法确保了整个视频中无缝的帧转换和一致的身份保护，从而产生高度表现力和逼真的动画。实验结果表明，EMO不仅能够制作出令人信服的演讲视频，而且能够制作出各种风格的歌唱视频，在表现力和真实性方面显著优于现有的最先进的方法。 et.al.|[2402.17485](http://arxiv.org/abs/2402.17485)|null|

<p align=right>(<a href=#updated-on-20240228>back to top</a>)</p>

## NeRF

|Publish Date|Title|Abstract|PDF|Code|
|---|---|---|---|---|
|**2024-02-27**|**AlignMiF: Geometry-Aligned Multimodal Implicit Field for LiDAR-Camera Joint Synthesis**|神经隐式场已经成为新视图合成中事实上的标准。最近，有一些方法探索在一个领域内融合多个模态，旨在共享不同模态的隐含特征，以提高重建性能。然而，这些模态往往表现出错位行为：对一种模态（如激光雷达）进行优化可能会对另一种模态产生不利影响，如相机性能，反之亦然。在这项工作中，我们对激光雷达相机联合合成的多模式隐场进行了全面分析，揭示了潜在的问题在于不同传感器的错位。此外，我们还介绍了AlignMiF，这是一个几何对齐的多模式隐式场，具有两个拟议的模块：几何感知对齐（GAA）和共享几何初始化（SGI）。这些模块有效地调整了不同模态的粗略几何结构，显著增强了激光雷达和相机数据之间的融合过程。通过在各种数据集和场景中进行广泛的实验，我们证明了我们的方法在促进激光雷达和相机模态之间在统一的神经场中更好地交互方面的有效性。具体而言，我们提出的AlignMiF比最近的隐式融合方法（KITTI-360和Waymo数据集上的图像PSNR分别为+2.01和+3.11）实现了显著的改进，并始终超过单模态性能（在各自的数据集上，激光雷达切角距离分别减少了13.8%和14.2%）。 et.al.|[2402.17483](http://arxiv.org/abs/2402.17483)|**[link](https://github.com/tangtaogo/alignmif)**|
|**2024-02-26**|**GEM3D: GEnerative Medial Abstractions for 3D Shape Synthesis**|我们介绍了GEM3D——一种新的深度、拓扑感知的三维形状生成模型。我们的方法的关键成分是基于神经骨架的表示，对形状拓扑和几何信息进行编码。通过去噪扩散概率模型，我们的方法首先根据中轴变换（MAT）生成基于骨架的表示，然后通过骨架驱动的神经隐式公式生成曲面。神经隐式考虑了存储在生成的骨架表示中的拓扑和几何信息，以产生与以前的神经场公式相比在拓扑和几何上更准确的曲面。我们讨论了我们的方法在形状合成和点云重建任务中的应用，并对我们的方法进行了定性和定量评估。与最先进的技术相比，我们展示了更忠实的表面重建和多样化的形状生成结果，还涉及从Thingi10K和ShapeNet重建和合成结构复杂的高属形表面的挑战性场景。 et.al.|[2402.16994](http://arxiv.org/abs/2402.16994)|null|
|**2024-02-21**|**Geometry-Informed Neural Networks**|我们引入了几何知情神经网络（GINN）的概念，它包括（i）在几何约束下的学习，（ii）作为适当表示的神经场，以及（iii）为几何任务中经常遇到的不确定系统生成不同的解决方案。值得注意的是，GINN公式不需要训练数据，因此可以被视为纯粹由约束驱动的生成建模。我们添加了一个明确的多样性损失来缓解模式崩溃。我们考虑了几个约束，特别是分量的连通性，我们通过Morse理论将其转化为可微损失。在实验上，我们展示了GINN学习范式在一系列二维和三维场景中的有效性，这些场景的复杂性不断增加。 et.al.|[2402.14009](http://arxiv.org/abs/2402.14009)|null|
|**2024-02-18**|**Pattern Recognition Facilities of Extended Kalman Filtering in Stochastic Neural Fields**|在数学神经科学中，人们特别关注在存在模型不确定性的情况下，由动态神经场（DNF）建模的神经组织中的工作记忆机制。工作记忆设施意味着，由于网络中反复的相互作用，在去除外部刺激后，神经元的活动保持自我维持，并允许系统处理丢失的传感器信息。在我们之前的工作中，我们已经根据传感器提供的不完整数据开发了两种神经膜电位的重建方法。这些方法是在扩展卡尔曼滤波方法中通过使用Euler Maruyama方法和\^{o}-Taylor订单1.5的扩展。它表明\^{o}-Taylor基于EKF的恢复过程比基于Euler Maruyama的替代方案更准确。在传感器信息不完整的情况下，它提高了膜电位重建的质量。本文的目的是研究它们的模式识别功能，即在模型不确定和信息不完整的情况下，模式形成重建的质量。数值实验是以神经组织中出现多个活动区的随机DNF为例提供的。 et.al.|[2402.11551](http://arxiv.org/abs/2402.11551)|null|
|**2024-02-15**|**Reg-NF: Efficient Registration of Implicit Surfaces within Neural Fields**|神经场，即基于坐标的神经网络，最近因隐含地表示场景而广受欢迎。与基于点云等显式表示的经典方法相比，神经场提供了连续的场景表示，能够以紧凑且理想的机器人应用方式表示3D几何结构和外观。然而，有限的现有方法已经研究了通过直接利用这些连续的隐式表示来配准多个神经场。在本文中，我们提出了Reg-NF，这是一种基于神经场的配准，它优化了两个任意神经场之间的相对6-DoF变换，即使这两个场具有不同的比例因子。Reg NF的关键组成部分包括双向配准损失、多视图表面采样和体积符号距离函数（SDF）的利用。我们在一个新的神经场数据集上展示了我们的方法，用于评估配准问题。我们提供了一组详尽的实验和消融研究，以确定我们的方法的性能，同时也讨论了局限性，为研究界在无约束环境中利用神经场的开放挑战提供了未来的方向。 et.al.|[2402.09722](http://arxiv.org/abs/2402.09722)|null|
|**2024-02-12**|**Unsupervised Discovery of Object-Centric Neural Fields**|我们研究从单个图像中推断3D以对象为中心的场景表示。虽然最近的方法在从简单的合成图像中无监督地发现3D对象方面显示出了潜力，但它们未能推广到具有视觉丰富和多样化对象的真实世界场景。这种限制源于它们的对象表示，它将对象的内在属性（如形状和外观）与外在的、以观察者为中心的属性（如3D位置）纠缠在一起。为了解决这一瓶颈，我们提出了以对象为中心的神经场的无监督发现（uOCF）。uOCF专注于学习对象的内在，并分别对外在进行建模。我们的方法显著提高了系统泛化能力，从而能够从稀疏的真实世界图像中无监督地学习高保真的以对象为中心的场景表示。为了评估我们的方法，我们收集了三个新的数据集，包括两个真实的厨房环境。大量实验表明，uOCF能够在无监督的情况下从单个真实图像中发现视觉丰富的对象，从而实现3D对象分割和场景操作等应用。值得注意的是，uOCF演示了对单个真实图像中看不见的物体的零样本泛化。项目页面：https://red-fairy.github.io/uOCF/ et.al.|[2402.07376](http://arxiv.org/abs/2402.07376)|null|
|**2024-02-06**|**Improved Generalization of Weight Space Networks via Augmentations**|在深度权重空间（DWS）中学习，神经网络处理其他神经网络的权重，是一个新兴的研究方向，应用于2D和3D神经领域（INRs、NeRFs），以及对其他类型的神经网络进行推断。不幸的是，权重空间模型往往存在严重的过拟合问题。我们实证分析了这种过拟合的原因，发现一个关键原因是DWS数据集缺乏多样性。虽然给定的对象可以用许多不同的权重配置来表示，但典型的INR训练集无法捕捉表示同一对象的INR之间的可变性。为了解决这一问题，我们探索了在权重空间中增加数据的策略，并提出了一种适用于权重空间的MixUp方法。我们在两个设置中展示了这些方法的有效性。在分类方面，它们可以提高性能，类似于拥有10倍以上的数据。在自我监督的对比学习中，它们在下游分类中产生了5-10%的显著收益。 et.al.|[2402.04081](http://arxiv.org/abs/2402.04081)|null|
|**2024-01-31**|**BlockFusion: Expandable 3D Scene Generation using Latent Tri-plane Extrapolation**|我们介绍了BlockFusion，这是一种基于扩散的模型，它将3D场景生成为单元块，并无缝地合并新的块来扩展场景。BlockFusion使用从完整的3D场景网格中随机裁剪的3D块的数据集进行训练。通过逐块拟合，所有训练块都被转换为混合神经场：具有包含几何特征的三平面，然后是用于解码有符号距离值的多层感知器（MLP）。采用变分自动编码器将三平面压缩到潜在的三平面空间中，在该空间上进行去噪扩散处理。应用于潜在表示的扩散允许高质量和多样化的3D场景生成。要在生成过程中扩展场景，只需附加空块以与当前场景重叠，并外推现有的潜在三平面以填充新块。外推是通过在去噪迭代过程中使用来自重叠三平面的特征样本来调节生成过程来完成的。潜在的三平面外推法产生语义和几何上有意义的过渡，与现有场景和谐融合。2D布局调节机制用于控制场景元素的放置和布置。实验结果表明，BlockFusion能够在室内和室外场景中生成具有前所未有的高质量形状的多样化、几何一致和无边界的大型3D场景。 et.al.|[2401.17053](http://arxiv.org/abs/2401.17053)|null|
|**2024-01-26**|**Learning Neural Radiance Fields of Forest Structure for Scalable and Fine Monitoring**|这项工作利用神经辐射场和遥感技术用于林业应用。在这里，我们展示了神经辐射场为改进森林监测中现有的遥感方法提供了广泛的可能性。我们提出的实验证明了它们的潜力：（1）表达森林三维结构的精细特征，（2）融合可用的遥感模式，（3）改进三维结构衍生的森林指标。总之，这些特性使神经场成为一种有吸引力的计算工具，具有进一步提高森林监测程序的可扩展性和准确性的巨大潜力。 et.al.|[2401.15029](http://arxiv.org/abs/2401.15029)|null|
|**2024-01-25**|**Learning Robust Generalizable Radiance Field with Visibility and Feature Augmented Point Representation**|本文介绍了广义神经辐射场（NeRF）的一种新范式。以前的通用NeRF方法将多视点立体技术与基于图像的神经渲染相结合进行泛化，产生了令人印象深刻的结果，同时存在三个问题。首先，遮挡常常导致不一致的特征匹配。然后，由于采样点和粗略特征聚合的单独过程，它们在几何不连续性和局部尖锐形状中传递失真和伪影。第三，当源视图离目标视图不够近时，它们基于图像的表示会发生严重退化。为了应对挑战，我们提出了第一个基于点而不是基于图像的渲染构建可泛化神经场的范式，我们称之为可泛化神经点场（GPF）。我们的方法通过几何先验显式地建模可见性，并用神经特征增强它们。我们提出了一种新的非均匀对数采样策略，以提高渲染速度和重建质量。此外，我们提出了一种可学习的内核，该内核在空间上增加了用于特征聚合的特征，减轻了几何结构急剧变化的地方的失真。此外，我们的表现很容易被操纵。实验表明，在泛化和微调设置中，我们的模型可以在三个数据集上提供比所有对应模型和基准更好的几何结构、视图一致性和渲染质量，初步证明了可泛化NeRF新范式的潜力。 et.al.|[2401.14354](http://arxiv.org/abs/2401.14354)|null|

<p align=right>(<a href=#updated-on-20240228>back to top</a>)</p>

[contributors-shield]: https://img.shields.io/github/contributors/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[contributors-url]: https://github.com/Vincentqyw/cv-arxiv-daily/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[forks-url]: https://github.com/Vincentqyw/cv-arxiv-daily/network/members
[stars-shield]: https://img.shields.io/github/stars/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[stars-url]: https://github.com/Vincentqyw/cv-arxiv-daily/stargazers
[issues-shield]: https://img.shields.io/github/issues/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[issues-url]: https://github.com/Vincentqyw/cv-arxiv-daily/issues

