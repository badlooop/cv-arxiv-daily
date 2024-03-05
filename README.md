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
|**2024-03-02**|**NeRF-VPT: Learning Novel View Representations with Neural Radiance Fields via View Prompt Tuning**|神经辐射场（NeRF）在新视图合成中取得了显著的成功。尽管如此，为新颖的视图生成高质量图像的任务仍然是一个关键的挑战。虽然现有的努力取得了值得称赞的进展，但捕捉复杂的细节、增强纹理和实现卓越的峰值信噪比（PSNR）指标值得进一步关注和进步。在这项工作中，我们提出了NeRF VPT，这是一种用于新视图合成的创新方法，以应对这些挑战。我们提出的NeRF VPT采用级联视图提示调整范式，其中从先前渲染结果中获得的RGB信息作为后续渲染阶段的指导性视觉提示，期望嵌入提示中的先验知识可以促进渲染图像质量的逐步增强。NeRF VPT只需要在每个训练阶段从前一阶段渲染中采样RGB数据作为先验，而不需要依赖额外的指导或复杂的技术。因此，我们的NeRF VPT是即插即用的，可以很容易地集成到现有的方法中。通过在要求苛刻的真实场景基准上对我们的NeRF VPT与几种基于NeRF的方法进行比较分析，如真实合成360、真实前向、副本数据集和用户捕获的数据集，我们证实，与所有最先进的方法相比，我们的NeRF VPT显著提高了基线性能，并能熟练地生成更高质量的新视图图像。此外，NeRF VPT的级联学习引入了对具有稀疏输入的场景的适应性，从而显著提高了稀疏视图新视图合成的准确性。源代码和数据集位于\url{https://github.com/Freedomcls/NeRF-VPT}. et.al.|[2403.01325](http://arxiv.org/abs/2403.01325)|**[link](https://github.com/freedomcls/nerf-vpt)**|
|**2024-03-02**|**Neural Field Classifiers via Target Encoding and Classification Loss**|神经场方法在计算机视觉和计算机图形学中的各种长期任务中取得了巨大进展，包括新颖的视图合成和几何重建。由于现有的神经场方法试图预测一些基于坐标的连续目标值，例如神经辐射场（NeRF）的RGB，所有这些方法都是回归模型，并通过一些回归损失进行优化。然而，对于神经场方法来说，回归模型真的比分类模型更好吗？在这项工作中，我们试图从机器学习的角度来探讨神经领域这个非常基本但被忽视的问题。我们成功地提出了一种新的神经场分类器（NFC）框架，该框架将现有的神经场方法公式化为分类任务，而不是回归任务。所提出的NFC可以通过使用新的目标编码模块和优化分类损失，轻松地将任意神经场回归器（NFR）转换为其分类变体。通过将连续回归目标编码为高维离散编码，我们自然地形成了多标签分类任务。大量的实验证明了NFC在几乎免费的额外计算成本下令人印象深刻的有效性。此外，NFC还显示出对稀疏输入、损坏图像和动态场景的鲁棒性。 et.al.|[2403.01058](http://arxiv.org/abs/2403.01058)|null|
|**2024-02-29**|**ViewFusion: Towards Multi-View Consistency via Interpolated Denoising**|通过扩散模型进行的新型视图合成在生成多样化和高质量图像方面表现出了显著的潜力。然而，在这些主流方法中，图像生成的独立过程导致了在保持多视图一致性方面的挑战。为了解决这一问题，我们引入了ViewFusion，这是一种新颖的无训练算法，可以无缝集成到现有的预训练扩散模型中。我们的方法采用了一种自回归方法，该方法隐式地利用先前生成的视图作为下一个视图生成的上下文，确保了在新视图生成过程中强大的多视图一致性。通过通过插值去噪融合已知视图信息的扩散过程，我们的框架成功地扩展了单视图条件模型，使其在多视图条件设置下工作，而无需任何额外的微调。大量的实验结果证明了ViewFusion在生成一致且详细的新视图方面的有效性。 et.al.|[2402.18842](http://arxiv.org/abs/2402.18842)|**[link](https://github.com/Wi-sc/ViewFusion)**|
|**2024-02-28**|**PolyOculus: Simultaneous Multi-view Image-based Novel View Synthesis**|本文考虑了生成新视图合成（GNVS）的问题，即在给定有限数量的已知视图的情况下生成场景的新颖、合理的视图。在这里，我们提出了一个基于集合的生成模型，该模型可以同时生成多个自洽的新视图，条件是任何数量的已知视图。我们的方法不限于一次生成单个图像，并且可以以零、一个或多个视图为条件。因此，当生成大量视图时，我们的方法不限于低阶自回归生成方法，并且能够更好地在大图像集上保持生成的图像质量。我们在标准NVS数据集上评估了所提出的模型，并表明它优于最先进的基于图像的GNVS基线。此外，我们表明，该模型能够生成没有自然顺序的相机视图集，如循环和双目轨迹，并且在此类任务上显著优于其他方法。 et.al.|[2402.17986](http://arxiv.org/abs/2402.17986)|null|
|**2024-02-27**|**AlignMiF: Geometry-Aligned Multimodal Implicit Field for LiDAR-Camera Joint Synthesis**|神经隐式场已经成为新视图合成中事实上的标准。最近，有一些方法探索在一个领域内融合多个模态，旨在共享不同模态的隐含特征，以提高重建性能。然而，这些模态往往表现出错位行为：对一种模态（如激光雷达）进行优化可能会对另一种模态产生不利影响，如相机性能，反之亦然。在这项工作中，我们对激光雷达相机联合合成的多模式隐场进行了全面分析，揭示了潜在的问题在于不同传感器的错位。此外，我们还介绍了AlignMiF，这是一个几何对齐的多模式隐式场，具有两个拟议的模块：几何感知对齐（GAA）和共享几何初始化（SGI）。这些模块有效地调整了不同模态的粗略几何结构，显著增强了激光雷达和相机数据之间的融合过程。通过在各种数据集和场景中进行广泛的实验，我们证明了我们的方法在促进激光雷达和相机模态之间在统一的神经场中更好地交互方面的有效性。具体而言，我们提出的AlignMiF比最近的隐式融合方法（KITTI-360和Waymo数据集上的图像PSNR分别为+2.01和+3.11）实现了显著的改进，并始终超过单模态性能（在各自的数据集上，激光雷达切角距离分别减少了13.8%和14.2%）。 et.al.|[2402.17483](http://arxiv.org/abs/2402.17483)|**[link](https://github.com/tangtaogo/alignmif)**|
|**2024-02-26**|**GEA: Reconstructing Expressive 3D Gaussian Avatar from Monocular Video**|本文提出了GEA，这是一种基于3D高斯的身体和手的高保真重建来创建富有表现力的3D化身的新方法。关键贡献有两方面。首先，我们设计了一种两阶段姿态估计方法，以从输入图像中获得准确的SMPL-X姿态，从而在训练图像的像素和SMPL-X模型之间提供正确的映射。它使用注意力感知网络和优化方案来对齐图像中估计的SMPL-X身体和真实身体之间的法线和轮廓。其次，我们提出了一种迭代重新初始化策略来处理高斯表示所面临的不平衡聚合和初始化偏差。该策略迭代地重新分布化身的高斯点，通过应用网格划分、重采样和重高斯运算，使其均匀分布在人体表面附近。结果，可以实现更高质量的渲染。大量的实验分析验证了所提出的模型的有效性，表明它在逼真的新视图合成中实现了最先进的性能，同时提供了对人体和手部姿势的细粒度控制。项目页面：https://3d-aigc.github.io/GEA/. et.al.|[2402.16607](http://arxiv.org/abs/2402.16607)|null|
|**2024-02-26**|**CMC: Few-shot Novel View Synthesis via Cross-view Multiplane Consistency**|神经辐射场（NeRF）由于其连续表示场景的能力，在新颖的视图合成中，特别是在虚拟现实（VR）和增强现实（AR）中，显示出了令人印象深刻的结果。然而，当只有几个输入视图图像可用时，NeRF倾向于过度拟合给定视图，从而使像素的估计深度共享几乎相同的值。与以前通过引入复杂的先验或额外的监督来进行正则化的方法不同，我们提出了一种简单而有效的方法，该方法明确地在输入视图之间建立深度感知一致性，以应对这一挑战。我们的关键见解是，通过强制在不同的输入视图中重复采样相同的空间点，我们能够加强视图之间的相互作用，从而缓解过拟合问题。为了实现这一点，我们在分层表示（\textit｛即｝多平面图像）上建立神经网络，因此可以在多个离散平面上对采样点进行重新采样。此外，为了正则化看不见的目标视图，我们将不同输入视图的渲染颜色和深度约束为相同。尽管简单，但大量的实验表明，与最先进的方法相比，我们提出的方法可以获得更好的合成质量。 et.al.|[2402.16407](http://arxiv.org/abs/2402.16407)|null|
|**2024-02-26**|**FrameNeRF: A Simple and Efficient Framework for Few-shot Novel View Synthesis**|我们提出了一种新的框架，称为FrameNeRF，旨在将现成的快速高保真NeRF模型应用于少镜头的新颖视图合成任务，该模型具有快速训练速度和高渲染质量。快速高保真度模型的训练稳定性通常局限于密集视图，这使得它们不适合于少镜头的新颖视图合成任务。为了解决这一限制，我们利用正则化模型作为数据生成器，从稀疏输入中生成密集视图，从而促进快速高保真模型的后续训练。由于这些密集视图是由正则化模型生成的伪地面实况，因此使用原始稀疏图像来微调快速高保真度模型。这个过程有助于模型学习真实的细节，并更正早期阶段引入的工件。通过利用现成的正则化模型和快速高保真度模型，我们的方法在各种基准数据集上实现了最先进的性能。 et.al.|[2402.14586](http://arxiv.org/abs/2402.14586)|null|
|**2024-02-22**|**TaylorGrid: Towards Fast and High-Quality Implicit Field Learning via Direct Taylor-based Grid Optimization**|基于坐标的神经隐式表示或隐式场已被广泛研究用于3D几何表示或新颖视图合成。近年来，人们致力于加快基于坐标的内隐场学习的速度和提高其质量。代替学习重MLP来预测查询坐标的神经隐式值，已经提出了与浅MLP相结合的神经体素或网格来实现具有减少的优化时间的高质量隐式场学习。另一方面，为了进一步提高学习速度，已经提出了诸如线性网格之类的轻量级场表示。在本文中，我们的目标是快速和高质量的隐场学习，并提出了TaylorGrid，这是一种新的隐场表示，可以在2D或3D网格上通过直接泰勒展开优化有效地计算。一般来说，TaylorGrid可以适用于不同的内隐场学习任务，如SDF学习或NeRF。通过广泛的定量和定性比较，TaylorGrid实现了线性网格和神经体素之间的平衡，显示了其在快速和高质量的内隐场学习中的优势。 et.al.|[2402.14415](http://arxiv.org/abs/2402.14415)|null|
|**2024-02-20**|**Improving Robustness for Joint Optimization of Camera Poses and Decomposed Low-Rank Tensorial Radiance Fields**|在本文中，我们提出了一种算法，该算法允许仅使用2D图像作为监督，对由分解的低秩张量表示的相机姿态和场景几何进行联合细化。首先，我们基于1D信号进行了一项试点研究，并将我们的发现与3D场景联系起来，在3D场景中，基于体素的NeRF上的初始关节姿态优化可以很容易地导致次优解。此外，基于频谱分析，我们建议在2D和3D辐射场上应用卷积高斯滤波器，以实现从粗到细的训练计划，从而实现联合相机姿态优化。利用分解后的低秩张量中的分解特性，我们的方法实现了与强力3D卷积等效的效果，只需很少的计算开销。为了进一步提高联合优化的鲁棒性和稳定性，我们还提出了平滑的2D监督、随机缩放的核参数和边缘引导的损失掩模技术。广泛的定量和定性评估表明，我们提出的框架在新的视图合成方面取得了卓越的性能，并实现了快速收敛的优化。 et.al.|[2402.13252](http://arxiv.org/abs/2402.13252)|**[link](https://github.com/nemo1999/joint-tensorf)**|

<p align=right>(<a href=#updated-on-20240305>back to top</a>)</p>

## 3D Reconstruction

|Publish Date|Title|Abstract|PDF|Code|
|---|---|---|---|---|
|**2024-03-01**|**G3DR: Generative 3D Reconstruction in ImageNet**|我们介绍了一种新的3D生成方法，即ImageNet中的生成3D重建（G3DR），该方法能够从单个图像中生成各种高质量的3D对象，解决了现有方法的局限性。我们框架的核心是一种新颖的深度正则化技术，它能够生成具有高几何保真度的场景。G3DR还利用预训练的语言视觉模型，如CLIP，实现新视图中的重建，并提高几代人的视觉逼真度。此外，G3DR设计了一种简单但有效的采样程序，以进一步提高世代的质量。G3DR提供基于类或文本条件的多样化且高效的3D资产生成。尽管G3DR很简单，但它能够击败最先进的方法，在感知指标和几何得分方面比它们提高了22%和90%，而只需要一半的训练时间。代码位于https://github.com/preddy5/G3DR et.al.|[2403.00939](http://arxiv.org/abs/2403.00939)|null|
|**2024-03-01**|**DISORF: A Distributed Online NeRF Training and Rendering Framework for Mobile Robots**|我们提出了一个框架DISORF，用于对资源受限的移动机器人和边缘设备捕获的场景进行在线3D重建和可视化。为了解决边缘设备的有限计算能力和潜在的有限网络可用性，我们设计了一个在边缘设备和远程服务器之间有效分配计算的框架。我们利用设备上的SLAM系统生成姿势关键帧，并将其传输到远程服务器，远程服务器可以通过利用NeRF模型在运行时执行高质量的3D重建和可视化。我们发现了在线NeRF训练的一个关键挑战，在该挑战中，天真的图像采样策略可能导致渲染质量的显著下降。我们提出了一种新的移位指数帧采样方法，以解决在线NeRF训练的这一挑战。我们展示了我们的框架在实现未知场景的高质量实时重建和可视化方面的有效性，因为这些场景是从移动机器人和边缘设备中的相机捕获和流式传输的。 et.al.|[2403.00228](http://arxiv.org/abs/2403.00228)|null|
|**2024-02-29**|**VEnvision3D: A Synthetic Perception Dataset for 3D Multi-Task Model Research**|开发统一的多任务基础模型已成为计算机视觉研究中的一个关键挑战。在当前的3D计算机视觉领域，大多数数据集只关注相对有限的一组任务，这使各种下游任务的并行训练要求复杂化。这使得多目标网络的训练难以进行，进一步阻碍了三维视觉领域基础模型的发展。在本文中，我们介绍了VEnvision3D，这是一个用于多任务学习的大型3D合成感知数据集，包括深度完成、分割、上采样、位置识别和3D重建。由于每个任务的数据都是在相同的场景中收集的，因此任务在使用的数据方面本质上是一致的。因此，这样一个独特的属性可以帮助探索多任务模型甚至基础模型的潜力，而无需单独的训练方法。基于所提出的数据集的特点，提出了几个新的基准。对端到端模型进行了广泛的研究，揭示了新的观察结果、挑战和未来研究的机会。此外，我们设计了一个直接的多任务网络，以揭示VEnvision3D可以为基础模型提供的能力。我们的数据集和代码将在接受后开源。 et.al.|[2402.19059](http://arxiv.org/abs/2402.19059)|null|
|**2024-02-29**|**ViewFusion: Towards Multi-View Consistency via Interpolated Denoising**|通过扩散模型进行的新型视图合成在生成多样化和高质量图像方面表现出了显著的潜力。然而，在这些主流方法中，图像生成的独立过程导致了在保持多视图一致性方面的挑战。为了解决这一问题，我们引入了ViewFusion，这是一种新颖的无训练算法，可以无缝集成到现有的预训练扩散模型中。我们的方法采用了一种自回归方法，该方法隐式地利用先前生成的视图作为下一个视图生成的上下文，确保了在新视图生成过程中强大的多视图一致性。通过通过插值去噪融合已知视图信息的扩散过程，我们的框架成功地扩展了单视图条件模型，使其在多视图条件设置下工作，而无需任何额外的微调。大量的实验结果证明了ViewFusion在生成一致且详细的新视图方面的有效性。 et.al.|[2402.18842](http://arxiv.org/abs/2402.18842)|**[link](https://github.com/Wi-sc/ViewFusion)**|
|**2024-02-28**|**The Role of a Neutron Component in the Photospheric Emission of Long-Duration Gamma-Ray Burst Jets**|长时间伽马射线暴（LGRB）被认为是在核心坍塌超新星期间产生的，可能在流出物质中有显著的中子成分。如果存在，中子可以通过降低其不透明度来改变光子在外流中的散射方式，从而使光子比没有中子的情况下更快地解耦。因此，了解这一过程的细节可以让我们探索LGRB的中心引擎，否则它是隐藏的。在这里，我们使用相对论流体动力学模拟和使用蒙特卡罗辐射转移（MCRaT）代码的辐射转移后处理相结合的方法，给出了LGRB喷流的光球发射结果。我们通过改变平衡电子分数 $Y_｛e｝$来控制喷流材料中中子组分的大小，我们发现GRB火球中中子的存在会影响能带参数$\alpha$和$e_｛0｝$，而带有$\beta$参数的图片则不太清楚。特别地，断裂能量$E_{0}$ 被转移到更高的能量。此外，我们发现，增加中子分量的大小也会增加多个视角下流出的总辐射能量。我们的研究结果不仅揭示了LGRB，而且与与双星中子星合并相关的短时间伽马射线爆发有关，因为在这样的系统中可能存在突出的中子成分。 et.al.|[2402.18657](http://arxiv.org/abs/2402.18657)|null|
|**2024-02-27**|**Sora Generates Videos with Stunning Geometrical Consistency**|最近开发的索拉模型[1]在视频生成方面表现出了非凡的能力，引发了关于其模拟真实世界现象能力的激烈讨论。尽管它越来越受欢迎，但缺乏既定的指标来定量评估它对现实世界物理的保真度。在本文中，我们介绍了一种新的基准，该基准基于视频对真实世界物理原理的遵守程度来评估生成视频的质量。我们采用了一种将生成的视频转换为3D模型的方法，利用了3D重建的准确性在很大程度上取决于视频质量的前提。从3D重建的角度来看，我们使用所构建的3D模型所满足的几何约束的保真度作为代理来衡量生成的视频在多大程度上符合真实世界的物理规则。项目页面：https://sora-geometrical-consistency.github.io/ et.al.|[2402.17403](http://arxiv.org/abs/2402.17403)|null|
|**2024-02-27**|**CharNeRF: 3D Character Generation from Concept Art**|3D建模在AR/VR和游戏领域具有重要意义，既有艺术创意，也有实际应用。然而，这个过程往往很耗时，而且需要很高的技能水平。在本文中，我们提出了一种新的方法，从一致的周转概念艺术中创建3D角色的体积表示，这是3D建模行业的标准输入。虽然神经辐射场（NeRF）已经改变了基于图像的3D重建的游戏规则，但据我们所知，还没有已知的研究可以优化概念艺术的管道。为了利用概念艺术的潜力，通过其定义的身体姿势和特定的视角，我们建议将其编码为我们模型的先验。我们训练网络，通过可学习的视图方向关注的多头自注意层，将这些先验用于各种3D点。此外，我们还证明了射线采样和表面采样的结合增强了我们网络的推理能力。我们的模型能够生成高质量的360度字符视图。随后，我们提供了一个简单的指南，以更好地利用我们的模型来提取3D网格。需要注意的是，我们模型的推理能力受到训练数据特征的影响，主要集中在具有单头、双臂和双腿的角色上。尽管如此，我们的方法仍然是通用的，适用于来自不同主题的概念艺术，而不会对数据强加任何具体的假设。 et.al.|[2402.17115](http://arxiv.org/abs/2402.17115)|null|
|**2024-02-26**|**Self Supervised Correlation-based Permutations for Multi-View Clustering**|融合来自不同模式的信息可以增强数据分析任务，包括聚类。然而，现有的多视图聚类（MVC）解决方案仅限于特定领域，或者依赖于次优且计算要求高的两阶段表示和聚类过程。我们提出了一种基于端到端深度学习的通用数据（图像、表格等）MVC框架。我们的方法包括使用一个新的基于排列的正则相关目标来学习有意义的融合数据表示。同时，我们通过在多个视图中识别一致的伪标签来学习集群分配。我们使用十个MVC基准数据集展示了我们的模型的有效性。从理论上讲，我们证明了我们的模型近似于监督线性判别分析（LDA）表示。此外，我们还提供了由伪标签注释引起的错误边界。 et.al.|[2402.16383](http://arxiv.org/abs/2402.16383)|null|
|**2024-02-26**|**DreamUp3D: Object-Centric Generative Models for Single-View 3D Scene Understanding and Real-to-Sim Transfer**|机器人应用的3D场景理解呈现出一组独特的要求，包括实时推理、以对象为中心的潜在表示学习、精确的6D姿态估计和对象的3D重建。当前的场景理解方法通常依赖于训练的模型与显式或学习的体积表示的组合，所有这些方法都有自己的缺点和局限性。我们介绍了DreamUp3D，这是一种新颖的以对象为中心的生成模型（OCGM），专门设计用于对仅由单个RGB-D图像通知的3D场景执行推理。DreamUp3D是一个端到端训练的自监督模型，能够分割对象，提供3D对象重建，生成以对象为中心的潜在表示和精确的每个对象6D姿势估计。在一系列任务中，我们将DreamUp3D与基线进行了比较，包括NeRF、预训练的CLIP特征、ObSurf和ObPose，包括3D场景重建、对象匹配和对象姿态估计。我们的实验表明，我们的模型在现实世界场景中显著优于所有基线，这表明它适用于3D场景理解任务，同时满足机器人应用中的严格要求。 et.al.|[2402.16308](http://arxiv.org/abs/2402.16308)|null|
|**2024-02-25**|**GenNBV: Generalizable Next-Best-View Policy for Active 3D Reconstruction**|尽管神经辐射领域的最新进展使大规模场景的数字化变得现实，但图像捕获过程仍然耗时耗力。以前的工作试图使用次最佳视图（NBV）策略自动进行主动三维重建。然而，现有的NBV策略在很大程度上依赖于手工制定的标准、有限的动作空间或每场景优化的表示。这些约束限制了其跨数据集的可推广性。为了克服这些问题，我们提出了GenNBV，一种端到端可推广的NBV策略。我们的策略采用了基于强化学习（RL）的框架，并将典型的有限动作空间扩展到5D自由空间。它使我们的代理无人机能够从任何角度进行扫描，甚至在训练过程中与看不见的几何形状进行交互。为了提高跨数据集的可推广性，我们还提出了一种新的多源状态嵌入，包括几何、语义和动作表示。我们使用Isaac Gym模拟器与House3K和OmniObject3D数据集建立了一个基准，以评估该NBV策略。实验表明，我们的策略在这些数据集中对看不见的建筑规模对象的覆盖率分别达到98.26%和97.12%，优于先前的解决方案。 et.al.|[2402.16174](http://arxiv.org/abs/2402.16174)|null|

<p align=right>(<a href=#updated-on-20240305>back to top</a>)</p>

## Diffusion

|Publish Date|Title|Abstract|PDF|Code|
|---|---|---|---|---|
|**2024-03-02**|**Bespoke Non-Stationary Solvers for Fast Sampling of Diffusion and Flow Models**|本文介绍了定制的非稳态（BNS）求解器，这是一种求解器蒸馏方法，用于提高扩散和流动模型的样本效率。BNS解算器基于一系列非平稳解算器，这些解算器可证明包含了现有的数值ODE解算器并因此在这些基线上证明了样本近似（PSNR）的显著改进。与模型蒸馏相比，BNS解算器受益于微小的参数空间（ $<$ 200参数）、快速优化（快两个数量级）、保持样本的多样性，并且与以前的解算器蒸馏方法相比，蒸馏方法几乎缩小了与标准蒸馏方法（如低-中NFE状态下的渐进蒸馏）的差距。例如，BNS求解器使用类条件ImageNet-64中的16个NFE来实现45 PSNR/1.76 FID。我们用BNS解算器进行了条件图像生成、文本到图像生成和文本到音频生成的实验，显示出样本近似（PSNR）的显著改进。 et.al.|[2403.01329](http://arxiv.org/abs/2403.01329)|null|
|**2024-03-02**|**Longtime behavior of semilinear multi-term fractional in time diffusion**|本文分析了一类具有多重分数阶Caputo导数的半线性积分微分方程的初边值问题。这个方程的一个特殊情况模拟了氧气通过毛细管的扩散。在对系数和非线性的适当假设下，讨论了解的长期行为（如 $t\to+\infty$ ）。特别地，在适当的函数空间中建立了吸收集的存在性。 et.al.|[2403.01302](http://arxiv.org/abs/2403.01302)|null|
|**2024-03-02**|**Anomalous mass dependency in Hydra endoderm cell cluster diffusion**|组织组织在形态发生、伤口愈合和癌症转移中起着至关重要的作用。Hydra以其再生能力而闻名，是研究细胞结构的优秀模型，特别是在细胞簇的模式形成和扩散方面。已建立的实验方案能够通过光学显微镜检查再生和组织分离。最近的实验挑战了以前的理论，认为细胞的集体行为是水螅细胞聚集组织的关键因素。利用Hydra分离实验荧光图像的图像处理技术，我们跟踪内胚层细胞簇，并研究其扩散常数与簇大小之间的关系。与在非活性物质中观察到的结果相反，我们发现扩散对团簇质量的依赖性几乎是恒定的。这一发现有助于理解最近实验中观测到的快速分离，并对一般的细胞组织过程有意义。 et.al.|[2403.01294](http://arxiv.org/abs/2403.01294)|null|
|**2024-03-02**|**On the Arnold diffusion mechanism in Medium Earth Orbit**|空间碎片缓减准则是保护环地环境的最有效方法。其中，报废处置解决方案发挥着关键作用。越来越多的人致力于利用自然扰动引导卫星重返大气层，从而降低处置成本，如果卫星离开高海拔地区也是如此。在导航卫星（如伽利略）所在的中地球轨道区域的情况下，主要驱动因素是月球引起的引力扰动，从长远来看，这会增加离心率。通过这种方式，中心附近的高度可以进入大气阻力域，卫星最终可以重新进入。在这项工作中，我们展示了Arnold扩散机制是如何触发离心率增长的。以伽利略为例，我们考虑了一系列哈密顿模型，假设航天器运动的主要扰动是地球的扁率和月球的引力。首先，假设月球位于黄道平面上，在给定共振附近，计算不同能级的周期轨道和相关的稳定和不稳定不变流形。沿着每个不变流形，离心率自然增加，在它们之间的第一个交点处达到最大值。然而，这种增长不足以实现重返社会。通过移动到一个考虑到月球倾角的模型，这个问题变得不自主，卫星能够沿着不同的能级移动。在对自治情况下流形的横截性进行模拟的情况下，通过数值检验，应用庞加莱-梅尔尼科夫技术来展示如何通过构建一系列同宿轨道来实现扩散，这些同宿轨道连接不同能级的不变环面。 et.al.|[2403.01283](http://arxiv.org/abs/2403.01283)|null|
|**2024-03-02**|**Rigidity results for group von Neumann algebras with diffuse center**|我们介绍了具有无限中心的群 $G$的第一个例子，这些群在自然意义上可以从它们的von Neumann代数$\mathcal{L}（G）$中完全识别。具体地说，假设$G=A\乘以W$，其中$A$是无限阿贝尔群，$W$是具有性质（T）和平凡阿贝尔化的ICC环状乘积群[CIOS22a；AMCOS23]。然后，只要$H$是一个\emph｛任意｝群，使得$\mathcal｛L｝（G）$与$\mathical L（H）$同构，通过一个保持规范迹的\emph{任意}$\ast$同构，就必须是$H＝B\次H_0$的情况，其中$B$是无限阿贝尔的，$H_0$同构于$W$。此外，我们完全描述了$\mathcalL（G）$和$\mathcal L（H）$之间的$\ast$同构。这为群C$^*$-代数的分类提供了新的应用，包括不可服从群的例子，这些群可以从它们的约化C$^**$ -代数中恢复，但不能从它们的von Neumann代数中恢复。 et.al.|[2403.01280](http://arxiv.org/abs/2403.01280)|null|
|**2024-03-02**|**Analyzing the transport coefficients and observables of a rotating QGP medium in kinetic theory framework with a novel approach to the collision integral**|在本工作中，我们研究了QGP介质的旋转如何影响重离子碰撞中的输运系数和可观察性。对于非中心碰撞，尽管大部分角动量被观众带走，但在角速度范围有限的情况下，仍然存在有限的角动量，从而引发所产生物质的旋转。因此，QGP介质的各种性质可能会受到旋转的调制。我们利用动力学理论计算了输运系数和可观察性，如电导率、热导率、克努森数、椭圆流、定压比热、定容比热、痕量异常、热扩散常数和等温压缩性，以观察旋转对它们的影响。特别地，我们使用相对论玻尔兹曼输运方程中碰撞积分的新弛豫时间近似来导出输运系数，并将其与动力学理论方法中的弛豫时间逼近中的值以及有限角速度进行比较。我们发现角速度在介质中起着重要作用，并增强了电荷和热量的流动。此外，与弛豫时间近似相比，电导率和热导率在新的弛豫时间逼近中具有较小的值，并且所述近似中的电导率之间的这些差异在高温下比在低温下更明显。此外，发现所有上述可观察器都对QGP介质的旋转敏感。 et.al.|[2403.01240](http://arxiv.org/abs/2403.01240)|null|
|**2024-03-02**|**DiffSal: Joint Audio and Video Learning for Diffusion Saliency Prediction**|视听显著性预测可以从不同的模态互补中获得支持，但进一步的性能增强仍然受到定制架构和特定任务损失函数的挑战。在最近的研究中，去噪扩散模型由于其固有的泛化能力，在统一任务框架方面显示出更大的前景。基于这一动机，本文提出了一种新的广义视听显著性预测的扩散结构（DiffSal），该结构利用输入音频和视频作为条件，将预测问题公式化为显著性图的条件生成任务。基于时空视听特征，设计了一个额外的网络显著性UNet来执行多模式注意力调制，以从噪声图中逐步细化地面实况显著性图。大量实验表明，所提出的DiffSal可以在六个具有挑战性的视听基准上实现出色的性能，在六个指标上比以前最先进的结果平均相对改进6.3\%。 et.al.|[2403.01226](http://arxiv.org/abs/2403.01226)|null|
|**2024-03-02**|**TCIG: Two-Stage Controlled Image Generation with Quality Enhancement through Diffusion**|近年来，在文本到图像生成模型的开发方面取得了重大进展。然而，当涉及到在发电过程中实现完全可控性时，这些模型仍然面临限制。通常，需要特定的训练或使用有限的模型，即使这样，它们也有一定的限制。为了应对这些挑战，提出了一种在图像生成中有效地结合可控性和高质量的两阶段方法。这种方法利用预先训练的模型的专业知识来实现对生成图像的精确控制，同时还利用扩散模型的力量来实现最先进的质量。该方法将可控性与高质量分离开来，取得了显著的效果。它与潜影和图像空间扩散模型兼容，确保了多功能性和灵活性。此外，这种方法始终产生与该领域当前最先进的方法相当的结果。总的来说，这种提出的方法代表了文本到图像生成的显著进步，在不影响生成图像质量的情况下提高了可控性。 et.al.|[2403.01212](http://arxiv.org/abs/2403.01212)|null|
|**2024-03-02**|**Atacama Large Aperture Submillimeter Telescope (AtLAST) science: Gas and dust in nearby galaxies**|了解调节恒星形成和星系演化的物理过程是现代天体物理学的主要活动领域。附近的星系提供了独特的机会，可以从亚星系（kpc）尺度到亚云（sub-pc）尺度，从静止星系到恒星爆发，从场星系到超密度，详细检查星际介质（ISM）、恒星形成（SF）、辐射、动力学和磁物理。在本案例研究中，我们讨论了阿塔卡马大口径亚毫米望远镜（AtLAST）将在这一研究领域取得的重大突破，这是一种拟议的50米单碟亚毫米望远镜。AtLAST的新发现空间来自于其非凡的灵敏度，特别是对扩展的低表面亮度发射、非常大的2度视场和相应的高映射效率。本文主要关注四个主题，这些主题将特别受益于AtLAST：1）LMC和SMC，2）河外磁场，3）星际介质的物理和化学，以及4）恒星形成和星系演化。通过每次约1000-2000小时的调查，AtLAST可以以秒差距的分辨率提供整个LMC和SMC场的深部尘埃连续体图，约100个附近星系中致密和扩散ISM的磁场结构、气体密度、温度和成分的高分辨率图，以及附近宇宙中的首次大规模盲CO调查，为多达10^6个星系输送分子气体质量（比目前的样本多3个数量级）。通过这样的观测活动，AtLAST将对我们理解重子周期和各种环境中的恒星形成产生深远影响。 et.al.|[2403.01202](http://arxiv.org/abs/2403.01202)|null|
|**2024-03-02**|**Modelling ion acceleration and transport in corotating interaction regions: the mass-to-charge ratio dependence of the particle spectrum**|我们研究了垂直扩散在共旋相互作用区（CIRs）中形成高能离子光谱的作用，重点是其质量与电荷（ $A/Q$）的依赖性。我们使用EUropean Heliophere FORcasting Information Asset（EUHFORIA）模拟了合成CIR，并通过求解包含平行和垂直扩散的聚焦输运方程来对随后的离子加速和输运进行建模。我们的结果揭示了有和没有垂直扩散的情况下离子光谱的明显差异。在没有垂直扩散的情况下，CIRs附近的离子光谱显示出强烈的$（a/Q）^｛\epsilon｝$依赖性，其中$\epsilon$取决于湍流光谱指数，与理论预测一致。相反，垂直扩散的结合，其特征是弱的$a/Q$ 依赖性，导致不同离子种类的光谱相似。这在质量上与CIR中高能粒子的观测结果一致。 et.al.|[2403.01201](http://arxiv.org/abs/2403.01201)|null|

<p align=right>(<a href=#updated-on-20240305>back to top</a>)</p>

## NeRF

|Publish Date|Title|Abstract|PDF|Code|
|---|---|---|---|---|
|**2024-03-02**|**Neural Field Classifiers via Target Encoding and Classification Loss**|神经场方法在计算机视觉和计算机图形学中的各种长期任务中取得了巨大进展，包括新颖的视图合成和几何重建。由于现有的神经场方法试图预测一些基于坐标的连续目标值，例如神经辐射场（NeRF）的RGB，所有这些方法都是回归模型，并通过一些回归损失进行优化。然而，对于神经场方法来说，回归模型真的比分类模型更好吗？在这项工作中，我们试图从机器学习的角度来探讨神经领域这个非常基本但被忽视的问题。我们成功地提出了一种新的神经场分类器（NFC）框架，该框架将现有的神经场方法公式化为分类任务，而不是回归任务。所提出的NFC可以通过使用新的目标编码模块和优化分类损失，轻松地将任意神经场回归器（NFR）转换为其分类变体。通过将连续回归目标编码为高维离散编码，我们自然地形成了多标签分类任务。大量的实验证明了NFC在几乎免费的额外计算成本下令人印象深刻的有效性。此外，NFC还显示出对稀疏输入、损坏图像和动态场景的鲁棒性。 et.al.|[2403.01058](http://arxiv.org/abs/2403.01058)|null|
|**2024-02-28**|**NERV++: An Enhanced Implicit Neural Video Representation**|神经场，也称为隐式神经表示（INRs），在表示、生成和操作各种数据类型方面表现出了非凡的能力，允许在低内存占用下进行连续的数据重建。尽管应用于视频压缩的INRs很有前景，但仍需要大幅度提高其率失真性能，并且需要大量的参数和长时间的训练迭代来捕捉高频细节，限制了其更广泛的适用性。解决这个问题仍然是一项极具挑战性的任务，这将使INR在压缩任务中更容易访问。我们通过引入视频的神经表示NeRV++朝着解决这些缺点迈出了一步，NeRV++是一种增强的隐式神经视频表示，是对原始NeRV解码器架构的更直接但有效的增强，其特征是夹着上采样块（UB）的可分离conv2d残差块（SCRB），以及用于改进特征表示的双线性插值跳过层。NeRV++允许将视频直接表示为神经网络近似的函数，并显著增强了当前基于INR的视频编解码器之外的表示能力。我们在UVG、MCL-JVC和Bunny数据集上评估了我们的方法，在INRs的视频压缩方面取得了有竞争力的结果。这一成果缩小了与基于自动编码器的视频编码的差距，标志着基于INR的视频压缩研究迈出了重要一步。 et.al.|[2402.18305](http://arxiv.org/abs/2402.18305)|null|
|**2024-02-27**|**NIIRF: Neural IIR Filter Field for HRTF Upsampling and Personalization**|头部相关传递函数（HRTF）对于沉浸式音频是重要的，并且已经研究了它们的空间插值来对有限测量进行上采样。近年来，从声源方向映射到HRTF的神经场（NF）引起了人们的关注。现有的基于NF的方法侧重于从给定的声源方向估计HRTF的幅度，并将该幅度转换为有限脉冲响应（FIR）滤波器。我们提出了神经无限冲激响应滤波器场（NIIRF）方法来估计级联IIR滤波器的系数。IIR滤波器模拟HRTF的模态特性，因此与FIR滤波器相比，需要更少的系数来很好地近似它们。我们发现，我们的方法可以在多个数据集上匹配现有的基于NF的方法的性能，甚至在测量稀疏时优于它们。我们还探索了将NF个性化到受试者的方法，并通过实验发现低秩自适应是有效的。 et.al.|[2402.17907](http://arxiv.org/abs/2402.17907)|**[link](https://github.com/merlresearch/neural-iir-field)**|
|**2024-02-27**|**AlignMiF: Geometry-Aligned Multimodal Implicit Field for LiDAR-Camera Joint Synthesis**|神经隐式场已经成为新视图合成中事实上的标准。最近，有一些方法探索在一个领域内融合多个模态，旨在共享不同模态的隐含特征，以提高重建性能。然而，这些模态往往表现出错位行为：对一种模态（如激光雷达）进行优化可能会对另一种模态产生不利影响，如相机性能，反之亦然。在这项工作中，我们对激光雷达相机联合合成的多模式隐场进行了全面分析，揭示了潜在的问题在于不同传感器的错位。此外，我们还介绍了AlignMiF，这是一个几何对齐的多模式隐式场，具有两个拟议的模块：几何感知对齐（GAA）和共享几何初始化（SGI）。这些模块有效地调整了不同模态的粗略几何结构，显著增强了激光雷达和相机数据之间的融合过程。通过在各种数据集和场景中进行广泛的实验，我们证明了我们的方法在促进激光雷达和相机模态之间在统一的神经场中更好地交互方面的有效性。具体而言，我们提出的AlignMiF比最近的隐式融合方法（KITTI-360和Waymo数据集上的图像PSNR分别为+2.01和+3.11）实现了显著的改进，并始终超过单模态性能（在各自的数据集上，激光雷达切角距离分别减少了13.8%和14.2%）。 et.al.|[2402.17483](http://arxiv.org/abs/2402.17483)|**[link](https://github.com/tangtaogo/alignmif)**|
|**2024-02-26**|**GEM3D: GEnerative Medial Abstractions for 3D Shape Synthesis**|我们介绍了GEM3D——一种新的深度、拓扑感知的三维形状生成模型。我们的方法的关键成分是基于神经骨架的表示，对形状拓扑和几何信息进行编码。通过去噪扩散概率模型，我们的方法首先根据中轴变换（MAT）生成基于骨架的表示，然后通过骨架驱动的神经隐式公式生成曲面。神经隐式考虑了存储在生成的骨架表示中的拓扑和几何信息，以产生与以前的神经场公式相比在拓扑和几何上更准确的曲面。我们讨论了我们的方法在形状合成和点云重建任务中的应用，并对我们的方法进行了定性和定量评估。与最先进的技术相比，我们展示了更忠实的表面重建和多样化的形状生成结果，还涉及从Thingi10K和ShapeNet重建和合成结构复杂的高属形表面的挑战性场景。 et.al.|[2402.16994](http://arxiv.org/abs/2402.16994)|null|
|**2024-02-21**|**Geometry-Informed Neural Networks**|我们引入了几何知情神经网络（GINN）的概念，它包括（i）在几何约束下的学习，（ii）作为适当表示的神经场，以及（iii）为几何任务中经常遇到的不确定系统生成不同的解决方案。值得注意的是，GINN公式不需要训练数据，因此可以被视为纯粹由约束驱动的生成建模。我们添加了一个明确的多样性损失来缓解模式崩溃。我们考虑了几个约束，特别是分量的连通性，我们通过Morse理论将其转化为可微损失。在实验上，我们展示了GINN学习范式在一系列二维和三维场景中的有效性，这些场景的复杂性不断增加。 et.al.|[2402.14009](http://arxiv.org/abs/2402.14009)|null|
|**2024-02-18**|**Pattern Recognition Facilities of Extended Kalman Filtering in Stochastic Neural Fields**|在数学神经科学中，人们特别关注在存在模型不确定性的情况下，由动态神经场（DNF）建模的神经组织中的工作记忆机制。工作记忆设施意味着，由于网络中反复的相互作用，在去除外部刺激后，神经元的活动保持自我维持，并允许系统处理丢失的传感器信息。在我们之前的工作中，我们已经根据传感器提供的不完整数据开发了两种神经膜电位的重建方法。这些方法是在扩展卡尔曼滤波方法中通过使用Euler Maruyama方法和\^{o}-Taylor订单1.5的扩展。它表明\^{o}-Taylor基于EKF的恢复过程比基于Euler Maruyama的替代方案更准确。在传感器信息不完整的情况下，它提高了膜电位重建的质量。本文的目的是研究它们的模式识别功能，即在模型不确定和信息不完整的情况下，模式形成重建的质量。数值实验是以神经组织中出现多个活动区的随机DNF为例提供的。 et.al.|[2402.11551](http://arxiv.org/abs/2402.11551)|null|
|**2024-02-15**|**Reg-NF: Efficient Registration of Implicit Surfaces within Neural Fields**|神经场，即基于坐标的神经网络，最近因隐含地表示场景而广受欢迎。与基于点云等显式表示的经典方法相比，神经场提供了连续的场景表示，能够以紧凑且理想的机器人应用方式表示3D几何结构和外观。然而，有限的现有方法已经研究了通过直接利用这些连续的隐式表示来配准多个神经场。在本文中，我们提出了Reg-NF，这是一种基于神经场的配准，它优化了两个任意神经场之间的相对6-DoF变换，即使这两个场具有不同的比例因子。Reg NF的关键组成部分包括双向配准损失、多视图表面采样和体积符号距离函数（SDF）的利用。我们在一个新的神经场数据集上展示了我们的方法，用于评估配准问题。我们提供了一组详尽的实验和消融研究，以确定我们的方法的性能，同时也讨论了局限性，为研究界在无约束环境中利用神经场的开放挑战提供了未来的方向。 et.al.|[2402.09722](http://arxiv.org/abs/2402.09722)|null|
|**2024-02-12**|**Unsupervised Discovery of Object-Centric Neural Fields**|我们研究从单个图像中推断3D以对象为中心的场景表示。虽然最近的方法在从简单的合成图像中无监督地发现3D对象方面显示出了潜力，但它们未能推广到具有视觉丰富和多样化对象的真实世界场景。这种限制源于它们的对象表示，它将对象的内在属性（如形状和外观）与外在的、以观察者为中心的属性（如3D位置）纠缠在一起。为了解决这一瓶颈，我们提出了以对象为中心的神经场的无监督发现（uOCF）。uOCF专注于学习对象的内在，并分别对外在进行建模。我们的方法显著提高了系统泛化能力，从而能够从稀疏的真实世界图像中无监督地学习高保真的以对象为中心的场景表示。为了评估我们的方法，我们收集了三个新的数据集，包括两个真实的厨房环境。大量实验表明，uOCF能够在无监督的情况下从单个真实图像中发现视觉丰富的对象，从而实现3D对象分割和场景操作等应用。值得注意的是，uOCF演示了对单个真实图像中看不见的物体的零样本泛化。项目页面：https://red-fairy.github.io/uOCF/ et.al.|[2402.07376](http://arxiv.org/abs/2402.07376)|null|
|**2024-02-06**|**Improved Generalization of Weight Space Networks via Augmentations**|在深度权重空间（DWS）中学习，神经网络处理其他神经网络的权重，是一个新兴的研究方向，应用于2D和3D神经领域（INRs、NeRFs），以及对其他类型的神经网络进行推断。不幸的是，权重空间模型往往存在严重的过拟合问题。我们实证分析了这种过拟合的原因，发现一个关键原因是DWS数据集缺乏多样性。虽然给定的对象可以用许多不同的权重配置来表示，但典型的INR训练集无法捕捉表示同一对象的INR之间的可变性。为了解决这一问题，我们探索了在权重空间中增加数据的策略，并提出了一种适用于权重空间的MixUp方法。我们在两个设置中展示了这些方法的有效性。在分类方面，它们可以提高性能，类似于拥有10倍以上的数据。在自我监督的对比学习中，它们在下游分类中产生了5-10%的显著收益。 et.al.|[2402.04081](http://arxiv.org/abs/2402.04081)|null|

<p align=right>(<a href=#updated-on-20240305>back to top</a>)</p>

[contributors-shield]: https://img.shields.io/github/contributors/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[contributors-url]: https://github.com/Vincentqyw/cv-arxiv-daily/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[forks-url]: https://github.com/Vincentqyw/cv-arxiv-daily/network/members
[stars-shield]: https://img.shields.io/github/stars/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[stars-url]: https://github.com/Vincentqyw/cv-arxiv-daily/stargazers
[issues-shield]: https://img.shields.io/github/issues/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[issues-url]: https://github.com/Vincentqyw/cv-arxiv-daily/issues

