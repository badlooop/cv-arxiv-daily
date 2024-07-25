[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]

## Updated on 2024.07.25
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
|**2024-07-24**|**SV4D: Dynamic 3D Content Generation with Multi-Frame and Multi-View Consistency**|我们提出了稳定视频4D（SV4D），这是一种用于多帧和多视图一致动态3D内容生成的潜在视频扩散模型。与之前依赖于单独训练的生成模型进行视频生成和新颖视图合成的方法不同，我们设计了一个统一的扩散模型来生成动态3D对象的新颖视图视频。具体来说，给定单眼参考视频，SV4D为每个视频帧生成时间上一致的新视图。然后，我们使用生成的新颖视图视频来有效地优化隐式4D表示（动态NeRF），而不需要大多数先前工作中使用的繁琐的基于SDS的优化。为了训练我们的统一新颖视图视频生成模型，我们从现有的Objaverse数据集中策划了一个动态3D对象数据集。多个数据集和用户研究的广泛实验结果表明，与先前的工作相比，SV4D在新视图视频合成和4D生成方面具有最先进的性能。 et.al.|[2407.17470](http://arxiv.org/abs/2407.17470)|null|
|**2024-07-24**|**Pose Estimation from Camera Images for Underwater Inspection**|高精度定位是水下复验任务的关键。惯性导航系统、多普勒速度记录仪和声学定位等传统定位方法面临着重大挑战，对于某些应用来说成本效益不高。在这种情况下，视觉定位是一种经济高效的替代方案，利用检查车辆上已经配备的摄像头从周围场景的图像中估计姿态。其中，基于机器学习的图像姿态估计在水下环境中显示出前景，使用基于先前映射场景训练的模型进行高效的重新定位。我们探索了基于学习的姿态估计器在清水和浑浊水检查任务中的有效性，评估了图像格式、模型架构和训练数据多样性的影响。我们通过采用新颖的视图合成模型来生成增强训练数据，从而显著增强了未探索区域的姿态估计。此外，我们通过扩展卡尔曼滤波器将姿态估计器输出与传感器数据相结合，提高了定位精度，证明了轨迹平滑度和精度的提高。 et.al.|[2407.16961](http://arxiv.org/abs/2407.16961)|null|
|**2024-07-23**|**DHGS: Decoupled Hybrid Gaussian Splatting for Driving Scene**|由于缺乏巧妙的设计和相关元素的几何约束，现有的高斯飞溅方法在驾驶场景中难以实现令人满意的新颖视图合成。本文介绍了一种称为解耦混合高斯散点（DHGS）的新方法，旨在提高驾驶场景新型视图合成的渲染质量。这项工作的新颖之处在于，用于道路和非道路层的解耦和混合像素级混合器，不需要为整个场景提供传统的统一可微渲染逻辑，同时通过提出的深度有序渲染策略保持一致和连续的叠加。除此之外，还训练了一个由符号距离场（SDF）组成的隐式道路表示，以监督具有微妙几何属性的路面。伴随着辅助透射率损失和一致性损失的使用，最终获得了具有不可察觉边界和高保真度的新图像。在Waymo数据集上的大量实验证明，DHGS的性能优于最先进的方法。 et.al.|[2407.16600](http://arxiv.org/abs/2407.16600)|null|
|**2024-07-23**|**HDRSplat: Gaussian Splatting for High Dynamic Range 3D Scene Reconstruction from Raw Images**|最近出现的3D高斯散斑（3DGS）彻底改变了3D场景重建空间，实现了实时高保真的新颖视图合成。然而，除了RawNeRF之外，所有先前的基于3DGS和NeRF的方法都依赖于8位色调映射的低动态范围（LDR）图像进行场景重建。这种方法难以在需要更高动态范围的场景中实现精确的重建。示例包括在夜间或光线不足的室内空间中拍摄的具有低信噪比的场景，以及阴影区域表现出极端对比度的日光场景。我们提出的方法HDRSplat定制3DGS，在近暗环境中直接在14位线性原始图像上训练，保留了场景的完整动态范围和内容。我们的主要贡献有两个方面：首先，我们提出了一种适合线性HDR空间损耗的方法，可以同时从嘈杂的暗区和接近饱和的亮区中有效地提取场景信息，同时处理与视图相关的颜色，而不会增加球谐波的程度。其次，通过仔细的光栅化调整，我们隐含地克服了3DGS对点云初始化的严重依赖和敏感性。这对于在低纹理、高景深和低照度区域进行精确重建至关重要。HDRSplat是迄今为止最快的方法，可以在15分钟/场景内完成14位（HDR）3D场景重建（比之前最先进的RawNeRF快30倍）。它还拥有最快的推理速度，为120fps。我们通过展示各种应用，如合成散焦、密集深度图提取以及曝光、色调映射和视点的捕捉后控制，进一步证明了HDR场景重建的适用性。 et.al.|[2407.16503](http://arxiv.org/abs/2407.16503)|null|
|**2024-07-22**|**BoostMVSNeRFs: Boosting MVS-based NeRFs to Generalizable View Synthesis in Large-scale Scenes**|虽然神经辐射场（NeRFs）表现出了卓越的质量，但其漫长的训练时间仍然是一个限制。可推广和基于MVS的NeRF虽然能够缩短训练时间，但往往会在质量上进行权衡。本文提出了一种称为BoostMVSNeRFs的新方法，以提高基于MVS的NeRF在大规模场景中的渲染质量。我们首先确定了基于MVS的NeRF方法的局限性，例如受限的视口覆盖和由于有限的输入视图引起的伪影。然后，我们通过提出一种在体绘制过程中选择和组合多个成本体积的新方法来解决这些局限性。我们的方法不需要训练，可以以前馈方式适应任何基于MVS的NeRF方法，以提高渲染质量。此外，我们的方法也是端到端可训练的，允许对特定场景进行微调。我们通过在大规模数据集上的实验证明了我们的方法的有效性，在大规模场景和无界户外场景中显示出显著的渲染质量改进。BoostMVSNeRFs的源代码发布于https://su-terry.github.io/BoostMVSNeRFs/. et.al.|[2407.15848](http://arxiv.org/abs/2407.15848)|null|
|**2024-07-22**|**6DGS: 6D Pose Estimation from a Single Image and a 3D Gaussian Splatting Model**|我们提出了6DGS来估计给定表示场景的3D高斯散斑（3DGS）模型的目标RGB图像的相机姿态。6DGS避免了典型的合成分析方法（如iNeRF）的迭代过程，该方法还需要初始化相机姿态才能收敛。相反，我们的方法通过反转3DGS渲染过程来估计6DoF姿态。从物体表面开始，我们定义了一个辐射Ellicell，它均匀地生成从每个椭球体出发的光线，这些椭球体对3DGS模型进行了参数化。每个Ellicell光线都与每个椭球体的渲染参数相关联，这些参数又用于获得目标图像像素和投射光线之间的最佳绑定。然后对这些像素光线绑定进行排序，以选择得分最高的光线束，它们的交点提供了相机中心，进而提供了相机旋转。所提出的解决方案消除了初始化时“先验”姿态的必要性，并以封闭形式解决了6DoF姿态估计问题，而不需要迭代。此外，与现有的用于姿态估计的新视图合成（NVS）基线相比，6DGS可以在真实场景中将整体平均旋转精度提高12%，平移精度提高22%，尽管不需要任何初始化姿态。同时，我们的方法近乎实时运行，在消费类硬件上达到15fps。 et.al.|[2407.15484](http://arxiv.org/abs/2407.15484)|null|
|**2024-07-19**|**SparseCraft: Few-Shot Neural Reconstruction through Stereopsis Guided Geometric Linearization**|我们提出了一种从少数彩色图像中恢复3D形状和视图相关外观的新方法，实现了高效的3D重建和新颖的视图合成。我们的方法以符号距离函数（SDF）和辐射场的形式学习隐式神经表示。该模型通过支持光线行进的体积渲染逐步训练，并使用无需学习的多视图立体（MVS）线索进行正则化。我们贡献的关键是一种新的隐式神经形状函数学习策略，该策略鼓励我们的SDF场在水平集附近尽可能线性，从而使训练对监督和正则化信号发出的噪声具有鲁棒性。在不使用任何预训练先验的情况下，我们的方法SparseCraft在新的视图合成和标准基准中从稀疏视图重建方面都达到了最先进的性能，同时只需要不到10分钟的训练时间。 et.al.|[2407.14257](http://arxiv.org/abs/2407.14257)|null|
|**2024-07-19**|**Mono-ViFI: A Unified Learning Framework for Self-supervised Single- and Multi-frame Monocular Depth Estimation**|自监督单目深度估计引起了人们的极大兴趣，因为它可以将训练从对深度注释的依赖中解放出来。在单目视频训练的情况下，最近的方法只在现有的摄像机视图之间进行视图合成，导致引导不足。为了解决这个问题，我们试图通过基于流的视频帧插值（VFI）来合成更多的虚拟相机视图，称为时间增强。对于多帧推理，为了避开基于显式几何的方法（如ManyDepth）遇到的动态对象问题，我们回到了特征融合范式，并设计了一个VFI辅助的多帧融合模块，使用基于流的VFI模型获得的运动和遮挡信息来对齐和聚合多帧特征。最后，我们构建了一个统一的自监督学习框架，名为Mono ViFI，以双向连接单帧和多帧深度。在这个框架中，通过图像仿射变换进行空间数据增强以实现数据多样性，同时进行正则化的三重深度一致性损失。单帧和多帧模型可以共享权重，使我们的框架紧凑且内存高效。大量实验表明，我们的方法可以为当前的先进架构带来重大改进。源代码可在https://github.com/LiuJF1226/Mono-ViFI. et.al.|[2407.14126](http://arxiv.org/abs/2407.14126)|**[link](https://github.com/liujf1226/mono-vifi)**|
|**2024-07-18**|**Shape of Motion: 4D Reconstruction from a Single Video**|由于单眼动态重建任务的高度不适定性，它是一个具有挑战性和长期存在的视觉问题。现有的方法存在局限性，因为它们要么依赖于模板，要么仅在准静态场景中有效，要么无法明确地对3D运动进行建模。在这项工作中，我们介绍了一种能够从随意捕获的单眼视频中重建具有显式、全序列长3D运动的通用动态场景的方法。我们通过两个关键的见解来解决这个问题的欠约束性质：首先，我们通过用一组紧凑的SE3运动基表示场景运动来利用3D运动的低维结构。每个点的运动都表示为这些基的线性组合，有助于将场景软分解为多个刚性移动的组。其次，我们利用了一套全面的数据驱动先验，包括单眼深度图和长距离2D轨迹，并设计了一种方法来有效地整合这些嘈杂的监控信号，从而得到动态场景的全局一致表示。实验表明，我们的方法在长距离3D/2D运动估计和动态场景上的新颖视图合成方面都取得了最先进的性能。项目页面：https://shape-of-motion.github.io/ et.al.|[2407.13764](http://arxiv.org/abs/2407.13764)|null|
|**2024-07-18**|**Streetscapes: Large-scale Consistent Street View Generation Using Autoregressive Video Diffusion**|我们提出了一种通过动态合成的城市尺度场景生成街景长序列视图的方法。我们这一代人受到语言输入（如城市名称、天气）以及承载所需轨迹的底层地图/布局的制约。与最近的视频生成或3D视图合成模型相比，我们的方法可以扩展到更远的摄像机轨迹，跨越几个街区，同时保持视觉质量和一致性。为了实现这一目标，我们基于最近在视频扩散方面的工作，在一个可以轻松扩展到长序列的自回归框架内使用。特别是，我们引入了一种新的时间插补方法，可以防止我们的自回归方法偏离现实城市图像的分布。我们使用来自谷歌街景的令人信服的数据源来训练我们的街景系统，这些数据源包括图像，以及上下文地图数据，这些数据允许用户根据任何所需的城市布局生成城市景观，并具有可控的摄像器姿态。请在我们的项目页面上查看更多结果https://boyangdeng.com/streetscapes. et.al.|[2407.13759](http://arxiv.org/abs/2407.13759)|null|

<p align=right>(<a href=#updated-on-20240725>back to top</a>)</p>

## 3D Reconstruction

|Publish Date|Title|Abstract|PDF|Code|
|---|---|---|---|---|
|**2024-07-21**|**A Novel Method to Improve Quality Surface Coverage in Multi-View Capture**|相机的景深是需要在短距离内拍摄图像或使用大焦距的应用的限制因素，如全身摄影、考古和其他近景摄影测量应用。此外，在多视图捕获中，当目标大于相机的视场时，优化捕获的表面覆盖质量的有效方法仍然是一个挑战。给定目标对象的3D网格和相机姿态，我们提出了一种新的方法来为每个相机推导焦距，以优化覆盖表面区域的质量。我们首先设计了一个期望最小化（EM）算法，将网格上的点唯一地分配给相机，然后在给定相关点集的情况下求解每个相机的焦距。我们通过提出一种 $k$-view算法来进一步提高质量表面覆盖率，该算法通过同时考虑多个视图来解决点分配和焦距问题。我们在各种全身摄影模拟下证明了所提出方法的有效性。EM和$k$-view算法分别将基线单视图方法的相对成本提高了至少24$%和28$%，相当于将聚焦表面积增加了大约1550$cm$^2$和1780$cm$^ 2$ 。我们认为，这些算法可用于许多需要摄影测量细节但受景深限制的视觉应用。 et.al.|[2407.15883](http://arxiv.org/abs/2407.15883)|null|
|**2024-07-22**|**Enhancement of 3D Gaussian Splatting using Raw Mesh for Photorealistic Recreation of Architectures**|建筑场景的真实感重建和渲染在电影、游戏和交通等行业有着广泛的应用。它在城市规划、建筑设计和城市推广方面也发挥着重要作用，特别是在保护历史文化遗产方面。由于其优于NeRF的性能，3D高斯散斑已成为3D重建的主流技术。它唯一的输入是一组图像，但它在很大程度上依赖于SfM过程计算的几何参数。与此同时，现有大量的原始3D模型可以为某些建筑物的结构感知提供信息，但无法应用。在这篇论文中，我们提出了一种直接的方法，利用这些原始的3D模型来引导3D高斯人捕捉建筑物的基本形状，并在非系统地捕捉照片时提高纹理和细节的视觉质量。这一探索为提高3D重建技术在建筑设计领域的有效性开辟了新的可能性。 et.al.|[2407.15435](http://arxiv.org/abs/2407.15435)|null|
|**2024-07-21**|**3D Reconstruction of the Human Colon from Capsule Endoscope Video**|随着受胃肠系统疾病影响的人数不断增加，对预防性筛查的更高要求是不可避免的。这将大大增加胃肠病学家的工作量。为了帮助减少工作量，计算机视觉工具可能会有所帮助。在这篇论文中，我们研究了使用无线胶囊内窥镜视频中的图像序列构建人体结肠整个切片的3D模型的可能性，为胃肠病学家提供了增强的观看体验。由于胶囊内窥镜图像包含失真和伪影，这对许多3D重建算法来说是不理想的，因此这个问题具有挑战性。然而，最近基于虚拟图形的人体胃肠系统模型的发展，可以启用或禁用失真和伪影，从而可以“剖析”这个问题。图形模型还提供了一个地面真实值，可以计算3D重建方法引入的几何失真。在这篇论文中，大多数失真和伪影被排除在外，以确定通过现有方法重建人体胃肠系统的整个部分是否可行。我们证明了使用同步定位和映射可以进行3D重建。此外，为了从密度变化很大的点云重建胃肠壁表面，泊松表面重建是一个不错的选择。研究结果很有希望，鼓励对这个问题进行进一步的研究。 et.al.|[2407.15228](http://arxiv.org/abs/2407.15228)|null|
|**2024-07-21**|**HoloDreamer: Holistic 3D Panoramic World Generation from Text Descriptions**|3D场景生成在各个领域都有很高的需求，包括虚拟现实、游戏和电影行业。由于文本到图像扩散模型具有强大的生成能力，可以提供可靠的先验信息，因此仅使用文本提示创建3D场景变得可行，从而显著推进了文本驱动的3D场景生成研究。为了从2D扩散模型中获得多视图监控，主流方法通常采用扩散模型生成初始局部图像，然后使用扩散模型迭代地绘制局部图像以逐渐生成场景。然而，这些基于外画的方法容易产生全局不一致的场景生成结果，没有高度的完整性，限制了它们更广泛的应用。为了解决这些问题，我们引入了HoloDreamer，这是一个框架，它首先生成高清全景作为完整3D场景的整体初始化，然后利用3D高斯散斑（3D-GS）快速重建3D场景，从而促进创建视图一致和完全封闭的3D场景。具体来说，我们提出了风格化的等矩形全景生成，这是一种结合了多个扩散模型的管道，可以从复杂的文本提示中生成风格化和详细的等矩形的全景。随后，引入了增强两阶段全景重建，对3D-GS进行两阶段优化，以输入缺失区域并增强场景的完整性。综合实验表明，在生成全封闭场景时，我们的方法在整体视觉一致性和和谐性以及重建质量和渲染鲁棒性方面优于先前的工作。 et.al.|[2407.15187](http://arxiv.org/abs/2407.15187)|null|
|**2024-07-21**|**VoxDepth: Rectification of Depth Images on Edge Devices**|自动飞行无人机和工业机器人等自主移动机器人在很大程度上依赖于深度图像来执行3D重建和视觉SLAM等任务。然而，这些深度图像中不准确的存在会极大地阻碍这些应用的有效性，导致次优结果。商用相机产生的深度图像经常出现噪声，表现为闪烁的像素和错误的补丁。基于ML的校正这些图像的方法不适合计算资源非常有限的边缘设备。非机器学习方法要快得多，但精度有限，特别是对于纠正因遮挡和相机移动而导致的错误。我们提出了一种名为VoxDepth的方案，该方案快速、准确，在边缘设备上运行良好。它依赖于一系列新技术：3D点云构建和融合，并使用它来创建一个可以修复错误深度图像的模板。VoxDepth在合成数据集和真实数据集上都显示出卓越的结果。与现实世界深度数据集上的最先进方法相比，我们的质量提高了31%，同时保持了27 FPS（每秒帧数）的竞争帧率。 et.al.|[2407.15067](http://arxiv.org/abs/2407.15067)|null|
|**2024-07-19**|**SparseCraft: Few-Shot Neural Reconstruction through Stereopsis Guided Geometric Linearization**|我们提出了一种从少数彩色图像中恢复3D形状和视图相关外观的新方法，实现了高效的3D重建和新颖的视图合成。我们的方法以符号距离函数（SDF）和辐射场的形式学习隐式神经表示。该模型通过支持光线行进的体积渲染逐步训练，并使用无需学习的多视图立体（MVS）线索进行正则化。我们贡献的关键是一种新的隐式神经形状函数学习策略，该策略鼓励我们的SDF场在水平集附近尽可能线性，从而使训练对监督和正则化信号发出的噪声具有鲁棒性。在不使用任何预训练先验的情况下，我们的方法SparseCraft在新的视图合成和标准基准中从稀疏视图重建方面都达到了最先进的性能，同时只需要不到10分钟的训练时间。 et.al.|[2407.14257](http://arxiv.org/abs/2407.14257)|null|
|**2024-07-19**|**I Know About "Up"! Enhancing Spatial Reasoning in Visual Language Models Through 3D Reconstruction**|视觉语言模型（VLMs）对于各种任务，特别是视觉推理任务至关重要，因为它们具有强大的多模态信息集成、视觉推理能力和上下文感知能力。然而，现有的视觉空间推理能力往往不足，即使在区分左右等基本任务上也很困难。为了解决这个问题，我们提出了我们的模型，旨在增强VLMS的视觉空间推理能力。ZeroVLM采用Zero1-to-3，这是一种3D重建模型，用于获得输入图像的不同视图，并结合了提示机制，以进一步改善视觉空间推理。在四个视觉空间推理数据集上的实验结果表明，我们的{}实现了高达19.48%的准确率提高，这表明了ZeroVLM的3D重建和提示机制的有效性。 et.al.|[2407.14133](http://arxiv.org/abs/2407.14133)|null|
|**2024-07-19**|**FAVis: Visual Analytics of Factor Analysis for Psychological Research**|心理学研究通常涉及通过对问卷收集的数据进行因子分析来理解心理结构，问卷可能包括数百个问题。如果没有用于解释因子模型的交互系统，研究人员经常会受到主观性的影响，这可能会导致误解或忽视关键信息。本文介绍了FAVis，这是一种新型的交互式可视化工具，旨在帮助研究人员解释和评估因子分析结果。FAVis通过支持多种视图来可视化因素载荷和相关性，使用户能够从不同角度分析信息，从而增强了对变量和因素之间关系的理解。FAVis的主要功能是使用户能够为因子负载设置最佳阈值，以平衡清晰度和信息保留。FAVis还允许用户为变量分配标签，通过将它们与相关的心理结构联系起来，增强对因素的理解。我们的用户研究证明了FAVis在各种任务中的实用性。 et.al.|[2407.14072](http://arxiv.org/abs/2407.14072)|null|
|**2024-07-19**|**DirectL: Efficient Radiance Fields Rendering for 3D Light Field Displays**|尽管经过几十年的发展，自动立体显示器尚未得到广泛应用，主要是因为非专业人士在3D内容创作方面面临着艰巨的挑战。辐射场作为一种创新的3D表示的出现，显著地彻底改变了3D重建和生成的领域。这项技术大大简化了普通用户的3D内容创建，扩大了光场显示器（LFD）的适用范围。然而，这两个领域的结合在很大程度上仍未得到探索。为基于视差的光场显示器创建最佳内容的标准范式要求渲染至少45个略微偏移的视图，最好是每帧高分辨率，这是实时渲染的一个重大障碍。我们介绍了DirectL，这是一种用于3D显示器上辐射场的新型渲染范式。我们深入分析了空间光线到屏幕子像素的交织映射，精确地确定了进入人眼的光线，并提出了子像素的重新利用，以显著减少渲染所需的像素数。针对两个主要的辐射场——神经辐射场（NeRFs）和3D高斯散斑（3DGS），我们提出了相应的优化渲染管道，直接渲染光场图像，而不是多视图图像。在各种显示器和用户研究中进行的广泛实验表明，与标准范式相比，DirectL在不牺牲视觉质量的情况下将渲染速度提高了40倍。仅对其渲染过程进行修改，即可无缝集成到后续的辐射场任务中。最后，我们将DirectL集成到各种应用中，展示了令人惊叹的视觉体验以及LFD和Radiance Fields之间的协同作用，这为商业化应用带来了巨大的潜力。\href{direct-l.github.io}{\textbf{项目主页} et.al.|[2407.14053](http://arxiv.org/abs/2407.14053)|null|
|**2024-07-18**|**MaRINeR: Enhancing Novel Views by Matching Rendered Images with Nearby References**|从3D重建中渲染逼真的图像是许多计算机视觉和机器人管道的重要任务，特别是对于混合现实应用以及在模拟环境中训练自主代理。然而，新颖视图的质量在很大程度上取决于源重建，由于噪声或缺少几何和外观，源重建往往是不完美的。受最近基于参考的超分辨率网络成功的启发，我们提出了MaRINeR，这是一种利用附近映射图像的信息来改善目标视点渲染的细化方法。我们首先基于深度特征在目标视点的场景几何的原始渲染图像和附近的参考之间建立匹配，然后进行分层细节传递。我们从显式和隐式场景表示的定量指标和定性示例中展示了改进的渲染。我们进一步将我们的方法应用于伪地面真实性验证、合成数据增强和细节恢复等下游任务，用于简化3D重建的渲染。 et.al.|[2407.13745](http://arxiv.org/abs/2407.13745)|null|

<p align=right>(<a href=#updated-on-20240725>back to top</a>)</p>

## Diffusion

|Publish Date|Title|Abstract|PDF|Code|
|---|---|---|---|---|
|**2024-07-24**|**SV4D: Dynamic 3D Content Generation with Multi-Frame and Multi-View Consistency**|我们提出了稳定视频4D（SV4D），这是一种用于多帧和多视图一致动态3D内容生成的潜在视频扩散模型。与之前依赖于单独训练的生成模型进行视频生成和新颖视图合成的方法不同，我们设计了一个统一的扩散模型来生成动态3D对象的新颖视图视频。具体来说，给定单眼参考视频，SV4D为每个视频帧生成时间上一致的新视图。然后，我们使用生成的新颖视图视频来有效地优化隐式4D表示（动态NeRF），而不需要大多数先前工作中使用的繁琐的基于SDS的优化。为了训练我们的统一新颖视图视频生成模型，我们从现有的Objaverse数据集中策划了一个动态3D对象数据集。多个数据集和用户研究的广泛实验结果表明，与先前的工作相比，SV4D在新视图视频合成和4D生成方面具有最先进的性能。 et.al.|[2407.17470](http://arxiv.org/abs/2407.17470)|null|
|**2024-07-24**|**Gender disparities in the dissemination and acquisition of scientific knowledge**|最近的研究挑战了学术界普遍认为的性别不平等只需增加女性人数就会消失的观点。更复杂的原因可能在起作用，体现在科学合作的网络结构中。在这里，我们旨在了解男女学者在科学知识传播方面的结构性不平等。我们使用美国物理学会（APS）的大规模学术出版物数据集，构建了一个从1970年到2020年的时变合作网络。我们将知识传播建模为一个传染过程，在这个过程中，科学家通过合作者传播知识而获得信息。我们根据女性与男性相比如何获取和传播知识来量化该系统的公平性。我们的研究结果表明，女性的知识获取和传播速度比预期的要慢。我们发现，女性劣势的主要决定因素是合作者累积数量的差距，这突显了时间如何造成结构性劣势，导致女性在物理学中被边缘化。我们的工作揭示了科学合作的动态如何影响知识传播中的性别差异，并呼吁更深入地了解如何干预以提高科学界的公平性和多样性。 et.al.|[2407.17441](http://arxiv.org/abs/2407.17441)|null|
|**2024-07-24**|**CDDIP: Constrained Diffusion-Driven Deep Image Prior for Seismic Image Reconstruction**|地震数据经常显示出缺失的痕迹，严重影响了后续的地震处理和解释。基于深度学习的方法在通过监督和无监督方法重建不规则缺失的地震数据方面取得了重大进展。尽管如此，仍然存在重大挑战，例如推理过程中的泛化能力和计算时间成本。我们的工作介绍了一种重建方法，该方法使用预训练的生成扩散模型进行图像合成，并在重建地震图像中缺失的痕迹时结合深度图像先验（DIP）来保持数据一致性。所提出的方法对具有不同结构复杂度的现场和合成地震图像表现出很强的鲁棒性和高重建能力，即使在测试图像不在训练域的情况下也是如此。这表明我们的方法可以处理不同勘探目标的高地质变异性。此外，与使用扩散模型的其他最先进的地震重建方法相比，我们的方法将神经函数评估的数量减少了4倍。 et.al.|[2407.17402](http://arxiv.org/abs/2407.17402)|null|
|**2024-07-24**|**Kinetic theory applied to pressure-controlled shear flows of frictionless spheres between rigid, bumpy planes**|我们通过离散元模拟数值研究了在没有重力和固定法向载荷的情况下，在两个平行、颠簸的平面之间剪切的相同、无摩擦球体的稳定流动。我们测量了固体体积分数、平均速度、搅拌强度和应力的空间分布，并证实了之前关于状态方程和颗粒气体动力学理论预测的粘度的有效性的结果。首先，我们还直接测量了波动动能的扩散率和碰撞耗散率的空间分布，并成功地检验了动力学理论的相关本构关系。然后，我们用适当的边界条件对控制流动的微分方程组进行表述和数值积分，并在水动力场轮廓、剪应力与压力之比以及颠簸平面之间的间隙对碰撞恢复系数、施加的载荷和平面颠簸的依赖性方面，与离散模拟的结果在定性和定量上表现出显著的一致性。最后，我们提出了一个标准，根据边值问题的解来预测施加载荷的临界值，超过该临界值可能会发生结晶。这显著地再现了我们在离散模拟中观察到的结果。 et.al.|[2407.17397](http://arxiv.org/abs/2407.17397)|null|
|**2024-07-24**|**How optimal control of polar sea-ice depends on its tipping points**|由于气候变暖加剧，地球系统的几个组成部分面临着发生快速和不可逆转的质变或“倾倒”的高风险。潜在的倾倒因素包括北极海冰、大西洋经向翻转环流和热带珊瑚礁。在这种紧迫的问题中，有必要研究使用反馈控制来阻止甚至扭转翻倒阈值的可行性。本文研究了地球气候理想化扩散能量平衡模型（EBM）的控制；由于强烈的共反照率反馈，该模型有两个临界点。其中一个临界点是“小冰盖”的不稳定性，这是在温室气体（GHG）排放增加的情况下迅速过渡到无冰气候状态的原因。我们为不同气候强迫情景下的EBM开发了一种最优控制策略，目标是扭转海冰损失，同时最大限度地降低成本。我们发现，这种系统可以实现有效的控制，但与达到临界点之前的状态相比，在刚刚倾斜的初始状态下，扭转海冰损失的成本几乎翻了两番。我们还表明，热惯性可能会延迟倾翻，导致临界温室气体强迫阈值超调。这可能会提供一个短暂的干预窗口（过冲窗口），在此期间，逆转海冰损失所需的控制仅随干预时间呈线性变化。虽然具有较大系统惯性的系统可能具有较长的超调窗口，但一旦干预延迟超过此窗口，这种增加的回旋余地就会使必要的控制急剧上升。此外，我们发现恢复海冰的必要控制局限于极地地区。 et.al.|[2407.17357](http://arxiv.org/abs/2407.17357)|null|
|**2024-07-24**|**Optimal Control of a Reaction-Diffusion Epidemic Model with Noncompliance**|本文考虑了具有人类行为效应的基于反应扩散的SIR流行病模型的最优分布式控制问题。我们开发了一个模型，其中实施了非药物干预方法，但部分人群不遵守这些方法，这种不遵守会影响疾病的传播。根据社会传染理论，我们的模型允许不遵守行为的传播与疾病的传播平行。控制感兴趣的数量是顺从人群中感染率的降低、不顺从的传播率，以及不顺从者在收到更多或更好的有关潜在疾病的信息后变得顺从的速度。我们证明了固定控制的全局时间解的存在性，并研究了由此产生的控制对状态图的正则性。然后，在一类相当一般的目标函数的抽象框架中建立最优控制的存在性。通过基于拉格朗日的平稳性系统获得了必要的一阶最优性条件。最后，我们讨论了如何最小化感染和不依从人群的规模，并给出了各种参数值的模拟，以证明模型的行为。 et.al.|[2407.17298](http://arxiv.org/abs/2407.17298)|null|
|**2024-07-24**|**Hybrid-PFC: coupling the phase-field crystal model and its amplitude-equation formulation**|相场晶体（PFC）模型描述了通过周期性微观密度场在扩散时间尺度上的晶体结构。有人提出模拟晶体生长中的弹性，并编码了与晶体力学性能相关的大部分现象学，如位错成核和运动、晶界以及弹性或界面能量各向异性。为了克服小系统的局限性，设计了一种粗粒度公式，重点关注微观密度场缓慢变化的复振幅。这种振幅PFC（APFC）模型很好地描述了弹性和位错，同时近似了微观特征，在描述大角度晶界方面受到限制。我们在这里提出了混合多尺度PFC-APFC框架的开创性概念，该框架结合了块状晶粒中APFC模型的粗粒度描述，同时利用了位错、晶界和界面或表面的PFC分辨率。这是通过基于傅里叶谱方法的高级离散化将两个模型耦合起来，并允许局部解决方案更新来实现的。这种离散化也推广了PFC模型边界条件的描述。我们通过二维基准模拟展示了框架的功能。我们还表明，所提出的公式可以克服APFC模型在描述大角度晶界方面的局限性。 et.al.|[2407.17283](http://arxiv.org/abs/2407.17283)|null|
|**2024-07-24**|**Stochastic Aggregation Diffusion-Equation : Analysis via Dirichlet Forms**|本文研究了由单调径向核表示的具有奇异漂移的随机聚集扩散方程。我们证明了作为方程弱解的扩散过程的存在性和唯一性。这个过程可以描述为源自离域点的扭曲布朗运动。利用Dirichlet形式理论，我们证明了状态空间中拟处处点的弱解的存在性。然而，从极集合外的点开始的解的唯一性并不能得到保证，明确表征这些集合构成了一个重大挑战。为了解决这个问题，我们采用了Albeverio等人（2003）引入的H_2条件。这个条件提供了对Dirichlet形式框架内唯一性问题的更深入的理解。因此，H_2条件在加强弱解分析、确保更详细地理解问题方面至关重要。还提供了与某些核相关的广义薛定谔算子的显式表达式。 et.al.|[2407.17239](http://arxiv.org/abs/2407.17239)|null|
|**2024-07-24**|**LPGen: Enhancing High-Fidelity Landscape Painting Generation through Diffusion Model**|生成山水画拓展了艺术创造力和想象力的可能性。传统的山水画方法涉及在宣纸上使用墨水或彩色墨水，这需要大量的时间和精力。这些方法容易出现错误和不一致，并且缺乏对线条和颜色的精确控制。本文介绍了一种高保真、可控的风景画生成模型LPGen，引入了一种将图像提示集成到扩散模型中的新型多模态框架。我们通过计算目标景观图像中的精明边缘来提取其边缘和轮廓。这些，以及自然语言文本提示和绘图风格参考，作为条件被输入潜在扩散模型。我们实施了一种解耦的交叉注意力策略，以确保图像和文本提示之间的兼容性，从而促进多模态图像生成。解码器生成最终图像。定量和定性分析表明，我们的方法在风景画生成方面优于现有的方法，并超越了当前的最新技术。LPGen网络有效地控制了风景画的构图和颜色，生成了更准确的图像，并支持基于深度学习的风景画生成的进一步研究。 et.al.|[2407.17229](http://arxiv.org/abs/2407.17229)|null|
|**2024-07-24**|**Sublinear Regret for An Actor-Critic Algorithm in Continuous-Time Linear-Quadratic Reinforcement Learning**|我们研究了一类连续时间线性二次型（LQ）扩散控制问题的强化学习（RL），其中状态过程的波动性取决于状态和控制变量。我们应用了一种无模型的方法，既不依赖于模型参数的知识，也不依赖于它们的估计，并设计了一种行动者批评算法来直接学习最优策略参数。我们的主要贡献包括引入了一种新的探索计划，并对提出的算法进行了遗憾分析。我们提供了策略参数到最优参数的收敛速度，并证明了该算法在对数因子上达到了 $O（N^{\frac{3}{4}}）$ 的遗憾界。我们进行了一项仿真研究，以验证理论结果，并证明所提出算法的有效性和可靠性。我们还对我们的方法与最近基于模型的随机LQ RL研究的方法进行了数值比较，这些研究适用于状态和控制相关的波动率设置，证明了前者在遗憾界限方面的更好性能。 et.al.|[2407.17226](http://arxiv.org/abs/2407.17226)|null|

<p align=right>(<a href=#updated-on-20240725>back to top</a>)</p>

## NeRF

|Publish Date|Title|Abstract|PDF|Code|
|---|---|---|---|---|
|**2024-07-24**|**Neural field equations with time-periodic external inputs and some applications to visual processing**|这项工作的目的是为研究视觉处理任务中的闪烁输入提供一个数学框架。当与几何图案结合时，这些输入会影响并诱发有趣的心理物理现象，如麦凯效应和比洛克-邹效应，在这些效应中，受试者感知到通常由闪烁频率调制的特定余像。由于输入的对称破缺结构，经典分叉理论和多尺度分析技术在我们的背景下不是很有效。因此，我们采用了一种基于Amari型神经场控制理论的输入-输出框架的方法。这使我们能够证明，当受到周期性输入的驱动时，动态会收敛到周期性状态。此外，我们研究了在哪些假设下，这些非线性动力学可以有效地线性化，在这种情况下，我们提出了短程兴奋性和远程抑制性神经元相互作用的积分核的精确近似值。最后，对于集中在具有闪烁背景的视野中心的输入，我们直接将余像中出现的虚幻轮廓的宽度与闪烁频率和抑制强度联系起来。 et.al.|[2407.17294](http://arxiv.org/abs/2407.17294)|null|
|**2024-07-23**|**Fluorescence Diffraction Tomography using Explicit Neural Fields**|从荧光图像中求解3D折射率（RI）可以提供有关生物样本的荧光和相位信息。然而，在大体积、高分辨率和反射模式下准确检索部分相干光的相位以重建无标签相位物体的未知RI仍然具有挑战性。为了应对这一挑战，我们开发了具有显式神经场的荧光衍射断层扫描（FDT），可以从散焦荧光散斑图像重建3D RI。使用FDT成功重建3D RI依赖于四个关键组件：粗到细建模、自校准、差分多层渲染模型和部分相干掩模。具体而言，显式表示与粗到细建模有效地集成在一起，以实现高速、高分辨率的重建。此外，我们将多层方程推进到微分多层渲染模型，这使得系统的外部和内部参数能够进行自校准。自校准有助于高精度的正向图像预测和RI重建。部分相干掩模是数字掩模，用于准确有效地解决相干光模型和部分相干光数据之间的差异。FDT成功地从荧光图像中重建了24个z $层上1024$×1024像素的530$×530$×300$μm^3$ 体积的3D培养无标记3D MuSCs管的RI，证明了在体外对体积庞大和异质的生物样本进行高保真3D RI重建。 et.al.|[2407.16657](http://arxiv.org/abs/2407.16657)|null|
|**2024-07-22**|**Iterative approach to reconstructing neural disparity fields from light-field data**|本研究提出了一种神经视差场（NDF），该场基于神经场建立了场景视差的隐式连续表示，并采用迭代方法解决了从光场数据重建NDF的逆问题。NDF能够无缝和精确地表征三维场景中的视差变化，并可以以任何任意分辨率对视差进行离散化，克服了传统视差图容易出现采样误差和插值不准确的局限性。所提出的NDF网络架构利用哈希编码结合多层感知器来捕获纹理级别的详细差异，从而增强其表示复杂场景几何信息的能力。通过利用光场数据中固有的空间角度一致性，开发了一种可微分正向模型，用于从光场数据生成中心视图图像。基于正向模型，建立了一种使用可微传播算子的NDF重建逆问题的优化方案。此外，在优化方案中，采用迭代求解方法重建NDF，该方法不需要训练数据集，适用于各种采集方法捕获的光场数据。实验结果表明，使用所提出的方法可以从光场数据中重建高质量的NDF。NDF可以有效地恢复高分辨率视差，证明了其隐式、连续表示场景视差的能力。 et.al.|[2407.15380](http://arxiv.org/abs/2407.15380)|null|
|**2024-07-19**|**Contextual modulation of language comprehension in a dynamic neural model of lexical meaning**|我们提出并计算实现了一个词汇意义的动态神经模型，并对其行为预测进行了实验测试。我们使用英语词汇“have”作为测试用例来演示模型的架构和行为，重点关注其多义词的使用。在该模型中，“have”映射到由两个连续的概念维度（连通性和控制不对称性）定义的语义空间，这两个维度之前被提出用于参数化语言的概念系统。映射被建模为表示词条的神经节点和表示概念维度的神经场之间的耦合。虽然词汇知识被建模为稳定的耦合模式，但实时词汇意义检索被建模为神经激活模式在对应于语义解释或阅读的亚稳态之间的运动。模型模拟捕捉到了两个先前报道的实证观察结果：（1）词汇语义解释的语境调制，以及（2）这种调制幅度的个体差异。模拟还产生了一种新的预测，即句子阅读时间和可接受性之间的试验关系应该根据上下文进行调节。结合自定进度阅读和可接受性判断的实验复制了之前的结果，并证实了新的模型预测。总之，研究结果支持了一种关于词汇多义的新观点：一个词的许多相关含义是亚稳态的神经激活状态，这是由控制连续语义维度解释的神经群体的非线性动力学引起的。 et.al.|[2407.14701](http://arxiv.org/abs/2407.14701)|null|
|**2024-07-18**|**MeshFeat: Multi-Resolution Features for Neural Fields on Meshes**|参数特征网格编码作为神经场的编码方法受到了广泛关注，因为它们允许更小的MLP，这大大缩短了模型的推理时间。在这项工作中，我们提出了MeshFeat，这是一种针对网格量身定制的参数特征编码，为此我们采用了欧几里德空间的多分辨率特征网格的思想。我们从给定顶点拓扑提供的结构开始，使用网格简化算法直接在网格上构建多分辨率特征表示。该方法允许在网格上的神经场中使用小MLP，与之前的表示相比，我们显示出显著的加速，同时保持了纹理重建和BRDF表示的可比重建质量。鉴于其与顶点的内在耦合，该方法特别适用于变形网格上的表示，使其非常适合对象动画。 et.al.|[2407.13592](http://arxiv.org/abs/2407.13592)|null|
|**2024-07-16**|**Adaptive Environment-Aware Robotic Arm Reaching Based on a Bio-Inspired Neurodynamical Computational Framework**|仿生机器人系统具有自适应学习、可扩展控制和高效信息处理的能力。为这些系统提供实时决策对于应对环境的动态变化至关重要。我们专注于在开放区域使用带有鸟瞰摄像头的机器人六自由度操纵器进行动态目标跟踪，并部署神经动力学计算框架（NeuCF）进行视觉反馈。NeuCF是最近开发的一种基于动态神经场（DNF）和随机最优控制（SOC）理论的仿生目标跟踪模型。它已经过训练，可以在平面上对局部视觉信标进行到达动作，并且可以根据环境的变化（例如，出现了新的目标，或者删除了现有的目标）实时重新定位或生成停止信号。我们在各种目标达成场景下评估了我们的系统。在所有实验中，与基线三次多项式轨迹生成器相比，NeuCF具有较高的末端执行器位置精度，生成了平滑的轨迹，并提供了更短的路径长度。总之，开发的系统提供了一种强大的、动态感知的机器人操纵方法，可以提供实时决策。 et.al.|[2407.11377](http://arxiv.org/abs/2407.11377)|null|
|**2024-07-12**|**Physics-Informed Learning of Characteristic Trajectories for Smoke Reconstruction**|我们通过稀疏视图RGB视频深入研究了烟雾和障碍物的物理信息神经重建，解决了复杂动力学观测有限带来的挑战。现有的基于物理信息的神经网络通常强调短期物理约束，对长期守恒的适当保护探索较少。我们引入了神经特征轨迹场，这是一种利用欧拉神经场隐式建模拉格朗日流体轨迹的新表示方法。这种无拓扑、可自动微分的表示便于在任意帧之间进行高效的流图计算，以及通过自动微分进行高效的速度提取。因此，它实现了涵盖长期保护和短期物理先验的端到端监督。在此基础上，我们提出了基于物理的轨迹学习和集成到基于NeRF的场景重建中。我们通过自我监督的场景分解和无缝集成的边界约束来实现高级障碍物处理。我们的结果展示了克服遮挡不确定性、密度-颜色模糊性和静态-动态纠缠等挑战的能力。代码和示例测试位于\url{https://github.com/19reborn/PICT_smoke}. et.al.|[2407.09679](http://arxiv.org/abs/2407.09679)|null|
|**2024-07-10**|**Neural Localizer Fields for Continuous 3D Human Pose and Shape Estimation**|随着可用训练数据的爆炸性增长，单图像3D人体建模领先于向以数据为中心的范式过渡。成功利用数据规模的关键是设计灵活的模型，这些模型可以从不同研究人员或供应商生产的各种异构数据源进行监督。为此，我们提出了一种简单而强大的范式，用于无缝统一不同的人体姿势和形状相关的任务和数据集。我们的公式侧重于在训练和测试时查询人体体积的任意点并在3D中获得其估计位置的能力。我们通过学习身体点定位器函数的连续神经场来实现这一点，每个函数都是基于不同参数化的3D热图卷积点定位器（检测器）。为了生成参数输出，我们提出了一种高效的后处理步骤，用于将SMPL族身体模型拟合到非参数关节和顶点预测中。通过这种方法，我们可以自然地利用不同注释的数据源，包括网格、2D/3D骨架和密集姿势，而无需在它们之间进行转换，从而训练出大规模的3D人体网格和骨架估计模型，这些模型在3DPW、EMDB和SSP-3D等几个公共基准上的表现远远优于最先进的水平。 et.al.|[2407.07532](http://arxiv.org/abs/2407.07532)|null|
|**2024-07-03**|**Cerebral cortex inspired representation of neural field network**|进化及其智能元素在探索中带来了刺激和挑战。然而，物种如何拥有记忆、检索记忆并保持连续性是根本问题。大多数现象只能由研究人员假设，通过实验验证它们是一个很大的挑战。将大脑视为理想的智能机器并对其进行建模，为计算算法开辟了新的维度。本文提出了一个假设，即类似于大脑皮层的记忆创造。大脑皮层的区域隐含着特定功能的特异性，构成了一维的矢量形式的神经场。整个皮层的神经场相互连接形成了一个网络。这些网络与生存本能、情绪和奖励相关联，构成了对暴露环境的记忆，或者说学习。具有多维控制点的图形工具NURBS被隐式地用于将这些网络表示为一组三次方程。通过数据学习是智能系统的主要模块，本文试图将数据转换为低维模式，而不是实时智能系统的现有绝对形式。 et.al.|[2407.04741](http://arxiv.org/abs/2407.04741)|null|
|**2024-07-01**|**Fast and Efficient: Mask Neural Fields for 3D Scene Segmentation**|理解3D场景是计算机视觉研究中的一个关键挑战，其应用跨越多个领域。最近在将2D视觉语言基础模型提取到神经领域（如NeRF和3DGS）方面取得的进展，使3D场景能够从2D多视图图像中进行开放式词汇分割，而不需要精确的3D注释。然而，虽然有效，但高维CLIP特征的每像素蒸馏会引入模糊性，并需要复杂的正则化策略，从而在训练过程中增加效率。本文介绍了MaskField，它能够在弱监督下利用神经场实现快速高效的3D开放式分词。与以前的方法不同，MaskField提取掩模而不是密集的高维CLIP特征。MaskFields使用神经场作为二进制掩模生成器，并使用SAM生成的掩模对其进行监督，并通过粗略的CLIP特征进行分类。MaskField通过在训练过程中自然引入SAM分割的对象形状而无需额外的正则化来克服模糊的对象边界。通过在训练过程中避免直接处理高维CLIP特征，MaskField与3DGS等显式场景表示特别兼容。我们广泛的实验表明，MaskField不仅超越了现有的最先进的方法，而且实现了非常快的收敛速度，仅需5分钟的训练就超越了以前的方法。我们希望MaskField能够激发对如何训练神经场以从2D模型中理解3D场景的进一步探索。 et.al.|[2407.01220](http://arxiv.org/abs/2407.01220)|null|

<p align=right>(<a href=#updated-on-20240725>back to top</a>)</p>

[contributors-shield]: https://img.shields.io/github/contributors/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[contributors-url]: https://github.com/Vincentqyw/cv-arxiv-daily/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[forks-url]: https://github.com/Vincentqyw/cv-arxiv-daily/network/members
[stars-shield]: https://img.shields.io/github/stars/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[stars-url]: https://github.com/Vincentqyw/cv-arxiv-daily/stargazers
[issues-shield]: https://img.shields.io/github/issues/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[issues-url]: https://github.com/Vincentqyw/cv-arxiv-daily/issues

