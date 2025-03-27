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
|**2025-03-25**|**PartRM: Modeling Part-Level Dynamics with Large Cross-State Reconstruction Model**|随着人们对根据当前观测和行动预测未来状态的世界模型的兴趣日益浓厚，准确建模零件级动态对于各种应用来说变得越来越重要。现有的方法，如Puppet Master，依赖于对大规模预训练的视频扩散模型进行微调，由于2D视频表示的局限性和缓慢的处理时间，这些模型在现实世界中是不切实际的。为了克服这些挑战，我们提出了PartRM，这是一种新颖的4D重建框架，可以从静态对象的多视图图像中同时对外观、几何形状和零件级运动进行建模。PartRM基于大型3D高斯重建模型，利用其对静态对象外观和几何的广泛知识。为了解决4D中的数据稀缺问题，我们引入了PartDrag-4D数据集，提供了20000多个州的零件级动态的多视图观测。我们通过多尺度阻力嵌入模块增强了模型对相互作用条件的理解，该模块捕获了不同粒度下的动力学。为了防止在微调过程中发生灾难性遗忘，我们实施了一个两阶段的训练过程，该过程依次侧重于运动和外观学习。实验结果表明，PartRM建立了零件级运动学习的最新技术，可以应用于机器人的操纵任务。我们的代码、数据和模型是公开的，以促进未来的研究。 et.al.|[2503.19913](http://arxiv.org/abs/2503.19913)|null|
|**2025-03-25**|**FullDiT: Multi-Task Video Generative Foundation Model with Full Attention**|当前的视频生成基础模型主要关注文本到视频的任务，为细粒度视频内容创建提供了有限的控制。尽管基于适配器的方法（例如ControlNet）能够以最小的微调实现额外的控制，但在集成多种条件时会遇到挑战，包括：独立训练的适配器之间的分支冲突、导致计算成本增加的参数冗余，以及与完全微调相比性能欠佳。为了应对这些挑战，我们引入了FullDiT，这是一种用于视频生成的统一基础模型，通过统一的全注意力机制无缝集成了多种条件。通过将多任务条件融合到统一的序列表示中，并利用完全自我关注的长上下文学习能力来捕获条件动态，FullDiT减少了参数开销，避免了条件冲突，并显示了可扩展性和涌现能力。我们进一步介绍了用于多任务视频生成评估的FullBench。实验证明，FullDiT取得了最先进的结果，突出了全注意力在复杂多任务视频生成中的功效。 et.al.|[2503.19907](http://arxiv.org/abs/2503.19907)|null|
|**2025-03-25**|**Mask $^2$DiT: Dual Mask-based Diffusion Transformer for Multi-Scene Long Video Generation**|Sora揭示了扩散变换器（DiT）架构在单场景视频生成中的巨大潜力。然而，提供更广泛应用的多场景视频生成这一更具挑战性的任务仍然相对缺乏探索。为了弥合这一差距，我们提出了Mask$^2$DiT，这是一种新颖的方法，可以在视频片段与其相应的文本注释之间建立细粒度的一对一对齐。具体来说，我们在DiT架构中的每个注意力层引入了一个对称的二进制掩码，确保每个文本注释仅适用于其各自的视频片段，同时保持视觉标记之间的时间连贯性。这种注意力机制实现了精确的分段级文本与视觉对齐，使DiT架构能够有效地处理具有固定数量场景的视频生成任务。为了进一步使DiT架构具备基于现有场景生成额外场景的能力，我们引入了一个分段级条件掩码，该掩码将每个新生成的分段与前面的视频分段相结合，从而实现了自回归场景扩展。定性和定量实验都证实，Mask$^2$ DiT在保持分段之间的视觉一致性方面表现出色，同时确保每个分段与其相应的文本描述之间的语义对齐。我们的项目页面是https://tianhao-qi.github.io/Mask2DiTProject. et.al.|[2503.19881](http://arxiv.org/abs/2503.19881)|null|
|**2025-03-25**|**AudCast: Audio-Driven Human Video Generation by Cascaded Diffusion Transformers**|尽管音频驱动视频生成最近取得了进展，但现有的方法大多侧重于驱动面部运动，导致头部和身体动态不连贯。展望未来，在给定音频的情况下，生成具有精确唇同步和微妙的同音手势的整体人类视频是可取的，但也是具有挑战性的。在这项工作中，我们提出了AudCast，这是一种采用级联扩散变换器（DiTs）范式的广义音频驱动的人类视频生成框架，它基于参考图像和给定的音频合成整体人类视频。1） 首先，提出了一种音频调节的整体人体DiT架构，以生动的手势动力学直接驱动任何人体的运动。2） 然后，为了增强众所周知难以处理的手部和面部细节，区域细化DiT利用区域3D拟合作为桥梁来改造信号，从而产生最终结果。大量实验表明，我们的框架能够生成具有时间连贯性和精细面部和手部细节的高保真音频驱动的整体人类视频。资源可以在以下网址找到https://guanjz20.github.io/projects/AudCast. et.al.|[2503.19824](http://arxiv.org/abs/2503.19824)|null|
|**2025-03-25**|**AccVideo: Accelerating Video Diffusion Model with Synthetic Dataset**|扩散模型在视频生成领域取得了显著进展。然而，它们的迭代去噪特性需要大量的推理步骤来生成视频，这很慢，计算成本很高。本文首先详细分析了现有扩散蒸馏方法中存在的挑战，并提出了一种新的有效方法，即AccVideo，以减少使用合成数据集加速视频扩散模型的推理步骤。我们利用预训练的视频扩散模型生成多个有效的去噪轨迹作为我们的合成数据集，这消除了在蒸馏过程中使用无用的数据点。基于合成数据集，我们设计了一种基于轨迹的少步制导，该制导利用去噪轨迹中的关键数据点来学习噪声到视频的映射，从而能够以更少的步骤生成视频。此外，由于合成数据集捕获了每个扩散时间步的数据分布，我们引入了一种对抗性训练策略，使学生模型的输出分布与我们的合成数据集的输出分布对齐，从而提高了视频质量。大量实验表明，与教师模型相比，我们的模型在生成速度上提高了8.5倍，同时保持了相当的性能。与之前的加速方法相比，我们的方法能够生成更高质量和分辨率的视频，即5秒、720x1280、24fps。 et.al.|[2503.19462](http://arxiv.org/abs/2503.19462)|null|
|**2025-03-26**|**Inference-Time Scaling for Flow Models via Stochastic Generation and Rollover Budget Forcing**|我们提出了一种用于预训练流模型的推理时间缩放方法。最近，推理时间缩放在LLM和扩散模型中引起了极大的关注，通过利用额外的计算来提高样本质量或更好地将输出与用户偏好对齐。对于扩散模型，由于中间去噪步骤的随机性，粒子采样允许更有效的缩放。相反，虽然流模型作为扩散模型的替代品越来越受欢迎，在最先进的图像和视频生成模型中提供了更快的生成和高质量的输出，但由于其确定性的生成过程，用于扩散模型的高效推理时间标度方法不能直接应用。为了实现流模型的有效推理时间缩放，我们提出了三个关键思想：1）基于SDE的生成，在流模型中实现粒子采样，2）插值转换，扩大搜索空间并增强样本多样性，3）滚动预算强制（RBF），这是一种跨时间步自适应分配计算资源以最大限度地提高预算利用率的方法。我们的实验表明，基于SDE的生成，特别是基于方差保持（VP）插值的生成，提高了粒子采样方法在流模型中推理时间缩放的性能。此外，我们证明了具有VP-SDE的RBF实现了最佳性能，优于所有先前的推理时间缩放方法。 et.al.|[2503.19385](http://arxiv.org/abs/2503.19385)|null|
|**2025-03-25**|**MVPortrait: Text-Guided Motion and Emotion Control for Multi-view Vivid Portrait Animation**|最近的肖像动画方法在生成逼真的嘴唇同步方面取得了重大进展。然而，他们往往缺乏对头部运动和面部表情的明确控制，无法从多个视角制作视频，导致动画的可控性和表现力较低。此外，尽管文本引导的肖像动画具有用户友好的特性，但它仍然没有得到充分的探索。我们提出了一种新颖的两阶段文本引导框架MVPortrait（多视图生动肖像），用于生成富有表现力的多视图肖像动画，忠实地捕捉所描述的运动和情感。MVPortrait是第一个引入FLAME作为中间表示的软件，它有效地将面部动作、表情和视图变换嵌入到其参数空间中。在第一阶段，我们分别训练基于文本输入的火焰运动和情感扩散模型。在第二阶段，我们训练了一个多视图视频生成模型，该模型以第一阶段的参考肖像图像和多视图FLAME渲染序列为条件。实验结果表明，MVPortrait在运动和情感控制以及视图一致性方面优于现有方法。此外，通过利用FLAME作为桥梁，MVPortrait成为第一个与文本、语音和视频作为驱动信号兼容的可控肖像动画框架。 et.al.|[2503.19383](http://arxiv.org/abs/2503.19383)|null|
|**2025-03-26**|**EfficientMT: Efficient Temporal Adaptation for Motion Transfer in Text-to-Video Diffusion Models**|生成模型的进步导致了文本到视频（T2V）生成的重大进展，但生成视频的运动可控性仍然有限。现有的运动传递方法探索了参考视频的运动表示来指导生成。然而，这些方法通常依赖于特定于样本的优化策略，导致计算负担很高。本文提出了一种新颖高效的视频运动传输端到端框架EfficientMT。通过利用一小部分合成的成对运动传递样本，EfficientMT有效地将预训练的T2V模型适应到一个通用的运动传递框架中，该框架可以准确地捕捉和再现各种运动模式。具体来说，我们重新调整了T2V模型的主干，从参考视频中提取时间信息，并进一步提出了一个缩放器模块来提取运动相关信息。随后，我们引入了一种时间整合机制，该机制将参考运动特征无缝地整合到视频生成过程中。在对我们自行收集的合成配对样本进行训练后，EfficientMT能够实现一般的视频运动传输，而不需要优化测试时间。大量实验表明，我们的EfficientMT在效率方面优于现有方法，同时保持了灵活的运动可控性。我们的代码将可用https://github.com/PrototypeNx/EfficientMT. et.al.|[2503.19369](http://arxiv.org/abs/2503.19369)|null|
|**2025-03-25**|**Long-Context Autoregressive Video Modeling with Next-Frame Prediction**|长上下文自回归建模显著提高了语言生成，但视频生成仍然难以充分利用扩展的时间上下文。为了研究长上下文视频建模，我们引入了帧自回归（FAR），这是视频自回归建模的一个强基线。正如语言模型学习令牌之间的因果依赖关系（即令牌AR）一样，FAR对连续帧之间的时间因果依赖关系进行建模，实现了比令牌AR和视频扩散变换器更好的收敛。基于FAR，我们观察到长上下文视觉建模由于视觉冗余而面临挑战。现有的RoPE缺乏对远程上下文的有效时间衰减，并且无法很好地推断出长视频序列。此外，长视频的训练在计算上很昂贵，因为视觉标记的增长速度比语言标记快得多。为了解决这些问题，我们建议平衡局部性和长期依赖性。我们介绍了FlexRoPE，这是一种测试时间技术，为RoPE添加了灵活的时间衰减，使外推到16倍长的视觉环境。此外，我们提出了长短期上下文建模，其中高分辨率的短期上下文窗口确保了细粒度的时间一致性，而无限的长期上下文窗口使用较少的令牌对长程信息进行编码。通过这种方法，我们可以在具有可管理令牌上下文长度的长视频序列上进行训练。我们证明，FAR在短视频和长视频生成方面都达到了最先进的性能，为视频自回归建模提供了一个简单而有效的基线。 et.al.|[2503.19325](http://arxiv.org/abs/2503.19325)|null|
|**2025-03-24**|**Target-Aware Video Diffusion Models**|我们提出了一种目标感知视频扩散模型，该模型根据输入图像生成视频，其中演员在执行所需动作的同时与指定目标进行交互。目标由分割掩码定义，所需动作通过文本提示描述。与现有的可控图像到视频扩散模型不同，这些模型通常依赖于密集的结构或运动线索来引导演员向目标移动，我们的目标感知模型只需要一个简单的掩码来指示目标，利用预训练模型的泛化能力来产生合理的动作。这使得我们的方法在人机交互（HOI）场景中特别有效，在这种场景中，提供精确的动作指导是具有挑战性的，并且还可以在机器人等应用中使用视频扩散模型进行高级动作规划。我们通过扩展基线模型来构建目标感知模型，以将目标掩码作为额外的输入。为了增强目标意识，我们引入了一个特殊的令牌，在文本提示中对目标的空间信息进行编码。然后，我们使用一种新的交叉注意力损失方法，用我们精心策划的数据集对模型进行微调，该方法将与此令牌相关的交叉注意力图与输入目标掩码对齐。为了进一步提高性能，我们有选择地将这种损失应用于语义上最相关的变换器块和注意力区域。实验结果表明，我们的目标感知模型在生成演员与指定目标准确交互的视频方面优于现有的解决方案。我们进一步证明了它在两个下游应用中的功效：视频内容创建和零样本3D HOI运动合成。 et.al.|[2503.18950](http://arxiv.org/abs/2503.18950)|null|

<p align=right>(<a href=#updated-on-20250327>back to top</a>)</p>

## 3D

|Publish Date|Title|Abstract|PDF|Code|
|---|---|---|---|---|
|**2025-03-25**|**Exploring Disentangled and Controllable Human Image Synthesis: From End-to-End to Stage-by-Stage**|在人类图像合成中实现精细可控性是计算机视觉领域的一个长期挑战。现有的方法主要集中在面部合成或近额体生成上，以一种解耦的方式同时控制视点、姿势、服装和身份等关键因素的能力有限。本文介绍了一种新的解纠缠和可控的人工合成任务，该任务在统一的框架内明确地分离和操纵这四个因素。我们首先开发了一个在MVHumanNet上训练的端到端生成模型，用于因素解纠缠。然而，MVHumanNet和野外数据之间的领域差距产生了不令人满意的尝试结果，促使人们探索虚拟试穿（VTON）数据集作为一种潜在的解决方案。通过实验，我们观察到，简单地将VTON数据集作为额外数据来训练端到端模型会降低性能，这主要是由于两个数据集之间的数据形式不一致，从而破坏了解纠缠过程。为了更好地利用这两个数据集，我们提出了一个分阶段的框架，将人体图像生成分解为三个连续的步骤：穿衣a姿势生成、后视图合成以及姿势和视图控制。这种结构化的管道可以在不同阶段更好地利用数据集，显著提高可控性和泛化能力，特别是在野外场景中。大量实验表明，我们的分阶段方法在视觉保真度和解纠缠质量方面都优于端到端模型，为现实世界的任务提供了可扩展的解决方案。项目页面上提供了其他演示：https://taited.github.io/discohuman-project/. et.al.|[2503.19486](http://arxiv.org/abs/2503.19486)|null|
|**2025-03-25**|**HoGS: Unified Near and Far Object Reconstruction via Homogeneous Gaussian Splatting**|新型视图合成最近取得了令人瞩目的进展，3D高斯散点（3DGS）提供了高效的训练时间和逼真的实时渲染。然而，对笛卡尔坐标的依赖限制了3DGS在远处物体上的性能，这对于重建无界的室外环境非常重要。我们发现，尽管3DGS管道非常简单，但使用齐次坐标（投影几何中的一个概念）显著提高了远处物体的渲染精度。因此，我们提出了将齐次坐标合并到3DGS框架中的齐次高斯散斑（HoGS），为增强远近物体提供了统一的表示。HoGS通过采用射影几何原理，有效地管理了广阔的空间位置和尺度，特别是在室外无界环境中。实验表明，HoGS显著提高了重建远处物体的准确性，同时保持了附近物体的高质量渲染，以及快速的训练速度和实时渲染能力。我们的实现可以在我们的项目页面上找到https://kh129.github.io/hogs/. et.al.|[2503.19232](http://arxiv.org/abs/2503.19232)|**[link](https://github.com/huntorochi/HoGS)**|
|**2025-03-24**|**RomanTex: Decoupling 3D-aware Rotary Positional Embedded Multi-Attention Network for Texture Synthesis**|为现有几何体绘制纹理是3D资产生成中一个关键但劳动密集型的过程。文本到图像（T2I）模型的最新进展导致了纹理生成的重大进展。大多数现有的研究通过首先使用图像扩散模型在2D空间中生成图像，然后进行纹理烘焙过程来实现UV纹理，从而完成这项任务。然而，由于生成的多视图图像之间的不一致性，这些方法往往难以产生高质量的纹理，从而导致接缝和重影伪影。相比之下，基于3D的纹理合成方法旨在解决这些不一致性，但它们往往忽略了2D扩散模型先验，使其难以应用于现实世界的对象。为了克服这些局限性，我们提出了RomanTex，这是一种基于多视图的纹理生成框架，通过我们新颖的3D感知旋转位置嵌入，将多注意力网络与底层3D表示相结合。此外，我们在多注意力块中加入了解耦特性，以增强模型在图像到纹理任务中的鲁棒性，从而实现语义正确的后视图合成。此外，我们引入了一种与几何相关的无分类器引导（CFG）机制，以进一步改善与几何和图像的对齐。定量和定性评估以及全面的用户研究表明，我们的方法在纹理质量和一致性方面取得了最先进的结果。 et.al.|[2503.19011](http://arxiv.org/abs/2503.19011)|null|
|**2025-03-24**|**NexusGS: Sparse View Synthesis with Epipolar Depth Priors in 3D Gaussian Splatting**|神经辐射场（NeRF）和3D高斯散斑（3DGS）使用来自密集间隔的相机视点的图像，显著提高了照片真实感的新颖视图合成。然而，由于监督有限，这些方法在少数拍摄场景中很难使用。在本文中，我们提出了NexusGS，这是一种基于3DGS的方法，通过将深度信息直接嵌入点云中，而不依赖于复杂的手动正则化，增强了稀疏视图图像的新颖视图合成。利用3DGS固有的极线几何，我们的方法引入了一种新的点云加密策略，该策略用密集的点云初始化3DGS，减少了点放置的随机性，同时防止了过平滑和过拟合。具体来说，NexusGS包括三个关键步骤：极性深度连接、流动弹性深度混合和流动过滤深度修剪。这些步骤利用光流和相机姿态来计算精确的深度图，同时减轻了通常与光流相关的不准确之处。通过整合极线深度先验，NexusGS确保了可靠的密集点云覆盖，并在稀疏视图条件下支持稳定的3DGS训练。实验表明，NexusGS显著提高了深度精度和渲染质量，远远超过了最先进的方法。此外，我们通过大幅提高竞争方法的性能来验证我们生成的点云的优越性。项目页面：https://usmizuki.github.io/NexusGS/. et.al.|[2503.18794](http://arxiv.org/abs/2503.18794)|null|
|**2025-03-24**|**Accenture-NVS1: A Novel View Synthesis Dataset**|本文介绍了ACC-NVS1，这是一个专门为机载和地面图像的新型视图合成研究而设计的专用数据集。ACC-NVS1的数据分别于2023年和2024年在德克萨斯州奥斯汀和宾夕法尼亚州匹兹堡收集。该系列包括从机载和地面摄像机拍摄的六个不同的现实世界场景，总共有148000张图像。ACC-NVS1解决了不同高度和瞬态物体等挑战。该数据集旨在补充现有数据集，为综合研究提供额外资源，而不是作为基准。 et.al.|[2503.18711](http://arxiv.org/abs/2503.18711)|null|
|**2025-03-24**|**Hardware-Rasterized Ray-Based Gaussian Splatting**|我们提出了一种用于基于光线的3D高斯散斑（RayGS）的新颖硬件光栅化渲染方法，为新颖的视图合成获得了快速和高质量的结果。我们的工作包含一个数学严谨和几何直观的推导，关于如何有效地估计渲染RayGS模型的所有相关量，这些模型是相对于标准硬件光栅化着色器构建的。我们的解决方案是第一个能够以足够高的帧率渲染RayGS模型，以支持虚拟现实和混合现实等对质量敏感的应用程序。我们的第二个贡献是通过解决在训练和测试期间渲染不同尺度时出现的MIP相关问题，实现了RayGS的无别名渲染。我们在不同的基准场景中展示了显著的性能提升，同时保留了RayGS最先进的外观质量。 et.al.|[2503.18682](http://arxiv.org/abs/2503.18682)|null|
|**2025-03-25**|**LookCloser: Frequency-aware Radiance Field for Tiny-Detail Scene**|人类通过跨越多个频率的信息来感知和理解周围的环境。在沉浸式场景中，人们自然地扫描他们的环境以掌握其整体结构，同时检查吸引他们注意力的物体的细节。然而，目前的NeRF框架主要侧重于对高频局部视图或具有低频信息的场景的广泛结构进行建模，这仅限于平衡两者。我们介绍了FA NeRF，这是一种用于视图合成的新型频率感知框架，可在单个NeRF模型中同时捕获整体场景结构和高清细节。为了实现这一目标，我们提出了一种3D频率量化方法，该方法分析场景的频率分布，实现频率感知渲染。我们的框架包含一个用于快速收敛和查询的频率网格，一个用于平衡不同频率内容特征的频率感知特征重新加权策略。大量实验表明，我们的方法在保留细节的同时，在建模整个场景方面明显优于现有方法。项目页面：https://coscatter.github.io/LookCloser/ et.al.|[2503.18513](http://arxiv.org/abs/2503.18513)|null|
|**2025-03-25**|**StableGS: A Floater-Free Framework for 3D Gaussian Splatting**|近年来，3D高斯散点（3DGS）在新颖的视图合成中取得了显著的成功，在质量和效率上都超越了先前的可微渲染方法。然而，其训练过程受到耦合不透明度颜色优化的影响，该优化经常收敛到局部最小值，产生降低视觉保真度的漂浮伪影。我们提出了StableGS，这是一个通过交叉视图深度一致性约束消除浮动的框架，同时引入了双重不透明度GS模型来解耦半透明对象的几何和材料属性。为了进一步提高弱纹理区域的重建质量，我们集成了DUSt3R深度估计，显著提高了几何稳定性。我们的方法从根本上解决了3DGS训练的不稳定性，在开源数据集上优于现有的最先进方法。 et.al.|[2503.18458](http://arxiv.org/abs/2503.18458)|null|
|**2025-03-24**|**MonoInstance: Enhancing Monocular Priors via Multi-view Instance Alignment for Neural Rendering and Reconstruction**|单眼深度先验已被神经渲染广泛应用于基于多视图的任务，如3D重建和新颖的视图合成。然而，由于对每个视图的预测不一致，如何在多视图环境中更有效地利用单眼线索仍然是一个挑战。当前的方法不加选择地对待整个估计的深度图，并将其用作地面实况监督，而忽略了单目先验中固有的不准确性和交叉视图不一致性。为了解决这些问题，我们提出了MonoInstance，这是一种探索单眼深度不确定性的通用方法，为神经渲染和重建提供增强的几何先验。我们的关键见解在于将来自多个视图的每个分段实例深度对齐到一个共同的3D空间中，从而将单目深度的不确定性估计转化为噪声点云中的密度度量。对于深度先验不可靠的高不确定性区域，我们进一步引入了一个约束项，鼓励投影实例与附近视图上的相应实例掩码对齐。MonoInstance是一种多功能策略，可以无缝集成到各种多视图神经渲染框架中。我们的实验结果表明，MonoInstance在各种基准下显著提高了重建和新视图合成的性能。 et.al.|[2503.18363](http://arxiv.org/abs/2503.18363)|null|
|**2025-03-22**|**DVG-Diffusion: Dual-View Guided Diffusion Model for CT Reconstruction from X-Rays**|使用端到端深度学习网络从少视图2D X射线直接重建3D CT体积是一项具有挑战性的任务，因为X射线图像只是3D CT体积的投影视图。在这项工作中，我们通过结合新的视图合成来促进复杂的2D X射线图像到3D CT的映射，并通过视图引导的特征对齐来降低学习难度。具体而言，我们提出了一种双视图引导扩散模型（DVG扩散），该模型将真实输入的X射线视图和合成的新X射线视图耦合起来，共同引导CT重建。首先，一种新型的视图参数引导编码器从与CT空间对齐的X射线中捕获特征。接下来，我们将提取的双视图特征连接起来，作为潜在扩散模型学习和改进CT潜在表示的条件。最后，将CT潜在表示解码为像素空间中的CT体积。通过结合视图参数引导编码和双视图引导CT重建，我们的DVG扩散可以在CT重建的高保真度和感知质量之间实现有效的平衡。实验结果表明，我们的方法优于最先进的方法。在实验的基础上，对视图和重建进行了综合分析和讨论。 et.al.|[2503.17804](http://arxiv.org/abs/2503.17804)|null|

<p align=right>(<a href=#updated-on-20250327>back to top</a>)</p>

## 3D Reconstruction

|Publish Date|Title|Abstract|PDF|Code|
|---|---|---|---|---|
|**2025-03-26**|**A Survey on Event-driven 3D Reconstruction: Development under Different Categories**|事件相机因其高时间分辨率、低延迟和高动态范围而越来越受到人们对3D重建的关注。它们异步捕获每像素的亮度变化，允许在快速运动和具有挑战性的照明条件下进行精确重建。在这项调查中，我们全面回顾了事件驱动的3D重建方法，包括立体、单眼和多模态系统。我们根据几何、基于学习和混合方法对最近的发展进行了进一步分类。还涵盖了新兴趋势，如神经辐射场和事件数据的3D高斯飞溅。相关作品按时间顺序排列，以说明该领域的创新和进步。为了支持未来的研究，我们还强调了数据集、实验、评估、事件表示等方面的关键研究差距和未来的研究方向。 et.al.|[2503.19753](http://arxiv.org/abs/2503.19753)|null|
|**2025-03-25**|**Wavelet-based Global-Local Interaction Network with Cross-Attention for Multi-View Diabetic Retinopathy Detection**|多视图糖尿病视网膜病变（DR）检测最近成为一种有前景的方法，可以解决单视图DR面临的不完全病变问题。然而，由于病变的大小和位置各不相同，它仍然具有挑战性。此外，现有的多视图DR方法通常会合并多个视图，而不考虑它们之间病变信息的相关性和冗余性。因此，我们提出了一种新方法来克服病变信息学习困难和多视图融合不足的挑战。具体来说，我们引入了一个双分支网络来获得局部病变特征及其全局相关性。小波变换的高频分量用于利用病变边缘信息，然后通过全局语义对其进行增强，以促进困难的病变学习。此外，我们提出了一种跨视图融合模块，以改进多视图融合并减少冗余。在大型公共数据集上的实验结果证明了我们方法的有效性。该代码是开源的https://github.com/HuYongting/WGLIN. et.al.|[2503.19329](http://arxiv.org/abs/2503.19329)|null|
|**2025-03-24**|**MonoInstance: Enhancing Monocular Priors via Multi-view Instance Alignment for Neural Rendering and Reconstruction**|单眼深度先验已被神经渲染广泛应用于基于多视图的任务，如3D重建和新颖的视图合成。然而，由于对每个视图的预测不一致，如何在多视图环境中更有效地利用单眼线索仍然是一个挑战。当前的方法不加选择地对待整个估计的深度图，并将其用作地面实况监督，而忽略了单目先验中固有的不准确性和交叉视图不一致性。为了解决这些问题，我们提出了MonoInstance，这是一种探索单眼深度不确定性的通用方法，为神经渲染和重建提供增强的几何先验。我们的关键见解在于将来自多个视图的每个分段实例深度对齐到一个共同的3D空间中，从而将单目深度的不确定性估计转化为噪声点云中的密度度量。对于深度先验不可靠的高不确定性区域，我们进一步引入了一个约束项，鼓励投影实例与附近视图上的相应实例掩码对齐。MonoInstance是一种多功能策略，可以无缝集成到各种多视图神经渲染框架中。我们的实验结果表明，MonoInstance在各种基准下显著提高了重建和新视图合成的性能。 et.al.|[2503.18363](http://arxiv.org/abs/2503.18363)|null|
|**2025-03-24**|**Surface-Aware Distilled 3D Semantic Features**|许多3D任务，如姿势对齐、动画、运动转移和3D重建，都依赖于建立3D形状之间的对应关系。最近，通过匹配预训练视觉模型的语义特征来应对这一挑战。然而，尽管这些特征很强大，但它们很难区分同一语义类的实例，例如“左手”和“右手”，这会导致大量的映射错误。为了解决这个问题，我们学习了一个对这些模糊性具有鲁棒性的表面感知嵌入空间。重要的是，我们的方法是自我监督的，只需要少量不成对的训练网格就可以在测试时推断出新的3D形状的特征。我们通过引入对比损失来实现这一点，该损失保留了从基础模型中提取的特征的语义内容，同时消除了形状表面相距甚远的特征的歧义。我们在对应匹配基准测试中观察到卓越的性能，并支持下游应用，包括零件分割、姿态对齐和运动转移。项目现场可在https://lukas.uzolas.com/SurfaceAware3DFeaturesSite. et.al.|[2503.18254](http://arxiv.org/abs/2503.18254)|null|
|**2025-03-23**|**MLLM-For3D: Adapting Multimodal Large Language Model for 3D Reasoning Segmentation**|推理分割旨在基于人类意图和空间推理对复杂场景中的目标对象进行分割。虽然最近的多模态大型语言模型（MLLM）已经证明了令人印象深刻的2D图像推理分割，但将这些功能应用于3D场景的探索仍然不足。在本文中，我们介绍了MLLM-For3D，这是一个简单而有效的框架，可以将知识从2D MLLMs转移到3D场景理解。具体来说，我们利用MLLM生成多视图伪分割掩模和相应的文本嵌入，然后将2D掩模投影到3D空间中，并将其与文本嵌入对齐。主要的挑战在于缺乏跨多个视图的3D上下文和空间一致性，导致模型产生幻觉，使不存在的对象无法一致地定位对象。用这种不相关的对象训练3D模型会导致性能下降。为了解决这个问题，我们引入了一种空间一致性策略，以强制分割掩模在3D空间中保持一致，有效地捕捉场景的几何形状。此外，我们开发了一种用于多模态语义对齐的查询令牌方法，实现了跨不同视图对同一对象的一致识别。对各种具有挑战性的室内场景基准的广泛评估表明，即使没有任何标记的3D训练数据，MLLM-For3D也优于现有的3D推理分割方法，有效地解释了用户意图，理解了3D场景，并对空间关系进行了推理。 et.al.|[2503.18135](http://arxiv.org/abs/2503.18135)|null|
|**2025-03-22**|**GaussianFocus: Constrained Attention Focus for 3D Gaussian Splatting**|3D重建和神经渲染的最新发展极大地推动了各种学术和工业领域中照片级逼真3D场景渲染的能力。3D高斯散点技术及其衍生技术集成了基于基元和体积表示的优点，以提供顶级渲染质量和效率。尽管取得了这些进步，但该方法往往会产生过度冗余的噪声高斯分布，过度适应每个训练视图，从而降低渲染质量。此外，虽然3D高斯散斑在小规模和以对象为中心的场景中表现出色，但它在更大场景中的应用受到视频内存有限、优化持续时间过长和视图外观可变等限制的阻碍。为了应对这些挑战，我们引入了GaussianFocus，这是一种创新的方法，它结合了补丁注意力算法来提高渲染质量，并实现了高斯约束策略来最小化冗余。此外，我们提出了一种针对大规模场景的细分重建策略，将它们划分为更小、可管理的块进行单独训练。我们的结果表明，GaussianFocus显著减少了不必要的高斯分布，提高了渲染质量，超越了现有的最新技术（SoTA）方法。此外，我们展示了我们的方法能够有效地管理和渲染大型场景，如城市环境，同时保持视觉输出的高保真度。 et.al.|[2503.17798](http://arxiv.org/abs/2503.17798)|null|
|**2025-03-22**|**3D Modeling: Camera Movement Estimation and path Correction for SFM Model using the Combination of Modified A-SIFT and Stereo System**|创建准确高效的3D模型带来了重大挑战，特别是在解决大视点变化、计算复杂性和对齐差异方面。高效的相机路径生成可以帮助解决这些问题。在此背景下，提出了一种仿射尺度不变特征变换（ASIFT）的改进版本，以减少计算开销的方式提取更多的匹配点，确保有足够数量的内层用于精确的相机旋转角度估计。此外，引入了一种新的基于双相机的旋转校正模型，以减轻小的旋转误差，进一步提高精度。此外，通过改变运动结构（SFM）模型，实现了基于立体相机的平移估计和校正模型，以确定3D空间中的相机运动。最后，ASIFT和基于两个相机的SFM模型的新颖组合提供了3D空间中精确的相机运动轨迹。实验结果表明，与实际相机运动路径相比，所提出的相机运动方法达到了99.9%的精度，并且优于最先进的相机路径估计方法。通过利用这种精确的相机路径，该系统有助于创建精确的3D模型，使其成为3D重建中需要高保真度和效率的应用的强大解决方案。 et.al.|[2503.17668](http://arxiv.org/abs/2503.17668)|null|
|**2025-03-21**|**Pow3R: Empowering Unconstrained 3D Reconstruction with Camera and Scene Priors**|我们提出了Pow3r，这是一种新型的大型3D视觉回归模型，在接受的输入模式方面具有高度的通用性。与之前缺乏在测试时利用已知相机或场景先验的任何机制的前馈模型不同，Pow3r在单个网络中结合了辅助信息的任何组合，如内部函数、相对姿态、密集或稀疏深度，以及输入图像。基于最新的DUSt3R范式，这是一种利用强大预训练的基于变换器的架构，我们的轻量级和多功能的调节为网络提供了额外的指导，以便在辅助信息可用时预测更准确的估计。在训练过程中，我们在每次迭代时向模型提供模态的随机子集，这使得模型能够在测试时在不同水平的已知先验下运行。这反过来又开辟了新的功能，例如以本机图像分辨率执行推理或点云完成。我们在3D重建、深度完成、多视图深度预测、多视图立体和多视图姿态估计任务上的实验产生了最先进的结果，并证实了Pow3r在利用所有可用信息方面的有效性。项目网页为https://europe.naverlabs.com/pow3r. et.al.|[2503.17316](http://arxiv.org/abs/2503.17316)|null|
|**2025-03-21**|**Ex vivo experiment on vertebral body with defect representing bone metastasis**|位于椎骨的溶骨性转移会降低强度，增加椎体骨折的风险。这种风险可以通过经过验证的有限元模型进行预测，但需要评估其可重复性。为此，需要实验数据。本研究的目的是在椎骨上进行开放式实验，人工缺陷代表溶解性转移，并使用明确的边界条件。通过去除皮质终板并钻松质骨制造代表溶解性转移的缺陷，制备了12个腰椎体（L1）。在创建缺陷之前和之后，使用临床高分辨率外围定量计算机断层扫描对椎体进行3D重建扫描。然后在压缩载荷下对试样进行测试，直至失效。表面数字图像相关性用于评估椎体前壁的应变场。这些数据（生物力学数据和构建特定受试者模型所需的断层图像）与科学界共享，以便在同一数据集上评估不同的椎体模型。 et.al.|[2503.17047](http://arxiv.org/abs/2503.17047)|null|
|**2025-03-21**|**DroneSplat: 3D Gaussian Splatting for Robust 3D Reconstruction from In-the-Wild Drone Imagery**|无人机因其出色的机动性而成为重建野生场景的重要工具。辐射场方法的最新进展取得了显著的渲染质量，为无人机图像的3D重建提供了新的途径。然而，野生环境中的动态干扰物挑战了辐射场中的静态场景假设，而有限的视图约束阻碍了对底层场景几何的准确捕捉。为了应对这些挑战，我们引入了DroneSplat，这是一种新颖的框架，旨在从野外无人机图像中进行稳健的3D重建。我们的方法通过将局部全局分割启发式方法与统计方法相结合，自适应地调整掩蔽阈值，从而能够精确识别和消除静态场景中的动态干扰物。我们通过多视图立体预测和体素引导优化策略增强了3D高斯散点，支持在有限视图约束下的高质量渲染。为了进行全面评估，我们提供了一个包含动态和静态场景的无人机捕获的3D重建数据集。大量实验表明，DroneSplat在处理野生无人机图像方面优于3DGS和NeRF基线。 et.al.|[2503.16964](http://arxiv.org/abs/2503.16964)|null|

<p align=right>(<a href=#updated-on-20250327>back to top</a>)</p>

## Diffusion

|Publish Date|Title|Abstract|PDF|Code|
|---|---|---|---|---|
|**2025-03-25**|**Learning 3D Object Spatial Relationships from Pre-trained 2D Diffusion Models**|我们提出了一种通过利用预先训练的2D扩散模型合成生成的3D样本来学习对象对之间的3D空间关系的方法，称为对象-对象空间关系（OOR）。我们假设，由2D扩散模型合成的图像天生就能捕捉到合理和真实的OOR线索，从而能够有效地收集3D数据集来学习各种无界对象类别的OOR。我们的方法首先合成各种图像，捕捉到合理的OOR线索，然后将其提升为3D样本。利用我们为对象对收集的各种看似合理的3D样本，我们训练了一个基于分数的OOR扩散模型来学习它们相对空间关系的分布。此外，我们通过在成对关系之间强制一致性并防止对象冲突，将成对OOR扩展到多对象OOR。大量实验证明了我们的方法在各种对象-对象空间关系中的鲁棒性，以及它对使用OOR扩散模型的真实世界3D场景排列任务的适用性。 et.al.|[2503.19914](http://arxiv.org/abs/2503.19914)|null|
|**2025-03-25**|**PartRM: Modeling Part-Level Dynamics with Large Cross-State Reconstruction Model**|随着人们对根据当前观测和行动预测未来状态的世界模型的兴趣日益浓厚，准确建模零件级动态对于各种应用来说变得越来越重要。现有的方法，如Puppet Master，依赖于对大规模预训练的视频扩散模型进行微调，由于2D视频表示的局限性和缓慢的处理时间，这些模型在现实世界中是不切实际的。为了克服这些挑战，我们提出了PartRM，这是一种新颖的4D重建框架，可以从静态对象的多视图图像中同时对外观、几何形状和零件级运动进行建模。PartRM基于大型3D高斯重建模型，利用其对静态对象外观和几何的广泛知识。为了解决4D中的数据稀缺问题，我们引入了PartDrag-4D数据集，提供了20000多个州的零件级动态的多视图观测。我们通过多尺度阻力嵌入模块增强了模型对相互作用条件的理解，该模块捕获了不同粒度下的动力学。为了防止在微调过程中发生灾难性遗忘，我们实施了一个两阶段的训练过程，该过程依次侧重于运动和外观学习。实验结果表明，PartRM建立了零件级运动学习的最新技术，可以应用于机器人的操纵任务。我们的代码、数据和模型是公开的，以促进未来的研究。 et.al.|[2503.19913](http://arxiv.org/abs/2503.19913)|null|
|**2025-03-26**|**AvatarArtist: Open-Domain 4D Avatarization**|这项工作侧重于开放域4D虚拟化，目的是从任意风格的肖像图像中创建4D虚拟形象。我们选择参数三平面作为中间的4D表示，并提出了一种实用的训练范式，该范式利用了生成对抗网络（GAN）和扩散模型。我们的设计源于观察到4D GAN擅长在没有监督的情况下桥接图像和三平面，但在处理不同的数据分布时通常会面临挑战。一个强大的2D扩散先验作为解决方案出现，帮助GAN在各个领域转移其专业知识。这些专家之间的协同作用允许构建多域图像三平面数据集，这推动了通用4D化身创建者的发展。大量实验表明，我们的模型AvatarArtist能够生成高质量的4D化身，对各种源图像域具有很强的鲁棒性。代码、数据和模型将公开，以促进未来的研究。 et.al.|[2503.19906](http://arxiv.org/abs/2503.19906)|null|
|**2025-03-25**|**ICE: Intrinsic Concept Extraction from a Single Image via Diffusion Models**|定义视觉概念的固有模糊性给现代生成模型（如基于扩散的文本到图像（T2I）模型）从单个图像中准确学习概念带来了重大挑战。现有的方法缺乏一种系统的方法来可靠地提取可解释的潜在内在概念。为了应对这一挑战，我们提出了ICE，即内在概念提取的缩写，这是一种新颖的框架，专门利用T2I模型从单个图像中自动系统地提取内在概念。ICE由两个关键阶段组成。在第一阶段，ICE设计了一个自动概念定位模块，以精确定位图像中相关的基于文本的概念及其相应的掩码。这一关键阶段简化了概念初始化，并为后续分析提供了精确的指导。第二阶段深入研究每个已识别的掩码，将对象级概念分解为内在概念和一般概念。这种分解允许对视觉元素进行更细粒度和可解释的分解。我们的框架在无监督的方式下从单个图像中提取内在概念方面表现出了卓越的性能。项目页面：https://visual-ai.github.io/ice et.al.|[2503.19902](http://arxiv.org/abs/2503.19902)|null|
|**2025-03-25**|**Scaling Down Text Encoders of Text-to-Image Diffusion Models**|扩散模型中的文本编码器发展迅速，从CLIP过渡到T5-XXL。尽管这一演变显著增强了模型理解复杂提示和生成文本的能力，但也导致了参数数量的大幅增加。尽管T5系列编码器是在C4自然语言语料库上训练的，其中包括大量的非视觉数据，但具有T5编码器的扩散模型对这些非视觉提示没有反应，这表明表征能力存在冗余。因此，它提出了一个重要的问题：“我们真的需要这么大的文本编码器吗？”为了寻找答案，我们采用基于视觉的知识提取来训练一系列T5编码器模型。为了充分继承其功能，我们基于三个标准构建了我们的数据集：图像质量、语义理解和文本渲染。我们的结果表明，提取的T5基础模型可以生成与T5-XXL生成的图像质量相当的图像，同时尺寸小50倍。模型尺寸的减小显著降低了运行FLUX和SD3等最先进模型的GPU要求，使高质量的文本到图像生成更容易实现。 et.al.|[2503.19897](http://arxiv.org/abs/2503.19897)|null|
|**2025-03-25**|**A Multi-Agent Framework Integrating Large Language Models and Generative AI for Accelerated Metamaterial Design**|超材料以其卓越的机械、电磁和热性能而闻名，在各种应用中具有变革潜力，但它们的设计仍然受到劳动密集型试错方法和有限数据互操作性的限制。在这里，我们介绍CrossMatAgent——一种新型的多智能体框架，它将大型语言模型与最先进的生成人工智能协同集成，从而彻底改变超材料设计。通过组织一个分层的代理团队——每个代理都专门从事模式分析、架构综合、即时工程和监督反馈等任务——我们的系统利用了GPT-4o的多模态推理以及DALL-E 3的生成精度和微调的Stable Diffusion XL模型。这种集成方法自动化了数据增强，提高了设计保真度，并产生了可用于模拟和3D打印的超材料图案。综合评估，包括基于CLIP的对齐、SHAP可解释性分析和不同负载条件下的机械模拟，证明了该框架生成多样化、可重复和应用就绪设计的能力。因此，CrossMatAgent建立了一个可扩展的、人工智能驱动的范式，弥合了概念创新和实际实现之间的差距，为加速超材料开发铺平了道路。 et.al.|[2503.19889](http://arxiv.org/abs/2503.19889)|null|
|**2025-03-25**|**Mask $^2$DiT: Dual Mask-based Diffusion Transformer for Multi-Scene Long Video Generation**|Sora揭示了扩散变换器（DiT）架构在单场景视频生成中的巨大潜力。然而，提供更广泛应用的多场景视频生成这一更具挑战性的任务仍然相对缺乏探索。为了弥合这一差距，我们提出了Mask$^2$DiT，这是一种新颖的方法，可以在视频片段与其相应的文本注释之间建立细粒度的一对一对齐。具体来说，我们在DiT架构中的每个注意力层引入了一个对称的二进制掩码，确保每个文本注释仅适用于其各自的视频片段，同时保持视觉标记之间的时间连贯性。这种注意力机制实现了精确的分段级文本与视觉对齐，使DiT架构能够有效地处理具有固定数量场景的视频生成任务。为了进一步使DiT架构具备基于现有场景生成额外场景的能力，我们引入了一个分段级条件掩码，该掩码将每个新生成的分段与前面的视频分段相结合，从而实现了自回归场景扩展。定性和定量实验都证实，Mask$^2$ DiT在保持分段之间的视觉一致性方面表现出色，同时确保每个分段与其相应的文本描述之间的语义对齐。我们的项目页面是https://tianhao-qi.github.io/Mask2DiTProject. et.al.|[2503.19881](http://arxiv.org/abs/2503.19881)|null|
|**2025-03-25**|**Role of enthalpy transport in laminar premixed hydrogen flames at atmospheric and elevated pressures**|这项工作讨论了扩散焓输运在热扩散不稳定性起源和由此增强的反应性方面的作用。预混合氢气火焰中的热扩散效应通常通过局部当量比波动来解释和建模。然而，这里重申的是，物种和热扩散之间的不平衡（微分扩散），而不是局部物种到物种的扩散不平衡（优先扩散）是主导顺序效应。通过分析未拉伸火焰中的焓通量发散项，证明反应物（H $_2$）、产物（H$_2$ O）和中间体（H）物种都在焓的传输中发挥作用。然后分析不同应变率和压力下的预混合逆流火焰，以证明反应性的增强源于焓传输和反应区相对于火焰厚度的宽度的组合。还讨论了关键压降反应的影响，以确定详细化学的重要性和泽尔多维奇数的使用。最后，对二维平面火焰进行了模拟和分析，以证明曲率和应变率的作用，并讨论了这些发现在混合和湍流火焰中的意义。 et.al.|[2503.19865](http://arxiv.org/abs/2503.19865)|null|
|**2025-03-25**|**Comparing the Run-time Behavior of Modern PDES Engines on Alternative Hardware Architectures**|当前的技术趋势使配备多个处理器和多个内存插槽的并行机器可以以合理的成本现成提供，或者通过Iaas Clouds租用。这为在工业或学术实验室等分散的现实中原生支持HPC开辟了可能性。与此同时，并行离散事件仿真（PDES）领域已经产生了有吸引力的仿真引擎，其设计面向高性能和可扩展性，也针对底层硬件提供的特定支持的差异化利用。在这篇文章中，我们进行了一项实验研究，在基于CISC或RISC技术的两个截然不同的硬件芯片组之上部署了两个上一代开源PDES平台——一个乐观（USE）和一个保守（PARSIR），这两个芯片组都提供了多个非统一内存访问（NUMA）节点和数十个内核和硬件线程（逻辑CPU）。此外，我们考虑了以各种不同方式配置的真实世界仿真模型，以研究PDES引擎在两个不同硬件平台上的实际执行情况。我们的目标是提供对当前性能趋势的见解，这可以支持离散事件模拟领域在软件平台采用策略和硬件平台投资方面的决策。 et.al.|[2503.19857](http://arxiv.org/abs/2503.19857)|null|
|**2025-03-25**|**FireEdit: Fine-grained Instruction-based Image Editing via Region-aware Vision Language Model**|目前，基于指令的图像编辑方法通过利用视觉语言模型（VLMs）强大的跨模态理解能力取得了重大进展。然而，他们仍然在三个关键领域面临挑战：1）复杂的情景；2） 语义一致性；以及3）细粒度编辑。为了解决这些问题，我们提出了FireEdit，这是一种创新的基于细粒度指令的图像编辑框架，利用了REgion感知的VLM。FireEdit旨在准确理解用户指令，并确保对编辑过程的有效控制。具体来说，我们通过引入额外的区域标记来增强VLM的细粒度视觉感知能力。仅依靠LLM的输出来指导扩散模型可能会导致次优的编辑结果。因此，我们提出了一种时间感知目标注入模块和一种混合视觉交叉注意力模块。前者通过将时间步长嵌入与文本嵌入相结合，在各个去噪阶段动态调整引导强度。后者增强了图像编辑的视觉细节，从而保持了编辑结果和源图像之间的语义一致性。通过将VLM增强与细粒度区域令牌和时间依赖扩散模型相结合，FireEdit在理解编辑指令和保持高度语义一致性方面显示出显著的优势。大量实验表明，我们的方法超越了最先进的基于指令的图像编辑方法。我们的项目可在https://zjgans.github.io/fireedit.github.io. et.al.|[2503.19839](http://arxiv.org/abs/2503.19839)|null|

<p align=right>(<a href=#updated-on-20250327>back to top</a>)</p>

## NeRF

|Publish Date|Title|Abstract|PDF|Code|
|---|---|---|---|---|
|**2025-03-25**|**Decoupled Dynamics Framework with Neural Fields for 3D Spatio-temporal Prediction of Vehicle Collisions**|本研究提出了一种神经框架，通过独立建模全局刚体运动和局部结构变形来预测3D车辆碰撞动力学。与直接预测绝对位移的方法不同，这种方法明确地将车辆的整体平移和旋转与其结构变形分开。两个专门的网络构成了该框架的核心：一个基于四元数的刚性网络用于刚性运动，一个基于坐标的变形网络用于局部变形。通过独立处理根本不同的物理现象，所提出的架构实现了准确的预测，而不需要对每个组件进行单独的监督。该模型仅在10%的可用模拟数据上进行训练，其性能明显优于基线模型，包括单层感知器（MLP）和深度算子网络（DeepONet），预测误差降低了83%。广泛的验证表明，它对训练范围外的碰撞条件具有很强的泛化能力，即使在涉及极端速度和大冲击角度的严重冲击下，也能准确预测响应。此外，该框架成功地从低分辨率输入重建了高分辨率变形细节，而无需增加计算工作量。因此，所提出的方法为在复杂的碰撞场景中快速可靠地评估车辆安全提供了一种有效、计算高效的方法，大大减少了所需的模拟数据和时间，同时保持了预测的保真度。 et.al.|[2503.19712](http://arxiv.org/abs/2503.19712)|null|
|**2025-03-21**|**Towards Understanding the Benefits of Neural Network Parameterizations in Geophysical Inversions: A Study With Neural Fields**|在这项工作中，我们采用了神经场，它使用神经网络以测试时学习的方式将坐标映射到该坐标处的相应物理属性值。对于测试时学习方法，与需要使用训练数据集训练网络的传统方法相比，在反演过程中学习权重。首先展示了地震层析成像和直流电阻率反演中的合成示例结果。然后，我们对这两种情况下的神经网络权重的雅可比矩阵进行奇异值分解分析（SVD分析），以探索神经网络对恢复模型的影响。结果表明，测试时间学习方法可以消除恢复的地下物理性质模型中由测量和物理敏感性引起的不必要的伪影。因此，在某些情况下，与常规反演相比，NFs-Inv可以改善反演结果，例如恢复倾角或预测主要目标的边界。在SVD分析中，我们观察到左奇异向量中的相似模式，就像在计算机视觉中的生成任务中以监督方式训练的一些扩散模型中观察到的那样。这一观察结果提供了证据，表明神经网络结构中固有的隐式偏差在监督学习和测试时学习模型中很有用。这种隐式偏差有可能对地球物理反演中的模型恢复有用。 et.al.|[2503.17503](http://arxiv.org/abs/2503.17503)|null|
|**2025-03-19**|**GO-N3RDet: Geometry Optimized NeRF-enhanced 3D Object Detector**|我们提出了GO-N3RDet，这是一种通过神经辐射场增强的场景几何优化的多视图3D物体检测器。准确的3D对象检测的关键在于有效的体素表示。然而，由于遮挡和缺乏3D信息，从多视图2D图像构建3D特征具有挑战性。为了解决这个问题，我们引入了一种独特的3D位置信息嵌入体素优化机制来融合多视图特征。为了优先考虑目标区域的神经场重建，我们还为探测器的NeRF分支设计了一种双重重要性采样方案。我们还提出了一个不透明度优化模块，通过实施多视图一致性约束来进行精确的体素不透明度预测。此外，为了进一步提高跨多个视角的体素密度一致性，我们将射线距离作为加权因子，以最小化累积射线误差。我们独特的模块协同形成了一个端到端的神经模型，建立了基于NeRF的多视图3D检测的最新技术，并在ScanNet和ARKITCenes上进行了广泛的实验验证。代码将在以下网址提供https://github.com/ZechuanLi/GO-N3RDet. et.al.|[2503.15211](http://arxiv.org/abs/2503.15211)|null|
|**2025-03-14**|**NF-SLAM: Effective, Normalizing Flow-supported Neural Field representations for object-level visual SLAM in automotive applications**|我们提出了一种新颖的、仅限视觉的对象级SLAM框架，用于通过隐式符号距离函数表示3D形状的汽车应用。我们的主要创新包括通过归一化流网络增强标准神经表示。因此，通过仅具有16维潜码的紧凑网络，可以在特定类别的道路车辆上实现强大的表示能力。此外，通过对合成数据的比较实验证明，新提出的架构在仅存在稀疏和噪声数据的情况下表现出显著的性能改进。该模块嵌入到基于立体视觉的框架的后端，用于联合增量形状优化。损失函数由基于稀疏3D点的SDF损失、稀疏渲染损失和基于语义掩码的轮廓一致性项的组合给出。我们还利用语义信息来确定前端的关键点提取密度。最后，对真实世界数据的实验结果显示，与使用直接深度读数的替代框架相比，其性能准确可靠。所提出的方法仅在通过束调整获得的稀疏3D点上表现良好，即使在仅使用掩模一致性项的情况下，最终也能继续提供稳定的结果。 et.al.|[2503.11199](http://arxiv.org/abs/2503.11199)|null|
|**2025-03-13**|**RSR-NF: Neural Field Regularization by Static Restoration Priors for Dynamic Imaging**|动态成像涉及使用欠采样测量值随时重建时空对象。特别是，在动态计算机断层扫描（dCT）中，一次只能获得一个视角的单个投影，这使得逆问题非常具有挑战性。此外，地面实况动态数据通常要么不可用，要么太稀缺，无法用于监督学习技术。为了解决这个问题，我们提出了RSR-NF，它使用神经场（NF）来表示动态对象，并使用去噪正则化（RED）框架，通过学习的恢复算子将额外的静态深空间先验合并到变分公式中。我们使用基于ADMM的可变分裂算法来有效地优化变分目标。我们将RSR-NF与三种替代方案进行了比较：仅具有时间正则化的NF；最近的一种方法，使用对静态数据进行预训练的去噪器，将部分可分离的低秩表示与RED相结合；以及基于深度图像先验的模型。第一个比较展示了通过将NF表示与静态恢复先验相结合所实现的重建改进，而另外两个则展示了与dCT的最新技术相比的改进。 et.al.|[2503.10015](http://arxiv.org/abs/2503.10015)|null|
|**2025-03-11**|**Representing 3D Shapes With 64 Latent Vectors for 3D Diffusion Models**|通过变分自编码器（VAE）构建压缩的潜在空间是高效3D扩散模型的关键。本文介绍了COD-VAE，这是一种在不牺牲质量的情况下将3D形状编码为1D潜在向量的COmpact集的VAE。COD-VAE引入了一种两级自动编码器方案，以提高压缩和解码效率。首先，我们的编码器块通过中间点补丁将点云逐步压缩为紧凑的潜在向量。其次，我们的基于三平面的解码器从潜在向量重建密集的三平面，而不是直接解码神经场，大大降低了神经场解码的计算开销。最后，我们提出了不确定性引导的令牌修剪，通过在更简单的区域跳过计算来自适应地分配资源，提高了解码器的效率。实验结果表明，与基线相比，COD-VAE在保持质量的同时实现了16倍的压缩。这使得生成速度提高了20.8倍，突显出大量潜在矢量不是高质量重建和生成的先决条件。 et.al.|[2503.08737](http://arxiv.org/abs/2503.08737)|null|
|**2025-03-09**|**Gaussian RBFNet: Gaussian Radial Basis Functions for Fast and Accurate Representation and Reconstruction of Neural Fields**|DeepSDF和神经辐射场等神经场最近彻底改变了RGB图像和视频的新颖视图合成和3D重建。然而，实现高质量的表示、重建和渲染需要深度神经网络，而深度神经网络的训练和评估速度很慢。尽管已经提出了几种加速技术，但它们经常以速度换取内存。另一方面，基于高斯飞溅的方法加快了渲染时间，但在存储大量高斯参数所需的训练速度和内存方面仍然成本高昂。在本文中，我们介绍了一种新的神经表示方法，它在训练和推理时间都很快，而且很轻。我们的关键观察是，传统MLP中使用的神经元执行简单的计算（点积，然后是ReLU激活），因此需要使用宽和深MLP或高分辨率和高维特征网格来参数化复杂的非线性函数。我们在这篇论文中表明，通过用径向基函数（RBF）核替换传统神经元，只需一层这样的神经元，就可以实现2D（RGB图像）、3D（几何）和5D（辐射场）信号的高精度表示。该表示具有高度的并行性，可在低分辨率特征网格上运行，并且结构紧凑，内存高效。我们证明，所提出的新表示可以在不到15秒的时间内训练出3D几何表示，在不到十五分钟的时间内就可以训练出新的视图合成。在运行时，它可以在不牺牲质量的情况下以超过60 fps的速度合成新颖的视图。 et.al.|[2503.06762](http://arxiv.org/abs/2503.06762)|null|
|**2025-03-09**|**X-LRM: X-ray Large Reconstruction Model for Extremely Sparse-View Computed Tomography Recovery in One Second**|稀疏视图3D CT重建旨在从有限数量的2D X射线投影中恢复体积结构。现有的前馈方法受到基于CNN的架构容量有限和大规模训练数据集稀缺的限制。本文提出了一种用于极稀疏视图（<10视图）CT重建的X射线大重建模型（X-LRM）。X-LRM由两个关键部件组成：X-former和X-triplane。我们的X-former可以使用基于MLP的图像标记器和基于Transformer的编码器来处理任意数量的输入视图。然后，输出标记被上采样到我们的X三平面表示中，该表示将3D辐射密度建模为隐式神经场。为了支持X-LRM的训练，我们引入了Torso-16K，这是一个由各种躯干器官的16K多个体积投影对组成的大规模数据集。大量实验表明，X-LRM的性能比最先进的方法高出1.5 dB，速度快27倍，灵活性更好。此外，肺部分割任务的下游评估也表明了我们方法的实用价值。我们的代码、预训练模型和数据集将于https://github.com/caiyuanhao1998/X-LRM et.al.|[2503.06382](http://arxiv.org/abs/2503.06382)|null|
|**2025-03-05**|**Distilling Dataset into Neural Field**|利用大规模数据集对于训练高性能深度学习模型至关重要，但它也带来了巨大的计算和存储成本。为了克服这些挑战，数据集蒸馏已成为一种有前景的解决方案，它将大规模数据集压缩成一个较小的合成数据集，保留了训练所需的基本信息。本文提出了一种新的数据集提取参数化框架，称为神经场提取数据集（DDiF），它利用神经场存储大规模数据集的必要信息。由于神经场以坐标作为输入和输出量的独特性质，DDiF有效地保留了信息，并易于生成各种形状的数据。我们从理论上证实，当单个合成实例的使用预算相同时，DDiF表现出比以前的一些文献更大的表现力。通过广泛的实验，我们证明DDiF在几个基准数据集上取得了卓越的性能，扩展到图像域之外，包括视频、音频和3D体素。我们在发布代码https://github.com/aailab-kaist/DDiF. et.al.|[2503.04835](http://arxiv.org/abs/2503.04835)|**[link](https://github.com/aailab-kaist/ddif)**|
|**2025-02-27**|**RANGE: Retrieval Augmented Neural Fields for Multi-Resolution Geo-Embeddings**|地理位置表示的选择会显著影响各种地理空间任务模型的准确性，包括细粒度物种分类、种群密度估计和生物群落分类。最近的作品，如SatCLIP和GeoCLIP，通过将地理位置与共置图像进行对比对齐来学习这种表示。虽然这些方法非常有效，但在本文中，我们认为当前的训练策略未能完全捕捉到重要的视觉特征。我们从信息论的角度解释了为什么这些方法产生的嵌入会丢弃对许多下游任务很重要的关键视觉信息。为了解决这个问题，我们提出了一种新的检索增强策略，称为RANGE。我们的方法基于这样一种直觉，即可以通过组合来自多个看起来相似的位置的视觉特征来估计位置的视觉特性。我们在各种各样的任务中评估我们的方法。我们的结果表明，RANGE在大多数任务中表现优于现有的最先进的模型，并具有显著的优势。我们显示，分类任务的收益高达13.1%，回归任务的收益为0.145 $R^2$ 。我们所有的代码都将在GitHub上发布。我们的模型将在HuggingFace上发布。 et.al.|[2502.19781](http://arxiv.org/abs/2502.19781)|null|

<p align=right>(<a href=#updated-on-20250327>back to top</a>)</p>

[contributors-shield]: https://img.shields.io/github/contributors/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[contributors-url]: https://github.com/Vincentqyw/cv-arxiv-daily/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[forks-url]: https://github.com/Vincentqyw/cv-arxiv-daily/network/members
[stars-shield]: https://img.shields.io/github/stars/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[stars-url]: https://github.com/Vincentqyw/cv-arxiv-daily/stargazers
[issues-shield]: https://img.shields.io/github/issues/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[issues-url]: https://github.com/Vincentqyw/cv-arxiv-daily/issues

