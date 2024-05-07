[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]

## Updated on 2024.05.07
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
|**2024-05-06**|**A Construct-Optimize Approach to Sparse View Synthesis without Camera Pose**|从稀疏的输入图像集进行新的视图合成是一个具有挑战性的问题，具有很大的实际意义，尤其是当相机姿态不存在或不准确时。由于姿态和深度之间的耦合以及单目深度估计的不精确性，在神经辐射场算法中直接优化相机姿态和使用估计的深度通常不会产生好的结果。在本文中，我们利用最近的3D高斯飞溅方法，开发了一种新的无相机姿态稀疏视图合成的构造和优化方法。具体来说，我们通过使用单目深度并将像素投影回3D世界来逐步构建解决方案。在构建过程中，我们通过检测训练视图和相应渲染图像之间的2D对应关系来优化解决方案。我们开发了一个统一的可微分管道，用于相机配准和调整相机姿势和深度，然后进行反向投影。我们还引入了高斯飞溅中预期表面的新概念，这对我们的优化至关重要。这些步骤实现了粗略的解决方案，然后可以使用标准优化方法对其进行低通滤波和细化。我们展示了坦克、寺庙和静态远足数据集的结果，只有三个宽间距的视图，显示出比竞争方法（包括具有近似相机姿态信息的方法）明显更好的质量。此外，即使使用一半的数据集，我们的结果也会随着更多的视图而改进，并优于以前的InstantNGP和Gaussian Splatting算法。 et.al.|[2405.03659](http://arxiv.org/abs/2405.03659)|null|
|**2024-05-06**|**Gaussian Splatting: 3D Reconstruction and Novel View Synthesis, a Review**|基于图像的3D重建是一项具有挑战性的任务，涉及从一组输入图像推断对象或场景的3D形状。基于学习的方法因其直接估计3D形状的能力而受到关注。这篇综述论文的重点是最先进的3D重建技术，包括生成新颖的、看不见的视图。概述了高斯飞溅方法的最新发展，包括输入类型、模型结构、输出表示和训练策略。还讨论了尚未解决的挑战和未来的方向。鉴于该领域的快速进展以及增强3D重建方法的众多机会，对算法进行全面检查似乎至关重要。因此，本研究对高斯散射的最新进展进行了全面的概述。 et.al.|[2405.03417](http://arxiv.org/abs/2405.03417)|null|
|**2024-05-04**|**LidaRF: Delving into Lidar for Neural Radiance Field on Street Scenes**|逼真度模拟在自动驾驶等应用中发挥着至关重要的作用，神经辐射场（NeRF）的进步可以通过自动创建数字3D资产实现更好的可扩展性。然而，由于在较高速度下相机运动基本共线和采样稀疏，街道场景的重建质量受到影响。另一方面，应用程序通常要求从偏离输入的摄影机视图进行渲染，以准确模拟车道变更等行为。在本文中，我们提出了一些见解，可以更好地利用激光雷达数据来提高街景的NeRF质量。首先，我们的框架从激光雷达中学习几何场景表示，该表示与基于隐式网格的表示融合用于辐射解码，从而提供由显式点云提供的更强的几何信息。其次，我们提出了一种鲁棒的遮挡感知深度监督方案，该方案允许通过累积来利用密集的激光雷达点。第三，我们从激光雷达点生成增强训练视图，以便进一步改进。我们的见解转化为在真实驾驶场景下大大改进的新颖视图合成。 et.al.|[2405.00900](http://arxiv.org/abs/2405.00900)|null|
|**2024-05-01**|**RTG-SLAM: Real-time 3D Reconstruction at Scale using Gaussian Splatting**|我们提出了实时高斯SLAM（RTG-SLAM），这是一个使用RGBD相机的实时三维重建系统，用于使用高斯飞溅的大规模环境。该系统具有紧凑的高斯表示和高效的动态高斯优化方案。我们强制每个高斯要么不透明，要么几乎透明，不透明的适合表面和主色，透明的适合残余色。通过以不同于彩色渲染的方式渲染深度，我们让单个不透明高斯很好地拟合局部表面区域，而不需要多个重叠的高斯，从而大大降低了内存和计算成本。对于动态高斯优化，我们明确地为每帧三种类型的像素添加高斯：新观察到的、具有大颜色误差的和具有大深度误差的。我们还将所有高斯分为稳定高斯和不稳定高斯，其中稳定高斯有望很好地拟合先前观察到的RGBD图像，否则不稳定。我们只优化不稳定的高斯，只渲染不稳定高斯占用的像素。这样，要优化的高斯数和要渲染的像素都大大减少，并且可以实时进行优化。我们展示了各种大型场景的实时重建。与最先进的基于NeRF的RGBD SLAM相比，我们的系统实现了相当高质量的重建，但速度约为其两倍，内存成本约为其一半，并在新视图合成的真实性和相机跟踪精度方面表现出卓越的性能。 et.al.|[2404.19706](http://arxiv.org/abs/2404.19706)|null|
|**2024-04-29**|**SAGS: Structure-Aware 3D Gaussian Splatting**|随着NeRFs的出现，3D高斯散射（3D-GS）为实时神经渲染铺平了道路，克服了体积方法的计算负担。继3D-GS的开创性工作之后，有几种方法试图实现可压缩和高保真度性能的替代方案。然而，通过采用几何不可知的优化方案，这些方法忽略了场景的固有3D结构，从而限制了表示的表现力和质量，导致了各种浮点和伪影。在这项工作中，我们提出了一种结构感知的高斯飞溅方法（SAGS），该方法隐式地对场景的几何结构进行编码，这反映了最先进的渲染性能，并降低了基准新视图合成数据集的存储要求。SAGS建立在局部全局图表示的基础上，有助于复杂场景的学习，并强制执行有意义的点位移，以保持场景的几何结构。此外，我们还介绍了一种轻量级的SAGS，使用了一种简单而有效的中点插值方案，该方案展示了场景的紧凑表示，在不依赖任何压缩策略的情况下，大小减少了24 $\times$ 。在多个基准数据集上进行的大量实验表明，在渲染质量和模型大小方面，与最先进的3D-GS方法相比，SAGS具有优越性。此外，我们证明了我们的结构感知方法可以有效地减轻先前方法的浮动伪影和不规则失真，同时获得精确的深度图。项目页面https://eververas.github.io/SAGS/. et.al.|[2404.19149](http://arxiv.org/abs/2404.19149)|null|
|**2024-04-29**|**Simple-RF: Regularizing Sparse Input Radiance Fields with Simpler Solutions**|神经辐射场（NeRF）在场景的照片逼真的自由视图渲染中表现出令人印象深刻的性能。最近对NeRF的改进，如TensoRF和ZipNeRF，与使用隐式表示的NeRF相比，使用显式模型进行更快的优化和渲染。然而，隐式和显式辐射场都需要对给定场景中的图像进行密集采样。当只有一组稀疏的视图可用时，它们的性能会显著下降。研究人员发现，监督辐射场估计的深度有助于以更少的视角有效训练辐射场。深度监督是使用经典方法或在大型数据集上预先训练的神经网络来获得的。前者可能只提供稀疏的监督，而后者可能存在泛化问题。与早期的方法不同，我们试图通过设计增强模型并将其与主辐射场一起训练来学习深度监督。此外，我们的目标是设计一个正则化框架，该框架可以在不同的隐式和显式辐射场中工作。我们观察到，在稀疏输入场景中，这些辐射场模型的某些特征与观察到的图像过度拟合。我们的关键发现是，降低辐射场在位置编码、分解张量分量的数量或哈希表的大小方面的能力，限制了模型学习更简单的解决方案，从而在某些区域估计更好的深度。通过设计基于这种降低的能力的增强模型，我们可以更好地对主辐射场进行深度监督。通过采用上述正则化，我们在包含前向和360 $^\circ$ 场景的流行数据集上使用稀疏输入视图实现了最先进的视图合成性能。 et.al.|[2404.19015](http://arxiv.org/abs/2404.19015)|null|
|**2024-04-29**|**3D Gaussian Splatting with Deferred Reflection**|基于神经和高斯的辐射场方法的出现在新视图合成领域取得了巨大成功。然而，镜面反射仍然是不平凡的，因为众所周知，高频辐射场很难稳定准确地拟合。我们提出了一种延迟着色方法来有效地渲染高斯飞溅的镜面反射。关键的挑战来自环境图反射模型，该模型需要精确的表面法线，同时使用不连续的梯度来限制法线估计。我们利用延迟着色生成的每像素反射梯度来桥接相邻高斯的优化过程，允许几乎正确的法线估计逐渐传播并最终传播到所有反射对象上。我们的方法在合成高质量镜面反射效果方面显著优于最先进的技术和并行工作，证明了合成场景和真实世界场景的峰值信噪比（PSNR）都得到了一致的提高，同时以几乎与香草高斯飞溅相同的帧速率运行。 et.al.|[2404.18454](http://arxiv.org/abs/2404.18454)|null|
|**2024-04-29**|**$ν$-DBA: Neural Implicit Dense Bundle Adjustment Enables Image-Only Driving Scene Reconstruction**|传感器轨迹和3D地图的联合优化是束调整（BA）的一个关键特性，对自动驾驶至关重要。本文提出了$\nu$ -DBA，这是一种使用三维神经隐式曲面进行地图参数化来实现几何密集束平差（DBA）的新框架，该框架使用密集光流预测引导的几何误差来优化地图表面和轨迹姿态。此外，我们通过逐场景自监督对光流模型进行微调，以进一步提高密集映射的质量。我们在多个驾驶场景数据集上的实验结果表明，我们的方法实现了卓越的轨迹优化和密集的重建精度。我们还研究了光度误差和不同的神经几何先验对表面重建和新视图合成性能的影响。我们的方法是朝着在密集束调整中利用神经隐式表示实现更准确的轨迹和详细的环境映射迈出的重要一步。 et.al.|[2404.18439](http://arxiv.org/abs/2404.18439)|null|
|**2024-04-25**|**Depth Supervised Neural Surface Reconstruction from Airborne Imagery**|虽然最初是为新颖的视图合成而开发的，但神经辐射场（NeRF）最近已成为多视图立体（MVS）的替代品。在一系列研究活动的触发下，已经获得了有希望的结果，尤其是在无纹理、透明和反射表面方面，而这些场景对传统的基于MVS的方法仍然具有挑战性。然而，这些调查大多集中在近距离场景上，对空中场景的研究仍然缺失。对于这项任务，NeRF在图像冗余度低和数据证据薄弱的区域面临潜在的困难，如经常在街道峡谷、立面或建筑阴影中发现的那样。此外，训练这样的网络在计算上是昂贵的。因此，我们工作的目的有两个：首先，我们研究NeRFs对代表不同特征的航空图像块的适用性，如仅最低点、倾斜和高分辨率图像。其次，在这些调查过程中，我们证明了从联络点测量中积分深度先验的好处，这些测量是在预先假设的束块调整过程中提供的。我们的工作基于最先进的框架VolSDF，该框架通过符号距离函数（SDF）对3D场景进行建模，因为与普通NeRF中的标准体积表示相比，这更适用于表面重建。为了进行评估，将基于NeRF的重建与航空图像的公开基准数据集的结果进行比较。 et.al.|[2404.16429](http://arxiv.org/abs/2404.16429)|null|
|**2024-04-25**|**DIG3D: Marrying Gaussian Splatting with Deformable Transformer for Single Image 3D Reconstruction**|在本文中，我们研究了从单视图RGB图像进行三维重建的问题，并提出了一种新的方法，称为DIG3D，用于三维对象重建和新的视图合成。我们的方法利用编码器-解码器框架，该框架在编码器的深度感知图像特征的指导下在解码器中生成3D高斯。特别是，我们介绍了可变形变换器的使用，允许通过3D参考点和多层细化自适应进行高效和有效的解码。通过利用3D高斯的优势，我们的方法为单视图图像的3D重建提供了一个高效而准确的解决方案。我们在ShapeNet SRN数据集上评估了我们的方法，在汽车和椅子数据集中分别获得了24.21和24.98的PSNR。结果优于最近的方法约2.25%，证明了我们的方法在获得优异结果方面的有效性。 et.al.|[2404.16323](http://arxiv.org/abs/2404.16323)|null|

<p align=right>(<a href=#updated-on-20240507>back to top</a>)</p>

## 3D Reconstruction

|Publish Date|Title|Abstract|PDF|Code|
|---|---|---|---|---|
|**2024-05-06**|**Gaussian Splatting: 3D Reconstruction and Novel View Synthesis, a Review**|基于图像的3D重建是一项具有挑战性的任务，涉及从一组输入图像推断对象或场景的3D形状。基于学习的方法因其直接估计3D形状的能力而受到关注。这篇综述论文的重点是最先进的3D重建技术，包括生成新颖的、看不见的视图。概述了高斯飞溅方法的最新发展，包括输入类型、模型结构、输出表示和训练策略。还讨论了尚未解决的挑战和未来的方向。鉴于该领域的快速进展以及增强3D重建方法的众多机会，对算法进行全面检查似乎至关重要。因此，本研究对高斯散射的最新进展进行了全面的概述。 et.al.|[2405.03417](http://arxiv.org/abs/2405.03417)|null|
|**2024-05-05**|**Morphokinematical study of the planetary nebula Me2-1: Unveiling its point-symmetric and unusual physical structure**|（摘要）我们展示了几条发射线的窄带图像，以及Me2-1的高分辨率和中分辨率长缝光谱，以研究其形态和3D结构、物理参数和化学丰度。我们在Me2-1中发现：一个椭圆环；两个细长的弯曲结构（帽），其包含三对亮点对称（PS）结；所述环的壳内部；以及微弱的光晕或附着的外壳。在所有图像中都观察到了帽，PS结仅在低激发发射线图像中观察到。这些结构也在高分辨率的长狭缝光谱中被识别。3D重建显示，Me2-1由一个几乎是极点的环和一个几乎球形的外壳组成，盖子和PS结连接在外壳上。帽状物和PS结最有可能追踪沿着摆动轴喷出的高速准直双极外流与球壳碰撞、减速并保持附着的位置。尽管Me2-1中的主要激发机制被发现是光电离，但PS结中的冲击的贡献是由它们的发射线比提出的。在行星状星云中，准直外流和带有球形外壳的环的结合是不寻常的。我们推测，如果两颗行星都在祖先的渐近巨星分支阶段进入共同的包络演化，那么这两颗行星可能都参与了Me2-1的形成，每颗行星的质量都小于一个木星。一颗行星被潮汐破坏，在中心恒星周围形成吸积盘，准直的双极性外流从吸积盘喷出；另一颗行星幸存下来，导致吸积盘摆动。导出的物理参数和化学丰度与之前的分析中获得的相似，丰度也指向Me2-1的低质量祖先。 et.al.|[2405.02938](http://arxiv.org/abs/2405.02938)|null|
|**2024-05-05**|**MVIP-NeRF: Multi-view 3D Inpainting on NeRF Scenes via Diffusion Prior**|尽管出现了基于显式RGB和深度2D修复监督的成功NeRF修复方法，但这些方法固有地受到其底层2D修复器能力的约束。这是由于两个关键原因：（i）独立修复组成图像会导致视图不一致的图像，以及（ii）2D修复器难以确保高质量的几何图形完成和与修复的RGB图像对齐。为了克服这些限制，我们提出了一种称为MVIP NeRF的新方法，该方法利用扩散先验的潜力进行NeRF修复，同时解决外观和几何方面的问题。MVIP NeRF跨多个视图执行联合修复，以达到一致的解决方案，这是通过基于分数蒸馏采样（SDS）的迭代优化过程实现的。除了恢复渲染的RGB图像外，我们还提取法线贴图作为几何表示，并定义法线SDS损失，以促进精确的几何修复和与外观对齐。此外，我们制定了一个多视图SDS评分函数，以从不同的视图图像中同时提取生成先验，确保在处理大的视图变化时一致的视觉完成。我们的实验结果显示出比以前的NeRF修复方法更好的外观和几何恢复。 et.al.|[2405.02859](http://arxiv.org/abs/2405.02859)|null|
|**2024-05-04**|**Beyond Unimodal Learning: The Importance of Integrating Multiple Modalities for Lifelong Learning**|当人类擅长持续学习时，深度神经网络表现出灾难性的遗忘。大脑允许有效CL的一个显著特征是，它利用多种模式进行学习和推理，而这在DNN中尚未得到充分探索。因此，我们研究了多种模式在减轻遗忘中的作用和相互作用，并为多模式持续学习引入了一个基准。我们的研究结果表明，利用来自多种模态的多个视图和互补信息，使模型能够学习更准确、更稳健的表示。这使得模型不那么容易受到模态特定规律的影响，并大大减少了遗忘。此外，我们观察到，个体模态对分布变化表现出不同程度的鲁棒性。最后，我们提出了一种方法，通过利用每个模态中数据点之间的关系结构相似性来集成和对齐来自不同模态的信息。我们的方法设置了一个强大的基线，可以实现单模式和多模式推理。我们的研究为进一步探索多种模式在实现CL中的作用提供了一个有希望的案例，并为未来的研究提供了标准基准。 et.al.|[2405.02766](http://arxiv.org/abs/2405.02766)|null|
|**2024-05-04**|**ActiveNeuS: Active 3D Reconstruction using Neural Implicit Surface Uncertainty**|3D场景重建中的主动学习已经得到了广泛的研究，因为选择信息丰富的训练视图对重建至关重要。最近，神经辐射场（NeRF）变体在使用图像渲染或几何不确定性的主动3D重建中显示出性能提高。然而，在选择信息视图时同时考虑这两种不确定性仍然没有得到探索，而利用不同类型的不确定性可以减少在输入稀疏的早期训练阶段出现的偏差。在本文中，我们提出了ActiveNeuS，它在考虑两种不确定性的情况下评估候选视图。ActiveNeuS提供了一种积累图像渲染不确定性的方法，同时避免了估计密度可能引入的偏差。ActiveNeuS计算神经隐含的表面不确定性，提供颜色不确定性和表面信息。它通过使用表面信息和网格来有效地处理偏差，从而能够快速选择不同的视点。我们的方法优于以前在流行数据集Blender和DTU上的工作，表明ActiveNeuS选择的视图显著提高了性能。 et.al.|[2405.02568](http://arxiv.org/abs/2405.02568)|null|
|**2024-05-03**|**CVTGAD: Simplified Transformer with Cross-View Attention for Unsupervised Graph-level Anomaly Detection**|无监督图级异常检测（UGAD）在化学分析和生物信息学等关键学科中取得了显著的成绩。现有的UGAD范式通常采用数据扩充技术来构建多个视图，然后采用不同的策略从不同的视图中获得表示，以共同进行UGAD。然而，以前的大多数工作只从有限的感受野中考虑节点/图之间的关系，导致一些关键的结构模式和特征信息被忽视。此外，现有的大多数方法以并行的方式分别考虑不同的视图，无法直接探索不同视图之间的相互关系。因此，需要一种具有更大感受野的方法，可以直接探索不同观点之间的相互关系。在本文中，我们提出了一种新的用于无监督图级异常检测的具有交叉视图注意的简化变换器，即CVTGAD。为了增加感受野，我们构建了一个简化的基于转换器的模块，从图内和图间的角度利用节点/图之间的关系。此外，我们设计了一种跨视图注意力机制，直接利用不同视图之间的视图共生，在节点级和图级弥合视图间的差距。据我们所知，这是首次将transformer和cross-attention应用于UGAD，实现了图神经网络和transformer的协同工作。在3个领域的15个真实世界数据集上进行的大量实验证明了CVTGAD在UGAD任务上的优越性。代码位于\url{https://github.com/jindongli-Ai/CVTGAD}. et.al.|[2405.02359](http://arxiv.org/abs/2405.02359)|null|
|**2024-05-04**|**HandSSCA: 3D Hand Mesh Reconstruction with State Space Channel Attention from RGB images**|从单个RGB图像重建手网格是一项具有挑战性的任务，因为手经常被物体遮挡。以前的大多数工作都试图引入更多的附加信息并采用注意力机制来改善3D重建结果，但这会增加计算复杂性。这一观察结果促使我们提出一种新的简洁架构，同时提高计算效率。在这项工作中，我们提出了一种简单有效的三维手部网格重建网络HandSSCA，它是第一个将状态空间建模纳入手部姿态估计领域的网络。在网络中，我们设计了一个新的状态空间通道注意力模块，该模块扩展了有效的感觉场，提取了空间维度上的手部特征，并增强了通道维度上的手部区域特征。这种设计有助于重建完整而详细的手部网格。在具有挑战性手对象遮挡的知名数据集（如FREIHAND、DEXYCB和HO3D）上进行的大量实验表明，我们提出的HandSSCA在保持最小参数计数的同时实现了最先进的性能。 et.al.|[2405.01066](http://arxiv.org/abs/2405.01066)|null|
|**2024-05-01**|**Coherent 3D Portrait Video Reconstruction via Triplane Fusion**|最近在单图像3D肖像重建方面的突破使远程呈现系统能够实时流式传输来自单个相机的3D肖像视频，从而有可能使远程呈现民主化。然而，每帧3D重建表现出时间上的不一致性并且忘记了用户的外观。另一方面，自再现方法可以通过驱动个性化的3D先验来渲染连贯的3D肖像，但不能忠实地重建用户的每帧外观（例如，面部表情和照明）。在这项工作中，我们认识到需要保持连贯的身份和动态的每帧外观，以实现最佳的真实感。为此，我们提出了一种新的基于融合的方法，该方法将个性化的3D主题先验与每帧信息融合，生成时间稳定的3D视频，并忠实地重建用户的每帧外观。我们的基于编码器的方法仅使用由表达条件的3D GAN产生的合成数据进行训练，在工作室和野外数据集上实现了最先进的3D重建精度和时间一致性。 et.al.|[2405.00794](http://arxiv.org/abs/2405.00794)|null|
|**2024-05-01**|**Depth Priors in Removal Neural Radiance Fields**|神经辐射场（NeRF）在三维重建和生成新视图方面显示出令人印象深刻的结果。NeRF的一个关键挑战是重建场景的编辑，如对象移除，这需要在多个视图之间保持一致性，并确保高质量的合成视角。先前的研究结合了深度先验，通常来自激光雷达或COLMAP提供的稀疏深度测量，以提高NeRF中的目标去除性能。然而，这些方法要么昂贵，要么耗时。在本文中，我们提出了一种新的方法，将单目深度估计与基于NeRF的对象去除模型相结合，以显著减少时间消耗，提高场景生成和对象去除的鲁棒性和质量。我们在KITTI数据集上对COLMAP的密集深度重建进行了全面评估，以验证其在深度图生成中的准确性。我们的研究结果表明，COLMAP可以作为地面实况深度图的有效替代方案，在这种情况下，这些信息缺失或获取成本高昂。此外，我们将各种单目深度估计方法集成到去除NeRF模型中，即SpinNeRF，以评估其提高物体去除性能的能力。我们的实验结果突出了单目深度估计在显著改善NeRF应用方面的潜力。 et.al.|[2405.00630](http://arxiv.org/abs/2405.00630)|null|
|**2024-05-01**|**NC-SDF: Enhancing Indoor Scene Reconstruction Using Neural SDFs with View-Dependent Normal Compensation**|通过将单目几何先验作为额外的监督，最先进的神经隐式表面表示在室内场景重建中取得了令人印象深刻的结果。然而，我们已经观察到，这种先验之间的多视图不一致对高质量重建构成了挑战。作为回应，我们提出了NC-SDF，一种具有视图相关法线补偿（NC）的神经符号距离场（SDF）三维重建框架。具体来说，我们将单目正常先验中的视图相关偏差集成到场景的神经隐式表示中。通过自适应地学习和纠正偏差，我们的NC-SDF有效地减轻了不一致监督的不利影响，增强了重建中的全局一致性和局部细节。为了进一步细化细节，我们引入了一种信息像素采样策略，以更多地关注信息含量更高的复杂几何体。此外，我们设计了一种混合几何建模方法来改进神经隐式表示。在合成和真实世界数据集上的实验表明，NC-SDF在重建质量方面优于现有方法。 et.al.|[2405.00340](http://arxiv.org/abs/2405.00340)|null|

<p align=right>(<a href=#updated-on-20240507>back to top</a>)</p>

## Diffusion

|Publish Date|Title|Abstract|PDF|Code|
|---|---|---|---|---|
|**2024-05-06**|**An Empty Room is All We Want: Automatic Defurnishing of Indoor Panoramas**|我们提出了一种管道，该管道利用稳定扩散来改善去家具化背景下的修复结果，即从室内全景图像中移除家具。具体来说，我们说明了增加上下文、特定领域的模型微调和改进的图像混合如何在不需要依赖房间布局估计的情况下产生几何上合理的高保真度修复。我们展示了与其他家具移除技术相比在质量和数量上的改进。 et.al.|[2405.03682](http://arxiv.org/abs/2405.03682)|null|
|**2024-05-06**|**Field-of-View Extension for Diffusion MRI via Deep Generative Models**|目的：在扩散MRI（dMRI）中，不完全视野（FOV）可能会严重阻碍全脑组织微观结构和连接的体积和束分析。这项工作旨在开发一种方法，在FOV不完整的情况下，直接从现有的dMRI扫描中输入缺失的切片。我们假设具有完全视野的估算图像可以改善具有不完全视野的受损数据的全脑束描记术。因此，我们的方法提供了一种理想的替代方案，可以丢弃有价值的dMRI数据，从而实现后续的束描记术分析，否则这些分析将具有挑战性或无法获得损坏的数据。方法：我们提出了一个基于深度生成模型的框架，该模型估计了不完全FOV的dMRI扫描中缺失的大脑区域。该模型能够学习扩散加权图像（DWI）中的扩散特性和相应结构图像中明显的解剖特征，以有效地在不完全FOV之外输入DWI的缺失切片。结果：对于估算切片的评估，在WRAP数据集上，所提出的框架实现了PSNRb0=22.397，SSIMb0=0.905，PSNRb1300=22.479，SSIMb1300=0.893；在NACC数据集上，它实现了PSNRb0=21.304，SSIMb0=0.892，PSNRb1300=21.599，SSIMb1300=0.877。所提出的框架提高了束描记术的准确性，如WRAP和NACC数据集上72个束的平均Dice得分增加（p＜0.001）所示。结论：结果表明，所提出的框架在FOV不完整的dMRI数据中实现了足够的插补性能，可以改进全脑束成像，从而修复损坏的数据。我们的方法通过扩展和完整的FOV实现了更准确的全脑束成像结果，并降低了分析与阿尔茨海默病相关的束时的不确定性。 et.al.|[2405.03652](http://arxiv.org/abs/2405.03652)|null|
|**2024-05-06**|**Cosine Annealing Optimized Denoising Diffusion Error Correction Codes**|为了解决去噪扩散纠错码中线性搜索后期误码率增加的问题，我们提出了一种使用余弦退火优化去噪扩散误差校正码（ECC）的新方法。为了应对解码长码字的挑战，所提出的方法在反向扩散过程中采用了方差调整策略，而不是保持恒定的方差。该方法利用余弦退火，有效地降低了误码率，提高了解码效率。这封信通过实验广泛验证了该方法，并证明与现有方法相比，该方法在降低误码率和迭代效率方面有显著改进。这一进步为提高ECC解码性能提供了一个有前景的解决方案，可能会影响安全的数字通信实践。 et.al.|[2405.03638](http://arxiv.org/abs/2405.03638)|null|
|**2024-05-06**|**Strang Splitting for Parametric Inference in Second-order Stochastic Differential Equations**|我们讨论了在物理学、生物学和生态学中普遍存在的二阶随机微分方程（SDE）中的参数估计。通过引入辅助速度变量将二阶SDE转换为一阶系统，提出了两个主要挑战。首先，系统是次椭圆的，因为噪声只影响速度，使得Euler Maruyama估计器是病态的。为了克服这一点，我们提出了一种基于Strang分裂方案的估计器。其次，由于很少观测到速度，我们调整了部分观测的估计器。我们给出了完全和部分观测的四个估计量，使用全似然或仅使用速度边际似然。这些估计量直观，易于实现，计算速度快，我们证明了它们的一致性和渐近正态性。我们的分析表明，在完全观测的情况下使用全似然减少了扩散估计器的渐近方差。对于部分观测，渐近方差由于信息丢失而增加，但不受似然选择的影响。然而，对Kramers振子的数值研究表明，使用边际似然进行部分观测会产生偏差较小的估计量。我们将我们的方法应用于格陵兰冰芯的古气候数据，并将其拟合到Kramers振荡模型中，捕捉反映冰川时代观测到的气候条件的亚稳态之间的转变。 et.al.|[2405.03606](http://arxiv.org/abs/2405.03606)|null|
|**2024-05-06**|**Dissipative gradient nonlinearities prevent $δ$ -formations in local and nonlocal attraction-repulsion chemotaxis models**|我们研究了一些吸引-排斥趋化性模型，其特征是细胞密度扩散、化学引诱剂和化学排斥剂的化学敏感性和产生速率的非线性定律。此外，还加入了一个来源，该来源也涉及物种梯度的一些表达。 et.al.|[2405.03586](http://arxiv.org/abs/2405.03586)|null|
|**2024-05-06**|**Bridging discrete and continuous state spaces: Exploring the Ehrenfest process in time-continuous diffusion models**|通过随机过程的生成建模已经产生了显著的经验结果，并在理论理解方面取得了最新进展。原则上，过程的空间和时间都可以是离散的或连续的。在这项工作中，我们研究了离散状态空间上的时间连续马尔可夫跳跃过程，并研究了它们与SDE给出的状态连续扩散过程的对应关系。特别地，我们重新审视 $\textit｛Ehrenfest过程｝$ ，它在无限状态空间极限中收敛于Ornstein-Uhlenbeck过程。同样，我们可以证明Ehrenfest过程的时间反转收敛于时间反转的Ornstein-Uhlenbeck过程。这种观察桥接了离散和连续的状态空间，并允许将方法从一个设置转移到相应的另一个设置。此外，我们提出了一种用于训练马尔可夫跳跃过程的时间反转的算法，该算法依赖于条件期望，因此可以与去噪分数匹配直接相关。我们在多个令人信服的数值实验中演示了我们的方法。 et.al.|[2405.03549](http://arxiv.org/abs/2405.03549)|null|
|**2024-05-06**|**CCDM: Continuous Conditional Diffusion Models for Image Generation**|连续条件生成建模（CCGM）旨在估计高维数据（通常是图像）的分布，这些数据以称为回归标签的标量连续变量为条件。虽然连续条件生成对抗性网络（CcGAN）最初是为这项任务设计的，但其对抗性训练机制仍然容易受到极稀疏或不平衡数据的影响，从而导致次优结果。为了提高生成图像的质量，一个有前途的替代方案是用条件扩散模型（CDM）取代CcGAN，CDM以其稳定的训练过程和生成更逼真图像的能力而闻名。然而，由于一些局限性，如U-Net架构不足和处理回归标签的模型拟合机制不足，现有的CDM在应用于CCGM任务时遇到了挑战。在本文中，我们介绍了连续条件扩散模型（CCDM），这是第一个专门为CCGM任务设计的CDM。CCDM通过引入专门设计的条件扩散过程、具有定制条件机制的改进去噪U-Net、用于模型拟合的新的硬邻域损失和有效的条件采样程序来解决现有CDM的局限性。通过在分辨率从64x64到192x192不等的四个数据集上进行全面实验，我们证明了所提出的CCDM优于最先进的CCGM模型，从而在CCGM中建立了新的基准。广泛的消融研究验证了所提出的CCDM的模型设计和实施配置。我们的代码公开于https://github.com/UBCDingXin/CCDM. et.al.|[2405.03546](http://arxiv.org/abs/2405.03546)|null|
|**2024-05-06**|**Asymptotic-preserving hybridizable discontinuous Galerkin method for the Westervelt quasilinear wave equation**|我们讨论了超声波Westervelt模型的可杂交不连续Galerkin方法的渐近保持性质。更准确地说，我们通过推导低阶和高阶能量稳定性估计，以及与~ $\delta$无关的误差界，证明了所提出的方法对于声扩散阻尼参数~$\deleta$的小值是稳健的。然后使用这样的边界来表明，当~$\delta\rightarrow 0^+$时，该方法保持稳定，并且离散声速势~$\psi_h^{（\delta）}$收敛到~$\pis_h^{（0）}$，其中后者是奇异消失耗散极限。此外，我们证明了声粒子速度变量~$\bv=nabla\psi$ 近似的最优收敛性。通过数值实验验证了所建立的理论结果。 et.al.|[2405.03535](http://arxiv.org/abs/2405.03535)|null|
|**2024-05-06**|**Quasi-Monte Carlo for Bayesian design of experiment problems governed by parametric PDEs**|本文有助于研究偏微分方程（PDE）控制的贝叶斯反问题的最优实验设计。我们推导了贝叶斯最优设计问题中高维参数和数据域上的多元二重积分问题的参数正则性的估计。我们使用两种方法对这些二重积分问题进行了详细分析：参数域和数据域上的拟蒙特卡罗（QMC）体积规则的全张量积和稀疏张量积组合。具体而言，我们表明后一种方法显著提高了收敛速度，表现出与单个高维积分的QMC积分相当的性能。此外，我们在两个空间维度上对具有未知扩散系数的椭圆PDE问题的预测收敛速度进行了数值验证，提供了支持理论结果的经验证据，并突出了实际应用性。 et.al.|[2405.03529](http://arxiv.org/abs/2405.03529)|null|
|**2024-05-06**|**On anomalous dissipation induced by transport noise**|在本文中，我们证明了适当的传输噪声会导致二维Navier-Stokes方程和扩散方程在所有维度上解的能量异常耗散。关键因素是Meyers对具有传输噪声的SPDE的类型估计，该估计与最近对此类SPDE的缩放限制相结合。前者允许我们第一次对于这种类型的标度极限，在时间上一致地获得正光滑空间中的收敛性。与已知结果相比，主要的新颖之处之一是，即使存在强度任意小的传输噪声，也可能发生异常耗散。此外，我们还讨论了物理解释。 et.al.|[2405.03525](http://arxiv.org/abs/2405.03525)|null|

<p align=right>(<a href=#updated-on-20240507>back to top</a>)</p>

## NeRF

|Publish Date|Title|Abstract|PDF|Code|
|---|---|---|---|---|
|**2024-05-06**|**Neural Graph Mapping for Dense SLAM with Efficient Loop Closure**|现有的基于神经场的SLAM方法通常使用单个单片场作为其场景表示。这阻碍了循环闭合约束的有效结合，并限制了可扩展性。为了解决这些缺点，我们提出了一种神经映射框架，该框架将轻量级神经场锚定到稀疏视觉SLAM系统的姿态图上。我们的方法显示了整合大规模闭环的能力，同时限制了必要的重新融合。此外，我们通过在优化过程中考虑多个环路闭合来验证我们的方法的可扩展性，并证明我们的方法在质量和运行时间方面优于现有的最先进的方法。我们的代码可在https://kth-rpl.github.io/neural_graph_mapping/. et.al.|[2405.03633](http://arxiv.org/abs/2405.03633)|null|
|**2024-05-03**|**Simulation-based Inference of Developmental EEG Maturation with the Spectral Graph Model**|宏观神经活动的光谱内容在整个发育过程中不断演变，但这种成熟与潜在的大脑网络形成和动力学之间的关系尚不清楚。为了深入了解这一过程的机制，我们通过频谱图模型（SGM）的贝叶斯模型反演来评估发育脑电频谱变化，SGM是一种全脑空间频谱活动的简约模型，源于由结构连接体耦合的线性化神经场模型。基于模拟的推理用于从跨越发育期的脑电图频谱中估计年龄变化的SGM参数后验分布。我们发现，这种模型拟合方法通过关键神经参数的神经生物学一致进展准确地捕捉了脑电图频谱的发育成熟：长程耦合、轴突传导速度和兴奋性：抑制性平衡。这些结果表明，在正常发育过程中观察到的大脑活动的光谱成熟得到了功能适应的支持，特别是局部神经动力学的年龄依赖性调节及其在宏观结构网络中的长期耦合。 et.al.|[2405.02524](http://arxiv.org/abs/2405.02524)|null|
|**2024-04-30**|**Lightplane: Highly-Scalable Components for Neural 3D Fields**|当代3D研究，特别是在重建和生成方面，严重依赖2D图像进行输入或监督。然而，这些2D-3D映射的当前设计是内存密集型的，对现有方法构成了显著的瓶颈，并阻碍了新的应用。作为回应，我们为3D神经场提出了一对高度可扩展的组件：Lightplane Render和Splatter，这显著减少了2D-3D映射中的内存使用。这些创新能够以较小的内存和计算成本处理更多、更高分辨率的图像。我们展示了它们在各种应用中的实用性，从有利于图像级损失的单场景优化到实现用于大幅缩放3D重建和生成的多功能管道。代码：\url{https://github.com/facebookresearch/lightplane}. et.al.|[2404.19760](http://arxiv.org/abs/2404.19760)|**[link](https://github.com/facebookresearch/lightplane)**|
|**2024-05-03**|**Object Registration in Neural Fields**|神经场以一种对机器人应用具有巨大前景的方式提供3D几何结构和外观的连续场景表示。解锁机器人中神经领域独特用例的一个功能是对象6-DoF注册。在本文中，我们对最近的Reg-NF神经场配准方法及其在机器人环境中的用例进行了扩展分析。我们展示了使用场景和对象神经场模型确定场景中已知对象的6-DoF姿态的场景。我们展示了如何使用它来更好地表示未完全建模的场景中的对象，并通过将对象神经场模型替换到场景中来生成新的场景。 et.al.|[2404.18381](http://arxiv.org/abs/2404.18381)|null|
|**2024-04-26**|**ArtNeRF: A Stylized Neural Field for 3D-Aware Cartoonized Face Synthesis**|生成视觉模型和神经辐射领域的最新进展极大地促进了3D感知图像合成和风格化任务。然而，以前基于NeRF的工作仅限于单场景风格化，训练模型生成具有任意风格的3D感知卡通人脸仍然没有解决。为了解决这个问题，我们提出了ArtNeRF，这是一种从3D感知GAN中派生出来的新颖的人脸风格化框架。在这个框架中，我们利用表达生成器来合成风格化的人脸，并利用三分支鉴别器模块来提高生成人脸的视觉质量和风格一致性。具体而言，利用基于对比学习的风格编码器来提取风格图像的鲁棒低维嵌入，使生成器能够获得各种风格的知识。为了平滑跨领域迁移学习的训练过程，我们提出了一个自适应风格混合模块，该模块有助于注入风格信息，并允许用户自由调整风格化水平。我们进一步引入了一个神经渲染模块，以实现更高分辨率图像的高效实时渲染。大量实验表明，ArtNeRF在生成具有任意风格的高质量3D感知卡通人脸方面是通用的。 et.al.|[2404.13711](http://arxiv.org/abs/2404.13711)|**[link](https://github.com/silence-tang/artnerf)**|
|**2024-04-19**|**BANF: Band-limited Neural Fields for Levels of Detail Reconstruction**|主要由于其隐含性质，神经场缺乏直接的滤波机制，因为离散信号处理的傅立叶分析不直接适用于这些表示。神经场的有效滤波对于实现下游应用程序中的细节处理水平至关重要，并支持在规则网格上对场进行采样的操作（例如，行进立方体）。试图在频域中分解神经场的现有方法要么采用启发式方法，要么需要对神经场架构进行广泛修改。我们展示了通过一个简单的修改，可以获得低通滤波的神经场，进而展示了如何利用这一点来获得整个信号的频率分解。我们通过研究细节水平重建来证明我们的技术的有效性，并展示了如何有效地计算粗糙的表示。 et.al.|[2404.13024](http://arxiv.org/abs/2404.13024)|null|
|**2024-04-15**|**Efficient and accurate neural field reconstruction using resistive memory**|人类通过将稀疏的观测整合到大规模互连的突触和神经元中来构建空间感知，提供了卓越的并行性和效率。在人工智能中复制这一能力在医学成像、AR/VR和嵌入式人工智能中有着广泛的应用，在这些领域，输入数据往往是稀疏的，计算资源有限。然而，传统的数字计算机信号重构方法面临着软硬件两方面的挑战。在软件方面，传统显式信号表示中的存储效率低下会带来困难。硬件障碍包括冯·诺依曼瓶颈，它限制了CPU和存储器之间的数据传输，以及CMOS电路在支持并行处理方面的局限性。我们提出了一种软硬件协同优化的系统方法，用于从稀疏输入重建信号。在软件方面，我们使用神经场通过神经网络隐式地表示信号，并使用低秩分解和结构化修剪对其进行进一步压缩。在硬件方面，我们设计了一个基于电阻存储器的内存计算（CIM）平台，该平台具有高斯编码器（GE）和MLP处理引擎（PE）。GE利用电阻存储器的内在随机性进行有效的输入编码，而PE通过硬件感知量化（HAQ）电路实现精确的权重映射。我们在基于40nm 256Kb电阻存储器的内存内计算宏上展示了该系统的功效，在不影响3D CT稀疏重建、新视图合成和动态场景新视图合成等任务的重建质量的情况下，实现了巨大的能效和并行性改进。这项工作推进了人工智能驱动的信号恢复技术，为未来高效、稳健的医疗人工智能和3D视觉应用铺平了道路。 et.al.|[2404.09613](http://arxiv.org/abs/2404.09613)|null|
|**2024-04-10**|**Ray-driven Spectral CT Reconstruction Based on Neural Base-Material Fields**|在谱CT重建中，基底材料分解涉及求解大规模非线性积分方程组，这在数学上是高度不适定的。本文提出了一种模型，该模型使用神经场表示来参数化对象的衰减系数，从而避免了线积分离散化过程中像素驱动的投影系数矩阵的复杂计算。介绍了一种基于光线驱动神经场的线积分轻量级离散化方法，提高了离散化过程中积分逼近的精度。将基底材料表示为连续的向量值隐函数，以建立基底材料的神经场参数化模型。然后使用深度学习的自动微分框架来求解神经基底材料场的隐式连续函数。该方法不受重建图像空间分辨率的限制，并且网络具有紧凑和规则的特性。实验验证表明，我们的方法在处理光谱CT重建方面表现得非常好。此外，它还满足了生成高分辨率重建图像的要求。 et.al.|[2404.06991](http://arxiv.org/abs/2404.06991)|null|
|**2024-04-12**|**SpikeNVS: Enhancing Novel View Synthesis from Blurry Images via Spike Camera**|使用神经辐射场（NeRF）和三维高斯散射（3DGS）等神经场方法实现清晰的新视图合成（NVS）的最关键因素之一是训练图像的质量。然而，传统的RGB相机容易受到运动模糊的影响。相比之下，像事件和尖峰相机这样的神经形态相机固有地捕捉更全面的时间信息，这可以作为额外的训练数据提供场景的清晰表示。最近的方法已经探索了集成事件摄像机以提高NVS的质量。事件RGB方法有一些局限性，例如高昂的培训成本和无法在后台有效工作。相反，我们的研究引入了一种新的方法，使用尖峰相机来克服这些限制。通过将尖峰流的纹理重建视为基本事实，我们设计了尖峰纹理（TfS）损失。由于尖峰摄像机依赖于时间积分，而不是事件摄像机使用的时间微分，我们提出的TfS损失保持了可管理的训练成本。它同时处理前景对象和背景。我们还提供了用spike RGB相机系统拍摄的真实世界数据集，以促进未来的研究工作。我们使用合成和真实世界的数据集进行了广泛的实验，以证明我们的设计可以增强NeRF和3DGS的新视图合成。代码和数据集将提供给公众访问。 et.al.|[2404.06710](http://arxiv.org/abs/2404.06710)|null|
|**2024-04-03**|**LiDAR4D: Dynamic Neural Fields for Novel Space-time View LiDAR Synthesis**|尽管神经辐射场（NeRFs）在图像新视图合成（NVS）方面取得了成功，但激光雷达NVS在很大程度上仍未被探索。以前的激光雷达NVS方法采用了图像NVS方法的简单转变，同时忽略了激光雷达点云的动态特性和大规模重建问题。有鉴于此，我们提出了LiDAR4D，这是一种用于新的时空LiDAR视图合成的仅限LiDAR的可微分框架。考虑到稀疏性和大规模特征，我们设计了一种结合多平面和网格特征的4D混合表示，以实现从粗到细的有效重建。此外，我们引入了从点云导出的几何约束，以提高时间一致性。对于激光雷达点云的真实合成，我们结合了光线下降概率的全局优化，以保持跨区域模式。在KITTI-360和NuScenes数据集上进行的大量实验证明了我们的方法在实现几何感知和时间一致的动态重建方面的优越性。代码可在https://github.com/ispc-lab/LiDAR4D. et.al.|[2404.02742](http://arxiv.org/abs/2404.02742)|**[link](https://github.com/ispc-lab/lidar4d)**|

<p align=right>(<a href=#updated-on-20240507>back to top</a>)</p>

[contributors-shield]: https://img.shields.io/github/contributors/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[contributors-url]: https://github.com/Vincentqyw/cv-arxiv-daily/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[forks-url]: https://github.com/Vincentqyw/cv-arxiv-daily/network/members
[stars-shield]: https://img.shields.io/github/stars/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[stars-url]: https://github.com/Vincentqyw/cv-arxiv-daily/stargazers
[issues-shield]: https://img.shields.io/github/issues/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[issues-url]: https://github.com/Vincentqyw/cv-arxiv-daily/issues

