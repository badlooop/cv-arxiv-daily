[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]

## Updated on 2024.08.02
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
|**2024-07-31**|**Forecasting Future Videos from Novel Views via Disentangled 3D Scene Representation**|空间和时间视频外推（VEST）使观众能够预测未来的3D场景，并从新颖的视角观看。最近的方法提出学习纠缠表示，旨在将分层场景几何、运动预测和新颖的视图合成建模在一起，同时假设每个场景层都有简化的仿射运动和基于单应性的扭曲，导致视频外推不准确。我们的方法不是纠缠的场景表示和渲染，而是选择通过将2D场景提升到3D点云来将场景几何体与场景运动分离，从而能够从新颖的视角对未来的视频进行高质量的渲染。为了模拟未来的3D场景运动，我们提出了一种解纠缠的两阶段方法，该方法首先预测自我运动，然后预测动态对象（如汽车、人）的残余运动。这种方法通过减少自我运动与动态物体运动纠缠的不准确性来确保更精确的运动预测，更好的自我运动预测可以显著提高视觉效果。对两个城市场景数据集的广泛实验分析表明，与强基线相比，我们提出的方法具有更优的性能。 et.al.|[2407.21450](http://arxiv.org/abs/2407.21450)|null|
|**2024-07-30**|**Dynamic Scene Understanding through Object-Centric Voxelization and Neural Rendering**|从无监督视频中学习以对象为中心的表示是具有挑战性的。与之前大多数专注于分解2D图像的方法不同，我们提出了一个名为DynaVol-S的3D生成模型，用于动态场景，该模型在可微体绘制框架内实现了以对象为中心的学习。其关键思想是执行以对象为中心的体素化，以捕捉场景的3D特性，从而推断单个空间位置的每个对象占用概率。这些体素特征通过规范空间变形函数演变，并在具有组合NeRF的逆渲染管道中进行优化。此外，我们的方法整合了2D语义特征来创建3D语义网格，通过多个解纠缠的体素网格来表示场景。DynaVol-S在动态场景的新颖视图合成和无监督分解任务中都明显优于现有模型。通过联合考虑几何结构和语义特征，它有效地解决了涉及复杂对象交互的具有挑战性的现实世界场景。此外，一旦经过训练，显式有意义的体素特征能够实现2D场景分解方法无法实现的额外功能，例如通过编辑几何形状或操纵对象的运动轨迹来生成新的场景。 et.al.|[2407.20908](http://arxiv.org/abs/2407.20908)|**[link](https://github.com/zyp123494/dynavol)**|
|**2024-07-29**|**Radiance Fields for Robotic Teleoperation**|神经辐射场（NeRFs）或3D高斯散斑（3DGS）等辐射场方法彻底改变了图形和新颖的视图合成。它们能够合成具有照片级真实感的新视点，以及捕捉复杂的体积和镜面场景，使其成为机器人遥操作设置的理想可视化工具。直接摄像机遥操作以牺牲机动性为代价提供高保真度操作，而基于重建的方法提供了保真度较低的可控场景。考虑到这一点，我们建议用在线辐射场取代机器人遥操作管道的传统重建可视化组件，提供具有照片级真实感的高度可操作场景。因此，对现有技术有三个主要贡献：（1）使用来自多个相机的实时数据对辐射场进行在线训练，（2）支持包括NeRF和3DGS在内的各种辐射方法，（3）这些方法的可视化套件，包括虚拟现实场景。为了实现与现有设置的无缝集成，这些组件在多种配置下用多个机器人进行了测试，并使用传统工具和VR耳机进行了显示。将不同方法和机器人的结果与网格重建的基线进行了定量比较，并进行了一项用户研究来比较不同的可视化方法。有关视频和代码，请查看https://leggedrobotics.github.io/rffr.github.io/. et.al.|[2407.20194](http://arxiv.org/abs/2407.20194)|**[link](https://github.com/leggedrobotics/rf_ros)**|
|**2024-07-25**|**Towards the Spectral bias Alleviation by Normalizations in Coordinate Networks**|最近，使用坐标网络表示信号主导了逆问题领域，并广泛应用于各种科学计算任务中。尽管如此，坐标网络中仍存在光谱偏差的问题，限制了学习高频分量的能力。这个问题是由坐标网络的神经切线核（NTK）特征值的病理分布引起的。我们发现，使用经典归一化技术（批归一化和层归一化）可以改善这种病理分布，这些技术通常用于卷积神经网络，但很少用于坐标网络。我们证明，归一化技术大大降低了NTK特征值的最大值和方差，同时略微修改了均值，考虑到最大特征值远大于最大值，这种方差变化导致特征值分布从较低的分布向较高的分布偏移，因此可以减轻谱偏差。此外，我们通过以不同的方式组合这两种技术，提出了两种新的归一化技术。通过将基于归一化的坐标网络应用于各种任务，包括图像压缩、计算机断层扫描重建、形状表示、磁共振成像、新视图合成和多视图立体重建，这些归一化技术的有效性得到了显著改进和最新技术水平的证实。 et.al.|[2407.17834](http://arxiv.org/abs/2407.17834)|**[link](https://github.com/aiolus-x/norm-inr)**|
|**2024-07-24**|**SV4D: Dynamic 3D Content Generation with Multi-Frame and Multi-View Consistency**|我们提出了稳定视频4D（SV4D），这是一种用于多帧和多视图一致动态3D内容生成的潜在视频扩散模型。与之前依赖于单独训练的生成模型进行视频生成和新颖视图合成的方法不同，我们设计了一个统一的扩散模型来生成动态3D对象的新颖视图视频。具体来说，给定单眼参考视频，SV4D为每个视频帧生成时间上一致的新视图。然后，我们使用生成的新颖视图视频来有效地优化隐式4D表示（动态NeRF），而不需要大多数先前工作中使用的繁琐的基于SDS的优化。为了训练我们的统一新颖视图视频生成模型，我们从现有的Objaverse数据集中策划了一个动态3D对象数据集。多个数据集和用户研究的广泛实验结果表明，与先前的工作相比，SV4D在新视图视频合成和4D生成方面具有最先进的性能。 et.al.|[2407.17470](http://arxiv.org/abs/2407.17470)|null|
|**2024-07-24**|**Pose Estimation from Camera Images for Underwater Inspection**|高精度定位是水下复验任务的关键。惯性导航系统、多普勒速度记录仪和声学定位等传统定位方法面临着重大挑战，对于某些应用来说成本效益不高。在这种情况下，视觉定位是一种经济高效的替代方案，利用检查车辆上已经配备的摄像头从周围场景的图像中估计姿态。其中，基于机器学习的图像姿态估计在水下环境中显示出前景，使用基于先前映射场景训练的模型进行高效的重新定位。我们探索了基于学习的姿态估计器在清水和浑浊水检查任务中的有效性，评估了图像格式、模型架构和训练数据多样性的影响。我们通过采用新颖的视图合成模型来生成增强训练数据，从而显著增强了未探索区域的姿态估计。此外，我们通过扩展卡尔曼滤波器将姿态估计器输出与传感器数据相结合，提高了定位精度，证明了轨迹平滑度和精度的提高。 et.al.|[2407.16961](http://arxiv.org/abs/2407.16961)|null|
|**2024-07-29**|**DHGS: Decoupled Hybrid Gaussian Splatting for Driving Scene**|现有的高斯飞溅方法在驾驶场景中往往无法实现令人满意的新颖视图合成，这主要是由于所涉及的元素缺乏巧妙的设计和几何约束。本文介绍了一种新的神经渲染方法，称为解耦混合高斯散点（DHGS），旨在提高静态驾驶场景新型视图合成的渲染质量。这项工作的新颖之处在于，它为道路和非道路层提供了解耦和混合像素级混合器，而不需要为整个场景提供传统的统一可微渲染逻辑，同时通过提出的深度有序混合渲染策略仍然保持一致和连续的叠加。此外，对由符号距离场（SDF）组成的隐式道路表示进行训练，以监控具有微妙几何属性的路面。伴随着辅助透射率损失和一致性损失的使用，最终获得了具有不可察觉边界和高保真度的新图像。在Waymo数据集上进行的大量实验证明，DHGS的性能优于最先进的方法。提供更多视频证据的项目页面是：https://ironbrotherstyle.github.io/dhgs_web. et.al.|[2407.16600](http://arxiv.org/abs/2407.16600)|null|
|**2024-07-23**|**HDRSplat: Gaussian Splatting for High Dynamic Range 3D Scene Reconstruction from Raw Images**|最近出现的3D高斯散斑（3DGS）彻底改变了3D场景重建空间，实现了实时高保真的新颖视图合成。然而，除了RawNeRF之外，所有先前的基于3DGS和NeRF的方法都依赖于8位色调映射的低动态范围（LDR）图像进行场景重建。这种方法难以在需要更高动态范围的场景中实现精确的重建。示例包括在夜间或光线不足的室内空间中拍摄的具有低信噪比的场景，以及阴影区域表现出极端对比度的日光场景。我们提出的方法HDRSplat定制3DGS，在近暗环境中直接在14位线性原始图像上训练，保留了场景的完整动态范围和内容。我们的主要贡献有两个方面：首先，我们提出了一种适合线性HDR空间损耗的方法，可以同时从嘈杂的暗区和接近饱和的亮区中有效地提取场景信息，同时处理与视图相关的颜色，而不会增加球谐波的程度。其次，通过仔细的光栅化调整，我们隐含地克服了3DGS对点云初始化的严重依赖和敏感性。这对于在低纹理、高景深和低照度区域进行精确重建至关重要。HDRSplat是迄今为止最快的方法，可以在15分钟/场景内完成14位（HDR）3D场景重建（比之前最先进的RawNeRF快30倍）。它还拥有最快的推理速度，为120fps。我们通过展示各种应用，如合成散焦、密集深度图提取以及曝光、色调映射和视点的捕捉后控制，进一步证明了HDR场景重建的适用性。 et.al.|[2407.16503](http://arxiv.org/abs/2407.16503)|**[link](https://github.com/shreyesss/hdrsplat)**|
|**2024-07-22**|**BoostMVSNeRFs: Boosting MVS-based NeRFs to Generalizable View Synthesis in Large-scale Scenes**|虽然神经辐射场（NeRFs）表现出了卓越的质量，但其漫长的训练时间仍然是一个限制。可推广和基于MVS的NeRF虽然能够缩短训练时间，但往往会在质量上进行权衡。本文提出了一种称为BoostMVSNeRFs的新方法，以提高基于MVS的NeRF在大规模场景中的渲染质量。我们首先确定了基于MVS的NeRF方法的局限性，例如受限的视口覆盖和由于有限的输入视图引起的伪影。然后，我们通过提出一种在体绘制过程中选择和组合多个成本体积的新方法来解决这些局限性。我们的方法不需要训练，可以以前馈方式适应任何基于MVS的NeRF方法，以提高渲染质量。此外，我们的方法也是端到端可训练的，允许对特定场景进行微调。我们通过在大规模数据集上的实验证明了我们的方法的有效性，在大规模场景和无界户外场景中显示出显著的渲染质量改进。BoostMVSNeRFs的源代码发布于https://su-terry.github.io/BoostMVSNeRFs/. et.al.|[2407.15848](http://arxiv.org/abs/2407.15848)|null|
|**2024-07-22**|**6DGS: 6D Pose Estimation from a Single Image and a 3D Gaussian Splatting Model**|我们提出了6DGS来估计给定表示场景的3D高斯散斑（3DGS）模型的目标RGB图像的相机姿态。6DGS避免了典型的合成分析方法（如iNeRF）的迭代过程，该方法还需要初始化相机姿态才能收敛。相反，我们的方法通过反转3DGS渲染过程来估计6DoF姿态。从物体表面开始，我们定义了一个辐射Ellicell，它均匀地生成从每个椭球体出发的光线，这些椭球体对3DGS模型进行了参数化。每个Ellicell光线都与每个椭球体的渲染参数相关联，这些参数又用于获得目标图像像素和投射光线之间的最佳绑定。然后对这些像素光线绑定进行排序，以选择得分最高的光线束，它们的交点提供了相机中心，进而提供了相机旋转。所提出的解决方案消除了初始化时“先验”姿态的必要性，并以封闭形式解决了6DoF姿态估计问题，而不需要迭代。此外，与现有的用于姿态估计的新视图合成（NVS）基线相比，6DGS可以在真实场景中将整体平均旋转精度提高12%，平移精度提高22%，尽管不需要任何初始化姿态。同时，我们的方法近乎实时运行，在消费类硬件上达到15fps。 et.al.|[2407.15484](http://arxiv.org/abs/2407.15484)|null|

<p align=right>(<a href=#updated-on-20240802>back to top</a>)</p>

## 3D Reconstruction

|Publish Date|Title|Abstract|PDF|Code|
|---|---|---|---|---|
|**2024-07-30**|**NIS-SLAM: Neural Implicit Semantic RGB-D SLAM for 3D Consistent Scene Understanding**|近年来，神经内隐表示范式在同步定位和映射（SLAM）领域引起了广泛关注。然而，在场景理解方面，现有的方法存在明显的差距。本文介绍了NIS-SLAM，这是一种高效的神经隐式语义RGB-D SLAM系统，它利用预训练的2D分割网络来学习一致的语义表示。具体来说，为了实现高保真表面重建和空间一致的场景理解，我们将基于高频多分辨率四面体的特征和低频位置编码结合起来作为隐式场景表示。此外，为了解决多视图二维分割结果的不一致性，我们提出了一种融合策略，将先前非关键帧的语义概率整合到关键帧中，以实现一致的语义学习。此外，我们实现了一种基于置信度的像素采样和渐进优化权重函数，用于鲁棒的相机跟踪。在各种数据集上的广泛实验结果表明，与其他现有的神经密集隐式RGB-D SLAM方法相比，我们的系统具有更好或更具竞争力的性能。最后，我们还表明我们的方法可以用于增强现实应用。项目页面：\href{https://zju3dv.github.io/nis_slam}{https://zju3dv.github.io/nis\_砰。 et.al.|[2407.20853](http://arxiv.org/abs/2407.20853)|null|
|**2024-07-29**|**X-ray nano-holotomography reconstruction with simultaneous probe retrieval**|在传统的断层重建中，预处理步骤包括平场校正，其中探测器上的每个样本投影都除以没有样本的参考图像。当使用相干X射线作为探针时，这种方法忽略了照明场（探针）的相位分量，导致相位检索投影图像中的伪影，然后将伪影传播到重建的3D样本表示中。在使用聚焦光学元件的纳米全息断层扫描中，由于各种缺陷，探头功能中会产生高频分量，这一问题更加严重。在这里，我们提出了一种新的全断层摄影迭代重建方案，同时检索复值探测函数。该算法在GPU上实现，可实现3D重建，分辨率为使用纳米全息断层扫描测量的3D ALD标准样品中的两倍薄层。 et.al.|[2407.20304](http://arxiv.org/abs/2407.20304)|null|
|**2024-07-29**|**TeleOR: Real-time Telemedicine System for Full-Scene Operating Room**|远程医疗的出现代表了利用技术将专业医疗专业知识扩展到远程手术的变革性发展，在这个领域，专家指导的即时性至关重要。然而，手术室（OR）场景的复杂动态给远程医疗带来了独特的挑战，特别是在障碍物和带宽限制下实现高保真、实时的场景重建和传输。本文介绍了TeleOR，这是一个开创性的系统，旨在通过远程干预的实时OR场景重建来应对这些挑战。TeleOR以三种创新方法脱颖而出：动态自校准，利用固有的场景特征进行校准，无需预设标记，允许避障和实时调整相机；选择性OR重建，侧重于动态变化的场景片段，以降低重建复杂度；基于实时客户端反馈优化数据传输以在带宽限制内有效地提供高质量的3D重建。4D-OR手术场景数据集的综合实验证明了TeleOR的优越性和适用性，阐明了通过克服远程手术指导固有的空间和技术障碍来彻底改变远程干预的潜力。 et.al.|[2407.19763](http://arxiv.org/abs/2407.19763)|null|
|**2024-07-29**|**SALVE: A 3D Reconstruction Benchmark of Wounds from Consumer-grade Videos**|管理慢性伤口是一项全球性挑战，可以通过采用消费级视频的临床伤口评估自动系统来缓解。虽然2D图像分析方法不足以处理伤口的3D特征，但利用3D重建方法的现有方法尚未得到彻底评估。为了解决这一差距，本文对消费级视频的3D伤口重建进行了全面的研究。具体来说，我们介绍了SALVE数据集，其中包括用不同相机拍摄的逼真伤口幻影的视频记录。使用此数据集，我们评估了最先进的3D重建方法的准确性和精度，从传统的摄影测量管道到先进的神经渲染方法。在我们的实验中，我们观察到摄影测量方法不能提供适合精确临床测量伤口的光滑表面。神经渲染方法在解决这一问题方面显示出希望，推动了这项技术在伤口护理实践中的应用。 et.al.|[2407.19652](http://arxiv.org/abs/2407.19652)|null|
|**2024-07-28**|**Cycle3D: High-quality and Consistent Image-to-3D Generation via Generation-Reconstruction Cycle**|最近的3D大型重建模型通常采用两阶段过程，包括首先通过多视图扩散模型生成多视图图像，然后利用前馈模型将图像重建为3D内容。然而，多视图扩散模型通常会产生低质量和不一致的图像，对最终3D重建的质量产生不利影响。为了解决这个问题，我们提出了一种名为Cycle3D的统一3D生成框架，该框架在多步扩散过程中循环利用基于2D扩散的生成模块和前馈3D重建模块。具体而言，2D扩散模型用于生成高质量的纹理，重建模型保证了多视图的一致性。此外，2D扩散模型可以进一步控制生成的内容，并为看不见的视图注入参考视图信息，从而增强去噪过程中3D生成的多样性和纹理一致性。大量实验证明，与最先进的基线相比，我们的方法具有创建高质量和一致性的3D内容的卓越能力。 et.al.|[2407.19548](http://arxiv.org/abs/2407.19548)|null|
|**2024-07-27**|**A Bayesian Approach Toward Robust Multidimensional Ellipsoid-Specific Fitting**|这项工作提出了一种新颖有效的方法，用于在噪声和异常值污染的情况下将多维椭球体拟合到散射数据中。我们将该问题视为贝叶斯参数估计过程，并在给定数据的情况下最大化某个椭球解的后验概率。我们基于贝叶斯框架内的预测分布在这些点之间建立了更稳健的相关性。我们采用均匀的先验分布来约束在椭球域内搜索原始参数，确保无论输入如何，都能得到椭球特定的结果。然后，我们通过贝叶斯规则建立测量点和模型数据之间的连接，以增强该方法对噪声的鲁棒性。由于与空间维度无关，所提出的方法不仅为具有挑战性的细长椭球体提供了高质量的拟合，而且很好地推广到多维空间。为了解决以往方法经常忽视的异常值干扰，我们在预测分布的基础上进一步引入了均匀分布，以显著增强算法对异常值的鲁棒性。我们引入了一种加速技术，大大加快了EM的收敛速度。据我们所知，这是第一种能够在各种干扰下在贝叶斯优化范式内进行多维椭球体特定拟合的综合方法。我们在存在强噪声、异常值和轴比大幅变化的情况下，在低维和高维空间中对其进行评估。此外，我们将其应用于广泛的实际应用，如显微镜细胞计数、3D重建、几何形状近似和磁力计校准任务。 et.al.|[2407.19269](http://arxiv.org/abs/2407.19269)|**[link](https://github.com/zikai1/bayfit)**|
|**2024-07-26**|**Floating No More: Object-Ground Reconstruction from a Single Image**|从单个图像重建3D对象的最新进展主要集中在提高对象形状的准确性上。然而，这些技术往往无法准确捕捉物体、地面和相机之间的相互关系。因此，当放置在平面上时，重建的对象通常会出现浮动或倾斜。这一限制严重影响了3D感知图像编辑应用程序，如阴影渲染和对象姿态操纵。为了解决这个问题，我们引入了ORG（地面对象重建），这是一项旨在结合地面重建3D对象几何的新任务。我们的方法使用两个紧凑的像素级表示来描述相机、物体和地面之间的关系。实验表明，与传统的单图像3D重建技术相比，所提出的ORG模型可以在看不见的数据上有效地重建目标地面几何，显著提高了阴影生成和姿态操纵的质量。 et.al.|[2407.18914](http://arxiv.org/abs/2407.18914)|null|
|**2024-07-26**|**IOVS4NeRF:Incremental Optimal View Selection for Large-Scale NeRFs**|现代应用的城市级三维重建需要高渲染保真度，同时最大限度地降低计算成本。神经辐射场（NeRF）的出现增强了3D重建，但它在多个视点下表现出伪影。本文提出了一种新的NeRF框架方法来解决这些问题。我们的方法使用图像内容和姿势数据来迭代地规划下一个最佳视图。该方法的一个关键方面涉及不确定性估计，指导从候选集中选择具有最大信息增益的视图。随着时间的推移，这种迭代过程提高了渲染质量。同时，我们引入了Vonoroi图和阈值采样以及飞行分类器，以提高效率，同时保持原始NeRF网络的完整性。它可以作为一个插件工具来帮助更好的渲染，优于基线和类似的先前工作。 et.al.|[2407.18611](http://arxiv.org/abs/2407.18611)|null|
|**2024-07-25**|**UMono: Physical Model Informed Hybrid CNN-Transformer Framework for Underwater Monocular Depth Estimation**|水下单目深度估计是水下场景三维重建等任务的基础。然而，由于光和介质的影响，水下环境经历了独特的成像过程，这给从单幅图像中准确估计深度带来了挑战。现有的方法未能考虑水下环境的独特特征，导致估计结果不足，泛化性能有限。此外，水下深度估计需要提取和融合局部和全局特征，这在现有方法中没有得到充分探索。本文提出了一种用于水下单目深度估计的端到端学习框架UMono，该框架将水下图像形成模型特征融入网络架构，有效地利用了水下图像的局部和全局特征。实验结果表明，该方法对水下单目深度估计是有效的，在定量和定性分析方面都优于现有方法。 et.al.|[2407.17838](http://arxiv.org/abs/2407.17838)|null|
|**2024-07-24**|**SMA-Hyper: Spatiotemporal Multi-View Fusion Hypergraph Learning for Traffic Accident Prediction**|预测交通事故是可持续城市管理的关键，这需要有效解决城市的动态和复杂的时空特征。当前的数据驱动模型经常与数据稀疏性作斗争，通常忽视了不同城市数据源的集成及其内部的高阶依赖关系。此外，它们经常依赖于预定义的拓扑或权重，限制了它们在时空预测中的适应性。为了解决这些问题，我们引入了时空多视图自适应超图学习（SMA Hyper）模型，这是一种为交通事故预测设计的动态深度学习框架。基于先前的研究，这一创新模型结合了双重自适应时空图学习机制，通过超图和动态适应不断变化的城市数据，实现了高阶跨区域学习。它还利用对比学习来增强稀疏数据集中的全局和局部数据表示，并采用预先注意机制来融合事故数据和城市功能特征的多种视图，从而丰富了对风险因素的上下文理解。对伦敦交通事故数据集的广泛测试表明，SMA Hyper模型在各种时间范围和多步输出方面明显优于基线模型，证实了其多视图融合和自适应学习策略的有效性。结果的可解释性进一步强调了其通过利用复杂的时空城市数据来改善城市交通管理和安全的潜力，提供了一个适应不同城市环境的可扩展框架。 et.al.|[2407.17642](http://arxiv.org/abs/2407.17642)|null|

<p align=right>(<a href=#updated-on-20240802>back to top</a>)</p>

## Diffusion

|Publish Date|Title|Abstract|PDF|Code|
|---|---|---|---|---|
|**2024-07-31**|**Detecting, Explaining, and Mitigating Memorization in Diffusion Models**|扩散模型的最新突破显示出卓越的图像生成能力。然而，研究表明，一些输出只是训练数据的复制。这种复制给模型所有者带来了潜在的法律挑战，特别是当生成的内容包含专有信息时。在这项工作中，我们介绍了一种通过检查文本条件预测的幅度来检测记忆提示的简单而有效的方法。我们提出的方法无缝集成，不会中断采样算法，即使在第一代步骤也能提供高精度，每个提示只生成一代。基于我们的检测策略，我们推出了一种可解释的方法，显示了单个单词或标记对记忆的贡献。这为用户提供了一个交互式媒介来调整他们的提示。此外，我们提出了两种策略，即通过在推理过程中最小化或在训练过程中过滤来利用文本条件预测的幅度来减轻记忆。这些提出的策略有效地抵消了记忆，同时保持了高代质量。代码可在以下网址获得https://github.com/YuxinWenRick/diffusion_memorization. et.al.|[2407.21720](http://arxiv.org/abs/2407.21720)|null|
|**2024-07-31**|**Dephasing-assisted transport in a tight-binding chain with a linear potential**|与量子系统相互作用的环境可以通过抑制导致局域化的量子效应来增强输运。本文研究了边界驱动紧束缚链中体退相和线性势之间的相互作用。线性电势在没有噪声的情况下诱导Wannier-Stark局域化，而在没有倾斜的情况下，去相位诱导扩散输运。我们推导出了稳态电流作为退相和倾斜函数的近似表达式，该表达式与各种参数的精确解非常匹配。由此，我们发现，在Wannier-Stark局域化系统中，当退相率等于布洛赫振荡的周期时，电流达到最大。我们还发现，如果整个链上的总潜在倾斜保持不变，则电流显示为系统大小的函数的最大值。我们的结果可以在当前的实验平台上得到验证，代表着环境辅助运输分析研究向前迈出了一步。 et.al.|[2407.21715](http://arxiv.org/abs/2407.21715)|null|
|**2024-07-31**|**Tora: Trajectory-oriented Diffusion Transformer for Video Generation**|扩散变换器（DiT）的最新进展证明了其在制作高质量视频内容方面的卓越能力。尽管如此，基于变压器的扩散模型在有效生成具有可控运动的视频方面的潜力仍然是一个有限的探索领域。本文介绍了Tora，这是第一个面向轨迹的DiT框架，它同时集成了文本、视觉和轨迹条件，用于视频生成。具体来说，Tora由轨迹提取器~（TE）、时空DiT和运动制导融合器~（MGF）组成。TE使用3D视频压缩网络将任意轨迹编码为分层时空运动块。MGF将运动块集成到DiT块中，以生成遵循轨迹的一致视频。我们的设计与DiT的可扩展性无缝对接，允许以不同的持续时间、宽高比和分辨率精确控制视频内容的动态。广泛的实验证明了Tora在实现高运动保真度方面的卓越表现，同时也细致地模拟了物理世界的运动。页面可以在以下网址找到https://ali-videoai.github.io/tora_video. et.al.|[2407.21705](http://arxiv.org/abs/2407.21705)|null|
|**2024-07-31**|**Generative Diffusion Model for Seismic Imaging Improvement of Sparsely Acquired Data and Uncertainty Quantification**|稀疏采集数据的地震成像面临着图像质量低、不连续性和偏移摆动伪影等挑战。现有的基于卷积神经网络（CNN）的方法难以处理复杂的特征分布，无法有效评估不确定性，因此难以评估其处理结果的可靠性。为了解决这些问题，我们提出了一种使用生成扩散模型（GDM）的新方法。在这里，在训练阶段，我们使用稀疏数据的成像结果作为条件输入，结合密集数据成像结果的噪声版本，让网络预测添加的噪声。经过训练后，该网络可以使用具有条件控制的生成过程，从稀疏数据采集中预测测试图像的成像结果。这种GDM不仅提高了图像质量，消除了稀疏数据引起的伪影，而且通过利用GDM的概率特性自然地评估了不确定性。为了克服大规模图像的生成质量下降和内存负担，我们开发了一种补丁融合策略，有效地解决了这些问题。合成和现场数据示例表明，我们的方法显著提高了成像质量，并提供了有效的不确定性量化。 et.al.|[2407.21683](http://arxiv.org/abs/2407.21683)|null|
|**2024-07-31**|**Charged-impurity free printing-based diffusion doping in molybdenum disulfide field-effect transistors**|在实际的电子应用中，掺杂对于开发大面积二维（2D）半导体至关重要，表面电荷转移掺杂（SCTD）已成为定制其电特性的一种有前景的策略。然而，在提供或提取载流子后，由产生的电离掺杂剂引起的杂质散射阻碍了2D半导体层中的传输，限制了载流子迁移率。在这里，我们提出了一种用于化学气相沉积（CVD）生长的二硫化钼的扩散掺杂方法，该方法避免了带电杂质的干扰。选择性喷墨印刷的掺杂剂仅引入接触区域，由于电子密度差异，允许过量捐赠的电子扩散到沟道层。因此，扩散掺杂的二硫化钼FET在沟道上没有不希望的带电杂质，与传统的直接掺杂FET相比，其场效应迁移率高出两倍以上。我们的研究为一种新的掺杂策略铺平了道路，该策略同时抑制了带电杂质散射，并促进了SCTD效应的定制。 et.al.|[2407.21678](http://arxiv.org/abs/2407.21678)|null|
|**2024-07-31**|**Stable Perovskite Solar Cells via exfoliated graphite as an ion diffusion-blocking layer**|金属卤化物钙钛矿、电荷传输层和电极中的离子和金属扩散对钙钛矿基光伏器件的性能和稳定性有害。因此，人们对开发新的缺陷和离子扩散缓解策略有着浓厚的研究兴趣。我们提出了一种简单、低成本、可扩展且高效的方法，该方法使用喷涂剥离石墨中间层来阻止离子和金属在钙钛矿、空穴传输材料和金属电极中的扩散和湿度进入。通过多种方法，包括X射线衍射、飞行时间二次离子质谱、扫描电子显微镜、原子力显微镜、电流-电压（J-V）特性、瞬态光电流和瞬态光电压，研究了插入剥离石墨薄膜对结构、表面形态和光电性能的影响。我们的综合调查发现，剥离石墨薄膜减少了层间的I-和Li+扩散，从而减轻了缺陷，减少了非辐射复合，提高了器件的稳定性。因此，性能最佳的器件表现出25%的功率转换效率和超过80%的填充系数。此外，这些设备经过了不同的寿命测试，显著提高了操作稳定性。 et.al.|[2407.21662](http://arxiv.org/abs/2407.21662)|null|
|**2024-07-31**|**Properties of the diffuse gas component in filaments detected in the Dianoga cosmological simulations**|流体动力学宇宙学模拟是研究宇宙网演化的理想实验室。这使得更容易了解细丝的性质。我们研究了从更大的宇宙学模拟中提取的区域中细丝的内在特性是如何演变的。我们的目标是确定暖热星系际介质（WHIM）特性的重要趋势，并提出可能的解释。为了研究细丝及其含量，我们从Dianoga模拟中选择了一部分区域。我们分析了用不同重子物理模拟的这些区域，即有和没有AGN反馈。我们使用子空间约束均值漂移（SCMS）算法和求解细丝的序列链算法（SCARF）构建宇宙网。我们研究了细丝的基本物理性质（长度、形状、质量、半径），并分析了这些结构中的不同气相（热、WHIM和冷气体成分）。在红移范围 $0<z<1.48$内研究了整体灯丝性能和气相性能的演变。在我们的模拟中，检测到的细丝平均长度低于9$Mpc。细丝的形状与其长度相关；它们越长，就越有可能弯曲。我们发现，细丝的质量$M$和长度$L$之间的标度关系可以用幂律$M\propto L^{1.7}$ 很好地描述。径向密度分布随着红移而变宽，这意味着细丝的半径随着时间的推移而变大。WHIM相中的气体质量分数不取决于模型，并且正在向较低的红移方向上升。然而，所包含的重子物理学对细丝中气体的金属性有很强的影响，表明AGN反馈已经在红移2美元时影响了金属含量。 et.al.|[2407.21636](http://arxiv.org/abs/2407.21636)|null|
|**2024-07-31**|**VEGAS-SSS: Tracing Globular Cluster Populations in the Interacting NGC3640 Galaxy Group**|球状星团（GC）是宇宙中最古老的恒星系统之一。因此，GC群体是星系形成和相互作用历史的有价值的化石示踪剂。我们使用VST获得的多波段宽场图像来研究相互作用星系对中GC粒子群的性质。我们以两个椭圆星系组成的星系群为中心，推导出了1.5x1.5deg^2 $以上的ugri光度：NGC3640及其较暗的伴星NGC3641。我们研究了ugri和gri匹配目录中的GC系统特性。根据光度特性（颜色、大小）和形态计量标准（浓度指数、伸长率、半峰全宽）的组合，使用文献中可用的光谱或成像数据中具有明确分类的来源和数值模拟作为参考，确定了GC候选者。选择标准也适用于空白字段，以确定已识别GC候选人数量的统计背景校正。GC的二维密度图似乎与星系合并事件产生的漫射光斑对齐。观测到GC的最高密度峰值在NGC3641而不是NGC3640上，尽管后者是质量更大的星系。这两个星系的方位角平均径向密度分布揭示，GC群体延伸到星系光分布之外，并表明可能存在组内GC成分。NGC3641在（u-r）和（g-i）中观察到颜色双峰，而NGC3640显示出宽的单峰分布。GC光度函数的分析表明，这两个星系大致位于相同的距离（~27Mpc）。我们提供了GC总数的估计值，并确定了NGC3640的具体频率，$S_N=2.0\pm0.6$，这与预期一致，而对于NGC3641，我们发现一个很大的$S_N=4.5\pm1.6$ 。 et.al.|[2407.21620](http://arxiv.org/abs/2407.21620)|null|
|**2024-07-31**|**A τ Matrix Based Approximate Inverse Preconditioning for Tempered Fractional Diffusion Equations**|回火分数扩散方程是广泛应用于许多物理领域的一类关键方程。本文首先应用Crank-Nicolson方法和回火加权和移位Gr“unwald公式对回火分数扩散方程进行离散化。然后我们得到离散系统的系数矩阵具有单位矩阵和对角矩阵之和乘以对称正定（SPD）Toeplitz矩阵的结构。基于SPD Toeplitz阵的性质，我们使用 $tau矩阵对其进行近似，然后提出了一种新的近似逆预条件器来近似系数矩阵。基于$ tau矩阵的近似逆前条件器可以使用离散正弦变换（DST）有效地计算。在谱分析中，预条件系数的特征值矩阵围绕1进行聚类，确保了Krylov子空间方法与新预处理器的快速收敛。最后，数值实验证明了所提出的预处理器的有效性。 et.al.|[2407.21603](http://arxiv.org/abs/2407.21603)|null|
|**2024-07-31**|**Robust Simultaneous Multislice MRI Reconstruction Using Deep Generative Priors**|同步多层（SMS）成像是一种加速磁共振成像（MRI）采集的强大技术。然而，由于受激切片之间和内部复杂的信号相互作用，SMS重建仍然具有挑战性。本研究提出了一种使用深度生成先验的鲁棒SMS MRI重建方法。从高斯噪声出发，我们利用去噪扩散概率模型（DDPM）通过反向扩散迭代逐步恢复单个切片，同时在读出级联框架下从测量的k空间中施加数据一致性。后验采样过程的设计使得DDPM训练可以在单层图像上进行，而无需对SMS任务进行特殊调整。此外，我们的方法集成了低频增强（LFE）模块，以解决SMS加速的快速自旋回波（FSE）和回波平面成像（EPI）序列不能轻易嵌入自动校准信号的实际问题。大量的实验表明，我们的方法始终优于现有方法，并很好地推广到看不见的数据集。该代码可在以下网址获得https://github.com/Solor-pikachu/ROGER在审查过程之后。 et.al.|[2407.21600](http://arxiv.org/abs/2407.21600)|null|

<p align=right>(<a href=#updated-on-20240802>back to top</a>)</p>

## NeRF

|Publish Date|Title|Abstract|PDF|Code|
|---|---|---|---|---|
|**2024-07-30**|**Neural Fields for Continuous Periodic Motion Estimation in 4D Cardiovascular Imaging**|时间分辨三维血流MRI（4D血流MRI）提供了一种独特的非侵入性解决方案，用于可视化和量化主动脉弓等血管中的血流动力学。然而，由于难以获得完整的周期分割，目前大多数动脉4D血流MRI分析方法使用静态动脉壁。为了克服这一局限性，我们提出了一种基于神经场的方法，可以直接估计整个心动周期中连续的周期性壁变形。对于3D+时间成像数据集，我们优化了表示时间依赖速度矢量场（VVF）的隐式神经表示（INR）。ODE求解器用于将VVF集成到变形矢量场（DVF）中，该矢量场可以随着时间的推移使图像、分割掩模或网格变形，从而可视化和量化局部壁运动模式。为了正确反映3D+时间心血管数据的周期性，我们以两种方式施加周期性。首先，通过定期对输入到INR的时间进行编码，从而对VVF进行编码。其次，通过规范DVF。我们证明了这种方法在不同周期模式的合成数据、心电图门控CT和4D血流MRI数据上的有效性。所获得的方法可用于改进4D血流MRI分析。 et.al.|[2407.20728](http://arxiv.org/abs/2407.20728)|null|
|**2024-07-29**|**Aero-Nef: Neural Fields for Rapid Aircraft Aerodynamics Simulations**|本文提出了一种基于隐式神经表示（INR）在网格域上学习稳态流体动力学模拟替代模型的方法。所提出的模型可以直接应用于不同流动条件下的非结构化域，处理非参数3D几何变化，并推广到测试时看不见的形状。基于坐标的公式自然会导致离散化的鲁棒性，从而在计算成本（内存占用和训练时间）和精度之间实现了极好的权衡。该方法在两个工业相关应用中得到了验证：跨音速翼型上二维可压缩流的RANS数据集和三维机翼上表面压力分布的数据集，包括形状、流入条件和控制表面偏转变化。在所考虑的测试用例中，与最先进的图神经网络架构相比，我们的方法实现了三倍多的测试误差，并显著改善了看不见的几何形状的泛化误差。值得注意的是，该方法在RANS跨音速翼型数据集上的推理速度比高保真求解器快五个数量级。代码可在以下网址获得https://gitlab.isae-supaero.fr/gi.catalani/aero-nepf et.al.|[2407.19916](http://arxiv.org/abs/2407.19916)|null|
|**2024-07-26**|**ObjectCarver: Semi-automatic segmentation, reconstruction and separation of 3D objects**|隐式神经场在从多幅图像重建3D表面方面取得了显著进展；然而，在分离场景中的单个对象时，他们遇到了挑战。之前的工作试图通过引入一个框架来解决这个问题，该框架为N个对象中的每一个同时训练单独的带符号距离场（SDF），并使用正则化项来防止对象重叠。然而，所有这些方法都需要提供分割掩模，这并不总是容易获得的。我们介绍了我们的方法ObjectCarver，来解决在单个视图中从点击输入中分离对象的问题。给定摆出的多视图图像和一组用户输入点击来提示分割单个对象，我们的方法将场景分解为单独的对象，并为每个对象重建高质量的3D表面。我们引入了一个损失函数，可以防止漂浮物，避免因遮挡而造成不适当的雕刻。此外，我们引入了一种新的场景初始化方法，与之前的方法相比，该方法在保留几何细节的同时显著加快了过程。尽管不需要地面真实掩模或单眼线索，但我们的方法在定性和定量上都优于基线。此外，我们引入了一个新的基准数据集进行评估。 et.al.|[2407.19108](http://arxiv.org/abs/2407.19108)|null|
|**2024-07-24**|**Neural field equations with time-periodic external inputs and some applications to visual processing**|这项工作的目的是为研究视觉处理任务中的闪烁输入提供一个数学框架。当与几何图案结合时，这些输入会影响并诱发有趣的心理物理现象，如麦凯效应和比洛克-邹效应，在这些效应中，受试者感知到通常由闪烁频率调制的特定余像。由于输入的对称破缺结构，经典分叉理论和多尺度分析技术在我们的背景下不是很有效。因此，我们采用了一种基于Amari型神经场控制理论的输入-输出框架的方法。这使我们能够证明，当受到周期性输入的驱动时，动态会收敛到周期性状态。此外，我们研究了在哪些假设下，这些非线性动力学可以有效地线性化，在这种情况下，我们提出了短程兴奋性和远程抑制性神经元相互作用的积分核的精确近似值。最后，对于集中在具有闪烁背景的视野中心的输入，我们直接将余像中出现的虚幻轮廓的宽度与闪烁频率和抑制强度联系起来。 et.al.|[2407.17294](http://arxiv.org/abs/2407.17294)|null|
|**2024-07-23**|**Fluorescence Diffraction Tomography using Explicit Neural Fields**|从荧光图像中求解3D折射率（RI）可以提供有关生物样本的荧光和相位信息。然而，在大体积、高分辨率和反射模式下准确检索部分相干光的相位以重建无标签相位物体的未知RI仍然具有挑战性。为了应对这一挑战，我们开发了具有显式神经场的荧光衍射断层扫描（FDT），可以从散焦荧光散斑图像重建3D RI。使用FDT成功重建3D RI依赖于四个关键组件：粗到细建模、自校准、差分多层渲染模型和部分相干掩模。具体而言，显式表示与粗到细建模有效地集成在一起，以实现高速、高分辨率的重建。此外，我们将多层方程推进到微分多层渲染模型，这使得系统的外部和内部参数能够进行自校准。自校准有助于高精度的正向图像预测和RI重建。部分相干掩模是数字掩模，用于准确有效地解决相干光模型和部分相干光数据之间的差异。FDT成功地从荧光图像中重建了24个z $层上1024$×1024像素的530$×530$×300$μm^3$ 体积的3D培养无标记3D MuSCs管的RI，证明了在体外对体积庞大和异质的生物样本进行高保真3D RI重建。 et.al.|[2407.16657](http://arxiv.org/abs/2407.16657)|null|
|**2024-07-22**|**Iterative approach to reconstructing neural disparity fields from light-field data**|本研究提出了一种神经视差场（NDF），该场基于神经场建立了场景视差的隐式连续表示，并采用迭代方法解决了从光场数据重建NDF的逆问题。NDF能够无缝和精确地表征三维场景中的视差变化，并可以以任何任意分辨率对视差进行离散化，克服了传统视差图容易出现采样误差和插值不准确的局限性。所提出的NDF网络架构利用哈希编码结合多层感知器来捕获纹理级别的详细差异，从而增强其表示复杂场景几何信息的能力。通过利用光场数据中固有的空间角度一致性，开发了一种可微分正向模型，用于从光场数据生成中心视图图像。基于正向模型，建立了一种使用可微传播算子的NDF重建逆问题的优化方案。此外，在优化方案中，采用迭代求解方法重建NDF，该方法不需要训练数据集，适用于各种采集方法捕获的光场数据。实验结果表明，使用所提出的方法可以从光场数据中重建高质量的NDF。NDF可以有效地恢复高分辨率视差，证明了其隐式、连续表示场景视差的能力。 et.al.|[2407.15380](http://arxiv.org/abs/2407.15380)|null|
|**2024-07-19**|**Contextual modulation of language comprehension in a dynamic neural model of lexical meaning**|我们提出并计算实现了一个词汇意义的动态神经模型，并对其行为预测进行了实验测试。我们使用英语词汇“have”作为测试用例来演示模型的架构和行为，重点关注其多义词的使用。在该模型中，“have”映射到由两个连续的概念维度（连通性和控制不对称性）定义的语义空间，这两个维度之前被提出用于参数化语言的概念系统。映射被建模为表示词条的神经节点和表示概念维度的神经场之间的耦合。虽然词汇知识被建模为稳定的耦合模式，但实时词汇意义检索被建模为神经激活模式在对应于语义解释或阅读的亚稳态之间的运动。模型模拟捕捉到了两个先前报道的实证观察结果：（1）词汇语义解释的语境调制，以及（2）这种调制幅度的个体差异。模拟还产生了一种新的预测，即句子阅读时间和可接受性之间的试验关系应该根据上下文进行调节。结合自定进度阅读和可接受性判断的实验复制了之前的结果，并证实了新的模型预测。总之，研究结果支持了一种关于词汇多义的新观点：一个词的许多相关含义是亚稳态的神经激活状态，这是由控制连续语义维度解释的神经群体的非线性动力学引起的。 et.al.|[2407.14701](http://arxiv.org/abs/2407.14701)|null|
|**2024-07-18**|**MeshFeat: Multi-Resolution Features for Neural Fields on Meshes**|参数特征网格编码作为神经场的编码方法受到了广泛关注，因为它们允许更小的MLP，这大大缩短了模型的推理时间。在这项工作中，我们提出了MeshFeat，这是一种针对网格量身定制的参数特征编码，为此我们采用了欧几里德空间的多分辨率特征网格的思想。我们从给定顶点拓扑提供的结构开始，使用网格简化算法直接在网格上构建多分辨率特征表示。该方法允许在网格上的神经场中使用小MLP，与之前的表示相比，我们显示出显著的加速，同时保持了纹理重建和BRDF表示的可比重建质量。鉴于其与顶点的内在耦合，该方法特别适用于变形网格上的表示，使其非常适合对象动画。 et.al.|[2407.13592](http://arxiv.org/abs/2407.13592)|null|
|**2024-07-16**|**Adaptive Environment-Aware Robotic Arm Reaching Based on a Bio-Inspired Neurodynamical Computational Framework**|仿生机器人系统具有自适应学习、可扩展控制和高效信息处理的能力。为这些系统提供实时决策对于应对环境的动态变化至关重要。我们专注于在开放区域使用带有鸟瞰摄像头的机器人六自由度操纵器进行动态目标跟踪，并部署神经动力学计算框架（NeuCF）进行视觉反馈。NeuCF是最近开发的一种基于动态神经场（DNF）和随机最优控制（SOC）理论的仿生目标跟踪模型。它已经过训练，可以在平面上对局部视觉信标进行到达动作，并且可以根据环境的变化（例如，出现了新的目标，或者删除了现有的目标）实时重新定位或生成停止信号。我们在各种目标达成场景下评估了我们的系统。在所有实验中，与基线三次多项式轨迹生成器相比，NeuCF具有较高的末端执行器位置精度，生成了平滑的轨迹，并提供了更短的路径长度。总之，开发的系统提供了一种强大的、动态感知的机器人操纵方法，可以提供实时决策。 et.al.|[2407.11377](http://arxiv.org/abs/2407.11377)|null|
|**2024-07-12**|**Physics-Informed Learning of Characteristic Trajectories for Smoke Reconstruction**|我们通过稀疏视图RGB视频深入研究了烟雾和障碍物的物理信息神经重建，解决了复杂动力学观测有限带来的挑战。现有的基于物理信息的神经网络通常强调短期物理约束，对长期守恒的适当保护探索较少。我们引入了神经特征轨迹场，这是一种利用欧拉神经场隐式建模拉格朗日流体轨迹的新表示方法。这种无拓扑、可自动微分的表示便于在任意帧之间进行高效的流图计算，以及通过自动微分进行高效的速度提取。因此，它实现了涵盖长期保护和短期物理先验的端到端监督。在此基础上，我们提出了基于物理的轨迹学习和集成到基于NeRF的场景重建中。我们通过自我监督的场景分解和无缝集成的边界约束来实现高级障碍物处理。我们的结果展示了克服遮挡不确定性、密度-颜色模糊性和静态-动态纠缠等挑战的能力。代码和示例测试位于\url{https://github.com/19reborn/PICT_smoke}. et.al.|[2407.09679](http://arxiv.org/abs/2407.09679)|**[link](https://github.com/19reborn/pict_smoke)**|

<p align=right>(<a href=#updated-on-20240802>back to top</a>)</p>

[contributors-shield]: https://img.shields.io/github/contributors/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[contributors-url]: https://github.com/Vincentqyw/cv-arxiv-daily/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[forks-url]: https://github.com/Vincentqyw/cv-arxiv-daily/network/members
[stars-shield]: https://img.shields.io/github/stars/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[stars-url]: https://github.com/Vincentqyw/cv-arxiv-daily/stargazers
[issues-shield]: https://img.shields.io/github/issues/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[issues-url]: https://github.com/Vincentqyw/cv-arxiv-daily/issues

