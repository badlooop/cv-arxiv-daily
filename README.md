[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]

## Updated on 2024.03.14
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
|**2024-03-12**|**Q-SLAM: Quadric Representations for Monocular SLAM**|Monocular SLAM长期以来一直在努力应对准确建模3D几何图形的挑战。基于神经辐射场（NeRF）的单目SLAM的最新进展显示出了前景，但这些方法通常侧重于新颖的视图合成，而不是精确的3D几何建模。这种关注导致NeRF应用（即新的视图合成）与SLAM的要求之间的显著脱节。我们发现，间隙是由NeRF中使用的体积表示产生的，这些表示通常是密集的和有噪声的。在这项研究中，我们提出了一种新的方法，通过二次曲面的透镜重新想象体积表示。我们假设大多数场景组件可以有效地表示为二次平面。利用这一假设，我们通过几个二次平面用数百万个立方体重塑体积表示，这导致在SLAM环境中对3D场景进行更准确和高效的建模。我们的方法包括两个关键步骤：首先，我们使用二次假设来增强从跟踪模块（例如Droid SLAM）获得的粗略深度估计。仅此步骤就显著提高了深度估计的准确性。其次，在随后的映射阶段，我们偏离了以前基于NeRF的SLAM方法，该方法在整个体积空间中分布采样点。相反，我们将采样点集中在二次平面周围，并使用一种新的二次分解变换器对它们进行聚合。此外，我们还介绍了一种端到端的联合优化策略，该策略将姿态估计与三维重建同步。 et.al.|[2403.08125](http://arxiv.org/abs/2403.08125)|null|
|**2024-03-12**|**Learning Generalizable Feature Fields for Mobile Manipulation**|移动操作中的一个悬而未决的问题是如何以统一的方式表示对象和场景，以便机器人既可以在环境中导航，也可以操作对象。后者需要在理解细粒度语义的同时捕获复杂的几何体，而前者则需要捕获继承到扩展物理规模的复杂性。在这项工作中，我们提出了GeFF（可泛化特征场），这是一个场景级的可泛化神经特征场，作为实时执行的导航和操纵的统一表示。为此，我们将生成新视图合成视为预训练任务，然后通过CLIP特征提取将生成的丰富场景先验与自然语言对齐。我们通过在配备机械手的四足机器人上部署GeFF来证明这种方法的有效性。当在动态场景中执行开放词汇移动操作时，我们评估了GeFF泛化到开放集对象的能力以及运行时间。 et.al.|[2403.07563](http://arxiv.org/abs/2403.07563)|null|
|**2024-03-13**|**DNGaussian: Optimizing Sparse-View 3D Gaussian Radiance Fields with Global-Local Depth Normalization**|辐射场在从稀疏输入视图合成新视图方面表现出了令人印象深刻的性能，但主流方法的训练成本高，推理速度慢。本文介绍了DNGaussian，一种基于三维高斯辐射场的深度正则化框架，以低成本提供实时、高质量的少镜头新视图合成。我们的动机源于最近的3D高斯飞溅的高效表示和令人惊讶的质量，尽管当输入视图减少时，它会遇到几何退化。在高斯辐射场中，我们发现场景几何的这种退化主要与高斯基元的定位有关，并且可以通过深度约束来缓解。因此，我们提出了一种硬深度和软深度正则化，以在粗略的单目深度监督下恢复准确的场景几何体，同时保持细粒度的颜色外观。为了进一步细化详细的几何体重塑，我们引入了全局局部深度归一化，增强了对局部深度小变化的关注。在LLFF、DTU和Blender数据集上进行的大量实验表明，DNGaussian优于最先进的方法，实现了相当或更好的结果，显著降低了内存成本，减少了25美元的训练时间，渲染速度快了3000美元以上。 et.al.|[2403.06912](http://arxiv.org/abs/2403.06912)|**[link](https://github.com/fictionarry/dngaussian)**|
|**2024-03-11**|**FreGS: 3D Gaussian Splatting with Progressive Frequency Regularization**|三维高斯泼溅在实时新颖视图合成中取得了令人印象深刻的性能。然而，在高斯致密化过程中，它经常遭受过度重建，其中高方差图像区域仅被几个大高斯覆盖，导致渲染图像中的模糊和伪影。我们设计了一种渐进频率正则化（FreGS）技术来解决频率空间内的过重构问题。具体而言，FreGS通过利用傅立叶空间中的低通和高通滤波器可以容易地提取的低频到高频分量来执行从粗到细的高斯致密化。通过最小化渲染图像的频谱与相应的地面实况之间的差异，它实现了高质量的高斯致密化，并有效地缓解了高斯飞溅的过度重建。在多个广泛采用的基准上进行的实验（例如，Mip-NeRF360、Tanks and Temples和Deep Blending）表明，FreGS实现了卓越的新型视图合成，并始终优于最先进的视图合成。 et.al.|[2403.06908](http://arxiv.org/abs/2403.06908)|null|
|**2024-03-11**|**V3D: Video Diffusion Models are Effective 3D Generators**|3D自动生成最近引起了广泛关注。最近的方法大大加快了生成速度，但由于模型容量或3D数据有限，通常会生成不太详细的对象。受视频扩散模型最新进展的启发，我们引入了V3D，它利用预先训练的视频扩散模型的世界模拟能力来促进3D生成。为了充分释放视频扩散感知3D世界的潜力，我们进一步引入了几何一致性先验，并将视频扩散模型扩展到多视图一致的3D生成器中。得益于此，可以对最先进的视频扩散模型进行微调，以在给定单个图像的情况下生成围绕对象的360度轨道帧。通过我们量身定制的重建管道，我们可以在3分钟内生成高质量的网格或3D高斯。此外，我们的方法可以扩展到场景级的新视图合成，实现对稀疏输入视图的相机路径的精确控制。大量实验证明了该方法的优越性能，特别是在生成质量和多视图一致性方面。我们的代码可在https://github.com/heheyas/V3D et.al.|[2403.06738](http://arxiv.org/abs/2403.06738)|**[link](https://github.com/heheyas/v3d)**|
|**2024-03-11**|**Vosh: Voxel-Mesh Hybrid Representation for Real-Time View Synthesis**|神经辐射场（NeRF）已成为合成新颖视图的逼真图像的一种突出方法。虽然基于体素或网格的神经辐射表示分别提供了不同的优势，在渲染质量或速度方面都很出色，但每种方法在其他方面都有局限性。作为回应，我们提出了一种名为Vosh的开创性混合表示，在用于视图合成的混合渲染中无缝组合体素和网格组件。Vosh是通过优化NeRF的体素网格精心制作的，战略性地将选定的体素替换为网格。因此，它擅长通过网格组件快速渲染具有简单几何体和纹理的场景，同时通过利用体素组件在复杂区域实现高质量渲染。Vosh的灵活性通过调整混合比率的能力得到了展示，为用户提供了基于灵活使用控制渲染质量和速度之间平衡的能力。实验结果表明，我们的方法在渲染质量和速度之间实现了值得称赞的折衷，并且在移动设备上具有显著的实时性能。 et.al.|[2403.06505](http://arxiv.org/abs/2403.06505)|null|
|**2024-03-13**|**FSViewFusion: Few-Shots View Generation of Novel Objects**|自从NeRF出现以来，新颖的视图合成已经得到了巨大的发展。然而，Nerf模型在单个场景上过拟合，缺乏对分布外对象的泛化能力。最近，扩散模型在视图合成中引入泛化方面表现出了显著的性能。受这些进步的启发，我们探索了预训练的稳定扩散模型在没有显式3D先验的情况下进行视图合成的能力。具体来说，我们的方法基于个性化的文本到图像模型Dreambooth，因为它具有很强的能力，只需几次拍摄就可以适应特定的新颖对象。我们的研究揭示了两个有趣的发现。首先，我们观察到，与涉及对大量多视图数据进行微调扩散的更复杂的策略相比，Dreambooth可以学习视图的高级概念。其次，我们建立了一个观点的概念可以被解开并转移到一个新的对象上，而不考虑从中学习观点的原始对象的身份。受此启发，我们引入了一种学习策略FSViewFusion，该策略仅通过单个场景的一个图像样本继承特定视图，并使用低阶适配器将知识转移到从少数镜头中学习的新对象。通过广泛的实验，我们证明了我们的方法虽然简单，但在为野生图像生成可靠的视图样本方面是有效的。将发布代码和模型。 et.al.|[2403.06394](http://arxiv.org/abs/2403.06394)|null|
|**2024-03-13**|**S-DyRF: Reference-Based Stylized Radiance Fields for Dynamic Scenes**|目前的3D风格化方法往往假设场景是静态的，这违背了我们现实世界的动态本质。为了解决这一限制，我们提出了S-DyRF，这是一种基于参考的动态神经辐射场时空风格化方法。然而，由于沿时间轴的风格化参考图像的可用性有限，风格化动态3D场景本质上是具有挑战性的。我们的关键见解在于除了提供的参考之外，还引入了额外的时间线索。为此，我们从给定的程式化引用中生成时间伪引用。这些伪参考便于样式信息从参考传播到整个动态3D场景。对于粗略的样式转换，我们强制使用新颖的视图和时间，以在特征级别模拟伪引用中存在的样式细节。为了保留高频细节，我们从时间伪参考创建了一个风格化的时间伪射线集合。这些伪射线作为实现精细风格转换的详细和明确的风格化指导。在合成数据集和真实世界数据集上的实验表明，我们的方法在动态3D场景上产生了合理的时空视图合成风格化结果。 et.al.|[2403.06205](http://arxiv.org/abs/2403.06205)|null|
|**2024-03-10**|**Is Vanilla MLP in Neural Radiance Field Enough for Few-shot View Synthesis?**|神经辐射场（NeRF）通过使用多层感知（MLP）和体绘制程序对场景进行建模，在新的视图合成中实现了卓越的性能，然而，当给定的已知视图较少时（即，很少的镜头视图合成），模型容易过拟合给定的视图。为了解决这个问题，以前的努力是利用学习到的先验知识或引入额外的正则化。相反，在本文中，我们首次从网络结构的角度提供了一种正交方法。考虑到微不足道地减少模型参数的数量可以缓解过拟合问题，但以丢失细节为代价，我们提出了多输入MLP（mi-MLP），它将普通MLP的输入（即位置和观看方向）合并到每一层中，以防止过拟合问题而不损害详细合成。为了进一步减少伪影，我们建议分别对颜色和体积密度进行建模，并提出两个正则化项。在多个数据集上的大量实验表明：1）尽管所提出的mi MLP易于实现，但它的有效性令人惊讶，因为它将基线的PSNR从14.73美元提高到24.23美元。2） 总体框架在广泛的基准上取得了最先进的成果。我们将在发布后发布代码。 et.al.|[2403.06092](http://arxiv.org/abs/2403.06092)|null|
|**2024-03-09**|**Lightning NeRF: Efficient Hybrid Scene Representation for Autonomous Driving**|最近的研究强调了NeRF在自动驾驶环境中的应用前景。然而，室外环境的复杂性，加上驾驶场景中的视点受限，使精确重建场景几何体的任务变得复杂。这些挑战往往会导致重建质量下降，训练和渲染的持续时间延长。为了应对这些挑战，我们推出了Lightning NeRF。它使用了一种高效的混合场景表示，在自动驾驶场景中有效地利用了激光雷达的几何先验。Lightning NeRF显著提高了NeRF的新颖视图合成性能，并减少了计算开销。通过对真实世界数据集（如KITTI-360、Argoverse2和我们的私人数据集）的评估，我们证明了我们的方法不仅在新视图合成质量方面超过了当前最先进的技术，而且在训练速度上提高了五倍，在渲染速度上也提高了十倍。代码可在https://github.com/VISION-SJTU/Lightning-NeRF . et.al.|[2403.05907](http://arxiv.org/abs/2403.05907)|**[link](https://github.com/vision-sjtu/lightning-nerf)**|

<p align=right>(<a href=#updated-on-20240314>back to top</a>)</p>

## 3D Reconstruction

|Publish Date|Title|Abstract|PDF|Code|
|---|---|---|---|---|
|**2024-03-13**|**3DFIRES: Few Image 3D REconstruction for Scenes with Hidden Surface**|本文介绍了一种新的基于姿态图像的场景级三维重建系统3DFIRES。3DFIRES的设计只适用于一个视图，它重建了看不见的场景的完整几何体，包括隐藏的表面。使用多个视图输入，我们的方法可以在所有相机截头体内进行完全重建。我们的方法的一个关键特征是在特征级别融合多视图信息，从而实现连贯和全面的3D重建。我们在大规模真实场景数据集的非水密扫描上训练我们的系统。我们表明，它与仅使用一个输入的单视图重建方法的效果相匹配，并且在稀疏视图3D重建的定量和定性测量方面都超过了现有技术。 et.al.|[2403.08768](http://arxiv.org/abs/2403.08768)|null|
|**2024-03-13**|**Refractive COLMAP: Refractive Structure-from-Motion Revisited**|在本文中，我们提出了一个完整的折射运动结构（RSfM）框架，用于使用折射相机设置（用于平端口和圆顶端口水下外壳）进行水下3D重建。尽管在过去十年中在折射多视图几何方面取得了显著成就，但目前还没有一个强大、完整和公开的解决方案来解决这类任务，而且实际应用往往不得不通过针孔相机模型的固有（失真）参数来近似折射效应。为了填补这一空白，我们在最先进的开源SfM框架COLMAP中，在整个SfM过程中集成了折射考虑因素。对具有地面实况的合成生成但照片逼真的图像进行的数值模拟和重建结果验证了与空中重建相比，启用折射不会损害准确性或稳健性。最后，我们使用由近6000张图像组成的数据集展示了我们的方法在大规模折射场景中的能力。该实现以开源形式发布于：https://cau-git.rz.uni-kiel.de/inf-ag-koeser/colmap_underwater. et.al.|[2403.08640](http://arxiv.org/abs/2403.08640)|null|
|**2024-03-12**|**Q-SLAM: Quadric Representations for Monocular SLAM**|Monocular SLAM长期以来一直在努力应对准确建模3D几何图形的挑战。基于神经辐射场（NeRF）的单目SLAM的最新进展显示出了前景，但这些方法通常侧重于新颖的视图合成，而不是精确的3D几何建模。这种关注导致NeRF应用（即新的视图合成）与SLAM的要求之间的显著脱节。我们发现，间隙是由NeRF中使用的体积表示产生的，这些表示通常是密集的和有噪声的。在这项研究中，我们提出了一种新的方法，通过二次曲面的透镜重新想象体积表示。我们假设大多数场景组件可以有效地表示为二次平面。利用这一假设，我们通过几个二次平面用数百万个立方体重塑体积表示，这导致在SLAM环境中对3D场景进行更准确和高效的建模。我们的方法包括两个关键步骤：首先，我们使用二次假设来增强从跟踪模块（例如Droid SLAM）获得的粗略深度估计。仅此步骤就显著提高了深度估计的准确性。其次，在随后的映射阶段，我们偏离了以前基于NeRF的SLAM方法，该方法在整个体积空间中分布采样点。相反，我们将采样点集中在二次平面周围，并使用一种新的二次分解变换器对它们进行聚合。此外，我们还介绍了一种端到端的联合优化策略，该策略将姿态估计与三维重建同步。 et.al.|[2403.08125](http://arxiv.org/abs/2403.08125)|null|
|**2024-03-11**|**Bayesian Diffusion Models for 3D Shape Reconstruction**|我们提出了贝叶斯扩散模型（BDM），这是一种通过联合扩散过程将自上而下（先验）的信息与自下而上（数据驱动）的过程紧密耦合来执行有效贝叶斯推理的预测算法。我们展示了BDM在三维形状重建任务中的有效性。与在配对（监督）数据标签（如图像点云）数据集上训练的原型深度学习数据驱动方法相比，我们的BDM从独立标签（如点云）中引入了丰富的先验信息，以改进自下而上的3D重建。与推理需要显式先验和似然的标准贝叶斯框架不同，BDM通过与学习的梯度计算网络的耦合扩散过程来执行无缝信息融合。我们BDM的特点在于它能够参与自上而下和自下而上的过程的积极有效的信息交换和融合，其中每个过程本身就是一个扩散过程。我们在3D形状重建的合成基准和真实世界基准上展示了最先进的结果。 et.al.|[2403.06973](http://arxiv.org/abs/2403.06973)|null|
|**2024-03-08**|**DITTO: Dual and Integrated Latent Topologies for Implicit 3D Reconstruction**|我们提出了一种新的对偶和集成潜在拓扑（简称DITTO）概念，用于从噪声和稀疏点云中进行隐式三维重建。大多数现有的方法主要关注单个潜在类型，如点或网格潜在。相反，所提出的DITTO利用点和网格潜伏时间（即双重潜伏时间）来增强它们的强度、网格潜伏时间的稳定性和点潜伏时间的细节丰富能力。DITTO由双隐式编码器和集成隐式解码器组成。在双潜伏编码器中，双潜伏层是构成编码器的关键模块块，它并行地细化两个潜伏，保持它们不同的形状，并实现递归交互。值得注意的是，新提出的双潜伏层内的动态稀疏点变换器有效地细化了点潜伏。然后，集成隐式解码器系统地结合了这些精细的延迟，实现了高保真度的3D重建，并在对象和场景级数据集上超越了以前最先进的方法，尤其是在薄而详细的结构中。 et.al.|[2403.05005](http://arxiv.org/abs/2403.05005)|null|
|**2024-03-11**|**Efficient LoFTR: Semi-Dense Local Feature Matching with Sparse-Like Speed**|我们提出了一种新的方法来有效地产生图像之间的半密集匹配。先前的无检测器匹配器LoFTR在处理大的视点变化和纹理较差的场景时显示出显著的匹配能力，但效率较低。我们重新审视了它的设计选择，并在效率和准确性方面进行了多项改进。一个关键的观察结果是，由于共享的局部信息，在整个特征图上执行转换是冗余的，因此我们提出了一种具有自适应令牌选择的聚合注意力机制，以提高效率。此外，我们发现LoFTR的精细相关模块存在空间方差，这不利于匹配精度。提出了一种新的两级相关层，以实现精确的亚像素对应，从而提高精度。我们的效率优化模型比LoFTR快$\sim 2.5\倍，甚至可以超过最先进的高效稀疏匹配管道SuperPoint+LightGlue。此外，大量的实验表明，与竞争性的半密集匹配器相比，我们的方法可以实现更高的精度，并具有可观的效率效益。这为大规模或延迟敏感的应用（如图像检索和3D重建）开辟了令人兴奋的前景。项目页面：https://zju3dv.github.io/efficientloftr. et.al.|[2403.04765](http://arxiv.org/abs/2403.04765)|null|
|**2024-03-08**|**Finding Waldo: Towards Efficient Exploration of NeRF Scene Spaces**|近年来，神经辐射场（NeRF）以其卓越的性能迅速成为三维重建和新视图合成的主要方法。尽管人们对NeRF方法非常感兴趣，但NeRF的一个实际用例在很大程度上被忽视了；由NeRF建模的场景空间的探索。在本文中，我们在文献中首次提出并正式定义场景探索框架为NeRF模型输入（即坐标和视角）的有效发现，使用该框架可以呈现符合用户选择标准的新颖视图，我们首先提出了两种基线方法，称为引导随机搜索（GRS）和基于姿态插值的搜索（PIBS）。然后，我们将场景探索视为一个优化问题，并提出了标准不可知的进化引导姿势搜索（EGPS）来进行有效的探索。我们用各种标准（例如显著性最大化、图像质量最大化、照片构图质量改进）测试了所有三种方法，并表明我们的EGPS比其他基线表现得更好。最后，我们强调了场景探索的重点和局限性，并概述了未来研究的方向。 et.al.|[2403.04508](http://arxiv.org/abs/2403.04508)|null|
|**2024-03-07**|**CN-RMA: Combined Network with Ray Marching Aggregation for 3D Indoors Object Detection from Multi-view Images**|本文介绍了一种从多视角图像中检测三维室内物体的新方法CN-RMA。我们观察到关键挑战是图像和3D对应关系的模糊性，而没有明确的几何结构来提供遮挡信息。为了解决这个问题，CN-RMA利用了3D重建网络和3D对象检测网络的协同作用，其中重建网络提供了粗略的截断有符号距离函数（TSDF），并引导图像特征以端到端的方式正确地投票到3D空间。具体来说，我们通过射线行进将权重与每条射线的采样点相关联，表示图像中像素对相应3D位置的贡献。这样的权重由预测的带符号距离确定，使得图像特征仅投票给重建表面附近的区域。我们的方法在从多视图图像中检测3D对象方面实现了最先进的性能，通过mAP@0.25和mAP@0.5在ScanNet和ARKitScenes数据集上。代码和型号发布于https://github.com/SerCharles/CN-RMA. et.al.|[2403.04198](http://arxiv.org/abs/2403.04198)|**[link](https://github.com/sercharles/cn-rma)**|
|**2024-03-07**|**Radiative Gaussian Splatting for Efficient X-ray Novel View Synthesis**|X射线由于其比自然光更强的穿透性而被广泛应用于透射成像。在绘制新视图X射线投影时，现有的主要基于NeRF的方法训练时间长，推理速度慢。在本文中，我们提出了一种基于三维高斯散射的框架，即X-Gaussian，用于X射线新视图合成。首先，受X射线成像各向同性的启发，我们重新设计了一个辐射高斯点云模型。我们的模型在学习预测3D点的辐射强度时排除了视角方向的影响。基于该模型，我们开发了一种具有CUDA实现的可微分辐射光栅化（DRR）。其次，我们定制了一种角度姿态长方体均匀初始化（ACUI）策略，该策略直接使用X射线扫描仪的参数来计算相机信息，然后对包围扫描对象的长方体内的点位置进行均匀采样。实验表明，我们的X-Gaussian比最先进的方法高6.5 dB，同时享受不到15%的训练时间和超过73倍的推理速度。在稀疏视图CT重建中的应用也揭示了该方法的实用价值。代码和模型将在https://github.com/caiyuanhao1998/X-Gaussian . 培训过程可视化的视频演示位于https://www.youtube.com/watch?v=gDVf_Ngeghg . et.al.|[2403.04116](http://arxiv.org/abs/2403.04116)|**[link](https://github.com/caiyuanhao1998/x-gaussian)**|
|**2024-03-05**|**Pooling Image Datasets With Multiple Covariate Shift and Imbalance**|小样本量在许多学科中很常见，这就需要在多个机构中汇集大致相似的数据集，以研究图像和疾病结果之间微弱但相关的关联。这种数据通常表现出协变量（即二次非成像数据）的偏移/不平衡。控制这种干扰变量在标准统计分析中很常见，但这些想法并不直接适用于参数过大的模型。因此，最近的工作表明，来自不变表示学习的策略是如何提供一个有意义的起点的，但目前的方法仅限于一次只考虑几个协变量的变化/不平衡。在本文中，我们展示了如何从范畴理论的角度看待这个问题，提供了一个简单有效的解决方案，完全避免了原本需要的复杂的多阶段训练管道。我们通过在真实数据集上进行的大量实验证明了这种方法的有效性。此外，我们讨论了这种形式的公式如何为至少5个以上不同的问题设置提供统一的视角，从自监督学习到3D重建中的匹配问题。 et.al.|[2403.02598](http://arxiv.org/abs/2403.02598)|null|

<p align=right>(<a href=#updated-on-20240314>back to top</a>)</p>

## Diffusion

|Publish Date|Title|Abstract|PDF|Code|
|---|---|---|---|---|
|**2024-03-13**|**VLOGGER: Multimodal Diffusion for Embodied Avatar Synthesis**|我们提出了VLOGGER，这是一种从一个人的单个输入图像中生成音频驱动的人类视频的方法，它建立在最近生成扩散模型的成功基础上。我们的方法包括1）一个随机的人三维运动扩散模型，以及2）一个新颖的基于扩散的架构，该架构通过空间和时间控制来增强文本到图像模型。这支持生成可变长度的高质量视频，易于通过人脸和身体的高级表示进行控制。与之前的工作相比，我们的方法不需要对每个人进行训练，不依赖于面部检测和裁剪，生成完整的图像（不仅仅是面部或嘴唇），并考虑了广泛的场景（例如可见躯干或不同的主体身份），这些场景对正确合成交流的人类至关重要。我们还策划了MENTOR，这是一个新的、多样化的数据集，具有三维姿势和表情注释，比以前的数据集（800000个身份）大一个数量级，并具有动态手势，我们在此基础上训练和展示我们的主要技术贡献。VLOGGER在三个公共基准中都优于最先进的方法，考虑到图像质量、身份保护和时间一致性，同时还生成上半身手势。我们分析了VLOGGER在多个多样性指标方面的性能，表明我们的架构选择和MENTOR的使用有利于在规模上训练一个公平和公正的模型。最后，我们展示了在视频编辑和个性化方面的应用。 et.al.|[2403.08764](http://arxiv.org/abs/2403.08764)|null|
|**2024-03-13**|**Spatiotemporal Diffusion Model with Paired Sampling for Accelerated Cardiac Cine MRI**|当前用于加速心脏电影MRI的深度学习重建存在空间和时间模糊问题。我们的目标是在高欠采样率下提高电影MRI的图像清晰度和运动描绘。开发了一种以现有深度学习重建为条件的时空扩散增强模型以及一种新的配对采样策略。在专家对临床数据的评估中，扩散模型提供了比原始重建更清晰的组织边界和更清晰的运动。创新的配对采样策略大大减少了生成结果中的人为噪声。 et.al.|[2403.08758](http://arxiv.org/abs/2403.08758)|null|
|**2024-03-13**|**Efficient Combinatorial Optimization via Heat Diffusion**|组合优化问题是广泛存在的，但由于其离散性而具有内在的挑战性。现有方法的主要局限性在于，它们在每次迭代时只能访问解空间的一小部分，导致搜索全局最优的效率有限。为了克服这一挑战，与扩大求解器搜索范围的传统努力不同，我们专注于使信息能够通过热扩散主动传播到求解器。通过变换目标函数同时保持其最优值，热扩散有助于信息从遥远的区域流到求解器，从而提供更有效的导航。利用热扩散，我们提出了一个解决一般组合优化问题的框架。所提出的方法在一系列最具挑战性和广泛遇到的组合优化中表现出卓越的性能。与利用热力学实现生成人工智能的最新进展相呼应，我们的研究进一步揭示了其在推进组合优化方面的巨大潜力。 et.al.|[2403.08757](http://arxiv.org/abs/2403.08757)|null|
|**2024-03-13**|**Sticky-threshold diffusions, local time approximation and parameter estimation**|我们研究了一类具有粘性振荡偏斜（SOS）阈值的扩散的高频路径泛函，包括粘性反射的情况，并建立了到局部时间的收敛性。这在几个方向上扩展了粘性、振荡（状态切换）和偏斜或反射扩散的现有结果。首先，它考虑任何偏离速度慢于 $n$的归一化序列$（u_n）_n$ 。其次，它允许这些功能的组合。基于此，以及占用时间的近似值，我们设计了一致的偏斜和粘性参数估计量。 et.al.|[2403.08754](http://arxiv.org/abs/2403.08754)|null|
|**2024-03-13**|**Clinically Feasible Diffusion Reconstruction for Highly-Accelerated Cardiac Cine MRI**|目前有限的加速心脏电影重建质量可能会通过新兴的扩散模型得到改善，但临床上不可接受的长处理时间带来了挑战。我们的目标是开发一种临床上可行的基于扩散模型的重建管道，以提高电影MRI的图像质量。我们开发了一个多入多出扩散增强模型和快速推理策略，用于与重建模型结合使用。专家检查证实，扩散重建减少了前瞻性欠采样临床数据中的空间和时间模糊。每个视频处理时间1.5秒，使该方法能够应用于临床场景。 et.al.|[2403.08749](http://arxiv.org/abs/2403.08749)|null|
|**2024-03-13**|**GaussCtrl: Multi-View Consistent Text-Driven 3D Gaussian Splatting Editing**|我们提出了GaussCtrl，这是一种文本驱动的方法来编辑通过3D高斯飞溅（3DGS）重建的3D场景。我们的方法首先通过使用3DGS渲染图像集合，并根据输入提示使用预先训练的2D扩散模型（ControlNet）对其进行编辑，然后使用该模型来优化3D模型。我们的主要贡献是多视图一致性编辑，它能够一起编辑所有图像，而不是像以前的工作那样在更新3D模型的同时迭代编辑一个图像。它可以实现更快的编辑和更高的视觉质量。这是通过两个术语实现的：（a）深度条件编辑，通过利用自然一致的深度图来加强多视图图像的几何一致性。（b） 基于注意力的潜在代码对齐，通过图像潜在表示之间的自我和跨视图注意力，将编辑图像的编辑条件为几个参考视图，从而统一编辑图像的外观。实验表明，与以前最先进的方法相比，我们的方法实现了更快的编辑和更好的视觉效果。 et.al.|[2403.08733](http://arxiv.org/abs/2403.08733)|null|
|**2024-03-13**|**Ambient Diffusion Posterior Sampling: Solving Inverse Problems with Diffusion Models trained on Corrupted Data**|我们提供了一个框架来解决从线性破坏数据中学习的扩散模型的反问题。我们的方法，环境扩散后验采样（A-DPS），利用在一种类型的损坏（例如图像修复）上预先训练的生成模型，以潜在不同的前向过程（例如图像模糊）的测量为条件进行后验采样。我们在标准自然图像数据集（CelebA、FFHQ和AFHQ）上测试了我们的方法的有效性，我们发现A-DPS有时在速度和性能方面都优于在干净数据上训练的模型。我们进一步扩展了环境扩散框架，以训练MRI模型，仅访问各种加速度因子（R=2，4，6，8）下的傅立叶子采样多线圈MRI测量。我们再次观察到，与在完全采样数据上训练的模型相比，在高加速状态下，在高子采样数据上培训的模型是解决反问题的更好的先验。我们开源了我们的代码和经过训练的Ambient Diffusion MRI模型：https://github.com/utcsilab/ambient-diffusion-mri . et.al.|[2403.08728](http://arxiv.org/abs/2403.08728)|**[link](https://github.com/utcsilab/ambient-diffusion-mri)**|
|**2024-03-13**|**Historical Astronomical Diagrams Decomposition in Geometric Primitives**|从历史手稿中绘制的数十万张图表中自动提取几何内容，将使历史学家能够在全球范围内研究天文学知识的传播。然而，最先进的矢量化方法，通常是为了处理现代数据而设计的，并不适应历史天文图的复杂性和多样性。因此，我们的贡献是双重的。首先，我们介绍了一个独特的数据集，其中包括来自不同传统的303幅天文图，从19世纪到18世纪，用3000多条线段、圆和弧进行了注释。其次，我们开发了一个基于DINO-DETR的模型，以实现对多个几何图元的预测。我们证明，它可以仅在合成数据上进行训练，并在我们具有挑战性的数据集上准确预测基元。我们的方法通过对多个基元引入有意义的参数化，联合训练进行检测和参数细化，使用可变形注意力和对丰富的合成数据进行训练，大大改进了仅限于线的LETR基线。我们的数据集和代码可在我们的网页上找到。 et.al.|[2403.08721](http://arxiv.org/abs/2403.08721)|null|
|**2024-03-13**|**Limits on the OH Molecule in the Smith High Velocity Cloud**|我们使用绿岸望远镜（GBT）在史密斯云中的几个位置搜索OH分子，史密斯云是银河系周围最突出的高速云之一。选择了五个HI柱密度高的位置作为单个点的目标，以及普朗克望远镜在史密斯云尖端附近探测到的分子云周围的平方度。星系盘中具有类似 $N_{HI}$值的气体具有可检测的OH发射。尽管我们在与前景阿奎拉分子云一致的速度下发现了OH，但在1 km$s^1$通道中，在史密斯云的速度达到0.7 mK（T$_b$）的rms水平时，没有发现任何OH。详细分析了对OH给出最严格限制的三个位置。它们的组合数据暗示了$N（H_2）/N｛HI｝leq 0.03$的$5\ sigma$极限，该极限由取决于OH激发温度和背景连续体$T_｛ex｝/（T_{ex}-T_{bg}）$ 。没有证据表明史密斯云中的尘埃会发出远红外辐射。这些结果与人们对暴露在银河系晕辐射场中的低金属度漫射云的预期一致，而不是银河系喷泉的产物。 et.al.|[2403.08704](http://arxiv.org/abs/2403.08704)|null|
|**2024-03-13**|**Diffusion-based Iterative Counterfactual Explanations for Fetal Ultrasound Image Quality Assessment**|产科超声图像质量对于准确诊断和监测胎儿健康至关重要。然而，由于超声医师的专业知识和母亲BMI或胎儿动力学等因素的影响，制作高质量的标准平面是困难的。在这项工作中，我们建议使用基于扩散的反事实可解释人工智能从低质量的非标准平面生成真实的高质量标准平面。通过定量和定性评估，我们证明了我们的方法在产生质量提高的合理反事实方面的有效性。这表明了未来通过提供视觉反馈来加强临床医生的培训，以及提高图像质量，从而提高下游诊断和监测的前景。 et.al.|[2403.08700](http://arxiv.org/abs/2403.08700)|null|

<p align=right>(<a href=#updated-on-20240314>back to top</a>)</p>

## NeRF

|Publish Date|Title|Abstract|PDF|Code|
|---|---|---|---|---|
|**2024-03-12**|**Scalable Spatiotemporal Prediction with Bayesian Neural Fields**|时空数据集由空间参考的时间序列组成，在许多科学和商业智能应用中无处不在，如空气污染监测、疾病跟踪和云需求预测。随着现代数据集的规模和复杂性不断增加，人们越来越需要新的统计方法，这些方法足够灵活，可以捕捉复杂的时空动态，并且可以扩展，可以处理大型预测问题。这项工作提出了贝叶斯神经场（BayesNF），这是一种用于推断时空域上丰富概率分布的域通用统计模型，可用于数据分析任务，包括预测、插值和变差法。BayesNF将一种用于高容量函数估计的新型深度神经网络架构与用于鲁棒不确定性量化的分层贝叶斯推理相结合。通过通过一系列平滑可微变换定义先验，使用通过随机梯度下降训练的变量学习代理对大规模数据进行后验推理。我们根据突出的统计和机器学习基线评估BayesNF，显示出在气候和公共卫生数据集的各种预测问题上的显著改进，这些数据集包含数万到数十万个测量值。该论文附有一个开源软件包(https://github.com/google/bayesnf)它易于使用，并与JAX机器学习平台上的现代GPU和TPU加速器兼容。 et.al.|[2403.07657](http://arxiv.org/abs/2403.07657)|**[link](https://github.com/google/bayesnf)**|
|**2024-03-11**|**SiLVR: Scalable Lidar-Visual Reconstruction with Neural Radiance Fields for Robotic Inspection**|我们提出了一种基于神经场的大规模重建系统，该系统融合激光雷达和视觉数据，生成几何精度高的高质量重建，并捕捉照片逼真的纹理。该系统采用了最先进的神经辐射场（NeRF）表示，还结合了激光雷达数据，这对深度和表面法线增加了强大的几何约束。我们利用实时激光雷达SLAM系统的轨迹来引导运动结构（SfM）过程，以显著减少计算时间，并提供对激光雷达深度损失至关重要的度量尺度。我们使用子映射将系统缩放到长轨迹上捕获的大规模环境。我们用多摄像头、激光雷达传感器套件的数据演示了重建系统，该套件安装在腿式机器人上，手持扫描600米的建筑场景，并安装在空中机器人上，测量多层模拟灾难现场建筑。网站https://ori-drs.github.io/projects/silvr/ et.al.|[2403.06877](http://arxiv.org/abs/2403.06877)|null|
|**2024-03-09**|**CoNFiLD: Conditional Neural Field Latent Diffusion Model Generating Spatiotemporal Turbulence**|本研究介绍了条件神经场潜在扩散（CoNFiLD）模型，这是一种新的生成学习框架，旨在快速模拟三维不规则域内混沌和湍流系统中复杂的时空动力学。传统的涡解析数值模拟，尽管提供了详细的流量预测，但由于其广泛的计算需求，遇到了很大的局限性，限制了其在更广泛的工程环境中的应用。相比之下，基于深度学习的代理模型有望提供高效、数据驱动的解决方案。然而，它们的有效性往往因依赖确定性框架而受到损害，而确定性框架在准确捕捉湍流的混沌和随机性质方面存在不足。CoNFiLD模型通过将条件神经场编码与潜在扩散过程协同集成来解决这些挑战，从而能够在不同条件下高效且稳健地生成时空湍流。利用贝叶斯条件采样，该模型可以无缝适应各种湍流生成场景，而无需再训练，涵盖从使用稀疏传感器测量的零样本全场流重建到超分辨率生成和时空流数据恢复的应用。已经对各种具有不规则几何形状的非均匀、各向异性湍流进行了全面的数值实验，以评估该模型的多功能性和有效性，展示了其在湍流生成和更广泛的时空动力学建模领域的变革潜力。 et.al.|[2403.05940](http://arxiv.org/abs/2403.05940)|null|
|**2024-03-09**|**Learned 3D volumetric recovery of clouds and its uncertainty for climate analysis**|气候预测和云物理的重大不确定性与浅层散射云的观测差距有关。应对这些挑战需要对其三维（3D）异质体积散射内容进行遥感。这就需要无源散射计算机断层扫描（CT）。我们设计了一个基于学习的模型（ProbeCT）来实现这种云的CT，基于有噪声的多视图星载图像。ProbeCT首次推断出每个3D位置的异质消光系数的后验概率分布。这产生了任意有价值的统计数据，例如，最可能灭绝的3D场及其不确定性。ProbeCT使用神经场表示，进行本质上实时的推理。ProbeCT通过一个新的基于物理的云体积场及其相应图像的标记多类数据库进行监督训练。为了改进分布外推理，我们通过差分渲染引入了自监督学习。我们在模拟和真实世界的数据中演示了该方法，并指出了3D恢复和不确定性与降水和可再生能源的相关性。 et.al.|[2403.05932](http://arxiv.org/abs/2403.05932)|null|
|**2024-03-06**|**ProxNF: Neural Field Proximal Training for High-Resolution 4D Dynamic Image Reconstruction**|精确的时空图像重建方法被广泛的生物医学研究领域所需要，但由于数据的不完整性和计算负担而面临挑战。数据不完整性源于增加帧速率和减少采集时间所需的欠采样，而计算负担则源于具有三维空间和扩展时间范围的高分辨率图像的内存占用。神经场是一类新兴的神经网络，充当时空对象的连续表示，以前已经引入它来通过将图像重建重新定义为估计网络参数的问题来解决这些动态成像问题。神经场可以通过利用这些时空对象中潜在的冗余来解决数据不完整和计算负担这两个挑战。这项工作提出了ProxNF，这是一种用于时空图像重建的新的神经场训练方法，利用近端分裂方法将涉及成像算子的计算与网络参数的更新分开。具体而言，ProxNF评估图像域中数据保真度项的（子采样）梯度，并使用完全监督学习方法来更新神经场参数。通过减少内存占用和评估成像算子的计算成本，所提出的ProxNF方法允许重建大的、高分辨率的时空图像。该方法在两项数值研究中得到了证明，这两项研究涉及解剖逼真的动态数值小鼠模型和肿瘤灌注的两室模型的虚拟动态对比增强光声计算机断层扫描成像。 et.al.|[2403.03860](http://arxiv.org/abs/2403.03860)|null|
|**2024-03-05**|**NRDF: Neural Riemannian Distance Fields for Learning Articulated Pose Priors**|忠实地为关节空间建模是一项关键任务，它可以恢复和生成逼真的姿势，而且仍然是一项臭名昭著的挑战。为此，我们引入了神经黎曼距离场（NRDF），这是一种数据驱动的先验，用于建模看似合理的关节空间，表示为高维乘积四元数空间中神经场的零级集。为了仅在正示例上训练NRDF，我们引入了一种新的采样算法，确保测地距离遵循所需的分布，从而产生一种原则性的距离场学习范式。然后，我们设计了一种投影算法，通过自适应步长黎曼优化器将任何随机姿态映射到水平集上，始终遵循关节旋转的乘积流形。NRDF可以通过反向传播和数学类比计算黎曼梯度，与最近的生成模型黎曼流匹配有关。我们在各种下游任务中，即姿态生成、基于图像的姿态估计和求解逆运动学，对照其他姿态先验对NRDF进行了全面评估，突出了NRDF的优越性能。除了人类，NRDF的多功能性还延伸到手和动物姿势，因为它可以有效地代表任何关节。 et.al.|[2403.03122](http://arxiv.org/abs/2403.03122)|null|
|**2024-03-04**|**MagicClay: Sculpting Meshes With Generative Neural Fields**|神经领域的最新发展为形状生成领域带来了非凡的能力，但它们缺乏关键的特性，例如增量控制，这是艺术作品的基本要求。另一方面，三角网格是大多数几何相关任务的选择，提供了高效和直观的控制，但不适合神经优化。为了支持下游任务，现有技术通常提出两步方法，其中首先使用神经场生成形状，然后提取网格进行进一步处理。相反，在本文中，我们引入了一种混合方法，该方法保持网格和符号距离场（SDF）表示的一致性。使用这种表示，我们介绍了MagicClay——一种艺术家友好的工具，用于根据文本提示雕刻网格区域，同时保持其他区域不变。我们的框架仔细而有效地平衡了形状优化每一步中表示和正则化之间的一致性；依靠网格表示，我们展示了如何以更高的分辨率和更快的速度渲染SDF。此外，我们利用最近在可微网格重建方面的工作，在需要的地方自适应地分配网格中的三角形，如SDF所示。使用一个实现的原型，我们展示了与最先进的生成几何体相比的优越性，以及新颖的一致性控制，首次允许对同一网格进行基于提示的顺序编辑。 et.al.|[2403.02460](http://arxiv.org/abs/2403.02460)|null|
|**2024-03-04**|**Activity estimation via distributed measurements in an orientation sensitive neural fields model of the visual cortex**|本文在可观察性理论的框架下研究了初级视觉皮层（V1）内神经活动的在线估计。我们专注于对超体积活动建模的低维神经场，以描述V1中的活动。我们使用V1上的平均皮层活动作为测量。我们的贡献包括详细说明模型的可观察性奇点，并开发一种混合高增益观测器，该观测器在特定的激励条件下实现实际收敛，同时在生物相关性的情况下保持渐近收敛。该研究强调了模型的非线性性质与其可观测性之间的内在联系。我们还介绍了数值实验，强调了观测者的不同性质。 et.al.|[2403.01906](http://arxiv.org/abs/2403.01906)|null|
|**2024-03-02**|**Neural Field Classifiers via Target Encoding and Classification Loss**|神经场方法在计算机视觉和计算机图形学中的各种长期任务中取得了巨大进展，包括新颖的视图合成和几何重建。由于现有的神经场方法试图预测一些基于坐标的连续目标值，例如神经辐射场（NeRF）的RGB，所有这些方法都是回归模型，并通过一些回归损失进行优化。然而，对于神经场方法来说，回归模型真的比分类模型更好吗？在这项工作中，我们试图从机器学习的角度来探讨神经领域这个非常基本但被忽视的问题。我们成功地提出了一种新的神经场分类器（NFC）框架，该框架将现有的神经场方法公式化为分类任务，而不是回归任务。所提出的NFC可以通过使用新的目标编码模块和优化分类损失，轻松地将任意神经场回归器（NFR）转换为其分类变体。通过将连续回归目标编码为高维离散编码，我们自然地形成了多标签分类任务。大量的实验证明了NFC在几乎免费的额外计算成本下令人印象深刻的有效性。此外，NFC还显示出对稀疏输入、损坏图像和动态场景的鲁棒性。 et.al.|[2403.01058](http://arxiv.org/abs/2403.01058)|null|
|**2024-02-28**|**NERV++: An Enhanced Implicit Neural Video Representation**|神经场，也称为隐式神经表示（INRs），在表示、生成和操作各种数据类型方面表现出了非凡的能力，允许在低内存占用下进行连续的数据重建。尽管应用于视频压缩的INRs很有前景，但仍需要大幅度提高其率失真性能，并且需要大量的参数和长时间的训练迭代来捕捉高频细节，限制了其更广泛的适用性。解决这个问题仍然是一项极具挑战性的任务，这将使INR在压缩任务中更容易访问。我们通过引入视频的神经表示NeRV++朝着解决这些缺点迈出了一步，NeRV++是一种增强的隐式神经视频表示，是对原始NeRV解码器架构的更直接但有效的增强，其特征是夹着上采样块（UB）的可分离conv2d残差块（SCRB），以及用于改进特征表示的双线性插值跳过层。NeRV++允许将视频直接表示为神经网络近似的函数，并显著增强了当前基于INR的视频编解码器之外的表示能力。我们在UVG、MCL-JVC和Bunny数据集上评估了我们的方法，在INRs的视频压缩方面取得了有竞争力的结果。这一成果缩小了与基于自动编码器的视频编码的差距，标志着基于INR的视频压缩研究迈出了重要一步。 et.al.|[2402.18305](http://arxiv.org/abs/2402.18305)|null|

<p align=right>(<a href=#updated-on-20240314>back to top</a>)</p>

[contributors-shield]: https://img.shields.io/github/contributors/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[contributors-url]: https://github.com/Vincentqyw/cv-arxiv-daily/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[forks-url]: https://github.com/Vincentqyw/cv-arxiv-daily/network/members
[stars-shield]: https://img.shields.io/github/stars/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[stars-url]: https://github.com/Vincentqyw/cv-arxiv-daily/stargazers
[issues-shield]: https://img.shields.io/github/issues/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[issues-url]: https://github.com/Vincentqyw/cv-arxiv-daily/issues

