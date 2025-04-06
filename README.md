[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]

## Updated on 2025.04.06
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
|**2025-04-03**|**Unified World Models: Coupling Video and Action Diffusion for Pretraining on Large Robotic Datasets**|模仿学习已成为构建多面手机器人的一种有前景的方法。然而，由于依赖于高质量的专家演示，对大型机器人基础模型进行大规模模仿学习仍然具有挑战性。同时，描绘各种环境和不同行为的大量视频数据很容易获得。这些数据提供了有关真实世界动态和代理环境交互的丰富信息来源。然而，由于缺乏大多数现代方法所需的动作注释，直接利用这些数据进行模仿学习已被证明是困难的。在这项工作中，我们提出了统一世界模型（UWM），这是一个允许利用视频和行动数据进行政策学习的框架。具体来说，UWM在统一的变换器架构中集成了动作扩散过程和视频扩散过程，其中独立的扩散时间步长控制着每种模态。我们证明，通过简单地控制每个扩散时间步长，UWM可以灵活地表示策略、正向动态、反向动态和视频生成器。通过模拟和现实世界的实验，我们表明：（1）UWM能够对具有动力学和动作预测的大规模多任务机器人数据集进行有效的预训练，从而产生比模仿学习更具普遍性和鲁棒性的策略，（2）UWM通过独立控制特定模态的扩散时间步长，自然地促进了从无动作视频数据中的学习，进一步提高了微调策略的性能。我们的研究结果表明，UWM在利用大型异构数据集进行可扩展机器人学习方面迈出了有前景的一步，并在模仿学习和世界建模的经常不同的范式之间实现了简单的统一。视频和代码可在https://weirdlabuw.github.io/uwm/. et.al.|[2504.02792](http://arxiv.org/abs/2504.02792)|null|
|**2025-04-03**|**Scene Splatter: Momentum 3D Scene Generation from Single Image with Video Diffusion Model**|在本文中，我们提出了场景飞溅，这是一种基于动量的视频扩散范式，可以从单个图像生成通用场景。现有的方法采用视频生成模型来合成新的视图，但视频长度有限，场景不一致，导致在进一步重建过程中出现伪影和失真。为了解决这个问题，我们从原始特征中构建噪声样本作为动量，以增强视频细节并保持场景一致性。然而，对于具有跨越已知和未知区域的感知场的潜在特征，这种潜在水平动量限制了未知区域中视频扩散的生成能力。因此，我们进一步将上述一致视频作为像素级动量引入到直接生成的无动量视频中，以更好地恢复看不见的区域。我们的级联动量使视频扩散模型能够生成高保真度和一致的新颖视图。我们进一步使用增强帧对全局高斯表示进行微调，并在下一步渲染新帧以进行动量更新。通过这种方式，我们可以迭代地恢复3D场景，避免视频长度的限制。大量实验证明了我们的方法在高保真度和一致性场景生成方面的泛化能力和优越性能。 et.al.|[2504.02764](http://arxiv.org/abs/2504.02764)|null|
|**2025-04-03**|**Audio-visual Controlled Video Diffusion with Masked Selective State Spaces Modeling for Natural Talking Head Generation**|会说话的头部合成对于虚拟化身和人机交互至关重要。然而，大多数现有的方法通常仅限于接受来自单一主要模态的控制，这限制了它们的实际应用。为此，我们引入\textbf{ACTalker}，这是一个端到端的视频扩散框架，支持多信号控制和单信号控制，用于生成说话头视频。对于多重控制，我们设计了一个具有多个分支的并行曼巴结构，每个分支都利用单独的驱动信号来控制特定的面部区域。门机制应用于所有分支，提供对视频生成的灵活控制。为了确保受控视频在时间和空间上的自然协调，我们采用了曼巴结构，该结构使驱动信号能够在每个分支的两个维度上操纵特征标记。此外，我们引入了一种掩模丢弃策略，允许每个驱动信号独立控制曼巴结构内相应的面部区域，防止控制冲突。实验结果表明，我们的方法产生了由不同信号驱动的自然面部视频，曼巴层无缝集成了多种驱动方式，没有冲突。 et.al.|[2504.02542](http://arxiv.org/abs/2504.02542)|null|
|**2025-04-03**|**ConMo: Controllable Motion Disentanglement and Recomposition for Zero-Shot Motion Transfer**|文本到视频（T2V）生成的发展使运动传输成为可能，从而能够基于现有镜头控制视频运动。然而，目前的方法有两个局限性：1）难以处理多主题视频，无法传输特定的主题运动；2） 在转移到不同形状的物体时，努力保持运动的多样性和准确性。为了克服这些问题，我们引入了\textbf｛ConMo｝，这是一个零样本框架，可以解开并重新组合被摄体的运动和相机的运动。ConMo仅使用主题掩码从源视频中的复杂轨迹中分离出单个主题和背景运动线索，并将其重新组装以生成目标视频。这种方法实现了跨不同主题的更精确的运动控制，并提高了多主题场景中的性能。此外，我们提出在重组阶段进行软引导，控制原始运动的保留以调整形状约束，帮助主体形状适应和语义转换。与以前的方法不同，ConMo解锁了广泛的应用程序，包括主题大小和位置编辑、主题移除、语义修改和相机运动模拟。大量实验表明，ConMo在运动保真度和语义一致性方面明显优于最先进的方法。该代码可在以下网址获得https://github.com/Andyplus1/ConMo. et.al.|[2504.02451](http://arxiv.org/abs/2504.02451)|null|
|**2025-04-03**|**SkyReels-A2: Compose Anything in Video Diffusion Transformers**|本文介绍了SkyReels-A2，这是一种可控的视频生成框架，能够根据文本提示将任意视觉元素（如字符、对象、背景）组装成合成视频，同时与每个元素的参考图像保持严格一致。我们将此任务元素称为视频（E2V），其主要挑战在于保持每个参考元素的保真度，确保场景的连贯构图，并实现自然输出。为了解决这些问题，我们首先设计了一个全面的数据管道来构建用于模型训练的即时参考视频三元组。接下来，我们提出了一种新的图像-文本联合嵌入模型，将多元素表示注入生成过程，平衡元素特定的一致性与全局连贯性和文本对齐。我们还优化了推理管道的速度和输出稳定性。此外，我们引入了一个精心策划的系统评估基准，即A2 Bench。实验证明，我们的框架可以生成具有精确元素控制的多样化、高质量的视频。SkyReels-A2是E2V一代的第一款开源商业级车型，与先进的闭源商业车型相比表现良好。我们预计SkyReels-A2将推进戏剧和虚拟电子商务等创意应用，突破可控视频生成的界限。 et.al.|[2504.02436](http://arxiv.org/abs/2504.02436)|null|
|**2025-04-03**|**MG-Gen: Single Image to Motion Graphics Generation with Layer Decomposition**|一般的图像到视频生成方法通常会产生不符合动画图形要求的次优动画，因为它们缺乏主动文本运动并表现出对象失真。此外，基于代码的动画生成方法通常需要层结构的矢量数据，而这些数据通常不易用于运动图形生成。为了应对这些挑战，我们提出了一个名为MG-Gen的新框架，该框架从单个光栅图像重建矢量格式的数据，以扩展基于代码的方法的能力，从而在通用图像到视频生成的框架中从光栅图像生成运动图形。MG Gen首先将输入图像分解为逐层元素，将其重建为HTML格式数据，然后为重建的HTML数据生成可执行的JavaScript代码。我们通过实验证实，我们的{}在保持文本可读性和输入一致性的同时生成了运动图形。这些成功的结果表明，将层分解和动画代码生成相结合是一种有效的运动图形生成策略。 et.al.|[2504.02361](http://arxiv.org/abs/2504.02361)|null|
|**2025-04-03**|**OmniCam: Unified Multimodal Video Generation via Camera Control**|通过改变相机位置和姿态来实现多样化视觉效果的相机控制引起了广泛关注。然而，现有的方法面临着复杂的交互和有限的控制能力等挑战。为了解决这些问题，我们提出了OmniCam，这是一个统一的多模式相机控制框架。利用大型语言模型和视频扩散模型，OmniCam生成时空一致的视频。它支持各种输入方式的组合：用户可以提供具有预期轨迹的文本或视频作为相机路径引导，图像或视频作为内容参考，从而实现对相机运动的精确控制。为了便于训练OmniCam，我们引入了OmniTr数据集，其中包含大量高质量的长序列轨迹、视频和相应的描述。实验结果表明，我们的模型在各种指标的高质量相机控制视频生成方面取得了最先进的性能。 et.al.|[2504.02312](http://arxiv.org/abs/2504.02312)|null|
|**2025-04-02**|**WorldPrompter: Traversable Text-to-Scene Generation**|场景级3D生成是一个具有挑战性的研究课题，大多数现有方法只生成部分场景，提供的导航自由度有限。我们介绍了WorldPrompter，这是一种新颖的生成管道，用于从文本提示中合成可遍历的3D场景。我们利用全景视频作为中间表示来模拟场景的360度细节。WorldPrompter集成了一个有条件的360度全景视频生成器，能够生成128帧的视频，模拟一个人走过并捕捉虚拟环境。然后，快速前馈3D重建器将得到的视频重建为高斯斑点，从而在3D场景中实现真正的步行体验。实验证明，我们的全景视频生成模型在帧之间实现了令人信服的视图一致性，实现了高质量的全景高斯斑点重建，并促进了场景区域的遍历。定性和定量结果还表明，它优于最先进的360度视频生成器和3D场景生成模型。 et.al.|[2504.02045](http://arxiv.org/abs/2504.02045)|null|
|**2025-04-03**|**VideoScene: Distilling Video Diffusion Model to Generate 3D Scenes in One Step**|由于其固有的不适定问题，从稀疏视图中恢复3D场景是一项具有挑战性的任务。传统方法已经开发出专门的解决方案（例如几何正则化或前馈确定性模型）来缓解这个问题。然而，由于输入视图之间的重叠最小，视觉信息不足，它们的性能仍然会下降。幸运的是，最近的视频生成模型在解决这一挑战方面显示出希望，因为它们能够生成具有合理3D结构的视频片段。在大型预训练视频扩散模型的支持下，一些开创性的研究开始探索视频生成先验的潜力，并从稀疏视图创建3D场景。尽管有令人印象深刻的改进，但它们受到推理时间慢和缺乏3D约束的限制，导致效率低下和重建伪影与现实世界的几何结构不一致。本文中，我们提出了VideoScene来提取视频扩散模型，一步生成3D场景，旨在构建一个高效有效的工具来弥合视频到3D的差距。具体来说，我们设计了一种3D感知的跳跃流蒸馏策略，以跳过耗时的冗余信息，并训练一个动态去噪策略网络，以自适应地确定推理过程中的最佳跳跃时间步长。大量实验表明，我们的VideoScene实现了比以前的视频扩散模型更快、更优的3D场景生成结果，突显了它作为未来视频到3D应用的有效工具的潜力。项目页面：https://hanyang-21.github.io/VideoScene et.al.|[2504.01956](http://arxiv.org/abs/2504.01956)|null|
|**2025-04-01**|**Articulated Kinematics Distillation from Video Diffusion Models**|我们提出了铰接运动学蒸馏（AKD），这是一个通过融合基于骨架的动画和现代生成模型的优势来生成高保真角色动画的框架。AKD使用基于骨架的表示来表示操纵的3D资源，通过专注于关节级控制来大幅降低自由度（DoF），从而实现高效、一致的运动合成。通过带有预训练视频扩散模型的分数蒸馏采样（SDS），AKD在保持结构完整性的同时提取复杂的关节运动，克服了4D神经变形场在保持形状一致性方面面临的挑战。这种方法与基于物理的模拟自然兼容，确保了物理上合理的交互。实验表明，与现有的文本到4D生成工作相比，AKD实现了更优的3D一致性和运动质量。项目页面：https://research.nvidia.com/labs/dir/akd/ et.al.|[2504.01204](http://arxiv.org/abs/2504.01204)|null|

<p align=right>(<a href=#updated-on-20250406>back to top</a>)</p>

## 3D

|Publish Date|Title|Abstract|PDF|Code|
|---|---|---|---|---|
|**2025-04-03**|**MD-ProjTex: Texturing 3D Shapes with Multi-Diffusion Projection**|我们介绍了MD ProjTex，这是一种使用预训练的文本到图像扩散模型为3D形状快速一致地生成文本引导纹理的方法。我们方法的核心是UV空间中的多视图一致性机制，它确保了不同视点之间的连贯纹理。具体来说，MD ProjTex在每个扩散步骤融合来自多个视图的噪声预测，并联合更新每个视图的去噪方向，以保持3D一致性。与依赖于优化或顺序视图合成的现有最先进的方法相比，MD-ProjTex在计算上更高效，并获得了更好的定量和定性结果。 et.al.|[2504.02762](http://arxiv.org/abs/2504.02762)|null|
|**2025-04-02**|**Diffusion-Guided Gaussian Splatting for Large-Scale Unconstrained 3D Reconstruction and Novel View Synthesis**|3D高斯散斑（3DGS）和神经辐射场（NeRF）的最新进展在实时3D重建和新颖的视图合成方面取得了令人印象深刻的结果。然而，这些方法在大规模、无约束的环境中很难实现，在这些环境中，稀疏和不均匀的输入覆盖、瞬态遮挡、外观可变性和不一致的相机设置会导致质量下降。我们提出了GS-Diff，一种由多视图扩散模型引导的新型3DGS框架，以解决这些局限性。通过生成以多视图输入为条件的伪观测值，我们的方法将受约束的3D重建问题转化为适定问题，即使在稀疏数据的情况下也能实现鲁棒优化。GS-Diff还集成了一些增强功能，包括外观嵌入、单目深度先验、动态对象建模、各向异性正则化和高级光栅化技术，以解决现实世界中的几何和光度挑战。在四个基准上的实验表明，GS-Diff始终以显著的优势优于最先进的基线。 et.al.|[2504.01960](http://arxiv.org/abs/2504.01960)|null|
|**2025-04-02**|**BOGausS: Better Optimized Gaussian Splatting**|3D高斯散斑（3DGS）为新颖的视图合成提出了一种有效的解决方案。它的框架提供了快速和高保真的渲染。虽然比神经辐射场（NeRF）等其他解决方案简单，但在不牺牲质量的情况下构建较小的模型仍然存在一些挑战。在这项研究中，我们对3DGS训练过程进行了仔细的分析，并提出了一种新的优化方法。我们的优化高斯散斑（BOGausS）解决方案能够生成比原始3DGS轻十倍的模型，而不会降低质量，从而与最新技术相比显著提高了高斯散斑的性能。 et.al.|[2504.01844](http://arxiv.org/abs/2504.01844)|null|
|**2025-04-02**|**FIORD: A Fisheye Indoor-Outdoor Dataset with LIDAR Ground Truth for 3D Scene Reconstruction and Benchmarking**|大规模3D场景重建和新型视图合成方法的发展主要依赖于包含窄视场（FoV）透视图像的数据集。虽然对小规模场景有效，但这些数据集需要大型图像集和广泛的运动结构（SfM）处理，限制了可扩展性。为了解决这个问题，我们引入了一个为场景重建任务量身定制的鱼眼图像数据集。使用双200度鱼眼镜头，我们的数据集提供了5个室内和5个室外场景的360度全覆盖。每个场景都有稀疏的SfM点云和精确的LIDAR衍生的密集点云，可以用作几何地面真实值，在遮挡和反射等具有挑战性的条件下实现稳健的基准测试。虽然基线实验侧重于香草高斯Splatting和基于NeRF的Nerfacto方法，但该数据集支持场景重建、新颖视图合成和基于图像的渲染的多种方法。 et.al.|[2504.01732](http://arxiv.org/abs/2504.01732)|null|
|**2025-04-02**|**FlowR: Flowing from Sparse to Dense 3D Reconstructions**|3D高斯飞溅技术能够以实时帧率实现高质量的新颖视图合成（NVS）。然而，随着我们偏离训练的观点，它的质量急剧下降。因此，需要密集的捕捉来满足某些应用程序的高质量期望，例如虚拟现实（VR）。然而，获得如此密集的捕获是非常费力和昂贵的。现有的工作已经探索了使用2D生成模型通过蒸馏或生成额外的训练视图来缓解这一要求。这些方法通常仅以少数参考输入视图为条件，因此没有充分利用可用的3D信息，导致生成结果不一致和重建伪影。为了解决这个问题，我们提出了一种多视图流匹配模型，该模型学习一个流，将可能稀疏重建的新视图渲染连接到我们期望密集重建的渲染。这使得能够用新颖的、生成的视图来增强场景捕获，以提高重建质量。我们的模型是在一个360万图像对的新数据集上训练的，可以在一个H100 GPU上以540x960分辨率（91K令牌）在一次前向传递中处理多达45个视图。我们的流水线在稀疏和密集视图场景中持续改进NVS，从而在多个广泛使用的NVS基准测试中实现比先前工作更高质量的重建。 et.al.|[2504.01647](http://arxiv.org/abs/2504.01647)|null|
|**2025-04-02**|**Luminance-GS: Adapting 3D Gaussian Splatting to Challenging Lighting Conditions with View-Adaptive Curve Adjustment**|在不同的现实世界照明条件下捕捉高质量的照片是具有挑战性的，因为自然光照（如低光照）和相机曝光设置（如曝光时间）都会显著影响图像质量。在多视图场景中，这一挑战变得更加明显，因为不同视点之间的照明和图像信号处理器（ISP）设置的变化会导致光度不一致。这种照明退化和视图相关变化对基于神经辐射场（NeRF）和3D高斯散斑（3DGS）的新型视图合成（NVS）框架提出了重大挑战。为了解决这个问题，我们引入了Luminance GS，这是一种使用3DGS在各种具有挑战性的照明条件下实现高质量新颖视图合成结果的新方法。通过采用每视图颜色矩阵映射和视图自适应曲线调整，Luminance GS在各种照明条件下（包括低光、曝光过度和曝光变化）都能获得最先进的（SOTA）结果，同时不会改变原始的3DGS显式表示。与之前基于NeRF和3DGS的基线相比，Luminance GS提供了实时渲染速度和改进的重建质量。 et.al.|[2504.01503](http://arxiv.org/abs/2504.01503)|null|
|**2025-04-01**|**NeuRadar: Neural Radiance Fields for Automotive Radar Point Clouds**|雷达是自动驾驶（AD）系统的重要传感器，因为它对恶劣天气和不同光照条件具有鲁棒性。使用神经辐射场（NeRFs）的新型视图合成最近在AD中受到了相当大的关注，因为它有可能实现高效的测试和验证，但对于雷达点云仍未进行探索。在本文中，我们介绍了NeuRadar，这是一种基于NeRF的模型，可以联合生成雷达点云、相机图像和激光雷达点云。我们探索了基于集合的对象检测方法，如DETR，并提出了一种基于NeRF几何的编码器解决方案，以提高泛化能力。我们提出了一种确定性和概率性的点云表示方法来精确地模拟雷达行为，后者能够捕捉雷达的随机行为。我们为两个汽车数据集实现了逼真的重建结果，为基于NeRF的雷达点云仿真模型建立了基线。此外，我们还发布了ZOD序列和驱动器的雷达数据，以促进该领域的进一步研究。为了鼓励雷达NeRF的进一步发展，我们发布了NeuRadar的源代码。 et.al.|[2504.00859](http://arxiv.org/abs/2504.00859)|null|
|**2025-04-01**|**DropGaussian: Structural Regularization for Sparse-view Gaussian Splatting**|最近，3D高斯散斑（3DGS）因其快速的性能和出色的图像质量而在新型视图合成领域受到了广泛关注。然而，稀疏视图设置（例如，三个视图输入）中的3DGS经常面临与训练视图过拟合的问题，这大大降低了新视图图像的视觉质量。许多现有的方法通过使用强先验来解决这个问题，例如2D生成上下文信息和外部深度信号。相比之下，本文介绍了一种先验自由方法，即所谓的DropGaussian，它对3D高斯飞溅进行了简单的改变。具体来说，我们在训练过程中以类似的dropout方式随机删除高斯分布，这使得非排除的高斯分布具有更大的梯度，同时提高了它们的可见性。这使得剩余的高斯分布对稀疏输入视图渲染的优化过程做出了更大的贡献。这种简单的操作有效地缓解了过拟合问题，提高了新颖视图合成的质量。通过简单地将DropGaussian应用于原始3DGS框架，我们可以在基准数据集的稀疏视图设置中实现与现有基于先验的3DGS方法具有竞争力的性能，而无需任何额外的复杂性。代码和模型可在以下网址公开获取：https://github.com/DCVL-3D/DropGaussian释放。 et.al.|[2504.00773](http://arxiv.org/abs/2504.00773)|null|
|**2025-04-01**|**Coca-Splat: Collaborative Optimization for Camera Parameters and 3D Gaussians**|在这项工作中，我们介绍了Coca-Splat，这是一种通过使用3D高斯联合优化相机参数来解决稀疏视图无姿态场景重建和新颖视图合成（NVS）挑战的新方法。受可变形检测变换器的启发，我们为3D高斯和相机参数设计了单独的查询，并通过可变形变换器层逐层更新它们，从而在单个网络中实现联合优化。这种设计表现出更好的性能，因为精确渲染接近地面真实图像的视图依赖于对3D高斯和摄像机参数的精确估计。在这种设计中，通过相机参数将3D高斯分布的中心投影到每个视图上，得到投影点，这些投影点在可变形交叉注意力中被视为2D参考点。通过相机感知多视图可变形交叉注意（CaMDFA），3D高斯和相机参数通过共享2D参考点而内在地联系在一起。此外，从相机中心到参考点定义的2D参考点确定射线（RayRef）通过对从射线导出的超定方程组进行RQ分解，有助于对3D高斯和相机参数之间的关系进行建模，增强了3D高斯和摄像机参数之间的关系。广泛的评估表明，在相同的无姿势设置下，我们的方法在RealEstate10K和ACID上优于之前的方法，无论是需要姿势还是无姿势。 et.al.|[2504.00639](http://arxiv.org/abs/2504.00639)|null|
|**2025-03-31**|**LITA-GS: Illumination-Agnostic Novel View Synthesis via Reference-Free 3D Gaussian Splatting and Physical Priors**|在具有不利光照条件的图像上直接采用3D高斯散斑（3DGS）在实现高质量、正常曝光的表示方面存在相当大的困难，原因是：（1）在不利光照场景中估计的有限运动结构（SfM）点无法捕捉到足够的场景细节；（2） 如果没有地面真实参考，密集的信息丢失、显著的噪声和颜色失真对3DGS产生高质量的结果构成了重大挑战；（3） 将现有的曝光校正方法与3DGS相结合，由于其各自的增强过程，导致不同视点的增强图像之间的照明不一致，因此无法达到令人满意的性能。为了解决这些问题，我们提出了LITA-GS，这是一种基于无参考3DGS和物理先验的新型光照无关视图合成方法。首先，我们介绍了一种光照不变的物理先验提取流水线。其次，基于提取的鲁棒空间结构先验，我们开发了与光照无关的结构渲染策略，这有助于优化场景结构和对象外观。此外，引入了渐进式去噪模块，以有效减轻光不变表示中的噪声。我们采用无监督策略对LITA-GS进行训练，大量实验表明，LITA-GS超越了最先进的（SOTA）基于NeRF的方法，同时具有更快的推理速度和更短的训练时间。代码发布于https://github.com/LowLevelAI/LITA-GS. et.al.|[2504.00219](http://arxiv.org/abs/2504.00219)|null|

<p align=right>(<a href=#updated-on-20250406>back to top</a>)</p>

## 3D Reconstruction

|Publish Date|Title|Abstract|PDF|Code|
|---|---|---|---|---|
|**2025-04-03**|**MD-ProjTex: Texturing 3D Shapes with Multi-Diffusion Projection**|我们介绍了MD ProjTex，这是一种使用预训练的文本到图像扩散模型为3D形状快速一致地生成文本引导纹理的方法。我们方法的核心是UV空间中的多视图一致性机制，它确保了不同视点之间的连贯纹理。具体来说，MD ProjTex在每个扩散步骤融合来自多个视图的噪声预测，并联合更新每个视图的去噪方向，以保持3D一致性。与依赖于优化或顺序视图合成的现有最先进的方法相比，MD-ProjTex在计算上更高效，并获得了更好的定量和定性结果。 et.al.|[2504.02762](http://arxiv.org/abs/2504.02762)|null|
|**2025-04-03**|**LPA3D: 3D Room-Level Scene Generation from In-the-Wild Images**|从野外图像中生成具有语义上合理和详细外观的逼真的房间级室内场景对于VR、AR和机器人的各种应用至关重要。基于NeRF的生成方法的成功表明了解决这一挑战的一个有前景的方向。然而，与它们在对象级别的成功不同，现有的场景级生成方法需要额外的信息，如多视图、深度图像或语义指导，而不是仅仅依赖RGB图像。这是因为基于NeRF的方法需要相机姿态的先验知识，由于定义对齐的复杂性以及在相机后面看不见的部分的情况下从单个图像全局估计姿态的困难，这对室内场景的近似具有挑战性。为了应对这一挑战，我们在局部姿态对齐（LPA）的框架内重新定义了全局姿态，这是一种基于锚点的多局部坐标系，使用选定数量的锚点作为这些坐标的根。在此基础上，我们介绍了LPA-GAN，这是一种基于NeRF的生成方法，它结合了特定的修改来估计LPA下相机姿态的先验。它还共同优化了姿态预测器和场景生成过程。我们的消融研究以及与基于NeRF的对象生成方法的直接扩展的比较证明了我们方法的有效性。此外，与其他技术的视觉比较表明，我们的方法实现了更好的视图间一致性和语义正态性。 et.al.|[2504.02337](http://arxiv.org/abs/2504.02337)|null|
|**2025-04-03**|**MultiTSF: Transformer-based Sensor Fusion for Human-Centric Multi-view and Multi-modal Action Recognition**|多模态和多视图观测的动作识别在监控、机器人和智能环境中具有巨大的应用潜力。然而，现有的方法往往无法解决现实世界的挑战，如不同的环境条件、严格的传感器同步以及对细粒度注释的需求。在这项研究中，我们提出了基于多模态多视图变换的传感器融合（MultiTSF）。所提出的方法利用基于Transformer的动态建模视图间关系，并捕获多个视图之间的时间依赖关系。此外，我们引入了一个人类检测模块来生成伪地面真实标签，使模型能够优先考虑包含人类活动的帧，并增强空间特征学习。在我们内部的MultiSensor Home数据集和现有的MM Office数据集上进行的综合实验表明，MultiTSF在视频序列级和帧级动作识别设置中都优于最先进的方法。 et.al.|[2504.02279](http://arxiv.org/abs/2504.02279)|null|
|**2025-04-02**|**A Chefs KISS -- Utilizing semantic information in both ICP and SLAM framework**|为了在城市地区使用自动驾驶汽车，需要可靠的定位。特别是在使用高清地图时，必须选择一种精确且可重复的方法。因此，精确的地图生成以及针对这些地图的重新定位都是必要的。由于对周围环境的最佳3D重建，激光雷达已成为一种可靠的定位方式。最新的激光雷达里程计估计基于迭代最近点（ICP）方法，即KISS-ICP和SAGE-ICP。我们通过使用具有最小参数调整的通用方法将语义信息纳入点对齐过程，扩展了KISS-ICP的功能。这种增强使我们能够在绝对轨迹误差（ATE）方面超越KISS-ICP，ATE是地图精度的主要指标。此外，我们改进了Cartographer映射框架来处理语义信息。制图器有助于在更大的区域进行环路闭合检测，减轻里程计漂移，进一步提高ATE精度。通过将语义信息集成到映射过程中，我们可以从生成的地图中过滤特定的类，如停放的车辆。这种过滤通过解决时间变化（如车辆移动）来提高重新定位质量。 et.al.|[2504.02086](http://arxiv.org/abs/2504.02086)|null|
|**2025-04-02**|**Evaluation of Flight Parameters in UAV-based 3D Reconstruction for Rooftop Infrastructure Assessment**|使用基于无人机的摄影测量进行屋顶3D重建为基础设施评估提供了一种有前景的解决方案，但现有的方法在使用自主飞行路径时通常需要高百分比的图像重叠和延长的飞行时间来确保模型的准确性。本研究系统地评估了关键飞行参数地面采样距离（GSD）和图像重叠，以优化复杂屋顶基础设施的3D重建。使用大疆幻影4 Pro V2在女王大学的多段屋顶上进行了受控无人机飞行，具有不同的GSD和重叠设置。收集的数据使用Reality Capture软件进行处理，并根据基于无人机的激光雷达和地面激光扫描（TLS）生成的地面实况模型进行评估。实验结果表明，0.75-1.26 cm的GSD范围与85%的图像重叠相结合，实现了高度的模型精度，同时最大限度地减少了收集的图像和飞行时间。这些发现为规划自主无人机飞行路径以进行高效的屋顶评估提供了指导。 et.al.|[2504.02084](http://arxiv.org/abs/2504.02084)|null|
|**2025-04-02**|**Diffusion-Guided Gaussian Splatting for Large-Scale Unconstrained 3D Reconstruction and Novel View Synthesis**|3D高斯散斑（3DGS）和神经辐射场（NeRF）的最新进展在实时3D重建和新颖的视图合成方面取得了令人印象深刻的结果。然而，这些方法在大规模、无约束的环境中很难实现，在这些环境中，稀疏和不均匀的输入覆盖、瞬态遮挡、外观可变性和不一致的相机设置会导致质量下降。我们提出了GS-Diff，一种由多视图扩散模型引导的新型3DGS框架，以解决这些局限性。通过生成以多视图输入为条件的伪观测值，我们的方法将受约束的3D重建问题转化为适定问题，即使在稀疏数据的情况下也能实现鲁棒优化。GS-Diff还集成了一些增强功能，包括外观嵌入、单目深度先验、动态对象建模、各向异性正则化和高级光栅化技术，以解决现实世界中的几何和光度挑战。在四个基准上的实验表明，GS-Diff始终以显著的优势优于最先进的基线。 et.al.|[2504.01960](http://arxiv.org/abs/2504.01960)|null|
|**2025-04-03**|**Toward Real-world BEV Perception: Depth Uncertainty Estimation via Gaussian Splatting**|鸟瞰图（BEV）感知受到了广泛关注，因为它提供了一种统一的表示方式来融合多个视图图像，并支持广泛的下游自动驾驶任务，如预测和规划。最近最先进的模型利用基于投影的方法，将BEV感知转化为查询学习，以绕过显式深度估计。虽然我们观察到这一范式取得了有希望的进展，但由于缺乏不确定性建模和昂贵的计算要求，它们仍然无法满足现实世界的应用。在这项工作中，我们介绍了GaussianLSS，这是一种新的不确定性感知BEV感知框架，它修改了基于非投影的方法，特别是Lift Splat Shoot（LSS）范式，并通过深度不确定性建模对其进行了增强。GaussianLSS通过学习软深度均值并计算深度分布的方差来表示空间色散，这隐式地捕获了对象范围。然后，我们将深度分布转换为3D高斯分布，并对其进行光栅化，以构建具有不确定性感知的BEV特征。我们在nuScenes数据集上评估了GaussianLSS，与基于非投影的方法相比，实现了最先进的性能。特别是，与基于投影的方法相比，它在速度、运行速度和内存效率方面具有显著优势，使用的内存减少了0.3倍，同时实现了具有竞争力的性能，IoU差异仅为0.4%。 et.al.|[2504.01957](http://arxiv.org/abs/2504.01957)|null|
|**2025-04-02**|**BlenderGym: Benchmarking Foundational Model Systems for Graphics Editing**|3D图形编辑在电影制作和游戏设计等应用中至关重要，但它仍然是一个耗时的过程，需要高度专业化的领域专业知识。自动化这一过程具有挑战性，因为图形编辑需要执行各种任务，每项任务都需要不同的技能。最近，视觉语言模型（VLMs）已经成为自动化编辑过程的强大框架，但由于缺乏需要人类感知并呈现现实世界编辑复杂性的全面基准，其开发和评估受到了瓶颈。在这项工作中，我们介绍了BlenderGym，这是第一个用于3D图形编辑的全面VLM系统基准。BlenderGym通过基于代码的3D重建任务评估VLM系统。我们评估了封闭式和开源VLM系统，并观察到即使是最先进的VLM系统也难以完成人类Blender用户相对容易的任务。在BlenderGym的支持下，我们研究了推理缩放技术如何影响VLM在图形编辑任务中的性能。值得注意的是，我们的研究结果表明，用于指导生成缩放的验证器本身可以通过推理缩放来改进，补充了最近关于编码和数学任务中LLM生成推理缩放的见解。我们进一步表明，推理计算不是一致有效的，可以通过在生成和验证之间进行策略性分配来优化。 et.al.|[2504.01786](http://arxiv.org/abs/2504.01786)|null|
|**2025-04-02**|**FlowR: Flowing from Sparse to Dense 3D Reconstructions**|3D高斯飞溅技术能够以实时帧率实现高质量的新颖视图合成（NVS）。然而，随着我们偏离训练的观点，它的质量急剧下降。因此，需要密集的捕捉来满足某些应用程序的高质量期望，例如虚拟现实（VR）。然而，获得如此密集的捕获是非常费力和昂贵的。现有的工作已经探索了使用2D生成模型通过蒸馏或生成额外的训练视图来缓解这一要求。这些方法通常仅以少数参考输入视图为条件，因此没有充分利用可用的3D信息，导致生成结果不一致和重建伪影。为了解决这个问题，我们提出了一种多视图流匹配模型，该模型学习一个流，将可能稀疏重建的新视图渲染连接到我们期望密集重建的渲染。这使得能够用新颖的、生成的视图来增强场景捕获，以提高重建质量。我们的模型是在一个360万图像对的新数据集上训练的，可以在一个H100 GPU上以540x960分辨率（91K令牌）在一次前向传递中处理多达45个视图。我们的流水线在稀疏和密集视图场景中持续改进NVS，从而在多个广泛使用的NVS基准测试中实现比先前工作更高质量的重建。 et.al.|[2504.01647](http://arxiv.org/abs/2504.01647)|null|
|**2025-04-01**|**Neural Pruning for 3D Scene Reconstruction: Efficient NeRF Acceleration**|近年来，神经辐射场（NeRF）已成为一种流行的3D重建方法。虽然它们能产生高质量的结果，但它们也需要漫长的训练时间，通常跨越几天。本文研究了神经修剪作为解决这些问题的策略。我们比较了剪枝方法，包括均匀采样、基于重要性的方法和基于核心集的技术，以减小模型大小并加快训练速度。我们的研究结果表明，核心集驱动的修剪可以使模型大小减少50%，训练速度提高35%，准确性仅略有下降。这些结果表明，修剪可以成为提高资源有限环境中NeRF模型效率的有效方法。 et.al.|[2504.00950](http://arxiv.org/abs/2504.00950)|null|

<p align=right>(<a href=#updated-on-20250406>back to top</a>)</p>

## Diffusion

|Publish Date|Title|Abstract|PDF|Code|
|---|---|---|---|---|
|**2025-04-03**|**Concept Lancet: Image Editing with Compositional Representation Transplant**|扩散模型广泛用于图像编辑任务。现有的编辑方法通常通过在文本嵌入或评分空间中策划编辑方向来设计表示操作过程。然而，这样的程序面临着一个关键挑战：高估编辑强度会损害视觉一致性，而低估编辑强度则会使编辑任务失败。值得注意的是，每个源图像可能需要不同的编辑强度，通过试错法搜索适当的强度成本很高。为了应对这一挑战，我们提出了概念柳叶刀（CoLan），这是一种零样本即插即用框架，用于基于扩散的图像编辑中的原则性表示操作。在推理时，我们将潜在（文本嵌入或扩散分数）空间中的源输入分解为收集到的视觉概念表示的稀疏线性组合。这使我们能够准确地估计每张图像中概念的存在，从而为编辑提供信息。基于编辑任务（替换/添加/删除），我们执行定制的概念移植过程，以施加相应的编辑方向。为了充分模拟概念空间，我们策划了一个概念表示数据集CoLan-150K，其中包含潜在词典的视觉术语和短语的不同描述和场景。在多个基于扩散的图像编辑基线上的实验表明，配备CoLan的方法在编辑效果和一致性保持方面达到了最先进的性能。 et.al.|[2504.02828](http://arxiv.org/abs/2504.02828)|null|
|**2025-04-03**|**F-ViTA: Foundation Model Guided Visible to Thermal Translation**|热成像对于场景理解至关重要，特别是在低光照和夜间条件下。然而，由于红外图像捕获所需的专用设备，收集大型热数据集成本高昂且劳动密集。为了应对这一挑战，研究人员探索了可见光到热图像的转换。大多数现有的方法依赖于生成对抗网络（GAN）或扩散模型（DM），将任务视为风格转换问题。因此，这些方法试图从有限的训练数据中学习模态分布变化和潜在的物理原理。在本文中，我们提出了F-ViTA，这是一种利用基础模型中嵌入的一般世界知识来指导改进翻译的传播过程的新方法。具体而言，我们使用零样本掩模和来自基础模型（如SAM和Grounded DINO）的标签来调节InstructionPix2Pix扩散模型。这使得模型能够学习红外图像中场景对象与其热特征之间有意义的相关性。在五个公共数据集上进行的广泛实验表明，F-ViTA优于最先进的（SOTA）方法。此外，我们的模型可以很好地推广到非分布（OOD）场景，并且可以从同一可见光图像中生成长波红外（LWIR）、中波红外（MWIR）和近红外（NIR）转换。代码：https://github.com/JayParanjape/F-ViTA/tree/master. et.al.|[2504.02801](http://arxiv.org/abs/2504.02801)|null|
|**2025-04-03**|**Unified World Models: Coupling Video and Action Diffusion for Pretraining on Large Robotic Datasets**|模仿学习已成为构建多面手机器人的一种有前景的方法。然而，由于依赖于高质量的专家演示，对大型机器人基础模型进行大规模模仿学习仍然具有挑战性。同时，描绘各种环境和不同行为的大量视频数据很容易获得。这些数据提供了有关真实世界动态和代理环境交互的丰富信息来源。然而，由于缺乏大多数现代方法所需的动作注释，直接利用这些数据进行模仿学习已被证明是困难的。在这项工作中，我们提出了统一世界模型（UWM），这是一个允许利用视频和行动数据进行政策学习的框架。具体来说，UWM在统一的变换器架构中集成了动作扩散过程和视频扩散过程，其中独立的扩散时间步长控制着每种模态。我们证明，通过简单地控制每个扩散时间步长，UWM可以灵活地表示策略、正向动态、反向动态和视频生成器。通过模拟和现实世界的实验，我们表明：（1）UWM能够对具有动力学和动作预测的大规模多任务机器人数据集进行有效的预训练，从而产生比模仿学习更具普遍性和鲁棒性的策略，（2）UWM通过独立控制特定模态的扩散时间步长，自然地促进了从无动作视频数据中的学习，进一步提高了微调策略的性能。我们的研究结果表明，UWM在利用大型异构数据集进行可扩展机器人学习方面迈出了有前景的一步，并在模仿学习和世界建模的经常不同的范式之间实现了简单的统一。视频和代码可在https://weirdlabuw.github.io/uwm/. et.al.|[2504.02792](http://arxiv.org/abs/2504.02792)|null|
|**2025-04-03**|**GPT-ImgEval: A Comprehensive Benchmark for Diagnosing GPT4o in Image Generation**|OpenAI GPT4o模型最近的突破在图像生成和编辑方面表现出了令人惊讶的良好能力，这在社区中引起了极大的兴奋。本技术报告介绍了首个外观评估基准（名为GPT ImgEval），定量和定性地诊断了GPT-4o在三个关键维度上的性能：（1）生成质量，（2）编辑熟练度，以及（3）基于世界知识的语义综合。在所有三项任务中，GPT-4o都表现出了强大的性能，在图像生成控制和输出质量方面大大超越了现有的方法，同时也展示了卓越的知识推理能力。此外，基于GPT-4o生成的数据，我们提出了一种基于分类模型的方法来研究GPT-4o的底层架构，我们的实证结果表明，该模型由自回归（AR）和基于扩散的图像解码头组成，而不是类似VAR的架构。我们还对GPT-4o的整体架构进行了全面的推测。此外，我们进行了一系列分析，以识别和可视化GPT-4o的具体局限性以及在图像生成中常见的合成伪影。我们还对GPT-4o和Gemini 2.0 Flash之间的多轮图像编辑进行了比较研究，并讨论了GPT-4o输出的安全影响，特别是现有图像取证模型的可检测性。我们希望我们的工作能够提供有价值的见解，并提供一个可靠的基准来指导未来的研究，促进可重复性，并加速图像生成及其他领域的创新。用于评估GPT-4o的代码和数据集可以在以下网址找到https://github.com/PicoTrex/GPT-ImgEval. et.al.|[2504.02782](http://arxiv.org/abs/2504.02782)|null|
|**2025-04-03**|**Scene Splatter: Momentum 3D Scene Generation from Single Image with Video Diffusion Model**|在本文中，我们提出了场景飞溅，这是一种基于动量的视频扩散范式，可以从单个图像生成通用场景。现有的方法采用视频生成模型来合成新的视图，但视频长度有限，场景不一致，导致在进一步重建过程中出现伪影和失真。为了解决这个问题，我们从原始特征中构建噪声样本作为动量，以增强视频细节并保持场景一致性。然而，对于具有跨越已知和未知区域的感知场的潜在特征，这种潜在水平动量限制了未知区域中视频扩散的生成能力。因此，我们进一步将上述一致视频作为像素级动量引入到直接生成的无动量视频中，以更好地恢复看不见的区域。我们的级联动量使视频扩散模型能够生成高保真度和一致的新颖视图。我们进一步使用增强帧对全局高斯表示进行微调，并在下一步渲染新帧以进行动量更新。通过这种方式，我们可以迭代地恢复3D场景，避免视频长度的限制。大量实验证明了我们的方法在高保真度和一致性场景生成方面的泛化能力和优越性能。 et.al.|[2504.02764](http://arxiv.org/abs/2504.02764)|null|
|**2025-04-03**|**MD-ProjTex: Texturing 3D Shapes with Multi-Diffusion Projection**|我们介绍了MD ProjTex，这是一种使用预训练的文本到图像扩散模型为3D形状快速一致地生成文本引导纹理的方法。我们方法的核心是UV空间中的多视图一致性机制，它确保了不同视点之间的连贯纹理。具体来说，MD ProjTex在每个扩散步骤融合来自多个视图的噪声预测，并联合更新每个视图的去噪方向，以保持3D一致性。与依赖于优化或顺序视图合成的现有最先进的方法相比，MD-ProjTex在计算上更高效，并获得了更好的定量和定性结果。 et.al.|[2504.02762](http://arxiv.org/abs/2504.02762)|null|
|**2025-04-03**|**RBR4DNN: Requirements-based Testing of Neural Networks**|深度神经网络（DNN）测试对于关键系统的可靠性和安全性至关重要，在这些系统中，故障可能会产生严重后果。尽管已经开发了各种技术来创建健壮性测试套件，但基于需求的DNN测试在很大程度上仍未得到探索，但此类测试被认为是关键系统软件验证的重要组成部分。在这项工作中，我们提出了一种基于需求的测试套件生成方法，该方法使用在语义特征空间中制定的结构化自然语言需求来创建测试套件，通过提示具有需求前提的文本条件潜在扩散模型，然后使用相关的后置条件定义一个测试预言机来判断被测DNN的输出。我们使用预训练生成模型的微调变体来研究这种方法。我们在MNIST、Celebra HQ、ImageNet和自动驾驶汽车数据集上的实验表明，生成的测试套件是真实的、多样化的、符合先决条件的，并且能够揭示故障。 et.al.|[2504.02737](http://arxiv.org/abs/2504.02737)|null|
|**2025-04-03**|**Monitored Fluctuating Hydrodynamics**|我们引入了一个描述受监控的经典随机过程的流体动力学框架。我们研究这些监测过程的条件集成，即我们计算以固定的典型测量记录为条件的时空相关函数。在存在全局对称性的情况下，我们发现这些条件集成可以根据监测速率进行测量诱导的“锐化”相变；此外，即使是微弱的监测也会产生新的关键阶段，这完全是从经典的角度得出的。我们给出了扩散多体量子系统已知电荷锐化跃迁的简单流体动力学推导。我们发现，尽管未受监控的对称和非对称排斥过程处于不同的输运普适性类别中，但它们的条件系综在监控下流向具有涌现相对论不变性的同一不动点。另一方面，具有非阿贝尔对称性的弱监控系统进入了一个新的具有非平凡动力学指数的强耦合不动点，我们对其进行了表征。我们的形式主义自然地考虑了监测一般可观测值，如电流或密度梯度，并允许直接计算锐化跃迁的信息论诊断，包括测量记录的香农熵。 et.al.|[2504.02734](http://arxiv.org/abs/2504.02734)|null|
|**2025-04-03**|**Autonomous Human-Robot Interaction via Operator Imitation**|遥控机器人角色可以依靠操作员的经验和社会直觉与人类进行富有表现力的互动。在这项工作中，我们建议通过训练一个模型来模仿操作员数据，从而创建自主交互式机器人。我们的模型是在人机交互数据集上训练的，其中要求专家操作员改变机器人的交互和情绪，同时记录操作员的命令以及人类和机器人的姿势。我们的方法通过扩散过程学习预测连续的操作员命令，通过分类器学习预测离散的命令，所有这些都统一在一个变压器架构中。我们在仿真中评估了得到的模型，并对真实系统进行了用户研究。我们证明，我们的方法能够实现与专家操作员基线相当的简单自主人机交互，并且用户可以识别我们模型生成的不同机器人情绪。最后，我们演示了将我们的模型零样本转移到具有相同操作员界面的不同机器人平台上。 et.al.|[2504.02724](http://arxiv.org/abs/2504.02724)|null|
|**2025-04-03**|**Phase transitions for interacting particle systems on random graphs**|本文研究随机图上的弱相互作用扩散过程。我们主要关注平均场极限的性质，特别是稳态的非唯一性。通过将经典分叉分析扩展到包括多色相互作用势和随机图结构，我们明确地识别了分叉点，并将其与graphon积分算子的特征值联系起来。此外，我们将得到的McKean-Vlasov偏微分方程表征为相对于适当度量的梯度流。我们将这些理论结果与线性化McKean-Vlasov算子的谱分析和广泛的数值模拟相结合，以深入了解平稳解的稳定性和长期行为。此外，我们提供了强有力的证据，证明（负）相互作用粒子系统的相互作用能是一个自然序参数。特别是，在过渡点之后，对于多色相互作用，我们观察到与系统的动态亚稳态密切相关的能量级联。 et.al.|[2504.02721](http://arxiv.org/abs/2504.02721)|null|

<p align=right>(<a href=#updated-on-20250406>back to top</a>)</p>

## NeRF

|Publish Date|Title|Abstract|PDF|Code|
|---|---|---|---|---|
|**2025-04-03**|**A Physics-Informed Meta-Learning Framework for the Continuous Solution of Parametric PDEs on Arbitrary Geometries**|在这项工作中，我们引入了隐式有限算子学习（iFOL），用于任意几何上偏微分方程（PDE）的连续和参数解。我们提出了一种基于物理信息的编解码器网络，以建立连续参数和解空间之间的映射。解码器通过利用以潜在或特征码为条件的隐式神经场网络来构建参数解场。实例特定代码是通过基于二阶元学习技术的PDE编码过程导出的。在训练和推理中，在PDE编码和解码过程中，物理信息损失函数被最小化。iFOL以能量或加权残差形式表示损失函数，并使用从标准数值PDE方法导出的离散残差对其进行评估。这种方法在训练和推理过程中都会导致离散残差的反向传播。iFOL具有几个关键特性：（1）其独特的损失公式消除了以前在PDE的条件神经场算子学习中使用的传统编码过程-解码流水线的需要；（2） 它不仅提供精确的参数和连续场，而且提供参数梯度的解，而不需要额外的损失项或灵敏度分析；（3） 它可以有效地捕捉溶液中的尖锐不连续性；（4）它消除了对几何和网格的约束，使其适用于任意几何和空间采样（零样本超分辨率能力）。我们批判性地评估了这些特征，并分析了网络在稳态和瞬态PDE中推广到看不见的样本的能力。所提出的方法的整体性能是有希望的，证明了它适用于计算力学中一系列具有挑战性的问题。 et.al.|[2504.02459](http://arxiv.org/abs/2504.02459)|null|
|**2025-04-01**|**Flow Matching on Lie Groups**|流匹配（FM）是一种最新的生成建模技术：我们的目标是学习如何从分布中采样{X}_1 $通过从某些分布中流动样本$\mathfrak{X}_0$很容易取样。关键技巧是，在$\mathfrak中对端点进行调节的同时，可以训练这个流场{X}_1$：给定终点，只需沿直线段移动到终点（Lipman等人，2022）。然而，直线段仅在欧几里德空间上定义良好。因此，Chen和Lipman（2023）将该方法推广到黎曼流形上的FM，用测地线或其谱近似代替线段。我们采取了另一种观点：我们通过用指数曲线代替线段来推广李群上的FM。这导致了许多矩阵李群的简单、内在和快速实现，因为所需的李群运算（积、逆、指数、对数）仅由相应的矩阵运算给出。然后，李群上的FM可用于生成建模，数据由特征集（在$\mathbb{R}^n$ 中）和姿势集（在某些李群中）组成，例如等变神经场的潜在码（Wessels等人，2025）。 et.al.|[2504.00494](http://arxiv.org/abs/2504.00494)|**[link](https://github.com/finnsherry/FlowMatching)**|
|**2025-03-29**|**NeuralGS: Bridging Neural Fields and 3D Gaussian Splatting for Compact 3D Representations**|3D高斯散点（3DGS）显示了卓越的质量和渲染速度，但有数百万的3D高斯分布和巨大的存储和传输成本。最近的3DGS压缩方法主要集中在压缩脚手架GS上，取得了令人印象深刻的性能，但增加了体素结构和复杂的编码和量化策略。在这篇论文中，我们的目标是开发一种简单而有效的方法，称为NeuralGS，它以另一种方式探索将原始3DGS压缩成紧凑的表示，而不需要体素结构和复杂的量化策略。我们的观察是，像NeRF这样的神经场可以用多层感知器（MLP）神经网络表示复杂的3D场景，只需要几兆字节。因此，NeuralGS有效地采用神经场表示来用MLP对3D高斯的属性进行编码，即使对于大规模场景，也只需要很小的存储空间。为了实现这一点，我们采用了一种聚类策略，并根据高斯的重要性得分作为拟合权重，为每个聚类用不同的微小MLP对高斯进行拟合。我们在多个数据集上进行实验，在不损害视觉质量的情况下实现了平均模型大小减少45倍。我们的方法在原始3DGS上的压缩性能与基于Scaffold GS的专用压缩方法相当，这表明了用神经场直接压缩原始3DGS的巨大潜力。 et.al.|[2503.23162](http://arxiv.org/abs/2503.23162)|null|
|**2025-03-27**|**Renormalization group analysis of noisy neural field**|大脑中的神经元在个体特性和与其他神经元的连接方面表现出极大的多样性。为了深入了解神经元多样性如何在大尺度上促进大脑动力学和功能，我们借鉴了复制方法的框架，该框架已成功应用于平衡统计力学中一大类具有淬灭噪声的问题。我们分析了Wilson Cowan模型的两个线性化版本，其随机系数在空间上是相关的。特别是：（A）神经元本身的性质是异质的，（B）它们的连接是各向异性的。在这两个模型中，淬火随机性的平均会产生额外的非线性。这些非线性在威尔逊重整化群的框架内进行了分析。我们发现，对于模型A，如果噪声的空间相关性随距离衰减，指数小于-2 $，则在大的空间尺度上，噪声的影响消失了。相比之下，对于模型B，只有当空间相关性以小于-1$ 的指数衰减时，噪声对神经元连接的影响才会消失。我们的计算还表明，在某些条件下，噪声的存在可能会在大尺度上产生类似行波的行为，尽管这一结果在微扰理论的高阶下是否仍然有效还有待观察。 et.al.|[2503.21605](http://arxiv.org/abs/2503.21605)|null|
|**2025-03-25**|**Thin-Shell-SfT: Fine-Grained Monocular Non-rigid 3D Surface Tracking with Neural Deformation Fields**|从单目RGB视频中重建高度可变形的表面（如布料）是一个具有挑战性的问题，没有任何解决方案可以提供一致和准确的细粒度表面细节恢复。为了解释环境的病态性，现有的方法使用具有统计、神经或物理先验的变形模型。它们还主要依赖于非自适应离散曲面表示（例如多边形网格），逐帧优化导致误差传播，并受到基于网格的可微渲染器梯度差的影响。因此，织物褶皱等精细表面细节往往无法以所需的精度恢复。针对这些局限性，我们提出了ThinShell SfT，这是一种用于非刚性3D跟踪的新方法，将表面表示为隐式和连续的时空神经场。我们采用基于基尔霍夫-洛夫模型的连续薄壳物理先验进行空间正则化，这与早期作品的离散化替代方案形成了鲜明对比。最后，我们利用3D高斯溅射将表面可微分地渲染到图像空间中，并根据合成原理分析优化变形。我们的薄壳SfT在定性和定量上都优于先前的工作，这要归功于我们的连续表面公式以及专门定制的模拟先验和表面诱导的3D高斯。请访问我们的项目页面https://4dqv.mpiinf.mpg.de/ThinShellSfT. et.al.|[2503.19976](http://arxiv.org/abs/2503.19976)|null|
|**2025-03-25**|**Decoupled Dynamics Framework with Neural Fields for 3D Spatio-temporal Prediction of Vehicle Collisions**|本研究提出了一种神经框架，通过独立建模全局刚体运动和局部结构变形来预测3D车辆碰撞动力学。与直接预测绝对位移的方法不同，这种方法明确地将车辆的整体平移和旋转与其结构变形分开。两个专门的网络构成了该框架的核心：一个基于四元数的刚性网络用于刚性运动，一个基于坐标的变形网络用于局部变形。通过独立处理根本不同的物理现象，所提出的架构实现了准确的预测，而不需要对每个组件进行单独的监督。该模型仅在10%的可用模拟数据上进行训练，其性能明显优于基线模型，包括单层感知器（MLP）和深度算子网络（DeepONet），预测误差降低了83%。广泛的验证表明，它对训练范围外的碰撞条件具有很强的泛化能力，即使在涉及极端速度和大冲击角度的严重冲击下，也能准确预测响应。此外，该框架成功地从低分辨率输入重建了高分辨率变形细节，而无需增加计算工作量。因此，所提出的方法为在复杂的碰撞场景中快速可靠地评估车辆安全提供了一种有效、计算高效的方法，大大减少了所需的模拟数据和时间，同时保持了预测的保真度。 et.al.|[2503.19712](http://arxiv.org/abs/2503.19712)|null|
|**2025-03-21**|**Towards Understanding the Benefits of Neural Network Parameterizations in Geophysical Inversions: A Study With Neural Fields**|在这项工作中，我们采用了神经场，它使用神经网络以测试时学习的方式将坐标映射到该坐标处的相应物理属性值。对于测试时学习方法，与需要使用训练数据集训练网络的传统方法相比，在反演过程中学习权重。首先展示了地震层析成像和直流电阻率反演中的合成示例结果。然后，我们对这两种情况下的神经网络权重的雅可比矩阵进行奇异值分解分析（SVD分析），以探索神经网络对恢复模型的影响。结果表明，测试时间学习方法可以消除恢复的地下物理性质模型中由测量和物理敏感性引起的不必要的伪影。因此，在某些情况下，与常规反演相比，NFs-Inv可以改善反演结果，例如恢复倾角或预测主要目标的边界。在SVD分析中，我们观察到左奇异向量中的相似模式，就像在计算机视觉中的生成任务中以监督方式训练的一些扩散模型中观察到的那样。这一观察结果提供了证据，表明神经网络结构中固有的隐式偏差在监督学习和测试时学习模型中很有用。这种隐式偏差有可能对地球物理反演中的模型恢复有用。 et.al.|[2503.17503](http://arxiv.org/abs/2503.17503)|null|
|**2025-03-19**|**GO-N3RDet: Geometry Optimized NeRF-enhanced 3D Object Detector**|我们提出了GO-N3RDet，这是一种通过神经辐射场增强的场景几何优化的多视图3D物体检测器。准确的3D对象检测的关键在于有效的体素表示。然而，由于遮挡和缺乏3D信息，从多视图2D图像构建3D特征具有挑战性。为了解决这个问题，我们引入了一种独特的3D位置信息嵌入体素优化机制来融合多视图特征。为了优先考虑目标区域的神经场重建，我们还为探测器的NeRF分支设计了一种双重重要性采样方案。我们还提出了一个不透明度优化模块，通过实施多视图一致性约束来进行精确的体素不透明度预测。此外，为了进一步提高跨多个视角的体素密度一致性，我们将射线距离作为加权因子，以最小化累积射线误差。我们独特的模块协同形成了一个端到端的神经模型，建立了基于NeRF的多视图3D检测的最新技术，并在ScanNet和ARKITCenes上进行了广泛的实验验证。代码将在以下网址提供https://github.com/ZechuanLi/GO-N3RDet. et.al.|[2503.15211](http://arxiv.org/abs/2503.15211)|null|
|**2025-03-14**|**NF-SLAM: Effective, Normalizing Flow-supported Neural Field representations for object-level visual SLAM in automotive applications**|我们提出了一种新颖的、仅限视觉的对象级SLAM框架，用于通过隐式符号距离函数表示3D形状的汽车应用。我们的主要创新包括通过归一化流网络增强标准神经表示。因此，通过仅具有16维潜码的紧凑网络，可以在特定类别的道路车辆上实现强大的表示能力。此外，通过对合成数据的比较实验证明，新提出的架构在仅存在稀疏和噪声数据的情况下表现出显著的性能改进。该模块嵌入到基于立体视觉的框架的后端，用于联合增量形状优化。损失函数由基于稀疏3D点的SDF损失、稀疏渲染损失和基于语义掩码的轮廓一致性项的组合给出。我们还利用语义信息来确定前端的关键点提取密度。最后，对真实世界数据的实验结果显示，与使用直接深度读数的替代框架相比，其性能准确可靠。所提出的方法仅在通过束调整获得的稀疏3D点上表现良好，即使在仅使用掩模一致性项的情况下，最终也能继续提供稳定的结果。 et.al.|[2503.11199](http://arxiv.org/abs/2503.11199)|null|
|**2025-03-13**|**RSR-NF: Neural Field Regularization by Static Restoration Priors for Dynamic Imaging**|动态成像涉及使用欠采样测量值随时重建时空对象。特别是，在动态计算机断层扫描（dCT）中，一次只能获得一个视角的单个投影，这使得逆问题非常具有挑战性。此外，地面实况动态数据通常要么不可用，要么太稀缺，无法用于监督学习技术。为了解决这个问题，我们提出了RSR-NF，它使用神经场（NF）来表示动态对象，并使用去噪正则化（RED）框架，通过学习的恢复算子将额外的静态深空间先验合并到变分公式中。我们使用基于ADMM的可变分裂算法来有效地优化变分目标。我们将RSR-NF与三种替代方案进行了比较：仅具有时间正则化的NF；最近的一种方法，使用对静态数据进行预训练的去噪器，将部分可分离的低秩表示与RED相结合；以及基于深度图像先验的模型。第一个比较展示了通过将NF表示与静态恢复先验相结合所实现的重建改进，而另外两个则展示了与dCT的最新技术相比的改进。 et.al.|[2503.10015](http://arxiv.org/abs/2503.10015)|null|

<p align=right>(<a href=#updated-on-20250406>back to top</a>)</p>

[contributors-shield]: https://img.shields.io/github/contributors/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[contributors-url]: https://github.com/Vincentqyw/cv-arxiv-daily/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[forks-url]: https://github.com/Vincentqyw/cv-arxiv-daily/network/members
[stars-shield]: https://img.shields.io/github/stars/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[stars-url]: https://github.com/Vincentqyw/cv-arxiv-daily/stargazers
[issues-shield]: https://img.shields.io/github/issues/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[issues-url]: https://github.com/Vincentqyw/cv-arxiv-daily/issues

