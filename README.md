[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]

## Updated on 2024.03.13
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
|**2024-03-12**|**Learning Generalizable Feature Fields for Mobile Manipulation**|移动操作中的一个悬而未决的问题是如何以统一的方式表示对象和场景，以便机器人既可以在环境中导航，也可以操作对象。后者需要在理解细粒度语义的同时捕获复杂的几何体，而前者则需要捕获继承到扩展物理规模的复杂性。在这项工作中，我们提出了GeFF（可泛化特征场），这是一个场景级的可泛化神经特征场，作为实时执行的导航和操纵的统一表示。为此，我们将生成新视图合成视为预训练任务，然后通过CLIP特征提取将生成的丰富场景先验与自然语言对齐。我们通过在配备机械手的四足机器人上部署GeFF来证明这种方法的有效性。当在动态场景中执行开放词汇移动操作时，我们评估了GeFF泛化到开放集对象的能力以及运行时间。 et.al.|[2403.07563](http://arxiv.org/abs/2403.07563)|null|
|**2024-03-11**|**DNGaussian: Optimizing Sparse-View 3D Gaussian Radiance Fields with Global-Local Depth Normalization**|辐射场在从稀疏输入视图合成新视图方面表现出了令人印象深刻的性能，但主流方法的训练成本高，推理速度慢。本文介绍了DNGaussian，一种基于三维高斯辐射场的深度正则化框架，以低成本提供实时、高质量的少镜头新视图合成。我们的动机源于最近的3D高斯飞溅的高效表示和令人惊讶的质量，尽管当输入视图减少时，它会遇到几何退化。在高斯辐射场中，我们发现场景几何的这种退化主要与高斯基元的定位有关，并且可以通过深度约束来缓解。因此，我们提出了一种硬深度和软深度正则化，以在粗略的单目深度监督下恢复准确的场景几何体，同时保持细粒度的颜色外观。为了进一步细化详细的几何体重塑，我们引入了全局局部深度归一化，增强了对局部深度小变化的关注。在LLFF、DTU和Blender数据集上进行的大量实验表明，DNGaussian优于最先进的方法，实现了相当或更好的结果，显著降低了内存成本，减少了25美元的训练时间，渲染速度快了3000美元以上。 et.al.|[2403.06912](http://arxiv.org/abs/2403.06912)|**[link](https://github.com/fictionarry/dngaussian)**|
|**2024-03-11**|**FreGS: 3D Gaussian Splatting with Progressive Frequency Regularization**|三维高斯泼溅在实时新颖视图合成中取得了令人印象深刻的性能。然而，在高斯致密化过程中，它经常遭受过度重建，其中高方差图像区域仅被几个大高斯覆盖，导致渲染图像中的模糊和伪影。我们设计了一种渐进频率正则化（FreGS）技术来解决频率空间内的过重构问题。具体而言，FreGS通过利用傅立叶空间中的低通和高通滤波器可以容易地提取的低频到高频分量来执行从粗到细的高斯致密化。通过最小化渲染图像的频谱与相应的地面实况之间的差异，它实现了高质量的高斯致密化，并有效地缓解了高斯飞溅的过度重建。在多个广泛采用的基准上进行的实验（例如，Mip-NeRF360、Tanks and Temples和Deep Blending）表明，FreGS实现了卓越的新型视图合成，并始终优于最先进的视图合成。 et.al.|[2403.06908](http://arxiv.org/abs/2403.06908)|null|
|**2024-03-11**|**V3D: Video Diffusion Models are Effective 3D Generators**|3D自动生成最近引起了广泛关注。最近的方法大大加快了生成速度，但由于模型容量或3D数据有限，通常会生成不太详细的对象。受视频扩散模型最新进展的启发，我们引入了V3D，它利用预先训练的视频扩散模型的世界模拟能力来促进3D生成。为了充分释放视频扩散感知3D世界的潜力，我们进一步引入了几何一致性先验，并将视频扩散模型扩展到多视图一致的3D生成器中。得益于此，可以对最先进的视频扩散模型进行微调，以在给定单个图像的情况下生成围绕对象的360度轨道帧。通过我们量身定制的重建管道，我们可以在3分钟内生成高质量的网格或3D高斯。此外，我们的方法可以扩展到场景级的新视图合成，实现对稀疏输入视图的相机路径的精确控制。大量实验证明了该方法的优越性能，特别是在生成质量和多视图一致性方面。我们的代码可在https://github.com/heheyas/V3D et.al.|[2403.06738](http://arxiv.org/abs/2403.06738)|**[link](https://github.com/heheyas/v3d)**|
|**2024-03-11**|**Vosh: Voxel-Mesh Hybrid Representation for Real-Time View Synthesis**|神经辐射场（NeRF）已成为合成新颖视图的逼真图像的一种突出方法。虽然基于体素或网格的神经辐射表示分别提供了不同的优势，在渲染质量或速度方面都很出色，但每种方法在其他方面都有局限性。作为回应，我们提出了一种名为Vosh的开创性混合表示，在用于视图合成的混合渲染中无缝组合体素和网格组件。Vosh是通过优化NeRF的体素网格精心制作的，战略性地将选定的体素替换为网格。因此，它擅长通过网格组件快速渲染具有简单几何体和纹理的场景，同时通过利用体素组件在复杂区域实现高质量渲染。Vosh的灵活性通过调整混合比率的能力得到了展示，为用户提供了基于灵活使用控制渲染质量和速度之间平衡的能力。实验结果表明，我们的方法在渲染质量和速度之间实现了值得称赞的折衷，并且在移动设备上具有显著的实时性能。 et.al.|[2403.06505](http://arxiv.org/abs/2403.06505)|null|
|**2024-03-11**|**FSViewFusion: Few-Shots View Generation of Novel Objects**|自从NeRF出现以来，新颖的视图合成已经得到了巨大的发展。然而，Nerf模型在单个场景上过拟合，缺乏对分布外对象的泛化能力。最近，扩散模型在视图合成中引入泛化方面表现出了显著的性能。受这些进步的启发，我们探索了预训练的稳定扩散模型在没有显式3D先验的情况下进行视图合成的能力。具体来说，我们的方法基于个性化的文本到图像模型Dreambooth，因为它具有很强的能力，只需几次拍摄就可以适应特定的新颖对象。我们的研究揭示了两个有趣的发现。首先，我们观察到，与涉及对大量多视图数据进行微调扩散的更复杂的策略相比，Dreambooth可以学习视图的高级概念。其次，我们建立了一个观点的概念可以被解开并转移到一个新的对象上，而不考虑从中学习观点的原始对象的身份。受此启发，我们引入了一种学习策略FSViewFusion，该策略仅通过单个场景的一个图像样本继承特定视图，并使用低阶适配器将知识转移到从少数镜头中学习的新对象。通过广泛的实验，我们证明了我们的方法虽然简单，但在为野生图像生成可靠的视图样本方面是有效的。将发布代码和模型。 et.al.|[2403.06394](http://arxiv.org/abs/2403.06394)|null|
|**2024-03-10**|**S-DyRF: Reference-Based Stylized Radiance Fields for Dynamic Scenes**|目前的3D风格化方法往往假设场景是静态的，这违背了我们现实世界的动态本质。为了解决这一限制，我们提出了S-DyRF，这是一种基于参考的动态神经辐射场时空风格化方法。然而，由于沿时间轴的风格化参考图像的可用性有限，风格化动态3D场景本质上是具有挑战性的。我们的关键见解在于除了提供的参考之外，还引入了额外的时间线索。为此，我们从给定的程式化引用中生成时间伪引用。这些伪参考便于样式信息从参考传播到整个动态3D场景。对于粗略的样式转换，我们强制使用新颖的视图和时间，以在特征级别模拟伪引用中存在的样式细节。为了保留高频细节，我们从时间伪参考创建了一个风格化的时间伪射线集合。这些伪射线作为实现精细风格转换的详细和明确的风格化指导。在合成数据集和真实世界数据集上的实验表明，我们的方法在动态3D场景上产生了合理的时空视图合成风格化结果。 et.al.|[2403.06205](http://arxiv.org/abs/2403.06205)|null|
|**2024-03-10**|**Is Vanilla MLP in Neural Radiance Field Enough for Few-shot View Synthesis?**|神经辐射场（NeRF）通过使用多层感知（MLP）和体绘制程序对场景进行建模，在新的视图合成中实现了卓越的性能，然而，当给定的已知视图较少时（即，很少的镜头视图合成），模型容易过拟合给定的视图。为了解决这个问题，以前的努力是利用学习到的先验知识或引入额外的正则化。相反，在本文中，我们首次从网络结构的角度提供了一种正交方法。考虑到微不足道地减少模型参数的数量可以缓解过拟合问题，但以丢失细节为代价，我们提出了多输入MLP（mi-MLP），它将普通MLP的输入（即位置和观看方向）合并到每一层中，以防止过拟合问题而不损害详细合成。为了进一步减少伪影，我们建议分别对颜色和体积密度进行建模，并提出两个正则化项。在多个数据集上的大量实验表明：1）尽管所提出的mi MLP易于实现，但它的有效性令人惊讶，因为它将基线的PSNR从14.73美元提高到24.23美元。2） 总体框架在广泛的基准上取得了最先进的成果。我们将在发布后发布代码。 et.al.|[2403.06092](http://arxiv.org/abs/2403.06092)|null|
|**2024-03-09**|**Lightning NeRF: Efficient Hybrid Scene Representation for Autonomous Driving**|最近的研究强调了NeRF在自动驾驶环境中的应用前景。然而，室外环境的复杂性，加上驾驶场景中的视点受限，使精确重建场景几何体的任务变得复杂。这些挑战往往会导致重建质量下降，训练和渲染的持续时间延长。为了应对这些挑战，我们推出了Lightning NeRF。它使用了一种高效的混合场景表示，在自动驾驶场景中有效地利用了激光雷达的几何先验。Lightning NeRF显著提高了NeRF的新颖视图合成性能，并减少了计算开销。通过对真实世界数据集（如KITTI-360、Argoverse2和我们的私人数据集）的评估，我们证明了我们的方法不仅在新视图合成质量方面超过了当前最先进的技术，而且在训练速度上提高了五倍，在渲染速度上也提高了十倍。代码可在https://github.com/VISION-SJTU/Lightning-NeRF . et.al.|[2403.05907](http://arxiv.org/abs/2403.05907)|null|
|**2024-03-07**|**BAGS: Blur Agnostic Gaussian Splatting through Multi-Scale Kernel Modeling**|最近在使用3D高斯进行场景重建和新颖的视图合成方面的努力可以在精心策划的基准上取得令人印象深刻的结果；然而，在现实生活中拍摄的图像往往是模糊的。在这项工作中，我们分析了基于高斯散斑的方法对各种图像模糊的鲁棒性，如运动模糊、散焦模糊、降尺度模糊等。在这些退化情况下，基于高斯散点的方法往往比基于神经辐射场的方法过拟合并产生更差的结果。为了解决这个问题，我们提出了模糊不可知高斯飞溅（BAGS）。BAGS引入了额外的2D建模能力，从而可以在图像模糊的情况下重建3D一致性和高质量的场景。具体来说，我们通过从模糊建议网络（BPN）估计每像素卷积核来对模糊进行建模。BPN旨在考虑场景的空间、颜色和深度变化，以最大限度地提高建模能力。此外，BPN还提出了一种质量评估掩模，用于指示出现模糊的区域。最后，我们介绍了一个从粗到细的核优化方案；该优化方案速度快，避免了由于稀疏点云初始化而导致的次优解，当我们将“运动结构”应用于模糊图像时，经常会出现这种情况。我们证明，BAGS在各种具有挑战性的模糊条件和成像几何结构下实现了真实感渲染，同时显著改进了现有方法。 et.al.|[2403.04926](http://arxiv.org/abs/2403.04926)|**[link](https://github.com/snldmt/bags)**|

<p align=right>(<a href=#updated-on-20240313>back to top</a>)</p>

## 3D Reconstruction

|Publish Date|Title|Abstract|PDF|Code|
|---|---|---|---|---|
|**2024-03-11**|**Bayesian Diffusion Models for 3D Shape Reconstruction**|我们提出了贝叶斯扩散模型（BDM），这是一种通过联合扩散过程将自上而下（先验）的信息与自下而上（数据驱动）的过程紧密耦合来执行有效贝叶斯推理的预测算法。我们展示了BDM在三维形状重建任务中的有效性。与在配对（监督）数据标签（如图像点云）数据集上训练的原型深度学习数据驱动方法相比，我们的BDM从独立标签（如点云）中引入了丰富的先验信息，以改进自下而上的3D重建。与推理需要显式先验和似然的标准贝叶斯框架不同，BDM通过与学习的梯度计算网络的耦合扩散过程来执行无缝信息融合。我们BDM的特点在于它能够参与自上而下和自下而上的过程的积极有效的信息交换和融合，其中每个过程本身就是一个扩散过程。我们在3D形状重建的合成基准和真实世界基准上展示了最先进的结果。 et.al.|[2403.06973](http://arxiv.org/abs/2403.06973)|null|
|**2024-03-08**|**DITTO: Dual and Integrated Latent Topologies for Implicit 3D Reconstruction**|我们提出了一种新的对偶和集成潜在拓扑（简称DITTO）概念，用于从噪声和稀疏点云中进行隐式三维重建。大多数现有的方法主要关注单个潜在类型，如点或网格潜在。相反，所提出的DITTO利用点和网格潜伏时间（即双重潜伏时间）来增强它们的强度、网格潜伏时间的稳定性和点潜伏时间的细节丰富能力。DITTO由双隐式编码器和集成隐式解码器组成。在双潜伏编码器中，双潜伏层是构成编码器的关键模块块，它并行地细化两个潜伏，保持它们不同的形状，并实现递归交互。值得注意的是，新提出的双潜伏层内的动态稀疏点变换器有效地细化了点潜伏。然后，集成隐式解码器系统地结合了这些精细的延迟，实现了高保真度的3D重建，并在对象和场景级数据集上超越了以前最先进的方法，尤其是在薄而详细的结构中。 et.al.|[2403.05005](http://arxiv.org/abs/2403.05005)|null|
|**2024-03-11**|**Efficient LoFTR: Semi-Dense Local Feature Matching with Sparse-Like Speed**|我们提出了一种新的方法来有效地产生图像之间的半密集匹配。先前的无检测器匹配器LoFTR在处理大的视点变化和纹理较差的场景时显示出显著的匹配能力，但效率较低。我们重新审视了它的设计选择，并在效率和准确性方面进行了多项改进。一个关键的观察结果是，由于共享的局部信息，在整个特征图上执行转换是冗余的，因此我们提出了一种具有自适应令牌选择的聚合注意力机制，以提高效率。此外，我们发现LoFTR的精细相关模块存在空间方差，这不利于匹配精度。提出了一种新的两级相关层，以实现精确的亚像素对应，从而提高精度。我们的效率优化模型比LoFTR快$\sim 2.5\倍，甚至可以超过最先进的高效稀疏匹配管道SuperPoint+LightGlue。此外，大量的实验表明，与竞争性的半密集匹配器相比，我们的方法可以实现更高的精度，并具有可观的效率效益。这为大规模或延迟敏感的应用（如图像检索和3D重建）开辟了令人兴奋的前景。项目页面：https://zju3dv.github.io/efficientloftr. et.al.|[2403.04765](http://arxiv.org/abs/2403.04765)|null|
|**2024-03-08**|**Finding Waldo: Towards Efficient Exploration of NeRF Scene Spaces**|近年来，神经辐射场（NeRF）以其卓越的性能迅速成为三维重建和新视图合成的主要方法。尽管人们对NeRF方法非常感兴趣，但NeRF的一个实际用例在很大程度上被忽视了；由NeRF建模的场景空间的探索。在本文中，我们在文献中首次提出并正式定义场景探索框架为NeRF模型输入（即坐标和视角）的有效发现，使用该框架可以呈现符合用户选择标准的新颖视图，我们首先提出了两种基线方法，称为引导随机搜索（GRS）和基于姿态插值的搜索（PIBS）。然后，我们将场景探索视为一个优化问题，并提出了标准不可知的进化引导姿势搜索（EGPS）来进行有效的探索。我们用各种标准（例如显著性最大化、图像质量最大化、照片构图质量改进）测试了所有三种方法，并表明我们的EGPS比其他基线表现得更好。最后，我们强调了场景探索的重点和局限性，并概述了未来研究的方向。 et.al.|[2403.04508](http://arxiv.org/abs/2403.04508)|null|
|**2024-03-07**|**CN-RMA: Combined Network with Ray Marching Aggregation for 3D Indoors Object Detection from Multi-view Images**|本文介绍了一种从多视角图像中检测三维室内物体的新方法CN-RMA。我们观察到关键挑战是图像和3D对应关系的模糊性，而没有明确的几何结构来提供遮挡信息。为了解决这个问题，CN-RMA利用了3D重建网络和3D对象检测网络的协同作用，其中重建网络提供了粗略的截断有符号距离函数（TSDF），并引导图像特征以端到端的方式正确地投票到3D空间。具体来说，我们通过射线行进将权重与每条射线的采样点相关联，表示图像中像素对相应3D位置的贡献。这样的权重由预测的带符号距离确定，使得图像特征仅投票给重建表面附近的区域。我们的方法在从多视图图像中检测3D对象方面实现了最先进的性能，通过mAP@0.25和mAP@0.5在ScanNet和ARKitScenes数据集上。代码和型号发布于https://github.com/SerCharles/CN-RMA. et.al.|[2403.04198](http://arxiv.org/abs/2403.04198)|**[link](https://github.com/sercharles/cn-rma)**|
|**2024-03-07**|**Radiative Gaussian Splatting for Efficient X-ray Novel View Synthesis**|X射线由于其比自然光更强的穿透性而被广泛应用于透射成像。在绘制新视图X射线投影时，现有的主要基于NeRF的方法训练时间长，推理速度慢。在本文中，我们提出了一种基于三维高斯散射的框架，即X-Gaussian，用于X射线新视图合成。首先，受X射线成像各向同性的启发，我们重新设计了一个辐射高斯点云模型。我们的模型在学习预测3D点的辐射强度时排除了视角方向的影响。基于该模型，我们开发了一种具有CUDA实现的可微分辐射光栅化（DRR）。其次，我们定制了一种角度姿态长方体均匀初始化（ACUI）策略，该策略直接使用X射线扫描仪的参数来计算相机信息，然后对包围扫描对象的长方体内的点位置进行均匀采样。实验表明，我们的X-Gaussian比最先进的方法高6.5 dB，同时享受不到15%的训练时间和超过73倍的推理速度。在稀疏视图CT重建中的应用也揭示了该方法的实用价值。代码和模型将在https://github.com/caiyuanhao1998/X-Gaussian . 培训过程可视化的视频演示位于https://www.youtube.com/watch?v=gDVf_Ngeghg . et.al.|[2403.04116](http://arxiv.org/abs/2403.04116)|**[link](https://github.com/caiyuanhao1998/x-gaussian)**|
|**2024-03-05**|**Pooling Image Datasets With Multiple Covariate Shift and Imbalance**|小样本量在许多学科中很常见，这就需要在多个机构中汇集大致相似的数据集，以研究图像和疾病结果之间微弱但相关的关联。这种数据通常表现出协变量（即二次非成像数据）的偏移/不平衡。控制这种干扰变量在标准统计分析中很常见，但这些想法并不直接适用于参数过大的模型。因此，最近的工作表明，来自不变表示学习的策略是如何提供一个有意义的起点的，但目前的方法仅限于一次只考虑几个协变量的变化/不平衡。在本文中，我们展示了如何从范畴理论的角度看待这个问题，提供了一个简单有效的解决方案，完全避免了原本需要的复杂的多阶段训练管道。我们通过在真实数据集上进行的大量实验证明了这种方法的有效性。此外，我们讨论了这种形式的公式如何为至少5个以上不同的问题设置提供统一的视角，从自监督学习到3D重建中的匹配问题。 et.al.|[2403.02598](http://arxiv.org/abs/2403.02598)|null|
|**2024-03-04**|**DragTex: Generative Point-Based Texture Editing on 3D Mesh**|最近，使用生成人工智能创建3D纹理网格引起了人们的极大关注。虽然现有方法支持在3D网格上基于文本的生成纹理生成或编辑，但它们往往难以通过更直观的交互来精确控制纹理图像的像素。虽然2D图像可以使用拖动交互进行生成编辑，但将这种类型的方法直接应用于3D网格纹理仍然会导致多个视图之间缺乏局部一致性、错误累积和训练时间长等问题。为了解决这些挑战，我们提出了一种基于生成点的3D网格纹理编辑方法，称为DragTex。该方法利用扩散模型在不同视图之间混合变形轮廓附近区域中的局部不一致纹理，从而实现局部一致的纹理编辑。此外，我们对解码器进行微调，以减少非拖动区域的重建误差，从而减少总体误差积累。此外，我们使用多视图图像来训练LoRA，而不是单独训练每个视图，这显著缩短了训练时间。实验结果表明，我们的方法有效地实现了3D网格上的拖动纹理，并生成了符合拖动交互所需意图的合理纹理。 et.al.|[2403.02217](http://arxiv.org/abs/2403.02217)|null|
|**2024-03-04**|**TripoSR: Fast 3D Object Reconstruction from a Single Image**|本技术报告介绍了TripoSR，这是一种利用变压器架构进行快速前馈3D生成的3D重建模型，可在0.5秒内从单个图像生成3D网格。基于LRM网络架构，TripoSR集成了数据处理、模型设计和训练技术方面的实质性改进。对公共数据集的评估表明，与其他开源替代品相比，TripoSR在数量和质量上都表现出优异的性能。TripoSR是根据麻省理工学院的许可发布的，旨在为研究人员、开发人员和创意人员提供3D生成人工智能的最新进展。 et.al.|[2403.02151](http://arxiv.org/abs/2403.02151)|**[link](https://github.com/vast-ai-research/triposr)**|
|**2024-03-03**|**A Novel Dynamic Light-Section 3D Reconstruction Method for Wide-Range Sensing**|现有的基于检流计的激光扫描系统在多尺度3D重建中的应用具有挑战性，因为难以在高重建精度和宽重建范围之间实现平衡。本文提出了一种新的方法，通过使用多电流计切换相机的视场来同步激光扫描。除了先进的硬件设置外，我们还通过建模动态相机、动态激光器及其组合交互，建立了系统的综合数学模型。然后，我们通过构建误差模型并最小化目标函数，提出了一种高精度、灵活的校准方法。最后，我们通过扫描标准组件来评估所提出的系统的性能。评估结果表明，当测量范围扩展到1100 mm $\times$1300 mm$\imes$ 650 mm时，所提出的三维重建系统的精度达到0.3 mm。在相同的重建精度下，重建范围扩展了25倍，表明所提出的方法同时允许在工业应用中进行高精度和宽范围的3D重建。 et.al.|[2403.01374](http://arxiv.org/abs/2403.01374)|null|

<p align=right>(<a href=#updated-on-20240313>back to top</a>)</p>

## Diffusion

|Publish Date|Title|Abstract|PDF|Code|
|---|---|---|---|---|
|**2024-03-12**|**Bridging Different Language Models and Generative Vision Models for Text-to-Image Generation**|随着文本到图像扩散模型的引入，文本到图像的生成取得了重大进展。这些模型通常由解释用户提示的语言模型和生成相应图像的视觉模型组成。随着语言和视觉模型在各自领域的不断发展，探索用更先进的模型替换文本到图像扩散模型中的组件具有巨大的潜力。因此，更广泛的研究目标是研究任何两种不相关的语言和生成视觉模型在文本到图像生成中的集成。在本文中，我们探索了这一目标，并提出了LaVi Bridge，这是一个能够集成各种预先训练的语言模型和生成视觉模型的管道，用于文本到图像的生成。通过利用LoRA和适配器，LaVi-Bridge提供了一种灵活的即插即用方法，无需修改语言和视觉模型的原始权重。我们的管道与各种语言模型和生成视觉模型兼容，适应不同的结构。在这个框架内，我们证明，结合更高级的语言模型或生成视觉模型等高级模块，可以显著提高文本对齐或图像质量等功能。已经进行了广泛的评估，以验证拉维大桥的有效性。代码位于https://github.com/ShihaoZhaoZSH/LaVi-Bridge. et.al.|[2403.07860](http://arxiv.org/abs/2403.07860)|**[link](https://github.com/shihaozhaozsh/lavi-bridge)**|
|**2024-03-12**|**Quantifying and Mitigating Privacy Risks for Tabular Generative Models**|来自生成模型的合成数据成为保护隐私的数据共享解决方案。这种合成数据集应与原始数据相似，而不会泄露可识别的私人信息。表格合成器的主干技术植根于图像生成模型，从生成对抗性网络（GANs）到最近的扩散模型。最近的先前工作揭示了表格数据的效用-隐私权衡，揭示和量化了合成数据的隐私风险。我们首先进行了详尽的实证分析，强调了五种最先进的表格合成器在对抗八种隐私攻击时的效用-隐私权衡，特别关注成员推断攻击。基于对表格扩散中高数据质量和高隐私风险的观察，我们提出了DP-TLDM，即差分私有表格潜在扩散模型，该模型由用于编码表格数据的自动编码器网络和用于合成潜在表格的潜在扩散模型组成。根据新兴的f-DP框架，我们将DP-SGD应用于结合批量裁剪训练自动编码器，并使用分离值作为隐私度量，以更好地捕捉DP算法的隐私增益。我们的实证评估表明，DP-TLDM能够实现有意义的理论隐私保障，同时显著提高合成数据的实用性。具体而言，与其他受DP保护的表格生成模型相比，DP-TLDM在数据相似性方面平均提高了35%，在下游任务的实用性方面平均改善了15%，在数据可分辨性方面平均改进了50%，同时保持了相当水平的隐私风险。 et.al.|[2403.07842](http://arxiv.org/abs/2403.07842)|null|
|**2024-03-12**|**MPCPA: Multi-Center Privacy Computing with Predictions Aggregation based on Denoising Diffusion Probabilistic Model**|在医疗保健和金融等许多应用中，隐私保护计算对于多中心机器学习至关重要。本文提出了一种基于去噪扩散概率模型（DDPM）的多中心预测聚合隐私计算框架（MPCPA），其中包括条件扩散模型训练、DDPM数据生成、分类器和预测聚合策略。与联合学习相比，该框架需要更少的通信，并利用高质量的生成数据来支持强大的隐私计算。跨多个数据集的实验验证表明，所提出的框架优于经典的联合学习，并接近原始数据集中学习的性能。此外，我们的方法展示了强大的安全性，有效地解决了图像记忆和成员推断攻击等挑战。我们的实验强调了所提出的框架在隐私计算领域的有效性，代码集将很快发布。 et.al.|[2403.07838](http://arxiv.org/abs/2403.07838)|null|
|**2024-03-12**|**Fragmentation of Dense Rotation-Dominated Structures Fed by Collapsing Gravomagneto-Sheetlets and Origin of Misaligned 100 au-Scale Binaries and Multiple Systems**|大多数恒星都在双星/多系统中。在存在非理想MHD效应的情况下，这种系统是如何在分子云的湍流磁化核心中形成的，目前还没有得到充分的探索。通过基于ATHENA++的具有双极扩散的非理想MHD AMR模拟，我们表明坍缩的原恒星包络由致密的全磁薄片主导，这是由引力坍缩的各向异性磁阻产生的经典伪盘的湍流翘曲版本，与之前对湍流磁化单恒星形成的模拟一致。小型张将质量、磁场和角动量提供给密集ROD结构，该结构分裂成二元/多个系统。这种DROD碎片场景是二元/多重形成的传统圆盘碎片场景的一种更动态的变体，由高度结构化的大型小型张体的不均匀进给产生密集的螺旋丝，而不是由磁制动主导的角动量传输的需要。致密螺旋丝之间的碰撞在将局部磁Toomre参数 $Q_\mathrm{m}$推至1以下方面发挥着关键作用，如果局部材料充分消磁，等离子体-$\beta$ 的数量级或更高，则会导致引力坍缩和恒星伴星形成。这种机制可以自然地在100 au尺度上产生错位系统，通常通过高分辨率ALMA观测来检测。我们的模拟还强调了非理想MHD效应的重要性，它影响是否发生碎裂，如果发生碎裂，还会影响形成的恒星伴星的质量和轨道参数。 et.al.|[2403.07777](http://arxiv.org/abs/2403.07777)|null|
|**2024-03-12**|**SemCity: Semantic Scene Generation with Triplane Diffusion**|我们介绍了“SemCity”，这是一个用于在真实世界户外环境中生成语义场景的3D扩散模型。大多数3D扩散模型专注于生成单个对象、合成室内场景或合成室外场景，而很少涉及真实世界室外场景的生成。在本文中，我们专注于通过在真实世界的户外数据集上学习扩散模型来生成真实的户外场景。与合成数据相比，由于传感器的限制，真实的室外数据集通常包含更多的空白空间，这给学习真实的室外分布带来了挑战。为了解决这个问题，我们利用三平面表示作为场景分布的代理形式，通过我们的扩散模型来学习。此外，我们提出了一种与我们的三平面扩散模型无缝集成的三平面操作。该操作提高了我们的扩散模型在与室外场景生成相关的各种下游任务中的适用性，如场景修复、场景外画和语义场景完成细化。在实验结果中，我们证明，与真实户外数据集SemanticKITTI中的现有工作相比，我们的三平面扩散模型显示出有意义的生成结果。我们还展示了我们的三平面操纵有助于无缝添加、移除或修改场景中的对象。此外，它还能够将场景扩展到城市级别的规模。最后，我们评估了我们的语义场景完成细化方法，其中我们的扩散模型通过学习场景分布来增强语义场景完成网络的预测。我们的代码可在https://github.com/zoomin-lee/SemCity. et.al.|[2403.07773](http://arxiv.org/abs/2403.07773)|**[link](https://github.com/zoomin-lee/semcity)**|
|**2024-03-12**|**A first principles study of the Stark shift effect on the zero-phonon line of the NV center in diamond**|半导体中的点缺陷是量子信息科学应用的有吸引力的候选者，因为它们能够充当自旋光子界面或单光子发射器。然而，电子激发时偶极矩的变化与缺陷附近的杂散电场之间的耦合，这种效应被称为斯塔克位移，可以在发射的光子中引起显著的光谱扩散。在这项工作中，使用第一性原理计算，我们重新审视了计算点缺陷的斯塔克位移到二阶的方法。该方法包括在平板中的缺陷上施加电场，并监测通过约束轨道占据（约束DFT）获得的计算零声子线的变化（即基态和激发态之间的能量差）。我们用这种平板方法研究了金刚石中带负电荷的氮空位（NV）中心的斯塔克位移。我们讨论并比较了确保平板中带负电荷缺陷的两种方法，并表明可以获得通过基态和激发态之间的偶极矩变化（ $\Delta\mu$）测量的斯塔克位移的收敛值。我们使用半局部GGA-PBE函数获得$\Delta\mu$=2.68D的斯塔克位移，使用HSE混合函数获得$\Delta\mu$=2.23D的斯塔克偏移。平板计算的结果与现代极化理论获得的结果显著不同（对于GGA-PBE，$\Delta\mu$ =4.34D），这表明至少在某些代码中，约束DFT和现代极化理论的组合存在潜在问题。 et.al.|[2403.07771](http://arxiv.org/abs/2403.07771)|null|
|**2024-03-12**|**Stable-Makeup: When Real-World Makeup Transfer Meets Diffusion Model**|目前的化妆转移方法仅限于简单的化妆风格，因此很难在现实世界中应用。在本文中，我们介绍了稳定化妆，这是一种新的基于扩散的化妆转移方法，能够将广泛的真实世界化妆稳健地转移到用户提供的脸上。稳定化妆基于预先训练的扩散模型，并利用细节保持（D-P）化妆编码器对化妆细节进行编码。它还使用内容和结构控制模块来保存源图像的内容和结构信息。借助我们在U-Net中新添加的化妆交叉关注层，我们可以将详细的化妆准确地转移到源图像中的相应位置。经过内容结构解耦训练后，Stable Makeup可以保持源图像的内容和面部结构。此外，我们的方法具有很强的鲁棒性和可推广性，适用于各种任务，如跨域化妆转移、化妆引导的文本到图像生成等。大量实验表明，我们的算法提供了最先进的（SOTA）结果在现有的化妆转移方法中表现出很有前途，在各个相关领域具有广泛的应用潜力。 et.al.|[2403.07764](http://arxiv.org/abs/2403.07764)|null|
|**2024-03-12**|**Visual Decoding and Reconstruction via EEG Embeddings with Guided Diffusion**|如何通过神经信号解码人类视觉吸引了神经科学和机器学习的长期兴趣。现代对比学习和生成模型提高了基于功能磁共振成像的视觉解码和重建的性能。然而，功能磁共振成像的高成本和低时间分辨率限制了其在脑机接口（BCI）中的应用，促使人们对基于脑电的视觉重建提出了更高的要求。在这项研究中，我们提出了一个基于脑电的视觉重建框架。它包括一个称为自适应思维映射器（ATM）的即插即用脑电编码器，它与图像嵌入对齐，以及一个两阶段的脑电引导图像生成器，该生成器首先将脑电特征转换为图像先验，然后使用预训练的图像生成器重建视觉刺激。我们的方法允许EEG嵌入在图像分类和检索任务中实现卓越的性能。我们的两阶段图像生成策略生动地重建了人类看到的图像。此外，我们还分析了来自不同时间窗口和大脑区域的信号对解码和重建的影响。我们的框架的多功能性在脑磁图（MEG）数据模式中得到了证明。我们报告称，基于脑电的视觉解码实现了SOTA性能，突出了脑电的可移植性、低成本和高时间分辨率，实现了广泛的脑机接口应用。ATM的代码可在https://anonymous.4open.science/status/EEG_Image_decode-DEEF. et.al.|[2403.07721](http://arxiv.org/abs/2403.07721)|null|
|**2024-03-12**|**SSM Meets Video Diffusion Models: Efficient Video Generation with Structured State Spaces**|鉴于通过扩散模型生成图像的显著成就，研究界对将这些模型扩展到视频生成越来越感兴趣。最近用于视频生成的扩散模型主要利用注意力层来提取时间特征。然而，注意力层受到其内存消耗的限制，内存消耗随着序列长度的二次方增加。当试图使用扩散模型生成更长的视频序列时，这种限制带来了重大挑战。为了克服这一挑战，我们建议利用状态空间模型（SSM）。SSM由于其相对于序列长度的线性内存消耗，最近作为可行的替代方案而受到关注。在实验中，我们首先用视频生成的标准基准UCF101来评估我们的基于SSM的模型。此外，为了研究SSM用于更长视频生成的潜力，我们使用MineRL Navigate数据集进行了一项实验，将帧数更改为64和150。在这些设置中，我们基于SSM的模型可以显著节省较长序列的内存消耗，同时保持与基于注意力的模型相比具有竞争力的FVD分数。我们的代码可在https://github.com/shim0114/SSM-Meets-Video-Diffusion-Models. et.al.|[2403.07711](http://arxiv.org/abs/2403.07711)|**[link](https://github.com/shim0114/ssm-meets-video-diffusion-models)**|
|**2024-03-12**|**Genuine Knowledge from Practice: Diffusion Test-Time Adaptation for Video Adverse Weather Removal**|现实世界中的视觉任务经常会出现意想不到的不利天气条件，包括雨、雾、雪和雨滴。在过去的十年里，卷积神经网络和视觉转换器在单天气视频去除方面取得了突出的成果。然而，由于缺乏适当的适应，它们大多无法推广到其他天气条件。尽管ViWS-Net被提议用一组预先训练的权重来消除视频中的不利天气条件，但它在训练时被可见的天气严重蒙蔽，在测试期间遇到看不见的天气时会退化。在这项工作中，我们将测试时间自适应引入视频中的不利天气去除，并提出了第一个将测试时间适应性集成到迭代扩散反向过程中的框架。具体来说，我们设计了一种具有新的时间噪声模型的基于扩散的网络，以在训练阶段有效地探索退化视频片段中的帧相关信息。在推理阶段，我们引入了一个名为Diffusion Tubelet Self Calibration的代理任务来学习测试视频流的引物分布，并通过近似时间噪声模型来优化模型以进行在线自适应。在基准数据集上的实验结果表明，我们的基于扩散网络的测试时间自适应方法（Diff-TTA）在恢复因可见天气条件而退化的视频方面优于最先进的方法。在合成视频和真实世界视频中，它的可推广能力也通过看不见的天气条件得到了验证。 et.al.|[2403.07684](http://arxiv.org/abs/2403.07684)|null|

<p align=right>(<a href=#updated-on-20240313>back to top</a>)</p>

## NeRF

|Publish Date|Title|Abstract|PDF|Code|
|---|---|---|---|---|
|**2024-03-12**|**Scalable Spatiotemporal Prediction with Bayesian Neural Fields**|时空数据集由空间参考的时间序列组成，在许多科学和商业智能应用中无处不在，如空气污染监测、疾病跟踪和云需求预测。随着现代数据集的规模和复杂性不断增加，人们越来越需要新的统计方法，这些方法足够灵活，可以捕捉复杂的时空动态，并且可以扩展，可以处理大型预测问题。这项工作提出了贝叶斯神经场（BayesNF），这是一种用于推断时空域上丰富概率分布的域通用统计模型，可用于数据分析任务，包括预测、插值和变差法。BayesNF将一种用于高容量函数估计的新型深度神经网络架构与用于鲁棒不确定性量化的分层贝叶斯推理相结合。通过通过一系列平滑可微变换定义先验，使用通过随机梯度下降训练的变量学习代理对大规模数据进行后验推理。我们根据突出的统计和机器学习基线评估BayesNF，显示出在气候和公共卫生数据集的各种预测问题上的显著改进，这些数据集包含数万到数十万个测量值。该论文附有一个开源软件包(https://github.com/google/bayesnf)它易于使用，并与JAX机器学习平台上的现代GPU和TPU加速器兼容。 et.al.|[2403.07657](http://arxiv.org/abs/2403.07657)|**[link](https://github.com/google/bayesnf)**|
|**2024-03-11**|**SiLVR: Scalable Lidar-Visual Reconstruction with Neural Radiance Fields for Robotic Inspection**|我们提出了一种基于神经场的大规模重建系统，该系统融合激光雷达和视觉数据，生成几何精度高的高质量重建，并捕捉照片逼真的纹理。该系统采用了最先进的神经辐射场（NeRF）表示，还结合了激光雷达数据，这对深度和表面法线增加了强大的几何约束。我们利用实时激光雷达SLAM系统的轨迹来引导运动结构（SfM）过程，以显著减少计算时间，并提供对激光雷达深度损失至关重要的度量尺度。我们使用子映射将系统缩放到长轨迹上捕获的大规模环境。我们用多摄像头、激光雷达传感器套件的数据演示了重建系统，该套件安装在腿式机器人上，手持扫描600米的建筑场景，并安装在空中机器人上，测量多层模拟灾难现场建筑。网站https://ori-drs.github.io/projects/silvr/ et.al.|[2403.06877](http://arxiv.org/abs/2403.06877)|null|
|**2024-03-09**|**CoNFiLD: Conditional Neural Field Latent Diffusion Model Generating Spatiotemporal Turbulence**|本研究介绍了条件神经场潜在扩散（CoNFiLD）模型，这是一种新的生成学习框架，旨在快速模拟三维不规则域内混沌和湍流系统中复杂的时空动力学。传统的涡解析数值模拟，尽管提供了详细的流量预测，但由于其广泛的计算需求，遇到了很大的局限性，限制了其在更广泛的工程环境中的应用。相比之下，基于深度学习的代理模型有望提供高效、数据驱动的解决方案。然而，它们的有效性往往因依赖确定性框架而受到损害，而确定性框架在准确捕捉湍流的混沌和随机性质方面存在不足。CoNFiLD模型通过将条件神经场编码与潜在扩散过程协同集成来解决这些挑战，从而能够在不同条件下高效且稳健地生成时空湍流。利用贝叶斯条件采样，该模型可以无缝适应各种湍流生成场景，而无需再训练，涵盖从使用稀疏传感器测量的零样本全场流重建到超分辨率生成和时空流数据恢复的应用。已经对各种具有不规则几何形状的非均匀、各向异性湍流进行了全面的数值实验，以评估该模型的多功能性和有效性，展示了其在湍流生成和更广泛的时空动力学建模领域的变革潜力。 et.al.|[2403.05940](http://arxiv.org/abs/2403.05940)|null|
|**2024-03-09**|**Learned 3D volumetric recovery of clouds and its uncertainty for climate analysis**|气候预测和云物理的重大不确定性与浅层散射云的观测差距有关。应对这些挑战需要对其三维（3D）异质体积散射内容进行遥感。这就需要无源散射计算机断层扫描（CT）。我们设计了一个基于学习的模型（ProbeCT）来实现这种云的CT，基于有噪声的多视图星载图像。ProbeCT首次推断出每个3D位置的异质消光系数的后验概率分布。这产生了任意有价值的统计数据，例如，最可能灭绝的3D场及其不确定性。ProbeCT使用神经场表示，进行本质上实时的推理。ProbeCT通过一个新的基于物理的云体积场及其相应图像的标记多类数据库进行监督训练。为了改进分布外推理，我们通过差分渲染引入了自监督学习。我们在模拟和真实世界的数据中演示了该方法，并指出了3D恢复和不确定性与降水和可再生能源的相关性。 et.al.|[2403.05932](http://arxiv.org/abs/2403.05932)|null|
|**2024-03-06**|**ProxNF: Neural Field Proximal Training for High-Resolution 4D Dynamic Image Reconstruction**|精确的时空图像重建方法被广泛的生物医学研究领域所需要，但由于数据的不完整性和计算负担而面临挑战。数据不完整性源于增加帧速率和减少采集时间所需的欠采样，而计算负担则源于具有三维空间和扩展时间范围的高分辨率图像的内存占用。神经场是一类新兴的神经网络，充当时空对象的连续表示，以前已经引入它来通过将图像重建重新定义为估计网络参数的问题来解决这些动态成像问题。神经场可以通过利用这些时空对象中潜在的冗余来解决数据不完整和计算负担这两个挑战。这项工作提出了ProxNF，这是一种用于时空图像重建的新的神经场训练方法，利用近端分裂方法将涉及成像算子的计算与网络参数的更新分开。具体而言，ProxNF评估图像域中数据保真度项的（子采样）梯度，并使用完全监督学习方法来更新神经场参数。通过减少内存占用和评估成像算子的计算成本，所提出的ProxNF方法允许重建大的、高分辨率的时空图像。该方法在两项数值研究中得到了证明，这两项研究涉及解剖逼真的动态数值小鼠模型和肿瘤灌注的两室模型的虚拟动态对比增强光声计算机断层扫描成像。 et.al.|[2403.03860](http://arxiv.org/abs/2403.03860)|null|
|**2024-03-05**|**NRDF: Neural Riemannian Distance Fields for Learning Articulated Pose Priors**|忠实地为关节空间建模是一项关键任务，它可以恢复和生成逼真的姿势，而且仍然是一项臭名昭著的挑战。为此，我们引入了神经黎曼距离场（NRDF），这是一种数据驱动的先验，用于建模看似合理的关节空间，表示为高维乘积四元数空间中神经场的零级集。为了仅在正示例上训练NRDF，我们引入了一种新的采样算法，确保测地距离遵循所需的分布，从而产生一种原则性的距离场学习范式。然后，我们设计了一种投影算法，通过自适应步长黎曼优化器将任何随机姿态映射到水平集上，始终遵循关节旋转的乘积流形。NRDF可以通过反向传播和数学类比计算黎曼梯度，与最近的生成模型黎曼流匹配有关。我们在各种下游任务中，即姿态生成、基于图像的姿态估计和求解逆运动学，对照其他姿态先验对NRDF进行了全面评估，突出了NRDF的优越性能。除了人类，NRDF的多功能性还延伸到手和动物姿势，因为它可以有效地代表任何关节。 et.al.|[2403.03122](http://arxiv.org/abs/2403.03122)|null|
|**2024-03-04**|**MagicClay: Sculpting Meshes With Generative Neural Fields**|神经领域的最新发展为形状生成领域带来了非凡的能力，但它们缺乏关键的特性，例如增量控制，这是艺术作品的基本要求。另一方面，三角网格是大多数几何相关任务的选择，提供了高效和直观的控制，但不适用于神经优化。为了支持下游任务，现有技术通常提出两步方法，其中首先使用神经场生成形状，然后提取网格进行进一步处理。相反，在本文中，我们引入了一种混合方法，该方法保持网格和符号距离场（SDF）表示的一致性。使用这种表示，我们介绍了MagicClay——一种艺术家友好的工具，用于根据文本提示雕刻网格区域，同时保持其他区域不变。我们的框架仔细而有效地平衡了形状优化每一步中表示和正则化之间的一致性；依靠网格表示，我们展示了如何以更高的分辨率和更快的速度渲染SDF。此外，我们利用最近在可微网格重建方面的工作，在需要的地方自适应地分配网格中的三角形，如SDF所示。使用一个实现的原型，我们展示了与最先进的生成几何体相比的优越性，以及新颖的一致性控制，首次允许对同一网格进行基于提示的顺序编辑。 et.al.|[2403.02460](http://arxiv.org/abs/2403.02460)|null|
|**2024-03-04**|**Activity estimation via distributed measurements in an orientation sensitive neural fields model of the visual cortex**|本文在可观察性理论的框架下研究了初级视觉皮层（V1）内神经活动的在线估计。我们专注于对超体积活动建模的低维神经场，以描述V1中的活动。我们使用V1上的平均皮层活动作为测量。我们的贡献包括详细说明模型的可观察性奇点，并开发一种混合高增益观测器，该观测器在特定的激励条件下实现实际收敛，同时在生物相关性的情况下保持渐近收敛。该研究强调了模型的非线性性质与其可观测性之间的内在联系。我们还介绍了数值实验，强调了观测者的不同性质。 et.al.|[2403.01906](http://arxiv.org/abs/2403.01906)|null|
|**2024-03-02**|**Neural Field Classifiers via Target Encoding and Classification Loss**|神经场方法在计算机视觉和计算机图形学中的各种长期任务中取得了巨大进展，包括新颖的视图合成和几何重建。由于现有的神经场方法试图预测一些基于坐标的连续目标值，例如神经辐射场（NeRF）的RGB，所有这些方法都是回归模型，并通过一些回归损失进行优化。然而，对于神经场方法来说，回归模型真的比分类模型更好吗？在这项工作中，我们试图从机器学习的角度来探讨神经领域这个非常基本但被忽视的问题。我们成功地提出了一种新的神经场分类器（NFC）框架，该框架将现有的神经场方法公式化为分类任务，而不是回归任务。所提出的NFC可以通过使用新的目标编码模块和优化分类损失，轻松地将任意神经场回归器（NFR）转换为其分类变体。通过将连续回归目标编码为高维离散编码，我们自然地形成了多标签分类任务。大量的实验证明了NFC在几乎免费的额外计算成本下令人印象深刻的有效性。此外，NFC还显示出对稀疏输入、损坏图像和动态场景的鲁棒性。 et.al.|[2403.01058](http://arxiv.org/abs/2403.01058)|null|
|**2024-02-28**|**NERV++: An Enhanced Implicit Neural Video Representation**|神经场，也称为隐式神经表示（INRs），在表示、生成和操作各种数据类型方面表现出了非凡的能力，允许在低内存占用下进行连续的数据重建。尽管前景广阔，但应用于视频压缩的INRs仍需要大幅度提高其率失真性能，并且需要大量的参数和长时间的训练迭代来捕捉高频细节，这限制了其更广泛的适用性。解决这个问题仍然是一项极具挑战性的任务，这将使INR在压缩任务中更容易访问。我们通过引入视频的神经表示NeRV++朝着解决这些缺点迈出了一步，NeRV++是一种增强的隐式神经视频表示，是对原始NeRV解码器架构的更直接但有效的增强，其特征是夹着上采样块（UB）的可分离conv2d残差块（SCRB），以及用于改进特征表示的双线性插值跳过层。NeRV++允许将视频直接表示为神经网络近似的函数，并显著增强了当前基于INR的视频编解码器之外的表示能力。我们在UVG、MCL-JVC和Bunny数据集上评估了我们的方法，在INRs的视频压缩方面取得了有竞争力的结果。这一成果缩小了与基于自动编码器的视频编码的差距，标志着基于INR的视频压缩研究迈出了重要一步。 et.al.|[2402.18305](http://arxiv.org/abs/2402.18305)|null|

<p align=right>(<a href=#updated-on-20240313>back to top</a>)</p>

[contributors-shield]: https://img.shields.io/github/contributors/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[contributors-url]: https://github.com/Vincentqyw/cv-arxiv-daily/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[forks-url]: https://github.com/Vincentqyw/cv-arxiv-daily/network/members
[stars-shield]: https://img.shields.io/github/stars/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[stars-url]: https://github.com/Vincentqyw/cv-arxiv-daily/stargazers
[issues-shield]: https://img.shields.io/github/issues/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[issues-url]: https://github.com/Vincentqyw/cv-arxiv-daily/issues

