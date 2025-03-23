[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]

## Updated on 2025.03.23
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
|**2025-03-20**|**XAttention: Block Sparse Attention with Antidiagonal Scoring**|长上下文变换器模型（LCTM）对于现实世界的应用至关重要，但由于注意力的二次复杂性，计算成本很高。块稀疏注意力通过将计算集中在关键区域来缓解这一问题，但由于块重要性测量成本高昂，现有方法在平衡精度和效率方面存在困难。在本文中，我们介绍了XAttention，这是一个即插即用的框架，它使用稀疏注意力显著加速了Transformers模型中的长上下文推理。XAttention的关键创新在于，它发现注意力矩阵中的反诊断值之和（即从左下角到右上角）为块重要性提供了强有力的代理。这允许对非必要块进行精确识别和修剪，从而实现高稀疏性和显著加速的推理。对要求苛刻的长上下文基准进行全面评估，包括用于语言的RULER和LongBench、用于视频理解的VideoMME和用于视频生成的VBench。XAttention在提供大量计算增益的同时，实现了与完全注意力相当的准确性。我们在注意力计算中展示了高达13.5倍的加速度。这些结果强调了XAttention能够释放块稀疏注意力的实际潜力，为在现实应用中可扩展和高效地部署LCTM铺平了道路。代码可在以下网址获得https://github.com/mit-han-lab/x-attention. et.al.|[2503.16428](http://arxiv.org/abs/2503.16428)|null|
|**2025-03-20**|**MagicMotion: Controllable Video Generation with Dense-to-Sparse Trajectory Guidance**|视频生成的最新进展导致了视觉质量和时间连贯性的显著提高。在此基础上，出现了轨迹可控的视频生成，通过明确定义的空间路径实现了精确的对象运动控制。然而，现有的方法难以应对复杂的物体运动和多物体运动控制，导致轨迹附着不精确、物体一致性差、视觉质量受损。此外，这些方法仅支持单一格式的轨迹控制，限制了它们在不同场景中的适用性。此外，没有专门为轨迹可控视频生成量身定制的公开数据集或基准，这阻碍了稳健的训练和系统评估。为了应对这些挑战，我们引入了MagicMotion，这是一种新颖的图像到视频生成框架，可以通过从密集到稀疏的三个级别的条件进行轨迹控制：掩码、边界框和稀疏框。给定输入图像和轨迹，MagicMotion可以沿着定义的轨迹无缝地为对象设置动画，同时保持对象的一致性和视觉质量。此外，我们还介绍了MagicData，这是一个大规模的轨迹控制视频数据集，以及一个用于注释和过滤的自动化管道。我们还引入了MagicBench，一个全面的基准，用于评估不同数量对象的视频质量和轨迹控制精度。大量实验表明，MagicMotion在各种指标上都优于之前的方法。我们的项目页面可在https://quanhaol.github.io/magicmotion-site. et.al.|[2503.16421](http://arxiv.org/abs/2503.16421)|null|
|**2025-03-20**|**ScalingNoise: Scaling Inference-Time Search for Generating Infinite Videos**|视频扩散模型（VDM）有助于生成高质量的视频，目前的研究主要集中在通过提高数据质量、计算资源和模型复杂性在训练过程中进行缩放。然而，推理时间缩放受到的关注较少，大多数方法将模型限制为单代尝试。最近的研究发现，在生成过程中存在可以提高视频质量的“金噪声”。在此基础上，我们发现，指导VDM的缩放推理时间搜索以识别更好的噪声候选不仅可以评估当前步骤中生成的帧的质量，还可以通过参考先前多块中的锚帧来保留高级对象特征，从而提供长期价值。我们的分析表明，扩散模型天生具有通过改变去噪步骤来灵活调整计算的能力，甚至在奖励信号的指导下，一步去噪方法也能产生显著的长期效益。基于观察结果，我们提出了ScalingNoise，这是一种即插即用的推理时间搜索策略，可以为扩散采样过程识别黄金初始噪声，以提高全局内容一致性和视觉多样性。具体来说，我们执行一步去噪，将初始噪声转换为片段，随后利用由先前生成的内容锚定的奖励模型来评估其长期价值。此外，为了保持多样性，我们从倾斜的噪声分布中对候选者进行采样，该分布对有希望的噪声进行加权。通过这种方式，ScalingNoise显著减少了噪声引起的错误，确保了更连贯和时空一致的视频生成。对基准数据集的大量实验表明，所提出的ScalingNoise有效地提高了长视频的生成效率。 et.al.|[2503.16400](http://arxiv.org/abs/2503.16400)|null|
|**2025-03-20**|**SV4D 2.0: Enhancing Spatio-Temporal Consistency in Multi-View Video Diffusion for High-Quality 4D Generation**|我们提出了Stable Video 4D 2.0（SV4D 2.0），这是一种用于动态3D资产生成的多视图视频扩散模型。与其前身SV4D相比，SV4D 2.0对遮挡和大运动更稳健，对真实世界的视频有更好的泛化能力，并在细节清晰度和时空一致性方面产生更高质量的输出。我们通过在多个方面引入关键改进来实现这一目标：1）网络架构：消除参考多视图的依赖性，设计3D和帧注意力的混合机制；2）数据：提高训练数据的质量和数量；3）训练策略：采用渐进式3D-4D训练以获得更好的泛化能力；4）4D优化：通过两阶段细化和渐进式帧采样处理3D不一致性和大运动。大量实验表明，SV4D 2.0在视觉和定量上都有显著的性能提升，与SV4D相比，在新视图视频合成和4D优化（-12%LPIPS和-24%FV4D）中实现了更好的细节（-14%LPIPS）和4D一致性（-44%FV4D）。项目页面：https://sv4d2.0.github.io. et.al.|[2503.16396](http://arxiv.org/abs/2503.16396)|null|
|**2025-03-20**|**PoseTraj: Pose-Aware Trajectory Control in Video Diffusion**|轨迹引导视频生成的最新进展取得了显著进展。然而，由于对3D的理解有限，现有模型在生成具有在宽范围旋转下可能变化的6D姿态的物体运动方面仍然面临挑战。为了解决这个问题，我们引入了PoseTraj，这是一种姿态感知视频拖动模型，用于从2D轨迹生成3D对齐运动。我们的方法采用了一种新颖的两阶段姿态感知预训练框架，提高了对不同轨迹的3D理解。具体来说，我们提出了一个大规模的合成数据集PoseTraj-10K，其中包含10K个物体遵循旋转轨迹的视频，并通过将3D边界框作为中间监督信号来增强物体姿态变化的模型感知。在此之后，我们对现实世界视频上的轨迹控制模块进行了微调，应用了一个额外的相机解纠缠模块来进一步提高运动精度。在各种基准数据集上的实验表明，我们的方法不仅在旋转轨迹的3D姿态对齐拖动方面表现出色，而且在轨迹精度和视频质量方面也优于现有的基线。 et.al.|[2503.16068](http://arxiv.org/abs/2503.16068)|null|
|**2025-03-20**|**Animating the Uncaptured: Humanoid Mesh Animation with Video Diffusion Models**|人形角色的动画在各种图形应用中都是必不可少的，但创建逼真的动画需要大量的时间和成本。我们提出了一种方法，利用生成视频模型中的强广义运动先验来合成输入静态3D人形网格的4D动画序列，因为这些视频模型包含覆盖各种人类运动的强大运动信息。从输入的静态3D人形网格和描述所需动画的文本提示中，我们合成了一个基于3D网格渲染图像的相应视频。然后，基于我们的运动优化，我们使用底层SMPL表示来根据视频生成的运动为相应的3D网格设置动画。这提供了一种经济高效且易于使用的解决方案，可以合成各种逼真的4D动画。 et.al.|[2503.15996](http://arxiv.org/abs/2503.15996)|null|
|**2025-03-20**|**MiLA: Multi-view Intensive-fidelity Long-term Video Generation World Model for Autonomous Driving**|近年来，数据驱动技术极大地推动了自动驾驶系统的发展，但对稀有和多样化的训练数据的需求仍然是一个挑战，需要在设备和劳动力方面进行大量投资。预测和生成未来环境状态的世界模型通过合成带注释的视频数据进行训练，提供了一种有前景的解决方案。然而，现有的方法很难在不积累错误的情况下生成长而一致的视频，尤其是在动态场景中。为了解决这个问题，我们提出了MiLA，这是一种生成高保真、长时间视频的新框架，最长可达一分钟。MiLA利用粗糙到再（精细）的方法来稳定视频生成和校正动态对象的失真。此外，我们引入了时间渐进去噪调度器和联合去噪和校正流模块，以提高生成视频的质量。在nuScenes数据集上的大量实验表明，MiLA在视频生成质量方面达到了最先进的性能。有关更多信息，请访问项目网站：https://github.com/xiaomi-mlab/mila.github.io. et.al.|[2503.15875](http://arxiv.org/abs/2503.15875)|null|
|**2025-03-20**|**VideoRFSplat: Direct Scene-Level Text-to-3D Gaussian Splatting Generation with Flexible Pose and Multi-View Joint Modeling**|我们提出了VideoRFSplat，这是一种直接的文本到3D模型，利用视频生成模型为无限的现实世界场景生成逼真的3D高斯散斑（3DGS）。为了生成不同的相机姿态和现实世界场景的无限空间范围，同时确保对任意文本提示的泛化，以前的方法对2D生成模型进行微调，以联合建模相机姿态和多视图图像。然而，由于模态差距，这些方法在将2D生成模型扩展到联合建模时存在不稳定性，这需要额外的模型来稳定训练和推理。在这项工作中，我们提出了一种架构和采样策略，在微调视频生成模型时，对多视图图像和相机姿态进行联合建模。我们的核心思想是一种双流架构，通过通信块将专用的姿势生成模型与预训练的视频生成模型连接在一起，通过单独的流生成多视图图像和相机姿势。这种设计减少了姿态和图像模态之间的干扰。此外，我们提出了一种异步采样策略，该策略比多视图图像更快地对相机姿态进行去噪，允许快速去噪姿态来调节多视图生成，减少相互模糊并增强跨模态一致性。VideoRFSplat经过多个大规模真实世界数据集（RealEstate10K、MVImgNet、DL3DV-10K、ACID）的训练，其性能优于现有的文本到3D直接生成方法，这些方法严重依赖于通过分数蒸馏采样进行事后细化，即使不进行此类细化，也能获得优异的结果。 et.al.|[2503.15855](http://arxiv.org/abs/2503.15855)|null|
|**2025-03-20**|**Zero-1-to-A: Zero-Shot One Image to Animatable Head Avatars Using Video Diffusion**|可动画化的头部化身生成通常需要大量数据进行训练。为了减少数据需求，一个自然的解决方案是利用现有的无数据静态化身生成方法，例如具有分数蒸馏采样（SDS）的预训练扩散模型，该模型将化身与扩散模型的伪地面真实输出对齐。然而，由于生成的视频在空间和时间上的不一致性，直接从视频扩散中提取4D化身通常会导致结果过于平滑。为了解决这个问题，我们提出了Zero-1-To-A，这是一种鲁棒的方法，可以使用视频扩散模型合成用于4D化身重建的空间和时间一致性数据集。具体来说，Zero-1-to-A迭代地构建视频数据集，并以渐进的方式优化可设置动画的化身，确保化身质量在整个学习过程中平稳一致地提高。这种渐进式学习包括两个阶段：（1）空间一致性学习修复表情并从正面到侧面进行学习，（2）时间一致性学习固定视图并从放松到夸张的表情进行学习，以简单到复杂的方式生成4D化身。大量实验表明，与现有的基于扩散的方法相比，Zero-1-to-A提高了保真度、动画质量和渲染速度，为逼真的化身创建提供了一种解决方案。代码可在以下网址公开获取：https://github.com/ZhenglinZhou/Zero-1-to-A. et.al.|[2503.15851](http://arxiv.org/abs/2503.15851)|null|
|**2025-03-19**|**Uncertainty-Aware Diffusion Guided Refinement of 3D Scenes**|由于问题的严重欠约束性，从单个图像重建3D场景是一项根本不适定的任务。因此，当从新颖的相机视图渲染场景时，现有的单图像到3D重建方法会渲染不连贯和模糊的视图。当看不见的区域远离输入相机时，这个问题会加剧。在这项工作中，我们解决了现有单图像到3D场景前馈网络中的这些固有局限性。为了缓解由于输入图像视图之外的信息不足而导致的性能不佳，我们利用预训练的潜在视频扩散模型形式的强生成先验，对由可优化高斯参数表示的粗略场景进行迭代细化。为了确保生成的图像的风格和纹理与输入图像的样式和纹理对齐，我们在生成的图像和输入图像之间进行了实时傅里叶风格转换。此外，我们设计了一个语义不确定性量化模块，该模块计算每像素的熵，并生成不确定性图，用于从最自信的像素中指导细化过程，同时丢弃剩余的高度不确定性像素。我们在真实世界的场景数据集上进行了广泛的实验，包括域内RealEstate-10K和域外KITTI-v2，表明与现有的最先进方法相比，我们的方法可以提供更真实、高保真的新颖视图合成结果。 et.al.|[2503.15742](http://arxiv.org/abs/2503.15742)|null|

<p align=right>(<a href=#updated-on-20250323>back to top</a>)</p>

## 3D

|Publish Date|Title|Abstract|PDF|Code|
|---|---|---|---|---|
|**2025-03-20**|**Gaussian Graph Network: Learning Efficient and Generalizable Gaussian Representations from Multi-view Images**|3D高斯散斑（3DGS）显示出令人印象深刻的新颖视图合成性能。虽然传统方法需要针对每个场景进行优化，但最近提出了几种前馈方法，通过可学习的网络生成像素对齐的高斯表示，这些方法可推广到不同的场景。然而，这些方法只是将来自多个视图的像素对齐高斯图像组合为场景表示，从而导致伪影和额外的内存成本，而没有完全捕捉到不同图像中高斯图像的关系。本文中，我们提出了高斯图网络（GGN）来生成高效且可推广的高斯表示。具体来说，我们构建高斯图，从不同的角度对高斯群的关系进行建模。为了支持高斯级别的消息传递，我们重新制定了高斯表示上的基本图操作，使每个高斯都能通过高斯特征融合从其连接的高斯群中受益。此外，我们设计了一个高斯池层来聚合各种高斯群，以实现高效表示。我们在大规模RealEstate10K和ACID数据集上进行了实验，以证明我们方法的效率和泛化能力。与最先进的方法相比，我们的模型使用更少的高斯分布，并以更高的渲染速度实现了更好的图像质量。 et.al.|[2503.16338](http://arxiv.org/abs/2503.16338)|null|
|**2025-03-20**|**Enhancing Close-up Novel View Synthesis via Pseudo-labeling**|最近的方法，如神经辐射场（NeRF）和3D高斯散斑（3DGS），在新颖的视图合成方面表现出了显著的能力。然而，尽管他们成功地为与训练期间看到的视点类似的视点生成了高质量的图像，但他们在从明显偏离训练集的视点生成详细图像时遇到了困难，特别是在特写视图中。主要挑战源于缺乏特写视图的特定训练数据，导致当前方法无法准确渲染这些视图。为了解决这个问题，我们引入了一种新的基于伪标签的学习策略。这种方法利用从现有训练数据中得出的伪标签，在广泛的特写视角下提供有针对性的监督。认识到这一具体挑战缺乏基准，我们还提出了一个新的数据集，旨在评估当前和未来方法在这一领域的有效性。我们广泛的实验证明了我们方法的有效性。 et.al.|[2503.15908](http://arxiv.org/abs/2503.15908)|null|
|**2025-03-19**|**Uncertainty-Aware Diffusion Guided Refinement of 3D Scenes**|由于问题的严重欠约束性，从单个图像重建3D场景是一项根本不适定的任务。因此，当从新颖的相机视图渲染场景时，现有的单图像到3D重建方法会渲染不连贯和模糊的视图。当看不见的区域远离输入相机时，这个问题会加剧。在这项工作中，我们解决了现有单图像到3D场景前馈网络中的这些固有局限性。为了缓解由于输入图像视图之外的信息不足而导致的性能不佳，我们利用预训练的潜在视频扩散模型形式的强生成先验，对由可优化高斯参数表示的粗略场景进行迭代细化。为了确保生成的图像的风格和纹理与输入图像的样式和纹理对齐，我们在生成的图像和输入图像之间进行了实时傅里叶风格转换。此外，我们设计了一个语义不确定性量化模块，该模块计算每像素的熵，并生成不确定性图，用于从最自信的像素中指导细化过程，同时丢弃剩余的高度不确定性像素。我们在真实世界的场景数据集上进行了广泛的实验，包括域内RealEstate-10K和域外KITTI-v2，表明与现有的最先进方法相比，我们的方法可以提供更真实、高保真的新颖视图合成结果。 et.al.|[2503.15742](http://arxiv.org/abs/2503.15742)|null|
|**2025-03-19**|**CHROME: Clothed Human Reconstruction with Occlusion-Resilience and Multiview-Consistency from a Single Image**|从单个图像重建穿着衣服的人是计算机视觉中的一项基本任务，具有广泛的应用。尽管现有的单眼服装人体重建解决方案已经显示出有希望的结果，但它们通常依赖于人类受试者处于无遮挡环境的假设。因此，当在野外遇到遮挡图像时，这些算法会产生多视图不一致和碎片化的重建。此外，大多数单眼3D人体重建算法都利用SMPL注释等几何先验进行训练和推理，这在现实世界的应用中极具挑战性。为了解决这些局限性，我们提出了CHROME:基于单图像的具有遮挡弹性和多视图一致性的遮挡人体重建，这是一种新的管道，旨在从单个遮挡图像中重建具有多视图一致度的遮挡弹性3D人体，而不需要基础几何先验注释或3D监督。具体来说，CHROME利用多视图扩散模型，首先从被遮挡的输入中合成无遮挡的人体图像，与现成的姿态控制兼容，以在合成过程中明确地增强交叉视图的一致性。然后，训练3D重建模型来预测一组基于遮挡输入和合成视图的3D高斯分布，对齐交叉视图细节以产生连贯准确的3D表示。CHROME在新颖的视图合成（高达3db PSNR）和具有挑战性的条件下的几何重建方面都取得了显著的进步。 et.al.|[2503.15671](http://arxiv.org/abs/2503.15671)|null|
|**2025-03-19**|**DiffPortrait360: Consistent Portrait Diffusion for 360 View Synthesis**|从单视图图像生成高质量的360度人头视图对于实现可访问的沉浸式远程呈现应用程序和可扩展的个性化内容创建至关重要。虽然全头部生成的尖端方法仅限于模拟逼真的人类头部，但最新的基于扩散的风格全知头部合成方法只能产生正面视图，并且难以保证视图的一致性，从而无法将其转换为从任意角度渲染的真正3D模型。我们介绍了一种新颖的方法，可以生成完全一致的360度头部视图，适应人类、程式化和拟人化的形式，包括眼镜和帽子等配饰。我们的方法基于DiffPortrait3D框架，结合了一个用于生成后脑细节的自定义ControlNet和一个双重外观模块，以确保全局前后一致性。通过对连续视图序列进行训练并整合后向参考图像，我们的方法实现了鲁棒的局部连续视图合成。我们的模型可用于生成高质量的神经辐射场（NeRF），用于实时、自由视点渲染，在对象合成和360度头部生成方面优于最先进的方法，适用于非常具有挑战性的输入肖像。 et.al.|[2503.15667](http://arxiv.org/abs/2503.15667)|null|
|**2025-03-19**|**Learn Your Scales: Towards Scale-Consistent Generative Novel View Synthesis**|传统的无深度多视图数据集是使用移动的单目相机捕获的，没有进行度量校准。在这种单眼设置中，相机位置的比例是模糊的。先前的方法通过各种ad-hoc归一化预处理步骤承认了多视图数据中的尺度模糊，但没有直接分析不正确的场景尺度对其应用的影响。在本文中，我们试图理解和解决尺度模糊在用于训练生成性新视图合成方法（GNVS）时的影响。在GNVS中，给定单个图像，场景或对象的新视图可以最小限度地合成，因此不受约束，需要使用生成方法。这些模型的生成性捕获了不确定性的各个方面，包括场景尺度的任何不确定性，这些不确定性充当了任务的干扰变量。我们通过分离场景尺度模糊对结果模型的影响，研究了从单幅图像采样时GNVS中场景尺度模糊的影响，并基于这些直觉定义了衡量生成视图尺度不一致性的新指标。然后，我们提出了一个框架，以端到端的方式与GNVS模型联合估计场景规模。经验表明，我们的方法减少了生成视图的尺度不一致性，而没有以前尺度归一化方法的复杂性或缺点。此外，我们还表明，消除这种模糊性可以提高生成的GNVS模型的图像质量。 et.al.|[2503.15412](http://arxiv.org/abs/2503.15412)|null|
|**2025-03-19**|**DiST-4D: Disentangled Spatiotemporal Diffusion with Metric Depth for 4D Driving Scene Generation**|当前的生成模型难以合成动态4D驾驶场景，这些场景同时支持时间外推和空间新视图合成（NVS），而无需对每个场景进行优化。一个关键的挑战在于找到一种高效且可推广的几何表示，将时间和空间合成无缝连接起来。为了解决这个问题，我们提出了DiST-4D，这是第一个用于4D驾驶场景生成的解纠缠时空扩散框架，它利用度量深度作为核心几何表示。DiST-4D将问题分解为两个扩散过程：DiST-T，它直接从过去的观测中预测未来的度量深度和多视图RGB序列；DiST-S，它通过仅在现有视点上训练来实现空间NVS，同时强制循环一致性。这种循环一致性机制引入了前后渲染约束，缩小了观察到的视点和看不到的视点之间的泛化差距。度量深度对于准确可靠的预测和准确的空间NVS至关重要，因为它提供了一种视图一致的几何表示，可以很好地推广到看不见的视角。实验表明，DiST-4D在时间预测和NVS任务中都达到了最先进的性能，同时在规划相关评估方面也提供了有竞争力的性能。 et.al.|[2503.15208](http://arxiv.org/abs/2503.15208)|null|
|**2025-03-19**|**MultiBARF: Integrating Imagery of Different Wavelength Regions by Using Neural Radiance Fields**|光学传感器应用通过数字化转型变得流行。将观测数据与现实世界的位置联系起来，并结合不同的图像传感器，对于使应用程序实用高效至关重要。然而，尝试不同传感器组合的数据准备需要高度的传感和图像处理专业知识。为了使不熟悉传感和图像处理的用户更容易进行数据准备，我们开发了MultiBARF。该方法通过在指定视点合成两对不同的传感器图像和深度图像来代替共配准和几何校准。我们的方法为两个成像器扩展了束调整神经辐射场（BARF），这是一种基于深度神经网络的新型视图合成方法。通过对可见光和热成像图像的实验，我们证明了我们的方法将这些传感器图像的两个颜色通道叠加在NeRF上。 et.al.|[2503.15070](http://arxiv.org/abs/2503.15070)|null|
|**2025-03-18**|**SplatVoxel: History-Aware Novel View Streaming without Temporal Training**|我们研究了稀疏视图视频中的新视图流问题，该问题旨在随着新的输入帧的到来，生成连续的高质量、时间一致的新视图序列。然而，现有的新颖视图合成方法在时间连贯性和视觉保真度方面存在困难，导致闪烁和不一致。为了应对这些挑战，我们引入了历史感知，利用之前的帧来重建场景，提高质量和稳定性。我们提出了一种混合飞溅体素前馈场景重建方法，该方法结合了高斯飞溅来随时间传播信息，并采用分层体素网格进行时间融合。使用将2D跟踪模型扩展到3D运动的运动图，高斯基元随着时间的推移被有效地扭曲，而稀疏体素变换器则以误差感知的方式整合新的时间观测值。至关重要的是，我们的方法不需要在多视图视频数据集上进行训练，这些数据集目前在大小和多样性方面受到限制，并且可以在推理时以历史感知的方式直接应用于稀疏视图视频流。我们的方法在静态和流式场景重建方面都达到了最先进的性能，在单个H100 GPU上以交互速率（15fps，350ms延迟）运行时，有效地减少了时间伪影和视觉伪影。项目页面：https://19reborn.github.io/SplatVoxel/ et.al.|[2503.14698](http://arxiv.org/abs/2503.14698)|null|
|**2025-03-18**|**Stable Virtual Camera: Generative View Synthesis with Diffusion Models**|我们提出了稳定的虚拟相机（Seva），这是一种多面手扩散模型，可以在给定任意数量的输入视图和目标相机的情况下创建场景的新颖视图。现有的工作难以生成大的视点变化或时间平滑的样本，同时依赖于特定的任务配置。我们的方法通过简单的模型设计、优化的训练配方和灵活的采样策略克服了这些局限性，这些策略在测试时跨视图合成任务进行泛化。因此，我们的样本保持了高一致性，而不需要额外的基于3D表示的蒸馏，从而简化了野外的视图合成。此外，我们证明我们的方法可以生成持续时间长达半分钟的高质量视频，并实现无缝循环闭合。广泛的基准测试表明，Seva在不同的数据集和设置中表现优于现有方法。 et.al.|[2503.14489](http://arxiv.org/abs/2503.14489)|null|

<p align=right>(<a href=#updated-on-20250323>back to top</a>)</p>

## 3D Reconstruction

|Publish Date|Title|Abstract|PDF|Code|
|---|---|---|---|---|
|**2025-03-20**|**DreamTexture: Shape from Virtual Texture with Analysis by Augmentation**|DreamFusion通过结合生成模型和可微渲染的进步，为从虚拟视图进行无监督的3D重建建立了一种新的范式。然而，底层的多视图渲染以及大规模生成模型的监督在计算上很昂贵，而且受到的限制也很小。我们提出了DreamTexture，这是一种新颖的虚拟纹理形状方法，利用单眼深度线索重建3D对象。我们的方法通过将虚拟纹理与输入中的真实深度线索对齐来对输入图像进行纹理化，利用了现代扩散模型中编码的单眼几何的固有理解。然后，我们使用新的共形映射优化从虚拟纹理变形中重建深度，这减轻了内存密集型的体积表示。我们的实验表明，生成模型对单眼形状线索有理解，可以通过增强和对齐纹理线索来提取，这是一种新的单眼重建范式，我们称之为增强分析。 et.al.|[2503.16412](http://arxiv.org/abs/2503.16412)|null|
|**2025-03-20**|**Gaussian Graph Network: Learning Efficient and Generalizable Gaussian Representations from Multi-view Images**|3D高斯散斑（3DGS）显示出令人印象深刻的新颖视图合成性能。虽然传统方法需要针对每个场景进行优化，但最近提出了几种前馈方法，通过可学习的网络生成像素对齐的高斯表示，这些方法可推广到不同的场景。然而，这些方法只是将来自多个视图的像素对齐高斯图像组合为场景表示，从而导致伪影和额外的内存成本，而没有完全捕捉到不同图像中高斯图像的关系。本文中，我们提出了高斯图网络（GGN）来生成高效且可推广的高斯表示。具体来说，我们构建高斯图，从不同的角度对高斯群的关系进行建模。为了支持高斯级别的消息传递，我们重新制定了高斯表示上的基本图操作，使每个高斯都能通过高斯特征融合从其连接的高斯群中受益。此外，我们设计了一个高斯池层来聚合各种高斯群，以实现高效表示。我们在大规模RealEstate10K和ACID数据集上进行了实验，以证明我们方法的效率和泛化能力。与最先进的方法相比，我们的模型使用更少的高斯分布，并以更高的渲染速度实现了更好的图像质量。 et.al.|[2503.16338](http://arxiv.org/abs/2503.16338)|null|
|**2025-03-20**|**Dynamic Point Maps: A Versatile Representation for Dynamic 3D Reconstruction**|DUSt3R最近表明，可以将多视图几何中的许多任务简化为对一对视点不变点图的预测，即在公共参考系中定义的像素对齐点云，包括估计相机内部和外部、重建3D场景和建立图像对应关系。这种公式优雅而强大，但无法处理动态场景。为了应对这一挑战，我们引入了动态点图（DPM）的概念，扩展了标准点图以支持4D任务，如运动分割、场景流估计、3D对象跟踪和2D对应。我们的主要直觉是，当引入时间时，有几种可能的空间和时间参考可用于定义点图。我们确定了这种组合的一个最小子集，可以通过网络进行回归来解决上述子任务。我们在合成和真实数据的混合上训练DPM预测器，并在视频深度预测、动态点云重建、3D场景流和对象姿态跟踪的不同基准上对其进行评估，从而实现最先进的性能。代码、模型和其他结果可在https://www.robots.ox.ac.uk/~vgg/研究/动态点地图/。 et.al.|[2503.16318](http://arxiv.org/abs/2503.16318)|null|
|**2025-03-20**|**From Monocular Vision to Autonomous Action: Guiding Tumor Resection via 3D Reconstruction**|手术自动化需要精确的指导和对场景的理解。文献中目前的方法依赖于笨重的深度相机来创建解剖图，但这并不能很好地应用于空间有限的临床应用。单眼相机很小，可以在狭小的空间内进行微创手术，但需要额外的处理来生成3D场景理解。我们提出了一种仅使用RGB图像创建目标解剖结构的分割点云的3D映射管道。为了确保最精确的重建，我们比较了不同结构-运动算法在绘制中央气道阻塞方面的性能，并在肿瘤切除的下游任务中测试了管道。在几个指标上，包括术后组织模型评估，我们的管道性能与RGB-D相机相当，在某些情况下甚至超过了它们的性能。这些有希望的结果表明，在使用单眼相机的微创手术中可以实现自动化引导。这项研究是迈向手术机器人完全自主的一步。 et.al.|[2503.16263](http://arxiv.org/abs/2503.16263)|null|
|**2025-03-20**|**3-D Image-to-Image Fusion in Lightsheet Microscopy by Two-Step Adversarial Network: Contribution to the FuseMyCells Challenge**|光片显微镜是一种强大的3D成像技术，它解决了传统光学和共聚焦显微镜的局限性，但在更大的深度存在穿透深度低和图像质量降低的问题。多视图光片显微镜通过组合多个视图来提高3D分辨率，但同时增加了复杂性和光子预算，导致潜在的光漂白和光毒性。FuseMyCells挑战赛与IEEE ISBI 2025会议联合举办，旨在对基于深度学习的解决方案进行基准测试，以融合来自单个3D视图的高质量3D体积，从而简化程序并节省光子预算。在这项工作中，我们提出了一个基于两步程序的FuseMyCells挑战。第一步处理图像的降采样版本以捕获整个感兴趣区域，而第二步使用基于补丁的方法进行高分辨率推理，结合对抗性损失来增强视觉效果。这种方法解决了与高数据分辨率、全局上下文的必要性和高频细节的保存相关的挑战。实验结果证明了我们方法的有效性，突出了其提高三维图像融合质量和扩展光片显微镜功能的潜力。细胞核和膜的平均SSIM分别大于0.85和0.91。 et.al.|[2503.16075](http://arxiv.org/abs/2503.16075)|null|
|**2025-03-20**|**Reconstructing In-the-Wild Open-Vocabulary Human-Object Interactions**|从单幅图像重建人-物交互（HOI）是计算机视觉的基础。由于缺乏3D数据，特别是受对象种类的限制，现有方法主要在室内场景中进行训练和测试，因此很难推广到具有广泛对象的现实世界场景。以前的3D HOI数据集的局限性主要是由于获取3D对象资产的困难。然而，随着从单个图像重建3D的发展，最近已经有可能从2D HOI图像重建各种物体。因此，我们提出了一种管道，用于从单个图像中注释细粒度的3D人类、对象及其交互。我们从现有的2D HOI数据集中注释了2.5k+的3D HOI资产，并在野生3D HOI数据集Open3DHOI中构建了第一个开放词汇表，作为未来的测试集。此外，我们设计了一种新的高斯HOI优化器，该优化器在学习接触区域的同时，有效地重建了人与物体之间的空间交互。除了3D HOI重建外，我们还为3D HOI理解提出了几个新任务，为未来的工作铺平了道路。数据和代码将在https://wenboran2002.github.io/3dhoi. et.al.|[2503.15898](http://arxiv.org/abs/2503.15898)|null|
|**2025-03-19**|**Uncertainty-Aware Diffusion Guided Refinement of 3D Scenes**|由于问题的严重欠约束性，从单个图像重建3D场景是一项根本不适定的任务。因此，当从新颖的相机视图渲染场景时，现有的单图像到3D重建方法会渲染不连贯和模糊的视图。当看不见的区域远离输入相机时，这个问题会加剧。在这项工作中，我们解决了现有单图像到3D场景前馈网络中的这些固有局限性。为了缓解由于输入图像视图之外的信息不足而导致的性能不佳，我们利用预训练的潜在视频扩散模型形式的强生成先验，对由可优化高斯参数表示的粗略场景进行迭代细化。为了确保生成的图像的风格和纹理与输入图像的样式和纹理对齐，我们在生成的图像和输入图像之间进行了实时傅里叶风格转换。此外，我们设计了一个语义不确定性量化模块，该模块计算每像素的熵，并生成不确定性图，用于从最自信的像素中指导细化过程，同时丢弃剩余的高度不确定性像素。我们在真实世界的场景数据集上进行了广泛的实验，包括域内RealEstate-10K和域外KITTI-v2，表明与现有的最先进方法相比，我们的方法可以提供更真实、高保真的新颖视图合成结果。 et.al.|[2503.15742](http://arxiv.org/abs/2503.15742)|null|
|**2025-03-19**|**CHROME: Clothed Human Reconstruction with Occlusion-Resilience and Multiview-Consistency from a Single Image**|从单个图像重建穿着衣服的人是计算机视觉中的一项基本任务，具有广泛的应用。尽管现有的单眼服装人体重建解决方案已经显示出有希望的结果，但它们通常依赖于人类受试者处于无遮挡环境的假设。因此，当在野外遇到遮挡图像时，这些算法会产生多视图不一致和碎片化的重建。此外，大多数单眼3D人体重建算法都利用SMPL注释等几何先验进行训练和推理，这在现实世界的应用中极具挑战性。为了解决这些局限性，我们提出了CHROME:基于单图像的具有遮挡弹性和多视图一致性的遮挡人体重建，这是一种新的管道，旨在从单个遮挡图像中重建具有多视图一致度的遮挡弹性3D人体，而不需要基础几何先验注释或3D监督。具体来说，CHROME利用多视图扩散模型，首先从被遮挡的输入中合成无遮挡的人体图像，与现成的姿态控制兼容，以在合成过程中明确地增强交叉视图的一致性。然后，训练3D重建模型来预测一组基于遮挡输入和合成视图的3D高斯分布，对齐交叉视图细节以产生连贯准确的3D表示。CHROME在新颖的视图合成（高达3db PSNR）和具有挑战性的条件下的几何重建方面都取得了显著的进步。 et.al.|[2503.15671](http://arxiv.org/abs/2503.15671)|null|
|**2025-03-18**|**SIR-DIFF: Sparse Image Sets Restoration with Multi-View Diffusion Model**|计算机视觉界已经开发了许多技术，用于从单视图退化的照片中数字恢复真实的场景信息，这是一项重要但极其不适的任务。在这项工作中，我们通过联合去噪同一场景的多张照片，从不同的角度处理图像恢复问题。我们的核心假设是，捕获共享场景的退化图像包含互补信息，当这些信息结合在一起时，可以更好地约束恢复问题。为此，我们实现了一个强大的多视图扩散模型，通过从多视图关系中提取丰富的信息，共同生成未损坏的视图。我们的实验表明，我们的多视图方法在图像去模糊和超分辨率任务上优于现有的单视图图像甚至基于视频的方法。至关重要的是，我们的模型经过训练，可以输出3D一致的图像，使其成为需要强大的多视图集成的应用程序的有前景的工具，如3D重建或姿态估计。 et.al.|[2503.14463](http://arxiv.org/abs/2503.14463)|null|
|**2025-03-18**|**Bolt3D: Generating 3D Scenes in Seconds**|我们提出了一种用于快速前馈3D场景生成的潜在扩散模型。给定一个或多个图像，我们的模型Bolt3D在单个GPU上直接在不到七秒的时间内对3D场景表示进行采样。我们通过利用强大且可扩展的现有2D扩散网络架构来生成一致的高保真3D场景表示，从而实现了这一目标。为了训练这个模型，我们通过将最先进的密集3D重建技术应用于现有的多视图图像数据集，创建了一个大规模的多视图一致的3D几何和外观数据集。与之前需要对每个场景进行优化以进行3D重建的多视图生成模型相比，Bolt3D将推理成本降低了300倍。 et.al.|[2503.14445](http://arxiv.org/abs/2503.14445)|null|

<p align=right>(<a href=#updated-on-20250323>back to top</a>)</p>

## Diffusion

|Publish Date|Title|Abstract|PDF|Code|
|---|---|---|---|---|
|**2025-03-20**|**Tokenize Image as a Set**|本文通过基于集合的标记化和分布建模，提出了一种全新的图像生成范式。与将图像序列化为具有统一压缩比的固定位置潜码的传统方法不同，我们引入了一种无序的令牌集表示，以基于区域语义复杂性动态分配编码容量。此TokenSet增强了全局上下文聚合，并提高了对局部扰动的鲁棒性。为了解决离散集建模的关键挑战，我们设计了一种对偶变换机制，将集双射转换为具有求和约束的固定长度整数序列。此外，我们提出了固定和离散扩散——第一个同时处理离散值、固定序列长度和求和不变性的框架——实现了有效的集分布建模。实验证明了我们的方法在语义感知表示和生成质量方面的优越性。我们的创新跨越了新颖的表示和建模策略，将视觉生成超越了传统的顺序令牌范式。我们的代码和模型可在以下网址公开获取https://github.com/Gengzigang/TokenSet. et.al.|[2503.16425](http://arxiv.org/abs/2503.16425)|**[link](https://github.com/Gengzigang/TokenSet)**|
|**2025-03-20**|**InfiniteYou: Flexible Photo Recrafting While Preserving Your Identity**|实现灵活和高保真的身份保留图像生成仍然是艰巨的，特别是使用FLUX等先进的扩散变换器（DiT）。我们介绍InfiniteYou（InfU），它是最早利用DiT完成此任务的健壮框架之一。InfU解决了现有方法的重大问题，如身份相似性不足、文本图像对齐不佳以及生成质量和美学低。InfU的核心是InfuseNet，它是一个通过残差连接将身份特征注入DiT基础模型的组件，在保持生成能力的同时增强了身份相似性。多阶段训练策略，包括使用合成单人多样本（SPMS）数据进行预训练和监督微调（SFT），进一步改善了文本图像对齐，提高了图像质量，并减轻了面部复制粘贴。大量实验表明，InfU达到了最先进的性能，超过了现有的基线。此外，InfU的即插即用设计确保了与各种现有方法的兼容性，为更广泛的社区做出了宝贵贡献。 et.al.|[2503.16418](http://arxiv.org/abs/2503.16418)|null|
|**2025-03-20**|**DreamTexture: Shape from Virtual Texture with Analysis by Augmentation**|DreamFusion通过结合生成模型和可微渲染的进步，为从虚拟视图进行无监督的3D重建建立了一种新的范式。然而，底层的多视图渲染以及大规模生成模型的监督在计算上很昂贵，而且受到的限制也很小。我们提出了DreamTexture，这是一种新颖的虚拟纹理形状方法，利用单眼深度线索重建3D对象。我们的方法通过将虚拟纹理与输入中的真实深度线索对齐来对输入图像进行纹理化，利用了现代扩散模型中编码的单眼几何的固有理解。然后，我们使用新的共形映射优化从虚拟纹理变形中重建深度，这减轻了内存密集型的体积表示。我们的实验表明，生成模型对单眼形状线索有理解，可以通过增强和对齐纹理线索来提取，这是一种新的单眼重建范式，我们称之为增强分析。 et.al.|[2503.16412](http://arxiv.org/abs/2503.16412)|null|
|**2025-03-20**|**VerbDiff: Text-Only Diffusion Models with Enhanced Interaction Awareness**|最近的大规模文本到图像扩散模型生成了逼真的图像，但由于其区分各种交互单词的能力有限，往往难以准确描绘人与物体之间的交互。在这项工作中，我们提出了VerbDiff来解决在文本到图像扩散模型中捕捉细微交互的挑战。VerbDiff是一种新颖的文本到图像生成模型，它削弱了交互词和对象之间的偏见，增强了对交互的理解。具体来说，我们将各种交互词从基于频率的锚词中分离出来，并利用生成图像中的局部交互区域来帮助模型在没有额外条件的情况下更好地捕捉不同单词的语义。我们的方法使模型能够准确理解人与物体之间的预期交互，生成与指定动词对齐的高质量交互图像。在HICO-DET数据集上进行的大量实验表明，与以前的方法相比，我们的方法是有效的。 et.al.|[2503.16406](http://arxiv.org/abs/2503.16406)|null|
|**2025-03-20**|**ScalingNoise: Scaling Inference-Time Search for Generating Infinite Videos**|视频扩散模型（VDM）有助于生成高质量的视频，目前的研究主要集中在通过提高数据质量、计算资源和模型复杂性在训练过程中进行缩放。然而，推理时间缩放受到的关注较少，大多数方法将模型限制为单代尝试。最近的研究发现，在生成过程中存在可以提高视频质量的“金噪声”。在此基础上，我们发现，指导VDM的缩放推理时间搜索以识别更好的噪声候选不仅可以评估当前步骤中生成的帧的质量，还可以通过参考先前多块中的锚帧来保留高级对象特征，从而提供长期价值。我们的分析表明，扩散模型天生具有通过改变去噪步骤来灵活调整计算的能力，甚至在奖励信号的指导下，一步去噪方法也能产生显著的长期效益。基于观察结果，我们提出了ScalingNoise，这是一种即插即用的推理时间搜索策略，可以为扩散采样过程识别黄金初始噪声，以提高全局内容一致性和视觉多样性。具体来说，我们执行一步去噪，将初始噪声转换为片段，随后利用由先前生成的内容锚定的奖励模型来评估其长期价值。此外，为了保持多样性，我们从倾斜的噪声分布中对候选者进行采样，该分布对有希望的噪声进行加权。通过这种方式，ScalingNoise显著减少了噪声引起的错误，确保了更连贯和时空一致的视频生成。对基准数据集的大量实验表明，所提出的ScalingNoise有效地提高了长视频的生成效率。 et.al.|[2503.16400](http://arxiv.org/abs/2503.16400)|null|
|**2025-03-20**|**Scale-wise Distillation of Diffusion Models**|我们提出了SwD，这是一个用于扩散模型（DM）的逐尺度蒸馏框架，它有效地将下一尺度预测思想应用于基于扩散的少步生成器。更详细地说，SwD受到了最近将扩散过程与隐式谱自回归相关的见解的启发。我们假设DM可以在较低的数据分辨率下启动生成，并在每个去噪步骤中逐步提高样本数量，而不会降低性能，同时显著降低计算成本。SwD自然地将这一想法整合到基于分布匹配的现有扩散蒸馏方法中。此外，我们通过引入一种新的补丁丢失来增强与目标分布的细粒度相似性，从而丰富了分布匹配方法家族。当应用于最先进的文本到图像扩散模型时，SwD接近两个全分辨率步骤的推理时间，在相同的计算预算下明显优于同行，这可以从自动化指标和人类偏好研究中得到证明。 et.al.|[2503.16397](http://arxiv.org/abs/2503.16397)|null|
|**2025-03-20**|**SV4D 2.0: Enhancing Spatio-Temporal Consistency in Multi-View Video Diffusion for High-Quality 4D Generation**|我们提出了Stable Video 4D 2.0（SV4D 2.0），这是一种用于动态3D资产生成的多视图视频扩散模型。与其前身SV4D相比，SV4D 2.0对遮挡和大运动更稳健，对真实世界的视频有更好的泛化能力，并在细节清晰度和时空一致性方面产生更高质量的输出。我们通过在多个方面引入关键改进来实现这一目标：1）网络架构：消除参考多视图的依赖性，设计3D和帧注意力的混合机制；2）数据：提高训练数据的质量和数量；3）训练策略：采用渐进式3D-4D训练以获得更好的泛化能力；4）4D优化：通过两阶段细化和渐进式帧采样处理3D不一致性和大运动。大量实验表明，SV4D 2.0在视觉和定量上都有显著的性能提升，与SV4D相比，在新视图视频合成和4D优化（-12%LPIPS和-24%FV4D）中实现了更好的细节（-14%LPIPS）和4D一致性（-44%FV4D）。项目页面：https://sv4d2.0.github.io. et.al.|[2503.16396](http://arxiv.org/abs/2503.16396)|null|
|**2025-03-20**|**Do Visual Imaginations Improve Vision-and-Language Navigation Agents?**|视觉和语言导航（VLN）代理的任务是使用自然语言指令在看不见的环境中导航。在这项工作中，我们研究了指令中隐含的子目标的视觉表示是否可以作为导航线索，并提高导航性能。为了综合这些视觉表示或想象，我们利用分段指令中包含的地标参考上的文本到图像扩散模型。这些想象被提供给VLN主体，作为一种附加的模态来充当地标线索，并添加了一种辅助损失，以明确地鼓励将这些与它们相应的指称表达联系起来。我们的研究结果显示，成功率（SR）增加了约1分，成功率增加了0.5分，按代理的反向路径长度（SPL）进行缩放。这些结果表明，与仅依赖语言指令相比，所提出的方法增强了视觉理解。我们工作的代码和数据可以在以下网址找到https://www.akhilperincherry.com/VLN-Imagine-website/. et.al.|[2503.16394](http://arxiv.org/abs/2503.16394)|null|
|**2025-03-20**|**LaPIG: Cross-Modal Generation of Paired Thermal and Visible Facial Images**|现代机器学习的成功，特别是在面部翻译网络中，在很大程度上取决于高质量、成对的大规模数据集的可用性。然而，获取足够的数据往往具有挑战性且成本高昂。受扩散模型在高质量图像合成中的最新成功和大型语言模型（LLM）的进步的启发，我们提出了一种称为LLM辅助配对图像生成（LaPIG）的新框架。该框架能够使用LLM生成的字幕构建全面、高质量的成对可见光和热图像。我们的方法包括三个部分：使用ArcFace嵌入的可见图像合成、使用潜在扩散模型（LDM）的热图像转换和使用LLM的字幕生成。我们的方法不仅生成多视图配对的可见光和热图像以增加数据多样性，而且在保持其身份信息的同时生成高质量的配对数据。我们通过与现有方法进行比较，在公共数据集上评估了我们的方法，证明了LaPIG的优越性。 et.al.|[2503.16376](http://arxiv.org/abs/2503.16376)|null|
|**2025-03-20**|**NuiScene: Exploring Efficient Generation of Unbounded Outdoor Scenes**|本文探讨了生成从城堡到高层建筑等广阔户外场景的任务。与室内场景生成不同，室内场景生成一直是先前工作的主要重点，室外场景生成带来了独特的挑战，包括场景高度的广泛变化以及对能够快速生成大型景观的方法的需求。为了解决这个问题，我们提出了一种高效的方法，将场景块编码为统一的向量集，提供了比现有方法中使用的空间结构化延迟更好的压缩和性能。此外，我们为无界生成训练了一个显式的外画模型，与之前的基于重采样的修复方案相比，该模型提高了一致性，同时通过消除额外的扩散步骤加快了生成速度。为了促进这项任务，我们策划了NuiScene43，这是一组小而高质量的场景，经过预处理后用于联合训练。值得注意的是，当在不同风格的场景中训练时，我们的模型可以在同一场景中融合不同的环境，如农村房屋和城市摩天大楼，突出了我们的策划过程利用异构场景进行联合训练的潜力。 et.al.|[2503.16375](http://arxiv.org/abs/2503.16375)|**[link](https://github.com/3dlg-hcvc/NuiScene)**|

<p align=right>(<a href=#updated-on-20250323>back to top</a>)</p>

## NeRF

|Publish Date|Title|Abstract|PDF|Code|
|---|---|---|---|---|
|**2025-03-19**|**GO-N3RDet: Geometry Optimized NeRF-enhanced 3D Object Detector**|我们提出了GO-N3RDet，这是一种通过神经辐射场增强的场景几何优化的多视图3D物体检测器。准确的3D对象检测的关键在于有效的体素表示。然而，由于遮挡和缺乏3D信息，从多视图2D图像构建3D特征具有挑战性。为了解决这个问题，我们引入了一种独特的3D位置信息嵌入体素优化机制来融合多视图特征。为了优先考虑目标区域的神经场重建，我们还为探测器的NeRF分支设计了一种双重重要性采样方案。我们还提出了一个不透明度优化模块，通过实施多视图一致性约束来进行精确的体素不透明度预测。此外，为了进一步提高跨多个视角的体素密度一致性，我们将射线距离作为加权因子，以最小化累积射线误差。我们独特的模块协同形成了一个端到端的神经模型，建立了基于NeRF的多视图3D检测的最新技术，并在ScanNet和ARKITCenes上进行了广泛的实验验证。代码将在以下网址提供https://github.com/ZechuanLi/GO-N3RDet. et.al.|[2503.15211](http://arxiv.org/abs/2503.15211)|null|
|**2025-03-14**|**NF-SLAM: Effective, Normalizing Flow-supported Neural Field representations for object-level visual SLAM in automotive applications**|我们提出了一种新颖的、仅限视觉的对象级SLAM框架，用于通过隐式符号距离函数表示3D形状的汽车应用。我们的主要创新包括通过归一化流网络增强标准神经表示。因此，通过仅具有16维潜码的紧凑网络，可以在特定类别的道路车辆上实现强大的表示能力。此外，通过对合成数据的比较实验证明，新提出的架构在仅存在稀疏和噪声数据的情况下表现出显著的性能改进。该模块嵌入到基于立体视觉的框架的后端，用于联合增量形状优化。损失函数由基于稀疏3D点的SDF损失、稀疏渲染损失和基于语义掩码的轮廓一致性项的组合给出。我们还利用语义信息来确定前端的关键点提取密度。最后，对真实世界数据的实验结果显示，与使用直接深度读数的替代框架相比，其性能准确可靠。所提出的方法仅在通过束调整获得的稀疏3D点上表现良好，即使在仅使用掩模一致性项的情况下，最终也能继续提供稳定的结果。 et.al.|[2503.11199](http://arxiv.org/abs/2503.11199)|null|
|**2025-03-13**|**RSR-NF: Neural Field Regularization by Static Restoration Priors for Dynamic Imaging**|动态成像涉及使用欠采样测量值随时重建时空对象。特别是，在动态计算机断层扫描（dCT）中，一次只能获得一个视角的单个投影，这使得逆问题非常具有挑战性。此外，地面实况动态数据通常要么不可用，要么太稀缺，无法用于监督学习技术。为了解决这个问题，我们提出了RSR-NF，它使用神经场（NF）来表示动态对象，并使用去噪正则化（RED）框架，通过学习的恢复算子将额外的静态深空间先验合并到变分公式中。我们使用基于ADMM的可变分裂算法来有效地优化变分目标。我们将RSR-NF与三种替代方案进行了比较：仅具有时间正则化的NF；最近的一种方法，使用对静态数据进行预训练的去噪器，将部分可分离的低秩表示与RED相结合；以及基于深度图像先验的模型。第一个比较展示了通过将NF表示与静态恢复先验相结合所实现的重建改进，而另外两个则展示了与dCT的最新技术相比的改进。 et.al.|[2503.10015](http://arxiv.org/abs/2503.10015)|null|
|**2025-03-11**|**Representing 3D Shapes With 64 Latent Vectors for 3D Diffusion Models**|通过变分自编码器（VAE）构建压缩的潜在空间是高效3D扩散模型的关键。本文介绍了COD-VAE，这是一种在不牺牲质量的情况下将3D形状编码为1D潜在向量的COmpact集的VAE。COD-VAE引入了一种两级自动编码器方案，以提高压缩和解码效率。首先，我们的编码器块通过中间点补丁将点云逐步压缩为紧凑的潜在向量。其次，我们的基于三平面的解码器从潜在向量重建密集的三平面，而不是直接解码神经场，大大降低了神经场解码的计算开销。最后，我们提出了不确定性引导的令牌修剪，通过在更简单的区域跳过计算来自适应地分配资源，提高了解码器的效率。实验结果表明，与基线相比，COD-VAE在保持质量的同时实现了16倍的压缩。这使得生成速度提高了20.8倍，突显出大量潜在矢量不是高质量重建和生成的先决条件。 et.al.|[2503.08737](http://arxiv.org/abs/2503.08737)|null|
|**2025-03-09**|**Gaussian RBFNet: Gaussian Radial Basis Functions for Fast and Accurate Representation and Reconstruction of Neural Fields**|DeepSDF和神经辐射场等神经场最近彻底改变了RGB图像和视频的新颖视图合成和3D重建。然而，实现高质量的表示、重建和渲染需要深度神经网络，而深度神经网络的训练和评估速度很慢。尽管已经提出了几种加速技术，但它们经常以速度换取内存。另一方面，基于高斯飞溅的方法加快了渲染时间，但在存储大量高斯参数所需的训练速度和内存方面仍然成本高昂。在本文中，我们介绍了一种新的神经表示方法，它在训练和推理时间都很快，而且很轻。我们的关键观察是，传统MLP中使用的神经元执行简单的计算（点积，然后是ReLU激活），因此需要使用宽和深MLP或高分辨率和高维特征网格来参数化复杂的非线性函数。我们在这篇论文中表明，通过用径向基函数（RBF）核替换传统神经元，只需一层这样的神经元，就可以实现2D（RGB图像）、3D（几何）和5D（辐射场）信号的高精度表示。该表示具有高度的并行性，可在低分辨率特征网格上运行，并且结构紧凑，内存高效。我们证明，所提出的新表示可以在不到15秒的时间内训练出3D几何表示，在不到十五分钟的时间内就可以训练出新的视图合成。在运行时，它可以在不牺牲质量的情况下以超过60 fps的速度合成新颖的视图。 et.al.|[2503.06762](http://arxiv.org/abs/2503.06762)|null|
|**2025-03-09**|**X-LRM: X-ray Large Reconstruction Model for Extremely Sparse-View Computed Tomography Recovery in One Second**|稀疏视图3D CT重建旨在从有限数量的2D X射线投影中恢复体积结构。现有的前馈方法受到基于CNN的架构容量有限和大规模训练数据集稀缺的限制。本文提出了一种用于极稀疏视图（<10视图）CT重建的X射线大重建模型（X-LRM）。X-LRM由两个关键部件组成：X-former和X-triplane。我们的X-former可以使用基于MLP的图像标记器和基于Transformer的编码器来处理任意数量的输入视图。然后，输出标记被上采样到我们的X三平面表示中，该表示将3D辐射密度建模为隐式神经场。为了支持X-LRM的训练，我们引入了Torso-16K，这是一个由各种躯干器官的16K多个体积投影对组成的大规模数据集。大量实验表明，X-LRM的性能比最先进的方法高出1.5 dB，速度快27倍，灵活性更好。此外，肺部分割任务的下游评估也表明了我们方法的实用价值。我们的代码、预训练模型和数据集将于https://github.com/caiyuanhao1998/X-LRM et.al.|[2503.06382](http://arxiv.org/abs/2503.06382)|null|
|**2025-03-05**|**Distilling Dataset into Neural Field**|利用大规模数据集对于训练高性能深度学习模型至关重要，但它也带来了巨大的计算和存储成本。为了克服这些挑战，数据集蒸馏已成为一种有前景的解决方案，它将大规模数据集压缩成一个较小的合成数据集，保留了训练所需的基本信息。本文提出了一种新的数据集提取参数化框架，称为神经场提取数据集（DDiF），它利用神经场存储大规模数据集的必要信息。由于神经场以坐标作为输入和输出量的独特性质，DDiF有效地保留了信息，并易于生成各种形状的数据。我们从理论上证实，当单个合成实例的使用预算相同时，DDiF表现出比以前的一些文献更大的表现力。通过广泛的实验，我们证明DDiF在几个基准数据集上取得了卓越的性能，扩展到图像域之外，包括视频、音频和3D体素。我们在发布代码https://github.com/aailab-kaist/DDiF. et.al.|[2503.04835](http://arxiv.org/abs/2503.04835)|**[link](https://github.com/aailab-kaist/ddif)**|
|**2025-02-27**|**RANGE: Retrieval Augmented Neural Fields for Multi-Resolution Geo-Embeddings**|地理位置表示的选择会显著影响各种地理空间任务模型的准确性，包括细粒度物种分类、种群密度估计和生物群落分类。最近的作品，如SatCLIP和GeoCLIP，通过将地理位置与共置图像进行对比对齐来学习这种表示。虽然这些方法非常有效，但在本文中，我们认为当前的训练策略未能完全捕捉到重要的视觉特征。我们从信息论的角度解释了为什么这些方法产生的嵌入会丢弃对许多下游任务很重要的关键视觉信息。为了解决这个问题，我们提出了一种新的检索增强策略，称为RANGE。我们的方法基于这样一种直觉，即可以通过组合来自多个看起来相似的位置的视觉特征来估计位置的视觉特性。我们在各种各样的任务中评估我们的方法。我们的结果表明，RANGE在大多数任务中表现优于现有的最先进的模型，并具有显著的优势。我们显示，分类任务的收益高达13.1%，回归任务的收益为0.145 $R^2$ 。我们所有的代码都将在GitHub上发布。我们的模型将在HuggingFace上发布。 et.al.|[2502.19781](http://arxiv.org/abs/2502.19781)|null|
|**2025-03-04**|**MedFuncta: Modality-Agnostic Representations Based on Efficient Neural Fields**|最近关于深度学习医学图像分析的研究几乎完全集中在基于网格或体素的数据表示上。我们通过引入MedFuncta来挑战这一常见选择，MedFuncta是一种基于神经场的模态无关连续数据表示。我们演示了如何通过利用医学信号中的冗余以及应用具有上下文缩减方案的高效元学习方法，将神经场从单个实例扩展到大型数据集。我们通过引入 $\omega_0$ -调度，提高重建质量和收敛速度，进一步解决了常用SIREN激活中的光谱偏差问题。我们在各种不同维度和模式的医学信号上验证了我们提出的方法（1D：心电图；2D：胸部X射线、视网膜OCT、眼底照相机、皮肤镜、结肠组织病理学、细胞显微镜；3D：脑MRI、肺CT），并成功证明我们可以解决这些表示的相关下游任务。我们还发布了一个超过550k个带注释神经场的大规模数据集，以促进这方面的研究。 et.al.|[2502.14401](http://arxiv.org/abs/2502.14401)|**[link](https://github.com/pfriedri/medfuncta)**|
|**2025-02-15**|**Implicit Neural Representations of Molecular Vector-Valued Functions**|分子有各种计算表示，包括数值描述符、字符串、图形、点云和曲面。每种表示方法都可以应用各种机器学习方法，从线性回归到与大型语言模型配对的图神经网络。为了补充现有的表示，我们通过向量值函数或n维向量场引入分子的表示，这些向量值函数由神经网络参数化，我们称之为分子神经场。与表面表征不同，分子神经场捕获蛋白质等大分子的外部特征和疏水核心。与离散图或点表示相比，分子神经场结构紧凑，分辨率无关，天生适合在空间和时间维度上进行插值。分子神经场继承的这些特性适用于包括基于所需形状、结构和组成生成分子，以及空间和时间中分子构象之间分辨率无关的插值在内的任务。在这里，我们为分子神经场提供了一个框架和概念证明，即使用自动解码器架构对蛋白质-配体复合物进行参数化和超分辨率重建，以及使用自动编码器架构将分子体积嵌入潜在空间。 et.al.|[2502.10848](http://arxiv.org/abs/2502.10848)|**[link](https://github.com/daenuprobst/minf)**|

<p align=right>(<a href=#updated-on-20250323>back to top</a>)</p>

[contributors-shield]: https://img.shields.io/github/contributors/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[contributors-url]: https://github.com/Vincentqyw/cv-arxiv-daily/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[forks-url]: https://github.com/Vincentqyw/cv-arxiv-daily/network/members
[stars-shield]: https://img.shields.io/github/stars/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[stars-url]: https://github.com/Vincentqyw/cv-arxiv-daily/stargazers
[issues-shield]: https://img.shields.io/github/issues/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[issues-url]: https://github.com/Vincentqyw/cv-arxiv-daily/issues

