[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]

## Updated on 2024.08.08
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
|**2024-08-07**|**3iGS: Factorised Tensorial Illumination for 3D Gaussian Splatting**|使用3D高斯作为辐射场的表示，实现了实时渲染速度下的高质量新颖视图合成。然而，选择将每个高斯光束的出射辐射独立地优化为球面谐波会导致不令人满意的视景相关效果。为了应对这些局限性，我们的工作，3D高斯散斑的因子化张量照明，或3iGS，提高了3D高斯散场（3DGS）的渲染质量。3iGS不是优化单个出射辐射参数，而是通过将出射辐射表示为局部照明场和双向反射分布函数（BRDF）特征的函数来增强3DGS视图相关效果。我们通过张量分解表示优化连续入射光照场，同时分别微调每个3D高斯光照场相对于该光照场的BRDF特征。我们的方法显著提高了3DGS的镜面视图相关效果的渲染质量，同时保持了快速的训练和渲染速度。 et.al.|[2408.03753](http://arxiv.org/abs/2408.03753)|null|
|**2024-08-06**|**RayGauss: Volumetric Gaussian-Based Ray Casting for Photorealistic Novel View Synthesis**|基于微分体绘制的方法在新的视图合成方面取得了重大进展。一方面，创新的方法用局部参数化结构取代了神经辐射场（NeRF）网络，在合理的时间内实现了高质量的渲染。另一方面，这些方法使用可微分溅射而不是NeRF的光线投射来使用高斯核快速优化辐射场，从而可以对场景进行精细调整。然而，不规则间隔内核的可微分光线投射几乎没有得到探索，而飞溅尽管可以实现快速渲染时间，但容易受到清晰可见的伪影的影响。我们的工作通过提供发射辐射c和密度{\sigma}的物理一致公式来缩小这一差距，该公式用与球面高斯/谐波相关的高斯函数分解，用于所有频率的色度表示。我们还介绍了一种方法，该方法使用逐片积分辐射场并利用BVH结构的算法，实现了不规则分布高斯分布的可微分光线投射。这使得我们的方法能够很好地适应场景，同时避免飞溅的伪影。因此，与最先进的技术相比，我们实现了卓越的渲染质量，同时保持了合理的训练时间，并在Blender数据集上实现了25 FPS的推理速度。带有视频和代码的项目页面：https://raygauss.github.io/ et.al.|[2408.03356](http://arxiv.org/abs/2408.03356)|null|
|**2024-08-06**|**Efficient NeRF Optimization -- Not All Samples Remain Equally Hard**|我们提出了一种在线硬样本挖掘的应用，用于高效训练神经辐射场（NeRF）。NeRF模型为许多3D重建和渲染任务提供了最先进的质量，但需要大量的计算资源。NeRF网络参数内场景信息的编码需要随机采样。我们观察到，在训练过程中，大部分计算时间和内存使用都花在处理已经学习的样本上，这不再对模型更新产生显著影响。我们将随机样本的反向传递确定为优化过程中的计算瓶颈。因此，我们在推理模式下执行第一次前向传递，作为对硬样本的相对低成本搜索。随后，构建计算图，并仅使用硬样本更新NeRF网络参数。为了证明所提出方法的有效性，我们将我们的方法应用于Instant NGP，使视图合成质量比基线有了显著提高（平均每训练时间提高1 dB，或加速2倍以达到相同的PSNR水平），同时仅使用硬样本构建计算图可节省约40%的内存。由于我们的方法只与网络模块交互，我们希望它能得到广泛应用。 et.al.|[2408.03193](http://arxiv.org/abs/2408.03193)|null|
|**2024-08-06**|**MGFs: Masked Gaussian Fields for Meshing Building based on Multi-View Images**|在过去的几十年里，基于图像的建筑表面重建引起了广泛的研究兴趣，并已应用于遗产保护、建筑规划等各个领域。与传统的摄影测量和基于NeRF的解决方案相比，最近，基于高斯场的方法因其高效的训练和详细的3D信息保存，在生成表面网格方面显示出巨大的潜力。然而，大多数基于高斯场的方法都是用所有图像像素训练的，包括建筑和非建筑区域，这会导致建筑网格的显著噪声和时间效率的退化。本文提出了一种新的框架——掩模高斯场（MGF），旨在以一种时间高效的方式为建筑物生成精确的表面重建。该框架首先应用EfficientSAM和COLMAP来生成建筑的多级掩模和相应的掩模点云。随后，通过整合两种创新损失来训练掩蔽高斯场：一种是专注于构建建筑区域的多级感知掩蔽损失，另一种是旨在增强不同掩模之间边界细节的边界损失。最后，我们改进了基于掩模高斯球的四面体表面网格提取方法。对无人机图像的综合实验表明，与传统方法和几种基于NeRF和高斯的SOTA解决方案相比，我们的方法显著提高了建筑表面重建的准确性和效率。值得注意的是，作为副产品，建筑的新颖视图合成还有额外的收益。 et.al.|[2408.03060](http://arxiv.org/abs/2408.03060)|null|
|**2024-08-05**|**UlRe-NeRF: 3D Ultrasound Imaging through Neural Rendering with Ultrasound Reflection Direction Parameterization**|三维超声成像是一项广泛应用于医学诊断的关键技术。然而，传统的3D超声成像方法具有固定分辨率、低存储效率和上下文连接不足等局限性，导致处理复杂伪影和反射特性的性能较差。最近，基于NeRF（神经辐射场）的技术在视图合成和3D重建方面取得了重大进展，但在高质量超声成像方面仍存在研究差距。为了解决这些问题，我们提出了一种新的模型UlRe-NeRF，它将隐式神经网络和显式超声体积渲染结合到一个超声神经渲染架构中。该模型结合了反射方向参数化和谐波编码，使用方向MLP模块生成视图相关的高频反射强度估计，并使用空间MLP模块产生介质的物理特性参数。这些参数用于体绘制过程中，以准确再现超声波在介质中的传播和反射行为。实验结果表明，UlRe-NeRF模型显著提高了高保真超声图像重建的真实性和准确性，特别是在处理复杂介质结构时。 et.al.|[2408.00860](http://arxiv.org/abs/2408.00860)|null|
|**2024-08-01**|**EmoTalk3D: High-Fidelity Free-View Synthesis of Emotional 3D Talking Head**|我们提出了一种合成具有可控情绪的3D对话头的新方法，该方法具有增强的嘴唇同步和渲染质量。尽管在该领域取得了重大进展，但现有方法仍然存在多视图一致性和缺乏情感表达的问题。为了解决这些问题，我们收集了带有校准的多视图视频、情感注释和每帧3D几何的EmoTalk3D数据集。通过在EmoTalk3D数据集上进行训练，我们提出了一个\textit{“语音到几何到外观”}映射框架，该框架首先从音频特征预测忠实的3D几何序列，然后从预测的几何中合成由4D高斯表示的3D说话头的外观。该外观进一步被分解为规范高斯和动态高斯，从多视图视频中学习，并融合以渲染自由视图说话的头部动画。此外，我们的模型能够在生成的说话头中实现可控的情绪，并且可以在宽范围的视图中呈现。我们的方法在嘴唇运动生成中表现出改进的渲染质量和稳定性，同时捕获了动态面部细节，如皱纹和微妙的表情。实验证明了我们的方法在生成高保真度和情绪可控的3D对话头方面的有效性。代码和EmoTalk3D数据集发布于https://nju-3dv.github.io/projects/EmoTalk3D. et.al.|[2408.00297](http://arxiv.org/abs/2408.00297)|null|
|**2024-08-01**|**Head360: Learning a Parametric 3D Full-Head for Free-View Synthesis in 360°**|创建人类头部的360度参数模型是一项非常具有挑战性的任务。虽然最近的进展已经证明了利用合成数据构建此类参数化头部模型的有效性，但它们在表情驱动动画、发型编辑和基于文本的修改等关键领域的性能仍然不足。在本文中，我们构建了一个艺术家设计的高保真人头数据集，并提出从中创建一个新的参数化360度可渲染参数化人头模型。我们的方案将面部运动/形状和面部外观解耦，分别由经典的参数化3D网格模型和附加的神经纹理表示。我们进一步提出了一种分解发型和面部外观的训练方法，允许自由交换发型。提出了一种基于单图像输入的具有高泛化和保真度的反演拟合方法。据我们所知，我们的模型是第一个在单个模型中实现360度自由视图合成、基于图像的拟合、外观编辑和动画的参数化3D全头模型。实验表明，面部运动和外观在参数空间中很好地解耦，从而在渲染和动画质量方面提高了SOTA的性能。代码和SynHead100数据集发布于https://nju-3dv.github.io/projects/Head360. et.al.|[2408.00296](http://arxiv.org/abs/2408.00296)|null|
|**2024-08-01**|**LoopSparseGS: Loop Based Sparse-View Friendly Gaussian Splatting**|尽管原始的3D高斯散点（3DGS）实现了逼真的新视图合成（NVS）性能，但其渲染质量在稀疏输入视图下会显著降低。这种性能下降主要是由于稀疏输入生成的初始点数量有限、训练过程中的监督不足以及超大高斯椭球体的正则化不足造成的。为了解决这些问题，我们提出了LoopSparseGS，这是一个基于循环的3DGS框架，用于稀疏新颖视图合成任务。具体来说，我们提出了一种基于循环的渐进高斯初始化（PGI）策略，该策略可以在训练过程中使用渲染的伪图像迭代加密初始化的点云。然后，利用运动结构的稀疏可靠深度和基于窗口的密集单眼深度，通过提出的深度对齐正则化（DAR）提供精确的几何监督。此外，我们引入了一种新的稀疏友好采样（SFS）策略来处理导致大像素误差的超大高斯椭球。在四个数据集上的综合实验表明，在各种图像分辨率的室内、室外和对象级场景中，LoopSparseGS在稀疏输入新视图合成方面优于现有的最先进方法。 et.al.|[2408.00254](http://arxiv.org/abs/2408.00254)|null|
|**2024-08-02**|**Forecasting Future Videos from Novel Views via Disentangled 3D Scene Representation**|空间和时间视频外推（VEST）使观众能够预测未来的3D场景，并从新颖的视角观看。最近的方法提出学习纠缠表示，旨在将分层场景几何、运动预测和新颖的视图合成建模在一起，同时假设每个场景层都有简化的仿射运动和基于单应性的扭曲，导致视频外推不准确。我们的方法不是纠缠的场景表示和渲染，而是选择通过将2D场景提升到3D点云来将场景几何体与场景运动分离，从而能够从新颖的视角对未来的视频进行高质量的渲染。为了模拟未来的3D场景运动，我们提出了一种解纠缠的两阶段方法，该方法首先预测自我运动，然后预测动态对象（如汽车、人）的残余运动。这种方法通过减少自我运动与动态物体运动纠缠的不准确性来确保更精确的运动预测，更好的自我运动预测可以显著提高视觉效果。对两个城市场景数据集的广泛实验分析表明，与强基线相比，我们提出的方法具有更优的性能。 et.al.|[2407.21450](http://arxiv.org/abs/2407.21450)|null|
|**2024-07-30**|**Dynamic Scene Understanding through Object-Centric Voxelization and Neural Rendering**|从无监督视频中学习以对象为中心的表示是具有挑战性的。与之前大多数专注于分解2D图像的方法不同，我们提出了一个名为DynaVol-S的3D生成模型，用于动态场景，该模型在可微体绘制框架内实现了以对象为中心的学习。其关键思想是执行以对象为中心的体素化，以捕捉场景的3D特性，从而推断单个空间位置的每个对象占用概率。这些体素特征通过规范空间变形函数演变，并在具有组合NeRF的逆渲染管道中进行优化。此外，我们的方法整合了2D语义特征来创建3D语义网格，通过多个解纠缠的体素网格来表示场景。DynaVol-S在动态场景的新颖视图合成和无监督分解任务中都明显优于现有模型。通过联合考虑几何结构和语义特征，它有效地解决了涉及复杂对象交互的具有挑战性的现实世界场景。此外，一旦经过训练，显式有意义的体素特征能够实现2D场景分解方法无法实现的额外功能，例如通过编辑几何形状或操纵对象的运动轨迹来生成新的场景。 et.al.|[2407.20908](http://arxiv.org/abs/2407.20908)|**[link](https://github.com/zyp123494/dynavol)**|

<p align=right>(<a href=#updated-on-20240808>back to top</a>)</p>

## 3D Reconstruction

|Publish Date|Title|Abstract|PDF|Code|
|---|---|---|---|---|
|**2024-08-07**|**Opening the Black Box of 3D Reconstruction Error Analysis with VECTOR**|从2D图像重建3D场景是一项技术挑战，影响了从地球和行星科学、太空探索到增强现实和虚拟现实的各个领域。通常，重建算法首先识别图像中的共同特征，然后在估计地形形状后最小化重建误差。这个束调整（BA）步骤围绕一个简化的标量值进行优化，该标量值混淆了重建误差的许多可能原因（例如，相机位置和方向的初始估计、照明条件、地形中特征检测的难易程度）。重建误差可能导致不准确的科学推断，或危及探索偏远环境的航天器。为了应对这一挑战，我们提出了VECTOR，这是一种视觉分析工具，可以改善立体重建BA的误差检查。VECTOR为分析人员提供了以前无法获得的特征位置、相机姿态和计算出的3D点的可见性。VECTOR是与美国国家航空航天局喷气推进实验室的Perseverance火星漫游者和Ingenuity火星直升机地形重建团队合作开发的。我们报告了如何使用该工具调试和改进火星2020任务的地形重建。 et.al.|[2408.03503](http://arxiv.org/abs/2408.03503)|**[link](https://github.com/NASA-AMMOS/VECTOR)**|
|**2024-08-06**|**Efficient NeRF Optimization -- Not All Samples Remain Equally Hard**|我们提出了一种在线硬样本挖掘的应用，用于高效训练神经辐射场（NeRF）。NeRF模型为许多3D重建和渲染任务提供了最先进的质量，但需要大量的计算资源。NeRF网络参数内场景信息的编码需要随机采样。我们观察到，在训练过程中，大部分计算时间和内存使用都花在处理已经学习的样本上，这不再对模型更新产生显著影响。我们将随机样本的反向传递确定为优化过程中的计算瓶颈。因此，我们在推理模式下执行第一次前向传递，作为对硬样本的相对低成本搜索。随后，构建计算图，并仅使用硬样本更新NeRF网络参数。为了证明所提出方法的有效性，我们将我们的方法应用于Instant NGP，使视图合成质量比基线有了显著提高（平均每训练时间提高1 dB，或加速2倍以达到相同的PSNR水平），同时仅使用硬样本构建计算图可节省约40%的内存。由于我们的方法只与网络模块交互，我们希望它能得到广泛应用。 et.al.|[2408.03193](http://arxiv.org/abs/2408.03193)|null|
|**2024-08-06**|**BodySLAM: A Generalized Monocular Visual SLAM Framework for Surgical Applications**|内窥镜手术依赖于二维视图，给外科医生在深度感知和器械操作方面带来了挑战。虽然同步定位和标测（SLAM）已成为解决这些局限性的有前景的解决方案，但由于硬件限制，如使用单眼相机和没有里程计传感器，在内窥镜手术中的实施带来了重大挑战。本研究提出了一种强大的基于深度学习的SLAM方法，该方法结合了最先进和新开发的模型。它由三个主要部分组成：单眼姿态估计模块，它引入了一种基于CycleGAN架构的新型无监督方法；单眼深度估计模块，利用了新型Zoe架构；以及3D重建模块，它使用来自先前模型的信息来创建连贯的手术图。使用三个公开可用的数据集（Hamlyn、EndoSLAM和SCARED）严格评估了该程序的性能，并与两种最先进的方法EndoSFMLearner和EndoDepth进行了基准比较。与内窥镜中最先进的深度估计算法相比，Zoe在MDEM中的集成表现出了卓越的性能，而MPEM中的新方法表现出了具有竞争力的性能和最低的推理时间。结果展示了我们的方法在腹腔镜、胃镜和结肠镜检查中的稳健性，这是内镜手术中的三种不同场景。所提出的SLAM方法有可能通过为外科医生提供增强的深度感知和3D重建能力来提高内窥镜手术的准确性和效率。 et.al.|[2408.03078](http://arxiv.org/abs/2408.03078)|null|
|**2024-08-06**|**VirtualNexus: Enhancing 360-Degree Video AR/VR Collaboration with Environment Cutouts and Virtual Replicas**|非对称AR/VR协作系统将远程VR用户带到本地AR用户的物理环境中，使他们能够在共享的虚拟/物理空间内进行通信和工作。这样的系统通常通过3D重建或360度视频显示远程环境。虽然360度相机以更高的质量流式传输环境，但它们缺乏空间信息，使其交互性较差。我们推出了VirtualNexus，这是一个AR/VR协作系统，通过环境切口和虚拟复制品增强了360度视频AR/VR的协作。VR用户可以定义远程环境的切口，将其作为一个微型世界进行交互，他们的交互与本地AR视角同步。此外，AR用户可以使用神经渲染快速扫描和共享物理对象的3D虚拟副本。我们通过3个示例应用程序展示了我们系统的实用性，并在二元可用性测试中评估了我们的系统。VirtualNexus扩展了360度远程呈现系统的交互空间，提供了更好的物理存在、多功能性和交互清晰度。 et.al.|[2408.02914](http://arxiv.org/abs/2408.02914)|null|
|**2024-08-04**|**View-consistent Object Removal in Radiance Fields**|辐射场（RF）已成为3D场景表示的关键技术，能够合成具有非凡真实感的新颖视图。然而，随着RF的使用越来越广泛，对保持不同视角连贯性的有效编辑技术的需求变得显而易见。当前的方法主要依赖于每帧2D图像修复，这往往无法保持视图之间的一致性，从而损害了编辑RF场景的真实感。在这项工作中，我们引入了一种新的RF编辑流水线，通过只需要修复一个参考图像来显著提高一致性。然后，使用基于深度的方法将该图像投影到多个视图上，有效地减少了每帧修复中观察到的不一致性。然而，投影通常假设视图之间的光度一致性，这在现实世界的设置中通常是不切实际的。为了适应照明和视点的真实变化，我们的管道通过生成修复图像的多个方向变体来调整投影视图的外观，从而适应不同的光度条件。此外，我们提出了一种有效且稳健的多视图对象分割方法，作为我们管道的宝贵副产品。大量实验表明，我们的方法在保持视图之间的内容一致性和提高视觉质量方面明显优于现有框架。更多结果请访问https://vulab-ai.github.io/View-consistent_Object_Removal_in_Radiance_Fields. et.al.|[2408.02100](http://arxiv.org/abs/2408.02100)|null|
|**2024-08-04**|**PanicleNeRF: low-cost, high-precision in-field phenotypingof rice panicles with smartphone**|水稻穗部性状显著影响粮食产量，使其成为水稻表型研究的主要目标。然而，大多数现有技术仅限于受控的室内环境，难以在自然生长条件下捕捉水稻穗部特征。在这里，我们开发了PanicleNeRF，这是一种新方法，可以使用智能手机在田间高精度、低成本地重建水稻穗三维（3D）模型。该方法将大模型Segment Anything model（SAM）和小模型You Only Look Once version 8（YOLOv8）相结合，实现了水稻穗图像的高精度分割。然后，使用具有2D分割的图像，采用NeRF技术进行3D重建。最后，对得到的点云进行处理，成功提取穗部特征。结果表明，PanicleNeRF有效地解决了2D图像分割任务，实现了86.9%的平均F1分数和79.8%的平均联合交叉（IoU），与YOLOv8相比，边界重叠（BO）性能几乎翻了一番。在点云质量方面，PanicleNeRF明显优于传统的SfM MVS（运动结构和多视图立体）方法，如COLMAP和Metashape。然后精确提取穗长，籼稻的rRMSE为2.94%，粳稻为1.75%。根据3D点云估算的穗体积与粒数（籼稻R2=0.85，粳稻R2=0.82）和粒重（籼稻0.80，粳稻0.76）密切相关。该方法为水稻穗的田间表型高通量提供了一种低成本的解决方案，加快了水稻育种的效率。 et.al.|[2408.02053](http://arxiv.org/abs/2408.02053)|null|
|**2024-08-02**|**Enhanced Knee Kinematics: Leveraging Deep Learning and Morphing Algorithms for 3D Implant Modeling**|植入膝关节模型的准确重建在骨科手术和生物医学工程中至关重要，可以加强术前计划，优化植入物设计，改善手术结果。传统方法依赖于劳动密集型和易出错的手动分割。本研究提出了一种使用机器学习（ML）算法和变形技术对植入膝关节模型进行精确3D重建的新方法。该方法首先获取术前成像数据，如患者膝关节的荧光透视或X射线图像。然后训练卷积神经网络（CNN）来自动分割植入组件的股骨轮廓，大大减少了人工劳动并确保了高精度。分割后，变形算法使用分割数据和生物力学原理生成植入膝关节的个性化3D模型。该算法考虑植入物的位置、大小和方向来模拟膝关节的形状。通过将形态数据与植入物特定参数相结合，重建的模型准确地反映了患者的植入物解剖结构和配置。通过定量评估，包括与地面实况数据和现有技术的比较，证明了该方法的有效性。在涉及各种植入物类型的19个测试案例中，与手动分割相比，基于机器学习的分割方法显示出更高的准确性和一致性，平均RMS误差为0.58+/-0.14 mm。这项研究通过为植入膝关节模型的自动重建提供一个强大的框架，推动了骨科手术的发展。利用机器学习和变形算法，临床医生和研究人员可以获得对患者特定膝关节解剖、植入物生物力学和手术计划的宝贵见解，从而改善患者预后并提高护理质量。 et.al.|[2408.01557](http://arxiv.org/abs/2408.01557)|null|
|**2024-08-07**|**IG-SLAM: Instant Gaussian SLAM**|3D高斯散点最近显示出有希望的结果，作为SLAM系统中神经隐式表示的替代场景表示。然而，目前的方法要么缺乏密集的深度图来监督绘图过程，要么缺乏考虑环境规模的详细训练设计。为了解决这些缺点，我们提出了IG-SLAM，这是一种仅包含RGB的密集SLAM系统，它采用鲁棒的密集SLAN方法进行跟踪，并将其与高斯散斑相结合。使用跟踪提供的精确姿态和密集深度构建环境的3D地图。此外，我们在地图优化中利用深度不确定性来改进3D重建。我们在映射优化中的衰减策略增强了收敛性，并允许系统在单个过程中以每秒10帧的速度运行。我们通过最先进的仅RGB SLAM系统展示了具有竞争力的性能，同时实现了更快的运行速度。我们展示了在Replica、TUM-RGBD、ScanNet和EuRoC数据集上的实验。该系统在大规模序列中实现了逼真的3D重建，特别是在EuRoC数据集中。 et.al.|[2408.01126](http://arxiv.org/abs/2408.01126)|null|
|**2024-08-02**|**Structure from Motion-based Motion Estimation and 3D Reconstruction of Unknown Shaped Space Debris**|随着近几十年来航天器发射数量的增加，空间碎片问题日益变得至关重要。为了实现可持续的空间利用，持续清除空间碎片是人类面临的最严峻问题。为了最大限度地提高轨道碎片捕获任务的可靠性，对目标进行精确的运动估计至关重要。空间碎片已经失去了姿态和轨道控制能力，由于断裂，其形状未知。本文提出了一种基于运动结构的算法，用于在资源有限的情况下进行未知形状空间碎片运动估计，其中只需要2D图像作为输入。然后，该方法同时输出未知物体的重建形状和目标与相机之间的相对姿态轨迹，用于估计目标的运动。该方法通过二维气浮试验台微重力实验和三维运动学模拟生成的真实图像数据集进行了定量验证。 et.al.|[2408.01035](http://arxiv.org/abs/2408.01035)|null|
|**2024-08-05**|**UlRe-NeRF: 3D Ultrasound Imaging through Neural Rendering with Ultrasound Reflection Direction Parameterization**|三维超声成像是一项广泛应用于医学诊断的关键技术。然而，传统的3D超声成像方法具有固定分辨率、低存储效率和上下文连接不足等局限性，导致处理复杂伪影和反射特性的性能较差。最近，基于NeRF（神经辐射场）的技术在视图合成和3D重建方面取得了重大进展，但在高质量超声成像方面仍存在研究差距。为了解决这些问题，我们提出了一种新的模型UlRe-NeRF，它将隐式神经网络和显式超声体积渲染结合到一个超声神经渲染架构中。该模型结合了反射方向参数化和谐波编码，使用方向MLP模块生成视图相关的高频反射强度估计，并使用空间MLP模块产生介质的物理特性参数。这些参数用于体绘制过程中，以准确再现超声波在介质中的传播和反射行为。实验结果表明，UlRe-NeRF模型显著提高了高保真超声图像重建的真实性和准确性，特别是在处理复杂介质结构时。 et.al.|[2408.00860](http://arxiv.org/abs/2408.00860)|null|

<p align=right>(<a href=#updated-on-20240808>back to top</a>)</p>

## Diffusion

|Publish Date|Title|Abstract|PDF|Code|
|---|---|---|---|---|
|**2024-08-07**|**Dynamical patterns in active-passive particle mixtures with non-reciprocal interactions: Exact hydrodynamic analysis**|动力学模式的形成是非平衡物理系统最显著的特征之一。最近的研究表明，这种模式通常是由违反牛顿第三定律的力引起的，即非互易相互作用。这些非平衡现象对现代理论提出了挑战。在这里，我们介绍了一种具有非互易有效相互作用的主动（自推进）和被动（扩散）粒子的模型混合物，可以进行精确的数学分析。我们利用最先进的方法推导出粒子密度的精确流体动力学方程。我们研究了由此产生的集体行为，包括均匀态的线性稳定性和大系统中的相位共存。这揭示了一个新的相图，其中与主动相分离相关的旋节通过相关的双峰突出，预示着动态稳态的出现。我们在大系统尺寸的热力学极限下分析了这些状态，例如，表明尖锐的界面可以以有限的速度传播，但传播相分离态是被禁止的。该模型的数学可处理性使其能够得出超越粒子模型或场论数值模拟的精确新结论。 et.al.|[2408.03932](http://arxiv.org/abs/2408.03932)|null|
|**2024-08-07**|**Fluctuation of coherences in noisy mesoscopic quantum systems with diffusive transport**|本文的动机是找到具有扩散输运性质的介观量子系统中量子相干效应的波动流体动力学描述。相干效应被嵌入相干（两点格林函数）中，我们将其作为这种理论的基石。我们的方法相当数学化，与具体实验无关。我们研究了量子对称简单排斥过程（QSSEP），这是一个描述一维晶格上噪声自由费米子输运的潜在标志性模型，它具有捕获我们感兴趣的最小结构：长程相干性和扩散输运。平均而言，QSSEP简化为对称简单排除过程（SSEP），这是一个经典的玩具模型，在宏观波动理论的发展中很重要，是对经典系统中扩散输运的波动流体动力学描述。研究QSSEP，我们希望在宏观涨落理论的量子相干扩展方面取得进展。本文总结了过去三年中我们在QSSEP方面取得的许多成果，如动力学方程和流体动力学尺度相干相关函数的精确稳态解，QSSEP中纠缠的分布，以及为什么QSSEP可能是更通用介观量子系统的有效噪声描述的论点。其中许多结果是由于QSSEP中相干性的统计性质与自由概率理论之间的关系。我们用了一整章来讨论这种关系，并作为副产品，提出了一种表征一大类结构化随机矩阵子块谱的方法。 et.al.|[2408.03917](http://arxiv.org/abs/2408.03917)|null|
|**2024-08-07**|**Disorder-induced delocalization and reentrance in a Chern-Hopf insulator**|Chern-Hopf绝缘体是一种非常规的三维拓扑绝缘体，具有体隙和无间隙边界态，不受全局离散对称性的保护。这项研究调查了它在混乱中的命运。通过使用大规模数值模拟和自洽玻恩近似分析表面态和零能量堆积态密度，我们发现它在中等无序度之前是稳定的。无序的Chern-Hopf绝缘体表现出可重入行为：无序首先增强拓扑相，然后驱动其穿过绝缘体扩散金属过渡。我们通过体密度、参与熵和两端电导的有限尺寸标度来检验相关的临界指数。我们估计了相关长度指数 $\nu\simeq 1.0（1）$ ，与干净的二维Chern普适性一致，与整数量子霍尔指数不同。 et.al.|[2408.03908](http://arxiv.org/abs/2408.03908)|null|
|**2024-08-07**|**A first-order hyperbolic reformulation of the Cahn-Hilliard equation**|本文提出了Cahn-Hilliard方程的一阶双曲型新表述。该模型是通过将本文作者早些时候提出的增广拉格朗日技术与经典Cattaneo型弛豫相结合而获得的，该弛豫允许将扩散方程重新表述为具有刚性弛豫源项的增广一阶双曲系统。根据原始方程，所提出的系统被证明是双曲的，并且承认李雅普诺夫泛函。提出了一种基于保守半隐式有限差分求解原始Cahn-Hilliard方程的新数值方案，而双曲系统则采用经典的二阶MUSCL Hancock型有限体积方案进行数值求解。所提出的方法通过一组经典基准进行了验证，如旋节分解、奥斯特瓦尔德成熟和精确稳态解。 et.al.|[2408.03862](http://arxiv.org/abs/2408.03862)|null|
|**2024-08-07**|**Data Generation Scheme for Thermal Modality with Edge-Guided Adversarial Conditional Diffusion Model**|在具有挑战性的低光照和恶劣天气条件下，热视觉算法，特别是物体检测，表现出了显著的潜力，与可见视觉算法经常遇到的困难形成鲜明对比。然而，由深度学习模型驱动的热视觉算法的有效性仍然受到可用训练数据样本不足的限制。为此，本文介绍了一种称为边缘引导条件扩散模型的新方法。该框架旨在利用从可见图像中提取的边缘信息，在像素级生成精心对齐的伪热图像。通过利用边缘作为可见域的上下文线索，扩散模型实现了对生成图像中对象描绘的精细控制。为了减轻那些不应出现在热域中的可见特定边缘信息的影响，提出了一种两阶段模态对抗训练策略，通过区分可见和热模态将其从生成的图像中过滤出来。在LLVIP上进行的大量实验表明，ECDM在图像生成质量方面优于现有的最先进方法。 et.al.|[2408.03748](http://arxiv.org/abs/2408.03748)|null|
|**2024-08-07**|**Flexible Bayesian Last Layer Models Using Implicit Priors and Diffusion Posterior Sampling**|贝叶斯最后一层（BLL）模型仅关注神经网络输出层的不确定性，其性能与更复杂的贝叶斯模型相当。然而，在贝叶斯最后一层（BLL）模型中，使用高斯先验作为最后一层权重限制了它们在面对非高斯、异常值丰富或高维数据集时的表达能力。为了解决这一不足，我们引入了一种将扩散技术和隐式先验相结合的新方法，用于贝叶斯最后一层权重的变分学习。该方法利用隐式分布对BLL中的权重先验进行建模，并结合扩散采样器来近似真实的后验预测，从而建立了一种全面的贝叶斯先验和后验估计策略。通过提供显式和计算高效的变分下限，我们的方法旨在增强BLL模型的表达能力，提高模型精度、校准和分布外检测能力。通过详细的探索和实验验证，我们展示了该方法在确保计算效率的同时提高预测准确性和不确定性量化的潜力。 et.al.|[2408.03746](http://arxiv.org/abs/2408.03746)|null|
|**2024-08-07**|**Unsupervised Detection of Fetal Brain Anomalies using Denoising Diffusion Models**|先天性脑畸形是影响胎儿发育的最常见的胎儿异常之一。以前的超声图像异常检测方法基于监督学习，依赖于手动注释，并且有可能遗漏代表性不足的类别。在这项工作中，我们将胎儿大脑异常检测构建为使用扩散模型的无监督任务。为此，我们采用了一种基于修复的噪声不可知异常检测方法，该方法使用来自多个噪声水平的扩散重建胎儿大脑图像来识别异常。我们的方法只需要正常的胎儿大脑超声图像进行训练，解决了异常数据可用性有限的问题。我们在真实世界临床数据集上的实验表明，使用无监督方法检测胎儿大脑异常具有潜力。此外，我们全面评估了不同噪声类型如何影响胎儿异常检测领域的扩散模型。 et.al.|[2408.03654](http://arxiv.org/abs/2408.03654)|null|
|**2024-08-07**|**Superdiffusion of energetic particles at shocks: A Lévy Flight model for acceleration**|在日光层中，观察到幂律粒子分布，例如行星际激波的上游，这可能是由超扩散输运引起的。这种非高斯输运机制可能是由间歇磁场结构引起的。最近，我们发现，L’vy飞行模型再现了冲击时的观测特征：上游的幂律分布和冲击时强度的增强。我们扩展了L’vy飞行模型，以研究超扩散输运对冲击下粒子加速度的影响。将加速度时间尺度和谱斜率与高斯扩散和L’vy游走模型进行了比较。分数输运方程是通过用相应的随机微分方程对数密度进行采样来求解的，该随机微分方程由α稳定的L’vy分布驱动。对于高斯和超扩散输运，我们使用CRPropa 3.2的修改版本。我们得到了常数和能量依赖的反常扩散的数密度和能谱，并发现与高斯扩散的情况相比，冲击下的能谱更硬，加速度更快。光谱斜率甚至比L’vy行走的预测更难。超扩散输运的L’vy飞行模型导致了日光层中的观测特征。我们进一步表明，超扩散输运通过改变逃离冲击的概率来影响加速过程。考虑到激波几何形状和磁场结构，L’vy飞行模型的灵活性允许在未来进行进一步的研究。 et.al.|[2408.03638](http://arxiv.org/abs/2408.03638)|null|
|**2024-08-07**|**TALE: Training-free Cross-domain Image Composition via Adaptive Latent Manipulation and Energy-guided Optimization**|我们提出了TALE，这是一种新的无训练框架，利用文本到图像扩散模型的生成能力来解决跨域图像合成任务，该任务侧重于将用户指定的对象完美地整合到指定的视觉环境中，而不管域差异如何。以前的方法通常涉及在定制数据集上训练辅助网络或微调扩散模型，这些方法成本高昂，可能会破坏预训练扩散模型的鲁棒文本和视觉先验。最近的一些研究试图通过提出无需训练的解决方法来打破这一障碍，这些方法依赖于操纵注意力图来隐含地驯服去噪过程。然而，通过注意力图进行构图并不一定能产生理想的构图结果。这些方法只能保留一些语义信息，通常无法保留输入对象的身份特征，或者在生成的图像中表现出有限的背景对象风格适应。相比之下，TALE是一种直接在潜在空间上操作的新方法，为解决这些问题的构图过程提供明确有效的指导。具体来说，我们为TALE配备了两种机制，称为自适应潜在操纵和能量引导潜在优化。前者通过直接利用相应时间步的背景和前景延迟来制定有利于启动和指导构图过程的噪声延迟，后者利用指定的能量函数来进一步优化符合特定条件的中间延迟，以补充前者，从而产生所需的最终结果。我们的实验表明，TALE超越了先前的基线，在各种真实感和艺术领域的图像引导构图中达到了最先进的性能。 et.al.|[2408.03637](http://arxiv.org/abs/2408.03637)|null|
|**2024-08-07**|**"The Strength of Weak Ties" Varies Across Viral Channels**|通过社交网络传播新信息对于拆除回音室和促进创新至关重要。我们的研究考察了两种主要类型的病毒渠道，特别是直接消息（DM）和广播（BC），如何影响在社交网络上传播新信息时众所周知的“弱关系强度”。我们进行了一项大规模的实证分析，考察了一个主要社交媒体平台上50万用户在两个月内的分享行为。我们的研究结果表明，与BC相比，DM传输新信息的能力更强，尽管DM通常涉及更强的联系。此外，“弱联系的强度”仅在不列颠哥伦比亚省明显，而在DM中则不明显，因为弱联系不会传递更多新颖的信息。我们的机制分析表明，发送者和接收者的内容选择取决于联系强度，这有助于观察到这两个渠道之间的差异。这些发现既扩展了我们对当代弱联系理论的理解，也扩展了我们如何在社交网络中传播新信息的知识。 et.al.|[2408.03579](http://arxiv.org/abs/2408.03579)|null|

<p align=right>(<a href=#updated-on-20240808>back to top</a>)</p>

## NeRF

|Publish Date|Title|Abstract|PDF|Code|
|---|---|---|---|---|
|**2024-08-07**|**Compact 3D Gaussian Splatting for Static and Dynamic Radiance Fields**|3D高斯飞溅（3DGS）最近成为一种替代表示，它利用基于3D高斯的表示并引入了近似的体积渲染，实现了非常快的渲染速度和有前景的图像质量。此外，后续的研究已成功地将3DGS扩展到动态3D场景，展示了其广泛的应用。然而，由于3DGS及其后续方法需要大量的高斯分布来保持渲染图像的高保真度，这需要大量的内存和存储，因此出现了一个重大的缺点。为了解决这个关键问题，我们特别强调两个关键目标：在不牺牲性能的情况下减少高斯点的数量，以及压缩高斯属性，如视图相关的颜色和协方差。为此，我们提出了一种可学习的掩码策略，该策略在保持高性能的同时显著减少了高斯数。此外，我们提出了一种紧凑但有效的视图相关颜色表示方法，即采用基于网格的神经场，而不是依赖球谐函数。最后，我们学习码本，通过残差矢量量化来紧凑地表示几何和时间属性。通过量化和熵编码等模型压缩技术，我们始终表明，与静态场景的3DGS相比，存储空间减少了25倍以上，渲染速度提高了25倍，同时保持了场景表示的质量。对于动态场景，与现有的最先进方法相比，我们的方法实现了超过12倍的存储效率，并保留了高质量的重建。我们的工作为3D场景表示提供了一个全面的框架，实现了高性能、快速训练、紧凑性和实时渲染。我们的项目页面可在https://maincold2.github.io/c3dgs/. et.al.|[2408.03822](http://arxiv.org/abs/2408.03822)|null|
|**2024-08-07**|**PRTGS: Precomputed Radiance Transfer of Gaussian Splats for Real-Time High-Quality Relighting**|我们提出了高斯斑点的预计算辐射转移（PRTGS），这是一种在低频照明环境中用于高斯斑点的实时高质量重新照明方法，通过预计算3D高斯斑点的辐射转移来捕获柔和的阴影和相互反射。现有的研究表明，在动态照明场景中，3D高斯溅射（3DGS）的效率优于神经场。然而，目前基于3DGS的重新照明方法仍然难以实时计算动态光的高质量阴影和间接照明，导致渲染结果不切实际。我们通过预先计算复杂传递函数（如阴影）所需的昂贵传输模拟来解决这个问题，得到的传递函数表示为每个高斯斑点的密集向量集或矩阵集。我们介绍了针对训练和渲染阶段量身定制的不同预计算方法，以及针对3D高斯斑点的独特光线追踪和间接照明预计算技术，以加快训练速度并计算与环境光相关的准确间接照明。实验分析表明，我们的方法在保持有竞争力的训练时间的同时实现了最先进的视觉质量，并允许以1080p分辨率对动态光和相对复杂的场景进行高质量的实时（30+fps）重新照明。 et.al.|[2408.03538](http://arxiv.org/abs/2408.03538)|null|
|**2024-08-01**|**Neural Octahedral Field: Octahedral prior for simultaneous smoothing and sharp edge regularization**|神经隐式表示，将距离函数参数化为坐标神经场，已成为解决无方向点云表面重建的有前景的前沿。为了确保方向一致，现有的方法侧重于正则化距离函数的梯度，例如将其约束为单位范数，最小化其散度，或将其与对应于零特征值的Hessian特征向量对齐。然而，在存在大扫描噪声的情况下，它们往往要么过拟合噪声输入，要么产生过于平滑的重建。在这项工作中，我们建议利用六面体网格中产生的八面体框架的球谐表示，在一种新的神经场变体——八面体场下指导曲面重建。当约束为平滑时，该字段会自动捕捉到几何特征，并在折痕上插值时自然保留锐角。通过同时拟合和平滑隐式几何旁边的八面体场，它的行为类似于双边滤波，从而在保持锐边的同时实现平滑重建。尽管是纯逐点操作，但我们的方法在广泛的实验中表现优于各种传统和神经方法，并且与需要正常和数据先验的方法非常有竞争力。我们的全面实施可在以下网址获得：https://github.com/Ankbzpx/frame-field. et.al.|[2408.00303](http://arxiv.org/abs/2408.00303)|null|
|**2024-07-30**|**Neural Fields for Continuous Periodic Motion Estimation in 4D Cardiovascular Imaging**|时间分辨三维血流MRI（4D血流MRI）提供了一种独特的非侵入性解决方案，用于可视化和量化主动脉弓等血管中的血流动力学。然而，由于难以获得完整的周期分割，目前大多数动脉4D血流MRI分析方法使用静态动脉壁。为了克服这一局限性，我们提出了一种基于神经场的方法，可以直接估计整个心动周期中连续的周期性壁变形。对于3D+时间成像数据集，我们优化了表示时间依赖速度矢量场（VVF）的隐式神经表示（INR）。ODE求解器用于将VVF集成到变形矢量场（DVF）中，该矢量场可以随着时间的推移使图像、分割掩模或网格变形，从而可视化和量化局部壁运动模式。为了正确反映3D+时间心血管数据的周期性，我们以两种方式施加周期性。首先，通过定期对输入到INR的时间进行编码，从而对VVF进行编码。其次，通过规范DVF。我们证明了这种方法在不同周期模式的合成数据、心电图门控CT和4D血流MRI数据上的有效性。所获得的方法可用于改进4D血流MRI分析。 et.al.|[2407.20728](http://arxiv.org/abs/2407.20728)|null|
|**2024-07-29**|**Aero-Nef: Neural Fields for Rapid Aircraft Aerodynamics Simulations**|本文提出了一种基于隐式神经表示（INR）在网格域上学习稳态流体动力学模拟替代模型的方法。所提出的模型可以直接应用于不同流动条件下的非结构化域，处理非参数3D几何变化，并推广到测试时看不见的形状。基于坐标的公式自然会导致离散化的鲁棒性，从而在计算成本（内存占用和训练时间）和精度之间实现了极好的权衡。该方法在两个工业相关应用中得到了验证：跨音速翼型上二维可压缩流的RANS数据集和三维机翼上表面压力分布的数据集，包括形状、流入条件和控制表面偏转变化。在所考虑的测试用例中，与最先进的图神经网络架构相比，我们的方法实现了三倍多的测试误差，并显著改善了看不见的几何形状的泛化误差。值得注意的是，该方法在RANS跨音速翼型数据集上的推理速度比高保真求解器快五个数量级。代码可在以下网址获得https://gitlab.isae-supaero.fr/gi.catalani/aero-nepf et.al.|[2407.19916](http://arxiv.org/abs/2407.19916)|null|
|**2024-07-26**|**ObjectCarver: Semi-automatic segmentation, reconstruction and separation of 3D objects**|隐式神经场在从多幅图像重建3D表面方面取得了显著进展；然而，在分离场景中的单个对象时，他们遇到了挑战。之前的工作试图通过引入一个框架来解决这个问题，该框架为N个对象中的每一个同时训练单独的带符号距离场（SDF），并使用正则化项来防止对象重叠。然而，所有这些方法都需要提供分割掩模，这并不总是容易获得的。我们介绍了我们的方法ObjectCarver，来解决在单个视图中从点击输入中分离对象的问题。给定摆出的多视图图像和一组用户输入点击来提示分割单个对象，我们的方法将场景分解为单独的对象，并为每个对象重建高质量的3D表面。我们引入了一个损失函数，可以防止漂浮物，避免因遮挡而造成不适当的雕刻。此外，我们引入了一种新的场景初始化方法，与之前的方法相比，该方法在保留几何细节的同时显著加快了过程。尽管不需要地面真实掩模或单眼线索，但我们的方法在定性和定量上都优于基线。此外，我们引入了一个新的基准数据集进行评估。 et.al.|[2407.19108](http://arxiv.org/abs/2407.19108)|null|
|**2024-07-24**|**Neural field equations with time-periodic external inputs and some applications to visual processing**|这项工作的目的是为研究视觉处理任务中的闪烁输入提供一个数学框架。当与几何图案结合时，这些输入会影响并诱发有趣的心理物理现象，如麦凯效应和比洛克-邹效应，在这些效应中，受试者感知到通常由闪烁频率调制的特定余像。由于输入的对称破缺结构，经典分叉理论和多尺度分析技术在我们的背景下不是很有效。因此，我们采用了一种基于Amari型神经场控制理论的输入-输出框架的方法。这使我们能够证明，当受到周期性输入的驱动时，动态会收敛到周期性状态。此外，我们研究了在哪些假设下，这些非线性动力学可以有效地线性化，在这种情况下，我们提出了短程兴奋性和远程抑制性神经元相互作用的积分核的精确近似值。最后，对于集中在具有闪烁背景的视野中心的输入，我们直接将余像中出现的虚幻轮廓的宽度与闪烁频率和抑制强度联系起来。 et.al.|[2407.17294](http://arxiv.org/abs/2407.17294)|null|
|**2024-07-23**|**Fluorescence Diffraction Tomography using Explicit Neural Fields**|从荧光图像中求解3D折射率（RI）可以提供有关生物样本的荧光和相位信息。然而，在大体积、高分辨率和反射模式下准确检索部分相干光的相位以重建无标签相位物体的未知RI仍然具有挑战性。为了应对这一挑战，我们开发了具有显式神经场的荧光衍射断层扫描（FDT），可以从散焦荧光散斑图像重建3D RI。使用FDT成功重建3D RI依赖于四个关键组件：粗到细建模、自校准、差分多层渲染模型和部分相干掩模。具体而言，显式表示与粗到细建模有效地集成在一起，以实现高速、高分辨率的重建。此外，我们将多层方程推进到微分多层渲染模型，这使得系统的外部和内部参数能够进行自校准。自校准有助于高精度的正向图像预测和RI重建。部分相干掩模是数字掩模，用于准确有效地解决相干光模型和部分相干光数据之间的差异。FDT成功地从荧光图像中重建了24个z $层上1024$×1024像素的530$×530$×300$μm^3$ 体积的3D培养无标记3D MuSCs管的RI，证明了在体外对体积庞大和异质的生物样本进行高保真3D RI重建。 et.al.|[2407.16657](http://arxiv.org/abs/2407.16657)|null|
|**2024-07-22**|**Iterative approach to reconstructing neural disparity fields from light-field data**|本研究提出了一种神经视差场（NDF），该场基于神经场建立了场景视差的隐式连续表示，并采用迭代方法解决了从光场数据重建NDF的逆问题。NDF能够无缝和精确地表征三维场景中的视差变化，并可以以任何任意分辨率对视差进行离散化，克服了传统视差图容易出现采样误差和插值不准确的局限性。所提出的NDF网络架构利用哈希编码结合多层感知器来捕获纹理级别的详细差异，从而增强其表示复杂场景几何信息的能力。通过利用光场数据中固有的空间角度一致性，开发了一种可微分正向模型，用于从光场数据生成中心视图图像。基于正向模型，建立了一种使用可微传播算子的NDF重建逆问题的优化方案。此外，在优化方案中，采用迭代求解方法重建NDF，该方法不需要训练数据集，适用于各种采集方法捕获的光场数据。实验结果表明，使用所提出的方法可以从光场数据中重建高质量的NDF。NDF可以有效地恢复高分辨率视差，证明了其隐式、连续表示场景视差的能力。 et.al.|[2407.15380](http://arxiv.org/abs/2407.15380)|null|
|**2024-07-19**|**Contextual modulation of language comprehension in a dynamic neural model of lexical meaning**|我们提出并计算实现了一个词汇意义的动态神经模型，并对其行为预测进行了实验测试。我们使用英语词汇“have”作为测试用例来演示模型的架构和行为，重点关注其多义词的使用。在该模型中，“have”映射到由两个连续的概念维度（连通性和控制不对称性）定义的语义空间，这两个维度之前被提出用于参数化语言的概念系统。映射被建模为表示词条的神经节点和表示概念维度的神经场之间的耦合。虽然词汇知识被建模为稳定的耦合模式，但实时词汇意义检索被建模为神经激活模式在对应于语义解释或阅读的亚稳态之间的运动。模型模拟捕捉到了两个先前报道的实证观察结果：（1）词汇语义解释的语境调制，以及（2）这种调制幅度的个体差异。模拟还产生了一种新的预测，即句子阅读时间和可接受性之间的试验关系应该根据上下文进行调节。结合自定进度阅读和可接受性判断的实验复制了之前的结果，并证实了新的模型预测。总之，研究结果支持了一种关于词汇多义的新观点：一个词的许多相关含义是亚稳态的神经激活状态，这是由控制连续语义维度解释的神经群体的非线性动力学引起的。 et.al.|[2407.14701](http://arxiv.org/abs/2407.14701)|null|

<p align=right>(<a href=#updated-on-20240808>back to top</a>)</p>

[contributors-shield]: https://img.shields.io/github/contributors/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[contributors-url]: https://github.com/Vincentqyw/cv-arxiv-daily/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[forks-url]: https://github.com/Vincentqyw/cv-arxiv-daily/network/members
[stars-shield]: https://img.shields.io/github/stars/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[stars-url]: https://github.com/Vincentqyw/cv-arxiv-daily/stargazers
[issues-shield]: https://img.shields.io/github/issues/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[issues-url]: https://github.com/Vincentqyw/cv-arxiv-daily/issues

