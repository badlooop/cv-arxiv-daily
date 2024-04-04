[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]

## Updated on 2024.04.04
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
|**2024-04-03**|**LiDAR4D: Dynamic Neural Fields for Novel Space-time View LiDAR Synthesis**|尽管神经辐射场（NeRFs）在图像新视图合成（NVS）方面取得了成功，但激光雷达NVS在很大程度上仍未被探索。以前的激光雷达NVS方法采用了图像NVS方法的简单转变，同时忽略了激光雷达点云的动态特性和大规模重建问题。有鉴于此，我们提出了LiDAR4D，这是一种用于新的时空LiDAR视图合成的仅限LiDAR的可微分框架。考虑到稀疏性和大规模特征，我们设计了一种结合多平面和网格特征的4D混合表示，以实现从粗到细的有效重建。此外，我们引入了从点云导出的几何约束，以提高时间一致性。对于激光雷达点云的真实合成，我们结合了光线下降概率的全局优化，以保持跨区域模式。在KITTI-360和NuScenes数据集上进行的大量实验证明了我们的方法在实现几何感知和时间一致的动态重建方面的优越性。代码可在https://github.com/ispc-lab/LiDAR4D. et.al.|[2404.02742](http://arxiv.org/abs/2404.02742)|null|
|**2024-04-02**|**NeRFCodec: Neural Feature Compression Meets Neural Radiance Fields for Memory-Efficient Scene Representation**|神经辐射场（NeRF）的出现极大地影响了三维场景建模和新颖的视图合成。作为一种用于三维场景表示的视觉媒体，具有高率失真性能的压缩是一个永恒的目标。受神经压缩和神经场表示进步的启发，我们提出了NeRFCodec，这是一种端到端的NeRF压缩框架，它集成了非线性变换、量化和熵编码，用于高效记忆的场景表示。由于直接在大规模的NeRF特征平面上训练非线性变换是不切实际的，我们发现，当添加内容特定参数时，可以使用预先训练的神经2D图像编解码器来压缩特征。具体来说，我们重用神经2D图像编解码器，但修改其编码器和解码器头，同时保持预训练解码器的其他部分冻结。这使我们能够通过监督渲染损失和熵损失来训练整个管道，通过更新特定于内容的参数来实现率失真平衡。在测试时，包含潜在代码、特征解码器头和其他辅助信息的比特流被发送用于通信。实验结果表明，我们的方法优于现有的NeRF压缩方法，能够在0.5MB的内存预算下实现高质量的新视图合成。 et.al.|[2404.02185](http://arxiv.org/abs/2404.02185)|null|
|**2024-04-02**|**Surface Reconstruction from Gaussian Splatting via Novel Stereo Views**|最近，高斯散射辐射场渲染方法作为一种精确场景表示的有效方法出现了。它优化了3D高斯元素云的位置、大小、颜色和形状，以便在投影或飞溅后，在视觉上匹配从不同观看方向拍摄的一组给定图像。然而，尽管高斯元素接近形状边界，但场景中对象的直接表面重建是一个挑战。我们提出了一种从高斯飞溅模型重建表面的新方法。我们利用3DGS优越的新型视图合成能力，而不是依赖高斯元素的位置作为表面重建的先验。为此，我们使用高斯飞溅模型来渲染成对的立体校准的新视图，并使用立体匹配方法从中提取深度轮廓。然后，我们将提取的RGB-D图像组合成几何一致的曲面。与从高斯飞溅模型进行表面重建的其他方法相比，所得到的重建更准确，并且显示出更精细的细节，同时与其他表面重建方法相比，需要更少的计算时间。我们在智能手机拍摄的野外场景中对所提出的方法进行了广泛的测试，展示了其卓越的重建能力。此外，我们在Tanks and Temples基准上测试了所提出的方法，它已经超过了目前从高斯飞溅模型进行表面重建的领先方法。项目页面：https://gs2mesh.github.io/. et.al.|[2404.01810](http://arxiv.org/abs/2404.01810)|null|
|**2024-04-01**|**NVINS: Robust Visual Inertial Navigation Fused with NeRF-augmented Camera Pose Regressor and Uncertainty Quantification**|近年来，神经辐射场（NeRF）已成为三维重建和新型视图合成的强大工具。然而，NeRF渲染的计算成本和由于伪影的存在而导致的质量下降，对其在实时和鲁棒机器人任务中的应用，特别是在嵌入式系统中的应用提出了重大挑战。本文介绍了一种新的框架，该框架将NeRF导出的定位信息与视觉惯性里程计（VIO）相结合，为机器人实时导航提供了一个稳健的解决方案。通过使用NeRF渲染的增强图像数据训练绝对姿态回归网络并量化其不确定性，我们的方法有效地对抗了位置漂移并提高了系统可靠性。考虑到贝叶斯框架下的不确定性，我们还为将视觉惯性导航与相机定位神经网络相结合奠定了数学上坚实的基础。在真实感仿真环境中的实验验证表明，与传统的VIO方法相比，精度显著提高。 et.al.|[2404.01400](http://arxiv.org/abs/2404.01400)|null|
|**2024-04-02**|**SurMo: Surface-based 4D Motion Modeling for Dynamic Human Rendering**|通过将视频序列的动态人体渲染公式化为从静态姿势到人体图像的映射，该渲染已经取得了显著的进展。然而，现有的方法侧重于每一帧的人脸重建，而时间运动关系并没有得到充分的探索。在本文中，我们提出了一种新的4D运动建模范式SurMo，它在一个统一的框架中用三个关键设计联合建模时间动力学和人类外观：1）基于表面的运动编码，它用一个高效的紧凑的基于表面的三平面来建模4D人类运动。它在统计身体模板的稠密表面流形上编码空间和时间运动关系，该模板继承了身体拓扑先验，用于具有稀疏训练观测的可推广新视图合成。2） 物理运动解码，其被设计为通过在训练阶段中对时间步长t处的运动三平面特征进行解码以预测下一时间步长t+1处的空间导数和时间导数来鼓励物理运动学习。3） 4D外观解码，通过高效的体积表面条件渲染器将运动三平面渲染成图像，该渲染器专注于利用运动学习条件渲染身体表面。大量实验验证了我们新范式的最先进性能，并说明了基于表面的运动三板的表现力，可以通过快速运动甚至依赖于运动的阴影来呈现与人类一致的高保真度视图。我们的项目页面位于：https://taohuumd.github.io/projects/SurMo/ et.al.|[2404.01225](http://arxiv.org/abs/2404.01225)|null|
|**2024-04-01**|**Mirror-3DGS: Incorporating Mirror Reflections into 3D Gaussian Splatting**|三维高斯散射（3DGS）技术在三维场景重建和新颖视图合成领域取得了重大突破。然而，3DGS与其前身神经辐射场（NeRF）非常相似，很难准确地对物理反射进行建模，尤其是在现实世界场景中无处不在的镜子中。这种疏忽错误地将反射视为物理存在的独立实体，导致不准确的重建和不同视点的反射特性不一致。为了应对这一关键挑战，我们引入了Mirror-3DGS，这是一种创新的渲染框架，旨在掌握镜子几何形状和反射的复杂性，为生成逼真的镜子反射铺平了道路。mirror-3DGS巧妙地将镜像属性融入3DGS，并利用平面镜像成像的原理，制作了一个镜像视点，从镜子后面进行观察，丰富了场景渲染的真实感。广泛的评估涵盖了合成场景和真实世界场景，展示了我们的方法能够实时渲染逼真度更高的新视图，特别是在具有挑战性的镜像区域内，超过了最先进的Mirror NeRF。我们的代码将公开用于可重复的研究。 et.al.|[2404.01168](http://arxiv.org/abs/2404.01168)|null|
|**2024-04-01**|**CityGaussian: Real-time High-quality Large-Scale Scene Rendering with Gaussians**|三维高斯散射（3DGS）极大地推动了实时三维场景重建和新视图合成的发展。然而，有效地训练大规模3DGS并在各种尺度上实时渲染它仍然具有挑战性。本文介绍了CityGaussian（CityGS），它采用了一种新的分而治之的训练方法和细节层次（LoD）策略来进行高效的大规模3DGS训练和渲染。具体来说，全局场景先验和自适应训练数据选择使训练和无缝融合成为可能。基于融合的高斯基元，我们通过压缩生成不同的细节级别，并通过所提出的逐块细节级别选择和聚合策略实现跨不同尺度的快速渲染。在大规模场景上的大量实验结果表明，我们的方法达到了最先进的渲染质量，能够在截然不同的尺度上对大规模场景进行一致的实时渲染。我们的项目页面位于https://dekuliutesla.github.io/citygs/. et.al.|[2404.01133](http://arxiv.org/abs/2404.01133)|null|
|**2024-04-01**|**SGCNeRF: Few-Shot Neural Rendering via Sparse Geometric Consistency Guidance**|神经辐射场（NeRF）技术在创造新观点方面取得了重大进展。然而，当使用稀疏可用的视图时，它的有效性会受到阻碍，通常会由于过拟合而导致性能下降。FreeNeRF试图通过集成隐式几何正则化来克服这一限制，该正则化可以逐步改进几何体和纹理。尽管如此，初始的低位置编码带宽导致排除了高频元件。寻求一种同时解决过度拟合和保留高频细节的整体方法仍在进行中。本文介绍了一种新的基于特征匹配的稀疏几何正则化模块。该模块擅长精确定位高频关键点，从而保护精细细节的完整性。通过在NeRF迭代中逐步细化几何体和纹理，我们推出了一种有效的少镜头神经渲染架构，称为SGCNeRF，用于增强新视图合成。我们的实验表明，SGCNeRF不仅实现了卓越的几何一致性结果，而且超过了FreeNeRF，在LLFF和DTU数据集上的PSNR分别提高了0.7dB和0.6dB。 et.al.|[2404.00992](http://arxiv.org/abs/2404.00992)|null|
|**2024-03-31**|**Knowledge NeRF: Few-shot Novel View Synthesis for Dynamic Articulated Objects**|我们提出了知识NeRF来合成动态场景的新颖视图。从少数稀疏视图重建动态3D场景并从任意角度渲染它们是各个领域应用中的一个具有挑战性的问题。以前的动态NeRF方法从单目视频中学习关节物体的变形。然而，他们重建的场景的质量是有限的。为了清晰地重建动态场景，我们提出了一个新的框架，每次考虑两个帧。我们为铰接对象预训练NeRF模型。当铰接对象移动时，Knowledge NeRF通过将过去的知识结合到预训练的NeRF模型中来学习在新状态下生成新的视图，在当前状态下具有最小的观测值。我们提出了一个投影模块，使NeRF适应动态场景，学习预训练的知识库和当前状态之间的对应关系。实验结果证明了该方法在一种状态下用5幅输入图像重建动态三维场景的有效性。知识NeRF是动态关节对象中新的视图合成的一种新的管道和有前途的解决方案。数据和实施情况可在https://github.com/RussRobin/Knowledge_NeRF. et.al.|[2404.00674](http://arxiv.org/abs/2404.00674)|**[link](https://github.com/russrobin/knowledge_nerf)**|
|**2024-03-29**|**Multi-Level Neural Scene Graphs for Dynamic Urban Environments**|我们根据不同环境条件下的多个车辆捕获来估计大规模动态区域的辐射场。该领域以前的作品要么局限于静态环境，不扩展到多个短视频，要么难以单独表示动态对象实例。为此，我们提出了一种适用于动态城市环境的新的可分解辐射场方法。我们提出了一种多级神经场景图表示，该表示可扩展到数百个快速移动对象的数十个序列中的数千幅图像。为了能够有效地训练和渲染我们的表示，我们开发了一种快速的复合光线采样和渲染方案。为了在城市驾驶场景中测试我们的方法，我们引入了一个新的、新颖的视图合成基准。我们表明，我们的方法在已建立的和提出的基准上都显著优于现有技术，同时在训练和渲染方面更快。 et.al.|[2404.00168](http://arxiv.org/abs/2404.00168)|null|

<p align=right>(<a href=#updated-on-20240404>back to top</a>)</p>

## 3D Reconstruction

|Publish Date|Title|Abstract|PDF|Code|
|---|---|---|---|---|
|**2024-04-03**|**Neural Radiance Fields with Torch Units**|神经辐射场（NeRF）产生了在工业应用中广泛使用的基于学习的3D重建方法。尽管流行的方法在小规模场景中实现了相当大的改进，但在复杂和大规模场景中实现重建仍然具有挑战性。首先，复杂场景中的背景显示出不同视图之间的巨大差异。其次，当前的推理模式，即$，即一个像素仅依赖于单个相机光线，无法捕捉上下文信息。为了解决这些问题，我们建议扩大射线感知场，建立采样点之间的相互作用。在本文中，我们设计了一种新的推理模式，该模式鼓励单个相机射线拥有更多的上下文信息，并对每个相机射线上的采样点之间的关系进行建模。为了保存上下文信息，在我们提出的方法中，相机光线可以同时渲染一块像素。此外，我们用距离感知卷积代替神经辐射场模型中的MLP，以增强来自同一相机射线的样本点之间的特征传播。总之，在我们提出的方法中，光线作为火炬光实现了对图像的渲染。因此，我们将所提出的方法称为Torch NeRF。在KITTI-360和LLFF上进行的大量实验表明，Torch NeRF表现出优异的性能。 et.al.|[2404.02617](http://arxiv.org/abs/2404.02617)|null|
|**2024-04-03**|**TCLC-GS: Tightly Coupled LiDAR-Camera Gaussian Splatting for Surrounding Autonomous Driving Scenes**|大多数基于3D高斯散射（3D-GS）的城市场景方法直接用3D激光雷达点初始化3D高斯，这不仅没有充分利用激光雷达的数据能力，而且忽略了将激光雷达与相机数据融合的潜在优势。在本文中，我们设计了一种新型的紧密耦合激光雷达相机高斯散射（TCLC-GS），以充分利用激光雷达和相机传感器的综合优势，实现快速、高质量的3D重建和新颖的视图RGB/深度合成。TCLC-GS设计了一种基于激光雷达相机数据的显式（彩色3D网格）和隐式（层次八叉树特征）混合3D表示，以丰富3D高斯的飞溅特性。3D高斯的属性不仅被初始化为与提供更完整的3D形状和颜色信息的3D网格对齐，而且还通过检索到的八叉树隐式特征被赋予更广泛的上下文信息。在高斯飞溅优化过程中，3D网格提供密集的深度信息作为监督，通过学习稳健的几何结构来增强训练过程。对Waymo开放数据集和nuScenes数据集进行的全面评估验证了我们的方法最先进的（SOTA）性能。利用单个NVIDIA RTX 3090 Ti，我们的方法演示了快速训练，并在城市场景中实现了分辨率为1920x1280（Waymo）的90 FPS和分辨率为1600x900（nuScenes）的120 FPS的实时RGB和深度渲染。 et.al.|[2404.02410](http://arxiv.org/abs/2404.02410)|null|
|**2024-04-03**|**APC2Mesh: Bridging the gap from occluded building façades to full 3D models**|拥有城市建筑的数字双胞胎有很多好处。然而，从机载激光雷达点云创建它们时遇到的一个主要困难是在点密度变化和噪声中准确重建显著遮挡的有效方法。为了弥合噪声/稀疏性/遮挡间隙并生成高保真度的3D建筑模型，我们提出了APC2Mesh，它将点完成集成到3D重建管道中，从而能够学习建筑的密集几何精确表示。具体来说，我们利用由遮挡点生成的完整点作为线性化的基于跳跃注意力的变形网络的输入，用于3D网格重建。在我们在3个不同场景上进行的实验中，我们证明：（1）APC2Mesh提供了相对优越的结果，表明其在处理不同风格和复杂性的遮挡机载构建点的挑战方面具有有效性。（2） 将点完成与典型的基于深度学习的三维点云重建方法相结合，为重建被严重遮挡的机载建筑点提供了直接有效的解决方案。因此，这种神经集成有望以更高的准确性和保真度推进城市建筑数字孪生的创建。 et.al.|[2404.02391](http://arxiv.org/abs/2404.02391)|null|
|**2024-04-02**|**One Noise to Rule Them All: Multi-View Adversarial Attacks with Universal Perturbation**|本文提出了一种新的通用摄动方法，用于生成三维物体识别中的鲁棒多视图对抗性示例。与仅限于单个视图的传统攻击不同，我们的方法对多个2D图像进行操作，为增强模型的可扩展性和稳健性提供了一个实用且可扩展的解决方案。这种可推广的方法弥合了二维扰动和类三维攻击能力之间的差距，使其适用于现实世界的应用。当图像经历诸如照明、相机位置或自然变形的变化等变换时，现有的对抗性攻击可能变得无效。我们通过制作适用于各种物体视图的单一通用噪声扰动来应对这一挑战。在不同渲染的3D对象上进行的实验证明了我们的方法的有效性。通用扰动成功地从多个姿势和视点为每个给定的3D对象渲染集识别了单个对抗性噪声。与单视图攻击相比，我们的通用攻击降低了多个视角的分类置信度，尤其是在低噪声水平下。示例实现可在https://github.com/memoatwit/UniversalPerturbation. et.al.|[2404.02287](http://arxiv.org/abs/2404.02287)|**[link](https://github.com/memoatwit/universalperturbation)**|
|**2024-04-01**|**Neural Implicit Representation for Building Digital Twins of Unknown Articulated Objects**|我们解决了从物体在不同关节状态下的两次RGBD扫描中构建未知关节物体的数字双胞胎的问题。我们将问题分解为两个阶段，每个阶段都涉及不同的方面。我们的方法首先在每个状态下重建对象级别的形状，然后恢复基本的关节模型，包括将两种状态关联起来的部分分割和关节关节。通过明确建模点级对应关系，并利用图像、3D重建和运动学中的线索，与之前的工作相比，我们的方法产生了更准确、更稳定的结果。它还处理多个可移动部件，不依赖于任何物体形状或结构先验。项目页面：https://github.com/NVlabs/DigitalTwinArt et.al.|[2404.01440](http://arxiv.org/abs/2404.01440)|**[link](https://github.com/nvlabs/digitaltwinart)**|
|**2024-04-01**|**NVINS: Robust Visual Inertial Navigation Fused with NeRF-augmented Camera Pose Regressor and Uncertainty Quantification**|近年来，神经辐射场（NeRF）已成为三维重建和新型视图合成的强大工具。然而，NeRF渲染的计算成本和由于伪影的存在而导致的质量下降，对其在实时和鲁棒机器人任务中的应用，特别是在嵌入式系统中的应用提出了重大挑战。本文介绍了一种新的框架，该框架将NeRF导出的定位信息与视觉惯性里程计（VIO）相结合，为机器人实时导航提供了一个稳健的解决方案。通过使用NeRF渲染的增强图像数据训练绝对姿态回归网络并量化其不确定性，我们的方法有效地对抗了位置漂移并提高了系统可靠性。考虑到贝叶斯框架下的不确定性，我们还为将视觉惯性导航与相机定位神经网络相结合奠定了数学上坚实的基础。在真实感仿真环境中的实验验证表明，与传统的VIO方法相比，精度显著提高。 et.al.|[2404.01400](http://arxiv.org/abs/2404.01400)|null|
|**2024-04-01**|**FPGA-Accelerated Correspondence-free Point Cloud Registration with PointNet Features**|点云配准是视觉和机器人应用（包括3D重建和映射）的基础。尽管在结果质量上有了显著的改进，但最近的深度学习方法在计算上昂贵且耗电，使其难以部署在资源受限的边缘设备上。为了解决这个问题，在本文中，我们提出了一种快速、准确和稳健的低成本嵌入式FPGA注册方法。基于并行和流水线的PointNet特征提取器，我们为两种不同的基于学习的方法开发了自定义加速器核心，即PointLKCore和ReAgentCore。它们既没有对应关系，又在计算上高效，因为它们避免了涉及最近邻居搜索的代价高昂的特征匹配步骤。所提出的核心在Xilinx ZCU104板上实现，并使用合成和真实世界的数据集进行评估，显示了运行时间和注册质量之间的权衡有了实质性的改进。它们比ARM Cortex-A53 CPU运行速度快44.08-45.75倍，比Intel Xeon CPU和Nvidia Jetson板提供1.98-11.13倍的加速，同时与Nvidia GeForce GPU相比，功耗不到1W，能效达到163.11-213.58倍。与经典方法相比，所提出的核心对噪声和大的初始偏差更具鲁棒性，并在不到15ms的时间内快速找到合理的解决方案，展示了实时性能。 et.al.|[2404.01237](http://arxiv.org/abs/2404.01237)|null|
|**2024-04-02**|**Few-shot point cloud reconstruction and denoising via learned Guassian splats renderings and fine-tuned diffusion features**|现有的用于点云重建和去噪的深度学习方法依赖于3D形状的小数据集。我们通过利用在数十亿张图像上训练的深度学习方法来规避这个问题。我们提出了一种方法，通过利用从基于图像的深度学习模型中提取的先验知识，从少量图像中重建点云，并从渲染中对点云进行去噪。为了改进约束设置中的重建，我们通过引入语义一致性监督来规范具有混合表面和外观的可微渲染器的训练。此外，我们提出了一种微调稳定扩散的管道，以对噪声点云的渲染进行去噪，并演示了如何使用这些学习的滤波器来去除无需3D监督的点云噪声。我们将我们的方法与DSS和PointRadiance进行了比较，并在Sketchfab测试集和SCUT数据集上实现了更高质量的3D重建。 et.al.|[2404.01112](http://arxiv.org/abs/2404.01112)|null|
|**2024-04-01**|**Interpretable Multi-View Clustering Based on Anchor Graph Tensor Factorization**|基于锚图的聚类方法因其卓越的聚类性能和处理大规模数据的能力而受到广泛关注。一种常见的方法是学习具有K连通分量的二部图，这有助于避免后处理的需要。然而，这种方法有严格的参数要求，并且可能并不总是得到K连通分量。为了解决这个问题，一种替代方法是通过对锚图执行非负矩阵分解（NMF）来直接获得聚类标签矩阵。然而，现有的基于锚图分解的多视图聚类方法对分解后的矩阵缺乏足够的聚类可解释性，并且经常忽略视图间信息。我们通过使用非负张量分解来分解结合多个视图的锚图的锚图张量来解决这一限制。这种方法使我们能够全面考虑视图间信息。分解后的张量，即样本指标张量和锚指标张量，增强了因子分解的可解释性。大量实验验证了该方法的有效性。 et.al.|[2404.00883](http://arxiv.org/abs/2404.00883)|null|
|**2024-03-30**|**DiffHuman: Probabilistic Photorealistic 3D Reconstruction of Humans**|我们提出了DiffHuman，这是一种从单个RGB图像进行真实感3D人体重建的概率方法。尽管这个问题具有不适定性，但大多数方法都是确定性的，并输出单一的解决方案，通常导致在看不见或不确定的区域缺乏几何细节和模糊性。相反，DiffHuman预测了以输入2D图像为条件的3D重建的概率分布，这允许我们对与图像一致的多个详细3D化身进行采样。DiffHuman被实现为条件扩散模型，该模型对底层3D形状表示的像素对齐的2D观测值进行去噪。在推断期间，我们可以通过迭代地对预测的3D表示的2D渲染进行去噪来对3D化身进行采样。此外，我们引入了一种生成器神经网络，该网络以显著降低的运行时间（55倍的速度）近似渲染，从而产生了一种新的双分支扩散框架。我们的实验表明，DiffHuman可以对输入图像中看不见或不确定的人的部位进行多样化和详细的重建，同时在重建可见表面时与最先进的技术保持竞争力。 et.al.|[2404.00485](http://arxiv.org/abs/2404.00485)|null|

<p align=right>(<a href=#updated-on-20240404>back to top</a>)</p>

## Diffusion

|Publish Date|Title|Abstract|PDF|Code|
|---|---|---|---|---|
|**2024-04-03**|**Visual Autoregressive Modeling: Scalable Image Generation via Next-Scale Prediction**|我们提出了视觉自回归建模（VAR），这是一种新一代的范式，它将图像上的自回归学习重新定义为从粗到细的“下一尺度预测”或“下一分辨率预测”，与标准光栅扫描的“下个标记预测”不同。这种简单直观的方法使自回归（AR）变换器能够快速学习视觉分布并很好地推广：VAR首次使AR模型在图像生成方面超过扩散变换器。在ImageNet 256x256基准上，VAR通过将Frechet起始距离（FID）从18.65提高到1.80，起始得分（IS）从80.4提高到356.4，显著提高了AR基线，推理速度快了约20倍。还实证验证了VAR在图像质量、推理速度、数据效率和可扩展性等多个维度上优于扩散变换器（DiT）。放大VAR模型显示出与LLM中观察到的相似的清晰幂律缩放定律，接近-0.998的线性相关系数是确凿的证据。VAR进一步展示了零样本在下游任务中的泛化能力，包括图像内画、外画和编辑。这些结果表明，VAR最初模拟了LLM的两个重要特性：缩放定律和零样本任务泛化。我们已经发布了所有模型和代码，以促进AR/VAR模型的探索，用于视觉生成和统一学习。 et.al.|[2404.02905](http://arxiv.org/abs/2404.02905)|**[link](https://github.com/FoundationVision/VAR)**|
|**2024-04-03**|**LidarDM: Generative LiDAR Simulation in a Generated World**|我们提出了LidarDM，这是一种新颖的激光雷达生成模型，能够生成逼真、布局感知、物理上合理和时间上连贯的激光雷达视频。LidarDM在激光雷达生成建模方面具有两项前所未有的能力：（i）由驾驶场景引导的激光雷达生成，为自动驾驶模拟提供了巨大的潜力；（ii）4D激光雷达点云生成，能够创建逼真的时间相干序列。我们的模型的核心是一个新颖的集成4D世界生成框架。具体来说，我们使用潜在扩散模型来生成3D场景，将其与动态演员相结合，形成底层4D世界，然后在这个虚拟环境中产生逼真的感官观察。我们的实验表明，我们的方法在真实性、时间一致性和布局一致性方面优于竞争算法。我们还表明，LidarDM可以用作生成世界模型模拟器，用于训练和测试感知模型。 et.al.|[2404.02903](http://arxiv.org/abs/2404.02903)|null|
|**2024-04-03**|**MatAtlas: Text-driven Consistent Geometry Texturing and Material Assignment**|我们介绍了MatAtlas，一种用于一致文本引导的3D模型纹理化的方法。根据最近的进展，我们利用大规模文本到图像生成模型（例如，稳定扩散）作为纹理化3D模型之前的模型。我们精心设计了一个RGB纹理管道，它利用了由深度和边缘驱动的网格图案扩散。通过提出多步骤纹理细化过程，我们显著提高了纹理输出的质量和3D一致性。为了进一步解决烘焙照明的问题，我们超越了RGB颜色，转而将参数化材质指定给资源。考虑到高质量的初始RGB纹理，我们提出了一种新的基于大型语言模型（LLM）的材料检索方法，使其具有可编辑性和可重用性。我们在各种几何形状上评估了我们的方法，并表明我们的方法明显优于现有技术。我们还通过详细的消融研究分析了每个部件的作用。 et.al.|[2404.02899](http://arxiv.org/abs/2404.02899)|null|
|**2024-04-03**|**On the Scalability of Diffusion-based Text-to-Image Generation**|扩展模型和数据大小对于LLM的发展是非常成功的。然而，基于扩散的文本到图像（T2I）模型的缩放定律尚未得到充分探索。目前还不清楚如何有效地扩展模型，以降低成本获得更好的性能。不同的训练设置和昂贵的训练成本使得公平的模型比较极其困难。在这项工作中，我们通过对去噪主干和训练集的缩放进行广泛而严格的消融，实证研究了基于扩散的T2I模型的缩放特性，包括在高达600M图像的数据集上训练缩放的UNet和Transformer变体，参数范围从0.4B到4B。对于模型缩放，我们发现交叉注意力的位置和数量区分了现有UNet设计的性能。与增加通道数量相比，增加转换器块对于改善文本图像对齐更具参数效率。然后，我们确定了一种有效的UNet变体，它比SDXL的UNet小45%，快28%。在数据缩放方面，我们表明训练集的质量和多样性比简单的数据集大小更重要。增加字幕密度和多样性可以提高文本图像对齐性能和学习效率。最后，我们提供了缩放函数来预测文本图像对齐性能，作为模型大小、计算和数据集大小的缩放函数。 et.al.|[2404.02883](http://arxiv.org/abs/2404.02883)|null|
|**2024-04-03**|**Uniqueness of the blow-down limit for triple junction problem**|我们证明了具有三阱势的平面Allen-Cahn系统的整个最小化解 $u:\mathbb｛R｝^2 \rightarrow\mathbb｛R}^2$在无穷大处的$L^1$排污极限的唯一性。因此，$u$ 可以用无穷远处的三结映射来近似。该证明利用了对能量上限和下限的仔细分析，确保扩散界面在所有尺度上都保持在近似三结的小邻域内。 et.al.|[2404.02859](http://arxiv.org/abs/2404.02859)|null|
|**2024-04-03**|**Efficient Quantum Circuits for Non-Unitary and Unitary Diagonal Operators with Space-Time-Accuracy trade-offs**|酉和非酉对角算子是量子算法的基本组成部分，应用于偏微分方程的求解、哈密顿模拟、量子计算机上经典数据的加载（量子态制备）和许多其他方面。在本文中，我们介绍了一种用有效的可调深度量子电路实现酉和非酉对角算子的通用方法。深度，即量子电路的量子门的层数，可以相对于宽度，即辅助量子位的数量，或者相对于所实现的算子和目标算子之间的精度来减少。虽然精确方法在大小、｛\sl即｝基量子门的总数或宽度方面具有最佳指数标度，但近似方法被证明对依赖于光滑、至少可微函数的对角线算子类是有效的。我们的方法足够通用，可以允许对角线运算符的任何方法成为可调整的深度或近似值，通过增加其宽度或近似水平来减少电路的深度。该功能提供了灵活性，并且可以与相干时间或累积门误差方面的硬件限制相匹配。我们通过对扩散方程进行量子态制备和非酉实空间模拟来说明这些方法：在通过扩散过程的非酉演化算子演化之前，在一组量子位上制备初始高斯函数。 et.al.|[2404.02819](http://arxiv.org/abs/2404.02819)|null|
|**2024-04-03**|**Fast Diffusion Model For Seismic Data Noise Attenuation**|噪声是地震勘探中干扰的主要来源之一。许多作者提出了从地震数据中去除噪声的各种方法；然而，在强噪声条件下，往往无法获得令人满意的结果。近年来，基于扩散模型的方法已被应用于地震数据中的强噪声处理任务。然而，由于迭代计算，基于扩散的方法的计算效率远低于传统方法。为了解决这个问题，我们建议使用改进的贝叶斯方程进行迭代，从计算中去除随机项。此外，我们还提出了一种新的适用于扩散模型的归一化方法。通过各种改进，在合成数据集和现场数据集上，与基准方法相比，我们提出的方法实现了显著更好的噪声衰减效果，同时计算速度也提高了数倍。我们使用迁移学习来证明我们提出的方法在开源合成地震数据上的稳健性，并在开源现场数据集上进行验证。最后，我们开源了代码，促进了高精度高效地震勘探工作的发展。 et.al.|[2404.02767](http://arxiv.org/abs/2404.02767)|null|
|**2024-04-03**|**Cross-Attention Makes Inference Cumbersome in Text-to-Image Diffusion Models**|本研究探讨了在文本条件扩散模型中，交叉注意在推理过程中的作用。我们发现，经过几个推理步骤后，交叉注意力输出收敛到一个固定点。因此，收敛的时间点自然地将整个推理过程分为两个阶段：初始语义规划阶段，在此期间，模型依赖于交叉关注来规划面向文本的视觉语义，以及随后的保真度提高阶段，在此阶段，模型试图从先前规划的语义生成图像。令人惊讶的是，在保真度提高阶段忽略文本条件不仅降低了计算复杂度，而且保持了模型性能。这产生了一种简单且无需训练的方法，称为TGATE，用于高效生成，该方法在交叉注意力输出收敛后缓存交叉注意力输出，并在剩余的推理步骤中保持固定。我们对MS-COCO验证集的实证研究证实了其有效性。TGATE的源代码可在https://github.com/HaozheLiu-ST/T-GATE. et.al.|[2404.02747](http://arxiv.org/abs/2404.02747)|**[link](https://github.com/haozheliu-st/t-gate)**|
|**2024-04-03**|**InstantStyle: Free Lunch towards Style-Preserving in Text-to-Image Generation**|基于调整自由扩散的模型在图像个性化和定制领域显示出巨大的潜力。然而，尽管取得了显著进展，但当前的模型在生成风格一致的图像方面仍面临着几个复杂的挑战。首先，风格的概念本质上是不确定的，包括颜色、材料、氛围、设计和结构等众多元素。其次，基于反演的方法容易出现风格退化，往往导致细粒度细节的丢失。最后，基于适配器的方法经常需要对每个参考图像进行细致的权重调整，以实现风格强度和文本可控性之间的平衡。在本文中，我们首先考察了几个令人信服但经常被忽视的观察结果。然后，我们继续介绍InstantStyle，这是一个旨在通过实施两个关键策略来解决这些问题的框架：1）一种简单的机制，将风格和内容与特征空间内的参考图像解耦，其前提是假设同一空间内的特征可以相互相加或相减。2） 将参考图像特征专门注入到特定样式的块中，从而防止样式泄漏，并避免了繁琐的权重调整的需要，这通常是参数较多的设计的特点。我们的作品展示了卓越的视觉风格化结果，在风格的强度和文本元素的可控性之间取得了最佳平衡。我们的代码将在https://github.com/InstantStyle/InstantStyle. et.al.|[2404.02733](http://arxiv.org/abs/2404.02733)|**[link](https://github.com/instantstyle/instantstyle)**|
|**2024-04-03**|**Harnessing the Power of Large Vision Language Models for Synthetic Image Detection**|近年来，能够从文本中生成图像的模型的出现引起了人们的极大兴趣，提供了从文本描述中创建逼真图像的可能性。然而，这些进步也引发了人们对这些图像可能被滥用的担忧，包括制造虚假新闻和宣传等误导性内容。本研究调查了使用高级视觉语言模型（VLM）进行合成图像识别的有效性。具体而言，重点是调整用于合成图像检测的最先进的图像字幕模型。通过利用大型VLM强大的理解能力，目的是将真实图像与基于扩散的模型生成的合成图像区分开来。这项研究通过利用视觉语言模型（如BLIP-2和ViTGPT2）的能力，为合成图像检测的发展做出了贡献。通过定制图像字幕模型，我们解决了在现实世界应用中可能滥用合成图像的挑战。本文中描述的结果突出了VLM在合成图像检测领域的良好作用，优于传统的基于图像的检测技术。代码和型号可在https://github.com/Mamadou-Keita/VLM-DETECT. et.al.|[2404.02726](http://arxiv.org/abs/2404.02726)|null|

<p align=right>(<a href=#updated-on-20240404>back to top</a>)</p>

## NeRF

|Publish Date|Title|Abstract|PDF|Code|
|---|---|---|---|---|
|**2024-04-03**|**LiDAR4D: Dynamic Neural Fields for Novel Space-time View LiDAR Synthesis**|尽管神经辐射场（NeRFs）在图像新视图合成（NVS）方面取得了成功，但激光雷达NVS在很大程度上仍未被探索。以前的激光雷达NVS方法采用了图像NVS方法的简单转变，同时忽略了激光雷达点云的动态特性和大规模重建问题。有鉴于此，我们提出了LiDAR4D，这是一种用于新的时空LiDAR视图合成的仅限LiDAR的可微分框架。考虑到稀疏性和大规模特征，我们设计了一种结合多平面和网格特征的4D混合表示，以实现从粗到细的有效重建。此外，我们引入了从点云导出的几何约束，以提高时间一致性。对于激光雷达点云的真实合成，我们结合了光线下降概率的全局优化，以保持跨区域模式。在KITTI-360和NuScenes数据集上进行的大量实验证明了我们的方法在实现几何感知和时间一致的动态重建方面的优越性。代码可在https://github.com/ispc-lab/LiDAR4D. et.al.|[2404.02742](http://arxiv.org/abs/2404.02742)|null|
|**2024-04-03**|**Vestibular schwannoma growth_prediction from longitudinal MRI by time conditioned neural fields**|前庭神经鞘瘤（VS）是一种良性肿瘤，通常通过MRI检查进行积极监测来治疗。为了进一步帮助临床决策并避免过度治疗，基于纵向成像的肿瘤生长的准确预测是非常可取的。在本文中，我们介绍了DeepGrowth，这是一种深度学习方法，它结合了神经场和递归神经网络，用于前瞻性肿瘤生长预测。在所提出的方法中，每个肿瘤都表示为以低维潜在码为条件的有符号距离函数（SDF）。与之前直接在图像空间中进行肿瘤形状预测的研究不同，我们预测潜在代码，然后从中重建未来的形状。为了处理不规则的时间间隔，我们引入了一个基于ConvLSTM的时间条件递归模块和一种新的时间编码策略，使所提出的模型能够输出随时间变化的肿瘤形状。在内部纵向VS数据集上的实验表明，所提出的模型显著提高了性能（ $\ge 1.6\%%$Dice评分和$\ge0.20$mm95\%Hausdorff距离），特别是对于生长或缩小最多的前20%肿瘤（$\ge4.6\%%$Dice评分和$\ge 0.73$ mm95\%Hausdoff距离）。我们的代码可在~\bull获得{https://github.com/cyjdswx/DeepGrowth} et.al.|[2404.02614](http://arxiv.org/abs/2404.02614)|**[link](https://github.com/cyjdswx/deepgrowth)**|
|**2024-04-02**|**NeRFCodec: Neural Feature Compression Meets Neural Radiance Fields for Memory-Efficient Scene Representation**|神经辐射场（NeRF）的出现极大地影响了三维场景建模和新颖的视图合成。作为一种用于三维场景表示的视觉媒体，具有高率失真性能的压缩是一个永恒的目标。受神经压缩和神经场表示进步的启发，我们提出了NeRFCodec，这是一种端到端的NeRF压缩框架，它集成了非线性变换、量化和熵编码，用于高效记忆的场景表示。由于直接在大规模的NeRF特征平面上训练非线性变换是不切实际的，我们发现，当添加内容特定参数时，可以使用预先训练的神经2D图像编解码器来压缩特征。具体来说，我们重用神经2D图像编解码器，但修改其编码器和解码器头，同时保持预训练解码器的其他部分冻结。这使我们能够通过监督渲染损失和熵损失来训练整个管道，通过更新特定于内容的参数来实现率失真平衡。在测试时，包含潜在代码、特征解码器头和其他辅助信息的比特流被发送用于通信。实验结果表明，我们的方法优于现有的NeRF压缩方法，能够在0.5MB的内存预算下实现高质量的新视图合成。 et.al.|[2404.02185](http://arxiv.org/abs/2404.02185)|null|
|**2024-04-01**|**NeRF-MAE : Masked AutoEncoders for Self Supervised 3D representation Learning for Neural Radiance Fields**|神经领域在计算机视觉和机器人领域表现出色，因为它们能够理解3D视觉世界，如推断语义、几何和动力学。考虑到神经场在从2D图像密集表示3D场景方面的能力，我们提出了一个问题：我们是否可以扩展它们的自监督预训练，特别是使用掩蔽的自动编码器，从姿态RGB图像中生成有效的3D表示。由于将转换器扩展到新型数据模式的惊人成功，我们采用了标准的3D视觉转换器来适应NeRF的独特配方。我们利用NeRF的体积网格作为变压器的密集输入，将其与其他3D表示（如点云）进行对比，在点云中，信息密度可能不均匀，并且表示不规则。由于将掩蔽的自动编码器应用于隐式表示（如NeRF）很困难，我们选择提取通过使用相机轨迹进行采样来规范化跨域场景的显式表示。我们的目标是通过从NeRF的辐射和密度网格中屏蔽随机补丁，并使用标准的3D Swin Transformer来重建屏蔽的补丁。通过这样做，模型可以学习完整场景的语义和空间结构。我们在我们提出的精心策划的姿势RGB数据上对这种表示进行了大规模的预训练，总共超过160万张图像。一旦经过预训练，编码器就用于有效的3D迁移学习。我们针对NeRF的新型自监督预训练NeRF-MAE可扩展性非常好，并提高了在各种具有挑战性的3D任务中的性能。在Front3D和ScanNet数据集上，利用未标记的姿态2D数据进行预训练，NeRF MAE显著优于自监督3D预训练和NeRF场景理解基线，在3D对象检测方面的绝对性能提高超过20%AP50和8%AP25。 et.al.|[2404.01300](http://arxiv.org/abs/2404.01300)|null|
|**2024-03-29**|**Grounding and Enhancing Grid-based Models for Neural Fields**|当代许多研究利用基于网格的模型来表示神经场，但仍然缺乏对基于网格模型的系统分析，阻碍了这些模型的改进。因此，本文介绍了一个基于网格的模型的理论框架。该框架指出，这些模型的逼近和泛化行为是由网格切线核（GTK）决定的，GTK是基于网格的模型的固有性质。所提出的框架有助于对各种基于网格的模型进行一致和系统的分析。此外，引入的框架推动了一种新的基于网格的模型的开发，该模型名为乘法傅立叶自适应网格（MulFAGrid）。数值分析表明，MulFAGrid表现出比其前身更低的泛化界，表明其具有鲁棒的泛化性能。实证研究表明，MulFAGrid在各种任务中都取得了最先进的性能，包括2D图像拟合、3D符号距离场（SDF）重建和新颖的视图合成，表现出了卓越的表示能力。项目网站位于https://sites.google.com/view/cvpr24-2034-submission/home. et.al.|[2403.20002](http://arxiv.org/abs/2403.20002)|null|
|**2024-04-01**|**Efficient 3D Instance Mapping and Localization with Neural Fields**|我们解决了从一系列摆姿势的RGB图像中学习用于3D实例分割的隐式场景表示的问题。为此，我们引入了3DIML，这是一种新的框架，可以有效地学习可以从新的视点渲染的标签字段，以产生视图一致的实例分割掩码。3DIML显著改进了现有的基于隐式场景表示的方法的训练和推理运行时。与现有技术相反，现有技术以自我监督的方式优化神经场，需要复杂的训练过程和损失函数设计，3DIML利用了两阶段过程。第一阶段InstanceMap将前端实例分割模型生成的图像序列的2D分割掩码作为输入，并将图像上的相应掩码与3D标签相关联。然后，在第二阶段InstanceLift中使用这些几乎视图一致的伪标签掩码来监督神经标签字段的训练，该字段对InstanceMap遗漏的区域进行插值并解决歧义。此外，我们介绍了InstanceLoc，它能够在给定训练过的标签字段和现成的图像分割模型的情况下，通过融合两者的输出，实现实例掩码的近实时定位。我们在Replica和ScanNet数据集的序列上评估了3DIML，并证明了在图像序列的温和假设下3DIML的有效性。与现有的质量相当的隐式场景表示方法相比，我们实现了巨大的实际加速，展示了其促进更快、更有效的3D场景理解的潜力。 et.al.|[2403.19797](http://arxiv.org/abs/2403.19797)|null|
|**2024-03-28**|**Neural Fields for 3D Tracking of Anatomy and Surgical Instruments in Monocular Laparoscopic Video Clips**|腹腔镜视频跟踪主要关注两种目标类型：手术器械和解剖结构。前者可用于技能评估，而后者对于虚拟覆盖的投影是必要的。在仪器和解剖跟踪通常被视为两个独立的问题的情况下，在本文中，我们提出了一种同时对所有结构进行联合跟踪的方法。基于单个2D单眼视频剪辑，我们训练神经场来表示连续的时空场景，用于创建至少一帧中可见的所有表面的3D轨迹。由于仪器尺寸较小，它们通常只覆盖图像的一小部分，导致跟踪精度下降。因此，我们建议增强类权重以改善仪器轨迹。我们评估了对腹腔镜胆囊切除术视频片段的跟踪，发现解剖结构和器械的平均跟踪准确率分别为92.4%和87.4%。此外，我们还评估了从该方法的场景重建中获得的深度图的质量。我们表明，这些伪深度具有与最先进的预训练深度估计器相当的质量。在SCARED数据集中的腹腔镜视频上，该方法预测深度的MAE为2.9 mm，相对误差为9.2%。这些结果表明了使用神经场进行腹腔镜场景的单目3D重建的可行性。 et.al.|[2403.19265](http://arxiv.org/abs/2403.19265)|null|
|**2024-03-28**|**From Activation to Initialization: Scaling Insights for Optimizing Neural Fields**|在计算机视觉领域，神经场作为一种利用神经网络进行信号表示的现代工具，已经获得了突出地位。尽管在调整这些网络以解决各种问题方面取得了显著进展，但该领域仍然缺乏一个全面的理论框架。本文旨在通过深入研究初始化和激活之间复杂的相互作用来解决这一差距，为神经领域的稳健优化提供基础。我们的理论见解揭示了网络初始化、架构选择和优化过程之间的深层次联系，强调在设计尖端神经场时需要整体方法。 et.al.|[2403.19205](http://arxiv.org/abs/2403.19205)|null|
|**2024-03-22**|**LATTE3D: Large-scale Amortized Text-To-Enhanced3D Synthesis**|最近的文本到3D生成方法产生了令人印象深刻的3D结果，但需要耗时的优化，每次提示可能需要一个小时。ATT3D等摊销方法同时优化多个提示以提高效率，实现快速的文本到三维合成。然而，它们无法捕捉高频几何体和纹理细节，并且难以缩放到大型提示集，因此泛化能力较差。我们引入LATTE3D，解决了这些限制，以在更大的提示集上实现快速、高质量的生成。我们方法的关键是1）构建可扩展的体系结构，2）在优化过程中通过3D感知扩散先验、形状正则化和模型初始化来利用3D数据，以实现对各种复杂训练提示的鲁棒性。LATTE3D对神经场和纹理表面生成进行摊销，以在单个正向过程中生成高度详细的纹理网格。LATTE3D在400ms内生成3D对象，并可通过快速测试时间优化进一步增强。 et.al.|[2403.15385](http://arxiv.org/abs/2403.15385)|null|
|**2024-03-20**|**Visual Imitation Learning of Task-Oriented Object Grasping and Rearrangement**|面向任务的物体抓取和重排是机器人完成不同现实操作任务的关键技能。然而，由于对物体的部分观察和分类物体的形状变化，它们仍然具有挑战性。在本文中，我们提出了多特征隐式模型（MIMO），这是一种新的对象表示，它在隐式神经场中对点和对象之间的多个空间特征进行编码。在多个特征上训练这样的模型可以确保它在不同方面一致地嵌入物体形状，从而提高其在从局部观察、形状相似性测量和建模物体之间的空间关系的物体形状重建中的性能。基于MIMO，我们提出了一个从单个或多个人类演示视频中学习面向任务的对象抓取和重排的框架。仿真评估表明，我们的方法在多视图和单视图观测方面优于最先进的方法。真实世界的实验证明了我们的方法在操纵任务的单次和少次模仿学习中的有效性。 et.al.|[2403.14000](http://arxiv.org/abs/2403.14000)|null|

<p align=right>(<a href=#updated-on-20240404>back to top</a>)</p>

[contributors-shield]: https://img.shields.io/github/contributors/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[contributors-url]: https://github.com/Vincentqyw/cv-arxiv-daily/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[forks-url]: https://github.com/Vincentqyw/cv-arxiv-daily/network/members
[stars-shield]: https://img.shields.io/github/stars/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[stars-url]: https://github.com/Vincentqyw/cv-arxiv-daily/stargazers
[issues-shield]: https://img.shields.io/github/issues/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[issues-url]: https://github.com/Vincentqyw/cv-arxiv-daily/issues

