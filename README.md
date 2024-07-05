[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]

## Updated on 2024.07.05
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
|**2024-07-03**|**VEGS: View Extrapolation of Urban Scenes in 3D Gaussian Splatting using Learned Priors**|基于神经渲染的城市场景重建方法通常依赖于从驾驶车辆中收集的图像，其中摄像机面向前方并向前移动。尽管这些方法可以成功地从与训练相机轨迹相似的视图进行合成，但将新视图引导到训练相机分布之外并不能保证达到标准的性能。在本文中，我们通过评估关于训练相机分布的视图重建（如向左、向右或向下看）来解决外推视图合成（EVS）问题。为了提高EVS的渲染质量，我们通过构建密集的激光雷达图来初始化我们的模型，并提出利用先验场景知识，如表面法线估计器和大规模扩散模型。定性和定量比较证明了我们的方法在EVS上的有效性。据我们所知，我们是第一个解决城市场景重建中EVS问题的人。链接到我们的项目页面：https://vegs3d.github.io/. et.al.|[2407.02945](http://arxiv.org/abs/2407.02945)|null|
|**2024-07-03**|**Free-SurGS: SfM-Free 3D Gaussian Splatting for Surgical Scene Reconstruction**|手术场景的实时3D重建在计算机辅助手术中发挥着至关重要的作用，有望提高外科医生的可视性。3D高斯散射（3DGS）的最新进展显示出在一般场景的实时新颖视图合成方面的巨大潜力，该合成依赖于由运动结构（SfM）生成的精确姿态和点云进行初始化。然而，由于纹理最小和光度不一致的挑战，带有SfM的3DGS无法在手术场景中恢复准确的相机姿势和几何结构。为了解决这个问题，在本文中，我们提出了第一种基于无SfM的3DGS的手术场景重建方法，通过联合优化相机姿态和场景表示。基于视频连续性，我们的方法的关键是利用即时光流先验来引导从3D高斯导出的投影流。与以前大多数只依赖光度损失的方法不同，我们将姿态估计问题公式化为最小化投影流和光流之间的流量损失。进一步引入了一致性检查，通过检测满足核极几何的刚性可靠点来过滤流量异常值。在3D高斯优化过程中，我们随机采样帧以优化场景表示，从而逐步增长3D高斯。在SCARED数据集上的实验表明，与现有方法相比，我们在高效的新视图合成和姿态估计方面具有优越的性能。代码位于https://github.com/wrld/Free-SurGS. et.al.|[2407.02918](http://arxiv.org/abs/2407.02918)|null|
|**2024-07-02**|**MomentsNeRF: Leveraging Orthogonal Moments for Few-Shot Neural Rendering**|我们提出了MomentsNeRF，这是一种用于单镜头和少镜头神经渲染的新框架，它使用正交矩来预测3D场景的神经表示。我们的架构提供了一种新的迁移学习方法，用于在多场景上进行训练，并在测试时使用一个或几个图像进行逐场景优化。我们的方法是第一个成功利用从Gabor和Zernike矩中提取的特征，将它们无缝集成到NeRF架构中。我们表明，与最近的单镜头和少镜头神经渲染框架相比，MomentsNeRF在合成具有复杂纹理和形状的图像方面表现更好，实现了显著的降噪、伪影消除和完成缺失部分。在DTU和Shapenet数据集上进行的大量实验表明，MomentsNeRF通过｛3.39\；dB\；PSNR｝、11.1%SSIM、17.9%LPIPS和8.3%DISTS指标改进了最先进的技术。此外，它在新视图合成和单图像3D视图重建方面都优于最先进的性能。源代码可访问：https://amughrabi.github.io/momentsnerf/. et.al.|[2407.02668](http://arxiv.org/abs/2407.02668)|null|
|**2024-07-02**|**AutoSplat: Constrained Gaussian Splatting for Autonomous Driving Scene Reconstruction**|真实场景重建和视图合成对于通过模拟安全关键场景来推进自动驾驶系统至关重要。3D Gaussian Splatting擅长实时渲染和静态场景重建，但由于复杂的背景、动态对象和稀疏的视图，难以对驾驶场景进行建模。我们提出了AutoSplat，这是一个使用高斯飞溅来实现自动驾驶场景的高度逼真重建的框架。通过对表示道路和天空区域的高斯图施加几何约束，我们的方法能够对包括车道变化在内的具有挑战性的场景进行多视图一致模拟。利用3D模板，我们引入了反射高斯一致性约束来监督前景对象的可见和不可见面。此外，为了对前景对象的动态外观进行建模，我们估计了每个前景高斯的残差球面谐波。在Pandaset和KITTI上进行的大量实验表明，AutoSplat在不同驾驶场景下的场景重建和新视图合成方面优于最先进的方法。访问我们的 $\href{https://autosplat.github.io/}｛\text｛项目页面｝｝$ 。 et.al.|[2407.02598](http://arxiv.org/abs/2407.02598)|null|
|**2024-07-01**|**DRAGON: Drone and Ground Gaussian Splatting for 3D Building Reconstruction**|从成像数据重建三维建筑是从城市规划到侦察等许多应用的重要任务。NeRF和Gaussian Splatting等现代新颖视图合成（NVS）方法为以无监督的方式从自然2D图像开发3D模型提供了强大的技术。这些算法通常需要感兴趣场景周围的输入训练视图，而在大型建筑的情况下，这通常不适用于所有的摄像机立面。特别是，在大多数建筑中，最容易获得的相机视角是在近地面（例如，使用手机）和空中（无人机）高度。然而，由于无人机和地面图像集在视点上的显著差异，相机配准——NVS算法的必要步骤——失败了。在这项工作中，我们提出了一种方法，即DRAGON，它可以将无人机和地面建筑图像作为输入，并生成3D NVS模型。DRAGON的关键见解是，中间高程图像可以通过NVS算法本身在具有感知正则化的迭代过程中外推，从而弥合两个高程之间的视觉特征差距并实现配准。我们使用Google Earth Studio汇编了一个包含9个大型建筑场景的半合成数据集，并从数量和质量上证明，与基线策略相比，DRAGON可以在该数据集上生成引人注目的渲染图。 et.al.|[2407.01761](http://arxiv.org/abs/2407.01761)|null|
|**2024-07-01**|**EndoSparse: Real-Time Sparse View Synthesis of Endoscopic Scenes using Gaussian Splatting**|从一组内窥镜图像中对生物组织进行3D重建是解锁具有3D能力的各种重要下游外科应用的关键。现有的方法使用各种先进的神经渲染技术进行真实感视图合成，但当只有稀疏的观测可用时，它们往往难以恢复准确的3D表示，这在现实世界的临床场景中通常是这样。为了应对这一{稀疏性}挑战，我们提出了一个在重建过程中利用多个基础模型的先验知识的框架，称为\textit{EndoSparse}。实验结果表明，在具有挑战性的稀疏视图条件下，包括仅使用三个视图，我们提出的策略显著提高了几何和外观质量。在针对最先进方法的严格基准测试实验中，\textit｛EndoSparse｝在精确的几何形状、逼真的外观和渲染效率方面取得了优异的结果，证实了内窥镜重建中对稀疏视图限制的稳健性。\textit｛EndoSparse｝标志着神经3D重建在现实世界临床场景中的实际部署迈出了稳步的一步。项目页面：https://endo-sparse.github.io/. et.al.|[2407.01029](http://arxiv.org/abs/2407.01029)|null|
|**2024-06-30**|**Ego-to-Exo: Interfacing Third Person Visuals from Egocentric Views in Real-time for Improved ROV Teleoperation**|水下遥控潜水器是一种无人潜水器，设计用于在海洋深处进行探索和操作。尽管使用了高端相机，但基于第一人称（以自我为中心）视角的典型遥操作引擎限制了水面操作员在复杂深水任务中操纵和导航ROV的能力。在本文中，我们提出了一种交互式遥操作界面，该界面（i）从过去的自我中心视图提供按需的“第三人”（外部中心）视觉效果，以及（ii）通过增强的ROV姿势实时增强外围信息。我们通过将基于3D几何的Ego-to-Exo视图合成算法集成到单目SLAM系统中以实现精确的轨迹估计来实现这一点。所提出的闭合形式解决方案仅使用ROV过去的以自我为中心的视图和SLAM主干进行姿态估计，这使其可移植到现有的ROV平台。与数据驱动的解决方案不同，它对应用程序和水体特定场景是不变的。我们通过在具有挑战性的弱光条件下进行2自由度室内导航和6自由度水下洞穴探索的大量实验，验证了所提出框架的几何精度。我们通过遵循水下洞穴内的洞穴线等导航指南，展示了动态Ego-to-Exo视图生成和实时姿态渲染在远程遥控潜水器遥操作中的优势。这种新的交互式遥控潜水器遥控操作方式为未来的水下遥控机器人研究开辟了广阔的前景。 et.al.|[2407.00848](http://arxiv.org/abs/2407.00848)|null|
|**2024-06-29**|**Intrinsic PAPR for Point-level 3D Scene Albedo and Shading Editing**|神经渲染的最新进展在从多视图RGB图像合成新视图方面表现出色。然而，它们通常缺乏在详细的点级别编辑场景的着色或颜色的能力，同时确保不同视点之间的一致性。在这项工作中，我们解决了点级3D场景反照率和多视图RGB图像的着色编辑的挑战，重点是点级而不是局部或全局级的详细编辑。虽然之前基于体积表示的工作（如NeRF）难以在点级别实现3D一致性编辑，但基于点的神经渲染的最新进展显示出克服这一挑战的前景。我们介绍了“内在PAPR”，这是一种基于最近的基于点的神经绘制技术——接近注意力点绘制（PAPR）的新方法。与其他对场景的内在分解建模的基于点的方法不同，我们的方法不依赖于复杂的着色模型或可能不普遍适用的简单先验。相反，我们直接将场景分解建模为反照率和阴影分量，从而获得更好的估计精度。与最新的基于点的反向渲染方法的比较评估表明，Intrinsic PAPR实现了更高质量的新颖视图渲染和卓越的点级反照率和着色编辑。 et.al.|[2407.00500](http://arxiv.org/abs/2407.00500)|null|
|**2024-06-28**|**ASSR-NeRF: Arbitrary-Scale Super-Resolution on Voxel Grid for High-Quality Radiance Fields Reconstruction**|基于NeRF的方法通过构建具有隐式或显式表示的辐射场来重建3D场景。虽然基于NeRF的方法可以在任意尺度上执行新视图合成（NVS），但在具有低分辨率（LR）优化的高分辨率新视图综合（HRNVS）中的性能往往导致过度平滑。另一方面，单图像超分辨率（SR）旨在将LR图像增强到HR图像，但缺乏多视点一致性。为了应对这些挑战，我们提出了任意尺度超分辨率NeRF（ASSR-NeRF），这是一种用于超分辨率新视图合成（SRNVS）的新框架。我们提出了一种基于注意力的VoxelGridSR模型来直接对优化的体积执行3D超分辨率（SR）。我们的模型在不同的场景中进行了训练，以确保可推广性。对于用LR视图训练的看不见的场景，我们可以直接应用我们的VoxelGridSR来进一步细化体积并实现多视图一致SR。我们从数量和质量上证明了所提出的方法在SRNVS中取得了显著的性能。 et.al.|[2406.20066](http://arxiv.org/abs/2406.20066)|null|
|**2024-06-27**|**360 in the Wild: Dataset for Depth Prediction and View Synthesis**|大量的透视相机数据集促进了用于各种任务的新的基于学习的策略的出现，如相机定位、单图像深度估计或视图合成。然而，全景或全向图像数据集，包括姿势和深度等基本信息，大多是用合成场景制作的。在这项工作中，我们介绍了一个大规模的野外360 $^｛\circ｝$ 视频数据集。这个数据集是从互联网上仔细收集的，并从世界各地捕获。因此，该数据集展示了非常多样化的环境（例如，室内和室外）和上下文（例如，有和没有移动物体）。构成我们数据集的25K幅图像中的每一幅都提供了其各自相机的姿势和深度图。我们说明了我们的数据集与两个主要任务的相关性，即单图像深度估计和视图合成。 et.al.|[2406.18898](http://arxiv.org/abs/2406.18898)|null|

<p align=right>(<a href=#updated-on-20240705>back to top</a>)</p>

## 3D Reconstruction

|Publish Date|Title|Abstract|PDF|Code|
|---|---|---|---|---|
|**2024-07-03**|**Free-SurGS: SfM-Free 3D Gaussian Splatting for Surgical Scene Reconstruction**|手术场景的实时3D重建在计算机辅助手术中发挥着至关重要的作用，有望提高外科医生的可视性。3D高斯散射（3DGS）的最新进展显示出在一般场景的实时新颖视图合成方面的巨大潜力，该合成依赖于由运动结构（SfM）生成的精确姿态和点云进行初始化。然而，由于纹理最小和光度不一致的挑战，带有SfM的3DGS无法在手术场景中恢复准确的相机姿势和几何结构。为了解决这个问题，在本文中，我们提出了第一种基于无SfM的3DGS的手术场景重建方法，通过联合优化相机姿态和场景表示。基于视频连续性，我们的方法的关键是利用即时光流先验来引导从3D高斯导出的投影流。与以前大多数只依赖光度损失的方法不同，我们将姿态估计问题公式化为最小化投影流和光流之间的流量损失。进一步引入了一致性检查，通过检测满足核极几何的刚性可靠点来过滤流量异常值。在3D高斯优化过程中，我们随机采样帧以优化场景表示，从而逐步增长3D高斯。在SCARED数据集上的实验表明，与现有方法相比，我们在高效的新视图合成和姿态估计方面具有优越的性能。代码位于https://github.com/wrld/Free-SurGS. et.al.|[2407.02918](http://arxiv.org/abs/2407.02918)|null|
|**2024-07-03**|**A Radiometric Correction based Optical Modeling Approach to Removing Reflection Noise in TLS Point Clouds of Urban Scenes**|点云在三维重建、自动驾驶和机器人等计算机视觉任务中至关重要。然而，TLS获取的点云通常包含来自反射表面的虚拟点，从而导致中断。本文提出了一种TLS点云的反射噪声消除算法。我们创新的反射平面检测算法基于几何光学模型和物理特性，根据光学反射理论识别和分类反射点。我们对LSFH特征描述符进行了调整，以保留反射特征，从而减少对称架构结构的干扰。通过引入Hausdorff特征距离，该算法增强了对重影和变形的恢复能力，提高了虚拟点检测的准确性。在具有虚拟TLS反射噪声的不同城市环境的3DRN基准数据集上进行的大量实验表明，我们的算法将反射区域中3D点的精度和召回率分别提高了57.03\%和31.80\%。我们的方法比领先的方法提高了9.17%的异常值检测率和5.65%的准确率。访问3DRN数据集(https://github.com/Tsuiky/3DRN). et.al.|[2407.02830](http://arxiv.org/abs/2407.02830)|null|
|**2024-07-02**|**The influence of the 3D Galactic gas structure on cosmic-ray transport and gamma-ray emission**|宇宙射线（CR）在星际介质（ISM）的动力学中起着重要作用。它们的相互作用和传输电离、加热并推动ISM，从而耦合ISM的不同区域。CR的空间分布取决于其来源的分布以及它们相互作用的ISM成分，如气体、星光和磁场。特别是，气体与CR密切相互作用，影响CR通量和伽马射线发射。我们说明了三维气体结构对CR传输和伽马射线发射的影响。我们使用PICARD代码和最近HI和H $_2$ 银河系气体成分的多个3D重建样本来研究对CR传输和伽马射线发射的影响。我们找到了必要的输运参数来再现CR通量的局部测量，并发现它们取决于气体密度和结构的局部分布。CR通量的分布表现出与能量相关的结构，由于其相应的损失过程，所有CR物种都会发生变化。增强的次级（初级）物种的区域与气体密度在空间上相关（反相关）。我们观察到伽马射线发射对气体结构对比度的高灵敏度，因为这些结构决定了强子相互作用和韧致辐射的三维空间分布。我们发现在逆康普顿（IC）发射中也可以看到CR电子分布中相应的气体诱导结构。由于上述敏感性，对CR源和输送参数的CR数据的分析需要使用准确的3D气体图。 et.al.|[2407.02410](http://arxiv.org/abs/2407.02410)|null|
|**2024-07-02**|**Indoor 3D Reconstruction with an Unknown Camera-Projector Pair**|基于结构光的摄像机-投影对（CPP）方法在室内三维重建中起着至关重要的作用，尤其是对于纹理较弱的场景。以前的方法通常假设已知的本质，这些本质是从已知物体中预先校准的，或者是从多视图观测中自我校准的。在没有任何已知对象的情况下，仅从两个视图可靠地恢复CPP内部函数仍然具有挑战性。在本文中，我们提供了一个简单而可靠的解决方案。我们首次证明，可以从未知的长方体角（C2），例如房间的角，导出对CPP本质的足够约束，这是室内场景中的常见结构。此外，在只有已知相机主点的情况下，所有CPP本质的复杂多变量估计可以简化为一个简单的单变量优化问题，从而实现可靠的校准，从而在未知CPP的情况下直接进行3D重建。大量结果表明，与传统方法和基于学习的方法相比，所提出的方法具有优越性。此外，所提出的方法还展示了在没有主动照明的情况下解决类似任务的巨大潜力，例如来自运动的稀疏视图结构。 et.al.|[2407.01945](http://arxiv.org/abs/2407.01945)|null|
|**2024-07-02**|**PO-MSCKF: An Efficient Visual-Inertial Odometry by Reconstructing the Multi-State Constrained Kalman Filter with the Pose-only Theory**|有效的视觉惯性里程计（VIO）对于有效载荷受限的机器人至关重要。尽管现代基于优化的算法已经实现了优越的精度，但基于MSCKF的VIO算法仍然因其高效和一致的性能而被广泛要求。由于MSCKF建立在传统的多视图几何结构上，因此测量的残差不仅与状态误差有关，而且与特征位置误差有关。为了应用EKF融合，需要投影过程来消除观测模型中的特征位置误差，这可能导致模型和精度下降。为了获得有效的视觉惯性融合模型，同时保持模型的一致性，我们提出用新的仅姿态（PO）多视图几何描述来重建MSCKF-VIO。在新构建的滤波器中，我们对PO重投影残差进行了建模，这些残差仅与运动状态相关，从而克服了空间投影的要求。此外，新滤波器不需要任何特征位置信息，这消除了由3D重建过程带来的计算成本和线性化误差。我们在多个数据集上进行了全面的实验，其中所提出的方法在具有挑战性的序列中显示出准确性的提高和一致的性能。 et.al.|[2407.01888](http://arxiv.org/abs/2407.01888)|null|
|**2024-07-02**|**Multi-level Reliable Guidance for Unpaired Multi-view Clustering**|在本文中，我们解决了不成对多视图聚类（UMC）的挑战性问题，旨在使用多个视图中的不成对观测样本进行有效的联合聚类。通常，传统的不完全多视图聚类（IMC）方法通常依赖于成对的样本来捕获视图之间的互补信息。然而，由于缺乏配对样本，该策略在UMC中变得不切实际。尽管一些研究人员试图通过在视图之间保持一致的聚类结构来解决这个问题，但他们经常忽视这些聚类结构的可信度，尤其是对于初始训练期间的边界样本和不确定的聚类结构。因此，我们提出了一种称为UMC多级可靠指导（MRG-UMC）的方法，该方法利用多级聚类来帮助分别跨内部视图、跨视图和公共视图学习可信的聚类结构。具体来说，在每个视图中，多级集群在不同级别上培育了一个值得信赖的集群结构，并减少了集群错误。在跨视图学习中，可靠的视图引导增强了集群结构对其他视图的信心。同样，在多层次框架内，合并一个共同的视图有助于对齐不同的视图，从而减少聚类误差和聚类结构的不确定性。最后，正如大量实验所证明的那样，与20种最先进的方法相比，我们的UMC方法显示出显著的效率提高。 et.al.|[2407.01247](http://arxiv.org/abs/2407.01247)|null|
|**2024-07-01**|**EndoSparse: Real-Time Sparse View Synthesis of Endoscopic Scenes using Gaussian Splatting**|从一组内窥镜图像中对生物组织进行3D重建是解锁具有3D能力的各种重要下游外科应用的关键。现有的方法使用各种先进的神经渲染技术进行真实感视图合成，但当只有稀疏的观测可用时，它们往往难以恢复准确的3D表示，这在现实世界的临床场景中通常是这样。为了应对这一{稀疏性}挑战，我们提出了一个在重建过程中利用多个基础模型的先验知识的框架，称为\textit{EndoSparse}。实验结果表明，在具有挑战性的稀疏视图条件下，包括仅使用三个视图，我们提出的策略显著提高了几何和外观质量。在针对最先进方法的严格基准测试实验中，\textit｛EndoSparse｝在精确的几何形状、逼真的外观和渲染效率方面取得了优异的结果，证实了内窥镜重建中对稀疏视图限制的稳健性。\textit｛EndoSparse｝标志着神经3D重建在现实世界临床场景中的实际部署迈出了稳步的一步。项目页面：https://endo-sparse.github.io/. et.al.|[2407.01029](http://arxiv.org/abs/2407.01029)|null|
|**2024-06-28**|**Odd-One-Out: Anomaly Detection by Comparing with Neighbors**|本文介绍了一种新的异常检测（AD）问题，该问题的重点是识别相对于场景中其他实例的“奇怪的”对象。与传统的AD基准不同，在我们的设置中，这种情况下的异常是特定于场景的，由占大多数的常规实例定义。由于对象实例通常从单个视点部分可见，因此我们的设置提供每个场景的多个视图作为输入。为了为未来的研究提供一个试验台，我们介绍了两个基准，ToysAD-8K和PartsAD-15K。我们提出了一种新的方法，该方法为每个实例生成以对象为中心的3D表示，并通过实例之间的交叉检查来检测异常表示。我们在给出的基准中对我们的方法进行了严格的定量和定性分析。 et.al.|[2406.20099](http://arxiv.org/abs/2406.20099)|**[link](https://github.com/VICO-UoE/OddOneOutAD)**|
|**2024-06-28**|**SpotlessSplats: Ignoring Distractors in 3D Gaussian Splatting**|三维高斯散射（3DGS）是一种很有前途的三维重建技术，它提供了高效的训练和渲染速度，适用于实时应用。然而，当前的方法需要高度受控的环境（没有移动的人或风吹的元素，以及一致的照明）来满足3DGS的视图间一致性假设。这使得真实世界捕捉的重建成为问题。我们提出了SpotlessSplats，这是一种利用预先训练的通用功能与稳健优化相结合的方法，可以有效地忽略瞬态干扰因素。我们的方法在随意捕捉的情况下，在视觉和数量上都达到了最先进的重建质量。 et.al.|[2406.20055](http://arxiv.org/abs/2406.20055)|null|
|**2024-06-28**|**Deep Learning-based Depth Estimation Methods from Monocular Image and Videos: A Comprehensive Survey**|由于其在自动驾驶、3D重建、数字娱乐和机器人等许多领域的应用，从单个RGB图像和视频中估计深度引起了广泛的兴趣。在过去的10年里，已经发表了500多篇基于深度学习的论文，这表明人们对这项任务的兴趣越来越大。本文对现有的基于深度学习的方法、它们所面临的挑战以及它们在架构和监督方法方面的发展进行了全面的调查。它提供了一种分类法，用于根据输入和输出模式、网络架构和学习方法对当前工作进行分类。它还讨论了单目深度估计历史上的主要里程碑，以及现有方法中使用的不同管道、数据集和评估指标。 et.al.|[2406.19675](http://arxiv.org/abs/2406.19675)|null|

<p align=right>(<a href=#updated-on-20240705>back to top</a>)</p>

## Diffusion

|Publish Date|Title|Abstract|PDF|Code|
|---|---|---|---|---|
|**2024-07-03**|**DisCo-Diff: Enhancing Continuous Diffusion Models with Discrete Latents**|扩散模型已经彻底改变了生成性学习。它们利用扩散过程将数据编码为简单的高斯分布。然而，将复杂的、潜在的多模式数据分布编码为单个连续高斯分布可以说是一个不必要的具有挑战性的学习问题。我们提出了离散连续潜在变量扩散模型（DisCo-Diff），通过引入互补的离散潜在变量来简化这一任务。我们用编码器推断的可学习离散延迟来增强DM，并端到端地训练DM和编码器。DisCo-Diff不依赖于预先训练的网络，因此该框架具有普遍适用性。离散潜伏时间通过减少DM的生成ODE的曲率，显著简化了DM的复杂噪声到数据映射的学习。一个额外的自回归变换器对离散延迟的分布进行建模，这是一个简单的步骤，因为DisCo-Diff只需要几个具有小码本的离散变量。我们在玩具数据、几个图像合成任务以及分子对接上验证了DisCo-Diff，并发现引入离散潜伏期可以持续提高模型性能。例如，DisCo-Diff使用ODE采样器在类条件ImageNet-64/128数据集上实现了最先进的FID分数。 et.al.|[2407.03300](http://arxiv.org/abs/2407.03300)|null|
|**2024-07-03**|**Improved Noise Schedule for Diffusion Training**|扩散模型已经成为产生视觉信号的事实选择。然而，训练单个模型来预测不同级别的噪声带来了巨大的挑战，需要多次迭代，并产生巨大的计算成本。已经引入了各种方法，如损失加权策略设计和架构优化，以加快收敛。在这项研究中，我们提出了一种新的方法来设计噪声调度，以增强扩散模型的训练。我们的关键见解是，当将采样频率增加到 $\log\text｛SNR｝＝0$ 左右时，信噪比对数（logSNR）的重要性采样在理论上等效于修改的噪声调度，对训练效率特别有益。我们从经验上证明了我们的噪声调度优于标准余弦调度。此外，我们在ImageNet基准上强调了我们的噪声调度设计的优势，表明所设计的调度始终有利于不同的预测目标。 et.al.|[2407.03297](http://arxiv.org/abs/2407.03297)|null|
|**2024-07-03**|**LivePortrait: Efficient Portrait Animation with Stitching and Retargeting Control**|肖像动画旨在从单一来源的图像中合成逼真的视频，将其作为外观参考，并从驾驶视频、音频、文本或生成中提取运动（即面部表情和头部姿势）。我们没有遵循主流的基于扩散的方法，而是探索和扩展了基于隐式关键点的框架的潜力，它有效地平衡了计算效率和可控性。在此基础上，我们开发了一个名为LivePortrait的视频驱动人像动画框架，重点是更好的通用性、可控性和实用效率。为了增强生成质量和泛化能力，我们将训练数据扩展到约6900万个高质量帧，采用混合图像视频训练策略，升级网络架构，并设计更好的运动变换和优化目标。此外，我们发现紧凑的隐式关键点可以有效地表示一种混合形状，并精心提出了一个缝合和两个重定目标模块，该模块利用了一个计算开销可忽略不计的小MLP来增强可控性。实验结果表明，即使与基于扩散的方法相比，我们的框架也是有效的。在带有PyTorch的RTX 4090 GPU上，生成速度显著达到12.8ms。推理代码和模型可在https://github.com/KwaiVGI/LivePortrait et.al.|[2407.03168](http://arxiv.org/abs/2407.03168)|**[link](https://github.com/KwaiVGI/LivePortrait)**|
|**2024-07-03**|**Closing Pandora's Box -- The deepest X-ray observations of Abell 2744 and a multi-wavelength merger picture**|阿贝尔2744，也被称为潘多拉星团，是一个复杂的合并星系团。虽然沿南北轴线明显存在重大合并，但西北亚星团的动力学状态一直高度不确定。我们介绍了用钱德拉X射线天文台获得的Abell 2744的超深（约2.1 Ms美元）X射线观测结果，并用一系列星系团合并的理想化模拟重新解释了多波长图像。新数据以前所未有的细节揭示了三个X射线发光亚簇中冷核的破坏，并证实了西北部存在冲击。星团成员星系的位置-速度集群显示出明显分离的S2分量， $\Delta z$意味着53 Mpc的分离或4500 rm{km\s^{-1}}$ 的视线速度，或者可能是两者的某种组合。虽然二元模拟允许NW在第一次周心通道后经历引力弹弓射击，但三重合并模拟排除了这种情况，因为两次合并必须相隔0.5 Gyr，并且两次合并的冲击的联合影响将完全破坏SE和NW冷芯；它们只在1-2Gyr后才重新形成，此时核心分离大大超过观测值。最能描述Abell 2744的场景是一次0.5-0.6美元Gyrs前的南北向正面合并，然后是NW子集群的第一次合并。此外，我们注意到，具有三个星团大小晕的模型，其质量与引力透镜约束一致，但产生的透镜会聚和表面亮度低于在大多数视场中观察到的，而温度与观察到的一致。这表明存在大规模的超密度，这有助于在不加热最稠密气体的情况下产生扩散发射和总表面密度。 et.al.|[2407.03142](http://arxiv.org/abs/2407.03142)|null|
|**2024-07-03**|**$L_p$-norm Distortion-Efficient Adversarial Attack**|对抗性的例子显示了一种强大的能力，可以使训练有素的模型被错误分类。当前主流的对抗性攻击方法只考虑$L_0$-范数、$L_2$-范数和$L_\infty$-范数中的一种失真$基于L_0$-normam的方法对单个像素造成较大的修改，导致肉眼可见的检测，而基于$L_2$-normal和$L_\infty$-norma的方法对对抗性防御的鲁棒性较弱，因为它们总是将微小的扰动扩散到所有像素。更现实的对抗性扰动应该是稀疏的和不可察觉的。在本文中，我们提出了一种新的$L_p$-范数失真高效对抗性攻击，它不仅拥有最小的$L_2$-范数损失，而且显著减少了$L_0$-范数畸变。为此，我们设计了一种新的优化方案，该方案首先在$L_2$范数约束下优化初始对抗性扰动，然后构造初始扰动的维数不重要矩阵。这样的维度不重要度矩阵可以指示初始扰动的每个维度的对抗性不重要度。此外，我们为维数不重要矩阵引入了一个新的对抗性阈值概念。不重要度高于阈值的初始扰动的维数将全部设置为零，大大降低了$L_0$-范数失真。在三个基准数据集上的实验结果表明，在相同的查询预算下，我们的方法生成的对抗性示例具有比现有技术更低的$L_0$-范数和$L_2$ -范数失真。这证明了所提出的方法在对抗性鲁棒性和视觉不可见性方面优于竞争对手。 et.al.|[2407.03115](http://arxiv.org/abs/2407.03115)|null|
|**2024-07-03**|**Spatio-Temporal Adaptive Diffusion Models for EEG Super-Resolution in Epilepsy Diagnosis**|脑电图（EEG）技术，特别是高密度脑电图（HD EEG）设备，在神经科学等领域得到了广泛应用。HD脑电图设备通过在头皮上放置更多电极来提高脑电图的空间分辨率，满足癫痫病灶定位等临床诊断应用的要求。然而，这项技术面临着诸如高昂的获取成本和有限的使用场景等挑战。本文提出了时空自适应扩散模型（STADM），以率先使用扩散模型实现从低分辨率（LR，64通道或更少）脑电图到高分辨率（HR，256通道）脑电图的空间SR重建。具体来说，设计了一个时空条件模块来提取LR EEG的时空特征，然后将其作为条件输入来指导扩散模型的反向去噪过程。此外，构建了多尺度Transformer去噪模块，利用多尺度卷积块和基于交叉注意力的扩散Transformer块进行条件引导，生成受试者自适应SR EEG。实验结果表明，该方法有效地提高了LR脑电的空间分辨率，在数量上优于现有方法。此外，STADM通过将合成SR EEG应用于癫痫患者的分类和源定位任务来证明其价值，表明其有可能显著提高LR EEG的空间分辨率。 et.al.|[2407.03089](http://arxiv.org/abs/2407.03089)|null|
|**2024-07-03**|**Electromagnetic Property Sensing Based on Diffusion Model in ISAC System**|集成传感与通信（ISAC）为未来的无线系统开辟了许多改变游戏规则的机会。在本文中，我们开发了一种新的ISAC方案，该方案利用扩散模型来感测目标在预定感测区域中的电磁（EM）特性。具体而言，我们首先通过使用通信和从目标回波的感测信号来估计感测信道。然后，我们使用扩散模型来生成表示目标的点云，从而实现目标EM特性分布的3D可视化。为了最小化地面实况和估计的点云之间的平均切角距离（MCD），我们在每个用户设备（UE）的最大发射功率和最小通信可实现速率的约束下，进一步设计了通信和感测波束成形矩阵。仿真结果证明了所提出的方法在实现目标形状、相对介电常数和电导率的高质量重建方面的有效性。此外，该方法可以在感测区域的任何位置有效地感测目标的电磁特性。 et.al.|[2407.03075](http://arxiv.org/abs/2407.03075)|null|
|**2024-07-03**|**Semantic-Aware Power Allocation for Generative Semantic Communications with Foundation Models**|扩散模型的最新进展在生成建模方面取得了重大突破。生成模型和语义通信（SemCom）的结合实现了超低速率的高保真语义信息交换。提出了一种新的图像任务生成SemCom框架，其中预训练的基础模型分别用作语义特征提取和图像再生的语义编码器和解码器。通过对Kodak数据集进行数值模拟，对再生图像的传输可靠性和感知质量之间的数学关系以及语义特征的语义值进行了建模。我们还研究了语义感知的功率分配问题，目的是在保证语义性能的同时最小化总功耗。为了解决这一问题，分别通过约束解耦和二等分搜索提出了两种语义软件功率分配方法。数值结果表明，与传统方法相比，所提出的语义感知方法在总功耗方面表现出优越的性能。 et.al.|[2407.03050](http://arxiv.org/abs/2407.03050)|null|
|**2024-07-03**|**SlerpFace: Face Template Protection via Spherical Linear Interpolation**|现代人脸识别系统使用从人脸图像中提取的特征模板来识别人。为了增强隐私，人脸模板保护技术被广泛用于隐藏存储在模板中的敏感身份和外观信息。本文确定了一种新出现的利用扩散模型的隐私攻击形式，该形式可能会使先前的保护无效，称为反向攻击。该攻击可以从模板中合成高质量的、保留身份的人脸图像，揭示人物的外貌。在研究扩散模型生成能力的基础上，本文提出了一种通过将模板旋转到类噪声分布来恶化攻击的防御方法。这可以通过在其定位的超球面上进行球面和线性插值模板（slerp）来有效地实现。本文进一步提出了分组明智地划分和剔除模板的特征维度，以增强旋转模板的不可逆性。小组的划分和每个小组中的辍学者都是以一种有利于识别的方式学习的。将所提出的技术具体化为一种新的人脸模板保护技术SlerpFace。大量实验表明，SlerpFace提供了令人满意的识别精度和全面的隐私保护，以抵御反转和其他攻击形式，优于现有技术。 et.al.|[2407.03043](http://arxiv.org/abs/2407.03043)|null|
|**2024-07-03**|**NLP Sampling: Combining MCMC and NLP Methods for Diverse Constrained Sampling**|在硬约束下生成不同的样本是许多领域的核心挑战。通过这项工作，我们旨在提供一个综合的观点和框架，将MCMC、约束优化和机器人领域的方法相结合，并从经验评估中深入了解其优势。我们提出了NLP采样作为一种通用问题公式，提出了一系列重启两阶段方法作为跨领域集成方法的框架，并在分析和机器人操作规划问题上对其进行了评估。作为补充，我们提供了几个概念讨论，例如拉格朗日参数的作用、全局采样以及扩散NLP和相应的基于模型的去噪采样器的想法。 et.al.|[2407.03035](http://arxiv.org/abs/2407.03035)|null|

<p align=right>(<a href=#updated-on-20240705>back to top</a>)</p>

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

<p align=right>(<a href=#updated-on-20240705>back to top</a>)</p>

[contributors-shield]: https://img.shields.io/github/contributors/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[contributors-url]: https://github.com/Vincentqyw/cv-arxiv-daily/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[forks-url]: https://github.com/Vincentqyw/cv-arxiv-daily/network/members
[stars-shield]: https://img.shields.io/github/stars/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[stars-url]: https://github.com/Vincentqyw/cv-arxiv-daily/stargazers
[issues-shield]: https://img.shields.io/github/issues/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[issues-url]: https://github.com/Vincentqyw/cv-arxiv-daily/issues

