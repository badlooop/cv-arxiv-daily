[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]

## Updated on 2025.03.04
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
|**2025-02-28**|**Raccoon: Multi-stage Diffusion Training with Coarse-to-Fine Curating Videos**|随着扩散模型的出现，文本到视频的生成已经显示出有希望的进展，但现有的方法受到数据集质量和计算资源的限制。为了解决这些局限性，本文提出了一种全面的方法，该方法同时推进了数据管理和模型设计。我们介绍了CFC-VIDS-1M，这是一个通过系统的粗到细管理管道构建的高质量视频数据集。该管道首先在多个维度上评估视频质量，然后是一个细粒度阶段，该阶段利用视觉语言模型来增强文本视频对齐和语义丰富性。基于精心策划的数据集对视觉质量和时间连贯性的强调，我们开发了RACCOON，这是一种基于转换器的架构，具有解耦的时空注意力机制。该模型通过渐进的四阶段策略进行训练，旨在有效地处理视频生成的复杂性。大量实验表明，我们的高质量数据管理和高效训练策略的集成方法在保持计算效率的同时，生成了具有视觉吸引力和时间连贯性的视频。我们将发布我们的数据集、代码和模型。 et.al.|[2502.21314](http://arxiv.org/abs/2502.21314)|null|
|**2025-02-28**|**Training-free and Adaptive Sparse Attention for Efficient Long Video Generation**|使用扩散变换器（DiTs）生成高保真长视频通常会受到显著延迟的阻碍，主要是由于注意力机制的计算需求。例如，使用HunyuanVideo生成一个8秒的720p视频（11万个代币）大约需要600个PFLOP，其中注意力计算消耗了大约500个PFLOPs。为了解决这个问题，我们提出了AdaSpa，这是第一种动态模式和在线精确搜索稀疏注意力方法。首先，为了实现动态模式，我们引入了一种块化模式来有效地捕获DiTs中固有的分层稀疏性。这是基于我们的观察，即DiTs的稀疏特征在不同模态之间和内部表现出分层和块化结构。这种块化方法显著降低了注意力计算的复杂性，同时保持了生成视频的高保真度。其次，为了实现在线精确搜索，我们提出了具有头部自适应分层块稀疏注意的融合LSE缓存搜索。该方法的动机是我们发现DiTs的稀疏模式和LSE随输入、层和头部而变化，但在去噪步骤中保持不变。通过在去噪步骤中利用这种不变性，它适应了DiT的动态特性，并允许以最小的开销精确、实时地识别稀疏索引。AdaSpa是一种自适应的即插即用解决方案，可以与现有的DiT无缝集成，既不需要额外的微调，也不需要依赖数据集的分析。大量实验证实，AdaSpa在保持视频质量的同时，在各种模型上提供了显著的加速，使其成为一种强大且可扩展的高效视频生成方法。 et.al.|[2502.21079](http://arxiv.org/abs/2502.21079)|null|
|**2025-02-28**|**HAIC: Improving Human Action Understanding and Generation with Better Captions for Multi-modal Large Language Models**|最近的多模态大语言模型（MLLM）在视频理解方面取得了很大进展。然而，由于缺乏高质量的数据，它们在涉及人类行为的视频上的表现仍然有限。为了解决这个问题，我们引入了一个两阶段数据注释管道。首先，我们设计策略，从互联网上收集具有清晰人类行为的视频。其次，视频以标准化的字幕格式进行注释，该格式使用人类属性来区分个人，并按时间顺序详细说明他们的行为和互动。通过这个管道，我们策划了两个数据集，即HAICTrain和HAICBench。\textbf{HAICTrain}由Gemini Pro生成的126K个视频字幕对组成，并经过验证用于训练目的。同时，\textbf{HAICBench}包括500个手动注释的视频字幕对和1400个QA对，用于全面评估人类行为理解。实验结果表明，使用HAICTrain进行训练不仅可以显著提高人类在4个基准测试中的理解能力，还可以改善文本到视频的生成结果。HAICTrain和HAICBench均于https://huggingface.co/datasets/KuaishouHAIC/HAIC. et.al.|[2502.20811](http://arxiv.org/abs/2502.20811)|null|
|**2025-02-28**|**WorldModelBench: Judging Video Generation Models As World Models**|视频生成模型发展迅速，将自己定位为能够支持机器人和自动驾驶等决策应用的视频世界模型。然而，目前的基准测试未能严格评估这些说法，只关注一般的视频质量，忽视了世界模型的重要因素，如物理依从性。为了弥合这一差距，我们提出了WorldModelBench，这是一个基准测试，旨在评估应用程序驱动领域中视频生成模型的世界建模能力。WorldModelBench提供了两个关键优势：（1）针对细微的世界建模违规：通过结合指令遵循和物理遵守维度，WorldModelBench可以检测到微妙的违规行为，例如违反质量守恒定律的物体大小的不规则变化——这些问题被之前的基准所忽视。（2） 与大规模人类偏好相一致：我们众包了6700个人类标签，以准确测量14个前沿模型。使用我们高质量的人类标签，我们进一步微调了一个准确的判断器，使评估过程自动化，在预测世界建模违规方面的平均准确率比2B参数的GPT-4o高8.6%。此外，我们证明，通过最大化评判者的奖励来对齐人类注释的训练显著提高了世界建模能力。该网站可在https://worldmodelbench-team.github.io. et.al.|[2502.20694](http://arxiv.org/abs/2502.20694)|null|
|**2025-02-27**|**Mobius: Text to Seamless Looping Video Generation via Latent Shift**|我们提出了Mobius，这是一种直接从文本描述生成无缝循环视频的新方法，无需任何用户注释，从而为多媒体演示创建新的视觉材料。我们的方法重新利用预训练的视频潜在扩散模型，在没有任何训练的情况下从文本提示生成循环视频。在推理过程中，我们首先通过连接视频的开始和结束噪声来构建一个潜在循环。考虑到视频扩散模型的上下文可以保持时间一致性，我们通过在每一步中将第一帧潜在帧逐渐移动到末尾来执行多帧潜在去噪。因此，去噪上下文在每个步骤中都有所不同，同时在整个推理过程中保持一致性。此外，我们方法中的潜在循环可以是任何长度。这扩展了我们潜在的移位方法，以生成超出视频扩散模型上下文范围的无缝循环视频。与之前的电影图像不同，所提出的方法不需要图像作为外观，这将限制生成结果的运动。相反，我们的方法可以产生更动态的运动和更好的视觉质量。我们进行了多次实验和比较，以验证所提出方法的有效性，证明其在不同场景下的有效性。所有代码都将可用。 et.al.|[2502.20307](http://arxiv.org/abs/2502.20307)|**[link](https://github.com/yisuitt/mobius)**|
|**2025-02-27**|**FlexiDiT: Your Diffusion Transformer Can Easily Generate High-Quality Samples with Less Compute**|尽管其性能卓越，但现代扩散变换器在推理过程中受到大量资源需求的阻碍，这些资源需求源于每个去噪步骤所需的固定和大量计算。在这项工作中，我们重新审视了为每次去噪迭代分配固定计算预算的传统静态范式，并提出了一种动态策略。我们简单且高效的示例框架使预训练的DiT模型能够转换为被称为FlexiDiT的灵活模型，使其能够以不同的计算预算处理输入。我们演示了单个\emph｛flexible｝模型如何在不降低质量的情况下生成图像，同时与静态模型相比，在类条件和文本条件的图像生成中，将所需的FLOP降低了40%以上。我们的方法是通用的，对输入和条件模式不可知。我们展示了如何将我们的方法轻松扩展到视频生成，其中FlexiDiT模型生成的样本在不影响性能的情况下，计算成本降低了75%。 et.al.|[2502.20126](http://arxiv.org/abs/2502.20126)|null|
|**2025-02-27**|**High-Fidelity Relightable Monocular Portrait Animation with Lighting-Controllable Video Diffusion Model**|可靠的肖像动画旨在为静态参考肖像制作动画，以匹配驾驶视频的头部运动和表情，同时适应用户指定或参考的照明条件。现有的肖像动画方法无法实现可重现的肖像，因为它们没有分离和操纵内在（身份和外观）和外在（姿势和照明）特征。本文提出了一种用于高保真、可重现肖像动画的照明可控视频扩散模型（LCVD）。我们通过在预训练图像到视频扩散模型的特征空间内通过专用子空间区分这些特征类型来解决这一局限性。具体来说，我们使用肖像的3D网格、姿势和照明渲染着色提示来表示外部属性，而引用表示内部属性。在训练阶段，我们使用参考适配器将参考映射到内在特征子空间，并使用着色适配器将着色提示映射到外在特征子空间。通过合并这些子空间的特征，该模型实现了对生成动画中的照明、姿势和表情的精细控制。广泛的评估表明，LCVD在照明逼真度、图像质量和视频一致性方面优于最先进的方法，为可重现的肖像动画树立了新的基准。 et.al.|[2502.19894](http://arxiv.org/abs/2502.19894)|**[link](https://github.com/MingtaoGuo/relightable-portrait-animation)**|
|**2025-02-27**|**C-Drag: Chain-of-Thought Driven Motion Controller for Video Generation**|基于轨迹的运动控制已经成为一种直观有效的可控视频生成方法。然而，现有的基于轨迹的方法通常仅限于生成受控对象的运动轨迹，而忽略受控对象与其周围环境之间的动态相互作用。为了解决这一局限性，我们提出了一种名为C-Drag的基于思维链的运动控制器，用于可控视频生成。我们的C-Drag不是直接生成某些对象的运动，而是首先执行对象感知，然后根据对象的给定运动控制来推断不同对象之间的动态交互。具体来说，我们的方法包括一个对象感知模块和一个基于思维链的运动推理模块。对象感知模块采用视觉语言模型来捕捉图像中各种对象的位置和类别信息。基于思维链的运动推理模块将此信息作为输入，并进行分阶段的推理过程，为每个受影响的对象生成运动轨迹，随后将其馈送到扩散模型进行视频合成。此外，我们引入了一种新的视频对象交互（VOI）数据集来评估运动控制视频生成方法的生成质量。我们的VOI数据集包含三种典型的交互类型，并提供了可用于准确性能评估的物体运动轨迹。实验结果表明，C-Drag在多个指标上表现良好，在对象运动控制方面表现出色。我们的基准、代码和模型将在https://github.com/WesLee88524/C-Drag-Official-Repo. et.al.|[2502.19868](http://arxiv.org/abs/2502.19868)|**[link](https://github.com/weslee88524/c-drag-official-repo)**|
|**2025-02-26**|**FLAP: Fully-controllable Audio-driven Portrait Video Generation through 3D head conditioned diffusion mode**|基于扩散的视频生成技术显著改进了零样本会说话的头部化身生成，增强了头部运动和面部表情的自然度。然而，现有的方法可控性较差，使其不太适用于现实世界的场景，如电影制作和电子商务直播。为了解决这一局限性，我们提出了FLAP，这是一种将显式3D中间参数（头部姿势和面部表情）集成到扩散模型中的新方法，用于端到端生成逼真的肖像视频。所提出的架构允许该模型从音频中生成生动的肖像视频，同时结合额外的控制信号，如头部旋转角度和眨眼频率。此外，头部姿势和面部表情的解耦允许对每一个进行独立控制，从而提供对化身姿势和面部面部表情的精确操纵。我们还展示了它在与现有的3D头部生成方法集成方面的灵活性，弥合了基于3D模型的方法和端到端扩散技术之间的差距。大量实验表明，我们的方法在自然度和可控性方面都优于最近的音频驱动肖像视频模型。 et.al.|[2502.19455](http://arxiv.org/abs/2502.19455)|null|
|**2025-03-03**|**TransVDM: Motion-Constrained Video Diffusion Model for Transparent Video Synthesis**|视频扩散模型（VDM）的最新发展已经证明了其生成高质量视频内容的显著能力。尽管如此，VDM创建透明视频的潜力在很大程度上仍然未知。本文介绍了TransVDM，这是第一个专门为透明视频生成设计的基于扩散的模型。TransVDM集成了透明变分自编码器（TVAE）和基于预训练UNet的VDM，以及一种新型的阿尔法运动约束模块（AMCM）。TVAE捕获视频帧的阿尔法通道透明度，并将其编码到VDM的潜在空间中，从而促进向透明视频扩散模型的无缝过渡。为了改善透明区域的检测，AMCM在VDM中集成了前景的运动约束，有助于减少不希望的伪影。此外，我们策划了一个包含250K个透明帧的数据集进行训练。实验结果证明了我们的方法在各种基准测试中的有效性。 et.al.|[2502.19454](http://arxiv.org/abs/2502.19454)|null|

<p align=right>(<a href=#updated-on-20250304>back to top</a>)</p>

## 3D

|Publish Date|Title|Abstract|PDF|Code|
|---|---|---|---|---|
|**2025-02-28**|**EndoPBR: Material and Lighting Estimation for Photorealistic Surgical Simulations via Physically-based Rendering**|手术场景的3D视觉中缺乏标记数据集，这阻碍了医学领域稳健的3D重建算法的发展。尽管神经辐射场和3D高斯散斑在一般计算机视觉领域很受欢迎，但由于非平稳照明和非朗伯表面等挑战，这些系统在手术场景中尚未取得一致的成功。因此，对标记手术数据集的需求继续增长。在这项工作中，我们引入了一种可微分渲染框架，用于从内窥镜图像和已知几何形状中估计材料和光照。与之前将光照和材质联合建模为辐射的方法相比，我们明确地解开了这些场景属性，以实现鲁棒和逼真的新颖视图合成。为了消除训练过程的歧义，我们制定了手术场景中固有的领域特定属性。具体来说，我们将场景照明建模为简单的聚光灯，将材质属性建模为双向反射分布函数，由神经网络参数化。通过在渲染方程中进行颜色预测，我们可以在任意相机姿态下生成逼真的图像。我们使用结肠镜3D视频数据集中的各种序列评估了我们的方法，并表明与其他方法相比，我们的方法产生了具有竞争力的新颖视图合成结果。此外，我们证明，通过使用我们的渲染输出微调深度估计模型，合成数据可用于开发3D视觉算法。总体而言，我们看到深度估计性能与原始真实图像的微调相当。 et.al.|[2502.20669](http://arxiv.org/abs/2502.20669)|null|
|**2025-02-27**|**No Parameters, No Problem: 3D Gaussian Splatting without Camera Intrinsics and Extrinsics**|虽然3D高斯散斑（3DGS）在场景重建和新颖的视图合成方面取得了重大进展，但它仍然严重依赖于精确预先计算的相机内部和外部，如焦距和相机姿态。为了减轻这种依赖性，之前的工作主要集中在优化3DGS而不需要相机姿态，但相机内部函数仍然是必要的。为了进一步放宽要求，我们提出了一种联合优化方法，从图像集合中训练3DGS，而不需要相机内部或外部。为了实现这一目标，我们在3DGS的联合训练中介绍了几个关键改进。我们从理论上推导出相机内部函数的梯度，从而在训练过程中同时优化相机内部函数。此外，我们整合全局轨迹信息并选择与每个轨迹相关的高斯核，这些核将被训练并自动重新缩放到无穷小的大小，接近表面点，并专注于加强多视图一致性和最小化重投影误差，而其余的核将继续发挥其原始作用。这种混合训练策略很好地将相机参数估计和3DGS训练结合起来。广泛的评估表明，所提出的方法在公共和合成数据集上都达到了最先进的（SOTA）性能。 et.al.|[2502.19800](http://arxiv.org/abs/2502.19800)|null|
|**2025-02-26**|**Does 3D Gaussian Splatting Need Accurate Volumetric Rendering?**|自引入以来，3D高斯散斑（3DGS）已成为学习捕获场景的3D表示的重要参考方法，允许实时进行具有高视觉质量和快速训练时间的新颖视图合成。在3DGS之前的神经辐射场（NeRF）基于用于体绘制的原则性光线行进方法。相比之下，虽然与NeRF共享类似的图像形成模型，但3DGS使用了一种基于体绘制和原始光栅化优势的混合渲染解决方案。3DGS的一个关键优势是它的性能，在许多情况下，它是通过一组近似值实现的，与体积渲染理论有关。一个自然产生的问题是，用更有原则的体积渲染解决方案替换这些近似值是否可以提高3DGS的质量。在本文中，我们对原始3DGS解决方案使用的各种近似值和假设进行了深入分析。我们证明，虽然更精确的体积渲染可以帮助减少基元数量，但高效优化和大量高斯分布的强大功能使3DGS在近似值下仍能超越体积渲染。 et.al.|[2502.19318](http://arxiv.org/abs/2502.19318)|**[link](https://github.com/cg-tuwien/does_3d_gaussian_splatting_need_accurate_volumetric_rendering)**|
|**2025-02-25**|**Synthesizing Consistent Novel Views via 3D Epipolar Attention without Re-Training**|大型扩散模型在单个图像的新颖视图合成中表现出显著的零样本能力。然而，这些模型在保持新颖和参考视图之间的一致性方面经常面临挑战。导致这一问题的一个关键因素是参考视图中上下文信息的利用有限。具体来说，当两个视图之间的视锥中存在重叠时，必须确保相应的区域在几何形状和外观上保持一致性。这一观察结果导致了一种简单而有效的方法，我们建议使用极线几何来定位和检索输入视图中的重叠信息。然后，这些信息被纳入目标视图的生成中，从而消除了训练或微调的需要，因为该过程不需要可学习的参数。此外，为了增强生成视图的整体一致性，我们将极线注意力的利用扩展到多视图设置，允许从输入视图和其他目标视图中检索重叠信息。定性和定量实验结果表明，我们的方法在不需要任何微调的情况下显著提高了合成视图的一致性。此外，这种增强还提高了3D重建等下游应用的性能。该代码可在以下网址获得https://github.com/botaoye/ConsisSyn. et.al.|[2502.18219](http://arxiv.org/abs/2502.18219)|null|
|**2025-02-23**|**Efficient 4D Gaussian Stream with Low Rank Adaptation**|最近的方法在合成具有长视频序列的新视图方面取得了重大进展。本文提出了一种高度可扩展的连续学习动态新视图合成方法。我们利用3D高斯分布来表示场景，并利用基于低阶自适应的变形模型来捕捉动态场景变化。我们的方法使用视频帧块连续重建动态，将流带宽减少了90%，同时保持了与离线SOTA方法相当的高渲染质量。 et.al.|[2502.16575](http://arxiv.org/abs/2502.16575)|null|
|**2025-02-24**|**Para-Lane: Multi-Lane Dataset Registering Parallel Scans for Benchmarking Novel View Synthesis**|为了评估端到端的自动驾驶系统，基于新型视图合成（NVS）技术的仿真环境至关重要，该环境在新的车辆姿态下，特别是在交叉车道场景下，从之前记录的序列中合成逼真的图像和点云。因此，开发多通道数据集和基准是必要的。虽然最近基于合成场景的NVS数据集已经为跨车道基准测试做好了准备，但它们仍然缺乏捕获图像和点云的真实感。为了进一步评估基于NeRF和3DGS的现有方法的性能，我们提出了第一个多车道数据集，该数据集专门用于记录从真实世界扫描中导出的新型驾驶视图合成数据集的并行扫描，包括25组相关序列，包括16000个正视图图像、64000个环绕视图图像和16000个激光雷达帧。所有帧都进行了标记，以区分移动对象和静态元素。使用此数据集，我们评估了现有方法在不同车道和距离的各种测试场景中的性能。此外，我们的方法为解决和评估多传感器姿态的质量提供了解决方案，用于多模态数据对齐，以便在现实世界中管理这样的数据集。我们计划不断添加新的序列，以测试现有方法在不同场景中的泛化能力。数据集在项目页面上公开发布：https://nizqleo.github.io/paralane-dataset/. et.al.|[2502.15635](http://arxiv.org/abs/2502.15635)|null|
|**2025-02-21**|**RGB-Only Gaussian Splatting SLAM for Unbounded Outdoor Scenes**|3D高斯散斑（3DGS）已成为SLAM中一种流行的解决方案，因为它可以产生高保真的新颖视图。然而，之前基于GS的方法主要针对室内场景，依赖于RGB-D传感器或预训练的深度估计模型，因此在室外场景中表现不佳。为了解决这个问题，我们提出了一种用于无界户外场景的仅RGB高斯飞溅SLAM方法——OpenGS SLAM。从技术上讲，我们首先使用点图回归网络在帧之间生成一致的点图，用于姿态估计。与常用的深度图相比，点图包括跨多个视图的空间关系和场景几何形状，从而实现了稳健的相机姿态估计。然后，我们提出将估计的相机姿态与3DGS渲染集成为端到端的可微分流水线。我们的方法实现了相机姿态和3DGS场景参数的同时优化，显著提高了系统跟踪精度。具体来说，我们还为点图回归网络设计了一个自适应比例映射器，它为3DGS图表示提供了更精确的点图映射。我们在Waymo数据集上的实验表明，OpenGS SLAM将跟踪误差降低到之前3DGS方法的9.8%，并在新的视图合成中取得了最先进的结果。项目页面：https://3dagentworld.github.io/opengs-slam/ et.al.|[2502.15633](http://arxiv.org/abs/2502.15633)|null|
|**2025-02-20**|**RendBEV: Semantic Novel View Synthesis for Self-Supervised Bird's Eye View Segmentation**|鸟瞰图（BEV）语义图作为解决辅助和自动驾驶任务的有用环境表示，最近引起了人们的广泛关注。然而，现有的大部分工作都集中在完全监督的环境中，在大型带注释的数据集上训练网络。在这项工作中，我们提出了RendBEV，这是一种用于BEV语义分割网络自监督训练的新方法，利用可微分体绘制来接收由2D语义分割模型计算的语义透视图的监督。我们的方法能够实现零样本BEV语义分割，并且已经在这种具有挑战性的环境中提供了具有竞争力的结果。当用作预训练，然后对标记的BEV地面真实值进行微调时，我们的方法显著提高了低注释状态下的性能，并在对所有可用标签进行微调时达到了新的水平。 et.al.|[2502.14792](http://arxiv.org/abs/2502.14792)|null|
|**2025-02-20**|**CDGS: Confidence-Aware Depth Regularization for 3D Gaussian Splatting**|3D高斯散斑（3DGS）在新颖的视图合成（NVS）中显示出显著的优势，特别是在实现高渲染速度和高质量结果方面。然而，由于在优化过程中缺乏明确的几何约束，其在3D重建中的几何精度仍然有限。本文介绍了CDGS，这是一种为增强3DGS而开发的具有置信度的深度正则化方法。我们利用单目深度估计的多线索置信图和运动深度稀疏结构，在优化过程中自适应地调整深度监控。我们的方法在早期训练阶段证明了改进的几何细节保存，并在NVS质量和几何精度方面取得了具有竞争力的性能。在公开的Tanks和Temples基准数据集上的实验表明，我们的方法实现了更稳定的收敛行为和更准确的几何重建结果，NVS的PSNR提高了2.31 dB，M3C2距离度量的几何误差也持续降低。值得注意的是，我们的方法仅用50%的训练迭代就达到了与原始3DGS相当的F分数。我们预计这项工作将有助于为数字孪生创建、遗产保护或林业应用等现实世界应用开发高效准确的3D重建系统。 et.al.|[2502.14684](http://arxiv.org/abs/2502.14684)|**[link](https://github.com/zqlin0521/cdgs-release)**|
|**2025-02-20**|**Exploiting Deblurring Networks for Radiance Fields**|在本文中，我们提出了DeepDeblurRF，这是一种新的辐射场去模糊方法，可以从模糊的训练视图中合成高质量的新视图，大大缩短训练时间。DeepDeblurRF利用基于深度神经网络（DNN）的去模糊模块来享受其去模糊性能和计算效率。为了有效地结合基于DNN的去模糊和辐射场构造，我们提出了一种新的辐射场（RF）引导的去模糊方法和一种迭代框架，该框架以交替的方式执行RF引导的去雾和辐射场构建。此外，DeepDeblurRF与各种场景表示兼容，如体素网格和3D高斯分布，从而扩展了其适用性。我们还介绍了BlurRF Synth，这是第一个用于训练辐射场去模糊框架的大规模合成数据集。我们对相机运动模糊和散焦模糊进行了广泛的实验，证明DeepDeblurRF在显著减少训练时间的情况下实现了最先进的新颖视图合成质量。 et.al.|[2502.14454](http://arxiv.org/abs/2502.14454)|null|

<p align=right>(<a href=#updated-on-20250304>back to top</a>)</p>

## 3D Reconstruction

|Publish Date|Title|Abstract|PDF|Code|
|---|---|---|---|---|
|**2025-02-28**|**MESC-3D:Mining Effective Semantic Cues for 3D Reconstruction from a Single Image**|从单个图像重建3D形状在计算机视觉中起着重要作用。已经提出了许多方法，并取得了令人印象深刻的性能。然而，现有的方法主要侧重于从图像中提取语义信息，然后简单地将其与3D点云连接起来，而不进一步探索连接的语义。因此，这些纠缠的语义特征严重阻碍了重建性能。本文提出了一种新的单图像三维重建方法，称为从单图像中挖掘有效语义线索进行三维重建（MESC-3D），该方法可以从纠缠特征中主动挖掘有效的语义线索。具体来说，我们设计了一个有效的语义挖掘模块，在点云和图像语义属性之间建立联系，使点云能够自主选择必要的信息。此外，为了解决单个图像中语义信息的潜在不足，例如遮挡，受人类使用从日常经验中提取的先验知识表示3D对象的能力的启发，我们引入了一个3D语义先验学习模块。该模块结合了对空间结构的语义理解，使模型能够更准确、更真实地解释和重建3D对象，密切反映了人类对复杂3D环境的感知。广泛的评估表明，与先前的工作相比，我们的方法在重建质量和鲁棒性方面取得了显著的改进。此外，进一步的实验验证了强大的泛化能力，并在看不见的类上优于零样本预性能。代码可在以下网址获得https://github.com/QINGQINGLE/MESC-3D. et.al.|[2502.20861](http://arxiv.org/abs/2502.20861)|null|
|**2025-02-28**|**EndoPBR: Material and Lighting Estimation for Photorealistic Surgical Simulations via Physically-based Rendering**|手术场景的3D视觉中缺乏标记数据集，这阻碍了医学领域稳健的3D重建算法的发展。尽管神经辐射场和3D高斯散斑在一般计算机视觉领域很受欢迎，但由于非平稳照明和非朗伯表面等挑战，这些系统在手术场景中尚未取得一致的成功。因此，对标记手术数据集的需求继续增长。在这项工作中，我们引入了一种可微分渲染框架，用于从内窥镜图像和已知几何形状中估计材料和光照。与之前将光照和材质联合建模为辐射的方法相比，我们明确地解开了这些场景属性，以实现鲁棒和逼真的新颖视图合成。为了消除训练过程的歧义，我们制定了手术场景中固有的领域特定属性。具体来说，我们将场景照明建模为简单的聚光灯，将材质属性建模为双向反射分布函数，由神经网络参数化。通过在渲染方程中进行颜色预测，我们可以在任意相机姿态下生成逼真的图像。我们使用结肠镜3D视频数据集中的各种序列评估了我们的方法，并表明与其他方法相比，我们的方法产生了具有竞争力的新颖视图合成结果。此外，我们证明，通过使用我们的渲染输出微调深度估计模型，合成数据可用于开发3D视觉算法。总体而言，我们看到深度估计性能与原始真实图像的微调相当。 et.al.|[2502.20669](http://arxiv.org/abs/2502.20669)|null|
|**2025-02-27**|**Cutting-edge 3D reconstruction solutions for underwater coral reef images: A review and comparison**|珊瑚是珊瑚礁生态系统中的基础栖息地构建生物，构建了延伸至遥远距离的广泛结构。然而，它们固有的脆弱性和易受各种威胁的脆弱性使它们容易受到重大损害和破坏。应用先进的3D重建技术进行高质量建模对于保存它们至关重要。这些技术帮助科学家准确记录和监测珊瑚礁的状态，包括其结构、物种分布和随时间的变化。基于摄影测量的方法在现有的解决方案中脱颖而出，特别是随着水下摄影、摄影测量计算机视觉和机器学习的最新进展。尽管基于图像的3D重建技术不断进步，但仍然缺乏对专门应用于水下珊瑚礁图像的尖端解决方案的系统回顾和全面评估。新兴的先进方法可能难以应对水下成像环境、复杂的珊瑚结构和计算资源限制。需要对它们进行审查和评估，以弥合许多前沿技术研究和实际应用之间的差距。本文重点研究了这些方法的两个关键阶段：相机姿态估计和密集表面重建。我们系统地回顾和总结了经典和新兴方法，通过现实世界和模拟数据集进行了全面评估。基于我们的研究结果，我们提出了参考建议，并深入讨论了现有方法的发展潜力和挑战。这项工作为科学家和管理人员提供了处理水下珊瑚礁图像进行3D重建的技术基础和实践指导。。。。 et.al.|[2502.20154](http://arxiv.org/abs/2502.20154)|null|
|**2025-02-26**|**Compression in 3D Gaussian Splatting: A Survey of Methods, Trends, and Future Directions**|3D高斯散斑（3DGS）最近成为显式场景渲染和计算机图形学中的一种开创性方法。与传统的神经辐射场（NeRF）方法不同，后者通常依赖于隐式的基于坐标的模型将空间坐标映射到像素值，3DGS利用了数百万个可学习的3D高斯分布。其可微分渲染技术和显式场景表示和操纵的固有能力使3DGS成为下一代3D重建和表示技术的潜在游戏规则改变者。这使得3DGS能够提供实时渲染速度，同时提供无与伦比的可编辑性级别。然而，尽管3DGS具有优势，但它存在大量的内存和存储需求，这给在资源受限的设备上部署带来了挑战。在本次调查中，我们提供了一个全面的概述，重点介绍了3DGS的可扩展性和压缩性。我们首先对3DGS进行详细的背景概述，然后对现有的压缩方法进行结构化分类。此外，我们从拓扑的角度分析和比较了当前的方法，评估了它们在保真度、压缩比和计算效率方面的优势和局限性。此外，我们还探讨了高效NeRF表示的进步如何激发3DGS优化的未来发展。最后，我们总结了当前的研究挑战，并强调了未来探索的关键方向。 et.al.|[2502.19457](http://arxiv.org/abs/2502.19457)|null|
|**2025-02-26**|**Flexible Foil Mesh Generation for Spatial Focal-Body Modeling of a Spherical Mirror**|我们提出了一种柔性箔网格生成（FFMG）方法的新应用，用于对球面镜在其光轴上收集来自无限远光源的光所生成的 $3D$ 焦点进行建模。该研究解决了准确表示由聚焦效应形成的高度凹形结构的挑战。通过理论分析和数值模拟，我们证明了FFMG方法在捕捉焦体复杂几何形状方面的有效性，并对计算几何、三维重建和光学系统建模产生了影响。 et.al.|[2502.19092](http://arxiv.org/abs/2502.19092)|null|
|**2025-02-25**|**Spatial Analysis of Neuromuscular Junctions Activation in Three-Dimensional Histology-based Muscle Reconstructions**|组织学长期以来一直是通过组织切片研究解剖结构的基础技术。计算方法的进步现在可以从组织学图像中对器官进行三维（3D）重建，从而增强对结构和功能特征的分析。在这里，我们提出了一种新的多模态计算方法，使用经典的图像处理和数据分析技术在3D中重建啮齿动物肌肉，分析其结构特征并将其与之前记录的电生理数据相关联。该算法分析通过组织学染色识别的特征的空间分布模式，并在多个样本中对其进行归一化。此外，该算法成功地将空间模式与高密度肌表肌电（hdEMG）记录相关联，提供了神经肌肉动力学的多模态视角，将空间和电生理信息联系起来。通过观察幼年比目鱼肌中神经肌肉接头（NMJ）的分布，并将观察到的分布和模式与先前文献中观察到的进行比较，验证了该代码的有效性。我们的结果与预期结果一致，验证了我们的特征和模式识别方法。多模式方面显示在初生比目鱼肌中，通过hdEMG得出的运动单位位置与从组织学获得的NMJ位置之间存在很强的相关性，突出了它们的空间关系。这种多模态分析工具将3D结构数据与电生理活动相结合，为肌肉诊断、再生医学和个性化治疗开辟了新的途径，在这些领域，空间洞察力有朝一日可以预测电生理行为，反之亦然。 et.al.|[2502.18646](http://arxiv.org/abs/2502.18646)|**[link](https://github.com/aleasca/histology-nmj-and-muscle-activity-toolbox)**|
|**2025-03-01**|**Table-top three-dimensional photoemission orbital tomography with a femtosecond extreme ultraviolet light source**|在量子力学电子波函数水平上跟踪分子和材料中的电子过程，具有埃级的空间分辨率，并完全可以访问其飞秒时间动力学，这是超快凝聚态物理学的核心。一项允许实验获取电子波函数的突破性发明是2009年根据角分辨光电子能谱数据重建分子轨道，称为光电发射轨道断层扫描（POT）。本发明使超快三维（3D）POT触手可及，为超快光物质相互作用、飞秒化学和光诱导相变的研究带来了许多新的前景。在这里，我们开发了一种协同实验算法方法，使用短脉冲极紫外光源实现了第一个3D-POT实验。我们将光电子能谱的一种新变体，即超快动量显微镜，与台式光谱可调高次谐波产生光源和量身定制的算法相结合，用于从稀疏、欠采样的数据中高效地进行3D重建。这种组合大大加快了实验数据采集的速度，同时降低了实现完整3D信息的采样要求。我们通过对原始Ag（110）上吸收的原型有机半导体的前线轨道进行全3D成像，展示了这种方法的强大功能。 et.al.|[2502.18269](http://arxiv.org/abs/2502.18269)|null|
|**2025-02-25**|**Synthesizing Consistent Novel Views via 3D Epipolar Attention without Re-Training**|大型扩散模型在单个图像的新颖视图合成中表现出显著的零样本能力。然而，这些模型在保持新颖和参考视图之间的一致性方面经常面临挑战。导致这一问题的一个关键因素是参考视图中上下文信息的利用有限。具体来说，当两个视图之间的视锥中存在重叠时，必须确保相应的区域在几何形状和外观上保持一致性。这一观察结果导致了一种简单而有效的方法，我们建议使用极线几何来定位和检索输入视图中的重叠信息。然后，这些信息被纳入目标视图的生成中，从而消除了训练或微调的需要，因为该过程不需要可学习的参数。此外，为了增强生成视图的整体一致性，我们将极线注意力的利用扩展到多视图设置，允许从输入视图和其他目标视图中检索重叠信息。定性和定量实验结果表明，我们的方法在不需要任何微调的情况下显著提高了合成视图的一致性。此外，这种增强还提高了3D重建等下游应用的性能。该代码可在以下网址获得https://github.com/botaoye/ConsisSyn. et.al.|[2502.18219](http://arxiv.org/abs/2502.18219)|null|
|**2025-02-24**|**Graph-Guided Scene Reconstruction from Images with 3D Gaussian Splatting**|本文研究了从图像重建高质量、大型3D开放场景的开放性研究挑战。据观察，现有的方法有各种局限性，例如需要精确的相机姿态进行输入，需要密集的视点进行监督。为了进行有效和高效的3D场景重建，我们提出了一种新的图引导3D场景重建框架GraphGS。具体来说，给定场景上RGB相机捕获的一组图像，我们首先设计了一种基于空间先验的场景结构估计方法。然后，这将用于创建包含有关相机拓扑信息的相机图。此外，我们建议将图引导的多视图一致性约束和自适应采样策略应用于3D高斯散斑优化过程。这大大缓解了高斯点对特定稀疏视点过拟合的问题，并加快了3D重建过程。我们证明GraphGS能够从图像中实现高保真度的3D重建，通过对多个数据集进行定量和定性评估，展现出最先进的性能。项目页面：https://3dagentworld.github.io/graphgs. et.al.|[2502.17377](http://arxiv.org/abs/2502.17377)|null|
|**2025-02-25**|**MegaLoc: One Retrieval to Place Them All**|从给定查询的同一位置检索图像是多个计算机视觉任务的重要组成部分，如视觉位置识别、地标检索、视觉定位、3D重建和SLAM。然而，现有的解决方案是专门为其中一项任务而构建的，当需求略有变化或满足分布外数据时，已知会失败。在本文中，我们结合了各种现有的方法、训练技术和数据集来训练一个名为MegaLoc的检索模型，该模型可在多个任务上运行。我们发现，MegaLoc（1）在大量视觉位置识别数据集上达到了最先进的水平，（2）在常见的地标检索数据集上取得了令人印象深刻的结果，（3）在LaMAR数据集上为视觉定位设定了新的水平，我们只将检索方法更改为现有的定位管道。MegaLoc的代码可在以下网址获得https://github.com/gmberton/MegaLoc et.al.|[2502.17237](http://arxiv.org/abs/2502.17237)|**[link](https://github.com/gmberton/megaloc)**|

<p align=right>(<a href=#updated-on-20250304>back to top</a>)</p>

## Diffusion

|Publish Date|Title|Abstract|PDF|Code|
|---|---|---|---|---|
|**2025-02-28**|**Raccoon: Multi-stage Diffusion Training with Coarse-to-Fine Curating Videos**|随着扩散模型的出现，文本到视频的生成已经显示出有希望的进展，但现有的方法受到数据集质量和计算资源的限制。为了解决这些局限性，本文提出了一种全面的方法，该方法同时推进了数据管理和模型设计。我们介绍了CFC-VIDS-1M，这是一个通过系统的粗到细管理管道构建的高质量视频数据集。该管道首先在多个维度上评估视频质量，然后是一个细粒度阶段，该阶段利用视觉语言模型来增强文本视频对齐和语义丰富性。基于精心策划的数据集对视觉质量和时间连贯性的强调，我们开发了RACCOON，这是一种基于转换器的架构，具有解耦的时空注意力机制。该模型通过渐进的四阶段策略进行训练，旨在有效地处理视频生成的复杂性。大量实验表明，我们的高质量数据管理和高效训练策略的集成方法在保持计算效率的同时，生成了具有视觉吸引力和时间连贯性的视频。我们将发布我们的数据集、代码和模型。 et.al.|[2502.21314](http://arxiv.org/abs/2502.21314)|null|
|**2025-02-28**|**Oscillatory finite-time singularities in rockbursts**|由于涉及重大不确定性，预测剧烈岩爆仍然是一项艰巨的挑战。一个主要的不确定性来自岩石破坏过程的间歇性，其特征通常是一系列逐渐缩短的静止阶段，中间穿插着突然的加速，而不是朝向最终破坏的平稳连续进展。岩体变形的这种非单调演化使岩爆预测复杂化，挑战了通常假设平滑幂律加速行为的传统失效时间模型。在这里，我们引入了一种广义的失效时间模型，称为对数周期幂律奇异性（LPPLS）模型，以有效地捕捉岩石中导致剧烈岩爆的损伤和破裂过程的间歇动力学。我们对三个地下矿山的11个历史岩爆事件进行了参数和非参数检验，记录了经验证据，并提供了理论论据，以证明对数周期振荡幂律有限时间奇异性的意义。这些岩爆事件的对数周期性可能是由亚平行传播裂纹的相互作用、应力触发过程的扩散或应力降和应力腐蚀之间的相互作用驱动的。我们获得的结果和见解不仅对理解而且对预测岩爆具有重要意义，因为识别和表征测井周期性可以帮助将传统感知噪声的间歇性转化为有价值的预测信息。 et.al.|[2502.21296](http://arxiv.org/abs/2502.21296)|null|
|**2025-03-03**|**MIGE: A Unified Framework for Multimodal Instruction-Based Image Generation and Editing**|尽管在基于扩散的图像生成方面取得了重大进展，但主题驱动的生成和基于指令的编辑仍然具有挑战性。现有的方法通常将它们分开处理，难以处理有限的高质量数据和较差的泛化能力。然而，这两项任务都需要捕捉复杂的视觉变化，同时保持输入和输出之间的一致性。因此，我们提出了MIGE，这是一个使用多模态指令标准化任务表示的统一框架。它将主题驱动的生成视为在空白画布上的创建，将基于指令的编辑视为对现有图像的修改，建立共享的输入输出公式。MIGE引入了一种新型的多模态编码器，该编码器将自由形式的多模态指令映射到统一的视觉语言空间中，通过特征融合机制整合视觉和语义特征。这种统一实现了两个任务的联合训练，提供了两个关键优势：（1）跨任务增强：通过利用共享的视觉和语义表示，联合训练提高了主题驱动生成和基于指令的编辑中的指令遵从性和视觉一致性。（2） 泛化：统一格式的学习有助于跨任务知识转移，使MIGE能够泛化到新的组合任务，包括基于指令的主题驱动编辑。实验表明，MIGE在主题驱动生成和基于指令的编辑方面都表现出色，同时为基于指令的主题驱动编辑的新任务设定了最先进的水平。代码和模型已公开于https://github.com/Eureka-Maggie/MIGE. et.al.|[2502.21291](http://arxiv.org/abs/2502.21291)|null|
|**2025-02-28**|**Flow-Driven Rotor Simulations of Seyi-Chunlei Ducted Turbine**|本文提出了一种改进的克拉克森导管式风力涡轮机（DWT）设计，该设计使用了一种基于Selig S1223翼型的新型扩散器，攻角（AoA）为20度，叶尖间隙较小。与最初的克拉克森管道式风力发电机（CDWT）相比，该拟议设计特此命名为Selig20克拉克森管道风力发电机或Seyi Chunlei管道式风力涡轮机（SCDT）。在SCDT和CDWT配置中，转子都放置在管道喉部后面一定距离处。为了进行深入分析，我们采用了商业CFD软件包Simerics MP+的流驱动转子（FDR）模型，该模型基于非定常雷诺平均Navier-Stokes（URANS）方程的非结构化网格有限体积解，用于与涡轮机转子刚体旋转的动态解双向完全耦合的流场。FDR模型成功地预测了最佳推力系数，而规定的旋转模型未能做到这一点。尽管FDR模型预测的最佳Cp与规定的运动模型的预测相当接近，但FDR在预测远离最佳叶尖速比的环境风条件下的性能不佳方面通常更准确。FDR为在环境风条件下模拟导管式风力涡轮机提供了一条新途径。经证实，Seyi Chunlei管道式水轮机的Cpt峰值比Clarkson DWT高出约7%。SCDT还具有更广泛的最佳叶尖速比，使其能够在环境条件下收获更多的风能。 et.al.|[2502.21289](http://arxiv.org/abs/2502.21289)|null|
|**2025-02-28**|**Does Generation Require Memorization? Creative Diffusion Models using Ambient Diffusion**|有强有力的实证证据表明，最先进的扩散建模范式导致模型能够记住训练集，尤其是在训练集很小的情况下。先前缓解记忆问题的方法通常会导致图像质量下降。是否有可能获得强大而创造性的生成模型，即实现高生成质量和低记忆的模型？尽管目前的结果令人悲观，但我们在推动保真度和记忆之间的权衡方面取得了重大进展。我们首先提供了理论证据，证明扩散模型中的记忆只对低噪声尺度（通常用于生成高频细节）的去噪问题是必要的。基于这一理论见解，我们提出了一种简单、有原则的方法，使用大噪声尺度下的噪声数据训练扩散模型。我们表明，对于文本条件和无条件模型以及各种数据可用性设置，我们的方法在不降低图像质量的情况下显著减少了记忆。 et.al.|[2502.21278](http://arxiv.org/abs/2502.21278)|null|
|**2025-02-28**|**Log-Periodic Precursors to Volcanic Eruptions: Evidence from 34 Events**|由于火山过程固有的复杂性和可变性，预测火山爆发仍然是一项艰巨的挑战。不确定性的一个关键来源是火山动荡的零星性，其特征通常是间歇的静止减速和突然加速阶段，而不是一致的、可预测的喷发进程。这种看似不稳定的模式使火山预测变得复杂，因为它挑战了通常假设简单平稳幂律加速的传统故障时间模型。我们提出了一个对数周期幂律奇异性模型，该模型有效地捕捉了现场尺度上复活火山的间歇和非单调破裂动力学特征。从数学上讲，通过将幂律指数从实数扩展到复数来推广幂律指数，该模型捕捉到了连续尺度不变性到离散尺度不变性的部分突破，这是非均匀地壳系统中损伤和破裂过程的间歇动力学所固有的。通过对全球34次历史火山爆发的大型数据集进行参数和非参数检验，我们提出了经验证据和理论论据，证明了在爆发前火山动荡期间对数周期振荡装饰幂律有限时间奇异性的统计意义。火山的对数周期性可能源于各种机制，包括扩散主导的岩浆流动、岩浆驱动的近平行岩脉传播、应力降和应力腐蚀之间的相互作用，和/或火山系统内惯性、损伤和愈合的相互作用。我们的研究结果对火山预测具有重要意义，因为理解和表征测井周期性可以将火山活动的间歇性从挑战转变为改进预测的宝贵资产。 et.al.|[2502.21277](http://arxiv.org/abs/2502.21277)|null|
|**2025-02-28**|**PET Image Denoising via Text-Guided Diffusion: Integrating Anatomical Priors through Text Prompts**|低剂量正电子发射断层扫描（PET）成像由于噪声增加和图像质量降低而面临重大挑战，这可能会损害其诊断准确性和临床实用性。去噪扩散概率模型（DDPM）在PET图像去噪方面表现出了良好的性能。然而，现有的基于DDPM的方法通常会忽略有价值的元数据，如患者人口统计、解剖信息和扫描参数，如果考虑到这些元数据，应该会进一步提高去噪性能。视觉语言模型（VLMs）的最新进展，特别是预训练的对比语言图像预训练（CLIP）模型，突显了将基于文本的信息整合到视觉任务中以提高下游性能的潜力。在这项初步研究中，我们提出了一种新的文本引导DDPM用于PET图像去噪，该方法通过文本提示整合了解剖先验。使用预训练的CLIP文本编码器对解剖文本描述进行编码，以提取语义指导，然后通过交叉注意力机制将其纳入扩散过程。基于1/20低剂量和正常剂量18F-FDG PET数据集的评估表明，所提出的方法在全身和器官水平上都比传统的UNet和标准DDPM方法具有更好的定量性能。这些结果强调了利用VLM将丰富的元数据整合到扩散框架中以提高低剂量PET扫描图像质量的潜力。 et.al.|[2502.21260](http://arxiv.org/abs/2502.21260)|null|
|**2025-02-28**|**Short-Rate Derivatives in a Higher-for-Longer Environment**|我们介绍了一类短期利率模型，它们表现出“长时间更高”的现象。具体而言，短速率被建模为有限区间上的一般时间齐次单因素马尔可夫扩散。根据边界分类，下端点被假设为规则的、出口的或自然的，而上端点则被假设为具有规则的吸收行为。在此背景下，我们给出了零息债券（以及更一般的利率衍生品）价格的显式表达式，该表达式表示在新的概率度量下的短期利率转移密度，以及非线性常微分方程（ODE）的解。然后，我们将重点缩小到一类可以显式求解跃迁密度和常微分方程的模型。对于此类中的模型，我们提供了下端点是规则的、退出的和自然的条件。最后，我们研究了两个具体的模型——一个模型的下限是出口，另一个模型中的下限是自然的。在这两个模型中，我们给出了作为（广义）本征函数展开的短速率跃迁密度的显式解。我们提供了转换密度、（广义）本征函数、债券价格和相关收益率曲线的图。 et.al.|[2502.21252](http://arxiv.org/abs/2502.21252)|null|
|**2025-03-03**|**Stability of axial free-boundary hyperplanes in circular cones**|给定一个轴对称的 $（n+1）$维凸锥$\Omega\secute\mathbb{R}^{n+1}$，我们研究了通过将$\Omega$与包含$\Omega$轴的$n$平面相交而获得的自由边界最小曲面$\Sigma$的稳定性。在$n=2$的情况下，$\Sigma$总是不稳定的，正如同一作者最近在一篇论文中证明的顶点跳跃性质的一个特例。相反，只要n\ge 3$和$\Omega$具有足够大的孔径（取决于维度$n$），我们就会证明$\Sigma$是严格稳定的。为了我们的稳定性分析，我们引入了一个Lipschitz流$\Sigma_{t}[f]$，该流与紧支撑的标量变形场$f$相关联的$\Sigma$变形，它满足所有$t\in\mathbb{R}$的关键属性$\partial\Sigma_{t}/f]\subsette\partial\Omega$。然后，我们计算了$\Sigma$ 沿流面积的右下二阶变分，并最终通过利用其与在反应扩散问题背景下研究的泛函不等式的联系证明了它是正的。 et.al.|[2502.21205](http://arxiv.org/abs/2502.21205)|null|
|**2025-02-28**|**Sub-elliptic diffusions on compact groups via Dirichlet form perturbation**|这项工作在无限维紧连通可度量群的背景下扩展了经典有限维亚椭圆理论的部分内容。给定一个易于理解且行为良好的双不变拉普拉斯算子 $\Delta$和一个子拉普拉斯算子$L$，它们自然地附加了内在距离$d_\Delta$d_L$，我们证明了形式为$d_L\le C（d_\Delta）^C$（对于某些$0<C\le 1$）的比较不等式意味着$\Delta-$的分数幂的狄利克雷形式由与$L$相关的狄利克莱形式主导。我们利用这一结果表明，在其他假设下，$\Delta$的热核的某些良好属性随后被传递给与$L$相关的热核。讨论了关于$SU（2）$ 副本的无穷乘积的显式例子来说明这些结果。 et.al.|[2502.21152](http://arxiv.org/abs/2502.21152)|null|

<p align=right>(<a href=#updated-on-20250304>back to top</a>)</p>

## NeRF

|Publish Date|Title|Abstract|PDF|Code|
|---|---|---|---|---|
|**2025-02-27**|**RANGE: Retrieval Augmented Neural Fields for Multi-Resolution Geo-Embeddings**|地理位置表示的选择会显著影响各种地理空间任务模型的准确性，包括细粒度物种分类、种群密度估计和生物群落分类。最近的作品，如SatCLIP和GeoCLIP，通过将地理位置与共置图像进行对比对齐来学习这种表示。虽然这些方法非常有效，但在本文中，我们认为当前的训练策略未能完全捕捉到重要的视觉特征。我们从信息论的角度解释了为什么这些方法产生的嵌入会丢弃对许多下游任务很重要的关键视觉信息。为了解决这个问题，我们提出了一种新的检索增强策略，称为RANGE。我们的方法基于这样一种直觉，即可以通过组合来自多个看起来相似的位置的视觉特征来估计位置的视觉特性。我们在各种各样的任务中评估我们的方法。我们的结果表明，RANGE在大多数任务中表现优于现有的最先进的模型，并具有显著的优势。我们显示，分类任务的收益高达13.1%，回归任务的收益为0.145 $R^2$ 。我们所有的代码都将在GitHub上发布。我们的模型将在HuggingFace上发布。 et.al.|[2502.19781](http://arxiv.org/abs/2502.19781)|null|
|**2025-02-20**|**MedFuncta: Modality-Agnostic Representations Based on Efficient Neural Fields**|最近关于深度学习医学图像分析的研究几乎完全集中在基于网格或体素的数据表示上。我们通过引入MedFuncta来挑战这一常见选择，MedFuncta是一种基于神经场的模态无关连续数据表示。我们演示了如何通过利用医学信号中的冗余以及应用具有上下文缩减方案的高效元学习方法，将神经场从单个实例扩展到大型数据集。我们通过引入 $\omega_0$ -调度，提高重建质量和收敛速度，进一步解决了常用SIREN激活中的光谱偏差问题。我们在各种不同维度和模式的医学信号上验证了我们提出的方法（1D：心电图；2D：胸部X射线、视网膜OCT、眼底照相机、皮肤镜、结肠组织病理学、细胞显微镜；3D：脑MRI、肺CT），并成功证明我们可以解决这些表示的相关下游任务。我们还发布了一个超过550k个带注释神经场的大规模数据集，以促进这方面的研究。 et.al.|[2502.14401](http://arxiv.org/abs/2502.14401)|**[link](https://github.com/pfriedri/medfuncta)**|
|**2025-02-15**|**Implicit Neural Representations of Molecular Vector-Valued Functions**|分子有各种计算表示，包括数值描述符、字符串、图形、点云和曲面。每种表示方法都可以应用各种机器学习方法，从线性回归到与大型语言模型配对的图神经网络。为了补充现有的表示，我们通过向量值函数或n维向量场引入分子的表示，这些向量值函数由神经网络参数化，我们称之为分子神经场。与表面表征不同，分子神经场捕获蛋白质等大分子的外部特征和疏水核心。与离散图或点表示相比，分子神经场结构紧凑，分辨率无关，天生适合在空间和时间维度上进行插值。分子神经场继承的这些特性适用于包括基于所需形状、结构和组成生成分子，以及空间和时间中分子构象之间分辨率无关的插值在内的任务。在这里，我们为分子神经场提供了一个框架和概念证明，即使用自动解码器架构对蛋白质-配体复合物进行参数化和超分辨率重建，以及使用自动编码器架构将分子体积嵌入潜在空间。 et.al.|[2502.10848](http://arxiv.org/abs/2502.10848)|**[link](https://github.com/daenuprobst/minf)**|
|**2025-02-05**|**Poisson Hypothesis and large-population limit for networks of spiking neurons**|我们研究了具有随机尖峰时间的线性（泄漏）和二次积分和放电神经元的空间扩展网络的平均场描述。我们考虑了具有线性和二次内在动力学的连续时间Galves-L“ocherbach（GL）网络的大种群极限。我们证明了泊松假设适用于这些网络的复制平均场极限，即在适当定义的极限内，神经元是独立的，相互作用时间被强度取决于平均放电率的独立时间非均匀泊松过程所取代，将已知结果扩展到具有二次内在动态和重置的网络。证明泊松假设成立为研究这些网络中的大种群限值开辟了可能性。我们证明这个极限是一个适定的神经场模型，受随机重置的影响。 et.al.|[2502.03379](http://arxiv.org/abs/2502.03379)|null|
|**2025-02-04**|**Geometric Neural Process Fields**|本文解决了神经场（NeF）泛化的挑战，其中模型必须有效地适应仅给出少量观测值的新信号。为了解决这个问题，我们提出了几何神经过程场（G-NPF），这是一个明确捕捉不确定性的神经辐射场的概率框架。我们将NeF泛化表述为概率问题，从而能够从有限的上下文观测中直接推断出NeF函数分布。为了引入结构归纳偏差，我们引入了一组几何基来编码空间结构，并促进NeF函数分布的推断。在此基础上，我们设计了一个分层潜在变量模型，使G-NPF能够整合多个空间层次的结构信息，并有效地参数化INR函数。这种分层方法提高了对新场景和未知信号的泛化能力。针对3D场景的新颖视图合成以及2D图像和1D信号回归的实验证明了我们的方法在捕捉不确定性和利用结构信息提高泛化能力方面的有效性。 et.al.|[2502.02338](http://arxiv.org/abs/2502.02338)|null|
|**2025-02-05**|**A Poisson Process AutoDecoder for X-ray Sources**|钱德拉X射线天文台和eROSITA等X射线观测设施已经探测到数百万个与高能现象相关的天文源。光子的到达作为时间的函数遵循泊松过程，并且可以按数量级变化，这为源分类、物理性质推导和异常检测等常见任务带来了障碍。之前的工作要么未能直接捕捉数据的泊松性质，要么只关注泊松率函数重建。在这项工作中，我们提出了泊松过程自动解码器（PPAD）。PPAD是一种神经场解码器，通过无监督学习将固定长度的潜在特征映射到跨能带和时间的连续泊松率函数。PPAD重建速率函数并同时产生表示。我们使用钱德拉源目录通过重建、回归、分类和异常检测实验证明了PPAD的有效性。 et.al.|[2502.01627](http://arxiv.org/abs/2502.01627)|null|
|**2025-02-03**|**Regularized interpolation in 4D neural fields enables optimization of 3D printed geometries**|精确生产具有特定特性的几何形状的能力可能是制造过程中最重要的特征。3D打印具有非凡的设计自由度和复杂性，但也容易出现几何和其他缺陷，必须解决这些缺陷才能充分发挥其潜力。最终，这将需要精明的设计决策和及时的参数调整来保持稳定性，即使是专业的人类操作员也很难做到这一点。虽然机器学习在3D打印中得到了广泛的研究，但现有的方法通常会忽略不同打印的空间特征，因此很难产生所需的几何形状。在这里，我们将打印部件的体积表示编码到神经场中，并应用一种新的正则化策略，该策略基于最小化场输出相对于单个不可学习参数的偏导数。因此，通过鼓励小的输入变化只产生小的输出变化，我们鼓励在观测体积之间进行平滑插值，从而实现现实的几何预测。因此，该框架允许提取“想象的”3D形状，揭示了在以前看不见的参数下制造的零件的外观。由此产生的连续场用于数据驱动优化，以最大限度地提高预期和生产几何形状之间的几何保真度，减少后处理、材料浪费和生产成本。通过动态优化工艺参数，我们的方法实现了先进的规划策略，有可能使制造商更好地实现复杂和功能丰富的设计。 et.al.|[2502.01517](http://arxiv.org/abs/2502.01517)|**[link](https://github.com/cam-cambridge/4d-neural-fields-optimise-3d-printing)**|
|**2025-02-03**|**Modelling change in neural dynamics during phonetic accommodation**|短期语音调节是口音变化背后的基本驱动力，但来自另一个说话者声音的实时输入是如何塑造对话者的语音规划表示的？我们基于运动规划和记忆动力学的动态神经场方程，提出了一种语音调节过程中语音表征变化的计算模型。我们测试了该模型从实验研究中捕捉经验模式的能力，在实验研究中，说话者用与自己不同的口音跟踪模型说话者。实验数据显示了阴影期间元音特定的收敛程度，随后在阴影后恢复到基线（或轻微发散）。该模型可以通过调节抑制性记忆动力学的大小来再现这些现象，这可能反映了由于语音和/或社会语言压力导致的对调节的抵抗。我们讨论了这些结果对短期语音调节和长期声音变化模式之间关系的影响。 et.al.|[2502.01210](http://arxiv.org/abs/2502.01210)|null|
|**2025-02-02**|**Lifting the Winding Number: Precise Representation of Complex Cuts in Subspace Physics Simulations**|切割薄壁可变形结构在日常生活中很常见，但由于引入了空间不连续性，给模拟带来了重大挑战。传统方法依赖于基于网格的域表示，这需要频繁的重新网格划分和细化，以准确捕捉不断变化的不连续性。这些挑战在缩减空间模拟中进一步加剧，在这种模拟中，基函数固有地依赖于几何和网格，使得基难以甚至不可能表示切割引入的各种不连续性。用神经场表示基函数的最新进展提供了一种有前景的替代方案，利用其离散化不可知的性质来表示不同几何形状的变形。然而，神经场的固有连续性阻碍了泛化，特别是在神经网络权重中编码了不连续性的情况下。我们提出了Wind-Lifter，这是一种新的神经表示，旨在精确模拟薄壁可变形结构中的复杂切割。我们的方法构建神经场，在指定位置精确再现不连续性，而无需在切割线的位置烘烤。至关重要的是，我们的方法没有将不连续性嵌入神经网络的权重中，为切割位置的泛化开辟了道路。我们的方法实现了实时仿真速度，并支持在仿真过程中动态更新切割线几何形状。此外，不连续性的显式表示使我们的神经场易于控制和编辑，与传统的神经场相比具有显著的优势，在传统的神经场内，不连续被嵌入网络的权重中，并支持依赖于一般切割位置的新应用。 et.al.|[2502.00626](http://arxiv.org/abs/2502.00626)|null|
|**2025-01-31**|**Lifting by Gaussians: A Simple, Fast and Flexible Method for 3D Instance Segmentation**|我们介绍了一种新的三维高斯散斑辐射场（3DGS）开放世界实例分割方法——高斯提升（LBG）。最近，3DGS场已经成为基于神经场的高质量新视图合成方法的高效和明确的替代方案。我们的3D实例分割方法直接从SAM（或FastSAM等）中提取2D分割掩模，以及CLIP和DINOv2的特征，直接将它们融合到3DGS（或类似的高斯辐射场，如2DGS）上。与以前的方法不同，LBG不需要每个场景的训练，使其能够在任何现有的3DGS重建上无缝运行。我们的方法不仅比现有方法快一个数量级，而且更简单；它也是高度模块化的，能够对现有的3DGS字段进行3D语义分割，而不需要对3D高斯进行特定的参数化。此外，我们的技术在保持灵活性和效率的同时，为2D语义新颖视图合成和3D资产提取结果实现了卓越的语义分割。我们进一步介绍了一种从3D辐射场分割方法中评估单独分割的3D资产的新方法。 et.al.|[2502.00173](http://arxiv.org/abs/2502.00173)|null|

<p align=right>(<a href=#updated-on-20250304>back to top</a>)</p>

[contributors-shield]: https://img.shields.io/github/contributors/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[contributors-url]: https://github.com/Vincentqyw/cv-arxiv-daily/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[forks-url]: https://github.com/Vincentqyw/cv-arxiv-daily/network/members
[stars-shield]: https://img.shields.io/github/stars/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[stars-url]: https://github.com/Vincentqyw/cv-arxiv-daily/stargazers
[issues-shield]: https://img.shields.io/github/issues/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[issues-url]: https://github.com/Vincentqyw/cv-arxiv-daily/issues

