[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]

## Updated on 2023.10.09
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
|**2023-10-06**|**Improving Neural Radiance Field using Near-Surface Sampling with Point Cloud Generation**|神经辐射场（NeRF）是一种新兴的视图合成方法，它对三维空间中的点进行采样，并估计它们的存在和颜色概率。NeRF的缺点是它需要很长的训练时间，因为它对许多3D点进行采样。此外，如果从遮挡区域或在不太可能存在对象的空间中采样点，则NeRF的渲染质量可能会降低。这些问题可以通过估计3D场景的几何形状来解决。本文提出了一种近表面采样框架来提高NeRF的渲染质量。为此，所提出的方法使用训练集的深度图像来估计3D对象的表面，并且仅在那里执行采样。为了获得新视图的深度信息，本文提出了一种三维点云生成方法和一种简单的点云投影深度细化方法。实验结果表明，与原始的NeRF和最先进的基于深度的NeRF方法相比，所提出的近表面采样NeRF框架可以显著提高渲染质量。此外，使用所提出的近表面采样框架，可以显著加快NeRF模型的训练时间。 et.al.|[2310.04152](http://arxiv.org/abs/2310.04152)|null|
|**2023-10-06**|**ILSH: The Imperial Light-Stage Head Dataset for Human Head View Synthesis**|本文介绍了Imperial Light Stage Head（ILSH）数据集，这是一个新颖的Light Stage捕获的人头数据集，旨在支持人头的视图合成学术挑战。ILSH数据集旨在促进各种方法，如场景特定或通用神经渲染、多视图几何、3D视觉和计算机图形学，以进一步推动照片逼真的人类化身的开发。本文详细介绍了专门用于捕捉高分辨率（4K）人头图像的光台的设置，并描述了在收集高质量数据时应对挑战（预处理、道德问题）的过程。除了数据收集之外，我们还将数据集拆分为训练集、验证集和测试集。我们的目标是为这个新的数据集设计和支持一个公平视图综合挑战任务，以便在使用测试集时，如在使用验证集时，可以保持和预期类似的性能水平。ILSH数据集由52名受试者组成，这些受试者使用24台相机拍摄，所有82个光源都打开，共产生1248张特写头部图像、边界遮罩和相机姿势对。 et.al.|[2310.03952](http://arxiv.org/abs/2310.03952)|null|
|**2023-10-05**|**Drag View: Generalizable Novel View Synthesis with Unposed Imagery**|我们介绍了DragView，这是一个新颖的交互式框架，用于生成看不见的场景的新颖视图。DragView从单个源图像初始化新视图，渲染由一组稀疏的未聚焦多视图图像支持，所有这些图像都在一个前馈过程中无缝执行。我们的方法从用户通过本地相对坐标系拖动源视图开始。像素对齐特征是通过将采样的3D点沿着目标射线投影到源视图上而获得的。然后，我们结合了一个与视图相关的调制层，以在投影过程中有效地处理遮挡。此外，我们将核极注意力机制扩展到包括所有源像素，有助于聚合来自其他未聚焦视图的初始化坐标对齐点特征。最后，我们使用另一个变换器将射线特征解码为最终的像素强度。至关重要的是，我们的框架既不依赖于2D先验模型，也不依赖于对相机姿态的明确估计。在测试过程中，DragView展示了将其推广到训练中看不见的新场景的能力，还仅使用未渲染的支持图像，从而能够生成以灵活的相机轨迹为特征的照片逼真的新视图。在我们的实验中，我们将DragView的性能与最近在无姿态条件下运行的场景表示网络以及在噪声测试相机姿态下的可推广NeRF进行了全面比较。DragView在视图合成质量方面始终如一地展示了其卓越的性能，同时也更加用户友好。项目页面：https://zhiwenfan.github.io/DragView/. et.al.|[2310.03704](http://arxiv.org/abs/2310.03704)|null|
|**2023-10-05**|**Point-Based Radiance Fields for Controllable Human Motion Synthesis**|本文提出了一种新的基于静态点辐射场的精细变形可控人体运动合成方法。尽管以前的可编辑神经辐射场方法可以在新的视图合成上产生令人印象深刻的结果，并允许天真变形，但很少有算法可以实现复杂的三维人体编辑，如正向运动学。我们的方法利用显式点云来训练静态3D场景，并通过使用变形MLP对点云平移进行编码来应用变形。为了确保渲染结果与规范空间训练一致，我们使用SVD估计局部旋转，并将每点旋转插值到预训练辐射场的查询视图方向。大量实验表明，我们的方法在精细复杂变形方面可以显著优于最先进的方法，该方法可以推广到除人类之外的其他3D角色。 et.al.|[2310.03375](http://arxiv.org/abs/2310.03375)|**[link](https://github.com/dehezhang2/point_based_nerf_editing)**|
|**2023-10-04**|**Consistent-1-to-3: Consistent Image to 3D View Synthesis via Geometry-aware Diffusion Models**|从单个图像中进行零样本新视图合成（NVS）是三维对象理解中的一个基本问题。尽管最近利用预先训练的生成模型的方法可以从野外输入中合成高质量的新视图，但它们仍然难以在不同视图之间保持3D一致性。在本文中，我们提出了Consistent-1-to-3，这是一个显著缓解这一问题的生成框架。具体来说，我们将NVS任务分解为两个阶段：（i）将观察到的区域转换为新的视图，以及（ii）对看不见的区域产生幻觉。我们设计了一个场景表示转换器和视图条件扩散模型，分别用于执行这两个阶段。在模型内部，为了增强三维一致性，我们建议使用六面体引导注意力来结合几何约束，并使用多视图注意力来更好地聚合多视图信息。最后，我们设计了一个层次生成范式来生成长序列的一致视图，允许对所提供的对象图像进行全方位的360度观察。对多个数据集的定性和定量评估证明了所提出的机制相对于最先进方法的有效性。我们的项目页面位于https://jianglongye.com/consistent123/ et.al.|[2310.03020](http://arxiv.org/abs/2310.03020)|null|
|**2023-10-04**|**Efficient-3DiM: Learning a Generalizable Single-image Novel-view Synthesizer in One Day**|新颖视图合成的任务旨在从有限的一组输入图像中生成对象或场景的看不见的视角。然而，从单个图像合成新颖的视图仍然是计算机视觉领域的一个重大挑战。以前的方法通过采用网格预测、多平面图像构建或更先进的技术（如神经辐射场）来解决这个问题。最近，一种专门为2D图像合成设计的预训练扩散模型已经证明，如果在3D微调任务上进行充分优化，它就能够产生逼真的新视图。尽管保真度和可推广性大大提高，但训练这样一个强大的扩散模型需要大量的训练数据和模型参数，这导致了众所周知的长时间和高计算成本。为了解决这个问题，我们提出了Efficient-3DiM，这是一个简单但有效的框架来学习单个图像的新颖视图合成器。受我们对扩散模型推理过程的深入分析的启发，我们提出了几种实用的策略，将训练开销降低到可管理的规模，包括精心设计的时间步长采样策略、卓越的3D特征提取器和增强的训练方案。当组合在一起时，我们的框架能够将总训练时间从10天减少到不到1天，从而显著加快了在相同计算平台下的训练过程（一个例子中有8个Nvidia A100 GPU）。通过综合实验验证了该方法的有效性和可推广性。 et.al.|[2310.03015](http://arxiv.org/abs/2310.03015)|null|
|**2023-10-05**|**USB-NeRF: Unrolling Shutter Bundle Adjusted Neural Radiance Fields**|神经辐射场（NeRF）由于其令人印象深刻的三维场景表示和合成新视图图像的能力，近年来受到了广泛的关注。现有的作品通常假设输入图像是由全局快门相机拍摄的。因此，滚动快门（RS）图像不能简单地应用于用于新颖视图合成的现成NeRF算法。滚动快门效应也会影响相机姿态估计的准确性（例如，通过COLMAP），这进一步阻碍了NeRF算法在RS图像中的成功。在本文中，我们提出了Unrolling Shutter Bundle Adjusted Neural Radiance Fields（USB NeRF）。USB NeRF能够在NeRF的框架下，通过对RS相机的物理图像形成过程进行建模，同时校正滚动快门失真并恢复精确的相机运动轨迹。实验结果表明，USB NeRF在RS效应去除、新视角图像合成以及相机运动估计方面都比以往的工作取得了更好的性能。此外，我们的算法还可以用于从RS图像序列中恢复高保真高帧率全局快门视频。 et.al.|[2310.02687](http://arxiv.org/abs/2310.02687)|null|
|**2023-10-05**|**MagicDrive: Street View Generation with Diverse 3D Geometry Control**|扩散模型的最新进展显著增强了2D控制的数据合成。然而，街景生成中的精确3D控制，对于3D感知任务至关重要，仍然难以捉摸。具体而言，将鸟瞰图（BEV）作为主要条件通常会导致几何控制（如高度）方面的挑战，影响物体形状、遮挡模式和路面高程的表示，所有这些对于感知数据合成至关重要，尤其是对于3D物体检测任务。在本文中，我们介绍了MagicDrive，这是一种新颖的街景生成框架，提供各种3D几何控制，包括相机姿势、道路地图和3D边界框，以及文本描述，通过定制的编码策略实现。此外，我们的设计包含了一个跨视图注意力模块，确保了多个相机视图的一致性。通过MagicDrive，我们实现了高保真街景合成，可以捕捉细微的3D几何结构和各种场景描述，增强了BEV分割和3D对象检测等任务。 et.al.|[2310.02601](http://arxiv.org/abs/2310.02601)|null|
|**2023-10-03**|**MIMO-NeRF: Fast Neural Rendering with Multi-input Multi-output Neural Radiance Fields**|神经辐射场（NeRF）在新的视图合成中显示出令人印象深刻的结果。然而，它们依赖于重复使用单输入单输出多层感知器（SISO MLP），该感知器以逐样本的方式将3D坐标和视图方向映射到颜色和体积密度，这会减慢渲染速度。我们提出了一种多输入多输出NeRF（MIMO NeRF），通过用MIMO MLP替换SISO MLP并以分组方式进行映射来减少运行的MLP的数量。这种方法的一个显著挑战是，根据组中输入坐标的选择，每个点的颜色和体积密度可能不同，这可能导致一些显著的模糊性。我们还提出了一种自监督学习方法，该方法使用多个快速重新表述的MLP来正则化MIMO MLP，以在不使用预训练模型的情况下缓解这种模糊性。包括比较和消融研究在内的综合实验评估结果表明，在合理的训练时间内，MIMO NeRF在速度和质量之间取得了良好的平衡。然后，我们通过将MIMO NeRF应用于两个具有代表性的快速NeRF，即具有样本减少的NeRF（DONeRF）和具有替代表示的NeRF，来证明MIMO NeRF与NeRF的先前进步兼容并互补。 et.al.|[2310.01821](http://arxiv.org/abs/2310.01821)|null|
|**2023-10-02**|**LEAP: Liberate Sparse-view 3D Modeling from Camera Poses**|多视图三维建模是否需要相机姿势？现有的方法主要假设能够获得准确的相机姿势。虽然这一假设可能适用于密集视图，但准确估计稀疏视图的相机姿态往往是难以捉摸的。我们的分析表明，噪声估计的姿态会导致现有稀疏视图三维建模方法的性能下降。为了解决这个问题，我们提出了LEAP，这是一种新颖的无姿势方法，因此挑战了相机姿势不可或缺的普遍观念。LEAP放弃基于姿态的操作，并从数据中学习几何知识。LEAP配备了一个神经体积，该体积在场景中共享，并被参数化以编码几何和纹理先验。对于每个进入的场景，我们通过以特征相似性驱动的方式聚集2D图像特征来更新神经体积。更新后的神经体积被解码到辐射场中，从而能够从任何视点进行新颖的视图合成。在以对象为中心和场景级别的数据集上，我们表明，当LEAP使用最先进的姿态估计器的预测姿态时，它们显著优于先前的方法。值得注意的是，LEAP的表现与之前使用真实姿势的方法不相上下，同时比PixelNeRF快400美元\倍。我们展示了LEAP可以推广到新的对象类别和场景，并学习与极线几何非常相似的知识。项目页面：https://hwjiang1510.github.io/LEAP/ et.al.|[2310.01410](http://arxiv.org/abs/2310.01410)|null|

<p align=right>(<a href=#updated-on-20231009>back to top</a>)</p>

## 3D Reconstruction

|Publish Date|Title|Abstract|PDF|Code|
|---|---|---|---|---|
|**2023-10-06**|**Towards Non-contact 3D Ultrasound for Wrist Imaging**|目的：这项工作的目的是尝试在现有的护理点超声（POCUS）系统的基础上，以最小的复杂性实现非接触式徒手三维超声成像。方法：本研究提出了一种使用机械轨道进行非接触超声（US）扫描的新方法。因此，该方法将探针运动限制在线性平面上，以简化采集和3D重建过程。开发了一种利用美国研究平台和基于GPU的边缘设备进行美国3D体积重建的管道。结果：通过离体和体内实验证明了该方法的有效性。结论：所提出的方法具有可调节的视场能力、非接触式设计和低部署成本，而不会显著改变现有设置，这将为传统系统的升级打开大门，使其能够应用于广泛的3D US成像。意义：超声（US）成像是一种流行的临床成像方式，用于护理点床边成像，尤其是儿科人群的手腕/膝盖，因为其具有非侵入性和无辐射性。然而，在这种情况下，用2D US获得的组织结构的有限视图使诊断具有挑战性。为了克服这一点，开发了使用2D US图像及其方向/位置来重建3D体积的3D US成像。在三维重建中，以低成本精确估计美国探测器的位置一直是一项具有挑战性的任务。此外，US成像涉及接触，这会给儿科受试者在监测活骨折或开放性伤口时带来困难。为了克服这些挑战，本工作尝试了一种新颖的框架。 et.al.|[2310.04296](http://arxiv.org/abs/2310.04296)|null|
|**2023-10-06**|**ILSH: The Imperial Light-Stage Head Dataset for Human Head View Synthesis**|本文介绍了Imperial Light Stage Head（ILSH）数据集，这是一个新颖的Light Stage捕获的人头数据集，旨在支持人头的视图合成学术挑战。ILSH数据集旨在促进各种方法，如场景特定或通用神经渲染、多视图几何、3D视觉和计算机图形学，以进一步推动照片逼真的人类化身的开发。本文详细介绍了专门用于捕捉高分辨率（4K）人头图像的光台的设置，并描述了在收集高质量数据时应对挑战（预处理、道德问题）的过程。除了数据收集之外，我们还将数据集拆分为训练集、验证集和测试集。我们的目标是为这个新的数据集设计和支持一个公平视图综合挑战任务，以便在使用测试集时，如在使用验证集时，可以保持和预期类似的性能水平。ILSH数据集由52名受试者组成，这些受试者使用24台相机拍摄，所有82个光源都打开，共产生1248张特写头部图像、边界遮罩和相机姿势对。 et.al.|[2310.03952](http://arxiv.org/abs/2310.03952)|null|
|**2023-10-05**|**Hard View Selection for Contrastive Learning**|许多对比学习（CL）方法将其模型训练为对图像输入的不同“视图”保持不变，而良好的数据增强管道对图像输入至关重要。尽管在改进文本前任务、架构或鲁棒性（例如，连体网络或教师softmax居中）方面做出了相当大的努力，但这些方法中的大多数仍然强烈依赖于图像增强管道内操作的随机采样，例如随机调整大小的裁剪或颜色失真操作。在本文中，我们认为，到目前为止，视图生成的作用及其对性能的影响还没有得到足够的关注。为了解决这一问题，我们提出了一种简单、无需学习但功能强大的硬视图选择（HVS）策略，该策略旨在扩展随机视图生成，以在CL训练期间将预训练的模型暴露给更硬的样本。它包括以下迭代步骤：1）随机采样多个视图并创建两个视图对，2）在当前训练的模型上为每个视图对运行前向传递，3）对抗性地选择产生最差损失的对，以及4）使用所选对运行后向传递。在我们的实证分析中，我们发现在引擎盖下，HVS通过在预训练过程中控制视图并集上的交集来增加任务难度。HVS只需要300个历元的预训练，就可以与800个历元DINO基线相媲美，即使考虑到HVS额外前锋导致的速度放缓，这一基线仍然非常有利。此外，HVS在ImageNet上的线性评估精度持续提高0.55%至1.9%，在多种CL方法（如DINO、SimSiam和SimCLR）的传输任务上也实现了类似的改进。 et.al.|[2310.03940](http://arxiv.org/abs/2310.03940)|null|
|**2023-10-04**|**Condition numbers in multiview geometry, instability in relative pose estimation, and RANSAC**|在本文中，我们介绍了一个通用框架，用于分析多视图几何中最小问题的数值条件，使用计算代数和黎曼几何的工具。特别的动机来自这样一个事实，即基于标准的5点或7点随机样本一致性（RANSAC）算法的相对姿态估计，即使不存在异常值，并且有足够的数据支持假设，也可能失败。我们认为，这些情况是由于5点和7点极小问题的内在不稳定性引起的。我们应用我们的框架来表征不稳定性，既可以从导致无限条件数的世界场景的角度，也可以直接从病态图像数据的角度。该方法产生计算测试，用于在解决最小问题之前评估条件数。最后，合成和真实数据实验表明，正如我们的理论预测的那样，RANSAC不仅可以去除异常值，还可以选择条件良好的图像数据。 et.al.|[2310.02719](http://arxiv.org/abs/2310.02719)|null|
|**2023-10-02**|**PC-NeRF: Parent-Child Neural Radiance Fields under Partial Sensor Data Loss in Autonomous Driving Environments**|重建大规模3D场景对自动驾驶汽车至关重要，尤其是在部分传感器数据丢失的情况下。尽管最近开发的神经辐射场（NeRF）在隐式表示中显示出了令人信服的结果，但使用部分丢失的激光雷达点云数据进行大规模3D场景重建仍需探索。为了弥补这一差距，我们提出了一种新的3D场景重建框架，称为父子神经辐射场（PC NeRF）。该框架包括两个模块，父NeRF和子NeRF，以同时优化场景级、分段级和点级场景表示。通过利用子NeRF的分段级表示能力，可以更有效地利用传感器数据，并且即使在有限的观测下也可以快速获得场景的近似体积表示。经过大量的实验，我们提出的PC NeRF被证明可以在大规模场景中实现高精度的3D重建。此外，PC NeRF可以有效地处理部分传感器数据丢失的情况，并且在有限的训练时间内具有较高的部署效率。我们的方法实施和预先培训的模型将在https://github.com/biter0088/pc-nerf. et.al.|[2310.00874](http://arxiv.org/abs/2310.00874)|**[link](https://github.com/biter0088/pc-nerf)**|
|**2023-10-01**|**Enabling Neural Radiance Fields (NeRF) for Large-scale Aerial Images -- A Multi-tiling Approaching and the Geometry Assessment of NeRF**|神经辐射场（NeRF）提供了有益于3D重建任务的潜力，包括航空摄影测量。然而，对于大规模航空资产，推断几何结构的可扩展性和准确性并没有得到很好的证明，因为这样的数据集通常会导致非常高的内存消耗和缓慢的收敛。。在本文中，我们的目标是在大型scael航空数据集上缩放NeRF，并对NeRF进行全面的几何评估。具体而言，我们介绍了一种特定于位置的采样技术以及多摄像头拼接（MCT）策略，以减少RAM图像加载期间的内存消耗、GPU内存的表示训练，并提高拼接内的收敛率。MCT将大帧图像分解为具有不同相机模型的多个拼接图像，允许这些小帧图像根据特定位置的需要被输入到训练过程中，而不会损失准确性。我们在一种具有代表性的方法Mip-NeRF上实现了我们的方法，并在两个典型的航空数据集上与激光雷达参考数据比较了其几何性能与三光图MVS管道。定性和定量结果都表明，与传统方法相比，所提出的NeRF方法产生了更好的完整性和对象细节，尽管到目前为止，它在准确性方面仍然不足。 et.al.|[2310.00530](http://arxiv.org/abs/2310.00530)|null|
|**2023-09-29**|**3D Reconstruction in Noisy Agricultural Environments: A Bayesian Optimization Perspective for View Planning**|三维重建是机器人技术中的一项基本任务，由于其在农业、水下和城市环境等各种实际环境中的重大影响而受到关注。这项任务的一个重要方法，即视图规划，是明智地将多个相机放置在最大限度地提高视觉信息的位置，从而改进最终的3D重建。为了避免对大量任意图像的需求，可以应用几何标准来选择更少但信息更丰富的图像，以显著提高3D重建性能。尽管如此，将存在于各种真实世界场景中的环境噪声纳入这些标准可能是具有挑战性的，特别是当没有提供关于噪声的先验信息时。为此，这项工作提倡一种新的几何函数，它可以解释现有的噪声，只依赖于相对少量的噪声实现，而不需要其闭合形式的表达式。在没有几何函数的解析表达式的情况下，本文提出了一种在噪声存在的情况下进行精确三维重建的贝叶斯优化算法。在嘈杂的农业环境中进行的数值测试表明，即使使用少量可用的摄像机，所提出的3D重建方法也具有令人印象深刻的优点。 et.al.|[2310.00145](http://arxiv.org/abs/2310.00145)|null|
|**2023-09-29**|**Multi-task View Synthesis with Neural Radiance Fields**|多任务视觉学习是计算机视觉的一个重要方面。然而，目前的研究主要集中在多任务密集预测环境上，它忽略了内在的3D世界及其多视图一致的结构，缺乏丰富想象力的能力。为了应对这些限制，我们提出了一种新的问题设置——多任务视图合成（MTVS），它将多任务预测重新解释为一组针对多个场景属性（包括RGB）的新视图合成任务。为了解决MTVS问题，我们提出了MuvieNeRF，这是一个结合了多任务和跨视图知识的框架，可以同时合成多个场景属性。MuvieNeRF集成了两个关键模块，即跨任务注意力（CTA）和跨视图注意力（CVA）模块，实现了跨多个视图和任务的信息高效使用。对合成和逼真基准的广泛评估表明，MuvieNeRF能够同时合成具有良好视觉质量的不同场景属性，甚至在各种设置下都优于传统的判别模型。值得注意的是，我们发现MuvieNeRF在一系列NeRF主干上表现出普遍的适用性。我们的代码可在https://github.com/zsh2000/MuvieNeRF. et.al.|[2309.17450](http://arxiv.org/abs/2309.17450)|**[link](https://github.com/zsh2000/muvienerf)**|
|**2023-09-29**|**Effect of structure-based training on 3D localization precision and quality**|本研究介绍了一种基于结构的训练方法，用于单分子定位显微镜（SMLM）和三维物体重建中基于CNN的算法。我们将这种方法与传统的基于随机的训练方法进行了比较，利用LUENN包作为我们的AI管道。定量评估表明，使用基于结构的训练方法，特别是在不同信噪比（SNR）的情况下，检测率和定位精度显著提高。此外，该方法有效地去除了棋盘伪影，确保了更准确的三维重建。我们的发现突出了基于结构的训练方法在推进超分辨率显微镜和加深我们对纳米级复杂生物系统的理解方面的潜力。 et.al.|[2309.17265](http://arxiv.org/abs/2309.17265)|null|
|**2023-09-28**|**Sketch2CADScript: 3D Scene Reconstruction from 2D Sketch using Visual Transformer and Rhino Grasshopper**|现有的3D模型重建方法通常以体素、点云或网格的形式产生输出。然而，这些方法中的每一种都有其局限性，可能不适合每种情况。例如，生成的模型可能会呈现粗糙的表面和扭曲的结构，这使得手动编辑和后处理对人类来说具有挑战性。在本文中，我们介绍了一种新的三维重建方法，旨在解决这些问题。我们训练了一个视觉转换器来从单线帧图像中预测“场景描述符”。该描述符包含关键信息，包括对象类型和参数，如位置、旋转和大小。有了预测的参数，可以使用Blender或Rhino Grasshopper等3D建模软件重建3D场景，该软件提供了可编程的界面，从而生成精细且易于编辑的3D模型。为了评估所提出的模型，我们创建了两个数据集：一个以简单场景为特征，另一个以复杂场景为特征。测试结果证明了该模型准确重建简单场景的能力，但也揭示了其在更复杂场景中的挑战。 et.al.|[2309.16850](http://arxiv.org/abs/2309.16850)|null|

<p align=right>(<a href=#updated-on-20231009>back to top</a>)</p>

## Diffusion

|Publish Date|Title|Abstract|PDF|Code|
|---|---|---|---|---|
|**2023-10-06**|**Diffusion Random Feature Model**|扩散概率模型已成功地用于从噪声中生成数据。然而，由于缺乏理论依据，大多数扩散模型的计算成本高昂，难以解释。另一方面，随机特征模型由于其可解释性而广受欢迎，但其在复杂机器学习任务中的应用仍然有限。在这项工作中，我们提出了一个受扩散模型启发的深度随机特征模型，该模型是可解释的，并给出了与具有相同数量可训练参数的全连接神经网络相当的数值结果。具体来说，我们扩展了随机特征的现有结果，并使用分数匹配的特性推导了采样数据的分布和真实分布之间的泛化边界。我们通过在时尚MNIST数据集和工具音频数据上生成样本来验证我们的发现。 et.al.|[2310.04417](http://arxiv.org/abs/2310.04417)|null|
|**2023-10-06**|**CIFAR-10-Warehouse: Broad and More Realistic Testbeds in Model Generalization Analysis**|分析模型在各种看不见的环境中的性能是机器学习界的一个关键研究问题。为了研究这个问题，重要的是构建一个具有广泛覆盖环境差异的分布外测试集的测试台。然而，现有的测试台通常要么具有少量的域，要么通过图像损坏进行合成，这阻碍了展示真实世界有效性的算法设计。在本文中，我们介绍了CIFAR-10-Warehouse，它由180个数据集组成，这些数据集是通过各种方式提示图像搜索引擎和扩散模型收集的。数据集通常大小在300到8000张图像之间，包含自然图像、卡通、某些颜色或不自然出现的对象。使用CIFAR-10-W，我们旨在增强对两个泛化任务的评估并加深对这两个任务的理解：在各种分布外环境中的领域泛化和模型精度预测。我们进行了广泛的基准测试和比较实验，并表明CIFAR-10-W提供了这些任务固有的新的有趣见解。我们还讨论了将受益于CIFAR-10-W的其他领域。 et.al.|[2310.04414](http://arxiv.org/abs/2310.04414)|null|
|**2023-10-06**|**Seeding the CGM: How Satellites Populate the Cold Phase of Milky Way Halos**|CGM中冷相的起源是一个备受争议的问题。我们研究了卫星星系对类银河系宿主星系环星系介质（CGM）中冷气体预算的贡献。我们对三种不同的卫星质量分布进行了控制实验，并确定了卫星向CGM添加冷气体的几种机制，包括冲压压力汽提和汽提冷气体混合层的诱导冷却。这两种机制为宿主CGM提供了相当数量的冷气体。我们发现，质量较小的卫星（ $\leq10^9M_\odot$）不仅在短时间内（$\sim$0.5-1Gyr）失去了所有的冷气体，而且它们剥离的冷云也与热的CGM气体混合并迅速升温。然而，来自这些质量较小的卫星的恒星反馈可以极大地改变其剥离气体的命运。反馈通过使这些卫星的冷云更具扩散性和更大的表面积，加快了对它们的破坏。另一方面，质量更大的卫星（LMC或SMC，如$\sim 10^｛10｝M_\odot$ ）可以在几Gyr内将冷气体添加到主CGM的总气体预算中。 et.al.|[2310.04404](http://arxiv.org/abs/2310.04404)|null|
|**2023-10-06**|**Supernova Remnants in the Irregular Galaxy NGC4449**|附近的不规则星系NGC449的恒星形成率约为0.4太阳质量/年，其SNR数量级应为70，小于20000年，这是SNR扩展到单位密度ISM达到辐射相的典型年龄。我们进行了光学成像和光谱调查，试图识别这些SNR。这项任务具有挑战性，因为[SI]∶H-，｛在使用这种常见的SNR诊断时会引起混乱。使用窄带干扰滤波器图像，我们首先识别出49个物体，与附近的HII区域相比，它们的[SI]:H-alpha比率升高。然后使用Gemini-N和GMOS，我们获得了其中30个候选SNR的高分辨率光谱，其中25个的[SI]：H-alpha比率大于0.5。其中，15个星云几乎可以肯定是SNR，这是基于以下特征的组合：比HII区域观察到的更高的[OI]:H-α比率和更宽的线宽。其余部分也是不错的候选者，但需要进一步确认。令人惊讶的是，尽管有优越的成像和光谱数据集可供检查，但我们无法确认Leonidaki（2013）提出的大多数候选者。虽然NGC449可能是一个极端的情况，因为它的表面亮度很高，扩散气体的[SI]：H-alpha比率升高，但它强调了对敏感的高分辨率光学光谱的需求，或高空间分辨率的无线电或X射线观测，以确保在外部星系中准确识别SNR。 et.al.|[2310.04382](http://arxiv.org/abs/2310.04382)|null|
|**2023-10-06**|**Latent Consistency Models: Synthesizing High-Resolution Images with Few-Step Inference**|潜在扩散模型（LDMs）在合成高分辨率图像方面取得了显著的成果。然而，迭代采样过程是计算密集型的，并且导致生成缓慢。受一致性模型的启发（song等人），我们提出了潜在一致性模型（LCMs），能够在任何预先训练的LDM上以最小的步骤进行快速推理，包括稳定扩散（rombach等人）。将引导反向扩散过程视为求解增广概率流ODE（PF-ODE），LCM被设计为在潜在空间中直接预测这种ODE的解，从而减少了多次迭代的需要，并允许快速高保真采样。高效地从预先训练的无分类器引导扩散模型中提取，高质量的768 x 768 2~4步LCM只需32个A100 GPU小时即可进行训练。此外，我们还介绍了潜在一致性微调（LCF），这是一种专门针对定制图像数据集上的LCM进行微调的新方法。对LAION-5B-美学数据集的评估表明，LCM在少步推理的情况下实现了最先进的文本到图像生成性能。项目页面：https://latent-consistency-models.github.io/ et.al.|[2310.04378](http://arxiv.org/abs/2310.04378)|**[link](https://github.com/luosiallen/latent-consistency-model)**|
|**2023-10-06**|**Molecular Structural Dynamics in Water-Ethanol Mixtures: Spectroscopy with Polarized Neutrons Simultaneously Accessing Collective and Self-Diffusion**|水与低级醇的二元混合物在混合时表现出非线性相行为，这归因于分子水平上潜在的团簇形成。解开这种难以捉摸的结构需要研究亚纳秒的氢键动力学。我们将高分辨率中子飞行时间光谱与极化分析相结合，结合选择性氘化，研究水-乙醇混合物相图富含水部分的浓度依赖性结构动力学。该方法能够同时获得空间和时间中的原子相关性，并使我们能够将乙醇部分的空间非相干散射探测自扩散与水网络整体的相干散射探测集体扩散分离开来。我们的观察结果表明，随着乙醇分数的增加，与分子内尺度相比，在介观长度尺度上氢键网络的刚性增强，这与团簇的假设一致。 et.al.|[2310.04320](http://arxiv.org/abs/2310.04320)|null|
|**2023-10-06**|**Zentropy Theory for Quantitative Prediction of Emergent Behaviors**|密度泛函理论（DFT）是一种事实上的方法，用于预测复杂原子、分子和固体基态构型的自洽场电子结构，并为材料的发现和设计提供其性质数据。这一能力在很大程度上得益于John Perdew及其合作者在过去几十年中开发的一组重要交换相关泛函与交换相关相互作用的广义梯度近似。科学界和本作者小组从这种能力中受益匪浅。多年来，本作者的团队将零K和有限温度下基于DFT计算的能量学整合到热力学建模中，并开发了预测示踪剂扩散率、弹性系数、界面能和与自由能导数相关的许多其他性质的方法。一个关键的结果是通过考虑基态和稳定的对称性破缺非基态构型来准确预测系统的自由能。阐明了在感兴趣的温度和体积范围内，所有单个构型的声子性质都可以通过准谐波近似来精确计算，并且系统的涌现行为和非谐性主要源于所有构型之间的统计竞争。 et.al.|[2310.04279](http://arxiv.org/abs/2310.04279)|null|
|**2023-10-06**|**Fully discrete Galerkin scheme for a semilinear subdiffusion equation with nonsmooth data and time-dependent coefficient**|我们将Caputo分数阶导数在时间上的L1离散化与Galerkin格式相结合，设计了一种求解半线性次扩散方程的线性数值方法。我们提出的两个重要观点是：非光滑初始数据和含时扩散系数。在关于扩散率规律的弱假设下，我们证明了该方法的稳定性和收敛性。我们发现了空间上的最优点误差和时间上的全局误差，并通过几个数值实验进行了验证。 et.al.|[2310.04246](http://arxiv.org/abs/2310.04246)|null|
|**2023-10-06**|**Exploring the interstellar medium of NGC 891 at millimeter wavelengths using the NIKA2 camera**|在IMEGIN大型计划的框架内，我们使用IRAM 30米望远镜上的NIKA2相机分别以1.15毫米和2毫米以及11.1“和17.6”的FWHM观测NGC 891星系的边缘。使用HerBIE SED代码（与THEMIS尘埃模型相结合）拟合的新NIKA2观测结果丰富的多波长数据来约束ISM的物理特性。在从中红外到毫米的所有波长下都能检测到来自扩散尘埃盘的发射，而中红外观测揭示了致密HII区域的暖尘发射。在星系盘的外部也发现了毫米过量发射的迹象。此外，我们的SED拟合分析限制了小（<15埃）尘粒的质量分数。我们发现，小颗粒占银河系平面总尘埃质量的9.5%，但在距离银河系平面较远的地方（|z|>3kpc），这一比例会增加到约20%。 et.al.|[2310.04204](http://arxiv.org/abs/2310.04204)|null|
|**2023-10-06**|**Real diffusion with complex spectral gap**|在适当的假设下，Langevin过程发生器的低本征值在低温状态下满足Eyring-Kramers定律。这些特征值一般是实的。我们构造了生成器，其谱间隙由非实特征值或具有Jordan块的实特征值给出。 et.al.|[2310.04203](http://arxiv.org/abs/2310.04203)|null|

<p align=right>(<a href=#updated-on-20231009>back to top</a>)</p>

## NeRF

|Publish Date|Title|Abstract|PDF|Code|
|---|---|---|---|---|
|**2023-10-05**|**Variational Barycentric Coordinates**|我们提出了一种变分技术来优化广义重心坐标，与现有模型相比，该技术提供了额外的控制。先前的工作使用网格或闭式公式表示重心坐标，在实践中限制了目标函数的选择。相反，我们使用神经场直接参数化连续函数，该函数将多面体内部的任何坐标映射到其重心坐标。这个公式是通过我们对重心坐标的理论表征实现的，这使我们能够构建将有效坐标的整个函数类参数化的神经场。我们使用各种目标函数展示了我们模型的灵活性，包括多重光滑性和变形感知能量；作为补充，我们还提出了数学上合理的方法来测量和最小化目标，如不连续神经场的总变化。我们提供了一个实用的加速策略，对我们的算法进行了彻底的验证，并展示了几个应用。 et.al.|[2310.03861](http://arxiv.org/abs/2310.03861)|null|
|**2023-10-05**|**High-Degrees-of-Freedom Dynamic Neural Fields for Robot Self-Modeling and Motion Planning**|机器人自模型是机器人物理形态的任务不可知表示，在没有经典几何运动学模型的情况下，可用于运动规划任务。特别是，当后者难以设计或机器人的运动学发生意外变化时，人类自由的自我建模是真正自主智能体的必要特征。在这项工作中，我们利用神经场使机器人能够将其运动学自建模为仅从带有相机姿势和配置的2D图像中学习的神经隐式查询模型。这使得比依赖于深度图像或几何知识的现有方法具有更大的适用性。为此，除了课程数据采样策略外，我们还提出了一种新的基于编码器的神经密度场架构，用于高自由度（DOF）条件下的动态对象中心场景。在7自由度机器人测试装置中，学习的自模型实现了机器人工作空间尺寸2%的倒角-L2距离。作为一个示例性的下游应用程序，我们展示了该模型在运动规划任务中的能力。 et.al.|[2310.03624](http://arxiv.org/abs/2310.03624)|null|
|**2023-10-02**|**Neural Processing of Tri-Plane Hybrid Neural Fields**|在用于存储和通信3D数据的神经场的吸引人的特性的驱动下，直接处理它们以解决分类和零件分割等任务的问题已经出现，并在最近的工作中进行了研究。早期的方法使用由在整个数据集上训练的共享网络参数化的神经场，实现了良好的任务性能，但牺牲了重建质量。为了改进后者，后来的方法侧重于参数化为大型多层感知器（MLP）的单个神经场，然而，由于权重空间的高维性、固有的权重空间对称性和对随机初始化的敏感性，这些神经元场的处理具有挑战性。因此，结果明显不如通过处理显式表示（例如点云或网格）所获得的结果。与此同时，混合表示，特别是基于三平面的混合表示，已经成为实现神经场的一种更有效的替代方案，但其直接处理尚未得到研究。在本文中，我们证明了三平面离散数据结构编码了丰富的信息，标准的深度学习机器可以有效地处理这些信息。我们定义了一个广泛的基准，涵盖了一组不同的字段，如占用率、有符号/无符号距离，以及首次定义的辐射字段。在处理具有相同重建质量的字段时，我们实现的任务性能远远优于处理大型MLP的框架，并且首次几乎与处理显式表示的架构不相上下。 et.al.|[2310.01140](http://arxiv.org/abs/2310.01140)|null|
|**2023-09-27**|**Neural Acoustic Context Field: Rendering Realistic Room Impulse Response With Neural Fields**|房间脉冲响应（RIR）测量声音在环境中的传播，对于合成给定环境下的高保真音频至关重要。一些先前的工作已经提出将RIR表示为声音发射器和接收器位置的神经场函数。然而，这些方法没有充分考虑音频场景的声学特性，导致性能不令人满意。这封信提出了一种新的神经声学上下文场方法，称为NACF，通过利用多个声学上下文（如几何结构、材料特性和空间信息）来参数化音频场景。在RIR的独特性质，即时间不光滑性和单调能量衰减的驱动下，我们设计了一个时间相关模块和多尺度能量衰减准则。实验结果表明，NACF的性能显著优于现有的基于字段的方法。请访问我们的项目页面了解更多定性结果。 et.al.|[2309.15977](http://arxiv.org/abs/2309.15977)|null|
|**2023-09-27**|**SHACIRA: Scalable HAsh-grid Compression for Implicit Neural Representations**|隐式神经表示（INR）或神经场已成为编码多媒体信号（如图像和辐射场）同时保持高质量的流行框架。最近，Instant NGP提出的可学习特征网格通过用特征向量的多分辨率查找表和更小的神经网络取代大型神经网络，在训练和INR采样方面实现了显著的加速。然而，这些功能网格是以大量内存消耗为代价的，这可能是存储和流应用程序的瓶颈。在这项工作中，我们提出了SHACIRA，这是一个简单而有效的任务无关框架，用于压缩这种特征网格，而不需要额外的事后修剪/量化阶段。我们用量化的潜在权重对特征网格进行重新参数化，并在潜在空间中应用熵正则化，以在各个领域实现高水平的压缩。在由图像、视频和辐射场组成的不同数据集上的定量和定性结果表明，我们的方法优于现有的INR方法，而不需要任何大型数据集或特定领域的启发式方法。我们的项目页面可在http://shacira.github.io。 et.al.|[2309.15848](http://arxiv.org/abs/2309.15848)|null|
|**2023-09-27**|**NeuRBF: A Neural Fields Representation with Adaptive Radial Basis Functions**|我们提出了一种新型的神经场，它使用一般的径向基来表示信号。现有技术的神经领域通常依赖于用于存储局部神经特征的基于网格的表示和用于在连续查询点处插值特征的N维线性核。它们的神经特征的空间位置固定在网格节点上，不能很好地适应目标信号。相反，我们的方法建立在具有灵活内核位置和形状的通用径向基上，这些径向基具有更高的空间自适应性，可以更紧密地拟合目标信号。为了进一步提高径向基函数的信道容量，我们建议将它们与多频率正弦函数组合。该技术将径向基扩展到不同频带的多个傅立叶径向基，而不需要额外的参数，便于细节的表示。此外，通过将自适应径向基与基于网格的径向基相结合，我们的混合组合继承了自适应性和插值平滑性。我们精心设计了加权方案，使径向基有效地适应不同类型的信号。我们在2D图像和3D符号距离场表示上的实验证明了我们的方法比现有技术更高的精度和紧凑性。当应用于神经辐射场重建时，我们的方法实现了最先进的渲染质量，模型大小小，训练速度相当。 et.al.|[2309.15426](http://arxiv.org/abs/2309.15426)|**[link](https://github.com/oppo-us-research/NeuRBF)**|
|**2023-09-29**|**3D Reconstruction with Generalizable Neural Fields using Scene Priors**|由于神经领域的最新进展，高保真3D场景重建得到了实质性的推进。然而，大多数现有的方法为每个单独的场景从头开始训练单独的网络。这是不可扩展的，效率低下，并且在视图有限的情况下无法产生良好的结果。虽然基于学习的多视图立体方法在一定程度上缓解了这一问题，但它们的多视图设置使其扩展和广泛应用的灵活性降低。相反，我们引入了结合场景先验（NFP）的训练可推广神经场。NFP网络将任何单视图RGB-D图像映射为带符号的距离和辐射值。在没有融合模块的情况下，可以通过合并体积空间中的各个帧来重建完整的场景，这提供了更好的灵活性。场景先验可以在大规模数据集上进行训练，从而能够快速适应具有较少视图的新场景的重建。NFP不仅展示了SOTA场景重建的性能和效率，而且还支持单图像新视图合成，这在神经领域还没有得到充分的探索。更多定性结果可在以下网站获得：https://oasisyang.github.io/neural-prior et.al.|[2309.15164](http://arxiv.org/abs/2309.15164)|null|
|**2023-09-22**|**NOC: High-Quality Neural Object Cloning with 3D Lifting of Segment Anything**|随着神经领域的发展，从多视图输入重建目标物体的3D模型最近越来越受到社会的关注。现有的方法通常学习整个场景的神经场，而如何在飞行中重建用户指示的特定对象仍在探索之中。考虑到分段任意模型（SAM）在分割任何2D图像方面都显示出了有效性，本文提出了一种新的高质量3D对象重建方法——神经对象克隆（NOC），它从两个方面利用了神经场和SAM的优点。首先，为了将目标对象从场景中分离出来，我们提出了一种新的策略，将SAM的多视图2D分割掩模提升到一个统一的3D变化场中。然后，3D变化场被投影到2D空间中，并生成SAM的新提示。这个过程是迭代的，直到收敛，以将目标对象从场景中分离出来。然后，除了2D掩模之外，我们进一步将SAM编码器的2D特征提升到3D SAM场中，以提高目标对象的重建质量。NOC将SAM的2D掩模和特征提升到3D神经场中，用于高质量的目标对象重建。我们在几个基准数据集上进行了详细的实验，以证明我们的方法的优势。代码将被发布。 et.al.|[2309.12790](http://arxiv.org/abs/2309.12790)|null|
|**2023-09-15**|**Breathing New Life into 3D Assets with Generative Repainting**|基于扩散的文本到图像模型引发了视觉社区、艺术家和内容创作者的巨大关注。这些模型的广泛采用是由于世代质量的显著提高以及对各种模式的有效调节，而不仅仅是文本。然而，将这些2D模型的丰富生成先验提升到3D中是具有挑战性的。最近的工作提出了由扩散模型和神经场的纠缠提供动力的各种管道。我们探索了预训练的2D扩散模型和标准3D神经辐射场作为独立工具的威力，并展示了它们以非学习方式协同工作的能力。这种模块化具有易于部分升级的内在优势，这在这样一个快节奏的领域中成为了一个重要的特性。我们的管道接受任何遗留的可渲染几何体，如纹理或无纹理网格，协调2D生成细化和3D一致性强制工具之间的交互，并以多种格式输出绘制的输入几何体。我们对ShapeNetSem数据集中的广泛对象和类别进行了大规模研究，并从定性和定量两个方面展示了我们方法的优势。项目页面：https://www.obukhov.ai/repainting_3d_assets et.al.|[2309.08523](http://arxiv.org/abs/2309.08523)|**[link](https://github.com/kongdai123/repainting_3d_assets)**|
|**2023-09-14**|**Neural Field Representations of Articulated Objects for Robotic Manipulation Planning**|传统的操作规划方法依赖于环境的显式几何模型来将给定任务公式化为优化问题。然而，从原始传感器输入推断准确的模型本身就是一个难题，尤其是对于铰接物体（例如壁橱、抽屉）。在本文中，我们提出了一种关节对象的神经场表示（NFR），可以直接从图像中进行操作规划。具体来说，在拍摄了一个新的关节物体的几张照片后，我们可以向前模拟它可能的运动，因此，可以直接使用该神经模型进行轨迹优化规划。此外，这种表示可以用于形状重建、语义分割和图像渲染，这在训练和泛化过程中提供了强大的监督信号。我们表明，我们的模型仅在合成图像上训练，能够在模拟和真实图像中为同类看不见的物体提取有意义的表示。此外，我们证明了该表示能够直接从图像中对现实世界中的关节物体进行机器人操作。 et.al.|[2309.07620](http://arxiv.org/abs/2309.07620)|null|

<p align=right>(<a href=#updated-on-20231009>back to top</a>)</p>

[contributors-shield]: https://img.shields.io/github/contributors/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[contributors-url]: https://github.com/Vincentqyw/cv-arxiv-daily/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[forks-url]: https://github.com/Vincentqyw/cv-arxiv-daily/network/members
[stars-shield]: https://img.shields.io/github/stars/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[stars-url]: https://github.com/Vincentqyw/cv-arxiv-daily/stargazers
[issues-shield]: https://img.shields.io/github/issues/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[issues-url]: https://github.com/Vincentqyw/cv-arxiv-daily/issues

