[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]

## Updated on 2024.05.14
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
|**2024-05-10**|**I3DGS: Improve 3D Gaussian Splatting from Multiple Dimensions**|3D Gaussian Splatting是一种新的三维视图合成方法，与传统的神经渲染技术相比，它可以获得隐含的神经学习渲染结果，但保持更高清晰度的快速渲染速度。但是，对于实际应用来说，在三维高斯散射上仍然很难达到足够快的效率。为了解决这个问题，我们提出了I3DS，一种综合模型性能改进的评估解决方案和实验测试。从原始三维高斯飞溅的多个重要层面或维度，我们进行了2000多种不同的实验，以测试所选择的不同项目和组件如何影响三维高斯飞溅模型的训练效率。在本文中，我们将分享关于如何提高训练、绩效以及模型的不同项目所造成的影响的丰富而有意义的经验和方法。提出了一种特殊但正常的95进制整数压缩和94进制浮点压缩ASCII编解码机制。将记录许多真实有效的实验和测试结果或现象。经过一系列合理的微调，I3DS可以获得比之前更好的性能提升。项目代码以开源形式提供。 et.al.|[2405.06408](http://arxiv.org/abs/2405.06408)|null|
|**2024-05-10**|**MGS-SLAM: Monocular Sparse Tracking and Gaussian Mapping with Depth Smooth Regularization**|本文介绍了一种基于高斯散射的密集视觉同步定位与映射（VSLAM）的新框架。近年来，基于高斯飞溅的SLAM取得了很好的结果，但它依赖于RGB-D输入，跟踪能力较弱。为了解决这些局限性，我们首次将高级稀疏视觉里程计与密集高斯散射场景表示独特地集成在一起，从而消除了对基于高斯散射的SLAM系统典型的深度图的依赖，并增强了跟踪鲁棒性。在这里，稀疏视觉里程计在RGB流中跟踪相机姿势，而高斯散射处理地图重建。这些组件通过多视图立体（MVS）深度估计网络互连。我们提出了一种深度平滑损失来减少估计深度图的负面影响。此外，稀疏视觉里程计和密集高斯图之间的尺度一致性通过稀疏密集调整环（SDAR）得以保持。我们已经在各种合成和真实世界的数据集上评估了我们的系统。我们的姿态估计精度超过了现有方法，并达到了最先进的性能。此外，在新的视图合成保真度方面，它优于以前的单目方法，与利用RGB-D输入的神经SLAM系统的结果相匹配。 et.al.|[2405.06241](http://arxiv.org/abs/2405.06241)|null|
|**2024-05-09**|**FastScene: Text-Driven Fast 3D Indoor Scene Generation via Panoramic Gaussian Splatting**|文本驱动的3D室内场景生成具有广泛的应用，从游戏和智能家居到AR/VR应用。快速高保真的场景生成对于确保用户友好的体验至关重要。然而，现有方法的特点是生成过程漫长，或者需要复杂的手动指定运动参数，这给用户带来了不便。此外，这些方法通常依赖于窄场视点迭代生成，从而影响全局一致性和整体场景质量。为了解决这些问题，我们提出了FastScene，这是一个用于快速、更高质量的3D场景生成的框架，同时保持场景一致性。具体来说，在给定文本提示的情况下，我们生成全景图并估计其深度，因为全景图包含了关于整个场景的信息，并表现出明确的几何约束。为了获得高质量的新颖视图，我们引入了粗略视图合成（CVS）和渐进新颖视图修复（PNVI）策略，以确保场景一致性和视图质量。随后，我们利用多视图投影（MVP）形成透视图，并应用3D高斯散射（3DGS）进行场景重建。综合实验表明，FastScene在生成速度和质量上都优于其他方法，具有更好的场景一致性。值得注意的是，FastScene仅在文本提示的引导下，就可以在15分钟内生成3D场景，这比最先进的方法快至少一个小时，使其成为用户友好的场景生成典范。 et.al.|[2405.05768](http://arxiv.org/abs/2405.05768)|null|
|**2024-05-09**|**RPBG: Towards Robust Neural Point-based Graphics in the Wild**|基于点的表示最近在新颖的视图合成中流行起来，因为它们具有直观的几何表示、简单的操作和更快的收敛等独特优势。然而，根据我们的观察，这些基于点的神经重渲染方法预计只能在理想条件下表现良好，并且会遇到噪声、斑点点和无边界场景，这些问题很难处理，但在实际应用中很常见。为此，我们重新审视了一种有影响力的方法，称为基于神经点的图形（NPBG），作为我们的基线，并提出了稳健的基于点图形（RPBG）。我们深入分析了阻碍NPBG在通用数据集上实现令人满意的渲染的因素，并相应地改革了管道，使其对野外不同的数据集更具鲁棒性。受图像恢复实践的启发，我们极大地增强了神经渲染器，以实现基于注意力的点可见性校正和不完全光栅化的修复，只需可接受的开销。我们还寻求一种简单而轻量级的环境建模替代方案和一种迭代方法来缓解较差的几何形状问题。通过对具有不同拍摄条件和相机轨迹的广泛数据集进行彻底评估，RPBG稳定地以很大的优势优于基线，并表现出其相对于最先进的基于NeRF的变体的强大鲁棒性。代码可在https://github.com/QT-Zhu/RPBG. et.al.|[2405.05663](http://arxiv.org/abs/2405.05663)|null|
|**2024-05-08**|**GDGS: Gradient Domain Gaussian Splatting for Sparse Representation of Radiance Fields**|3D高斯飞溅方法越来越流行。然而，它们直接作用于信号，导致信号的密集表示。即使使用一些技术，如修剪或蒸馏，结果仍然很密集。在本文中，我们建议对原始信号的梯度进行建模。梯度比原始信号稀疏得多。因此，梯度使用更少的高斯飞溅，从而在训练和渲染过程中获得更高效的存储，从而获得更高的计算性能。由于稀疏性，在视图合成过程中，只需要少量像素，从而获得高得多的计算性能（快 $100\sim 1000\times$ ）。并且可以通过求解具有线性计算复杂性的泊松方程来从梯度中恢复2D图像。进行了几个实验来验证梯度的稀疏性和所提出方法的计算性能。该方法可以应用于各种应用，如人体建模和室内环境建模。 et.al.|[2405.05446](http://arxiv.org/abs/2405.05446)|null|
|**2024-05-07**|**Novel View Synthesis with Neural Radiance Fields for Industrial Robot Applications**|神经辐射场（NeRF）已成为一个快速发展的研究领域，有可能彻底改变典型的摄影测量工作流程，例如用于3D场景重建的工作流程。作为输入，NeRF需要具有相应相机姿态和内部方向的多视图图像。在典型的NeRF工作流程中，相机姿态和内部方向是通过运动结构（SfM）预先估计的。但是，生成的新视图的质量很难预测，这取决于不同的参数，如可用图像的数量和分布，以及相关相机姿态和内部方向的准确性。此外，SfM是一个耗时的预处理步骤，其质量在很大程度上取决于图像内容。此外，SfM的未定义的缩放因子阻碍了需要度量信息的后续步骤。在本文中，我们评估了NeRF在工业机器人应用中的潜力。我们提出了一种SfM预处理的替代方案：我们使用连接到工业机器人末端执行器的校准相机捕捉输入图像，并基于机器人运动学确定具有公制尺度的精确相机姿态。然后，我们通过将新观点与基本事实进行比较，并基于集成方法计算内部质量度量，来研究这些观点的质量。出于评估目的，我们获取了多个数据集，这些数据集对典型的工业应用的重建提出了挑战，如反射物体、较差的纹理和精细的结构。我们表明，基于机器人的姿态确定在非要求的情况下达到了与SfM相似的精度，同时在更具挑战性的场景中具有明显的优势。最后，我们给出了在缺乏基本事实的情况下应用集成方法来估计合成新视图的质量的第一个结果。 et.al.|[2405.04345](http://arxiv.org/abs/2405.04345)|null|
|**2024-05-06**|**A Construct-Optimize Approach to Sparse View Synthesis without Camera Pose**|从稀疏的输入图像集进行新的视图合成是一个具有挑战性的问题，具有很大的实际意义，尤其是当相机姿态不存在或不准确时。由于姿态和深度之间的耦合以及单目深度估计的不精确性，在神经辐射场算法中直接优化相机姿态和使用估计的深度通常不会产生好的结果。在本文中，我们利用最近的3D高斯飞溅方法，开发了一种新的无相机姿态稀疏视图合成的构造和优化方法。具体来说，我们通过使用单目深度并将像素投影回3D世界来逐步构建解决方案。在构建过程中，我们通过检测训练视图和相应渲染图像之间的2D对应关系来优化解决方案。我们开发了一个统一的可微分管道，用于相机配准和调整相机姿势和深度，然后进行反向投影。我们还引入了高斯飞溅中预期表面的新概念，这对我们的优化至关重要。这些步骤实现了粗略的解决方案，然后可以使用标准优化方法对其进行低通滤波和细化。我们展示了坦克、寺庙和静态远足数据集的结果，只有三个宽间距的视图，显示出比竞争方法（包括具有近似相机姿态信息的方法）明显更好的质量。此外，即使使用一半的数据集，我们的结果也会随着更多的视图而改进，并优于以前的InstantNGP和Gaussian Splatting算法。 et.al.|[2405.03659](http://arxiv.org/abs/2405.03659)|null|
|**2024-05-06**|**Gaussian Splatting: 3D Reconstruction and Novel View Synthesis, a Review**|基于图像的3D重建是一项具有挑战性的任务，涉及从一组输入图像推断对象或场景的3D形状。基于学习的方法因其直接估计3D形状的能力而受到关注。这篇综述论文的重点是最先进的3D重建技术，包括生成新颖的、看不见的视图。概述了高斯飞溅方法的最新发展，包括输入类型、模型结构、输出表示和训练策略。还讨论了尚未解决的挑战和未来的方向。鉴于该领域的快速进展以及增强3D重建方法的众多机会，对算法进行全面检查似乎至关重要。因此，本研究对高斯散射的最新进展进行了全面的概述。 et.al.|[2405.03417](http://arxiv.org/abs/2405.03417)|null|
|**2024-05-04**|**LidaRF: Delving into Lidar for Neural Radiance Field on Street Scenes**|逼真度模拟在自动驾驶等应用中发挥着至关重要的作用，神经辐射场（NeRF）的进步可以通过自动创建数字3D资产实现更好的可扩展性。然而，由于在较高速度下相机运动基本共线和采样稀疏，街道场景的重建质量受到影响。另一方面，应用程序通常要求从偏离输入的摄影机视图进行渲染，以准确模拟车道变更等行为。在本文中，我们提出了一些见解，可以更好地利用激光雷达数据来提高街景的NeRF质量。首先，我们的框架从激光雷达中学习几何场景表示，该表示与基于隐式网格的表示融合用于辐射解码，从而提供由显式点云提供的更强的几何信息。其次，我们提出了一种鲁棒的遮挡感知深度监督方案，该方案允许通过累积来利用密集的激光雷达点。第三，我们从激光雷达点生成增强训练视图，以便进一步改进。我们的见解转化为在真实驾驶场景下大大改进的新颖视图合成。 et.al.|[2405.00900](http://arxiv.org/abs/2405.00900)|null|
|**2024-05-09**|**RTG-SLAM: Real-time 3D Reconstruction at Scale using Gaussian Splatting**|我们提出了实时高斯SLAM（RTG-SLAM），这是一个使用RGBD相机的实时三维重建系统，用于使用高斯飞溅的大规模环境。该系统具有紧凑的高斯表示和高效的动态高斯优化方案。我们强制每个高斯要么不透明，要么几乎透明，不透明的适合表面和主色，透明的适合残余色。通过以不同于彩色渲染的方式渲染深度，我们让单个不透明高斯很好地拟合局部表面区域，而不需要多个重叠的高斯，从而大大降低了内存和计算成本。对于动态高斯优化，我们明确地为每帧三种类型的像素添加高斯：新观察到的、具有大颜色误差的和具有大深度误差的。我们还将所有高斯分为稳定高斯和不稳定高斯，其中稳定高斯有望很好地拟合先前观察到的RGBD图像，否则不稳定。我们只优化不稳定的高斯，只渲染不稳定高斯占用的像素。这样，要优化的高斯数和要渲染的像素都大大减少，并且可以实时进行优化。我们展示了各种大型场景的实时重建。与最先进的基于NeRF的RGBD SLAM相比，我们的系统实现了相当高质量的重建，但速度约为其两倍，内存成本约为其一半，并在新视图合成的真实性和相机跟踪精度方面表现出卓越的性能。 et.al.|[2404.19706](http://arxiv.org/abs/2404.19706)|null|

<p align=right>(<a href=#updated-on-20240514>back to top</a>)</p>

## 3D Reconstruction

|Publish Date|Title|Abstract|PDF|Code|
|---|---|---|---|---|
|**2024-05-12**|**Hologram: Realtime Holographic Overlays via LiDAR Augmented Reconstruction**|在臭名昭著的《星球大战》系列全息技术的指导下，我提出了一个使用激光雷达增强3D重建创建实时全息覆盖的应用程序。先前的尝试涉及SLAM或NeRF，它们要么需要高度校准的场景，要么产生高昂的计算成本，要么无法渲染动态场景。我提出了3种高保真度重建工具，可以在便携式设备上运行，例如iPhone 14 Pro，它可以实现精确的面部重建。我的系统实现了交互式和沉浸式全息体验，可用于广泛的应用，包括增强现实、远程呈现和娱乐。 et.al.|[2405.07178](http://arxiv.org/abs/2405.07178)|null|
|**2024-05-12**|**CoViews: Adaptive Augmentation Using Cooperative Views for Enhanced Contrastive Learning**|数据扩充在生成有效对比学习所需的高质量正负对方面发挥着关键作用。然而，常见的做法涉及重复使用单个增强策略来生成多个视图，由于视图之间缺乏合作，可能导致训练对效率低下。此外，为了找到最佳的扩充集，许多现有方法需要广泛的监督评估，忽略了模型的演变性质，在整个训练过程中可能需要不同的扩充。其他方法训练可微增广生成器，从而限制了文献中不可微变换函数的使用。在本文中，我们通过提出一个框架来解决这些挑战，该框架用于以最小的计算开销学习用于对比学习的高效自适应数据增强策略。我们的方法在培训期间不断生成新的数据增强策略，并在没有任何监督的情况下产生有效的积极/消极因素。在这个框架内，我们提出了两种方法：\ac｛IndepViews｝，它生成在所有视图中使用的增强策略；\ac{CoViews}，它为每个视图生成依赖的增强策略。这使我们能够学习应用于每个视图的转换之间的依赖关系，并确保应用于不同视图的增强策略相互补充，从而产生更有意义和有区别的表示。通过在多个数据集和对比学习框架上的广泛实验，我们证明了我们的方法始终优于基线解决方案，并且使用依赖于视图的增强策略的训练优于使用跨视图共享的独立策略的训练，展示了其在增强对比学习性能方面的有效性。 et.al.|[2405.07116](http://arxiv.org/abs/2405.07116)|null|
|**2024-05-11**|**TD-NeRF: Novel Truncated Depth Prior for Joint Camera Pose and Neural Radiance Field Optimization**|对精确相机姿态的依赖是神经辐射场（NeRF）模型在3D重建和SLAM任务中广泛部署的一个重要障碍。现有方法引入单目深度先验来联合优化相机姿态和NeRF，未能充分利用深度先验，并忽略了其固有噪声的影响。在本文中，我们提出了截断深度NeRF（TD NeRF），这是一种新的方法，通过联合优化辐射场和相机姿态的可学习参数，可以从未知的相机姿态中训练NeRF。我们的方法通过三个关键进展明确利用了单目深度先验：1）我们提出了一种新的基于截断正态分布的基于深度的射线采样策略，提高了姿态估计的收敛速度和精度；2） 为了规避局部极小值并细化深度几何，我们引入了一种从粗到细的训练策略，该策略逐步提高了深度精度；3） 我们提出了一种更鲁棒的帧间点约束，该约束增强了训练过程中对深度噪声的鲁棒性。在三个数据集上的实验结果表明，TD NeRF在相机姿态和NeRF的联合优化方面取得了卓越的性能，超过了以往的工作，并生成了更准确的深度几何。我们方法的实现已在发布https://github.com/nubot-nudt/TD-NeRF. et.al.|[2405.07027](http://arxiv.org/abs/2405.07027)|null|
|**2024-05-10**|**OneTo3D: One Image to Re-editable Dynamic 3D Model and Video Generation**|单图像到可编辑动态三维模型和视频生成是单图像到三维表示或图像三维重建研究领域的新方向和变化。与原始的神经辐射场相比，高斯散射在隐式三维重建中显示了其优势。随着技术和原理的快速发展，人们试图使用稳定扩散模型来生成带有文本指令的目标模型。然而，使用普通的隐式机器学习方法很难获得精确的运动和动作控制，而且很难生成内容长、语义连续的3D视频。为了解决这个问题，我们提出了OneTo3D，这是一种使用单个图像生成可编辑3D模型并生成目标语义连续时间不受限制的3D视频的方法和理论。我们使用普通的基本高斯飞溅模型从单个图像生成3D模型，这需要较少的视频内存和计算机计算能力。随后，我们设计了一种对象电枢的自动生成和自适应绑定机制。结合我们提出的可重新编辑的运动和动作分析与控制算法，我们可以在建立3D模型、精确的运动和行动控制以及用输入的文本指令生成稳定的语义连续时间无限制的3D视频方面取得比SOTA项目更好的性能。在这里我们将分析详细的实施方法和理论分析。将介绍相关比较和结论。项目代码是开源的。 et.al.|[2405.06547](http://arxiv.org/abs/2405.06547)|**[link](https://github.com/lin-jinwei/OneTo3D)**|
|**2024-05-10**|**Comparative Analysis of Advanced Feature Matching Algorithms in Challenging High Spatial Resolution Optical Satellite Stereo Scenarios**|特征匹配决定了高空间分辨率（HSR）光学卫星立体定向的精度，从而影响了3D重建和变化检测等几个重要应用。然而，偏离轨道的HSR光学卫星立体像的匹配经常遇到具有挑战性的条件，包括宽基线观测、显著的辐射差异、多时相变化、不同的空间分辨率、不一致的光谱分辨率和不同的传感器。在这项研究中，我们评估了各种先进的HSR光学卫星立体特征匹配算法。利用来自六个具有挑战性场景的五颗卫星的专门构建的数据集，即HSROSS数据集，我们对四种算法进行了比较分析：传统的SIFT和基于深度学习的方法，包括SuperPoint+SuperGlue、SuperPoint+LightGlue和LoFTR。我们的研究结果突出了SuperPoint+LightGlue在平衡稳健性、准确性、分布性和效率方面的整体卓越性能，展示了其在复杂高铁光学卫星场景中的潜力。 et.al.|[2405.06246](http://arxiv.org/abs/2405.06246)|null|
|**2024-05-09**|**Minimal Perspective Autocalibration**|我们从多个角度引入了一个新的最小问题族进行重构。我们的主要关注点是一种新的自动校准方法，这是计算机视觉中一个长期存在的问题。解决这个问题的传统方法，如基于Kruppa方程或模约束的方法，明确地依赖于多个基本矩阵或投影重建的知识。相反，我们考虑了一种新的公式，该公式涉及图像点的约束、3D点的未知深度和部分指定的校准矩阵 $K$。对于$2$和$3$视图，我们给出了通过放松其中一些约束而获得的最小自动校准问题的综合分类法。这些问题根据视图的数量和$K$ 的任何假定先验知识被组织成类。在每个类中，我们用最少的——或者相对较少的——解决方案来确定问题。从这一大堆问题中，我们设计了三个实用的解决方案。使用合成数据和真实数据进行的实验以及我们的求解器与COLMAP的接口证明，与最先进的校准方法相比，我们实现了卓越的精度。代码位于https://github.com/andreadalcin/MinimalPerspectiveAutocalibration et.al.|[2405.05605](http://arxiv.org/abs/2405.05605)|null|
|**2024-05-09**|**Benchmarking Neural Radiance Fields for Autonomous Robots: An Overview**|神经辐射场（NeRF）已成为3D场景表示的一种强大范例，提供了一组稀疏和非结构化传感器数据的高保真渲染和重建。在自主机器人的背景下，对环境的感知和理解至关重要，NeRF在提高性能方面有着巨大的前景。在本文中，我们对利用NeRF增强自主机器人能力的最新技术进行了全面的调查和分析。我们特别关注自主机器人的感知、定位和导航以及决策模块，并深入研究对自主操作至关重要的任务，包括3D重建、分割、姿态估计、同步定位和映射（SLAM）、导航和规划以及交互。我们的调查仔细地对现有的基于NeRF的方法进行了基准测试，深入了解了它们的优势和局限性。此外，我们还探索了这一领域未来研究和开发的有希望的途径。值得注意的是，我们讨论了3D高斯飞溅（3DGS）、大型语言模型（LLM）和生成人工智能等先进技术的集成，以提高重建效率、场景理解和决策能力。这项调查为寻求利用NeRF为自主机器人赋能的研究人员提供了路线图，为能够在复杂环境中无缝导航和交互的创新解决方案铺平了道路。 et.al.|[2405.05526](http://arxiv.org/abs/2405.05526)|null|
|**2024-05-06**|**MVDiff: Scalable and Flexible Multi-View Diffusion for 3D Object Reconstruction from Single-View**|为3D重建任务生成一致的多个视图仍然是对现有图像到3D扩散模型的挑战。通常，将3D表示合并到扩散模型中会降低模型的速度以及可推广性和质量。本文提出了一个通用框架，从单个图像或利用场景表示变换器和视图条件扩散模型生成一致的多视图图像。在模型中，我们引入了极线几何约束和多视图注意力，以增强三维一致性。从一个图像输入中，我们的模型能够生成超过评估指标基线方法的3D网格，包括PSNR、SSIM和LPIPS。 et.al.|[2405.03894](http://arxiv.org/abs/2405.03894)|null|
|**2024-05-06**|**Gaussian Splatting: 3D Reconstruction and Novel View Synthesis, a Review**|基于图像的3D重建是一项具有挑战性的任务，涉及从一组输入图像推断对象或场景的3D形状。基于学习的方法因其直接估计3D形状的能力而受到关注。这篇综述论文的重点是最先进的3D重建技术，包括生成新颖的、看不见的视图。概述了高斯飞溅方法的最新发展，包括输入类型、模型结构、输出表示和训练策略。还讨论了尚未解决的挑战和未来的方向。鉴于该领域的快速进展以及增强3D重建方法的众多机会，对算法进行全面检查似乎至关重要。因此，本研究对高斯散射的最新进展进行了全面的概述。 et.al.|[2405.03417](http://arxiv.org/abs/2405.03417)|null|
|**2024-05-05**|**Morphokinematical study of the planetary nebula Me2-1: Unveiling its point-symmetric and unusual physical structure**|（摘要）我们展示了几条发射线的窄带图像，以及Me2-1的高分辨率和中分辨率长缝光谱，以研究其形态和3D结构、物理参数和化学丰度。我们在Me2-1中发现：一个椭圆环；两个细长的弯曲结构（帽），其包含三对亮点对称（PS）结；所述环的壳内部；以及微弱的光晕或附着的外壳。在所有图像中都观察到了帽，PS结仅在低激发发射线图像中观察到。这些结构也在高分辨率的长狭缝光谱中被识别。3D重建显示，Me2-1由一个几乎是极点的环和一个几乎球形的外壳组成，盖子和PS结连接在外壳上。帽状物和PS结最有可能追踪沿着摆动轴喷出的高速准直双极外流与球壳碰撞、减速并保持附着的位置。尽管Me2-1中的主要激发机制被发现是光电离，但PS结中的冲击的贡献是由它们的发射线比提出的。在行星状星云中，准直外流和带有球形外壳的环的结合是不寻常的。我们推测，如果两颗行星都在祖先的渐近巨星分支阶段进入共同的包络演化，那么这两颗行星可能都参与了Me2-1的形成，每颗行星的质量都小于一个木星。一颗行星被潮汐破坏，在中心恒星周围形成吸积盘，准直的双极性外流从吸积盘喷出；另一颗行星幸存下来，导致吸积盘摆动。导出的物理参数和化学丰度与之前的分析中获得的相似，丰度也指向Me2-1的低质量祖先。 et.al.|[2405.02938](http://arxiv.org/abs/2405.02938)|null|

<p align=right>(<a href=#updated-on-20240514>back to top</a>)</p>

## Diffusion

|Publish Date|Title|Abstract|PDF|Code|
|---|---|---|---|---|
|**2024-05-13**|**Cloaking for random walks using a discrete potential theory**|带电粒子在图中的扩散可以使用加权图上的随机游动来建模。我们从测量远离掩蔽子图的节点处的预期净粒子电荷的角度，给出了隐藏（或掩蔽）子图中变化的策略。我们根据策略是否涉及注入粒子来区分被动策略和主动策略。被动策略可以隐藏拓扑和边权重的更改。除了这些能力之外，主动策略还可以隐藏粒子来源，代价是参考图中预期净粒子电荷的先验知识。我们提出的策略依赖于经典势理论的离散类似物，其中包括图上的Calder演算。 et.al.|[2405.07961](http://arxiv.org/abs/2405.07961)|null|
|**2024-05-13**|**Stable Diffusion-based Data Augmentation for Federated Learning with Non-IID Data**|边缘设备的激增使联合学习（FL）成为一种很有前途的去中心化和协作模型培训模式，同时保护客户数据的隐私。然而，当面对参与客户端之间的非独立和同分布（Non-IID）数据分布时，FL面临着显著的性能降低和较差的收敛性。尽管之前的努力，如客户端漂移缓解和先进的服务器端模型融合技术，在解决这一挑战方面取得了一定的成功，但它们往往忽略了性能下降的根本原因——缺乏准确反映客户端之间全球数据分布的相同数据。在本文中，我们介绍了Gen FedSD，这是一种新颖的方法，它利用最先进的文本到图像基础模型的强大功能来弥补FL中显著的非IID性能差距。在Gen FedSD中，每个客户端都为每个类标签构建文本提示，并利用现成的最先进的预训练稳定扩散模型来合成高质量的数据样本。生成的合成数据针对每个客户独特的本地数据缺口和分布差异进行了定制，有效地使最终增强的本地数据成为IID。通过广泛的实验，我们证明了Gen FedSD在各种数据集和非IID设置中实现了最先进的性能和显著的通信成本节约。 et.al.|[2405.07925](http://arxiv.org/abs/2405.07925)|null|
|**2024-05-13**|**CTRLorALTer: Conditional LoRAdapter for Efficient 0-Shot Control & Altering of T2I Models**|文本到图像生成模型已成为一种突出而强大的工具，擅长生成高分辨率逼真图像。然而，指导这些模型的生成过程考虑反映风格和/或结构信息的条件反射的详细形式仍然是一个悬而未决的问题。在本文中，我们提出了LoRAdapter，这是一种使用新的条件LoRA块将风格和结构条件统一在同一公式下的方法，该块能够实现零样本控制。LoRAdapter是一种高效、强大且与体系结构无关的方法，用于调节文本到图像的扩散模型，它在生成过程中实现了细粒度的控制调节，并优于最近最先进的方法 et.al.|[2405.07913](http://arxiv.org/abs/2405.07913)|null|
|**2024-05-13**|**Latest results from Super-Kamiokande**|Super Kamiokande是世界上最大的水切伦科夫实验，其50千吨的超纯水罐最近掺杂了钆，以增强中子捕获识别。这是一个在MeV-TeV范围内的高度通用、多用途的实验，在这里我们将总结大气- $\nu$、太阳-$\nu$ 和漫射超新星中微子背景分析的最新结果和进展。 et.al.|[2405.07900](http://arxiv.org/abs/2405.07900)|null|
|**2024-05-13**|**Improving Breast Cancer Grade Prediction with Multiparametric MRI Created Using Optimized Synthetic Correlated Diffusion Imaging**|2015年至2020年间，超过780万女性被诊断出患有癌症。分级在癌症治疗计划中起着至关重要的作用。然而，目前的肿瘤分级方法涉及从患者身上提取组织，导致压力、不适和高昂的医疗成本。最近一篇利用合成相关扩散成像（CDI $^s$）的体积深部放射组学特征预测乳腺癌症分级的论文显示了无创分级方法的巨大前景。受CDI$^s$优化对前列腺癌症划定的影响，本文研究了使用优化的CDI$^ s$改善癌症分级预测。我们将优化的CDI$^s$ 信号与扩散加权成像（DWI）融合，为每位患者创建多参数MRI。使用更大的患者队列，并在预训练的MONAI模型的所有层进行训练，我们实现了95.79%的留一交叉验证准确率，比之前报道的高出8%以上。 et.al.|[2405.07861](http://arxiv.org/abs/2405.07861)|null|
|**2024-05-13**|**Radiogenomic biomarkers for immunotherapy in glioblastoma: A systematic review of magnetic resonance imaging studies**|免疫疗法是治疗多种癌症的有效精准药物。胶质母细胞瘤患者潜在基因组（放射基因组学）的成像特征可以作为肿瘤宿主免疫系统的术前生物标志物。经验证的生物标志物有可能在免疫疗法临床试验中对患者进行分层，如果试验有益，则有助于个性化的新辅助治疗。全基因组测序数据的使用增加，以及生物信息学和机器学习的进步，使这种发展成为可能。我们进行了一项系统综述，以确定胶质母细胞瘤免疫相关放射基因组生物标志物的开发和验证程度。根据PRISMA指南，使用PubMed、Medline和Embase数据库进行系统审查。通过结合QUADAS 2工具和索赔清单进行定性分析。PROSPERO注册CRD42022340968。提取的数据不够同质，无法进行荟萃分析。结果纳入9项研究，均为回顾性研究。从感兴趣的磁共振成像体积中提取的生物标志物包括表观扩散系数值、相对脑血容量值和图像衍生特征。这些生物标志物与来自肿瘤细胞或免疫细胞的基因组标志物或与患者生存率相关。大多数研究对所进行的指数测试存在较高的偏倚风险和适用性问题。放射基因组免疫生物标志物有可能为胶质母细胞瘤患者提供早期治疗选择。根据这些生物标志物进行分层的靶向免疫疗法有可能在临床试验中提供个性化的新辅助精确治疗选择。然而，没有前瞻性研究验证这些生物标志物，而且由于研究偏倚，解释有限，几乎没有可推广性的证据。 et.al.|[2405.07858](http://arxiv.org/abs/2405.07858)|null|
|**2024-05-13**|**Using Multiparametric MRI with Optimized Synthetic Correlated Diffusion Imaging to Enhance Breast Cancer Pathologic Complete Response Prediction**|2020年，全世界有685000人死于癌症，这突出表明迫切需要创新和有效的癌症治疗。新辅助化疗作为癌症的一种很有前途的治疗策略，近年来越来越受欢迎，这归功于其在缩小大肿瘤和导致病理完全反应方面的疗效。然而，目前推荐新辅助化疗的过程依赖于医学专家的主观评估，其中包含固有的偏见和重大的不确定性。最近的一项研究，利用从合成相关扩散成像（CDI $^s$）中提取的体积深部放射学特征，证明了无创乳腺癌症病理完全反应预测的巨大潜力。受优化前列腺癌症CDI$^s$描绘的积极结果的启发，本研究调查了优化CDI$^ s$在增强癌症病理完全反应预测中的应用。使用将优化的CDI$^s$ 与扩散加权成像（DWI）融合在一起的多参数MRI，我们获得了93.28%的漏一交叉验证准确率，比之前报道的高出5.5%以上。 et.al.|[2405.07854](http://arxiv.org/abs/2405.07854)|null|
|**2024-05-13**|**SAR Image Synthesis with Diffusion Models**|近年来，扩散模型（DM）已成为生成合成数据的一种流行方法。通过获得更高质量的样本，它们很快就优于生成对抗性网络（GANs）和当前最先进的生成建模方法。然而，它们的潜力尚未在雷达中得到利用，因为缺乏可用的训练数据是一个长期存在的问题。在这项工作中，一种特定类型的DM，即去噪扩散概率模型（DDPM）适用于SAR领域。我们研究了有条件和无条件SAR图像生成的网络选择和特定扩散参数。在我们的实验中，我们表明DDPM在质量和数量上都优于最先进的基于GAN的SAR图像生成方法。最后，我们证明了DDPM得益于对大规模杂波数据的预训练，生成了更高质量的SAR图像。 et.al.|[2405.07776](http://arxiv.org/abs/2405.07776)|null|
|**2024-05-13**|**LGDE: Local Graph-based Dictionary Expansion**|扩展预先选择的关键字的字典对于信息检索任务（如数据库查询和在线数据收集）至关重要。在这里，我们提出了基于局部图的字典扩展（LGDE），这是一种使用流形学习和网络科学的工具从种子字典开始进行数据驱动的关键字发现的方法。LGDE的核心是创建源自单词嵌入的单词相似性图，以及应用基于图扩散的局部社区检测来发现预定义种子关键字的语义邻域。局部图流形中的扩散允许探索单词嵌入的复杂非线性几何，并且可以基于语义关联的路径来捕捉单词相似性。我们在Reddit和Gab的仇恨言论相关帖子语料库上验证了我们的方法，并表明LGDE丰富了关键词列表，并实现了比基于直接单词相似性的阈值方法更好的性能。我们通过通信科学的真实世界用例进一步证明了我们方法的潜力，其中LGDE是根据领域专家通过扩展阴谋相关词典收集和分析的数据进行定量评估的。 et.al.|[2405.07764](http://arxiv.org/abs/2405.07764)|null|
|**2024-05-13**|**FastSAG: Towards Fast Non-Autoregressive Singing Accompaniment Generation**|伴唱生成（SAG）是为输入人声生成器乐的过程，对开发人类与人工智能共生的艺术创作系统至关重要。最先进的方法SingSong利用多级自回归（AR）模型进行SAG，然而，这种方法非常缓慢，因为它递归地生成语义和声学标记，这使得实时应用无法实现。在本文中，我们的目标是开发一种快速SAG方法，可以创建高质量和连贯的伴奏。开发了一种基于非AR扩散的框架，通过仔细设计从人声信号中推断出的条件，直接生成目标伴奏的Mel声谱图。通过扩散和Mel谱图建模，该方法显著简化了基于AR令牌的SingSong框架，并大大加快了生成速度。我们还设计了语义投影、先验投影块以及一组损失函数，以确保生成的伴奏与人声信号具有语义和节奏连贯性。通过深入的实验研究，我们证明了所提出的方法可以生成比SingSong更好的样本，并将生成速度加快至少30倍。音频样本和代码可在https://fastsag.github.io/. et.al.|[2405.07682](http://arxiv.org/abs/2405.07682)|null|

<p align=right>(<a href=#updated-on-20240514>back to top</a>)</p>

## NeRF

|Publish Date|Title|Abstract|PDF|Code|
|---|---|---|---|---|
|**2024-05-08**|**${M^2D}$NeRF: Multi-Modal Decomposition NeRF with 3D Feature Fields**|神经场（NeRF）已经成为表示连续3D场景的一种很有前途的方法。然而，NeRF中缺乏语义编码对场景分解提出了重大挑战。为了应对这一挑战，我们提出了一个单一的模型，即多模式分解NeRF（${M^2D}$ NeRF），它能够进行基于文本和基于视觉补丁的编辑。具体来说，我们使用多模态特征提取将来自预训练的视觉和语言模型的教师特征集成到3D语义特征体积中，从而促进一致的3D编辑。为了增强三维特征体积中视觉特征和语言特征之间的一致性，我们引入了多模态相似性约束。我们还引入了一种基于补丁的联合对比损失，这有助于鼓励对象区域在3D特征空间中合并，从而产生更精确的边界。与先前的基于NeRF的方法相比，在各种真实世界场景上的实验显示出在3D场景分解任务中的优越性能。 et.al.|[2405.05010](http://arxiv.org/abs/2405.05010)|null|
|**2024-05-09**|**Radar Fields: Frequency-Space Neural Scene Representations for FMCW Radar**|神经场作为再现和新一代各种户外场景的场景表示，包括自动驾驶汽车和机器人必须处理的场景，已经得到了广泛的研究。虽然存在RGB和激光雷达数据的成功方法，但雷达作为传感模式的神经重建方法在很大程度上尚未被探索。雷达传感器在毫米波长下工作，对雾和雨中的散射具有鲁棒性，因此为主动和被动光学传感技术提供了一种互补的方式。此外，现有的雷达传感器具有很高的成本效益，并广泛应用于户外作业的机器人和车辆中。我们介绍了雷达场——一种为有源雷达成像器设计的神经场景重建方法。我们的方法将一个明确的、基于物理的传感器模型与一个隐含的神经几何和反射模型相结合，直接合成原始雷达测量值并提取场景占用率。所提出的方法不依赖于体绘制。相反，我们在傅立叶频率空间中学习场，并用原始雷达数据进行监督。我们在不同的室外场景中验证了该方法的有效性，包括车辆和基础设施密集的城市场景，以及在毫米波长传感特别有利的恶劣天气场景中。 et.al.|[2405.04662](http://arxiv.org/abs/2405.04662)|null|
|**2024-05-06**|**Neural Graph Mapping for Dense SLAM with Efficient Loop Closure**|现有的基于神经场的SLAM方法通常使用单个单片场作为其场景表示。这阻碍了循环闭合约束的有效结合，并限制了可扩展性。为了解决这些缺点，我们提出了一种神经映射框架，该框架将轻量级神经场锚定到稀疏视觉SLAM系统的姿态图上。我们的方法显示了整合大规模闭环的能力，同时限制了必要的重新融合。此外，我们通过在优化过程中考虑多个环路闭合来验证我们的方法的可扩展性，并证明我们的方法在质量和运行时间方面优于现有的最先进的方法。我们的代码可在https://kth-rpl.github.io/neural_graph_mapping/. et.al.|[2405.03633](http://arxiv.org/abs/2405.03633)|null|
|**2024-05-03**|**Simulation-based Inference of Developmental EEG Maturation with the Spectral Graph Model**|宏观神经活动的光谱内容在整个发育过程中不断演变，但这种成熟与潜在的大脑网络形成和动力学之间的关系尚不清楚。为了深入了解这一过程的机制，我们通过频谱图模型（SGM）的贝叶斯模型反演来评估发育脑电频谱变化，SGM是一种全脑空间频谱活动的简约模型，源于由结构连接体耦合的线性化神经场模型。基于模拟的推理用于从跨越发育期的脑电图频谱中估计年龄变化的SGM参数后验分布。我们发现，这种模型拟合方法通过关键神经参数的神经生物学一致进展准确地捕捉了脑电图频谱的发育成熟：长程耦合、轴突传导速度和兴奋性：抑制性平衡。这些结果表明，在正常发育过程中观察到的大脑活动的光谱成熟得到了功能适应的支持，特别是局部神经动力学的年龄依赖性调节及其在宏观结构网络中的长期耦合。 et.al.|[2405.02524](http://arxiv.org/abs/2405.02524)|null|
|**2024-04-30**|**Lightplane: Highly-Scalable Components for Neural 3D Fields**|当代3D研究，特别是在重建和生成方面，严重依赖2D图像进行输入或监督。然而，这些2D-3D映射的当前设计是内存密集型的，对现有方法构成了显著的瓶颈，并阻碍了新的应用。作为回应，我们为3D神经场提出了一对高度可扩展的组件：Lightplane Render和Splatter，这显著减少了2D-3D映射中的内存使用。这些创新能够以较小的内存和计算成本处理更多、更高分辨率的图像。我们展示了它们在各种应用中的实用性，从有利于图像级损失的单场景优化到实现用于大幅缩放3D重建和生成的多功能管道。代码：\url{https://github.com/facebookresearch/lightplane}. et.al.|[2404.19760](http://arxiv.org/abs/2404.19760)|**[link](https://github.com/facebookresearch/lightplane)**|
|**2024-05-03**|**Object Registration in Neural Fields**|神经场以一种对机器人应用具有巨大前景的方式提供3D几何结构和外观的连续场景表示。解锁机器人中神经领域独特用例的一个功能是对象6-DoF注册。在本文中，我们对最近的Reg-NF神经场配准方法及其在机器人环境中的用例进行了扩展分析。我们展示了使用场景和对象神经场模型确定场景中已知对象的6-DoF姿态的场景。我们展示了如何使用它来更好地表示未完全建模的场景中的对象，并通过将对象神经场模型替换到场景中来生成新的场景。 et.al.|[2404.18381](http://arxiv.org/abs/2404.18381)|null|
|**2024-04-26**|**ArtNeRF: A Stylized Neural Field for 3D-Aware Cartoonized Face Synthesis**|生成视觉模型和神经辐射领域的最新进展极大地促进了3D感知图像合成和风格化任务。然而，以前基于NeRF的工作仅限于单场景风格化，训练模型生成具有任意风格的3D感知卡通人脸仍然没有解决。为了解决这个问题，我们提出了ArtNeRF，这是一种从3D感知GAN中派生出来的新颖的人脸风格化框架。在这个框架中，我们利用表达生成器来合成风格化的人脸，并利用三分支鉴别器模块来提高生成人脸的视觉质量和风格一致性。具体而言，利用基于对比学习的风格编码器来提取风格图像的鲁棒低维嵌入，使生成器能够获得各种风格的知识。为了平滑跨领域迁移学习的训练过程，我们提出了一个自适应风格混合模块，该模块有助于注入风格信息，并允许用户自由调整风格化水平。我们进一步引入了一个神经渲染模块，以实现更高分辨率图像的高效实时渲染。大量实验表明，ArtNeRF在生成具有任意风格的高质量3D感知卡通人脸方面是通用的。 et.al.|[2404.13711](http://arxiv.org/abs/2404.13711)|**[link](https://github.com/silence-tang/artnerf)**|
|**2024-04-19**|**BANF: Band-limited Neural Fields for Levels of Detail Reconstruction**|主要由于其隐含性质，神经场缺乏直接的滤波机制，因为离散信号处理的傅立叶分析不直接适用于这些表示。神经场的有效滤波对于实现下游应用程序中的细节处理水平至关重要，并支持在规则网格上对场进行采样的操作（例如，行进立方体）。试图在频域中分解神经场的现有方法要么采用启发式方法，要么需要对神经场架构进行广泛修改。我们展示了通过一个简单的修改，可以获得低通滤波的神经场，进而展示了如何利用这一点来获得整个信号的频率分解。我们通过研究细节水平重建来证明我们的技术的有效性，并展示了如何有效地计算粗糙的表示。 et.al.|[2404.13024](http://arxiv.org/abs/2404.13024)|null|
|**2024-04-15**|**Efficient and accurate neural field reconstruction using resistive memory**|人类通过将稀疏的观测整合到大规模互连的突触和神经元中来构建空间感知，提供了卓越的并行性和效率。在人工智能中复制这一能力在医学成像、AR/VR和嵌入式人工智能中有着广泛的应用，在这些领域，输入数据往往是稀疏的，计算资源有限。然而，传统的数字计算机信号重构方法面临着软硬件两方面的挑战。在软件方面，传统显式信号表示中的存储效率低下会带来困难。硬件障碍包括冯·诺依曼瓶颈，它限制了CPU和存储器之间的数据传输，以及CMOS电路在支持并行处理方面的局限性。我们提出了一种软硬件协同优化的系统方法，用于从稀疏输入重建信号。在软件方面，我们使用神经场通过神经网络隐式地表示信号，并使用低秩分解和结构化修剪对其进行进一步压缩。在硬件方面，我们设计了一个基于电阻存储器的内存计算（CIM）平台，该平台具有高斯编码器（GE）和MLP处理引擎（PE）。GE利用电阻存储器的内在随机性进行有效的输入编码，而PE通过硬件感知量化（HAQ）电路实现精确的权重映射。我们在基于40nm 256Kb电阻存储器的内存内计算宏上展示了该系统的功效，在不影响3D CT稀疏重建、新视图合成和动态场景新视图合成等任务的重建质量的情况下，实现了巨大的能效和并行性改进。这项工作推进了人工智能驱动的信号恢复技术，为未来高效、稳健的医疗人工智能和3D视觉应用铺平了道路。 et.al.|[2404.09613](http://arxiv.org/abs/2404.09613)|null|
|**2024-04-10**|**Ray-driven Spectral CT Reconstruction Based on Neural Base-Material Fields**|在谱CT重建中，基底材料分解涉及求解大规模非线性积分方程组，这在数学上是高度不适定的。本文提出了一种模型，该模型使用神经场表示来参数化对象的衰减系数，从而避免了线积分离散化过程中像素驱动的投影系数矩阵的复杂计算。介绍了一种基于光线驱动神经场的线积分轻量级离散化方法，提高了离散化过程中积分逼近的精度。将基底材料表示为连续的向量值隐函数，以建立基底材料的神经场参数化模型。然后使用深度学习的自动微分框架来求解神经基底材料场的隐式连续函数。该方法不受重建图像空间分辨率的限制，并且网络具有紧凑和规则的特性。实验验证表明，我们的方法在处理光谱CT重建方面表现得非常好。此外，它还满足了生成高分辨率重建图像的要求。 et.al.|[2404.06991](http://arxiv.org/abs/2404.06991)|null|

<p align=right>(<a href=#updated-on-20240514>back to top</a>)</p>

[contributors-shield]: https://img.shields.io/github/contributors/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[contributors-url]: https://github.com/Vincentqyw/cv-arxiv-daily/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[forks-url]: https://github.com/Vincentqyw/cv-arxiv-daily/network/members
[stars-shield]: https://img.shields.io/github/stars/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[stars-url]: https://github.com/Vincentqyw/cv-arxiv-daily/stargazers
[issues-shield]: https://img.shields.io/github/issues/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[issues-url]: https://github.com/Vincentqyw/cv-arxiv-daily/issues

