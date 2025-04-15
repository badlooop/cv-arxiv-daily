[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]

## Updated on 2025.04.15
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
|**2025-04-11**|**Seaweed-7B: Cost-Effective Training of Video Generation Foundation Model**|本技术报告提出了一种经济高效的策略，用于训练视频生成基础模型。我们提出了一个中等规模的研究模型，它有大约70亿个参数（7B），称为海藻-7B，使用665000 H100 GPU小时从头开始训练。尽管使用适度的计算资源进行训练，但与当代更大尺寸的视频生成模型相比，海藻-7B表现出了极具竞争力的性能。在资源受限的环境中，设计选择尤为重要。本技术报告重点介绍了提高中型扩散模型性能的关键设计决策。根据经验，我们得出两个观察结果：（1）Seaweed-7B的性能与在更大GPU资源上训练的更大模型相当，甚至超过了后者；（2）我们的模型具有很强的泛化能力，可以通过轻量级微调或持续训练在广泛的下游应用程序中有效地适应。请参阅项目页面https://seaweed.video/ et.al.|[2504.08685](http://arxiv.org/abs/2504.08685)|null|
|**2025-04-11**|**Training-free Guidance in Text-to-Video Generation via Multimodal Planning and Structured Noise Initialization**|文本到视频（T2V）扩散模型的最新进展显著提高了生成视频的视觉质量。然而，即使是最近的T2V模型也发现很难准确地遵循文本描述，特别是当提示需要精确控制空间布局或对象轨迹时。最近的一项研究使用了T2V模型的布局指导，这些模型需要在推理过程中对注意力图进行微调或迭代操作。这大大增加了内存需求，使得很难采用大型T2V模型作为骨干。为了解决这个问题，我们引入了视频MSG，这是一种基于多模态规划和结构化噪声初始化的T2V生成无需训练的引导方法。视频MSG由三个步骤组成，在前两个步骤中，视频MSG创建视频草图，这是最终视频的精细时空计划，以草稿视频帧的形式指定背景、前景和对象轨迹。在最后一步中，Video MSG通过噪声反演和去噪，使用Video Sketch引导下游T2V扩散模型。值得注意的是，在推理过程中，视频MSG不需要进行微调或注意力操纵，也不需要额外的记忆，这使得采用大型T2V模型变得更加容易。Video MSG在流行的T2V生成基准（T2VCompBench和VBench）上展示了其在增强多个T2V主干（VideoCrafter2和CogVideoX-5B）的文本对齐方面的有效性。我们提供了关于噪声反转率、不同背景生成器、背景对象检测和前景对象分割的全面消融研究。 et.al.|[2504.08641](http://arxiv.org/abs/2504.08641)|null|
|**2025-04-11**|**Discriminator-Free Direct Preference Optimization for Video Diffusion**|直接偏好优化（DPO）通过输赢数据对将模型与人类偏好对齐，在语言和图像生成方面取得了显著成功。然而，将DPO应用于视频扩散模型面临着严峻的挑战：（1）数据效率低下。每次DPO迭代生成数千个视频会带来高昂的成本；（2） 评估不确定性。人类注释存在主观偏见，自动鉴别器无法检测到闪烁或运动不连贯等微妙的时间伪影。为了解决这些问题，我们提出了一种无鉴别器的视频DPO框架，该框架：（1）使用原始真实视频作为获胜案例，使用其编辑版本（例如，反转、混洗或噪声破坏的剪辑）作为失败案例；（2） 训练视频扩散模型以区分和避免编辑引入的伪影。这种方法消除了对昂贵的合成视频比较的需要，提供了明确的质量信号，并通过简单的编辑操作实现了无限制的训练数据扩展。我们从理论上证明了该框架的有效性，即使真实视频和模型生成的视频遵循不同的分布。CogVideoX上的实验证明了所提出方法的有效性。 et.al.|[2504.08542](http://arxiv.org/abs/2504.08542)|null|
|**2025-04-11**|**Diffusion Models for Robotic Manipulation: A Survey**|扩散生成模型在图像和视频生成等视觉领域取得了显著成功。最近，它们也成为机器人技术中一种有前景的方法，特别是在机器人操作方面。扩散模型利用概率框架，它们以建模多模态分布的能力和对高维输入和输出空间的鲁棒性而脱颖而出。这项调查全面回顾了机器人操纵中最先进的扩散模型，包括抓握学习、轨迹规划和数据增强。场景和图像增强的扩散模型位于机器人技术和计算机视觉的交叉点，用于基于视觉的任务，以提高通用性和数据稀缺性。本文还介绍了扩散模型的两个主要框架及其与模仿学习和强化学习的整合。此外，它还讨论了常见的架构和基准测试，并指出了当前最先进的基于扩散的方法的挑战和优势。 et.al.|[2504.08438](http://arxiv.org/abs/2504.08438)|null|
|**2025-04-11**|**EasyGenNet: An Efficient Framework for Audio-Driven Gesture Video Generation Based on Diffusion Model**|音频驱动的cospeech视频生成通常涉及两个阶段：语音到手势和手势到视频。虽然在语音到手势生成方面取得了重大进展，但在手势到视频系统中合成自然表情和手势仍然具有挑战性。为了提高生成效果，以往的工作采用了复杂的输入和训练策略，需要大量的数据集进行预训练，这给实际应用带来了不便。我们提出了一种简单的单阶段训练方法和一种基于扩散模型的时间推理方法，用于合成逼真和连续的手势视频，而不需要对时间模块进行额外的训练。整个模型利用了现有的预训练权重，每个角色一次只需要几千帧数据即可完成微调。在视频生成器的基础上，我们引入了一种新的音频到视频管道来合成同语音视频，使用2D人体骨架作为中间运动表示。我们的实验表明，我们的方法优于现有的基于GAN和基于扩散的方法。 et.al.|[2504.08344](http://arxiv.org/abs/2504.08344)|null|
|**2025-04-11**|**Generative AI for Film Creation: A Survey of Recent Advances**|生成人工智能（GenAI）正在改变电影制作，为艺术家提供文本到图像和图像到视频扩散、神经辐射场、化身生成和3D合成等工具。本文研究了这些技术在电影制作中的应用，分析了最近人工智能驱动电影的工作流程，以了解GenAI如何为角色创作、美学风格和叙事做出贡献。我们探索了保持角色一致性、实现风格连贯性和确保动作连续性的关键策略。此外，我们强调了新兴趋势，如3D生成的使用越来越多，以及真实镜头与人工智能生成元素的整合。除了技术进步，我们还研究了GenAI如何实现新的艺术表达，从生成难以拍摄的镜头到基于梦幻扩散的变形效果、抽象视觉效果和超凡脱俗的物体。我们还收集艺术家对挑战和所需改进的反馈，包括一致性、可控性、精细编辑和动作细化。我们的研究提供了对人工智能和电影制作不断发展的交叉点的见解，为研究人员和艺术家在这个快速发展的领域中导航提供了路线图。 et.al.|[2504.08296](http://arxiv.org/abs/2504.08296)|null|
|**2025-04-11**|**RealCam-Vid: High-resolution Video Dataset with Dynamic Scenes and Metric-scale Camera Movements**|相机可控视频生成的最新进展受到了对具有相对比例相机注释的静态场景数据集（如RealEstate10K）的依赖的限制。虽然这些数据集能够实现基本的视点控制，但它们无法捕捉动态场景交互，并且缺乏度量尺度几何一致性，这对于在复杂环境中合成逼真的物体运动和精确的相机轨迹至关重要。为了弥合这一差距，我们在https://github.com/ZGCTroy/RealCam-Vid. et.al.|[2504.08212](http://arxiv.org/abs/2504.08212)|null|
|**2025-04-11**|**TokenMotion: Decoupled Motion Control via Token Disentanglement for Human-centric Video Generation**|视频生成中以人为中心的运动控制仍然是一个关键挑战，特别是在像标志性的格莱美Glambot时刻这样的场景中联合控制相机运动和人体姿势时。虽然最近的视频扩散模型取得了重大进展，但现有的方法在有限的运动表示和相机与人体运动控制的集成不足方面存在困难。在这项工作中，我们提出了TokenMotion，这是第一个基于DiT的视频扩散框架，可以对相机运动、人体运动及其联合交互进行精细控制。我们将相机轨迹和人体姿势表示为时空标记，以实现局部控制粒度。我们的方法引入了一个统一的建模框架，该框架利用解耦和融合策略，由人类感知的动态掩模桥接，有效地处理了组合运动信号的空间和时间变化特性。通过广泛的实验，我们证明了TokenMotion在文本到视频和图像到视频范式中的有效性，在以人为中心的运动控制任务中始终优于当前最先进的方法。我们的工作代表了可控视频生成的重大进步，尤其与创意制作应用相关。 et.al.|[2504.08181](http://arxiv.org/abs/2504.08181)|null|
|**2025-04-10**|**Geo4D: Leveraging Video Generators for Geometric 4D Scene Reconstruction**|我们介绍了Geo4D，这是一种将视频扩散模型重新用于动态场景的单目3D重建的方法。通过利用这种视频模型捕获的强动态先验，可以仅使用合成数据来训练Geo4D，同时以零样本的方式将其很好地推广到真实数据。Geo4D预测了几种互补的几何形态，即点、深度和射线图。它使用一种新的多模态对齐算法在推理时对齐和融合这些模态以及多个滑动窗口，从而获得长视频的鲁棒和准确的4D重建。跨多个基准的广泛实验表明，Geo4D显著超越了最先进的视频深度估计方法，包括MonST3R等最新方法，这些方法也被设计用于处理动态场景。 et.al.|[2504.07961](http://arxiv.org/abs/2504.07961)|null|
|**2025-04-10**|**Beyond the Frame: Generating 360° Panoramic Videos from Perspective Videos**|360度视频已经成为代表我们动态视觉世界的有前景的媒介。与标准相机的“隧道视觉”相比，它们的无边界视野为我们的周围环境提供了更完整的视角。虽然现有的视频模型擅长制作标准视频，但它们生成完整全景视频的能力仍然难以捉摸。在本文中，我们研究了视频到360度生成的任务：给定一个透视视频作为输入，我们的目标是生成一个与原始视频一致的完整全景视频。与传统的视频生成任务不同，输出的视场要大得多，模型需要对场景的空间布局和对象的动态有深入的了解，以保持时空一致性。为了应对这些挑战，我们首先利用在线提供的丰富的360度视频，并开发一个高质量的数据过滤管道来管理成对训练数据。然后，我们仔细设计了一系列几何和运动感知操作，以促进学习过程并提高360度视频生成的质量。实验结果表明，我们的模型可以从野外视角视频中生成逼真连贯的360度视频。此外，我们还展示了它的潜在应用，包括视频稳定、相机视点控制和交互式视觉问答。 et.al.|[2504.07940](http://arxiv.org/abs/2504.07940)|null|

<p align=right>(<a href=#updated-on-20250415>back to top</a>)</p>

## 3D

|Publish Date|Title|Abstract|PDF|Code|
|---|---|---|---|---|
|**2025-04-14**|**LL-Gaussian: Low-Light Scene Reconstruction and Enhancement via Gaussian Splatting for Novel View Synthesis**|低光场景中的新型视图合成（NVS）仍然是一个重大挑战，因为输入质量下降，噪声严重，动态范围低（LDR），初始化不可靠。虽然最近基于NeRF的方法显示出有希望的结果，但大多数方法都存在计算成本高的问题，有些方法依赖于仔细捕获或预处理的数据，如RAW传感器输入或多次曝光序列，这严重限制了它们的实用性。相比之下，3D高斯散斑（3DGS）能够以具有竞争力的视觉保真度实现实时渲染；然而，现有的基于3DGS的方法在低光sRGB输入方面存在困难，导致高斯初始化不稳定和噪声抑制无效。为了应对这些挑战，我们提出了LL Gaussian，这是一种用于从低光sRGB图像进行3D重建和增强的新框架，实现了伪正常光新视图合成。我们的方法引入了三个关键创新：1）端到端的低光高斯初始化模块（LLGIM），该模块利用基于学习的MVS方法中的密集先验来生成高质量的初始点云；2） 双分支高斯分解模型，将固有场景属性（反射率和照度）与瞬态干扰分离，实现稳定和可解释的优化；3） 在联合引导分解和增强之前，由物理约束和扩散引导的无监督优化策略。此外，我们还提供了一个在极端低光环境中收集的具有挑战性的数据集，并展示了LL Gaussian的有效性。与最先进的基于NeRF的方法相比，LL Gaussian的推理速度提高了2000倍，训练时间缩短到2%，同时提供了卓越的重建和渲染质量。 et.al.|[2504.10331](http://arxiv.org/abs/2504.10331)|null|
|**2025-04-14**|**EBAD-Gaussian: Event-driven Bundle Adjusted Deblur Gaussian Splatting**|虽然3D高斯散斑（3D-GS）实现了逼真的新颖视图合成，但其性能会随着运动模糊而降低。在快速运动或低光照条件下，现有的基于RGB的去模糊方法难以对曝光过程中的相机姿态和辐射变化进行建模，从而降低了重建精度。事件相机捕捉曝光过程中连续的亮度变化，可以有效地帮助建模运动模糊并提高重建质量。因此，我们提出了事件驱动的束调整去模糊高斯散斑（EBAD-Gaussian），它从事件流和严重模糊的图像中重建清晰的3D高斯分布。该方法在恢复曝光时间内的相机运动轨迹的同时，联合学习这些高斯参数。具体来说，我们首先通过在曝光时间内合成多个潜在的清晰图像来构建模糊损失函数，使真实模糊图像和合成模糊图像之间的差异最小化。然后，我们使用事件流来监控曝光期内任何时间潜在清晰图像之间的光强变化，补充RGB图像中丢失的光强动态变化。此外，我们基于基于事件的双积分（EDI）先验优化了中间曝光时间的潜在清晰图像，应用一致性约束来增强重建图像的细节和纹理信息。对合成数据集和真实世界数据集的广泛实验表明，EBAD-Gaussian可以在模糊图像和事件流输入的条件下实现高质量的3D场景重建。 et.al.|[2504.10012](http://arxiv.org/abs/2504.10012)|null|
|**2025-04-14**|**MCBlock: Boosting Neural Radiance Field Training Speed by MCTS-based Dynamic-Resolution Ray Sampling**|神经辐射场（NeRF）因其高保真的新颖视图合成而广为人知。然而，即使是最先进的NeRF模型Gaussian Splatting也需要几分钟的训练时间，远低于远程医疗等多媒体场景所需的实时性能。其中一个障碍是采样效率低下，现有工作仅部分解决了这一问题。现有的点采样算法均匀地采样简单纹理区域（易于拟合）和复杂纹理区域（难以拟合），而现有的光线采样算法则以最精细的粒度（即像素级）对这些区域进行采样，这都浪费了GPU训练资源。实际上，具有不同纹理强度的区域需要不同的采样粒度。为此，我们提出了一种新的动态分辨率射线采样算法MCBlock，该算法采用蒙特卡洛树搜索（MCTS）将每个训练图像划分为不同大小的像素块，用于主动逐块训练。具体来说，根据训练图像的纹理对树进行初始化，以提高初始化速度，扩展/修剪模块动态优化块划分。MCBlock在开源工具集Nerfstudio中实现，训练加速高达2.33倍，超过了其他射线采样算法。我们相信MCBlock可以应用于任何锥体追踪NeRF模型，并为多媒体社区做出贡献。 et.al.|[2504.09878](http://arxiv.org/abs/2504.09878)|null|
|**2025-04-13**|**DropoutGS: Dropping Out Gaussians for Better Sparse-view Rendering**|尽管3D高斯散斑（3DGS）在新颖的视图合成中显示出有前景的结果，但其性能会随着稀疏输入而急剧下降，并产生不希望的伪影。随着训练视图数量的减少，新的视图合成任务会退化为一个高度不确定的问题，导致现有方法存在臭名昭著的过拟合问题。有趣的是，我们观察到高斯基元较少的模型在稀疏输入下表现出较少的过拟合。受这一观察的启发，我们提出了一种随机丢弃正则化（RDR）来利用低复杂度模型的优点来缓解过拟合。此外，为了弥补这些模型缺乏高频细节的问题，开发了一种边缘引导的分割策略（ESS）。通过这两种技术，我们的方法（称为DropoutGS）提供了一种简单而有效的插件方法来提高现有3DGS方法的泛化性能。广泛的实验表明，我们的DropoutGS在包括Blender、LLFF和DTU在内的基准数据集的稀疏视图下产生了最先进的性能。项目页面位于：https://xuyx55.github.io/DropoutGS/. et.al.|[2504.09491](http://arxiv.org/abs/2504.09491)|null|
|**2025-04-12**|**BlockGaussian: Efficient Large-Scale Scene NovelView Synthesis via Adaptive Block-Based Gaussian Splatting**|3D高斯散斑（3DGS）的最新进展在新的视图合成任务中显示出巨大的潜力。分而治之范式实现了大规模场景重建，但在场景分割、优化和合并过程中仍然存在重大挑战。本文介绍了BlockGaussian，这是一种新的框架，结合了内容感知场景分割策略和可见性感知块优化，以实现高效、高质量的大规模场景重建。具体来说，我们的方法考虑了不同区域之间的内容复杂度变化，并在场景分割过程中平衡了计算负载，从而实现了高效的场景重建。为了解决独立块优化中的监督不匹配问题，我们在单个块优化中引入了辅助点来对齐地面真实监督，从而提高了重建质量。此外，我们提出了一种伪视图几何约束，有效地减轻了块合并过程中空域浮动导致的渲染质量下降。大规模场景上的大量实验表明，我们的方法在重建效率和渲染质量方面都达到了最先进的性能，优化速度提高了5倍，在多个基准测试中平均PSNR提高了1.21dB。值得注意的是，BlockGaussian显著降低了计算要求，可以在单个24GB VRAM设备上进行大规模场景重建。项目页面可在https://github.com/SunshineWYC/BlockGaussian et.al.|[2504.09048](http://arxiv.org/abs/2504.09048)|null|
|**2025-04-11**|**Cut-and-Splat: Leveraging Gaussian Splatting for Synthetic Data Generation**|生成合成图像是一种廉价获取标记数据以训练计算机视觉模型的有用方法。然而，获得相关对象的精确3D模型是必要的，由于模拟照明效果和相机伪影的挑战，最终的图像在真实感方面往往存在差距。我们建议使用称为高斯散斑的新颖视图合成方法来解决这些挑战。我们开发了一个合成数据管道，用于为特定对象生成高质量的上下文感知实例分割训练数据。这个过程是完全自动化的，只需要目标对象的视频。我们训练目标对象的高斯散斑模型，并自动从视频中提取对象。利用高斯散斑，我们然后在随机背景图像上渲染对象，并采用单目深度估计将对象放置在可信的姿势中。我们引入了一个新的数据集来验证我们的方法，并显示出比其他数据生成方法（如剪切粘贴和扩散模型生成）更优越的性能。 et.al.|[2504.08473](http://arxiv.org/abs/2504.08473)|null|
|**2025-04-11**|**SN-LiDAR: Semantic Neural Fields for Novel Space-time View LiDAR Synthesis**|最近的研究已经开始探索激光雷达点云的新颖视图合成（NVS），旨在从看不见的视点生成逼真的激光雷达扫描。然而，大多数现有的方法都不能重建语义标签，而语义标签对于自动驾驶和机器人感知等许多下游应用至关重要。与受益于强大分割模型的图像不同，LiDAR点云缺乏如此大规模的预训练模型，这使得语义标注既费时又费力。为了应对这一挑战，我们提出了SN LiDAR，这是一种联合执行精确语义分割、高质量几何重建和逼真LiDAR合成的方法。具体来说，我们采用从粗到细的平面网格特征表示来从多帧点云中提取全局特征，并利用基于CNN的编码器从当前帧点云中提取局部语义特征。SemanticKITTI和KITTI-360的大量实验证明了SN LiDAR在语义和几何重建方面的优越性，有效地处理了动态对象和大规模场景。代码将在https://github.com/dtc111111/SN-Lidar. et.al.|[2504.08361](http://arxiv.org/abs/2504.08361)|null|
|**2025-04-11**|**Geometric Consistency Refinement for Single Image Novel View Synthesis via Test-Time Adaptation of Diffusion Models**|单图像新视图合成（NVS）的扩散模型可以生成高度逼真和合理的图像，但它们在给定相对姿态的几何一致性方面受到限制。生成的图像通常显示出与目标姿态给出的应满足的极线约束相关的显著误差。本文通过提出一种方法来提高单图像NVS扩散模型生成的图像的几何正确性，从而解决了这个问题。我们基于图像匹配和极线约束制定了一个损失函数，并优化了扩散采样过程中的起始噪声，使生成的图像既能是真实的图像，又能满足从给定目标姿态导出的几何约束。我们的方法不需要训练数据或对扩散模型进行微调，我们表明我们可以将其应用于单幅图像NVS的多个最先进的模型。该方法在MegaScenes数据集上进行了评估，我们表明，与基线模型相比，几何一致性得到了改善，同时保留了生成图像的质量。 et.al.|[2504.08348](http://arxiv.org/abs/2504.08348)|null|
|**2025-04-10**|**InteractAvatar: Modeling Hand-Face Interaction in Photorealistic Avatars with Deformable Gaussians**|随着社区对数字化身的兴趣日益浓厚，加上表情和手势在交流中的重要性，在电话会议、游戏和AR/VR等许多行业中，对自然化身行为进行建模仍然是一个重要的挑战。人的手是与环境交互的主要工具，对于逼真的人类行为建模至关重要，但现有的3D手和头部化身模型往往忽视了手与身体交互的关键方面，例如手与脸之间的交互。我们提出了InteractitAvatar，这是第一个忠实地捕捉动态手和非刚性手-脸交互的照片级真实感外观的模型。我们的新型动态高斯手模型结合了模板模型和3D高斯散布以及动态细化模块，捕捉了姿势相关的变化，例如关节运动过程中出现的细皱纹和复杂阴影。重要的是，我们的人脸交互模块模拟了常见手势背后的微妙几何形状和外观动态。通过新颖的视图合成、自再现和跨身份再现实验，我们证明了InteractitAvatar可以从单目或多视点视频中重建手和手脸交互，具有高保真的细节，并可以用新颖的姿势进行动画制作。 et.al.|[2504.07949](http://arxiv.org/abs/2504.07949)|null|
|**2025-04-09**|**Glossy Object Reconstruction with Cost-effective Polarized Acquisition**|基于图像的光滑物体3D重建的挑战在于从捕获的图像中分离出光滑表面上的漫反射和镜面反射分量，这项任务因仅使用RGB数据识别照明条件和材质属性的模糊性而变得复杂。虽然最先进的方法依赖于定制和/或高端设备进行数据采集，这可能既麻烦又耗时，但这项工作引入了一种可扩展的极化辅助方法，该方法采用了具有成本效益的采集工具。通过将线性偏振器连接到现成的RGB相机上，可以捕获多视图偏振图像，而不需要预先校准或精确测量偏振器角度，从而大大降低了系统建设成本。所提出的方法将极化BRDF、斯托克斯矢量和物体表面的极化状态表示为神经隐式场。通过优化输入偏振图像的渲染损失，结合偏振器角度，可以恢复这些场。通过利用偏振渲染的隐式表示的基本物理原理，我们的方法通过在公共数据集和真实捕获的图像中进行重建和新视图合成的实验，证明了其优于现有技术。 et.al.|[2504.07025](http://arxiv.org/abs/2504.07025)|null|

<p align=right>(<a href=#updated-on-20250415>back to top</a>)</p>

## 3D Reconstruction

|Publish Date|Title|Abstract|PDF|Code|
|---|---|---|---|---|
|**2025-04-14**|**LL-Gaussian: Low-Light Scene Reconstruction and Enhancement via Gaussian Splatting for Novel View Synthesis**|低光场景中的新型视图合成（NVS）仍然是一个重大挑战，因为输入质量下降，噪声严重，动态范围低（LDR），初始化不可靠。虽然最近基于NeRF的方法显示出有希望的结果，但大多数方法都存在计算成本高的问题，有些方法依赖于仔细捕获或预处理的数据，如RAW传感器输入或多次曝光序列，这严重限制了它们的实用性。相比之下，3D高斯散斑（3DGS）能够以具有竞争力的视觉保真度实现实时渲染；然而，现有的基于3DGS的方法在低光sRGB输入方面存在困难，导致高斯初始化不稳定和噪声抑制无效。为了应对这些挑战，我们提出了LL Gaussian，这是一种用于从低光sRGB图像进行3D重建和增强的新框架，实现了伪正常光新视图合成。我们的方法引入了三个关键创新：1）端到端的低光高斯初始化模块（LLGIM），该模块利用基于学习的MVS方法中的密集先验来生成高质量的初始点云；2） 双分支高斯分解模型，将固有场景属性（反射率和照度）与瞬态干扰分离，实现稳定和可解释的优化；3） 在联合引导分解和增强之前，由物理约束和扩散引导的无监督优化策略。此外，我们还提供了一个在极端低光环境中收集的具有挑战性的数据集，并展示了LL Gaussian的有效性。与最先进的基于NeRF的方法相比，LL Gaussian的推理速度提高了2000倍，训练时间缩短到2%，同时提供了卓越的重建和渲染质量。 et.al.|[2504.10331](http://arxiv.org/abs/2504.10331)|null|
|**2025-04-14**|**TT3D: Table Tennis 3D Reconstruction**|体育分析需要处理大量数据，这既费时又昂贵。神经网络的进步大大减轻了这一负担，在体育广播中实现了高度精确的球跟踪。然而，仅依赖2D球跟踪是有限的，因为它取决于相机的视点，并且不支持全面的游戏分析。为了解决这一局限性，我们提出了一种从在线乒乓球比赛记录中重建精确3D球轨迹的新方法。我们的方法利用球运动的基本物理特性来识别反弹状态，从而最大限度地减少球飞行轨迹的重投影误差，从而确保准确可靠的3D重建。我们的方法的一个关键优势是它能够推断球的旋转，而不依赖于人体姿势估计或球拍跟踪，而这些在广播镜头中通常是不可靠或不可用的。我们开发了一种能够可靠地跟踪相机运动的自动相机校准方法。此外，我们采用了一种现有的3D姿态估计模型，该模型缺乏深度运动捕捉，可以准确地跟踪玩家的动作。这些贡献共同实现了乒乓球拉力赛的完整3D重建。 et.al.|[2504.10035](http://arxiv.org/abs/2504.10035)|null|
|**2025-04-13**|**smFISH_batchRun: A smFISH image processing tool for single-molecule RNA Detection and 3D reconstruction**|随着显微镜方法的最新进展，单分子RNA成像已成为可能。然而，由于高度可变的背景噪声，即使在应用了复杂的计算清除方法后，对这些图像的系统分析也具有挑战性。在这里，我们描述了我们的定制MATLAB脚本，它使我们能够以单分子精度检测活性转录位点（ATS）的核新生转录本和成熟的细胞质mRNA，并在3D中重建组织以进行进一步分析。我们的编码最初针对秀丽隐杆线虫种系进行了优化，但被设计为广泛适用于其他物种和组织类型。 et.al.|[2504.09692](http://arxiv.org/abs/2504.09692)|null|
|**2025-04-13**|**TextSplat: Text-Guided Semantic Fusion for Generalizable Gaussian Splatting**|可泛化高斯散斑的最新进展通过利用前馈高斯散斑模型，实现了从稀疏输入视图进行稳健的3D重建，实现了卓越的跨场景泛化。然而，尽管许多方法侧重于几何一致性，但它们往往忽视了文本驱动引导在增强语义理解方面的潜力，而语义理解对于在复杂场景中准确重建细粒度细节至关重要。为了解决这一局限性，我们提出了TextSplat——第一个文本驱动的可泛化高斯散点框架。通过采用不同语义线索的文本引导融合，我们的框架学习了鲁棒的跨模态特征表示，改善了几何和语义信息的对齐，产生了高保真的3D重建。具体来说，我们的框架采用了三个并行模块来获得互补的表示：用于精确深度信息的扩散先验深度估计器、用于详细语义信息的语义感知分割网络和用于细化跨视图特征的多视图交互网络。然后，在文本引导语义融合模块中，这些表示通过文本引导和基于注意力的特征聚合机制进行集成，从而得到增强的3D高斯参数，并丰富了详细的语义线索。在各种基准数据集上的实验结果表明，与现有方法相比，在多个评估指标上的性能有所提高，验证了我们框架的有效性。代码将公开发布。 et.al.|[2504.09588](http://arxiv.org/abs/2504.09588)|null|
|**2025-04-12**|**A Constrained Optimization Approach for Gaussian Splatting from Coarsely-posed Images and Noisy Lidar Point Clouds**|3D高斯散斑（3DGS）是一种强大的重建技术，但它需要从精确的相机姿态和高保真点云进行初始化。通常，初始化来自运动结构（SfM）算法；然而，SfM耗时长，限制了3DGS在现实场景和大规模场景重建中的应用。我们介绍了一种不需要SfM支持的约束优化方法，用于同时进行相机姿态估计和3D重建。我们方法的核心是将相机姿态分解为一系列相机到（设备）中心和（设备）从中心到世界的优化。为了方便起见，我们提出了两个以每个参数组的灵敏度为条件的优化约束，并限制了每个参数的搜索空间。此外，当我们直接从嘈杂的点云中学习场景几何时，我们提出了几何约束来提高重建质量。实验表明，在我们收集的数据集和两个公共基准上，所提出的方法明显优于现有的（多模态）3DGS基线和COLMAP补充的方法。 et.al.|[2504.09129](http://arxiv.org/abs/2504.09129)|null|
|**2025-04-12**|**You Need a Transition Plane: Bridging Continuous Panoramic 3D Reconstruction with Perspective Gaussian Splatting**|最近，使用先进的3D高斯散斑（3DGS）技术从单个全景图像重建场景引起了越来越多的兴趣。全景图像提供360美元×180美元的视场（FoV），在一次拍摄中捕捉到整个场景。然而，全景图像引入了严重的失真，使得将3D高斯图像直接渲染到2D失真的等矩形空间中变得具有挑战性。将等矩形图像转换为立方体贴图投影在一定程度上缓解了这个问题，但也带来了新的挑战，例如投影失真和立方体面边界的不连续性。为了解决这些局限性，我们提出了一个名为TPGS的新框架，将连续全景3D场景重建与透视高斯飞溅联系起来。首先，我们在相邻立方体面之间引入一个过渡平面，以实现更平滑的飞溅方向过渡，并减轻边界区域的优化模糊性。此外，提出了一种面部内部到内部的优化策略，以增强局部细节并恢复立方体面部边界的视觉一致性。具体来说，我们优化单个立方体面内的3D高斯分布，然后在拼接的全景空间中对其进行微调。此外，我们引入了一种球形采样技术来消除可见的缝合缝。在室内和室外、以自我为中心和漫游基准数据集上进行的广泛实验表明，我们的方法优于现有的最先进的方法。代码和模型将在https://github.com/zhijieshen-bjtu/TPGS. et.al.|[2504.09062](http://arxiv.org/abs/2504.09062)|null|
|**2025-04-11**|**X2BR: High-Fidelity 3D Bone Reconstruction from a Planar X-Ray Image with Hybrid Neural Implicit Methods**|由于解剖结构的复杂性和输入数据的有限性，从单个平面X射线进行精确的3D骨重建仍然是一个挑战。我们提出了X2BR，这是一种混合神经隐式框架，将连续体积重建与模板引导的非刚性配准相结合。核心网络X2B采用基于ConvNeXt的编码器从X射线中提取空间特征，并预测高保真3D骨骼占用场，而不依赖于统计形状模型。为了进一步提高解剖精度，X2BR集成了一个基于YOLOv9的检测和SKEL生物力学骨架模型构建的患者特异性模板网格。使用基于测地线的相干点漂移将粗略重建与模板对齐，从而实现解剖学上一致的3D骨体积。临床数据集的实验结果表明，X2B达到了最高的数值精度，IoU为0.952，Chamfer-L1距离为0.005，优于包括X2V和D2IM-Net在内的最新基线。在此基础上，X2BR通过基于YOLOv9的骨检测和生物力学模板对齐结合了解剖先验，从而实现了重建，虽然IoU略低（0.875），但提供了卓越的解剖真实性，特别是在肋骨弯曲和椎体对齐方面。X2B和X2BR之间的数值精度与视觉一致性权衡突显了混合框架在临床相关3D重建中的价值。 et.al.|[2504.08675](http://arxiv.org/abs/2504.08675)|null|
|**2025-04-11**|**Digital Twin Catalog: A Large-Scale Photorealistic 3D Object Digital Twin Dataset**|我们介绍了数字孪生目录（DTC），这是一种新的大规模真实感3D对象数字孪生数据集。3D对象的数字孪生是对物理对象的高度详细、几乎无法区分的表示，准确捕捉其形状、外观、物理属性和其他属性。基于神经网络的3D重建和逆渲染的最新进展显著提高了3D对象重建的质量。尽管取得了这些进步，但仍然缺乏一个大规模的、数字孪生质量的真实世界数据集和基准，可以定量评估和比较不同重建方法的性能，并通过训练或微调来提高重建质量。此外，为了使3D数字双胞胎创作民主化，将创作技术与下一代以自我为中心的计算平台（如AR眼镜）相结合至关重要。目前，没有可用的数据集来评估使用以自我为中心的捕获图像进行3D对象重建。为了解决这些差距，DTC数据集包含2000个扫描的数字双质量3D对象，以及在不同光照条件下使用单反相机和自中心AR眼镜捕获的图像序列。该数据集为3D数字孪生创建任务建立了第一个全面的真实世界评估基准，为比较和改进现有的重建方法提供了坚实的基础。DTC数据集已于发布https://www.projectaria.com/datasets/dtc/我们还将使基线评估开源。 et.al.|[2504.08541](http://arxiv.org/abs/2504.08541)|null|
|**2025-04-14**|**PMNI: Pose-free Multi-view Normal Integration for Reflective and Textureless Surface Reconstruction**|反射和无纹理表面仍然是多视图3D重建中的一个挑战。由于交叉视图视觉特征不足或不可靠，相机姿态校准和形状重建经常失败。为了解决这些问题，我们提出了PMNI（无姿态多视图法线积分），这是一种神经表面重建方法，通过利用表面法线贴图而不是RGB图像来整合丰富的几何信息。通过在神经符号距离函数（SDF）优化框架内强制执行曲面法线的几何约束和多视图形状一致性，PMNI同时恢复了精确的相机姿态和高保真曲面几何。在合成和真实世界数据集上的实验结果表明，即使没有可靠的初始相机姿态，我们的方法在重建反射表面方面也达到了最先进的性能。 et.al.|[2504.08410](http://arxiv.org/abs/2504.08410)|null|
|**2025-04-10**|**Geo4D: Leveraging Video Generators for Geometric 4D Scene Reconstruction**|我们介绍了Geo4D，这是一种将视频扩散模型重新用于动态场景的单目3D重建的方法。通过利用这种视频模型捕获的强动态先验，可以仅使用合成数据来训练Geo4D，同时以零样本的方式将其很好地推广到真实数据。Geo4D预测了几种互补的几何形态，即点、深度和射线图。它使用一种新的多模态对齐算法在推理时对齐和融合这些模态以及多个滑动窗口，从而获得长视频的鲁棒和准确的4D重建。跨多个基准的广泛实验表明，Geo4D显著超越了最先进的视频深度估计方法，包括MonST3R等最新方法，这些方法也被设计用于处理动态场景。 et.al.|[2504.07961](http://arxiv.org/abs/2504.07961)|null|

<p align=right>(<a href=#updated-on-20250415>back to top</a>)</p>

## Diffusion

|Publish Date|Title|Abstract|PDF|Code|
|---|---|---|---|---|
|**2025-04-14**|**Decoupled Diffusion Sparks Adaptive Scene Generation**|可控的场景生成可以大大降低自动驾驶多样化数据收集的成本。先前的工作通过一次对整个序列进行去噪或迭代预测下一帧，将交通布局生成表述为预测性进展。然而，全序列去噪阻碍了在线反应，而后者的短视下一帧预测缺乏精确的目标状态指导。此外，由于开放数据集中存在大量安全有序的驾驶行为，学习模型难以生成复杂或具有挑战性的场景。为了克服这些问题，我们引入了Nexus，这是一个解耦的场景生成框架，通过从具有独立噪声状态的细粒度令牌中模拟有序和具有挑战性的场景来提高反应性和目标条件。解耦管道的核心是部分噪声掩蔽训练策略和噪声感知调度的集成，以确保在整个去噪过程中及时更新环境。为了补充具有挑战性的场景生成，我们收集了一个由复杂角案例组成的数据集。它涵盖了540小时的模拟数据，包括切入、突然制动和碰撞等高风险交互。Nexus在保持反应性和目标定向的同时实现了卓越的生成真实感，位移误差减少了40%。我们进一步证明，Nexus通过数据增强将闭环规划提高了20%，并展示了其在安全关键数据生成方面的能力。 et.al.|[2504.10485](http://arxiv.org/abs/2504.10485)|null|
|**2025-04-14**|**REPA-E: Unlocking VAE for End-to-End Tuning with Latent Diffusion Transformers**|在这篇论文中，我们解决了一个基本问题：“我们能否以端到端的方式与变分自动编码器（VAE）标记器一起训练潜在扩散模型？”传统的深度学习智慧表明，在可能的情况下，端到端训练通常更可取。然而，对于潜在的扩散变压器，观察到使用标准扩散损耗的VAE和扩散模型的端到端训练是无效的，甚至会导致最终性能的下降。我们表明，虽然扩散损失是无效的，但端到端的训练可以通过表示对齐（REPA）损失来解锁——允许在训练过程中联合调整VAE和扩散模型。尽管简单，但所提出的训练配方（REPA-E）显示出了显著的性能；将扩散模型训练速度分别提高了REPA和vanilla训练配方的17倍和45倍以上。有趣的是，我们观察到使用REPA-E进行端到端调优也改善了VAE本身；从而改善了潜在空间结构和下游发电性能。在最终性能方面，我们的方法设定了新的最先进水平；在ImageNet 256 x 256上，在无分类器引导和无分类器引导的情况下，实现了1.26和1.83的FID。代码可在以下网址获得https://end2end-diffusion.github.io. et.al.|[2504.10483](http://arxiv.org/abs/2504.10483)|null|
|**2025-04-14**|**Bayesian Analysis of Interpretable Aging across Thousands of Lithium-ion Battery Cycles**|Doyle Fuller-Newman（DFN）模型是锂离子电池的常见力学模型。DFN模型中的反应速率常数和扩散率是直接影响锂离子运动的关键参数，从而为电池老化提供了解释。这项工作研究了使用镍钴铝氧化物（NCA）阴极和氧化硅-石墨（LiC $_\text{6}$--SiO$_{x}$ ）阳极唯一估计95特斯拉Model 3电池的每个电极的扩散系数和反应速率常数的能力。在每个电池的生命周期内，以间歇诊断周期估算参数。在C/5、1C和2C的放电C速率下，使用马尔可夫链蒙特卡罗（MCMC）对总共7776个循环的不确定性量化（UQ）来估计这四个参数。虽然在每个电池的寿命期间，一个或多个阳极参数是唯一可识别的，但阴极参数在寿命中期到末期变得可识别，这表明阴极中可测量的电阻增长。关键参数对健康状态（SOH）的贡献表示为幂律。该SOH模型与每个电池在整个寿命期间进行的MCMC结果高度一致。我们的方法表明，通过预测导致细胞衰老的参数的轨迹，可以实现对衰老的有效诊断。因此，用基于DFN的更精确的物理模型扩展我们的分析可能会导致更多可识别的参数，并进一步改善老化预测。 et.al.|[2504.10439](http://arxiv.org/abs/2504.10439)|null|
|**2025-04-14**|**Anchor Token Matching: Implicit Structure Locking for Training-free AR Image Editing**|文本到图像生成在扩散模型方面取得了突破性的进展，通过交叉注意力操纵实现了高保真合成和精确的图像编辑。最近，自回归（AR）模型重新成为强大的替代品，利用下一代代币来匹配扩散模型。然而，由于结构控制的根本差异，为扩散模型设计的现有编辑技术无法直接转化为AR模型。具体来说，AR模型在图像编辑过程中存在注意力图的空间贫困和结构误差的顺序累积，这会破坏对象布局和全局一致性。在这项工作中，我们介绍了隐式结构锁定（ISLock），这是AR视觉模型的第一种无训练编辑策略。ISLock不依赖于显式的注意力操纵或微调，而是通过锚令牌匹配（ATM）协议将自我注意力模式与参考图像动态对齐，从而保留结构蓝图。通过隐式地强制潜在空间中的结构一致性，我们的方法ISLock实现了结构感知编辑，同时保持了生成自主性。大量实验表明，ISLock无需额外训练即可实现高质量、结构一致的编辑，并且优于或可与传统编辑技术相媲美。我们的研究结果开创了高效灵活的基于AR的图像编辑方法，进一步弥合了扩散和自回归生成模型之间的性能差距。该代码将在以下网址公开：https://github.com/hutaiHang/ATM et.al.|[2504.10434](http://arxiv.org/abs/2504.10434)|null|
|**2025-04-14**|**MonoDiff9D: Monocular Category-Level 9D Object Pose Estimation via Diffusion Model**|物体姿态估计是机器人理解和与环境交互的核心手段。对于这项任务，单眼类别级方法很有吸引力，因为它们只需要一个RGB相机。然而，当前的方法依赖于类内已知对象的形状先验或CAD模型。我们提出了一种基于扩散的单目类别级9D物体姿态生成方法MonoDiff9D。我们的动机是利用扩散模型的概率特性来减轻对形状先验、CAD模型或深度传感器的需求，以进行类内未知物体姿态估计。我们首先通过DINOv2以零样本的方式从单目图像估计粗略深度，并将其转换为点云。然后，我们将点云的全局特征与输入图像融合，并使用融合的特征和编码的时间步长来调节MonoDiff9D。最后，我们设计了一种基于变换器的去噪器，用于从高斯噪声中恢复物体姿态。在两个流行的基准数据集上进行的广泛实验表明，MonoDiff9D实现了最先进的单眼类别级9D对象姿态估计精度，在任何阶段都不需要形状先验或CAD模型。我们的代码将在https://github.com/CNJianLiu/MonoDiff9D. et.al.|[2504.10433](http://arxiv.org/abs/2504.10433)|null|
|**2025-04-14**|**Cosmogenic Neutrino Point Source and KM3-230213A**|宇宙中微子（CN）是由超高能宇宙射线（UHECR）与宇宙背景辐射相互作用产生的。我们通过假设UHECR源是瞬态事件，如伽马射线爆发，研究了CN点/扩展源的性质，即中微子谱和角轮廓随时间的变化。这些特性在很大程度上取决于星系间磁场（IGMF），但角度范围通常为亚度，在这个范围内，CN通量可以在早期超过扩散CN通量。未来的中微子望远镜可以探测到附近的CN点源，用于低IGMF情况。最近的KM3-230213A事件可能是由附近的瞬态CN源引起的，而不是由扩散的CN发射引起的。对CN点源的观测将为搜索UHECR源提供机会。 et.al.|[2504.10378](http://arxiv.org/abs/2504.10378)|null|
|**2025-04-14**|**Improving diffusion modeling in all-solid-state lithium batteries: a novel approach for grain boundary effects**|全固态锂离子电池在容量、安全性和性能方面具有很好的优势。锂离子在所含多晶固态电解质中的扩散行为对电池功能至关重要。虽然原子论研究表明晶界（GB）和晶粒尺寸显著影响扩散率，但相应的影响要么在更大尺度的模拟中被忽略，要么仅在各向同性等强假设下被考虑。我们的方法考虑了完全解析的晶体结构，其参数化与原子论视角相一致，以描述沿晶界和跨晶界的扩散。该方法被嵌入到有限元模拟中，使用基于厚度方向分析描述的新型折叠界面单元。结果受块体和GB域中不同且可能各向异性的扩散系数的控制。中尺度响应是使用线性计算均匀化来捕捉大尺度效应的。新颖的折叠界面描述允许在GB域内重建3D输运行为，而无需解析它，并且能够捕获相关的输运机制，如沟道效应和浓度跳跃。粒度和GB体积分数以仿射参数依赖性表示，可以在不改变几何形状或网格的情况下进行更改。结合观察到的有效材料响应对各向异性GB参数化的依赖性，这导致了四种不同的扩散机制的识别，每种机制都对电池材料的设计有影响。 et.al.|[2504.10348](http://arxiv.org/abs/2504.10348)|null|
|**2025-04-14**|**LL-Gaussian: Low-Light Scene Reconstruction and Enhancement via Gaussian Splatting for Novel View Synthesis**|低光场景中的新型视图合成（NVS）仍然是一个重大挑战，因为输入质量下降，噪声严重，动态范围低（LDR），初始化不可靠。虽然最近基于NeRF的方法显示出有希望的结果，但大多数方法都存在计算成本高的问题，有些方法依赖于仔细捕获或预处理的数据，如RAW传感器输入或多次曝光序列，这严重限制了它们的实用性。相比之下，3D高斯散斑（3DGS）能够以具有竞争力的视觉保真度实现实时渲染；然而，现有的基于3DGS的方法在低光sRGB输入方面存在困难，导致高斯初始化不稳定和噪声抑制无效。为了应对这些挑战，我们提出了LL Gaussian，这是一种用于从低光sRGB图像进行3D重建和增强的新框架，实现了伪正常光新视图合成。我们的方法引入了三个关键创新：1）端到端的低光高斯初始化模块（LLGIM），该模块利用基于学习的MVS方法中的密集先验来生成高质量的初始点云；2） 双分支高斯分解模型，将固有场景属性（反射率和照度）与瞬态干扰分离，实现稳定和可解释的优化；3） 在联合引导分解和增强之前，由物理约束和扩散引导的无监督优化策略。此外，我们还提供了一个在极端低光环境中收集的具有挑战性的数据集，并展示了LL Gaussian的有效性。与最先进的基于NeRF的方法相比，LL Gaussian的推理速度提高了2000倍，训练时间缩短到2%，同时提供了卓越的重建和渲染质量。 et.al.|[2504.10331](http://arxiv.org/abs/2504.10331)|null|
|**2025-04-14**|**Analysis of Attention in Video Diffusion Transformers**|我们对视频扩散变压器（VDiTs）中的注意力进行了深入分析，并报告了一些新发现。我们确定了VDiTs中注意力的三个关键属性：结构、稀疏性和下沉。结构：我们观察到，不同VDIT的注意力模式在不同提示下表现出相似的结构，我们可以利用注意力模式的相似性通过自我注意力图转移来解锁视频编辑。稀疏：我们研究了VDiTs中的注意力稀疏性，发现提出的稀疏方法并不适用于所有VDiTs，因为一些看似稀疏的层无法稀疏。水槽：我们首次研究了VDiTs中的注意水槽，将其与语言模型中的注意槽进行了比较和对比。我们提出了一些未来的方向，可以利用我们的见解来提高VDiT的效率质量帕累托前沿。 et.al.|[2504.10317](http://arxiv.org/abs/2504.10317)|null|
|**2025-04-14**|**DiffMOD: Progressive Diffusion Point Denoising for Moving Object Detection in Remote Sensing**|遥感中的运动目标检测（MOD）受到低分辨率、极小目标尺寸和复杂噪声干扰的严重挑战。当前基于深度学习的MOD方法依赖于概率密度估计，这限制了对象之间和跨时间帧的灵活信息交互。为了灵活捕捉高阶对象间和时间关系，我们提出了一种基于点的遥感MOD。受扩散模型的启发，网络优化被表述为一个渐进的去噪过程，该过程从稀疏的噪声点迭代地恢复运动对象中心。具体来说，我们从骨干输出中采样分散的特征作为原子单位进行后续处理，同时聚合全局特征嵌入以补偿稀疏点特征的有限覆盖范围。通过对空间相对位置和语义亲和性进行建模，空间关系聚合注意力旨在实现点级特征之间的高阶交互，以增强对象表示。为了提高时间一致性，设计了时间传播和全局融合模块，该模块利用隐式记忆推理机制进行鲁棒的跨帧特征集成。为了与渐进式去噪过程保持一致，我们提出了一种渐进式MinK最优传输分配策略，该策略在每个去噪级别建立了专门的学习目标。此外，我们引入了一个缺失损失函数来抵消显著对象周围去噪点的聚类趋势。在RsData遥感MOD数据集上的实验表明，我们基于散乱点去噪的MOD方法可以更有效地探索稀疏运动对象之间的潜在关系，提高检测能力和时间一致性。 et.al.|[2504.10278](http://arxiv.org/abs/2504.10278)|null|

<p align=right>(<a href=#updated-on-20250415>back to top</a>)</p>

## NeRF

|Publish Date|Title|Abstract|PDF|Code|
|---|---|---|---|---|
|**2025-04-14**|**DNF-Avatar: Distilling Neural Fields for Real-time Animatable Avatar Relighting**|从单眼视频中创建可重现和可动画化的人类化身是一个新兴的研究课题，具有广泛的应用，例如虚拟现实、体育和视频游戏。之前的研究利用神经场和基于物理的渲染（PBR）来估计人类化身的几何形状并解开其外观属性。然而，这些方法的一个缺点是由于昂贵的蒙特卡洛射线追踪导致渲染速度较慢。为了解决这个问题，我们提出将隐式神经场（教师）的知识提取为显式的2D高斯飞溅（学生）表示，以利用高斯飞溅的快速光栅化特性。为了避免光线追踪，我们对PBR外观采用了分裂和近似。我们还提出了用于阴影计算的新型部分式环境遮挡探头。阴影预测是通过每像素只查询一次这些探测器来实现的，这为化身的实时重新照明铺平了道路。这些技术相结合，可以提供高质量的重新照明效果和逼真的阴影效果。我们的实验表明，所提出的学生模型与我们的教师模型实现了相当甚至更好的重新照明结果，同时在推理时快了370倍，达到了67 FPS的渲染速度。 et.al.|[2504.10486](http://arxiv.org/abs/2504.10486)|null|
|**2025-04-11**|**SN-LiDAR: Semantic Neural Fields for Novel Space-time View LiDAR Synthesis**|最近的研究已经开始探索激光雷达点云的新颖视图合成（NVS），旨在从看不见的视点生成逼真的激光雷达扫描。然而，大多数现有的方法都不能重建语义标签，而语义标签对于自动驾驶和机器人感知等许多下游应用至关重要。与受益于强大分割模型的图像不同，LiDAR点云缺乏如此大规模的预训练模型，这使得语义标注既费时又费力。为了应对这一挑战，我们提出了SN LiDAR，这是一种联合执行精确语义分割、高质量几何重建和逼真LiDAR合成的方法。具体来说，我们采用从粗到细的平面网格特征表示来从多帧点云中提取全局特征，并利用基于CNN的编码器从当前帧点云中提取局部语义特征。SemanticKITTI和KITTI-360的大量实验证明了SN LiDAR在语义和几何重建方面的优越性，有效地处理了动态对象和大规模场景。代码将在https://github.com/dtc111111/SN-Lidar. et.al.|[2504.08361](http://arxiv.org/abs/2504.08361)|null|
|**2025-04-08**|**econSG: Efficient and Multi-view Consistent Open-Vocabulary 3D Semantic Gaussians**|最近关于开放词汇神经场的工作的主要重点是从VLM中提取精确的语义特征，然后将它们有效地整合到多视图一致的3D神经场表示中。然而，大多数现有的工作都是在受信任的SAM上进行的，以规范图像级CLIP，而无需进一步细化。此外，一些现有的研究通过在与3DGS语义场融合之前对2D VLM的语义特征进行降维来提高效率，这不可避免地导致了多视图不一致。在这项工作中，我们提出了使用3DGS进行开放式词汇语义分割的econSG。我们的econSG由以下部分组成：1）置信区间引导正则化（CRR），它相互细化SAM和CLIP，以获得具有完整和精确边界的精确语义特征的两全其美。2） 一个低维上下文空间，通过融合反投影的多视图2D特征来增强3D多视图一致性，同时提高计算效率，然后直接对融合的3D特征进行降维，而不是分别对每个2D视图进行操作。与现有方法相比，我们的econSG在四个基准数据集上显示了最先进的性能。此外，我们也是所有方法中最有效的培训。 et.al.|[2504.06003](http://arxiv.org/abs/2504.06003)|null|
|**2025-04-08**|**Meta-Continual Learning of Neural Fields**|神经场（NF）作为一种用于复杂数据表示的通用框架，已经获得了突出地位。这项工作揭示了一个新的问题设置，称为“神经场元连续学习”（MCL-NF），并引入了一种新的策略，该策略采用模块化架构与基于优化的元学习相结合。我们的策略侧重于克服现有神经场连续学习方法的局限性，如灾难性遗忘和缓慢收敛，实现了高质量的重建，显著提高了学习速度。我们进一步引入了神经辐射场的Fisher信息最大化损失（FIM-NeRF），它在样本级别最大化信息增益以增强学习泛化，并证明了收敛保证和泛化界限。我们在六个不同的数据集上对图像、音频、视频重建和视图合成任务进行了广泛的评估，证明了我们的方法在重建质量和速度方面优于现有的MCL和CL-NF方法。值得注意的是，我们的方法在降低参数要求的情况下，实现了神经场对城市级NeRF渲染的快速适应。 et.al.|[2504.05806](http://arxiv.org/abs/2504.05806)|null|
|**2025-04-06**|**Dynamic Neural Field Modeling of Visual Contrast for Perceiving Incoherent Looming**|Amari的动态神经场（DNF）框架提供了一种受大脑启发的方法来模拟神经元群的平均激活。利用单一领域，DNF已成为机器人应用中低能耗隐约感知模块的有前景的基础。然而，之前的DNF方法在检测不连贯或不一致的迫在眉睫的特征方面面临着重大挑战，这些特征在现实世界场景中很常见，例如雨天的碰撞检测。果蝇和蝗虫视觉系统的见解表明，编码ON/OFF视觉对比在增强迫在眉睫的选择性方面起着至关重要的作用。此外，横向激发机制可能会改善织机敏感神经元对连贯和非连贯刺激的反应。这些共同为改进迫在眉睫的感知模型提供了宝贵的指导。基于这些生物学证据，我们通过结合on/OFF视觉对比度的建模来扩展之前的单场DNF框架，每个对比度都由一个专用的DNF控制。使用归一化高斯核对每个ON/OFF对比场内的横向激励进行公式化，并将其输出整合到求和字段中以生成碰撞警报。实验评估表明，所提出的模型有效地解决了非相干逼近检测的挑战，并且明显优于最先进的蝗虫启发模型。它在各种刺激下表现出了强大的性能，包括合成雨效应，突显了它在复杂、嘈杂的环境中，在视觉线索不一致的情况下，具有可靠的隐约感知的潜力。 et.al.|[2504.04551](http://arxiv.org/abs/2504.04551)|null|
|**2025-04-03**|**A Physics-Informed Meta-Learning Framework for the Continuous Solution of Parametric PDEs on Arbitrary Geometries**|在这项工作中，我们引入了隐式有限算子学习（iFOL），用于任意几何上偏微分方程（PDE）的连续和参数解。我们提出了一种基于物理信息的编解码器网络，以建立连续参数和解空间之间的映射。解码器通过利用以潜在或特征码为条件的隐式神经场网络来构建参数解场。实例特定代码是通过基于二阶元学习技术的PDE编码过程导出的。在训练和推理中，在PDE编码和解码过程中，物理信息损失函数被最小化。iFOL以能量或加权残差形式表示损失函数，并使用从标准数值PDE方法导出的离散残差对其进行评估。这种方法在训练和推理过程中都会导致离散残差的反向传播。iFOL具有几个关键特性：（1）其独特的损失公式消除了以前在PDE的条件神经场算子学习中使用的传统编码过程-解码流水线的需要；（2） 它不仅提供精确的参数和连续场，而且提供参数梯度的解，而不需要额外的损失项或灵敏度分析；（3） 它可以有效地捕捉溶液中的尖锐不连续性；（4）它消除了对几何和网格的约束，使其适用于任意几何和空间采样（零样本超分辨率能力）。我们批判性地评估了这些特征，并分析了网络在稳态和瞬态PDE中推广到看不见的样本的能力。所提出的方法的整体性能是有希望的，证明了它适用于计算力学中一系列具有挑战性的问题。 et.al.|[2504.02459](http://arxiv.org/abs/2504.02459)|**[link](https://github.com/rezanajian/fol)**|
|**2025-04-01**|**Flow Matching on Lie Groups**|流匹配（FM）是一种最新的生成建模技术：我们的目标是学习如何从分布中采样{X}_1 $通过从某些分布中流动样本$\mathfrak{X}_0$很容易取样。关键技巧是，在$\mathfrak中对端点进行调节的同时，可以训练这个流场{X}_1$：给定终点，只需沿直线段移动到终点（Lipman等人，2022）。然而，直线段仅在欧几里德空间上定义良好。因此，Chen和Lipman（2023）将该方法推广到黎曼流形上的FM，用测地线或其谱近似代替线段。我们采取了另一种观点：我们通过用指数曲线代替线段来推广李群上的FM。这导致了许多矩阵李群的简单、内在和快速实现，因为所需的李群运算（积、逆、指数、对数）仅由相应的矩阵运算给出。然后，李群上的FM可用于生成建模，数据由特征集（在$\mathbb{R}^n$ 中）和姿势集（在某些李群中）组成，例如等变神经场的潜在码（Wessels等人，2025）。 et.al.|[2504.00494](http://arxiv.org/abs/2504.00494)|**[link](https://github.com/finnsherry/FlowMatching)**|
|**2025-03-29**|**NeuralGS: Bridging Neural Fields and 3D Gaussian Splatting for Compact 3D Representations**|3D高斯散点（3DGS）显示了卓越的质量和渲染速度，但有数百万的3D高斯分布和巨大的存储和传输成本。最近的3DGS压缩方法主要集中在压缩脚手架GS上，取得了令人印象深刻的性能，但增加了体素结构和复杂的编码和量化策略。在这篇论文中，我们的目标是开发一种简单而有效的方法，称为NeuralGS，它以另一种方式探索将原始3DGS压缩成紧凑的表示，而不需要体素结构和复杂的量化策略。我们的观察是，像NeRF这样的神经场可以用多层感知器（MLP）神经网络表示复杂的3D场景，只需要几兆字节。因此，NeuralGS有效地采用神经场表示来用MLP对3D高斯的属性进行编码，即使对于大规模场景，也只需要很小的存储空间。为了实现这一点，我们采用了一种聚类策略，并根据高斯的重要性得分作为拟合权重，为每个聚类用不同的微小MLP对高斯进行拟合。我们在多个数据集上进行实验，在不损害视觉质量的情况下实现了平均模型大小减少45倍。我们的方法在原始3DGS上的压缩性能与基于Scaffold GS的专用压缩方法相当，这表明了用神经场直接压缩原始3DGS的巨大潜力。 et.al.|[2503.23162](http://arxiv.org/abs/2503.23162)|null|
|**2025-03-27**|**Renormalization group analysis of noisy neural field**|大脑中的神经元在个体特性和与其他神经元的连接方面表现出极大的多样性。为了深入了解神经元多样性如何在大尺度上促进大脑动力学和功能，我们借鉴了复制方法的框架，该框架已成功应用于平衡统计力学中一大类具有淬灭噪声的问题。我们分析了Wilson Cowan模型的两个线性化版本，其随机系数在空间上是相关的。特别是：（A）神经元本身的性质是异质的，（B）它们的连接是各向异性的。在这两个模型中，淬火随机性的平均会产生额外的非线性。这些非线性在威尔逊重整化群的框架内进行了分析。我们发现，对于模型A，如果噪声的空间相关性随距离衰减，指数小于-2 $，则在大的空间尺度上，噪声的影响消失了。相比之下，对于模型B，只有当空间相关性以小于-1$ 的指数衰减时，噪声对神经元连接的影响才会消失。我们的计算还表明，在某些条件下，噪声的存在可能会在大尺度上产生类似行波的行为，尽管这一结果在微扰理论的高阶下是否仍然有效还有待观察。 et.al.|[2503.21605](http://arxiv.org/abs/2503.21605)|null|
|**2025-03-25**|**Thin-Shell-SfT: Fine-Grained Monocular Non-rigid 3D Surface Tracking with Neural Deformation Fields**|从单目RGB视频中重建高度可变形的表面（如布料）是一个具有挑战性的问题，没有任何解决方案可以提供一致和准确的细粒度表面细节恢复。为了解释环境的病态性，现有的方法使用具有统计、神经或物理先验的变形模型。它们还主要依赖于非自适应离散曲面表示（例如多边形网格），逐帧优化导致误差传播，并受到基于网格的可微渲染器梯度差的影响。因此，织物褶皱等精细表面细节往往无法以所需的精度恢复。针对这些局限性，我们提出了ThinShell SfT，这是一种用于非刚性3D跟踪的新方法，将表面表示为隐式和连续的时空神经场。我们采用基于基尔霍夫-洛夫模型的连续薄壳物理先验进行空间正则化，这与早期作品的离散化替代方案形成了鲜明对比。最后，我们利用3D高斯溅射将表面可微分地渲染到图像空间中，并根据合成原理分析优化变形。我们的薄壳SfT在定性和定量上都优于先前的工作，这要归功于我们的连续表面公式以及专门定制的模拟先验和表面诱导的3D高斯。请访问我们的项目页面https://4dqv.mpiinf.mpg.de/ThinShellSfT. et.al.|[2503.19976](http://arxiv.org/abs/2503.19976)|null|

<p align=right>(<a href=#updated-on-20250415>back to top</a>)</p>

[contributors-shield]: https://img.shields.io/github/contributors/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[contributors-url]: https://github.com/Vincentqyw/cv-arxiv-daily/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[forks-url]: https://github.com/Vincentqyw/cv-arxiv-daily/network/members
[stars-shield]: https://img.shields.io/github/stars/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[stars-url]: https://github.com/Vincentqyw/cv-arxiv-daily/stargazers
[issues-shield]: https://img.shields.io/github/issues/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[issues-url]: https://github.com/Vincentqyw/cv-arxiv-daily/issues

