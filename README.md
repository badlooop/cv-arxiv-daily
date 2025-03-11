[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]

## Updated on 2025.03.11
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
|**2025-03-10**|**AR-Diffusion: Asynchronous Video Generation with Auto-Regressive Diffusion**|视频生成的任务需要合成视觉上逼真且时间上连贯的视频帧。现有的方法主要使用异步自回归模型或同步扩散模型来解决这一挑战。然而，异步自回归模型经常受到训练和推理之间不一致的影响，导致误差累积等问题，而同步扩散模型则受到其对刚性序列长度依赖的限制。为了解决这些问题，我们引入了自回归扩散（AR扩散），这是一种新的模型，结合了自回归和扩散模型的优点，用于灵活、异步的视频生成。具体来说，我们的方法利用扩散来逐渐破坏训练和推理中的视频帧，从而减少这些阶段之间的差异。受自回归生成的启发，我们对单个帧的腐败时间步长进行了非递减约束，确保早期帧比后续帧更清晰。这种设置，再加上时间因果注意力，可以灵活地生成不同长度的视频，同时保持时间连贯性。此外，我们设计了两个专门的时间步长调度器：FoPP调度器用于训练期间的平衡时间步长采样，AD调度器用于推理期间灵活的时间步长差异，支持同步和异步生成。广泛的实验证明了我们提出的方法的优越性，该方法在四个具有挑战性的基准测试中取得了具有竞争力和最先进的结果。 et.al.|[2503.07418](http://arxiv.org/abs/2503.07418)|null|
|**2025-03-10**|**Automated Movie Generation via Multi-Agent CoT Planning**|现有的长篇视频生成框架缺乏自动化规划，需要手动输入故事情节、场景、电影摄影和角色交互，导致成本高、效率低。为了应对这些挑战，我们提出了MovieAgent，这是一种通过多代理思维链（CoT）规划的自动电影生成。MovieAgent提供了两个关键优势：1）我们首先探索和定义了自动电影/长视频生成的范式。给定一个剧本和角色库，我们的MovieAgent可以生成多场景、多镜头的长篇视频，具有连贯的叙事，同时确保整个电影中的角色一致性、同步字幕和稳定的音频。2） MovieAgent引入了一种基于CoT的分层推理过程，可以自动构建场景、相机设置和电影摄影，大大减少了人力。通过使用多个LLM代理来模拟导演、编剧、故事板艺术家和位置经理的角色，MovieAgent简化了制作流程。实验表明，MovieAgent在剧本忠实性、角色一致性和叙事连贯性方面取得了最新的成果。我们的分层框架向前迈出了一步，为全自动电影生成提供了新的见解。代码和项目网站可在以下网址获得：https://github.com/showlab/MovieAgent以及https://weijiawu.github.io/MovieAgent. et.al.|[2503.07314](http://arxiv.org/abs/2503.07314)|null|
|**2025-03-09**|**VideoPhy-2: A Challenging Action-Centric Physical Commonsense Evaluation in Video Generation**|大规模视频生成模型能够创建具有不同视觉概念的逼真视频，是通用物理世界模拟器的有力候选者。然而，他们在现实世界的行为中对身体常识的坚持尚不清楚（例如，打网球、后空翻）。现有的基准存在局限性，如规模有限、缺乏人工评估、与真实差距相似以及缺乏细粒度的物理规则分析。为了解决这个问题，我们引入了VideoPhy-2，这是一个以动作为中心的数据集，用于评估生成视频中的物理常识。我们从现代生成模型中策划了200个不同的动作和详细的视频合成提示。我们执行人工评估，评估生成视频中的语义依从性、物理常识和物理规则的基础。我们的研究结果揭示了主要的缺点，即使是最好的模型在VideoPhy-2的硬子集上也只能实现22%的联合性能（即高语义和物理常识依从性）。我们发现，这些模型特别难以应对质量和动量等守恒定律。最后，我们还训练了VideoPhy AutoEval，这是一个自动评估器，用于对我们的数据集进行快速、可靠的评估。总体而言，VideoPhy-2是一个严格的基准，揭示了视频生成模型中的关键差距，并指导了未来基于物理的视频生成研究。数据和代码可在https://videophy2.github.io/. et.al.|[2503.06800](http://arxiv.org/abs/2503.06800)|null|
|**2025-03-09**|**Learning Few-Step Diffusion Models by Trajectory Distribution Matching**|加速扩散模型采样对于高效部署AIGC至关重要。虽然基于分布匹配和轨迹匹配的扩散蒸馏方法将采样减少到一步，但它们在文本到图像生成等复杂任务上存在不足。很少有步骤生成在速度和质量之间提供更好的平衡，但现有的方法面临着持续的权衡：分布匹配缺乏多步采样的灵活性，而轨迹匹配通常会产生次优的图像质量。为了弥合这一差距，我们提出通过轨迹分布匹配（TDM）学习几步扩散模型，这是一种结合了分布和轨迹匹配优势的统一蒸馏范式。我们的方法引入了一个无数据的分数蒸馏目标，在分布水平上将学生的轨迹与教师的轨迹对齐。此外，我们开发了一个采样步骤感知目标，该目标将不同步骤的学习目标解耦，从而实现了更可调整的采样。这种方法既支持确定性采样以获得卓越的图像质量，又支持灵活的多步自适应，以显著的效率实现了最先进的性能。我们的TDM模型在各种主干上优于现有的方法，如SDXL和PixArt- $\alpha$，提供了卓越的质量并显著降低了培训成本。特别是，我们的方法将PixArt-$\alpha$ 提取为一个4步生成器，该生成器在1024分辨率下的真实用户偏好上优于其老师。这是通过500次迭代和2个A800小时完成的，仅占教师培训成本的0.01%。此外，我们提出的TDM可以扩展到加速文本到视频的传播。值得注意的是，TDM可以通过在VBench上仅使用4个NFE来超越其教师模型（CogVideoX-2B），将总分从80.91提高到81.65。项目页面：https://tdm-t2x.github.io/ et.al.|[2503.06674](http://arxiv.org/abs/2503.06674)|null|
|**2025-03-09**|**TR-DQ: Time-Rotation Diffusion Quantization**|扩散模型在图像和视频生成中得到了广泛的应用。然而，它们复杂的网络架构导致其生成过程的推理开销很高。现有的扩散量化方法主要关注模型结构的量化，而忽略了采样过程中时间步长变化的影响。与此同时，大多数当前的方法未能考虑到无法消除的显著激活，导致量化后性能大幅下降。为了解决这些问题，我们提出了时间旋转扩散量化（TR-DQ），这是一种结合了时间步长和基于旋转的优化的新型量化方法。TR-DQ首先根据时间步长划分采样过程，并应用旋转矩阵动态平滑激活和权重。对于不同的时间步长，引入了一个专用的超参数用于自适应定时建模，这使得能够在不同的时间步上进行动态量化。此外，我们还探索了无分类器引导（CFG方式）的压缩潜力，为后续工作奠定了基础。与现有的量化方法相比，TR-DQ在图像生成和视频生成任务上实现了最先进的（SOTA）性能，推理速度提高了1.38-1.89倍，内存减少了1.97-2.58倍。 et.al.|[2503.06564](http://arxiv.org/abs/2503.06564)|null|
|**2025-03-09**|**QuantCache: Adaptive Importance-Guided Quantization with Hierarchical Latent and Layer Caching for Video Generation**|最近，扩散变压器（DiTs）已经成为视频生成中的主导架构，在性能方面超越了基于U-Net的模型。然而，DiT的增强功能也存在重大缺陷，包括计算和内存成本的增加，这阻碍了它们在资源受限的设备上的部署。当前的加速技术，如量化和缓存机制，提供了有限的加速，并且通常是孤立应用的，无法完全解决DiT架构的复杂性。在本文中，我们提出了QuantCache，这是一种新的无训练推理加速框架，可以联合优化分层潜在缓存、自适应重要性引导量化和结构冗余感知修剪。QuantCache在Open Sora上实现了6.72美元/次的端到端延迟加速，生成质量损失最小。跨多个视频生成基准的广泛实验证明了我们方法的有效性，为高效的DiT推理设定了新的标准。代码和模型将在https://github.com/JunyiWuCode/QuantCache. et.al.|[2503.06545](http://arxiv.org/abs/2503.06545)|null|
|**2025-03-09**|**A Light and Tuning-free Method for Simulating Camera Motion in Video Generation**|现有的摄像机运动控制视频生成方法在微调和推理方面面临计算瓶颈。本文提出了LightMotion，这是一种在视频生成中模拟相机运动的无光和无调谐方法。在潜在空间中操作，它消除了额外的微调、修复和深度估计，使其比现有方法更加精简。本文的工作包括：（i）潜在空间置换操作有效地模拟了各种相机运动，如摇摄、变焦和旋转。（ii）潜在空间重采样策略结合了背景感知采样和跨帧对齐，以准确填充新的视角，同时保持跨帧的连贯性。（iii）我们的深入分析表明，置换和重采样会导致潜在空间中的信噪比偏移，从而导致生成质量差。为了解决这个问题，我们提出了潜在空间校正，该校正在去噪过程中重新引入噪声，以减轻信噪比偏移并提高视频生成质量。详尽的实验表明，我们的LightMotion在定量和定性方面都优于现有的方法。 et.al.|[2503.06508](http://arxiv.org/abs/2503.06508)|null|
|**2025-03-09**|**Generative Video Bi-flow**|我们提出了一种新的生成视频模型，该模型通过将时间变化作为神经常微分方程（ODE）流进行鲁棒学习，其双线性目标结合了两个方面：第一个是将过去的视频帧直接映射到未来的视频帧。之前的工作已经将噪声映射到新帧，这是一个计算成本更高的过程。不幸的是，从上一帧开始，而不是噪声，更容易产生漂移误差。因此，第二，我们还学习了如何通过在训练过程中添加噪声来消除累积误差作为联合目标。我们以流式方式演示了各种视频数据集的无条件视频生成，与基线条件扩散相比，所有这些数据集的质量都具有竞争力，但速度更快，即ODE求解器步骤更少。 et.al.|[2503.06364](http://arxiv.org/abs/2503.06364)|null|
|**2025-03-08**|**Text2Story: Advancing Video Storytelling with Text Guidance**|仅使用文本提示从离散输入生成连贯的长视频序列是内容创建中的一项关键任务。虽然基于扩散的模型在短视频合成方面表现出色，但从文本中讲长篇故事在很大程度上仍未得到探索，这是一个挑战，因为存在时间连贯性、在整个视频中保持语义意义和动作连续性的挑战。我们引入了一种新颖的故事讲述方法，通过自然的动作过渡和结构化的叙事实现无缝的视频生成。我们提出了一种双向时间加权的潜在混合策略，以确保生成的长视频片段之间的时间一致性。此外，我们的方法将Black-Scholes算法从用于图像生成的快速混合扩展到视频生成，通过结构化文本调节实现了受控的运动进化。为了进一步增强运动连续性，我们提出了一种语义动作表示框架，将高级动作语义编码到混合过程中，根据动作相似性动态调整转换，确保平滑但可适应的运动变化。潜在空间混合保持场景中对象之间的空间一致性，而时间加权混合则强制执行时间一致性的双向约束。这种综合方法可以防止突然的转变，同时确保流畅的故事讲述。大量实验表明，与基线相比，视频叙事在时间上一致，视觉上引人注目，无需任何额外训练。我们的方法弥合了短片和扩展视频之间的差距，为GenAI驱动的文本视频合成建立了一个新的范式。 et.al.|[2503.06310](http://arxiv.org/abs/2503.06310)|null|
|**2025-03-08**|**Object-Centric World Model for Language-Guided Manipulation**|世界模型对于智能体预测未来和规划自动驾驶和机器人等领域至关重要。为了实现这一目标，最近的进展集中在视频生成上，由于扩散模型的巨大成功，视频生成受到了广泛关注。然而，这些模型需要大量的计算资源。为了应对这些挑战，我们提出了一种世界模型，该模型利用以对象为中心的表示空间，在语言指令的指导下使用槽注意力。我们的模型将当前状态感知为以对象为中心的表示，并在自然语言指令的条件下预测该表示空间中的未来状态。与基于扩散的生成替代方案相比，这种方法产生了一个更紧凑、计算效率更高的模型。此外，它还可以根据语言指令灵活预测未来的状态，并在对象识别至关重要的操纵任务中提供了显著的优势。在本文中，我们证明了我们的潜在预测世界模型在视觉语言运动控制任务中优于生成世界模型，实现了更高的样本和计算效率。我们还研究了所提出方法的泛化性能，并探索了使用以对象为中心的表示来预测动作的各种策略。 et.al.|[2503.06170](http://arxiv.org/abs/2503.06170)|null|

<p align=right>(<a href=#updated-on-20250311>back to top</a>)</p>

## 3D

|Publish Date|Title|Abstract|PDF|Code|
|---|---|---|---|---|
|**2025-03-10**|**SOGS: Second-Order Anchor for Advanced 3D Gaussian Splatting**|基于锚点的3D高斯飞溅（3D-GS）利用了3D高斯预测中的锚点特征，在减少高斯冗余的情况下实现了令人印象深刻的3D渲染质量。另一方面，它经常遇到锚点特征、模型大小和渲染质量之间的困境——较大的锚点特征会导致较大的3D模型和高质量的渲染，而减少锚点特征会降低高斯属性预测，从而导致渲染纹理和几何体中出现明显的伪影。我们设计了SOGS，这是一种基于锚点的3D-GS技术，它引入了二阶锚点，以实现卓越的渲染质量，同时减少锚点特征和模型大小。具体来说，SOGS结合了基于协方差的二阶统计和跨特征维度的相关性，以增强每个锚点内的特征，补偿减少的特征大小，并有效提高渲染质量。此外，它引入了选择性梯度损失，以增强场景纹理和场景几何形状的优化，从而实现具有小锚点特征的高质量渲染。在多个广泛采用的基准上进行的广泛实验表明，SOGS在新的视图合成中实现了卓越的渲染质量，模型尺寸明显减小。 et.al.|[2503.07476](http://arxiv.org/abs/2503.07476)|null|
|**2025-03-10**|**Learning A Zero-shot Occupancy Network from Vision Foundation Models via Self-supervised Adaptation**|由于3D注释的劳动密集型性质，从2D单眼图像估计3D世界是一项基本但具有挑战性的任务。为了简化标签获取，这项工作提出了一种新方法，通过将3D监督解耦为图像级基元（例如语义和几何组件）的集成，将2D视觉基础模型（VFM）与3D任务连接起来。作为一个关键的激励因素，我们利用视觉语言模型的零样本功能来实现图像语义。然而，由于臭名昭著的病态问题——多个不同的3D场景可以产生相同的2D投影，以零样本方式直接从单目图像推断度量深度是不合适的。相比之下，2D VFM提供了有前景的相对深度来源，当适当缩放和偏移时，理论上与度量深度对齐。因此，我们通过使用时间一致性优化比例和偏移，将从VFM导出的相对深度调整为度量深度，也称为新颖的视图合成，而无需访问地面真实度量深度。因此，我们使用重建的度量深度将语义投影到3D空间中，从而提供3D监督。在nuScenes和SemanticKITTI上的大量实验证明了我们框架的有效性。例如，在nuScene上，所提出的方法在体素占用预测方面比当前最先进的方法高出3.34%的mIoU。 et.al.|[2503.07125](http://arxiv.org/abs/2503.07125)|null|
|**2025-03-09**|**Gaussian RBFNet: Gaussian Radial Basis Functions for Fast and Accurate Representation and Reconstruction of Neural Fields**|DeepSDF和神经辐射场等神经场最近彻底改变了RGB图像和视频的新颖视图合成和3D重建。然而，实现高质量的表示、重建和渲染需要深度神经网络，而深度神经网络的训练和评估速度很慢。尽管已经提出了几种加速技术，但它们经常以速度换取内存。另一方面，基于高斯飞溅的方法加快了渲染时间，但在存储大量高斯参数所需的训练速度和内存方面仍然成本高昂。在本文中，我们介绍了一种新的神经表示方法，它在训练和推理时间都很快，而且很轻。我们的关键观察是，传统MLP中使用的神经元执行简单的计算（点积，然后是ReLU激活），因此需要使用宽和深MLP或高分辨率和高维特征网格来参数化复杂的非线性函数。我们在这篇论文中表明，通过用径向基函数（RBF）核替换传统神经元，只需一层这样的神经元，就可以实现2D（RGB图像）、3D（几何）和5D（辐射场）信号的高精度表示。该表示具有高度的并行性，可在低分辨率特征网格上运行，并且结构紧凑，内存高效。我们证明，所提出的新表示可以在不到15秒的时间内训练出3D几何表示，在不到十五分钟的时间内就可以训练出新的视图合成。在运行时，它可以在不牺牲质量的情况下以超过60 fps的速度合成新颖的视图。 et.al.|[2503.06762](http://arxiv.org/abs/2503.06762)|null|
|**2025-03-09**|**CoDa-4DGS: Dynamic Gaussian Splatting with Context and Deformation Awareness for Autonomous Driving**|动态场景渲染通过使用逼真的数据进行闭环模拟，为自动驾驶开辟了新的途径，这对于验证端到端算法至关重要。然而，交通环境的复杂性和高度动态性给准确渲染这些场景带来了重大挑战。本文介绍了一种新的4D高斯散布（4DGS）方法，该方法结合了上下文和时间变形感知来改善动态场景渲染。具体来说，我们采用2D语义分割基础模型来自我监督高斯的4D语义特征，确保有意义的上下文嵌入。同时，我们跟踪相邻帧中每个高斯函数的时间变形。通过聚合和编码语义和时间变形特征，每个高斯模型都配备了3D空间内潜在变形补偿的线索，从而更精确地表示动态场景。实验结果表明，我们的方法提高了4DGS在自动驾驶动态场景渲染中捕获精细细节的能力，并在4D重建和新颖视图合成方面优于其他自监督方法。此外，CoDa-4DGS使每个高斯函数的语义特征变形，从而实现了更广泛的应用。 et.al.|[2503.06744](http://arxiv.org/abs/2503.06744)|null|
|**2025-03-09**|**D3DR: Lighting-Aware Object Insertion in Gaussian Splatting**|高斯散斑已成为各种3D计算机视觉任务的流行技术，包括新颖的视图合成、场景重建和动态场景渲染。然而，自然外观对象插入的挑战，即对象的外观与场景无缝匹配，仍未得到解决。在这项工作中，我们提出了一种称为D3DR的方法，用于将3DGS参数化对象插入3DGS场景中，同时校正其光照、阴影和其他视觉伪影以确保一致性，这是一个以前从未成功解决的问题。我们利用扩散模型的进步，该模型基于真实世界的数据进行训练，隐含地理解正确的场景照明。插入对象后，我们优化了一个基于扩散的增量去噪分数（DDS）启发的物镜，以调整其3D高斯参数，从而进行适当的光照校正。利用扩散模型个性化技术来提高优化质量，我们的方法确保了无缝的对象插入和自然的外观。最后，我们通过与现有方法的比较证明了该方法的有效性，在重新照明质量方面实现了0.5 PSNR和0.15 SSIM的改进。 et.al.|[2503.06740](http://arxiv.org/abs/2503.06740)|null|
|**2025-03-09**|**StructGS: Adaptive Spherical Harmonics and Rendering Enhancements for Superior 3D Gaussian Splatting**|3D重建与神经渲染技术的最新进展极大地改善了照片级逼真3D场景的创建，影响了学术研究和工业应用。3D高斯散点技术及其变体结合了基于基元和体积表示的优点，实现了卓越的渲染质量。虽然3D几何散射（3DGS）及其变体推进了3D表示领域，但它们在训练过程中未能捕捉到非局部结构信息的随机特性。此外，基于3DGS的方法中球面函数的初始化通常无法在早期训练回合中使用高阶项，从而导致训练过程中不必要的计算开销。此外，目前基于3DGS的方法需要在更高分辨率的图像上进行训练以呈现更高分辨率输出，这大大增加了内存需求并延长了训练持续时间。我们介绍了StructGS，这是一个增强3D高斯散点（3DGS）的框架，用于改进3D重建中的新颖视图合成。StructGS创新性地结合了基于补丁的SSIM损耗、动态球面谐波初始化和多尺度残差网络（MSRN），分别解决了上述局限性。我们的框架显著减少了计算冗余，增强了细节捕捉，并支持从低分辨率输入进行高分辨率渲染。实验表明，StructGS的性能优于最先进的（SOTA）模型，能够以更少的伪影实现更高质量、更详细的渲染。 et.al.|[2503.06462](http://arxiv.org/abs/2503.06462)|null|
|**2025-03-08**|**StreamGS: Online Generalizable Gaussian Splatting Reconstruction for Unposed Image Streams**|3D高斯散斑（3DGS）的出现带来了先进的3D场景重建和新颖的视图合成。随着需要即时反馈的交互式应用程序的兴趣日益浓厚，实时在线3DGS重建的需求量很大。然而，由于三个主要挑战，现有的方法都无法满足需求：缺乏预定的相机参数，需要可推广的3DGS优化，以及减少冗余的必要性。我们提出了StreamGS，这是一种用于无基图像流的在线可推广3DGS重建方法，通过预测和聚合每帧高斯分布，将图像流逐步转换为3D高斯流。我们的方法通过引入内容自适应细化，克服了初始点重建在处理域外（OOD）问题时的局限性。该改进通过在相邻帧之间建立可靠的像素对应关系来增强跨帧一致性。这种对应关系进一步有助于通过跨帧特征聚合来合并冗余的高斯分布。因此，高斯分布的密度降低，通过显著降低计算和内存成本来实现在线重建。对不同数据集的广泛实验表明，StreamGS的质量与基于优化的方法相当，但速度快150倍，在处理面向对象的场景方面表现出卓越的泛化能力。 et.al.|[2503.06235](http://arxiv.org/abs/2503.06235)|null|
|**2025-03-07**|**Free Your Hands: Lightweight Relightable Turntable Capture Pipeline**|从物体的多张捕获照片中进行新颖的视图合成（NVS）是一个广泛研究的问题。实现高质量通常需要对输入视图进行密集采样，这可能会导致令人沮丧和乏味的体力劳动。手动定位摄像头以保持最佳的理想分布对人类来说可能很困难，如果找到了良好的分布，就不容易复制。此外，由于人为错误，捕获的数据可能会出现运动模糊和散焦。在本文中，我们提出了一种轻量级的对象捕获管道，以减少手动工作量并规范采集设置。我们使用消费者转盘来携带物体，使用三脚架来固定相机。随着转盘的旋转，我们会自动从各种视图和光照条件中捕获密集的样本；我们可以对多个相机位置重复此操作。这样，我们可以在几分钟内轻松捕获数百张有效图像，而无需动手。然而，在物体参考系中，光照条件各不相同；这对假设固定照明的3D高斯散射（3DGS）等标准NVS方法是有害的。我们设计了一种以光旋转为条件的神经辐射表示，解决了这个问题，并允许再发光作为额外的好处。我们使用3DGS作为底层框架展示了我们的管道，与之前的方法相比，通过详尽的采集实现了具有竞争力的质量，并展示了其重新照明和协调任务的潜力。 et.al.|[2503.05511](http://arxiv.org/abs/2503.05511)|null|
|**2025-03-07**|**MGSR: 2D/3D Mutual-boosted Gaussian Splatting for High-fidelity Surface Reconstruction under Various Light Conditions**|新视图合成（NVS）和曲面重建（SR）是三维高斯散斑（3D-GS）中的基本任务。尽管最近取得了进展，但这些任务通常是独立解决的，基于GS的渲染方法在各种光照条件下都很困难，无法生成准确的曲面，而基于GS的重建方法经常会影响渲染质量。这就提出了一个核心问题：渲染和重建必须始终涉及权衡吗？为了解决这个问题，我们提出了MGSR，这是一种用于表面重建的2D/3D相互增强高斯飞溅，可以提高渲染质量和3D重建精度。MGSR引入了两个分支——一个基于2D-GS，另一个基于3D-GS。2D-GS分支在曲面重建方面表现出色，为3D-GS分支提供了精确的几何信息。利用这种几何形状，3D-GS分支采用了一个几何引导的照明分解模块，该模块可以捕获反射和透射分量，从而在不同的光照条件下实现逼真的渲染。使用传输的分量作为监督，2D-GS分支也实现了高保真的表面重建。在整个优化过程中，2D-GS和3D-GS分支进行交替优化，提供相互监督。在此之前，每个分支都会完成一个独立的预热阶段，并实施早期停止策略以降低计算成本。我们在一组不同的合成和真实世界数据集上评估了MGSR，包括对象和场景级别，在渲染和表面重建方面表现出色。 et.al.|[2503.05182](http://arxiv.org/abs/2503.05182)|null|
|**2025-03-10**|**GSplatVNM: Point-of-View Synthesis for Visual Navigation Models Using Gaussian Splatting**|本文提出了一种将三维高斯散斑（3DGS）与视觉导航模型（VNM）相结合的图像目标导航新方法，我们称之为GSplatVNM。VNM通过引导机器人穿过一系列视点图像，为图像目标导航提供了一种有前景的范式，而不需要测量定位或特定环境的训练。然而，从开始到目标构建一个密集且可遍历的目标视点序列仍然是一个核心挑战，特别是在可用图像数据库稀疏的情况下。为了应对这些挑战，我们提出了一种基于3DGS的VNM视点合成框架，该框架综合中间视点，无缝弥合稀疏数据中的差距，同时显著降低存储开销。在真实感模拟器中的实验结果表明，我们的方法不仅提高了导航效率，而且在不同水平的图像数据库稀疏性下表现出鲁棒性。 et.al.|[2503.05152](http://arxiv.org/abs/2503.05152)|null|

<p align=right>(<a href=#updated-on-20250311>back to top</a>)</p>

## 3D Reconstruction

|Publish Date|Title|Abstract|PDF|Code|
|---|---|---|---|---|
|**2025-03-10**|**NeAS: 3D Reconstruction from X-ray Images using Neural Attenuation Surface**|从二维（2D）X射线图像重建三维（3D）结构在医疗应用中是一种有价值且有效的技术，它比计算机断层扫描需要更少的辐射暴露。最近使用隐式神经表示的方法使稀疏X射线图像能够合成新的视图。然而，尽管图像合成提高了精度，但表面形状估计的精度仍然不足。因此，我们提出了一种使用神经衰减表面（NeAS）重建3D场景的新方法，该方法同时捕获表面几何形状和衰减系数场。NeAS结合了一个带符号的距离函数（SDF），该函数定义了衰减场，并有助于提取场景中的3D表面。我们使用模拟和真实的X射线图像进行了实验，结果表明，NeAS可以仅使用2D X射线图像准确提取场景中的3D表面。 et.al.|[2503.07491](http://arxiv.org/abs/2503.07491)|null|
|**2025-03-10**|**GM-MoE: Low-Light Enhancement with Gated-Mechanism Mixture-of-Experts**|低光增强在自动驾驶、3D重建、遥感、监控等领域有着广泛的应用，可以显著提高信息利用率。然而，大多数现有方法缺乏通用性，仅限于图像恢复等特定任务。为了解决这些问题，我们提出了\textbf{门控机制专家混合（GM-MoE）}，这是第一个引入混合专家网络进行低光图像增强的框架。GM MoE由一个动态门控权重调节网络和三个子专家网络组成，每个子专家网络专门从事一项不同的增强任务。结合自行设计的门控机制，动态调整不同数据域的子专家网络的权重。此外，我们在子专家网络中集成了局部和全局特征融合，通过捕获多尺度特征来提高图像质量。实验结果表明，与25种比较方法相比，GM MoE具有更优的泛化能力，在5个基准测试中的PSNR和4个基准测试的SSIM上分别达到了最先进的性能。 et.al.|[2503.07417](http://arxiv.org/abs/2503.07417)|null|
|**2025-03-10**|**Multi-Modal 3D Mesh Reconstruction from Images and Text**|在机器人技术中，对看不见的物体进行6D物体姿态估计至关重要，但传统上依赖于需要大量数据集、高计算成本且难以推广的训练模型。零样本方法消除了训练的需要，但依赖于预先存在的3D对象模型，这通常是不切实际的。为了解决这个问题，我们提出了一种语言引导的少镜头3D重建方法，从少量输入图像重建3D网格。在所提出的流水线中，接收一组输入图像和一个语言查询。GroundingDINO和Segment Anything模型的组合输出分段掩模，使用VGGSfM从中重建稀疏点云。随后，使用高斯散斑法SuGAR重建网格。在最后的清洁步骤中，去除伪影，从而得到查询对象的最终3D网格。我们从几何和纹理的准确性和质量方面对该方法进行了评估。此外，我们研究了成像条件（如视角、输入图像数量和图像重叠）对3D对象重建质量、效率和计算可扩展性的影响。 et.al.|[2503.07190](http://arxiv.org/abs/2503.07190)|null|
|**2025-03-10**|**Accessing the Effect of Phyllotaxy and Planting Density on Light Use Efficiency in Field-Grown Maize using 3D Reconstructions**|高密度种植是一种广泛采用的提高玉米生产力的策略，但它也带来了诸如增加套种竞争和遮荫等挑战，这可能会限制光捕获和整体产量潜力。作为回应，一些玉米植株自然地重新调整其冠层以优化光捕获，这一过程被称为冠层重新定位。了解这种适应性反应及其对光捕获的影响对于最大限度地提高农业产量潜力至关重要。本研究引入了一个端到端的框架，该框架将田间玉米的真实3D重建与光合活性辐射（标准杆数）模型相结合，以评估叶性和种植密度对光拦截的影响。特别是，使用源自田间数据的3D点云，构建了一组不同玉米基因型的虚拟田间，并根据田间标准杆数测量进行了验证。利用该框架，我们详细分析了林冠方向、植物和行间距以及种植行方向对整个典型生长季节标准杆数截留的影响。我们的研究结果强调了不同种植密度和冠层方向的光截获效率存在显著差异。通过阐明冠层结构与光捕获之间的关系，本研究为优化不同农业环境中的玉米育种和栽培策略提供了有价值的指导。 et.al.|[2503.06887](http://arxiv.org/abs/2503.06887)|null|
|**2025-03-10**|**Sub-Image Recapture for Multi-View 3D Reconstruction**|由于大输入图像尺寸所需的大内存，高分辨率目标的3D重建仍然是一项具有挑战性的任务。最近开发的基于学习的算法提供了比传统算法更有前景的重建性能，然而，它们通常需要比传统算法更多的内存，并面临可扩展性问题。在这篇论文中，我们开发了一种通用的方法，子图像重捕获（SIR），将大图像分割成更小的子图像并单独处理。由于该框架，现有的3D重建算法可以基于子图像再捕获来实现，大大减少了内存，大大提高了可扩展性 et.al.|[2503.06818](http://arxiv.org/abs/2503.06818)|null|
|**2025-03-09**|**Gaussian RBFNet: Gaussian Radial Basis Functions for Fast and Accurate Representation and Reconstruction of Neural Fields**|DeepSDF和神经辐射场等神经场最近彻底改变了RGB图像和视频的新颖视图合成和3D重建。然而，实现高质量的表示、重建和渲染需要深度神经网络，而深度神经网络的训练和评估速度很慢。尽管已经提出了几种加速技术，但它们经常以速度换取内存。另一方面，基于高斯飞溅的方法加快了渲染时间，但在存储大量高斯参数所需的训练速度和内存方面仍然成本高昂。在本文中，我们介绍了一种新的神经表示方法，它在训练和推理时间都很快，而且很轻。我们的关键观察是，传统MLP中使用的神经元执行简单的计算（点积，然后是ReLU激活），因此需要使用宽和深MLP或高分辨率和高维特征网格来参数化复杂的非线性函数。我们在这篇论文中表明，通过用径向基函数（RBF）核替换传统神经元，只需一层这样的神经元，就可以实现2D（RGB图像）、3D（几何）和5D（辐射场）信号的高精度表示。该表示具有高度的并行性，可在低分辨率特征网格上运行，并且结构紧凑，内存高效。我们证明，所提出的新表示可以在不到15秒的时间内训练出3D几何表示，在不到十五分钟的时间内就可以训练出新的视图合成。在运行时，它可以在不牺牲质量的情况下以超过60 fps的速度合成新颖的视图。 et.al.|[2503.06762](http://arxiv.org/abs/2503.06762)|null|
|**2025-03-09**|**Sign Language Translation using Frame and Event Stream: Benchmark Dataset and Algorithms**|准确的手语理解是残疾人的重要沟通渠道。当前的手语翻译算法主要依赖于RGB帧，这可能受到固定帧率、可变光照条件和快速手部运动引起的运动模糊的限制。受最近事件相机在其他领域的成功应用的启发，我们建议利用事件流来协助RGB相机捕获手势数据，以解决上述各种挑战。具体来说，我们首先使用DVS346相机收集了一个大规模的RGB事件手语翻译数据集，称为VECSL，其中包含15676个RGB事件样本、15191个注释，涵盖2568个汉字。这些样本是在各种室内和室外环境中收集的，捕捉了多个视角、不同的光强度和不同的相机运动。由于在这个新任务中没有用于比较的基准算法，我们重新训练和评估了多种最先进的SLT算法，并相信这个基准可以有效地支持后续的相关研究。此外，我们提出了一种新的RGB事件手语翻译框架（即M $^2$ -SLT），该框架结合了细粒度微符号和粗粒度宏符号检索，在所提出的数据集上实现了最先进的结果。源代码和数据集都将在https://github.com/Event-AHU/OpenESL. et.al.|[2503.06484](http://arxiv.org/abs/2503.06484)|null|
|**2025-03-09**|**StructGS: Adaptive Spherical Harmonics and Rendering Enhancements for Superior 3D Gaussian Splatting**|3D重建与神经渲染技术的最新进展极大地改善了照片级逼真3D场景的创建，影响了学术研究和工业应用。3D高斯散点技术及其变体结合了基于基元和体积表示的优点，实现了卓越的渲染质量。虽然3D几何散射（3DGS）及其变体推进了3D表示领域，但它们在训练过程中未能捕捉到非局部结构信息的随机特性。此外，基于3DGS的方法中球面函数的初始化通常无法在早期训练回合中使用高阶项，从而导致训练过程中不必要的计算开销。此外，目前基于3DGS的方法需要在更高分辨率的图像上进行训练以呈现更高分辨率输出，这大大增加了内存需求并延长了训练持续时间。我们介绍了StructGS，这是一个增强3D高斯散点（3DGS）的框架，用于改进3D重建中的新颖视图合成。StructGS创新性地结合了基于补丁的SSIM损耗、动态球面谐波初始化和多尺度残差网络（MSRN），分别解决了上述局限性。我们的框架显著减少了计算冗余，增强了细节捕捉，并支持从低分辨率输入进行高分辨率渲染。实验表明，StructGS的性能优于最先进的（SOTA）模型，能够以更少的伪影实现更高质量、更详细的渲染。 et.al.|[2503.06462](http://arxiv.org/abs/2503.06462)|null|
|**2025-03-08**|**RGB-Phase Speckle: Cross-Scene Stereo 3D Reconstruction via Wrapped Pre-Normalization**|随着高级图像应用的发展，3D重建越来越受到关注，其中密集立体匹配（DSM）是一项关键技术。以前的研究通常依赖于公开可用的数据集进行训练，重点是修改网络架构或合并专门的模块来提取域不变特征，从而提高模型的鲁棒性。相比之下，受单帧结构光相移编码的启发，本研究引入了RGB散斑，这是一种基于主动立体相机系统的跨场景3D重建框架，旨在增强鲁棒性。具体来说，我们提出了一种新的相位预归一化编码解码方法：首先，我们随机扰动相移图并将其嵌入到三个RGB通道中以生成彩色散斑图案；随后，相机捕获由物体调制的相位编码图像作为立体匹配网络的输入。该技术有效地减轻了外部干扰，并确保了RGB散斑的一致输入数据，从而增强了跨域3D重建的稳定性。为了验证所提出的方法，我们进行了复杂的实验：（1）基于所提出的编码方案构建了一个用于复杂场景的彩色散斑数据集；（2） 评估相位预归一化编码解码技术对3D重建精度的影响；以及（3）进一步研究其在不同条件下的鲁棒性。实验结果表明，所提出的RGB散斑模型在跨域和跨场景3D重建任务中具有显著优势，增强了模型泛化能力，增强了在具有挑战性的环境中的鲁棒性，从而为鲁棒3D重建研究提供了一种新的解决方案。 et.al.|[2503.06125](http://arxiv.org/abs/2503.06125)|null|
|**2025-03-08**|**GrInAdapt: Scaling Retinal Vessel Structural Map Segmentation Through Grounding, Integrating and Adapting Multi-device, Multi-site, and Multi-modal Fundus Domains**|视网膜血管分割对于诊断眼部疾病至关重要，但目前的深度学习方法受到特定模态挑战和成像设备、分辨率和解剖区域之间显著分布变化的限制。在这篇论文中，我们提出了GrInAdapt，这是一种新的无源多目标域自适应框架，它利用多视图图像来细化分割标签，并增强眼底光学相干断层扫描血管造影（OCTA）的模型泛化能力。GrInAdapt遵循一种直观的三步方法：（i）通过注册将图像固定到一个共同的锚空间，（ii）整合来自多个视图的预测以实现改进的标签共识，以及（iii）使源模型适应不同的目标域。此外，GrInAdapt足够灵活，可以结合彩色眼底摄影等辅助手段，为稳健的血管分割提供补充线索。在多设备、多站点和多模态视网膜数据集上进行的广泛实验表明，GrInAdapt明显优于现有的域自适应方法，在多个域上实现了更高的分割精度和鲁棒性。这些结果突出了GrInAdapt在推进自动化视网膜血管分析和支持稳健临床决策方面的潜力。 et.al.|[2503.05991](http://arxiv.org/abs/2503.05991)|null|

<p align=right>(<a href=#updated-on-20250311>back to top</a>)</p>

## Diffusion

|Publish Date|Title|Abstract|PDF|Code|
|---|---|---|---|---|
|**2025-03-10**|**Trapping and Transport of Inertial Particles in a Taylor-Green Vortex: Effects of Added Mass and History Force**|我们研究了二维稳态泰勒-格林涡旋流中小惯性粒子的动力学。Taylor（2022）的一项经典研究表明，当测量颗粒惯性的斯托克斯数St小于1/4时，重惯性点颗粒（密度参数R=1）被流分离器捕获。在这里，我们考虑有限密度粒子，结合了之前被忽视的附加质量效应和Boussinesq-Basset历史力。利用驻点附近的线性稳定性分析，我们确定了St-R平面中导致粒子被困在涡流单元内的临界参数条件。当考虑附加质量效应时，我们识别出惯性粒子感知到的额外滞流点，这些滞流点超出了涡流室角的传统滞流点。我们分析了它们的稳定性。对整个非线性系统的数值分析证实，根据初始条件，存在不同的粒子行为——俘获、扩散和弹道——这与Nath等人（2024）的观点一致，并因附加质量效应而有所修改。我们根据突出的粒子动力学描绘了St-R平面中这些行为占主导地位的区域。然而，当同时考虑历史力和附加质量效应时，所有粒子都表现出弹道运动，而与St和R无关。 et.al.|[2503.07480](http://arxiv.org/abs/2503.07480)|null|
|**2025-03-10**|**DRESS: Diffusion Reasoning-based Reward Shaping Scheme For Intelligent Networks**|网络优化仍然是无线通信的基础，基于人工智能（AI）的解决方案得到了广泛采用。随着第六代（6G）通信网络追求全场景覆盖，复杂极端环境中的优化面临着前所未有的挑战。这些环境的动态特性，再加上物理约束，使得深度强化学习（DRL）等人工智能解决方案难以为训练过程获得有效的奖励反馈。然而，许多现有的基于DRL的网络优化研究通过理想化的环境设置忽视了这一挑战。受生成人工智能（GenAI），特别是扩散模型在捕捉复杂潜在分布方面的强大能力的启发，我们引入了一种新的基于扩散推理的奖励整形方案（DRESS）来实现鲁棒的网络优化。通过对观察到的环境状态和执行的动作进行调节，DRESS利用扩散模型的多步去噪过程作为一种深度推理的形式，逐步细化潜在表示，以生成有意义的辅助奖励信号，捕捉网络系统的模式。此外，DRESS旨在与任何DRL框架无缝集成，使DRESS辅助DRL（DRESSed DRL）即使在极端网络环境下也能实现稳定高效的DRL训练。实验结果表明，与基线方法相比，DRESSed DRL在稀疏奖励无线环境中的收敛速度比其原始版本快约1.5倍，在多个通用DRL基准环境中的性能也有显著提高。DRESS的代码可在以下网址获得https://github.com/NICE-HKU/DRESS. et.al.|[2503.07433](http://arxiv.org/abs/2503.07433)|null|
|**2025-03-10**|**AR-Diffusion: Asynchronous Video Generation with Auto-Regressive Diffusion**|视频生成的任务需要合成视觉上逼真且时间上连贯的视频帧。现有的方法主要使用异步自回归模型或同步扩散模型来解决这一挑战。然而，异步自回归模型经常受到训练和推理之间不一致的影响，导致误差累积等问题，而同步扩散模型则受到其对刚性序列长度依赖的限制。为了解决这些问题，我们引入了自回归扩散（AR扩散），这是一种新的模型，结合了自回归和扩散模型的优点，用于灵活、异步的视频生成。具体来说，我们的方法利用扩散来逐渐破坏训练和推理中的视频帧，从而减少这些阶段之间的差异。受自回归生成的启发，我们对单个帧的腐败时间步长进行了非递减约束，确保早期帧比后续帧更清晰。这种设置，再加上时间因果注意力，可以灵活地生成不同长度的视频，同时保持时间连贯性。此外，我们设计了两个专门的时间步长调度器：FoPP调度器用于训练期间的平衡时间步长采样，AD调度器用于推理期间灵活的时间步长差异，支持同步和异步生成。广泛的实验证明了我们提出的方法的优越性，该方法在四个具有挑战性的基准测试中取得了具有竞争力和最先进的结果。 et.al.|[2503.07418](http://arxiv.org/abs/2503.07418)|null|
|**2025-03-10**|**TimeStep Master: Asymmetrical Mixture of Timestep LoRA Experts for Versatile and Efficient Diffusion Models in Vision**|在过去几年中，扩散模型推动了视觉生成的进步。然而，由于大量的微调成本，将这些大型模型应用于下游任务通常很困难。最近，低秩自适应（LoRA）已被应用于扩散模型的有效调谐。不幸的是，LoRA调谐扩散模型的能力是有限的，因为相同的LoRA用于扩散过程的不同时间步。为了解决这个问题，我们引入了一个通用而简洁的TimeStep-Master（TSM）范式，其中包含两个关键的微调阶段。在培育阶段（1阶段），我们应用不同的LoRA在不同的时间步长间隔内微调扩散模型。这导致不同的TimeStep LoRA专家能够有效地捕捉不同的噪声水平。在组装阶段（2阶段），我们通过专家在多尺度区间的核心上下文协作，设计了一种新型的TimeStep-LoRA专家不对称混合。对于每个时间步，我们利用最小间隔内的timestep LoRA专家作为无门控的核心专家，并使用较大间隔内的专家作为具有时间依赖门控的上下文专家。因此，我们的TSM可以通过专家在最精细的区间内有效地对噪声水平进行建模，并自适应地整合其他尺度专家的上下文，从而提高扩散模型的通用性。为了证明我们的TSM范式的有效性，我们对扩散模型的三个典型和流行的LoRA相关任务进行了广泛的实验，包括域适应、后预训练和模型蒸馏。我们的TSM在各种模型结构（UNet、DiT和MM-DiT）和视觉数据模态（图像、视频）中，在所有这些任务上都取得了最先进的结果，显示了其出色的泛化能力。 et.al.|[2503.07416](http://arxiv.org/abs/2503.07416)|null|
|**2025-03-10**|**Bound state formation within the Lindblad approach**|Lindblad主方程是一种常用的马尔可夫方法，用于根据约化密度矩阵的时间演化来描述开放量子系统。在这里，追踪热环境以获得一个表达式来描述所谓的系统的演化：一个粒子或一系列相互作用的粒子，它们被热浴包围。在这项工作中，我们研究了非相对论束缚态的形成，涉及P“oschl-Teller势，以讨论形成时间和热平衡，应用核物理学的尺度。这个问题借鉴了重离子碰撞领域，其中氘核是在化学冻结温度附近的温度范围内测量的探针，而氘核本身的结合能要低得多。这被称为“地狱中的雪球”。我们使用重新表述的Lindblad方程，根据有源的扩散-平流方程，从而提供了耗散量子主方程的流体动力学公式。 et.al.|[2503.07402](http://arxiv.org/abs/2503.07402)|null|
|**2025-03-10**|**SPEED: Scalable, Precise, and Efficient Concept Erasure for Diffusion Models**|由于对版权侵权、攻击性内容和隐私侵犯的日益关注，从大规模文本到图像（T2I）传播模型中删除概念变得越来越重要。然而，由于固有的优化限制，现有方法要么需要昂贵的微调，要么降低非目标概念（即先验）的图像质量。在本文中，我们介绍了SPEED，这是一种基于模型编辑的概念擦除方法，利用零空间约束实现可扩展、精确和高效的擦除。具体来说，SPEED结合了基于影响的先验滤波（IPF），以在擦除过程中保留受影响最大的非目标概念，定向先验增强（DPA），以扩大先验覆盖范围，同时保持语义一致性，以及不变相等约束（IEC），通过在T2I生成过程中显式保留关键不变量来规范模型编辑。对多个概念擦除任务的广泛评估表明，SPEED在先前保存方面始终优于现有方法，同时实现了高效高保真的概念擦除，在短短5秒内成功删除了100个概念。我们的代码和型号可在以下网址获得：https://github.com/Ouxiang-Li/SPEED. et.al.|[2503.07392](http://arxiv.org/abs/2503.07392)|null|
|**2025-03-10**|**PersonaBooth: Personalized Text-to-Motion Generation**|本文介绍了运动个性化，这是一项新任务，它使用包含Persona的几个基本运动生成与文本描述对齐的个性化运动。为了支持这项新任务，我们引入了一个名为PerMo（PersonaMotion）的新的大规模运动数据集，它捕获了多个演员的独特角色。我们还提出了一种称为PersonaBooth的预训练运动扩散模型的多模态微调方法。PersonaBooth解决了两个主要挑战：i）以人物角色为中心的PerMo数据集和缺乏人物角色特定数据的预训练数据集之间存在显著的分布差距，ii）从动作中捕捉一致人物角色的难度因内容（动作类型）而异。为了解决数据集分布差距，我们引入了一个人物角色令牌来接受新的人物角色特征，并在微调过程中对文本和视觉效果进行多模态自适应。为了捕捉一致的人物角色，我们采用对比学习技术来增强具有相同人物角色的样本之间的内部凝聚力。此外，我们引入了一种上下文感知融合机制，以最大限度地整合来自多个输入动作的角色线索。PersonaBooth的表现优于最先进的运动风格转换方法，为运动个性化树立了新的基准。 et.al.|[2503.07390](http://arxiv.org/abs/2503.07390)|null|
|**2025-03-10**|**TRCE: Towards Reliable Malicious Concept Erasure in Text-to-Image Diffusion Models**|文本到图像扩散模型的最新进展能够生成逼真的图像，但它们也有可能产生恶意内容，如NSFW图像。为了降低风险，研究了概念擦除方法，以促进模型忘却特定概念。然而，目前的研究很难完全消除隐含在提示中的恶意概念（例如隐喻表达或对抗性提示），同时保留模型的正常生成能力。为了应对这一挑战，我们的研究提出了TRCE，使用两阶段概念擦除策略来实现可靠擦除和知识保存之间的有效权衡。首先，TRCE首先删除文本提示中隐含的恶意语义。通过确定一个关键的映射目标（即[EoT]嵌入），我们优化了交叉注意力层，将恶意提示映射到上下文相似但具有安全概念的提示。此步骤可防止模型在去噪过程中受到恶意语义的过度影响。在此基础上，考虑到扩散模型采样轨迹的确定性，TRCE通过对比学习进一步将早期去噪预测转向安全方向，远离不安全方向，从而进一步避免恶意内容的产生。最后，我们在多个恶意概念擦除基准上对TRCE进行了全面评估，结果表明它在擦除恶意概念的同时更好地保留了模型的原始生成能力。该代码可在以下网址获得：http://github.com/ddgoodgood/TRCE.注意：本文包括可能包含冒犯性内容的模型生成内容。 et.al.|[2503.07389](http://arxiv.org/abs/2503.07389)|null|
|**2025-03-10**|**Molecular Weight-Dependent Evaporation Dynamics and Morphology of PEG Sessile Drops on Hydrophobic Substrates**|固着液滴的蒸发动力学对于喷墨打印和药物开发等应用中的材料沉积至关重要。然而，高分子量聚合物溶液的蒸发行为及其对沉积物形态和流场的影响尚不清楚。本研究调查了分子量为200至1000k g/mol的聚乙二醇（PEG）溶液滴在疏水基材上的蒸发动力学和沉积形态，涵盖了五个数量级。结果表明，在所有PEG分子量范围内，蒸汽扩散主导了蒸发过程。通过图像分析和微粒图像测速技术（ $\mu$ -PIV），我们发现分子量会影响接触线动力学和内部流动，从而导致不同的沉积物形态，包括球形帽、柱状、池状盘和平盘。瞬态散度和P’clet数计算进一步证实了水动力学在矿床形成中的作用。这些发现为控制聚合物固着液滴蒸发的流体动力学和热力学因素提供了见解，对材料制造和喷墨印刷和涂层技术的发展具有重要意义。 et.al.|[2503.07372](http://arxiv.org/abs/2503.07372)|null|
|**2025-03-10**|**AttenST: A Training-Free Attention-Driven Style Transfer Framework with Pre-Trained Diffusion Models**|虽然扩散模型在风格转换任务中取得了显著进展，但现有的方法通常依赖于在推理过程中对预训练模型进行微调或优化，这导致了高昂的计算成本和在平衡内容保存与风格集成方面的挑战。为了解决这些局限性，我们引入了AttenST，这是一个无需训练的注意力驱动风格转换框架。具体来说，我们提出了一种风格引导的自我注意力机制，通过保留内容图像的查询，同时用风格图像中的键和值替换其键和值，将自我注意力限制在参考风格上，从而实现有效的风格特征整合。为了减少反演过程中样式信息的丢失，我们引入了一种样式保持反演策略，通过多个重采样步骤来提高反演精度。此外，我们提出了一种内容感知自适应实例规范化方法，该方法将内容统计信息集成到规范化过程中，以优化样式融合，同时减轻内容退化。此外，我们引入了一种双重特征交叉注意机制，将内容和风格特征融合在一起，确保结构保真度和风格表达的和谐综合。大量实验表明，AttenST优于现有方法，在风格转换数据集中实现了最先进的性能。 et.al.|[2503.07307](http://arxiv.org/abs/2503.07307)|null|

<p align=right>(<a href=#updated-on-20250311>back to top</a>)</p>

## NeRF

|Publish Date|Title|Abstract|PDF|Code|
|---|---|---|---|---|
|**2025-03-09**|**Gaussian RBFNet: Gaussian Radial Basis Functions for Fast and Accurate Representation and Reconstruction of Neural Fields**|DeepSDF和神经辐射场等神经场最近彻底改变了RGB图像和视频的新颖视图合成和3D重建。然而，实现高质量的表示、重建和渲染需要深度神经网络，而深度神经网络的训练和评估速度很慢。尽管已经提出了几种加速技术，但它们经常以速度换取内存。另一方面，基于高斯飞溅的方法加快了渲染时间，但在存储大量高斯参数所需的训练速度和内存方面仍然成本高昂。在本文中，我们介绍了一种新的神经表示方法，它在训练和推理时间都很快，而且很轻。我们的关键观察是，传统MLP中使用的神经元执行简单的计算（点积，然后是ReLU激活），因此需要使用宽和深MLP或高分辨率和高维特征网格来参数化复杂的非线性函数。我们在这篇论文中表明，通过用径向基函数（RBF）核替换传统神经元，只需一层这样的神经元，就可以实现2D（RGB图像）、3D（几何）和5D（辐射场）信号的高精度表示。该表示具有高度的并行性，可在低分辨率特征网格上运行，并且结构紧凑，内存高效。我们证明，所提出的新表示可以在不到15秒的时间内训练出3D几何表示，在不到十五分钟的时间内就可以训练出新的视图合成。在运行时，它可以在不牺牲质量的情况下以超过60 fps的速度合成新颖的视图。 et.al.|[2503.06762](http://arxiv.org/abs/2503.06762)|null|
|**2025-03-09**|**X-LRM: X-ray Large Reconstruction Model for Extremely Sparse-View Computed Tomography Recovery in One Second**|稀疏视图3D CT重建旨在从有限数量的2D X射线投影中恢复体积结构。现有的前馈方法受到基于CNN的架构容量有限和大规模训练数据集稀缺的限制。本文提出了一种用于极稀疏视图（<10视图）CT重建的X射线大重建模型（X-LRM）。X-LRM由两个关键部件组成：X-former和X-triplane。我们的X-former可以使用基于MLP的图像标记器和基于Transformer的编码器来处理任意数量的输入视图。然后，输出标记被上采样到我们的X三平面表示中，该表示将3D辐射密度建模为隐式神经场。为了支持X-LRM的训练，我们引入了Torso-16K，这是一个由各种躯干器官的16K多个体积投影对组成的大规模数据集。大量实验表明，X-LRM的性能比最先进的方法高出1.5 dB，速度快27倍，灵活性更好。此外，肺部分割任务的下游评估也表明了我们方法的实用价值。我们的代码、预训练模型和数据集将于https://github.com/caiyuanhao1998/X-LRM et.al.|[2503.06382](http://arxiv.org/abs/2503.06382)|null|
|**2025-03-05**|**Distilling Dataset into Neural Field**|利用大规模数据集对于训练高性能深度学习模型至关重要，但它也带来了巨大的计算和存储成本。为了克服这些挑战，数据集蒸馏已成为一种有前景的解决方案，它将大规模数据集压缩成一个较小的合成数据集，保留了训练所需的基本信息。本文提出了一种新的数据集提取参数化框架，称为神经场提取数据集（DDiF），它利用神经场存储大规模数据集的必要信息。由于神经场以坐标作为输入和输出量的独特性质，DDiF有效地保留了信息，并易于生成各种形状的数据。我们从理论上证实，当单个合成实例的使用预算相同时，DDiF表现出比以前的一些文献更大的表现力。通过广泛的实验，我们证明DDiF在几个基准数据集上取得了卓越的性能，扩展到图像域之外，包括视频、音频和3D体素。我们在发布代码https://github.com/aailab-kaist/DDiF. et.al.|[2503.04835](http://arxiv.org/abs/2503.04835)|null|
|**2025-02-27**|**RANGE: Retrieval Augmented Neural Fields for Multi-Resolution Geo-Embeddings**|地理位置表示的选择会显著影响各种地理空间任务模型的准确性，包括细粒度物种分类、种群密度估计和生物群落分类。最近的作品，如SatCLIP和GeoCLIP，通过将地理位置与共置图像进行对比对齐来学习这种表示。虽然这些方法非常有效，但在本文中，我们认为当前的训练策略未能完全捕捉到重要的视觉特征。我们从信息论的角度解释了为什么这些方法产生的嵌入会丢弃对许多下游任务很重要的关键视觉信息。为了解决这个问题，我们提出了一种新的检索增强策略，称为RANGE。我们的方法基于这样一种直觉，即可以通过组合来自多个看起来相似的位置的视觉特征来估计位置的视觉特性。我们在各种各样的任务中评估我们的方法。我们的结果表明，RANGE在大多数任务中表现优于现有的最先进的模型，并具有显著的优势。我们显示，分类任务的收益高达13.1%，回归任务的收益为0.145 $R^2$ 。我们所有的代码都将在GitHub上发布。我们的模型将在HuggingFace上发布。 et.al.|[2502.19781](http://arxiv.org/abs/2502.19781)|null|
|**2025-03-04**|**MedFuncta: Modality-Agnostic Representations Based on Efficient Neural Fields**|最近关于深度学习医学图像分析的研究几乎完全集中在基于网格或体素的数据表示上。我们通过引入MedFuncta来挑战这一常见选择，MedFuncta是一种基于神经场的模态无关连续数据表示。我们演示了如何通过利用医学信号中的冗余以及应用具有上下文缩减方案的高效元学习方法，将神经场从单个实例扩展到大型数据集。我们通过引入 $\omega_0$ -调度，提高重建质量和收敛速度，进一步解决了常用SIREN激活中的光谱偏差问题。我们在各种不同维度和模式的医学信号上验证了我们提出的方法（1D：心电图；2D：胸部X射线、视网膜OCT、眼底照相机、皮肤镜、结肠组织病理学、细胞显微镜；3D：脑MRI、肺CT），并成功证明我们可以解决这些表示的相关下游任务。我们还发布了一个超过550k个带注释神经场的大规模数据集，以促进这方面的研究。 et.al.|[2502.14401](http://arxiv.org/abs/2502.14401)|**[link](https://github.com/pfriedri/medfuncta)**|
|**2025-02-15**|**Implicit Neural Representations of Molecular Vector-Valued Functions**|分子有各种计算表示，包括数值描述符、字符串、图形、点云和曲面。每种表示方法都可以应用各种机器学习方法，从线性回归到与大型语言模型配对的图神经网络。为了补充现有的表示，我们通过向量值函数或n维向量场引入分子的表示，这些向量值函数由神经网络参数化，我们称之为分子神经场。与表面表征不同，分子神经场捕获蛋白质等大分子的外部特征和疏水核心。与离散图或点表示相比，分子神经场结构紧凑，分辨率无关，天生适合在空间和时间维度上进行插值。分子神经场继承的这些特性适用于包括基于所需形状、结构和组成生成分子，以及空间和时间中分子构象之间分辨率无关的插值在内的任务。在这里，我们为分子神经场提供了一个框架和概念证明，即使用自动解码器架构对蛋白质-配体复合物进行参数化和超分辨率重建，以及使用自动编码器架构将分子体积嵌入潜在空间。 et.al.|[2502.10848](http://arxiv.org/abs/2502.10848)|**[link](https://github.com/daenuprobst/minf)**|
|**2025-02-05**|**Poisson Hypothesis and large-population limit for networks of spiking neurons**|我们研究了具有随机尖峰时间的线性（泄漏）和二次积分和放电神经元的空间扩展网络的平均场描述。我们考虑了具有线性和二次内在动力学的连续时间Galves-L“ocherbach（GL）网络的大种群极限。我们证明了泊松假设适用于这些网络的复制平均场极限，即在适当定义的极限内，神经元是独立的，相互作用时间被强度取决于平均放电率的独立时间非均匀泊松过程所取代，将已知结果扩展到具有二次内在动态和重置的网络。证明泊松假设成立为研究这些网络中的大种群限值开辟了可能性。我们证明这个极限是一个适定的神经场模型，受随机重置的影响。 et.al.|[2502.03379](http://arxiv.org/abs/2502.03379)|null|
|**2025-02-04**|**Geometric Neural Process Fields**|本文解决了神经场（NeF）泛化的挑战，其中模型必须有效地适应仅给出少量观测值的新信号。为了解决这个问题，我们提出了几何神经过程场（G-NPF），这是一个明确捕捉不确定性的神经辐射场的概率框架。我们将NeF泛化表述为概率问题，从而能够从有限的上下文观测中直接推断出NeF函数分布。为了引入结构归纳偏差，我们引入了一组几何基来编码空间结构，并促进NeF函数分布的推断。在此基础上，我们设计了一个分层潜在变量模型，使G-NPF能够整合多个空间层次的结构信息，并有效地参数化INR函数。这种分层方法提高了对新场景和未知信号的泛化能力。针对3D场景的新颖视图合成以及2D图像和1D信号回归的实验证明了我们的方法在捕捉不确定性和利用结构信息提高泛化能力方面的有效性。 et.al.|[2502.02338](http://arxiv.org/abs/2502.02338)|null|
|**2025-02-05**|**A Poisson Process AutoDecoder for X-ray Sources**|钱德拉X射线天文台和eROSITA等X射线观测设施已经探测到数百万个与高能现象相关的天文源。光子的到达作为时间的函数遵循泊松过程，并且可以按数量级变化，这为源分类、物理性质推导和异常检测等常见任务带来了障碍。之前的工作要么未能直接捕捉数据的泊松性质，要么只关注泊松率函数重建。在这项工作中，我们提出了泊松过程自动解码器（PPAD）。PPAD是一种神经场解码器，通过无监督学习将固定长度的潜在特征映射到跨能带和时间的连续泊松率函数。PPAD重建速率函数并同时产生表示。我们使用钱德拉源目录通过重建、回归、分类和异常检测实验证明了PPAD的有效性。 et.al.|[2502.01627](http://arxiv.org/abs/2502.01627)|null|
|**2025-02-03**|**Regularized interpolation in 4D neural fields enables optimization of 3D printed geometries**|精确生产具有特定特性的几何形状的能力可能是制造过程中最重要的特征。3D打印具有非凡的设计自由度和复杂性，但也容易出现几何和其他缺陷，必须解决这些缺陷才能充分发挥其潜力。最终，这将需要精明的设计决策和及时的参数调整来保持稳定性，即使是专业的人类操作员也很难做到这一点。虽然机器学习在3D打印中得到了广泛的研究，但现有的方法通常会忽略不同打印的空间特征，因此很难产生所需的几何形状。在这里，我们将打印部件的体积表示编码到神经场中，并应用一种新的正则化策略，该策略基于最小化场输出相对于单个不可学习参数的偏导数。因此，通过鼓励小的输入变化只产生小的输出变化，我们鼓励在观测体积之间进行平滑插值，从而实现现实的几何预测。因此，该框架允许提取“想象的”3D形状，揭示了在以前看不见的参数下制造的零件的外观。由此产生的连续场用于数据驱动优化，以最大限度地提高预期和生产几何形状之间的几何保真度，减少后处理、材料浪费和生产成本。通过动态优化工艺参数，我们的方法实现了先进的规划策略，有可能使制造商更好地实现复杂和功能丰富的设计。 et.al.|[2502.01517](http://arxiv.org/abs/2502.01517)|**[link](https://github.com/cam-cambridge/4d-neural-fields-optimise-3d-printing)**|

<p align=right>(<a href=#updated-on-20250311>back to top</a>)</p>

[contributors-shield]: https://img.shields.io/github/contributors/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[contributors-url]: https://github.com/Vincentqyw/cv-arxiv-daily/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[forks-url]: https://github.com/Vincentqyw/cv-arxiv-daily/network/members
[stars-shield]: https://img.shields.io/github/stars/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[stars-url]: https://github.com/Vincentqyw/cv-arxiv-daily/stargazers
[issues-shield]: https://img.shields.io/github/issues/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[issues-url]: https://github.com/Vincentqyw/cv-arxiv-daily/issues

