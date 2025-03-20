[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]

## Updated on 2025.03.20
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
|**2025-03-19**|**Temporal Regularization Makes Your Video Generator Stronger**|时间质量是视频生成的一个关键方面，因为它确保了跨帧的一致运动和逼真的动态。然而，实现高度的时间连贯性和多样性仍然具有挑战性。在这项工作中，我们首次探索了视频生成中的时间增强，并引入了FluxFlow进行初步研究，这是一种旨在提高时间质量的策略。FluxFlow在数据级别运行，应用受控的时间扰动，而不需要进行架构修改。对UCF-101和VBench基准的广泛实验表明，FluxFlow显著提高了各种视频生成模型（包括U-Net、DiT和基于AR的架构）的时间一致性和多样性，同时保持了空间保真度。这些发现强调了时间增强作为提高视频生成质量的一种简单而有效的方法的潜力。 et.al.|[2503.15417](http://arxiv.org/abs/2503.15417)|null|
|**2025-03-19**|**VideoGen-of-Thought: Step-by-step generating multi-shot video with minimal manual intervention**|目前的视频生成模型擅长短片，但由于视觉动态脱节和故事情节断裂，无法产生连贯的多镜头叙事。现有的解决方案要么依赖于大量的手动脚本/编辑，要么将单镜头保真度置于跨场景连续性之上，这限制了它们在电影类内容中的实用性。我们介绍了VideoGen of Thought（VGoT），这是一个循序渐进的框架，通过系统地解决三个核心挑战，从一句话中自动合成多镜头视频：（1）叙事碎片化：现有方法缺乏结构化的叙事。我们提出了动态故事情节建模，首先将用户提示转换为简洁的镜头描述，然后在五个领域（角色动态、背景连续性、关系演变、相机移动、HDR照明）将其细化为详细的电影规范，确保逻辑叙事进展和自我验证。（2） 视觉不一致性：现有的方法难以保持镜头之间的视觉一致性。我们的身份感知交叉镜头传播生成了身份保持肖像（IPP）令牌，这些令牌保持了角色的保真度，同时允许故事情节所决定的特征变化（表情、衰老）。（3） 过渡伪影：突然的镜头变化会破坏沉浸感。我们的相邻潜在过渡机制实施了边界感知重置策略，在过渡点处理相邻镜头的特征，在保持叙事连续性的同时实现无缝的视觉流动。VGoT生成的多镜头视频在镜头内面部一致性方面比最先进的基线高出20.4%，在风格一致性方面高出17.4%，同时实现了100%以上的跨镜头一致性，手动调整比其他选择少10倍。 et.al.|[2503.15138](http://arxiv.org/abs/2503.15138)|null|
|**2025-03-18**|**MusicInfuser: Making Video Diffusion Listen and Dance**|我们介绍MusicInfuser，这是一种生成与指定音乐曲目同步的高质量舞蹈视频的方法。我们没有试图设计和训练一个新的多模式音视频模型，而是展示了如何通过引入轻量级的音乐视频交叉注意力和低阶适配器来调整现有的视频扩散模型，使其与音乐输入相一致。与之前需要动作捕捉数据的工作不同，我们的方法只对舞蹈视频进行微调。MusicInfuser实现了高质量的音乐驱动视频生成，同时保留了底层模型的灵活性和生成能力。我们引入了一个使用视频LLM来评估舞蹈生成质量的多个维度的评估框架。项目页面和代码可在https://susunghong.github.io/MusicInfuser. et.al.|[2503.14505](http://arxiv.org/abs/2503.14505)|null|
|**2025-03-18**|**Lux Post Facto: Learning Portrait Performance Relighting with Conditional Video Diffusion and a Hybrid Dataset**|视频肖像重新照明仍然具有挑战性，因为结果需要具有照片级真实感和时间稳定性。这通常需要一个强大的模型设计，可以捕捉复杂的面部反射，并对高质量的成对视频数据集进行强化训练，例如动态一次一盏灯（OLAT）。在这项工作中，我们介绍了Lux Post Facto，这是一种新颖的肖像视频重新照明方法，可以产生逼真和时间一致的照明效果。从模型方面来看，我们设计了一个新的条件视频扩散模型，该模型基于最先进的预训练视频扩散模型构建，并采用了一种新的照明注入机制来实现精确控制。通过这种方式，我们利用强大的空间和时间生成能力，为不适定的再照明问题生成合理的解决方案。我们的技术使用由静态表情OLAT数据和野生肖像表演视频组成的混合数据集，共同学习再照明和时间建模。这避免了在不同光照条件下获取配对视频数据的需要。我们广泛的实验表明，我们的模型在真实感和时间一致性方面都能产生最先进的结果。 et.al.|[2503.14485](http://arxiv.org/abs/2503.14485)|null|
|**2025-03-18**|**MagicComp: Training-free Dual-Phase Refinement for Compositional Video Generation**|文本到视频（T2V）生成在扩散模型方面取得了重大进展。然而，现有的方法仍然难以准确绑定属性、确定空间关系和捕捉多个主体之间的复杂动作交互。为了解决这些局限性，我们提出了MagicComp，这是一种无需训练的方法，通过双相细化来增强合成T2V的生成。具体来说，（1）在条件化阶段：我们引入语义锚消歧，通过逐步将语义锚的方向向量注入原始文本嵌入，来强化特定主题的语义，解决主题间的歧义；（2） 在去噪阶段：我们提出了动态布局融合注意力，它集成了接地先验和模型自适应空间感知，通过掩蔽注意力调制将受试者灵活地绑定到他们的时空区域。此外，MagicComp是一种与模型无关且通用的方法，可以无缝集成到现有的T2V架构中。在T2V CompBench和VBench上进行的广泛实验表明，MagicComp的性能优于最先进的方法，突显了其在基于复杂提示和轨迹可控视频生成等应用中的潜力。项目页面：https://hong-yu-zhang.github.io/MagicComp-Page/. et.al.|[2503.14428](http://arxiv.org/abs/2503.14428)|null|
|**2025-03-18**|**Impossible Videos**|如今，合成视频被广泛用于补充现实世界视频的数据稀缺性和多样性。目前的合成数据集主要复制现实世界的场景，对不可能、反事实和反现实的视频概念探索不足。这项工作旨在回答两个问题：1）今天的视频生成模型能否有效地按照提示创建不可能的视频内容？2） 今天的视频理解模型是否足以理解不可能的视频？为此，我们介绍了IPV Bench，这是一种新的基准测试，旨在评估和促进视频理解和生成方面的进展。IPV Bench以全面的分类法为基础，包括4个领域、14个类别。它以各种场景为特色，无视物理、生物、地理或社会规律。基于分类法，构建了一个提示套件来评估视频生成模型，挑战它们的提示跟踪和创造力。此外，还策划了一个视频基准，以评估视频LLM理解不可能视频的能力，这特别需要对时间动态和世界知识进行推理。综合评估揭示了视频模型未来发展方向的局限性和见解，为下一代视频模型铺平了道路。 et.al.|[2503.14378](http://arxiv.org/abs/2503.14378)|null|
|**2025-03-18**|**VEGGIE: Instructional Editing and Reasoning Video Concepts with Grounded Generation**|最近的视频传播模型增强了视频编辑，但在统一的框架内处理教学编辑和各种任务（例如添加、删除、更改）仍然具有挑战性。在本文中，我们介绍了VEGGIE，这是一个基于指令的接地生成视频编辑器，它是一个简单的端到端框架，可以根据不同的用户指令统一视频概念编辑、接地和推理。具体来说，给定视频和文本查询，VEGGIE首先利用MLLM来解释指令中的用户意图，并将其与视频上下文联系起来，为像素空间响应生成特定于帧的接地任务查询。然后，扩散模型渲染这些计划，并生成与用户意图一致的编辑视频。为了支持多样化的任务和复杂的指令，我们采用了一种课程学习策略：首先将MLLM和视频扩散模型与大规模教学图像编辑数据对齐，然后对高质量的多任务视频数据进行端到端的微调。此外，我们引入了一种新的数据合成管道，用于生成成对的教学视频编辑数据，以进行模型训练。它通过利用图像到视频模型注入动态，将静态图像数据转换为多样化的高质量视频编辑样本。VEGGIE在具有不同编辑技能的教学视频编辑方面表现出色，作为一种多功能模型，其表现优于最佳教学基线，而其他模型则难以同时处理多任务。VEGGIE在视频对象基础和推理分割方面也表现出色，在其他基线失败的情况下。我们进一步揭示了多个任务是如何相互帮助的，并重点介绍了有前景的应用，如零样本多模式教学和上下文视频编辑。 et.al.|[2503.14350](http://arxiv.org/abs/2503.14350)|null|
|**2025-03-18**|**LeanVAE: An Ultra-Efficient Reconstruction VAE for Video Diffusion Models**|潜在视频扩散模型（LVDM）的最新进展通过利用视频变分自编码器（Video VAE）将复杂的视频数据压缩到紧凑的潜在空间中，彻底改变了视频生成。然而，随着LVDM训练的扩展，视频VAE的计算开销成为一个关键的瓶颈，特别是对于编码高分辨率视频。为了解决这个问题，我们提出了LeanVAE，这是一种新颖且超高效的视频VAE框架，引入了两项关键创新：（1）基于邻域感知前馈（NAF）模块和非重叠补丁操作的轻量级架构，大大降低了计算成本；（2）集成了小波变换和压缩感知技术，以提高重建质量。大量实验验证了LeanVAE在视频重建和生成方面的优势，特别是在提高现有视频VAE的效率方面。我们的模型提供的FLOP减少了50倍，推理速度提高了44倍，同时保持了具有竞争力的重建质量，为可扩展、高效的视频生成提供了见解。我们的型号和代码可在https://github.com/westlake-repl/LeanVAE et.al.|[2503.14325](http://arxiv.org/abs/2503.14325)|**[link](https://github.com/westlake-repl/leanvae)**|
|**2025-03-18**|**Concat-ID: Towards Universal Identity-Preserving Video Synthesis**|我们提出了Concat-ID，这是一个用于身份保持视频生成的统一框架。Concat ID采用变分自编码器来提取图像特征，这些特征与序列维度上的视频延迟相连接，仅利用3D自我关注机制，而不需要额外的模块。引入了一种新的跨视频配对策略和多阶段训练方案，在提高视频自然度的同时平衡身份一致性和面部可编辑性。大量实验表明，Concat ID在单身份和多身份生成方面都优于现有方法，并且可以无缝扩展到多主题场景，包括虚拟试穿和后台可控生成。Concat ID为身份保护视频合成建立了一个新的基准，为广泛的应用提供了一个通用且可扩展的解决方案。 et.al.|[2503.14151](http://arxiv.org/abs/2503.14151)|null|
|**2025-03-18**|**Fast Autoregressive Video Generation with Diagonal Decoding**|自回归变换器模型在视频生成方面表现出了令人印象深刻的性能，但它们的逐个令牌的顺序解码过程构成了一个主要的瓶颈，特别是对于由数万个令牌表示的长视频。在本文中，我们提出了对角解码（Diagonal Decoding，DiagD），这是一种无需训练的推理加速算法，用于自回归预训练模型，利用视频中的空间和时间相关性。我们的方法在时空令牌网格中沿对角线路径生成令牌，实现了每帧内的并行解码以及连续帧之间的部分重叠。所提出的算法是通用的，适用于各种生成模型和任务，同时对推理速度和视觉质量之间的权衡提供了灵活的控制。此外，我们提出了一种经济高效的微调策略，将模型的注意力模式与我们的解码顺序对齐，进一步缩小了小规模模型上的训练推理差距。在多个自回归视频生成模型和数据集上的实验表明，与简单的顺序解码相比，DiagD实现了高达10倍的加速，同时保持了相当的视觉保真度。 et.al.|[2503.14070](http://arxiv.org/abs/2503.14070)|null|

<p align=right>(<a href=#updated-on-20250320>back to top</a>)</p>

## 3D

|Publish Date|Title|Abstract|PDF|Code|
|---|---|---|---|---|
|**2025-03-19**|**Learn Your Scales: Towards Scale-Consistent Generative Novel View Synthesis**|传统的无深度多视图数据集是使用移动的单目相机捕获的，没有进行度量校准。在这种单眼设置中，相机位置的比例是模糊的。先前的方法通过各种ad-hoc归一化预处理步骤承认了多视图数据中的尺度模糊，但没有直接分析不正确的场景尺度对其应用的影响。在本文中，我们试图理解和解决尺度模糊在用于训练生成性新视图合成方法（GNVS）时的影响。在GNVS中，给定单个图像，场景或对象的新视图可以最小限度地合成，因此不受约束，需要使用生成方法。这些模型的生成性捕获了不确定性的各个方面，包括场景尺度的任何不确定性，这些不确定性充当了任务的干扰变量。我们通过分离场景尺度模糊对结果模型的影响，研究了从单幅图像采样时GNVS中场景尺度模糊的影响，并基于这些直觉定义了衡量生成视图尺度不一致性的新指标。然后，我们提出了一个框架，以端到端的方式与GNVS模型联合估计场景规模。经验表明，我们的方法减少了生成视图的尺度不一致性，而没有以前尺度归一化方法的复杂性或缺点。此外，我们还表明，消除这种模糊性可以提高生成的GNVS模型的图像质量。 et.al.|[2503.15412](http://arxiv.org/abs/2503.15412)|null|
|**2025-03-19**|**DiST-4D: Disentangled Spatiotemporal Diffusion with Metric Depth for 4D Driving Scene Generation**|当前的生成模型难以合成动态4D驾驶场景，这些场景同时支持时间外推和空间新视图合成（NVS），而无需对每个场景进行优化。一个关键的挑战在于找到一种高效且可推广的几何表示，将时间和空间合成无缝连接起来。为了解决这个问题，我们提出了DiST-4D，这是第一个用于4D驾驶场景生成的解纠缠时空扩散框架，它利用度量深度作为核心几何表示。DiST-4D将问题分解为两个扩散过程：DiST-T，它直接从过去的观测中预测未来的度量深度和多视图RGB序列；DiST-S，它通过仅在现有视点上训练来实现空间NVS，同时强制循环一致性。这种循环一致性机制引入了前后渲染约束，缩小了观察到的视点和看不到的视点之间的泛化差距。度量深度对于准确可靠的预测和准确的空间NVS至关重要，因为它提供了一种视图一致的几何表示，可以很好地推广到看不见的视角。实验表明，DiST-4D在时间预测和NVS任务中都达到了最先进的性能，同时在规划相关评估方面也提供了有竞争力的性能。 et.al.|[2503.15208](http://arxiv.org/abs/2503.15208)|null|
|**2025-03-19**|**MultiBARF: Integrating Imagery of Different Wavelength Regions by Using Neural Radiance Fields**|光学传感器应用通过数字化转型变得流行。将观测数据与现实世界的位置联系起来，并结合不同的图像传感器，对于使应用程序实用高效至关重要。然而，尝试不同传感器组合的数据准备需要高度的传感和图像处理专业知识。为了使不熟悉传感和图像处理的用户更容易进行数据准备，我们开发了MultiBARF。该方法通过在指定视点合成两对不同的传感器图像和深度图像来代替共配准和几何校准。我们的方法为两个成像器扩展了束调整神经辐射场（BARF），这是一种基于深度神经网络的新型视图合成方法。通过对可见光和热成像图像的实验，我们证明了我们的方法将这些传感器图像的两个颜色通道叠加在NeRF上。 et.al.|[2503.15070](http://arxiv.org/abs/2503.15070)|null|
|**2025-03-18**|**SplatVoxel: History-Aware Novel View Streaming without Temporal Training**|我们研究了稀疏视图视频中的新视图流问题，该问题旨在随着新的输入帧的到来，生成连续的高质量、时间一致的新视图序列。然而，现有的新颖视图合成方法在时间连贯性和视觉保真度方面存在困难，导致闪烁和不一致。为了应对这些挑战，我们引入了历史感知，利用之前的帧来重建场景，提高质量和稳定性。我们提出了一种混合飞溅体素前馈场景重建方法，该方法结合了高斯飞溅来随时间传播信息，并采用分层体素网格进行时间融合。使用将2D跟踪模型扩展到3D运动的运动图，高斯基元随着时间的推移被有效地扭曲，而稀疏体素变换器则以误差感知的方式整合新的时间观测值。至关重要的是，我们的方法不需要在多视图视频数据集上进行训练，这些数据集目前在大小和多样性方面受到限制，并且可以在推理时以历史感知的方式直接应用于稀疏视图视频流。我们的方法在静态和流式场景重建方面都达到了最先进的性能，在单个H100 GPU上以交互速率（15fps，350ms延迟）运行时，有效地减少了时间伪影和视觉伪影。项目页面：https://19reborn.github.io/SplatVoxel/ et.al.|[2503.14698](http://arxiv.org/abs/2503.14698)|null|
|**2025-03-18**|**Stable Virtual Camera: Generative View Synthesis with Diffusion Models**|我们提出了稳定的虚拟相机（Seva），这是一种多面手扩散模型，可以在给定任意数量的输入视图和目标相机的情况下创建场景的新颖视图。现有的工作难以生成大的视点变化或时间平滑的样本，同时依赖于特定的任务配置。我们的方法通过简单的模型设计、优化的训练配方和灵活的采样策略克服了这些局限性，这些策略在测试时跨视图合成任务进行泛化。因此，我们的样本保持了高一致性，而不需要额外的基于3D表示的蒸馏，从而简化了野外的视图合成。此外，我们证明我们的方法可以生成持续时间长达半分钟的高质量视频，并实现无缝循环闭合。广泛的基准测试表明，Seva在不同的数据集和设置中表现优于现有方法。 et.al.|[2503.14489](http://arxiv.org/abs/2503.14489)|null|
|**2025-03-18**|**Optimized 3D Gaussian Splatting using Coarse-to-Fine Image Frequency Modulation**|3D高斯散点（3DGS）技术彻底改变了新视图合成领域，它能够实现实时渲染的高质量场景重建。基于3DGS的技术通常受到高GPU内存和磁盘存储要求的困扰，这限制了它们在消费级设备上的实际应用。我们提出了Opti3DGS，这是一种新型的频率调制粗到细优化框架，旨在最小化用于表示场景的高斯基元的数量，从而减少内存和存储需求。Opti3DGS利用图像频率调制，最初强制使用粗略的场景表示，然后通过调制训练图像中的频率细节来逐步细化。在基线3DGS上，我们证明高斯分布平均减少了62%，训练GPU内存需求减少了40%，优化时间减少了20%，而不会牺牲视觉质量。此外，我们表明，我们的方法与许多基于3DGS的技术无缝集成，在保持并经常提高视觉质量的同时，持续减少高斯基元的数量。此外，Opti3DGS本身可以在不增加额外成本的情况下产生一定程度的细节场景表示，这是优化管道的自然副产品。结果和代码将公开。 et.al.|[2503.14475](http://arxiv.org/abs/2503.14475)|null|
|**2025-03-18**|**Improving Adaptive Density Control for 3D Gaussian Splatting**|3D高斯散斑（3DGS）已成为过去一年中最具影响力的作品之一。由于其高效和高质量的新颖视图合成能力，它在许多研究领域和应用中得到了广泛的应用。然而，3DGS仍然面临着正确管理场景重建过程中使用的高斯基元数量的挑战。遵循3D高斯散点的自适应密度控制（ADC）机制，在重建不足的区域创建新的高斯分布，同时修剪对渲染质量没有贡献的高斯分布。我们观察到，这些用于加密和修剪高斯分布的标准有时会引入伪影，从而导致渲染效果变差。我们特别观察重建后的背景或过拟合的前景区域。为了解决这两个问题，我们对自适应密度控制机制提出了三项新的改进。其中包括对场景范围计算的校正，该校正不仅依赖于相机位置，还包括指数级上升的梯度阈值以提高训练收敛性，以及基于重要性的修剪策略以避免背景伪影。通过这些自适应，我们证明了在使用相同数量的高斯基元时，渲染质量得到了提高。此外，随着我们的改进，训练收敛速度大大加快，训练时间是3DGS的两倍多，质量也比3DGS好。最后，我们的贡献很容易与3DGS的大多数现有衍生作品兼容，使其与未来的作品相关。 et.al.|[2503.14274](http://arxiv.org/abs/2503.14274)|null|
|**2025-03-18**|**Segmentation-Guided Neural Radiance Fields for Novel Street View Synthesis**|神经辐射场（NeRF）的最新进展在3D重建和新颖的视图合成方面显示出巨大的潜力，特别是对于室内和小规模场景。然而，将NeRF扩展到大规模户外环境带来了挑战，如瞬态物体、稀疏的相机和纹理以及不同的照明条件。本文针对复杂的城市环境，提出了一种针对室外街道场景的NeRF分割引导增强方法。我们的方法扩展了ZipNeRF，并利用Grounded SAM进行分割掩模生成，从而能够有效地处理瞬态对象、对天空进行建模和对地面进行正则化。我们还引入了外观嵌入，以适应视图序列中不一致的照明。实验结果表明，我们的方法优于基线ZipNeRF，以更少的伪影和更清晰的细节提高了新的视图合成质量。 et.al.|[2503.14219](http://arxiv.org/abs/2503.14219)|null|
|**2025-03-18**|**RoGSplat: Learning Robust Generalizable Human Gaussian Splatting from Sparse Multi-View Images**|本文介绍了RoGSplat，这是一种从稀疏的多视图图像中合成高保真度的看不见的人的新视图的新方法，同时不需要繁琐的按主题优化。与之前的方法不同，这些方法通常难以处理很少重叠的稀疏视图，并且在重建复杂的人体几何形状方面效果较差，所提出的方法能够在这种具有挑战性的条件下进行稳健的重建。我们的关键思想是将SMPL顶点提升到表示精确人体几何形状的密集可靠的3D先验点，然后基于这些点回归人体高斯参数。为了解释SMPL模型和图像之间可能存在的错位，我们建议通过利用像素级特征和体素级特征来预测图像对齐的3D先验点，并从中回归粗高斯分布。为了增强捕获高频细节的能力，我们进一步从粗略的3D高斯分布中渲染深度图，以帮助回归细粒度的像素高斯分布。在几个基准数据集上的实验表明，我们的方法在新颖的视图合成和跨数据集泛化方面优于最先进的方法。我们的代码可在https://github.com/iSEE-Laboratory/RoGSplat. et.al.|[2503.14198](http://arxiv.org/abs/2503.14198)|**[link](https://github.com/isee-laboratory/rogsplat)**|
|**2025-03-18**|**Lightweight Gradient-Aware Upscaling of 3D Gaussian Splatting Images**|我们介绍了一种为轻量级GPU上的3D高斯散斑（3DGS）量身定制的图像缩放技术。与3DGS相比，它实现了显著更高的渲染速度，并减少了3DGS重建中常见的伪影。我们的技术通过直接利用高斯的分析图像梯度进行基于梯度的双三次样条插值，在成本略有增加的情况下提高了低分辨率3DGS渲染的规模。该技术与特定的3DGS实现无关，以比基线实现高3x-4x的速率实现了新颖的视图合成。通过在多个数据集上的广泛实验，我们展示了3DGS图像的梯度感知放大所能实现的性能改进和高重建保真度。我们进一步演示了将梯度感知升级集成到3DGS模型的基于梯度的优化中，并分析了其对重建质量和性能的影响。 et.al.|[2503.14171](http://arxiv.org/abs/2503.14171)|null|

<p align=right>(<a href=#updated-on-20250320>back to top</a>)</p>

## 3D Reconstruction

|Publish Date|Title|Abstract|PDF|Code|
|---|---|---|---|---|
|**2025-03-18**|**Three-dimensional Reconstruction of the Lumbar Spine with Submillimeter Accuracy Using Biplanar X-ray Images**|从双平面X射线图像中重建负重条件下脊柱的三维结构对于脊柱疾病的临床评估具有重要意义。然而，目前的全自动重建方法精度低，无法满足临床应用标准。本研究开发并验证了一种从双平面X射线图像进行腰椎高精度3D重建的全自动方法。该方法涉及腰椎分解和从原始X射线图像中检测界标，然后是可变形模型和界标加权2D-3D配准方法。通过将CT分割的椎体模型与双平面X射线图像配准获得的金标准验证了重建精度。所提出的方法实现了0.80mm的3D重建精度，比主流方法有了显著改进。本研究将有助于腰椎负重位的临床诊断。 et.al.|[2503.14573](http://arxiv.org/abs/2503.14573)|null|
|**2025-03-18**|**SuperPC: A Single Diffusion Model for Point Cloud Completion, Upsampling, Denoising, and Colorization**|点云（PC）处理任务，如完成、上采样、去噪和着色，在自动驾驶和3D重建等应用中至关重要。尽管取得了长足的进步，但以前的方法通常独立地解决这些任务中的每一个，并使用单独的模型来解决单个问题。然而，这种孤立的方法无法解释这样一个事实，即不完整性、低分辨率、噪声和缺乏颜色等缺陷经常共存，每种缺陷都会影响和关联其他缺陷。简单地按顺序应用这些模型可能会导致每个模型的误差累积，同时增加计算成本。为了应对这些挑战，我们引入了SuperPC，这是第一个能够同时处理所有四个任务的统一扩散模型。我们的方法采用了一个三级条件扩散框架，并辅以一种新的空间混合融合策略，利用这四种缺陷之间的相关性进行同时、高效的处理。我们证明，SuperPC在所有四个单独的任务上都优于最先进的专业型号及其组合。 et.al.|[2503.14558](http://arxiv.org/abs/2503.14558)|null|
|**2025-03-18**|**SIR-DIFF: Sparse Image Sets Restoration with Multi-View Diffusion Model**|计算机视觉界已经开发了许多技术，用于从单视图退化的照片中数字恢复真实的场景信息，这是一项重要但极其不适的任务。在这项工作中，我们通过联合去噪同一场景的多张照片，从不同的角度处理图像恢复问题。我们的核心假设是，捕获共享场景的退化图像包含互补信息，当这些信息结合在一起时，可以更好地约束恢复问题。为此，我们实现了一个强大的多视图扩散模型，通过从多视图关系中提取丰富的信息，共同生成未损坏的视图。我们的实验表明，我们的多视图方法在图像去模糊和超分辨率任务上优于现有的单视图图像甚至基于视频的方法。至关重要的是，我们的模型经过训练，可以输出3D一致的图像，使其成为需要强大的多视图集成的应用程序的有前景的工具，如3D重建或姿态估计。 et.al.|[2503.14463](http://arxiv.org/abs/2503.14463)|null|
|**2025-03-18**|**Bolt3D: Generating 3D Scenes in Seconds**|我们提出了一种用于快速前馈3D场景生成的潜在扩散模型。给定一个或多个图像，我们的模型Bolt3D在单个GPU上直接在不到七秒的时间内对3D场景表示进行采样。我们通过利用强大且可扩展的现有2D扩散网络架构来生成一致的高保真3D场景表示，从而实现了这一目标。为了训练这个模型，我们通过将最先进的密集3D重建技术应用于现有的多视图图像数据集，创建了一个大规模的多视图一致的3D几何和外观数据集。与之前需要对每个场景进行优化以进行3D重建的多视图生成模型相比，Bolt3D将推理成本降低了300倍。 et.al.|[2503.14445](http://arxiv.org/abs/2503.14445)|null|
|**2025-03-18**|**Segmentation-Guided Neural Radiance Fields for Novel Street View Synthesis**|神经辐射场（NeRF）的最新进展在3D重建和新颖的视图合成方面显示出巨大的潜力，特别是对于室内和小规模场景。然而，将NeRF扩展到大规模户外环境带来了挑战，如瞬态物体、稀疏的相机和纹理以及不同的照明条件。本文针对复杂的城市环境，提出了一种针对室外街道场景的NeRF分割引导增强方法。我们的方法扩展了ZipNeRF，并利用Grounded SAM进行分割掩模生成，从而能够有效地处理瞬态对象、对天空进行建模和对地面进行正则化。我们还引入了外观嵌入，以适应视图序列中不一致的照明。实验结果表明，我们的方法优于基线ZipNeRF，以更少的伪影和更清晰的细节提高了新的视图合成质量。 et.al.|[2503.14219](http://arxiv.org/abs/2503.14219)|null|
|**2025-03-18**|**BG-Triangle: Bézier Gaussian Triangle for 3D Vectorization and Rendering**|微分渲染通过允许在渲染过程中计算梯度来实现高效优化，从而促进3D重建、逆渲染和神经场景表示学习。为了确保可微性，现有的解决方案使用平滑的概率代理（如体积或高斯基元）近似或重新制定传统的渲染操作。因此，由于缺乏明确的边界定义，它们很难保持锋利的边缘。我们提出了一种新的混合表示方法，即B’zier高斯三角形（BG Triangle），它将基于B‘zier三角形的矢量图形基元与基于高斯的概率模型相结合，在进行分辨率无关的可微渲染的同时保持精确的形状建模。我们提出一种鲁棒有效的不连续感知渲染技术，以减少对象边界的不确定性。我们还采用自适应密集化和修剪方案进行高效训练，同时可靠地处理细节水平（LoD）变化。实验表明，BG Triangle的渲染质量与3DGS相当，但具有优异的边界保持能力。更重要的是，BG Triangle使用的图元数量比其替代品少得多，展示了矢量化图形图元的好处，以及弥合经典和新兴表示之间差距的潜力。 et.al.|[2503.13961](http://arxiv.org/abs/2503.13961)|null|
|**2025-03-17**|**Using 3D reconstruction from image motion to predict total leaf area in dwarf tomato plants**|准确估算总叶面积（TLA）对于评估植物生长、光合活性和蒸腾作用至关重要。然而，由于其复杂的树冠，矮番茄等灌木植物仍然面临挑战。传统方法通常是劳动密集型的，对植物有害，或者在捕捉树冠复杂性方面有限。本研究评估了一种非破坏性方法，该方法结合了RGB图像的连续3D重建和机器学习，用于估算三种矮番茄品种的TLA：Mohamed、Hahms-Gelbe-Topftomate和Red Robin，这些品种在受控温室条件下生长。两个实验（春夏和秋冬）包括73株植物，通过“洋葱”方法进行了418次TLA测量。录制了高分辨率视频，每株植物使用500帧进行3D重建。使用四种算法（阿尔法形状、行进立方体、泊松、球旋转）处理点云，并使用七种回归模型对网格进行评估：多变量线性回归、拉索回归、岭回归、弹性网络回归、随机森林、极端梯度提升和多层感知器。使用极端梯度增强的阿尔法形状重建（ $\Alpha=3$）取得了最佳性能（$R^2=0.80$，$MAE=489 cm^2$）。交叉实验验证显示了稳健的结果（$R^2=0.56$，$MAE=579 cm^2$ ）。特征重要性分析将高度、宽度和表面积确定为关键预测因素。这种可扩展的自动化TLA估算方法适用于城市农业和精准农业，在自动化修剪、资源效率和可持续粮食生产方面具有应用价值。该方法在可变的环境条件和冠层结构中表现出了鲁棒性。 et.al.|[2503.13778](http://arxiv.org/abs/2503.13778)|null|
|**2025-03-17**|**Amodal3R: Amodal 3D Reconstruction from Occluded 2D Images**|大多数基于图像的3D对象重建器都假设对象是完全可见的，忽略了现实世界场景中常见的遮挡。本文介绍了Amodal3R，这是一种用于从部分观测中重建3D对象的条件3D生成模型。我们从一个“基础”3D生成模型开始，并对其进行扩展，以从被遮挡的对象中恢复出合理的3D几何和外观。我们引入了一种掩模加权多头交叉注意力机制，随后是一个遮挡感知注意力层，该层明确利用遮挡先验来指导重建过程。我们证明，通过仅在合成数据上进行训练，Amodal3R即使在真实场景中存在遮挡的情况下也能学习恢复完整的3D对象。它大大优于独立执行2D amodal完成然后进行3D重建的现有方法，从而为遮挡感知3D重建建立了一个新的基准。 et.al.|[2503.13439](http://arxiv.org/abs/2503.13439)|null|
|**2025-03-17**|**WideRange4D: Enabling High-Quality 4D Reconstruction with Wide-Range Movements and Scenes**|随着3D重建技术的快速发展，4D重建的研究也在不断推进，现有的4D重建方法可以生成高质量的4D场景。然而，由于获取多视图视频数据的挑战，目前的4D重建基准主要显示在有限场景内就地执行的动作，如跳舞。在实际场景中，许多场景涉及大范围的空间运动，突显了现有4D重建数据集的局限性。此外，现有的4D重建方法依赖于变形场来估计3D对象的动态，但变形场难以应对宽范围的空间运动，这限制了实现具有宽范围空间运动的高质量4D场景重建的能力。在本文中，我们专注于具有显著对象空间运动的4D场景重建，并提出了一种新的4D重建基准WideRange4D。该基准包括具有较大空间变化的丰富4D场景数据，可以更全面地评估4D生成方法的生成能力。此外，我们介绍了一种新的4D重建方法Progress4D，它可以在各种复杂的4D场景重建任务中生成稳定和高质量的4D结果。我们在WideRange4D上进行了定量和定性比较实验，表明我们的Progress4D优于现有的最先进的4D重建方法。项目：https://github.com/Gen-Verse/WideRange4D et.al.|[2503.13435](http://arxiv.org/abs/2503.13435)|**[link](https://github.com/gen-verse/widerange4d)**|
|**2025-03-17**|**AugMapNet: Improving Spatial Latent Structure via BEV Grid Augmentation for Enhanced Vectorized Online HD Map Construction**|自动驾驶需要了解基础设施要素，如车道和人行横道。为了安全导航，这种理解必须实时从传感器数据中得出，并需要以矢量化形式表示。学习型鸟瞰图（BEV）编码器通常用于将来自多个视图的一组相机图像组合成一个联合的潜在BEV网格。传统上，从这个潜在空间预测中间光栅地图，提供密集的空间监督，但需要后处理成所需的矢量化形式。最近的模型使用矢量化地图解码器直接将基础设施元素导出为折线，提供实例级信息。我们的方法，增强图网络（AugMapNet），提出了潜在的BEV网格增强，这是一种显著增强潜在BEV表示的新技术。AugMapNet比现有架构更有效地结合了矢量解码和密集空间监督，同时保持了与辅助监督一样易于集成和通用的特点。在nuScenes和Argoverse2数据集上的实验表明，矢量化地图预测性能在60米范围内比StreamMapNet基线提高了13.3%，在更大范围内提高了更大的性能。我们通过将我们的方法应用于另一个基线来确认可转移性，并发现了类似的改进。对潜在BEV网格的详细分析证实了AugMapNet更结构化的潜在空间，并展示了我们的新概念在纯粹性能改进之外的价值。代码很快就会发布。 et.al.|[2503.13430](http://arxiv.org/abs/2503.13430)|null|

<p align=right>(<a href=#updated-on-20250320>back to top</a>)</p>

## Diffusion

|Publish Date|Title|Abstract|PDF|Code|
|---|---|---|---|---|
|**2025-03-19**|**Active wetting transitions induced by rotational noise at solid interfaces**|我们研究了限制在刚性、不可穿透的平坦壁内的活性布朗粒子（ABP）的集合所显示的润湿转变。在我们使用布朗动力学模拟的计算研究中，壁粒子相互作用是通过短程排斥势实现的。壁上增强的旋转扩散被用作润湿转变的控制参数。增加壁旋转扩散会破坏完全润湿的稳定性，骨料会出现形态转变。我们观察到随着壁旋转扩散的增加，一系列形态转变：对称完全润湿（SCW）、不对称完全润湿（ACW）、部分润湿（PW）和液滴形成，以及干燥。在PW状态下，我们计算接触角作为活动和旋转噪声的函数。我们的分析表明，这些转变与稠密状态下粒子和气泡形成的动能波动增强有关。我们通过系统地分析序参数来进一步表征这些转变的性质。我们的工作表明，仅修改局部重取向率就足以诱导活性系统中的润湿转变。 et.al.|[2503.15476](http://arxiv.org/abs/2503.15476)|null|
|**2025-03-19**|**FP4DiT: Towards Effective Floating Point Quantization for Diffusion Transformers**|扩散模型（DM）彻底改变了文本到图像的视觉生成过程。然而，DM的巨大计算成本和模型占用阻碍了实际部署，特别是在边缘设备上。训练后量化（PTQ）是一种轻量级的方法，可以减轻这些负担，而不需要训练或微调。虽然最近的DM PTQ方法在基于整数的PTQ上实现了W4A8，但仍然存在两个关键局限性：首先，虽然大多数现有的DM PTO方法在经典的DM上进行评估，如Stable Diffusion XL、1.5或更早版本，这些方法使用卷积U网，但PixArt系列、浑源等较新的扩散变换器（DiT）模型采用了根本不同的变换器主干来实现卓越的图像合成。其次，整数（INT）量化在DM PTQ中占主导地位，但与网络权重和激活分布不一致，而浮点量化（FPQ）仍在研究中，但它有可能在DiT的低位设置中更好地对齐权重和激活分配。作为回应，我们介绍了FP4DiT，这是一种利用FPQ实现W4A6量化的PTQ方法。具体来说，我们扩展和推广了自适应舍入PTQ技术，以充分校准FPQ的权重量化，并证明DiT激活取决于输入补丁数据，因此需要稳健的在线激活量化技术。实验结果表明，FP4DiT在W4A6和W4A8精度上优于基于整数的PTQ，并在PixArt- $\alpha$、PixArt-$\Sigma$ 和浑源上生成了令人信服的视觉内容，这些内容基于HPSv2和CLIP等T2I指标。 et.al.|[2503.15465](http://arxiv.org/abs/2503.15465)|null|
|**2025-03-19**|**Di $\mathtt{[M]}$O: Distilling Masked Diffusion Models into One-step Generator**|掩蔽扩散模型（MDMs）已经成为一种强大的生成建模技术。尽管他们取得了显著的成果，但他们通常会经历几个步骤的缓慢推理。在本文中，我们提出了Di$\mathtt{[M]}$O，这是一种将掩蔽扩散模型提取为一步生成器的新方法。Di$\mathtt{[M]}$O解决了两个关键挑战：（1）使用中间步骤信息进行一步生成的难题，我们通过令牌级分布匹配来解决，该匹配在辅助模型的帮助下通过“政策框架”优化模型输出逻辑；以及（2）初始分布中缺乏熵，我们通过一种令牌初始化策略来解决这个问题，该策略在注入随机性的同时保持与教师培训分布的相似性。我们展示了Di$\mathtt{[M]}$ O在类条件和文本条件图像生成方面的有效性，令人印象深刻地实现了与多步教师输出相媲美的性能，同时大大缩短了推理时间。据我们所知，我们是第一个成功实现掩蔽扩散模型一步蒸馏的人，也是第一个将离散蒸馏应用于文本到图像生成的人，为高效的生成建模开辟了新的途径。 et.al.|[2503.15457](http://arxiv.org/abs/2503.15457)|null|
|**2025-03-19**|**MotionStreamer: Streaming Motion Generation via Diffusion-based Autoregressive Model in Causal Latent Space**|本文解决了文本条件流式运动生成的挑战，这要求我们根据可变长度的历史运动和传入文本预测下一步的人体姿势。现有的方法难以实现流式运动生成，例如，扩散模型受到预定义运动长度的约束，而基于GPT的方法由于离散化的非因果标记化而存在延迟响应和误差累积问题。为了解决这些问题，我们提出了MotionStreamer，这是一个将连续因果潜在空间纳入概率自回归模型的新框架。连续延迟减轻了离散化造成的信息损失，并有效地减少了长期自回归生成过程中的误差累积。此外，通过建立当前和历史运动延迟之间的时间因果关系，我们的模型充分利用了可用信息来实现准确的在线运动解码。实验表明，我们的方法优于现有的方法，同时提供了更多的应用，包括多轮生成、长期生成和动态运动合成。项目页面：https://zju3dv.github.io/MotionStreamer/ et.al.|[2503.15451](http://arxiv.org/abs/2503.15451)|null|
|**2025-03-19**|**Particle Pairing Caused Subdiffusion of Heavy Particles in the Imbalanced Hubbard Model**|不平衡Hubbard模型的特征是动态状态之间的过渡，这取决于两种不同粒子之间的质量比和耦合强度。轻粒子传输的减缓可归因于重粒子在高质量比和强耦合下引发的紧急有效无序。这种次扩散机制被解释为格里菲斯相，将这种效应与金属和绝缘区域的共存联系起来。在这里，我们研究了重粒子的动力学，这也揭示了次扩散行为，但无法在格里菲斯图中解释。我们证明，在动力学过程中，重粒子主要形成小团簇，主要是成对的，这降低了它们的传播速度，并在后期将含时扩散常数暂时转变为次扩散状态。驱动这一过程的粒子之间的必要吸引力可以在玻恩-奥本海默近似下理解。我们引入了一个经典的一维随机游走模型，该模型可以定量地再现强耦合区域中的次扩散动力学。 et.al.|[2503.15409](http://arxiv.org/abs/2503.15409)|null|
|**2025-03-19**|**Visual Persona: Foundation Model for Full-Body Human Customization**|我们介绍了Visual Persona，这是一个文本到图像全身人体定制的基础模型，给定一个野生的人体图像，在文本描述的指导下生成个体的不同图像。与之前只关注保留面部身份的方法不同，我们的方法捕获了详细的全身外观，与身体结构和场景变化的文本描述相一致。训练这个模型需要大规模的配对人类数据，每个人都有多张具有一致全身身份的图像，这是出了名的难以获得的。为了解决这个问题，我们提出了一个数据管理管道，利用视觉语言模型来评估全身外观的一致性，从而产生了Visual Persona-500K，这是一个包含10万个独特身份的58万对人类图像的数据集。为了实现精确的外观转换，我们引入了一种适用于预训练文本到图像扩散模型的变换器-编码器-解码器架构，该架构将输入图像扩展到不同的身体区域，将这些区域编码为局部外观特征，并将其独立投影到密集的身份嵌入中，以调节扩散模型，从而合成定制图像。Visual Persona始终超越现有方法，从野外输入中生成高质量的定制图像。广泛的消融研究验证了设计选择，我们展示了Visual Persona在各种下游任务中的多功能性。 et.al.|[2503.15406](http://arxiv.org/abs/2503.15406)|null|
|**2025-03-19**|**CCDP: Composition of Conditional Diffusion Policies with Guided Sampling**|模仿学习提供了一种有前景的方法，可以直接从数据中学习，而不需要显式的模型、模拟或详细的任务定义。在推理过程中，从学习到的分布中采样动作并在机器人上执行。然而，采样操作可能会因各种原因而失败，简单地重复采样步骤直到获得成功的操作可能效率低下。在这项工作中，我们提出了一种增强的采样策略，该策略优化了采样分布，以避免以前不成功的操作。我们证明，通过仅利用成功演示的数据，我们的方法可以推断出恢复操作，而不需要额外的探索行为或高级控制器。此外，我们利用扩散模型分解的概念，将主要问题（可能需要长期历史来管理故障）分解为学习、数据收集和推理中的多个更小、更易于管理的子问题，从而使系统能够适应可变的故障计数。我们的方法产生了一个低级控制器，当先前的样本不足时，该控制器会动态调整其采样空间以提高效率。我们在多个任务中验证了我们的方法，包括未知方向的开门、对象操作和按钮搜索场景，证明我们的方法优于传统基线。 et.al.|[2503.15386](http://arxiv.org/abs/2503.15386)|null|
|**2025-03-19**|**Material Decomposition in Photon-Counting Computed Tomography with Diffusion Models: Comparative Study and Hybridization with Variational Regularizers**|光子计数计算机断层扫描（PCCT）已成为一种有前景的成像技术，能够实现光谱成像和材料分解（MD）。然而，由于低光子计数和稀疏视图设置等限制，图像通常会受到低信噪比的影响。变分方法最小化了与手工正则化器耦合的数据拟合函数，但高度依赖于正则化器的选择。基于人工智能（AI）的方法，特别是卷积神经网络（CNN），现在被认为是最先进的方法，可以用作MD的端到端方法或隐含地学习先验知识。在过去的几年里，扩散模型（DM）在学习分布函数的生成模型领域占据主导地位。该分布函数可用作求解逆问题的先验。这项工作研究了在PCCT中使用DM作为MD任务的正则化器。通过扩散后验采样（DPS）可以实现MD。评估了三种基于DPS的方法——图像域两步DPS（im TDPS）、投影域两步DPS（proj TDPS）和一步DPS（ODPS）。前两种方法分两步执行MD：im TDPS通过DPS对光谱图像进行采样，然后执行基于图像的MD，而proj TDPS执行基于投影的MD，然后通过DPS对材料图像进行采样。最后一种方法ODPS直接从测量数据中采样材料图像。结果表明，与im TDPS和proj TDPS相比，ODPS具有更优的性能，可以提供更清晰、无噪声和无串扰的图像。此外，我们引入了一种新的混合ODPS方法，将DM先验与标准变分正则化器相结合，用于涉及训练数据集中缺失材料的场景。与标准变分方法相比，这种混合方法提高了材料重建质量。 et.al.|[2503.15383](http://arxiv.org/abs/2503.15383)|null|
|**2025-03-19**|**Fickian yet non-Gaussian diffusion in an annealed heterogeneous environment**|菲克-非高斯扩散是在各种生物和软物质系统中观察到的普遍现象。这种异常动力学通常归因于异质环境导致示踪剂颗粒扩散率的时空变化。虽然之前的研究主要集中在表现出空间或时间异质性的系统上，但这项工作通过引入一个基于退火极端景观的模型来同时考虑这两种异质性，从而弥合了这一差距。通过计算分析和分析推导的结合，我们研究了能源景观中空间和时间异质性的相互作用如何导致菲克式但非高斯的扩散。此外，我们证明，在存在时间环境波动的情况下，非均匀扩散不可避免地通过均匀化过程收敛到经典布朗运动。我们推导出了均匀化时间的解析表达式，该表达式是控制系统时空异质性的关键参数的函数。此外，我们量化了粒子间扩散的异质性，并研究了该模型的遍历特性，为复杂、异质系统的动力学提供了更深入的见解。 et.al.|[2503.15366](http://arxiv.org/abs/2503.15366)|null|
|**2025-03-19**|**Halide Perovskites as Spin-1 Dirac Materials**|卤化物钙钛矿是一类有前景的光电和光伏应用材料，由于其强烈的光吸收和较长的载流子扩散长度，表现出高功率转换效率。虽然已经研究了它们的晶体和电子结构的各个方面，但我们发现了一个以前被忽视的基本特性，这可能会显著影响它们的效率。我们证明卤化物钙钛矿实现了三维（3D）Lieb晶格，从而产生了自旋1费米子的带隙3D狄拉克锥。与传统的立方体结构相比，这导致有效质量减少了五倍，并且由于克莱因隧穿而抑制了载流子后向散射。我们的结论得到了CsPbBr $_3$和CsSnBr$_3$$的能带结构计算和角度分辨光电子能谱的支持。特别是，我们揭示了Lieb晶格平带的转变以及狄拉克锥光电发射中暗走廊效应的出现，该效应随着带隙从CsPbBr$_3$减小到CsSnBr$_3$$ 而增加。 et.al.|[2503.15343](http://arxiv.org/abs/2503.15343)|null|

<p align=right>(<a href=#updated-on-20250320>back to top</a>)</p>

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

<p align=right>(<a href=#updated-on-20250320>back to top</a>)</p>

[contributors-shield]: https://img.shields.io/github/contributors/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[contributors-url]: https://github.com/Vincentqyw/cv-arxiv-daily/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[forks-url]: https://github.com/Vincentqyw/cv-arxiv-daily/network/members
[stars-shield]: https://img.shields.io/github/stars/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[stars-url]: https://github.com/Vincentqyw/cv-arxiv-daily/stargazers
[issues-shield]: https://img.shields.io/github/issues/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[issues-url]: https://github.com/Vincentqyw/cv-arxiv-daily/issues

