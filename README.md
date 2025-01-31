[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]

## Updated on 2025.01.31
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
|**2025-01-28**|**LinPrim: Linear Primitives for Differentiable Volumetric Rendering**|体绘制已成为现代新型视图合成方法的核心，这些方法使用可微绘制直接从观察到的视图中优化3D场景表示。虽然最近的许多作品都建立在NeRF或3D高斯模型上，但我们探索了一种替代的体积场景表示方法。更具体地说，我们引入了两种基于线性图元八面体和四面体的新场景表示，这两种图元都定义了由三角形面界定的均匀体积。该公式与标准的基于网格的工具自然对齐，最大限度地减少了下游应用的开销。为了优化这些图元，我们提出了一种在GPU上高效运行的可微分光栅化器，允许端到端的基于梯度的优化，同时保持实时渲染能力。通过在真实世界数据集上的实验，我们展示了与最先进的体积方法相当的性能，同时需要更少的图元来实现类似的重建保真度。我们的研究结果为体绘制的几何形状提供了见解，并表明采用显式多面体可以扩展场景表示的设计空间。 et.al.|[2501.16312](http://arxiv.org/abs/2501.16312)|null|
|**2025-01-25**|**HuGDiffusion: Generalizable Single-Image Human Rendering via 3D Gaussian Diffusion**|我们提出了HuGDiffusion，这是一种可推广的3D高斯飞溅（3DGS）学习管道，用于从单视图输入图像中实现人物角色的新颖视图合成（NVS）。现有的方法通常需要单目视频或校准的多视图图像作为输入，在具有任意和/或未知相机姿态的现实世界场景中，其适用性可能会减弱。在本文中，我们的目标是通过基于扩散的框架生成3DGS属性集，该框架以从单幅图像中提取的人类先验为条件。具体来说，我们从精心整合的以人为中心的特征提取过程开始，以推断出信息丰富的条件信号。基于我们的经验观察，联合学习整个3DGS属性具有优化挑战性，我们设计了一种多阶段生成策略来获得不同类型的3DGS属性。为了简化训练过程，我们研究了将代理地面真值3D高斯属性构建为高质量的属性级监督信号。通过广泛的实验，我们的HuGDiffusion显示出比最先进的方法有显著的性能改进。我们的代码将公开。 et.al.|[2501.15008](http://arxiv.org/abs/2501.15008)|null|
|**2025-01-24**|**CheapNVS: Real-Time On-Device Narrow-Baseline Novel View Synthesis**|单视图新视图合成（NVS）因其不适定性而成为一个臭名昭著的问题，并且通常需要大量计算昂贵的方法来产生有形的结果。在本文中，我们提出了CheapNVS：一种基于多级训练的新颖、高效的多编码器/解码器设计的窄基线单视图NVS的完全端到端方法。CheapNVS首先使用轻量级的可学习模块来近似费力的3D图像扭曲，这些模块以目标视图的相机姿态嵌入为条件，然后并行地对遮挡区域进行修复，以实现显著的性能提升。一旦在Open Images数据集的一个子集上进行了训练，CheapNVS的性能就超过了最先进的技术，尽管速度快了10倍，内存消耗减少了6%。此外，CheapNVS在移动设备上实时运行舒适，在三星Tab 9+上达到30 FPS以上。 et.al.|[2501.14533](http://arxiv.org/abs/2501.14533)|null|
|**2025-01-27**|**3DGS $^2$ : Near Second-order Converging 3D Gaussian Splatting**|3D高斯散斑（3DGS）已成为新颖视图合成和3D重建的主流解决方案。通过使用高斯核的集合对3D场景进行显式编码，3DGS以卓越的效率实现了高质量的渲染。作为一种基于学习的方法，3DGS训练采用了标准的随机梯度下降（SGD）方法，该方法最多提供线性收敛。因此，即使在GPU加速的情况下，训练通常也需要几十分钟。本文介绍了一种用于3DGS的（近）二阶收敛训练算法，利用其独特的特性。我们的方法受到两个关键观察结果的启发。首先，高斯核的属性独立地影响图像空间损失，这支持孤立和局部优化算法。我们通过在单个内核属性级别分割优化，为每个参数组解析构建小尺寸牛顿系统，并在GPU线程上高效求解这些系统来利用这一点。这实现了每个训练图像的牛顿式收敛，而不依赖于全局Hessian。其次，核在输入图像之间表现出稀疏和结构化的耦合。这一特性使我们能够有效地利用空间信息来减轻随机训练过程中的超调。我们的方法比基于标准GPU的3DGS训练更快地收敛顺序，需要的迭代次数比基于SGD的3DGS重建少10多倍，同时保持或超过重建的质量。 et.al.|[2501.13975](http://arxiv.org/abs/2501.13975)|null|
|**2025-01-22**|**GS-LiDAR: Generating Realistic LiDAR Point Clouds with Panoramic Gaussian Splatting**|激光雷达新视图合成（NVS）已成为激光雷达模拟中的一项新任务，它从新的视角提供有价值的模拟点云数据，以帮助自动驾驶系统。然而，现有的LiDAR NVS方法通常依赖于神经辐射场（NeRF）作为其3D表示，这在训练和渲染方面都会产生巨大的计算成本。此外，NeRF及其变体是为对称场景设计的，因此不适合驾驶场景。为了应对这些挑战，我们提出了GS LiDAR，这是一种用于生成具有全景高斯散射的逼真LiDAR点云的新框架。我们的方法采用具有周期性振动特性的二维高斯基元，允许在驾驶场景中对静态和动态元素进行精确的几何重建。我们进一步介绍了一种新的全景渲染技术，该技术在全景LiDAR监控的引导下，具有显式的光线平面相交。通过将强度和光线滴球面谐波（SH）系数合并到高斯基元中，我们增强了渲染点云的真实感。在KITTI-360和nuScenes上的大量实验证明了我们的方法在定量指标、视觉质量以及训练和渲染效率方面的优越性。 et.al.|[2501.13971](http://arxiv.org/abs/2501.13971)|**[link](https://github.com/fudan-zvg/gs-lidar)**|
|**2025-01-23**|**GoDe: Gaussians on Demand for Progressive Level of Detail and Scalable Compression**|3D高斯散斑通过用高斯混合表示场景并利用可微光栅化来增强新颖视图合成中的实时性能。然而，它通常需要大的存储容量和高VRAM，要求设计有效的修剪和压缩技术。现有方法虽然在某些情况下有效，但在可扩展性方面存在困难，无法根据计算能力或带宽等关键因素调整模型，需要在不同配置下重新训练模型。在这项工作中，我们提出了一种新颖的、与模型无关的技术，将高斯分布组织成几个层次，实现了渐进的细节层次（LoD）策略。这种方法与最近的3DGS压缩方法相结合，允许单个模型在多个压缩比上即时扩展，与单个不可扩展模型相比，对质量的影响最小或没有影响，也不需要重新训练。我们在典型的数据集和基准上验证了我们的方法，展示了低失真和在可扩展性和适应性方面的显著收益。 et.al.|[2501.13558](http://arxiv.org/abs/2501.13558)|null|
|**2025-01-22**|**DWTNeRF: Boosting Few-shot Neural Radiance Fields via Discrete Wavelet Transform**|神经辐射场（NeRF）在新颖的视图合成和3D场景表示方面取得了卓越的性能，但其实际应用受到收敛缓慢和依赖密集训练视图的阻碍。为此，我们提出了DWTNeRF，这是一个基于Instant NGP快速训练哈希编码的统一框架。它与为少镜头NeRF设计的正则化项相结合，后者在稀疏训练视图上运行。我们的DWTNeRF包括一种新颖的离散小波损耗，允许在训练目标中直接对低频进行显式优先级排序，从而减少早期训练阶段少数镜头NeRF对高频的过拟合。我们还引入了一种基于模型的方法，该方法基于多头注意力，与基于INGP的模型兼容，这些模型对架构变化很敏感。在3-shot LLFF基准测试中，DWTNeRF的PSNR、SSIM和LPIPS分别比Vanilla NeRF高出15.07%、24.45%和36.30%。我们的方法鼓励重新思考基于INGP模型的当前少镜头方法。 et.al.|[2501.12637](http://arxiv.org/abs/2501.12637)|null|
|**2025-01-22**|**HAC++: Towards 100X Compression of 3D Gaussian Splatting**|3D高斯散斑（3DGS）已成为一种有前景的新型视图合成框架，具有快速渲染速度和高保真度。然而，大量的高斯分布及其相关属性需要有效的压缩技术。然而，高斯点云（或我们论文中的锚点）的稀疏性和无组织性给压缩带来了挑战。为了实现紧凑的大小，我们提出了HAC++，它利用了无组织锚点和结构化哈希网格之间的关系，利用它们的互信息进行上下文建模。此外，HAC++捕获锚点内的上下文关系，以进一步提高压缩性能。为了促进熵编码，我们利用高斯分布来精确估计每个量化属性的概率，其中提出了一种自适应量化模块来实现这些属性的高精度量化，以提高保真度恢复。此外，我们采用了一种自适应掩蔽策略来消除无效的高斯分布和锚点。总体而言，与vanilla 3DGS相比，HAC++在所有数据集上平均时实现了超过100倍的显著尺寸减小，同时提高了保真度。与脚手架GS相比，它还可以减少20倍以上的尺寸。我们的代码可在https://github.com/YihangChen-ee/HAC-plus. et.al.|[2501.12255](http://arxiv.org/abs/2501.12255)|**[link](https://github.com/yihangchen-ee/hac-plus)**|
|**2025-01-21**|**Survey on Monocular Metric Depth Estimation**|单目深度估计（MDE）是一项基本的计算机视觉任务，支撑着空间理解、3D重建和自动驾驶等应用。虽然基于深度学习的MDE方法可以从单个图像中预测相对深度，但它们缺乏度量尺度信息通常会导致尺度不一致，限制了它们在视觉SLAM、3D重建和新颖视图合成等下游任务中的实用性。单目度量深度估计（MMDE）通过实现精确的场景级深度推断来解决这些挑战。MMDE提高了深度一致性，增强了顺序任务的稳定性，简化了与下游应用程序的集成，并拓宽了实际用例。本文对深度估计技术进行了全面的回顾，重点介绍了从基于几何的方法到最先进的深度学习方法的演变。它强调了标度不可知方法的进步，这对于实现零样本泛化作为MMDE的基础能力至关重要。探讨了零样本MMDE研究的最新进展，重点讨论了模型泛化和场景边界细节丢失等挑战。解决这些问题的创新策略包括无标签数据增强、图像修补、架构优化和生成技术。详细分析后，这些进步表明了对克服现有局限性的重大贡献。最后，本文综合了零样本MMDE的最新发展，确定了尚未解决的挑战，并概述了未来的研究方向。通过提供清晰的路线图和前沿的见解，这项工作旨在加深对MMDE的理解，激发新的应用，并推动技术创新。 et.al.|[2501.11841](http://arxiv.org/abs/2501.11841)|null|
|**2025-01-20**|**See In Detail: Enhancing Sparse-view 3D Gaussian Splatting with Local Depth and Semantic Regularization**|3D高斯散斑（3DGS）在新颖的视图合成中表现出了显著的性能。然而，当输入视图稀疏时，其渲染质量会下降，导致内容失真和细节减少。这种限制阻碍了它的实际应用。为了解决这个问题，我们提出了一种稀疏视图3DGS方法。鉴于稀疏视图渲染固有的不适定性，整合先验信息至关重要。我们提出了一种语义正则化技术，使用从预训练的DINO-ViT模型中提取的特征来确保多视图语义的一致性。此外，我们提出了局部深度正则化，它约束深度值以提高对看不见的视图的泛化能力。我们的方法优于最先进的新颖视图合成方法，在LLFF数据集上实现了高达0.4dB的PSNR改善，同时减少了失真并提高了视觉质量。 et.al.|[2501.11508](http://arxiv.org/abs/2501.11508)|null|

<p align=right>(<a href=#updated-on-20250131>back to top</a>)</p>

## 3D Reconstruction

|Publish Date|Title|Abstract|PDF|Code|
|---|---|---|---|---|
|**2025-01-30**|**Efficient Interactive 3D Multi-Object Removal**|对象去除对于3D场景理解具有重要意义，对于内容过滤和场景编辑中的应用至关重要。目前的主流方法主要侧重于删除单个对象，少数方法专门用于删除整个区域或某一类别的所有对象。然而，他们面临着现实世界应用程序粒度和灵活性不足的挑战，用户要求在定义的区域内对对象进行量身定制的切除和保存。此外，目前的大多数方法在处理多视图修复时都需要各种先验，这很耗时。为了解决这些局限性，我们提出了一种高效且用户友好的3D多对象删除管道，使用户能够灵活选择区域并定义要删除或保存的对象。具体来说，为了确保对象在多个视图之间的一致性和对应性，我们提出了一种新的掩模匹配和细化模块，该模块将基于单应性的扭曲与高置信度锚点相结合，用于分割。通过利用IoU关节形状上下文距离损失，我们提高了扭曲掩模的准确性，并改进了后续的修复过程。考虑到目前3D多目标去除的不成熟，我们提供了一个新的评估数据集来填补发展空白。实验结果表明，我们的方法显著降低了计算成本，处理速度比最先进的方法快80%以上，同时保持了同等或更高的重建质量。 et.al.|[2501.17636](http://arxiv.org/abs/2501.17636)|null|
|**2025-01-28**|**Consistency Diffusion Models for Single-Image 3D Reconstruction with Priors**|本文深入研究了从单幅图像重建三维点云的方法。我们的目标是开发一致性扩散模型，在贝叶斯框架中探索协同的2D和3D先验，以确保重建过程的高度一致性，这是该领域具有挑战性但至关重要的要求。具体来说，我们在扩散模型下引入了一个开创性的培训框架，该框架带来了两个关键创新。首先，我们将来自初始3D点云的3D结构先验转换为有界项，以增加变分贝叶斯框架中的证据，利用这些鲁棒的内在先验来严格控制扩散训练过程，并增强重建的一致性。其次，我们从单个输入图像中提取并合并2D先验，将其投影到3D点云上，以丰富扩散训练的指导。我们的框架不仅避开了在训练过程中直接施加额外约束可能引起的潜在模型学习转变，而且将2D先验精确地转换到3D域中。广泛的实验评估表明，我们的方法在合成和现实世界的数据集中都设定了新的基准。代码包含在提交中。 et.al.|[2501.16737](http://arxiv.org/abs/2501.16737)|null|
|**2025-01-27**|**3D Reconstruction of non-visible surfaces of objects from a Single Depth View -- Comparative Study**|场景和对象重建是机器人技术中的一个重要问题，特别是在规划无碰撞轨迹或对象操纵方面。本文比较了从单个RGB-D相机视图重建物体表面不可见部分的两种策略。第一种方法名为DeepSDF，用于预测3D空间中给定点到对象曲面的有符号距离变换。第二种方法名为MirrorNet，通过从观察对象的另一侧生成图像来重建被遮挡对象的部分。对ShapeNet数据集中的对象进行的实验表明，依赖于视图的MirrorNet在大多数类别中速度更快，重建误差更小。 et.al.|[2501.16101](http://arxiv.org/abs/2501.16101)|null|
|**2025-01-27**|**MatCLIP: Light- and Shape-Insensitive Assignment of PBR Material Models**|为3D模型分配逼真的材质仍然是计算机图形学中的一个重大挑战。我们提出了MatCLIP，这是一种提取基于物理的渲染（PBR）材料的形状和光照不敏感描述符的新方法，可以根据图像（如潜在扩散模型（LDM）或照片的输出）为3D对象分配合理的纹理。将PBR材质与静态图像相匹配是具有挑战性的，因为PBR表示可以在不同的视角、形状和光照条件下捕捉材质的动态外观。通过在不同形状和照明的材质渲染上扩展基于Alpha CLIP的模型，并对PBR材质的多个查看条件进行编码，我们的方法生成了描述符，将PBR表示的领域与照片或渲染（包括LDM输出）联系起来。这使得材料分配保持一致，而不需要明确了解物体不同部分之间的材料关系。MatCLIP实现了76.6%的前1名分类准确率，在公开数据集上比PhotoShape和MatAtlas等最先进的方法高出15个百分点以上。我们的方法可用于为ShapeNet、3DCoMPaT++和Objaverse等3D形状数据集构建材质分配。所有代码和数据都将被发布。 et.al.|[2501.15981](http://arxiv.org/abs/2501.15981)|null|
|**2025-01-26**|**Dfilled: Repurposing Edge-Enhancing Diffusion for Guided DSM Void Filling**|数字表面模型（DSM）对于在地理空间分析中准确表示地球地形至关重要。DSM捕捉自然和人为特征的详细高程，这对于城市规划、植被研究和3D重建等应用至关重要。然而，由于遮挡、阴影和低信号区域，从立体卫星图像中导出的DSM通常包含空白或缺失的数据。之前的研究主要集中在数字高程模型（DEM）和数字地形模型（DTM）的空隙填充上，采用了逆距离加权（IDW）、克里金和样条插值等方法。虽然这些方法对更简单的地形有效，但它们往往无法处理DSM中存在的复杂结构。为了克服这些局限性，我们引入了Dfilled，这是一种引导式DSM空隙填充方法，通过边缘增强扩散利用光学遥感图像。Dfilled将最初为超分辨率任务设计的深度各向异性扩散模型重新用于输入DSM。此外，我们利用Perlin噪声来创建修复掩模，以模仿DSMs中的自然空隙模式。实验评估表明，Dfilled在DSM空隙填充任务中超越了传统的插值方法和深度学习方法。定量和定性评估都强调了该方法管理复杂特征并提供准确、视觉连贯的结果的能力。 et.al.|[2501.15440](http://arxiv.org/abs/2501.15440)|null|
|**2025-01-28**|**Acquiring Submillimeter-Accurate Multi-Task Vision Datasets for Computer-Assisted Orthopedic Surgery**|计算机视觉的进步，特别是基于光学图像的3D重建和特征匹配，使无标记手术导航和手术数字化等应用成为可能。然而，由于缺乏具有3D地面实况的合适数据集，它们的发展受到了阻碍。这项工作探索了一种生成真实准确的离体数据集的方法，该数据集专为开放式骨科手术中的3D重建和特征匹配而定制。为了开发适用于手术的基于视觉的3D重建和匹配方法，需要一组姿态图像和场景的精确配准的地面真实表面网格。我们提出了一个由三个核心步骤组成的框架，并比较了每个步骤的不同方法：3D扫描、一组高分辨率RGB图像的视点校准，以及一种基于光学的场景配准方法。我们使用猪脊柱在真实手术室条件下进行离体脊柱侧凸手术，评估该框架的每一步。相对于3D地面真值，实现了0.35mm的平均3D欧几里德误差。所提出的方法可以产生亚毫米级的精确3D地面实况和空间分辨率为0.1毫米的手术图像。这为获取未来用于高精度应用的手术数据集打开了大门。 et.al.|[2501.15371](http://arxiv.org/abs/2501.15371)|**[link](https://github.com/emmamost26/CamSceneRegistration)**|
|**2025-01-24**|**Light3R-SfM: Towards Feed-forward Structure-from-Motion**|我们提出了Light3R SfM，这是一个前馈的端到端可学习框架，用于从无约束图像集合中高效地实现大规模运动结构（SfM）。与依赖于昂贵的匹配和全局优化来实现精确3D重建的现有SfM解决方案不同，Light3R SfM通过一种新颖的潜在全局对齐模块解决了这一局限性。该模块用可学习的注意力机制取代了传统的全局优化，有效地捕获了图像中的多视图约束，以实现稳健和精确的相机姿态估计。Light3R SfM通过检索分数引导的最短路径树构建稀疏场景图，与朴素方法相比，大大减少了内存使用和计算开销。大量实验表明，Light3R SfM在显著减少运行时间的同时实现了具有竞争力的精度，使其成为具有运行时间约束的现实世界应用程序中的3D重建任务的理想选择。这项工作开创了一种数据驱动的前馈SfM方法，为在野外进行可扩展、准确和高效的3D重建铺平了道路。 et.al.|[2501.14914](http://arxiv.org/abs/2501.14914)|null|
|**2025-01-24**|**Glissando-Net: Deep sinGLe vIew category level poSe eStimation ANd 3D recOnstruction**|我们提出了一个名为Glissando Net的深度学习模型，可以从单个RGB图像中同时估计物体的姿态并在类别级别重建物体的3D形状。以前的工作主要集中在估计姿势（通常在实例级别）或重建形状，但不是两者兼而有之。Glissando Net由两个联合训练的自动编码器组成，一个用于RGB图像，另一个用于点云。我们在Glissando Net中采用了两个关键的设计选择，以在给定单个RGB图像作为输入的情况下，更准确地预测物体的3D形状和姿态。首先，我们用来自图像解码器的变换特征图来增强点云编码器和解码器的特征图，从而在训练和预测中实现有效的2D-3D交互。其次，我们在解码器阶段预测对象的3D形状和姿态。这样，我们可以更好地利用仅在训练阶段呈现的3D点云中的信息来训练网络，以进行更准确的预测。我们联合训练RGB和点云数据的两个编码器-解码器，学习如何在推理过程中将潜在特征传递给点云解码器。在测试中，3D点云的编码器被丢弃。Glissando Net的设计灵感来自codeSLAM。与以场景三维重建为目标的codeSLAM不同，我们专注于物体的姿态估计和形状重建，直接预测物体的姿态和姿态不变的三维重建，而不需要代码优化步骤。广泛的实验，包括消融研究和与竞争方法的比较，证明了我们提出的方法的有效性，并与最先进的方法进行了比较。 et.al.|[2501.14896](http://arxiv.org/abs/2501.14896)|null|
|**2025-01-24**|**Towards Unified Structured Light Optimization**|结构光（SL）3D重建捕捉物体的精确表面形状，提供工业检测和机器人视觉系统所必需的高精度3D数据。然而，目前在SL 3D重建中优化投影模式的研究面临两个主要局限性：每个场景都需要单独训练校准参数，优化仅限于特定类型的SL，这限制了它们的应用范围。为了解决这些局限性，我们提出了一个统一的SL优化框架，适用于不同的照明条件、对象类型和不同类型的SL。我们的框架仅使用单个投影图像即可快速确定最佳投影模式。主要贡献包括一种针对投影仪的新型全局匹配方法，该方法仅使用一个投影图像即可实现精确的投影仪-相机对准，以及一种具有光度调整模块的新投影补偿模型，以减少色域外裁剪产生的伪影。实验结果表明，我们的方法在各种对象、SL模式和光照条件下实现了卓越的解码精度，明显优于以前的方法。 et.al.|[2501.14659](http://arxiv.org/abs/2501.14659)|null|
|**2025-01-24**|**Trick-GS: A Balanced Bag of Tricks for Efficient Gaussian Splatting**|高斯溅射（GS）用于3D重建因其快速训练、推理速度和高质量重建而变得非常流行。然而，基于GS的重建通常由数百万高斯人组成，这使得它们很难在智能手机等计算受限的设备上使用。本文首先对高效GS方法的进展进行了原则性分析。然后，我们提出了Trick GS，它是几种策略的精心组合，包括（1）具有分辨率、噪声和高斯尺度的渐进式训练，（2）学习根据基元和SH带的重要性修剪和屏蔽基元和SH-带，以及（3）加速GS训练框架。Trick GS向资源受限的GS迈出了一大步，其中更快的运行时间、更小更快的模型收敛是最重要的。我们在三个数据集上的结果表明，与普通GS相比，Trick GS的训练速度提高了2倍，磁盘大小减小了40倍，渲染速度提高了两倍，同时具有相当的准确性。 et.al.|[2501.14534](http://arxiv.org/abs/2501.14534)|null|

<p align=right>(<a href=#updated-on-20250131>back to top</a>)</p>

## Diffusion

|Publish Date|Title|Abstract|PDF|Code|
|---|---|---|---|---|
|**2025-01-29**|**Planetesimal formation in a pressure bump induced by infall**|星际物质的注入是原行星盘中压力颠簸的潜在非行星起源。虽然其他机制产生的压力凸起已被数值证明可以促进行星形成，但流入引起的压力凸起的影响仍未得到探索。我们的目标是从亚微米大小的尘埃颗粒开始，研究在撞击诱导的压力碰撞中形成星子的可能性，并确定最有利于触发这一过程的条件。我们开发了一个数值模型，该模型集成了轴对称入流、尘埃漂移和尘埃凝结，以及通过流不稳定性形成的星子。我们的参数空间包括气体粘度、粉尘破碎速度、初始盘质量、特征盘半径、入流速率和持续时间，以及入流区域的位置和宽度。由入流引起的压力冲击可以从入流材料和外盘捕获灰尘，促进灰尘生长。局部增强的尘气比引发了流动不稳定，在中心入流位置内形成了一个星子带，直到粘性气体扩散使压力凸起变得平滑。一条巨大的窄流注落入一个低粘度、低质量、空间延伸的含有高碎裂速度尘埃的圆盘上，有利于星宿形成。这种配置提高了压块内侧灰尘的向外漂移速度，同时也确保了压块的持久性。即使落入的物质仅由气体组成，也可能发生行星体形成。由撞击引起的压力冲击是尘埃生长和星子形成的有利场所，这种机制不需要预先存在的大质量行星来产生冲击。 et.al.|[2501.17857](http://arxiv.org/abs/2501.17857)|null|
|**2025-01-29**|**Langevin Soft Actor-Critic: Efficient Exploration through Uncertainty-Driven Critic Learning**|现有的行动者批评算法在连续控制强化学习（RL）任务中很受欢迎，但由于缺乏有原则的探索机制，样本效率很低。受Thompson采样在RL高效探索中的成功启发，我们提出了一种新的无模型RL算法Langevin Soft Actor Critic（LSAC），该算法通过不确定性估计优先于策略优化来增强批评者学习。LSAC采用了三项关键创新：通过基于分布朗之万蒙特卡罗（LMC）的 $Q$更新进行近似汤普森采样，并行回火以探索$Q$函数后验的多种模式，以及用$Q$ 动作梯度正则化的扩散合成状态动作样本。我们广泛的实验表明，对于连续控制任务，LSAC的性能优于或匹配主流无模型RL算法的性能。值得注意的是，LSAC标志着基于LMC的Thompson采样在具有连续动作空间的连续控制任务中的首次成功应用。 et.al.|[2501.17827](http://arxiv.org/abs/2501.17827)|null|
|**2025-01-29**|**VICCA: Visual Interpretation and Comprehension of Chest X-ray Anomalies in Generated Report Without Human Feedback**|随着人工智能（AI）在医疗保健领域变得越来越重要，对可解释和值得信赖的模型的需求至关重要。目前的胸部X射线（CXR）报告生成系统通常缺乏在没有专家监督的情况下验证输出的机制，这引发了人们对可靠性和可解释性的担忧。为了应对这些挑战，我们提出了一种新的多模式框架，旨在提高人工智能生成的医疗报告的语义对齐和定位准确性。我们的框架集成了两个关键模块：短语基础模型，它根据文本提示识别和定位CXR图像中的病理，以及文本到图像扩散模块，它根据提示生成合成的CXR图像，同时保持解剖保真度。通过比较原始图像和生成图像之间的特征，我们引入了一个双重评分系统：一个评分量化定位准确性，另一个评分评估语义一致性。这种方法明显优于现有方法，在病理定位和文本到图像对齐方面取得了最先进的结果。将短语基础与扩散模型相结合，再加上双重评分评估系统，为验证报告质量提供了一个强大的机制，为医学成像中更值得信赖和透明的人工智能铺平了道路。 et.al.|[2501.17726](http://arxiv.org/abs/2501.17726)|null|
|**2025-01-29**|**Enhanced dissipation by advection and applications to PDEs**|这项调查简要而全面地概述了增强耗散现象，从平流和扩散之间相互作用的物理原理无缝过渡到其严格的数学公式和分析。讨论从增强耗散的标准理论开始，突出了关键机制和结果，并进展到其在Cahn-Hilliard和Kuramoto-Sivashinsky方程等显著非线性偏微分方程中的应用。 et.al.|[2501.17695](http://arxiv.org/abs/2501.17695)|null|
|**2025-01-29**|**Distinguished Quantized Guidance for Diffusion-based Sequence Recommendation**|扩散模型（DM）因其强大的数据分布建模能力和生成高质量项目的能力，已成为顺序推荐的有前景的方法。现有的工作通常会给下一个项目添加噪声，并在用户交互序列的指导下逐步对其进行去噪，生成与用户兴趣紧密一致的项目。然而，我们确定了这一范式中的两个关键问题。首先，序列在长度和内容上通常是异构的，由于随机用户行为而表现出噪声。使用这样的序列作为指导可能会阻碍DM准确理解用户兴趣。其次，DM容易产生数据偏差，往往只生成主导训练数据集的热门项目，因此无法满足不同用户的个性化需求。为了解决这些问题，我们提出了基于扩散的序列推荐的可分辨量化指导（DiQDiff），旨在提取稳健的指导来理解用户兴趣，并在DM中为个性化用户兴趣生成可分辨的项目。为了提取稳健的指导，DiQDiff引入了语义向量量化（SVQ），使用码本将序列量化为语义向量（例如协作信号和类别兴趣），这可以丰富指导，更好地理解用户兴趣。为了生成可区分的项目，DiQDiff通过对比差异最大化（CDM）对生成进行个性化，CDM使用对比损失最大化去噪轨迹之间的距离，以防止对不同用户的有偏差生成。进行了广泛的实验，将DiQDiff与四个广泛使用的数据集上的多个基线模型进行比较。DiQDiff相对于领先方法的卓越推荐性能证明了其在连续推荐任务中的有效性。 et.al.|[2501.17670](http://arxiv.org/abs/2501.17670)|null|
|**2025-01-29**|**Spinal study of a population model for colonial species with interactions and environmental noise**|我们介绍并研究了通过裂变或碎裂繁殖的群体物种动力学的随机模型。裂变率取决于种群中菌落的相对大小，菌落的生长速度受到内在随机性和环境随机性的影响。因此，我们的设置捕捉到了外部噪声的影响，将所有菌落的性状动态联系起来。特别是，我们研究了这种相关性的强度对殖民地之间资源分配的影响。然后，我们将该模型扩展到一大类具有相互作用的结构化分支过程，其中粒子类型根据扩散而演变。分枝率和死亡率是整个种群的一般函数。在这个框架中，我们推导出了一个 $\psi$ -脊椎结构和一个多对一公式，扩展了之前关于相互作用分支过程的工作。利用这种脊柱结构，我们还提出了一种替代的模拟方法，并说明了它在群体模型上的有效性。我们提出的扩展框架可以模拟各种具有相互作用、个体和环境噪声的生态系统。 et.al.|[2501.17608](http://arxiv.org/abs/2501.17608)|null|
|**2025-01-29**|**Intermittent molecular motion and first passage statistics for the NMR relaxation of confined water**|限制在纳米多孔介质中的流体的结构和动力学不同于块体中的流体，可以使用核磁共振弛豫测量来探测。我们在这里使用狭缝纳米孔中水的原子分子动力学模拟表明，具有不同表面相互作用和约束强度的NMR弛豫速率R1的行为可以从吸附表面层和本体区域之间的流体分子交换统计数据中估算出来，分子在本体区域经历间歇动力学。我们采用首次返回通道时间计算来量化分子交换统计数据，从而将受限流体的微观参数（如吸附时间、孔径和扩散系数）与NMR弛豫速率联系起来。这种方法允许仅使用统计力学的概念来预测和解释界面处流体的分子弛豫，并且可以推广到封闭和开放的几何形状。 et.al.|[2501.17596](http://arxiv.org/abs/2501.17596)|null|
|**2025-01-29**|**On the Singular Control of a Diffusion and Its Running Infimum or Supremum**|我们研究了一类一维扩散 $X$的奇异随机控制问题，其中要优化的性能标准明确取决于受控过程的运行下确界$I$（或上确界$S$）。我们引入了两个与哈密顿-雅可比-贝尔曼方程一致的新型积分算子，用于求解由此产生的二维奇异控制问题。第一个算子涉及积分，其中积分器是二维过程$（X，I）$或$（X、S）$ 的控制过程；第二个算子涉及积分，其中积分器是正在运行的下确界或上确界过程本身。使用这些定义，我们证明了涉及二维状态相关运行成本、控制过程成本、增加运行下确界（或上确界）成本和退出时间的问题的一般验证定理。最后，我们应用我们的结果来显式地解决一个最优股息问题，其中经理的时间偏好取决于公司历史上最差的业绩。 et.al.|[2501.17577](http://arxiv.org/abs/2501.17577)|null|
|**2025-01-29**|**Trustworthy image-to-image translation: evaluating uncertainty calibration in unpaired training scenarios**|乳腺X线筛查是检测癌症的有效方法，有利于早期诊断。然而，目前手动检查图像的需求给医疗系统带来了沉重的负担，激发了人们对自动化诊断协议的渴望。基于深度神经网络的技术在一些研究中已被证明是有效的，但它们的过度拟合倾向会给泛化和误诊带来相当大的风险，从而阻碍了它们在临床环境中的广泛应用。已经提出了基于非配对神经风格传递模型的数据增强方案，该方案通过在没有配对训练数据（任何一种图像风格中的同一组织的图像）的情况下使训练图像特征的表示多样化来提高泛化能力。但这些模型同样容易出现各种病理，在没有基础事实/大型数据集的情况下评估它们的性能是具有挑战性的（就像医学成像中经常出现的情况一样）。在这里，我们考虑两种框架/架构：基于GAN的cycleGAN和最近开发的基于扩散的SynDiff。我们评估了它们在从三个开放存取乳房X线摄影数据集和一个非医学图像数据集解析的图像补丁上训练时的性能。我们考虑使用不确定性量化来评估模型的可信度，并提出了一种在非配对训练场景中评估校准质量的方案。这最终有助于在通常无法获得基本事实的领域中可靠地使用图像到图像的翻译模型。 et.al.|[2501.17570](http://arxiv.org/abs/2501.17570)|null|
|**2025-01-29**|**Reproducible generation of green-emitting color centers in hBN using oxygen annealing**|在固态矩阵中产生具有可重复特性的量子发射器的能力对量子技术至关重要。在这里，我们表明，在氧气气氛下退火，可以在商用六方氮化硼中产生高密度的接近相同的单光子发射器。这个简单的过程产生了均匀的色心平面内分布，始终发射约539.4nm的光，波长分布小于1nm。我们对它们的光物理性质进行了广泛的表征，表明发射体明亮稳定，在低温下表现出窄谱线，光谱扩散最小。这些特性使得这个量子发射器家族在量子信息科学的应用中极具吸引力。 et.al.|[2501.17562](http://arxiv.org/abs/2501.17562)|null|

<p align=right>(<a href=#updated-on-20250131>back to top</a>)</p>

## NeRF

|Publish Date|Title|Abstract|PDF|Code|
|---|---|---|---|---|
|**2025-01-22**|**Retrieval-Augmented Neural Field for HRTF Upsampling and Personalization**|具有密集空间网格的头部相关传递函数（HRTF）是沉浸式双耳音频生成的理想选择，但它们的记录很耗时。尽管HRTF空间上采样在神经场方面取得了显著进展，但仅从几个测量方向（例如3或5个测量方向）进行空间上采样仍然具有挑战性。为了解决这个问题，我们提出了一种检索增强神经场（RANF）。RANF从数据集中检索HRTF接近目标受试者HRTF的受试者。除了声源方向本身之外，检索到的对象在所需方向上的HRTF也被馈送到神经场中。此外，我们提出了一种神经网络，它可以有效地处理多个检索到的主题，灵感来自一种称为变换平均连接的多通道处理技术。我们的实验证实了RANF在SONICOM数据集上的优势，它是2024年听众声学个性化挑战任务2获胜解决方案的关键组成部分。 et.al.|[2501.13017](http://arxiv.org/abs/2501.13017)|**[link](https://github.com/merlresearch/ranf-hrtf)**|
|**2025-01-15**|**CityDreamer4D: Compositional Generative Model of Unbounded 4D Cities**|近年来，3D场景生成引起了越来越多的关注，并取得了重大进展。生成4D城市比3D场景更具挑战性，因为存在结构复杂、视觉多样的物体，如建筑物和车辆，并且人类对城市环境中的扭曲更加敏感。为了解决这些问题，我们提出了CityDreamer4D，这是一个专门为生成无界4D城市而定制的组合生成模型。我们的主要见解是1）4D城市生成应该将动态对象（如车辆）与静态场景（如建筑物和道路）分开，2）4D场景中的所有对象都应该由建筑物、车辆和背景材料的不同类型的神经场组成。具体来说，我们提出了交通场景生成器和无边界布局生成器，使用高度紧凑的BEV表示生成动态交通场景和静态城市布局。4D城市中的对象是通过结合面向对象和面向实例的神经场来生成的，用于背景材料、建筑物和车辆。为了适应背景材料和实例的不同特征，神经场采用定制的生成哈希网格和周期性位置嵌入作为场景参数化。此外，我们还为城市生成提供了一套全面的数据集，包括OSM、GoogleEarth和CityTopia。OSM数据集提供了各种真实世界的城市布局，而谷歌地球和CityTopia数据集则提供了大规模、高质量的城市图像，并附有3D实例注释。利用其组合设计，CityDreamer4D支持一系列下游应用程序，如实例编辑、城市风格化和城市模拟，同时在生成逼真的4D城市方面提供最先进的性能。 et.al.|[2501.08983](http://arxiv.org/abs/2501.08983)|**[link](https://github.com/hzxie/CityDreamer4D)**|
|**2025-01-15**|**Score-based 3D molecule generation with neural fields**|我们介绍了一种基于连续原子密度场的3D分子的新表示方法。使用这种表示法，我们提出了一种基于步跳采样的新模型，用于使用神经场在连续空间中无条件生成3D分子。我们的模型FuncMol使用条件神经场将分子场编码为潜码，使用Langevin MCMC从高斯平滑分布中采样噪声码（walk），在一步中对这些样本进行去噪（jump），最后将它们解码为分子场。与大多数方法不同，FuncMol可以在不假设分子结构的情况下进行3D分子的全原子生成，并且可以很好地与分子的大小进行缩放。我们的方法在类药物分子上取得了具有竞争力的结果，并且很容易扩展到大环肽，采样速度至少快一个数量级。该代码可在以下网址获得https://github.com/prescient-design/funcmol. et.al.|[2501.08508](http://arxiv.org/abs/2501.08508)|**[link](https://github.com/prescient-design/funcmol)**|
|**2025-01-10**|**Nonlinear partial differential equations in neuroscience: from modelling to mathematical theory**|许多偏微分方程组已被提出作为大型神经元网络中复杂集体行为的简化表示。在这项调查中，我们简要讨论了它们的推导，然后回顾了为处理这些模型的独特特征而开发的数学方法，这些模型通常是非线性和非局部的。第一部分重点介绍抛物型福克-普朗克方程：非线性噪声泄漏积分和火神经元模型，PDE形式的随机神经场及其在网格单元中的应用，以及基于速率的决策模型。第二部分涉及双曲线输运方程，即自上次排放以来经过的时间模型和基于跳跃的泄漏积分和火灾模型。最后一部分介绍了一些动力学介观模型，特别关注动力学电压电导模型和FitzHugh-Nagumo动力学福克-普朗克系统。 et.al.|[2501.06015](http://arxiv.org/abs/2501.06015)|null|
|**2025-01-10**|**Locality-aware Gaussian Compression for Fast and High-quality Rendering**|我们提出了LocoGS，这是一种局部感知的3D高斯散斑（3DGS）框架，它利用3D高斯的空间相干性对体积场景进行紧凑建模。为此，我们首先分析了3D高斯属性的局部相干性，并提出了一种新的局部感知3D高斯表示，该表示使用具有最小存储要求的神经场表示对局部相干高斯属性进行有效编码。除了新颖的表示方法外，LocoGS还经过精心设计，添加了密集初始化、自适应球面谐波带宽方案和针对不同高斯属性的不同编码方案等附加组件，以最大限度地提高压缩性能。实验结果表明，对于代表性的真实世界3D数据集，我们的方法优于现有的紧凑高斯表示的渲染质量，同时实现了从54.6美元到96.6美元的压缩存储大小，以及从2.1美元到2.4美元的渲染速度。甚至我们的方法也证明了平均渲染速度比最先进的压缩方法高2.4倍，具有相当的压缩性能。 et.al.|[2501.05757](http://arxiv.org/abs/2501.05757)|null|
|**2025-01-08**|**KN-LIO: Geometric Kinematics and Neural Field Coupled LiDAR-Inertial Odometry**|激光雷达惯性测距（LIO）的最新进展推动了大量应用。然而，传统的LIO系统往往更侧重于定位而不是映射，映射主要由稀疏的几何元素组成，这对于下游任务来说并不理想。最近新兴的神经场技术在密集测绘方面具有巨大的潜力，但纯激光雷达测绘很难在高动态车辆上进行。为了缓解这一挑战，我们提出了一种新的解决方案，将几何运动学与神经场紧密耦合，以增强同时状态估计和密集映射能力。我们提出了半耦合和紧耦合的运动学神经LIO（KN-LIO）系统，该系统利用在线SDF解码和迭代误差状态卡尔曼滤波来融合激光和惯性数据。我们的KN-LIO最大限度地减少了信息丢失，提高了状态估计的准确性，同时也适应了异步多LiDAR输入。对各种高动态数据集的评估表明，我们的KN-LIO在姿态估计方面的性能与现有最先进的解决方案相当或更优，并且与纯基于LiDAR的方法相比，提供了更高的密集映射精度。相关代码和数据集将在https://**上提供。 et.al.|[2501.04263](http://arxiv.org/abs/2501.04263)|null|
|**2025-01-06**|**NeuroPMD: Neural Fields for Density Estimation on Product Manifolds**|我们提出了一种新的深度神经网络方法，用于在乘积黎曼流形域上进行密度估计。在我们的方法中，网络直接参数化未知密度函数，并使用惩罚最大似然框架进行训练，惩罚项使用流形微分算子形成。网络架构和估计算法经过精心设计，以应对高维积流形域的挑战，有效地减轻了限制传统核和基展开估计器的维数灾难，并克服了非专用神经网络方法遇到的收敛问题。广泛的模拟和对大脑结构连接数据的实际应用突显了我们的方法相对于竞争对手的明显优势。 et.al.|[2501.02994](http://arxiv.org/abs/2501.02994)|**[link](https://github.com/will-consagra/neuropmd)**|
|**2025-01-03**|**Fusion DeepONet: A Data-Efficient Neural Operator for Geometry-Dependent Hypersonic Flows on Arbitrary Grids**|设计再入飞行器需要准确预测其几何形状周围的高超音速流动。对这种流动的快速预测可以彻底改变车辆设计，特别是对于变形几何形状。我们评估了先进的神经算子模型，如深度算子网络（DeepONet）、参数条件U-Net、傅里叶神经算子（FNO）和MeshGraphNet，目的是解决在有限数据下学习依赖几何的高超音速流场的挑战。具体来说，我们比较了两种网格类型的这些模型的性能：均匀笛卡尔网格和不规则网格。为了训练这些模型，我们使用36个独特的椭圆几何体，使用高阶熵稳定的DGSEM求解器生成高保真模拟，强调了使用稀缺数据集的挑战。我们评估并比较了四种基于算子的模型在预测椭圆体周围高超音速流场方面的有效性。此外，我们开发了一个名为Fusion DeepONet的新框架，该框架利用了神经场概念，并在不同的几何结构中有效地进行了推广。尽管训练数据稀缺，Fusion DeepONet在均匀网格上的性能与参数条件U-Net相当，而在不规则、任意网格上的表现优于MeshGraphNet和vanilla DeepONnet。与U-Net、MeshGraphNet和FNO相比，Fusion DeepONet需要更少的可训练参数，使其计算效率更高。我们还使用奇异值分解分析了Fusion DeepONet模型的基函数。该分析表明，Fusion DeepONet能够有效地推广到看不见的解决方案，并适应不同的几何形状和网格点，证明了其在训练数据有限的情况下的鲁棒性。 et.al.|[2501.01934](http://arxiv.org/abs/2501.01934)|null|
|**2024-12-30**|**Hierarchical Pose Estimation and Mapping with Multi-Scale Neural Feature Fields**|机器人应用需要对场景有全面的了解。近年来，基于神经场的参数化整个环境的方法已经变得流行。由于其连续性和学习场景先验的能力，这些方法很有前景。然而，当处理未知的传感器姿态和连续测量时，在机器人中使用神经场变得具有挑战性。本文主要研究大规模神经隐式SLAM的传感器姿态估计问题。我们从概率的角度研究了隐式映射，并提出了具有相应神经网络架构的分层姿态估计。我们的方法非常适合大规模隐式映射表示。所提出的方法在连续的室外LiDAR扫描上运行，实现了精确的姿态估计，同时保持了短轨迹和长轨迹的稳定映射质量。我们在适合大规模重建的结构化稀疏隐式表示上构建了我们的方法，并使用KITTI和MaiCity数据集对其进行了评估。我们的方法在未知姿态的映射方面优于基线，并实现了最先进的定位精度。 et.al.|[2412.20976](http://arxiv.org/abs/2412.20976)|null|
|**2024-12-26**|**Humans as a Calibration Pattern: Dynamic 3D Scene Reconstruction from Unsynchronized and Uncalibrated Videos**|最近关于动态神经场重建的工作假设输入来自具有已知姿势的同步多视图视频。这些输入约束在现实世界的设置中经常得不到满足，使得这种方法不切实际。我们证明，如果视频捕捉到人体运动，则姿态未知的非同步视频可以生成动态神经场。人类是最常见的动态主体之一，其姿势可以使用最先进的方法进行估计。在有噪声的情况下，估计的人体形状和姿态参数为训练一致的动态神经表示的高度非凸和欠约束问题提供了一个不错的初始化。给定人类的姿势和形状序列，我们估计视频之间的时间偏移，然后通过分析3D关节位置进行相机姿势估计。然后，我们使用多分辨率脊训练动态NeRF，同时细化时间偏移和相机姿态。该设置仍然涉及优化许多参数，因此，我们引入了一种鲁棒的渐进学习策略来稳定该过程。实验表明，我们的方法在具有挑战性的条件下实现了精确的时空校准和高质量的场景重建。 et.al.|[2412.19089](http://arxiv.org/abs/2412.19089)|null|

<p align=right>(<a href=#updated-on-20250131>back to top</a>)</p>

[contributors-shield]: https://img.shields.io/github/contributors/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[contributors-url]: https://github.com/Vincentqyw/cv-arxiv-daily/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[forks-url]: https://github.com/Vincentqyw/cv-arxiv-daily/network/members
[stars-shield]: https://img.shields.io/github/stars/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[stars-url]: https://github.com/Vincentqyw/cv-arxiv-daily/stargazers
[issues-shield]: https://img.shields.io/github/issues/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[issues-url]: https://github.com/Vincentqyw/cv-arxiv-daily/issues

