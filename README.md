[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]

## Updated on 2024.12.15
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
|**2024-12-12**|**Representing Long Volumetric Video with Temporal Gaussian Hierarchy**|本文旨在解决从多视图RGB视频重建长体积视频的挑战。最近的动态视图合成方法利用强大的4D表示，如特征网格或点云序列，来实现高质量的渲染结果。然而，它们通常仅限于短（1~2s）的视频片段，在处理较长的视频时，通常会占用大量内存。为了解决这个问题，我们提出了一种新的4D表示方法，称为时间高斯层次，用于对长体积视频进行紧凑建模。我们的主要观察结果是，动态场景中通常存在不同程度的时间冗余，这些场景由以不同速度变化的区域组成。受此启发，我们的方法构建了一个4D高斯基元的多级层次结构，其中每一级分别描述内容变化程度不同的场景区域，并自适应地共享高斯基元来表示不同时间段上不变的场景内容，从而有效地减少了高斯基元数量。此外，高斯层次结构的树状结构使我们能够用高斯基元的子集有效地表示特定时刻的场景，从而在训练或渲染过程中几乎恒定地使用GPU内存，而不管视频长度如何。大量的实验结果表明，我们的方法在训练成本、渲染速度和存储使用方面优于其他方法。据我们所知，这项工作是第一种能够有效处理数分钟体积视频数据同时保持最先进渲染质量的方法。我们的项目页面位于：https://zju3dv.github.io/longvolcap. et.al.|[2412.09608](http://arxiv.org/abs/2412.09608)|**[link](https://github.com/dendenxu/fast-gaussian-rasterization)**|
|**2024-12-12**|**Feat2GS: Probing Visual Foundation Models with Gaussian Splatting**|鉴于视觉基础模型（VFM）是在广泛的数据集上训练的，但通常仅限于2D图像，一个自然的问题出现了：它们对3D世界的理解程度如何？由于架构和训练协议（即目标、代理任务）的差异，迫切需要一个统一的框架来公平、全面地探索他们的3D意识。现有的3D探测工作建议单视图2.5D估计（例如深度和法线）或双视图稀疏2D对应（例如匹配和跟踪）。不幸的是，这些任务忽略了纹理感知，需要3D数据作为地面真实数据，这限制了其评估集的规模和多样性。为了解决这些问题，我们引入了Feat2GS，它从未经处理的图像中提取的VFM特征中读出3D高斯属性。这使我们能够通过新颖的视图合成来探索几何和纹理的3D感知，而不需要3D数据。此外，3DGS参数（几何体（ $\boldsymbol{x}，\alpha，\Sigma$）和纹理（$\bold symbol{1c}$ ））的解纠缠可以单独分析纹理和几何体感知。在Feat2GS下，我们进行了广泛的实验来探索几种VFM的3D感知能力，并研究了导致3D感知VFM的成分。基于这些发现，我们开发了几个变体，在不同的数据集上实现了最先进的技术。这使得Feat2GS可用于探测VFM，并作为新颖视图合成的简单而有效的基线。代码和数据将在https://fanegg.github.io/Feat2GS/. et.al.|[2412.09606](http://arxiv.org/abs/2412.09606)|null|
|**2024-12-12**|**DrivingRecon: Large 4D Gaussian Reconstruction Model For Autonomous Driving**|街道场景的逼真4D重建对于开发自动驾驶中的真实世界模拟器至关重要。然而，大多数现有的方法都是离线执行这项任务，并且依赖于耗时的迭代过程，这限制了它们的实际应用。为此，我们引入了大4D高斯重建模型（DrivingRecon），这是一种可推广的驾驶场景重建模型，可以直接从环绕视图视频中预测4D高斯。为了更好地整合环绕视图图像，提出了Prune和Dilate块（PD块）来消除相邻视图之间的重叠高斯点并去除冗余背景点。为了增强跨时间信息，对动态和静态解耦进行了定制，以更好地学习几何和运动特征。实验结果表明，与现有方法相比，DrivingRecon显著提高了场景重建质量和新颖的视图合成。此外，我们还探索了DrivingRecon在模型预训练、车辆自适应和场景编辑中的应用。我们的代码可在https://github.com/EnVision-Research/DriveRecon. et.al.|[2412.09043](http://arxiv.org/abs/2412.09043)|**[link](https://github.com/envision-research/driverecon)**|
|**2024-12-12**|**Pragmatist: Multiview Conditional Diffusion Models for High-Fidelity 3D Reconstruction from Unposed Sparse Views**|由于其不受约束的性质，从稀疏、无基观测中推断3D结构具有挑战性。最近的方法提出以数据驱动的方式直接从非平稳输入中预测隐式表示，取得了有希望的结果。然而，这些方法不利用几何先验，也不会产生看不见区域的幻觉，因此重建精细的几何和纹理细节具有挑战性。为了应对这一挑战，我们的关键思想是将这个不适定问题重新表述为条件新视图合成，旨在从有限的输入视图中生成完整的观察结果，以促进重建。通过完整的观察，可以很容易地恢复输入视图的姿态，并进一步用于优化重建的对象。为此，我们提出了一种新的管道实用主义者。首先，我们通过多视图条件扩散模型生成对物体的完整观察。然后，我们使用前馈大重建模型来获得重建的网格。为了进一步提高重建质量，我们通过反转获得的3D表示来恢复输入视图的姿态，并使用详细的输入视图进一步优化纹理。与以前的方法不同，我们的管道通过有效地利用无基输入和生成先验来改进重建，从而避免了直接解决高度不适定的问题。大量实验表明，我们的方法在几个基准测试中取得了良好的性能。 et.al.|[2412.08412](http://arxiv.org/abs/2412.08412)|null|
|**2024-12-11**|**NeRF-NQA: No-Reference Quality Assessment for Scenes Generated by NeRF and Neural View Synthesis Methods**|神经视图合成（NVS）已被证明在使用具有稀疏视图的图像集生成高保真密集视点视频方面是有效的。然而，现有的质量评估方法，如PSNR、SSIM和LPIPS，并不是为NVS和NeRF变体合成的具有密集视点的场景量身定制的，因此，它们在捕捉感知质量方面往往不足，包括NVS合成场景的空间和角度方面。此外，由于缺乏密集的地面真实视图，对NVS合成场景的全面参考质量评估变得具有挑战性。例如，LLFF等数据集仅提供稀疏图像，不足以进行完整的参考评估。为了解决上述问题，我们提出了NeRF NQA，这是第一种针对由NVS和NeRF变体合成的密集观测场景的无参考质量评估方法。NeRF NQA采用联合质量评估策略，整合了视图和点方法，以评估NVS生成场景的质量。视图方法评估每个单独合成视图的空间质量和整体视图间一致性，而点方法侧重于场景表面点的角度质量及其复合点间质量。进行了广泛的评估，将NeRF NQA与23种主流视觉质量评估方法（来自图像、视频和光场评估领域）进行了比较。结果表明，NeRF NQA显著优于现有的评估方法，在评估无参考的NVS合成场景方面显示出显著的优势。本文的实施方式可在https://github.com/VincentQQu/NeRF-NQA. et.al.|[2412.08029](http://arxiv.org/abs/2412.08029)|**[link](https://github.com/vincentqqu/nerf-nqa)**|
|**2024-12-10**|**From an Image to a Scene: Learning to Imagine the World from a Million 360 Videos**|对物体和场景的三维（3D）理解在人类与世界互动的能力中起着关键作用，一直是计算机视觉、图形学和机器人学的一个活跃研究领域。大规模合成和以对象为中心的3D数据集已被证明在训练对对象有3D理解的模型方面是有效的。然而，由于缺乏大规模数据，将类似的方法应用于现实世界的对象和场景是困难的。视频是现实世界3D数据的潜在来源，但在规模上很难找到同一内容的不同但相应的视图。此外，标准视频具有在拍摄时确定的固定视点。这限制了从各种更多样化和潜在有用的角度访问场景的能力。我们认为，大规模360度视频可以解决这些局限性，提供：来自不同视角的可扩展对应帧。在本文中，我们介绍了360-1M，一个360度视频数据集，以及一个从不同视点按比例高效查找相应帧的过程。我们在360-1M上训练基于扩散的模型Odin。借助迄今为止最大的真实世界多视图数据集，Odin能够自由生成真实世界场景的新颖视图。与之前的方法不同，Odin可以在环境中移动相机，使模型能够推断场景的几何形状和布局。此外，我们在标准新颖视图合成和3D重建基准测试中表现出了改进的性能。 et.al.|[2412.07770](http://arxiv.org/abs/2412.07770)|**[link](https://github.com/mattwallingford/360-1m)**|
|**2024-12-10**|**SimVS: Simulating World Inconsistencies for Robust View Synthesis**|新颖的视图合成技术在静态场景中取得了令人印象深刻的结果，但在面对随意捕捉设置固有的不一致性时却举步维艰：变化的照明、场景运动和其他难以明确建模的意外效果。我们提出了一种利用生成视频模型来模拟捕获过程中可能出现的世界不一致的方法。我们使用这个过程以及现有的多视图数据集来创建合成数据，以训练一个多视图协调网络，该网络能够将不一致的观察结果协调成一致的3D场景。我们证明，我们的世界模拟策略在处理现实世界场景变化方面明显优于传统的增强方法，从而在存在各种具有挑战性的不一致的情况下实现了高度精确的静态3D重建。项目页面：https://alextrevithick.github.io/simvs et.al.|[2412.07696](http://arxiv.org/abs/2412.07696)|null|
|**2024-12-10**|**Faster and Better 3D Splatting via Group Training**|3D高斯散斑（3DGS）已成为一种强大的新型视图合成技术，通过其高斯基元表示在高保真场景重建方面表现出卓越的能力。然而，大量基元引起的计算开销对训练效率构成了重大瓶颈。为了克服这一挑战，我们提出了组训练，这是一种简单而有效的策略，可以将高斯基元组织成可管理的组，优化训练效率并提高渲染质量。这种方法与现有的3DGS框架（包括vanilla 3DGS和Mip Splatting）具有通用兼容性，在保持卓越合成质量的同时，始终实现加速训练。广泛的实验表明，我们简单的组训练策略在不同场景下实现了高达30%的收敛速度和更高的渲染质量。 et.al.|[2412.07608](http://arxiv.org/abs/2412.07608)|null|
|**2024-12-10**|**ResGS: Residual Densification of 3D Gaussian for Efficient Detail Recovery**|最近，3D高斯散斑（3D-GS）在新颖的视图合成中占主导地位，实现了高保真度和效率。然而，它往往难以捕捉到丰富的细节和完整的几何形状。我们的分析强调了3D-GS的一个关键局限性，这是由致密化中的固定阈值引起的，该阈值在阈值变化时平衡了几何覆盖与细节恢复。为了解决这个问题，我们引入了一种新的致密化方法，残差分割，该方法添加了一个降尺度高斯作为残差。我们的方法能够自适应地检索细节并补充缺失的几何体，同时实现渐进式细化。为了进一步支持这种方法，我们提出了一个名为ResGS的管道。具体来说，我们整合了一个高斯图像金字塔进行渐进式监督，并实施了一个选择方案，该方案优先考虑粗高斯图像随时间的致密化。大量实验表明，我们的方法达到了SOTA渲染质量。通过将我们的残差分割应用于各种3D-GS变体，可以实现一致的性能改进，强调其在基于3D GS的应用中的多功能性和更广泛的应用潜力。 et.al.|[2412.07494](http://arxiv.org/abs/2412.07494)|null|
|**2024-12-10**|**EventSplat: 3D Gaussian Splatting from Moving Event Cameras for Real-time Rendering**|我们介绍了一种通过高斯散斑在新的视图合成中使用事件相机数据的方法。事件摄像机提供卓越的时间分辨率和高动态范围。利用这些功能，我们可以在快速相机运动的情况下有效地应对新的视图合成挑战。为了初始化优化过程，我们的方法使用事件到视频模型中编码的先验知识。我们还使用样条插值来获得沿事件相机轨迹的高质量姿态。这提高了快速移动相机的重建质量，同时克服了传统上与基于事件的神经辐射场（NeRF）方法相关的计算限制。我们的实验评估表明，我们的结果比现有的基于事件的NeRF方法实现了更高的视觉保真度和更好的性能，同时渲染速度快了一个数量级。 et.al.|[2412.07293](http://arxiv.org/abs/2412.07293)|null|

<p align=right>(<a href=#updated-on-20241215>back to top</a>)</p>

## 3D Reconstruction

|Publish Date|Title|Abstract|PDF|Code|
|---|---|---|---|---|
|**2024-12-12**|**Stereo4D: Learning How Things Move in 3D from Internet Stereo Videos**|从图像中学习理解动态3D场景对于从机器人到场景重建的应用至关重要。然而，与大规模监督训练能够实现快速进展的其他问题不同，由于获取地面实况注释的根本困难，直接监督恢复3D运动的方法仍然具有挑战性。我们提出了一种从互联网立体广角视频中挖掘高质量4D重建的系统。我们的系统将相机姿态估计、立体深度估计和时间跟踪方法的输出融合并过滤成高质量的动态3D重建。我们使用这种方法以具有长期运动轨迹的世界一致性伪度量3D点云的形式生成大规模数据。我们通过训练DUSt3R的变体来预测真实世界图像对的结构和3D运动，展示了这些数据的实用性，表明对重建数据的训练能够泛化到不同的真实世界场景。项目页面：https://stereo4d.github.io et.al.|[2412.09621](http://arxiv.org/abs/2412.09621)|null|
|**2024-12-12**|**Learning Camera Movement Control from Real-World Drone Videos**|这项研究旨在自动化相机运动控制，将现有主题拍摄成有吸引力的视频，与通过直接生成像素来创建不存在的内容形成对比。我们选择无人机视频作为我们的测试案例，因为它们具有丰富而具有挑战性的运动模式、独特的视角和精确的控制。现有的人工智能摄像方法在模拟训练中的外观多样性有限，记录专家操作的成本高昂，以及在设计基于启发式的目标以覆盖所有场景方面存在困难。为了避免这些问题，我们提出了一种可扩展的方法，该方法涉及收集真实世界的训练数据以提高多样性，自动提取相机轨迹以最小化注释成本，以及训练一个不依赖启发式的有效架构。具体来说，我们通过在在线视频上运行3D重建，连接连续帧的相机姿态以制定3D相机路径，并使用卡尔曼滤波器识别和删除低质量数据来收集99k个高质量轨迹。此外，我们介绍了DVGFormer，这是一种自回归变换器，它利用相机路径和所有过去帧的图像来预测下一帧的相机运动。我们在38个合成自然场景和7个真实城市3D扫描中评估了我们的系统。我们的研究表明，我们的系统能够有效地学习执行具有挑战性的相机动作，例如在障碍物中导航、保持低空以提高感知速度，以及绕塔和建筑物旋转，这对录制高质量视频非常有用。数据和代码可以在dvgformer.github上找到。 et.al.|[2412.09620](http://arxiv.org/abs/2412.09620)|null|
|**2024-12-12**|**NormalFlow: Fast, Robust, and Accurate Contact-based Object 6DoF Pose Tracking with Vision-based Tactile Sensors**|触觉传感对于旨在实现人类水平灵巧性的机器人至关重要。在依赖触觉的技能中，基于触觉的物体跟踪是许多任务的基石，包括操纵、手部操纵和3D重建。在这项工作中，我们介绍了NormalFlow，一种快速、鲁棒、实时的基于触觉的6DoF跟踪算法。NormalFlow利用基于视觉的触觉传感器的精确表面法线估计，通过最小化触觉导出的表面法线之间的差异来确定对象运动。我们的结果表明，NormalFlow始终优于竞争基线，可以跟踪桌子表面等低纹理对象。对于长时间跟踪，我们演示了当传感器围绕珠子滚动360度时，NormalFlow保持2.5度的旋转跟踪误差。此外，我们展示了最先进的基于触觉的3D重建结果，展示了NormalFlow的高精度。我们相信NormalFlow为涉及用手与物体交互的高精度感知和操纵任务开辟了新的可能性。视频演示、代码和数据集可在我们的网站上获得：https://joehjhuang.github.io/normalflow. et.al.|[2412.09617](http://arxiv.org/abs/2412.09617)|**[link](https://github.com/rpl-cmu/normalflow)**|
|**2024-12-12**|**LiftImage3D: Lifting Any Single Image to 3D Gaussians with Video Generation Priors**|由于固有的几何模糊性和有限的视点信息，单图像3D重建仍然是计算机视觉中的一个基本挑战。潜在视频扩散模型（LVDM）的最新进展提供了从大规模视频数据中学习的有前景的3D先验。然而，有效地利用这些先验知识面临着三个关键挑战：（1）大型相机运动的质量下降，（2）实现精确相机控制的困难，以及（3）破坏3D一致性的扩散过程固有的几何失真。我们通过提出LiftImage3D来应对这些挑战，该框架有效地释放了LVDM的生成先验，同时确保了3D的一致性。具体来说，我们设计了一种铰接轨迹策略来生成视频帧，该策略将具有大相机运动的视频序列分解为具有可控小运动的视频。然后，我们使用鲁棒的神经匹配模型，即MASt3R，来校准生成帧的相机姿态并生成相应的点云。最后，我们提出了一种失真感知的3D高斯飞溅表示，它可以学习帧之间的独立失真，并输出未失真的规范高斯分布。大量实验表明，LiftImage3D在两个具有挑战性的数据集（即LLFF、DL3DV和坦克与神庙）上实现了最先进的性能，并很好地推广到各种野生图像，从卡通插图到复杂的现实世界场景。 et.al.|[2412.09597](http://arxiv.org/abs/2412.09597)|null|
|**2024-12-12**|**FreeSplatter: Pose-free Gaussian Splatting for Sparse-view 3D Reconstruction**|现有的稀疏视图重建模型严重依赖于精确的已知相机姿态。然而，从稀疏视图图像中导出相机外部函数和内部函数带来了重大挑战。在这项工作中，我们提出了FreeSplatter，这是一种高度可扩展的前馈重建框架，能够从未校准的稀疏视图图像中生成高质量的3D高斯图像，并在几秒钟内恢复其相机参数。FreeSplatter建立在流线型的变换器架构之上，包括顺序的自我关注块，这些块有助于多视图图像令牌之间的信息交换，并将其解码为逐像素的3D高斯基元。预测的高斯基元位于统一的参考系中，允许使用现成的求解器进行高保真3D建模和即时相机参数估计。为了满足以对象为中心和场景级重建的需求，我们在大量数据集上训练了FreeSplatter的两个模型变体。在这两种情况下，FreeSplatter在重建质量和姿态估计精度方面都优于最先进的基线。此外，我们还展示了FreeSplatter在提高下游应用程序（如文本/图像到3D内容创建）生产力方面的潜力。 et.al.|[2412.09573](http://arxiv.org/abs/2412.09573)|null|
|**2024-12-12**|**A Plug-and-Play Algorithm for 3D Video Super-Resolution of Single-Photon LiDAR data**|单光子雪崩二极管（SPAD）是一种先进的传感器，能够检测单个光子，并使用时间相关的单光子计数检测技术以皮秒分辨率记录它们的到达时间。它们用于各种应用，如激光雷达，可以捕获高速序列的二进制单光子图像，为重建具有高运动动力学的3D环境提供了巨大的潜力。为了补充单光子数据，它们通常与传统的被动相机配对，后者以较低的帧率捕获高分辨率（HR）强度图像。然而，从SPAD数据进行3D重建面临着挑战。聚合多个二进制测量值可以提高精度并减少噪声，但在动态场景中可能会导致运动模糊。此外，SPAD阵列的分辨率通常低于被动相机。为了解决这些问题，我们提出了一种新的计算成像算法，通过解决运动模糊和提高本地空间分辨率来改进SPAD数据中运动场景的3D重建。我们在优化方案中采用即插即用的方法，在3D场景的引导视频超分辨率和使用光流的精确图像重新对齐之间交替。对合成数据的实验表明，在各种信噪比和光子水平下，图像分辨率显著提高。我们在三种具有动态对象的实际情况下使用真实世界的SPAD测量来验证我们的方法。首先是实验室条件下短距离快速移动的场景；使用意法半导体的消费级SPAD传感器对人进行第二次非常低分辨率的成像；最后，使用短波红外SPAD相机在眼睛安全照明条件下对白天在室外325米范围内行走的人进行HR成像。这些结果证明了我们方法的鲁棒性和通用性。 et.al.|[2412.09427](http://arxiv.org/abs/2412.09427)|null|
|**2024-12-12**|**Mixture of neural fields for heterogeneous reconstruction in cryo-EM**|低温电子显微镜（Cryo-EM）是一种用于蛋白质结构测定的实验技术，可以在接近生理环境的情况下对大分子的集合进行成像。虽然最近的进展能够重建单个生物分子复合物的动态构象，但目前的方法并不能充分模拟具有混合构象和成分异质性的样品。特别是，包含多种蛋白质混合物的数据集需要联合推断结构、姿势、组成类别和构象状态以进行3D重建。在这里，我们提出了Hydra，这是一种通过参数化K个神经场之一产生的结构来完全从头计算模拟构象和组成异质性的方法。我们采用了一种新的基于似然的损失函数，并证明了我们的方法在由具有高度构象变异的蛋白质混合物组成的合成数据集上的有效性。我们还在含有不同蛋白质复合物混合物的细胞裂解物的实验数据集上演示了Hydra。Hydra扩展了非均匀重建方法的表现力，从而将冷冻EM的范围扩大到越来越复杂的样本。 et.al.|[2412.09420](http://arxiv.org/abs/2412.09420)|null|
|**2024-12-12**|**SLAM3R: Real-Time Dense Scene Reconstruction from Monocular RGB Videos**|本文介绍了\textbf{SLAM3R}，这是一种新颖有效的单目RGB SLAM系统，用于实时和高质量的密集3D重建。SLAM3R通过前馈神经网络无缝集成局部3D重建和全局坐标配准，提供了一种端到端的解决方案。给定一个输入视频，系统首先使用滑动窗口机制将其转换为重叠的剪辑。与传统的基于姿势优化的方法不同，SLAM3R直接从每个窗口中的RGB图像中回归3D点图，并逐步对齐和变形这些局部点图，以创建全局一致的场景重建——所有这些都不需要明确求解任何相机参数。跨数据集的实验一致表明，SLAM3R在保持20+FPS实时性能的同时，实现了最先进的重建精度和完整性。代码和权重位于：\url{https://github.com/PKU-VCL-3DV/SLAM3R}. et.al.|[2412.09401](http://arxiv.org/abs/2412.09401)|null|
|**2024-12-12**|**Synchrotron X-Ray Multi-Projection Imaging for Multiphase Flow**|多相流以分散在流体中的颗粒、气泡或液滴为特征，在自然和工业过程中无处不在。在不引入扰动的情况下，在非常小的尺度上研究4D（3D+时间）中密集分散的流动是具有挑战性的，但对于理解它们的宏观行为至关重要。X射线的穿透力和同步辐射设施等先进X射线源提供的通量为满足这一需求提供了机会。然而，这些设施目前的X射线方法需要旋转样品以获得4D信息，从而干扰了流动。在这里，我们展示了使用X射线多投影成像（XMPI）的潜力，这是一种在4D中暂时解析任何密集颗粒悬浮流的新技术，同时消除了样品旋转的需要。通过同时从多个观察方向获取微粒种子流的图像，我们可以确定它们在简单液体和高密度不透明的复杂流体（如血液）中流动时的瞬时三维位置。随着人工智能支持的稀疏投影4D重建的最新进展，这种方法为高速无旋转4D显微断层摄影创造了新的机会，开辟了一个新的时空前沿。借助XMPI，现在可以跟踪稠密悬浮液中单个微粒的运动，甚至可以扩展到湍流的混沌领域。 et.al.|[2412.09368](http://arxiv.org/abs/2412.09368)|null|
|**2024-12-12**|**Hyperbolic-constraint Point Cloud Reconstruction from Single RGB-D Images**|重建所需的对象和场景一直是3D计算机视觉的主要目标。单视点云重建因其成本低、结果准确而成为一种流行的技术。然而，单视图重建方法通常依赖于昂贵的CAD模型和复杂的几何先验。有效利用关于数据的先验知识仍然是一个挑战。本文将双曲空间引入三维点云重建，使模型能够以低失真表示和理解点云中的复杂层次结构。我们在先前方法的基础上，提出了双曲切弗距离和正则化三重态损失，以增强部分和完整点云之间的关系。此外，我们设计了自适应边界条件，以提高模型对3D结构的理解和重建。我们的模型优于大多数现有模型，消融研究证明了我们的模型及其组件的重要性。实验结果表明，我们的方法显著提高了特征提取能力。我们的模型在3D重建任务中表现出色。 et.al.|[2412.09055](http://arxiv.org/abs/2412.09055)|null|

<p align=right>(<a href=#updated-on-20241215>back to top</a>)</p>

## Diffusion

|Publish Date|Title|Abstract|PDF|Code|
|---|---|---|---|---|
|**2024-12-12**|**FreeScale: Unleashing the Resolution of Diffusion Models via Tuning-Free Scale Fusion**|视觉扩散模型取得了显著进展，但由于缺乏高分辨率数据和有限的计算资源，它们通常在有限的分辨率下进行训练，这阻碍了它们以更高分辨率生成高保真图像或视频的能力。最近的努力探索了无需调整的策略，以展示预训练模型未开发的更高分辨率视觉生成潜力。然而，这些方法仍然容易产生具有重复模式的低质量视觉内容。关键障碍在于，当模型生成的视觉内容超过其训练分辨率时，高频信息不可避免地会增加，从而导致累积误差产生不希望的重复模式。为了应对这一挑战，我们提出了FreeScale，这是一种无需调整的推理范式，通过尺度融合实现更高分辨率的视觉生成。具体来说，FreeScale处理来自不同接收尺度的信息，然后通过提取所需的频率分量将其融合。大量实验验证了我们的范式在扩展图像和视频模型的更高分辨率视觉生成能力方面的优越性。值得注意的是，与之前表现最佳的方法相比，FreeScale首次解锁了8k分辨率图像的生成。 et.al.|[2412.09626](http://arxiv.org/abs/2412.09626)|null|
|**2024-12-12**|**Illusion3D: 3D Multiview Illusion with 2D Diffusion Priors**|自动生成多视图错觉是一个令人信服的挑战，其中单个视觉内容可以从不同的观看角度提供不同的解释。传统的方法，如阴影艺术和线艺术，可以创造有趣的3D幻觉，但仅限于简单的视觉输出（即图形背景或线条绘制），限制了它们的艺术表现力和实用性。最近基于扩散的错觉生成方法可以生成更复杂的设计，但仅限于2D图像。在这项工作中，我们提出了一种基于用户提供的文本提示或图像创建3D多视图错觉的简单而有效的方法。我们的方法利用预训练的文本到图像扩散模型，通过可微分渲染优化神经3D表示的纹理和几何形状。当从多个角度观察时，这会产生不同的解释。我们开发了几种技术来提高生成的3D多视图错觉的质量。我们通过广泛的实验证明了我们方法的有效性，并展示了不同3D形式的幻觉生成。 et.al.|[2412.09625](http://arxiv.org/abs/2412.09625)|null|
|**2024-12-12**|**OmniDrag: Enabling Motion Control for Omnidirectional Image-to-Video Generation**|随着虚拟现实的普及，对可控创建沉浸式和动态全向视频（ODV）的需求正在增加。虽然之前的文本到ODV生成方法取得了令人印象深刻的结果，但由于仅依赖文本输入，它们在内容不准确和不一致方面遇到了困难。尽管最近的运动控制技术为视频生成提供了细粒度的控制，但将这些方法直接应用于ODV通常会导致空间失真和性能不理想，特别是在复杂的球形运动中。为了应对这些挑战，我们提出了OmniDrag，这是第一种能够实现场景和对象级运动控制的方法，用于精确、高质量的全向图像到视频生成。基于预训练的视频扩散模型，我们引入了一个全向控制模块，该模块与时间注意力层联合微调，以有效处理复杂的球形运动。此外，我们开发了一种新的球形运动估计器，可以准确地提取运动控制信号，并允许用户通过简单地绘制手柄和目标点来执行拖动式ODV生成。我们还提出了一个名为Move360的新数据集，解决了具有大型场景和对象运动的ODV数据稀缺的问题。实验证明，OmniDrag在实现ODV生成的整体场景级和细粒度对象级控制方面具有显著优势。项目页面可在https://lwq20020127.github.io/OmniDrag. et.al.|[2412.09623](http://arxiv.org/abs/2412.09623)|null|
|**2024-12-12**|**LoRACLR: Contrastive Adaptation for Customization of Diffusion Models**|文本到图像定制的最新进展实现了高保真、上下文丰富的个性化图像生成，允许特定概念出现在各种场景中。然而，当前的方法难以结合多个个性化模型，这通常会导致属性纠缠或需要单独的训练来保持概念的独特性。我们提出了LoRACLR，这是一种用于多概念图像生成的新方法，它将多个LoRA模型合并到一个统一的模型中，每个模型都针对不同的概念进行了微调，而无需额外的单独微调。LoRACLR使用对比目标来对齐和合并这些模型的权重空间，确保兼容性，同时最大限度地减少干扰。通过为每个概念实施不同但有凝聚力的表示，LoRACLR实现了高效、可扩展的模型组合，以实现高质量、多概念的图像合成。我们的研究结果突出了LoRACLR在准确融合多个概念、提高个性化图像生成能力方面的有效性。 et.al.|[2412.09622](http://arxiv.org/abs/2412.09622)|null|
|**2024-12-12**|**SnapGen: Taming High-Resolution Text-to-Image Models for Mobile Devices with Efficient Architectures and Training**|现有的文本到图像（T2I）扩散模型面临几个局限性，包括模型尺寸大、运行时间慢以及移动设备上的生成质量低。本文旨在通过开发一种极小而快速的T2I模型来解决所有这些挑战，该模型可以在移动平台上生成高分辨率和高质量的图像。我们提出了几种技术来实现这一目标。首先，我们系统地检查了网络架构的设计选择，以减少模型参数和延迟，同时确保高质量的生成。其次，为了进一步提高生成质量，我们从更大的模型中提取跨架构知识，使用多层次方法从头开始指导模型的训练。第三，我们通过将对抗性指导与知识提炼相结合，实现了几步生成。我们的SnapGen型号首次演示了在移动设备上生成1024x1024像素的图像，大约需要1.4秒。在ImageNet-1K上，我们的模型只有372M个参数，对于256x256像素的生成，FID为2.06。在T2I基准测试（即GenEval和DPG Bench）上，我们的模型只有379M个参数，在尺寸小得多的情况下（例如，比SDXL小7倍，比IF-XL小14倍）超过了具有数十亿个参数的大型模型。 et.al.|[2412.09619](http://arxiv.org/abs/2412.09619)|null|
|**2024-12-12**|**EasyRef: Omni-Generalized Group Image Reference for Diffusion Models via Multimodal LLM**|在扩散模型的个性化方面取得了重大成就。传统的无调谐方法大多通过将图像嵌入平均作为注入条件来对多个参考图像进行编码，但这种与图像无关的操作无法在图像之间进行交互，以捕获多个参考中的一致视觉元素。尽管基于调谐的低秩自适应（LoRA）可以通过训练过程有效地提取多个图像中的一致元素，但它需要对每个不同的图像组进行特定的微调。本文介绍了一种新的即插即用自适应方法EasyRef，该方法使扩散模型能够基于多个参考图像和文本提示进行调节。为了有效地利用多幅图像中一致的视觉元素，我们利用了多模态大型语言模型（MLLM）的多图像理解和指令跟踪能力，促使它根据指令捕获一致的视觉要素。此外，通过适配器将MLLM的表示注入扩散过程可以很容易地推广到看不见的领域，挖掘看不见数据中一致的视觉元素。为了降低计算成本并增强细粒度细节的保留，我们引入了一种高效的参考聚合策略和渐进式训练方案。最后，我们介绍了一种新的多参考图像生成基准MRBench。实验结果表明，EasyRef超越了IP-Adapter等无调谐方法和LoRA等基于调谐的方法，在不同领域实现了卓越的美学质量和稳健的零样本泛化。 et.al.|[2412.09618](http://arxiv.org/abs/2412.09618)|null|
|**2024-12-12**|**Context Canvas: Enhancing Text-to-Image Diffusion Models with Knowledge Graph-Based RAG**|我们引入了一种新的方法，通过结合基于图的RAG来增强文本到图像模型的能力。我们的系统从知识图中动态检索详细的字符信息和关系数据，从而生成视觉准确、上下文丰富的图像。这种能力显著改善了现有T2I模型的局限性，由于数据集的限制，这些模型往往难以准确描述复杂或文化特定的主题。此外，我们提出了一种新的文本到图像模型的自校正机制，以确保视觉输出的一致性和保真度，利用图中丰富的上下文来指导校正。我们的定性和定量实验表明，Context Canvas显著增强了Flux、Stable Diffusion和DALL-E等流行模型的功能，并改进了ControlNet在细粒度图像编辑任务中的功能。据我们所知，Context Canvas代表了基于图的RAG在增强T2I模型方面的首次应用，代表了在生成高保真、上下文感知的多面图像方面的重大进步。 et.al.|[2412.09614](http://arxiv.org/abs/2412.09614)|null|
|**2024-12-12**|**LiftImage3D: Lifting Any Single Image to 3D Gaussians with Video Generation Priors**|由于固有的几何模糊性和有限的视点信息，单图像3D重建仍然是计算机视觉中的一个基本挑战。潜在视频扩散模型（LVDM）的最新进展提供了从大规模视频数据中学习的有前景的3D先验。然而，有效地利用这些先验知识面临着三个关键挑战：（1）大型相机运动的质量下降，（2）实现精确相机控制的困难，以及（3）破坏3D一致性的扩散过程固有的几何失真。我们通过提出LiftImage3D来应对这些挑战，该框架有效地释放了LVDM的生成先验，同时确保了3D的一致性。具体来说，我们设计了一种铰接轨迹策略来生成视频帧，该策略将具有大相机运动的视频序列分解为具有可控小运动的视频。然后，我们使用鲁棒的神经匹配模型，即MASt3R，来校准生成帧的相机姿态并生成相应的点云。最后，我们提出了一种失真感知的3D高斯飞溅表示，它可以学习帧之间的独立失真，并输出未失真的规范高斯分布。大量实验表明，LiftImage3D在两个具有挑战性的数据集（即LLFF、DL3DV和坦克与神庙）上实现了最先进的性能，并很好地推广到各种野生图像，从卡通插图到复杂的现实世界场景。 et.al.|[2412.09597](http://arxiv.org/abs/2412.09597)|null|
|**2024-12-12**|**Probing a diffuse flux of axion-like particles from galactic supernovae with neutrino water Cherenkov detectors**|在这篇文章中，我们声称，在核心坍缩超新星（SNe）中，可以以半相对论速度产生具有MeV质量的轴子状粒子（ALP），从而产生弥漫的星系通量。我们证明，这些ALP可以通过 $a\，p\rightarrow p\，\gamma$相互作用在中微子-水切伦科夫探测器中检测到。使用超级神冈数据，我们推导出了ALP参数空间的新约束，不包括ALP质量在1-80美元MeV范围内和ALP质子耦合在6美元×10美元之间的冷却边界以上的ALP质子偶联中跨越一个数量级以上的区域^{-6}-2\×10^{-4}$。我们证明，未来的超级神冈探测器将能够探测小至2美元×10^{-6}$ 的耦合，完全关闭SN 1987A冷却边界以上的允许区域。 et.al.|[2412.09595](http://arxiv.org/abs/2412.09595)|null|
|**2024-12-12**|**Neural LightRig: Unlocking Accurate Object Normal and Material Estimation with Multi-Light Diffusion**|由于其欠约束的性质，从单个图像中恢复对象的几何形状和材质具有挑战性。在本文中，我们提出了神经LightRig，这是一种新的框架，通过利用2D扩散先验的辅助多光照条件来增强内在估计。具体来说，1）我们首先利用大规模扩散模型中的照明先验，在具有专用设计的合成再照明数据集上构建我们的多光扩散模型。该扩散模型生成多个一致的图像，每个图像由不同方向的点光源照射。2） 通过使用这些不同的光照图像来降低估计的不确定性，我们训练了一个具有U-Net骨干的大型G缓冲区模型，以准确预测表面法线和材料。大量实验证实，我们的方法明显优于最先进的方法，能够实现精确的表面法线和PBR材料估计，并具有生动的重新照明效果。代码和数据集可在我们的项目页面上找到，网址为https://projects.zxhezexin.com/neural-lightrig. et.al.|[2412.09593](http://arxiv.org/abs/2412.09593)|null|

<p align=right>(<a href=#updated-on-20241215>back to top</a>)</p>

## NeRF

|Publish Date|Title|Abstract|PDF|Code|
|---|---|---|---|---|
|**2024-12-12**|**Mixture of neural fields for heterogeneous reconstruction in cryo-EM**|低温电子显微镜（Cryo-EM）是一种用于蛋白质结构测定的实验技术，可以在接近生理环境的情况下对大分子的集合进行成像。虽然最近的进展能够重建单个生物分子复合物的动态构象，但目前的方法并不能充分模拟具有混合构象和成分异质性的样品。特别是，包含多种蛋白质混合物的数据集需要联合推断结构、姿势、组成类别和构象状态以进行3D重建。在这里，我们提出了Hydra，这是一种通过参数化K个神经场之一产生的结构来完全从头计算模拟构象和组成异质性的方法。我们采用了一种新的基于似然的损失函数，并证明了我们的方法在由具有高度构象变异的蛋白质混合物组成的合成数据集上的有效性。我们还在含有不同蛋白质复合物混合物的细胞裂解物的实验数据集上演示了Hydra。Hydra扩展了非均匀重建方法的表现力，从而将冷冻EM的范围扩大到越来越复杂的样本。 et.al.|[2412.09420](http://arxiv.org/abs/2412.09420)|null|
|**2024-12-11**|**From MLP to NeoMLP: Leveraging Self-Attention for Neural Fields**|神经场（NeFs）最近已成为编码各种模态时空信号的最先进方法。尽管NeFs在重建单个信号方面取得了成功，但它们作为下游任务（如分类或分割）中的表示，除了缺乏强大和可扩展的调节机制外，还受到参数空间及其潜在对称性的复杂性的阻碍。在这项工作中，我们从连接主义的原则中汲取灵感，设计了一种基于MLP的新架构，我们称之为NeoMLP。我们从一个被视为图的MLP开始，将其从一个多部分图转换为一个包含输入、隐藏和输出节点的完整图，并配备了高维特征。我们在这个图上执行消息传递，并在所有节点之间通过自我关注进行权重共享。NeoMLP具有通过隐藏和输出节点进行调节的内置机制，这些节点充当一组潜在代码，因此，NeoMLP可以直接用作条件神经场。我们通过拟合高分辨率信号（包括多模态视听数据）来证明我们的方法的有效性。此外，我们通过使用单个骨干架构学习特定于实例的潜在代码集来拟合神经表示的数据集，然后将它们用于下游任务，优于最近最先进的方法。源代码开源于https://github.com/mkofinas/neomlp. et.al.|[2412.08731](http://arxiv.org/abs/2412.08731)|**[link](https://github.com/mkofinas/neomlp)**|
|**2024-12-11**|**Combining Neural Fields and Deformation Models for Non-Rigid 3D Motion Reconstruction from Partial Data**|我们介绍了一种新的数据驱动方法，用于从非刚性变形形状的非结构化和潜在的部分观测中重建时间相干的3D运动。我们的目标是为经历近等距变形的形状（如穿着宽松衣服的人）实现高保真运动重建。我们工作的关键新颖之处在于它能够将隐式形状表示与显式基于网格的变形模型相结合，从而在不依赖于参数化形状模型或解耦形状和运动的情况下实现详细和时间连贯的运动重建。每一帧都表示为从特征空间解码的神经场，在特征空间中，随着时间的推移，观测值被融合在一起，从而保留了输入数据中存在的几何细节。时间连贯性是通过应用于神经场中基础表面的相邻帧之间的近等距变形约束来实现的。我们的方法优于最先进的方法，正如它在从单眼深度视频重建的人类和动物运动序列中的应用所证明的那样。 et.al.|[2412.08511](http://arxiv.org/abs/2412.08511)|null|
|**2024-12-08**|**Unsupervised Multi-Parameter Inverse Solving for Reducing Ring Artifacts in 3D X-Ray CBCT**|由于X射线探测器的非理想响应，环形伪影在3D锥束计算机断层扫描（CBCT）中很普遍，严重降低了成像质量和可靠性。当前最先进的（SOTA）环伪影减少（RAR）算法依赖于广泛的成对CT样本进行监督学习。虽然有效，但这些方法并不能完全捕捉到环形伪影的物理特征，导致应用于域外数据时性能明显下降。此外，它们在3D CBCT中的应用受到高内存需求的限制。在这项工作中，我们介绍了\textbf{Riner}，这是一种将3D CBCT RAR表述为多参数逆问题的无监督方法。我们的核心创新是将X射线探测器响应参数化为微分物理模型中的可解变量。通过联合优化神经场以表示无伪影的CT图像，并直接从原始测量值估计响应参数，Riner消除了对外部训练数据的需求。此外，它还可适应不同的CT几何形状，提高了实用性。在模拟和真实数据集上的实证结果表明，Riner在性能上优于现有的SOTA RAR方法。 et.al.|[2412.05853](http://arxiv.org/abs/2412.05853)|null|
|**2024-12-06**|**Physics-informed reduced order model with conditional neural fields**|本研究提出了用于降阶建模（CNF-ROM）框架的条件神经场，以近似参数化偏微分方程（PDE）的解。该方法将用于随时间建模潜在动力学的参数神经ODE（PNODE）与从相应潜在状态重建PDE解的解码器相结合。我们为CNF-ROM引入了一个物理知情学习目标，其中包括两个关键组成部分。首先，该框架使用基于坐标的神经网络通过自动微分计算空间导数并应用时间导数的链式规则来计算和最小化PDE残差。其次，使用近似距离函数（ADF）施加精确的初始和边界条件（IC/BC）[Sukumar和Srivastava，CMAME，2022]。然而，当ADFs的二阶或高阶导数在边界的连接点处变得不稳定时，ADFs引入了一种权衡。为了解决这个问题，我们引入了一个受[Gladstone等人，NeurIPS ML4PS研讨会，2022年]启发的辅助网络。我们的方法通过参数外推和插值、时间外推以及与解析解的比较得到了验证。 et.al.|[2412.05233](http://arxiv.org/abs/2412.05233)|null|
|**2024-12-06**|**Spatially-Adaptive Hash Encodings For Neural Surface Reconstruction**|位置编码是神经场景重建方法的一个常见组成部分，它提供了一种将神经场的学习偏向于更粗糙或更精细表示的方法。当前的神经表面重建方法使用“一刀切”的编码方法，在所有场景中选择一组固定的编码函数，从而产生偏差。当前最先进的表面重建方法利用基于网格的多分辨率哈希编码来恢复高细节几何。我们提出了一种学习方法，通过掩盖以单独网格分辨率存储的特征的贡献，允许网络根据空间选择其编码基础。由此产生的空间自适应方法允许网络在不引入噪声的情况下适应更宽的频率范围。我们在标准基准曲面重建数据集上测试了我们的方法，并在两个基准数据集上实现了最先进的性能。 et.al.|[2412.05179](http://arxiv.org/abs/2412.05179)|null|
|**2024-12-06**|**DNF: Unconditional 4D Generation with Dictionary-based Neural Fields**|虽然通过基于扩散的形状3D生成模型取得了显著成功，但由于物体变形的复杂性，4D生成建模仍然具有挑战性。我们提出了DNF，这是一种用于无条件生成建模的新4D表示，它有效地对具有解纠缠形状和运动的可变形形状进行建模，同时捕获变形对象中的高保真细节。为了实现这一点，我们提出了一种字典学习方法，将4D运动与形状作为神经场进行分离。形状和运动都表示为学习潜在空间，其中每个可变形形状由其形状和运动全局潜在码、形状特定系数向量和共享字典信息表示。这在学习词典中捕获了特定形状的细节和全局共享信息。我们基于字典的表示法很好地平衡了保真度、连续性和压缩性——结合基于变换器的扩散模型，我们的方法能够生成有效、高保真的4D动画。 et.al.|[2412.05161](http://arxiv.org/abs/2412.05161)|null|
|**2024-12-04**|**Theoretical / numerical study of modulated traveling waves in inhibition stabilized networks**|我们证明了实线上神经场方程行波解的线性化稳定性原理。此外，我们提供了行波附近有限维不变中心流形的存在性，这使得研究行波的分叉成为可能。最后，研究了调制行波的光谱特性。提供了计算调制行波的数值方案。然后，我们将这些结果和方法应用于研究抑制稳定状态下的神经场模型。我们展示了行进脉冲的Fold、Hopf和Bodgdanov-Takens分叉。此外，我们继续将调制行进脉冲作为两个神经群体时间尺度比的函数，并展示了调制行进脉冲蜿蜒的数值证据。 et.al.|[2412.03613](http://arxiv.org/abs/2412.03613)|null|
|**2024-12-04**|**Sparse-view Pose Estimation and Reconstruction via Analysis by Generative Synthesis**|推断一组多视图图像背后的3D结构通常需要解决两个相互依赖的任务——精确的3D重建需要精确的相机姿态，预测相机姿态依赖于（隐式或显式）对底层3D进行建模。经典的综合分析框架将这一推断视为一种联合优化，旨在解释观察到的像素，最近的实例通过基于梯度下降的初始姿态估计的姿态细化来学习表达性的3D表示（例如神经场）。然而，给定一组稀疏的观测视图，观测可能无法提供足够的直接证据来获得完整准确的3D。此外，姿势估计中的大误差可能不容易纠正，并可能进一步降低推断的3D。为了在这种具有挑战性的设置中实现稳健的3D重建和姿态估计，我们提出了SparseAGS，这是一种通过以下方式调整这种综合分析方法的方法：a）将基于新视图合成的生成先验与光度目标结合起来，以提高推断的3D的质量，b）明确地推理异常值，并使用基于连续优化策略的离散搜索来纠正它们。我们结合几个现成的姿态估计系统，在真实世界和合成数据集中验证我们的框架作为初始化。我们发现，它显著提高了基础系统的姿态精度，同时产生了高质量的3D重建，其效果优于当前多视图重建基线的结果。 et.al.|[2412.03570](http://arxiv.org/abs/2412.03570)|null|
|**2024-12-04**|**RoDyGS: Robust Dynamic Gaussian Splatting for Casual Videos**|动态视图合成（DVS）近年来取得了显著进展，在降低计算成本的同时实现了高保真渲染。尽管取得了进展，但从休闲视频中优化动态神经场仍然具有挑战性，因为这些视频不提供直接的3D信息，如相机轨迹或底层场景几何形状。在这项工作中，我们介绍了RoDyGS，这是一个用于从休闲视频中动态高斯散布的优化管道。它通过分离动态和静态图元有效地学习场景的运动和底层几何，并通过结合运动和几何正则化项确保学习到的运动和几何在物理上是合理的。我们还介绍了一个全面的基准测试Kubric MRig，它提供了广泛的相机和物体运动以及同时的多视图捕捉，这是以前基准测试中没有的功能。实验结果表明，与现有的无姿态静态神经场相比，所提出的方法明显优于之前的无姿态动态神经场，并实现了具有竞争力的渲染质量。代码和数据可在以下网址公开获取https://rodygs.github.io/. et.al.|[2412.03077](http://arxiv.org/abs/2412.03077)|null|

<p align=right>(<a href=#updated-on-20241215>back to top</a>)</p>

[contributors-shield]: https://img.shields.io/github/contributors/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[contributors-url]: https://github.com/Vincentqyw/cv-arxiv-daily/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[forks-url]: https://github.com/Vincentqyw/cv-arxiv-daily/network/members
[stars-shield]: https://img.shields.io/github/stars/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[stars-url]: https://github.com/Vincentqyw/cv-arxiv-daily/stargazers
[issues-shield]: https://img.shields.io/github/issues/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[issues-url]: https://github.com/Vincentqyw/cv-arxiv-daily/issues

