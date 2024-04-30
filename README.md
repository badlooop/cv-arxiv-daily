[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]

## Updated on 2024.04.30
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
|**2024-04-29**|**3D Gaussian Splatting with Deferred Reflection**|基于神经和高斯的辐射场方法的出现在新视图合成领域取得了巨大成功。然而，镜面反射仍然是不平凡的，因为众所周知，高频辐射场很难稳定准确地拟合。我们提出了一种延迟着色方法来有效地渲染高斯飞溅的镜面反射。关键的挑战来自环境图反射模型，该模型需要精确的表面法线，同时使用不连续的梯度来限制法线估计。我们利用延迟着色生成的每像素反射梯度来桥接相邻高斯的优化过程，允许几乎正确的法线估计逐渐传播并最终传播到所有反射对象上。我们的方法在合成高质量镜面反射效果方面显著优于最先进的技术和并行工作，证明了合成场景和真实世界场景的峰值信噪比（PSNR）都得到了一致的提高，同时以几乎与香草高斯飞溅相同的帧速率运行。 et.al.|[2404.18454](http://arxiv.org/abs/2404.18454)|null|
|**2024-04-29**|**$ν$-DBA: Neural Implicit Dense Bundle Adjustment Enables Image-Only Driving Scene Reconstruction**|传感器轨迹和3D地图的联合优化是束调整（BA）的一个关键特性，对自动驾驶至关重要。本文提出了$\nu$ -DBA，这是一种使用三维神经隐式曲面进行地图参数化来实现几何密集束平差（DBA）的新框架，该框架使用密集光流预测引导的几何误差来优化地图表面和轨迹姿态。此外，我们通过逐场景自监督对光流模型进行微调，以进一步提高密集映射的质量。我们在多个驾驶场景数据集上的实验结果表明，我们的方法实现了卓越的轨迹优化和密集的重建精度。我们还研究了光度误差和不同的神经几何先验对表面重建和新视图合成性能的影响。我们的方法是朝着在密集束调整中利用神经隐式表示实现更准确的轨迹和详细的环境映射迈出的重要一步。 et.al.|[2404.18439](http://arxiv.org/abs/2404.18439)|null|
|**2024-04-25**|**Depth Supervised Neural Surface Reconstruction from Airborne Imagery**|虽然最初是为新颖的视图合成而开发的，但神经辐射场（NeRF）最近已成为多视图立体（MVS）的替代品。在一系列研究活动的触发下，已经获得了有希望的结果，尤其是在无纹理、透明和反射表面方面，而这些场景对传统的基于MVS的方法仍然具有挑战性。然而，这些调查大多集中在近距离场景上，对空中场景的研究仍然缺失。对于这项任务，NeRF在图像冗余度低和数据证据薄弱的区域面临潜在的困难，如经常在街道峡谷、立面或建筑阴影中发现的那样。此外，训练这样的网络在计算上是昂贵的。因此，我们工作的目的有两个：首先，我们研究NeRFs对代表不同特征的航空图像块的适用性，如仅最低点、倾斜和高分辨率图像。其次，在这些调查过程中，我们证明了从联络点测量中积分深度先验的好处，这些测量是在预先假设的束块调整过程中提供的。我们的工作基于最先进的框架VolSDF，该框架通过符号距离函数（SDF）对3D场景进行建模，因为与普通NeRF中的标准体积表示相比，这更适用于表面重建。为了进行评估，将基于NeRF的重建与航空图像的公开基准数据集的结果进行比较。 et.al.|[2404.16429](http://arxiv.org/abs/2404.16429)|null|
|**2024-04-25**|**DIG3D: Marrying Gaussian Splatting with Deformable Transformer for Single Image 3D Reconstruction**|在本文中，我们研究了从单视图RGB图像进行三维重建的问题，并提出了一种新的方法，称为DIG3D，用于三维对象重建和新的视图合成。我们的方法利用编码器-解码器框架，该框架在编码器的深度感知图像特征的指导下在解码器中生成3D高斯。特别是，我们介绍了可变形变换器的使用，允许通过3D参考点和多层细化自适应进行高效和有效的解码。通过利用3D高斯的优势，我们的方法为单视图图像的3D重建提供了一个高效而准确的解决方案。我们在ShapeNet SRN数据集上评估了我们的方法，在汽车和椅子数据集中分别获得了24.21和24.98的PSNR。结果优于最近的方法约2.25%，证明了我们的方法在获得优异结果方面的有效性。 et.al.|[2404.16323](http://arxiv.org/abs/2404.16323)|null|
|**2024-04-23**|**FlowMap: High-Quality Camera Poses, Intrinsics, and Depth via Gradient Descent**|本文介绍了FlowMap，这是一种端到端可微的方法，用于解决视频序列的精确相机姿态、相机本质和每帧密集深度。我们的方法对一个简单的最小二乘目标执行每视频梯度下降最小化，该目标将由深度、本质和姿态引起的光流与通过现成的光流和点跟踪获得的对应关系进行比较。除了使用点轨迹来鼓励长期的几何一致性外，我们还引入了适用于一阶优化的深度、本质和姿态的可微重新参数化。我们的经验表明，通过我们的方法恢复的相机参数和密集深度能够使用高斯飞溅在360度轨迹上进行照片逼真的新视图合成。我们的方法不仅远远优于现有的基于梯度下降的束调整方法，而且在360度新视图合成的下游任务上，令人惊讶地与最先进的SfM方法COLMAP不相上下（尽管我们的方法完全基于梯度下降，完全可微，并与传统的SfM完全不同）。 et.al.|[2404.15259](http://arxiv.org/abs/2404.15259)|**[link](https://github.com/dcharatan/flowmap)**|
|**2024-04-22**|**CrossScore: Towards Multi-View Image Evaluation and Scoring**|我们引入了一种新的交叉参考图像质量评估方法，该方法有效地填补了图像评估领域的空白，补充了一系列已建立的评估方案——从SSIM等全参考指标、NIQE等无参考指标到FID等通用参考指标，以及CLIPScore等多模式参考指标。利用具有交叉注意力机制的神经网络和NVS优化的独特数据收集管道，我们的方法能够在不需要地面实况参考的情况下进行准确的图像质量评估。通过将查询图像与同一场景的多个视图进行比较，我们的方法解决了新视图合成（NVS）和无法获得直接参考图像的类似任务中现有度量的局限性。实验结果表明，我们的方法与全参考度量SSIM密切相关，而不需要地面实况参考。 et.al.|[2404.14409](http://arxiv.org/abs/2404.14409)|null|
|**2024-04-22**|**Scene Coordinate Reconstruction: Posing of Image Collections via Incremental Learning of a Relocalizer**|我们处理从描绘场景的一组图像中估计相机参数的任务。流行的基于特征的运动结构（SfM）工具通过增量重建来解决这一任务：它们重复稀疏3D点的三角测量和将更多相机视图注册到稀疏点云。我们将来自运动的增量结构重新解释为视觉重定位器的迭代应用和改进，即将新视图注册到重建的当前状态的方法。这种视角使我们能够研究不植根于局部特征匹配的替代视觉重定位器。我们展示了场景坐标回归，一种基于学习的重新定位方法，使我们能够从未融合的图像中构建隐含的神经场景表示。与其他基于学习的重建方法不同，我们不需要姿态先验，也不需要顺序输入，并且我们可以有效地优化数千幅图像。我们的方法ACE0（ACE Zero）估计相机姿态的精度与基于特征的SfM相当，这一点在新的视图合成中得到了证明。项目页面：https://nianticlabs.github.io/acezero/ et.al.|[2404.14351](http://arxiv.org/abs/2404.14351)|null|
|**2024-04-22**|**NeRF-DetS: Enhancing Multi-View 3D Object Detection with Sampling-adaptive Network of Continuous NeRF-based Representation**|作为前期工作，NeRF Det将新视图合成和3D感知的任务统一起来，证明感知任务可以受益于NeRF等新视图合成方法，显著提高室内多视图3D对象检测的性能。使用NeRF的几何MLP将检测头的注意力引导到关键部件，并结合新视图渲染的自监督损失，有助于实现改进。为了更好地利用在空间中通过神经渲染进行连续表示的显著优势，我们引入了一种新的3D感知网络结构NeRF DetS。NeRF DetS的关键部件是多级采样自适应网络，使采样过程从粗到细自适应。此外，我们还提出了一种优越的多视图信息融合方法，称为多头加权融合。这种融合方法有效地解决了在使用算术平均值时丢失多视图信息的挑战，同时保持了较低的计算成本。在ScanNetV2数据集上，NeRF DetS的性能优于竞争对手NeRF Det，分别提高了+5.02%和+5.92%mAP@.25和mAP@.50分别地 et.al.|[2404.13921](http://arxiv.org/abs/2404.13921)|null|
|**2024-04-23**|**CT-NeRF: Incremental Optimizing Neural Radiance Field and Poses with Complex Trajectory**|神经辐射场（NeRF）在高质量的三维场景重建中取得了令人印象深刻的成果。然而，NeRF在很大程度上依赖于精确的相机姿势。虽然最近像BARF这样的工作已经在NeRF中引入了相机姿态优化，但它们的适用性仅限于简单的轨迹场景。现有的方法在处理涉及大旋转的复杂轨迹时会遇到困难。为了解决这一限制，我们提出了CT NeRF，这是一种仅使用RGB图像而不使用姿态和深度输入的增量重建优化流水线。在这个流水线中，我们首先提出了在连接相邻帧的姿态图下进行局部全局束调整，以加强姿态之间的一致性，从而避免仅由姿态与场景结构的一致性引起的局部最小值。此外，我们将姿态之间的一致性实例化为由输入图像对之间的像素级对应产生的重新投影的几何图像距离约束。通过增量重建，CT NeRF能够恢复相机姿态和场景结构，并能够处理具有复杂轨迹的场景。我们在两个真实世界的数据集NeRFBuster和Free数据集上评估了CT NeRF的性能，这两个数据集具有复杂的轨迹。结果表明，CT NeRF在新的视图合成和姿态估计精度方面优于现有方法。 et.al.|[2404.13896](http://arxiv.org/abs/2404.13896)|null|
|**2024-04-22**|**PGAHum: Prior-Guided Geometry and Appearance Learning for High-Fidelity Animatable Human Reconstruction**|最近关于隐式几何表示学习和神经渲染的技术已经显示出从稀疏视频输入进行三维人体重建的有希望的结果。然而，重建详细的表面几何结构仍然具有挑战性，甚至更难将逼真的新颖视图与动画人体姿势合成。在这项工作中，我们介绍了PGAHum，一种用于高保真动画人体重建的先验引导几何和外观学习框架。我们在PGAHum的三个关键模块中充分利用了3D人体先验，以实现具有复杂细节的高质量几何重建和对看不见的姿势的真实感视图合成。首先，提出了一种基于先验的三维人体隐式几何表示，该表示包含由三平面网络预测的delta SDF和从先验SMPL模型导出的基本SDF，以解纠缠的方式对表面细节和体型进行建模。其次，我们引入了一种新颖的先验引导采样策略，该策略充分利用人体姿态和身体的先验信息对体表内或体表附近的查询点进行采样。通过避免在空的3D空间中进行不必要的学习，神经渲染可以恢复更多的外观细节。最后，我们提出了一种新的迭代后向变形策略，以逐步找到观测空间中查询点的对应关系。基于SMPL模型提供的先验知识来学习蒙皮权重预测模型，以实现迭代的反向LBS变形。在各种数据集上进行了广泛的定量和定性比较，结果证明了我们框架的优越性。消融研究还验证了每个方案在几何和外观学习方面的有效性。 et.al.|[2404.13862](http://arxiv.org/abs/2404.13862)|null|

<p align=right>(<a href=#updated-on-20240430>back to top</a>)</p>

## 3D Reconstruction

|Publish Date|Title|Abstract|PDF|Code|
|---|---|---|---|---|
|**2024-04-29**|**Bootstrap 3D Reconstructed Scenes from 3D Gaussian Splatting**|神经渲染技术的最新发展极大地增强了学术和商业领域中照片逼真3D场景的渲染。最新的方法被称为3D高斯飞溅（3D-GS），为渲染质量和速度设定了新的基准。然而，3D-GS的局限性在合成新的视点时变得明显，尤其是对于与训练中看到的视点大相径庭的视点。此外，放大或缩小时还会出现诸如膨胀和混叠之类的问题。这些挑战都可以追溯到一个根本问题：采样不足。在我们的论文中，我们提出了一种显著解决这个问题的自举方法。这种方法使用扩散模型来增强使用经过训练的3D-GS的新视图的渲染，从而简化训练过程。我们的结果表明，自举有效地减少了工件，并明显增强了评估指标。此外，我们证明了我们的方法是通用的，可以很容易地集成，使各种3D重建项目从我们的方法中受益。 et.al.|[2404.18669](http://arxiv.org/abs/2404.18669)|null|
|**2024-04-29**|**Reconstructing Satellites in 3D from Amateur Telescope Images**|本文提出了一个利用小型业余望远镜拍摄的视频对近地轨道卫星进行三维重建的框架。从这些望远镜获得的视频数据与标准3D重建任务的数据有很大不同，其特征是强烈的运动模糊、大气湍流、普遍的背景光污染、焦距延长和观测视角受限。为了应对这些挑战，我们的方法从全面的预处理工作流程开始，该工作流程包括基于深度学习的图像恢复、特征点提取和相机姿态初始化。我们继续应用改进的3D高斯飞溅算法来重建3D模型。我们的技术支持同时进行3D高斯训练和姿态估计，从而能够从稀疏、嘈杂的数据中稳健地生成复杂的3D点云。编辑后阶段进一步支持了这一过程，该阶段旨在消除与我们先前对卫星几何约束的了解不一致的噪声点。我们使用合成数据集和中国空间站的实际观测结果验证了我们的方法，展示了其在从地面观测重建三维空间物体方面优于现有方法的显著优势。 et.al.|[2404.18394](http://arxiv.org/abs/2404.18394)|null|
|**2024-04-27**|**Unpaired Multi-view Clustering via Reliable View Guidance**|本文重点研究了不成对的多视图聚类（UMC），这是一个具有挑战性的问题，其中成对的观测样本在多个视图中不可用。目标是使用所有视图中未配对的观测样本执行有效的联合聚类。在不完全多视图聚类中，现有的方法通常依赖于视图之间的样本配对来捕获它们的互补性。然而，这不适用于UMC的情况。因此，我们的目标是提取视图之间一致的聚类结构。在UMC中，出现了两个具有挑战性的问题：由于缺乏标签而导致的聚类结构不确定和由于缺乏配对样本而导致的配对关系不确定。我们假设具有良好聚类结构的视图是可靠的视图，它充当了指导其他视图聚类的监督者。在可靠视图的指导下，在实现可靠视图与其他视图对齐的同时，获得了这些视图的更确定的聚类结构。然后，我们提出了具有一个可靠视图（RG-UMC）和多个可靠视图的UMC的可靠视图引导（RGs-UMC）。具体来说，我们分别设计了具有一个可靠视图和多个可靠视图的对齐模块，以自适应地指导优化过程。此外，我们还利用紧致性模块来增强同一聚类中样本之间的关系。同时，将正交约束应用于潜在表示以获得判别特征。大量实验表明，RG-UMC和RGs-UMC在NMI中的平均值分别为24.14%和29.42%，优于最先进的方法。 et.al.|[2404.17894](http://arxiv.org/abs/2404.17894)|null|
|**2024-04-29**|**MV-VTON: Multi-View Virtual Try-On with Diffusion Models**|基于图像的虚拟试穿的目标是生成自然穿着给定服装的目标人物的图像。然而，大多数现有的方法只专注于正面尝试使用正面服装。当衣服和人的观点明显不一致时，特别是当人的观点不是正面的时，结果是不令人满意的。为了应对这一挑战，我们引入了多视图虚拟试穿（MV-VTON），旨在使用给定的衣服从多个视图重建一个人的穿着结果。一方面，考虑到单视图衣服为MV-VTON提供的信息不足，我们转而使用两个图像，即衣服的前视图和后视图，以尽可能多地包含完整视图。另一方面，采用了表现出卓越能力的扩散模型来执行我们的MV-VTON。特别地，我们提出了一种视图自适应选择方法，其中硬选择和软选择分别应用于全局和局部服装特征提取。这样可以确保衣服的特征大致适合人的视野。随后，我们建议使用一个联合注意力块来将服装特征与人物特征对齐并融合。此外，我们收集了一个MV-VTON数据集，即多视图服装（MVG），其中每个人都有多张不同视图和姿势的照片。实验表明，该方法不仅在使用MVG数据集的MV-VTON任务上取得了最先进的结果，而且在使用VITON-HD和DressCode数据集的正视虚拟试穿任务上也具有优势。代码和数据集将在https://github.com/hywang2002/MV-VTON . et.al.|[2404.17364](http://arxiv.org/abs/2404.17364)|**[link](https://github.com/hywang2002/mv-vton)**|
|**2024-04-26**|**Enhancing mmWave Radar Point Cloud via Visual-inertial Supervision**|与流行的激光雷达和相机系统互补，毫米波雷达对雾、暴雨和暴风雪等不利天气条件具有较强的鲁棒性，但提供稀疏的点云。目前的技术通过监督激光雷达的数据来增强点云。然而，高性能激光雷达非常昂贵，而且在车辆上并不常见。本文介绍了mmEMP，这是一种监督学习方法，使用低成本相机和惯性测量单元（IMU）增强雷达点云，实现了商用车的众包训练数据。由于动态物体的空间不可知性，引入视觉惯性（VI）监督具有挑战性。此外，射频多径诅咒产生的杂散雷达点使机器人误解了场景。mmEMP首先设计了一种动态三维重建算法，用于恢复动态特征的三维位置。然后，我们设计了一个神经网络来加密雷达数据并消除虚假的雷达点。我们在现实世界中构建了一个新的数据集。大量实验表明，根据激光雷达的数据，mmEMP与SOTA方法训练相比具有竞争力。此外，我们使用增强的点云来执行对象检测、定位和映射，以证明mmEMP的有效性。 et.al.|[2404.17229](http://arxiv.org/abs/2404.17229)|null|
|**2024-04-28**|**PhyRecon: Physically Plausible Neural Scene Reconstruction**|虽然神经隐式表示在多视图3D重建中越来越受欢迎，但之前的工作很难产生物理上合理的结果，从而限制了它们在具体人工智能和机器人等物理要求高的领域的应用。合理性的缺乏源于现有管道中缺乏物理建模，以及无法恢复复杂的几何结构。在本文中，我们介绍了PhyRecon，它是第一种利用可微渲染和可微物理模拟来学习隐式曲面表示的方法。我们的框架提出了一种新的基于可微粒子的物理模拟器，该模拟器与神经隐式表示无缝集成。其核心是通过我们提出的算法——曲面点行进立方体（SP-MC），在基于SDF的隐式表示和显式曲面点之间进行有效转换，从而实现可微分学习，同时具有渲染和物理损失。此外，我们对渲染和物理不确定性进行建模，以识别和补偿不一致和不准确的单目几何先验。物理不确定性还使物理引导的像素采样能够增强细长结构的学习。通过合并这些技术，我们的模型有助于通过外观、几何和物理进行高效的关节建模。大量实验表明，PhyRecon在重建质量方面显著优于所有最先进的方法。我们的重建结果也产生了卓越的物理稳定性，经Isaac Gym验证，在所有数据集中至少提高了40%，为未来基于物理的应用开辟了更广阔的途径。 et.al.|[2404.16666](http://arxiv.org/abs/2404.16666)|null|
|**2024-04-25**|**DIG3D: Marrying Gaussian Splatting with Deformable Transformer for Single Image 3D Reconstruction**|在本文中，我们研究了从单视图RGB图像进行三维重建的问题，并提出了一种新的方法，称为DIG3D，用于三维对象重建和新的视图合成。我们的方法利用编码器-解码器框架，该框架在编码器的深度感知图像特征的指导下在解码器中生成3D高斯。特别是，我们介绍了可变形变换器的使用，允许通过3D参考点和多层细化自适应进行高效和有效的解码。通过利用3D高斯的优势，我们的方法为单视图图像的3D重建提供了一个高效而准确的解决方案。我们在ShapeNet SRN数据集上评估了我们的方法，在汽车和椅子数据集中分别获得了24.21和24.98的PSNR。结果优于最近的方法约2.25%，证明了我们的方法在获得优异结果方面的有效性。 et.al.|[2404.16323](http://arxiv.org/abs/2404.16323)|null|
|**2024-04-24**|**Mammo-CLIP: Leveraging Contrastive Language-Image Pre-training (CLIP) for Enhanced Breast Cancer Diagnosis with Multi-view Mammography**|尽管来自多个乳腺X线照片的信息融合在提高癌症检测的准确性方面起着重要作用，但开发基于多个乳腺x线照片的计算机辅助诊断（CAD）方案仍然面临挑战，并且这种CAD方案尚未在临床实践中使用。为了克服这些挑战，我们研究了一种基于对比语言图像预训练（CLIP）的新方法，该方法引发了人们对各种医学成像任务的兴趣。通过解决以下挑战：（1）有效地将单视图CLIP用于多视图特征融合，以及（2）在有限的样本和计算资源下有效地微调该参数密集模型，我们引入了Mammo CLIP，这是第一个处理多视图乳房X光照片和相应的简单文本的多模式框架。Mammo CLIP使用早期特征融合策略来学习从左乳房和右乳房的CC和MLO视图获得的四张乳房X光照片中的多视图关系。为了提高学习效率，在CLIP图像和文本编码器中添加了即插即用适配器，用于微调参数并将更新限制在参数的1%左右。对于框架评估，我们回顾性地收集了两个数据集。第一个数据集包括470例恶性和479例良性病例，用于通过5倍交叉验证对拟议的Mammo CLIP进行少量微调和内部评估。第二个数据集，包括60例恶性和294例良性病例，用于测试Mammo CLIP的可推广性。研究结果表明，Mammo CLIP在两个数据集的AUC（0.841对0.817，0.837对0.807）上都优于最先进的交叉视图变换器。它也超过了之前两种基于CLIP的方法20.3%和14.3%。这项研究强调了应用微调视觉语言模型开发下一代基于图像文本的癌症CAD方案的潜力。 et.al.|[2404.15946](http://arxiv.org/abs/2404.15946)|null|
|**2024-04-25**|**OMEGAS: Object Mesh Extraction from Large Scenes Guided by Gaussian Segmentation**|3D重建技术的最新进展为复杂3D场景的高质量实时渲染铺平了道路。尽管取得了这些成就，但一个显著的挑战仍然存在：很难从大型场景中精确重建特定物体。当前的场景重建技术经常导致对象细节纹理的丢失，并且无法重建在视图中被遮挡或看不见的对象部分。为了应对这一挑战，我们深入研究了大型场景中特定对象的精细3D重建，并提出了一个名为OMEGAS的框架：在高斯分割的指导下从大型场景中提取对象网格。OMEGAS采用多步骤方法，以几种优秀的现成方法为基础。具体来说，最初，我们利用分段任意模型（SAM）来指导3D高斯散射（3DGS）的分割，从而创建目标对象的基本3DGS模型。然后，我们利用大规模扩散先验来进一步细化3DGS模型的细节，特别是针对原始场景视图中不可见或被遮挡的对象部分。随后，通过将3DGS模型重新渲染到场景视图上，我们实现了精确的对象分割，并有效地去除了背景。最后，使用这些仅针对目标的图像来进一步改进3DGS模型，并通过SuGaR模型提取最终的3D对象网格。在各种场景中，我们的实验表明OMEGAS显著优于现有的场景重建方法。我们的项目页面位于：https://github.com/CrystalWlz/OMEGAS et.al.|[2404.15891](http://arxiv.org/abs/2404.15891)|**[link](https://github.com/crystalwlz/omegas)**|
|**2024-04-24**|**3D Freehand Ultrasound using Visual Inertial and Deep Inertial Odometry for Measuring Patellar Tracking**|髌股关节（PFJ）问题影响四分之一的人，尽管接受了治疗，仍有20%的人经历了慢性膝关节疼痛。膝关节置换术后的不良结果和疼痛通常与髌骨追踪不良有关。CT和MRI等传统成像方法面临挑战，包括成本和金属伪影，目前没有理想的方法来观察关节运动而不出现软组织伪影或辐射暴露等问题。一种监测关节运动的新系统可以显著提高对PFJ动力学的理解，有助于更好的患者护理和结果。将2D超声与运动跟踪相结合以使用语义分割和位置配准进行关节的3D重建可能是一种解决方案。然而，需要昂贵的外部基础设施来估计扫描仪的轨迹仍然是临床上通过手持式超声扫描实现3D骨骼重建的主要限制。我们提出了视觉惯性里程计（VIO）和基于深度学习的仅惯性里程计方法，作为跟踪手持超声扫描仪的运动捕捉的替代方法。通过这些方法生成的3D重建已经证明了评估PFJ和通过徒手超声扫描进行进一步测量的潜力。结果表明，VIO方法的性能与运动捕捉方法一样好，平均重建误差分别为1.25mm和1.21mm。VIO方法是第一种无基础设施的方法，用于通过无线手持超声扫描进行骨骼的3D重建，其精度与需要外部基础设施的方式相当。 et.al.|[2404.15847](http://arxiv.org/abs/2404.15847)|null|

<p align=right>(<a href=#updated-on-20240430>back to top</a>)</p>

## Diffusion

|Publish Date|Title|Abstract|PDF|Code|
|---|---|---|---|---|
|**2024-04-29**|**Stylus: Automatic Adapter Selection for Diffusion Models**|除了用更多的数据或参数缩放基本模型之外，微调适配器还提供了一种以更低的成本生成高保真度定制图像的替代方法。因此，适配器已被开源社区广泛采用，积累了超过10万个适配器的数据库，其中大多数都是高度定制的，没有足够的描述。本文探讨了将提示与一组相关适配器匹配的问题，这是基于最近的工作，这些工作强调了编写适配器的性能增益。我们介绍了Stylus，它可以根据提示的关键字有效地选择并自动组合特定于任务的适配器。Stylus概述了一种三阶段方法，该方法首先总结具有改进的描述和嵌入的适配器，检索相关适配器，然后通过检查适配器与提示的匹配程度，根据提示的关键字进一步组装适配器。为了评估Stylus，我们开发了StylusDocs，这是一个精心策划的数据集，包含75K适配器和预先计算的适配器嵌入。在我们对流行的稳定扩散检查点的评估中，Stylus实现了更高的CLIP-FID Pareto效率，并且在人类和多模式模型作为评估者的情况下，它是基础模型的两倍。有关更多信息，请参阅stylelus-diffusion.github.io。 et.al.|[2404.18928](http://arxiv.org/abs/2404.18928)|null|
|**2024-04-29**|**TheaterGen: Character Management with LLM for Consistent Multi-turn Image Generation**|扩散模型的最新进展可以从文本中生成高质量和令人惊叹的图像。然而，在现实世界场景中需求很高的多回合图像生成，在保持图像和文本之间的语义一致性以及同一主题在多个交互回合中的上下文一致性方面仍然面临挑战。为了解决这个问题，我们介绍了TheaterGen，这是一个无训练的框架，它集成了大型语言模型（LLM）和文本到图像（T2I）模型，以提供多回合图像生成的能力。在这个框架内，LLM作为“编剧”，参与多回合互动，生成和管理一本标准化的提示书，其中包括目标图像中每个角色的提示和布局设计。在此基础上，Theatergen生成一个角色图像列表，并提取指导信息，类似于“排练”。随后，通过将提示书和指导信息纳入T2I扩散模型的反向去噪过程，Theatergen生成最终图像，从而进行“最终性能”。通过对提示书和人物图像的有效管理，TheaterGen显著提高了合成图像的语义和上下文一致性。此外，我们还引入了一个专用的基准，CMIGBench（一致多转图像生成基准），其中包含8000条多转指令。与以前的多回合基准测试不同，CMIGBench没有预先定义字符。CMIGBench包含了故事生成和多回合编辑的任务，用于综合评估。大量实验结果表明，TheaterGen显著优于最先进的方法。它将尖端Mini-DALE 3模型的性能标准提高了21%的平均字符-字符相似度和19%的平均文本-图像相似度。 et.al.|[2404.18919](http://arxiv.org/abs/2404.18919)|null|
|**2024-04-29**|**Learning general Gaussian mixtures with efficient score matching**|我们研究了 $k$Gaussians在$d$维度上的混合学习问题。我们对潜在的混合分量不做分离假设：我们只要求协方差矩阵具有有界条件数，并且均值和协方差位于有界半径的球中。我们给出了一种算法，该算法从目标混合物中提取$d^｛\mathrm｛poly｝（k/\varepsilon）｝$样本，在样本多项式时间内运行，并构造了一个采样器，其输出分布为$\varepsilion$，在总变化中远离未知混合物。先前针对该问题的工作要么（i）在维度$d$中需要指数运行时间，要么（ii）对实例进行了强有力的假设（例如，球面协变或可聚类性），要么（iii）对组件$k$ 的数量具有双指数依赖性。我们的方法与解决这个问题的常用技术不同，比如矩量法。相反，我们利用最近开发的基于扩散模型的约简，从分布学习到称为分数匹配的监督学习任务。我们通过证明一个结构结果给出了后者的算法，该结果表明高斯混合的分数函数可以用分段多项式函数近似，并且有一个有效的算法来找到它。据我们所知，这是扩散模型为无监督学习任务实现最先进理论保证的第一个例子。 et.al.|[2404.18893](http://arxiv.org/abs/2404.18893)|null|
|**2024-04-29**|**A Survey on Diffusion Models for Time Series and Spatio-Temporal Data**|对时间序列数据的研究对于了解一段时间内的趋势和异常情况至关重要，从而能够对各个部门进行预测性洞察。另一方面，时空数据对于分析空间和时间中的现象至关重要，为复杂系统的相互作用提供了动态视角。近年来，扩散模型在时间序列和时空数据挖掘中得到了广泛的应用。它们不仅增强了序列和时间数据的生成和推理能力，而且还扩展到其他下游任务。在这项调查中，我们全面彻底地回顾了扩散模型在时间序列和时空数据中的使用，并按模型类别、任务类型、数据模式和实际应用领域对其进行了分类。详细地，我们将扩散模型分为非条件型和条件型，并分别讨论了时间序列数据和时空数据。无条件模型在无监督的情况下运行，可细分为基于概率和基于分数的模型，用于预测和生成任务，如预测、异常检测、分类和插补。另一方面，条件模型利用额外的信息来提高性能，并类似地划分为预测任务和生成任务。我们的调查广泛涵盖了它们在各个领域的应用，包括医疗保健、推荐、气候、能源、音频和交通，为这些模型如何分析和生成数据提供了基础了解。通过这一结构化概述，我们旨在让研究人员和从业者全面了解时间序列和时空数据分析的扩散模型，旨在通过应对传统挑战和探索扩散模型框架内的创新解决方案来指导未来的创新和应用。 et.al.|[2404.18886](http://arxiv.org/abs/2404.18886)|null|
|**2024-04-29**|**Learning Mixtures of Gaussians Using Diffusion Models**|我们给出了一种新的算法来学习 $k$Gaussians（单位协方差为$\mathbb｛R｝^n$）到TV误差$\varepsilon$的混合，具有准多项式（$O（n^｛\text｛poly-log｝\left（\frac｛n+k｝｛\varepsilion｝\right）｝）$）时间和样本复杂度，在最小权重假设下。与以前的方法不同，大多数方法本质上是代数的，我们的方法是分析的，并依赖于扩散模型的框架。扩散模型是生成建模的现代范式，它通常依赖于沿着将纯噪声分布（在我们的情况下是高斯分布）转换为数据分布的过程学习得分函数（梯度log pdf）。尽管它们在图像生成等任务中表现出色，但很少有端到端的理论保证可以有效地学习非平凡的分布族；我们提供了第一批这样的担保。我们通过推导高斯混合的得分函数的高阶高斯噪声灵敏度边界来证明它们可以使用分段多项式回归（高达多对数阶）进行归纳学习，并将其与扩散模型的已知收敛结果相结合。我们的结果推广到高斯的连续混合物，其中混合分布支持在恒定半径的$k$ 球的并集上。特别地，这适用于低维流形上的分布的高斯卷积的情况，或者更一般地，适用于具有小覆盖数的集合。 et.al.|[2404.18869](http://arxiv.org/abs/2404.18869)|null|
|**2024-04-29**|**Construction of local reduced spaces for Friedrichs' systems via randomized training**|这一贡献将传统上用于多尺度问题和具有局部异质系数的参数化偏微分方程（PDE）的局部训练方法扩展到一类线性正对称算子，即Friedrichs算子。考虑具有相应过采样域的局部子域，我们证明了将边界数据映射到内域上的解的传递算子的紧致性。虽然量化能量衰减到内部的Cacciopoli不等式对所有Friedrichs系统都适用，但显示托管解的图空间的紧致性结果是额外必要的。我们讨论了对流-扩散反应问题的混合公式，其中通过Picard-Weck-Weber定理得到了必要的紧致性结果。我们的数值结果集中在具有多个高电导率通道的非均匀扩散场的情况下，证明了所提出方法的有效性。 et.al.|[2404.18839](http://arxiv.org/abs/2404.18839)|null|
|**2024-04-29**|**Towards Extreme Image Compression with Latent Feature Guidance and Diffusion Prior**|由于大量的信息丢失，以极低的比特率（低于每像素0.1比特（bpp））压缩图像是一个重大的挑战。现有的极端图像压缩方法通常遭受严重的压缩伪影或低保真度重建。为了解决这个问题，我们提出了一种新的极限图像压缩框架，该框架以端到端的方式将压缩VAE和预训练的文本到图像扩散模型相结合。具体来说，我们介绍了一种基于压缩VAE的潜在特征引导压缩模块。该模块压缩图像，并最初将压缩的信息解码为内容变量。为了增强内容变量和扩散空间之间的一致性，我们引入了外部引导来调制中间特征图。随后，我们开发了一个条件扩散解码模块，该模块利用预先训练的扩散模型来进一步解码这些内容变量。为了保持预先训练的扩散模型的生成能力，我们保持它们的参数固定，并使用控制模块注入内容信息。我们还设计了空间对准损失，为潜在特征引导的压缩模块提供足够的约束。大量实验表明，在极低的比特率下，我们的方法在视觉性能和图像保真度方面都优于最先进的方法。 et.al.|[2404.18820](http://arxiv.org/abs/2404.18820)|null|
|**2024-04-29**|**Spectral measures and iterative bounds for effective diffusivity of steady and space-time periodic flows**|三十多年前，稳定流体速度场的平流-扩散方程被均匀化，导致有效扩散率的Stieltjes积分表示，该表示是根据紧致自伴随算子的谱测度和流体流的P’clet数给出的。这一结果最近被推广到时空周期流，而不是涉及无界自伴随算子。根据谱测度的矩，Pad近似为Stieltjes函数提供了严格的上界和下界。然而，由于缺乏计算一般流体速度场的谱测度矩的方法，这种强大的数学框架用于计算有效扩散率边界的效用尚未完全实现。在这里，我们通过提供一种迭代方法显著扩展了该框架的适用性，该方法能够以闭合形式对空间和时空周期流分析计算任意数量的矩，从而计算边界。该方法被证明适用于两个空间维度的周期性流动。稳定流的有效扩散率的已知渐近行为通过高阶上界和下界准确地捕捉到，证明了该方法能够为大范围的参数值提供有效扩散系数的准确估计。 et.al.|[2404.18754](http://arxiv.org/abs/2404.18754)|null|
|**2024-04-29**|**Diffuse scattering from dynamically compressed single-crystal zirconium following the pressure-induced $α\toω$ phase transition**|锆中典型的$\alpha\to\omega$相变是我们理解极端负载条件下多态性的理想试验台。经过半个世纪的研究，人们一致认为，这种转变是通过两种不同的驱动机制之一实现的，这取决于压缩路径的性质。然而，最近几年进行的配有原位衍射诊断的动态压缩实验揭示了新的转变机制，这表明我们对潜在原子动力学和转变动力学的理解实际上还远远不够完整。我们使用机器学习类势对沿[0001]轴压缩的单晶锆冲击中的$\alpha\to\omega$相变进行了经典分子动力学模拟。据预测，该转变主要通过两阶段Usikov-Zilberstein机制的修改版本进行，通过该机制，高压$\omega$-相在中间$\beta$-相的晶粒之间的边界处非均匀成核。我们进一步观察到原子无序在$\beta$晶粒之间的连接处加剧，导致$\omega$晶粒之间形成高度缺陷的间隙材料。我们直接将模拟产生的合成x射线衍射图与最近动态压缩实验中使用飞秒衍射获得的衍射图进行了比较，并表明模拟产生了与以前从元素金属中看到的相同的独特、各向异性的漫散射信号。我们的模拟表明，散射信号源于热散射、残余动力学稳定的$\alpha$和$\beta$ 晶粒的纳米粒子状散射以及间隙缺陷结构的散射的组合。 et.al.|[2404.18740](http://arxiv.org/abs/2404.18740)|null|
|**2024-04-29**|**Diffusion coefficient matrix for multiple conserved charges: a Kubo approach**|相对论重离子碰撞中产生的强相互作用物质具有几个守恒的量子数，如重子数、奇异度和电荷。这些电荷的扩散过程可以用描述各种电荷扩散相互影响的扩散矩阵来表征。我们导出了将扩散系数作为扩散矩阵元素来评估的Kubo关系。我们进一步证明，在弱耦合极限下，通过Kubo关系获得的扩散矩阵元素在适当识别弛豫时间的情况下，可以简化为动力学理论中获得的元素。我们在具有两个守恒电荷的两个相互作用标量场的玩具模型中说明了这一评估。 et.al.|[2404.18718](http://arxiv.org/abs/2404.18718)|null|

<p align=right>(<a href=#updated-on-20240430>back to top</a>)</p>

## NeRF

|Publish Date|Title|Abstract|PDF|Code|
|---|---|---|---|---|
|**2024-04-29**|**Object Registration in Neural Fields**|神经场以一种对机器人应用具有巨大前景的方式提供3D几何结构和外观的连续场景表示。解锁机器人中神经领域独特用例的一个功能是对象6-DoF注册。在本文中，我们对最近的Reg-NF神经场配准方法及其在机器人环境中的用例进行了扩展分析。我们展示了使用场景和对象神经场模型确定场景中已知对象的6-DoF姿态的场景。我们展示了如何使用它来更好地表示未完全建模的场景中的对象，并通过将对象神经场模型替换到场景中来生成新的场景。 et.al.|[2404.18381](http://arxiv.org/abs/2404.18381)|null|
|**2024-04-26**|**ArtNeRF: A Stylized Neural Field for 3D-Aware Cartoonized Face Synthesis**|生成视觉模型和神经辐射领域的最新进展极大地促进了3D感知图像合成和风格化任务。然而，以前基于NeRF的工作仅限于单场景风格化，训练模型生成具有任意风格的3D感知卡通人脸仍然没有解决。为了解决这个问题，我们提出了ArtNeRF，这是一种从3D感知GAN中派生出来的新颖的人脸风格化框架。在这个框架中，我们利用表达生成器来合成风格化的人脸，并利用三分支鉴别器模块来提高生成人脸的视觉质量和风格一致性。具体而言，利用基于对比学习的风格编码器来提取风格图像的鲁棒低维嵌入，使生成器能够获得各种风格的知识。为了平滑跨领域迁移学习的训练过程，我们提出了一个自适应风格混合模块，该模块有助于注入风格信息，并允许用户自由调整风格化水平。我们进一步引入了一个神经渲染模块，以实现更高分辨率图像的高效实时渲染。大量实验表明，ArtNeRF在生成具有任意风格的高质量3D感知卡通人脸方面是通用的。 et.al.|[2404.13711](http://arxiv.org/abs/2404.13711)|**[link](https://github.com/silence-tang/artnerf)**|
|**2024-04-19**|**BANF: Band-limited Neural Fields for Levels of Detail Reconstruction**|主要由于其隐含性质，神经场缺乏直接的滤波机制，因为离散信号处理的傅立叶分析不直接适用于这些表示。神经场的有效滤波对于实现下游应用程序中的细节处理水平至关重要，并支持在规则网格上对场进行采样的操作（例如，行进立方体）。试图在频域中分解神经场的现有方法要么采用启发式方法，要么需要对神经场架构进行广泛修改。我们展示了通过一个简单的修改，可以获得低通滤波的神经场，进而展示了如何利用这一点来获得整个信号的频率分解。我们通过研究细节水平重建来证明我们的技术的有效性，并展示了如何有效地计算粗糙的表示。 et.al.|[2404.13024](http://arxiv.org/abs/2404.13024)|null|
|**2024-04-15**|**Efficient and accurate neural field reconstruction using resistive memory**|人类通过将稀疏的观测整合到大规模互连的突触和神经元中来构建空间感知，提供了卓越的并行性和效率。在人工智能中复制这一能力在医学成像、AR/VR和嵌入式人工智能中有着广泛的应用，在这些领域，输入数据往往是稀疏的，计算资源有限。然而，传统的数字计算机信号重构方法面临着软硬件两方面的挑战。在软件方面，传统显式信号表示中的存储效率低下会带来困难。硬件障碍包括冯·诺依曼瓶颈，它限制了CPU和存储器之间的数据传输，以及CMOS电路在支持并行处理方面的局限性。我们提出了一种软硬件协同优化的系统方法，用于从稀疏输入重建信号。在软件方面，我们使用神经场通过神经网络隐式地表示信号，并使用低秩分解和结构化修剪对其进行进一步压缩。在硬件方面，我们设计了一个基于电阻存储器的内存计算（CIM）平台，该平台具有高斯编码器（GE）和MLP处理引擎（PE）。GE利用电阻存储器的内在随机性进行有效的输入编码，而PE通过硬件感知量化（HAQ）电路实现精确的权重映射。我们在基于40nm 256Kb电阻存储器的内存内计算宏上展示了该系统的功效，在不影响3D CT稀疏重建、新视图合成和动态场景新视图合成等任务的重建质量的情况下，实现了巨大的能效和并行性改进。这项工作推进了人工智能驱动的信号恢复技术，为未来高效、稳健的医疗人工智能和3D视觉应用铺平了道路。 et.al.|[2404.09613](http://arxiv.org/abs/2404.09613)|null|
|**2024-04-10**|**Ray-driven Spectral CT Reconstruction Based on Neural Base-Material Fields**|在谱CT重建中，基底材料分解涉及求解大规模非线性积分方程组，这在数学上是高度不适定的。本文提出了一种模型，该模型使用神经场表示来参数化对象的衰减系数，从而避免了线积分离散化过程中像素驱动的投影系数矩阵的复杂计算。介绍了一种基于光线驱动神经场的线积分轻量级离散化方法，提高了离散化过程中积分逼近的精度。将基底材料表示为连续的向量值隐函数，以建立基底材料的神经场参数化模型。然后使用深度学习的自动微分框架来求解神经基底材料场的隐式连续函数。该方法不受重建图像空间分辨率的限制，并且网络具有紧凑和规则的特性。实验验证表明，我们的方法在处理光谱CT重建方面表现得非常好。此外，它还满足了生成高分辨率重建图像的要求。 et.al.|[2404.06991](http://arxiv.org/abs/2404.06991)|null|
|**2024-04-12**|**SpikeNVS: Enhancing Novel View Synthesis from Blurry Images via Spike Camera**|使用神经辐射场（NeRF）和三维高斯散射（3DGS）等神经场方法实现清晰的新视图合成（NVS）的最关键因素之一是训练图像的质量。然而，传统的RGB相机容易受到运动模糊的影响。相比之下，像事件和尖峰相机这样的神经形态相机固有地捕捉更全面的时间信息，这可以作为额外的训练数据提供场景的清晰表示。最近的方法已经探索了集成事件摄像机以提高NVS的质量。事件RGB方法有一些局限性，例如高昂的培训成本和无法在后台有效工作。相反，我们的研究引入了一种新的方法，使用尖峰相机来克服这些限制。通过将尖峰流的纹理重建视为基本事实，我们设计了尖峰纹理（TfS）损失。由于尖峰摄像机依赖于时间积分，而不是事件摄像机使用的时间微分，我们提出的TfS损失保持了可管理的训练成本。它同时处理前景对象和背景。我们还提供了用spike RGB相机系统拍摄的真实世界数据集，以促进未来的研究工作。我们使用合成和真实世界的数据集进行了广泛的实验，以证明我们的设计可以增强NeRF和3DGS的新视图合成。代码和数据集将提供给公众访问。 et.al.|[2404.06710](http://arxiv.org/abs/2404.06710)|null|
|**2024-04-03**|**A Coupled Neural Field Model for the Standard Consolidation Theory**|标准巩固理论指出，位于海马体的短期记忆能够巩固新皮层的长期记忆。换言之，新皮层在海马体的短暂支持下慢慢学习长期记忆，海马体会快速学习不稳定的记忆。然而，目前尚不清楚这些学习率和记忆时间尺度差异背后的神经生物学机制是什么。在这里，我们提出了一种新的标准巩固理论的建模方法，重点关注其潜在的神经生物学机制。除了突触可塑性和棘突频率适应外，我们的模型还结合了齿状回的成年神经发生以及新皮层和海马体之间的大小差异，我们将其与距离依赖性突触可塑性联系起来。我们还考虑了相关大脑区域的相互关联的空间结构，将上述神经生物学机制纳入耦合的神经场框架中，其中每个区域由具有区域内和区域间连接的单独神经场表示。据我们所知，这是将神经场应用于这一过程的首次尝试。使用数值模拟和数学分析，我们探索了在外部输入的海马重放和检索线索的相位交替时，模型的短期和长期动力学。该外部输入可被编码为单个神经场中的多凸点吸引器模式形式的记忆模式。在该模型中，由于海马记忆模式的突起之间的距离较小，海马记忆模式在新皮质记忆模式之前首先被编码。因此，在短时间尺度上检索新皮层中的输入模式需要由海马体的记忆模式提供额外的输入。新皮质记忆模式在较长的时间内逐渐巩固，直到它们的恢复不再需要海马体的支持。在较长的时间内，神经发生对海马神经场的扰动会抹去海马模式，导致记忆模式只在新皮层中唤起的最终状态。因此，我们模型的动力学成功地再现了标准固结理论的主要特征。这表明，海马体的神经发生和距离依赖性突触可塑性，再加上突触抑制和尖峰频率适应，确实是记忆巩固的关键神经生物学过程。 et.al.|[2404.02938](http://arxiv.org/abs/2404.02938)|null|
|**2024-04-03**|**LiDAR4D: Dynamic Neural Fields for Novel Space-time View LiDAR Synthesis**|尽管神经辐射场（NeRFs）在图像新视图合成（NVS）方面取得了成功，但激光雷达NVS在很大程度上仍未被探索。以前的激光雷达NVS方法采用了图像NVS方法的简单转变，同时忽略了激光雷达点云的动态特性和大规模重建问题。有鉴于此，我们提出了LiDAR4D，这是一种用于新的时空LiDAR视图合成的仅限LiDAR的可微分框架。考虑到稀疏性和大规模特征，我们设计了一种结合多平面和网格特征的4D混合表示，以实现从粗到细的有效重建。此外，我们引入了从点云导出的几何约束，以提高时间一致性。对于激光雷达点云的真实合成，我们结合了光线下降概率的全局优化，以保持跨区域模式。在KITTI-360和NuScenes数据集上进行的大量实验证明了我们的方法在实现几何感知和时间一致的动态重建方面的优越性。代码可在https://github.com/ispc-lab/LiDAR4D. et.al.|[2404.02742](http://arxiv.org/abs/2404.02742)|**[link](https://github.com/ispc-lab/lidar4d)**|
|**2024-04-04**|**Vestibular schwannoma growth prediction from longitudinal MRI by time conditioned neural fields**|前庭神经鞘瘤（VS）是一种良性肿瘤，通常通过MRI检查进行积极监测来治疗。为了进一步帮助临床决策并避免过度治疗，基于纵向成像的肿瘤生长的准确预测是非常可取的。在本文中，我们介绍了DeepGrowth，这是一种深度学习方法，它结合了神经场和递归神经网络，用于前瞻性肿瘤生长预测。在所提出的方法中，每个肿瘤都表示为以低维潜在码为条件的有符号距离函数（SDF）。与之前直接在图像空间中进行肿瘤形状预测的研究不同，我们预测潜在代码，然后从中重建未来的形状。为了处理不规则的时间间隔，我们引入了一个基于ConvLSTM的时间条件递归模块和一种新的时间编码策略，使所提出的模型能够输出随时间变化的肿瘤形状。在内部纵向VS数据集上的实验表明，所提出的模型显著提高了性能（ $\ge 1.6\%%$Dice评分和$\ge0.20$mm95\%Hausdorff距离），特别是对于生长或缩小最多的前20%肿瘤（$\ge4.6\%%$Dice评分和$\ge 0.73$ mm95\%Hausdoff距离）。我们的代码可在~\bull获得{https://github.com/cyjdswx/DeepGrowth} et.al.|[2404.02614](http://arxiv.org/abs/2404.02614)|**[link](https://github.com/cyjdswx/deepgrowth)**|
|**2024-04-02**|**NeRFCodec: Neural Feature Compression Meets Neural Radiance Fields for Memory-Efficient Scene Representation**|神经辐射场（NeRF）的出现极大地影响了三维场景建模和新颖的视图合成。作为一种用于三维场景表示的视觉媒体，具有高率失真性能的压缩是一个永恒的目标。受神经压缩和神经场表示进步的启发，我们提出了NeRFCodec，这是一种端到端的NeRF压缩框架，它集成了非线性变换、量化和熵编码，用于高效记忆的场景表示。由于直接在大规模的NeRF特征平面上训练非线性变换是不切实际的，我们发现，当添加内容特定参数时，可以使用预先训练的神经2D图像编解码器来压缩特征。具体来说，我们重用神经2D图像编解码器，但修改其编码器和解码器头，同时保持预训练解码器的其他部分冻结。这使我们能够通过监督渲染损失和熵损失来训练整个管道，通过更新特定于内容的参数来实现率失真平衡。在测试时，包含潜在代码、特征解码器头和其他辅助信息的比特流被发送用于通信。实验结果表明，我们的方法优于现有的NeRF压缩方法，能够在0.5MB的内存预算下实现高质量的新视图合成。 et.al.|[2404.02185](http://arxiv.org/abs/2404.02185)|null|

<p align=right>(<a href=#updated-on-20240430>back to top</a>)</p>

[contributors-shield]: https://img.shields.io/github/contributors/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[contributors-url]: https://github.com/Vincentqyw/cv-arxiv-daily/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[forks-url]: https://github.com/Vincentqyw/cv-arxiv-daily/network/members
[stars-shield]: https://img.shields.io/github/stars/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[stars-url]: https://github.com/Vincentqyw/cv-arxiv-daily/stargazers
[issues-shield]: https://img.shields.io/github/issues/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[issues-url]: https://github.com/Vincentqyw/cv-arxiv-daily/issues

