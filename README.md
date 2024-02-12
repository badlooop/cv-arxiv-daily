[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]

## Updated on 2024.02.12
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
|**2024-02-09**|**NCRF: Neural Contact Radiance Fields for Free-Viewpoint Rendering of Hand-Object Interaction**|在三维计算机视觉中，建模手与物体的交互是一项具有根本挑战性的任务。尽管在该领域已经取得了显著的进展，但现有的方法仍然无法真实地合成手与物体的交互照片，因为手与物体之间的严重相互遮挡导致渲染质量下降，以及手与物体姿态估计不准确。为了应对这些挑战，我们提出了一种新的自由视点渲染框架，即神经接触辐射场（NCRF），以从稀疏的视频集重建手与物体的交互。特别地，所提出的NCRF框架由两个关键组件组成：（a）接触优化字段，该字段从3D查询点预测准确的接触字段，以实现手和物体之间的期望接触。（b） 手对象神经辐射场，用于学习静态规范空间中的隐含手对象表示，与专门设计的手对象运动场相一致，以产生观察到的规范对应关系。我们共同学习这些关键组件，它们在视觉和几何约束下相互帮助和规则化，产生高质量的手对象重建，实现照片逼真的新颖视图合成。在HO3D和DexYCB数据集上进行的大量实验表明，我们的方法在渲染质量和姿态估计精度方面都优于当前最先进的方法。 et.al.|[2402.05532](http://arxiv.org/abs/2402.05532)|null|
|**2024-02-07**|**SPAD : Spatially Aware Multiview Diffusers**|我们提出了SPAD，这是一种从文本提示或单个图像创建一致多视图图像的新方法。为了实现多视图生成，我们通过扩展具有跨视图交互的自注意层来重新调整预训练的2D扩散模型的用途，并在Ob厌恶的高质量子集上对其进行微调。我们发现，先前工作中提出的自我关注的天真扩展（例如MVDream）会导致视图之间的内容复制。因此，我们明确地限制了基于核极几何的跨视图注意力。为了进一步增强3D一致性，我们利用从相机射线导出的Plucker坐标，并将其作为位置编码注入。这使得SPAD能够对3D井中的空间接近度进行推理。与最近只能在固定方位角和仰角下生成视图的工作不同，SPAD提供了完整的相机控制，并在Ob厌恶和谷歌扫描对象数据集中对看不见的对象进行新的视图合成方面取得了最先进的结果。最后，我们证明了使用SPAD的文本到3D生成可以防止多面Janus问题。更多详细信息，请访问我们的网页：https://yashkant.github.io/spad et.al.|[2402.05235](http://arxiv.org/abs/2402.05235)|null|
|**2024-02-06**|**EscherNet: A Generative Model for Scalable View Synthesis**|我们介绍了EscherNet，一个用于视图合成的多视图条件扩散模型。EscherNet学习隐含的和生成的3D表示，再加上专门的相机位置编码，允许对任意数量的参考视图和目标视图之间的相机变换进行精确和连续的相对控制。EscherNet在视图合成方面提供了非凡的通用性、灵活性和可扩展性——尽管它使用固定数量的3个参考视图到3个目标视图进行训练，但它可以在单个消费级GPU上同时生成100多个一致的目标视图。因此，EscherNet不仅解决了零样本新视图合成问题，而且自然地将单图像和多图像3D重建相结合，将这些不同的任务组合成一个单一的、有凝聚力的框架。我们的大量实验表明，EscherNet在多个基准测试中实现了最先进的性能，即使与专门针对每个单独问题定制的方法相比也是如此。这种非凡的多功能性为设计用于3D视觉的可扩展神经结构开辟了新的方向。项目页面：\url{https://kxhit.github.io/EscherNet}. et.al.|[2402.03908](http://arxiv.org/abs/2402.03908)|null|
|**2024-02-06**|**Rig3DGS: Creating Controllable Portraits from Casual Monocular Videos**|从随意的智能手机视频中创建可控的3D人像是非常可取的，因为它们在AR/VR应用中具有巨大的价值。3D高斯散点（3DGS）的最新发展已经显示出在渲染质量和训练效率方面的改进。然而，要从单个视图捕捉中准确地建模和分解头部运动和面部表情，以实现高质量的渲染，仍然是一个挑战。在本文中，我们介绍了Rig3DGS来应对这一挑战。我们在规范空间中使用一组3D高斯表示整个场景，包括动态主体。使用一组控制信号，如头部姿势和表情，我们将它们转换到具有学习变形的3D空间，以生成所需的渲染。我们的关键创新是一种精心设计的变形方法，该方法以从3D可变形模型导出的可学习先验为指导。这种方法在训练中效率很高，在控制各种捕捉的面部表情、头部位置和视图合成方面也很有效。我们通过大量的定量和定性实验证明了我们所学变形的有效性。项目页面位于http://shahrukhathar.github.io/2024/02/05/Rig3DGS.html et.al.|[2402.03723](http://arxiv.org/abs/2402.03723)|null|
|**2024-02-05**|**Denoising Diffusion via Image-Based Rendering**|生成3D场景是一个具有挑战性的开放问题，需要合成在3D空间中完全一致的看似合理的内容。虽然最近的方法（如神经辐射场）擅长于视图合成和3D重建，但由于缺乏生成能力，它们无法在未观察到的区域合成看似合理的细节。相反，现有的生成方法通常无法重建野外的详细、大规模场景，因为它们使用有限容量的3D场景表示，需要对齐的相机姿势，或者依赖于额外的正则化子。在这项工作中，我们介绍了第一个能够快速、详细地重建和生成真实世界3D场景的扩散模型。为了实现这一目标，我们作出了三点贡献。首先，我们引入了一种新的神经场景表示，即IB平面，它可以有效而准确地表示大型3D场景，并根据需要动态分配更多的容量来捕捉每个图像中可见的细节。其次，我们提出了一种去噪扩散框架来学习这种新颖的3D场景表示的先验知识，仅使用2D图像，而不需要任何额外的监督信号，如掩模或深度。这支持在统一架构中进行3D重建和生成。第三，我们开发了一种原则性方法，通过放弃一些图像的表示，在将基于图像的渲染与扩散模型集成时避免琐碎的3D解决方案。我们在真实图像和合成图像的几个具有挑战性的数据集上评估了该模型，并展示了在生成、新视图合成和3D重建方面的卓越结果。 et.al.|[2402.03445](http://arxiv.org/abs/2402.03445)|null|
|**2024-02-07**|**4D Gaussian Splatting: Towards Efficient Novel View Synthesis for Dynamic Scenes**|我们考虑动态场景的新视图合成（NVS）问题。最近的神经方法已经为静态3D场景实现了异常的NVS结果，但对4D时变场景的扩展仍然是不平凡的。先前的工作通常通过学习规范空间加上隐式或显式变形场来编码动力学，这些变形场在突发运动或捕捉高保真渲染等具有挑战性的场景中很困难。在本文中，我们介绍了4D高斯散射（4DGS），这是一种用各向异性4D XYZT高斯表示动态场景的新方法，其灵感来自于3D高斯散射在静态场景中的成功。我们通过对4D高斯进行时间切片来对每个时间戳的动力学进行建模，4D高斯自然构成动态3D高斯，并可以无缝投影到图像中。作为一种明确的时空表示，4DGS展示了对复杂动力学和精细细节建模的强大能力，尤其是对于具有突然运动的场景。我们在高度优化的CUDA加速框架中进一步实现了我们的时间切片和飞溅技术，在RTX 3090 GPU上实现了高达277 FPS的实时推理渲染速度，在RTX4090 GPU上达到了583 FPS的实时推断渲染速度。对不同运动场景的严格评估显示了4DGS的卓越效率和有效性，它在数量和质量上都始终优于现有方法。 et.al.|[2402.03307](http://arxiv.org/abs/2402.03307)|null|
|**2024-02-05**|**ViewFusion: Learning Composable Diffusion Models for Novel View Synthesis**|深度学习为新视图合成的老问题提供了丰富的新方法，从基于神经辐射场（NeRF）的方法到端到端风格的架构。每种方法都有特定的优势，但在适用性方面也有特定的局限性。这项工作介绍了ViewFusion，这是一种最先进的端到端生成新视图合成方法，具有无与伦比的灵活性。ViewFusion包括同时将扩散去噪步骤应用于场景的任意数量的输入视图，然后将为每个视图获得的噪声梯度与（推断的）像素加权掩码相结合，确保对于目标场景的每个区域，只考虑信息量最大的输入视图。我们的方法通过以下方式解决了以前方法的几个局限性：（1）可在多个场景和对象类中进行训练和推广，（2）在训练和测试时自适应地获取可变数量的无姿态视图，（3）即使在严重不确定的条件下也能生成合理的视图（由于其生成性）——同时生成质量与最先进方法不相上下甚至更好的视图。局限性包括没有生成场景的3D嵌入，导致推理速度相对较慢，并且我们的方法仅在相对较小的数据集NMR上进行测试。代码可用。 et.al.|[2402.02906](http://arxiv.org/abs/2402.02906)|**[link](https://github.com/bronemos/view-fusion)**|
|**2024-02-06**|**GaMeS: Mesh-Based Adapting and Modification of Gaussian Splatting**|近年来，已经引入了一系列基于神经网络的图像渲染方法。例如，广泛研究的神经辐射场（NeRF）依赖于神经网络来表示3D场景，从而允许从少量2D图像中合成逼真的视图。然而，大多数NeRF模型都受到长训练和推理时间的限制。相比之下，高斯散射（GS）是一种新颖的、最先进的技术，用于通过高斯分布近似点对图像像素的贡献来渲染3D场景中的点，从而保证快速训练和快速实时渲染。GS的一个缺点是，由于需要对几十万个高斯分量进行调节，因此缺乏定义明确的方法来进行调节。为了解决这个问题，我们引入了高斯网格飞溅（GaMeS）模型，这是网格和高斯分布的混合，它将所有高斯飞溅物固定在物体表面（网格）上。我们的方法的独特贡献是仅根据高斯飞溅在网格上的位置来定义高斯飞溅，从而允许在动画过程中自动调整位置、比例和旋转。因此，我们在实时生成高质量视图的过程中获得了高质量的渲染图。此外，我们证明，在没有预定义网格的情况下，可以在学习过程中微调初始网格。 et.al.|[2402.01459](http://arxiv.org/abs/2402.01459)|**[link](https://github.com/waczjoan/gaussian-mesh-splatting)**|
|**2024-02-01**|**360-GS: Layout-guided Panoramic Gaussian Splatting For Indoor Roaming**|近年来，三维高斯散射（3D-GS）以其实时性和照片真实性的渲染引起了人们的极大关注。这项技术通常将透视图像作为输入，并通过将一组3D椭圆高斯分布到图像平面上来优化它们，从而产生2D高斯。然而，将3D-GS应用于全景输入在使用2D高斯有效地将投影建模到 ${360^\circ}$图像的球面上方面存在挑战。在实际应用中，输入全景图往往是稀疏的，导致3D高斯图的初始化不可靠，并导致3D-GS质量下降。此外，由于无纹理平面（例如，墙和地板）的几何约束不足，3D-GS难以用椭圆高斯对这些平坦区域进行建模，导致在新视图中出现显著的浮动。为了解决这些问题，我们提出了360-GS，这是一种针对有限的全景输入集的新的$360^{\circ}$ 高斯飞溅。360-GS不是将3D高斯直接泼洒到球面上，而是将其投影到单位球体的切平面上，然后将其映射到球面投影。这种自适应使得能够使用高斯表示投影。我们通过利用全景图中的布局先验来指导360-GS的优化，这些先验易于获得，并包含关于室内场景的强大结构信息。我们的实验结果表明，360-GS允许全景渲染，并在新的视图合成中以更少的伪影优于最先进的方法，从而在室内场景中提供身临其境的漫游。 et.al.|[2402.00763](http://arxiv.org/abs/2402.00763)|null|
|**2024-02-01**|**StopThePop: Sorted Gaussian Splatting for View-Consistent Real-time Rendering**|高斯散射已经成为从不同领域的图像构建3D表示的一个突出模型。然而，3D高斯飞溅渲染管道的效率依赖于几个简化。值得注意的是，使用单个视图空间深度将高斯飞溅减少到2D会在视图旋转过程中引入爆裂和混合伪影。解决这个问题需要精确的每像素深度计算，但与全局排序操作相比，完整的每像素排序成本过高。在本文中，我们提出了一种新的分层光栅化方法，该方法以最小的处理开销系统地处理和剔除飞溅。我们的软件光栅化器有效地消除了弹出的伪影和视图不一致，通过定量和定性测量都证明了这一点。同时，我们的方法通过弹出来减少欺骗视图相关效果的可能性，确保了更真实的表示。尽管消除了作弊，但我们的方法在测试图像中获得了可比的定量结果，同时提高了运动中新视图合成的一致性。由于其设计，我们的分层方法平均只比原始的高斯飞溅慢4%。值得注意的是，强制执行一致性可以将Gaussian的数量减少大约一半，同时具有几乎相同的质量和视图一致性。因此，渲染性能几乎翻了一番，使我们的方法比原始的高斯Splatting快1.6倍，同时减少了50%的内存需求。 et.al.|[2402.00525](http://arxiv.org/abs/2402.00525)|null|

<p align=right>(<a href=#updated-on-20240212>back to top</a>)</p>

## 3D Reconstruction

|Publish Date|Title|Abstract|PDF|Code|
|---|---|---|---|---|
|**2024-02-07**|**Carousel phase retrieval algorithm for 3D coherent X-ray diffraction imaging**|相干X射线衍射成像（CXDI）是一种独特的技术，通过基于测量的散射强度图执行计算相位重建程序，可以以纳米级分辨率重建2D和3D物体。重建过程可能具有高计算复杂度，并且通常不能在实验期间实时执行。我们提出了一种转盘相位检索算法（CPRA），该算法基于傅立叶切片定理将3D重建问题表示为对应于不同收集角度的投影图像的一组2D重建。为了保持2D重建之间的一致性，我们引入了一种迭代过程，其中每个2D重建都以周期性（旋转）的方式基于相邻的2D重建。2D重建的使用大大减少了计算时间和内存消耗。我们展示了在CPU和GPU计算架构上针对各种空间大小的复杂生物细胞的测试问题的CPRA实现。与传统的CXDI重建算法相比，CPRA在GPU上表现出300倍的速度，在CPU上表现出120倍的速度。CPRA还可以实现更高的重建质量。所实现的速度允许实时对计算上较大的对象进行高分辨率重建。 et.al.|[2402.05283](http://arxiv.org/abs/2402.05283)|**[link](https://github.com/UCSD-CEM/Carousel-Phase-Retrieval-Algorithm)**|
|**2024-02-07**|**Scalable Multi-view Clustering via Explicit Kernel Features Maps**|人们越来越意识到多视图学习是数据科学和机器学习的重要组成部分，这是多视图在现实世界应用中越来越普遍的结果，尤其是在网络环境中。在本文中，我们介绍了一种新的多视图子空间聚类的可扩展性框架。提出了一种有效的优化策略，利用核特征图来减少计算负担，同时保持良好的聚类性能。该算法的可扩展性意味着它可以在几分钟内使用标准机器应用于大规模数据集，包括具有数百万数据点的数据集。我们在不同规模的真实世界基准网络上进行了广泛的实验，以评估我们的算法相对于最先进的多视图子空间聚类方法和属性网络多视图方法的性能。 et.al.|[2402.04794](http://arxiv.org/abs/2402.04794)|null|
|**2024-02-06**|**EscherNet: A Generative Model for Scalable View Synthesis**|我们介绍了EscherNet，一个用于视图合成的多视图条件扩散模型。EscherNet学习隐含的和生成的3D表示，再加上专门的相机位置编码，允许对任意数量的参考视图和目标视图之间的相机变换进行精确和连续的相对控制。EscherNet在视图合成方面提供了非凡的通用性、灵活性和可扩展性——尽管它使用固定数量的3个参考视图到3个目标视图进行训练，但它可以在单个消费级GPU上同时生成100多个一致的目标视图。因此，EscherNet不仅解决了零样本新视图合成问题，而且自然地将单图像和多图像3D重建相结合，将这些不同的任务组合成一个单一的、有凝聚力的框架。我们的大量实验表明，EscherNet在多个基准测试中实现了最先进的性能，即使与专门针对每个单独问题定制的方法相比也是如此。这种非凡的多功能性为设计用于3D视觉的可扩展神经结构开辟了新的方向。项目页面：\url{https://kxhit.github.io/EscherNet}. et.al.|[2402.03908](http://arxiv.org/abs/2402.03908)|null|
|**2024-02-06**|**Efficient Generation of Hidden Outliers for Improved Outlier Detection**|异常值生成是一种常用的技术，用于解决重要的异常值检测任务。生成具有现实行为的异常值具有挑战性。现有的流行方法往往忽略高维空间中异常值的“多视图”特性。对这一财产进行核算的唯一现有方法在效率和有效性方面不足。我们提出了BISECT，这是一种新的异常值生成方法，可以创建模拟上述属性的真实异常值。为此，BISECT采用了本文中介绍的一个新颖命题，说明如何有效地生成所述现实异常值。我们的方法比当前重建“多个视图”的方法有更好的保证和复杂性。我们使用BISECT生成的合成异常值来有效地增强不同数据集中的异常值检测，用于多种用例。例如，与基线相比，BISECT的过采样将误差减少了3倍。 et.al.|[2402.03846](http://arxiv.org/abs/2402.03846)|**[link](https://github.com/jcribeiro98/bisect)**|
|**2024-02-09**|**MoD-SLAM: Monocular Dense Mapping for Unbounded 3D Scene Reconstruction**|神经隐式表示最近已经在许多领域得到了证明，包括同时定位和映射（SLAM）。目前的神经SLAM在重建有界场景时可以获得理想的结果，但这依赖于RGB-D图像的输入。仅基于RGB图像的基于神经的SLAM无法准确地重建场景的尺度，而且由于跟踪过程中积累的误差，它还存在尺度漂移。为了克服这些限制，我们提出了MoD SLAM，这是一种单目密集映射方法，允许在无界场景中实时进行全局姿态优化和3D重建。通过单目深度估计优化场景重建，并使用闭环检测更新相机姿态，可以在大型场景上进行详细而精确的重建。与以前的工作相比，我们的方法更加健壮、可扩展和通用。我们的实验表明，与现有的神经SLAM方法相比，MoD-SLAM具有更出色的映射性能，尤其是在大型无边界场景中。 et.al.|[2402.03762](http://arxiv.org/abs/2402.03762)|null|
|**2024-02-05**|**Denoising Diffusion via Image-Based Rendering**|生成3D场景是一个具有挑战性的开放问题，需要合成在3D空间中完全一致的看似合理的内容。虽然最近的方法（如神经辐射场）擅长于视图合成和3D重建，但由于缺乏生成能力，它们无法在未观察到的区域合成看似合理的细节。相反，现有的生成方法通常无法重建野外的详细、大规模场景，因为它们使用有限容量的3D场景表示，需要对齐的相机姿势，或者依赖于额外的正则化子。在这项工作中，我们介绍了第一个能够快速、详细地重建和生成真实世界3D场景的扩散模型。为了实现这一目标，我们作出了三点贡献。首先，我们引入了一种新的神经场景表示，即IB平面，它可以有效而准确地表示大型3D场景，并根据需要动态分配更多的容量来捕捉每个图像中可见的细节。其次，我们提出了一种去噪扩散框架来学习这种新颖的3D场景表示的先验知识，仅使用2D图像，而不需要任何额外的监督信号，如掩模或深度。这支持在统一架构中进行3D重建和生成。第三，我们开发了一种原则性方法，通过放弃一些图像的表示，在将基于图像的渲染与扩散模型集成时避免琐碎的3D解决方案。我们在真实图像和合成图像的几个具有挑战性的数据集上评估了该模型，并展示了在生成、新视图合成和3D重建方面的卓越结果。 et.al.|[2402.03445](http://arxiv.org/abs/2402.03445)|null|
|**2024-02-02**|**Di-NeRF: Distributed NeRF for Collaborative Learning with Unknown Relative Poses**|未知环境的协作映射可以比单个机器人更快、更稳健地完成。然而，协作方法需要一个可扩展的分布式范式来处理通信问题。这项工作提出了一种全分布式算法，使一组机器人能够共同优化神经辐射场（NeRF）的参数。该算法涉及每个机器人训练的NeRF参数在网状网络上的通信，在网状网络中，每个机器人训练其NeRF，并且只能访问自己的视觉数据。此外，所有机器人的相对姿态都与模型参数一起进行了联合优化，从而能够使用未知的相对相机姿态进行映射。我们证明了多机器人系统可以受益于从多个NeRF优化的可微分和鲁棒的3D重建。在真实世界和合成数据上的实验证明了所提出的算法的有效性。实验视频和补充材料见项目网站(https://sites.google.com/view/di-nerf/home). et.al.|[2402.01485](http://arxiv.org/abs/2402.01485)|null|
|**2024-02-02**|**SiMA-Hand: Boosting 3D Hand-Mesh Reconstruction by Single-to-Multi-View Adaptation**|从RGB图像中估计3D手部网格是一个长期存在的问题，其中遮挡是最具挑战性的问题之一。当遮挡在图像空间中占主导地位时，针对该任务的现有尝试往往失败。在本文中，我们提出了SiMA Hand，旨在通过单视图到多视图自适应来提高网格重建性能。首先，我们设计了一个多视图手动重建器，通过在图像、关节和顶点级别全面采用特征融合来融合多个视图之间的信息。然后，我们介绍了一种配备SiMA的单视图手动重建器。尽管在推理时仅将一个视图作为输入，但通过在训练时从额外的视图中学习非遮挡知识，可以丰富单个视图重构器中的形状和方向特征，提高遮挡区域的重构精度。我们在Dex-YCB和HanCo基准上对具有挑战性的物体和自身造成的遮挡情况进行了实验，表明SiMA Hand始终实现了优于现有技术的性能。代码将于发布https://github.com/JoyboyWang/SiMA-HandPytorch。 et.al.|[2402.01389](http://arxiv.org/abs/2402.01389)|**[link](https://github.com/JoyboyWang/SiMA-Hand_Pytorch)**|
|**2024-02-02**|**DeepAAT: Deep Automated Aerial Triangulation for Fast UAV-based Mapping**|自动空中三角测量（AAT）旨在恢复图像姿态和重建稀疏点，在对地观测中发挥着关键作用。AAT在摄影测量领域拥有数十年的丰富研究遗产，已发展成为一个广泛应用于大规模无人机测绘的基础过程。尽管取得了进步，但经典的AAT方法仍然面临着效率低和稳健性有限等挑战。本文介绍了DeepAAT，一个专门为无人机图像AAT设计的深度学习网络。DeepAAT考虑了图像的空间和光谱特征，增强了其解决错误匹配对和准确预测图像姿态的能力。DeepAAT标志着AAT效率的重大飞跃，确保了全面的场景覆盖和精度。其处理速度超过增量AAT方法数百倍，超过全局AAT方法数十倍，同时保持了相当水平的重建精度。此外，DeepAAT的场景聚类和合并策略有助于大规模无人机图像的快速定位和姿态确定，即使在计算资源有限的情况下也是如此。实验结果表明，DeepAAT比传统的AAT方法有了实质性的改进，突出了其在基于无人机的三维重建任务的效率和准确性方面的潜力。为了造福摄影测量学会，DeepAAT的代码将发布在：https://github.com/WHU-USI3DV/DeepAAT. et.al.|[2402.01134](http://arxiv.org/abs/2402.01134)|**[link](https://github.com/whu-usi3dv/deepaat)**|
|**2024-02-02**|**Learning Which Side to Scan: Multi-View Informed Active Perception with Side Scan Sonar for Autonomous Underwater Vehicles**|自动水下航行器通常执行捕获目标的多个视图的勘测，以便为人类操作员或自动目标识别算法提供更多信息。在这项工作中，我们解决了选择信息量最大的视图的问题，这些视图可以最大限度地减少调查时间，同时最大限度地提高分类器的准确性。我们介绍了一种新的主动感知框架，用于使用侧扫声纳图像进行多视图自适应测量和重新获取。我们的框架通过使用自适应调查任务的图形公式来应对这一挑战。然后，我们使用图神经网络（GNN）对获取的声纳视图进行分类，并根据收集的数据选择下一个最佳视图。我们使用高保真侧扫声纳模拟器中的模拟调查来评估我们的方法。我们的结果表明，我们的方法能够在分类精度和调查效率方面超越最先进的方法。该框架是一种很有前途的方法，可用于更高效的自主任务，包括侧扫声纳，如水下勘探、海洋考古和环境监测。 et.al.|[2402.01106](http://arxiv.org/abs/2402.01106)|null|

<p align=right>(<a href=#updated-on-20240212>back to top</a>)</p>

## Diffusion

|Publish Date|Title|Abstract|PDF|Code|
|---|---|---|---|---|
|**2024-02-09**|**The impact of different unravelings in a monitored system of free fermions**|我们考虑了一个自由费米子链正在经历去相位，由两种不同的随机测量协议（解开）描述：量子态扩散和量子跳跃协议。这两种协议都将状态保持在Slater行列式形式，允许处理相当大的系统大小。我们发现测量算子沿量子轨迹的分布存在分叉跃迁，从单峰变为双峰。对于两种解开，发生这种转变的测量强度值相似，但分布和转变具有不同的性质，反映了两种测量协议的对称性。我们还考虑了Slater行列式分量的反参与比随系统大小的缩放，并找到了一个幂律缩放，它标志着在分解和任何非零测量强度中的多重分形行为。 et.al.|[2402.06597](http://arxiv.org/abs/2402.06597)|null|
|**2024-02-09**|**Diffusion-ES: Gradient-free Planning with Diffusion for Autonomous Driving and Zero-Shot Instruction Following**|扩散模型擅长为决策和控制建模复杂和多模式的轨迹分布。最近提出了奖励梯度引导去噪，以生成最大化可微分奖励函数和扩散模型捕获的数据分布下的可能性的轨迹。奖励梯度引导去噪需要一个适用于干净样本和有噪声样本的可微分奖励函数，这限制了其作为通用轨迹优化器的适用性。在本文中，我们提出了DiffusionES，这是一种将无梯度优化与轨迹去噪相结合的方法，用于在数据流形中优化黑盒不可微目标。扩散ES从扩散模型中对进化搜索过程中的轨迹进行采样，并使用黑匣子奖励函数对其进行评分。它使用截断扩散过程来变异高分轨迹，该过程应用了少量的去噪和去噪步骤，从而能够更有效地探索解空间。我们展示了DiffusionES在nuPlan上实现了最先进的性能，nuPlan是一个已建立的自动驾驶闭环规划基准。扩散ES优于现有的基于采样的规划者、反应性确定性或基于扩散的策略以及奖励梯度指导。此外，我们还表明，与先前的引导方法不同，我们的方法可以优化由少镜头LLM提示生成的不可微语言形状的奖励函数。当由发出指令的人类教师指导时，我们的方法可以产生新的、高度复杂的行为，例如攻击性的车道编织，而这些行为在训练数据中并不存在。这使我们能够解决最困难的nuPlan场景，这些场景超出了现有轨迹优化方法和驱动策略的能力。 et.al.|[2402.06559](http://arxiv.org/abs/2402.06559)|null|
|**2024-02-09**|**The role of mobility in epidemics near criticality**|一般流行病过程（GEP），也称为易感感染者康复模型（SIR），描述了流行病如何在康复后获得永久免疫的易感人群中传播。该模型表现出二阶吸收态相变，通常在假设健康个体不动的情况下进行研究。我们通过引入GEP的两个推广来研究流动性对接近灭绝阈值的疾病传播的影响，其中易感个体和康复个体的流动性是独立检查的。在这两种情况下，包括迁移率都违反了GEP的快反对称性，并改变了吸收态的数量。通过微扰重整化群方法和使用Gillespie算法的大规模随机模拟来分析模型的临界动力学。重整化群分析预测，当感染者与扩散物种相互作用并在康复时获得免疫时，这两个模型属于同一个新的普适性类，描述流行病传播的关键动力学。在相关的重整化群不动点，不动物种与受感染物种的动力学解耦，主要由与扩散物种的耦合决定。二维数值模拟通过识别两个模型的同一组临界指数来确认我们的重整化群结果。通过打破相关的超尺度关系，证实了对快度反转对称性的破坏。我们的研究强调了流动性在接近灭绝阈值时形成种群传播动态的重要性。 et.al.|[2402.06505](http://arxiv.org/abs/2402.06505)|null|
|**2024-02-09**|**Sequential Flow Matching for Generative Modeling**|拉直连续时间生成模型（如扩散模型或基于流的模型）的概率流是通过数值求解器快速采样的关键，现有方法通过直接生成噪声和数据分布之间的联合分布的概率路径来学习线性路径。模拟这些生成模型的基于常微分方程的求解器采样速度慢的一个关键原因是常微分方程求解器的全局截断误差，这是由常微分方程轨迹的高曲率引起的，它在低NFE状态下爆炸了数值求解器的截断误差。为了应对这一挑战，我们提出了一种称为SeqRF的新方法，这是一种学习技术，可以拉直概率流以减少全局截断误差，从而加速采样并提高合成质量。在理论和实证研究中，我们首先观察了SeqRF的矫直特性。通过SeqRF基于流量的生成模型进行实证评估，我们在CIFAR-10、CelebA- $64\times 64$ 和LSUN Church数据集上取得了超越结果。 et.al.|[2402.06461](http://arxiv.org/abs/2402.06461)|null|
|**2024-02-09**|**ControlUDA: Controllable Diffusion-assisted Unsupervised Domain Adaptation for Cross-Weather Semantic Segmentation**|数据生成被认为是在不利天气下进行无监督领域自适应（UDA）相关语义分割的一种有效策略。然而，这些不利天气场景包含多种可能性，在之前的UDA工作中，对具有可控天气的高保真数据合成的研究不足。最近在大规模文本到图像扩散模型（DM）方面取得的进展为研究开辟了一条新的途径，使基于语义标签的真实图像的生成成为可能。由于共享标签空间，这种能力被证明有助于从源域到目标域的跨域数据合成。因此，源域标签可以与那些生成的伪目标数据配对，用于训练UDA。然而，从UDA的角度来看，DM训练存在几个挑战：（i）目标领域的基本事实标签缺失；（ii）提示生成器可能对来自不利天气的图像产生模糊或嘈杂的描述；（iii）当仅以语义标签为条件时，现有艺术往往难以很好地处理城市场景的复杂场景结构和几何结构。为了解决上述问题，我们提出了ControlUDA，这是一种为恶劣天气条件下的UDA分割量身定制的扩散辅助框架。它首先利用来自预先训练的分割器的目标先验来调整DM，补偿丢失的目标域标签；它还包含UDAControlNet，这是一个条件融合的多尺度即时增强网络，旨在在恶劣天气下生成高保真数据。使用我们生成的数据训练UDA，将模型性能带到了一个新的里程碑（72.0 mIoU），在流行的城市景观到ACDC的不利天气基准上。此外，ControlUDA有助于在看不见的数据上实现良好的模型可推广性。 et.al.|[2402.06446](http://arxiv.org/abs/2402.06446)|null|
|**2024-02-09**|**Improving 2D-3D Dense Correspondences with Diffusion Models for 6D Object Pose Estimation**|估计RGB图像和3D空间之间的2D-3D对应关系是6D物体姿态估计的基本问题。最近的姿态估计器使用密集对应图和点对点算法来估计物体姿态。姿态估计的准确性在很大程度上取决于密集对应图的质量及其抵抗遮挡、杂波和具有挑战性的材料特性的能力。目前，使用基于GANs、自动编码器或直接回归模型的图像到图像转换模型来估计密集对应图。然而，图像到图像翻译的最新进展导致在基准数据集上评估时，扩散模型是最佳选择。在这项研究中，我们比较了基于GANs和扩散模型的图像到图像翻译网络用于6D物体姿态估计的下游任务。我们的结果表明，基于扩散的图像到图像转换模型优于GAN，揭示了在6D物体姿态估计模型中进一步改进的潜力。 et.al.|[2402.06436](http://arxiv.org/abs/2402.06436)|null|
|**2024-02-09**|**Enhanced bubble growth near an advancing solidification front**|冷冻水可能看起来不透明，因为在冷冻过程中，杂质或气泡可能会被困在冰中。由于在其附近形成气体过饱和区域，后者在前进的凝固前沿附近成核并生长。传质速率和冻结速率之间的微妙相互作用决定了截留气泡的最终形状和大小。在这项工作中，我们通过实验和数值研究了这种气泡的初始生长，这些气泡在前进的冰锋附近成核并生长。我们表明，这些气泡的初始生长受扩散控制，并且由于背景气体浓度梯度的存在和接近前沿的运动的组合而增强。此外，我们将该问题重新划分为均匀浓度场中运动的球形物体的质量传递问题，发现我们的实验数据与后一个问题的现有比例关系之间存在良好的一致性。最后，我们讨论了气泡周围的流体流动如何进一步影响这种增长，并通过数值模拟对其进行了定性探索。 et.al.|[2402.06409](http://arxiv.org/abs/2402.06409)|null|
|**2024-02-09**|**Spectral properties of the Dirichlet-to-Neumann operator for spheroids**|我们研究了从针到圆盘的椭球域中Dirichlet到Neumann算子的谱性质和相关的Steklov问题。对于内部和外部问题，导出了该算子的显式矩阵表示。我们展示了球体的各向异性如何影响算子的本征值和本征函数。作为物理应用的例子，我们讨论了球形部分反应目标上的扩散控制反应，以及扩散粒子和球形边界之间相遇的统计数据。 et.al.|[2402.06372](http://arxiv.org/abs/2402.06372)|null|
|**2024-02-09**|**Sparse identification of nonlocal interaction kernels in nonlinear gradient flow equations via partial inversion**|我们讨论了从有噪声的离散轨迹数据中识别非线性聚集扩散方程中的非局部相互作用势的反问题。我们的方法涉及公式化和求解正则化变分问题，这需要最小化一组假设函数中的二次误差函数，并通过稀疏性增强正则化子进一步增强。我们使用类似于CoSaMP[57]和子空间追踪算法[31]的部分反演算法来解决基追踪问题。一个关键的理论贡献是我们对偏微分方程的新稳定性估计，验证了控制使用真实和估计的相互作用势生成的解之间的2-Wasserstein距离的误差函数能力。我们的工作还包括对实际实现中由离散化和观测误差引起的估计量的误差分析。我们通过展示集体行为的各种1D和2D示例来证明这些方法的有效性。 et.al.|[2402.06355](http://arxiv.org/abs/2402.06355)|null|
|**2024-02-09**|**Particle Denoising Diffusion Sampler**|去噪扩散模型对于生成建模已经变得无处不在。其核心思想是通过使用扩散将数据分布传输到高斯分布。然后，通过使用分数匹配思想估计这种扩散的时间反转，从数据分布中获得近似样本。我们在这里遵循类似的策略，从未归一化的概率密度中进行采样，并计算它们的归一化常数。然而，这里通过使用依赖于新的分数匹配损失的原始迭代粒子方案来模拟时间反向扩散。与标准的去噪扩散模型相反，所得的粒子去噪扩散采样器（PDDS）在温和的假设下提供了渐近一致的估计。我们在多模式和高维采样任务上演示PDDS。 et.al.|[2402.06320](http://arxiv.org/abs/2402.06320)|**[link](https://github.com/angusphillips/particle_denoising_diffusion_sampler)**|

<p align=right>(<a href=#updated-on-20240212>back to top</a>)</p>

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

<p align=right>(<a href=#updated-on-20240212>back to top</a>)</p>

[contributors-shield]: https://img.shields.io/github/contributors/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[contributors-url]: https://github.com/Vincentqyw/cv-arxiv-daily/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[forks-url]: https://github.com/Vincentqyw/cv-arxiv-daily/network/members
[stars-shield]: https://img.shields.io/github/stars/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[stars-url]: https://github.com/Vincentqyw/cv-arxiv-daily/stargazers
[issues-shield]: https://img.shields.io/github/issues/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[issues-url]: https://github.com/Vincentqyw/cv-arxiv-daily/issues

