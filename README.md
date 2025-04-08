[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]

## Updated on 2025.04.08
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
|**2025-04-07**|**One-Minute Video Generation with Test-Time Training**|今天的变形金刚仍然很难制作一分钟的视频，因为自我关注层在长时间的背景下效率低下。曼巴图层等替代方案难以处理复杂的多场景故事，因为它们的隐藏状态表现力较弱。我们尝试了测试时间训练（TTT）层，其隐藏状态本身可以是神经网络，因此更具表现力。将TTT层添加到预训练的Transformer中，使其能够从文本故事板生成一分钟的视频。为了验证概念，我们根据《猫和老鼠》漫画策划了一个数据集。与Mamba~2、门控DeltaNet和滑动窗口注意力层等基线相比，TTT层生成了更连贯的视频，讲述了复杂的故事，在每种方法100个视频的人类评估中领先34个Elo点。尽管有希望，但结果仍然包含伪影，这可能是由于预训练的5B模型的能力有限。我们的执行效率也可以提高。由于资源限制，我们只尝试了一分钟的视频，但这种方法可以扩展到更长的视频和更复杂的故事。示例视频、代码和注释可在以下网址获得：https://test-time-training.github.io/video-dit et.al.|[2504.05298](http://arxiv.org/abs/2504.05298)|null|
|**2025-04-07**|**Video-Bench: Human-Aligned Video Generation Benchmark**|视频生成评估对于确保生成模型在符合人类期望的同时生成视觉逼真、高质量的视频至关重要。当前的视频生成基准分为两大类：传统基准，它使用度量和嵌入来评估跨多个维度生成的视频质量，但往往与人类判断不一致；基于大型语言模型（LLM）的基准测试虽然能够进行类似人类的推理，但受到对视频质量指标和跨模态一致性理解有限的限制。为了应对这些挑战并建立一个更符合人类偏好的基准，本文介绍了Video Bench，这是一个全面的基准，具有丰富的提示套件和广泛的评估维度。该基准测试首次尝试在生成模型中系统地利用MLLM进行与视频生成评估相关的所有维度。通过结合少量镜头评分和查询链技术，Video Bench为生成的视频评估提供了一种结构化、可扩展的方法。在包括Sora在内的先进模型上的实验表明，Video Bench在所有维度上都与人类偏好高度一致。此外，在我们的框架评估与人类评估不同的情况下，它始终如一地提供更客观和准确的见解，这表明它比传统的人类判断具有更大的潜在优势。 et.al.|[2504.04907](http://arxiv.org/abs/2504.04907)|null|
|**2025-04-07**|**FantasyTalking: Realistic Talking Portrait Generation via Coherent Motion Synthesis**|从单个静态肖像创建逼真的可动画化身仍然具有挑战性。现有的方法往往很难捕捉到微妙的面部表情、相关的全局身体动作和动态背景。为了解决这些局限性，我们提出了一种新的框架，该框架利用预训练的视频扩散变换器模型来生成具有可控运动动态的高保真、连贯的谈话肖像。我们工作的核心是双阶段视听对齐策略。在第一阶段，我们采用剪辑级训练方案，通过在整个场景中对齐音频驱动的动态来建立连贯的全局运动，包括参考肖像、上下文对象和背景。在第二阶段，我们使用嘴唇跟踪掩模在帧级别细化嘴唇运动，确保与音频信号的精确同步。为了在不影响运动灵活性的情况下保持身份，我们用一个面部聚焦的交叉注意力模块取代了常用的参考网络，该模块在整个视频中有效地保持了面部的一致性。此外，我们还集成了一个运动强度调制模块，该模块明确控制表情和身体运动强度，从而能够对肖像运动进行可控的操纵，而不仅仅是嘴唇运动。大量的实验结果表明，我们提出的方法实现了更高的质量，具有更好的真实感、连贯性、运动强度和身份保持。我们的项目页面：https://fantasy-amap.github.io/fantasy-talking/. et.al.|[2504.04842](http://arxiv.org/abs/2504.04842)|null|
|**2025-04-05**|**Video4DGen: Enhancing Video and 4D Generation through Mutual Optimization**|4D（即顺序3D）生成的进步为各种应用中的逼真体验开辟了新的可能性，用户可以从任何角度探索动态对象或角色。与此同时，视频生成模型因其能够生成逼真和富有想象力的帧而受到特别关注。这些模型也被观察到具有很强的3D一致性，表明它们有可能成为世界模拟器。在这项工作中，我们提出了Video4DGen，这是一个新颖的框架，擅长从单个或多个生成的视频中生成4D表示，以及生成4D引导视频。该框架对于创建保持空间和时间一致性的高保真虚拟内容至关重要。Video4DGen生成的4D输出使用我们提出的动态高斯曲面（DGS）表示，DGS优化了时变扭曲函数，将高斯曲面（曲面元素）从静态转换为动态扭曲状态。我们设计了高斯表面的扭曲状态几何正则化和细化，以保持结构的完整性和细粒度的外观细节。为了从多个视频中执行4D生成，并在空间、时间和姿势维度上捕获表示，我们设计了多视频对齐、根姿势优化和姿势引导帧采样策略。利用连续扭曲场还可以精确描绘每个视频帧的姿态、运动和变形。此外，为了提高观察所有相机姿态的整体保真度，Video4DGen在4D内容的指导下进行了新颖的视图视频生成，并使用所提出的置信度滤波DGS来提高生成序列的质量。凭借4D和视频生成的能力，Video4DGen为虚拟现实、动画等领域的应用提供了强大的工具。 et.al.|[2504.04153](http://arxiv.org/abs/2504.04153)|null|
|**2025-04-05**|**Multi-identity Human Image Animation with Structural Video Diffusion**|从单个图像生成人类视频，同时确保高视觉质量和精确控制是一项具有挑战性的任务，特别是在涉及多个人和与物体交互的复杂场景中。现有的方法虽然对单个人类案例有效，但往往无法处理复杂的多身份交互，因为它们很难将正确的人类外观和姿势条件配对，并对3D感知动态的分布进行建模。为了解决这些局限性，我们提出了结构化视频扩散，这是一种为生成逼真的多人视频而设计的新框架。我们的方法引入了两个核心创新：身份特定的嵌入，以保持个体之间的一致外观，以及一种结构学习机制，该机制结合了深度和表面法线线索来模拟人与物体的交互。此外，我们用25K个新视频扩展了现有的人类视频数据集，这些视频具有不同的多人和对象交互场景，为训练提供了坚实的基础。实验结果表明，结构化视频扩散在为多个主题生成逼真、连贯的视频方面表现出色，具有动态和丰富的交互，推进了以人为中心的视频生成状态。 et.al.|[2504.04126](http://arxiv.org/abs/2504.04126)|null|
|**2025-04-05**|**Can You Count to Nine? A Human Evaluation Benchmark for Counting Limits in Modern Text-to-Video Models**|生成模型推动了各种人工智能任务的重大进展，包括文本到视频生成，其中视频LDM和稳定视频扩散等模型可以从文本指令中生成逼真的电影级视频。尽管取得了这些进步，但当前的文本到视频模型在可靠地遵循人类命令方面仍然面临着根本性的挑战，特别是在遵守简单的数值约束方面。在这项工作中，我们提出了T2VCountBench，这是一个专门的基准，旨在评估截至2025年SOTA文本到视频模型的计数能力。我们的基准采用严格的人工评估来衡量生成对象的数量，涵盖了各种生成器，包括开源和商业模型。大量的实验表明，所有现有的模型都难以完成基本的数值任务，几乎总是无法生成对象数量为9或更少的视频。此外，我们的综合消融研究探讨了视频风格、时间动态和多语言输入等因素如何影响计数性能。我们还探索了快速细化技术，并证明将任务分解为更小的子任务并不容易缓解这些限制。我们的研究结果突出了当前文本到视频生成中的重要挑战，并为旨在提高对基本数值约束的遵守程度的未来研究提供了见解。 et.al.|[2504.04051](http://arxiv.org/abs/2504.04051)|null|
|**2025-04-05**|**DiTaiListener: Controllable High Fidelity Listener Video Generation with Diffusion**|为长时间的互动生成自然而微妙的听众动作仍然是一个悬而未决的问题。现有的方法通常依赖于低维运动代码来生成面部行为，然后进行逼真的渲染，这限制了视觉保真度和表达丰富性。为了应对这些挑战，我们引入了DiTaiListener，它由具有多模态条件的视频扩散模型提供支持。我们的方法首先使用DiTaiListener-Gen根据说话者的语音和面部动作生成听众反应的短片段。然后通过DiTaiListener Edit优化过渡帧，实现无缝过渡。具体来说，DiTaiListener Gen通过引入因果时间多模态适配器（CTM适配器）来处理说话者的听觉和视觉线索，从而使扩散变换器（DiT）适应听众头像生成的任务。CTM适配器将说话者的输入以因果方式集成到视频生成过程中，以确保听众的反应在时间上连贯。对于长格式视频生成，我们引入了DiTaiListener Edit，这是一种过渡细化视频到视频扩散模型。该模型将视频片段融合成平滑连续的视频，确保在合并DiTaiListener-Gen生成的短视频片段时面部表情和图像质量的时间一致性。从数量上讲，DiTaiListener在照片真实感（RealTalk上的FID为+73.8%）和运动表示（VICO上的FD度量为+6.1%）空间的基准数据集上都达到了最先进的性能。用户研究证实了DiTaiListener的卓越性能，该模型在反馈、多样性和平滑性方面具有明显的偏好，远远优于竞争对手。 et.al.|[2504.04010](http://arxiv.org/abs/2504.04010)|null|
|**2025-04-04**|**Model Reveals What to Cache: Profiling-Based Feature Reuse for Video Diffusion Models**|扩散模型的最新进展已经证明了其在视频生成方面的显著能力。然而，计算强度仍然是实际应用中的一个重大挑战。虽然已经提出了特征缓存来减轻扩散模型的计算负担，但现有的方法通常会忽视单个块的异构意义，导致次优重用和输出质量下降。为此，我们通过引入ProfilingDiT来解决这一差距，ProfilingDiT是一种新的自适应缓存策略，可以显式地解开前景和背景聚焦块。通过对扩散模型中注意力分布的系统分析，我们揭示了一个关键的观察结果：1）大多数层对前景或背景区域表现出一致的偏好。2） 预测噪声最初表现出较低的步间相似性，随着去噪的进行而稳定。这一发现激励我们制定一种选择性缓存策略，在有效缓存静态背景特征的同时，保留动态前景元素的完整计算。我们的方法大大减少了计算开销，同时保持了视觉保真度。大量实验表明，我们的框架实现了显著的加速（例如，Wan2.1的加速是2.01倍），同时在综合质量指标上保持了视觉保真度，为高效的视频生成建立了一种可行的方法。 et.al.|[2504.03140](http://arxiv.org/abs/2504.03140)|null|
|**2025-04-03**|**How I Warped Your Noise: a Temporally-Correlated Noise Prior for Diffusion Models**|视频编辑和生成方法通常依赖于预训练的基于图像的扩散模型。然而，在扩散过程中，对不保留视频后续帧中存在的相关性的基本噪声采样技术的依赖对结果的质量有害。这要么会产生高频闪烁，要么会产生不适合后处理的纹理粘滞伪影。考虑到这一点，我们提出了一种在噪声样本序列中保持时间相关性的新方法。这种方法通过一种新的噪声表示来实现，称为 $\int$-噪声（积分噪声），它将单个噪声样本重新解释为连续积分的噪声场：像素值不表示离散值，而是像素区域上潜在的无限分辨率噪声的积分。此外，我们提出了一种精心定制的传输方法，该方法使用$\int$-噪声在帧序列上准确地平流噪声样本，最大限度地提高不同帧之间的相关性，同时保持噪声特性。我们的结果表明，所提出的\\int$ -噪声可用于各种任务，如视频恢复、替代渲染和条件视频生成。看见https://warpyournoise.github.io/视频结果。 et.al.|[2504.03072](http://arxiv.org/abs/2504.03072)|null|
|**2025-04-03**|**Unified World Models: Coupling Video and Action Diffusion for Pretraining on Large Robotic Datasets**|模仿学习已成为构建多面手机器人的一种有前景的方法。然而，由于依赖于高质量的专家演示，对大型机器人基础模型进行大规模模仿学习仍然具有挑战性。同时，描绘各种环境和不同行为的大量视频数据很容易获得。这些数据提供了有关真实世界动态和代理环境交互的丰富信息来源。然而，由于缺乏大多数现代方法所需的动作注释，直接利用这些数据进行模仿学习已被证明是困难的。在这项工作中，我们提出了统一世界模型（UWM），这是一个允许利用视频和行动数据进行政策学习的框架。具体来说，UWM在统一的变换器架构中集成了动作扩散过程和视频扩散过程，其中独立的扩散时间步长控制着每种模态。我们证明，通过简单地控制每个扩散时间步长，UWM可以灵活地表示策略、正向动态、反向动态和视频生成器。通过模拟和现实世界的实验，我们表明：（1）UWM能够对具有动力学和动作预测的大规模多任务机器人数据集进行有效的预训练，从而产生比模仿学习更具普遍性和鲁棒性的策略，（2）UWM通过独立控制特定模态的扩散时间步长，自然地促进了从无动作视频数据中的学习，进一步提高了微调策略的性能。我们的研究结果表明，UWM在利用大型异构数据集进行可扩展机器人学习方面迈出了有前景的一步，并在模仿学习和世界建模的经常不同的范式之间实现了简单的统一。视频和代码可在https://weirdlabuw.github.io/uwm/. et.al.|[2504.02792](http://arxiv.org/abs/2504.02792)|null|

<p align=right>(<a href=#updated-on-20250408>back to top</a>)</p>

## 3D

|Publish Date|Title|Abstract|PDF|Code|
|---|---|---|---|---|
|**2025-04-07**|**DeclutterNeRF: Generative-Free 3D Scene Recovery for Occlusion Removal**|最近的新颖视图合成（NVS）技术，包括神经辐射场（NeRF）和3D高斯散斑（3DGS），极大地推进了具有高质量渲染和逼真细节恢复的3D场景重建。在保留场景细节的同时有效地消除遮挡可以进一步增强这些技术的鲁棒性和适用性。然而，现有的对象和遮挡去除方法主要依赖于生成先验，尽管填充了由此产生的洞，但会引入新的伪影和模糊。此外，用于评估遮挡去除方法的现有基准数据集缺乏现实的复杂性和视点变化。为了解决这些问题，我们引入了DeclutterSet，这是一个新的数据集，具有不同的场景，在前景、中景和背景上分布着明显的遮挡，在视点之间表现出大量的相对运动。我们进一步介绍了DeclutterNeRF，这是一种没有生成先验的咬合去除方法。DeclutterNeRF引入了可学习相机参数的联合多视图优化、遮挡退火正则化，并采用了可解释的随机结构相似性损失，确保从不完整图像中进行高质量、无伪影的重建。实验表明，在我们提出的DeclutterSet上，DeclutterNeRF的表现明显优于最先进的方法，为未来的研究奠定了坚实的基础。 et.al.|[2504.04679](http://arxiv.org/abs/2504.04679)|null|
|**2025-04-05**|**3R-GS: Best Practice in Optimizing Camera Poses Along with 3DGS**|3D高斯散点（3DGS）以其效率和质量彻底改变了神经渲染，但与许多新颖的视图合成方法一样，它在很大程度上依赖于运动结构（SfM）系统的精确相机姿态。尽管最近的SfM管道取得了令人印象深刻的进展，但如何同时进一步提高其在具有挑战性的条件下（例如无纹理场景）的鲁棒性能和相机参数估计的精度仍然是个问题。我们提出了3R-GS，这是一个3D高斯散布框架，通过联合优化来自大型重建先验MASt3R SfM的3D高斯和相机参数来弥合这一差距。我们注意到，天真地执行联合3D高斯和相机优化面临着两个挑战：对SfM初始化质量的敏感性，以及其有限的全局优化能力，导致次优重建结果。我们的3R-GS通过整合优化实践克服了这些问题，即使在相机配准不完美的情况下也能实现稳健的场景重建。大量实验表明，3R-GS提供了高质量的新颖视图合成和精确的相机姿态估计，同时保持了计算效率。项目页面：https://zsh523.github.io/3R-GS/ et.al.|[2504.04294](http://arxiv.org/abs/2504.04294)|null|
|**2025-04-04**|**WildGS-SLAM: Monocular Gaussian Splatting SLAM in Dynamic Environments**|我们介绍了WildGS SLAM，这是一个强大而高效的单目RGB SLAM系统，旨在通过利用不确定性感知几何映射来处理动态环境。与假设静态场景的传统SLAM系统不同，我们的方法集成了深度和不确定性信息，以提高存在运动物体时的跟踪、映射和渲染性能。我们引入了一个由浅层多层感知器和DINOv2特征预测的不确定性映射，以指导跟踪和映射过程中的动态对象去除。该不确定性图增强了密集束调整和高斯图优化，提高了重建精度。我们的系统在多个数据集上进行了评估，并演示了无伪影的视图合成。结果显示，与最先进的方法相比，WildGS SLAM在动态环境中具有卓越的性能。 et.al.|[2504.03886](http://arxiv.org/abs/2504.03886)|null|
|**2025-04-04**|**3D Scene Understanding Through Local Random Access Sequence Modeling**|从单个图像中理解3D场景是计算机视觉中的一个关键问题，在图形、增强现实和机器人技术中有许多下游应用。虽然基于扩散的建模方法显示出了希望，但它们往往难以保持对象和场景的一致性，尤其是在复杂的现实世界场景中。为了解决这些局限性，我们提出了一种称为局部随机访问序列（LRAS）建模的自回归生成方法，该方法使用局部补丁量化和随机序列生成。通过利用光流作为3D场景编辑的中间表示，我们的实验表明，LRAS实现了最先进的新颖视图合成和3D对象操纵功能。此外，我们通过对序列设计的简单修改，证明了我们的框架可以自然地扩展到自监督深度估计。通过在多个3D场景理解任务上实现强大的性能，LRAS为构建下一代3D视觉模型提供了一个统一有效的框架。 et.al.|[2504.03875](http://arxiv.org/abs/2504.03875)|null|
|**2025-04-04**|**NeRFlex: Resource-aware Real-time High-quality Rendering of Complex Scenes on Mobile Devices**|神经辐射场（NeRF）是一种基于神经网络的尖端技术，用于3D重建中的新型视图合成。然而，其巨大的计算需求给在移动设备上的部署带来了挑战。虽然基于网格的NeRF解决方案在移动平台上实现实时渲染方面显示出了潜力，但在渲染实际复杂场景时，它们往往无法提供高质量的重建。此外，由预先计算的中间结果引起的不可忽略的内存开销使它们的实际应用变得复杂。为了克服这些挑战，我们提出了NeRFlex，这是一个资源感知、高分辨率、实时的渲染框架，用于移动设备上的复杂场景。NeRFlex将移动NeRF渲染与多NeRF表示相结合，将场景分解为多个子场景，每个子场景由一个单独的NeRF网络表示。至关重要的是，NeRFlex认为内存和计算约束都是一级公民，并相应地重新设计了重建过程。NeRFlex首先设计了一个面向细节的分割模块，用于识别具有高频细节的子场景。对于每个NeRF网络，使用基于领域知识的轻量级分析器来准确地将配置映射到视觉质量和内存使用情况。基于这些见解和移动设备上的资源限制，NeRFlex提出了一种动态规划算法，可以有效地确定所有NeRF表示的配置，尽管原始决策问题具有NP难度。在真实世界的数据集和移动设备上进行的广泛实验表明，NeRFlex在商业移动设备上实现了实时、高质量的渲染。 et.al.|[2504.03415](http://arxiv.org/abs/2504.03415)|null|
|**2025-04-03**|**MD-ProjTex: Texturing 3D Shapes with Multi-Diffusion Projection**|我们介绍了MD ProjTex，这是一种使用预训练的文本到图像扩散模型为3D形状快速一致地生成文本引导纹理的方法。我们方法的核心是UV空间中的多视图一致性机制，它确保了不同视点之间的连贯纹理。具体来说，MD ProjTex在每个扩散步骤融合来自多个视图的噪声预测，并联合更新每个视图的去噪方向，以保持3D一致性。与依赖于优化或顺序视图合成的现有最先进的方法相比，MD-ProjTex在计算上更高效，并获得了更好的定量和定性结果。 et.al.|[2504.02762](http://arxiv.org/abs/2504.02762)|null|
|**2025-04-02**|**Diffusion-Guided Gaussian Splatting for Large-Scale Unconstrained 3D Reconstruction and Novel View Synthesis**|3D高斯散斑（3DGS）和神经辐射场（NeRF）的最新进展在实时3D重建和新颖的视图合成方面取得了令人印象深刻的结果。然而，这些方法在大规模、无约束的环境中很难实现，在这些环境中，稀疏和不均匀的输入覆盖、瞬态遮挡、外观可变性和不一致的相机设置会导致质量下降。我们提出了GS-Diff，一种由多视图扩散模型引导的新型3DGS框架，以解决这些局限性。通过生成以多视图输入为条件的伪观测值，我们的方法将受约束的3D重建问题转化为适定问题，即使在稀疏数据的情况下也能实现鲁棒优化。GS-Diff还集成了一些增强功能，包括外观嵌入、单目深度先验、动态对象建模、各向异性正则化和高级光栅化技术，以解决现实世界中的几何和光度挑战。在四个基准上的实验表明，GS-Diff始终以显著的优势优于最先进的基线。 et.al.|[2504.01960](http://arxiv.org/abs/2504.01960)|null|
|**2025-04-02**|**BOGausS: Better Optimized Gaussian Splatting**|3D高斯散斑（3DGS）为新颖的视图合成提出了一种有效的解决方案。它的框架提供了快速和高保真的渲染。虽然比神经辐射场（NeRF）等其他解决方案简单，但在不牺牲质量的情况下构建较小的模型仍然存在一些挑战。在这项研究中，我们对3DGS训练过程进行了仔细的分析，并提出了一种新的优化方法。我们的优化高斯散斑（BOGausS）解决方案能够生成比原始3DGS轻十倍的模型，而不会降低质量，从而与最新技术相比显著提高了高斯散斑的性能。 et.al.|[2504.01844](http://arxiv.org/abs/2504.01844)|null|
|**2025-04-02**|**FIORD: A Fisheye Indoor-Outdoor Dataset with LIDAR Ground Truth for 3D Scene Reconstruction and Benchmarking**|大规模3D场景重建和新型视图合成方法的发展主要依赖于包含窄视场（FoV）透视图像的数据集。虽然对小规模场景有效，但这些数据集需要大型图像集和广泛的运动结构（SfM）处理，限制了可扩展性。为了解决这个问题，我们引入了一个为场景重建任务量身定制的鱼眼图像数据集。使用双200度鱼眼镜头，我们的数据集提供了5个室内和5个室外场景的360度全覆盖。每个场景都有稀疏的SfM点云和精确的LIDAR衍生的密集点云，可以用作几何地面真实值，在遮挡和反射等具有挑战性的条件下实现稳健的基准测试。虽然基线实验侧重于香草高斯Splatting和基于NeRF的Nerfacto方法，但该数据集支持场景重建、新颖视图合成和基于图像的渲染的多种方法。 et.al.|[2504.01732](http://arxiv.org/abs/2504.01732)|null|
|**2025-04-02**|**FlowR: Flowing from Sparse to Dense 3D Reconstructions**|3D高斯飞溅技术能够以实时帧率实现高质量的新颖视图合成（NVS）。然而，随着我们偏离训练的观点，它的质量急剧下降。因此，需要密集的捕捉来满足某些应用程序的高质量期望，例如虚拟现实（VR）。然而，获得如此密集的捕获是非常费力和昂贵的。现有的工作已经探索了使用2D生成模型通过蒸馏或生成额外的训练视图来缓解这一要求。这些方法通常仅以少数参考输入视图为条件，因此没有充分利用可用的3D信息，导致生成结果不一致和重建伪影。为了解决这个问题，我们提出了一种多视图流匹配模型，该模型学习一个流，将可能稀疏重建的新视图渲染连接到我们期望密集重建的渲染。这使得能够用新颖的、生成的视图来增强场景捕获，以提高重建质量。我们的模型是在一个360万图像对的新数据集上训练的，可以在一个H100 GPU上以540x960分辨率（91K令牌）在一次前向传递中处理多达45个视图。我们的流水线在稀疏和密集视图场景中持续改进NVS，从而在多个广泛使用的NVS基准测试中实现比先前工作更高质量的重建。 et.al.|[2504.01647](http://arxiv.org/abs/2504.01647)|null|

<p align=right>(<a href=#updated-on-20250408>back to top</a>)</p>

## 3D Reconstruction

|Publish Date|Title|Abstract|PDF|Code|
|---|---|---|---|---|
|**2025-04-07**|**InteractVLM: 3D Interaction Reasoning from 2D Foundational Models**|我们介绍了InteractVLM，这是一种从单个野生图像中估计人体和物体上的3D接触点的新方法，可以在3D中实现精确的人体-物体联合重建。由于遮挡、深度模糊和物体形状变化很大，这很有挑战性。现有方法依赖于通过昂贵的运动捕捉系统或繁琐的手动标记收集的3D联系人注释，限制了可扩展性和通用性。为了克服这一点，InteractVLM利用了大型视觉语言模型（VLM）的广泛视觉知识，并利用有限的3D接触数据进行了微调。然而，直接应用这些模型并非易事，因为它们只在2D中推理，而人与物体的接触本质上是3D的。因此，我们引入了一种新的Render Localize Lift模块，该模块：（1）通过多视图渲染在2D空间中嵌入3D身体和物体表面，（2）训练一个新的多视图定位模型（MV-Loc）来推断2D中的接触，以及（3）将其提升到3D。此外，我们提出了一项名为语义人类接触估计的新任务，其中人类接触预测明确地以对象语义为条件，从而实现了更丰富的交互建模。InteractVLM优于现有的接触估计工作，也有助于从野外图像进行3D重建。代码和型号可在https://interactvlm.is.tue.mpg.de. et.al.|[2504.05303](http://arxiv.org/abs/2504.05303)|null|
|**2025-04-07**|**OCC-MLLM-CoT-Alpha: Towards Multi-stage Occlusion Recognition Based on Large Language Models via 3D-Aware Supervision and Chain-of-Thoughts Guidance**|在现有的大规模视觉语言多模态模型中，对遮挡对象的理解还没有得到很好的研究。当前最先进的多模态大型模型难以通过通用视觉编码器和监督学习策略在理解遮挡物体方面提供令人满意的结果。因此，我们提出了OCC MLLM CoT Alpha，这是一个集成了3D感知监督和思维链指导的多模态大型视觉语言框架。具体来说，（1）我们构建了一个由大型多模态视觉语言模型和3D重建专家模型组成的多模态大型视觉语言模型框架。（2） 通过监督和强化训练策略的组合来学习相应的多模态思维链，使多模态视觉语言模型能够在学习的多模态思想链指导下增强识别能力。（3） 构建了一个大规模的多模态思维链推理数据集，其中包含价值11万美元的手持遮挡对象样本。在评估中，所提出的方法表明，对于各种最先进模型的两种设置，决策得分分别提高了15.75%、15.30%、16.98%、14.62%和4.42%、3.63%、6.94%、10.70%。 et.al.|[2504.04781](http://arxiv.org/abs/2504.04781)|null|
|**2025-04-07**|**Dual Consistent Constraint via Disentangled Consistency and Complementarity for Multi-view Clustering**|多视图聚类可以从多个视图中探索共同的语义，近年来受到了越来越多的关注。然而，目前的方法侧重于表征中的学习一致性，忽视了每个视图的互补性在表征学习中的贡献。这一限制对多视图表示学习提出了重大挑战。本文提出了一种新的多视图聚类框架，该框架引入了一种解纠缠的变分自动编码器，将多视图分为共享和私有信息，即一致性和互补性信息。我们首先通过对比学习最大化不同观点之间的相互信息来学习信息丰富和一致的表示。此过程将忽略补充信息。然后，当试图在所有视图中寻求共享信息的一致性时，我们采用一致性推理约束来显式地利用互补信息。具体来说，我们使用每个视图的私有和共享信息进行内部重建，使用所有视图的共享信息进行交叉重建。双重一致性约束不仅能有效提高数据的表示质量，而且易于扩展到其他场景，特别是在复杂的多视图场景中。这可能是在统一的MVC理论框架中首次尝试使用双重一致约束。在训练过程中，一致性和互补性特征被联合优化。大量实验表明，我们的方法优于基线方法。 et.al.|[2504.04676](http://arxiv.org/abs/2504.04676)|null|
|**2025-04-06**|**Tool-as-Interface: Learning Robot Policies from Human Tool Usage through Imitation Learning**|工具的使用对于使机器人能够执行复杂的现实世界任务至关重要，利用人类工具使用数据可以帮助机器人教学。然而，现有的数据收集方法，如遥操作，速度慢，容易出现控制延迟，不适合动态任务。相比之下，人类直接使用工具执行任务的人类自然数据提供了高效且易于收集的自然、非结构化的交互。基于人类和机器人可以共享相同工具的认识，我们提出了一个框架，将工具使用知识从人类数据转移到机器人。使用两个RGB相机，我们的方法生成3D重建，应用高斯飞溅进行新颖的视图增强，采用分割模型提取与实施例无关的观察结果，并利用任务空间工具动作表示来训练视觉运动策略。我们在各种现实世界的任务中验证了我们的方法，包括舀取肉丸、翻锅、平衡酒瓶和其他复杂的任务。与使用远程操作数据训练的扩散策略相比，我们的方法实现了71%的平均成功率，并将数据收集时间缩短了77%，有些任务只能通过我们的框架来解决。与手持夹具相比，我们方法将数据收集时间缩短了41%。此外，我们的方法弥合了实施例之间的差距，提高了对相机视点和机器人配置变化的鲁棒性，并有效地跨对象和空间设置进行了推广。 et.al.|[2504.04612](http://arxiv.org/abs/2504.04612)|null|
|**2025-04-06**|**Thermoxels: a voxel-based method to generate simulation-ready 3D thermal models**|在欧盟，建筑物占能源使用量的42%和温室气体排放量的35%。由于到2050年，大多数现有建筑仍将使用，因此改造对减排至关重要。然而，目前的建筑评估方法主要依赖于定性热成像，这限制了数据驱动的节能决策。另一方面，使用有限元分析（FEA）的定量评估提供了精确的见解，但需要手动CAD设计，这既繁琐又容易出错。3D重建的最新进展，如神经辐射场（NeRF）和高斯散斑，能够从稀疏图像中进行精确的3D建模，但缺乏FEA所需的明确定义的体积和它们之间的界面。我们提出了Thermoxels，这是一种基于体素的新方法，能够从稀疏的RGB和热图像集生成兼容FEA的模型，包括几何和温度。使用成对的RGB和热图像作为输入，热像素将场景的几何体表示为一组包含颜色和温度信息的体素。优化后，使用一个简单的过程将热素模型转换为与有限元分析兼容的四面体网格。我们展示了Thermoxels生成3D场景的RGB+Thermal网格的能力，超越了其他最先进的方法。为了展示Thermoxels模型的实际应用，我们使用有限元分析进行了一个简单的热传导模拟，从Thermoxels热重建定义的初始状态实现了收敛。此外，我们将Thermoxels的图像合成能力与当前最先进的方法进行了比较，展示了具有竞争力的结果，并讨论了现有指标在评估网格质量方面的局限性。 et.al.|[2504.04448](http://arxiv.org/abs/2504.04448)|null|
|**2025-04-05**|**Interpretable Single-View 3D Gaussian Splatting using Unsupervised Hierarchical Disentangled Representation Learning**|高斯散斑（GS）最近在3D重建方面取得了重大进展，提供了快速渲染和高质量的结果。然而，现有的3DGS方法在理解底层3D语义方面存在挑战，这阻碍了模型的可控性和可解释性。为了解决这个问题，我们提出了一种可解释的单视图3DGS框架，称为3DisGS，通过分层解纠缠表示学习（DRL）来发现粗粒度和细粒度的3D语义。具体来说，该模型采用双分支架构，由点云初始化分支和三平面高斯生成分支组成，通过分离3D几何和视觉外观特征来实现粗粒度解纠缠。随后，通过基于DRL的编码器适配器进一步发现每种模态中的细粒度语义表示。据我们所知，这是第一项实现无监督可解释3DGS的工作。评估表明，我们的模型在保持高质量和快速重建的同时实现了3D解纠缠。 et.al.|[2504.04190](http://arxiv.org/abs/2504.04190)|null|
|**2025-04-04**|**HumanDreamer-X: Photorealistic Single-image Human Avatars Reconstruction via Gaussian Restoration**|单图像人体重建对于数字人体建模应用至关重要，但仍然是一项极具挑战性的任务。当前的方法依赖于生成模型来合成多视图图像，以用于后续的3D重建和动画。然而，从单个人体图像直接生成多个视图会受到几何不一致的影响，导致重建模型中出现肢体碎片或模糊等问题。为了解决这些局限性，我们引入了\textbf{HumanDreamer-X}，这是一个将多视图人类生成和重建集成到统一管道中的新框架，显著提高了重建3D模型的几何一致性和视觉保真度。在这个框架中，3D高斯散斑作为一种显式的3D表示，提供初始几何和外观优先级。在此基础上，\textbf{HumanFixer}经过训练，可以恢复3DGS渲染，从而保证照片级的真实感。此外，我们深入研究了多视图人类生成中与注意力机制相关的固有挑战，并提出了一种注意力调节策略，有效地提高了多视图中几何细节的一致性。实验结果表明，我们的方法显著提高了生成和重建PSNR质量指标，分别提高了16.45%和12.65%，实现了高达25.62 dB的PSNR，同时还显示了对野外数据的泛化能力以及对各种人类重建骨干模型的适用性。 et.al.|[2504.03536](http://arxiv.org/abs/2504.03536)|null|
|**2025-04-04**|**NeRFlex: Resource-aware Real-time High-quality Rendering of Complex Scenes on Mobile Devices**|神经辐射场（NeRF）是一种基于神经网络的尖端技术，用于3D重建中的新型视图合成。然而，其巨大的计算需求给在移动设备上的部署带来了挑战。虽然基于网格的NeRF解决方案在移动平台上实现实时渲染方面显示出了潜力，但在渲染实际复杂场景时，它们往往无法提供高质量的重建。此外，由预先计算的中间结果引起的不可忽略的内存开销使它们的实际应用变得复杂。为了克服这些挑战，我们提出了NeRFlex，这是一个资源感知、高分辨率、实时的渲染框架，用于移动设备上的复杂场景。NeRFlex将移动NeRF渲染与多NeRF表示相结合，将场景分解为多个子场景，每个子场景由一个单独的NeRF网络表示。至关重要的是，NeRFlex认为内存和计算约束都是一级公民，并相应地重新设计了重建过程。NeRFlex首先设计了一个面向细节的分割模块，用于识别具有高频细节的子场景。对于每个NeRF网络，使用基于领域知识的轻量级分析器来准确地将配置映射到视觉质量和内存使用情况。基于这些见解和移动设备上的资源限制，NeRFlex提出了一种动态规划算法，可以有效地确定所有NeRF表示的配置，尽管原始决策问题具有NP难度。在真实世界的数据集和移动设备上进行的广泛实验表明，NeRFlex在商业移动设备上实现了实时、高质量的渲染。 et.al.|[2504.03415](http://arxiv.org/abs/2504.03415)|null|
|**2025-04-03**|**Compressing 3D Gaussian Splatting by Noise-Substituted Vector Quantization**|3D高斯散点（3DGS）在3D重建中表现出了显著的有效性，通过实时辐射场渲染实现了高质量的结果。然而，一个关键的挑战是巨大的存储成本：重建单个场景通常需要数百万个高斯散点，每个散点由59个浮点参数表示，大约需要1~GB的内存。为了应对这一挑战，我们提出了一种压缩方法，通过构建单独的属性码本并仅存储离散的码索引。具体来说，我们采用噪声替代的矢量量化技术来联合训练码本和模型特征，确保梯度下降优化和参数离散化之间的一致性。我们的方法有效地降低了内存消耗（约45美元），同时在标准3D基准场景上保持了有竞争力的重建质量。不同码本大小的实验表明了压缩比和图像质量之间的权衡。此外，经过训练的压缩模型仍然与流行的3DGS查看器完全兼容，并能够实现更快的渲染速度，使其非常适合实际应用。 et.al.|[2504.03059](http://arxiv.org/abs/2504.03059)|null|
|**2025-04-03**|**MD-ProjTex: Texturing 3D Shapes with Multi-Diffusion Projection**|我们介绍了MD ProjTex，这是一种使用预训练的文本到图像扩散模型为3D形状快速一致地生成文本引导纹理的方法。我们方法的核心是UV空间中的多视图一致性机制，它确保了不同视点之间的连贯纹理。具体来说，MD ProjTex在每个扩散步骤融合来自多个视图的噪声预测，并联合更新每个视图的去噪方向，以保持3D一致性。与依赖于优化或顺序视图合成的现有最先进的方法相比，MD-ProjTex在计算上更高效，并获得了更好的定量和定性结果。 et.al.|[2504.02762](http://arxiv.org/abs/2504.02762)|null|

<p align=right>(<a href=#updated-on-20250408>back to top</a>)</p>

## Diffusion

|Publish Date|Title|Abstract|PDF|Code|
|---|---|---|---|---|
|**2025-04-07**|**CREA: A Collaborative Multi-Agent Framework for Creative Content Generation with Diffusion Models**|人工智能图像的创造力仍然是一个根本性的挑战，不仅需要生成视觉上引人注目的内容，还需要为图像添加新颖、富有表现力和艺术丰富的转换。与依赖于直接基于提示的修改的传统编辑任务不同，创意图像编辑需要一种自主、迭代的方法来平衡原创性、连贯性和艺术意图。为了解决这个问题，我们引入了CREA，这是一种模仿人类创作过程的新型多智能体协作框架。我们的框架利用了一个由专业人工智能代理组成的团队，他们动态协作，对图像进行概念化、生成、评论和增强。通过广泛的定性和定量评估，我们证明CREA在多样性、语义对齐和创造性转换方面明显优于最先进的方法。通过将创造力构建为一个动态的、能动的过程，CREA重新定义了人工智能与艺术的交叉点，为自主的人工智能驱动的艺术探索、生成设计和人类与人工智能的共同创造铺平了道路。据我们所知，这是第一部介绍创意编辑任务的作品。 et.al.|[2504.05306](http://arxiv.org/abs/2504.05306)|null|
|**2025-04-07**|**Gaussian Mixture Flow Matching Models**|扩散模型将去噪分布近似为高斯分布并预测其均值，而流匹配模型将高斯均值重新参数化为流速。然而，由于离散化误差，它们在几步采样中表现不佳，并且在无分类器引导（CFG）下往往会产生过饱和的颜色。为了解决这些局限性，我们提出了一种新的高斯混合流匹配（GMFlow）模型：GMFlow预测动态高斯混合（GM）参数，而不是预测平均值，以捕捉多模态流速分布，这可以通过KL散度损失来学习。我们证明了GMFlow推广了之前的扩散和流匹配模型，在这些模型中，单个高斯函数的学习具有 $L_2$ 的去噪损失。为了进行推理，我们推导出了GM-SDE/ODE求解器，该求解器利用解析去噪分布和速度场进行精确的几步采样。此外，我们引入了一种新的概率制导方案，该方案减轻了CFG的过饱和问题，提高了图像生成质量。大量实验表明，GMFlow在生成质量方面始终优于流匹配基线，在ImageNet 256×256上仅用6个采样步骤就实现了0.942的精度。 et.al.|[2504.05304](http://arxiv.org/abs/2504.05304)|null|
|**2025-04-07**|**Dimension-Free Convergence of Diffusion Models for Approximate Gaussian Mixtures**|扩散模型以其卓越的生成性能而闻名，特别是在通过迭代去噪生成高质量样本方面。虽然目前的理论表明，准确生成样本所需的去噪步骤数量应与数据维度呈线性关系，但这并不能反映广泛使用的算法（如去噪扩散概率模型（DDPM））的实际效率。本文研究了扩散模型在从复杂的高维分布中采样的有效性，高斯混合模型（GMM）可以很好地近似这些分布。对于这些分布，我们的主要结果表明，DDPM最多需要 $\widetilde{O}（1/\varepsilon）$迭代才能获得总变化（TV）距离的$\varepilon$精确分布，与环境维度$d$和组件数量$K$ 无关，最多可达对数因子。此外，该结果对评分估计误差仍然具有鲁棒性。这些发现强调了在高维环境中，考虑到GMM的普遍近似能力，扩散模型的显著有效性，并为它们的实际成功提供了理论见解。 et.al.|[2504.05300](http://arxiv.org/abs/2504.05300)|null|
|**2025-04-07**|**AnomalousNet: A Hybrid Approach with Attention U-Nets and Change Point Detection for Accurate Characterization of Anomalous Diffusion in Video Data**|异常扩散发生在各种系统中，包括细胞内的蛋白质运输、复杂栖息地中的动物运动、地下水中的污染物分散以及合成材料中的纳米粒子运动。根据粒子轨迹准确估计异常扩散指数和扩散系数对于区分亚扩散、超扩散或正常扩散状态至关重要。这些估计提供了对系统潜在动力学的更深入了解，有助于识别粒子行为和检测扩散状态的变化。然而，分析短而嘈杂的视频数据往往会产生不完整和异构的轨迹，这对传统的统计方法提出了重大挑战。我们介绍了一种数据驱动的方法，该方法集成了粒子跟踪、注意力U-Net架构和变化点检测算法来解决这些问题。这种方法不仅可以高精度地推断异常扩散参数，而且即使在存在噪声和有限时间分辨率的情况下，也可以识别不同状态之间的时间转换。我们的方法在第二次异常扩散（AnDi）挑战基准测试中表现出色，在视频任务的顶级提交中表现出色。 et.al.|[2504.05271](http://arxiv.org/abs/2504.05271)|null|
|**2025-04-07**|**Federated Learning for Medical Image Classification: A Comprehensive Benchmark**|联邦学习范式非常适合医学图像分析领域，因为它可以有效地应对孤立的多中心数据上的机器学习，同时保护参与方的隐私。然而，目前对联邦学习中优化算法的研究往往集中在有限的数据集和场景上，主要集中在自然图像上，在医学背景下的比较实验不足。在这项工作中，我们对医学成像背景下几种最先进的联邦学习算法进行了全面评估。我们在多个医学成像数据集上对使用各种联邦学习算法训练的分类模型进行了公平的比较。此外，我们评估了系统性能指标，如通信成本和计算效率，同时考虑了不同的联邦学习架构。我们的研究结果表明，医学成像数据集对当前的联邦学习优化算法构成了重大挑战。没有一种算法能在所有医学联合学习场景中始终如一地提供最佳性能，许多优化算法在应用于这些数据集时可能表现不佳。我们的实验为未来联合学习在医学成像环境中的研究和应用提供了基准和指导。此外，我们提出了一种高效且稳健的方法，该方法将使用去噪扩散概率模型的生成技术与标签平滑相结合，以增强数据集，广泛提高了联合学习在各种医学成像数据集的分类任务上的性能。我们的代码将在GitHub上发布，为未来的医学影像联合学习研究提供可靠和全面的基准。 et.al.|[2504.05238](http://arxiv.org/abs/2504.05238)|null|
|**2025-04-07**|**Universal Lymph Node Detection in Multiparametric MRI with Selective Augmentation**|多参数MRI（mpMRI）中淋巴结（LN）的稳健定位对于评估淋巴结病至关重要。放射科医生定期测量LN的大小，以区分良性和恶性淋巴结，这需要随后的癌症分期。确定尺寸是一项繁琐的任务，再加上LN在mpMRI中的不同外观，这使得它们的测量变得困难。此外，在繁忙的临床工作日，可能会错过较小且可能转移的淋巴结。为了缓解这些成像和工作流程问题，我们提出了一种管道，可以普遍检测体内的良性和转移性淋巴结，以便进行后续测量。最近提出的VFNet神经网络用于识别T2脂肪抑制和弥散加权成像（DWI）序列中的LN，这些序列由各种扫描仪通过各种检查协议采集。我们还使用了一种称为标签内LISA（ILL）的选择性增强技术，使模型在训练过程中看到的输入数据样本多样化，从而提高了其在评估阶段的鲁棒性。在4 FP/vol下，ILL的灵敏度为 $\sim$83\%，而没有ILL的敏感性为$\sim$80\%。与目前在mpMRI上评估的LN检测方法相比，我们在4 FP/vol下的灵敏度提高了$\sim$ 9\%。 et.al.|[2504.05196](http://arxiv.org/abs/2504.05196)|null|
|**2025-04-07**|**DDPM Score Matching and Distribution Learning**|分数估计是基于分数的生成模型（SGMs）的支柱，特别是去噪扩散概率模型（DDPMs）。该领域的一个关键结果表明，通过准确的分数估计，SGM可以从任何现实的数据分布中有效地生成样本（Chen等人，ICLR’23；Lee等人，ALT’23）。这种分布学习结果，其中学习到的分布隐含地是采样器输出的分布，并没有解释分数估计与参数和密度估计的经典任务之间的关系。本文介绍了一种将分数估计简化为这两项任务的框架，对统计和计算学习理论有各种影响：参数估计：Koehler等人（ICLR'23）证明，分数匹配变体对于实践中常见的多峰密度的参数估计在统计上效率低下。相比之下，我们证明在温和条件下，DDPM中的去噪分数匹配是渐近有效的。密度估计：通过将生成与分数估计联系起来，我们将现有的分数估计保证提升到 $（\epsilon，\delta）$-PAC密度估计，即一个函数，在除$\delta$-部分空间外的所有空间上近似$\epsilon$ 内的目标对数密度。我们基于Gatmiry等人（arXiv'24）的一个开放问题，为经典高斯位置混合模型提供了（i）用于密度估计的最小最大速率和（ii）准多项式PAC密度估计算法。分数估计的下限：我们的框架提供了第一种原则性方法来证明跨一般分布的分数估计的计算下限。作为应用，我们为一般高斯混合模型中的分数估计建立了密码下限，在概念上恢复了Song（NeurIPS'24）结果，并提出了他的关键开放问题。 et.al.|[2504.05161](http://arxiv.org/abs/2504.05161)|null|
|**2025-04-07**|**DA2Diff: Exploring Degradation-aware Adaptive Diffusion Priors for All-in-One Weather Restoration**|在恶劣天气条件下进行图像恢复是许多基于视觉的应用的关键任务。最近在统一模型中处理多种天气退化的一体化框架显示出了潜力。然而，不同天气条件下退化模式的多样性，以及现实世界退化的复杂性和多样性，对多种天气的消除构成了重大挑战。为了应对这些挑战，我们提出了一种创新的扩散范式，该范式具有感知退化的自适应先验，用于一体化天气恢复，称为DA2Diff。将CLIP应用于感知退化感知特性以实现更好的多天气恢复是一种新的探索。具体来说，我们部署了一组可学习的提示，通过CLIP空间中的提示图像相似性约束来捕获感知退化的表示。通过将雪/霾/雨图像与雪/霾/雨提示对齐，每个提示都会导致不同的天气退化特征。然后，通过设计的特定天气提示引导模块，将学习到的提示集成到扩散模型中，从而可以恢复多种天气类型。为了进一步提高对复杂天气退化的适应性，我们提出了一种动态专家选择调制器，该调制器采用动态天气感知路由器，为每个天气失真的图像灵活调度不同数量的恢复专家，使扩散模型能够自适应地恢复不同的退化。实验结果证实了DA2Diff在定量和定性评估方面优于最新技术。验收后将提供源代码。 et.al.|[2504.05135](http://arxiv.org/abs/2504.05135)|null|
|**2025-04-07**|**Kinetic study of compressible Rayleigh-Taylor instability with time-varying acceleration**|在实际应用中，瑞利-泰勒（RT）不稳定性通常出现在具有时变加速度的可压缩系统中。为了捕捉此类系统的复杂动力学，开发了一种双组分离散玻尔兹曼方法来系统地研究变加速度驱动的可压缩RT不稳定性。具体而言，系统分析了不同加速周期、振幅和相位的影响。模拟结果从三个关键角度进行解释：密度梯度，表征密度的空间变化；热力学非平衡强度，量化系统与局部热力学平衡的偏差；以及非平衡区域的分数，它捕捉到了非平衡行为的空间分布。值得注意的是，流体系统表现出丰富多样的动态模式，这是由多种相互竞争的物理机制相互作用引起的，包括时间依赖的加速、RT不稳定性、扩散和耗散效应。这些发现为复杂驾驶条件下可压缩RT不稳定性的演变和调节提供了更深入的见解。 et.al.|[2504.05128](http://arxiv.org/abs/2504.05128)|null|
|**2025-04-07**|**Morse Index Theorem for Sturm-Liouville Operators on the Real Line**|经典的Morse指数定理建立了Morse指数、表征线性自伴微分算子关键谱性质的负特征值数量和相应共轭点计数之间的基本联系。本文将这些基本结果推广到 $\mathbb{R}$ 上的Sturm-Liouville算子。特别是，对于自治拉格朗日系统，我们采用几何论证来推导莫尔斯指数的下限。作为具体应用，我们建立了一个检测梯度反应扩散系统中行波不稳定性的标准。 et.al.|[2504.05091](http://arxiv.org/abs/2504.05091)|null|

<p align=right>(<a href=#updated-on-20250408>back to top</a>)</p>

## NeRF

|Publish Date|Title|Abstract|PDF|Code|
|---|---|---|---|---|
|**2025-04-06**|**Dynamic Neural Field Modeling of Visual Contrast for Perceiving Incoherent Looming**|Amari的动态神经场（DNF）框架提供了一种受大脑启发的方法来模拟神经元群的平均激活。利用单一领域，DNF已成为机器人应用中低能耗隐约感知模块的有前景的基础。然而，之前的DNF方法在检测不连贯或不一致的迫在眉睫的特征方面面临着重大挑战，这些特征在现实世界场景中很常见，例如雨天的碰撞检测。果蝇和蝗虫视觉系统的见解表明，编码ON/OFF视觉对比在增强迫在眉睫的选择性方面起着至关重要的作用。此外，横向激发机制可能会改善织机敏感神经元对连贯和非连贯刺激的反应。这些共同为改进迫在眉睫的感知模型提供了宝贵的指导。基于这些生物学证据，我们通过结合on/OFF视觉对比度的建模来扩展之前的单场DNF框架，每个对比度都由一个专用的DNF控制。使用归一化高斯核对每个ON/OFF对比场内的横向激励进行公式化，并将其输出整合到求和字段中以生成碰撞警报。实验评估表明，所提出的模型有效地解决了非相干逼近检测的挑战，并且明显优于最先进的蝗虫启发模型。它在各种刺激下表现出了强大的性能，包括合成雨效应，突显了它在复杂、嘈杂的环境中，在视觉线索不一致的情况下，具有可靠的隐约感知的潜力。 et.al.|[2504.04551](http://arxiv.org/abs/2504.04551)|null|
|**2025-04-03**|**A Physics-Informed Meta-Learning Framework for the Continuous Solution of Parametric PDEs on Arbitrary Geometries**|在这项工作中，我们引入了隐式有限算子学习（iFOL），用于任意几何上偏微分方程（PDE）的连续和参数解。我们提出了一种基于物理信息的编解码器网络，以建立连续参数和解空间之间的映射。解码器通过利用以潜在或特征码为条件的隐式神经场网络来构建参数解场。实例特定代码是通过基于二阶元学习技术的PDE编码过程导出的。在训练和推理中，在PDE编码和解码过程中，物理信息损失函数被最小化。iFOL以能量或加权残差形式表示损失函数，并使用从标准数值PDE方法导出的离散残差对其进行评估。这种方法在训练和推理过程中都会导致离散残差的反向传播。iFOL具有几个关键特性：（1）其独特的损失公式消除了以前在PDE的条件神经场算子学习中使用的传统编码过程-解码流水线的需要；（2） 它不仅提供精确的参数和连续场，而且提供参数梯度的解，而不需要额外的损失项或灵敏度分析；（3） 它可以有效地捕捉溶液中的尖锐不连续性；（4）它消除了对几何和网格的约束，使其适用于任意几何和空间采样（零样本超分辨率能力）。我们批判性地评估了这些特征，并分析了网络在稳态和瞬态PDE中推广到看不见的样本的能力。所提出的方法的整体性能是有希望的，证明了它适用于计算力学中一系列具有挑战性的问题。 et.al.|[2504.02459](http://arxiv.org/abs/2504.02459)|null|
|**2025-04-01**|**Flow Matching on Lie Groups**|流匹配（FM）是一种最新的生成建模技术：我们的目标是学习如何从分布中采样{X}_1 $通过从某些分布中流动样本$\mathfrak{X}_0$很容易取样。关键技巧是，在$\mathfrak中对端点进行调节的同时，可以训练这个流场{X}_1$：给定终点，只需沿直线段移动到终点（Lipman等人，2022）。然而，直线段仅在欧几里德空间上定义良好。因此，Chen和Lipman（2023）将该方法推广到黎曼流形上的FM，用测地线或其谱近似代替线段。我们采取了另一种观点：我们通过用指数曲线代替线段来推广李群上的FM。这导致了许多矩阵李群的简单、内在和快速实现，因为所需的李群运算（积、逆、指数、对数）仅由相应的矩阵运算给出。然后，李群上的FM可用于生成建模，数据由特征集（在$\mathbb{R}^n$ 中）和姿势集（在某些李群中）组成，例如等变神经场的潜在码（Wessels等人，2025）。 et.al.|[2504.00494](http://arxiv.org/abs/2504.00494)|**[link](https://github.com/finnsherry/FlowMatching)**|
|**2025-03-29**|**NeuralGS: Bridging Neural Fields and 3D Gaussian Splatting for Compact 3D Representations**|3D高斯散点（3DGS）显示了卓越的质量和渲染速度，但有数百万的3D高斯分布和巨大的存储和传输成本。最近的3DGS压缩方法主要集中在压缩脚手架GS上，取得了令人印象深刻的性能，但增加了体素结构和复杂的编码和量化策略。在这篇论文中，我们的目标是开发一种简单而有效的方法，称为NeuralGS，它以另一种方式探索将原始3DGS压缩成紧凑的表示，而不需要体素结构和复杂的量化策略。我们的观察是，像NeRF这样的神经场可以用多层感知器（MLP）神经网络表示复杂的3D场景，只需要几兆字节。因此，NeuralGS有效地采用神经场表示来用MLP对3D高斯的属性进行编码，即使对于大规模场景，也只需要很小的存储空间。为了实现这一点，我们采用了一种聚类策略，并根据高斯的重要性得分作为拟合权重，为每个聚类用不同的微小MLP对高斯进行拟合。我们在多个数据集上进行实验，在不损害视觉质量的情况下实现了平均模型大小减少45倍。我们的方法在原始3DGS上的压缩性能与基于Scaffold GS的专用压缩方法相当，这表明了用神经场直接压缩原始3DGS的巨大潜力。 et.al.|[2503.23162](http://arxiv.org/abs/2503.23162)|null|
|**2025-03-27**|**Renormalization group analysis of noisy neural field**|大脑中的神经元在个体特性和与其他神经元的连接方面表现出极大的多样性。为了深入了解神经元多样性如何在大尺度上促进大脑动力学和功能，我们借鉴了复制方法的框架，该框架已成功应用于平衡统计力学中一大类具有淬灭噪声的问题。我们分析了Wilson Cowan模型的两个线性化版本，其随机系数在空间上是相关的。特别是：（A）神经元本身的性质是异质的，（B）它们的连接是各向异性的。在这两个模型中，淬火随机性的平均会产生额外的非线性。这些非线性在威尔逊重整化群的框架内进行了分析。我们发现，对于模型A，如果噪声的空间相关性随距离衰减，指数小于-2 $，则在大的空间尺度上，噪声的影响消失了。相比之下，对于模型B，只有当空间相关性以小于-1$ 的指数衰减时，噪声对神经元连接的影响才会消失。我们的计算还表明，在某些条件下，噪声的存在可能会在大尺度上产生类似行波的行为，尽管这一结果在微扰理论的高阶下是否仍然有效还有待观察。 et.al.|[2503.21605](http://arxiv.org/abs/2503.21605)|null|
|**2025-03-25**|**Thin-Shell-SfT: Fine-Grained Monocular Non-rigid 3D Surface Tracking with Neural Deformation Fields**|从单目RGB视频中重建高度可变形的表面（如布料）是一个具有挑战性的问题，没有任何解决方案可以提供一致和准确的细粒度表面细节恢复。为了解释环境的病态性，现有的方法使用具有统计、神经或物理先验的变形模型。它们还主要依赖于非自适应离散曲面表示（例如多边形网格），逐帧优化导致误差传播，并受到基于网格的可微渲染器梯度差的影响。因此，织物褶皱等精细表面细节往往无法以所需的精度恢复。针对这些局限性，我们提出了ThinShell SfT，这是一种用于非刚性3D跟踪的新方法，将表面表示为隐式和连续的时空神经场。我们采用基于基尔霍夫-洛夫模型的连续薄壳物理先验进行空间正则化，这与早期作品的离散化替代方案形成了鲜明对比。最后，我们利用3D高斯溅射将表面可微分地渲染到图像空间中，并根据合成原理分析优化变形。我们的薄壳SfT在定性和定量上都优于先前的工作，这要归功于我们的连续表面公式以及专门定制的模拟先验和表面诱导的3D高斯。请访问我们的项目页面https://4dqv.mpiinf.mpg.de/ThinShellSfT. et.al.|[2503.19976](http://arxiv.org/abs/2503.19976)|null|
|**2025-03-25**|**Decoupled Dynamics Framework with Neural Fields for 3D Spatio-temporal Prediction of Vehicle Collisions**|本研究提出了一种神经框架，通过独立建模全局刚体运动和局部结构变形来预测3D车辆碰撞动力学。与直接预测绝对位移的方法不同，这种方法明确地将车辆的整体平移和旋转与其结构变形分开。两个专门的网络构成了该框架的核心：一个基于四元数的刚性网络用于刚性运动，一个基于坐标的变形网络用于局部变形。通过独立处理根本不同的物理现象，所提出的架构实现了准确的预测，而不需要对每个组件进行单独的监督。该模型仅在10%的可用模拟数据上进行训练，其性能明显优于基线模型，包括单层感知器（MLP）和深度算子网络（DeepONet），预测误差降低了83%。广泛的验证表明，它对训练范围外的碰撞条件具有很强的泛化能力，即使在涉及极端速度和大冲击角度的严重冲击下，也能准确预测响应。此外，该框架成功地从低分辨率输入重建了高分辨率变形细节，而无需增加计算工作量。因此，所提出的方法为在复杂的碰撞场景中快速可靠地评估车辆安全提供了一种有效、计算高效的方法，大大减少了所需的模拟数据和时间，同时保持了预测的保真度。 et.al.|[2503.19712](http://arxiv.org/abs/2503.19712)|null|
|**2025-03-21**|**Towards Understanding the Benefits of Neural Network Parameterizations in Geophysical Inversions: A Study With Neural Fields**|在这项工作中，我们采用了神经场，它使用神经网络以测试时学习的方式将坐标映射到该坐标处的相应物理属性值。对于测试时学习方法，与需要使用训练数据集训练网络的传统方法相比，在反演过程中学习权重。首先展示了地震层析成像和直流电阻率反演中的合成示例结果。然后，我们对这两种情况下的神经网络权重的雅可比矩阵进行奇异值分解分析（SVD分析），以探索神经网络对恢复模型的影响。结果表明，测试时间学习方法可以消除恢复的地下物理性质模型中由测量和物理敏感性引起的不必要的伪影。因此，在某些情况下，与常规反演相比，NFs-Inv可以改善反演结果，例如恢复倾角或预测主要目标的边界。在SVD分析中，我们观察到左奇异向量中的相似模式，就像在计算机视觉中的生成任务中以监督方式训练的一些扩散模型中观察到的那样。这一观察结果提供了证据，表明神经网络结构中固有的隐式偏差在监督学习和测试时学习模型中很有用。这种隐式偏差有可能对地球物理反演中的模型恢复有用。 et.al.|[2503.17503](http://arxiv.org/abs/2503.17503)|null|
|**2025-03-19**|**GO-N3RDet: Geometry Optimized NeRF-enhanced 3D Object Detector**|我们提出了GO-N3RDet，这是一种通过神经辐射场增强的场景几何优化的多视图3D物体检测器。准确的3D对象检测的关键在于有效的体素表示。然而，由于遮挡和缺乏3D信息，从多视图2D图像构建3D特征具有挑战性。为了解决这个问题，我们引入了一种独特的3D位置信息嵌入体素优化机制来融合多视图特征。为了优先考虑目标区域的神经场重建，我们还为探测器的NeRF分支设计了一种双重重要性采样方案。我们还提出了一个不透明度优化模块，通过实施多视图一致性约束来进行精确的体素不透明度预测。此外，为了进一步提高跨多个视角的体素密度一致性，我们将射线距离作为加权因子，以最小化累积射线误差。我们独特的模块协同形成了一个端到端的神经模型，建立了基于NeRF的多视图3D检测的最新技术，并在ScanNet和ARKITCenes上进行了广泛的实验验证。代码将在以下网址提供https://github.com/ZechuanLi/GO-N3RDet. et.al.|[2503.15211](http://arxiv.org/abs/2503.15211)|null|
|**2025-03-14**|**NF-SLAM: Effective, Normalizing Flow-supported Neural Field representations for object-level visual SLAM in automotive applications**|我们提出了一种新颖的、仅限视觉的对象级SLAM框架，用于通过隐式符号距离函数表示3D形状的汽车应用。我们的主要创新包括通过归一化流网络增强标准神经表示。因此，通过仅具有16维潜码的紧凑网络，可以在特定类别的道路车辆上实现强大的表示能力。此外，通过对合成数据的比较实验证明，新提出的架构在仅存在稀疏和噪声数据的情况下表现出显著的性能改进。该模块嵌入到基于立体视觉的框架的后端，用于联合增量形状优化。损失函数由基于稀疏3D点的SDF损失、稀疏渲染损失和基于语义掩码的轮廓一致性项的组合给出。我们还利用语义信息来确定前端的关键点提取密度。最后，对真实世界数据的实验结果显示，与使用直接深度读数的替代框架相比，其性能准确可靠。所提出的方法仅在通过束调整获得的稀疏3D点上表现良好，即使在仅使用掩模一致性项的情况下，最终也能继续提供稳定的结果。 et.al.|[2503.11199](http://arxiv.org/abs/2503.11199)|null|

<p align=right>(<a href=#updated-on-20250408>back to top</a>)</p>

[contributors-shield]: https://img.shields.io/github/contributors/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[contributors-url]: https://github.com/Vincentqyw/cv-arxiv-daily/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[forks-url]: https://github.com/Vincentqyw/cv-arxiv-daily/network/members
[stars-shield]: https://img.shields.io/github/stars/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[stars-url]: https://github.com/Vincentqyw/cv-arxiv-daily/stargazers
[issues-shield]: https://img.shields.io/github/issues/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[issues-url]: https://github.com/Vincentqyw/cv-arxiv-daily/issues

