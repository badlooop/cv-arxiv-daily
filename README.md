[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]

## Updated on 2024.04.02
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
|**2024-03-29**|**InstantSplat: Unbounded Sparse-view Pose-free Gaussian Splatting in 40 Seconds**|虽然新型视图合成（NVS）在3D计算机视觉中取得了实质性进展，但它通常需要从密集的视点对相机的内在和外在进行初步估计。这种预处理通常通过运动结构（SfM）管道进行，这一过程可能缓慢且不可靠，尤其是在稀疏视图场景中，匹配特征不足以进行准确重建。在这项工作中，我们将基于点的表示（例如，3D高斯飞溅，3D-GS）的优势与端到端密集立体模型（DUSt3R）相结合，以解决无约束设置下NVS中复杂但尚未解决的问题，包括无姿态和稀疏视图挑战。我们的框架InstantSplat将密集的立体先验与3D-GS相结合，在不到1分钟的时间内从稀疏和无姿势的图像中构建大规模场景的3D高斯。具体而言，InstantSplat包括一个粗略几何初始化（CGI）模块，该模块利用从预先训练的密集立体管道中导出的全局对齐3D点图，在所有训练视图中快速建立初步场景结构和相机参数。随后是快速三维高斯优化（F-3DGO）模块，该模块通过姿态正则化联合优化三维高斯属性和初始化姿态。在大型户外坦克和寺庙数据集上进行的实验表明，InstantSplat显著提高了SSIM（32%），同时将绝对轨迹误差（ATE）降低了80%。这些使InstantSplat成为涉及无偏序和稀疏视图条件的场景的可行解决方案。项目页面：instansplat.github.io。 et.al.|[2403.20309](http://arxiv.org/abs/2403.20309)|null|
|**2024-03-29**|**Snap-it, Tap-it, Splat-it: Tactile-Informed 3D Gaussian Splatting for Reconstructing Challenging Surfaces**|触觉和视觉齐头并进，相互增强我们理解世界的能力。从研究的角度来看，触摸和视觉的混合问题还没有得到充分的探索，并提出了有趣的挑战。为此，我们提出了触觉知情3DGS，这是一种将触摸数据（局部深度图）与多视图视觉数据相结合的新方法，以实现表面重建和新的视图合成。我们的方法优化了3D高斯基元，以准确地对物体在接触点的几何结构进行建模。通过创建一个降低触摸位置透射率的框架，我们实现了精细的表面重建，确保了均匀平滑的深度图。当考虑非朗伯物体（例如有光泽或反射的表面）时，触摸尤其有用，因为现代方法往往无法用逼真的镜面高光进行重建。通过将视觉和触觉相结合，我们可以用比现有方法更少的图像实现更准确的几何重建。我们对具有光泽和反射表面的物体进行评估，并证明了我们的方法的有效性，显著提高了重建质量。 et.al.|[2403.20275](http://arxiv.org/abs/2403.20275)|null|
|**2024-03-29**|**SGD: Street View Synthesis with Gaussian Splatting and Diffusion Prior**|街道场景的新颖视图合成（NVS）在自动驾驶仿真中起着至关重要的作用。目前实现它的主流技术是神经渲染，如神经辐射场（NeRF）和三维高斯散射（3DGS）。尽管已经取得了令人兴奋的进展，但在处理街景时，当前的方法很难在与训练视点显著偏离的视点处保持渲染质量。这个问题源于移动车辆上固定摄像头拍摄的稀疏训练视图。为了解决这个问题，我们提出了一种新的方法，通过利用扩散模型的先验知识和互补的多模态数据来增强3DGS的能力。具体来说，我们首先通过添加相邻帧的图像作为条件来微调扩散模型，同时利用激光雷达点云的深度数据来提供额外的空间信息。然后，我们应用扩散模型对训练过程中看不见的视图处的3DGS进行正则化。实验结果验证了我们的方法与当前最先进的模型相比的有效性，并证明了它在从更广阔的视角渲染图像方面的进步。 et.al.|[2403.20079](http://arxiv.org/abs/2403.20079)|null|
|**2024-03-29**|**NeSLAM: Neural Implicit Mapping and Self-Supervised Feature Tracking With Depth Completion and Denoising**|近年来，在3D重建和密集RGB-D SLAM系统方面取得了重大进展。一个值得注意的发展是神经辐射场（NeRF）在这些系统中的应用，它利用隐式神经表示对3D场景进行编码。将NeRF扩展到SLAM已经显示出有希望的结果。然而，从消费级RGB-D传感器获得的深度图像往往是稀疏和有噪声的，这对3D重建提出了重大挑战，并影响了场景几何结构的表示精度。此外，具有占用值的原始层次特征网格对于场景几何表示是不准确的。此外，现有的方法选择随机像素进行相机跟踪，这导致定位不准确，并且在真实的室内环境中不鲁棒。为此，我们提出了NeSLAM，这是一种先进的框架，可以实现精确而密集的深度估计、稳健的相机跟踪和新颖视图的逼真合成。首先，设计了一个深度完成和去噪网络，以提供密集的几何先验，并指导神经隐式表示优化。其次，用符号距离场（SDF）分层场景表示代替占用场景表示，以实现高质量的重建和视图合成。此外，我们还提出了一种基于NeRF的自监督特征跟踪算法，用于鲁棒实时跟踪。在各种室内数据集上的实验证明了该系统在重建、跟踪质量和新视图合成方面的有效性和准确性。 et.al.|[2403.20034](http://arxiv.org/abs/2403.20034)|**[link](https://github.com/dtc111111/neslam)**|
|**2024-03-29**|**Grounding and Enhancing Grid-based Models for Neural Fields**|当代许多研究利用基于网格的模型来表示神经场，但仍然缺乏对基于网格模型的系统分析，阻碍了这些模型的改进。因此，本文介绍了一个基于网格的模型的理论框架。该框架指出，这些模型的逼近和泛化行为是由网格切线核（GTK）决定的，GTK是基于网格的模型的固有性质。所提出的框架有助于对各种基于网格的模型进行一致和系统的分析。此外，引入的框架推动了一种新的基于网格的模型的开发，该模型名为乘法傅立叶自适应网格（MulFAGrid）。数值分析表明，MulFAGrid表现出比其前身更低的泛化界，表明其具有鲁棒的泛化性能。实证研究表明，MulFAGrid在各种任务中都取得了最先进的性能，包括2D图像拟合、3D符号距离场（SDF）重建和新颖的视图合成，表现出了卓越的表示能力。项目网站位于https://sites.google.com/view/cvpr24-2034-submission/home. et.al.|[2403.20002](http://arxiv.org/abs/2403.20002)|null|
|**2024-03-29**|**Stable Surface Regularization for Fast Few-Shot NeRF**|本文提出了一种在少镜头设置下合成新视图的算法。主要概念是开发一种称为退火符号距离函数（ASDF）的稳定曲面正则化技术，该技术以从粗到细的方式对曲面进行退火，以加快收敛速度。我们观察到，Eikonal损失是一种广为人知的几何正则化，它需要密集的训练信号来塑造SDF的不同级别集，导致在很少的射击训练下产生低保真度结果。相比之下，所提出的表面正则化成功地重建了场景，并通过稳定的训练生成了高保真度的几何体。利用网格表示和单目几何先验进一步加速了我们的方法。最后，所提出的方法比现有的少镜头新视图合成方法快45倍，并且在ScanNet数据集和NeRF Real数据集中产生了可比较的结果。 et.al.|[2403.19985](http://arxiv.org/abs/2403.19985)|null|
|**2024-03-28**|**Mitigating Motion Blur in Neural Radiance Fields with Events and Frames**|神经辐射场在新视图合成中显示出巨大的潜力。然而，当用于训练的数据受到运动模糊的影响时，它们很难渲染清晰的图像。另一方面，事件相机在动态场景中表现出色，因为它们以微秒的分辨率测量亮度变化，因此只受模糊的轻微影响。最近的方法试图通过融合帧和事件来增强相机运动下的NeRF重建。然而，它们在恢复准确的颜色内容或将NeRF限制在一组预定义的相机姿势方面面临挑战，从而在具有挑战性的条件下损害重建质量。本文提出了一种新的公式，通过利用基于模型和学习的模块来解决这些问题。我们明确地对模糊形成过程进行建模，利用事件二重积分作为额外的基于模型的先验。此外，我们使用端到端可学习的响应函数对事件像素响应进行建模，使我们的方法能够适应真实事件摄像机传感器中的非理想情况。我们在合成数据和真实数据上表明，所提出的方法比仅使用帧的现有去模糊NeRF以及将帧和事件组合的去模糊NeRFs分别高出+6.13dB和+2.48dB。 et.al.|[2403.19780](http://arxiv.org/abs/2403.19780)|**[link](https://github.com/uzh-rpg/evdeblurnerf)**|
|**2024-03-28**|**GauStudio: A Modular Framework for 3D Gaussian Splatting and Beyond**|我们介绍了GauStudio，这是一种用于建模3D高斯飞溅（3DGS）的新型模块化框架，为用户提供标准化的即插即用组件，以便轻松定制和实现3DGS管道。在我们的框架的支持下，我们提出了一种具有前景和天球背景模型的混合高斯表示。实验证明，这种表示减少了无边界户外场景中的伪影，并改进了新颖的视图合成。最后，我们提出了高斯飞溅表面重建（GauS），这是一种新的先渲染后融合的方法，用于在没有微调的情况下从3DGS输入进行高保真度网格重建。总体而言，我们的GauStudio框架、混合表示和GauS方法增强了3DGS建模和渲染能力，实现了更高质量的新视图合成和曲面重建。 et.al.|[2403.19632](http://arxiv.org/abs/2403.19632)|**[link](https://github.com/gap-lab-cuhk-sz/gaustudio)**|
|**2024-03-28**|**SAID-NeRF: Segmentation-AIDed NeRF for Depth Completion of Transparent Objects**|使用现成的RGB-D相机获取透明物体的准确深度信息是计算机视觉和机器人学中的一个众所周知的挑战。深度估计/完成方法通常在具有质量深度标签的数据集上使用和训练，该质量深度标签是从模拟、附加传感器或专门的数据收集设置和已知的三维模型中获取的。然而，大规模获取数据集的可靠深度信息并不简单，这限制了训练的可扩展性和泛化能力。神经辐射场（NeRF）是一种无需学习的方法，在新的视图合成和形状恢复方面取得了广泛的成功。然而，通常需要启发式和受控环境（灯光、背景等）来准确捕捉镜面反射表面。在本文中，我们建议使用视觉基础模型（VFM）以零样本、无标签的方式进行分割，通过同时重建语义字段和扩展来指导这些对象的NeRF重建过程，以提高鲁棒性。我们提出的方法Segmentation AIDed NeRF（SAID NeRF）在透明物体和机器人抓取的深度完成数据集上表现出显著的性能。 et.al.|[2403.19607](http://arxiv.org/abs/2403.19607)|null|
|**2024-03-28**|**XScale-NVS: Cross-Scale Novel View Synthesis with Hash Featurized Manifold**|我们提出了用于真实世界大规模场景的高保真度跨尺度新颖视图合成的XScale NVS。基于显式曲面的现有表示存在离散化分辨率或UV失真问题，而隐式体积表示由于分散的权重分布和曲面模糊性而缺乏大型场景的可扩展性。鉴于上述挑战，我们引入了哈希特征化流形，这是一种新的基于哈希的特征化与延迟神经渲染框架相结合。这种方法通过将哈希条目显式集中在2D流形上，充分释放了表示的表现力，从而有效地表示了独立于离散化分辨率的高度详细的内容。我们还引入了一个新的数据集，即GigaNVS，用于对现实世界大规模场景的跨尺度、高分辨率新视图合成进行基准测试。我们的方法在各种真实世界场景中显著优于竞争基线，在具有挑战性的GigaNVS基准上产生的平均LPIPS比之前的最先进水平低40%。请参阅我们的项目页面：xscalenvs.github.io。 et.al.|[2403.19517](http://arxiv.org/abs/2403.19517)|null|

<p align=right>(<a href=#updated-on-20240402>back to top</a>)</p>

## 3D Reconstruction

|Publish Date|Title|Abstract|PDF|Code|
|---|---|---|---|---|
|**2024-03-29**|**NeSLAM: Neural Implicit Mapping and Self-Supervised Feature Tracking With Depth Completion and Denoising**|近年来，在3D重建和密集RGB-D SLAM系统方面取得了重大进展。一个值得注意的发展是神经辐射场（NeRF）在这些系统中的应用，它利用隐式神经表示对3D场景进行编码。将NeRF扩展到SLAM已经显示出有希望的结果。然而，从消费级RGB-D传感器获得的深度图像往往是稀疏和有噪声的，这对3D重建提出了重大挑战，并影响了场景几何结构的表示精度。此外，具有占用值的原始层次特征网格对于场景几何表示是不准确的。此外，现有的方法选择随机像素进行相机跟踪，这导致定位不准确，并且在真实的室内环境中不鲁棒。为此，我们提出了NeSLAM，这是一种先进的框架，可以实现精确而密集的深度估计、稳健的相机跟踪和新颖视图的逼真合成。首先，设计了一个深度完成和去噪网络，以提供密集的几何先验，并指导神经隐式表示优化。其次，用符号距离场（SDF）分层场景表示代替占用场景表示，以实现高质量的重建和视图合成。此外，我们还提出了一种基于NeRF的自监督特征跟踪算法，用于鲁棒实时跟踪。在各种室内数据集上的实验证明了该系统在重建、跟踪质量和新视图合成方面的有效性和准确性。 et.al.|[2403.20034](http://arxiv.org/abs/2403.20034)|**[link](https://github.com/dtc111111/neslam)**|
|**2024-03-29**|**A Semiparametric Gaussian Mixture Model for Chest CT-based 3D Blood Vessel Reconstruction**|自20世纪70年代出现以来，计算机断层扫描（CT）一直是一种强大的诊断工具。使用CT数据，可以使用专业软件重建人体内部器官和组织（如血管）的三维（3D）结构。这种三维重建对外科手术至关重要，可以作为生动的医学教学实例。然而，传统的3D重建在很大程度上依赖于手动操作，这是耗时的、主观的，并且需要大量的经验。为了解决这个问题，我们开发了一种新的半参数高斯混合模型，用于血管的三维重建。该模型通过根据体素位置实现感兴趣的分量参数的非参数变化来扩展经典高斯混合模型。我们开发了一种基于核的期望最大化算法来估计模型参数，并辅以一个支持的渐近理论。此外，我们还提出了一种新的优化带宽选择的回归方法。与传统的基于交叉验证的（CV）方法相比，回归方法在计算和统计效率方面优于CV方法。在应用中，这种方法有助于以显著的精度实现3D血管结构的全自动重建。 et.al.|[2403.19929](http://arxiv.org/abs/2403.19929)|null|
|**2024-03-28**|**CoherentGS: Sparse Novel View Synthesis with Coherent 3D Gaussians**|在过去的几年里，从图像进行3D重建的领域迅速发展，首先是引入了神经辐射场（NeRF），最近又引入了3D高斯散射（3DGS）。后者在训练和推理速度以及重建质量方面提供了优于NeRF的显著优势。尽管3DGS适用于密集的输入图像，但非结构化的点云状表示很快过度适应极稀疏的输入图像（例如，3个图像）的更具挑战性的设置，从而从新颖的视图中创建出看起来像一堆针的表示。为了解决这个问题，我们提出了正则化优化和基于深度的初始化。我们的关键思想是引入一种可以在2D图像空间中控制的结构化高斯表示。然后，我们约束高斯，特别是它们的位置，并防止它们在优化过程中独立移动。具体来说，我们分别通过隐式卷积解码器和总变化损失引入单视角和多视角约束。通过向高斯引入相干性，我们通过基于流量的损失函数进一步约束优化。为了支持我们的正则化优化，我们提出了一种在每个输入视图使用单目深度估计来初始化高斯的方法。我们在各种场景中展示了与最先进的基于稀疏视图NeRF的方法相比的显著改进。 et.al.|[2403.19495](http://arxiv.org/abs/2403.19495)|null|
|**2024-03-30**|**Total-Decom: Decomposed 3D Scene Reconstruction with Minimal Interaction**|从多视点图像重建场景是计算机视觉和图形学中的一个基本问题。最近的神经隐式表面重建方法已经获得了高质量的结果；然而，由于缺乏自然分解的对象实体和复杂的对象/背景组成，编辑和操纵重建场景的3D几何结构仍然具有挑战性。在本文中，我们提出了Total Decom，这是一种在最小化人类交互的情况下进行分解三维重建的新方法。我们的方法将Segment Anything Model（SAM）与混合隐式-显式神经表面表示和基于网格的区域生长技术无缝集成，用于精确的3D对象分解。Total Decom需要最少的人工注释，同时为用户提供对分解粒度和质量的实时控制。我们在基准数据集上广泛评估了我们的方法，并展示了其在动画和场景编辑等下游应用中的潜力。代码位于https://github.com/CVMI-Lab/Total-Decom.git. et.al.|[2403.19314](http://arxiv.org/abs/2403.19314)|**[link](https://github.com/cvmi-lab/total-decom)**|
|**2024-03-28**|**Neural Fields for 3D Tracking of Anatomy and Surgical Instruments in Monocular Laparoscopic Video Clips**|腹腔镜视频跟踪主要关注两种目标类型：手术器械和解剖结构。前者可用于技能评估，而后者对于虚拟覆盖的投影是必要的。在仪器和解剖跟踪通常被视为两个独立的问题的情况下，在本文中，我们提出了一种同时对所有结构进行联合跟踪的方法。基于单个2D单眼视频剪辑，我们训练神经场来表示连续的时空场景，用于创建至少一帧中可见的所有表面的3D轨迹。由于仪器尺寸较小，它们通常只覆盖图像的一小部分，导致跟踪精度下降。因此，我们建议增强类权重以改善仪器轨迹。我们评估了对腹腔镜胆囊切除术视频片段的跟踪，发现解剖结构和器械的平均跟踪准确率分别为92.4%和87.4%。此外，我们还评估了从该方法的场景重建中获得的深度图的质量。我们表明，这些伪深度具有与最先进的预训练深度估计器相当的质量。在SCARED数据集中的腹腔镜视频上，该方法预测深度的MAE为2.9 mm，相对误差为9.2%。这些结果表明了使用神经场进行腹腔镜场景的单目3D重建的可行性。 et.al.|[2403.19265](http://arxiv.org/abs/2403.19265)|null|
|**2024-03-27**|**WALT3D: Generating Realistic Training Data from Time-Lapse Imagery for Reconstructing Dynamic Objects under Occlusion**|当前的2D和3D对象理解方法在繁忙的城市环境中难以解决严重的遮挡问题，部分原因是缺乏用于学习遮挡的大规模标记地面实况注释。在这项工作中，我们介绍了一种新的框架，用于使用免费可用的延时图像自动生成遮挡下动态对象的大型逼真数据集。通过利用现成的2D（边界框、分割、关键点）和3D（姿势、形状）预测作为伪背景，可以自动识别未遮挡的3D对象，并以剪贴画风格将其合成到背景中，确保逼真的外观和物理上准确的遮挡配置。所得到的具有伪背景真相的剪贴画图像能够有效地训练对遮挡鲁棒的对象重建方法。我们的方法在2D和3D重建方面都有显著改进，特别是在城市场景中车辆和人等物体被严重遮挡的场景中。 et.al.|[2403.19022](http://arxiv.org/abs/2403.19022)|null|
|**2024-03-29**|**Gamba: Marry Gaussian Splatting with Mamba for single view 3D reconstruction**|随着对自动化3D内容创建管道的需求不断增长，我们解决了从单个图像高效重建3D资产的挑战。以前的方法主要依赖于分数蒸馏采样（SDS）和神经辐射场（NeRF）。尽管这些方法取得了显著的成功，但由于漫长的优化和大量的内存使用，它们遇到了实际的局限性。在本报告中，我们介绍了Gamba，一种基于单视图图像的端到端摊销3D重建模型，强调了两个主要见解：（1）3D表示：利用大量的3D高斯进行高效的3D高斯飞溅过程；（2） 骨干设计：引入基于Mamba的序列网络，该网络有助于上下文相关推理和序列（令牌）长度的线性可伸缩性，可容纳大量高斯。Gamba在数据预处理、正则化设计和训练方法方面取得了重大进展。我们使用真实世界扫描的OmniObject3D数据集，对照现有的基于优化和前馈的3D生成方法对Gamba进行了评估。在这里，Gamba在质量和数量上都展示了具有竞争力的生成能力，同时在单个NVIDIA A100 GPU上实现了约0.6秒的惊人速度。 et.al.|[2403.18795](http://arxiv.org/abs/2403.18795)|null|
|**2024-03-29**|**SplatFace: Gaussian Splat Face Reconstruction Leveraging an Optimizable Surface**|我们提出了SplatFace，这是一种新的高斯飞溅框架，用于三维人脸重建，而不依赖于精确的预定几何结构。我们的方法旨在同时提供高质量的新颖视图渲染和精确的3D网格重建。我们结合了一个通用的3D变形模型（3DMM）来提供表面几何结构，从而可以用有限的一组输入图像重建人脸。我们引入了一种联合优化策略，该策略通过协同的非刚性对齐过程来细化高斯曲面和可变形曲面。提出了一种新的距离度量，即飞溅到表面，通过考虑高斯位置和协方差来改进对准。表面信息还被用于结合世界空间致密化过程，从而获得卓越的重建质量。我们的实验分析表明，在生成具有高几何精度的三维人脸网格方面，所提出的方法在新的视图合成中与其他高斯飞溅技术和其他三维重建方法都具有竞争力。 et.al.|[2403.18784](http://arxiv.org/abs/2403.18784)|null|
|**2024-03-27**|**Breaking the Limitations with Sparse Inputs by Variational Frameworks (BLIss) in Terahertz Super-Resolution 3D Reconstruction**|数据采集、图像处理和图像质量是太赫兹（THz）3D重建成像的长期问题。考虑到与获得超分辨率（SR）数据相关的挑战以及传统计算机断层扫描（CT）中缺乏有效的SR 3D重建框架，现有方法主要针对2D场景设计。在这里，我们演示了BLIss，这是一种使用稀疏2D数据输入进行THz-SR 3D重建的新方法。BLIss将传统的CT技术和变分框架与基于Euler Elastica的自适应模型的核心无缝集成。定量的3D图像评估指标，包括高斯的标准差、平均曲率和多尺度结构相似性指数测度（MS-SSIM），验证了与传统的THz-CT模态相比，我们的变分框架方法所实现的优越的平滑度和保真度。除了对推进THz-SR 3D重建的贡献外，BLIss还展示了其在其他成像模式（如X射线和MRI）中的潜在适用性。这表明它对更广泛的成像应用领域产生了广泛的影响。 et.al.|[2403.18776](http://arxiv.org/abs/2403.18776)|**[link](https://github.com/cyiyoo/bliss)**|
|**2024-03-27**|**SAT-NGP : Unleashing Neural Graphics Primitives for Fast Relightable Transient-Free 3D reconstruction from Satellite Imagery**|当前的立体视觉管道在使用多对或三组卫星图像时产生高精度的3D重建。然而，这些管道对多日期采集可能导致的图像之间的变化很敏感。这种变化主要是由于可变的阴影、反射和瞬态物体（汽车、植被）。为了考虑到这些变化，神经辐射场（NeRF）最近被应用于多日期卫星图像。然而，神经方法是计算密集型的，需要几十个小时才能学习，而标准立体视觉管道需要几分钟。遵循即时神经图形原语的思想，我们建议使用有效的采样策略和多分辨率哈希编码来加速学习。我们的模型，卫星神经图形原件（SAT-NGP）将学习时间减少到15分钟，同时保持3D重建的质量。 et.al.|[2403.18711](http://arxiv.org/abs/2403.18711)|null|

<p align=right>(<a href=#updated-on-20240402>back to top</a>)</p>

## Diffusion

|Publish Date|Title|Abstract|PDF|Code|
|---|---|---|---|---|
|**2024-03-29**|**Relation Rectification in Diffusion Model**|尽管有着非凡的生成能力，但大型文本到图像的扩散模型，就像熟练但粗心的艺术家一样，经常难以准确描绘物体之间的视觉关系。正如我们通过仔细分析发现的那样，这个问题源于一个错位的文本编码器，该编码器难以解释特定的关系并区分相关对象的逻辑顺序。为了解决这个问题，我们引入了一项名为“关系矫正”的新任务，旨在细化模型，以准确地表示它最初无法生成的给定关系。为了解决这一问题，我们提出了一种利用异构图卷积网络（HGCN）的创新解决方案。它对输入提示中的关系项和相应对象之间的方向关系进行建模。具体来说，我们在一对具有相同关系词但对象顺序相反的提示上优化HGCN，并辅以一些参考图像。轻量级的HGCN调整文本编码器生成的文本嵌入，确保文本关系在嵌入空间中的准确反映。至关重要的是，我们的方法保留了文本编码器和扩散模型的参数，保留了模型在不相关描述上的鲁棒性能。我们在一个新策划的不同关系数据集上验证了我们的方法，证明了在生成具有精确视觉关系的图像方面的定量和定性增强。项目页面：https://wuyinwei-hah.github.io/rrnet.github.io/. et.al.|[2403.20249](http://arxiv.org/abs/2403.20249)|null|
|**2024-03-29**|**Graph Neural Aggregation-diffusion with Metastability**|基于微分方程的连续图神经模型扩展了图神经网络的结构。由于图扩散和消息传递之间的联系，基于扩散的模型得到了广泛的研究。然而，扩散自然会将系统推向平衡状态，从而导致过度平滑等问题。为此，我们受图-聚集-扩散方程的启发，提出了GRADE，该方程包括非线性扩散和相互作用势引起的聚集之间的微妙平衡。通过聚集-扩散方程获得的节点表示表现出亚稳态，表明特征可以聚集成多个簇。此外，这些集群内的动态可以持续很长一段时间，从而有可能缓解过度平滑效应。我们模型中的这种非线性扩散推广了现有的基于扩散的模型，并与经典GNN建立了联系。我们证明了GRADE在各种基准测试中实现了有竞争力的性能，并缓解了增强的狄利克雷能量所证明的GNN中的过平滑问题。 et.al.|[2403.20221](http://arxiv.org/abs/2403.20221)|null|
|**2024-03-29**|**Scaled Brownian motion with random anomalous diffusion exponent**|尺度布朗运动（SBM）被认为是典型的随机过程之一，具有以扩散指数为特征的反常扩散性质。这是一个具有独立增量的高斯自相似过程，已在从湍流、随机水文到生物物理的各个领域得到应用。在我们的论文中，受最近单粒子跟踪生物学实验的启发，我们引入了一种称为具有随机指数的缩放布朗运动（SBMRE）的过程，该过程在单个轨迹的水平上保持了SBM特性，尽管轨迹上的异常扩散指数随机变化。我们讨论了SBMRE的主要概率性质，包括它的概率密度函数（pdf）和第q个绝对矩。此外，我们还给出了时间平均均方位移（TAMSD）的期望值和遍历性破缺参数。此外，我们还分析了半无限域中第一次命中时间的pdf，SBMRE的鞅性质及其随机指数。作为特例，我们考虑了异常扩散指数的两种分布，即两点分布和贝塔分布，并讨论了在这种情况下所呈现特征的渐近性。通过数值模拟验证了SBMRE的理论结果，并与SBM的相应特性进行了比较。 et.al.|[2403.20206](http://arxiv.org/abs/2403.20206)|null|
|**2024-03-29**|**Motion Inversion for Video Customization**|在这项研究中，我们提出了一种新的视频生成中的运动定制方法，解决了在视频生成模型中深入探索运动表示的广泛差距。认识到视频的时空特性带来的独特挑战，我们的方法引入了运动嵌入，这是一组从给定视频中导出的显式、时间相干的一维嵌入。这些嵌入被设计为与视频扩散模型的时间变换器模块无缝集成，在不影响空间完整性的情况下跨帧调制自注意力计算。我们的方法为运动表示提供了一个紧凑而有效的解决方案，并通过嵌入空间中的矢量运算实现了对运动特征的复杂操作。此外，我们确定了视频生成模型中的时间差异，这是指不同运动模块如何处理帧之间的时间关系的变化。我们利用这种理解来优化我们的运动嵌入的集成。我们的贡献包括为定制任务引入量身定制的运动嵌入，深入了解视频模型中的时间处理差异，以及通过广泛的实验证明我们的方法的实际优势和有效性。 et.al.|[2403.20193](http://arxiv.org/abs/2403.20193)|null|
|**2024-03-29**|**Energy solutions of the Cauchy-Dirichlet problem for fractional nonlinear diffusion equations**|本文研究了有界域中分数阶（和非分数阶）非线性扩散方程的Cauchy-Dirichlet问题。主要结果包括在没有符号限制的能量类中的适定性，以及这种（可能改变符号的）能量解在适当的重新缩放后收敛到渐近轮廓。它们将仅在变分格式中证明，而不使用半群理论或经典拟线性抛物型理论。证明是自包含的，并且以完全统一的方式对分数和非分数情况以及多孔介质和快速扩散情况进行。 et.al.|[2403.20176](http://arxiv.org/abs/2403.20176)|null|
|**2024-03-29**|**Na Vacancy Driven Phase Transformation and Fast Ion Conduction in W-doped Na $_3$SbS$_4$ from Machine Learning Force Fields**|固态钠电池需要在室温下导电的有效电解质。研究了Na$_3$SbS$_4$（Pn=P，Sb；Ch=S，Se）家族的高钠离子电导率。在这些材料中介导离子扩散的Na空位的群体可以通过在pnictogen位点上进行脂蛋白掺杂来增强。为了探究外源掺杂的微观作用及其对扩散和相稳定性的影响，我们基于等变图神经网络训练了Na$_{3-x}$W$_{x}$Sb$_{1-x}$S$_4$ 的机器学习力场。对大尺度分子动力学轨迹的分析表明，增加的Na空位布居在较低温度下稳定了全局立方相，增强了Na离子的扩散，并且取代W掺杂剂的显式作用是有限的。在全局立方相中，我们观察到原子与平均对称性的大而长期的偏差，这与最近的实验建议相呼应。还提出了相关钠离子扩散的证据，这些证据支持了这些材料的超离子性质。 et.al.|[2403.20138](http://arxiv.org/abs/2403.20138)|null|
|**2024-03-29**|**FreeSeg-Diff: Training-Free Open-Vocabulary Segmentation with Diffusion Models**|基础模型在处理许多领域和任务方面表现出了前所未有的能力。CLIP等模型目前被广泛用于桥接跨模态表示，而文本到图像的扩散模型可以说是逼真图像生成方面的领先模型。图像生成模型是在海量数据集上训练的，这些数据集为它们提供了强大的内部空间表示。在这项工作中，我们探索了这种表示在图像生成之外的潜在好处，特别是对于密集的视觉预测任务。我们专注于图像分割的任务，传统上通过在封闭词汇数据集上训练模型来解决，并使用像素级注释。为了避免注释成本或训练大型扩散模型，我们将我们的设置限制为零样本和无训练。简言之，我们的管道利用不同且相对较小的开源基础模型进行零样本开放式词汇细分。管道如下：图像被传递到字幕器模型（即BLIP）和扩散模型（即稳定扩散模型），以分别生成文本描述和视觉表示。对特征进行聚类和二值化，以获得每个对象的类不可知掩码。然后，这些掩码被映射到一个文本类，使用CLIP模型来支持开放词汇表。最后，我们增加了一个细化步骤，可以获得更精确的分割掩码。我们的方法（称为FreeSeg-Diff）不依赖于任何训练，在Pascal VOC和COCO数据集上都优于许多基于训练的方法。此外，与最近的弱监督分割方法相比，我们显示了非常有竞争力的结果。我们提供了全面的实验，显示了与其他预训练模型相比，扩散模型特征的优越性。项目页面：https://bcorrad.github.io/freesegdiff/ et.al.|[2403.20105](http://arxiv.org/abs/2403.20105)|null|
|**2024-03-29**|**SGD: Street View Synthesis with Gaussian Splatting and Diffusion Prior**|街道场景的新颖视图合成（NVS）在自动驾驶仿真中起着至关重要的作用。目前实现它的主流技术是神经渲染，如神经辐射场（NeRF）和三维高斯散射（3DGS）。尽管已经取得了令人兴奋的进展，但在处理街景时，当前的方法很难在与训练视点显著偏离的视点处保持渲染质量。这个问题源于移动车辆上固定摄像头拍摄的稀疏训练视图。为了解决这个问题，我们提出了一种新的方法，通过利用扩散模型的先验知识和互补的多模态数据来增强3DGS的能力。具体来说，我们首先通过添加相邻帧的图像作为条件来微调扩散模型，同时利用激光雷达点云的深度数据来提供额外的空间信息。然后，我们应用扩散模型对训练过程中看不见的视图处的3DGS进行正则化。实验结果验证了我们的方法与当前最先进的模型相比的有效性，并证明了它在从更广阔的视角渲染图像方面的进步。 et.al.|[2403.20079](http://arxiv.org/abs/2403.20079)|null|
|**2024-03-29**|**Efficacy of the Sterile Insect Technique in the presence of inaccessible areas: A study using two-patch models**|昆虫不育技术（SIT）是控制病媒的可持续策略之一，包括释放不育的雄性，与野生雌性交配，从而减少并最终局部消灭野生种群。当无法直接释放无菌昆虫的无法进入区域时，SIT在现场的实施可能会出现问题，野生昆虫从这些区域迁移到处理区可能会影响该技术的效果。然而，我们也可以利用不育个体的移动来控制这些无法到达的地方的野生种群。在本文中，我们推导了伊蚊的双斑块模型，其中我们考虑了处理区域和无法进入区域之间的离散扩散。我们研究了两种不同的释放策略（恒定和脉冲周期性释放），通过使用模型的单调性，我们表明，如果释放的不育雄性数量超过某个阈值，该技术将成功地将这两个地区的整个种群推向灭绝。该阈值不仅取决于种群的生物学参数，还取决于两个斑块之间的扩散。 et.al.|[2403.20069](http://arxiv.org/abs/2403.20069)|null|
|**2024-03-29**|**Optimal s-boxes against alternative operations**|Civino等人已经描述了当使用来自消息空间上同构于翻译组的组的替代操作时，使SPN暴露于差分密码分析的漏洞的扩散层。在这项研究中，我们提出了一种扩散层的分类，该分类在具有4位s盒的密码的并行可选操作中表现出线性，从而实现了同时针对块内所有s盒的可选差分攻击的可能性。此外，正如Leander和Poschmann（2007）所定义的，我们研究了所有类别的最优4位s盒关于替代运算的微分行为。我们的研究表明，某些类包含弱排列w.r.t.替代差分攻击，我们利用这些漏洞执行了一系列实验。 et.al.|[2403.20059](http://arxiv.org/abs/2403.20059)|null|

<p align=right>(<a href=#updated-on-20240402>back to top</a>)</p>

## NeRF

|Publish Date|Title|Abstract|PDF|Code|
|---|---|---|---|---|
|**2024-03-29**|**Grounding and Enhancing Grid-based Models for Neural Fields**|当代许多研究利用基于网格的模型来表示神经场，但仍然缺乏对基于网格模型的系统分析，阻碍了这些模型的改进。因此，本文介绍了一个基于网格的模型的理论框架。该框架指出，这些模型的逼近和泛化行为是由网格切线核（GTK）决定的，GTK是基于网格的模型的固有性质。所提出的框架有助于对各种基于网格的模型进行一致和系统的分析。此外，引入的框架推动了一种新的基于网格的模型的开发，该模型名为乘法傅立叶自适应网格（MulFAGrid）。数值分析表明，MulFAGrid表现出比其前身更低的泛化界，表明其具有鲁棒的泛化性能。实证研究表明，MulFAGrid在各种任务中都取得了最先进的性能，包括2D图像拟合、3D符号距离场（SDF）重建和新颖的视图合成，表现出了卓越的表示能力。项目网站位于https://sites.google.com/view/cvpr24-2034-submission/home. et.al.|[2403.20002](http://arxiv.org/abs/2403.20002)|null|
|**2024-04-01**|**Efficient 3D Instance Mapping and Localization with Neural Fields**|我们解决了从一系列摆姿势的RGB图像中学习用于3D实例分割的隐式场景表示的问题。为此，我们引入了3DIML，这是一种新的框架，可以有效地学习可以从新的视点渲染的标签字段，以产生视图一致的实例分割掩码。3DIML显著改进了现有的基于隐式场景表示的方法的训练和推理运行时。与现有技术相反，现有技术以自我监督的方式优化神经场，需要复杂的训练过程和损失函数设计，3DIML利用了两阶段过程。第一阶段InstanceMap将前端实例分割模型生成的图像序列的2D分割掩码作为输入，并将图像上的相应掩码与3D标签相关联。然后，在第二阶段InstanceLift中使用这些几乎视图一致的伪标签掩码来监督神经标签字段的训练，该字段对InstanceMap遗漏的区域进行插值并解决歧义。此外，我们介绍了InstanceLoc，它能够在给定训练过的标签字段和现成的图像分割模型的情况下，通过融合两者的输出，实现实例掩码的近实时定位。我们在Replica和ScanNet数据集的序列上评估了3DIML，并证明了在图像序列的温和假设下3DIML的有效性。与现有的质量相当的隐式场景表示方法相比，我们实现了巨大的实际加速，展示了其促进更快、更有效的3D场景理解的潜力。 et.al.|[2403.19797](http://arxiv.org/abs/2403.19797)|null|
|**2024-03-28**|**Neural Fields for 3D Tracking of Anatomy and Surgical Instruments in Monocular Laparoscopic Video Clips**|腹腔镜视频跟踪主要关注两种目标类型：手术器械和解剖结构。前者可用于技能评估，而后者对于虚拟覆盖的投影是必要的。在仪器和解剖跟踪通常被视为两个独立的问题的情况下，在本文中，我们提出了一种同时对所有结构进行联合跟踪的方法。基于单个2D单眼视频剪辑，我们训练神经场来表示连续的时空场景，用于创建至少一帧中可见的所有表面的3D轨迹。由于仪器尺寸较小，它们通常只覆盖图像的一小部分，导致跟踪精度下降。因此，我们建议增强类权重以改善仪器轨迹。我们评估了对腹腔镜胆囊切除术视频片段的跟踪，发现解剖结构和器械的平均跟踪准确率分别为92.4%和87.4%。此外，我们还评估了从该方法的场景重建中获得的深度图的质量。我们表明，这些伪深度具有与最先进的预训练深度估计器相当的质量。在SCARED数据集中的腹腔镜视频上，该方法预测深度的MAE为2.9 mm，相对误差为9.2%。这些结果表明了使用神经场进行腹腔镜场景的单目3D重建的可行性。 et.al.|[2403.19265](http://arxiv.org/abs/2403.19265)|null|
|**2024-03-28**|**From Activation to Initialization: Scaling Insights for Optimizing Neural Fields**|在计算机视觉领域，神经场作为一种利用神经网络进行信号表示的现代工具，已经获得了突出地位。尽管在调整这些网络以解决各种问题方面取得了显著进展，但该领域仍然缺乏一个全面的理论框架。本文旨在通过深入研究初始化和激活之间复杂的相互作用来解决这一差距，为神经领域的稳健优化提供基础。我们的理论见解揭示了网络初始化、架构选择和优化过程之间的深层次联系，强调在设计尖端神经场时需要整体方法。 et.al.|[2403.19205](http://arxiv.org/abs/2403.19205)|null|
|**2024-03-22**|**LATTE3D: Large-scale Amortized Text-To-Enhanced3D Synthesis**|最近的文本到3D生成方法产生了令人印象深刻的3D结果，但需要耗时的优化，每次提示可能需要一个小时。ATT3D等摊销方法同时优化多个提示以提高效率，实现快速的文本到三维合成。然而，它们无法捕捉高频几何体和纹理细节，并且难以缩放到大型提示集，因此泛化能力较差。我们引入LATTE3D，解决了这些限制，以在更大的提示集上实现快速、高质量的生成。我们方法的关键是1）构建可扩展的体系结构，2）在优化过程中通过3D感知扩散先验、形状正则化和模型初始化来利用3D数据，以实现对各种复杂训练提示的鲁棒性。LATTE3D对神经场和纹理表面生成进行摊销，以在单个正向过程中生成高度详细的纹理网格。LATTE3D在400ms内生成3D对象，并可通过快速测试时间优化进一步增强。 et.al.|[2403.15385](http://arxiv.org/abs/2403.15385)|null|
|**2024-03-20**|**Visual Imitation Learning of Task-Oriented Object Grasping and Rearrangement**|面向任务的物体抓取和重排是机器人完成不同现实操作任务的关键技能。然而，由于对物体的部分观察和分类物体的形状变化，它们仍然具有挑战性。在本文中，我们提出了多特征隐式模型（MIMO），这是一种新的对象表示，它在隐式神经场中对点和对象之间的多个空间特征进行编码。在多个特征上训练这样的模型可以确保它在不同方面一致地嵌入物体形状，从而提高其在从局部观察、形状相似性测量和建模物体之间的空间关系的物体形状重建中的性能。基于MIMO，我们提出了一个从单个或多个人类演示视频中学习面向任务的对象抓取和重排的框架。仿真评估表明，我们的方法在多视图和单视图观测方面优于最先进的方法。真实世界的实验证明了我们的方法在操纵任务的单次和少次模仿学习中的有效性。 et.al.|[2403.14000](http://arxiv.org/abs/2403.14000)|null|
|**2024-03-18**|**LN3Diff: Scalable Latent Neural Fields Diffusion for Speedy 3D Generation**|随着生成模型和可微分绘制技术的进步，神经绘制领域取得了重大进展。尽管2D扩散已经取得了成功，但统一的3D扩散管道仍然悬而未决。本文介绍了一种称为LN3Diff的新框架来解决这一差距，并实现快速、高质量和通用的条件3D生成。我们的方法利用3D感知架构和变分自动编码器（VAE）将输入图像编码到结构化、紧凑和3D潜在空间中。潜像由基于变换器的解码器解码为高容量的3D神经场。通过在这个3D感知的潜在空间上训练扩散模型，我们的方法在ShapeNet上实现了最先进的3D生成性能，并在各种数据集的单目3D重建和条件3D生成中表现出卓越的性能。此外，它在推理速度方面超过了现有的3D扩散方法，不需要每实例优化。我们提出的LN3Diff在三维生成建模方面取得了重大进展，并有望在三维视觉和图形任务中应用。 et.al.|[2403.12019](http://arxiv.org/abs/2403.12019)|null|
|**2024-03-15**|**NeuralOCT: Airway OCT Analysis via Neural Fields**|光学相干断层扫描（OCT）是眼科中一种流行的模式，也用于血管内。我们对这项工作的兴趣是在婴儿和儿童气道异常的背景下进行OCT，其中OCT的高分辨率和无辐射的事实很重要。气道OCT的目标是提供气道几何形状的准确估计（2D和3D），以评估气道异常，如声门下狭窄。我们提出 $\texttt｛NeuralOCT｝$，这是一种基于学习的方法来处理气道OCT图像。具体而言，$\texttt｛NeuralOCT｝$通过稳健地桥接两个步骤从OCT扫描中提取3D几何形状：通过2D分割提取点云和通过神经场从点云中重建3D。我们的实验表明，$\texttt｛NeuralOCT｝$ 可以产生准确而稳健的3D气道重建，平均A线误差小于70微米。我们的代码将在GitHub上提供。 et.al.|[2403.10622](http://arxiv.org/abs/2403.10622)|null|
|**2024-03-15**|**NECA: Neural Customizable Human Avatar**|人类化身已经成为一种具有各种应用的新型3D资产。理想情况下，人类化身应该是完全可定制的，以适应不同的设置和环境。在这项工作中，我们介绍了NECA，这是一种能够从单目或稀疏视图视频中学习多功能人体表示的方法，能够在姿势、阴影、形状、照明和纹理等方面进行细粒度定制。我们方法的核心是在互补的双空间中表示人类，并预测几何、反照率、阴影以及外部照明的解开神经场，从中我们能够通过体积渲染获得具有高频细节的真实感渲染。大量实验证明了我们的方法在真实感渲染以及各种编辑任务（如新颖的姿势合成和重新照明）方面优于最先进的方法。代码位于https://github.com/iSEE-Laboratory/NECA. et.al.|[2403.10335](http://arxiv.org/abs/2403.10335)|**[link](https://github.com/isee-laboratory/neca)**|
|**2024-03-13**|**Representing Anatomical Trees by Denoising Diffusion of Implicit Neural Fields**|解剖树在临床诊断和治疗计划中起着核心作用。然而，由于解剖树的拓扑结构和几何形状多变且复杂，因此准确地表示解剖树具有挑战性。使用医学成像捕获的表示树状结构的传统方法虽然对可视化血管和支气管网络非常宝贵，但在分辨率、灵活性和效率方面存在缺陷。最近，隐式神经表示（INRs）已经成为准确有效地表示形状的强大工具。我们提出了一种使用INR表示解剖树的新方法，同时还通过INR空间中的去噪扩散来捕捉一组树的分布。我们以任何所需的分辨率准确捕捉解剖树的复杂几何形状和拓扑结构。通过广泛的定性和定量评估，我们展示了高保真度树重建，具有任意分辨率但紧凑的存储，以及跨解剖部位和树复杂性的多功能性。 et.al.|[2403.08974](http://arxiv.org/abs/2403.08974)|**[link](https://github.com/sinashish/treediffusion)**|

<p align=right>(<a href=#updated-on-20240402>back to top</a>)</p>

[contributors-shield]: https://img.shields.io/github/contributors/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[contributors-url]: https://github.com/Vincentqyw/cv-arxiv-daily/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[forks-url]: https://github.com/Vincentqyw/cv-arxiv-daily/network/members
[stars-shield]: https://img.shields.io/github/stars/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[stars-url]: https://github.com/Vincentqyw/cv-arxiv-daily/stargazers
[issues-shield]: https://img.shields.io/github/issues/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[issues-url]: https://github.com/Vincentqyw/cv-arxiv-daily/issues

