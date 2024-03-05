[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]

## Updated on 2024.03.05
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
|**2024-02-29**|**ViewFusion: Towards Multi-View Consistency via Interpolated Denoising**|通过扩散模型进行的新型视图合成在生成多样化和高质量图像方面表现出了显著的潜力。然而，在这些主流方法中，图像生成的独立过程导致了在保持多视图一致性方面的挑战。为了解决这一问题，我们引入了ViewFusion，这是一种新颖的无训练算法，可以无缝集成到现有的预训练扩散模型中。我们的方法采用了一种自回归方法，该方法隐式地利用先前生成的视图作为下一个视图生成的上下文，确保了在新视图生成过程中强大的多视图一致性。通过通过插值去噪融合已知视图信息的扩散过程，我们的框架成功地扩展了单视图条件模型，使其在多视图条件设置下工作，而无需任何额外的微调。大量的实验结果证明了ViewFusion在生成一致且详细的新视图方面的有效性。 et.al.|[2402.18842](http://arxiv.org/abs/2402.18842)|**[link](https://github.com/Wi-sc/ViewFusion)**|
|**2024-02-28**|**PolyOculus: Simultaneous Multi-view Image-based Novel View Synthesis**|本文考虑了生成新视图合成（GNVS）的问题，即在给定有限数量的已知视图的情况下生成场景的新颖、合理的视图。在这里，我们提出了一个基于集合的生成模型，该模型可以同时生成多个自洽的新视图，条件是任何数量的已知视图。我们的方法不限于一次生成单个图像，并且可以以零、一个或多个视图为条件。因此，当生成大量视图时，我们的方法不限于低阶自回归生成方法，并且能够更好地在大图像集上保持生成的图像质量。我们在标准NVS数据集上评估了所提出的模型，并表明它优于最先进的基于图像的GNVS基线。此外，我们表明，该模型能够生成没有自然顺序的相机视图集，如循环和双目轨迹，并且在此类任务上显著优于其他方法。 et.al.|[2402.17986](http://arxiv.org/abs/2402.17986)|null|
|**2024-02-27**|**AlignMiF: Geometry-Aligned Multimodal Implicit Field for LiDAR-Camera Joint Synthesis**|神经隐式场已经成为新视图合成中事实上的标准。最近，有一些方法探索在一个领域内融合多个模态，旨在共享不同模态的隐含特征，以提高重建性能。然而，这些模态往往表现出错位行为：对一种模态（如激光雷达）进行优化可能会对另一种模态产生不利影响，如相机性能，反之亦然。在这项工作中，我们对激光雷达相机联合合成的多模式隐场进行了全面分析，揭示了潜在的问题在于不同传感器的错位。此外，我们还介绍了AlignMiF，这是一个几何对齐的多模式隐式场，具有两个拟议的模块：几何感知对齐（GAA）和共享几何初始化（SGI）。这些模块有效地调整了不同模态的粗略几何结构，显著增强了激光雷达和相机数据之间的融合过程。通过在各种数据集和场景中进行广泛的实验，我们证明了我们的方法在促进激光雷达和相机模态之间在统一的神经场中更好地交互方面的有效性。具体而言，我们提出的AlignMiF比最近的隐式融合方法（KITTI-360和Waymo数据集上的图像PSNR分别为+2.01和+3.11）实现了显著的改进，并始终超过单模态性能（在各自的数据集上，激光雷达切角距离分别减少了13.8%和14.2%）。 et.al.|[2402.17483](http://arxiv.org/abs/2402.17483)|**[link](https://github.com/tangtaogo/alignmif)**|
|**2024-02-26**|**GEA: Reconstructing Expressive 3D Gaussian Avatar from Monocular Video**|本文提出了GEA，这是一种基于3D高斯的身体和手的高保真重建来创建富有表现力的3D化身的新方法。关键贡献有两方面。首先，我们设计了一种两阶段姿态估计方法，以从输入图像中获得准确的SMPL-X姿态，从而在训练图像的像素和SMPL-X模型之间提供正确的映射。它使用注意力感知网络和优化方案来对齐图像中估计的SMPL-X身体和真实身体之间的法线和轮廓。其次，我们提出了一种迭代重新初始化策略来处理高斯表示所面临的不平衡聚合和初始化偏差。该策略迭代地重新分布化身的高斯点，通过应用网格划分、重采样和重高斯运算，使其均匀分布在人体表面附近。结果，可以实现更高质量的渲染。大量的实验分析验证了所提出的模型的有效性，表明它在逼真的新视图合成中实现了最先进的性能，同时提供了对人体和手部姿势的细粒度控制。项目页面：https://3d-aigc.github.io/GEA/. et.al.|[2402.16607](http://arxiv.org/abs/2402.16607)|null|
|**2024-02-26**|**CMC: Few-shot Novel View Synthesis via Cross-view Multiplane Consistency**|神经辐射场（NeRF）由于其连续表示场景的能力，在新颖的视图合成中，特别是在虚拟现实（VR）和增强现实（AR）中，显示出了令人印象深刻的结果。然而，当只有几个输入视图图像可用时，NeRF倾向于过度拟合给定视图，从而使像素的估计深度共享几乎相同的值。与以前通过引入复杂的先验或额外的监督来进行正则化的方法不同，我们提出了一种简单而有效的方法，该方法明确地在输入视图之间建立深度感知一致性，以应对这一挑战。我们的关键见解是，通过强制在不同的输入视图中重复采样相同的空间点，我们能够加强视图之间的相互作用，从而缓解过拟合问题。为了实现这一点，我们在分层表示（\textit｛即｝多平面图像）上建立神经网络，因此可以在多个离散平面上对采样点进行重新采样。此外，为了正则化看不见的目标视图，我们将不同输入视图的渲染颜色和深度约束为相同。尽管简单，但大量的实验表明，与最先进的方法相比，我们提出的方法可以获得更好的合成质量。 et.al.|[2402.16407](http://arxiv.org/abs/2402.16407)|null|
|**2024-02-26**|**FrameNeRF: A Simple and Efficient Framework for Few-shot Novel View Synthesis**|我们提出了一种新的框架，称为FrameNeRF，旨在将现成的快速高保真NeRF模型应用于少镜头的新颖视图合成任务，该模型具有快速训练速度和高渲染质量。快速高保真度模型的训练稳定性通常局限于密集视图，这使得它们不适合于少镜头的新颖视图合成任务。为了解决这一限制，我们利用正则化模型作为数据生成器，从稀疏输入中生成密集视图，从而促进快速高保真模型的后续训练。由于这些密集视图是由正则化模型生成的伪地面实况，因此使用原始稀疏图像来微调快速高保真度模型。这个过程有助于模型学习真实的细节，并更正早期阶段引入的工件。通过利用现成的正则化模型和快速高保真度模型，我们的方法在各种基准数据集上实现了最先进的性能。 et.al.|[2402.14586](http://arxiv.org/abs/2402.14586)|null|
|**2024-02-22**|**TaylorGrid: Towards Fast and High-Quality Implicit Field Learning via Direct Taylor-based Grid Optimization**|基于坐标的神经隐式表示或隐式场已被广泛研究用于3D几何表示或新颖视图合成。近年来，人们致力于加快基于坐标的内隐场学习的速度和提高其质量。代替学习重MLP来预测查询坐标的神经隐式值，已经提出了与浅MLP相结合的神经体素或网格来实现具有减少的优化时间的高质量隐式场学习。另一方面，为了进一步提高学习速度，已经提出了诸如线性网格之类的轻量级场表示。在本文中，我们的目标是快速和高质量的隐场学习，并提出了TaylorGrid，这是一种新的隐场表示，可以在2D或3D网格上通过直接泰勒展开优化有效地计算。一般来说，TaylorGrid可以适用于不同的内隐场学习任务，如SDF学习或NeRF。通过广泛的定量和定性比较，TaylorGrid实现了线性网格和神经体素之间的平衡，显示了其在快速和高质量的内隐场学习中的优势。 et.al.|[2402.14415](http://arxiv.org/abs/2402.14415)|null|
|**2024-02-20**|**Improving Robustness for Joint Optimization of Camera Poses and Decomposed Low-Rank Tensorial Radiance Fields**|在本文中，我们提出了一种算法，该算法允许仅使用2D图像作为监督，对由分解的低秩张量表示的相机姿态和场景几何进行联合细化。首先，我们基于1D信号进行了一项试点研究，并将我们的发现与3D场景联系起来，在3D场景中，基于体素的NeRF上的初始关节姿态优化可以很容易地导致次优解。此外，基于频谱分析，我们建议在2D和3D辐射场上应用卷积高斯滤波器，以实现从粗到细的训练计划，从而实现联合相机姿态优化。利用分解后的低秩张量中的分解特性，我们的方法实现了与强力3D卷积等效的效果，只需很少的计算开销。为了进一步提高联合优化的鲁棒性和稳定性，我们还提出了平滑的2D监督、随机缩放的核参数和边缘引导的损失掩模技术。广泛的定量和定性评估表明，我们提出的框架在新的视图合成方面取得了卓越的性能，并实现了快速收敛的优化。 et.al.|[2402.13252](http://arxiv.org/abs/2402.13252)|**[link](https://github.com/nemo1999/joint-tensorf)**|
|**2024-02-20**|**Real-time High-resolution View Synthesis of Complex Scenes with Explicit 3D Visibility Reasoning**|绘制复杂场景的照片逼真的新颖视图图像一直是计算机图形学中的一个长期挑战。近年来，在视图合成领域，在提高渲染质量和加快渲染速度方面取得了很大的研究进展。然而，当使用稀疏视图渲染复杂的动态场景时，由于遮挡问题，渲染质量仍然有限。此外，对于在动态场景中渲染高分辨率图像，渲染速度仍远未达到实时性。在这项工作中，我们提出了一种可推广的视图合成方法，该方法可以从稀疏视图实时渲染复杂静态和动态场景的高分辨率新视图图像。为了解决由输入视图的稀疏性和捕获场景的复杂性引起的遮挡问题，我们引入了一种显式3D可见性推理方法，该方法可以有效地估计采样的3D点对输入视图的可见性。所提出的可见性推理方法是完全可微分的，可以很好地适应体绘制管道，使我们能够在训练网络时只使用多视图图像作为监督，同时细化几何体和纹理。此外，我们管道中的每个模块都经过精心设计，以绕过耗时的MLP查询过程，提高高分辨率图像的渲染质量，使我们能够实时渲染高分辨率的新视图图像。实验结果表明，我们的方法在渲染质量和速度上都优于以前的视图合成方法，尤其是在处理具有稀疏视图的复杂动态场景时。 et.al.|[2402.12886](http://arxiv.org/abs/2402.12886)|null|
|**2024-02-20**|**MVDiffusion++: A Dense High-resolution Multi-view Diffusion Model for Single or Sparse-view 3D Object Reconstruction**|本文提出了一种用于3D对象重建的神经结构MVDiffusion++，该结构在给定一张或几张没有相机姿势的图像的情况下合成对象的密集和高分辨率视图。MVDiffusion++通过两个令人惊讶的简单想法实现了卓越的灵活性和可扩展性：1）“无姿势架构”，其中2D潜在特征之间的标准自关注在任意数量的条件视图和生成视图中学习3D一致性，而无需显式使用相机姿势信息；和2）一种“视图丢弃策略”，在训练期间丢弃大量输出视图，这减少了训练时间内存占用，并在测试时实现了密集和高分辨率的视图合成。我们使用Ob厌恶对象进行训练，使用谷歌扫描对象进行评估，并使用标准的新视图合成和3D重建指标，其中MVDiffusion++显著优于当前的技术状态。我们还通过将MVDiffusion++与文本到图像生成模型相结合，展示了一个文本到3D应用程序示例。 et.al.|[2402.12712](http://arxiv.org/abs/2402.12712)|null|

<p align=right>(<a href=#updated-on-20240305>back to top</a>)</p>

## 3D Reconstruction

|Publish Date|Title|Abstract|PDF|Code|
|---|---|---|---|---|
|**2024-02-29**|**VEnvision3D: A Synthetic Perception Dataset for 3D Multi-Task Model Research**|开发统一的多任务基础模型已成为计算机视觉研究中的一个关键挑战。在当前的3D计算机视觉领域，大多数数据集只关注相对有限的一组任务，这使各种下游任务的并行训练要求复杂化。这使得多目标网络的训练难以进行，进一步阻碍了三维视觉领域基础模型的发展。在本文中，我们介绍了VEnvision3D，这是一个用于多任务学习的大型3D合成感知数据集，包括深度完成、分割、上采样、位置识别和3D重建。由于每个任务的数据都是在相同的场景中收集的，因此任务在使用的数据方面本质上是一致的。因此，这样一个独特的属性可以帮助探索多任务模型甚至基础模型的潜力，而无需单独的训练方法。基于所提出的数据集的特点，提出了几个新的基准。对端到端模型进行了广泛的研究，揭示了新的观察结果、挑战和未来研究的机会。此外，我们设计了一个直接的多任务网络，以揭示VEnvision3D可以为基础模型提供的能力。我们的数据集和代码将在接受后开源。 et.al.|[2402.19059](http://arxiv.org/abs/2402.19059)|null|
|**2024-02-29**|**ViewFusion: Towards Multi-View Consistency via Interpolated Denoising**|通过扩散模型进行的新型视图合成在生成多样化和高质量图像方面表现出了显著的潜力。然而，在这些主流方法中，图像生成的独立过程导致了在保持多视图一致性方面的挑战。为了解决这一问题，我们引入了ViewFusion，这是一种新颖的无训练算法，可以无缝集成到现有的预训练扩散模型中。我们的方法采用了一种自回归方法，该方法隐式地利用先前生成的视图作为下一个视图生成的上下文，确保了在新视图生成过程中强大的多视图一致性。通过通过插值去噪融合已知视图信息的扩散过程，我们的框架成功地扩展了单视图条件模型，使其在多视图条件设置下工作，而无需任何额外的微调。大量的实验结果证明了ViewFusion在生成一致且详细的新视图方面的有效性。 et.al.|[2402.18842](http://arxiv.org/abs/2402.18842)|**[link](https://github.com/Wi-sc/ViewFusion)**|
|**2024-02-28**|**The Role of a Neutron Component in the Photospheric Emission of Long-Duration Gamma-Ray Burst Jets**|长时间伽马射线暴（LGRB）被认为是在核心坍塌超新星期间产生的，可能在流出物质中有显著的中子成分。如果存在，中子可以通过降低其不透明度来改变光子在外流中的散射方式，从而使光子比没有中子的情况下更快地解耦。因此，了解这一过程的细节可以让我们探索LGRB的中心引擎，否则它是隐藏的。在这里，我们使用相对论流体动力学模拟和使用蒙特卡罗辐射转移（MCRaT）代码的辐射转移后处理相结合的方法，给出了LGRB喷流的光球发射结果。我们通过改变平衡电子分数 $Y_｛e｝$来控制喷流材料中中子组分的大小，我们发现GRB火球中中子的存在会影响能带参数$\alpha$和$e_｛0｝$，而带有$\beta$参数的图片则不太清楚。特别地，断裂能量$E_{0}$ 被转移到更高的能量。此外，我们发现，增加中子分量的大小也会增加多个视角下流出的总辐射能量。我们的研究结果不仅揭示了LGRB，而且与与双星中子星合并相关的短时间伽马射线爆发有关，因为在这样的系统中可能存在突出的中子成分。 et.al.|[2402.18657](http://arxiv.org/abs/2402.18657)|null|
|**2024-02-27**|**Sora Generates Videos with Stunning Geometrical Consistency**|最近开发的索拉模型[1]在视频生成方面表现出了非凡的能力，引发了关于其模拟真实世界现象能力的激烈讨论。尽管它越来越受欢迎，但缺乏既定的指标来定量评估它对现实世界物理的保真度。在本文中，我们介绍了一种新的基准，该基准基于视频对真实世界物理原理的遵守程度来评估生成视频的质量。我们采用了一种将生成的视频转换为3D模型的方法，利用了3D重建的准确性在很大程度上取决于视频质量的前提。从3D重建的角度来看，我们使用所构建的3D模型所满足的几何约束的保真度作为代理来衡量生成的视频在多大程度上符合真实世界的物理规则。项目页面：https://sora-geometrical-consistency.github.io/ et.al.|[2402.17403](http://arxiv.org/abs/2402.17403)|null|
|**2024-02-27**|**CharNeRF: 3D Character Generation from Concept Art**|3D建模在AR/VR和游戏领域具有重要意义，既有艺术创意，也有实际应用。然而，这个过程往往很耗时，而且需要很高的技能水平。在本文中，我们提出了一种新的方法，从一致的周转概念艺术中创建3D角色的体积表示，这是3D建模行业的标准输入。虽然神经辐射场（NeRF）已经改变了基于图像的3D重建的游戏规则，但据我们所知，还没有已知的研究可以优化概念艺术的管道。为了利用概念艺术的潜力，通过其定义的身体姿势和特定的视角，我们建议将其编码为我们模型的先验。我们训练网络，通过可学习的视图方向关注的多头自注意层，将这些先验用于各种3D点。此外，我们还证明了射线采样和表面采样的结合增强了我们网络的推理能力。我们的模型能够生成高质量的360度字符视图。随后，我们提供了一个简单的指南，以更好地利用我们的模型来提取3D网格。需要注意的是，我们模型的推理能力受到训练数据特征的影响，主要集中在具有单头、双臂和双腿的角色上。尽管如此，我们的方法仍然是通用的，适用于来自不同主题的概念艺术，而不会对数据强加任何具体的假设。 et.al.|[2402.17115](http://arxiv.org/abs/2402.17115)|null|
|**2024-02-28**|**Reliable Conflictive Multi-View Learning**|多视图学习旨在结合多种特征，实现对数据的更全面描述。以前的大多数工作都假设多个视图是严格对齐的。然而，真实世界的多视图数据可能包含低质量的冲突实例，这些实例在不同的视图中显示冲突信息。以前解决这个问题的方法主要集中在通过删除或替换冲突的视图来消除冲突的数据实例。然而，现实世界中的应用程序通常需要为冲突实例做出决策，而不仅仅是消除它们。为了解决这个问题，我们提出了一个新的可靠冲突多视图学习（RCML）问题，该问题要求模型为冲突多视图数据提供决策结果和附加的可靠性。针对这个问题，我们开发了一种证据冲突多视角学习（ECML）方法。ECML首先学习视图特定的证据，可以称为从数据中收集的对每个类别的支持量。然后，我们可以构建由决策结果和可靠性组成的视图特定意见。在多视图融合阶段，我们提出了一种冲突性的意见聚合策略，并从理论上证明了该策略可以准确地建模多视图公共可靠性和视图特定可靠性的关系。在6个数据集上进行的实验验证了ECML的有效性。 et.al.|[2402.16897](http://arxiv.org/abs/2402.16897)|**[link](https://github.com/jiajunsi/rcml)**|
|**2024-02-26**|**Self Supervised Correlation-based Permutations for Multi-View Clustering**|融合来自不同模式的信息可以增强数据分析任务，包括聚类。然而，现有的多视图聚类（MVC）解决方案仅限于特定领域，或者依赖于次优且计算要求高的两阶段表示和聚类过程。我们提出了一种基于端到端深度学习的通用数据（图像、表格等）MVC框架。我们的方法包括使用一个新的基于排列的正则相关目标来学习有意义的融合数据表示。同时，我们通过在多个视图中识别一致的伪标签来学习集群分配。我们使用十个MVC基准数据集展示了我们的模型的有效性。从理论上讲，我们证明了我们的模型近似于监督线性判别分析（LDA）表示。此外，我们还提供了由伪标签注释引起的错误边界。 et.al.|[2402.16383](http://arxiv.org/abs/2402.16383)|null|
|**2024-02-26**|**DreamUp3D: Object-Centric Generative Models for Single-View 3D Scene Understanding and Real-to-Sim Transfer**|机器人应用的3D场景理解呈现出一组独特的要求，包括实时推理、以对象为中心的潜在表示学习、精确的6D姿态估计和对象的3D重建。当前的场景理解方法通常依赖于训练的模型与显式或学习的体积表示的组合，所有这些方法都有自己的缺点和局限性。我们介绍了DreamUp3D，这是一种新颖的以对象为中心的生成模型（OCGM），专门设计用于对仅由单个RGB-D图像通知的3D场景执行推理。DreamUp3D是一个端到端训练的自监督模型，能够分割对象，提供3D对象重建，生成以对象为中心的潜在表示和精确的每个对象6D姿势估计。在一系列任务中，我们将DreamUp3D与基线进行了比较，包括NeRF、预训练的CLIP特征、ObSurf和ObPose，包括3D场景重建、对象匹配和对象姿态估计。我们的实验表明，我们的模型在现实世界场景中显著优于所有基线，这表明它适用于3D场景理解任务，同时满足机器人应用中的严格要求。 et.al.|[2402.16308](http://arxiv.org/abs/2402.16308)|null|
|**2024-02-25**|**GenNBV: Generalizable Next-Best-View Policy for Active 3D Reconstruction**|尽管神经辐射领域的最新进展使大规模场景的数字化变得现实，但图像捕获过程仍然耗时耗力。以前的工作试图使用次最佳视图（NBV）策略自动进行主动三维重建。然而，现有的NBV策略在很大程度上依赖于手工制定的标准、有限的动作空间或每场景优化的表示。这些约束限制了其跨数据集的可推广性。为了克服这些问题，我们提出了GenNBV，一种端到端可推广的NBV策略。我们的策略采用了基于强化学习（RL）的框架，并将典型的有限动作空间扩展到5D自由空间。它使我们的代理无人机能够从任何角度进行扫描，甚至在训练过程中与看不见的几何形状进行交互。为了提高跨数据集的可推广性，我们还提出了一种新的多源状态嵌入，包括几何、语义和动作表示。我们使用Isaac Gym模拟器与House3K和OmniObject3D数据集建立了一个基准，以评估该NBV策略。实验表明，我们的策略在这些数据集中对看不见的建筑规模对象的覆盖率分别达到98.26%和97.12%，优于先前的解决方案。 et.al.|[2402.16174](http://arxiv.org/abs/2402.16174)|null|
|**2024-02-24**|**A Generative Machine Learning Model for Material Microstructure 3D Reconstruction and Performance Evaluation**|从二维切片重建三维微观结构被认为在预测材料的空间结构和物理性质方面具有重要价值。从当前的技术角度来看，从2D到3D的尺寸扩展被视为一个极具挑战性的反问题。近年来，基于生成对抗性网络的方法得到了广泛的关注。然而，它们仍然受到许多限制的阻碍，包括模型过于简化、需要大量的训练样本，以及在训练过程中难以实现模型收敛。有鉴于此，提出了一种新的生成模型，该模型将U-net的多尺度特性与GAN的生成能力相结合。基于此，创新构建多尺度通道聚合模块、多尺度层次特征聚合模块和卷积块注意力机制，可以更好地捕捉材料微观结构的特性，提取图像信息。通过将图像正则化损失与Wasserstein距离损失相结合，进一步提高了模型的精度。此外，本研究利用各向异性指数准确区分图像的性质，可以清楚地确定图像的各向同性和各向异性。这也是首次评估来自不同领域的材料样本的生成质量，并比较模型本身的性能。实验结果表明，该模型不仅在生成的三维结构和真实样本之间显示出非常高的相似性，而且在统计数据分析方面与真实数据高度一致。 et.al.|[2402.15815](http://arxiv.org/abs/2402.15815)|null|

<p align=right>(<a href=#updated-on-20240305>back to top</a>)</p>

## Diffusion

|Publish Date|Title|Abstract|PDF|Code|
|---|---|---|---|---|
|**2024-02-29**|**DistriFusion: Distributed Parallel Inference for High-Resolution Diffusion Models**|扩散模型在合成高质量图像方面取得了巨大成功。然而，由于巨大的计算成本，使用扩散模型生成高分辨率图像仍然具有挑战性，这导致交互式应用程序的延迟过高。在本文中，我们提出了DistriFusion，通过利用多个GPU之间的并行性来解决这个问题。我们的方法将模型输入拆分为多个补丁，并将每个补丁分配给GPU。但是，na“｛\i｝实际实现这样的算法会破坏补丁之间的交互并失去保真度，而合并这样的交互将导致巨大的通信开销。为了克服这一困境，我们观察到来自相邻扩散步骤的输入之间的高度相似性，并提出了移位补丁并行性，它利用了扩散过程的顺序性质，通过重用来自先前时间步骤的预先计算的特征图来为当前步骤提供上下文。因此，我们的方法支持异步通信，异步通信可以通过计算进行流水线处理。大量实验表明，我们的方法可以应用于最近的Stable Diffusion XL，而不会出现质量下降，并且与一个相比，八个NVIDIA A100的速度提高了6.1 $\times$ 。我们的代码公开于https://github.com/mit-han-lab/distrifuser. et.al.|[2402.19481](http://arxiv.org/abs/2402.19481)|null|
|**2024-02-29**|**Towards Generalizable Tumor Synthesis**|肿瘤合成可以在医学图像中创建人工肿瘤，有助于训练用于肿瘤检测和分割的人工智能模型。然而，肿瘤合成的成功取决于创建可在多个器官中推广的视觉逼真的肿瘤，此外，由此产生的人工智能模型能够检测来自不同领域（如医院）的图像中的真实肿瘤。这篇论文通过利用一个关键的观察结果，朝着可推广的肿瘤合成迈出了一大步：早期肿瘤（<2cm）在计算机断层扫描（CT）中往往具有相似的成像特征，无论它们起源于肝脏、胰腺还是肾脏。我们已经确定，生成性人工智能模型，例如扩散模型，即使在仅针对一个器官的有限数量的肿瘤实例进行训练时，也可以创建推广到一系列器官的真实肿瘤。此外，我们已经证明，在这些合成肿瘤上训练的人工智能模型可以被推广到从CT体积中检测和分割真实肿瘤，包括广泛的患者人口统计、成像协议和医疗机构。 et.al.|[2402.19470](http://arxiv.org/abs/2402.19470)|null|
|**2024-02-29**|**Anomalous contribution to galactic rotation curves due to stochastic spacetime**|我们考虑了一种量子引力的替代方案，其中时空度量被视为经典，即使物质场仍然是量子的。理论的一致性必然要求度量是随机演化的。在这里，我们证明了这种随机行为导致了在低加速度下广义相对论的修正。在低加速度状态下，与牛顿势产生的加速度相比，引力场产生的加速度变化很大，并起到熵力的作用，导致偏离爱因斯坦的广义相对论。我们证明，在这种“扩散机制”中，熵力从引力的角度起作用，就好像它对物质分布有贡献一样。我们通过路径积分形式计算了这是如何修改度量的期望值的，并发现由随机宇宙学常数驱动的熵力可以解释星系旋转曲线，而不需要唤起暗物质。我们警告说，在得出结论之前，需要对这种效应有更多的了解，很可能是通过数值模拟得出的，并为计算与广义相对论的偏差提供一个模板，广义相对论是时空布朗运动的实验特征。 et.al.|[2402.19459](http://arxiv.org/abs/2402.19459)|null|
|**2024-02-29**|**Listening to the Noise: Blind Denoising with Gibbs Diffusion**|近年来，去噪问题与深度生成模型的发展交织在一起。特别地，扩散模型像去噪器一样进行训练，并且它们建模的分布与贝叶斯图像中的去噪先验一致。然而，通过基于扩散的后验采样去噪需要知道噪声水平和协方差，从而防止了盲去噪。我们通过引入吉布斯扩散（GDiff）克服了这一限制，这是一种解决信号和噪声参数后验采样的通用方法。假设任意参数高斯噪声，我们开发了一种吉布斯算法，该算法交替从条件扩散模型中采样步骤，该条件扩散模型被训练为在噪声分布族之前映射信号，以及蒙特卡罗采样器来推断噪声参数。我们的理论分析突出了潜在的陷阱，指导了诊断的使用，并量化了由扩散模型引起的吉布斯平稳分布中的误差。我们展示了我们的方法：1）对涉及振幅和光谱指数未知的有色噪声的自然图像进行盲去噪；2）宇宙学问题，即宇宙微波背景数据的分析，其中“噪声”参数的贝叶斯推断意味着约束宇宙演化模型。 et.al.|[2402.19455](http://arxiv.org/abs/2402.19455)|**[link](https://github.com/rubenohana/gibbs-diffusion)**|
|**2024-02-29**|**Structure Preserving Diffusion Models**|近年来，扩散模型已成为主流的分布学习方法。在此，我们引入了保结构扩散过程，这是一个用于学习具有额外结构（如群对称性）的分布的扩散过程家族，通过发展扩散过渡步骤保持所述对称性的理论条件。在实现等变数据采样轨迹的同时，我们通过开发一组能够学习固有对称分布的不同对称等变扩散模型来举例说明这些结果。在合成数据集和真实世界数据集上进行的实证研究用于验证所开发的模型符合所提出的理论，并且能够在样本平等方面实现比现有方法更好的性能。我们还展示了在没有图像方向的先验知识的情况下，如何使用所提出的模型来实现理论上有保证的等变图像降噪。 et.al.|[2402.19369](http://arxiv.org/abs/2402.19369)|null|
|**2024-02-29**|**A new analytical model of the cosmic-ray energy flux for Galactic diffuse radio emission**|漫射同步辐射的低频无线电观测为研究从漫射星际介质（ISM）到恒星形成区域的星系内结构形成过程中气体和磁场之间的复杂关系提供了一个独特的有利位置。实现这一关键目标取决于对宇宙射线特性的全面理解，宇宙射线特性决定了相对论电子的有效能量分布，而相对论电子主要负责可观测的同步辐射。值得注意的是，能量在100 MeV和10 GeV之间的宇宙射线电子（CRe）在决定GHz范围以下的大部分天空亮度方面发挥着至关重要的作用。然而，由于太阳的调制，它们的能量通量（ $j_e$）仍然难以捉摸。我们建议通过低频无线电发射的亮度-温度光谱指数来推导星际CRe的这一能隙的观测约束，这里表示为$\β_｛\rm obs｝$。我们引入了一个新的参数分析模型，该模型根据文献中测量的50 MHz至1 GHz之间银河系漫射发射的$\beta_｛\rm obs｝$值，拟合$j_e$的可用数据。我们的模型允许考虑与低于10$\mu$ G的现有测量结果一致的磁场强度的多个观测结果。我们首次提供了垂直于视线的磁场平均分量的全天空图，并根据扩散ISM的最先进数值模拟验证了我们的方法。这项研究在用实用的参数形式模拟银河漫发射方面取得了进展。它为平方公里阵列即将到来的准备工作提供了重要的见解。 et.al.|[2402.19367](http://arxiv.org/abs/2402.19367)|null|
|**2024-02-29**|**A Novel Approach to Industrial Defect Generation through Blended Latent Diffusion Model with Online Adaptation**|有效应对工业异常检测（AD）的挑战需要充足的缺陷样本供应，而在工业环境中，缺陷样本的稀缺性往往会阻碍这一限制。本文介绍了一种新的算法，旨在增加缺陷样本，从而提高AD性能。所提出的方法对用于缺陷样本生成的混合潜在扩散模型进行了裁剪，采用扩散模型在潜在空间中生成缺陷样本。由“trimap”遮罩和文本提示控制的特征编辑过程会细化生成的样例。图像生成推理过程分为三个阶段：自由扩散阶段、编辑扩散阶段和在线解码器自适应阶段。这种复杂的推理策略产生了具有不同模式变化的高质量合成缺陷样本，从而显著提高了基于增强训练集的AD精度。具体而言，在广泛认可的MVTec AD数据集上，对于AD指标AP、IAP和IAP90，所提出的方法通过增强数据将AD的最先进（SOTA）性能分别提高了1.5%、1.9%和3.1%。这项工作的实现代码可以在GitHub存储库中找到https://github.com/GrandpaXun242/AdaBLDM.git et.al.|[2402.19330](http://arxiv.org/abs/2402.19330)|null|
|**2024-02-29**|**DiffAssemble: A Unified Graph-Diffusion Model for 2D and 3D Reassembly**|重组任务在许多领域发挥着基础性作用，存在多种方法来解决特定的重组问题。在这种情况下，我们假设一个通用的统一模型可以有效地解决所有问题，而不考虑输入数据类型（图像、3D等）。我们介绍了DiffAssemble，这是一种基于图神经网络（GNN）的体系结构，它学习使用扩散模型公式来解决重组任务。我们的方法将集合的元素（无论是2D面片还是3D对象片段）视为空间图的节点。训练是通过将噪声引入元素的位置和旋转中，并迭代地对它们进行去噪以重建相干的初始姿态来执行的。DiffAssemble在大多数2D和3D重组任务中实现了最先进的（SOTA）结果，是第一种解决旋转和平移2D难题的基于学习的方法。此外，我们强调了它显著减少了运行时间，比最快的基于优化的解谜方法快11倍。代码可在https://github.com/IIT-PAVIS/DiffAssemble et.al.|[2402.19302](http://arxiv.org/abs/2402.19302)|**[link](https://github.com/iit-pavis/diffassemble)**|
|**2024-02-29**|**Modeling the Progenitor Stars of Observed IIP Supernovae**|IIP型超新星（SNe IIP）的光度主要源于爆炸冲击电离的氢和钴的放射性衰变的复合。然而，SNe IIP与其祖恒星之间的物理联系尚不清楚。本文提出了一个综合的恒星演化模型网格及其相应的超新星光曲线（LCs），以研究观测到的SNe IIP的物理性质。这项研究采用了一维恒星演化代码。我们的模型考虑了大质量恒星演化中恒星金属性、质量和自转的影响，以及超新星建模中的爆炸能量和Ni产生。为了阐明观测到的SNe IIP的LCs并探测其祖星，我们将观测到的SNe IIP与我们的多色LCs进行了拟合，并讨论了它们的物理起源。此外，我们还研究了恒星参数对LCs的影响。祖恒星的质量、自转、金属丰度、爆炸能量和Ni产生等因素会影响光曲线的形状和持续时间。我们发现，由于大质量喷出物导致光子扩散时间增加，影响了光曲线的持续时间，因此质量较高的恒星表现出较长的平稳期。快速旋转影响恒星内部结构，增强对流混合和质量损失，可能影响平台的亮度和持续时间。更高的金属性会导致不透明度的增加，从而改变能量传输和光度。更高的爆炸能量由于更快的喷出物而导致更明亮但更短的平台。\镍的产生影响后期光度和平台持续时间，质量越大，下降速度越慢。 et.al.|[2402.19260](http://arxiv.org/abs/2402.19260)|**[link](https://github.com/astrocatalogs/OACAPI)**|
|**2024-02-29**|**Generative models struggle with kirigami metamaterials**|生成型机器学习模型在识别与特定目标特性相匹配的超材料架构方面取得了显著成功。超材料的行为主要由其内部组织决定。通过研究基里加米超材料，其中切口之间的依赖性产生了复杂的设计限制，我们证明了这种在超材料生成模型应用方面的成功可能类似于生存偏差。我们评估了四种最流行的生成模型——变分自动编码器（VAE）、生成对抗性网络（GAN）、Wasserstein GAN（WGAN）和去噪扩散概率模型（DDPM）——在生成基里加米结构方面的性能。禁止切割交叉可能会阻碍基里加米超材料的适当相似性度量的确定，从而显著影响VAE和WGAN的有效性，因为它们依赖于欧几里得距离，而欧几里得距离被证明不适合所考虑的几何形状。这对使用现代生成模型来创建各种超材料施加了重大限制。 et.al.|[2402.19196](http://arxiv.org/abs/2402.19196)|null|

<p align=right>(<a href=#updated-on-20240305>back to top</a>)</p>

## NeRF

|Publish Date|Title|Abstract|PDF|Code|
|---|---|---|---|---|
|**2024-02-28**|**NERV++: An Enhanced Implicit Neural Video Representation**|神经场，也称为隐式神经表示（INRs），在表示、生成和操作各种数据类型方面表现出了非凡的能力，允许在低内存占用下进行连续的数据重建。尽管应用于视频压缩的INRs很有前景，但仍需要大幅度提高其率失真性能，并且需要大量的参数和长时间的训练迭代来捕捉高频细节，限制了其更广泛的适用性。解决这个问题仍然是一项极具挑战性的任务，这将使INR在压缩任务中更容易访问。我们通过引入视频的神经表示NeRV++朝着解决这些缺点迈出了一步，NeRV++是一种增强的隐式神经视频表示，是对原始NeRV解码器架构的更直接但有效的增强，其特征是夹着上采样块（UB）的可分离conv2d残差块（SCRB），以及用于改进特征表示的双线性插值跳过层。NeRV++允许将视频直接表示为神经网络近似的函数，并显著增强了当前基于INR的视频编解码器之外的表示能力。我们在UVG、MCL-JVC和Bunny数据集上评估了我们的方法，在INRs的视频压缩方面取得了有竞争力的结果。这一成果缩小了与基于自动编码器的视频编码的差距，标志着基于INR的视频压缩研究迈出了重要一步。 et.al.|[2402.18305](http://arxiv.org/abs/2402.18305)|null|
|**2024-02-27**|**NIIRF: Neural IIR Filter Field for HRTF Upsampling and Personalization**|头部相关传递函数（HRTF）对于沉浸式音频是重要的，并且已经研究了它们的空间插值来对有限测量进行上采样。近年来，从声源方向映射到HRTF的神经场（NF）引起了人们的关注。现有的基于NF的方法侧重于从给定的声源方向估计HRTF的幅度，并将该幅度转换为有限脉冲响应（FIR）滤波器。我们提出了神经无限冲激响应滤波器场（NIIRF）方法来估计级联IIR滤波器的系数。IIR滤波器模拟HRTF的模态特性，因此与FIR滤波器相比，需要更少的系数来很好地近似它们。我们发现，我们的方法可以在多个数据集上匹配现有的基于NF的方法的性能，甚至在测量稀疏时优于它们。我们还探索了将NF个性化到受试者的方法，并通过实验发现低秩自适应是有效的。 et.al.|[2402.17907](http://arxiv.org/abs/2402.17907)|**[link](https://github.com/merlresearch/neural-iir-field)**|
|**2024-02-27**|**AlignMiF: Geometry-Aligned Multimodal Implicit Field for LiDAR-Camera Joint Synthesis**|神经隐式场已经成为新视图合成中事实上的标准。最近，有一些方法探索在一个领域内融合多个模态，旨在共享不同模态的隐含特征，以提高重建性能。然而，这些模态往往表现出错位行为：对一种模态（如激光雷达）进行优化可能会对另一种模态产生不利影响，如相机性能，反之亦然。在这项工作中，我们对激光雷达相机联合合成的多模式隐场进行了全面分析，揭示了潜在的问题在于不同传感器的错位。此外，我们还介绍了AlignMiF，这是一个几何对齐的多模式隐式场，具有两个拟议的模块：几何感知对齐（GAA）和共享几何初始化（SGI）。这些模块有效地调整了不同模态的粗略几何结构，显著增强了激光雷达和相机数据之间的融合过程。通过在各种数据集和场景中进行广泛的实验，我们证明了我们的方法在促进激光雷达和相机模态之间在统一的神经场中更好地交互方面的有效性。具体而言，我们提出的AlignMiF比最近的隐式融合方法（KITTI-360和Waymo数据集上的图像PSNR分别为+2.01和+3.11）实现了显著的改进，并始终超过单模态性能（在各自的数据集上，激光雷达切角距离分别减少了13.8%和14.2%）。 et.al.|[2402.17483](http://arxiv.org/abs/2402.17483)|**[link](https://github.com/tangtaogo/alignmif)**|
|**2024-02-26**|**GEM3D: GEnerative Medial Abstractions for 3D Shape Synthesis**|我们介绍了GEM3D——一种新的深度、拓扑感知的三维形状生成模型。我们的方法的关键成分是基于神经骨架的表示，对形状拓扑和几何信息进行编码。通过去噪扩散概率模型，我们的方法首先根据中轴变换（MAT）生成基于骨架的表示，然后通过骨架驱动的神经隐式公式生成曲面。神经隐式考虑了存储在生成的骨架表示中的拓扑和几何信息，以产生与以前的神经场公式相比在拓扑和几何上更准确的曲面。我们讨论了我们的方法在形状合成和点云重建任务中的应用，并对我们的方法进行了定性和定量评估。与最先进的技术相比，我们展示了更忠实的表面重建和多样化的形状生成结果，还涉及从Thingi10K和ShapeNet重建和合成结构复杂的高属形表面的挑战性场景。 et.al.|[2402.16994](http://arxiv.org/abs/2402.16994)|null|
|**2024-02-21**|**Geometry-Informed Neural Networks**|我们引入了几何知情神经网络（GINN）的概念，它包括（i）在几何约束下的学习，（ii）作为适当表示的神经场，以及（iii）为几何任务中经常遇到的不确定系统生成不同的解决方案。值得注意的是，GINN公式不需要训练数据，因此可以被视为纯粹由约束驱动的生成建模。我们添加了一个明确的多样性损失来缓解模式崩溃。我们考虑了几个约束，特别是分量的连通性，我们通过Morse理论将其转化为可微损失。在实验上，我们展示了GINN学习范式在一系列二维和三维场景中的有效性，这些场景的复杂性不断增加。 et.al.|[2402.14009](http://arxiv.org/abs/2402.14009)|null|
|**2024-02-18**|**Pattern Recognition Facilities of Extended Kalman Filtering in Stochastic Neural Fields**|在数学神经科学中，人们特别关注在存在模型不确定性的情况下，由动态神经场（DNF）建模的神经组织中的工作记忆机制。工作记忆设施意味着，由于网络中反复的相互作用，在去除外部刺激后，神经元的活动保持自我维持，并允许系统处理丢失的传感器信息。在我们之前的工作中，我们已经根据传感器提供的不完整数据开发了两种神经膜电位的重建方法。这些方法是在扩展卡尔曼滤波方法中通过使用Euler Maruyama方法和\^{o}-Taylor订单1.5的扩展。它表明\^{o}-Taylor基于EKF的恢复过程比基于Euler Maruyama的替代方案更准确。在传感器信息不完整的情况下，它提高了膜电位重建的质量。本文的目的是研究它们的模式识别功能，即在模型不确定和信息不完整的情况下，模式形成重建的质量。数值实验是以神经组织中出现多个活动区的随机DNF为例提供的。 et.al.|[2402.11551](http://arxiv.org/abs/2402.11551)|null|
|**2024-02-15**|**Reg-NF: Efficient Registration of Implicit Surfaces within Neural Fields**|神经场，即基于坐标的神经网络，最近因隐含地表示场景而广受欢迎。与基于点云等显式表示的经典方法相比，神经场提供了连续的场景表示，能够以紧凑且理想的机器人应用方式表示3D几何结构和外观。然而，有限的现有方法已经研究了通过直接利用这些连续的隐式表示来配准多个神经场。在本文中，我们提出了Reg-NF，这是一种基于神经场的配准，它优化了两个任意神经场之间的相对6-DoF变换，即使这两个场具有不同的比例因子。Reg NF的关键组成部分包括双向配准损失、多视图表面采样和体积符号距离函数（SDF）的利用。我们在一个新的神经场数据集上展示了我们的方法，用于评估配准问题。我们提供了一组详尽的实验和消融研究，以确定我们的方法的性能，同时也讨论了局限性，为研究界在无约束环境中利用神经场的开放挑战提供了未来的方向。 et.al.|[2402.09722](http://arxiv.org/abs/2402.09722)|null|
|**2024-02-12**|**Unsupervised Discovery of Object-Centric Neural Fields**|我们研究从单个图像中推断3D以对象为中心的场景表示。虽然最近的方法在从简单的合成图像中无监督地发现3D对象方面显示出了潜力，但它们未能推广到具有视觉丰富和多样化对象的真实世界场景。这种限制源于它们的对象表示，它将对象的内在属性（如形状和外观）与外在的、以观察者为中心的属性（如3D位置）纠缠在一起。为了解决这一瓶颈，我们提出了以对象为中心的神经场的无监督发现（uOCF）。uOCF专注于学习对象的内在，并分别对外在进行建模。我们的方法显著提高了系统泛化能力，从而能够从稀疏的真实世界图像中无监督地学习高保真的以对象为中心的场景表示。为了评估我们的方法，我们收集了三个新的数据集，包括两个真实的厨房环境。大量实验表明，uOCF能够在无监督的情况下从单个真实图像中发现视觉丰富的对象，从而实现3D对象分割和场景操作等应用。值得注意的是，uOCF演示了对单个真实图像中看不见的物体的零样本泛化。项目页面：https://red-fairy.github.io/uOCF/ et.al.|[2402.07376](http://arxiv.org/abs/2402.07376)|null|
|**2024-02-06**|**Improved Generalization of Weight Space Networks via Augmentations**|在深度权重空间（DWS）中学习，神经网络处理其他神经网络的权重，是一个新兴的研究方向，应用于2D和3D神经领域（INRs、NeRFs），以及对其他类型的神经网络进行推断。不幸的是，权重空间模型往往存在严重的过拟合问题。我们实证分析了这种过拟合的原因，发现一个关键原因是DWS数据集缺乏多样性。虽然给定的对象可以用许多不同的权重配置来表示，但典型的INR训练集无法捕捉表示同一对象的INR之间的可变性。为了解决这一问题，我们探索了在权重空间中增加数据的策略，并提出了一种适用于权重空间的MixUp方法。我们在两个设置中展示了这些方法的有效性。在分类方面，它们可以提高性能，类似于拥有10倍以上的数据。在自我监督的对比学习中，它们在下游分类中产生了5-10%的显著收益。 et.al.|[2402.04081](http://arxiv.org/abs/2402.04081)|null|
|**2024-01-31**|**BlockFusion: Expandable 3D Scene Generation using Latent Tri-plane Extrapolation**|我们介绍了BlockFusion，这是一种基于扩散的模型，它将3D场景生成为单元块，并无缝地合并新的块来扩展场景。BlockFusion使用从完整的3D场景网格中随机裁剪的3D块的数据集进行训练。通过逐块拟合，所有训练块都被转换为混合神经场：具有包含几何特征的三平面，然后是用于解码有符号距离值的多层感知器（MLP）。采用变分自动编码器将三平面压缩到潜在的三平面空间中，在该空间上进行去噪扩散处理。应用于潜在表示的扩散允许高质量和多样化的3D场景生成。要在生成过程中扩展场景，只需附加空块以与当前场景重叠，并外推现有的潜在三平面以填充新块。外推是通过在去噪迭代过程中使用来自重叠三平面的特征样本来调节生成过程来完成的。潜在的三平面外推法产生语义和几何上有意义的过渡，与现有场景和谐融合。2D布局调节机制用于控制场景元素的放置和布置。实验结果表明，BlockFusion能够在室内和室外场景中生成具有前所未有的高质量形状的多样化、几何一致和无边界的大型3D场景。 et.al.|[2401.17053](http://arxiv.org/abs/2401.17053)|null|

<p align=right>(<a href=#updated-on-20240305>back to top</a>)</p>

[contributors-shield]: https://img.shields.io/github/contributors/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[contributors-url]: https://github.com/Vincentqyw/cv-arxiv-daily/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[forks-url]: https://github.com/Vincentqyw/cv-arxiv-daily/network/members
[stars-shield]: https://img.shields.io/github/stars/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[stars-url]: https://github.com/Vincentqyw/cv-arxiv-daily/stargazers
[issues-shield]: https://img.shields.io/github/issues/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[issues-url]: https://github.com/Vincentqyw/cv-arxiv-daily/issues

