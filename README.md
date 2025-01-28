[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]

## Updated on 2025.01.28
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
|**2025-01-24**|**CheapNVS: Real-Time On-Device Narrow-Baseline Novel View Synthesis**|单视图新视图合成（NVS）因其不适定性而成为一个臭名昭著的问题，并且通常需要大量计算昂贵的方法来产生有形的结果。在本文中，我们提出了CheapNVS：一种基于多级训练的新颖、高效的多编码器/解码器设计的窄基线单视图NVS的完全端到端方法。CheapNVS首先使用轻量级的可学习模块来近似费力的3D图像扭曲，这些模块以目标视图的相机姿态嵌入为条件，然后并行地对遮挡区域进行修复，以实现显著的性能提升。一旦在Open Images数据集的一个子集上进行了训练，CheapNVS的性能就超过了最先进的技术，尽管速度快了10倍，内存消耗减少了6%。此外，CheapNVS在移动设备上实时运行舒适，在三星Tab 9+上达到30 FPS以上。 et.al.|[2501.14533](http://arxiv.org/abs/2501.14533)|null|
|**2025-01-22**|**3DGS $^2$ : Near Second-order Converging 3D Gaussian Splatting**|3D高斯散斑（3DGS）已成为新颖视图合成和3D重建的主流解决方案。通过使用高斯核的集合对3D场景进行显式编码，3DGS以卓越的效率实现了高质量的渲染。作为一种基于学习的方法，3DGS训练采用了标准的随机梯度下降（SGD）方法，该方法最多提供线性收敛。因此，即使在GPU加速的情况下，训练通常也需要几十分钟。本文介绍了一种用于3DGS的（近）二阶收敛训练算法，利用其独特的特性。我们的方法受到两个关键观察结果的启发。首先，高斯核的属性独立地影响图像空间损失，这支持孤立和局部优化算法。我们通过在单个内核属性级别分割优化，为每个参数组解析构建小尺寸牛顿系统，并在GPU线程上高效求解这些系统来利用这一点。这实现了每个训练图像的牛顿式收敛，而不依赖于全局Hessian。其次，核在输入图像之间表现出稀疏和结构化的耦合。这一特性使我们能够有效地利用空间信息来减轻随机训练过程中的超调。我们的方法比基于标准GPU的3DGS训练更快地收敛顺序，需要的迭代次数比基于SGD的3DGS重建少10多倍，同时保持或超过重建的质量。 et.al.|[2501.13975](http://arxiv.org/abs/2501.13975)|null|
|**2025-01-22**|**GS-LiDAR: Generating Realistic LiDAR Point Clouds with Panoramic Gaussian Splatting**|激光雷达新视图合成（NVS）已成为激光雷达模拟中的一项新任务，它从新的视角提供有价值的模拟点云数据，以帮助自动驾驶系统。然而，现有的LiDAR NVS方法通常依赖于神经辐射场（NeRF）作为其3D表示，这在训练和渲染方面都会产生巨大的计算成本。此外，NeRF及其变体是为对称场景设计的，因此不适合驾驶场景。为了应对这些挑战，我们提出了GS LiDAR，这是一种用于生成具有全景高斯散射的逼真LiDAR点云的新框架。我们的方法采用具有周期性振动特性的二维高斯基元，允许在驾驶场景中对静态和动态元素进行精确的几何重建。我们进一步介绍了一种新的全景渲染技术，该技术在全景LiDAR监控的引导下，具有显式的光线平面相交。通过将强度和光线滴球面谐波（SH）系数合并到高斯基元中，我们增强了渲染点云的真实感。在KITTI-360和nuScenes上的大量实验证明了我们的方法在定量指标、视觉质量以及训练和渲染效率方面的优越性。 et.al.|[2501.13971](http://arxiv.org/abs/2501.13971)|**[link](https://github.com/fudan-zvg/gs-lidar)**|
|**2025-01-23**|**GoDe: Gaussians on Demand for Progressive Level of Detail and Scalable Compression**|3D高斯散斑通过用高斯混合表示场景并利用可微光栅化来增强新颖视图合成中的实时性能。然而，它通常需要大的存储容量和高VRAM，要求设计有效的修剪和压缩技术。现有方法虽然在某些情况下有效，但在可扩展性方面存在困难，无法根据计算能力或带宽等关键因素调整模型，需要在不同配置下重新训练模型。在这项工作中，我们提出了一种新颖的、与模型无关的技术，将高斯分布组织成几个层次，实现了渐进的细节层次（LoD）策略。这种方法与最近的3DGS压缩方法相结合，允许单个模型在多个压缩比上即时扩展，与单个不可扩展模型相比，对质量的影响最小或没有影响，也不需要重新训练。我们在典型的数据集和基准上验证了我们的方法，展示了低失真和在可扩展性和适应性方面的显著收益。 et.al.|[2501.13558](http://arxiv.org/abs/2501.13558)|null|
|**2025-01-22**|**DWTNeRF: Boosting Few-shot Neural Radiance Fields via Discrete Wavelet Transform**|神经辐射场（NeRF）在新颖的视图合成和3D场景表示方面取得了卓越的性能，但其实际应用受到收敛缓慢和依赖密集训练视图的阻碍。为此，我们提出了DWTNeRF，这是一个基于Instant NGP快速训练哈希编码的统一框架。它与为少镜头NeRF设计的正则化项相结合，后者在稀疏训练视图上运行。我们的DWTNeRF包括一种新颖的离散小波损耗，允许在训练目标中直接对低频进行显式优先级排序，从而减少早期训练阶段少数镜头NeRF对高频的过拟合。我们还引入了一种基于模型的方法，该方法基于多头注意力，与基于INGP的模型兼容，这些模型对架构变化很敏感。在3-shot LLFF基准测试中，DWTNeRF的PSNR、SSIM和LPIPS分别比Vanilla NeRF高出15.07%、24.45%和36.30%。我们的方法鼓励重新思考基于INGP模型的当前少镜头方法。 et.al.|[2501.12637](http://arxiv.org/abs/2501.12637)|null|
|**2025-01-22**|**HAC++: Towards 100X Compression of 3D Gaussian Splatting**|3D高斯散斑（3DGS）已成为一种有前景的新型视图合成框架，具有快速渲染速度和高保真度。然而，大量的高斯分布及其相关属性需要有效的压缩技术。然而，高斯点云（或我们论文中的锚点）的稀疏性和无组织性给压缩带来了挑战。为了实现紧凑的大小，我们提出了HAC++，它利用了无组织锚点和结构化哈希网格之间的关系，利用它们的互信息进行上下文建模。此外，HAC++捕获锚点内的上下文关系，以进一步提高压缩性能。为了促进熵编码，我们利用高斯分布来精确估计每个量化属性的概率，其中提出了一种自适应量化模块来实现这些属性的高精度量化，以提高保真度恢复。此外，我们采用了一种自适应掩蔽策略来消除无效的高斯分布和锚点。总体而言，与vanilla 3DGS相比，HAC++在所有数据集上平均时实现了超过100倍的显著尺寸减小，同时提高了保真度。与脚手架GS相比，它还可以减少20倍以上的尺寸。我们的代码可在https://github.com/YihangChen-ee/HAC-plus. et.al.|[2501.12255](http://arxiv.org/abs/2501.12255)|**[link](https://github.com/yihangchen-ee/hac-plus)**|
|**2025-01-21**|**Survey on Monocular Metric Depth Estimation**|单目深度估计（MDE）是一项基本的计算机视觉任务，支撑着空间理解、3D重建和自动驾驶等应用。虽然基于深度学习的MDE方法可以从单个图像中预测相对深度，但它们缺乏度量尺度信息通常会导致尺度不一致，限制了它们在视觉SLAM、3D重建和新颖视图合成等下游任务中的实用性。单目度量深度估计（MMDE）通过实现精确的场景级深度推断来解决这些挑战。MMDE提高了深度一致性，增强了顺序任务的稳定性，简化了与下游应用程序的集成，并拓宽了实际用例。本文对深度估计技术进行了全面的回顾，重点介绍了从基于几何的方法到最先进的深度学习方法的演变。它强调了标度不可知方法的进步，这对于实现零样本泛化作为MMDE的基础能力至关重要。探讨了零样本MMDE研究的最新进展，重点讨论了模型泛化和场景边界细节丢失等挑战。解决这些问题的创新策略包括无标签数据增强、图像修补、架构优化和生成技术。详细分析后，这些进步表明了对克服现有局限性的重大贡献。最后，本文综合了零样本MMDE的最新发展，确定了尚未解决的挑战，并概述了未来的研究方向。通过提供清晰的路线图和前沿的见解，这项工作旨在加深对MMDE的理解，激发新的应用，并推动技术创新。 et.al.|[2501.11841](http://arxiv.org/abs/2501.11841)|null|
|**2025-01-20**|**See In Detail: Enhancing Sparse-view 3D Gaussian Splatting with Local Depth and Semantic Regularization**|3D高斯散斑（3DGS）在新颖的视图合成中表现出了显著的性能。然而，当输入视图稀疏时，其渲染质量会下降，导致内容失真和细节减少。这种限制阻碍了它的实际应用。为了解决这个问题，我们提出了一种稀疏视图3DGS方法。鉴于稀疏视图渲染固有的不适定性，整合先验信息至关重要。我们提出了一种语义正则化技术，使用从预训练的DINO-ViT模型中提取的特征来确保多视图语义的一致性。此外，我们提出了局部深度正则化，它约束深度值以提高对看不见的视图的泛化能力。我们的方法优于最先进的新颖视图合成方法，在LLFF数据集上实现了高达0.4dB的PSNR改善，同时减少了失真并提高了视觉质量。 et.al.|[2501.11508](http://arxiv.org/abs/2501.11508)|null|
|**2025-01-18**|**Decoupling Appearance Variations with 3D Consistent Features in Gaussian Splatting**|高斯散斑已成为新颖视图合成中一种突出的3D表示，但它仍然存在外观变化，这是由各种因素引起的，如现代相机ISP、一天中的不同时间、天气条件和局部光线变化。这些变化可能会导致渲染图像/视频中的浮动和颜色失真。高斯散斑中最近的外观建模方法要么与渲染过程紧密耦合，阻碍了实时渲染，要么只考虑了轻微的全局变化，在局部光线变化的场景中表现不佳。在本文中，我们提出了DAVIGS，这是一种以即插即用和高效的方式解耦外观变化的方法。通过在图像级别而不是高斯级别转换渲染结果，我们的方法可以在最小的优化时间和内存开销下对外观变化进行建模。此外，我们的方法在3D空间中收集与外观相关的信息来转换渲染图像，从而隐式地建立视图之间的3D一致性。我们在几个外观变体场景上验证了我们的方法，并证明它在不影响渲染速度的情况下，以最少的训练时间和内存使用实现了最先进的渲染质量。此外，它以即插即用的方式为不同的高斯散斑基线提供了性能改进。 et.al.|[2501.10788](http://arxiv.org/abs/2501.10788)|null|
|**2025-01-16**|**CrossModalityDiffusion: Multi-Modal Novel View Synthesis with Unified Intermediate Representation**|地理空间成像利用了来自各种传感方式的数据，如地球观测、合成孔径雷达和激光雷达，从地面无人机到卫星视图。这些异构输入为场景理解提供了重要机会，但在准确解释几何体方面存在挑战，特别是在缺乏精确地面实况数据的情况下。为了解决这个问题，我们提出了CrossModalityDiffusion，这是一个模块化框架，旨在在没有场景几何先验知识的情况下生成不同模态和视点的图像。CrossModalityDiffusion采用特定于模态的编码器，这些编码器拍摄多个输入图像并产生几何感知特征体，这些特征体对相对于其输入相机位置的场景结构进行编码。放置特征体积的空间是统一输入模式的共同基础。这些特征体被重叠，并使用体绘制技术从新的角度渲染成特征图像。渲染的特征图像被用作特定模态扩散模型的调节输入，从而能够合成所需输出模态的新图像。在本文中，我们证明了联合训练不同的模块可以确保框架内所有模态的一致几何理解。我们在合成ShapeNet汽车数据集上验证了CrossModalityDiffusion的能力，证明了它在跨多种成像模态和视角生成准确一致的新视图方面的有效性。 et.al.|[2501.09838](http://arxiv.org/abs/2501.09838)|**[link](https://github.com/alexberian/crossmodalitydiffusion)**|

<p align=right>(<a href=#updated-on-20250128>back to top</a>)</p>

## 3D Reconstruction

|Publish Date|Title|Abstract|PDF|Code|
|---|---|---|---|---|
|**2025-01-24**|**Towards Unified Structured Light Optimization**|结构光（SL）3D重建捕捉物体的精确表面形状，提供工业检测和机器人视觉系统所必需的高精度3D数据。然而，目前在SL 3D重建中优化投影模式的研究面临两个主要局限性：每个场景都需要单独训练校准参数，优化仅限于特定类型的SL，这限制了它们的应用范围。为了解决这些局限性，我们提出了一个统一的SL优化框架，适用于不同的照明条件、对象类型和不同类型的SL。我们的框架仅使用单个投影图像即可快速确定最佳投影模式。主要贡献包括一种针对投影仪的新型全局匹配方法，该方法仅使用一个投影图像即可实现精确的投影仪-相机对准，以及一种具有光度调整模块的新投影补偿模型，以减少色域外裁剪产生的伪影。实验结果表明，我们的方法在各种对象、SL模式和光照条件下实现了卓越的解码精度，明显优于以前的方法。 et.al.|[2501.14659](http://arxiv.org/abs/2501.14659)|null|
|**2025-01-24**|**Trick-GS: A Balanced Bag of Tricks for Efficient Gaussian Splatting**|高斯溅射（GS）用于3D重建因其快速训练、推理速度和高质量重建而变得非常流行。然而，基于GS的重建通常由数百万高斯人组成，这使得它们很难在智能手机等计算受限的设备上使用。本文首先对高效GS方法的进展进行了原则性分析。然后，我们提出了Trick GS，它是几种策略的精心组合，包括（1）具有分辨率、噪声和高斯尺度的渐进式训练，（2）学习根据基元和SH带的重要性修剪和屏蔽基元和SH-带，以及（3）加速GS训练框架。Trick GS向资源受限的GS迈出了一大步，其中更快的运行时间、更小更快的模型收敛是最重要的。我们在三个数据集上的结果表明，与普通GS相比，Trick GS的训练速度提高了2倍，磁盘大小减小了40倍，渲染速度提高了两倍，同时具有相当的准确性。 et.al.|[2501.14534](http://arxiv.org/abs/2501.14534)|null|
|**2025-01-24**|**Scalable Benchmarking and Robust Learning for Noise-Free Ego-Motion and 3D Reconstruction from Noisy Video**|我们的目标是通过解决现有模型中对无噪声数据的依赖这一关键限制，重新定义鲁棒的自我运动估计和逼真的3D重建。虽然这种经过净化的条件简化了评估，但它们未能捕捉到现实世界环境中不可预测、嘈杂的复杂性。当这些模型在实践中部署时，动态运动、传感器缺陷和同步扰动会导致性能急剧下降，这表明迫切需要能够在现实世界的噪音中接受并表现出色的框架。为了弥合这一差距，我们解决了三个核心挑战：可扩展的数据生成、全面的基准测试和模型鲁棒性增强。首先，我们介绍了一个可扩展的噪声数据合成流水线，该流水线生成各种数据集，模拟复杂的运动、传感器缺陷和同步误差。其次，我们利用这个管道创建了Robust-Ego3D，这是一个严格设计的基准，旨在暴露噪声引起的性能下降，突显了当前基于学习的方法在自我运动精度和3D重建质量方面的局限性。第三，我们提出了对应引导高斯散斑（CorrGS），这是一种新的测试时间自适应方法，通过将噪声观测值与来自干净3D地图的渲染RGB-D帧对齐，逐步细化内部干净的3D表示，通过视觉对应增强几何对齐和外观恢复。对合成和真实世界数据的广泛实验表明，CorrGS始终优于现有的最先进方法，特别是在涉及快速运动和动态照明的场景中。 et.al.|[2501.14319](http://arxiv.org/abs/2501.14319)|**[link](https://github.com/xiaohao-xu/slam-under-perturbation)**|
|**2025-01-24**|**Comparative analysis of two episodes of strongly geoeffective CME events in November and December 2023**|2023年秋季，一系列时间紧迫的喷发事件被远程观测和现场测量。我们研究了类似的太阳事件，其中几个日冕物质抛射部分来自CH附近的同一（活动）区域。这些事件发生在两个事件中，由一个完整的太阳自转隔开，涵盖2023年10月31日至11月3日和11月27日至28日。这两次事件都与2023年11月4日至5日和12月1日至2日的强地磁暴有关。我们的目标是了解这些事件的复杂性，以及全球磁场、太阳风条件和结构相互作用如何与观测到的地磁效应相关。利用GCS三维重建方法，我们推导出了每个CME的运动方向和速度。这些结果与增强的纬度信息（3D DBM）一起输入DBM，有助于将现场测量与太阳表面结构联系起来进行综合解释。第一次发作导致SAR弧，2023年11月5日，三步Dst指数降至-163 nT。两次CME相关的冲击在时间上很接近，被SBC隔开，随后是一个短时间的通量绳状结构。在第二集中，极光和两步Dst指数在2023年12月1日降至-108nT。一个日冕物质抛射的冲击与前一个日冕物抛射的磁结构相互作用，再次与SBC结合。从产生冲击的CME中检测到清晰的磁通绳结构。这两个事件都显示了SBC后明显的磁场“涟漪”以及密度和温度的波动。这项研究比较了2023年11月和12月的两次多次爆发事件。相互作用的CME结构和SBC相关的磁调制导致了更强的地磁影响，特别是在2023年11月4日至5日的事件中。高度倾斜的日球层电流片可能进一步影响了日冕物质抛射对地球的影响。 et.al.|[2501.14295](http://arxiv.org/abs/2501.14295)|null|
|**2025-01-24**|**Dense-SfM: Structure from Motion with Dense Consistent Matching**|我们提出了Dense SfM，这是一种新的运动结构（SfM）框架，旨在从多视图图像中进行密集和精确的3D重建。传统SfM方法经常依赖的稀疏关键点匹配限制了精度和点密度，特别是在无纹理区域。密集SfM通过将密集匹配与基于高斯散布（GS）的轨迹扩展相结合来解决这一局限性，该轨迹扩展提供了更一致、更长的特征轨迹。为了进一步提高重建精度，Dense SfM配备了一个多视图核化匹配模块，该模块利用变换器和高斯过程架构，在多个视图之间进行稳健的轨迹细化。对ETH3D和纹理差SfM数据集的评估表明，与最先进的方法相比，密集SfM在精度和密度方面有了显著提高。 et.al.|[2501.14277](http://arxiv.org/abs/2501.14277)|null|
|**2025-01-24**|**Micro-macro Wavelet-based Gaussian Splatting for 3D Reconstruction from Unconstrained Images**|由于外观变化和瞬态遮挡，从无约束图像集合中进行3D重建面临着巨大的挑战。在本文中，我们介绍了一种基于微观-宏观小波的高斯散斑（MW-GS），这是一种通过将场景表示分解为全局、精细和内在分量来增强3D重建的新方法。所提出的方法有两个关键创新：微观-宏观投影，它允许高斯点从多个尺度的特征图中捕获细节，增强多样性；以及基于小波的采样，它利用频域信息来细化特征表示，并显著改善场景外观的建模。此外，我们还整合了一个分层残差融合网络，以无缝集成这些功能。大量实验表明，MW-GS提供了最先进的渲染性能，超越了现有的方法。 et.al.|[2501.14231](http://arxiv.org/abs/2501.14231)|null|
|**2025-01-22**|**3DGS $^2$ : Near Second-order Converging 3D Gaussian Splatting**|3D高斯散斑（3DGS）已成为新颖视图合成和3D重建的主流解决方案。通过使用高斯核的集合对3D场景进行显式编码，3DGS以卓越的效率实现了高质量的渲染。作为一种基于学习的方法，3DGS训练采用了标准的随机梯度下降（SGD）方法，该方法最多提供线性收敛。因此，即使在GPU加速的情况下，训练通常也需要几十分钟。本文介绍了一种用于3DGS的（近）二阶收敛训练算法，利用其独特的特性。我们的方法受到两个关键观察结果的启发。首先，高斯核的属性独立地影响图像空间损失，这支持孤立和局部优化算法。我们通过在单个内核属性级别分割优化，为每个参数组解析构建小尺寸牛顿系统，并在GPU线程上高效求解这些系统来利用这一点。这实现了每个训练图像的牛顿式收敛，而不依赖于全局Hessian。其次，核在输入图像之间表现出稀疏和结构化的耦合。这一特性使我们能够有效地利用空间信息来减轻随机训练过程中的超调。我们的方法比基于标准GPU的3DGS训练更快地收敛顺序，需要的迭代次数比基于SGD的3DGS重建少10多倍，同时保持或超过重建的质量。 et.al.|[2501.13975](http://arxiv.org/abs/2501.13975)|null|
|**2025-01-23**|**Fast3R: Towards 3D Reconstruction of 1000+ Images in One Forward Pass**|多视图3D重建仍然是计算机视觉的核心挑战，特别是在需要跨不同视角进行准确和可扩展表示的应用中。当前领先的方法，如DUSt3R，采用基本成对的方法，成对处理图像，需要昂贵的全局对齐过程来从多个视图进行重建。在这项工作中，我们提出了快速3D重建（Fast3R），这是对DUSt3R的一种新的多视图泛化，通过并行处理多个视图来实现高效和可扩展的3D重建。Fast3R的基于Transformer的架构在一次转发中转发N个图像，绕过了迭代对齐的需要。通过对相机姿态估计和3D重建的广泛实验，Fast3R展示了最先进的性能，在推理速度和减少误差累积方面有了显著提高。这些结果确立了Fast3R作为多视图应用程序的稳健替代方案，在不影响重建精度的情况下提供了增强的可扩展性。 et.al.|[2501.13928](http://arxiv.org/abs/2501.13928)|null|
|**2025-01-23**|**MV-GMN: State Space Model for Multi-View Action Recognition**|多视图动作识别的最新进展在很大程度上依赖于基于Transformer的模型。虽然这些模型有效且适应性强，但通常需要大量的计算资源，特别是在具有多个视图和多个时间序列的场景中。为了解决这一局限性，本文介绍了MV-GMN模型，这是一种状态空间模型，专门用于高效地聚合多模态数据（RGB和骨架）、多视图视角和多时相信息，以降低计算复杂度进行动作识别。MV-GMN模型采用了一种创新的多视图图Mamba网络，该网络由一系列MV-GMN块组成。每个块包括一个拟议的双向状态空间块和一个GCN模块。双向状态空间块引入了四种扫描策略，包括视图优先和时间优先方法。GCN模块利用基于规则和基于KNN的方法构建图网络，有效地整合了来自不同视角和时间实例的特征。MV-GMN在多个数据集上的表现优于最新技术，在跨主题和跨视图场景下，在NTU RGB+D 120数据集上分别实现了97.3%和96.7%的显著准确率，证明了其有效性。MV-GMN还超越了基于Transformer的基线，同时只需要线性推理复杂性，突显了该模型减少计算负载、增强多视图动作识别技术的可扩展性和适用性的能力。 et.al.|[2501.13829](http://arxiv.org/abs/2501.13829)|null|
|**2025-01-23**|**VARFVV: View-Adaptive Real-Time Interactive Free-View Video Streaming with Edge Computing**|自由观看视频（FVV）允许用户从多个视角探索沉浸式视频内容。然而，由于视图切换的不确定性，再加上传输和解码多个视频流所需的大量带宽和计算资源，交付FVV带来了重大挑战，这可能会导致频繁的播放中断。现有的方法，无论是基于客户端还是基于云，都难以在有限的带宽和计算资源下满足高质量的体验（QoE）要求。为了解决这些问题，我们提出了VARFVV，这是一种带宽和计算效率高的系统，能够实现具有高QoE和低切换延迟的实时交互式FVV流。具体来说，VARFVV引入了一种低复杂度的FVV生成方案，该方案基于用户选择的视图轨迹在边缘服务器上重新组装多视图视频帧，消除了转码的需要，并显著降低了计算开销。这种设计使其非常适合大规模、基于移动的UHD FVV体验。此外，我们提出了一种利用图神经网络的流行度自适应比特分配方法，该方法预测视图流行度并动态调整比特分配，以在带宽限制内最大化QoE。我们还构建了一个FVV数据集，其中包括来自10个场景的330个视频，包括篮球、歌剧等。大量实验表明，VARFVV在视频质量、切换延迟、计算效率和带宽使用方面优于现有方法，在单个边缘服务器上支持500多个用户，切换延迟为71.5ms。我们的代码和数据集可在https://github.com/qianghu-huber/VARFVV. et.al.|[2501.13630](http://arxiv.org/abs/2501.13630)|null|

<p align=right>(<a href=#updated-on-20250128>back to top</a>)</p>

## Diffusion

|Publish Date|Title|Abstract|PDF|Code|
|---|---|---|---|---|
|**2025-01-24**|**Relightable Full-Body Gaussian Codec Avatars**|我们提出了Relightable Full Body Gaussian Codec Avatars，这是一种用精细细节（包括面部和手部）对Relightable全身化身进行建模的新方法。重新照亮全身化身的独特挑战在于身体关节引起的大变形以及光传输对外观的影响。身体姿势的变化会极大地改变身体表面相对于光线的方向，导致局部光传输功能的变化导致局部外观的变化，以及身体部位之间的遮挡导致的非局部变化。为了解决这个问题，我们将光传输分解为局部和非局部效应。使用可学习的带状谐波对漫射辐射传输的局部外观变化进行建模。与球面谐波不同，区域谐波在铰接状态下旋转效率很高。这使我们能够在局部坐标系中学习漫反射辐射传递，从而将局部辐射传递与身体的关节分离。为了考虑非局部外观变化，我们引入了一个阴影网络，该网络在基础网格上预先计算入射辐照度的情况下预测阴影。这有助于学习身体部位之间的非局部阴影。最后，我们使用延迟着色方法来模拟镜面辐射传输，并更好地捕捉反射和高光，如眼睛闪烁。我们证明，我们的方法成功地模拟了可重新点燃的全身化身所需的局部和非局部光传输，在新的照明条件和看不见的姿势下具有出色的泛化能力。 et.al.|[2501.14726](http://arxiv.org/abs/2501.14726)|null|
|**2025-01-24**|**Diffusion based Text-to-Music Generationwith Global and Local Text based Conditioning**|基于扩散的文本到音乐（TTM）模型生成与文本描述相对应的音乐。通常，基于UNet的扩散模型以预训练的大型语言模型或跨模态音频语言表示模型生成的文本嵌入为条件。这项工作提出了一种基于扩散的TTM，其中UNet以（i）通过交叉注意力的单模态语言模型（如T5）和（ii）通过特征线性调制（FiLM）的跨模态音频语言表示模型（如CLAP）为条件。对扩散模型进行训练，以利用T5的局部文本表示和CLAP的全局表示。此外，我们提出了修改，通过我们称之为均值池和自关注池的池化机制从T5中提取全局和局部表示。这种方法减轻了对额外编码器（例如CLAP）提取全局表示的需求，从而减少了模型参数的数量。我们的结果表明，与仅依赖T5局部嵌入的基线模型（KL=1.54）相比，将CLAP全局嵌入结合到T5局部嵌入可以提高文本粘附性（KL=1.47）。或者，通过所提出的均值池方法直接从T5局部嵌入中提取全局文本嵌入，可以产生更好的生成质量（FAD=1.89），同时与基于CLAP和T5文本嵌入的模型相比，表现出稍差的文本粘附性（KL=1.51）（FAD=1.94和KL=1.47）。我们提出的解决方案不仅高效，而且在所需参数数量方面也很紧凑。 et.al.|[2501.14680](http://arxiv.org/abs/2501.14680)|null|
|**2025-01-24**|**On the multidimensional elephant random walk with stops**|本文的目的是研究多维带止点大象随机游走（MERWS）的渐近行为。与标准的大象随机行走相反，大象可以保持自己的位置。我们证明了与MERWS相关的Gram矩阵，经过适当的归一化，几乎肯定会收敛到与MERWS均匀移动的轴相关的确定性矩阵和Mittag-Leffler分布的乘积。它允许我们扩展之前为一维大象随机行走建立的所有结果。更确切地说，在扩散和临界状态下，我们证明了MERWS几乎肯定会收敛。在超扩散状态下，我们建立了MERWS在适当归一化的情况下几乎肯定收敛到非退化随机向量。我们还研究了MERWS的自归一化渐近正态性。 et.al.|[2501.14594](http://arxiv.org/abs/2501.14594)|null|
|**2025-01-24**|**Anomalous Dynamics of a Liquid Corner Film**|测量液体的流变性通常需要精确控制剪切速率和应力。然而，我们证明，幂律流体的特征可以通过简单地观察楔形几何形状内粘性液滴的毛细管扩散动力学来预测。通过考虑这种几何结构中毛细管力和粘性力的影响，我们表明扩散动力学可以用非线性扩散方程来描述。分析预测表明了次扩散行为，在扩散指数和流变指数之间建立了直接关系，这也得到了实验结果的证实。由于这种关系与流动细节无关，因此它为幂律流体的流变特性提供了稳健的预测。 et.al.|[2501.14571](http://arxiv.org/abs/2501.14571)|null|
|**2025-01-24**|**Diffusive transport on the real line: semi-contractive gradient flows and their discretization**|引入了扩散传输距离，这是实线上概率度量之间的一种新的伪度量。它推广了鞅最优输运，并与Hellinger和Wasserstein度量形成了一个层次结构。我们观察到，某些类抛物型偏微分方程，其中包括指数为2的多孔介质方程，在新距离内形式上是半收缩度量梯度流。为了对所考虑的偏微分方程进行适当的空间离散化，这一观察结果是严格的：这些是相对于点格上测量的自适应扩散传输距离的半收缩梯度流。主要结果是凸性模量相对于晶格间距是均匀的。特别是对于二次多孔介质方程，这与Wasserstein梯度流结构的离散化所观察到的相反。 et.al.|[2501.14527](http://arxiv.org/abs/2501.14527)|null|
|**2025-01-24**|**Training-Free Style and Content Transfer by Leveraging U-Net Skip Connections in Stable Diffusion 2.***|尽管最近在利用扩散模型生成图像方面取得了重大进展，但人们对其内部潜在表示仍然知之甚少。现有的研究主要集中在稳定扩散U-Net的瓶颈层（h-space），或者利用交叉注意力、自我注意力或解码层。我们的模型SkipInject利用了U-Net的跳过连接。我们对跳跃连接的作用进行了深入分析，发现第三个编码器块通过的残差连接携带了重建图像的大部分空间信息，将内容从样式中分离出来。我们证明，从该块注入表示可用于基于文本的编辑、精确修改和样式转换。我们比较了我们的方法——最先进的风格转换和图像编辑方法，并证明我们的方法获得了最佳的内容对齐和最佳的结构保留权衡。 et.al.|[2501.14524](http://arxiv.org/abs/2501.14524)|null|
|**2025-01-24**|**Ballistic diffusion vs. damped oscillation of energy in a $\mathcal{PT}$ -symmetric quantum kicked harmonic oscillator**|我们数值研究了对称踢脚谐振子的量子动力学。我们观察到，动量的有向流和能量的弹道扩散在非共振条件下共存，而在共振条件下，动量和能量都以相同频率的阻尼余弦函数振荡。研究表明，动量的有向流和能量的弹道扩散源于非厄米驱动下动量本征态之间的最近邻跳跃，而动量和能量的阻尼振荡源于非赫米驱动和谐振子之间的共振耦合。我们的发现表明，该系统的非厄密性和频率特性共同导致了这些独特的动力学行为。 et.al.|[2501.14507](http://arxiv.org/abs/2501.14507)|null|
|**2025-01-24**|**Central schemes for systems of non-local balance laws**|我们提出了近似非局部平衡律系统解的数值方法。特别是，我们基于著名的Nessyahu-Tadmor方案推导出了一个非交错中心方案，并证明了它保留了解的正性。为了减少数值扩散，我们考虑了Kurganov-Tadmor方案的非局部版本。对于这两种方案，非局部项的适当近似对于保持二阶精度至关重要。数值例子验证了我们的理论，并证明了它对各种非局部问题系统的适用性。 et.al.|[2501.14425](http://arxiv.org/abs/2501.14425)|null|
|**2025-01-24**|**Handling Heterophily in Recommender Systems with Wavelet Hypergraph Diffusion**|推荐系统在跨各个领域提供个性化用户体验方面至关重要。然而，捕捉用户-项目交互的异质性模式和多维性带来了重大挑战。为了解决这个问题，我们引入了FWHDNN（基于融合的小波超图扩散神经网络），这是一种创新的框架，旨在推进基于超图的推荐任务中的表示学习。该模型包含三个关键组成部分：（1）交叉差分关系编码器，利用异质性感知超图扩散来适应不同类别标签的消息传递；（2）多级聚类编码器，采用基于小波变换的超图神经网络层来捕获多尺度拓扑关系；（3）集成的多模态融合机制，通过中间和后期融合策略将结构和文本信息结合起来。对真实世界数据集的广泛实验表明，FWHDNN在捕获用户和项目之间的高阶互连方面，在准确性、鲁棒性和可扩展性方面超越了最先进的方法。 et.al.|[2501.14399](http://arxiv.org/abs/2501.14399)|null|
|**2025-01-24**|**Advancing data-driven broadband seismic wavefield simulation with multi-conditional diffusion model**|地震传感器和震源的稀疏分布给地下成像、震源表征和地震动建模带来了挑战。虽然大型N阵列显示了密集观测数据的潜力，但它们在广大地区的部署受到经济和后勤限制的限制。数值模拟提供了一种替代方案，但模拟真实的波场在计算上仍然很昂贵。为了应对这些挑战，我们开发了一种多条件扩散变换器，用于在不需要先验地质知识的情况下生成地震波场。我们的方法产生高分辨率的波场，可以准确地捕获不同源和站配置的振幅和相位信息。该模型首先生成以输入属性为条件的振幅谱，随后通过迭代相位优化来细化波场。我们使用间歇泉地热场的数据验证了我们的方法，展示了在光谱振幅和相位方面具有空间连续性和保真度的波场的生成。这些合成波场有望推进地震学中的结构成像和震源表征。 et.al.|[2501.14348](http://arxiv.org/abs/2501.14348)|null|

<p align=right>(<a href=#updated-on-20250128>back to top</a>)</p>

## NeRF

|Publish Date|Title|Abstract|PDF|Code|
|---|---|---|---|---|
|**2025-01-22**|**Retrieval-Augmented Neural Field for HRTF Upsampling and Personalization**|具有密集空间网格的头部相关传递函数（HRTF）是沉浸式双耳音频生成的理想选择，但它们的记录很耗时。尽管HRTF空间上采样在神经场方面取得了显著进展，但仅从几个测量方向（例如3或5个测量方向）进行空间上采样仍然具有挑战性。为了解决这个问题，我们提出了一种检索增强神经场（RANF）。RANF从数据集中检索HRTF接近目标受试者HRTF的受试者。除了声源方向本身之外，检索到的对象在所需方向上的HRTF也被馈送到神经场中。此外，我们提出了一种神经网络，它可以有效地处理多个检索到的主题，灵感来自一种称为变换平均连接的多通道处理技术。我们的实验证实了RANF在SONICOM数据集上的优势，它是2024年听众声学个性化挑战任务2获胜解决方案的关键组成部分。 et.al.|[2501.13017](http://arxiv.org/abs/2501.13017)|null|
|**2025-01-15**|**CityDreamer4D: Compositional Generative Model of Unbounded 4D Cities**|近年来，3D场景生成引起了越来越多的关注，并取得了重大进展。生成4D城市比3D场景更具挑战性，因为存在结构复杂、视觉多样的物体，如建筑物和车辆，并且人类对城市环境中的扭曲更加敏感。为了解决这些问题，我们提出了CityDreamer4D，这是一个专门为生成无界4D城市而定制的组合生成模型。我们的主要见解是1）4D城市生成应该将动态对象（如车辆）与静态场景（如建筑物和道路）分开，2）4D场景中的所有对象都应该由建筑物、车辆和背景材料的不同类型的神经场组成。具体来说，我们提出了交通场景生成器和无边界布局生成器，使用高度紧凑的BEV表示生成动态交通场景和静态城市布局。4D城市中的对象是通过结合面向对象和面向实例的神经场来生成的，用于背景材料、建筑物和车辆。为了适应背景材料和实例的不同特征，神经场采用定制的生成哈希网格和周期性位置嵌入作为场景参数化。此外，我们还为城市生成提供了一套全面的数据集，包括OSM、GoogleEarth和CityTopia。OSM数据集提供了各种真实世界的城市布局，而谷歌地球和CityTopia数据集则提供了大规模、高质量的城市图像，并附有3D实例注释。利用其组合设计，CityDreamer4D支持一系列下游应用程序，如实例编辑、城市风格化和城市模拟，同时在生成逼真的4D城市方面提供最先进的性能。 et.al.|[2501.08983](http://arxiv.org/abs/2501.08983)|**[link](https://github.com/hzxie/CityDreamer4D)**|
|**2025-01-15**|**Score-based 3D molecule generation with neural fields**|我们介绍了一种基于连续原子密度场的3D分子的新表示方法。使用这种表示法，我们提出了一种基于步跳采样的新模型，用于使用神经场在连续空间中无条件生成3D分子。我们的模型FuncMol使用条件神经场将分子场编码为潜码，使用Langevin MCMC从高斯平滑分布中采样噪声码（walk），在一步中对这些样本进行去噪（jump），最后将它们解码为分子场。与大多数方法不同，FuncMol可以在不假设分子结构的情况下进行3D分子的全原子生成，并且可以很好地与分子的大小进行缩放。我们的方法在类药物分子上取得了具有竞争力的结果，并且很容易扩展到大环肽，采样速度至少快一个数量级。该代码可在以下网址获得https://github.com/prescient-design/funcmol. et.al.|[2501.08508](http://arxiv.org/abs/2501.08508)|**[link](https://github.com/prescient-design/funcmol)**|
|**2025-01-10**|**Nonlinear partial differential equations in neuroscience: from modelling to mathematical theory**|许多偏微分方程组已被提出作为大型神经元网络中复杂集体行为的简化表示。在这项调查中，我们简要讨论了它们的推导，然后回顾了为处理这些模型的独特特征而开发的数学方法，这些模型通常是非线性和非局部的。第一部分重点介绍抛物型福克-普朗克方程：非线性噪声泄漏积分和火神经元模型，PDE形式的随机神经场及其在网格单元中的应用，以及基于速率的决策模型。第二部分涉及双曲线输运方程，即自上次排放以来经过的时间模型和基于跳跃的泄漏积分和火灾模型。最后一部分介绍了一些动力学介观模型，特别关注动力学电压电导模型和FitzHugh-Nagumo动力学福克-普朗克系统。 et.al.|[2501.06015](http://arxiv.org/abs/2501.06015)|null|
|**2025-01-10**|**Locality-aware Gaussian Compression for Fast and High-quality Rendering**|我们提出了LocoGS，这是一种局部感知的3D高斯散斑（3DGS）框架，它利用3D高斯的空间相干性对体积场景进行紧凑建模。为此，我们首先分析了3D高斯属性的局部相干性，并提出了一种新的局部感知3D高斯表示，该表示使用具有最小存储要求的神经场表示对局部相干高斯属性进行有效编码。除了新颖的表示方法外，LocoGS还经过精心设计，添加了密集初始化、自适应球面谐波带宽方案和针对不同高斯属性的不同编码方案等附加组件，以最大限度地提高压缩性能。实验结果表明，对于代表性的真实世界3D数据集，我们的方法优于现有的紧凑高斯表示的渲染质量，同时实现了从54.6美元到96.6美元的压缩存储大小，以及从2.1美元到2.4美元的渲染速度。甚至我们的方法也证明了平均渲染速度比最先进的压缩方法高2.4倍，具有相当的压缩性能。 et.al.|[2501.05757](http://arxiv.org/abs/2501.05757)|null|
|**2025-01-08**|**KN-LIO: Geometric Kinematics and Neural Field Coupled LiDAR-Inertial Odometry**|激光雷达惯性测距（LIO）的最新进展推动了大量应用。然而，传统的LIO系统往往更侧重于定位而不是映射，映射主要由稀疏的几何元素组成，这对于下游任务来说并不理想。最近新兴的神经场技术在密集测绘方面具有巨大的潜力，但纯激光雷达测绘很难在高动态车辆上进行。为了缓解这一挑战，我们提出了一种新的解决方案，将几何运动学与神经场紧密耦合，以增强同时状态估计和密集映射能力。我们提出了半耦合和紧耦合的运动学神经LIO（KN-LIO）系统，该系统利用在线SDF解码和迭代误差状态卡尔曼滤波来融合激光和惯性数据。我们的KN-LIO最大限度地减少了信息丢失，提高了状态估计的准确性，同时也适应了异步多LiDAR输入。对各种高动态数据集的评估表明，我们的KN-LIO在姿态估计方面的性能与现有最先进的解决方案相当或更优，并且与纯基于LiDAR的方法相比，提供了更高的密集映射精度。相关代码和数据集将在https://**上提供。 et.al.|[2501.04263](http://arxiv.org/abs/2501.04263)|null|
|**2025-01-06**|**NeuroPMD: Neural Fields for Density Estimation on Product Manifolds**|我们提出了一种新的深度神经网络方法，用于在乘积黎曼流形域上进行密度估计。在我们的方法中，网络直接参数化未知密度函数，并使用惩罚最大似然框架进行训练，惩罚项使用流形微分算子形成。网络架构和估计算法经过精心设计，以应对高维积流形域的挑战，有效地减轻了限制传统核和基展开估计器的维数灾难，并克服了非专用神经网络方法遇到的收敛问题。广泛的模拟和对大脑结构连接数据的实际应用突显了我们的方法相对于竞争对手的明显优势。 et.al.|[2501.02994](http://arxiv.org/abs/2501.02994)|**[link](https://github.com/will-consagra/neuropmd)**|
|**2025-01-03**|**Fusion DeepONet: A Data-Efficient Neural Operator for Geometry-Dependent Hypersonic Flows on Arbitrary Grids**|设计再入飞行器需要准确预测其几何形状周围的高超音速流动。对这种流动的快速预测可以彻底改变车辆设计，特别是对于变形几何形状。我们评估了先进的神经算子模型，如深度算子网络（DeepONet）、参数条件U-Net、傅里叶神经算子（FNO）和MeshGraphNet，目的是解决在有限数据下学习依赖几何的高超音速流场的挑战。具体来说，我们比较了两种网格类型的这些模型的性能：均匀笛卡尔网格和不规则网格。为了训练这些模型，我们使用36个独特的椭圆几何体，使用高阶熵稳定的DGSEM求解器生成高保真模拟，强调了使用稀缺数据集的挑战。我们评估并比较了四种基于算子的模型在预测椭圆体周围高超音速流场方面的有效性。此外，我们开发了一个名为Fusion DeepONet的新框架，该框架利用了神经场概念，并在不同的几何结构中有效地进行了推广。尽管训练数据稀缺，Fusion DeepONet在均匀网格上的性能与参数条件U-Net相当，而在不规则、任意网格上的表现优于MeshGraphNet和vanilla DeepONnet。与U-Net、MeshGraphNet和FNO相比，Fusion DeepONet需要更少的可训练参数，使其计算效率更高。我们还使用奇异值分解分析了Fusion DeepONet模型的基函数。该分析表明，Fusion DeepONet能够有效地推广到看不见的解决方案，并适应不同的几何形状和网格点，证明了其在训练数据有限的情况下的鲁棒性。 et.al.|[2501.01934](http://arxiv.org/abs/2501.01934)|null|
|**2024-12-30**|**Hierarchical Pose Estimation and Mapping with Multi-Scale Neural Feature Fields**|机器人应用需要对场景有全面的了解。近年来，基于神经场的参数化整个环境的方法已经变得流行。由于其连续性和学习场景先验的能力，这些方法很有前景。然而，当处理未知的传感器姿态和连续测量时，在机器人中使用神经场变得具有挑战性。本文主要研究大规模神经隐式SLAM的传感器姿态估计问题。我们从概率的角度研究了隐式映射，并提出了具有相应神经网络架构的分层姿态估计。我们的方法非常适合大规模隐式映射表示。所提出的方法在连续的室外LiDAR扫描上运行，实现了精确的姿态估计，同时保持了短轨迹和长轨迹的稳定映射质量。我们在适合大规模重建的结构化稀疏隐式表示上构建了我们的方法，并使用KITTI和MaiCity数据集对其进行了评估。我们的方法在未知姿态的映射方面优于基线，并实现了最先进的定位精度。 et.al.|[2412.20976](http://arxiv.org/abs/2412.20976)|null|
|**2024-12-26**|**Humans as a Calibration Pattern: Dynamic 3D Scene Reconstruction from Unsynchronized and Uncalibrated Videos**|最近关于动态神经场重建的工作假设输入来自具有已知姿势的同步多视图视频。这些输入约束在现实世界的设置中经常得不到满足，使得这种方法不切实际。我们证明，如果视频捕捉到人体运动，则姿态未知的非同步视频可以生成动态神经场。人类是最常见的动态主体之一，其姿势可以使用最先进的方法进行估计。在有噪声的情况下，估计的人体形状和姿态参数为训练一致的动态神经表示的高度非凸和欠约束问题提供了一个不错的初始化。给定人类的姿势和形状序列，我们估计视频之间的时间偏移，然后通过分析3D关节位置进行相机姿势估计。然后，我们使用多分辨率脊训练动态NeRF，同时细化时间偏移和相机姿态。该设置仍然涉及优化许多参数，因此，我们引入了一种鲁棒的渐进学习策略来稳定该过程。实验表明，我们的方法在具有挑战性的条件下实现了精确的时空校准和高质量的场景重建。 et.al.|[2412.19089](http://arxiv.org/abs/2412.19089)|null|

<p align=right>(<a href=#updated-on-20250128>back to top</a>)</p>

[contributors-shield]: https://img.shields.io/github/contributors/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[contributors-url]: https://github.com/Vincentqyw/cv-arxiv-daily/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[forks-url]: https://github.com/Vincentqyw/cv-arxiv-daily/network/members
[stars-shield]: https://img.shields.io/github/stars/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[stars-url]: https://github.com/Vincentqyw/cv-arxiv-daily/stargazers
[issues-shield]: https://img.shields.io/github/issues/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[issues-url]: https://github.com/Vincentqyw/cv-arxiv-daily/issues

