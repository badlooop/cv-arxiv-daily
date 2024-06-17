[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]

## Updated on 2024.06.17
> Usage instructions: [here](./docs/README.md#usage)

<details>
  <summary>Table of Contents</summary>
  <ol>
    <li><a href=#3d>3D</a></li>
    <li><a href=#3d-reconstruction>3D Reconstruction</a></li>
    <li><a href=#diffusion>Diffusion</a></li>
    <li><a href=#nerf>NeRF</a></li>
  </ol>
</details>

## 3D

|Publish Date|Title|Abstract|PDF|Code|
|---|---|---|---|---|
|**2024-06-14**|**PUP 3D-GS: Principled Uncertainty Pruning for 3D Gaussian Splatting**|新视图合成的最新进展使实时渲染速度和高重建精度成为可能。3D高斯散射（3D-GS）是一种基于点的参数化3D场景表示，它将场景建模为大型的3D高斯集。复杂的场景可能包括数百万高斯，相当于巨大的存储和内存需求，这限制了3D-GS在资源有限的设备上的可行性。当前通过修剪高斯来压缩这些预训练模型的技术依赖于组合启发式来确定要删除哪些模型。在本文中，我们提出了一个原则性的空间敏感性修剪得分，它优于这些方法。它被计算为训练视图上的重构误差相对于每个高斯的空间参数的二阶近似。此外，我们提出了一种多轮修剪-细化流水线，该流水线可以应用于任何预训练的3D-GS模型，而无需改变训练流水线。在修剪了88.44%的高斯之后，我们观察到我们的PUP 3D-GS管道将3D-GS的平均渲染速度提高了2.65 $\times$ ，同时保留了更显著的前景信息，并实现了比以前在Mip NeRF 360、Tanks&Temples和Deep Blending数据集的场景上的修剪技术更高的图像质量指标。 et.al.|[2406.10219](http://arxiv.org/abs/2406.10219)|null|
|**2024-06-14**|**GaussianSR: 3D Gaussian Super-Resolution with 2D Diffusion Priors**|由于缺乏高分辨率数据，从低分辨率输入视图实现高分辨率新视图合成是一项具有挑战性的任务。以前的方法从低分辨率输入视图优化高分辨率神经辐射场（NeRF），但渲染速度较慢。在这项工作中，我们将我们的方法建立在3D高斯散射（3DGS）的基础上，因为它能够以更快的渲染速度生成高质量的图像。为了缓解用于更高分辨率合成的数据短缺，我们建议通过分数蒸馏采样（SDS）将2D知识蒸馏为3D，从而利用现成的2D扩散先验。然而，由于生成先验带来的随机性，将SDS直接应用于基于高斯的3D超分辨率会导致不期望的和冗余的3D高斯基元。为了缓解这个问题，我们引入了两种简单而有效的技术来减少SDS引入的随机扰动。具体来说，我们1）用退火策略缩小SDS中扩散时间步长的范围；2） 在致密化期间随机丢弃冗余的高斯基元。大量实验表明，我们提出的GaussainSR可以在合成数据集和真实世界数据集上仅用低分辨率输入就可以获得高质量的HRNVS结果。项目页面：https://chchnii.github.io/GaussianSR/ et.al.|[2406.10111](http://arxiv.org/abs/2406.10111)|null|
|**2024-06-14**|**D-NPC: Dynamic Neural Point Clouds for Non-Rigid View Synthesis from Monocular Video**|非刚性变形场景的动态重建和时空新颖视图合成近年来受到越来越多的关注。虽然现有的工作在多视角或隐形传送相机设置上实现了令人印象深刻的质量和性能，但大多数方法都无法有效、忠实地从随意的单目拍摄中恢复运动和外观。本文介绍了一种从单眼视频（如随意的智能手机捕捉）中进行动态新视图合成的新方法，为该领域做出了贡献。我们的方法将场景表示为 $\textit｛动态神经点云｝$ ，这是一种隐式的时间条件点分布，对静态和动态区域的单独散列编码神经特征网格中的局部几何结构和外观进行编码。通过从我们的模型中采样离散点云，我们可以使用快速可微分光栅化器和神经渲染网络有效地渲染高质量的新视图。与最近的工作类似，我们通过结合数据驱动的先验（如单目深度估计和对象分割）来解决单目捕获引起的运动和深度模糊，从而利用神经场景分析的进步。除了指导优化过程，我们还表明，可以利用这些先验来显式初始化我们的场景表示，从而大幅提高优化速度和最终图像质量。正如我们的实验评估所证明的那样，我们的动态点云模型不仅能够为交互式应用程序实现快速优化和实时帧速率，而且在单目基准序列上实现了有竞争力的图像质量。我们的项目页面位于https://moritzkappel.github.io/projects/dnpc. et.al.|[2406.10078](http://arxiv.org/abs/2406.10078)|null|
|**2024-06-14**|**RaNeuS: Ray-adaptive Neural Surface Reconstruction**|我们的目标是利用可微分辐射场，例如NeRF，除了生成标准的新视图渲染图外，还可以重建详细的3D表面。已经存在执行这种任务的相关方法，通常通过利用有符号距离场（SDF）。然而，最先进的方法仍然无法正确重建小规模的细节，如树叶、绳索和织物表面。考虑到不同的方法使用全局常数Eikonal正则化来公式化和优化从SDF到辐射场的投影，我们使用射线加权因子进行改进，以在建立完美SDF的基础上优先考虑渲染和过零曲面拟合。我们建议自适应地调整有符号距离场上的正则化，以便不令人满意的渲染光线不会强制执行无效的强Eikonal正则化，并允许来自具有良好学习的辐射区域的梯度有效地反向传播到SDF。因此，平衡这两个目标，以便生成准确而详细的曲面。此外，关于SDF中的过零表面和辐射场中的渲染点之间是否存在几何偏差，在优化过程中，投影也可以根据不同的3D位置进行调整。我们提出的\textit｛RaNeuS｝在合成和真实数据集上进行了广泛的评估，在新的视图合成和几何重建方面都取得了最先进的结果。 et.al.|[2406.09801](http://arxiv.org/abs/2406.09801)|**[link](https://github.com/wangyida/ra-neus)**|
|**2024-06-13**|**Modeling Ambient Scene Dynamics for Free-view Synthesis**|我们介绍了一种新的方法，用于从单目捕捉中动态自由地合成环境场景，为观看体验带来身临其境的质量。我们的方法建立在3D高斯散射（3DGS）的最新进展之上，该技术可以忠实地重建复杂的静态场景。以前扩展3DGS以表示动力学的尝试仅限于有界场景或需要多摄像机捕捉，并且往往无法推广到看不见的运动，限制了它们的实际应用。我们的方法通过利用环境运动的周期性来学习运动轨迹模型，再加上仔细的正则化，克服了这些限制。我们还提出了重要的实用策略，以提高基线3DGS静态重建的视觉质量，并提高GPU内存密集型学习的关键内存效率。我们展示了几个具有复杂纹理和精细结构元素的环境自然场景的高质量真实感新颖视图合成。 et.al.|[2406.09395](http://arxiv.org/abs/2406.09395)|null|
|**2024-06-13**|**Gaussian-Forest: Hierarchical-Hybrid 3D Gaussian Splatting for Compressed Scene Modeling**|最近，在新颖视图合成领域出现了3D高斯飞溅，它以基于点的方式表示场景，并通过光栅化进行渲染。与依赖光线跟踪的“辐射场”相比，这种方法显示出卓越的渲染质量和速度。然而，3D高斯的显式和非结构化性质对存储提出了重大挑战，阻碍了其更广泛的应用。为了应对这一挑战，我们引入了高斯森林建模框架，该框架将场景分层表示为混合3D高斯森林。每个混合高斯保留其唯一的显式属性，同时与其兄弟高斯共享隐式属性，从而用显著更少的变量优化参数化。此外，还设计了自适应生长和修剪策略，确保了在复杂区域的详细表现，并显著减少了所需的高斯数。大量实验表明，高斯森林不仅保持了相当的速度和质量，而且实现了超过10倍的压缩率，标志着高效场景建模的重大进步。代码可在https://github.com/Xian-Bei/GaussianForest. et.al.|[2406.08759](http://arxiv.org/abs/2406.08759)|null|
|**2024-06-12**|**From Chaos to Clarity: 3DGS in the Dark**|与来自低动态范围RGB图像的重建相比，来自原始图像的新颖视图合成提供了优越的高动态范围（HDR）信息。然而，未处理的原始图像中的固有噪声损害了3D场景表示的准确性。我们的研究表明，3D高斯散射（3DGS）特别容易受到这种噪声的影响，导致许多细长的高斯形状过度拟合噪声，从而显著降低重建质量和推理速度，尤其是在视图有限的场景中。为了解决这些问题，我们引入了一种新颖的自监督学习框架，该框架旨在从有限数量的噪声原始图像中重建HDR 3DGS。该框架通过集成噪声提取器并采用利用噪声分布先验的噪声鲁棒重建损失来增强3DGS。实验结果表明，在RawNeRF数据集上，在广泛的训练视图中，我们的方法在重建质量和推理速度方面都优于LDR/HDR 3DGS和以前最先进的（SOTA）自监督和监督预训练模型。代码可以在\url中找到{https://lizhihao6.github.io/Raw3DGS}. et.al.|[2406.08300](http://arxiv.org/abs/2406.08300)|null|
|**2024-06-12**|**Spatial Annealing Smoothing for Efficient Few-shot Neural Rendering**|具有混合表示的神经辐射场（NeRF）在重建场景以进行视图合成方面表现出了令人印象深刻的能力，提供了高效率。尽管如此，由于过拟合的问题，它们的性能在稀疏视图输入的情况下显著下降。虽然已经设计了各种正则化策略来应对这些挑战，但它们往往依赖于低效的假设，或者与混合模型不兼容。显然需要一种在混合框架内保持效率并提高稀疏视图弹性的方法。在本文中，我们介绍了一种精确高效的少镜头神经渲染方法，称为空间退火平滑正则化NeRF（SANeRF），它是专门为预滤波驱动的混合表示架构设计的。我们实现了样本空间大小从最初的大值的指数减少。这种方法对于稳定训练阶段的早期阶段至关重要，并大大有助于加强后续的细节细化过程。我们的大量实验表明，与当前的少镜头NeRF方法相比，SANeRF只需添加一行代码，就可以提供卓越的渲染质量和更快的重建速度。值得注意的是，SANeRF在Blender数据集上的PSNR比FreeNeRF高0.3 dB，同时实现了700倍的更快重建速度。 et.al.|[2406.07828](http://arxiv.org/abs/2406.07828)|**[link](https://github.com/pulangk97/SANeRF)**|
|**2024-06-11**|**Cinematic Gaussians: Real-Time HDR Radiance Fields with Depth of Field**|辐射场方法代表了从多视图照片重建复杂场景的技术状态。然而，这些重建通常受到以下一个或两个限制：首先，它们通常代表低动态范围（LDR）的场景，这限制了它们在均匀照明的环境中的使用，并阻碍了沉浸式观看体验。其次，假设所有场景元素都在输入图像中聚焦，它们对针孔相机模型的依赖带来了实际挑战，并使新视图合成过程中的重新聚焦变得复杂。针对这些限制，我们提出了一种基于3D高斯散射的轻量级方法，该方法利用具有不同曝光时间、光圈和焦距的场景的多视图LDR图像作为输入，来重建高动态范围（HDR）辐射场。通过结合基于薄镜头相机模型的高斯分析卷积以及色调映射模块，我们的重建能够以灵活的重新聚焦功能渲染HDR内容。我们证明，我们对HDR和景深的组合处理有助于实时电影渲染，优于现有技术。 et.al.|[2406.07329](http://arxiv.org/abs/2406.07329)|null|
|**2024-06-10**|**IllumiNeRF: 3D Relighting without Inverse Rendering**|现有的可重新照明视图合成方法——使用一组未知照明下的对象图像来恢复可以在目标照明下从新视点渲染的3D表示——基于反向渲染，并试图解开解释输入图像的对象几何结构、材料和照明。此外，这通常涉及通过可微分蒙特卡罗渲染进行优化，这是脆弱的，并且计算成本很高。在这项工作中，我们提出了一种更简单的方法：我们首先使用以照明为条件的图像扩散模型重新照明每个输入图像，然后用这些重新照明的图像重建神经辐射场（NeRF），从中我们在目标照明下绘制新的视图。我们证明，这一战略具有惊人的竞争力，并在多个重新照明基准上取得了最先进的结果。请参阅我们的项目页面https://illuminerf.github.io/. et.al.|[2406.06527](http://arxiv.org/abs/2406.06527)|null|

<p align=right>(<a href=#updated-on-20240617>back to top</a>)</p>

## 3D Reconstruction

|Publish Date|Title|Abstract|PDF|Code|
|---|---|---|---|---|
|**2024-06-14**|**A Two-Stage Masked Autoencoder Based Network for Indoor Depth Completion**|深度图像具有广泛的应用，如3D重建、自动驾驶、增强现实、机器人导航和场景理解。商品级深度相机对于明亮、有光泽、透明和遥远的表面来说很难感知深度。尽管现有的深度完成方法已经取得了显著的进展，但当应用于复杂的室内场景时，它们的性能是有限的。为了解决这些问题，我们提出了一种基于变压器的两步网络，用于室内深度完井。与现有的深度完成方法不同，我们采用了一种基于掩蔽自动编码器的自监督预训练编码器来学习缺失深度值的有效潜在表示；然后我们提出了一种基于令牌融合机制的解码器来从RGB和不完全深度图像中完成（即重建）全深度。与现有方法相比，我们提出的网络在Matterport3D数据集上实现了最先进的性能。此外，为了验证深度完成任务的重要性，我们将我们的方法应用于室内三维重建。代码、数据集和演示可在https://github.com/kailaisun/Indoor-Depth-Completion. et.al.|[2406.09792](http://arxiv.org/abs/2406.09792)|**[link](https://github.com/kailaisun/indoor-depth-completion)**|
|**2024-06-14**|**Grounding Image Matching in 3D with MASt3R**|图像匹配是3D视觉中所有性能最好的算法和管道的核心组成部分。然而，尽管匹配从根本上来说是一个3D问题，与相机姿势和场景几何体有着内在的联系，但它通常被视为2D问题。这是有道理的，因为匹配的目标是在2D像素场之间建立对应关系，但这似乎也是一个潜在的危险选择。在这项工作中，我们采取了不同的立场，并建议使用DUSt3R将匹配作为一项3D任务，DUSt3R是一种基于Transformers的最新强大的3D重建框架。基于点图回归，该方法在匹配具有极端视点变化的视图时表现出了令人印象深刻的稳健性，但精度有限。我们的目标是提高这种方法的匹配能力，同时保持其稳健性。因此，我们建议用一个新的头来增强DUSt3R网络，该头输出密集的局部特征，并用额外的匹配损失进行训练。我们进一步解决了密集匹配的二次复杂度问题，如果不仔细处理，这对于下游应用来说会变得非常缓慢。我们引入了一种快速倒数匹配方案，该方案不仅将匹配速度提高了几个数量级，而且具有理论保证，最后还改进了结果。大量实验表明，我们创造的MASt3R方法在多个匹配任务上显著优于现有技术。特别是，在极具挑战性的无地图定位数据集上，它在VCRE AUC方面击败了已发表的最佳方法30%（绝对改进）。 et.al.|[2406.09756](http://arxiv.org/abs/2406.09756)|null|
|**2024-06-13**|**Multiagent Multitraversal Multimodal Self-Driving: Open MARS Dataset**|大规模数据集推动了基于人工智能的自动驾驶汽车研究的最新进展。然而，这些数据集通常是从单个车辆一次性通过某个位置收集的，缺乏多智能体交互或重复穿越同一地点。这些信息可以带来自动驾驶汽车感知、预测和规划能力的变革性增强。为了弥补这一差距，我们与自动驾驶公司May Mobility合作，提出了MARS数据集，该数据集统一了多Agent、多行程和多模式自动驾驶汽车研究的场景。更具体地说，MARS是由在特定地理区域内行驶的自动驾驶汽车车队收集的。每辆车都有自己的路线，不同的车辆可能会出现在附近的位置。每辆车都配备了激光雷达和环绕RGB摄像头。我们在MARS中策划了两个子集：一个子集有助于多辆车同时出现在同一位置的协同驾驶，另一个子集通过多辆车对同一位置进行异步遍历来实现记忆回顾。我们进行了原位识别和神经重建实验。更重要的是，MARS引入了新的研究机遇和挑战，如多遍历3D重建、多智能体感知和无监督对象发现。我们的数据和代码可以在https://ai4ce.github.io/MARS/. et.al.|[2406.09383](http://arxiv.org/abs/2406.09383)|null|
|**2024-06-13**|**LRM-Zero: Training Large Reconstruction Models with Synthesized Data**|我们提出了LRM-Zero，这是一种完全在合成的3D数据上训练的大型重建模型（LRM），实现了高质量的稀疏视图3D重建。LRM Zero的核心是我们的程序3D数据集Zeroverse，它是通过随机纹理和增强（例如，高度场、布尔差和线框）从简单的原始形状自动合成的。与以前的3D数据集（例如，Ob厌恶对象）不同，Zeroverse通常由人类捕捉或制作来近似真实的3D数据，它完全忽略了真实的全局语义，但富含复杂的几何和纹理细节，这些细节在局部上与真实对象相似，甚至比真实对象更复杂。我们证明，用我们完全合成的Zeroverse训练的LRM Zero可以在真实世界物体的重建中实现高视觉质量，与在Ob厌恶对象上训练的模型相比具有竞争力。我们还分析了Zeroverse的几个关键设计选择，这些选择有助于LRM Zero的能力和训练稳定性。我们的工作表明，3D重建是3D视觉的核心任务之一，可以在没有真实世界对象语义的情况下解决。Zeroverse的程序合成代码和交互式可视化可在以下位置获得：https://desaixie.github.io/lrm-zero/. et.al.|[2406.09371](http://arxiv.org/abs/2406.09371)|null|
|**2024-06-13**|**OpenMaterial: A Comprehensive Dataset of Complex Materials for 3D Reconstruction**|深度学习的最新进展，如神经辐射场和隐式神经表示，极大地推动了3D重建领域的发展。然而，由于金属和玻璃等具有复杂光学特性的物体具有独特的镜面反射和透光特性，因此准确重建它们仍然是一项艰巨的挑战。为了促进这些挑战的解决方案的开发，我们引入了OpenMaterial数据集，该数据集包括1001个由295种不同材料制成的物体，包括导体、电介质、塑料及其粗糙变体，并在723种不同的照明条件下捕获。为此，我们使用了基于物理的渲染和实验室测量的折射率（IOR），并生成了紧密复制真实世界对象的高保真多视图图像。OpenMaterial提供了全面的注释，包括3D形状、材质类型、相机姿势、深度和对象遮罩。它是第一个大规模数据集，能够对具有不同和挑战性材料的物体上的现有算法进行定量评估，从而为开发能够处理复杂材料特性的3D重建算法铺平了道路。 et.al.|[2406.08894](http://arxiv.org/abs/2406.08894)|null|
|**2024-06-13**|**A Tangible Multi-Display Toolkit to Support the Collaborative Design Exploration of AV-Pedestrian Interfaces**|机器人和自动驾驶汽车等网络物理系统的出现为交互设计领域带来了新的机遇和挑战。尽管人们对以人为中心的开发的价值达成了共识，但缺乏有记录的、针对性的方法和工具，无法让多个利益相关者参与设计探索过程。在本文中，我们提出了一种使用有形的多显示器工具包的新方法。该工具包通过在多个显示器上编排计算机生成的图像，可以同时捕捉多个视角和视角（例如俯视图、第一人称行人视图）。参与者能够通过有形物体与模拟环境直接互动。同时，对象在物理上模拟界面的行为（例如通过集成LED显示器）。我们在与专家的设计会议上评估了该工具包，以收集有关AV行人界面设计的反馈和意见。本文报告了有形物体和多个显示器的组合如何支持协同设计探索。 et.al.|[2406.08733](http://arxiv.org/abs/2406.08733)|null|
|**2024-06-12**|**Human 3Diffusion: Realistic Avatar Creation via Explicit 3D Consistent Diffusion Models**|从单个RGB图像创建逼真的化身是一个有吸引力但具有挑战性的问题。由于其不适定性，最近的工作利用了在大型数据集上预训练的2D扩散模型的强大先验。尽管2D扩散模型表现出强大的泛化能力，但它们不能提供具有保证的3D一致性的多视图形状先验。我们提出了人类三维扩散：通过显式三维一致扩散创造真实的化身。我们的关键见解是，2D多视图扩散和3D重建模型为彼此提供了互补的信息，通过紧密耦合它们，我们可以充分利用这两个模型的潜力。我们介绍了一种新的图像条件生成的3D高斯飞溅重建模型，该模型利用了来自2D多视图扩散模型的先验，并提供了明确的3D表示，这进一步指导了2D反向采样过程，以获得更好的3D一致性。实验表明，我们提出的框架优于最先进的方法，能够从单个RGB图像中创建逼真的化身，实现几何和外观的高保真度。广泛的消融也验证了我们设计的有效性，（1）生成三维重建中的多视图二维先验条件和（2）通过显式三维表示对采样轨迹进行一致性细化。我们的代码和模型将于发布https://yuxuan-xue.com/human-3diffusion. et.al.|[2406.08475](http://arxiv.org/abs/2406.08475)|null|
|**2024-06-12**|**2.5D Multi-view Averaging Diffusion Model for 3D Medical Image Translation: Application to Low-count PET Reconstruction with CT-less Attenuation Correction**|正电子发射断层扫描（PET）是一种重要的临床成像工具，但不可避免地会给患者和医疗保健提供者带来辐射危害。减少示踪剂注射剂量和消除用于衰减校正的CT采集可以减少总辐射剂量，但通常会导致PET具有高噪声和偏差。因此，希望开发3D方法来将非衰减校正的低剂量PET（NAC-LDPET）转换为衰减校正的标准剂量PET（AC-SDPET）。最近，扩散模型已经成为一种新的最先进的图像到图像翻译的深度学习方法，优于传统的基于CNN的方法。然而，由于高计算成本和存储器负担，它在很大程度上局限于2D应用。为了应对这些挑战，我们开发了一种新的2.5D多视图平均扩散模型（MADM），用于3D图像到图像的翻译，并应用于NAC-LDPET到AC-SDPET的翻译。具体而言，MADM对轴向、冠状和矢状视图使用单独的扩散模型，在每个采样步骤中对其输出进行平均，以确保多个视图的3D生成质量。为了加快3D采样过程，我们还提出了一种策略，使用基于CNN的3D生成作为扩散模型的先验。我们对人类患者研究的实验结果表明，MADM可以生成高质量的3D翻译图像，优于以前基于CNN和基于扩散的基线方法。 et.al.|[2406.08374](http://arxiv.org/abs/2406.08374)|null|
|**2024-06-12**|**GPT4Rec: Graph Prompt Tuning for Streaming Recommendation**|在个性化推荐系统领域，适应不断变化的用户偏好以及不断涌入的新用户和项目的挑战至关重要。传统的模型通常依赖于静态训练测试方法，难以跟上这些动态需求的步伐。流式推荐，特别是通过连续图形学习，已经成为一种新颖的解决方案。然而，该领域的现有方法要么依赖于历史数据回放，由于严格的数据隐私规定，这越来越不切实际；或者无法有效解决过度稳定问题；或者依赖于模型隔离和扩展策略。为了解决这些困难，我们提出了GPT4Rec，一种用于流式推荐的图形提示调整方法。给定不断发展的用户-项目交互图，GPT4Rec首先将图模式分解为多个视图。在隔离不同视图中的特定交互模式和关系后，GPT4Rec利用轻量级图形提示，在用户项目图中的不同交互模式之间有效地指导模型。首先，采用节点级提示来指示模型适应图中单个节点的属性或属性的变化。其次，结构级提示指导模型适应图中更广泛的连接和关系模式。最后，创新性地设计了视图级提示，以便于聚合来自多个解纠缠视图的信息。这些提示设计使GPT4Rec能够综合对图形的全面理解，确保用户-项目交互的所有重要方面都得到考虑并有效集成。在四个不同的真实世界数据集上的实验证明了我们的建议的有效性和效率。 et.al.|[2406.08229](http://arxiv.org/abs/2406.08229)|null|
|**2024-06-12**|**Category-level Neural Field for Reconstruction of Partially Observed Objects in Indoor Environment**|通过各种成功案例，神经隐式表示在三维重建中引起了人们的关注。对于进一步的应用，如场景理解或编辑，一些作品已经显示出在对象组成重建方面的进展。尽管它们在观测区域具有优越的性能，但在重建部分观测到的对象时，它们的性能仍然有限。为了更好地处理这个问题，我们引入了类别级神经场，该神经场在场景中属于同一类别的对象之间学习有意义的公共3D信息。我们的主要想法是根据观察到的形状对对象进行子分类，以便更好地训练类别级模型。然后，我们利用神经场，通过选择基于射线的不确定性选择的代表性对象并与之对齐，来执行配准部分观测对象的挑战性任务。在模拟和真实世界数据集上的实验表明，我们的方法改进了几个类别的未观察零件的重建。 et.al.|[2406.08176](http://arxiv.org/abs/2406.08176)|null|

<p align=right>(<a href=#updated-on-20240617>back to top</a>)</p>

## Diffusion

|Publish Date|Title|Abstract|PDF|Code|
|---|---|---|---|---|
|**2024-06-14**|**VideoGUI: A Benchmark for GUI Automation from Instructional Videos**|图形用户界面（GUI）自动化在通过协助计算机任务来提高人类生产力方面有着重要的前景。现有的任务公式主要集中在可以由单一的、仅限语言的指令指定的简单任务上，例如“插入新幻灯片”。在这项工作中，我们介绍了VideoGUI，这是一种新的多模式基准测试，旨在评估以视觉为中心的GUI任务中的GUI助手。我们的基准测试源于高质量的网络教学视频，专注于涉及专业和新颖软件（如Adobe Photoshop或Stable Diffusion WebUI）和复杂活动（如视频编辑）的任务。VideoGUI通过分层过程评估GUI助手，允许识别它们可能失败的特定级别：（i）高级规划：在没有语言描述的情况下，从视觉条件重建过程子任务；（ii）中层规划：根据视觉状态（即屏幕截图）和目标生成精确的动作叙述序列；（iii）原子动作执行：执行特定动作，如准确点击指定元素。对于每个级别，我们在各个维度上设计评估指标，以提供清晰的信号，例如原子操作执行的单击、拖动、键入和滚动的各个性能。我们对VideoGUI的评估表明，即使是SoTA大型多模式模型GPT4o在以视觉为中心的GUI任务上也表现不佳，尤其是在高级规划方面。 et.al.|[2406.10227](http://arxiv.org/abs/2406.10227)|null|
|**2024-06-14**|**SatDiffMoE: A Mixture of Estimation Method for Satellite Image Super-resolution with Latent Diffusion Models**|在卫星图像的采集过程中，由于卫星成像系统的机载传感器，通常在空间分辨率和时间分辨率（采集频率）之间存在权衡。高分辨率卫星图像对于土地作物监测、城市规划、野火管理和各种应用都非常重要。在卫星成像中实现高时空分辨率是一项重要而富有挑战性的任务。随着扩散模型的出现，我们现在可以学习强大的生成先验来生成高分辨率的真实卫星图像，这也可以用于促进超分辨率任务。在这项工作中，我们提出了一种新的基于扩散的融合算法，称为\textbf｛SatDiffMoE｝，该算法可以将同一位置的任意数量的连续低分辨率卫星图像作为输入，并通过利用和融合来自不同时间点的互补信息，将它们融合成一个具有更精细细节的高分辨率重建图像。我们的算法非常灵活，允许对任意数量的低分辨率图像进行训练和推理。实验结果表明，与以前的方法相比，我们提出的SatDiffMoE方法不仅在各种数据集上实现了优越的卫星图像超分辨率任务性能，而且在降低模型参数的情况下提高了计算效率。 et.al.|[2406.10225](http://arxiv.org/abs/2406.10225)|null|
|**2024-06-14**|**Diffusion Synthesizer for Efficient Multilingual Speech to Speech Translation**|我们介绍了DiffuseST，这是一种低延迟、直接语音到速度的翻译系统，能够在从多种源语言翻译成英语时保留输入说话者的声音零样本。我们对该架构的合成器组件进行了实验，将基于Tacotron的合成器与新型的基于扩散的合成器进行了比较。我们发现，基于扩散的合成器可以将MOS和PESQ的音频质量指标分别提高23%和5%，同时保持可比较的BLEU分数。尽管参数计数增加了一倍多，但扩散合成器的延迟较低，使整个模型的运行速度比实时速度快5$\倍。 et.al.|[2406.10223](http://arxiv.org/abs/2406.10223)|null|
|**2024-06-14**|**DiffusionBlend: Learning 3D Image Prior through Position-aware Diffusion Score Blending for 3D Computed Tomography Reconstruction**|扩散模型在实际应用中用于大规模医学图像重建（如3D计算机断层扫描（CT））时面临重大挑战。由于对内存、时间和数据的要求很高，很难直接在高维数据的整个体积上训练扩散模型以获得有效的3D扩散先验。现有的工作利用手工制作的跨切片正则化在单个2D图像切片上的扩散先验，会牺牲z轴的一致性，从而导致沿z轴的严重伪影。在这项工作中，我们提出了一种新的框架，该框架能够通过位置感知的3D补丁扩散分数混合来学习3D图像先验，用于重建大规模3D医学图像。据我们所知，我们是第一个利用3D补丁扩散先验进行3D医学图像重建的人。对稀疏视图和有限角度CT重建的大量实验表明，我们的DiffusionBlend方法显著优于以前的方法，并在高维3D图像的真实世界CT重建问题上实现了最先进的性能（即， $256\乘以256\乘以500$ ）。我们的算法还具有比以前最先进的方法更好或相当的计算效率。 et.al.|[2406.10211](http://arxiv.org/abs/2406.10211)|null|
|**2024-06-14**|**Make It Count: Text-to-Image Generation with an Accurate Number of Objects**|尽管文本到图像扩散模型取得了前所未有的成功，但使用文本控制所描绘对象的数量却出奇地困难。这对于从技术文档到儿童书籍再到烹饪食谱图解的各种应用都很重要。生成对象正确计数从根本上来说是具有挑战性的，因为生成模型需要为对象的每个实例保持独立的同一性，即使几个对象看起来相同或重叠，然后在生成过程中隐式地执行全局计算。目前还不知道是否存在这样的表述。为了解决计数正确生成的问题，我们首先识别扩散模型中可以携带对象身份信息的特征。然后，我们在去噪过程中使用它们来分离和计数对象的实例，并检测过生成和欠生成。我们通过训练一个模型来修复后者，该模型基于现有对象的布局来预测缺失对象的形状和位置，并展示如何使用它来指导正确的对象计数去噪。我们的方法CountGen不依赖于外部来源来确定对象布局，而是使用扩散模型本身的先验知识，创建依赖于提示和依赖于种子的布局。在两个基准数据集上进行评估后，我们发现CountGen的计数精度大大优于现有基线的计数精度。 et.al.|[2406.10210](http://arxiv.org/abs/2406.10210)|null|
|**2024-06-14**|**Crafting Parts for Expressive Object Composition**|从稳定扩散、DALLE-2等大型生成模型生成文本到图像，由于其卓越的质量和广泛的知识库，已成为各种任务的通用基础。由于图像的合成和生成是创造性的过程，艺术家需要对生成的图像的各个部分进行控制。我们发现，仅仅在基本文本提示中添加有关零件的详细信息，要么会导致完全不同的图像（例如，丢失/不正确的身份），要么会忽略额外的零件详细信息。为了缓解这些问题，我们引入了PartCraft，它允许基于在基本文本提示中为对象指定的细粒度零件级细节来生成图像。这允许艺术家进行更多的控制，并通过组合独特的物体部分来实现新颖的物体构图。PartCraft首先通过对特定扩散过程中的对象区域进行去噪来定位对象部分。这使得每个零件标记都能够定位到正确的对象区域。在获得零件掩模后，我们基于细粒度的零件描述在每个零件区域中运行局部扩散过程，并将其组合以生成最终图像。PartCraft的所有阶段都基于重新调整预先训练的扩散模型的用途，这使其能够在没有训练的情况下在各个领域进行推广。我们通过视觉示例和与当代基线的定量比较，定性地证明了PartCraft提供的零件级控制的有效性。 et.al.|[2406.10197](http://arxiv.org/abs/2406.10197)|null|
|**2024-06-14**|**Training-free Camera Control for Video Generation**|我们提出了一种无训练且稳健的解决方案，为现成的视频扩散模型提供相机运动控制。与之前的工作不同，我们的方法不需要对相机注释的数据集进行任何监督微调，也不需要通过数据扩充进行自监督训练。相反，它可以与大多数预训练的视频扩散模型一起插入和播放，并以单个图像或文本提示作为输入生成相机可控的视频。我们工作的灵感来自于中间延迟对生成结果保持不变的布局，因此重新排列其中的噪声像素也会使输出内容重新分配。由于相机移动也可以被视为一种由视角变化引起的像素重排，如果视频的噪声潜伏期相应变化，则视频可以根据特定的相机移动进行重组。在此基础上，我们提出了我们的方法CamTrol，该方法能够对视频扩散模型进行稳健的相机控制。它是通过两个阶段的过程来实现的。首先，我们通过在三维点云空间中显式的相机移动来对图像布局重排进行建模。其次，我们使用由一系列重新排列的图像形成的噪声潜伏的布局先验来生成具有相机运动的视频。大量的实验已经证明了我们的方法在控制生成视频的相机运动方面的稳健性。此外，我们还表明，我们的方法可以在生成具有动态内容的3D旋转视频方面产生令人印象深刻的结果。项目页面位于https://lifedecoder.github.io/CamTrol/. et.al.|[2406.10126](http://arxiv.org/abs/2406.10126)|null|
|**2024-06-14**|**GaussianSR: 3D Gaussian Super-Resolution with 2D Diffusion Priors**|由于缺乏高分辨率数据，从低分辨率输入视图实现高分辨率新视图合成是一项具有挑战性的任务。以前的方法从低分辨率输入视图优化高分辨率神经辐射场（NeRF），但渲染速度较慢。在这项工作中，我们将我们的方法建立在3D高斯散射（3DGS）的基础上，因为它能够以更快的渲染速度生成高质量的图像。为了缓解用于更高分辨率合成的数据短缺，我们建议通过分数蒸馏采样（SDS）将2D知识蒸馏为3D，从而利用现成的2D扩散先验。然而，由于生成先验带来的随机性，将SDS直接应用于基于高斯的3D超分辨率会导致不期望的和冗余的3D高斯基元。为了缓解这个问题，我们引入了两种简单而有效的技术来减少SDS引入的随机扰动。具体来说，我们1）用退火策略缩小SDS中扩散时间步长的范围；2） 在致密化期间随机丢弃冗余的高斯基元。大量实验表明，我们提出的GaussainSR可以在合成数据集和真实世界数据集上仅用低分辨率输入就可以获得高质量的HRNVS结果。项目页面：https://chchnii.github.io/GaussianSR/ et.al.|[2406.10111](http://arxiv.org/abs/2406.10111)|null|
|**2024-06-14**|**Convergence to equilibrium for cross diffusion systems with nonlocal interaction**|我们研究了具有小交叉扩散效应的非线性扩散-聚集方程的双组分系统的弱解的存在性和平衡速率。聚集项被假设为纯粹有吸引力，并且在没有交叉扩散的情况下，流动朝着紧支撑的稳态呈指数收缩。我们的主要结果是，对于小的交叉扩散，系统仍然以略低的速率收敛到变形但仍然紧密支撑的稳态。我们的方法依赖于将PDE系统解释为双组分Wasserstein度量中的梯度流。能量由负责自扩散和非局部聚集的一致凸部分和产生交叉扩散的完全非凸部分组成；后者通过耦合参数 $\varepsilon>0$来缩放。证明的核心思想是对凸/非凸分裂进行$\varepsilon$ 相关的修改，并通过凸项建立对非凸项的控制。 et.al.|[2406.10075](http://arxiv.org/abs/2406.10075)|null|
|**2024-06-14**|**Partial stochastic resetting with refractory periods**|研究了部分复位过程中不应期的影响。在Poissonian部分重置的情况下，状态变量以不变的速率跳到离原点更近一个固定分数的值， $x\到x$。每次重置后，都会发生一个任意持续时间的固定不应期。我们推导了傅立叶-拉普拉斯空间中传播子的精确闭合形式表达式，该表达式显示出丰富的动力学特征，例如不仅与其他重置方案有关，而且与间歇运动有关。对于扩散过程，我们使用传播算子导出所有阶的$x$ 的时间相关矩的精确表达式。在后期，系统达到非平衡稳态，其形式为混合分布，将系统分为两个子种群；在静止状态的任何给定时间发现自己处于自由演化阶段的轨迹，以及处于难熔阶段的轨迹。与传统的重置相反，部分重置即使对于难治性亚群也会产生非平凡的稳态。研究了与稳态密度相关的矩和累积量，我们发现峰度的普遍最优值可以作为平均不应期时间的函数，仅由复位强度和平均复位间时间决定。所提出的结果可能与崩溃后有一段时间不活动的增长崩溃过程有关。 et.al.|[2406.10039](http://arxiv.org/abs/2406.10039)|null|

<p align=right>(<a href=#updated-on-20240617>back to top</a>)</p>

## NeRF

|Publish Date|Title|Abstract|PDF|Code|
|---|---|---|---|---|
|**2024-06-13**|**Well-posedness and regularity of solutions to neural field problems with dendritic processing**|我们研究了最近提出的神经场模型的解决方案，在该模型中，树突被建模为源自体细胞层的垂直纤维的连续体。由于电压通过具有非局部源的电缆方程沿树枝状方向传播，因此该模型具有各向异性扩散算子以及突触耦合的积分项。因此，相应的柯西问题与经典的神经场方程明显不同。我们证明了问题的弱公式允许一个唯一的解，嵌入估计类似于非线性局部反应扩散方程的嵌入估计。我们的分析依赖于无扩散问题的扰动弱解，即标准神经场，迄今为止尚未对其弱问题进行研究。我们找到了有扩散和无扩散问题的严格渐近估计，并证明了这两个模型的解在有限时间间隔上在适当的范数下保持接近。我们提供了微扰结果的数值证据。 et.al.|[2406.09222](http://arxiv.org/abs/2406.09222)|null|
|**2024-06-13**|**Preserving Identity with Variational Score for General-purpose 3D Editing**|我们提出了Piva（用变分分数蒸馏保持同一性），这是一种新的基于优化的方法，用于编辑基于扩散模型的图像和3D模型。具体来说，我们的方法受到了最近提出的2D图像编辑方法——德尔塔去噪分数（DDS）的启发。我们指出了DDS在二维和三维编辑中的局限性，这会导致细节丢失和过饱和。为了解决这一问题，我们提出了一个额外的分数提取术语，以强制执行身份保护。这导致了更稳定的编辑过程，逐步优化NeRF模型以匹配目标提示，同时保留关键的输入特征。我们证明了我们的方法在零样本图像和神经场编辑中的有效性。我们的方法成功地改变了视觉属性，添加了微妙和实质性的结构元素，转换了形状，并在标准的2D和3D编辑基准上取得了有竞争力的结果。此外，我们的方法没有施加任何约束，如掩蔽或预训练，使其与广泛的预训练扩散模型兼容。这允许进行多功能编辑，而不需要神经场到网格的转换，提供更用户友好的体验。 et.al.|[2406.08953](http://arxiv.org/abs/2406.08953)|null|
|**2024-06-12**|**Category-level Neural Field for Reconstruction of Partially Observed Objects in Indoor Environment**|通过各种成功案例，神经隐式表示在三维重建中引起了人们的关注。对于进一步的应用，如场景理解或编辑，一些作品已经显示出在对象组成重建方面的进展。尽管它们在观测区域具有优越的性能，但在重建部分观测到的对象时，它们的性能仍然有限。为了更好地处理这个问题，我们引入了类别级神经场，该神经场在场景中属于同一类别的对象之间学习有意义的公共3D信息。我们的主要想法是根据观察到的形状对对象进行子分类，以便更好地训练类别级模型。然后，我们利用神经场，通过选择基于射线的不确定性选择的代表性对象并与之对齐，来执行配准部分观测对象的挑战性任务。在模拟和真实世界数据集上的实验表明，我们的方法改进了几个类别的未观察零件的重建。 et.al.|[2406.08176](http://arxiv.org/abs/2406.08176)|null|
|**2024-06-12**|**OpenObj: Open-Vocabulary Object-Level Neural Radiance Fields with Fine-Grained Understanding**|近年来，人们对由视觉语言模型（VLM）促进的开放词汇三维场景重建产生了浓厚的兴趣，VLM在开放集检索中展示了非凡的能力。然而，现有的方法面临一些局限性：它们要么专注于学习逐点特征，导致语义理解模糊，要么只处理对象级重建，从而忽略对象内部的复杂细节。为了应对这些挑战，我们引入了OpenObj，这是一种创新的方法，用于构建具有细粒度理解的开放词汇表对象级神经辐射场（NeRF）。从本质上讲，OpenObj建立了一个健壮的框架，用于在对象级别进行高效和严密的场景建模和理解。此外，我们将零件级特征融入神经领域，从而实现物体内部的细致入微的表示。这种方法捕获对象级实例，同时保持细粒度的理解。在多个数据集上的结果表明，OpenObj在零样本语义分割和检索任务中取得了优异的性能。此外，OpenObj支持多尺度的真实世界机器人任务，包括全局移动和局部操纵。 et.al.|[2406.08009](http://arxiv.org/abs/2406.08009)|**[link](https://github.com/BIT-DYN/OpenObj)**|
|**2024-06-11**|**Image Neural Field Diffusion Models**|扩散模型在对复杂数据分布建模方面表现出了令人印象深刻的能力，与GANs相比具有几个关键优势，例如稳定的训练、更好地覆盖训练分布的模式，以及在没有额外训练的情况下解决反问题的能力。然而，大多数扩散模型学习固定分辨率图像的分布。我们建议通过在图像神经场上训练扩散模型来学习连续图像的分布，该模型可以以任何分辨率渲染，并显示出其相对于固定分辨率模型的优势。为了实现这一点，一个关键的挑战是获得一个代表真实感图像神经场的潜在空间。受最近几项技术的启发，我们提出了一种简单有效的方法，但有一些关键的变化，使图像神经场具有真实感。我们的方法可以用于将现有的潜在扩散自动编码器转换为图像神经场自动编码器。我们证明，图像神经场扩散模型可以使用混合分辨率图像数据集进行训练，优于固定分辨率扩散模型和超分辨率模型，并且可以有效地解决不同尺度条件下的逆问题。 et.al.|[2406.07480](http://arxiv.org/abs/2406.07480)|null|
|**2024-06-10**|**Space-Time Continuous PDE Forecasting using Equivariant Neural Fields**|最近，条件神经场（NeF）通过将解学习为条件NeF的潜在空间中的流，已成为偏微分方程的强大建模范式。尽管受益于NeFs的有利特性，如网格不可知性和时空连续动力学建模，但这种方法限制了将PDE的已知约束强加给解决方案的能力，例如对称性或边界条件，有利于建模的灵活性。相反，我们提出了一种基于时空连续NeF的求解框架，该框架通过在潜在空间中保留几何信息，尊重PDE的已知对称性。我们表明，将解建模为感兴趣组 $G$ 上的点云流，可以提高泛化和数据效率。我们验证了我们的框架很容易推广到看不见的空间和时间位置，以及初始条件的几何变换——在其他基于NeF的PDE预测方法失败的地方——并在一些具有挑战性的几何结构中超过基线进行改进。 et.al.|[2406.06660](http://arxiv.org/abs/2406.06660)|null|
|**2024-06-11**|**LOP-Field: Brain-inspired Layout-Object-Position Fields for Robotic Scene Understanding**|空间认知使动物具有非常高效的导航能力，这在很大程度上取决于对空间环境的场景级理解。最近，人们发现，大鼠大脑嗅后皮层的神经群体比场景中的物体更能强烈地适应空间布局。受局部场景中空间布局表示的启发，我们提出了实现布局对象位置（LOP）关联的LOP域，以对机器人场景理解的层次表示进行建模。在基础模型和隐式场景表示的支持下，神经场被实现为机器人的场景存储器，存储具有位置、对象和布局信息的场景的可查询表示。为了验证所建立的LOP关联，对该模型进行了测试，以使用定量指标从3D位置推断区域信息，实现了超过88%的平均准确度。还表明，与最先进的定位方法相比，所提出的使用区域信息的方法可以在文本和RGB输入的情况下实现改进的对象和视图定位结果。 et.al.|[2406.05985](http://arxiv.org/abs/2406.05985)|null|
|**2024-06-11**|**Grounding Continuous Representations in Geometry: Equivariant Neural Fields**|最近，神经场已经成为表示连续信号的强大建模范式。在条件神经领域中，一个领域由一个潜在变量表示，该变量对NeF进行了调节，否则其参数化将在整个数据集上共享。我们提出了基于交叉注意力变换器的等变神经场，其中NeFs以几何条件变量，即潜在点云为条件，从而实现从潜在到场的等变解码。我们的等变方法引入了一个可操纵性性质，通过该性质，场和势能都以几何为基础，并服从变换定律。如果场变换，势能相应地表示变换，反之亦然。至关重要的是，等变关系确保潜在的能够（1）真实地表示几何模式，允许在潜在空间中进行几何推理，（2）在空间相似的模式上进行权重共享，允许有效地学习场的数据集。与其他非等变NeF方法相比，使用分类实验和拟合整个数据集的能力验证了这些主要特性。我们通过展示独特的局部场编辑特性，进一步验证了ENF的潜力。 et.al.|[2406.05753](http://arxiv.org/abs/2406.05753)|null|
|**2024-06-06**|**ReFiNe: Recursive Field Networks for Cross-modal Multi-scene Representation**|最先进的多形状表示方法（单个模型“打包”多个对象）的常见权衡包括将建模精度与内存和存储进行权衡。我们展示了如何以比以前更高的精度和低内存使用率对表示为连续神经场的多个形状进行编码。我们方法的关键是利用对象自相似性的递归层次公式，从而产生高度压缩和高效的形状潜在空间。由于递归公式，我们的方法支持空间和全局到局部的潜在特征融合，而无需初始化和维护辅助数据结构，同时仍允许连续的字段查询，以实现光线跟踪等应用。在一组不同数据集上的实验中，我们提供了令人信服的定性结果，并展示了每个数据集使用单个网络的最先进的多场景重建和压缩结果。 et.al.|[2406.04309](http://arxiv.org/abs/2406.04309)|null|
|**2024-06-06**|**Vectorized Conditional Neural Fields: A Framework for Solving Time-dependent Parametric Partial Differential Equations**|变压器模型越来越多地用于求解偏微分方程（PDE）。已经提出了几种自适应方法，所有这些方法都存在变压器的典型问题，如二次记忆和时间复杂性。此外，用于PDE求解的所有流行体系结构都缺乏理想代理模型的几个期望性质中的至少一个，例如（i）对训练期间未看到的PDE参数的泛化，（ii）空间和时间零样本超分辨率，（iii）连续时间外推，（iv）对1D、2D和3D PDE的支持，以及（v）对更长时间展开的有效推断。为了解决这些局限性，我们提出了矢量化条件神经场（VCNeFs），它将时间相关偏微分方程的解表示为神经场。然而，与先前的方法相反，对于一组多个时空查询点，VCNeF并行计算它们的解决方案，并通过注意力机制对它们的依赖性进行建模。此外，VCNeF可以根据偏微分方程的初始条件和参数来调节神经场。一组广泛的实验表明，VCNeF与现有的基于ML的代理模型具有竞争力，并且往往优于现有的代理模型。 et.al.|[2406.03919](http://arxiv.org/abs/2406.03919)|**[link](https://github.com/jhagnberger/vcnef)**|

<p align=right>(<a href=#updated-on-20240617>back to top</a>)</p>

[contributors-shield]: https://img.shields.io/github/contributors/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[contributors-url]: https://github.com/Vincentqyw/cv-arxiv-daily/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[forks-url]: https://github.com/Vincentqyw/cv-arxiv-daily/network/members
[stars-shield]: https://img.shields.io/github/stars/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[stars-url]: https://github.com/Vincentqyw/cv-arxiv-daily/stargazers
[issues-shield]: https://img.shields.io/github/issues/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[issues-url]: https://github.com/Vincentqyw/cv-arxiv-daily/issues

