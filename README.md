[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]

## Updated on 2024.05.29
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
|**2024-05-28**|**NeRAF: 3D Scene Infused Neural Radiance and Acoustic Fields**|声音在人类感知中起着重要作用，它与视觉一起提供了重要的场景信息，以了解我们的环境。尽管在神经隐式表示方面取得了进展，但学习与视觉场景相匹配的声学仍然具有挑战性。我们提出了NeRAF，这是一种联合学习声场和辐射场的方法。NeRAF被设计为Nerfstudio模块，可方便地访问逼真的视听生成。它在新的位置合成新的视图和空间化的音频，利用辐射场能力用3D场景信息调节声场。在推理时，每个模态都可以独立地呈现在空间分离的位置，从而提供更大的通用性。我们在SoundSpaces数据集上展示了我们的方法的优势。NeRAF在提高数据效率的同时，比以前的作品实现了显著的性能改进。此外，NeRAF通过跨模态学习增强了用稀疏数据训练的复杂场景的新颖视图合成。 et.al.|[2405.18213](http://arxiv.org/abs/2405.18213)|null|
|**2024-05-28**|**RT-GS2: Real-Time Generalizable Semantic Segmentation for 3D Gaussian Representations of Radiance Fields**|高斯飞溅通过实现高实时渲染性能，彻底改变了新颖视图合成的世界。最近，研究的重点是用下游任务的语义信息丰富这些3D表示。在本文中，我们介绍了RT-GS2，这是第一种使用高斯Splatting的可推广语义分割方法。虽然现有的基于高斯飞溅的方法依赖于特定场景的训练，但RT-GS2展示了推广到看不见的场景的能力。我们的方法采用了一种新的方法，首先以自监督的方式提取与视图无关的3D高斯特征，然后进行新的与视图相关/与视图无关（VDVI）的特征融合，以增强不同视图的语义一致性。在三个不同的数据集上进行的广泛实验表明，RT-GS2在语义分割质量方面优于最先进的方法，例如Replica数据集的mIoU增加了8.01%。此外，我们的方法实现了27.03 FPS的实时性能，与现有方法相比，速度提高了901倍。据我们所知，这项工作通过引入第一种用于辐射场的3D高斯表示的实时可推广语义分割方法，代表了该领域的重大进展。 et.al.|[2405.18033](http://arxiv.org/abs/2405.18033)|null|
|**2024-05-28**|**FreeSplat: Generalizable 3D Gaussian Splatting Towards Free-View Synthesis of Indoor Scenes**|赋予3D高斯飞溅以泛化能力是很有吸引力的。然而，现有的可推广的3D高斯散点方法由于其主干较重，在很大程度上局限于立体图像之间的窄范围插值，因此缺乏准确定位3D高斯并支持宽视野范围内的自由视野合成的能力。在本文中，我们提出了一种新的框架FreeSplat，它能够从长序列输入到自由视图合成重建几何一致的3D场景。具体而言，我们首先介绍了低成本跨视图聚合，该聚合通过在附近视图之间构建自适应成本体积并使用多尺度结构聚合特征来实现。随后，我们提出了逐像素三元组融合，以消除重叠视图区域中3D高斯的冗余，并聚合在多个视图中观察到的特征。此外，我们提出了一种简单但有效的自由视图训练策略，无论视图的数量如何，都能确保在更广泛的视图范围内进行稳健的视图合成。我们的经验结果表明，在不同数量的输入视图中，新视图渲染的颜色图质量和深度图精度都具有最先进的新视图合成性能。我们还表明，FreeSplat可以更有效地执行推理，并可以有效地减少冗余高斯，为无深度先验的前馈大场景重建提供了可能性。 et.al.|[2405.17958](http://arxiv.org/abs/2405.17958)|null|
|**2024-05-28**|**A Refined 3D Gaussian Representation for High-Quality Dynamic Scene Reconstruction**|近年来，神经辐射场（NeRF）以其隐式表示方式彻底改变了三维重建。基于NeRF，3D高斯飞溅（3D-GS）已经脱离了神经网络的隐式表示，而是直接将场景表示为具有高斯形状分布的点云。虽然这种转变显著提高了辐射场的渲染质量和速度，但不可避免地导致了内存使用量的显著增加。此外，在3D-GS中有效地渲染动态场景已经成为一个紧迫的挑战。为了解决这些问题，本文提出了一种用于高质量动态场景重建的精细3D高斯表示。首先，我们使用可变形多层感知器（MLP）网络来捕捉高斯点的动态偏移，并通过哈希编码和微小的MLP来表达点的颜色特征，以减少存储需求。随后，我们引入了一种可学习的去噪掩模，结合去噪损失来消除场景中的噪声点，从而进一步压缩3D高斯模型。最后，通过静态约束和运动一致性约束来减轻点的运动噪声。实验结果表明，我们的方法在渲染质量和速度方面优于现有方法，同时显著减少了与3D-GS相关的内存使用，使其非常适合于各种任务，如新颖的视图合成和动态映射。 et.al.|[2405.17891](http://arxiv.org/abs/2405.17891)|null|
|**2024-05-28**|**Mani-GS: Gaussian Splatting Manipulation with Triangular Mesh**|神经3D表示，如神经辐射场（NeRF），擅长产生逼真的渲染结果，但缺乏对内容创建至关重要的操作和编辑灵活性。先前的工作试图通过在规范空间中变形NeRF或基于显式网格操纵辐射场来解决这个问题。然而，操纵NeRF不是高度可控的，并且需要长的训练和推理时间。随着3D高斯散射（3DGS）的出现，使用基于显式点的3D表示可以以更快的训练和渲染速度实现极高保真度的新视图合成。然而，仍然缺乏在保持渲染质量的同时自由操作3DGS的有效手段。在这项工作中，我们的目标是解决实现可操作的照片真实感渲染的挑战。我们建议利用三角形网格直接自适应地操作3DGS。这种方法减少了为不同类型的高斯操作设计各种算法的需要。利用三角形状感知的高斯绑定和自适应方法，可以实现3DGS操作，并在操作后保持高保真度渲染。我们的方法能够处理大变形、局部操作和柔体模拟，同时保持高质量的渲染。此外，我们还证明了我们的方法在处理从3DGS中提取的不准确网格时也是有效的。进行的实验证明了我们的方法的有效性及其优于基线方法的优势。 et.al.|[2405.17811](http://arxiv.org/abs/2405.17811)|null|
|**2024-05-28**|**SafeguardGS: 3D Gaussian Primitive Pruning While Avoiding Catastrophic Scene Destruction**|三维高斯散射（3DGS）在新视图合成方面迈出了重要的一步，在实现实时渲染速度的同时，展现了一流的渲染质量。然而，3DGS的次优致密化过程导致了过多的高斯基元，这带来了一个重大挑战，降低了每秒帧数（FPS），并要求相当大的内存成本，这对低端设备不利。为了解决这个问题，许多后续研究提出了各种修剪技术，通常与不同的分数函数相结合，以优化渲染性能。尽管如此，关于其有效性和对所有技术的影响的全面讨论仍然缺失。在本文中，我们首先将3DGS修剪技术分为两种类型：跨视图修剪和逐像素修剪，这两种技术在对基元进行排序的方法上有所不同。我们随后的实验表明，虽然在极端高斯基元抽取下，交叉视图修剪会导致灾难性的质量下降，但逐像素修剪技术不仅在性能下降很小的情况下保持了相对较高的渲染质量，而且还为修剪提供了合理的最小边界。基于这一观察，我们进一步提出了分数函数的多种变体，并根据经验发现，颜色加权分数函数在区分用于渲染的不重要基元方面优于其他函数。我们相信，我们的研究为优化未来作品的3DGS修剪策略提供了有价值的见解。 et.al.|[2405.17793](http://arxiv.org/abs/2405.17793)|null|
|**2024-05-27**|**DC-Gaussian: Improving 3D Gaussian Splatting for Reflective Dash Cam Videos**|我们提出了DC高斯，一种从车载行车记录仪视频中生成新视图的新方法。虽然神经渲染技术在驾驶场景中取得了重大进展，但现有的方法主要是为自动驾驶汽车收集的视频设计的。然而，与行车记录仪视频相比，这些视频在数量和多样性方面都有限，行车记录仪视频更广泛地用于各种类型的车辆，并捕捉更广泛的场景。行车记录仪视频经常会遇到严重的障碍，如挡风玻璃上的反射和遮挡，这严重阻碍了神经渲染技术的应用。为了应对这一挑战，我们在最近的实时神经渲染技术3D高斯飞溅（3DGS）的基础上开发了DC高斯。我们的方法包括一个自适应图像分解模块，以统一的方式对反射和遮挡进行建模。此外，我们引入了照明感知障碍建模，以管理不同照明条件下的反射和遮挡。最后，我们采用几何引导的高斯增强策略，通过引入额外的几何先验来改善渲染细节。在自拍和公共行车记录仪视频上的实验表明，我们的方法不仅在新颖的视图合成方面取得了最先进的性能，而且可以准确地重建拍摄的场景，消除障碍。 et.al.|[2405.17705](http://arxiv.org/abs/2405.17705)|null|
|**2024-05-27**|**DOF-GS: Adjustable Depth-of-Field 3D Gaussian Splatting for Refocusing,Defocus Rendering and Blur Removal**|基于3D高斯散射的技术最近推进了3D场景重建和新颖的视图合成，实现了高质量的实时渲染。然而，这些方法在建模图像时受到针孔相机假设的固有限制，因此仅适用于全聚焦（AiF）清晰图像输入。这严重影响了它们在真实世界场景中的适用性，其中由于成像设备的有限景深（DOF），图像经常表现出散焦模糊。此外，现有的三维高斯散射（3DGS）方法也不支持DOF效果的渲染。为了解决这些挑战，我们引入了DOF-GS，它允许渲染可调节的DOF效果，消除散焦模糊以及重新聚焦3D场景，所有这些都来自因散焦模糊而退化的多视图图像。为此，我们通过使用有限孔径相机模型，结合由混淆圆（CoC）引导的显式、可微分散焦渲染，重新想象传统的高斯散射管道。所提出的框架通过按需改变底层相机模型的光圈和焦距来提供DOF效果的动态调整。它还能够在优化后渲染3D场景的不同DOF效果，并从散焦训练图像生成AiF图像。此外，我们设计了一种联合优化策略，通过联合优化渲染的散焦图像和AiF图像来进一步增强重建场景中的细节。我们的实验结果表明，DOF-GS在受散焦模糊影响的输入的条件下产生高质量的清晰全聚焦渲染，训练过程仅导致GPU内存消耗的适度增加。我们进一步展示了所提出的方法在可调散焦渲染和从因散焦模糊而退化的输入图像重新聚焦3D场景中的应用。 et.al.|[2405.17351](http://arxiv.org/abs/2405.17351)|null|
|**2024-05-27**|**GenWarp: Single Image to Novel Views with Semantic-Preserving Generative Warping**|由于3D场景的复杂性和现有多视图数据集训练模型的多样性有限，从单个图像生成新视图仍然是一项具有挑战性的任务。最近的研究将大规模文本到图像（T2I）模型与单目深度估计（MDE）相结合，在处理野生图像方面显示出了前景。在这些方法中，输入视图被几何扭曲为具有估计的深度图的新视图，然后扭曲的图像被T2I模型修复。然而，当将输入视图扭曲为新颖的视点时，它们很难处理嘈杂的深度图和语义细节的丢失。在本文中，我们提出了一种新的单镜头新视图合成方法，这是一种语义保持的生成扭曲框架，通过用自注意增强跨视图注意力，使T2I生成模型能够学习在哪里扭曲和在哪里生成。我们的方法通过将生成模型以源视图图像为条件并结合几何扭曲信号来解决现有方法的局限性。定性和定量评估表明，我们的模型在域内和域外场景中都优于现有方法。项目页面位于https://GenWarp-NVS.github.io/. et.al.|[2405.17251](http://arxiv.org/abs/2405.17251)|null|
|**2024-05-24**|**Feature Splatting for Better Novel View Synthesis with Low Overlap**|3D高斯飞溅已经成为一种非常有前途的场景表示，在新的视图合成中实现最先进的质量明显快于竞争对手。然而，它使用球面谐波来表示场景颜色限制了3D高斯的表现力，因此，当我们离开训练视图时，该表示的泛化能力也受到了限制。在本文中，我们提出将3D高斯的颜色信息编码为每高斯特征向量，我们将其表示为特征飞溅（FeatSplat）。为了合成一个新的视图，首先将高斯“飞溅”到图像平面中，然后对相应的特征向量进行阿尔法混合，最后通过小MLP对混合向量进行解码，以渲染RGB像素值。为了进一步告知模型，我们将相机嵌入连接到混合特征向量，以使解码也以视点信息为条件。我们的实验表明，这些用于编码辐射的新模型显著改进了远离训练视图的低重叠视图的新视图合成。最后，我们还展示了我们的特征向量表示的能力和便利性，展示了它不仅能够为新视图生成RGB值，而且能够生成其每像素语义标签。我们将在接受后发布代码。关键词：高斯散射、新视图合成、特征散射 et.al.|[2405.15518](http://arxiv.org/abs/2405.15518)|null|

<p align=right>(<a href=#updated-on-20240529>back to top</a>)</p>

## 3D Reconstruction

|Publish Date|Title|Abstract|PDF|Code|
|---|---|---|---|---|
|**2024-05-28**|**FreeSplat: Generalizable 3D Gaussian Splatting Towards Free-View Synthesis of Indoor Scenes**|赋予3D高斯飞溅以泛化能力是很有吸引力的。然而，现有的可推广的3D高斯散点方法由于其主干较重，在很大程度上局限于立体图像之间的窄范围插值，因此缺乏准确定位3D高斯并支持宽视野范围内的自由视野合成的能力。在本文中，我们提出了一种新的框架FreeSplat，它能够从长序列输入到自由视图合成重建几何一致的3D场景。具体而言，我们首先介绍了低成本跨视图聚合，该聚合通过在附近视图之间构建自适应成本体积并使用多尺度结构聚合特征来实现。随后，我们提出了逐像素三元组融合，以消除重叠视图区域中3D高斯的冗余，并聚合在多个视图中观察到的特征。此外，我们提出了一种简单但有效的自由视图训练策略，无论视图的数量如何，都能确保在更广泛的视图范围内进行稳健的视图合成。我们的经验结果表明，在不同数量的输入视图中，新视图渲染的颜色图质量和深度图精度都具有最先进的新视图合成性能。我们还表明，FreeSplat可以更有效地执行推理，并可以有效地减少冗余高斯，为无深度先验的前馈大场景重建提供了可能性。 et.al.|[2405.17958](http://arxiv.org/abs/2405.17958)|null|
|**2024-05-28**|**A Refined 3D Gaussian Representation for High-Quality Dynamic Scene Reconstruction**|近年来，神经辐射场（NeRF）以其隐式表示方式彻底改变了三维重建。基于NeRF，3D高斯飞溅（3D-GS）已经脱离了神经网络的隐式表示，而是直接将场景表示为具有高斯形状分布的点云。虽然这种转变显著提高了辐射场的渲染质量和速度，但不可避免地导致了内存使用量的显著增加。此外，在3D-GS中有效地渲染动态场景已经成为一个紧迫的挑战。为了解决这些问题，本文提出了一种用于高质量动态场景重建的精细3D高斯表示。首先，我们使用可变形多层感知器（MLP）网络来捕捉高斯点的动态偏移，并通过哈希编码和微小的MLP来表达点的颜色特征，以减少存储需求。随后，我们引入了一种可学习的去噪掩模，结合去噪损失来消除场景中的噪声点，从而进一步压缩3D高斯模型。最后，通过静态约束和运动一致性约束来减轻点的运动噪声。实验结果表明，我们的方法在渲染质量和速度方面优于现有方法，同时显著减少了与3D-GS相关的内存使用，使其非常适合于各种任务，如新颖的视图合成和动态映射。 et.al.|[2405.17891](http://arxiv.org/abs/2405.17891)|null|
|**2024-05-27**|**Memorize What Matters: Emergent Scene Decomposition from Multitraverse**|人类自然会保留对永恒元素的记忆，而短暂的时刻往往会从记忆的缝隙中溜走。这种选择性保留对于机器人感知、定位和绘图至关重要。为了赋予机器人这种能力，我们引入了3D高斯映射（3DGM），这是一种基于3D高斯飞溅的自监督、仅限相机的离线映射框架。3DGM将来自同一区域的多遍历RGB视频转换为基于高斯的环境图，同时执行2D短暂对象分割。我们的主要观察结果是，环境在遍历中保持一致，而对象经常发生变化。这使我们能够利用重复遍历的自我监督来实现环境对象分解。更具体地说，3DGM将多遍历环境映射公式化为一个鲁棒的可微渲染问题，将环境和对象的像素分别视为内值和外值。3DGM使用稳健特征提取、特征残差挖掘和稳健优化，在没有人工干预的情况下联合执行3D映射和2D分割。我们建立了Mapverse基准，来源于伊萨卡365和nuPlan数据集，以评估我们在无监督二维分割、三维重建和神经渲染中的方法。大量结果验证了我们的方法在自动驾驶和机器人方面的有效性和潜力。 et.al.|[2405.17187](http://arxiv.org/abs/2405.17187)|null|
|**2024-05-27**|**SDL-MVS: View Space and Depth Deformable Learning Paradigm for Multi-View Stereo Reconstruction in Remote Sensing**|基于遥感图像的多视角立体研究促进了大规模城市三维重建的发展。然而，遥感多视点图像数据在获取过程中存在遮挡和视点之间亮度不均匀的问题，这导致了深度估计中细节模糊的问题。为了解决上述问题，我们重新审视了多视图立体任务中的可变形学习方法，并提出了一种基于视图空间和深度可变形学习（SDL-MVS）的新范式，旨在学习不同视图空间中特征的可变形交互，并对深度范围和区间进行可变形建模，以实现高精度的深度估计。具体来说，为了解决遮挡和亮度不均匀导致的视图噪声问题，我们提出了一种渐进空间可变形采样（PSS）机制，该机制以渐进的方式对3D截头体空间和2D图像空间中的采样点进行可变形学习，以自适应地将源特征嵌入到参考特征中。为了进一步优化深度，我们引入了深度假设可变形离散化（DHD），它通过自适应调整深度范围假设和对深度区间假设进行可变形离散来实现深度先验的精确定位。最后，我们的SDL-MVS通过视图空间和深度的可变形学习范式，实现了多视图立体中遮挡和亮度不均的显式建模，实现了精确的多视图深度估计。在珞珈MVS和WHU数据集上进行的大量实验表明，我们的SDL-MVS达到了最先进的性能。值得注意的是，在三个视图作为输入的前提下，我们的SDL-MVS在珞珈MVS数据集上实现了0.086的MAE误差，<0.6米的准确率为98.9%，<3区间的准确度为98.9%。 et.al.|[2405.17140](http://arxiv.org/abs/2405.17140)|null|
|**2024-05-27**|**DINO-SD: Champion Solution for ICRA 2024 RoboDepth Challenge**|环绕视图深度估计是一项关键任务，旨在获取周围视图的深度图。它在自动驾驶、AR/VR和3D重建等现实场景中有许多应用。然而，鉴于自动驾驶数据集中的大部分数据都是在白天场景中收集的，这导致深度模型在面对分布外（OoD）数据时性能较差。虽然一些工作试图提高OoD数据下深度模型的稳健性，但这些方法要么需要额外的训练数据，要么需要湖的可推广性。在本报告中，我们介绍了DINO-SD，一种新的环绕视图深度估计模型。我们的DINO-SD不需要额外的数据，并且具有很强的稳健性。我们的DINO-SD在ICRA 2024机器人深度挑战赛的赛道4中获得最佳表现。 et.al.|[2405.17102](http://arxiv.org/abs/2405.17102)|null|
|**2024-05-27**|**Part123: Part-aware 3D Reconstruction from a Single-view Image**|最近，扩散模型的出现为单视图重建开辟了新的机会。然而，所有现有的方法都将目标对象表示为没有任何结构信息的闭合网格，从而忽略了重建形状的基于零件的结构，这对许多下游应用至关重要。此外，生成的网格通常会遇到大噪声、表面不光滑和纹理模糊的问题，这使得使用3D分割技术获得令人满意的零件分割具有挑战性。在本文中，我们提出了Part123，这是一种从单视图图像进行零件感知三维重建的新框架。我们首先使用扩散模型从给定的图像中生成多视角一致的图像，然后利用对任意对象表现出强大泛化能力的分段任意模型（SAM）来生成多视角分割掩模。为了有效地将基于2D零件的信息纳入3D重建并处理不一致性，我们将对比学习引入神经渲染框架，以学习基于多视图分割掩模的零件感知特征空间。还开发了一种基于聚类的算法，以从重建的模型中自动导出3D零件分割结果。实验表明，我们的方法可以在各种物体上生成具有高质量分割部分的三维模型。与现有的非结构化重建方法相比，该方法中的零件感知三维模型有利于一些重要的应用，包括特征保持重建、基元拟合和三维形状编辑。 et.al.|[2405.16888](http://arxiv.org/abs/2405.16888)|null|
|**2024-05-28**|**3D Reconstruction with Fast Dipole Sums**|我们介绍了一种从多视图图像重建高保真表面的技术。我们的技术使用了一种新的基于点的表示，即偶极和，它推广了绕组数，以允许在具有噪声或异常点的点云中对任意每点属性进行插值。使用偶极和，我们可以根据点云的点属性来表示隐含的几何和辐射场，我们可以直接从运动的结构中初始化点云。我们还推导了用于加速正向和反向模式偶极和查询的Barnes-Hut快速求和方案。这些查询有助于使用光线跟踪，以使用基于点的表示高效且可微分地渲染图像，从而更新其点属性以优化场景几何体和外观。我们根据最先进的替代方案，基于神经表示的光线跟踪或基于高斯点的表示的光栅化，来评估这种反向渲染框架。我们的技术在同等运行时间显著提高了重建质量，同时还支持更通用的渲染技术，如用于直接照明的阴影光线。在补充中，我们提供了结果的交互式可视化。 et.al.|[2405.16788](http://arxiv.org/abs/2405.16788)|null|
|**2024-05-26**|**Splat-SLAM: Globally Optimized RGB-only SLAM with 3D Gaussians**|3D Gaussian Splatting已成为仅RGB密集同时定位和映射（SLAM）的几何和外观的强大表示，因为它提供了紧凑的密集地图表示，同时实现了高效和高质量的地图渲染。然而，现有方法显示出比使用其他3D表示（如神经点云）的竞争方法差得多的重建质量，因为它们要么不采用全局地图和姿态优化，要么利用单目深度。作为回应，我们提出了第一个具有密集3D高斯图表示的仅RGB SLAM系统，该系统通过主动变形3D高斯图来动态适应关键帧姿态和深度更新，从而利用全局优化跟踪的所有好处。此外，我们发现，用单目深度估计器细化不准确区域的深度更新进一步提高了3D重建的准确性。我们在Replica、TUM-RGBD和ScanNet数据集上的实验表明了全局优化的3D高斯的有效性，因为该方法在跟踪、映射和渲染精度方面与现有的仅RGB的SLAM方法实现了卓越或不相上下的性能，同时产生了小的地图大小和快速的运行时间。源代码位于https://github.com/eriksandstroem/Splat-SLAM. et.al.|[2405.16544](http://arxiv.org/abs/2405.16544)|null|
|**2024-05-25**|**Neural Network-Based Tracking and 3D Reconstruction of Baseball Pitch Trajectories from Single-View 2D Video**|在本文中，我们提出了一种基于神经网络的方法，用于跟踪和重建棒球场从2D视频片段到3D坐标的轨迹。我们利用OpenCV的CSRT算法来准确跟踪2D视频帧中的棒球和固定参考点。然后，这些跟踪的像素坐标被用作我们的神经网络模型的输入特征，该模型包括多个完全连接的层，以将2D坐标映射到3D空间。该模型使用均方误差损失函数和Adam优化器在标记轨迹的数据集上进行训练，优化网络以最大限度地减少预测误差。我们的实验结果表明，这种方法在从2D输入重建3D轨迹时实现了高精度。这种方法在运动分析、指导和提高各种运动轨迹预测的准确性方面显示出巨大的应用潜力。 et.al.|[2405.16296](http://arxiv.org/abs/2405.16296)|null|
|**2024-05-25**|**3D reconstruction of a million atoms by multiple-section local-orbital tomography**|存在两组能够提供物体的三维（3D）结构信息的电子显微镜方法，即电子断层扫描和深度切片。电子断层扫描能够在所有三维中解析原子，但原子位置的精度较低，并且可以重建的物体尺寸有限。深度切片方法在成像平面中给出高的位置精度，但在第三维中的空间分辨率低。在这项工作中，电子断层扫描和深度切片相结合，形成了一种称为多切片局部轨道断层扫描的方法，简称nLOT。nLOT方法在所有三维中提供高空间分辨率和高位置精度。可以重建的物体大小被扩展到一百万个原子。本方法为原子电子层析成像的广泛应用奠定了基础。 et.al.|[2405.16007](http://arxiv.org/abs/2405.16007)|null|

<p align=right>(<a href=#updated-on-20240529>back to top</a>)</p>

## Diffusion

|Publish Date|Title|Abstract|PDF|Code|
|---|---|---|---|---|
|**2024-05-28**|**On the Origin of Llamas: Model Tree Heritage Recovery**|互联网上共享的神经网络模型的快速增长使模型权重成为一种重要的数据形式。然而，这些信息没有得到充分利用，因为权重无法解释，并且公开可用的模型杂乱无章。受达尔文生命树的启发，我们定义了模型树，它描述了模型的起源，即用于微调目标模型的父模型。与自然界相似，树的结构是未知的。在本文中，我们介绍了模型树遗产恢复（MoTHer Recovery）的任务，用于在不断增长的神经网络领域中发现模型树。我们的假设是，模型权重对这些信息进行编码，挑战在于在给定权重的情况下解码底层的树结构。除了模型作者归因的即时应用之外，MoTHer恢复还具有令人兴奋的长期应用，类似于搜索引擎对互联网进行索引。实际上，对于每对模型，这项任务需要：i）确定它们是否相关，以及ii）确定关系的方向。我们发现，在训练过程中，权重的某些分布性质是单调演化的，这使我们能够对两个给定模型之间的关系进行分类。MoTHer恢复重建整个模型层次结构，由有向树表示，其中父模型通过额外的训练产生多个子模型。我们的方法成功地重建了复杂的模型树，以及“野外”模型族的结构，如Llama 2和Stable Diffusion。 et.al.|[2405.18432](http://arxiv.org/abs/2405.18432)|null|
|**2024-05-28**|**DiG: Scalable and Efficient Diffusion Models with Gated Linear Attention**|具有大规模预训练的扩散模型在视觉内容生成领域取得了重大成功，尤其是以扩散变压器（DiT）为例。然而，DiT模型在可扩展性和二次复杂度效率方面面临挑战。在本文中，我们的目标是利用门控线性注意力（GLA）变换器的长序列建模能力，将其扩展到扩散模型。我们介绍了扩散门线性注意力变换器（DiG），这是一种简单、可采用的解决方案，具有最小的参数开销，遵循DiT设计，但提供了卓越的效率和有效性。除了比DiT更好的性能外，DiG-S/2的训练速度比DiT-S/2高2.5倍，并且在1792倍的分辨率下节省了75.7%的GPU内存。此外，我们还分析了DiG在各种计算复杂度下的可扩展性。随着深度/宽度的增加或输入标记的增加，DiG模型始终表现出FID的减少。我们进一步将DiG与其他次二次时间扩散模型进行了比较。在相同的模型尺寸下，DiG XL/2在1024 $分辨率下比最近的基于曼巴的扩散模型快4.2\倍$，在2048$分辨率下，比使用CUDA优化的FlashAttention-2的DiT快1.8\倍$ 。所有这些结果都证明了它在最新的扩散模型中具有优越的效率。代码发布于https://github.com/hustvl/DiG. et.al.|[2405.18428](http://arxiv.org/abs/2405.18428)|null|
|**2024-05-28**|**Phased Consistency Model**|一致性模型（CM）最近在加速生成扩散模型方面取得了重大进展。然而，它在潜在空间中的高分辨率、文本条件图像生成（又称LCM）中的应用仍然不令人满意。在本文中，我们确定了LCM当前设计中的三个关键缺陷。我们研究了这些限制背后的原因，并提出了分阶段一致性模型（PCM），该模型概括了设计空间并解决了所有已确定的限制。我们的评估表明，PCM在1-16步生成设置中显著优于LCM。虽然PCM是专门为多步细化而设计的，但它实现了比以前最先进的专门设计的一步方法更优越或可比的一步生成结果。此外，我们还展示了PCM的方法是通用的，适用于视频生成，使我们能够训练最先进的几步文本到视频生成器。更多详细信息，请访问https://g-u-n.github.io/projects/pcm/. et.al.|[2405.18407](http://arxiv.org/abs/2405.18407)|null|
|**2024-05-28**|**RACCooN: Remove, Add, and Change Video Content with Auto-Generated Narratives**|最近的视频生成模型主要依靠精心编写的文本提示来完成特定任务，如修复或风格编辑。它们需要对输入视频进行劳动密集型的文本描述，这阻碍了它们根据用户规范调整个人/原始视频的灵活性。本文提出了RACCooN，这是一个通用且用户友好的视频到段落到视频生成框架，通过统一的管道支持多种视频编辑功能，如删除、添加和修改。RACCooN由两个主要阶段组成：视频到段落（V2P）和段落到视频（P2V）。在V2P阶段，我们用结构良好的自然语言自动描述视频场景，捕捉整体上下文和聚焦对象的细节。随后，在P2V阶段，用户可以选择性地细化这些描述以指导视频扩散模型，从而能够对输入视频进行各种修改，例如移除、改变主题和/或添加新对象。所提出的方法通过几个重要贡献从其他方法中脱颖而出：（1）RACCooN提出了一种多粒度时空池策略，以生成结构良好的视频描述，在不需要复杂的人工注释的情况下捕获广泛的上下文和对象细节，简化了用户基于文本的精确视频内容编辑。（2） 我们的视频生成模型结合了自动生成的叙述或指令，以提高生成内容的质量和准确性。它支持在统一的框架内添加视频对象、修复和属性修改，超越了现有的视频编辑和修复基准。所提出的框架在视频到段落生成、视频内容编辑方面展示了令人印象深刻的多功能能力，并可被纳入其他SoTA视频生成模型中进行进一步增强。 et.al.|[2405.18406](http://arxiv.org/abs/2405.18406)|null|
|**2024-05-28**|**Short-time Fokker-Planck propagator beyond the Gaussian approximation**|我们提出了一种微扰方法来计算一维福克-普朗克方程的短时间传播子或跃迁密度，原则上按时间增量的任意顺序计算。我们的方法准确地保留了概率，并允许我们评估分析可观察性的期望值，原则上达到任意精度；为了证明这一点，我们推导了空间增量矩、有限时间Kramers-Moyal系数和平均介质熵产生率的扰动展开式。对于具有可用解析解的显式乘性噪声系统，我们验证了所有的微扰结果。在整个过程中，我们将我们的微扰结果与从广泛使用的短时传播子的高斯近似中获得的结果进行了比较；我们证明了这种高斯传播子导致的误差可能比我们的微扰方法产生的误差大很多数量级。我们的结果的潜在应用包括从观测到的时间序列中参数化扩散随机动力学，以及对随机轨迹的路径空间进行数值采样。 et.al.|[2405.18381](http://arxiv.org/abs/2405.18381)|null|
|**2024-05-28**|**A Hessian-Aware Stochastic Differential Equation for Modelling SGD**|随机梯度下降（SGD）的连续时间近似是研究其从平稳点逃逸行为的重要工具。然而，现有的随机微分方程（SDE）模型无法完全捕捉这些行为，即使是对于简单的二次目标也是如此。基于一种新的随机后向误差分析框架，我们推导出了Hessian Aware随机修正方程（HA-SME），这是一种将目标函数的Hessian信息纳入其漂移项和扩散项的SDE。我们的分析表明，HA-SME与文献中现有的SDE模型中的阶最佳逼近误差保证相匹配，同时显著降低了对目标平滑度参数的依赖性。此外，对于二次目标，在温和条件下，HA-SME被证明是第一个在分布意义上准确恢复SGD动力学的SDE模型。因此，当固定点附近的局部景观可以用二次方法近似时，HA-SME有望准确预测SGD的局部逃逸行为。 et.al.|[2405.18373](http://arxiv.org/abs/2405.18373)|null|
|**2024-05-28**|**Simulating infinite-dimensional nonlinear diffusion bridges**|扩散桥是一种以在有限时间内达到特定状态为条件的扩散过程。它在贝叶斯推理、金融数学、控制理论和形状分析等领域有着广泛的应用。然而，由于漂移项和数据的连续表示的复杂性，模拟自然数据的扩散桥可能具有挑战性。尽管有几种方法可用于模拟有限维扩散桥，但无限维的情况仍未解决。在本文中，我们通过将分数匹配技术与算子学习相结合，提出了一种解决这一问题的方法，从而为无限维桥梁的分数匹配提供了一种直接的方法。我们将分数构造为离散不变，这在给定潜在的空间连续过程的情况下是自然的。我们进行了一系列实验，从具有闭合形式解的合成示例到真实世界生物形状数据的随机非线性演化，我们的方法表现出了很高的效率，特别是由于它能够在没有额外训练的情况下适应任何分辨率。 et.al.|[2405.18353](http://arxiv.org/abs/2405.18353)|null|
|**2024-05-28**|**VITON-DiT: Learning In-the-Wild Video Try-On from Human Dance Videos via Diffusion Transformers**|视频试穿因其巨大的现实世界潜力而成为一个有前景的领域。之前的工作仅限于将产品服装图像转移到具有简单姿势和背景的人物视频上，而在随意拍摄的视频上表现不佳。最近，Sora展示了Diffusion Transformer（DiT）在生成具有真实世界场景的逼真视频方面的可扩展性。受此启发，我们探索并提出了第一个用于实际应用的基于DiT的视频试穿框架，名为VITON DiT。具体来说，VITON DiT由服装提取器、时空去噪DiT和身份保护控制网组成。为了忠实地恢复服装细节，将提取的服装特征与去噪DiT和ControlNet的自注意输出相融合。我们还在训练中引入了新的随机选择策略，并在推理中引入了插值自回归（IAR）技术，以促进长视频的生成。与现有的需要费力和限制性地构建配对训练数据集的尝试不同，VITON DiT仅依靠未配对的人类舞蹈视频和精心设计的多阶段训练策略来缓解这种情况，这严重限制了其可扩展性。此外，我们策划了一个具有挑战性的基准数据集来评估随意视频试穿的性能。大量实验证明了VITON DiT在为具有复杂人体姿势的野外视频生成时空一致试穿结果方面的优势。 et.al.|[2405.18326](http://arxiv.org/abs/2405.18326)|null|
|**2024-05-28**|**Multi-modal Generation via Cross-Modal In-Context Learning**|在这项工作中，我们研究了从复杂的多模式提示序列生成新图像的问题。虽然现有的方法在文本到图像生成方面取得了很好的结果，但它们往往难以从冗长的提示中捕捉到细粒度的细节，并在提示序列中保持上下文连贯性。此外，它们经常导致以多个对象为特征的提示序列的图像生成不对齐。为了解决这一问题，我们提出了一种通过跨模态上下文学习（MGCC）的多模态生成方法，该方法通过利用大型语言模型（LLM）和扩散模型的组合能力，从复杂的多模态提示序列中生成新的图像。我们的MGCC包括一个新颖的跨模态优化模块，用于显式学习LLM嵌入空间中文本和图像之间的跨模态依赖关系，以及一个上下文对象基础模块，用于生成专门针对具有多个对象的场景的对象边界框。我们的MGCC展示了多种多样的多模式能力，如新颖的图像生成、促进多模式对话和文本生成。在两个基准数据集上的实验评估证明了我们方法的有效性。在具有多模式输入的视觉故事生成（VIST）数据集上，与SOTA GILL 0.641 $相比，我们的MGCC实现了0.652$ 的CLIP相似性得分。同样，在具有长对话序列的视觉对话上下文（VisDial）上，我们的MGCC获得了令人印象深刻的0.660美元的CLIP得分，大大优于现有的0.645美元的SOTA方法。密码https://github.com/VIROBO-15/MGCC et.al.|[2405.18304](http://arxiv.org/abs/2405.18304)|null|
|**2024-05-28**|**CT-based brain ventricle segmentation via diffusion Schrödinger Bridge without target domain ground truths**|从临床CT扫描中高效准确地分割脑心室对于脑室切开术等紧急手术至关重要。鉴于软组织对比度差的挑战和临床脑CT注释良好的数据库的稀缺性，我们引入了一种新的不确定性感知心室分割技术，通过利用基于扩散模型的域自适应，无需CT分割基本事实。具体而言，我们的方法使用扩散Schr“odinger Bridge和注意力递归残差U-Net来利用不成对的CT和MRI扫描，从MRI扫描中获得更容易访问的自动CT分割。重要的是，我们提出了一个图像翻译和分割任务的端到端联合训练框架，并证明了其相对于单独训练单个任务的优势。通过将所提出的方法与使用两种不同GAN模型进行域自适应（CycleGAN和CUT）的类似设置进行比较，我们还揭示了扩散模型在提高分割和图像翻译质量方面的优势。Dice得分为0.78 $\pm$ 0.27，我们提出的方法优于包括SynSeg-Net在内的比较方法，同时提供了直观的不确定性以进一步促进自动分割结果的质量控制的措施。 et.al.|[2405.18267](http://arxiv.org/abs/2405.18267)|null|

<p align=right>(<a href=#updated-on-20240529>back to top</a>)</p>

## NeRF

|Publish Date|Title|Abstract|PDF|Code|
|---|---|---|---|---|
|**2024-05-27**|**Extreme Compression of Adaptive Neural Images**|隐式神经表示（INRs）和神经场是一种新的信号表示范式，从图像和音频到3D场景和视频。其基本思想是将信号表示为连续且可微分的神经网络。这一思想提供了前所未有的优势，如连续分辨率和存储效率，从而实现了新的压缩技术。然而，将数据表示为神经网络带来了新的挑战。例如，给定一个2D图像作为神经网络，我们如何进一步压缩这样的神经图像？。在这项工作中，我们提出了一种新的压缩神经场的分析，重点是图像。我们还介绍了自适应神经图像（ANI），这是一种有效的神经表示，能够适应不同的推理或传输要求。我们提出的方法可以将神经图像的每像素比特数（bpp）减少4倍，而不会丢失敏感细节或损害保真度。我们之所以能做到这一点，是因为我们成功地实现了4位神经表示。我们的工作为开发压缩神经场提供了一个新的框架。 et.al.|[2405.16807](http://arxiv.org/abs/2405.16807)|null|
|**2024-05-24**|**Blaze3DM: Marry Triplane Representation with Diffusion for 3D Medical Inverse Problem Solving**|解决图像恢复和重建等三维医学逆问题在现代医学领域至关重要。然而，3D医疗数据中的维度诅咒导致主流的体积方法遭受高资源消耗，并挑战模型成功捕捉自然分布，导致不可避免的体积不一致和伪影。最近的一些工作试图简化潜在空间中的生成，但缺乏对复杂图像细节进行有效建模的能力。为了解决这些局限性，我们提出了Blaze3DM，这是一种新的方法，通过集成紧凑的三平面神经场和强大的扩散模型，实现了快速高保真的生成。在技术上，Blaze3DM首先同时优化数据相关的三平面嵌入和共享解码器，将每个三平面重建回相应的3D体积。为了进一步增强3D一致性，我们引入了一个轻量级的3D感知模块来对三个垂直平面的相关性进行建模。然后，在潜在的三平面嵌入上训练扩散模型，并实现无条件和有条件的三平面生成，最终解码为任意大小的体积。对零样本三维医学逆问题求解的大量实验，包括稀疏视图CT、有限角度CT、压缩传感MRI和MRI各向同性超分辨率，表明Blaze3DM不仅实现了最先进的性能，而且显著提高了现有方法的计算效率（比以前的工作快22~40倍）。 et.al.|[2405.15241](http://arxiv.org/abs/2405.15241)|null|
|**2024-05-17**|**SNF-ROM: Projection-based nonlinear reduced order modeling with smooth neural fields**|降阶建模通过从数据中学习低阶空间表示并使用控制方程的流形投影动态演化这些表示，降低了求解偏微分方程的计算成本。虽然通常使用线性子空间降阶模型（ROM），但对于Kolmogorov $n$ -宽度缓慢衰减的问题，例如高雷诺数下以平流为主的流体流动，通常是次优的。人们对非线性ROM越来越感兴趣，它使用最先进的表示学习技术以较少的自由度准确地捕捉这种现象。我们提出了光滑神经场ROM（SNF-ROM），这是一种将无网格简化表示与Galerkin投影相结合的非线性简化建模框架。SNF-ROM体系结构将学习到的ROM轨迹约束为平滑变化的路径，这在根据支配PDE遍历简化流形时的动力学评估中是有益的。此外，我们设计了鲁棒正则化方案，以确保学习的神经场是光滑和可微的。这使我们能够使用自动微分来非侵入地计算简化系统的基于物理的动力学，并使用经典时间积分器来演化简化系统。SNF-ROM可以实现快速的离线训练，并提高在线动力学评估的准确性和稳定性。我们证明了SNF-ROM在一系列平流主导的线性和非线性PDE问题上的有效性，在这些问题上，我们始终优于最先进的ROM。 et.al.|[2405.14890](http://arxiv.org/abs/2405.14890)|null|
|**2024-05-23**|**NeuroGauss4D-PCI: 4D Neural Fields and Gaussian Deformation Fields for Point Cloud Interpolation**|点云插值面临着点稀疏性、复杂的时空动力学以及从稀疏的时间信息中导出完整的三维点云的困难等挑战。本文介绍了NeuroGauss4D PCI，它擅长在各种动态场景中建模复杂的非刚性变形。该方法从迭代高斯云软聚类模块开始，提供结构化的时间点云表示。所提出的时间径向基函数高斯残差利用高斯参数随时间插值，实现平滑的参数转换并捕获高斯分布的时间残差。此外，4D高斯变形场跟踪这些参数的演变，创建连续的时空变形场。4D神经场将低维时空坐标（ $x，y，z，t$ ）转换为高维潜在空间。最后，我们自适应有效地融合了来自神经场的潜在特征和来自高斯变形场的几何特征。NeuroGauss4D PCI在点云帧插值方面优于现有方法，在对象级（DHB）和大规模自动驾驶数据集（NL Drive）上都提供了领先的性能，并可扩展到自动标记和点云加密任务。源代码发布于https://github.com/jiangchaokang/NeuroGauss4D-PCI. et.al.|[2405.14241](http://arxiv.org/abs/2405.14241)|null|
|**2024-05-23**|**Multi-view Remote Sensing Image Segmentation With SAM priors**|遥感中的多视图分割（RS）寻求从场景内的不同视角对图像进行分割。最近的方法利用了从隐式神经场（INF）中提取的3D信息，增强了多个视图的结果一致性，同时使用有限的标签（甚至在3-5个标签内）来简化劳动力。尽管如此，由于不充分的全场景监督和INF中不充分的语义特征，在有限视图标签的约束下实现卓越性能仍然具有挑战性。我们建议将视觉基础模型Segment Anything（SAM）的先验注入INF，以在有限的训练数据下获得更好的结果。具体而言，我们对比测试视图和训练视图之间的SAM特征，以导出每个测试视图的伪标签，增强场景范围的标签信息。随后，我们通过转换器将SAM特征引入场景的INF中，补充语义信息。实验结果表明，我们的方法优于主流方法，证实了SAM作为INF的补充对该任务的有效性。 et.al.|[2405.14171](http://arxiv.org/abs/2405.14171)|null|
|**2024-05-22**|**Bridging Operator Learning and Conditioned Neural Fields: A Unifying Perspective**|算子学习是机器学习的一个新兴领域，旨在学习无穷维函数空间之间的映射。在这里，我们从计算机视觉中揭示了算子学习架构和条件神经场之间的联系，为研究流行的算子学习模型之间的差异提供了一个统一的视角。我们发现，许多常用的算子学习模型可以被视为神经场，其条件机制仅限于点和/或全局信息。受此启发，我们提出了连续视觉转换器（CViT），这是一种新的神经算子架构，它使用视觉转换器编码器，并使用交叉注意力来调制由可训练的基于网格的查询坐标位置编码构建的基场。尽管它很简单，但CViT在气候建模和流体动力学的挑战性基准中取得了最先进的结果。我们的贡献可以被视为在物理科学中适应先进的计算机视觉架构以构建更灵活、更准确的机器学习模型的第一步。 et.al.|[2405.13998](http://arxiv.org/abs/2405.13998)|**[link](https://github.com/predictiveintelligencelab/cvit)**|
|**2024-05-21**|**Unsupervised Searches for Cosmological Parity Violation: Improving Detection Power with the Neural Field Scattering Transform**|最近使用四点相关性的研究表明，星系分布中存在宇称破坏，尽管这些探测的重要性对用于模拟星系分布噪声特性的模拟的选择很敏感。在最近的一篇论文中，我们介绍了一种无监督学习方法，该方法提供了一种替代方法，通过直接从观测数据中学习奇偶性违反，避免了对模拟目录的依赖。然而，我们以前的无监督方法所使用的卷积神经网络（CNN）模型很难扩展到数据有限的更现实的场景。我们提出了一种新的方法，即神经场散射变换（NFST），它通过添加可训练滤波器来增强小波散射变换（WST）技术，该滤波器被参数化为神经场。我们首先调整NFST模型，以在简化的数据集中检测奇偶校验违规，然后在不同的训练集大小下，将其性能与WST和CNN基准进行比较。我们发现，NFST可以检测奇偶校验违规，数据比CNN少4倍，比WST少32倍。此外，在数据有限的情况下，NFST可以检测到高达 $6\sigma$ 置信度的奇偶校验违规，其中WST和CNN无法进行任何检测。我们发现，与基准模型相比，NFST增加的灵活性，特别是学习不对称滤波器的能力，以及NFST架构中内置的特定对称性，有助于提高其性能。我们进一步证明了NFST是易于解释的，这对于物理应用（如奇偶校验违反的检测）是有价值的。 et.al.|[2405.13083](http://arxiv.org/abs/2405.13083)|null|
|**2024-05-21**|**Implicit-ARAP: Efficient Handle-Guided Deformation of High-Resolution Meshes and Neural Fields via Local Patch Meshing**|在这项工作中，我们提出了神经符号距离场的局部补丁网格表示。该技术允许通过仅使用SDF信息及其梯度将平面面片网格投影和变形到标高集曲面上来离散输入SDF的标高集的局部区域。我们的分析表明，这种方法比标准的行进立方体算法更准确地逼近隐式曲面。然后，我们将这种表示应用于手柄引导变形的设置：我们引入了两个不同的管道，它们利用3D神经场来计算在给定约束集下高分辨率网格和神经场的“尽可能刚性”变形。我们对我们的方法和神经场和网格变形的各种基线进行了全面评估，结果表明，这两条管道在结果质量和稳健性方面都取得了令人印象深刻的效率和显著的改进。通过我们的新型流水线，我们引入了一种可扩展的方法来解决高分辨率网格上公认的几何处理问题，并为通过局部面片网格将其他几何任务扩展到隐式曲面领域铺平了道路。 et.al.|[2405.12895](http://arxiv.org/abs/2405.12895)|null|
|**2024-05-16**|**Single-shot volumetric fluorescence imaging with neural fields**|与需要在多个轴向平面上扫描的传统成像方法相比，单次体积荧光（SVF）成像提供了显著的优势，因为它可以在大视场上以高时间分辨率捕获生物过程。现有的SVF成像方法通常需要大的、复杂的点扩展函数（PSF）来满足压缩传感的多路复用要求，这限制了信噪比、分辨率和/或视场。在本文中，我们介绍了QuadraPol-PSF与神经场相结合，这是一种新的SVF成像方法。该方法在后焦平面利用成本效益高的定制偏振器和偏振相机来检测荧光，在紧凑的PSF内有效地编码3D场景，而没有深度模糊。此外，我们提出了一种基于神经场技术的重建算法，该算法解决了用于校正成像系统像差的相位检索方法的不精确性。该算法将实验PSF的准确性与计算生成的检索PSF的长景深相结合。QuadraPol PSF与神经场相结合，可将传统荧光显微镜的采集时间显著缩短约20倍，并可一次性捕获100 mm $^3$ 立方体积。我们通过对沙子表面细菌菌落的全聚焦成像和植物根系形态的可视化，验证了我们的硬件和算法的有效性。我们的方法为推进生物学研究和生态学研究提供了强有力的工具。 et.al.|[2405.10463](http://arxiv.org/abs/2405.10463)|null|
|**2024-05-08**|**${M^2D}$NeRF: Multi-Modal Decomposition NeRF with 3D Feature Fields**|神经场（NeRF）已经成为表示连续3D场景的一种很有前途的方法。然而，NeRF中缺乏语义编码对场景分解提出了重大挑战。为了应对这一挑战，我们提出了一个单一的模型，即多模式分解NeRF（${M^2D}$ NeRF），它能够进行基于文本和基于视觉补丁的编辑。具体来说，我们使用多模态特征提取将来自预训练的视觉和语言模型的教师特征集成到3D语义特征体积中，从而促进一致的3D编辑。为了增强三维特征体积中视觉特征和语言特征之间的一致性，我们引入了多模态相似性约束。我们还引入了一种基于补丁的联合对比损失，这有助于鼓励对象区域在3D特征空间中合并，从而产生更精确的边界。与先前的基于NeRF的方法相比，在各种真实世界场景上的实验显示出在3D场景分解任务中的优越性能。 et.al.|[2405.05010](http://arxiv.org/abs/2405.05010)|null|

<p align=right>(<a href=#updated-on-20240529>back to top</a>)</p>

[contributors-shield]: https://img.shields.io/github/contributors/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[contributors-url]: https://github.com/Vincentqyw/cv-arxiv-daily/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[forks-url]: https://github.com/Vincentqyw/cv-arxiv-daily/network/members
[stars-shield]: https://img.shields.io/github/stars/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[stars-url]: https://github.com/Vincentqyw/cv-arxiv-daily/stargazers
[issues-shield]: https://img.shields.io/github/issues/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[issues-url]: https://github.com/Vincentqyw/cv-arxiv-daily/issues

