[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]

## Updated on 2025.04.17
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
|**2025-04-15**|**NormalCrafter: Learning Temporally Consistent Normals from Video Diffusion Priors**|表面法线估计是一系列计算机视觉应用的基石。尽管已经对静态图像场景进行了大量研究，但确保基于视频的正常估计中的时间一致性仍然是一个艰巨的挑战。我们提出NormalCrafter来利用视频扩散模型的固有时间先验，而不是仅仅用时间分量来增强现有的方法。为了确保跨序列的高保真正态估计，我们提出了语义特征正则化（SFR），它将扩散特征与语义线索对齐，鼓励模型专注于场景的内在语义。此外，我们引入了一种两阶段训练协议，该协议利用潜在和像素空间学习来保持空间精度，同时保持长时间上下文。广泛的评估证明了我们的方法的有效性，展示了从不同视频中生成具有复杂细节的时间一致的正常序列的卓越性能。 et.al.|[2504.11427](http://arxiv.org/abs/2504.11427)|null|
|**2025-04-15**|**VideoPanda: Video Panoramic Diffusion with Multi-view Attention**|高分辨率全景视频内容对于虚拟现实中的沉浸式体验至关重要，但收集起来并不容易，因为它需要专门的设备和复杂的相机设置。在这项工作中，我们介绍了VideoPanda，这是一种基于文本或单视图视频数据合成360度视频的新方法。VideoPanda利用多视图注意力层来增强视频扩散模型，使其能够生成一致的多视图视频，这些视频可以组合成沉浸式全景内容。VideoPanda使用两种条件联合训练：纯文本和单视图视频，并支持长视频的自回归生成。为了克服多视图视频生成的计算负担，我们随机对训练过程中使用的持续时间和相机视图进行子采样，并表明该模型能够优雅地推广到在推理过程中生成更多帧。对真实世界和合成视频数据集的广泛评估表明，与现有方法相比，VideoPanda在所有输入条件下生成了更逼真、更连贯的360度全景图。访问项目网站https://research-staging.nvidia.com/labs/toronto-ai/VideoPanda/为了获得结果。 et.al.|[2504.11389](http://arxiv.org/abs/2504.11389)|null|
|**2025-04-15**|**UniAnimate-DiT: Human Image Animation with Large-Scale Video Diffusion Transformer**|本报告介绍了UniAnimate DiT，这是一个先进的项目，利用开源Wan2.1模型的尖端和强大功能，实现一致的人体图像动画。具体来说，为了保持原始Wan2.1模型的稳健生成能力，我们实现了低秩自适应（LoRA）技术来微调一组最小的参数，从而显著降低了训练内存开销。设计了一种由多个堆叠的3D卷积层组成的轻量级姿态编码器，用于对驱动姿态的运动信息进行编码。此外，我们采用简单的级联操作将参考外观集成到模型中，并结合参考图像的姿态信息以增强姿态对齐。实验结果表明，我们的方法实现了视觉上呈现和时间上一致的高保真动画。经过480p（832x480）视频的训练，UniAnimate DiT展示了强大的泛化能力，可以在推理过程中无缝升级到720P（1280x720）。训练和推理代码可在以下网址公开获取https://github.com/ali-vilab/UniAnimate-DiT. et.al.|[2504.11289](http://arxiv.org/abs/2504.11289)|null|
|**2025-04-15**|**Taming Consistency Distillation for Accelerated Human Image Animation**|视频扩散模型推动了人类图像动画的最新进展，但它们对大量迭代去噪步骤的依赖导致了高推理成本和低速度。一个直观的解决方案是采用一致性模型，通过一致性蒸馏作为有效的加速范式。然而，在人类图像动画中简单地采用这种策略往往会导致质量下降，包括视觉模糊、运动退化和面部失真，特别是在动态区域。在这篇论文中，我们提出了DanceLCM方法，并辅以几项增强措施，以提高低阶状态下的视觉质量和运动连续性：（1）分段一致性蒸馏，带有辅助的轻量级头部，以结合来自真实视频延迟的监督，减轻了由单个完整轨迹生成引起的累积误差；（2） 以运动为中心的损失以运动区域为中心，以及明确注入面部保真度特征以提高面部真实性。大量的定性和定量实验表明，DanceLCM仅需2-4个推理步骤即可实现与最先进的视频扩散模型相当的结果，在不影响视频质量的情况下显著减轻了推理负担。代码和模型将公开。 et.al.|[2504.11143](http://arxiv.org/abs/2504.11143)|null|
|**2025-04-15**|**InterAnimate: Taming Region-aware Diffusion Model for Realistic Human Interaction Animation**|最近的视频生成研究主要集中在孤立的动作上，而手-脸交互等交互式动作基本上没有得到研究。这些交互对于新兴的生物特征认证系统至关重要，这些系统依赖于基于交互式运动的反欺骗方法。从安全角度来看，越来越需要大规模、高质量的交互式视频来训练和加强身份验证模型。在这项工作中，我们介绍了一种新的范式，用于制作逼真的手-脸交互动画。我们的方法同时学习时空接触动力学和生物力学上合理的变形效应，实现了自然交互，其中手部运动会引起解剖学上精确的面部变形，同时保持无碰撞接触。为了促进这项研究，我们提出了InterHF，这是一个大规模的人脸交互数据集，包含18种交互模式和90000个带注释的视频。此外，我们提出了InterAnimate，这是一种专门为交互动画设计的区域感知扩散模型。InterAnimate利用可学习的空间和时间延迟来有效地捕获动态交互先验，并集成了一种区域感知交互机制，将这些先验注入去噪过程。据我们所知，这项工作代表了首次大规模系统研究人脸交互的努力。定性和定量结果表明，InterAnimate制作了高度逼真的动画，树立了新的基准。代码和数据将公开以推进研究。 et.al.|[2504.10905](http://arxiv.org/abs/2504.10905)|null|
|**2025-04-15**|**OmniVDiff: Omni Controllable Video Diffusion for Generation and Understanding**|本文提出了一种新的可控视频扩散框架OmniVDiff，旨在在单个扩散模型中合成和理解多个视频视觉内容。为了实现这一点，OmniVDiff处理颜色空间中的所有视频视觉模态以学习联合分布，同时采用自适应控制策略，在扩散过程中动态调整每种视觉模态的作用，无论是作为生成模态还是调节模态。这允许灵活操纵每种模态的角色，从而支持广泛的任务。因此，我们的模型支持三个关键功能：（1）文本条件视频生成：在一个扩散过程中，基于文本条件生成多模态视觉视频序列（即rgb、深度、canny、分段）；（2） 视频理解：OmniVDiff可以估计输入rgb帧的深度、canny映射和语义分割，同时确保与rgb输入的一致性；以及（3）X条件视频生成：OmniVDiff生成基于细粒度属性（例如深度图或分割图）的视频。通过将这些不同的任务集成到一个统一的视频传播框架中，OmniVDiff增强了可控视频传播的灵活性和可扩展性，使其成为各种下游应用（如视频到视频翻译）的有效工具。大量的实验证明了我们的方法的有效性，突出了它在各种视频相关应用中的潜力。 et.al.|[2504.10825](http://arxiv.org/abs/2504.10825)|null|
|**2025-04-14**|**H-MoRe: Learning Human-centric Motion Representation for Action Analysis**|在本文中，我们提出了H-MoRe，这是一种用于学习精确的以人为中心的运动表示的新型流水线。我们的方法动态地保留了相关的人体运动，同时过滤掉了背景运动。值得注意的是，与之前依赖于从合成数据中完全监督学习的方法不同，H-MoRe以自我监督的方式直接从现实世界场景中学习，结合了人体姿势和身体形状信息。受运动学的启发，H-MoRe以矩阵格式表示每个身体点的绝对和相对运动，捕捉到细微的运动细节，称为世界局部流。H-MoRe提供了对人体运动的精细洞察，可以无缝集成到各种与动作相关的应用程序中。实验结果表明，H-MoRe在各种下游任务中带来了实质性的改进，包括步态识别(CL@R1：+16.01%），行动识别(Acc@1：+8.92%）和视频生成（FVD:-67.07%）。此外，H-MoRe具有很高的推理效率（34fps），使其适用于大多数实时场景。模型和代码将在发布后发布。 et.al.|[2504.10676](http://arxiv.org/abs/2504.10676)|null|
|**2025-04-14**|**H3AE: High Compression, High Speed, and High Quality AutoEncoder for Video Diffusion Models**|自编码器（AE）是图像和视频生成潜在扩散模型成功的关键，它降低了去噪分辨率，提高了效率。然而，在网络设计、压缩比和训练策略方面，AE的力量长期以来一直没有得到充分的探索。在这项工作中，我们系统地研究了架构设计选择，并优化了计算分布，以获得一系列高效、高压缩的视频AE，这些AE可以在移动设备上实时解码。我们还统一了普通自动编码器和图像条件I2V VAE的设计，在单个网络中实现了多功能性。此外，我们发现，广泛采用的判别损失，即GAN、LPIPS和DWT损失，在大规模训练AE时没有显著改善。我们提出了一种新的潜在一致性损失，不需要复杂的鉴别器设计或超参数调整，但可以稳定地提高重建质量。我们的AE在移动设备上实现了超高的压缩比和实时解码速度，同时在重建指标方面大大优于现有技术。我们最终通过在DiT的潜在空间上训练DiT来验证我们的AE，并展示了快速、高质量的文本到视频生成能力。 et.al.|[2504.10567](http://arxiv.org/abs/2504.10567)|null|
|**2025-04-14**|**FingER: Content Aware Fine-grained Evaluation with Reasoning for AI-Generated Videos**|视频生成的最新进展给人工智能生成内容的评估带来了巨大挑战，特别是随着越来越复杂的模型的出现。在这些视频中观察到的各种不一致和缺陷本质上是复杂的，这使得总体评分非常困难。在这篇论文中，我们强调了将细粒度推理集成到视频评估中的至关重要性，并提出了一种新的实体级推理评估框架 $\textbf{F}$ing$\textbf{ER}$，该框架首先自动生成$\textbf{F}$细粒度$\textbf{E}$实体级问题，然后通过一个带有分数的$\textbbf{R}$ 推理模型来回答这些问题，随后可以对不同应用程序的总分进行加权求和。具体来说，我们利用LLM从五个不同的角度得出实体级问题，这些角度（i）通常关注内容的某些特定实体，从而使MLLM更容易回答或评分，并且（ii）更具可解释性。然后我们构建了一个FingER数据集，由大约3.3k个视频和相应的60k个细粒度QA注释组成，每个注释都有详细的原因。在此基础上，我们进一步研究了各种训练协议，以最好地激励MLLM的推理能力进行正确答案预测。大量实验表明，使用具有冷启动策略的组相对策略优化（GRPO）训练的推理模型可以获得最佳性能。值得注意的是，我们的模型在GenAI Bench和MonetBench上分别以11.8美元和5.5美元的相对优势超越了现有的方法，只有3.3k个训练视频，这最多是其他方法使用的训练样本的十分之一。我们的代码和数据集将很快发布。 et.al.|[2504.10358](http://arxiv.org/abs/2504.10358)|null|
|**2025-04-14**|**Analysis of Attention in Video Diffusion Transformers**|我们对视频扩散变压器（VDiTs）中的注意力进行了深入分析，并报告了一些新发现。我们确定了VDiTs中注意力的三个关键属性：结构、稀疏性和下沉。结构：我们观察到，不同VDIT的注意力模式在不同提示下表现出相似的结构，我们可以利用注意力模式的相似性通过自我注意力图转移来解锁视频编辑。稀疏：我们研究了VDiTs中的注意力稀疏性，发现提出的稀疏方法并不适用于所有VDiTs，因为一些看似稀疏的层无法稀疏。水槽：我们首次研究了VDiTs中的注意水槽，将其与语言模型中的注意槽进行了比较和对比。我们提出了一些未来的方向，可以利用我们的见解来提高VDiT的效率质量帕累托前沿。 et.al.|[2504.10317](http://arxiv.org/abs/2504.10317)|null|

<p align=right>(<a href=#updated-on-20250417>back to top</a>)</p>

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

<p align=right>(<a href=#updated-on-20250417>back to top</a>)</p>

## 3D Reconstruction

|Publish Date|Title|Abstract|PDF|Code|
|---|---|---|---|---|
|**2025-04-15**|**Deep Learning-based Bathymetry Retrieval without In-situ Depths using Remote Sensing Imagery and SfM-MVS DSMs with Data Gaps**|准确、详细和高频的测深对于面临强烈气候和人为压力的浅海底区域至关重要。目前利用机载或卫星光学图像进行测深的方法主要依赖于具有折射校正的SfM MVS或光谱衍生测深（SDB）。然而，SDB方法通常需要大量的人工实地考察或昂贵的参考数据，而SfM MVS方法即使在折射校正后也面临着挑战。这些包括具有均匀视觉纹理的环境中的深度数据间隙和噪声，这阻碍了海底准确和完整的数字表面模型（DSM）的创建。为了应对这些挑战，这项工作引入了一种方法，该方法将SfM MVS方法的高保真3D重建能力与最先进的折射校正技术相结合，以及一种新的基于深度学习的测深预测方法的光谱分析能力。这种集成实现了一种协同方法，其中使用具有数据差距的SfM MVS衍生的DSM作为训练数据来生成完整的测深图。在此背景下，我们提出了Swin BathyUNet，它将U-Net与Swin Transformer的自我关注层和专门为SDB量身定制的交叉关注机制相结合。Swin BathyUNet旨在通过捕获长距离空间关系来提高测深精度，也可以作为具有各种训练深度数据的标准SDB的独立解决方案，独立于SfM MVS输出。地中海和波罗的海两个完全不同的测试地点的实验结果通过广泛的实验证明了所提出方法的有效性，这些实验证明了预测的DSM在测深精度、细节、覆盖范围和降噪方面的改进。该代码可在以下网址获得https://github.com/pagraf/Swin-BathyUNet. et.al.|[2504.11416](http://arxiv.org/abs/2504.11416)|null|
|**2025-04-15**|**Explicit and Implicit Representations in AI-based 3D Reconstruction for Radiology: A systematic literature review**|临床实践和辅助诊断对高质量医学成像的需求使放射学成像中的3D重建成为一个关键的研究重点。人工智能（AI）已成为一种有前景的方法，可以提高重建精度，同时减少采集和处理时间，从而最大限度地减少患者的辐射暴露和不适，最终有利于临床诊断。本文探讨了放射学成像中最先进的基于人工智能的3D重建算法，根据其基本原理将其分为显式和隐式方法。显式方法包括基于点、基于体积和高斯表示，而隐式方法包括隐式先验嵌入和神经辐射场。此外，我们还研究了常用的评估指标和基准数据集。最后，我们讨论了这一不断发展的领域的发展现状、关键挑战和未来的研究方向。我们的项目可在以下网址获得：https://github.com/Bean-Young/AI4Med. et.al.|[2504.11349](http://arxiv.org/abs/2504.11349)|null|
|**2025-04-15**|**Super time-resolved tomography**|了解3D基本过程对于学术和工业应用至关重要。如今，X射线时间分辨断层扫描或断层扫描是原位和操作4D（3D+时间）表征的领先技术。尽管它能够在大型X射线设施中实现每秒1000张断层图像，但其适用性受到施加在样品上的离心力以及为这种高速研究开发合适环境的挑战的限制。在这里，我们介绍STRT，这是一种有可能将断层扫描的时间分辨率提高至少一个数量级，同时保持空间分辨率的方法。STRT利用4D DL重建算法在每个时间点产生高保真3D重建，与传统断层扫描的0-180度相比，从显著减小的几度角度范围内检索。因此，与断层扫描相比，STRT将时间分辨率提高了一倍，等于180度与STRT使用的角度范围之间的比率。在这项工作中，我们通过液滴碰撞模拟和增材制造工艺的模拟和实验验证了STRT的4D能力。我们预计STRT将显著扩展4D X射线成像的能力，使以前在学术和工业环境中无法实现的研究成为可能，如材料形成和机械测试。 et.al.|[2504.11148](http://arxiv.org/abs/2504.11148)|null|
|**2025-04-15**|**Easy3D: A Simple Yet Effective Method for 3D Interactive Segmentation**|数字3D环境的可用性越来越高，无论是通过基于图像的3D重建、生成还是机器人获得的扫描，都在推动各种应用的创新。这些都伴随着对3D交互的巨大需求，例如3D交互式分割，这对对象选择和操纵等任务很有用。此外，人们一直需要高效、精确且在各种环境中表现良好的解决方案，特别是在看不见的环境和不熟悉的物体中。在这项工作中，我们介绍了一种3D交互式分割方法，该方法在域内和域外数据集上始终超越了以前最先进的技术。我们的简单方法将基于体素的稀疏编码器与基于轻量级变换器的解码器集成在一起，该解码器实现了隐式点击融合，实现了卓越的性能并最大限度地提高了效率。我们的方法在基准数据集（包括ScanNet、ScanNet++、S3DIS和KITTI-360）上以及在看不见的几何分布（如高斯散斑法获得的分布）上都有实质性的改进。项目网页可在https://simonelli-andrea.github.io/easy3d. et.al.|[2504.11024](http://arxiv.org/abs/2504.11024)|null|
|**2025-04-15**|**ZeroGrasp: Zero-Shot Shape Reconstruction Enabled Robotic Grasping**|机器人抓取是实体系统的基石能力。许多方法直接从部分信息中输出抓取，而不建模场景的几何形状，导致次优运动甚至碰撞。为了解决这些问题，我们引入了ZeroGrasp，这是一种新颖的框架，可以近乎实时地同时执行3D重建和抓取姿态预测。我们方法的一个关键见解是，遮挡推理和对对象之间的空间关系进行建模有利于精确重建和抓取。我们将我们的方法与一个新的大规模合成数据集相结合，该数据集包括来自Objaverse LVIS数据集的12K个对象的1M照片级逼真图像、高分辨率3D重建和11.3B物理有效的抓取姿势注释。我们在GraspNet-1B基准上以及通过现实世界的机器人实验对ZeroGrasp进行了评估。ZeroGrasp通过利用合成数据实现了最先进的性能，并推广到新的现实世界对象。 et.al.|[2504.10857](http://arxiv.org/abs/2504.10857)|null|
|**2025-04-15**|**LL-Gaussian: Low-Light Scene Reconstruction and Enhancement via Gaussian Splatting for Novel View Synthesis**|低光场景中的新型视图合成（NVS）仍然是一个重大挑战，因为输入质量下降，噪声严重，动态范围低（LDR），初始化不可靠。虽然最近基于NeRF的方法显示出有希望的结果，但大多数方法都存在计算成本高的问题，有些方法依赖于仔细捕获或预处理的数据，如RAW传感器输入或多次曝光序列，这严重限制了它们的实用性。相比之下，3D高斯散斑（3DGS）能够以具有竞争力的视觉保真度实现实时渲染；然而，现有的基于3DGS的方法在低光sRGB输入方面存在困难，导致高斯初始化不稳定和噪声抑制无效。为了应对这些挑战，我们提出了LL Gaussian，这是一种用于从低光sRGB图像进行3D重建和增强的新框架，实现了伪正常光新视图合成。我们的方法引入了三个关键创新：1）端到端的低光高斯初始化模块（LLGIM），该模块利用基于学习的MVS方法中的密集先验来生成高质量的初始点云；2） 双分支高斯分解模型，将固有场景属性（反射率和照度）与瞬态干扰分离，实现稳定和可解释的优化；3） 在联合引导分解和增强之前，由物理约束和扩散引导的无监督优化策略。此外，我们还提供了一个在极端低光环境中收集的具有挑战性的数据集，并展示了LL Gaussian的有效性。与最先进的基于NeRF的方法相比，LL Gaussian的推理速度提高了2000倍，训练时间缩短到2%，同时提供了卓越的重建和渲染质量。 et.al.|[2504.10331](http://arxiv.org/abs/2504.10331)|null|
|**2025-04-14**|**TT3D: Table Tennis 3D Reconstruction**|体育分析需要处理大量数据，这既费时又昂贵。神经网络的进步大大减轻了这一负担，在体育广播中实现了高度精确的球跟踪。然而，仅依赖2D球跟踪是有限的，因为它取决于相机的视点，并且不支持全面的游戏分析。为了解决这一局限性，我们提出了一种从在线乒乓球比赛记录中重建精确3D球轨迹的新方法。我们的方法利用球运动的基本物理特性来识别反弹状态，从而最大限度地减少球飞行轨迹的重投影误差，从而确保准确可靠的3D重建。我们的方法的一个关键优势是它能够推断球的旋转，而不依赖于人体姿势估计或球拍跟踪，而这些在广播镜头中通常是不可靠或不可用的。我们开发了一种能够可靠地跟踪相机运动的自动相机校准方法。此外，我们采用了一种现有的3D姿态估计模型，该模型缺乏深度运动捕捉，可以准确地跟踪玩家的动作。这些贡献共同实现了乒乓球拉力赛的完整3D重建。 et.al.|[2504.10035](http://arxiv.org/abs/2504.10035)|null|
|**2025-04-13**|**smFISH_batchRun: A smFISH image processing tool for single-molecule RNA Detection and 3D reconstruction**|随着显微镜方法的最新进展，单分子RNA成像已成为可能。然而，由于高度可变的背景噪声，即使在应用了复杂的计算清除方法后，对这些图像的系统分析也具有挑战性。在这里，我们描述了我们的定制MATLAB脚本，它使我们能够以单分子精度检测活性转录位点（ATS）的核新生转录本和成熟的细胞质mRNA，并在3D中重建组织以进行进一步分析。我们的编码最初针对秀丽隐杆线虫种系进行了优化，但被设计为广泛适用于其他物种和组织类型。 et.al.|[2504.09692](http://arxiv.org/abs/2504.09692)|null|
|**2025-04-13**|**TextSplat: Text-Guided Semantic Fusion for Generalizable Gaussian Splatting**|可泛化高斯散斑的最新进展通过利用前馈高斯散斑模型，实现了从稀疏输入视图进行稳健的3D重建，实现了卓越的跨场景泛化。然而，尽管许多方法侧重于几何一致性，但它们往往忽视了文本驱动引导在增强语义理解方面的潜力，而语义理解对于在复杂场景中准确重建细粒度细节至关重要。为了解决这一局限性，我们提出了TextSplat——第一个文本驱动的可泛化高斯散点框架。通过采用不同语义线索的文本引导融合，我们的框架学习了鲁棒的跨模态特征表示，改善了几何和语义信息的对齐，产生了高保真的3D重建。具体来说，我们的框架采用了三个并行模块来获得互补的表示：用于精确深度信息的扩散先验深度估计器、用于详细语义信息的语义感知分割网络和用于细化跨视图特征的多视图交互网络。然后，在文本引导语义融合模块中，这些表示通过文本引导和基于注意力的特征聚合机制进行集成，从而得到增强的3D高斯参数，并丰富了详细的语义线索。在各种基准数据集上的实验结果表明，与现有方法相比，在多个评估指标上的性能有所提高，验证了我们框架的有效性。代码将公开发布。 et.al.|[2504.09588](http://arxiv.org/abs/2504.09588)|null|
|**2025-04-12**|**A Constrained Optimization Approach for Gaussian Splatting from Coarsely-posed Images and Noisy Lidar Point Clouds**|3D高斯散斑（3DGS）是一种强大的重建技术，但它需要从精确的相机姿态和高保真点云进行初始化。通常，初始化来自运动结构（SfM）算法；然而，SfM耗时长，限制了3DGS在现实场景和大规模场景重建中的应用。我们介绍了一种不需要SfM支持的约束优化方法，用于同时进行相机姿态估计和3D重建。我们方法的核心是将相机姿态分解为一系列相机到（设备）中心和（设备）从中心到世界的优化。为了方便起见，我们提出了两个以每个参数组的灵敏度为条件的优化约束，并限制了每个参数的搜索空间。此外，当我们直接从嘈杂的点云中学习场景几何时，我们提出了几何约束来提高重建质量。实验表明，在我们收集的数据集和两个公共基准上，所提出的方法明显优于现有的（多模态）3DGS基线和COLMAP补充的方法。 et.al.|[2504.09129](http://arxiv.org/abs/2504.09129)|null|

<p align=right>(<a href=#updated-on-20250417>back to top</a>)</p>

## Diffusion

|Publish Date|Title|Abstract|PDF|Code|
|---|---|---|---|---|
|**2025-04-15**|**Aligning Generative Denoising with Discriminative Objectives Unleashes Diffusion for Visual Perception**|随着图像生成的成功，生成扩散模型越来越多地被用于判别任务，因为像素生成提供了一个统一的感知界面。然而，直接将生成去噪过程重新用于区分性目标，揭示了以前很少解决的关键差距。如果最终分布仍然合理，生成模型可以容忍中间采样误差，但区分性任务在整个过程中都需要严格的准确性，正如参考图像分割等具有挑战性的多模态任务所证明的那样。受这一差距的启发，我们分析并加强了生成扩散过程和感知任务之间的对齐，重点研究了去噪过程中感知质量的演变。我们发现：（1）早期的去噪步骤对感知质量的贡献不成比例，促使我们提出反映不同时间步长贡献的定制学习目标；（2） 后续的去噪步骤显示出意想不到的感知退化，突出了对训练去噪分布变化的敏感性，这通过我们的扩散定制数据增强来解决；以及（3）生成过程独特地实现了交互性，作为可控的用户界面，适用于多轮交互中的纠正提示。我们的见解在不改变架构的情况下显著改善了基于扩散的感知模型，在深度估计、参考图像分割和多面手感知任务方面实现了最先进的性能。代码可在https://github.com/ziqipang/ADDP. et.al.|[2504.11457](http://arxiv.org/abs/2504.11457)|null|
|**2025-04-16**|**Diffusion Distillation With Direct Preference Optimization For Efficient 3D LiDAR Scene Completion**|由于扩散采样速度较慢，扩散模型在3D LiDAR场景完成中的应用受到限制。分数蒸馏加速了扩散采样，但性能下降，而使用直接策略优化（DPO）的后训练使用偏好数据提高了性能。本文提出了一种新的扩散蒸馏DPO框架，用于具有偏好对齐的LiDAR场景完成。首先，学生模型生成具有不同初始噪声的成对完成场景。其次，使用LiDAR场景评估指标作为偏好，我们构建了获胜和失败的样本对。这种构造是合理的，因为大多数LiDAR场景度量都是信息量大但不可微分的，可以直接进行优化。第三，蒸馏DPO通过利用成对完成场景中教师和学生模型之间的分数函数差异来优化学生模型。重复此过程，直到收敛。大量实验表明，与最先进的激光雷达场景完成扩散模型相比，蒸馏DPO实现了更高质量的场景完成，同时将完成速度提高了5倍以上。我们的方法是第一个探索在蒸馏中采用偏好学习的方法，并提供对偏好对齐蒸馏的见解。我们的代码公开于https://github.com/happyw1nd/DistillationDPO. et.al.|[2504.11447](http://arxiv.org/abs/2504.11447)|null|
|**2025-04-15**|**Analysis of Preheat Propagation in MagLIF-like Plasmas**|燃料的预热和预磁化是磁化线性惯性聚变（MagLIF）配置设计中的重要步骤。通常，预热激光的能量沉积在燃料的中心区域，并向外传播，产生磁流体动力学结构，在随后的内爆过程中影响燃料质量分布和磁通量压缩。我们对MagLIF典型条件下磁化等离子体中的预热传播进行了理论分析。该分析基于压力扰动传播的声学时间尺度远短于热扩散的传导时间尺度。在这种状态下，预热驱动的膨胀会引起燃料质量和磁场的分层，这些分层会积聚在由前导激波界定的密集外架中。我们推导了描述膨胀流体动力学轮廓的数学模型的自相似解，并评估了这种配置下磁场的演变。该模型得到了预热传播的FLASH模拟的支持。我们的分析表明，燃料磁化显著的区域往往在时间上渐近地局部化在分隔外架和内热核的界面处。我们评估了这种分层对磁通量守恒和全集成MagLIF FLASH模拟性能的影响。 et.al.|[2504.11432](http://arxiv.org/abs/2504.11432)|null|
|**2025-04-15**|**NormalCrafter: Learning Temporally Consistent Normals from Video Diffusion Priors**|表面法线估计是一系列计算机视觉应用的基石。尽管已经对静态图像场景进行了大量研究，但确保基于视频的正常估计中的时间一致性仍然是一个艰巨的挑战。我们提出NormalCrafter来利用视频扩散模型的固有时间先验，而不是仅仅用时间分量来增强现有的方法。为了确保跨序列的高保真正态估计，我们提出了语义特征正则化（SFR），它将扩散特征与语义线索对齐，鼓励模型专注于场景的内在语义。此外，我们引入了一种两阶段训练协议，该协议利用潜在和像素空间学习来保持空间精度，同时保持长时间上下文。广泛的评估证明了我们的方法的有效性，展示了从不同视频中生成具有复杂细节的时间一致的正常序列的卓越性能。 et.al.|[2504.11427](http://arxiv.org/abs/2504.11427)|null|
|**2025-04-15**|**ADT: Tuning Diffusion Models with Adversarial Supervision**|扩散模型通过反转正向噪声过程来近似真实数据分布，实现了出色的图像生成。在训练过程中，这些模型在单次前向通过中从真实样本的噪声版本预测扩散分数，而推理需要从白噪声开始迭代去噪。由于潜在的预测偏差和累积误差累积，这种训练推理分歧阻碍了推理和训练数据分布之间的对齐。为了解决这个问题，我们提出了一种直观但有效的微调框架，称为对抗扩散调整（ADT），通过在优化过程中刺激推理过程，并通过对抗监督将最终输出与训练数据对齐。具体来说，为了实现鲁棒的对抗训练，ADT具有一个暹罗网络鉴别器，该鉴别器具有固定的预训练骨干和轻量级的可训练参数，结合了图像到图像的采样策略来平滑鉴别困难，并保留了原始的扩散损失以防止鉴别器被黑客攻击。此外，我们仔细约束了沿推理路径反向传播梯度的反向流动路径，而不会导致内存过载或梯度爆炸。最后，对稳定扩散模型（v1.5、XL和v3）的广泛实验表明，ADT显著提高了分布对齐和图像质量。 et.al.|[2504.11423](http://arxiv.org/abs/2504.11423)|null|
|**2025-04-15**|**VideoPanda: Video Panoramic Diffusion with Multi-view Attention**|高分辨率全景视频内容对于虚拟现实中的沉浸式体验至关重要，但收集起来并不容易，因为它需要专门的设备和复杂的相机设置。在这项工作中，我们介绍了VideoPanda，这是一种基于文本或单视图视频数据合成360度视频的新方法。VideoPanda利用多视图注意力层来增强视频扩散模型，使其能够生成一致的多视图视频，这些视频可以组合成沉浸式全景内容。VideoPanda使用两种条件联合训练：纯文本和单视图视频，并支持长视频的自回归生成。为了克服多视图视频生成的计算负担，我们随机对训练过程中使用的持续时间和相机视图进行子采样，并表明该模型能够优雅地推广到在推理过程中生成更多帧。对真实世界和合成视频数据集的广泛评估表明，与现有方法相比，VideoPanda在所有输入条件下生成了更逼真、更连贯的360度全景图。访问项目网站https://research-staging.nvidia.com/labs/toronto-ai/VideoPanda/为了获得结果。 et.al.|[2504.11389](http://arxiv.org/abs/2504.11389)|null|
|**2025-04-16**|**DeepWheel: Generating a 3D Synthetic Wheel Dataset for Design and Performance Evaluation**|数据驱动设计正在成为加速工程创新的有力战略。然而，由于缺乏包括3D几何和物理性能指标的大规模高质量数据集，其在车轮设计中的应用仍然有限。为了解决这一差距，本研究提出了一种使用生成式人工智能的合成设计性能数据集生成框架。该框架首先使用稳定扩散生成2D渲染图像，然后通过2.5D深度估计重建3D几何结构。随后进行结构模拟以提取工程性能数据。为了进一步扩大设计和性能空间，应用了拓扑优化，从而能够生成更多样化的车轮设计。最终的数据集名为DeepWheel，由6000多张照片级逼真图像和900个经过结构分析的3D模型组成。这个多模态数据集是替代模型训练、数据驱动的逆向设计和设计空间探索的宝贵资源。所提出的方法也适用于其他复杂的设计领域。该数据集根据知识共享署名-非商业4.0国际（CC BY-NC 4.0）发布，可在https://www.smartdesignlab.org/datasets et.al.|[2504.11347](http://arxiv.org/abs/2504.11347)|null|
|**2025-04-15**|**Decorrelation in Complex Wave Scattering**|涉及多重散射的现象，尽管几十年来在物理学中引起了相当大的关注，但仍然会产生意想不到和违反直觉的行为，促使进一步的研究。对于光散射，只要散射强度和深度在一定范围内，记忆效应就可以很好地预测四阶统计量，即强度相关性。记忆效应已经得到了广泛的应用，其局限性也变得明显：例如，在通过浑浊介质成像时，由于厚样本中的多散射导致的去相关性已被证明会限制视场。然而，据我们所知，迄今为止还没有一种全面的机制可以精确地解释去相关性。在本文中，我们量化了散射体自身的统计数据如何确定这些局限性。我们表明，背散射场的系综统计可以分解为两个项：一个表示表面散射，其中多尺度结构特征的统计分布可以从我们之前的工作中推断出来；而第二项来源于底层散射体积并且是扩散的。新框架与实验结果一致，包括对单一实现引起的波动的新准幂律的预测。 et.al.|[2504.11330](http://arxiv.org/abs/2504.11330)|null|
|**2025-04-15**|**Autoregressive Distillation of Diffusion Transformers**|具有变压器架构的扩散模型在生成高保真图像和高分辨率可扩展性方面表现出了很有前景的能力。然而，合成所需的迭代采样过程非常耗费资源。一系列工作的重点是将概率流ODE的解提取到几步学生模型中。然而，现有的方法由于依赖于最新的去噪样本作为输入而受到限制，使其容易受到暴露偏差的影响。为了解决这一局限性，我们提出了自回归蒸馏（ARD），这是一种利用常微分方程的历史轨迹来预测未来步骤的新方法。ARD提供了两个关键优势：1）它通过利用不易受累积误差影响的预测历史轨迹来减轻曝光偏差，2）它利用ODE轨迹的先前历史作为更有效的粗粒度信息来源。ARD通过添加令牌式时间嵌入来标记轨迹历史中的每个输入，并采用块式因果注意力掩码进行训练，从而修改了教师转换器架构。此外，仅在较低的变压器层中合并历史输入可以提高性能和效率。我们在ImageNet和T2I合成上验证了ARD在类条件生成中的有效性。与基线方法相比，我们的模型在FID退化方面减少了5倍，而在ImageNet-256上只需要额外1.1%的FLOP。此外，ARD在ImageNet-256上仅用4步就达到了1.84的FID，在即时依从性得分方面优于公开的1024p文本到图像提取模型，与教师相比，FID下降幅度最小。项目页面：https://github.com/alsdudrla10/ARD. et.al.|[2504.11295](http://arxiv.org/abs/2504.11295)|null|
|**2025-04-15**|**UniAnimate-DiT: Human Image Animation with Large-Scale Video Diffusion Transformer**|本报告介绍了UniAnimate DiT，这是一个先进的项目，利用开源Wan2.1模型的尖端和强大功能，实现一致的人体图像动画。具体来说，为了保持原始Wan2.1模型的稳健生成能力，我们实现了低秩自适应（LoRA）技术来微调一组最小的参数，从而显著降低了训练内存开销。设计了一种由多个堆叠的3D卷积层组成的轻量级姿态编码器，用于对驱动姿态的运动信息进行编码。此外，我们采用简单的级联操作将参考外观集成到模型中，并结合参考图像的姿态信息以增强姿态对齐。实验结果表明，我们的方法实现了视觉上呈现和时间上一致的高保真动画。经过480p（832x480）视频的训练，UniAnimate DiT展示了强大的泛化能力，可以在推理过程中无缝升级到720P（1280x720）。训练和推理代码可在以下网址公开获取https://github.com/ali-vilab/UniAnimate-DiT. et.al.|[2504.11289](http://arxiv.org/abs/2504.11289)|null|

<p align=right>(<a href=#updated-on-20250417>back to top</a>)</p>

## NeRF

|Publish Date|Title|Abstract|PDF|Code|
|---|---|---|---|---|
|**2025-04-14**|**DNF-Avatar: Distilling Neural Fields for Real-time Animatable Avatar Relighting**|从单眼视频中创建可重现和可动画化的人类化身是一个新兴的研究课题，具有广泛的应用，例如虚拟现实、体育和视频游戏。之前的研究利用神经场和基于物理的渲染（PBR）来估计人类化身的几何形状并解开其外观属性。然而，这些方法的一个缺点是由于昂贵的蒙特卡洛射线追踪导致渲染速度较慢。为了解决这个问题，我们提出将隐式神经场（教师）的知识提取为显式的2D高斯飞溅（学生）表示，以利用高斯飞溅的快速光栅化特性。为了避免光线追踪，我们对PBR外观采用了分裂和近似。我们还提出了用于阴影计算的新型部分式环境遮挡探头。阴影预测是通过每像素只查询一次这些探测器来实现的，这为化身的实时重新照明铺平了道路。这些技术相结合，可以提供高质量的重新照明效果和逼真的阴影效果。我们的实验表明，所提出的学生模型与我们的教师模型实现了相当甚至更好的重新照明结果，同时在推理时快了370倍，达到了67 FPS的渲染速度。 et.al.|[2504.10486](http://arxiv.org/abs/2504.10486)|null|
|**2025-04-11**|**SN-LiDAR: Semantic Neural Fields for Novel Space-time View LiDAR Synthesis**|最近的研究已经开始探索激光雷达点云的新颖视图合成（NVS），旨在从看不见的视点生成逼真的激光雷达扫描。然而，大多数现有的方法都不能重建语义标签，而语义标签对于自动驾驶和机器人感知等许多下游应用至关重要。与受益于强大分割模型的图像不同，LiDAR点云缺乏如此大规模的预训练模型，这使得语义标注既费时又费力。为了应对这一挑战，我们提出了SN LiDAR，这是一种联合执行精确语义分割、高质量几何重建和逼真LiDAR合成的方法。具体来说，我们采用从粗到细的平面网格特征表示来从多帧点云中提取全局特征，并利用基于CNN的编码器从当前帧点云中提取局部语义特征。SemanticKITTI和KITTI-360的大量实验证明了SN LiDAR在语义和几何重建方面的优越性，有效地处理了动态对象和大规模场景。代码将在https://github.com/dtc111111/SN-Lidar. et.al.|[2504.08361](http://arxiv.org/abs/2504.08361)|**[link](https://github.com/dtc111111/sn-lidar)**|
|**2025-04-08**|**econSG: Efficient and Multi-view Consistent Open-Vocabulary 3D Semantic Gaussians**|最近关于开放词汇神经场的工作的主要重点是从VLM中提取精确的语义特征，然后将它们有效地整合到多视图一致的3D神经场表示中。然而，大多数现有的工作都是在受信任的SAM上进行的，以规范图像级CLIP，而无需进一步细化。此外，一些现有的研究通过在与3DGS语义场融合之前对2D VLM的语义特征进行降维来提高效率，这不可避免地导致了多视图不一致。在这项工作中，我们提出了使用3DGS进行开放式词汇语义分割的econSG。我们的econSG由以下部分组成：1）置信区间引导正则化（CRR），它相互细化SAM和CLIP，以获得具有完整和精确边界的精确语义特征的两全其美。2） 一个低维上下文空间，通过融合反投影的多视图2D特征来增强3D多视图一致性，同时提高计算效率，然后直接对融合的3D特征进行降维，而不是分别对每个2D视图进行操作。与现有方法相比，我们的econSG在四个基准数据集上显示了最先进的性能。此外，我们也是所有方法中最有效的培训。 et.al.|[2504.06003](http://arxiv.org/abs/2504.06003)|null|
|**2025-04-08**|**Meta-Continual Learning of Neural Fields**|神经场（NF）作为一种用于复杂数据表示的通用框架，已经获得了突出地位。这项工作揭示了一个新的问题设置，称为“神经场元连续学习”（MCL-NF），并引入了一种新的策略，该策略采用模块化架构与基于优化的元学习相结合。我们的策略侧重于克服现有神经场连续学习方法的局限性，如灾难性遗忘和缓慢收敛，实现了高质量的重建，显著提高了学习速度。我们进一步引入了神经辐射场的Fisher信息最大化损失（FIM-NeRF），它在样本级别最大化信息增益以增强学习泛化，并证明了收敛保证和泛化界限。我们在六个不同的数据集上对图像、音频、视频重建和视图合成任务进行了广泛的评估，证明了我们的方法在重建质量和速度方面优于现有的MCL和CL-NF方法。值得注意的是，我们的方法在降低参数要求的情况下，实现了神经场对城市级NeRF渲染的快速适应。 et.al.|[2504.05806](http://arxiv.org/abs/2504.05806)|null|
|**2025-04-06**|**Dynamic Neural Field Modeling of Visual Contrast for Perceiving Incoherent Looming**|Amari的动态神经场（DNF）框架提供了一种受大脑启发的方法来模拟神经元群的平均激活。利用单一领域，DNF已成为机器人应用中低能耗隐约感知模块的有前景的基础。然而，之前的DNF方法在检测不连贯或不一致的迫在眉睫的特征方面面临着重大挑战，这些特征在现实世界场景中很常见，例如雨天的碰撞检测。果蝇和蝗虫视觉系统的见解表明，编码ON/OFF视觉对比在增强迫在眉睫的选择性方面起着至关重要的作用。此外，横向激发机制可能会改善织机敏感神经元对连贯和非连贯刺激的反应。这些共同为改进迫在眉睫的感知模型提供了宝贵的指导。基于这些生物学证据，我们通过结合on/OFF视觉对比度的建模来扩展之前的单场DNF框架，每个对比度都由一个专用的DNF控制。使用归一化高斯核对每个ON/OFF对比场内的横向激励进行公式化，并将其输出整合到求和字段中以生成碰撞警报。实验评估表明，所提出的模型有效地解决了非相干逼近检测的挑战，并且明显优于最先进的蝗虫启发模型。它在各种刺激下表现出了强大的性能，包括合成雨效应，突显了它在复杂、嘈杂的环境中，在视觉线索不一致的情况下，具有可靠的隐约感知的潜力。 et.al.|[2504.04551](http://arxiv.org/abs/2504.04551)|null|
|**2025-04-03**|**A Physics-Informed Meta-Learning Framework for the Continuous Solution of Parametric PDEs on Arbitrary Geometries**|在这项工作中，我们引入了隐式有限算子学习（iFOL），用于任意几何上偏微分方程（PDE）的连续和参数解。我们提出了一种基于物理信息的编解码器网络，以建立连续参数和解空间之间的映射。解码器通过利用以潜在或特征码为条件的隐式神经场网络来构建参数解场。实例特定代码是通过基于二阶元学习技术的PDE编码过程导出的。在训练和推理中，在PDE编码和解码过程中，物理信息损失函数被最小化。iFOL以能量或加权残差形式表示损失函数，并使用从标准数值PDE方法导出的离散残差对其进行评估。这种方法在训练和推理过程中都会导致离散残差的反向传播。iFOL具有几个关键特性：（1）其独特的损失公式消除了以前在PDE的条件神经场算子学习中使用的传统编码过程-解码流水线的需要；（2） 它不仅提供精确的参数和连续场，而且提供参数梯度的解，而不需要额外的损失项或灵敏度分析；（3） 它可以有效地捕捉溶液中的尖锐不连续性；（4）它消除了对几何和网格的约束，使其适用于任意几何和空间采样（零样本超分辨率能力）。我们批判性地评估了这些特征，并分析了网络在稳态和瞬态PDE中推广到看不见的样本的能力。所提出的方法的整体性能是有希望的，证明了它适用于计算力学中一系列具有挑战性的问题。 et.al.|[2504.02459](http://arxiv.org/abs/2504.02459)|**[link](https://github.com/rezanajian/fol)**|
|**2025-04-01**|**Flow Matching on Lie Groups**|流匹配（FM）是一种最新的生成建模技术：我们的目标是学习如何从分布中采样{X}_1 $通过从某些分布中流动样本$\mathfrak{X}_0$很容易取样。关键技巧是，在$\mathfrak中对端点进行调节的同时，可以训练这个流场{X}_1$：给定终点，只需沿直线段移动到终点（Lipman等人，2022）。然而，直线段仅在欧几里德空间上定义良好。因此，Chen和Lipman（2023）将该方法推广到黎曼流形上的FM，用测地线或其谱近似代替线段。我们采取了另一种观点：我们通过用指数曲线代替线段来推广李群上的FM。这导致了许多矩阵李群的简单、内在和快速实现，因为所需的李群运算（积、逆、指数、对数）仅由相应的矩阵运算给出。然后，李群上的FM可用于生成建模，数据由特征集（在$\mathbb{R}^n$ 中）和姿势集（在某些李群中）组成，例如等变神经场的潜在码（Wessels等人，2025）。 et.al.|[2504.00494](http://arxiv.org/abs/2504.00494)|**[link](https://github.com/finnsherry/FlowMatching)**|
|**2025-03-29**|**NeuralGS: Bridging Neural Fields and 3D Gaussian Splatting for Compact 3D Representations**|3D高斯散点（3DGS）显示了卓越的质量和渲染速度，但有数百万的3D高斯分布和巨大的存储和传输成本。最近的3DGS压缩方法主要集中在压缩脚手架GS上，取得了令人印象深刻的性能，但增加了体素结构和复杂的编码和量化策略。在这篇论文中，我们的目标是开发一种简单而有效的方法，称为NeuralGS，它以另一种方式探索将原始3DGS压缩成紧凑的表示，而不需要体素结构和复杂的量化策略。我们的观察是，像NeRF这样的神经场可以用多层感知器（MLP）神经网络表示复杂的3D场景，只需要几兆字节。因此，NeuralGS有效地采用神经场表示来用MLP对3D高斯的属性进行编码，即使对于大规模场景，也只需要很小的存储空间。为了实现这一点，我们采用了一种聚类策略，并根据高斯的重要性得分作为拟合权重，为每个聚类用不同的微小MLP对高斯进行拟合。我们在多个数据集上进行实验，在不损害视觉质量的情况下实现了平均模型大小减少45倍。我们的方法在原始3DGS上的压缩性能与基于Scaffold GS的专用压缩方法相当，这表明了用神经场直接压缩原始3DGS的巨大潜力。 et.al.|[2503.23162](http://arxiv.org/abs/2503.23162)|null|
|**2025-03-27**|**Renormalization group analysis of noisy neural field**|大脑中的神经元在个体特性和与其他神经元的连接方面表现出极大的多样性。为了深入了解神经元多样性如何在大尺度上促进大脑动力学和功能，我们借鉴了复制方法的框架，该框架已成功应用于平衡统计力学中一大类具有淬灭噪声的问题。我们分析了Wilson Cowan模型的两个线性化版本，其随机系数在空间上是相关的。特别是：（A）神经元本身的性质是异质的，（B）它们的连接是各向异性的。在这两个模型中，淬火随机性的平均会产生额外的非线性。这些非线性在威尔逊重整化群的框架内进行了分析。我们发现，对于模型A，如果噪声的空间相关性随距离衰减，指数小于-2 $，则在大的空间尺度上，噪声的影响消失了。相比之下，对于模型B，只有当空间相关性以小于-1$ 的指数衰减时，噪声对神经元连接的影响才会消失。我们的计算还表明，在某些条件下，噪声的存在可能会在大尺度上产生类似行波的行为，尽管这一结果在微扰理论的高阶下是否仍然有效还有待观察。 et.al.|[2503.21605](http://arxiv.org/abs/2503.21605)|null|
|**2025-03-25**|**Thin-Shell-SfT: Fine-Grained Monocular Non-rigid 3D Surface Tracking with Neural Deformation Fields**|从单目RGB视频中重建高度可变形的表面（如布料）是一个具有挑战性的问题，没有任何解决方案可以提供一致和准确的细粒度表面细节恢复。为了解释环境的病态性，现有的方法使用具有统计、神经或物理先验的变形模型。它们还主要依赖于非自适应离散曲面表示（例如多边形网格），逐帧优化导致误差传播，并受到基于网格的可微渲染器梯度差的影响。因此，织物褶皱等精细表面细节往往无法以所需的精度恢复。针对这些局限性，我们提出了ThinShell SfT，这是一种用于非刚性3D跟踪的新方法，将表面表示为隐式和连续的时空神经场。我们采用基于基尔霍夫-洛夫模型的连续薄壳物理先验进行空间正则化，这与早期作品的离散化替代方案形成了鲜明对比。最后，我们利用3D高斯溅射将表面可微分地渲染到图像空间中，并根据合成原理分析优化变形。我们的薄壳SfT在定性和定量上都优于先前的工作，这要归功于我们的连续表面公式以及专门定制的模拟先验和表面诱导的3D高斯。请访问我们的项目页面https://4dqv.mpiinf.mpg.de/ThinShellSfT. et.al.|[2503.19976](http://arxiv.org/abs/2503.19976)|null|

<p align=right>(<a href=#updated-on-20250417>back to top</a>)</p>

[contributors-shield]: https://img.shields.io/github/contributors/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[contributors-url]: https://github.com/Vincentqyw/cv-arxiv-daily/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[forks-url]: https://github.com/Vincentqyw/cv-arxiv-daily/network/members
[stars-shield]: https://img.shields.io/github/stars/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[stars-url]: https://github.com/Vincentqyw/cv-arxiv-daily/stargazers
[issues-shield]: https://img.shields.io/github/issues/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[issues-url]: https://github.com/Vincentqyw/cv-arxiv-daily/issues

