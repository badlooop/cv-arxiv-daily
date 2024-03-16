[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]

## Updated on 2024.03.16
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
|**2024-03-14**|**The NeRFect Match: Exploring NeRF Features for Visual Localization**|在这项工作中，我们建议使用神经辐射场（NeRF）作为视觉定位的场景表示。最近，NeRF已被用于通过增强训练数据库、通过渲染图像提供辅助监督或作为迭代细化模块来增强姿态回归和场景坐标回归模型。我们通过探索NeRF的内部特征在建立精确的2D-3D定位匹配方面的潜力，扩展了其公认的优势——它能够提供具有逼真外观和精确几何形状的紧凑场景表示。为此，我们对通过视图合成获得的NeRF的内隐知识进行了全面的检查，以在各种条件下进行匹配。这包括探索不同的匹配网络架构，在多个层提取编码器特征，以及不同的训练配置。值得注意的是，我们引入了NeRFMatch，这是一种先进的2D-3D匹配功能，它利用了通过视图合成学习到的NeRF的内部知识。我们在基于结构的管道内，根据标准本地化基准对NeRFMatch进行评估，为剑桥地标的本地化性能树立了新的最先进水平。 et.al.|[2403.09577](http://arxiv.org/abs/2403.09577)|null|
|**2024-03-14**|**Relaxing Accurate Initialization Constraint for 3D Gaussian Splatting**|3D高斯散射（3DGS）最近在实时新视图合成和3D重建方面表现出了令人印象深刻的能力。然而，3DGS在很大程度上依赖于从运动结构（SfM）方法导出的精确初始化。当使用随机初始化的点云进行训练时，3DGS无法保持其产生高质量图像的能力，PSNR的性能大幅下降4-5dB。通过在频域中对SfM初始化的广泛分析和对具有多个1D高斯的1D回归任务的分析，我们提出了一种新的优化策略RAIN-GS（放宽3D高斯散射的精确初始化约束），该策略成功地从随机点云中训练了3D高斯。我们通过在多个数据集上进行定量和定性比较，展示了我们策略的有效性，大大提高了所有环境中的性能。我们的项目页面和代码可以在https://ku-cvlab.github.io/RAIN-GS. et.al.|[2403.09413](http://arxiv.org/abs/2403.09413)|**[link](https://github.com/KU-CVLAB/RAIN-GS)**|
|**2024-03-12**|**Q-SLAM: Quadric Representations for Monocular SLAM**|Monocular SLAM长期以来一直在努力应对准确建模3D几何图形的挑战。基于神经辐射场（NeRF）的单目SLAM的最新进展显示出了前景，但这些方法通常侧重于新颖的视图合成，而不是精确的3D几何建模。这种关注导致NeRF应用（即新的视图合成）与SLAM的要求之间的显著脱节。我们发现，间隙是由NeRF中使用的体积表示产生的，这些表示通常是密集的和有噪声的。在这项研究中，我们提出了一种新的方法，通过二次曲面的透镜重新想象体积表示。我们假设大多数场景组件可以有效地表示为二次平面。利用这一假设，我们通过几个二次平面用数百万个立方体重塑体积表示，这导致在SLAM环境中对3D场景进行更准确和高效的建模。我们的方法包括两个关键步骤：首先，我们使用二次假设来增强从跟踪模块（例如Droid SLAM）获得的粗略深度估计。仅此步骤就显著提高了深度估计的准确性。其次，在随后的映射阶段，我们偏离了以前基于NeRF的SLAM方法，该方法在整个体积空间中分布采样点。相反，我们将采样点集中在二次平面周围，并使用一种新的二次分解变换器对它们进行聚合。此外，我们还介绍了一种端到端的联合优化策略，该策略将姿态估计与三维重建同步。 et.al.|[2403.08125](http://arxiv.org/abs/2403.08125)|null|
|**2024-03-12**|**Learning Generalizable Feature Fields for Mobile Manipulation**|移动操作中的一个悬而未决的问题是如何以统一的方式表示对象和场景，以便机器人既可以在环境中导航，也可以操作对象。后者需要在理解细粒度语义的同时捕获复杂的几何体，而前者则需要捕获继承到扩展物理规模的复杂性。在这项工作中，我们提出了GeFF（可泛化特征场），这是一个场景级的可泛化神经特征场，作为实时执行的导航和操纵的统一表示。为此，我们将生成新视图合成视为预训练任务，然后通过CLIP特征提取将生成的丰富场景先验与自然语言对齐。我们通过在配备机械手的四足机器人上部署GeFF来证明这种方法的有效性。当在动态场景中执行开放词汇移动操作时，我们评估了GeFF泛化到开放集对象的能力以及运行时间。 et.al.|[2403.07563](http://arxiv.org/abs/2403.07563)|null|
|**2024-03-13**|**DNGaussian: Optimizing Sparse-View 3D Gaussian Radiance Fields with Global-Local Depth Normalization**|辐射场在从稀疏输入视图合成新视图方面表现出了令人印象深刻的性能，但主流方法的训练成本高，推理速度慢。本文介绍了DNGaussian，一种基于三维高斯辐射场的深度正则化框架，以低成本提供实时、高质量的少镜头新视图合成。我们的动机源于最近的3D高斯飞溅的高效表示和令人惊讶的质量，尽管当输入视图减少时，它会遇到几何退化。在高斯辐射场中，我们发现场景几何的这种退化主要与高斯基元的定位有关，并且可以通过深度约束来缓解。因此，我们提出了一种硬深度和软深度正则化，以在粗略的单目深度监督下恢复准确的场景几何体，同时保持细粒度的颜色外观。为了进一步细化详细的几何体重塑，我们引入了全局局部深度归一化，增强了对局部深度小变化的关注。在LLFF、DTU和Blender数据集上进行的大量实验表明，DNGaussian优于最先进的方法，实现了相当或更好的结果，显著降低了内存成本，减少了25美元的训练时间，渲染速度快了3000美元以上。 et.al.|[2403.06912](http://arxiv.org/abs/2403.06912)|**[link](https://github.com/fictionarry/dngaussian)**|
|**2024-03-11**|**FreGS: 3D Gaussian Splatting with Progressive Frequency Regularization**|三维高斯泼溅在实时新颖视图合成中取得了令人印象深刻的性能。然而，在高斯致密化过程中，它经常遭受过度重建，其中高方差图像区域仅被几个大高斯覆盖，导致渲染图像中的模糊和伪影。我们设计了一种渐进频率正则化（FreGS）技术来解决频率空间内的过重构问题。具体而言，FreGS通过利用傅立叶空间中的低通和高通滤波器可以容易地提取的低频到高频分量来执行从粗到细的高斯致密化。通过最小化渲染图像的频谱与相应的地面实况之间的差异，它实现了高质量的高斯致密化，并有效地缓解了高斯飞溅的过度重建。在多个广泛采用的基准上进行的实验（例如，Mip-NeRF360、Tanks and Temples和Deep Blending）表明，FreGS实现了卓越的新型视图合成，并始终优于最先进的视图合成。 et.al.|[2403.06908](http://arxiv.org/abs/2403.06908)|null|
|**2024-03-11**|**V3D: Video Diffusion Models are Effective 3D Generators**|3D自动生成最近引起了广泛关注。最近的方法大大加快了生成速度，但由于模型容量或3D数据有限，通常会生成不太详细的对象。受视频扩散模型最新进展的启发，我们引入了V3D，它利用预先训练的视频扩散模型的世界模拟能力来促进3D生成。为了充分释放视频扩散感知3D世界的潜力，我们进一步引入了几何一致性先验，并将视频扩散模型扩展到多视图一致的3D生成器中。得益于此，可以对最先进的视频扩散模型进行微调，以在给定单个图像的情况下生成围绕对象的360度轨道帧。通过我们量身定制的重建管道，我们可以在3分钟内生成高质量的网格或3D高斯。此外，我们的方法可以扩展到场景级的新视图合成，实现对稀疏输入视图的相机路径的精确控制。大量实验证明了该方法的优越性能，特别是在生成质量和多视图一致性方面。我们的代码可在https://github.com/heheyas/V3D et.al.|[2403.06738](http://arxiv.org/abs/2403.06738)|**[link](https://github.com/heheyas/v3d)**|
|**2024-03-11**|**Vosh: Voxel-Mesh Hybrid Representation for Real-Time View Synthesis**|神经辐射场（NeRF）已成为合成新颖视图的逼真图像的一种突出方法。虽然基于体素或网格的神经辐射表示分别提供了不同的优势，在渲染质量或速度方面都很出色，但每种方法在其他方面都有局限性。作为回应，我们提出了一种名为Vosh的开创性混合表示，在用于视图合成的混合渲染中无缝组合体素和网格组件。Vosh是通过优化NeRF的体素网格精心制作的，战略性地将选定的体素替换为网格。因此，它擅长通过网格组件快速渲染具有简单几何体和纹理的场景，同时通过利用体素组件在复杂区域实现高质量渲染。Vosh的灵活性通过调整混合比率的能力得到了展示，为用户提供了基于灵活使用控制渲染质量和速度之间平衡的能力。实验结果表明，我们的方法在渲染质量和速度之间实现了值得称赞的折衷，并且在移动设备上具有显著的实时性能。 et.al.|[2403.06505](http://arxiv.org/abs/2403.06505)|null|
|**2024-03-13**|**FSViewFusion: Few-Shots View Generation of Novel Objects**|自从NeRF出现以来，新颖的视图合成已经得到了巨大的发展。然而，Nerf模型在单个场景上过拟合，缺乏对分布外对象的泛化能力。最近，扩散模型在视图合成中引入泛化方面表现出了显著的性能。受这些进步的启发，我们探索了预训练的稳定扩散模型在没有显式3D先验的情况下进行视图合成的能力。具体来说，我们的方法基于个性化的文本到图像模型Dreambooth，因为它具有很强的能力，只需几次拍摄就可以适应特定的新颖对象。我们的研究揭示了两个有趣的发现。首先，我们观察到，与涉及对大量多视图数据进行微调扩散的更复杂的策略相比，Dreambooth可以学习视图的高级概念。其次，我们建立了一个观点的概念可以被解开并转移到一个新的对象上，而不考虑从中学习观点的原始对象的身份。受此启发，我们引入了一种学习策略FSViewFusion，该策略仅通过单个场景的一个图像样本继承特定视图，并使用低阶适配器将知识转移到从少数镜头中学习的新对象。通过广泛的实验，我们证明了我们的方法虽然简单，但在为野生图像生成可靠的视图样本方面是有效的。将发布代码和模型。 et.al.|[2403.06394](http://arxiv.org/abs/2403.06394)|null|
|**2024-03-13**|**S-DyRF: Reference-Based Stylized Radiance Fields for Dynamic Scenes**|目前的3D风格化方法往往假设场景是静态的，这违背了我们现实世界的动态本质。为了解决这一限制，我们提出了S-DyRF，这是一种基于参考的动态神经辐射场时空风格化方法。然而，由于沿时间轴的风格化参考图像的可用性有限，风格化动态3D场景本质上是具有挑战性的。我们的关键见解在于除了提供的参考之外，还引入了额外的时间线索。为此，我们从给定的程式化引用中生成时间伪引用。这些伪参考便于样式信息从参考传播到整个动态3D场景。对于粗略的样式转换，我们强制使用新颖的视图和时间，以在特征级别模拟伪引用中存在的样式细节。为了保留高频细节，我们从时间伪参考创建了一个风格化的时间伪射线集合。这些伪射线作为实现精细风格转换的详细和明确的风格化指导。在合成数据集和真实世界数据集上的实验表明，我们的方法在动态3D场景上产生了合理的时空视图合成风格化结果。 et.al.|[2403.06205](http://arxiv.org/abs/2403.06205)|null|

<p align=right>(<a href=#updated-on-20240316>back to top</a>)</p>

## 3D Reconstruction

|Publish Date|Title|Abstract|PDF|Code|
|---|---|---|---|---|
|**2024-03-14**|**Relaxing Accurate Initialization Constraint for 3D Gaussian Splatting**|3D高斯散射（3DGS）最近在实时新视图合成和3D重建方面表现出了令人印象深刻的能力。然而，3DGS在很大程度上依赖于从运动结构（SfM）方法导出的精确初始化。当使用随机初始化的点云进行训练时，3DGS无法保持其产生高质量图像的能力，PSNR的性能大幅下降4-5dB。通过在频域中对SfM初始化的广泛分析和对具有多个1D高斯的1D回归任务的分析，我们提出了一种新的优化策略RAIN-GS（放宽3D高斯散射的精确初始化约束），该策略成功地从随机点云中训练了3D高斯。我们通过在多个数据集上进行定量和定性比较，展示了我们策略的有效性，大大提高了所有环境中的性能。我们的项目页面和代码可以在https://ku-cvlab.github.io/RAIN-GS. et.al.|[2403.09413](http://arxiv.org/abs/2403.09413)|**[link](https://github.com/KU-CVLAB/RAIN-GS)**|
|**2024-03-13**|**3DFIRES: Few Image 3D REconstruction for Scenes with Hidden Surface**|本文介绍了一种新的基于姿态图像的场景级三维重建系统3DFIRES。3DFIRES的设计只适用于一个视图，它重建了看不见的场景的完整几何体，包括隐藏的表面。使用多个视图输入，我们的方法可以在所有相机截头体内进行完全重建。我们的方法的一个关键特征是在特征级别融合多视图信息，从而实现连贯和全面的3D重建。我们在大规模真实场景数据集的非水密扫描上训练我们的系统。我们表明，它与仅使用一个输入的单视图重建方法的效果相匹配，并且在稀疏视图3D重建的定量和定性测量方面都超过了现有技术。 et.al.|[2403.08768](http://arxiv.org/abs/2403.08768)|null|
|**2024-03-13**|**Refractive COLMAP: Refractive Structure-from-Motion Revisited**|在本文中，我们提出了一个完整的折射运动结构（RSfM）框架，用于使用折射相机设置（用于平端口和圆顶端口水下外壳）进行水下3D重建。尽管在过去十年中在折射多视图几何方面取得了显著成就，但目前还没有一个强大、完整和公开的解决方案来解决这类任务，而且实际应用往往不得不通过针孔相机模型的固有（失真）参数来近似折射效应。为了填补这一空白，我们在最先进的开源SfM框架COLMAP中，在整个SfM过程中集成了折射考虑因素。对具有地面实况的合成生成但照片逼真的图像进行的数值模拟和重建结果验证了与空中重建相比，启用折射不会损害准确性或稳健性。最后，我们使用由近6000张图像组成的数据集展示了我们的方法在大规模折射场景中的能力。该实现以开源形式发布于：https://cau-git.rz.uni-kiel.de/inf-ag-koeser/colmap_underwater. et.al.|[2403.08640](http://arxiv.org/abs/2403.08640)|null|
|**2024-03-12**|**Q-SLAM: Quadric Representations for Monocular SLAM**|Monocular SLAM长期以来一直在努力应对准确建模3D几何图形的挑战。基于神经辐射场（NeRF）的单目SLAM的最新进展显示出了前景，但这些方法通常侧重于新颖的视图合成，而不是精确的3D几何建模。这种关注导致NeRF应用（即新的视图合成）与SLAM的要求之间的显著脱节。我们发现，间隙是由NeRF中使用的体积表示产生的，这些表示通常是密集的和有噪声的。在这项研究中，我们提出了一种新的方法，通过二次曲面的透镜重新想象体积表示。我们假设大多数场景组件可以有效地表示为二次平面。利用这一假设，我们通过几个二次平面用数百万个立方体重塑体积表示，这导致在SLAM环境中对3D场景进行更准确和高效的建模。我们的方法包括两个关键步骤：首先，我们使用二次假设来增强从跟踪模块（例如Droid SLAM）获得的粗略深度估计。仅此步骤就显著提高了深度估计的准确性。其次，在随后的映射阶段，我们偏离了以前基于NeRF的SLAM方法，该方法在整个体积空间中分布采样点。相反，我们将采样点集中在二次平面周围，并使用一种新的二次分解变换器对它们进行聚合。此外，我们还介绍了一种端到端的联合优化策略，该策略将姿态估计与三维重建同步。 et.al.|[2403.08125](http://arxiv.org/abs/2403.08125)|null|
|**2024-03-11**|**Bayesian Diffusion Models for 3D Shape Reconstruction**|我们提出了贝叶斯扩散模型（BDM），这是一种通过联合扩散过程将自上而下（先验）的信息与自下而上（数据驱动）的过程紧密耦合来执行有效贝叶斯推理的预测算法。我们展示了BDM在三维形状重建任务中的有效性。与在配对（监督）数据标签（如图像点云）数据集上训练的原型深度学习数据驱动方法相比，我们的BDM从独立标签（如点云）中引入了丰富的先验信息，以改进自下而上的3D重建。与推理需要显式先验和似然的标准贝叶斯框架不同，BDM通过与学习的梯度计算网络的耦合扩散过程来执行无缝信息融合。我们BDM的特点在于它能够参与自上而下和自下而上的过程的积极有效的信息交换和融合，其中每个过程本身就是一个扩散过程。我们在3D形状重建的合成基准和真实世界基准上展示了最先进的结果。 et.al.|[2403.06973](http://arxiv.org/abs/2403.06973)|null|
|**2024-03-08**|**DITTO: Dual and Integrated Latent Topologies for Implicit 3D Reconstruction**|我们提出了一种新的对偶和集成潜在拓扑（简称DITTO）概念，用于从噪声和稀疏点云中进行隐式三维重建。大多数现有的方法主要关注单个潜在类型，如点或网格潜在。相反，所提出的DITTO利用点和网格潜伏时间（即双重潜伏时间）来增强它们的强度、网格潜伏时间的稳定性和点潜伏时间的细节丰富能力。DITTO由双隐式编码器和集成隐式解码器组成。在双潜伏编码器中，双潜伏层是构成编码器的关键模块块，它并行地细化两个潜伏，保持它们不同的形状，并实现递归交互。值得注意的是，新提出的双潜伏层内的动态稀疏点变换器有效地细化了点潜伏。然后，集成隐式解码器系统地结合了这些精细的延迟，实现了高保真度的3D重建，并在对象和场景级数据集上超越了以前最先进的方法，尤其是在薄而详细的结构中。 et.al.|[2403.05005](http://arxiv.org/abs/2403.05005)|null|
|**2024-03-11**|**Efficient LoFTR: Semi-Dense Local Feature Matching with Sparse-Like Speed**|我们提出了一种新的方法来有效地产生图像之间的半密集匹配。先前的无检测器匹配器LoFTR在处理大的视点变化和纹理较差的场景时显示出显著的匹配能力，但效率较低。我们重新审视了它的设计选择，并在效率和准确性方面进行了多项改进。一个关键的观察结果是，由于共享的局部信息，在整个特征图上执行转换是冗余的，因此我们提出了一种具有自适应令牌选择的聚合注意力机制，以提高效率。此外，我们发现LoFTR的精细相关模块存在空间方差，这不利于匹配精度。提出了一种新的两级相关层，以实现精确的亚像素对应，从而提高精度。我们的效率优化模型比LoFTR快$\sim 2.5\倍，甚至可以超过最先进的高效稀疏匹配管道SuperPoint+LightGlue。此外，大量的实验表明，与竞争性的半密集匹配器相比，我们的方法可以实现更高的精度，并具有可观的效率效益。这为大规模或延迟敏感的应用（如图像检索和3D重建）开辟了令人兴奋的前景。项目页面：https://zju3dv.github.io/efficientloftr. et.al.|[2403.04765](http://arxiv.org/abs/2403.04765)|null|
|**2024-03-08**|**Finding Waldo: Towards Efficient Exploration of NeRF Scene Spaces**|近年来，神经辐射场（NeRF）以其卓越的性能迅速成为三维重建和新视图合成的主要方法。尽管人们对NeRF方法非常感兴趣，但NeRF的一个实际用例在很大程度上被忽视了；由NeRF建模的场景空间的探索。在本文中，我们在文献中首次提出并正式定义场景探索框架为NeRF模型输入（即坐标和视角）的有效发现，使用该框架可以呈现符合用户选择标准的新颖视图，我们首先提出了两种基线方法，称为引导随机搜索（GRS）和基于姿态插值的搜索（PIBS）。然后，我们将场景探索视为一个优化问题，并提出了标准不可知的进化引导姿势搜索（EGPS）来进行有效的探索。我们用各种标准（例如显著性最大化、图像质量最大化、照片构图质量改进）测试了所有三种方法，并表明我们的EGPS比其他基线表现得更好。最后，我们强调了场景探索的重点和局限性，并概述了未来研究的方向。 et.al.|[2403.04508](http://arxiv.org/abs/2403.04508)|null|
|**2024-03-07**|**CN-RMA: Combined Network with Ray Marching Aggregation for 3D Indoors Object Detection from Multi-view Images**|本文介绍了一种从多视角图像中检测三维室内物体的新方法CN-RMA。我们观察到关键挑战是图像和3D对应关系的模糊性，而没有明确的几何结构来提供遮挡信息。为了解决这个问题，CN-RMA利用了3D重建网络和3D对象检测网络的协同作用，其中重建网络提供了粗略的截断有符号距离函数（TSDF），并引导图像特征以端到端的方式正确地投票到3D空间。具体来说，我们通过射线行进将权重与每条射线的采样点相关联，表示图像中像素对相应3D位置的贡献。这样的权重由预测的带符号距离确定，使得图像特征仅投票给重建表面附近的区域。我们的方法在从多视图图像中检测3D对象方面实现了最先进的性能，通过mAP@0.25和mAP@0.5在ScanNet和ARKitScenes数据集上。代码和型号发布于https://github.com/SerCharles/CN-RMA. et.al.|[2403.04198](http://arxiv.org/abs/2403.04198)|**[link](https://github.com/sercharles/cn-rma)**|
|**2024-03-07**|**Radiative Gaussian Splatting for Efficient X-ray Novel View Synthesis**|X射线由于其比自然光更强的穿透性而被广泛应用于透射成像。在绘制新视图X射线投影时，现有的主要基于NeRF的方法训练时间长，推理速度慢。在本文中，我们提出了一种基于三维高斯散射的框架，即X-Gaussian，用于X射线新视图合成。首先，受X射线成像各向同性的启发，我们重新设计了一个辐射高斯点云模型。我们的模型在学习预测3D点的辐射强度时排除了视角方向的影响。基于该模型，我们开发了一种具有CUDA实现的可微分辐射光栅化（DRR）。其次，我们定制了一种角度姿态长方体均匀初始化（ACUI）策略，该策略直接使用X射线扫描仪的参数来计算相机信息，然后对包围扫描对象的长方体内的点位置进行均匀采样。实验表明，我们的X-Gaussian比最先进的方法高6.5 dB，同时享受不到15%的训练时间和超过73倍的推理速度。在稀疏视图CT重建中的应用也揭示了该方法的实用价值。代码和模型将在https://github.com/caiyuanhao1998/X-Gaussian . 培训过程可视化的视频演示位于https://www.youtube.com/watch?v=gDVf_Ngeghg . et.al.|[2403.04116](http://arxiv.org/abs/2403.04116)|**[link](https://github.com/caiyuanhao1998/x-gaussian)**|

<p align=right>(<a href=#updated-on-20240316>back to top</a>)</p>

## Diffusion

|Publish Date|Title|Abstract|PDF|Code|
|---|---|---|---|---|
|**2024-03-14**|**SCP-Diff: Photo-Realistic Semantic Image Synthesis with Spatial-Categorical Joint Prior**|语义图像合成在传感器仿真中显示出良好的前景。然而，基于GANs的当前该领域的最佳实践尚未达到所需的质量水平。随着潜在扩散模型在图像生成方面取得重大进展，我们被要求评估ControlNet，这是一种以其密集控制能力而闻名的方法。我们的调查结果揭示了两个主要问题：在大的语义区域中存在奇怪的子结构，以及内容与语义掩码的错位。通过实证研究，我们确定了这些问题的原因是噪声训练数据分布与推理阶段应用的标准正态先验之间的不匹配。为了应对这一挑战，我们为SIS开发了特定的噪声先验，包括空间、分类和一种新的用于推理的空间-分类联合先验。我们将这种方法命名为SCP-Diff，它产生了非凡的结果，在Cityscapes上实现了10.53的FID，在ADE20K上实现了12.66的FID。代码和模型可以通过项目页面访问。 et.al.|[2403.09638](http://arxiv.org/abs/2403.09638)|null|
|**2024-03-14**|**3D-VLA: A 3D Vision-Language-Action Generative World Model**|最近的视觉-语言-动作（VLA）模型依赖于2D输入，缺乏与3D物理世界更广泛领域的集成。此外，他们通过学习从感知到行动的直接映射来进行行动预测，忽略了世界的巨大动态以及行动和动态之间的关系。相比之下，人类被赋予了世界模型，这些模型描绘了对未来场景的想象，并据此计划行动。为此，我们提出了3D-VLA，通过引入一系列新的具体基础模型，通过生成世界模型将3D感知、推理和行动无缝连接起来。具体而言，3D-VLA建立在基于3D的大型语言模型（LLM）之上，并引入一组交互令牌来与具体环境互动。此外，为了将生成能力注入到模型中，我们训练了一系列具体的扩散模型，并将它们对齐到LLM中，用于预测目标图像和点云。为了训练我们的3D-VLA，我们通过从现有的机器人数据集中提取大量的3D相关信息来策划一个大规模的3D嵌入式指令数据集。我们在固定数据集上的实验表明，3D-VLA显著提高了嵌入式环境中的推理、多模式生成和规划能力，展示了其在现实世界应用中的潜力。 et.al.|[2403.09631](http://arxiv.org/abs/2403.09631)|null|
|**2024-03-14**|**Generalized Predictive Model for Autonomous Driving**|在本文中，我们介绍了自动驾驶学科中第一个大规模视频预测模型。为了消除高成本数据收集的限制，增强我们模型的泛化能力，我们从网络上获取大量数据，并将其与多样化和高质量的文本描述配对。由此产生的数据集累积了2000多个小时的驾驶视频，涵盖了世界各地不同天气条件和交通场景的地区。我们的模型被称为GenAD，继承了最近潜在扩散模型的优点，用新颖的时间推理块处理驾驶场景中具有挑战性的动力学。我们展示了它可以以零样本的方式推广到各种看不见的驾驶数据集，超过了一般或特定驾驶的视频预测同行。此外，GenAD可以适用于动作条件预测模型或运动规划器，在现实世界的驾驶应用中具有巨大潜力。 et.al.|[2403.09630](http://arxiv.org/abs/2403.09630)|null|
|**2024-03-14**|**Make-Your-3D: Fast and Consistent Subject-Driven 3D Content Generation**|近年来，3D生成模型具有强大的功能，它允许用户通过单个图像或自然语言指导3D内容生成过程，从而提供了新的创造性灵活性。然而，现有的3D生成方法在不同的提示下创建主题驱动的3D内容仍然具有挑战性。在本文中，我们介绍了一种新的3D定制方法，称为Make-Your-3D，它可以在5分钟内从具有文本描述的受试者的单个图像中个性化高保真度和一致性的3D内容。我们的关键见解是协调多视图扩散模型和身份特定的2D生成模型的分布，使其与所需3D对象的分布相一致。具体而言，我们设计了一个协同进化框架来减少分布的方差，其中每个模型分别通过身份感知优化和主题先验优化进行相互学习的过程。大量实验表明，我们的方法可以通过文本驱动的修改生成高质量、一致的、针对特定主题的3D内容，而这些修改在主题图像中是看不到的。 et.al.|[2403.09625](http://arxiv.org/abs/2403.09625)|null|
|**2024-03-14**|**Score-Guided Diffusion for 3D Human Recovery**|我们提出了分数引导的人体网格恢复（ScoreHMR），这是一种解决三维人体姿态和形状重建逆问题的方法。这些逆问题涉及将人体模型拟合到图像观测，传统上通过优化技术来解决。ScoreHMR模拟模型拟合方法，但通过在扩散模型的潜在空间中进行分数引导来实现与图像观察的对齐。训练扩散模型以捕捉给定输入图像的人体模型参数的条件分布。通过用特定任务的分数指导其去噪过程，ScoreHMR有效地解决了各种应用程序的逆问题，而无需重新训练任务不可知的扩散模型。我们在三个设置/应用程序上评估我们的方法。它们是：（一）单框架模型拟合；（ii）从多个未校准的视图重建；（iii）在视频序列中重建人类。ScoreHMR在所有设置中始终优于流行基准测试上的所有优化基线。我们的代码和模型可在https://statho.github.io/ScoreHMR. et.al.|[2403.09623](http://arxiv.org/abs/2403.09623)|**[link](https://github.com/statho/scorehmr)**|
|**2024-03-14**|**Explore In-Context Segmentation via Latent Diffusion Models**|随着视觉基础模型的引入，上下文分割越来越受到关注。大多数现有方法采用度量学习或掩蔽图像建模来建立视觉提示和输入图像查询之间的相关性。在这项工作中，我们从一个新的角度探讨了这个问题，使用了一个具有代表性的生成模型，即潜在扩散模型（LDM）。我们在扩散模型中观察到生成和分割之间存在任务差距，但LDM仍然是上下文分割的有效最小值。特别地，我们提出了两种元架构，并相应地设计了几种输出对齐和优化策略。我们进行了全面的消融研究，并根据经验发现，分割质量取决于输出对齐和上下文指令。此外，我们建立了一个新的、公平的上下文分割基准，包括图像和视频数据集。实验验证了我们方法的有效性，证明了与以前的专业模型或视觉基础模型相比，结果相当甚至更强。我们的研究表明，LDM也可以在具有挑战性的上下文分割任务中获得足够好的结果。 et.al.|[2403.09616](http://arxiv.org/abs/2403.09616)|null|
|**2024-03-14**|**Generative reconstruction of 3D volume elements for Ti-6Al-4V basketweave microstructure by optimization of CNN-based microstructural descriptors**|我们提出了一种3D体积元素（VE）的生成重建方法，用于增材制造（AM）处理的Ti-6Al-4V的数值多尺度分析。在传统的电子背向散射（EBSD）显微照片中分析了在AM处理的Ti-6Al-4V中通常占主导地位的编织物形态。之前\b{eta}-grain执行重建以利用Burgers取向关系获得观察到的晶粒的平面外取向。从2D数据中提取基于卷积神经网络（CNN）的微观结构描述符，并使用微观结构表征和重建（MCR）实现MCRpy[16]用于3D正交平面上基于截面的像素值优化。为了利用对二元系统表现最好的MCRpy，将由多达12个不同晶粒取向组成的篮编织微观结构分解为几个独立的两相系统。我们的重建捕捉到了钛网编织形态的关键特征，并与实验获得的3D数据在质量上相似。在这个阶段，在重建的组装过程中保持体积分数仍然是一个未解决的挑战。 et.al.|[2403.09609](http://arxiv.org/abs/2403.09609)|null|
|**2024-03-14**|**The effect of spatially-varying collision frequency on the development of the Rayleigh-Taylor instability**|瑞利-泰勒（RT）不稳定性普遍存在，但传统上使用理想流体模型进行研究。碰撞性在流体界面上可能会有很大的变化，之前的工作证明了动力学模型在某些碰撞状态下完全捕捉动力学的必要性。在之前的动力学模拟使用空间和时间恒定的碰撞频率的情况下，本工作使用更真实的空间变化碰撞频率对RT不稳定性进行了5维（两个空间和三个速度维度）连续动力学模拟。探讨了两个阿特伍德数碰撞变化的三种情况：低到中等、中等到高和低到高。从低到中等的情况没有表现出RT不稳定性增长，而从中等到高的情况类似于流体极限动力学情况，界面加宽偏向较低碰撞区域。这项工作的一个新贡献是低到高碰撞情况，该情况显示出通过界面的向上运动显著改变的不稳定性增长，以及由于下部区域中自由流动颗粒扩散增加而阻尼的尖峰增长。流体模型无法获得分布函数的非麦克斯韦部分对能量通量的贡献，并且在尖峰和低碰撞区域的贡献最大。增加阿特伍德数会导致更大的RT不稳定性增长和界面向上运动的减少。分布函数与麦克斯韦方程的偏差与碰撞频率成反比，并集中在流体界面附近。RT不稳定性增长的线性阶段通过考虑粘度和扩散的理论线性增长率来很好地描述。 et.al.|[2403.09591](http://arxiv.org/abs/2403.09591)|null|
|**2024-03-14**|**MambaTalk: Efficient Holistic Gesture Synthesis with Selective State Space Models**|手势合成是人机交互的一个重要领域，在电影、机器人和虚拟现实等各个领域都有广泛的应用。最近的进展已经利用扩散模型和注意力机制来改进手势合成。然而，由于这些技术的高计算复杂性，生成具有低延迟的长而多样的序列仍然是一个挑战。我们探索了状态空间模型（SSM）解决这一挑战的潜力，实现了具有离散运动先验的两阶段建模策略，以提高手势的质量。利用基础Mamba区块，我们引入MambaTalk，通过多模式集成增强手势多样性和节奏。大量实验表明，我们的方法与最先进的模型的性能相匹配或超过了这些模型的性能。 et.al.|[2403.09471](http://arxiv.org/abs/2403.09471)|null|
|**2024-03-14**|**Eta Inversion: Designing an Optimal Eta Function for Diffusion-based Real Image Editing**|扩散模型在文本引导图像生成领域以及最近在文本引导的图像编辑领域取得了显著的成功。编辑真实图像的常用策略包括反转扩散过程以获得原始图像的噪声表示，然后对其进行去噪以实现所需的编辑。然而，当前的扩散反转方法往往难以产生既忠实于指定文本提示又与源图像非常相似的编辑。为了克服这些限制，我们介绍了一种用于真实图像编辑的新颖且适应性强的扩散反演技术，该技术基于对 $\eta$在DDIM采样方程中的作用的理论分析，以增强可编辑性。通过设计一种具有时间和区域相关$\eta$ 函数的通用扩散反演方法，我们能够灵活控制编辑范围。通过一系列全面的定量和定性评估，包括与一系列近期方法的比较，我们展示了我们方法的优越性。我们的方法不仅在该领域树立了新的基准，而且显著优于现有策略。我们的代码可在https://github.com/furiosa-ai/eta-inversion et.al.|[2403.09468](http://arxiv.org/abs/2403.09468)|**[link](https://github.com/furiosa-ai/eta-inversion)**|

<p align=right>(<a href=#updated-on-20240316>back to top</a>)</p>

## NeRF

|Publish Date|Title|Abstract|PDF|Code|
|---|---|---|---|---|
|**2024-03-13**|**Representing Anatomical Trees by Denoising Diffusion of Implicit Neural Fields**|解剖树在临床诊断和治疗计划中起着核心作用。然而，由于解剖树的拓扑结构和几何形状多变且复杂，因此准确地表示解剖树具有挑战性。使用医学成像捕获的表示树状结构的传统方法虽然对可视化血管和支气管网络非常宝贵，但在分辨率、灵活性和效率方面存在缺陷。最近，隐式神经表示（INRs）已经成为准确有效地表示形状的强大工具。我们提出了一种使用INR表示解剖树的新方法，同时还通过INR空间中的去噪扩散来捕捉一组树的分布。我们以任何所需的分辨率准确捕捉解剖树的复杂几何形状和拓扑结构。通过广泛的定性和定量评估，我们展示了高保真度树重建，具有任意分辨率但紧凑的存储，以及跨解剖部位和树复杂性的多功能性。 et.al.|[2403.08974](http://arxiv.org/abs/2403.08974)|null|
|**2024-03-12**|**Scalable Spatiotemporal Prediction with Bayesian Neural Fields**|时空数据集由空间参考的时间序列组成，在许多科学和商业智能应用中无处不在，如空气污染监测、疾病跟踪和云需求预测。随着现代数据集的规模和复杂性不断增加，人们越来越需要新的统计方法，这些方法足够灵活，可以捕捉复杂的时空动态，并且可以扩展，可以处理大型预测问题。这项工作提出了贝叶斯神经场（BayesNF），这是一种用于推断时空域上丰富概率分布的域通用统计模型，可用于数据分析任务，包括预测、插值和变差法。BayesNF将一种用于高容量函数估计的新型深度神经网络架构与用于鲁棒不确定性量化的分层贝叶斯推理相结合。通过通过一系列平滑可微变换定义先验，使用通过随机梯度下降训练的变量学习代理对大规模数据进行后验推理。我们根据突出的统计和机器学习基线评估BayesNF，显示出在气候和公共卫生数据集的各种预测问题上的显著改进，这些数据集包含数万到数十万个测量值。该论文附有一个开源软件包(https://github.com/google/bayesnf)它易于使用，并与JAX机器学习平台上的现代GPU和TPU加速器兼容。 et.al.|[2403.07657](http://arxiv.org/abs/2403.07657)|**[link](https://github.com/google/bayesnf)**|
|**2024-03-11**|**SiLVR: Scalable Lidar-Visual Reconstruction with Neural Radiance Fields for Robotic Inspection**|我们提出了一种基于神经场的大规模重建系统，该系统融合激光雷达和视觉数据，生成几何精度高的高质量重建，并捕捉照片逼真的纹理。该系统采用了最先进的神经辐射场（NeRF）表示，还结合了激光雷达数据，这对深度和表面法线增加了强大的几何约束。我们利用实时激光雷达SLAM系统的轨迹来引导运动结构（SfM）过程，以显著减少计算时间，并提供对激光雷达深度损失至关重要的度量尺度。我们使用子映射将系统缩放到长轨迹上捕获的大规模环境。我们用多摄像头、激光雷达传感器套件的数据演示了重建系统，该套件安装在腿式机器人上，手持扫描600米的建筑场景，并安装在空中机器人上，测量多层模拟灾难现场建筑。网站https://ori-drs.github.io/projects/silvr/ et.al.|[2403.06877](http://arxiv.org/abs/2403.06877)|null|
|**2024-03-09**|**CoNFiLD: Conditional Neural Field Latent Diffusion Model Generating Spatiotemporal Turbulence**|本研究介绍了条件神经场潜在扩散（CoNFiLD）模型，这是一种新的生成学习框架，旨在快速模拟三维不规则域内混沌和湍流系统中复杂的时空动力学。传统的涡解析数值模拟，尽管提供了详细的流量预测，但由于其广泛的计算需求，遇到了很大的局限性，限制了其在更广泛的工程环境中的应用。相比之下，基于深度学习的代理模型有望提供高效、数据驱动的解决方案。然而，它们的有效性往往因依赖确定性框架而受到损害，而确定性框架在准确捕捉湍流的混沌和随机性质方面存在不足。CoNFiLD模型通过将条件神经场编码与潜在扩散过程协同集成来解决这些挑战，从而能够在不同条件下高效且稳健地生成时空湍流。利用贝叶斯条件采样，该模型可以无缝适应各种湍流生成场景，而无需再训练，涵盖从使用稀疏传感器测量的零样本全场流重建到超分辨率生成和时空流数据恢复的应用。已经对各种具有不规则几何形状的非均匀、各向异性湍流进行了全面的数值实验，以评估该模型的多功能性和有效性，展示了其在湍流生成和更广泛的时空动力学建模领域的变革潜力。 et.al.|[2403.05940](http://arxiv.org/abs/2403.05940)|null|
|**2024-03-09**|**Learned 3D volumetric recovery of clouds and its uncertainty for climate analysis**|气候预测和云物理的重大不确定性与浅层散射云的观测差距有关。应对这些挑战需要对其三维（3D）异质体积散射内容进行遥感。这就需要无源散射计算机断层扫描（CT）。我们设计了一个基于学习的模型（ProbeCT）来实现这种云的CT，基于有噪声的多视图星载图像。ProbeCT首次推断出每个3D位置的异质消光系数的后验概率分布。这产生了任意有价值的统计数据，例如，最可能灭绝的3D场及其不确定性。ProbeCT使用神经场表示，进行本质上实时的推理。ProbeCT通过一个新的基于物理的云体积场及其相应图像的标记多类数据库进行监督训练。为了改进分布外推理，我们通过差分渲染引入了自监督学习。我们在模拟和真实世界的数据中演示了该方法，并指出了3D恢复和不确定性与降水和可再生能源的相关性。 et.al.|[2403.05932](http://arxiv.org/abs/2403.05932)|null|
|**2024-03-06**|**ProxNF: Neural Field Proximal Training for High-Resolution 4D Dynamic Image Reconstruction**|精确的时空图像重建方法被广泛的生物医学研究领域所需要，但由于数据的不完整性和计算负担而面临挑战。数据不完整性源于增加帧速率和减少采集时间所需的欠采样，而计算负担则源于具有三维空间和扩展时间范围的高分辨率图像的内存占用。神经场是一类新兴的神经网络，充当时空对象的连续表示，以前已经引入它来通过将图像重建重新定义为估计网络参数的问题来解决这些动态成像问题。神经场可以通过利用这些时空对象中潜在的冗余来解决数据不完整和计算负担这两个挑战。这项工作提出了ProxNF，这是一种用于时空图像重建的新的神经场训练方法，利用近端分裂方法将涉及成像算子的计算与网络参数的更新分开。具体而言，ProxNF评估图像域中数据保真度项的（子采样）梯度，并使用完全监督学习方法来更新神经场参数。通过减少内存占用和评估成像算子的计算成本，所提出的ProxNF方法允许重建大的、高分辨率的时空图像。该方法在两项数值研究中得到了证明，这两项研究涉及解剖逼真的动态数值小鼠模型和肿瘤灌注的两室模型的虚拟动态对比增强光声计算机断层扫描成像。 et.al.|[2403.03860](http://arxiv.org/abs/2403.03860)|null|
|**2024-03-05**|**NRDF: Neural Riemannian Distance Fields for Learning Articulated Pose Priors**|忠实地为关节空间建模是一项关键任务，它可以恢复和生成逼真的姿势，而且仍然是一项臭名昭著的挑战。为此，我们引入了神经黎曼距离场（NRDF），这是一种数据驱动的先验，用于建模看似合理的关节空间，表示为高维乘积四元数空间中神经场的零级集。为了仅在正示例上训练NRDF，我们引入了一种新的采样算法，确保测地距离遵循所需的分布，从而产生一种原则性的距离场学习范式。然后，我们设计了一种投影算法，通过自适应步长黎曼优化器将任何随机姿态映射到水平集上，始终遵循关节旋转的乘积流形。NRDF可以通过反向传播和数学类比计算黎曼梯度，与最近的生成模型黎曼流匹配有关。我们在各种下游任务中，即姿态生成、基于图像的姿态估计和求解逆运动学，对照其他姿态先验对NRDF进行了全面评估，突出了NRDF的优越性能。除了人类，NRDF的多功能性还延伸到手和动物姿势，因为它可以有效地代表任何关节。 et.al.|[2403.03122](http://arxiv.org/abs/2403.03122)|null|
|**2024-03-04**|**MagicClay: Sculpting Meshes With Generative Neural Fields**|神经领域的最新发展为形状生成领域带来了非凡的能力，但它们缺乏关键的特性，例如增量控制，这是艺术作品的基本要求。另一方面，三角网格是大多数几何相关任务的选择，提供了高效和直观的控制，但不适用于神经优化。为了支持下游任务，现有技术通常提出两步方法，其中首先使用神经场生成形状，然后提取网格进行进一步处理。相反，在本文中，我们引入了一种混合方法，该方法保持网格和符号距离场（SDF）表示的一致性。使用这种表示，我们介绍了MagicClay——一种艺术家友好的工具，用于根据文本提示雕刻网格区域，同时保持其他区域不变。我们的框架仔细而有效地平衡了形状优化每一步中表示和正则化之间的一致性；依靠网格表示，我们展示了如何以更高的分辨率和更快的速度渲染SDF。此外，我们利用最近在可微网格重建方面的工作，在需要的地方自适应地分配网格中的三角形，如SDF所示。使用一个实现的原型，我们展示了与最先进的生成几何体相比的优越性，以及新颖的一致性控制，首次允许对同一网格进行基于提示的顺序编辑。 et.al.|[2403.02460](http://arxiv.org/abs/2403.02460)|null|
|**2024-03-04**|**Activity estimation via distributed measurements in an orientation sensitive neural fields model of the visual cortex**|本文在可观察性理论的框架下研究了初级视觉皮层（V1）内神经活动的在线估计。我们专注于对超体积活动建模的低维神经场，以描述V1中的活动。我们使用V1上的平均皮层活动作为测量。我们的贡献包括详细说明模型的可观察性奇点，并开发一种混合高增益观测器，该观测器在特定的激励条件下实现实际收敛，同时在生物相关性的情况下保持渐近收敛。该研究强调了模型的非线性性质与其可观测性之间的内在联系。我们还介绍了数值实验，强调了观测者的不同性质。 et.al.|[2403.01906](http://arxiv.org/abs/2403.01906)|null|
|**2024-03-02**|**Neural Field Classifiers via Target Encoding and Classification Loss**|神经场方法在计算机视觉和计算机图形学中的各种长期任务中取得了巨大进展，包括新颖的视图合成和几何重建。由于现有的神经场方法试图预测一些基于坐标的连续目标值，例如神经辐射场（NeRF）的RGB，所有这些方法都是回归模型，并通过一些回归损失进行优化。然而，对于神经场方法来说，回归模型真的比分类模型更好吗？在这项工作中，我们试图从机器学习的角度来探讨神经领域这个非常基本但被忽视的问题。我们成功地提出了一种新的神经场分类器（NFC）框架，该框架将现有的神经场方法公式化为分类任务，而不是回归任务。所提出的NFC可以通过使用新的目标编码模块和优化分类损失，轻松地将任意神经场回归器（NFR）转换为其分类变体。通过将连续回归目标编码为高维离散编码，我们自然地形成了多标签分类任务。大量的实验证明了NFC在几乎免费的额外计算成本下令人印象深刻的有效性。此外，NFC还显示出对稀疏输入、损坏图像和动态场景的鲁棒性。 et.al.|[2403.01058](http://arxiv.org/abs/2403.01058)|null|

<p align=right>(<a href=#updated-on-20240316>back to top</a>)</p>

[contributors-shield]: https://img.shields.io/github/contributors/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[contributors-url]: https://github.com/Vincentqyw/cv-arxiv-daily/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[forks-url]: https://github.com/Vincentqyw/cv-arxiv-daily/network/members
[stars-shield]: https://img.shields.io/github/stars/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[stars-url]: https://github.com/Vincentqyw/cv-arxiv-daily/stargazers
[issues-shield]: https://img.shields.io/github/issues/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[issues-url]: https://github.com/Vincentqyw/cv-arxiv-daily/issues

