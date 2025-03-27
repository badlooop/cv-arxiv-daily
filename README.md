[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]

## Updated on 2025.03.27
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
|**2025-03-26**|**Free4D: Tuning-free 4D Scene Generation with Spatial-Temporal Consistency**|我们介绍了Free4D，这是一个新的无需调整的框架，用于从单个图像生成4D场景。现有的方法要么侧重于对象级生成，使场景级生成不可行，要么依赖于大规模多视图视频数据集进行昂贵的训练，由于4D场景数据的稀缺，泛化能力有限。相比之下，我们的关键见解是提取预训练的基础模型，以实现一致的4D场景表示，这提供了效率和可推广性等有前景的优势。1） 为了实现这一点，我们首先使用图像到视频扩散模型对输入图像进行动画处理，然后进行4D几何结构初始化。2） 为了将这种粗糙结构转化为时空一致的多视图视频，我们设计了一种自适应引导机制，该机制具有用于空间一致性的点引导去噪策略和用于时间一致性的新型潜在替换策略。3） 为了将这些生成的观测结果提升为一致的4D表示，我们提出了一种基于调制的改进方法，以减轻不一致性，同时充分利用生成的信息。由此产生的4D表示实现了实时、可控的渲染，标志着基于单幅图像的4D场景生成的重大进步。 et.al.|[2503.20785](http://arxiv.org/abs/2503.20785)|null|
|**2025-03-26**|**RecTable: Fast Modeling Tabular Data with Rectified Flow**|基于分数或扩散的模型生成高质量的表格数据，超越了基于GAN和基于VAE的模型。然而，这些方法需要大量的训练时间。本文介绍了RecTable，它使用整流流建模，应用于文本到图像生成和文本到视频生成。RecTable具有由几个堆叠的门控线性单元块组成的简单架构。此外，我们的训练策略也很简单，包括混合型噪声分布和logit正态时间步长分布。我们的实验表明，与几种最先进的扩散和基于分数的模型相比，RecTable在减少所需训练时间的同时实现了具有竞争力的性能。我们的代码可在https://github.com/fmp453/rectable. et.al.|[2503.20731](http://arxiv.org/abs/2503.20731)|null|
|**2025-03-26**|**AccidentSim: Generating Physically Realistic Vehicle Collision Videos from Real-World Accident Reports**|由于其罕见性和复杂性，为自动驾驶研究收集真实世界的车辆事故视频具有挑战性。虽然现有的驾驶视频生成方法可以生成视觉上逼真的视频，但它们往往无法提供物理上逼真的模拟，因为它们缺乏生成准确碰撞后轨迹的能力。本文介绍了AccidentSim，这是一种新的框架，通过提取和利用现实世界车辆事故报告中可用的物理线索和上下文信息来生成物理逼真的车辆碰撞视频。具体而言，AccidentSim利用可靠的物理模拟器从事故报告中的物理和上下文信息中复制碰撞后的车辆轨迹，并构建车辆碰撞轨迹数据集。然后，该数据集用于微调语言模型，使其能够响应用户提示，并根据用户描述预测各种驾驶场景中物理上一致的碰撞后轨迹。最后，我们使用神经辐射场（NeRF）来渲染高质量的背景，将它们与表现出物理真实轨迹的前景车辆合并，以生成车辆碰撞视频。实验结果表明，AccidentSim制作的视频在视觉和物理真实性方面都表现出色。 et.al.|[2503.20654](http://arxiv.org/abs/2503.20654)|null|
|**2025-03-26**|**GAIA-2: A Controllable Multi-View Generative World Model for Autonomous Driving**|生成模型为模拟复杂环境提供了一种可扩展和灵活的范式，但目前的方法在满足自动驾驶的特定领域要求方面存在不足，例如多智能体交互、细粒度控制和多摄像头一致性。我们介绍了GAIA-2，自主生成人工智能，这是一个潜在的扩散世界模型，将这些功能统一在一个生成框架内。GAIA-2支持基于丰富的结构化输入集的可控视频生成：自我车辆动力学、代理配置、环境因素和道路语义。它在地理位置不同的驾驶环境（英国、美国、德国）中生成高分辨率、时空一致的多摄像头视频。该模型集成了结构化条件反射和外部潜在嵌入（例如，来自专有驱动模型），以促进灵活和语义基础的场景合成。通过这种集成，GAIA-2能够对常见和罕见的驾驶场景进行可扩展的模拟，推动生成世界模型作为自主系统开发的核心工具的使用。视频可在https://wayve.ai/thinking/gaia-2. et.al.|[2503.20523](http://arxiv.org/abs/2503.20523)|null|
|**2025-03-26**|**VPO: Aligning Text-to-Video Generation Models with Prompt Optimization**|视频生成模型在文本到视频任务中取得了显著进展。这些模型通常在具有高度详细和精心制作的描述的文本视频对上进行训练，而推理过程中的真实世界用户输入通常简洁、模糊或结构不佳。这种差距使得快速优化对于生成高质量视频至关重要。当前的方法通常依赖于大型语言模型（LLM）通过上下文学习来细化提示，但存在几个局限性：它们可能会扭曲用户意图、遗漏关键细节或引入安全风险。此外，他们优化提示而不考虑对最终视频质量的影响，这可能会导致次优结果。为了解决这些问题，我们引入了VPO，这是一个基于三个核心原则优化提示的原则性框架：无害性、准确性和有用性。生成的提示忠实地保留了用户意图，更重要的是，提高了生成视频的安全性和质量。为了实现这一目标，VPO采用了两阶段优化方法。首先，我们基于安全和对齐原则构建并完善了一个监督微调（SFT）数据集。其次，我们引入了文本级和视频级反馈，以进一步优化具有偏好学习的SFT模型。我们广泛的实验表明，与基线方法相比，VPO显著提高了安全性、对齐和视频质量。此外，VPO在视频生成模型中表现出很强的泛化能力。此外，我们证明了VPO在视频生成模型上的表现优于RLHF方法，并与RLHF方法相结合，强调了VPO对对齐视频生成模型的有效性。我们的代码和数据可在以下网址公开获取https://github.com/thu-coai/VPO. et.al.|[2503.20491](http://arxiv.org/abs/2503.20491)|null|
|**2025-03-26**|**Wan: Open and Advanced Large-Scale Video Generative Models**|本报告介绍了Wan，这是一套全面而开放的视频基础模型，旨在突破视频生成的界限。基于主流的扩散变换器范式，Wan通过一系列创新在生成能力方面取得了重大进展，包括我们新颖的VAE、可扩展的预训练策略、大规模数据管理和自动化评估指标。这些贡献共同提高了模型的性能和多功能性。具体来说，Wan具有四个关键特征：领先性能：Wan的14B模型在包含数十亿张图像和视频的庞大数据集上训练，展示了视频生成相对于数据和模型大小的缩放规律。它在多个内部和外部基准测试中始终优于现有的开源模型以及最先进的商业解决方案，显示出明显而显著的性能优势。全面性：万提供了两个功能强大的模型，即1.3B和14B参数，分别用于效率和有效性。它还涵盖了多个下游应用程序，包括图像到视频、指令引导视频编辑和个人视频生成，最多包含八项任务。消费级效率：1.3B型号表现出卓越的资源效率，只需要8.19 GB VRAM，使其与各种消费级GPU兼容。开放性：我们开源了整个Wan系列，包括源代码和所有模型，旨在促进视频生成社区的发展。这种开放性旨在显著扩大行业视频制作的创意可能性，并为学术界提供高质量的视频基础模型。所有代码和型号均可在https://github.com/Wan-Video/Wan2.1. et.al.|[2503.20314](http://arxiv.org/abs/2503.20314)|null|
|**2025-03-26**|**EGVD: Event-Guided Video Diffusion Model for Physically Realistic Large-Motion Frame Interpolation**|由于帧之间的运动模糊性，在具有大运动的场景中的视频帧插值（VFI）仍然具有挑战性。虽然事件摄像机可以捕获高时间分辨率的运动信息，但现有的基于事件的VFI方法在有限的训练数据和复杂的运动模式下难以应对。在本文中，我们介绍了事件引导视频扩散模型（EGVD），这是一种新的框架，它利用了预训练的稳定视频扩散模型的强大先验以及来自事件相机的精确时间信息。我们的方法采用多模态运动条件生成器（MMCG），有效地整合RGB帧和事件信号来指导扩散过程，产生物理上逼真的中间帧。我们采用了一种选择性微调策略，在保留空间建模能力的同时，有效地整合了事件引导的时间信息。我们结合了受扩散建模最新进展启发的输入输出归一化技术，以提高不同噪声水平下的训练稳定性。为了提高泛化能力，我们构建了一个综合数据集，结合了不同场景中的真实和模拟事件数据。在真实和模拟数据集上进行的广泛实验表明，EGVD在处理大运动和具有挑战性的照明条件方面明显优于现有方法，在感知质量指标方面取得了实质性改善（Prophesee的LPIPS提高了27.4%，BSRGB提高了24.1%），同时保持了具有竞争力的保真度指标。代码和数据集可在以下网址获得：https://github.com/OpenImagingLab/EGVD. et.al.|[2503.20268](http://arxiv.org/abs/2503.20268)|null|
|**2025-03-26**|**Unconditional Priors Matter! Improving Conditional Generation of Fine-Tuned Diffusion Models**|无分类器引导（CFG）是训练条件扩散模型的基本技术。基于CFG的训练的常见做法是使用单个网络来学习条件和无条件噪声预测，条件训练的辍学率很小。然而，我们观察到，在训练中联合学习带宽有限的无条件噪声会导致无条件情况下的先验较差。更重要的是，这些糟糕的无条件噪声预测成为降低条件生成质量的严重原因。受大多数基于CFG的条件模型是通过微调具有更好无条件生成的基础模型来训练的这一事实的启发，我们首先证明，简单地用基础模型预测的噪声替换CFG中的无条件噪声可以显著改善条件生成。此外，我们表明，除了微调模型所训练的扩散模型之外，其他扩散模型也可以用于无条件噪声替换。我们通过一系列基于CFG的条件模型对我们的说法进行了实验验证，这些模型用于图像和视频生成，包括零-1到3、通用扩散、DiT、DynamiCrafter和InstructPix2Pix。 et.al.|[2503.20240](http://arxiv.org/abs/2503.20240)|null|
|**2025-03-26**|**Video Motion Graphs**|我们介绍了视频运动图，这是一个旨在生成逼真人体运动视频的系统。使用参考视频和音乐或运动标签等条件信号，该系统通过首先检索具有与条件匹配的手势的视频剪辑，然后生成插值帧以无缝连接剪辑边界来合成新视频。我们方法的核心是HMInterp，这是一种强大的视频帧插值（VFI）模型，即使在跳舞等复杂的运动场景中，也能实现不连续帧的无缝插值。HMInterp i）采用双分支插值方法，将用于人体骨架运动插值的运动扩散模型与用于最终帧生成的基于扩散的视频帧插值模型相结合。ii）采用条件渐进训练，有效利用身份强弱条件，如图像和姿势。这些设计确保了高视频纹理质量和精确的运动轨迹。结果表明，我们的视频运动图在多模态条件人体运动视频生成方面优于现有的基于生成和检索的方法。项目页面可以在以下网址找到https://h-liu1997.github.io/Video-Motion-Graphs/ et.al.|[2503.20218](http://arxiv.org/abs/2503.20218)|null|
|**2025-03-25**|**Zero-Shot Human-Object Interaction Synthesis with Multimodal Priors**|人机交互（HOI）合成对于从虚拟现实到机器人的各种应用都很重要。然而，由于其复杂性和高成本，获取3D HOI数据具有挑战性，将现有方法限制在训练数据集中对象类型和交互模式的狭隘多样性上。本文提出了一种新的零样本HOI合成框架，该框架不依赖于当前有限的3D HOI数据集上的端到端训练。我们方法的核心思想在于利用预先训练的多模态模型中广泛的HOI知识。给定文本描述，我们的系统首先使用图像或视频生成模型获得时间一致的2D HOI图像序列，然后将其提升到人类和物体姿态的3D HOI里程碑。我们采用预训练的人体姿态估计模型来提取人体姿态，并引入了一种可推广的类别级6-DoF估计方法来从2D HOI图像中获得物体姿态。我们的估计方法适用于从文本到三维模型或在线检索中获得的各种对象模板。基于物理的3D HOI运动学里程碑跟踪进一步应用于细化身体运动和物体姿势，从而产生更合理的HOI生成结果。实验结果表明，我们的方法能够生成具有物理真实性和语义多样性的开放词汇HOI。 et.al.|[2503.20118](http://arxiv.org/abs/2503.20118)|null|

<p align=right>(<a href=#updated-on-20250327>back to top</a>)</p>

## 3D

|Publish Date|Title|Abstract|PDF|Code|
|---|---|---|---|---|
|**2025-03-26**|**TC-GS: Tri-plane based compression for 3D Gaussian Splatting**|最近，3D高斯散斑（3DGS）已经成为新型视图合成的一个突出框架，提供了高保真度和快速渲染速度。然而，3DGS的大量数据及其属性阻碍了其实际应用，需要压缩技术来降低内存成本。然而，3DGS的无序形状导致压缩困难。为了将非结构化属性转化为规范分布，我们提出了一种结构良好的三平面来编码高斯属性，利用属性的分布进行压缩。为了利用相邻高斯分布之间的相关性，在从三平面解码高斯分布时使用了K近邻（KNN）。我们还引入高斯位置信息作为位置敏感解码器的先验。此外，我们引入了自适应小波损失，旨在随着迭代次数的增加，专注于高频细节。我们的方法在多个数据集的广泛实验中取得了与SOTA 3D高斯散斑压缩工作相当或超越的结果。代码发布于https://github.com/timwang2001/TC-GS. et.al.|[2503.20221](http://arxiv.org/abs/2503.20221)|null|
|**2025-03-26**|**EVolSplat: Efficient Volume-based Gaussian Splatting for Urban View Synthesis**|城市场景的新颖视图合成对于自动驾驶相关应用至关重要。现有的基于NeRF和3DGS的方法在实现照片级真实感渲染方面显示出有希望的结果，但需要缓慢的每场景优化。我们介绍了EVolSplat，这是一种用于城市场景的高效3D高斯散点模型，以前馈方式工作。与现有的前馈、像素对齐的3DGS方法不同，这些方法通常会遇到多视图不一致和重复内容等问题，我们的方法使用3D卷积网络预测统一体积内多个帧的3D高斯分布。这是通过用噪声深度预测初始化3D高斯分布，然后在3D空间中细化它们的几何属性，并基于2D纹理预测颜色来实现的。我们的模型还使用灵活的半球背景模型处理远景和天空。这使我们能够在实现实时渲染的同时进行快速的前馈重建。对KITTI-360和Waymo数据集的实验评估表明，与现有的基于前馈3DGS和NeRF的方法相比，我们的方法达到了最先进的质量。 et.al.|[2503.20168](http://arxiv.org/abs/2503.20168)|null|
|**2025-03-25**|**Learning Scene-Level Signed Directional Distance Function with Ellipsoidal Priors and Neural Residuals**|密集的几何环境表示对于自主移动机器人导航和探索至关重要。最近的工作表明，使用神经网络学习的占用率、带符号距离或辐射率的隐式连续表示在重建保真度、效率和可微性方面优于基于网格、点云和体素的显式离散表示。在这项工作中，我们探索了有符号距离的方向公式，称为有符号方向距离函数（SDDF）。与有符号距离函数（SDF）不同，与神经辐射场（NeRF）相似，SDDF具有位置和观察方向作为输入。与SDF类似，与NeRF不同，SDDF直接沿方向提供到观测表面的距离，而不是沿视图射线进行积分，从而实现了高效的视图合成。为了有效地学习和预测场景级SDDF，我们开发了一种结合显式椭圆先验和隐式神经残差的可微混合表示。这种方法使模型能够有效地处理障碍物边界周围的大距离不连续性，同时保持密集高保真预测的能力。我们表明，SDDF在重建精度和渲染效率方面与最先进的神经隐式场景模型具有竞争力，同时允许对机器人轨迹优化进行可微视图预测。 et.al.|[2503.20066](http://arxiv.org/abs/2503.20066)|null|
|**2025-03-25**|**Exploring Disentangled and Controllable Human Image Synthesis: From End-to-End to Stage-by-Stage**|在人类图像合成中实现精细可控性是计算机视觉领域的一个长期挑战。现有的方法主要集中在面部合成或近额体生成上，以一种解耦的方式同时控制视点、姿势、服装和身份等关键因素的能力有限。本文介绍了一种新的解纠缠和可控的人工合成任务，该任务在统一的框架内明确地分离和操纵这四个因素。我们首先开发了一个在MVHumanNet上训练的端到端生成模型，用于因素解纠缠。然而，MVHumanNet和野外数据之间的领域差距产生了不令人满意的尝试结果，促使人们探索虚拟试穿（VTON）数据集作为一种潜在的解决方案。通过实验，我们观察到，简单地将VTON数据集作为额外数据来训练端到端模型会降低性能，这主要是由于两个数据集之间的数据形式不一致，从而破坏了解纠缠过程。为了更好地利用这两个数据集，我们提出了一个分阶段的框架，将人体图像生成分解为三个连续的步骤：穿衣a姿势生成、后视图合成以及姿势和视图控制。这种结构化的管道可以在不同阶段更好地利用数据集，显著提高可控性和泛化能力，特别是在野外场景中。大量实验表明，我们的分阶段方法在视觉保真度和解纠缠质量方面都优于端到端模型，为现实世界的任务提供了可扩展的解决方案。项目页面上提供了其他演示：https://taited.github.io/discohuman-project/. et.al.|[2503.19486](http://arxiv.org/abs/2503.19486)|null|
|**2025-03-25**|**HoGS: Unified Near and Far Object Reconstruction via Homogeneous Gaussian Splatting**|新型视图合成最近取得了令人瞩目的进展，3D高斯散点（3DGS）提供了高效的训练时间和逼真的实时渲染。然而，对笛卡尔坐标的依赖限制了3DGS在远处物体上的性能，这对于重建无界的室外环境非常重要。我们发现，尽管3DGS管道非常简单，但使用齐次坐标（投影几何中的一个概念）显著提高了远处物体的渲染精度。因此，我们提出了将齐次坐标合并到3DGS框架中的齐次高斯散斑（HoGS），为增强远近物体提供了统一的表示。HoGS通过采用射影几何原理，有效地管理了广阔的空间位置和尺度，特别是在室外无界环境中。实验表明，HoGS显著提高了重建远处物体的准确性，同时保持了附近物体的高质量渲染，以及快速的训练速度和实时渲染能力。我们的实现可以在我们的项目页面上找到https://kh129.github.io/hogs/. et.al.|[2503.19232](http://arxiv.org/abs/2503.19232)|**[link](https://github.com/huntorochi/HoGS)**|
|**2025-03-24**|**RomanTex: Decoupling 3D-aware Rotary Positional Embedded Multi-Attention Network for Texture Synthesis**|为现有几何体绘制纹理是3D资产生成中一个关键但劳动密集型的过程。文本到图像（T2I）模型的最新进展导致了纹理生成的重大进展。大多数现有的研究通过首先使用图像扩散模型在2D空间中生成图像，然后进行纹理烘焙过程来实现UV纹理，从而完成这项任务。然而，由于生成的多视图图像之间的不一致性，这些方法往往难以产生高质量的纹理，从而导致接缝和重影伪影。相比之下，基于3D的纹理合成方法旨在解决这些不一致性，但它们往往忽略了2D扩散模型先验，使其难以应用于现实世界的对象。为了克服这些局限性，我们提出了RomanTex，这是一种基于多视图的纹理生成框架，通过我们新颖的3D感知旋转位置嵌入，将多注意力网络与底层3D表示相结合。此外，我们在多注意力块中加入了解耦特性，以增强模型在图像到纹理任务中的鲁棒性，从而实现语义正确的后视图合成。此外，我们引入了一种与几何相关的无分类器引导（CFG）机制，以进一步改善与几何和图像的对齐。定量和定性评估以及全面的用户研究表明，我们的方法在纹理质量和一致性方面取得了最先进的结果。 et.al.|[2503.19011](http://arxiv.org/abs/2503.19011)|null|
|**2025-03-24**|**NexusGS: Sparse View Synthesis with Epipolar Depth Priors in 3D Gaussian Splatting**|神经辐射场（NeRF）和3D高斯散斑（3DGS）使用来自密集间隔的相机视点的图像，显著提高了照片真实感的新颖视图合成。然而，由于监督有限，这些方法在少数拍摄场景中很难使用。在本文中，我们提出了NexusGS，这是一种基于3DGS的方法，通过将深度信息直接嵌入点云中，而不依赖于复杂的手动正则化，增强了稀疏视图图像的新颖视图合成。利用3DGS固有的极线几何，我们的方法引入了一种新的点云加密策略，该策略用密集的点云初始化3DGS，减少了点放置的随机性，同时防止了过平滑和过拟合。具体来说，NexusGS包括三个关键步骤：极性深度连接、流动弹性深度混合和流动过滤深度修剪。这些步骤利用光流和相机姿态来计算精确的深度图，同时减轻了通常与光流相关的不准确之处。通过整合极线深度先验，NexusGS确保了可靠的密集点云覆盖，并在稀疏视图条件下支持稳定的3DGS训练。实验表明，NexusGS显著提高了深度精度和渲染质量，远远超过了最先进的方法。此外，我们通过大幅提高竞争方法的性能来验证我们生成的点云的优越性。项目页面：https://usmizuki.github.io/NexusGS/. et.al.|[2503.18794](http://arxiv.org/abs/2503.18794)|null|
|**2025-03-24**|**Accenture-NVS1: A Novel View Synthesis Dataset**|本文介绍了ACC-NVS1，这是一个专门为机载和地面图像的新型视图合成研究而设计的专用数据集。ACC-NVS1的数据分别于2023年和2024年在德克萨斯州奥斯汀和宾夕法尼亚州匹兹堡收集。该系列包括从机载和地面摄像机拍摄的六个不同的现实世界场景，总共有148000张图像。ACC-NVS1解决了不同高度和瞬态物体等挑战。该数据集旨在补充现有数据集，为综合研究提供额外资源，而不是作为基准。 et.al.|[2503.18711](http://arxiv.org/abs/2503.18711)|null|
|**2025-03-24**|**Hardware-Rasterized Ray-Based Gaussian Splatting**|我们提出了一种用于基于光线的3D高斯散斑（RayGS）的新颖硬件光栅化渲染方法，为新颖的视图合成获得了快速和高质量的结果。我们的工作包含一个数学严谨和几何直观的推导，关于如何有效地估计渲染RayGS模型的所有相关量，这些模型是相对于标准硬件光栅化着色器构建的。我们的解决方案是第一个能够以足够高的帧率渲染RayGS模型，以支持虚拟现实和混合现实等对质量敏感的应用程序。我们的第二个贡献是通过解决在训练和测试期间渲染不同尺度时出现的MIP相关问题，实现了RayGS的无别名渲染。我们在不同的基准场景中展示了显著的性能提升，同时保留了RayGS最先进的外观质量。 et.al.|[2503.18682](http://arxiv.org/abs/2503.18682)|null|
|**2025-03-25**|**LookCloser: Frequency-aware Radiance Field for Tiny-Detail Scene**|人类通过跨越多个频率的信息来感知和理解周围的环境。在沉浸式场景中，人们自然地扫描他们的环境以掌握其整体结构，同时检查吸引他们注意力的物体的细节。然而，目前的NeRF框架主要侧重于对高频局部视图或具有低频信息的场景的广泛结构进行建模，这仅限于平衡两者。我们介绍了FA NeRF，这是一种用于视图合成的新型频率感知框架，可在单个NeRF模型中同时捕获整体场景结构和高清细节。为了实现这一目标，我们提出了一种3D频率量化方法，该方法分析场景的频率分布，实现频率感知渲染。我们的框架包含一个用于快速收敛和查询的频率网格，一个用于平衡不同频率内容特征的频率感知特征重新加权策略。大量实验表明，我们的方法在保留细节的同时，在建模整个场景方面明显优于现有方法。项目页面：https://coscatter.github.io/LookCloser/ et.al.|[2503.18513](http://arxiv.org/abs/2503.18513)|null|

<p align=right>(<a href=#updated-on-20250327>back to top</a>)</p>

## 3D Reconstruction

|Publish Date|Title|Abstract|PDF|Code|
|---|---|---|---|---|
|**2025-03-26**|**FB-4D: Spatial-Temporal Coherent Dynamic 3D Content Generation with Feature Banks**|随着扩散模型和3D生成技术的快速发展，动态3D内容生成已成为一个关键的研究领域。然而，实现具有强时空一致性的高保真4D（动态3D）生成仍然是一项具有挑战性的任务。受最近预训练扩散特征捕获丰富对应关系的发现的启发，我们提出了FB-4D，这是一种新的4D生成框架，集成了特征库机制，以增强生成帧中的空间和时间一致性。在FB-4D中，我们存储从先前帧中提取的特征，并将其融合到生成后续帧的过程中，确保跨时间和多个视图的特征一致。为了确保紧凑的表示，特征库通过提出的动态合并机制进行更新。利用这个特征库，我们首次证明通过多次自回归迭代生成额外的参考序列可以不断提高生成性能。实验结果表明，FB-4D在渲染质量、时空一致性和鲁棒性方面明显优于现有方法。它在很大程度上超越了所有无需调整的多视图生成方法，并实现了与基于训练的方法相当的性能。 et.al.|[2503.20784](http://arxiv.org/abs/2503.20784)|null|
|**2025-03-25**|**Thin-Shell-SfT: Fine-Grained Monocular Non-rigid 3D Surface Tracking with Neural Deformation Fields**|从单目RGB视频中重建高度可变形的表面（如布料）是一个具有挑战性的问题，没有任何解决方案可以提供一致和准确的细粒度表面细节恢复。为了解释环境的病态性，现有的方法使用具有统计、神经或物理先验的变形模型。它们还主要依赖于非自适应离散曲面表示（例如多边形网格），逐帧优化导致误差传播，并受到基于网格的可微渲染器梯度差的影响。因此，织物褶皱等精细表面细节往往无法以所需的精度恢复。针对这些局限性，我们提出了ThinShell SfT，这是一种用于非刚性3D跟踪的新方法，将表面表示为隐式和连续的时空神经场。我们采用基于基尔霍夫-洛夫模型的连续薄壳物理先验进行空间正则化，这与早期作品的离散化替代方案形成了鲜明对比。最后，我们利用3D高斯溅射将表面可微分地渲染到图像空间中，并根据合成原理分析优化变形。我们的薄壳SfT在定性和定量上都优于先前的工作，这要归功于我们的连续表面公式以及专门定制的模拟先验和表面诱导的3D高斯。请访问我们的项目页面https://4dqv.mpiinf.mpg.de/ThinShellSfT. et.al.|[2503.19976](http://arxiv.org/abs/2503.19976)|null|
|**2025-03-26**|**A Survey on Event-driven 3D Reconstruction: Development under Different Categories**|事件相机因其高时间分辨率、低延迟和高动态范围而越来越受到人们对3D重建的关注。它们异步捕获每像素的亮度变化，允许在快速运动和具有挑战性的照明条件下进行精确重建。在这项调查中，我们全面回顾了事件驱动的3D重建方法，包括立体、单眼和多模态系统。我们根据几何、基于学习和混合方法对最近的发展进行了进一步分类。还涵盖了新兴趋势，如神经辐射场和事件数据的3D高斯飞溅。相关作品按时间顺序排列，以说明该领域的创新和进步。为了支持未来的研究，我们还强调了数据集、实验、评估、事件表示等方面的关键研究差距和未来的研究方向。 et.al.|[2503.19753](http://arxiv.org/abs/2503.19753)|null|
|**2025-03-25**|**Wavelet-based Global-Local Interaction Network with Cross-Attention for Multi-View Diabetic Retinopathy Detection**|多视图糖尿病视网膜病变（DR）检测最近成为一种有前景的方法，可以解决单视图DR面临的不完全病变问题。然而，由于病变的大小和位置各不相同，它仍然具有挑战性。此外，现有的多视图DR方法通常会合并多个视图，而不考虑它们之间病变信息的相关性和冗余性。因此，我们提出了一种新方法来克服病变信息学习困难和多视图融合不足的挑战。具体来说，我们引入了一个双分支网络来获得局部病变特征及其全局相关性。小波变换的高频分量用于利用病变边缘信息，然后通过全局语义对其进行增强，以促进困难的病变学习。此外，我们提出了一种跨视图融合模块，以改进多视图融合并减少冗余。在大型公共数据集上的实验结果证明了我们方法的有效性。该代码是开源的https://github.com/HuYongting/WGLIN. et.al.|[2503.19329](http://arxiv.org/abs/2503.19329)|null|
|**2025-03-24**|**MonoInstance: Enhancing Monocular Priors via Multi-view Instance Alignment for Neural Rendering and Reconstruction**|单眼深度先验已被神经渲染广泛应用于基于多视图的任务，如3D重建和新颖的视图合成。然而，由于对每个视图的预测不一致，如何在多视图环境中更有效地利用单眼线索仍然是一个挑战。当前的方法不加选择地对待整个估计的深度图，并将其用作地面实况监督，而忽略了单目先验中固有的不准确性和交叉视图不一致性。为了解决这些问题，我们提出了MonoInstance，这是一种探索单眼深度不确定性的通用方法，为神经渲染和重建提供增强的几何先验。我们的关键见解在于将来自多个视图的每个分段实例深度对齐到一个共同的3D空间中，从而将单目深度的不确定性估计转化为噪声点云中的密度度量。对于深度先验不可靠的高不确定性区域，我们进一步引入了一个约束项，鼓励投影实例与附近视图上的相应实例掩码对齐。MonoInstance是一种多功能策略，可以无缝集成到各种多视图神经渲染框架中。我们的实验结果表明，MonoInstance在各种基准下显著提高了重建和新视图合成的性能。 et.al.|[2503.18363](http://arxiv.org/abs/2503.18363)|null|
|**2025-03-24**|**Surface-Aware Distilled 3D Semantic Features**|许多3D任务，如姿势对齐、动画、运动转移和3D重建，都依赖于建立3D形状之间的对应关系。最近，通过匹配预训练视觉模型的语义特征来应对这一挑战。然而，尽管这些特征很强大，但它们很难区分同一语义类的实例，例如“左手”和“右手”，这会导致大量的映射错误。为了解决这个问题，我们学习了一个对这些模糊性具有鲁棒性的表面感知嵌入空间。重要的是，我们的方法是自我监督的，只需要少量不成对的训练网格就可以在测试时推断出新的3D形状的特征。我们通过引入对比损失来实现这一点，该损失保留了从基础模型中提取的特征的语义内容，同时消除了形状表面相距甚远的特征的歧义。我们在对应匹配基准测试中观察到卓越的性能，并支持下游应用，包括零件分割、姿态对齐和运动转移。项目现场可在https://lukas.uzolas.com/SurfaceAware3DFeaturesSite. et.al.|[2503.18254](http://arxiv.org/abs/2503.18254)|null|
|**2025-03-23**|**MLLM-For3D: Adapting Multimodal Large Language Model for 3D Reasoning Segmentation**|推理分割旨在基于人类意图和空间推理对复杂场景中的目标对象进行分割。虽然最近的多模态大型语言模型（MLLM）已经证明了令人印象深刻的2D图像推理分割，但将这些功能应用于3D场景的探索仍然不足。在本文中，我们介绍了MLLM-For3D，这是一个简单而有效的框架，可以将知识从2D MLLMs转移到3D场景理解。具体来说，我们利用MLLM生成多视图伪分割掩模和相应的文本嵌入，然后将2D掩模投影到3D空间中，并将其与文本嵌入对齐。主要的挑战在于缺乏跨多个视图的3D上下文和空间一致性，导致模型产生幻觉，使不存在的对象无法一致地定位对象。用这种不相关的对象训练3D模型会导致性能下降。为了解决这个问题，我们引入了一种空间一致性策略，以强制分割掩模在3D空间中保持一致，有效地捕捉场景的几何形状。此外，我们开发了一种用于多模态语义对齐的查询令牌方法，实现了跨不同视图对同一对象的一致识别。对各种具有挑战性的室内场景基准的广泛评估表明，即使没有任何标记的3D训练数据，MLLM-For3D也优于现有的3D推理分割方法，有效地解释了用户意图，理解了3D场景，并对空间关系进行了推理。 et.al.|[2503.18135](http://arxiv.org/abs/2503.18135)|null|
|**2025-03-22**|**GaussianFocus: Constrained Attention Focus for 3D Gaussian Splatting**|3D重建和神经渲染的最新发展极大地推动了各种学术和工业领域中照片级逼真3D场景渲染的能力。3D高斯散点技术及其衍生技术集成了基于基元和体积表示的优点，以提供顶级渲染质量和效率。尽管取得了这些进步，但该方法往往会产生过度冗余的噪声高斯分布，过度适应每个训练视图，从而降低渲染质量。此外，虽然3D高斯散斑在小规模和以对象为中心的场景中表现出色，但它在更大场景中的应用受到视频内存有限、优化持续时间过长和视图外观可变等限制的阻碍。为了应对这些挑战，我们引入了GaussianFocus，这是一种创新的方法，它结合了补丁注意力算法来提高渲染质量，并实现了高斯约束策略来最小化冗余。此外，我们提出了一种针对大规模场景的细分重建策略，将它们划分为更小、可管理的块进行单独训练。我们的结果表明，GaussianFocus显著减少了不必要的高斯分布，提高了渲染质量，超越了现有的最新技术（SoTA）方法。此外，我们展示了我们的方法能够有效地管理和渲染大型场景，如城市环境，同时保持视觉输出的高保真度。 et.al.|[2503.17798](http://arxiv.org/abs/2503.17798)|null|
|**2025-03-22**|**3D Modeling: Camera Movement Estimation and path Correction for SFM Model using the Combination of Modified A-SIFT and Stereo System**|创建准确高效的3D模型带来了重大挑战，特别是在解决大视点变化、计算复杂性和对齐差异方面。高效的相机路径生成可以帮助解决这些问题。在此背景下，提出了一种仿射尺度不变特征变换（ASIFT）的改进版本，以减少计算开销的方式提取更多的匹配点，确保有足够数量的内层用于精确的相机旋转角度估计。此外，引入了一种新的基于双相机的旋转校正模型，以减轻小的旋转误差，进一步提高精度。此外，通过改变运动结构（SFM）模型，实现了基于立体相机的平移估计和校正模型，以确定3D空间中的相机运动。最后，ASIFT和基于两个相机的SFM模型的新颖组合提供了3D空间中精确的相机运动轨迹。实验结果表明，与实际相机运动路径相比，所提出的相机运动方法达到了99.9%的精度，并且优于最先进的相机路径估计方法。通过利用这种精确的相机路径，该系统有助于创建精确的3D模型，使其成为3D重建中需要高保真度和效率的应用的强大解决方案。 et.al.|[2503.17668](http://arxiv.org/abs/2503.17668)|null|
|**2025-03-21**|**Pow3R: Empowering Unconstrained 3D Reconstruction with Camera and Scene Priors**|我们提出了Pow3r，这是一种新型的大型3D视觉回归模型，在接受的输入模式方面具有高度的通用性。与之前缺乏在测试时利用已知相机或场景先验的任何机制的前馈模型不同，Pow3r在单个网络中结合了辅助信息的任何组合，如内部函数、相对姿态、密集或稀疏深度，以及输入图像。基于最新的DUSt3R范式，这是一种利用强大预训练的基于变换器的架构，我们的轻量级和多功能的调节为网络提供了额外的指导，以便在辅助信息可用时预测更准确的估计。在训练过程中，我们在每次迭代时向模型提供模态的随机子集，这使得模型能够在测试时在不同水平的已知先验下运行。这反过来又开辟了新的功能，例如以本机图像分辨率执行推理或点云完成。我们在3D重建、深度完成、多视图深度预测、多视图立体和多视图姿态估计任务上的实验产生了最先进的结果，并证实了Pow3r在利用所有可用信息方面的有效性。项目网页为https://europe.naverlabs.com/pow3r. et.al.|[2503.17316](http://arxiv.org/abs/2503.17316)|null|

<p align=right>(<a href=#updated-on-20250327>back to top</a>)</p>

## Diffusion

|Publish Date|Title|Abstract|PDF|Code|
|---|---|---|---|---|
|**2025-03-26**|**Free4D: Tuning-free 4D Scene Generation with Spatial-Temporal Consistency**|我们介绍了Free4D，这是一个新的无需调整的框架，用于从单个图像生成4D场景。现有的方法要么侧重于对象级生成，使场景级生成不可行，要么依赖于大规模多视图视频数据集进行昂贵的训练，由于4D场景数据的稀缺，泛化能力有限。相比之下，我们的关键见解是提取预训练的基础模型，以实现一致的4D场景表示，这提供了效率和可推广性等有前景的优势。1） 为了实现这一点，我们首先使用图像到视频扩散模型对输入图像进行动画处理，然后进行4D几何结构初始化。2） 为了将这种粗糙结构转化为时空一致的多视图视频，我们设计了一种自适应引导机制，该机制具有用于空间一致性的点引导去噪策略和用于时间一致性的新型潜在替换策略。3） 为了将这些生成的观测结果提升为一致的4D表示，我们提出了一种基于调制的改进方法，以减轻不一致性，同时充分利用生成的信息。由此产生的4D表示实现了实时、可控的渲染，标志着基于单幅图像的4D场景生成的重大进步。 et.al.|[2503.20785](http://arxiv.org/abs/2503.20785)|null|
|**2025-03-26**|**FB-4D: Spatial-Temporal Coherent Dynamic 3D Content Generation with Feature Banks**|随着扩散模型和3D生成技术的快速发展，动态3D内容生成已成为一个关键的研究领域。然而，实现具有强时空一致性的高保真4D（动态3D）生成仍然是一项具有挑战性的任务。受最近预训练扩散特征捕获丰富对应关系的发现的启发，我们提出了FB-4D，这是一种新的4D生成框架，集成了特征库机制，以增强生成帧中的空间和时间一致性。在FB-4D中，我们存储从先前帧中提取的特征，并将其融合到生成后续帧的过程中，确保跨时间和多个视图的特征一致。为了确保紧凑的表示，特征库通过提出的动态合并机制进行更新。利用这个特征库，我们首次证明通过多次自回归迭代生成额外的参考序列可以不断提高生成性能。实验结果表明，FB-4D在渲染质量、时空一致性和鲁棒性方面明显优于现有方法。它在很大程度上超越了所有无需调整的多视图生成方法，并实现了与基于训练的方法相当的性能。 et.al.|[2503.20784](http://arxiv.org/abs/2503.20784)|null|
|**2025-03-26**|**High Quality Diffusion Distillation on a Single GPU with Relative and Absolute Position Matching**|我们介绍了相对和绝对位置匹配（RAPM），这是一种扩散蒸馏方法，可以在单个GPU上高效训练高质量的生成。最近的扩散蒸馏研究在使用相一致性模型（PCM）和改进的分布匹配蒸馏（DMD2）等方法生成高分辨率文本到图像方面取得了优异的结果。然而，这些方法在训练过程中通常需要许多GPU（例如~8-64）和大量的批处理（例如~128-2048），导致内存和计算需求超出了一些研究人员的资源。RAPM提供有效的单GPU扩散蒸馏训练，批量为1。新方法试图通过匹配相对和绝对位置来模仿教师模型的采样轨迹。相对位置的设计灵感来自PCM。RAPM中相应地引入了两个鉴别器，一个用于匹配相对位置，另一个用于绝对位置。在StableDiffusion（SD）V1.5和SDXL上的实验结果表明，在非常有限的计算资源下，具有4个时间步长的RAPM产生的FID分数与具有1个时间步的最佳方法相当。 et.al.|[2503.20744](http://arxiv.org/abs/2503.20744)|null|
|**2025-03-26**|**RecTable: Fast Modeling Tabular Data with Rectified Flow**|基于分数或扩散的模型生成高质量的表格数据，超越了基于GAN和基于VAE的模型。然而，这些方法需要大量的训练时间。本文介绍了RecTable，它使用整流流建模，应用于文本到图像生成和文本到视频生成。RecTable具有由几个堆叠的门控线性单元块组成的简单架构。此外，我们的训练策略也很简单，包括混合型噪声分布和logit正态时间步长分布。我们的实验表明，与几种最先进的扩散和基于分数的模型相比，RecTable在减少所需训练时间的同时实现了具有竞争力的性能。我们的代码可在https://github.com/fmp453/rectable. et.al.|[2503.20731](http://arxiv.org/abs/2503.20731)|null|
|**2025-03-26**|**Dynamic Motion Blending for Versatile Motion Editing**|文本引导的运动编辑实现了超越传统关键帧动画的高级语义控制和迭代修改。现有的方法依赖于有限的预先收集的训练三元组，这严重阻碍了它们在各种编辑场景中的通用性。我们介绍了MotionCutMix，这是一种在线数据增强技术，通过基于输入文本混合身体部位运动来动态生成训练三元组。虽然MotionCoutMix有效地扩展了训练分布，但组合性质引入了更多的随机性和潜在的身体部位不协调。为了模拟如此丰富的分布，我们提出了MotionReFit，这是一个带有运动协调器的自回归扩散模型。自回归架构通过分解长序列来促进学习，而运动协调器则减轻了运动合成的伪影。我们的方法直接从高级人类指令处理空间和时间运动编辑，而不依赖于额外的规范或大型语言模型。通过广泛的实验，我们表明MotionReFit在文本引导的运动编辑中达到了最先进的性能。 et.al.|[2503.20724](http://arxiv.org/abs/2503.20724)|null|
|**2025-03-26**|**A weakly-supervised deep learning model for fast localisation and delineation of the skeleton, internal organs, and spinal canal on Whole-Body Diffusion-Weighted MRI (WB-DWI)**|背景：全身扩散加权MRI（WB-DWI）的表观扩散系数（ADC）值和总扩散体积（TDV）是公认的癌症成像生物标志物。然而，ADC和TDV测量的手动疾病描绘在临床实践中是不可行的，需要自动化。作为第一步，我们提出了一种算法来生成骨骼、相邻内脏器官（肝脏、脾脏、膀胱和肾脏）和椎管的快速和可重复的概率图。方法：我们开发了一种基于3D补丁的残差U-Net架构的自动深度学习管道，该管道在WB-DWI上定位和描绘这些解剖结构。该算法使用“软标签”（非二进制分割）进行训练，该标签来自计算密集型的基于图谱的方法。为了进行训练和验证，我们采用了一个多中心WB-DWI数据集，包括来自晚期前列腺癌症（APC）或多发性骨髓瘤（MM）患者的532次扫描，并对45名患者进行了测试。结果：我们的弱监督深度学习模型实现了骨骼轮廓的平均骰子得分/精确度/召回率为0.66/0.6/0.73，内脏器官为0.8/0.79/0.81，椎管为0.85/0.79/0.94，表面距离始终低于3 mm。自动和手动专家定义的全身轮廓之间的相对中值ADC和对数转换体积差异分别低于10%和4%。生成概率图的计算时间比基于图谱的配准算法快12倍（25秒对5分钟）。一位经验丰富的放射科医生在测试数据集上将模型的准确性评为“良好”或“优秀”。结论：我们的模型为在WB-DWI上定位和描绘身体区域提供了快速和可重复的概率图，实现了ADC和TDV的量化，可能为临床医生进行疾病分期和治疗反应评估提供支持。 et.al.|[2503.20722](http://arxiv.org/abs/2503.20722)|null|
|**2025-03-26**|**ARMO: Autoregressive Rigging for Multi-Category Objects**|大规模生成模型的最新进展显著提高了3D形状生成的质量和多样性。然而，大多数现有方法主要侧重于生成静态3D模型，忽略了某些形状（如类人、动物和昆虫）的潜在动态特性。为了解决这一差距，我们专注于装配，这是动画中的一项基本任务，为3D模型建立骨架结构和蒙皮。本文介绍了OmniRig，这是第一个大规模装配数据集，由79499个网格组成，具有详细的骨架和蒙皮信息。与依赖于预定义标准姿势（如A姿势、T姿势）的传统基准不同，我们的数据集包含了不同的形状类别、风格和姿势。利用这一丰富的数据集，我们提出了ARMO，这是一种新的装配框架，它利用自回归模型以统一的方式预测关节位置和连接关系。通过将骨架结构视为一个完整的图并将其离散化为标记，我们使用自动编码器对关节进行编码，以获得潜在的嵌入和自回归模型来预测标记。使用网格条件下的潜在扩散模型来预测条件骨架生成的潜在嵌入。我们的方法解决了基于回归的方法的局限性，这些方法经常受到误差累积和次优连通性估计的影响。通过在OmniRig数据集上进行广泛的实验，我们的方法在骨架预测方面取得了最先进的性能，证明了跨不同对象类别的泛化能力得到了提高。代码和数据集将在接受后公开供学术使用。 et.al.|[2503.20663](http://arxiv.org/abs/2503.20663)|null|
|**2025-03-26**|**MMGen: Unified Multi-modal Image Generation and Understanding in One Go**|用于多模态生成和理解的统一扩散框架具有实现无缝可控图像扩散和其他跨模态任务的变革潜力。在本文中，我们介绍了MMGen，这是一个将多个生成任务集成到单个扩散模型中的统一框架。这包括：（1）多模态类别条件生成，在给定类别信息的情况下，通过单个推理过程同时生成多模态输出；（2） 多模态视觉理解，从RGB图像中准确预测深度、表面法线和分割图；以及（3）多模态条件生成，其基于特定模态条件和其他对齐的模态生成相应的RGB图像。我们的方法开发了一种灵活支持多模态输出的新型扩散变换器，以及一种简单的模态解耦策略来统一各种任务。广泛的实验和应用证明了MMGen在不同任务和条件下的有效性和优越性，突出了其在需要同时生成和理解的应用中的潜力。 et.al.|[2503.20644](http://arxiv.org/abs/2503.20644)|null|
|**2025-03-26**|**Fast relaxation of a viscous vortex in an external flow**|我们研究了二维空间中由平滑、无发散速度场平流的集中涡旋的演变。在初始涡量为狄拉克质量的理想化情况下，我们计算了解的近似值，该近似值在高雷诺数范围内准确描述了涡流中心的运动和外部流动剪切应力下流线的变形。对于准备不充分的初始数据，对应于尖峰高斯涡旋，我们证明了由于涡旋核心内部耗散的增强，在比扩散时间短得多的时间尺度上对先前解的弛豫。 et.al.|[2503.20643](http://arxiv.org/abs/2503.20643)|null|
|**2025-03-26**|**Diffusion Counterfactuals for Image Regressors**|反事实解释已被成功应用于为各种黑匣子模型创建人类可解释的解释。它们对于图像领域的任务非常方便，在图像领域，解释的质量得益于生成模型的最新进展。尽管反事实解释已被广泛应用于分类模型，但它们在回归任务中的应用仍未得到充分探索。我们提出了两种方法，使用基于扩散的生成模型为图像回归任务创建反事实解释，以解决稀疏性和质量方面的挑战：1）一种基于直接在像素空间中操作的去噪扩散概率模型，2）另一种基于在潜在空间中运行的扩散自编码器。两者都在Celebra HQ和合成数据集上产生了现实、语义和平滑的反事实，为回归模型的决策过程提供了易于解释的见解，并揭示了虚假的相关性。我们发现，对于回归反事实，特征的变化取决于预测值的区域。预测值的显著变化需要较大的语义变化，因此比使用分类器更难找到稀疏的反事实。此外，像素空间反事实更稀疏，而潜在空间反事实质量更高，允许更大的语义变化。 et.al.|[2503.20595](http://arxiv.org/abs/2503.20595)|null|

<p align=right>(<a href=#updated-on-20250327>back to top</a>)</p>

## NeRF

|Publish Date|Title|Abstract|PDF|Code|
|---|---|---|---|---|
|**2025-03-25**|**Thin-Shell-SfT: Fine-Grained Monocular Non-rigid 3D Surface Tracking with Neural Deformation Fields**|从单目RGB视频中重建高度可变形的表面（如布料）是一个具有挑战性的问题，没有任何解决方案可以提供一致和准确的细粒度表面细节恢复。为了解释环境的病态性，现有的方法使用具有统计、神经或物理先验的变形模型。它们还主要依赖于非自适应离散曲面表示（例如多边形网格），逐帧优化导致误差传播，并受到基于网格的可微渲染器梯度差的影响。因此，织物褶皱等精细表面细节往往无法以所需的精度恢复。针对这些局限性，我们提出了ThinShell SfT，这是一种用于非刚性3D跟踪的新方法，将表面表示为隐式和连续的时空神经场。我们采用基于基尔霍夫-洛夫模型的连续薄壳物理先验进行空间正则化，这与早期作品的离散化替代方案形成了鲜明对比。最后，我们利用3D高斯溅射将表面可微分地渲染到图像空间中，并根据合成原理分析优化变形。我们的薄壳SfT在定性和定量上都优于先前的工作，这要归功于我们的连续表面公式以及专门定制的模拟先验和表面诱导的3D高斯。请访问我们的项目页面https://4dqv.mpiinf.mpg.de/ThinShellSfT. et.al.|[2503.19976](http://arxiv.org/abs/2503.19976)|null|
|**2025-03-25**|**Decoupled Dynamics Framework with Neural Fields for 3D Spatio-temporal Prediction of Vehicle Collisions**|本研究提出了一种神经框架，通过独立建模全局刚体运动和局部结构变形来预测3D车辆碰撞动力学。与直接预测绝对位移的方法不同，这种方法明确地将车辆的整体平移和旋转与其结构变形分开。两个专门的网络构成了该框架的核心：一个基于四元数的刚性网络用于刚性运动，一个基于坐标的变形网络用于局部变形。通过独立处理根本不同的物理现象，所提出的架构实现了准确的预测，而不需要对每个组件进行单独的监督。该模型仅在10%的可用模拟数据上进行训练，其性能明显优于基线模型，包括单层感知器（MLP）和深度算子网络（DeepONet），预测误差降低了83%。广泛的验证表明，它对训练范围外的碰撞条件具有很强的泛化能力，即使在涉及极端速度和大冲击角度的严重冲击下，也能准确预测响应。此外，该框架成功地从低分辨率输入重建了高分辨率变形细节，而无需增加计算工作量。因此，所提出的方法为在复杂的碰撞场景中快速可靠地评估车辆安全提供了一种有效、计算高效的方法，大大减少了所需的模拟数据和时间，同时保持了预测的保真度。 et.al.|[2503.19712](http://arxiv.org/abs/2503.19712)|null|
|**2025-03-21**|**Towards Understanding the Benefits of Neural Network Parameterizations in Geophysical Inversions: A Study With Neural Fields**|在这项工作中，我们采用了神经场，它使用神经网络以测试时学习的方式将坐标映射到该坐标处的相应物理属性值。对于测试时学习方法，与需要使用训练数据集训练网络的传统方法相比，在反演过程中学习权重。首先展示了地震层析成像和直流电阻率反演中的合成示例结果。然后，我们对这两种情况下的神经网络权重的雅可比矩阵进行奇异值分解分析（SVD分析），以探索神经网络对恢复模型的影响。结果表明，测试时间学习方法可以消除恢复的地下物理性质模型中由测量和物理敏感性引起的不必要的伪影。因此，在某些情况下，与常规反演相比，NFs-Inv可以改善反演结果，例如恢复倾角或预测主要目标的边界。在SVD分析中，我们观察到左奇异向量中的相似模式，就像在计算机视觉中的生成任务中以监督方式训练的一些扩散模型中观察到的那样。这一观察结果提供了证据，表明神经网络结构中固有的隐式偏差在监督学习和测试时学习模型中很有用。这种隐式偏差有可能对地球物理反演中的模型恢复有用。 et.al.|[2503.17503](http://arxiv.org/abs/2503.17503)|null|
|**2025-03-19**|**GO-N3RDet: Geometry Optimized NeRF-enhanced 3D Object Detector**|我们提出了GO-N3RDet，这是一种通过神经辐射场增强的场景几何优化的多视图3D物体检测器。准确的3D对象检测的关键在于有效的体素表示。然而，由于遮挡和缺乏3D信息，从多视图2D图像构建3D特征具有挑战性。为了解决这个问题，我们引入了一种独特的3D位置信息嵌入体素优化机制来融合多视图特征。为了优先考虑目标区域的神经场重建，我们还为探测器的NeRF分支设计了一种双重重要性采样方案。我们还提出了一个不透明度优化模块，通过实施多视图一致性约束来进行精确的体素不透明度预测。此外，为了进一步提高跨多个视角的体素密度一致性，我们将射线距离作为加权因子，以最小化累积射线误差。我们独特的模块协同形成了一个端到端的神经模型，建立了基于NeRF的多视图3D检测的最新技术，并在ScanNet和ARKITCenes上进行了广泛的实验验证。代码将在以下网址提供https://github.com/ZechuanLi/GO-N3RDet. et.al.|[2503.15211](http://arxiv.org/abs/2503.15211)|null|
|**2025-03-14**|**NF-SLAM: Effective, Normalizing Flow-supported Neural Field representations for object-level visual SLAM in automotive applications**|我们提出了一种新颖的、仅限视觉的对象级SLAM框架，用于通过隐式符号距离函数表示3D形状的汽车应用。我们的主要创新包括通过归一化流网络增强标准神经表示。因此，通过仅具有16维潜码的紧凑网络，可以在特定类别的道路车辆上实现强大的表示能力。此外，通过对合成数据的比较实验证明，新提出的架构在仅存在稀疏和噪声数据的情况下表现出显著的性能改进。该模块嵌入到基于立体视觉的框架的后端，用于联合增量形状优化。损失函数由基于稀疏3D点的SDF损失、稀疏渲染损失和基于语义掩码的轮廓一致性项的组合给出。我们还利用语义信息来确定前端的关键点提取密度。最后，对真实世界数据的实验结果显示，与使用直接深度读数的替代框架相比，其性能准确可靠。所提出的方法仅在通过束调整获得的稀疏3D点上表现良好，即使在仅使用掩模一致性项的情况下，最终也能继续提供稳定的结果。 et.al.|[2503.11199](http://arxiv.org/abs/2503.11199)|null|
|**2025-03-13**|**RSR-NF: Neural Field Regularization by Static Restoration Priors for Dynamic Imaging**|动态成像涉及使用欠采样测量值随时重建时空对象。特别是，在动态计算机断层扫描（dCT）中，一次只能获得一个视角的单个投影，这使得逆问题非常具有挑战性。此外，地面实况动态数据通常要么不可用，要么太稀缺，无法用于监督学习技术。为了解决这个问题，我们提出了RSR-NF，它使用神经场（NF）来表示动态对象，并使用去噪正则化（RED）框架，通过学习的恢复算子将额外的静态深空间先验合并到变分公式中。我们使用基于ADMM的可变分裂算法来有效地优化变分目标。我们将RSR-NF与三种替代方案进行了比较：仅具有时间正则化的NF；最近的一种方法，使用对静态数据进行预训练的去噪器，将部分可分离的低秩表示与RED相结合；以及基于深度图像先验的模型。第一个比较展示了通过将NF表示与静态恢复先验相结合所实现的重建改进，而另外两个则展示了与dCT的最新技术相比的改进。 et.al.|[2503.10015](http://arxiv.org/abs/2503.10015)|null|
|**2025-03-11**|**Representing 3D Shapes With 64 Latent Vectors for 3D Diffusion Models**|通过变分自编码器（VAE）构建压缩的潜在空间是高效3D扩散模型的关键。本文介绍了COD-VAE，这是一种在不牺牲质量的情况下将3D形状编码为1D潜在向量的COmpact集的VAE。COD-VAE引入了一种两级自动编码器方案，以提高压缩和解码效率。首先，我们的编码器块通过中间点补丁将点云逐步压缩为紧凑的潜在向量。其次，我们的基于三平面的解码器从潜在向量重建密集的三平面，而不是直接解码神经场，大大降低了神经场解码的计算开销。最后，我们提出了不确定性引导的令牌修剪，通过在更简单的区域跳过计算来自适应地分配资源，提高了解码器的效率。实验结果表明，与基线相比，COD-VAE在保持质量的同时实现了16倍的压缩。这使得生成速度提高了20.8倍，突显出大量潜在矢量不是高质量重建和生成的先决条件。 et.al.|[2503.08737](http://arxiv.org/abs/2503.08737)|null|
|**2025-03-09**|**Gaussian RBFNet: Gaussian Radial Basis Functions for Fast and Accurate Representation and Reconstruction of Neural Fields**|DeepSDF和神经辐射场等神经场最近彻底改变了RGB图像和视频的新颖视图合成和3D重建。然而，实现高质量的表示、重建和渲染需要深度神经网络，而深度神经网络的训练和评估速度很慢。尽管已经提出了几种加速技术，但它们经常以速度换取内存。另一方面，基于高斯飞溅的方法加快了渲染时间，但在存储大量高斯参数所需的训练速度和内存方面仍然成本高昂。在本文中，我们介绍了一种新的神经表示方法，它在训练和推理时间都很快，而且很轻。我们的关键观察是，传统MLP中使用的神经元执行简单的计算（点积，然后是ReLU激活），因此需要使用宽和深MLP或高分辨率和高维特征网格来参数化复杂的非线性函数。我们在这篇论文中表明，通过用径向基函数（RBF）核替换传统神经元，只需一层这样的神经元，就可以实现2D（RGB图像）、3D（几何）和5D（辐射场）信号的高精度表示。该表示具有高度的并行性，可在低分辨率特征网格上运行，并且结构紧凑，内存高效。我们证明，所提出的新表示可以在不到15秒的时间内训练出3D几何表示，在不到十五分钟的时间内就可以训练出新的视图合成。在运行时，它可以在不牺牲质量的情况下以超过60 fps的速度合成新颖的视图。 et.al.|[2503.06762](http://arxiv.org/abs/2503.06762)|null|
|**2025-03-09**|**X-LRM: X-ray Large Reconstruction Model for Extremely Sparse-View Computed Tomography Recovery in One Second**|稀疏视图3D CT重建旨在从有限数量的2D X射线投影中恢复体积结构。现有的前馈方法受到基于CNN的架构容量有限和大规模训练数据集稀缺的限制。本文提出了一种用于极稀疏视图（<10视图）CT重建的X射线大重建模型（X-LRM）。X-LRM由两个关键部件组成：X-former和X-triplane。我们的X-former可以使用基于MLP的图像标记器和基于Transformer的编码器来处理任意数量的输入视图。然后，输出标记被上采样到我们的X三平面表示中，该表示将3D辐射密度建模为隐式神经场。为了支持X-LRM的训练，我们引入了Torso-16K，这是一个由各种躯干器官的16K多个体积投影对组成的大规模数据集。大量实验表明，X-LRM的性能比最先进的方法高出1.5 dB，速度快27倍，灵活性更好。此外，肺部分割任务的下游评估也表明了我们方法的实用价值。我们的代码、预训练模型和数据集将于https://github.com/caiyuanhao1998/X-LRM et.al.|[2503.06382](http://arxiv.org/abs/2503.06382)|null|
|**2025-03-05**|**Distilling Dataset into Neural Field**|利用大规模数据集对于训练高性能深度学习模型至关重要，但它也带来了巨大的计算和存储成本。为了克服这些挑战，数据集蒸馏已成为一种有前景的解决方案，它将大规模数据集压缩成一个较小的合成数据集，保留了训练所需的基本信息。本文提出了一种新的数据集提取参数化框架，称为神经场提取数据集（DDiF），它利用神经场存储大规模数据集的必要信息。由于神经场以坐标作为输入和输出量的独特性质，DDiF有效地保留了信息，并易于生成各种形状的数据。我们从理论上证实，当单个合成实例的使用预算相同时，DDiF表现出比以前的一些文献更大的表现力。通过广泛的实验，我们证明DDiF在几个基准数据集上取得了卓越的性能，扩展到图像域之外，包括视频、音频和3D体素。我们在发布代码https://github.com/aailab-kaist/DDiF. et.al.|[2503.04835](http://arxiv.org/abs/2503.04835)|**[link](https://github.com/aailab-kaist/ddif)**|

<p align=right>(<a href=#updated-on-20250327>back to top</a>)</p>

[contributors-shield]: https://img.shields.io/github/contributors/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[contributors-url]: https://github.com/Vincentqyw/cv-arxiv-daily/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[forks-url]: https://github.com/Vincentqyw/cv-arxiv-daily/network/members
[stars-shield]: https://img.shields.io/github/stars/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[stars-url]: https://github.com/Vincentqyw/cv-arxiv-daily/stargazers
[issues-shield]: https://img.shields.io/github/issues/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[issues-url]: https://github.com/Vincentqyw/cv-arxiv-daily/issues

