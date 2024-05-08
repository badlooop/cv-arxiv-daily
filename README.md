[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]

## Updated on 2024.05.08
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
|**2024-05-07**|**Novel View Synthesis with Neural Radiance Fields for Industrial Robot Applications**|神经辐射场（NeRF）已成为一个快速发展的研究领域，有可能彻底改变典型的摄影测量工作流程，例如用于3D场景重建的工作流程。作为输入，NeRF需要具有相应相机姿态和内部方向的多视图图像。在典型的NeRF工作流程中，相机姿态和内部方向是通过运动结构（SfM）预先估计的。但是，生成的新视图的质量很难预测，这取决于不同的参数，如可用图像的数量和分布，以及相关相机姿态和内部方向的准确性。此外，SfM是一个耗时的预处理步骤，其质量在很大程度上取决于图像内容。此外，SfM的未定义的缩放因子阻碍了需要度量信息的后续步骤。在本文中，我们评估了NeRF在工业机器人应用中的潜力。我们提出了一种SfM预处理的替代方案：我们使用连接到工业机器人末端执行器的校准相机捕捉输入图像，并基于机器人运动学确定具有公制尺度的精确相机姿态。然后，我们通过将新观点与基本事实进行比较，并基于集成方法计算内部质量度量，来研究这些观点的质量。出于评估目的，我们获取了多个数据集，这些数据集对典型的工业应用的重建提出了挑战，如反射物体、较差的纹理和精细的结构。我们表明，基于机器人的姿态确定在非要求的情况下达到了与SfM相似的精度，同时在更具挑战性的场景中具有明显的优势。最后，我们给出了在缺乏基本事实的情况下应用集成方法来估计合成新视图的质量的第一个结果。 et.al.|[2405.04345](http://arxiv.org/abs/2405.04345)|null|
|**2024-05-06**|**A Construct-Optimize Approach to Sparse View Synthesis without Camera Pose**|从稀疏的输入图像集进行新的视图合成是一个具有挑战性的问题，具有很大的实际意义，尤其是当相机姿态不存在或不准确时。由于姿态和深度之间的耦合以及单目深度估计的不精确性，在神经辐射场算法中直接优化相机姿态和使用估计的深度通常不会产生好的结果。在本文中，我们利用最近的3D高斯飞溅方法，开发了一种新的无相机姿态稀疏视图合成的构造和优化方法。具体来说，我们通过使用单目深度并将像素投影回3D世界来逐步构建解决方案。在构建过程中，我们通过检测训练视图和相应渲染图像之间的2D对应关系来优化解决方案。我们开发了一个统一的可微分管道，用于相机配准和调整相机姿势和深度，然后进行反向投影。我们还引入了高斯飞溅中预期表面的新概念，这对我们的优化至关重要。这些步骤实现了粗略的解决方案，然后可以使用标准优化方法对其进行低通滤波和细化。我们展示了坦克、寺庙和静态远足数据集的结果，只有三个宽间距的视图，显示出比竞争方法（包括具有近似相机姿态信息的方法）明显更好的质量。此外，即使使用一半的数据集，我们的结果也会随着更多的视图而改进，并优于以前的InstantNGP和Gaussian Splatting算法。 et.al.|[2405.03659](http://arxiv.org/abs/2405.03659)|null|
|**2024-05-06**|**Gaussian Splatting: 3D Reconstruction and Novel View Synthesis, a Review**|基于图像的3D重建是一项具有挑战性的任务，涉及从一组输入图像推断对象或场景的3D形状。基于学习的方法因其直接估计3D形状的能力而受到关注。这篇综述论文的重点是最先进的3D重建技术，包括生成新颖的、看不见的视图。概述了高斯飞溅方法的最新发展，包括输入类型、模型结构、输出表示和训练策略。还讨论了尚未解决的挑战和未来的方向。鉴于该领域的快速进展以及增强3D重建方法的众多机会，对算法进行全面检查似乎至关重要。因此，本研究对高斯散射的最新进展进行了全面的概述。 et.al.|[2405.03417](http://arxiv.org/abs/2405.03417)|null|
|**2024-05-04**|**LidaRF: Delving into Lidar for Neural Radiance Field on Street Scenes**|逼真度模拟在自动驾驶等应用中发挥着至关重要的作用，神经辐射场（NeRF）的进步可以通过自动创建数字3D资产实现更好的可扩展性。然而，由于在较高速度下相机运动基本共线和采样稀疏，街道场景的重建质量受到影响。另一方面，应用程序通常要求从偏离输入的摄影机视图进行渲染，以准确模拟车道变更等行为。在本文中，我们提出了一些见解，可以更好地利用激光雷达数据来提高街景的NeRF质量。首先，我们的框架从激光雷达中学习几何场景表示，该表示与基于隐式网格的表示融合用于辐射解码，从而提供由显式点云提供的更强的几何信息。其次，我们提出了一种鲁棒的遮挡感知深度监督方案，该方案允许通过累积来利用密集的激光雷达点。第三，我们从激光雷达点生成增强训练视图，以便进一步改进。我们的见解转化为在真实驾驶场景下大大改进的新颖视图合成。 et.al.|[2405.00900](http://arxiv.org/abs/2405.00900)|null|
|**2024-05-01**|**RTG-SLAM: Real-time 3D Reconstruction at Scale using Gaussian Splatting**|我们提出了实时高斯SLAM（RTG-SLAM），这是一个使用RGBD相机的实时三维重建系统，用于使用高斯飞溅的大规模环境。该系统具有紧凑的高斯表示和高效的动态高斯优化方案。我们强制每个高斯要么不透明，要么几乎透明，不透明的适合表面和主色，透明的适合残余色。通过以不同于彩色渲染的方式渲染深度，我们让单个不透明高斯很好地拟合局部表面区域，而不需要多个重叠的高斯，从而大大降低了内存和计算成本。对于动态高斯优化，我们明确地为每帧三种类型的像素添加高斯：新观察到的、具有大颜色误差的和具有大深度误差的。我们还将所有高斯分为稳定高斯和不稳定高斯，其中稳定高斯有望很好地拟合先前观察到的RGBD图像，否则不稳定。我们只优化不稳定的高斯，只渲染不稳定高斯占用的像素。这样，要优化的高斯数和要渲染的像素都大大减少，并且可以实时进行优化。我们展示了各种大型场景的实时重建。与最先进的基于NeRF的RGBD SLAM相比，我们的系统实现了相当高质量的重建，但速度约为其两倍，内存成本约为其一半，并在新视图合成的真实性和相机跟踪精度方面表现出卓越的性能。 et.al.|[2404.19706](http://arxiv.org/abs/2404.19706)|null|
|**2024-04-29**|**SAGS: Structure-Aware 3D Gaussian Splatting**|随着NeRFs的出现，3D高斯散射（3D-GS）为实时神经渲染铺平了道路，克服了体积方法的计算负担。继3D-GS的开创性工作之后，有几种方法试图实现可压缩和高保真度性能的替代方案。然而，通过采用几何不可知的优化方案，这些方法忽略了场景的固有3D结构，从而限制了表示的表现力和质量，导致了各种浮点和伪影。在这项工作中，我们提出了一种结构感知的高斯飞溅方法（SAGS），该方法隐式地对场景的几何结构进行编码，这反映了最先进的渲染性能，并降低了基准新视图合成数据集的存储要求。SAGS建立在局部全局图表示的基础上，有助于复杂场景的学习，并强制执行有意义的点位移，以保持场景的几何结构。此外，我们还介绍了一种轻量级的SAGS，使用了一种简单而有效的中点插值方案，该方案展示了场景的紧凑表示，在不依赖任何压缩策略的情况下，大小减少了24 $\times$ 。在多个基准数据集上进行的大量实验表明，在渲染质量和模型大小方面，与最先进的3D-GS方法相比，SAGS具有优越性。此外，我们证明了我们的结构感知方法可以有效地减轻先前方法的浮动伪影和不规则失真，同时获得精确的深度图。项目页面https://eververas.github.io/SAGS/. et.al.|[2404.19149](http://arxiv.org/abs/2404.19149)|null|
|**2024-04-29**|**Simple-RF: Regularizing Sparse Input Radiance Fields with Simpler Solutions**|神经辐射场（NeRF）在场景的照片逼真的自由视图渲染中表现出令人印象深刻的性能。最近对NeRF的改进，如TensoRF和ZipNeRF，与使用隐式表示的NeRF相比，使用显式模型进行更快的优化和渲染。然而，隐式和显式辐射场都需要对给定场景中的图像进行密集采样。当只有一组稀疏的视图可用时，它们的性能会显著下降。研究人员发现，监督辐射场估计的深度有助于以更少的视角有效训练辐射场。深度监督是使用经典方法或在大型数据集上预先训练的神经网络来获得的。前者可能只提供稀疏的监督，而后者可能存在泛化问题。与早期的方法不同，我们试图通过设计增强模型并将其与主辐射场一起训练来学习深度监督。此外，我们的目标是设计一个正则化框架，该框架可以在不同的隐式和显式辐射场中工作。我们观察到，在稀疏输入场景中，这些辐射场模型的某些特征与观察到的图像过度拟合。我们的关键发现是，降低辐射场在位置编码、分解张量分量的数量或哈希表的大小方面的能力，限制了模型学习更简单的解决方案，从而在某些区域估计更好的深度。通过设计基于这种降低的能力的增强模型，我们可以更好地对主辐射场进行深度监督。通过采用上述正则化，我们在包含前向和360 $^\circ$ 场景的流行数据集上使用稀疏输入视图实现了最先进的视图合成性能。 et.al.|[2404.19015](http://arxiv.org/abs/2404.19015)|null|
|**2024-04-29**|**3D Gaussian Splatting with Deferred Reflection**|基于神经和高斯的辐射场方法的出现在新视图合成领域取得了巨大成功。然而，镜面反射仍然是不平凡的，因为众所周知，高频辐射场很难稳定准确地拟合。我们提出了一种延迟着色方法来有效地渲染高斯飞溅的镜面反射。关键的挑战来自环境图反射模型，该模型需要精确的表面法线，同时使用不连续的梯度来限制法线估计。我们利用延迟着色生成的每像素反射梯度来桥接相邻高斯的优化过程，允许几乎正确的法线估计逐渐传播并最终传播到所有反射对象上。我们的方法在合成高质量镜面反射效果方面显著优于最先进的技术和并行工作，证明了合成场景和真实世界场景的峰值信噪比（PSNR）都得到了一致的提高，同时以几乎与香草高斯飞溅相同的帧速率运行。 et.al.|[2404.18454](http://arxiv.org/abs/2404.18454)|null|
|**2024-04-29**|**$ν$-DBA: Neural Implicit Dense Bundle Adjustment Enables Image-Only Driving Scene Reconstruction**|传感器轨迹和3D地图的联合优化是束调整（BA）的一个关键特性，对自动驾驶至关重要。本文提出了$\nu$ -DBA，这是一种使用三维神经隐式曲面进行地图参数化来实现几何密集束平差（DBA）的新框架，该框架使用密集光流预测引导的几何误差来优化地图表面和轨迹姿态。此外，我们通过逐场景自监督对光流模型进行微调，以进一步提高密集映射的质量。我们在多个驾驶场景数据集上的实验结果表明，我们的方法实现了卓越的轨迹优化和密集的重建精度。我们还研究了光度误差和不同的神经几何先验对表面重建和新视图合成性能的影响。我们的方法是朝着在密集束调整中利用神经隐式表示实现更准确的轨迹和详细的环境映射迈出的重要一步。 et.al.|[2404.18439](http://arxiv.org/abs/2404.18439)|null|
|**2024-04-25**|**Depth Supervised Neural Surface Reconstruction from Airborne Imagery**|虽然最初是为新颖的视图合成而开发的，但神经辐射场（NeRF）最近已成为多视图立体（MVS）的替代品。在一系列研究活动的触发下，已经获得了有希望的结果，尤其是在无纹理、透明和反射表面方面，而这些场景对传统的基于MVS的方法仍然具有挑战性。然而，这些调查大多集中在近距离场景上，对空中场景的研究仍然缺失。对于这项任务，NeRF在图像冗余度低和数据证据薄弱的区域面临潜在的困难，如经常在街道峡谷、立面或建筑阴影中发现的那样。此外，训练这样的网络在计算上是昂贵的。因此，我们工作的目的有两个：首先，我们研究NeRFs对代表不同特征的航空图像块的适用性，如仅最低点、倾斜和高分辨率图像。其次，在这些调查过程中，我们证明了从联络点测量中积分深度先验的好处，这些测量是在预先假设的束块调整过程中提供的。我们的工作基于最先进的框架VolSDF，该框架通过符号距离函数（SDF）对3D场景进行建模，因为与普通NeRF中的标准体积表示相比，这更适用于表面重建。为了进行评估，将基于NeRF的重建与航空图像的公开基准数据集的结果进行比较。 et.al.|[2404.16429](http://arxiv.org/abs/2404.16429)|null|

<p align=right>(<a href=#updated-on-20240508>back to top</a>)</p>

## 3D Reconstruction

|Publish Date|Title|Abstract|PDF|Code|
|---|---|---|---|---|
|**2024-05-06**|**MVDiff: Scalable and Flexible Multi-View Diffusion for 3D Object Reconstruction from Single-View**|为3D重建任务生成一致的多个视图仍然是对现有图像到3D扩散模型的挑战。通常，将3D表示合并到扩散模型中会降低模型的速度以及可推广性和质量。本文提出了一个通用框架，从单个图像或利用场景表示变换器和视图条件扩散模型生成一致的多视图图像。在模型中，我们引入了极线几何约束和多视图注意力，以增强三维一致性。从一个图像输入中，我们的模型能够生成超过评估指标基线方法的3D网格，包括PSNR、SSIM和LPIPS。 et.al.|[2405.03894](http://arxiv.org/abs/2405.03894)|null|
|**2024-05-06**|**Gaussian Splatting: 3D Reconstruction and Novel View Synthesis, a Review**|基于图像的3D重建是一项具有挑战性的任务，涉及从一组输入图像推断对象或场景的3D形状。基于学习的方法因其直接估计3D形状的能力而受到关注。这篇综述论文的重点是最先进的3D重建技术，包括生成新颖的、看不见的视图。概述了高斯飞溅方法的最新发展，包括输入类型、模型结构、输出表示和训练策略。还讨论了尚未解决的挑战和未来的方向。鉴于该领域的快速进展以及增强3D重建方法的众多机会，对算法进行全面检查似乎至关重要。因此，本研究对高斯散射的最新进展进行了全面的概述。 et.al.|[2405.03417](http://arxiv.org/abs/2405.03417)|null|
|**2024-05-05**|**Morphokinematical study of the planetary nebula Me2-1: Unveiling its point-symmetric and unusual physical structure**|（摘要）我们展示了几条发射线的窄带图像，以及Me2-1的高分辨率和中分辨率长缝光谱，以研究其形态和3D结构、物理参数和化学丰度。我们在Me2-1中发现：一个椭圆环；两个细长的弯曲结构（帽），其包含三对亮点对称（PS）结；所述环的壳内部；以及微弱的光晕或附着的外壳。在所有图像中都观察到了帽，PS结仅在低激发发射线图像中观察到。这些结构也在高分辨率的长狭缝光谱中被识别。3D重建显示，Me2-1由一个几乎是极点的环和一个几乎球形的外壳组成，盖子和PS结连接在外壳上。帽状物和PS结最有可能追踪沿着摆动轴喷出的高速准直双极外流与球壳碰撞、减速并保持附着的位置。尽管Me2-1中的主要激发机制被发现是光电离，但PS结中的冲击的贡献是由它们的发射线比提出的。在行星状星云中，准直外流和带有球形外壳的环的结合是不寻常的。我们推测，如果两颗行星都在祖先的渐近巨星分支阶段进入共同的包络演化，那么这两颗行星可能都参与了Me2-1的形成，每颗行星的质量都小于一个木星。一颗行星被潮汐破坏，在中心恒星周围形成吸积盘，准直的双极性外流从吸积盘喷出；另一颗行星幸存下来，导致吸积盘摆动。导出的物理参数和化学丰度与之前的分析中获得的相似，丰度也指向Me2-1的低质量祖先。 et.al.|[2405.02938](http://arxiv.org/abs/2405.02938)|null|
|**2024-05-05**|**MVIP-NeRF: Multi-view 3D Inpainting on NeRF Scenes via Diffusion Prior**|尽管出现了基于显式RGB和深度2D修复监督的成功NeRF修复方法，但这些方法固有地受到其底层2D修复器能力的约束。这是由于两个关键原因：（i）独立修复组成图像会导致视图不一致的图像，以及（ii）2D修复器难以确保高质量的几何图形完成和与修复的RGB图像对齐。为了克服这些限制，我们提出了一种称为MVIP NeRF的新方法，该方法利用扩散先验的潜力进行NeRF修复，同时解决外观和几何方面的问题。MVIP NeRF跨多个视图执行联合修复，以达到一致的解决方案，这是通过基于分数蒸馏采样（SDS）的迭代优化过程实现的。除了恢复渲染的RGB图像外，我们还提取法线贴图作为几何表示，并定义法线SDS损失，以促进精确的几何修复和与外观对齐。此外，我们制定了一个多视图SDS评分函数，以从不同的视图图像中同时提取生成先验，确保在处理大的视图变化时一致的视觉完成。我们的实验结果显示出比以前的NeRF修复方法更好的外观和几何恢复。 et.al.|[2405.02859](http://arxiv.org/abs/2405.02859)|null|
|**2024-05-04**|**Beyond Unimodal Learning: The Importance of Integrating Multiple Modalities for Lifelong Learning**|当人类擅长持续学习时，深度神经网络表现出灾难性的遗忘。大脑允许有效CL的一个显著特征是，它利用多种模式进行学习和推理，而这在DNN中尚未得到充分探索。因此，我们研究了多种模式在减轻遗忘中的作用和相互作用，并为多模式持续学习引入了一个基准。我们的研究结果表明，利用来自多种模态的多个视图和互补信息，使模型能够学习更准确、更稳健的表示。这使得模型不那么容易受到模态特定规律的影响，并大大减少了遗忘。此外，我们观察到，个体模态对分布变化表现出不同程度的鲁棒性。最后，我们提出了一种方法，通过利用每个模态中数据点之间的关系结构相似性来集成和对齐来自不同模态的信息。我们的方法设置了一个强大的基线，可以实现单模式和多模式推理。我们的研究为进一步探索多种模式在实现CL中的作用提供了一个有希望的案例，并为未来的研究提供了标准基准。 et.al.|[2405.02766](http://arxiv.org/abs/2405.02766)|null|
|**2024-05-04**|**ActiveNeuS: Active 3D Reconstruction using Neural Implicit Surface Uncertainty**|3D场景重建中的主动学习已经得到了广泛的研究，因为选择信息丰富的训练视图对重建至关重要。最近，神经辐射场（NeRF）变体在使用图像渲染或几何不确定性的主动3D重建中显示出性能提高。然而，在选择信息视图时同时考虑这两种不确定性仍然没有得到探索，而利用不同类型的不确定性可以减少在输入稀疏的早期训练阶段出现的偏差。在本文中，我们提出了ActiveNeuS，它在考虑两种不确定性的情况下评估候选视图。ActiveNeuS提供了一种积累图像渲染不确定性的方法，同时避免了估计密度可能引入的偏差。ActiveNeuS计算神经隐含的表面不确定性，提供颜色不确定性和表面信息。它通过使用表面信息和网格来有效地处理偏差，从而能够快速选择不同的视点。我们的方法优于以前在流行数据集Blender和DTU上的工作，表明ActiveNeuS选择的视图显著提高了性能。 et.al.|[2405.02568](http://arxiv.org/abs/2405.02568)|null|
|**2024-05-03**|**CVTGAD: Simplified Transformer with Cross-View Attention for Unsupervised Graph-level Anomaly Detection**|无监督图级异常检测（UGAD）在化学分析和生物信息学等关键学科中取得了显著的成绩。现有的UGAD范式通常采用数据扩充技术来构建多个视图，然后采用不同的策略从不同的视图中获得表示，以共同进行UGAD。然而，以前的大多数工作只从有限的感受野中考虑节点/图之间的关系，导致一些关键的结构模式和特征信息被忽视。此外，现有的大多数方法以并行的方式分别考虑不同的视图，无法直接探索不同视图之间的相互关系。因此，需要一种具有更大感受野的方法，可以直接探索不同观点之间的相互关系。在本文中，我们提出了一种新的用于无监督图级异常检测的具有交叉视图注意的简化变换器，即CVTGAD。为了增加感受野，我们构建了一个简化的基于转换器的模块，从图内和图间的角度利用节点/图之间的关系。此外，我们设计了一种跨视图注意力机制，直接利用不同视图之间的视图共生，在节点级和图级弥合视图间的差距。据我们所知，这是首次将transformer和cross-attention应用于UGAD，实现了图神经网络和transformer的协同工作。在3个领域的15个真实世界数据集上进行的大量实验证明了CVTGAD在UGAD任务上的优越性。代码位于\url{https://github.com/jindongli-Ai/CVTGAD}. et.al.|[2405.02359](http://arxiv.org/abs/2405.02359)|**[link](https://github.com/jindongli-ai/cvtgad)**|
|**2024-05-04**|**HandSSCA: 3D Hand Mesh Reconstruction with State Space Channel Attention from RGB images**|从单个RGB图像重建手网格是一项具有挑战性的任务，因为手经常被物体遮挡。以前的大多数工作都试图引入更多的附加信息并采用注意力机制来改善3D重建结果，但这会增加计算复杂性。这一观察结果促使我们提出一种新的简洁架构，同时提高计算效率。在这项工作中，我们提出了一种简单有效的三维手部网格重建网络HandSSCA，它是第一个将状态空间建模纳入手部姿态估计领域的网络。在网络中，我们设计了一个新的状态空间通道注意力模块，该模块扩展了有效的感觉场，提取了空间维度上的手部特征，并增强了通道维度上的手部区域特征。这种设计有助于重建完整而详细的手部网格。在具有挑战性手对象遮挡的知名数据集（如FREIHAND、DEXYCB和HO3D）上进行的大量实验表明，我们提出的HandSSCA在保持最小参数计数的同时实现了最先进的性能。 et.al.|[2405.01066](http://arxiv.org/abs/2405.01066)|null|
|**2024-05-01**|**Coherent 3D Portrait Video Reconstruction via Triplane Fusion**|最近在单图像3D肖像重建方面的突破使远程呈现系统能够实时流式传输来自单个相机的3D肖像视频，从而有可能使远程呈现民主化。然而，每帧3D重建表现出时间上的不一致性并且忘记了用户的外观。另一方面，自再现方法可以通过驱动个性化的3D先验来渲染连贯的3D肖像，但不能忠实地重建用户的每帧外观（例如，面部表情和照明）。在这项工作中，我们认识到需要保持连贯的身份和动态的每帧外观，以实现最佳的真实感。为此，我们提出了一种新的基于融合的方法，该方法将个性化的3D主题先验与每帧信息融合，生成时间稳定的3D视频，并忠实地重建用户的每帧外观。我们的基于编码器的方法仅使用由表达条件的3D GAN产生的合成数据进行训练，在工作室和野外数据集上实现了最先进的3D重建精度和时间一致性。 et.al.|[2405.00794](http://arxiv.org/abs/2405.00794)|null|
|**2024-05-01**|**Depth Priors in Removal Neural Radiance Fields**|神经辐射场（NeRF）在三维重建和生成新视图方面显示出令人印象深刻的结果。NeRF的一个关键挑战是重建场景的编辑，如对象移除，这需要在多个视图之间保持一致性，并确保高质量的合成视角。先前的研究结合了深度先验，通常来自激光雷达或COLMAP提供的稀疏深度测量，以提高NeRF中的目标去除性能。然而，这些方法要么昂贵，要么耗时。在本文中，我们提出了一种新的方法，将单目深度估计与基于NeRF的对象去除模型相结合，以显著减少时间消耗，提高场景生成和对象去除的鲁棒性和质量。我们在KITTI数据集上对COLMAP的密集深度重建进行了全面评估，以验证其在深度图生成中的准确性。我们的研究结果表明，COLMAP可以作为地面实况深度图的有效替代方案，在这种情况下，这些信息缺失或获取成本高昂。此外，我们将各种单目深度估计方法集成到去除NeRF模型中，即SpinNeRF，以评估其提高物体去除性能的能力。我们的实验结果突出了单目深度估计在显著改善NeRF应用方面的潜力。 et.al.|[2405.00630](http://arxiv.org/abs/2405.00630)|null|

<p align=right>(<a href=#updated-on-20240508>back to top</a>)</p>

## Diffusion

|Publish Date|Title|Abstract|PDF|Code|
|---|---|---|---|---|
|**2024-05-07**|**Tactile-Augmented Radiance Fields**|我们提出了一种场景表示，我们称之为触觉增强辐射场（TaRF），它将视觉和触摸带入共享的3D空间。该表示可以用于估计场景内给定3D位置的视觉和触觉信号。我们从一组照片和稀疏采样的触摸探针中捕捉场景的TaRF。我们的方法利用了两个见解：（i）常见的基于视觉的触摸传感器建立在普通相机上，因此可以使用多视图几何的方法将其注册到图像中；（ii）场景的视觉和结构相似的区域共享相同的触觉特征。我们使用这些见解将触摸信号注册到捕捉的视觉场景中，并训练条件扩散模型，该模型提供了从神经辐射场渲染的RGB-D图像，生成其相应的触觉信号。为了评估我们的方法，我们收集了一个TaRF数据集。该数据集包含比以前的真实世界数据集更多的触摸样本，并且它为每个捕获的触摸信号提供空间对齐的视觉信号。我们展示了我们的跨模态生成模型的准确性，以及捕获的视觉触觉数据在几个下游任务中的实用性。项目页面：https://dou-yiming.github.io/TaRF et.al.|[2405.04534](http://arxiv.org/abs/2405.04534)|null|
|**2024-05-07**|**Edit-Your-Motion: Space-Time Diffusion Decoupling Learning for Video Motion Editing**|现有的基于扩散的视频编辑方法在运动编辑中取得了令人印象深刻的结果。现有的大多数方法都集中在编辑视频和参考视频之间的运动对准上。然而，这些方法并不限制视频的背景和对象内容保持不变，这使得用户有可能生成意外的视频。在本文中，我们提出了一种名为“编辑你的运动”的一次性视频运动编辑方法，该方法只需要一对文本视频进行训练。具体来说，我们设计了详细提示引导学习策略（DPL）来解耦时空扩散模型中的时空特征。DPL将学习对象内容和运动分为两个训练阶段。在第一个训练阶段，我们专注于学习空间特征（对象内容的特征），并通过混洗来分解视频帧中的时间关系。我们进一步提出了递归因果注意（RC Attn）来从无序的视频帧中学习对象的一致内容特征。在第二个训练阶段，我们恢复视频帧中的时间关系，以学习时间特征（背景和对象运动的特征）。我们还采用噪声约束损失来平滑帧间差异。最后，在推理阶段，我们通过两个分支结构（编辑分支和重构分支）将源对象的内容特征注入到编辑分支中。使用“编辑你的运动”，用户可以编辑源视频中对象的运动，以生成更令人兴奋和多样化的视频。综合的定性实验、定量实验和用户偏好研究表明，“编辑你的运动”比其他方法性能更好。 et.al.|[2405.04496](http://arxiv.org/abs/2405.04496)|null|
|**2024-05-07**|**CloudDiff: Super-resolution ensemble retrieval of cloud properties for all day using the generative diffusion model**|云在地球的水和能源循环中发挥着至关重要的作用，这突出了关于云相位和性质的高时空分辨率数据对准确的数值建模和天气预测的重要性。目前，中分辨率成像光谱仪（MODIS）提供的云产品空间分辨率为1公里。然而，这些产品的重新访问周期很长。本研究开发了一个生成扩散模型（捐赠为CloudDiff），用于高时空云相位和特性的超分辨率检索，适用于白天和晚上。利用2公里空间分辨率的Himawari-8高级Himawari成像仪（AHI）热红外（TIR）辐射和视景几何形状作为条件，以及白天的MODIS产品作为目标，该模型可以以1公里空间分辨率和10分钟时间分辨率生成云相（CLP）、云顶高度（CTH）、云光学厚度（COT）和云有效半径（CER）。与确定性超分辨率方法相比，条件扩散模型可以生成更清晰的图像并捕捉更精细的局部特征。它根据潜在的概率分布绘制多个样本，实现检索不确定性评估。评估显示，云阶段与CloudDiff和MODIS云产品的属性一致。发现集合均值提高了检索的准确性和可信度，优于确定性模型。 et.al.|[2405.04483](http://arxiv.org/abs/2405.04483)|null|
|**2024-05-07**|**Derivation of kinetic and diffusion equations from a hard-sphere Rayleigh gas using collision trees and semigroups**|我们将重新审视经典问题，即理解直径为 $\varepsilon$的$N$硬球的各种确定性动力学的统计数据，以及Boltzmann Grad标度中的随机初始数据，因为$\varepilon$趋于零，$N$ 趋于无穷大。在瑞利气体的情况下，使用半群方法来描述与物理轨迹相关的碰撞树上的概率测度，显示了经验粒子动力学到玻尔兹曼型动力学的收敛性。作为一个应用，我们通过进一步的重新缩放导出了扩散方程。 et.al.|[2405.04449](http://arxiv.org/abs/2405.04449)|null|
|**2024-05-07**|**Brownian Motion on The Spider Like Quantum Graphs**|本文包含了最简单量子图spider上布朗运动的概率分析：一个N半轴系统，仅在图的原点通过最简单的（所谓的Kirchhoff）粘合条件连接。这种图上扩散的极限定理，特别是当 $N\to\infty$与经典情况$N=2$ （全轴）显著不同时。另外的结果涉及蜘蛛拉普拉斯算子的谱测度的性质和相应的广义傅立叶变换。本文的续文将包括对蜘蛛图上一类Schr“odinger算子的谱的研究：受无界势和相关相变扰动的拉普拉斯算子。 et.al.|[2405.04439](http://arxiv.org/abs/2405.04439)|null|
|**2024-05-07**|**Learning local Dirichlet-to-Neumann maps of nonlinear elliptic PDEs with rough coefficients**|涉及高对比度和振荡系数的偏微分方程（PDE）在科学和工业应用中很常见。这些偏微分方程的数值近似是一项具有挑战性的任务，例如可以通过多尺度有限元分析来解决。对于线性问题，多尺度有限元方法（MsFEM）已得到很好的建立，并且已知一些对非线性偏微分方程的可行扩展。然而，该方法的一些特征似乎本质上是基于线性的。特别是，传统的MsFEM依赖于计算的重用。例如，刚度矩阵可以只计算一次，同时用于几个右侧，或者作为多级迭代算法的一部分。粗略地说，该方法的离线阶段相当于预组装局部线性狄利克雷到诺依曼（DtN）算子。我们给出了一些关于MsFEM与机器学习工具相结合的初步结果。通过学习局部非线性DtN映射，实现了MsFEM对非线性问题的扩展。基于学习的多尺度方法在一组模型非线性偏微分方程上进行了测试，该模型涉及 $p-$ 拉普拉斯算子和退化非线性扩散。 et.al.|[2405.04433](http://arxiv.org/abs/2405.04433)|null|
|**2024-05-07**|**Josephson threshold detector in the phase diffusion regime**|我们证明，通过利用相扩散机制，可以显著提高基于Al Josephson结的阈值检测器的性能。当探测器的逃逸动力学切换到该状态时，同时观察到暗计数率和开关电流的标准偏差的降低。然而，这种效应对于（i）低于100nA的临界电流和（ii）几百毫开尔文量级的温度是必不可少的。重要的是，对于这种探测器来说，最佳性能发生在有限的温度下，使得微波单光子探测即使在亚K范围内也是可行的。讨论了对这些发现的可能解释。 et.al.|[2405.04426](http://arxiv.org/abs/2405.04426)|null|
|**2024-05-07**|**Mathematical Modeling of $^{18}$F-Fluoromisonidazole ($^{18}$F-FMISO) Radiopharmaceutical Transport in Vascularized Solid Tumors**|$^{18}$F-Fluoromisonidazole（$^{18}$F-FMISO）是一种非常有前途的正电子发射断层扫描放射性药物，用于识别实体瘤中的缺氧区域。这项研究采用时空多尺度数学模型来探索不同水平的血管生成如何影响放射性药物在肿瘤内的转运。在这项研究中，采用了两种毛细管网络分布不均匀的肿瘤几何形状来合并不同程度的微血管密度。通过模拟血管生成过程生成异质性和血管化肿瘤的合成图像。所提出的多尺度时空模型考虑了肿瘤微环境中复杂的生理和生物化学因素，如放射性药物的跨血管运输，其通过扩散和对流机制进入间质空间，并最终被肿瘤细胞吸收。结果表明，在肿瘤生长的不同阶段，$^{18}$F-FMISO摄取的定量和半定量指标在空间和时间上都不同。均匀血管化肿瘤中高微血管密度的存在增加了细胞摄取，因为它允许更有效地释放和快速分布放射性药物分子。与异质性血管化肿瘤相比，这导致摄取增强。在肿瘤中微血管的不均匀和均匀分布中，扩散传输机制比对流更明显。这项研究的发现揭示了$^{18}$ F-FMISO放射性药物分布及其在肿瘤微环境中的输送现象，帮助肿瘤学家进行日常决策。 et.al.|[2405.04418](http://arxiv.org/abs/2405.04418)|null|
|**2024-05-07**|**Community Detection for Heterogeneous Multiple Social Networks**|社区在理解社交网络中的用户行为和网络特征方面发挥着至关重要的作用。一些用户可以为了各种目的同时使用多个社交网络。这些用户被称为跨接不同社交网络的重叠用户。检测多个社交网络中的社区对于网络之间的互动挖掘、信息传播和行为迁移分析至关重要。针对多个异构社交网络，提出了一种基于非负矩阵三因子分解的社区检测方法，该方法建立了一个公共一致性矩阵来表示全局融合社区。具体而言，所提出的方法包括基于网络结构和内容相似性创建邻接矩阵，然后创建对齐矩阵，以区分不同社交网络中的重叠用户。利用生成的对齐矩阵，该方法可以通过检测网络中重叠的用户社区来提高全局社区的融合度。在Twitter、Instagram和汤博乐数据集上使用新的指标评估了所提出方法的有效性。实验结果表明，它在社区质量和社区融合方面具有优越的性能。 et.al.|[2405.04371](http://arxiv.org/abs/2405.04371)|null|
|**2024-05-07**|**Diff-IP2D: Diffusion-Based Hand-Object Interaction Prediction on Egocentric Videos**|了解人类在手-物交互过程中的行为对于服务机器人操作和扩展现实的应用至关重要。为了实现这一点，最近的一些工作被提出在人类以自我为中心的视频中同时预测手的轨迹和物体的可供性。它们被视为未来手-物交互的表现，表明人类潜在的运动和动机。然而，现有的方法大多采用自回归范式进行单向预测，在整体未来序列中缺乏相互约束，并且沿着时间轴积累误差。同时，这些作品基本上忽略了相机自我运动对第一人称视角预测的影响。为了解决这些局限性，我们提出了一种新的基于扩散的交互预测方法，即Diff-IP2D，以迭代非自回归的方式同时预测未来的手轨迹和物体可供性。我们将连续的二维图像转换到潜在特征空间中，并设计一个去噪扩散模型来预测基于过去潜在交互特征的未来潜在交互特征。运动特征被进一步集成到条件去噪过程中，以使Diff-IP2D能够感知相机佩戴者的动态，从而进行更准确的交互预测。实验结果表明，我们的方法在现成指标和我们提出的新评估协议方面都显著优于最先进的基线。这突出了利用生成范式进行2D手-物体交互预测的功效。Diff-IP2D的代码将在发布https://github.com/IRMVLab/Diff-IP2D. et.al.|[2405.04370](http://arxiv.org/abs/2405.04370)|null|

<p align=right>(<a href=#updated-on-20240508>back to top</a>)</p>

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

<p align=right>(<a href=#updated-on-20240508>back to top</a>)</p>

[contributors-shield]: https://img.shields.io/github/contributors/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[contributors-url]: https://github.com/Vincentqyw/cv-arxiv-daily/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[forks-url]: https://github.com/Vincentqyw/cv-arxiv-daily/network/members
[stars-shield]: https://img.shields.io/github/stars/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[stars-url]: https://github.com/Vincentqyw/cv-arxiv-daily/stargazers
[issues-shield]: https://img.shields.io/github/issues/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[issues-url]: https://github.com/Vincentqyw/cv-arxiv-daily/issues

