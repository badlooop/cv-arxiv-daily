[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]

## Updated on 2025.02.11
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
|**2025-02-10**|**Lumina-Video: Efficient and Flexible Video Generation with Multi-scale Next-DiT**|最近的进展已经将扩散变换器（DiTs）确立为生成建模中的主导框架。在这一成功的基础上，Lumina Next在使用Next DiT生成逼真图像方面取得了卓越的性能。然而，它在视频生成方面的潜力在很大程度上仍未得到开发，在对视频数据固有的时空复杂性进行建模方面存在重大挑战。为了解决这个问题，我们引入了Lumina Video，这是一个利用Next DiT优势的框架，同时为视频合成引入了量身定制的解决方案。Lumina Video采用了多尺度Next DiT架构，该架构联合学习多个拼接，以提高效率和灵活性。通过将运动分数作为显式条件，Lumina Video还可以直接控制生成视频的动态程度。结合分辨率和FPS越来越高的渐进式训练方案，以及混合自然和合成数据的多源训练方案，Lumina Video在高训练和推理效率下实现了卓越的美学质量和运动平滑度。我们还提出了Lumina-V2A，一种基于Next DiT的视频到音频模型，为生成的视频创建同步声音。代码发布于https://www.github.com/Alpha-VLLM/Lumina-Video. et.al.|[2502.06782](http://arxiv.org/abs/2502.06782)|null|
|**2025-02-10**|**History-Guided Video Diffusion**|无分类器引导（CFG）是改进扩散模型中条件生成的关键技术，可以在提高样本质量的同时实现更精确的控制。将这种技术扩展到视频扩散是很自然的，视频扩散生成以可变数量的上下文帧为条件的视频，统称为历史。然而，我们发现使用可变长度历史进行指导存在两个关键挑战：仅支持固定大小条件的架构，以及CFG风格历史丢失表现不佳的实证观察。为了解决这个问题，我们提出了扩散强制变换器（DFoT），这是一种视频扩散架构和理论上有根据的训练目标，可以共同对灵活数量的历史帧进行调节。然后，我们介绍历史指导，这是DFoT独有的一系列指导方法。我们发现，其最简单的形式，香草历史指导，已经显著提高了视频生成质量和时间一致性。一种更先进的方法，跨时间和频率的历史引导，进一步增强了运动动力学，能够对分布历史进行合成泛化，并可以稳定地推出超长视频。网站：https://boyuan.space/history-guidance et.al.|[2502.06764](http://arxiv.org/abs/2502.06764)|null|
|**2025-02-10**|**Señorita-2M: A High-Quality Instruction-based Dataset for General Video Editing by Video Specialists**|视频生成的最新进展刺激了视频编辑技术的发展，视频编辑技术可分为基于反转的方法和端到端方法。然而，目前的视频编辑方法仍然面临着几个挑战。基于反转的方法虽然训练自由且灵活，但在推理过程中耗时，难以处理细粒度的编辑指令，并产生伪影和抖动。另一方面，依赖于编辑视频对进行训练的端到端方法提供了更快的推理速度，但由于缺乏高质量的训练视频对，往往会产生较差的编辑结果。本文中，为了缩小端到端方法的差距，我们引入了高质量视频编辑数据集Se-norita-2M。Se-norita-2M由大约200万对视频编辑对组成。它由四个高质量的专业视频编辑模型构建而成，每个模型都由我们的团队精心制作和训练，以实现最先进的编辑效果。我们还提出了一种过滤管道来消除编辑不佳的视频对。此外，我们探索了常见的视频编辑架构，以基于当前预训练的生成模型确定最有效的结构。大量实验表明，我们的数据集可以帮助产生非常高质量的视频编辑结果。更多详细信息请访问https://senorita.github.io. et.al.|[2502.06734](http://arxiv.org/abs/2502.06734)|null|
|**2025-02-10**|**TripoSG: High-Fidelity 3D Shape Synthesis using Large-Scale Rectified Flow Models**|扩散技术的最新进展将图像和视频生成推向了前所未有的质量水平，显著加速了生成式人工智能的部署和应用。然而，由于3D数据规模的限制、3D数据处理的复杂性以及对3D领域先进技术的探索不足，3D形状生成技术迄今为止一直落后。当前的3D形状生成方法在输出质量、泛化能力和与输入条件的对齐方面面临着巨大的挑战。我们提出了TripoSG，这是一种新的流线型形状扩散范式，能够生成与输入图像精确对应的高保真3D网格。具体来说，我们提出：1）一种用于3D形状生成的大型整流流量变换器，通过对大量高质量数据的训练实现最先进的保真度。2） 一种混合监督训练策略，结合SDF、正常损失和程知损失，用于3D VAE，实现高质量的3D重建性能。3） 一个数据处理管道，用于生成200万个高质量的3D样本，突出了训练3D生成模型时数据质量和数量的关键规则。通过全面的实验，我们验证了新框架中每个组件的有效性。这些部件的无缝集成使TripoSG在3D形状生成方面达到了最先进的性能。由于高分辨率功能，由此产生的3D形状显示出增强的细节，并对输入图像表现出卓越的保真度。此外，TripoSG在从不同的图像风格和内容生成3D模型方面表现出了更强的通用性，展示了强大的生成能力。为了促进3D生成领域的进步和创新，我们将公开我们的模型。 et.al.|[2502.06608](http://arxiv.org/abs/2502.06608)|null|
|**2025-02-10**|**CustomVideoX: 3D Reference Attention Driven Dynamic Adaptation for Zero-Shot Customized Video Diffusion Transformers**|定制生成在图像合成方面取得了重大进展，但由于时间不一致和质量下降，个性化视频生成仍然具有挑战性。在本文中，我们介绍了CustomVideoX，这是一个利用视频扩散变换器从参考图像生成个性化视频的创新框架。CustomVideoX通过专门训练LoRA参数来提取参考特征，从而利用预训练的视频网络，确保效率和适应性。为了促进参考图像和视频内容之间的无缝交互，我们提出了3D参考注意力，它允许参考图像特征在空间和时间维度上与所有视频帧直接和同时交互。为了减轻推理过程中参考图像特征和文本引导对生成视频内容的过度影响，我们实现了时间感知参考注意力偏差（TAB）策略，在不同的时间步长上动态调节参考偏差。此外，我们引入了实体区域感知增强（ERAE）模块，通过调整注意力偏差，将关键实体令牌的高度激活区域与参考特征注入对齐。为了全面评估个性化视频生成，我们建立了一个新的基准VideoBench，包括50多个对象和100个用于广泛评估的提示。实验结果表明，CustomVideoX在视频一致性和质量方面明显优于现有方法。 et.al.|[2502.06527](http://arxiv.org/abs/2502.06527)|null|
|**2025-02-10**|**Efficient-vDiT: Efficient Video Diffusion Transformers With Attention Tile**|尽管有望合成高保真视频，但由于注意力计算的复杂性和众多采样步骤，具有3D全注意力的扩散变换器（DiTs）受到昂贵推理的影响。例如，流行的Open Sora Plan模型生成29帧的单个视频需要9分钟以上的时间。本文从两个方面解决了效率低下的问题：1）基于视频数据中的冗余修剪3D全注意力；我们在视频数据的3D注意力图中识别出一种流行的瓦片式重复模式，并倡导一种新的稀疏3D注意力家族，该家族的复杂度与视频帧数呈线性关系。2） 采用现有的多步稠度蒸馏缩短取样过程；我们将整个采样轨迹分为几个部分，并在每个部分内进行一致性蒸馏，以激活少量步骤生成能力。我们进一步设计了一个三阶段培训管道，将低复杂性注意力和少步骤生成能力结合起来。值得注意的是，在0.1%的预训练数据下，我们将Open-Sora-Plan-1.2模型转化为一个高效的模型，对于29帧和93帧720p视频生成，其速度提高了7.4倍-7.8倍，在VBench中的性能折衷很小。此外，我们证明了我们的方法适用于分布式推理，当在4个具有序列并行性的GPU上运行时，可以实现额外的3.91x加速。 et.al.|[2502.06155](http://arxiv.org/abs/2502.06155)|null|
|**2025-02-09**|**VFX Creator: Animated Visual Effect Generation with Controllable Diffusion Transformer**|制作魔术和幻觉是电影制作中最激动人心的方面之一，视觉效果（VFX）是令人难忘的电影体验背后的动力。虽然生成式人工智能的最新进展推动了通用图像和视频合成的进步，但可控视觉特效生成领域的探索仍然相对不足。在这项工作中，我们提出了一种新的动画视觉特效生成范式，即图像动画，其中动态效果是由用户友好的文本描述和静态参考图像生成的。我们的工作有两个主要贡献：（i）Open VFX，第一个高质量的VFX视频数据集，涵盖15个不同的效果类别，用文本描述、用于空间调节的实例分割掩码和用于时间控制的开始-结束时间戳进行注释。（ii）VFX Creator，一个基于视频扩散变换器的简单而有效的可控VFX生成框架。该模型结合了一个空间和时间可控的LoRA适配器，需要最少的训练视频。具体来说，即插即用掩码控制模块实现了实例级的空间操纵，而嵌入在扩散过程中的标记化开始-结束运动时间戳与文本编码器一起，允许对效果时间和节奏进行精确的时间控制。在Open VFX测试集上进行的广泛实验证明了所提出的系统在生成逼真和动态效果方面的优越性，在空间和时间可控性方面实现了最先进的性能和泛化能力。此外，我们引入了一个专门的度量来评估时间控制的精度。通过将传统的视觉特效技术与生成方法相结合，VFX Creator为高效和高质量的视频效果生成开辟了新的可能性，使更广泛的受众能够使用先进的视觉特效。 et.al.|[2502.05979](http://arxiv.org/abs/2502.05979)|null|
|**2025-02-08**|**Towards AI-driven Sign Language Generation with Non-manual Markers**|手语对聋哑人（DHH）社区至关重要。手语生成系统有可能通过将英语等书面语言翻译成签名视频来支持交流。然而，由于语法结构翻译不佳、缺乏面部线索和肢体语言以及视觉和运动保真度不足，当前的系统往往无法满足用户需求。我们通过建立LLM和视频生成模型的最新进展来解决这些挑战，将英语句子翻译成看起来自然的AI ASL签名者。我们模型的文本组件提取ASL的手动和非手动组件的信息，用于合成骨骼姿态序列和相应的视频帧。我们对30名DHH参与者的用户研究和彻底的技术评估的结果表明，取得了重大进展，并确定了满足用户需求所需的关键领域。 et.al.|[2502.05661](http://arxiv.org/abs/2502.05661)|null|
|**2025-02-08**|**Training-Free Constrained Generation With Stable Diffusion Models**|稳定扩散模型代表了跨不同领域数据合成的最新技术，并在科学和工程应用中具有变革性的潜力，例如，通过促进发现新的解决方案和模拟计算上难以明确建模的系统。然而，由于无法严格遵守物理定律和特定领域的约束，它们在这些领域的当前效用受到严重限制。如果没有这一基础，在从材料科学到安全关键系统的关键应用中部署此类模型仍然不切实际。本文通过提出一种将稳定扩散模型与约束优化框架集成的新方法来解决这一基本局限性，使它们能够生成满足严格物理和功能要求的输出。我们通过材料科学实验证明了这种方法的有效性，这些实验要求遵守精确的形态测量特性，涉及使用循环中的模拟器生成视频以产生应力-应变响应的逆向设计问题，以及输出必须避免侵犯版权的安全设置。 et.al.|[2502.05625](http://arxiv.org/abs/2502.05625)|null|
|**2025-02-08**|**A Physical Coherence Benchmark for Evaluating Video Generation Models via Optical Flow-guided Frame Prediction**|视频生成模型的最新进展表明了它们作为世界模拟器的潜力，但它们经常与偏离物理定律的视频作斗争，这是大多数文本到视频基准测试所忽视的一个关键问题。我们介绍了一个专门用于评估生成视频的物理一致性的基准，PhyCoBench。我们的基准包括120个提示，涵盖7类物理原理，捕捉视频内容中可观察到的关键物理定律。我们在PhyCoBench上评估了四种最先进的（SoTA）T2V模型，并进行了手动评估。此外，我们提出了一种自动评估模型：PhyCoPredictor，这是一种以级联方式生成光流和视频帧的扩散模型。通过比较自动和手动排序的一致性评估，实验结果表明，PhyCoPredictor目前与人类评估最接近。因此，它可以有效地评估视频的物理一致性，为未来的模型优化提供见解。我们的基准测试，包括物理一致性提示、自动评估工具PhyCoPredictor和生成的视频数据集，都将很快在GitHub上发布。 et.al.|[2502.05503](http://arxiv.org/abs/2502.05503)|null|

<p align=right>(<a href=#updated-on-20250211>back to top</a>)</p>

## 3D

|Publish Date|Title|Abstract|PDF|Code|
|---|---|---|---|---|
|**2025-02-10**|**SIREN: Semantic, Initialization-Free Registration of Multi-Robot Gaussian Splatting Maps**|我们提出了SIREN用于多机器人高斯散点（GSplat）地图的注册，对相机姿态、图像和用于初始化或融合局部子地图的地图间变换零访问。为了实现这些功能，SIREN以三种关键方式利用语义的通用性和鲁棒性，为多机器人GSplat地图推导出严格的配准流水线。首先，SIREN利用语义来识别局部图中特征丰富的区域，在这些区域中更好地提出了配准问题，从而消除了先前工作中通常需要的任何初始化。其次，SIREN使用鲁棒的语义特征来识别局部地图中高斯之间的候选对应关系，为鲁棒的几何优化奠定了基础，粗略地对齐了从局部地图中提取的3D高斯基元。第三，这一关键步骤使子图之间的变换能够进行后续的光度细化，其中SIREN利用GSplat图中的新颖视图合成以及基于语义的图像滤波器来计算高精度的非刚性变换，以生成高保真融合图。我们在一系列真实世界的数据集中，特别是在最广泛使用的机器人硬件平台上，包括机械手、无人机和四足动物，展示了SIREN与竞争基线相比的卓越性能。在我们的实验中，SIREN在最具挑战性的场景中实现了约90倍的较小旋转误差、300倍的较小平移误差和44倍的较小尺度误差，在这些场景中，竞争方法很难解决。在审查过程结束后，我们将发布代码并提供项目页面的链接。 et.al.|[2502.06519](http://arxiv.org/abs/2502.06519)|null|
|**2025-02-05**|**VistaFlow: Photorealistic Volumetric Reconstruction with Dynamic Resolution Management via Q-Learning**|我们介绍VistaFlow，这是一种可扩展的三维成像技术，能够从一组二维照片中重建完全交互式的三维体积图像。我们的模型通过一个可微分的渲染系统来合成新的视点，该系统能够对逼真的3D场景进行动态分辨率管理。我们通过引入QuiQ来实现这一目标，QuiQ是一种通过Q学习训练的新型中间视频控制器，通过以毫秒精度调整渲染分辨率来保持一致的高帧率。值得注意的是，VistaFlow在集成CPU图形上本地运行，使其适用于移动和入门级设备，同时仍能提供高性能渲染。VistaFlow绕过神经辐射场（NeRF），使用PlenOctree数据结构以最低的硬件要求渲染复杂的光相互作用，如反射和次表面散射。我们的模型能够在消费类硬件上以每秒100帧以上的1080p分辨率进行新颖的视图合成，从而超越最先进的方法。通过根据每个设备的功能定制渲染质量，VistaFlow有可能提高从高端工作站到廉价微控制器等各种硬件的真实感3D场景渲染的效率和可访问性。 et.al.|[2502.05222](http://arxiv.org/abs/2502.05222)|null|
|**2025-02-07**|**PoI: Pixel of Interest for Novel View Synthesis Assisted Scene Coordinate Regression**|通过新的视图合成技术，如NeRF和高斯散斑，可以增强估计相机姿态的任务，以增加训练数据的多样性和扩展性。然而，这些技术通常会产生模糊和重影等问题的渲染图像，从而影响其可靠性。对于在像素级别估计3D坐标的场景坐标回归（SCR）方法来说，这些问题变得尤为明显。为了缓解与不可靠渲染图像相关的问题，我们引入了一种新的滤波方法，该方法选择性地提取渲染良好的像素，同时丢弃较差的像素。该滤波器在训练过程中同时测量SCR模型的实时重投影损失和梯度。基于这种滤波技术，我们还开发了一种新的策略，利用稀疏输入改进场景坐标回归，并借鉴了稀疏输入技术在新颖视图合成中的成功应用。我们的实验结果验证了我们方法的有效性，在室内和室外数据集上展示了最先进的性能。 et.al.|[2502.04843](http://arxiv.org/abs/2502.04843)|null|
|**2025-02-05**|**Controllable Satellite-to-Street-View Synthesis with Precise Pose Alignment and Zero-Shot Environmental Control**|从卫星图像生成街景图像是一项具有挑战性的任务，特别是在保持精确的姿态对齐和结合不同的环境条件方面。虽然扩散模型在生成任务中显示出了希望，但它们在整个扩散过程中保持严格姿态对齐的能力是有限的。本文提出了一种新的迭代单应性调整（IHA）方案，应用于去噪过程中，有效地解决了姿态失准问题，并确保了生成的街景图像的空间一致性。此外，目前，用于卫星到街道视图生成的可用数据集在光照和天气条件的多样性方面受到限制，从而限制了生成输出的通用性。为了缓解这种情况，我们引入了一种文本引导的照明和天气控制的采样策略，可以对环境因素进行精细控制。大量的定量和定性评估表明，我们的方法显著提高了姿态精度，增强了生成的街景图像的多样性和真实性，为卫星到街景生成任务设定了新的基准。 et.al.|[2502.03498](http://arxiv.org/abs/2502.03498)|null|
|**2025-02-04**|**Geometric Neural Process Fields**|本文解决了神经场（NeF）泛化的挑战，其中模型必须有效地适应仅给出少量观测值的新信号。为了解决这个问题，我们提出了几何神经过程场（G-NPF），这是一个明确捕捉不确定性的神经辐射场的概率框架。我们将NeF泛化表述为概率问题，从而能够从有限的上下文观测中直接推断出NeF函数分布。为了引入结构归纳偏差，我们引入了一组几何基来编码空间结构，并促进NeF函数分布的推断。在此基础上，我们设计了一个分层潜在变量模型，使G-NPF能够整合多个空间层次的结构信息，并有效地参数化INR函数。这种分层方法提高了对新场景和未知信号的泛化能力。针对3D场景的新颖视图合成以及2D图像和1D信号回归的实验证明了我们的方法在捕捉不确定性和利用结构信息提高泛化能力方面的有效性。 et.al.|[2502.02338](http://arxiv.org/abs/2502.02338)|null|
|**2025-02-05**|**GP-GS: Gaussian Processes for Enhanced Gaussian Splatting**|3D高斯散斑已经成为一种高效的真实感新型视图合成方法。然而，它对稀疏运动结构（SfM）点云的依赖一直会损害场景重建的质量。为了解决这些局限性，本文提出了一种新的3D重建框架高斯过程高斯散斑（GP-GS），其中开发了一个多输出高斯过程模型，以实现稀疏SfM点云的自适应和不确定性引导的致密化。具体来说，我们提出了一种动态采样和滤波流水线，通过利用基于GP的预测从输入的2D像素和深度图中推断出新的候选点，自适应地扩展SfM点云。该管道利用不确定性估计来指导高方差预测的修剪，确保几何一致性，并能够生成密集的点云。加密的点云提供了高质量的初始3D高斯分布，以提高重建性能。在各种规模的合成和真实世界数据集上进行的广泛实验验证了所提出框架的有效性和实用性。 et.al.|[2502.02283](http://arxiv.org/abs/2502.02283)|null|
|**2025-02-03**|**WonderHuman: Hallucinating Unseen Parts in Dynamic 3D Human Reconstruction**|在这篇论文中，我们提出了WonderHuman来从单目视频中重建动态的人类化身，以实现高保真的新颖视图合成。以前的动态人体化身重建方法通常要求输入视频完全覆盖观察到的人体。然而，在日常实践中，人们通常可以访问有限的视点，例如单眼正视视频，这使得以前的方法重建人类化身的看不见的部分成为一项繁琐的任务。为了解决这个问题，我们提出了WonderHuman，它利用2D生成扩散模型先验，从单眼视频中实现动态人类化身的高质量、逼真的重建，包括精确渲染看不见的身体部位。我们的方法引入了双空间优化技术，在规范和观察空间中应用分数蒸馏采样（SDS），以确保视觉一致性，并增强动态人体重建的真实感。此外，我们提出了一种视图选择策略和姿势特征注入，以加强SDS预测和观测数据之间的一致性，确保重建化身的姿势依赖效果和更高的保真度。在实验中，我们的方法在从给定的单眼视频中生成真实感渲染时达到了SOTA性能，特别是对于那些具有挑战性的看不见的部分。项目页面和源代码可以在https://wyiguanw.github.io/WonderHuman/. et.al.|[2502.01045](http://arxiv.org/abs/2502.01045)|null|
|**2025-01-31**|**Lifting by Gaussians: A Simple, Fast and Flexible Method for 3D Instance Segmentation**|我们介绍了一种新的三维高斯散斑辐射场（3DGS）开放世界实例分割方法——高斯提升（LBG）。最近，3DGS场已经成为基于神经场的高质量新视图合成方法的高效和明确的替代方案。我们的3D实例分割方法直接从SAM（或FastSAM等）中提取2D分割掩模，以及CLIP和DINOv2的特征，直接将它们融合到3DGS（或类似的高斯辐射场，如2DGS）上。与以前的方法不同，LBG不需要每个场景的训练，使其能够在任何现有的3DGS重建上无缝运行。我们的方法不仅比现有方法快一个数量级，而且更简单；它也是高度模块化的，能够对现有的3DGS字段进行3D语义分割，而不需要对3D高斯进行特定的参数化。此外，我们的技术在保持灵活性和效率的同时，为2D语义新颖视图合成和3D资产提取结果实现了卓越的语义分割。我们进一步介绍了一种从3D辐射场分割方法中评估单独分割的3D资产的新方法。 et.al.|[2502.00173](http://arxiv.org/abs/2502.00173)|null|
|**2025-01-31**|**Advancing Dense Endoscopic Reconstruction with Gaussian Splatting-driven Surface Normal-aware Tracking and Mapping**|同步定位和标测（SLAM）对于微创手术中的精确手术干预和机器人任务至关重要。虽然3D高斯散斑（3DGS）的最新进展通过高质量的新颖视图合成和快速渲染改进了SLAM，但由于多视图不一致，这些系统在精确的深度和表面重建方面遇到了困难。简单地结合SLAM和3DGS会导致重建帧之间的不匹配。在这项工作中，我们提出了Endo-2DTAM，一种具有二维高斯散斑（2DGS）的实时内窥镜SLAM系统，以应对这些挑战。Endo-2DTAM包含一个表面法线感知管道，该管道由跟踪、映射和束调整模块组成，用于几何精确重建。我们强大的跟踪模块结合了点对点和点对平面距离度量，而映射模块利用法线一致性和深度失真来提高表面重建质量。我们还引入了一种姿态一致性策略，用于高效和几何相干的关键帧采样。对公共内窥镜数据集的广泛实验表明，Endo-2DTAM在手术场景的深度重建方面实现了1.87美元/分钟0.63美元/毫米的RMSE，同时保持了计算效率高的跟踪、高质量的视觉外观和实时渲染。我们的代码将在github.com/lastbasket/Endo-2DTAM上发布。 et.al.|[2501.19319](http://arxiv.org/abs/2501.19319)|**[link](https://github.com/lastbasket/endo-2dtam)**|
|**2025-01-30**|**Zero-Shot Novel View and Depth Synthesis with Multi-View Geometric Diffusion**|从稀疏姿态图像重建3D场景的当前方法采用中间3D表示，如神经场、体素网格或3D高斯，以实现多视图一致的场景外观和几何形状。本文介绍了MVGD，这是一种基于扩散的架构，能够在给定任意数量的输入视图的情况下，从新的视点直接生成像素级的图像和深度图。我们的方法使用光线图调节来增强来自不同视点的空间信息的视觉特征，并指导从新视图生成图像和深度图。我们方法的一个关键方面是图像和深度图的多任务生成，使用可学习的任务嵌入来指导向特定模态的扩散过程。我们从公开可用的数据集中收集了6000多万个多视图样本来训练这个模型，并提出了在这种不同条件下实现高效和一致学习的技术。我们还提出了一种新策略，通过逐步微调较小的模型，实现了对较大模型的有效训练，并具有很好的扩展行为。通过广泛的实验，我们报告了多个新颖的视图合成基准以及多视图立体和视频深度估计的最新结果。 et.al.|[2501.18804](http://arxiv.org/abs/2501.18804)|null|

<p align=right>(<a href=#updated-on-20250211>back to top</a>)</p>

## 3D Reconstruction

|Publish Date|Title|Abstract|PDF|Code|
|---|---|---|---|---|
|**2025-02-10**|**TripoSG: High-Fidelity 3D Shape Synthesis using Large-Scale Rectified Flow Models**|扩散技术的最新进展将图像和视频生成推向了前所未有的质量水平，显著加速了生成式人工智能的部署和应用。然而，由于3D数据规模的限制、3D数据处理的复杂性以及对3D领域先进技术的探索不足，3D形状生成技术迄今为止一直落后。当前的3D形状生成方法在输出质量、泛化能力和与输入条件的对齐方面面临着巨大的挑战。我们提出了TripoSG，这是一种新的流线型形状扩散范式，能够生成与输入图像精确对应的高保真3D网格。具体来说，我们提出：1）一种用于3D形状生成的大型整流流量变换器，通过对大量高质量数据的训练实现最先进的保真度。2） 一种混合监督训练策略，结合SDF、正常损失和程知损失，用于3D VAE，实现高质量的3D重建性能。3） 一个数据处理管道，用于生成200万个高质量的3D样本，突出了训练3D生成模型时数据质量和数量的关键规则。通过全面的实验，我们验证了新框架中每个组件的有效性。这些部件的无缝集成使TripoSG在3D形状生成方面达到了最先进的性能。由于高分辨率功能，由此产生的3D形状显示出增强的细节，并对输入图像表现出卓越的保真度。此外，TripoSG在从不同的图像风格和内容生成3D模型方面表现出了更强的通用性，展示了强大的生成能力。为了促进3D生成领域的进步和创新，我们将公开我们的模型。 et.al.|[2502.06608](http://arxiv.org/abs/2502.06608)|null|
|**2025-02-07**|**SC-OmniGS: Self-Calibrating Omnidirectional Gaussian Splatting**|360度相机通过捕获全面的场景数据，简化了辐射场3D重建的数据收集。然而，传统的辐射场方法并没有解决360度图像固有的具体挑战。我们提出了SC OmniGS，这是一种新型的自校准全向高斯散射系统，用于使用360度图像快速准确地重建全向辐射场。我们没有将360度图像转换为立方体图并执行透视图像校准，而是将360度图视为一个完整的球体，并推导出一个数学框架，该框架能够实现直接的全向相机姿态校准，并伴随着3D高斯优化。此外，我们引入了一种可微分的全向相机模型，以纠正现实世界数据的失真，从而提高性能。总体而言，通过最小化加权球面光度损失，对全向相机的内在模型、外在姿态和3D高斯分布进行了联合优化。广泛的实验表明，我们提出的SC OmniGS能够从嘈杂的相机姿态中恢复高质量的辐射场，甚至在以宽基线和非对象中心配置为特征的具有挑战性的场景中没有姿态。消费级全向相机捕获的真实世界数据集中的显著性能提升验证了我们的通用全向相机模型在减少360度图像失真方面的有效性。 et.al.|[2502.04734](http://arxiv.org/abs/2502.04734)|null|
|**2025-02-06**|**Measuring Physical Plausibility of 3D Human Poses Using Physics Simulation**|在物理场景中对人类进行建模对于理解涉及增强现实或从视频中评估人类行为（如体育或身体康复）的应用程序中的人类与环境交互至关重要。最先进的文献从单目或多视角的3D人体姿势开始，并使用这种表示将人固定在3D世界空间中。虽然精度的标准指标捕捉了关节位置误差，但它们并没有考虑3D姿势的物理合理性。这一局限性促使研究人员提出了评估抖动、地板穿透和不平衡姿势的其他指标。然而，这些方法测量的是独立的误差实例，并不代表运动过程中的平衡或稳定性。在这项工作中，我们建议从物理模拟中测量物理合理性。我们引入了两个指标来捕捉来自任何3D人体姿态估计模型的预测3D姿态的物理合理性和稳定性。通过物理模拟，我们发现了与现有合理性度量和运动过程中测量稳定性的相关性。我们评估并比较了两种最先进的方法的性能，即多视图三角基线和来自Human3.6m数据集的地面真实3D标记。 et.al.|[2502.04483](http://arxiv.org/abs/2502.04483)|null|
|**2025-02-06**|**XMTC: Explainable Early Classification of Multivariate Time Series in Reach-to-Grasp Hand Kinematics**|手部运动学可以在人机交互（HCI）中进行测量，目的是预测用户在伸手抓握动作中的意图。使用多个手部传感器，可以捕获多元时间序列数据。给定多个对象上的多个可能动作，目标是对多元时间序列数据进行分类，其中应尽早预测类别。许多机器学习方法已经被开发用于此类分类任务，其中不同的方法在不同的数据集上产生有利的解决方案。因此，我们采用了一种集成方法，包括并加权不同的方法。为了提供值得信赖的分类结果，我们提出了XMTC工具，该工具结合了协调的多视图可视化来分析预测。时间精度图、混淆矩阵热图、时间置信度热图和部分依赖图允许识别早期预测和预测质量之间的最佳权衡，检测和分析具有挑战性的分类条件，并以全面和详细的方式调查预测演变。我们将XMTC应用于多种场景中的真实HCI数据，并表明我们的分类器可以在早期实现良好的分类预测，以及哪些条件易于区分，哪些多元时间序列测量带来了挑战，哪些特征具有最大的影响。 et.al.|[2502.04398](http://arxiv.org/abs/2502.04398)|null|
|**2025-02-06**|**sshELF: Single-Shot Hierarchical Extrapolation of Latent Features for 3D Reconstruction from Sparse-Views**|由于视图重叠最小，从稀疏的朝外视图重建无边界的室外场景带来了重大挑战。以前的方法通常缺乏跨场景理解，其以原始为中心的公式会过载局部特征以补偿缺失的全局上下文，导致场景中看不见的部分模糊。我们提出了sshELF，这是一种通过潜在特征的分层外推进行稀疏视图3D场景重建的快速单镜头流水线。我们的关键见解是，从原始解码中提取信息外推，可以在训练场景中有效地传递结构模式。我们的方法：（1）学习跨场景先验来生成中间虚拟视图，以外推到未观察到的区域，（2）提供了一种将虚拟视图生成与3D原始解码分离的两阶段网络设计，用于高效训练和模块化模型设计，（3）集成了一个预训练的基础模型，用于联合推断潜在特征和纹理，提高了场景理解和泛化能力。sshELF可以从六个稀疏输入视图重建360度场景，并在合成和现实数据集上取得有竞争力的结果。我们发现sshELF忠实地重建了闭塞区域，支持实时渲染，并为下游应用提供了丰富的潜在特征。代码将被发布。 et.al.|[2502.04318](http://arxiv.org/abs/2502.04318)|null|
|**2025-02-05**|**Enhancing Free-hand 3D Photoacoustic and Ultrasound Reconstruction using Deep Learning**|本研究介绍了一种基于运动的学习网络，该网络具有全局局部自关注模块（MoGLo-Net），可增强手持光声和超声（PAUS）成像中的3D重建。标准PAUS成像通常受到视野狭窄和无法有效可视化复杂3D结构的限制。3D徒手技术对齐连续的2D图像进行3D重建，在不依赖外部位置传感器的情况下进行精确的运动估计方面面临着重大挑战。MoGLo-Net通过创新的自我关注机制来解决这些局限性，该机制有效地利用了关键区域，如连续超声图像中完全发育的斑点区域或高回声组织区域，以准确估计运动参数。这有助于从单个帧中提取复杂的特征。此外，我们设计了一种逐块相关操作，以生成与扫描运动高度相关的相关体积。还开发了一个自定义损失函数，以确保在最小化偏差的情况下进行鲁棒学习，利用运动参数的特性。实验评估表明，MoGLo-Net在定量和定性性能指标方面都超越了当前最先进的方法。此外，我们将3D重建技术的应用扩展到简单的B型超声体积之外，以结合多普勒超声和光声成像，实现血管系统的3D可视化。本研究的源代码可在以下网址公开获取：https://github.com/guhong3648/US3D et.al.|[2502.03505](http://arxiv.org/abs/2502.03505)|null|
|**2025-02-05**|**Dress-1-to-3: Single Image to Simulation-Ready 3D Outfit with Diffusion Prior and Differentiable Physics**|大型模型的最新进展显著推进了图像到3D的重建。然而，生成的模型通常被融合成一个整体，限制了它们在下游任务中的适用性。本文主要研究3D服装生成，这是动态服装动画虚拟试穿等应用的一个关键领域，这些应用要求服装是可分离的，并且可以进行模拟。我们介绍Dress1-to-3，这是一种新颖的管道，可以从野外图像中重建具有缝制图案和人类的物理上合理的、可模拟的分离服装。从图像开始，我们的方法将预训练的图像与用于创建粗略缝制图案的缝制图案生成模型与预训练的多视图扩散模型相结合，以生成多视图图像。基于生成的多视图图像，使用可区分的服装模拟器进一步细化缝制图案。多功能实验表明，我们的优化方法大大增强了重建的3D服装和人类与输入图像的几何对齐。此外，通过集成纹理生成模块和人体运动生成模块，我们生成了定制的物理逼真的动态服装演示。项目页面：https://dress-1-to-3.github.io/ et.al.|[2502.03449](http://arxiv.org/abs/2502.03449)|null|
|**2025-02-04**|**SiLVR: Scalable Lidar-Visual Radiance Field Reconstruction with Uncertainty Quantification**|我们提出了一种基于神经辐射场（NeRF）的大规模重建系统，该系统将激光雷达和视觉数据融合在一起，生成高质量的重建，这些重建具有几何精度，并能捕捉到逼真的纹理。我们的系统采用了最先进的NeRF表示法，额外集成了激光雷达。添加激光雷达数据会对深度和表面法线添加强烈的几何约束，这在建模包含模糊视觉重建线索的均匀纹理表面时特别有用。此外，我们将重建的认知不确定性估计为给定相机和激光雷达的传感器观测值的辐射场中每个点位置的空间方差。这使得能够识别由每种传感器模态可靠重建的区域，从而允许根据估计的不确定性对地图进行滤波。我们的系统还可以利用实时位姿图激光雷达SLAM系统在在线映射过程中产生的轨迹，引导（后处理）运动结构（SfM）重建过程，将SfM训练时间减少高达70%。它还有助于正确约束对激光雷达深度损失至关重要的整体度量尺度。然后，可以使用光谱聚类将全局一致的轨迹划分为子图，将共视图像集分组在一起。这种子映射方法比基于距离的分割更适合视觉重建。根据逐点不确定性估计对每个子图进行滤波并合并，以获得最终的大规模3D重建。我们在涉及机器人安装和手持扫描的实验中演示了使用多摄像头激光雷达传感器套件的重建系统。我们的测试数据集覆盖了20000多平方米的总面积，包括多座大学建筑和一座多层建筑的航空测量。 et.al.|[2502.02657](http://arxiv.org/abs/2502.02657)|null|
|**2025-02-05**|**GP-GS: Gaussian Processes for Enhanced Gaussian Splatting**|3D高斯散斑已经成为一种高效的真实感新型视图合成方法。然而，它对稀疏运动结构（SfM）点云的依赖一直会损害场景重建的质量。为了解决这些局限性，本文提出了一种新的3D重建框架高斯过程高斯散斑（GP-GS），其中开发了一个多输出高斯过程模型，以实现稀疏SfM点云的自适应和不确定性引导的致密化。具体来说，我们提出了一种动态采样和滤波流水线，通过利用基于GP的预测从输入的2D像素和深度图中推断出新的候选点，自适应地扩展SfM点云。该管道利用不确定性估计来指导高方差预测的修剪，确保几何一致性，并能够生成密集的点云。加密的点云提供了高质量的初始3D高斯分布，以提高重建性能。在各种规模的合成和真实世界数据集上进行的广泛实验验证了所提出框架的有效性和实用性。 et.al.|[2502.02283](http://arxiv.org/abs/2502.02283)|null|
|**2025-02-04**|**Mask-informed Deep Contrastive Incomplete Multi-view Clustering**|多视图聚类（MvC）利用来自多个视图的信息来揭示数据的底层结构。尽管多视图控制取得了重大进展，但减轻特定视图中缺失样本对不同视图知识整合的影响仍然是一个关键挑战。本文提出了一种新的掩模通知深度对比不完整多视图聚类（Mask IMvC）方法，该方法优雅地识别了一种用于聚类的视图公共表示。具体来说，我们引入了一种掩模通知融合网络，该网络在将不同视图上的样本观察状态视为掩模的同时聚合不完整的多视图信息，从而减少了缺失值的不利影响。此外，我们设计了一种先验知识辅助的对比学习损失，通过注入来自不同视图的样本的邻域信息来提高聚合视图公共表示的表示能力。最后，进行了广泛的实验，以证明所提出的Mask IMvC方法在完整和不完整场景下，在多个MvC数据集上优于最先进的方法。 et.al.|[2502.02234](http://arxiv.org/abs/2502.02234)|null|

<p align=right>(<a href=#updated-on-20250211>back to top</a>)</p>

## Diffusion

|Publish Date|Title|Abstract|PDF|Code|
|---|---|---|---|---|
|**2025-02-10**|**Lumina-Video: Efficient and Flexible Video Generation with Multi-scale Next-DiT**|最近的进展已经将扩散变换器（DiTs）确立为生成建模中的主导框架。在这一成功的基础上，Lumina Next在使用Next DiT生成逼真图像方面取得了卓越的性能。然而，它在视频生成方面的潜力在很大程度上仍未得到开发，在对视频数据固有的时空复杂性进行建模方面存在重大挑战。为了解决这个问题，我们引入了Lumina Video，这是一个利用Next DiT优势的框架，同时为视频合成引入了量身定制的解决方案。Lumina Video采用了多尺度Next DiT架构，该架构联合学习多个拼接，以提高效率和灵活性。通过将运动分数作为显式条件，Lumina Video还可以直接控制生成视频的动态程度。结合分辨率和FPS越来越高的渐进式训练方案，以及混合自然和合成数据的多源训练方案，Lumina Video在高训练和推理效率下实现了卓越的美学质量和运动平滑度。我们还提出了Lumina-V2A，一种基于Next DiT的视频到音频模型，为生成的视频创建同步声音。代码发布于https://www.github.com/Alpha-VLLM/Lumina-Video. et.al.|[2502.06782](http://arxiv.org/abs/2502.06782)|null|
|**2025-02-10**|**Train for the Worst, Plan for the Best: Understanding Token Ordering in Masked Diffusions**|近年来，掩蔽扩散模型（MDMs）已成为离散域生成建模的一种有前景的替代方法。与自回归模型（ARM）相比，MDMs在训练时的复杂性与推理时的灵活性之间进行了权衡。在训练时，他们必须学会解决指数级的大量填充问题，但在推理时，他们可以以基本上任意的顺序解码令牌。在这项工作中，我们仔细研究了这两种相互竞争的效应。在训练方面，我们从理论和实证上证明，与自回归对应物相比，MDMs确实在计算上难以处理的子问题上进行训练。在推理方面，我们表明，自适应选择令牌解码顺序的合适策略显著提高了MDM的能力，使其能够避开硬子问题。在数独等逻辑谜题中，我们发现自适应推理可以将预训练的MDMs的求解精度从 $<7$%提高到$\near 90$%，甚至优于参数数量为$7\times$ 且通过教师强制学习正确解码顺序进行明确训练的ARM。 et.al.|[2502.06768](http://arxiv.org/abs/2502.06768)|null|
|**2025-02-10**|**History-Guided Video Diffusion**|无分类器引导（CFG）是改进扩散模型中条件生成的关键技术，可以在提高样本质量的同时实现更精确的控制。将这种技术扩展到视频扩散是很自然的，视频扩散生成以可变数量的上下文帧为条件的视频，统称为历史。然而，我们发现使用可变长度历史进行指导存在两个关键挑战：仅支持固定大小条件的架构，以及CFG风格历史丢失表现不佳的实证观察。为了解决这个问题，我们提出了扩散强制变换器（DFoT），这是一种视频扩散架构和理论上有根据的训练目标，可以共同对灵活数量的历史帧进行调节。然后，我们介绍历史指导，这是DFoT独有的一系列指导方法。我们发现，其最简单的形式，香草历史指导，已经显著提高了视频生成质量和时间一致性。一种更先进的方法，跨时间和频率的历史引导，进一步增强了运动动力学，能够对分布历史进行合成泛化，并可以稳定地推出超长视频。网站：https://boyuan.space/history-guidance et.al.|[2502.06764](http://arxiv.org/abs/2502.06764)|null|
|**2025-02-10**|**Persistent spin grids with spin-orbit coupled 2D electron gas**|我们考虑了在窄通道网格内具有自旋轨道耦合的二维电子气的扩散自旋动力学。我们发现，这种网格中某些自旋分布的寿命大大超过了无约束二维电子气中的寿命，并且随着沟道宽度接近零而发散。如果电子自旋方向在围绕网格板扩散后保持不变，则会出现这种持久的自旋网格。我们建立一个拓扑 $\mathbb{Z}_2$ 对持久自旋网格进行分类，并推测该设置可用于模拟非阿贝尔晶格规范理论。 et.al.|[2502.06745](http://arxiv.org/abs/2502.06745)|null|
|**2025-02-10**|**Spatial Pattern Formation in Eco-Evolutionary Games with Environment-Driven Motion**|公共资源的可持续管理往往导致一种被称为“公地悲剧”的社会困境：个人受益于资源的快速开采，而整个社区则受益于更可持续的开采策略。这种社会困境可能会因空间对资源和收割机的作用而进一步复杂化，其中资源的空间扩散和收割机的定向运动可能会成为环境资源集群和可持续收割策略出现的潜在特征。本文探索了一个具有环境反馈的进化博弈论PDE模型，描述了资源开采策略和环境资源的空间分布如何因局部生态进化动力学和环境驱动的收割机定向运动而变化。通过线性稳定性分析，我们表明，这种向更高质量环境的偏向运动会导致提取策略分布的空间模式，从而创建环境质量得到改善的局部区域，并增加资源提取器的回报。然而，通过测量整个空间域的平均收益和环境质量，我们看到，在没有空间运动的情况下，这种模式形成机制实际上会降低种群相对于均衡结果的整体成功率。这表明，环境驱动的运动会产生一种空间社会困境，在这种困境中，偏向于更有利地区的运动会导致人口整体环境恶化的新兴模式。 et.al.|[2502.06723](http://arxiv.org/abs/2502.06723)|null|
|**2025-02-10**|**Neumann eigenmaps for landmark embedding**|我们提出了Neumann特征图（NeuMaps），这是一种使用界标（即数据集中的区分样本）增强标准扩散图嵌入的新方法。通过将这些地标解释为更大数据图的子图，NeuMaps是通过重整化Neumann拉普拉斯算子的本征分解获得的。我们证明NeuMaps提供了两个关键优势：（1）它们提供了一种计算高效的嵌入，可以准确地恢复与子图上的反射随机游走相关的扩散距离，（2）它们通过离散的Neumann边界条件在扩散图框架内自然地结合了Nystrom扩展。通过数字分类和分子动力学中的例子，我们证明NeuMap不仅改进了现有的基于地标的嵌入方法，而且提高了扩散图嵌入的稳定性，以去除高度显著的点。 et.al.|[2502.06689](http://arxiv.org/abs/2502.06689)|null|
|**2025-02-10**|**Transfer Your Perspective: Controllable 3D Generation from Any Viewpoint in a Driving Scene**|仅依赖自我中心感知的自动驾驶汽车在感知方面面临局限性，往往无法检测到被遮挡的遥远物体。协作自动驾驶（CAV）似乎是一个有前景的方向，但收集数据用于开发并非易事。它需要在现实世界的驾驶场景中同时放置多个配备传感器的代理！因此，现有的数据集在位置和代理方面是有限的。我们引入了一种新的替代品来进行救援，即在驾驶场景中从不同的角度生成逼真的感知，以现实世界的样本——自我汽车的感官数据为条件。这个替代品具有巨大的潜力：它有可能将任何自我汽车数据集转化为协作驾驶数据集，以扩大CAV的开发规模。我们提出了第一个解决方案，结合了模拟的协作数据和真实的自我汽车数据。我们的方法，转移你的视角（TYP），学习一个条件扩散模型，其输出样本不仅真实，而且在语义和布局上与给定的自我汽车数据一致。实证结果证明了TYP在CAV环境中的有效性。特别是，TYP使我们能够（预）训练协作感知算法，如早期和晚期融合，很少或没有真实世界的协作数据，极大地促进了下游CAV应用。 et.al.|[2502.06682](http://arxiv.org/abs/2502.06682)|null|
|**2025-02-10**|**Unleashing the Potential of Pre-Trained Diffusion Models for Generalizable Person Re-Identification**|域可泛化重新识别（DG re ID）旨在在一个或多个源域上训练模型，并评估其在看不见的目标域上的性能，这项任务因其实际相关性而引起了越来越多的关注。虽然已经提出了许多方法，但大多数方法都依赖于判别或对比学习框架来学习可泛化的特征表示。然而，这些方法往往无法缓解快捷学习，导致性能不佳。在这项工作中，我们提出了一种称为扩散模型辅助表示学习的新方法，该方法使用相关感知条件化方案（DCAC）来增强DG Re-ID。我们的方法通过相关感知的条件化方案将判别和对比的Re-ID模型与预训练的扩散模型相结合。通过将Re-ID模型生成的ID分类概率与一组可学习的ID提示相结合，条件化方案注入了捕获ID相关性的暗知识，以指导扩散过程。同时，来自扩散模型的反馈通过调节方案反向传播到Re-ID模型，有效地提高了Re-ID特征的泛化能力。在单源和多源DG Re ID任务上的广泛实验表明，我们的方法达到了最先进的性能。全面的消融研究进一步验证了所提出方法的有效性，为其稳健性提供了见解。代码将在以下网址提供https://github.com/RikoLi/DCAC. et.al.|[2502.06619](http://arxiv.org/abs/2502.06619)|null|
|**2025-02-10**|**TripoSG: High-Fidelity 3D Shape Synthesis using Large-Scale Rectified Flow Models**|扩散技术的最新进展将图像和视频生成推向了前所未有的质量水平，显著加速了生成式人工智能的部署和应用。然而，由于3D数据规模的限制、3D数据处理的复杂性以及对3D领域先进技术的探索不足，3D形状生成技术迄今为止一直落后。当前的3D形状生成方法在输出质量、泛化能力和与输入条件的对齐方面面临着巨大的挑战。我们提出了TripoSG，这是一种新的流线型形状扩散范式，能够生成与输入图像精确对应的高保真3D网格。具体来说，我们提出：1）一种用于3D形状生成的大型整流流量变换器，通过对大量高质量数据的训练实现最先进的保真度。2） 一种混合监督训练策略，结合SDF、正常损失和程知损失，用于3D VAE，实现高质量的3D重建性能。3） 一个数据处理管道，用于生成200万个高质量的3D样本，突出了训练3D生成模型时数据质量和数量的关键规则。通过全面的实验，我们验证了新框架中每个组件的有效性。这些部件的无缝集成使TripoSG在3D形状生成方面达到了最先进的性能。由于高分辨率功能，由此产生的3D形状显示出增强的细节，并对输入图像表现出卓越的保真度。此外，TripoSG在从不同的图像风格和内容生成3D模型方面表现出了更强的通用性，展示了强大的生成能力。为了促进3D生成领域的进步和创新，我们将公开我们的模型。 et.al.|[2502.06608](http://arxiv.org/abs/2502.06608)|null|
|**2025-02-10**|**MaterialFusion: High-Quality, Zero-Shot, and Controllable Material Transfer with Diffusion Models**|操纵图像中物体的物质外观对于增强现实、虚拟原型和数字内容创建等应用至关重要。我们介绍了MaterialFusion，这是一种用于高质量材料转移的新型框架，允许用户调整材料应用程度，在新材料特性和物体原始特征之间实现最佳平衡。MaterialFusion通过保持背景一致性和减轻边界伪影，将修改后的对象无缝集成到场景中。为了全面评估我们的方法，我们编制了一个真实世界材料转移示例的数据集，并进行了复杂的比较分析。通过全面的定量评估和用户研究，我们证明MaterialFusion在质量、用户控制和背景保护方面明显优于现有方法。代码可在以下网址获得https://github.com/kzGarifullin/MaterialFusion. et.al.|[2502.06606](http://arxiv.org/abs/2502.06606)|null|

<p align=right>(<a href=#updated-on-20250211>back to top</a>)</p>

## NeRF

|Publish Date|Title|Abstract|PDF|Code|
|---|---|---|---|---|
|**2025-02-05**|**Poisson Hypothesis and large-population limit for networks of spiking neurons**|我们研究了具有随机尖峰时间的线性（泄漏）和二次积分和放电神经元的空间扩展网络的平均场描述。我们考虑了具有线性和二次内在动力学的连续时间Galves-L“ocherbach（GL）网络的大种群极限。我们证明了泊松假设适用于这些网络的复制平均场极限，即在适当定义的极限内，神经元是独立的，相互作用时间被强度取决于平均放电率的独立时间非均匀泊松过程所取代，将已知结果扩展到具有二次内在动态和重置的网络。证明泊松假设成立为研究这些网络中的大种群限值开辟了可能性。我们证明这个极限是一个适定的神经场模型，受随机重置的影响。 et.al.|[2502.03379](http://arxiv.org/abs/2502.03379)|null|
|**2025-02-04**|**Geometric Neural Process Fields**|本文解决了神经场（NeF）泛化的挑战，其中模型必须有效地适应仅给出少量观测值的新信号。为了解决这个问题，我们提出了几何神经过程场（G-NPF），这是一个明确捕捉不确定性的神经辐射场的概率框架。我们将NeF泛化表述为概率问题，从而能够从有限的上下文观测中直接推断出NeF函数分布。为了引入结构归纳偏差，我们引入了一组几何基来编码空间结构，并促进NeF函数分布的推断。在此基础上，我们设计了一个分层潜在变量模型，使G-NPF能够整合多个空间层次的结构信息，并有效地参数化INR函数。这种分层方法提高了对新场景和未知信号的泛化能力。针对3D场景的新颖视图合成以及2D图像和1D信号回归的实验证明了我们的方法在捕捉不确定性和利用结构信息提高泛化能力方面的有效性。 et.al.|[2502.02338](http://arxiv.org/abs/2502.02338)|null|
|**2025-02-05**|**A Poisson Process AutoDecoder for X-ray Sources**|钱德拉X射线天文台和eROSITA等X射线观测设施已经探测到数百万个与高能现象相关的天文源。光子的到达作为时间的函数遵循泊松过程，并且可以按数量级变化，这为源分类、物理性质推导和异常检测等常见任务带来了障碍。之前的工作要么未能直接捕捉数据的泊松性质，要么只关注泊松率函数重建。在这项工作中，我们提出了泊松过程自动解码器（PPAD）。PPAD是一种神经场解码器，通过无监督学习将固定长度的潜在特征映射到跨能带和时间的连续泊松率函数。PPAD重建速率函数并同时产生表示。我们使用钱德拉源目录通过重建、回归、分类和异常检测实验证明了PPAD的有效性。 et.al.|[2502.01627](http://arxiv.org/abs/2502.01627)|null|
|**2025-02-03**|**Regularized interpolation in 4D neural fields enables optimization of 3D printed geometries**|精确生产具有特定特性的几何形状的能力可能是制造过程中最重要的特征。3D打印具有非凡的设计自由度和复杂性，但也容易出现几何和其他缺陷，必须解决这些缺陷才能充分发挥其潜力。最终，这将需要精明的设计决策和及时的参数调整来保持稳定性，即使是专业的人类操作员也很难做到这一点。虽然机器学习在3D打印中得到了广泛的研究，但现有的方法通常会忽略不同打印的空间特征，因此很难产生所需的几何形状。在这里，我们将打印部件的体积表示编码到神经场中，并应用一种新的正则化策略，该策略基于最小化场输出相对于单个不可学习参数的偏导数。因此，通过鼓励小的输入变化只产生小的输出变化，我们鼓励在观测体积之间进行平滑插值，从而实现现实的几何预测。因此，该框架允许提取“想象的”3D形状，揭示了在以前看不见的参数下制造的零件的外观。由此产生的连续场用于数据驱动优化，以最大限度地提高预期和生产几何形状之间的几何保真度，减少后处理、材料浪费和生产成本。通过动态优化工艺参数，我们的方法实现了先进的规划策略，有可能使制造商更好地实现复杂和功能丰富的设计。 et.al.|[2502.01517](http://arxiv.org/abs/2502.01517)|null|
|**2025-02-03**|**Modelling change in neural dynamics during phonetic accommodation**|短期语音调节是口音变化背后的基本驱动力，但来自另一个说话者声音的实时输入是如何塑造对话者的语音规划表示的？我们基于运动规划和记忆动力学的动态神经场方程，提出了一种语音调节过程中语音表征变化的计算模型。我们测试了该模型从实验研究中捕捉经验模式的能力，在实验研究中，说话者用与自己不同的口音跟踪模型说话者。实验数据显示了阴影期间元音特定的收敛程度，随后在阴影后恢复到基线（或轻微发散）。该模型可以通过调节抑制性记忆动力学的大小来再现这些现象，这可能反映了由于语音和/或社会语言压力导致的对调节的抵抗。我们讨论了这些结果对短期语音调节和长期声音变化模式之间关系的影响。 et.al.|[2502.01210](http://arxiv.org/abs/2502.01210)|null|
|**2025-02-02**|**Lifting the Winding Number: Precise Representation of Complex Cuts in Subspace Physics Simulations**|切割薄壁可变形结构在日常生活中很常见，但由于引入了空间不连续性，给模拟带来了重大挑战。传统方法依赖于基于网格的域表示，这需要频繁的重新网格划分和细化，以准确捕捉不断变化的不连续性。这些挑战在缩减空间模拟中进一步加剧，在这种模拟中，基函数固有地依赖于几何和网格，使得基难以甚至不可能表示切割引入的各种不连续性。用神经场表示基函数的最新进展提供了一种有前景的替代方案，利用其离散化不可知的性质来表示不同几何形状的变形。然而，神经场的固有连续性阻碍了泛化，特别是在神经网络权重中编码了不连续性的情况下。我们提出了Wind-Lifter，这是一种新的神经表示，旨在精确模拟薄壁可变形结构中的复杂切割。我们的方法构建神经场，在指定位置精确再现不连续性，而无需在切割线的位置烘烤。至关重要的是，我们的方法没有将不连续性嵌入神经网络的权重中，为切割位置的泛化开辟了道路。我们的方法实现了实时仿真速度，并支持在仿真过程中动态更新切割线几何形状。此外，不连续性的显式表示使我们的神经场易于控制和编辑，与传统的神经场相比具有显著的优势，在传统的神经场内，不连续被嵌入网络的权重中，并支持依赖于一般切割位置的新应用。 et.al.|[2502.00626](http://arxiv.org/abs/2502.00626)|null|
|**2025-01-31**|**Lifting by Gaussians: A Simple, Fast and Flexible Method for 3D Instance Segmentation**|我们介绍了一种新的三维高斯散斑辐射场（3DGS）开放世界实例分割方法——高斯提升（LBG）。最近，3DGS场已经成为基于神经场的高质量新视图合成方法的高效和明确的替代方案。我们的3D实例分割方法直接从SAM（或FastSAM等）中提取2D分割掩模，以及CLIP和DINOv2的特征，直接将它们融合到3DGS（或类似的高斯辐射场，如2DGS）上。与以前的方法不同，LBG不需要每个场景的训练，使其能够在任何现有的3DGS重建上无缝运行。我们的方法不仅比现有方法快一个数量级，而且更简单；它也是高度模块化的，能够对现有的3DGS字段进行3D语义分割，而不需要对3D高斯进行特定的参数化。此外，我们的技术在保持灵活性和效率的同时，为2D语义新颖视图合成和3D资产提取结果实现了卓越的语义分割。我们进一步介绍了一种从3D辐射场分割方法中评估单独分割的3D资产的新方法。 et.al.|[2502.00173](http://arxiv.org/abs/2502.00173)|null|
|**2025-01-30**|**Zero-Shot Novel View and Depth Synthesis with Multi-View Geometric Diffusion**|从稀疏姿态图像重建3D场景的当前方法采用中间3D表示，如神经场、体素网格或3D高斯，以实现多视图一致的场景外观和几何形状。本文介绍了MVGD，这是一种基于扩散的架构，能够在给定任意数量的输入视图的情况下，从新的视点直接生成像素级的图像和深度图。我们的方法使用光线图调节来增强来自不同视点的空间信息的视觉特征，并指导从新视图生成图像和深度图。我们方法的一个关键方面是图像和深度图的多任务生成，使用可学习的任务嵌入来指导向特定模态的扩散过程。我们从公开可用的数据集中收集了6000多万个多视图样本来训练这个模型，并提出了在这种不同条件下实现高效和一致学习的技术。我们还提出了一种新策略，通过逐步微调较小的模型，实现了对较大模型的有效训练，并具有很好的扩展行为。通过广泛的实验，我们报告了多个新颖的视图合成基准以及多视图立体和视频深度估计的最新结果。 et.al.|[2501.18804](http://arxiv.org/abs/2501.18804)|null|
|**2025-01-22**|**Retrieval-Augmented Neural Field for HRTF Upsampling and Personalization**|具有密集空间网格的头部相关传递函数（HRTF）是沉浸式双耳音频生成的理想选择，但它们的记录很耗时。尽管HRTF空间上采样在神经场方面取得了显著进展，但仅从几个测量方向（例如3或5个测量方向）进行空间上采样仍然具有挑战性。为了解决这个问题，我们提出了一种检索增强神经场（RANF）。RANF从数据集中检索HRTF接近目标受试者HRTF的受试者。除了声源方向本身之外，检索到的对象在所需方向上的HRTF也被馈送到神经场中。此外，我们提出了一种神经网络，它可以有效地处理多个检索到的主题，灵感来自一种称为变换平均连接的多通道处理技术。我们的实验证实了RANF在SONICOM数据集上的优势，它是2024年听众声学个性化挑战任务2获胜解决方案的关键组成部分。 et.al.|[2501.13017](http://arxiv.org/abs/2501.13017)|**[link](https://github.com/merlresearch/ranf-hrtf)**|
|**2025-01-15**|**CityDreamer4D: Compositional Generative Model of Unbounded 4D Cities**|近年来，3D场景生成引起了越来越多的关注，并取得了重大进展。生成4D城市比3D场景更具挑战性，因为存在结构复杂、视觉多样的物体，如建筑物和车辆，并且人类对城市环境中的扭曲更加敏感。为了解决这些问题，我们提出了CityDreamer4D，这是一个专门为生成无界4D城市而定制的组合生成模型。我们的主要见解是1）4D城市生成应该将动态对象（如车辆）与静态场景（如建筑物和道路）分开，2）4D场景中的所有对象都应该由建筑物、车辆和背景材料的不同类型的神经场组成。具体来说，我们提出了交通场景生成器和无边界布局生成器，使用高度紧凑的BEV表示生成动态交通场景和静态城市布局。4D城市中的对象是通过结合面向对象和面向实例的神经场来生成的，用于背景材料、建筑物和车辆。为了适应背景材料和实例的不同特征，神经场采用定制的生成哈希网格和周期性位置嵌入作为场景参数化。此外，我们还为城市生成提供了一套全面的数据集，包括OSM、GoogleEarth和CityTopia。OSM数据集提供了各种真实世界的城市布局，而谷歌地球和CityTopia数据集则提供了大规模、高质量的城市图像，并附有3D实例注释。利用其组合设计，CityDreamer4D支持一系列下游应用程序，如实例编辑、城市风格化和城市模拟，同时在生成逼真的4D城市方面提供最先进的性能。 et.al.|[2501.08983](http://arxiv.org/abs/2501.08983)|**[link](https://github.com/hzxie/CityDreamer4D)**|

<p align=right>(<a href=#updated-on-20250211>back to top</a>)</p>

[contributors-shield]: https://img.shields.io/github/contributors/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[contributors-url]: https://github.com/Vincentqyw/cv-arxiv-daily/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[forks-url]: https://github.com/Vincentqyw/cv-arxiv-daily/network/members
[stars-shield]: https://img.shields.io/github/stars/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[stars-url]: https://github.com/Vincentqyw/cv-arxiv-daily/stargazers
[issues-shield]: https://img.shields.io/github/issues/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[issues-url]: https://github.com/Vincentqyw/cv-arxiv-daily/issues

