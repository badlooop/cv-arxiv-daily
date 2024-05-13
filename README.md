[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]

## Updated on 2024.05.13
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
|**2024-05-09**|**FastScene: Text-Driven Fast 3D Indoor Scene Generation via Panoramic Gaussian Splatting**|文本驱动的3D室内场景生成具有广泛的应用，从游戏和智能家居到AR/VR应用。快速高保真的场景生成对于确保用户友好的体验至关重要。然而，现有方法的特点是生成过程漫长，或者需要复杂的手动指定运动参数，这给用户带来了不便。此外，这些方法通常依赖于窄场视点迭代生成，从而影响全局一致性和整体场景质量。为了解决这些问题，我们提出了FastScene，这是一个用于快速、更高质量的3D场景生成的框架，同时保持场景一致性。具体来说，在给定文本提示的情况下，我们生成全景图并估计其深度，因为全景图包含了关于整个场景的信息，并表现出明确的几何约束。为了获得高质量的新颖视图，我们引入了粗略视图合成（CVS）和渐进新颖视图修复（PNVI）策略，以确保场景一致性和视图质量。随后，我们利用多视图投影（MVP）形成透视图，并应用3D高斯散射（3DGS）进行场景重建。综合实验表明，FastScene在生成速度和质量上都优于其他方法，具有更好的场景一致性。值得注意的是，FastScene仅在文本提示的引导下，就可以在15分钟内生成3D场景，这比最先进的方法快至少一个小时，使其成为用户友好的场景生成典范。 et.al.|[2405.05768](http://arxiv.org/abs/2405.05768)|null|
|**2024-05-09**|**RPBG: Towards Robust Neural Point-based Graphics in the Wild**|基于点的表示最近在新颖的视图合成中流行起来，因为它们具有直观的几何表示、简单的操作和更快的收敛等独特优势。然而，根据我们的观察，这些基于点的神经重渲染方法预计只能在理想条件下表现良好，并且会遇到噪声、斑点点和无边界场景，这些问题很难处理，但在实际应用中很常见。为此，我们重新审视了一种有影响力的方法，称为基于神经点的图形（NPBG），作为我们的基线，并提出了稳健的基于点图形（RPBG）。我们深入分析了阻碍NPBG在通用数据集上实现令人满意的渲染的因素，并相应地改革了管道，使其对野外不同的数据集更具鲁棒性。受图像恢复实践的启发，我们极大地增强了神经渲染器，以实现基于注意力的点可见性校正和不完全光栅化的修复，只需可接受的开销。我们还寻求一种简单而轻量级的环境建模替代方案和一种迭代方法来缓解较差的几何形状问题。通过对具有不同拍摄条件和相机轨迹的广泛数据集进行彻底评估，RPBG稳定地以很大的优势优于基线，并表现出其相对于最先进的基于NeRF的变体的强大鲁棒性。代码可在https://github.com/QT-Zhu/RPBG. et.al.|[2405.05663](http://arxiv.org/abs/2405.05663)|null|
|**2024-05-08**|**GDGS: Gradient Domain Gaussian Splatting for Sparse Representation of Radiance Fields**|3D高斯飞溅方法越来越流行。然而，它们直接作用于信号，导致信号的密集表示。即使使用一些技术，如修剪或蒸馏，结果仍然很密集。在本文中，我们建议对原始信号的梯度进行建模。梯度比原始信号稀疏得多。因此，梯度使用更少的高斯飞溅，从而在训练和渲染过程中获得更高效的存储，从而获得更高的计算性能。由于稀疏性，在视图合成过程中，只需要少量像素，从而获得高得多的计算性能（快 $100\sim 1000\times$ ）。并且可以通过求解具有线性计算复杂性的泊松方程来从梯度中恢复2D图像。进行了几个实验来验证梯度的稀疏性和所提出方法的计算性能。该方法可以应用于各种应用，如人体建模和室内环境建模。 et.al.|[2405.05446](http://arxiv.org/abs/2405.05446)|null|
|**2024-05-07**|**Novel View Synthesis with Neural Radiance Fields for Industrial Robot Applications**|神经辐射场（NeRF）已成为一个快速发展的研究领域，有可能彻底改变典型的摄影测量工作流程，例如用于3D场景重建的工作流程。作为输入，NeRF需要具有相应相机姿态和内部方向的多视图图像。在典型的NeRF工作流程中，相机姿态和内部方向是通过运动结构（SfM）预先估计的。但是，生成的新视图的质量很难预测，这取决于不同的参数，如可用图像的数量和分布，以及相关相机姿态和内部方向的准确性。此外，SfM是一个耗时的预处理步骤，其质量在很大程度上取决于图像内容。此外，SfM的未定义的缩放因子阻碍了需要度量信息的后续步骤。在本文中，我们评估了NeRF在工业机器人应用中的潜力。我们提出了一种SfM预处理的替代方案：我们使用连接到工业机器人末端执行器的校准相机捕捉输入图像，并基于机器人运动学确定具有公制尺度的精确相机姿态。然后，我们通过将新观点与基本事实进行比较，并基于集成方法计算内部质量度量，来研究这些观点的质量。出于评估目的，我们获取了多个数据集，这些数据集对典型的工业应用的重建提出了挑战，如反射物体、较差的纹理和精细的结构。我们表明，基于机器人的姿态确定在非要求的情况下达到了与SfM相似的精度，同时在更具挑战性的场景中具有明显的优势。最后，我们给出了在缺乏基本事实的情况下应用集成方法来估计合成新视图的质量的第一个结果。 et.al.|[2405.04345](http://arxiv.org/abs/2405.04345)|null|
|**2024-05-06**|**A Construct-Optimize Approach to Sparse View Synthesis without Camera Pose**|从稀疏的输入图像集进行新的视图合成是一个具有挑战性的问题，具有很大的实际意义，尤其是当相机姿态不存在或不准确时。由于姿态和深度之间的耦合以及单目深度估计的不精确性，在神经辐射场算法中直接优化相机姿态和使用估计的深度通常不会产生好的结果。在本文中，我们利用最近的3D高斯飞溅方法，开发了一种新的无相机姿态稀疏视图合成的构造和优化方法。具体来说，我们通过使用单目深度并将像素投影回3D世界来逐步构建解决方案。在构建过程中，我们通过检测训练视图和相应渲染图像之间的2D对应关系来优化解决方案。我们开发了一个统一的可微分管道，用于相机配准和调整相机姿势和深度，然后进行反向投影。我们还引入了高斯飞溅中预期表面的新概念，这对我们的优化至关重要。这些步骤实现了粗略的解决方案，然后可以使用标准优化方法对其进行低通滤波和细化。我们展示了坦克、寺庙和静态远足数据集的结果，只有三个宽间距的视图，显示出比竞争方法（包括具有近似相机姿态信息的方法）明显更好的质量。此外，即使使用一半的数据集，我们的结果也会随着更多的视图而改进，并优于以前的InstantNGP和Gaussian Splatting算法。 et.al.|[2405.03659](http://arxiv.org/abs/2405.03659)|null|
|**2024-05-06**|**Gaussian Splatting: 3D Reconstruction and Novel View Synthesis, a Review**|基于图像的3D重建是一项具有挑战性的任务，涉及从一组输入图像推断对象或场景的3D形状。基于学习的方法因其直接估计3D形状的能力而受到关注。这篇综述论文的重点是最先进的3D重建技术，包括生成新颖的、看不见的视图。概述了高斯飞溅方法的最新发展，包括输入类型、模型结构、输出表示和训练策略。还讨论了尚未解决的挑战和未来的方向。鉴于该领域的快速进展以及增强3D重建方法的众多机会，对算法进行全面检查似乎至关重要。因此，本研究对高斯散射的最新进展进行了全面的概述。 et.al.|[2405.03417](http://arxiv.org/abs/2405.03417)|null|
|**2024-05-04**|**LidaRF: Delving into Lidar for Neural Radiance Field on Street Scenes**|逼真度模拟在自动驾驶等应用中发挥着至关重要的作用，神经辐射场（NeRF）的进步可以通过自动创建数字3D资产实现更好的可扩展性。然而，由于在较高速度下相机运动基本共线和采样稀疏，街道场景的重建质量受到影响。另一方面，应用程序通常要求从偏离输入的摄影机视图进行渲染，以准确模拟车道变更等行为。在本文中，我们提出了一些见解，可以更好地利用激光雷达数据来提高街景的NeRF质量。首先，我们的框架从激光雷达中学习几何场景表示，该表示与基于隐式网格的表示融合用于辐射解码，从而提供由显式点云提供的更强的几何信息。其次，我们提出了一种鲁棒的遮挡感知深度监督方案，该方案允许通过累积来利用密集的激光雷达点。第三，我们从激光雷达点生成增强训练视图，以便进一步改进。我们的见解转化为在真实驾驶场景下大大改进的新颖视图合成。 et.al.|[2405.00900](http://arxiv.org/abs/2405.00900)|null|
|**2024-05-09**|**RTG-SLAM: Real-time 3D Reconstruction at Scale using Gaussian Splatting**|我们提出了实时高斯SLAM（RTG-SLAM），这是一个使用RGBD相机的实时三维重建系统，用于使用高斯飞溅的大规模环境。该系统具有紧凑的高斯表示和高效的动态高斯优化方案。我们强制每个高斯要么不透明，要么几乎透明，不透明的适合表面和主色，透明的适合残余色。通过以不同于彩色渲染的方式渲染深度，我们让单个不透明高斯很好地拟合局部表面区域，而不需要多个重叠的高斯，从而大大降低了内存和计算成本。对于动态高斯优化，我们明确地为每帧三种类型的像素添加高斯：新观察到的、具有大颜色误差的和具有大深度误差的。我们还将所有高斯分为稳定高斯和不稳定高斯，其中稳定高斯有望很好地拟合先前观察到的RGBD图像，否则不稳定。我们只优化不稳定的高斯，只渲染不稳定高斯占用的像素。这样，要优化的高斯数和要渲染的像素都大大减少，并且可以实时进行优化。我们展示了各种大型场景的实时重建。与最先进的基于NeRF的RGBD SLAM相比，我们的系统实现了相当高质量的重建，但速度约为其两倍，内存成本约为其一半，并在新视图合成的真实性和相机跟踪精度方面表现出卓越的性能。 et.al.|[2404.19706](http://arxiv.org/abs/2404.19706)|null|
|**2024-04-29**|**SAGS: Structure-Aware 3D Gaussian Splatting**|随着NeRFs的出现，3D高斯散射（3D-GS）为实时神经渲染铺平了道路，克服了体积方法的计算负担。继3D-GS的开创性工作之后，有几种方法试图实现可压缩和高保真度性能的替代方案。然而，通过采用几何不可知的优化方案，这些方法忽略了场景的固有3D结构，从而限制了表示的表现力和质量，导致了各种浮点和伪影。在这项工作中，我们提出了一种结构感知的高斯飞溅方法（SAGS），该方法隐式地对场景的几何结构进行编码，这反映了最先进的渲染性能，并降低了基准新视图合成数据集的存储要求。SAGS建立在局部全局图表示的基础上，有助于复杂场景的学习，并强制执行有意义的点位移，以保持场景的几何结构。此外，我们还介绍了一种轻量级的SAGS，使用了一种简单而有效的中点插值方案，该方案展示了场景的紧凑表示，在不依赖任何压缩策略的情况下，大小减少了24 $\times$ 。在多个基准数据集上进行的大量实验表明，在渲染质量和模型大小方面，与最先进的3D-GS方法相比，SAGS具有优越性。此外，我们证明了我们的结构感知方法可以有效地减轻先前方法的浮动伪影和不规则失真，同时获得精确的深度图。项目页面https://eververas.github.io/SAGS/. et.al.|[2404.19149](http://arxiv.org/abs/2404.19149)|null|
|**2024-04-29**|**Simple-RF: Regularizing Sparse Input Radiance Fields with Simpler Solutions**|神经辐射场（NeRF）在场景的照片逼真的自由视图渲染中表现出令人印象深刻的性能。最近对NeRF的改进，如TensoRF和ZipNeRF，与使用隐式表示的NeRF相比，使用显式模型进行更快的优化和渲染。然而，隐式和显式辐射场都需要对给定场景中的图像进行密集采样。当只有一组稀疏的视图可用时，它们的性能会显著下降。研究人员发现，监督辐射场估计的深度有助于以更少的视角有效训练辐射场。深度监督是使用经典方法或在大型数据集上预先训练的神经网络来获得的。前者可能只提供稀疏的监督，而后者可能存在泛化问题。与早期的方法不同，我们试图通过设计增强模型并将其与主辐射场一起训练来学习深度监督。此外，我们的目标是设计一个正则化框架，该框架可以在不同的隐式和显式辐射场中工作。我们观察到，在稀疏输入场景中，这些辐射场模型的某些特征与观察到的图像过度拟合。我们的关键发现是，降低辐射场在位置编码、分解张量分量的数量或哈希表的大小方面的能力，限制了模型学习更简单的解决方案，从而在某些区域估计更好的深度。通过设计基于这种降低的能力的增强模型，我们可以更好地对主辐射场进行深度监督。通过采用上述正则化，我们在包含前向和360 $^\circ$ 场景的流行数据集上使用稀疏输入视图实现了最先进的视图合成性能。 et.al.|[2404.19015](http://arxiv.org/abs/2404.19015)|null|

<p align=right>(<a href=#updated-on-20240513>back to top</a>)</p>

## 3D Reconstruction

|Publish Date|Title|Abstract|PDF|Code|
|---|---|---|---|---|
|**2024-05-09**|**Minimal Perspective Autocalibration**|我们从多个角度引入了一个新的最小问题族进行重构。我们的主要关注点是一种新的自动校准方法，这是计算机视觉中一个长期存在的问题。解决这个问题的传统方法，如基于Kruppa方程或模约束的方法，明确地依赖于多个基本矩阵或投影重建的知识。相反，我们考虑了一种新的公式，该公式涉及图像点的约束、3D点的未知深度和部分指定的校准矩阵 $K$。对于$2$和$3$视图，我们给出了通过放松其中一些约束而获得的最小自动校准问题的综合分类法。这些问题根据视图的数量和$K$ 的任何假定先验知识被组织成类。在每个类中，我们用最少的——或者相对较少的——解决方案来确定问题。从这一大堆问题中，我们设计了三个实用的解决方案。使用合成数据和真实数据进行的实验以及我们的求解器与COLMAP的接口证明，与最先进的校准方法相比，我们实现了卓越的精度。代码位于https://github.com/andreadalcin/MinimalPerspectiveAutocalibration et.al.|[2405.05605](http://arxiv.org/abs/2405.05605)|null|
|**2024-05-09**|**Benchmarking Neural Radiance Fields for Autonomous Robots: An Overview**|神经辐射场（NeRF）已成为3D场景表示的一种强大范例，提供了一组稀疏和非结构化传感器数据的高保真渲染和重建。在自主机器人的背景下，对环境的感知和理解至关重要，NeRF在提高性能方面有着巨大的前景。在本文中，我们对利用NeRF增强自主机器人能力的最新技术进行了全面的调查和分析。我们特别关注自主机器人的感知、定位和导航以及决策模块，并深入研究对自主操作至关重要的任务，包括3D重建、分割、姿态估计、同步定位和映射（SLAM）、导航和规划以及交互。我们的调查仔细地对现有的基于NeRF的方法进行了基准测试，深入了解了它们的优势和局限性。此外，我们还探索了这一领域未来研究和开发的有希望的途径。值得注意的是，我们讨论了3D高斯飞溅（3DGS）、大型语言模型（LLM）和生成人工智能等先进技术的集成，以提高重建效率、场景理解和决策能力。这项调查为寻求利用NeRF为自主机器人赋能的研究人员提供了路线图，为能够在复杂环境中无缝导航和交互的创新解决方案铺平了道路。 et.al.|[2405.05526](http://arxiv.org/abs/2405.05526)|null|
|**2024-05-06**|**MVDiff: Scalable and Flexible Multi-View Diffusion for 3D Object Reconstruction from Single-View**|为3D重建任务生成一致的多个视图仍然是对现有图像到3D扩散模型的挑战。通常，将3D表示合并到扩散模型中会降低模型的速度以及可推广性和质量。本文提出了一个通用框架，从单个图像或利用场景表示变换器和视图条件扩散模型生成一致的多视图图像。在模型中，我们引入了极线几何约束和多视图注意力，以增强三维一致性。从一个图像输入中，我们的模型能够生成超过评估指标基线方法的3D网格，包括PSNR、SSIM和LPIPS。 et.al.|[2405.03894](http://arxiv.org/abs/2405.03894)|null|
|**2024-05-06**|**Gaussian Splatting: 3D Reconstruction and Novel View Synthesis, a Review**|基于图像的3D重建是一项具有挑战性的任务，涉及从一组输入图像推断对象或场景的3D形状。基于学习的方法因其直接估计3D形状的能力而受到关注。这篇综述论文的重点是最先进的3D重建技术，包括生成新颖的、看不见的视图。概述了高斯飞溅方法的最新发展，包括输入类型、模型结构、输出表示和训练策略。还讨论了尚未解决的挑战和未来的方向。鉴于该领域的快速进展以及增强3D重建方法的众多机会，对算法进行全面检查似乎至关重要。因此，本研究对高斯散射的最新进展进行了全面的概述。 et.al.|[2405.03417](http://arxiv.org/abs/2405.03417)|null|
|**2024-05-05**|**Morphokinematical study of the planetary nebula Me2-1: Unveiling its point-symmetric and unusual physical structure**|（摘要）我们展示了几条发射线的窄带图像，以及Me2-1的高分辨率和中分辨率长缝光谱，以研究其形态和3D结构、物理参数和化学丰度。我们在Me2-1中发现：一个椭圆环；两个细长的弯曲结构（帽），其包含三对亮点对称（PS）结；所述环的壳内部；以及微弱的光晕或附着的外壳。在所有图像中都观察到了帽，PS结仅在低激发发射线图像中观察到。这些结构也在高分辨率的长狭缝光谱中被识别。3D重建显示，Me2-1由一个几乎是极点的环和一个几乎球形的外壳组成，盖子和PS结连接在外壳上。帽状物和PS结最有可能追踪沿着摆动轴喷出的高速准直双极外流与球壳碰撞、减速并保持附着的位置。尽管Me2-1中的主要激发机制被发现是光电离，但PS结中的冲击的贡献是由它们的发射线比提出的。在行星状星云中，准直外流和带有球形外壳的环的结合是不寻常的。我们推测，如果两颗行星都在祖先的渐近巨星分支阶段进入共同的包络演化，那么这两颗行星可能都参与了Me2-1的形成，每颗行星的质量都小于一个木星。一颗行星被潮汐破坏，在中心恒星周围形成吸积盘，准直的双极性外流从吸积盘喷出；另一颗行星幸存下来，导致吸积盘摆动。导出的物理参数和化学丰度与之前的分析中获得的相似，丰度也指向Me2-1的低质量祖先。 et.al.|[2405.02938](http://arxiv.org/abs/2405.02938)|null|
|**2024-05-05**|**MVIP-NeRF: Multi-view 3D Inpainting on NeRF Scenes via Diffusion Prior**|尽管出现了基于显式RGB和深度2D修复监督的成功NeRF修复方法，但这些方法固有地受到其底层2D修复器能力的约束。这是由于两个关键原因：（i）独立修复组成图像会导致视图不一致的图像，以及（ii）2D修复器难以确保高质量的几何图形完成和与修复的RGB图像对齐。为了克服这些限制，我们提出了一种称为MVIP NeRF的新方法，该方法利用扩散先验的潜力进行NeRF修复，同时解决外观和几何方面的问题。MVIP NeRF跨多个视图执行联合修复，以达到一致的解决方案，这是通过基于分数蒸馏采样（SDS）的迭代优化过程实现的。除了恢复渲染的RGB图像外，我们还提取法线贴图作为几何表示，并定义法线SDS损失，以促进精确的几何修复和与外观对齐。此外，我们制定了一个多视图SDS评分函数，以从不同的视图图像中同时提取生成先验，确保在处理大的视图变化时一致的视觉完成。我们的实验结果显示出比以前的NeRF修复方法更好的外观和几何恢复。 et.al.|[2405.02859](http://arxiv.org/abs/2405.02859)|null|
|**2024-05-04**|**Beyond Unimodal Learning: The Importance of Integrating Multiple Modalities for Lifelong Learning**|当人类擅长持续学习时，深度神经网络表现出灾难性的遗忘。大脑允许有效CL的一个显著特征是，它利用多种模式进行学习和推理，而这在DNN中尚未得到充分探索。因此，我们研究了多种模式在减轻遗忘中的作用和相互作用，并为多模式持续学习引入了一个基准。我们的研究结果表明，利用来自多种模态的多个视图和互补信息，使模型能够学习更准确、更稳健的表示。这使得模型不那么容易受到模态特定规律的影响，并大大减少了遗忘。此外，我们观察到，个体模态对分布变化表现出不同程度的鲁棒性。最后，我们提出了一种方法，通过利用每个模态中数据点之间的关系结构相似性来集成和对齐来自不同模态的信息。我们的方法设置了一个强大的基线，可以实现单模式和多模式推理。我们的研究为进一步探索多种模式在实现CL中的作用提供了一个有希望的案例，并为未来的研究提供了标准基准。 et.al.|[2405.02766](http://arxiv.org/abs/2405.02766)|**[link](https://github.com/NeurAI-Lab/MultiModal-CL)**|
|**2024-05-04**|**ActiveNeuS: Active 3D Reconstruction using Neural Implicit Surface Uncertainty**|3D场景重建中的主动学习已经得到了广泛的研究，因为选择信息丰富的训练视图对重建至关重要。最近，神经辐射场（NeRF）变体在使用图像渲染或几何不确定性的主动3D重建中显示出性能提高。然而，在选择信息视图时同时考虑这两种不确定性仍然没有得到探索，而利用不同类型的不确定性可以减少在输入稀疏的早期训练阶段出现的偏差。在本文中，我们提出了ActiveNeuS，它在考虑两种不确定性的情况下评估候选视图。ActiveNeuS提供了一种积累图像渲染不确定性的方法，同时避免了估计密度可能引入的偏差。ActiveNeuS计算神经隐含的表面不确定性，提供颜色不确定性和表面信息。它通过使用表面信息和网格来有效地处理偏差，从而能够快速选择不同的视点。我们的方法优于以前在流行数据集Blender和DTU上的工作，表明ActiveNeuS选择的视图显著提高了性能。 et.al.|[2405.02568](http://arxiv.org/abs/2405.02568)|null|
|**2024-05-03**|**CVTGAD: Simplified Transformer with Cross-View Attention for Unsupervised Graph-level Anomaly Detection**|无监督图级异常检测（UGAD）在化学分析和生物信息学等关键学科中取得了显著的成绩。现有的UGAD范式通常采用数据扩充技术来构建多个视图，然后采用不同的策略从不同的视图中获得表示，以共同进行UGAD。然而，以前的大多数工作只从有限的感受野中考虑节点/图之间的关系，导致一些关键的结构模式和特征信息被忽视。此外，现有的大多数方法以并行的方式分别考虑不同的视图，无法直接探索不同视图之间的相互关系。因此，需要一种具有更大感受野的方法，可以直接探索不同观点之间的相互关系。在本文中，我们提出了一种新的用于无监督图级异常检测的具有交叉视图注意的简化变换器，即CVTGAD。为了增加感受野，我们构建了一个简化的基于转换器的模块，从图内和图间的角度利用节点/图之间的关系。此外，我们设计了一种跨视图注意力机制，直接利用不同视图之间的视图共生，在节点级和图级弥合视图间的差距。据我们所知，这是首次将transformer和cross-attention应用于UGAD，实现了图神经网络和transformer的协同工作。在3个领域的15个真实世界数据集上进行的大量实验证明了CVTGAD在UGAD任务上的优越性。代码位于\url{https://github.com/jindongli-Ai/CVTGAD}. et.al.|[2405.02359](http://arxiv.org/abs/2405.02359)|**[link](https://github.com/jindongli-ai/cvtgad)**|
|**2024-05-04**|**HandSSCA: 3D Hand Mesh Reconstruction with State Space Channel Attention from RGB images**|从单个RGB图像重建手网格是一项具有挑战性的任务，因为手经常被物体遮挡。以前的大多数工作都试图引入更多的附加信息并采用注意力机制来改善3D重建结果，但这会增加计算复杂性。这一观察结果促使我们提出一种新的简洁架构，同时提高计算效率。在这项工作中，我们提出了一种简单有效的三维手部网格重建网络HandSSCA，它是第一个将状态空间建模纳入手部姿态估计领域的网络。在网络中，我们设计了一个新的状态空间通道注意力模块，该模块扩展了有效的感觉场，提取了空间维度上的手部特征，并增强了通道维度上的手部区域特征。这种设计有助于重建完整而详细的手部网格。在具有挑战性手对象遮挡的知名数据集（如FREIHAND、DEXYCB和HO3D）上进行的大量实验表明，我们提出的HandSSCA在保持最小参数计数的同时实现了最先进的性能。 et.al.|[2405.01066](http://arxiv.org/abs/2405.01066)|null|

<p align=right>(<a href=#updated-on-20240513>back to top</a>)</p>

## Diffusion

|Publish Date|Title|Abstract|PDF|Code|
|---|---|---|---|---|
|**2024-05-09**|**Distilling Diffusion Models into Conditional GANs**|我们提出了一种将复杂的多步扩散模型提取为单步条件GAN学生模型的方法，极大地加速了推理，同时保持了图像质量。我们的方法将扩散蒸馏解释为一个成对的图像到图像转换任务，使用扩散模型的ODE轨迹的噪声到图像对。为了进行有效的回归损失计算，我们提出了E-LatentLIPS，这是一种直接在扩散模型的潜在空间中操作的感知损失，利用增强集合。此外，我们采用扩散模型来构建具有文本对齐损失的多尺度鉴别器，以构建有效的基于条件GAN的公式。E-LatentLIPS比许多现有的蒸馏方法更有效地收敛，甚至考虑到数据集的构建成本。我们证明，我们的一步发生器在零样本COCO基准上优于先进的一步扩散蒸馏模型DMD、SDXL-Turbo和SDXL-Lightning。 et.al.|[2405.05967](http://arxiv.org/abs/2405.05967)|null|
|**2024-05-09**|**Towards comprehensive coverage of chemical space: Quantum mechanical properties of 836k constitutional and conformational closed shell neutral isomers consisting of HCNOFSiPSClBr**|Vector-QM24（VQM24）数据集试图在最先进的理论水平上更全面地涵盖所有可能的中性闭壳小有机和无机分子及其构象异构体。我们使用密度泛函理论（ $\omega$B97X-D3/cc-pVDZ）来优化577k个构象异构体，对应于258k个组成异构体。包括的异构体包含最多五个重原子（非氢），由$p$ -嵌段元素C、N、O、F、Si、p、S、Cl、Br组成。单点扩散量子蒙特卡罗(DMC@PBE0（ccECP/cc-pVQZ））的能量。该数据集是通过考虑所有组合可能的化学计量和图（根据SURGE包中实现的Lewis规则），以及GFN2-xTB确定的所有稳定构象而系统生成的。除了图形、几何结构、旋转常数和振动正模之外，VQM24还包括内部、原子化、电子-电子排斥、交换相关、色散、振动频率、吉布斯自由度、焓、ZPV、分子轨道能量；以及熵和热容。电子性质包括多极矩（偶极、四极、八极、六极）、原子核处的静电势（炼金术势）、穆利肯电荷和分子波函数。VQM24代表了一个高度准确和无偏的分子数据集，非常适合测试和训练真实量子系统的可转移、可扩展和生成ML模型。 et.al.|[2405.05961](http://arxiv.org/abs/2405.05961)|null|
|**2024-05-09**|**Self-Supervised Learning of Time Series Representation via Diffusion Process and Imputation-Interpolation-Forecasting Mask**|时间序列表示学习（TSRL）专注于为各种时间序列（TS）建模任务生成信息表示。TSRL中的传统自监督学习（SSL）方法分为四大类：重建、对抗、对比和预测，每种方法都面临着对噪声和复杂数据细微差别敏感的共同挑战。最近，基于扩散的方法已经显示出先进的生成能力。然而，它们主要针对插补和预测等特定应用场景，在利用一般TSRL的扩散模型方面留下了差距。我们的工作，时间序列扩散嵌入（TSDE），作为第一种基于扩散的SSL TSRL方法，弥补了这一差距。TSDE使用脉冲插值预测（IIF）掩模将TS数据分割为观测部分和掩蔽部分。它将可训练嵌入函数应用于观察到的部分，该函数具有带有交叉机制的双正交Transformer编码器。我们训练了一个以嵌入为条件的反向扩散过程，旨在预测添加到掩蔽部分的噪声。大量实验证明了TSDE在插补、插值、预测、异常检测、分类和聚类方面的优越性。我们还进行了消融研究，展示了嵌入可视化，并比较了推理速度，进一步证明了TSDE在TS数据学习表示方面的效率和有效性。 et.al.|[2405.05959](http://arxiv.org/abs/2405.05959)|**[link](https://github.com/eqtpartners/tsde)**|
|**2024-05-09**|**Frame Interpolation with Consecutive Brownian Bridge Diffusion**|最近在视频帧插值（VFI）方面的工作试图将VFI公式化为一个基于扩散的条件图像生成问题，合成给定随机噪声的中间帧和相邻帧。由于视频的分辨率相对较高，潜在扩散模型（LDM）被用作条件生成模型，其中自动编码器将图像压缩为潜在表示以进行扩散，然后从这些潜在表示重建图像。这样的公式提出了一个关键的挑战：VFI期望输出在确定性上等于基本事实中间帧，但当模型运行多次时，LDM随机生成一组不同的图像。多样化生成的原因是LDM中生成的潜在表示的累积方差（在生成的每一步累积的方差）很大。这使得采样轨迹是随机的，从而导致多样化而非确定性生成。为了解决这个问题，我们提出了我们独特的解决方案：连续布朗桥扩散的帧插值。具体而言，我们提出了连续的布朗桥扩散，该扩散以确定性初始值作为输入，从而产生更小的潜在表示的累积方差。我们的实验表明，我们的方法可以随着自动编码器的改进而改进，并在VFI中实现最先进的性能，为进一步增强留下了强大的潜力。 et.al.|[2405.05953](http://arxiv.org/abs/2405.05953)|null|
|**2024-05-09**|**Lumina-T2X: Transforming Text into Any Modality, Resolution, and Duration via Flow-based Large Diffusion Transformers**|Sora展示了缩放Diffusion Transformer以生成任意分辨率、纵横比和持续时间的照片级真实感图像和视频的潜力，但它仍然缺乏足够的实现细节。在本技术报告中，我们介绍了Lumina-T2X系列，这是一系列基于流量的大型扩散变压器（Flag DiT），配备了零初始化注意力，作为一个统一的框架，旨在将噪声转换为基于文本指令的图像、视频、多视图3D对象和音频片段。通过标记潜在的时空空间，并结合可学习的占位符，如[nextline]和[nextframe]标记，Lumina-T2X无缝地统一了不同时空分辨率下不同模态的表示。这种统一的方法能够在单个框架内对不同的模态进行训练，并允许在推理过程中灵活生成任何分辨率、纵横比和长度的多模态数据。RoPE、RMSNorm和流匹配等先进技术增强了Flag DiT的稳定性、灵活性和可扩展性，使Lumina-T2X的模型能够扩展到70亿个参数，并将上下文窗口扩展到128K个令牌。这对于使用我们的Lumina-T2I型号创建超高清图像和使用Lumina-V2V型号创建720p长视频特别有益。值得注意的是，Lumina-T2I由50亿个参数的Flag DiT提供动力，只需要6亿个参数初始DiT的训练计算成本的35%。我们进一步的全面分析强调了Lumina-T2X在分辨率外推、高分辨率编辑、生成一致的3D视图以及无缝转换合成视频方面的初步能力。我们预计，Lumina-T2X的开源将进一步促进生成型人工智能社区的创造力、透明度和多样性。 et.al.|[2405.05945](http://arxiv.org/abs/2405.05945)|**[link](https://github.com/alpha-vllm/lumina-t2x)**|
|**2024-05-09**|**Composable Part-Based Manipulation**|在本文中，我们提出了可组合的基于零件的操纵（CPM），这是一种利用对象-零件分解和零件-零件对应关系来提高机器人操纵技能的学习和泛化能力的新方法。通过考虑对象部分之间的功能对应关系，我们将功能动作（如倾倒和约束放置）概念化为不同对应约束的组合。CPM包括可组合扩散模型的集合，其中每个模型捕获不同的对象间对应关系。这些扩散模型可以基于特定的对象部分生成用于操纵技能的参数。利用基于零件的对应关系，再加上将任务分解为不同的约束，可以对新的对象和对象类别进行强大的泛化。我们在模拟和真实世界的场景中验证了我们的方法，证明了其在实现稳健和通用操作能力方面的有效性。 et.al.|[2405.05876](http://arxiv.org/abs/2405.05876)|null|
|**2024-05-09**|**Parameter identification for an uncertain reaction-diffusion equation via setpoint regulation**|讨论了由反应扩散偏微分方程控制的系统的反应系数的估计问题。提出了一种仅依赖于边界测量的估计器。该估计器基于设定点调节策略，并导致未知反应系数的渐近收敛估计。所提出的估计器与状态观测器相结合，可以提供实际系统状态的渐近估计。一个数值例子支持并说明了理论结果。 et.al.|[2405.05866](http://arxiv.org/abs/2405.05866)|null|
|**2024-05-09**|**Pre-trained Text-to-Image Diffusion Models Are Versatile Representation Learners for Control**|具体化的人工智能代理需要通过视觉和语言输入对物理世界进行精细的理解。这种能力很难仅从特定任务的数据中学习。这导致了预训练的视觉语言模型的出现，作为一种将从互联网规模的数据中学习到的表示转移到下游任务和新领域的工具。然而，通常使用的对比训练表示（如CLIP）已被证明无法使具体化的代理获得足够细粒度的场景理解——这对控制至关重要。为了解决这一缺点，我们考虑了来自预训练的文本到图像扩散模型的表示，该模型被明确优化以从文本提示生成图像，因此，它包含反映高度细粒度视觉空间信息的文本条件表示。使用预先训练的文本到图像扩散模型，我们构建了稳定的控制表示，允许学习推广到复杂开放环境的下游控制策略。我们表明，在广泛的模拟控制设置中，使用稳定控制表示学习的策略与最先进的表示学习方法具有竞争力，包括具有挑战性的操纵和导航任务。最值得注意的是，我们展示了稳定控制表示使学习策略能够在OVMM（一个困难的开放词汇导航基准）上表现出最先进的性能。 et.al.|[2405.05852](http://arxiv.org/abs/2405.05852)|**[link](https://github.com/ykarmesh/stable-control-representations)**|
|**2024-05-09**|**Could It Be Generated? Towards Practical Analysis of Memorization in Text-To-Image Diffusion Models**|在过去的几年里，扩散模型在文本引导的图像生成方面取得了长足的进步。然而，研究表明，文本到图像的扩散模型容易受到训练图像记忆的影响，这引发了人们对侵犯版权和侵犯隐私的担忧。在这项工作中，我们对文本到图像扩散模型中的记忆进行了实际分析。针对一组需要保护的图像，我们对其进行定量分析，而无需收集任何提示。具体来说，我们首先正式定义了图像的记忆，并确定了记忆的三个必要条件，分别是相似性、存在性和概率。然后，我们揭示了模型的预测误差与图像复制之间的相关性。基于相关性，我们建议利用反演技术来验证目标图像不被记忆的安全性，并测量它们被记忆的程度。模型开发人员可以利用我们的分析方法来发现记忆的图像，或者可靠地宣称对记忆的安全性。在流行的开源文本到图像扩散模型Stable Diffusion上进行的大量实验证明了我们分析方法的有效性。 et.al.|[2405.05846](http://arxiv.org/abs/2405.05846)|null|
|**2024-05-09**|**MSDiff: Multi-Scale Diffusion Model for Ultra-Sparse View CT Reconstruction**|计算机断层扫描（CT）技术通过稀疏采样减少了对人体的辐射危害，但较少的采样角度给图像重建带来了挑战。基于分数的生成模型广泛用于稀疏视图CT重建，其性能随着投影角度的急剧减小而显著降低。因此，我们提出了一种利用多尺度dif融合模型（MSDiff）的超稀疏视图CT重建方法，旨在关注信息的全局分布，促进具有局部图像特征的稀疏视图的重建。具体而言，所提出的模型巧妙地集成了来自综合采样和选择性稀疏采样技术的信息。通过对扩散模型的精确调整，它能够提取不同的噪声分布，加深对图像整体结构的理解，并帮助完全采样的模型更有效地恢复图像信息。通过利用项目数据中的固有相关性，我们设计了一个等距掩模，使模型能够更有效地集中注意力。实验结果表明，多尺度模型方法显著提高了超稀疏角度下的图像重建质量，在各种数据集上具有良好的泛化能力。 et.al.|[2405.05814](http://arxiv.org/abs/2405.05814)|null|

<p align=right>(<a href=#updated-on-20240513>back to top</a>)</p>

## NeRF

|Publish Date|Title|Abstract|PDF|Code|
|---|---|---|---|---|
|**2024-05-08**|**${M^2D}$NeRF: Multi-Modal Decomposition NeRF with 3D Feature Fields**|神经场（NeRF）已经成为表示连续3D场景的一种很有前途的方法。然而，NeRF中缺乏语义编码对场景分解提出了重大挑战。为了应对这一挑战，我们提出了一个单一的模型，即多模式分解NeRF（${M^2D}$ NeRF），它能够进行基于文本和基于视觉补丁的编辑。具体来说，我们使用多模态特征提取将来自预训练的视觉和语言模型的教师特征集成到3D语义特征体积中，从而促进一致的3D编辑。为了增强三维特征体积中视觉特征和语言特征之间的一致性，我们引入了多模态相似性约束。我们还引入了一种基于补丁的联合对比损失，这有助于鼓励对象区域在3D特征空间中合并，从而产生更精确的边界。与先前的基于NeRF的方法相比，在各种真实世界场景上的实验显示出在3D场景分解任务中的优越性能。 et.al.|[2405.05010](http://arxiv.org/abs/2405.05010)|null|
|**2024-05-09**|**Radar Fields: Frequency-Space Neural Scene Representations for FMCW Radar**|神经场作为再现和新一代各种户外场景的场景表示，包括自动驾驶汽车和机器人必须处理的场景，已经得到了广泛的研究。虽然存在RGB和激光雷达数据的成功方法，但雷达作为传感模式的神经重建方法在很大程度上尚未被探索。雷达传感器在毫米波长下工作，对雾和雨中的散射具有鲁棒性，因此为主动和被动光学传感技术提供了一种互补的方式。此外，现有的雷达传感器具有很高的成本效益，并广泛应用于户外作业的机器人和车辆中。我们介绍了雷达场——一种为有源雷达成像器设计的神经场景重建方法。我们的方法将一个明确的、基于物理的传感器模型与一个隐含的神经几何和反射模型相结合，直接合成原始雷达测量值并提取场景占用率。所提出的方法不依赖于体绘制。相反，我们在傅立叶频率空间中学习场，并用原始雷达数据进行监督。我们在不同的室外场景中验证了该方法的有效性，包括车辆和基础设施密集的城市场景，以及在毫米波长传感特别有利的恶劣天气场景中。 et.al.|[2405.04662](http://arxiv.org/abs/2405.04662)|null|
|**2024-05-06**|**Neural Graph Mapping for Dense SLAM with Efficient Loop Closure**|现有的基于神经场的SLAM方法通常使用单个单片场作为其场景表示。这阻碍了循环闭合约束的有效结合，并限制了可扩展性。为了解决这些缺点，我们提出了一种神经映射框架，该框架将轻量级神经场锚定到稀疏视觉SLAM系统的姿态图上。我们的方法显示了整合大规模闭环的能力，同时限制了必要的重新融合。此外，我们通过在优化过程中考虑多个环路闭合来验证我们的方法的可扩展性，并证明我们的方法在质量和运行时间方面优于现有的最先进的方法。我们的代码可在https://kth-rpl.github.io/neural_graph_mapping/. et.al.|[2405.03633](http://arxiv.org/abs/2405.03633)|null|
|**2024-05-03**|**Simulation-based Inference of Developmental EEG Maturation with the Spectral Graph Model**|宏观神经活动的光谱内容在整个发育过程中不断演变，但这种成熟与潜在的大脑网络形成和动力学之间的关系尚不清楚。为了深入了解这一过程的机制，我们通过频谱图模型（SGM）的贝叶斯模型反演来评估发育脑电频谱变化，SGM是一种全脑空间频谱活动的简约模型，源于由结构连接体耦合的线性化神经场模型。基于模拟的推理用于从跨越发育期的脑电图频谱中估计年龄变化的SGM参数后验分布。我们发现，这种模型拟合方法通过关键神经参数的神经生物学一致进展准确地捕捉了脑电图频谱的发育成熟：长程耦合、轴突传导速度和兴奋性：抑制性平衡。这些结果表明，在正常发育过程中观察到的大脑活动的光谱成熟得到了功能适应的支持，特别是局部神经动力学的年龄依赖性调节及其在宏观结构网络中的长期耦合。 et.al.|[2405.02524](http://arxiv.org/abs/2405.02524)|null|
|**2024-04-30**|**Lightplane: Highly-Scalable Components for Neural 3D Fields**|当代3D研究，特别是在重建和生成方面，严重依赖2D图像进行输入或监督。然而，这些2D-3D映射的当前设计是内存密集型的，对现有方法构成了显著的瓶颈，并阻碍了新的应用。作为回应，我们为3D神经场提出了一对高度可扩展的组件：Lightplane Render和Splatter，这显著减少了2D-3D映射中的内存使用。这些创新能够以较小的内存和计算成本处理更多、更高分辨率的图像。我们展示了它们在各种应用中的实用性，从有利于图像级损失的单场景优化到实现用于大幅缩放3D重建和生成的多功能管道。代码：\url{https://github.com/facebookresearch/lightplane}. et.al.|[2404.19760](http://arxiv.org/abs/2404.19760)|**[link](https://github.com/facebookresearch/lightplane)**|
|**2024-05-03**|**Object Registration in Neural Fields**|神经场以一种对机器人应用具有巨大前景的方式提供3D几何结构和外观的连续场景表示。解锁机器人中神经领域独特用例的一个功能是对象6-DoF注册。在本文中，我们对最近的Reg-NF神经场配准方法及其在机器人环境中的用例进行了扩展分析。我们展示了使用场景和对象神经场模型确定场景中已知对象的6-DoF姿态的场景。我们展示了如何使用它来更好地表示未完全建模的场景中的对象，并通过将对象神经场模型替换到场景中来生成新的场景。 et.al.|[2404.18381](http://arxiv.org/abs/2404.18381)|null|
|**2024-04-26**|**ArtNeRF: A Stylized Neural Field for 3D-Aware Cartoonized Face Synthesis**|生成视觉模型和神经辐射领域的最新进展极大地促进了3D感知图像合成和风格化任务。然而，以前基于NeRF的工作仅限于单场景风格化，训练模型生成具有任意风格的3D感知卡通人脸仍然没有解决。为了解决这个问题，我们提出了ArtNeRF，这是一种从3D感知GAN中派生出来的新颖的人脸风格化框架。在这个框架中，我们利用表达生成器来合成风格化的人脸，并利用三分支鉴别器模块来提高生成人脸的视觉质量和风格一致性。具体而言，利用基于对比学习的风格编码器来提取风格图像的鲁棒低维嵌入，使生成器能够获得各种风格的知识。为了平滑跨领域迁移学习的训练过程，我们提出了一个自适应风格混合模块，该模块有助于注入风格信息，并允许用户自由调整风格化水平。我们进一步引入了一个神经渲染模块，以实现更高分辨率图像的高效实时渲染。大量实验表明，ArtNeRF在生成具有任意风格的高质量3D感知卡通人脸方面是通用的。 et.al.|[2404.13711](http://arxiv.org/abs/2404.13711)|**[link](https://github.com/silence-tang/artnerf)**|
|**2024-04-19**|**BANF: Band-limited Neural Fields for Levels of Detail Reconstruction**|主要由于其隐含性质，神经场缺乏直接的滤波机制，因为离散信号处理的傅立叶分析不直接适用于这些表示。神经场的有效滤波对于实现下游应用程序中的细节处理水平至关重要，并支持在规则网格上对场进行采样的操作（例如，行进立方体）。试图在频域中分解神经场的现有方法要么采用启发式方法，要么需要对神经场架构进行广泛修改。我们展示了通过一个简单的修改，可以获得低通滤波的神经场，进而展示了如何利用这一点来获得整个信号的频率分解。我们通过研究细节水平重建来证明我们的技术的有效性，并展示了如何有效地计算粗糙的表示。 et.al.|[2404.13024](http://arxiv.org/abs/2404.13024)|null|
|**2024-04-15**|**Efficient and accurate neural field reconstruction using resistive memory**|人类通过将稀疏的观测整合到大规模互连的突触和神经元中来构建空间感知，提供了卓越的并行性和效率。在人工智能中复制这一能力在医学成像、AR/VR和嵌入式人工智能中有着广泛的应用，在这些领域，输入数据往往是稀疏的，计算资源有限。然而，传统的数字计算机信号重构方法面临着软硬件两方面的挑战。在软件方面，传统显式信号表示中的存储效率低下会带来困难。硬件障碍包括冯·诺依曼瓶颈，它限制了CPU和存储器之间的数据传输，以及CMOS电路在支持并行处理方面的局限性。我们提出了一种软硬件协同优化的系统方法，用于从稀疏输入重建信号。在软件方面，我们使用神经场通过神经网络隐式地表示信号，并使用低秩分解和结构化修剪对其进行进一步压缩。在硬件方面，我们设计了一个基于电阻存储器的内存计算（CIM）平台，该平台具有高斯编码器（GE）和MLP处理引擎（PE）。GE利用电阻存储器的内在随机性进行有效的输入编码，而PE通过硬件感知量化（HAQ）电路实现精确的权重映射。我们在基于40nm 256Kb电阻存储器的内存内计算宏上展示了该系统的功效，在不影响3D CT稀疏重建、新视图合成和动态场景新视图合成等任务的重建质量的情况下，实现了巨大的能效和并行性改进。这项工作推进了人工智能驱动的信号恢复技术，为未来高效、稳健的医疗人工智能和3D视觉应用铺平了道路。 et.al.|[2404.09613](http://arxiv.org/abs/2404.09613)|null|
|**2024-04-10**|**Ray-driven Spectral CT Reconstruction Based on Neural Base-Material Fields**|在谱CT重建中，基底材料分解涉及求解大规模非线性积分方程组，这在数学上是高度不适定的。本文提出了一种模型，该模型使用神经场表示来参数化对象的衰减系数，从而避免了线积分离散化过程中像素驱动的投影系数矩阵的复杂计算。介绍了一种基于光线驱动神经场的线积分轻量级离散化方法，提高了离散化过程中积分逼近的精度。将基底材料表示为连续的向量值隐函数，以建立基底材料的神经场参数化模型。然后使用深度学习的自动微分框架来求解神经基底材料场的隐式连续函数。该方法不受重建图像空间分辨率的限制，并且网络具有紧凑和规则的特性。实验验证表明，我们的方法在处理光谱CT重建方面表现得非常好。此外，它还满足了生成高分辨率重建图像的要求。 et.al.|[2404.06991](http://arxiv.org/abs/2404.06991)|null|

<p align=right>(<a href=#updated-on-20240513>back to top</a>)</p>

[contributors-shield]: https://img.shields.io/github/contributors/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[contributors-url]: https://github.com/Vincentqyw/cv-arxiv-daily/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[forks-url]: https://github.com/Vincentqyw/cv-arxiv-daily/network/members
[stars-shield]: https://img.shields.io/github/stars/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[stars-url]: https://github.com/Vincentqyw/cv-arxiv-daily/stargazers
[issues-shield]: https://img.shields.io/github/issues/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[issues-url]: https://github.com/Vincentqyw/cv-arxiv-daily/issues

