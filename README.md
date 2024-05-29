[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]

## Updated on 2024.05.29
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
|**2024-05-27**|**DOF-GS: Adjustable Depth-of-Field 3D Gaussian Splatting for Refocusing,Defocus Rendering and Blur Removal**|基于3D高斯散射的技术最近推进了3D场景重建和新颖的视图合成，实现了高质量的实时渲染。然而，这些方法在建模图像时受到针孔相机假设的固有限制，因此仅适用于全聚焦（AiF）清晰图像输入。这严重影响了它们在真实世界场景中的适用性，其中由于成像设备的有限景深（DOF），图像经常表现出散焦模糊。此外，现有的三维高斯散射（3DGS）方法也不支持DOF效果的渲染。为了解决这些挑战，我们引入了DOF-GS，它允许渲染可调节的DOF效果，消除散焦模糊以及重新聚焦3D场景，所有这些都来自因散焦模糊而退化的多视图图像。为此，我们通过使用有限孔径相机模型，结合由混淆圆（CoC）引导的显式、可微分散焦渲染，重新想象传统的高斯散射管道。所提出的框架通过按需改变底层相机模型的光圈和焦距来提供DOF效果的动态调整。它还能够在优化后渲染3D场景的不同DOF效果，并从散焦训练图像生成AiF图像。此外，我们设计了一种联合优化策略，通过联合优化渲染的散焦图像和AiF图像来进一步增强重建场景中的细节。我们的实验结果表明，DOF-GS在受散焦模糊影响的输入的条件下产生高质量的清晰全聚焦渲染，训练过程仅导致GPU内存消耗的适度增加。我们进一步展示了所提出的方法在可调散焦渲染和从因散焦模糊而退化的输入图像重新聚焦3D场景中的应用。 et.al.|[2405.17351](http://arxiv.org/abs/2405.17351)|null|
|**2024-05-27**|**GenWarp: Single Image to Novel Views with Semantic-Preserving Generative Warping**|由于3D场景的复杂性和现有多视图数据集训练模型的多样性有限，从单个图像生成新视图仍然是一项具有挑战性的任务。最近的研究将大规模文本到图像（T2I）模型与单目深度估计（MDE）相结合，在处理野生图像方面显示出了前景。在这些方法中，输入视图被几何扭曲为具有估计的深度图的新视图，然后扭曲的图像被T2I模型修复。然而，当将输入视图扭曲为新颖的视点时，它们很难处理嘈杂的深度图和语义细节的丢失。在本文中，我们提出了一种新的单镜头新视图合成方法，这是一种语义保持的生成扭曲框架，通过用自注意增强跨视图注意力，使T2I生成模型能够学习在哪里扭曲和在哪里生成。我们的方法通过将生成模型以源视图图像为条件并结合几何扭曲信号来解决现有方法的局限性。定性和定量评估表明，我们的模型在域内和域外场景中都优于现有方法。项目页面位于https://GenWarp-NVS.github.io/. et.al.|[2405.17251](http://arxiv.org/abs/2405.17251)|null|
|**2024-05-24**|**Feature Splatting for Better Novel View Synthesis with Low Overlap**|3D高斯飞溅已经成为一种非常有前途的场景表示，在新的视图合成中实现最先进的质量明显快于竞争对手。然而，它使用球面谐波来表示场景颜色限制了3D高斯的表现力，因此，当我们离开训练视图时，该表示的泛化能力也受到了限制。在本文中，我们提出将3D高斯的颜色信息编码为每高斯特征向量，我们将其表示为特征飞溅（FeatSplat）。为了合成一个新的视图，首先将高斯“飞溅”到图像平面中，然后对相应的特征向量进行阿尔法混合，最后通过小MLP对混合向量进行解码，以渲染RGB像素值。为了进一步告知模型，我们将相机嵌入连接到混合特征向量，以使解码也以视点信息为条件。我们的实验表明，这些用于编码辐射的新模型显著改进了远离训练视图的低重叠视图的新视图合成。最后，我们还展示了我们的特征向量表示的能力和便利性，展示了它不仅能够为新视图生成RGB值，而且能够生成其每像素语义标签。我们将在接受后发布代码。关键词：高斯散射、新视图合成、特征散射 et.al.|[2405.15518](http://arxiv.org/abs/2405.15518)|null|
|**2024-05-24**|**NVS-Solver: Video Diffusion Model as Zero-Shot Novel View Synthesizer**|通过利用预先训练的大型视频扩散模型的强大生成能力，我们提出了NVS解算器，这是一种新的视图合成（NVS）范式，无需训练即可进行操作。NVS解算器自适应地调整具有给定视图的扩散采样过程，以便能够从静态场景的单个或多个视图或动态场景的单目视频中创建显著的视觉体验。具体来说，在我们的理论建模的基础上，我们用扭曲的输入视图表示的给定场景先验迭代地调制分数函数，以控制视频扩散过程。此外，通过理论上探索估计误差的边界，我们根据视点姿态和扩散步骤的数量以自适应的方式实现调制。对静态和动态场景的广泛评估证实了我们的NVS解算器在数量和质量上都优于最先进的方法。\textit｛源代码在｝\href{https://github.com/ZHU-Zhiyu/NVS_Solver}{https://github.com/ZHU-Zhiyu/NVS $\_$$ Solver｝。 et.al.|[2405.15364](http://arxiv.org/abs/2405.15364)|**[link](https://github.com/zhu-zhiyu/nvs_solver)**|
|**2024-05-24**|**DisC-GS: Discontinuity-aware Gaussian Splatting**|最近，高斯散射（Gaussian Splatting）是一种将3D场景表示为高斯分布集合的方法，在解决新视图合成任务方面受到了极大的关注。在本文中，我们强调了高斯散射的一个基本限制：由于高斯分布的连续性，它无法准确地渲染图像中的不连续性和边界。为了解决这个问题，我们提出了一种新的框架，使高斯Splatting能够执行不连续感知的图像渲染。此外，我们在我们的框架中引入了一种B’zier边界梯度近似策略，以保持所提出的不连续感知渲染过程的“可微性”。大量实验证明了我们的框架的有效性。 et.al.|[2405.15196](http://arxiv.org/abs/2405.15196)|null|
|**2024-05-27**|**HDR-GS: Efficient High Dynamic Range Novel View Synthesis at 1000x Speed via Gaussian Splatting**|高动态范围（HDR）新视图合成（NVS）旨在使用HDR成像技术从新视点创建真实感图像。与普通低动态范围（LDR）图像相比，渲染的HDR图像捕获更宽范围的亮度级别，其中包含更多的场景细节。现有的HDR NVS方法主要基于NeRF。它们的训练时间长，推理速度慢。在本文中，我们提出了一种新的框架，即高动态范围高斯散射（HDR-GS），它可以有效地渲染新的HDR视图，并在用户输入曝光时间的情况下重建LDR图像。具体来说，我们设计了一个双动态范围（DDR）高斯点云模型，该模型使用球面谐波来拟合HDR颜色，并使用基于MLP的色调映射器来渲染LDR颜色。然后将HDR和LDR颜色馈送到两个并行可微分光栅化（PDR）过程中，以重建HDR和LDPR视图。为了为HDR NVS中基于3D高斯飞溅的方法的研究奠定数据基础，我们重新校准了相机参数并计算了高斯点云的初始位置。实验表明，我们的HDR-GS在LDR和HDR-NVS上分别超过了最先进的基于NeRF的方法3.84和1.91dB，同时具有1000倍的推理速度，只需要6.3%的训练时间。代码、模型和重新校准的数据将在https://github.com/caiyuanhao1998/HDR-GS et.al.|[2405.15125](http://arxiv.org/abs/2405.15125)|**[link](https://github.com/caiyuanhao1998/hdr-gs)**|
|**2024-05-24**|**GS-Hider: Hiding Messages into 3D Gaussian Splatting**|三维高斯散射（3DGS）已经成为三维场景重建和新型视图合成领域的新兴研究热点。鉴于训练3DGS需要大量的时间和计算成本，保护此类3D资产的版权、完整性和隐私至关重要。隐写术作为加密传输和版权保护的关键技术，已被广泛研究。然而，它仍然缺乏针对3DGS的深入探索。与前代NeRF不同，3DGS具有两个明显的特征：1）显式的3D表示；以及2）实时渲染速度。这些特性导致3DGS点云文件是公开和透明的，每个高斯点都具有明确的物理意义。因此，在将信息嵌入3DGS点云文件的同时，确保原始3D场景的安全性和保真度是一项极具挑战性的任务。为了解决上述问题，我们首先提出了一种用于3DGS的隐写术框架，称为GS Hider，它可以以不可见的方式将3D场景和图像嵌入到原始GS点云中，并准确地提取隐藏的消息。具体来说，我们设计了一个耦合的安全特征属性来替换原始3DGS的球面谐波系数，然后使用场景解码器和消息解码器来解开原始RGB场景和隐藏消息。大量实验表明，所提出的GS隐藏器可以在不影响渲染质量的情况下有效隐藏多模式消息，并具有卓越的安全性、鲁棒性、容量和灵活性。我们的项目位于：https://xuanyuzhang21.github.io/project/gshider. et.al.|[2405.15118](http://arxiv.org/abs/2405.15118)|null|
|**2024-05-23**|**NeRF-Casting: Improved View-Dependent Appearance with Consistent Reflections**|神经辐射场（NeRF）通常难以重建和渲染高度镜面反射的对象，这些对象的外观随着视点的变化而快速变化。最近的工作提高了NeRF渲染远处环境照明的详细镜面外观的能力，但无法合成较近内容的一致反射。此外，这些技术依赖于计算成本高昂的大型神经网络来对出射辐射进行建模，这严重限制了优化和渲染速度。我们使用一种基于光线跟踪的方法来解决这些问题：我们的模型不是向昂贵的神经网络查询每条相机光线上各点的出射视图相关辐射，而是从这些点投射反射光线，并通过NeRF表示进行跟踪，以渲染使用小型廉价网络解码为颜色的特征向量。我们证明，我们的模型在包含闪亮物体的场景的视图合成方面优于现有方法，并且它是唯一一种能够在真实世界场景中合成照片级真实镜面外观和反射的NeRF方法，同时需要与当前最先进的视图合成模型相当的优化时间。 et.al.|[2405.14871](http://arxiv.org/abs/2405.14871)|null|
|**2024-05-23**|**Generative Camera Dolly: Extreme Monocular Dynamic Novel View Synthesis**|在计算机视觉中，仅从单个视点精确重建复杂的动态场景仍然是一项具有挑战性的任务。当前的动态新颖视图合成方法通常需要来自许多不同相机视点的视频，这需要仔细的记录设置，并大大限制了它们在野外以及具体的人工智能应用中的实用性。在本文中，我们提出了 $\textbf{GCD}$ ，这是一种可控的单目动态视图合成管道，它利用大规模扩散先验，在给定任何场景的视频的情况下，以一组相对相机姿态参数为条件，从任何其他选择的视角生成同步视频。我们的模型不需要深度作为输入，也不明确地对3D场景几何进行建模，而是执行端到端的视频到视频转换，以有效地实现其目标。尽管只在合成多视图视频数据上进行训练，但零样本现实世界的泛化实验在机器人、物体持久性和驾驶环境等多个领域都显示出了有希望的结果。我们相信，我们的框架有可能在丰富的动态场景理解、机器人感知和虚拟现实的交互式3D视频观看体验中解锁强大的应用程序。 et.al.|[2405.14868](http://arxiv.org/abs/2405.14868)|null|
|**2024-05-23**|**Tele-Aloha: A Low-budget and High-authenticity Telepresence System Using Sparse RGB Cameras**|在本文中，我们针对对等通信场景，提出了一种低预算、高真实性的双向遥现系统Tele Aloha。与以前的系统相比，Tele Aloha仅使用四个稀疏RGB相机、一个消费级GPU和一个自动立体屏幕来实现高分辨率（2048x2048）、实时性（30fps）、低延迟（小于150ms）和强大的远程通信。作为Tele Aloha的核心，我们提出了一种高效的上半身视图合成算法。首先，我们设计了一个级联视差估计器来获得鲁棒的几何线索。此外，还引入了一个通过高斯散射的神经光栅化器，将潜在特征投影到目标视图上，并将其解码为降低的分辨率。此外，考虑到高质量的捕获数据，我们利用加权混合机制将解码图像细化为2K的最终分辨率。利用世界领先的自动立体显示和低延迟虹膜跟踪，即使没有任何可穿戴的头戴式显示设备，用户也能够体验到强烈的三维感。总之，我们的远程呈现系统在现实生活中的实验中展示了共同存在感，激发了下一代的交流。 et.al.|[2405.14866](http://arxiv.org/abs/2405.14866)|null|

<p align=right>(<a href=#updated-on-20240529>back to top</a>)</p>

## 3D Reconstruction

|Publish Date|Title|Abstract|PDF|Code|
|---|---|---|---|---|
|**2024-05-27**|**Memorize What Matters: Emergent Scene Decomposition from Multitraverse**|人类自然会保留对永恒元素的记忆，而短暂的时刻往往会从记忆的缝隙中溜走。这种选择性保留对于机器人感知、定位和绘图至关重要。为了赋予机器人这种能力，我们引入了3D高斯映射（3DGM），这是一种基于3D高斯飞溅的自监督、仅限相机的离线映射框架。3DGM将来自同一区域的多遍历RGB视频转换为基于高斯的环境图，同时执行2D短暂对象分割。我们的主要观察结果是，环境在遍历中保持一致，而对象经常发生变化。这使我们能够利用重复遍历的自我监督来实现环境对象分解。更具体地说，3DGM将多遍历环境映射公式化为一个鲁棒的可微渲染问题，将环境和对象的像素分别视为内值和外值。3DGM使用稳健特征提取、特征残差挖掘和稳健优化，在没有人工干预的情况下联合执行3D映射和2D分割。我们建立了Mapverse基准，来源于伊萨卡365和nuPlan数据集，以评估我们在无监督二维分割、三维重建和神经渲染中的方法。大量结果验证了我们的方法在自动驾驶和机器人方面的有效性和潜力。 et.al.|[2405.17187](http://arxiv.org/abs/2405.17187)|null|
|**2024-05-27**|**SDL-MVS: View Space and Depth Deformable Learning Paradigm for Multi-View Stereo Reconstruction in Remote Sensing**|基于遥感图像的多视角立体研究促进了大规模城市三维重建的发展。然而，遥感多视点图像数据在获取过程中存在遮挡和视点之间亮度不均匀的问题，这导致了深度估计中细节模糊的问题。为了解决上述问题，我们重新审视了多视图立体任务中的可变形学习方法，并提出了一种基于视图空间和深度可变形学习（SDL-MVS）的新范式，旨在学习不同视图空间中特征的可变形交互，并对深度范围和区间进行可变形建模，以实现高精度的深度估计。具体来说，为了解决遮挡和亮度不均匀导致的视图噪声问题，我们提出了一种渐进空间可变形采样（PSS）机制，该机制以渐进的方式对3D截头体空间和2D图像空间中的采样点进行可变形学习，以自适应地将源特征嵌入到参考特征中。为了进一步优化深度，我们引入了深度假设可变形离散化（DHD），它通过自适应调整深度范围假设和对深度区间假设进行可变形离散来实现深度先验的精确定位。最后，我们的SDL-MVS通过视图空间和深度的可变形学习范式，实现了多视图立体中遮挡和亮度不均的显式建模，实现了精确的多视图深度估计。在珞珈MVS和WHU数据集上进行的大量实验表明，我们的SDL-MVS达到了最先进的性能。值得注意的是，在三个视图作为输入的前提下，我们的SDL-MVS在珞珈MVS数据集上实现了0.086的MAE误差，<0.6米的准确率为98.9%，<3区间的准确度为98.9%。 et.al.|[2405.17140](http://arxiv.org/abs/2405.17140)|null|
|**2024-05-27**|**DINO-SD: Champion Solution for ICRA 2024 RoboDepth Challenge**|环绕视图深度估计是一项关键任务，旨在获取周围视图的深度图。它在自动驾驶、AR/VR和3D重建等现实场景中有许多应用。然而，鉴于自动驾驶数据集中的大部分数据都是在白天场景中收集的，这导致深度模型在面对分布外（OoD）数据时性能较差。虽然一些工作试图提高OoD数据下深度模型的稳健性，但这些方法要么需要额外的训练数据，要么需要湖的可推广性。在本报告中，我们介绍了DINO-SD，一种新的环绕视图深度估计模型。我们的DINO-SD不需要额外的数据，并且具有很强的稳健性。我们的DINO-SD在ICRA 2024机器人深度挑战赛的赛道4中获得最佳表现。 et.al.|[2405.17102](http://arxiv.org/abs/2405.17102)|null|
|**2024-05-27**|**Part123: Part-aware 3D Reconstruction from a Single-view Image**|最近，扩散模型的出现为单视图重建开辟了新的机会。然而，所有现有的方法都将目标对象表示为没有任何结构信息的闭合网格，从而忽略了重建形状的基于零件的结构，这对许多下游应用至关重要。此外，生成的网格通常会遇到大噪声、表面不光滑和纹理模糊的问题，这使得使用3D分割技术获得令人满意的零件分割具有挑战性。在本文中，我们提出了Part123，这是一种从单视图图像进行零件感知三维重建的新框架。我们首先使用扩散模型从给定的图像中生成多视角一致的图像，然后利用对任意对象表现出强大泛化能力的分段任意模型（SAM）来生成多视角分割掩模。为了有效地将基于2D零件的信息纳入3D重建并处理不一致性，我们将对比学习引入神经渲染框架，以学习基于多视图分割掩模的零件感知特征空间。还开发了一种基于聚类的算法，以从重建的模型中自动导出3D零件分割结果。实验表明，我们的方法可以在各种物体上生成具有高质量分割部分的三维模型。与现有的非结构化重建方法相比，该方法中的零件感知三维模型有利于一些重要的应用，包括特征保持重建、基元拟合和三维形状编辑。 et.al.|[2405.16888](http://arxiv.org/abs/2405.16888)|null|
|**2024-05-28**|**3D Reconstruction with Fast Dipole Sums**|我们介绍了一种从多视图图像重建高保真表面的技术。我们的技术使用了一种新的基于点的表示，即偶极和，它推广了绕组数，以允许在具有噪声或异常点的点云中对任意每点属性进行插值。使用偶极和，我们可以根据点云的点属性来表示隐含的几何和辐射场，我们可以直接从运动的结构中初始化点云。我们还推导了用于加速正向和反向模式偶极和查询的Barnes-Hut快速求和方案。这些查询有助于使用光线跟踪，以使用基于点的表示高效且可微分地渲染图像，从而更新其点属性以优化场景几何体和外观。我们根据最先进的替代方案，基于神经表示的光线跟踪或基于高斯点的表示的光栅化，来评估这种反向渲染框架。我们的技术在同等运行时间显著提高了重建质量，同时还支持更通用的渲染技术，如用于直接照明的阴影光线。在补充中，我们提供了结果的交互式可视化。 et.al.|[2405.16788](http://arxiv.org/abs/2405.16788)|null|
|**2024-05-26**|**Splat-SLAM: Globally Optimized RGB-only SLAM with 3D Gaussians**|3D Gaussian Splatting已成为仅RGB密集同时定位和映射（SLAM）的几何和外观的强大表示，因为它提供了紧凑的密集地图表示，同时实现了高效和高质量的地图渲染。然而，现有方法显示出比使用其他3D表示（如神经点云）的竞争方法差得多的重建质量，因为它们要么不采用全局地图和姿态优化，要么利用单目深度。作为回应，我们提出了第一个具有密集3D高斯图表示的仅RGB SLAM系统，该系统通过主动变形3D高斯图来动态适应关键帧姿态和深度更新，从而利用全局优化跟踪的所有好处。此外，我们发现，用单目深度估计器细化不准确区域的深度更新进一步提高了3D重建的准确性。我们在Replica、TUM-RGBD和ScanNet数据集上的实验表明了全局优化的3D高斯的有效性，因为该方法在跟踪、映射和渲染精度方面与现有的仅RGB的SLAM方法实现了卓越或不相上下的性能，同时产生了小的地图大小和快速的运行时间。源代码位于https://github.com/eriksandstroem/Splat-SLAM. et.al.|[2405.16544](http://arxiv.org/abs/2405.16544)|null|
|**2024-05-25**|**Neural Network-Based Tracking and 3D Reconstruction of Baseball Pitch Trajectories from Single-View 2D Video**|在本文中，我们提出了一种基于神经网络的方法，用于跟踪和重建棒球场从2D视频片段到3D坐标的轨迹。我们利用OpenCV的CSRT算法来准确跟踪2D视频帧中的棒球和固定参考点。然后，这些跟踪的像素坐标被用作我们的神经网络模型的输入特征，该模型包括多个完全连接的层，以将2D坐标映射到3D空间。该模型使用均方误差损失函数和Adam优化器在标记轨迹的数据集上进行训练，优化网络以最大限度地减少预测误差。我们的实验结果表明，这种方法在从2D输入重建3D轨迹时实现了高精度。这种方法在运动分析、指导和提高各种运动轨迹预测的准确性方面显示出巨大的应用潜力。 et.al.|[2405.16296](http://arxiv.org/abs/2405.16296)|null|
|**2024-05-25**|**3D reconstruction of a million atoms by multiple-section local-orbital tomography**|存在两组能够提供物体的三维（3D）结构信息的电子显微镜方法，即电子断层扫描和深度切片。电子断层扫描能够在所有三维中解析原子，但原子位置的精度较低，并且可以重建的物体尺寸有限。深度切片方法在成像平面中给出高的位置精度，但在第三维中的空间分辨率低。在这项工作中，电子断层扫描和深度切片相结合，形成了一种称为多切片局部轨道断层扫描的方法，简称nLOT。nLOT方法在所有三维中提供高空间分辨率和高位置精度。可以重建的物体大小被扩展到一百万个原子。本方法为原子电子层析成像的广泛应用奠定了基础。 et.al.|[2405.16007](http://arxiv.org/abs/2405.16007)|null|
|**2024-05-24**|**LAM3D: Large Image-Point-Cloud Alignment Model for 3D Reconstruction from Single Image**|大型重建模型在从单个或多个输入图像自动生成3D内容的领域取得了重大进展。尽管这些模型取得了成功，但由于仅从图像数据推导3D形状的固有挑战，这些模型通常会产生几何不准确的3D网格。在这项工作中，我们介绍了一种新的框架，即大图像和点云对齐模型（LAM3D），它利用3D点云数据来增强生成的3D网格的保真度。我们的方法从开发基于点云的网络开始，该网络可以有效地生成精确且有意义的潜在三平面，为精确的三维网格重建奠定基础。在此基础上，我们的图像点云特征对齐技术处理单个输入图像，与潜在的三平面对齐，为图像特征注入稳健的3D信息。该过程不仅丰富了图像特征，而且有助于在不需要多视图输入的情况下生成高保真3D网格，显著减少了几何失真。我们的方法仅用6秒就从单个图像中实现了最先进的高保真3D网格重建，在各种数据集上的实验证明了其有效性。 et.al.|[2405.15622](http://arxiv.org/abs/2405.15622)|null|
|**2024-05-24**|**DiffCalib: Reformulating Monocular Camera Calibration as Diffusion-Based Dense Incident Map Generation**|单眼相机校准是众多3D视觉应用的关键前提条件。尽管取得了相当大的进步，但现有的方法往往依赖于特定的假设，难以在不同的现实世界场景中进行推广，并且性能受到训练数据不足的限制。最近，在扩展数据集上训练的扩散模型已被证实能够保持生成多样化、高质量图像的能力。这一成功表明，模型在有效理解各种视觉信息方面具有强大的潜力。在这项工作中，我们利用嵌入预先训练的扩散模型中的全面视觉知识，实现更稳健、更准确的单目相机固有估计。具体而言，我们将相机固有参数的四个自由度（4-DoF）估计问题重新表述为密集入射图生成任务。该图详细说明了RGB图像中每个像素的入射角，其格式与扩散模型的范例非常一致。然后，在推理过程中，可以使用简单的非学习RANSAC算法从事件图中导出相机固有值。此外，为了进一步提高性能，我们联合估计深度图，为事件图估计提供额外的几何信息。在多个测试数据集上进行的大量实验表明，我们的模型实现了最先进的性能，预测误差减少了40%。此外，实验还表明，我们的管道估计的精确相机固有图和深度图可以极大地有利于实际应用，如从单个野生图像进行3D重建。 et.al.|[2405.15619](http://arxiv.org/abs/2405.15619)|null|

<p align=right>(<a href=#updated-on-20240529>back to top</a>)</p>

## Diffusion

|Publish Date|Title|Abstract|PDF|Code|
|---|---|---|---|---|
|**2024-05-27**|**Collaborative Video Diffusion: Consistent Multi-video Generation with Camera Control**|最近，视频生成的研究取得了巨大进展，使高质量的视频能够从文本提示或图像中生成。为视频生成过程增加控制是向前推进的一个重要目标，最近将视频生成模型置于相机轨迹之上的方法正在朝着这一目标迈进。然而，从多个不同的相机轨迹生成同一场景的视频仍然具有挑战性。这种多视频生成问题的解决方案可以实现具有可编辑相机轨迹的大规模3D场景生成以及其他应用。我们引入协作视频扩散（CVD）作为实现这一愿景的重要一步。CVD框架包括一种新颖的跨视频同步模块，该模块使用核极注意力机制来促进从不同相机姿势渲染的相同视频的对应帧之间的一致性。如大量实验所示，CVD在用于视频生成的最先进的相机控制模块的基础上进行训练，生成从不同相机轨迹渲染的多个视频，其一致性明显优于基线。项目页面：https://collaborativevideodiffusion.github.io/. et.al.|[2405.17414](http://arxiv.org/abs/2405.17414)|null|
|**2024-05-27**|**Human4DiT: Free-view Human Video Generation with 4D Diffusion Transformer**|我们提出了一种在任意视点下从单个图像生成高质量、时空连贯的人类视频的新方法。我们的框架结合了用于精确条件注入的U-Nets和用于捕捉视点和时间之间的全局相关性的扩散变换器的优势。核心是级联的4D转换器架构，该架构跨视图、时间和空间维度分解注意力，实现4D空间的高效建模。通过将人的身份、相机参数和时间信号注入相应的变换器来实现精确的调节。为了训练该模型，我们策划了一个涵盖图像、视频、多视图数据和3D/4D扫描的多维数据集，以及多维训练策略。我们的方法克服了以前基于GAN或UNet的扩散模型的方法的局限性，这些方法难以处理复杂的运动和视点变化。通过广泛的实验，我们展示了我们的方法合成逼真、连贯和自由视角的人类视频的能力，为虚拟现实和动画等领域的高级多媒体应用铺平了道路。我们的项目网站是https://human4dit.github.io. et.al.|[2405.17405](http://arxiv.org/abs/2405.17405)|null|
|**2024-05-27**|**A Closer Look at Time Steps is Worthy of Triple Speed-Up for Diffusion Model Training**|训练扩散模型总是一项计算密集型任务。在本文中，我们介绍了一种新的扩散模型训练加速方法，称为，它基于对时间步长的仔细观察。我们的主要发现是：i）根据过程增量，时间步长可以根据经验分为加速、减速和收敛区域。ii）这些时间步长是不平衡的，许多时间步长集中在收敛区域。iii）集中的步骤对扩散训练的益处有限。为了解决这一问题，我们设计了一种不对称采样策略，该策略降低了收敛区域的步长频率，同时增加了其他区域步长的采样概率。此外，我们提出了一种加权策略，以强调具有快速变化过程增量的时间步长的重要性。作为一种即插即用和体系结构无关的方法，SpeeD在各种扩散体系结构、数据集和任务中始终实现3倍的加速。值得注意的是，由于其简单的设计，我们的方法以最小的开销显著降低了扩散模型训练的成本。我们的研究使更多的研究人员能够以更低的成本训练扩散模型。 et.al.|[2405.17403](http://arxiv.org/abs/2405.17403)|**[link](https://github.com/1zeryu/speed)**|
|**2024-05-27**|**RB-Modulation: Training-Free Personalization of Diffusion Models using Stochastic Optimal Control**|我们提出了基于参考的调制（RB调制），这是一种新的即插即用解决方案，用于训练扩散模型的自由个性化。现有的无训练方法在（a）在没有额外的风格或内容文本描述的情况下从参考图像中提取风格，（b）从参考风格图像中不希望的内容泄漏，以及（c）风格和内容的有效组合方面表现出困难。RB调制建立在一种新的随机最优控制器上，其中风格描述符通过终端成本对所需属性进行编码。由此产生的漂移不仅克服了上述困难，而且确保了对参考样式的高保真度，并遵守给定的文本提示。我们还引入了一种基于交叉注意力的特征聚合方案，该方案允许RB调制将内容和风格与参考图像解耦。通过理论论证和经验证据，我们的框架展示了以无需训练的方式对内容和风格的精确提取和控制。此外，我们的方法允许内容和样式的无缝组合，这标志着对外部适配器或ControlNets的依赖性的偏离。 et.al.|[2405.17401](http://arxiv.org/abs/2405.17401)|null|
|**2024-05-27**|**EASI-Tex: Edge-Aware Mesh Texturing from Single Image**|我们提出了一种新的单图像网格纹理化方法，该方法使用具有明智条件的扩散模型，将对象的纹理从单个RGB图像无缝转移到给定的3D网格对象。我们不认为这两个对象属于同一类别，即使它们属于同一类，它们的几何图形和零件比例也可能存在显著差异。我们的方法旨在通过调节预训练的稳定扩散生成器来纠正差异，该生成器具有通过ControlNet描述网格的边缘，以及使用IP适配器从输入图像中提取的特征，以生成尊重网格底层几何结构和输入纹理的纹理，而无需任何优化或训练。我们还介绍了图像反转，这是一种使用单个图像快速个性化单个概念的扩散模型的新技术，用于预训练的IP适配器无法忠实地捕捉输入图像中的所有细节的情况。实验结果证明了我们的边缘感知单图像网格纹理方法的效率和有效性，该方法被称为EASI-Tex，在尊重不同3D对象的几何结构的同时，保留了输入纹理的细节。 et.al.|[2405.17393](http://arxiv.org/abs/2405.17393)|null|
|**2024-05-28**|**Global existence, fast signal diffusion limit, and $L^\infty$-in-time convergence rates in a competitive chemotaxis system**|我们研究了一个趋化系统，该系统在二维域中包括两个竞争性猎物和一个捕食者物种，其中猎物（即捕食者）的运动由捕食者（即猎物）分泌的化学物质驱动，称为相互排斥（即相互吸引）趋化效应。所有物种的动力学都是根据猎物的竞争Lotka-Volterra方程和捕食者的Holling型函数反应来选择的。在与生物学相关的情况下，即化学物质的扩散速度远快于所有物种的个体扩散速度，并且适当的重新缩放，化学物质浓度的方程是抛物线型的，系数为$0<\varepsilon\ll 1$。在第一个主要结果中，我们证明了对于每个$\varepsilon$，系统的唯一经典解的全局存在性。其次，我们严格研究了所谓的快速信号扩散极限，从包含缓慢演化的抛物型方程的系统传递到包含所有化学浓度椭圆方程的系统，即$\varepsilon\到0$的极限。这就解释了为什么可以提出用于化学浓度的椭圆方程，而不是具有缓慢演化的抛物方程。第三，估计了快速信号扩散极限的$L^\infty$ -时间收敛速度，其中仔细处理了初始层的影响。最后，通过数值模拟讨论了有和没有缓慢进化的系统之间的差异，以及有一只或两只猎物的系统之间。 et.al.|[2405.17392](http://arxiv.org/abs/2405.17392)|null|
|**2024-05-27**|**Supernova Remnants in Gamma Rays**|在20世纪60年代，超新星爆炸（SNR）的残余物被认为是通过扩散冲击加速（DSA）机制产生银河系宇宙射线的可能来源。从那时起，观测这些物体中相对论离子的伽马射线发射一直是高能天体物理学的主要目标之一。在过去的二十年里，已经在GeV和TeV光子能量下探测到几十个SNR。然而，这些观察结果显示了一种复杂的现象学，不容易简化为基于DSA加速度的标准范式。尽管人们对这些天体的了解大大增加，并且已经观察到它们作为高效电子和质子加速器的性质，但这些天体是否是银河系宇宙射线的主要贡献者仍有待澄清。在这里，我们回顾了SNR对｛\gamma｝射线发射的观测结果以及对未来的展望。 et.al.|[2405.17384](http://arxiv.org/abs/2405.17384)|null|
|**2024-05-27**|**Muon spin relaxation in mixed perovskite (LaAlO $_3$)$_{x}$(SrAl$_{0.5}$Ta$_{0.5}$O$_3$)$_{1-x}$ with $x\simeq 0.3$**|我们报道了混合钙钛矿化合物（LaAlO$_3$）$_{x}$（SrAl$_{0.5}$Ta$_{0.5}$O$_3$）$_｛1-x｝$中μ介子自旋弛豫（$\mu^+$SR）的测量，该化合物被广泛用作薄膜沉积的单晶衬底。在零外加场（ZF）中，在4 K至270 K的温度范围内观察到由于核偶极子场分布引起的μ介子去极化。有趣的是，ZF中的$\mu^+$ SR时间谱在整个范围内保持类高斯特征，而去极化率随着温度的升高而单调下降。这种行为可以归因于μ介子在埃尺度的有限空间内的几个相邻位置之间的热激活扩散，其中每个μ介子经历的运动平均局部场可以保持非零，并导致维持类高斯线形。通过密度泛函理论计算评估的晶格间隙处静电势的空间分布表明，μ介子扩散路径的这种限制可能是由混合钙钛矿晶格中具有不同标称价态的阳离子的随机分布引起的。 et.al.|[2405.17371](http://arxiv.org/abs/2405.17371)|null|
|**2024-05-27**|**Finite Fractal Dimension of uniform attractors for non-autonomous dynamical systems with infinite dimensional symbol space**|本文的目的是找到非自治动力系统一致吸引子的盒计数维数的一个上界。与文献中的结果相反，我们并不要求符号空间具有有限的盒计数维数。相反，我们提出了一个条件，即当时间变为无穷大时，系统的回调吸引子的半连续性。如果我们假设极限符号存在有限维指数一致吸引子，则可以实现这种半连续性。在给出这些新结果后，我们将它们应用于研究反应扩散方程的一致吸引子的盒计数维数，并找到了一个特定的强迫项，使得符号空间具有无限的盒计数维，但一致吸引子无论如何都具有有限的盒计数维度。 et.al.|[2405.17367](http://arxiv.org/abs/2405.17367)|null|
|**2024-05-27**|**Emergent time crystal from a fractional Langevin equation with white and colored noise**|我们使用分析和数值方法研究了与白色和彩色热浴耦合的系统的分数阶Langevin方程和线性摩擦项。我们使用Prabhakar-Mittag-Lefler函数找到了系统的位置和均方位移（MSD）的解析表达式。MSD表现出由彩色噪声驱动的长期亚扩散状态 $t^{\alpha}$和由白噪声驱动的$t^｛2\alpha-1｝$。当忽略线性摩擦时，小分数阶$\alpha\lesssim 0.1$会出现周期有序相。特别是，仅由有色噪声驱动的零线性摩擦系统表现出时间晶体的性质，基态满足波动耗散定理，周期性与$2\pi$成比例。另一方面，仅由白噪声驱动的零线性摩擦系统显示出不平衡的时间玻璃相，其周期性与$\pi$成比例。当系统耦合到两个浴时，会遇到一个混合相，该混合相的贡献来自基态和非平衡态。在这种情况下，由于阻尼效应，周期性偏离$2\pi$ 。我们通过实现离散递归表达式对所有分析结果进行了数值测试，其中系统的随机力被建模为分数布朗运动的导数。Calderira-Leggett模型的扩展也为该系统提供了微观描述。 et.al.|[2405.17331](http://arxiv.org/abs/2405.17331)|null|

<p align=right>(<a href=#updated-on-20240529>back to top</a>)</p>

## NeRF

|Publish Date|Title|Abstract|PDF|Code|
|---|---|---|---|---|
|**2024-05-27**|**Extreme Compression of Adaptive Neural Images**|隐式神经表示（INRs）和神经场是一种新的信号表示范式，从图像和音频到3D场景和视频。其基本思想是将信号表示为连续且可微分的神经网络。这一思想提供了前所未有的优势，如连续分辨率和存储效率，从而实现了新的压缩技术。然而，将数据表示为神经网络带来了新的挑战。例如，给定一个2D图像作为神经网络，我们如何进一步压缩这样的神经图像？。在这项工作中，我们提出了一种新的压缩神经场的分析，重点是图像。我们还介绍了自适应神经图像（ANI），这是一种有效的神经表示，能够适应不同的推理或传输要求。我们提出的方法可以将神经图像的每像素比特数（bpp）减少4倍，而不会丢失敏感细节或损害保真度。我们之所以能做到这一点，是因为我们成功地实现了4位神经表示。我们的工作为开发压缩神经场提供了一个新的框架。 et.al.|[2405.16807](http://arxiv.org/abs/2405.16807)|null|
|**2024-05-24**|**Blaze3DM: Marry Triplane Representation with Diffusion for 3D Medical Inverse Problem Solving**|解决图像恢复和重建等三维医学逆问题在现代医学领域至关重要。然而，3D医疗数据中的维度诅咒导致主流的体积方法遭受高资源消耗，并挑战模型成功捕捉自然分布，导致不可避免的体积不一致和伪影。最近的一些工作试图简化潜在空间中的生成，但缺乏对复杂图像细节进行有效建模的能力。为了解决这些局限性，我们提出了Blaze3DM，这是一种新的方法，通过集成紧凑的三平面神经场和强大的扩散模型，实现了快速高保真的生成。在技术上，Blaze3DM首先同时优化数据相关的三平面嵌入和共享解码器，将每个三平面重建回相应的3D体积。为了进一步增强3D一致性，我们引入了一个轻量级的3D感知模块来对三个垂直平面的相关性进行建模。然后，在潜在的三平面嵌入上训练扩散模型，并实现无条件和有条件的三平面生成，最终解码为任意大小的体积。对零样本三维医学逆问题求解的大量实验，包括稀疏视图CT、有限角度CT、压缩传感MRI和MRI各向同性超分辨率，表明Blaze3DM不仅实现了最先进的性能，而且显著提高了现有方法的计算效率（比以前的工作快22~40倍）。 et.al.|[2405.15241](http://arxiv.org/abs/2405.15241)|null|
|**2024-05-17**|**SNF-ROM: Projection-based nonlinear reduced order modeling with smooth neural fields**|降阶建模通过从数据中学习低阶空间表示并使用控制方程的流形投影动态演化这些表示，降低了求解偏微分方程的计算成本。虽然通常使用线性子空间降阶模型（ROM），但对于Kolmogorov $n$ -宽度缓慢衰减的问题，例如高雷诺数下以平流为主的流体流动，通常是次优的。人们对非线性ROM越来越感兴趣，它使用最先进的表示学习技术以较少的自由度准确地捕捉这种现象。我们提出了光滑神经场ROM（SNF-ROM），这是一种将无网格简化表示与Galerkin投影相结合的非线性简化建模框架。SNF-ROM体系结构将学习到的ROM轨迹约束为平滑变化的路径，这在根据支配PDE遍历简化流形时的动力学评估中是有益的。此外，我们设计了鲁棒正则化方案，以确保学习的神经场是光滑和可微的。这使我们能够使用自动微分来非侵入地计算简化系统的基于物理的动力学，并使用经典时间积分器来演化简化系统。SNF-ROM可以实现快速的离线训练，并提高在线动力学评估的准确性和稳定性。我们证明了SNF-ROM在一系列平流主导的线性和非线性PDE问题上的有效性，在这些问题上，我们始终优于最先进的ROM。 et.al.|[2405.14890](http://arxiv.org/abs/2405.14890)|null|
|**2024-05-23**|**NeuroGauss4D-PCI: 4D Neural Fields and Gaussian Deformation Fields for Point Cloud Interpolation**|点云插值面临着点稀疏性、复杂的时空动力学以及从稀疏的时间信息中导出完整的三维点云的困难等挑战。本文介绍了NeuroGauss4D PCI，它擅长在各种动态场景中建模复杂的非刚性变形。该方法从迭代高斯云软聚类模块开始，提供结构化的时间点云表示。所提出的时间径向基函数高斯残差利用高斯参数随时间插值，实现平滑的参数转换并捕获高斯分布的时间残差。此外，4D高斯变形场跟踪这些参数的演变，创建连续的时空变形场。4D神经场将低维时空坐标（ $x，y，z，t$ ）转换为高维潜在空间。最后，我们自适应有效地融合了来自神经场的潜在特征和来自高斯变形场的几何特征。NeuroGauss4D PCI在点云帧插值方面优于现有方法，在对象级（DHB）和大规模自动驾驶数据集（NL Drive）上都提供了领先的性能，并可扩展到自动标记和点云加密任务。源代码发布于https://github.com/jiangchaokang/NeuroGauss4D-PCI. et.al.|[2405.14241](http://arxiv.org/abs/2405.14241)|null|
|**2024-05-23**|**Multi-view Remote Sensing Image Segmentation With SAM priors**|遥感中的多视图分割（RS）寻求从场景内的不同视角对图像进行分割。最近的方法利用了从隐式神经场（INF）中提取的3D信息，增强了多个视图的结果一致性，同时使用有限的标签（甚至在3-5个标签内）来简化劳动力。尽管如此，由于不充分的全场景监督和INF中不充分的语义特征，在有限视图标签的约束下实现卓越性能仍然具有挑战性。我们建议将视觉基础模型Segment Anything（SAM）的先验注入INF，以在有限的训练数据下获得更好的结果。具体而言，我们对比测试视图和训练视图之间的SAM特征，以导出每个测试视图的伪标签，增强场景范围的标签信息。随后，我们通过转换器将SAM特征引入场景的INF中，补充语义信息。实验结果表明，我们的方法优于主流方法，证实了SAM作为INF的补充对该任务的有效性。 et.al.|[2405.14171](http://arxiv.org/abs/2405.14171)|null|
|**2024-05-22**|**Bridging Operator Learning and Conditioned Neural Fields: A Unifying Perspective**|算子学习是机器学习的一个新兴领域，旨在学习无穷维函数空间之间的映射。在这里，我们从计算机视觉中揭示了算子学习架构和条件神经场之间的联系，为研究流行的算子学习模型之间的差异提供了一个统一的视角。我们发现，许多常用的算子学习模型可以被视为神经场，其条件机制仅限于点和/或全局信息。受此启发，我们提出了连续视觉转换器（CViT），这是一种新的神经算子架构，它使用视觉转换器编码器，并使用交叉注意力来调制由可训练的基于网格的查询坐标位置编码构建的基场。尽管它很简单，但CViT在气候建模和流体动力学的挑战性基准中取得了最先进的结果。我们的贡献可以被视为在物理科学中适应先进的计算机视觉架构以构建更灵活、更准确的机器学习模型的第一步。 et.al.|[2405.13998](http://arxiv.org/abs/2405.13998)|**[link](https://github.com/predictiveintelligencelab/cvit)**|
|**2024-05-21**|**Unsupervised Searches for Cosmological Parity Violation: Improving Detection Power with the Neural Field Scattering Transform**|最近使用四点相关性的研究表明，星系分布中存在宇称破坏，尽管这些探测的重要性对用于模拟星系分布噪声特性的模拟的选择很敏感。在最近的一篇论文中，我们介绍了一种无监督学习方法，该方法提供了一种替代方法，通过直接从观测数据中学习奇偶性违反，避免了对模拟目录的依赖。然而，我们以前的无监督方法所使用的卷积神经网络（CNN）模型很难扩展到数据有限的更现实的场景。我们提出了一种新的方法，即神经场散射变换（NFST），它通过添加可训练滤波器来增强小波散射变换（WST）技术，该滤波器被参数化为神经场。我们首先调整NFST模型，以在简化的数据集中检测奇偶校验违规，然后在不同的训练集大小下，将其性能与WST和CNN基准进行比较。我们发现，NFST可以检测奇偶校验违规，数据比CNN少4倍，比WST少32倍。此外，在数据有限的情况下，NFST可以检测到高达 $6\sigma$ 置信度的奇偶校验违规，其中WST和CNN无法进行任何检测。我们发现，与基准模型相比，NFST增加的灵活性，特别是学习不对称滤波器的能力，以及NFST架构中内置的特定对称性，有助于提高其性能。我们进一步证明了NFST是易于解释的，这对于物理应用（如奇偶校验违反的检测）是有价值的。 et.al.|[2405.13083](http://arxiv.org/abs/2405.13083)|null|
|**2024-05-21**|**Implicit-ARAP: Efficient Handle-Guided Deformation of High-Resolution Meshes and Neural Fields via Local Patch Meshing**|在这项工作中，我们提出了神经符号距离场的局部补丁网格表示。该技术允许通过仅使用SDF信息及其梯度将平面面片网格投影和变形到标高集曲面上来离散输入SDF的标高集的局部区域。我们的分析表明，这种方法比标准的行进立方体算法更准确地逼近隐式曲面。然后，我们将这种表示应用于手柄引导变形的设置：我们引入了两个不同的管道，它们利用3D神经场来计算在给定约束集下高分辨率网格和神经场的“尽可能刚性”变形。我们对我们的方法和神经场和网格变形的各种基线进行了全面评估，结果表明，这两条管道在结果质量和稳健性方面都取得了令人印象深刻的效率和显著的改进。通过我们的新型流水线，我们引入了一种可扩展的方法来解决高分辨率网格上公认的几何处理问题，并为通过局部面片网格将其他几何任务扩展到隐式曲面领域铺平了道路。 et.al.|[2405.12895](http://arxiv.org/abs/2405.12895)|null|
|**2024-05-16**|**Single-shot volumetric fluorescence imaging with neural fields**|与需要在多个轴向平面上扫描的传统成像方法相比，单次体积荧光（SVF）成像提供了显著的优势，因为它可以在大视场上以高时间分辨率捕获生物过程。现有的SVF成像方法通常需要大的、复杂的点扩展函数（PSF）来满足压缩传感的多路复用要求，这限制了信噪比、分辨率和/或视场。在本文中，我们介绍了QuadraPol-PSF与神经场相结合，这是一种新的SVF成像方法。该方法在后焦平面利用成本效益高的定制偏振器和偏振相机来检测荧光，在紧凑的PSF内有效地编码3D场景，而没有深度模糊。此外，我们提出了一种基于神经场技术的重建算法，该算法解决了用于校正成像系统像差的相位检索方法的不精确性。该算法将实验PSF的准确性与计算生成的检索PSF的长景深相结合。QuadraPol PSF与神经场相结合，可将传统荧光显微镜的采集时间显著缩短约20倍，并可一次性捕获100 mm $^3$ 立方体积。我们通过对沙子表面细菌菌落的全聚焦成像和植物根系形态的可视化，验证了我们的硬件和算法的有效性。我们的方法为推进生物学研究和生态学研究提供了强有力的工具。 et.al.|[2405.10463](http://arxiv.org/abs/2405.10463)|null|
|**2024-05-08**|**${M^2D}$NeRF: Multi-Modal Decomposition NeRF with 3D Feature Fields**|神经场（NeRF）已经成为表示连续3D场景的一种很有前途的方法。然而，NeRF中缺乏语义编码对场景分解提出了重大挑战。为了应对这一挑战，我们提出了一个单一的模型，即多模式分解NeRF（${M^2D}$ NeRF），它能够进行基于文本和基于视觉补丁的编辑。具体来说，我们使用多模态特征提取将来自预训练的视觉和语言模型的教师特征集成到3D语义特征体积中，从而促进一致的3D编辑。为了增强三维特征体积中视觉特征和语言特征之间的一致性，我们引入了多模态相似性约束。我们还引入了一种基于补丁的联合对比损失，这有助于鼓励对象区域在3D特征空间中合并，从而产生更精确的边界。与先前的基于NeRF的方法相比，在各种真实世界场景上的实验显示出在3D场景分解任务中的优越性能。 et.al.|[2405.05010](http://arxiv.org/abs/2405.05010)|null|

<p align=right>(<a href=#updated-on-20240529>back to top</a>)</p>

[contributors-shield]: https://img.shields.io/github/contributors/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[contributors-url]: https://github.com/Vincentqyw/cv-arxiv-daily/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[forks-url]: https://github.com/Vincentqyw/cv-arxiv-daily/network/members
[stars-shield]: https://img.shields.io/github/stars/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[stars-url]: https://github.com/Vincentqyw/cv-arxiv-daily/stargazers
[issues-shield]: https://img.shields.io/github/issues/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[issues-url]: https://github.com/Vincentqyw/cv-arxiv-daily/issues

