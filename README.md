[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]

## Updated on 2024.08.10
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
|**2024-08-08**|**Sampling for View Synthesis: From Local Light Field Fusion to Neural Radiance Fields and Beyond**|捕捉和渲染复杂现实世界场景的新颖视图是计算机图形学和视觉领域的一个长期问题，在增强现实和虚拟现实、沉浸式体验和3D摄影中都有应用。深度学习的出现使这一领域取得了革命性的进步，传统上称为基于图像的渲染。然而，以前的方法需要难以处理的密集视图采样，或者对于用户应该如何采样场景视图以可靠地渲染高质量的新视图提供很少或根本没有指导。局部光场融合提出了一种用于从采样视图的不规则网格进行实际视图合成的算法，该算法首先通过多平面图像场景表示将每个采样视图扩展为局部光场，然后通过混合相邻的局部光场来渲染新的视图。至关重要的是，我们扩展了传统的全光采样理论，得出了一个界限，该界限精确地指定了用户在使用我们的算法时应该对给定场景的视图进行多密集采样。我们实现了奈奎斯特速率视图采样的感知质量，同时使用的视图减少了4000倍。后续的发展为深度学习带来了新的场景表示，特别是神经辐射场，但从少量图像进行稀疏视图合成的问题只会变得越来越重要。我们重申了最近关于稀疏甚至单图像视图合成的一些结果，同时提出了规定采样准则是否适用于新一代基于图像的渲染算法的问题。 et.al.|[2408.04586](http://arxiv.org/abs/2408.04586)|null|
|**2024-08-08**|**Evaluating Modern Approaches in 3D Scene Reconstruction: NeRF vs Gaussian-Based Methods**|本研究探索了神经辐射场（NeRF）和基于高斯的方法在3D场景重建中的能力，将这些现代方法与传统的同步定位和映射（SLAM）系统进行了对比。利用Replica和ScanNet等数据集，我们根据跟踪精度、映射保真度和视图合成来评估性能。研究结果表明，NeRF在视图合成方面表现出色，在从现有数据生成新视角方面提供了独特的能力，尽管处理速度较慢。相反，基于高斯的方法提供了快速的处理和显著的表现力，但缺乏全面的场景完成。通过全局优化和循环闭合技术的增强，NICE-SLAM和SplaTAM等新方法不仅在鲁棒性方面超越了ORB-SLAM2等旧框架，而且在动态和复杂环境中表现出卓越的性能。这种比较分析将理论研究与实际意义联系起来，为各种现实世界应用中鲁棒3D场景重建的未来发展提供了线索。 et.al.|[2408.04268](http://arxiv.org/abs/2408.04268)|null|
|**2024-08-07**|**3iGS: Factorised Tensorial Illumination for 3D Gaussian Splatting**|使用3D高斯作为辐射场的表示，实现了实时渲染速度下的高质量新颖视图合成。然而，选择将每个高斯光束的出射辐射独立地优化为球面谐波会导致不令人满意的视景相关效果。为了应对这些局限性，我们的工作，3D高斯散斑的因子化张量照明，或3iGS，提高了3D高斯散场（3DGS）的渲染质量。3iGS不是优化单个出射辐射参数，而是通过将出射辐射表示为局部照明场和双向反射分布函数（BRDF）特征的函数来增强3DGS视图相关效果。我们通过张量分解表示优化连续入射光照场，同时分别微调每个3D高斯光照场相对于该光照场的BRDF特征。我们的方法显著提高了3DGS的镜面视图相关效果的渲染质量，同时保持了快速的训练和渲染速度。 et.al.|[2408.03753](http://arxiv.org/abs/2408.03753)|null|
|**2024-08-06**|**RayGauss: Volumetric Gaussian-Based Ray Casting for Photorealistic Novel View Synthesis**|基于微分体绘制的方法在新的视图合成方面取得了重大进展。一方面，创新的方法用局部参数化结构取代了神经辐射场（NeRF）网络，在合理的时间内实现了高质量的渲染。另一方面，这些方法使用可微分溅射而不是NeRF的光线投射来使用高斯核快速优化辐射场，从而可以对场景进行精细调整。然而，不规则间隔内核的可微分光线投射几乎没有得到探索，而飞溅尽管可以实现快速渲染时间，但容易受到清晰可见的伪影的影响。我们的工作通过提供发射辐射c和密度{\sigma}的物理一致公式来缩小这一差距，该公式用与球面高斯/谐波相关的高斯函数分解，用于所有频率的色度表示。我们还介绍了一种方法，该方法使用逐片积分辐射场并利用BVH结构的算法，实现了不规则分布高斯分布的可微分光线投射。这使得我们的方法能够很好地适应场景，同时避免飞溅的伪影。因此，与最先进的技术相比，我们实现了卓越的渲染质量，同时保持了合理的训练时间，并在Blender数据集上实现了25 FPS的推理速度。带有视频和代码的项目页面：https://raygauss.github.io/ et.al.|[2408.03356](http://arxiv.org/abs/2408.03356)|null|
|**2024-08-06**|**Efficient NeRF Optimization -- Not All Samples Remain Equally Hard**|我们提出了一种在线硬样本挖掘的应用，用于高效训练神经辐射场（NeRF）。NeRF模型为许多3D重建和渲染任务提供了最先进的质量，但需要大量的计算资源。NeRF网络参数内场景信息的编码需要随机采样。我们观察到，在训练过程中，大部分计算时间和内存使用都花在处理已经学习的样本上，这不再对模型更新产生显著影响。我们将随机样本的反向传递确定为优化过程中的计算瓶颈。因此，我们在推理模式下执行第一次前向传递，作为对硬样本的相对低成本搜索。随后，构建计算图，并仅使用硬样本更新NeRF网络参数。为了证明所提出方法的有效性，我们将我们的方法应用于Instant NGP，使视图合成质量比基线有了显著提高（平均每训练时间提高1 dB，或加速2倍以达到相同的PSNR水平），同时仅使用硬样本构建计算图可节省约40%的内存。由于我们的方法只与网络模块交互，我们希望它能得到广泛应用。 et.al.|[2408.03193](http://arxiv.org/abs/2408.03193)|null|
|**2024-08-06**|**MGFs: Masked Gaussian Fields for Meshing Building based on Multi-View Images**|在过去的几十年里，基于图像的建筑表面重建引起了广泛的研究兴趣，并已应用于遗产保护、建筑规划等各个领域。与传统的摄影测量和基于NeRF的解决方案相比，最近，基于高斯场的方法因其高效的训练和详细的3D信息保存，在生成表面网格方面显示出巨大的潜力。然而，大多数基于高斯场的方法都是用所有图像像素训练的，包括建筑和非建筑区域，这会导致建筑网格的显著噪声和时间效率的退化。本文提出了一种新的框架——掩模高斯场（MGF），旨在以一种时间高效的方式为建筑物生成精确的表面重建。该框架首先应用EfficientSAM和COLMAP来生成建筑的多级掩模和相应的掩模点云。随后，通过整合两种创新损失来训练掩蔽高斯场：一种是专注于构建建筑区域的多级感知掩蔽损失，另一种是旨在增强不同掩模之间边界细节的边界损失。最后，我们改进了基于掩模高斯球的四面体表面网格提取方法。对无人机图像的综合实验表明，与传统方法和几种基于NeRF和高斯的SOTA解决方案相比，我们的方法显著提高了建筑表面重建的准确性和效率。值得注意的是，作为副产品，建筑的新颖视图合成还有额外的收益。 et.al.|[2408.03060](http://arxiv.org/abs/2408.03060)|null|
|**2024-08-05**|**UlRe-NeRF: 3D Ultrasound Imaging through Neural Rendering with Ultrasound Reflection Direction Parameterization**|三维超声成像是一项广泛应用于医学诊断的关键技术。然而，传统的3D超声成像方法具有固定分辨率、低存储效率和上下文连接不足等局限性，导致处理复杂伪影和反射特性的性能较差。最近，基于NeRF（神经辐射场）的技术在视图合成和3D重建方面取得了重大进展，但在高质量超声成像方面仍存在研究差距。为了解决这些问题，我们提出了一种新的模型UlRe-NeRF，它将隐式神经网络和显式超声体积渲染结合到一个超声神经渲染架构中。该模型结合了反射方向参数化和谐波编码，使用方向MLP模块生成视图相关的高频反射强度估计，并使用空间MLP模块产生介质的物理特性参数。这些参数用于体绘制过程中，以准确再现超声波在介质中的传播和反射行为。实验结果表明，UlRe-NeRF模型显著提高了高保真超声图像重建的真实性和准确性，特别是在处理复杂介质结构时。 et.al.|[2408.00860](http://arxiv.org/abs/2408.00860)|null|
|**2024-08-01**|**EmoTalk3D: High-Fidelity Free-View Synthesis of Emotional 3D Talking Head**|我们提出了一种合成具有可控情绪的3D对话头的新方法，该方法具有增强的嘴唇同步和渲染质量。尽管在该领域取得了重大进展，但现有方法仍然存在多视图一致性和缺乏情感表达的问题。为了解决这些问题，我们收集了带有校准的多视图视频、情感注释和每帧3D几何的EmoTalk3D数据集。通过在EmoTalk3D数据集上进行训练，我们提出了一个\textit{“语音到几何到外观”}映射框架，该框架首先从音频特征预测忠实的3D几何序列，然后从预测的几何中合成由4D高斯表示的3D说话头的外观。该外观进一步被分解为规范高斯和动态高斯，从多视图视频中学习，并融合以渲染自由视图说话的头部动画。此外，我们的模型能够在生成的说话头中实现可控的情绪，并且可以在宽范围的视图中呈现。我们的方法在嘴唇运动生成中表现出改进的渲染质量和稳定性，同时捕获了动态面部细节，如皱纹和微妙的表情。实验证明了我们的方法在生成高保真度和情绪可控的3D对话头方面的有效性。代码和EmoTalk3D数据集发布于https://nju-3dv.github.io/projects/EmoTalk3D. et.al.|[2408.00297](http://arxiv.org/abs/2408.00297)|null|
|**2024-08-01**|**Head360: Learning a Parametric 3D Full-Head for Free-View Synthesis in 360°**|创建人类头部的360度参数模型是一项非常具有挑战性的任务。虽然最近的进展已经证明了利用合成数据构建此类参数化头部模型的有效性，但它们在表情驱动动画、发型编辑和基于文本的修改等关键领域的性能仍然不足。在本文中，我们构建了一个艺术家设计的高保真人头数据集，并提出从中创建一个新的参数化360度可渲染参数化人头模型。我们的方案将面部运动/形状和面部外观解耦，分别由经典的参数化3D网格模型和附加的神经纹理表示。我们进一步提出了一种分解发型和面部外观的训练方法，允许自由交换发型。提出了一种基于单图像输入的具有高泛化和保真度的反演拟合方法。据我们所知，我们的模型是第一个在单个模型中实现360度自由视图合成、基于图像的拟合、外观编辑和动画的参数化3D全头模型。实验表明，面部运动和外观在参数空间中很好地解耦，从而在渲染和动画质量方面提高了SOTA的性能。代码和SynHead100数据集发布于https://nju-3dv.github.io/projects/Head360. et.al.|[2408.00296](http://arxiv.org/abs/2408.00296)|null|
|**2024-08-01**|**LoopSparseGS: Loop Based Sparse-View Friendly Gaussian Splatting**|尽管原始的3D高斯散点（3DGS）实现了逼真的新视图合成（NVS）性能，但其渲染质量在稀疏输入视图下会显著降低。这种性能下降主要是由于稀疏输入生成的初始点数量有限、训练过程中的监督不足以及超大高斯椭球体的正则化不足造成的。为了解决这些问题，我们提出了LoopSparseGS，这是一个基于循环的3DGS框架，用于稀疏新颖视图合成任务。具体来说，我们提出了一种基于循环的渐进高斯初始化（PGI）策略，该策略可以在训练过程中使用渲染的伪图像迭代加密初始化的点云。然后，利用运动结构的稀疏可靠深度和基于窗口的密集单眼深度，通过提出的深度对齐正则化（DAR）提供精确的几何监督。此外，我们引入了一种新的稀疏友好采样（SFS）策略来处理导致大像素误差的超大高斯椭球。在四个数据集上的综合实验表明，在各种图像分辨率的室内、室外和对象级场景中，LoopSparseGS在稀疏输入新视图合成方面优于现有的最先进方法。 et.al.|[2408.00254](http://arxiv.org/abs/2408.00254)|null|

<p align=right>(<a href=#updated-on-20240810>back to top</a>)</p>

## 3D Reconstruction

|Publish Date|Title|Abstract|PDF|Code|
|---|---|---|---|---|
|**2024-08-06**|**LumiGauss: High-Fidelity Outdoor Relighting with 2D Gaussian Splatting**|使用无约束的照片集将照明与几何体解耦是出了名的挑战。解决这个问题将使许多用户受益，因为创建复杂的3D资产需要数天的体力劳动。许多先前的工作都试图解决这个问题，但往往以牺牲输出保真度为代价，这对这些方法的实用性提出了质疑。我们介绍了LumiGauss，这是一种通过2D高斯散斑处理场景和环境照明的3D重建的技术。我们的方法可以产生高质量的场景重建，并在新颖的环境地图下实现逼真的照明合成。我们还提出了一种通过利用球面谐波特性来提高室外场景中常见阴影质量的方法。我们的方法有助于与游戏引擎无缝集成，并支持使用快速预计算的辐射传输。我们在NeRF OSR数据集上验证了我们的方法，证明了其优于基线方法的性能。此外，LumiGauss在应用新的环境地图时可以合成逼真的图像。 et.al.|[2408.04474](http://arxiv.org/abs/2408.04474)|null|
|**2024-08-08**|**A Review of 3D Reconstruction Techniques for Deformable Tissues in Robotic Surgery**|作为机器人微创手术中一项关键而复杂的任务，使用立体或单眼内窥镜视频重建手术场景具有巨大的临床应用潜力。基于NeRF的技术最近因其隐式重建场景的能力而受到关注。另一方面，基于高斯飞溅的3D-GS显式地使用3D高斯表示场景，并将其投影到2D平面上，以替代NeRF中的复杂体绘制。然而，这些方法在手术场景重建方面面临着挑战，例如推理速度慢、动态场景和手术工具遮挡。这项工作探索和回顾了最先进的（SOTA）方法，讨论了它们的创新和实施原则。此外，我们复制了模型，并对两个数据集进行了测试和评估。测试结果表明，随着这些技术的进步，实现实时、高质量的重建变得可行。 et.al.|[2408.04426](http://arxiv.org/abs/2408.04426)|**[link](https://github.com/epsilon404/surgicalnerf)**|
|**2024-08-07**|**Opening the Black Box of 3D Reconstruction Error Analysis with VECTOR**|从2D图像重建3D场景是一项技术挑战，影响了从地球和行星科学、太空探索到增强现实和虚拟现实的各个领域。通常，重建算法首先识别图像中的共同特征，然后在估计地形形状后最小化重建误差。这个束调整（BA）步骤围绕一个简化的标量值进行优化，该标量值混淆了重建误差的许多可能原因（例如，相机位置和方向的初始估计、照明条件、地形中特征检测的难易程度）。重建误差可能导致不准确的科学推断，或危及探索偏远环境的航天器。为了应对这一挑战，我们提出了VECTOR，这是一种视觉分析工具，可以改善立体重建BA的误差检查。VECTOR为分析人员提供了以前无法获得的特征位置、相机姿态和计算出的3D点的可见性。VECTOR是与美国国家航空航天局喷气推进实验室的Perseverance火星漫游者和Ingenuity火星直升机地形重建团队合作开发的。我们报告了如何使用该工具调试和改进火星2020任务的地形重建。 et.al.|[2408.03503](http://arxiv.org/abs/2408.03503)|**[link](https://github.com/NASA-AMMOS/VECTOR)**|
|**2024-08-06**|**Efficient NeRF Optimization -- Not All Samples Remain Equally Hard**|我们提出了一种在线硬样本挖掘的应用，用于高效训练神经辐射场（NeRF）。NeRF模型为许多3D重建和渲染任务提供了最先进的质量，但需要大量的计算资源。NeRF网络参数内场景信息的编码需要随机采样。我们观察到，在训练过程中，大部分计算时间和内存使用都花在处理已经学习的样本上，这不再对模型更新产生显著影响。我们将随机样本的反向传递确定为优化过程中的计算瓶颈。因此，我们在推理模式下执行第一次前向传递，作为对硬样本的相对低成本搜索。随后，构建计算图，并仅使用硬样本更新NeRF网络参数。为了证明所提出方法的有效性，我们将我们的方法应用于Instant NGP，使视图合成质量比基线有了显著提高（平均每训练时间提高1 dB，或加速2倍以达到相同的PSNR水平），同时仅使用硬样本构建计算图可节省约40%的内存。由于我们的方法只与网络模块交互，我们希望它能得到广泛应用。 et.al.|[2408.03193](http://arxiv.org/abs/2408.03193)|null|
|**2024-08-06**|**BodySLAM: A Generalized Monocular Visual SLAM Framework for Surgical Applications**|内窥镜手术依赖于二维视图，给外科医生在深度感知和器械操作方面带来了挑战。虽然同步定位和标测（SLAM）已成为解决这些局限性的有前景的解决方案，但由于硬件限制，如使用单眼相机和没有里程计传感器，在内窥镜手术中的实施带来了重大挑战。本研究提出了一种强大的基于深度学习的SLAM方法，该方法结合了最先进和新开发的模型。它由三个主要部分组成：单眼姿态估计模块，它引入了一种基于CycleGAN架构的新型无监督方法；单眼深度估计模块，利用了新型Zoe架构；以及3D重建模块，它使用来自先前模型的信息来创建连贯的手术图。使用三个公开可用的数据集（Hamlyn、EndoSLAM和SCARED）严格评估了该程序的性能，并与两种最先进的方法EndoSFMLearner和EndoDepth进行了基准比较。与内窥镜中最先进的深度估计算法相比，Zoe在MDEM中的集成表现出了卓越的性能，而MPEM中的新方法表现出了具有竞争力的性能和最低的推理时间。结果展示了我们的方法在腹腔镜、胃镜和结肠镜检查中的稳健性，这是内镜手术中的三种不同场景。所提出的SLAM方法有可能通过为外科医生提供增强的深度感知和3D重建能力来提高内窥镜手术的准确性和效率。 et.al.|[2408.03078](http://arxiv.org/abs/2408.03078)|**[link](https://github.com/GuidoManni/BodySLAM)**|
|**2024-08-06**|**VirtualNexus: Enhancing 360-Degree Video AR/VR Collaboration with Environment Cutouts and Virtual Replicas**|非对称AR/VR协作系统将远程VR用户带到本地AR用户的物理环境中，使他们能够在共享的虚拟/物理空间内进行通信和工作。这样的系统通常通过3D重建或360度视频显示远程环境。虽然360度相机以更高的质量流式传输环境，但它们缺乏空间信息，使其交互性较差。我们推出了VirtualNexus，这是一个AR/VR协作系统，通过环境切口和虚拟复制品增强了360度视频AR/VR的协作。VR用户可以定义远程环境的切口，将其作为一个微型世界进行交互，他们的交互与本地AR视角同步。此外，AR用户可以使用神经渲染快速扫描和共享物理对象的3D虚拟副本。我们通过3个示例应用程序展示了我们系统的实用性，并在二元可用性测试中评估了我们的系统。VirtualNexus扩展了360度远程呈现系统的交互空间，提供了更好的物理存在、多功能性和交互清晰度。 et.al.|[2408.02914](http://arxiv.org/abs/2408.02914)|null|
|**2024-08-04**|**View-consistent Object Removal in Radiance Fields**|辐射场（RF）已成为3D场景表示的关键技术，能够合成具有非凡真实感的新颖视图。然而，随着RF的使用越来越广泛，对保持不同视角连贯性的有效编辑技术的需求变得显而易见。当前的方法主要依赖于每帧2D图像修复，这往往无法保持视图之间的一致性，从而损害了编辑RF场景的真实感。在这项工作中，我们引入了一种新的RF编辑流水线，通过只需要修复一个参考图像来显著提高一致性。然后，使用基于深度的方法将该图像投影到多个视图上，有效地减少了每帧修复中观察到的不一致性。然而，投影通常假设视图之间的光度一致性，这在现实世界的设置中通常是不切实际的。为了适应照明和视点的真实变化，我们的管道通过生成修复图像的多个方向变体来调整投影视图的外观，从而适应不同的光度条件。此外，我们提出了一种有效且稳健的多视图对象分割方法，作为我们管道的宝贵副产品。大量实验表明，我们的方法在保持视图之间的内容一致性和提高视觉质量方面明显优于现有框架。更多结果请访问https://vulab-ai.github.io/View-consistent_Object_Removal_in_Radiance_Fields. et.al.|[2408.02100](http://arxiv.org/abs/2408.02100)|null|
|**2024-08-04**|**PanicleNeRF: low-cost, high-precision in-field phenotypingof rice panicles with smartphone**|水稻穗部性状显著影响粮食产量，使其成为水稻表型研究的主要目标。然而，大多数现有技术仅限于受控的室内环境，难以在自然生长条件下捕捉水稻穗部特征。在这里，我们开发了PanicleNeRF，这是一种新方法，可以使用智能手机在田间高精度、低成本地重建水稻穗三维（3D）模型。该方法将大模型Segment Anything model（SAM）和小模型You Only Look Once version 8（YOLOv8）相结合，实现了水稻穗图像的高精度分割。然后，使用具有2D分割的图像，采用NeRF技术进行3D重建。最后，对得到的点云进行处理，成功提取穗部特征。结果表明，PanicleNeRF有效地解决了2D图像分割任务，实现了86.9%的平均F1分数和79.8%的平均联合交叉（IoU），与YOLOv8相比，边界重叠（BO）性能几乎翻了一番。在点云质量方面，PanicleNeRF明显优于传统的SfM MVS（运动结构和多视图立体）方法，如COLMAP和Metashape。然后精确提取穗长，籼稻的rRMSE为2.94%，粳稻为1.75%。根据3D点云估算的穗体积与粒数（籼稻R2=0.85，粳稻R2=0.82）和粒重（籼稻0.80，粳稻0.76）密切相关。该方法为水稻穗的田间表型高通量提供了一种低成本的解决方案，加快了水稻育种的效率。 et.al.|[2408.02053](http://arxiv.org/abs/2408.02053)|null|
|**2024-08-02**|**Enhanced Knee Kinematics: Leveraging Deep Learning and Morphing Algorithms for 3D Implant Modeling**|植入膝关节模型的准确重建在骨科手术和生物医学工程中至关重要，可以加强术前计划，优化植入物设计，改善手术结果。传统方法依赖于劳动密集型和易出错的手动分割。本研究提出了一种使用机器学习（ML）算法和变形技术对植入膝关节模型进行精确3D重建的新方法。该方法首先获取术前成像数据，如患者膝关节的荧光透视或X射线图像。然后训练卷积神经网络（CNN）来自动分割植入组件的股骨轮廓，大大减少了人工劳动并确保了高精度。分割后，变形算法使用分割数据和生物力学原理生成植入膝关节的个性化3D模型。该算法考虑植入物的位置、大小和方向来模拟膝关节的形状。通过将形态数据与植入物特定参数相结合，重建的模型准确地反映了患者的植入物解剖结构和配置。通过定量评估，包括与地面实况数据和现有技术的比较，证明了该方法的有效性。在涉及各种植入物类型的19个测试案例中，与手动分割相比，基于机器学习的分割方法显示出更高的准确性和一致性，平均RMS误差为0.58+/-0.14 mm。这项研究通过为植入膝关节模型的自动重建提供一个强大的框架，推动了骨科手术的发展。利用机器学习和变形算法，临床医生和研究人员可以获得对患者特定膝关节解剖、植入物生物力学和手术计划的宝贵见解，从而改善患者预后并提高护理质量。 et.al.|[2408.01557](http://arxiv.org/abs/2408.01557)|null|
|**2024-08-07**|**IG-SLAM: Instant Gaussian SLAM**|3D高斯散点最近显示出有希望的结果，作为SLAM系统中神经隐式表示的替代场景表示。然而，目前的方法要么缺乏密集的深度图来监督绘图过程，要么缺乏考虑环境规模的详细训练设计。为了解决这些缺点，我们提出了IG-SLAM，这是一种仅包含RGB的密集SLAM系统，它采用鲁棒的密集SLAN方法进行跟踪，并将其与高斯散斑相结合。使用跟踪提供的精确姿态和密集深度构建环境的3D地图。此外，我们在地图优化中利用深度不确定性来改进3D重建。我们在映射优化中的衰减策略增强了收敛性，并允许系统在单个过程中以每秒10帧的速度运行。我们通过最先进的仅RGB SLAM系统展示了具有竞争力的性能，同时实现了更快的运行速度。我们展示了在Replica、TUM-RGBD、ScanNet和EuRoC数据集上的实验。该系统在大规模序列中实现了逼真的3D重建，特别是在EuRoC数据集中。 et.al.|[2408.01126](http://arxiv.org/abs/2408.01126)|null|

<p align=right>(<a href=#updated-on-20240810>back to top</a>)</p>

## Diffusion

|Publish Date|Title|Abstract|PDF|Code|
|---|---|---|---|---|
|**2024-08-08**|**Puppet-Master: Scaling Interactive Video Generation as a Motion Prior for Part-Level Dynamics**|我们提出了Puppet Master，这是一个交互式视频生成模型，可以作为零件级动力学的运动先验。在测试时，给定一张图像和一组稀疏的运动轨迹（即拖动），Puppet Master可以合成一个视频，描绘出忠实于给定拖动交互的逼真部分级运动。这是通过微调大规模预训练的视频扩散模型来实现的，为此我们提出了一种新的调节架构来有效地注入拖动控制。更重要的是，我们引入了全对第一注意力机制，这是对广泛采用的空间注意力模块的直接替代，通过解决现有模型中的外观和背景问题，显著提高了生成质量。与其他在野生视频中训练并主要移动整个对象的运动条件视频生成器不同，Puppet Master是从Objaverse Animation HQ学习的，这是一个新的精选部分级运动剪辑数据集。我们提出了一种策略，可以自动过滤出次优动画，并用有意义的运动轨迹来增强合成渲染。Puppet-Master很好地概括了各种类别的真实图像，并在现实世界的基准测试中以零样本的方式优于现有方法。有关更多结果，请参阅我们的项目页面：vgg-puppetmaster.github.io。 et.al.|[2408.04631](http://arxiv.org/abs/2408.04631)|null|
|**2024-08-08**|**Regularized Unconstrained Weakly Submodular Maximization**|子模块优化在机器学习和数据挖掘中得到了应用。本文研究了 $h=f-c$形式的函数最大化问题，其中$f$是单调、非负、弱子模集函数，$c$是模函数。我们设计了一种确定性近似算法，该算法使用${{O}}（\frac{n}{\epsilon}\log\frac{n}\gamma \epsilon}）$oracle调用函数$h$，并输出一个集合${S}$，使得$h（{S}）\geq\gamma（1-\epsilo）f（OPT）-c（OPT f$。针对这个问题的现有算法要么承认较差的近似比，要么具有二次运行时间。我们还提出了我们的算法对这个问题的近似比率，近似预言符为$f$。我们通过对现实世界应用的广泛实证评估来验证我们的理论结果，包括子模型效用函数$f$的顶点覆盖和影响扩散问题，以及弱子模型$f$ 中的贝叶斯A-最优设计。我们的实验结果表明，我们的算法有效地实现了高质量的解决方案。 et.al.|[2408.04620](http://arxiv.org/abs/2408.04620)|null|
|**2024-08-08**|**An empirical background modeling tool (TweedleDEE) applied to new Milky Way satellite Leo VI**|我们提出了一种计算工具TweedleDEE，用于使用略微偏离该区域的公开伽马射线数据，对天空1度区域的漫射伽马射线背景发射进行经验建模。这个背景模型允许用户对异常的局部伽马射线发射源进行纯粹的数据驱动搜索，包括新的物理学。作为一个应用，我们使用TweedleDEE和MADHATv2包对新发现的Leo VI矮球状星系中的暗物质湮灭进行了首次搜索，并提出了湮灭通道和横截面速度依赖性的各种选择的模型约束。 et.al.|[2408.04611](http://arxiv.org/abs/2408.04611)|null|
|**2024-08-08**|**Img-Diff: Contrastive Data Synthesis for Multimodal Large Language Models**|高性能多模态大型语言模型（MLLM）在很大程度上依赖于数据质量。本研究引入了一种名为Img-Diff的新数据集，旨在通过利用对比学习和图像差异字幕的见解来增强MLLM中的细粒度图像识别。通过分析相似图像之间的对象差异，我们挑战模型来识别匹配和不同的组件。我们利用Stable Diffusion XL模型和先进的图像编辑技术来创建成对的相似图像，突出显示对象替换。我们的方法包括一个用于识别对象差异的差异区域生成器，以及一个用于详细差异描述的差异标题生成器。结果是一个相对较小但高质量的“对象替换”样本数据集。我们使用所提出的数据集来微调最先进的（SOTA）MLLM，如MGM-7B，在许多图像差异和视觉问答任务中，与使用大规模数据集训练的SOTA模型相比，性能得分得到了全面提高。例如，我们训练的模型在MMVP基准上明显超过了SOTA模型GPT-4V和Gemini。此外，我们研究了通过“对象去除”生成图像差异数据的替代方法，并进行了彻底的评估，以确认数据集的多样性、质量和鲁棒性，对这种对比数据集的合成提出了一些见解。为了鼓励进一步的研究，推进多模态数据合成领域，增强MLLM在图像理解方面的基本能力，我们在https://github.com/modelscope/data-juicer/tree/ImgDiff. et.al.|[2408.04594](http://arxiv.org/abs/2408.04594)|**[link](https://github.com/modelscope/data-juicer)**|
|**2024-08-08**|**Sketch2Scene: Automatic Generation of Interactive 3D Game Scenes from User's Casual Sketches**|3D内容生成是许多计算机图形应用程序的核心，包括视频游戏、电影制作、虚拟和增强现实等。本文提出了一种基于深度学习的新方法，用于自动生成交互式和可玩的3D游戏场景，所有这些场景都来自用户的随意提示，如手绘草图。基于草图的输入在内容创建过程中提供了一种自然、便捷的方式来传达用户的设计意图。为了规避学习中数据不足的挑战（即缺乏3D场景的大量训练数据），我们的方法利用预训练的2D去噪扩散模型来生成场景的2D图像作为概念指导。在这个过程中，我们采用等距投影模式，在获得场景布局的同时剔除未知的相机姿态。从生成的等距图像中，我们使用预训练的图像理解方法将图像分割成有意义的部分，如离地物体、树木和建筑物，并提取二维场景布局。这些片段和布局随后被馈送到程序内容生成（PCG）引擎中，例如Unity或Unreal等3D视频游戏引擎，以创建3D场景。由此产生的3D场景可以无缝集成到游戏开发环境中，并且易于玩。广泛的测试表明，我们的方法可以有效地生成高质量和交互式的3D游戏场景，其布局紧密遵循用户的意图。 et.al.|[2408.04567](http://arxiv.org/abs/2408.04567)|null|
|**2024-08-08**|**Local and global existence for the stochastic Prandtl equation driven by multiplicative noises in two and three dimensions**|本文研究了二维和三维随机普朗特方程的局部和全局存在性，该方程控制着在具有防滑边界条件的随机Navier-Stokes方程的无粘极限中出现的边界层内的速度场。在随机状态下建立适定性时出现了新的问题：人们永远无法推导出用于描述确定性环境中解的解析半径的能量泛函的路径控制。为此，我们在共正态Sobolev空间中建立了高阶估计，以消除解析半径对未知的依赖性。构造了三个近似方案来求解随机普朗特方程，并在切向解析的通常Sobolev型空间中获得了局部适定性。此外，我们研究了由切向随机扩散驱动的随机普朗特方程，发现噪声使方程正则化，因为在二维和三维中，都存在高概率的全局Gevrey-2解，并且半径随时间线性增长。 et.al.|[2408.04546](http://arxiv.org/abs/2408.04546)|null|
|**2024-08-08**|**Electrical resistivity, thermal conductivity, and viscosity of Fe-H alloys at Earth's core conditions**|铁氢合金的输运性质（电阻率、热导率和粘度）对行星磁场的稳定性和演化具有重要意义。在这里，我们研究了掺杂不同氢含量的铁的热输运特性，作为地球外核顶部和底部及以外的压力（P）和温度（T）的函数，对应于约130至300 GPa的压力和4000至7000 K的温度。使用第一性原理密度泛函理论分子动力学模拟（FPMD），我们验证了晶体FeH $_x$是超离子的，H自由扩散。我们通过线性响应格林-库博公式发现，在地球外核条件下，液态Fe-H合金的低频粘度为10-11mPa$\cdot$s。利用密度泛函理论（DFT）和动态平均场理论（DMFT）中的KKR方法，我们发现在外核条件下，铁液的电阻率随着温度的升高而饱和。我们发现H对电和热输运的影响很小，因此不需要核中确切的H含量。H的主要作用是对状态方程的影响，在常数P和T下降低密度。我们发现洛伦兹数小于理想值，当X（H）=0.20或0.45 wt%H时，热导率为105和190^{-1}K^{-1}$ 分别在靠近地核-地幔和内外地核边界的条件下。 et.al.|[2408.04521](http://arxiv.org/abs/2408.04521)|null|
|**2024-08-08**|**Diffusive hydrodynamics from long-range correlations**|在流体动力学理论中，多体系统的非平衡动力学在大尺度的空间和时间上通过不可逆弛豫到局部熵最大化来近似。这导致对流方程由梯度展开中的粘性或扩散项校正，如Navier-Stokes方程。扩散项使用Kubo公式进行评估，可能是由丢弃的微观自由度引起的突发噪声引起的。在一维空间中，由于噪声导致超扩散，扩散缩放通常会被破坏。但在线性退化流体力学中，如可积模型，观察到了扩散行为，长期以来人们认为标准扩散图仍然有效。在这封信中，我们证明了在这种系统中，Navier-Stokes方程在线性响应之外会失效。我们证明扩散阶修正不采用梯度展开的形式。相反，它们完全由初始状态波动的弹道输运决定，并从弹道宏观波动理论（BMFT）最近预测的非局部两点相关性中获得；由此得到的流体动力学方程是可逆的。为此，我们建立了一个正则化波动理论，为最近的观点奠定了坚实的基础，即初始状态波动的弹道输运决定了欧拉标度之外的波动和相关性。这将之前为解释可积系统中的Kubo公式而开发的“对流扩散”概念扩展到一般的非平衡设置。 et.al.|[2408.04502](http://arxiv.org/abs/2408.04502)|null|
|**2024-08-08**|**Extrinsic Orbital Hall Effect: Interplay Between Diffusive and Intrinsic Transport**|尽管最近成功地识别了轨道霍尔效应（OHE）的实验特征，但对这一独特现象背后的微观机制的研究仍处于起步阶段。在这里，我们使用带隙的2D狄拉克材料作为OHE的模型系统，开发了一种轨道输运的微观理论，该理论无扰动地捕获了外部无序效应。我们发现，它预测了几个迄今为止未知的效应，包括（i）OHE电导率与杂质散射势的强度和对称性的强烈依赖性，以及（ii）作为费米能量函数的从本征OHE到外征OHE的平滑交叉。与之前的（微扰）研究相比，发现OHE在稀杂质极限下表现出真正的扩散行为，这可以追溯到斜散射型过程的主导地位。我们的工作揭示了非微扰顶点校正对于正确描述外轨道霍尔输运的关键性质，并证实了常见的短程杂质是OHE的关键促成因素。 et.al.|[2408.04492](http://arxiv.org/abs/2408.04492)|null|
|**2024-08-08**|**Random Walk Diffusion for Efficient Large-Scale Graph Generation**|图生成解决了生成具有与真实世界图相似的数据分布的新图的问题。虽然以前基于扩散的图生成方法显示出了有希望的结果，但它们往往难以扩展到大型图。在这项工作中，我们提出了ARROW Diff（自回归随机游走扩散），这是一种新的基于随机游走的扩散方法，用于高效的大规模图生成。我们的方法包括随机游走采样和图修剪的迭代过程中的两个组成部分。我们证明ARROW Diff可以有效地扩展到大型图形，在生成时间和多图统计方面都超过了其他基线方法，反映了生成图形的高质量。 et.al.|[2408.04461](http://arxiv.org/abs/2408.04461)|null|

<p align=right>(<a href=#updated-on-20240810>back to top</a>)</p>

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

<p align=right>(<a href=#updated-on-20240810>back to top</a>)</p>

[contributors-shield]: https://img.shields.io/github/contributors/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[contributors-url]: https://github.com/Vincentqyw/cv-arxiv-daily/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[forks-url]: https://github.com/Vincentqyw/cv-arxiv-daily/network/members
[stars-shield]: https://img.shields.io/github/stars/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[stars-url]: https://github.com/Vincentqyw/cv-arxiv-daily/stargazers
[issues-shield]: https://img.shields.io/github/issues/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[issues-url]: https://github.com/Vincentqyw/cv-arxiv-daily/issues

