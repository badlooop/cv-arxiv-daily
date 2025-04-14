[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]

## Updated on 2025.04.14
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
|**2025-04-10**|**Geo4D: Leveraging Video Generators for Geometric 4D Scene Reconstruction**|我们介绍了Geo4D，这是一种将视频扩散模型重新用于动态场景的单目3D重建的方法。通过利用这种视频模型捕获的强动态先验，可以仅使用合成数据来训练Geo4D，同时以零样本的方式将其很好地推广到真实数据。Geo4D预测了几种互补的几何形态，即点、深度和射线图。它使用一种新的多模态对齐算法在推理时对齐和融合这些模态以及多个滑动窗口，从而获得长视频的鲁棒和准确的4D重建。跨多个基准的广泛实验表明，Geo4D显著超越了最先进的视频深度估计方法，包括MonST3R等最新方法，这些方法也被设计用于处理动态场景。 et.al.|[2504.07961](http://arxiv.org/abs/2504.07961)|null|
|**2025-04-10**|**Beyond the Frame: Generating 360° Panoramic Videos from Perspective Videos**|360度视频已经成为代表我们动态视觉世界的有前景的媒介。与标准相机的“隧道视觉”相比，它们的无边界视野为我们的周围环境提供了更完整的视角。虽然现有的视频模型擅长制作标准视频，但它们生成完整全景视频的能力仍然难以捉摸。在本文中，我们研究了视频到360度生成的任务：给定一个透视视频作为输入，我们的目标是生成一个与原始视频一致的完整全景视频。与传统的视频生成任务不同，输出的视场要大得多，模型需要对场景的空间布局和对象的动态有深入的了解，以保持时空一致性。为了应对这些挑战，我们首先利用在线提供的丰富的360度视频，并开发一个高质量的数据过滤管道来管理成对训练数据。然后，我们仔细设计了一系列几何和运动感知操作，以促进学习过程并提高360度视频生成的质量。实验结果表明，我们的模型可以从野外视角视频中生成逼真连贯的360度视频。此外，我们还展示了它的潜在应用，包括视频稳定、相机视点控制和交互式视觉问答。 et.al.|[2504.07940](http://arxiv.org/abs/2504.07940)|null|
|**2025-04-10**|**Diffusion Transformers for Tabular Data Time Series Generation**|由于其不同的应用场景，表格数据生成最近引起了越来越多的兴趣。然而，生成表格数据的时间序列，其中序列的每个元素都依赖于其他元素，仍然是一个很大程度上未被探索的领域。这种差距可能是由于联合解决不同问题的困难造成的，其中主要是表格数据的异质性（非时间依赖方法常见的问题）和时间序列的可变长度。本文提出了一种基于扩散变换器（DiTs）的表格数据序列生成方法。受DiTs在图像和视频生成方面最近取得的成功的启发，我们扩展了这个框架来处理异构数据和可变长度序列。通过在六个数据集上进行广泛的实验，我们表明所提出的方法在很大程度上优于之前的工作。 et.al.|[2504.07566](http://arxiv.org/abs/2504.07566)|null|
|**2025-04-10**|**STeP: A General and Scalable Framework for Solving Video Inverse Problems with Spatiotemporal Diffusion Priors**|我们研究了如何使用扩散模型先验来解决涉及视频的一般贝叶斯逆问题。虽然希望在有效捕获复杂的时间关系之前使用视频扩散，但由于训练这种模型的计算和数据要求，先前的工作转而依赖于单帧上的图像扩散先验，并结合启发式方法来增强时间一致性。然而，这些方法难以忠实地恢复潜在的时间关系，特别是对于具有高时间不确定性的任务。在本文中，我们通过使用特定领域中的有限视频对预训练图像扩散模型中的潜在视频扩散模型进行微调，证明了实用且可访问的时空扩散先验的可行性。利用这种即插即用的时空扩散先验，我们引入了一种通用且可扩展的框架来解决视频逆问题。然后，我们将我们的框架应用于两个具有挑战性的科学视频逆问题——黑洞成像和动态MRI。我们的框架能够生成多样化、高保真的视频重建，不仅适合观测，还能恢复多模态解。通过引入时空扩散先验，我们显著提高了捕获数据中复杂时间关系的能力，同时也提高了空间保真度。 et.al.|[2504.07549](http://arxiv.org/abs/2504.07549)|null|
|**2025-04-09**|**EIDT-V: Exploiting Intersections in Diffusion Trajectories for Model-Agnostic, Zero-Shot, Training-Free Text-to-Video Generation**|零样本、无训练、基于图像的文本到视频生成是一个新兴领域，旨在使用现有的基于图像的扩散模型生成视频。该领域的当前方法需要对图像生成模型进行特定的架构更改，这限制了它们的适应性和可扩展性。与这些方法相比，我们提供了一种与模型无关的方法。我们在扩散轨迹中使用交点，只处理潜在值。仅通过轨迹的交点，我们无法获得局部的逐帧一致性和多样性。因此，我们转而使用基于网格的方法。上下文训练的LLM用于生成连贯的逐帧提示；另一个用于识别帧之间的差异。基于这些，我们获得了一个基于CLIP的注意力掩码，该掩码控制着每个网格单元的提示切换时间。较早的转换导致更高的方差，而较晚的转换导致更多的连贯性。因此，我们的方法可以确保帧的连贯性和方差之间的适当控制。我们的方法可实现最先进的性能，同时在处理各种图像生成模型时更加灵活。使用定量指标和用户研究的实证分析证实了我们的模型具有卓越的时间一致性、视觉保真度和用户满意度，从而为获得无训练、基于图像的文本到视频生成提供了一种新方法。 et.al.|[2504.06861](http://arxiv.org/abs/2504.06861)|null|
|**2025-04-09**|**DyDiT++: Dynamic Diffusion Transformers for Efficient Visual Generation**|扩散变换器（DiT）是一种新兴的视觉生成扩散模型，其性能优越，但计算成本高昂。我们的研究表明，这些成本主要源于\emph{静态}推理范式，它不可避免地在某些\emph{diffusion timestep}和\emph}空间区域引入了冗余计算。为了克服这种低效，我们提出\textbf{Dy}namic\textbf{Di}ffusion\textbf{T}ransformer（DyDiT）是一种架构，它可以沿emph{timestep}和emph{spatial}维度动态调整其计算。具体来说，我们引入了一种\ emph{时间步长动态宽度}（TDW）方法，该方法根据生成时间步长调整模型宽度。此外，我们设计了一种{Spatial wise Dynamic Token}（SDT）策略，以避免在不必要的空间位置进行冗余计算。TDW和SDT可以无缝集成到DiT中，大大加快了发电过程。在这些设计的基础上，我们在三个关键方面进一步增强了DyDiT。首先，DyDiT与基于流匹配的生成无缝集成，增强了其多功能性。此外，我们增强了DyDiT，以处理更复杂的视觉生成任务，包括视频生成和文本到图像生成，从而拓宽了其在现实世界中的应用。最后，为了解决完全微调和技术访问民主化的高成本问题，我们研究了以参数高效的方式训练DyDiT的可行性，并引入了基于时间步长的动态LoRA（TD-LoRA）。对不同视觉生成模型（包括DiT、SiT、Latte和FLUX）的广泛实验证明了DyDiT的有效性。 et.al.|[2504.06803](http://arxiv.org/abs/2504.06803)|null|
|**2025-04-09**|**RAGME: Retrieval Augmented Video Generation for Enhanced Motion Realism**|视频生成正在经历快速增长，这得益于扩散模型的进步以及更好、更大数据集的发展。然而，由于高维数据和任务的复杂性，制作高质量视频仍然具有挑战性。最近的努力主要集中在提高视觉质量和解决时间不一致性，如闪烁。尽管在这些领域取得了进展，但生成的视频在运动复杂性和物理合理性方面往往不足，许多输出要么看起来是静态的，要么表现出不切实际的运动。在这项工作中，我们提出了一个框架来提高生成视频中运动的真实感，探索了与现有文献的互补方向。具体来说，我们主张在生成阶段引入检索机制。检索到的视频充当接地信号，为模型提供物体如何移动的演示。我们的管道旨在应用于任何文本到视频的扩散模型，通过最小的微调对检索到的样本进行预训练模型的调节。我们通过既定的指标、最近提出的基准和定性结果展示了我们方法的优越性，并强调了该框架的其他应用。 et.al.|[2504.06672](http://arxiv.org/abs/2504.06672)|null|
|**2025-04-09**|**Patch Matters: Training-free Fine-grained Image Caption Enhancement via Local Perception**|高质量的图像字幕在提高跨模式应用程序的性能方面发挥着至关重要的作用，如文本到图像生成、文本到视频生成和文本图像检索。为了生成长格式、高质量的字幕，最近的许多研究都采用了多模态大语言模型（MLLM）。然而，目前的MLLM通常会产生缺乏细粒度细节的字幕或产生幻觉，这在开源和闭源模型中都是一个挑战。受特征整合理论的启发，该理论认为注意力必须集中在特定区域才能有效地整合视觉信息，我们提出了一种\textbf{分割然后聚合}策略。我们的方法首先将图像划分为语义和空间块，以提取细粒度的细节，增强模型对图像的局部感知。然后，这些局部细节被分层聚合，以生成全面的全局描述。为了解决生成的字幕中的幻觉和不一致问题，我们在层次聚合过程中应用了语义级过滤过程。这种无需训练的管道可以应用于开源模型（LLaVA-1.5、LLaVA-1.6、Mini Gemini）和闭源模型（Claude-3.5-Sonnet、GPT-4o、GLM-4V-Plus）。大量实验表明，我们的方法生成了更详细、更可靠的字幕，在不需要模型再训练的情况下推进了多模态描述生成。源代码可以在https://https://GeWu-Lab/Patch-Matters上找到 et.al.|[2504.06666](http://arxiv.org/abs/2504.06666)|null|
|**2025-04-08**|**CamContextI2V: Context-aware Controllable Video Generation**|最近，图像到视频（I2V）扩散模型已经证明了令人印象深刻的场景理解和生成质量，结合了图像条件来指导生成。然而，这些模型主要为静态图像制作动画，而不会超出其提供的上下文。引入额外的约束，如相机轨迹，可以增强多样性，但往往会降低视觉质量，限制了它们在需要忠实场景表示的任务中的适用性。我们提出了CamContextI2V，这是一种I2V模型，它将多种图像条件与3D约束以及相机控制相结合，以丰富全局语义和细粒度视觉细节。这使得视频生成更加连贯和上下文感知。此外，我们强调了时间意识对于有效语境表征的必要性。我们对RealEstate10K数据集的全面研究表明，视觉质量和相机可控性得到了改善。我们在以下网址公开我们的代码和模型：https://github.com/LDenninger/CamContextI2V. et.al.|[2504.06022](http://arxiv.org/abs/2504.06022)|null|
|**2025-04-07**|**One-Minute Video Generation with Test-Time Training**|今天的变形金刚仍然很难制作一分钟的视频，因为自我关注层在长时间的背景下效率低下。曼巴图层等替代方案难以处理复杂的多场景故事，因为它们的隐藏状态表现力较弱。我们尝试了测试时间训练（TTT）层，其隐藏状态本身可以是神经网络，因此更具表现力。将TTT层添加到预训练的Transformer中，使其能够从文本故事板生成一分钟的视频。为了验证概念，我们根据《猫和老鼠》漫画策划了一个数据集。与Mamba~2、门控DeltaNet和滑动窗口注意力层等基线相比，TTT层生成了更连贯的视频，讲述了复杂的故事，在每种方法100个视频的人类评估中领先34个Elo点。尽管有希望，但结果仍然包含伪影，这可能是由于预训练的5B模型的能力有限。我们的执行效率也可以提高。由于资源限制，我们只尝试了一分钟的视频，但这种方法可以扩展到更长的视频和更复杂的故事。示例视频、代码和注释可在以下网址获得：https://test-time-training.github.io/video-dit et.al.|[2504.05298](http://arxiv.org/abs/2504.05298)|null|

<p align=right>(<a href=#updated-on-20250414>back to top</a>)</p>

## 3D

|Publish Date|Title|Abstract|PDF|Code|
|---|---|---|---|---|
|**2025-04-10**|**InteractAvatar: Modeling Hand-Face Interaction in Photorealistic Avatars with Deformable Gaussians**|随着社区对数字化身的兴趣日益浓厚，加上表情和手势在交流中的重要性，在电话会议、游戏和AR/VR等许多行业中，对自然化身行为进行建模仍然是一个重要的挑战。人的手是与环境交互的主要工具，对于逼真的人类行为建模至关重要，但现有的3D手和头部化身模型往往忽视了手与身体交互的关键方面，例如手与脸之间的交互。我们提出了InteractitAvatar，这是第一个忠实地捕捉动态手和非刚性手-脸交互的照片级真实感外观的模型。我们的新型动态高斯手模型结合了模板模型和3D高斯散布以及动态细化模块，捕捉了姿势相关的变化，例如关节运动过程中出现的细皱纹和复杂阴影。重要的是，我们的人脸交互模块模拟了常见手势背后的微妙几何形状和外观动态。通过新颖的视图合成、自再现和跨身份再现实验，我们证明了InteractitAvatar可以从单目或多视点视频中重建手和手脸交互，具有高保真的细节，并可以用新颖的姿势进行动画制作。 et.al.|[2504.07949](http://arxiv.org/abs/2504.07949)|null|
|**2025-04-09**|**Glossy Object Reconstruction with Cost-effective Polarized Acquisition**|基于图像的光滑物体3D重建的挑战在于从捕获的图像中分离出光滑表面上的漫反射和镜面反射分量，这项任务因仅使用RGB数据识别照明条件和材质属性的模糊性而变得复杂。虽然最先进的方法依赖于定制和/或高端设备进行数据采集，这可能既麻烦又耗时，但这项工作引入了一种可扩展的极化辅助方法，该方法采用了具有成本效益的采集工具。通过将线性偏振器连接到现成的RGB相机上，可以捕获多视图偏振图像，而不需要预先校准或精确测量偏振器角度，从而大大降低了系统建设成本。所提出的方法将极化BRDF、斯托克斯矢量和物体表面的极化状态表示为神经隐式场。通过优化输入偏振图像的渲染损失，结合偏振器角度，可以恢复这些场。通过利用偏振渲染的隐式表示的基本物理原理，我们的方法通过在公共数据集和真实捕获的图像中进行重建和新视图合成的实验，证明了其优于现有技术。 et.al.|[2504.07025](http://arxiv.org/abs/2504.07025)|null|
|**2025-04-09**|**SVG-IR: Spatially-Varying Gaussian Splatting for Inverse Rendering**|由于其不适定特性，从图像重建3D资产（称为逆渲染（IR））仍然是一项具有挑战性的任务。3D高斯散斑（3DGS）在新的视图合成（NVS）任务中表现出了令人印象深刻的能力。方法通过将辐射分离为BRDF参数和照明来将其应用于重新照明，但由于每个高斯函数的能力有限，每个高斯函数具有恒定的材料参数和法线，并且没有间接照明的物理约束，因此会产生伪影和不自然的间接照明，从而产生较差的重新照明质量。在本文中，我们提出了一种称为空间维高斯逆渲染（SVG-IR）的新框架，旨在提高NVS和重新照明质量。为此，我们提出了一种新的表示空间变化高斯（SVG），它允许每高斯空间变化的参数。这种增强的表示方式由SVG飞溅方案补充，类似于传统图形管道中的顶点/片段着色。此外，我们整合了一个基于物理的间接照明模型，实现了更逼真的重新照明。所提出的SVG-IR框架显著提高了渲染质量，在峰值信噪比（PSNR）方面比最先进的基于NeRF的方法高出2.5 dB，在重新点亮任务方面比现有的基于高斯的技术高出3.5 dB，同时保持实时渲染速度。 et.al.|[2504.06815](http://arxiv.org/abs/2504.06815)|null|
|**2025-04-09**|**Collision avoidance from monocular vision trained with novel view synthesis**|碰撞避免可以在显式环境模型中进行检查，如高程图或占用网格，但将这些模型与运动策略集成需要准确的状态估计。在这项工作中，我们考虑了从隐式环境模型中避免碰撞的问题。我们使用单眼RGB图像作为输入，并从2D高斯飞溅生成的逼真图像中训练碰撞避免策略。我们在现实世界的实验中评估了在速度命令下产生的管道，该命令使机器人在有障碍物的拦截过程中。我们的研究结果表明，RGB图像足以在收集训练数据的房间和非分布环境中做出避免碰撞的决定。 et.al.|[2504.06651](http://arxiv.org/abs/2504.06651)|null|
|**2025-04-10**|**Stochastic Ray Tracing of 3D Transparent Gaussians**|3D高斯散点最近被广泛用作新颖的视图合成、重新照明和文本到3D生成任务的3D表示，通过一组带有不透明度和视图相关颜色的显式3D高斯分布，提供逼真和详细的结果。然而，许多透明图元的高效渲染仍然是一个重大挑战。现有的方法要么对3D高斯进行光栅化，按视图进行近似排序，要么依赖于高端RTX GPU来彻底处理所有光线高斯交点（通过网格边界高斯）。本文提出了一种随机光线追踪方法来渲染透明图元的3D云。与按顺序处理所有光线高斯交点不同，每条光线只穿过加速度结构一次，随机接受并着色单个交点（或使用简单扩展的N个交点）。这种方法最大限度地减少了着色时间，避免了沿光线对高斯分布进行排序，同时最大限度地降低了寄存器的使用率，即使在低端GPU上也最大限度地提高了并行性。穿过高斯资产的光线成本与标准网格相交光线的成本相当。虽然我们的方法引入了噪声，但阴影是无偏的，方差很小，因为随机接受度是基于累积不透明度进行重要抽样的。与蒙特卡洛哲学的一致性简化了实现，并很容易将我们的方法集成到传统的路径跟踪框架中。 et.al.|[2504.06598](http://arxiv.org/abs/2504.06598)|null|
|**2025-04-08**|**HiMoR: Monocular Deformable Gaussian Reconstruction with Hierarchical Motion Representation**|我们提出了分层运动表示（HiMoR），这是一种用于3D高斯基元的新型变形表示，能够实现高质量的单目动态3D重建。HiMoR背后的见解是，日常场景中的运动可以分解为更粗糙的运动，作为更精细细节的基础。使用树结构，HiMoR的节点表示不同级别的运动细节，较浅的节点对粗略运动进行建模以实现时间平滑，较深的节点捕获更精细的运动。此外，我们的模型使用一些共享的运动基来表示不同节点集的运动，这与运动趋于平滑和简单的假设相一致。这种运动表示设计为高斯模型提供了更结构化的变形，最大限度地利用时间关系来解决单目动态3D重建的挑战性任务。我们还建议使用更可靠的感知度量作为替代方案，因为用于评估单眼动态3D重建的像素级度量有时可能无法准确反映重建的真实质量。大量实验证明了我们的方法在从具有复杂运动的挑战性单眼视频中实现卓越的新颖视图合成方面的有效性。 et.al.|[2504.06210](http://arxiv.org/abs/2504.06210)|null|
|**2025-04-08**|**Meta-Continual Learning of Neural Fields**|神经场（NF）作为一种用于复杂数据表示的通用框架，已经获得了突出地位。这项工作揭示了一个新的问题设置，称为“神经场元连续学习”（MCL-NF），并引入了一种新的策略，该策略采用模块化架构与基于优化的元学习相结合。我们的策略侧重于克服现有神经场连续学习方法的局限性，如灾难性遗忘和缓慢收敛，实现了高质量的重建，显著提高了学习速度。我们进一步引入了神经辐射场的Fisher信息最大化损失（FIM-NeRF），它在样本级别最大化信息增益以增强学习泛化，并证明了收敛保证和泛化界限。我们在六个不同的数据集上对图像、音频、视频重建和视图合成任务进行了广泛的评估，证明了我们的方法在重建质量和速度方面优于现有的MCL和CL-NF方法。值得注意的是，我们的方法在降低参数要求的情况下，实现了神经场对城市级NeRF渲染的快速适应。 et.al.|[2504.05806](http://arxiv.org/abs/2504.05806)|null|
|**2025-04-07**|**DeclutterNeRF: Generative-Free 3D Scene Recovery for Occlusion Removal**|最近的新颖视图合成（NVS）技术，包括神经辐射场（NeRF）和3D高斯散斑（3DGS），极大地推进了具有高质量渲染和逼真细节恢复的3D场景重建。在保留场景细节的同时有效地消除遮挡可以进一步增强这些技术的鲁棒性和适用性。然而，现有的对象和遮挡去除方法主要依赖于生成先验，尽管填充了由此产生的洞，但会引入新的伪影和模糊。此外，用于评估遮挡去除方法的现有基准数据集缺乏现实的复杂性和视点变化。为了解决这些问题，我们引入了DeclutterSet，这是一个新的数据集，具有不同的场景，在前景、中景和背景上分布着明显的遮挡，在视点之间表现出大量的相对运动。我们进一步介绍了DeclutterNeRF，这是一种没有生成先验的咬合去除方法。DeclutterNeRF引入了可学习相机参数的联合多视图优化、遮挡退火正则化，并采用了可解释的随机结构相似性损失，确保从不完整图像中进行高质量、无伪影的重建。实验表明，在我们提出的DeclutterSet上，DeclutterNeRF的表现明显优于最先进的方法，为未来的研究奠定了坚实的基础。 et.al.|[2504.04679](http://arxiv.org/abs/2504.04679)|null|
|**2025-04-05**|**3R-GS: Best Practice in Optimizing Camera Poses Along with 3DGS**|3D高斯散点（3DGS）以其效率和质量彻底改变了神经渲染，但与许多新颖的视图合成方法一样，它在很大程度上依赖于运动结构（SfM）系统的精确相机姿态。尽管最近的SfM管道取得了令人印象深刻的进展，但如何同时进一步提高其在具有挑战性的条件下（例如无纹理场景）的鲁棒性能和相机参数估计的精度仍然是个问题。我们提出了3R-GS，这是一个3D高斯散布框架，通过联合优化来自大型重建先验MASt3R SfM的3D高斯和相机参数来弥合这一差距。我们注意到，天真地执行联合3D高斯和相机优化面临着两个挑战：对SfM初始化质量的敏感性，以及其有限的全局优化能力，导致次优重建结果。我们的3R-GS通过整合优化实践克服了这些问题，即使在相机配准不完美的情况下也能实现稳健的场景重建。大量实验表明，3R-GS提供了高质量的新颖视图合成和精确的相机姿态估计，同时保持了计算效率。项目页面：https://zsh523.github.io/3R-GS/ et.al.|[2504.04294](http://arxiv.org/abs/2504.04294)|null|
|**2025-04-04**|**WildGS-SLAM: Monocular Gaussian Splatting SLAM in Dynamic Environments**|我们介绍了WildGS SLAM，这是一个强大而高效的单目RGB SLAM系统，旨在通过利用不确定性感知几何映射来处理动态环境。与假设静态场景的传统SLAM系统不同，我们的方法集成了深度和不确定性信息，以提高存在运动物体时的跟踪、映射和渲染性能。我们引入了一个由浅层多层感知器和DINOv2特征预测的不确定性映射，以指导跟踪和映射过程中的动态对象去除。该不确定性图增强了密集束调整和高斯图优化，提高了重建精度。我们的系统在多个数据集上进行了评估，并演示了无伪影的视图合成。结果显示，与最先进的方法相比，WildGS SLAM在动态环境中具有卓越的性能。 et.al.|[2504.03886](http://arxiv.org/abs/2504.03886)|null|

<p align=right>(<a href=#updated-on-20250414>back to top</a>)</p>

## 3D Reconstruction

|Publish Date|Title|Abstract|PDF|Code|
|---|---|---|---|---|
|**2025-04-10**|**Geo4D: Leveraging Video Generators for Geometric 4D Scene Reconstruction**|我们介绍了Geo4D，这是一种将视频扩散模型重新用于动态场景的单目3D重建的方法。通过利用这种视频模型捕获的强动态先验，可以仅使用合成数据来训练Geo4D，同时以零样本的方式将其很好地推广到真实数据。Geo4D预测了几种互补的几何形态，即点、深度和射线图。它使用一种新的多模态对齐算法在推理时对齐和融合这些模态以及多个滑动窗口，从而获得长视频的鲁棒和准确的4D重建。跨多个基准的广泛实验表明，Geo4D显著超越了最先进的视频深度估计方法，包括MonST3R等最新方法，这些方法也被设计用于处理动态场景。 et.al.|[2504.07961](http://arxiv.org/abs/2504.07961)|null|
|**2025-04-10**|**V2V3D: View-to-View Denoised 3D Reconstruction for Light-Field Microscopy**|光场显微镜（LFM）因其能够捕获基于快照的大规模3D荧光图像而受到广泛关注。然而，现有的LFM重建算法对传感器噪声高度敏感，或者需要难以获得的地面实况注释数据进行训练。为了应对这些挑战，本文介绍了V2V3D，这是一种基于view2view的无监督框架，为在统一架构中联合优化图像去噪和3D重建建立了一种新的范式。我们假设LF图像来自一致的3D信号，每个视图中的噪声是独立的。这使得V2V3D能够结合noise2-noise原理进行有效的去噪。为了增强高频细节的恢复，我们提出了一种新的基于波动光学的特征对齐技术，该技术将用于波动光学中前向传播的点扩散函数转换为专门为特征对齐设计的卷积核。此外，我们引入了一个LFM数据集，其中包含LF图像及其相应的3D强度体积。大量实验表明，我们的方法实现了高计算效率，并优于其他最先进的方法。这些进步使V2V3D成为在具有挑战性的条件下进行3D成像的有前景的解决方案。 et.al.|[2504.07853](http://arxiv.org/abs/2504.07853)|null|
|**2025-04-10**|**Adversarial Subspace Generation for Outlier Detection in High-Dimensional Data**|高维表格数据中的异常检测具有挑战性，因为数据通常分布在多个低维子空间中，这种现象被称为多视图效应（MV）。这种效应导致了大量研究集中在挖掘这样的子空间上，即子空间选择。然而，由于对MV效应的精确性质没有很好的理解，传统方法不得不依赖启发式驱动的搜索方案，这些方案难以准确捕捉数据的真实结构。正确识别这些子空间对于无监督任务（如异常值检测或聚类）至关重要，在这些任务中，歪曲底层数据结构可能会阻碍性能。我们引入了近视子空间理论（MST），这是一个新的理论框架，从数学上阐述了多视图效应，并将子空间选择写为随机优化问题。基于MST，我们引入了V-GAN，这是一种经过训练的生成方法来解决此类优化问题。这种方法避免了在特征空间上进行任何穷举搜索，同时确保保留了固有的数据结构。在42个真实世界数据集上的实验表明，与现有的子空间选择、特征选择和嵌入方法相比，使用V-GAN子空间构建集成方法可以显著提高单类分类性能。对合成数据的进一步实验表明，V-GAN比其他相关子空间选择方法更准确地识别子空间，同时缩放效果更好。这些结果证实了我们方法的理论保证，也突显了它在高维环境中的实际可行性。 et.al.|[2504.07522](http://arxiv.org/abs/2504.07522)|**[link](https://github.com/jcribeiro98/v-gan)**|
|**2025-04-09**|**Adaptive Vision-Guided Robotic Arm Control for Precision Pruning in Dynamic Orchard Environments**|本研究提出了一种用于自动果树修剪应用的视觉引导机器人控制系统。传统农业实践依赖于缺乏可扩展性和效率的劳动密集型任务和流程，迫切需要自动化研究来满足对更高作物产量、可扩展操作和减少体力劳动的日益增长的需求。为此，本文提出了一种新的算法，用于在密集果园中进行鲁棒和自动的水果修剪。所提出的算法利用了CoTracker，该算法旨在以显著的鲁棒性和准确性跟踪视频序列中的2D特征点，同时利用联合注意力机制来解释点间的依赖关系，从而在具有挑战性和复杂的条件下实现鲁棒性和精确的跟踪。为了验证CoTracker的有效性，在安装在ClearPath Robotics Warthog机器人上的Gazebo模拟环境中使用了Universal Robots机械手UR5e，该机器人配备了Intel RealSense D435摄像头。该系统在修剪试验中取得了93%的成功率，平均末端轨迹误差为0.23 mm。视觉控制器在处理遮挡和在手臂朝向目标点移动时保持稳定轨迹方面表现出了强大的性能。结果验证了将基于视觉的跟踪与运动控制相结合用于精准农业任务的有效性。未来的工作将侧重于现实世界的实施和3D重建技术的集成，以增强动态环境中的适应性。 et.al.|[2504.07309](http://arxiv.org/abs/2504.07309)|null|
|**2025-04-09**|**Glossy Object Reconstruction with Cost-effective Polarized Acquisition**|基于图像的光滑物体3D重建的挑战在于从捕获的图像中分离出光滑表面上的漫反射和镜面反射分量，这项任务因仅使用RGB数据识别照明条件和材质属性的模糊性而变得复杂。虽然最先进的方法依赖于定制和/或高端设备进行数据采集，这可能既麻烦又耗时，但这项工作引入了一种可扩展的极化辅助方法，该方法采用了具有成本效益的采集工具。通过将线性偏振器连接到现成的RGB相机上，可以捕获多视图偏振图像，而不需要预先校准或精确测量偏振器角度，从而大大降低了系统建设成本。所提出的方法将极化BRDF、斯托克斯矢量和物体表面的极化状态表示为神经隐式场。通过优化输入偏振图像的渲染损失，结合偏振器角度，可以恢复这些场。通过利用偏振渲染的隐式表示的基本物理原理，我们的方法通过在公共数据集和真实捕获的图像中进行重建和新视图合成的实验，证明了其优于现有技术。 et.al.|[2504.07025](http://arxiv.org/abs/2504.07025)|null|
|**2025-04-09**|**SIGMAN:Scaling 3D Human Gaussian Generation with Millions of Assets**|长期以来，3D人体数字化一直是一项备受追求但具有挑战性的任务。现有的方法旨在从单个或多个视图生成高质量的3D数字人，但主要受到当前范式和3D人力资源稀缺的限制。具体而言，最近的方法分为几种范式：基于优化和前馈（单视图回归和带重建的多视图生成）。然而，由于遮挡和不可见性，它们在将低维平面映射到高维空间时分别受到速度慢、质量低、级联推理和模糊性的限制。此外，现有的3D人力资源规模仍然很小，不足以进行大规模培训。为了应对这些挑战，我们提出了一种用于3D人体数字化的潜在空间生成范式，该范式涉及通过UV结构化VAE将多视图图像压缩为高斯图像，以及基于DiT的条件生成，我们将不适定的低维到高维映射问题转化为可学习的分布偏移，这也支持端到端推理。此外，我们采用多视图优化方法结合合成数据构建HGS-1M数据集，其中包含100万美元的3D高斯资产，以支持大规模训练。实验结果表明，我们的范式在大规模训练的支持下，产生了具有复杂纹理、面部细节和宽松服装变形的高质量3D人体高斯模型。 et.al.|[2504.06982](http://arxiv.org/abs/2504.06982)|null|
|**2025-04-09**|**Wheat3DGS: In-field 3D Reconstruction, Instance Segmentation and Phenotyping of Wheat Heads with Gaussian Splatting**|植物形态特征的自动提取对于通过高通量田间表型分析（HTFP）支持作物育种和农业管理至关重要。基于多视图RGB图像的解决方案因其可扩展性和可负担性而具有吸引力，能够实现2D方法无法直接捕获的体积测量。虽然神经辐射场（NeRFs）等先进方法显示出了希望，但它们的应用仅限于从少数植物或器官中计数或提取特征。此外，由于田间条件下作物冠层的遮挡和密集排列，准确测量研究作物产量所必需的单个小麦头等复杂结构仍然特别具有挑战性。3D高斯散斑（3DGS）的最新发展为HTFP提供了一种有前景的替代方案，因为它具有高质量的重建和显式的基于点的表示。在本文中，我们提出了Wheat3DGS，这是一种利用3DGS和Segment Anything模型（SAM）自动对数百个小麦头进行精确3D实例分割和形态测量的新方法，代表了3DGS在HTFP中的首次应用。我们根据高分辨率激光扫描数据验证了小麦头提取的准确性，获得了长度、宽度和体积的平均绝对百分比误差分别为15.1%、18.3%和40.2%。我们提供了与基于NeRF的方法和传统多视图立体声（MVS）的额外比较，展示了卓越的结果。我们的方法能够大规模快速、无损地测量与产量相关的关键性状，这对加快作物育种和提高我们对小麦发育的理解具有重要意义。 et.al.|[2504.06978](http://arxiv.org/abs/2504.06978)|null|
|**2025-04-09**|**S-EO: A Large-Scale Dataset for Geometry-Aware Shadow Detection in Remote Sensing Applications**|我们介绍S-EO数据集：一个大规模、高分辨率的数据集，旨在推进几何感知阴影检测。我们的数据集来自不同的公共领域来源，包括挑战数据集和美国地质调查局等政府提供商，包括美国各地的702个地理参考图块，每个图块覆盖500x500米。每个图块包括多日期、多角度WorldView-3泛色RGB图像、全色图像和从激光雷达扫描获得的该地区的地面实况DSM。对于每张图像，我们提供了一个基于几何形状和太阳位置的阴影掩模、一个基于NDVI指数的植被掩模和一个捆绑调整的RPC模型。S-EO数据集拥有约20000张图像，为遥感图像中的阴影检测及其在3D重建中的应用建立了一个新的公共资源。为了证明数据集的影响，我们训练和评估了一个阴影探测器，展示了它的泛化能力，甚至是对航空图像的泛化能力。最后，我们扩展了EO-NeRF——一种最先进的卫星图像NeRF方法——以利用我们的阴影预测来改进3D重建。 et.al.|[2504.06920](http://arxiv.org/abs/2504.06920)|null|
|**2025-04-09**|**GSta: Efficient Training Scheme with Siestaed Gaussians for Monocular 3D Scene Reconstruction**|高斯散斑（GS）是一种流行的3D重建方法，主要是因为它能够合理快速地收敛，忠实地表示场景，并以快速的方式渲染（新颖的）视图。然而，它存在较大的存储和内存需求，其训练速度仍然落后于基于哈希网格的辐射场方法（如Instant NGP），这使得在机器人场景中部署它们变得特别困难，在这些场景中，3D重建对于精确操作至关重要。在本文中，我们提出了GSta，它基于高斯分布的位置和颜色梯度规范，动态识别在训练过程中收敛良好的高斯分布。通过迫使这些高斯人午睡并在训练过程中停止更新（冻结），与现有技术相比，我们以具有竞争力的准确性提高了训练速度。我们还提出了一种基于在训练图像子集上计算的PSNR值的早期停止机制。结合其他改进，如集成学习率调度器，GSta在保持质量的同时，在收敛速度、内存和存储要求方面实现了改进的帕累托前沿。我们还表明，GSta可以改进其他方法，并在提高效率方面补充正交方法；一旦与Trick GS结合使用，GSta的训练速度将提高5倍，磁盘大小比普通GS小16倍，同时具有相当的准确性，只消耗一半的峰值内存。更多可视化信息请访问https://anilarmagan.github.io/SRUK-GSta. et.al.|[2504.06716](http://arxiv.org/abs/2504.06716)|null|
|**2025-04-08**|**D^2USt3R: Enhancing 3D Reconstruction with 4D Pointmaps for Dynamic Scenes**|我们解决了动态场景中的3D重建任务，其中对象运动会降低先前3D点图回归方法的质量，例如最初为静态3D场景重建设计的DUSt3R。尽管这些方法在静态环境中提供了一种优雅而强大的解决方案，但它们在仅基于相机姿态的动态运动中难以实现。为了克服这一点，我们提出了D^2USt3R，它对4D点图进行回归，以前馈方式同时捕获静态和动态3D场景几何。通过明确地结合空间和时间方面，我们的方法成功地封装了与所提出的4D点图的时空密集对应关系，增强了下游任务。广泛的实验评估表明，我们提出的方法在具有复杂运动的各种数据集上始终实现了卓越的重建性能。 et.al.|[2504.06264](http://arxiv.org/abs/2504.06264)|null|

<p align=right>(<a href=#updated-on-20250414>back to top</a>)</p>

## Diffusion

|Publish Date|Title|Abstract|PDF|Code|
|---|---|---|---|---|
|**2025-04-10**|**Geo4D: Leveraging Video Generators for Geometric 4D Scene Reconstruction**|我们介绍了Geo4D，这是一种将视频扩散模型重新用于动态场景的单目3D重建的方法。通过利用这种视频模型捕获的强动态先验，可以仅使用合成数据来训练Geo4D，同时以零样本的方式将其很好地推广到真实数据。Geo4D预测了几种互补的几何形态，即点、深度和射线图。它使用一种新的多模态对齐算法在推理时对齐和融合这些模态以及多个滑动窗口，从而获得长视频的鲁棒和准确的4D重建。跨多个基准的广泛实验表明，Geo4D显著超越了最先进的视频深度估计方法，包括MonST3R等最新方法，这些方法也被设计用于处理动态场景。 et.al.|[2504.07961](http://arxiv.org/abs/2504.07961)|null|
|**2025-04-10**|**VisualCloze: A Universal Image Generation Framework via Visual In-Context Learning**|扩散模型的最新进展显著地推进了各种图像生成任务。然而，目前的主流方法仍然侧重于构建特定任务的模型，在支持各种不同需求时效率有限。虽然通用模型试图解决这一局限性，但它们面临着严峻的挑战，包括通用的任务指令、适当的任务分配和统一的架构设计。为了应对这些挑战，我们提出了VisualCloze，这是一个通用的图像生成框架，支持广泛的领域内任务、对看不见的任务的泛化、多个任务的看不见统一和反向生成。与依赖于基于语言的任务教学的现有方法不同，我们将视觉融入上下文学习，允许模型从视觉演示中识别任务，从而导致任务模糊和泛化能力弱。同时，视觉任务分布的固有稀疏性阻碍了跨任务可转移知识的学习。为此，我们引入了Graph200K，这是一个图结构的数据集，可以建立各种相互关联的任务，提高任务密度和可转移的知识。此外，我们发现，我们的统一图像生成公式与图像填充具有一致的目标，使我们能够在不修改架构的情况下利用预训练填充模型的强生成先验。 et.al.|[2504.07960](http://arxiv.org/abs/2504.07960)|null|
|**2025-04-10**|**GenEAva: Generating Cartoon Avatars with Fine-Grained Facial Expressions from Realistic Diffusion-based Faces**|卡通化身已被广泛应用于各种应用中，包括社交媒体、在线辅导和游戏。然而，现有的卡通化身数据集和生成方法很难用精细的面部表情来呈现高表达性的化身，并且往往受到现实世界身份的启发，这引发了隐私问题。为了应对这些挑战，我们提出了一种新的框架GenEAva，用于生成具有精细面部表情的高质量卡通化身。我们的方法微调了最先进的文本到图像扩散模型，以合成高度详细和富有表现力的面部表情。然后，我们结合了一个风格化模型，将这些逼真的面孔转换为卡通化身，同时保留身份和表情。利用这一框架，我们引入了第一个富有表现力的卡通化身数据集GenEAva 1.0，专门用于捕捉135个精细的面部表情，包括13230个富有表现能力的卡通化身，在性别、种族和年龄范围内分布均衡。我们证明，我们的微调模型比最先进的文本到图像扩散模型SDXL生成了更具表现力的面部。我们还验证了我们的框架生成的卡通化身不包括来自微调数据的记忆身份。所提出的框架和数据集为未来卡通形象生成的研究提供了多样化和富有表现力的基准。 et.al.|[2504.07945](http://arxiv.org/abs/2504.07945)|null|
|**2025-04-10**|**HoloPart: Generative 3D Part Amodal Segmentation**|3D部分模分割——将3D形状分解为完整的、语义上有意义的部分，即使在被遮挡的情况下——对于3D内容的创建和理解来说是一项具有挑战性但至关重要的任务。现有的3D零件分割方法只能识别可见的表面补丁，限制了它们的实用性。受2D amodal分割的启发，我们将这项新任务引入3D领域，并提出了一种实用的两阶段方法，解决了推断遮挡的3D几何形状、保持全局形状一致性以及在有限的训练数据下处理不同形状的关键挑战。首先，我们利用现有的3D零件分割来获得初始的、不完整的零件段。其次，我们引入了HoloPart，一种新的基于扩散的模型，将这些片段完整地转化为3D零件。HoloPart利用具有局部关注的专用架构来捕获细粒度的零件几何形状和全局形状上下文关注，以确保整体形状的一致性。我们引入了基于ABO和PartObjaverse Tiny数据集的新基准测试，并证明HoloPart明显优于最先进的形状完成方法。通过将HoloPart与现有的分割技术相结合，我们在3D零件无模分割方面取得了有前景的结果，为几何编辑、动画和材料分配的应用开辟了新的途径。 et.al.|[2504.07943](http://arxiv.org/abs/2504.07943)|null|
|**2025-04-10**|**Optimal Control For Anti-Abeta Treatment in Alzheimer's Disease using a Reaction-Diffusion Model**|阿尔茨海默病是一种进行性神经退行性疾病，严重损害患者的生存和生活质量。虽然目前的药物治疗旨在减缓疾病进展，但它们仍然不足以阻止认知能力下降。数学建模已成为理解AD动力学和优化治疗策略的有力工具。然而，大多数现有的模型都使用基于常微分方程的方法关注时间动力学，往往忽视了空间异质性在疾病进展中的关键作用。在这项研究中，我们采用空间显式反应扩散模型来描述大脑中的淀粉样蛋白β（aβ）动力学，在考虑潜在副作用的同时进行治疗优化。我们的目标是尽量减少淀粉样蛋白β斑块浓度，同时平衡治疗效果与不良反应，如淀粉样蛋白相关成像异常（ARIA）。在特定的假设下，我们建立了最优解的适定性和唯一性。我们采用基于有限元法的数值方法来计算个性化治疗策略，利用真实的患者淀粉样蛋白β正电子发射断层扫描（PET）扫描数据。我们的研究结果表明，最佳治疗策略优于恒定给药方案，在最大限度地减少副作用的同时，显著降低了淀粉样蛋白负荷。通过整合空间动力学和个性化治疗计划，我们的框架提供了一种改进阿尔茨海默病治疗干预的新方法。 et.al.|[2504.07913](http://arxiv.org/abs/2504.07913)|null|
|**2025-04-10**|**Hodge Laplacians and Hodge Diffusion Maps**|我们介绍了Hodge扩散图，这是一种新的流形学习算法，旨在从高维数据集中分析和提取拓扑信息。该方法近似作用于微分形式的外导数，从而提供Hodge-Lalacian算子的近似值。霍奇扩散图扩展了现有的非线性降维技术，包括向量扩散图，以及扩散图和拉普拉斯特征图背后的理论。我们的方法通过使用霍奇-拉普拉斯算子将数据集投影到低维欧几里德空间来捕获数据集的高阶拓扑特征。我们开发了一个理论框架，基于分布在真实流形上的采样点来估计外导数的近似误差。数值实验支持并验证了所提出的方法。 et.al.|[2504.07910](http://arxiv.org/abs/2504.07910)|null|
|**2025-04-10**|**Stupendously Large Primordial Black Holes from the QCD axion**|当场空间中简并极小值之间的距离距离膨胀哈勃尺度不太远时，具有离散对称性的（伪）标量场的膨胀扩散可以在膨胀后引发闭畴壁气体的形成。一旦足够重的畴壁重新进入哈勃球体，原始黑洞（PBH）就可以形成。在这种情况下，膨胀决定了一种独特的PBH质量分布，这种分布相当平坦，因此可以导致PBH的总丰度相当大，同时避免了临界坍塌对PBH形成的一些不利影响。我们证明，衰减常数接近膨胀哈勃尺度的通用QCD轴子模型可以以PBH的形式产生高达1%的暗物质（DM），同时与宇宙微波背景观测的等曲率约束兼容。当轴子衰变常数值在 $f_a\simeq 10^{8}~\text{GeV}$附近时，就会发生这种情况，该区域是轴子日镜的目标区域，部分受到天体物理观测的限制。由此产生的PBH质量巨大，超过10美元^{11}M_\odot$，它们的存在可以通过大尺度结构观测来探测。轴子样粒子可以产生更大的PBH丰度。或者，在可以放宽等曲率约束的情况下，我们发现DM的整体可以通过QCD轴子失准机制产生，并伴随着质量为$（10^5-10^6）~M_odot$的PBH中的$\cal O}（10^{-3}）$ DM分数。正如最近JWST观测所表明的那样，这些可以作为在大红移下形成大质量黑洞的种子。 et.al.|[2504.07890](http://arxiv.org/abs/2504.07890)|null|
|**2025-04-10**|**Numerical solution by shape optimization method to an inverse shape problem in multi-dimensional advection-diffusion problem with space dependent coefficients**|这项工作的重点是使用形状优化技术数值求解与具有空间相关系数的平流扩散过程相关的形状识别问题。考虑了两个边界型成本泛函，并使用伴随方法，采用链式规则方法推导了它们相对于形状的相应变化。这涉及首先利用状态系统的物质导数，其次利用其形状导数。随后，将交替方向乘子法（ADMM）与Sobolev梯度下降算法相结合，稳定地解决了形状重建问题。通过二维和三维数值实验证明了该方法的可行性。 et.al.|[2504.07796](http://arxiv.org/abs/2504.07796)|null|
|**2025-04-10**|**Revisiting Likelihood-Based Out-of-Distribution Detection by Modeling Representations**|分布外（OOD）检测对于确保深度学习系统的可靠性至关重要，特别是在安全关键的应用中。基于似然性的深度生成模型历来因其在面向对象检测中的表现不佳而受到批评，当应用于图像数据时，它们通常为面向对象数据分配比分布样本更高的似然性。在这项工作中，我们证明了可能性本身并没有缺陷。相反，图像空间中的几个属性禁止将似然性作为有效的检测分数。给定一个足够好的似然估计器，特别是使用扩散模型的概率流公式，我们表明，当应用于预训练编码器的表示空间时，基于似然的方法仍然可以与最先进的方法相提并论。我们的工作代码可以在 $\href上找到{https://github.com/limchaos/Likelihood-OOD.git}｛\texttt{https://github.com/limchaos/Likelihood-OOD.git}}$ . et.al.|[2504.07793](http://arxiv.org/abs/2504.07793)|**[link](https://github.com/limchaos/likelihood-ood)**|
|**2025-04-10**|**Millimeter emission from supermassive black hole coronae**|活动星系核（AGN）是吸积超大质量黑洞（SMBH）的宿主。吸积会导致在SMBH附近形成一个高温的X射线发射日冕，能够加速相对论电子。毫米波段的观测可以探测到它的同步辐射。我们提供了一个框架，通过模拟从无线电到远红外频率的光谱能量分布（SED）来获取SMBH日冕的物理信息。我们还探索了从毫米观测中获取额外信息的可能性，如SMBH质量，并研究了高红移透镜源。我们介绍了一种基于单区球形区域的电晕发射模型，该模型具有混合的热等离子体和非热等离子体。我们详细研究了电晕SED如何取决于不同的参数，如尺寸、不透明度和磁场强度。来自尘埃、电离气体和扩散相对论电子的其他星系发射成分也包括在SED拟合方案中。我们一致地将我们的代码应用于一个无线电静默AGN样本，该样本在毫米范围内有强烈的日冕成分指示。检测到的SMBH日冕的毫米辐射与非热相对论粒子群的能量密度一致，该粒子群的能量密度约为热等离子体中的0.5-10%。这需要接近热气体均分的磁能密度，以及60-250重力半径的日冕尺寸。在考虑电晕尺寸的不确定性时，该模型还可以再现观察到的毫米发射和SMBH质量之间的相关性。毫米波段为SMBH日冕的物理学提供了一个独特的窗口，可以研究高度尘埃遮蔽的源和高红移透镜类星体。深入了解SMBH日冕中的相对论粒子群可以为其潜在的多波长和中微子发射提供关键见解。 et.al.|[2504.07762](http://arxiv.org/abs/2504.07762)|null|

<p align=right>(<a href=#updated-on-20250414>back to top</a>)</p>

## NeRF

|Publish Date|Title|Abstract|PDF|Code|
|---|---|---|---|---|
|**2025-04-08**|**econSG: Efficient and Multi-view Consistent Open-Vocabulary 3D Semantic Gaussians**|最近关于开放词汇神经场的工作的主要重点是从VLM中提取精确的语义特征，然后将它们有效地整合到多视图一致的3D神经场表示中。然而，大多数现有的工作都是在受信任的SAM上进行的，以规范图像级CLIP，而无需进一步细化。此外，一些现有的研究通过在与3DGS语义场融合之前对2D VLM的语义特征进行降维来提高效率，这不可避免地导致了多视图不一致。在这项工作中，我们提出了使用3DGS进行开放式词汇语义分割的econSG。我们的econSG由以下部分组成：1）置信区间引导正则化（CRR），它相互细化SAM和CLIP，以获得具有完整和精确边界的精确语义特征的两全其美。2） 一个低维上下文空间，通过融合反投影的多视图2D特征来增强3D多视图一致性，同时提高计算效率，然后直接对融合的3D特征进行降维，而不是分别对每个2D视图进行操作。与现有方法相比，我们的econSG在四个基准数据集上显示了最先进的性能。此外，我们也是所有方法中最有效的培训。 et.al.|[2504.06003](http://arxiv.org/abs/2504.06003)|null|
|**2025-04-08**|**Meta-Continual Learning of Neural Fields**|神经场（NF）作为一种用于复杂数据表示的通用框架，已经获得了突出地位。这项工作揭示了一个新的问题设置，称为“神经场元连续学习”（MCL-NF），并引入了一种新的策略，该策略采用模块化架构与基于优化的元学习相结合。我们的策略侧重于克服现有神经场连续学习方法的局限性，如灾难性遗忘和缓慢收敛，实现了高质量的重建，显著提高了学习速度。我们进一步引入了神经辐射场的Fisher信息最大化损失（FIM-NeRF），它在样本级别最大化信息增益以增强学习泛化，并证明了收敛保证和泛化界限。我们在六个不同的数据集上对图像、音频、视频重建和视图合成任务进行了广泛的评估，证明了我们的方法在重建质量和速度方面优于现有的MCL和CL-NF方法。值得注意的是，我们的方法在降低参数要求的情况下，实现了神经场对城市级NeRF渲染的快速适应。 et.al.|[2504.05806](http://arxiv.org/abs/2504.05806)|null|
|**2025-04-06**|**Dynamic Neural Field Modeling of Visual Contrast for Perceiving Incoherent Looming**|Amari的动态神经场（DNF）框架提供了一种受大脑启发的方法来模拟神经元群的平均激活。利用单一领域，DNF已成为机器人应用中低能耗隐约感知模块的有前景的基础。然而，之前的DNF方法在检测不连贯或不一致的迫在眉睫的特征方面面临着重大挑战，这些特征在现实世界场景中很常见，例如雨天的碰撞检测。果蝇和蝗虫视觉系统的见解表明，编码ON/OFF视觉对比在增强迫在眉睫的选择性方面起着至关重要的作用。此外，横向激发机制可能会改善织机敏感神经元对连贯和非连贯刺激的反应。这些共同为改进迫在眉睫的感知模型提供了宝贵的指导。基于这些生物学证据，我们通过结合on/OFF视觉对比度的建模来扩展之前的单场DNF框架，每个对比度都由一个专用的DNF控制。使用归一化高斯核对每个ON/OFF对比场内的横向激励进行公式化，并将其输出整合到求和字段中以生成碰撞警报。实验评估表明，所提出的模型有效地解决了非相干逼近检测的挑战，并且明显优于最先进的蝗虫启发模型。它在各种刺激下表现出了强大的性能，包括合成雨效应，突显了它在复杂、嘈杂的环境中，在视觉线索不一致的情况下，具有可靠的隐约感知的潜力。 et.al.|[2504.04551](http://arxiv.org/abs/2504.04551)|null|
|**2025-04-03**|**A Physics-Informed Meta-Learning Framework for the Continuous Solution of Parametric PDEs on Arbitrary Geometries**|在这项工作中，我们引入了隐式有限算子学习（iFOL），用于任意几何上偏微分方程（PDE）的连续和参数解。我们提出了一种基于物理信息的编解码器网络，以建立连续参数和解空间之间的映射。解码器通过利用以潜在或特征码为条件的隐式神经场网络来构建参数解场。实例特定代码是通过基于二阶元学习技术的PDE编码过程导出的。在训练和推理中，在PDE编码和解码过程中，物理信息损失函数被最小化。iFOL以能量或加权残差形式表示损失函数，并使用从标准数值PDE方法导出的离散残差对其进行评估。这种方法在训练和推理过程中都会导致离散残差的反向传播。iFOL具有几个关键特性：（1）其独特的损失公式消除了以前在PDE的条件神经场算子学习中使用的传统编码过程-解码流水线的需要；（2） 它不仅提供精确的参数和连续场，而且提供参数梯度的解，而不需要额外的损失项或灵敏度分析；（3） 它可以有效地捕捉溶液中的尖锐不连续性；（4）它消除了对几何和网格的约束，使其适用于任意几何和空间采样（零样本超分辨率能力）。我们批判性地评估了这些特征，并分析了网络在稳态和瞬态PDE中推广到看不见的样本的能力。所提出的方法的整体性能是有希望的，证明了它适用于计算力学中一系列具有挑战性的问题。 et.al.|[2504.02459](http://arxiv.org/abs/2504.02459)|**[link](https://github.com/rezanajian/fol)**|
|**2025-04-01**|**Flow Matching on Lie Groups**|流匹配（FM）是一种最新的生成建模技术：我们的目标是学习如何从分布中采样{X}_1 $通过从某些分布中流动样本$\mathfrak{X}_0$很容易取样。关键技巧是，在$\mathfrak中对端点进行调节的同时，可以训练这个流场{X}_1$：给定终点，只需沿直线段移动到终点（Lipman等人，2022）。然而，直线段仅在欧几里德空间上定义良好。因此，Chen和Lipman（2023）将该方法推广到黎曼流形上的FM，用测地线或其谱近似代替线段。我们采取了另一种观点：我们通过用指数曲线代替线段来推广李群上的FM。这导致了许多矩阵李群的简单、内在和快速实现，因为所需的李群运算（积、逆、指数、对数）仅由相应的矩阵运算给出。然后，李群上的FM可用于生成建模，数据由特征集（在$\mathbb{R}^n$ 中）和姿势集（在某些李群中）组成，例如等变神经场的潜在码（Wessels等人，2025）。 et.al.|[2504.00494](http://arxiv.org/abs/2504.00494)|**[link](https://github.com/finnsherry/FlowMatching)**|
|**2025-03-29**|**NeuralGS: Bridging Neural Fields and 3D Gaussian Splatting for Compact 3D Representations**|3D高斯散点（3DGS）显示了卓越的质量和渲染速度，但有数百万的3D高斯分布和巨大的存储和传输成本。最近的3DGS压缩方法主要集中在压缩脚手架GS上，取得了令人印象深刻的性能，但增加了体素结构和复杂的编码和量化策略。在这篇论文中，我们的目标是开发一种简单而有效的方法，称为NeuralGS，它以另一种方式探索将原始3DGS压缩成紧凑的表示，而不需要体素结构和复杂的量化策略。我们的观察是，像NeRF这样的神经场可以用多层感知器（MLP）神经网络表示复杂的3D场景，只需要几兆字节。因此，NeuralGS有效地采用神经场表示来用MLP对3D高斯的属性进行编码，即使对于大规模场景，也只需要很小的存储空间。为了实现这一点，我们采用了一种聚类策略，并根据高斯的重要性得分作为拟合权重，为每个聚类用不同的微小MLP对高斯进行拟合。我们在多个数据集上进行实验，在不损害视觉质量的情况下实现了平均模型大小减少45倍。我们的方法在原始3DGS上的压缩性能与基于Scaffold GS的专用压缩方法相当，这表明了用神经场直接压缩原始3DGS的巨大潜力。 et.al.|[2503.23162](http://arxiv.org/abs/2503.23162)|null|
|**2025-03-27**|**Renormalization group analysis of noisy neural field**|大脑中的神经元在个体特性和与其他神经元的连接方面表现出极大的多样性。为了深入了解神经元多样性如何在大尺度上促进大脑动力学和功能，我们借鉴了复制方法的框架，该框架已成功应用于平衡统计力学中一大类具有淬灭噪声的问题。我们分析了Wilson Cowan模型的两个线性化版本，其随机系数在空间上是相关的。特别是：（A）神经元本身的性质是异质的，（B）它们的连接是各向异性的。在这两个模型中，淬火随机性的平均会产生额外的非线性。这些非线性在威尔逊重整化群的框架内进行了分析。我们发现，对于模型A，如果噪声的空间相关性随距离衰减，指数小于-2 $，则在大的空间尺度上，噪声的影响消失了。相比之下，对于模型B，只有当空间相关性以小于-1$ 的指数衰减时，噪声对神经元连接的影响才会消失。我们的计算还表明，在某些条件下，噪声的存在可能会在大尺度上产生类似行波的行为，尽管这一结果在微扰理论的高阶下是否仍然有效还有待观察。 et.al.|[2503.21605](http://arxiv.org/abs/2503.21605)|null|
|**2025-03-25**|**Thin-Shell-SfT: Fine-Grained Monocular Non-rigid 3D Surface Tracking with Neural Deformation Fields**|从单目RGB视频中重建高度可变形的表面（如布料）是一个具有挑战性的问题，没有任何解决方案可以提供一致和准确的细粒度表面细节恢复。为了解释环境的病态性，现有的方法使用具有统计、神经或物理先验的变形模型。它们还主要依赖于非自适应离散曲面表示（例如多边形网格），逐帧优化导致误差传播，并受到基于网格的可微渲染器梯度差的影响。因此，织物褶皱等精细表面细节往往无法以所需的精度恢复。针对这些局限性，我们提出了ThinShell SfT，这是一种用于非刚性3D跟踪的新方法，将表面表示为隐式和连续的时空神经场。我们采用基于基尔霍夫-洛夫模型的连续薄壳物理先验进行空间正则化，这与早期作品的离散化替代方案形成了鲜明对比。最后，我们利用3D高斯溅射将表面可微分地渲染到图像空间中，并根据合成原理分析优化变形。我们的薄壳SfT在定性和定量上都优于先前的工作，这要归功于我们的连续表面公式以及专门定制的模拟先验和表面诱导的3D高斯。请访问我们的项目页面https://4dqv.mpiinf.mpg.de/ThinShellSfT. et.al.|[2503.19976](http://arxiv.org/abs/2503.19976)|null|
|**2025-03-25**|**Decoupled Dynamics Framework with Neural Fields for 3D Spatio-temporal Prediction of Vehicle Collisions**|本研究提出了一种神经框架，通过独立建模全局刚体运动和局部结构变形来预测3D车辆碰撞动力学。与直接预测绝对位移的方法不同，这种方法明确地将车辆的整体平移和旋转与其结构变形分开。两个专门的网络构成了该框架的核心：一个基于四元数的刚性网络用于刚性运动，一个基于坐标的变形网络用于局部变形。通过独立处理根本不同的物理现象，所提出的架构实现了准确的预测，而不需要对每个组件进行单独的监督。该模型仅在10%的可用模拟数据上进行训练，其性能明显优于基线模型，包括单层感知器（MLP）和深度算子网络（DeepONet），预测误差降低了83%。广泛的验证表明，它对训练范围外的碰撞条件具有很强的泛化能力，即使在涉及极端速度和大冲击角度的严重冲击下，也能准确预测响应。此外，该框架成功地从低分辨率输入重建了高分辨率变形细节，而无需增加计算工作量。因此，所提出的方法为在复杂的碰撞场景中快速可靠地评估车辆安全提供了一种有效、计算高效的方法，大大减少了所需的模拟数据和时间，同时保持了预测的保真度。 et.al.|[2503.19712](http://arxiv.org/abs/2503.19712)|null|
|**2025-03-21**|**Towards Understanding the Benefits of Neural Network Parameterizations in Geophysical Inversions: A Study With Neural Fields**|在这项工作中，我们采用了神经场，它使用神经网络以测试时学习的方式将坐标映射到该坐标处的相应物理属性值。对于测试时学习方法，与需要使用训练数据集训练网络的传统方法相比，在反演过程中学习权重。首先展示了地震层析成像和直流电阻率反演中的合成示例结果。然后，我们对这两种情况下的神经网络权重的雅可比矩阵进行奇异值分解分析（SVD分析），以探索神经网络对恢复模型的影响。结果表明，测试时间学习方法可以消除恢复的地下物理性质模型中由测量和物理敏感性引起的不必要的伪影。因此，在某些情况下，与常规反演相比，NFs-Inv可以改善反演结果，例如恢复倾角或预测主要目标的边界。在SVD分析中，我们观察到左奇异向量中的相似模式，就像在计算机视觉中的生成任务中以监督方式训练的一些扩散模型中观察到的那样。这一观察结果提供了证据，表明神经网络结构中固有的隐式偏差在监督学习和测试时学习模型中很有用。这种隐式偏差有可能对地球物理反演中的模型恢复有用。 et.al.|[2503.17503](http://arxiv.org/abs/2503.17503)|null|

<p align=right>(<a href=#updated-on-20250414>back to top</a>)</p>

[contributors-shield]: https://img.shields.io/github/contributors/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[contributors-url]: https://github.com/Vincentqyw/cv-arxiv-daily/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[forks-url]: https://github.com/Vincentqyw/cv-arxiv-daily/network/members
[stars-shield]: https://img.shields.io/github/stars/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[stars-url]: https://github.com/Vincentqyw/cv-arxiv-daily/stargazers
[issues-shield]: https://img.shields.io/github/issues/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[issues-url]: https://github.com/Vincentqyw/cv-arxiv-daily/issues

