[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]

## Updated on 2025.03.16
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
|**2025-03-13**|**V2Edit: Versatile Video Diffusion Editor for Videos and 3D Scenes**|本文介绍了V $^2$Edit，这是一种用于指令引导视频和3D场景编辑的新型无训练框架。为了应对平衡原始内容保存与编辑任务完成的关键挑战，我们的方法采用了一种渐进策略，将复杂的编辑任务分解为一系列更简单的子任务。每个子任务都通过三个关键的协同机制进行控制：初始噪声、在每个去噪步骤添加的噪声以及文本提示和视频内容之间的交叉注意力图。这确保了原始视频元素的稳健保存，同时有效地应用了所需的编辑。除了其原生视频编辑功能外，我们还通过“渲染-编辑-重建”过程将V$^2$Edit扩展到3D场景编辑，即使对于涉及大量几何变化（如对象插入）的任务，也能进行高质量、3D一致的编辑。大量实验表明，我们的V$^2$ Edit在各种具有挑战性的视频编辑任务和复杂的3D场景编辑任务中实现了高质量和成功的编辑，从而在这两个领域建立了最先进的性能。 et.al.|[2503.10634](http://arxiv.org/abs/2503.10634)|null|
|**2025-03-13**|**NIL: No-data Imitation Learning by Leveraging Pre-trained Video Diffusion Models**|在包括人形机器人、四足动物和动物在内的各种非传统形态中获得物理上合理的运动技能对于推进角色模拟和机器人技术至关重要。传统的方法，如强化学习（RL），是特定于任务和身体的，需要大量的奖励函数工程，并且不能很好地推广。模仿学习提供了一种替代方法，但严重依赖于高质量的专家演示，这对于非人类形态来说很难获得。另一方面，视频扩散模型能够生成各种形态的逼真视频，从人类到蚂蚁。利用这一能力，我们提出了一种独立于数据的技能获取方法，该方法从2D生成的视频中学习3D运动技能，并具有对非传统和非人类形式的泛化能力。具体来说，我们通过计算视频嵌入之间的成对距离，利用视觉变换器进行基于视频的比较，从而指导模仿学习过程。除了视频编码距离，我们还使用分段视频帧之间的计算相似度作为指导奖励。我们在涉及独特身体配置的运动任务中验证了我们的方法。在类人机器人运动任务中，我们证明了“无数据模仿学习”（NIL）优于基于3D运动捕捉数据训练的基线。我们的研究结果强调了利用生成视频模型进行具有不同形态的物理上合理的技能学习的潜力，有效地用数据生成代替数据收集进行模仿学习。 et.al.|[2503.10626](http://arxiv.org/abs/2503.10626)|null|
|**2025-03-13**|**MuDG: Taming Multi-modal Diffusion with Gaussian Splatting for Urban Scene Reconstruction**|最近在辐射领域的突破显著推进了自动驾驶中的3D场景重建和新颖视图合成（NVS）。然而，关键的局限性仍然存在：基于重建的方法在与训练轨迹的显著视点偏差下表现出显著的性能下降，而基于生成的技术在时间连贯性和精确的场景可控性方面存在困难。为了克服这些挑战，我们提出了MuDG，这是一个创新的框架，将多模态扩散模型与高斯散斑（GS）相结合，用于城市场景重建。MuDG利用具有RGB和几何先验的聚合LiDAR点云来调节多模态视频扩散模型，为新的视点合成逼真的RGB、深度和语义输出。该合成流水线支持前馈NVS，而无需计算密集型的每个场景优化，提供全面的监督信号来细化3DGS表示，以在极端视点变化下增强渲染鲁棒性。在Open Waymo数据集上的实验表明，MuDG在重建和合成质量方面都优于现有方法。 et.al.|[2503.10604](http://arxiv.org/abs/2503.10604)|null|
|**2025-03-13**|**CameraCtrl II: Dynamic Scene Exploration via Camera-controlled Video Diffusion Models**|本文介绍了CameraCtrl II，这是一个通过相机控制的视频扩散模型实现大规模动态场景探索的框架。以前的相机条件视频生成模型在生成具有大相机运动的视频时，视频动态性降低，视点范围有限。我们采取了一种逐步扩展动态场景生成的方法——首先增强单个视频片段中的动态内容，然后扩展此功能，在宽视点范围内创建无缝探索。具体来说，我们构建了一个具有大量动态特性的数据集，并附有相机参数注释进行训练，同时设计了一个轻量级的相机注入模块和训练方案，以保持预训练模型的动态特性。基于这些改进的单剪辑技术，我们允许用户迭代地指定相机轨迹以生成连贯的视频序列，从而实现了扩展的场景探索。不同场景的实验表明，CameraCtrl Ii能够实现相机控制的动态场景合成，其空间探索范围比以前的方法要广得多。 et.al.|[2503.10592](http://arxiv.org/abs/2503.10592)|null|
|**2025-03-13**|**Long Context Tuning for Video Generation**|视频生成的最新进展可以通过可扩展的扩散变换器生成逼真的、一分钟长的单镜头视频。然而，现实世界的叙事视频需要多镜头场景，镜头之间的视觉和动态一致性。在这项工作中，我们引入了长上下文调整（LCT），这是一种训练范式，它扩展了预训练的单镜头视频扩散模型的上下文窗口，直接从数据中学习场景级一致性。我们的方法将全注意力机制从单个镜头扩展到场景中的所有镜头，结合了交错的3D位置嵌入和异步噪声策略，实现了无需额外参数的联合和自回归镜头生成。LCT后具有双向注意力的模型可以进一步用上下文因果注意力进行微调，通过高效的KV缓存促进自回归生成。实验证明，LCT后的单镜头模型可以产生连贯的多镜头场景，并展现出新兴的能力，包括构图生成和交互式镜头扩展，为更实用的视觉内容创作铺平了道路。看见https://guoyww.github.io/projects/long-context-video/了解更多详情。 et.al.|[2503.10589](http://arxiv.org/abs/2503.10589)|null|
|**2025-03-13**|**CINEMA: Coherent Multi-Subject Video Generation via MLLM-Based Guidance**|随着深度生成模型，特别是扩散模型的出现，视频生成取得了显著进展。虽然现有的方法在从文本提示或单张图像生成高质量视频方面表现出色，但个性化多主题视频生成仍然是一个很大程度上未被探索的挑战。这项任务涉及合成包含多个不同主题的视频，每个主题由单独的参考图像定义，同时确保时间和空间的一致性。目前的方法主要依赖于将主题图像映射到文本提示中的关键字，这引入了歧义，限制了它们有效建模主题关系的能力。在本文中，我们提出了CINEMA，这是一种利用多模态大语言模型（MLLM）生成连贯多主题视频的新框架。我们的方法消除了主题图像和文本实体之间明确对应的需要，减轻了歧义并减少了注释工作。通过利用MLLM来解释主题关系，我们的方法促进了可扩展性，使大型和多样化的数据集能够用于训练。此外，我们的框架可以根据不同数量的主题进行调整，为个性化内容创建提供了更大的灵活性。通过广泛的评估，我们证明我们的方法显著提高了主题的一致性和整体视频的连贯性，为讲故事、互动媒体和个性化视频生成的高级应用铺平了道路。 et.al.|[2503.10391](http://arxiv.org/abs/2503.10391)|null|
|**2025-03-13**|**Semantic Latent Motion for Portrait Video Generation**|肖像视频生成的最新进展值得注意。然而，现有的方法严重依赖于人类先验和预训练的生成模型，这可能会引入不切实际的运动，导致推理效率低下。为了应对这些挑战，我们提出了语义潜在运动（SeMo），这是一种紧凑而富有表现力的运动表示。利用这种表示，我们的方法既实现了高质量的视觉结果，又实现了高效的推理。SeMo遵循一个有效的三步框架：抽象、推理和生成。首先，在抽象步骤中，我们使用精心设计的掩模运动编码器将受试者的运动状态压缩为紧凑抽象的潜在运动（1D标记）。其次，在推理步骤中，在这个潜在空间中进行长期建模和高效推理，以生成运动序列。最后，在生成步骤中，运动动力学作为条件信息，指导生成模型合成从参考帧到目标帧的真实过渡。由于语义潜在运动的紧凑性和描述性，我们的方法能够生成具有高度逼真运动的实时视频。用户研究表明，我们的方法超越了最先进的模型，在现实中的获胜率为81%。广泛的实验进一步突显了其强大的压缩能力、重建质量和生成潜力。此外，其完全自我监督的性质表明，它在更广泛的视频生成任务中具有广阔的应用前景。 et.al.|[2503.10096](http://arxiv.org/abs/2503.10096)|null|
|**2025-03-13**|**VMBench: A Benchmark for Perception-Aligned Video Motion Generation**|视频生成技术发展迅速，改进了评估方法，但评估视频的运动仍然是一个主要挑战。具体来说，有两个关键问题：1）当前的运动指标与人类感知不完全一致；2） 现有的运动提示是有限的。基于这些发现，我们介绍了VMBench——一个全面的视频运动基准测试，它具有感知对齐的运动度量，并具有最多样化的运动类型。VMBench有几个吸引人的特性：1）感知驱动的运动评估指标，我们在运动视频评估中基于人类感知确定了五个维度，并开发了细粒度的评估指标，从而更深入地了解了模型在运动质量方面的优缺点。2） 元引导运动提示生成是一种结构化方法，可以提取元信息，使用LLM生成各种运动提示，并通过人工智能验证对其进行改进，从而形成一个覆盖六个关键动态场景维度的多级提示库。3） 人类对齐验证机制，我们提供人类偏好注释来验证我们的基准，我们的指标在Spearman相关性方面比基线方法平均提高了35.3%。这是首次从人类感知对齐的角度评估视频中的运动质量。此外，我们很快将在https://github.com/GD-AIGC/VMBench，为评估和推进运动生成模型设定了新的标准。 et.al.|[2503.10076](http://arxiv.org/abs/2503.10076)|null|
|**2025-03-13**|**UVE: Are MLLMs Unified Evaluators for AI-Generated Videos?**|随着视频生成模型（VGM）的快速增长，为人工智能生成的视频（AIGV）开发可靠和全面的自动指标至关重要。现有的方法要么使用针对其他任务优化的现成模型，要么依靠人工评估数据来培训专业评估人员。这些方法仅限于特定的评估方面，并且难以随着对更细粒度和更全面的评估需求的增加而扩展。为了解决这个问题，这项工作研究了使用多模态大型语言模型（MLLM）作为AIGV统一评估器的可行性，利用其强大的视觉感知和语言理解能力。为了评估自动度量在统一AIGV评估中的性能，我们引入了一个名为UVE Bench的基准。UVE Bench收集由最先进的VGM生成的视频，并在15个评估方面提供成对的人类偏好注释。使用UVE Bench，我们广泛评估了16个MLLM。我们的实证结果表明，虽然先进的MLLM（如Qwen2VL-72B和InternVL2.5-78B）仍然落后于人类评估者，但它们在统一AIGV评估方面表现出了有前景的能力，大大超过了现有的专业评估方法。此外，我们对影响MLLM驱动评估器性能的关键设计选择进行了深入分析，为未来AIGV评估的研究提供了有价值的见解。该代码可在以下网址获得https://github.com/bytedance/UVE. et.al.|[2503.09949](http://arxiv.org/abs/2503.09949)|null|
|**2025-03-13**|**VideoMerge: Towards Training-free Long Video Generation**|长视频生成仍然是计算机视觉领域一个具有挑战性和吸引力的话题。在各种视频生成方法中，基于扩散的模型通过迭代去噪过程实现了最先进的质量。然而，视频域的内在复杂性使得这种扩散模型的训练在数据管理和计算资源方面都非常昂贵。此外，这些模型通常对表示视频的固定噪声张量进行操作，从而产生预定的空间和时间维度。尽管有几种高质量的开源预训练视频扩散模型，可以在不同长度和分辨率的图像和视频上联合训练，但通常不建议在推理时指定未包含在训练集中的视频长度。因此，这些模型不容易通过仅仅增加指定的视频长度来直接生成较长的视频。除了可行性挑战外，长视频生成还遇到了质量问题。长视频的领域本质上比短视频更复杂：持续时间延长会带来更大的可变性，需要长时间的时间一致性，从而增加了任务的整体难度。我们提出了VideoMerge，这是一种无需训练的方法，可以无缝地将预训练文本生成的短视频合并到视频扩散模型中。我们的方法保留了模型的原始表现力和一致性，同时允许用户指定的延长持续时间和动态变化。通过利用预训练模型的优势，我们的方法通过协作实现卓越质量的正交策略来解决与平滑度、一致性和动态内容相关的挑战。 et.al.|[2503.09926](http://arxiv.org/abs/2503.09926)|null|

<p align=right>(<a href=#updated-on-20250316>back to top</a>)</p>

## 3D

|Publish Date|Title|Abstract|PDF|Code|
|---|---|---|---|---|
|**2025-03-13**|**MuDG: Taming Multi-modal Diffusion with Gaussian Splatting for Urban Scene Reconstruction**|最近在辐射领域的突破显著推进了自动驾驶中的3D场景重建和新颖视图合成（NVS）。然而，关键的局限性仍然存在：基于重建的方法在与训练轨迹的显著视点偏差下表现出显著的性能下降，而基于生成的技术在时间连贯性和精确的场景可控性方面存在困难。为了克服这些挑战，我们提出了MuDG，这是一个创新的框架，将多模态扩散模型与高斯散斑（GS）相结合，用于城市场景重建。MuDG利用具有RGB和几何先验的聚合LiDAR点云来调节多模态视频扩散模型，为新的视点合成逼真的RGB、深度和语义输出。该合成流水线支持前馈NVS，而无需计算密集型的每个场景优化，提供全面的监督信号来细化3DGS表示，以在极端视点变化下增强渲染鲁棒性。在Open Waymo数据集上的实验表明，MuDG在重建和合成质量方面都优于现有方法。 et.al.|[2503.10604](http://arxiv.org/abs/2503.10604)|null|
|**2025-03-13**|**GroomLight: Hybrid Inverse Rendering for Relightable Human Hair Appearance Modeling**|我们提出了GroomLight，这是一种从多视图图像中重建可照亮头发外观的新方法。现有的头发捕捉方法难以在照片级真实感渲染和重新照明功能之间取得平衡。分析材料模型虽然具有物理基础，但往往无法完全捕捉外观细节。相反，神经渲染方法在视图合成方面表现出色，但在新的照明条件下推广较差。GroomLight通过结合两种范式的优势来应对这一挑战。它采用扩展的头发BSDF模型来捕获主要的光传输，并采用光感知残差模型来重建剩余的细节。我们还提出了一种混合逆渲染管道来优化这两个组件，实现高保真度的重新照明、视图合成和材质编辑。对真实世界头发数据的广泛评估证明了我们方法的最先进性能。 et.al.|[2503.10597](http://arxiv.org/abs/2503.10597)|null|
|**2025-03-13**|**Flow-NeRF: Joint Learning of Geometry, Poses, and Dense Flow within Unified Neural Representations**|由于固有的几何模糊性，在神经辐射场中学习没有姿态先验的精确场景重建具有挑战性。最近的发展要么依赖于对应先验进行正则化，要么使用现成的流估计器来推导分析姿态。然而，在统一的神经表示中联合学习场景几何、相机姿态和密集流的潜力在很大程度上仍未得到探索。在本文中，我们提出了Flow NeRF，这是一个统一的框架，可以同时优化场景几何、相机姿态和密集的光流。为了能够学习神经辐射场内的密集流，我们设计并构建了一个基于姿态的双射映射进行流估计。为了使场景重建受益于流估计，我们开发了一种有效的特征增强机制，将规范空间特征传递给世界空间表示，显著增强了场景几何。我们使用多个数据集在四个重要任务上验证了我们的模型，即新颖的视图合成、深度估计、相机姿态预测和密集光流估计。我们的方法在几乎所有新视图合成和深度估计的度量方面都超越了以前的方法，并产生了定性可靠和定量准确的新视图流。我们的项目页面是https://zhengxunzhi.github.io/flownerf/. et.al.|[2503.10464](http://arxiv.org/abs/2503.10464)|null|
|**2025-03-13**|**3D Student Splatting and Scooping**|最近，3D高斯散点（3DGS）为新颖的视图合成提供了一个新的框架，并在神经渲染和相关应用方面掀起了新的研究浪潮。随着3DGS成为许多模型的基础组件，对3DGS本身的任何改进都可以带来巨大的好处。为此，我们的目标是改进3DGS的基本范式和公式。我们认为，作为一个非正规化的混合模型，它既不需要高斯模型，也不需要飞溅模型。随后，我们提出了一种新的混合模型，该模型由灵活的Student t分布组成，具有正（飞溅）和负（铲起）密度。我们将我们的模型命名为学生飞溅和滑行，或SSS。当提供更好的表现力时，SSS也给学习带来了新的挑战。因此，我们还提出了一种新的优化原则采样方法。通过对多个数据集、设置和指标的详尽评估和比较，我们证明SSS在质量和参数效率方面优于现有方法，例如，用相似数量的组件实现匹配或更好的质量，并在将组件数量减少高达82%的同时获得可比的结果。 et.al.|[2503.10148](http://arxiv.org/abs/2503.10148)|null|
|**2025-03-13**|**GaussHDR: High Dynamic Range Gaussian Splatting via Learning Unified 3D and 2D Local Tone Mapping**|高动态范围（HDR）新视图合成（NVS）旨在通过利用在不同曝光水平下捕获的多视图低动态范围（LDR）图像来重建HDR场景。当前使用3D色调映射的训练范式通常会导致不稳定的HDR重建，而使用2D色调映射进行训练会降低模型拟合LDR图像的能力。此外，现有方法中使用的全局色调映射器可能会阻碍HDR和LDR表示的学习。为了应对这些挑战，我们提出了GaussHDR，它通过3D高斯飞溅统一了3D和2D局部色调映射。具体来说，我们为3D和2D色调映射设计了一个残差局部色调映射器，该映射器接受额外的上下文特征作为输入。然后，我们建议在损失级别组合来自3D和2D局部色调映射的双LDR渲染结果。最后，认识到不同场景可能在双重结果之间表现出不同的平衡，我们引入了不确定性学习，并将不确定性用于自适应调制。大量实验表明，GaussHDR在合成和现实场景中都明显优于最先进的方法。 et.al.|[2503.10143](http://arxiv.org/abs/2503.10143)|null|
|**2025-03-12**|**Hybrid Rendering for Multimodal Autonomous Driving: Merging Neural and Physics-Based Simulation**|近年来，用于自动驾驶仿真的神经重建模型取得了重大进展，动态模型变得越来越普遍。然而，这些模型通常仅限于处理紧跟其原始轨迹的域内对象。我们介绍了一种混合方法，将神经重建的优势与基于物理的渲染相结合。这种方法可以将传统的基于网格的动态代理虚拟放置在任意位置，调整环境条件，并从新的相机视角进行渲染。我们的方法显著提高了新的视图合成质量，特别是对于路面和车道标记，同时通过我们的新训练方法NeRF2GS保持交互式帧率。该技术利用了基于NeRF的方法的卓越泛化能力和3D高斯散斑（3DGS）的实时渲染速度。我们通过在原始图像上训练定制的NeRF模型来实现这一点，该模型具有从嘈杂的LiDAR点云导出的深度正则化，然后将其用作3DGS训练的教师模型。此过程可确保精确的深度、曲面法线和相机外观建模作为监督。通过我们基于块的训练并行化，该方法可以处理大规模重建（大于或等于100000平方米），并预测分割掩模、表面法线和深度图。在模拟过程中，它支持基于光栅化的渲染后端，具有基于深度的构图和多个相机模型，用于实时相机模拟，以及用于精确LiDAR模拟的光线追踪后端。 et.al.|[2503.09464](http://arxiv.org/abs/2503.09464)|null|
|**2025-03-12**|**Close-up-GS: Enhancing Close-Up View Synthesis in 3D Gaussian Splatting with Progressive Self-Training**|3D高斯散斑（3DGS）在给定视点集上训练后，在合成新视图方面表现出了令人印象深刻的性能。然而，当合成视图明显偏离训练视图时，其渲染质量会恶化。这种下降是由于（1）模型难以推广到分布外的场景，以及（2）由于分辨率的大幅变化和遮挡导致的插值精细细节的挑战。这种限制的一个显著例子是特写视图生成——生成的视图比训练集中的视图更接近对象。为了解决这个问题，我们提出了一种基于逐步用自生成数据训练3DGS模型的特写视图生成新方法。我们的解决方案基于三个关键思想。首先，我们利用最近推出的3D感知生成模型See3D来增强渲染视图的细节。其次，我们提出了一种策略，逐步扩大3DGS模型的“信任区域”，并更新See3D的一组参考视图。最后，我们引入了一种微调策略，用上述方案生成的训练数据仔细更新3DGS模型。我们进一步定义了特写视图评估的指标，以促进对这个问题的更好研究。通过对特写镜头的特定场景进行评估，我们提出的方法比竞争解决方案具有明显的优势。 et.al.|[2503.09396](http://arxiv.org/abs/2503.09396)|null|
|**2025-03-12**|**Better Together: Unified Motion Capture and 3D Avatar Reconstruction**|我们提出了Better Together，这是一种同时解决人体姿态估计问题的方法，同时从多视图视频中重建逼真的3D人体化身。虽然现有技术通常单独解决这些问题，但我们认为，使用3D可渲染身体模型对骨骼运动进行联合优化会带来协同效应，即产生更精确的运动捕捉和提高化身实时渲染的视觉质量。为了实现这一目标，我们引入了一种新型的可动画化化身，其3D高斯模型被装配在个性化网格上，并建议使用时间依赖的MLP来优化运动序列，以提供准确和时间一致的姿态估计。我们首先在极具挑战性的瑜伽姿势上评估了我们的方法，并展示了多视图人体姿势估计的最新精度，与基于关键点的方法相比，身体关节和手关节的误差分别降低了35%和45%。同时，我们的方法在各种具有挑战性的主题上显著提高了可动画化身的视觉质量（新颖视图合成时为+2dB PSNR）。 et.al.|[2503.09293](http://arxiv.org/abs/2503.09293)|null|
|**2025-03-11**|**GarmentCrafter: Progressive Novel View Synthesis for Single-View 3D Garment Reconstruction and Editing**|我们介绍GarmentCrafter，这是一种新方法，使非专业用户能够从单视图图像创建和修改3D服装。虽然图像生成的最新进展促进了2D服装设计，但创建和编辑3D服装对非专业用户来说仍然具有挑战性。现有的单视图3D重建方法通常依赖于预训练的生成模型来合成基于参考图像和相机姿态的新视图，但它们缺乏跨视图一致性，无法捕捉不同视图之间的内部关系。在本文中，我们通过渐进式深度预测和图像扭曲来近似新视图，从而解决了这一挑战。随后，我们训练了一个多视图扩散模型，以完成遮挡和未知的服装区域，并由不断变化的相机姿态提供信息。通过联合推断RGB和深度，GarmentCrafter增强了视图间的连贯性，并重建了精确的几何形状和精细的细节。大量实验表明，与最先进的单视图3D服装重建方法相比，我们的方法实现了更高的视觉保真度和视点间一致性。 et.al.|[2503.08678](http://arxiv.org/abs/2503.08678)|null|
|**2025-03-11**|**X-Field: A Physically Grounded Representation for 3D X-ray Reconstruction**|X射线成像在医学诊断中不可或缺，但由于潜在的健康风险，其使用受到严格监管。为了减少辐射暴露，最近的研究侧重于从稀疏输入中生成新的视图，并重建计算机断层扫描（CT）体积，借用3D重建区域的表示。然而，这些表示最初针对的是强调反射和散射效应的可见光成像，而忽略了X射线成像的穿透和衰减特性。在本文中，我们介绍了X-Field，这是第一个专门为X射线成像设计的3D表示，其根源在于不同材料的能量吸收率。为了准确模拟内部结构中的各种材料，我们采用了具有不同衰减系数的3D椭球体。为了估算每种材料对X射线的能量吸收，我们设计了一种有效的路径分割算法，该算法考虑了复杂的椭球交点。我们进一步提出了混合渐进初始化来提高X-Filed的几何精度，并结合基于材料的优化来增强沿材料边界的模型拟合。实验表明，X-Field在真实世界的人体器官和合成对象数据集上都实现了卓越的视觉保真度，在X射线新视图合成和CT重建方面优于最先进的方法。 et.al.|[2503.08596](http://arxiv.org/abs/2503.08596)|null|

<p align=right>(<a href=#updated-on-20250316>back to top</a>)</p>

## 3D Reconstruction

|Publish Date|Title|Abstract|PDF|Code|
|---|---|---|---|---|
|**2025-03-13**|**OSMa-Bench: Evaluating Open Semantic Mapping Under Varying Lighting Conditions**|开放语义映射（OSM）是机器人感知的关键技术，结合了语义分割和SLAM技术。本文介绍了一种用于评估OSM解决方案的动态可配置和高度自动化的LLM/LVLM驱动管道，称为OSMa Bench（开放语义映射基准）。该研究侧重于评估不同室内照明条件下最先进的语义映射算法，这是室内环境中的一个关键挑战。我们介绍了一种新的数据集，其中包含模拟的RGB-D序列和地面真实3D重建，有助于对不同光照条件下的映射性能进行严格分析。通过在ConceptGraphs、BBQ和OpenScene等领先模型上的实验，我们评估了对象识别和分割的语义保真度。此外，我们引入了一种场景图评估方法来分析模型解释语义结构的能力。这些结果为这些模型的鲁棒性提供了见解，为开发有弹性和适应性的机器人系统形成了未来的研究方向。我们的代码可在https://be2rlab.github.io/OSMa-Bench/. et.al.|[2503.10331](http://arxiv.org/abs/2503.10331)|null|
|**2025-03-13**|**Deep Learning-Based Direct Leaf Area Estimation using Two RGBD Datasets for Model Development**|单叶面积的估计可以作为作物生长的衡量标准，也是培育新品种的表型特征。它也被用于测量叶面积指数和总叶面积。一些研究使用手持相机、图像处理3D重建和基于无监督学习的方法来估计植物图像中的叶面积。深度学习在目标检测和分割任务中表现良好；然而，还没有对目标的直接面积估计进行探索。这项工作研究了基于深度学习的叶面积估计，用于在真实场景中使用移动相机设置拍摄的RGBD图像。收集了用顶角视图捕获的附着叶子数据集和分离的单叶数据集，用于模型开发和测试。首先，在人工分割的叶子上测试了基于图像处理的面积估计。然后研究了基于Mask R-CNN的模型，并对其进行了修改，以接受RGBD图像并估计叶面积。然后将分离的叶子数据集与附加的叶子植物数据集混合，以估计植物图像的单叶面积，并提出了另一种具有两个主干的网络设计：一个用于分割，另一个用于面积估计。在超参数调优中使用了敏捷方法，而不是尝试所有可能性或随机值。最终的模型用5倍进行了交叉验证，并用两个看不见的数据集进行了测试：分离和附着的叶子。在看不见的离体叶片数据上，90%IoA的分割结果的F1得分为1.0，而面积估计的R平方为0.81。对于看不见的植物数据分割，IoA为90%的F1得分为0.59，而R平方得分为0.57。研究建议使用带有地面真实区域的附着叶子来提高结果。 et.al.|[2503.10129](http://arxiv.org/abs/2503.10129)|null|
|**2025-03-13**|**AI-assisted 3D Preservation and Reconstruction of Temple Arts**|人工智能如何在保护中与过去联系起来？17年前的照片对重新保护有什么帮助？本研究旨在使用人工智能将两者连接起来，从台湾云林宫的图像数据中无缝重建遗产。人工智能辅助的3D建模用于在Postshot或KIRI引擎生成的3DGS或NeRF模型的不同3D平台上重建相应的细节。Zephyr的多边形或点模型被分为两组进行参考和评估。结果还包括基于稳定扩散和后拍动画的AI辅助建模结果。人工智能中不断发展的文档和解释呈现了一种新的工作流程安排，这是由资源、格式和界面的新结构和管理所促成的，是一种持续的保护工作。 et.al.|[2503.10031](http://arxiv.org/abs/2503.10031)|null|
|**2025-03-13**|**MetricGrids: Arbitrary Nonlinear Approximation with Elementary Metric Grids based Implicit Neural Representation**|本文介绍了MetricGrids，这是一种基于网格的神经表示方法，它将各种度量空间中的基本度量网格组合在一起，以近似复杂的非线性信号。虽然基于网格的表示因其效率和可扩展性而被广泛采用，但现有的具有连续空间点线性索引的特征网格只能提供退化的线性潜在空间表示，并且这种表示不能通过以下紧凑的解码器充分补偿来表示复杂的非线性信号。为了在保持规则网格结构简单性的同时解决这个问题，我们的方法建立在基于标准网格的范式之上，根据泰勒展开原理，将多个基本度量网格构建为高阶项来近似复杂的非线性。此外，我们通过基于网格不同稀疏度的哈希编码来提高模型的紧凑性，以防止有害的哈希冲突，并使用高阶外推解码器来降低显式网格存储要求。2D和3D重建的实验结果表明，所提出的方法在不同信号类型上具有优异的拟合和渲染精度，验证了其鲁棒性和可推广性。代码可在以下网址获得https://github.com/wangshu31/MetricGrids}{https://github.com/wangshu31/MetricGrids. et.al.|[2503.10000](http://arxiv.org/abs/2503.10000)|null|
|**2025-03-13**|**Reference-Free 3D Reconstruction of Brain Dissection Photographs with Machine Learning**|神经病理学与MRI的相关性有可能将病理学的微观特征转移到体内扫描中。最近，提出了一种经典的配准方法，从大脑库中常规拍摄的3D重建解剖照片堆中建立这些相关性。这些照片绕过了体外MRI的需要，而体外MRI并不普及。然而，这种方法需要一整堆脑板和一个参考掩模（例如，用表面扫描仪获取），这严重限制了该技术的适用性。在这里，我们提出了RefFree，一种无需外部参考的解剖照片重建方法。RefFree是一种学习方法，它估计每张照片中每个像素在图集空间中的3D坐标；然后可以使用简单的最小二乘拟合来计算3D重建。作为副产品，RefFree还可以对重建的堆栈进行基于图集的分割。RefFree基于数字切片3D MRI数据生成的合成照片进行训练，具有随机外观以增强泛化能力。对模拟和真实数据的实验表明，RefFree在没有显式引用的情况下实现了与基线方法相当的性能，同时也能够重建部分堆栈。我们的代码可在https://github.com/lintian-a/reffree. et.al.|[2503.09963](http://arxiv.org/abs/2503.09963)|null|
|**2025-03-13**|**WonderVerse: Extendable 3D Scene Generation with Video Generative Models**|我们介绍\textit{WonderVerse}，这是一个简单但有效的生成可扩展3D场景的框架。与依赖于迭代深度估计和图像修复的现有方法不同，WonderVerse利用嵌入在视频生成基础模型中的强大的世界级先验来创建高度沉浸式和几何连贯的3D环境。此外，我们提出了一种新的可控3D场景扩展技术，以大幅增加生成环境的规模。此外，我们引入了一种新的异常序列检测模块，该模块利用相机轨迹来解决生成视频中的几何不一致问题。最后，WonderVerse与各种3D重建方法兼容，可以实现高效和高质量的生成。对3D场景生成的广泛实验表明，我们的WonderVerse具有优雅而简单的管道，可提供可扩展且高度逼真的3D场景，明显优于依赖更复杂架构的现有作品。 et.al.|[2503.09160](http://arxiv.org/abs/2503.09160)|null|
|**2025-03-11**|**Acoustic Neural 3D Reconstruction Under Pose Drift**|我们考虑了使用漂移传感器姿态收集的声学图像优化神经隐式曲面进行3D重建的问题。当前最先进的3D声学建模算法的准确性高度依赖于精确的姿态估计；传感器姿态的微小误差可能会导致严重的重建伪影。本文提出了一种联合优化神经场景表示和声纳姿态的算法。我们的算法通过将6DoF姿态参数化为可学习的参数，并通过神经渲染器和隐式表示反向传播梯度来实现这一点。我们在真实和模拟数据集上验证了我们的算法。即使在明显的姿态漂移下，它也能产生高保真的3D重建。 et.al.|[2503.08930](http://arxiv.org/abs/2503.08930)|null|
|**2025-03-11**|**GarmentCrafter: Progressive Novel View Synthesis for Single-View 3D Garment Reconstruction and Editing**|我们介绍GarmentCrafter，这是一种新方法，使非专业用户能够从单视图图像创建和修改3D服装。虽然图像生成的最新进展促进了2D服装设计，但创建和编辑3D服装对非专业用户来说仍然具有挑战性。现有的单视图3D重建方法通常依赖于预训练的生成模型来合成基于参考图像和相机姿态的新视图，但它们缺乏跨视图一致性，无法捕捉不同视图之间的内部关系。在本文中，我们通过渐进式深度预测和图像扭曲来近似新视图，从而解决了这一挑战。随后，我们训练了一个多视图扩散模型，以完成遮挡和未知的服装区域，并由不断变化的相机姿态提供信息。通过联合推断RGB和深度，GarmentCrafter增强了视图间的连贯性，并重建了精确的几何形状和精细的细节。大量实验表明，与最先进的单视图3D服装重建方法相比，我们的方法实现了更高的视觉保真度和视点间一致性。 et.al.|[2503.08678](http://arxiv.org/abs/2503.08678)|null|
|**2025-03-11**|**Language-Depth Navigated Thermal and Visible Image Fusion**|深度引导多模态融合结合了可见光和红外图像的深度信息，显著提高了3D重建和机器人应用的性能。现有的热-可见光图像融合主要侧重于检测任务，忽略了深度等其他关键信息。通过解决低光和复杂环境中单一模态的局限性，融合图像的深度信息不仅生成了更准确的点云数据，提高了3D重建的完整性和精度，还为机器人导航、定位和环境感知提供了全面的场景理解。这支持在自动驾驶和救援任务等应用中的精确识别和高效操作。我们介绍了一种文本引导和深度驱动的红外和可见光图像融合网络。该模型由一个图像融合分支和两个辅助深度估计分支组成，图像融合分支用于通过扩散模型提取多通道互补信息，并配备了文本引导模块。融合分支使用CLIP从深度丰富的图像描述中提取语义信息和参数，以指导扩散模型提取多通道特征并生成融合图像。然后将这些融合图像输入到深度估计分支中，以计算深度驱动损失，优化图像融合网络。该框架旨在整合视觉语言和深度，直接从多模态输入中生成彩色融合图像。 et.al.|[2503.08676](http://arxiv.org/abs/2503.08676)|null|
|**2025-03-11**|**X-Field: A Physically Grounded Representation for 3D X-ray Reconstruction**|X射线成像在医学诊断中不可或缺，但由于潜在的健康风险，其使用受到严格监管。为了减少辐射暴露，最近的研究侧重于从稀疏输入中生成新的视图，并重建计算机断层扫描（CT）体积，借用3D重建区域的表示。然而，这些表示最初针对的是强调反射和散射效应的可见光成像，而忽略了X射线成像的穿透和衰减特性。在本文中，我们介绍了X-Field，这是第一个专门为X射线成像设计的3D表示，其根源在于不同材料的能量吸收率。为了准确模拟内部结构中的各种材料，我们采用了具有不同衰减系数的3D椭球体。为了估算每种材料对X射线的能量吸收，我们设计了一种有效的路径分割算法，该算法考虑了复杂的椭球交点。我们进一步提出了混合渐进初始化来提高X-Filed的几何精度，并结合基于材料的优化来增强沿材料边界的模型拟合。实验表明，X-Field在真实世界的人体器官和合成对象数据集上都实现了卓越的视觉保真度，在X射线新视图合成和CT重建方面优于最先进的方法。 et.al.|[2503.08596](http://arxiv.org/abs/2503.08596)|null|

<p align=right>(<a href=#updated-on-20250316>back to top</a>)</p>

## Diffusion

|Publish Date|Title|Abstract|PDF|Code|
|---|---|---|---|---|
|**2025-03-13**|**GoT: Unleashing Reasoning Capability of Multimodal Large Language Model for Visual Generation and Editing**|当前的图像生成和编辑方法主要将文本提示作为直接输入进行处理，而不考虑视觉构图和显式操作。我们提出了生成思维链（GoT），这是一种新颖的范式，可以在输出图像之前通过显式的语言推理过程进行生成和编辑。这种方法将传统的文本到图像生成和编辑转换为分析语义关系和空间排列的推理引导框架。我们定义了GoT的公式，并构建了包含超过900万个样本的大规模GoT数据集，其中包含捕获语义空间关系的详细推理链。为了利用GoT的优势，我们实现了一个统一的框架，该框架将用于推理链生成的Qwen2.5-VL与我们新颖的语义空间指导模块增强的端到端扩散模型集成在一起。实验表明，我们的GoT框架在生成和编辑任务上都取得了出色的性能，比基线有了显著改进。此外，我们的方法支持交互式视觉生成，允许用户明确修改推理步骤以进行精确的图像调整。GoT开创了推理驱动的视觉生成和编辑的新方向，生成了更符合人类意图的图像。为了促进未来的研究，我们将我们的数据集、代码和预训练模型公开在https://github.com/rongyaofang/GoT. et.al.|[2503.10639](http://arxiv.org/abs/2503.10639)|null|
|**2025-03-13**|**Studying Classifier(-Free) Guidance From a Classifier-Centric Perspective**|无分类器引导已成为去噪扩散模型条件生成的主要方法。然而，对无分类器引导的全面理解仍然缺失。在这项工作中，我们进行了一项实证研究，为无分类器指导提供了一个新的视角。具体来说，我们不是只关注无分类器的引导，而是追溯到根源，即分类器引导，找出推导的关键假设，并进行系统研究以了解分类器的作用。我们发现，分类器引导和无分类器引导都是通过将去噪扩散轨迹推离决策边界来实现条件生成的，即条件信息通常纠缠且难以学习的区域。基于这种以分类器为中心的理解，我们提出了一种基于流匹配的通用后处理步骤，以缩小预训练去噪扩散模型的学习分布与实际数据分布之间的差距，主要是在决策边界附近。在各种数据集上的实验验证了所提出方法的有效性。 et.al.|[2503.10638](http://arxiv.org/abs/2503.10638)|null|
|**2025-03-13**|**Distilling Diversity and Control in Diffusion Models**|蒸馏扩散模型存在一个关键的局限性：与基础模型相比，样本多样性降低。在这项工作中，我们发现，尽管存在这种多样性损失，但蒸馏模型保留了基础模型的基本概念表示。我们演示了控制蒸馏——在基础模型上训练的概念滑块和LoRA等控制机制可以无缝地转移到蒸馏模型，反之亦然，无需任何再训练即可有效地蒸馏控制。这种表征结构的保留促使我们研究了蒸馏过程中多样性崩溃的机制。为了了解蒸馏如何影响多样性，我们引入了扩散目标（DT）可视化，这是一种分析和调试工具，可以揭示模型如何在中间步骤预测最终输出。通过DT可视化，我们识别出生成伪影、不一致性，并证明初始扩散时间步长不成比例地决定了输出多样性，而后续步骤主要是细化细节。基于这些见解，我们引入了多样性蒸馏——一种混合推理方法，在过渡到高效蒸馏模型之前，仅在第一个关键时间步战略性地使用基础模型。我们的实验表明，这种简单的修改不仅恢复了从基础到蒸馏模型的多样性能力，而且出乎意料地超过了它，同时几乎保持了蒸馏推理的计算效率，所有这些都不需要额外的训练或模型修改。我们的代码和数据可在https://distillation.baulab.info et.al.|[2503.10637](http://arxiv.org/abs/2503.10637)|null|
|**2025-03-13**|**V2Edit: Versatile Video Diffusion Editor for Videos and 3D Scenes**|本文介绍了V $^2$Edit，这是一种用于指令引导视频和3D场景编辑的新型无训练框架。为了应对平衡原始内容保存与编辑任务完成的关键挑战，我们的方法采用了一种渐进策略，将复杂的编辑任务分解为一系列更简单的子任务。每个子任务都通过三个关键的协同机制进行控制：初始噪声、在每个去噪步骤添加的噪声以及文本提示和视频内容之间的交叉注意力图。这确保了原始视频元素的稳健保存，同时有效地应用了所需的编辑。除了其原生视频编辑功能外，我们还通过“渲染-编辑-重建”过程将V$^2$Edit扩展到3D场景编辑，即使对于涉及大量几何变化（如对象插入）的任务，也能进行高质量、3D一致的编辑。大量实验表明，我们的V$^2$ Edit在各种具有挑战性的视频编辑任务和复杂的3D场景编辑任务中实现了高质量和成功的编辑，从而在这两个领域建立了最先进的性能。 et.al.|[2503.10634](http://arxiv.org/abs/2503.10634)|null|
|**2025-03-13**|**HybridVLA: Collaborative Diffusion and Autoregression in a Unified Vision-Language-Action Model**|用于常识推理的视觉语言模型（VLM）的最新进展导致了视觉语言动作（VLA）模型的发展，使机器人能够执行广义操作。尽管现有的自回归VLA方法利用了大规模的预训练知识，但它们破坏了动作的连续性。同时，一些VLA方法加入了一个额外的扩散头来预测连续动作，仅依赖VLM提取的特征，这限制了它们的推理能力。在本文中，我们介绍了HybridVLA，这是一个统一的框架，它将自回归和扩散策略的优势无缝集成到一个大型语言模型中，而不是简单地将它们连接起来。为了弥合代沟，提出了一种协作训练方案，将扩散建模直接注入到下一个令牌预测中。通过这个配方，我们发现这两种形式的动作预测不仅相互强化，而且在不同的任务中表现出不同的性能。因此，我们设计了一种协作动作集成机制，自适应地融合这两个预测，从而实现更稳健的控制。在实验中，HybridVLA在各种模拟和现实世界任务中表现优于以前最先进的VLA方法，包括单臂和双臂机器人，同时在以前看不到的配置中展示了稳定的操纵。 et.al.|[2503.10631](http://arxiv.org/abs/2503.10631)|null|
|**2025-03-13**|**NIL: No-data Imitation Learning by Leveraging Pre-trained Video Diffusion Models**|在包括人形机器人、四足动物和动物在内的各种非传统形态中获得物理上合理的运动技能对于推进角色模拟和机器人技术至关重要。传统的方法，如强化学习（RL），是特定于任务和身体的，需要大量的奖励函数工程，并且不能很好地推广。模仿学习提供了一种替代方法，但严重依赖于高质量的专家演示，这对于非人类形态来说很难获得。另一方面，视频扩散模型能够生成各种形态的逼真视频，从人类到蚂蚁。利用这一能力，我们提出了一种独立于数据的技能获取方法，该方法从2D生成的视频中学习3D运动技能，并具有对非传统和非人类形式的泛化能力。具体来说，我们通过计算视频嵌入之间的成对距离，利用视觉变换器进行基于视频的比较，从而指导模仿学习过程。除了视频编码距离，我们还使用分段视频帧之间的计算相似度作为指导奖励。我们在涉及独特身体配置的运动任务中验证了我们的方法。在类人机器人运动任务中，我们证明了“无数据模仿学习”（NIL）优于基于3D运动捕捉数据训练的基线。我们的研究结果强调了利用生成视频模型进行具有不同形态的物理上合理的技能学习的潜力，有效地用数据生成代替数据收集进行模仿学习。 et.al.|[2503.10626](http://arxiv.org/abs/2503.10626)|null|
|**2025-03-13**|**DiT-Air: Revisiting the Efficiency of Diffusion Model Architecture Design in Text to Image Generation**|在这项工作中，我们实证研究了用于文本到图像生成的扩散变换器（DiTs），重点研究了架构选择、文本调节策略和训练协议。我们评估了一系列基于DiT的架构，包括PixArt风格和MMDiT变体，并将其与直接处理级联文本和噪声输入的标准DiT变体进行了比较。令人惊讶的是，我们的研究结果表明，标准DiT的性能与那些专业模型相当，同时表现出卓越的参数效率，尤其是在扩大规模时。利用分层参数共享策略，与MMDiT架构相比，我们的模型大小进一步减少了66%，对性能的影响最小。在深入分析文本编码器和变分自动编码器（VAE）等关键组件的基础上，我们介绍了DiT Air和DiT Air Lite。通过监督和奖励微调，DiT Air在GenEval和T2I CompBench上实现了最先进的性能，而DiT Air Lite尽管体积小巧，但仍然具有很强的竞争力，超过了大多数现有型号。 et.al.|[2503.10618](http://arxiv.org/abs/2503.10618)|null|
|**2025-03-13**|**ConsisLoRA: Enhancing Content and Style Consistency for LoRA-based Style Transfer**|样式转移涉及将样式从参考图像转移到目标图像的内容。基于LoRA（低秩自适应）方法的最新进展在有效捕获单个图像的风格方面显示出了希望。然而，这些方法仍然面临着重大挑战，如内容不一致、风格不一致和内容泄漏。本文全面分析了标准扩散参数化在风格转换背景下学习预测噪声的局限性。为了解决这些问题，我们引入了ConsisLoRA，这是一种基于LoRA的方法，通过优化LoRA权重来预测原始图像而不是噪声，从而增强内容和风格的一致性。我们还提出了一种两步训练策略，将内容和风格的学习与参考图像解耦。为了有效地捕捉内容图像的全局结构和局部细节，我们引入了逐步损失转换策略。此外，我们提出了一种推理指导方法，可以在推理过程中持续控制内容和风格强度。通过定性和定量评估，我们的方法在内容和风格一致性方面取得了显著改善，同时有效地减少了内容泄露。 et.al.|[2503.10614](http://arxiv.org/abs/2503.10614)|null|
|**2025-03-13**|**CoSTA $\ast$ : Cost-Sensitive Toolpath Agent for Multi-turn Image Editing**|像稳定扩散和DALLE-3这样的文本到图像模型仍然难以进行多轮图像编辑。我们将这样的任务分解为工具使用的代理工作流（路径），该工作流通过不同成本的人工智能工具处理一系列子任务。传统的搜索算法需要昂贵的探索来找到刀具路径。虽然大型语言模型（LLM）拥有子任务规划的先验知识，但它们可能缺乏对工具能力和成本的准确估计，以确定在每个子任务中应用哪些工具。我们能否结合LLM和图搜索的优势来找到具有成本效益的刀具路径？我们提出了一种三阶段方法“CoSTA*”，该方法利用LLM创建子任务树，帮助修剪给定任务的AI工具图，然后在小子图上进行a*搜索以找到工具路径。为了更好地平衡总成本和质量，CoSTA*结合了每个子任务中每个工具的两个指标来指导A*搜索。然后，每个子任务的输出都由视觉语言模型（VLM）进行评估，其中故障将触发子任务上工具成本和质量的更新。因此，A*搜索可以快速从失败中恢复，以探索其他路径。此外，CoSTA*可以在子任务之间自动切换模式，以实现更好的成本-质量权衡。我们建立了一个具有挑战性的多回合图像编辑的新基准，在这个基准上，CoSTA＊在成本和质量方面都优于最先进的图像编辑模型或代理，并根据用户偏好进行多种权衡。 et.al.|[2503.10613](http://arxiv.org/abs/2503.10613)|**[link](https://github.com/tianyi-lab/CoSTAR)**|
|**2025-03-13**|**MuDG: Taming Multi-modal Diffusion with Gaussian Splatting for Urban Scene Reconstruction**|最近在辐射领域的突破显著推进了自动驾驶中的3D场景重建和新颖视图合成（NVS）。然而，关键的局限性仍然存在：基于重建的方法在与训练轨迹的显著视点偏差下表现出显著的性能下降，而基于生成的技术在时间连贯性和精确的场景可控性方面存在困难。为了克服这些挑战，我们提出了MuDG，这是一个创新的框架，将多模态扩散模型与高斯散斑（GS）相结合，用于城市场景重建。MuDG利用具有RGB和几何先验的聚合LiDAR点云来调节多模态视频扩散模型，为新的视点合成逼真的RGB、深度和语义输出。该合成流水线支持前馈NVS，而无需计算密集型的每个场景优化，提供全面的监督信号来细化3DGS表示，以在极端视点变化下增强渲染鲁棒性。在Open Waymo数据集上的实验表明，MuDG在重建和合成质量方面都优于现有方法。 et.al.|[2503.10604](http://arxiv.org/abs/2503.10604)|null|

<p align=right>(<a href=#updated-on-20250316>back to top</a>)</p>

## NeRF

|Publish Date|Title|Abstract|PDF|Code|
|---|---|---|---|---|
|**2025-03-13**|**RSR-NF: Neural Field Regularization by Static Restoration Priors for Dynamic Imaging**|动态成像涉及使用欠采样测量值随时重建时空对象。特别是，在动态计算机断层扫描（dCT）中，一次只能获得一个视角的单个投影，这使得逆问题非常具有挑战性。此外，地面实况动态数据通常要么不可用，要么太稀缺，无法用于监督学习技术。为了解决这个问题，我们提出了RSR-NF，它使用神经场（NF）来表示动态对象，并使用去噪正则化（RED）框架，通过学习的恢复算子将额外的静态深空间先验合并到变分公式中。我们使用基于ADMM的可变分裂算法来有效地优化变分目标。我们将RSR-NF与三种替代方案进行了比较：仅具有时间正则化的NF；最近的一种方法，使用对静态数据进行预训练的去噪器，将部分可分离的低秩表示与RED相结合；以及基于深度图像先验的模型。第一个比较展示了通过将NF表示与静态恢复先验相结合所实现的重建改进，而另外两个则展示了与dCT的最新技术相比的改进。 et.al.|[2503.10015](http://arxiv.org/abs/2503.10015)|null|
|**2025-03-11**|**Representing 3D Shapes With 64 Latent Vectors for 3D Diffusion Models**|通过变分自编码器（VAE）构建压缩的潜在空间是高效3D扩散模型的关键。本文介绍了COD-VAE，这是一种在不牺牲质量的情况下将3D形状编码为1D潜在向量的COmpact集的VAE。COD-VAE引入了一种两级自动编码器方案，以提高压缩和解码效率。首先，我们的编码器块通过中间点补丁将点云逐步压缩为紧凑的潜在向量。其次，我们的基于三平面的解码器从潜在向量重建密集的三平面，而不是直接解码神经场，大大降低了神经场解码的计算开销。最后，我们提出了不确定性引导的令牌修剪，通过在更简单的区域跳过计算来自适应地分配资源，提高了解码器的效率。实验结果表明，与基线相比，COD-VAE在保持质量的同时实现了16倍的压缩。这使得生成速度提高了20.8倍，突显出大量潜在矢量不是高质量重建和生成的先决条件。 et.al.|[2503.08737](http://arxiv.org/abs/2503.08737)|null|
|**2025-03-09**|**Gaussian RBFNet: Gaussian Radial Basis Functions for Fast and Accurate Representation and Reconstruction of Neural Fields**|DeepSDF和神经辐射场等神经场最近彻底改变了RGB图像和视频的新颖视图合成和3D重建。然而，实现高质量的表示、重建和渲染需要深度神经网络，而深度神经网络的训练和评估速度很慢。尽管已经提出了几种加速技术，但它们经常以速度换取内存。另一方面，基于高斯飞溅的方法加快了渲染时间，但在存储大量高斯参数所需的训练速度和内存方面仍然成本高昂。在本文中，我们介绍了一种新的神经表示方法，它在训练和推理时间都很快，而且很轻。我们的关键观察是，传统MLP中使用的神经元执行简单的计算（点积，然后是ReLU激活），因此需要使用宽和深MLP或高分辨率和高维特征网格来参数化复杂的非线性函数。我们在这篇论文中表明，通过用径向基函数（RBF）核替换传统神经元，只需一层这样的神经元，就可以实现2D（RGB图像）、3D（几何）和5D（辐射场）信号的高精度表示。该表示具有高度的并行性，可在低分辨率特征网格上运行，并且结构紧凑，内存高效。我们证明，所提出的新表示可以在不到15秒的时间内训练出3D几何表示，在不到十五分钟的时间内就可以训练出新的视图合成。在运行时，它可以在不牺牲质量的情况下以超过60 fps的速度合成新颖的视图。 et.al.|[2503.06762](http://arxiv.org/abs/2503.06762)|null|
|**2025-03-09**|**X-LRM: X-ray Large Reconstruction Model for Extremely Sparse-View Computed Tomography Recovery in One Second**|稀疏视图3D CT重建旨在从有限数量的2D X射线投影中恢复体积结构。现有的前馈方法受到基于CNN的架构容量有限和大规模训练数据集稀缺的限制。本文提出了一种用于极稀疏视图（<10视图）CT重建的X射线大重建模型（X-LRM）。X-LRM由两个关键部件组成：X-former和X-triplane。我们的X-former可以使用基于MLP的图像标记器和基于Transformer的编码器来处理任意数量的输入视图。然后，输出标记被上采样到我们的X三平面表示中，该表示将3D辐射密度建模为隐式神经场。为了支持X-LRM的训练，我们引入了Torso-16K，这是一个由各种躯干器官的16K多个体积投影对组成的大规模数据集。大量实验表明，X-LRM的性能比最先进的方法高出1.5 dB，速度快27倍，灵活性更好。此外，肺部分割任务的下游评估也表明了我们方法的实用价值。我们的代码、预训练模型和数据集将于https://github.com/caiyuanhao1998/X-LRM et.al.|[2503.06382](http://arxiv.org/abs/2503.06382)|null|
|**2025-03-05**|**Distilling Dataset into Neural Field**|利用大规模数据集对于训练高性能深度学习模型至关重要，但它也带来了巨大的计算和存储成本。为了克服这些挑战，数据集蒸馏已成为一种有前景的解决方案，它将大规模数据集压缩成一个较小的合成数据集，保留了训练所需的基本信息。本文提出了一种新的数据集提取参数化框架，称为神经场提取数据集（DDiF），它利用神经场存储大规模数据集的必要信息。由于神经场以坐标作为输入和输出量的独特性质，DDiF有效地保留了信息，并易于生成各种形状的数据。我们从理论上证实，当单个合成实例的使用预算相同时，DDiF表现出比以前的一些文献更大的表现力。通过广泛的实验，我们证明DDiF在几个基准数据集上取得了卓越的性能，扩展到图像域之外，包括视频、音频和3D体素。我们在发布代码https://github.com/aailab-kaist/DDiF. et.al.|[2503.04835](http://arxiv.org/abs/2503.04835)|null|
|**2025-02-27**|**RANGE: Retrieval Augmented Neural Fields for Multi-Resolution Geo-Embeddings**|地理位置表示的选择会显著影响各种地理空间任务模型的准确性，包括细粒度物种分类、种群密度估计和生物群落分类。最近的作品，如SatCLIP和GeoCLIP，通过将地理位置与共置图像进行对比对齐来学习这种表示。虽然这些方法非常有效，但在本文中，我们认为当前的训练策略未能完全捕捉到重要的视觉特征。我们从信息论的角度解释了为什么这些方法产生的嵌入会丢弃对许多下游任务很重要的关键视觉信息。为了解决这个问题，我们提出了一种新的检索增强策略，称为RANGE。我们的方法基于这样一种直觉，即可以通过组合来自多个看起来相似的位置的视觉特征来估计位置的视觉特性。我们在各种各样的任务中评估我们的方法。我们的结果表明，RANGE在大多数任务中表现优于现有的最先进的模型，并具有显著的优势。我们显示，分类任务的收益高达13.1%，回归任务的收益为0.145 $R^2$ 。我们所有的代码都将在GitHub上发布。我们的模型将在HuggingFace上发布。 et.al.|[2502.19781](http://arxiv.org/abs/2502.19781)|null|
|**2025-03-04**|**MedFuncta: Modality-Agnostic Representations Based on Efficient Neural Fields**|最近关于深度学习医学图像分析的研究几乎完全集中在基于网格或体素的数据表示上。我们通过引入MedFuncta来挑战这一常见选择，MedFuncta是一种基于神经场的模态无关连续数据表示。我们演示了如何通过利用医学信号中的冗余以及应用具有上下文缩减方案的高效元学习方法，将神经场从单个实例扩展到大型数据集。我们通过引入 $\omega_0$ -调度，提高重建质量和收敛速度，进一步解决了常用SIREN激活中的光谱偏差问题。我们在各种不同维度和模式的医学信号上验证了我们提出的方法（1D：心电图；2D：胸部X射线、视网膜OCT、眼底照相机、皮肤镜、结肠组织病理学、细胞显微镜；3D：脑MRI、肺CT），并成功证明我们可以解决这些表示的相关下游任务。我们还发布了一个超过550k个带注释神经场的大规模数据集，以促进这方面的研究。 et.al.|[2502.14401](http://arxiv.org/abs/2502.14401)|**[link](https://github.com/pfriedri/medfuncta)**|
|**2025-02-15**|**Implicit Neural Representations of Molecular Vector-Valued Functions**|分子有各种计算表示，包括数值描述符、字符串、图形、点云和曲面。每种表示方法都可以应用各种机器学习方法，从线性回归到与大型语言模型配对的图神经网络。为了补充现有的表示，我们通过向量值函数或n维向量场引入分子的表示，这些向量值函数由神经网络参数化，我们称之为分子神经场。与表面表征不同，分子神经场捕获蛋白质等大分子的外部特征和疏水核心。与离散图或点表示相比，分子神经场结构紧凑，分辨率无关，天生适合在空间和时间维度上进行插值。分子神经场继承的这些特性适用于包括基于所需形状、结构和组成生成分子，以及空间和时间中分子构象之间分辨率无关的插值在内的任务。在这里，我们为分子神经场提供了一个框架和概念证明，即使用自动解码器架构对蛋白质-配体复合物进行参数化和超分辨率重建，以及使用自动编码器架构将分子体积嵌入潜在空间。 et.al.|[2502.10848](http://arxiv.org/abs/2502.10848)|**[link](https://github.com/daenuprobst/minf)**|
|**2025-02-05**|**Poisson Hypothesis and large-population limit for networks of spiking neurons**|我们研究了具有随机尖峰时间的线性（泄漏）和二次积分和放电神经元的空间扩展网络的平均场描述。我们考虑了具有线性和二次内在动力学的连续时间Galves-L“ocherbach（GL）网络的大种群极限。我们证明了泊松假设适用于这些网络的复制平均场极限，即在适当定义的极限内，神经元是独立的，相互作用时间被强度取决于平均放电率的独立时间非均匀泊松过程所取代，将已知结果扩展到具有二次内在动态和重置的网络。证明泊松假设成立为研究这些网络中的大种群限值开辟了可能性。我们证明这个极限是一个适定的神经场模型，受随机重置的影响。 et.al.|[2502.03379](http://arxiv.org/abs/2502.03379)|null|
|**2025-02-04**|**Geometric Neural Process Fields**|本文解决了神经场（NeF）泛化的挑战，其中模型必须有效地适应仅给出少量观测值的新信号。为了解决这个问题，我们提出了几何神经过程场（G-NPF），这是一个明确捕捉不确定性的神经辐射场的概率框架。我们将NeF泛化表述为概率问题，从而能够从有限的上下文观测中直接推断出NeF函数分布。为了引入结构归纳偏差，我们引入了一组几何基来编码空间结构，并促进NeF函数分布的推断。在此基础上，我们设计了一个分层潜在变量模型，使G-NPF能够整合多个空间层次的结构信息，并有效地参数化INR函数。这种分层方法提高了对新场景和未知信号的泛化能力。针对3D场景的新颖视图合成以及2D图像和1D信号回归的实验证明了我们的方法在捕捉不确定性和利用结构信息提高泛化能力方面的有效性。 et.al.|[2502.02338](http://arxiv.org/abs/2502.02338)|null|

<p align=right>(<a href=#updated-on-20250316>back to top</a>)</p>

[contributors-shield]: https://img.shields.io/github/contributors/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[contributors-url]: https://github.com/Vincentqyw/cv-arxiv-daily/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[forks-url]: https://github.com/Vincentqyw/cv-arxiv-daily/network/members
[stars-shield]: https://img.shields.io/github/stars/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[stars-url]: https://github.com/Vincentqyw/cv-arxiv-daily/stargazers
[issues-shield]: https://img.shields.io/github/issues/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[issues-url]: https://github.com/Vincentqyw/cv-arxiv-daily/issues

