[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]

## Updated on 2023.11.26
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
|**2023-11-22**|**WildFusion: Learning 3D-Aware Latent Diffusion Models in View Space**|现代基于学习的3D感知图像合成方法实现了生成图像的高真实感和3D一致的视点变化。现有方法表示共享规范空间中的实例。然而，对于野生数据集，共享规范系统可能很难定义，甚至可能不存在。在这项工作中，我们转而在视图空间中对实例进行建模，从而减少了对摆拍图像和学习相机分布的需求。我们发现，在这种情况下，现有的基于GAN的方法容易生成平面几何体，并且难以实现分布覆盖。因此，我们提出了WildFusion，这是一种基于潜在扩散模型（LDMs）的3D感知图像合成的新方法。我们首先训练一个自动编码器，该编码器推断出压缩的潜在表示，该编码器还捕获了图像的底层3D结构，不仅能够进行重建，还能够进行新颖的视图合成。为了学习忠实的3D表示，我们利用单目深度预测的线索。然后，我们在3D感知的潜在空间中训练扩散模型，从而能够合成高质量的3D一致图像样本，优于最近最先进的基于GAN的方法。重要的是，我们的3D感知LDM在没有来自多视点图像或3D几何结构的任何直接监督的情况下进行训练，并且不需要姿势图像或学习姿势或相机分布。它直接学习三维表示，而不依赖于规范的相机坐标。这为可扩展的3D感知图像合成和从野生图像数据创建3D内容开辟了有前景的研究途径。看见https://katjaschwarz.github.io/wildfusion我们的3D结果的视频。 et.al.|[2311.13570](http://arxiv.org/abs/2311.13570)|null|
|**2023-11-21**|**An Efficient 3D Gaussian Representation for Monocular/Multi-view Dynamic Scenes**|在从多个输入视图合成场景的新视图中，3D高斯散射是现有辐射场方法的可行替代方案，提供了良好的视觉质量和实时渲染。尽管在静态场景中取得了成功，但由于每个时间步长存储3D高斯参数的责任，3D高斯表示的当前进展在动态场景中在内存消耗和每个时间步长需要大量观测方面面临挑战。在这项研究中，我们提出了一种为动态场景量身定制的高效3D高斯表示，其中我们将位置和旋转定义为时间的函数，同时保持静态3D高斯的其他时不变特性不变。值得注意的是，我们的表示减少了内存使用，无论输入序列长度如何，内存使用都是一致的。此外，它通过考虑时间变化来降低过度拟合观测帧的风险。基于图像和流重建的高斯表示的优化为单目和多视图情况下的动态场景视图合成提供了强大的框架。我们在单个GPU的分辨率为 $1352\times 1014$的情况下获得了每秒$118$ 帧（FPS）的最高渲染速度，显示了我们提出的方法在动态场景渲染场景中的实用性和有效性。 et.al.|[2311.12897](http://arxiv.org/abs/2311.12897)|null|
|**2023-11-21**|**Hyb-NeRF: A Multiresolution Hybrid Encoding for Neural Radiance Fields**|神经辐射场（NeRF）的最新进展已经实现了用于新型视图合成的高保真场景重建。然而，NeRF需要每个像素数百次网络评估来近似体积渲染积分，这使得它的训练速度很慢。将NeRF缓存到显式数据结构中可以有效地提高渲染速度，但代价是更高的内存使用率。为了解决这些问题，我们提出了Hyb-NeRF，这是一种具有多分辨率混合编码的新型神经辐射场，可以实现高效的神经建模和快速渲染，还可以实现高质量的新视图合成。Hyb-NeRF的关键思想是使用从粗分辨率到精细分辨率的不同编码策略来表示场景。Hyb-NeRF利用了粗分辨率下的记忆效率可学习的位置特征，以及精细分辨率下基于哈希的特征网格的快速优化速度和局部细节。此外，为了进一步提高性能，我们在可学习的位置编码中嵌入了基于圆锥跟踪的特征，从而消除了编码的模糊性并减少了混叠伪影。在合成和真实世界数据集上进行的大量实验表明，与以前最先进的方法相比，Hyb-NeRF实现了更快的渲染速度、更好的渲染质量，甚至更低的内存占用。 et.al.|[2311.12490](http://arxiv.org/abs/2311.12490)|null|
|**2023-11-20**|**Holistic Inverse Rendering of Complex Facade via Aerial 3D Scanning**|在这项工作中，我们使用多视图航空图像，使用神经符号距离场（SDF）重建立面的几何结构、照明和材料。在不需要复杂设备的情况下，我们的方法只将无人机捕捉到的简单RGB图像作为输入，以实现基于物理和照片真实感的新颖视图渲染、重新照明和编辑。然而，现实世界中的立面通常具有复杂的外观，从具有细微细节的漫射岩石到具有镜面反射的大面积玻璃窗，这使得很难处理所有事情。因此，以前的方法可以保留几何细节，但无法重建光滑的玻璃窗或虎钳。为了应对这一挑战，我们引入了三种空间和语义自适应优化策略，包括基于零样本分割技术的语义正则化方法以提高材料一致性，频率软件几何正则化方法来平衡不同表面中的表面平滑度和细节，以及基于可见性探针的方案，以实现对大规模户外环境中的局部照明的有效建模。此外，我们还捕捉了真实世界的立面航空3D扫描图像集和相应的点云，用于训练和基准测试。实验证明，与最先进的基线相比，我们的方法在立面整体逆绘制、新颖的视图合成和场景编辑方面具有卓越的质量。 et.al.|[2311.11825](http://arxiv.org/abs/2311.11825)|null|
|**2023-11-18**|**Structure-Aware Sparse-View X-ray 3D Reconstruction**|X射线以其揭示物体内部结构的能力而闻名，有望为3D重建提供比可见光更丰富的信息。然而，现有的神经辐射场（NeRF）算法忽略了X射线的这一重要性质，导致它们在捕捉成像对象的结构内容方面存在局限性。在本文中，我们提出了一个用于稀疏视图X射线三维重建的框架，即结构感知X射线神经辐射密度场（SAX-NeRF）。首先，我们设计了一个基于线段的转换器（Lineformer）作为SAX NeRF的主干。Linefomer通过对X射线的每个线段内的相关性进行建模，捕捉三维空间中对象的内部结构。其次，我们提出了一种掩模局部全局（MLG）射线采样策略来提取二维投影中的上下文和几何信息。此外，我们还收集了一个更大规模的数据集X3D，涵盖了更广泛的X射线应用。在X3D上的实验表明，SAX-NeRF在新的视图合成和CT重建方面分别比以前的基于NeRF的方法高出12.56和2.49dB。代码、模型和数据将在https://github.com/caiyuanhao1998/SAX-NeRF et.al.|[2311.10959](http://arxiv.org/abs/2311.10959)|**[link](https://github.com/caiyuanhao1998/sax-nerf)**|
|**2023-11-16**|**Adaptive Shells for Efficient Neural Radiance Field Rendering**|神经辐射场在新视图合成中实现了前所未有的质量，但其体积公式仍然昂贵，需要大量样本才能渲染高分辨率图像。体积编码对于表示树叶和头发等模糊几何体至关重要，它们非常适合随机优化。然而，许多场景最终主要由固体表面组成，这些表面可以通过每个像素的单个采样精确渲染。基于这一见解，我们提出了一种神经辐射公式，可以在基于体积和表面的渲染之间平滑过渡，大大加快渲染速度，甚至提高视觉逼真度。我们的方法构造了一个显式网格包络，该包络在空间上限制了神经体积表示。在实体区域中，包络几乎收敛到曲面，并且通常可以使用单个采样进行渲染。为此，我们推广了NeuS公式，该公式具有学习的空间变化的核大小，该核大小对密度的扩展进行编码，将宽核与类体积区域拟合，将紧核与类表面区域拟合。然后，我们提取表面周围窄带的显式网格，其宽度由内核大小决定，并微调该窄带内的辐射场。在推断时，我们将光线投射到网格上，并仅在封闭区域内评估辐射场，从而大大减少了所需的样本数量。实验表明，我们的方法能够以非常高的保真度实现高效的渲染。我们还证明了提取的包络可以实现动画和模拟等下游应用。 et.al.|[2311.10091](http://arxiv.org/abs/2311.10091)|null|
|**2023-11-16**|**Reconstructing Continuous Light Field From Single Coded Image**|我们提出了一种从单个观测图像重建目标场景的连续光场的方法。我们的方法两全其美：用于压缩光场采集的联合孔径曝光编码和用于视图合成的神经辐射场（NeRF）。在相机中实现的联合孔径曝光编码能够将3D场景信息有效地嵌入到观察到的图像中，但在以前的工作中，它仅用于重建离散的光场视图。基于NeRF的神经渲染能够从连续视点对3D场景进行高质量的视图合成，但当只给出单个图像作为输入时，它很难实现令人满意的质量。我们的方法将这两种技术集成到一个高效且端到端可训练的管道中。经过对各种场景的训练，我们的方法可以准确高效地重建连续光场，而无需任何测试时间优化。据我们所知，这是第一项将两个世界连接起来的工作：有效获取三维信息的相机设计和神经渲染。 et.al.|[2311.09646](http://arxiv.org/abs/2311.09646)|null|
|**2023-11-11**|**Aria-NeRF: Multimodal Egocentric View Synthesis**|基于受神经辐射场（NeRFs）启发的可微分体积射线跟踪，我们寻求加快开发从以自我为中心的数据训练的丰富的多模式场景模型的研究。从以自我为中心的图像序列构建类似NeRF的模型在理解人类行为方面发挥着关键作用，并在VR/AR领域具有多种应用。这种以自我为中心的类NeRF模型可以用作现实模拟，对能够在现实世界中执行任务的智能代理的发展做出了重大贡献。以自我为中心的视图合成的未来可能会通过使用多模式传感器（如用于自我运动跟踪的IMU、用于捕捉表面纹理和人类语言上下文的音频传感器以及用于推断场景中人类注意力模式的眼睛凝视跟踪器）来增强视觉数据，从而产生超越当今NeRF的新环境表示。为了支持和促进以自我为中心的多模式场景建模的开发和评估，我们提出了一个全面的多模式自我中心视频数据集。该数据集提供了一个全面的感官数据集，包括RGB图像、眼动追踪相机镜头、麦克风录音、气压计的气压读数、GPS的位置坐标、Wi-Fi和蓝牙的连接细节，以及与磁力计配对的双频IMU数据集（1kHz和800Hz）的信息。数据集是使用Meta Aria Glasses可穿戴设备平台收集的。该数据集中捕获的各种数据模式和真实世界背景为我们进一步理解人类行为奠定了坚实的基础，并在VR、AR和机器人领域实现了更身临其境的智能体验。 et.al.|[2311.06455](http://arxiv.org/abs/2311.06455)|null|
|**2023-11-10**|**Improved Positional Encoding for Implicit Neural Representation based Compact Data Representation**|采用位置编码来捕获隐式神经表示（INR）中编码信号的高频信息。在本文中，我们提出了一种新的位置编码方法，该方法提高了INR的重建质量。所提出的嵌入方法对于紧凑的数据表示更有利，因为它比现有方法具有更多的频率基。我们的实验表明，该方法在压缩任务中没有引入任何额外的复杂性，并且在新的视图合成中具有更高的重建质量，从而在率失真性能上获得了显著的增益。 et.al.|[2311.06059](http://arxiv.org/abs/2311.06059)|null|
|**2023-11-09**|**Real-Time Neural Rasterization for Large Scenes**|提出了一种新的大场景真实感实时新视图合成方法。现有的神经渲染方法可以生成逼真的结果，但主要适用于小规模场景（<50平方米），在大规模场景（>10000平方米）中存在困难。传统的基于图形的光栅化渲染对于大型场景来说速度很快，但缺乏真实感，并且需要昂贵的手动创建资源。我们的方法结合了两全其美，将中等质量的脚手架网格作为输入，学习神经纹理场和着色器来建模与视图相关的效果，以增强真实感，同时仍然使用标准图形管道进行实时渲染。我们的方法优于现有的神经渲染方法，为大型自动驾驶和无人机场景提供了至少30倍的渲染速度和相当或更好的真实感。我们的工作是第一个实现大型真实世界场景的实时渲染。 et.al.|[2311.05607](http://arxiv.org/abs/2311.05607)|null|

<p align=right>(<a href=#updated-on-20231126>back to top</a>)</p>

## 3D Reconstruction

|Publish Date|Title|Abstract|PDF|Code|
|---|---|---|---|---|
|**2023-11-22**|**DRIFu: Differentiable Rendering and Implicit Function-based Single-View 3D Reconstruction**|基于可微分绘制和隐函数的模型（DRIFu）源于像素对齐隐函数（PIFU），这是一种开创性的3D数字化技术，最初是为穿着衣服的人体设计的。PIFU擅长在低维空间内捕捉细微的体型变化，并在人体3D扫描中进行了广泛的训练。然而，PIFU在活体动物中的应用带来了重大挑战，主要是由于在3D扫描中获得动物合作的固有困难。为了应对这一挑战，我们引入了专门为动物数字化量身定制的DRIFu模型。为了训练DRIFu，我们采用了一套精心策划的合成3D动物模型，包括不同的形状、大小，甚至考虑到各种变化，如幼鸟。我们创新的比对工具在将这些不同的合成动物模型映射到统一的模板上发挥着关键作用，有助于精确预测动物的形状和纹理。至关重要的是，我们的模板对齐策略建立了一个共享的形状空间，允许对新的动物形状进行无缝采样，逼真地摆出它们的姿势，设置它们的动画，并将它们与真实世界的数据对齐。这种突破性的方法彻底改变了我们全面理解和表现鸟类形态的能力。有关该项目的更多详细信息和访问权限，请访问项目网站https://github.com/kuangzijian/drifu-for-animals et.al.|[2311.13199](http://arxiv.org/abs/2311.13199)|**[link](https://github.com/kuangzijian/drifu-for-animals)**|
|**2023-11-22**|**Differentiable Radio Frequency Ray Tracing for Millimeter-Wave Sensing**|毫米波传感是一种新兴技术，在三维物体表征和环境测绘中有着广泛的应用。然而，从稀疏毫米波信号中实现精确的3D重建仍然具有挑战性。现有的方法依赖于数据驱动的学习，受到数据集可用性和泛化困难的限制。我们提出了DiffSBR，一种基于毫米波的三维重建的可微分框架。DiffSBR结合了一个可微分光线跟踪引擎，从虚拟3D模型中模拟雷达点云。基于梯度的优化器对模型参数进行细化，以最大限度地减少模拟点云和真实点云之间的差异。使用各种雷达硬件的实验验证了DiffSBR进行细粒度3D重建的能力，即使是以前雷达看不到的新物体。通过将基于物理的模拟与梯度优化相结合，DiffSBR超越了数据驱动方法的局限性，开创了毫米波传感的新范式。 et.al.|[2311.13182](http://arxiv.org/abs/2311.13182)|null|
|**2023-11-21**|**Text-Guided Texturing by Synchronized Multi-View Diffusion**|本文介绍了一种在给定文本提示的情况下合成纹理来装扮给定三维对象的新方法。基于预训练的文本到图像（T2I）扩散模型，现有方法通常采用投影和修复方法，其中首先生成给定对象的视图，并将其扭曲到另一个视图进行修复。但由于多个视图的异步扩散，它往往会生成不一致的纹理。我们认为，这种异步传播和视图之间信息共享不足是不一致工件的根本原因。在本文中，我们提出了一种同步的多视图扩散方法，该方法允许来自不同视图的扩散过程在过程的早期就生成的内容达成共识，从而确保纹理的一致性。为了同步扩散，我们在每个去噪步骤中在不同的视图之间共享去噪内容，特别是从具有重叠的视图中混合纹理域中的潜在内容。与最先进的方法相比，我们的方法在生成一致、无缝、高度详细的纹理方面表现出卓越的性能。 et.al.|[2311.12891](http://arxiv.org/abs/2311.12891)|null|
|**2023-11-21**|**Physics-guided Shape-from-Template: Monocular Video Perception through Neural Surrogate Models**|动态场景的3D重建是计算机图形学中一个长期存在的问题，并且随着可用信息的减少而变得越来越困难。基于模板的形状（SfT）方法旨在从RGB图像或视频序列重建基于模板的几何体，通常只利用一个没有深度信息的单眼相机，例如常规的智能手机记录。不幸的是，现有的重建方法要么是非物理的、有噪声的，要么优化缓慢。为了解决这个问题，我们提出了一种新的布料SfT重建算法，该算法使用预先训练的神经代理模型，该模型快速评估、稳定，并且由于正则化的物理模拟而产生平滑的重建。模拟网格的可差分渲染实现了重建和目标视频序列之间的逐像素比较，该视频序列可用于基于梯度的优化过程，以不仅提取形状信息，还提取物理参数，例如布料的拉伸、剪切或弯曲刚度。与最先进的基于物理的SfT方法 $\phi$ -SfT相比，这允许保持精确、稳定和平滑的重建几何结构，同时将运行时间减少400-500倍。 et.al.|[2311.12796](http://arxiv.org/abs/2311.12796)|**[link](https://github.com/davidstotko/physics-guided-shape-from-template)**|
|**2023-11-20**|**Uncertainty Estimation in Contrast-Enhanced MR Image Translation with Multi-Axis Fusion**|近年来，深度学习已被应用于广泛的医学成像和图像处理任务。在这项工作中，我们专注于3D医学图像到图像翻译的认知不确定性的估计。我们提出了一种新的模型不确定性量化方法，即多轴融合（MAF），该方法依赖于从体积图像数据的多个视图中获得的互补信息的集成。将所提出的方法应用于基于原生T1、T2和T2-FLAIR扫描合成对比度增强的T1加权图像的任务。定量结果表明，我们的MAF方法的平均绝对图像合成误差和平均不确定度得分之间存在很强的相关性（ $\rho_｛\text health｝=0.89$ ）。因此，我们认为MAF是一种很有前途的方法，可以解决在推理时检测合成失败这一高度相关的任务。 et.al.|[2311.12153](http://arxiv.org/abs/2311.12153)|null|
|**2023-11-20**|**Mixing-Denoising Generalizable Occupancy Networks**|虽然目前最先进的可推广隐式神经形状模型依赖于卷积的归纳偏差，但仍不完全清楚从这种偏差中产生的特性如何与从点云进行3D重建的任务兼容。在这种情况下，我们探索了一种可推广性的替代方法。我们放松了固有的模型偏差（即，使用MLP来编码局部特征，而不是卷积），并用与重建任务相关的辅助正则化来约束假设空间，即去噪。所得到的模型是第一个基于点云网络的具有快速前馈推理的唯一MLP局部条件隐式形状重建。点云承载的特征和去噪偏移是在单次前向通过中从完全MLP制造的网络中预测的。解码器通过在去噪相对位置编码的指导下，从点云顺序不变地汇集附近的特征来预测空间中任何地方的查询的占用概率。我们在使用一半数量的模型参数的同时，优于最先进的卷积方法。 et.al.|[2311.12125](http://arxiv.org/abs/2311.12125)|null|
|**2023-11-20**|**PF-LRM: Pose-Free Large Reconstruction Model for Joint Pose and Shape Prediction**|我们提出了一种无姿态大型重建模型（PF-LRM），用于从一些未经处理的图像重建3D对象，即使视觉重叠很小，同时在单个A100 GPU上估计1.3秒内的相对相机姿态。PF-LRM是一种高度可扩展的方法，利用自关注块在3D对象令牌和2D图像令牌之间交换信息；我们为每个视图预测一个粗略的点云，然后使用可微分透视n-point（PnP）解算器来获得相机姿势。当在约1M个对象的大量多视图姿态数据上训练时，PF-LRM表现出强大的跨数据集泛化能力，并且在各种看不见的评估数据集上，在姿态预测精度和3D重建质量方面大大优于基线方法。我们还通过快速前馈推理证明了我们的模型在下游文本/图像到3D任务中的适用性。我们的项目网站位于：https://totoro97.github.io/pf-lrm。 et.al.|[2311.12024](http://arxiv.org/abs/2311.12024)|null|
|**2023-11-19**|**GaussianDiffusion: 3D Gaussian Splatting for Denoising Diffusion Probabilistic Models with Structured Noise**|文本到3D以其高效的生成方法和广阔的创作潜力而闻名，在AIGC领域引起了极大的关注。然而，Nerf和2D扩散模型的融合经常产生过饱和图像，由于像素绘制方法的限制，对下游工业应用造成了严重限制。高斯散射最近取代了基于NeRF的方法中流行的传统逐点采样技术，彻底改变了3D重建的各个方面。本文介绍了一种新的基于高斯飞溅的文本到3D内容生成框架，通过单个高斯球体透明度对图像饱和度进行精细控制，从而生成更逼真的图像。在三维生成中实现多视图一致性的挑战极大地阻碍了建模的复杂性和准确性。受SJC的启发，我们探索使用多视图噪声分布来干扰由3D高斯飞溅生成的图像，旨在纠正多视图几何中的不一致性。我们巧妙地设计了一种有效的方法来生成噪声，该方法从不同的角度产生高斯噪声，所有这些都源于共享的噪声源。此外，基于香草3D高斯的生成倾向于将模型困在局部极小值中，导致漂浮物、毛刺或增殖元素等伪影。为了缓解这些问题，我们提出了变分高斯飞溅技术来提高3D外观的质量和稳定性。据我们所知，我们的方法首次在整个3D内容生成过程中全面利用高斯飞溅。 et.al.|[2311.11221](http://arxiv.org/abs/2311.11221)|null|
|**2023-11-18**|**LOSTU: Fast, Scalable, and Uncertainty-Aware Triangulation**|三角测量算法通常旨在最小化重投影（ $L_2$）误差，但这仅在相机参数或相机姿态没有误差时提供最大似然估计。尽管最近的进步已经产生了估计相机参数的技术，考虑到3D点的不确定性，但大多数运动结构（SfM）管道仍然使用旧的三角测量算法。这项工作利用最近的发现，提供了一种快速、可扩展和统计优化的三角测量方法，称为LOSTU。结果表明，与传统的$L_2$ 三角测量方法相比，LOSTU始终产生较低的三维重建误差——通常允许LOSTU成功地三角测量更多的点。此外，除了提供更好的3D重建外，LOSTU可以比Levenberg-Marquardt（或类似）优化方案快得多。 et.al.|[2311.11171](http://arxiv.org/abs/2311.11171)|null|
|**2023-11-18**|**Invariant-based Mapping of Space During General Motion of an Observer**|本文探索了基于视觉运动的不变量，产生了一个新的瞬时域，其中：a）即使2D图像由于相机运动而发生连续变化，静止环境也被感知为不变，b）可以在特定的子空间中检测并潜在地避免障碍物，c）可以潜在地检测运动对象。为了实现这一点，我们使用了从可测量光流导出的非线性函数，这些函数与几何三维不变量相关联。我们展示的模拟涉及一台相对于3D对象平移和旋转的相机，捕捉相机投影图像的快照。我们表明，随着时间的推移，对象在新域中看起来没有变化。我们处理来自KITTI数据集的真实数据，并演示如何分割空间以识别自由导航区域并检测预定子空间内的障碍物。此外，我们还介绍了基于KITTI数据集的运动物体识别和分割以及形状恒定性可视化的初步结果。这种表示是直接的，依赖于用于光流的简单去旋转的函数。这种表示只需要一个相机，它是基于像素的，适合并行处理，并且它消除了3D重建技术的必要性。 et.al.|[2311.11130](http://arxiv.org/abs/2311.11130)|null|

<p align=right>(<a href=#updated-on-20231126>back to top</a>)</p>

## Diffusion

|Publish Date|Title|Abstract|PDF|Code|
|---|---|---|---|---|
|**2023-11-22**|**On diffusion-based generative models and their error bounds: The log-concave case with full convergence estimates**|在强对数凹数据分布的假设下，我们为基于扩散的生成模型的收敛行为提供了充分的理论保证，而我们用于得分估计的近似函数类是由Lipschitz连续函数组成的。我们通过一个激励性的例子，从均值未知的高斯分布中采样，证明了我们方法的强大性。在这种情况下，为相关优化问题提供显式估计，即分数近似，同时将这些估计与相应的采样估计相结合。因此，对于数据分布（具有未知平均值的高斯）和我们的采样算法之间的Wasserstein-2距离，我们获得了关于感兴趣的关键量（如维数和收敛率）的最已知的上界估计。除了激励性的例子之外，为了允许使用各种各样的随机优化器，我们使用 $L^2$ 精确的分数估计假设来呈现我们的结果，该假设关键是在对随机优化器和我们只使用已知信息的新辅助过程的期望下形成的。这种方法为我们的采样算法产生了已知的最佳收敛速度。 et.al.|[2311.13584](http://arxiv.org/abs/2311.13584)|null|
|**2023-11-22**|**WildFusion: Learning 3D-Aware Latent Diffusion Models in View Space**|现代基于学习的3D感知图像合成方法实现了生成图像的高真实感和3D一致的视点变化。现有方法表示共享规范空间中的实例。然而，对于野生数据集，共享规范系统可能很难定义，甚至可能不存在。在这项工作中，我们转而在视图空间中对实例进行建模，从而减少了对摆拍图像和学习相机分布的需求。我们发现，在这种情况下，现有的基于GAN的方法容易生成平面几何体，并且难以实现分布覆盖。因此，我们提出了WildFusion，这是一种基于潜在扩散模型（LDMs）的3D感知图像合成的新方法。我们首先训练一个自动编码器，该编码器推断出压缩的潜在表示，该编码器还捕获了图像的底层3D结构，不仅能够进行重建，还能够进行新颖的视图合成。为了学习忠实的3D表示，我们利用单目深度预测的线索。然后，我们在3D感知的潜在空间中训练扩散模型，从而能够合成高质量的3D一致图像样本，优于最近最先进的基于GAN的方法。重要的是，我们的3D感知LDM在没有来自多视点图像或3D几何结构的任何直接监督的情况下进行训练，并且不需要姿势图像或学习姿势或相机分布。它直接学习三维表示，而不依赖于规范的相机坐标。这为可扩展的3D感知图像合成和从野生图像数据创建3D内容开辟了有前景的研究途径。看见https://katjaschwarz.github.io/wildfusion我们的3D结果的视频。 et.al.|[2311.13570](http://arxiv.org/abs/2311.13570)|null|
|**2023-11-22**|**ADriver-I: A General World Model for Autonomous Driving**|通常，自动驾驶采用模块化设计，将整个堆栈分为感知、预测、规划和控制部分。尽管可以解释，但这种模块化设计往往会引入大量冗余。近年来，多模态大语言模型（MLLM）和扩散技术在理解和生成能力方面表现出了优异的性能。在本文中，我们首先引入了交错视觉-动作对的概念，它统一了视觉特征和控制信号的格式。基于视觉-动作对，我们构建了一个基于MLLM和自动驾驶扩散模型的通用世界模型，称为ADriver-I。它以视觉-动作对作为输入，并自回归预测当前帧的控制信号。所生成的控制信号与历史视觉-动作对一起被进一步调节以预测未来帧。利用预测的下一帧，ADriver-I执行进一步的控制信号预测。这样的过程可以无限重复，ADriver-I在自己创造的世界里实现了自动驾驶。在nuScenes和我们的大规模私人数据集上进行了广泛的实验。与几个构建的基线相比，ADriver-I表现出了令人印象深刻的性能。我们希望我们的ADriver-I能够为未来的自动驾驶和嵌入式智能提供一些新的见解。 et.al.|[2311.13549](http://arxiv.org/abs/2311.13549)|null|
|**2023-11-22**|**DiffusionMat: Alpha Matting as Sequential Refinement Learning**|在本文中，我们介绍了DiffusionMat，这是一种新的图像遮片框架，它采用了一个扩散模型来从粗糙的阿尔法物质过渡到精细的阿尔法物质。与传统方法不同的是，传统方法仅将三角图作为阿尔法遮片预测的松散指导，我们的方法将图像遮片视为一个顺序细化学习过程。该过程从向三分图添加噪声开始，并使用预先训练的扩散模型迭代地对其进行去噪，该模型逐渐将预测引导到干净的阿尔法遮片。我们框架的关键创新是一个校正模块，该模块在每个去噪步骤调整输出，确保最终结果与输入图像的结构一致。我们还介绍了阿尔法可靠性传播，这是一种新技术，旨在通过有信心的阿尔法信息选择性地增强三映射区域，从而简化校正任务，从而最大限度地提高可用制导的效用。为了训练校正模块，我们设计了专门的损失函数，以阿尔法遮片边缘的准确性及其不透明和透明区域的一致性为目标。我们在几个图像抠图基准上评估了我们的模型，结果表明DiffusionMat始终优于现有方法。位于~\url的项目页面{https://cnnlstm.github.io/DiffusionMat et.al.|[2311.13535](http://arxiv.org/abs/2311.13535)|null|
|**2023-11-22**|**Analysis of a multi-species Cahn-Hilliard-Keller-Segel tumor growth model with chemotaxis and angiogenesis**|我们介绍了一种用于肿瘤生长的多物种扩散界面模型，其特征是它结合了与趋化性、血管生成和增殖机制相关的基本特征。我们在一个适当的变分框架内建立了系统的弱适定性，考虑了非线性势的各种选择。这项工作的主要新颖之处之一在于通过引入精细近似方案，严格地建立了弱解的存在性。据我们所知，这代表了复杂的Cahn-Hilliard-Keller-Segel系统和具有源项的Keller-Segel子系统的一个新进展。此外，当满足特定条件时，例如具有更规则的初始数据，趋化常数相对于初始条件的大小的小条件，以及可能仅关注二维情况，我们提供了弱解的规则性结果。最后，我们导出了一个连续的依赖性估计，这反过来又导致了平滑解的唯一性，这是一个自然的结果。 et.al.|[2311.13470](http://arxiv.org/abs/2311.13470)|null|
|**2023-11-22**|**Accelerating Inference in Molecular Diffusion Models with Latent Representations of Protein Structure**|扩散生成模型已经成为解决结构生物学和基于结构的药物设计问题的强大框架。这些模型直接作用于三维分子结构。由于图神经网络（GNN）在图大小上的缩放不利，以及扩散模型固有的相对较慢的推理速度，许多现有的分子扩散模型依赖于蛋白质结构的粗粒度表示来使训练和推理变得可行。然而，这种粗粒度表示丢弃了用于建模分子相互作用的基本信息，并损害了生成结构的质量。在这项工作中，我们提出了一种新的基于GNN的结构，用于学习分子结构的潜在表征。当使用从头配体设计的扩散模型进行端到端训练时，我们的模型实现了与全原子蛋白质表示的模型相当的性能，同时显示出推理时间减少了3倍。 et.al.|[2311.13466](http://arxiv.org/abs/2311.13466)|**[link](https://github.com/dunni3/keypoint-diffusion)**|
|**2023-11-22**|**An exact bandit model for the risk-volatility tradeoff**|我们重新讨论了双臂土匪（TAB）问题，其中双臂都是由具有共同瞬时回报的扩散随机过程驱动的。我们关注的情况是，第一个臂相对于第二个臂的跃迁概率密度之间的Radon-Nikodym导数是明确已知的。我们计算了相应的Gittins指数在这种概率测度变化下的表现。该通用框架用于解决TAB问题的最优分配，其中第一个臂由纯布朗运动驱动，第二个臂由方差随时间二次增长的中心超扩散非高斯过程驱动。由于超级扩散引起的概率扩散给分配问题引入了额外的风险。这会极大地影响最优决策规则。我们的模型说明了风险和波动性概念之间的相互作用。 et.al.|[2311.13461](http://arxiv.org/abs/2311.13461)|null|
|**2023-11-22**|**Guided Flows for Generative Modeling and Decision Making**|无分类器引导是提高条件生成模型在许多下游任务中的性能的关键组成部分。它大大提高了所生产样品的质量，但迄今为止仅用于扩散模型。流匹配（FM）是一种替代的无模拟方法，它基于回归向量场训练连续归一化流（CNF）。流匹配模型是否可以执行无分类器引导，以及它在多大程度上提高了性能，这仍然是一个悬而未决的问题。在本文中，我们探讨了引导流在各种下游应用中的使用，包括条件图像生成、语音合成和强化学习。特别是，我们是第一个将流模型应用于离线强化学习环境的人。我们还表明，引导流显著提高了图像生成和零样本文本到速度合成中的样本质量，并且可以在不影响代理整体性能的情况下使用极低的计算量。 et.al.|[2311.13443](http://arxiv.org/abs/2311.13443)|null|
|**2023-11-22**|**Simultaneous uniqueness and numerical inversion for an inverse problem in the time-domain diffuse optical tomography with fluorescence**|在这项工作中，研究了由荧光时域扩散光学层析成像（DOT-FDOT）产生的多个系数的确定的反问题。通过时间相关边界测量，我们同时恢复了生物组织中背景吸收系数、光子扩散系数以及荧光吸收的分布。我们建立了这个多系数同时反问题的唯一性定理。然后，考虑了数值反演。我们介绍了一种加速Landweber迭代算法，并给出了几个数值例子来说明所提出的反演方案的性能。 et.al.|[2311.13391](http://arxiv.org/abs/2311.13391)|null|
|**2023-11-22**|**LucidDreamer: Domain-free Generation of 3D Gaussian Splatting Scenes**|随着VR设备和内容的广泛使用，对3D场景生成技术的需求变得越来越普遍。然而，现有的3D场景生成模型将目标场景限制在特定领域，主要是因为它们使用的3D扫描数据集的训练策略与现实世界相去甚远。为了解决这种局限性，我们提出了LucidDreamer，这是一种通过充分利用现有的基于大规模扩散的生成模型的力量而实现的无领域场景生成管道。我们的LucidDreamer有两个可选步骤：Dreaming和Alignment。首先，为了根据输入生成多视图一致的图像，我们将点云设置为每次图像生成的几何准则。具体来说，我们将点云的一部分投影到所需的视图，并提供投影作为使用生成模型进行修复的指导。修复后的图像被提升到具有估计深度图的3D空间，构成新的点。其次，为了将新的点聚合到3D场景中，我们提出了一种对齐算法，该算法和谐地集成了新生成的3D场景的部分。最终获得的3D场景用作优化高斯飞溅的初始点。LucidDreamer生成的高斯飞溅与以前的3D场景生成方法相比非常详细，对目标场景的域没有限制。 et.al.|[2311.13384](http://arxiv.org/abs/2311.13384)|null|

<p align=right>(<a href=#updated-on-20231126>back to top</a>)</p>

## NeRF

|Publish Date|Title|Abstract|PDF|Code|
|---|---|---|---|---|
|**2023-11-21**|**3D Compression Using Neural Fields**|神经场（NFs）作为一种压缩各种数据模式的工具，如图像和视频，已经获得了发展势头。这项工作利用了以前的进展，并提出了一种新的基于NF的3D数据压缩算法。我们推导出了两个版本的方法——一个是基于有符号距离域（SDF）的水密形状，另一个是使用无符号距离场（UDF）的任意非水密形状。我们证明了我们的方法在三维点云和网格上的几何压缩方面表现出色。此外，我们表明，由于NF公式，可以直接扩展我们的压缩算法来压缩3D数据的几何结构和属性（例如颜色）。 et.al.|[2311.13009](http://arxiv.org/abs/2311.13009)|null|
|**2023-11-20**|**NePF: Neural Photon Field for Single-Stage Inverse Rendering**|我们提出了一种新的单级框架——神经光子场（NePF），以解决多视图图像的不适定逆绘制问题。与以前在多个阶段恢复几何、材料和照明并从不同神经场的各种多层感知器中提取特性的方法相反，我们质疑这种复杂性，并介绍了我们的方法-一个统一恢复所有特性的单阶段框架。NePF通过充分利用神经隐式曲面的权重函数背后的物理含义和与视图相关的辐射来实现这种统一。此外，我们还介绍了一种创新的基于坐标的照明模型，用于快速基于体积的物理渲染。为了正则化这种照明，我们实现了用于散射估计的次表面散射模型。我们在真实数据集和合成数据集上评估了我们的方法。结果证明了我们的方法在恢复高保真几何和视觉上合理的材料属性方面的优越性。 et.al.|[2311.11555](http://arxiv.org/abs/2311.11555)|null|
|**2023-11-15**|**RENI++ A Rotation-Equivariant, Scale-Invariant, Natural Illumination Prior**|反向渲染是一个不适定的问题。以前的工作试图通过关注对象或场景形状或外观的先验来解决这个问题。在这项工作中，我们转而关注自然照明的先验。目前的方法依赖于球面谐波照明或其他通用表示，充其量，依赖于参数的简单化先验。这导致在照明条件的表现力方面对反向设置的限制，尤其是在考虑镜面反射时。我们提出了一种基于变分自动解码器和变换器解码器的条件神经场表示。我们扩展了矢量神经元，将等方差直接构建到我们的架构中，并通过尺度不变损失函数利用深度估计的见解，实现了高动态范围（HDR）图像的精确表示。其结果是一个紧凑的、旋转等变的HDR神经照明模型，能够捕捉自然环境地图中复杂的高频特征。在一个由1.6K HDR自然场景环境图组成的精心策划的数据集上训练我们的模型，我们将其与传统表示进行比较，证明其适用于反向渲染任务，并显示部分观测的环境图完成情况。我们在https://github.com/JADGardner/ns_reni et.al.|[2311.09361](http://arxiv.org/abs/2311.09361)|**[link](https://github.com/jadgardner/ns_reni)**|
|**2023-11-15**|**Data Augmentations in Deep Weight Spaces**|在权重空间中学习，神经网络处理其他深度神经网络的权重，已成为一个很有前途的研究方向，在各个领域都有应用，从分析和编辑神经领域和隐式神经表示，到网络修剪和量化。最近的工作设计了在该空间中进行有效学习的架构，考虑到了其独特的置换等变结构。不幸的是，到目前为止，这些架构存在严重的过拟合问题，并被证明受益于大型数据集。这带来了重大挑战，因为为这种学习设置生成数据既费力又耗时，因为每个数据样本都是必须训练的一整套网络权重。在本文中，我们通过研究权重空间的数据增强来解决这一困难，这是一组能够在不需要训练额外输入权重空间元素的情况下实时生成新数据示例的技术。我们首先回顾了最近提出的几个数据增强方案%，并将其分为几类。然后，我们介绍了一种新的基于Mixup方法的增强方案。我们评估了这些技术在现有基准以及我们生成的新基准上的性能，这对未来的研究很有价值。 et.al.|[2311.08851](http://arxiv.org/abs/2311.08851)|null|
|**2023-11-14**|**Instant3D: Instant Text-to-3D Generation**|文本到三维生成，旨在通过文本提示合成生动的三维对象，引起了计算机视觉界的广泛关注。虽然已有的几项工作在这项任务上取得了令人印象深刻的成果，但它们主要依赖于耗时的优化范式。具体来说，这些方法为每个文本提示从头开始优化神经场，生成一个对象大约需要一个小时或更长时间。这种繁重和重复的培训成本阻碍了他们的实际部署。在本文中，我们提出了一种新的快速文本到三维生成框架，称为Instant3D。一旦经过训练，Instant3D就能够通过一次前馈网络运行，在不到一秒钟的时间内为看不见的文本提示创建一个3D对象。我们通过设计一个新的网络来实现这一惊人的速度，该网络直接从文本提示构建3D三平面。我们的Instant3D的核心创新在于探索将文本条件有效地注入网络的策略。此外，我们提出了一种简单而有效的激活函数，即缩放的sigmoid函数，以取代原始的sigmoid函数，它将训练收敛速度提高了十倍以上。最后，为了解决3D生成中的Janus（多头）问题，我们提出了一种自适应Perp-Neg算法，该算法可以在训练过程中根据Janus问题的严重程度动态调整其概念否定量表，有效地降低了多头效应。在各种基准数据集上进行的大量实验表明，所提出的算法在质量和数量上都优于最先进的方法，同时实现了显著更好的效率。项目页面位于https://ming1993li.github.io/Instant3DProj. et.al.|[2311.08403](http://arxiv.org/abs/2311.08403)|null|
|**2023-11-13**|**On the mathematical replication of the MacKay effect from redundant stimulation**|在这项研究中，我们研究了视觉感知与初级视觉皮层（V1）神经活动的数学建模之间的复杂联系，重点是复制麦凯效应[MacKay，Nature 1957]。虽然分叉理论一直是解决神经科学问题的一种突出的数学方法，特别是在描述V1中由于参数变化而自发形成的模式时，它在具有局部感觉输入的场景中面临挑战。例如，这一点在麦凯的心理物理学实验中很明显，在该实验中，视觉刺激信息的冗余导致了不规则的形状，使分叉理论和多尺度分析的效果较差。为了解决这个问题，我们遵循了一个基于Amari型神经场模型的输入输出可控性的数学观点。该框架将感觉输入视为一种控制功能，通过视觉刺激的视网膜-皮层图进行皮层表征，捕捉刺激的不同特征，特别是麦凯漏斗模式“麦凯射线”中的中心冗余。从控制理论的角度，讨论了Amari型方程对于线性和非线性响应函数的精确可控性。然后，应用于麦凯效应复制，我们调整了表示神经元内连接的参数，以确保在没有感觉输入的情况下，皮层活动指数稳定到静止状态，我们进行了定量和定性研究，以表明它捕捉到了麦凯报告的诱导后图像的所有基本特征 et.al.|[2311.07338](http://arxiv.org/abs/2311.07338)|null|
|**2023-11-10**|**Improved Positional Encoding for Implicit Neural Representation based Compact Data Representation**|采用位置编码来捕获隐式神经表示（INR）中编码信号的高频信息。在本文中，我们提出了一种新的位置编码方法，该方法提高了INR的重建质量。所提出的嵌入方法对于紧凑的数据表示更有利，因为它比现有方法具有更多的频率基。我们的实验表明，该方法在压缩任务中没有引入任何额外的复杂性，并且在新的视图合成中具有更高的重建质量，从而在率失真性能上获得了显著的增益。 et.al.|[2311.06059](http://arxiv.org/abs/2311.06059)|null|
|**2023-11-09**|**BakedAvatar: Baking Neural Fields for Real-Time Head Avatar Synthesis**|从视频中合成逼真的4D人头头像对于VR/AR、远程呈现和视频游戏应用至关重要。尽管现有的基于神经辐射场（NeRF）的方法实现了高保真度的结果，但计算费用限制了它们在实时应用中的使用。为了克服这一限制，我们引入了BakedAvatar，这是一种用于实时神经头部化身合成的新表示，可部署在标准多边形光栅化管道中。我们的方法从学习的头部等值面中提取可变形的多层网格，并计算与表情、姿势和视图相关的外观，这些外观可以烘焙到静态纹理中，以实现高效的光栅化。因此，我们提出了一种用于神经头化身合成的三阶段流水线，包括学习连续变形、流形和辐射场，提取分层网格和纹理，以及使用差分光栅化微调纹理细节。实验结果表明，我们的表示生成的合成结果质量与其他最先进的方法相当，同时显著减少了所需的推理时间。我们进一步展示了单眼视频中的各种头部化身合成结果，包括视图合成、面部再现、表情编辑和姿势编辑，所有这些都是以交互式帧率进行的。 et.al.|[2311.05521](http://arxiv.org/abs/2311.05521)|null|
|**2023-11-08**|**Learning Robust Multi-Scale Representation for Neural Radiance Fields from Unposed Images**|我们介绍了一种改进的计算机视觉中基于神经图像的绘制问题的解决方案。给定一组在火车时刻从自由移动的相机拍摄的图像，所提出的方法可以在测试时刻从一个新颖的视角合成真实的场景图像。本文提出的关键思想是：（i）在神经新视图合成问题中，通过稳健的管道从未处理的日常图像中恢复准确的相机参数同样至关重要；（ii）以不同的分辨率对对象的内容进行建模更为实用，因为在日常的未渲染图像中，相机的剧烈运动极有可能发生。为了结合这些关键思想，我们利用了场景刚性、多尺度神经场景表示和单图像深度预测的基本原理。具体地说，所提出的方法使相机参数在基于神经场的建模框架中是可学习的。通过假设每个视图的深度预测是按比例进行的，我们限制了连续帧之间的相对姿态。根据相对姿态，通过多尺度神经场网络内的基于图神经网络的多运动平均来建模绝对相机姿态估计，从而产生单个损失函数。优化引入的损失函数提供了相机内在的、外在的以及从未聚焦的图像渲染的图像。我们通过例子证明，对于从日常获取的未聚焦多视图图像中精确建模多尺度神经场景表示的统一框架，在场景表示框架内进行精确的相机姿态估计同样重要。如果不考虑相机姿态估计管道中的鲁棒性措施，对多尺度混叠伪影进行建模可能会适得其反。我们在几个基准数据集上进行了大量实验，以证明我们的方法的适用性。 et.al.|[2311.04521](http://arxiv.org/abs/2311.04521)|null|
|**2023-11-06**|**Dynamic Neural Fields for Learning Atlases of 4D Fetal MRI Time-series**|我们提出了一种使用神经场快速构建生物医学图像图谱的方法。图谱是生物医学图像分析任务的关键，但传统的深度网络估计方法仍然耗时。在这项初步工作中，我们将特定主题的图谱构建框定为学习可变形时空观测的神经场。我们将我们的方法应用于学习子宫内胎儿动态BOLD MRI时间序列的受试者特异性图谱和运动稳定性。我们的方法产生了胎儿BOLD时间序列的高质量图谱，与现有工作相比，收敛速度更快。虽然我们的方法在解剖重叠方面稍逊于调整良好的基线，但它估计模板的速度要快得多，从而能够快速处理和稳定4D动态MRI采集的大型数据库。代码可在https://github.com/Kidrauh/neural-atlasing et.al.|[2311.02874](http://arxiv.org/abs/2311.02874)|**[link](https://github.com/kidrauh/neural-atlasing)**|

<p align=right>(<a href=#updated-on-20231126>back to top</a>)</p>

[contributors-shield]: https://img.shields.io/github/contributors/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[contributors-url]: https://github.com/Vincentqyw/cv-arxiv-daily/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[forks-url]: https://github.com/Vincentqyw/cv-arxiv-daily/network/members
[stars-shield]: https://img.shields.io/github/stars/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[stars-url]: https://github.com/Vincentqyw/cv-arxiv-daily/stargazers
[issues-shield]: https://img.shields.io/github/issues/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[issues-url]: https://github.com/Vincentqyw/cv-arxiv-daily/issues

