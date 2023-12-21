[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]

## Updated on 2023.12.21
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
|**2023-12-20**|**DiffPortrait3D: Controllable Diffusion for Zero-Shot Portrait View Synthesis**|我们提出了DiffPortrait3D，这是一种条件扩散模型，能够从野生肖像中的一张照片中合成3D一致的照片逼真的新颖视图。具体来说，在给定单个RGB输入的情况下，我们的目标是合成从新颖的相机视图中呈现的看似合理但一致的面部细节，同时保留身份和面部表情。除了耗时的优化和微调外，我们的零样本方法很好地推广到任意面部肖像，具有无污染的相机视图、极端的面部表情和多样化的艺术描绘。其核心是，我们利用在大规模图像数据集上预先训练的2D扩散模型的生成先验作为我们的渲染骨干，而去噪是通过对外观和相机姿态的细致控制来指导的。为了实现这一点，我们首先将参考图像的外观上下文注入冻结的UNets的自关注层。然后利用新颖的条件控制模块来操纵渲染视图，该条件控制模块通过从同一视图观看交叉对象的条件图像来解释相机姿态。此外，我们插入了一个可训练的跨视图注意力模块来增强视图一致性，在推理过程中，通过一个新颖的3D感知噪声生成过程进一步增强了视图一致性。我们在野外和多视图基准测试中展示了最先进的定性和定量结果。 et.al.|[2312.13016](http://arxiv.org/abs/2312.13016)|null|
|**2023-12-20**|**Radar Fields: An Extension of Radiance Fields to SAR**|辐射场是多视图图像采集中复杂场景的反向渲染、新颖视图合成和3D建模领域的一个重大突破。自从它们被引入以来，已经表明它们可以扩展到其他模式，如激光雷达、射频、X射线或超声波。在本文中，我们表明，尽管光学和合成孔径雷达（SAR）图像形成模型之间存在重要差异，但有可能将辐射场扩展到雷达图像，从而呈现第一个“雷达场”。这使我们能够仅使用雷达图像的集合来学习表面模型，类似于规则辐射场的学习方式，并且平均具有相同的计算复杂度。由于这两个领域的定义方式相似，这项工作也显示了将光学图像和SAR图像相结合的混合方法的潜力。 et.al.|[2312.12961](http://arxiv.org/abs/2312.12961)|null|
|**2023-12-19**|**pixelSplat: 3D Gaussian Splats from Image Pairs for Scalable Generalizable 3D Reconstruction**|我们介绍了pixelSplat，这是一种前馈模型，它学习从成对的图像中重建由3D高斯基元参数化的3D辐射场。我们的模型具有实时和内存高效的渲染功能，可进行可扩展训练，并在推理时进行快速3D重建。为了克服稀疏和局部支持表示固有的局部极小值，我们预测了三维上的稠密概率分布，并根据该概率分布对高斯均值进行采样。我们通过重新参数化技巧使这种采样操作可微分，允许我们通过高斯飞溅表示反向传播梯度。我们在真实世界的RealEstate10k和ACID数据集上以宽基线新视图合成为基准，在那里我们优于最先进的光场变换器，并将渲染加速2.5个数量级，同时重建可解释和可编辑的3D辐射场。 et.al.|[2312.12337](http://arxiv.org/abs/2312.12337)|null|
|**2023-12-20**|**MixRT: Mixed Neural Representations For Real-Time NeRF Rendering**|神经辐射场（NeRF）由于其令人印象深刻的真实感重建和渲染能力，已成为新型视图合成的领先技术。然而，在大规模场景中实现实时NeRF渲染带来了挑战，通常导致采用具有大量三角形的复杂烘焙网格表示或烘焙表示中的资源密集型光线行进。我们对这些约定提出了质疑，注意到由具有实质三角形的网格表示的高质量几何体对于实现照片级真实感渲染质量是不必要的。因此，我们提出了MixRT，这是一种新的NeRF表示，包括低质量网格、视图相关位移图和压缩的NeRF模型。这种设计有效地利用了现有图形硬件的功能，从而实现了边缘设备上的实时NeRF渲染。利用高度优化的基于WebGL的渲染框架，我们提出的MixRT在边缘设备上实现了实时渲染速度（在MacBook M1 Pro笔记本电脑上以1280 x 720的分辨率超过30 FPS）、更好的渲染质量（在Unboundd-360数据集的室内场景中高出0.2 PSNR）和更小的存储大小（与最先进的方法相比，小于80%）。 et.al.|[2312.11841](http://arxiv.org/abs/2312.11841)|null|
|**2023-12-18**|**GauFRe: Gaussian Deformation Fields for Real-time Dynamic Novel View Synthesis**|我们提出了一种使用可变形3D高斯进行动态场景重建的方法，该方法适用于单目视频。在高斯飞溅效率的基础上，我们的方法通过位于规范空间中的可变形高斯集和由多层感知器（MLP）定义的时间相关变形场来扩展表示以适应动态元素。此外，在大多数自然场景都有保持静态的大区域的假设下，我们允许MLP通过额外包括静态高斯点云来集中其代表能力。串联的动态和静态点云形成高斯飞溅光栅化器的输入，从而实现实时渲染。在自监督渲染损失的情况下，对可微管道进行端到端优化。我们的方法获得的结果与最先进的动态神经辐射场方法相当，同时允许更快的优化和渲染。项目网站：https://lynl7130.github.io/gaufre/index.html et.al.|[2312.11458](http://arxiv.org/abs/2312.11458)|null|
|**2023-12-18**|**SinMPI: Novel View Synthesis from a Single Image with Expanded Multiplane Images**|单图像新视图合成是一个具有挑战性且正在进行的问题，其目的是从单个输入图像生成无限数量的一致视图。尽管已经做出了重大努力来提高生成的新视图的质量，但对底层场景表示的扩展却关注较少，这对生成逼真的新视图图像至关重要。本文提出了SinMPI，这是一种使用扩展多平面图像（MPI）作为3D场景表示的新方法，可以显著扩展MPI的透视范围，并从大的多平面空间生成高质量的新视图。我们的方法的关键思想是使用稳定扩散生成视图外内容，根据单目深度估计器预测的深度将所有场景内容投影到扩展的多平面图像中，然后在深度感知扭曲和修复模块生成的伪多视图数据的监督下优化多平面图像。我们进行了定性和定量实验，以验证我们的方法相对于现有技术的优越性。我们的代码和数据可在https://github.com/trickygo/sinmpi. et.al.|[2312.11037](http://arxiv.org/abs/2312.11037)|**[link](https://github.com/trickygo/sinmpi)**|
|**2023-12-18**|**T-Code: Simple Temporal Latent Code for Efficient Dynamic View Synthesis**|动态场景的新颖视图合成是计算机视觉研究的热点之一。有效的动态视图合成的关键是找到一个紧凑的表示来存储跨时间的信息。尽管现有的方法通过张量分解或哈希网格特征级联来实现快速的动态视图合成，但它们的混合表示忽略了时域和空域之间的结构差异，导致计算和存储成本次优。本文提出了仅在时间维度上有效解耦的潜码T码。分解的功能设计使定制模块能够满足不同场景的个性化需求，并以更低的成本产生所需的结果。基于T代码，我们提出了用于多摄像机设置的高度紧凑的混合神经图形基元（HybridNGP）和用于单目场景的具有T代码的变形神经图形基基元（DNGP-T）。实验表明，HybridNGP以极低的存储消耗以最高的处理速度提供高保真度结果，而DNGP-T则实现了最先进的单目重建质量和高训练速度。 et.al.|[2312.11015](http://arxiv.org/abs/2312.11015)|null|
|**2023-12-17**|**PNeRFLoc: Visual Localization with Point-based Neural Radiance Fields**|由于能够合成高质量的新视图，神经辐射场（NeRF）最近被用来改善已知环境中的视觉定位。然而，现有的方法大多利用NeRFs进行数据扩充来改进回归模型的训练，并且由于缺乏几何约束，在新的视点和外观上的性能仍然有限。在本文中，我们提出了一种新的基于统一点表示的视觉定位框架，即PNeRFLoc。一方面，PNeRFLoc像传统的基于结构的方法一样，通过匹配2D和3D特征点来支持初始姿态估计；另一方面，它还通过使用基于渲染的优化的新颖视图合成来实现姿态细化。具体来说，我们提出了一种新的特征自适应模块来缩小视觉定位和神经渲染特征之间的差距。为了提高基于神经渲染的优化的有效性和效率，我们还开发了一个具有扭曲损失函数的高效基于渲染的框架。此外，还开发了几种鲁棒性技术来处理室外场景的照明变化和动态对象。实验表明，当NeRF模型可以很好地学习时，PNeRFLoc在合成数据上表现最好，并且在视觉定位基准数据集上表现与SOTA方法相当。 et.al.|[2312.10649](http://arxiv.org/abs/2312.10649)|null|
|**2023-12-15**|**SlimmeRF: Slimmable Radiance Fields**|神经辐射场（NeRF）及其变体最近已成为新型视图合成和3D场景重建的成功方法。然而，大多数当前的NeRF模型要么使用大的模型尺寸来实现高精度，要么通过权衡精度来实现高存储效率。这限制了任何单个模型的适用范围，因为高精度模型可能不适合低内存设备，而高效内存模型可能无法满足高质量要求。为此，我们提出了SlimmeRF模型，该模型允许通过精简在模型大小和准确性之间进行即时测试时间权衡，从而使模型同时适用于具有不同计算预算的场景。我们通过一种新提出的名为张量秩增量（TRaIn）的算法来实现这一点，该算法在训练过程中逐渐增加模型张量表示的秩。我们还观察到，我们的模型允许在稀疏视图场景中进行更有效的权衡，有时甚至在精简后实现更高的精度。我们将此归功于这样一个事实，即错误信息（如浮动信息）往往存储在与更高级别相对应的组件中。我们的实施可在https://github.com/shiran-yuan/slimmerf. et.al.|[2312.10034](http://arxiv.org/abs/2312.10034)|**[link](https://github.com/shiran-yuan/slimmerf)**|
|**2023-12-15**|**RANRAC: Robust Neural Scene Representations via Random Ray Consensus**|我们介绍了RANRAC，这是一种用于处理遮挡和分心图像的3D对象的鲁棒重建算法，这是现有鲁棒重建方法无法处理的一个特别具有挑战性的场景。我们的解决方案通过涉及光场网络支持单镜头重建，也适用于基于神经辐射场的真实世界图像的照片逼真、鲁棒、多视图重建。虽然该算法对场景表示以及支持的场景类型施加了一定的限制，但它可靠地检测并排除了不一致的视角，从而产生了没有浮动伪影的干净图像。我们的解决方案基于随机样本一致性范式的模糊自适应，使其能够应用于大规模模型。我们将确定模型参数的最小样本数解释为可调超参数。这是适用的，因为更干净的样本集提高了重建质量。此外，此过程还处理异常值。特别是对于条件模型，它可以在潜在空间中产生与完全干净集相同的局部最小值。我们报告了在遮挡场景中新视图合成的显著改进，与基线相比，PSNR高达8dB。 et.al.|[2312.09780](http://arxiv.org/abs/2312.09780)|null|

<p align=right>(<a href=#updated-on-20231221>back to top</a>)</p>

## 3D Reconstruction

|Publish Date|Title|Abstract|PDF|Code|
|---|---|---|---|---|
|**2023-12-20**|**UniSDF: Unifying Neural Representations for High-Fidelity 3D Reconstruction of Complex Scenes with Reflections**|神经3D场景表示已经显示出从2D图像进行3D重建的巨大潜力。然而，重建复杂场景的真实世界捕捉仍然是一个挑战。现有的通用3D重建方法通常难以表示精细的几何细节，并且不能充分地对大规模场景的反射表面进行建模。明确关注反射表面的技术可以通过利用更好的反射参数化来对复杂和详细的反射进行建模。然而，我们观察到，在存在非反射和反射组件的真实无界场景中，这些方法通常是不稳健的。在这项工作中，我们提出了UniSDF，这是一种通用的3D重建方法，可以重建具有反射的大型复杂场景。我们研究了基于视图和基于反射的颜色预测参数化技术，发现在3D空间中显式混合这些表示可以重建几何精度更高的表面，尤其是反射表面。我们进一步将这种表示与多分辨率网格主干相结合，该主干以从粗到细的方式进行训练，从而实现比先前方法更快的重建。在对象级数据集DTU、Shiny Blender以及无界数据集Mip NeRF 360和Ref NeRF real上进行的大量实验表明，我们的方法能够稳健地重建具有精细细节和反射表面的复杂大规模场景。请参阅我们的项目页面https://fangjinhuawang.github.io/unisdf. et.al.|[2312.13285](http://arxiv.org/abs/2312.13285)|null|
|**2023-12-20**|**Splatter Image: Ultra-Fast Single-View 3D Reconstruction**|我们介绍了飞溅图像，这是一种用于单目3D对象重建的超快速方法，其操作速度为38 FPS。飞溅图像是基于高斯飞溅的，它最近为多视图重建带来了实时渲染、快速训练和出色的缩放能力。我们首次在单目重建设置中应用高斯散射。我们的方法是基于学习的，在测试时，重建只需要对神经网络进行前馈评估。Splatter Image的主要创新是令人惊讶的简单设计：它使用2D图像到图像网络将输入图像映射到每个像素一个3D高斯。由此产生的高斯图像具有图像的形式，即飞溅图像。我们进一步扩展了该方法，将多个图像作为输入，我们通过添加跨视图注意力来实现这一点。由于渲染器的速度（588 FPS），我们可以使用单个GPU进行训练，同时在每次迭代时生成整个图像，以优化LPIPS等感知指标。在标准基准上，我们不仅证明了快速重建，而且在PSNR、LPIPS和其他指标方面，比最近的更昂贵的基线取得了更好的结果。 et.al.|[2312.13150](http://arxiv.org/abs/2312.13150)|**[link](https://github.com/szymanowiczs/splatter-image)**|
|**2023-12-19**|**pixelSplat: 3D Gaussian Splats from Image Pairs for Scalable Generalizable 3D Reconstruction**|我们介绍了pixelSplat，这是一种前馈模型，它学习从成对的图像中重建由3D高斯基元参数化的3D辐射场。我们的模型具有实时和内存高效的渲染功能，可进行可扩展训练，并在推理时进行快速3D重建。为了克服稀疏和局部支持表示固有的局部极小值，我们预测了三维上的稠密概率分布，并根据该概率分布对高斯均值进行采样。我们通过重新参数化技巧使这种采样操作可微分，允许我们通过高斯飞溅表示反向传播梯度。我们在真实世界的RealEstate10k和ACID数据集上以宽基线新视图合成为基准，在那里我们优于最先进的光场变换器，并将渲染加速2.5个数量级，同时重建可解释和可编辑的3D辐射场。 et.al.|[2312.12337](http://arxiv.org/abs/2312.12337)|null|
|**2023-12-19**|**EVI-SAM: Robust, Real-time, Tightly-coupled Event-Visual-Inertial State Estimation and 3D Dense Mapping**|事件摄像机是受生物启发的运动激活传感器，在处理具有挑战性的情况（如运动模糊和高动态范围）方面表现出巨大的潜力。在本文中，我们提出了EVI-SAM来解决使用单目事件相机进行6自由度姿态跟踪和三维重建的问题。利用特征匹配的鲁棒性和直接对准的精度，设计了一种新的基于事件的混合跟踪框架来估计姿态。具体来说，我们开发了一种基于事件的2D-2D对齐来构建光度约束，并将其与基于事件的重投影约束紧密集成。映射模块通过基于图像引导的事件映射方法来恢复场景的密集和丰富多彩的深度。随后，可以通过使用截断符号距离函数（TSDF）融合来自多个视点的密集深度图来重建3D场景的外观、纹理和表面网格。据我们所知，这是第一个实现基于事件的密集映射的非学习工作。在公开的和自行收集的数据集上进行了数值评估，定性和定量地证明了我们方法的优越性能。我们的EVI-SAM有效地平衡了准确性和稳健性，同时保持了计算效率，在具有挑战性的场景中展示了卓越的姿态跟踪和密集映射性能。视频演示：https://youtu.be/nn40u4e5si8. et.al.|[2312.11911](http://arxiv.org/abs/2312.11911)|null|
|**2023-12-17**|**Primitive-based 3D Human-Object Interaction Modelling and Programming**|在三维环境中嵌入人与关节对象交互（HAOI）是深入理解人类活动的一个重要方向。与以往使用参数化和CAD模型来表示人和物体的工作不同，在这项工作中，我们提出了一种新的基于三维几何图元的语言来对人和物体进行编码。在我们的新范式下，人和物体都是原语的组成部分，而不是异构实体。因此，可以在人类的有限3D数据和不同对象类别之间实现相互信息学习。此外，考虑到表达式的简单性和所包含信息的丰富性，我们选择超二次曲面作为原始表示。为了探索机器的HAOI的有效嵌入，我们在由基元及其图像组成的3D HAOI上建立了一个新的基准，并提出了一项任务，要求机器使用图像中的基元恢复三维HAOI。此外，我们提出了基于HAOI的单视图三维重建的基线。我们相信，这种基于原始的3D HAOI表示将为3D HAOI研究铺平道路。我们的代码和数据可在https://mvig-rhos.com/p3haoi. et.al.|[2312.10714](http://arxiv.org/abs/2312.10714)|null|
|**2023-12-16**|**Triplane Meets Gaussian Splatting: Fast and Generalizable Single-View 3D Reconstruction with Transformers**|生成模型的发展推动了从单个图像进行3D重建的最新进展。其中最突出的是基于分数蒸馏采样（SDS）的方法和3D域中扩散模型的自适应。尽管这些技术取得了进展，但由于优化或渲染过程缓慢，导致训练和优化时间过长，这些技术往往面临限制。在本文中，我们介绍了一种新的单视图重建方法，该方法通过前馈推理从单个图像有效地生成3D模型。我们的方法利用两个基于变换器的网络，即点解码器和三平面解码器，使用混合三平面高斯中间表示来重建3D对象。这种混合表示实现了平衡，与隐式表示相比，实现了更快的渲染速度，同时提供了比显式表示更高的渲染质量。点解码器被设计用于从单个图像生成点云，提供显式表示，然后由三平面解码器使用该显式表示来查询每个点的高斯特征。这种设计选择解决了与直接回归以其非结构性质为特征的显式三维高斯属性相关的挑战。随后，通过MLP对3D高斯进行解码，以实现通过飞溅的快速渲染。这两个解码器都建立在可扩展的、基于转换器的架构上，并在大规模3D数据集上进行了有效的训练。对合成数据集和真实世界图像进行的评估表明，与以前最先进的技术相比，我们的方法不仅实现了更高的质量，而且确保了更快的运行时间。请参阅我们的项目页面https://zouzx.github.io/triplanegaussian/. et.al.|[2312.09147](http://arxiv.org/abs/2312.09147)|null|
|**2023-12-14**|**Living Scenes: Multi-object Relocalization and Reconstruction in Changing 3D Environments**|对动态3D场景理解的研究主要集中在密集观测的短期变化跟踪上，而很少关注稀疏观测的长期变化。我们用MoRE解决了这一差距，MoRE是一种在进化环境中进行多对象重新定位和重建的新方法。我们将这些环境视为“真实场景”，并考虑将在不同时间点进行的扫描转换为对象实例的3D重建的问题，其准确性和完整性会随着时间的推移而提高。我们方法的核心是在合成数据上训练的单个编码器-解码器网络中的SE（3）-等变表示。这种表示使我们能够无缝地处理实例匹配、注册和重建。我们还引入了一种联合优化算法，该算法有助于在不同时间点进行的多次扫描中积累源自同一实例的点云。我们在合成和真实世界的数据上验证了我们的方法，并在端到端性能和单个子任务中展示了最先进的性能。 et.al.|[2312.09138](http://arxiv.org/abs/2312.09138)|null|
|**2023-12-14**|**Learned Fusion: 3D Object Detection using Calibration-Free Transformer Feature Fusion**|使用传感器融合的3D对象检测的现有技术在很大程度上依赖于校准质量，这在实验室环境之外的大规模部署中很难维持。我们提出了第一种用于三维物体检测的无校准方法。因此，消除了对复杂且昂贵的校准程序的需要。我们的方法使用转换器在多个抽象级别上映射不同传感器的多个视图之间的特征。在对物体检测的广泛评估中，我们不仅表明我们的方法在BEV mAP中比单模态设置好14.1%，而且转换器确实学习了映射。通过表明传感器融合不需要校准，我们希望激励其他研究人员遵循无校准融合的方向。此外，由此产生的方法对旋转和平移变化具有相当大的弹性。 et.al.|[2312.09082](http://arxiv.org/abs/2312.09082)|null|
|**2023-12-14**|**Scene 3-D Reconstruction System in Scattering Medium**|随着新模型和扩展的发展，用于新视图合成的神经辐射场研究经历了爆炸式增长。适用于水下场景或散射介质的NERF算法也在不断发展。现有的水下三维重建系统仍然面临训练时间长、渲染效率低等挑战。本文提出了一种改进的水下三维重建系统来解决这些问题，并实现快速、高质量的三维重建。首先，我们增强了单眼相机拍摄的水下视频，以纠正水介质物理特性造成的图像质量差的问题，同时确保相邻帧增强的一致性。随后，我们对视频帧进行关键帧选择，以优化资源利用率，消除动态对象对重建结果的影响。所选关键帧在使用COLMAP进行姿态估计后，使用基于多分辨率哈希编码的神经辐射场进行三维重建改进过程，用于模型构建和渲染。 et.al.|[2312.09005](http://arxiv.org/abs/2312.09005)|null|
|**2023-12-13**|**ProNeRF: Learning Efficient Projection-Aware Ray Sampling for Fine-Grained Implicit Neural Radiance Fields**|神经渲染的最新进展表明，尽管速度较慢，但隐式紧凑模型可以从多个视图中学习场景的几何图形和视图相关外观。为了保持如此小的内存占用，但实现更快的推理时间，最近的工作采用了“采样器”网络，该网络自适应地对隐式神经辐射场中沿每条射线的一小部分点进行采样。尽管这些方法在渲染时间上减少了10美元\倍，但与香草NeRF相比，它们的质量仍有相当大的下降。相反，我们提出了ProNeRF，它在内存占用（类似于NeRF）、速度（比HyperReel快）和质量（比K-Planes好）之间提供了最佳折衷。ProNeRF配备了一种新的投影感知采样（PAS）网络，以及一种用于射线探测和利用的新训练策略，从而实现高效的细粒度粒子采样。我们的ProNeRF产生了最先进的指标，比NeRF快15-23倍，PSNR比NeRF高0.65dB，比已发表的最佳基于采样器的方法HyperReel高0.95dB。我们的探索和开发训练策略使ProNeRF能够学习完整场景的颜色和密度分布，同时学习聚焦于最高密度区域的高效光线采样。我们提供了广泛的实验结果，分别在广泛采用的前向和360数据集LLFF和Blender上支持我们的方法的有效性。 et.al.|[2312.08136](http://arxiv.org/abs/2312.08136)|null|

<p align=right>(<a href=#updated-on-20231221>back to top</a>)</p>

## Diffusion

|Publish Date|Title|Abstract|PDF|Code|
|---|---|---|---|---|
|**2023-12-20**|**A structure preserving discretization for the Derrida-Lebowitz-Speer-Spohn equation based on diffusive transport**|我们提出了四阶非线性DLSS方程在圆上的空间离散化。我们选择离散化的动机是关于推广鞅输运的度量的一个新的梯度流公式。离散动力学继承了这种梯度流结构，以及其他性质，如Wasserstein距离中的替代梯度流公式、Hellinger距离中的压缩性和几个Lypunov泛函的单调性。我们的主要结果是收敛于消失网格大小的极限。该证明依赖于涉及二阶导数的积分表达式之间的非线性函数不等式的离散版本。 et.al.|[2312.13284](http://arxiv.org/abs/2312.13284)|null|
|**2023-12-20**|**Repaint123: Fast and High-quality One Image to 3D Generation with Progressive Controllable 2D Repainting**|最近的单图像到3D生成方法通常采用分数蒸馏采样（SDS）。尽管取得了令人印象深刻的结果，但仍存在多个缺陷，包括多视图不一致、纹理过饱和和过平滑，以及生成速度慢。为了解决这些不足，我们提出了Repaint123，以减轻多视图偏见以及纹理退化，并加快生成过程。核心思想是将2D扩散模型强大的图像生成能力和重绘策略的纹理对齐能力相结合，生成具有一致性的高质量多视图图像。我们进一步提出了重叠区域的可见性感知自适应重绘强度，以增强重绘过程中生成的图像质量。生成的高质量和多视图一致的图像使得能够使用简单的均方误差（MSE）损失来快速生成3D内容。我们进行了广泛的实验，并表明我们的方法具有卓越的能力，可以在2分钟内从头开始生成具有多视图一致性和精细纹理的高质量3D内容。代码位于https://github.com/junwuzhang19/repaint123. et.al.|[2312.13271](http://arxiv.org/abs/2312.13271)|**[link](https://github.com/junwuzhang19/repaint123)**|
|**2023-12-20**|**Conditional Image Generation with Pretrained Generative Model**|近年来，与GAN模型相比，扩散模型因其生成更高质量图像的能力而广受欢迎。然而，与任何其他大型生成模型一样，这些模型需要大量的数据、计算资源和细致的调整才能成功训练。这是一个重大挑战，使其对大多数人来说不可行。因此，研究界设计了一些方法，利用预先训练的无条件扩散模型和额外的指导，以实现条件图像生成的目的。这些方法能够在不同的输入上进行有条件的图像生成，并且最重要的是，避免了训练扩散模型的需要。在本文中，我们的目标是减少在扩散模型中添加引导所需的时间和计算开销，同时保持可比较的图像质量。我们在实证分析的基础上提出了一套方法，证明计算时间减少了大约三倍。 et.al.|[2312.13253](http://arxiv.org/abs/2312.13253)|null|
|**2023-12-20**|**Zero-Shot Metric Depth with a Field-of-View Conditioned Diffusion Model**|虽然单目深度估计方法在标准基准上取得了重大进展，但零样本度量深度估计仍然没有解决。挑战包括室内和室外场景的联合建模，这些场景通常表现出明显不同的RGB和深度分布，以及由于未知的相机本质而导致的深度尺度模糊。最近的工作提出了用于联合建模室内和室外场景的专用多头架构。相比之下，我们提倡一种通用的、与任务无关的扩散模型，并取得了一些进展，如对数尺度深度参数化，以实现室内和室外场景的联合建模，调节视场（FOV）来处理尺度模糊性，以及在训练期间综合增强FOV，以超越训练数据集中有限的相机本质。此外，通过使用比常见的更多样的训练混合物和有效的扩散参数化，我们的方法DMD（度量深度扩散）仅使用少量去噪步骤，就实现了零样本室内数据集的相对误差（REL）减少25%，零样本室外数据集的相关误差减少33%。有关概述，请参阅https://diffusion-vision.github.io/dmd et.al.|[2312.13252](http://arxiv.org/abs/2312.13252)|null|
|**2023-12-20**|**Diffusion Models With Learned Adaptive Noise**|扩散模型作为合成高质量图像的强大算法，已经获得了广泛的关注。这些算法的核心是扩散过程，它根据热力学启发的方程将数据映射到噪声，并会显著影响性能。一个广泛存在的假设是，扩散模型的ELBO目标对噪声过程是不变的（Kingma et al.，2021）。在这项工作中，我们消除了这一假设——我们提出了多元学习自适应噪声（MuLAN），这是一种在图像中以不同速率应用高斯噪声的学习扩散过程。我们的方法由三个组成部分组成——多元噪声调度、实例条件扩散和辅助变量——它们确保学习目标不再像以前的工作那样对噪声调度的选择是不变的。我们的工作以贝叶斯推理为基础，并将学习到的扩散过程视为一个近似的变分后验，该后验产生了更严格的边际似然下限。从经验上讲，与经典扩散相比，MuLAN在CIFAR-10和ImageNet上的密度估计方面开创了新的技术。代码位于https://github.com/s-sahoo/mulan et.al.|[2312.13236](http://arxiv.org/abs/2312.13236)|**[link](https://github.com/s-sahoo/mulan)**|
|**2023-12-20**|**A pedagogical introduction to continuously monitored quantum systems and measurement-based feedback**|在这篇手稿中，我们介绍了连续监测量子系统的教学介绍。我们首先根据碰撞模型和输入输出理论的精神，给出了Lindblad形式的马尔可夫主方程的简化推导，该方程描述了连续监测系统的无条件动力学。然后利用相同的形式来推导描述条件动力学的随机主方程。我们关注连续监测的两个最典型的例子：连续光电探测，导致具有“量子跳跃”的不连续动力学，以及连续零差测量，导致扩散动力学。然后，我们推导了反馈主方程，该方程描述了当连续测量光电流作为线性驱动哈密顿量反馈到系统时的动力学（有条件或无条件），这种模式被称为线性马尔可夫反馈。在手稿的第二部分中，我们重点研究连续可变高斯系统：我们首先给出了描述连续广义达因测量下动力学的一阶和二阶矩方程，然后我们更详细地讨论了马尔可夫和基于状态的反馈下的条件和无条件动力学。 et.al.|[2312.13214](http://arxiv.org/abs/2312.13214)|null|
|**2023-12-20**|**MoSAR: Monocular Semi-Supervised Model for Avatar Reconstruction using Differentiable Shading**|从肖像图像重建化身在多媒体中有许多应用，但仍然是一个具有挑战性的研究问题。从一张图像中提取反射率图和几何图形是不合适的：恢复几何图形是一个一对多的映射问题，反射率和光很难解开。可以在光台的受控条件下捕获精确的几何形状和反射率，但以这种方式获取大型数据集的成本很高。此外，仅使用这种类型的数据进行训练会导致野生图像的泛化能力较差。这促使MoSAR的引入，这是一种从单目图像生成3D化身的方法。我们提出了一种半监督训练方案，通过从光阶段和野外数据集学习来提高泛化能力。这是使用一种新颖的可微分着色公式实现的。我们证明，我们的方法有效地解开了固有的人脸参数，产生了可重新点亮的化身。因此，与现有的最先进的方法相比，MoSAR估计了一组更丰富的皮肤反射率图，并生成了更逼真的化身。我们还介绍了一个新的数据集，名为FFHQ UV Intrensics，这是第一个为总共10k名受试者提供按比例（漫反射、镜面反射、环境遮挡和半透明图）的内部人脸属性的公共数据集。项目网站和数据集可通过以下链接获得：https://ubisoftlaforge.github.io/character/mosar et.al.|[2312.13091](http://arxiv.org/abs/2312.13091)|null|
|**2023-12-20**|**DiffPortrait3D: Controllable Diffusion for Zero-Shot Portrait View Synthesis**|我们提出了DiffPortrait3D，这是一种条件扩散模型，能够从野生肖像中的一张照片中合成3D一致的照片逼真的新颖视图。具体来说，在给定单个RGB输入的情况下，我们的目标是合成从新颖的相机视图中呈现的看似合理但一致的面部细节，同时保留身份和面部表情。除了耗时的优化和微调外，我们的零样本方法很好地推广到任意面部肖像，具有无污染的相机视图、极端的面部表情和多样化的艺术描绘。其核心是，我们利用在大规模图像数据集上预先训练的2D扩散模型的生成先验作为我们的渲染骨干，而去噪是通过对外观和相机姿态的细致控制来指导的。为了实现这一点，我们首先将参考图像的外观上下文注入冻结的UNets的自关注层。然后利用新颖的条件控制模块来操纵渲染视图，该条件控制模块通过从同一视图观看交叉对象的条件图像来解释相机姿态。此外，我们插入了一个可训练的跨视图注意力模块来增强视图一致性，在推理过程中，通过一个新颖的3D感知噪声生成过程进一步增强了视图一致性。我们在野外和多视图基准测试中展示了最先进的定性和定量结果。 et.al.|[2312.13016](http://arxiv.org/abs/2312.13016)|null|
|**2023-12-20**|**A comparative study of analytical models of diffuse reflectance in homogeneous biological tissues: Gelatin based phantoms and Monte Carlo experiments**|通过非接触成像测量的漫反射光谱可以提取组织氧饱和度（ $StO_2$ ）和其他相关重要生理参数的信息。已经提出了三种均匀、半无限组织的分析光学反射率模型（Modified Beer-Lambert，Jacques 1999，Yudovsky 2009），但这些模型尚未直接用于组织参数提取。我们使用蒙特卡罗模拟的漫反射光谱和控制的明胶基体模将这些分析模型与测量的漫反射谱和已知的真实成分参数进行比较。尤多夫斯基模型在拟合优度和参数提取精度方面与蒙特卡洛模拟和组织模型的测量光谱相比表现最好，紧随其后的是雅克模型。在这项研究中，Yudovsky的模型看起来最稳健，但我们的结果表明，Yudofsky和Jacques模型都适用于模拟可以近似为单个、均匀、半无限平板的组织。 et.al.|[2312.12935](http://arxiv.org/abs/2312.12935)|null|
|**2023-12-20**|**On the validity of some equilibrium models for thermodiffusion**|当应用于二元溶液时，热梯度会导致浓度梯度的产生，从而导致不均匀系统。尽管人们已经知道这一现象150多年了，但其分子起源仍存在争议，而且对于能够解释浓度梯度对给定温度梯度的响应幅度的基本物理模型或理论还没有达成共识。值得注意的是，已经有一些尝试将这种非平衡、稳态的表现与这些溶液的平衡性质联系起来，例如，与自扩散系数的温度依赖性或与它们的每个组分的溶剂化自由能联系起来。在这里，我们在热泳环境和平衡条件下对含有分子大小溶质的稀溶液进行分子动力学模拟，以测试此类模型的有效性。我们表明，与基于不平衡测量的方法相比，这些方法是不充分的，并导致完全不相关的估计。至关重要的是，它们未能解释在模拟和实验中观察到的强烈质量依赖性（热力学或单粒子扩散对其不敏感）。然而，我们的结果表明，短时间分子运动的振幅和浓度梯度的振幅之间存在有趣的相关性，值得未来研究。 et.al.|[2312.12912](http://arxiv.org/abs/2312.12912)|null|

<p align=right>(<a href=#updated-on-20231221>back to top</a>)</p>

## NeRF

|Publish Date|Title|Abstract|PDF|Code|
|---|---|---|---|---|
|**2023-12-20**|**Deep Learning on 3D Neural Fields**|近年来，神经场（NFs）已成为编码各种连续信号（如图像、视频、音频和3D形状）的有效工具。当应用于3D数据时，NFs提供了一种解决方案来解决与流行的离散表示相关的碎片化和局限性。然而，鉴于神经网络本质上是神经网络，目前尚不清楚它们是否以及如何无缝集成到深度学习管道中，以解决下游任务。本文解决了这一研究问题，并介绍了nf2vec，这是一个能够在单个推理过程中为输入NF生成紧凑的潜在表示的框架。我们证明了nf2vec有效地嵌入了由输入NF表示的3D对象，并展示了如何在深度学习管道中使用由此产生的嵌入来成功地处理各种任务，同时只处理NF。我们在几个用于表示3D曲面的NFs上测试了这个框架，例如无符号/有符号距离和占用字段。此外，我们用更复杂的NFs证明了我们的方法的有效性，这些NFs包括3D对象的几何形状和外观，如神经辐射场。 et.al.|[2312.13277](http://arxiv.org/abs/2312.13277)|null|
|**2023-12-16**|**How to Train Neural Field Representations: A Comprehensive Study and Benchmark**|神经场（NeFs）最近已成为一种用于对各种模态（包括图像、形状和场景）的信号进行建模的通用方法。随后，许多工作探索了使用NeF作为下游任务的表示，例如，根据适合的NeF的参数对图像进行分类。然而，NeF超参数对其作为下游表示的质量的影响很少被理解，而且在很大程度上仍未被探索。这在一定程度上是由于拟合神经场数据集所需的大量时间造成的。在这项工作中，我们提出了 $\verb|fit-a-nef|$ ，这是一个基于JAX的库，它利用并行化来实现大规模nef数据集的快速优化，从而显著加快速度。有了这个库，我们进行了一项全面的研究，研究了不同超参数——包括初始化、网络架构和优化策略——对下游任务的NeF拟合的影响。我们的研究为如何训练NeF提供了宝贵的见解，并为优化其在下游应用中的有效性提供了指导。最后，基于所提出的库和我们的分析，我们提出了Neural Field Arena，这是一个由流行视觉数据集的神经场变体组成的基准，包括MNIST、CIFAR、ImageNet和ShapeNetv2的变体。我们的图书馆和神经领域竞技场将是开源的，以引入标准化的基准测试，并促进对神经领域的进一步研究。 et.al.|[2312.10531](http://arxiv.org/abs/2312.10531)|**[link](https://github.com/samuelepapa/fit-a-nef)**|
|**2023-12-18**|**LatentEditor: Text Driven Local Editing of 3D Scenes**|虽然神经领域在视图合成和场景重建方面取得了重大进展，但由于其对来自多视图输入的几何和纹理信息的隐式编码，编辑它们带来了巨大的挑战。在本文中，我们介绍了\textsc｛LatentEditor｝，这是一个创新的框架，旨在让用户能够使用文本提示对神经字段进行精确和本地控制的编辑。利用去噪扩散模型，我们成功地将真实世界的场景嵌入到潜在空间中，与传统方法相比，产生了更快、更具适应性的NeRF主干进行编辑。为了提高编辑精度，我们引入了一个delta分数来计算潜在空间中的2D掩模，该分数可以作为局部修改的指南，同时保留不相关的区域。我们新颖的像素级评分方法利用InstructPix2Pix（IP2P）的能力来辨别潜在空间中IP2P条件和无条件噪声预测之间的差异。然后在训练集中迭代地更新以2D掩码为条件的编辑的潜伏时间，以实现3D局部编辑。与现有的3D编辑模型相比，我们的方法实现了更快的编辑速度和卓越的输出质量，弥合了文本指令和潜在空间中高质量3D场景编辑之间的差距。我们在LLFF、IN2N、NeRFStudio和NeRFArt四个基准3D数据集上展示了我们的方法的优势。 et.al.|[2312.09313](http://arxiv.org/abs/2312.09313)|**[link](https://github.com/umarkhalidAI/LatentEditor)**|
|**2023-12-14**|**ZeroRF: Fast Sparse View 360° Reconstruction with Zero Pretraining**|我们提出了ZeroRF，这是一种新的每场景优化方法，解决了神经场表示中稀疏视图360重建的挑战。目前的突破，如神经辐射场（NeRF）已经证明了高保真度的图像合成，但难以处理稀疏的输入视图。现有的方法，如可泛化的NeRF和每场景优化方法，在数据依赖性、计算成本和跨不同场景的泛化方面面临限制。为了克服这些挑战，我们提出了ZeroRF，其关键思想是将定制的深度图像先验集成到因子分解的NeRF表示中。与传统方法不同，ZeroRF使用神经网络生成器对特征网格进行参数化，从而实现高效的稀疏视图360重建，而无需任何预训练或额外的正则化。大量实验展示了ZeroRF在质量和速度方面的多功能性和优势，在基准数据集上取得了最先进的结果。ZeroRF的意义延伸到3D内容生成和编辑的应用。项目页面：https://sarahweiii.github.io/zerorf/ et.al.|[2312.09249](http://arxiv.org/abs/2312.09249)|null|
|**2023-12-12**|**SMERF: Streamable Memory Efficient Radiance Fields for Real-Time Large-Scene Exploration**|最近的实时视图合成技术在保真度和速度上迅速进步，现代方法能够以交互式帧速率渲染接近照片级真实感的场景。与此同时，在易于光栅化的显式场景表示和基于射线行进的神经场之间出现了紧张关系，后者的最先进实例在质量上超过了前者，同时对于实时应用来说成本高得令人望而却步。在这项工作中，我们介绍了SMERF，这是一种视图合成方法，在占地面积高达3亿 $^2$、体积分辨率为3.5毫米$^3$ 的大型场景中，它实现了实时方法中最先进的精度。我们的方法建立在两个主要贡献之上：一个是分层模型划分方案，它在限制计算和内存消耗的同时增加了模型容量，另一个是蒸馏训练策略，它同时产生高保真度和内部一致性。我们的方法能够在网络浏览器中实现全六自由度（6DOF）导航，并在商品智能手机和笔记本电脑上实时渲染。大量实验表明，我们的方法在实时新视图合成方面，在标准基准上超过了当前最先进的0.78 dB，在大型场景上超过了1.78 dB，渲染帧的速度比最先进的辐射场模型快三个数量级，并在包括智能手机在内的各种商品设备上实现了实时性能。我们鼓励读者在我们的项目网站上亲自探索这些模型：https://smerf-3d.github.io. et.al.|[2312.07541](http://arxiv.org/abs/2312.07541)|null|
|**2023-12-09**|**Robo360: A 3D Omnispective Multi-Material Robotic Manipulation Dataset**|长期以来，制造能够自动化劳动密集型任务的机器人一直是计算机视觉和机器人界进步的核心动力。最近人们对利用3D算法，特别是神经领域的兴趣，导致了机器人在操作场景中的感知和物理理解方面的进步。然而，现实世界的复杂性带来了重大挑战。为了应对这些挑战，我们提出了Robo360，这是一个以机器人操作为特征的数据集，具有密集的视图覆盖范围，能够实现高质量的3D神经表示学习，以及一组具有各种物理和光学特性的不同对象，有助于各种对象操作和物理世界建模任务的研究。我们使用现有的动态NeRF来确认我们的数据集的有效性，并评估其在学习多视图策略方面的潜力。我们希望Robo360能够在理解3D物理世界和机器人控制的交叉点上开辟新的研究方向。 et.al.|[2312.06686](http://arxiv.org/abs/2312.06686)|null|
|**2023-12-11**|**Representing stimulus motion with waves in adaptive neural fields**|神经活动的行波在皮层网络中自发出现，并对刺激做出反应。波的时空结构可以指示它们编码的信息以及维持它们的生理过程。在这里，我们研究了作为视觉运动处理模型的自适应神经场中出现的行波的刺激响应关系。神经场方程将皮层组织的活动建模为连续的可兴奋介质，自适应过程提供负反馈，产生局部活动模式。在我们的模型中，突触连接由一个积分核来描述，该积分核由于依赖于活动的突触抑制而动态减弱，导致边缘稳定的行进前沿（具有衰减的后部）或固定速度的脉冲。我们的分析量化了弱刺激如何随着时间的推移改变这些波的相对位置，其特征是我们扰动地获得的波响应函数。持续和连续可见的刺激模拟移动的视觉对象。在视觉空间中跳跃的间歇性闪光可以产生流畅的视觉运动体验。我们的理论和数值模拟很好地描述了波对两种运动刺激的夹带，提供了视觉运动感知的机制描述。 et.al.|[2312.06100](http://arxiv.org/abs/2312.06100)|null|
|**2023-12-10**|**Accurate Differential Operators for Hybrid Neural Fields**|神经场已广泛应用于从形状表示到神经渲染以及求解偏微分方程（PDE）的各个领域。随着混合神经场表示的出现，如利用小MLP和显式表示的即时NGP，这些模型训练迅速，可以适应大型场景。然而，在渲染和模拟等许多应用中，混合神经场可能会导致明显且不合理的伪影。这是因为它们不能产生这些下游应用所需的精确的空间导数。在这项工作中，我们提出了两种规避这些挑战的方法。我们的第一种方法是一种事后算子，它使用局部多项式拟合从预先训练的混合神经场中获得更准确的导数。此外，我们还提出了一种自监督微调方法，该方法在保留初始信号的同时，对神经场进行细化，以直接产生准确的导数。我们展示了我们的方法在渲染、碰撞模拟和求解偏微分方程中的应用。我们观察到，使用我们的方法可以产生更准确的导数，减少伪影，并在下游应用中实现更准确的模拟。 et.al.|[2312.05984](http://arxiv.org/abs/2312.05984)|null|
|**2023-12-11**|**Nuvo: Neural UV Mapping for Unruly 3D Representations**|现有的UV映射算法被设计为在性能良好的网格上操作，而不是由最先进的3D重建和生成技术产生的几何表示。因此，将这些方法应用于由神经辐射场和相关技术（或从这些场三角化的网格）恢复的体积密度会导致纹理图谱过于分散，无法用于视图合成或外观编辑等任务。我们提出了一种UV映射方法，旨在对通过3D重建和生成技术产生的几何体进行操作。我们的方法Nuvo不是计算在网格顶点上定义的映射，而是使用神经场来表示连续的UV映射，并将其优化为仅针对一组可见点（即仅影响场景外观的点）的有效且性能良好的映射。我们展示了我们的模型对不良几何体带来的挑战是稳健的，并且它生成了可以表示详细外观的可编辑UV映射。 et.al.|[2312.05283](http://arxiv.org/abs/2312.05283)|null|
|**2023-12-08**|**Dynamic LiDAR Re-simulation using Compositional Neural Fields**|我们介绍了DyNFL，这是一种新的基于神经场的方法，用于动态驾驶场景中激光雷达扫描的高保真度重新模拟。DyNFL处理来自动态环境的激光雷达测量，并伴随着移动物体的边界框，以构建可编辑的神经场。该字段包括单独重建的静态背景和动态对象，允许用户在重新模拟的场景中修改视点、调整对象位置以及无缝添加或删除对象。我们方法的一个关键创新是神经场合成技术，该技术通过光线下降测试有效地集成了来自各种场景的重建神经资产，考虑到了遮挡和透明表面。我们对合成和真实世界环境的评估表明，\ShortName大大改进了基于激光雷达扫描的动态场景模拟，提供了物理保真度和灵活编辑功能的组合。 et.al.|[2312.05247](http://arxiv.org/abs/2312.05247)|null|

<p align=right>(<a href=#updated-on-20231221>back to top</a>)</p>

[contributors-shield]: https://img.shields.io/github/contributors/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[contributors-url]: https://github.com/Vincentqyw/cv-arxiv-daily/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[forks-url]: https://github.com/Vincentqyw/cv-arxiv-daily/network/members
[stars-shield]: https://img.shields.io/github/stars/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[stars-url]: https://github.com/Vincentqyw/cv-arxiv-daily/stargazers
[issues-shield]: https://img.shields.io/github/issues/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[issues-url]: https://github.com/Vincentqyw/cv-arxiv-daily/issues

