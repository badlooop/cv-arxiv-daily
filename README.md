[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]

## Updated on 2024.02.09
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
|**2024-02-08**|**NCRF: Neural Contact Radiance Fields for Free-Viewpoint Rendering of Hand-Object Interaction**|在三维计算机视觉中，建模手与物体的交互是一项具有根本挑战性的任务。尽管在该领域已经取得了显著的进展，但现有的方法仍然无法真实地合成手与物体的交互照片，因为手与物体之间的严重相互遮挡导致渲染质量下降，以及手与物体姿态估计不准确。为了应对这些挑战，我们提出了一种新的自由视点渲染框架，即神经接触辐射场（NCRF），以从稀疏的视频集重建手与物体的交互。特别地，所提出的NCRF框架由两个关键组件组成：（a）接触优化字段，该字段从3D查询点预测准确的接触字段，以实现手和物体之间的期望接触。（b） 手对象神经辐射场，用于学习静态规范空间中的隐含手对象表示，与专门设计的手对象运动场相一致，以产生观察到的规范对应关系。我们共同学习这些关键组件，它们在视觉和几何约束下相互帮助和规则化，产生高质量的手对象重建，实现照片逼真的新颖视图合成。在HO3D和DexYCB数据集上进行的大量实验表明，我们的方法在渲染质量和姿态估计精度方面都优于当前最先进的方法。 et.al.|[2402.05532](http://arxiv.org/abs/2402.05532)|null|
|**2024-02-07**|**SPAD : Spatially Aware Multiview Diffusers**|我们提出了SPAD，这是一种从文本提示或单个图像创建一致多视图图像的新方法。为了实现多视图生成，我们通过扩展具有跨视图交互的自注意层来重新调整预训练的2D扩散模型的用途，并在Ob厌恶的高质量子集上对其进行微调。我们发现，先前工作中提出的自我关注的天真扩展（例如MVDream）会导致视图之间的内容复制。因此，我们明确地限制了基于核极几何的跨视图注意力。为了进一步增强3D一致性，我们利用从相机射线导出的Plucker坐标，并将其作为位置编码注入。这使得SPAD能够对3D井中的空间接近度进行推理。与最近只能在固定方位角和仰角下生成视图的工作不同，SPAD提供了完整的相机控制，并在Ob厌恶和谷歌扫描对象数据集中对看不见的对象进行新的视图合成方面取得了最先进的结果。最后，我们证明了使用SPAD的文本到3D生成可以防止多面Janus问题。更多详细信息，请访问我们的网页：https://yashkant.github.io/spad et.al.|[2402.05235](http://arxiv.org/abs/2402.05235)|null|
|**2024-02-06**|**EscherNet: A Generative Model for Scalable View Synthesis**|我们介绍了EscherNet，一个用于视图合成的多视图条件扩散模型。EscherNet学习隐含的和生成的3D表示，再加上专门的相机位置编码，允许对任意数量的参考视图和目标视图之间的相机变换进行精确和连续的相对控制。EscherNet在视图合成方面提供了非凡的通用性、灵活性和可扩展性——尽管它使用固定数量的3个参考视图到3个目标视图进行训练，但它可以在单个消费级GPU上同时生成100多个一致的目标视图。因此，EscherNet不仅解决了零样本新视图合成问题，而且自然地将单图像和多图像3D重建相结合，将这些不同的任务组合成一个单一的、有凝聚力的框架。我们的大量实验表明，EscherNet在多个基准测试中实现了最先进的性能，即使与专门针对每个单独问题定制的方法相比也是如此。这种非凡的多功能性为设计用于3D视觉的可扩展神经结构开辟了新的方向。项目页面：\url{https://kxhit.github.io/EscherNet}. et.al.|[2402.03908](http://arxiv.org/abs/2402.03908)|null|
|**2024-02-06**|**Rig3DGS: Creating Controllable Portraits from Casual Monocular Videos**|从随意的智能手机视频中创建可控的3D人像是非常可取的，因为它们在AR/VR应用中具有巨大的价值。3D高斯散点（3DGS）的最新发展已经显示出在渲染质量和训练效率方面的改进。然而，要从单个视图捕捉中准确地建模和分解头部运动和面部表情，以实现高质量的渲染，仍然是一个挑战。在本文中，我们介绍了Rig3DGS来应对这一挑战。我们在规范空间中使用一组3D高斯表示整个场景，包括动态主体。使用一组控制信号，如头部姿势和表情，我们将它们转换到具有学习变形的3D空间，以生成所需的渲染。我们的关键创新是一种精心设计的变形方法，该方法以从3D可变形模型导出的可学习先验为指导。这种方法在训练中效率很高，在控制各种捕捉的面部表情、头部位置和视图合成方面也很有效。我们通过大量的定量和定性实验证明了我们所学变形的有效性。项目页面位于http://shahrukhathar.github.io/2024/02/05/Rig3DGS.html et.al.|[2402.03723](http://arxiv.org/abs/2402.03723)|null|
|**2024-02-05**|**Denoising Diffusion via Image-Based Rendering**|生成3D场景是一个具有挑战性的开放问题，需要合成在3D空间中完全一致的看似合理的内容。虽然最近的方法（如神经辐射场）擅长于视图合成和3D重建，但由于缺乏生成能力，它们无法在未观察到的区域合成看似合理的细节。相反，现有的生成方法通常无法重建野外的详细、大规模场景，因为它们使用有限容量的3D场景表示，需要对齐的相机姿势，或者依赖于额外的正则化子。在这项工作中，我们介绍了第一个能够快速、详细地重建和生成真实世界3D场景的扩散模型。为了实现这一目标，我们作出了三点贡献。首先，我们引入了一种新的神经场景表示，即IB平面，它可以有效而准确地表示大型3D场景，并根据需要动态分配更多的容量来捕捉每个图像中可见的细节。其次，我们提出了一种去噪扩散框架来学习这种新颖的3D场景表示的先验知识，仅使用2D图像，而不需要任何额外的监督信号，如掩模或深度。这支持在统一架构中进行3D重建和生成。第三，我们开发了一种原则性方法，通过放弃一些图像的表示，在将基于图像的渲染与扩散模型集成时避免琐碎的3D解决方案。我们在真实图像和合成图像的几个具有挑战性的数据集上评估了该模型，并展示了在生成、新视图合成和3D重建方面的卓越结果。 et.al.|[2402.03445](http://arxiv.org/abs/2402.03445)|null|
|**2024-02-07**|**4D Gaussian Splatting: Towards Efficient Novel View Synthesis for Dynamic Scenes**|我们考虑动态场景的新视图合成（NVS）问题。最近的神经方法已经为静态3D场景实现了异常的NVS结果，但对4D时变场景的扩展仍然是不平凡的。先前的工作通常通过学习规范空间加上隐式或显式变形场来编码动力学，这些变形场在突发运动或捕捉高保真渲染等具有挑战性的场景中很困难。在本文中，我们介绍了4D高斯散射（4DGS），这是一种用各向异性4D XYZT高斯表示动态场景的新方法，其灵感来自于3D高斯散射在静态场景中的成功。我们通过对4D高斯进行时间切片来对每个时间戳的动力学进行建模，4D高斯自然构成动态3D高斯，并可以无缝投影到图像中。作为一种明确的时空表示，4DGS展示了对复杂动力学和精细细节建模的强大能力，尤其是对于具有突然运动的场景。我们在高度优化的CUDA加速框架中进一步实现了我们的时间切片和飞溅技术，在RTX 3090 GPU上实现了高达277 FPS的实时推理渲染速度，在RTX4090 GPU上达到了583 FPS的实时推断渲染速度。对不同运动场景的严格评估显示了4DGS的卓越效率和有效性，它在数量和质量上都始终优于现有方法。 et.al.|[2402.03307](http://arxiv.org/abs/2402.03307)|null|
|**2024-02-05**|**ViewFusion: Learning Composable Diffusion Models for Novel View Synthesis**|深度学习为新视图合成的老问题提供了丰富的新方法，从基于神经辐射场（NeRF）的方法到端到端风格的架构。每种方法都有特定的优势，但在适用性方面也有特定的局限性。这项工作介绍了ViewFusion，这是一种最先进的端到端生成新视图合成方法，具有无与伦比的灵活性。ViewFusion包括同时将扩散去噪步骤应用于场景的任意数量的输入视图，然后将为每个视图获得的噪声梯度与（推断的）像素加权掩码相结合，确保对于目标场景的每个区域，只考虑信息量最大的输入视图。我们的方法通过以下方式解决了以前方法的几个局限性：（1）可在多个场景和对象类中进行训练和推广，（2）在训练和测试时自适应地获取可变数量的无姿态视图，（3）即使在严重不确定的条件下也能生成合理的视图（由于其生成性）——同时生成质量与最先进方法不相上下甚至更好的视图。局限性包括没有生成场景的3D嵌入，导致推理速度相对较慢，并且我们的方法仅在相对较小的数据集NMR上进行测试。代码可用。 et.al.|[2402.02906](http://arxiv.org/abs/2402.02906)|**[link](https://github.com/bronemos/view-fusion)**|
|**2024-02-06**|**GaMeS: Mesh-Based Adapting and Modification of Gaussian Splatting**|近年来，已经引入了一系列基于神经网络的图像渲染方法。例如，广泛研究的神经辐射场（NeRF）依赖于神经网络来表示3D场景，从而允许从少量2D图像中合成逼真的视图。然而，大多数NeRF模型都受到长训练和推理时间的限制。相比之下，高斯散射（GS）是一种新颖的、最先进的技术，用于通过高斯分布近似点对图像像素的贡献来渲染3D场景中的点，从而保证快速训练和快速实时渲染。GS的一个缺点是，由于需要对几十万个高斯分量进行调节，因此缺乏定义明确的方法来进行调节。为了解决这个问题，我们引入了高斯网格飞溅（GaMeS）模型，这是网格和高斯分布的混合，它将所有高斯飞溅物固定在物体表面（网格）上。我们的方法的独特贡献是仅根据高斯飞溅在网格上的位置来定义高斯飞溅，从而允许在动画过程中自动调整位置、比例和旋转。因此，我们在实时生成高质量视图的过程中获得了高质量的渲染图。此外，我们证明，在没有预定义网格的情况下，可以在学习过程中微调初始网格。 et.al.|[2402.01459](http://arxiv.org/abs/2402.01459)|**[link](https://github.com/waczjoan/gaussian-mesh-splatting)**|
|**2024-02-01**|**360-GS: Layout-guided Panoramic Gaussian Splatting For Indoor Roaming**|近年来，三维高斯散射（3D-GS）以其实时性和照片真实性的渲染引起了人们的极大关注。这项技术通常将透视图像作为输入，并通过将一组3D椭圆高斯分布到图像平面上来优化它们，从而产生2D高斯。然而，将3D-GS应用于全景输入在使用2D高斯有效地将投影建模到 ${360^\circ}$图像的球面上方面存在挑战。在实际应用中，输入全景图往往是稀疏的，导致3D高斯图的初始化不可靠，并导致3D-GS质量下降。此外，由于无纹理平面（例如，墙和地板）的几何约束不足，3D-GS难以用椭圆高斯对这些平坦区域进行建模，导致在新视图中出现显著的浮动。为了解决这些问题，我们提出了360-GS，这是一种针对有限的全景输入集的新的$360^{\circ}$ 高斯飞溅。360-GS不是将3D高斯直接泼洒到球面上，而是将其投影到单位球体的切平面上，然后将其映射到球面投影。这种自适应使得能够使用高斯表示投影。我们通过利用全景图中的布局先验来指导360-GS的优化，这些先验易于获得，并包含关于室内场景的强大结构信息。我们的实验结果表明，360-GS允许全景渲染，并在新的视图合成中以更少的伪影优于最先进的方法，从而在室内场景中提供身临其境的漫游。 et.al.|[2402.00763](http://arxiv.org/abs/2402.00763)|null|
|**2024-02-01**|**StopThePop: Sorted Gaussian Splatting for View-Consistent Real-time Rendering**|高斯散射已经成为从不同领域的图像构建3D表示的一个突出模型。然而，3D高斯飞溅渲染管道的效率依赖于几个简化。值得注意的是，使用单个视图空间深度将高斯飞溅减少到2D会在视图旋转过程中引入爆裂和混合伪影。解决这个问题需要精确的每像素深度计算，但与全局排序操作相比，完整的每像素排序成本过高。在本文中，我们提出了一种新的分层光栅化方法，该方法以最小的处理开销系统地处理和剔除飞溅。我们的软件光栅化器有效地消除了弹出的伪影和视图不一致，通过定量和定性测量都证明了这一点。同时，我们的方法通过弹出来减少欺骗视图相关效果的可能性，确保了更真实的表示。尽管消除了作弊，但我们的方法在测试图像中获得了可比的定量结果，同时提高了运动中新视图合成的一致性。由于其设计，我们的分层方法平均只比原始的高斯飞溅慢4%。值得注意的是，强制执行一致性可以将Gaussian的数量减少大约一半，同时具有几乎相同的质量和视图一致性。因此，渲染性能几乎翻了一番，使我们的方法比原始的高斯Splatting快1.6倍，同时减少了50%的内存需求。 et.al.|[2402.00525](http://arxiv.org/abs/2402.00525)|null|

<p align=right>(<a href=#updated-on-20240209>back to top</a>)</p>

## 3D Reconstruction

|Publish Date|Title|Abstract|PDF|Code|
|---|---|---|---|---|
|**2024-02-07**|**Carousel phase retrieval algorithm for 3D coherent X-ray diffraction imaging**|相干X射线衍射成像（CXDI）是一种独特的技术，通过基于测量的散射强度图执行计算相位重建程序，可以以纳米级分辨率重建2D和3D物体。重建过程可能具有高计算复杂度，并且通常不能在实验期间实时执行。我们提出了一种转盘相位检索算法（CPRA），该算法基于傅立叶切片定理将3D重建问题表示为对应于不同收集角度的投影图像的一组2D重建。为了保持2D重建之间的一致性，我们引入了一种迭代过程，其中每个2D重建都以周期性（旋转）的方式基于相邻的2D重建。2D重建的使用大大减少了计算时间和内存消耗。我们展示了在CPU和GPU计算架构上针对各种空间大小的复杂生物细胞的测试问题的CPRA实现。与传统的CXDI重建算法相比，CPRA在GPU上表现出300倍的速度，在CPU上表现出120倍的速度。CPRA还可以实现更高的重建质量。所实现的速度允许实时对计算上较大的对象进行高分辨率重建。 et.al.|[2402.05283](http://arxiv.org/abs/2402.05283)|**[link](https://github.com/UCSD-CEM/Carousel-Phase-Retrieval-Algorithm)**|
|**2024-02-07**|**Scalable Multi-view Clustering via Explicit Kernel Features Maps**|人们越来越意识到多视图学习是数据科学和机器学习的重要组成部分，这是多视图在现实世界应用中越来越普遍的结果，尤其是在网络环境中。在本文中，我们介绍了一种新的多视图子空间聚类的可扩展性框架。提出了一种有效的优化策略，利用核特征图来减少计算负担，同时保持良好的聚类性能。该算法的可扩展性意味着它可以在几分钟内使用标准机器应用于大规模数据集，包括具有数百万数据点的数据集。我们在不同规模的真实世界基准网络上进行了广泛的实验，以评估我们的算法相对于最先进的多视图子空间聚类方法和属性网络多视图方法的性能。 et.al.|[2402.04794](http://arxiv.org/abs/2402.04794)|null|
|**2024-02-06**|**EscherNet: A Generative Model for Scalable View Synthesis**|我们介绍了EscherNet，一个用于视图合成的多视图条件扩散模型。EscherNet学习隐含的和生成的3D表示，再加上专门的相机位置编码，允许对任意数量的参考视图和目标视图之间的相机变换进行精确和连续的相对控制。EscherNet在视图合成方面提供了非凡的通用性、灵活性和可扩展性——尽管它使用固定数量的3个参考视图到3个目标视图进行训练，但它可以在单个消费级GPU上同时生成100多个一致的目标视图。因此，EscherNet不仅解决了零样本新视图合成问题，而且自然地将单图像和多图像3D重建相结合，将这些不同的任务组合成一个单一的、有凝聚力的框架。我们的大量实验表明，EscherNet在多个基准测试中实现了最先进的性能，即使与专门针对每个单独问题定制的方法相比也是如此。这种非凡的多功能性为设计用于3D视觉的可扩展神经结构开辟了新的方向。项目页面：\url{https://kxhit.github.io/EscherNet}. et.al.|[2402.03908](http://arxiv.org/abs/2402.03908)|null|
|**2024-02-06**|**Efficient Generation of Hidden Outliers for Improved Outlier Detection**|异常值生成是一种常用的技术，用于解决重要的异常值检测任务。生成具有现实行为的异常值具有挑战性。现有的流行方法往往忽略高维空间中异常值的“多视图”特性。对这一财产进行核算的唯一现有方法在效率和有效性方面不足。我们提出了BISECT，这是一种新的异常值生成方法，可以创建模拟上述属性的真实异常值。为此，BISECT采用了本文中介绍的一个新颖命题，说明如何有效地生成所述现实异常值。我们的方法比当前重建“多个视图”的方法有更好的保证和复杂性。我们使用BISECT生成的合成异常值来有效地增强不同数据集中的异常值检测，用于多种用例。例如，与基线相比，BISECT的过采样将误差减少了3倍。 et.al.|[2402.03846](http://arxiv.org/abs/2402.03846)|**[link](https://github.com/jcribeiro98/bisect)**|
|**2024-02-06**|**MoD-SLAM: Monocular Dense Mapping for Unbounded 3D Scene Reconstruction**|神经隐式表示最近已经在许多领域得到了证明，包括同时定位和映射（SLAM）。目前的神经SLAM在重建有界场景时可以获得理想的结果，但这依赖于RGB-D图像的输入。仅基于RGB图像的基于神经的SLAM无法准确地重建场景的尺度，而且由于跟踪过程中积累的误差，它还存在尺度漂移。为了克服这些限制，我们提出了MoD SLAM，这是一种单目密集映射方法，允许在无界场景中实时进行全局姿态优化和3D重建。通过单目深度估计优化场景重建，并使用闭环检测更新相机姿态，可以在大型场景上进行详细而精确的重建。与以前的工作相比，我们的方法更加健壮、可扩展和通用。我们的实验表明，与现有的神经SLAM方法相比，MoD-SLAM具有更出色的映射性能，尤其是在大型无边界场景中。 et.al.|[2402.03762](http://arxiv.org/abs/2402.03762)|null|
|**2024-02-05**|**Denoising Diffusion via Image-Based Rendering**|生成3D场景是一个具有挑战性的开放问题，需要合成在3D空间中完全一致的看似合理的内容。虽然最近的方法（如神经辐射场）擅长于视图合成和3D重建，但由于缺乏生成能力，它们无法在未观察到的区域合成看似合理的细节。相反，现有的生成方法通常无法重建野外的详细、大规模场景，因为它们使用有限容量的3D场景表示，需要对齐的相机姿势，或者依赖于额外的正则化子。在这项工作中，我们介绍了第一个能够快速、详细地重建和生成真实世界3D场景的扩散模型。为了实现这一目标，我们作出了三点贡献。首先，我们引入了一种新的神经场景表示，即IB平面，它可以有效而准确地表示大型3D场景，并根据需要动态分配更多的容量来捕捉每个图像中可见的细节。其次，我们提出了一种去噪扩散框架来学习这种新颖的3D场景表示的先验知识，仅使用2D图像，而不需要任何额外的监督信号，如掩模或深度。这支持在统一架构中进行3D重建和生成。第三，我们开发了一种原则性方法，通过放弃一些图像的表示，在将基于图像的渲染与扩散模型集成时避免琐碎的3D解决方案。我们在真实图像和合成图像的几个具有挑战性的数据集上评估了该模型，并展示了在生成、新视图合成和3D重建方面的卓越结果。 et.al.|[2402.03445](http://arxiv.org/abs/2402.03445)|null|
|**2024-02-02**|**Di-NeRF: Distributed NeRF for Collaborative Learning with Unknown Relative Poses**|未知环境的协作映射可以比单个机器人更快、更稳健地完成。然而，协作方法需要一个可扩展的分布式范式来处理通信问题。这项工作提出了一种全分布式算法，使一组机器人能够共同优化神经辐射场（NeRF）的参数。该算法涉及每个机器人训练的NeRF参数在网状网络上的通信，在网状网络中，每个机器人训练其NeRF，并且只能访问自己的视觉数据。此外，所有机器人的相对姿态都与模型参数一起进行了联合优化，从而能够使用未知的相对相机姿态进行映射。我们证明了多机器人系统可以受益于从多个NeRF优化的可微分和鲁棒的3D重建。在真实世界和合成数据上的实验证明了所提出的算法的有效性。实验视频和补充材料见项目网站(https://sites.google.com/view/di-nerf/home). et.al.|[2402.01485](http://arxiv.org/abs/2402.01485)|null|
|**2024-02-02**|**SiMA-Hand: Boosting 3D Hand-Mesh Reconstruction by Single-to-Multi-View Adaptation**|从RGB图像中估计3D手部网格是一个长期存在的问题，其中遮挡是最具挑战性的问题之一。当遮挡在图像空间中占主导地位时，针对该任务的现有尝试往往失败。在本文中，我们提出了SiMA Hand，旨在通过单视图到多视图自适应来提高网格重建性能。首先，我们设计了一个多视图手动重建器，通过在图像、关节和顶点级别全面采用特征融合来融合多个视图之间的信息。然后，我们介绍了一种配备SiMA的单视图手动重建器。尽管在推理时仅将一个视图作为输入，但通过在训练时从额外的视图中学习非遮挡知识，可以丰富单个视图重构器中的形状和方向特征，提高遮挡区域的重构精度。我们在Dex-YCB和HanCo基准上对具有挑战性的物体和自身造成的遮挡情况进行了实验，表明SiMA Hand始终实现了优于现有技术的性能。代码将于发布https://github.com/JoyboyWang/SiMA-HandPytorch。 et.al.|[2402.01389](http://arxiv.org/abs/2402.01389)|**[link](https://github.com/JoyboyWang/SiMA-Hand_Pytorch)**|
|**2024-02-02**|**DeepAAT: Deep Automated Aerial Triangulation for Fast UAV-based Mapping**|自动空中三角测量（AAT）旨在恢复图像姿态和重建稀疏点，在对地观测中发挥着关键作用。AAT在摄影测量领域拥有数十年的丰富研究遗产，已发展成为一个广泛应用于大规模无人机测绘的基础过程。尽管取得了进步，但经典的AAT方法仍然面临着效率低和稳健性有限等挑战。本文介绍了DeepAAT，一个专门为无人机图像AAT设计的深度学习网络。DeepAAT考虑了图像的空间和光谱特征，增强了其解决错误匹配对和准确预测图像姿态的能力。DeepAAT标志着AAT效率的重大飞跃，确保了全面的场景覆盖和精度。其处理速度超过增量AAT方法数百倍，超过全局AAT方法数十倍，同时保持了相当水平的重建精度。此外，DeepAAT的场景聚类和合并策略有助于大规模无人机图像的快速定位和姿态确定，即使在计算资源有限的情况下也是如此。实验结果表明，DeepAAT比传统的AAT方法有了实质性的改进，突出了其在基于无人机的三维重建任务的效率和准确性方面的潜力。为了造福摄影测量学会，DeepAAT的代码将发布在：https://github.com/WHU-USI3DV/DeepAAT. et.al.|[2402.01134](http://arxiv.org/abs/2402.01134)|**[link](https://github.com/whu-usi3dv/deepaat)**|
|**2024-02-02**|**Learning Which Side to Scan: Multi-View Informed Active Perception with Side Scan Sonar for Autonomous Underwater Vehicles**|自动水下航行器通常执行捕获目标的多个视图的勘测，以便为人类操作员或自动目标识别算法提供更多信息。在这项工作中，我们解决了选择信息量最大的视图的问题，这些视图可以最大限度地减少调查时间，同时最大限度地提高分类器的准确性。我们介绍了一种新的主动感知框架，用于使用侧扫声纳图像进行多视图自适应测量和重新获取。我们的框架通过使用自适应调查任务的图形公式来应对这一挑战。然后，我们使用图神经网络（GNN）对获取的声纳视图进行分类，并根据收集的数据选择下一个最佳视图。我们使用高保真侧扫声纳模拟器中的模拟调查来评估我们的方法。我们的结果表明，我们的方法能够在分类精度和调查效率方面超越最先进的方法。该框架是一种很有前途的方法，可用于更高效的自主任务，包括侧扫声纳，如水下勘探、海洋考古和环境监测。 et.al.|[2402.01106](http://arxiv.org/abs/2402.01106)|null|

<p align=right>(<a href=#updated-on-20240209>back to top</a>)</p>

## Diffusion

|Publish Date|Title|Abstract|PDF|Code|
|---|---|---|---|---|
|**2024-02-08**|**InstaGen: Enhancing Object Detection by Training on Synthetic Dataset**|在本文中，我们引入了一种新的范式，通过在扩散模型生成的合成数据集上进行训练来增强对象检测器的能力，例如扩展类别或提高检测性能。具体而言，我们将实例级接地头集成到预先训练的生成扩散模型中，以增强其在生成图像中定位任意实例的能力。使用现成对象检测器的监督和检测器未覆盖的（新颖的）类别的新颖自训练方案，训练接地头以使类别名称的文本嵌入与扩散模型的区域视觉特征对齐。这种被称为InstaGen的扩散模型的增强版本可以作为对象检测的数据合成器。我们进行了彻底的实验，表明在InstaGen的合成数据集上训练时，对象检测器可以得到增强，在开放词汇表（+4.5 AP）和数据稀疏（+1.2到5.2 AP）场景中表现出优于现有最先进方法的性能。 et.al.|[2402.05937](http://arxiv.org/abs/2402.05937)|null|
|**2024-02-08**|**Time Series Diffusion in the Frequency Domain**|傅立叶分析一直是信号处理发展的工具。这让我们怀疑这个框架是否同样有利于生成建模。在本文中，我们通过时间序列扩散模型的范围来探讨这个问题。更具体地说，我们分析了在频域中表示时间序列是否是基于分数的扩散模型的有用归纳偏差。从时域中扩散的标准SDE公式开始，我们证明了在频域中发生的双重扩散过程有一个重要的细微差别：布朗运动被我们所说的镜像布朗运动所取代，其特征是其分量之间的镜像对称性。基于这一见解，我们展示了如何调整去噪分数匹配方法，以在频域中实现扩散模型。这导致了频率扩散模型，我们将其与标准时间扩散模型进行比较。我们对涵盖医疗保健和金融等各个领域的真实世界数据集的实证评估表明，频率扩散模型比时间扩散模型更好地捕捉训练分布。我们通过表明这些数据集的时间序列往往在频域中比在时域中更局部化来解释这一观察结果，这使得它们在前一种情况下更容易建模。我们所有的观察结果都指向傅立叶分析和扩散模型之间有影响力的协同作用。 et.al.|[2402.05933](http://arxiv.org/abs/2402.05933)|null|
|**2024-02-08**|**Dirichlet Flow Matching with Applications to DNA Sequence Design**|离散扩散或流动模型可以比自回归模型更快、更可控地生成序列。我们展示了na\“单纯形上的ive线性流匹配不足以实现这一目标，因为它存在训练目标的不连续性和进一步的病态。为了克服这一点，我们在单纯形上开发了基于狄利克雷分布混合物作为概率路径的狄利克雷流匹配。在这个框架中，我们导出了混合物分数和流的矢量场之间的联系允许分类器和无分类器引导。此外，我们提供了提取的狄利克雷流匹配，它能够以最小的性能命中率生成一步序列，与自回归模型相比，导致 $O（L）$ 加速。在复杂的DNA序列生成任务中，与所有基线相比，我们在分布度量和实现所生成序列的预期设计目标方面表现出了卓越的性能。最后，我们证明了我们的无分类器引导方法改进了无条件生成，并且对于生成满足设计目标的DNA是有效的。代码位于https://github.com/HannesStark/dirichlet-flow-matching. et.al.|[2402.05841](http://arxiv.org/abs/2402.05841)|**[link](https://github.com/hannesstark/dirichlet-flow-matching)**|
|**2024-02-08**|**AvatarMMC: 3D Head Avatar Generation and Editing with Multi-Modal Conditioning**|我们介绍了一种基于3D生成对抗性网络（GAN）和潜在扩散模型（LDM）的具有多模式条件的3D头部化身生成和编辑方法。3D GANs可以在给定单一条件或不给定条件的情况下生成高质量的头部化身。然而，生成符合不同模式的多种条件的样本是具有挑战性的。另一方面，LDM擅长学习复杂的条件分布。为此，我们建议利用LDM的调节能力，实现对预训练的3D GAN的潜在空间的多模态控制。我们的方法可以在给定混合控制信号（如RGB输入、分割掩码和全局属性）的情况下生成和编辑3D头部化身。这提供了对全局和本地合成化身的生成和编辑的更好控制。实验表明，我们提出的方法在生成和编辑任务的质量和数量上都优于单独基于GAN的方法。据我们所知，我们的方法是第一个将多模态条件反射引入3D化身生成和编辑的方法\\href｛avatarmc-sig24.github.io｝｛项目页面｝ et.al.|[2402.05803](http://arxiv.org/abs/2402.05803)|null|
|**2024-02-08**|**Determining the significance and relative importance of parameters of a simulated quenching algorithm using statistical tools**|在设计搜索方法时，了解哪些参数对算法的行为和性能影响最大是非常重要的。为此，通常通过理论分析或密集实验来校准算法参数。在对每个参数的影响进行详细的统计分析时，设计者应主要关注具有统计意义的参数。本文使用ANOVA（方差分析）方法对基于模拟退火的方法及其所需的不同参数进行了详尽的分析。根据这一想法，使用ANOVA和事后Tukey HSD检验，对四个众所周知的函数优化问题和用于估计对数正态扩散过程中涉及的参数的似然函数，获得了与所获得的结果有关的参数的显著性和相对重要性，以及每种结果的合适值。通过这项统计研究，我们使用参数假设检验验证了参考文献中可用参数值的充分性。 et.al.|[2402.05791](http://arxiv.org/abs/2402.05791)|null|
|**2024-02-08**|**Hydrogen abstraction from metal surfaces: When electron-hole pair excitations strongly affect hot-atom recombination**|利用分子动力学模拟，我们预测非绝热电子激发的加入会影响通过氢散射从W（110）表面预吸附氢提取的动力学，在低覆盖率和低入射能下，受到电子-空穴对激发介导的能量耗散的显著影响。这个问题很重要，因为这种提取机制被认为在很大程度上有助于金属表面形成分子氢。 et.al.|[2402.05743](http://arxiv.org/abs/2402.05743)|null|
|**2024-02-08**|**First operation of a multi-channel Q-Pix prototype: measuring transverse electron diffusion in a gas time projection chamber**|我们报道了在实验室规模的时间投影室（TPC）中，利用一种称为Q-Pix的新型像素化信号捕获和数字化技术，对P-10气体（90%Ar，10%CH4）中电子的横向扩散进行的测量。Q-Pix方法结合了一个精密开关积分跨阻放大器，其输出与阈值电压进行比较。达到阈值后，比较器发送“重置”信号，启动积分电容器的放电。连续重置之间的时间差与该时间间隔内像素处的平均电流成反比，重置次数与收集的总电荷成正比。我们开发了一个由商用现成组件制成的16通道Q-Pix原型，并将其耦合到16个同心环形阳极电极，以测量电子群在漂移通过TPC的均匀场后到达阳极的空间范围。该粒子群是在金光电阴极上使用脉冲紫外线产生的。在操作压力范围（200-1500托）内，测得的横向扩散与PyBoltz中的模拟结果一致。这些结果表明，Q-Pix读出可以成功地重建TPC中的电离拓扑。 et.al.|[2402.05734](http://arxiv.org/abs/2402.05734)|null|
|**2024-02-08**|**DiffSpeaker: Speech-Driven 3D Facial Animation with Diffusion Transformer**|语音驱动的3D面部动画对于许多多媒体应用来说是重要的。最近的工作已经显示出使用扩散模型或Transformer架构来完成这项任务的前景。然而，它们仅仅是聚合并不能提高性能。我们怀疑这是由于配对音频-4D数据的短缺，这对于Transformer在Diffusion框架内有效地充当去噪器至关重要。为了解决这个问题，我们提出了DiffSpeaker，这是一种基于Transformer的网络，配备了新颖的有偏条件注意模块。这些模块取代了标准变形金刚中传统的自我/交叉注意力，结合了精心设计的偏见，引导注意力机制专注于相关的特定任务和扩散相关的条件。我们还探讨了在扩散范式中准确的嘴唇同步和非语言面部表情之间的权衡。实验表明，我们的模型不仅在现有的基准上实现了最先进的性能，而且由于其能够并行生成面部运动，因此推理速度也很快。 et.al.|[2402.05712](http://arxiv.org/abs/2402.05712)|**[link](https://github.com/theericma/diffspeaker)**|
|**2024-02-08**|**Discovery and characterisation of a new Galactic Planetary Nebula**|行星状星云是中低质量恒星演化的最后阶段之一。它们有各种各样的形状。由于表面亮度较低，较老和较暗的通常更难识别。本文报道了一个新的微弱星系行星状星云（PN）的偶然发现，在一场识别矮星系的运动中，矮星系是螺旋星系NGC 2403的伙伴。我们的目的是确认在骆驼座发现的一个漫射物体的PN性质。我们用直径从20厘米到6米的业余和专业望远镜获得了该星云及其中心恒星的窄带滤波图像和光谱。我们探测到一个密集的三角形星云，被一个椭圆形区域包围，名为凸轮星云。它们是一个更大、更暗的圆形星云结构TBG-1的一部分，在其中心，我们已经确定了可能的中心恒星，一颗温度约为22000K的白矮星。对光谱的分析使测量星云的物理特征，特别是电子密度和温度成为可能。对图像、星云和中心恒星光谱的分析证实了TBG-1的PN性质，它位于大约1kpc的距离处。这项工作重申了天文学家和业余天文学家在探测和研究新天体方面进行富有成果的合作的潜力。 et.al.|[2402.05658](http://arxiv.org/abs/2402.05658)|null|
|**2024-02-08**|**Scalable Diffusion Models with State Space Backbone**|本文对一类基于状态空间结构的扩散模型进行了新的探索。我们努力训练图像数据的扩散模型，其中传统的U-Net主干被状态空间主干取代，在原始补丁或潜在空间上发挥作用。鉴于其在适应长程依赖性方面的显著功效，扩散状态空间模型（DiS）通过将包括时间、条件和噪声图像块在内的所有输入视为标记来区分。我们对DiS的评估包括无条件和类条件的图像生成场景，表明DiS表现出与相应大小的基于CNN或基于Transformer的U-Net架构相当（如果不是更好的话）的性能。此外，我们还分析了DiS的可扩展性，通过Gflops中量化的前向通过复杂性来衡量。通过增加深度/宽度或增加输入标记实现的具有更高Gflop的DiS模型始终显示出更低的FID。除了表现出值得称赞的可扩展性特征外，潜在空间中的DiS-H/2模型在256 $\times$256和512$\times$ 512的分辨率下实现了类似于类条件ImageNet基准上的先前扩散模型的性能水平，同时显著减少了计算负担。代码和型号位于：https://github.com/feizc/DiS. et.al.|[2402.05608](http://arxiv.org/abs/2402.05608)|**[link](https://github.com/feizc/dis)**|

<p align=right>(<a href=#updated-on-20240209>back to top</a>)</p>

## NeRF

|Publish Date|Title|Abstract|PDF|Code|
|---|---|---|---|---|
|**2024-02-06**|**Improved Generalization of Weight Space Networks via Augmentations**|在深度权重空间（DWS）中学习，神经网络处理其他神经网络的权重，是一个新兴的研究方向，应用于2D和3D神经领域（INRs、NeRFs），以及对其他类型的神经网络进行推断。不幸的是，权重空间模型往往存在严重的过拟合问题。我们实证分析了这种过拟合的原因，发现一个关键原因是DWS数据集缺乏多样性。虽然给定的对象可以用许多不同的权重配置来表示，但典型的INR训练集无法捕捉表示同一对象的INR之间的可变性。为了解决这一问题，我们探索了在权重空间中增加数据的策略，并提出了一种适用于权重空间的MixUp方法。我们在两个设置中展示了这些方法的有效性。在分类方面，它们可以提高性能，类似于拥有10倍以上的数据。在自我监督的对比学习中，它们在下游分类中产生了5-10%的显著收益。 et.al.|[2402.04081](http://arxiv.org/abs/2402.04081)|null|
|**2024-01-31**|**BlockFusion: Expandable 3D Scene Generation using Latent Tri-plane Extrapolation**|我们介绍了BlockFusion，这是一种基于扩散的模型，它将3D场景生成为单元块，并无缝地合并新的块来扩展场景。BlockFusion使用从完整的3D场景网格中随机裁剪的3D块的数据集进行训练。通过逐块拟合，所有训练块都被转换为混合神经场：具有包含几何特征的三平面，然后是用于解码有符号距离值的多层感知器（MLP）。采用变分自动编码器将三平面压缩到潜在的三平面空间中，在该空间上进行去噪扩散处理。应用于潜在表示的扩散允许高质量和多样化的3D场景生成。要在生成过程中扩展场景，只需附加空块以与当前场景重叠，并外推现有的潜在三平面以填充新块。外推是通过在去噪迭代过程中使用来自重叠三平面的特征样本来调节生成过程来完成的。潜在的三平面外推法产生语义和几何上有意义的过渡，与现有场景和谐融合。2D布局调节机制用于控制场景元素的放置和布置。实验结果表明，BlockFusion能够在室内和室外场景中生成具有前所未有的高质量形状的多样化、几何一致和无边界的大型3D场景。 et.al.|[2401.17053](http://arxiv.org/abs/2401.17053)|null|
|**2024-01-26**|**Learning Neural Radiance Fields of Forest Structure for Scalable and Fine Monitoring**|这项工作利用神经辐射场和遥感技术用于林业应用。在这里，我们展示了神经辐射场为改进森林监测中现有的遥感方法提供了广泛的可能性。我们提出的实验证明了它们的潜力：（1）表达森林三维结构的精细特征，（2）融合可用的遥感模式，（3）改进三维结构衍生的森林指标。总之，这些特性使神经场成为一种有吸引力的计算工具，具有进一步提高森林监测程序的可扩展性和准确性的巨大潜力。 et.al.|[2401.15029](http://arxiv.org/abs/2401.15029)|null|
|**2024-01-25**|**Learning Robust Generalizable Radiance Field with Visibility and Feature Augmented Point Representation**|本文介绍了广义神经辐射场（NeRF）的一种新范式。以前的通用NeRF方法将多视点立体技术与基于图像的神经渲染相结合进行泛化，产生了令人印象深刻的结果，同时存在三个问题。首先，遮挡常常导致不一致的特征匹配。然后，由于采样点和粗略特征聚合的单独过程，它们在几何不连续性和局部尖锐形状中传递失真和伪影。第三，当源视图离目标视图不够近时，它们基于图像的表示会发生严重退化。为了应对挑战，我们提出了第一个基于点而不是基于图像的渲染构建可泛化神经场的范式，我们称之为可泛化神经点场（GPF）。我们的方法通过几何先验显式地建模可见性，并用神经特征增强它们。我们提出了一种新的非均匀对数采样策略，以提高渲染速度和重建质量。此外，我们提出了一种可学习的内核，该内核在空间上增加了用于特征聚合的特征，减轻了几何结构急剧变化的地方的失真。此外，我们的表现很容易被操纵。实验表明，在泛化和微调设置中，我们的模型可以在三个数据集上提供比所有对应模型和基准更好的几何结构、视图一致性和渲染质量，初步证明了可泛化NeRF新范式的潜力。 et.al.|[2401.14354](http://arxiv.org/abs/2401.14354)|null|
|**2024-01-24**|**Unified neural field theory of brain dynamics underlying oscillations in Parkinson's disease and generalized epilepsies**|通过皮质丘脑基底神经节（CTBG）系统的神经场模型，联合探讨了帕金森病（PD）和全身性癫痫的病理同步神经振荡的机制。基底神经节（BG）被近似为一个单一的有效群体，并分析了它们在调节振荡皮质丘脑（CT）动力学中的作用，反之亦然。除了正常的脑电图节律外，模型中还存在4 Hz和20 Hz左右的增强活动，这与PD的特征频率一致。这些节律是由BG和CT人群之间回路中的共振引起的，类似于先前CT模型中潜在的癫痫振荡。多巴胺耗竭被认为削弱了对PD中这些共振的抑制，网络连接解释了在4-8Hz和20Hz左右BG、丘脑和皮层活动之间的显著一致性。丘脑网状核（TRN）和BG的传入和传出连接位点之间的相似性预测低多巴胺对应于强直-阵挛（大发作）癫痫发作的可能性降低，这与实验结果一致。此外，该模型预测，与实验结果相匹配的低多巴胺水平会增加缺席（轻微）癫痫发作的可能性。与其他CTBG建模研究一致，当传入和传出BG与CT系统的连接增强时，表现出对缺席发作活动的抑制。BG被证明在强直-阵挛发作状态附近抑制CTBG系统的活性，从而深入了解BG回路中目前治疗的疗效。TRN的睡眠状态也被发现可以抑制病理性PD活动匹配观察。总的来说，这些发现证明了广泛性癫痫和帕金森病的相干振荡之间有很强的相似性，并为可能的合并症提供了见解。 et.al.|[2401.13467](http://arxiv.org/abs/2401.13467)|null|
|**2024-01-17**|**Reproducibility via neural fields of visual illusions induced by localized stimuli**|本文研究了Billock和Tsou[PNAS，2007]使用Amari型神经场的可控性对初级视皮层（V1）皮层活动进行建模的实验复制，重点关注中央凹或外周视野中的规则漏斗模式。其目的是理解和模拟在这些实验中观察到的视觉现象，强调其非线性性质。这项研究包括设计模拟Billock和Tsou实验中视觉刺激的感官输入。然后从理论和数值上研究这些输入引起的后图像，以确定它们复制实验观察到的视觉效果的能力。这项研究的一个关键方面是研究神经反应的非线性性质所引起的影响。特别是，通过强调兴奋性和抑制性神经元在某些视觉现象出现中的重要性，这项研究表明，这两种类型的神经元活动的相互作用在视觉过程中发挥着重要作用，挑战了后者主要由兴奋性活动单独驱动的假设。 et.al.|[2401.09108](http://arxiv.org/abs/2401.09108)|null|
|**2024-01-12**|**Motion2VecSets: 4D Latent Vector Set Diffusion for Non-rigid Shape Reconstruction and Tracking**|我们介绍了Motion2VecSets，这是一种用于从点云序列进行动态曲面重建的4D扩散模型。虽然现有的最先进的方法已经证明在使用神经场表示重建非刚性对象方面取得了成功，但传统的前馈网络遇到了来自噪声、部分或稀疏点云的模糊观测的挑战。为了应对这些挑战，我们引入了一种扩散模型，该模型通过压缩潜在表示的迭代去噪过程来显式学习非刚性对象的形状和运动分布。当处理模糊输入时，基于扩散的先验能够进行更合理和概率的重建。我们用潜在向量集参数化4D动力学，而不是使用全局潜在。这种新颖的4D表示使我们能够学习局部表面形状和变形模式，从而实现更准确的非线性运动捕捉，并显著提高对看不见的运动和身份的可推广性。对于更具时间连贯性的目标跟踪，我们同步地对变形潜集进行去噪，并在多个帧之间交换信息。为了避免计算开销，我们设计了一个交错的空间和时间注意力块，以沿着空间和时间域交替聚集变形潜伏期。与最先进的方法进行了广泛的比较，证明了我们的Motion2VenSets在从各种不完美的观测进行4D重建方面的优势，特别是在从DeformingThings4D Animals数据集上的稀疏点云重建看不见的个体方面，与CaDex相比，交集优于并集（IoU）提高了19%。更多详细信息，请访问https://vveicao.github.io/projects/Motion2VecSets/. et.al.|[2401.06614](http://arxiv.org/abs/2401.06614)|null|
|**2024-01-05**|**Denoising Vision Transformers**|我们深入研究了视觉转换器（ViTs）固有的一个细微但重大的挑战：这些模型的特征图显示出网格状的伪影，这对ViTs在下游任务中的性能造成了不利影响。我们的研究将这个基本问题追溯到输入阶段的位置嵌入。为了解决这一问题，我们提出了一种新的噪声模型，该模型普遍适用于所有的ViT。具体来说，噪声模型将ViT输出分解为三个部分：一个没有噪声伪影的语义术语和两个以像素位置为条件的伪影相关术语。这种分解是通过在每幅图像的基础上加强与神经场的交叉视图特征一致性来实现的。这种逐图像优化过程从原始ViT输出中提取无伪影特征，为离线应用程序提供干净的特征。扩大了我们的解决方案的范围，以支持在线功能，我们引入了一种可学习的去噪器，直接从未处理的ViT输出中预测无伪影特征，这显示出对新数据的显著泛化能力，而无需对每张图像进行优化。我们的两阶段方法，称为去噪视觉转换器（DVT），不需要重新训练现有的预先训练的ViT，并且立即适用于任何基于转换器的架构。我们在各种具有代表性的ViT（DINO、MAE、DeiT III、EVA02、CLIP、DINOv2、DINOv2-reg）上评估了我们的方法。广泛的评估表明，我们的DVT在多个数据集（例如+3.84mIoU）的语义和几何任务中持续显著地改进了现有的最先进的通用模型。我们希望我们的研究将鼓励对ViT设计进行重新评估，特别是关于位置嵌入的天真使用。 et.al.|[2401.02957](http://arxiv.org/abs/2401.02957)|null|
|**2023-12-30**|**PlanarNeRF: Online Learning of Planar Primitives with Neural Radiance Fields**|从视觉数据中识别空间完整的平面基元是计算机视觉中的一项关键任务。现有的方法在很大程度上局限于2D片段恢复或简化3D结构，即使具有广泛的平面注释。我们提出了PlanarNeRF，这是一种能够通过在线学习检测密集3D平面的新框架。PlanarNeRF利用神经场表示，带来了三个主要贡献。首先，它利用并行的外观和几何知识增强了三维平面检测。其次，提出了一种轻量级的平面拟合模块来估计平面参数。第三，引入了一种具有更新机制的新的全局内存库结构，确保了跨帧一致性。PlanarNeRF的灵活架构使其能够在二维监督和自监督解决方案中发挥作用，在每种解决方案中，它都可以有效地从稀疏的训练信号中学习，显著提高训练效率。通过广泛的实验，我们证明了PlanarNeRF在各种场景下的有效性，并比现有工作有了显著的改进。 et.al.|[2401.00871](http://arxiv.org/abs/2401.00871)|null|
|**2024-01-01**|**Deblurring 3D Gaussian Splatting**|最近对辐射场的研究为具有照片级真实感渲染质量的新颖视图合成铺平了坚实的道路。然而，它们通常使用神经网络和体积绘制，这两种方法的训练成本很高，并且由于绘制时间长，阻碍了它们在各种实时应用中的广泛使用。最近，人们提出了一种基于3D高斯散射的方法来对3D场景进行建模，并在实时渲染图像的同时实现了显著的视觉质量。然而，如果训练图像模糊，则渲染质量会严重下降。模糊通常是由于镜头散焦、物体运动和相机抖动而产生的，它不可避免地会干扰干净图像的获取。先前的几项研究试图使用神经场从模糊的输入图像中渲染干净清晰的图像。然而，这些工作中的大多数仅设计用于基于体积渲染的神经辐射场，并不直接适用于基于光栅化的3D高斯散射方法。因此，我们提出了一种新的实时去模糊框架，即去模糊3D高斯散点，使用小型多层感知器（MLP）来操纵每个3D高斯的协方差来对场景模糊度进行建模。虽然去模糊的3D高斯飞溅仍然可以享受实时渲染，但它可以从模糊的图像中重建精细和清晰的细节。在该基准上进行了各种实验，结果显示了我们的去模糊方法的有效性。定性结果可在https://benhenryl.github.io/Deblurring-3D-Gaussian-Splatting/ et.al.|[2401.00834](http://arxiv.org/abs/2401.00834)|null|

<p align=right>(<a href=#updated-on-20240209>back to top</a>)</p>

[contributors-shield]: https://img.shields.io/github/contributors/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[contributors-url]: https://github.com/Vincentqyw/cv-arxiv-daily/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[forks-url]: https://github.com/Vincentqyw/cv-arxiv-daily/network/members
[stars-shield]: https://img.shields.io/github/stars/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[stars-url]: https://github.com/Vincentqyw/cv-arxiv-daily/stargazers
[issues-shield]: https://img.shields.io/github/issues/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[issues-url]: https://github.com/Vincentqyw/cv-arxiv-daily/issues

