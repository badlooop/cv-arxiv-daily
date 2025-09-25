---
layout: default
---

[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]

## Updated on 2025.09.25
> Usage instructions: [here](./docs/README.md#usage)

## Video Diffusion

| Publish Date | Title | Abstract | PDF | Code |
|:---------|:-----------------------|:---------|:------|:------|
|**2025-09-24**|**EditVerse: Unifying Image and Video Editing and Generation with In-Context Learning**|基础模型的最新进展突出了统一和扩展的明确趋势，显示了各种领域的新兴能力。尽管图像生成和编辑已迅速从特定于任务的框架过渡到统一的框架，但由于建筑局限性和数据稀缺性，视频生成和编辑仍然存在分散。在这项工作中，我们介绍了Editverse，这是一个统一的图像和视频生成框架，并在单个模型中进行编辑。通过表示所有模式，即文本，图像和视频，作为统一的令牌序列，Editverse Leververs Leververs of自我注意力以实现强大的内在学习，自然的跨模式知识传递以及具有任意决议和持续时间的输入和输出的灵活处理。为了解决缺乏视频编辑培训数据，我们设计了一条可扩展的数据管道，该管道策划了232K视频编辑样本，并将它们与大型图像和视频数据集结合在一起，以进行联合培训。此外，我们介绍了EditverseBench，这是基于教学的视频编辑的第一个基准，涵盖了各种任务和决议。广泛的实验和用户研究表明，Editverse实现了最先进的性能，超过了现有的开源和商业模型，同时表现出跨模式的紧急编辑和发电能力。|[2509.20360](http://arxiv.org/abs/2509.20360)|null|
|**2025-09-24**|**PhysCtrl: Generative Physics for Controllable and Physics-Grounded Video Generation**|现有的视频生成模型在产生文本或图像的照片真实视频方面表现出色，但通常缺乏身体上的合理性和3D可控性。为了克服这些局限性，我们介绍了Physctrl，这是一个具有物理参数和力控制的物理界面形成图像之间的新型框架。其核心是一个生成物理网络，它通过以物理参数和施加力为条件的扩散模型了解了四种材料（弹性，沙子，塑料和刚性）之间物理动力学的分布。我们将物理动力学表示为3D点轨迹，并在物理模拟器生成的550K动画的大规模合成数据集上进行训练。我们使用新型的时空注意力块增强了扩散模型，该模型模拟了粒子相互作用，并在训练过程中纳入了基于物理的约束以实现物理合理性。实验表明，PhysCtrl会生成逼真的，物理接收的运动轨迹，当用于驱动图像到视频模型时，会产生高保真，可控的视频，以优于视觉质量和物理合理性的现有方法。项目页面：https：//cwchenwang.github.io/physctrl|[2509.20358](http://arxiv.org/abs/2509.20358)|null|
|**2025-09-24**|**4D Driving Scene Generation With Stereo Forcing**|当前的生成模型难以合成动态4D驾驶场景，同时支持时间外推和空间新型视图合成（NVS），而无需每场比赛优化。桥接产生和新型观点综合仍然是一个主要挑战。我们提出了Phigenesis，这是4D场景生成的统一框架，它以几何和时间的一致性扩展了视频生成技术。给定的多视图图像序列和摄像机参数，化根发生沿目标3D轨迹产生时间连续的4D高斯脱落表示形式。在其第一阶段，化根利用具有新颖的范围视图适配器的预训练的视频VAE来启用来自多视图图像的前馈4D重建。该体系结构支持单帧或视频输入和输出完整的4D场景，包括几何，语义和运动。在第二阶段，Phigenesis介绍了几何引导的视频扩散模型，使用渲染的历史4D场景作为先验，以生成以轨迹为条件的未来视图。为了解决新型观点中的几何暴露偏见，我们提出了立体声强迫，这是一种新颖的调理策略，可以整合denoing期间的几何不确定性。该方法通过基于不确定性意识的扰动来动态调整生成影响来增强时间连贯性。我们的实验结果表明，我们的方法在外观和几何重建，时间产生和新型视图合成（NVS）任务中都达到了最先进的性能，同时在下游评估中同时提供了竞争性能。主页位于\ href {https://jiangxb98.github.io/phigensis} {phigensis}。|[2509.20251](http://arxiv.org/abs/2509.20251)|null|
|**2025-09-24**|**CamPVG: Camera-Controlled Panoramic Video Generation with Epipolar-Aware Diffusion**|最近，摄像机控制的视频生成已经快速开发，提供了对视频生成的更精确的控制。但是，现有方法主要集中在透视投影视频中，而几何一致的全景视频生成仍然具有挑战性。该限制主要是由于全景姿势表示和球形投影的固有复杂性。为了解决这个问题，我们提出了Campvg，这是由精确的相机姿势指导的第一个基于扩散的视频生成框架。我们实现了基于球形投影的全景图像和跨视图汇总的相机位置。具体而言，我们提出了一个全景pl \“ ucker嵌入，通过球形坐标转换来编码相机外在参数。这种姿势有效地捕获了全景几何形状，克服了传统方法的局限性，当应用于等效的启动的spherical epip eporces时，我们将其应用于等效的启动。 Epolar Line。该模块可以实现精细的跨视图特征聚合，从而增强了生成的全景视频的质量和一致性。|[2509.19979](http://arxiv.org/abs/2509.19979)|null|
|**2025-09-24**|**From Prompt to Progression: Taming Video Diffusion Models for Seamless Attribute Transition**|现有模型通常会在复杂的时间变化中挣扎，尤其是在生成具有逐渐属性过渡的视频时。运动过渡的最常见及时插值方法通常无法处理渐进的属性转变，而不一致往往会变得更加明显。在这项工作中，我们提出了一种简单而有效的方法，通过在DeNoising过程中引入框架指导来扩展现有模型以进行平滑且一致的属性过渡。我们的方法为每个嘈杂的潜在构建一个特定于数据的过渡方向，在保留视频的运动动力学的同时，通过框架指导从初始属性到最终属性的逐渐转移。此外，我们介绍了控制属性和运动动力学的受控 - 属性转换基准（CAT Bench），以全面评估不同模型的性能。我们进一步提出了两个指标，以评估属性过渡的准确性和平滑性。实验结果表明，我们的方法对现有基线，实现视觉保真度，与文本提示保持一致并提供无缝属性过渡相对。代码和catbench发布：https：//github.com/lynn-ling-lo/prompt2progression。|[2509.19690](http://arxiv.org/abs/2509.19690)|null|
|**2025-09-23**|**Lyra: Generative 3D Scene Reconstruction via Video Diffusion Model Self-Distillation**|生成虚拟环境的能力对于从游戏到物理AI领域（例如机器人技术，自动驾驶和工业AI）等应用至关重要。当前基于学习的3D重建方法取决于捕获的现实世界多视图数据的可用性，这并不总是很容易获得。视频扩散模型的最新进展显示出了显着的想象力，但是它们的2D性质将应用程序限制为模拟机器人需要导航和与环境交互的模拟。在本文中，我们提出了一个自distillation框架，旨在将视频扩散模型中的隐式3D知识提炼成明显的3D高斯分裂（3DGS）表示，从而消除了对多视图训练数据的需求。具体来说，我们使用3DGS解码器增强了典型的RGB解码器，该解码器由RGB解码器的输出进行监督。在这种方法中，3DGS解码器可以通过视频扩散模型生成的合成数据纯粹训练。在推理时，我们的模型可以从文本提示或单个图像中合成3D场景以进行实时渲染。我们的框架进一步扩展到单眼输入视频的动态3D场景生成。实验结果表明，我们的框架在静态和动态的3D场景生成中实现了最先进的性能。|[2509.19296](http://arxiv.org/abs/2509.19296)|null|
|**2025-09-23**|**Flow marching for a generative PDE foundation model**|在大规模的PDE州时空轨迹上进行了预处理，最近显示出有望构建动态系统的可通用模型。然而，大多数现有的PDE基础模型都依赖于确定性的变压器体系结构，这些结构缺乏许多科学和工程应用程序的生成灵活性。我们提出了流程，这是一种算法，该算法将神经操作员学习与流动匹配，该流程匹配是通过分析物理动力学系统中错误积累的分析，并且我们在其上构建了生成的PDE基础模型。通过共同采样噪声水平和相邻状态之间的物理时间步长，该模型学习了一个统一的速度场，该速度场将嘈杂的当前状态传输到其干净的后继者，从而减少了长期的推出漂移，同时使不确定性吸引了一代。除了该核心算法外，我们还引入了物理学预言的变异自动编码器（P2VAE），将物理状态嵌入到一个紧凑的潜在空间中，并有效的流动变压器（FMT）结合了扩散式方案，该方案将扩散型方案与潜在的较大的较大的范围延伸到更大的范围，从而达到更大的计算范围，从而达到15x的良好范围，以达到15x的范围，以达到15x的范围，以达到15倍的范围。大大降低了成本。我们在12个不同的PDE家族中策划了约250万个轨迹的语料库，并在多个尺度上策划了P2VAES和FMT的套件。在下游评估中，我们基于看不见的kolmogorov湍流，几乎没有射击适应，证明了对确定性对应物的长期推出稳定性，并提出了不确定性分层的集合结果，强调了生成PDE基础模型对现实世界应用的重要性。|[2509.18611](http://arxiv.org/abs/2509.18611)|null|
|**2025-09-22**|**VideoFrom3D: 3D Scene Video Generation via Complementary Image and Video Diffusion Models**|在本文中，我们提出了Videofrom3D，这是一个新颖的框架，用于合成粗糙几何，摄像机轨迹和参考图像的高质量3D场景视频。我们的方法简化了3D图形设计工作流程，从而可以灵活设计探索并快速生产可交付成果。从粗几何形状中综合视频的直接方法可能会使视频扩散模型在几何结构上。但是，由于难以联合建模视觉质量，运动和时间一致性，因此现有的视频扩散模型难以为复杂场景产生高保真结果。为了解决这个问题，我们提出了一个生成框架，以利用图像和视频扩散模型的互补优势。具体而言，我们的框架由稀疏的锚定生成（SAG）和几何引导的生成式Inbetinging（GGI）模块组成。 SAG模块使用图像扩散模型生成高质量的，跨视图一致的锚点视图，并通过稀疏的外观引导采样的帮助。 GGI模块以这些锚点的视图为基础，使用视频扩散模型忠实地插入了中间帧，并通过基于流动的摄像机控制和结构指导增强了中间框架。值得注意的是，两个模块都没有任何配对的3D场景模型和自然图像的数据集，这非常困难。综合实验表明，我们的方法在多样化和挑战性的场景下产生高质量的风格场景视频，表现优于简单和扩展的基线。|[2509.17985](http://arxiv.org/abs/2509.17985)|null|
|**2025-09-22**|**I2VWM: Robust Watermarking for Image to Video Generation**|图像引导的视频生成（I2V）的快速进步引起了人们对其在错误信息和欺诈方面的潜在滥用的担忧，强调了迫切需要有效的数字水印。尽管现有的水印方法证明了单个模态内的鲁棒性，但它们无法在I2V设置中追踪源图像。为了解决这一差距，我们介绍了稳健的扩散距离的概念，该距离衡量了生成的视频中水印信号的时间持久性。在此基础上，我们提出了I2VWM，这是一种跨模式水印框架，旨在增强随时间的水印稳健性。 I2VWM在训练过程中利用视频模拟噪声层，并在推理过程中采用基于光学的对准模块。开源和商业I2V模型的实验表明，I2VWM在保持不可识别的同时显着提高了鲁棒性，在生成视频时代建立了新的跨模式水印范式。 \ href {https://github.com/mrcrims/i2vwm-robust-watermarking-for-image-to-video-generation} {代码发布。}|[2509.17773](http://arxiv.org/abs/2509.17773)|null|
|**2025-09-21**|**Echo-Path: Pathology-Conditioned Echo Video Generation**|心血管疾病（CVD）仍然是全球死亡率的主要原因，超声心动图对于诊断常见和先天性心脏状况至关重要。但是，某些病理的超声心动图数据稀缺，阻碍了强大的自动诊断模型的发展。在这项工作中，我们提出了Echo-Path，这是一种新型的生成框架，以生成以特定心脏病理为条件的超声心动图视频。 Echo-Path可以合成具有靶向异常的现实超声视频序列，重点是心房间隔缺陷（ASD）和肺动脉高压（PAH）。我们的方法将病理条件的机制引入了最新的回声视频发生器，从而使模型可以在心脏中学习和控制特定于疾病的结构和运动模式。定量评估表明，合成视频达到了低分布距离，表明视觉效果很高。在临床上，产生的回声表现出合理的病理标记。此外，经过培训的合成数据的分类器可以很好地推广到真实数据，并且在用于增强实际训练集的情况下，它将ASD和PAH的下游诊断分别提高了7 \％和8 \％。代码，权重和数据集可在此处提供https://github.com/marshall-mk/echopathv1|[2509.17190](http://arxiv.org/abs/2509.17190)|null|

[contributors-shield]: https://img.shields.io/github/contributors/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[contributors-url]: https://github.com/Vincentqyw/cv-arxiv-daily/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[forks-url]: https://github.com/Vincentqyw/cv-arxiv-daily/network/members
[stars-shield]: https://img.shields.io/github/stars/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[stars-url]: https://github.com/Vincentqyw/cv-arxiv-daily/stargazers
[issues-shield]: https://img.shields.io/github/issues/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[issues-url]: https://github.com/Vincentqyw/cv-arxiv-daily/issues

