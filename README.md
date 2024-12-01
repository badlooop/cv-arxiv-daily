[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]

## Updated on 2024.12.01
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
|**2024-11-27**|**CAT4D: Create Anything in 4D with Multi-View Video Diffusion Models**|我们介绍了CAT4D，这是一种从单眼视频创建4D（动态3D）场景的方法。CAT4D利用在各种数据集组合上训练的多视图视频扩散模型，在任何指定的相机姿态和时间戳下实现新颖的视图合成。结合一种新颖的采样方法，该模型可以将单个单眼视频转换为多视图视频，通过优化可变形的3D高斯表示实现稳健的4D重建。我们在新颖的视图合成和动态场景重建基准上展示了具有竞争力的性能，并强调了从真实或生成的视频生成4D场景的创造性能力。有关结果和交互式演示，请参阅我们的项目页面：\url{cat-4d.github.io}。 et.al.|[2411.18613](http://arxiv.org/abs/2411.18613)|null|
|**2024-11-27**|**SmileSplat: Generalizable Gaussian Splats for Unconstrained Sparse Images**|稀疏多视图图像可以通过广义高斯散斑方法学习来预测显式辐射场，在不需要地面实况相机参数作为输入的情况下，可以在现实生活中实现更广泛的应用前景。本文提出了一种新的可推广高斯散斑方法SmileSplat，用于重建仅需要无约束稀疏多视图图像的不同场景的像素对齐高斯表面。首先，基于多头高斯回归解码器预测高斯曲面，该解码器可以用较少的自由度表示，但具有更好的多视图一致性。此外，基于高质量的法向量先验，高斯曲面的法向量得到了增强。其次，基于所提出的束调整高斯散斑模块，优化高斯和相机参数（包括外部和内部参数），以获得高质量的高斯辐射场，用于新的视图合成任务。在公共数据集上对新颖的视图渲染和深度图预测任务进行了广泛的实验，证明所提出的方法在各种3D视觉任务中达到了最先进的性能。更多信息可以在我们的项目页面上找到(https://yanyan-li.github.io/project/gs/smilesplat) et.al.|[2411.18072](http://arxiv.org/abs/2411.18072)|null|
|**2024-11-26**|**Geometry Field Splatting with Gaussian Surfels**|从图像中几何重建不透明表面是计算机视觉领域的一个长期挑战，使用辐射场的体积视图合成算法重新引起了人们的兴趣。我们利用最近工作中提出的随机不透明表面的几何场，然后将其转换为体积密度。我们采用高斯核或曲面来绘制几何场而不是体积，从而能够精确重建不透明固体。我们的第一个贡献是为高斯曲面参数化的几何场推导出一种高效且几乎精确的可微渲染算法，同时消除了涉及泰勒级数的当前近似值，并且没有自衰减。接下来，我们讨论了当曲面在几何体附近聚集时的不连续损失情况，展示了如何保证渲染的颜色是核颜色的连续函数，而不管顺序如何。最后，我们使用球面谐波编码反射矢量的潜在表示，而不是球面谐波编码颜色，以更好地解决镜面问题。我们在广泛使用的数据集上证明了重建的3D表面质量的显著提高。 et.al.|[2411.17067](http://arxiv.org/abs/2411.17067)|null|
|**2024-11-25**|**G2SDF: Surface Reconstruction from Explicit Gaussians with Implicit SDFs**|最先进的新颖视图合成方法，如3D高斯散斑（3DGS），实现了卓越的视觉质量。虽然3DGS及其变体可以使用光栅化有效地渲染，但许多任务需要访问底层3D表面，由于这种表示的稀疏和显式性质，提取仍然具有挑战性。本文介绍了G2SDF，这是一种通过将神经隐式有符号距离场（SDF）集成到高斯散斑框架中来解决这一局限性的新方法。我们的方法将高斯的不透明度值与其到表面的距离联系起来，确保高斯与场景表面更紧密地对齐。为了将这种方法扩展到不同尺度的无界场景，我们提出了一种将任何范围映射到固定间隔的归一化函数。为了进一步提高重建质量，我们在高斯散布优化过程中利用现成的深度估计器作为伪地面真值。通过在显式高斯分布和隐式SDF之间建立可微连接，我们的方法能够实现高质量的曲面重建和渲染。在几个真实世界数据集上的实验结果表明，G2SDF在保持3DGS效率的同时，实现了比先前工作更优的重建质量。 et.al.|[2411.16898](http://arxiv.org/abs/2411.16898)|null|
|**2024-11-25**|**PreF3R: Pose-Free Feed-Forward 3D Gaussian Splatting from Variable-length Image Sequence**|我们提出了PreF3R，即从可变长度的图像序列进行无姿态前馈3D重建。与之前的方法不同，PreF3R消除了对相机校准的需要，并直接从一系列未经处理的图像中重建规范坐标系内的3D高斯场，从而实现了高效的新颖视图渲染。我们利用DUSt3R的成对3D结构重建能力，并通过空间存储网络将其扩展到连续的多视图输入，从而消除了基于优化的全局对齐的需要。此外，PreF3R还集成了一个密集的高斯参数预测头，这使得后续的可微光栅化视图合成成为可能。这允许通过结合光度损失和点图回归损失来监督我们的模型，从而提高照片真实感和结构精度。在给定一系列有序图像的情况下，PreF3R以20 FPS的速度增量重建3D高斯场，从而实现了实时新视图渲染。经验实验表明，PreF3R是无姿态前馈新视图合成这一具有挑战性任务的有效解决方案，同时对看不见的场景也表现出鲁棒的泛化能力。 et.al.|[2411.16877](http://arxiv.org/abs/2411.16877)|null|
|**2024-11-25**|**MAGiC-SLAM: Multi-Agent Gaussian Globally Consistent SLAM**|具有新颖视图合成功能的同步定位和映射（SLAM）系统广泛应用于计算机视觉，并在增强现实、机器人和自动驾驶中得到应用。然而，现有的方法仅限于单代理操作。最近的工作使用分布式神经场景表示来解决这个问题。遗憾的是，现有的方法速度较慢，无法准确呈现真实世界的数据，仅限于两个代理，跟踪精度有限。相比之下，我们提出了一种基于刚性可变形3D高斯的场景表示，大大加快了系统的速度。然而，由于轨迹漂移和代理观察结果之间的差异，提高跟踪精度和从多个代理重建全局一致的地图仍然具有挑战性。因此，我们提出了新的跟踪和映射合并机制，并在基于高斯的SLAM流水线中集成了环路闭合。我们在合成和真实世界的数据集上评估了MAGiC-SLAM，发现它比最新技术更准确、更快。 et.al.|[2411.16785](http://arxiv.org/abs/2411.16785)|null|
|**2024-11-25**|**Quark: Real-time, High-resolution, and General Neural View Synthesis**|我们提出了一种新的神经算法，用于执行高质量、高分辨率、实时的新颖视图合成。我们的网络从一组稀疏的输入RGB图像或视频流中重建3D场景，并在NVIDIA A100上以1080p分辨率和30fps渲染新颖的视图。我们的前馈网络适用于各种数据集和场景，并为实时方法提供最先进的质量。我们的质量接近，在某些情况下甚至超过了一些顶级线下方法的质量。为了实现这些结果，我们使用了几个关键概念的新颖组合，并将它们联系在一起，形成一个连贯有效的算法。我们基于之前使用半透明层表示场景的工作，并使用迭代学习渲染和优化方法来改进这些层。我们的方法重建了分层深度图（LDM），而不是平面层，它有效地表示了具有复杂深度和遮挡的场景。迭代更新步骤嵌入在多尺度、UNet风格的架构中，以降低分辨率执行尽可能多的计算。在每个更新步骤中，为了更好地聚合来自多个输入视图的信息，我们使用了一个专门的基于Transformer的网络组件。与层空间相反，这允许在输入图像空间中执行大部分每输入图像处理，从而进一步提高了效率。最后，由于重建和渲染的实时性，我们为每一帧动态创建和丢弃内部3D几何体，为每个视图生成LDM。综上所述，这产生了一种新颖有效的视图合成算法。通过广泛的评估，我们证明我们以实时速率实现了最先进的质量。项目页面：https://quark-3d.github.io/ et.al.|[2411.16680](http://arxiv.org/abs/2411.16680)|null|
|**2024-11-25**|**SplatFlow: Multi-View Rectified Flow Model for 3D Gaussian Splatting Synthesis**|基于文本的3D场景生成和编辑具有通过直观的用户交互简化内容创建的巨大潜力。虽然最近的进展利用3D高斯散斑（3DGS）进行高保真和实时渲染，但现有的方法通常是专门的和以任务为中心的，缺乏生成和编辑的统一框架。在本文中，我们介绍了SplatFlow，这是一个全面的框架，通过实现直接的3DGS生成和编辑来解决这一差距。SplatFlow包括两个主要组件：多视图整流流（RF）模型和高斯散斑解码器（GSDecoder）。多视图RF模型在潜在空间中运行，根据文本提示同时生成多视图图像、深度和相机姿态，从而解决了现实世界中不同场景比例和复杂相机轨迹等挑战。然后，GSDecoder通过前馈3DGS方法有效地将这些潜在输出转换为3DGS表示。SplatFlow利用无需训练的反转和修复技术，实现了无缝的3DGS编辑，并在统一的框架内支持广泛的3D任务，包括对象编辑、新颖的视图合成和相机姿态估计，而不需要额外的复杂管道。我们在MVImgNet和DL3DV-7K数据集上验证了SplatFlow的功能，展示了它在各种基于3D生成、编辑和修复的任务中的多功能性和有效性。 et.al.|[2411.16443](http://arxiv.org/abs/2411.16443)|**[link](https://github.com/gohyojun15/SplatFlow)**|
|**2024-11-25**|**U2NeRF: Unsupervised Underwater Image Restoration and Neural Radiance Fields**|由于光吸收、折射、散射和恢复，水下图像会出现颜色偏移、对比度低和模糊等问题，因此这些图像值得关注。在这项工作中，我们提出了无监督水下神经辐射场U2NeRF，这是一种基于变换器的架构，可以学习同时渲染和恢复基于多视图几何的新视图。由于缺乏监督，我们试图将恢复能力隐式地烘焙到NeRF管道上，并将预测的颜色分解为几个分量——场景辐射、直接传输图、反向散射传输图和全局背景光，当组合在一起时，以自我监督的方式重建水下图像。此外，我们发布了一个由12个水下场景组成的水下视图合成UVS数据集，其中包含合成生成的数据和真实世界的数据。我们的实验表明，当在单个场景上进行优化时，U2NeRF的表现优于多个基线，LPIPS为11%，UIQM为5%，UCIQE为4%（平均），并展示了改进的渲染和恢复能力。代码将在验收后提供。 et.al.|[2411.16172](http://arxiv.org/abs/2411.16172)|null|
|**2024-11-26**|**MVGenMaster: Scaling Multi-View Generation from Any Image via 3D Priors Enhanced Diffusion Model**|我们介绍了MVGenMaster，这是一种用3D先验增强的多视图扩散模型，用于解决多功能的新视图合成（NVS）任务。MVGenMaster利用使用度量深度和相机姿态扭曲的3D先验，显著增强了NVS中的泛化能力和3D一致性。我们的模型具有一个简单而有效的管道，可以通过一个正向过程生成多达100个基于可变参考视图和相机姿态的新视图。此外，我们还开发了一个名为MvD-1M的全面的大规模多视图图像数据集，包含多达160万个场景，配备了对齐良好的度量深度来训练MVGenMaster。此外，我们提出了一些训练和模型修改，以用放大的数据集来加强模型。对域内和域外基准的广泛评估证明了我们提出的方法和数据公式的有效性。型号和代码将于https://github.com/ewrfcas/MVGenMaster/. et.al.|[2411.16157](http://arxiv.org/abs/2411.16157)|**[link](https://github.com/ewrfcas/mvgenmaster)**|

<p align=right>(<a href=#updated-on-20241201>back to top</a>)</p>

## 3D Reconstruction

|Publish Date|Title|Abstract|PDF|Code|
|---|---|---|---|---|
|**2024-11-27**|**Textured Gaussians for Enhanced 3D Scene Appearance Modeling**|3D高斯散斑（3DGS）最近因其高质量的结果和快速的训练和渲染时间而成为一种最先进的3D重建和渲染技术。然而，被同一高斯覆盖的像素总是以相同的颜色着色，直到高斯衰减缩放因子。此外，任何单个高斯都可以表示的最精细的几何细节是一个简单的椭球体。3DGS的这些特性极大地限制了单个高斯基元的表现力。为了解决这些问题，我们从传统图形中的纹理和阿尔法映射中汲取灵感，并将其与3DGS集成。具体来说，我们提出了一种新的广义高斯外观表示方法，该方法使用alpha~（a）、RGB或RGBA纹理映射来增强每个高斯分布，以模拟每个高斯分布范围内空间变化的颜色和不透明度。因此，每个高斯分布可以表示一组更丰富的纹理图案和几何结构，而不是像朴素的高斯分布那样只表示一种颜色和椭球体。令人惊讶的是，我们发现仅使用alpha纹理贴图可以大大提高高斯的表现力，而用RGB纹理贴图进一步增强高斯可以获得最高的表现力。我们在各种标准基准数据集和我们自己在对象和场景级别的自定义捕获上验证了我们的方法。我们展示了在使用相似或更少数量的高斯分布的情况下，图像质量比现有方法有所提高。 et.al.|[2411.18625](http://arxiv.org/abs/2411.18625)|null|
|**2024-11-26**|**MARVEL-40M+: Multi-Level Visual Elaboration for High-Fidelity Text-to-3D Content Creation**|由于现有数据集的大小、多样性和注释深度有限，从文本提示生成高保真3D内容仍然是计算机视觉领域的一个重大挑战。为了解决这个问题，我们引入了MARVEL-40M+，这是一个庞大的数据集，包含4000万个文本注释，涵盖了从七个主要3D数据集聚合而来的890多万个3D资产。我们的贡献是一个新颖的多阶段注释管道，它集成了开源预训练的多视图VLM和LLM，可以自动生成多级描述，从详细的（150-200个单词）到简洁的语义标签（10-20个单词）。这种结构支持细粒度3D重建和快速原型制作。此外，我们将源数据集中的人类元数据合并到我们的注释管道中，以在注释中添加特定于领域的信息，并减少VLM幻觉。此外，我们还开发了MARVEL-FX3D，这是一个两阶段的文本到3D管道。我们使用注释微调稳定扩散，并使用预训练的图像到3D网络在15秒内生成3D纹理网格。广泛的评估表明，MARVEL-40M+在注释质量和语言多样性方面明显优于现有数据集，GPT-4的胜率为72.41%，人工评估者的胜率达到73.40%。 et.al.|[2411.17945](http://arxiv.org/abs/2411.17945)|null|
|**2024-11-26**|**MVBoost: Boost 3D Reconstruction with Multi-View Refinement**|3D对象重建的最新进展令人瞩目，但目前大多数3D模型严重依赖现有的3D数据集。不同3D数据集的稀缺导致3D重建模型的泛化能力有限。本文提出了一种通过生成伪GT数据来增强多视图细化（MVBoost）3D重建的新框架。MVBoost的关键是结合多视图生成模型的高精度和3D重建模型的一致性，创建可靠的数据源。具体来说，给定一个单视图输入图像，我们采用多视图扩散模型来生成多个视图，然后使用大型3D重建模型来生成一致的3D数据。MVBoost然后自适应地细化这些从一致的3D数据渲染的多视图图像，以构建大规模多视图数据集，用于训练前馈3D重建模型。此外，输入视图优化旨在根据用户的输入图像优化相应的视点，确保最重要的视点能够准确地满足用户的需求。广泛的评估表明，与先前的工作相比，我们的方法实现了更优的重建结果和鲁棒的泛化。 et.al.|[2411.17772](http://arxiv.org/abs/2411.17772)|null|
|**2024-11-26**|**Puzzle Similarity: A Perceptually-guided No-Reference Metric for Artifact Detection in 3D Scene Reconstructions**|现代重建技术可以从稀疏的2D视图中有效地对复杂的3D场景进行建模。然而，由于缺乏地面真实图像以及在预测详细伪影图时没有参考图像度量的局限性，自动评估新视图的质量和识别伪影具有挑战性。缺乏这样的质量指标阻碍了对生成视图质量的准确预测，并限制了采用后处理技术（如修复）来提高重建质量。在这项工作中，我们提出了一种新的无参考度量——拼图相似度，旨在定位新视图中的伪影。我们的方法利用来自输入视图的图像补丁统计数据来建立场景特定的分布，该分布后来用于识别新视图中重建不佳的区域。我们在3D重建的背景下测试和评估了我们的方法；为此，我们在看不见的重建视图中收集了一个新的人体质量评估数据集。通过这个数据集，我们证明了我们的方法不仅可以成功地定位与人类评估相关的新视图中的伪影，而且可以在没有直接引用的情况下实现。令人惊讶的是，我们的指标优于无参考指标和流行的全参考图像指标。我们可以利用我们的新指标来增强自动图像恢复、引导采集或稀疏输入的3D重建等应用。 et.al.|[2411.17489](http://arxiv.org/abs/2411.17489)|null|
|**2024-11-26**|**DWCL: Dual-Weighted Contrastive Learning for Multi-View Clustering**|多视图对比聚类（MVCC）因其通过对比学习从多个视图生成一致的聚类结构而受到广泛关注。然而，大多数现有的MVCC方法通过组合任何两个视图来创建交叉视图，从而导致大量不可靠的对。此外，这些方法经常忽略多视图表示中的差异，导致表示退化。为了应对这些挑战，我们引入了一种名为双加权对比学习（DWCL）的多视图聚类新模型。具体来说，为了减少不可靠交叉视图的影响，我们引入一种创新的最佳其他（B-O）对比机制，以低计算成本增强单个视图的表示。此外，我们开发了一种双重加权策略，将反映每个视图质量的视图质量权重与视图差异权重相结合。这种方法通过淡化质量低、差异大的交叉视图，有效地减轻了表示退化。我们从理论上验证了B-O对比机制的效率和双加权策略的有效性。大量实验表明，DWCL在八个多视图数据集中的表现优于之前的方法，在MVCC中展示了卓越的性能和鲁棒性。具体来说，与Caltech6V7和MSRCv1数据集上的最新方法相比，我们的方法分别实现了5.4%和5.6%的绝对精度提高。 et.al.|[2411.17354](http://arxiv.org/abs/2411.17354)|**[link](https://github.com/SHERSONH/DWCL)**|
|**2024-11-26**|**Boost 3D Reconstruction using Diffusion-based Monocular Camera Calibration**|在本文中，我们提出了DM Calib，这是一种基于扩散的方法，用于从单个输入图像中估计针孔相机的固有参数。单眼相机校准对于许多3D视觉任务至关重要。然而，大多数现有的方法都依赖于手工制作的假设，或者受到有限训练数据的限制，导致对不同真实世界图像的泛化能力较差。基于海量数据训练的稳定扩散模型的最新进展表明，它能够生成具有不同特征的高质量图像。新出现的证据表明，这些模型隐含地捕捉到了相机焦距和图像内容之间的关系。基于这一认识，我们探索了如何利用扩散模型的强大先验进行单目针孔相机校准。具体来说，我们引入了一种新的基于图像的表示方法，称为Camera image，它对数字相机内部函数进行无损编码，并与扩散框架无缝集成。使用这种表示方法，我们将估计相机内部函数的问题重新表述为在输入图像的条件下生成密集的相机图像。通过微调稳定的扩散模型，从单个RGB输入生成相机图像，我们可以通过RANSAC操作提取相机内部函数。我们进一步证明，我们的单目校准方法提高了各种3D任务的性能，包括零样本测量深度估计、3D测量、姿态估计和稀疏视图重建。在多个公共数据集上进行的广泛实验表明，我们的方法明显优于基线，并为3D视觉任务提供了广泛的好处。代码可在以下网址获得https://github.com/JunyuanDeng/DM-Calib. et.al.|[2411.17240](http://arxiv.org/abs/2411.17240)|**[link](https://github.com/junyuandeng/dm-calib)**|
|**2024-11-27**|**SelfSplat: Pose-Free and 3D Prior-Free Generalizable 3D Gaussian Splatting**|我们提出了SelfSplat，这是一种新颖的3D高斯散斑模型，旨在从无基化多视图图像中执行无姿态和无3D先验的可推广3D重建。由于缺乏地面真实数据、学习到的几何信息，以及需要在不进行微调的情况下实现精确的3D重建，这些设置本身就不合适，这使得传统方法难以获得高质量的结果。我们的模型通过有效地将显式3D表示与自监督深度和姿态估计技术相结合来解决这些挑战，从而在姿态精度和3D重建质量方面实现了相互改进。此外，我们结合了一个匹配感知的姿态估计网络和一个深度细化模块，以增强视图之间的几何一致性，确保更准确和稳定的3D重建。为了展示我们的方法的性能，我们在大规模的真实世界数据集上对其进行了评估，包括RealEstate10K、ACID和DL3DV。SelfSplat在外观和几何质量方面都比以前最先进的方法取得了更优的结果，也展示了强大的跨数据集泛化能力。广泛的消融研究和分析也验证了我们提出的方法的有效性。代码和预训练模型可在https://gynjn.github.io/selfsplat/ et.al.|[2411.17190](http://arxiv.org/abs/2411.17190)|null|
|**2024-11-25**|**PreF3R: Pose-Free Feed-Forward 3D Gaussian Splatting from Variable-length Image Sequence**|我们提出了PreF3R，即从可变长度的图像序列进行无姿态前馈3D重建。与之前的方法不同，PreF3R消除了对相机校准的需要，并直接从一系列未经处理的图像中重建规范坐标系内的3D高斯场，从而实现了高效的新颖视图渲染。我们利用DUSt3R的成对3D结构重建能力，并通过空间存储网络将其扩展到连续的多视图输入，从而消除了基于优化的全局对齐的需要。此外，PreF3R还集成了一个密集的高斯参数预测头，这使得后续的可微光栅化视图合成成为可能。这允许通过结合光度损失和点图回归损失来监督我们的模型，从而提高照片真实感和结构精度。在给定一系列有序图像的情况下，PreF3R以20 FPS的速度增量重建3D高斯场，从而实现了实时新视图渲染。经验实验表明，PreF3R是无姿态前馈新视图合成这一具有挑战性任务的有效解决方案，同时对看不见的场景也表现出鲁棒的泛化能力。 et.al.|[2411.16877](http://arxiv.org/abs/2411.16877)|null|
|**2024-11-26**|**Functionality understanding and segmentation in 3D scenes**|理解3D场景中的功能涉及解释自然语言描述，以在3D环境中定位功能交互对象，如手柄和按钮。功能理解极具挑战性，因为它既需要世界知识来解释语言，也需要空间感知来识别细粒度对象。例如，给定一个像“打开顶灯”这样的任务，一个嵌入式AI代理必须推断出它需要定位电灯开关，即使任务描述中没有明确提到开关。迄今为止，还没有针对这个问题开发出专门的方法。本文介绍了Fun3DU，这是第一种为3D场景中的功能理解而设计的方法。Fun3DU使用语言模型通过思维链推理解析任务描述，以识别感兴趣的对象。通过使用视觉和语言模型，在捕获场景的多个视图中分割识别的对象。来自每个视图的分割结果在3D中被提升，并使用几何信息聚合到点云中。Fun3DU是免费训练的，完全依赖于预先训练的模型。我们在SceneFun3D上评估了Fun3DU，这是最新也是唯一一个对这项任务进行基准测试的数据集，它包括230个场景的3000多个任务描述。我们的方法明显优于最先进的开放词汇3D分割方法。项目页面：https://jcorsetti.github.io/fun3du et.al.|[2411.16310](http://arxiv.org/abs/2411.16310)|null|
|**2024-11-25**|**Event-boosted Deformable 3D Gaussians for Fast Dynamic Scene Reconstruction**|3D高斯散斑（3D-GS）可以实现实时渲染，但由于RGB相机的低时间分辨率，在快速运动方面遇到了困难。为了解决这个问题，我们介绍了第一种将捕获高时间分辨率连续运动数据的事件相机与可变形3D-GS相结合的方法，用于快速动态场景重建。我们观察到，事件的阈值建模在实现高质量重建方面起着至关重要的作用。因此，我们提出了一种GS阈值联合建模（GTJM）策略，创建了一个相辅相成的过程，大大改善了3D重建和阈值建模。此外，我们引入了一种动态静态分解（DSD）策略，该策略首先通过利用静态高斯模型无法表示运动来识别动态区域，然后应用基于缓冲区的软分解来分离动态和静态区域。此策略通过避免静态区域中不必要的变形来加速渲染，并侧重于动态区域以提高保真度。我们的方法在RTX 3090 GPU上实现了156 FPS的高保真动态重建，分辨率为400美元×400美元。 et.al.|[2411.16180](http://arxiv.org/abs/2411.16180)|null|

<p align=right>(<a href=#updated-on-20241201>back to top</a>)</p>

## Diffusion

|Publish Date|Title|Abstract|PDF|Code|
|---|---|---|---|---|
|**2024-11-27**|**GeneMAN: Generalizable Single-Image 3D Human Reconstruction from Multi-Source Human Data**|给定一张野外人类照片，重建高保真3D人体模型仍然是一项具有挑战性的任务。现有方法面临困难，包括a）在野外人类图像中捕获的不同身体比例；b） 镜头内的各种个人物品；c）人体姿势的模糊性和人体纹理的不一致性。此外，高质量人类数据的稀缺加剧了这一挑战。为了解决这些问题，我们提出了一个名为GeneMAN的通用图像到3D huMAN重建框架，该框架基于一个全面的多源高质量人类数据集合，包括3D扫描、多视图视频、单张照片和我们生成的合成人类数据。GeneMAN包含三个关键模块。1） 在不依赖于参数化人体模型（例如SMPL）的情况下，GeneMAN首先训练一个特定于人体的文本到图像扩散模型和一个视图条件扩散模型，分别用作GeneMAN 2D人体先验和3D人体先验进行重建。2） 在预训练的人类先验模型的帮助下，利用几何初始化和雕刻管道在给定单个图像的情况下恢复高质量的3D人体几何。3） 为了实现高保真的3D人体纹理，GeneMAN采用了多空间纹理细化管道，连续细化潜在空间和像素空间中的纹理。大量的实验结果表明，GeneMAN可以从单个图像输入中生成高质量的3D人体模型，优于现有的最先进方法。值得注意的是，GeneMAN在处理野生图像时可以显示出更好的通用性，通常会产生具有常见项目的自然姿势的高质量3D人体模型，而不管输入图像中的身体比例如何。 et.al.|[2411.18624](http://arxiv.org/abs/2411.18624)|null|
|**2024-11-27**|**Diffusion Self-Distillation for Zero-Shot Customized Image Generation**|文本到图像的扩散模型产生了令人印象深刻的结果，但对于想要精细控制的艺术家来说，这是一个令人沮丧的工具。例如，一个常见的用例是在新的上下文中创建特定实例的图像，即“身份保持生成”。此设置以及许多其他任务（例如重新照明）非常适合图像+文本条件生成模型。然而，没有足够的高质量配对数据来直接训练这样的模型。我们提出了扩散自蒸馏，这是一种使用预训练的文本到图像模型为文本条件的图像到图像任务生成自己的数据集的方法。我们首先利用文本到图像扩散模型的上下文生成能力来创建图像网格，并在视觉语言模型的帮助下管理大型配对数据集。然后，我们使用精心策划的配对数据集将文本到图像模型微调为文本+图像到图像模型。我们证明，扩散自统计优于现有的零样本方法，在不需要测试时间优化的情况下，在广泛的身份保留生成任务上与持续调整技术具有竞争力。 et.al.|[2411.18616](http://arxiv.org/abs/2411.18616)|null|
|**2024-11-27**|**CAT4D: Create Anything in 4D with Multi-View Video Diffusion Models**|我们介绍了CAT4D，这是一种从单眼视频创建4D（动态3D）场景的方法。CAT4D利用在各种数据集组合上训练的多视图视频扩散模型，在任何指定的相机姿态和时间戳下实现新颖的视图合成。结合一种新颖的采样方法，该模型可以将单个单眼视频转换为多视图视频，通过优化可变形的3D高斯表示实现稳健的4D重建。我们在新颖的视图合成和动态场景重建基准上展示了具有竞争力的性能，并强调了从真实或生成的视频生成4D场景的创造性能力。有关结果和交互式演示，请参阅我们的项目页面：\url{cat-4d.github.io}。 et.al.|[2411.18613](http://arxiv.org/abs/2411.18613)|null|
|**2024-11-27**|**Evaluating and Improving the Effectiveness of Synthetic Chest X-Rays for Medical Image Analysis**|目的：探索生成合成胸部X射线图像和增强医学成像数据集的最佳实践方法，以优化深度学习模型在分类和分割等下游任务中的性能。材料和方法：我们利用潜在扩散模型来调节文本提示和/或分割掩模上合成胸部X射线的生成。我们探索了使用代理模型和放射科医生反馈等方法来提高合成数据的质量。然后，根据相关疾病信息或几何变换的分割掩模生成这些合成图像，并将其添加到来自CheXpert、CANDID-PTX、SIIM和RSNA肺炎数据集的地面真值训练集图像中，以衡量测试集上分类和分割模型性能的改善。F1和Dice评分分别用于评估分类和分割。Bonferroni校正的单尾t检验评估了合成数据性能改进的统计意义。结果：在所有实验中，与仅使用真实数据相比，我们生成的合成数据使平均分类F1得分提高了0.150453（CI:0.099108-0.201798；P=0.0031）。对于分割，Dice评分的最大改善为0.14575（CI:0.108267-0.183233；P=0.0064）。结论：为下游任务生成合成胸部X射线图像的最佳实践包括对单个疾病标签或几何变换的分割掩模进行处理，以及可能使用代理建模来微调这些生成。 et.al.|[2411.18602](http://arxiv.org/abs/2411.18602)|null|
|**2024-11-27**|**Frequency redistribution and step-size distribution of light scattered by atomic vapor: applications to Lévy flight random walk**|经过共振原子蒸气多次散射的光的传播可以描述为L’vy飞行。重飞行是一个具有重尾步长（r）分布的随机游走，渐近衰减为 $P（r）\sim r^{-1-\alpha}$，其中$\alpha<2$。L’vy飞行中典型的大台阶起源于蒸汽散射光的频率重新分布。我们计算了原子蒸气中光扩散的频率再分配函数和步长分布。从步长分布中，我们提取一个取决于步长的L'vy参数$\alpha$。我们研究了频率再分配函数和步长分布如何受到蒸汽有限尺寸和碱蒸汽典型的多级结构的影响。蒸汽的有限尺寸引入了光散射光谱的截止，从而引入了台阶尺寸的截止。多级结构在$P（r）$ 斜率中引入了振荡。这两种效应都可能对与L’vy飞行随机游走相关的可测量值产生影响。 et.al.|[2411.18570](http://arxiv.org/abs/2411.18570)|null|
|**2024-11-27**|**DexDiffuser: Interaction-aware Diffusion Planning for Adaptive Dexterous Manipulation**|具有丰富接触交互的灵巧操作对于先进的机器人技术至关重要。虽然最近基于扩散的规划方法显示出对更简单操作任务的希望，但它们在处理复杂的顺序交互时往往会产生不切实际的幻影状态（例如，物体在没有手接触的情况下自动移动）或缺乏适应性。在这项工作中，我们介绍了DexDiffuser，这是一种用于自适应灵巧操作的交互感知扩散规划框架。DexDiffuser通过双相扩散过程模拟关节状态动作动力学，该过程由交互前接触对齐和接触后目标导向控制组成，实现了目标自适应的通用灵巧操作。此外，我们结合了基于动力学模型的双制导，并利用大型语言模型进行自动制导功能生成，增强了物理交互的通用性，并通过语言线索促进了多样化的目标适应。在开门、笔和积木重新定位以及锤击等物理交互任务上的实验表明，DexDiffuser在训练分布之外的目标上是有效的，与现有方法相比，平均成功率（59.2%对29.5%）提高了一倍多。我们的框架在30度开门时实现了70.0%的成功率，在笔和块半侧重新定位时分别实现了40.0%和36.7%，在锤钉半驱动时实现了46.7%，突出了其在接触丰富的操作中的鲁棒性和灵活性。 et.al.|[2411.18562](http://arxiv.org/abs/2411.18562)|null|
|**2024-11-27**|**FAM Diffusion: Frequency and Attention Modulation for High-Resolution Image Generation with Stable Diffusion**|扩散模型擅长生成高质量的图像。然而，只有在训练期间使用的分辨率下操作时，它们才有效。按比例分辨率进行推理会导致重复模式和结构失真。以更高的分辨率进行再培训很快就会变得令人望而却步。因此，使预先存在的扩散模型能够以灵活的测试时间分辨率运行的方法是非常可取的。以前的作品经常出现伪影，并且经常引入较大的延迟开销。我们提出了两个简单的模块来解决这些问题。我们引入了一个利用傅里叶域提高全局结构一致性的频率调制（FM）模块，以及一个提高局部纹理模式一致性的注意力调制（AM）模块，这是一个在先前工作中基本忽略的问题。我们的方法被称为Fam扩散，可以无缝集成到任何潜在的扩散模型中，不需要额外的训练。大量的定性结果突出了我们的方法在解决结构和局部伪影方面的有效性，而定量结果则显示了最先进的性能。此外，我们的方法避免了冗余的推理技巧，以提高一致性，如基于补丁或渐进式生成，导致延迟开销可以忽略不计。 et.al.|[2411.18552](http://arxiv.org/abs/2411.18552)|null|
|**2024-11-27**|**The Rise and Fall of Ideas' Popularity**|在当代社会的动态景观中，思想、观点和利益的流行迅速波动。社会科学中的传统动态模型往往无法捕捉到这种内在的波动性，将变化归因于外生冲击，而不是系统的内在特征。本文介绍了一种新颖、易于处理的模型，该模型模拟了思想流行的自然起伏，提供了对现实世界动态的更准确表示。基于SIRS（易感、传染性、恢复、易感）流行病学模型，我们引入了一种反馈机制，允许恢复率根据系统的当前状态动态变化。这种修改反映了在社会饱和和新兴趣的推动下，想法采用和放弃的周期性。我们的模型成功地捕捉到了流行度的快速和反复变化，为这些波动背后的机制提供了宝贵的见解。这种方法为研究流行思想的传播动态提供了一个强大的框架，在营销、技术采用和政治运动等各个领域都有潜在的应用。 et.al.|[2411.18541](http://arxiv.org/abs/2411.18541)|null|
|**2024-11-27**|**Chemical pressure tuning of competing orders in $\textrm{Ba}_{1-x}\textrm{Ca}_{x}\textrm{Ni}_{2}\textrm{As}_{2}$**|$\mathrm{Ba}\mathrm{Ni}_{2} \数学{As}_{2} $，与铁基母体化合物$\mathrm{Ba}\mathrm结构相似{Fe}_{2} \数学{As}_{2} $，提供了一个独特的平台来研究超导性、电荷密度波和可能的电子向列性之间的相互作用。在这里，我们报告了$\mathrm的增长和特征{Ba}_{1-x}\mathrm{Ca}_{x} \数学{Ni}_{2} \数学{As}_{2} $单晶，$0\leq x\leq 0.1$，使用x射线衍射、扩散x射线散射、热容和电子输运测量的组合。我们的结果表明，钙替代会影响$\mathrm{Ba}\mathrm的结构、电子和热力学性质{Ni}_{2} \数学{As}_{2} 尽管存在明显差异，但这种方式让人强烈联想到适度的静水压力。特别是，钙替代有效地抑制了三斜晶系结构转变和相关的相称电荷密度波的形成，同时提高了超导转变温度。我们发现，晶体保持均匀的替代范围是有限的，因为对于浓度$x\geq 0.04$ ，强烈的扩散x射线散射表明了堆垛层错的形成，尽管NiAs层保持了完整性，但在化学压力完全抑制结构不稳定性的浓度下，这阻碍了研究。 et.al.|[2411.18536](http://arxiv.org/abs/2411.18536)|null|
|**2024-11-27**|**Spin liquid properties of the kagome material Cu $_3$(HOTP)$_2$**|金属有机框架（MOF）化合物Cu$_3$（HOTP）$_2$，也称为Cu$_3加元（HHTP）$_2$$，是一种小间隙半导体，含有反铁磁耦合的kagome晶格$S$=1/2 Cu$^\mathrm{II}$自旋，层内最近邻交换耦合$J\sim$2K。从DFT+U计算中获得的层内$J$值与合理的U值的实验值相匹配。μon自旋弛豫证实，在低至50mK的范围内没有磁序，并且看到自旋波动在2D晶格上扩散，这与量子自旋液体（QSL）基态存在于高度解耦了kagome层。从顺磁性区域到低温QSL区域冷却时自旋扩散速率的降低反映了量子纠缠。还发现，在低温QSL区域，这些层变得更加强烈地解耦。对QSL区域的自旋扩散、磁化率和比热结果的比较表明，该区域非常接近量子临界点，并且低能量无自旋电子激发密度很大。发现用于QSL自旋激发的Z$_2$ -线性狄拉克模型与实验最匹配。 et.al.|[2411.18518](http://arxiv.org/abs/2411.18518)|null|

<p align=right>(<a href=#updated-on-20241201>back to top</a>)</p>

## NeRF

|Publish Date|Title|Abstract|PDF|Code|
|---|---|---|---|---|
|**2024-11-27**|**Neural Image Unfolding: Flattening Sparse Anatomical Structures using Neural Fields**|断层成像揭示了3D物体的内部结构，对医学诊断至关重要。在断层体积的多个2D切片上，可视化非平面稀疏解剖结构的形态和外观本质上很困难，但对决策和报告很有价值。因此，存在各种器官特异性展开技术，将其密集采样的3D表面映射到失真最小化的2D表示。然而，目前还没有通用的框架来压平复杂的稀疏结构，包括血管、导管或骨骼系统。我们部署了一个神经场，将感兴趣的解剖结构转换为二维概览图像。我们进一步提出了失真正则化策略，并将几何损失公式与基于强度的损失公式相结合，以显示无注释和辅助目标。除了提高通用性外，我们的展开技术在稀疏结构的峰值失真方面优于基于网格的基线，与基于神经场的图像配准的雅可比公式相比，我们的正则化方案产生了更平滑的变换。 et.al.|[2411.18415](http://arxiv.org/abs/2411.18415)|null|
|**2024-11-25**|**The Radiance of Neural Fields: Democratizing Photorealistic and Dynamic Robotic Simulation**|随着机器人越来越多地与人类共存，它们必须在复杂、动态的环境中导航，这些环境富含视觉信息和隐含的社会动态，比如何时屈服或穿过人群。应对这些挑战需要在基于视觉的传感方面取得重大进展，并对社会动态因素有更深入的了解，特别是在导航等任务中。为了促进这一点，机器人研究人员需要先进的仿真平台，提供具有逼真演员的动态、逼真的环境。不幸的是，大多数现有的模拟器都达不到要求，将几何精度置于视觉保真度之上，并使用具有固定轨迹和低质量视觉效果的不切实际的代理。为了克服这些局限性，我们开发了一个模拟器，该模拟器结合了三个基本要素：（1）环境的逼真神经渲染，（2）具有行为管理的神经动画人类实体，以及（3）提供多传感器输出的以自我为中心的机器人代理。通过在双NeRF模拟器中利用先进的神经渲染技术，我们的系统可以生成环境和人体实体的高保真、逼真的渲染。此外，它还集成了最先进的社会力模型来模拟动态的人机和人机交互，创建了第一个由神经渲染驱动的逼真和可访问的人机模拟系统。 et.al.|[2411.16940](http://arxiv.org/abs/2411.16940)|null|
|**2024-11-21**|**CoNFiLD-inlet: Synthetic Turbulence Inflow Using Generative Latent Diffusion Models with Neural Fields**|涡流解析湍流模拟需要随机流入条件，以准确复制复杂的多尺度湍流结构。传统的基于再循环的方法依赖于计算昂贵的前体模拟，而现有的合成流入发生器往往无法再现真实的湍流相干结构。深度学习（DL）的最新进展为流入湍流生成开辟了新的可能性，但许多基于DL的方法依赖于确定性、自回归框架，容易产生误差累积，导致长期预测的鲁棒性较差。在这项工作中，我们提出了CoNFiLD入口，这是一种基于DL的新型流入湍流发生器，它将扩散模型与条件神经场（CNF）编码的潜在空间相结合，以产生逼真的随机流入湍流。通过使用雷诺数对流入条件进行参数化，CoNFiLD入口在很宽的雷诺数范围内（ $Re_tau$在$10^3$和$10^4$ 之间）有效地推广，而不需要重新训练或参数调整。通过直接数值模拟（DNS）和壁模型大涡模拟（WMLES）中的先验和后验测试进行的全面验证证明了其高保真度、鲁棒性和可扩展性，使其成为流入湍流合成的高效和通用解决方案。 et.al.|[2411.14378](http://arxiv.org/abs/2411.14378)|null|
|**2024-11-20**|**FAST-Splat: Fast, Ambiguity-Free Semantics Transfer in Gaussian Splatting**|我们提出了FAST Splat，用于快速、无歧义的语义高斯Splatting，旨在解决现有语义高斯Splatting方法的主要局限性，即：训练和渲染速度慢；内存使用率高；语义对象定位模糊。在推导FAST Splat时，我们将开放词汇语义高斯Splatting表述为将闭集语义蒸馏扩展到开放集（开放词汇）设置的问题，使FAST Splat能够提供精确的语义对象定位结果，即使在用户提供的模糊自然语言查询提示时也是如此。此外，通过最大限度地利用高斯散斑场景表示的显式形式，FAST Splat保留了高斯散斑的显著训练和渲染速度。具体来说，虽然现有的语义高斯散斑方法将语义提取到一个单独的神经场中或利用神经模型进行降维，但FAST Splat直接用特定的语义代码增强每个高斯分布，保留了高斯散斑相对于神经场方法的训练、渲染和内存使用优势。与先前的方法不同，这些高斯特定的语义代码以及哈希表使语义相似性能够通过开放词汇表用户提示进行测量，并进一步使FAST Splat能够用明确的语义对象标签和3D掩码进行响应。在实验中，我们证明，与最好的竞争语义高斯Splatting方法相比，FAST Splat的训练速度快4倍至6倍，数据预处理步骤快13倍，渲染速度快18倍至75倍，所需GPU内存大约小3倍。此外，与现有方法相比，FAST Splat实现了相对相似或更好的语义分割性能。审查期结束后，我们将提供项目网站和代码库的链接。 et.al.|[2411.13753](http://arxiv.org/abs/2411.13753)|null|
|**2024-11-20**|**GazeGaussian: High-Fidelity Gaze Redirection with 3D Gaussian Splatting**|在处理分布外数据时，凝视估计遇到了泛化挑战。为了解决这个问题，最近的方法使用神经辐射场（NeRF）来生成增强数据。然而，基于NeRF的现有方法计算成本高昂，缺乏面部细节。三维高斯散斑（3DGS）已成为神经场的主流表示。虽然3DGS已经在头部化身中得到了广泛的研究，但它面临着在不同受试者之间进行精确视线控制和泛化的挑战。在这项工作中，我们提出了GazeGaussian，这是一种高保真的视线重定向方法，它使用双流3DGS模型分别表示面部和眼睛区域。通过利用3DGS的非结构化特性，我们开发了一种基于目标凝视方向的刚性眼睛旋转的新眼睛表示。为了增强各种主题的综合泛化能力，我们集成了一个表达式条件模块来指导神经渲染器。综合实验表明，GazeGaussian在渲染速度、视线重定向精度和跨多个数据集的面部合成方面优于现有方法。我们还证明，现有的凝视估计方法可以利用GazeGaussian来提高其泛化性能。该代码将在以下网址提供：https://ucwxb.github.io/GazeGaussian/. et.al.|[2411.12981](http://arxiv.org/abs/2411.12981)|null|
|**2024-11-18**|**NeuMaDiff: Neural Material Synthesis via Hyperdiffusion**|高质量的材料合成对于复制复杂的表面特性以创建逼真的数字场景至关重要。然而，现有的方法往往在时间和内存方面效率低下，需要领域专业知识，或者需要大量的训练数据，而高维材料数据进一步限制了性能。此外，大多数方法缺乏多模态制导能力和标准化的评估指标，限制了综合任务的控制和可比性。为了解决这些局限性，我们提出了NeuMaDiff，这是一种利用超扩散的新型神经材料合成框架。我们的方法采用神经场作为低维表示，并结合了多模态条件超扩散模型来学习材料重量的分布。这使得通过材料类型、文本描述或参考图像等输入进行灵活指导成为可能，从而对合成提供了更大的控制。为了支持未来的研究，我们贡献了两个新的材料数据集，并引入了两个BRDF分布度量，以进行更严格的评估。我们通过广泛的实验证明了NeuMaDiff的有效性，包括一种新的基于统计的约束合成方法，该方法能够生成所需类别的材料。 et.al.|[2411.12015](http://arxiv.org/abs/2411.12015)|null|
|**2024-11-14**|**The Hydrodynamic Limit of Hawkes Processes on Adaptive Stochastic Networks**|我们确定了自适应网络上相互作用的霍克斯过程网络的大尺寸限制。节点变量的翻转被认为具有由传入边缘和节点的平均场给出的强度。边缘变量的翻转是传入节点变量的函数。边变量可以是对称的，也可以是不对称的。该模型受到社会学、神经科学和流行病学应用的启发。一般来说，极限概率律可以表示为具有强度函数的自洽泊松过程的不动点，该强度函数（i）是延迟的，（ii）取决于其自身的概率律。在边缘翻转仅由突触前神经元的状态决定的特定情况下（如神经科学中），证明了可以获得突触增强和神经增强双重进化的自主神经场型方程。 et.al.|[2411.09260](http://arxiv.org/abs/2411.09260)|null|
|**2024-11-09**|**Epi-NAF: Enhancing Neural Attenuation Fields for Limited-Angle CT with Epipolar Consistency Conditions**|神经场方法最初在逆渲染领域取得了成功，最近已扩展到CT重建，标志着传统技术的范式转变。虽然这些方法在稀疏视图CT重建中提供了最先进的结果，但它们在有限的角度设置中很难实现，在有限的视角范围内捕获输入投影。我们提出了一种基于X射线投影图像中相应极线之间一致性条件的新损失项，旨在规范神经衰减场优化。通过强制执行这些一致性条件，我们的方法Epi NAF将监督从有限角度范围内的输入视图传播到整个锥束CT范围内的预测投影。与基线方法相比，这种损失导致重建的定性和定量改进。 et.al.|[2411.06181](http://arxiv.org/abs/2411.06181)|null|
|**2024-11-07**|**LoFi: Scalable Local Image Reconstruction with Implicit Neural Representation**|神经场或隐式神经表示（INR）因其对图像和3D体积的有效连续表示而在机器学习和信号处理中引起了广泛关注。在这项工作中，我们以INR为基础，引入了一种基于坐标的局部处理框架来解决成像逆问题，称为LoFi（局部场）。与传统的图像重建方法不同，LoFi通过多层感知器（MLP）分别处理每个坐标处的局部信息，在该特定坐标处恢复对象。与INR类似，LoFi可以在任何连续坐标下恢复图像，从而实现多分辨率的图像重建。LoFi在图像重建方面的性能与标准CNN相当或更好，几乎与图像分辨率无关，对分布外数据和内存使用具有出色的泛化能力。值得注意的是，对1024美元×1024美元的图像进行训练只需要3GB的内存，比标准CNN通常需要的内存少20多倍。此外，LoFi的局部设计使其能够在小于10个样本的极小数据集上进行训练，而不会过拟合或需要正则化或提前停止。最后，我们使用LoFi作为即插即用框架中的去噪先验，用于解决一般的逆问题，以受益于其连续的图像表示和强大的泛化能力。尽管在低分辨率图像上进行了训练，但LoFi可以用作低维先验，以解决任何分辨率的逆问题。我们通过各种成像方式验证了我们的框架，从低剂量计算机断层扫描到无线电干涉成像。 et.al.|[2411.04995](http://arxiv.org/abs/2411.04995)|null|
|**2024-11-04**|**Physically Based Neural Bidirectional Reflectance Distribution Function**|我们介绍了基于物理的神经双向反射分布函数（PBNBRDF），这是一种基于神经场的材料外观的新颖连续表示。我们的模型准确地重建了真实世界的材料，同时独特地增强了现实BRDF的物理特性，特别是通过重新参数化的亥姆霍兹互易性和通过高效分析积分的能量无源性。我们进行了系统分析，证明了遵守这些物理定律对重建材料的视觉质量的好处。此外，我们通过引入色度强制监督RGB通道的规范来提高神经BRDF的颜色精度。通过在多个测量的真实BRDF数据库上进行定性和定量实验，我们表明，遵守这些物理约束可以使神经场更忠实、更稳定地表示原始数据，并实现更高的渲染质量。 et.al.|[2411.02347](http://arxiv.org/abs/2411.02347)|null|

<p align=right>(<a href=#updated-on-20241201>back to top</a>)</p>

[contributors-shield]: https://img.shields.io/github/contributors/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[contributors-url]: https://github.com/Vincentqyw/cv-arxiv-daily/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[forks-url]: https://github.com/Vincentqyw/cv-arxiv-daily/network/members
[stars-shield]: https://img.shields.io/github/stars/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[stars-url]: https://github.com/Vincentqyw/cv-arxiv-daily/stargazers
[issues-shield]: https://img.shields.io/github/issues/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[issues-url]: https://github.com/Vincentqyw/cv-arxiv-daily/issues

