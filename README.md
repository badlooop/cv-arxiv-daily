[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]

## Updated on 2025.02.18
> Usage instructions: [here](./docs/README.md#usage)

<details>
  <summary>Table of Contents</summary>
  <ol>
    <li><a href=#video-diffusion>Video Diffusion</a></li>
    <li><a href=#3d>3D</a></li>
    <li><a href=#3d-reconstruction>3D Reconstruction</a></li>
    <li><a href=#diffusion>Diffusion</a></li>
    <li><a href=#nerf>NeRF</a></li>
  </ol>
</details>

## Video Diffusion

|Publish Date|Title|Abstract|PDF|Code|
|---|---|---|---|---|
|**2025-02-14**|**Step-Video-T2V Technical Report: The Practice, Challenges, and Future of Video Foundation Model**|我们介绍了Step-Video-T2V，这是一种最先进的文本到视频预训练模型，具有30B参数，能够生成长达204帧的视频。深度压缩变分自编码器Video VAE专为视频生成任务而设计，可实现16x16的空间和8倍的时间压缩比，同时保持出色的视频重建质量。用户提示使用两个双语文本编码器进行编码，以处理英语和中文。使用流匹配训练具有3D全注意力的DiT，并将其用于将输入噪声去噪到潜在帧中。应用基于视频的DPO方法video DPO来减少伪影并提高生成视频的视觉质量。我们还详细介绍了我们的培训策略，并分享了关键的观察结果和见解。Step-Video-T2V的性能在一个新的视频生成基准Step-Video-T2V-Eval上进行了评估，与开源和商业引擎相比，展示了其最先进的文本到视频质量。此外，我们讨论了当前基于扩散的模型范式的局限性，并概述了视频基础模型的未来方向。我们提供Step-Video-T2V和Step-Video-T2V-Eval，网址为https://github.com/stepfun-ai/Step-Video-T2V.在线版本可以从以下网址访问https://yuewen.cn/videos也。我们的目标是加速视频基础模型的创新，并赋予视频内容创作者权力。 et.al.|[2502.10248](http://arxiv.org/abs/2502.10248)|null|
|**2025-02-14**|**RealCam-I2V: Real-World Image-to-Video Generation with Interactive Complex Camera Control**|与基于文本的方法相比，相机轨迹引导图像到视频生成的最新进展为复杂的相机控制提供了更高的精度和更好的支持。然而，它们也带来了重大的可用性挑战，因为用户在处理任意真实世界的图像时，在不了解其深度或场景比例的情况下，往往难以提供精确的相机参数。为了解决这些现实世界的应用问题，我们提出了RealCam-I2V，这是一种新的基于扩散的视频生成框架，它集成了单目度量深度估计，在预处理步骤中建立了3D场景重建。在训练过程中，重建的3D场景能够将相机参数从相对值缩放到绝对值，确保不同真实世界图像的兼容性和缩放一致性。因此，RealCam-I2V提供了一个直观的界面，用户可以通过在3D场景中拖动来精确绘制相机轨迹。为了进一步增强精确的相机控制和场景一致性，我们提出了场景约束噪声整形，该整形可以整形高级别噪声，并允许该框架在低噪声阶段保持动态、连贯的视频生成。RealCam-I2V在RealEstate10K和域外图像的可控性和视频质量方面取得了显著改善。我们还支持相机控制的循环视频生成和生成帧插值等应用。我们将发布我们的绝对比例注释、代码和所有检查点。请在中查看动态结果https://zgctroy.github.io/RealCam-I2V. et.al.|[2502.10059](http://arxiv.org/abs/2502.10059)|null|
|**2025-02-14**|**GEVRM: Goal-Expressive Video Generation Model For Robust Visual Manipulation**|随着具身人工智能的快速发展，用于一般机器人决策的视觉语言动作（VLA）模型取得了重大进展。然而，大多数现有的VLAN都没有考虑到部署过程中不可避免的外部干扰。这些扰动向VLA引入了不可预见的状态信息，导致动作不准确，从而导致泛化性能显著下降。经典的内模控制（IMC）原理表明，具有包括外部输入信号的内部模型的闭环系统可以准确地跟踪参考输入并有效地抵消干扰。我们提出了一种新的闭环VLA方法GEVRM，该方法集成了IMC原理，以提高机器人视觉操纵的鲁棒性。GEVRM中的文本引导视频生成模型可以生成具有高度表现力的未来视觉规划目标。同时，我们通过模拟响应来评估扰动，这些响应被称为内部嵌入，并通过原型对比学习进行优化。这使得模型能够隐式地推断和区分来自外部环境的扰动。所提出的GEVRM在标准和扰动CALVIN基准上都达到了最先进的性能，并在现实的机器人任务中显示出显著的改进。 et.al.|[2502.09268](http://arxiv.org/abs/2502.09268)|null|
|**2025-02-12**|**CineMaster: A 3D-Aware and Controllable Framework for Cinematic Text-to-Video Generation**|在这项工作中，我们提出了CineMaster，这是一个用于3D感知和可控文本到视频生成的新框架。我们的目标是为用户提供与专业电影导演相当的可控性：在场景中精确放置物体，在3D空间中灵活操纵物体和相机，以及对渲染帧的直观布局控制。为了实现这一目标，CineMaster分两个阶段运行。在第一阶段，我们设计了一个交互式工作流程，允许用户通过定位对象边界框和定义3D空间内的相机运动来直观地构建3D感知条件信号。在第二阶段，这些控制信号——包括渲染的深度图、相机轨迹和对象类标签——作为文本到视频扩散模型的指导，确保生成用户期望的视频内容。此外，为了克服具有3D对象运动和相机姿态注释的野外数据集的稀缺性，我们仔细建立了一个自动数据注释管道，从大规模视频数据中提取3D边界框和相机轨迹。大量的定性和定量实验表明，CineMaster明显优于现有方法，并实现了出色的3D感知文本到视频生成。项目页面：https://cinemaster-dev.github.io/. et.al.|[2502.08639](http://arxiv.org/abs/2502.08639)|null|
|**2025-02-12**|**FloVD: Optical Flow Meets Video Diffusion Model for Enhanced Camera-Controlled Video Synthesis**|本文介绍了FloVD，这是一种基于光流的新型视频扩散模型，用于相机可控视频生成。FloVD利用光流图来表示相机和运动物体的运动。这种方法有两个关键好处。由于光流可以直接从视频中估计出来，因此我们的方法允许在没有地面实况相机参数的情况下使用任意训练视频。此外，由于背景光流编码了不同视点之间的3D相关性，我们的方法通过利用背景运动实现了详细的相机控制。为了在支持详细相机控制的同时合成自然物体运动，我们的框架采用了一个由光流生成和流调节视频合成组成的两级视频合成流水线。大量实验表明，在精确的相机控制和自然物体运动合成方面，我们的方法比以前的方法具有优越性。 et.al.|[2502.08244](http://arxiv.org/abs/2502.08244)|null|
|**2025-02-12**|**Learning Human Skill Generators at Key-Step Levels**|我们致力于在关键步骤层面学习人类技能生成器。技能的生成是一项具有挑战性的工作，但它的成功实施可以极大地促进人类的技能学习，并为具身智能提供更多的经验。尽管当前的视频生成模型可以合成简单和原子的人类操作，但由于其复杂的过程，它们在人类技能方面存在困难。人类技能涉及多步骤、长时间的动作和复杂的场景转换，因此现有的合成长视频的朴素自回归方法无法生成人类技能。为了解决这个问题，我们提出了一项新任务，即关键步骤技能生成（KS Gen），旨在降低生成人类技能视频的复杂性。给定初始状态和技能描述，任务是生成完成技能的关键步骤的视频片段，而不是全长视频。为了支持这项任务，我们引入了一个精心策划的数据集，并定义了多个评估指标来评估绩效。考虑到KS Gen的复杂性，我们为这项任务提出了一个新的框架。首先，多模态大型语言模型（MLLM）使用检索参数生成关键步骤的描述。随后，我们使用关键步骤图像生成器（KIG）来解决技能视频中关键步骤之间的不连续性。最后，视频生成模型使用这些描述和关键步骤图像来生成具有高时间一致性的关键步骤的视频片段。我们对结果进行了详细分析，希望为人类技能生成提供更多见解。所有模型和数据均可在https://github.com/MCG-NJU/KS-Gen. et.al.|[2502.08234](http://arxiv.org/abs/2502.08234)|null|
|**2025-02-12**|**AnyCharV: Bootstrap Controllable Character Video Generation with Fine-to-Coarse Guidance**|角色视频生成是一个重要的现实世界应用程序，专注于制作具有特定角色的高质量视频。最近的进步引入了各种控制信号来制作静态角色的动画，成功地增强了对生成过程的控制。然而，这些方法往往缺乏灵活性，限制了它们的适用性，并使用户难以将源角色合成到所需的目标场景中。为了解决这个问题，我们提出了一种新的框架AnyCharV，该框架在姿态信息的指导下，使用任意源角色和目标场景灵活生成角色视频。我们的方法包括两个阶段的训练过程。在第一阶段，我们开发了一个基础模型，该模型能够使用姿态引导将源角色与目标场景集成在一起。第二阶段通过自增强机制进一步引导可控生成，我们使用第一阶段生成的视频，用粗掩模替换精细掩模，从而更好地保留角色细节，实现训练结果。实验结果证明了我们提出的方法的有效性和鲁棒性。我们的项目页面是https://anycharv.github.io. et.al.|[2502.08189](http://arxiv.org/abs/2502.08189)|null|
|**2025-02-12**|**Next Block Prediction: Video Generation via Semi-Autoregressive Modeling**|Next Token Prediction（NTP）是自回归（AR）视频生成的一种事实上的方法，但它存在次优单向依赖性和推理速度慢的问题。在这项工作中，我们提出了一种用于视频生成的半自回归（半AR）框架，称为下一块预测（NBP）。通过将视频内容统一分解为大小相等的块（例如，行或帧），我们将生成单元从单个令牌转移到块，允许当前块中的每个令牌同时预测下一个块中的相应令牌。与传统的AR建模不同，我们的框架在每个块内采用双向注意力，使令牌能够捕获更强大的空间依赖关系。通过并行预测多个令牌，NBP模型显著减少了生成步骤的数量，从而实现了更快、更高效的推理。我们的模型在UCF101上获得了103.3的FVD分数，在K600上获得了25.5的FVD评分，平均比vanilla NTP模型高出4.4。此外，由于推理步骤的减少，NBP模型每秒生成8.89帧（128x128分辨率），实现了11倍的加速。我们还探索了从700M到3B参数的模型尺度，观察到发电质量的显著提高，UCF101的FVD得分从103.3下降到55.3，K600的FVD分数从25.5下降到19.5，这证明了我们方法的可扩展性。 et.al.|[2502.07737](http://arxiv.org/abs/2502.07737)|null|
|**2025-02-14**|**Magic 1-For-1: Generating One Minute Video Clips within One Minute**|在本技术报告中，我们介绍了Magic 1-For-1（Magic141），这是一种高效的视频生成模型，具有优化的内存消耗和推理延迟。关键思想很简单：将文本到视频生成任务分解为两个单独的更容易的扩散步骤蒸馏任务，即文本到图像生成和图像到视频生成。我们验证了使用相同的优化算法，图像到视频任务确实比文本到视频任务更容易收敛。我们还从三个方面探索了一系列优化技巧，以降低训练图像到视频（I2V）模型的计算成本：1）通过使用多模态先验条件注入来加速模型收敛；2） 通过应用对抗性步骤蒸馏来加速推理延迟，以及3）通过参数稀疏化进行推理内存成本优化。通过这些技术，我们能够在3秒内生成5秒的视频片段。通过应用测试时间滑动窗口，我们能够在一分钟内生成一分钟长的视频，显著提高了视觉质量和运动动态，平均生成1秒视频片段的时间不到1秒。我们进行了一系列初步探索，以找出扩散阶跃蒸馏过程中计算成本和视频质量之间的最佳权衡，并希望这能成为开源探索的良好基础模型。代码和模型权重可在以下网址获得https://github.com/DA-Group-PKU/Magic-1-For-1. et.al.|[2502.07701](http://arxiv.org/abs/2502.07701)|**[link](https://github.com/da-group-pku/magic-1-for-1)**|
|**2025-02-12**|**VidCRAFT3: Camera, Object, and Lighting Control for Image-to-Video Generation**|最近的图像到视频生成方法在实现对一个或两个视觉元素（如相机轨迹或物体运动）的控制方面取得了成功。然而，由于数据和网络效率的限制，这些方法无法提供对多个视觉元素的控制。在本文中，我们介绍了VidCRAFT3，这是一种用于精确图像到视频生成的新框架，可以同时控制相机运动、物体运动和照明方向。为了更好地解耦对每个视觉元素的控制，我们提出了空间三重注意力转换器，它以对称的方式集成了照明方向、文本和图像。由于大多数真实世界的视频数据集缺乏照明注释，我们构建了一个高质量的合成视频数据集，即VideoLightingDirection（VLD）数据集。该数据集包括照明方向注释和不同外观的对象，使VidCRAFT3能够有效地处理强光透射和反射效果。此外，我们提出了一种三阶段训练策略，该策略消除了同时使用多个视觉元素（相机运动、物体运动和照明方向）注释训练数据的需要。对基准数据集的广泛实验证明了VidCRAFT3在制作高质量视频内容方面的功效，在控制粒度和视觉连贯性方面超越了现有的最先进方法。所有代码和数据都将公开。 et.al.|[2502.07531](http://arxiv.org/abs/2502.07531)|null|

<p align=right>(<a href=#updated-on-20250218>back to top</a>)</p>

## 3D

|Publish Date|Title|Abstract|PDF|Code|
|---|---|---|---|---|
|**2025-02-13**|**Large Images are Gaussians: High-Quality Large Image Representation with Levels of 2D Gaussian Splatting**|虽然内隐神经表征（INR）在图像表征方面取得了显著成功，但它们往往受到训练记忆大和解码速度慢的阻碍。最近，高斯散斑（GS）因其高质量的新颖视图合成和快速渲染能力而成为3D重建中一种有前景的解决方案，使其成为广泛应用的有价值的工具。特别是，基于GS的表示2DGS已经显示出图像拟合的潜力。在我们的工作中，我们提出\textbf{L}arge\textbf{I}magesare \textbf{G}aussians（\textbf{LIG}），深入研究了2DGS在图像表示中的应用，通过两个不同的修改解决了在高斯点众多的情况下用2DGS拟合大图像的挑战：1）我们采用了一种表示和优化策略的变体，促进了大量高斯点的拟合；2） 我们提出了一种高斯水平方法，用于重建粗略的低频初始化和精细的高频细节。因此，我们成功地将大图像表示为高斯点，并实现了高质量的大图像表示，证明了其在各种类型的大图像中的有效性。代码可在｛\href获得{https://github.com/HKU-MedAI/LIG}{https://github.com/HKU-MedAI/LIG}}. et.al.|[2502.09039](http://arxiv.org/abs/2502.09039)|**[link](https://github.com/hku-medai/lig)**|
|**2025-02-11**|**Matrix3D: Large Photogrammetry Model All-in-One**|我们提出了Matrix3D，这是一个统一的模型，可以执行多个摄影测量子任务，包括姿态估计、深度预测和使用相同模型的新颖视图合成。Matrix3D利用多模态扩散变换器（DiT）来整合多种模态的变换，如图像、相机参数和深度图。Matrix3D大规模多模式训练的关键在于结合掩码学习策略。这使得即使有部分完整的数据，如图像姿态和图像深度对的双模态数据，也能进行全模态模型训练，从而显著增加了可用的训练数据池。Matrix3D在姿态估计和新颖的视图合成任务中展示了最先进的性能。此外，它通过多轮交互提供精细控制，使其成为3D内容创建的创新工具。项目页面：https://nju-3dv.github.io/projects/matrix3d. et.al.|[2502.07685](http://arxiv.org/abs/2502.07685)|null|
|**2025-02-11**|**Flow Distillation Sampling: Regularizing 3D Gaussians with Pre-trained Matching Priors**|3D高斯散斑（3DGS）以快速的训练和渲染速度实现了出色的渲染质量。然而，其优化过程缺乏明确的几何约束，导致在稀疏或没有观测输入视图的区域进行次优几何重建。在这项工作中，我们试图通过在3DGS优化过程之前加入预训练的匹配来缓解这个问题。我们介绍了流动蒸馏采样（FDS），这是一种利用预先训练的几何知识来提高高斯辐射场准确性的技术。我们的方法采用了一种策略性采样技术，以输入视图附近的未观测视图为目标，利用匹配模型（先验流）计算的光流来引导根据3DGS几何（辐射流）分析计算的流。深度渲染、网格重建和新颖视图合成方面的综合实验展示了FDS相对于最先进方法的显著优势。此外，我们的解释性实验和分析旨在阐明FDS对几何精度和渲染质量的影响，从而为读者提供对其性能的见解。项目页面：https://nju-3dv.github.io/projects/fds et.al.|[2502.07615](http://arxiv.org/abs/2502.07615)|null|
|**2025-02-10**|**GAS: Generative Avatar Synthesis from a Single Image**|我们引入了一个通用和统一的框架，从单个图像中合成视图一致和时间连贯的化身，解决了单个图像化身生成的挑战性问题。虽然最近的方法采用了基于人类模板（如深度或法线图）的扩散模型，但由于稀疏驾驶信号与实际人类受试者之间的差异，它们往往难以保留外观信息，从而导致多视图和时间不一致。我们的方法通过将基于回归的3D人体重建的重建能力与扩散模型的生成能力相结合，弥合了这一差距。来自初始重建人体的密集驱动信号提供了全面的调节，确保了忠实于参考外观和结构的高质量合成。此外，我们提出了一个统一的框架，使从野生视频中的新颖姿态合成中学到的泛化能力能够自然地转移到新颖的视图合成中。我们的基于视频的扩散模型通过高质量的视图一致性渲染来增强解纠缠合成，以获得新颖的视图和新颖姿势动画中逼真的非刚性变形。结果表明，我们的方法在野生数据集中具有跨域和跨域的优越泛化能力。项目页面：https://humansensinglab.github.io/GAS/ et.al.|[2502.06957](http://arxiv.org/abs/2502.06957)|null|
|**2025-02-10**|**SIREN: Semantic, Initialization-Free Registration of Multi-Robot Gaussian Splatting Maps**|我们提出了SIREN用于多机器人高斯散点（GSplat）地图的注册，对相机姿态、图像和用于初始化或融合局部子地图的地图间变换零访问。为了实现这些功能，SIREN以三种关键方式利用语义的通用性和鲁棒性，为多机器人GSplat地图推导出严格的配准流水线。首先，SIREN利用语义来识别局部图中特征丰富的区域，在这些区域中更好地提出了配准问题，从而消除了先前工作中通常需要的任何初始化。其次，SIREN使用鲁棒的语义特征来识别局部地图中高斯之间的候选对应关系，为鲁棒的几何优化奠定了基础，粗略地对齐了从局部地图中提取的3D高斯基元。第三，这一关键步骤使子图之间的变换能够进行后续的光度细化，其中SIREN利用GSplat图中的新颖视图合成以及基于语义的图像滤波器来计算高精度的非刚性变换，以生成高保真融合图。我们在一系列真实世界的数据集中，特别是在最广泛使用的机器人硬件平台上，包括机械手、无人机和四足动物，展示了SIREN与竞争基线相比的卓越性能。在我们的实验中，SIREN在最具挑战性的场景中实现了约90倍的较小旋转误差、300倍的较小平移误差和44倍的较小尺度误差，在这些场景中，竞争方法很难解决。在审查过程结束后，我们将发布代码并提供项目页面的链接。 et.al.|[2502.06519](http://arxiv.org/abs/2502.06519)|null|
|**2025-02-05**|**VistaFlow: Photorealistic Volumetric Reconstruction with Dynamic Resolution Management via Q-Learning**|我们介绍VistaFlow，这是一种可扩展的三维成像技术，能够从一组二维照片中重建完全交互式的三维体积图像。我们的模型通过一个可微分的渲染系统来合成新的视点，该系统能够对逼真的3D场景进行动态分辨率管理。我们通过引入QuiQ来实现这一目标，QuiQ是一种通过Q学习训练的新型中间视频控制器，通过以毫秒精度调整渲染分辨率来保持一致的高帧率。值得注意的是，VistaFlow在集成CPU图形上本地运行，使其适用于移动和入门级设备，同时仍能提供高性能渲染。VistaFlow绕过神经辐射场（NeRF），使用PlenOctree数据结构以最低的硬件要求渲染复杂的光相互作用，如反射和次表面散射。我们的模型能够在消费类硬件上以每秒100帧以上的1080p分辨率进行新颖的视图合成，从而超越最先进的方法。通过根据每个设备的功能定制渲染质量，VistaFlow有可能提高从高端工作站到廉价微控制器等各种硬件的真实感3D场景渲染的效率和可访问性。 et.al.|[2502.05222](http://arxiv.org/abs/2502.05222)|null|
|**2025-02-11**|**PoI: Pixel of Interest for Novel View Synthesis Assisted Scene Coordinate Regression**|通过新的视图合成技术，如NeRF和高斯散斑，可以增强估计相机姿态的任务，以增加训练数据的多样性和扩展性。然而，这些技术通常会产生模糊和重影等问题的渲染图像，从而影响其可靠性。对于在像素级别估计3D坐标的场景坐标回归（SCR）方法来说，这些问题变得尤为明显。为了缓解与不可靠渲染图像相关的问题，我们引入了一种新的滤波方法，该方法选择性地提取渲染良好的像素，同时丢弃较差的像素。该滤波器在训练过程中同时测量SCR模型的实时重投影损失和梯度。基于这种滤波技术，我们还开发了一种新的策略，利用稀疏输入改进场景坐标回归，并借鉴了稀疏输入技术在新颖视图合成中的成功应用。我们的实验结果验证了我们方法的有效性，在室内和室外数据集上展示了最先进的性能。 et.al.|[2502.04843](http://arxiv.org/abs/2502.04843)|null|
|**2025-02-05**|**Controllable Satellite-to-Street-View Synthesis with Precise Pose Alignment and Zero-Shot Environmental Control**|从卫星图像生成街景图像是一项具有挑战性的任务，特别是在保持精确的姿态对齐和结合不同的环境条件方面。虽然扩散模型在生成任务中显示出了希望，但它们在整个扩散过程中保持严格姿态对齐的能力是有限的。本文提出了一种新的迭代单应性调整（IHA）方案，应用于去噪过程中，有效地解决了姿态失准问题，并确保了生成的街景图像的空间一致性。此外，目前，用于卫星到街道视图生成的可用数据集在光照和天气条件的多样性方面受到限制，从而限制了生成输出的通用性。为了缓解这种情况，我们引入了一种文本引导的照明和天气控制的采样策略，可以对环境因素进行精细控制。大量的定量和定性评估表明，我们的方法显著提高了姿态精度，增强了生成的街景图像的多样性和真实性，为卫星到街景生成任务设定了新的基准。 et.al.|[2502.03498](http://arxiv.org/abs/2502.03498)|null|
|**2025-02-04**|**Geometric Neural Process Fields**|本文解决了神经场（NeF）泛化的挑战，其中模型必须有效地适应仅给出少量观测值的新信号。为了解决这个问题，我们提出了几何神经过程场（G-NPF），这是一个明确捕捉不确定性的神经辐射场的概率框架。我们将NeF泛化表述为概率问题，从而能够从有限的上下文观测中直接推断出NeF函数分布。为了引入结构归纳偏差，我们引入了一组几何基来编码空间结构，并促进NeF函数分布的推断。在此基础上，我们设计了一个分层潜在变量模型，使G-NPF能够整合多个空间层次的结构信息，并有效地参数化INR函数。这种分层方法提高了对新场景和未知信号的泛化能力。针对3D场景的新颖视图合成以及2D图像和1D信号回归的实验证明了我们的方法在捕捉不确定性和利用结构信息提高泛化能力方面的有效性。 et.al.|[2502.02338](http://arxiv.org/abs/2502.02338)|null|
|**2025-02-05**|**GP-GS: Gaussian Processes for Enhanced Gaussian Splatting**|3D高斯散斑已经成为一种高效的真实感新型视图合成方法。然而，它对稀疏运动结构（SfM）点云的依赖一直会损害场景重建的质量。为了解决这些局限性，本文提出了一种新的3D重建框架高斯过程高斯散斑（GP-GS），其中开发了一个多输出高斯过程模型，以实现稀疏SfM点云的自适应和不确定性引导的致密化。具体来说，我们提出了一种动态采样和滤波流水线，通过利用基于GP的预测从输入的2D像素和深度图中推断出新的候选点，自适应地扩展SfM点云。该管道利用不确定性估计来指导高方差预测的修剪，确保几何一致性，并能够生成密集的点云。加密的点云提供了高质量的初始3D高斯分布，以提高重建性能。在各种规模的合成和真实世界数据集上进行的广泛实验验证了所提出框架的有效性和实用性。 et.al.|[2502.02283](http://arxiv.org/abs/2502.02283)|null|

<p align=right>(<a href=#updated-on-20250218>back to top</a>)</p>

## 3D Reconstruction

|Publish Date|Title|Abstract|PDF|Code|
|---|---|---|---|---|
|**2025-02-14**|**ReStyle3D: Scene-Level Appearance Transfer with Semantic Correspondences**|我们介绍了ReStyle3D，这是一个新颖的框架，用于将场景级外观从单个样式图像转换为由多个视图表示的真实场景。该方法将显式语义对应与多视图一致性相结合，实现精确连贯的风格化。与全局应用参考样式的传统样式化方法不同，ReStyle3D使用开放式词汇分割在样式和现实世界图像之间建立密集的实例级对应关系。这确保了每个对象都具有语义匹配的纹理。它首先使用扩散模型中的无训练语义注意力机制将样式转移到单个视图。然后，它通过学习扭曲将样式化提升到其他视图，并在单目深度和像素对应的指导下优化网络。实验表明，ReStyle3D在结构保持、感知风格相似性和多视图连贯性方面始终优于现有方法。用户研究进一步验证了它产生逼真、语义忠实的结果的能力。我们的代码、预训练模型和数据集将公开发布，以支持室内设计、虚拟舞台和3D一致性风格化中的新应用。 et.al.|[2502.10377](http://arxiv.org/abs/2502.10377)|null|
|**2025-02-13**|**PUGS: Perceptual Uncertainty for Grasp Selection in Underwater Environments**|当在感官信息不完美和不完整的具有挑战性的环境中导航和交互时，机器人必须做出考虑这些缺点的决定。我们提出了一种通过占用不确定性估计来量化和表示3D重建中这种感知不确定性的新方法。我们开发了一个框架，将其纳入水下环境中自主操纵的抓取选择中。在决定从哪个位置抓取时，我们没有平等对待每个测量值，而是提出了一个框架，将多视图重建过程中固有的不确定性传播到抓取选择中。我们用模拟和真实世界的数据来评估我们的方法，结果表明，通过考虑不确定性，抓取选择对部分和噪声测量变得鲁棒。代码将在以下网址提供https://onurbagoren.github.io/PUGS/ et.al.|[2502.09824](http://arxiv.org/abs/2502.09824)|null|
|**2025-02-13**|**Latent Radiance Fields with 3D-aware 2D Representations**|潜在的3D重建在通过将2D特征提取到3D空间中来增强3D语义理解和3D生成方面显示出巨大的前景。然而，现有的方法难以解决2D特征空间和3D表示之间的域差距，导致渲染性能下降。为了应对这一挑战，我们提出了一种新的框架，将3D意识整合到2D潜在空间中。该框架由三个阶段组成：（1）增强2D潜在表示的3D一致性的对应感知自动编码方法，（2）将这些3D感知的2D表示提升到3D空间的潜在辐射场（LRF），以及（3）改进从渲染的2D表示进行图像解码的VAE辐射场（VAE-RF）对齐策略。大量实验表明，我们的方法在合成性能和跨数据集泛化能力方面优于最先进的潜在3D重建方法，适用于各种室内和室外场景。据我们所知，这是第一项表明由2D潜在表示构建的辐射场表示可以产生逼真的3D重建性能的工作。 et.al.|[2502.09613](http://arxiv.org/abs/2502.09613)|null|
|**2025-02-13**|**Large Images are Gaussians: High-Quality Large Image Representation with Levels of 2D Gaussian Splatting**|虽然内隐神经表征（INR）在图像表征方面取得了显著成功，但它们往往受到训练记忆大和解码速度慢的阻碍。最近，高斯散斑（GS）因其高质量的新颖视图合成和快速渲染能力而成为3D重建中一种有前景的解决方案，使其成为广泛应用的有价值的工具。特别是，基于GS的表示2DGS已经显示出图像拟合的潜力。在我们的工作中，我们提出\textbf{L}arge\textbf{I}magesare \textbf{G}aussians（\textbf{LIG}），深入研究了2DGS在图像表示中的应用，通过两个不同的修改解决了在高斯点众多的情况下用2DGS拟合大图像的挑战：1）我们采用了一种表示和优化策略的变体，促进了大量高斯点的拟合；2） 我们提出了一种高斯水平方法，用于重建粗略的低频初始化和精细的高频细节。因此，我们成功地将大图像表示为高斯点，并实现了高质量的大图像表示，证明了其在各种类型的大图像中的有效性。代码可在｛\href获得{https://github.com/HKU-MedAI/LIG}{https://github.com/HKU-MedAI/LIG}}. et.al.|[2502.09039](http://arxiv.org/abs/2502.09039)|**[link](https://github.com/hku-medai/lig)**|
|**2025-02-13**|**Re $^3$Sim: Generating High-Fidelity Simulation Data via 3D-Photorealistic Real-to-Sim for Robotic Manipulation**|机器人的真实世界数据收集成本高昂，资源密集，需要熟练的操作员和昂贵的硬件。仿真提供了一种可扩展的替代方案，但由于几何和视觉差距，往往无法实现模拟到真实的泛化。为了应对这些挑战，我们提出了一种3D逼真的真实到模拟系统，即RE$^3$sim，解决了几何和视觉上的模拟到真实的差距。RE$^3$ SIM采用先进的3D重建和神经渲染技术，忠实地重建现实世界的场景，在基于物理的模拟器中实时渲染模拟的交叉视图相机。通过利用特权信息在仿真中有效地收集专家演示，并用模仿学习训练机器人策略，我们验证了真实到模拟到真实管道在各种操纵任务场景中的有效性。值得注意的是，只需模拟数据，我们就可以实现零样本模拟到真实传输，平均成功率超过58%。为了突破真实到模拟的极限，我们进一步生成了一个大规模的模拟数据集，演示了如何从跨各种对象的模拟数据中构建稳健的策略。代码和演示可在以下网址获得：http://xshenhan.github.io/Re3Sim/. et.al.|[2502.08645](http://arxiv.org/abs/2502.08645)|null|
|**2025-02-11**|**EventEgo3D++: 3D Human Motion Capture from a Head-Mounted Event Camera**|单眼以自我为中心的3D人体运动捕捉仍然是一个重大挑战，特别是在低光照和快速运动的条件下，这在头戴式设备应用中很常见。在这些条件下，依赖RGB相机的现有方法往往会失败。为了解决这些局限性，我们引入了EventEgo3D++，这是第一种利用带有鱼眼镜头的单眼事件相机进行3D人体运动捕捉的方法。由于其高时间分辨率，事件相机在高速场景和变化的照明中表现出色，为准确的3D人体运动捕捉提供了可靠的线索。EventEgo3D++利用事件流的LNES表示来实现精确的3D重建。我们还开发了一种配备事件摄像头的移动头戴式设备（HMD）原型，除了合成数据集外，还捕获了一个全面的数据集，其中包括来自受控工作室环境和野外环境的真实事件观察结果。此外，为了提供更全面的数据集，我们包括了提供HMD佩戴者不同视角的非中心RGB流，以及相应的SMPL身体模型。我们的实验表明，与现有解决方案相比，EventEgo3D++即使在具有挑战性的条件下也能实现更高的3D精度和鲁棒性。此外，我们的方法支持以140Hz的速率进行实时3D姿态更新。这项工作是EventEgo3D方法（CVPR 2024）的扩展，进一步推进了以自我为中心的3D人体运动捕捉的最新技术。有关更多详细信息，请访问项目页面https://eventego3d.mpi-inf.mpg.de. et.al.|[2502.07869](http://arxiv.org/abs/2502.07869)|null|
|**2025-02-10**|**TripoSG: High-Fidelity 3D Shape Synthesis using Large-Scale Rectified Flow Models**|扩散技术的最新进展将图像和视频生成推向了前所未有的质量水平，显著加速了生成式人工智能的部署和应用。然而，由于3D数据规模的限制、3D数据处理的复杂性以及对3D领域先进技术的探索不足，3D形状生成技术迄今为止一直落后。当前的3D形状生成方法在输出质量、泛化能力和与输入条件的对齐方面面临着巨大的挑战。我们提出了TripoSG，这是一种新的流线型形状扩散范式，能够生成与输入图像精确对应的高保真3D网格。具体来说，我们提出：1）一种用于3D形状生成的大型整流流量变换器，通过对大量高质量数据的训练实现最先进的保真度。2） 一种混合监督训练策略，结合SDF、正常损失和程知损失，用于3D VAE，实现高质量的3D重建性能。3） 一个数据处理管道，用于生成200万个高质量的3D样本，突出了训练3D生成模型时数据质量和数量的关键规则。通过全面的实验，我们验证了新框架中每个组件的有效性。这些部件的无缝集成使TripoSG在3D形状生成方面达到了最先进的性能。由于高分辨率功能，由此产生的3D形状显示出增强的细节，并对输入图像表现出卓越的保真度。此外，TripoSG在从不同的图像风格和内容生成3D模型方面表现出了更强的通用性，展示了强大的生成能力。为了促进3D生成领域的进步和创新，我们将公开我们的模型。 et.al.|[2502.06608](http://arxiv.org/abs/2502.06608)|null|
|**2025-02-07**|**SC-OmniGS: Self-Calibrating Omnidirectional Gaussian Splatting**|360度相机通过捕获全面的场景数据，简化了辐射场3D重建的数据收集。然而，传统的辐射场方法并没有解决360度图像固有的具体挑战。我们提出了SC OmniGS，这是一种新型的自校准全向高斯散射系统，用于使用360度图像快速准确地重建全向辐射场。我们没有将360度图像转换为立方体图并执行透视图像校准，而是将360度图视为一个完整的球体，并推导出一个数学框架，该框架能够实现直接的全向相机姿态校准，并伴随着3D高斯优化。此外，我们引入了一种可微分的全向相机模型，以纠正现实世界数据的失真，从而提高性能。总体而言，通过最小化加权球面光度损失，对全向相机的内在模型、外在姿态和3D高斯分布进行了联合优化。广泛的实验表明，我们提出的SC OmniGS能够从嘈杂的相机姿态中恢复高质量的辐射场，甚至在以宽基线和非对象中心配置为特征的具有挑战性的场景中没有姿态。消费级全向相机捕获的真实世界数据集中的显著性能提升验证了我们的通用全向相机模型在减少360度图像失真方面的有效性。 et.al.|[2502.04734](http://arxiv.org/abs/2502.04734)|null|
|**2025-02-06**|**Measuring Physical Plausibility of 3D Human Poses Using Physics Simulation**|在物理场景中对人类进行建模对于理解涉及增强现实或从视频中评估人类行为（如体育或身体康复）的应用程序中的人类与环境交互至关重要。最先进的文献从单目或多视角的3D人体姿势开始，并使用这种表示将人固定在3D世界空间中。虽然精度的标准指标捕捉了关节位置误差，但它们并没有考虑3D姿势的物理合理性。这一局限性促使研究人员提出了评估抖动、地板穿透和不平衡姿势的其他指标。然而，这些方法测量的是独立的误差实例，并不代表运动过程中的平衡或稳定性。在这项工作中，我们建议从物理模拟中测量物理合理性。我们引入了两个指标来捕捉来自任何3D人体姿态估计模型的预测3D姿态的物理合理性和稳定性。通过物理模拟，我们发现了与现有合理性度量和运动过程中测量稳定性的相关性。我们评估并比较了两种最先进的方法的性能，即多视图三角基线和来自Human3.6m数据集的地面真实3D标记。 et.al.|[2502.04483](http://arxiv.org/abs/2502.04483)|**[link](https://github.com/MichiganCOG/Simulation_Physical_Plausibility)**|
|**2025-02-06**|**sshELF: Single-Shot Hierarchical Extrapolation of Latent Features for 3D Reconstruction from Sparse-Views**|由于视图重叠最小，从稀疏的朝外视图重建无边界的室外场景带来了重大挑战。以前的方法通常缺乏跨场景理解，其以原始为中心的公式会过载局部特征以补偿缺失的全局上下文，导致场景中看不见的部分模糊。我们提出了sshELF，这是一种通过潜在特征的分层外推进行稀疏视图3D场景重建的快速单镜头流水线。我们的关键见解是，从原始解码中提取信息外推，可以在训练场景中有效地传递结构模式。我们的方法：（1）学习跨场景先验来生成中间虚拟视图，以外推到未观察到的区域，（2）提供了一种将虚拟视图生成与3D原始解码分离的两阶段网络设计，用于高效训练和模块化模型设计，（3）集成了一个预训练的基础模型，用于联合推断潜在特征和纹理，提高了场景理解和泛化能力。sshELF可以从六个稀疏输入视图重建360度场景，并在合成和现实数据集上取得有竞争力的结果。我们发现sshELF忠实地重建了闭塞区域，支持实时渲染，并为下游应用提供了丰富的潜在特征。代码将被发布。 et.al.|[2502.04318](http://arxiv.org/abs/2502.04318)|null|

<p align=right>(<a href=#updated-on-20250218>back to top</a>)</p>

## Diffusion

|Publish Date|Title|Abstract|PDF|Code|
|---|---|---|---|---|
|**2025-02-14**|**Region-Adaptive Sampling for Diffusion Transformers**|扩散模型（DM）已成为跨不同领域生成任务的主要选择。然而，它们对多个连续正向传递的依赖极大地限制了实时性能。以前的加速方法主要侧重于减少采样步骤的数量或重用中间结果，由于卷积U-Net结构的约束，未能利用图像内空间区域的变化。通过利用扩散变换器（DiT）在处理可变数量的令牌方面的灵活性，我们引入了RAS，这是一种新颖的无训练采样策略，可以根据DiT模型的焦点动态地为图像内的区域分配不同的采样率。我们的关键观察是，在每个采样步骤中，模型都集中在语义上有意义的区域，这些关注区域在连续的步骤中表现出很强的连续性。利用这一见解，RAS仅更新当前聚焦的区域，而其他区域则使用上一步的缓存噪声进行更新。模型的焦点是根据前一步的输出确定的，利用了我们观察到的时间一致性。我们在稳定扩散3和Lumina-Next-T2I上评估了RAS，分别实现了高达2.36倍和2.51倍的加速，发电质量下降幅度最小。此外，一项用户研究表明，RAS在人类评估下提供了可比的质量，同时实现了1.6倍的加速。我们的方法朝着更高效的扩散变压器迈出了重要的一步，增强了它们在实时应用中的潜力。 et.al.|[2502.10389](http://arxiv.org/abs/2502.10389)|null|
|**2025-02-14**|**ReStyle3D: Scene-Level Appearance Transfer with Semantic Correspondences**|我们介绍了ReStyle3D，这是一个新颖的框架，用于将场景级外观从单个样式图像转换为由多个视图表示的真实场景。该方法将显式语义对应与多视图一致性相结合，实现精确连贯的风格化。与全局应用参考样式的传统样式化方法不同，ReStyle3D使用开放式词汇分割在样式和现实世界图像之间建立密集的实例级对应关系。这确保了每个对象都具有语义匹配的纹理。它首先使用扩散模型中的无训练语义注意力机制将样式转移到单个视图。然后，它通过学习扭曲将样式化提升到其他视图，并在单目深度和像素对应的指导下优化网络。实验表明，ReStyle3D在结构保持、感知风格相似性和多视图连贯性方面始终优于现有方法。用户研究进一步验证了它产生逼真、语义忠实的结果的能力。我们的代码、预训练模型和数据集将公开发布，以支持室内设计、虚拟舞台和3D一致性风格化中的新应用。 et.al.|[2502.10377](http://arxiv.org/abs/2502.10377)|null|
|**2025-02-14**|**Dimension-free Score Matching and Time Bootstrapping for Diffusion Models**|扩散模型通过估计不同噪声水平下目标分布的得分函数来生成样本。该模型使用从目标分布中提取的样本进行训练，逐步添加噪声。在这项工作中，我们建立了学习这些分数函数的第一个（几乎）无维样本复杂度界限，实现了维数比先前结果的双指数改进。我们分析的一个关键方面是使用单个函数近似器来联合估计不同噪声水平的分数，这是扩散模型在实践中的一个重要特征，可以跨时间步长进行泛化。我们的分析引入了一种新的基于鞅的误差分解和尖锐的方差界，能够从马尔可夫过程生成的依赖数据中高效学习，这可能是独立感兴趣的。基于这些见解，我们提出了Bootstrapd Score Matching（BSM），这是一种方差降低技术，利用之前学习的分数来提高更高噪声水平下的准确性。这些结果为生成建模的扩散模型的效率和有效性提供了至关重要的见解。 et.al.|[2502.10354](http://arxiv.org/abs/2502.10354)|null|
|**2025-02-14**|**Stretching theory of Hookean metashells**|尽管受到熟悉的虎克力学定律的支配，但具有内部结构的弹性壳（即元壳）表现出丰富的非结构化材料中没有的不寻常的力学性能。在这里，我展示了这种行为的大部分可以通过非均匀Schr的实值模拟来捕捉\“欧定谔方程，内部结构在波函数的作用下经历的侧向压力。在精细结构极限 $-$中，即当与内部结构相关的长度尺度远小于局部曲率半径$-$ 时，这种方法揭示了局部状态的存在，在这种状态下，弹性变形被阻止从原点扩散出去，从而使内部结构能够平滑地适应元壳的内在几何形状。利用与近自由电子中的散射态的类比，我进一步表明，从空间中周期性重复相同结构单元获得的周期性元壳支持弹性布洛赫波，对应于内部结构的静止周期性配置，其特征是几何相关的能带结构。当应用于晶体单层时，这种方法将相互作用拓扑缺陷的弹性理论推广到可压缩系统items。 et.al.|[2502.10345](http://arxiv.org/abs/2502.10345)|null|
|**2025-02-14**|**Bifurcation of global energy minimizers for a diffusion-aggregation model on sphere**|我们考虑在单位球面 $\mathbb{S}^d$上的概率密度上定义的自由能泛函，并研究其全局最小值。能量由两部分组成：熵和非局域相互作用能，分别有利于扩散和聚集行为。我们找到了吸引相互作用大小的阈值，并在每种情况下建立了全局能量最小化。研究了该阈值处的分叉。我们还将结果推广到由任意数量的球体组成的空间（例如，平面环面$\mathbb{S}^1\times\mathbb{S}^ 1$ ）。 et.al.|[2502.10337](http://arxiv.org/abs/2502.10337)|null|
|**2025-02-14**|**DiOpt: Self-supervised Diffusion for Constrained Optimization**|扩散模型的最新进展表明，通过利用其多模态采样能力来逃避局部最优解，基于学习的优化具有巨大的潜力。然而，现有的基于扩散的优化方法通常依赖于监督训练，缺乏一种机制来确保严格的约束满足，而这在现实世界的应用中是经常需要的。由此产生的一个观察结果是分布失准，即生成的解分布通常与可行域有很小的重叠。在本文中，我们提出了DiOpt，这是一种新的扩散范式，通过迭代自训练系统地学习近最优可行解分布。我们的框架引入了几个关键创新：专门设计的目标分布，旨在最大限度地增加与约束解流形的重叠；一种自举自训练机制，根据约束违反的严重程度和最优性差距自适应地对候选解决方案进行加权；以及一个动态内存缓冲区，通过在训练迭代中保留高质量的解来加速收敛。据我们所知，DiOpt代表了自监督扩散与硬约束满足的首次成功集成。对电网控制、运动重定向、无线分配等不同任务的评估表明，它在优化和约束满足方面都具有优势。 et.al.|[2502.10330](http://arxiv.org/abs/2502.10330)|null|
|**2025-02-14**|**Generalised Parallel Tempering: Flexible Replica Exchange via Flows and Diffusions**|并行回火（PT）是一种经典的MCMC算法，旨在利用并行计算通过退火从高维、多峰或其他复杂分布中高效采样。PT标准公式的一个局限性是，对于越来越具有挑战性的分布，生成高质量样本所需的计算资源的增长，这是通过有效样本量或往返率来衡量的。为了解决这个问题，我们提出了一个框架：广义并行回火（GePT），它允许在并行回火中结合现代生成建模的最新进展，如归一化流和扩散模型，同时保持与基于MCMC的方法相同的理论保证。例如，我们表明，这使我们能够以并行的方式利用扩散模型，绕过了生成高质量样本的大量步骤的通常计算成本。此外，我们实证证明，与经典算法相比，GePT可以提高样本质量，减少处理复杂分布所需的计算资源的增长。 et.al.|[2502.10328](http://arxiv.org/abs/2502.10328)|null|
|**2025-02-14**|**Dark Matter Attenuation Effects: Sensitivity Ceilings for Spin-Dependent and Spin-Independent Interactions**|旨在揭示暗物质（DM）难以捉摸性质的直接探测实验在探测DM-核子相互作用的更低横截面方面取得了重大进展。同时，由于DM在地球和大气中的散射，横截面灵敏度区域存在上限，因此永远不会到达探测器。我们研究了这种效应对自旋相关和自旋无关相互作用的影响。与之前假设DM散射为直线路径的研究相比，我们采用了一种半解析扩散模型，该模型考虑了光DM质量普遍存在的潜在大角度偏差的影响。我们发现，对于足够低的能量阈值，这种建模差异会影响DM相互作用横截面的敏感性。本研究在QUEST-DMC实验的背景下评估了影响，该实验利用基于表面的探测器和超流体氦-3测辐射热计来寻找利用低能量阈值的亚GeV DM。当质量低于1 GeV $/c^2$时，两个框架之间的偏差变得明显。使用扩散框架，QUEST-DMC在自旋相关DM中子横截面上的上限灵敏度极限为10^{-24}$cm$^2$的3倍，与直线路径DM散射近似加倍。同样，对于自旋无关DM核子横截面，在扩散框架下的上限极限为10^{-27}$cm$的7.5倍，在0.025-5GeV$/c^2$ 质量范围内，与直线轨迹近似也增加了约两倍。 et.al.|[2502.10251](http://arxiv.org/abs/2502.10251)|null|
|**2025-02-14**|**Step-Video-T2V Technical Report: The Practice, Challenges, and Future of Video Foundation Model**|我们介绍了Step-Video-T2V，这是一种最先进的文本到视频预训练模型，具有30B参数，能够生成长达204帧的视频。深度压缩变分自编码器Video VAE专为视频生成任务而设计，可实现16x16的空间和8倍的时间压缩比，同时保持出色的视频重建质量。用户提示使用两个双语文本编码器进行编码，以处理英语和中文。使用流匹配训练具有3D全注意力的DiT，并将其用于将输入噪声去噪到潜在帧中。应用基于视频的DPO方法video DPO来减少伪影并提高生成视频的视觉质量。我们还详细介绍了我们的培训策略，并分享了关键的观察结果和见解。Step-Video-T2V的性能在一个新的视频生成基准Step-Video-T2V-Eval上进行了评估，与开源和商业引擎相比，展示了其最先进的文本到视频质量。此外，我们讨论了当前基于扩散的模型范式的局限性，并概述了视频基础模型的未来方向。我们提供Step-Video-T2V和Step-Video-T2V-Eval，网址为https://github.com/stepfun-ai/Step-Video-T2V.在线版本可以从以下网址访问https://yuewen.cn/videos也。我们的目标是加速视频基础模型的创新，并赋予视频内容创作者权力。 et.al.|[2502.10248](http://arxiv.org/abs/2502.10248)|null|
|**2025-02-14**|**Shaping Inductive Bias in Diffusion Models through Frequency-Based Noise Control**|扩散概率模型（DPMs）是一种强大的生成模型，在许多生成任务中取得了无与伦比的成功。在这项工作中，我们的目标是在扩散模型的训练和采样中建立归纳偏差，以更好地适应模型数据的目标分布。对于拓扑结构的数据，我们设计了一种基于频率的噪声算子，有目的地操纵和设置这些归纳偏差。我们首先证明，对噪声正向过程的适当操作可以使DPM专注于分布的特定方面进行学习。我们表明，不同的数据集需要不同的归纳偏差，与标准扩散相比，适当的基于频率的噪声控制可以提高生成性能。最后，我们证明了在学习时忽略特定频率信息的可能性。我们在图像损坏和恢复任务中展示了这一点，在该任务中，我们训练DPM在严重噪声损坏后恢复原始目标分布。 et.al.|[2502.10236](http://arxiv.org/abs/2502.10236)|null|

<p align=right>(<a href=#updated-on-20250218>back to top</a>)</p>

## NeRF

|Publish Date|Title|Abstract|PDF|Code|
|---|---|---|---|---|
|**2025-02-05**|**Poisson Hypothesis and large-population limit for networks of spiking neurons**|我们研究了具有随机尖峰时间的线性（泄漏）和二次积分和放电神经元的空间扩展网络的平均场描述。我们考虑了具有线性和二次内在动力学的连续时间Galves-L“ocherbach（GL）网络的大种群极限。我们证明了泊松假设适用于这些网络的复制平均场极限，即在适当定义的极限内，神经元是独立的，相互作用时间被强度取决于平均放电率的独立时间非均匀泊松过程所取代，将已知结果扩展到具有二次内在动态和重置的网络。证明泊松假设成立为研究这些网络中的大种群限值开辟了可能性。我们证明这个极限是一个适定的神经场模型，受随机重置的影响。 et.al.|[2502.03379](http://arxiv.org/abs/2502.03379)|null|
|**2025-02-04**|**Geometric Neural Process Fields**|本文解决了神经场（NeF）泛化的挑战，其中模型必须有效地适应仅给出少量观测值的新信号。为了解决这个问题，我们提出了几何神经过程场（G-NPF），这是一个明确捕捉不确定性的神经辐射场的概率框架。我们将NeF泛化表述为概率问题，从而能够从有限的上下文观测中直接推断出NeF函数分布。为了引入结构归纳偏差，我们引入了一组几何基来编码空间结构，并促进NeF函数分布的推断。在此基础上，我们设计了一个分层潜在变量模型，使G-NPF能够整合多个空间层次的结构信息，并有效地参数化INR函数。这种分层方法提高了对新场景和未知信号的泛化能力。针对3D场景的新颖视图合成以及2D图像和1D信号回归的实验证明了我们的方法在捕捉不确定性和利用结构信息提高泛化能力方面的有效性。 et.al.|[2502.02338](http://arxiv.org/abs/2502.02338)|null|
|**2025-02-05**|**A Poisson Process AutoDecoder for X-ray Sources**|钱德拉X射线天文台和eROSITA等X射线观测设施已经探测到数百万个与高能现象相关的天文源。光子的到达作为时间的函数遵循泊松过程，并且可以按数量级变化，这为源分类、物理性质推导和异常检测等常见任务带来了障碍。之前的工作要么未能直接捕捉数据的泊松性质，要么只关注泊松率函数重建。在这项工作中，我们提出了泊松过程自动解码器（PPAD）。PPAD是一种神经场解码器，通过无监督学习将固定长度的潜在特征映射到跨能带和时间的连续泊松率函数。PPAD重建速率函数并同时产生表示。我们使用钱德拉源目录通过重建、回归、分类和异常检测实验证明了PPAD的有效性。 et.al.|[2502.01627](http://arxiv.org/abs/2502.01627)|null|
|**2025-02-03**|**Regularized interpolation in 4D neural fields enables optimization of 3D printed geometries**|精确生产具有特定特性的几何形状的能力可能是制造过程中最重要的特征。3D打印具有非凡的设计自由度和复杂性，但也容易出现几何和其他缺陷，必须解决这些缺陷才能充分发挥其潜力。最终，这将需要精明的设计决策和及时的参数调整来保持稳定性，即使是专业的人类操作员也很难做到这一点。虽然机器学习在3D打印中得到了广泛的研究，但现有的方法通常会忽略不同打印的空间特征，因此很难产生所需的几何形状。在这里，我们将打印部件的体积表示编码到神经场中，并应用一种新的正则化策略，该策略基于最小化场输出相对于单个不可学习参数的偏导数。因此，通过鼓励小的输入变化只产生小的输出变化，我们鼓励在观测体积之间进行平滑插值，从而实现现实的几何预测。因此，该框架允许提取“想象的”3D形状，揭示了在以前看不见的参数下制造的零件的外观。由此产生的连续场用于数据驱动优化，以最大限度地提高预期和生产几何形状之间的几何保真度，减少后处理、材料浪费和生产成本。通过动态优化工艺参数，我们的方法实现了先进的规划策略，有可能使制造商更好地实现复杂和功能丰富的设计。 et.al.|[2502.01517](http://arxiv.org/abs/2502.01517)|**[link](https://github.com/cam-cambridge/4d-neural-fields-optimise-3d-printing)**|
|**2025-02-03**|**Modelling change in neural dynamics during phonetic accommodation**|短期语音调节是口音变化背后的基本驱动力，但来自另一个说话者声音的实时输入是如何塑造对话者的语音规划表示的？我们基于运动规划和记忆动力学的动态神经场方程，提出了一种语音调节过程中语音表征变化的计算模型。我们测试了该模型从实验研究中捕捉经验模式的能力，在实验研究中，说话者用与自己不同的口音跟踪模型说话者。实验数据显示了阴影期间元音特定的收敛程度，随后在阴影后恢复到基线（或轻微发散）。该模型可以通过调节抑制性记忆动力学的大小来再现这些现象，这可能反映了由于语音和/或社会语言压力导致的对调节的抵抗。我们讨论了这些结果对短期语音调节和长期声音变化模式之间关系的影响。 et.al.|[2502.01210](http://arxiv.org/abs/2502.01210)|null|
|**2025-02-02**|**Lifting the Winding Number: Precise Representation of Complex Cuts in Subspace Physics Simulations**|切割薄壁可变形结构在日常生活中很常见，但由于引入了空间不连续性，给模拟带来了重大挑战。传统方法依赖于基于网格的域表示，这需要频繁的重新网格划分和细化，以准确捕捉不断变化的不连续性。这些挑战在缩减空间模拟中进一步加剧，在这种模拟中，基函数固有地依赖于几何和网格，使得基难以甚至不可能表示切割引入的各种不连续性。用神经场表示基函数的最新进展提供了一种有前景的替代方案，利用其离散化不可知的性质来表示不同几何形状的变形。然而，神经场的固有连续性阻碍了泛化，特别是在神经网络权重中编码了不连续性的情况下。我们提出了Wind-Lifter，这是一种新的神经表示，旨在精确模拟薄壁可变形结构中的复杂切割。我们的方法构建神经场，在指定位置精确再现不连续性，而无需在切割线的位置烘烤。至关重要的是，我们的方法没有将不连续性嵌入神经网络的权重中，为切割位置的泛化开辟了道路。我们的方法实现了实时仿真速度，并支持在仿真过程中动态更新切割线几何形状。此外，不连续性的显式表示使我们的神经场易于控制和编辑，与传统的神经场相比具有显著的优势，在传统的神经场内，不连续被嵌入网络的权重中，并支持依赖于一般切割位置的新应用。 et.al.|[2502.00626](http://arxiv.org/abs/2502.00626)|null|
|**2025-01-31**|**Lifting by Gaussians: A Simple, Fast and Flexible Method for 3D Instance Segmentation**|我们介绍了一种新的三维高斯散斑辐射场（3DGS）开放世界实例分割方法——高斯提升（LBG）。最近，3DGS场已经成为基于神经场的高质量新视图合成方法的高效和明确的替代方案。我们的3D实例分割方法直接从SAM（或FastSAM等）中提取2D分割掩模，以及CLIP和DINOv2的特征，直接将它们融合到3DGS（或类似的高斯辐射场，如2DGS）上。与以前的方法不同，LBG不需要每个场景的训练，使其能够在任何现有的3DGS重建上无缝运行。我们的方法不仅比现有方法快一个数量级，而且更简单；它也是高度模块化的，能够对现有的3DGS字段进行3D语义分割，而不需要对3D高斯进行特定的参数化。此外，我们的技术在保持灵活性和效率的同时，为2D语义新颖视图合成和3D资产提取结果实现了卓越的语义分割。我们进一步介绍了一种从3D辐射场分割方法中评估单独分割的3D资产的新方法。 et.al.|[2502.00173](http://arxiv.org/abs/2502.00173)|null|
|**2025-01-30**|**Zero-Shot Novel View and Depth Synthesis with Multi-View Geometric Diffusion**|从稀疏姿态图像重建3D场景的当前方法采用中间3D表示，如神经场、体素网格或3D高斯，以实现多视图一致的场景外观和几何形状。本文介绍了MVGD，这是一种基于扩散的架构，能够在给定任意数量的输入视图的情况下，从新的视点直接生成像素级的图像和深度图。我们的方法使用光线图调节来增强来自不同视点的空间信息的视觉特征，并指导从新视图生成图像和深度图。我们方法的一个关键方面是图像和深度图的多任务生成，使用可学习的任务嵌入来指导向特定模态的扩散过程。我们从公开可用的数据集中收集了6000多万个多视图样本来训练这个模型，并提出了在这种不同条件下实现高效和一致学习的技术。我们还提出了一种新策略，通过逐步微调较小的模型，实现了对较大模型的有效训练，并具有很好的扩展行为。通过广泛的实验，我们报告了多个新颖的视图合成基准以及多视图立体和视频深度估计的最新结果。 et.al.|[2501.18804](http://arxiv.org/abs/2501.18804)|null|
|**2025-01-22**|**Retrieval-Augmented Neural Field for HRTF Upsampling and Personalization**|具有密集空间网格的头部相关传递函数（HRTF）是沉浸式双耳音频生成的理想选择，但它们的记录很耗时。尽管HRTF空间上采样在神经场方面取得了显著进展，但仅从几个测量方向（例如3或5个测量方向）进行空间上采样仍然具有挑战性。为了解决这个问题，我们提出了一种检索增强神经场（RANF）。RANF从数据集中检索HRTF接近目标受试者HRTF的受试者。除了声源方向本身之外，检索到的对象在所需方向上的HRTF也被馈送到神经场中。此外，我们提出了一种神经网络，它可以有效地处理多个检索到的主题，灵感来自一种称为变换平均连接的多通道处理技术。我们的实验证实了RANF在SONICOM数据集上的优势，它是2024年听众声学个性化挑战任务2获胜解决方案的关键组成部分。 et.al.|[2501.13017](http://arxiv.org/abs/2501.13017)|**[link](https://github.com/merlresearch/ranf-hrtf)**|
|**2025-01-15**|**CityDreamer4D: Compositional Generative Model of Unbounded 4D Cities**|近年来，3D场景生成引起了越来越多的关注，并取得了重大进展。生成4D城市比3D场景更具挑战性，因为存在结构复杂、视觉多样的物体，如建筑物和车辆，并且人类对城市环境中的扭曲更加敏感。为了解决这些问题，我们提出了CityDreamer4D，这是一个专门为生成无界4D城市而定制的组合生成模型。我们的主要见解是1）4D城市生成应该将动态对象（如车辆）与静态场景（如建筑物和道路）分开，2）4D场景中的所有对象都应该由建筑物、车辆和背景材料的不同类型的神经场组成。具体来说，我们提出了交通场景生成器和无边界布局生成器，使用高度紧凑的BEV表示生成动态交通场景和静态城市布局。4D城市中的对象是通过结合面向对象和面向实例的神经场来生成的，用于背景材料、建筑物和车辆。为了适应背景材料和实例的不同特征，神经场采用定制的生成哈希网格和周期性位置嵌入作为场景参数化。此外，我们还为城市生成提供了一套全面的数据集，包括OSM、GoogleEarth和CityTopia。OSM数据集提供了各种真实世界的城市布局，而谷歌地球和CityTopia数据集则提供了大规模、高质量的城市图像，并附有3D实例注释。利用其组合设计，CityDreamer4D支持一系列下游应用程序，如实例编辑、城市风格化和城市模拟，同时在生成逼真的4D城市方面提供最先进的性能。 et.al.|[2501.08983](http://arxiv.org/abs/2501.08983)|**[link](https://github.com/hzxie/CityDreamer4D)**|

<p align=right>(<a href=#updated-on-20250218>back to top</a>)</p>

[contributors-shield]: https://img.shields.io/github/contributors/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[contributors-url]: https://github.com/Vincentqyw/cv-arxiv-daily/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[forks-url]: https://github.com/Vincentqyw/cv-arxiv-daily/network/members
[stars-shield]: https://img.shields.io/github/stars/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[stars-url]: https://github.com/Vincentqyw/cv-arxiv-daily/stargazers
[issues-shield]: https://img.shields.io/github/issues/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[issues-url]: https://github.com/Vincentqyw/cv-arxiv-daily/issues

