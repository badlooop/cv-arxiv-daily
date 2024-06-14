[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]

## Updated on 2024.06.14
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
|**2024-06-13**|**Modeling Ambient Scene Dynamics for Free-view Synthesis**|我们介绍了一种新的方法，用于从单目捕捉中动态自由地合成环境场景，为观看体验带来身临其境的质量。我们的方法建立在3D高斯散射（3DGS）的最新进展之上，该技术可以忠实地重建复杂的静态场景。以前扩展3DGS以表示动力学的尝试仅限于有界场景或需要多摄像机捕捉，并且往往无法推广到看不见的运动，限制了它们的实际应用。我们的方法通过利用环境运动的周期性来学习运动轨迹模型，再加上仔细的正则化，克服了这些限制。我们还提出了重要的实用策略，以提高基线3DGS静态重建的视觉质量，并提高GPU内存密集型学习的关键内存效率。我们展示了几个具有复杂纹理和精细结构元素的环境自然场景的高质量真实感新颖视图合成。 et.al.|[2406.09395](http://arxiv.org/abs/2406.09395)|null|
|**2024-06-13**|**Gaussian-Forest: Hierarchical-Hybrid 3D Gaussian Splatting for Compressed Scene Modeling**|最近，在新颖视图合成领域出现了3D高斯飞溅，它以基于点的方式表示场景，并通过光栅化进行渲染。与依赖光线跟踪的“辐射场”相比，这种方法显示出卓越的渲染质量和速度。然而，3D高斯的显式和非结构化性质对存储提出了重大挑战，阻碍了其更广泛的应用。为了应对这一挑战，我们引入了高斯森林建模框架，该框架将场景分层表示为混合3D高斯森林。每个混合高斯保留其唯一的显式属性，同时与其兄弟高斯共享隐式属性，从而用显著更少的变量优化参数化。此外，还设计了自适应生长和修剪策略，确保了在复杂区域的详细表现，并显著减少了所需的高斯数。大量实验表明，高斯森林不仅保持了相当的速度和质量，而且实现了超过10倍的压缩率，标志着高效场景建模的重大进步。代码可在https://github.com/Xian-Bei/GaussianForest. et.al.|[2406.08759](http://arxiv.org/abs/2406.08759)|null|
|**2024-06-12**|**From Chaos to Clarity: 3DGS in the Dark**|与来自低动态范围RGB图像的重建相比，来自原始图像的新颖视图合成提供了优越的高动态范围（HDR）信息。然而，未处理的原始图像中的固有噪声损害了3D场景表示的准确性。我们的研究表明，3D高斯散射（3DGS）特别容易受到这种噪声的影响，导致许多细长的高斯形状过度拟合噪声，从而显著降低重建质量和推理速度，尤其是在视图有限的场景中。为了解决这些问题，我们引入了一种新颖的自监督学习框架，该框架旨在从有限数量的噪声原始图像中重建HDR 3DGS。该框架通过集成噪声提取器并采用利用噪声分布先验的噪声鲁棒重建损失来增强3DGS。实验结果表明，在RawNeRF数据集上，在广泛的训练视图中，我们的方法在重建质量和推理速度方面都优于LDR/HDR 3DGS和以前最先进的（SOTA）自监督和监督预训练模型。代码可以在\url中找到{https://lizhihao6.github.io/Raw3DGS}. et.al.|[2406.08300](http://arxiv.org/abs/2406.08300)|null|
|**2024-06-12**|**Spatial Annealing Smoothing for Efficient Few-shot Neural Rendering**|具有混合表示的神经辐射场（NeRF）在重建场景以进行视图合成方面表现出了令人印象深刻的能力，提供了高效率。尽管如此，由于过拟合的问题，它们的性能在稀疏视图输入的情况下显著下降。虽然已经设计了各种正则化策略来应对这些挑战，但它们往往依赖于低效的假设，或者与混合模型不兼容。显然需要一种在混合框架内保持效率并提高稀疏视图弹性的方法。在本文中，我们介绍了一种精确高效的少镜头神经渲染方法，称为空间退火平滑正则化NeRF（SANeRF），它是专门为预滤波驱动的混合表示架构设计的。我们实现了样本空间大小从最初的大值的指数减少。这种方法对于稳定训练阶段的早期阶段至关重要，并大大有助于加强后续的细节细化过程。我们的大量实验表明，与当前的少镜头NeRF方法相比，SANeRF只需添加一行代码，就可以提供卓越的渲染质量和更快的重建速度。值得注意的是，SANeRF在Blender数据集上的PSNR比FreeNeRF高0.3 dB，同时实现了700倍的更快重建速度。 et.al.|[2406.07828](http://arxiv.org/abs/2406.07828)|**[link](https://github.com/pulangk97/SANeRF)**|
|**2024-06-11**|**Cinematic Gaussians: Real-Time HDR Radiance Fields with Depth of Field**|辐射场方法代表了从多视图照片重建复杂场景的技术状态。然而，这些重建通常受到以下一个或两个限制：首先，它们通常代表低动态范围（LDR）的场景，这限制了它们在均匀照明的环境中的使用，并阻碍了沉浸式观看体验。其次，假设所有场景元素都在输入图像中聚焦，它们对针孔相机模型的依赖带来了实际挑战，并使新视图合成过程中的重新聚焦变得复杂。针对这些限制，我们提出了一种基于3D高斯散射的轻量级方法，该方法利用具有不同曝光时间、光圈和焦距的场景的多视图LDR图像作为输入，来重建高动态范围（HDR）辐射场。通过结合基于薄镜头相机模型的高斯分析卷积以及色调映射模块，我们的重建能够以灵活的重新聚焦功能渲染HDR内容。我们证明，我们对HDR和景深的组合处理有助于实时电影渲染，优于现有技术。 et.al.|[2406.07329](http://arxiv.org/abs/2406.07329)|null|
|**2024-06-10**|**IllumiNeRF: 3D Relighting without Inverse Rendering**|现有的可重新照明视图合成方法——使用一组未知照明下的对象图像来恢复可以在目标照明下从新视点渲染的3D表示——基于反向渲染，并试图解开解释输入图像的对象几何结构、材料和照明。此外，这通常涉及通过可微分蒙特卡罗渲染进行优化，这是脆弱的，并且计算成本很高。在这项工作中，我们提出了一种更简单的方法：我们首先使用以照明为条件的图像扩散模型重新照明每个输入图像，然后用这些重新照明的图像重建神经辐射场（NeRF），从中我们在目标照明下绘制新的视图。我们证明，这一战略具有惊人的竞争力，并在多个重新照明基准上取得了最先进的结果。请参阅我们的项目页面https://illuminerf.github.io/. et.al.|[2406.06527](http://arxiv.org/abs/2406.06527)|null|
|**2024-06-10**|**Lighting Every Darkness with 3DGS: Fast Training and Real-Time Rendering for HDR View Synthesis**|基于体积渲染的方法，如NeRF，擅长从RAW图像合成HDR视图，尤其是在夜间场景中。然而，它们的训练时间很长，并且由于密集的采样要求而无法执行实时渲染。3D高斯散射（3DGS）的出现实现了实时渲染和更快的训练。然而，由于其固有的缺点，直接使用3DGS实现基于RAW图像的视图合成是具有挑战性的：1）在夜间场景中，极低的SNR导致远景中的运动结构（SfM）估计较差；2） 球面谐波（SH）函数有限的表示能力不适合于RAW线性颜色空间；以及3）不准确的场景结构阻碍了诸如重新聚焦之类的下游任务。为了解决这些问题，我们提出了LE3D（用3DGS照亮每一个黑暗）。我们的方法提出了锥散射初始化来丰富SfM的估计，并用彩色MLP代替SH来表示RAW线性颜色空间。此外，我们引入了深度失真和远近正则化，以提高下游任务场景结构的准确性。这些设计使LE3D能够执行实时新颖的视图合成、HDR渲染、重新聚焦和色调映射更改。与以前基于体积渲染的方法相比，LE3D将训练时间减少到1%，并将2K分辨率图像的渲染速度提高了4000倍。代码和查看器可在中找到https://github.com/Srameo/LE3D . et.al.|[2406.06216](http://arxiv.org/abs/2406.06216)|**[link](https://github.com/srameo/le3d)**|
|**2024-06-09**|**Self-supervised Adversarial Training of Monocular Depth Estimation against Physical-World Attacks**|单目深度估计（MDE）在自动驾驶等应用中发挥着至关重要的作用。然而，各种攻击针对MDE模型，物理攻击对系统安全构成重大威胁。传统的对抗性训练方法需要地面实况标签，不能直接应用于缺乏地面实况深度的MDE模型。一些自监督模型强化技术（例如，对比学习）忽略了MDE的领域知识，导致性能次优。在这项工作中，我们为MDE模型引入了一种新的自监督对抗性训练方法，利用视图合成而不需要地面实况深度。我们通过在训练过程中引入L_0-norm-bounded扰动来增强对抗真实世界攻击的鲁棒性。我们根据专门为MDE设计的基于监督学习和基于对比学习的方法来评估我们的方法。我们对两个具有代表性的MDE网络的实验表明，它提高了对各种对抗性攻击的鲁棒性，对良性性能的影响最小。 et.al.|[2406.05857](http://arxiv.org/abs/2406.05857)|**[link](https://github.com/Bob-cheng/DepthModelHardening)**|
|**2024-06-09**|**RefGaussian: Disentangling Reflections from 3D Gaussian Splatting for Realistic Rendering**|三维高斯散射（3D-GS）在神经渲染、三维场景重建和新型视图合成等领域取得了显著的进展。然而，3D-GS在准确表示物理反射方面遇到了主要挑战，尤其是在真实世界场景中常见的全反射和半反射的情况下。这种限制导致反射被错误地视为具有物理存在的独立元素，从而导致不精确的重建。在此，为了应对这一挑战，我们建议RefGaussian将反射从3D-GS中分离出来，以便对反射进行逼真建模。具体来说，我们建议将场景划分为透射分量和反射分量，并使用两个球面谐波（SH）来表示这些分量。考虑到这种分解尚未完全确定，我们使用局部正则化技术来确保透射分量和反射分量的局部平滑，从而实现比3D-GS更合理的分解结果。实验结果表明，我们的方法实现了优越的新视图合成和准确的深度估计结果。此外，它能够利用场景编辑应用程序，确保高质量的结果和物理一致性。 et.al.|[2406.05852](http://arxiv.org/abs/2406.05852)|null|
|**2024-06-09**|**VCR-GauS: View Consistent Depth-Normal Regularizer for Gaussian Surface Reconstruction**|尽管3D高斯散射由于其逼真和高效的新颖视图合成而得到了广泛的研究，但从基于点的表示中提取高质量的曲面仍然是一项挑战。先前的工作通过结合现成法线估计器的几何先验来改进曲面。然而，存在两个主要限制：1）监督从3D高斯渲染的法线仅更新旋转参数，而忽略其他几何参数；2） 跨多个视图的预测法线图的不一致性可能导致严重的重建伪影。在本文中，我们提出了一种深度正则化子，它直接将法线与其他几何参数耦合，从而从法线正则化中得到几何参数的完全更新。我们进一步提出了一个置信项，以减轻多个视图中正常预测的不一致性。此外，我们还引入了一种致密化和分裂策略，以正则化3D高斯的大小和分布，从而实现更精确的表面建模。与基于高斯的基线相比，实验表明，我们的方法在更快的训练速度和100+FPS的渲染下获得了更好的重建质量，并保持了有竞争力的外观质量。我们的代码将在论文接受后开源。 et.al.|[2406.05774](http://arxiv.org/abs/2406.05774)|null|

<p align=right>(<a href=#updated-on-20240614>back to top</a>)</p>

## 3D Reconstruction

|Publish Date|Title|Abstract|PDF|Code|
|---|---|---|---|---|
|**2024-06-13**|**Multiagent Multitraversal Multimodal Self-Driving: Open MARS Dataset**|大规模数据集推动了基于人工智能的自动驾驶汽车研究的最新进展。然而，这些数据集通常是从单个车辆一次性通过某个位置收集的，缺乏多智能体交互或重复穿越同一地点。这些信息可以带来自动驾驶汽车感知、预测和规划能力的变革性增强。为了弥补这一差距，我们与自动驾驶公司May Mobility合作，提出了MARS数据集，该数据集统一了多Agent、多行程和多模式自动驾驶汽车研究的场景。更具体地说，MARS是由在特定地理区域内行驶的自动驾驶汽车车队收集的。每辆车都有自己的路线，不同的车辆可能会出现在附近的位置。每辆车都配备了激光雷达和环绕RGB摄像头。我们在MARS中策划了两个子集：一个子集有助于多辆车同时出现在同一位置的协同驾驶，另一个子集通过多辆车对同一位置进行异步遍历来实现记忆回顾。我们进行了原位识别和神经重建实验。更重要的是，MARS引入了新的研究机遇和挑战，如多遍历3D重建、多智能体感知和无监督对象发现。我们的数据和代码可以在https://ai4ce.github.io/MARS/. et.al.|[2406.09383](http://arxiv.org/abs/2406.09383)|null|
|**2024-06-13**|**LRM-Zero: Training Large Reconstruction Models with Synthesized Data**|我们提出了LRM-Zero，这是一种完全在合成的3D数据上训练的大型重建模型（LRM），实现了高质量的稀疏视图3D重建。LRM Zero的核心是我们的程序3D数据集Zeroverse，它是通过随机纹理和增强（例如，高度场、布尔差和线框）从简单的原始形状自动合成的。与以前的3D数据集（例如，Ob厌恶对象）不同，Zeroverse通常由人类捕捉或制作来近似真实的3D数据，它完全忽略了真实的全局语义，但富含复杂的几何和纹理细节，这些细节在局部上与真实对象相似，甚至比真实对象更复杂。我们证明，用我们完全合成的Zeroverse训练的LRM Zero可以在真实世界物体的重建中实现高视觉质量，与在Ob厌恶对象上训练的模型相比具有竞争力。我们还分析了Zeroverse的几个关键设计选择，这些选择有助于LRM Zero的能力和训练稳定性。我们的工作表明，3D重建是3D视觉的核心任务之一，可以在没有真实世界对象语义的情况下解决。Zeroverse的程序合成代码和交互式可视化可在以下位置获得：https://desaixie.github.io/lrm-zero/. et.al.|[2406.09371](http://arxiv.org/abs/2406.09371)|null|
|**2024-06-13**|**OpenMaterial: A Comprehensive Dataset of Complex Materials for 3D Reconstruction**|深度学习的最新进展，如神经辐射场和隐式神经表示，极大地推动了3D重建领域的发展。然而，由于金属和玻璃等具有复杂光学特性的物体具有独特的镜面反射和透光特性，因此准确重建它们仍然是一项艰巨的挑战。为了促进这些挑战的解决方案的开发，我们引入了OpenMaterial数据集，该数据集包括1001个由295种不同材料制成的物体，包括导体、电介质、塑料及其粗糙变体，并在723种不同的照明条件下捕获。为此，我们使用了基于物理的渲染和实验室测量的折射率（IOR），并生成了紧密复制真实世界对象的高保真多视图图像。OpenMaterial提供了全面的注释，包括3D形状、材质类型、相机姿势、深度和对象遮罩。它是第一个大规模数据集，能够对具有不同和挑战性材料的物体上的现有算法进行定量评估，从而为开发能够处理复杂材料特性的3D重建算法铺平了道路。 et.al.|[2406.08894](http://arxiv.org/abs/2406.08894)|null|
|**2024-06-13**|**A Tangible Multi-Display Toolkit to Support the Collaborative Design Exploration of AV-Pedestrian Interfaces**|机器人和自动驾驶汽车等网络物理系统的出现为交互设计领域带来了新的机遇和挑战。尽管人们对以人为中心的开发的价值达成了共识，但缺乏有记录的、针对性的方法和工具，无法让多个利益相关者参与设计探索过程。在本文中，我们提出了一种使用有形的多显示器工具包的新方法。该工具包通过在多个显示器上编排计算机生成的图像，可以同时捕捉多个视角和视角（例如俯视图、第一人称行人视图）。参与者能够通过有形物体与模拟环境直接互动。同时，对象在物理上模拟界面的行为（例如通过集成LED显示器）。我们在与专家的设计会议上评估了该工具包，以收集有关AV行人界面设计的反馈和意见。本文报告了有形物体和多个显示器的组合如何支持协同设计探索。 et.al.|[2406.08733](http://arxiv.org/abs/2406.08733)|null|
|**2024-06-12**|**Human 3Diffusion: Realistic Avatar Creation via Explicit 3D Consistent Diffusion Models**|从单个RGB图像创建逼真的化身是一个有吸引力但具有挑战性的问题。由于其不适定性，最近的工作利用了在大型数据集上预训练的2D扩散模型的强大先验。尽管2D扩散模型表现出强大的泛化能力，但它们不能提供具有保证的3D一致性的多视图形状先验。我们提出了人类三维扩散：通过显式三维一致扩散创造真实的化身。我们的关键见解是，2D多视图扩散和3D重建模型为彼此提供了互补的信息，通过紧密耦合它们，我们可以充分利用这两个模型的潜力。我们介绍了一种新的图像条件生成的3D高斯飞溅重建模型，该模型利用了来自2D多视图扩散模型的先验，并提供了明确的3D表示，这进一步指导了2D反向采样过程，以获得更好的3D一致性。实验表明，我们提出的框架优于最先进的方法，能够从单个RGB图像中创建逼真的化身，实现几何和外观的高保真度。广泛的消融也验证了我们设计的有效性，（1）生成三维重建中的多视图二维先验条件和（2）通过显式三维表示对采样轨迹进行一致性细化。我们的代码和模型将于发布https://yuxuan-xue.com/human-3diffusion. et.al.|[2406.08475](http://arxiv.org/abs/2406.08475)|null|
|**2024-06-12**|**2.5D Multi-view Averaging Diffusion Model for 3D Medical Image Translation: Application to Low-count PET Reconstruction with CT-less Attenuation Correction**|正电子发射断层扫描（PET）是一种重要的临床成像工具，但不可避免地会给患者和医疗保健提供者带来辐射危害。减少示踪剂注射剂量和消除用于衰减校正的CT采集可以减少总辐射剂量，但通常会导致PET具有高噪声和偏差。因此，希望开发3D方法来将非衰减校正的低剂量PET（NAC-LDPET）转换为衰减校正的标准剂量PET（AC-SDPET）。最近，扩散模型已经成为一种新的最先进的图像到图像翻译的深度学习方法，优于传统的基于CNN的方法。然而，由于高计算成本和存储器负担，它在很大程度上局限于2D应用。为了应对这些挑战，我们开发了一种新的2.5D多视图平均扩散模型（MADM），用于3D图像到图像的翻译，并应用于NAC-LDPET到AC-SDPET的翻译。具体而言，MADM对轴向、冠状和矢状视图使用单独的扩散模型，在每个采样步骤中对其输出进行平均，以确保多个视图的3D生成质量。为了加快3D采样过程，我们还提出了一种策略，使用基于CNN的3D生成作为扩散模型的先验。我们对人类患者研究的实验结果表明，MADM可以生成高质量的3D翻译图像，优于以前基于CNN和基于扩散的基线方法。 et.al.|[2406.08374](http://arxiv.org/abs/2406.08374)|null|
|**2024-06-12**|**GPT4Rec: Graph Prompt Tuning for Streaming Recommendation**|在个性化推荐系统领域，适应不断变化的用户偏好以及不断涌入的新用户和项目的挑战至关重要。传统的模型通常依赖于静态训练测试方法，难以跟上这些动态需求的步伐。流式推荐，特别是通过连续图形学习，已经成为一种新颖的解决方案。然而，该领域的现有方法要么依赖于历史数据回放，由于严格的数据隐私规定，这越来越不切实际；或者无法有效解决过度稳定问题；或者依赖于模型隔离和扩展策略。为了解决这些困难，我们提出了GPT4Rec，一种用于流式推荐的图形提示调整方法。给定不断发展的用户-项目交互图，GPT4Rec首先将图模式分解为多个视图。在隔离不同视图中的特定交互模式和关系后，GPT4Rec利用轻量级图形提示，在用户项目图中的不同交互模式之间有效地指导模型。首先，采用节点级提示来指示模型适应图中单个节点的属性或属性的变化。其次，结构级提示指导模型适应图中更广泛的连接和关系模式。最后，创新性地设计了视图级提示，以便于聚合来自多个解纠缠视图的信息。这些提示设计使GPT4Rec能够综合对图形的全面理解，确保用户-项目交互的所有重要方面都得到考虑并有效集成。在四个不同的真实世界数据集上的实验证明了我们的建议的有效性和效率。 et.al.|[2406.08229](http://arxiv.org/abs/2406.08229)|null|
|**2024-06-12**|**Category-level Neural Field for Reconstruction of Partially Observed Objects in Indoor Environment**|通过各种成功案例，神经隐式表示在三维重建中引起了人们的关注。对于进一步的应用，如场景理解或编辑，一些作品已经显示出在对象组成重建方面的进展。尽管它们在观测区域具有优越的性能，但在重建部分观测到的对象时，它们的性能仍然有限。为了更好地处理这个问题，我们引入了类别级神经场，该神经场在场景中属于同一类别的对象之间学习有意义的公共3D信息。我们的主要想法是根据观察到的形状对对象进行子分类，以便更好地训练类别级模型。然后，我们利用神经场，通过选择基于射线的不确定性选择的代表性对象并与之对齐，来执行配准部分观测对象的挑战性任务。在模拟和真实世界数据集上的实验表明，我们的方法改进了几个类别的未观察零件的重建。 et.al.|[2406.08176](http://arxiv.org/abs/2406.08176)|null|
|**2024-06-12**|**FaithFill: Faithful Inpainting for Object Completion Using a Single Reference Image**|我们提出了FaithFill，一种基于扩散的修复对象完成方法，用于真实生成丢失的对象部分。通常，需要多个参考图像来实现这种逼真的生成，否则生成将不能忠实地保持形状、纹理、颜色和背景。在这项工作中，我们提出了一种仅使用单个输入参考图像的管道，该图像具有不同的照明、背景、对象姿态和/或视点。奇异参考图像用于生成待修复对象的多个视图。我们证明了FaithFill可以从单个参考图像中忠实地生成对象的缺失部分，并保留背景/场景。这可以通过标准相似性度量、人类判断和GPT评估来证明。我们的结果是在DreamBooth数据集和一个新提出的数据集上给出的。 et.al.|[2406.07865](http://arxiv.org/abs/2406.07865)|null|
|**2024-06-11**|**M-LRM: Multi-view Large Reconstruction Model**|尽管大型重建模型（LRM）的最新进展显示了令人印象深刻的结果，但当将其输入从单个图像扩展到多个图像时，它表现出效率低下、几何和纹理质量较差以及收敛速度低于预期。其原因是，LRM将3D重建公式化为一个天真的图像到3D的翻译问题，忽略了输入图像之间的强3D相干性。在本文中，我们提出了一种多视图大型重建模型（M-LRM），该模型旨在以3D感知的方式从多视图有效地重建高质量的3D形状。具体来说，我们引入了一种多视图一致交叉关注方案，使M-LRM能够准确地从输入图像中查询信息。此外，我们使用输入多视图图像的3D先验来初始化三平面标记。与LRM相比，所提出的M-LRM可以产生分辨率为128美元乘以128美元的三平面NeRF，并生成高保真度的3D形状。实验研究表明，我们的模型比LRM实现了显著的性能增益和更快的训练收敛。项目页面：https://murphylmf.github.io/M-LRM/ et.al.|[2406.07648](http://arxiv.org/abs/2406.07648)|null|

<p align=right>(<a href=#updated-on-20240614>back to top</a>)</p>

## Diffusion

|Publish Date|Title|Abstract|PDF|Code|
|---|---|---|---|---|
|**2024-06-13**|**Rethinking Score Distillation as a Bridge Between Image Distributions**|分数蒸馏采样（SDS）已被证明是一种重要的工具，能够在数据贫乏的领域中使用大规模扩散先验。不幸的是，SDS有许多特性工件，限制了它在通用应用程序中的有用性。在本文中，我们通过将SDS及其变体视为求解从源分布到目标分布的最优成本运输路径，在理解SDS及其变体的行为方面取得了进展。在这种新的解释下，这些方法试图将损坏的图像（源）传输到自然图像分布（目标）。我们认为，当前方法的特征伪影是由（1）最优路径的线性近似和（2）源分布的较差估计引起的。我们表明，校准源分布的文本条件可以产生高质量的生成和翻译结果，而几乎没有额外的开销。我们的方法可以很容易地应用于许多领域，与专门方法的性能相匹配或优于专门方法。我们展示了它在文本到2D、基于文本的NeRF优化、将绘画转换为真实图像、视错觉生成和3D草图转换为真实中的实用性。我们将我们的方法与现有的分数蒸馏采样方法进行了比较，并表明它可以产生具有逼真颜色的高频细节。 et.al.|[2406.09417](http://arxiv.org/abs/2406.09417)|null|
|**2024-06-13**|**Alleviating Distortion in Image Generation via Multi-Resolution Diffusion Models**|本文通过集成一种新的多分辨率网络和含时层归一化，对扩散模型进行了创新性的增强。扩散模型因其在高保真图像生成中的有效性而备受关注。虽然传统的方法依赖于卷积U-Net架构，但最近基于Transformer的设计已经证明了卓越的性能和可扩展性。然而，由于与标记长度有关的自注意操作的二次性，对输入数据进行标记化（通过“补丁”）的Transformer架构面临着视觉保真度和计算复杂性之间的权衡。虽然较大的补丁大小可以提高注意力计算效率，但它们很难捕捉到细粒度的视觉细节，导致图像失真。为了应对这一挑战，我们建议使用多分辨率网络（DiMR）来增强扩散模型，这是一个跨多分辨率细化特征的框架，从低分辨率到高分辨率逐步增强细节。此外，我们还引入了时间相关层归一化（TD-LN），这是一种参数高效的方法，将时间相关参数纳入层归一化中，以注入时间信息并实现卓越的性能。我们的方法的有效性在类条件ImageNet生成基准上得到了证明，其中DiMR XL变体优于先前的扩散模型，在ImageNet 256 x 256上设置了1.70的最先进FID分数，在ImageNet 512 x 512上设置了2.89的最先进的FID分数。项目页面：https://qihao067.github.io/projects/DiMR et.al.|[2406.09416](http://arxiv.org/abs/2406.09416)|null|
|**2024-06-13**|**An Image is Worth More Than 16x16 Patches: Exploring Transformers on Individual Pixels**|这项工作没有引入新的方法。相反，我们提出了一个有趣的发现，质疑归纳偏见的必要性——现代计算机视觉架构中的局部性。具体地说，我们发现香草变形金刚可以通过直接将每个单独的像素作为令牌来操作，并获得高性能的结果。这与Vision Transformer中的流行设计有很大不同，后者保持了ConvNets对局部邻域的感应偏置（例如，将每个16x16补丁视为令牌）。我们主要展示了像素作为标记在计算机视觉中三个研究良好的任务中的有效性：用于对象分类的监督学习、通过掩蔽自动编码的自监督学习和使用扩散模型的图像生成。尽管直接对单个像素进行操作在计算上不太实用，但我们相信，在为计算机视觉设计下一代神经架构时，社区必须意识到这一令人惊讶的知识。 et.al.|[2406.09415](http://arxiv.org/abs/2406.09415)|null|
|**2024-06-13**|**Depth Anything V2**|这部作品呈现了深度任意V2。在不追求花哨技术的情况下，我们的目标是揭示关键发现，为建立强大的单目深度估计模型铺平道路。值得注意的是，与V1相比，该版本通过三个关键实践产生了更精细、更稳健的深度预测：1）用合成图像替换所有标记的真实图像，2）扩大我们的教师模型的容量，3）通过大规模伪标记真实图像的桥梁教授学生模型。与基于Stable Diffusion的最新模型相比，我们的模型明显更高效（速度快10倍以上），更准确。我们提供不同规模的模型（参数从2500万到130万不等），以支持广泛的场景。得益于它们强大的泛化能力，我们使用度量深度标签对它们进行微调，以获得我们的度量深度模型。除了我们的模型之外，考虑到当前测试集中有限的多样性和频繁的噪声，我们构建了一个具有精确注释和多样化场景的通用评估基准，以便于未来的研究。 et.al.|[2406.09414](http://arxiv.org/abs/2406.09414)|null|
|**2024-06-13**|**Interpreting the Weight Space of Customized Diffusion Models**|我们研究了大量自定义扩散模型所跨越的权重空间。我们通过创建一个由60000多个模型组成的数据集来填充这个空间，每个模型都是一个基础模型，经过微调，可以插入不同的人的视觉身份。我们将这些权重的基本流形建模为子空间，我们称之为权重2权重。我们展示了这个空间的三个直接应用——采样、编辑和反演。首先，由于空间中的每个点都对应于一个恒等式，因此从中采样一组权重会产生一个编码新恒等式的模型。接下来，我们在这个空间中找到与身份的语义编辑（例如，添加胡子）相对应的线性方向。这些编辑在生成的样本中保持外观不变。最后，我们展示了将单个图像反转到这个空间中可以重建真实的身份，即使输入图像不分布（例如，一幅画）。我们的结果表明，微调扩散模型的权重空间表现为一个可解释的身份潜在空间。 et.al.|[2406.09413](http://arxiv.org/abs/2406.09413)|null|
|**2024-06-13**|**ConsistDreamer: 3D-Consistent 2D Diffusion for High-Fidelity Scene Editing**|本文提出了ConsistenDreamer，这是一种新颖的框架，可以提升具有3D感知和3D一致性的2D扩散模型，从而实现高保真度的指令指导场景编辑。为了克服2D扩散模型中缺少3D一致性的基本限制，我们的关键见解是引入三种协同策略，增加2D扩散模型的输入，使其具有3D意识，并在训练过程中明确加强3D一致性。具体而言，我们将周围视图设计为2D扩散模型的上下文丰富的输入，并生成3D一致的结构化噪声，而不是与图像无关的噪声。此外，我们在每场景编辑过程中引入了自我监督的一致性强制训练。广泛的评估表明，我们的ConsistenDreamer在各种场景和编辑指令的指令引导场景编辑方面实现了最先进的性能，特别是在ScanNet++的复杂大型室内场景中，清晰度和细粒度显著提高。值得注意的是，ConsistenDreamer是第一部能够成功编辑复杂（如格子/方格）图案的作品。我们的项目页面位于永生co.github.io/ConsistenDreamer。 et.al.|[2406.09404](http://arxiv.org/abs/2406.09404)|null|
|**2024-06-13**|**Instruct 4D-to-4D: Editing 4D Scenes as Pseudo-3D Scenes Using 2D Diffusion**|本文提出了instruction 4D-to-4D，它实现了2D扩散模型的4D感知和时空一致性，以生成高质量的instruction引导的动态场景编辑结果。2D扩散模型在动态场景编辑中的传统应用经常导致不一致性，主要是由于其固有的逐帧编辑方法。针对将指令引导编辑扩展到4D的复杂性，我们的关键见解是将4D场景视为伪3D场景，解耦为两个子问题：在视频编辑中实现时间一致性，并将这些编辑应用于伪3D场景。接下来，我们首先使用锚感知注意力模块来增强Instruction-Pix2Pix（IP2P）模型，用于批量处理和一致编辑。此外，我们以滑动窗口的方式集成了光流引导的外观传播，以实现更精确的逐帧编辑，并结合了基于深度的投影来管理伪3D场景的大量数据，然后进行迭代编辑以实现收敛。我们在各种场景和编辑指令中广泛评估了我们的方法，并证明它实现了空间和时间一致的编辑结果，与现有技术相比，细节和清晰度显著增强。值得注意的是，Directive 4D-to-4D是通用的，适用于单目和具有挑战性的多相机场景。代码和更多结果可在永生co.github.io/Instruction-4D-to-4D上获得。 et.al.|[2406.09402](http://arxiv.org/abs/2406.09402)|null|
|**2024-06-13**|**OmniTokenizer: A Joint Image-Video Tokenizer for Visual Generation**|Tokenizer作为一个翻译器，将复杂的视觉数据映射到一个紧凑的潜在空间中，是视觉生成模型的核心。基于现有的标记器是针对图像或视频输入量身定制的这一发现，本文提出了OmniTokenizer，一种用于图像和视频联合标记化的基于转换器的标记器。OmniTokenizer采用时空解耦架构设计，集成了窗口和因果注意力进行时空建模。为了利用图像和视频数据的互补性，我们进一步提出了一种渐进式训练策略，其中OmniTokenizer首先在固定分辨率的图像数据上进行训练，以开发空间编码能力，然后在多分辨率的图像和视频数据上进行联合训练，以学习时间动态。OmniTokenizer首次在统一的框架内处理图像和视频输入，并证明了实现其协同作用的可能性。大量实验表明，OmniTokenize在各种图像和视频数据集上实现了最先进的（SOTA）重建性能，例如，ImageNet上的1.11重建FID和UCF-101上的42重建FVD，分别比以前的SOTA方法高出13%和26%。此外，我们还表明，当与OmniTokenizer集成时，基于语言的方法和扩散模型都可以实现高级的视觉合成性能，这突出了我们方法的优越性和多功能性。代码位于https://github.com/FoundationVision/OmniTokenizer. et.al.|[2406.09399](http://arxiv.org/abs/2406.09399)|null|
|**2024-06-13**|**WonderWorld: Interactive 3D Scene Generation from a Single Image**|我们介绍了WonderWorld，这是一种新颖的3D场景外推框架，使用户能够基于单个输入图像和用户指定的文本来探索和塑造虚拟环境。虽然场景生成的视觉质量已经得到了显著改善，但现有方法是离线运行的，生成场景需要数十分钟到数小时。通过利用快速高斯曲面和基于引导扩散的深度估计方法，WonderWorld生成几何一致的外推，同时显著减少计算时间。我们的框架在一个A6000 GPU上用不到10秒的时间生成连接和多样化的3D场景，实现实时用户交互和探索。我们展示了WonderWorld在虚拟现实、游戏和创意设计中的应用潜力，用户可以从一张图像中快速生成和导航沉浸式的、潜在的无限虚拟世界。我们的方法代表了交互式3D场景生成的重大进步，为虚拟环境中用户驱动的内容创建和探索开辟了新的可能性。我们将发布完整的代码和软件以实现再现性。项目网站：https://WonderWorld-2024.github.io/ et.al.|[2406.09394](http://arxiv.org/abs/2406.09394)|null|
|**2024-06-13**|**Sagiri: Low Dynamic Range Image Enhancement with Generative Diffusion Prior**|使用8位相机拍摄高动态范围（HDR）场景通常会出现曝光过度/曝光不足、由于低位深度压缩而丢失精细细节、颜色分布偏斜以及黑暗区域中的强噪声等问题。传统的LDR图像增强方法主要集中在颜色映射上，通过扩展图像的颜色范围和调整亮度来增强视觉表现。然而，这些方法无法有效地恢复动态范围极值中的内容，动态范围极值是像素值接近0或255的区域。为了解决HDR成像的全部挑战并超越当前模型的局限性，我们提出了一种新的两阶段方法。第一阶段在保持现有细节的同时将颜色和亮度映射到适当的范围，第二阶段在生成捕捉过程中丢失的动态范围极值中的内容之前利用扩散。该生成细化模块也可以用作即插即用模块来增强和补充现有的LDR增强模型。所提出的方法显著提高了LDR图像的质量和细节，通过严格的实验验证证明了其优越的性能。项目页面位于https://sagiri0208.github.io et.al.|[2406.09389](http://arxiv.org/abs/2406.09389)|null|

<p align=right>(<a href=#updated-on-20240614>back to top</a>)</p>

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

<p align=right>(<a href=#updated-on-20240614>back to top</a>)</p>

[contributors-shield]: https://img.shields.io/github/contributors/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[contributors-url]: https://github.com/Vincentqyw/cv-arxiv-daily/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[forks-url]: https://github.com/Vincentqyw/cv-arxiv-daily/network/members
[stars-shield]: https://img.shields.io/github/stars/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[stars-url]: https://github.com/Vincentqyw/cv-arxiv-daily/stargazers
[issues-shield]: https://img.shields.io/github/issues/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[issues-url]: https://github.com/Vincentqyw/cv-arxiv-daily/issues

