[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]

## Updated on 2024.02.07
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
|**2024-02-06**|**EscherNet: A Generative Model for Scalable View Synthesis**|我们介绍了EscherNet，一个用于视图合成的多视图条件扩散模型。EscherNet学习隐含的和生成的3D表示，再加上专门的相机位置编码，允许对任意数量的参考视图和目标视图之间的相机变换进行精确和连续的相对控制。EscherNet在视图合成方面提供了非凡的通用性、灵活性和可扩展性——尽管它使用固定数量的3个参考视图到3个目标视图进行训练，但它可以在单个消费级GPU上同时生成100多个一致的目标视图。因此，EscherNet不仅解决了零样本新视图合成问题，而且自然地将单图像和多图像3D重建相结合，将这些不同的任务组合成一个单一的、有凝聚力的框架。我们的大量实验表明，EscherNet在多个基准测试中实现了最先进的性能，即使与专门针对每个单独问题定制的方法相比也是如此。这种非凡的多功能性为设计用于3D视觉的可扩展神经结构开辟了新的方向。项目页面：\url{https://kxhit.github.io/EscherNet}. et.al.|[2402.03908](http://arxiv.org/abs/2402.03908)|null|
|**2024-02-06**|**Rig3DGS: Creating Controllable Portraits from Casual Monocular Videos**|从随意的智能手机视频中创建可控的3D人像是非常可取的，因为它们在AR/VR应用中具有巨大的价值。3D高斯散点（3DGS）的最新发展已经显示出在渲染质量和训练效率方面的改进。然而，要从单个视图捕捉中准确地建模和分解头部运动和面部表情，以实现高质量的渲染，仍然是一个挑战。在本文中，我们介绍了Rig3DGS来应对这一挑战。我们在规范空间中使用一组3D高斯表示整个场景，包括动态主体。使用一组控制信号，如头部姿势和表情，我们将它们转换到具有学习变形的3D空间，以生成所需的渲染。我们的关键创新是一种精心设计的变形方法，该方法以从3D可变形模型导出的可学习先验为指导。这种方法在训练中效率很高，在控制各种捕捉的面部表情、头部位置和视图合成方面也很有效。我们通过大量的定量和定性实验证明了我们所学变形的有效性。项目页面位于http://shahrukhathar.github.io/2024/02/05/Rig3DGS.html et.al.|[2402.03723](http://arxiv.org/abs/2402.03723)|null|
|**2024-02-05**|**Denoising Diffusion via Image-Based Rendering**|生成3D场景是一个具有挑战性的开放问题，需要合成在3D空间中完全一致的看似合理的内容。虽然最近的方法（如神经辐射场）擅长于视图合成和3D重建，但由于缺乏生成能力，它们无法在未观察到的区域合成看似合理的细节。相反，现有的生成方法通常无法重建野外的详细、大规模场景，因为它们使用有限容量的3D场景表示，需要对齐的相机姿势，或者依赖于额外的正则化子。在这项工作中，我们介绍了第一个能够快速、详细地重建和生成真实世界3D场景的扩散模型。为了实现这一目标，我们作出了三点贡献。首先，我们引入了一种新的神经场景表示，即IB平面，它可以有效而准确地表示大型3D场景，并根据需要动态分配更多的容量来捕捉每个图像中可见的细节。其次，我们提出了一种去噪扩散框架来学习这种新颖的3D场景表示的先验知识，仅使用2D图像，而不需要任何额外的监督信号，如掩模或深度。这支持在统一架构中进行3D重建和生成。第三，我们开发了一种原则性方法，通过放弃一些图像的表示，在将基于图像的渲染与扩散模型集成时避免琐碎的3D解决方案。我们在真实图像和合成图像的几个具有挑战性的数据集上评估了该模型，并展示了在生成、新视图合成和3D重建方面的卓越结果。 et.al.|[2402.03445](http://arxiv.org/abs/2402.03445)|null|
|**2024-02-05**|**4D Gaussian Splatting: Towards Efficient Novel View Synthesis for Dynamic Scenes**|我们考虑动态场景的新视图合成（NVS）问题。最近的神经方法已经为静态3D场景实现了异常的NVS结果，但对4D时变场景的扩展仍然是不平凡的。先前的工作通常通过学习规范空间加上隐式或显式变形场来编码动力学，这些变形场在突发运动或捕捉高保真渲染等具有挑战性的场景中很困难。在本文中，我们介绍了4D高斯散射（4DGS），这是一种用各向异性4D XYZT高斯表示动态场景的新方法，其灵感来自于3D高斯散射在静态场景中的成功。我们通过对4D高斯进行时间切片来对每个时间戳的动力学进行建模，4D高斯自然构成动态3D高斯，并可以无缝投影到图像中。作为一种明确的时空表示，4DGS展示了对复杂动力学和精细细节建模的强大能力，尤其是对于具有突然运动的场景。我们在高度优化的CUDA加速框架中进一步实现了我们的时间切片和飞溅技术，在RTX 3090 GPU上实现了高达277 FPS的实时推理渲染速度，在RTX4090 GPU上达到了583 FPS的实时推断渲染速度。对不同运动场景的严格评估显示了4DGS的卓越效率和有效性，它在数量和质量上都始终优于现有方法。 et.al.|[2402.03307](http://arxiv.org/abs/2402.03307)|null|
|**2024-02-05**|**ViewFusion: Learning Composable Diffusion Models for Novel View Synthesis**|深度学习为新视图合成的老问题提供了丰富的新方法，从基于神经辐射场（NeRF）的方法到端到端风格的架构。每种方法都有特定的优势，但在适用性方面也有特定的局限性。这项工作介绍了ViewFusion，这是一种最先进的端到端生成新视图合成方法，具有无与伦比的灵活性。ViewFusion包括同时将扩散去噪步骤应用于场景的任意数量的输入视图，然后将为每个视图获得的噪声梯度与（推断的）像素加权掩码相结合，确保对于目标场景的每个区域，只考虑信息量最大的输入视图。我们的方法通过以下方式解决了以前方法的几个局限性：（1）可在多个场景和对象类中进行训练和推广，（2）在训练和测试时自适应地获取可变数量的无姿态视图，（3）即使在严重不确定的条件下也能生成合理的视图（由于其生成性）——同时生成质量与最先进方法不相上下甚至更好的视图。局限性包括没有生成场景的3D嵌入，导致推理速度相对较慢，并且我们的方法仅在相对较小的数据集NMR上进行测试。代码可用。 et.al.|[2402.02906](http://arxiv.org/abs/2402.02906)|**[link](https://github.com/bronemos/view-fusion)**|
|**2024-02-06**|**GaMeS: Mesh-Based Adapting and Modification of Gaussian Splatting**|近年来，已经引入了一系列基于神经网络的图像渲染方法。例如，广泛研究的神经辐射场（NeRF）依赖于神经网络来表示3D场景，从而允许从少量2D图像中合成逼真的视图。然而，大多数NeRF模型都受到长训练和推理时间的限制。相比之下，高斯散射（GS）是一种新颖的、最先进的技术，用于通过高斯分布近似点对图像像素的贡献来渲染3D场景中的点，从而保证快速训练和快速实时渲染。GS的一个缺点是，由于需要对几十万个高斯分量进行调节，因此缺乏定义明确的调节方法。为了解决这个问题，我们引入了高斯网格飞溅（GaMeS）模型，这是网格和高斯分布的混合，它将所有高斯飞溅物固定在物体表面（网格）上。我们的方法的独特贡献是仅根据高斯飞溅在网格上的位置来定义高斯飞溅，从而允许在动画过程中自动调整位置、比例和旋转。因此，我们在实时生成高质量视图的过程中获得了高质量的渲染图。此外，我们证明，在没有预定义网格的情况下，可以在学习过程中微调初始网格。 et.al.|[2402.01459](http://arxiv.org/abs/2402.01459)|**[link](https://github.com/waczjoan/gaussian-mesh-splatting)**|
|**2024-02-01**|**360-GS: Layout-guided Panoramic Gaussian Splatting For Indoor Roaming**|近年来，三维高斯散射（3D-GS）以其实时性和照片真实性的渲染引起了人们的极大关注。这项技术通常将透视图像作为输入，并通过将一组3D椭圆高斯分布到图像平面上来优化它们，从而产生2D高斯。然而，将3D-GS应用于全景输入在使用2D高斯有效地将投影建模到 ${360^\circ}$图像的球面上方面存在挑战。在实际应用中，输入全景图往往是稀疏的，导致3D高斯图的初始化不可靠，并导致3D-GS质量下降。此外，由于无纹理平面（例如，墙和地板）的几何约束不足，3D-GS难以用椭圆高斯对这些平坦区域进行建模，导致在新视图中出现显著的浮动。为了解决这些问题，我们提出了360-GS，这是一种针对有限的全景输入集的新的$360^{\circ}$ 高斯飞溅。360-GS不是将3D高斯直接泼洒到球面上，而是将其投影到单位球体的切平面上，然后将其映射到球面投影。这种自适应使得能够使用高斯表示投影。我们通过利用全景图中的布局先验来指导360-GS的优化，这些先验易于获得，并包含关于室内场景的强大结构信息。我们的实验结果表明，360-GS允许全景渲染，并在新的视图合成中以更少的伪影优于最先进的方法，从而在室内场景中提供身临其境的漫游。 et.al.|[2402.00763](http://arxiv.org/abs/2402.00763)|null|
|**2024-02-01**|**StopThePop: Sorted Gaussian Splatting for View-Consistent Real-time Rendering**|高斯散射已经成为从不同领域的图像构建3D表示的一个突出模型。然而，3D高斯飞溅渲染管道的效率依赖于几个简化。值得注意的是，使用单个视图空间深度将高斯飞溅减少到2D会在视图旋转过程中引入爆裂和混合伪影。解决这个问题需要精确的每像素深度计算，但与全局排序操作相比，完整的每像素排序成本过高。在本文中，我们提出了一种新的分层光栅化方法，该方法以最小的处理开销系统地处理和剔除飞溅。我们的软件光栅化器有效地消除了弹出的伪影和视图不一致，通过定量和定性测量都证明了这一点。同时，我们的方法通过弹出来减少欺骗视图相关效果的可能性，确保了更真实的表示。尽管消除了作弊，但我们的方法在测试图像中获得了可比的定量结果，同时提高了运动中新视图合成的一致性。由于其设计，我们的分层方法平均只比原始的高斯飞溅慢4%。值得注意的是，强制执行一致性可以将Gaussian的数量减少大约一半，同时具有几乎相同的质量和视图一致性。因此，渲染性能几乎翻了一番，使我们的方法比原始的高斯Splatting快1.6倍，同时减少了50%的内存需求。 et.al.|[2402.00525](http://arxiv.org/abs/2402.00525)|null|
|**2024-01-31**|**Advances in 3D Generation: A Survey**|生成三维模型是计算机图形学的核心，也是几十年来研究的焦点。随着先进的神经表示和生成模型的出现，3D内容生成领域正在迅速发展，能够创建越来越高质量和多样化的3D模型。这一领域的快速发展使得我们很难跟上最近的所有发展。在这项调查中，我们旨在介绍3D生成方法的基本方法，并建立一个结构化的路线图，包括3D表示、生成方法、数据集和相应的应用程序。具体来说，我们介绍了用作3D生成主干的3D表示。此外，我们全面概述了快速增长的生成方法文献，按算法范式的类型进行分类，包括前馈生成、基于优化的生成、过程生成和生成新视图合成。最后，我们讨论了可用的数据集、应用程序和开放的挑战。我们希望这项调查能帮助读者探索这个令人兴奋的话题，并促进3D内容生成领域的进一步发展。 et.al.|[2401.17807](http://arxiv.org/abs/2401.17807)|null|
|**2024-01-27**|**Gaussian Splashing: Dynamic Fluid Synthesis with Gaussian Splatting**|我们展示了将基于物理的固体和流体动画与3D高斯飞溅（3DGS）相结合的可行性，以在使用3DGS重建的虚拟场景中创建新的效果。利用底层表示中高斯飞溅和基于位置的动力学（PBD）的一致性，我们以内聚的方式管理渲染、视图合成以及固体和流体的动力学。与高斯着色器类似，我们使用添加的法线增强每个高斯内核，将内核的方向与曲面法线对齐，以优化PBD模拟。这种方法有效地消除了由固体中的旋转变形引起的尖锐噪声。它还允许我们集成基于物理的渲染，以增强流体上的动态曲面反射。因此，我们的框架能够真实地再现动态流体上的表面高光，并促进场景对象和新视图中流体之间的交互。有关更多信息，请访问我们的项目页面\url{https://amysteriouscat.github.io/GaussianSplashing/}. et.al.|[2401.15318](http://arxiv.org/abs/2401.15318)|null|

<p align=right>(<a href=#updated-on-20240207>back to top</a>)</p>

## 3D Reconstruction

|Publish Date|Title|Abstract|PDF|Code|
|---|---|---|---|---|
|**2024-02-06**|**EscherNet: A Generative Model for Scalable View Synthesis**|我们介绍了EscherNet，一个用于视图合成的多视图条件扩散模型。EscherNet学习隐含的和生成的3D表示，再加上专门的相机位置编码，允许对任意数量的参考视图和目标视图之间的相机变换进行精确和连续的相对控制。EscherNet在视图合成方面提供了非凡的通用性、灵活性和可扩展性——尽管它使用固定数量的3个参考视图到3个目标视图进行训练，但它可以在单个消费级GPU上同时生成100多个一致的目标视图。因此，EscherNet不仅解决了零样本新视图合成问题，而且自然地将单图像和多图像3D重建相结合，将这些不同的任务组合成一个单一的、有凝聚力的框架。我们的大量实验表明，即使与专门针对每个问题定制的方法相比，EscherNet也能在多个基准测试中实现最先进的性能。这种非凡的多功能性为设计用于3D视觉的可扩展神经结构开辟了新的方向。项目页面：\url{https://kxhit.github.io/EscherNet}. et.al.|[2402.03908](http://arxiv.org/abs/2402.03908)|null|
|**2024-02-06**|**Efficient Generation of Hidden Outliers for Improved Outlier Detection**|异常值生成是一种常用的技术，用于解决重要的异常值检测任务。生成具有现实行为的异常值具有挑战性。现有的流行方法往往忽略高维空间中异常值的“多视图”特性。对这一财产进行核算的唯一现有方法在效率和有效性方面不足。我们提出了BISECT，这是一种新的异常值生成方法，可以创建模拟上述属性的真实异常值。为此，BISECT采用了本文中介绍的一个新颖命题，说明如何有效地生成所述现实异常值。我们的方法比当前重建“多个视图”的方法有更好的保证和复杂性。我们使用BISECT生成的合成异常值来有效地增强不同数据集中的异常值检测，用于多种用例。例如，与基线相比，BISECT的过采样将误差减少了3倍。 et.al.|[2402.03846](http://arxiv.org/abs/2402.03846)|**[link](https://github.com/jcribeiro98/bisect)**|
|**2024-02-06**|**MoD-SLAM: Monocular Dense Mapping for Unbounded 3D Scene Reconstruction**|神经隐式表示最近已经在许多领域得到了证明，包括同时定位和映射（SLAM）。目前的神经SLAM在重建有界场景时可以获得理想的结果，但这依赖于RGB-D图像的输入。仅基于RGB图像的基于神经的SLAM无法准确地重建场景的尺度，而且由于跟踪过程中积累的误差，它还存在尺度漂移。为了克服这些限制，我们提出了MoD SLAM，这是一种单目密集映射方法，允许在无界场景中实时进行全局姿态优化和3D重建。通过单目深度估计优化场景重建，并使用闭环检测更新相机姿态，可以在大型场景上进行详细而精确的重建。与以前的工作相比，我们的方法更加健壮、可扩展和通用。我们的实验表明，与现有的神经SLAM方法相比，MoD-SLAM具有更出色的映射性能，尤其是在大型无边界场景中。 et.al.|[2402.03762](http://arxiv.org/abs/2402.03762)|null|
|**2024-02-05**|**Denoising Diffusion via Image-Based Rendering**|生成3D场景是一个具有挑战性的开放问题，需要合成在3D空间中完全一致的看似合理的内容。虽然最近的方法（如神经辐射场）擅长于视图合成和3D重建，但由于缺乏生成能力，它们无法在未观察到的区域合成看似合理的细节。相反，现有的生成方法通常无法重建野外的详细、大规模场景，因为它们使用有限容量的3D场景表示，需要对齐的相机姿势，或者依赖于额外的正则化子。在这项工作中，我们介绍了第一个能够快速、详细地重建和生成真实世界3D场景的扩散模型。为了实现这一目标，我们作出了三点贡献。首先，我们引入了一种新的神经场景表示，即IB平面，它可以有效而准确地表示大型3D场景，并根据需要动态分配更多的容量来捕捉每个图像中可见的细节。其次，我们提出了一种去噪扩散框架来学习这种新颖的3D场景表示的先验知识，仅使用2D图像，而不需要任何额外的监督信号，如掩模或深度。这支持在统一架构中进行3D重建和生成。第三，我们开发了一种原则性方法，通过放弃一些图像的表示，在将基于图像的渲染与扩散模型集成时避免琐碎的3D解决方案。我们在真实图像和合成图像的几个具有挑战性的数据集上评估了该模型，并展示了在生成、新视图合成和3D重建方面的卓越结果。 et.al.|[2402.03445](http://arxiv.org/abs/2402.03445)|null|
|**2024-02-02**|**Di-NeRF: Distributed NeRF for Collaborative Learning with Unknown Relative Poses**|未知环境的协作映射可以比单个机器人更快、更稳健地完成。然而，协作方法需要一个可扩展的分布式范式来处理通信问题。这项工作提出了一种全分布式算法，使一组机器人能够共同优化神经辐射场（NeRF）的参数。该算法涉及每个机器人训练的NeRF参数在网状网络上的通信，在网状网络中，每个机器人训练其NeRF，并且只能访问自己的视觉数据。此外，所有机器人的相对姿态都与模型参数一起进行了联合优化，从而能够使用未知的相对相机姿态进行映射。我们证明了多机器人系统可以受益于从多个NeRF优化的可微分和鲁棒的3D重建。在真实世界和合成数据上的实验证明了所提出的算法的有效性。实验视频和补充材料见项目网站(https://sites.google.com/view/di-nerf/home). et.al.|[2402.01485](http://arxiv.org/abs/2402.01485)|null|
|**2024-02-02**|**SiMA-Hand: Boosting 3D Hand-Mesh Reconstruction by Single-to-Multi-View Adaptation**|从RGB图像中估计3D手部网格是一个长期存在的问题，其中遮挡是最具挑战性的问题之一。当遮挡在图像空间中占主导地位时，针对该任务的现有尝试往往失败。在本文中，我们提出了SiMA Hand，旨在通过单视图到多视图自适应来提高网格重建性能。首先，我们设计了一个多视图手动重建器，通过在图像、关节和顶点级别全面采用特征融合来融合多个视图之间的信息。然后，我们介绍了一种配备SiMA的单视图手动重建器。尽管在推理时仅将一个视图作为输入，但通过在训练时从额外的视图中学习非遮挡知识，可以丰富单个视图重构器中的形状和方向特征，提高遮挡区域的重构精度。我们在Dex-YCB和HanCo基准上对具有挑战性的物体和自身造成的遮挡情况进行了实验，表明SiMA Hand始终实现了优于现有技术的性能。代码将于发布https://github.com/JoyboyWang/SiMA-HandPytorch。 et.al.|[2402.01389](http://arxiv.org/abs/2402.01389)|**[link](https://github.com/JoyboyWang/SiMA-Hand_Pytorch)**|
|**2024-02-02**|**DeepAAT: Deep Automated Aerial Triangulation for Fast UAV-based Mapping**|自动空中三角测量（AAT）旨在恢复图像姿态和重建稀疏点，在对地观测中发挥着关键作用。AAT在摄影测量领域拥有数十年的丰富研究遗产，已发展成为一个广泛应用于大规模无人机测绘的基础过程。尽管取得了进步，但经典的AAT方法仍然面临着效率低和稳健性有限等挑战。本文介绍了DeepAAT，一个专门为无人机图像AAT设计的深度学习网络。DeepAAT考虑了图像的空间和光谱特征，增强了其解决错误匹配对和准确预测图像姿态的能力。DeepAAT标志着AAT效率的重大飞跃，确保了全面的场景覆盖和精度。其处理速度超过增量AAT方法数百倍，超过全局AAT方法数十倍，同时保持了相当水平的重建精度。此外，DeepAAT的场景聚类和合并策略有助于大规模无人机图像的快速定位和姿态确定，即使在计算资源有限的情况下也是如此。实验结果表明，DeepAAT比传统的AAT方法有了实质性的改进，突出了其在基于无人机的三维重建任务的效率和准确性方面的潜力。为了造福摄影测量学会，DeepAAT的代码将发布在：https://github.com/WHU-USI3DV/DeepAAT. et.al.|[2402.01134](http://arxiv.org/abs/2402.01134)|**[link](https://github.com/whu-usi3dv/deepaat)**|
|**2024-02-02**|**Learning Which Side to Scan: Multi-View Informed Active Perception with Side Scan Sonar for Autonomous Underwater Vehicles**|自动水下航行器通常执行捕获目标的多个视图的勘测，以便为人类操作员或自动目标识别算法提供更多信息。在这项工作中，我们解决了选择信息量最大的视图的问题，这些视图可以最大限度地减少调查时间，同时最大限度地提高分类器的准确性。我们介绍了一种新的主动感知框架，用于使用侧扫声纳图像进行多视图自适应测量和重新获取。我们的框架通过使用自适应调查任务的图形公式来应对这一挑战。然后，我们使用图神经网络（GNN）对获取的声纳视图进行分类，并根据收集的数据选择下一个最佳视图。我们使用高保真侧扫声纳模拟器中的模拟调查来评估我们的方法。我们的结果表明，我们的方法能够在分类精度和调查效率方面超越最先进的方法。该框架是一种很有前途的方法，可用于更高效的自主任务，包括侧扫声纳，如水下勘探、海洋考古和环境监测。 et.al.|[2402.01106](http://arxiv.org/abs/2402.01106)|null|
|**2024-02-01**|**Enhanced fringe-to-phase framework using deep learning**|在边缘投影轮廓术（FPP）中，用有限数量的边缘图案实现稳健和准确的3D重建仍然是结构光3D成像中的一个挑战。传统的方法需要一组条纹图像，但仅使用一个或两个图案会使相位恢复和展开变得复杂。在这项研究中，我们介绍了SFNet，一种将两个条纹图像转换为绝对相位的对称融合网络。为了提高输出可靠性，我们的框架通过结合来自与用作输入的频率不同的条纹图像的信息来预测精细相位。这使我们能够仅用两个图像实现高精度。对比实验和消融研究验证了我们提出的方法的有效性。数据集和代码可在我们的项目页面上公开访问https://wonhoe-kim.github.io/SFNet. et.al.|[2402.00977](http://arxiv.org/abs/2402.00977)|null|
|**2024-02-01**|**Diffusion-based Light Field Synthesis**|光场（LFs）有助于在角度维度上记录全面的场景辐射，在3D重建、虚拟现实和计算摄影中有着广泛的应用。然而，由于主流的采集策略涉及手动采集或费力的软件合成，LF采集不可避免地耗时且资源密集。鉴于这一挑战，我们引入了LFdiff，这是一种简单而有效的基于扩散的生成框架，专门用于LF合成，它只采用单个RGB图像作为输入。LFdiff利用单目深度估计网络估计的视差，并结合了两个独特的组件：一个新的条件方案和一个为LF数据量身定制的噪声估计网络。具体来说，我们设计了一种位置感知扭曲条件方案，通过鲁棒的条件信号增强视图间几何学习。然后，我们提出了DistgUnet，一种基于解纠缠的噪声估计网络，以利用综合的LF表示。大量实验表明，LFdiff在合成视觉愉悦和视差可控的光场方面表现出色，具有增强的泛化能力。此外，综合结果证实了生成的LF数据的广泛适用性，涵盖了LF超分辨率和重新聚焦等应用。 et.al.|[2402.00575](http://arxiv.org/abs/2402.00575)|null|

<p align=right>(<a href=#updated-on-20240207>back to top</a>)</p>

## Diffusion

|Publish Date|Title|Abstract|PDF|Code|
|---|---|---|---|---|
|**2024-02-06**|**Geometric theory of (extended) time-reversal symmetries in stochastic processes -- Part I: finite dimension**|在本文中，我们分析了流形上具有高斯噪声的马尔可夫过程的三类时间反转。我们首先揭示了一个交换性约束，使这些时间反转中最普遍的是被很好地定义的。然后我们给出了随机过程时间可逆的一组充要条件。虽然文献中的大多数可逆性条件都需要平稳概率的知识，但我们的条件不需要，因此可以用系统的方式进行分析检查。然后，我们证明了可逆性条件要求其抵消的数学对象扮演着熵产生的独立来源的角色。此外，我们给出了所谓的不可逆循环亲和性的几何解释，即由扩散张量给出的黎曼几何的某个向量场的涡度。我们还讨论了随机过程的时间可逆性和相关的确定动力学的时间可逆度之间的关系：Stratonovitch平均值。最后，我们证明了参考测度的适当选择——根据上下文，可以被视为先验测度或规范——允许以一种无坐标且独立于用于定义随机积分的处方的方式研究随机过程。当这个参考测度扮演规范选择的角色时，我们通过规范理论的视角来解释我们之前的结果，并证明它们是规范不变的。 et.al.|[2402.04217](http://arxiv.org/abs/2402.04217)|null|
|**2024-02-06**|**Maximal regularity and optimal control for a non-local Cahn-Hilliard tumour growth model**|我们考虑了一个相场型的非局部肿瘤生长模型，描述了肿瘤细胞在营养物质存在下通过增殖的进化。该模型由一个耦合系统组成，结合了肿瘤时相变量的非局部Cahn-Hilliard方程和营养物的反应-扩散方程。通过具有适当空间核的卷积算子来包括非局部细胞间粘附效应。首先，我们通过在加权 $L^p$ 空间中应用极大正则性理论，为这种模型建立了新的正则性结果。这种技术使我们能够在一个相当普遍的框架中证明正则解的局部存在性和唯一性，其中也包括趋化性效应。然后，通过利用加权空间的时间正则化性质和全局有界性估计，我们在一些额外的假设下，将解进一步扩展到全局解。这些结果为解决最优分布式控制问题提供了基础，该问题旨在确定能够引导肿瘤向预定目标进化的合适疗法。具体地说，我们证明了最优治疗的存在性，然后通过研究控制对状态算子的Fr’chet-differentiability并引入伴随系统，我们得到了一阶必要的最优性条件。 et.al.|[2402.04204](http://arxiv.org/abs/2402.04204)|null|
|**2024-02-06**|**SHIELD : An Evaluation Benchmark for Face Spoofing and Forgery Detection with Multimodal Large Language Models**|基于强大的视觉语义表示和语言推理能力，多模式大语言模型（MLLMs）在各种视觉领域（如通用对象识别和基础）表现出了显著的解决问题的能力。然而，MLLMs是否对细微的视觉欺骗/伪造线索敏感，以及它们在人脸攻击检测领域（例如，人脸欺骗和伪造检测）中的表现仍有待探索。在本文中，我们引入了一个新的基准，即SHIELD，来评估MLLMs在人脸欺骗和伪造检测方面的能力。具体来说，我们设计了真/假和多项选择题来评估这两项人脸安全任务中的多模式人脸数据。对于人脸反欺骗任务，我们在四种类型的呈现攻击（即打印攻击、重放攻击、刚性掩模、纸掩模）下评估了三种不同的模式（即RGB、红外、深度）。对于人脸伪造检测任务，我们使用视觉和声学模式评估基于GAN和基于扩散的数据。每个问题都要在标准和思想链（COT）设置下进行零样本和少数热点测试。结果表明，MLLMs在人脸安全领域具有巨大的潜力，在可解释性、多模式灵活推理以及联合人脸欺骗和伪造检测方面比传统的特定模型具有优势。此外，我们开发了一种新的多属性思想链（MA-COT）范式，用于描述和判断人脸图像的各种任务特定和任务无关属性，为微妙的欺骗/伪造线索挖掘提供了丰富的任务相关知识。在单独的人脸反欺骗、单独的人脸伪造检测和联合检测任务中进行的大量实验证明了所提出的MA-COT的有效性。该项目可在https://github.com/laiyingxin2/SHIELD上获得 et.al.|[2402.04178](http://arxiv.org/abs/2402.04178)|**[link](https://github.com/laiyingxin2/shield)**|
|**2024-02-06**|**Entropy-regularized Diffusion Policy with Q-Ensembles for Offline Reinforcement Learning**|本文提出了用于离线强化学习（RL）的训练扩散策略的先进技术。其核心是一个均值回归随机微分方程（SDE），它将复杂的动作分布转换为标准高斯分布，然后用相应的反向时间SDE对环境状态下的动作进行采样，就像典型的扩散策略一样。我们证明，这样的SDE有一个解决方案，我们可以用来计算策略的对数概率，从而产生一个熵正则化子，改进离线数据集的探索。为了减轻分布外数据点的不准确值函数的影响，我们进一步建议学习Q集合的置信下限，以获得更稳健的策略改进。通过将熵正则化扩散策略与离线RL中的Q集合相结合，我们的方法在D4RL基准测试中的大多数任务上都实现了最先进的性能。代码位于\ href{https://github.com/ruoqizzz/Entropy-Regularized-Diffusion-Policy-with-QEnsemble}{https://github.com/ruoqizzz/Entropy-Regularized-Diffusion-Policy-with-QEnsemble}. et.al.|[2402.04080](http://arxiv.org/abs/2402.04080)|null|
|**2024-02-06**|**Generative Modeling of Graphs via Joint Diffusion of Node and Edge Attributes**|图形生成是各种工程和科学学科不可或缺的一部分。然而，现有的方法往往忽略了边缘属性的生成。然而，我们确定了边缘属性至关重要的关键应用程序，这使得先前的方法在这种情况下可能不合适。此外，虽然可以进行琐碎的调整，但实证研究揭示了它们的有限功效，因为它们没有正确地对图组件之间的相互作用进行建模。为了解决这一问题，我们提出了一种用于图生成的基于节点和边的联合评分模型，该模型考虑了所有图组件。我们的方法提供了两个关键的新颖之处：（i）节点和边缘属性组合在一个注意力模块中，该模块基于这两种成分生成样本；以及（ii）节点、边和邻接信息在图扩散过程中是相互依赖的。我们在涉及真实世界和合成数据集的具有挑战性的基准上评估我们的方法，其中边缘特征至关重要。此外，我们还引入了一个新的合成数据集，该数据集包含边缘值。此外，我们提出了一种新的应用程序，由于该方法的性质，它极大地受益于该方法：生成以图表示的交通场景。我们的方法优于其他图生成方法，证明了在边缘相关度量方面的显著优势。 et.al.|[2402.04046](http://arxiv.org/abs/2402.04046)|null|
|**2024-02-06**|**PAC-Bayesian Adversarially Robust Generalization Bounds for Graph Neural Network**|图神经网络（GNN）在各种与图相关的任务中越来越受欢迎。然而，与深度神经网络类似，GNN也容易受到对抗性攻击。实证研究表明，对抗性鲁棒泛化在建立有效的对抗性攻击防御算法方面发挥着关键作用。在本文中，我们使用PAC贝叶斯框架，为两种流行的GNN，即图卷积网络（GCN）和消息传递图神经网络，提供了对抗性鲁棒泛化边界。我们的结果表明，图上扩散矩阵的谱范数、权重的谱范数以及扰动因子决定了这两个模型的鲁棒推广界。我们的边界是（Liao et al.，2020）中从标准设置到对抗性设置的结果的非平凡推广，同时避免了最大节点度的指数依赖性。作为推论，我们在标准设置中推导了GCN更好的PAC贝叶斯鲁棒泛化边界，通过避免对最大节点度的指数依赖性，改进了（Liao et al.，2020）中的边界。 et.al.|[2402.04038](http://arxiv.org/abs/2402.04038)|null|
|**2024-02-06**|**Polyp-DDPM: Diffusion-Based Semantic Polyp Synthesis for Enhanced Segmentation**|本研究介绍了Polyp-DDPM，这是一种基于扩散的方法，用于在口罩上生成真实的息肉图像，旨在增强胃肠道息肉的分割。我们的方法解决了与医学图像相关的数据限制、高注释成本和隐私问题等挑战。通过将扩散模型调节在分割掩模上，表示异常区域的二进制掩模Polyp DDPM在图像质量（与83.79以上的分数相比实现78.47的Frechet Inception Distance（FID）分数）和分割性能（实现0.7156的交集（IoU），而对于来自基线模型的合成图像小于0.6694，对于真实数据小于0.7067）。我们的方法生成高质量、多样化的合成数据集进行训练，从而增强息肉分割模型，使其与真实图像相媲美，并提供更大的数据增强能力来改进分割模型。Polyp DDPM的源代码和预训练权重可在https://github.com/mobaidoctor/polyp-ddpm. et.al.|[2402.04031](http://arxiv.org/abs/2402.04031)|**[link](https://github.com/mobaidoctor/polyp-ddpm)**|
|**2024-02-06**|**Space Group Constrained Crystal Generation**|晶体是许多科学和工业应用的基础。虽然已经提出了各种基于学习的方法来生成晶体，但现有的方法很少考虑空间群约束，这对描述晶体的几何形状至关重要，并且与许多期望的性质密切相关。然而，考虑空间群约束由于其多样性和非平凡性而具有挑战性。在本文中，我们将空间群约束简化为一个等价的公式，该公式更易于手工制作到生成过程中。特别地，我们将空间群约束转化为两部分：格矩阵的不变对数空间的基约束和分数坐标的Wyckoff位置约束。根据推导出的约束，我们提出了DiffCSP++，这是一种新的扩散模型，通过进一步考虑空间群约束，增强了先前的工作DiffCSP。在几个流行数据集上的实验验证了空间群约束的好处，并表明我们的DiffCSP++在晶体结构预测、从头计算晶体生成和自定义空间群的可控生成方面取得了很好的性能。 et.al.|[2402.03992](http://arxiv.org/abs/2402.03992)|null|
|**2024-02-06**|**Controllable Diverse Sampling for Diffusion Based Motion Behavior Forecasting**|在自动驾驶任务中，复杂交通环境中的轨迹预测需要遵守现实世界的上下文条件和行为多模式。现有的方法主要依赖于先前的假设或在策划的数据上训练的生成模型来学习受场景约束的道路代理的随机行为。然而，由于数据不平衡和先验过于简单，他们经常面临模式平均问题，甚至可能由于不稳定的训练和单一事实监督而导致模式崩溃。这些问题导致现有方法失去了预测多样性和对场景约束的遵守。为了应对这些挑战，我们引入了一种名为可控扩散轨迹（CDT）的新型轨迹生成器，该生成器将地图信息和社会互动集成到基于Transformer的条件去噪扩散模型中，以指导未来轨迹的预测。为了确保多模式，我们结合了行为标记来指导轨迹的模式，如直行、右转或左转。此外，我们将预测的终点作为替代行为标记纳入CDT模型，以促进准确轨迹的预测。在Argoverse 2基准上进行的大量实验表明，CDT擅长在复杂的城市环境中生成多样化且符合场景的轨迹。 et.al.|[2402.03981](http://arxiv.org/abs/2402.03981)|null|
|**2024-02-06**|**Weibel- and non-resonant Whistler wave growth in an expanding plasma in a 1D simulation geometry**|用超强激光脉冲烧蚀目标可以产生无碰撞等离子体云。密度斜坡形成，其中等离子体密度随着离等离子体源的距离而降低，离子的平均速度随着距离的增加而增加。它的宽度随着时间的推移而增加。电子在离子的膨胀方向上失去能量，这使它们具有温度各向异性。我们用一维细胞内粒子模拟研究了致密等离子体向稀等离子体的膨胀，产生了与激光等离子体实验中类似的密度斜坡和热各向异性驱动的不稳定性。在没有初始磁场的模拟中，非传播Weibel型模式增长。它们的磁场在冲击中扩散并向上游扩展。圆偏振传播的Whistler波在第二个模拟中生长，其中磁场与离子膨胀方向对齐。两种波模式都是由非共振不稳定性驱动的，它们具有相似的指数增长率，并且它们可以离开密度斜坡并扩展到稀释等离子体中。它们的大磁幅应该能使它们在实验环境中被检测到。 et.al.|[2402.03925](http://arxiv.org/abs/2402.03925)|null|

<p align=right>(<a href=#updated-on-20240207>back to top</a>)</p>

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

<p align=right>(<a href=#updated-on-20240207>back to top</a>)</p>

[contributors-shield]: https://img.shields.io/github/contributors/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[contributors-url]: https://github.com/Vincentqyw/cv-arxiv-daily/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[forks-url]: https://github.com/Vincentqyw/cv-arxiv-daily/network/members
[stars-shield]: https://img.shields.io/github/stars/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[stars-url]: https://github.com/Vincentqyw/cv-arxiv-daily/stargazers
[issues-shield]: https://img.shields.io/github/issues/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[issues-url]: https://github.com/Vincentqyw/cv-arxiv-daily/issues

