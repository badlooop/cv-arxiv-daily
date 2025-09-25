[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]

## Updated on 2025.09.25
> Usage instructions: [here](./docs/README.md#usage)

<details>
  <summary>Table of Contents</summary>
  <ol>
    <li><a href=#video-diffusion>Video Diffusion</a></li>
  </ol>
</details>

## Video Diffusion

|Publish Date|Title|Abstract|PDF|Code|
|---|---|---|---|---|
|**2025-09-24**|**EditVerse: Unifying Image and Video Editing and Generation with In-Context Learning**|基础模型的最新进展突出了统一和扩展的明确趋势，显示了各种领域的新兴能力。尽管图像生成和编辑已迅速从特定于任务的框架过渡到统一的框架，但由于建筑局限性和数据稀缺性，视频生成和编辑仍然存在分散。在这项工作中，我们介绍了Editverse，这是一个统一的图像和视频生成框架，并在单个模型中进行编辑。通过表示所有模式，即文本，图像和视频，作为统一的令牌序列，Editverse Leververs Leververs of自我注意力以实现强大的内在学习，自然的跨模式知识传递以及具有任意决议和持续时间的输入和输出的灵活处理。为了解决缺乏视频编辑培训数据，我们设计了一条可扩展的数据管道，该管道策划了232K视频编辑样本，并将它们与大型图像和视频数据集结合在一起，以进行联合培训。此外，我们介绍了EditverseBench，这是基于教学的视频编辑的第一个基准，涵盖了各种任务和决议。广泛的实验和用户研究表明，Editverse实现了最先进的性能，超过了现有的开源和商业模型，同时表现出跨模式的紧急编辑和发电能力。|[2509.20360](http://arxiv.org/abs/2509.20360)|null|
|**2025-09-24**|**PhysCtrl: Generative Physics for Controllable and Physics-Grounded Video Generation**|现有的视频生成模型在产生文本或图像的照片真实视频方面表现出色，但通常缺乏身体上的合理性和3D可控性。为了克服这些局限性，我们介绍了Physctrl，这是一个具有物理参数和力控制的物理界面形成图像之间的新型框架。其核心是一个生成物理网络，它通过以物理参数和施加力为条件的扩散模型了解了四种材料（弹性，沙子，塑料和刚性）之间物理动力学的分布。我们将物理动力学表示为3D点轨迹，并在物理模拟器生成的550K动画的大规模合成数据集上进行训练。我们使用新型的时空注意力块增强了扩散模型，该模型模拟了粒子相互作用，并在训练过程中纳入了基于物理的约束以实现物理合理性。实验表明，PhysCtrl会生成逼真的，物理接收的运动轨迹，当用于驱动图像到视频模型时，会产生高保真，可控的视频，以优于视觉质量和物理合理性的现有方法。项目页面：https：//cwchenwang.github.io/physctrl|[2509.20358](http://arxiv.org/abs/2509.20358)|null|
|**2025-09-24**|**4D Driving Scene Generation With Stereo Forcing**|当前的生成模型难以合成动态4D驾驶场景，同时支持时间外推和空间新型视图合成（NVS），而无需每场比赛优化。桥接产生和新型观点综合仍然是一个主要挑战。我们提出了Phigenesis，这是4D场景生成的统一框架，它以几何和时间的一致性扩展了视频生成技术。给定的多视图图像序列和摄像机参数，化根发生沿目标3D轨迹产生时间连续的4D高斯脱落表示形式。在其第一阶段，化根利用具有新颖的范围视图适配器的预训练的视频VAE来启用来自多视图图像的前馈4D重建。该体系结构支持单帧或视频输入和输出完整的4D场景，包括几何，语义和运动。在第二阶段，Phigenesis介绍了几何引导的视频扩散模型，使用渲染的历史4D场景作为先验，以生成以轨迹为条件的未来视图。为了解决新型观点中的几何暴露偏见，我们提出了立体声强迫，这是一种新颖的调理策略，可以整合denoing期间的几何不确定性。该方法通过基于不确定性意识的扰动来动态调整生成影响来增强时间连贯性。我们的实验结果表明，我们的方法在外观和几何重建，时间产生和新型视图合成（NVS）任务中都达到了最先进的性能，同时在下游评估中同时提供了竞争性能。主页位于\ href {https://jiangxb98.github.io/phigensis} {phigensis}。|[2509.20251](http://arxiv.org/abs/2509.20251)|null|
|**2025-09-24**|**CamPVG: Camera-Controlled Panoramic Video Generation with Epipolar-Aware Diffusion**|最近，摄像机控制的视频生成已经快速开发，提供了对视频生成的更精确的控制。但是，现有方法主要集中在透视投影视频中，而几何一致的全景视频生成仍然具有挑战性。该限制主要是由于全景姿势表示和球形投影的固有复杂性。为了解决这个问题，我们提出了Campvg，这是由精确的相机姿势指导的第一个基于扩散的视频生成框架。我们实现了基于球形投影的全景图像和跨视图汇总的相机位置。具体而言，我们提出了一个全景pl \“ ucker嵌入，通过球形坐标转换来编码相机外在参数。这种姿势有效地捕获了全景几何形状，克服了传统方法的局限性，当应用于等效的启动的spherical epip eporces时，我们将其应用于等效的启动。 Epolar Line。该模块可以实现精细的跨视图特征聚合，从而增强了生成的全景视频的质量和一致性。|[2509.19979](http://arxiv.org/abs/2509.19979)|null|

<p align=right>(<a href=#updated-on-20250925>back to top</a>)</p>

[contributors-shield]: https://img.shields.io/github/contributors/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[contributors-url]: https://github.com/Vincentqyw/cv-arxiv-daily/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[forks-url]: https://github.com/Vincentqyw/cv-arxiv-daily/network/members
[stars-shield]: https://img.shields.io/github/stars/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[stars-url]: https://github.com/Vincentqyw/cv-arxiv-daily/stargazers
[issues-shield]: https://img.shields.io/github/issues/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[issues-url]: https://github.com/Vincentqyw/cv-arxiv-daily/issues

