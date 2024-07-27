[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]

## Updated on 2024.07.27
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
|**2024-07-25**|**Towards the Spectral bias Alleviation by Normalizations in Coordinate Networks**|最近，使用坐标网络表示信号主导了逆问题领域，并广泛应用于各种科学计算任务中。尽管如此，坐标网络中仍存在光谱偏差的问题，限制了学习高频分量的能力。这个问题是由坐标网络的神经切线核（NTK）特征值的病理分布引起的。我们发现，使用经典归一化技术（批归一化和层归一化）可以改善这种病理分布，这些技术通常用于卷积神经网络，但很少用于坐标网络。我们证明，归一化技术大大降低了NTK特征值的最大值和方差，同时略微修改了均值，考虑到最大特征值远大于最大值，这种方差变化导致特征值分布从较低的分布向较高的分布偏移，因此可以减轻谱偏差。此外，我们通过以不同的方式组合这两种技术，提出了两种新的归一化技术。通过将基于归一化的坐标网络应用于各种任务，包括图像压缩、计算机断层扫描重建、形状表示、磁共振成像、新视图合成和多视图立体重建，这些归一化技术的有效性得到了显著改进和最新技术水平的证实。 et.al.|[2407.17834](http://arxiv.org/abs/2407.17834)|null|
|**2024-07-24**|**SV4D: Dynamic 3D Content Generation with Multi-Frame and Multi-View Consistency**|我们提出了稳定视频4D（SV4D），这是一种用于多帧和多视图一致动态3D内容生成的潜在视频扩散模型。与之前依赖于单独训练的生成模型进行视频生成和新颖视图合成的方法不同，我们设计了一个统一的扩散模型来生成动态3D对象的新颖视图视频。具体来说，给定单眼参考视频，SV4D为每个视频帧生成时间上一致的新视图。然后，我们使用生成的新颖视图视频来有效地优化隐式4D表示（动态NeRF），而不需要大多数先前工作中使用的繁琐的基于SDS的优化。为了训练我们的统一新颖视图视频生成模型，我们从现有的Objaverse数据集中策划了一个动态3D对象数据集。多个数据集和用户研究的广泛实验结果表明，与先前的工作相比，SV4D在新视图视频合成和4D生成方面具有最先进的性能。 et.al.|[2407.17470](http://arxiv.org/abs/2407.17470)|null|
|**2024-07-24**|**Pose Estimation from Camera Images for Underwater Inspection**|高精度定位是水下复验任务的关键。惯性导航系统、多普勒速度记录仪和声学定位等传统定位方法面临着重大挑战，对于某些应用来说成本效益不高。在这种情况下，视觉定位是一种经济高效的替代方案，利用检查车辆上已经配备的摄像头从周围场景的图像中估计姿态。其中，基于机器学习的图像姿态估计在水下环境中显示出前景，使用基于先前映射场景训练的模型进行高效的重新定位。我们探索了基于学习的姿态估计器在清水和浑浊水检查任务中的有效性，评估了图像格式、模型架构和训练数据多样性的影响。我们通过采用新颖的视图合成模型来生成增强训练数据，从而显著增强了未探索区域的姿态估计。此外，我们通过扩展卡尔曼滤波器将姿态估计器输出与传感器数据相结合，提高了定位精度，证明了轨迹平滑度和精度的提高。 et.al.|[2407.16961](http://arxiv.org/abs/2407.16961)|null|
|**2024-07-23**|**DHGS: Decoupled Hybrid Gaussian Splatting for Driving Scene**|由于缺乏巧妙的设计和相关元素的几何约束，现有的高斯飞溅方法在驾驶场景中难以实现令人满意的新颖视图合成。本文介绍了一种称为解耦混合高斯散点（DHGS）的新方法，旨在提高驾驶场景新型视图合成的渲染质量。这项工作的新颖之处在于，用于道路和非道路层的解耦和混合像素级混合器，不需要为整个场景提供传统的统一可微渲染逻辑，同时通过提出的深度有序渲染策略保持一致和连续的叠加。除此之外，还训练了一个由符号距离场（SDF）组成的隐式道路表示，以监督具有微妙几何属性的路面。伴随着辅助透射率损失和一致性损失的使用，最终获得了具有不可察觉边界和高保真度的新图像。在Waymo数据集上的大量实验证明，DHGS的性能优于最先进的方法。 et.al.|[2407.16600](http://arxiv.org/abs/2407.16600)|null|
|**2024-07-23**|**HDRSplat: Gaussian Splatting for High Dynamic Range 3D Scene Reconstruction from Raw Images**|最近出现的3D高斯散斑（3DGS）彻底改变了3D场景重建空间，实现了实时高保真的新颖视图合成。然而，除了RawNeRF之外，所有先前的基于3DGS和NeRF的方法都依赖于8位色调映射的低动态范围（LDR）图像进行场景重建。这种方法难以在需要更高动态范围的场景中实现精确的重建。示例包括在夜间或光线不足的室内空间中拍摄的具有低信噪比的场景，以及阴影区域表现出极端对比度的日光场景。我们提出的方法HDRSplat定制3DGS，在近暗环境中直接在14位线性原始图像上训练，保留了场景的完整动态范围和内容。我们的主要贡献有两个方面：首先，我们提出了一种适合线性HDR空间损耗的方法，可以同时从嘈杂的暗区和接近饱和的亮区中有效地提取场景信息，同时处理与视图相关的颜色，而不会增加球谐波的程度。其次，通过仔细的光栅化调整，我们隐含地克服了3DGS对点云初始化的严重依赖和敏感性。这对于在低纹理、高景深和低照度区域进行精确重建至关重要。HDRSplat是迄今为止最快的方法，可以在15分钟/场景内完成14位（HDR）3D场景重建（比之前最先进的RawNeRF快30倍）。它还拥有最快的推理速度，为120fps。我们通过展示各种应用，如合成散焦、密集深度图提取以及曝光、色调映射和视点的捕捉后控制，进一步证明了HDR场景重建的适用性。 et.al.|[2407.16503](http://arxiv.org/abs/2407.16503)|null|
|**2024-07-22**|**BoostMVSNeRFs: Boosting MVS-based NeRFs to Generalizable View Synthesis in Large-scale Scenes**|虽然神经辐射场（NeRFs）表现出了卓越的质量，但其漫长的训练时间仍然是一个限制。可推广和基于MVS的NeRF虽然能够缩短训练时间，但往往会在质量上进行权衡。本文提出了一种称为BoostMVSNeRFs的新方法，以提高基于MVS的NeRF在大规模场景中的渲染质量。我们首先确定了基于MVS的NeRF方法的局限性，例如受限的视口覆盖和由于有限的输入视图引起的伪影。然后，我们通过提出一种在体绘制过程中选择和组合多个成本体积的新方法来解决这些局限性。我们的方法不需要训练，可以以前馈方式适应任何基于MVS的NeRF方法，以提高渲染质量。此外，我们的方法也是端到端可训练的，允许对特定场景进行微调。我们通过在大规模数据集上的实验证明了我们的方法的有效性，在大规模场景和无界户外场景中显示出显著的渲染质量改进。BoostMVSNeRFs的源代码发布于https://su-terry.github.io/BoostMVSNeRFs/. et.al.|[2407.15848](http://arxiv.org/abs/2407.15848)|null|
|**2024-07-22**|**6DGS: 6D Pose Estimation from a Single Image and a 3D Gaussian Splatting Model**|我们提出了6DGS来估计给定表示场景的3D高斯散斑（3DGS）模型的目标RGB图像的相机姿态。6DGS避免了典型的合成分析方法（如iNeRF）的迭代过程，该方法还需要初始化相机姿态才能收敛。相反，我们的方法通过反转3DGS渲染过程来估计6DoF姿态。从物体表面开始，我们定义了一个辐射Ellicell，它均匀地生成从每个椭球体出发的光线，这些椭球体对3DGS模型进行了参数化。每个Ellicell光线都与每个椭球体的渲染参数相关联，这些参数又用于获得目标图像像素和投射光线之间的最佳绑定。然后对这些像素光线绑定进行排序，以选择得分最高的光线束，它们的交点提供了相机中心，进而提供了相机旋转。所提出的解决方案消除了初始化时“先验”姿态的必要性，并以封闭形式解决了6DoF姿态估计问题，而不需要迭代。此外，与现有的用于姿态估计的新视图合成（NVS）基线相比，6DGS可以在真实场景中将整体平均旋转精度提高12%，平移精度提高22%，尽管不需要任何初始化姿态。同时，我们的方法近乎实时运行，在消费类硬件上达到15fps。 et.al.|[2407.15484](http://arxiv.org/abs/2407.15484)|null|
|**2024-07-19**|**SparseCraft: Few-Shot Neural Reconstruction through Stereopsis Guided Geometric Linearization**|我们提出了一种从少数彩色图像中恢复3D形状和视图相关外观的新方法，实现了高效的3D重建和新颖的视图合成。我们的方法以符号距离函数（SDF）和辐射场的形式学习隐式神经表示。该模型通过支持光线行进的体积渲染逐步训练，并使用无需学习的多视图立体（MVS）线索进行正则化。我们贡献的关键是一种新的隐式神经形状函数学习策略，该策略鼓励我们的SDF场在水平集附近尽可能线性，从而使训练对监督和正则化信号发出的噪声具有鲁棒性。在不使用任何预训练先验的情况下，我们的方法SparseCraft在新的视图合成和标准基准中从稀疏视图重建方面都达到了最先进的性能，同时只需要不到10分钟的训练时间。 et.al.|[2407.14257](http://arxiv.org/abs/2407.14257)|null|
|**2024-07-19**|**Mono-ViFI: A Unified Learning Framework for Self-supervised Single- and Multi-frame Monocular Depth Estimation**|自监督单目深度估计引起了人们的极大兴趣，因为它可以将训练从对深度注释的依赖中解放出来。在单目视频训练的情况下，最近的方法只在现有的摄像机视图之间进行视图合成，导致引导不足。为了解决这个问题，我们试图通过基于流的视频帧插值（VFI）来合成更多的虚拟相机视图，称为时间增强。对于多帧推理，为了避开基于显式几何的方法（如ManyDepth）遇到的动态对象问题，我们回到了特征融合范式，并设计了一个VFI辅助的多帧融合模块，使用基于流的VFI模型获得的运动和遮挡信息来对齐和聚合多帧特征。最后，我们构建了一个统一的自监督学习框架，名为Mono ViFI，以双向连接单帧和多帧深度。在这个框架中，通过图像仿射变换进行空间数据增强以实现数据多样性，同时进行正则化的三重深度一致性损失。单帧和多帧模型可以共享权重，使我们的框架紧凑且内存高效。大量实验表明，我们的方法可以为当前的先进架构带来重大改进。源代码可在https://github.com/LiuJF1226/Mono-ViFI. et.al.|[2407.14126](http://arxiv.org/abs/2407.14126)|**[link](https://github.com/liujf1226/mono-vifi)**|
|**2024-07-18**|**Shape of Motion: 4D Reconstruction from a Single Video**|由于单眼动态重建任务的高度不适定性，它是一个具有挑战性和长期存在的视觉问题。现有的方法存在局限性，因为它们要么依赖于模板，要么仅在准静态场景中有效，要么无法明确地对3D运动进行建模。在这项工作中，我们介绍了一种能够从随意捕获的单眼视频中重建具有显式、全序列长3D运动的通用动态场景的方法。我们通过两个关键的见解来解决这个问题的欠约束性质：首先，我们通过用一组紧凑的SE3运动基表示场景运动来利用3D运动的低维结构。每个点的运动都表示为这些基的线性组合，有助于将场景软分解为多个刚性移动的组。其次，我们利用了一套全面的数据驱动先验，包括单眼深度图和长距离2D轨迹，并设计了一种方法来有效地整合这些嘈杂的监控信号，从而得到动态场景的全局一致表示。实验表明，我们的方法在长距离3D/2D运动估计和动态场景上的新颖视图合成方面都取得了最先进的性能。项目页面：https://shape-of-motion.github.io/ et.al.|[2407.13764](http://arxiv.org/abs/2407.13764)|null|

<p align=right>(<a href=#updated-on-20240727>back to top</a>)</p>

## 3D Reconstruction

|Publish Date|Title|Abstract|PDF|Code|
|---|---|---|---|---|
|**2024-07-25**|**UMono: Physical Model Informed Hybrid CNN-Transformer Framework for Underwater Monocular Depth Estimation**|水下单目深度估计是水下场景三维重建等任务的基础。然而，由于光和介质的影响，水下环境经历了独特的成像过程，这给从单幅图像中准确估计深度带来了挑战。现有的方法未能考虑水下环境的独特特征，导致估计结果不足，泛化性能有限。此外，水下深度估计需要提取和融合局部和全局特征，这在现有方法中没有得到充分探索。本文提出了一种用于水下单目深度估计的端到端学习框架UMono，该框架将水下图像形成模型特征融入网络架构，有效地利用了水下图像的局部和全局特征。实验结果表明，该方法对水下单目深度估计是有效的，在定量和定性分析方面都优于现有方法。 et.al.|[2407.17838](http://arxiv.org/abs/2407.17838)|null|
|**2024-07-24**|**SMA-Hyper: Spatiotemporal Multi-View Fusion Hypergraph Learning for Traffic Accident Prediction**|预测交通事故是可持续城市管理的关键，这需要有效解决城市的动态和复杂的时空特征。当前的数据驱动模型经常与数据稀疏性作斗争，通常忽视了不同城市数据源的集成及其内部的高阶依赖关系。此外，它们经常依赖于预定义的拓扑或权重，限制了它们在时空预测中的适应性。为了解决这些问题，我们引入了时空多视图自适应超图学习（SMA Hyper）模型，这是一种为交通事故预测设计的动态深度学习框架。基于先前的研究，这一创新模型结合了双重自适应时空图学习机制，通过超图和动态适应不断变化的城市数据，实现了高阶跨区域学习。它还利用对比学习来增强稀疏数据集中的全局和局部数据表示，并采用预先注意机制来融合事故数据和城市功能特征的多种视图，从而丰富了对风险因素的上下文理解。对伦敦交通事故数据集的广泛测试表明，SMA Hyper模型在各种时间范围和多步输出方面明显优于基线模型，证实了其多视图融合和自适应学习策略的有效性。结果的可解释性进一步强调了其通过利用复杂的时空城市数据来改善城市交通管理和安全的潜力，提供了一个可扩展的框架，适用于不同的城市环境。 et.al.|[2407.17642](http://arxiv.org/abs/2407.17642)|null|
|**2024-07-21**|**A Novel Method to Improve Quality Surface Coverage in Multi-View Capture**|相机的景深是需要在短距离内拍摄图像或使用大焦距的应用的限制因素，如全身摄影、考古和其他近景摄影测量应用。此外，在多视图捕获中，当目标大于相机的视场时，优化捕获的表面覆盖质量的有效方法仍然是一个挑战。给定目标对象的3D网格和相机姿态，我们提出了一种新的方法来为每个相机推导焦距，以优化覆盖表面区域的质量。我们首先设计了一个期望最小化（EM）算法，将网格上的点唯一地分配给相机，然后在给定相关点集的情况下求解每个相机的焦距。我们通过提出一种 $k$-view算法来进一步提高质量表面覆盖率，该算法通过同时考虑多个视图来解决点分配和焦距问题。我们在各种全身摄影模拟下证明了所提出方法的有效性。EM和$k$-view算法分别将基线单视图方法的相对成本提高了至少24$%和28$%，相当于将聚焦表面积增加了大约1550$cm$^2$和1780$cm$^ 2$ 。我们认为，这些算法可用于许多需要摄影测量细节但受景深限制的视觉应用。 et.al.|[2407.15883](http://arxiv.org/abs/2407.15883)|null|
|**2024-07-22**|**Enhancement of 3D Gaussian Splatting using Raw Mesh for Photorealistic Recreation of Architectures**|建筑场景的真实感重建和渲染在电影、游戏和交通等行业有着广泛的应用。它在城市规划、建筑设计和城市推广方面也发挥着重要作用，特别是在保护历史文化遗产方面。由于其优于NeRF的性能，3D高斯散斑已成为3D重建的主流技术。它唯一的输入是一组图像，但它在很大程度上依赖于SfM过程计算的几何参数。与此同时，现有大量的原始3D模型可以为某些建筑物的结构感知提供信息，但无法应用。在这篇论文中，我们提出了一种直接的方法，利用这些原始的3D模型来引导3D高斯人捕捉建筑物的基本形状，并在非系统地捕捉照片时提高纹理和细节的视觉质量。这一探索为提高3D重建技术在建筑设计领域的有效性开辟了新的可能性。 et.al.|[2407.15435](http://arxiv.org/abs/2407.15435)|null|
|**2024-07-21**|**3D Reconstruction of the Human Colon from Capsule Endoscope Video**|随着受胃肠系统疾病影响的人数不断增加，对预防性筛查的更高要求是不可避免的。这将大大增加胃肠病学家的工作量。为了帮助减少工作量，计算机视觉工具可能会有所帮助。在这篇论文中，我们研究了使用无线胶囊内窥镜视频中的图像序列构建人体结肠整个切片的3D模型的可能性，为胃肠病学家提供了增强的观看体验。由于胶囊内窥镜图像包含失真和伪影，这对许多3D重建算法来说是不理想的，因此这个问题具有挑战性。然而，最近基于虚拟图形的人体胃肠系统模型的发展，可以启用或禁用失真和伪影，从而可以“剖析”这个问题。图形模型还提供了一个地面真实值，可以计算3D重建方法引入的几何失真。在这篇论文中，大多数失真和伪影被排除在外，以确定通过现有方法重建人体胃肠系统的整个部分是否可行。我们证明了使用同步定位和映射可以进行3D重建。此外，为了从密度变化很大的点云重建胃肠壁表面，泊松表面重建是一个不错的选择。研究结果很有希望，鼓励对这个问题进行进一步的研究。 et.al.|[2407.15228](http://arxiv.org/abs/2407.15228)|null|
|**2024-07-21**|**HoloDreamer: Holistic 3D Panoramic World Generation from Text Descriptions**|3D场景生成在各个领域都有很高的需求，包括虚拟现实、游戏和电影行业。由于文本到图像扩散模型具有强大的生成能力，可以提供可靠的先验信息，因此仅使用文本提示创建3D场景变得可行，从而显著推进了文本驱动的3D场景生成研究。为了从2D扩散模型中获得多视图监控，主流方法通常采用扩散模型生成初始局部图像，然后使用扩散模型迭代地绘制局部图像以逐渐生成场景。然而，这些基于外画的方法容易产生全局不一致的场景生成结果，没有高度的完整性，限制了它们更广泛的应用。为了解决这些问题，我们引入了HoloDreamer，这是一个框架，它首先生成高清全景作为完整3D场景的整体初始化，然后利用3D高斯散斑（3D-GS）快速重建3D场景，从而促进创建视图一致和完全封闭的3D场景。具体来说，我们提出了风格化的等矩形全景生成，这是一种结合了多个扩散模型的管道，可以从复杂的文本提示中生成风格化和详细的等矩形的全景。随后，引入了增强两阶段全景重建，对3D-GS进行两阶段优化，以输入缺失区域并增强场景的完整性。综合实验表明，在生成全封闭场景时，我们的方法在整体视觉一致性和和谐性以及重建质量和渲染鲁棒性方面优于先前的工作。 et.al.|[2407.15187](http://arxiv.org/abs/2407.15187)|null|
|**2024-07-21**|**VoxDepth: Rectification of Depth Images on Edge Devices**|自动飞行无人机和工业机器人等自主移动机器人在很大程度上依赖于深度图像来执行3D重建和视觉SLAM等任务。然而，这些深度图像中不准确的存在会极大地阻碍这些应用的有效性，导致次优结果。商用相机产生的深度图像经常出现噪声，表现为闪烁的像素和错误的补丁。基于ML的校正这些图像的方法不适合计算资源非常有限的边缘设备。非机器学习方法要快得多，但精度有限，特别是对于纠正因遮挡和相机移动而导致的错误。我们提出了一种名为VoxDepth的方案，该方案快速、准确，在边缘设备上运行良好。它依赖于一系列新技术：3D点云构建和融合，并使用它来创建一个可以修复错误深度图像的模板。VoxDepth在合成数据集和真实数据集上都显示出卓越的结果。与现实世界深度数据集上的最先进方法相比，我们的质量提高了31%，同时保持了27 FPS（每秒帧数）的竞争帧率。 et.al.|[2407.15067](http://arxiv.org/abs/2407.15067)|null|
|**2024-07-19**|**SparseCraft: Few-Shot Neural Reconstruction through Stereopsis Guided Geometric Linearization**|我们提出了一种从少数彩色图像中恢复3D形状和视图相关外观的新方法，实现了高效的3D重建和新颖的视图合成。我们的方法以符号距离函数（SDF）和辐射场的形式学习隐式神经表示。该模型通过支持光线行进的体积渲染逐步训练，并使用无需学习的多视图立体（MVS）线索进行正则化。我们贡献的关键是一种新的隐式神经形状函数学习策略，该策略鼓励我们的SDF场在水平集附近尽可能线性，从而使训练对监督和正则化信号发出的噪声具有鲁棒性。在不使用任何预训练先验的情况下，我们的方法SparseCraft在新的视图合成和标准基准中从稀疏视图重建方面都达到了最先进的性能，同时只需要不到10分钟的训练时间。 et.al.|[2407.14257](http://arxiv.org/abs/2407.14257)|null|
|**2024-07-19**|**I Know About "Up"! Enhancing Spatial Reasoning in Visual Language Models Through 3D Reconstruction**|视觉语言模型（VLMs）对于各种任务，特别是视觉推理任务至关重要，因为它们具有强大的多模态信息集成、视觉推理能力和上下文感知能力。然而，现有的视觉空间推理能力往往不足，即使在区分左右等基本任务上也很困难。为了解决这个问题，我们提出了我们的模型，旨在增强VLMS的视觉空间推理能力。ZeroVLM采用Zero1-to-3，这是一种3D重建模型，用于获得输入图像的不同视图，并结合了提示机制，以进一步改善视觉空间推理。在四个视觉空间推理数据集上的实验结果表明，我们的{}实现了高达19.48%的准确率提高，这表明了ZeroVLM的3D重建和提示机制的有效性。 et.al.|[2407.14133](http://arxiv.org/abs/2407.14133)|null|
|**2024-07-19**|**FAVis: Visual Analytics of Factor Analysis for Psychological Research**|心理学研究通常涉及通过对问卷收集的数据进行因子分析来理解心理结构，问卷可能包括数百个问题。如果没有用于解释因子模型的交互系统，研究人员经常会受到主观性的影响，这可能会导致误解或忽视关键信息。本文介绍了FAVis，这是一种新型的交互式可视化工具，旨在帮助研究人员解释和评估因子分析结果。FAVis通过支持多种视图来可视化因素载荷和相关性，使用户能够从不同角度分析信息，从而增强了对变量和因素之间关系的理解。FAVis的主要功能是使用户能够为因子负载设置最佳阈值，以平衡清晰度和信息保留。FAVis还允许用户为变量分配标签，通过将它们与相关的心理结构联系起来，增强对因素的理解。我们的用户研究证明了FAVis在各种任务中的实用性。 et.al.|[2407.14072](http://arxiv.org/abs/2407.14072)|null|

<p align=right>(<a href=#updated-on-20240727>back to top</a>)</p>

## Diffusion

|Publish Date|Title|Abstract|PDF|Code|
|---|---|---|---|---|
|**2024-07-25**|**RegionDrag: Fast Region-Based Image Editing with Diffusion Models**|基于点拖动的图像编辑方法，如DragDiffusion，引起了人们的广泛关注。然而，由于基于点的编辑指令的稀疏性，基于点拖动的方法存在计算开销和对用户意图的误解。本文提出了一种基于区域的复制粘贴拖动方法RegionDrag，以克服这些局限性。RegionDrag允许用户以句柄和目标区域的形式表达他们的编辑指令，从而实现更精确的控制并减轻歧义。此外，基于区域的操作在一次迭代中完成编辑，并且比基于点拖动的方法快得多。我们还采用了注意力交换技术，以提高编辑过程中的稳定性。为了验证我们的方法，我们使用基于区域的拖动指令扩展了现有的基于点拖动的数据集。实验结果表明，RegionDrag在速度、准确性和与用户意图的一致性方面优于现有的基于点拖动的方法。值得注意的是，RegionDrag在不到2秒的时间内完成了对分辨率为512x512的图像的编辑，这比DragDiffusion快100多倍，同时实现了更好的性能。项目页面：https://visual-ai.github.io/regiondrag. et.al.|[2407.18247](http://arxiv.org/abs/2407.18247)|null|
|**2024-07-25**|**VGGHeads: A Large-Scale Synthetic Dataset for 3D Human Heads**|人体头部检测、关键点估计和3D头部模型拟合是许多应用的重要任务。然而，传统的现实世界数据集往往受到偏见、隐私和伦理问题的困扰，并且它们是在实验室环境中记录的，这使得训练好的模型难以泛化。在这里，我们介绍VGGHeads——一个使用扩散模型生成的大规模合成数据集，用于人体头部检测和3D网格估计。我们的数据集包括100多万张高分辨率图像，每张图像都带有详细的3D头部网格、面部界标和边界框。使用该数据集，我们引入了一种新的模型架构，能够在一步中从单个图像中同时进行头部检测和头部网格重建。通过广泛的实验评估，我们证明了在我们的合成数据上训练的模型在真实图像上具有很强的性能。此外，我们数据集的多功能性使其适用于广泛的任务，提供了人类头部的一般和全面的表示。此外，我们还提供了有关合成数据生成管道的详细信息，使其能够重新用于其他任务和领域。 et.al.|[2407.18245](http://arxiv.org/abs/2407.18245)|null|
|**2024-07-25**|**$A+A \to A$, $\; \; B+A \to A$**|本文考虑了对于$d\geq 3$，在$\mathbb{Z}^d$ 上扩散和反应粒子的平移不变两物种系统的粒子强度衰减。强度被证明近似求解了修正的速率方程，从中可以推导出它们的多项式衰减。该系统表明，尽管系统在超临界维度上进化，但潜在的扩散和反应速率会影响精确的多项式衰变速率。 et.al.|[2407.18212](http://arxiv.org/abs/2407.18212)|null|
|**2024-07-25**|**Chemically reactive and aging macromolecular mixtures II: Phase separation and coarsening**|在一篇配套论文中，我们提出了一个热力学模型，用于通过涉及多种大分子物种的化学反应形成络合物，这些物质随后可能经历液-液相分离并进一步转变为凝胶状状态。在本研究中，我们构建了一个热力学一致的动力学框架，以研究空间不均匀大分子混合物中相分离、化学反应和老化之间的相互作用。还提出了一种数值算法，用于模拟二维和三维空间中液体和凝胶畴通过被动布朗运动碰撞产生的畴生长。我们的结果表明，粗化行为受到凝胶化程度和布朗运动的显著影响。凝析油中凝胶相的存在强烈限制了扩散传输过程，布朗运动聚结控制了凝胶状凝析油高面积/体积分数系统中的粗化过程，导致形成相互连接的畴，其非典型畴生长速率由尺寸依赖的平移和旋转扩散率控制。 et.al.|[2407.18171](http://arxiv.org/abs/2407.18171)|null|
|**2024-07-25**|**Solvability and optimal control of a multi-species Cahn-Hilliard-Keller-Segel tumor growth model**|本文研究了与二维多物种Cahn-Hilliard-Keller Segel肿瘤生长模型相关的最优控制问题，该模型结合了物种扩散、趋化性、血管生成和营养消耗等复杂的生物过程，从而形成了一个高度非线性的非线性偏微分方程系统。建模推导和相应的分析在之前的文章中已经讨论过。在此基础上，本研究的范围涉及研究分布式控制问题，目标是优化跟踪型成本函数。后者旨在最大限度地减少肿瘤细胞位置与所需靶配置的偏差，同时惩罚与实施控制措施相关的成本，类似于引入合适的药物。在适当的数学假设下，我们证明了充分正则解对控制变量具有连续依赖性。此外，我们建立了最优控制的存在性，并通过适当的变分不等式表征了一阶必要最优性条件。 et.al.|[2407.18162](http://arxiv.org/abs/2407.18162)|null|
|**2024-07-25**|**Self-supervised pre-training with diffusion model for few-shot landmark detection in x-ray images**|在过去的几年里，深度神经网络在医学领域得到了广泛的应用，用于不同的任务，从图像分类和分割到地标检测。然而，这些技术在医学领域的应用往往受到数据稀缺的阻碍，无论是在可用的注释还是图像方面。本研究介绍了一种基于扩散模型的新的自监督预训练协议，用于x射线图像中的地标检测。我们的结果表明，所提出的自监督框架可以用最少数量的可用带注释训练图像（最多50个）提供准确的地标检测，在三个流行的x射线基准数据集上优于ImageNet监督预训练和最先进的自监督预训练。据我们所知，这是首次探索用于地标检测中的自监督学习的扩散模型，这可能为缓解数据稀缺提供了一种在少数情况下有价值的预训练方法。 et.al.|[2407.18125](http://arxiv.org/abs/2407.18125)|null|
|**2024-07-25**|**Testing non-local gravity through Ultra-Diffuse Galaxies kinematics**|近年来，超扩散星系的出现对星系形成模型和引力扩展理论提出了严峻的挑战。在同一类天体物理物体中，暗物质缺失和暗物质主导的系统的存在确实要求引力模型具有足够的通用性，以描述非常不同的引力机制。在这项工作中，我们研究了广义相对论的一个非局部扩展，该理论近年来引起了越来越多的关注，因为它能够在不引入任何暗能量流体的情况下解释晚期宇宙加速。我们利用了三个超漫射星系的运动学数据：缺乏暗物质的NGC 1052-DF2和NGC 1052-TF4，以及表现出高度主导暗物质成分的蜻蜓44。我们的分析表明，牛顿势的非局部修正不会影响运动学预测，因此当非局部引力模型作为暗能量模型时，不会出现破坏效应。我们还提供了特征非局部半径在这些质量尺度下可以达到的最小值。 et.al.|[2407.18084](http://arxiv.org/abs/2407.18084)|null|
|**2024-07-25**|**Equation of state of Bose gases beyond the universal regime**|稀玻色气体的状态方程，其中能量仅取决于波散射长度，在普遍极限之外是相当未知的。我们进行了一系列扩散蒙特卡罗计算，气体参数高达10^{-2} $，以探索如何偏离普遍性。使用不同的模型势，我们在一定的统计噪声范围内以精确的方式计算气体的能量，并将结果作为三个相关散射参数的函数进行报告：$s$波散射长度$a_0$、$s$波有效范围$r_0$和$p$波散射长度$a_1$。如果有效范围不大，我们观察到$a_0$和$r_0$的普适性，直到气体参数为$10^{-2}$。如果$r_0$增长，这两个参数的普适性机制就会降低，并且开始观察到$a_1$的影响。在$（a_0，r_0）$ 泛域中，我们提出了一个分析定律，该定律很好地再现了精确的能量。 et.al.|[2407.18059](http://arxiv.org/abs/2407.18059)|null|
|**2024-07-25**|**AttentionHand: Text-driven Controllable Hand Image Generation for 3D Hand Reconstruction in the Wild**|最近，人们对使用各种形式的人机交互进行3D手部重建进行了大量研究。然而，由于极度缺乏野外3D手数据集，野外3D手重建具有挑战性。特别是当手处于复杂姿势时，如相互作用的手，外观相似性、双手闭合和深度模糊等问题使其变得更加困难。为了克服这些问题，我们提出了一种新的文本驱动可控手图像生成方法AttentionHand。由于AttentionHand可以生成与3D手标对齐的各种和大量的野生手图像，我们可以获得一个新的3D手数据集，并可以缓解室内和室外场景之间的领域差距。我们的方法需要易于使用的四种模态（即RGB图像、来自3D标签的手网格图像、边界框和文本提示）。这些模态通过编码阶段嵌入到潜在空间中。然后，通过文本注意阶段，关注给定文本提示中的手相关标记，以突出潜在嵌入的手相关区域。在突出显示的嵌入被馈送到视觉注意力阶段后，通过基于扩散的流水线对全局和局部手网格图像进行调节，来关注嵌入中与手相关的区域。在解码阶段，最终特征被解码为新的手部图像，这些图像与给定的手部网格图像和文本提示对齐良好。因此，AttentionHand在文本到手图像生成模型中达到了最先进的水平，并且通过使用AttentionHand生成的手图像进行额外训练，提高了3D手网格重建的性能。 et.al.|[2407.18034](http://arxiv.org/abs/2407.18034)|null|
|**2024-07-25**|**Three-dimensional exponential mixing and ideal kinematic dynamo with randomized ABC flows**|在这项工作中，我们考虑了三维周期盒中Arnold-Beltrami-Childress（ABC）随机版本的拉格朗日性质。我们证明了关联流图具有正的顶部李雅普诺夫指数，其关联的一点、两点和投影马尔可夫链是几何遍历的。对于被动标量，这样的速度是一个时空平滑的指数混合场，扩散系数均匀。对于被动矢量，它提供了一个通用理想（即非扩散）运动发电机的例子。 et.al.|[2407.18028](http://arxiv.org/abs/2407.18028)|null|

<p align=right>(<a href=#updated-on-20240727>back to top</a>)</p>

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

<p align=right>(<a href=#updated-on-20240727>back to top</a>)</p>

[contributors-shield]: https://img.shields.io/github/contributors/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[contributors-url]: https://github.com/Vincentqyw/cv-arxiv-daily/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[forks-url]: https://github.com/Vincentqyw/cv-arxiv-daily/network/members
[stars-shield]: https://img.shields.io/github/stars/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[stars-url]: https://github.com/Vincentqyw/cv-arxiv-daily/stargazers
[issues-shield]: https://img.shields.io/github/issues/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[issues-url]: https://github.com/Vincentqyw/cv-arxiv-daily/issues

