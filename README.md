[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]

## Updated on 2025.02.13
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
|**2025-02-12**|**CineMaster: A 3D-Aware and Controllable Framework for Cinematic Text-to-Video Generation**|在这项工作中，我们提出了CineMaster，这是一个用于3D感知和可控文本到视频生成的新框架。我们的目标是为用户提供与专业电影导演相当的可控性：在场景中精确放置物体，在3D空间中灵活操纵物体和相机，以及对渲染帧的直观布局控制。为了实现这一目标，CineMaster分两个阶段运行。在第一阶段，我们设计了一个交互式工作流程，允许用户通过定位对象边界框和定义3D空间内的相机运动来直观地构建3D感知条件信号。在第二阶段，这些控制信号——包括渲染的深度图、相机轨迹和对象类标签——作为文本到视频扩散模型的指导，确保生成用户期望的视频内容。此外，为了克服具有3D对象运动和相机姿态注释的野外数据集的稀缺性，我们仔细建立了一个自动数据注释管道，从大规模视频数据中提取3D边界框和相机轨迹。大量的定性和定量实验表明，CineMaster明显优于现有方法，并实现了出色的3D感知文本到视频生成。项目页面：https://cinemaster-dev.github.io/. et.al.|[2502.08639](http://arxiv.org/abs/2502.08639)|null|
|**2025-02-12**|**FloVD: Optical Flow Meets Video Diffusion Model for Enhanced Camera-Controlled Video Synthesis**|本文介绍了FloVD，这是一种基于光流的新型视频扩散模型，用于相机可控视频生成。FloVD利用光流图来表示相机和运动物体的运动。这种方法有两个关键好处。由于光流可以直接从视频中估计出来，因此我们的方法允许在没有地面实况相机参数的情况下使用任意训练视频。此外，由于背景光流编码了不同视点之间的3D相关性，我们的方法通过利用背景运动实现了详细的相机控制。为了在支持详细相机控制的同时合成自然物体运动，我们的框架采用了一个由光流生成和流调节视频合成组成的两级视频合成流水线。大量实验表明，在精确的相机控制和自然物体运动合成方面，我们的方法比以前的方法具有优越性。 et.al.|[2502.08244](http://arxiv.org/abs/2502.08244)|null|
|**2025-02-12**|**Learning Human Skill Generators at Key-Step Levels**|我们致力于在关键步骤层面学习人类技能生成器。技能的生成是一项具有挑战性的工作，但它的成功实施可以极大地促进人类的技能学习，并为具身智能提供更多的经验。尽管当前的视频生成模型可以合成简单和原子的人类操作，但由于其复杂的过程，它们在人类技能方面存在困难。人类技能涉及多步骤、长时间的动作和复杂的场景转换，因此现有的合成长视频的朴素自回归方法无法生成人类技能。为了解决这个问题，我们提出了一项新任务，即关键步骤技能生成（KS Gen），旨在降低生成人类技能视频的复杂性。给定初始状态和技能描述，任务是生成完成技能的关键步骤的视频片段，而不是全长视频。为了支持这项任务，我们引入了一个精心策划的数据集，并定义了多个评估指标来评估绩效。考虑到KS Gen的复杂性，我们为这项任务提出了一个新的框架。首先，多模态大型语言模型（MLLM）使用检索参数生成关键步骤的描述。随后，我们使用关键步骤图像生成器（KIG）来解决技能视频中关键步骤之间的不连续性。最后，视频生成模型使用这些描述和关键步骤图像来生成具有高时间一致性的关键步骤的视频片段。我们对结果进行了详细分析，希望为人类技能生成提供更多见解。所有模型和数据均可在https://github.com/MCG-NJU/KS-Gen. et.al.|[2502.08234](http://arxiv.org/abs/2502.08234)|null|
|**2025-02-12**|**AnyCharV: Bootstrap Controllable Character Video Generation with Fine-to-Coarse Guidance**|角色视频生成是一个重要的现实世界应用程序，专注于制作具有特定角色的高质量视频。最近的进步引入了各种控制信号来制作静态角色的动画，成功地增强了对生成过程的控制。然而，这些方法往往缺乏灵活性，限制了它们的适用性，并使用户难以将源角色合成到所需的目标场景中。为了解决这个问题，我们提出了一种新的框架AnyCharV，该框架在姿态信息的指导下，使用任意源角色和目标场景灵活生成角色视频。我们的方法包括两个阶段的训练过程。在第一阶段，我们开发了一个基础模型，该模型能够使用姿态引导将源角色与目标场景集成在一起。第二阶段通过自增强机制进一步引导可控生成，我们使用第一阶段生成的视频，用粗掩模替换精细掩模，从而更好地保留角色细节，实现训练结果。实验结果证明了我们提出的方法的有效性和鲁棒性。我们的项目页面是https://anycharv.github.io. et.al.|[2502.08189](http://arxiv.org/abs/2502.08189)|null|
|**2025-02-12**|**Next Block Prediction: Video Generation via Semi-Autoregressive Modeling**|Next Token Prediction（NTP）是自回归（AR）视频生成的一种事实上的方法，但它存在次优单向依赖性和推理速度慢的问题。在这项工作中，我们提出了一种用于视频生成的半自回归（半AR）框架，称为下一块预测（NBP）。通过将视频内容统一分解为大小相等的块（例如，行或帧），我们将生成单元从单个令牌转移到块，允许当前块中的每个令牌同时预测下一个块中的相应令牌。与传统的AR建模不同，我们的框架在每个块内采用双向注意力，使令牌能够捕获更强大的空间依赖关系。通过并行预测多个令牌，NBP模型显著减少了生成步骤的数量，从而实现了更快、更高效的推理。我们的模型在UCF101上获得了103.3的FVD分数，在K600上获得了25.5的FVD评分，平均比vanilla NTP模型高出4.4。此外，由于推理步骤的减少，NBP模型每秒生成8.89帧（128x128分辨率），实现了11倍的加速。我们还探索了从700M到3B参数的模型尺度，观察到发电质量的显著提高，UCF101的FVD得分从103.3下降到55.3，K600的FVD分数从25.5下降到19.5，这证明了我们方法的可扩展性。 et.al.|[2502.07737](http://arxiv.org/abs/2502.07737)|null|
|**2025-02-11**|**Magic 1-For-1: Generating One Minute Video Clips within One Minute**|在本技术报告中，我们介绍了Magic 1-For-1（Magic141），这是一种高效的视频生成模型，具有优化的内存消耗和推理延迟。关键思想很简单：将文本到视频生成任务分解为两个单独的更容易的扩散步骤蒸馏任务，即文本到图像生成和图像到视频生成。我们验证了使用相同的优化算法，图像到视频任务确实比文本到视频任务更容易收敛。我们还从三个方面探索了一系列优化技巧，以降低训练图像到视频（I2V）模型的计算成本：1）通过使用多模态先验条件注入来加速模型收敛；2） 通过应用对抗性步骤蒸馏来加速推理延迟，以及3）通过参数稀疏化进行推理内存成本优化。通过这些技术，我们能够在3秒内生成5秒的视频片段。通过应用测试时间滑动窗口，我们能够在一分钟内生成一分钟长的视频，显著提高了视觉质量和运动动态，平均生成1秒视频片段的时间不到1秒。我们进行了一系列初步探索，以找出扩散阶跃蒸馏过程中计算成本和视频质量之间的最佳权衡，并希望这能成为开源探索的良好基础模型。代码和模型权重可在以下网址获得https://github.com/DA-Group-PKU/Magic-1-For-1. et.al.|[2502.07701](http://arxiv.org/abs/2502.07701)|**[link](https://github.com/da-group-pku/magic-1-for-1)**|
|**2025-02-12**|**VidCRAFT3: Camera, Object, and Lighting Control for Image-to-Video Generation**|最近的图像到视频生成方法在实现对一个或两个视觉元素（如相机轨迹或物体运动）的控制方面取得了成功。然而，由于数据和网络效率的限制，这些方法无法提供对多个视觉元素的控制。在本文中，我们介绍了VidCRAFT3，这是一种用于精确图像到视频生成的新框架，可以同时控制相机运动、物体运动和照明方向。为了更好地解耦对每个视觉元素的控制，我们提出了空间三重注意力转换器，它以对称的方式集成了照明方向、文本和图像。由于大多数真实世界的视频数据集缺乏照明注释，我们构建了一个高质量的合成视频数据集，即VideoLightingDirection（VLD）数据集。该数据集包括照明方向注释和不同外观的对象，使VidCRAFT3能够有效地处理强光透射和反射效果。此外，我们提出了一种三阶段训练策略，该策略消除了同时使用多个视觉元素（相机运动、物体运动和照明方向）注释训练数据的需要。对基准数据集的广泛实验证明了VidCRAFT3在制作高质量视频内容方面的功效，在控制粒度和视觉连贯性方面超越了现有的最先进方法。所有代码和数据都将公开。 et.al.|[2502.07531](http://arxiv.org/abs/2502.07531)|null|
|**2025-02-11**|**Enhance-A-Video: Better Generated Video for Free**|基于DiT的视频生成已经取得了显著成果，但对增强现有模型的研究仍然相对未被探索。在这项工作中，我们引入了一种名为enhance-a-Video的无训练方法，以提高基于DiT生成的视频的连贯性和质量。核心思想是基于非对角时间注意力分布增强跨帧相关性。由于其简单的设计，我们的方法可以很容易地应用于大多数基于DiT的视频生成框架，而无需任何重新训练或微调。在各种基于DiT的视频生成模型中，我们的方法在时间一致性和视觉质量方面都有很好的改进。我们希望这项研究能够激发未来在视频生成增强方面的探索。 et.al.|[2502.07508](http://arxiv.org/abs/2502.07508)|null|
|**2025-02-11**|**Generative Ghost: Investigating Ranking Bias Hidden in AI-Generated Videos**|随着人工智能生成内容（AIGC）的快速发展，创建高质量的人工智能生成视频变得更快、更容易，导致互联网上充斥着各种视频内容。然而，这些视频对内容生态系统的影响在很大程度上仍未得到探索。视频信息检索仍然是访问视频内容的基本方法。基于检索模型在ad-hoc和图像检索任务中通常倾向于AI生成内容的观察，我们研究了在具有挑战性的视频检索环境中是否会出现类似的偏差，其中时间和视觉因素可能会进一步影响模型行为。为了探索这一点，我们首先构建了一个全面的基准数据集，其中包含真实和人工智能生成的视频，以及一组公平和严格的指标来评估偏见。该基准测试由两个最先进的开源视频生成模型生成的13000个视频组成。我们精心设计了一套严格的指标来准确衡量这种偏好，考虑了AIGC视频的有限帧率和次优质量带来的潜在偏差。然后，我们应用了三种现成的视频检索模型来对这个混合数据集执行检索任务。我们的研究结果表明，在检索中明显倾向于使用人工智能生成的视频。进一步的调查表明，将人工智能生成的视频纳入检索模型的训练集中会加剧这种偏见。与图像模态中观察到的偏好不同，我们发现视频检索偏差来自看不见的视觉和时间信息，这使得视频偏差的根本原因是这两个因素的复杂相互作用。为了减轻这种偏见，我们使用对比学习方法对检索模型进行微调。这项研究的结果突显了人工智能生成的视频对检索系统的潜在影响。 et.al.|[2502.07327](http://arxiv.org/abs/2502.07327)|null|
|**2025-02-11**|**Articulate That Object Part (ATOP): 3D Part Articulation from Text and Motion Personalization**|我们提出了ATOP（Articulate That Object Part），这是一种基于运动个性化的新方法，可以根据文本提示中的规定，将3D对象与零件及其运动联系起来。具体来说，文本输入使我们能够利用现代视频扩散的力量，为正确的对象类别和部分生成合理的运动样本。反过来，输入的3D对象提供图像提示，将生成的视频个性化到我们想要表达的对象。我们的方法首先对特定类别的运动生成进行一些镜头微调，这是弥补当前视频扩散模型缺乏清晰度意识的关键第一步。为此，我们使用为目标对象类别获得的少量视频样本来微调预训练的多视图图像生成模型，以实现可控的多视图视频生成。随后是通过目标3D对象的多视图渲染图像实现的运动视频个性化。最后，我们通过可微渲染将个性化视频运动传递给目标3D对象，通过分数蒸馏采样损失优化部分运动参数。我们证明，与先前的工作相比，我们的方法能够生成逼真的运动视频，并以更准确和更通用的方式预测3D运动参数。 et.al.|[2502.07278](http://arxiv.org/abs/2502.07278)|null|

<p align=right>(<a href=#updated-on-20250213>back to top</a>)</p>

## 3D

|Publish Date|Title|Abstract|PDF|Code|
|---|---|---|---|---|
|**2025-02-11**|**Matrix3D: Large Photogrammetry Model All-in-One**|我们提出了Matrix3D，这是一个统一的模型，可以执行多个摄影测量子任务，包括姿态估计、深度预测和使用相同模型的新颖视图合成。Matrix3D利用多模态扩散变换器（DiT）来整合多种模态的变换，如图像、相机参数和深度图。Matrix3D大规模多模式训练的关键在于结合掩码学习策略。这使得即使有部分完整的数据，如图像姿态和图像深度对的双模态数据，也能进行全模态模型训练，从而显著增加了可用的训练数据池。Matrix3D在姿态估计和新颖的视图合成任务中展示了最先进的性能。此外，它通过多轮交互提供精细控制，使其成为3D内容创建的创新工具。项目页面：https://nju-3dv.github.io/projects/matrix3d. et.al.|[2502.07685](http://arxiv.org/abs/2502.07685)|null|
|**2025-02-11**|**Flow Distillation Sampling: Regularizing 3D Gaussians with Pre-trained Matching Priors**|3D高斯散斑（3DGS）以快速的训练和渲染速度实现了出色的渲染质量。然而，其优化过程缺乏明确的几何约束，导致在稀疏或没有观测输入视图的区域进行次优几何重建。在这项工作中，我们试图通过在3DGS优化过程之前加入预训练的匹配来缓解这个问题。我们介绍了流动蒸馏采样（FDS），这是一种利用预先训练的几何知识来提高高斯辐射场准确性的技术。我们的方法采用了一种策略性采样技术，以输入视图附近的未观测视图为目标，利用匹配模型（先验流）计算的光流来引导根据3DGS几何（辐射流）分析计算的流。深度渲染、网格重建和新颖视图合成方面的综合实验展示了FDS相对于最先进方法的显著优势。此外，我们的解释性实验和分析旨在阐明FDS对几何精度和渲染质量的影响，从而为读者提供对其性能的见解。项目页面：https://nju-3dv.github.io/projects/fds et.al.|[2502.07615](http://arxiv.org/abs/2502.07615)|null|
|**2025-02-10**|**GAS: Generative Avatar Synthesis from a Single Image**|我们引入了一个通用和统一的框架，从单个图像中合成视图一致和时间连贯的化身，解决了单个图像化身生成的挑战性问题。虽然最近的方法采用了基于人类模板（如深度或法线图）的扩散模型，但由于稀疏驾驶信号与实际人类受试者之间的差异，它们往往难以保留外观信息，从而导致多视图和时间不一致。我们的方法通过将基于回归的3D人体重建的重建能力与扩散模型的生成能力相结合，弥合了这一差距。来自初始重建人体的密集驱动信号提供了全面的调节，确保了忠实于参考外观和结构的高质量合成。此外，我们提出了一个统一的框架，使从野生视频中的新颖姿态合成中学到的泛化能力能够自然地转移到新颖的视图合成中。我们的基于视频的扩散模型通过高质量的视图一致性渲染来增强解纠缠合成，以获得新颖的视图和新颖姿势动画中逼真的非刚性变形。结果表明，我们的方法在野生数据集中具有跨域和跨域的优越泛化能力。项目页面：https://humansensinglab.github.io/GAS/ et.al.|[2502.06957](http://arxiv.org/abs/2502.06957)|null|
|**2025-02-10**|**SIREN: Semantic, Initialization-Free Registration of Multi-Robot Gaussian Splatting Maps**|我们提出了SIREN用于多机器人高斯散点（GSplat）地图的注册，对相机姿态、图像和用于初始化或融合局部子地图的地图间变换零访问。为了实现这些功能，SIREN以三种关键方式利用语义的通用性和鲁棒性，为多机器人GSplat地图推导出严格的配准流水线。首先，SIREN利用语义来识别局部图中特征丰富的区域，在这些区域中更好地提出了配准问题，从而消除了先前工作中通常需要的任何初始化。其次，SIREN使用鲁棒的语义特征来识别局部地图中高斯之间的候选对应关系，为鲁棒的几何优化奠定了基础，粗略地对齐了从局部地图中提取的3D高斯基元。第三，这一关键步骤使子图之间的变换能够进行后续的光度细化，其中SIREN利用GSplat图中的新颖视图合成以及基于语义的图像滤波器来计算高精度的非刚性变换，以生成高保真融合图。我们在一系列真实世界的数据集中，特别是在最广泛使用的机器人硬件平台上，包括机械手、无人机和四足动物，展示了SIREN与竞争基线相比的卓越性能。在我们的实验中，SIREN在最具挑战性的场景中实现了约90倍的较小旋转误差、300倍的较小平移误差和44倍的较小尺度误差，在这些场景中，竞争方法很难解决。在审查过程结束后，我们将发布代码并提供项目页面的链接。 et.al.|[2502.06519](http://arxiv.org/abs/2502.06519)|null|
|**2025-02-05**|**VistaFlow: Photorealistic Volumetric Reconstruction with Dynamic Resolution Management via Q-Learning**|我们介绍VistaFlow，这是一种可扩展的三维成像技术，能够从一组二维照片中重建完全交互式的三维体积图像。我们的模型通过一个可微分的渲染系统来合成新的视点，该系统能够对逼真的3D场景进行动态分辨率管理。我们通过引入QuiQ来实现这一目标，QuiQ是一种通过Q学习训练的新型中间视频控制器，通过以毫秒精度调整渲染分辨率来保持一致的高帧率。值得注意的是，VistaFlow在集成CPU图形上本地运行，使其适用于移动和入门级设备，同时仍能提供高性能渲染。VistaFlow绕过神经辐射场（NeRF），使用PlenOctree数据结构以最低的硬件要求渲染复杂的光相互作用，如反射和次表面散射。我们的模型能够在消费类硬件上以每秒100帧以上的1080p分辨率进行新颖的视图合成，从而超越最先进的方法。通过根据每个设备的功能定制渲染质量，VistaFlow有可能提高从高端工作站到廉价微控制器等各种硬件的真实感3D场景渲染的效率和可访问性。 et.al.|[2502.05222](http://arxiv.org/abs/2502.05222)|null|
|**2025-02-11**|**PoI: Pixel of Interest for Novel View Synthesis Assisted Scene Coordinate Regression**|通过新的视图合成技术，如NeRF和高斯散斑，可以增强估计相机姿态的任务，以增加训练数据的多样性和扩展性。然而，这些技术通常会产生模糊和重影等问题的渲染图像，从而影响其可靠性。对于在像素级别估计3D坐标的场景坐标回归（SCR）方法来说，这些问题变得尤为明显。为了缓解与不可靠渲染图像相关的问题，我们引入了一种新的滤波方法，该方法选择性地提取渲染良好的像素，同时丢弃较差的像素。该滤波器在训练过程中同时测量SCR模型的实时重投影损失和梯度。基于这种滤波技术，我们还开发了一种新的策略，利用稀疏输入改进场景坐标回归，并借鉴了稀疏输入技术在新颖视图合成中的成功应用。我们的实验结果验证了我们方法的有效性，在室内和室外数据集上展示了最先进的性能。 et.al.|[2502.04843](http://arxiv.org/abs/2502.04843)|null|
|**2025-02-05**|**Controllable Satellite-to-Street-View Synthesis with Precise Pose Alignment and Zero-Shot Environmental Control**|从卫星图像生成街景图像是一项具有挑战性的任务，特别是在保持精确的姿态对齐和结合不同的环境条件方面。虽然扩散模型在生成任务中显示出了希望，但它们在整个扩散过程中保持严格姿态对齐的能力是有限的。本文提出了一种新的迭代单应性调整（IHA）方案，应用于去噪过程中，有效地解决了姿态失准问题，并确保了生成的街景图像的空间一致性。此外，目前，用于卫星到街道视图生成的可用数据集在光照和天气条件的多样性方面受到限制，从而限制了生成输出的通用性。为了缓解这种情况，我们引入了一种文本引导的照明和天气控制的采样策略，可以对环境因素进行精细控制。大量的定量和定性评估表明，我们的方法显著提高了姿态精度，增强了生成的街景图像的多样性和真实性，为卫星到街景生成任务设定了新的基准。 et.al.|[2502.03498](http://arxiv.org/abs/2502.03498)|null|
|**2025-02-04**|**Geometric Neural Process Fields**|本文解决了神经场（NeF）泛化的挑战，其中模型必须有效地适应仅给出少量观测值的新信号。为了解决这个问题，我们提出了几何神经过程场（G-NPF），这是一个明确捕捉不确定性的神经辐射场的概率框架。我们将NeF泛化表述为概率问题，从而能够从有限的上下文观测中直接推断出NeF函数分布。为了引入结构归纳偏差，我们引入了一组几何基来编码空间结构，并促进NeF函数分布的推断。在此基础上，我们设计了一个分层潜在变量模型，使G-NPF能够整合多个空间层次的结构信息，并有效地参数化INR函数。这种分层方法提高了对新场景和未知信号的泛化能力。针对3D场景的新颖视图合成以及2D图像和1D信号回归的实验证明了我们的方法在捕捉不确定性和利用结构信息提高泛化能力方面的有效性。 et.al.|[2502.02338](http://arxiv.org/abs/2502.02338)|null|
|**2025-02-05**|**GP-GS: Gaussian Processes for Enhanced Gaussian Splatting**|3D高斯散斑已经成为一种高效的真实感新型视图合成方法。然而，它对稀疏运动结构（SfM）点云的依赖一直会损害场景重建的质量。为了解决这些局限性，本文提出了一种新的3D重建框架高斯过程高斯散斑（GP-GS），其中开发了一个多输出高斯过程模型，以实现稀疏SfM点云的自适应和不确定性引导的致密化。具体来说，我们提出了一种动态采样和滤波流水线，通过利用基于GP的预测从输入的2D像素和深度图中推断出新的候选点，自适应地扩展SfM点云。该管道利用不确定性估计来指导高方差预测的修剪，确保几何一致性，并能够生成密集的点云。加密的点云提供了高质量的初始3D高斯分布，以提高重建性能。在各种规模的合成和真实世界数据集上进行的广泛实验验证了所提出框架的有效性和实用性。 et.al.|[2502.02283](http://arxiv.org/abs/2502.02283)|null|
|**2025-02-03**|**WonderHuman: Hallucinating Unseen Parts in Dynamic 3D Human Reconstruction**|在这篇论文中，我们提出了WonderHuman来从单目视频中重建动态的人类化身，以实现高保真的新颖视图合成。以前的动态人体化身重建方法通常要求输入视频完全覆盖观察到的人体。然而，在日常实践中，人们通常可以访问有限的视点，例如单眼正视视频，这使得以前的方法重建人类化身的看不见的部分成为一项繁琐的任务。为了解决这个问题，我们提出了WonderHuman，它利用2D生成扩散模型先验，从单眼视频中实现动态人类化身的高质量、逼真的重建，包括精确渲染看不见的身体部位。我们的方法引入了双空间优化技术，在规范和观察空间中应用分数蒸馏采样（SDS），以确保视觉一致性，并增强动态人体重建的真实感。此外，我们提出了一种视图选择策略和姿势特征注入，以加强SDS预测和观测数据之间的一致性，确保重建化身的姿势依赖效果和更高的保真度。在实验中，我们的方法在从给定的单眼视频中生成真实感渲染时达到了SOTA性能，特别是对于那些具有挑战性的看不见的部分。项目页面和源代码可以在https://wyiguanw.github.io/WonderHuman/. et.al.|[2502.01045](http://arxiv.org/abs/2502.01045)|null|

<p align=right>(<a href=#updated-on-20250213>back to top</a>)</p>

## 3D Reconstruction

|Publish Date|Title|Abstract|PDF|Code|
|---|---|---|---|---|
|**2025-02-12**|**Re $^3$Sim: Generating High-Fidelity Simulation Data via 3D-Photorealistic Real-to-Sim for Robotic Manipulation**|机器人的真实世界数据收集成本高昂，资源密集，需要熟练的操作员和昂贵的硬件。仿真提供了一种可扩展的替代方案，但由于几何和视觉差距，往往无法实现模拟到真实的泛化。为了应对这些挑战，我们提出了一种3D逼真的真实到模拟系统，即RE$^3$sim，解决了几何和视觉上的模拟到真实的差距。RE$^3$ SIM采用先进的3D重建和神经渲染技术，忠实地重建现实世界的场景，在基于物理的模拟器中实时渲染模拟的交叉视图相机。通过利用特权信息在仿真中有效地收集专家演示，并用模仿学习训练机器人策略，我们验证了真实到模拟到真实管道在各种操纵任务场景中的有效性。值得注意的是，只需模拟数据，我们就可以实现零样本模拟到真实传输，平均成功率超过58%。为了突破真实到模拟的极限，我们进一步生成了一个大规模的模拟数据集，演示了如何从跨各种对象的模拟数据中构建稳健的策略。代码和演示可在以下网址获得：http://xshenhan.github.io/Re3Sim/. et.al.|[2502.08645](http://arxiv.org/abs/2502.08645)|null|
|**2025-02-11**|**EventEgo3D++: 3D Human Motion Capture from a Head-Mounted Event Camera**|单眼以自我为中心的3D人体运动捕捉仍然是一个重大挑战，特别是在低光照和快速运动的条件下，这在头戴式设备应用中很常见。在这些条件下，依赖RGB相机的现有方法往往会失败。为了解决这些局限性，我们引入了EventEgo3D++，这是第一种利用带有鱼眼镜头的单眼事件相机进行3D人体运动捕捉的方法。由于其高时间分辨率，事件相机在高速场景和变化的照明中表现出色，为准确的3D人体运动捕捉提供了可靠的线索。EventEgo3D++利用事件流的LNES表示来实现精确的3D重建。我们还开发了一种配备事件摄像头的移动头戴式设备（HMD）原型，除了合成数据集外，还捕获了一个全面的数据集，其中包括来自受控工作室环境和野外环境的真实事件观察结果。此外，为了提供更全面的数据集，我们包括了提供HMD佩戴者不同视角的非中心RGB流，以及相应的SMPL身体模型。我们的实验表明，与现有解决方案相比，EventEgo3D++即使在具有挑战性的条件下也能实现更高的3D精度和鲁棒性。此外，我们的方法支持以140Hz的速率进行实时3D姿态更新。这项工作是EventEgo3D方法（CVPR 2024）的扩展，进一步推进了以自我为中心的3D人体运动捕捉的最新技术。有关更多详细信息，请访问项目页面https://eventego3d.mpi-inf.mpg.de. et.al.|[2502.07869](http://arxiv.org/abs/2502.07869)|null|
|**2025-02-10**|**TripoSG: High-Fidelity 3D Shape Synthesis using Large-Scale Rectified Flow Models**|扩散技术的最新进展将图像和视频生成推向了前所未有的质量水平，显著加速了生成式人工智能的部署和应用。然而，由于3D数据规模的限制、3D数据处理的复杂性以及对3D领域先进技术的探索不足，3D形状生成技术迄今为止一直落后。当前的3D形状生成方法在输出质量、泛化能力和与输入条件的对齐方面面临着巨大的挑战。我们提出了TripoSG，这是一种新的流线型形状扩散范式，能够生成与输入图像精确对应的高保真3D网格。具体来说，我们提出：1）一种用于3D形状生成的大型整流流量变换器，通过对大量高质量数据的训练实现最先进的保真度。2） 一种混合监督训练策略，结合SDF、正常损失和程知损失，用于3D VAE，实现高质量的3D重建性能。3） 一个数据处理管道，用于生成200万个高质量的3D样本，突出了训练3D生成模型时数据质量和数量的关键规则。通过全面的实验，我们验证了新框架中每个组件的有效性。这些部件的无缝集成使TripoSG在3D形状生成方面达到了最先进的性能。由于高分辨率功能，由此产生的3D形状显示出增强的细节，并对输入图像表现出卓越的保真度。此外，TripoSG在从不同的图像风格和内容生成3D模型方面表现出了更强的通用性，展示了强大的生成能力。为了促进3D生成领域的进步和创新，我们将公开我们的模型。 et.al.|[2502.06608](http://arxiv.org/abs/2502.06608)|null|
|**2025-02-07**|**SC-OmniGS: Self-Calibrating Omnidirectional Gaussian Splatting**|360度相机通过捕获全面的场景数据，简化了辐射场3D重建的数据收集。然而，传统的辐射场方法并没有解决360度图像固有的具体挑战。我们提出了SC OmniGS，这是一种新型的自校准全向高斯散射系统，用于使用360度图像快速准确地重建全向辐射场。我们没有将360度图像转换为立方体图并执行透视图像校准，而是将360度图视为一个完整的球体，并推导出一个数学框架，该框架能够实现直接的全向相机姿态校准，并伴随着3D高斯优化。此外，我们引入了一种可微分的全向相机模型，以纠正现实世界数据的失真，从而提高性能。总体而言，通过最小化加权球面光度损失，对全向相机的内在模型、外在姿态和3D高斯分布进行了联合优化。广泛的实验表明，我们提出的SC OmniGS能够从嘈杂的相机姿态中恢复高质量的辐射场，甚至在以宽基线和非对象中心配置为特征的具有挑战性的场景中没有姿态。消费级全向相机捕获的真实世界数据集中的显著性能提升验证了我们的通用全向相机模型在减少360度图像失真方面的有效性。 et.al.|[2502.04734](http://arxiv.org/abs/2502.04734)|null|
|**2025-02-06**|**Measuring Physical Plausibility of 3D Human Poses Using Physics Simulation**|在物理场景中对人类进行建模对于理解涉及增强现实或从视频中评估人类行为（如体育或身体康复）的应用程序中的人类与环境交互至关重要。最先进的文献从单目或多视角的3D人体姿势开始，并使用这种表示将人固定在3D世界空间中。虽然精度的标准指标捕捉了关节位置误差，但它们并没有考虑3D姿势的物理合理性。这一局限性促使研究人员提出了评估抖动、地板穿透和不平衡姿势的其他指标。然而，这些方法测量的是独立的误差实例，并不代表运动过程中的平衡或稳定性。在这项工作中，我们建议从物理模拟中测量物理合理性。我们引入了两个指标来捕捉来自任何3D人体姿态估计模型的预测3D姿态的物理合理性和稳定性。通过物理模拟，我们发现了与现有合理性度量和运动过程中测量稳定性的相关性。我们评估并比较了两种最先进的方法的性能，即多视图三角基线和来自Human3.6m数据集的地面真实3D标记。 et.al.|[2502.04483](http://arxiv.org/abs/2502.04483)|**[link](https://github.com/MichiganCOG/Simulation_Physical_Plausibility)**|
|**2025-02-06**|**XMTC: Explainable Early Classification of Multivariate Time Series in Reach-to-Grasp Hand Kinematics**|手部运动学可以在人机交互（HCI）中进行测量，目的是预测用户在伸手抓握动作中的意图。使用多个手部传感器，可以捕获多元时间序列数据。给定多个对象上的多个可能动作，目标是对多元时间序列数据进行分类，其中应尽早预测类别。许多机器学习方法已经被开发用于此类分类任务，其中不同的方法在不同的数据集上产生有利的解决方案。因此，我们采用了一种集成方法，包括并加权不同的方法。为了提供值得信赖的分类结果，我们提出了XMTC工具，该工具结合了协调的多视图可视化来分析预测。时间精度图、混淆矩阵热图、时间置信度热图和部分依赖图允许识别早期预测和预测质量之间的最佳权衡，检测和分析具有挑战性的分类条件，并以全面和详细的方式调查预测演变。我们将XMTC应用于多种场景中的真实HCI数据，并表明我们的分类器可以在早期实现良好的分类预测，以及哪些条件易于区分，哪些多元时间序列测量带来了挑战，哪些特征具有最大的影响。 et.al.|[2502.04398](http://arxiv.org/abs/2502.04398)|null|
|**2025-02-06**|**sshELF: Single-Shot Hierarchical Extrapolation of Latent Features for 3D Reconstruction from Sparse-Views**|由于视图重叠最小，从稀疏的朝外视图重建无边界的室外场景带来了重大挑战。以前的方法通常缺乏跨场景理解，其以原始为中心的公式会过载局部特征以补偿缺失的全局上下文，导致场景中看不见的部分模糊。我们提出了sshELF，这是一种通过潜在特征的分层外推进行稀疏视图3D场景重建的快速单镜头流水线。我们的关键见解是，从原始解码中提取信息外推，可以在训练场景中有效地传递结构模式。我们的方法：（1）学习跨场景先验来生成中间虚拟视图，以外推到未观察到的区域，（2）提供了一种将虚拟视图生成与3D原始解码分离的两阶段网络设计，用于高效训练和模块化模型设计，（3）集成了一个预训练的基础模型，用于联合推断潜在特征和纹理，提高了场景理解和泛化能力。sshELF可以从六个稀疏输入视图重建360度场景，并在合成和现实数据集上取得有竞争力的结果。我们发现sshELF忠实地重建了闭塞区域，支持实时渲染，并为下游应用提供了丰富的潜在特征。代码将被发布。 et.al.|[2502.04318](http://arxiv.org/abs/2502.04318)|null|
|**2025-02-05**|**Enhancing Free-hand 3D Photoacoustic and Ultrasound Reconstruction using Deep Learning**|本研究介绍了一种基于运动的学习网络，该网络具有全局局部自关注模块（MoGLo-Net），可增强手持光声和超声（PAUS）成像中的3D重建。标准PAUS成像通常受到视野狭窄和无法有效可视化复杂3D结构的限制。3D徒手技术对齐连续的2D图像进行3D重建，在不依赖外部位置传感器的情况下进行精确的运动估计方面面临着重大挑战。MoGLo-Net通过创新的自我关注机制来解决这些局限性，该机制有效地利用了关键区域，如连续超声图像中完全发育的斑点区域或高回声组织区域，以准确估计运动参数。这有助于从单个帧中提取复杂的特征。此外，我们设计了一种逐块相关操作，以生成与扫描运动高度相关的相关体积。还开发了一个自定义损失函数，以确保在最小化偏差的情况下进行鲁棒学习，利用运动参数的特性。实验评估表明，MoGLo-Net在定量和定性性能指标方面都超越了当前最先进的方法。此外，我们将3D重建技术的应用扩展到简单的B型超声体积之外，以结合多普勒超声和光声成像，实现血管系统的3D可视化。本研究的源代码可在以下网址公开获取：https://github.com/guhong3648/US3D et.al.|[2502.03505](http://arxiv.org/abs/2502.03505)|null|
|**2025-02-05**|**Dress-1-to-3: Single Image to Simulation-Ready 3D Outfit with Diffusion Prior and Differentiable Physics**|大型模型的最新进展显著推进了图像到3D的重建。然而，生成的模型通常被融合成一个整体，限制了它们在下游任务中的适用性。本文主要研究3D服装生成，这是动态服装动画虚拟试穿等应用的一个关键领域，这些应用要求服装是可分离的，并且可以进行模拟。我们介绍Dress1-to-3，这是一种新颖的管道，可以从野外图像中重建具有缝制图案和人类的物理上合理的、可模拟的分离服装。从图像开始，我们的方法将预训练的图像与用于创建粗略缝制图案的缝制图案生成模型与预训练的多视图扩散模型相结合，以生成多视图图像。基于生成的多视图图像，使用可区分的服装模拟器进一步细化缝制图案。多功能实验表明，我们的优化方法大大增强了重建的3D服装和人类与输入图像的几何对齐。此外，通过集成纹理生成模块和人体运动生成模块，我们生成了定制的物理逼真的动态服装演示。项目页面：https://dress-1-to-3.github.io/ et.al.|[2502.03449](http://arxiv.org/abs/2502.03449)|null|
|**2025-02-04**|**SiLVR: Scalable Lidar-Visual Radiance Field Reconstruction with Uncertainty Quantification**|我们提出了一种基于神经辐射场（NeRF）的大规模重建系统，该系统将激光雷达和视觉数据融合在一起，生成高质量的重建，这些重建具有几何精度，并能捕捉到逼真的纹理。我们的系统采用了最先进的NeRF表示法，额外集成了激光雷达。添加激光雷达数据会对深度和表面法线添加强烈的几何约束，这在建模包含模糊视觉重建线索的均匀纹理表面时特别有用。此外，我们将重建的认知不确定性估计为给定相机和激光雷达的传感器观测值的辐射场中每个点位置的空间方差。这使得能够识别由每种传感器模态可靠重建的区域，从而允许根据估计的不确定性对地图进行滤波。我们的系统还可以利用实时位姿图激光雷达SLAM系统在在线映射过程中产生的轨迹，引导（后处理）运动结构（SfM）重建过程，将SfM训练时间减少高达70%。它还有助于正确约束对激光雷达深度损失至关重要的整体度量尺度。然后，可以使用光谱聚类将全局一致的轨迹划分为子图，将共视图像集分组在一起。这种子映射方法比基于距离的分割更适合视觉重建。根据逐点不确定性估计对每个子图进行滤波并合并，以获得最终的大规模3D重建。我们在涉及机器人安装和手持扫描的实验中演示了使用多摄像头激光雷达传感器套件的重建系统。我们的测试数据集覆盖了20000多平方米的总面积，包括多座大学建筑和一座多层建筑的航空测量。 et.al.|[2502.02657](http://arxiv.org/abs/2502.02657)|null|

<p align=right>(<a href=#updated-on-20250213>back to top</a>)</p>

## Diffusion

|Publish Date|Title|Abstract|PDF|Code|
|---|---|---|---|---|
|**2025-02-12**|**SwiftSketch: A Diffusion Model for Image-to-Vector Sketch Generation**|大型视觉语言模型的最新进展使高表达性和多样化的矢量草图生成成为可能。然而，最先进的方法依赖于一个耗时的优化过程，该过程涉及来自预训练模型的重复反馈，以确定笔划位置。因此，尽管产生了令人印象深刻的草图，但这些方法在实际应用中受到限制。在这项工作中，我们介绍了SwiftSketch，这是一种用于图像条件矢量草图生成的扩散模型，可以在不到一秒钟的时间内生成高质量的草图。SwiftSketch通过逐步对从高斯分布中采样的笔划控制点进行去噪来进行操作。其变换器-解码器架构旨在有效地处理向量表示的离散性，并捕获笔划之间固有的全局依赖关系。为了训练SwiftSketch，我们构建了一个图像草图对的合成数据集，解决了现有草图数据集的局限性，这些数据集通常由非艺术家创建，缺乏专业质量。为了生成这些合成草图，我们引入了ControlSketch，这是一种通过深度感知ControlNet结合精确的空间控制来增强基于SDS的技术的方法。我们证明了SwiftSketch可以概括不同的概念，有效地制作出将高保真度与自然和视觉吸引力风格相结合的草图。 et.al.|[2502.08642](http://arxiv.org/abs/2502.08642)|null|
|**2025-02-12**|**CineMaster: A 3D-Aware and Controllable Framework for Cinematic Text-to-Video Generation**|在这项工作中，我们提出了CineMaster，这是一个用于3D感知和可控文本到视频生成的新框架。我们的目标是为用户提供与专业电影导演相当的可控性：在场景中精确放置物体，在3D空间中灵活操纵物体和相机，以及对渲染帧的直观布局控制。为了实现这一目标，CineMaster分两个阶段运行。在第一阶段，我们设计了一个交互式工作流程，允许用户通过定位对象边界框和定义3D空间内的相机运动来直观地构建3D感知条件信号。在第二阶段，这些控制信号——包括渲染的深度图、相机轨迹和对象类标签——作为文本到视频扩散模型的指导，确保生成用户期望的视频内容。此外，为了克服具有3D对象运动和相机姿态注释的野外数据集的稀缺性，我们仔细建立了一个自动数据注释管道，从大规模视频数据中提取3D边界框和相机轨迹。大量的定性和定量实验表明，CineMaster明显优于现有方法，并实现了出色的3D感知文本到视频生成。项目页面：https://cinemaster-dev.github.io/. et.al.|[2502.08639](http://arxiv.org/abs/2502.08639)|null|
|**2025-02-12**|**Chasing Charge Carriers: Diffusion Dynamics in Mixed-n Quasi-Two-Dimensional Colloidal MAPbBr3 Perovskites**|在光电应用中，金属卤化物钙钛矿（MHP）因其高度可调和竞争激烈的光学性能而成为引人注目的材料。胶体合成能够控制形成各种形态的MHP纳米晶体，所有这些纳米晶体都具有不同的载体性质，因此具有不同的光学和载流子输运行为。我们表征了三种不同的甲基铵-三溴化铅钙钛矿（MAPbBr3）形态：纳米片（NPL）、纳米片（NS）和纳米条纹（NST），它们是通过热注射合成方案合成的，参数略有不同。采用荧光成像显微镜（FLIM）对载流子迁移进行时间和空间分辨测量，以量化光激发下电荷载流子的迁移过程。考虑到混合n胶体MHPs中的漏斗和捕获过程，在二维扩散模型框架内对结果进行了合理化。发现亚扩散模式在纳米晶体中占主导地位，其中块状NST的载流子扩散率最高，其次是层状NSs和NPL薄膜。这些发现提供了对钙钛矿中与光伏和发光器件相关的光电过程的更好理解。 et.al.|[2502.08601](http://arxiv.org/abs/2502.08601)|null|
|**2025-02-12**|**Enhancing Diffusion Models Efficiency by Disentangling Total-Variance and Signal-to-Noise Ratio**|扩散模型的长采样时间仍然是一个重要的瓶颈，可以通过减少扩散时间步长来缓解。然而，步骤较少的样本的质量在很大程度上取决于噪声调度，即在每一步引入噪声和减少信号的具体方式。尽管之前的工作对原始的方差保持和方差爆炸调度进行了改进，但这些方法被动地调整了总方差，而没有直接控制它。在这项工作中，我们提出了一种新的总方差/信噪比解纠缠（TV/SNR）框架，其中TV和SNR可以独立控制。我们的方法表明，通过设置恒定的电视时间表，同时保持相同的信噪比时间表，电视呈指数级爆炸的不同现有时间表可以得到改进。此外，推广最优输运流匹配的信噪比调度显著提高了分子结构生成的性能，实现了稳定分子的少步生成。在图像生成中观察到类似的趋势，其中我们采用均匀扩散时间网格的方法与高度定制的EDM采样器的性能相当。 et.al.|[2502.08598](http://arxiv.org/abs/2502.08598)|null|
|**2025-02-12**|**Light-A-Video: Training-free Video Relighting via Progressive Light Fusion**|在大规模数据集和预先训练的扩散模型的推动下，图像再照明模型的最新进展使得能够施加一致的照明。然而，视频重新照明仍然滞后，主要是由于培训成本过高和缺乏多样化、高质量的视频重新照明数据集。在逐帧的基础上简单应用图像再照明模型会导致几个问题：照明源不一致和再照明外观不一致，导致生成的视频中出现闪烁。在这项工作中，我们提出了Light-A-Video，这是一种无需训练的方法，可以实现时间平滑的视频重新照明。Light-A-Video改编自图像重新照明模型，引入了两项关键技术来提高照明一致性。首先，我们设计了一个一致的光注意力（CLA）模块，该模块增强了自注意力层内的跨帧交互，以稳定背景光源的生成。其次，利用光传输独立性的物理原理，我们使用渐进式光融合（PLF）策略在源视频的外观和重新点亮的外观之间应用线性混合，以确保照明的平滑时间过渡。实验表明，Light-A-Video提高了重新点亮视频的时间一致性，同时保持了图像质量，确保了帧间连贯的照明过渡。项目页面：https://bujiazi.github.io/light-a-video.github.io/. et.al.|[2502.08590](http://arxiv.org/abs/2502.08590)|**[link](https://github.com/bcmi/Light-A-Video)**|
|**2025-02-12**|**Ultrasound Image Generation using Latent Diffusion Models**|用于图像生成的扩散模型由于其生成多样化、高质量图像的能力而越来越受到人们的关注。图像生成在医学成像中具有巨大的潜力，因为与自然图像相比，开源医学图像很难获得，特别是在罕见的情况下。生成的图像稍后可用于训练分类和分割模型。在本文中，我们提出通过在不同的公开数据库上连续微调大型扩散模型来模拟逼真的超声（US）图像。为此，我们在超声乳腺图像数据集BUSI（Breast US Images）上对最先进的潜在扩散模型Stable Diffusion进行了微调。我们使用指定器官和病理的简单提示成功生成了高质量的乳腺超声图像，这对三位经验丰富的美国科学家和一位美国放射科医生来说似乎很现实。此外，我们通过ControlNet用分割来调节模型，从而提供用户控制。我们将在发布源代码http://code.sonography.ai/以允许科学界快速生成美国图像。 et.al.|[2502.08580](http://arxiv.org/abs/2502.08580)|null|
|**2025-02-12**|**Mapping the Landscape of Generative AI in Network Monitoring and Management**|生成性人工智能（GenAI）模型，如LLM、GPT和扩散模型，最近受到了研究界和工业界的广泛关注。本次调查探讨了它们在网络监控和管理中的应用，重点关注突出的用例以及挑战和机遇。我们讨论了网络流量生成和分类、网络入侵检测、网络系统日志分析和网络数字辅助如何从GenAI模型的使用中受益。此外，我们还概述了可用的GenAI模型、大规模训练阶段的数据集以及开发此类模型的平台。最后，我们讨论了可能减轻采用GenAI进行网络监控和管理的障碍的研究方向。我们的调查旨在描绘当前的格局，并为未来利用GenAI进行网络监控和管理的研究铺平道路。 et.al.|[2502.08576](http://arxiv.org/abs/2502.08576)|null|
|**2025-02-12**|**Brain Latent Progression: Individual-based Spatiotemporal Disease Progression on 3D Brain MRIs via Latent Diffusion**|纵向磁共振成像（MRI）数据集的日益普及促进了人工智能（AI）驱动的疾病进展建模，使预测个体患者未来的医学扫描成为可能。然而，尽管人工智能取得了重大进展，但当前的方法仍面临挑战，包括实现患者特异性个性化、确保时空一致性、有效利用纵向数据以及管理3D扫描的大量内存需求。为了应对这些挑战，我们提出了脑潜伏进展（BrLP），这是一种新的时空模型，旨在预测3D脑MRI中的个体水平疾病进展。BrLP的关键贡献有四个方面：（i）它在一个小的潜伏空间中运作，减轻了高维成像数据带来的计算挑战；（ii）它明确地整合了主题元数据，以增强预测的个性化；（iii）它通过辅助模型整合了疾病动力学的先验知识，促进了纵向数据的整合；以及（iv）它引入了潜在平均稳定（LAS）算法，该算法（a）在推理时加强预测进程的时空一致性，（b）允许我们得出预测的不确定性度量。我们在2805名受试者的11730张T1加权（T1w）脑MRI上训练和评估BrLP，并在962名受试人的2257张MRI组成的外部测试集上验证其普适性。我们的实验将BrLP生成的MRI扫描与真实的随访MRI进行了比较，与现有方法相比，证明了最先进的准确性。该代码可在以下网址公开获取：https://github.com/LemuelPuglisi/BrLP. et.al.|[2502.08560](http://arxiv.org/abs/2502.08560)|null|
|**2025-02-12**|**Foliar Uptake of Biocides: Statistical Assessment of Compartmental and Diffusion-Based Models**|全球人口的增长导致了粮食需求的增加，为了实现这一目标，需要农药等产品来保护作物。研究的重点是开发对环境危害较小的新产品，数学模型是帮助理解农药吸收机制的工具，然后在产品开发阶段提供指导。本文应用了一种系统的方法来模拟农药的叶面吸收，以考虑实验数据和模型结构中的不确定性。对不同模型进行了比较，重点是通过动态灵敏度分布和相关性分析来识别模型参数。最后，进行了数据增强研究，以利用该模型进行实验设计，并为未来的实验活动提供实际支持，为在叶面吸收背景下进一步应用基于模型的实验设计技术铺平了道路。 et.al.|[2502.08533](http://arxiv.org/abs/2502.08533)|null|
|**2025-02-12**|**BCDDM: Branch-Corrected Denoising Diffusion Model for Black Hole Image Generation**|通过将事件视界望远镜（EHT）数据拟合到通过广义相对论射线追踪（GRRT）生成的模拟图像中，可以推断黑洞和吸积流的性质。然而，由于GRRT的计算密集性，生成特定辐射通量图像的效率需要提高。本文介绍了分支校正去噪扩散模型（BCDDM），该模型使用分支校正机制和加权混合损失函数来提高基于辐射低效吸积流（RIAF）模型的七个物理参数生成的黑洞图像的准确性。我们的实验表明，生成的图像与其物理参数之间存在很强的相关性。通过使用BCDDM生成的图像增强GRRT数据集，并使用ResNet50进行参数回归，我们实现了参数预测性能的显著提高。这种方法降低了计算成本，并为数据集扩展、参数估计和模型拟合提供了一种更快、更有效的方法。 et.al.|[2502.08528](http://arxiv.org/abs/2502.08528)|null|

<p align=right>(<a href=#updated-on-20250213>back to top</a>)</p>

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

<p align=right>(<a href=#updated-on-20250213>back to top</a>)</p>

[contributors-shield]: https://img.shields.io/github/contributors/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[contributors-url]: https://github.com/Vincentqyw/cv-arxiv-daily/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[forks-url]: https://github.com/Vincentqyw/cv-arxiv-daily/network/members
[stars-shield]: https://img.shields.io/github/stars/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[stars-url]: https://github.com/Vincentqyw/cv-arxiv-daily/stargazers
[issues-shield]: https://img.shields.io/github/issues/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[issues-url]: https://github.com/Vincentqyw/cv-arxiv-daily/issues

