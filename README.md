[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]

## Updated on 2024.03.31
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
|**2024-03-28**|**GauStudio: A Modular Framework for 3D Gaussian Splatting and Beyond**|我们介绍了GauStudio，这是一种用于建模3D高斯飞溅（3DGS）的新型模块化框架，为用户提供标准化的即插即用组件，以便轻松定制和实现3DGS管道。在我们的框架的支持下，我们提出了一种具有前景和天球背景模型的混合高斯表示。实验证明，这种表示减少了无边界户外场景中的伪影，并改进了新颖的视图合成。最后，我们提出了高斯飞溅表面重建（GauS），这是一种新的先渲染后融合的方法，用于在没有微调的情况下从3DGS输入进行高保真度网格重建。总体而言，我们的GauStudio框架、混合表示和GauS方法增强了3DGS建模和渲染能力，实现了更高质量的新视图合成和曲面重建。 et.al.|[2403.19632](http://arxiv.org/abs/2403.19632)|**[link](https://github.com/gap-lab-cuhk-sz/gaustudio)**|
|**2024-03-28**|**SAID-NeRF: Segmentation-AIDed NeRF for Depth Completion of Transparent Objects**|使用现成的RGB-D相机获取透明物体的准确深度信息是计算机视觉和机器人学中的一个众所周知的挑战。深度估计/完成方法通常在具有质量深度标签的数据集上使用和训练，该质量深度标签是从模拟、附加传感器或专门的数据收集设置和已知的三维模型中获取的。然而，大规模获取数据集的可靠深度信息并不简单，这限制了训练的可扩展性和泛化能力。神经辐射场（NeRF）是一种无需学习的方法，在新的视图合成和形状恢复方面取得了广泛的成功。然而，通常需要启发式和受控环境（灯光、背景等）来准确捕捉镜面反射表面。在本文中，我们建议使用视觉基础模型（VFM）以零样本、无标签的方式进行分割，通过同时重建语义字段和扩展来指导这些对象的NeRF重建过程，以提高鲁棒性。我们提出的方法Segmentation AIDed NeRF（SAID NeRF）在透明物体和机器人抓取的深度完成数据集上表现出显著的性能。 et.al.|[2403.19607](http://arxiv.org/abs/2403.19607)|null|
|**2024-03-28**|**XScale-NVS: Cross-Scale Novel View Synthesis with Hash Featurized Manifold**|我们提出了用于真实世界大规模场景的高保真度跨尺度新颖视图合成的XScale NVS。基于显式曲面的现有表示存在离散化分辨率或UV失真问题，而隐式体积表示由于分散的权重分布和曲面模糊性而缺乏大型场景的可扩展性。鉴于上述挑战，我们引入了哈希特征化流形，这是一种新的基于哈希的特征化与延迟神经渲染框架相结合。这种方法通过将哈希条目显式集中在2D流形上，充分释放了表示的表现力，从而有效地表示了独立于离散化分辨率的高度详细的内容。我们还引入了一个新的数据集，即GigaNVS，用于对现实世界大规模场景的跨尺度、高分辨率新视图合成进行基准测试。我们的方法在各种真实世界场景中显著优于竞争基线，在具有挑战性的GigaNVS基准上产生的平均LPIPS比之前的最先进水平低40%。请参阅我们的项目页面：xscalenvs.github.io。 et.al.|[2403.19517](http://arxiv.org/abs/2403.19517)|null|
|**2024-03-28**|**CoherentGS: Sparse Novel View Synthesis with Coherent 3D Gaussians**|在过去的几年里，从图像进行3D重建的领域迅速发展，首先是引入了神经辐射场（NeRF），最近又引入了3D高斯散射（3DGS）。后者在训练和推理速度以及重建质量方面提供了优于NeRF的显著优势。尽管3DGS适用于密集的输入图像，但非结构化的点云状表示很快过度适应极稀疏的输入图像（例如，3个图像）的更具挑战性的设置，从而从新颖的视图中创建出看起来像一堆针的表示。为了解决这个问题，我们提出了正则化优化和基于深度的初始化。我们的关键思想是引入一种可以在2D图像空间中控制的结构化高斯表示。然后，我们约束高斯，特别是它们的位置，并防止它们在优化过程中独立移动。具体来说，我们分别通过隐式卷积解码器和总变化损失引入单视角和多视角约束。通过向高斯引入相干性，我们通过基于流量的损失函数进一步约束优化。为了支持我们的正则化优化，我们提出了一种在每个输入视图使用单目深度估计来初始化高斯的方法。我们在各种场景中展示了与最先进的基于稀疏视图NeRF的方法相比的显著改进。 et.al.|[2403.19495](http://arxiv.org/abs/2403.19495)|null|
|**2024-03-28**|**Mesh2NeRF: Direct Mesh Supervision for Neural Radiance Field Representation and Generation**|我们提出了Mesh2NeRF，这是一种从纹理网格中导出地面实况辐射场的方法，用于3D生成任务。许多3D生成方法将3D场景表示为用于训练的辐射场。它们的地面实况辐射场通常是从大规模合成3D数据集的多视图渲染中拟合的，这通常会由于遮挡或拟合不足而导致伪影。在Mesh2NeRF中，我们提出了一种从3D网格直接获得地面实况辐射场的解析解，用具有定义表面厚度的占有函数来表征密度场，并通过考虑网格和环境照明的反射函数来确定与视图相关的颜色。Mesh2NeRF提取准确的辐射场，为训练生成NeRF和单场景表示提供直接监督。我们验证了Mesh2NeRF在各种任务中的有效性，在ABO数据集的单场景表示中，视图合成的PSNR显著提高了3.12dB，在ShapeNet Cars的单视图条件生成中，PSNR提高了0.69，在Ob厌恶Mugs的无条件生成中显著提高了NeRF的网格提取。 et.al.|[2403.19319](http://arxiv.org/abs/2403.19319)|null|
|**2024-03-27**|**MetaCap: Meta-learning Priors from Multi-View Imagery for Sparse-view Human Performance Capture and Rendering**|在视觉和图形学中，从稀疏的RGB观测中获取真实的人类性能和自由视图渲染是一个长期存在的问题。主要挑战是缺乏观察和环境的固有模糊性，例如遮挡和深度模糊。因此，辐射场在密集设置中捕捉高频外观和几何细节方面显示出巨大的前景，na时表现不佳\“在稀疏摄像机视图上对其进行有效监督，因为场只是过度适应稀疏视图输入。为了解决这一问题，我们提出了MetaCap，这是一种在人类非常稀疏甚至单个视图的情况下进行高效高质量几何恢复和新视图合成的方法。我们的关键思想是仅从潜在的稀疏多视图视频中元学习辐射场权重，这可以作为在描绘人类的稀疏图像上微调辐射场权重的先验。这种先验提供了良好的网络权重初始化，从而有效地解决稀疏视图捕获中的模糊性。由于人体的关节结构和运动引起的表面变形，学习这种先验是不容易的。因此，我们建议在姿势规范化空间中元学习场权重。”，这减少了空间特征范围，使特征学习更加有效。因此，人们可以微调我们的场参数，以快速推广到看不见的姿势，即我们ll作为新颖且稀疏（甚至是单目）的相机视图。为了在不同的场景下评估我们的方法，我们收集了一个新的数据集WildDynaCap，其中包含在密集摄像机圆顶和野生稀疏摄像机平台中拍摄的受试者，并在公共和WildDynaCap数据集上展示了与最新最先进的方法相比优越的结果。 et.al.|[2403.18820](http://arxiv.org/abs/2403.18820)|null|
|**2024-03-27**|**SplatFace: Gaussian Splat Face Reconstruction Leveraging an Optimizable Surface**|我们提出了SplatFace，这是一种新的高斯飞溅框架，用于三维人脸重建，而不依赖于精确的预定几何结构。我们的方法旨在同时提供高质量的新颖视图渲染和精确的3D网格重建。我们结合了一个通用的3D变形模型（3DMM）来提供表面几何结构，从而可以用有限的一组输入图像重建人脸。我们引入了一种联合优化策略，该策略通过协同的非刚性对齐过程来细化高斯曲面和可变形曲面。提出了一种新的距离度量，即飞溅到表面，通过考虑高斯位置和协方差来改进对准。表面信息还被用于结合世界空间致密化过程，从而获得卓越的重建质量。我们的实验分析表明，在生成具有高几何精度的三维人脸网格方面，所提出的方法在新的视图合成中与其他高斯飞溅技术和其他三维重建方法都具有竞争力。 et.al.|[2403.18784](http://arxiv.org/abs/2403.18784)|null|
|**2024-03-27**|**Modeling uncertainty for Gaussian Splatting**|我们提出了随机高斯散射（SGS）：第一个使用高斯散射（GS）进行不确定性估计的框架。GS最近以神经辐射场（NeRF）的一小部分计算成本实现了令人印象深刻的重建质量，从而推进了新的视图合成领域。然而，与后者相反，它仍然缺乏提供与产出相关的置信度信息的能力。为了解决这一局限性，在本文中，我们引入了一种基于变分推理的方法，该方法将不确定性预测无缝集成到GS的公共渲染管道中。此外，我们引入稀疏误差下面积（AUSE）作为损失函数中的一个新项，从而能够在图像重建的同时优化不确定性估计。在LLFF数据集上的实验结果表明，我们的方法在图像渲染质量和不确定性估计精度方面都优于现有方法。总的来说，我们的框架为从业者提供了对合成视图可靠性的宝贵见解，有助于在现实世界的应用程序中进行更安全的决策。 et.al.|[2403.18476](http://arxiv.org/abs/2403.18476)|null|
|**2024-03-26**|**2D Gaussian Splatting for Geometrically Accurate Radiance Fields**|3D高斯散射（3DGS）最近彻底改变了辐射场重建，实现了高质量的新颖视图合成和快速的无烘焙渲染速度。然而，由于3D高斯的多视图不一致性，3DGS无法准确地表示曲面。我们提出了二维高斯散射（2DGS），这是一种从多视图图像中建模和重建几何精确辐射场的新方法。我们的关键思想是将三维体积压缩为一组二维平面高斯圆盘。与3D高斯模型不同，2D高斯模型在对曲面进行本质建模的同时，提供了视图一致的几何图形。为了准确地恢复薄表面并实现稳定的优化，我们引入了一种利用射线散射相交和光栅化的透视精确二维散射过程。此外，我们结合了深度失真和法线一致性项，以进一步提高重建的质量。我们证明，我们的可微分渲染器允许无噪声和详细的几何重建，同时保持有竞争力的外观质量、快速训练速度和实时渲染。我们的代码将公开。 et.al.|[2403.17888](http://arxiv.org/abs/2403.17888)|null|
|**2024-03-26**|**DN-Splatter: Depth and Normal Priors for Gaussian Splatting and Meshing**|3D高斯飞溅是一种新的可微分绘制技术，以高的绘制速度和相对较低的训练时间获得了最先进的新视图合成结果。然而，由于优化过程中缺乏几何约束，它在室内数据集中常见的场景上的性能较差。我们扩展了具有深度和法线线索的3D高斯飞溅，以应对具有挑战性的室内数据集，并展示了高效网格提取技术，这是一个重要的下游应用。具体来说，我们用深度信息正则化优化过程，增强附近高斯的局部平滑性，并使用由法线线索监督的3D高斯的几何结构来实现与真实场景几何结构的更好对齐。我们在基线上改进了深度估计和新的视图合成结果，并展示了如何使用这种简单而有效的正则化技术直接从高斯表示中提取网格，从而在室内场景上产生更精确的物理重建。我们的代码将于发布https://github.com/maturk/dn-splatter. et.al.|[2403.17822](http://arxiv.org/abs/2403.17822)|null|

<p align=right>(<a href=#updated-on-20240331>back to top</a>)</p>

## 3D Reconstruction

|Publish Date|Title|Abstract|PDF|Code|
|---|---|---|---|---|
|**2024-03-28**|**CoherentGS: Sparse Novel View Synthesis with Coherent 3D Gaussians**|在过去的几年里，从图像进行3D重建的领域迅速发展，首先是引入了神经辐射场（NeRF），最近又引入了3D高斯散射（3DGS）。后者在训练和推理速度以及重建质量方面提供了优于NeRF的显著优势。尽管3DGS适用于密集的输入图像，但非结构化的点云状表示很快过度适应极稀疏的输入图像（例如，3个图像）的更具挑战性的设置，从而从新颖的视图中创建出看起来像一堆针的表示。为了解决这个问题，我们提出了正则化优化和基于深度的初始化。我们的关键思想是引入一种可以在2D图像空间中控制的结构化高斯表示。然后，我们约束高斯，特别是它们的位置，并防止它们在优化过程中独立移动。具体来说，我们分别通过隐式卷积解码器和总变化损失引入单视角和多视角约束。通过向高斯引入相干性，我们通过基于流量的损失函数进一步约束优化。为了支持我们的正则化优化，我们提出了一种在每个输入视图使用单目深度估计来初始化高斯的方法。我们在各种场景中展示了与最先进的基于稀疏视图NeRF的方法相比的显著改进。 et.al.|[2403.19495](http://arxiv.org/abs/2403.19495)|null|
|**2024-03-28**|**Total-Decom: Decomposed 3D Scene Reconstruction with Minimal Interaction**|从多视点图像重建场景是计算机视觉和图形学中的一个基本问题。最近的神经隐式表面重建方法已经获得了高质量的结果；然而，由于缺乏自然分解的对象实体和复杂的对象/背景组成，编辑和操纵重建场景的3D几何结构仍然具有挑战性。在本文中，我们提出了Total Decom，这是一种在最小化人类交互的情况下进行分解三维重建的新方法。我们的方法将Segment Anything Model（SAM）与混合隐式-显式神经表面表示和基于网格的区域生长技术无缝集成，用于精确的3D对象分解。Total Decom需要最少的人工注释，同时为用户提供对分解粒度和质量的实时控制。我们在基准数据集上广泛评估了我们的方法，并展示了其在动画和场景编辑等下游应用中的潜力。代码位于\ href{https://github.com/CVMI-Lab/Total-Decom.git}{https://github.com/CVMI-Lab/Total-Decom.git}. et.al.|[2403.19314](http://arxiv.org/abs/2403.19314)|**[link](https://github.com/cvmi-lab/total-decom)**|
|**2024-03-28**|**Neural Fields for 3D Tracking of Anatomy and Surgical Instruments in Monocular Laparoscopic Video Clips**|腹腔镜视频跟踪主要关注两种目标类型：手术器械和解剖结构。前者可用于技能评估，而后者对于虚拟覆盖的投影是必要的。在仪器和解剖跟踪通常被视为两个独立的问题的情况下，在本文中，我们提出了一种同时对所有结构进行联合跟踪的方法。基于单个2D单眼视频剪辑，我们训练神经场来表示连续的时空场景，用于创建至少一帧中可见的所有表面的3D轨迹。由于仪器尺寸较小，它们通常只覆盖图像的一小部分，导致跟踪精度下降。因此，我们建议增强类权重以改善仪器轨迹。我们评估了对腹腔镜胆囊切除术视频片段的跟踪，发现解剖结构和器械的平均跟踪准确率分别为92.4%和87.4%。此外，我们还评估了从该方法的场景重建中获得的深度图的质量。我们表明，这些伪深度具有与最先进的预训练深度估计器相当的质量。在SCARED数据集中的腹腔镜视频上，该方法预测深度的MAE为2.9 mm，相对误差为9.2%。这些结果表明了使用神经场进行腹腔镜场景的单目3D重建的可行性。 et.al.|[2403.19265](http://arxiv.org/abs/2403.19265)|null|
|**2024-03-27**|**WALT3D: Generating Realistic Training Data from Time-Lapse Imagery for Reconstructing Dynamic Objects under Occlusion**|当前的2D和3D对象理解方法在繁忙的城市环境中难以解决严重的遮挡问题，部分原因是缺乏用于学习遮挡的大规模标记地面实况注释。在这项工作中，我们介绍了一种新的框架，用于使用免费可用的延时图像自动生成遮挡下动态对象的大型逼真数据集。通过利用现成的2D（边界框、分割、关键点）和3D（姿势、形状）预测作为伪背景，可以自动识别未遮挡的3D对象，并以剪贴画风格将其合成到背景中，确保逼真的外观和物理上准确的遮挡配置。所得到的具有伪背景真相的剪贴画图像能够有效地训练对遮挡鲁棒的对象重建方法。我们的方法在2D和3D重建方面都有显著改进，特别是在城市场景中车辆和人等物体被严重遮挡的场景中。 et.al.|[2403.19022](http://arxiv.org/abs/2403.19022)|null|
|**2024-03-27**|**Gamba: Marry Gaussian Splatting with Mamba for single view 3D reconstruction**|随着对自动化3D内容创建管道的需求不断增长，我们解决了从单个图像高效重建3D资产的挑战。以前的方法主要依赖于分数蒸馏采样（SDS）和神经辐射场（NeRF）。尽管这些方法取得了显著的成功，但由于漫长的优化和大量的内存使用，它们遇到了实际的局限性。在本报告中，我们介绍了Gamba，一种基于单视图图像的端到端摊销3D重建模型，强调了两个主要见解：（1）3D表示：利用大量的3D高斯进行高效的3D高斯飞溅过程；（2） 骨干设计：引入基于Mamba的序列网络，该网络有助于上下文相关推理和序列（令牌）长度的线性可伸缩性，可容纳大量高斯。Gamba在数据预处理、正则化设计和训练方法方面取得了重大进展。我们使用真实世界扫描的OmniObject3D数据集，对照现有的基于优化和前馈的3D生成方法对Gamba进行了评估。在这里，Gamba在质量和数量上都展示了具有竞争力的生成能力，同时在单个NVIDIA A100 GPU上实现了约0.6秒的惊人速度。 et.al.|[2403.18795](http://arxiv.org/abs/2403.18795)|null|
|**2024-03-27**|**SplatFace: Gaussian Splat Face Reconstruction Leveraging an Optimizable Surface**|我们提出了SplatFace，这是一种新的高斯飞溅框架，用于三维人脸重建，而不依赖于精确的预定几何结构。我们的方法旨在同时提供高质量的新颖视图渲染和精确的3D网格重建。我们结合了一个通用的3D变形模型（3DMM）来提供表面几何结构，从而可以用有限的一组输入图像重建人脸。我们引入了一种联合优化策略，该策略通过协同的非刚性对齐过程来细化高斯曲面和可变形曲面。提出了一种新的距离度量，即飞溅到表面，通过考虑高斯位置和协方差来改进对准。表面信息还被用于结合世界空间致密化过程，从而获得卓越的重建质量。我们的实验分析表明，在生成具有高几何精度的三维人脸网格方面，所提出的方法在新的视图合成中与其他高斯飞溅技术和其他三维重建方法都具有竞争力。 et.al.|[2403.18784](http://arxiv.org/abs/2403.18784)|null|
|**2024-03-27**|**Breaking the Limitations with Sparse Inputs by Variational Frameworks (BLIss) in Terahertz Super-Resolution 3D Reconstruction**|数据采集、图像处理和图像质量是太赫兹（THz）3D重建成像的长期问题。考虑到与获得超分辨率（SR）数据相关的挑战以及传统计算机断层扫描（CT）中缺乏有效的SR 3D重建框架，现有方法主要针对2D场景设计。在这里，我们演示了BLIss，这是一种使用稀疏2D数据输入进行THz-SR 3D重建的新方法。BLIss将传统的CT技术和变分框架与基于Euler Elastica的自适应模型的核心无缝集成。定量的3D图像评估指标，包括高斯的标准差、平均曲率和多尺度结构相似性指数测度（MS-SSIM），验证了与传统的THz-CT模态相比，我们的变分框架方法所实现的优越的平滑度和保真度。除了对推进THz-SR 3D重建的贡献外，BLIss还展示了其在其他成像模式（如X射线和MRI）中的潜在适用性。这表明它对更广泛的成像应用领域产生了广泛的影响。 et.al.|[2403.18776](http://arxiv.org/abs/2403.18776)|**[link](https://github.com/cyiyoo/bliss)**|
|**2024-03-27**|**SAT-NGP : Unleashing Neural Graphics Primitives for Fast Relightable Transient-Free 3D reconstruction from Satellite Imagery**|当前的立体视觉管道在使用多对或三组卫星图像时产生高精度的3D重建。然而，这些管道对多日期采集可能导致的图像之间的变化很敏感。这种变化主要是由于可变的阴影、反射和瞬态物体（汽车、植被）。为了考虑到这些变化，神经辐射场（NeRF）最近被应用于多日期卫星图像。然而，神经方法是计算密集型的，需要几十个小时才能学习，而标准立体视觉管道需要几分钟。遵循即时神经图形原语的思想，我们建议使用有效的采样策略和多分辨率哈希编码来加速学习。我们的模型，卫星神经图形原件（SAT-NGP）将学习时间减少到15分钟，同时保持3D重建的质量。 et.al.|[2403.18711](http://arxiv.org/abs/2403.18711)|null|
|**2024-03-27**|**MonoHair: High-Fidelity Hair Modeling from a Monocular Video**|毫无疑问，高保真度的3D头发对于实现真实感、艺术表达和沉浸在计算机图形中至关重要。虽然现有的3D头发建模方法已经取得了令人印象深刻的性能，但实现高质量头发重建的挑战仍然存在：它们要么需要严格的捕捉条件，使实际应用变得困难，要么严重依赖于学习的先验数据，模糊了图像中的细粒度细节。为了应对这些挑战，我们提出了MonoHair，这是一种通用框架，用于从单眼视频中实现高保真头发重建，而无需对环境提出特定要求。我们的方法将头发建模过程分为两个主要阶段：精确的外部重建和内部结构推断。外部使用我们的基于补丁的多视图优化（PMVO）精心制作。该方法独立于先前的数据，从多个视图战略性地收集和集成头发信息，以生成高保真的外部3D线图。这张地图不仅捕捉到了复杂的细节，而且有助于推断头发的内部结构。对于内部，我们采用了数据驱动的多视图3D头发重建方法。该方法利用从重建的外部导出的2D结构渲染，镜像训练期间使用的合成2D输入。这种对齐有效地弥合了我们的训练数据和真实世界数据之间的领域差距，从而提高了我们内部结构推断的准确性和可靠性。最后，我们生成了一个头发束模型，并通过我们的头发生长算法解决了方向模糊问题。我们的实验表明，我们的方法在各种发型中都表现出了稳健性，并实现了最先进的性能。有关更多结果，请参阅我们的项目页面https://keyuwu-cs.github.io/MonoHair/. et.al.|[2403.18356](http://arxiv.org/abs/2403.18356)|null|
|**2024-03-26**|**EgoLifter: Open-world 3D Segmentation for Egocentric Perception**|在本文中，我们介绍了EgoLifter，这是一种新的系统，可以自动将从以自我为中心的传感器捕获的场景分割为单个3D对象的完整分解。该系统专门为以自我为中心的数据而设计，其中场景包含数百个从自然（非扫描）运动中捕获的对象。EgoLifter采用3D高斯作为3D场景和对象的底层表示，并使用来自Segment Anything Model（SAM）的分割掩码作为弱监督，以学习对象实例的灵活和可提示的定义，而不需要任何特定的对象分类法。为了应对以自我为中心的视频中动态对象的挑战，我们设计了一个瞬态预测模块，该模块学习在3D重建中过滤掉动态对象。其结果是一个完全自动的管道，能够将3D对象实例重建为共同组成整个场景的3D高斯集合。我们在Aria Digital Twin数据集上创建了一个新的基准，该数据集定量展示了其在自然自我中心输入的开放世界3D分割中的最先进性能。我们在各种以自我为中心的活动数据集上运行了EgoLifter，这表明了该方法在规模上实现3D自我中心感知的前景。 et.al.|[2403.18118](http://arxiv.org/abs/2403.18118)|null|

<p align=right>(<a href=#updated-on-20240331>back to top</a>)</p>

## Diffusion

|Publish Date|Title|Abstract|PDF|Code|
|---|---|---|---|---|
|**2024-03-28**|**GaussianCube: Structuring Gaussian Splatting using Optimal Transport for 3D Generative Modeling**|3D高斯散射（GS）在3D拟合保真度和渲染速度方面比神经辐射场有了相当大的改进。然而，这种具有分散高斯的非结构化表示对生成建模提出了重大挑战。为了解决这个问题，我们引入了GaussianCube，这是一种结构化的GS表示，对于生成建模来说既强大又高效。我们首先提出了一种改进的致密化约束GS拟合算法，该算法可以使用固定数量的自由高斯来产生高质量的拟合结果，然后通过最优传输将高斯重新排列到预定义的体素网格中。结构化网格表示允许我们使用标准的3D U-Net作为扩散生成建模的主干，而无需精心设计。在ShapeNet和OmniObject3D上进行的大量实验表明，我们的模型在定性和定量方面都取得了最先进的生成结果，突显了GaussianCube作为一种强大而通用的3D表示的潜力。 et.al.|[2403.19655](http://arxiv.org/abs/2403.19655)|null|
|**2024-03-28**|**Detecting Image Attribution for Text-to-Image Diffusion Models in RGB and Beyond**|现代文本到图像（T2I）扩散模型可以生成具有显著真实性和创造性的图像。这些进步引发了对假图像检测和归因的研究，但先前的研究尚未充分探索这项任务的实用性和科学性。除了将图像归因于12个最先进的T2I生成器之外，我们还对哪些推理阶段的超参数和图像修改是可辨别的进行了广泛的分析。我们的实验表明，初始化种子是高度可检测的，在某种程度上还有图像生成过程中的其他细微变化。我们通过扰动高频细节和使用图像风格和结构的中级表示，进一步研究了哪些视觉痕迹在图像归因中被利用。值得注意的是，改变高频信息只会导致准确性的轻微降低，并且在风格表示上训练属性器的效果优于在RGB图像上训练。我们的分析强调，与之前探索的相比，假图像在不同的视觉粒度水平上都是可检测和可归因的。 et.al.|[2403.19653](http://arxiv.org/abs/2403.19653)|**[link](https://github.com/k8xu/imageattribution)**|
|**2024-03-28**|**InterDreamer: Zero-Shot Text to 3D Dynamic Human-Object Interaction**|文本条件下的人类运动生成在基于广泛的运动捕捉数据和相应的文本注释训练的扩散模型方面取得了重大进展。然而，将这种成功扩展到3D动态人机交互（HOI）生成面临着显著的挑战，主要是由于缺乏与这些交互一致的大规模交互数据和全面描述。本文采取主动，展示了在不直接训练文本交互对数据的情况下生成人机交互的潜力。我们实现这一点的关键见解是，交互语义和动力学可以解耦。由于无法通过监督训练学习交互语义，我们转而利用预先训练的大型模型，协同来自大型语言模型和文本到运动模型的知识。虽然这些知识提供了对交互语义的高级控制，但它无法掌握低级交互动力学的复杂性。为了克服这个问题，我们进一步引入了一个旨在理解简单物理的世界模型，对人类行为如何影响物体运动进行建模。通过集成这些组件，我们的新框架InterDreamer能够以零样本的方式生成文本对齐的3D HOI序列。我们将InterDreamer应用于BEHAVE和CHAIRS数据集，我们的全面实验分析证明了它能够生成与文本指令无缝一致的真实连贯的交互序列。 et.al.|[2403.19652](http://arxiv.org/abs/2403.19652)|null|
|**2024-03-28**|**GANTASTIC: GAN-based Transfer of Interpretable Directions for Disentangled Image Editing in Text-to-Image Diffusion Models**|图像生成模型的快速发展主要是由扩散模型推动的，扩散模型在根据文本提示生成高保真、多样化的图像方面取得了无与伦比的成功。尽管它们取得了成功，但扩散模型在图像编辑领域遇到了巨大的挑战，特别是在执行针对图像特定属性的非纠缠编辑更改时，而不影响无关部分。相比之下，生成对抗性网络（GANs）因其通过可解释的潜在空间成功地解开了编辑的纠缠而受到认可。我们介绍了GANTASTIC，这是一种新的框架，它从预先训练的代表特定可控属性的GAN模型中获取现有方向，并将这些方向转移到基于扩散的模型中。这种新颖的方法不仅保持了扩散模型众所周知的生成质量和多样性，而且显著增强了它们执行精确、有针对性的图像编辑的能力，从而实现了两全其美。 et.al.|[2403.19645](http://arxiv.org/abs/2403.19645)|null|
|**2024-03-28**|**In the driver's mind: modeling the dynamics of human overtaking decisions in interactions with oncoming automated vehicles**|了解超车场景中的人类行为对于提高自动车辆混合交通中的道路安全至关重要。行为的计算模型在推进这一理解方面发挥着关键作用，因为它们可以提供超越实证研究的人类行为泛化的见解。然而，现有的人类超车行为研究和模型大多集中在迎面而来的车辆动力学简单、恒定的场景上，而忽略了AV通过隐性沟通主动影响人类驾驶员决策过程的潜力。此外，到目前为止，还不知道人类驾驶员的超车决策是否会受到他们是否与AV或人类驾驶车辆（HDV）互动的影响。为了解决这些差距，我们对30名参与者进行了“反向绿野仙踪”驾驶模拟器实验，他们反复与迎面而来的自动驾驶汽车和HDV互动，测量驾驶员的差距接受决定和响应时间。迎面而来的车辆具有时变动力学特性，旨在通过短暂减速然后恢复到初始速度来影响参与者的超车决策。我们发现，与HDV相比，参与者在与迎面而来的AV互动时不会改变他们的超车行为。此外，我们没有发现任何证据表明迎面而来的车辆短暂减速会影响参与者的决策或反应时间。对所获得数据的认知建模表明，具有动态漂移率和速度相关决策偏差的广义漂移扩散模型最能解释实验中观察到的间隙接受结果和响应时间。总的来说，我们的发现突出了认知模型的潜力，可以进一步推动人类驾驶员和自动驾驶汽车在超车过程中更安全互动的持续发展。 et.al.|[2403.19637](http://arxiv.org/abs/2403.19637)|null|
|**2024-03-28**|**Generalisation of the Spectral Difference scheme for the diffused-interface five equation model**|本工作的重点是将谱差（SD）格式推广到简化的Baer-Nunziato系统，即用于模拟两种不混溶可压缩流体的五方程模型。该五方程模型考虑了额外的Allen-Cahn正则化，以避免表示界面的相场的过度扩散和过度稀疏。最后，为了保持接触不连续性，在谱差分格式的重建步骤中，使用了变量从保守到原始的变化。这种方法被证明有利于避免材料界面处的压力振荡。提出了一系列广泛的数值测试来评估本方法的准确性和稳健性。同时考虑了运动学（Rider Kothe涡）和两相流问题（Rayleigh Taylor不稳定性、冲击液滴相互作用、Taylor Green涡）。 et.al.|[2403.19623](http://arxiv.org/abs/2403.19623)|null|
|**2024-03-28**|**More on Black Holes Perceiving the Dark Dimension**|在过去的两年里，暗维度场景已经成为许多研究兴趣的焦点。特别是，它起到了解决宇宙学层次问题的垫脚石的作用，并为暗物质竞争者提供了一个竞技场。我们重新审视了感知暗维度的原始黑洞（PBH）可能构成宇宙中所有暗物质的可能性。我们重新评估了霍金蒸发产生的 $\gamma$-射线发射对作为暗物质候选者的PBH丰度的限制。我们重新评估了银河系中心方向上散射$\gamma$-射线发射的约束，这为由PBH组成的暗物质部分提供了最佳和最固体的上限。允许PBH组装所有宇宙学暗物质的修正质量范围估计为$10^｛15｝\alt M_｛\rm BH｝/｛\rmg｝\alt 10^｛21｝$。我们证明，由于$\gamma$射线发射的限制，推测记忆负担效应引起的量子校正不会改变这个质量范围。我们还研究了PBHs的主要特征，这些特征定位在本体中。我们证明，如果$10^{11}\alt M_｛\rm BH｝/｛\rmg｝\alt 10^{21}$ ，定域在体中的PBH可以形成所有宇宙学暗物质。最后，我们评论一下，如果我们提倡一个有两个暗维度边界的空间，那么可能会产生黑洞。 et.al.|[2403.19604](http://arxiv.org/abs/2403.19604)|null|
|**2024-03-28**|**Enhance Image Classification via Inter-Class Image Mixup with Diffusion Model**|文本到图像（T2I）生成模型最近成为一种强大的工具，能够创建照片逼真的图像，并产生大量应用。然而，将T2I模型有效地集成到基本的图像分类任务中仍然是一个悬而未决的问题。提高图像分类性能的一种流行策略是通过用T2I模型生成的合成图像来增强训练集。在这项研究中，我们仔细检查了当前生成和传统数据增强技术的缺点。我们的分析表明，这些方法很难产生对特定领域概念既忠实（就前景对象而言）又多样化（就背景上下文而言）的图像。为了应对这一挑战，我们引入了一种创新的类间数据增强方法，称为Diff-Mix(https://github.com/Zhicaiwww/Diff-Mix)，通过在类之间执行图像转换来丰富数据集。我们的实证结果表明，Diff-Mix在忠实性和多样性之间实现了更好的平衡，从而显著提高了不同图像分类场景的性能，包括特定领域数据集的少镜头、传统和长尾分类。 et.al.|[2403.19600](http://arxiv.org/abs/2403.19600)|**[link](https://github.com/zhicaiwww/diff-mix)**|
|**2024-03-28**|**Frame by Familiar Frame: Understanding Replication in Video Diffusion Models**|基于图像生成扩散模型的势头，人们对基于视频的扩散模型越来越感兴趣。然而，由于视频生成的高维性、训练数据的稀缺性以及所涉及的复杂时空关系，它带来了更大的挑战。图像生成模型由于其广泛的数据需求，已经将计算资源限制在极限。这些模型从训练样本中复制元素的例子，导致了对样本复制的担忧，甚至法律纠纷。视频扩散模型使用更受约束的数据集，并负责生成空间和时间内容，可能更倾向于从其训练集中复制样本。使问题更加复杂的是，这些模型通常使用无意中奖励复制的指标进行评估。在我们的论文中，我们对视频扩散模型中的样本复制现象进行了系统的研究。我们仔细研究了最近用于视频合成的各种扩散模型，评估了它们在无条件和有条件生成场景中复制空间和时间内容的趋势。我们的研究确定了不太可能导致复制的策略。此外，我们提出了将复制考虑在内的新评估策略，从而更准确地衡量模型生成原始内容的能力。 et.al.|[2403.19593](http://arxiv.org/abs/2403.19593)|null|
|**2024-03-28**|**Keypoint Action Tokens Enable In-Context Imitation Learning in Robotics**|我们展示了现成的基于文本的变形金刚，在没有额外训练的情况下，可以进行少量的上下文视觉模仿学习，将视觉观察映射到模仿演示者行为的动作序列。我们通过将视觉观察（输入）和动作轨迹（输出）转换为令牌序列来实现这一点，文本预训练的转换器（GPT-4 Turbo）可以通过我们称为关键点动作令牌（KAT）的框架摄取并生成令牌序列。尽管只接受过语言训练，但我们发现，这些变形金刚擅长将标记化的视觉关键点观察转化为行动轨迹，在一系列现实世界的日常任务中，在低数据状态下，表现与最先进的模仿学习（扩散策略）不相上下或更好。KAT不是像通常那样在语言领域中操作，而是利用基于文本的转换器在视觉和动作领域中操作来学习演示数据中的一般模式，以实现高效的模仿学习，这表明了将自然语言模型重新用于具体任务的有前景的新途径。视频可在https://www.robot-learning.uk/keypoint-action-tokens. et.al.|[2403.19578](http://arxiv.org/abs/2403.19578)|null|

<p align=right>(<a href=#updated-on-20240331>back to top</a>)</p>

## NeRF

|Publish Date|Title|Abstract|PDF|Code|
|---|---|---|---|---|
|**2024-03-28**|**Neural Fields for 3D Tracking of Anatomy and Surgical Instruments in Monocular Laparoscopic Video Clips**|腹腔镜视频跟踪主要关注两种目标类型：手术器械和解剖结构。前者可用于技能评估，而后者对于虚拟覆盖的投影是必要的。在仪器和解剖跟踪通常被视为两个独立的问题的情况下，在本文中，我们提出了一种同时对所有结构进行联合跟踪的方法。基于单个2D单眼视频剪辑，我们训练神经场来表示连续的时空场景，用于创建至少一帧中可见的所有表面的3D轨迹。由于仪器尺寸较小，它们通常只覆盖图像的一小部分，导致跟踪精度下降。因此，我们建议增强类权重以改善仪器轨迹。我们评估了对腹腔镜胆囊切除术视频片段的跟踪，发现解剖结构和器械的平均跟踪准确率分别为92.4%和87.4%。此外，我们还评估了从该方法的场景重建中获得的深度图的质量。我们表明，这些伪深度具有与最先进的预训练深度估计器相当的质量。在SCARED数据集中的腹腔镜视频上，该方法预测深度的MAE为2.9 mm，相对误差为9.2%。这些结果表明了使用神经场进行腹腔镜场景的单目3D重建的可行性。 et.al.|[2403.19265](http://arxiv.org/abs/2403.19265)|null|
|**2024-03-28**|**From Activation to Initialization: Scaling Insights for Optimizing Neural Fields**|在计算机视觉领域，神经场作为一种利用神经网络进行信号表示的现代工具，已经获得了突出地位。尽管在调整这些网络以解决各种问题方面取得了显著进展，但该领域仍然缺乏一个全面的理论框架。本文旨在通过深入研究初始化和激活之间复杂的相互作用来解决这一差距，为神经领域的稳健优化提供基础。我们的理论见解揭示了网络初始化、架构选择和优化过程之间的深层次联系，强调在设计尖端神经场时需要整体方法。 et.al.|[2403.19205](http://arxiv.org/abs/2403.19205)|null|
|**2024-03-22**|**LATTE3D: Large-scale Amortized Text-To-Enhanced3D Synthesis**|最近的文本到3D生成方法产生了令人印象深刻的3D结果，但需要耗时的优化，每次提示可能需要一个小时。ATT3D等摊销方法同时优化多个提示以提高效率，实现快速的文本到三维合成。然而，它们无法捕捉高频几何体和纹理细节，并且难以缩放到大型提示集，因此泛化能力较差。我们引入LATTE3D，解决了这些限制，以在更大的提示集上实现快速、高质量的生成。我们方法的关键是1）构建可扩展的体系结构，2）在优化过程中通过3D感知扩散先验、形状正则化和模型初始化来利用3D数据，以实现对各种复杂训练提示的鲁棒性。LATTE3D对神经场和纹理表面生成进行摊销，以在单个正向过程中生成高度详细的纹理网格。LATTE3D在400ms内生成3D对象，并可通过快速测试时间优化进一步增强。 et.al.|[2403.15385](http://arxiv.org/abs/2403.15385)|null|
|**2024-03-20**|**Visual Imitation Learning of Task-Oriented Object Grasping and Rearrangement**|面向任务的物体抓取和重排是机器人完成不同现实操作任务的关键技能。然而，由于对物体的部分观察和分类物体的形状变化，它们仍然具有挑战性。在本文中，我们提出了多特征隐式模型（MIMO），这是一种新的对象表示，它在隐式神经场中对点和对象之间的多个空间特征进行编码。在多个特征上训练这样的模型可以确保它在不同方面一致地嵌入物体形状，从而提高其在从局部观察、形状相似性测量和建模物体之间的空间关系的物体形状重建中的性能。基于MIMO，我们提出了一个从单个或多个人类演示视频中学习面向任务的对象抓取和重排的框架。仿真评估表明，我们的方法在多视图和单视图观测方面优于最先进的方法。真实世界的实验证明了我们的方法在操纵任务的单次和少次模仿学习中的有效性。 et.al.|[2403.14000](http://arxiv.org/abs/2403.14000)|null|
|**2024-03-18**|**LN3Diff: Scalable Latent Neural Fields Diffusion for Speedy 3D Generation**|随着生成模型和可微分绘制技术的进步，神经绘制领域取得了重大进展。尽管2D扩散已经取得了成功，但统一的3D扩散管道仍然悬而未决。本文介绍了一种称为LN3Diff的新框架来解决这一差距，并实现快速、高质量和通用的条件3D生成。我们的方法利用3D感知架构和变分自动编码器（VAE）将输入图像编码到结构化、紧凑和3D潜在空间中。潜像由基于变换器的解码器解码为高容量的3D神经场。通过在这个3D感知的潜在空间上训练扩散模型，我们的方法在ShapeNet上实现了最先进的3D生成性能，并在各种数据集的单目3D重建和条件3D生成中表现出卓越的性能。此外，它在推理速度方面超过了现有的3D扩散方法，不需要每实例优化。我们提出的LN3Diff在三维生成建模方面取得了重大进展，并有望在三维视觉和图形任务中应用。 et.al.|[2403.12019](http://arxiv.org/abs/2403.12019)|null|
|**2024-03-15**|**NeuralOCT: Airway OCT Analysis via Neural Fields**|光学相干断层扫描（OCT）是眼科中一种流行的模式，也用于血管内。我们对这项工作的兴趣是在婴儿和儿童气道异常的背景下进行OCT，其中OCT的高分辨率和无辐射的事实很重要。气道OCT的目标是提供气道几何形状的准确估计（2D和3D），以评估气道异常，如声门下狭窄。我们提出 $\texttt｛NeuralOCT｝$，这是一种基于学习的方法来处理气道OCT图像。具体而言，$\texttt｛NeuralOCT｝$通过稳健地桥接两个步骤从OCT扫描中提取3D几何形状：通过2D分割提取点云和通过神经场从点云中重建3D。我们的实验表明，$\texttt｛NeuralOCT｝$ 可以产生准确而稳健的3D气道重建，平均A线误差小于70微米。我们的代码将在GitHub上提供。 et.al.|[2403.10622](http://arxiv.org/abs/2403.10622)|null|
|**2024-03-15**|**NECA: Neural Customizable Human Avatar**|人类化身已经成为一种具有各种应用的新型3D资产。理想情况下，人类化身应该是完全可定制的，以适应不同的设置和环境。在这项工作中，我们介绍了NECA，这是一种能够从单目或稀疏视图视频中学习多功能人体表示的方法，能够在姿势、阴影、形状、照明和纹理等方面进行细粒度定制。我们方法的核心是在互补的双空间中表示人类，并预测几何、反照率、阴影以及外部照明的解开神经场，从中我们能够通过体积渲染获得具有高频细节的真实感渲染。大量实验证明了我们的方法在真实感渲染以及各种编辑任务（如新颖的姿势合成和重新照明）方面优于最先进的方法。代码位于https://github.com/iSEE-Laboratory/NECA. et.al.|[2403.10335](http://arxiv.org/abs/2403.10335)|**[link](https://github.com/isee-laboratory/neca)**|
|**2024-03-13**|**Representing Anatomical Trees by Denoising Diffusion of Implicit Neural Fields**|解剖树在临床诊断和治疗计划中起着核心作用。然而，由于解剖树的拓扑结构和几何形状多变且复杂，因此准确地表示解剖树具有挑战性。使用医学成像捕获的表示树状结构的传统方法虽然对可视化血管和支气管网络非常宝贵，但在分辨率、灵活性和效率方面存在缺陷。最近，隐式神经表示（INRs）已经成为准确有效地表示形状的强大工具。我们提出了一种使用INR表示解剖树的新方法，同时还通过INR空间中的去噪扩散来捕捉一组树的分布。我们以任何所需的分辨率准确捕捉解剖树的复杂几何形状和拓扑结构。通过广泛的定性和定量评估，我们展示了高保真度树重建，具有任意分辨率但紧凑的存储，以及跨解剖部位和树复杂性的多功能性。 et.al.|[2403.08974](http://arxiv.org/abs/2403.08974)|**[link](https://github.com/sinashish/treediffusion)**|
|**2024-03-12**|**Scalable Spatiotemporal Prediction with Bayesian Neural Fields**|时空数据集由空间参考的时间序列组成，在许多科学和商业智能应用中无处不在，如空气污染监测、疾病跟踪和云需求预测。随着现代数据集的规模和复杂性不断增加，人们越来越需要新的统计方法，这些方法足够灵活，可以捕捉复杂的时空动态，并且可以扩展，可以处理大型预测问题。这项工作提出了贝叶斯神经场（BayesNF），这是一种用于推断时空域上丰富概率分布的域通用统计模型，可用于数据分析任务，包括预测、插值和变差法。BayesNF将一种用于高容量函数估计的新型深度神经网络架构与用于鲁棒不确定性量化的分层贝叶斯推理相结合。通过通过一系列平滑可微变换定义先验，使用通过随机梯度下降训练的变量学习代理对大规模数据进行后验推理。我们根据突出的统计和机器学习基线评估BayesNF，显示出在气候和公共卫生数据集的各种预测问题上的显著改进，这些数据集包含数万到数十万个测量值。该论文附有一个开源软件包(https://github.com/google/bayesnf)它易于使用，并与JAX机器学习平台上的现代GPU和TPU加速器兼容。 et.al.|[2403.07657](http://arxiv.org/abs/2403.07657)|**[link](https://github.com/google/bayesnf)**|
|**2024-03-11**|**SiLVR: Scalable Lidar-Visual Reconstruction with Neural Radiance Fields for Robotic Inspection**|我们提出了一种基于神经场的大规模重建系统，该系统融合激光雷达和视觉数据，生成几何精度高的高质量重建，并捕捉照片逼真的纹理。该系统采用了最先进的神经辐射场（NeRF）表示，还结合了激光雷达数据，这对深度和表面法线增加了强大的几何约束。我们利用实时激光雷达SLAM系统的轨迹来引导运动结构（SfM）过程，以显著减少计算时间，并提供对激光雷达深度损失至关重要的度量尺度。我们使用子映射将系统缩放到长轨迹上捕获的大规模环境。我们用多摄像头、激光雷达传感器套件的数据演示了重建系统，该套件安装在腿式机器人上，手持扫描600米的建筑场景，并安装在空中机器人上，测量多层模拟灾难现场建筑。网站https://ori-drs.github.io/projects/silvr/ et.al.|[2403.06877](http://arxiv.org/abs/2403.06877)|null|

<p align=right>(<a href=#updated-on-20240331>back to top</a>)</p>

[contributors-shield]: https://img.shields.io/github/contributors/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[contributors-url]: https://github.com/Vincentqyw/cv-arxiv-daily/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[forks-url]: https://github.com/Vincentqyw/cv-arxiv-daily/network/members
[stars-shield]: https://img.shields.io/github/stars/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[stars-url]: https://github.com/Vincentqyw/cv-arxiv-daily/stargazers
[issues-shield]: https://img.shields.io/github/issues/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[issues-url]: https://github.com/Vincentqyw/cv-arxiv-daily/issues

