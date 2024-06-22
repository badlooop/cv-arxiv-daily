[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]

## Updated on 2024.06.22
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
|**2024-06-20**|**Deblurring Neural Radiance Fields with Event-driven Bundle Adjustment**|神经辐射场（NeRF）以高质量的多视图图像作为输入，实现了令人印象深刻的3D表示学习和新颖的视图合成结果。然而，图像中的运动模糊经常发生在低光照和高速运动场景中，这显著降低了NeRF的重建质量。以前的去模糊NeRF方法难以估计曝光时间内的信息，无法准确地对运动模糊进行建模。相比之下，以高时间分辨率测量强度变化的仿生事件相机弥补了这一信息不足。在本文中，我们提出了用于去模糊神经辐射场的事件驱动束调整（EBAD NeRF），以通过利用混合事件RGB数据来联合优化可学习姿态和NeRF参数。引入强度变化度量事件损失和照片度量模糊损失来加强相机运动模糊的显式建模。对合成数据和真实捕获数据的实验结果表明，与先前的工作相比，EBAD NeRF可以在曝光时间内获得准确的相机姿态，并学习更清晰的3D表示。 et.al.|[2406.14360](http://arxiv.org/abs/2406.14360)|null|
|**2024-06-19**|**Simultaneous Map and Object Reconstruction**|在本文中，我们提出了一种利用激光雷达对大规模城市场景进行动态表面重建的方法。基于深度的重建往往侧重于小规模对象或将移动对象视为异常值的大规模SLAM重建。我们采用整体视角，优化动态场景的组成模型，将世界分解为刚性移动的对象和背景。为了实现这一点，我们从最近的新颖视图合成方法中获得灵感，并将重建问题作为全局优化，最小化我们预测的表面和输入激光雷达扫描之间的距离。我们展示了如何将这种全局优化分解为配准和表面重建步骤，这些步骤可以通过现成的方法很好地处理，而无需任何重新训练。通过对连续时间运动进行仔细建模，我们的重建可以补偿旋转激光雷达传感器的滚动快门效应。这允许第一个系统（据我们所知）对刚性移动物体的激光雷达扫描进行适当的运动补偿，补充了广泛使用的静态场景运动补偿技术。除了将动态重建本身作为一个目标之外，我们还表明，这样的系统可以用于自动标记部分注释的序列，并为难以标记的问题（如深度完成和场景流）生成地面实况注释。 et.al.|[2406.13896](http://arxiv.org/abs/2406.13896)|null|
|**2024-06-19**|**Splatter a Video: Video Gaussian Representation for Versatile Processing**|视频表示是一个长期存在的问题，对各种下游任务至关重要，如跟踪、深度预测、分割、视图合成和编辑。然而，由于缺乏3D结构，当前的方法要么难以对复杂的运动进行建模，要么依赖于不适合操纵任务的隐式3D表示。为了应对这些挑战，我们引入了一种新的显式3D表示视频高斯表示——将视频嵌入到3D高斯中。我们提出的表示使用显式高斯作为代理对3D规范空间中的视频外观进行建模，并将每个高斯与视频运动的3D运动相关联。这种方法提供了比分层图集或体积像素矩阵更内在和更明确的表示。为了获得这样的表示，我们从基础模型中提取二维先验，如光流和深度，以在这种不适定的环境中正则化学习。广泛的应用证明了我们新视频表示的多功能性。它已被证明在许多视频处理任务中有效，包括跟踪、一致的视频深度和特征细化、运动和外观编辑以及立体视频生成。项目页面：https://sunyangtian.github.io/spatter_a_video_web/ et.al.|[2406.13870](http://arxiv.org/abs/2406.13870)|null|
|**2024-06-18**|**HumanSplat: Generalizable Single-Image Human Gaussian Splatting with Structure Priors**|尽管高保真度人体重建技术最近取得了进展，但对密集捕获图像或耗时的每次优化的要求大大阻碍了它们在更广泛场景中的应用。为了解决这些问题，我们提出了HumanSplat，它以可推广的方式从单个输入图像中预测任何人的3D高斯飞溅特性。特别是，HumanSplat包括一个2D多视图扩散模型和一个具有人体结构先验的潜在重建转换器，这些先验能够在一个统一的框架内熟练地集成几何先验和语义特征。进一步设计了一种包含人体语义信息的层次损失，以实现高保真纹理建模，并更好地约束估计的多个视图。在标准基准和野外图像上的综合实验表明，HumanSplat在实现真实感新颖视图合成方面超越了现有的最先进方法。 et.al.|[2406.12459](http://arxiv.org/abs/2406.12459)|**[link](https://github.com/humansplat/humansplat.github.io)**|
|**2024-06-17**|**DistillNeRF: Perceiving 3D Scenes from Single-Glance Images by Distilling Neural Fields and Foundation Model Features**|我们提出了DistilleNeRF，这是一种自监督学习框架，解决了在自动驾驶中从有限的2D观测中理解3D环境的挑战。我们的方法是一个可推广的前馈模型，它从稀疏的单帧多视图相机输入中预测丰富的神经场景表示，并通过可微分渲染进行自监督训练，以重建RGB、深度或特征图像。我们的第一个见解是通过生成密集的深度和虚拟相机目标进行训练，利用每场景优化的神经辐射场（NeRF），从而帮助我们的模型从稀疏的非重叠图像输入中学习3D几何。其次，为了学习语义丰富的3D表示，我们建议从预先训练的2D基础模型（如CLIP或DINOv2）中提取特征，从而实现各种下游任务，而不需要昂贵的3D人工注释。为了利用这两个见解，我们引入了一种新的模型架构，该架构具有两级提升-飞溅-拍摄编码器和参数化稀疏分层体素表示。在NuScenes数据集上的实验结果表明，DistilleNeRF在场景重建、新视图合成和深度估计方面显著优于现有的可比自监督方法；并且它允许竞争性的零样本3D语义占用预测，以及通过提取的基础模型特征来理解开放世界场景。演示和代码将在https://distillnerf.github.io/. et.al.|[2406.12095](http://arxiv.org/abs/2406.12095)|null|
|**2024-06-17**|**A Hierarchical 3D Gaussian Representation for Real-Time Rendering of Very Large Datasets**|近年来，新型视图合成取得了重大进展，3D高斯飞溅提供了卓越的视觉质量、快速训练和实时渲染。然而，训练和渲染所需的资源不可避免地限制了可以以良好视觉质量表示的捕捉场景的大小。我们引入了一种3D高斯层次结构，它可以为非常大的场景保留视觉质量，同时提供了一种高效的细节级别（LOD）解决方案，通过有效的级别选择和级别之间的平滑过渡来高效渲染远处的内容。我们引入了一种分而治之的方法，使我们能够在独立的块中训练非常大的场景。我们将块合并到一个层次结构中，该层次结构可以进行优化，以进一步提高合并到中间节点的高斯图的视觉质量。非常大的捕获通常具有稀疏的场景覆盖，这对原始的3D高斯飞溅训练方法提出了许多挑战；我们调整并规范培训以解决这些问题。我们提供了一个完整的解决方案，能够实时渲染非常大的场景，并且由于我们的LOD方法，可以适应可用的资源。我们使用一个简单且价格合理的设备显示了拍摄场景的结果，其中包含多达数万张图像，覆盖的轨迹长达数公里，持续时间长达一小时。项目页面：https://repo-sam.inria.fr/fungraph/hierarchical-3d-gaussians/ et.al.|[2406.12080](http://arxiv.org/abs/2406.12080)|null|
|**2024-06-17**|**MegaScenes: Scene-Level View Synthesis at Scale**|场景级新颖视图合成（NVS）是许多视觉和图形应用的基础。最近，姿态条件扩散模型通过从2D基础模型中提取3D信息取得了显著进展，但这些方法受到缺乏场景级训练数据的限制。常见的数据集选择要么由孤立的对象（Ob厌恶对象）组成，要么由姿势分布有限的以对象为中心的场景（DTU、CO3D）组成。在本文中，我们从互联网照片集创建了一个大规模的场景级数据集，称为MegaScenes，其中包含来自世界各地的超过100K的运动结构（SfM）重建。互联网照片代表了一个可扩展的数据源，但也带来了照明和瞬态物体等挑战。我们解决这些问题是为了进一步创建适合NVS任务的子集。此外，我们分析了最先进的NVS方法的失败案例，并显著提高了生成一致性。通过广泛的实验，我们验证了我们的数据集和方法在野外场景生成方面的有效性。有关数据集和代码的详细信息，请参阅我们的项目页面https://megascenes.github.io . et.al.|[2406.11819](http://arxiv.org/abs/2406.11819)|null|
|**2024-06-15**|**Federated Neural Radiance Field for Distributed Intelligence**|新型视图合成（NVS）是许多AR和VR应用的重要技术。最近提出的神经辐射场（NeRF）方法在NVS任务上表现出了优越的性能，并已应用于其他相关领域。然而，由于严格的法规和隐私问题，具有分布式数据存储的某些应用场景可能会对NeRF方法获取训练图像带来挑战。为了克服这一挑战，我们将重点放在FedNeRF上，这是一种基于联合学习（FL）的NeRF方法，它利用不同数据所有者的可用图像，同时保护数据隐私。在本文中，我们首先构建了一个资源丰富、功能多样的联合学习测试平台。然后，我们在这样一个实际的FL系统中部署了FedNeRF算法，并进行了部分客户端选择的FedNeRF实验。预计本文对FedNeRF方法的研究将有助于促进NeRF方法在分布式数据存储场景中的未来应用。 et.al.|[2406.10474](http://arxiv.org/abs/2406.10474)|null|
|**2024-06-14**|**Wild-GS: Real-Time Novel View Synthesis from Unconstrained Photo Collections**|在非结构化旅游环境中拍摄的照片经常表现出可变的外观和短暂的遮挡，这对精确的场景重建和在新的视图合成中引入伪影提出了挑战。尽管先前的方法已经将神经辐射场（NeRF）与额外的可学习模块集成在一起，以处理动态外观并消除瞬态对象，但其广泛的训练需求和缓慢的渲染速度限制了实际部署。最近，3D高斯散射（3DGS）已成为NeRF的一种很有前途的替代方案，它提供了卓越的训练和推理效率以及更好的渲染质量。本文介绍了Wild GS，这是对3DGS的一种创新改编，针对无约束的照片集进行了优化，同时保留了其效率优势。Wild GS通过每个3D高斯的固有材料属性、每个图像的全局照明和相机特性以及点级局部反射率方差来确定其外观。与以前在图像空间中对参考特征建模的方法不同，Wild GS通过对从参考图像中提取的三平面进行采样，将像素外观特征与相应的局部高斯显式对齐。这种新颖的设计有效地将参考视图的高频细节外观转移到3D空间，并显著加快了训练过程。此外，利用2D可见性图和深度正则化来分别减轻瞬态效应和约束几何体。大量实验表明，在所有现有技术中，Wild GS实现了最先进的渲染性能和最高的训练和推理效率。 et.al.|[2406.10373](http://arxiv.org/abs/2406.10373)|null|
|**2024-06-14**|**PUP 3D-GS: Principled Uncertainty Pruning for 3D Gaussian Splatting**|新视图合成的最新进展使实时渲染速度和高重建精度成为可能。3D高斯散射（3D-GS）是一种基于点的参数化3D场景表示，它将场景建模为大型的3D高斯集。复杂的场景可能包括数百万高斯，相当于巨大的存储和内存需求，这限制了3D-GS在资源有限的设备上的可行性。当前通过修剪高斯来压缩这些预训练模型的技术依赖于组合启发式来确定要删除哪些模型。在本文中，我们提出了一个原则性的空间敏感性修剪得分，它优于这些方法。它被计算为训练视图上的重构误差相对于每个高斯的空间参数的二阶近似。此外，我们提出了一种多轮修剪-细化流水线，该流水线可以应用于任何预训练的3D-GS模型，而无需改变训练流水线。在修剪了88.44%的高斯之后，我们观察到我们的PUP 3D-GS管道将3D-GS的平均渲染速度提高了2.65 $\times$ ，同时保留了更显著的前景信息，并实现了比以前在Mip NeRF 360、Tanks&Temples和Deep Blending数据集的场景上的修剪技术更高的图像质量指标。 et.al.|[2406.10219](http://arxiv.org/abs/2406.10219)|null|

<p align=right>(<a href=#updated-on-20240622>back to top</a>)</p>

## 3D Reconstruction

|Publish Date|Title|Abstract|PDF|Code|
|---|---|---|---|---|
|**2024-06-19**|**MVSBoost: An Efficient Point Cloud-based 3D Reconstruction**|高效准确的3D重建对于各种应用至关重要，包括增强现实和虚拟现实、医学成像和电影特效。虽然传统的多视图立体（MVS）系统在这些应用中是基础，但在隐式3D场景建模中使用神经隐式场为处理复杂拓扑和连续曲面带来了新的可能性。然而，神经隐式场往往存在计算效率低、过拟合和严重依赖数据质量的问题，限制了其实际应用。本文提出了一种增强的MVS框架，该框架通过运动结构（SfM）和用于点云致密化、网格重建和纹理化的高级图像处理，将多视图360度图像与稳健的相机姿态估计相结合。我们的方法显著改进了传统的MVS方法，在真实合成360数据集上使用切角距离度量进行验证，提供了卓越的准确性和精度。所开发的MVS技术增强了3D重建的细节和清晰度，并在复杂场景重建中展示了卓越的计算效率和稳健性，有效地处理了遮挡和不同的视点。这些改进表明，我们的MVS框架可以与当前最先进的神经隐场方法竞争，并有可能超越这些方法，尤其是在需要实时处理和可扩展性的场景中。 et.al.|[2406.13515](http://arxiv.org/abs/2406.13515)|null|
|**2024-06-19**|**Assessing the 3D resolution of refocused correlation plenoptic images using a general-purpose image quality estimator**|相关全光成像（CPI）是一种很有前途的光场成像（LFI）方法，这是一种能够同时测量场景中光强分布和传播方向的技术。LFI允许单次3D采样，为广泛的应用提供快速的3D重建。然而，LFI中通常用于获得3D信息的微透镜阵列限制了图像分辨率，图像分辨率随着体积重建能力的增强而迅速下降。CPI通过使用两个具有空间分辨率的光电探测器来解耦光场信息测量，从而消除了对微透镜的需求，从而解决了这一限制。3D信息被编码在四维相关函数中，该函数在后处理中被解码以重建图像，而没有传统LFI中看到的分辨率损失。本文评估了CPI的断层成像性能，证明了重新聚焦重建方法提供了与传统成像系统相当的轴向切片能力。提出了一种基于图像保真度的通用分析方法来定量研究轴向和横向分辨率。该分析充分表征了任何CPI架构的体积分辨率，提供了对其成像性能的全面评估。 et.al.|[2406.13501](http://arxiv.org/abs/2406.13501)|null|
|**2024-06-19**|**Self-Supervised Diffusion Model for 3-D Seismic Data Reconstruction**|地震数据重建是补偿不均匀和不完全地震几何的有效工具。与二维地震数据重建方法相比，三维重建方法可以更多地考虑地震数据中的空间结构相关性。在早期的研究中，三维重建方法主要是理论驱动的，由于其对地震数据的先验假设，因此存在一些局限性。为了释放这些局限性，基于深度学习的重建方法兴起，并在处理重建问题方面显示出潜力。然而，现有的深度学习方法主要有两个缺点。一方面，现有的大多数基于深度学习的方法都采用卷积神经网络，在处理复杂或时变分布的数据时存在一些困难。最近，有报道称，扩散模型能够通过逐渐使数据分布复杂化来优化网络，从而解决具有复杂分布的数据。另一方面，现有的方法需要足够的成对数据来训练网络，这是很难获得的，尤其是对于缺乏的三维地震数据。基于深度先验的无监督和基于采样的自监督网络为这个问题提供了一个可用的解决方案。在本文中，我们开发了一个用于三维地震数据重建的自监督扩散模型（S2DM）。所提出的模型主要包括扩散恢复模型和变分时空模块。大量的合成和现场实验证明了所提出的S2DM算法的优越性。 et.al.|[2406.13252](http://arxiv.org/abs/2406.13252)|null|
|**2024-06-18**|**Semantic Graph Consistency: Going Beyond Patches for Regularizing Self-Supervised Vision Transformers**|具有视觉转换器（ViTs）的自监督学习（SSL）已被证明对表示学习有效，在各种下游任务上的出色表现证明了这一点。尽管取得了这些成功，但现有的基于ViT的SSL架构并没有完全利用ViT主干，尤其是ViT的补丁令牌。在本文中，我们引入了一个新的语义图一致性（SGC）模块来规范基于ViT的SSL方法，并有效地利用补丁令牌。我们将图像重新定义为图，将图像补丁作为节点，并通过使用图神经网络将显式消息传递到SSL框架中来注入关系归纳偏差。我们的SGC损失充当了一个正则化因子，利用未充分开发的ViTs补丁令牌来构建图，并在图像的多个视图中增强图特征之间的一致性。在包括ImageNet、RESISC和Food-101在内的各种数据集上进行的广泛实验表明，我们的方法显著提高了学习表示的质量，当有限的标记数据用于线性评估时，性能提高了5-10%。这些实验与一系列全面的消融相结合，证明了我们的方法在各种环境中的前景。 et.al.|[2406.12944](http://arxiv.org/abs/2406.12944)|null|
|**2024-06-18**|**HumanSplat: Generalizable Single-Image Human Gaussian Splatting with Structure Priors**|尽管高保真度人体重建技术最近取得了进展，但对密集捕获图像或耗时的每次优化的要求大大阻碍了它们在更广泛场景中的应用。为了解决这些问题，我们提出了HumanSplat，它以可推广的方式从单个输入图像中预测任何人的3D高斯飞溅特性。特别是，HumanSplat包括一个2D多视图扩散模型和一个具有人体结构先验的潜在重建转换器，这些先验能够在一个统一的框架内熟练地集成几何先验和语义特征。进一步设计了一种包含人体语义信息的层次损失，以实现高保真纹理建模，并更好地约束估计的多个视图。在标准基准和野外图像上的综合实验表明，HumanSplat在实现真实感新颖视图合成方面超越了现有的最先进方法。 et.al.|[2406.12459](http://arxiv.org/abs/2406.12459)|**[link](https://github.com/humansplat/humansplat.github.io)**|
|**2024-06-18**|**Fast Global Localization on Neural Radiance Field**|神经辐射场（NeRF）提供了一种新的场景表示方法，允许从2D图像进行高质量的3D重建。在取得显著成就后，NeRF地图中的全球定位是实现广泛应用的重要任务。最近，Loc-NeRF展示了一种将传统蒙特卡罗定位与NeRF相结合的定位方法，显示了使用NeRF作为环境图的有希望的结果。然而，尽管Loc-NeRF取得了进步，但它仍面临着时间密集型光线渲染过程的挑战，这在实际应用中可能是一个重大限制。为了解决这个问题，我们引入了Fast Loc NeRF，它利用从粗到细的方法来实现更高效、更准确的基于NeRF地图的全局定位。具体而言，Fast Loc NeRF在从低到高分辨率的多分辨率上匹配渲染像素和观察到的图像。因此，它加快了昂贵的粒子更新过程，同时保持了精确的定位结果。此外，为了拒绝异常粒子，我们提出了粒子拒绝加权，该加权通过利用NeRF的特性来估计粒子的不确定性，并在粒子加权过程中考虑它们。我们的Fast Loc NeRF在几个基准上设置了新的最先进的定位性能，使其准确性和效率令人信服。 et.al.|[2406.12202](http://arxiv.org/abs/2406.12202)|null|
|**2024-06-17**|**FAWN: Floor-And-Walls Normal Regularization for Direct Neural TSDF Reconstruction**|利用3D语义进行直接的3D重建具有巨大的潜力。例如，通过假设墙壁是垂直的，地板是平面和水平的，我们可以纠正扭曲的房间形状，并消除局部伪影，如洞、坑和山丘。在本文中，我们提出了FAWN，这是截断符号距离函数（TSDF）重建方法的一种改进，它通过检测场景中的墙壁和地板来考虑场景结构，并对偏离水平和垂直方向的相应表面法线进行惩罚。作为一个3D稀疏卷积模块实现，FAWN可以合并到任何预测TSDF的可训练管道中。由于FAWN只需要用于训练的3D语义，因此对进一步使用没有额外的限制。我们证明，与现有的基于语义的方法相比，FAWN修改的方法更有效地使用了语义。此外，我们将我们的修改应用于最先进的TSDF重建方法，并在SCANNET、ICL-NUIM、TUM RGB-D和7SCENES基准中证明了质量增益。 et.al.|[2406.12054](http://arxiv.org/abs/2406.12054)|null|
|**2024-06-18**|**Effective Rank Analysis and Regularization for Enhanced 3D Gaussian Splatting**|从多视图图像中进行三维重建是计算机视觉和图形学的基本挑战之一。近年来，三维高斯散射（3DGS）已经成为一种很有前途的技术，能够实时渲染和高质量的三维重建。该方法利用了三维高斯表示和基于瓦片的飞溅技术，绕过了昂贵的神经场查询。尽管3DGS具有潜力，但由于高斯收敛为具有一个主导方差的各向异性高斯，3DGS仍面临挑战，包括针状伪影、次优几何结构和不准确法线。我们建议使用有效秩分析来检查3D高斯基元的形状统计，并识别高斯确实收敛为有效秩为1的针状形状。为了解决这个问题，我们引入了有效秩作为正则化，它约束高斯的结构。我们的新正则化方法增强了法线和几何重建，同时减少了针状伪影。该方法可以作为附加模块集成到其他3DGS变体中，在不影响视觉逼真度的情况下提高其质量。 et.al.|[2406.11672](http://arxiv.org/abs/2406.11672)|null|
|**2024-06-15**|**fNeRF: High Quality Radiance Fields from Practical Cameras**|近年来，神经辐射场的发展使人们能够从多视图相机数据中对场景和物体进行前所未有的逼真3D重建。然而，以前的方法使用过于简化的针孔相机模型，导致散焦模糊被“烘焙”到重建的辐射场中。我们提出了一种对光线投射的修改，该修改利用透镜的光学特性来增强在存在散焦模糊的情况下的场景重建。这使我们能够从具有有限孔径的实际相机的测量中提高辐射场重建的质量。我们表明，与针孔模型和散焦模糊模型的其他近似值相比，所提出的模型更符合实际相机的散焦模糊行为，特别是在存在部分遮挡的情况下。这使我们能够实现更清晰的重建，在合成和真实数据集上验证所有对焦图像时将PSNR提高高达3dB。 et.al.|[2406.10633](http://arxiv.org/abs/2406.10633)|null|
|**2024-06-15**|**Detection and Utilization of Reflections in LiDAR Scans Through Plane Optimization and Plane SLAM**|在激光雷达传感中，玻璃、镜子和其他材料往往会导致数据读数不一致，因为激光束可能会报告玻璃的距离、玻璃后面物体的距离或到反射物体的距离。这导致了机器人和3D重建方面的问题，尤其是在定位、映射和导航方面。使用双返回激光雷达和其他方法，可以在一次扫描中检测玻璃平面并对点进行分类。在这项工作中，我们更进一步，构建了一个全局优化的反射平面图，以便在最后对所有激光雷达读数进行分类。正如我们的实验所表明的，与单扫描方法相比，这种方法提供了优越的分类精度。这项工作的代码和数据可以在线开源。 et.al.|[2406.10494](http://arxiv.org/abs/2406.10494)|null|

<p align=right>(<a href=#updated-on-20240622>back to top</a>)</p>

## Diffusion

|Publish Date|Title|Abstract|PDF|Code|
|---|---|---|---|---|
|**2024-06-20**|**A Survey of Multimodal-Guided Image Editing with Text-to-Image Diffusion Models**|图像编辑旨在编辑给定的合成或真实图像，以满足用户的特定要求。近年来，它作为人工智能生成内容（AIGC）的一个有前途且具有挑战性的领域被广泛研究。该领域最近的重大进展是基于文本到图像（T2I）扩散模型的发展，该模型根据文本提示生成图像。这些模型展示了非凡的生成能力，并已成为广泛使用的图像编辑工具。基于T2I的图像编辑方法显著提高了编辑性能，并为修改由多模式输入引导的内容提供了用户友好的界面。在这项调查中，我们对利用T2I扩散模型的多模式引导图像编辑技术进行了全面综述。首先，我们从整体的角度定义了图像编辑的范围，并详细说明了各种控制信号和编辑场景。然后，我们提出了一个统一的框架来形式化编辑过程，将其分为两个主要算法族。该框架为用户实现特定目标提供了一个设计空间。随后，我们对该框架内的每个组件进行了深入分析，考察了不同组合的特点和适用场景。考虑到基于训练的方法学习在用户指导下直接将源图像映射到目标图像，我们分别讨论了它们，并介绍了不同场景下源图像的注入方案。此外，我们还回顾了2D技术在视频编辑中的应用，重点介绍了帧间不一致的解决方案。最后，我们讨论了该领域中悬而未决的挑战，并提出了未来潜在的研究方向。我们一直在追踪相关作品https://github.com/xinchengshuai/Awesome-Image-Editing. et.al.|[2406.14555](http://arxiv.org/abs/2406.14555)|**[link](https://github.com/xinchengshuai/awesome-image-editing)**|
|**2024-06-20**|**Advancing Fine-Grained Classification by Structure and Subject Preserving Augmentation**|细粒度视觉分类（FGVC）涉及到对密切相关的子类进行分类。由于类之间的细微差异和高的类内方差，这项任务很困难。此外，FGVC数据集通常很小，难以收集，因此突出了对有效数据扩充的重大需求。文本到图像扩散模型的最新进展为增强分类数据集提供了新的可能性。虽然这些模型已被用于生成分类任务的训练数据，但它们在FGVC模型的全数据集训练中的有效性仍有待探索。最近的技术依赖于Text2Image生成或Img2Img方法，通常很难生成准确表示类的图像，同时将其修改到显著增加数据集多样性的程度。为了应对这些挑战，我们提出了SaSPA：结构和主题保留增强。与最近的方法相反，我们的方法不使用真实图像作为指导，从而增加了生成灵活性并促进了更大的多样性。为了确保准确的类表示，我们使用条件反射机制，特别是通过对图像边缘和主题表示进行条件反射。我们进行了广泛的实验，并将SaSPA与传统和最近的生成数据增强方法进行了比较。SaSPA在多种设置中始终优于所有已建立的基线，包括全数据集训练、上下文偏差和少镜头分类。此外，我们的结果揭示了使用合成数据进行FGVC模型的有趣模式；例如，我们发现实际使用的数据量与合成数据的最佳比例之间存在关系。代码位于https://github.com/EyalMichaeli/SaSPA-Aug. et.al.|[2406.14551](http://arxiv.org/abs/2406.14551)|**[link](https://github.com/eyalmichaeli/saspa-aug)**|
|**2024-06-20**|**Consistency Models Made Easy**|一致性模型（CM）是一类新兴的生成模型，它比传统的扩散模型提供更快的采样。CM强制将沿着采样轨迹的所有点映射到相同的初始点。但这一目标导致了资源密集型培训：例如，截至2024年，在CIFAR-10上培训SoTA CM需要一周的时间，在8个GPU上进行培训。在这项工作中，我们提出了一种训练CM的替代方案，大大提高了构建此类模型的效率。具体而言，通过通过特定的微分方程表达CM轨迹，我们认为扩散模型可以被视为具有特定离散化的CM的特殊情况。因此，我们可以从预先训练的扩散模型开始微调一致性模型，并在训练过程中逐步将完全一致性条件近似到更强的程度。我们得到的方法，我们称之为“简单一致性调整”（ECT），在大大提高训练时间的同时，确实提高了以前方法的质量：例如，ECT在单个A100 GPU上的1小时内，在CIFAR10上实现了2.73的两步FID，与数百个GPU小时训练的一致性蒸馏相匹配。由于这种计算效率，我们研究了ECT下CM的缩放定律，表明它们似乎遵循经典的幂律缩放，暗示了它们在更大尺度上提高效率和性能的能力。密码https://github.com/locuslab/ect)可用。 et.al.|[2406.14548](http://arxiv.org/abs/2406.14548)|**[link](https://github.com/locuslab/ect)**|
|**2024-06-20**|**Invertible Consistency Distillation for Text-Guided Image Editing in Around 7 Steps**|扩散蒸馏代表了在几个采样步骤中实现忠实的文本到图像生成的一个非常有前途的方向。然而，尽管最近取得了成功，但现有的提取模型仍然不能提供全谱的扩散能力，例如真实图像反演，这使得许多精确的图像处理方法成为可能。这项工作旨在丰富提取的文本到图像的扩散模型，使其能够有效地将真实图像编码到其潜在空间中。为此，我们引入了可逆一致性蒸馏（iCD），这是一种广义一致性蒸馏框架，仅需3-4个推理步骤即可实现高质量的图像合成和准确的图像编码。尽管高的无分类器制导尺度加剧了文本到图像扩散模型的反演问题，但我们注意到，动态制导显著减少了重建误差，而不会显著降低生成性能。因此，我们证明，配备动态引导的iCD可以作为零样本文本引导图像编辑的高效工具，与更昂贵的最先进的替代品竞争。 et.al.|[2406.14539](http://arxiv.org/abs/2406.14539)|null|
|**2024-06-20**|**Formulation of Chimera Gradient Flows for Chemotaxis Systems with Indirect Signal Production and Degenerate Diffusion**|将三个未知函数的抛物型系统视为三个耦合梯度流，该系统不能表示为梯度流。对于每个未知函数，使用最小化运动方案来构造时间离散的近似解。与梯度流的标准最小化运动方案不同，时间离散近似解相对于时间步长的相对紧致性并不是固有的保证。然而，李雅普诺夫泛函的存在确保了这种相对紧性，从而导致了时间全局解的存在。 et.al.|[2406.14536](http://arxiv.org/abs/2406.14536)|null|
|**2024-06-20**|**ForSE+: Simulating non-Gaussian CMB foregrounds at 3 arcminutes in a stochastic way based on a generative adversarial network**|我们介绍了ForSE+，这是一个Python包，它可以在弧角尺度上生成非高斯散射星系热尘埃发射图，并有能力生成小尺度的随机实现。这代表了ForSE（前景尺度扩展器）软件包的扩展，该软件包最近被提出用于使用生成对抗性网络（GANs）模拟非高斯小尺度的热尘排放。在输入来自观测的大尺度偏振图的情况下，ForSE+已被训练为在3'处产生真实的偏振小尺度，遵循通过Minkowski泛函评估的观测强度小尺度的统计特性，主要是非高斯性。此外，通过将随机分量的不同实现添加到大规模前景中，我们表明ForSE+能够以随机的方式生成小规模。在这两种情况下，与实际观测和作为幂律的正确振幅标度相比，输出小尺度具有相似的非高斯性水平。未来，这些逼真的新地图将有助于了解非高斯前景对宇宙微波背景（CMB）信号测量的影响，特别是对CMB偏振B模式中的透镜重建、去透镜和宇宙引力波检测的影响。 et.al.|[2406.14519](http://arxiv.org/abs/2406.14519)|**[link](https://github.com/yaojian95/ForSEplus)**|
|**2024-06-20**|**V-LASIK: Consistent Glasses-Removal from Videos Using Synthetic Data**|基于扩散的生成模型最近显示出显著的图像和视频编辑能力。然而，本地视频编辑，特别是去除眼镜等小属性，仍然是一个挑战。现有的方法要么过度改变视频，生成不现实的伪影，要么无法在整个视频中一致地执行所请求的编辑。在这项工作中，我们专注于视频中眼镜的一致性和身份保护去除，并将其作为视频中一致性局部属性去除的案例研究。由于缺乏配对数据，我们采用弱监督方法，使用调整的预训练扩散模型生成合成的不完美数据。我们表明，尽管数据不完善，但通过从我们生成的数据中学习并利用预先训练的扩散模型的先验知识，我们的模型能够始终如一地执行所需的编辑，同时保留原始视频内容。此外，我们通过将我们的方法成功地应用于面部贴纸去除，来证明我们的方法对其他本地视频编辑任务的泛化能力。我们的方法比现有方法有了显著的改进，展示了利用合成数据和强大的视频先验进行本地视频编辑任务的潜力。 et.al.|[2406.14510](http://arxiv.org/abs/2406.14510)|null|
|**2024-06-20**|**SafeSora: Towards Safety Alignment of Text2Video Generation via a Human Preference Dataset**|为了降低大型视觉模型（LVM）产生有害输出的风险，我们引入了SafeSora数据集，以促进将文本到视频的生成与人类价值观相一致的研究。该数据集包括文本到视频生成任务中的人类偏好，主要包括两个维度：有用性和无害性。为了捕捉深入的人类偏好并促进众包工作者的结构化推理，我们将有益性细分为4个子维度，将无害性细分为12个子类别，作为试点注释的基础。SafeSora数据集包括14711个独特的提示，57333个由4个不同的LVM生成的独特视频，以及51691对由人类标记的偏好注释。我们通过几个应用程序进一步证明了SafeSora数据集的实用性，包括训练文本视频调节模型，以及通过微调提示增强模块或扩散模型使LVM与人类偏好相一致。这些应用突出了其作为文本到视频对齐研究基础的潜力，例如人类偏好建模以及对齐算法的开发和验证。 et.al.|[2406.14477](http://arxiv.org/abs/2406.14477)|**[link](https://github.com/pku-alignment/safe-sora)**|
|**2024-06-20**|**Video Generation with Learned Action Prior**|当摄像机安装在移动平台上时，随机视频生成尤其具有挑战性，因为摄像机的运动与观察到的图像像素相互作用，产生复杂的时空动力学，并使问题部分可观察到。现有的方法通常通过专注于原始像素级图像重建来解决这一问题，而不明确地对相机运动动力学建模。我们提出了一种解决方案，将相机运动或动作视为观察到的图像状态的一部分，在多模态学习框架内对图像和动作进行建模。我们介绍了三个模型：具有学习动作先验的视频生成（VG-LeAP）将图像-动作对视为单个潜在随机过程生成的增广状态，并使用变分推理来学习图像-动作-潜在先验；因果LeAP，其在时间 $t$ 建立动作和观察到的图像帧之间的因果关系，学习以观察到的图片状态为条件的动作先验；以及RAFI，它将增强图像动作状态概念集成到具有扩散生成过程的流匹配中，表明这种动作条件图像生成概念可以扩展到其他基于扩散的模型。通过对我们新的视频动作数据集RoAM的详细实证研究，我们强调了多模式训练在部分可观察视频生成问题中的重要性。 et.al.|[2406.14436](http://arxiv.org/abs/2406.14436)|null|
|**2024-06-20**|**CollaFuse: Collaborative Diffusion Models**|在生成人工智能领域，基于扩散的模型已成为生成合成图像的一种很有前途的方法。然而，扩散模型的应用带来了许多挑战，特别是在数据可用性、计算要求和隐私方面。解决这些缺点的传统方法，如联合学习，往往会给单个客户端带来巨大的计算负担，尤其是那些资源有限的客户端。为了应对这些挑战，我们引入了一种受分裂学习启发的分布式协作扩散模型的新方法。我们的方法有助于扩散模型的协同训练，同时减轻图像合成过程中的客户端计算负担。这种减少的计算负担是通过在每个客户端本地保留数据和计算成本低的过程，同时将计算成本高的过程外包给共享的、更高效的服务器资源来实现的。通过在通用CelebA数据集上的实验，我们的方法通过减少共享原始数据的必要性来增强隐私。这些功能在各个应用领域都具有巨大的潜力，包括边缘计算解决方案的设计。因此，我们的工作通过促进协作扩散模型的发展来推进分布式机器学习。 et.al.|[2406.14429](http://arxiv.org/abs/2406.14429)|**[link](https://github.com/simeonallmendinger/collafuse)**|

<p align=right>(<a href=#updated-on-20240622>back to top</a>)</p>

## NeRF

|Publish Date|Title|Abstract|PDF|Code|
|---|---|---|---|---|
|**2024-06-17**|**DistillNeRF: Perceiving 3D Scenes from Single-Glance Images by Distilling Neural Fields and Foundation Model Features**|我们提出了DistilleNeRF，这是一种自监督学习框架，解决了在自动驾驶中从有限的2D观测中理解3D环境的挑战。我们的方法是一个可推广的前馈模型，它从稀疏的单帧多视图相机输入中预测丰富的神经场景表示，并通过可微分渲染进行自监督训练，以重建RGB、深度或特征图像。我们的第一个见解是通过生成密集的深度和虚拟相机目标进行训练，利用每场景优化的神经辐射场（NeRF），从而帮助我们的模型从稀疏的非重叠图像输入中学习3D几何。其次，为了学习语义丰富的3D表示，我们建议从预先训练的2D基础模型（如CLIP或DINOv2）中提取特征，从而实现各种下游任务，而不需要昂贵的3D人工注释。为了利用这两个见解，我们引入了一种新的模型架构，该架构具有两级提升-飞溅-拍摄编码器和参数化稀疏分层体素表示。在NuScenes数据集上的实验结果表明，DistilleNeRF在场景重建、新视图合成和深度估计方面显著优于现有的可比自监督方法；并且它允许竞争性的零样本3D语义占用预测，以及通过提取的基础模型特征来理解开放世界场景。演示和代码将在https://distillnerf.github.io/. et.al.|[2406.12095](http://arxiv.org/abs/2406.12095)|null|
|**2024-06-18**|**Effective Rank Analysis and Regularization for Enhanced 3D Gaussian Splatting**|从多视图图像中进行三维重建是计算机视觉和图形学的基本挑战之一。近年来，三维高斯散射（3DGS）已经成为一种很有前途的技术，能够实时渲染和高质量的三维重建。该方法利用了三维高斯表示和基于瓦片的飞溅技术，绕过了昂贵的神经场查询。尽管3DGS具有潜力，但由于高斯收敛为具有一个主导方差的各向异性高斯，3DGS仍面临挑战，包括针状伪影、次优几何结构和不准确法线。我们建议使用有效秩分析来检查3D高斯基元的形状统计，并识别高斯确实收敛为有效秩为1的针状形状。为了解决这个问题，我们引入了有效秩作为正则化，它约束高斯的结构。我们的新正则化方法增强了法线和几何重建，同时减少了针状伪影。该方法可以作为附加模块集成到其他3DGS变体中，在不影响视觉逼真度的情况下提高其质量。 et.al.|[2406.11672](http://arxiv.org/abs/2406.11672)|null|
|**2024-06-13**|**Well-posedness and regularity of solutions to neural field problems with dendritic processing**|我们研究了最近提出的神经场模型的解决方案，在该模型中，树突被建模为源自体细胞层的垂直纤维的连续体。由于电压通过具有非局部源的电缆方程沿树枝状方向传播，因此该模型具有各向异性扩散算子以及突触耦合的积分项。因此，相应的柯西问题与经典的神经场方程明显不同。我们证明了问题的弱公式允许一个唯一的解，嵌入估计类似于非线性局部反应扩散方程的嵌入估计。我们的分析依赖于无扩散问题的扰动弱解，即标准神经场，迄今为止尚未对其弱问题进行研究。我们找到了有扩散和无扩散问题的严格渐近估计，并证明了这两个模型的解在有限时间间隔上在适当的范数下保持接近。我们提供了微扰结果的数值证据。 et.al.|[2406.09222](http://arxiv.org/abs/2406.09222)|null|
|**2024-06-13**|**Preserving Identity with Variational Score for General-purpose 3D Editing**|我们提出了Piva（用变分分数蒸馏保持同一性），这是一种新的基于优化的方法，用于编辑基于扩散模型的图像和3D模型。具体来说，我们的方法受到了最近提出的2D图像编辑方法——德尔塔去噪分数（DDS）的启发。我们指出了DDS在二维和三维编辑中的局限性，这会导致细节丢失和过饱和。为了解决这一问题，我们提出了一个额外的分数提取术语，以强制执行身份保护。这导致了更稳定的编辑过程，逐步优化NeRF模型以匹配目标提示，同时保留关键的输入特征。我们证明了我们的方法在零样本图像和神经场编辑中的有效性。我们的方法成功地改变了视觉属性，添加了微妙和实质性的结构元素，转换了形状，并在标准的2D和3D编辑基准上取得了有竞争力的结果。此外，我们的方法没有施加任何约束，如掩蔽或预训练，使其与广泛的预训练扩散模型兼容。这允许进行多功能编辑，而不需要神经场到网格的转换，提供更用户友好的体验。 et.al.|[2406.08953](http://arxiv.org/abs/2406.08953)|null|
|**2024-06-12**|**Category-level Neural Field for Reconstruction of Partially Observed Objects in Indoor Environment**|通过各种成功案例，神经隐式表示在三维重建中引起了人们的关注。对于进一步的应用，如场景理解或编辑，一些作品已经显示出在对象组成重建方面的进展。尽管它们在观测区域具有优越的性能，但在重建部分观测到的对象时，它们的性能仍然有限。为了更好地处理这个问题，我们引入了类别级神经场，该神经场在场景中属于同一类别的对象之间学习有意义的公共3D信息。我们的主要想法是根据观察到的形状对对象进行子分类，以便更好地训练类别级模型。然后，我们利用神经场，通过选择基于射线的不确定性选择的代表性对象并与之对齐，来执行配准部分观测对象的挑战性任务。在模拟和真实世界数据集上的实验表明，我们的方法改进了几个类别的未观察零件的重建。 et.al.|[2406.08176](http://arxiv.org/abs/2406.08176)|**[link](https://github.com/Taekbum/category-nerf-reconstruction-official)**|
|**2024-06-12**|**OpenObj: Open-Vocabulary Object-Level Neural Radiance Fields with Fine-Grained Understanding**|近年来，人们对由视觉语言模型（VLM）促进的开放词汇三维场景重建产生了浓厚的兴趣，VLM在开放集检索中展示了非凡的能力。然而，现有的方法面临一些局限性：它们要么专注于学习逐点特征，导致语义理解模糊，要么只处理对象级重建，从而忽略对象内部的复杂细节。为了应对这些挑战，我们引入了OpenObj，这是一种创新的方法，用于构建具有细粒度理解的开放词汇表对象级神经辐射场（NeRF）。从本质上讲，OpenObj建立了一个健壮的框架，用于在对象级别进行高效和严密的场景建模和理解。此外，我们将零件级特征融入神经领域，从而实现物体内部的细致入微的表示。这种方法捕获对象级实例，同时保持细粒度的理解。在多个数据集上的结果表明，OpenObj在零样本语义分割和检索任务中取得了优异的性能。此外，OpenObj支持多尺度的真实世界机器人任务，包括全局移动和局部操纵。 et.al.|[2406.08009](http://arxiv.org/abs/2406.08009)|**[link](https://github.com/BIT-DYN/OpenObj)**|
|**2024-06-11**|**Image Neural Field Diffusion Models**|扩散模型在对复杂数据分布建模方面表现出了令人印象深刻的能力，与GANs相比具有几个关键优势，例如稳定的训练、更好地覆盖训练分布的模式，以及在没有额外训练的情况下解决反问题的能力。然而，大多数扩散模型学习固定分辨率图像的分布。我们建议通过在图像神经场上训练扩散模型来学习连续图像的分布，该模型可以以任何分辨率渲染，并显示出其相对于固定分辨率模型的优势。为了实现这一点，一个关键的挑战是获得一个代表真实感图像神经场的潜在空间。受最近几项技术的启发，我们提出了一种简单有效的方法，但有一些关键的变化，使图像神经场具有真实感。我们的方法可以用于将现有的潜在扩散自动编码器转换为图像神经场自动编码器。我们证明，图像神经场扩散模型可以使用混合分辨率图像数据集进行训练，优于固定分辨率扩散模型和超分辨率模型，并且可以有效地解决不同尺度条件下的逆问题。 et.al.|[2406.07480](http://arxiv.org/abs/2406.07480)|null|
|**2024-06-10**|**Space-Time Continuous PDE Forecasting using Equivariant Neural Fields**|最近，条件神经场（NeF）通过将解学习为条件NeF的潜在空间中的流，已成为偏微分方程的强大建模范式。尽管受益于NeFs的有利特性，如网格不可知性和时空连续动力学建模，但这种方法限制了将PDE的已知约束强加给解决方案的能力，例如对称性或边界条件，有利于建模的灵活性。相反，我们提出了一种基于时空连续NeF的求解框架，该框架通过在潜在空间中保留几何信息，尊重PDE的已知对称性。我们表明，将解建模为感兴趣组 $G$ 上的点云流，可以提高泛化和数据效率。我们验证了我们的框架很容易推广到看不见的空间和时间位置，以及初始条件的几何变换——在其他基于NeF的PDE预测方法失败的地方——并在一些具有挑战性的几何结构中超过基线进行改进。 et.al.|[2406.06660](http://arxiv.org/abs/2406.06660)|null|
|**2024-06-11**|**LOP-Field: Brain-inspired Layout-Object-Position Fields for Robotic Scene Understanding**|空间认知使动物具有非常高效的导航能力，这在很大程度上取决于对空间环境的场景级理解。最近，人们发现，大鼠大脑嗅后皮层的神经群体比场景中的物体更能强烈地适应空间布局。受局部场景中空间布局表示的启发，我们提出了实现布局对象位置（LOP）关联的LOP域，以对机器人场景理解的层次表示进行建模。在基础模型和隐式场景表示的支持下，神经场被实现为机器人的场景存储器，存储具有位置、对象和布局信息的场景的可查询表示。为了验证所建立的LOP关联，对该模型进行了测试，以使用定量指标从3D位置推断区域信息，实现了超过88%的平均准确度。还表明，与最先进的定位方法相比，所提出的使用区域信息的方法可以在文本和RGB输入的情况下实现改进的对象和视图定位结果。 et.al.|[2406.05985](http://arxiv.org/abs/2406.05985)|null|
|**2024-06-17**|**Grounding Continuous Representations in Geometry: Equivariant Neural Fields**|最近，神经场已经成为表示连续信号的强大建模范式。在条件神经领域中，一个领域由一个潜在变量表示，该变量对NeF进行了调节，否则其参数化将在整个数据集上共享。我们提出了基于交叉注意力变换器的等变神经场，其中NeFs以几何条件变量，即潜在点云为条件，从而实现从潜在到场的等变解码。我们的等变方法引入了一个可操纵性性质，通过该性质，场和势能都以几何为基础，并服从变换定律。如果场变换，势能相应地表示变换，反之亦然。至关重要的是，等变关系确保潜在的能够（1）真实地表示几何模式，允许在潜在空间中进行几何推理，（2）在空间相似的模式上进行权重共享，允许有效地学习场的数据集。与其他非等变NeF方法相比，使用分类实验和拟合整个数据集的能力验证了这些主要特性。我们通过展示独特的局部场编辑特性，进一步验证了ENF的潜力。 et.al.|[2406.05753](http://arxiv.org/abs/2406.05753)|null|

<p align=right>(<a href=#updated-on-20240622>back to top</a>)</p>

[contributors-shield]: https://img.shields.io/github/contributors/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[contributors-url]: https://github.com/Vincentqyw/cv-arxiv-daily/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[forks-url]: https://github.com/Vincentqyw/cv-arxiv-daily/network/members
[stars-shield]: https://img.shields.io/github/stars/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[stars-url]: https://github.com/Vincentqyw/cv-arxiv-daily/stargazers
[issues-shield]: https://img.shields.io/github/issues/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[issues-url]: https://github.com/Vincentqyw/cv-arxiv-daily/issues

