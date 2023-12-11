[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]

## Updated on 2023.12.11
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
|**2023-12-08**|**MuVieCAST: Multi-View Consistent Artistic Style Transfer**|我们介绍了MuVieCAST，这是一种模块化多视图一致风格传输网络架构，可实现同一场景的多个视点之间的一致风格传输。这种网络架构同时支持稀疏视图和密集视图，使其具有足够的通用性，可以处理广泛的多视图图像数据集。该方法由三个模块组成，它们执行与风格传递相关的特定任务，即内容保存、图像转换和多视图一致性强制执行。我们在多个应用领域广泛评估了我们的方法，包括基于深度图的点云融合、网格重建和新颖的视图合成。我们的实验表明，所提出的框架实现了风格化图像的特殊生成，在不同视角下表现出一致的结果。一项专注于新视图合成的用户研究进一步证实了这些结果，与最近最先进的方法相比，大约68%的案例参与者表示更喜欢我们生成的输出。我们的模块化框架是可扩展的，可以很容易地与各种主干架构集成，使其成为多视图风格传输的灵活解决方案。更多结果在我们的项目页面上展示：muviecast.github.io et.al.|[2312.05046](http://arxiv.org/abs/2312.05046)|null|
|**2023-12-07**|**MuRF: Multi-Baseline Radiance Fields**|我们提出了多基线辐射场（MuRF），这是一种通用的前馈方法，用于解决多个不同基线设置（小基线和大基线，以及不同数量的输入视图）下的稀疏视图合成问题。为了渲染目标新视图，我们将3D空间离散为平行于目标图像平面的平面，并相应地构建目标视图截头体。这样的目标体积表示与目标视图在空间上对齐，这有效地聚集了来自输入视图的相关信息以进行高质量渲染。由于其轴对齐性质，它还便于随后使用卷积网络进行辐射场回归。卷积网络建模的3D上下文使我们的方法能够合成比先前工作更清晰的场景结构。我们的MuRF在从简单物体（DTU）到复杂室内外场景（RealEstate10K和LLFF）的多种不同基线设置和不同场景中实现了最先进的性能。我们还在Mip-NeRF 360数据集上展示了有前景的零样本泛化能力，证明了MuRF的普遍适用性。 et.al.|[2312.04565](http://arxiv.org/abs/2312.04565)|**[link](https://github.com/autonomousvision/murf)**|
|**2023-12-07**|**Free3D: Consistent Novel View Synthesis without 3D Representation**|我们介绍了Free3D，这是一种用于从单个图像进行开集新视图合成（NVS）的简单方法。与Zero-1-to-3类似，我们从预先训练的2D图像生成器开始进行泛化，并对其进行NVS微调。与最近和同时进行的工作相比，我们在不使用显式3D表示的情况下获得了显著的改进，这是缓慢的、消耗内存的或训练额外的3D网络。我们通过新的每像素光线调节归一化（RCN）层对目标相机姿态进行更好的编码来实现这一点。后者通过告诉每个像素其特定的观看方向，在底层2D图像生成器中注入姿势信息。我们还通过轻量级的多视图注意力层和多视图噪声共享来提高多视图一致性。我们在Ob厌恶数据集上训练Free3D，并在包括OminiObject3D和GSO在内的几个新数据集中展示了对各种新类别的出色概括。我们希望我们简单有效的方法将成为一个坚实的基线，并有助于未来以更准确的姿态进行NVS研究。项目页面位于https://chuanxiaz.com/free3d/. et.al.|[2312.04551](http://arxiv.org/abs/2312.04551)|**[link](https://github.com/lyndonzheng/Free3D)**|
|**2023-12-07**|**Multi-View Unsupervised Image Generation with Cross Attention Guidance**|在神经辐射场（NeRF）模型的驱动下，人们对新视图合成越来越感兴趣，但由于它们依赖于精确注释的多视图图像，因此受到可扩展性问题的阻碍。最近的模型通过在合成多视图数据上微调大文本2图像扩散模型来解决这一问题。尽管有强大的零样本泛化，但它们可能需要后处理，并可能由于合成域间隙而面临质量问题。本文介绍了一种新的流水线，用于在单类别数据集上对姿态条件扩散模型进行无监督训练。在预训练的自监督视觉变换器（DINOv2）的帮助下，我们通过比较特定对象部分的可见性和位置来对数据集进行聚类，从而识别对象姿态。在姿势标签上训练并在推理时配备跨帧注意力的姿势条件扩散模型确保了跨视图的一致性，这进一步得益于我们新颖的硬注意力引导。我们的模型，MIRAGE，在真实图像的新颖视图合成方面超越了以往的工作。此外，正如我们在使用预训练的稳定扩散生成的合成图像上的实验所证明的那样，MIRAGE对不同的纹理和几何形状是鲁棒的。 et.al.|[2312.04337](http://arxiv.org/abs/2312.04337)|null|
|**2023-12-07**|**Towards 4D Human Video Stylization**|我们向4D（3D和时间）人类视频风格化迈出了第一步，它在一个统一的框架内解决了风格转换、新颖的视图合成和人类动画。虽然已经开发了许多视频风格化方法，但它们往往局限于在输入视频的特定视点中渲染图像，缺乏在动态场景中推广到新颖视图和新颖姿势的能力。为了克服这些限制，我们利用神经辐射场（NeRF）来表示视频，在渲染的特征空间中进行风格化。我们的创新方法包括使用两个NeRF同时表示人类主体和周围场景。这种双重表现促进了人类主体在各种姿势和新颖视角下的动画化。具体来说，我们引入了一种新的几何引导的三平面表示，与直接三平面优化相比，显著增强了特征表示的鲁棒性。在视频重建之后，在NeRF的渲染特征空间内执行风格化。大量实验表明，所提出的方法在风格化纹理和时间连贯性之间取得了卓越的平衡，超过了现有的方法。此外，我们的框架独特地扩展了其功能，以适应新颖的姿势和视角，使其成为创造性人类视频风格化的多功能工具。 et.al.|[2312.04143](http://arxiv.org/abs/2312.04143)|**[link](https://github.com/tiantianwang/4d_video_stylization)**|
|**2023-12-06**|**DreamComposer: Controllable 3D Object Generation via Multi-View Conditions**|利用预先训练的2D大规模生成模型，最近的工作能够从单个野生图像中生成高质量的新视图。然而，由于缺乏来自多个视角的信息，这些作品在生成可控的小说视角方面遇到了困难。在本文中，我们提出了DreamComposer，这是一个灵活且可扩展的框架，可以通过注入多视图条件来增强现有的视图感知扩散模型。具体而言，DreamComposer首先使用视图感知三维提升模块从多个视图中获得对象的三维表示。然后，利用多视图特征融合模块从三维表示中提取目标视图的潜在特征。最后，将从多视图输入中提取的目标视图特征注入到预先训练的扩散模型中。实验表明，DreamComposer与用于零样本新视图合成的最先进的扩散模型兼容，进一步增强了它们以生成具有多视图条件的高保真度新视图图像，为可控3D对象重建和各种其他应用做好了准备。 et.al.|[2312.03611](http://arxiv.org/abs/2312.03611)|null|
|**2023-12-06**|**Artist-Friendly Relightable and Animatable Neural Heads**|创建照片逼真数字化身的一种越来越常见的方法是通过使用体积神经场。当在一组多视图图像上训练时，原始神经辐射场（NeRF）允许静态头部进行令人印象深刻的新颖视图合成，后续方法表明，这些神经表示可以扩展到动态化身。最近，新的变体也超过了神经表示中烘焙照明的常见缺点，表明静态神经化身可以在任何环境中重新发光。在这项工作中，我们同时解决了运动和照明问题，为可重新照明和可动画化的神经头提出了一种新方法。我们的方法建立在一种已验证的动态化身方法的基础上，该方法基于体积基元的混合，结合最近提出的用于可重新照明神经场的轻量级硬件设置，并包括一种新的架构，该架构允许重新照明动态神经化身在任何环境中执行看不见的表情，即使是在近场照明和视点的情况下。 et.al.|[2312.03420](http://arxiv.org/abs/2312.03420)|null|
|**2023-12-06**|**RING-NeRF: A Versatile Architecture based on Residual Implicit Neural Grids**|自引入以来，神经场在三维重建和新视图合成方面变得非常流行。最近的研究集中在加速这一过程，以及提高对观测距离和有限监督视点数量变化的鲁棒性。然而，这些方法往往导致无法轻易结合的专门解决方案。为了解决这个问题，我们引入了一种新的简单但高效的架构，称为RING-NeRF，基于残差隐式神经网格，它提供了对场景和潜在空间之间映射函数的细节级别的控制。与距离感知的前向映射机制和连续的从粗到细的重建过程相关联，我们的多功能架构在以下方面展示了快速训练和最先进的性能：（1）抗混叠渲染，（2）从很少监督的视点的重建质量，以及（3）对于基于SDF的NeRF在没有适当的场景特定初始化的情况下的鲁棒性。我们还证明了我们的架构可以动态添加网格来增加重建的细节，为自适应重建开辟了道路。 et.al.|[2312.03357](http://arxiv.org/abs/2312.03357)|null|
|**2023-12-06**|**Feature 3DGS: Supercharging 3D Gaussian Splatting to Enable Distilled Feature Fields**|近年来，3D场景表示已经获得了巨大的普及。使用神经辐射场的方法适用于传统任务，如新颖的视图合成。近年来，出现了一些工作，旨在将NeRF的功能扩展到视图合成之外，用于语义感知任务，如使用2D基础模型中的3D特征场提取进行编辑和分割。然而，这些方法有两个主要的局限性：（a）它们受到NeRF管道的渲染速度的限制，以及（b）隐式表示的特征场受到连续性伪影的影响，从而降低了特征质量。最近，3D高斯散射在实时辐射场渲染方面表现出了最先进的性能。在这项工作中，我们更进一步：除了辐射场渲染外，我们还通过2D基础模型蒸馏实现了对任意维度语义特征的3D高斯飞溅。这种转换并不简单：天真地将特征字段合并到3DGS框架中会导致扭曲级别的差异。我们建议对架构和培训进行更改，以有效地避免此问题。我们提出的方法是通用的，我们的实验展示了新颖的视图语义分割、语言引导编辑和通过从最先进的2D基础模型（如SAM和CLIP-LSeg）中学习特征字段来分割任何内容。在整个实验中，我们的蒸馏方法能够提供类似或更好的结果，同时训练和渲染速度明显更快。此外，据我们所知，我们是第一个通过利用SAM模型启用点和边界框提示进行辐射场操作的方法。项目网站：https://feature-3dgs.github.io/ et.al.|[2312.03203](http://arxiv.org/abs/2312.03203)|null|
|**2023-12-05**|**HybridNeRF: Efficient Neural Rendering via Adaptive Volumetric Surfaces**|神经辐射场提供了最先进的视图合成质量，但渲染速度往往较慢。一个原因是它们使用体积渲染，因此在渲染时每条光线需要许多采样（和模型查询）。尽管这种表示方式灵活且易于优化，但大多数真实世界的对象都可以使用曲面而不是体积更有效地建模，因此每条射线所需的采样数要少得多。这一观察结果促使表面表示（如符号距离函数）取得了相当大的进展，但这些方法可能难以对半透明和薄结构进行建模。我们提出了一种名为HybridNeRF的方法，该方法通过将大多数对象渲染为曲面，同时对（通常）一小部分具有挑战性的区域进行体积建模，来利用这两种表示的优势。我们针对具有挑战性的Eyeful Tower数据集以及其他常用的视图合成数据集对HybridNeRF进行了评估。与最先进的基线（包括最近的基于光栅化的方法）相比，我们将错误率提高了15-30%，同时实现了虚拟现实分辨率（2Kx2K）的实时帧速率（至少36 FPS）。 et.al.|[2312.03160](http://arxiv.org/abs/2312.03160)|null|

<p align=right>(<a href=#updated-on-20231211>back to top</a>)</p>

## 3D Reconstruction

|Publish Date|Title|Abstract|PDF|Code|
|---|---|---|---|---|
|**2023-12-08**|**Fine Dense Alignment of Image Bursts through Camera Pose and Depth Estimation**|本文介绍了一种新的方法来对手持相机拍摄的突发图像进行精细对准。与估计帧对之间的二维变换或依赖于离散对应关系的传统技术相比，所提出的算法通过优化每个像素的相机运动和表面深度和方向来建立密集的对应关系。这种方法改进了对齐，特别是在具有视差挑战的场景中。以小基线甚至微小基线为特征的合成爆发的广泛实验表明，在这种情况下，它的性能优于目前可用的最佳光流方法，而不需要任何训练。除了增强对齐之外，我们的方法还为简单图像恢复之外的任务开辟了途径，如深度估计和3D重建，这得到了有希望的初步结果的支持。这将我们的方法定位为用于各种突发图像处理应用的通用工具。 et.al.|[2312.05190](http://arxiv.org/abs/2312.05190)|null|
|**2023-12-08**|**SuperNormal: Neural Surface Reconstruction via Multi-View Normal Integration**|我们介绍了SuperNormal，这是一种使用曲面法线贴图进行多视图三维重建的快速高保真方法。只需几分钟，SuperNormal就可以生成与3D扫描仪不相上下的详细曲面。我们利用体绘制来优化由多分辨率哈希编码提供支持的神经符号距离函数（SDF）。为了加速训练，我们提出了方向有限差分和基于补丁的射线行进来数值逼近SDF梯度。在不影响重建质量的同时，该策略的效率几乎是分析梯度的两倍，比轴对齐有限差分快约三倍。在基准数据集上的实验表明，与现有的多视图光度立体方法相比，SuperNormal在效率和准确性方面具有优势。在我们捕获的对象上，SuperNormal比最近的神经3D重建方法产生了更细粒度的几何体。 et.al.|[2312.04803](http://arxiv.org/abs/2312.04803)|null|
|**2023-12-07**|**FitDiff: Robust monocular 3D facial shape and reflectance estimation using Diffusion Models**|三维人脸重建的显著进展已经产生了高细节和逼真的人脸表示。最近，扩散模型实现了比GANs更好的性能，从而彻底改变了生成方法的能力。在这项工作中，我们提出了FitDiff，一个基于扩散的三维人脸化身生成模型。该模型利用从“野外”2D面部图像中提取的身份嵌入，准确地生成可重新点亮的面部化身。我们的多模式漫射模型同时输出面部反射率图（漫射和镜面反照率和法线）和形状，显示出强大的泛化能力。它只在公共面部数据集的注释子集上进行训练，并与3D重建相结合。我们通过使用感知和人脸识别损失来引导反向扩散过程，重新审视典型的3D人脸拟合方法。FitDiff是第一个以人脸识别嵌入为条件的LDM，它重建了可重新照明的人类化身，可以像在普通渲染引擎中一样使用，只从不受约束的面部图像开始，并实现了最先进的性能。 et.al.|[2312.04465](http://arxiv.org/abs/2312.04465)|null|
|**2023-12-07**|**Cascade-Zero123: One Image to Highly Consistent 3D with Self-Prompted Nearby Views**|从单个图像合成多视图3D是一项重要而富有挑战性的任务。为此，Zero-1-to-3方法旨在将2D潜在扩散模型扩展到3D范围。这些方法生成具有单个视点图像和相机姿态作为条件信息的目标视点图像。然而，Zero-1-to-3中采用的一对一方式给在视图之间建立几何和视觉一致性带来了挑战，尤其是对于复杂对象。为了解决这个问题，我们提出了一个由两个Zero-1-to-3模型构建的级联生成框架，称为cascade-Zero123，该框架从源图像中逐步提取3D信息。具体而言，设计了一种自提示机制，用于首先生成几个附近的视图。然后将这些视图与源图像一起作为生成条件馈送到第二阶段模型中。以自我提示的多个视图作为补充信息，我们的Cascade-Zero123生成了比Zero-1-3更高度一致的新视图图像。该促销活动对各种复杂和具有挑战性的场景具有重要意义，包括昆虫、人类、透明物体和堆叠的多个物体等。项目页面位于https://cascadezero123.github.io/. et.al.|[2312.04424](http://arxiv.org/abs/2312.04424)|null|
|**2023-12-06**|**DreamComposer: Controllable 3D Object Generation via Multi-View Conditions**|利用预先训练的2D大规模生成模型，最近的工作能够从单个野生图像中生成高质量的新视图。然而，由于缺乏来自多个视角的信息，这些作品在生成可控的小说视角方面遇到了困难。在本文中，我们提出了DreamComposer，这是一个灵活且可扩展的框架，可以通过注入多视图条件来增强现有的视图感知扩散模型。具体而言，DreamComposer首先使用视图感知三维提升模块从多个视图中获得对象的三维表示。然后，利用多视图特征融合模块从三维表示中提取目标视图的潜在特征。最后，将从多视图输入中提取的目标视图特征注入到预先训练的扩散模型中。实验表明，DreamComposer与用于零样本新视图合成的最先进的扩散模型兼容，进一步增强了它们以生成具有多视图条件的高保真度新视图图像，为可控3D对象重建和各种其他应用做好了准备。 et.al.|[2312.03611](http://arxiv.org/abs/2312.03611)|null|
|**2023-12-06**|**Gaussian-Flow: 4D Reconstruction with Dynamic 3D Gaussian Particle**|我们介绍了高斯流，这是一种新的基于点的方法，用于快速动态场景重建和多视图和单目视频的实时渲染。与因训练和渲染速度缓慢而受到阻碍的流行的基于NeRF的方法相比，我们的方法利用了基于点的3D高斯散射（3DGS）的最新进展。具体而言，提出了一种新的双域变形模型（DDDM）来显式地对每个高斯点的属性变形进行建模，其中通过时域中的多项式拟合和频域中的傅立叶级数拟合来捕获每个属性的时间相关残差。所提出的DDDM能够对长视频镜头中的复杂场景变形进行建模，消除了为每帧训练单独的3DGS的需要，或者引入了额外的隐式神经场来对3D动力学进行建模。此外，离散高斯点的显式变形建模确保了4D场景的超快速训练和渲染，这与为静态3D重建设计的原始3DGS相当。我们提出的方法展示了显著的效率提高，与每帧3DGS建模相比，训练速度快了5倍。此外，定量结果表明，所提出的高斯流在新视图渲染质量方面显著优于以前的主流方法。项目页面：https://nju-3dv.github.io/projects/gaussian-flow et.al.|[2312.03431](http://arxiv.org/abs/2312.03431)|null|
|**2023-12-06**|**Evaluating the point cloud of individual trees generated from images based on Neural Radiance fields (NeRF) method**|树木的三维重建一直是林业精确管理和研究的关键任务。由于树木本身的树枝形态结构复杂，以及树干、树枝和树叶的遮挡，传统的摄影测量方法很难从二维图像中重建完整的三维树木模型。在本研究中，基于各种相机以不同方式收集的树木图像，将神经辐射场（NeRF）方法用于单个树木的重建，并将导出的点云模型与摄影测量重建和激光扫描方法获得的点云进行比较。结果表明，NeRF方法在单株树木三维重建中表现良好，重建成功率较高，在树冠区域重建效果较好，所需图像量较少。与摄影测量重建方法相比，NeRF在重建效率上具有显著优势，适用于复杂场景，但生成的点云往往具有噪声大、分辨率低的特点。从摄影测量点云中提取的树木结构参数（树高和胸径）的精度仍然高于从NeRF点云中导出的精度。该研究结果说明了NeRF方法在个体树木重建方面的巨大潜力，为复杂森林场景的三维重建和可视化提供了新的思路和研究方向。 et.al.|[2312.03372](http://arxiv.org/abs/2312.03372)|null|
|**2023-12-06**|**RING-NeRF: A Versatile Architecture based on Residual Implicit Neural Grids**|自引入以来，神经场在三维重建和新视图合成方面变得非常流行。最近的研究集中在加速这一过程，以及提高对观测距离和有限监督视点数量变化的鲁棒性。然而，这些方法往往导致无法轻易结合的专门解决方案。为了解决这个问题，我们引入了一种新的简单但高效的架构，称为RING-NeRF，基于残差隐式神经网格，它提供了对场景和潜在空间之间映射函数的细节级别的控制。与距离感知的前向映射机制和连续的从粗到细的重建过程相关联，我们的多功能架构在以下方面展示了快速训练和最先进的性能：（1）抗混叠渲染，（2）从很少监督的视点的重建质量，以及（3）对于基于SDF的NeRF在没有适当的场景特定初始化的情况下的鲁棒性。我们还证明了我们的架构可以动态添加网格来增加重建的细节，为自适应重建开辟了道路。 et.al.|[2312.03357](http://arxiv.org/abs/2312.03357)|null|
|**2023-12-06**|**Bile Duct Segmentation Methods Under 3D Slicer Applied to ERCP: Advantages and Disadvantages**|本文对用于3D重建的胆道分割方法进行了评估，该方法在各种关键干预措施中可能非常有用，如使用3D Slicer软件的内镜逆行胰胆管造影（ERCP）。本文对用于3D重建的胆道分割技术进行了评估，通过使用3D Slicer软件，该技术在内镜逆行胰胆管造影（ERCP）等各种关键程序中具有很高的价值。评估了三种不同的方法，即阈值法、洪水填充法和区域增长法的优缺点。该研究涉及10个患者病例，并采用定量指标和定性评估来评估不同分割方法获得的分割结果。结果表明，阈值法几乎是手动的且耗时，而洪水填充法是半自动的且耗时。尽管这两种方法都提高了分割质量，但它们是不可重复的。因此，开发了一种基于区域生长的自动方法来减少分割时间，尽管这是以牺牲质量为代价的。这些发现突出了不同传统分割方法的优缺点，并强调了探索替代方法的必要性，如深度学习，以优化ERCP背景下的胆道分割。 et.al.|[2312.03356](http://arxiv.org/abs/2312.03356)|null|
|**2023-12-05**|**Fully Convolutional Slice-to-Volume Reconstruction for Single-Stack MRI**|在磁共振成像（MRI）中，片体积重建（SVR）是指从被运动破坏的2D片堆中计算重建未知的3D磁共振体积。虽然很有前景，但目前的SVR方法需要多个切片堆栈来进行精确的3D重建，这导致了长扫描，并限制了它们在胎儿功能磁共振成像等时间敏感应用中的使用。在这里，我们提出了一种SVR方法，该方法克服了先前工作的缺点，并在存在极端片间运动的情况下产生了最先进的重建。受最近单视图深度估计方法成功的启发，我们将SVR公式化为单堆栈运动估计任务，并训练全卷积网络来预测给定切片堆栈的运动堆栈，从而产生3D重建作为预测运动的副产品。对成人和胎儿大脑的SVR进行的广泛实验表明，我们的全卷积方法的准确性是以前的SVR方法的两倍。我们的代码可在github.com/seannz/svr上获得。 et.al.|[2312.03102](http://arxiv.org/abs/2312.03102)|null|

<p align=right>(<a href=#updated-on-20231211>back to top</a>)</p>

## Diffusion

|Publish Date|Title|Abstract|PDF|Code|
|---|---|---|---|---|
|**2023-12-08**|**KBFormer: A Diffusion Model for Structured Entity Completion**|我们开发了一种基于生成注意力的方法来建模包括不同属性类型的结构化实体，如数字、分类、字符串和复合。这种方法通过特性上的混合连续离散扩散过程来处理这种异构数据。我们灵活的框架可以为具有任意层次属性的实体建模，使应用程序能够结构化知识库（KB）实体和表格数据。我们的方法在15个数据集的大多数情况下都获得了最先进的性能。此外，使用设备KB和核物理数据集进行的实验证明了该模型在不同环境中学习对实体完成有用的表示的能力。这有许多下游用例，包括高精度的数值特性建模，这对科学应用至关重要，也得益于模型固有的概率性。 et.al.|[2312.05253](http://arxiv.org/abs/2312.05253)|null|
|**2023-12-08**|**SwiftBrush: One-Step Text-to-Image Diffusion Model with Variational Score Distillation**|尽管文本到图像扩散模型能够根据文本提示生成高分辨率和多样化的图像，但它们往往会经历缓慢的迭代采样过程。模型蒸馏是加速这些模型的最有效的方向之一。然而，以前的提取方法无法保持生成质量，同时需要大量的图像进行训练，无论是来自真实数据还是由教师模型综合生成。针对这一限制，我们提出了一种新的无图像蒸馏方案，命名为 $\textbf{SwiftBrush}$。从文本到三维合成中获得灵感，在该合成中，可以通过专门的损失从2D文本到图像的扩散中获得与输入提示一致的3D神经辐射场，而无需使用任何3D数据基础事实，我们的方法将相同的损失重新用于提取预训练的多步骤文本到图像模型，从而使学生网络只需一个推理步骤即可生成高保真图像。尽管它很简单，但我们的模型是第一个一步文本到图像生成器之一，它可以在不依赖任何训练图像数据的情况下生成与稳定扩散质量相当的图像。值得注意的是，SwiftBrush在COCO-30K基准上获得了$\textbf｛16.67｝$的FID分数和$ \textbf｛0.29｝美元的CLIP分数，取得了有竞争力的结果，甚至大大超过了现有的最先进的蒸馏技术。 et.al.|[2312.05239](http://arxiv.org/abs/2312.05239)|null|
|**2023-12-08**|**Stoichiometry preservation and generalization of Bilger mixture fraction for non-premixed combustion with differential molecular diffusion**|当考虑微分分子扩散时，Bilger混合物分数是非预混燃烧中广泛使用的参数，微分分子扩散是氢或氢混合燃料燃烧中的一种普遍现象。研究了混合馏分的化学计量守恒性质。澄清了两种不同的比尔格混合物级分配方。发现它们属于本文中发现的一类单参数广义混合分数定义。对碳氢化合物燃料的混合物馏分类别的具体定义进行了比较。比较表明，这种差异可能是显著的。通过最小化其与所需性质的偏差，从一般定义中寻求最佳混合物分数定义。所获得的最佳混合物组分总体上显示出比比尔格定义更好的化学计量保持性。还证明了广义混合物分数对其他含有氮（如氨 $\mathrm{NH_3}$）或硫（如硫化氢$\mathrm{H_2S}$ ）的燃料的推广。 et.al.|[2312.05204](http://arxiv.org/abs/2312.05204)|null|
|**2023-12-08**|**Membership Inference Attacks on Diffusion Models via Quantile Regression**|最近，扩散模型由于其高质量的输出而成为图像合成的流行工具。然而，与其他大型模型一样，它们可能会泄露有关其训练数据的私人信息。在这里，我们通过成员关系推理（MI）攻击展示了扩散模型的隐私漏洞，该攻击旨在识别给定训练的扩散模型时目标示例是否属于训练集。我们提出的MI攻击学习分位数回归模型，该模型预测未在训练中使用的示例上的重建损失分布（的分位数）。这允许我们定义一个细粒度假设测试，用于确定训练集中一个点的隶属度，基于使用根据该示例定制的自定义阈值对该点的重建损失进行阈值处理。我们还提供了一种简单的自举技术，该技术对“一袋弱攻击者”进行多数成员预测，从而提高了对单个分位数回归模型的准确性。我们表明，我们的攻击优于先前最先进的攻击，同时计算成本大大降低——先前的攻击需要训练多个“影子模型”，其架构与受攻击的模型相同，而我们的攻击只需要训练更小的模型。 et.al.|[2312.05140](http://arxiv.org/abs/2312.05140)|null|
|**2023-12-08**|**DreaMoving: A Human Dance Video Generation Framework based on Diffusion Models**|在本文中，我们提出了DreaMoving，这是一个基于扩散的可控视频生成框架，用于生成高质量的定制人类舞蹈视频。具体而言，给定目标身份和姿势序列，DreaMoving可以生成由姿势序列驱动的目标身份在任何地方跳舞的视频。为此，我们提出了一个用于运动控制的视频控制网和一个用于身份保护的内容引导器。所提出的模型易于使用，并且可以适用于大多数程式化的扩散模型，以产生不同的结果。项目页面位于https://dreamoving.github.io/dreamoving. et.al.|[2312.05107](http://arxiv.org/abs/2312.05107)|null|
|**2023-12-08**|**Application of deep learning to the estimation of normalization coefficients in diffusion-based covariance models**|海洋模型中的变分数据同化取决于在海岸线存在的情况下对一般相关算子进行建模的能力。基于扩散算子的网格点滤波器被广泛用于此目的，但存在计算瓶颈——每个模型网格点的归一化因子的估计成本高昂。在本文中，我们证明了一个简单的卷积神经网络可以有效地学习这些归一化因子，并且比当前的运算方法具有更好的精度。我们的网络使用来自NEMOVAR海洋数据同化系统的二维扩散算子进行了测试，该算子应用于水平分辨率约为一度的全球海洋网格。该网络是在通过强力方法估计的精确归一化因子上进行训练的。知道卷积网络只能对平移等变函数进行建模，我们确保归一化估计问题确实是平移等变的。具体来说，我们展示了如何在保持翻译等值的同时减少这个问题的输入数量。增加到海岸线的距离作为输入通道可以提高海岸线周围网络的性能。讨论了对三维扩散和更高水平分辨率的扩展。消除与归一化相关的计算瓶颈为使用自适应相关模型进行海洋数据同化开辟了道路。此作品的代码可在上公开获取https://github.com/folkeks/dl-normalization/tree/core-features et.al.|[2312.05068](http://arxiv.org/abs/2312.05068)|null|
|**2023-12-08**|**SmartMask: Context Aware High-Fidelity Mask Generation for Fine-grained Object Insertion and Layout Control**|随着潜在扩散模型的出现，生成图像修复和对象插入领域取得了重大进展。利用精确的物体掩模可以极大地增强这些应用。然而，由于用户在创建高保真度遮罩时遇到的挑战，这些方法有一种趋势，即在这些应用中依赖于更粗糙的遮罩（例如，边界框）。这导致了有限的控制和受损的背景内容保存。为了克服这些限制，我们引入了SmartMask，它允许任何新手用户创建用于精确插入对象的详细掩码。结合ControlNet Inpaint模型，我们的实验表明，SmartMask实现了卓越的对象插入质量，比以前的方法更有效地保留了背景内容。值得注意的是，与先前的工作不同，即使没有用户掩模引导，也可以使用所提出的方法，这允许它在不同的位置和尺度上执行无掩模对象插入。此外，我们发现，当与新的基于指令调优的规划模型迭代使用时，SmartMask可以用于从头开始设计详细的布局。与基于用户涂鸦的布局设计相比，我们观察到SmartMask通过布局到图像的生成方法实现了更好的输出质量。项目页面位于https://smartmask-gen.github.io et.al.|[2312.05039](http://arxiv.org/abs/2312.05039)|null|
|**2023-12-08**|**Numerical determination of iron dust laminar flame speeds with the counterflow twin-flame technique**|用低马赫数燃烧近似方法研究了铁粉逆流火焰。该模型考虑了两相之间的完全耦合，包括颗粒/液滴阻力。在低雷诺数条件下，推导了分散相流应变关系式。通过比较三种不同的模型来证明求解颗粒流应变模型的重要性：自由无应变火焰、假设颗粒流应变等于气体流应变的逆流火焰以及求解颗粒流应力的一种情况。由于铁在燃料混合物中缺乏扩散，所有三种情况都显示出优先扩散效应，例如DFe，m=0。优先扩散效应导致预热区中的燃料当量比达到峰值。在燃烧侧，应变和优先扩散的综合作用表明燃料当量比降低。惯性效应仅包括在解析的颗粒流应变情况下，抵消了这种效应，并导致燃烧侧的燃料当量比增加。进行了层流火焰速度分析，并就如何在逆流装置中通过实验确定火焰速度提出了建议。 et.al.|[2312.04994](http://arxiv.org/abs/2312.04994)|null|
|**2023-12-08**|**Gas-to-soliton transition of attractive bosons on a spherical surface**|我们研究了具有吸引零程相互作用的 $N$玻色子的基态性质，其特征是散射长度$a>0$，并局限于半径为$R$的球体表面。我们给出了$N=2$问题的解析解，$N\rightarrow\infty$的平均场分析，以及中间$N$的精确扩散蒙特卡罗结果。对于有限的$N$，我们观察到从极限$a/R\gg 1$（弱吸引）的一致状态到小$a/R$（强吸引）的局部化状态的平滑交叉。随着$N$的增加，这种交叉变窄为从均匀态到大小为$\sim R/\sqrt{N}$ 的孤立子的不连续转变。这两种状态被一个能垒分隔开，在能垒下隧穿被指数级抑制。系统行为的特点是空间曲率效应和超平均场项之间的特殊竞争，两者都打破了二维平均场理论的标度不变性。 et.al.|[2312.04984](http://arxiv.org/abs/2312.04984)|null|
|**2023-12-08**|**A search for new dwarf galaxies outside the nearby groups**|我们利用DESI Legacy Imaging Surveys的数据，在本体积中的已知星系群之外搜索附近的新矮星系。在5000平方度的广阔天空中，我们只发现了附近低质量星系的12个候选者。几乎所有的矮星都被归类为不规则矮星或过渡型矮星。此外，我们还检查了斯巴鲁望远镜的超超时空相机（700平方度）暴露在外的天空区域，并发现了附近矮星的另外九个候选者。最后，我们从Zaritsky的SMUDG目录中选择了九个局部体积的候选者，该目录包含在DESI调查的整个区域中自动检测到的7070个超漫射物体。我们估计，在一般宇宙场中，有一小部分静止的dSph星系小于10%。 et.al.|[2312.04930](http://arxiv.org/abs/2312.04930)|null|

<p align=right>(<a href=#updated-on-20231211>back to top</a>)</p>

## NeRF

|Publish Date|Title|Abstract|PDF|Code|
|---|---|---|---|---|
|**2023-12-08**|**Dynamic LiDAR Re-simulation using Compositional Neural Fields**|我们介绍了DyNFL，这是一种新的基于神经场的方法，用于动态驾驶场景中激光雷达扫描的高保真度重新模拟。DyNFL处理来自动态环境的激光雷达测量，并伴随着移动物体的边界框，以构建可编辑的神经场。该字段包括单独重建的静态背景和动态对象，允许用户在重新模拟的场景中修改视点、调整对象位置以及无缝添加或删除对象。我们方法的一个关键创新是神经场合成技术，该技术通过光线下降测试有效地集成了来自各种场景的重建神经资产，考虑到了遮挡和透明表面。我们对合成和真实世界环境的评估表明，\ShortName大大改进了基于激光雷达扫描的动态场景模拟，提供了物理保真度和灵活编辑功能的组合。 et.al.|[2312.05247](http://arxiv.org/abs/2312.05247)|null|
|**2023-12-08**|**TriHuman : A Real-time and Controllable Tri-plane Representation for Detailed Human Geometry and Appearance Synthesis**|仅从视频数据中创建可控、逼真和几何细节的真人数字替身是计算机图形学和视觉领域的一个关键挑战，尤其是在需要实时性能的情况下。最近的方法将神经辐射场（NeRF）连接到关节结构，例如身体模型或骨骼，以将点映射到姿势规范空间中，同时将NeRF调节在骨骼姿势上。这些方法通常使用多层感知器（MLP）对神经场进行参数化，导致运行时间缓慢。为了解决这一缺点，我们提出了一种新的人体定制、可变形和高效的三平面表示TriHuman，它实现了实时性能、最先进的姿态可控几何合成以及逼真的渲染质量。在核心，我们将全局光线样本非刚性地扭曲到未变形的三平面纹理空间中，这有效地解决了全局点映射到相同三平面位置的问题。然后，我们展示了如何将这种三平面特征表示以骨骼运动为条件，以考虑动态外观和几何结构的变化。我们的研究结果表明，在人类的几何形状和外观建模以及运行时性能方面，朝着更高质量迈出了明确的一步。 et.al.|[2312.05161](http://arxiv.org/abs/2312.05161)|null|
|**2023-12-08**|**GIR: 3D Gaussian Inverse Rendering for Relightable Scene Factorization**|本文提出了一种用于可重照明场景分解的三维高斯逆绘制方法GIR。与利用离散网格或神经隐式场进行反向渲染的现有方法相比，我们的方法利用3D高斯从多视图图像中估计对象的材料特性、照明和几何结构。我们的研究动机是有证据表明，在性能、多功能性和效率方面，3D高斯是比神经领域更有前途的主干。在本文中，我们旨在回答以下问题：“如何应用3D高斯来提高反向渲染的性能？”为了解决基于离散且通常在均匀分布的3D高斯表示中估计法线的复杂性，我们提出了一种高效的自正则化方法，该方法有助于在不需要额外监督的情况下对曲面法线进行建模。为了重建间接照明，我们提出了一种模拟光线跟踪的方法。大量实验证明，在反向渲染中，我们提出的GIR在各种广泛使用的数据集上跨多个任务的性能优于现有方法。这证实了它的功效和广泛的适用性，突出了它作为重新照明和重建中有影响力的工具的潜力。项目页面：https://3dgir.github.io et.al.|[2312.05133](http://arxiv.org/abs/2312.05133)|null|
|**2023-12-06**|**Gaussian-Flow: 4D Reconstruction with Dynamic 3D Gaussian Particle**|我们介绍了高斯流，这是一种新的基于点的方法，用于快速动态场景重建和多视图和单目视频的实时渲染。与因训练和渲染速度缓慢而受到阻碍的流行的基于NeRF的方法相比，我们的方法利用了基于点的3D高斯散射（3DGS）的最新进展。具体而言，提出了一种新的双域变形模型（DDDM）来显式地对每个高斯点的属性变形进行建模，其中通过时域中的多项式拟合和频域中的傅立叶级数拟合来捕获每个属性的时间相关残差。所提出的DDDM能够对长视频镜头中的复杂场景变形进行建模，消除了为每帧训练单独的3DGS的需要，或者引入了额外的隐式神经场来对3D动力学进行建模。此外，离散高斯点的显式变形建模确保了4D场景的超快速训练和渲染，这与为静态3D重建设计的原始3DGS相当。我们提出的方法展示了显著的效率提高，与每帧3DGS建模相比，训练速度快了5倍。此外，定量结果表明，所提出的高斯流在新视图渲染质量方面显著优于以前的主流方法。项目页面：https://nju-3dv.github.io/projects/gaussian-flow et.al.|[2312.03431](http://arxiv.org/abs/2312.03431)|null|
|**2023-12-06**|**Artist-Friendly Relightable and Animatable Neural Heads**|创建照片逼真数字化身的一种越来越常见的方法是通过使用体积神经场。当在一组多视图图像上训练时，原始神经辐射场（NeRF）允许静态头部进行令人印象深刻的新颖视图合成，后续方法表明，这些神经表示可以扩展到动态化身。最近，新的变体也超过了神经表示中烘焙照明的常见缺点，表明静态神经化身可以在任何环境中重新发光。在这项工作中，我们同时解决了运动和照明问题，为可重新照明和可动画化的神经头提出了一种新方法。我们的方法建立在一种已验证的动态化身方法的基础上，该方法基于体积基元的混合，结合最近提出的用于可重新照明神经场的轻量级硬件设置，并包括一种新的架构，该架构允许重新照明动态神经化身在任何环境中执行看不见的表情，即使是在近场照明和视点的情况下。 et.al.|[2312.03420](http://arxiv.org/abs/2312.03420)|null|
|**2023-12-06**|**RING-NeRF: A Versatile Architecture based on Residual Implicit Neural Grids**|自引入以来，神经场在三维重建和新视图合成方面变得非常流行。最近的研究集中在加速这一过程，以及提高对观测距离和有限监督视点数量变化的鲁棒性。然而，这些方法往往导致无法轻易结合的专门解决方案。为了解决这个问题，我们引入了一种新的简单但高效的架构，称为RING-NeRF，基于残差隐式神经网格，它提供了对场景和潜在空间之间映射函数的细节级别的控制。与距离感知的前向映射机制和连续的从粗到细的重建过程相关联，我们的多功能架构在以下方面展示了快速训练和最先进的性能：（1）抗混叠渲染，（2）从很少监督的视点的重建质量，以及（3）对于基于SDF的NeRF在没有适当的场景特定初始化的情况下的鲁棒性。我们还证明了我们的架构可以动态添加网格来增加重建的细节，为自适应重建开辟了道路。 et.al.|[2312.03357](http://arxiv.org/abs/2312.03357)|null|
|**2023-12-06**|**Multifractality in critical neural field dynamics**|大脑临界性框架在很大程度上认为大脑动力学是单分形的，尽管实验证据表明大脑表现出显著的多重分形。为了理解多重分形是如何在类临界系统中出现的，我们使用了临界神经振荡的计算模型。我们发现多重分形在同步相变附近出现。这些发现表明，时间动力学的多重分形在神经场的临界点达到峰值，为解释大脑记录中的多重分形提供了一个生成模型。 et.al.|[2312.03219](http://arxiv.org/abs/2312.03219)|null|
|**2023-12-04**|**GaussianHead: Impressive 3D Gaussian-based Head Avatars with Dynamic Hybrid Neural Field**|以前的头部化身方法大多依赖于固定的显式基元（网格、点）或隐式曲面（符号距离函数）和体积神经辐射场，难以在高保真度、训练速度和资源消耗之间取得平衡。混合场最近的流行带来了新的表示，但受到通过固定映射获得的参数化因子的限制。我们提出了GaussianHead：一种基于各向异性三维高斯基元的头部化身算法。我们利用规范高斯来表示动态场景。使用显式“动态”三平面作为参数化头部几何的有效容器，与底层几何和三平面中的因子很好地对齐，我们获得了正则高斯的对齐正则因子。利用微小的MLP，因子被解码为3D高斯基元的不透明度和球面谐波系数。最后，我们使用高效的可微高斯光栅化器进行渲染。我们的方法显著受益于我们基于3D高斯的新表示，并且三平面中底层几何结构和因子的适当对齐变换消除了固定映射引入的偏差。与最先进的技术相比，我们在自我重建、新视图合成和跨身份再现等任务中实现了最佳的视觉效果，同时保持了高渲染效率（每帧0.12秒）。在某些情况下，甚至鼻子周围的毛孔也清晰可见。代码和其他视频可以在项目主页上找到。 et.al.|[2312.01632](http://arxiv.org/abs/2312.01632)|null|
|**2023-11-29**|**Accelerating Neural Field Training via Soft Mining**|我们提出了一种通过有效选择采样位置来加速神经场训练的方法。虽然神经场最近变得很流行，但它通常是通过对训练域进行统一采样或通过手工启发式进行训练的。我们证明，通过基于重要性采样的软挖掘技术可以提高收敛性和最终训练质量：我们不是完全考虑或忽略一个像素，而是用标量来衡量相应的损失。为了实现我们的想法，我们使用Langevin蒙特卡罗采样。我们表明，通过这样做，具有更高误差的区域被更频繁地选择，导致收敛速度提高了2倍以上。本研究的代码和相关资源可在https://ubc-vision.github.io/nf-soft-mining/. et.al.|[2312.00075](http://arxiv.org/abs/2312.00075)|null|
|**2023-11-29**|**Neural Fields with Thermal Activations for Arbitrary-Scale Super-Resolution**|最近的任意尺度单图像超分辨率（ASSR）方法已经使用局部神经场来表示可以以不同速率采样的连续信号。然而，在这样的公式中，场值的逐点查询并不自然地与给定像素的点扩散函数（PSF）匹配。在这项工作中，我们提出了一种设计神经场的新方法，使得可以使用高斯PSF来查询点，该函数在ASSR的分辨率之间移动时起到抗混叠的作用。我们使用从傅立叶理论和热方程导出的新激活函数来实现这一点。这不需要额外的成本：与图像域中的滤波不同，在我们的框架中使用高斯PSF查询点不会影响计算成本。与超网络相结合，我们的方法不仅提供了理论上有保证的抗混叠，而且为ASSR设置了一个新的标准，同时也比以前的方法更具参数效率。 et.al.|[2311.17643](http://arxiv.org/abs/2311.17643)|null|

<p align=right>(<a href=#updated-on-20231211>back to top</a>)</p>

[contributors-shield]: https://img.shields.io/github/contributors/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[contributors-url]: https://github.com/Vincentqyw/cv-arxiv-daily/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[forks-url]: https://github.com/Vincentqyw/cv-arxiv-daily/network/members
[stars-shield]: https://img.shields.io/github/stars/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[stars-url]: https://github.com/Vincentqyw/cv-arxiv-daily/stargazers
[issues-shield]: https://img.shields.io/github/issues/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[issues-url]: https://github.com/Vincentqyw/cv-arxiv-daily/issues

