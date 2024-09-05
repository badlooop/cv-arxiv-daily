[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]

## Updated on 2024.09.05
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
|**2024-08-30**|**2DGH: 2D Gaussian-Hermite Splatting for High-quality Rendering and Better Geometry Reconstruction**|二维高斯散斑最近成为三维重建中的一种重要方法，可以同时进行新颖的视图合成和几何重建。虽然众所周知的高斯核被广泛使用，但它缺乏各向异性和变形能力，导致物体轮廓处的边缘模糊，限制了当前高斯溅射方法的重建质量。为了提高表示能力，我们从量子物理学中汲取灵感，提出使用高斯-厄米特核作为高斯溅射中的新基元。新的核采用统一的数学形式，并扩展了高斯函数，高斯函数在更新的公式中充当零秩项。我们的实验证明了高斯-厄米核在几何重建和新的视图合成任务中的非凡性能。所提出的核优于传统的高斯散斑核，展示了其高质量3D重建和渲染的潜力。 et.al.|[2408.16982](http://arxiv.org/abs/2408.16982)|null|
|**2024-08-29**|**GameIR: A Large-Scale Synthesized Ground-Truth Dataset for Image Restoration over Gaming Content**|超分辨率和图像合成等图像恢复方法已成功应用于NVIDIA的DLSS等商业云游戏产品中。然而，公众对游戏内容的恢复并没有进行很好的研究。这种差异主要是由于缺乏与测试用例相匹配的地面真实游戏训练数据造成的。由于游戏内容的独特性，通过降低原始HR图像的质量来生成伪训练数据的常见方法导致了较差的恢复性能。在这项工作中，我们开发了GameIR，这是一个大规模的高质量计算机合成地面实况数据集，以填补空白，针对两种不同的应用。第一种是具有延迟渲染的超分辨率，以支持仅渲染和传输LR图像并在客户端恢复HR图像的游戏解决方案。我们为这项任务提供了19200个LR-HR配对的地面实况帧，这些帧来自以720p和1440p渲染的640个视频。第二种是新颖视图合成（NVS），支持在客户端渲染和传输部分多视图帧并生成剩余帧的多视图游戏解决方案。此任务有57600个HR帧，来自160个场景的960个视频，有6个摄像头视图。除了RGB帧外，还提供了延迟渲染阶段的GBuffers，可用于帮助恢复。此外，我们在我们的数据集上评估了几种SOTA超分辨率算法和基于NeRF的NVS算法，这证明了我们的地面真实GameIR数据在提高游戏内容恢复性能方面的有效性。此外，我们还测试了将GBuffers作为额外输入信息来帮助超分辨率和NVS的方法。我们向公众发布我们的数据集和模型，以促进对游戏内容恢复方法的研究。 et.al.|[2408.16866](http://arxiv.org/abs/2408.16866)|null|
|**2024-09-01**|**Generic Objects as Pose Probes for Few-Shot View Synthesis**|辐射场，包括NeRF和3D高斯分布，在高保真渲染和场景重建方面展现出巨大的潜力，但它们需要大量的姿态图像作为输入。COLMAP经常用于预处理以估计姿态，但它需要大量的特征匹配才能有效运行，并且它难以处理特征稀疏、图像之间基线较大或输入图像数量有限的场景。我们的目标是仅使用3到6个未经处理的场景图像来解决少视图NeRF重建问题。传统方法通常使用校准板，但在图像中并不常见。我们提出了一种新的想法，即利用图像和现实生活中常见的日常物品作为“姿势探测器”。探测对象由SAM自动分割，SAM的形状由立方体初始化。我们应用双分支体绘制优化（对象NeRF和场景NeRF）来约束姿势优化并共同细化几何体。具体来说，首先通过SDF表示中的PnP匹配来估计两个视图的对象姿态，该表示用作初始姿态。PnP匹配只需要很少的特征，适用于特征稀疏的场景。其他视图会逐步合并，以从前面的视图中优化姿势。在实验中，PoseProbe在多个数据集的姿态估计和新颖的视图合成方面都达到了最先进的性能。我们证明了它的有效性，特别是在COLMAP挣扎的小视图和大基线场景中。在烧蚀中，在场景中使用不同的对象会产生相当的性能。我们的项目页面位于：\href{https://zhirui-gao.github.io/PoseProbe.github.io/}｛此https URL｝ et.al.|[2408.16690](http://arxiv.org/abs/2408.16690)|null|
|**2024-08-29**|**Spurfies: Sparse Surface Reconstruction using Local Geometry Priors**|我们介绍了Spurfies，这是一种稀疏视图曲面重建的新方法，它将外观和几何信息解耦，以利用在合成数据上训练的局部几何先验。最近的研究主要集中在使用密集的多视图设置进行3D重建，通常需要数百张图像。然而，这些方法往往难以应对少数视图场景。现有的稀疏视图重建技术通常依赖于多视图立体网络，这些网络需要从大量数据中学习几何和外观的联合先验。相比之下，我们引入了一种神经点表示，该表示将几何和外观解耦，以便在仅使用合成ShapeNet数据集的子集之前训练局部几何。在推理过程中，我们利用这个曲面先验作为额外的约束，通过可微体绘制从稀疏输入视图进行曲面和外观重建，限制了可能解的空间。我们在DTU数据集上验证了我们的方法的有效性，并证明它在表面质量方面比以前的技术水平高出35%，同时实现了具有竞争力的新颖视图合成质量。此外，与之前的工作相比，我们的方法可以应用于更大的无界场景，如Mip NeRF 360。 et.al.|[2408.16544](http://arxiv.org/abs/2408.16544)|null|
|**2024-08-28**|**G-Style: Stylized Gaussian Splatting**|我们介绍了G-Style，这是一种新的算法，旨在将图像的样式转换为使用高斯散斑表示的3D场景。与基于神经辐射场的其他方法相比，高斯散斑是一种强大的3D表示方法，用于新颖的视图合成，它提供了快速的场景渲染和用户对场景的控制。最近的预印本已经证明，高斯飞溅场景的风格可以使用图像样本进行修改。然而，由于场景几何在样式化过程中保持不变，当前的解决方案无法产生令人满意的结果。我们的算法旨在通过以下三步过程来解决这些局限性：在预处理步骤中，我们去除具有大投影面积或高度细长形状的不需要的高斯分布。随后，我们结合了几个精心设计的损失，以保留图像中不同比例的风格，同时尽可能保持原始场景内容的完整性。在风格化过程中，遵循高斯散斑的原始设计，我们通过跟踪风格化颜色的梯度来分割场景中需要额外细节的高斯分布。我们的实验表明，G-Style在短短几分钟内即可生成高质量的样式，在定性和定量上都优于现有方法。 et.al.|[2408.15695](http://arxiv.org/abs/2408.15695)|null|
|**2024-08-28**|**Ray-Distance Volume Rendering for Neural Scene Reconstruction**|现有的神经场景重建方法利用符号距离函数（SDF）对密度函数进行建模。然而，在室内场景中，由于相邻对象的影响，从采样点的SDF计算的密度可能无法始终如一地反映其在体绘制中的真正重要性。为了解决这个问题，我们的工作提出了一种新的室内场景重建方法，该方法使用有符号射线距离函数（SRDF）对密度函数进行参数化。首先，SRDF由网络预测，并转换为光线条件密度函数进行体绘制。我们认为，光线特定的SRDF只考虑了沿相机光线的表面，从该表面导出的密度函数比SDF更符合实际占用情况。其次，尽管SRDF和SDF代表场景几何体的不同方面，但它们的值应该共享相同的符号，指示底层空间占用率。因此，这项工作引入了SRDF-SDF一致性损失，以限制SRDF和SDF输出的符号。第三，本文提出了一种自我监督的可见性任务，将物理可见性几何引入到重建任务中。可见性任务将预测的SRDF和SDF作为伪标签进行组合，有助于生成更准确的3D几何图形。我们用不同表示实现的方法已在室内数据集上得到验证，在重建和视图合成方面都取得了改进的性能。 et.al.|[2408.15524](http://arxiv.org/abs/2408.15524)|null|
|**2024-08-27**|**Drone-assisted Road Gaussian Splatting with Cross-view Uncertainty**|在自动驾驶仿真中，大规模道路场景的稳健和逼真渲染至关重要。最近，3D高斯散点（3D-GS）在神经渲染方面取得了突破性进展，但大规模道路场景渲染的一般保真度往往受到输入图像的限制，输入图像通常视野狭窄，主要集中在街道级别的局部区域。直观地说，无人机视角的数据可以为地面车辆视角的数据提供一个互补的视角，增强场景重建和渲染的完整性。然而，使用空中和地面图像进行天真的训练，这些图像表现出较大的视图差异，对3D-GS构成了重大的收敛挑战，并且在道路视图上的性能没有显著提高。为了增强道路视图的新颖视图合成并有效地使用航空信息，我们设计了一种不确定性感知训练方法，该方法允许航空图像辅助合成地面图像学习效果较差的区域，而不是像以前的工作那样在3D-GS训练中对所有像素进行平均加权。我们是第一个通过将基于汽车视图集成的渲染不确定性与航空图像进行匹配，并对每个像素对训练过程的贡献进行加权，从而将交叉视图不确定性引入3D-GS的公司。此外，为了系统地量化评估指标，我们组装了一个高质量的合成数据集，其中包括道路场景的空中和地面图像。 et.al.|[2408.15242](http://arxiv.org/abs/2408.15242)|**[link](https://github.com/sainingzhang/uc-gs)**|
|**2024-08-27**|**CrossViewDiff: A Cross-View Diffusion Model for Satellite-to-Street View Synthesis**|卫星到街道视图合成旨在从其相应的卫星视图图像生成逼真的街道视图图像。尽管稳定的扩散模型在各种图像生成应用中表现出了显著的性能，但它们依赖于相似的视图输入来控制生成的结构或纹理，这限制了它们在具有挑战性的跨视图合成任务中的应用。在这项工作中，我们提出了CrossViewDiff，这是一种用于卫星到街道视图合成的交叉视图扩散模型。为了应对视图间巨大差异带来的挑战，我们设计了卫星场景结构估计和跨视图纹理映射模块，以构建街景图像合成的结构和纹理控制。我们进一步设计了一个跨视图控制引导的去噪过程，该过程通过增强的跨视图注意力模块结合了上述控制。为了更全面地评估合成结果，我们还设计了一种基于GPT的评分方法，作为标准评估指标的补充。我们还探讨了不同数据源（如文本、地图、建筑高度和多时相卫星图像）对此任务的影响。三个公共交叉视图数据集的结果表明，CrossViewDiff在标准和基于GPT的评估指标上都优于当前最先进的技术，在农村、郊区和城市场景中生成了具有更逼真结构和纹理的高质量街景全景图。这项工作的代码和模型将在https://opendatalab.github.io/CrossViewDiff/. et.al.|[2408.14765](http://arxiv.org/abs/2408.14765)|null|
|**2024-08-26**|**MagicMan: Generative Novel View Synthesis of Humans with 3D-Aware Diffusion and Iterative Refinement**|由于训练数据不足或缺乏全面的多视图知识导致3D不一致，单图像人体重建中的现有工作普遍性较差。本文介绍了MagicMan，这是一种针对人类的多视图扩散模型，旨在从单个参考图像生成高质量的新颖视图图像。作为其核心，我们利用预先训练的2D扩散模型作为可推广性的生成先验，参数化SMPL-X模型作为3D主体，以促进3D感知。为了应对在实现密集多视图生成以改进3D人体重建的同时保持一致性的关键挑战，我们首先引入了混合多视图注意力，以促进不同视图之间高效彻底的信息交换。此外，我们提出了一种几何感知双分支，可以在RGB和法线域中执行并发生成，通过几何线索进一步增强一致性。最后但并非最不重要的一点是，为了解决与参考图像冲突的不准确SMPL-X估计引起的形状不良问题，我们提出了一种新的迭代细化策略，该策略逐步优化SMPL-X精度，同时提高生成的多视图的质量和一致性。大量的实验结果表明，我们的方法在新颖的视图合成和后续的3D人体重建任务中都明显优于现有的方法。 et.al.|[2408.14211](http://arxiv.org/abs/2408.14211)|null|
|**2024-08-27**|**Splatt3R: Zero-shot Gaussian Splatting from Uncalibrated Image Pairs**|本文介绍了Splatt3R，这是一种无姿态的前馈方法，用于野外3D重建和从立体对合成新的视图。给定未校准的自然图像，Splatt3R可以预测3D高斯散点，而不需要任何相机参数或深度信息。为了通用性，我们在“基础”3D几何重建方法MASt3R的基础上构建了Splatt3R，将其扩展到处理3D结构和外观。具体来说，与仅重建3D点云的原始MASt3R不同，我们预测了为每个点构建高斯基元所需的额外高斯属性。因此，与其他新颖的视图合成方法不同，Splatt3R首先通过优化3D点云的几何损失来训练，然后是一个新的视图合成目标。通过这样做，我们避免了在从立体视图训练3D高斯散斑时出现的局部最小值。我们还提出了一种新的损失掩蔽策略，我们经验发现，该策略对于外推观点的强大性能至关重要。我们在ScanNet++数据集上训练Splatt3R，并对未校准的野生图像进行了出色的泛化。Splatt3R可以以512 x 512分辨率以4FPS重建场景，并且可以实时渲染生成的splat。 et.al.|[2408.13912](http://arxiv.org/abs/2408.13912)|null|

<p align=right>(<a href=#updated-on-20240905>back to top</a>)</p>

## 3D Reconstruction

|Publish Date|Title|Abstract|PDF|Code|
|---|---|---|---|---|
|**2024-08-30**|**DARES: Depth Anything in Robotic Endoscopic Surgery with Self-supervised Vector-LoRA of the Foundation Model**|机器人辅助手术（RAS）依赖于3D重建和可视化的精确深度估计。虽然像深度任意模型（DAM）这样的基础模型显示出希望，但直接将其应用于手术往往会产生次优结果。对有限的手术数据进行完全微调可能会导致过拟合和灾难性的遗忘，从而损害模型的鲁棒性和泛化能力。尽管低秩自适应（LoRA）解决了一些自适应问题，但其均匀的参数分布忽略了固有的特征层次结构，即学习更一般特征的早期层比后期层需要更多的参数。为了解决这个问题，我们引入了机器人内窥镜手术中的深度任意（DARES），这是一种在DAM V2上采用新的自适应技术矢量低秩自适应（Vector LoRA）在RAS场景中执行自监督单眼深度估计的新方法。为了提高学习效率，我们通过在早期层中集成更多参数并在后期层中逐渐减少参数来引入Vector LoRA。我们还设计了一种基于多尺度SSIM误差的重投影损失，通过更好地根据手术环境的具体要求定制基础模型来增强深度感知。所提出的方法在SCARED数据集上进行了验证，并证明了其优于最新最先进的自监督单目深度估计技术的性能，绝对相对误差度量提高了13.3%。代码和预先训练的重量可在以下网址获得https://github.com/mobarakol/DARES. et.al.|[2408.17433](http://arxiv.org/abs/2408.17433)|null|
|**2024-08-30**|**GMM-IKRS: Gaussian Mixture Models for Interpretable Keypoint Refinement and Scoring**|从定位到三维重建，图像中关键点的提取是许多计算机视觉应用的基础。关键点有一个分数，可以根据其质量对其进行排名。虽然学习到的关键点通常比手工制作的关键点表现出更好的特性，但它们的分数不容易解释，因此几乎不可能比较不同方法中单个关键点的质量。我们提出了一个框架，该框架可以细化，同时用可解释的分数来表征任何方法提取的关键点。我们的方法利用了一种改进的鲁棒高斯混合模型拟合，旨在拒绝非鲁棒关键点并细化其余关键点。我们的分数由两个部分组成：一个与从另一个视点捕获的图像中提取相同关键点的概率有关，另一个与关键点的定位精度有关。这两个可解释的组件允许对不同方法提取的单个关键点进行比较。通过广泛的实验，我们证明，当应用于流行的关键点检测器时，我们的框架始终如一地提高了关键点的可重复性，以及它们在单应性和双/多视图姿态恢复任务中的性能。 et.al.|[2408.17149](http://arxiv.org/abs/2408.17149)|null|
|**2024-08-30**|**2DGH: 2D Gaussian-Hermite Splatting for High-quality Rendering and Better Geometry Reconstruction**|二维高斯散斑最近成为三维重建中的一种重要方法，可以同时进行新颖的视图合成和几何重建。虽然众所周知的高斯核被广泛使用，但它缺乏各向异性和变形能力，导致物体轮廓处的边缘模糊，限制了当前高斯溅射方法的重建质量。为了提高表示能力，我们从量子物理学中汲取灵感，提出使用高斯-厄米特核作为高斯溅射中的新基元。新的核采用统一的数学形式，并扩展了高斯函数，高斯函数在更新的公式中充当零秩项。我们的实验证明了高斯-厄米核在几何重建和新的视图合成任务中的非凡性能。所提出的核优于传统的高斯散斑核，展示了其高质量3D重建和渲染的潜力。 et.al.|[2408.16982](http://arxiv.org/abs/2408.16982)|null|
|**2024-08-29**|**Spurfies: Sparse Surface Reconstruction using Local Geometry Priors**|我们介绍了Spurfies，这是一种稀疏视图曲面重建的新方法，它将外观和几何信息解耦，以利用在合成数据上训练的局部几何先验。最近的研究主要集中在使用密集的多视图设置进行3D重建，通常需要数百张图像。然而，这些方法往往难以应对少数视图场景。现有的稀疏视图重建技术通常依赖于多视图立体网络，这些网络需要从大量数据中学习几何和外观的联合先验。相比之下，我们引入了一种神经点表示，该表示将几何和外观解耦，以便在仅使用合成ShapeNet数据集的子集之前训练局部几何。在推理过程中，我们利用这个曲面先验作为额外的约束，通过可微体绘制从稀疏输入视图进行曲面和外观重建，限制了可能解的空间。我们在DTU数据集上验证了我们的方法的有效性，并证明它在表面质量方面比以前的技术水平高出35%，同时实现了具有竞争力的新颖视图合成质量。此外，与之前的工作相比，我们的方法可以应用于更大的无界场景，如Mip NeRF 360。 et.al.|[2408.16544](http://arxiv.org/abs/2408.16544)|null|
|**2024-08-29**|**Mismatched: Evaluating the Limits of Image Matching Approaches and Benchmarks**|从二维图像进行三维重建是计算机视觉领域的一个活跃研究领域，其应用范围从导航和目标跟踪到分割和三维建模。传统上，参数化技术被用于这项任务。然而，最近的进展已经转向基于学习的方法。鉴于研究的快速步伐和新的图像匹配方法的频繁引入，对其进行评估至关重要。本文对使用运动流水线结构的各种图像匹配方法进行了综合评估。我们评估了这些方法在域内和域外数据集上的性能，确定了方法和基准中的关键局限性。我们还研究了边缘检测作为预处理步骤的影响。我们的分析表明，3D重建的图像匹配仍然是一个悬而未决的挑战，需要仔细选择和调整特定场景的模型，同时也突出了指标目前表示方法性能的不匹配。 et.al.|[2408.16445](http://arxiv.org/abs/2408.16445)|**[link](https://github.com/surgical-vision/colmap-match-converter)**|
|**2024-08-28**|**3D Reconstruction with Spatial Memory**|我们提出了Spann3R，这是一种从有序或无序图像集合进行密集3D重建的新方法。Spann3R基于DUSt3R范式构建，使用基于变换器的架构直接从图像中回归点图，而无需事先了解场景或相机参数。与DUSt3R不同，DUSt3R预测每个图像对在其局部坐标系中表示的点图，Spann3R可以预测在全局坐标系中表达的每个图像点图，从而消除了基于优化的全局对齐的需要。Spann3R的核心思想是管理一个外部空间记忆，学习跟踪所有先前相关的3D信息。然后，Spann3R查询该空间记忆，以预测全局坐标系中下一帧的3D结构。利用DUSt3R的预训练权重，以及对数据集子集的进一步微调，Spann3R在各种看不见的数据集上显示出具有竞争力的性能和泛化能力，并且可以实时处理有序的图像集合。项目页面：\url{https://hengyiwang.github.io/projects/spanner} et.al.|[2408.16061](http://arxiv.org/abs/2408.16061)|null|
|**2024-08-28**|**Geometry-guided Feature Learning and Fusion for Indoor Scene Reconstruction**|除了颜色和纹理信息外，几何还为3D场景重建提供了重要线索。然而，当前的重建方法仅包括特征级别的几何，因此没有充分利用几何信息。相比之下，本文提出了一种用于3D场景重建的新型几何集成机制。我们的方法在三个层面上结合了3D几何，即特征学习、特征融合和网络监督。首先，几何引导特征学习对几何先验进行编码，以包含与视图相关的信息。其次，引入了一种几何引导的自适应特征融合，该融合利用几何先验作为引导，自适应地为多个视图生成权重。第三，在监督层面，考虑到2D和3D法线之间的一致性，设计了一个一致的3D法线损失来添加局部约束。在ScanNet数据集上进行了大规模实验，结果表明，采用我们的几何积分机制的体积方法在定量和定性方面都优于最先进的方法。我们的体积方法在7-Scenes和TUM RGB-D数据集上也显示出良好的泛化能力。 et.al.|[2408.15608](http://arxiv.org/abs/2408.15608)|null|
|**2024-08-27**|**Learning-based Multi-View Stereo: A Survey**|3D重建旨在恢复场景的密集3D结构。它在增强/虚拟现实（AR/VR）、自动驾驶和机器人等各种应用中发挥着至关重要的作用。利用从不同视点捕获的场景的多个视图，多视图立体（MVS）算法合成了一个全面的3D表示，从而能够在复杂环境中进行精确重建。由于其高效性和有效性，MVS已成为基于图像的3D重建的关键方法。最近，随着深度学习的成功，许多基于学习的MVS方法被提出，与传统方法相比取得了令人印象深刻的性能。我们将这些基于学习的方法分为：基于深度图、基于体素、基于NeRF、基于3D高斯散斑和大型前馈方法。其中，我们主要关注基于深度图的方法，由于其简洁性、灵活性和可扩展性，这些方法是MVS的主要家族。在这项调查中，我们对撰写本文时的文献进行了全面的回顾。我们研究了这些基于学习的方法，总结了它们在流行基准测试中的表现，并讨论了该领域有前景的未来研究方向。 et.al.|[2408.15235](http://arxiv.org/abs/2408.15235)|null|
|**2024-08-27**|**GeoTransfer : Generalizable Few-Shot Multi-View Reconstruction via Transfer Learning**|本文提出了一种新的稀疏3D重建方法，该方法利用神经辐射场（NeRF）的表现力和特征的快速传递来学习精确的占用场。现有的基于稀疏输入的3D重建方法仍然难以捕捉复杂的几何细节，并且在处理遮挡区域方面可能存在局限性。另一方面，NeRF擅长对复杂场景进行建模，但不提供提取有意义几何体的方法。我们提出的方法通过传输NeRF特征中编码的信息来获得准确的占用场表示，从而提供了两全其美的效果。我们利用预训练的、可推广的最先进的NeRF网络来捕获详细的场景辐射信息，并快速传递这些知识来训练可推广的隐式占用网络。这一过程有助于利用可推广的NeRF先验中编码的场景几何知识，并对其进行细化以学习占用场，从而更精确地推广3D空间的表示。迁移学习方法显著减少了训练时间，减少了几个数量级（即从几天减少到3.5小时），从而避免了从头开始训练可推广的稀疏表面重建方法的需要。此外，我们引入了一种新的体积渲染权重损失，有助于学习准确的占用场，以及一种有助于全局平滑占用场的正常损失。我们在DTU数据集上评估了我们的方法，并在重建精度方面展示了最先进的性能，特别是在具有稀疏输入数据和遮挡区域的挑战性场景中。我们还通过在混合MVS数据集上显示定性结果来证明我们的方法的泛化能力，而无需任何再训练。 et.al.|[2408.14724](http://arxiv.org/abs/2408.14724)|null|
|**2024-08-26**|**Pixel-Aligned Multi-View Generation with Depth Guided Decoder**|图像到多视图生成的任务是指从单个图像生成实例的新视图。最近的方法通过将文本到图像的潜在扩散模型扩展到多视图版本来实现这一点，该版本包含一个VAE图像编码器和一个U-Net扩散模型。具体来说，这些生成方法通常只修复VAE并微调U-Net。然而，从输入图像和独立解码计算的潜在矢量的显著缩小导致多个视图之间的像素级错位。为了解决这个问题，我们提出了一种像素级图像到多视图生成的新方法。与先前的工作不同，我们在潜在视频扩散模型的VAE解码器中跨多视图图像合并了注意力层。具体来说，我们引入了一种深度截断的极线注意，使模型能够专注于空间相邻的区域，同时保持内存效率。在推理过程中应用深度截断attn具有挑战性，因为通常很难获得地面真实深度，预训练的深度估计模型也很难提供准确的深度。因此，为了在缺少地面真实深度时增强对不准确深度的泛化能力，我们在训练过程中扰动深度输入。在推理过程中，我们采用了一种快速的多视图到3D重建方法NeuS来获得深度截断极线关注的粗略深度。我们的模型可以在多视图图像中实现更好的像素对齐。此外，我们证明了我们的方法在改进下游多视图3D重建任务方面的有效性。 et.al.|[2408.14016](http://arxiv.org/abs/2408.14016)|null|

<p align=right>(<a href=#updated-on-20240905>back to top</a>)</p>

## Diffusion

|Publish Date|Title|Abstract|PDF|Code|
|---|---|---|---|---|
|**2024-08-30**|**CinePreGen: Camera Controllable Video Previsualization via Engine-powered Diffusion**|随着视频生成人工智能模型（如SORA）的进步，创作者越来越多地使用这些技术来增强视频的视觉预览。然而，他们面临着不完整和不匹配的人工智能工作流程的挑战。现有的方法主要依赖于文本描述，并与相机放置作斗争，这是视觉预览的一个关键组成部分。为了解决这些问题，我们引入了CinePreGen，这是一种通过引擎驱动的扩散增强的视觉预视系统。它具有一个新颖的相机和故事板界面，提供从全局到局部相机调整的动态控制。这与用户友好的AI渲染工作流程相结合，旨在通过多掩码IP适配器和引擎模拟指南实现一致的结果。在我们的综合评估研究中，我们证明了我们的系统降低了开发粘度（即开发过程中的复杂性和挑战），满足了用户在设计过程中对广泛控制和迭代的需求，并且在电影摄影机运动方面优于其他AI视频制作工作流程，正如我们的实验和受试者内部用户研究所示。凭借其直观的相机控制和逼真的相机运动渲染，CinePreGen在改善个人创作者和行业专业人士的视频制作方面显示出巨大的潜力。 et.al.|[2408.17424](http://arxiv.org/abs/2408.17424)|null|
|**2024-08-30**|**High-order finite element methods for three-dimensional multicomponent convection-diffusion**|我们推导并分析了一类广泛的有限元方法，用于数值模拟常见热力学相中几种不同化学物质的浓缩混合物的稳态低雷诺数流动。我们离散化的基本偏微分方程是Stokes $\unicode{x2013}$Onsager$\unicode{x2013]$Stefan$\unicode{x2013}$Maxwell（SOSM）方程，它模拟了理想和非理想混合物中的体动量输运和多组分扩散。与以前的方法不同，这些方法可以在二维和三维空间中直接实现，并允许使用高阶有限元空间。推导离散化的关键思想是根据物种质量通量和化学势适当地重新表述SOSM方程，并使用稳定的$H（\textrm{div}）\unicode{x2013}L^2$ 有限元对对这些未知场进行离散化。我们证明了这些方法是收敛的，并为SOSM方程的Picard线性化产生了一个对称线性系统，该系统阻碍了浓度和化学势的更新。我们还讨论了如何将提出的方法扩展到SOSM方程的牛顿线性化，这需要同时求解摩尔分数、化学势和其他变量。我们的理论结果得到了数值实验的支持，我们展示了一个涉及碳氢化合物微流体非理想混合的物理应用示例。 et.al.|[2408.17390](http://arxiv.org/abs/2408.17390)|null|
|**2024-08-30**|**An enhanced version of the Gaia map of the brightness of the natural sky**|GAia自然天空亮度图（GAMBONS）是一个模型，用于绘制无云和无月夜晚天空的自然夜间亮度。它根据Gaia和Hipparcos目录中的光度数据计算恒星辐射，加上漫射银河系和河外光、黄道光和气辉的贡献，并考虑到大气衰减和散射的影响。该模型允许计算地面观察者在任何给定光度带中的自然天空亮度，前提是Gaia带有适当的转换。在这项工作中，我们介绍了该模型的最新改进，包括使用盖亚EDR3数据、包含一组广泛的光度带以及推导额外的天空亮度指标，如水平辐照度和平均半球辐射率 et.al.|[2408.17371](http://arxiv.org/abs/2408.17371)|null|
|**2024-08-30**|**Dimensional confinement and superdiffusive rotational motion of uniaxial colloids in the presence of cylindrical obstacles**|在细胞这样的生物系统中，各向异性粒子的大分子在拥挤的介质中扩散。在本研究中，我们通过改变障碍物和球形粒子的密度，研究了球形粒子在圆柱形障碍物之间的扩散。自由能的分析计算表明，在平衡状态下，单个扁粒子的取向矢量将垂直排列，而长粒子将平行于圆柱形障碍物的对称轴排列。有障碍物和没有障碍物的系统的向列相变保持不变，但在有障碍物的情况下，球体系统的向流矢量始终保持平行于圆柱轴。计算了各向同性系统中垂直于圆柱轴的球形粒子的平移扩散系数分量，与解析计算结果一致。当圆柱体重叠，使得球状粒子只能沿着平行于圆柱体轴线的方向扩散时，我们可以观察到尺寸限制。当绘制单个颗粒和有限体积分数的化学势时，通过扩散系数的不连续下降可以观察到这一点。在各向同性阶段，随着障碍物之间距离的增加，旋转扩散系数迅速达到体积值。在向列相，球体的旋转运动应该被阻止。我们观察到，即使整个系统仍处于向列相，靠近圆柱体的扁粒子也会发生翻转运动。结果是，当计算旋转均方位移时，即使取向自相关函数从未松弛到零，它也表现出超扩散行为。 et.al.|[2408.17345](http://arxiv.org/abs/2408.17345)|null|
|**2024-08-30**|**Subspace Diffusion Posterior Sampling for Travel-Time Tomography**|扩散模型作为求解逆问题的有效生成工具得到了广泛的研究。主要思想集中在执行基于噪声测量的反向采样过程，使用成熟的数值求解器进行梯度更新。尽管基于扩散的采样方法可以产生高质量的重建，但基于非线性偏微分方程的逆问题和采样速度仍然存在挑战。在这项工作中，我们探索了基于子空间扩散生成模型求解基于偏微分方程的走时层析成像。我们的主要贡献有两个：首先，我们通过求解相关的伴随状态方程，为基于偏微分方程的逆问题提出了一种后验采样过程。其次，我们采用基于子空间的降维技术进行条件采样加速，从而能够从粗网格到精网格求解基于偏微分方程的逆问题。我们的数值实验表明，在提高走时成像质量和减少重建采样时间方面取得了令人满意的进展。 et.al.|[2408.17333](http://arxiv.org/abs/2408.17333)|null|
|**2024-08-30**|**Image-Perfect Imperfections: Safety, Bias, and Authenticity in the Shadow of Text-To-Image Model Evolution**|文本到图像模型，如稳定扩散（SD），经过迭代更新以提高图像质量并解决安全等问题。图像质量的改善很容易评估。然而，模型更新如何解决现有的问题，以及它们是否会引发新的问题，仍有待探索。本研究从安全性、偏见和真实性的角度初步研究了文本到图像模型的演变。我们的研究结果以稳定扩散为中心，表明模型更新描绘了一幅混合的画面。虽然更新逐步减少了不安全图像的产生，但偏见问题，特别是性别偏见问题，加剧了。我们还发现，负面刻板印象要么在同一非白人种族群体中持续存在，要么通过SD更新转向其他非白人种族，但这些特征与白人种族群体的关联很小。此外，我们的评估揭示了一个源于SD更新的新问题：最初针对早期SD版本进行训练的最先进的假图像检测器很难识别更新版本生成的假图像。我们发现，在各种SD版本中，对更新版本生成的假图像进行微调可以达到至少96.6%的准确率，从而解决了这个问题。我们的见解强调了继续努力减轻文本到图像模型演变中的偏见和漏洞的重要性。 et.al.|[2408.17285](http://arxiv.org/abs/2408.17285)|null|
|**2024-08-30**|**Likelihood estimation for stochastic differential equations with mixed effects**|随机微分方程为模拟受随机噪声影响的动态现象提供了一种强大而通用的工具。如果对几个实验单元的时间序列进行重复观测，通常会出现一些参数在单个实验单元之间变化的情况，这激发了人们对具有混合效应的随机微分方程的极大兴趣，其中一部分参数是随机的。这些模型能够同时表示动力学中的随机性和实验单元之间的可变性。当数据是离散时间点的观测值时，似然函数很少明确可用，因此需要基于似然推理的数值方法。我们在Bladt和Sérensen（2014）中提出了基于扩散桥模拟简单方法的Gibbs采样器和随机EM算法。这些方法易于实现，并且没有调优参数。此外，它们在低采样频率下具有计算效率，因为计算时间随观测之间的时间呈线性增加。这些算法被证明可以大大简化指数族扩散过程。在一项模拟研究中，这些估计方法被证明对Ornstein-Uhlenbeck过程和具有混合效应的t-扩散非常有效。最后，将Gibbs采样器应用于神经元数据。 et.al.|[2408.17257](http://arxiv.org/abs/2408.17257)|null|
|**2024-08-30**|**A kinetic chemotaxis model and its diffusion limit in slab geometry**|趋化性描述了细胞运动对化学信号的复杂相互作用。我们在这里考虑板几何的情况，它模拟了两个无限膜之间的趋化运动。与之前的工作一样，我们对高翻滚率的渐近机制特别感兴趣。我们建立了动力学方程解的局部存在性和唯一性，并证明了它们在渐近极限下收敛于抛物Keller-Segel模型的解。此外，我们证明了在问题数据的附加正则性假设下，渐近参数的收敛速度。我们分析中的特殊困难是由动力学模型中的速度消失以及边界项的出现引起的。 et.al.|[2408.17243](http://arxiv.org/abs/2408.17243)|null|
|**2024-08-30**|**Shock-driven amorphization and melt in Fe $_2$O$_3$**|我们通过时间分辨原位x射线衍射，在高达209（10）GPa的激光驱动冲击压缩下，对Fe$_2$O$_3$非晶化和熔体进行了测量。在122（3）GPa下，观察到扩散信号，表明存在非晶相。已提取高达182（6）GPa的结构因子，显示存在两个明确的峰。在145（10）和151（10）GPa之间，两个峰的强度比发生了快速变化，这表明发生了相变。目前对Fe$_2$O$_3$Hugoniot沿线温度的DFT+$U$计算与SESAME 7440一致，表明温度相对较低，低于2000 K，高达150 GPa。因此，非晶态扩散散射与Fe$_2$O$_3$在122（3）和145（10）GPa之间的冲击非晶化一致，随后在151（10）GPa以上发生非晶态到液态的转变。释放后，观察到非晶相与晶相$\alpha$-Fe$_2$O$_3$并存。该释放相的提取结构因子和配对分布函数与环境压力下Fe$_2$O$_3$ 熔体的报道相似。 et.al.|[2408.17204](http://arxiv.org/abs/2408.17204)|null|
|**2024-08-30**|**Excitation and spatial study of a prestellar cluster towards G+0.693-0.027 in the Galactic centre**|中心分子区（CMZ）的恒星形成相对于银河系盘面受到抑制，这可能与它的高湍流环境有关。这种湍流阻碍了对星前核心的潜在探测。我们展示了CMZ分子云G+0.693-0.027的温度、密度和空间结构，该分子云被提出在Sgr B2区域拥有一个星前星团。我们分析了用IRAM 30m、APEX、Yebes 40m和GBT射电望远镜观测到的多个HC $_{3}$N旋转跃迁，以及SMA+APEC空间分辨图。HC$_{3}$N线的光谱形状显示了三个速度分量：一个线宽为23 km s$^{-1}$的宽分量（C1），以及两个线宽为7.2和8.8 km s$^{-1}$$的窄分量（C2和C3）。这表明，这片云中的一部分分子气体正在经历湍流消散。从非局部热力学平衡分析中，我们发现C1、C2和C3的H${2}$密度分别为2$times$10$^{4}$cm$^{-3}$、5$times$10$^{4}$cm$^{-3}$和4$times$10 ^{5}$cm$^{-3]$，动力学温度分别为140K、30K和80K。空间分辨图证实，在70-85kms^{-1}$ 速度范围内达到峰值的较冷和高密度冷凝C2和C3嵌入了更扩散和较暖的气体（C1）中。Sgr B2区域的大尺度结构显示，在40-50公里处有一个洞，这可能是由于一个小云冲击了Sgr B1区域，并与60-80公里处的一个大质量云在空间上相关。我们提出，撞击的小云依次触发了Sgr B2（M）、（N）和（S）的形成，并在其通过过程中在G+0.693-0.027中凝结。根据对两个凝聚体的质量和维里参数的分析，C2可能会膨胀，而C3可能会进一步碎裂或坍塌。 et.al.|[2408.17141](http://arxiv.org/abs/2408.17141)|null|

<p align=right>(<a href=#updated-on-20240905>back to top</a>)</p>

## NeRF

|Publish Date|Title|Abstract|PDF|Code|
|---|---|---|---|---|
|**2024-08-23**|**S4D: Streaming 4D Real-World Reconstruction with Gaussians and 3D Control Points**|最近，使用高斯分布的动态场景重建引起了越来越多的兴趣。主流方法通常采用全局变形场来扭曲规范空间中的3D场景。然而，隐式神经场固有的低频特性往往导致复杂运动的无效表示。此外，它们的结构刚性会阻碍对不同分辨率和持续时间的场景的适应。为了克服这些挑战，我们引入了一种利用离散3D控制点的新方法。该方法对局部射线进行物理建模，并建立一个运动解耦坐标系，该坐标系有效地将传统图形与可学习的流水线相结合，以实现鲁棒且高效的局部6自由度（6-DoF）运动表示。此外，我们还开发了一个广义框架，将我们的控制点与高斯算子结合起来。从初始3D重建开始，我们的工作流程将流式4D真实世界重建分解为四个独立的子模块：3D分割、3D控制点生成、对象运动操纵和残差补偿。我们的实验表明，该方法在Neu3DV和CMU全景数据集上的表现优于现有的最先进的4D高斯散斑技术。我们的方法还显著加速了训练，在单个NVIDIA 4070 GPU上，每帧只需2秒即可优化我们的3D控制点。 et.al.|[2408.13036](http://arxiv.org/abs/2408.13036)|null|
|**2024-08-22**|**Neural Fields and Noise-Induced Patterns in Neurons on Large Disordered Networks**|我们研究了随机图上受时空随机强迫的大维神经网络类的模式形成。在耦合和节点动力学的一般条件下，我们证明了该网络具有严格的平均场极限，类似于Wilson Cowan神经场方程。限制系统的状态变量是神经元活动的均值和方差。我们选择平均场方程易于处理的网络，并使用每个神经元上传入白噪声的扩散强度作为控制参数进行分叉分析。我们在皮质被建模为环的系统中找到了图灵分叉的条件，并在二维皮质模型中产生了噪声诱导螺旋波的数值证据。我们提供了数值证据，证明有限尺寸网络的解弱收敛于平均场模型的解。最后，我们证明了大偏差原理，该原理提供了一种评估有限尺寸效应引起的平均场方程偏差可能性的方法。 et.al.|[2408.12540](http://arxiv.org/abs/2408.12540)|null|
|**2024-08-19**|**Neural Representation of Shape-Dependent Laplacian Eigenfunctions**|拉普拉斯算子的特征函数在数学物理、工程和几何处理中至关重要。通常，这些是通过对域进行离散化并执行特征分解来计算的，将结果与特定的网格联系起来。然而，这种方法不适合连续参数化的形状。我们提出了一种连续参数化形状空间中本征函数的新表示，其中本征函数是连续依赖于形状参数的空间场，由最小狄利克雷能量、单位范数和相互正交性定义。我们用训练为神经场的多层感知器来实现这一点，将形状参数和域位置映射到特征函数值。一个独特的挑战是强制因果关系的相互正交性，其中因果顺序在形状空间中是不同的。因此，我们的训练方法需要三个相互交织的概念：（1）通过在单位范数约束下最小化狄利克雷能量来同时学习n$本征函数；（2） 在反向传播过程中过滤梯度以强制因果正交性，防止早期特征函数受到后期特征函数的影响；（3） 基于特征值对因果排序进行动态排序，以跟踪特征值曲线交叉。我们在形状族分析、不完整形状的特征函数预测、交互式形状操作和计算高维特征函数等问题上展示了我们的方法，这些问题都是传统方法所不能达到的。 et.al.|[2408.10099](http://arxiv.org/abs/2408.10099)|null|
|**2024-08-20**|**Scene123: One Prompt to 3D Scene Generation via Video-Assisted and Consistency-Enhanced MAE**|随着人工智能生成内容（AIGC）的进步，已经开发了各种方法来从单模式或多模式输入生成文本、图像、视频和3D对象，从而有助于模拟类人认知内容的创建。然而，由于确保模型生成的外推视图之间的一致性所涉及的复杂性，从单个输入生成逼真的大规模场景是一个挑战。受益于最新的视频生成模型和隐式神经表示，我们提出了Scene123，这是一种3D场景生成模型，它不仅通过视频生成框架确保了真实性和多样性，还使用隐式神经场与掩模自编码器（MAE）相结合，有效地确保了视图中看不见区域的一致性。具体来说，我们最初会扭曲输入图像（或从文本生成的图像）以模拟相邻的视图，用MAE模型填充不可见的区域。然而，这些填充图像通常无法保持视图一致性，因此我们利用产生的视图来优化神经辐射场，增强几何一致性。此外，为了进一步增强生成视图的细节和纹理保真度，我们对通过视频生成模型从输入图像中导出的图像采用了基于GAN的Loss。大量实验表明，我们的方法可以从单个提示中生成逼真一致的场景。定性和定量结果都表明，我们的方法超越了现有的最先进的方法。我们展示鼓励视频示例https://yiyingyang12.github.io/Scene123.github.io/. et.al.|[2408.05477](http://arxiv.org/abs/2408.05477)|null|
|**2024-08-07**|**Compact 3D Gaussian Splatting for Static and Dynamic Radiance Fields**|3D高斯飞溅（3DGS）最近成为一种替代表示，它利用基于3D高斯的表示并引入了近似的体积渲染，实现了非常快的渲染速度和有前景的图像质量。此外，后续的研究已成功地将3DGS扩展到动态3D场景，展示了其广泛的应用。然而，由于3DGS及其后续方法需要大量的高斯分布来保持渲染图像的高保真度，这需要大量的内存和存储，因此出现了一个重大的缺点。为了解决这个关键问题，我们特别强调两个关键目标：在不牺牲性能的情况下减少高斯点的数量，以及压缩高斯属性，如视图相关的颜色和协方差。为此，我们提出了一种可学习的掩码策略，该策略在保持高性能的同时显著减少了高斯数。此外，我们提出了一种紧凑但有效的视图相关颜色表示方法，即采用基于网格的神经场，而不是依赖球谐函数。最后，我们学习码本，通过残差矢量量化来紧凑地表示几何和时间属性。通过量化和熵编码等模型压缩技术，我们始终表明，与静态场景的3DGS相比，存储空间减少了25倍以上，渲染速度提高了25倍，同时保持了场景表示的质量。对于动态场景，与现有的最先进方法相比，我们的方法实现了超过12倍的存储效率，并保留了高质量的重建。我们的工作为3D场景表示提供了一个全面的框架，实现了高性能、快速训练、紧凑性和实时渲染。我们的项目页面可在https://maincold2.github.io/c3dgs/. et.al.|[2408.03822](http://arxiv.org/abs/2408.03822)|null|
|**2024-08-07**|**PRTGS: Precomputed Radiance Transfer of Gaussian Splats for Real-Time High-Quality Relighting**|我们提出了高斯斑点的预计算辐射转移（PRTGS），这是一种在低频照明环境中用于高斯斑点的实时高质量重新照明方法，通过预计算3D高斯斑点的辐射转移来捕获柔和的阴影和相互反射。现有的研究表明，在动态照明场景中，3D高斯溅射（3DGS）的效率优于神经场。然而，目前基于3DGS的重新照明方法仍然难以实时计算动态光的高质量阴影和间接照明，导致渲染结果不切实际。我们通过预先计算复杂传递函数（如阴影）所需的昂贵传输模拟来解决这个问题，得到的传递函数表示为每个高斯斑点的密集向量集或矩阵集。我们介绍了针对训练和渲染阶段量身定制的不同预计算方法，以及针对3D高斯斑点的独特光线追踪和间接照明预计算技术，以加快训练速度并计算与环境光相关的准确间接照明。实验分析表明，我们的方法在保持有竞争力的训练时间的同时实现了最先进的视觉质量，并允许以1080p分辨率对动态光和相对复杂的场景进行高质量的实时（30+fps）重新照明。 et.al.|[2408.03538](http://arxiv.org/abs/2408.03538)|null|
|**2024-08-01**|**Neural Octahedral Field: Octahedral prior for simultaneous smoothing and sharp edge regularization**|神经隐式表示，将距离函数参数化为坐标神经场，已成为解决无方向点云表面重建的有前景的前沿。为了确保方向一致，现有的方法侧重于正则化距离函数的梯度，例如将其约束为单位范数，最小化其散度，或将其与对应于零特征值的Hessian特征向量对齐。然而，在存在大扫描噪声的情况下，它们往往要么过拟合噪声输入，要么产生过于平滑的重建。在这项工作中，我们建议利用六面体网格中产生的八面体框架的球谐表示，在一种新的神经场变体——八面体场下指导曲面重建。当约束为平滑时，该字段会自动捕捉到几何特征，并在折痕上插值时自然保留锐角。通过同时拟合和平滑隐式几何旁边的八面体场，它的行为类似于双边滤波，从而在保持锐边的同时实现平滑重建。尽管是纯逐点操作，但我们的方法在广泛的实验中表现优于各种传统和神经方法，并且与需要正常和数据先验的方法非常有竞争力。我们的全面实施可在以下网址获得：https://github.com/Ankbzpx/frame-field. et.al.|[2408.00303](http://arxiv.org/abs/2408.00303)|**[link](https://github.com/ankbzpx/frame-field)**|
|**2024-07-30**|**Neural Fields for Continuous Periodic Motion Estimation in 4D Cardiovascular Imaging**|时间分辨三维血流MRI（4D血流MRI）提供了一种独特的非侵入性解决方案，用于可视化和量化主动脉弓等血管中的血流动力学。然而，由于难以获得完整的周期分割，目前大多数动脉4D血流MRI分析方法使用静态动脉壁。为了克服这一局限性，我们提出了一种基于神经场的方法，可以直接估计整个心动周期中连续的周期性壁变形。对于3D+时间成像数据集，我们优化了表示时间依赖速度矢量场（VVF）的隐式神经表示（INR）。ODE求解器用于将VVF集成到变形矢量场（DVF）中，该矢量场可以随着时间的推移使图像、分割掩模或网格变形，从而可视化和量化局部壁运动模式。为了正确反映3D+时间心血管数据的周期性，我们以两种方式施加周期性。首先，通过定期对输入到INR的时间进行编码，从而对VVF进行编码。其次，通过规范DVF。我们证明了这种方法在不同周期模式的合成数据、心电图门控CT和4D血流MRI数据上的有效性。所获得的方法可用于改进4D血流MRI分析。 et.al.|[2407.20728](http://arxiv.org/abs/2407.20728)|null|
|**2024-07-29**|**Aero-Nef: Neural Fields for Rapid Aircraft Aerodynamics Simulations**|本文提出了一种基于隐式神经表示（INR）在网格域上学习稳态流体动力学模拟替代模型的方法。所提出的模型可以直接应用于不同流动条件下的非结构化域，处理非参数3D几何变化，并推广到测试时看不见的形状。基于坐标的公式自然会导致离散化的鲁棒性，从而在计算成本（内存占用和训练时间）和精度之间实现了极好的权衡。该方法在两个工业相关应用中得到了验证：跨音速翼型上二维可压缩流的RANS数据集和三维机翼上表面压力分布的数据集，包括形状、流入条件和控制表面偏转变化。在所考虑的测试用例中，与最先进的图神经网络架构相比，我们的方法实现了三倍多的测试误差，并显著改善了看不见的几何形状的泛化误差。值得注意的是，该方法在RANS跨音速翼型数据集上的推理速度比高保真求解器快五个数量级。代码可在以下网址获得https://gitlab.isae-supaero.fr/gi.catalani/aero-nepf et.al.|[2407.19916](http://arxiv.org/abs/2407.19916)|**[link](https://gitlab.isae-supaero.fr/gi.catalani/aero-nepf)**|
|**2024-07-26**|**ObjectCarver: Semi-automatic segmentation, reconstruction and separation of 3D objects**|隐式神经场在从多幅图像重建3D表面方面取得了显著进展；然而，在分离场景中的单个对象时，他们遇到了挑战。之前的工作试图通过引入一个框架来解决这个问题，该框架为N个对象中的每一个同时训练单独的带符号距离场（SDF），并使用正则化项来防止对象重叠。然而，所有这些方法都需要提供分割掩模，这并不总是容易获得的。我们介绍了我们的方法ObjectCarver，来解决在单个视图中从点击输入中分离对象的问题。给定摆出的多视图图像和一组用户输入点击来提示分割单个对象，我们的方法将场景分解为单独的对象，并为每个对象重建高质量的3D表面。我们引入了一个损失函数，可以防止漂浮物，避免因遮挡而造成不适当的雕刻。此外，我们引入了一种新的场景初始化方法，与之前的方法相比，该方法在保留几何细节的同时显著加快了过程。尽管不需要地面真实掩模或单眼线索，但我们的方法在定性和定量上都优于基线。此外，我们引入了一个新的基准数据集进行评估。 et.al.|[2407.19108](http://arxiv.org/abs/2407.19108)|null|

<p align=right>(<a href=#updated-on-20240905>back to top</a>)</p>

[contributors-shield]: https://img.shields.io/github/contributors/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[contributors-url]: https://github.com/Vincentqyw/cv-arxiv-daily/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[forks-url]: https://github.com/Vincentqyw/cv-arxiv-daily/network/members
[stars-shield]: https://img.shields.io/github/stars/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[stars-url]: https://github.com/Vincentqyw/cv-arxiv-daily/stargazers
[issues-shield]: https://img.shields.io/github/issues/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[issues-url]: https://github.com/Vincentqyw/cv-arxiv-daily/issues

