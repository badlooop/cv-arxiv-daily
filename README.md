[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]

## Updated on 2025.04.18
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
|**2025-04-16**|**VGDFR: Diffusion-based Video Generation with Dynamic Latent Frame Rate**|基于扩散变换器（DiT）的生成模型在视频生成方面取得了显著成功。然而，它们固有的计算需求带来了巨大的效率挑战。在这篇论文中，我们利用了现实世界视频固有的时间不均匀性，观察到视频表现出动态信息密度，高运动片段比静态场景需要更大的细节保留。受这种时间不均匀性的启发，我们提出了VGDFR，这是一种无需训练的基于扩散的动态潜在帧率视频生成方法。VGDFR根据潜在空间内容的运动频率自适应地调整潜在空间中的元素数量，对低频段使用较少的令牌，同时保留高频段中的细节。具体来说，我们的主要贡献是：（1）用于DiT视频生成的动态帧率调度器，它自适应地为视频片段分配帧率。（2） 一种新的潜在空间帧合并方法，在合并低分辨率空间中的冗余表示之前，将潜在表示与其去噪对应物对齐。（3） 跨DiT层的旋转位置嵌入（RoPE）的偏好分析，为针对语义和局部信息捕获优化的定制RoPE策略提供信息。实验表明，VGDFR可以实现高达3倍的视频生成速度，同时质量下降最小。 et.al.|[2504.12259](http://arxiv.org/abs/2504.12259)|null|
|**2025-04-16**|**Modular-Cam: Modular Dynamic Camera-view Video Generation with LLM**|文本到视频生成利用提供的文本提示生成高质量的视频，由于最近扩散模型的发展而引起了越来越多的关注并取得了巨大的成功。现有的方法主要依赖于预训练的文本编码器来捕获语义信息，并与编码的文本提示进行交叉关注，以指导视频的生成。然而，当涉及到包含动态场景和多个相机视图变换的复杂提示时，这些方法无法将整体信息分解为单独的场景，也无法根据相应的相机视图平滑地更改场景。为了解决这些问题，我们提出了一种新的方法，即模块化凸轮。具体来说，为了更好地理解给定的复杂提示，我们利用一个大型语言模型来分析用户指令，并将它们与转换动作一起分解为多个场景。为了生成包含与给定相机视图匹配的动态场景的视频，我们将广泛使用的时间变换器纳入扩散模型，以确保单个场景内的连续性，并提出了CamOperator，这是一个基于模块化网络的模块，可以很好地控制相机的运动。此外，我们提出了AdaControlNet，它利用ControlNet来确保场景之间的一致性，并自适应地调整生成视频的色调。大量的定性和定量实验证明，我们提出的模块化摄像头具有生成多场景视频的强大能力，并且能够实现对摄像头运动的精细控制。生成的结果可在https://modular-cam.github.io. et.al.|[2504.12048](http://arxiv.org/abs/2504.12048)|null|
|**2025-04-17**|**Understanding Attention Mechanism in Video Diffusion Models**|文本到视频（T2V）合成模型，如OpenAI的Sora，因其能够从文本提示生成高质量视频而受到广泛关注。在基于扩散的T2V模型中，注意力机制是一个关键组成部分。然而，目前尚不清楚学习了哪些中间特征，以及T2V模型中的注意力块如何影响视频合成的各个方面，如图像质量和时间一致性。本文使用信息论方法对T2V模型的空间和时间注意力块进行了深入的扰动分析。我们的结果表明，时间和空间注意力图不仅影响视频的时间和布局，还影响时空元素的复杂性和合成视频的美学质量。值得注意的是，高熵注意力图通常是与卓越视频质量相关的关键元素，而低熵注意力图与视频的帧内结构相关。基于我们的研究结果，我们提出了两种提高视频质量和实现文本引导视频编辑的新方法。这些方法完全依赖于T2V模型中注意力矩阵的轻量级操作。通过跨多个数据集的实验评估，我们的方法的有效性和有效性得到了进一步验证。 et.al.|[2504.12027](http://arxiv.org/abs/2504.12027)|null|
|**2025-04-16**|**The Devil is in the Prompts: Retrieval-Augmented Prompt Optimization for Text-to-Video Generation**|在大规模数据集上训练的文本到视频（T2V）生成模型的演变取得了重大进展。然而，T2V生成模型对输入提示的敏感性突显了提示设计在影响生成结果中的关键作用。先前的研究主要依赖于大型语言模型（LLM）来将用户提供的提示与训练提示的分布相匹配，尽管没有包括提示词汇和句子结构细微差别的量身定制的指导。为此，我们介绍\textbf{RAPO}，一个新颖的\textbf{R}etrieval-\textbf{A}ugmented\textbf{P}rompt\textbf{O}ptimization为了解决LLM生成的提示可能产生的不准确和模糊细节。RAPO通过双优化分支对原始提示进行优化，选择更优的提示进行T2V生成。第一个分支使用从学习到的关系图中提取的各种修饰符来增强用户提示，通过微调的LLM对其进行细化，使其与训练提示的格式保持一致。相反，第二个分支根据定义良好的指令集，使用预训练的LLM重写幼稚提示。大量实验表明，RAPO可以有效地增强生成视频的静态和动态维度，证明了对用户提供的提示进行提示优化的重要性。项目网站：\href{https://whynothaha.github.io/Prompt_optimizer/RAPO.html}{GitHub}。 et.al.|[2504.11739](http://arxiv.org/abs/2504.11739)|null|
|**2025-04-16**|**EgoExo-Gen: Ego-centric Video Prediction by Watching Exo-centric Videos**|以第一人称视角生成视频在增强现实和具身智能领域具有广阔的应用前景。在这项工作中，我们探索了跨视图视频预测任务，在给定一个以外中心为中心的视频、相应的以自我为中心视频的第一帧和文本指令的情况下，目标是生成以自我为核心的视频的未来帧。受以自我为中心的视频中的手对象交互（HOI）代表当前演员的主要意图和行为这一概念的启发，我们提出了EgoExo-Gen，它明确地模拟了手对象动力学，用于跨视图视频预测。EgoExo-Gen由两个阶段组成。首先，我们设计了一个跨视图HOI掩码预测模型，通过建模时空自我-外部对应来预测未来自我框架中的HOI掩码。接下来，我们采用视频扩散模型，使用第一个自我帧和文本指令来预测未来的自我帧，同时将HOI掩码作为结构指导来提高预测质量。为了便于训练，我们开发了一个自动化管道，通过利用视觉基础模型为自我和外部视频生成伪HOI面具。大量实验表明，与之前在Ego-Exo4D和H2O基准数据集上的视频预测模型相比，我们提出的EgoExo-Gen具有更好的预测性能，HOI掩码显著改善了以自我为中心的视频中手和交互对象的生成。 et.al.|[2504.11732](http://arxiv.org/abs/2504.11732)|null|
|**2025-04-15**|**NormalCrafter: Learning Temporally Consistent Normals from Video Diffusion Priors**|表面法线估计是一系列计算机视觉应用的基石。尽管已经对静态图像场景进行了大量研究，但确保基于视频的正常估计中的时间一致性仍然是一个艰巨的挑战。我们提出NormalCrafter来利用视频扩散模型的固有时间先验，而不是仅仅用时间分量来增强现有的方法。为了确保跨序列的高保真正态估计，我们提出了语义特征正则化（SFR），它将扩散特征与语义线索对齐，鼓励模型专注于场景的内在语义。此外，我们引入了一种两阶段训练协议，该协议利用潜在和像素空间学习来保持空间精度，同时保持长时间上下文。广泛的评估证明了我们的方法的有效性，展示了从不同视频中生成具有复杂细节的时间一致的正常序列的卓越性能。 et.al.|[2504.11427](http://arxiv.org/abs/2504.11427)|null|
|**2025-04-15**|**VideoPanda: Video Panoramic Diffusion with Multi-view Attention**|高分辨率全景视频内容对于虚拟现实中的沉浸式体验至关重要，但收集起来并不容易，因为它需要专门的设备和复杂的相机设置。在这项工作中，我们介绍了VideoPanda，这是一种基于文本或单视图视频数据合成360度视频的新方法。VideoPanda利用多视图注意力层来增强视频扩散模型，使其能够生成一致的多视图视频，这些视频可以组合成沉浸式全景内容。VideoPanda使用两种条件联合训练：纯文本和单视图视频，并支持长视频的自回归生成。为了克服多视图视频生成的计算负担，我们随机对训练过程中使用的持续时间和相机视图进行子采样，并表明该模型能够优雅地推广到在推理过程中生成更多帧。对真实世界和合成视频数据集的广泛评估表明，与现有方法相比，VideoPanda在所有输入条件下生成了更逼真、更连贯的360度全景图。访问项目网站https://research-staging.nvidia.com/labs/toronto-ai/VideoPanda/为了获得结果。 et.al.|[2504.11389](http://arxiv.org/abs/2504.11389)|null|
|**2025-04-15**|**UniAnimate-DiT: Human Image Animation with Large-Scale Video Diffusion Transformer**|本报告介绍了UniAnimate DiT，这是一个先进的项目，利用开源Wan2.1模型的尖端和强大功能，实现一致的人体图像动画。具体来说，为了保持原始Wan2.1模型的稳健生成能力，我们实现了低秩自适应（LoRA）技术来微调一组最小的参数，从而显著降低了训练内存开销。设计了一种由多个堆叠的3D卷积层组成的轻量级姿态编码器，用于对驱动姿态的运动信息进行编码。此外，我们采用简单的级联操作将参考外观集成到模型中，并结合参考图像的姿态信息以增强姿态对齐。实验结果表明，我们的方法实现了视觉上呈现和时间上一致的高保真动画。经过480p（832x480）视频的训练，UniAnimate DiT展示了强大的泛化能力，可以在推理过程中无缝升级到720P（1280x720）。训练和推理代码可在以下网址公开获取https://github.com/ali-vilab/UniAnimate-DiT. et.al.|[2504.11289](http://arxiv.org/abs/2504.11289)|null|
|**2025-04-15**|**Taming Consistency Distillation for Accelerated Human Image Animation**|视频扩散模型推动了人类图像动画的最新进展，但它们对大量迭代去噪步骤的依赖导致了高推理成本和低速度。一个直观的解决方案是采用一致性模型，通过一致性蒸馏作为有效的加速范式。然而，在人类图像动画中简单地采用这种策略往往会导致质量下降，包括视觉模糊、运动退化和面部失真，特别是在动态区域。在这篇论文中，我们提出了DanceLCM方法，并辅以几项增强措施，以提高低阶状态下的视觉质量和运动连续性：（1）分段一致性蒸馏，带有辅助的轻量级头部，以结合来自真实视频延迟的监督，减轻了由单个完整轨迹生成引起的累积误差；（2） 以运动为中心的损失以运动区域为中心，以及明确注入面部保真度特征以提高面部真实性。大量的定性和定量实验表明，DanceLCM仅需2-4个推理步骤即可实现与最先进的视频扩散模型相当的结果，在不影响视频质量的情况下显著减轻了推理负担。代码和模型将公开。 et.al.|[2504.11143](http://arxiv.org/abs/2504.11143)|null|
|**2025-04-15**|**InterAnimate: Taming Region-aware Diffusion Model for Realistic Human Interaction Animation**|最近的视频生成研究主要集中在孤立的动作上，而手-脸交互等交互式动作基本上没有得到研究。这些交互对于新兴的生物特征认证系统至关重要，这些系统依赖于基于交互式运动的反欺骗方法。从安全角度来看，越来越需要大规模、高质量的交互式视频来训练和加强身份验证模型。在这项工作中，我们介绍了一种新的范式，用于制作逼真的手-脸交互动画。我们的方法同时学习时空接触动力学和生物力学上合理的变形效应，实现了自然交互，其中手部运动会引起解剖学上精确的面部变形，同时保持无碰撞接触。为了促进这项研究，我们提出了InterHF，这是一个大规模的人脸交互数据集，包含18种交互模式和90000个带注释的视频。此外，我们提出了InterAnimate，这是一种专门为交互动画设计的区域感知扩散模型。InterAnimate利用可学习的空间和时间延迟来有效地捕获动态交互先验，并集成了一种区域感知交互机制，将这些先验注入去噪过程。据我们所知，这项工作代表了首次大规模系统研究人脸交互的努力。定性和定量结果表明，InterAnimate制作了高度逼真的动画，树立了新的基准。代码和数据将公开以推进研究。 et.al.|[2504.10905](http://arxiv.org/abs/2504.10905)|null|

<p align=right>(<a href=#updated-on-20250418>back to top</a>)</p>

## 3D

|Publish Date|Title|Abstract|PDF|Code|
|---|---|---|---|---|
|**2025-04-15**|**3D Gabor Splatting: Reconstruction of High-frequency Surface Texture using Gabor Noise**|3D高斯飞溅在过去几年中在新颖视图合成领域经历了爆炸式的普及。使用高斯对辐射场的轻量级和可微分表示能够实现快速和高质量的重建和快速渲染。然而，重建具有高频表面纹理（例如细条纹）的对象需要许多细高斯核，因为从一个方向观察，每个高斯核只代表一种颜色。因此，例如，重建条纹图案至少需要高斯分布的条纹数量。我们提出了3D Gabor飞溅，它增强了高斯核，使用Gabor噪声来表示空间高频信号。Gabor核是高斯项和空间波动波函数的组合，使其适用于表示空间高频纹理。我们证明了我们的3D Gabor飞溅可以重建物体上的各种高频纹理。 et.al.|[2504.11003](http://arxiv.org/abs/2504.11003)|null|
|**2025-04-15**|**LL-Gaussian: Low-Light Scene Reconstruction and Enhancement via Gaussian Splatting for Novel View Synthesis**|低光场景中的新型视图合成（NVS）仍然是一个重大挑战，因为输入质量下降，噪声严重，动态范围低（LDR），初始化不可靠。虽然最近基于NeRF的方法显示出有希望的结果，但大多数方法都存在计算成本高的问题，有些方法依赖于仔细捕获或预处理的数据，如RAW传感器输入或多次曝光序列，这严重限制了它们的实用性。相比之下，3D高斯散斑（3DGS）能够以具有竞争力的视觉保真度实现实时渲染；然而，现有的基于3DGS的方法在低光sRGB输入方面存在困难，导致高斯初始化不稳定和噪声抑制无效。为了应对这些挑战，我们提出了LL Gaussian，这是一种用于从低光sRGB图像进行3D重建和增强的新框架，实现了伪正常光新视图合成。我们的方法引入了三个关键创新：1）端到端的低光高斯初始化模块（LLGIM），该模块利用基于学习的MVS方法中的密集先验来生成高质量的初始点云；2） 双分支高斯分解模型，将固有场景属性（反射率和照度）与瞬态干扰分离，实现稳定和可解释的优化；3） 在联合引导分解和增强之前，由物理约束和扩散引导的无监督优化策略。此外，我们还提供了一个在极端低光环境中收集的具有挑战性的数据集，并展示了LL Gaussian的有效性。与最先进的基于NeRF的方法相比，LL Gaussian的推理速度提高了2000倍，训练时间缩短到2%，同时提供了卓越的重建和渲染质量。 et.al.|[2504.10331](http://arxiv.org/abs/2504.10331)|null|
|**2025-04-14**|**EBAD-Gaussian: Event-driven Bundle Adjusted Deblur Gaussian Splatting**|虽然3D高斯散斑（3D-GS）实现了逼真的新颖视图合成，但其性能会随着运动模糊而降低。在快速运动或低光照条件下，现有的基于RGB的去模糊方法难以对曝光过程中的相机姿态和辐射变化进行建模，从而降低了重建精度。事件相机捕捉曝光过程中连续的亮度变化，可以有效地帮助建模运动模糊并提高重建质量。因此，我们提出了事件驱动的束调整去模糊高斯散斑（EBAD-Gaussian），它从事件流和严重模糊的图像中重建清晰的3D高斯分布。该方法在恢复曝光时间内的相机运动轨迹的同时，联合学习这些高斯参数。具体来说，我们首先通过在曝光时间内合成多个潜在的清晰图像来构建模糊损失函数，使真实模糊图像和合成模糊图像之间的差异最小化。然后，我们使用事件流来监控曝光期内任何时间潜在清晰图像之间的光强变化，补充RGB图像中丢失的光强动态变化。此外，我们基于基于事件的双积分（EDI）先验优化了中间曝光时间的潜在清晰图像，应用一致性约束来增强重建图像的细节和纹理信息。对合成数据集和真实世界数据集的广泛实验表明，EBAD-Gaussian可以在模糊图像和事件流输入的条件下实现高质量的3D场景重建。 et.al.|[2504.10012](http://arxiv.org/abs/2504.10012)|null|
|**2025-04-14**|**MCBlock: Boosting Neural Radiance Field Training Speed by MCTS-based Dynamic-Resolution Ray Sampling**|神经辐射场（NeRF）因其高保真的新颖视图合成而广为人知。然而，即使是最先进的NeRF模型Gaussian Splatting也需要几分钟的训练时间，远低于远程医疗等多媒体场景所需的实时性能。其中一个障碍是采样效率低下，现有工作仅部分解决了这一问题。现有的点采样算法均匀地采样简单纹理区域（易于拟合）和复杂纹理区域（难以拟合），而现有的光线采样算法则以最精细的粒度（即像素级）对这些区域进行采样，这都浪费了GPU训练资源。实际上，具有不同纹理强度的区域需要不同的采样粒度。为此，我们提出了一种新的动态分辨率射线采样算法MCBlock，该算法采用蒙特卡洛树搜索（MCTS）将每个训练图像划分为不同大小的像素块，用于主动逐块训练。具体来说，根据训练图像的纹理对树进行初始化，以提高初始化速度，扩展/修剪模块动态优化块划分。MCBlock在开源工具集Nerfstudio中实现，训练加速高达2.33倍，超过了其他射线采样算法。我们相信MCBlock可以应用于任何锥体追踪NeRF模型，并为多媒体社区做出贡献。 et.al.|[2504.09878](http://arxiv.org/abs/2504.09878)|null|
|**2025-04-13**|**DropoutGS: Dropping Out Gaussians for Better Sparse-view Rendering**|尽管3D高斯散斑（3DGS）在新颖的视图合成中显示出有前景的结果，但其性能会随着稀疏输入而急剧下降，并产生不希望的伪影。随着训练视图数量的减少，新的视图合成任务会退化为一个高度不确定的问题，导致现有方法存在臭名昭著的过拟合问题。有趣的是，我们观察到高斯基元较少的模型在稀疏输入下表现出较少的过拟合。受这一观察的启发，我们提出了一种随机丢弃正则化（RDR）来利用低复杂度模型的优点来缓解过拟合。此外，为了弥补这些模型缺乏高频细节的问题，开发了一种边缘引导的分割策略（ESS）。通过这两种技术，我们的方法（称为DropoutGS）提供了一种简单而有效的插件方法来提高现有3DGS方法的泛化性能。广泛的实验表明，我们的DropoutGS在包括Blender、LLFF和DTU在内的基准数据集的稀疏视图下产生了最先进的性能。项目页面位于：https://xuyx55.github.io/DropoutGS/. et.al.|[2504.09491](http://arxiv.org/abs/2504.09491)|null|
|**2025-04-15**|**BlockGaussian: Efficient Large-Scale Scene Novel View Synthesis via Adaptive Block-Based Gaussian Splatting**|3D高斯散斑（3DGS）的最新进展在新的视图合成任务中显示出巨大的潜力。分而治之范式实现了大规模场景重建，但在场景分割、优化和合并过程中仍然存在重大挑战。本文介绍了BlockGaussian，这是一种新的框架，结合了内容感知场景分割策略和可见性感知块优化，以实现高效、高质量的大规模场景重建。具体来说，我们的方法考虑了不同区域之间的内容复杂度变化，并在场景分割过程中平衡了计算负载，从而实现了高效的场景重建。为了解决独立块优化中的监督不匹配问题，我们在单个块优化中引入了辅助点来对齐地面真实监督，从而提高了重建质量。此外，我们提出了一种伪视图几何约束，有效地减轻了块合并过程中空域浮动导致的渲染质量下降。大规模场景上的大量实验表明，我们的方法在重建效率和渲染质量方面都达到了最先进的性能，优化速度提高了5倍，在多个基准测试中平均PSNR提高了1.21dB。值得注意的是，BlockGaussian显著降低了计算要求，可以在单个24GB VRAM设备上进行大规模场景重建。项目页面可在https://github.com/SunshineWYC/BlockGaussian et.al.|[2504.09048](http://arxiv.org/abs/2504.09048)|null|
|**2025-04-11**|**Cut-and-Splat: Leveraging Gaussian Splatting for Synthetic Data Generation**|生成合成图像是一种廉价获取标记数据以训练计算机视觉模型的有用方法。然而，获得相关对象的精确3D模型是必要的，由于模拟照明效果和相机伪影的挑战，最终的图像在真实感方面往往存在差距。我们建议使用称为高斯散斑的新颖视图合成方法来解决这些挑战。我们开发了一个合成数据管道，用于为特定对象生成高质量的上下文感知实例分割训练数据。这个过程是完全自动化的，只需要目标对象的视频。我们训练目标对象的高斯散斑模型，并自动从视频中提取对象。利用高斯散斑，我们然后在随机背景图像上渲染对象，并采用单目深度估计将对象放置在可信的姿势中。我们引入了一个新的数据集来验证我们的方法，并显示出比其他数据生成方法（如剪切粘贴和扩散模型生成）更优越的性能。 et.al.|[2504.08473](http://arxiv.org/abs/2504.08473)|**[link](https://github.com/edm-research/cut-and-splat)**|
|**2025-04-11**|**SN-LiDAR: Semantic Neural Fields for Novel Space-time View LiDAR Synthesis**|最近的研究已经开始探索激光雷达点云的新颖视图合成（NVS），旨在从看不见的视点生成逼真的激光雷达扫描。然而，大多数现有的方法都不能重建语义标签，而语义标签对于自动驾驶和机器人感知等许多下游应用至关重要。与受益于强大分割模型的图像不同，LiDAR点云缺乏如此大规模的预训练模型，这使得语义标注既费时又费力。为了应对这一挑战，我们提出了SN LiDAR，这是一种联合执行精确语义分割、高质量几何重建和逼真LiDAR合成的方法。具体来说，我们采用从粗到细的平面网格特征表示来从多帧点云中提取全局特征，并利用基于CNN的编码器从当前帧点云中提取局部语义特征。SemanticKITTI和KITTI-360的大量实验证明了SN LiDAR在语义和几何重建方面的优越性，有效地处理了动态对象和大规模场景。代码将在https://github.com/dtc111111/SN-Lidar. et.al.|[2504.08361](http://arxiv.org/abs/2504.08361)|**[link](https://github.com/dtc111111/sn-lidar)**|
|**2025-04-11**|**Geometric Consistency Refinement for Single Image Novel View Synthesis via Test-Time Adaptation of Diffusion Models**|单图像新视图合成（NVS）的扩散模型可以生成高度逼真和合理的图像，但它们在给定相对姿态的几何一致性方面受到限制。生成的图像通常显示出与目标姿态给出的应满足的极线约束相关的显著误差。本文通过提出一种方法来提高单图像NVS扩散模型生成的图像的几何正确性，从而解决了这个问题。我们基于图像匹配和极线约束制定了一个损失函数，并优化了扩散采样过程中的起始噪声，使生成的图像既能是真实的图像，又能满足从给定目标姿态导出的几何约束。我们的方法不需要训练数据或对扩散模型进行微调，我们表明我们可以将其应用于单幅图像NVS的多个最先进的模型。该方法在MegaScenes数据集上进行了评估，我们表明，与基线模型相比，几何一致性得到了改善，同时保留了生成图像的质量。 et.al.|[2504.08348](http://arxiv.org/abs/2504.08348)|null|
|**2025-04-10**|**InteractAvatar: Modeling Hand-Face Interaction in Photorealistic Avatars with Deformable Gaussians**|随着社区对数字化身的兴趣日益浓厚，加上表情和手势在交流中的重要性，在电话会议、游戏和AR/VR等许多行业中，对自然化身行为进行建模仍然是一个重要的挑战。人的手是与环境交互的主要工具，对于逼真的人类行为建模至关重要，但现有的3D手和头部化身模型往往忽视了手与身体交互的关键方面，例如手与脸之间的交互。我们提出了InteractitAvatar，这是第一个忠实地捕捉动态手和非刚性手-脸交互的照片级真实感外观的模型。我们的新型动态高斯手模型结合了模板模型和3D高斯散布以及动态细化模块，捕捉了姿势相关的变化，例如关节运动过程中出现的细皱纹和复杂阴影。重要的是，我们的人脸交互模块模拟了常见手势背后的微妙几何形状和外观动态。通过新颖的视图合成、自再现和跨身份再现实验，我们证明了InteractitAvatar可以从单目或多视点视频中重建手和手脸交互，具有高保真的细节，并可以用新颖的姿势进行动画制作。 et.al.|[2504.07949](http://arxiv.org/abs/2504.07949)|null|

<p align=right>(<a href=#updated-on-20250418>back to top</a>)</p>

## 3D Reconstruction

|Publish Date|Title|Abstract|PDF|Code|
|---|---|---|---|---|
|**2025-04-16**|**SHeaP: Self-Supervised Head Geometry Predictor Learned via 2D Gaussians**|从单眼图像和视频中准确、实时地重建人类头部是众多视觉应用的基础。由于3D地面实况数据很难大规模获得，以前的方法试图以自我监督的方式从丰富的2D视频中学习。通常，这涉及使用可微分网格渲染，这是有效的，但存在局限性。为了改进这一点，我们提出了SHeaP（通过2D高斯学习的自监督头部几何预测器）。给定一个源图像，我们预测一个3DMM网格和一组被装配到该网格的高斯分布。然后，我们重新激活这个被操纵的头部化身，以匹配目标帧，并将光度损失反向传播到3DMM和高斯预测网络。我们发现，使用高斯进行渲染大大提高了这种自监督方法的有效性。仅在2D数据上进行训练，我们的方法在中性人脸的NoW基准和非中性表情的新基准上的几何评估方面超越了现有的自监督方法。我们的方法还产生了高表现力的网格，在情感分类方面表现优于最先进的技术。 et.al.|[2504.12292](http://arxiv.org/abs/2504.12292)|null|
|**2025-04-16**|**Mind2Matter: Creating 3D Models from EEG Signals**|从脑信号重建三维物体在脑机接口（BCI）研究中受到了广泛关注。由于其出色的空间分辨率，目前的研究主要利用功能性磁共振成像（fMRI）进行3D重建任务。然而，fMRI的临床应用受到其高昂成本和无法支持实时操作的限制。相比之下，脑电图（EEG）作为一种经济实惠、非侵入性和移动的实时脑机交互系统解决方案，具有明显的优势。尽管深度学习的最新进展使神经数据图像生成取得了显著进展，但将EEG信号解码为结构化的3D表示在很大程度上仍未得到探索。在这篇论文中，我们提出了一种新的框架，通过利用神经解码技术和生成模型将EEG记录转换为3D对象重建。我们的方法包括训练EEG编码器以提取时空视觉特征，微调大型语言模型以将这些特征解释为描述性多模态输出，并利用具有布局引导控制的生成性3D高斯来合成最终的3D结构。实验表明，我们的模型捕捉到了显著的几何和语义特征，为脑机接口（BCI）、虚拟现实和神经假体的应用铺平了道路。我们的代码可以在https://github.com/sddwwww/Mind2Matter. et.al.|[2504.11936](http://arxiv.org/abs/2504.11936)|null|
|**2025-04-15**|**Deep Learning-based Bathymetry Retrieval without In-situ Depths using Remote Sensing Imagery and SfM-MVS DSMs with Data Gaps**|准确、详细和高频的测深对于面临强烈气候和人为压力的浅海底区域至关重要。目前利用机载或卫星光学图像进行测深的方法主要依赖于具有折射校正的SfM MVS或光谱衍生测深（SDB）。然而，SDB方法通常需要大量的人工实地考察或昂贵的参考数据，而SfM MVS方法即使在折射校正后也面临着挑战。这些包括具有均匀视觉纹理的环境中的深度数据间隙和噪声，这阻碍了海底准确和完整的数字表面模型（DSM）的创建。为了应对这些挑战，这项工作引入了一种方法，该方法将SfM MVS方法的高保真3D重建能力与最先进的折射校正技术相结合，以及一种新的基于深度学习的测深预测方法的光谱分析能力。这种集成实现了一种协同方法，其中使用具有数据差距的SfM MVS衍生的DSM作为训练数据来生成完整的测深图。在此背景下，我们提出了Swin BathyUNet，它将U-Net与Swin Transformer的自我关注层和专门为SDB量身定制的交叉关注机制相结合。Swin BathyUNet旨在通过捕获长距离空间关系来提高测深精度，也可以作为具有各种训练深度数据的标准SDB的独立解决方案，独立于SfM MVS输出。地中海和波罗的海两个完全不同的测试地点的实验结果通过广泛的实验证明了所提出方法的有效性，这些实验证明了预测的DSM在测深精度、细节、覆盖范围和降噪方面的改进。该代码可在以下网址获得https://github.com/pagraf/Swin-BathyUNet. et.al.|[2504.11416](http://arxiv.org/abs/2504.11416)|null|
|**2025-04-15**|**Explicit and Implicit Representations in AI-based 3D Reconstruction for Radiology: A systematic literature review**|临床实践和辅助诊断对高质量医学成像的需求使放射学成像中的3D重建成为一个关键的研究重点。人工智能（AI）已成为一种有前景的方法，可以提高重建精度，同时减少采集和处理时间，从而最大限度地减少患者的辐射暴露和不适，最终有利于临床诊断。本文探讨了放射学成像中最先进的基于人工智能的3D重建算法，根据其基本原理将其分为显式和隐式方法。显式方法包括基于点、基于体积和高斯表示，而隐式方法包括隐式先验嵌入和神经辐射场。此外，我们还研究了常用的评估指标和基准数据集。最后，我们讨论了这一不断发展的领域的发展现状、关键挑战和未来的研究方向。我们的项目可在以下网址获得：https://github.com/Bean-Young/AI4Med. et.al.|[2504.11349](http://arxiv.org/abs/2504.11349)|null|
|**2025-04-15**|**Super time-resolved tomography**|了解3D基本过程对于学术和工业应用至关重要。如今，X射线时间分辨断层扫描或断层扫描是原位和操作4D（3D+时间）表征的领先技术。尽管它能够在大型X射线设施中实现每秒1000张断层图像，但其适用性受到施加在样品上的离心力以及为这种高速研究开发合适环境的挑战的限制。在这里，我们介绍STRT，这是一种有可能将断层扫描的时间分辨率提高至少一个数量级，同时保持空间分辨率的方法。STRT利用4D DL重建算法在每个时间点产生高保真3D重建，与传统断层扫描的0-180度相比，从显著减小的几度角度范围内检索。因此，与断层扫描相比，STRT将时间分辨率提高了一倍，等于180度与STRT使用的角度范围之间的比率。在这项工作中，我们通过液滴碰撞模拟和增材制造工艺的模拟和实验验证了STRT的4D能力。我们预计STRT将显著扩展4D X射线成像的能力，使以前在学术和工业环境中无法实现的研究成为可能，如材料形成和机械测试。 et.al.|[2504.11148](http://arxiv.org/abs/2504.11148)|null|
|**2025-04-15**|**Easy3D: A Simple Yet Effective Method for 3D Interactive Segmentation**|数字3D环境的可用性越来越高，无论是通过基于图像的3D重建、生成还是机器人获得的扫描，都在推动各种应用的创新。这些都伴随着对3D交互的巨大需求，例如3D交互式分割，这对对象选择和操纵等任务很有用。此外，人们一直需要高效、精确且在各种环境中表现良好的解决方案，特别是在看不见的环境和不熟悉的物体中。在这项工作中，我们介绍了一种3D交互式分割方法，该方法在域内和域外数据集上始终超越了以前最先进的技术。我们的简单方法将基于体素的稀疏编码器与基于轻量级变换器的解码器集成在一起，该解码器实现了隐式点击融合，实现了卓越的性能并最大限度地提高了效率。我们的方法在基准数据集（包括ScanNet、ScanNet++、S3DIS和KITTI-360）上以及在看不见的几何分布（如高斯散斑法获得的分布）上都有实质性的改进。项目网页可在https://simonelli-andrea.github.io/easy3d. et.al.|[2504.11024](http://arxiv.org/abs/2504.11024)|null|
|**2025-04-15**|**ZeroGrasp: Zero-Shot Shape Reconstruction Enabled Robotic Grasping**|机器人抓取是实体系统的基石能力。许多方法直接从部分信息中输出抓取，而不建模场景的几何形状，导致次优运动甚至碰撞。为了解决这些问题，我们引入了ZeroGrasp，这是一种新颖的框架，可以近乎实时地同时执行3D重建和抓取姿态预测。我们方法的一个关键见解是，遮挡推理和对对象之间的空间关系进行建模有利于精确重建和抓取。我们将我们的方法与一个新的大规模合成数据集相结合，该数据集包括来自Objaverse LVIS数据集的12K个对象的1M照片级逼真图像、高分辨率3D重建和11.3B物理有效的抓取姿势注释。我们在GraspNet-1B基准上以及通过现实世界的机器人实验对ZeroGrasp进行了评估。ZeroGrasp通过利用合成数据实现了最先进的性能，并推广到新的现实世界对象。 et.al.|[2504.10857](http://arxiv.org/abs/2504.10857)|null|
|**2025-04-15**|**LL-Gaussian: Low-Light Scene Reconstruction and Enhancement via Gaussian Splatting for Novel View Synthesis**|低光场景中的新型视图合成（NVS）仍然是一个重大挑战，因为输入质量下降，噪声严重，动态范围低（LDR），初始化不可靠。虽然最近基于NeRF的方法显示出有希望的结果，但大多数方法都存在计算成本高的问题，有些方法依赖于仔细捕获或预处理的数据，如RAW传感器输入或多次曝光序列，这严重限制了它们的实用性。相比之下，3D高斯散斑（3DGS）能够以具有竞争力的视觉保真度实现实时渲染；然而，现有的基于3DGS的方法在低光sRGB输入方面存在困难，导致高斯初始化不稳定和噪声抑制无效。为了应对这些挑战，我们提出了LL Gaussian，这是一种用于从低光sRGB图像进行3D重建和增强的新框架，实现了伪正常光新视图合成。我们的方法引入了三个关键创新：1）端到端的低光高斯初始化模块（LLGIM），该模块利用基于学习的MVS方法中的密集先验来生成高质量的初始点云；2） 双分支高斯分解模型，将固有场景属性（反射率和照度）与瞬态干扰分离，实现稳定和可解释的优化；3） 在联合引导分解和增强之前，由物理约束和扩散引导的无监督优化策略。此外，我们还提供了一个在极端低光环境中收集的具有挑战性的数据集，并展示了LL Gaussian的有效性。与最先进的基于NeRF的方法相比，LL Gaussian的推理速度提高了2000倍，训练时间缩短到2%，同时提供了卓越的重建和渲染质量。 et.al.|[2504.10331](http://arxiv.org/abs/2504.10331)|null|
|**2025-04-14**|**TT3D: Table Tennis 3D Reconstruction**|体育分析需要处理大量数据，这既费时又昂贵。神经网络的进步大大减轻了这一负担，在体育广播中实现了高度精确的球跟踪。然而，仅依赖2D球跟踪是有限的，因为它取决于相机的视点，并且不支持全面的游戏分析。为了解决这一局限性，我们提出了一种从在线乒乓球比赛记录中重建精确3D球轨迹的新方法。我们的方法利用球运动的基本物理特性来识别反弹状态，从而最大限度地减少球飞行轨迹的重投影误差，从而确保准确可靠的3D重建。我们的方法的一个关键优势是它能够推断球的旋转，而不依赖于人体姿势估计或球拍跟踪，而这些在广播镜头中通常是不可靠或不可用的。我们开发了一种能够可靠地跟踪相机运动的自动相机校准方法。此外，我们采用了一种现有的3D姿态估计模型，该模型缺乏深度运动捕捉，可以准确地跟踪玩家的动作。这些贡献共同实现了乒乓球拉力赛的完整3D重建。 et.al.|[2504.10035](http://arxiv.org/abs/2504.10035)|null|
|**2025-04-13**|**smFISH_batchRun: A smFISH image processing tool for single-molecule RNA Detection and 3D reconstruction**|随着显微镜方法的最新进展，单分子RNA成像已成为可能。然而，由于高度可变的背景噪声，即使在应用了复杂的计算清除方法后，对这些图像的系统分析也具有挑战性。在这里，我们描述了我们的定制MATLAB脚本，它使我们能够以单分子精度检测活性转录位点（ATS）的核新生转录本和成熟的细胞质mRNA，并在3D中重建组织以进行进一步分析。我们的编码最初针对秀丽隐杆线虫种系进行了优化，但被设计为广泛适用于其他物种和组织类型。 et.al.|[2504.09692](http://arxiv.org/abs/2504.09692)|null|

<p align=right>(<a href=#updated-on-20250418>back to top</a>)</p>

## Diffusion

|Publish Date|Title|Abstract|PDF|Code|
|---|---|---|---|---|
|**2025-04-16**|**How Do I Do That? Synthesizing 3D Hand Motion and Contacts for Everyday Interactions**|我们解决了在给定单个RGB视图、动作文本和对象上的3D接触点作为输入的情况下预测3D手部运动和接触图（或交互轨迹）的新问题。我们的方法包括：（1）交互码本：一个VQVAE模型，用于学习手部姿势和接触点的潜在码本，有效地标记交互轨迹；（2）交互预测器：一个转换器-解码器模块，通过使用索引器模块从学习的码本中检索潜在的启示，从测试时间输入中预测交互轨迹。为了训练我们的模型，我们开发了一个数据引擎，从各种HoloAssist数据集中提取3D手部姿势和接触轨迹。我们在一个比现有作品大2.5-10倍的基准上评估我们的模型，在观察到的对象和交互的多样性方面，并测试模型在对象类别、动作类别、任务和场景中的泛化能力。实验结果表明，我们的方法在所有设置下的变压器和扩散基线上都是有效的。 et.al.|[2504.12284](http://arxiv.org/abs/2504.12284)|null|
|**2025-04-16**|**VGDFR: Diffusion-based Video Generation with Dynamic Latent Frame Rate**|基于扩散变换器（DiT）的生成模型在视频生成方面取得了显著成功。然而，它们固有的计算需求带来了巨大的效率挑战。在这篇论文中，我们利用了现实世界视频固有的时间不均匀性，观察到视频表现出动态信息密度，高运动片段比静态场景需要更大的细节保留。受这种时间不均匀性的启发，我们提出了VGDFR，这是一种无需训练的基于扩散的动态潜在帧率视频生成方法。VGDFR根据潜在空间内容的运动频率自适应地调整潜在空间中的元素数量，对低频段使用较少的令牌，同时保留高频段中的细节。具体来说，我们的主要贡献是：（1）用于DiT视频生成的动态帧率调度器，它自适应地为视频片段分配帧率。（2） 一种新的潜在空间帧合并方法，在合并低分辨率空间中的冗余表示之前，将潜在表示与其去噪对应物对齐。（3） 跨DiT层的旋转位置嵌入（RoPE）的偏好分析，为针对语义和局部信息捕获优化的定制RoPE策略提供信息。实验表明，VGDFR可以实现高达3倍的视频生成速度，同时质量下降最小。 et.al.|[2504.12259](http://arxiv.org/abs/2504.12259)|null|
|**2025-04-16**|**Cobra: Efficient Line Art COlorization with BRoAder References**|漫画制作行业需要基于参考的线条艺术着色，具有高精度、高效率、上下文一致性和灵活的控制。漫画页面通常涉及不同的人物、物体和背景，这使着色过程变得复杂。尽管图像生成的扩散模型取得了进步，但它们在线条艺术着色中的应用仍然有限，面临着处理大量参考图像、耗时推理和灵活控制等挑战。我们研究了广泛的语境图像引导对线条艺术着色质量的必要性。为了应对这些挑战，我们引入了Cobra，这是一种高效且通用的方法，支持颜色提示，并利用200多个参考图像，同时保持低延迟。Cobra的核心是因果稀疏DiT架构，它利用专门设计的位置编码、因果稀疏注意力和键值缓存来有效地管理长上下文引用并确保颜色标识的一致性。结果表明，Cobra通过广泛的上下文参考实现了精确的线条艺术着色，显著提高了推理速度和交互性，从而满足了关键的工业需求。我们在项目页面上发布代码和模型：https://zhuang2002.github.io/Cobra/. et.al.|[2504.12240](http://arxiv.org/abs/2504.12240)|null|
|**2025-04-16**|**Coding-Prior Guided Diffusion Network for Video Deblurring**|虽然最近的视频去模糊方法取得了显著进展，但它们往往忽略了两个有价值的先验信息：（1）来自视频编解码器的运动矢量（MV）和编码残差（CR），它们提供了有效的帧间对齐线索，以及（2）预训练的扩散生成模型中嵌入的丰富的现实世界知识。我们提出了CPGDNet，这是一种新颖的两阶段框架，有效地利用编码先验和生成扩散先验进行高质量的去模糊。首先，我们的编码先验特征传播（CPFP）模块利用MV进行高效的帧对齐，并利用CR生成注意掩码，解决了运动不准确和纹理变化的问题。其次，编码先验控制生成（CPC）模块网络将编码先验集成到预训练扩散模型中，引导其增强关键区域并合成现实细节。实验证明，我们的方法实现了最先进的感知质量，IQA指标提高了30%。代码和codingprior增强数据集都将开源。 et.al.|[2504.12222](http://arxiv.org/abs/2504.12222)|null|
|**2025-04-16**|**d1: Scaling Reasoning in Diffusion Large Language Models via Reinforcement Learning**|最近的大型语言模型（LLM）已经证明了强大的推理能力，这得益于在线强化学习（RL）。这些能力主要在左右自回归（AR）生成范式中得到了证明。相比之下，基于扩散的非自回归范式以从粗到细的方式生成文本。尽管最近基于扩散的大型语言模型（dLLM）与AR模型相比取得了具有竞争力的语言建模性能，但目前尚不清楚dLLM是否也能利用LLM推理的最新进展。为此，我们提出了d1，这是一个通过监督微调（SFT）和RL的组合将预训练的掩码dLLM适应推理模型的框架。具体来说，我们开发和扩展了改进预训练dLLM推理的技术：（a）我们利用掩码SFT技术直接从现有数据集中提取知识并灌输自我改进行为，以及（b）我们引入了一种新的无批评、基于策略梯度的RL算法，称为diffu-GRPO。通过实证研究，我们调查了不同训练后配方在多个数学和逻辑推理基准上的表现。我们发现d1产生了最佳性能，并显著提高了最先进的dLLM的性能。 et.al.|[2504.12216](http://arxiv.org/abs/2504.12216)|null|
|**2025-04-16**|**Creating non-reversible rejection-free samplers by rebalancing skew-balanced Markov jump processes**|马尔可夫链抽样方法构成了现代计算统计学的支柱。然而，许多流行的方法容易出现随机游走行为，即对样本空间的扩散式探索，导致混合缓慢，需要复杂的调整来缓解。不可逆采样器可以解决其中一些问题。我们介绍了一种设备，该设备将满足参考度量的偏斜详细平衡条件的跳跃过程转化为对相对于参考度量绝对连续的目标度量进行采样的过程。由此产生的采样器是无排斥、不可逆和连续时间的。作为一个例子，我们将该器件应用于由蛙跳积分器离散的哈密顿动力学，得到了哈密顿蒙特卡罗（HMC）的无排斥不可逆连续时间版本。我们证明了在某些凸性条件下所得采样器的几何遍历性，并通过数值例子证明了其与HMC的定性不同行为。 et.al.|[2504.12190](http://arxiv.org/abs/2504.12190)|null|
|**2025-04-16**|**Analysis of steady-state solutions to a vasculogenesis model in dimension two**|我们研究了有界二维域中由耦合偏微分方程控制的血管生成模型的稳态解。解析构造显式稳态解，并在规定的初始和边界条件下严格分析其稳定性。通过采用能量方法，我们证明了当满足特定的参数条件时，这些解表现出局部渐近稳定性。该分析建立了稳定性阈值与系统扩散系数之间的直接联系，为控制模式形成的机制提供了定量见解。这些结果为理解趋化性驱动的生物系统中的自组织，特别是血管生成提供了基础性的理论进展。 et.al.|[2504.12164](http://arxiv.org/abs/2504.12164)|null|
|**2025-04-16**|**Anti-Aesthetics: Protecting Facial Privacy against Customized Text-to-Image Synthesis**|定制传播模式的兴起刺激了个性化视觉内容创作的繁荣，但也带来了恶意滥用的风险，严重威胁了个人隐私和版权保护。一些研究表明，图像的美学特性与人类对图像质量的感知高度正相关。受此启发，我们从新颖有趣的美学角度来解决这个问题，降低恶意定制模型的生成质量，从而更好地保护面部身份。具体而言，我们提出了一个分层反美学（HAA）框架来充分探索美学线索，该框架由两个关键分支组成：1）全球反美学：通过建立全球反美学奖励机制和全球反美学损失，它可以降低生成内容的整体美学；2） 局部反美学：设计了一种局部反美学奖励机制和局部反美学损失，以引导对抗性扰动破坏局部面部身份。通过无缝整合这两个分支，我们的HAA在定制生成过程中有效地实现了从全球到地方层面的反美学目标。大量实验表明，HAA在身份去除方面大大优于现有的SOTA方法，为保护面部隐私和版权提供了一种强大的工具。 et.al.|[2504.12129](http://arxiv.org/abs/2504.12129)|null|
|**2025-04-16**|**The CAM Model: An in vivo Testbed for Molecular Communication Systems**|分子通信（MC）研究越来越侧重于生物医学应用，如健康监测和药物输送，要求在现实生活环境中进行测试。提升MC研究需要开发先进的体内试验台。我们介绍了绒毛尿囊膜（CAM）模型，作为第一个多功能的3D体内MC平台。CAM是受精鸡蛋中高度血管化的膜，在生物工程、癌症研究和药物开发中建立。其生物现实性、可重复性和多功能性使其成为下一代MC测试台的理想选择，连接概念验证系统和实际应用。我们全面描述了CAM模型的属性和MC系统的相关性。通过实验研究，我们研究了CAM闭环血管系统中的荧光分子分布。我们使用包裹正态分布推导了一个分析模型来描述由扩散和流动主导的色散闭环系统中的粒子传播。开发了参数模型来近似CAM中的粒子动力学，参数通过非线性最小二乘曲线拟合进行估计。来自25个卵子的69个区域的数据集验证了我们的模型。我们分析参数关系和生物学合理性。最后，我们开发了一个用于鸡胚长期颗粒行为和肝脏积累的参数模型。 et.al.|[2504.12123](http://arxiv.org/abs/2504.12123)|null|
|**2025-04-16**|**A Diffusion-Based Framework for Terrain-Aware Remote Sensing Image Reconstruction**|遥感图像对于环境监测、农业管理和灾害应对至关重要。然而，由于云层覆盖、传感器故障或采集不完整，特别是在高分辨率和高频任务中，数据丢失严重限制了卫星图像的有效性。传统的插值方法难以处理大的缺失区域和复杂的结构。遥感图像由多个波段组成，每个波段都有不同的含义，确保波段之间的一致性对于避免组合图像中的异常至关重要。本文提出了SatelliteMarker，这是一种基于扩散的方法，可以在不同程度的数据丢失中重建丢失的数据，同时保持空间、光谱和时间的一致性。我们还提出了数字高程模型（DEM）作为条件输入，并使用量身定制的提示来生成逼真的图像，使扩散模型适用于定量遥感任务。此外，我们提出了一种基于分布损耗的VGG适配器模块，该模块减少了分布差异，确保了样式的一致性。大量实验表明，SatelliteMark在多个任务中实现了最先进的性能。 et.al.|[2504.12112](http://arxiv.org/abs/2504.12112)|null|

<p align=right>(<a href=#updated-on-20250418>back to top</a>)</p>

## NeRF

|Publish Date|Title|Abstract|PDF|Code|
|---|---|---|---|---|
|**2025-04-16**|**SCENT: Robust Spatiotemporal Learning for Continuous Scientific Data via Scalable Conditioned Neural Fields**|由于空间和时间依赖性之间的复杂相互作用、数据的高维度和可扩展性约束，时空学习具有挑战性。这些挑战在科学领域进一步加剧，在这些领域，数据通常是不规则分布的（例如，传感器故障的缺失值）和高容量的（例如高保真模拟），带来了额外的计算和建模困难。在本文中，我们提出了SCENT，这是一种用于可扩展和连续性知情的时空表示学习的新框架。SCENT在单一架构中统一了插值、重建和预测。SCENT建立在基于变换器的编码器-处理器-解码器骨干上，引入了可学习的查询来增强泛化能力，并引入了查询式交叉关注机制来有效捕获多尺度依赖关系。为了确保数据大小和模型复杂性的可扩展性，我们引入了稀疏注意力机制，实现了灵活的输出表示和任意分辨率的高效评估。我们通过广泛的模拟和真实世界的实验来验证SCENT，在实现卓越可扩展性的同时，在多个具有挑战性的任务中展示了最先进的性能。 et.al.|[2504.12262](http://arxiv.org/abs/2504.12262)|null|
|**2025-04-14**|**DNF-Avatar: Distilling Neural Fields for Real-time Animatable Avatar Relighting**|从单眼视频中创建可重现和可动画化的人类化身是一个新兴的研究课题，具有广泛的应用，例如虚拟现实、体育和视频游戏。之前的研究利用神经场和基于物理的渲染（PBR）来估计人类化身的几何形状并解开其外观属性。然而，这些方法的一个缺点是由于昂贵的蒙特卡洛射线追踪导致渲染速度较慢。为了解决这个问题，我们提出将隐式神经场（教师）的知识提取为显式的2D高斯飞溅（学生）表示，以利用高斯飞溅的快速光栅化特性。为了避免光线追踪，我们对PBR外观采用了分裂和近似。我们还提出了用于阴影计算的新型部分式环境遮挡探头。阴影预测是通过每像素只查询一次这些探测器来实现的，这为化身的实时重新照明铺平了道路。这些技术相结合，可以提供高质量的重新照明效果和逼真的阴影效果。我们的实验表明，所提出的学生模型与我们的教师模型实现了相当甚至更好的重新照明结果，同时在推理时快了370倍，达到了67 FPS的渲染速度。 et.al.|[2504.10486](http://arxiv.org/abs/2504.10486)|null|
|**2025-04-11**|**SN-LiDAR: Semantic Neural Fields for Novel Space-time View LiDAR Synthesis**|最近的研究已经开始探索激光雷达点云的新颖视图合成（NVS），旨在从看不见的视点生成逼真的激光雷达扫描。然而，大多数现有的方法都不能重建语义标签，而语义标签对于自动驾驶和机器人感知等许多下游应用至关重要。与受益于强大分割模型的图像不同，LiDAR点云缺乏如此大规模的预训练模型，这使得语义标注既费时又费力。为了应对这一挑战，我们提出了SN LiDAR，这是一种联合执行精确语义分割、高质量几何重建和逼真LiDAR合成的方法。具体来说，我们采用从粗到细的平面网格特征表示来从多帧点云中提取全局特征，并利用基于CNN的编码器从当前帧点云中提取局部语义特征。SemanticKITTI和KITTI-360的大量实验证明了SN LiDAR在语义和几何重建方面的优越性，有效地处理了动态对象和大规模场景。代码将在https://github.com/dtc111111/SN-Lidar. et.al.|[2504.08361](http://arxiv.org/abs/2504.08361)|**[link](https://github.com/dtc111111/sn-lidar)**|
|**2025-04-08**|**econSG: Efficient and Multi-view Consistent Open-Vocabulary 3D Semantic Gaussians**|最近关于开放词汇神经场的工作的主要重点是从VLM中提取精确的语义特征，然后将它们有效地整合到多视图一致的3D神经场表示中。然而，大多数现有的工作都是在受信任的SAM上进行的，以规范图像级CLIP，而无需进一步细化。此外，一些现有的研究通过在与3DGS语义场融合之前对2D VLM的语义特征进行降维来提高效率，这不可避免地导致了多视图不一致。在这项工作中，我们提出了使用3DGS进行开放式词汇语义分割的econSG。我们的econSG由以下部分组成：1）置信区间引导正则化（CRR），它相互细化SAM和CLIP，以获得具有完整和精确边界的精确语义特征的两全其美。2） 一个低维上下文空间，通过融合反投影的多视图2D特征来增强3D多视图一致性，同时提高计算效率，然后直接对融合的3D特征进行降维，而不是分别对每个2D视图进行操作。与现有方法相比，我们的econSG在四个基准数据集上显示了最先进的性能。此外，我们也是所有方法中最有效的培训。 et.al.|[2504.06003](http://arxiv.org/abs/2504.06003)|null|
|**2025-04-08**|**Meta-Continual Learning of Neural Fields**|神经场（NF）作为一种用于复杂数据表示的通用框架，已经获得了突出地位。这项工作揭示了一个新的问题设置，称为“神经场元连续学习”（MCL-NF），并引入了一种新的策略，该策略采用模块化架构与基于优化的元学习相结合。我们的策略侧重于克服现有神经场连续学习方法的局限性，如灾难性遗忘和缓慢收敛，实现了高质量的重建，显著提高了学习速度。我们进一步引入了神经辐射场的Fisher信息最大化损失（FIM-NeRF），它在样本级别最大化信息增益以增强学习泛化，并证明了收敛保证和泛化界限。我们在六个不同的数据集上对图像、音频、视频重建和视图合成任务进行了广泛的评估，证明了我们的方法在重建质量和速度方面优于现有的MCL和CL-NF方法。值得注意的是，我们的方法在降低参数要求的情况下，实现了神经场对城市级NeRF渲染的快速适应。 et.al.|[2504.05806](http://arxiv.org/abs/2504.05806)|null|
|**2025-04-06**|**Dynamic Neural Field Modeling of Visual Contrast for Perceiving Incoherent Looming**|Amari的动态神经场（DNF）框架提供了一种受大脑启发的方法来模拟神经元群的平均激活。利用单一领域，DNF已成为机器人应用中低能耗隐约感知模块的有前景的基础。然而，之前的DNF方法在检测不连贯或不一致的迫在眉睫的特征方面面临着重大挑战，这些特征在现实世界场景中很常见，例如雨天的碰撞检测。果蝇和蝗虫视觉系统的见解表明，编码ON/OFF视觉对比在增强迫在眉睫的选择性方面起着至关重要的作用。此外，横向激发机制可能会改善织机敏感神经元对连贯和非连贯刺激的反应。这些共同为改进迫在眉睫的感知模型提供了宝贵的指导。基于这些生物学证据，我们通过结合on/OFF视觉对比度的建模来扩展之前的单场DNF框架，每个对比度都由一个专用的DNF控制。使用归一化高斯核对每个ON/OFF对比场内的横向激励进行公式化，并将其输出整合到求和字段中以生成碰撞警报。实验评估表明，所提出的模型有效地解决了非相干逼近检测的挑战，并且明显优于最先进的蝗虫启发模型。它在各种刺激下表现出了强大的性能，包括合成雨效应，突显了它在复杂、嘈杂的环境中，在视觉线索不一致的情况下，具有可靠的隐约感知的潜力。 et.al.|[2504.04551](http://arxiv.org/abs/2504.04551)|null|
|**2025-04-03**|**A Physics-Informed Meta-Learning Framework for the Continuous Solution of Parametric PDEs on Arbitrary Geometries**|在这项工作中，我们引入了隐式有限算子学习（iFOL），用于任意几何上偏微分方程（PDE）的连续和参数解。我们提出了一种基于物理信息的编解码器网络，以建立连续参数和解空间之间的映射。解码器通过利用以潜在或特征码为条件的隐式神经场网络来构建参数解场。实例特定代码是通过基于二阶元学习技术的PDE编码过程导出的。在训练和推理中，在PDE编码和解码过程中，物理信息损失函数被最小化。iFOL以能量或加权残差形式表示损失函数，并使用从标准数值PDE方法导出的离散残差对其进行评估。这种方法在训练和推理过程中都会导致离散残差的反向传播。iFOL具有几个关键特性：（1）其独特的损失公式消除了以前在PDE的条件神经场算子学习中使用的传统编码过程-解码流水线的需要；（2） 它不仅提供精确的参数和连续场，而且提供参数梯度的解，而不需要额外的损失项或灵敏度分析；（3） 它可以有效地捕捉溶液中的尖锐不连续性；（4）它消除了对几何和网格的约束，使其适用于任意几何和空间采样（零样本超分辨率能力）。我们批判性地评估了这些特征，并分析了网络在稳态和瞬态PDE中推广到看不见的样本的能力。所提出的方法的整体性能是有希望的，证明了它适用于计算力学中一系列具有挑战性的问题。 et.al.|[2504.02459](http://arxiv.org/abs/2504.02459)|**[link](https://github.com/rezanajian/fol)**|
|**2025-04-01**|**Flow Matching on Lie Groups**|流匹配（FM）是一种最新的生成建模技术：我们的目标是学习如何从分布中采样{X}_1 $通过从某些分布中流动样本$\mathfrak{X}_0$很容易取样。关键技巧是，在$\mathfrak中对端点进行调节的同时，可以训练这个流场{X}_1$：给定终点，只需沿直线段移动到终点（Lipman等人，2022）。然而，直线段仅在欧几里德空间上定义良好。因此，Chen和Lipman（2023）将该方法推广到黎曼流形上的FM，用测地线或其谱近似代替线段。我们采取了另一种观点：我们通过用指数曲线代替线段来推广李群上的FM。这导致了许多矩阵李群的简单、内在和快速实现，因为所需的李群运算（积、逆、指数、对数）仅由相应的矩阵运算给出。然后，李群上的FM可用于生成建模，数据由特征集（在$\mathbb{R}^n$ 中）和姿势集（在某些李群中）组成，例如等变神经场的潜在码（Wessels等人，2025）。 et.al.|[2504.00494](http://arxiv.org/abs/2504.00494)|**[link](https://github.com/finnsherry/FlowMatching)**|
|**2025-03-29**|**NeuralGS: Bridging Neural Fields and 3D Gaussian Splatting for Compact 3D Representations**|3D高斯散点（3DGS）显示了卓越的质量和渲染速度，但有数百万的3D高斯分布和巨大的存储和传输成本。最近的3DGS压缩方法主要集中在压缩脚手架GS上，取得了令人印象深刻的性能，但增加了体素结构和复杂的编码和量化策略。在这篇论文中，我们的目标是开发一种简单而有效的方法，称为NeuralGS，它以另一种方式探索将原始3DGS压缩成紧凑的表示，而不需要体素结构和复杂的量化策略。我们的观察是，像NeRF这样的神经场可以用多层感知器（MLP）神经网络表示复杂的3D场景，只需要几兆字节。因此，NeuralGS有效地采用神经场表示来用MLP对3D高斯的属性进行编码，即使对于大规模场景，也只需要很小的存储空间。为了实现这一点，我们采用了一种聚类策略，并根据高斯的重要性得分作为拟合权重，为每个聚类用不同的微小MLP对高斯进行拟合。我们在多个数据集上进行实验，在不损害视觉质量的情况下实现了平均模型大小减少45倍。我们的方法在原始3DGS上的压缩性能与基于Scaffold GS的专用压缩方法相当，这表明了用神经场直接压缩原始3DGS的巨大潜力。 et.al.|[2503.23162](http://arxiv.org/abs/2503.23162)|null|
|**2025-03-27**|**Renormalization group analysis of noisy neural field**|大脑中的神经元在个体特性和与其他神经元的连接方面表现出极大的多样性。为了深入了解神经元多样性如何在大尺度上促进大脑动力学和功能，我们借鉴了复制方法的框架，该框架已成功应用于平衡统计力学中一大类具有淬灭噪声的问题。我们分析了Wilson Cowan模型的两个线性化版本，其随机系数在空间上是相关的。特别是：（A）神经元本身的性质是异质的，（B）它们的连接是各向异性的。在这两个模型中，淬火随机性的平均会产生额外的非线性。这些非线性在威尔逊重整化群的框架内进行了分析。我们发现，对于模型A，如果噪声的空间相关性随距离衰减，指数小于-2 $，则在大的空间尺度上，噪声的影响消失了。相比之下，对于模型B，只有当空间相关性以小于-1$ 的指数衰减时，噪声对神经元连接的影响才会消失。我们的计算还表明，在某些条件下，噪声的存在可能会在大尺度上产生类似行波的行为，尽管这一结果在微扰理论的高阶下是否仍然有效还有待观察。 et.al.|[2503.21605](http://arxiv.org/abs/2503.21605)|null|

<p align=right>(<a href=#updated-on-20250418>back to top</a>)</p>

[contributors-shield]: https://img.shields.io/github/contributors/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[contributors-url]: https://github.com/Vincentqyw/cv-arxiv-daily/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[forks-url]: https://github.com/Vincentqyw/cv-arxiv-daily/network/members
[stars-shield]: https://img.shields.io/github/stars/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[stars-url]: https://github.com/Vincentqyw/cv-arxiv-daily/stargazers
[issues-shield]: https://img.shields.io/github/issues/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[issues-url]: https://github.com/Vincentqyw/cv-arxiv-daily/issues

