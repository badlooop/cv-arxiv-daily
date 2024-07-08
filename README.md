[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]

## Updated on 2024.07.08
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
|**2024-07-05**|**LaRa: Efficient Large-Baseline Radiance Fields**|辐射场方法已经实现了真实感的新视图合成和几何重建。但它们大多应用于逐场景优化或小基线设置。虽然最近的几项工作研究了通过利用变换器进行大基线的前馈重建，但它们都是以标准的全局注意力机制进行操作的，因此忽略了3D重建的局部性质。我们提出了一种在转换器层中统一局部和全局推理的方法，从而提高了质量和更快的收敛速度。我们的模型将场景表示为高斯体积，并将其与图像编码器和组注意力层相结合，以实现高效的前馈重建。实验结果表明，我们的模型在四个GPU上训练了两天，在重建360度辐射场时表现出了高保真度，并对零样本和域外测试表现出了鲁棒性。 et.al.|[2407.04699](http://arxiv.org/abs/2407.04699)|null|
|**2024-07-04**|**VEGS: View Extrapolation of Urban Scenes in 3D Gaussian Splatting using Learned Priors**|基于神经渲染的城市场景重建方法通常依赖于从驾驶车辆中收集的图像，其中摄像机面向前方并向前移动。尽管这些方法可以成功地从与训练相机轨迹相似的视图进行合成，但将新视图引导到训练相机分布之外并不能保证达到标准的性能。在本文中，我们通过评估关于训练相机分布的视图重建（如向左、向右或向下看）来解决外推视图合成（EVS）问题。为了提高EVS的渲染质量，我们通过构建密集的激光雷达图来初始化我们的模型，并提出利用先验场景知识，如表面法线估计器和大规模扩散模型。定性和定量比较证明了我们的方法在EVS上的有效性。据我们所知，我们是第一个解决城市场景重建中EVS问题的人。链接到我们的项目页面：https://vegs3d.github.io/. et.al.|[2407.02945](http://arxiv.org/abs/2407.02945)|null|
|**2024-07-03**|**Free-SurGS: SfM-Free 3D Gaussian Splatting for Surgical Scene Reconstruction**|手术场景的实时3D重建在计算机辅助手术中发挥着至关重要的作用，有望提高外科医生的可视性。3D高斯散射（3DGS）的最新进展显示出在一般场景的实时新颖视图合成方面的巨大潜力，该合成依赖于由运动结构（SfM）生成的精确姿态和点云进行初始化。然而，由于纹理最小和光度不一致的挑战，带有SfM的3DGS无法在手术场景中恢复准确的相机姿势和几何结构。为了解决这个问题，在本文中，我们提出了第一种基于无SfM的3DGS的手术场景重建方法，通过联合优化相机姿态和场景表示。基于视频连续性，我们的方法的关键是利用即时光流先验来引导从3D高斯导出的投影流。与以前大多数只依赖光度损失的方法不同，我们将姿态估计问题公式化为最小化投影流和光流之间的流量损失。进一步引入了一致性检查，通过检测满足核极几何的刚性可靠点来过滤流量异常值。在3D高斯优化过程中，我们随机采样帧以优化场景表示，从而逐步增长3D高斯。在SCARED数据集上的实验表明，与现有方法相比，我们在高效的新视图合成和姿态估计方面具有优越的性能。代码位于https://github.com/wrld/Free-SurGS. et.al.|[2407.02918](http://arxiv.org/abs/2407.02918)|**[link](https://github.com/wrld/free-surgs)**|
|**2024-07-02**|**MomentsNeRF: Leveraging Orthogonal Moments for Few-Shot Neural Rendering**|我们提出了MomentsNeRF，这是一种用于单镜头和少镜头神经渲染的新框架，它使用正交矩来预测3D场景的神经表示。我们的架构提供了一种新的迁移学习方法，用于在多场景上进行训练，并在测试时使用一个或几个图像进行逐场景优化。我们的方法是第一个成功利用从Gabor和Zernike矩中提取的特征，将它们无缝集成到NeRF架构中。我们表明，与最近的单镜头和少镜头神经渲染框架相比，MomentsNeRF在合成具有复杂纹理和形状的图像方面表现更好，实现了显著的降噪、伪影消除和完成缺失部分。在DTU和Shapenet数据集上进行的大量实验表明，MomentsNeRF通过｛3.39\；dB\；PSNR｝、11.1%SSIM、17.9%LPIPS和8.3%DISTS指标改进了最先进的技术。此外，它在新视图合成和单图像3D视图重建方面都优于最先进的性能。源代码可访问：https://amughrabi.github.io/momentsnerf/. et.al.|[2407.02668](http://arxiv.org/abs/2407.02668)|null|
|**2024-07-04**|**AutoSplat: Constrained Gaussian Splatting for Autonomous Driving Scene Reconstruction**|真实场景重建和视图合成对于通过模拟安全关键场景来推进自动驾驶系统至关重要。3D Gaussian Splatting擅长实时渲染和静态场景重建，但由于复杂的背景、动态对象和稀疏的视图，难以对驾驶场景进行建模。我们提出了AutoSplat，这是一个使用高斯飞溅来实现自动驾驶场景的高度逼真重建的框架。通过对表示道路和天空区域的高斯图施加几何约束，我们的方法能够对包括车道变化在内的具有挑战性的场景进行多视图一致模拟。利用3D模板，我们引入了反射高斯一致性约束来监督前景对象的可见和不可见面。此外，为了对前景对象的动态外观进行建模，我们估计了每个前景高斯的残差球面谐波。在Pandaset和KITTI上进行的大量实验表明，AutoSplat在不同驾驶场景下的场景重建和新视图合成方面优于最先进的方法。访问我们的项目页面https://autosplat.github.io/. et.al.|[2407.02598](http://arxiv.org/abs/2407.02598)|null|
|**2024-07-01**|**DRAGON: Drone and Ground Gaussian Splatting for 3D Building Reconstruction**|从成像数据重建三维建筑是从城市规划到侦察等许多应用的重要任务。NeRF和Gaussian Splatting等现代新颖视图合成（NVS）方法为以无监督的方式从自然2D图像开发3D模型提供了强大的技术。这些算法通常需要感兴趣场景周围的输入训练视图，而在大型建筑的情况下，这通常不适用于所有的摄像机立面。特别是，在大多数建筑中，最容易获得的相机视角是在近地面（例如，使用手机）和空中（无人机）高度。然而，由于无人机和地面图像集在视点上的显著差异，相机配准——NVS算法的必要步骤——失败了。在这项工作中，我们提出了一种方法，即DRAGON，它可以将无人机和地面建筑图像作为输入，并生成3D NVS模型。DRAGON的关键见解是，中间高程图像可以通过NVS算法本身在具有感知正则化的迭代过程中外推，从而弥合两个高程之间的视觉特征差距并实现配准。我们使用Google Earth Studio汇编了一个包含9个大型建筑场景的半合成数据集，并从数量和质量上证明，与基线策略相比，DRAGON可以在该数据集上生成引人注目的渲染图。 et.al.|[2407.01761](http://arxiv.org/abs/2407.01761)|null|
|**2024-07-01**|**EndoSparse: Real-Time Sparse View Synthesis of Endoscopic Scenes using Gaussian Splatting**|从一组内窥镜图像中对生物组织进行3D重建是解锁具有3D能力的各种重要下游外科应用的关键。现有的方法使用各种先进的神经渲染技术进行真实感视图合成，但当只有稀疏的观测可用时，它们往往难以恢复准确的3D表示，这在现实世界的临床场景中通常是这样。为了应对这一{稀疏性}挑战，我们提出了一个在重建过程中利用多个基础模型的先验知识的框架，称为\textit{EndoSparse}。实验结果表明，在具有挑战性的稀疏视图条件下，包括仅使用三个视图，我们提出的策略显著提高了几何和外观质量。在针对最先进方法的严格基准测试实验中，\textit｛EndoSparse｝在精确的几何形状、逼真的外观和渲染效率方面取得了优异的结果，证实了内窥镜重建中对稀疏视图限制的稳健性。\textit｛EndoSparse｝标志着神经3D重建在现实世界临床场景中的实际部署迈出了稳步的一步。项目页面：https://endo-sparse.github.io/. et.al.|[2407.01029](http://arxiv.org/abs/2407.01029)|null|
|**2024-06-30**|**Ego-to-Exo: Interfacing Third Person Visuals from Egocentric Views in Real-time for Improved ROV Teleoperation**|水下遥控潜水器是一种无人潜水器，设计用于在海洋深处进行探索和操作。尽管使用了高端相机，但基于第一人称（以自我为中心）视角的典型遥操作引擎限制了水面操作员在复杂深水任务中操纵和导航ROV的能力。在本文中，我们提出了一种交互式遥操作界面，该界面（i）从过去的自我中心视图提供按需的“第三人”（外部中心）视觉效果，以及（ii）通过增强的ROV姿势实时增强外围信息。我们通过将基于3D几何的Ego-to-Exo视图合成算法集成到单目SLAM系统中以实现精确的轨迹估计来实现这一点。所提出的闭合形式解决方案仅使用ROV过去的以自我为中心的视图和SLAM主干进行姿态估计，这使其可移植到现有的ROV平台。与数据驱动的解决方案不同，它对应用程序和水体特定场景是不变的。我们通过在具有挑战性的弱光条件下进行2自由度室内导航和6自由度水下洞穴探索的大量实验，验证了所提出框架的几何精度。我们通过遵循水下洞穴内的洞穴线等导航指南，展示了动态Ego-to-Exo视图生成和实时姿态渲染在远程遥控潜水器遥操作中的优势。这种新的交互式遥控潜水器遥控操作方式为未来的水下遥控机器人研究开辟了广阔的前景。 et.al.|[2407.00848](http://arxiv.org/abs/2407.00848)|null|
|**2024-06-29**|**Intrinsic PAPR for Point-level 3D Scene Albedo and Shading Editing**|神经渲染的最新进展在从多视图RGB图像合成新视图方面表现出色。然而，它们通常缺乏在详细的点级别编辑场景的着色或颜色的能力，同时确保不同视点之间的一致性。在这项工作中，我们解决了点级3D场景反照率和多视图RGB图像的着色编辑的挑战，重点是点级而不是局部或全局级的详细编辑。虽然之前基于体积表示的工作（如NeRF）难以在点级别实现3D一致性编辑，但基于点的神经渲染的最新进展显示出克服这一挑战的前景。我们介绍了“内在PAPR”，这是一种基于最近的基于点的神经绘制技术——接近注意力点绘制（PAPR）的新方法。与其他对场景的内在分解建模的基于点的方法不同，我们的方法不依赖于复杂的着色模型或可能不普遍适用的简单先验。相反，我们直接将场景分解建模为反照率和阴影分量，从而获得更好的估计精度。与最新的基于点的反向渲染方法的比较评估表明，Intrinsic PAPR实现了更高质量的新颖视图渲染和卓越的点级反照率和着色编辑。 et.al.|[2407.00500](http://arxiv.org/abs/2407.00500)|null|
|**2024-06-28**|**ASSR-NeRF: Arbitrary-Scale Super-Resolution on Voxel Grid for High-Quality Radiance Fields Reconstruction**|基于NeRF的方法通过构建具有隐式或显式表示的辐射场来重建3D场景。虽然基于NeRF的方法可以在任意尺度上执行新视图合成（NVS），但在具有低分辨率（LR）优化的高分辨率新视图综合（HRNVS）中的性能往往导致过度平滑。另一方面，单图像超分辨率（SR）旨在将LR图像增强到HR图像，但缺乏多视点一致性。为了应对这些挑战，我们提出了任意尺度超分辨率NeRF（ASSR-NeRF），这是一种用于超分辨率新视图合成（SRNVS）的新框架。我们提出了一种基于注意力的VoxelGridSR模型来直接对优化的体积执行3D超分辨率（SR）。我们的模型在不同的场景中进行了训练，以确保可推广性。对于用LR视图训练的看不见的场景，我们可以直接应用我们的VoxelGridSR来进一步细化体积并实现多视图一致SR。我们从数量和质量上证明了所提出的方法在SRNVS中取得了显著的性能。 et.al.|[2406.20066](http://arxiv.org/abs/2406.20066)|null|

<p align=right>(<a href=#updated-on-20240708>back to top</a>)</p>

## 3D Reconstruction

|Publish Date|Title|Abstract|PDF|Code|
|---|---|---|---|---|
|**2024-07-05**|**LaRa: Efficient Large-Baseline Radiance Fields**|辐射场方法已经实现了真实感的新视图合成和几何重建。但它们大多应用于逐场景优化或小基线设置。虽然最近的几项工作研究了通过利用变换器进行大基线的前馈重建，但它们都是以标准的全局注意力机制进行操作的，因此忽略了3D重建的局部性质。我们提出了一种在转换器层中统一局部和全局推理的方法，从而提高了质量和更快的收敛速度。我们的模型将场景表示为高斯体积，并将其与图像编码器和组注意力层相结合，以实现高效的前馈重建。实验结果表明，我们的模型在四个GPU上训练了两天，在重建360度辐射场时表现出了高保真度，并对零样本和域外测试表现出了鲁棒性。 et.al.|[2407.04699](http://arxiv.org/abs/2407.04699)|null|
|**2024-07-05**|**Rethinking Data Input for Point Cloud Upsampling**|近年来，点云上采样在三维重建和曲面生成等领域得到了广泛的应用。然而，现有的点云上采样输入都是基于补丁的，并且没有研究讨论点云模型全输入和基于补丁的输入之间的差异和原理。为了与基于补丁的点云输入进行比较，本文提出了一种新的数据输入方法，该方法在训练PU-GCN时划分全点云模型以确保形状完整性。本文在PU1K和ABC数据集上进行了验证，但结果表明，基于补丁的性能优于基于模型的全输入，即平均分段输入。因此，本文探讨了影响点云上采样结果的数据输入因素和模型模块。 et.al.|[2407.04476](http://arxiv.org/abs/2407.04476)|null|
|**2024-07-05**|**GSD: View-Guided Gaussian Splatting Diffusion for 3D Reconstruction**|我们提出了一种基于高斯散射（GS）表示的扩散模型方法GSD，用于从单个视图重建3D对象。先前的作品由于不正确的表示而遭受不一致的3D几何结构或平庸的渲染质量。我们通过利用最近最先进的3D显式表示、高斯散射和无条件扩散模型，朝着解决这些缺点迈出了一步。该模型学习生成由GS椭球集合表示的3D对象。有了这些强大的生成3D先验，尽管无条件地学习，但扩散模型可以在没有进一步模型微调的情况下进行视图引导重建。这是通过高效而灵活的飞溅函数和引导的去噪采样过程传播细粒度的2D特征来实现的。此外，还采用2D扩散模型来增强渲染保真度，并通过抛光和重新使用渲染图像来提高重建的GS质量。最终重建的对象明确地具有高质量的3D结构和纹理，并且可以在任意视图中有效地渲染。在具有挑战性的真实世界CO3D数据集上的实验证明了我们方法的优越性。 et.al.|[2407.04237](http://arxiv.org/abs/2407.04237)|null|
|**2024-07-04**|**SfM on-the-fly: Get better 3D from What You Capture**|在过去的二十年里，运动结构（SfM）一直是摄影测量、计算机视觉、机器人等领域的研究热点，而实时性能正是最近人们越来越感兴趣的话题。这项工作建立在原始的动态SfM（Zhan et al.，2024）的基础上，并提出了一个更新版本，其中包含三个新的进步，以从您捕获的图像中获得更好的3D效果：（i）通过使用分层导航小世界（HNSW）图，进一步增强了实时图像匹配，从而更快地识别出更多真实的正重叠图像候选者；（ii）提出了一种自适应加权策略，用于鲁棒的分层局部束调整，以改进SfM结果；（iii）包括多个代理用于支持协作SfM，并且当出现共同注册的图像时将多个3D重建无缝地合并到完整的3D场景中。各种综合实验表明，所提出的SfM方法（实时命名为SfMv2）可以以高效的方式生成更完整、更稳健的3D重建。代码位于http://yifeiyu225.github.io/on-the-flySfMv2.github.io/. et.al.|[2407.03939](http://arxiv.org/abs/2407.03939)|null|
|**2024-07-04**|**Beyond Viewpoint: Robust 3D Object Recognition under Arbitrary Views through Joint Multi-Part Representation**|现有的基于视图的方法擅长于从预定义的视点识别3D对象，但它们在任意视图下的识别探索是有限的。这是一个具有挑战性和现实性的设置，因为每个对象都有不同的视点位置和数量，并且它们的姿势不对齐。然而，大多数基于视图的方法，即聚合多个视图特征以获得全局特征表示，很难解决任意视图下的三维对象识别问题。由于来自任意视图的未对齐输入，稳健地聚合特征是一项挑战，导致性能下降。在本文中，我们介绍了一种新的部件感知网络（PANet），它是一种基于部件的表示，以解决这些问题。这种基于零件的表示旨在定位和理解3D对象的不同零件，如飞机机翼和尾部。它具有视点不变性和旋转鲁棒性等特性，这使它在解决任意视图下的三维对象识别问题时具有优势。我们在基准数据集上的结果清楚地表明，对于任意视图下的3D对象识别任务，我们提出的方法优于现有的基于视图的聚合基线，甚至超过了大多数固定视点方法。 et.al.|[2407.03842](http://arxiv.org/abs/2407.03842)|null|
|**2024-07-03**|**Free-SurGS: SfM-Free 3D Gaussian Splatting for Surgical Scene Reconstruction**|手术场景的实时3D重建在计算机辅助手术中发挥着至关重要的作用，有望提高外科医生的可视性。3D高斯散射（3DGS）的最新进展显示出在一般场景的实时新颖视图合成方面的巨大潜力，该合成依赖于由运动结构（SfM）生成的精确姿态和点云进行初始化。然而，由于纹理最小和光度不一致的挑战，带有SfM的3DGS无法在手术场景中恢复准确的相机姿势和几何结构。为了解决这个问题，在本文中，我们提出了第一种基于无SfM的3DGS的手术场景重建方法，通过联合优化相机姿态和场景表示。基于视频连续性，我们的方法的关键是利用即时光流先验来引导从3D高斯导出的投影流。与以前大多数只依赖光度损失的方法不同，我们将姿态估计问题公式化为最小化投影流和光流之间的流量损失。进一步引入了一致性检查，通过检测满足核极几何的刚性可靠点来过滤流量异常值。在3D高斯优化过程中，我们随机采样帧以优化场景表示，从而逐步增长3D高斯。在SCARED数据集上的实验表明，与现有方法相比，我们在高效的新视图合成和姿态估计方面具有优越的性能。代码位于https://github.com/wrld/Free-SurGS. et.al.|[2407.02918](http://arxiv.org/abs/2407.02918)|**[link](https://github.com/wrld/free-surgs)**|
|**2024-07-03**|**A Radiometric Correction based Optical Modeling Approach to Removing Reflection Noise in TLS Point Clouds of Urban Scenes**|点云在三维重建、自动驾驶和机器人等计算机视觉任务中至关重要。然而，TLS获取的点云通常包含来自反射表面的虚拟点，从而导致中断。本文提出了一种TLS点云的反射噪声消除算法。我们创新的反射平面检测算法基于几何光学模型和物理特性，根据光学反射理论识别和分类反射点。我们对LSFH特征描述符进行了调整，以保留反射特征，从而减少对称架构结构的干扰。通过引入Hausdorff特征距离，该算法增强了对重影和变形的恢复能力，提高了虚拟点检测的准确性。在具有虚拟TLS反射噪声的不同城市环境的3DRN基准数据集上进行的大量实验表明，我们的算法将反射区域中3D点的精度和召回率分别提高了57.03\%和31.80\%。我们的方法比领先的方法提高了9.17%的异常值检测率和5.65%的准确率。访问3DRN数据集(https://github.com/Tsuiky/3DRN). et.al.|[2407.02830](http://arxiv.org/abs/2407.02830)|null|
|**2024-07-02**|**The influence of the 3D Galactic gas structure on cosmic-ray transport and gamma-ray emission**|宇宙射线（CR）在星际介质（ISM）的动力学中起着重要作用。它们的相互作用和传输电离、加热并推动ISM，从而耦合ISM的不同区域。CR的空间分布取决于其来源的分布以及它们相互作用的ISM成分，如气体、星光和磁场。特别是，气体与CR密切相互作用，影响CR通量和伽马射线发射。我们说明了三维气体结构对CR传输和伽马射线发射的影响。我们使用PICARD代码和最近HI和H $_2$ 银河系气体成分的多个3D重建样本来研究对CR传输和伽马射线发射的影响。我们找到了必要的输运参数来再现CR通量的局部测量，并发现它们取决于气体密度和结构的局部分布。CR通量的分布表现出与能量相关的结构，由于其相应的损失过程，所有CR物种都会发生变化。增强的次级（初级）物种的区域与气体密度在空间上相关（反相关）。我们观察到伽马射线发射对气体结构对比度的高灵敏度，因为这些结构决定了强子相互作用和韧致辐射的三维空间分布。我们发现在逆康普顿（IC）发射中也可以看到CR电子分布中相应的气体诱导结构。由于上述敏感性，对CR源和输送参数的CR数据的分析需要使用准确的3D气体图。 et.al.|[2407.02410](http://arxiv.org/abs/2407.02410)|null|
|**2024-07-02**|**Indoor 3D Reconstruction with an Unknown Camera-Projector Pair**|基于结构光的摄像机-投影对（CPP）方法在室内三维重建中起着至关重要的作用，尤其是对于纹理较弱的场景。以前的方法通常假设已知的本质，这些本质是从已知物体中预先校准的，或者是从多视图观测中自我校准的。在没有任何已知对象的情况下，仅从两个视图可靠地恢复CPP内部函数仍然具有挑战性。在本文中，我们提供了一个简单而可靠的解决方案。我们首次证明，可以从未知的长方体角（C2），例如房间的角，导出对CPP本质的足够约束，这是室内场景中的常见结构。此外，在只有已知相机主点的情况下，所有CPP本质的复杂多变量估计可以简化为一个简单的单变量优化问题，从而实现可靠的校准，从而在未知CPP的情况下直接进行3D重建。大量结果表明，与传统方法和基于学习的方法相比，所提出的方法具有优越性。此外，所提出的方法还展示了在没有主动照明的情况下解决类似任务的巨大潜力，例如来自运动的稀疏视图结构。 et.al.|[2407.01945](http://arxiv.org/abs/2407.01945)|null|
|**2024-07-02**|**PO-MSCKF: An Efficient Visual-Inertial Odometry by Reconstructing the Multi-State Constrained Kalman Filter with the Pose-only Theory**|有效的视觉惯性里程计（VIO）对于有效载荷受限的机器人至关重要。尽管现代基于优化的算法已经实现了优越的精度，但基于MSCKF的VIO算法仍然因其高效和一致的性能而被广泛要求。由于MSCKF建立在传统的多视图几何结构上，因此测量的残差不仅与状态误差有关，而且与特征位置误差有关。为了应用EKF融合，需要投影过程来消除观测模型中的特征位置误差，这可能导致模型和精度下降。为了获得有效的视觉惯性融合模型，同时保持模型的一致性，我们提出用新的仅姿态（PO）多视图几何描述来重建MSCKF-VIO。在新构建的滤波器中，我们对PO重投影残差进行了建模，这些残差仅与运动状态相关，从而克服了空间投影的要求。此外，新滤波器不需要任何特征位置信息，这消除了由3D重建过程带来的计算成本和线性化误差。我们在多个数据集上进行了全面的实验，其中所提出的方法在具有挑战性的序列中显示出准确性的提高和一致的性能。 et.al.|[2407.01888](http://arxiv.org/abs/2407.01888)|null|

<p align=right>(<a href=#updated-on-20240708>back to top</a>)</p>

## Diffusion

|Publish Date|Title|Abstract|PDF|Code|
|---|---|---|---|---|
|**2024-07-05**|**Two methods to analyse radial diffusion ensembles: the peril of space- and time- dependent diffusion**|地球外辐射带中的粒子动力学可以使用扩散框架进行建模，其中通过单个绝热不变量 $L^{*}$``（L）“$的扩散方程来捕捉大规模电子运动。虽然系综模型被用来表示物理不确定性，但迄今为止还没有有效的方法来分析辐射带系综。由于扩散系数$D_{LL}$取决于$L$，因此与域相关的扩散使比较变得复杂。我们导出了两种分析系综成员的工具：时间到单调性$t_m$和质量/能量矩量$\mathcal{N}，\mathcal｛E}$。我们发现Jacobian（$1/L^ 2$）对于辐射带误差度量是必要的。显式计算$\partial\mathcal｛E｝/\partial t$的分量，以比较外部和内部边界条件以及损耗对正在进行的扩散的影响。使用$t_m$、$\mathcal{N｝$和$\mathcal{E｝$，我们发现：（a）外部边界条件和位置的不同物理动机选择导致不同的最终状态和不同的进化率；（b） 粒子分布的梯度比$D_{LL}$更显著地影响进化；（c） 增强位置和初始背景粒子的数量都是决定系统演化的重要因素；（d） 俯仰角散射损失通常占主导地位；它减轻但没有消除由于$D_{LL}$的$L$ 依赖性而引起的初始条件和外部边界设置的影响。我们预计，这项研究将促使人们重新关注辐射带建模中的分布梯度、外边界的位置和性质，并为系统的系综建模提供基础。 et.al.|[2407.04669](http://arxiv.org/abs/2407.04669)|null|
|**2024-07-05**|**Strongly consistent low-dissipation WENO schemes for finite elements**|对于守恒定律的连续和不连续Galerkin离散化，我们提出了一种在基于耗散的WENO稳定背景下保持强一致性和便于误差分析的方法。继Kuzmin和Vedral（J.Comput.Phys.487:1121532023）和Vedrar（arXiv预印本arXiv:2309.1919）之后，我们使用WENO冲击检测器来确定适当量的低阶人工粘度。与现有的WENO方法相比，我们的方法使用基于残差的非线性权重混合候选多项式。如果残差消失，我们的稳定伽辽金方法的冲击捕获项就会消失。与弱一致的替代方法相比，这使我们能够实现更高的精度。正如我们在稳态对流扩散反应（CDR）方程的上下文中所示，非线性局部投影稳定项可以以保持局部双线性形式的矫顽力的方式包含。对于CDR问题的相应Galerkin-WENO离散化，我们严格推导了先验误差估计。此外，我们还通过双曲守恒律及其系统的一维和二维数值实验证明了该方法的稳定性和准确性。代表性测试问题的数值结果优于传统WENO方案，特别是在涉及冲击和陡峭梯度的情况下。 et.al.|[2407.04646](http://arxiv.org/abs/2407.04646)|null|
|**2024-07-05**|**Randomized Physics-Informed Neural Networks for Bayesian Data Assimilation**|我们提出了一种随机物理知情神经网络（PINN）或rPINN方法，用于带噪声数据的偏微分方程反问题的不确定性量化。该方法用于量化逆PDE PINN解中的不确定性。最近，提出了贝叶斯PINN（BPINN）方法，其中使用贝叶斯定理来公式化PINN参数的后验分布，并使用近似推理方法（如哈密顿蒙特卡罗（HMC）和变分推理（VI）方法）进行采样。在这项工作中，我们证明了HMC不能收敛于非线性逆PDE问题。作为HMC的替代方案，我们通过求解通过将PINN损失函数随机化而获得的随机优化问题来对分布进行采样。对线性和非线性泊松方程以及具有高维空间相关扩散系数的扩散方程测试了rPINN方法的有效性。rPINN方法为所有考虑的问题提供了信息分布。对于线性泊松方程，HMC和rPINN产生相似的分布，但rPINN平均比HMC快27倍。对于非线性Poison和扩散方程，HMC方法无法收敛，因为单个HMC链无法在合理的时间内对PINN参数的后验分布的多个模式进行采样。 et.al.|[2407.04617](http://arxiv.org/abs/2407.04617)|null|
|**2024-07-05**|**An SDE Perspective on Stochastic Inertial Gradient Dynamics with Time-Dependent Viscosity and Geometric Damping**|我们的方法是连续耗散动力系统和优化算法之间紧密联系的一部分。我们的目标是通过由目标函数的梯度驱动的随机惯性微分方程来求解凸最小化问题。这将为分析具有随机梯度输入的快速优化算法提供一个通用的数学框架。我们的研究是我们之前致力于一阶时间随机最陡下降的工作的自然扩展。我们的目标是通过考虑时间上的二阶随机微分方程，结合粘性时间相关阻尼和Hessian驱动阻尼，进一步发展这些结果。为了开发这个程序，我们依赖于随机李雅普诺夫分析。假设扩散项乘以依赖于粘性阻尼的函数的平方可积条件，并且Hessian驱动阻尼是一个正常数，我们的第一个主要结果表明，几乎可以肯定，这些值是收敛的，并说明这些值在预期中是快速收敛的。此外，在Hessian驱动阻尼为零的情况下，我们得出了预期值的快速收敛的结论，并且在几乎可以肯定的意义上，我们还成功地证明了轨迹的几乎可以肯定弱收敛。我们通过在凸和强凸情况下建立几个新的逐点和遍历收敛率来提供全面的复杂性分析。 et.al.|[2407.04562](http://arxiv.org/abs/2407.04562)|null|
|**2024-07-05**|**Structural Constraint Integration in Generative Model for Discovery of Quantum Material Candidates**|数十亿的有机分子是已知的，但只有一小部分功能性无机材料被发现，这是一个与寻找新量子材料的社区特别相关的问题。基于机器学习的生成模型，特别是扩散模型的最新进展，显示出生成新的、稳定的材料的巨大前景。然而，将几何图案集成到材质生成中仍然是一个挑战。在这里，我们介绍了GENerative模型（SCIGEN）中的结构约束集成。我们的方法可以通过在每个扩散步骤之前用扩散约束结构对去噪结构进行策略掩蔽来修改任何训练的生成扩散模型，以将生成引向约束输出。此外，我们从数学上证明了SCIGEN有效地从原始分布执行条件采样，这对于生成稳定的受约束材料至关重要。我们使用阿基米德晶格作为原型约束生成了800万种化合物，其中超过10%的化合物在多阶段稳定性预筛选中存活下来。对26000种幸存化合物的高通量密度泛函理论（DFT）表明，超过50%的化合物在DFT水平上通过了结构优化。由于量子材料的性质与几何图案密切相关，我们的结果表明，SCIGEN为生成量子材料候选者提供了一个通用框架。 et.al.|[2407.04557](http://arxiv.org/abs/2407.04557)|null|
|**2024-07-05**|**More is Different: Mobile Ions Improve the Design Tolerances of Perovskite Solar Cells**|金属卤化物钙钛矿太阳能电池（PSC）性能的许多最新进展归因于表面处理，其钝化界面陷阱态，最大限度地减少电荷复合并提高光电压。令人惊讶的是，这些光电压超过了电池的内置电势，通常在钙钛矿和传输层半导体带边缘之间有很大的能量偏移，这与标准的光伏设计原理相矛盾。在这里，我们表明这种对能量偏移的耐受性是由钙钛矿层中的混合离子/电子传导引起的。将漂移扩散模拟与探索PSCs的电流-电压性能作为离子分布的函数的实验相结合，我们证明了离子电荷的静电再分配在稳态下减少了表面复合电流，使光电压增加了几十到几百毫伏。因此，可移动离子可以降低光电压对钙钛矿/传输层界面处的能量错位的敏感性，从而有利于整体效率。在这些见解的基础上，我们展示了如何修改光伏设计原理以考虑移动离子。 et.al.|[2407.04523](http://arxiv.org/abs/2407.04523)|null|
|**2024-07-05**|**Unified continuous-time q-learning for mean-field game and mean-field control problems**|本文从代表agent的角度研究了平均场跳跃扩散模型中的连续时间q学习。为了克服种群分布可能无法直接观测的挑战，我们引入了解耦形式的积分q函数（解耦Iq函数），并将其与值函数一起建立了鞅刻画，为平均场对策（MFG）和平均场控制（MFC）问题提供了统一的策略评估规则。此外，根据解决MFG或MFC问题的任务，我们可以通过不同的方法使用解耦的Iq函数来分别学习平均场平衡策略或平均场最优策略。因此，我们利用源于平均场相互作用的所有测试策略，为MFG和MFC问题设计了一个统一的q-学习算法。对于跳跃扩散设置中的几个例子，在LQ框架内外，我们可以获得解耦的Iq函数和值函数的精确参数化，并从代表代理的角度说明我们的算法，具有令人满意的性能。 et.al.|[2407.04521](http://arxiv.org/abs/2407.04521)|null|
|**2024-07-05**|**G-Adaptive mesh refinement -- leveraging graph neural networks and differentiable finite element solvers**|我们提出了一种新的、有效的方法来解决有限元方法中长期存在的网格自适应问题。有限元求解器是求解偏微分方程（PDE）的强大工具，但其成本和精度严重取决于网格点的选择。为了保持较低的计算成本，网格重定位（r-adaptivity）寻求优化固定数量的网格点的位置，以获得最佳的有限元解精度。解决这个问题的经典方法需要解决单独的非线性“网格”PDE来找到网格点的位置。这在重新网格化时产生了显著的成本，并且依赖于某些先验假设和指导启发式方法来获得最佳网格点位置。最近的r自适应机器学习方法主要集中在为这些经典方法构建快速代理。我们的新方法将图神经网络（GNN）驱动的架构与基于相对于网格点位置的有限元解误差的直接最小化的训练相结合。GNN采用图神经扩散（GRAND），将网格解空间与经典网格方法的网格解空间紧密对齐，从而用可学习的策略取代启发式，并提供强大的归纳偏差。这允许快速和稳健的训练，并产生一种极其高效和有效的在线r自适应GNN方法。在我们考虑的测试问题上，该方法优于经典和先验ML方法进行r自适应网格划分，特别是实现了较低的有限元解误差，同时保持了比先验ML工作中观察到的经典方法显著的加速。 et.al.|[2407.04516](http://arxiv.org/abs/2407.04516)|null|
|**2024-07-05**|**Analysis of SIR Reaction diffusion system with constant birth and death rate**|这是对伦敦帝国理工学院二年级小组项目的删减。本文考虑一个包含出生率和死亡率的SIR模型的双线性反应扩散系统。我们首先证明了非负性和全局存在性定理，以确保模型是有意义的。我们证明了无感染解的一致收敛性，并研究了可分离解可以计算的一个例子。我们还研究了稳态解，证明了解的非唯一性，并研究了一般解的正则性。最后，我们还介绍了一个有趣的现象，即由模型中的扩散引起的图灵不稳定性。 et.al.|[2407.04509](http://arxiv.org/abs/2407.04509)|null|
|**2024-07-05**|**Speed-accuracy trade-off for the diffusion models: Wisdom from nonequlibrium thermodynamics and optimal transport**|我们讨论了一个称为扩散模型的生成模型和福克-普朗克方程的非平衡热力学之间的联系，称为随机热力学。基于随机热力学技术，我们推导了扩散模型的速度-精度权衡，这是扩散模型中数据生成的速度和精度之间的权衡关系。我们的结果表明，正向过程中的熵产生率会影响数据生成中的误差。从随机热力学的角度来看，我们的结果为如何最好地生成扩散模型中的数据提供了定量的见解。最优学习协议是由随机热力学中的保守力和最优传输理论中的2-Wasserstein距离引入的空间测地线引入的。我们数值说明了具有不同噪声调度（如余弦调度、条件最优传输和最优传输）的扩散模型的速度-精度权衡的有效性。 et.al.|[2407.04495](http://arxiv.org/abs/2407.04495)|null|

<p align=right>(<a href=#updated-on-20240708>back to top</a>)</p>

## NeRF

|Publish Date|Title|Abstract|PDF|Code|
|---|---|---|---|---|
|**2024-07-01**|**Fast and Efficient: Mask Neural Fields for 3D Scene Segmentation**|理解3D场景是计算机视觉研究中的一个关键挑战，其应用涉及多个领域。在将2D视觉语言基础模型提取到神经领域（如NeRF和3DGS）方面的最新进展，使得能够从2D多视图图像中对3D场景进行开放式词汇分割，而无需精确的3D注释。然而，虽然有效，但高维CLIP特征的每像素提取引入了模糊性，并需要复杂的正则化策略，从而增加了训练过程中的低效率。本文提出了MaskField，它可以在弱监督下使用神经场实现快速高效的三维开放词汇分割。与以前的方法不同，MaskField提取的是遮罩，而不是密集的高维CLIP特征。MaskFields使用神经场作为二进制掩码生成器，并使用SAM生成的掩码对其进行监督，并根据粗略的CLIP特征进行分类。MaskField通过在训练过程中自然引入SAM分割的对象形状而无需额外的正则化，克服了模糊的对象边界。通过避免在训练过程中直接处理高维CLIP特征，MaskField与3DGS等显式场景表示特别兼容。我们的大量实验表明，MaskField不仅超越了现有的最先进的方法，而且实现了显著的快速收敛，仅需5分钟的训练就超过了以前的方法。我们希望MaskField将激励人们进一步探索如何训练神经场来从2D模型中理解3D场景。 et.al.|[2407.01220](http://arxiv.org/abs/2407.01220)|null|
|**2024-07-01**|**3D Feature Distillation with Object-Centric Priors**|将自然语言与物理世界联系起来是一个普遍存在的话题，在计算机视觉和机器人领域有着广泛的应用。最近，像CLIP这样的2D视觉语言模型已经被广泛普及，因为它们在2D图像中具有令人印象深刻的开放词汇基础能力。最近的工作旨在通过特征提取将2D CLIP特征提升到3D，但要么学习特定于场景的神经场，因此缺乏泛化能力，要么专注于需要访问多个相机视图的室内房间扫描数据，这在机器人操作场景中是不现实的。此外，相关方法通常在像素级融合特征，并假设所有相机视图的信息量相等。在这项工作中，我们证明了这种方法在基础精度和分割清晰度方面都会导致次优的3D特征。为了缓解这种情况，我们提出了一种多视图特征融合策略，该策略采用以对象为中心的先验来消除基于语义信息的无信息视图，并通过实例分割掩码在对象级别融合特征。为了提取我们以对象为中心的3D特征，我们生成了一个杂乱桌面场景的大规模合成多视图数据集，从3300多个独特的对象实例中生成了15k个场景，并将其公开。我们表明，我们的方法在从单视图RGB-D重建3D CLIP特征的同时，具有改进的接地能力和空间一致性，从而偏离了测试时多个相机视图的假设。最后，我们证明了我们的方法可以推广到新的桌面领域，并在不进行微调的情况下重新用于3D实例分割，并证明了它在语言引导的机器人抓取中的实用性 et.al.|[2406.18742](http://arxiv.org/abs/2406.18742)|null|
|**2024-06-25**|**Masked Generative Extractor for Synergistic Representation and 3D Generation of Point Clouds**|在2D图像生成建模和表示学习领域，掩模生成编码器（MAGE）已经证明了生成建模与表示学习之间的协同潜力。受此启发，我们提出了Point MAGE，将这一概念扩展到点云数据。具体而言，该框架首先利用矢量量化变分自动编码器（VQVAE）来重建3D形状的神经场表示，从而学习点块的离散语义特征。随后，通过将掩蔽模型与可变掩蔽比相结合，我们实现了生成和表示学习的同步训练。此外，我们的框架与现有的点云自监督学习（SSL）模型无缝集成，从而提高了它们的性能。我们广泛评估了Point MAGE的表示学习和生成能力。在形状分类任务中，Point MAGE在ModelNet40数据集上的准确率为94.2%，在ScanObjectNN数据集上达到92.9%（+1.3%）。此外，它在少量镜头学习和零件分割任务中实现了最先进的性能。实验结果还证实，点MAGE可以在无条件和有条件的设置中生成详细和高质量的3D形状。 et.al.|[2406.17342](http://arxiv.org/abs/2406.17342)|null|
|**2024-06-17**|**DistillNeRF: Perceiving 3D Scenes from Single-Glance Images by Distilling Neural Fields and Foundation Model Features**|我们提出了DistilleNeRF，这是一种自监督学习框架，解决了在自动驾驶中从有限的2D观测中理解3D环境的挑战。我们的方法是一个可推广的前馈模型，它从稀疏的单帧多视图相机输入中预测丰富的神经场景表示，并通过可微分渲染进行自监督训练，以重建RGB、深度或特征图像。我们的第一个见解是通过生成密集的深度和虚拟相机目标进行训练，利用每场景优化的神经辐射场（NeRF），从而帮助我们的模型从稀疏的非重叠图像输入中学习3D几何。其次，为了学习语义丰富的3D表示，我们建议从预先训练的2D基础模型（如CLIP或DINOv2）中提取特征，从而实现各种下游任务，而不需要昂贵的3D人工注释。为了利用这两个见解，我们引入了一种新的模型架构，该架构具有两级提升-飞溅-拍摄编码器和参数化稀疏分层体素表示。在NuScenes数据集上的实验结果表明，DistilleNeRF在场景重建、新视图合成和深度估计方面显著优于现有的可比自监督方法；并且它允许竞争性的零样本3D语义占用预测，以及通过提取的基础模型特征来理解开放世界场景。演示和代码将在https://distillnerf.github.io/. et.al.|[2406.12095](http://arxiv.org/abs/2406.12095)|null|
|**2024-06-18**|**Effective Rank Analysis and Regularization for Enhanced 3D Gaussian Splatting**|从多视图图像中进行三维重建是计算机视觉和图形学的基本挑战之一。近年来，三维高斯散射（3DGS）已经成为一种很有前途的技术，能够实时渲染和高质量的三维重建。该方法利用了三维高斯表示和基于瓦片的飞溅技术，绕过了昂贵的神经场查询。尽管3DGS具有潜力，但由于高斯收敛为具有一个主导方差的各向异性高斯，3DGS仍面临挑战，包括针状伪影、次优几何结构和不准确法线。我们建议使用有效秩分析来检查3D高斯基元的形状统计，并识别高斯确实收敛为有效秩为1的针状形状。为了解决这个问题，我们引入了有效秩作为正则化，它约束高斯的结构。我们的新正则化方法增强了法线和几何重建，同时减少了针状伪影。该方法可以作为附加模块集成到其他3DGS变体中，在不影响视觉逼真度的情况下提高其质量。 et.al.|[2406.11672](http://arxiv.org/abs/2406.11672)|null|
|**2024-06-13**|**Well-posedness and regularity of solutions to neural field problems with dendritic processing**|我们研究了最近提出的神经场模型的解决方案，在该模型中，树突被建模为源自体细胞层的垂直纤维的连续体。由于电压通过具有非局部源的电缆方程沿树枝状方向传播，因此该模型具有各向异性扩散算子以及突触耦合的积分项。因此，相应的柯西问题与经典的神经场方程明显不同。我们证明了问题的弱公式允许一个唯一的解，嵌入估计类似于非线性局部反应扩散方程的嵌入估计。我们的分析依赖于无扩散问题的扰动弱解，即标准神经场，迄今为止尚未对其弱问题进行研究。我们找到了有扩散和无扩散问题的严格渐近估计，并证明了这两个模型的解在有限时间间隔上在适当的范数下保持接近。我们提供了微扰结果的数值证据。 et.al.|[2406.09222](http://arxiv.org/abs/2406.09222)|null|
|**2024-06-13**|**Preserving Identity with Variational Score for General-purpose 3D Editing**|我们提出了Piva（用变分分数蒸馏保持同一性），这是一种新的基于优化的方法，用于编辑基于扩散模型的图像和3D模型。具体来说，我们的方法受到了最近提出的2D图像编辑方法——德尔塔去噪分数（DDS）的启发。我们指出了DDS在二维和三维编辑中的局限性，这会导致细节丢失和过饱和。为了解决这一问题，我们提出了一个额外的分数提取术语，以强制执行身份保护。这导致了更稳定的编辑过程，逐步优化NeRF模型以匹配目标提示，同时保留关键的输入特征。我们证明了我们的方法在零样本图像和神经场编辑中的有效性。我们的方法成功地改变了视觉属性，添加了微妙和实质性的结构元素，转换了形状，并在标准的2D和3D编辑基准上取得了有竞争力的结果。此外，我们的方法没有施加任何约束，如掩蔽或预训练，使其与广泛的预训练扩散模型兼容。这允许进行多功能编辑，而不需要神经场到网格的转换，提供更用户友好的体验。 et.al.|[2406.08953](http://arxiv.org/abs/2406.08953)|null|
|**2024-06-12**|**Category-level Neural Field for Reconstruction of Partially Observed Objects in Indoor Environment**|通过各种成功案例，神经隐式表示在三维重建中引起了人们的关注。对于进一步的应用，如场景理解或编辑，一些作品已经显示出在对象组成重建方面的进展。尽管它们在观测区域具有优越的性能，但在重建部分观测到的对象时，它们的性能仍然有限。为了更好地处理这个问题，我们引入了类别级神经场，该神经场在场景中属于同一类别的对象之间学习有意义的公共3D信息。我们的主要想法是根据观察到的形状对对象进行子分类，以便更好地训练类别级模型。然后，我们利用神经场，通过选择基于射线的不确定性选择的代表性对象并与之对齐，来执行配准部分观测对象的挑战性任务。在模拟和真实世界数据集上的实验表明，我们的方法改进了几个类别的未观察零件的重建。 et.al.|[2406.08176](http://arxiv.org/abs/2406.08176)|**[link](https://github.com/Taekbum/category-nerf-reconstruction-official)**|
|**2024-06-12**|**OpenObj: Open-Vocabulary Object-Level Neural Radiance Fields with Fine-Grained Understanding**|近年来，人们对由视觉语言模型（VLM）促进的开放词汇三维场景重建产生了浓厚的兴趣，VLM在开放集检索中展示了非凡的能力。然而，现有的方法面临一些局限性：它们要么专注于学习逐点特征，导致语义理解模糊，要么只处理对象级重建，从而忽略对象内部的复杂细节。为了应对这些挑战，我们引入了OpenObj，这是一种创新的方法，用于构建具有细粒度理解的开放词汇表对象级神经辐射场（NeRF）。从本质上讲，OpenObj建立了一个健壮的框架，用于在对象级别进行高效和严密的场景建模和理解。此外，我们将零件级特征融入神经领域，从而实现物体内部的细致入微的表示。这种方法捕获对象级实例，同时保持细粒度的理解。在多个数据集上的结果表明，OpenObj在零样本语义分割和检索任务中取得了优异的性能。此外，OpenObj支持多尺度的真实世界机器人任务，包括全局移动和局部操纵。 et.al.|[2406.08009](http://arxiv.org/abs/2406.08009)|**[link](https://github.com/BIT-DYN/OpenObj)**|
|**2024-06-11**|**Image Neural Field Diffusion Models**|扩散模型在对复杂数据分布建模方面表现出了令人印象深刻的能力，与GANs相比具有几个关键优势，例如稳定的训练、更好地覆盖训练分布的模式，以及在没有额外训练的情况下解决反问题的能力。然而，大多数扩散模型学习固定分辨率图像的分布。我们建议通过在图像神经场上训练扩散模型来学习连续图像的分布，该模型可以以任何分辨率渲染，并显示出其相对于固定分辨率模型的优势。为了实现这一点，一个关键的挑战是获得一个代表真实感图像神经场的潜在空间。受最近几项技术的启发，我们提出了一种简单有效的方法，但有一些关键的变化，使图像神经场具有真实感。我们的方法可以用于将现有的潜在扩散自动编码器转换为图像神经场自动编码器。我们证明，图像神经场扩散模型可以使用混合分辨率图像数据集进行训练，优于固定分辨率扩散模型和超分辨率模型，并且可以有效地解决不同尺度条件下的逆问题。 et.al.|[2406.07480](http://arxiv.org/abs/2406.07480)|null|

<p align=right>(<a href=#updated-on-20240708>back to top</a>)</p>

[contributors-shield]: https://img.shields.io/github/contributors/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[contributors-url]: https://github.com/Vincentqyw/cv-arxiv-daily/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[forks-url]: https://github.com/Vincentqyw/cv-arxiv-daily/network/members
[stars-shield]: https://img.shields.io/github/stars/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[stars-url]: https://github.com/Vincentqyw/cv-arxiv-daily/stargazers
[issues-shield]: https://img.shields.io/github/issues/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[issues-url]: https://github.com/Vincentqyw/cv-arxiv-daily/issues

