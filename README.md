[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]

## Updated on 2024.10.22
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
|**2024-10-18**|**Learning autonomous driving from aerial imagery**|在这项工作中，我们考虑了仅从航拍图像中学习端到端感知以控制地面车辆的问题。摄影测量模拟器允许通过将预先生成的资产转换为新视图来合成新视图。然而，它们的设置成本很高，需要仔细收集数据，并且通常需要人工来创建可用的模拟器。我们使用神经辐射场（NeRF）作为中间表示，从地面车辆的角度合成新的视图。然后，这些新颖的观点可用于几个下游的自主导航应用。在这项工作中，我们通过应用从图像和深度数据中训练端到端学习策略，展示了新颖视图合成的实用性。在传统的真实到模拟到真实的框架中，收集的数据将被转换为视觉模拟器，然后可用于生成新的视图。相比之下，使用NeRF可以实现紧凑的表示，并能够在环境中收集更多数据时优化视觉模拟器的参数。我们通过在机器人汽车上部署模仿策略，证明了我们的方法在定制的迷你城市环境中的有效性。我们还考虑了位置定位的任务，并证明我们的方法能够在现实世界中重新定位汽车。 et.al.|[2410.14177](http://arxiv.org/abs/2410.14177)|null|
|**2024-10-18**|**DaRePlane: Direction-aware Representations for Dynamic Scene Reconstruction**|最近许多建模和重新渲染动态场景的方法都利用了基于平面的显式表示，解决了与神经辐射场（NeRF）和高斯飞溅（GS）等模型相关的训练时间慢的问题。然而，仅仅将4D动态场景分解为多个基于2D平面的表示不足以对具有复杂运动的场景进行高保真度重渲染。作为回应，我们提出了DaRePlane，这是一种新的方向感知表示方法，可以从六个不同的方向捕获场景动态。这种学习表示经过逆双树复小波变换（DTCWT）以恢复基于平面的信息。在NeRF管道中，DaRePlane通过融合来自这些恢复平面的向量来计算每个时空点的特征，然后传递给一个微小的MLP进行颜色回归。当应用于高斯飞溅时，DaRePlane计算高斯点的特征，然后使用微小的多头MLP进行时空变形预测。值得注意的是，为了解决六个实数和六个虚数方向感知小波系数引入的冗余问题，我们引入了一种可训练的掩蔽方法，在不显著降低性能的情况下缓解了存储问题。为了证明DaRePlane的通用性和效率，我们在常规和手术动态场景下对NeRF和GS系统进行了测试。大量实验表明，DaRePlane在各种复杂动态场景的新颖视图合成中具有最先进的性能。 et.al.|[2410.14169](http://arxiv.org/abs/2410.14169)|null|
|**2024-10-17**|**DepthSplat: Connecting Gaussian Splatting and Depth**|高斯散射和单/多视图深度估计通常是单独研究的。本文中，我们提出了DepthSplat来连接高斯溅射和深度估计，并研究了它们之间的相互作用。更具体地说，我们首先通过利用预先训练的单眼深度特征来贡献一个稳健的多视图深度模型，从而得到高质量的前馈3D高斯飞溅重建。我们还表明，高斯飞溅可以作为一种无监督的预训练目标，用于从大规模未标记的数据集中学习强大的深度模型。我们通过广泛的消融和跨任务转移实验验证了高斯溅射和深度估计之间的协同作用。我们的DepthSplat在ScanNet、RealEstate10K和DL3DV数据集上实现了深度估计和新颖视图合成方面的最先进性能，展示了连接这两个任务的互惠互利。我们的代码、模型和视频结果可在https://haofeixu.github.io/depthsplat/. et.al.|[2410.13862](http://arxiv.org/abs/2410.13862)|**[link](https://github.com/cvg/depthsplat)**|
|**2024-10-17**|**Hybrid bundle-adjusting 3D Gaussians for view consistent rendering with pose optimization**|新型视图合成在3D计算机视觉领域取得了重大进展。然而，从不完美的相机姿态渲染视图一致的新颖视图仍然具有挑战性。本文介绍了一种混合束调整3D高斯模型，该模型能够实现具有姿态优化的视图一致性渲染。该模型联合提取基于图像和神经的3D表示，以在面向前方的场景中同时生成视图一致的图像和相机姿态。我们的模型的有效性通过在真实和合成数据集上进行的广泛实验得到了证明。这些实验清楚地表明，我们的模型可以有效地优化神经场景表示，同时解决明显的相机姿态失准问题。源代码可在https://github.com/Bistu3DV/hybridBA. et.al.|[2410.13280](http://arxiv.org/abs/2410.13280)|**[link](https://github.com/bistu3dv/hybridba)**|
|**2024-10-18**|**UniG: Modelling Unitary 3D Gaussians for View-consistent 3D Reconstruction**|在这项工作中，我们提出了UniG，这是一种视图一致的3D重建和新颖的视图合成模型，可以从稀疏图像中生成3D高斯的高保真表示。现有的基于3D高斯的方法通常对每个视图的每个像素进行高斯回归，分别为每个视图创建3D高斯，并通过点连接将其合并。这种与视图无关的重建方法通常会导致视图不一致问题，其中来自不同视图的同一3D点的预测位置可能存在差异。为了解决这个问题，我们开发了一个类似DETR（DEtect TRansformer）的框架，该框架将3D高斯视为解码器查询，并通过在多个输入图像上执行多视图交叉注意（MVDFA）来逐层更新其参数。通过这种方式，多个视图自然有助于对3D高斯的统一表示进行建模，从而使3D重建更加视图一致。此外，由于用作解码器查询的3D高斯数与输入视图的数量无关，因此允许任意数量的输入图像，而不会导致内存爆炸。大量的实验验证了我们的方法的优势，在定量和定性上展示了优于现有方法的性能（在Objaverse上训练并在GSO基准上测试时，PSNR提高了4.2 dB）。该代码将于https://github.com/jwubz123/UNIG. et.al.|[2410.13195](http://arxiv.org/abs/2410.13195)|**[link](https://github.com/jwubz123/UNIG)**|
|**2024-10-16**|**Triplet: Triangle Patchlet for Mesh-Based Inverse Rendering and Scene Parameters Approximation**|辐射场的最新进展显著改善了新颖的视图合成。然而，在许多现实世界的应用中，更高级的挑战在于逆渲染，它试图推导场景的物理属性，包括光、几何、纹理和材质。然而，网格作为许多模拟管道采用的传统表示方法，在逆渲染的辐射场中仍然显示出有限的影响。本文介绍了一种名为三角形补丁（缩写为Triplet）的新框架，这是一种基于网格的表示方法，可以全面近似这些场景参数。我们首先用随机生成的点或从相机校准中获得的稀疏点组装三元组，其中所有人脸都被视为一个独立的元素。接下来，我们模拟光的物理交互，并使用光栅化和光线跟踪等传统图形渲染技术优化场景参数，同时进行密度控制和传播。还提出了一种迭代网格提取过程，在该过程中，我们继续通过基于图的操作对几何形状和材料进行优化。我们还引入了几个监管术语，以便更好地概括材料性能。我们的框架可以在没有统一框架中的光、材料和几何先验的情况下，通过网格精确估计光、材料及几何。实验表明，我们的方法可以在重建高质量几何和精确材料属性的同时实现最先进的视觉质量。 et.al.|[2410.12414](http://arxiv.org/abs/2410.12414)|**[link](https://github.com/rando11199/triplet)**|
|**2024-10-16**|**GAN Based Top-Down View Synthesis in Reinforcement Learning Environments**|人类的行为是基于对环境的心理感知。即使环境的所有方面都不可见，人类也有一个内部心理模型，可以将部分可见的场景概括为完全构建和连接的视图。这种内部心理模型使用过去遇到的环境的空间和时间方面的学习抽象表示。强化学习环境中的人工智能也受益于从经验中学习环境的表示。它为代理提供了不直接可见的观点，帮助其做出更好的策略决策。它还可以用于预测环境的未来状态。该项目探索了基于人工智能的第一人称视图观察，使用生成对抗网络（GAN）学习强化学习环境的自上而下视图。自顶向下视图很有用，因为它通过构建整个环境的地图来提供环境的完整概述。它提供有关对象的尺寸和形状以及它们彼此之间的相对位置的信息。最初，当代理只能看到环境的部分观察时，只会生成部分自上而下的视图。当代理通过一组操作探索环境时，生成的自上而下的视图就完成了。这种生成的自上而下的视图可以帮助代理推断出更好的策略决策。该项目的重点是学习强化学习环境的自上而下的视图。它不处理任何强化学习任务。 et.al.|[2410.12372](http://arxiv.org/abs/2410.12372)|null|
|**2024-10-16**|**EG-HumanNeRF: Efficient Generalizable Human NeRF Utilizing Human Prior for Sparse View**|可泛化神经辐射场（NeRF）实现了基于神经的数字人体渲染，而无需对每个场景进行再训练。当与人类先验知识相结合时，即使输入视图稀疏，也可以实现高质量的人类渲染。然而，这些方法的推理仍然很慢，因为需要对每条射线进行大量的神经网络查询来确保渲染质量。此外，遮挡区域通常会出现伪影，尤其是在输入视图稀疏的情况下。为了解决这些问题，我们提出了一种通用的人类NeRF框架，通过广泛利用人类先验知识，实现了稀疏输入视图的高质量和实时渲染。我们采用两阶段采样缩减策略加速渲染：首先在人体几何体周围构建边界网格，以减少采样引导回归的光线样本数量，然后使用较少的引导样本进行体绘制。为了提高渲染质量，特别是在遮挡区域，我们提出了一种遮挡感知注意力机制，从人类先验中提取遮挡信息，然后使用图像空间细化网络来提高渲染质量。此外，对于体绘制，我们采用了符号射线距离函数（SRDF）公式，这使我们能够在每个采样位置提出SRDF损失，以进一步提高渲染质量。我们的实验表明，我们的方法在渲染质量方面优于最先进的方法，并且与速度优先的新型视图合成方法相比，具有竞争力的渲染速度。 et.al.|[2410.12242](http://arxiv.org/abs/2410.12242)|null|
|**2024-10-15**|**SplatPose+: Real-time Image-Based Pose-Agnostic 3D Anomaly Detection**|基于图像的姿态不可知三维异常检测是工业质量控制中出现的一项重要任务。该任务旨在在给定一组无异常对象的参考图像的情况下，从测试对象的查询图像中查找异常。挑战在于查询视图（也称为姿势）是未知的，可能与参考视图不同。目前，已经出现了OmniposeAD和SplatPose等新方法，通过在查询视图中合成伪参考图像进行像素间比较来弥合这一差距。然而，这些方法都不能实时推断，这在大规模生产的工业质量控制中至关重要。因此，我们提出了SplatPose+，它采用了一种混合表示，由用于定位的运动结构（SfM）模型和用于新视图合成的3D高斯散点（3DGS）模型组成。尽管我们提出的管道需要计算额外的SfM模型，但与SplatPose相比，它提供了实时推理速度和更快的训练。在质量方面，我们利用多姿态异常检测（MAD-SIM）数据集在姿态无关异常检测基准上实现了新的SOTA。 et.al.|[2410.12080](http://arxiv.org/abs/2410.12080)|null|
|**2024-10-15**|**LoGS: Visual Localization via Gaussian Splatting with Fewer Training Images**|视觉定位涉及估计查询图像的6-DoF（自由度）相机姿态，这是各种计算机视觉和机器人任务中的基本组成部分。本文介绍了LoGS，这是一种基于视觉的定位流水线，利用3D高斯散点（GS）技术作为场景表示。这种新颖的表示允许高质量的新颖视图合成。在映射阶段，首先应用运动结构（SfM），然后生成GS图。在定位过程中，通过图像检索、局部特征匹配和PnP求解器获得初始位置，然后在GS地图上通过综合分析的方式实现高精度姿态。在四个大规模数据集上的实验结果证明了所提出的方法在估计相机姿态方面的SoTA准确性和在具有挑战性的少镜头条件下的鲁棒性。 et.al.|[2410.11505](http://arxiv.org/abs/2410.11505)|null|

<p align=right>(<a href=#updated-on-20241022>back to top</a>)</p>

## 3D Reconstruction

|Publish Date|Title|Abstract|PDF|Code|
|---|---|---|---|---|
|**2024-10-17**|**Object Pose Estimation Using Implicit Representation For Transparent Objects**|物体姿态估计是计算机视觉中的一项重要任务。物体姿态给出了物体在现实世界空间中的方向和平移，这允许各种应用，如操纵、增强现实等。各种物体对光表现出不同的特性，如反射、吸收等。这使得理解物体在RGB和深度通道中的结构具有挑战性。最近的研究一直在向基于学习的方法发展，这些方法利用深度学习为对象姿态估计提供了一种更灵活、更通用的方法。一种这样的方法是渲染和比较方法，该方法从多个视图渲染对象并将其与给定的2D图像进行比较，这通常需要CAD模型形式的对象表示。我们认为CAD模型的合成纹理可能不适合渲染和比较操作。我们发现，如果对象以神经辐射场（NeRF）的形式表示为隐式（神经）表示，它会对实际场景进行更逼真的渲染，并保留关键的空间特征，这使得比较更加通用。我们在透明数据集上评估了渲染和比较方法的NeRF实现，发现它超过了当前最先进的结果。 et.al.|[2410.13465](http://arxiv.org/abs/2410.13465)|null|
|**2024-10-18**|**Context-Enhanced Multi-View Trajectory Representation Learning: Bridging the Gap through Self-Supervised Models**|使用通用密集表示对轨迹数据进行建模已成为各种下游应用的流行范式，如轨迹分类、行程时间估计和相似性计算。然而，现有的方法通常依赖于单一空间视图的轨迹，限制了它们捕获丰富上下文信息的能力，而丰富上下文信息对于深入了解不同地理空间背景下的运动模式至关重要。为此，我们提出了MVTraj，这是一种用于轨迹表示学习的新型多视图建模方法。MVTraj整合了从GPS到道路网络和兴趣点的各种背景知识，以更全面地了解轨迹数据。为了在多个视图之间对齐学习过程，我们利用GPS轨迹作为桥梁，并采用自我监督的借口任务来捕捉和区分不同空间视图之间的运动模式。在此之后，我们将来自不同视角的轨迹视为不同的模态，并应用分层跨模态交互模块来融合表示，从而丰富了从多个来源获得的知识。对真实世界数据集的广泛实验表明，MVTraj在与各种空间视图相关的任务中明显优于现有基线，验证了其在时空建模中的有效性和实用性。 et.al.|[2410.13196](http://arxiv.org/abs/2410.13196)|null|
|**2024-10-18**|**UniG: Modelling Unitary 3D Gaussians for View-consistent 3D Reconstruction**|在这项工作中，我们提出了UniG，这是一种视图一致的3D重建和新颖的视图合成模型，可以从稀疏图像中生成3D高斯的高保真表示。现有的基于3D高斯的方法通常对每个视图的每个像素进行高斯回归，分别为每个视图创建3D高斯，并通过点连接将其合并。这种与视图无关的重建方法通常会导致视图不一致问题，其中来自不同视图的同一3D点的预测位置可能存在差异。为了解决这个问题，我们开发了一个类似DETR（DEtect TRansformer）的框架，该框架将3D高斯视为解码器查询，并通过在多个输入图像上执行多视图交叉注意（MVDFA）来逐层更新其参数。通过这种方式，多个视图自然有助于对3D高斯的统一表示进行建模，从而使3D重建更加视图一致。此外，由于用作解码器查询的3D高斯数与输入视图的数量无关，因此允许任意数量的输入图像，而不会导致内存爆炸。大量的实验验证了我们的方法的优势，在定量和定性上展示了优于现有方法的性能（在Objaverse上训练并在GSO基准上测试时，PSNR提高了4.2 dB）。该代码将于https://github.com/jwubz123/UNIG. et.al.|[2410.13195](http://arxiv.org/abs/2410.13195)|**[link](https://github.com/jwubz123/UNIG)**|
|**2024-10-16**|**Configurable Embodied Data Generation for Class-Agnostic RGB-D Video Segmentation**|本文提出了一种生成大规模数据集的方法，以改善不同形状因子的机器人之间的类无关视频分割。具体来说，我们考虑的问题是，如果在数据生成过程中考虑了机器人的实施方式，那么在通用分割数据上训练的视频分割模型是否对特定的机器人平台更有效。为了回答这个问题，制定了一个管道，用于使用3D重建（例如来自HM3DSem）生成分段视频，这些视频可以根据机器人的实施例（例如传感器类型、传感器放置和照明源）进行配置。由此产生的大量RGB-D视频全景分割数据集（MVPd）被引入，用于与基础和视频分割模型进行广泛的基准测试，并支持视频分割中以实施例为重点的研究。我们的实验结果表明，在将基础模型转移到某些机器人实施例（如特定的相机放置）时，使用MVPd进行微调可以提高性能。这些实验还表明，使用3D模态（深度图像和相机姿态）可以提高视频分割的准确性和一致性。项目网页可在https://topipari.com/projects/MVPd et.al.|[2410.12995](http://arxiv.org/abs/2410.12995)|null|
|**2024-10-16**|**Cascade learning in multi-task encoder-decoder networks for concurrent bone segmentation and glenohumeral joint assessment in shoulder CT scans**|骨关节炎是一种影响骨骼和软骨的退行性疾病，通常导致骨赘形成、骨密度降低和关节间隙狭窄。恢复正常关节功能的治疗方案因病情的严重程度而异。这项工作引入了一种处理肩部CT扫描的创新深度学习框架。它具有肱骨近端和肩胛骨的语义分割、骨表面的3D重建、肩关节（GH）关节区域的识别以及三种常见骨关节炎相关病理的分期：骨赘形成（OS）、GH间隙缩小（JS）和肱骨肩胛骨对齐（HSA）。该流水线包括两个级联的CNN架构：用于分割的3D CEL-UNet和用于三重分类的3D Arthro-Net。使用571次CT扫描的回顾性数据集，对患有不同程度GH骨关节炎相关疾病的患者进行训练、验证和测试。肱骨三维重建的均方根误差和豪斯多夫距离中值分别为0.22mm和1.48mm，肩胛骨为0.24mm和1.48mm。其性能优于最先进的架构，可能适用于基于PSI的肩关节置换术前计划。OS、JS和HSA在所有三个类别中的分类准确率始终达到90%左右。推理管道的计算时间不到15秒，展示了该框架的效率和与骨科放射学实践的兼容性。这些结果代表了人工智能工具在医学翻译方面的一个有前景的进步。这一进展旨在简化术前计划流程，提供高质量的骨表面，并支持外科医生根据独特的患者关节状况选择最合适的手术方法。 et.al.|[2410.12641](http://arxiv.org/abs/2410.12641)|null|
|**2024-10-15**|**Stochastic 3D reconstruction of cracked polycrystalline NMC particles using 2D SEM data**|锂离子电池的性能受到其阴极性能的强烈影响，因此也受到阴极所含颗粒的3D微观结构的影响。在压延和循环过程中，阴极颗粒内会产生裂纹，这可能会以多种方式影响性能。一方面，裂纹降低了内部连接性，从而阻碍了阴极粒子内的电子传输。另一方面，颗粒内裂纹可以增加阴极反应表面。由于这些相互矛盾的影响，有必要定量研究电池循环如何影响开裂，以及开裂又如何影响电池性能。因此，有必要用结构描述符表征3D颗粒形态，并将其与有效电池性能定量关联。通常，使用图像数据进行3D结构表征。然而，信息丰富的3D成像技术耗时、昂贵且很少可用，因此分析通常必须依赖于2D图像数据。本文提出了一种新的体视学方法，用于生成虚拟3D阴极粒子，这些粒子表现出与实验测量粒子的2D截面中观察到的裂纹网络在统计上等效的裂纹网络。因此，更容易获得的2D图像数据足以得出破裂阴极颗粒的完整3D特征。在未来的研究中，虚拟生成的3D粒子将被用作空间分辨电化学机械模拟的几何输入，以加深我们对锂离子电池阴极结构-性能关系的理解。 et.al.|[2410.12020](http://arxiv.org/abs/2410.12020)|null|
|**2024-10-15**|**Robotic Arm Platform for Multi-View Image Acquisition and 3D Reconstruction in Minimally Invasive Surgery**|微创手术（MIS）具有显著的优势，如缩短恢复时间和最大限度地减少患者创伤，但在可见性和可及性方面存在挑战，使精确的3D重建成为手术规划和导航的重要工具。这项工作介绍了一种机器人手臂平台，用于在MIS环境中进行高效的多视图图像采集和精确的3D重建。我们将腹腔镜改装成机器人手臂，并在不同的照明条件（手术室和腹腔镜）和轨迹（球形和腹腔镜）下捕获了几个绵羊器官的离体图像。我们采用了最近发布的基于学习的特征匹配器与COLMAP相结合来生成我们的重建。通过高精度激光扫描对重建进行定量评估。我们的结果表明，虽然重建在真实的MIS照明和轨迹下遭受的损失最大，但我们的管道的许多版本都达到了接近亚毫米的精度，平均均方根误差为1.05毫米，倒角距离为0.82毫米。我们最好的重建结果发生在手术室照明和球形轨迹上。我们的机器人平台为MIS环境中的3D生成提供了一种受控、可重复的多视图数据采集工具，我们希望这能为训练基于学习的模型带来新的数据集。 et.al.|[2410.11703](http://arxiv.org/abs/2410.11703)|null|
|**2024-10-15**|**Simultaneous Diffusion Sampling for Conditional LiDAR Generation**|通过捕获反映周围环境几何形状的3D点云，LiDAR已成为自主系统的主要传感器。如果激光雷达扫描太稀疏、被障碍物遮挡或范围太小，在尊重场景几何形状的同时增强点云扫描对下游任务很有用。在视觉生成方法兴趣爆炸式增长的推动下，条件激光雷达生成开始兴起。本文提出了一种新的同时扩散采样方法，用于生成基于多视角场景三维结构的点云。关键思想是对生成过程施加多视图几何约束，利用互信息来增强结果。我们的方法首先将输入扫描重新转换为扫描周围的多个新视点，从而创建多个合成激光雷达扫描。然后，根据我们的方法，合成和输入的激光雷达扫描同时进行条件生成。结果表明，我们的方法可以对点云扫描产生准确和几何一致的增强，使其在各种基准测试中大大优于现有方法。 et.al.|[2410.11628](http://arxiv.org/abs/2410.11628)|null|
|**2024-10-16**|**Depth Estimation From Monocular Images With Enhanced Encoder-Decoder Architecture**|由于需要通常提供深度信息的立体或多视图数据，因此从单个2D图像估计深度是一项具有挑战性的任务。本文通过引入一种使用编码器-解码器架构的基于深度学习的新方法来应对这一挑战，其中Inception-ResNet-v2模型被用作编码器。根据现有文献，这是首次使用Inception-ResNet-v2作为单目深度估计的编码器，表明其性能优于之前的模型。Inception-ResNet-v2的使用使我们的模型能够有效地捕获通常难以预测的复杂对象和细粒度细节。此外，我们的模型结合了多尺度特征提取，以提高不同类型对象大小和距离的深度预测精度。我们提出了一种由深度损失、梯度边缘损失和SSIM损失组成的复合损失函数，其中对权重进行微调以优化加权和，确保深度估计不同方面的更好平衡。纽约大学深度V2数据集的实验结果表明，我们的模型达到了最先进的性能，ARE为0.064，RMSE为0.228，准确率（ $\delta$<1.25$ ）为89.3%。这些指标表明，即使在具有挑战性的情况下，我们的模型也能有效地预测深度，为机器人、3D重建和增强现实等现实世界的应用提供可扩展的解决方案。 et.al.|[2410.11610](http://arxiv.org/abs/2410.11610)|null|
|**2024-10-15**|**Multiview Scene Graph**|适当的场景表示是追求空间智能的核心，智能体可以稳健地重建并有效地理解3D场景。场景表示可以是度量，如3D重建中的地标图、对象检测中的3D边界框或占用预测中的体素网格，也可以是拓扑，如SLAM中具有循环闭包的姿态图或SfM中的可见性图。在这项工作中，我们建议从未涂胶的图像构建多视图场景图（MSG），用互连的位置和对象节点在拓扑上表示场景。构建MSG的任务对现有的表示学习方法来说是具有挑战性的，因为它需要联合解决视觉位置识别、对象检测和来自视野有限和潜在大视点变化的图像的对象关联问题。为了评估任何解决这一任务的方法，我们开发了一个基于公共3D数据集的MSG数据集和注释。我们还提出了一种基于MSG边联合得分交集的评估度量。此外，我们开发了一种基于主流预训练视觉模型的新基线方法，将视觉位置识别和对象关联结合到一个Transformer解码器架构中。实验证明，与现有的相关基线相比，我们的方法具有更优的性能。 et.al.|[2410.11187](http://arxiv.org/abs/2410.11187)|null|

<p align=right>(<a href=#updated-on-20241022>back to top</a>)</p>

## Diffusion

|Publish Date|Title|Abstract|PDF|Code|
|---|---|---|---|---|
|**2024-10-18**|**A GARCH model with two volatility components and two driving factors**|我们引入了一种新的GARCH模型，该模型整合了两种不确定性来源，以更好地捕捉金融资产波动中经常观察到的丰富的多成分动态。该模型提供了未来对数回报特征函数的准封闭形式表示，从中可以推导出期权定价的半解析公式。通过理论分析，建立了模型严格平稳性和几何遍历性的充分条件，同时得到了模型的连续时间扩散极限。使用标准普尔500时间序列数据进行的样本内和样本外实证评估表明，我们的模型在预测回报和期权价格方面优于广泛使用的单因素模型。 et.al.|[2410.14585](http://arxiv.org/abs/2410.14585)|null|
|**2024-10-18**|**Semi-Implicit Lagrangian Voronoi Approximation for Compressible Viscous Fluid Flows**|本文对基于Voronoi网格的拉格朗日方法的最新研究做出了贡献。其目的是设计一种新的保守数值方案，该方案可以比SPH（平滑粒子流体动力学）方法更精确地模拟复杂的流动和多相问题，但与固定网格拓扑上的扩散界面模型不同，它不会受到计算网格质量恶化的影响。数值解存储在粒子中，粒子随流体速度移动，也起着计算网格生成器的作用，在每个时间步长都能有效地重建。主要的新颖之处在于将拉格朗日Voronoi方案与可压缩流的半隐式积分器相结合。这允许对低马赫数流进行建模，而不会对时间步长施加极其严格的稳定性约束，并且可以正确缩放数值粘度。通过将动力学的可逆部分与不可逆（粘性）部分分开，然后利用可逆子系统的熵守恒推导出辅助椭圆方程，得到未知压力的隐式线性系统。该方法被称为SILVA（半隐式拉格朗日-沃罗诺伊近似），在各种具有不同马赫数、冲击和多相流的测试案例中得到了验证。 et.al.|[2410.14564](http://arxiv.org/abs/2410.14564)|null|
|**2024-10-18**|**Intrinsic cell-to-cell variance from experimental single-cell motility data**|在分析一组运动物体的单个位置动态时，提取的表征单个物体运动的参数，如均方瞬时速度或扩散率，表现出由于三种不同效应的卷积而导致的扩散：i）由波动环境引起的运动随机性，并由有限的观测时间增强，ii）取决于检测技术细节的测量误差，iii）表征单个物体之间差异的内在参数方差，即最终感兴趣的量。我们使用广义朗之万方程（GLE）开发了分离这些效应的理论框架，该方程构成了主动和被动动力学的最一般描述，因为它是在没有近似的情况下从所研究系统的一般潜在多体哈密顿量中推导出来的。我们应用我们的方法来确定活的人类乳腺癌细胞、藻类细胞的内在细胞间差异，以及作为基准的水中被动移动聚苯乙烯珠的尺寸差异。我们发现藻类和人类乳腺癌细胞表现出显著的个体差异，这反映在内在均方瞬时速度在两个数量级上的扩散上，鉴于所研究的乳腺癌细胞的遗传同质性，这是显著的，并突出了它们的表型多样性。单细胞特性的内在方差的量化与感染生物学、生态学和医学有关，并为以非破坏性的方式在单个生物体水平上估计种群异质性开辟了新的可能性。我们的框架不仅限于运动特性，而且可以很容易地应用于一般的实验时间序列数据。 et.al.|[2410.14561](http://arxiv.org/abs/2410.14561)|null|
|**2024-10-18**|**Multi-modal Pose Diffuser: A Multimodal Generative Conditional Pose Prior**|蒙皮多人线性（SMPL）模型在3D人体姿态估计中起着至关重要的作用，它提供了一种简化而有效的人体表示。然而，在人类网格回归等任务中确保SMPL配置的有效性仍然是一个重大挑战，这突显了能够识别真实人类姿势的鲁棒人体姿势先验的必要性。为了解决这个问题，我们引入了MOPED:\underline{M}ulti-m\下划线{O}dal\下划线{P}os\下划线{E}\underline{D}iffuser.MOPED是第一种利用新型多模态条件扩散模型作为SMPL姿态参数先验的方法。我们的方法提供了强大的无条件姿态生成功能，能够对图像和文本等多模态输入进行调节。这种能力通过结合传统姿势先验中经常被忽视的额外背景来增强我们方法的适用性。在三个不同任务中的广泛实验——姿势估计、姿势去噪和姿势完成——表明我们基于多模态扩散模型的先验明显优于现有方法。这些结果表明，我们的模型捕捉到了更广泛的合理的人体姿势。 et.al.|[2410.14540](http://arxiv.org/abs/2410.14540)|null|
|**2024-10-18**|**Diffusion-based Semi-supervised Spectral Algorithm for Regression on Manifolds**|我们介绍了一种新的基于扩散的谱算法来处理高维数据的回归分析，特别是嵌入低维流形中的数据。传统的谱算法在这种情况下往往不足，主要是由于依赖于预定的核函数，这些核函数不能充分解决基于流形的数据中固有的复杂结构。通过采用图拉普拉斯近似，我们的方法利用了热核的局部估计特性，提供了一种自适应的、数据驱动的方法来克服这一障碍。我们算法的另一个明显优势在于其半监督学习框架，使其能够充分利用额外的未标记数据。这种能力通过允许算法挖掘数据流形的频谱和曲率来提高性能，从而更全面地了解数据集。此外，我们的算法以完全数据驱动的方式执行，直接在数据的固有流形结构内运行，不需要任何预定义的流形信息。我们对我们的算法进行了收敛性分析。我们的研究结果表明，该算法的收敛速度仅取决于底层流形的内在维数，从而避免了与较高环境维数相关的维数灾难。 et.al.|[2410.14539](http://arxiv.org/abs/2410.14539)|null|
|**2024-10-18**|**LEAD: Latent Realignment for Human Motion Diffusion**|我们的目标是从自然语言中生成逼真的人体运动。现代方法经常面临模型表现力和文本到运动对齐之间的权衡。一些人将文本和运动潜在空间对齐，但牺牲了表现力；另一些则依赖于扩散模型产生令人印象深刻的运动，但在其潜在空间中缺乏语义意义。这可能会损害现实主义、多样性和适用性。在这里，我们通过将潜在扩散与重新排列机制相结合来解决这个问题，从而产生一个新颖的、语义结构化的空间，对语言的语义进行编码。利用这一能力，我们引入了文本运动反转的任务，从几个例子中捕捉新的运动概念。对于运动合成，我们在HumanML3D和KIT-ML上评估了LEAD，并在真实感、多样性和文本运动一致性方面显示出与最先进的性能相当的性能。我们的定性分析和用户研究表明，与现代方法相比，我们的合成运动更清晰，更像人类，更符合文本。对于运动文本反转，与传统的VAE相比，我们的方法在捕获分布外特征方面表现出了更高的能力。 et.al.|[2410.14508](http://arxiv.org/abs/2410.14508)|null|
|**2024-10-18**|**Reinforcement Learning in Non-Markov Market-Making**|我们为最优做市（MM）交易问题开发了一个深度强化学习（RL）框架，特别关注具有半马尔可夫和霍克斯跳跃扩散动力学的价格过程。我们首先讨论了强化学习的基础知识和使用的深度强化学习框架，在那里我们为深度学习部分部署了最先进的软参与者批评（SAC）算法。SAC算法是一种非策略熵最大化算法，更适合处理具有连续状态和动作空间的复杂高维问题，如最优做市（MM）。我们介绍了所考虑的最优MM问题，其中我们详细介绍了建立用于模拟该策略的环境的所有确定性和随机性过程。在这里，我们还深入概述了所使用的跳跃扩散定价动力学，我们在限价订单簿中处理逆向选择的方法，并强调了优化问题的工作部分。接下来，我们将讨论训练和测试结果，我们将直观地展示确定性和随机性过程（如买卖、交易执行、库存和奖励函数）的重要性。我们讨论了这些结果的局限性，这是在这种情况下大多数扩散模型需要注意的重要点。 et.al.|[2410.14504](http://arxiv.org/abs/2410.14504)|null|
|**2024-10-18**|**ANT: Adaptive Noise Schedule for Time Series Diffusion Models**|生成性人工智能扩散模型的进展最近已经传播到时间序列（TS）领域，在各种任务上展示了最先进的性能。然而，先前关于TS扩散模型的研究往往借鉴了其他领域现有研究的框架，而没有考虑TS数据的特征，导致性能不佳。在这项工作中，我们提出了时间序列扩散模型的自适应噪声调度（ANT），该调度根据表示非平稳性的统计数据自动为给定的TS数据集预先确定适当的噪声调度。我们的直觉是，最优噪声调度应满足以下要求：1）它线性地降低了TS数据的非平稳性，使所有扩散步骤都具有同等意义，2）数据在最后一步被随机噪声破坏，3）步骤数量足够大。所提出的方法是实用的，因为它消除了以较小的额外成本找到最优噪声调度来计算给定数据集统计数据的必要性，这可以在训练前离线完成。我们在来自不同领域的数据集上验证了我们的方法在各种任务中的有效性，包括TS预测、细化和生成。代码可在此存储库中获得：https://github.com/seunghan96/ANT. et.al.|[2410.14488](http://arxiv.org/abs/2410.14488)|**[link](https://github.com/seunghan96/ant)**|
|**2024-10-18**|**DRL Optimization Trajectory Generation via Wireless Network Intent-Guided Diffusion Models for Optimizing Resource Allocation**|随着包括低空经济、6G和Wi-Fi在内的无线通信领域的快速发展，无线网络的规模不断扩大，同时对服务质量的要求也在不断提高。传统的基于深度强化学习（DRL）的优化模型可以通过智能地解决非凸优化问题来提高网络性能。然而，他们严重依赖在线部署，通常需要大量的初始培训。在线DRL优化模型通常根据当前的信道状态分布做出准确的决策。当这些分布发生变化时，它们的泛化能力会降低，这阻碍了实时和高可靠性无线通信网络所必需的响应能力。此外，不同的用户在不同的场景中有不同的服务质量（QoS）要求，传统的在线DRL方法难以适应这种变化。因此，探索灵活和定制的人工智能策略至关重要。我们提出了一种基于生成扩散模型（GDM）的无线网络意图（WNI）引导轨迹生成模型。该模型可以实时生成和微调，以实现目标并满足目标意图网络的约束，从而显著减少无线通信过程中的状态信息暴露。此外，WNI引导的优化轨迹生成可以定制，以满足差异化的QoS要求，提高未来智能网络的整体通信质量。大量的仿真结果表明，我们的方法在频谱效率变化方面具有更高的稳定性，并且在动态通信系统中优于传统的DRL优化模型。 et.al.|[2410.14481](http://arxiv.org/abs/2410.14481)|null|
|**2024-10-18**|**LUDVIG: Learning-free Uplifting of 2D Visual features to Gaussian Splatting scenes**|我们解决了将视觉特征或语义掩模从2D视觉模型提升到高斯散斑表示的3D场景的任务。尽管常见的方法依赖于基于迭代优化的过程，但我们表明，一种简单而有效的聚合技术可以产生出色的结果。将我们的方法应用于Segment Anything（SAM）的语义掩码，其分割质量可与最新技术相媲美。然后，我们将这种方法扩展到通用的DINOv2特征，通过图扩散整合3D场景几何，并在DINOv2没有像SAM那样在数百万个带注释的掩码上进行训练的情况下获得有竞争力的分割结果。 et.al.|[2410.14462](http://arxiv.org/abs/2410.14462)|null|

<p align=right>(<a href=#updated-on-20241022>back to top</a>)</p>

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

<p align=right>(<a href=#updated-on-20241022>back to top</a>)</p>

[contributors-shield]: https://img.shields.io/github/contributors/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[contributors-url]: https://github.com/Vincentqyw/cv-arxiv-daily/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[forks-url]: https://github.com/Vincentqyw/cv-arxiv-daily/network/members
[stars-shield]: https://img.shields.io/github/stars/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[stars-url]: https://github.com/Vincentqyw/cv-arxiv-daily/stargazers
[issues-shield]: https://img.shields.io/github/issues/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[issues-url]: https://github.com/Vincentqyw/cv-arxiv-daily/issues

