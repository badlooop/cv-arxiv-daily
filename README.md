[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]

## Updated on 2025.03.18
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
|**2025-03-17**|**Generative Gaussian Splatting: Generating 3D Scenes with Video Diffusion Priors**|合成一致且逼真的3D场景是计算机视觉领域的一个悬而未决的问题。视频扩散模型生成令人印象深刻的视频，但不能直接合成3D表示，即生成的序列缺乏3D一致性。此外，由于缺乏大规模的3D训练数据，直接训练生成性3D模型具有挑战性。在这项工作中，我们提出了生成高斯散斑（GGS）——一种将3D表示与预训练的潜在视频扩散模型相结合的新方法。具体来说，我们的模型合成了一个通过3D高斯基元参数化的特征场。然后，特征场被渲染为特征图并解码为多视图图像，或者直接上采样为3D辐射场。我们在场景合成的两个常见基准数据集RealEstate10K和ScanNet+上评估了我们的方法，发现我们提出的GGS模型显著提高了生成的多视图图像的3D一致性，以及在所有相关基线上生成的3D场景的质量。与没有3D表示的类似模型相比，GGS在RealEstate10K和ScanNet+上将生成的3D场景的FID提高了约20%。项目页面：https://katjaschwarz.github.io/ggs/ et.al.|[2503.13272](http://arxiv.org/abs/2503.13272)|null|
|**2025-03-17**|**Training Video Foundation Models with NVIDIA NeMo**|视频基础模型（VFM）最近被用于模拟现实世界，以训练物理AI系统并开发创造性的视觉体验。然而，在训练能够生成高质量视频的大规模、高质量VFM方面存在重大挑战。我们使用NVIDIA NeMo提供了一个可扩展的开源VFM训练管道，提供加速的视频数据集管理、多模态数据加载以及并行化的视频扩散模型训练和推理。我们还提供全面的性能分析，重点介绍高效VFM培训和推理的最佳实践。 et.al.|[2503.12964](http://arxiv.org/abs/2503.12964)|null|
|**2025-03-17**|**Frame-wise Conditioning Adaptation for Fine-Tuning Diffusion Models in Text-to-Video Prediction**|文本视频预测（TVP）是一项下游视频生成任务，它需要一个模型来生成给定一系列初始视频帧和描述所需运动的文本的后续视频帧。在实践中，TVP方法侧重于描述人类或机器人手臂对物体进行操纵的特定类别的视频。以前的方法使预先训练过的文本到图像任务模型适应，因此往往会生成缺乏所需连续性的视频。一个自然的进展是利用最近的预训练文本到视频（T2V）模型。这种方法更具挑战性，因为最常见的微调技术，低秩自适应（LoRA），会产生不理想的结果。在这项工作中，我们提出了一种基于适应的策略，我们称之为框架式调节适应（FCA）。在该模块中，我们设计了一个子模块，该子模块从输入文本中生成逐帧文本嵌入，作为辅助生成的附加文本条件。我们使用FCA来微调T2V模型，该模型将初始帧作为额外条件。我们比较并讨论了将这种嵌入注入T2V模型的更有效策略。我们通过定量和定性性能分析对我们的设计选择进行了广泛的消融研究。我们的方法为TVP的任务建立了新的最先进的技术。项目页面位于https://github.com/Cuberick-Orion/FCA . et.al.|[2503.12953](http://arxiv.org/abs/2503.12953)|null|
|**2025-03-17**|**AUTV: Creating Underwater Video Datasets with Pixel-wise Annotations**|水下视频分析受到动态海洋环境和相机运动的阻碍，仍然是计算机视觉中一项具有挑战性的任务。现有的无训练视频生成技术，在逐帧的基础上学习运动动力学，通常会产生较差的结果，出现明显的运动中断和错位。为了解决这些问题，我们提出了AUTV，这是一个用于合成具有像素注释的海洋视频数据的框架。我们通过构建两个视频数据集来证明该框架的有效性，即UTV和SUTV，UTV是一个由2000个视频文本对组成的真实世界数据集，SUTV是一个合成视频数据集，包括10000个带有海洋物体分割掩模的视频。UTV提供多样化的水下视频，并附有全面的注释，包括外观、纹理、相机内部、照明和动物行为。SUTV可用于改进水下下游任务，这在视频修复和视频对象分割中得到了证明。 et.al.|[2503.12828](http://arxiv.org/abs/2503.12828)|null|
|**2025-03-16**|**SPC-GS: Gaussian Splatting with Semantic-Prompt Consistency for Indoor Open-World Free-view Synthesis from Sparse Inputs**|基于3D高斯散斑的室内开放世界自由视图合成方法在密集输入图像中显示出显著的性能。然而，当面对稀疏输入时，它们表现出较差的性能，主要是由于高斯点的稀疏分布和视图监督不足。为了缓解这些挑战，我们提出了SPC-GS，利用基于场景布局的高斯初始化（SGI）和语义提示一致性（SPC）正则化进行稀疏输入的开放世界自由视图合成。具体来说，SGI通过利用视频生成模型生成的视图变化图像和视图约束高斯点密集化，提供了一种基于场景布局的密集高斯分布。此外，SPC通过采用SAM2开发的基于语义提示的一致性约束来减轻有限的视图监督。这种方法利用训练视图中的可用语义作为指导性提示，在具有2D和3D一致性约束的新视图中优化视觉重叠区域。广泛的实验证明了SPC-GS在Replica和ScanNet基准测试中的卓越性能。值得注意的是，我们的SPC-GS在重建质量方面实现了3.06 dB的PSNR增益，在开放世界语义分割方面实现了7.3%的mIoU改进。 et.al.|[2503.12535](http://arxiv.org/abs/2503.12535)|null|
|**2025-03-16**|**Towards Suturing World Models: Learning Predictive Models for Robotic Surgical Tasks**|我们引入了专门的基于扩散的生成模型，通过对带注释的腹腔镜手术镜头进行监督学习，捕捉精细机器人手术亚缝合动作的时空动态。所提出的模型为数据驱动的世界模型奠定了基础，这些模型能够以高时间保真度模拟手术缝合的生物力学相互作用和程序动力学。对从模拟视频中提取的 $\sim2K$ 剪辑数据集进行注释，我们将手术动作分为细粒度的子缝合类，包括针定位、瞄准、驱动和拔出的理想和非理想执行。我们微调了两种最先进的视频扩散模型，LTX video和HunyuanVideo，以生成分辨率为768x512美元、帧数为49美元的高保真手术动作序列。为了训练我们的模型，我们探索了低秩自适应（LoRA）和全模型微调方法。我们的实验结果表明，这些世界模型可以有效地捕捉缝合的动态，从而有可能改进训练模拟器、手术技能评估工具和自主手术系统。这些模型还显示了区分理想和非理想技术执行的能力，为构建手术培训和评估系统奠定了基础。我们发布了我们的模型进行测试，并作为未来研究的基础。项目页面：https://mkturkcan.github.io/suturingmodels/ et.al.|[2503.12531](http://arxiv.org/abs/2503.12531)|null|
|**2025-03-15**|**A Speech-to-Video Synthesis Approach Using Spatio-Temporal Diffusion for Vocal Tract MRI**|了解语音过程中声道运动与产生的声信号之间的关系对于辅助临床评估和制定个性化治疗和康复策略至关重要。为了实现这一目标，我们引入了一个音频到视频生成框架，用于从语音信号中创建声道的实时/电影磁共振成像（RT-/cine MRI）视觉效果。我们的框架首先对RT-/cine MRI序列和语音样本进行预处理，以实现时间对齐，确保视觉和音频数据之间的同步。然后，我们采用了一种改进的稳定扩散模型，整合了结构和时间块，以有效地捕捉同步数据中的运动特征和时间动态。该过程能够从新的语音输入中生成MRI序列，改善音频到视觉数据的转换。我们通过分析和比较合成视频中的声道运动，评估了我们对健康对照和癌症患者的框架。我们的框架展示了对新语音输入的适应性和有效的泛化能力。此外，积极的人类评价证实了其有效性，具有逼真和准确的可视化效果，表明其在门诊治疗和个性化模拟声道可视化方面的潜力。 et.al.|[2503.12102](http://arxiv.org/abs/2503.12102)|null|
|**2025-03-15**|**TACO: Taming Diffusion for in-the-wild Video Amodal Completion**|人类可以依靠对物理世界的广泛先验知识，从有限的视觉线索中推断出物体的完整形状和外观。然而，对于现有的模型，特别是对于非结构化的野生视频，在确保视频帧一致性的同时完成部分可观察的对象仍然是一个挑战。本文讨论了视频模数完成（VAC）的任务，其目的是在给定指定感兴趣对象的视觉提示的情况下，在整个视频中一致地生成完整的对象。利用预训练视频扩散模型学习到的丰富、一致的流形，我们提出了一种条件扩散模型TACO，它将这些流形重新用于VAC。为了使其能够有效和稳健地泛化到具有挑战性的野外场景中，我们通过系统地将遮挡施加到未遮挡的视频上，策划了一个具有多个难度级别的大规模合成数据集。在此基础上，我们设计了一种渐进式微调范式，从更简单的恢复任务开始，逐步推进到更复杂的任务。我们展示了TACO在互联网上的各种野生视频以及在自动驾驶、机器人操纵和场景理解中常用的各种未知数据集上的多功能性。此外，我们表明TACO可以有效地应用于各种下游任务，如对象重建和姿态估计，突出了其促进物理世界理解和推理的潜力。我们的项目页面可在https://jason-aplp.github.io/TACO. et.al.|[2503.12049](http://arxiv.org/abs/2503.12049)|null|
|**2025-03-15**|**SteerX: Creating Any Camera-Free 3D and 4D Scenes with Geometric Steering**|3D/4D场景生成的最新进展强调了在整个视频生成和场景重建过程中物理对齐的重要性。然而，现有的方法在每个阶段分别改进对齐，使得难以管理另一个阶段产生的微妙错位。在这里，我们介绍了SteerX，这是一种零样本推理时间转向方法，它将场景重建统一到生成过程中，使数据分布朝着更好的几何对齐倾斜。为此，我们引入了两个几何奖励函数，用于使用无姿态前馈场景重建模型生成3D/4D场景。通过广泛的实验，我们证明了SteerX在改进3D/4D场景生成方面的有效性。 et.al.|[2503.12024](http://arxiv.org/abs/2503.12024)|null|
|**2025-03-14**|**ReCamMaster: Camera-Controlled Generative Rendering from A Single Video**|在文本或图像条件视频生成任务中，相机控制已经得到了积极的研究。然而，尽管在视频创作领域具有重要意义，但改变给定视频的相机轨迹仍有待探索。由于维护多帧外观和动态同步的额外约束，这并非易事。为了解决这个问题，我们提出了ReCamMaster，这是一个由相机控制的生成视频重渲染框架，可以在新的相机轨迹上再现输入视频的动态场景。核心创新在于通过一种简单而强大的视频调节机制，利用预训练文本到视频模型的生成能力——这一能力在当前的研究中经常被忽视。为了克服合格训练数据的稀缺性，我们使用虚幻引擎5构建了一个全面的多摄像机同步视频数据集，该数据集经过精心策划，符合现实世界的拍摄特点，涵盖了不同的场景和摄像机动作。它有助于模型在野生视频中推广。最后，我们通过精心设计的训练策略进一步提高了对不同输入的鲁棒性。广泛的实验表明，我们的方法大大优于现有的最先进的方法和强大的基线。我们的方法在视频稳定、超分辨率和外画方面也有很好的应用前景。项目页面：https://jianhongbai.github.io/ReCamMaster/ et.al.|[2503.11647](http://arxiv.org/abs/2503.11647)|null|

<p align=right>(<a href=#updated-on-20250318>back to top</a>)</p>

## 3D

|Publish Date|Title|Abstract|PDF|Code|
|---|---|---|---|---|
|**2025-03-17**|**TriDF: Triplane-Accelerated Density Fields for Few-Shot Remote Sensing Novel View Synthesis**|遥感新视图合成（NVS）为遥感场景的3D解释提供了巨大的潜力，在城市规划和环境监测中具有重要应用。然而，由于采集限制，遥感场景经常缺乏足够的多视图图像。虽然现有的NVS方法在处理有限的输入视图时往往会过拟合，但先进的少镜头NVS方法计算量大，在遥感场景中的表现欠佳。本文介绍了TriDF，这是一种高效的混合3D表示方法，用于从少至3个输入视图快速遥感NVS。我们的方法将颜色和体积密度信息解耦，独立建模，以减少隐式辐射场的计算负担并加速重建。我们通过将高频颜色信息映射到这种紧凑的结构上，探索了三平面表示在少镜头NVS任务中的潜力，特征平面的直接优化显著加快了收敛速度。体积密度被建模为连续的密度场，通过基于图像的渲染结合来自相邻视图的参考特征，以补偿有限的输入数据。此外，我们引入了基于点云的深度引导优化，有效地缓解了少镜头NVS中的过拟合问题。跨多个遥感场景的综合实验表明，与基于NeRF的方法相比，我们的混合表示实现了30倍的速度提升，同时比先进的少镜头方法提高了渲染质量指标（PSNR提高了7.4%，SSIM提高了12.2%，LPIPS提高了18.7%）。该代码可在以下网址公开获取https://github.com/kanehub/TriDF et.al.|[2503.13347](http://arxiv.org/abs/2503.13347)|null|
|**2025-03-17**|**FlexWorld: Progressively Expanding 3D Scenes for Flexiable-View Synthesis**|由于缺乏3D数据，从单个图像生成灵活的视图3D场景（包括360度旋转和缩放）具有挑战性。为此，我们引入了FlexWorld，这是一个由两个关键组件组成的新框架：（1）一个强大的视频到视频（V2V）扩散模型，用于从粗略场景渲染的不完整输入中生成高质量的新视图图像，以及（2）一个渐进式扩展过程，用于构建完整的3D场景。特别是，利用先进的预训练视频模型和精确的深度估计训练对，我们的V2V模型可以在大的相机姿态变化下生成新的视图。在此基础上，FlexWorld逐步生成新的3D内容，并通过几何感知场景融合将其集成到全局场景中。广泛的实验证明了FlexWorld在从单个图像生成高质量新颖视图视频和灵活视图3D场景方面的有效性，与现有的最先进方法相比，在多种流行的指标和数据集下实现了卓越的视觉质量。从定性上讲，我们强调FlexWorld可以生成具有360度旋转和缩放等灵活视图的高保真场景。项目页面：https://ml-gsai.github.io/FlexWorld. et.al.|[2503.13265](http://arxiv.org/abs/2503.13265)|null|
|**2025-03-17**|**DivCon-NeRF: Generating Augmented Rays with Diversity and Consistency for Few-shot View Synthesis**|神经辐射场（NeRF）在新颖的视图合成中表现出了卓越的性能，但需要许多多视图图像，这使得它在少数拍摄场景中不切实际。提出了射线增强，通过生成额外的射线来防止稀疏训练数据的过拟合。然而，现有的方法仅在原始光线附近产生增强光线，由于视点有限和附近障碍物和复杂表面阻挡的光线不一致，会产生严重的漂浮物和外观失真。为了解决这些问题，我们提出了DivCon NeRF，它显著提高了多样性和一致性。它采用表面球体增强，保留了原始相机和预测表面点之间的距离。这使得模型能够比较高概率表面点的顺序，并轻松滤除不一致的光线，而不需要精确的深度。通过引入内球增强，DivCon NeRF随机化了不同视点的角度和距离，进一步增加了多样性。因此，我们的方法显著减少了浮点运算和视觉失真，在Blender、LLFF和DTU数据集上实现了最先进的性能。我们的代码将公开。 et.al.|[2503.12947](http://arxiv.org/abs/2503.12947)|null|
|**2025-03-17**|**AR-1-to-3: Single Image to Consistent 3D Object Generation via Next-View Prediction**|新颖视图合成（NVS）是图像到3d创建的基石。然而，现有的作品仍然难以保持生成的视图和输入视图之间的一致性，特别是在存在明显的相机姿态差异的情况下，导致质量较差的3D几何和纹理。根据我们的经验观察，我们将这个问题归因于他们同等重视所有目标视图，即更接近输入视图的目标视图表现出更高的保真度。基于这一启发，我们提出了AR-1-to-3，这是一种基于扩散模型的新的下一视图预测范式，首先生成接近输入视图的视图，然后将其用作上下文信息，逐步合成更远的视图。为了将生成的视图子序列编码为下一个视图预测的局部和全局条件，我们相应地开发了一种堆叠的局部特征编码策略（stacked LE）和一种基于LSTM的全局特征编码策略。大量实验表明，我们的方法显著提高了生成的视图和输入视图之间的一致性，产生了高保真的3D资产。 et.al.|[2503.12929](http://arxiv.org/abs/2503.12929)|null|
|**2025-03-17**|**CAT-3DGS Pro: A New Benchmark for Efficient 3DGS Compression**|3D高斯散斑（3DGS）在新型视图合成方面显示出巨大的潜力。然而，实现用于传输和/或存储应用的3DGS表示的率失真优化压缩仍然是一个挑战。CAT-3DGS引入了上下文自适应三平面超优先级，用于端到端优化压缩，提供了最先进的编码性能。尽管如此，它需要长时间的训练和解码时间。为了解决这些局限性，我们提出了CAT-3DGS Pro，这是CAT-3DGS的增强版本，可以提高压缩性能和计算效率。首先，我们引入了一个PCA引导的向量矩阵超优先级，它取代了基于三平面的超优先级，以减少冗余参数。为了实现更平衡的率失真权衡和更快的编码，我们提出了一种替代优化策略（a-RDO）。此外，我们改进了CAT-3DGS中的采样率优化方法，显著提高了率失真性能。这些增强功能使BungeeNeRF的BD速率降低了46.6%，训练时间提高了3倍，同时与CAT-3DGS相比，阿姆斯特丹场景的解码速度提高了5倍。 et.al.|[2503.12862](http://arxiv.org/abs/2503.12862)|null|
|**2025-03-17**|**CompMarkGS: Robust Watermarking for Compression 3D Gaussian Splatting**|3D高斯散斑（3DGS）能够实现快速可微分渲染，用于3D重建和新颖的视图合成，从而使其得到广泛的商业应用。因此，通过水印进行版权保护变得至关重要。然而，由于3DGS依赖于数百万高斯人，这需要千兆字节的存储空间，因此高效的传输和存储需要压缩。现有的3DGS水印方法容易受到基于量化的压缩，通常会导致嵌入的水印丢失。为了应对这一挑战，我们提出了一种新的水印方法，该方法在保持高渲染质量的同时，确保模型压缩后的水印鲁棒性。具体来说，我们引入了一个量化失真层，在训练过程中模拟压缩，在基于量化的压缩下保留水印。此外，我们提出了一种可学习的水印嵌入特征，将水印嵌入锚特征中，确保结构一致性和无缝集成到3D场景中。此外，我们提出了一种频率感知锚生长机制，通过有效识别高频区域内的高斯分布来提高这些区域的图像质量。实验结果证实，我们的方法保留了水印，并在高压缩下保持了优异的图像质量，验证了它是一种有前景的安全3DGS模型方法。 et.al.|[2503.12836](http://arxiv.org/abs/2503.12836)|null|
|**2025-03-16**|**Niagara: Normal-Integrated Geometric Affine Field for Scene Reconstruction from a Single View**|单视图3D场景重建的最新进展突显了捕捉精细几何细节和确保结构一致性的挑战，特别是在高保真室外场景建模中。本文介绍了Niagara，这是一种新的单视图3D场景重建框架，首次可以从单个输入图像中忠实地重建具有挑战性的室外场景。我们的方法将单眼深度和法线估计作为输入，大大提高了捕捉精细细节的能力，减轻了几何细节丢失和变形等常见问题。此外，我们引入了几何仿射场（GAF）和3D自关注作为几何约束，将显式几何的结构特性与隐式特征场的适应性相结合，在高效渲染和高保真重建之间取得了平衡。我们的框架最终提出了一种专门的编码器-解码器架构，其中提出了一个基于深度的3D高斯解码器来预测3D高斯参数，可用于新颖的视图合成。广泛的结果和分析表明，我们的Niagara在单视图和双视图设置中都超越了Flash3D等先前的SoTA方法，显著提高了几何精度和视觉保真度，特别是在室外场景中。 et.al.|[2503.12553](http://arxiv.org/abs/2503.12553)|**[link](https://github.com/xianzuwu/Niagara)**|
|**2025-03-16**|**MTGS: Multi-Traversal Gaussian Splatting**|多遍历数据通常通过日常通勤或自动驾驶车队收集，为街区内的场景重建提供了多个视角。这些数据为高质量的新颖视图合成提供了巨大的潜力，这对自动驾驶汽车模拟器等应用至关重要。然而，多重遍历数据中的固有挑战往往导致重建质量欠佳，包括外观变化和动态对象的存在。为了解决这些问题，我们提出了多遍历高斯散点（MTGS），这是一种新方法，通过对共享的静态几何体进行建模，同时分别处理动态元素和外观变化，从任意收集的多遍历数据中重建高质量的驾驶场景。我们的方法采用具有共享静态节点和遍历特定动态节点的多遍历动态场景图，辅以具有可学习球面谐波系数残差的颜色校正节点。这种方法实现了高保真度的新颖视图合成，并提供了导航任何视点的灵活性。我们在具有多遍历数据的大规模驾驶数据集nuPlan上进行了广泛的实验。我们的结果表明，与单次遍历基线相比，MTGS将LPIPS提高了23.5%，几何精度提高了46.3%。代码和数据将向公众开放。 et.al.|[2503.12552](http://arxiv.org/abs/2503.12552)|null|
|**2025-03-16**|**SPC-GS: Gaussian Splatting with Semantic-Prompt Consistency for Indoor Open-World Free-view Synthesis from Sparse Inputs**|基于3D高斯散斑的室内开放世界自由视图合成方法在密集输入图像中显示出显著的性能。然而，当面对稀疏输入时，它们表现出较差的性能，主要是由于高斯点的稀疏分布和视图监督不足。为了缓解这些挑战，我们提出了SPC-GS，利用基于场景布局的高斯初始化（SGI）和语义提示一致性（SPC）正则化进行稀疏输入的开放世界自由视图合成。具体来说，SGI通过利用视频生成模型生成的视图变化图像和视图约束高斯点密集化，提供了一种基于场景布局的密集高斯分布。此外，SPC通过采用SAM2开发的基于语义提示的一致性约束来减轻有限的视图监督。这种方法利用训练视图中的可用语义作为指导性提示，在具有2D和3D一致性约束的新视图中优化视觉重叠区域。广泛的实验证明了SPC-GS在Replica和ScanNet基准测试中的卓越性能。值得注意的是，我们的SPC-GS在重建质量方面实现了3.06 dB的PSNR增益，在开放世界语义分割方面实现了7.3%的mIoU改进。 et.al.|[2503.12535](http://arxiv.org/abs/2503.12535)|null|
|**2025-03-16**|**GS-3I: Gaussian Splatting for Surface Reconstruction from Illumination-Inconsistent Images**|精确的几何表面重建为导航和操纵任务提供了必要的环境信息，对于实现机器人的自我探索和交互至关重要。最近，3D高斯散斑（3DGS）因其令人印象深刻的几何质量和计算效率而在曲面重建领域受到了广泛关注。虽然最近使用3DGS在不一致光照下进行新型视图合成的相关进展显示出了希望，但在这种条件下进行鲁棒表面重建的挑战仍在探索中。为了应对这一挑战，我们提出了一种名为GS-3I的方法。具体来说，为了减轻单视图图像中曝光不足区域引起的3D高斯优化偏差，基于卷积神经网络（CNN），引入了一种色调映射校正框架。此外，由于相机设置和复杂场景照明的变化，多视图图像中的照明不一致，通常会导致重建表面的几何约束失配和偏差。为了克服这一点，我们提出了一种法线补偿机制，该机制将从单视图图像中提取的参考法线与从多视图观测中计算的法线相结合，以有效地约束几何不一致。广泛的实验评估表明，GS-3I可以在复杂的照明场景中实现稳健和准确的表面重建，突出了其在这一关键挑战中的有效性和多功能性。https://github.com/TFwang-9527/GS-3I et.al.|[2503.12335](http://arxiv.org/abs/2503.12335)|null|

<p align=right>(<a href=#updated-on-20250318>back to top</a>)</p>

## 3D Reconstruction

|Publish Date|Title|Abstract|PDF|Code|
|---|---|---|---|---|
|**2025-03-17**|**Amodal3R: Amodal 3D Reconstruction from Occluded 2D Images**|大多数基于图像的3D对象重建器都假设对象是完全可见的，忽略了现实世界场景中常见的遮挡。本文介绍了Amodal3R，这是一种用于从部分观测中重建3D对象的条件3D生成模型。我们从一个“基础”3D生成模型开始，并对其进行扩展，以从被遮挡的对象中恢复出合理的3D几何和外观。我们引入了一种掩模加权多头交叉注意力机制，随后是一个遮挡感知注意力层，该层明确利用遮挡先验来指导重建过程。我们证明，通过仅在合成数据上进行训练，Amodal3R即使在真实场景中存在遮挡的情况下也能学习恢复完整的3D对象。它大大优于独立执行2D amodal完成然后进行3D重建的现有方法，从而为遮挡感知3D重建建立了一个新的基准。 et.al.|[2503.13439](http://arxiv.org/abs/2503.13439)|null|
|**2025-03-17**|**WideRange4D: Enabling High-Quality 4D Reconstruction with Wide-Range Movements and Scenes**|随着3D重建技术的快速发展，4D重建的研究也在不断推进，现有的4D重建方法可以生成高质量的4D场景。然而，由于获取多视图视频数据的挑战，目前的4D重建基准主要显示在有限场景内就地执行的动作，如跳舞。在实际场景中，许多场景涉及大范围的空间运动，突显了现有4D重建数据集的局限性。此外，现有的4D重建方法依赖于变形场来估计3D对象的动态，但变形场难以应对宽范围的空间运动，这限制了实现具有宽范围空间运动的高质量4D场景重建的能力。在本文中，我们专注于具有显著对象空间运动的4D场景重建，并提出了一种新的4D重建基准WideRange4D。该基准包括具有较大空间变化的丰富4D场景数据，可以更全面地评估4D生成方法的生成能力。此外，我们介绍了一种新的4D重建方法Progress4D，它可以在各种复杂的4D场景重建任务中生成稳定和高质量的4D结果。我们在WideRange4D上进行了定量和定性比较实验，表明我们的Progress4D优于现有的最先进的4D重建方法。项目：https://github.com/Gen-Verse/WideRange4D et.al.|[2503.13435](http://arxiv.org/abs/2503.13435)|null|
|**2025-03-17**|**AugMapNet: Improving Spatial Latent Structure via BEV Grid Augmentation for Enhanced Vectorized Online HD Map Construction**|自动驾驶需要了解基础设施要素，如车道和人行横道。为了安全导航，这种理解必须实时从传感器数据中得出，并需要以矢量化形式表示。学习型鸟瞰图（BEV）编码器通常用于将来自多个视图的一组相机图像组合成一个联合的潜在BEV网格。传统上，从这个潜在空间预测中间光栅地图，提供密集的空间监督，但需要后处理成所需的矢量化形式。最近的模型使用矢量化地图解码器直接将基础设施元素导出为折线，提供实例级信息。我们的方法，增强图网络（AugMapNet），提出了潜在的BEV网格增强，这是一种显著增强潜在BEV表示的新技术。AugMapNet比现有架构更有效地结合了矢量解码和密集空间监督，同时保持了与辅助监督一样易于集成和通用的特点。在nuScenes和Argoverse2数据集上的实验表明，矢量化地图预测性能在60米范围内比StreamMapNet基线提高了13.3%，在更大范围内提高了更大的性能。我们通过将我们的方法应用于另一个基线来确认可转移性，并发现了类似的改进。对潜在BEV网格的详细分析证实了AugMapNet更结构化的潜在空间，并展示了我们的新概念在纯粹性能改进之外的价值。代码很快就会发布。 et.al.|[2503.13430](http://arxiv.org/abs/2503.13430)|null|
|**2025-03-17**|**DeGauss: Dynamic-Static Decomposition with Gaussian Splatting for Distractor-free 3D Reconstruction**|从真实世界的捕捉中重建干净、无干扰的3D场景仍然是一个重大挑战，特别是在高度动态和混乱的环境中，如以自我为中心的视频。为了解决这个问题，我们引入了DeGauss，这是一种基于解耦动态静态高斯散斑设计的简单而鲁棒的动态场景重建自监督框架。DeGauss使用前景高斯模型对动态元素进行建模，使用背景高斯模型对静态内容进行建模，并使用概率掩模来协调它们的组成，从而实现独立但互补的优化。DeGauss在广泛的现实世界场景中具有鲁棒性，从随意的图像收集到长而动态的以自我为中心的视频，而不依赖于复杂的启发式或广泛的监督。包括NeRF on the go、ADT、AEA、Hot3D和EPIC Fields在内的基准测试表明，DeGauss始终优于现有方法，为高度动态、交互丰富的环境中的通用、无干扰的3D重建建立了强有力的基线。 et.al.|[2503.13176](http://arxiv.org/abs/2503.13176)|null|
|**2025-03-17**|**CompMarkGS: Robust Watermarking for Compression 3D Gaussian Splatting**|3D高斯散斑（3DGS）能够实现快速可微分渲染，用于3D重建和新颖的视图合成，从而使其得到广泛的商业应用。因此，通过水印进行版权保护变得至关重要。然而，由于3DGS依赖于数百万高斯人，这需要千兆字节的存储空间，因此高效的传输和存储需要压缩。现有的3DGS水印方法容易受到基于量化的压缩，通常会导致嵌入的水印丢失。为了应对这一挑战，我们提出了一种新的水印方法，该方法在保持高渲染质量的同时，确保模型压缩后的水印鲁棒性。具体来说，我们引入了一个量化失真层，在训练过程中模拟压缩，在基于量化的压缩下保留水印。此外，我们提出了一种可学习的水印嵌入特征，将水印嵌入锚特征中，确保结构一致性和无缝集成到3D场景中。此外，我们提出了一种频率感知锚生长机制，通过有效识别高频区域内的高斯分布来提高这些区域的图像质量。实验结果证实，我们的方法保留了水印，并在高压缩下保持了优异的图像质量，验证了它是一种有前景的安全3DGS模型方法。 et.al.|[2503.12836](http://arxiv.org/abs/2503.12836)|null|
|**2025-03-17**|**ProtoDepth: Unsupervised Continual Depth Completion with Prototypes**|我们提出了ProtoDepth，这是一种基于原型的无监督深度完成连续学习的新方法，是一种从RGB图像和稀疏点云中预测密集深度图的多模态3D重建任务。无监督学习范式非常适合持续学习，因为不需要基础知识。然而，当对新的非平稳分布进行训练时，深度完成模型将灾难性地忘记之前学习到的信息。我们通过学习原型集来解决遗忘问题，这些原型集使冻结的预训练模型的潜在特征适应新的领域。由于原始权重未被修改，ProtoDepth不会忘记何时知道测试时域身份。为了将ProtoDepth扩展到测试时域身份被保留的具有挑战性的设置，我们建议学习域描述符，使模型能够选择合适的原型集进行推理。我们在基准数据集序列上评估了ProtoDepth，与基线相比，室内遗忘减少了52.2%，室外遗忘减少了53.2%，达到了最先进的水平。 et.al.|[2503.12745](http://arxiv.org/abs/2503.12745)|null|
|**2025-03-15**|**Multi-slice beam propagation method for imaging multiple-scattering samples on reflective substrates**|衍射层析成像（DT）在透射模式配置中得到了广泛的探索，实现了高分辨率、无标记的3D成像。然而，由于强烈的基板反射和复杂的多重散射效应，将DT应用于反射模式测量带来了重大挑战，特别是在计量和工业检测应用中。在这项工作中，我们介绍了反射模式傅里叶成像断层扫描（rFPT），它实现了反射基板上多层强散射样品的高分辨率、体积成像。我们开发了一种反射模式多层光束传播方法（rMBSP）来模拟多重散射和基底相互作用，从而实现精确的3D重建。通过结合暗场测量，rFPT提高了分辨率，超越了传统的明场极限，并在实现光学切片的同时提供了亚微米的横向分辨率。我们通过在四层分辨率目标上的数值模拟和使用反射模式LED阵列显微镜的实验演示来验证rFPT。在两层分辨率目标和多层散射样品上的实验证实了该方法的有效性。我们的优化实现实现了快速成像，在1.6秒内覆盖1.2毫米×1.2毫米的区域，在0.4毫米×3美元的体积内重建超过10^9美元的体素。这项工作代表了将DT扩展到反射模式配置的重要一步，为3D计量和工业检测提供了一个强大且可扩展的解决方案。 et.al.|[2503.12246](http://arxiv.org/abs/2503.12246)|null|
|**2025-03-15**|**VTON 360: High-Fidelity Virtual Try-On from Any Viewing Direction**|Virtual Try On（VTON）是电子商务和时装设计领域的一项变革性技术，能够实现个人服装的逼真数字可视化。在这项工作中，我们提出了VTON 360，这是一种新颖的3D VTON方法，解决了实现支持任何视图渲染的高保真VTON的开放挑战。具体来说，我们利用了3D模型与其渲染的多视图2D图像之间的等效性，并将3D VTON重新表述为2D VTON的扩展，以确保跨多个视图的3D一致结果。为了实现这一点，我们扩展了2D VTON模型，将多视图服装和与服装无关的人体图像作为输入，并提出了几种增强它们的新技术，包括：i）使用从SMPL-X 3D人体模型导出的法线图的伪3D姿势表示，ii）对不同视角的特征之间的相关性进行建模的多视图空间注意力机制，以及iii）使用相机信息增强2D VTON中使用的服装CLIP特征的多视图CLIP嵌入。对来自电子商务平台的大规模真实数据集和服装图像进行的广泛实验证明了我们方法的有效性。项目页面：https://scnuhealthy.github.io/VTON360. et.al.|[2503.12165](http://arxiv.org/abs/2503.12165)|null|
|**2025-03-15**|**3D Gaussian Splatting against Moving Objects for High-Fidelity Street Scene Reconstruction**|动态街道场景的精确重建对于自动驾驶、增强现实和虚拟现实的应用至关重要。依赖密集点云和三角形网格的传统方法难以应对移动物体、遮挡和实时处理约束，限制了它们在复杂城市环境中的有效性。虽然多视图立体和神经辐射场具有先进的3D重建技术，但它们在计算效率和处理场景动力学方面面临挑战。本文提出了一种新的用于动态街道场景重建的3D高斯点分布方法。我们的方法引入了一种自适应透明度机制，在保留高保真静态场景细节的同时消除了运动对象。此外，高斯点分布的迭代细化提高了几何精度和纹理表示。我们将方向编码与空间位置优化相结合，以优化存储和渲染效率，在保持场景完整性的同时减少冗余。实验结果表明，我们的方法实现了高重建质量、改进的渲染性能和在大规模动态环境中的适应性。这些贡献为实时、高精度的3D重建建立了一个强大的框架，提高了动态场景建模在多个应用程序中的实用性。这项工作的源代码可在以下网址向公众开放：https://github.com/deepcoxcom/3dgs et.al.|[2503.12001](http://arxiv.org/abs/2503.12001)|null|
|**2025-03-14**|**Bring Your Rear Cameras for Egocentric 3D Human Pose Estimation**|使用安装在头戴式设备（HMD）前的摄像头，对以自我为中心的3D人体姿态估计进行了积极的研究。虽然正面放置是某些任务（如手部跟踪）的最佳和唯一选择，但由于自遮挡和有限的视野覆盖，目前尚不清楚全身跟踪是否也是如此。值得注意的是，在许多情况下，即使是最先进的方法也往往无法准确估计3D姿势，例如当HMD用户向上倾斜头部时（人类活动中常见的运动）。现有头戴式显示器设计的一个关键局限性是忽略了身体后部，尽管它有可能提供关键的3D重建线索。因此，本文研究了后置摄像头在HMD全身跟踪设计中的有用性。我们还表明，对于现有的方法来说，简单地将后视图添加到正面输入中并不是最优的，因为它们依赖于单个2D联合检测器，而没有有效的多视图集成。为了解决这个问题，我们提出了一种新的基于变换器的方法，该方法利用多视图信息和热图不确定性来改进二维联合热图估计，从而改善三维姿态跟踪。此外，我们引入了两个新的大规模数据集，Ego4View Syn和Ego4View-RW，用于后视评估。我们的实验表明，与仅正面放置相比，具有后视图的新相机配置为3D姿态跟踪提供了更优的支持。所提出的方法实现了对当前技术水平的显著改进（在MPJPE上>10%）。我们将在项目页面上发布源代码、训练模型和新数据集https://4dqv.mpi-inf.mpg.de/EgoRear/. et.al.|[2503.11652](http://arxiv.org/abs/2503.11652)|null|

<p align=right>(<a href=#updated-on-20250318>back to top</a>)</p>

## Diffusion

|Publish Date|Title|Abstract|PDF|Code|
|---|---|---|---|---|
|**2025-03-17**|**BlobCtrl: A Unified and Flexible Framework for Element-level Image Generation and Editing**|元素级视觉操作在数字内容创作中至关重要，但目前基于扩散的方法缺乏传统工具的准确性和灵活性。在这项工作中，我们介绍了BlobCtrl，这是一个使用基于概率blob的表示统一元素级生成和编辑的框架。通过使用blob作为视觉原语，我们的方法有效地解耦并表示了空间位置、语义内容和身份信息，从而实现了精确的元素级操作。我们的主要贡献包括：1）一种具有层次特征融合的双分支扩散架构，用于无缝的前景-背景集成；2） 具有定制数据增强和评分函数的自我监督训练范式；以及3）可控的丢弃策略，以平衡保真度和多样性。为了支持进一步的研究，我们引入了用于大规模训练的BlobData和用于系统评估的BlobBench。实验表明，BlobCtrl在各种元素级操作任务中表现出色，同时保持了计算效率，为精确灵活的视觉内容创建提供了一种实用的解决方案。项目页面：https://liyaowei-stu.github.io/project/BlobCtrl/ et.al.|[2503.13434](http://arxiv.org/abs/2503.13434)|null|
|**2025-03-17**|**SyncDiff: Diffusion-based Talking Head Synthesis with Bottlenecked Temporal Visual Prior for Improved Synchronization**|说话头合成，也称为语音到嘴唇合成，重建与给定音轨对齐的面部运动。合成视频主要从嘴唇语音同步和图像保真度两个方面进行评估。最近的研究表明，基于GAN和基于扩散的模型在这项任务中实现了最先进的（SOTA）性能，基于扩散的模式实现了卓越的图像保真度，但与基于GAN的模型相比，其同步性较低。为此，我们提出了SyncDiff，这是一种简单而有效的方法，可以使用具有信息瓶颈的时间姿态帧和从AVHuBERT中提取的面部信息音频特征来改进基于扩散的模型，作为扩散过程的条件输入。我们在两个典型的说话头数据集LRS2和LRS3上评估SyncDiff，以便与其他SOTA模型进行直接比较。在LRS2/LRS3数据集上的实验表明，SyncDiff的同步得分比以前的基于扩散的方法高27.7%/62.3%，同时保持了它们的高保真特性。 et.al.|[2503.13371](http://arxiv.org/abs/2503.13371)|null|
|**2025-03-17**|**One-Step Residual Shifting Diffusion for Image Super-Resolution via Distillation**|超分辨率（SR）的扩散模型可以产生高质量的视觉结果，但需要昂贵的计算成本。尽管已经开发了几种加速基于扩散的SR模型的方法，但有些（如SinSR）无法产生逼真的感知细节，而另一些（如OSEDiff）可能会产生不存在的结构的幻觉。为了克服这些问题，我们提出了RSD，这是ResShift的一种新的蒸馏方法，ResShift是基于扩散的SR模型之一。我们的方法基于训练学生网络来生成这样的图像，即在这些图像上训练的新的假ResShift模型将与教师模型相吻合。RSD实现了单步恢复，远远优于教师。我们证明，我们的蒸馏方法可以超越其他基于蒸馏的ResShift-SinSR方法，使其与最先进的基于扩散的SR蒸馏方法相媲美。与基于预训练文本到图像模型的SR方法相比，RSD产生了具有竞争力的感知质量，为退化的输入图像提供了更好的对齐，并且需要更少的参数和GPU内存。我们提供各种真实世界和合成数据集的实验结果，包括RealSR、RealSet65、DRealSR、ImageNet和DIV2K。 et.al.|[2503.13358](http://arxiv.org/abs/2503.13358)|null|
|**2025-03-17**|**MagicDistillation: Weak-to-Strong Video Distillation for Large-Scale Portrait Few-Step Synthesis**|为肖像视频合成任务微调开源大规模VDM可以在多个维度上实现显著改善，例如视觉质量和自然面部运动动态。尽管他们取得了进步，但如何实现分步蒸馏并减少大规模VDM的大量计算开销仍有待探索。为了填补这一空白，本文提出了弱到强视频蒸馏（W2SVD），以缓解训练记忆不足的问题和训练过程中香草DMD中观察到的训练崩溃问题。具体来说，我们首先利用LoRA来微调伪扩散变换器（DiT），以解决内存不足的问题。然后，我们采用W2S分布匹配来调整真实DiT的参数，巧妙地将其移向假DiT参数。这种调整是通过利用低秩分支的弱权重来实现的，有效地缓解了由少步生成器合成的视频偏离真实数据分布，导致KL散度近似不准确的难题。此外，我们最小化了假数据分布和地面真实分布之间的距离，以进一步提高合成视频的视觉质量。正如在浑源视频上的实验所证明的那样，W2SVD在1/4步视频合成中超过了标准Euler、LCM、DMD，甚至超过了FID/FVD和VBench中的28步标准采样。项目页面位于https://w2svd.github.io/W2SVD/. et.al.|[2503.13319](http://arxiv.org/abs/2503.13319)|null|
|**2025-03-17**|**Generative Gaussian Splatting: Generating 3D Scenes with Video Diffusion Priors**|合成一致且逼真的3D场景是计算机视觉领域的一个悬而未决的问题。视频扩散模型生成令人印象深刻的视频，但不能直接合成3D表示，即生成的序列缺乏3D一致性。此外，由于缺乏大规模的3D训练数据，直接训练生成性3D模型具有挑战性。在这项工作中，我们提出了生成高斯散斑（GGS）——一种将3D表示与预训练的潜在视频扩散模型相结合的新方法。具体来说，我们的模型合成了一个通过3D高斯基元参数化的特征场。然后，特征场被渲染为特征图并解码为多视图图像，或者直接上采样为3D辐射场。我们在场景合成的两个常见基准数据集RealEstate10K和ScanNet+上评估了我们的方法，发现我们提出的GGS模型显著提高了生成的多视图图像的3D一致性，以及在所有相关基线上生成的3D场景的质量。与没有3D表示的类似模型相比，GGS在RealEstate10K和ScanNet+上将生成的3D场景的FID提高了约20%。项目页面：https://katjaschwarz.github.io/ggs/ et.al.|[2503.13272](http://arxiv.org/abs/2503.13272)|null|
|**2025-03-17**|**FlexWorld: Progressively Expanding 3D Scenes for Flexiable-View Synthesis**|由于缺乏3D数据，从单个图像生成灵活的视图3D场景（包括360度旋转和缩放）具有挑战性。为此，我们引入了FlexWorld，这是一个由两个关键组件组成的新框架：（1）一个强大的视频到视频（V2V）扩散模型，用于从粗略场景渲染的不完整输入中生成高质量的新视图图像，以及（2）一个渐进式扩展过程，用于构建完整的3D场景。特别是，利用先进的预训练视频模型和精确的深度估计训练对，我们的V2V模型可以在大的相机姿态变化下生成新的视图。在此基础上，FlexWorld逐步生成新的3D内容，并通过几何感知场景融合将其集成到全局场景中。广泛的实验证明了FlexWorld在从单个图像生成高质量新颖视图视频和灵活视图3D场景方面的有效性，与现有的最先进方法相比，在多种流行的指标和数据集下实现了卓越的视觉质量。从定性上讲，我们强调FlexWorld可以生成具有360度旋转和缩放等灵活视图的高保真场景。项目页面：https://ml-gsai.github.io/FlexWorld. et.al.|[2503.13265](http://arxiv.org/abs/2503.13265)|null|
|**2025-03-17**|**Anatomically and Metabolically Informed Diffusion for Unified Denoising and Segmentation in Low-Count PET Imaging**|正电子发射断层扫描（PET）图像去噪以及病变和器官分割是PET辅助诊断的关键步骤。然而，现有的方法通常独立处理这些任务，忽略了它们之间作为分析管道中相关步骤的内在协同作用。在这项工作中，我们提出了解剖学和代谢信息扩散（AMDiff）模型，这是一个用于低计数PET成像中去噪和病变/器官分割的统一框架。通过整合多任务功能并利用这些任务的互惠互利，AMDiff能够从低计数输入中直接量化临床指标，如总损伤糖酵解（TLG）。AMDiff模型结合了基于扩散策略的语义知情去噪器和利用nnMamba架构的去噪知情分割器。分割器通过病变器官特异性正则化器约束去噪输出，而去噪器通过去噪修正模块提供丰富的图像信息来增强分割器。这些组件通过预热机制连接，以优化多任务交互。在多供应商、多中心和多噪声级数据集上的实验证明了AMDiff的优越性能。对于参与部位临床计数水平低于20%的测试病例，AMDiff的TLG量化偏差为-26.98%，优于其消融版本，消融版本的偏差为-35.85%（没有病变器官特异性正则化器）和-40.79%（没有去噪修正模块）。 et.al.|[2503.13257](http://arxiv.org/abs/2503.13257)|null|
|**2025-03-17**|**HoloGest: Decoupled Diffusion and Motion Priors for Generating Holisticly Expressive Co-speech Gestures**|用整体同音手势为虚拟角色制作动画是一项具有挑战性但至关重要的任务。以前的系统主要关注音频和手势之间的弱相关性，导致物理上不自然的结果，从而降低用户体验。为了解决这个问题，我们引入了HoleGest，这是一种基于解耦扩散和运动先验的新型神经网络框架，用于自动生成高质量、富有表现力的同音手势。我们的系统利用大规模的人体运动数据集来学习具有低音频依赖性和高运动依赖性的鲁棒先验，从而实现稳定的全局运动和详细的手指运动。为了提高基于扩散的模型的生成效率，我们将隐式联合约束与显式几何和条件约束相结合，捕捉大步之间的复杂运动分布。这种集成显著提高了生成速度，同时保持了高质量的运动。此外，我们设计了一个共享的嵌入空间用于手势转录文本对齐，从而能够生成语义正确的手势动作。大量的实验和用户反馈证明了我们模型的有效性和潜在应用，我们的方法实现了接近地面真实的真实感，提供了身临其境的用户体验。我们的代码、模型和演示可在https://cyk990422.github.io/HoloGest.github.io/. et.al.|[2503.13229](http://arxiv.org/abs/2503.13229)|null|
|**2025-03-17**|**MedLoRD: A Medical Low-Resource Diffusion Model for High-Resolution 3D CT Image Synthesis**|医学成像人工智能的进步提供了巨大的潜力。然而，它们的应用受到数据可用性有限以及医疗中心出于患者隐私考虑不愿共享数据的限制。生成模型通过创建合成数据作为真实患者数据的替代品，提供了一种有前景的解决方案。然而，医学图像通常是高维的，目前最先进的方法对于计算资源受限的医疗环境来说往往不切实际。这些模型依赖于数据子采样，这引发了人们对其可行性和现实世界适用性的怀疑。此外，这些模型中的许多都是根据定量指标进行评估的，这些指标在评估生成图像的图像质量和临床意义时可能会产生误导。为了解决这个问题，我们引入了MedLoRD，这是一种为计算资源受限环境设计的生成扩散模型。MedLoRD能够生成分辨率高达512美元×512美元×256美元的高维医学卷，利用仅具有24GB VRAM的GPU，这在标准台式工作站中很常见。MedLoRD在多种模式下进行评估，包括冠状动脉计算机断层扫描血管造影和肺计算机断层扫描数据集。通过放射学评估、相对区域体积分析、遵守条件掩模和下游任务进行的广泛评估表明，MedLoRD生成的高保真图像严格遵守分割掩模条件，在计算资源受限的环境中超过了当前最先进的医学图像合成生成模型的能力。 et.al.|[2503.13211](http://arxiv.org/abs/2503.13211)|null|
|**2025-03-17**|**The Lyman alpha Sky as Observed by New Horizons**|2023年9月，新视野号（NH）航天器上的爱丽丝紫外光谱仪被用来绘制距离太阳56.9天文单位的大部分天空上的弥漫莱曼-阿尔法（Lya）发射图。在这个距离上，模型预测，行星际介质Lya排放是由穿过太阳系的星际氢原子（HI）对太阳Lya线的相当数量的共振后向散射引起的，此外还有来自局部恒星间介质（LISM）的30-70R的近似各向同性背景。NH观测表明，与LISM附近的云结构或日光层的预期结构（如与日球层顶相关的氢墙）没有很强的相关性。为了解释LISM的相对明亮和均匀的Lya，我们提出，局部热泡（LHB）内的炽热年轻恒星照射在其内壁上，在那里光致电离HI原子。在通过共振散射放大扩散Lya后，这些离子的重组可以解释观察到的50R Lya背景，尽管应该使用复杂的（即3-D）辐射传输模型来证实这一猜想。未来使用能够解析线轮廓的仪器对漫射Lya进行观测，可以为LISM和日光层中的HI种群提供一个新的窗口。如果资源允许，这里提出的NH Alice全天空Lya观测结果可能会在未来的某个时候重复，并且这两张地图可以结合起来，大大提高角分辨率。 et.al.|[2503.13182](http://arxiv.org/abs/2503.13182)|null|

<p align=right>(<a href=#updated-on-20250318>back to top</a>)</p>

## NeRF

|Publish Date|Title|Abstract|PDF|Code|
|---|---|---|---|---|
|**2025-03-14**|**NF-SLAM: Effective, Normalizing Flow-supported Neural Field representations for object-level visual SLAM in automotive applications**|我们提出了一种新颖的、仅限视觉的对象级SLAM框架，用于通过隐式符号距离函数表示3D形状的汽车应用。我们的主要创新包括通过归一化流网络增强标准神经表示。因此，通过仅具有16维潜码的紧凑网络，可以在特定类别的道路车辆上实现强大的表示能力。此外，通过对合成数据的比较实验证明，新提出的架构在仅存在稀疏和噪声数据的情况下表现出显著的性能改进。该模块嵌入到基于立体视觉的框架的后端，用于联合增量形状优化。损失函数由基于稀疏3D点的SDF损失、稀疏渲染损失和基于语义掩码的轮廓一致性项的组合给出。我们还利用语义信息来确定前端的关键点提取密度。最后，对真实世界数据的实验结果显示，与使用直接深度读数的替代框架相比，其性能准确可靠。所提出的方法仅在通过束调整获得的稀疏3D点上表现良好，即使在仅使用掩模一致性项的情况下，最终也能继续提供稳定的结果。 et.al.|[2503.11199](http://arxiv.org/abs/2503.11199)|null|
|**2025-03-13**|**RSR-NF: Neural Field Regularization by Static Restoration Priors for Dynamic Imaging**|动态成像涉及使用欠采样测量值随时重建时空对象。特别是，在动态计算机断层扫描（dCT）中，一次只能获得一个视角的单个投影，这使得逆问题非常具有挑战性。此外，地面实况动态数据通常要么不可用，要么太稀缺，无法用于监督学习技术。为了解决这个问题，我们提出了RSR-NF，它使用神经场（NF）来表示动态对象，并使用去噪正则化（RED）框架，通过学习的恢复算子将额外的静态深空间先验合并到变分公式中。我们使用基于ADMM的可变分裂算法来有效地优化变分目标。我们将RSR-NF与三种替代方案进行了比较：仅具有时间正则化的NF；最近的一种方法，使用对静态数据进行预训练的去噪器，将部分可分离的低秩表示与RED相结合；以及基于深度图像先验的模型。第一个比较展示了通过将NF表示与静态恢复先验相结合所实现的重建改进，而另外两个则展示了与dCT的最新技术相比的改进。 et.al.|[2503.10015](http://arxiv.org/abs/2503.10015)|null|
|**2025-03-11**|**Representing 3D Shapes With 64 Latent Vectors for 3D Diffusion Models**|通过变分自编码器（VAE）构建压缩的潜在空间是高效3D扩散模型的关键。本文介绍了COD-VAE，这是一种在不牺牲质量的情况下将3D形状编码为1D潜在向量的COmpact集的VAE。COD-VAE引入了一种两级自动编码器方案，以提高压缩和解码效率。首先，我们的编码器块通过中间点补丁将点云逐步压缩为紧凑的潜在向量。其次，我们的基于三平面的解码器从潜在向量重建密集的三平面，而不是直接解码神经场，大大降低了神经场解码的计算开销。最后，我们提出了不确定性引导的令牌修剪，通过在更简单的区域跳过计算来自适应地分配资源，提高了解码器的效率。实验结果表明，与基线相比，COD-VAE在保持质量的同时实现了16倍的压缩。这使得生成速度提高了20.8倍，突显出大量潜在矢量不是高质量重建和生成的先决条件。 et.al.|[2503.08737](http://arxiv.org/abs/2503.08737)|null|
|**2025-03-09**|**Gaussian RBFNet: Gaussian Radial Basis Functions for Fast and Accurate Representation and Reconstruction of Neural Fields**|DeepSDF和神经辐射场等神经场最近彻底改变了RGB图像和视频的新颖视图合成和3D重建。然而，实现高质量的表示、重建和渲染需要深度神经网络，而深度神经网络的训练和评估速度很慢。尽管已经提出了几种加速技术，但它们经常以速度换取内存。另一方面，基于高斯飞溅的方法加快了渲染时间，但在存储大量高斯参数所需的训练速度和内存方面仍然成本高昂。在本文中，我们介绍了一种新的神经表示方法，它在训练和推理时间都很快，而且很轻。我们的关键观察是，传统MLP中使用的神经元执行简单的计算（点积，然后是ReLU激活），因此需要使用宽和深MLP或高分辨率和高维特征网格来参数化复杂的非线性函数。我们在这篇论文中表明，通过用径向基函数（RBF）核替换传统神经元，只需一层这样的神经元，就可以实现2D（RGB图像）、3D（几何）和5D（辐射场）信号的高精度表示。该表示具有高度的并行性，可在低分辨率特征网格上运行，并且结构紧凑，内存高效。我们证明，所提出的新表示可以在不到15秒的时间内训练出3D几何表示，在不到十五分钟的时间内就可以训练出新的视图合成。在运行时，它可以在不牺牲质量的情况下以超过60 fps的速度合成新颖的视图。 et.al.|[2503.06762](http://arxiv.org/abs/2503.06762)|null|
|**2025-03-09**|**X-LRM: X-ray Large Reconstruction Model for Extremely Sparse-View Computed Tomography Recovery in One Second**|稀疏视图3D CT重建旨在从有限数量的2D X射线投影中恢复体积结构。现有的前馈方法受到基于CNN的架构容量有限和大规模训练数据集稀缺的限制。本文提出了一种用于极稀疏视图（<10视图）CT重建的X射线大重建模型（X-LRM）。X-LRM由两个关键部件组成：X-former和X-triplane。我们的X-former可以使用基于MLP的图像标记器和基于Transformer的编码器来处理任意数量的输入视图。然后，输出标记被上采样到我们的X三平面表示中，该表示将3D辐射密度建模为隐式神经场。为了支持X-LRM的训练，我们引入了Torso-16K，这是一个由各种躯干器官的16K多个体积投影对组成的大规模数据集。大量实验表明，X-LRM的性能比最先进的方法高出1.5 dB，速度快27倍，灵活性更好。此外，肺部分割任务的下游评估也表明了我们方法的实用价值。我们的代码、预训练模型和数据集将于https://github.com/caiyuanhao1998/X-LRM et.al.|[2503.06382](http://arxiv.org/abs/2503.06382)|null|
|**2025-03-05**|**Distilling Dataset into Neural Field**|利用大规模数据集对于训练高性能深度学习模型至关重要，但它也带来了巨大的计算和存储成本。为了克服这些挑战，数据集蒸馏已成为一种有前景的解决方案，它将大规模数据集压缩成一个较小的合成数据集，保留了训练所需的基本信息。本文提出了一种新的数据集提取参数化框架，称为神经场提取数据集（DDiF），它利用神经场存储大规模数据集的必要信息。由于神经场以坐标作为输入和输出量的独特性质，DDiF有效地保留了信息，并易于生成各种形状的数据。我们从理论上证实，当单个合成实例的使用预算相同时，DDiF表现出比以前的一些文献更大的表现力。通过广泛的实验，我们证明DDiF在几个基准数据集上取得了卓越的性能，扩展到图像域之外，包括视频、音频和3D体素。我们在发布代码https://github.com/aailab-kaist/DDiF. et.al.|[2503.04835](http://arxiv.org/abs/2503.04835)|**[link](https://github.com/aailab-kaist/ddif)**|
|**2025-02-27**|**RANGE: Retrieval Augmented Neural Fields for Multi-Resolution Geo-Embeddings**|地理位置表示的选择会显著影响各种地理空间任务模型的准确性，包括细粒度物种分类、种群密度估计和生物群落分类。最近的作品，如SatCLIP和GeoCLIP，通过将地理位置与共置图像进行对比对齐来学习这种表示。虽然这些方法非常有效，但在本文中，我们认为当前的训练策略未能完全捕捉到重要的视觉特征。我们从信息论的角度解释了为什么这些方法产生的嵌入会丢弃对许多下游任务很重要的关键视觉信息。为了解决这个问题，我们提出了一种新的检索增强策略，称为RANGE。我们的方法基于这样一种直觉，即可以通过组合来自多个看起来相似的位置的视觉特征来估计位置的视觉特性。我们在各种各样的任务中评估我们的方法。我们的结果表明，RANGE在大多数任务中表现优于现有的最先进的模型，并具有显著的优势。我们显示，分类任务的收益高达13.1%，回归任务的收益为0.145 $R^2$ 。我们所有的代码都将在GitHub上发布。我们的模型将在HuggingFace上发布。 et.al.|[2502.19781](http://arxiv.org/abs/2502.19781)|null|
|**2025-03-04**|**MedFuncta: Modality-Agnostic Representations Based on Efficient Neural Fields**|最近关于深度学习医学图像分析的研究几乎完全集中在基于网格或体素的数据表示上。我们通过引入MedFuncta来挑战这一常见选择，MedFuncta是一种基于神经场的模态无关连续数据表示。我们演示了如何通过利用医学信号中的冗余以及应用具有上下文缩减方案的高效元学习方法，将神经场从单个实例扩展到大型数据集。我们通过引入 $\omega_0$ -调度，提高重建质量和收敛速度，进一步解决了常用SIREN激活中的光谱偏差问题。我们在各种不同维度和模式的医学信号上验证了我们提出的方法（1D：心电图；2D：胸部X射线、视网膜OCT、眼底照相机、皮肤镜、结肠组织病理学、细胞显微镜；3D：脑MRI、肺CT），并成功证明我们可以解决这些表示的相关下游任务。我们还发布了一个超过550k个带注释神经场的大规模数据集，以促进这方面的研究。 et.al.|[2502.14401](http://arxiv.org/abs/2502.14401)|**[link](https://github.com/pfriedri/medfuncta)**|
|**2025-02-15**|**Implicit Neural Representations of Molecular Vector-Valued Functions**|分子有各种计算表示，包括数值描述符、字符串、图形、点云和曲面。每种表示方法都可以应用各种机器学习方法，从线性回归到与大型语言模型配对的图神经网络。为了补充现有的表示，我们通过向量值函数或n维向量场引入分子的表示，这些向量值函数由神经网络参数化，我们称之为分子神经场。与表面表征不同，分子神经场捕获蛋白质等大分子的外部特征和疏水核心。与离散图或点表示相比，分子神经场结构紧凑，分辨率无关，天生适合在空间和时间维度上进行插值。分子神经场继承的这些特性适用于包括基于所需形状、结构和组成生成分子，以及空间和时间中分子构象之间分辨率无关的插值在内的任务。在这里，我们为分子神经场提供了一个框架和概念证明，即使用自动解码器架构对蛋白质-配体复合物进行参数化和超分辨率重建，以及使用自动编码器架构将分子体积嵌入潜在空间。 et.al.|[2502.10848](http://arxiv.org/abs/2502.10848)|**[link](https://github.com/daenuprobst/minf)**|
|**2025-02-05**|**Poisson Hypothesis and large-population limit for networks of spiking neurons**|我们研究了具有随机尖峰时间的线性（泄漏）和二次积分和放电神经元的空间扩展网络的平均场描述。我们考虑了具有线性和二次内在动力学的连续时间Galves-L“ocherbach（GL）网络的大种群极限。我们证明了泊松假设适用于这些网络的复制平均场极限，即在适当定义的极限内，神经元是独立的，相互作用时间被强度取决于平均放电率的独立时间非均匀泊松过程所取代，将已知结果扩展到具有二次内在动态和重置的网络。证明泊松假设成立为研究这些网络中的大种群限值开辟了可能性。我们证明这个极限是一个适定的神经场模型，受随机重置的影响。 et.al.|[2502.03379](http://arxiv.org/abs/2502.03379)|null|

<p align=right>(<a href=#updated-on-20250318>back to top</a>)</p>

[contributors-shield]: https://img.shields.io/github/contributors/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[contributors-url]: https://github.com/Vincentqyw/cv-arxiv-daily/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[forks-url]: https://github.com/Vincentqyw/cv-arxiv-daily/network/members
[stars-shield]: https://img.shields.io/github/stars/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[stars-url]: https://github.com/Vincentqyw/cv-arxiv-daily/stargazers
[issues-shield]: https://img.shields.io/github/issues/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[issues-url]: https://github.com/Vincentqyw/cv-arxiv-daily/issues

