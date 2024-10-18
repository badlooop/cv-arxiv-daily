[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]

## Updated on 2024.10.18
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
|**2024-10-16**|**Triplet: Triangle Patchlet for Mesh-Based Inverse Rendering and Scene Parameters Approximation**|辐射场的最新进展显著改善了新颖的视图合成。然而，在许多现实世界的应用中，更高级的挑战在于逆渲染，它试图推导场景的物理属性，包括光、几何、纹理和材质。然而，网格作为许多模拟管道采用的传统表示方法，在逆渲染的辐射场中仍然显示出有限的影响。本文介绍了一种名为三角形补丁（缩写为Triplet）的新框架，这是一种基于网格的表示方法，可以全面近似这些场景参数。我们首先用随机生成的点或从相机校准中获得的稀疏点组装三元组，其中所有人脸都被视为一个独立的元素。接下来，我们模拟光的物理交互，并使用光栅化和光线跟踪等传统图形渲染技术优化场景参数，同时进行密度控制和传播。还提出了一种迭代网格提取过程，在该过程中，我们继续通过基于图的操作对几何形状和材料进行优化。我们还引入了几个监管术语，以便更好地概括材料性能。我们的框架可以在没有统一框架中的光、材料和几何先验的情况下，通过网格精确估计光、材料及几何。实验表明，我们的方法可以在重建高质量几何和精确材料属性的同时实现最先进的视觉质量。 et.al.|[2410.12414](http://arxiv.org/abs/2410.12414)|null|
|**2024-10-16**|**GAN Based Top-Down View Synthesis in Reinforcement Learning Environments**|人类的行为是基于对环境的心理感知。即使环境的所有方面都不可见，人类也有一个内部心理模型，可以将部分可见的场景概括为完全构建和连接的视图。这种内部心理模型使用过去遇到的环境的空间和时间方面的学习抽象表示。强化学习环境中的人工智能也受益于从经验中学习环境的表示。它为代理提供了不直接可见的观点，帮助其做出更好的策略决策。它还可以用于预测环境的未来状态。该项目探索了基于人工智能的第一人称视图观察，使用生成对抗网络（GAN）学习强化学习环境的自上而下视图。自顶向下视图很有用，因为它通过构建整个环境的地图来提供环境的完整概述。它提供有关对象的尺寸和形状以及它们彼此之间的相对位置的信息。最初，当代理只能看到环境的部分观察时，只会生成部分自上而下的视图。当代理通过一组操作探索环境时，生成的自上而下的视图就完成了。这种生成的自上而下的视图可以帮助代理推断出更好的策略决策。该项目的重点是学习强化学习环境的自上而下的视图。它不处理任何强化学习任务。 et.al.|[2410.12372](http://arxiv.org/abs/2410.12372)|null|
|**2024-10-16**|**EG-HumanNeRF: Efficient Generalizable Human NeRF Utilizing Human Prior for Sparse View**|可泛化神经辐射场（NeRF）实现了基于神经的数字人体渲染，而无需对每个场景进行再训练。当与人类先验知识相结合时，即使输入视图稀疏，也可以实现高质量的人类渲染。然而，这些方法的推理仍然很慢，因为需要对每条射线进行大量的神经网络查询来确保渲染质量。此外，遮挡区域通常会出现伪影，尤其是在输入视图稀疏的情况下。为了解决这些问题，我们提出了一种通用的人类NeRF框架，通过广泛利用人类先验知识，实现了稀疏输入视图的高质量和实时渲染。我们采用两阶段采样缩减策略加速渲染：首先在人体几何体周围构建边界网格，以减少采样引导回归的光线样本数量，然后使用较少的引导样本进行体绘制。为了提高渲染质量，特别是在遮挡区域，我们提出了一种遮挡感知注意力机制，从人类先验中提取遮挡信息，然后使用图像空间细化网络来提高渲染质量。此外，对于体绘制，我们采用了符号射线距离函数（SRDF）公式，这使我们能够在每个采样位置提出SRDF损失，以进一步提高渲染质量。我们的实验表明，我们的方法在渲染质量方面优于最先进的方法，并且与速度优先的新型视图合成方法相比，具有竞争力的渲染速度。 et.al.|[2410.12242](http://arxiv.org/abs/2410.12242)|null|
|**2024-10-15**|**SplatPose+: Real-time Image-Based Pose-Agnostic 3D Anomaly Detection**|基于图像的姿态不可知三维异常检测是工业质量控制中出现的一项重要任务。该任务旨在在给定一组无异常对象的参考图像的情况下，从测试对象的查询图像中查找异常。挑战在于查询视图（也称为姿势）是未知的，可能与参考视图不同。目前，已经出现了OmniposeAD和SplatPose等新方法，通过在查询视图中合成伪参考图像进行像素间比较来弥合这一差距。然而，这些方法都不能实时推断，这在大规模生产的工业质量控制中至关重要。因此，我们提出了SplatPose+，它采用了一种混合表示，由用于定位的运动结构（SfM）模型和用于新视图合成的3D高斯散点（3DGS）模型组成。尽管我们提出的管道需要计算额外的SfM模型，但与SplatPose相比，它提供了实时推理速度和更快的训练。在质量方面，我们利用多姿态异常检测（MAD-SIM）数据集在姿态无关异常检测基准上实现了新的SOTA。 et.al.|[2410.12080](http://arxiv.org/abs/2410.12080)|null|
|**2024-10-15**|**LoGS: Visual Localization via Gaussian Splatting with Fewer Training Images**|视觉定位涉及估计查询图像的6-DoF（自由度）相机姿态，这是各种计算机视觉和机器人任务中的基本组成部分。本文介绍了LoGS，这是一种基于视觉的定位流水线，利用3D高斯散点（GS）技术作为场景表示。这种新颖的表示允许高质量的新颖视图合成。在映射阶段，首先应用运动结构（SfM），然后生成GS图。在定位过程中，通过图像检索、局部特征匹配和PnP求解器获得初始位置，然后在GS地图上通过综合分析的方式实现高精度姿态。在四个大规模数据集上的实验结果证明了所提出的方法在估计相机姿态方面的SoTA准确性和在具有挑战性的少镜头条件下的鲁棒性。 et.al.|[2410.11505](http://arxiv.org/abs/2410.11505)|null|
|**2024-10-15**|**GS^3: Efficient Relighting with Triple Gaussian Splatting**|我们提出了一种基于空间和角度高斯的表示和三重叠加过程，用于从多视点照明输入图像中实时、高质量地进行新颖的照明和视图合成。为了描述复杂的外观，我们采用朗伯加角高斯混合作为每个空间高斯的有效反射函数。为了生成自阴影，我们将所有空间高斯分布向光源投射以获得阴影值，这些值由一个小型多层感知器进一步细化。为了补偿全局照明等其他影响，训练另一个网络来计算并添加每个空间的高斯RGB元组。我们的表示方法的有效性在30个几何形状（从实心到蓬松）和外观（从半透明到各向异性）变化很大的样本上得到了证明，并使用了不同形式的输入数据，包括合成/重建物体的渲染图像、用手持相机和闪光灯拍摄的照片，或来自专业光台的照片。我们在单个商品GPU上实现了40-70分钟的训练时间和90 fps的渲染速度。我们的结果在质量/性能方面与最先进的技术相比毫不逊色。我们的代码和数据可在以下网址公开获取https://GSrelight.github.io/. et.al.|[2410.11419](http://arxiv.org/abs/2410.11419)|**[link](https://github.com/gsrelight/gs-relight)**|
|**2024-10-15**|**MCGS: Multiview Consistency Enhancement for Sparse-View 3D Gaussian Radiance Fields**|由3D高斯表示的辐射场擅长合成新颖的视图，提供了高训练效率和快速渲染。然而，在稀疏输入视图的情况下，缺乏多视图一致性约束会导致点云初始化不佳，优化和致密化的启发式方法不可靠，从而导致性能不佳。现有的方法通常包含来自密集估计网络的深度先验，但忽略了输入图像中固有的多视图一致性。此外，它们依赖于基于多视图立体（MVS）的初始化，这限制了场景表示的效率。为了克服这些挑战，我们提出了一种基于3D高斯散斑的视图合成框架，称为MCGS，能够从稀疏输入视图中重建出逼真的场景。MCGS在增强多视图一致性方面的关键创新如下：i）我们引入了一种初始化方法，该方法利用稀疏匹配器结合随机填充策略，产生了一组紧凑但足够的初始点。这种方法增强了初始几何先验，促进了高效的场景表示。ii）我们开发了一种多视图一致性引导的渐进修剪策略，通过增强一致性和消除低贡献高斯分布来细化高斯场。这些模块化的即插即用策略增强了对稀疏输入视图的鲁棒性，加速了渲染，减少了内存消耗，使MCGS成为3D高斯散斑的实用高效框架。 et.al.|[2410.11394](http://arxiv.org/abs/2410.11394)|null|
|**2024-10-15**|**Scalable Indoor Novel-View Synthesis using Drone-Captured 360 Imagery with 3D Gaussian Splatting**|对于大型、复杂、多层的室内场景，场景重建和新颖的视图合成是一项具有挑战性和耗时的任务。先前的方法利用无人机进行数据采集，利用辐射场进行场景重建，这两种方法都存在一定的挑战。首先，为了用无人机的前置摄像头捕捉不同的视角，一些方法以不稳定的锯齿形方式飞行无人机，这阻碍了无人机的驾驶，并在捕获的数据中产生了运动模糊。其次，大多数辐射场方法不容易扩展到任意数量的图像。本文提出了一种高效且可扩展的管道，用于使用3D高斯散斑从无人机捕获的360度视频中合成室内新颖的视图。360度摄像头可以捕捉到广泛的视点，从而在简单直接的无人机轨迹下进行全面的场景捕捉。为了将我们的方法扩展到大型场景，我们设计了一种分而治之的策略，将场景自动分割成可以单独和并行重建的较小块。我们还提出了一种从粗到细的对齐策略，将这些块无缝匹配在一起，组成整个场景。我们的实验表明，与现有方法相比，重建质量（即PSNR和SSIM）和计算时间都有显著提高。 et.al.|[2410.11285](http://arxiv.org/abs/2410.11285)|null|
|**2024-10-14**|**Few-shot Novel View Synthesis using Depth Aware 3D Gaussian Splatting**|3D高斯溅射在新颖的视图合成中已经超越了神经辐射场方法，实现了更低的计算成本和实时高质量的渲染。虽然它可以在大量输入视图的情况下产生高质量的绘制，但当只有少数视图可用时，其性能会显著下降。在这项工作中，我们通过提出一种用于少镜头新颖视图合成的深度感知高斯飞溅方法来解决这个问题。我们使用单目深度预测作为先验，并结合尺度不变的深度损失，在少数输入视图下约束3D形状。我们还使用低阶球谐函数对颜色进行建模，以避免过拟合。此外，我们观察到，像在原始作品中那样，定期删除不透明度较低的斑点会导致点云非常稀疏，从而降低渲染质量。为了减轻这种情况，我们保留了所有斑点，从而在一些视图设置中实现了更好的重建。实验结果表明，我们的方法在峰值信噪比、结构相似性指数和感知相似性方面分别提高了10.5%、6%和14.1%，优于传统的3D高斯飞溅方法，从而验证了我们方法的有效性。该代码将在以下网址提供：https://github.com/raja-kumar/depth-aware-3DGS et.al.|[2410.11080](http://arxiv.org/abs/2410.11080)|**[link](https://github.com/raja-kumar/depth-aware-3dgs)**|
|**2024-10-14**|**FlexGen: Flexible Multi-View Generation from Text and Image Inputs**|在这项工作中，我们介绍了FlexGen，这是一个灵活的框架，旨在生成可控和一致的多视图图像，以单个视图图像或文本提示为条件，或两者兼而有之。FlexGen通过对3D感知文本注释进行额外调节，解决了可控多视图合成的挑战。我们利用GPT-4V的强大推理能力来生成3D感知文本注释。通过分析作为平铺多视图图像排列的对象的四个正交视图，GPT-4V可以生成包含具有空间关系的3D感知信息的文本注释。通过将控制信号与所提出的自适应双控制模块集成，我们的模型可以生成与指定文本相对应的多视图图像。FlexGen支持多种可控功能，允许用户修改文本提示以生成合理且相应的看不见的部分。此外，用户可以影响外观和材料属性等属性，包括金属和粗糙度。大量实验表明，我们的方法提供了增强的多重可控性，标志着比现有多视图扩散模型的重大进步。这项工作对需要快速灵活的3D内容创建的领域具有重大意义，包括游戏开发、动画和虚拟现实。项目页面：https://xxu068.github.io/flexgen.github.io/. et.al.|[2410.10745](http://arxiv.org/abs/2410.10745)|null|

<p align=right>(<a href=#updated-on-20241018>back to top</a>)</p>

## 3D Reconstruction

|Publish Date|Title|Abstract|PDF|Code|
|---|---|---|---|---|
|**2024-10-16**|**Cascade learning in multi-task encoder-decoder networks for concurrent bone segmentation and glenohumeral joint assessment in shoulder CT scans**|骨关节炎是一种影响骨骼和软骨的退行性疾病，通常导致骨赘形成、骨密度降低和关节间隙狭窄。恢复正常关节功能的治疗方案因病情的严重程度而异。这项工作引入了一种处理肩部CT扫描的创新深度学习框架。它具有肱骨近端和肩胛骨的语义分割、骨表面的3D重建、肩关节（GH）关节区域的识别以及三种常见骨关节炎相关病理的分期：骨赘形成（OS）、GH间隙缩小（JS）和肱骨肩胛骨对齐（HSA）。该流水线包括两个级联的CNN架构：用于分割的3D CEL-UNet和用于三重分类的3D Arthro-Net。使用571次CT扫描的回顾性数据集，对患有不同程度GH骨关节炎相关疾病的患者进行训练、验证和测试。肱骨三维重建的均方根误差和豪斯多夫距离中值分别为0.22mm和1.48mm，肩胛骨为0.24mm和1.48mm。其性能优于最先进的架构，可能适用于基于PSI的肩关节置换术前计划。OS、JS和HSA在所有三个类别中的分类准确率始终达到90%左右。推理管道的计算时间不到15秒，展示了该框架的效率和与骨科放射学实践的兼容性。这些结果代表了人工智能工具在医学翻译方面的一个有前景的进步。这一进展旨在简化术前计划流程，提供高质量的骨表面，并支持外科医生根据独特的患者关节状况选择最合适的手术方法。 et.al.|[2410.12641](http://arxiv.org/abs/2410.12641)|null|
|**2024-10-15**|**Stochastic 3D reconstruction of cracked polycrystalline NMC particles using 2D SEM data**|锂离子电池的性能受到其阴极性能的强烈影响，因此也受到阴极所含颗粒的3D微观结构的影响。在压延和循环过程中，阴极颗粒内会产生裂纹，这可能会以多种方式影响性能。一方面，裂纹降低了内部连接性，从而阻碍了阴极粒子内的电子传输。另一方面，颗粒内裂纹可以增加阴极反应表面。由于这些相互矛盾的影响，有必要定量研究电池循环如何影响开裂，以及开裂又如何影响电池性能。因此，有必要用结构描述符表征3D颗粒形态，并将其与有效电池性能定量关联。通常，使用图像数据进行3D结构表征。然而，信息丰富的3D成像技术耗时、昂贵且很少可用，因此分析通常必须依赖于2D图像数据。本文提出了一种新的体视学方法，用于生成虚拟3D阴极粒子，这些粒子表现出与实验测量粒子的2D截面中观察到的裂纹网络在统计上等效的裂纹网络。因此，更容易获得的2D图像数据足以得出破裂阴极颗粒的完整3D特征。在未来的研究中，虚拟生成的3D粒子将被用作空间分辨电化学机械模拟的几何输入，以加深我们对锂离子电池阴极结构-性能关系的理解。 et.al.|[2410.12020](http://arxiv.org/abs/2410.12020)|null|
|**2024-10-15**|**Robotic Arm Platform for Multi-View Image Acquisition and 3D Reconstruction in Minimally Invasive Surgery**|微创手术（MIS）具有显著的优势，如缩短恢复时间和最大限度地减少患者创伤，但在可见性和可及性方面存在挑战，使精确的3D重建成为手术规划和导航的重要工具。这项工作介绍了一种机器人手臂平台，用于在MIS环境中进行高效的多视图图像采集和精确的3D重建。我们将腹腔镜改装成机器人手臂，并在不同的照明条件（手术室和腹腔镜）和轨迹（球形和腹腔镜）下捕获了几个绵羊器官的离体图像。我们采用了最近发布的基于学习的特征匹配器与COLMAP相结合来生成我们的重建。通过高精度激光扫描对重建进行定量评估。我们的结果表明，虽然重建在真实的MIS照明和轨迹下遭受的损失最大，但我们的管道的许多版本都达到了接近亚毫米的精度，平均均方根误差为1.05毫米，倒角距离为0.82毫米。我们最好的重建结果发生在手术室照明和球形轨迹上。我们的机器人平台为MIS环境中的3D生成提供了一种受控、可重复的多视图数据采集工具，我们希望这能为训练基于学习的模型带来新的数据集。 et.al.|[2410.11703](http://arxiv.org/abs/2410.11703)|null|
|**2024-10-15**|**Simultaneous Diffusion Sampling for Conditional LiDAR Generation**|通过捕获反映周围环境几何形状的3D点云，LiDAR已成为自主系统的主要传感器。如果激光雷达扫描太稀疏、被障碍物遮挡或范围太小，在尊重场景几何形状的同时增强点云扫描对下游任务很有用。在视觉生成方法兴趣爆炸式增长的推动下，条件激光雷达生成开始兴起。本文提出了一种新的同时扩散采样方法，用于生成基于多视角场景三维结构的点云。关键思想是对生成过程施加多视图几何约束，利用互信息来增强结果。我们的方法首先将输入扫描重新转换为扫描周围的多个新视点，从而创建多个合成激光雷达扫描。然后，根据我们的方法，合成和输入的激光雷达扫描同时进行条件生成。结果表明，我们的方法可以对点云扫描产生准确和几何一致的增强，使其在各种基准测试中大大优于现有方法。 et.al.|[2410.11628](http://arxiv.org/abs/2410.11628)|null|
|**2024-10-16**|**Depth Estimation From Monocular Images With Enhanced Encoder-Decoder Architecture**|由于需要通常提供深度信息的立体或多视图数据，因此从单个2D图像估计深度是一项具有挑战性的任务。本文通过引入一种使用编码器-解码器架构的基于深度学习的新方法来应对这一挑战，其中Inception-ResNet-v2模型被用作编码器。根据现有文献，这是首次使用Inception-ResNet-v2作为单目深度估计的编码器，表明其性能优于之前的模型。Inception-ResNet-v2的使用使我们的模型能够有效地捕获通常难以预测的复杂对象和细粒度细节。此外，我们的模型结合了多尺度特征提取，以提高不同类型对象大小和距离的深度预测精度。我们提出了一种由深度损失、梯度边缘损失和SSIM损失组成的复合损失函数，其中对权重进行微调以优化加权和，确保深度估计不同方面的更好平衡。纽约大学深度V2数据集的实验结果表明，我们的模型达到了最先进的性能，ARE为0.064，RMSE为0.228，准确率（ $\delta$<1.25$ ）为89.3%。这些指标表明，即使在具有挑战性的情况下，我们的模型也能有效地预测深度，为机器人、3D重建和增强现实等现实世界的应用提供可扩展的解决方案。 et.al.|[2410.11610](http://arxiv.org/abs/2410.11610)|null|
|**2024-10-15**|**Multiview Scene Graph**|适当的场景表示是追求空间智能的核心，智能体可以稳健地重建并有效地理解3D场景。场景表示可以是度量，如3D重建中的地标图、对象检测中的3D边界框或占用预测中的体素网格，也可以是拓扑，如SLAM中具有循环闭包的姿态图或SfM中的可见性图。在这项工作中，我们建议从未涂胶的图像构建多视图场景图（MSG），用互连的位置和对象节点在拓扑上表示场景。构建MSG的任务对现有的表示学习方法来说是具有挑战性的，因为它需要联合解决视觉位置识别、对象检测和来自视野有限和潜在大视点变化的图像的对象关联问题。为了评估任何解决这一任务的方法，我们开发了一个基于公共3D数据集的MSG数据集和注释。我们还提出了一种基于MSG边联合得分交集的评估度量。此外，我们开发了一种基于主流预训练视觉模型的新基线方法，将视觉位置识别和对象关联结合到一个Transformer解码器架构中。实验证明，与现有的相关基线相比，我们的方法具有更优的性能。 et.al.|[2410.11187](http://arxiv.org/abs/2410.11187)|null|
|**2024-10-14**|**Cultural Heritage 3D Reconstruction with Diffusion Networks**|本文探讨了使用最新的生成式人工智能算法修复文化遗产，利用一个旨在有效重建3D点云的条件扩散模型。我们的研究评估了该模型在一般和文化遗产特定环境中的表现。结果表明，在考虑对象变异性的情况下，扩散模型可以准确地再现文化遗产的几何形状。尽管遇到了数据多样性和异常敏感性等挑战，但该模型在伪影恢复研究中显示出巨大的潜力。这项工作为使用人工智能技术推进古代文物的修复方法奠定了基础。 et.al.|[2410.10927](http://arxiv.org/abs/2410.10927)|**[link](https://github.com/PJaramilloV/pcdiff-method)**|
|**2024-10-14**|**3DArticCyclists: Generating Simulated Dynamic 3D Cyclists for Human-Object Interaction (HOI) and Autonomous Driving Applications**|人机交互（HOI）和人场景交互（HSI）对于体现人工智能（EAI）、机器人和增强现实（AR）中以人为中心的场景理解应用至关重要。这些研究领域面临的一个共同限制是数据稀缺问题：输入图像上标记的人类场景对象对不足，它们之间的交互复杂性和粒度有限。最近的HOI和HSI方法通过生成与刚性对象的动态交互来解决这个问题。但更复杂的动态交互，如人类骑手踩着铰接式自行车，尚未得到探索。为了解决这一局限性，并能够研究复杂的动态人体关节对象交互，本文提出了一种生成模拟的3D动态自行车手资产和交互的方法。我们设计了一种方法，用于创建一个新的基于零件的多视图铰接合成3D自行车数据集，我们称之为3DArticBikes，可用于训练基于NeRF和3DGS的3D重建方法。然后，我们提出了一种基于3DGS的参数化自行车组合模型，用于组装8自由度姿态可控的3D自行车。最后，使用来自骑车人视频的动态信息，我们通过重新设置一个可选择的合成3D人的姿势，同时使用提出的基于3D关键点优化的逆运动学姿势细化将骑车人自动放置在我们新的铰接式3D自行车上，从而构建一个完整的合成动态3D骑车人（骑自行车的骑车人）。我们展示了定性和定量结果，将我们生成的自行车与最近稳定的基于扩散的方法生成的自行车进行了比较。 et.al.|[2410.10782](http://arxiv.org/abs/2410.10782)|null|
|**2024-10-13**|**Magnituder Layers for Implicit Neural Representations in 3D**|提高3D中隐式神经表示的效率和性能，特别是神经辐射场（NeRF）和有符号距离场（SDF），对于在实时应用中使用它们至关重要。这些模型虽然能够生成逼真的新颖视图和详细的3D重建，但往往存在计算成本高和推理速度慢的问题。为了解决这个问题，我们引入了一种名为“magnituder”的新型神经网络层，旨在减少这些模型中的训练参数数量，同时不牺牲其表达能力。通过将放大器集成到标准前馈层堆栈中，我们提高了推理速度和适应性。此外，我们的方法通过无反向传播的分层知识转移，能够提高训练的隐式神经表示模型的零样本性能，从而在动态环境中实现更高效的场景重建。 et.al.|[2410.09771](http://arxiv.org/abs/2410.09771)|null|
|**2024-10-13**|**EchoPrime: A Multi-Video View-Informed Vision-Language Model for Comprehensive Echocardiography Interpretation**|超声心动图是使用最广泛的心脏成像技术，通过捕获超声视频数据来评估心脏的结构和功能。超声心动图中的人工智能（AI）有可能简化手动任务，提高再现性和准确性。然而，大多数超声心动图人工智能模型都是单视图、单任务系统，不能从全面检查期间捕获的多个视图中合成互补信息，从而导致性能和应用范围有限。为了解决这个问题，我们引入了EchoPrime，这是一个多视图、视图知情、基于视频的视觉语言基础模型，在1200多万个视频报告对上进行了训练。EchoPrime使用对比学习为全面的超声心动图研究中的所有标准视图训练一个统一的嵌入模型，同时表示罕见和常见的疾病和诊断。然后，EchoPrime利用视图分类和视图通知的解剖注意力模型来加权视频特定的解释，这些解释准确地映射了超声心动图视图和解剖结构之间的关系。通过检索增强解释，EchoPrime将所有超声心动图视频中的信息整合到一项综合研究中，并进行全面的临床超声心动图解释。在来自两个独立医疗保健系统的数据集中，EchoPrime在23个不同的心脏形态和功能基准上实现了最先进的性能，超过了特定任务方法和先前基础模型的性能。经过严格的临床评估，EchoPrime可以帮助医生对综合超声心动图进行自动化的初步评估。 et.al.|[2410.09704](http://arxiv.org/abs/2410.09704)|**[link](https://github.com/echonet/echoprime)**|

<p align=right>(<a href=#updated-on-20241018>back to top</a>)</p>

## Diffusion

|Publish Date|Title|Abstract|PDF|Code|
|---|---|---|---|---|
|**2024-10-16**|**Meta-Unlearning on Diffusion Models: Preventing Relearning Unlearned Concepts**|随着基于扩散的内容生成的快速发展，人们正在做出重大努力，从预训练的扩散模型（DM）中忘却有害或受版权保护的概念，以防止潜在的模型误用。然而，可以观察到，即使在发布之前正确地学习了DM，恶意的微调也会破坏这一过程，导致DM重新学习未学习的概念。这部分是因为DM中保留的某些良性概念（例如“皮肤”）与未学习的概念（例如，“裸体”）有关，通过微调促进了它们的再学习。为了解决这个问题，我们建议对DM进行元忘却。直观地说，当按原样使用时，元未学习DM的行为应该像未学习DM一样；此外，如果元未学习DM对未学习的概念进行恶意微调，其中保留的相关良性概念将被触发自毁，阻碍未学习概念的再学习。我们的元忘却框架与大多数现有的忘却方法兼容，只需要添加一个易于实现的元目标。我们通过对稳定扩散模型（SD-v1-4和SDXL）的元忘却概念进行实证实验来验证我们的方法，并得到了广泛消融研究的支持。我们的代码可在https://github.com/sail-sg/Meta-Unlearning. et.al.|[2410.12777](http://arxiv.org/abs/2410.12777)|null|
|**2024-10-16**|**Should exponential integrators be used for advection-dominated problems?**|在本文中，我们考虑了指数积分器在平流主导问题中的应用，无论是在整个域上还是在域的一个子集上。在此背景下，我们比较了基于Leja和Krylov的方法来计算指数函数和相关矩阵函数的作用。我们通过计算实现所考虑算法所需的不同操作来建立性能模型。该模型假设右侧的评估是内存受限的，并允许我们以独立于硬件的方式评估性能。我们发现，对于整个域中以平流为主的问题，指数积分器的表现与显式龙格-库塔方案相当。此外，在域的小部分由扩散主导的情况下，它们能够超越显式方法。我们通常观察到，在所考虑的问题中，基于Leja的方法优于Krylov迭代。如果计算内积很昂贵，尤其如此。 et.al.|[2410.12765](http://arxiv.org/abs/2410.12765)|null|
|**2024-10-16**|**SAFREE: Training-Free and Adaptive Guard for Safe Text-to-Image And Video Generation**|扩散模型的最新进展显著提高了它们生成高质量图像和视频的能力，但也增加了产生不安全内容的风险。现有的基于忘却/编辑的安全生成方法可以从模型中删除有害概念，但面临着几个挑战：（1）没有训练，它们无法立即删除有害概念。（2） 它们的安全生成能力取决于收集到的训练数据。（3） 它们改变了模型权重，冒着与有毒概念无关的内容质量下降的风险。为了解决这些问题，我们提出了SAFREE，这是一种新的、无需训练的安全T2I和T2V方法，不会改变模型的权重。具体来说，我们在文本嵌入空间中检测与一组有毒概念相对应的子空间，并引导提示嵌入远离该子空间，从而在保留预期语义的同时过滤掉有害内容。为了平衡过滤毒性和保护安全概念之间的权衡，SAFREE引入了一种新的自验证过滤机制，该机制在应用过滤嵌入时动态调整去噪步骤。此外，我们在扩散潜在空间中引入了自适应再关注机制，以在像素级别选择性地减少与有毒概念相关的特征的影响。最后，SAFREE确保了连贯的安全检查，保持了输出的保真度、质量和安全性。与无训练基线相比，SAFREE在抑制T2I生成中的不安全内容方面实现了SOTA性能，并在保持高质量图像的同时有效地过滤了目标概念。它还显示了与基于训练的方法相比的竞争结果。我们将SAFREE扩展到各种T2I主干和T2V任务，展示了它的灵活性和通用性。SAFREE为确保安全的视觉生成提供了强大且适应性强的保障。 et.al.|[2410.12761](http://arxiv.org/abs/2410.12761)|null|
|**2024-10-16**|**Impact of Ion Mobility on Electron Density and Temperature in Hypersonic Flows**|这项研究首次全面分析了离子迁移率如何影响高超音速流中的电子密度和温度。我们比较了两种离子迁移率模型：一种来自Gupta Yos横截面，另一种来自群漂移速度实验。离子迁移率模型显著改变了高超音速乘波体周围的等离子体密度，在低动压和高马赫数下观察到等离子体密度增加了两倍以上。这部分是由于表面催化导致的电子损失，这取决于双极扩散与离子迁移率的缩放。我们还推导出了新的标度定律，突出了电子冷却对准中性区域和非中性等离子体鞘层内离子迁移率的强烈依赖性。电子冷却会影响整个等离子体的电子温度，从而导致离子迁移率对等离子体本体温度的先前未被认识的影响。这反过来又通过温度依赖的电子-离子复合速率影响等离子体密度。精确模拟离子迁移率对于预测高超音速等离子体行为至关重要，对优化磁流体动力学技术和减轻或利用等离子体对电磁波的干扰具有重要意义。 et.al.|[2410.12760](http://arxiv.org/abs/2410.12760)|null|
|**2024-10-16**|**Signature of Vertical Mixing in Hydrogen-dominated Exoplanet Atmospheres**|垂直混合是系外行星大气中一个至关重要的不平衡过程，对化学丰度和观测光谱有重大影响。虽然目前最先进的观测已经检测到了它的特征，但垂直混合对大气光谱的影响因行星参数而异。在这项研究中，我们探索了不平衡化学在包括涡流扩散、表面重力、内部和平衡温度以及金属性在内的参数空间中的影响。我们还评估了检索模型在约束涡流扩散系数方面的有效性。通过运行众多1D化学动力学模型，我们研究了垂直混合对透射光谱的影响。我们还建立了一个自定义的快速前向不平衡模型，其中包括使用淬灭近似的垂直混合，并比化学动力学模型更快地计算模型丰度数量级。我们将该正向模型与开源大气检索代码耦合，并将其用于我们化学动力学模型的JWST模拟输出数据，并检索到涡流扩散系数、内部温度和大气金属丰度。我们发现，在参数空间中有一个狭窄的区域，垂直混合对大气透射光谱有很大的影响。在参数空间的这一区域，反演模型可以对传输强度施加高度约束，并为研究垂直混合提供最佳的系外行星。此外，NH3丰度可用于约束平衡温度T_equi>1400K的内部温度。 et.al.|[2410.12737](http://arxiv.org/abs/2410.12737)|null|
|**2024-10-16**|**Smooth Geometry of Diffusion Algebras**|本文研究了扩散代数的微分光滑性。 et.al.|[2410.12701](http://arxiv.org/abs/2410.12701)|null|
|**2024-10-16**|**Embedding an Ethical Mind: Aligning Text-to-Image Synthesis via Lightweight Value Optimization**|基于大规模数据训练的扩散模型的最新进展使得生成难以区分的人类水平图像成为可能，但它们往往会产生与人类价值观不符的有害内容，例如社会偏见和冒犯性内容。尽管对大型语言模型（LLM）进行了广泛的研究，但文本到图像（T2I）模型对齐的挑战在很大程度上仍未得到探索。为了解决这个问题，我们提出了LiVO（轻量级价值优化），这是一种新的轻量级方法，用于将T2I模型与人类价值观对齐。LiVO只优化了即插即用值编码器，将指定的值原则与输入提示集成在一起，允许在语义和值上控制生成的图像。具体来说，我们设计了一个定制偏好优化损失的扩散模型，该模型在理论上近似于LLM对齐中使用的Bradley Terry模型，但在图像质量和值一致性之间提供了更灵活的权衡。为了优化值编码器，我们还开发了一个框架来自动构建86k（提示、对齐图像、违规图像、值原则）样本的文本图像偏好数据集。在不更新大多数模型参数的情况下，通过从输入提示中进行自适应值选择，LiVO显著减少了有害输出，实现了更快的收敛，超越了几个强基线，朝着符合伦理的T2I模型迈出了第一步。 et.al.|[2410.12700](http://arxiv.org/abs/2410.12700)|**[link](https://github.com/achernarwang/LiVO)**|
|**2024-10-16**|**AdaptiveDrag: Semantic-Driven Dragging on Diffusion-Based Image Editing**|最近，出现了几种基于点的图像编辑方法（例如DragDiffusion、FreeDrag、DragNoise），根据用户指令产生精确和高质量的结果。然而，这些方法往往没有充分利用语义信息，导致不太理想的结果。在这篇论文中，我们提出了一种新的基于无掩模点的图像编辑方法AdaptiveDrag，它提供了一种更灵活的编辑方法，并生成了更符合用户意图的图像。具体来说，我们设计了一个使用超像素分割的自动掩模生成模块，以方便用户使用。接下来，我们利用预训练的扩散模型来优化潜在特征，使特征能够从处理点拖动到目标点。为了确保输入图像和拖动过程之间的全面联系，我们开发了一种语义驱动的优化方法。我们设计了自适应步骤，这些步骤由点的位置和从超像素分割中导出的语义区域进行监督。这种精细的优化过程也带来了更真实、更准确的阻力结果。此外，为了解决扩散模型生成一致性的局限性，我们在采样过程中引入了一种创新的相应损失。基于这些有效的设计，我们的方法仅使用单个输入图像和手柄目标点对即可提供卓越的生成结果。已经进行了大量的实验，证明所提出的方法在处理不同领域（如动物、人脸、陆地空间、服装）的各种拖动指令（如调整大小、移动、扩展）方面优于其他方法。 et.al.|[2410.12696](http://arxiv.org/abs/2410.12696)|null|
|**2024-10-16**|**Hamiltonian bridge: A physics-driven generative framework for targeted pattern control**|模式在跨越科学的一系列系统中自发出现，他们的研究通常侧重于理解它们在时空中进化的机制。越来越多的人转向在各种功能设置中控制这些模式，这对工程有影响。在这里，我们结合了我们对非平衡系统中模式形成的一类动力学定律的了解，以及随机最优控制方法的力量，提出了一个框架，使我们能够在多个尺度上控制模式，我们称之为“哈密顿桥”。我们使用随机多体拉格朗日物理学和确定性欧拉模式形成偏微分方程之间的映射，利用我们最近的方法，利用基于Feynman-Kac的伴随路径积分公式来控制相互作用粒子，并将其推广到模式场的主动控制。我们通过数值实验证明了我们的计算框架在有和没有守恒序参数的相分离控制、液滴自组装、耦合反应扩散方程以及时空组织分化的唯象模型方面的适用性。我们根据对底层物理如何塑造模式流形几何形状的理论理解来解释我们的数值实验，改变模式的传输路径和模式插值的性质。最后，我们通过展示如何利用最优控制，通过对可转换为梯度流的模式形成偏微分方程的迭代控制协议来生成复杂的模式，从而得出结论。总之，我们的研究表明，我们如何系统地将物理先验构建成一个生成框架，用于跨多个长度和时间尺度的非平衡系统中的模式控制。 et.al.|[2410.12665](http://arxiv.org/abs/2410.12665)|null|
|**2024-10-16**|**Constrained Posterior Sampling: Time Series Generation with Hard Constraints**|生成真实的时间序列样本对于压力测试模型和使用合成数据保护用户隐私至关重要。在工程和安全关键应用中，这些样本必须满足特定领域或物理或自然强加的某些硬约束。例如，考虑在峰值需求时间受到限制的情况下产生电力需求模式。这可用于在恶劣天气条件下对电网的功能进行压力测试。现有的生成约束时间序列的方法要么不可扩展，要么会降低样本质量。为了应对这些挑战，我们引入了约束后验采样（CPS），这是一种基于扩散的采样算法，旨在在每次去噪更新后将后验均值估计投影到约束集中。值得注意的是，CPS可以扩展到大量约束（~100），而不需要额外的培训。我们提供了理论依据，强调了我们的预测步骤对采样的影响。根据经验，在真实世界的股票、交通和空气质量数据集上，CPS在样本质量和与实时序列的相似性方面分别比最先进的方法高出约10%和42%。 et.al.|[2410.12652](http://arxiv.org/abs/2410.12652)|null|

<p align=right>(<a href=#updated-on-20241018>back to top</a>)</p>

## NeRF

|Publish Date|Title|Abstract|PDF|Code|
|---|---|---|---|---|
|**2024-10-15**|**Deep vectorised operators for pulsatile hemodynamics estimation in coronary arteries from a steady-state prior**|心血管血流动力学场为冠状动脉疾病提供了有价值的医学决策标志。计算流体动力学（CFD）是体内准确、无创评估这些量的金标准。在这项工作中，我们提出了一种基于机器学习的时间高效替代模型，用于基于稳态先验估计脉动血流动力学。我们引入了深度矢量化算子，这是一种用于在无限维函数空间上进行离散化独立学习的建模框架。基础神经结构是一个以血流动力学边界条件为条件的神经场。重要的是，我们展示了如何将逐点动作的要求放宽到置换等变，从而产生一系列可以通过消息传递和自我关注层进行参数化的模型。我们在从冠状动脉计算机断层扫描血管造影（CCTA）中提取的74条狭窄冠状动脉的数据集上评估了我们的方法，并将患者特异性脉动CFD模拟作为基本事实。我们证明，我们的模型能够准确估计脉动速度和压力，同时不受源域重新采样的影响（离散化独立性）。这表明，深度矢量化算子是冠状动脉及其他动脉心血管血流动力学估计的强大建模工具。 et.al.|[2410.11920](http://arxiv.org/abs/2410.11920)|null|
|**2024-10-07**|**Fast Training of Sinusoidal Neural Fields via Scaling Initialization**|神经场是一种新兴的范式，它将数据表示为由神经网络参数化的连续函数。尽管有许多优点，但神经场通常具有较高的训练成本，这阻碍了更广泛的采用。在本文中，我们关注一个流行的神经场家族，称为正弦神经场（SNF），并研究如何初始化它以最大限度地提高训练速度。我们发现，基于信号传播原理设计的SNF标准初始化方案是次优的。特别是，我们证明，通过简单地将每个权重（最后一层除外）乘以一个常数，我们可以将SNF训练加速10 $\times$。这种方法被称为$\textit{weight scaling}$ ，在各种数据域上持续提供显著的加速，使SNF的训练速度比最近提出的架构更快。为了理解为什么权重缩放效果良好，我们进行了广泛的理论和实证分析，结果表明，权重缩放不仅有效地解决了频谱偏差，而且具有良好的优化轨迹。 et.al.|[2410.04779](http://arxiv.org/abs/2410.04779)|null|
|**2024-10-04**|**End-to-End Reaction Field Energy Modeling via Deep Learning based Voxel-to-voxel Transform**|在计算生物化学和生物物理学中，理解静电相互作用的作用对于阐明生物分子的结构、动力学和功能至关重要。泊松-玻尔兹曼（PB）方程是通过描述带电分子内部和周围的静电势来模拟这些相互作用的基础工具。然而，由于生物分子表面的复杂性和需要考虑可移动离子，求解PB方程带来了重大的计算挑战。虽然求解PB方程的传统数值方法是准确的，但它们的计算成本很高，并且随着系统规模的增加而扩展性较差。为了应对这些挑战，我们引入了PBNeF，这是一种新的机器学习方法，灵感来自基于神经网络的偏微分方程求解器的最新进展。我们的方法将PB方程的输入和边界静电条件转化为可学习的体素表示，使神经场变换器能够预测PB解，进而预测反应场势能。大量实验表明，与传统的PB求解器相比，PBNeF的速度提高了100倍以上，同时保持了与广义玻恩（GB）模型相当的精度。 et.al.|[2410.03927](http://arxiv.org/abs/2410.03927)|null|
|**2024-10-08**|**DressRecon: Freeform 4D Human Reconstruction from Monocular Video**|我们提出了一种从单目视频中重建时间一致的人体模型的方法，重点是极其宽松的衣服或手持物体的交互。之前在人体重建方面的工作要么局限于没有物体交互的紧身衣服，要么需要校准的多视图捕捉或个性化的模板扫描，而大规模收集这些数据成本很高。我们对高质量但灵活的重建的关键见解是，将关于关节体形状的通用人类先验（从大规模训练数据中学习）与视频特定的关节“骨骼袋”变形（通过测试时间优化适合单个视频）仔细结合。我们通过学习一个神经隐式模型来实现这一点，该模型将身体和衣服的变形作为单独的运动模型层来解开。为了捕捉服装的微妙几何形状，我们在优化过程中利用了基于图像的先验，如人体姿势、表面法线和光流。由此产生的神经场可以提取到时间一致的网格中，或进一步优化为显式3D高斯分布，以实现高保真交互式渲染。在具有高度挑战性的服装变形和物体交互的数据集上，DressReston可以产生比现有技术更高保真的3D重建。项目页面：https://jefftan969.github.io/dressrecon/ et.al.|[2409.20563](http://arxiv.org/abs/2409.20563)|null|
|**2024-09-25**|**TalkinNeRF: Animatable Neural Fields for Full-Body Talking Humans**|我们介绍了一种新的框架，该框架从单眼视频中学习全身说话的人的动态神经辐射场（NeRF）。之前的工作只代表身体姿势或面部。然而，人类通过全身进行交流，结合身体姿势、手势和面部表情。在这项工作中，我们提出了TalkinNeRF，这是一个基于NeRF的统一网络，代表了整体4D人体运动。给定一个受试者的单眼视频，我们学习身体、面部和手的相应模块，这些模块结合在一起生成最终结果。为了捕捉复杂的手指关节，我们学习了手的额外变形场。我们的多身份表示能够同时训练多个科目，以及在完全看不见的姿势下进行强大的动画。只要输入一段短视频，它也可以推广到新的身份。我们展示了最先进的性能，用于为全身说话的人类制作动画，具有精细的手部发音和面部表情。 et.al.|[2409.16666](http://arxiv.org/abs/2409.16666)|null|
|**2024-09-24**|**Generative 3D Cardiac Shape Modelling for In-Silico Trials**|我们提出了一种深度学习方法，基于将形状表示为神经有符号距离场的零级集，对合成主动脉形状进行建模和生成，该方法受一系列可训练的嵌入向量的约束，并对每个形状的几何特征进行编码。通过使神经场在采样表面点上消失并强制其空间梯度具有单位范数，在从CT图像重建的主动脉根部网格数据集上训练网络。实证结果表明，我们的模型可以高保真地表示主动脉形状。此外，通过从学习到的嵌入向量中采样，我们可以生成类似于真实患者解剖结构的新形状，可用于计算机模拟试验。 et.al.|[2409.16058](http://arxiv.org/abs/2409.16058)|null|
|**2024-09-21**|**MOSE: Monocular Semantic Reconstruction Using NeRF-Lifted Noisy Priors**|由于缺乏几何指导和不完美的视图相关2D先验，从单眼图像中精确重建密集和语义注释的3D网格仍然是一项具有挑战性的任务。尽管我们已经见证了隐式神经场景表示的最新进展，能够简单地从多视图图像中进行精确的2D渲染，但很少有研究仅使用单眼先验来解决3D场景理解问题。在本文中，我们提出了MOSE，这是一种神经场语义重建方法，可以将推断的图像级噪声先验提升到3D，在3D和2D空间中产生精确的语义和几何。我们方法的关键动机是利用通用类不可知的分段掩码作为指导，在训练过程中促进渲染语义的局部一致性。在语义的帮助下，我们进一步将平滑正则化应用于无纹理区域，以获得更好的几何质量，从而实现几何和语义的互惠互利。在ScanNet数据集上的实验表明，我们的MOSE在3D语义分割、2D语义分割和3D表面重建任务的所有指标上都优于相关基线。 et.al.|[2409.14019](http://arxiv.org/abs/2409.14019)|null|
|**2024-09-17**|**SplatFields: Neural Gaussian Splats for Sparse 3D and 4D Reconstruction**|从多视图图像中数字化3D静态场景和4D动态事件长期以来一直是计算机视觉和图形学领域的一个挑战。最近，3D高斯散斑（3DGS）已经成为一种实用且可扩展的重建方法，由于其令人印象深刻的重建质量、实时渲染能力以及与广泛使用的可视化工具的兼容性而越来越受欢迎。然而，该方法需要大量的输入视图来实现高质量的场景重建，这引入了一个重大的实际瓶颈。在捕捉动态场景时，这一挑战尤为严峻，因为部署广泛的相机阵列的成本可能高得令人望而却步。在这项工作中，我们发现斑点特征缺乏空间自相关性是导致3DGS技术在稀疏重建环境中性能不佳的因素之一。为了解决这个问题，我们提出了一种优化策略，通过将splat特征建模为相应隐式神经场的输出，有效地正则化splat特征。这导致在各种场景中重建质量的一致提高。我们的方法有效地处理了静态和动态情况，这在不同设置和场景复杂性的广泛测试中得到了证明。 et.al.|[2409.11211](http://arxiv.org/abs/2409.11211)|null|
|**2024-10-02**|**Neural Fields for Adaptive Photoacoustic Computed Tomography**|光声计算机断层扫描（PACT）是一种具有广泛医学应用的非侵入性成像技术。传统的PACT图像重建算法受到组织中声速不均匀（SOS）引起的波前失真的影响，导致图像质量下降。考虑到这些影响可以提高图像质量，但测量SOS分布的实验成本很高。另一种方法是仅使用PA信号对初始压力图像和SOS进行联合重建。现有的关节重建方法存在局限性：计算成本高，无法直接恢复SOS，以及依赖于不准确的简化假设。隐式神经表示或神经场是计算机视觉中的一种新兴技术，用于通过基于坐标的神经网络学习物理场的有效和连续表示。在这项工作中，我们介绍了NF-APACT，这是一种高效的自监督框架，利用神经场来估计SOS，以实现准确和鲁棒的多通道解卷积。我们的方法比现有方法更快、更准确地消除了SOS像差。我们在一个新的数值体模以及实验收集的体模和体内数据上证明了我们的方法的成功。我们的代码和数字幻影可在https://github.com/Lukeli0425/NF-APACT. et.al.|[2409.10876](http://arxiv.org/abs/2409.10876)|null|
|**2024-09-09**|**Lagrangian Hashing for Compressed Neural Field Representations**|我们提出了拉格朗日散列，这是一种神经场的表示，结合了依赖于欧拉网格（即~InstantNGP）的快速训练NeRF方法的特征，以及使用配备有特征的点作为表示信息的方法（例如3D高斯散点或PointNeRF）。我们通过将基于点的表示合并到InstantNGP表示的分层哈希表的高分辨率层中来实现这一点。由于我们的点具有影响域，我们的表示可以被解释为哈希表中存储的高斯混合。我们提出的损失鼓励我们的高斯人向需要更多代表预算才能充分代表的地区移动。我们的主要发现是，我们的表示允许使用更紧凑的表示来重建信号，而不会影响质量。 et.al.|[2409.05334](http://arxiv.org/abs/2409.05334)|null|

<p align=right>(<a href=#updated-on-20241018>back to top</a>)</p>

[contributors-shield]: https://img.shields.io/github/contributors/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[contributors-url]: https://github.com/Vincentqyw/cv-arxiv-daily/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[forks-url]: https://github.com/Vincentqyw/cv-arxiv-daily/network/members
[stars-shield]: https://img.shields.io/github/stars/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[stars-url]: https://github.com/Vincentqyw/cv-arxiv-daily/stargazers
[issues-shield]: https://img.shields.io/github/issues/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[issues-url]: https://github.com/Vincentqyw/cv-arxiv-daily/issues

