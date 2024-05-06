[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]

## Updated on 2024.05.06
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
|**2024-05-01**|**DiL-NeRF: Delving into Lidar for Neural Radiance Field on Street Scenes**|逼真度模拟在自动驾驶等应用中发挥着至关重要的作用，神经辐射场（NeRF）的进步可以通过自动创建数字3D资产实现更好的可扩展性。然而，由于在较高速度下相机运动基本共线和采样稀疏，街道场景的重建质量受到影响。另一方面，应用程序通常要求从偏离输入的摄影机视图进行渲染，以准确模拟车道变更等行为。在本文中，我们提出了一些见解，可以更好地利用激光雷达数据来提高街景的NeRF质量。首先，我们的框架从激光雷达中学习几何场景表示，该表示与基于隐式网格的表示融合用于辐射解码，从而提供由显式点云提供的更强的几何信息。其次，我们提出了一种鲁棒的遮挡感知深度监督方案，该方案允许通过累积来利用密集的激光雷达点。第三，我们从激光雷达点生成增强训练视图，以便进一步改进。我们的见解转化为在真实驾驶场景下大大改进的新颖视图合成。 et.al.|[2405.00900](http://arxiv.org/abs/2405.00900)|null|
|**2024-05-01**|**RTG-SLAM: Real-time 3D Reconstruction at Scale using Gaussian Splatting**|我们提出了实时高斯SLAM（RTG-SLAM），这是一个使用RGBD相机的实时三维重建系统，用于使用高斯飞溅的大规模环境。该系统具有紧凑的高斯表示和高效的动态高斯优化方案。我们强制每个高斯要么不透明，要么几乎透明，不透明的适合表面和主色，透明的适合残余色。通过以不同于彩色渲染的方式渲染深度，我们让单个不透明高斯很好地拟合局部表面区域，而不需要多个重叠的高斯，从而大大降低了内存和计算成本。对于动态高斯优化，我们明确地为每帧三种类型的像素添加高斯：新观察到的、具有大颜色误差的和具有大深度误差的。我们还将所有高斯分为稳定高斯和不稳定高斯，其中稳定高斯有望很好地拟合先前观察到的RGBD图像，否则不稳定。我们只优化不稳定的高斯，只渲染不稳定高斯占用的像素。这样，要优化的高斯数和要渲染的像素都大大减少，并且可以实时进行优化。我们展示了各种大型场景的实时重建。与最先进的基于NeRF的RGBD SLAM相比，我们的系统实现了相当高质量的重建，但速度约为其两倍，内存成本约为其一半，并在新视图合成的真实性和相机跟踪精度方面表现出卓越的性能。 et.al.|[2404.19706](http://arxiv.org/abs/2404.19706)|null|
|**2024-04-29**|**SAGS: Structure-Aware 3D Gaussian Splatting**|随着NeRFs的出现，3D高斯散射（3D-GS）为实时神经渲染铺平了道路，克服了体积方法的计算负担。继3D-GS的开创性工作之后，有几种方法试图实现可压缩和高保真度性能的替代方案。然而，通过采用几何不可知的优化方案，这些方法忽略了场景的固有3D结构，从而限制了表示的表现力和质量，导致了各种浮点和伪影。在这项工作中，我们提出了一种结构感知的高斯飞溅方法（SAGS），该方法隐式地对场景的几何结构进行编码，这反映了最先进的渲染性能，并降低了基准新视图合成数据集的存储要求。SAGS建立在局部全局图表示的基础上，有助于复杂场景的学习，并强制执行有意义的点位移，以保持场景的几何结构。此外，我们还介绍了一种轻量级的SAGS，使用了一种简单而有效的中点插值方案，该方案展示了场景的紧凑表示，在不依赖任何压缩策略的情况下，大小减少了24 $\times$ 。在多个基准数据集上进行的大量实验表明，在渲染质量和模型大小方面，与最先进的3D-GS方法相比，SAGS具有优越性。此外，我们证明了我们的结构感知方法可以有效地减轻先前方法的浮动伪影和不规则失真，同时获得精确的深度图。项目页面https://eververas.github.io/SAGS/. et.al.|[2404.19149](http://arxiv.org/abs/2404.19149)|null|
|**2024-04-29**|**Simple-RF: Regularizing Sparse Input Radiance Fields with Simpler Solutions**|神经辐射场（NeRF）在场景的照片逼真的自由视图渲染中表现出令人印象深刻的性能。最近对NeRF的改进，如TensoRF和ZipNeRF，与使用隐式表示的NeRF相比，使用显式模型进行更快的优化和渲染。然而，隐式和显式辐射场都需要对给定场景中的图像进行密集采样。当只有一组稀疏的视图可用时，它们的性能会显著下降。研究人员发现，监督辐射场估计的深度有助于以更少的视角有效训练辐射场。深度监督是使用经典方法或在大型数据集上预先训练的神经网络来获得的。前者可能只提供稀疏的监督，而后者可能存在泛化问题。与早期的方法不同，我们试图通过设计增强模型并将其与主辐射场一起训练来学习深度监督。此外，我们的目标是设计一个正则化框架，该框架可以在不同的隐式和显式辐射场中工作。我们观察到，在稀疏输入场景中，这些辐射场模型的某些特征与观察到的图像过度拟合。我们的关键发现是，降低辐射场在位置编码、分解张量分量的数量或哈希表的大小方面的能力，限制了模型学习更简单的解决方案，从而在某些区域估计更好的深度。通过设计基于这种降低的能力的增强模型，我们可以更好地对主辐射场进行深度监督。通过采用上述正则化，我们在包含前向和360 $^\circ$ 场景的流行数据集上使用稀疏输入视图实现了最先进的视图合成性能。 et.al.|[2404.19015](http://arxiv.org/abs/2404.19015)|null|
|**2024-04-29**|**3D Gaussian Splatting with Deferred Reflection**|基于神经和高斯的辐射场方法的出现在新视图合成领域取得了巨大成功。然而，镜面反射仍然是不平凡的，因为众所周知，高频辐射场很难稳定准确地拟合。我们提出了一种延迟着色方法来有效地渲染高斯飞溅的镜面反射。关键的挑战来自环境图反射模型，该模型需要精确的表面法线，同时使用不连续的梯度来限制法线估计。我们利用延迟着色生成的每像素反射梯度来桥接相邻高斯的优化过程，允许几乎正确的法线估计逐渐传播并最终传播到所有反射对象上。我们的方法在合成高质量镜面反射效果方面显著优于最先进的技术和并行工作，证明了合成场景和真实世界场景的峰值信噪比（PSNR）都得到了一致的提高，同时以几乎与香草高斯飞溅相同的帧速率运行。 et.al.|[2404.18454](http://arxiv.org/abs/2404.18454)|null|
|**2024-04-29**|**$ν$-DBA: Neural Implicit Dense Bundle Adjustment Enables Image-Only Driving Scene Reconstruction**|传感器轨迹和3D地图的联合优化是束调整（BA）的一个关键特性，对自动驾驶至关重要。本文提出了$\nu$ -DBA，这是一种使用三维神经隐式曲面进行地图参数化来实现几何密集束平差（DBA）的新框架，该框架使用密集光流预测引导的几何误差来优化地图表面和轨迹姿态。此外，我们通过逐场景自监督对光流模型进行微调，以进一步提高密集映射的质量。我们在多个驾驶场景数据集上的实验结果表明，我们的方法实现了卓越的轨迹优化和密集的重建精度。我们还研究了光度误差和不同的神经几何先验对表面重建和新视图合成性能的影响。我们的方法是朝着在密集束调整中利用神经隐式表示实现更准确的轨迹和详细的环境映射迈出的重要一步。 et.al.|[2404.18439](http://arxiv.org/abs/2404.18439)|null|
|**2024-04-25**|**Depth Supervised Neural Surface Reconstruction from Airborne Imagery**|虽然最初是为新颖的视图合成而开发的，但神经辐射场（NeRF）最近已成为多视图立体（MVS）的替代品。在一系列研究活动的触发下，已经获得了有希望的结果，尤其是在无纹理、透明和反射表面方面，而这些场景对传统的基于MVS的方法仍然具有挑战性。然而，这些调查大多集中在近距离场景上，对空中场景的研究仍然缺失。对于这项任务，NeRF在图像冗余度低和数据证据薄弱的区域面临潜在的困难，如经常在街道峡谷、立面或建筑阴影中发现的那样。此外，训练这样的网络在计算上是昂贵的。因此，我们工作的目的有两个：首先，我们研究NeRFs对代表不同特征的航空图像块的适用性，如仅最低点、倾斜和高分辨率图像。其次，在这些调查过程中，我们证明了从联络点测量中积分深度先验的好处，这些测量是在预先假设的束块调整过程中提供的。我们的工作基于最先进的框架VolSDF，该框架通过符号距离函数（SDF）对3D场景进行建模，因为与普通NeRF中的标准体积表示相比，这更适用于表面重建。为了进行评估，将基于NeRF的重建与航空图像的公开基准数据集的结果进行比较。 et.al.|[2404.16429](http://arxiv.org/abs/2404.16429)|null|
|**2024-04-25**|**DIG3D: Marrying Gaussian Splatting with Deformable Transformer for Single Image 3D Reconstruction**|在本文中，我们研究了从单视图RGB图像进行三维重建的问题，并提出了一种新的方法，称为DIG3D，用于三维对象重建和新的视图合成。我们的方法利用编码器-解码器框架，该框架在编码器的深度感知图像特征的指导下在解码器中生成3D高斯。特别是，我们介绍了可变形变换器的使用，允许通过3D参考点和多层细化自适应进行高效和有效的解码。通过利用3D高斯的优势，我们的方法为单视图图像的3D重建提供了一个高效而准确的解决方案。我们在ShapeNet SRN数据集上评估了我们的方法，在汽车和椅子数据集中分别获得了24.21和24.98的PSNR。结果优于最近的方法约2.25%，证明了我们的方法在获得优异结果方面的有效性。 et.al.|[2404.16323](http://arxiv.org/abs/2404.16323)|null|
|**2024-04-23**|**FlowMap: High-Quality Camera Poses, Intrinsics, and Depth via Gradient Descent**|本文介绍了FlowMap，这是一种端到端可微的方法，用于解决视频序列的精确相机姿态、相机本质和每帧密集深度。我们的方法对一个简单的最小二乘目标执行每视频梯度下降最小化，该目标将由深度、本质和姿态引起的光流与通过现成的光流和点跟踪获得的对应关系进行比较。除了使用点轨迹来鼓励长期的几何一致性外，我们还引入了适用于一阶优化的深度、本质和姿态的可微重新参数化。我们的经验表明，通过我们的方法恢复的相机参数和密集深度能够使用高斯飞溅在360度轨迹上进行照片逼真的新视图合成。我们的方法不仅远远优于现有的基于梯度下降的束调整方法，而且在360度新视图合成的下游任务上，令人惊讶地与最先进的SfM方法COLMAP不相上下（尽管我们的方法完全基于梯度下降，完全可微，并与传统的SfM完全不同）。 et.al.|[2404.15259](http://arxiv.org/abs/2404.15259)|**[link](https://github.com/dcharatan/flowmap)**|
|**2024-04-22**|**CrossScore: Towards Multi-View Image Evaluation and Scoring**|我们引入了一种新的交叉参考图像质量评估方法，该方法有效地填补了图像评估领域的空白，补充了一系列已建立的评估方案——从SSIM等全参考指标、NIQE等无参考指标到FID等通用参考指标，以及CLIPScore等多模式参考指标。利用具有交叉注意力机制的神经网络和NVS优化的独特数据收集管道，我们的方法能够在不需要地面实况参考的情况下进行准确的图像质量评估。通过将查询图像与同一场景的多个视图进行比较，我们的方法解决了新视图合成（NVS）和无法获得直接参考图像的类似任务中现有度量的局限性。实验结果表明，我们的方法与全参考度量SSIM密切相关，而不需要地面实况参考。 et.al.|[2404.14409](http://arxiv.org/abs/2404.14409)|null|

<p align=right>(<a href=#updated-on-20240506>back to top</a>)</p>

## 3D Reconstruction

|Publish Date|Title|Abstract|PDF|Code|
|---|---|---|---|---|
|**2024-05-02**|**HandSSCA: 3D Hand Mesh Reconstruction with State Space Channel Attention from RGB images**|从单个RGB图像重建手网格是一项具有挑战性的任务，因为手经常被物体遮挡。以前的大多数工作都试图引入更多的附加信息并采用注意力机制来改善3D重建结果，但这会增加计算复杂性。这一观察结果促使我们提出一种新的简洁架构，同时提高计算效率。在这项工作中，我们提出了一种简单有效的三维手部网格重建网络HandSSCA，它是第一个将状态空间建模纳入手部姿态估计领域的网络。在网络中，我们设计了一个新的状态空间通道注意力模块，该模块扩展了有效的感觉场，提取了空间维度上的手部特征，并增强了通道维度上的手部区域特征。这种设计有助于重建完整而详细的手部网格。在具有挑战性手对象遮挡的知名数据集（如FREIHAND、DEXYCB和HO3D）上进行的大量实验表明，我们提出的HandSSCA在保持最小参数计数的同时实现了最先进的性能。 et.al.|[2405.01066](http://arxiv.org/abs/2405.01066)|null|
|**2024-05-01**|**Coherent 3D Portrait Video Reconstruction via Triplane Fusion**|最近在单图像3D肖像重建方面的突破使远程呈现系统能够实时流式传输来自单个相机的3D肖像视频，从而有可能使远程呈现民主化。然而，每帧3D重建表现出时间上的不一致性并且忘记了用户的外观。另一方面，自再现方法可以通过驱动个性化的3D先验来渲染连贯的3D肖像，但不能忠实地重建用户的每帧外观（例如，面部表情和照明）。在这项工作中，我们认识到需要保持连贯的身份和动态的每帧外观，以实现最佳的真实感。为此，我们提出了一种新的基于融合的方法，该方法将个性化的3D主题先验与每帧信息融合，生成时间稳定的3D视频，并忠实地重建用户的每帧外观。我们的基于编码器的方法仅使用由表达条件的3D GAN产生的合成数据进行训练，在工作室和野外数据集上实现了最先进的3D重建精度和时间一致性。 et.al.|[2405.00794](http://arxiv.org/abs/2405.00794)|null|
|**2024-05-01**|**Depth Priors in Removal Neural Radiance Fields**|神经辐射场（NeRF）在三维重建和生成新视图方面显示出令人印象深刻的结果。NeRF的一个关键挑战是重建场景的编辑，如对象移除，这需要在多个视图之间保持一致性，并确保高质量的合成视角。先前的研究结合了深度先验，通常来自激光雷达或COLMAP提供的稀疏深度测量，以提高NeRF中的目标去除性能。然而，这些方法要么昂贵，要么耗时。在本文中，我们提出了一种新的方法，将单目深度估计与基于NeRF的对象去除模型相结合，以显著减少时间消耗，提高场景生成和对象去除的鲁棒性和质量。我们在KITTI数据集上对COLMAP的密集深度重建进行了全面评估，以验证其在深度图生成中的准确性。我们的研究结果表明，COLMAP可以作为地面实况深度图的有效替代方案，在这种情况下，这些信息缺失或获取成本高昂。此外，我们将各种单目深度估计方法集成到去除NeRF模型中，即SpinNeRF，以评估其提高物体去除性能的能力。我们的实验结果突出了单目深度估计在显著改善NeRF应用方面的潜力。 et.al.|[2405.00630](http://arxiv.org/abs/2405.00630)|null|
|**2024-05-01**|**NC-SDF: Enhancing Indoor Scene Reconstruction Using Neural SDFs with View-Dependent Normal Compensation**|通过将单目几何先验作为额外的监督，最先进的神经隐式表面表示在室内场景重建中取得了令人印象深刻的结果。然而，我们已经观察到，这种先验之间的多视图不一致对高质量重建构成了挑战。作为回应，我们提出了NC-SDF，一种具有视图相关法线补偿（NC）的神经符号距离场（SDF）三维重建框架。具体来说，我们将单目正常先验中的视图相关偏差集成到场景的神经隐式表示中。通过自适应地学习和纠正偏差，我们的NC-SDF有效地减轻了不一致监督的不利影响，增强了重建中的全局一致性和局部细节。为了进一步细化细节，我们引入了一种信息像素采样策略，以更多地关注信息含量更高的复杂几何体。此外，我们设计了一种混合几何建模方法来改进神经隐式表示。在合成和真实世界数据集上的实验表明，NC-SDF在重建质量方面优于现有方法。 et.al.|[2405.00340](http://arxiv.org/abs/2405.00340)|null|
|**2024-04-30**|**Lightplane: Highly-Scalable Components for Neural 3D Fields**|当代3D研究，特别是在重建和生成方面，严重依赖2D图像进行输入或监督。然而，这些2D-3D映射的当前设计是内存密集型的，对现有方法构成了显著的瓶颈，并阻碍了新的应用。作为回应，我们为3D神经场提出了一对高度可扩展的组件：Lightplane Render和Splatter，这显著减少了2D-3D映射中的内存使用。这些创新能够以较小的内存和计算成本处理更多、更高分辨率的图像。我们展示了它们在各种应用中的实用性，从有利于图像级损失的单场景优化到实现用于大幅缩放3D重建和生成的多功能管道。代码：\url{https://github.com/facebookresearch/lightplane}. et.al.|[2404.19760](http://arxiv.org/abs/2404.19760)|**[link](https://github.com/facebookresearch/lightplane)**|
|**2024-05-01**|**RTG-SLAM: Real-time 3D Reconstruction at Scale using Gaussian Splatting**|我们提出了实时高斯SLAM（RTG-SLAM），这是一个使用RGBD相机的实时三维重建系统，用于使用高斯飞溅的大规模环境。该系统具有紧凑的高斯表示和高效的动态高斯优化方案。我们强制每个高斯要么不透明，要么几乎透明，不透明的适合表面和主色，透明的适合残余色。通过以不同于彩色渲染的方式渲染深度，我们让单个不透明高斯很好地拟合局部表面区域，而不需要多个重叠的高斯，从而大大降低了内存和计算成本。对于动态高斯优化，我们明确地为每帧三种类型的像素添加高斯：新观察到的、具有大颜色误差的和具有大深度误差的。我们还将所有高斯分为稳定高斯和不稳定高斯，其中稳定高斯有望很好地拟合先前观察到的RGBD图像，否则不稳定。我们只优化不稳定的高斯，只渲染不稳定高斯占用的像素。这样，要优化的高斯数和要渲染的像素都大大减少，并且可以实时进行优化。我们展示了各种大型场景的实时重建。与最先进的基于NeRF的RGBD SLAM相比，我们的系统实现了相当高质量的重建，但速度约为其两倍，内存成本约为其一半，并在新视图合成的真实性和相机跟踪精度方面表现出卓越的性能。 et.al.|[2404.19706](http://arxiv.org/abs/2404.19706)|null|
|**2024-04-30**|**MicroDreamer: Zero-shot 3D Generation in $\sim$ 20 Seconds by Score-based Iterative Reconstruction**|基于优化的方法，如分数蒸馏采样（SDS），在零样本3D生成中显示出前景，但效率较低，主要是由于每个样本需要大量的功能评估（NFE）。在本文中，我们介绍了基于分数的迭代重建（SIR），这是一种使用基于多视图分数的扩散模型进行三维生成的高效通用算法。给定由扩散模型产生的图像，SIR通过重复优化3D参数来减少NFE，不像SDS中的单个优化那样，模拟3D重建过程。通过包括像素空间优化在内的其他改进，我们提出了一种称为MicroDreamer的高效方法，该方法通常适用于各种3D表示和3D生成任务。特别是，在保持类似性能的情况下，MicroDreamer在生成神经辐射场方面比SDS快5-20倍，并且在单个A100 GPU上从3D高斯分裂生成网格需要大约20秒，将最快的零样本基线DreamGaussian的时间减半。我们的代码可在https://github.com/ML-GSAI/MicroDreamer. et.al.|[2404.19525](http://arxiv.org/abs/2404.19525)|**[link](https://github.com/ml-gsai/microdreamer)**|
|**2024-04-30**|**PEVA-Net: Prompt-Enhanced View Aggregation Network for Zero/Few-Shot Multi-View 3D Shape Recognition**|大型视觉语言模型显著提高了零/少镜头场景下二维视觉识别的性能。在本文中，我们专注于利用大视觉语言模型，即CLIP，来解决基于多视图表示的零/少镜头3D形状识别问题。这两项任务的关键挑战是在没有明确训练（零样本3D形状识别）或使用有限数量的数据进行训练（很少拍摄3D形状辨识）的情况下，生成由多个视图图像表示的3D形状的判别描述符。我们分析这两项任务是相关的，可以同时考虑。具体而言，利用对零样本推理有效的描述符来指导在少热点训练下对聚合描述符的调整，可以显著提高少热点学习效率。因此，我们提出了即时增强视图聚合网络（PEVA-Net）来同时解决零/少镜头3D形状识别问题。在零样本场景下，我们建议利用从候选类别建立的提示来增强多个与视图相关的视觉特征的聚合过程。所得到的聚合特征用于3D形状的有效零样本识别。在少镜头场景下，我们首先利用转换器编码器将视图相关的视觉特征聚合到全局描述符中。为了与主要分类损失一起调整编码器，我们提出了一种通过特征提取损失的自判别方案，将零样本描述符作为少热点描述符的引导信号。该方案可以显著提高少镜头学习的效果。 et.al.|[2404.19168](http://arxiv.org/abs/2404.19168)|null|
|**2024-04-29**|**Bootstrap 3D Reconstructed Scenes from 3D Gaussian Splatting**|神经渲染技术的最新发展极大地增强了学术和商业领域中照片逼真3D场景的渲染。最新的方法被称为3D高斯飞溅（3D-GS），为渲染质量和速度设定了新的基准。然而，3D-GS的局限性在合成新的视点时变得明显，尤其是对于与训练中看到的视点大相径庭的视点。此外，放大或缩小时还会出现诸如膨胀和混叠之类的问题。这些挑战都可以追溯到一个根本问题：采样不足。在我们的论文中，我们提出了一种显著解决这个问题的自举方法。这种方法使用扩散模型来增强使用经过训练的3D-GS的新视图的渲染，从而简化训练过程。我们的结果表明，自举有效地减少了工件，并明显增强了评估指标。此外，我们证明了我们的方法是通用的，可以很容易地集成，使各种3D重建项目从我们的方法中受益。 et.al.|[2404.18669](http://arxiv.org/abs/2404.18669)|null|
|**2024-04-29**|**Reconstructing Satellites in 3D from Amateur Telescope Images**|本文提出了一个利用小型业余望远镜拍摄的视频对近地轨道卫星进行三维重建的框架。从这些望远镜获得的视频数据与标准3D重建任务的数据有很大不同，其特征是强烈的运动模糊、大气湍流、普遍的背景光污染、焦距延长和观测视角受限。为了应对这些挑战，我们的方法从全面的预处理工作流程开始，该工作流程包括基于深度学习的图像恢复、特征点提取和相机姿态初始化。我们继续应用改进的3D高斯飞溅算法来重建3D模型。我们的技术支持同时进行3D高斯训练和姿态估计，从而能够从稀疏、嘈杂的数据中稳健地生成复杂的3D点云。编辑后阶段进一步支持了这一过程，该阶段旨在消除与我们先前对卫星几何约束的了解不一致的噪声点。我们使用合成数据集和中国空间站的实际观测结果验证了我们的方法，展示了其在从地面观测重建三维空间物体方面优于现有方法的显著优势。 et.al.|[2404.18394](http://arxiv.org/abs/2404.18394)|null|

<p align=right>(<a href=#updated-on-20240506>back to top</a>)</p>

## Diffusion

|Publish Date|Title|Abstract|PDF|Code|
|---|---|---|---|---|
|**2024-05-02**|**Customizing Text-to-Image Models with a Single Image Pair**|艺术重新诠释是指创造参考作品的变体，使成对的艺术品呈现出独特的艺术风格。我们询问这样的图像对是否可以用于定制生成模型，以捕捉所展示的风格差异。我们提出了成对定制，这是一种新的定制方法，从单个图像对中学习风格差异，然后将获得的风格应用于生成过程。与现有的从一组图像中学习模仿单个概念的方法不同，我们的方法捕捉到了成对图像之间的风格差异。这使我们能够在不过度拟合示例中的特定图像内容的情况下应用风格变化。为了解决这一新任务，我们采用了一种联合优化方法，该方法将风格和内容明确地分离到不同的LoRA权重空间中。我们优化这些风格和内容权重，以再现风格和内容图像，同时鼓励它们的正交性。在推理过程中，我们根据学习到的权重，通过一种新的风格指导来修改扩散过程。定性和定量实验都表明，我们的方法可以有效地学习风格，同时避免对图像内容的过度拟合，突出了从单个图像对中建模这种风格差异的潜力。 et.al.|[2405.01536](http://arxiv.org/abs/2405.01536)|null|
|**2024-05-02**|**The heat equation with time-correlated random potential in d=2: Edwards-Wilkinson fluctuations**|我们考虑维度 $d=2$中的随机PDE:$ \partial_tu（t，x）=\frac｛1｝｛2｝\Delta u（t、x）+｛\beta｝｛。我们证明，在重整化后，解的波动收敛到Edwards-Wilkinson极限，具有显式有效方差和恒定有效扩散率。我们的主要工具是路径空间上的马尔可夫链，我们用它来建立Kallianpur-Robbins定律对特定再生过程的扩展。 et.al.|[2405.01519](http://arxiv.org/abs/2405.01519)|null|
|**2024-05-02**|**Effective Lifshitz black holes, hydrodynamics, and transport coefficients in fluid/gravity correspondence**|在流体/重力膜范式中讨论了具有任意动力学指数的有效Lifshitz黑洞。计算和分析了双Lifshitz场论中的输运和响应系数，包括电荷扩散常数和剪切模式阻尼常数，以及剪切粘度与熵密度的比值。采用Kubo公式，通过Lifshitz黑膜几何中规范矢量波动的全息线性响应，获得了杂质对应规范扇区的直流电导率。 et.al.|[2405.01505](http://arxiv.org/abs/2405.01505)|null|
|**2024-05-02**|**LocInv: Localization-aware Inversion for Text-Guided Image Editing**|大规模文本到图像（T2I）扩散模型展示了基于文本提示的显著生成能力。基于T2I扩散模型，文本引导图像编辑研究旨在使用户能够通过更改文本提示来操作生成的图像。然而，现有的图像编辑技术倾向于对超出预期目标区域的无意区域进行编辑，这主要是由于交叉注意力图中的不准确。为了解决这个问题，我们提出了定位感知反演（LocInv），它利用分割图或边界框作为额外的定位先验，在扩散过程的去噪阶段细化交叉注意力图。通过动态更新文本输入中与名词词相对应的标记，我们迫使交叉注意力图与文本提示中正确的名词和形容词紧密对齐。基于这项技术，我们实现了对特定对象的细粒度图像编辑，同时防止对其他区域进行不希望的更改。我们的方法LocInv基于公开的稳定扩散，在COCO数据集的一个子集上进行了广泛的评估，并在定量和定性方面一致获得了优越的结果。代码将在发布https://github.com/wangkai930418/DPL et.al.|[2405.01496](http://arxiv.org/abs/2405.01496)|**[link](https://github.com/wangkai930418/DPL)**|
|**2024-05-02**|**Navigating Heterogeneity and Privacy in One-Shot Federated Learning with Diffusion Models**|联合学习（FL）使多个客户端能够集体训练模型，同时保护数据隐私。然而，FL在通信成本和数据异构性方面面临挑战。一次性联合学习已经成为一种解决方案，它减少了通信次数，提高了效率，并提供了更好的安全性来抵御窃听攻击。尽管如此，数据异构性仍然是一个重大挑战，影响了性能。这项工作探索了扩散模型在一次性FL中的有效性，证明了它们在解决数据异质性和提高FL性能方面的适用性。此外，我们还研究了在差分隐私（DP）下，与其他一次性FL方法相比，我们的扩散模型方法FedDiff的效用。此外，为了提高DP设置下的生成样本质量，我们提出了一种实用的傅立叶幅度滤波（FMF）方法，提高了生成数据用于全局模型训练的有效性。 et.al.|[2405.01494](http://arxiv.org/abs/2405.01494)|null|
|**2024-05-02**|**StoryDiffusion: Consistent Self-Attention for Long-Range Image and Video Generation**|对于最近基于扩散的生成模型来说，在一系列生成的图像中保持一致的内容，尤其是那些包含主题和复杂细节的图像，是一个重大挑战。在本文中，我们提出了一种新的自注意计算方法，称为一致自注意，该方法显著提高了生成图像之间的一致性，并以零样本的方式增强了普遍的基于预训练扩散的文本到图像模型。为了将我们的方法扩展到远程视频生成，我们进一步引入了一个新的语义空间-时间运动预测模块，称为语义运动预测器。它被训练来估计语义空间中两个所提供的图像之间的运动条件。该模块将生成的图像序列转换为具有平滑过渡和一致主题的视频，这些视频比仅基于潜在空间的模块要稳定得多，尤其是在长视频生成的情况下。通过合并这两个新颖的组件，我们的框架（称为StoryDiffusion）可以描述一个基于文本的故事，其中包含一致的图像或视频，包含丰富的内容。所提出的StoryDiffusion包括通过图像和视频的呈现在视觉故事生成方面进行的开创性探索，我们希望这能从建筑修改方面启发更多的研究。我们的代码公开于https://github.com/HVision-NKU/StoryDiffusion. et.al.|[2405.01434](http://arxiv.org/abs/2405.01434)|**[link](https://github.com/hvision-nku/storydiffusion)**|
|**2024-05-02**|**In-and-Out: Algorithmic Diffusion for Sampling Convex Bodies**|我们提出了一种新的高维凸体均匀采样的随机游动。它实现了最先进的运行时复杂性，对输出的保证比以前已知的更强，即在R\'enyi散度（这意味着TV， $\mathcal{W}_2$，KL，$\chi^2$ ）。该证明偏离了用于该问题的多项式算法的已知方法——我们利用随机扩散视角来显示目标分布的收缩，其收敛速度由平稳密度的函数等周常数确定。 et.al.|[2405.01425](http://arxiv.org/abs/2405.01425)|null|
|**2024-05-02**|**Statistical algorithms for low-frequency diffusion data: A PDE approach**|我们考虑从低频数据在多维扩散模型中进行非参数推理的问题。由于可能性及其梯度的棘手性，这种情况下的统计分析是出了名的具有挑战性，迄今为止，计算方法在很大程度上依赖于昂贵的基于模拟的技术。在这篇文章中，我们提出了一种新的计算方法，该方法受PDE理论的启发，并围绕着将跃迁密度表征为相关热（Fokker-Planck）方程的解而建立。利用抛物型偏微分方程理论的最优正则性结果，我们证明了似然梯度的一个新的刻画。利用这些发展，对于恢复扩散率的非线性逆问题（在发散形式模型中），我们证明了似然性及其梯度的数值评估可以简化为标准椭圆特征值问题，可以通过强大的有限元方法求解。这使得能够有效地实现一大类统计算法，包括（i）用于后验采样的预处理Crank-Nicolson和Langevin型方法，以及（ii）用于计算最大似然和最大后验估计的基于梯度的下降优化方案。我们通过在具有高斯过程先验的非参数贝叶斯模型中进行广泛的模拟研究，展示了这些方法的有效性。有趣的是，尽管存在非线性问题，优化方案提供了令人满意的数值恢复，同时表现出向平稳点的快速收敛；因此，我们的方法可能会显著提高计算速度。可复制代码可在线获取，网址为https://github.com/MattGiord/LF-Diffusion. et.al.|[2405.01372](http://arxiv.org/abs/2405.01372)|null|
|**2024-05-02**|**On Nanowire Morphological Instability and Pinch-Off by Surface Electromigration**|表面扩散和表面电迁移可能导致固体薄膜和纳米线的形态不稳定。本文对受到轴向电流作用的单晶圆柱形纳米线的形态不稳定性进行了两种非线性分析。这些处理扩展了在没有表面电迁移的情况下进行的传统线性稳定性分析，表明了瑞利平台不稳定性。在略高于瑞利平台（长波）不稳定性阈值的情况下进行了弱非线性分析。它产生了一维Sivashinsky振幅方程，该方程描述了有限时间内表面扰动振幅的爆发。这是圆柱体半径的轴对称尖峰奇异性形成的特征，导致导线夹断并分离成不相交的线段。对振幅尖峰奇异性进行了标度分析，并表征了尖峰的时间和电场相关维数。在长波或短波不稳定性阈值以上的任意距离处进行弱非线性多尺度分析。导出并表征了主要不稳定模式的时间和电场相关傅立叶振幅。 et.al.|[2405.01331](http://arxiv.org/abs/2405.01331)|null|
|**2024-05-02**|**DiffusionPipe: Training Large Diffusion Models with Efficient Pipelines**|扩散模型已经成为图像生成的主要执行者。为了支持训练大型扩散模型，本文研究了扩散模型的管道并行训练，并提出了一种同步管道训练系统DiffusionPipe，该系统提倡创新的管道气泡填充技术，以适应扩散模型的结构特征。现有技术的扩散模型通常包括可训练（主干）和不可训练（例如，冻结输入编码器）部分。我们首先用动态规划方法将代表性扩散模型中单个和多个主干的最优阶段划分和管道调度统一起来。然后，我们提出通过高效的贪婪算法将不可训练模型部分的计算填充到骨干的流水线训练的空闲期中，从而实现高训练吞吐量。大量实验表明，在流行的扩散模型上，DiffusionPipe可以实现比管道并行方法高达1.41倍的加速和比数据并行训练高达1.28倍的加速。 et.al.|[2405.01248](http://arxiv.org/abs/2405.01248)|null|

<p align=right>(<a href=#updated-on-20240506>back to top</a>)</p>

## NeRF

|Publish Date|Title|Abstract|PDF|Code|
|---|---|---|---|---|
|**2024-04-30**|**Lightplane: Highly-Scalable Components for Neural 3D Fields**|当代3D研究，特别是在重建和生成方面，严重依赖2D图像进行输入或监督。然而，这些2D-3D映射的当前设计是内存密集型的，对现有方法构成了显著的瓶颈，并阻碍了新的应用。作为回应，我们为3D神经场提出了一对高度可扩展的组件：Lightplane Render和Splatter，这显著减少了2D-3D映射中的内存使用。这些创新能够以较小的内存和计算成本处理更多、更高分辨率的图像。我们展示了它们在各种应用中的实用性，从有利于图像级损失的单场景优化到实现用于大幅缩放3D重建和生成的多功能管道。代码：\url{https://github.com/facebookresearch/lightplane}. et.al.|[2404.19760](http://arxiv.org/abs/2404.19760)|**[link](https://github.com/facebookresearch/lightplane)**|
|**2024-05-03**|**Object Registration in Neural Fields**|神经场以一种对机器人应用具有巨大前景的方式提供3D几何结构和外观的连续场景表示。解锁机器人中神经领域独特用例的一个功能是对象6-DoF注册。在本文中，我们对最近的Reg-NF神经场配准方法及其在机器人环境中的用例进行了扩展分析。我们展示了使用场景和对象神经场模型确定场景中已知对象的6-DoF姿态的场景。我们展示了如何使用它来更好地表示未完全建模的场景中的对象，并通过将对象神经场模型替换到场景中来生成新的场景。 et.al.|[2404.18381](http://arxiv.org/abs/2404.18381)|null|
|**2024-04-26**|**ArtNeRF: A Stylized Neural Field for 3D-Aware Cartoonized Face Synthesis**|生成视觉模型和神经辐射领域的最新进展极大地促进了3D感知图像合成和风格化任务。然而，以前基于NeRF的工作仅限于单场景风格化，训练模型生成具有任意风格的3D感知卡通人脸仍然没有解决。为了解决这个问题，我们提出了ArtNeRF，这是一种从3D感知GAN中派生出来的新颖的人脸风格化框架。在这个框架中，我们利用表达生成器来合成风格化的人脸，并利用三分支鉴别器模块来提高生成人脸的视觉质量和风格一致性。具体而言，利用基于对比学习的风格编码器来提取风格图像的鲁棒低维嵌入，使生成器能够获得各种风格的知识。为了平滑跨领域迁移学习的训练过程，我们提出了一个自适应风格混合模块，该模块有助于注入风格信息，并允许用户自由调整风格化水平。我们进一步引入了一个神经渲染模块，以实现更高分辨率图像的高效实时渲染。大量实验表明，ArtNeRF在生成具有任意风格的高质量3D感知卡通人脸方面是通用的。 et.al.|[2404.13711](http://arxiv.org/abs/2404.13711)|**[link](https://github.com/silence-tang/artnerf)**|
|**2024-04-19**|**BANF: Band-limited Neural Fields for Levels of Detail Reconstruction**|主要由于其隐含性质，神经场缺乏直接的滤波机制，因为离散信号处理的傅立叶分析不直接适用于这些表示。神经场的有效滤波对于实现下游应用程序中的细节处理水平至关重要，并支持在规则网格上对场进行采样的操作（例如，行进立方体）。试图在频域中分解神经场的现有方法要么采用启发式方法，要么需要对神经场架构进行广泛修改。我们展示了通过一个简单的修改，可以获得低通滤波的神经场，进而展示了如何利用这一点来获得整个信号的频率分解。我们通过研究细节水平重建来证明我们的技术的有效性，并展示了如何有效地计算粗糙的表示。 et.al.|[2404.13024](http://arxiv.org/abs/2404.13024)|null|
|**2024-04-15**|**Efficient and accurate neural field reconstruction using resistive memory**|人类通过将稀疏的观测整合到大规模互连的突触和神经元中来构建空间感知，提供了卓越的并行性和效率。在人工智能中复制这一能力在医学成像、AR/VR和嵌入式人工智能中有着广泛的应用，在这些领域，输入数据往往是稀疏的，计算资源有限。然而，传统的数字计算机信号重构方法面临着软硬件两方面的挑战。在软件方面，传统显式信号表示中的存储效率低下会带来困难。硬件障碍包括冯·诺依曼瓶颈，它限制了CPU和存储器之间的数据传输，以及CMOS电路在支持并行处理方面的局限性。我们提出了一种软硬件协同优化的系统方法，用于从稀疏输入重建信号。在软件方面，我们使用神经场通过神经网络隐式地表示信号，并使用低秩分解和结构化修剪对其进行进一步压缩。在硬件方面，我们设计了一个基于电阻存储器的内存计算（CIM）平台，该平台具有高斯编码器（GE）和MLP处理引擎（PE）。GE利用电阻存储器的内在随机性进行有效的输入编码，而PE通过硬件感知量化（HAQ）电路实现精确的权重映射。我们在基于40nm 256Kb电阻存储器的内存内计算宏上展示了该系统的功效，在不影响3D CT稀疏重建、新视图合成和动态场景新视图合成等任务的重建质量的情况下，实现了巨大的能效和并行性改进。这项工作推进了人工智能驱动的信号恢复技术，为未来高效、稳健的医疗人工智能和3D视觉应用铺平了道路。 et.al.|[2404.09613](http://arxiv.org/abs/2404.09613)|null|
|**2024-04-10**|**Ray-driven Spectral CT Reconstruction Based on Neural Base-Material Fields**|在谱CT重建中，基底材料分解涉及求解大规模非线性积分方程组，这在数学上是高度不适定的。本文提出了一种模型，该模型使用神经场表示来参数化对象的衰减系数，从而避免了线积分离散化过程中像素驱动的投影系数矩阵的复杂计算。介绍了一种基于光线驱动神经场的线积分轻量级离散化方法，提高了离散化过程中积分逼近的精度。将基底材料表示为连续的向量值隐函数，以建立基底材料的神经场参数化模型。然后使用深度学习的自动微分框架来求解神经基底材料场的隐式连续函数。该方法不受重建图像空间分辨率的限制，并且网络具有紧凑和规则的特性。实验验证表明，我们的方法在处理光谱CT重建方面表现得非常好。此外，它还满足了生成高分辨率重建图像的要求。 et.al.|[2404.06991](http://arxiv.org/abs/2404.06991)|null|
|**2024-04-12**|**SpikeNVS: Enhancing Novel View Synthesis from Blurry Images via Spike Camera**|使用神经辐射场（NeRF）和三维高斯散射（3DGS）等神经场方法实现清晰的新视图合成（NVS）的最关键因素之一是训练图像的质量。然而，传统的RGB相机容易受到运动模糊的影响。相比之下，像事件和尖峰相机这样的神经形态相机固有地捕捉更全面的时间信息，这可以作为额外的训练数据提供场景的清晰表示。最近的方法已经探索了集成事件摄像机以提高NVS的质量。事件RGB方法有一些局限性，例如高昂的培训成本和无法在后台有效工作。相反，我们的研究引入了一种新的方法，使用尖峰相机来克服这些限制。通过将尖峰流的纹理重建视为基本事实，我们设计了尖峰纹理（TfS）损失。由于尖峰摄像机依赖于时间积分，而不是事件摄像机使用的时间微分，我们提出的TfS损失保持了可管理的训练成本。它同时处理前景对象和背景。我们还提供了用spike RGB相机系统拍摄的真实世界数据集，以促进未来的研究工作。我们使用合成和真实世界的数据集进行了广泛的实验，以证明我们的设计可以增强NeRF和3DGS的新视图合成。代码和数据集将提供给公众访问。 et.al.|[2404.06710](http://arxiv.org/abs/2404.06710)|null|
|**2024-04-03**|**A Coupled Neural Field Model for the Standard Consolidation Theory**|标准巩固理论指出，位于海马体的短期记忆能够巩固新皮层的长期记忆。换言之，新皮层在海马体的短暂支持下慢慢学习长期记忆，海马体会快速学习不稳定的记忆。然而，目前尚不清楚这些学习率和记忆时间尺度差异背后的神经生物学机制是什么。在这里，我们提出了一种新的标准巩固理论的建模方法，重点关注其潜在的神经生物学机制。除了突触可塑性和棘突频率适应外，我们的模型还结合了齿状回的成年神经发生以及新皮层和海马体之间的大小差异，我们将其与距离依赖性突触可塑性联系起来。我们还考虑了相关大脑区域的相互关联的空间结构，将上述神经生物学机制纳入耦合的神经场框架中，其中每个区域由具有区域内和区域间连接的单独神经场表示。据我们所知，这是将神经场应用于这一过程的首次尝试。使用数值模拟和数学分析，我们探索了在外部输入的海马重放和检索线索的相位交替时，模型的短期和长期动力学。该外部输入可被编码为单个神经场中的多凸点吸引器模式形式的记忆模式。在该模型中，由于海马记忆模式的突起之间的距离较小，海马记忆模式在新皮质记忆模式之前首先被编码。因此，在短时间尺度上检索新皮层中的输入模式需要由海马体的记忆模式提供额外的输入。新皮质记忆模式在较长的时间内逐渐巩固，直到它们的恢复不再需要海马体的支持。在较长的时间内，神经发生对海马神经场的扰动会抹去海马模式，导致记忆模式只在新皮层中唤起的最终状态。因此，我们模型的动力学成功地再现了标准固结理论的主要特征。这表明，海马体的神经发生和距离依赖性突触可塑性，再加上突触抑制和尖峰频率适应，确实是记忆巩固的关键神经生物学过程。 et.al.|[2404.02938](http://arxiv.org/abs/2404.02938)|null|
|**2024-04-03**|**LiDAR4D: Dynamic Neural Fields for Novel Space-time View LiDAR Synthesis**|尽管神经辐射场（NeRFs）在图像新视图合成（NVS）方面取得了成功，但激光雷达NVS在很大程度上仍未被探索。以前的激光雷达NVS方法采用了图像NVS方法的简单转变，同时忽略了激光雷达点云的动态特性和大规模重建问题。有鉴于此，我们提出了LiDAR4D，这是一种用于新的时空LiDAR视图合成的仅限LiDAR的可微分框架。考虑到稀疏性和大规模特征，我们设计了一种结合多平面和网格特征的4D混合表示，以实现从粗到细的有效重建。此外，我们引入了从点云导出的几何约束，以提高时间一致性。对于激光雷达点云的真实合成，我们结合了光线下降概率的全局优化，以保持跨区域模式。在KITTI-360和NuScenes数据集上进行的大量实验证明了我们的方法在实现几何感知和时间一致的动态重建方面的优越性。代码可在https://github.com/ispc-lab/LiDAR4D. et.al.|[2404.02742](http://arxiv.org/abs/2404.02742)|**[link](https://github.com/ispc-lab/lidar4d)**|
|**2024-04-04**|**Vestibular schwannoma growth prediction from longitudinal MRI by time conditioned neural fields**|前庭神经鞘瘤（VS）是一种良性肿瘤，通常通过MRI检查进行积极监测来治疗。为了进一步帮助临床决策并避免过度治疗，基于纵向成像的肿瘤生长的准确预测是非常可取的。在本文中，我们介绍了DeepGrowth，这是一种深度学习方法，它结合了神经场和递归神经网络，用于前瞻性肿瘤生长预测。在所提出的方法中，每个肿瘤都表示为以低维潜在码为条件的有符号距离函数（SDF）。与之前直接在图像空间中进行肿瘤形状预测的研究不同，我们预测潜在代码，然后从中重建未来的形状。为了处理不规则的时间间隔，我们引入了一个基于ConvLSTM的时间条件递归模块和一种新的时间编码策略，使所提出的模型能够输出随时间变化的肿瘤形状。在内部纵向VS数据集上的实验表明，所提出的模型显著提高了性能（ $\ge 1.6\%%$Dice评分和$\ge0.20$mm95\%Hausdorff距离），特别是对于生长或缩小最多的前20%肿瘤（$\ge4.6\%%$Dice评分和$\ge 0.73$ mm95\%Hausdoff距离）。我们的代码可在~\bull获得{https://github.com/cyjdswx/DeepGrowth} et.al.|[2404.02614](http://arxiv.org/abs/2404.02614)|**[link](https://github.com/cyjdswx/deepgrowth)**|

<p align=right>(<a href=#updated-on-20240506>back to top</a>)</p>

[contributors-shield]: https://img.shields.io/github/contributors/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[contributors-url]: https://github.com/Vincentqyw/cv-arxiv-daily/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[forks-url]: https://github.com/Vincentqyw/cv-arxiv-daily/network/members
[stars-shield]: https://img.shields.io/github/stars/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[stars-url]: https://github.com/Vincentqyw/cv-arxiv-daily/stargazers
[issues-shield]: https://img.shields.io/github/issues/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[issues-url]: https://github.com/Vincentqyw/cv-arxiv-daily/issues

