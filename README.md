[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]

## Updated on 2024.04.16
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
|**2024-04-12**|**MonoPatchNeRF: Improving Neural Radiance Fields with Patch-based Monocular Guidance**|最新的正则化神经辐射场（NeRF）方法对多视点立体（MVS）基准（如ETH3D）产生了较差的几何和视图外推。在本文中，我们的目标是创建提供精确几何和视图合成的3D模型，部分弥补NeRF和传统MVS方法之间的巨大几何性能差距。我们提出了一种基于补丁的方法，该方法可以有效地利用单目表面法线和相对深度预测。基于补丁的射线采样还实现了随机采样的虚拟视图和训练视图之间的归一化互相关（NCC）和结构相似性（SSIM）的外观正则化。我们进一步证明，基于运动点稀疏结构的“密度限制”可以帮助大大提高几何精度，而新的视图合成指标略有下降。我们的实验显示，RegNeRF的性能是其平均性能的4倍，FreeNeRF的平均性能是其8倍F1@2cm针对ETH3D MVS基准，提出了一个富有成果的研究方向，以提高基于NeRF的模型的几何精度，并揭示了一种潜在的未来方法，使基于NeRF优化最终优于传统MVS。 et.al.|[2404.08252](http://arxiv.org/abs/2404.08252)|null|
|**2024-04-11**|**Boosting Self-Supervision for Single-View Scene Completion via Knowledge Distillation**|通过运动结构从图像中推断场景几何是计算机视觉中一个长期存在的基本问题。虽然经典方法和最近的深度图预测只关注场景的可见部分，但场景完成的任务旨在推理几何体，即使在遮挡区域也是如此。随着神经辐射场（NeRFs）的普及，通过预测所谓的密度场，隐式表示也开始流行于场景完成。与明确的方法不同。例如，基于体素的方法、密度场也允许通过基于图像的渲染进行准确的深度预测和新颖的视图合成。在这项工作中，我们建议将多个图像的场景重建融合起来，并将这些知识提取到更准确的单视图场景重建中。为此，我们提出了多视图幕后（MVBTS）来融合来自多个姿势图像的密度场，仅根据图像数据进行完全自监督训练。使用知识提取，我们使用MVBTS通过称为KDBTS的直接监督来训练单视图场景完成网络。它在占用预测方面实现了最先进的性能，尤其是在遮挡区域。 et.al.|[2404.07933](http://arxiv.org/abs/2404.07933)|**[link](https://github.com/keonhee-han/KDBTS)**|
|**2024-04-11**|**G-NeRF: Geometry-enhanced Novel View Synthesis from Single-View Images**|新颖的视图合成旨在生成给定视图图像集合的新视图图像。最近的尝试依靠从多视图图像中学习的3D几何先验（例如，形状、大小和位置）来解决这个问题。然而，这种方法遇到以下限制：1）它们需要一组多视图图像作为特定场景（例如，人脸、汽车或椅子）的训练数据，而这在许多现实世界场景中往往是不可用的；2） 由于缺乏多视点监督，它们无法从单视点图像中提取几何先验。在本文中，我们提出了一种几何增强NeRF（G-NeRF），它试图通过几何引导的多视图合成方法来增强几何先验，然后进行深度感知训练。在合成过程中，受现有3D GAN模型可以无条件合成高保真多视图图像的启发，我们寻求采用现成的3D GAN模式，如EG3D，作为自由源，通过合成多视图数据来提供几何先验。同时，为了进一步提高合成数据的几何质量，我们引入了一种截断方法来有效地对3D GAN模型中的潜在代码进行采样。为了解决单视图图像缺乏多视图监督的问题，我们设计了深度感知训练方法，结合了深度感知鉴别器来引导几何先验通过深度图。实验证明了我们的方法在定性和定量结果方面的有效性。 et.al.|[2404.07474](http://arxiv.org/abs/2404.07474)|**[link](https://github.com/llrtt/G-NeRF)**|
|**2024-04-10**|**Self-supervised Monocular Depth Estimation on Water Scenes via Specular Reflection Prior**|由于没有足够的可靠线索作为先验知识，从单个图像进行单目深度估计对于计算机视觉来说是一个不适定的问题。除了帧间监督（即立体帧和相邻帧）之外，在同一帧中可以获得广泛的先验信息。来自镜面的反射，信息丰富的帧内先验，使我们能够将不适定深度估计任务重新表述为多视图合成。本文提出了第一种通过帧内先验进行水场景深度估计的自监督，即反射监督和几何约束。在第一阶段，执行水分割网络以从整个图像中分离反射分量。接下来，我们构建了一个自我监督的框架，从反射和其他角度来预测目标的外观。结合SmoothL1和一种新颖的光度自适应SSIM，建立了光度重投影误差公式，通过对齐变换后的虚拟深度和源深度来优化姿态和深度估计。作为补充，水面是根据真实和虚拟相机位置确定的，这与水域的深度互补。此外，为了减轻这些费力的地面实况注释，我们引入了从虚幻引擎4渲染的大规模水反射场景（WRS）数据集。在WRS数据集上进行的大量实验证明了与最先进的深度估计技术相比，所提出的方法的可行性。 et.al.|[2404.07176](http://arxiv.org/abs/2404.07176)|null|
|**2024-04-12**|**SpikeNVS: Enhancing Novel View Synthesis from Blurry Images via Spike Camera**|使用神经辐射场（NeRF）和三维高斯散射（3DGS）等神经场方法实现清晰的新视图合成（NVS）的最关键因素之一是训练图像的质量。然而，传统的RGB相机容易受到运动模糊的影响。相比之下，像事件和尖峰相机这样的神经形态相机固有地捕捉更全面的时间信息，这可以作为额外的训练数据提供场景的清晰表示。最近的方法已经探索了集成事件摄像机以提高NVS的质量。事件RGB方法有一些局限性，例如高昂的培训成本和无法在后台有效工作。相反，我们的研究引入了一种新的方法，使用尖峰相机来克服这些限制。通过将尖峰流的纹理重建视为基本事实，我们设计了尖峰纹理（TfS）损失。由于尖峰摄像机依赖于时间积分，而不是事件摄像机使用的时间微分，我们提出的TfS损失保持了可管理的训练成本。它同时处理前景对象和背景。我们还提供了用spike RGB相机系统拍摄的真实世界数据集，以促进未来的研究工作。我们使用合成和真实世界的数据集进行了广泛的实验，以证明我们的设计可以增强NeRF和3DGS的新视图合成。代码和数据集将提供给公众访问。 et.al.|[2404.06710](http://arxiv.org/abs/2404.06710)|null|
|**2024-04-14**|**3D Geometry-aware Deformable Gaussian Splatting for Dynamic View Synthesis**|在本文中，我们提出了一种用于动态视图合成的3D几何感知可变形高斯散射方法。现有的基于神经辐射场（NeRF）的解决方案以隐含的方式学习变形，而这种方式不能结合3D场景几何。因此，所学习的变形不一定是几何相干的，这导致了不令人满意的动态视图合成和3D动态重建。最近，3D高斯飞溅提供了3D场景的新表示，在此基础上可以利用3D几何来学习复杂的3D变形。具体而言，场景被表示为3D高斯的集合，其中每个3D高斯被优化为随着时间的推移移动和旋转，以对变形进行建模。为了在变形过程中加强3D场景几何约束，我们显式地提取3D几何特征，并将其集成到学习3D变形中。通过这种方式，我们的解决方案实现了3D几何感知变形建模，从而改进了动态视图合成和3D动态重建。在合成数据集和真实数据集上的大量实验结果证明了我们的解决方案的优越性，它实现了最先进的性能。该项目位于https://npucvr.github.io/GaGS/ et.al.|[2404.06270](http://arxiv.org/abs/2404.06270)|null|
|**2024-04-09**|**HFNeRF: Learning Human Biomechanic Features with Neural Radiance Fields**|在新视图合成的最新进展中，应用于人类受试者的基于可推广神经辐射场（NeRF）的方法在从少量图像生成新视图方面显示出显著的结果。但是，这种泛化能力无法捕捉所有实例共享的骨架的基本结构特征。在此基础上，我们介绍了HFNeRF：一种新的可推广的人体特征NeRF，旨在使用预训练的图像编码器生成人体生物力学特征。尽管先前的人类NeRF方法在生成照片真实感虚拟化身方面显示出了有希望的结果，但这种方法缺乏对包括增强现实（AR）/虚拟现实（VR）在内的下游应用至关重要的潜在人类结构或生物力学特征，如骨骼或关节信息。HFNeRF利用2D预训练的基础模型，使用神经渲染在3D中学习人类特征，然后使用体积渲染生成2D特征图。我们通过预测热图作为特征来评估骨架估计任务中的HFNeRF。所提出的方法是完全可微的，可以同时成功地学习颜色、几何和人体骨骼。本文介绍了HFNeRF的初步结果，说明了它在使用NeRF生成具有生物力学特征的逼真虚拟化身方面的潜力。 et.al.|[2404.06152](http://arxiv.org/abs/2404.06152)|null|
|**2024-04-09**|**Gaussian Pancakes: Geometrically-Regularized 3D Gaussian Splatting for Realistic Endoscopic Reconstruction**|在结直肠癌癌症诊断中，传统的结肠镜检查技术面临着严重的局限性，包括视野有限和缺乏深度信息，这可能会阻碍癌前病变的检测。目前的方法难以提供全面准确的结肠表面3D重建，这有助于最大限度地减少缺失区域并重新检查癌前息肉。为此，我们介绍了“高斯煎饼”，这是一种利用3D高斯散射（3D GS）与基于递归神经网络的同时定位和映射（RNNSLAM）系统相结合的方法。通过在3D GS框架中引入几何和深度正则化，我们的方法确保了高斯与结肠表面的更准确对齐，从而实现更平滑的3D重建，并能新颖地查看详细的纹理和结构。对三个不同数据集的评估表明，高斯煎饼增强了新的视图合成质量，超过了当前领先的方法，PSNR提高了18%，SSIM提高了16%。它还提供了超过100倍的渲染速度和超过10倍的训练时间，使其成为实时应用程序的实用工具。因此，这有望实现临床转化，更好地检测和诊断结直肠癌癌症。 et.al.|[2404.06128](http://arxiv.org/abs/2404.06128)|**[link](https://github.com/smbonilla/gaussianpancakes)**|
|**2024-04-09**|**Revising Densification in Gaussian Splatting**|在本文中，我们解决了自适应密度控制（ADC）在三维高斯散射（3DGS）中的局限性，3DGS是一种为新视图合成实现高质量、真实感结果的场景表示方法。ADC已被引入用于自动3D点基元管理，控制致密化和修剪，然而，在致密化逻辑中存在一定的局限性。我们的主要贡献是为3DGS中的密度控制提供了一种更原则的、像素误差驱动的公式，利用辅助的每像素误差函数作为致密化的标准。我们进一步引入了一种机制来控制每个场景生成的基元的总数，并在克隆操作期间校正ADC当前不透明度处理策略中的偏差。我们的方法在不牺牲方法效率的情况下，在各种基准场景中实现了一致的质量改进。 et.al.|[2404.06109](http://arxiv.org/abs/2404.06109)|null|
|**2024-04-09**|**Incremental Joint Learning of Depth, Pose and Implicit Scene Representation on Monocular Camera in Large-scale Scenes**|用于照片真实感视图合成的密集场景重建具有多种应用，如VR/AR、自动驾驶汽车。然而，由于三个核心挑战，大多数现有方法在大规模场景中都存在困难：\textit｛（a）不准确的深度输入。｝在真实世界的大规模场景中不可能获得准确的深度输出。\textit｛（b）不准确的姿势估计。｝大多数现有方法都依赖于准确的预先估计的相机姿势。\textit｛（c）场景表示能力不足。｝单个全局辐射场缺乏有效扩展到大规模场景的能力。为此，我们提出了一种增量联合学习框架，可以实现精确的深度、姿态估计和大规模场景重建。采用基于视觉变换器的网络作为骨干，以提高尺度信息估计的性能。对于姿态估计，设计了一种特征度量束调整（FBA）方法，用于在大规模场景中精确和稳健的相机跟踪。在隐式场景表示方面，我们提出了一种增量场景表示方法，将整个大规模场景构建为多个局部辐射场，以增强3D场景表示的可扩展性。已经进行了扩展实验来证明我们的方法在深度估计、姿态估计和大规模场景重建中的有效性和准确性。 et.al.|[2404.06050](http://arxiv.org/abs/2404.06050)|null|

<p align=right>(<a href=#updated-on-20240416>back to top</a>)</p>

## 3D Reconstruction

|Publish Date|Title|Abstract|PDF|Code|
|---|---|---|---|---|
|**2024-04-12**|**EventEgo3D: 3D Human Motion Capture from Egocentric Event Streams**|以单目自我为中心的三维人体运动捕捉是一个具有挑战性和积极研究的问题。现有的方法使用同步操作的视觉传感器（例如RGB相机），并且在低照明和快速运动下经常失败，这在涉及头戴式设备的许多应用中可能受到限制。针对现有的局限性，本文1）介绍了一个新问题，即使用鱼眼镜头的以自我为中心的单目事件相机进行三维人体运动捕捉，2）提出了第一种称为EventEgo3D（EE3D）的方法。事件流具有高的时间分辨率，并在高速人体运动和快速变化的照明下为3D人体运动捕捉提供可靠的提示。所提出的EE3D框架专门针对LNES表示中的事件流进行学习而定制，从而实现高3D重建精度。我们还设计了一个带有事件相机的移动头戴式设备的原型，并记录了一个真实的数据集，其中包含事件观测和真实的3D人体姿势（除了合成数据集）。我们的EE3D在各种具有挑战性的实验中展示了与现有解决方案相比的稳健性和卓越的3D精度，同时支持140Hz的实时3D姿态更新率。 et.al.|[2404.08640](http://arxiv.org/abs/2404.08640)|**[link](https://github.com/Chris10M/EventEgo3D)**|
|**2024-04-12**|**No Bells, Just Whistles: Sports Field Registration by Leveraging Geometric Properties**|传统上，广播运动场配准被视为单应性估计任务，将可见图像区域映射到平面场模型，主要集中在主摄像机镜头上。针对以前方法的缺点，我们提出了一种新的校准管道，可以使用3D足球场模型进行相机校准，并扩展该过程以评估广播视频的多视图性质。我们的方法从SoccerNet数据集注释派生的关键点生成管道开始，利用法庭的几何特性。随后，我们以极简的方式通过DLT算法执行经典的相机校准，而无需进一步细化。通过在真实世界的足球广播数据集（如SoccerNet Calibration、WorldCup 2014和TS-WorldCup）上进行广泛的实验，我们的方法在多视图和单视图3D相机校准方面都表现出了卓越的性能，同时与最先进的技术相比，在单应性估计方面保持了有竞争力的结果。 et.al.|[2404.08401](http://arxiv.org/abs/2404.08401)|null|
|**2024-04-11**|**Multi-view Aggregation Network for Dichotomous Image Segmentation**|最近，二分图像分割（DIS）朝着从高分辨率自然图像中进行高精度对象分割的方向发展。在设计有效的DIS模型时，主要的挑战是如何平衡高分辨率目标在小感受野中的语义分散和在大感受野中高精度细节的损失。现有的方法依赖于繁琐的多个编码器-解码器流和阶段来逐步完成全局定位和局部细化。人类视觉系统通过从多个视角观察感兴趣的区域来捕捉这些区域。受其启发，我们将DIS建模为一个多视图对象感知问题，并提供了一个简约的多视图聚合网络（MVANet），该网络通过一个编码器-解码器结构将远景和近景的特征融合统一为一个流。在所提出的多视图互补定位和细化模块的帮助下，我们的方法在多个视图之间建立了长距离、深刻的视觉交互，使详细特写视图的特征能够集中在高度细长的结构上。在流行的DIS-5K数据集上的实验表明，我们的MVANet在准确性和速度方面都显著优于最先进的方法。源代码和数据集将在\href公开{https://github.com/qianyu-dlut/MVANet}｛MVANet｝。 et.al.|[2404.07445](http://arxiv.org/abs/2404.07445)|**[link](https://github.com/qianyu-dlut/mvanet)**|
|**2024-04-10**|**RealmDreamer: Text-Driven 3D Scene Generation with Inpainting and Depth Diffusion**|我们介绍了RealmDreamer，这是一种从文本描述中生成通用前向3D场景的技术。我们的技术优化了3D高斯飞溅表示，以匹配复杂的文本提示。我们通过利用最先进的文本到图像生成器来初始化这些飞溅，将其样本提升到3D中，并计算遮挡体积。然后，我们将这种跨多个视图的表示优化为具有图像条件扩散模型的3D修复任务。为了学习正确的几何结构，我们通过对修复模型中的样本进行处理，引入了深度扩散模型，从而提供了丰富的几何结构。最后，我们使用来自图像生成器的锐化样本来微调模型。值得注意的是，我们的技术不需要视频或多视图数据，可以合成由多个对象组成的不同风格的各种高质量3D场景。其通用性还允许从单个图像进行3D合成。 et.al.|[2404.07199](http://arxiv.org/abs/2404.07199)|null|
|**2024-04-10**|**PACP: Priority-Aware Collaborative Perception for Connected and Autonomous Vehicles**|对于联网和自动驾驶汽车（CAV）的安全驾驶来说，周围的感知是至关重要的，其中鸟瞰图已被用于准确捕捉车辆之间的空间关系。然而，纯电动汽车的严重固有局限性，如盲点，已经被发现。协作感知已经成为通过从周围车辆的多个视图进行数据融合来克服这些限制的有效解决方案。虽然大多数现有的协作感知策略都采用了基于传输公平性的全连通图，但由于信道变化和感知冗余，它们往往忽略了单个车辆的不同重要性。为了应对这些挑战，我们提出了一种新的优先级感知协作感知（PACP）框架，以采用BEV匹配机制，根据附近CAV和自我感知载体之间的相关性来确定优先级。通过利用子模块优化，我们可以找到接近最优的传输速率、链路连接和压缩度量。此外，我们部署了一种基于深度学习的自适应自动编码器，以在动态信道条件下调制图像重建质量。最后，我们进行了广泛的研究，并证明我们的方案在交集和并集的效用和精度方面分别显著优于最先进的方案8.27%和13.60%。 et.al.|[2404.06891](http://arxiv.org/abs/2404.06891)|null|
|**2024-04-10**|**MonoSelfRecon: Purely Self-Supervised Explicit Generalizable 3D Reconstruction of Indoor Scenes from Monocular RGB Views**|当前的单目3D场景重建（3DR）工作要么是完全监督的，要么是不可推广的，要么隐含在3D表示中。我们提出了一种新的框架——MonoSelfRecon，它首次通过对体素SDF（有符号距离函数）的纯自监督，实现了具有单目RGB视图的可推广室内场景的显式3D网格重建。MonoSelfRecon遵循基于自动编码器的架构，解码体素SDF和可推广的神经辐射场（NeRF），用于指导体素SDF进行自我监督。我们提出了新的自监督损失，它不仅支持纯粹的自监督，而且可以与监督信号一起使用，以进一步增强监督训练。我们的实验表明，在纯自我监督中训练的“MonoSelfRecon”优于当前最好的自我监督室内深度估计模型，并且与在具有深度注释的完全监督中训练出的3DR模型相当。MonoSelfRecon不受特定模型设计的限制，它可以用于任何具有体素SDF的模型，用于纯自我监督的方式。 et.al.|[2404.06753](http://arxiv.org/abs/2404.06753)|null|
|**2024-04-10**|**Binomial Self-compensation for Motion Error in Dynamic 3D Scanning**|相移轮廓术（PSP）由于其高精度、鲁棒性和逐像素性，在高精度三维扫描中备受青睐。然而，在动态测量中违反了PSP的基本假设，即物体应该保持静止，这使得PSP容易受到物体移动的影响，从而导致点云中的波纹状误差。我们提出了一种逐像素和逐帧的可循环二项式自补偿（BSC）算法，以有效灵活地消除四步PSP中的运动误差。我们的数学模型表明，通过对由二项式系数加权的连续受运动影响的相位帧求和，运动误差随着二项式阶数的增加而呈指数级减小，从而在没有任何中间变量帮助的情况下，通过受运动影响的相位序列实现自动误差补偿。大量实验表明，我们的BSC在降低运动误差方面优于现有方法，同时实现了与相机采集速率（90fps）相等的深度图帧速率，实现了准单次拍摄帧速率的高精度3D重建。 et.al.|[2404.06693](http://arxiv.org/abs/2404.06693)|null|
|**2024-04-09**|**Laue Indexing with Optimal Transport**|Laue层析成像实验从多个视角下记录的衍射图中检索多晶样品中晶粒的位置和取向。使用宽波长光谱光束可以大大减少实验时间，但对多晶样品中衍射峰的索引提出了困难的挑战；不存在关于这些布拉格峰的波长的信息，并且来自多个晶粒的衍射图案被叠加。到目前为止，还不存在能够有效地索引具有超过大约500个晶粒的样本的算法。为了满足这一需求，我们提出了一种新的方法：最优传输的Laue索引（LaueOT）。我们创建了多粒度索引问题的概率描述，并提出了一种基于辛霍恩期望最大化方法的解决方案，由于使用最优传输计算分配，该方法可以有效地找到可能性的最大值。这是一个非凸优化问题，其中粒子的方向和位置与粒子到点的分配同时优化，同时稳健地处理异常值。优化问题中要考虑的初始原型晶粒的选择也在最优传输框架内计算。LaueOT可以在不到30分钟的时间内在单个大内存GPU上快速有效地索引多达1000个晶粒。我们展示了LaueOT在具有可变晶粒数量、点位置测量噪声水平和异常分数的模拟上的性能。在我们的实验中，即使对于高噪声水平和高达70%的异常值，该算法也能恢复正确数量的颗粒。我们将LaueOT索引的结果与现有算法进行了比较，无论是对来自特征良好样品的合成中子衍射数据还是真实中子衍射数据。 et.al.|[2404.06478](http://arxiv.org/abs/2404.06478)|**[link](https://github.com/laueot/laueotx)**|
|**2024-04-09**|**Gaussian Pancakes: Geometrically-Regularized 3D Gaussian Splatting for Realistic Endoscopic Reconstruction**|在结直肠癌癌症诊断中，传统的结肠镜检查技术面临着严重的局限性，包括视野有限和缺乏深度信息，这可能会阻碍癌前病变的检测。目前的方法难以提供全面准确的结肠表面3D重建，这有助于最大限度地减少缺失区域并重新检查癌前息肉。为此，我们介绍了“高斯煎饼”，这是一种利用3D高斯散射（3D GS）与基于递归神经网络的同时定位和映射（RNNSLAM）系统相结合的方法。通过在3D GS框架中引入几何和深度正则化，我们的方法确保了高斯与结肠表面的更准确对齐，从而实现更平滑的3D重建，并能新颖地查看详细的纹理和结构。对三个不同数据集的评估表明，高斯煎饼增强了新的视图合成质量，超过了当前领先的方法，PSNR提高了18%，SSIM提高了16%。它还提供了超过100倍的渲染速度和超过10倍的训练时间，使其成为实时应用程序的实用工具。因此，这有望实现临床转化，更好地检测和诊断结直肠癌癌症。 et.al.|[2404.06128](http://arxiv.org/abs/2404.06128)|**[link](https://github.com/smbonilla/gaussianpancakes)**|
|**2024-04-09**|**Estimating the lateral speed of a fast shock driven by a coronal mass ejection at the location of solar radio emissions**|快速日冕物质抛射（CME）可以驱动能够将电子加速到高能的冲击波。这些冲击加速的电子充当电磁辐射源，通常以太阳射电暴的形式出现。最近的发现表明，太阳射电暴的无线电成像可以提供一种方法来估计低日冕中CME和相关冲击的横向扩展。我们的目标是使用多个视角的冲击波三维重建来估计日冕物质抛射驱动的冲击在无线电发射位置的膨胀速度。我们使用Nan\c的无线电成像来估计无线电发射的3D位置{c}ay日射图和冲击的3D位置。使用日地关系天文台、太阳动力学天文台以及太阳和日球层天文台的白光和极紫外CME图像重建了3D冲击。然后，使用冲击表面上无线电发射的近似3D位置来估计CME驱动的冲击在电子加速位置的横向膨胀速度。与CME相关的射电暴被发现位于CME驱动的不断扩大的冲击的侧面。我们在两个不同的位置确定了两个显著的无线电源，并发现在这些位置，冲击的横向速度在800-1000美元的范围内。在喷发的早期阶段，如此高的速度已经表明低日冕中存在快速冲击。我们还发现，与在电晕中获得的值相比，径向和横向膨胀速度之间的比率更大。所获得的高冲击速度指示在喷发的初始阶段期间的快速加速度。这种加速度很可能是导致公制无线电发射（如II型无线电爆发）存在的关键参数之一。 et.al.|[2404.06102](http://arxiv.org/abs/2404.06102)|null|

<p align=right>(<a href=#updated-on-20240416>back to top</a>)</p>

## Diffusion

|Publish Date|Title|Abstract|PDF|Code|
|---|---|---|---|---|
|**2024-04-12**|**Lossy Image Compression with Foundation Diffusion Models**|在图像压缩域中结合扩散模型有可能产生逼真和详细的重建，尤其是在极低的比特率下。先前的方法侧重于使用扩散模型作为对调节信号中的量化误差具有鲁棒性的表达解码器，然而以这种方式实现有竞争力的结果需要对扩散模型进行昂贵的训练，并且由于迭代生成过程而需要长的推理时间。在这项工作中，我们将量化误差的去除公式化为去噪任务，使用扩散来恢复传输图像中丢失的信息。我们的方法允许我们执行不到10%的完整扩散生成过程，并且不需要对扩散模型进行架构更改，从而能够将基础模型用作强大的先验，而无需对主干进行额外的微调。我们提出的编解码器在量化真实性度量方面优于以前的方法，并且我们验证了我们的重建在质量上受到最终用户的青睐，即使其他方法使用两倍的比特率。 et.al.|[2404.08580](http://arxiv.org/abs/2404.08580)|null|
|**2024-04-12**|**Functional reducibility of higher-order networks**|人们普遍认为，经验复杂系统的特征不仅在于成对的相互作用，还在于影响从代谢反应到流行病等集体现象的高阶（群体）相互作用。然而，与经典的成对网络相比，高阶网络优越的描述能力会大大增加模型的复杂性和计算成本。因此，建立一种定量方法来确定这种建模框架何时相对于成对模型有利，以及在多大程度上提供了对经验系统的简约描述，这一点至关重要。在这里，我们提出了一种基于信息压缩的原则性方法，通过识别扩散过程中的冗余，同时保留相关的函数信息，来分析高阶网络对低阶交互的可还原性。对广泛经验系统的分析表明，尽管一些网络包含不可压缩的群相互作用，但其他网络可以通过低阶相互作用有效地近似——一些技术和生物系统甚至只是通过成对相互作用。更普遍地说，我们的发现标志着朝着最小化复杂系统模型维度迈出了重要一步 et.al.|[2404.08547](http://arxiv.org/abs/2404.08547)|null|
|**2024-04-12**|**Echoes of darkness: Supernova-neutrino-boosted dark matter from all galaxies**|最近有人提出，来自SN1987a或下一个星系SN的超新星中微子（SN $\nu$）增强的暗物质（BDM）可以作为探测DM和标准模型轻子之间非零相互作用的新成分。在这项工作中，我们扩展了这一概念，并评估了目前起源于所有红移较高的星系的SN$\nu$BDM的扩散通量。我们证明，通过考虑这种扩散BDM（DBDM）分量，在超级神冈或超级神冈等大型中微子实验中，可以获得DM-$\nu$和DM电子截面的乘积$\sqrt｛\sigma_｛\chi\nu｝\sigma｛\chi e｝｝\simq\mathcal｛O｝（10^｛-37｝）$~cm$^2$的最佳模型无关灵敏度，超过SN1987a估计的SN$\nu$BDM界。我们还研究了星系中超大质量黑洞周围DM尖峰的存在对SN$\nu$BDM和DBDM的影响。我们的结果表明，DBDM和SN$\nu$ BDM探测器都对DM尖峰的不确定性不敏感，除非下一个星系SN恰好发生在沿着SN视线非常靠近或正好在星系中心后面的位置。 et.al.|[2404.08528](http://arxiv.org/abs/2404.08528)|null|
|**2024-04-12**|**Generalized Hydrodynamics for the Volterra lattice: Ballistic and nonballistic behavior of correlation functions**|近年来，在描述可积系统的流体动力学行为方面付出了大量的努力。在本文中，我们描述了Volterra格的这种图。具体地说，我们能够根据被赋予广义吉布斯系综的Volterra晶格的态密度来显式地计算磁化率矩阵和电流场相关矩阵。此外，我们应用线性广义流体力学理论来描述相关函数的欧拉尺度行为。我们预计广义流体动力学方程的解在 $\xi_0=\frac｛x｝｛t｝$处产生冲击；因此，这种线性近似不能完全描述相关函数的行为。尽管这一事实很有趣，但我们进行了几次数值研究，结果表明，正是当流体动力学方程的解产生冲击时，相关函数表现出高度振荡的行为。鉴于这一经验观察，我们认为，在这一点上，$\xi_0$ 的扩散贡献并不是对弹道输运的次级校正，但它们的阶数相同。 et.al.|[2404.08499](http://arxiv.org/abs/2404.08499)|null|
|**2024-04-12**|**PiRD: Physics-informed Residual Diffusion for Flow Field Reconstruction**|在求解偏微分方程的正问题和反问题时，在流体动力学中使用机器学习来加快计算变得越来越普遍。然而，现有的基于卷积神经网络（CNN）的数据保真度增强方法的一个显著挑战是，它们在训练阶段依赖于特定的低保真度数据模式和分布。此外，基于CNN的方法本质上将流重建任务视为计算机视觉任务，该任务优先考虑元素精度，缺乏物理和数学解释。这种依赖性会极大地影响模型在真实世界场景中的有效性，尤其是当低保真度输入偏离训练数据或包含训练过程中未考虑的噪声时。在这种情况下引入扩散模型显示了提高性能和可推广性的前景。与从特定低保真度分布到高保真度分布的直接映射不同，扩散模型学习从任何低保真性分布向高保真度分布过渡。我们提出的模型——基于物理的残差扩散，证明了从标准低保真度输入到注入高斯噪声的低保真性输入以及随机收集样本的数据质量提升能力。通过将基于物理学的见解整合到目标函数中，它进一步提高了推断出的高质量数据的准确性和保真度。实验结果表明，我们的方法可以从一系列低保真度输入条件有效地重建二维湍流的高质量结果，而无需重新训练。 et.al.|[2404.08412](http://arxiv.org/abs/2404.08412)|null|
|**2024-04-12**|**Estimate of force noise from electrostatic patch potentials in LISA Pathfinder**|本文讨论了LISA和LISA Pathfinder中由测试质量和周围电极外壳表面上的贴片电势与其自身的时间波动的相互作用引起的力噪声。我们的目的是估计这种现象对LISA Pathfinder中检测到的力噪声的贡献，该力噪声超过了布朗运动的背景。我们引入了一个模型，该模型将相互作用的测试质量和外壳表面近似为同心球体，将贴片电势视为这些球体表面上的各向同性随机高斯过程。我们发现，由于表面污染导致的斑块情况，以及扩散驱动的密度波动，确实会产生与观察到的频率 $f^{-2}$ 相关的力噪声。然而，无论是LISA Pathfinder本身还是其他实验，都没有足够的实验证据来预测这种噪声的幅度，这种噪声的范围从完全可以忽略到解释整个噪声过量。我们简要讨论了在LISA中确保该噪声足够小的几种措施。 et.al.|[2404.08340](http://arxiv.org/abs/2404.08340)|null|
|**2024-04-12**|**Struggle with Adversarial Defense? Try Diffusion**|对抗性攻击通过引入微妙的扰动而导致错误分类。最近，扩散模型被应用于图像分类器，以通过对抗性训练或通过净化对抗性噪声来提高对抗性鲁棒性。然而，基于扩散的对抗性训练经常遇到收敛性挑战和高昂的计算费用。此外，基于扩散的净化不可避免地会导致数据转移，并被认为容易受到更强的自适应攻击。为了解决这些问题，我们提出了真相最大化扩散分类器（TMDC），这是一种基于预先训练的扩散模型和贝叶斯定理的生成贝叶斯分类器。与数据驱动的分类器不同，TMDC在贝叶斯原理的指导下，利用来自扩散模型的条件似然来确定输入图像的类别概率，从而避免数据偏移的影响和对抗性训练的局限性。此外，为了增强TMDC对更强大的对抗性攻击的抵御能力，我们提出了一种扩散分类器的优化策略。该策略包括在扰动数据集上以地面实况标签为条件对扩散模型进行后训练，引导扩散模型学习数据分布，并最大化地面实况标签下的可能性。所提出的方法在CIFAR10数据集上实现了最先进的性能，可以抵御重白盒攻击和强自适应攻击。具体而言，TMDC在 $\epsilon=0.05$的情况下，分别对$l_｛infty｝$范数有界扰动实现82.81%的鲁棒精度和对$l_｛2｝$ 范有界扰动的86.05%的鲁棒精度。 et.al.|[2404.08273](http://arxiv.org/abs/2404.08273)|null|
|**2024-04-12**|**An XRISM observation proposal: Gas velocity in the merging cluster Abell 2256**|XRISM任务的目标之一是用Resolve光谱学测量星系团的气体动力学。为了存档这些，我们建议在z=0.06时对X射线明亮星系团Abell 2256进行观测。这里有第二亮的漫射无线电遗迹。Suzaku首次在星团中以1500公里/秒的速度揭示了气体的整体运动。这个X射线气体速度与星系速度测量值一致，表明气体和星系正在一起运动。这些和其他观测结果使该系统最适用于气体体积和湍流运动及相关物理的XRISM光谱映射。我们提出两点来覆盖中心~400kpc区域。 et.al.|[2404.08267](http://arxiv.org/abs/2404.08267)|null|
|**2024-04-12**|**Balanced Mixed-Type Tabular Data Synthesis with Diffusion Models**|扩散模型已经成为各种生成任务（如图像和音频合成）的稳健框架，并且还证明了生成包括连续变量和离散变量的混合型表格数据的显著能力。然而，目前在混合类型表格数据上训练扩散模型的方法往往会继承训练数据集中存在的特征的不平衡分布，这可能导致有偏差的采样。在这项研究中，我们引入了一个公平扩散模型，旨在生成敏感属性的平衡数据。我们提供的经验证据表明，我们的方法有效地缓解了训练数据中的类不平衡，同时保持了生成样本的质量。此外，我们提供的证据表明，在性能和公平性方面，我们的方法优于现有的表格数据合成方法。 et.al.|[2404.08254](http://arxiv.org/abs/2404.08254)|null|
|**2024-04-12**|**An Asymptotically-Correct Implicit-Explicit Time Integration Scheme for Finite Volume Radiation-Hydrodynamics**|非相对论流的数值辐射流体力学（RHD）是一个具有挑战性的问题，因为它包含了在非常宽的时间尺度上作用的过程，并且这些过程的相对重要性在整个计算域中往往按数量级变化。在这里，我们提出了一种新的数值RHD隐显（IMEX）方法，该方法具有许多以前没有组合在单一方法中的理想性质。我们的方案基于矩，允许机器精确守恒能量和动量，非常适合自适应网格细化应用；它不需要比流体力学更多的通信，并且不包括非局部迭代步骤，这使得它非常适合于通信是瓶颈的大规模并行和基于GPU的系统；我们证明了它在流、静态扩散和动态扩散极限下是渐近准确的，包括在计算网格不求解光子平均自由程的所谓渐近扩散状态下。我们在GPU加速的RHD代码QUOKKA中实现了我们的方法，并表明它通过了广泛的数值测试。 et.al.|[2404.08247](http://arxiv.org/abs/2404.08247)|**[link](https://github.com/quokka-astro/quokka)**|

<p align=right>(<a href=#updated-on-20240416>back to top</a>)</p>

## NeRF

|Publish Date|Title|Abstract|PDF|Code|
|---|---|---|---|---|
|**2024-04-10**|**Ray-driven Spectral CT Reconstruction Based on Neural Base-Material Fields**|在谱CT重建中，基底材料分解涉及求解大规模非线性积分方程组，这在数学上是高度不适定的。本文提出了一种模型，该模型使用神经场表示来参数化对象的衰减系数，从而避免了线积分离散化过程中像素驱动的投影系数矩阵的复杂计算。介绍了一种基于光线驱动神经场的线积分轻量级离散化方法，提高了离散化过程中积分逼近的精度。将基底材料表示为连续的向量值隐函数，以建立基底材料的神经场参数化模型。然后使用深度学习的自动微分框架来求解神经基底材料场的隐式连续函数。该方法不受重建图像空间分辨率的限制，并且网络具有紧凑和规则的特性。实验验证表明，我们的方法在处理光谱CT重建方面表现得非常好。此外，它还满足了生成高分辨率重建图像的要求。 et.al.|[2404.06991](http://arxiv.org/abs/2404.06991)|null|
|**2024-04-12**|**SpikeNVS: Enhancing Novel View Synthesis from Blurry Images via Spike Camera**|使用神经辐射场（NeRF）和三维高斯散射（3DGS）等神经场方法实现清晰的新视图合成（NVS）的最关键因素之一是训练图像的质量。然而，传统的RGB相机容易受到运动模糊的影响。相比之下，像事件和尖峰相机这样的神经形态相机固有地捕捉更全面的时间信息，这可以作为额外的训练数据提供场景的清晰表示。最近的方法已经探索了集成事件摄像机以提高NVS的质量。事件RGB方法有一些局限性，例如高昂的培训成本和无法在后台有效工作。相反，我们的研究引入了一种新的方法，使用尖峰相机来克服这些限制。通过将尖峰流的纹理重建视为基本事实，我们设计了尖峰纹理（TfS）损失。由于尖峰摄像机依赖于时间积分，而不是事件摄像机使用的时间微分，我们提出的TfS损失保持了可管理的训练成本。它同时处理前景对象和背景。我们还提供了用spike RGB相机系统拍摄的真实世界数据集，以促进未来的研究工作。我们使用合成和真实世界的数据集进行了广泛的实验，以证明我们的设计可以增强NeRF和3DGS的新视图合成。代码和数据集将提供给公众访问。 et.al.|[2404.06710](http://arxiv.org/abs/2404.06710)|null|
|**2024-04-03**|**A Coupled Neural Field Model for the Standard Consolidation Theory**|标准巩固理论指出，位于海马体的短期记忆能够巩固新皮层的长期记忆。换言之，新皮层在海马体的短暂支持下慢慢学习长期记忆，海马体会快速学习不稳定的记忆。然而，目前尚不清楚这些学习率和记忆时间尺度差异背后的神经生物学机制是什么。在这里，我们提出了一种新的标准巩固理论的建模方法，重点关注其潜在的神经生物学机制。除了突触可塑性和棘突频率适应外，我们的模型还结合了齿状回的成年神经发生以及新皮层和海马体之间的大小差异，我们将其与距离依赖性突触可塑性联系起来。我们还考虑了相关大脑区域的相互关联的空间结构，将上述神经生物学机制纳入耦合的神经场框架中，其中每个区域由具有区域内和区域间连接的单独神经场表示。据我们所知，这是将神经场应用于这一过程的首次尝试。使用数值模拟和数学分析，我们探索了在外部输入的海马重放和检索线索的相位交替时，模型的短期和长期动力学。该外部输入可被编码为单个神经场中的多凸点吸引器模式形式的记忆模式。在该模型中，由于海马记忆模式的突起之间的距离较小，海马记忆模式在新皮质记忆模式之前首先被编码。因此，在短时间尺度上检索新皮层中的输入模式需要由海马体的记忆模式提供额外的输入。新皮质记忆模式在较长的时间内逐渐巩固，直到它们的恢复不再需要海马体的支持。在较长的时间内，神经发生对海马神经场的扰动会抹去海马模式，导致记忆模式只在新皮层中唤起的最终状态。因此，我们模型的动力学成功地再现了标准固结理论的主要特征。这表明，海马体的神经发生和距离依赖性突触可塑性，再加上突触抑制和尖峰频率适应，确实是记忆巩固的关键神经生物学过程。 et.al.|[2404.02938](http://arxiv.org/abs/2404.02938)|null|
|**2024-04-03**|**LiDAR4D: Dynamic Neural Fields for Novel Space-time View LiDAR Synthesis**|尽管神经辐射场（NeRFs）在图像新视图合成（NVS）方面取得了成功，但激光雷达NVS在很大程度上仍未被探索。以前的激光雷达NVS方法采用了图像NVS方法的简单转变，同时忽略了激光雷达点云的动态特性和大规模重建问题。有鉴于此，我们提出了LiDAR4D，这是一种用于新的时空LiDAR视图合成的仅限LiDAR的可微分框架。考虑到稀疏性和大规模特征，我们设计了一种结合多平面和网格特征的4D混合表示，以实现从粗到细的有效重建。此外，我们引入了从点云导出的几何约束，以提高时间一致性。对于激光雷达点云的真实合成，我们结合了光线下降概率的全局优化，以保持跨区域模式。在KITTI-360和NuScenes数据集上进行的大量实验证明了我们的方法在实现几何感知和时间一致的动态重建方面的优越性。代码可在https://github.com/ispc-lab/LiDAR4D. et.al.|[2404.02742](http://arxiv.org/abs/2404.02742)|**[link](https://github.com/ispc-lab/lidar4d)**|
|**2024-04-04**|**Vestibular schwannoma growth prediction from longitudinal MRI by time conditioned neural fields**|前庭神经鞘瘤（VS）是一种良性肿瘤，通常通过MRI检查进行积极监测来治疗。为了进一步帮助临床决策并避免过度治疗，基于纵向成像的肿瘤生长的准确预测是非常可取的。在本文中，我们介绍了DeepGrowth，这是一种深度学习方法，它结合了神经场和递归神经网络，用于前瞻性肿瘤生长预测。在所提出的方法中，每个肿瘤都表示为以低维潜在码为条件的有符号距离函数（SDF）。与之前直接在图像空间中进行肿瘤形状预测的研究不同，我们预测潜在代码，然后从中重建未来的形状。为了处理不规则的时间间隔，我们引入了一个基于ConvLSTM的时间条件递归模块和一种新的时间编码策略，使所提出的模型能够输出随时间变化的肿瘤形状。在内部纵向VS数据集上的实验表明，所提出的模型显著提高了性能（ $\ge 1.6\%%$Dice评分和$\ge0.20$mm95\%Hausdorff距离），特别是对于生长或缩小最多的前20%肿瘤（$\ge4.6\%%$Dice评分和$\ge 0.73$ mm95\%Hausdoff距离）。我们的代码可在~\bull获得{https://github.com/cyjdswx/DeepGrowth} et.al.|[2404.02614](http://arxiv.org/abs/2404.02614)|**[link](https://github.com/cyjdswx/deepgrowth)**|
|**2024-04-02**|**NeRFCodec: Neural Feature Compression Meets Neural Radiance Fields for Memory-Efficient Scene Representation**|神经辐射场（NeRF）的出现极大地影响了三维场景建模和新颖的视图合成。作为一种用于三维场景表示的视觉媒体，具有高率失真性能的压缩是一个永恒的目标。受神经压缩和神经场表示进步的启发，我们提出了NeRFCodec，这是一种端到端的NeRF压缩框架，它集成了非线性变换、量化和熵编码，用于高效记忆的场景表示。由于直接在大规模的NeRF特征平面上训练非线性变换是不切实际的，我们发现，当添加内容特定参数时，可以使用预先训练的神经2D图像编解码器来压缩特征。具体来说，我们重用神经2D图像编解码器，但修改其编码器和解码器头，同时保持预训练解码器的其他部分冻结。这使我们能够通过监督渲染损失和熵损失来训练整个管道，通过更新特定于内容的参数来实现率失真平衡。在测试时，包含潜在代码、特征解码器头和其他辅助信息的比特流被发送用于通信。实验结果表明，我们的方法优于现有的NeRF压缩方法，能够在0.5MB的内存预算下实现高质量的新视图合成。 et.al.|[2404.02185](http://arxiv.org/abs/2404.02185)|null|
|**2024-04-01**|**NeRF-MAE : Masked AutoEncoders for Self Supervised 3D representation Learning for Neural Radiance Fields**|神经领域在计算机视觉和机器人领域表现出色，因为它们能够理解3D视觉世界，如推断语义、几何和动力学。考虑到神经场在从2D图像密集表示3D场景方面的能力，我们提出了一个问题：我们是否可以扩展它们的自监督预训练，特别是使用掩蔽的自动编码器，从姿态RGB图像中生成有效的3D表示。由于将转换器扩展到新型数据模式的惊人成功，我们采用了标准的3D视觉转换器来适应NeRF的独特配方。我们利用NeRF的体积网格作为变压器的密集输入，将其与其他3D表示（如点云）进行对比，在点云中，信息密度可能不均匀，并且表示不规则。由于将掩蔽的自动编码器应用于隐式表示（如NeRF）很困难，我们选择提取通过使用相机轨迹进行采样来规范化跨域场景的显式表示。我们的目标是通过从NeRF的辐射和密度网格中屏蔽随机补丁，并使用标准的3D Swin Transformer来重建屏蔽的补丁。通过这样做，模型可以学习完整场景的语义和空间结构。我们在我们提出的精心策划的姿势RGB数据上对这种表示进行了大规模的预训练，总共超过160万张图像。一旦经过预训练，编码器就用于有效的3D迁移学习。我们针对NeRF的新型自监督预训练NeRF-MAE可扩展性非常好，并提高了在各种具有挑战性的3D任务中的性能。在Front3D和ScanNet数据集上，利用未标记的姿态2D数据进行预训练，NeRF MAE显著优于自监督3D预训练和NeRF场景理解基线，在3D对象检测方面的绝对性能提高超过20%AP50和8%AP25。 et.al.|[2404.01300](http://arxiv.org/abs/2404.01300)|null|
|**2024-04-06**|**Grounding and Enhancing Grid-based Models for Neural Fields**|当代许多研究利用基于网格的模型来表示神经场，但仍然缺乏对基于网格模型的系统分析，阻碍了这些模型的改进。因此，本文介绍了一个基于网格的模型的理论框架。该框架指出，这些模型的逼近和泛化行为是由网格切线核（GTK）决定的，GTK是基于网格的模型的固有性质。所提出的框架有助于对各种基于网格的模型进行一致和系统的分析。此外，引入的框架推动了一种新的基于网格的模型的开发，该模型名为乘法傅立叶自适应网格（MulFAGrid）。数值分析表明，MulFAGrid表现出比其前身更低的泛化界，表明其具有鲁棒的泛化性能。实证研究表明，MulFAGrid在各种任务中都取得了最先进的性能，包括2D图像拟合、3D符号距离场（SDF）重建和新颖的视图合成，表现出了卓越的表示能力。项目网站位于https://sites.google.com/view/cvpr24-2034-submission/home. et.al.|[2403.20002](http://arxiv.org/abs/2403.20002)|null|
|**2024-04-01**|**Efficient 3D Instance Mapping and Localization with Neural Fields**|我们解决了从一系列摆姿势的RGB图像中学习用于3D实例分割的隐式场景表示的问题。为此，我们引入了3DIML，这是一种新的框架，可以有效地学习可以从新的视点渲染的标签字段，以产生视图一致的实例分割掩码。3DIML显著改进了现有的基于隐式场景表示的方法的训练和推理运行时。与现有技术相反，现有技术以自我监督的方式优化神经场，需要复杂的训练过程和损失函数设计，3DIML利用了两阶段过程。第一阶段InstanceMap将前端实例分割模型生成的图像序列的2D分割掩码作为输入，并将图像上的相应掩码与3D标签相关联。然后，在第二阶段InstanceLift中使用这些几乎视图一致的伪标签掩码来监督神经标签字段的训练，该字段对InstanceMap遗漏的区域进行插值并解决歧义。此外，我们介绍了InstanceLoc，它能够在给定训练过的标签字段和现成的图像分割模型的情况下，通过融合两者的输出，实现实例掩码的近实时定位。我们在Replica和ScanNet数据集的序列上评估了3DIML，并证明了在图像序列的温和假设下3DIML的有效性。与现有的质量相当的隐式场景表示方法相比，我们实现了巨大的实际加速，展示了其促进更快、更有效的3D场景理解的潜力。 et.al.|[2403.19797](http://arxiv.org/abs/2403.19797)|null|
|**2024-03-28**|**Neural Fields for 3D Tracking of Anatomy and Surgical Instruments in Monocular Laparoscopic Video Clips**|腹腔镜视频跟踪主要关注两种目标类型：手术器械和解剖结构。前者可用于技能评估，而后者对于虚拟覆盖的投影是必要的。在仪器和解剖跟踪通常被视为两个独立的问题的情况下，在本文中，我们提出了一种同时对所有结构进行联合跟踪的方法。基于单个2D单眼视频剪辑，我们训练神经场来表示连续的时空场景，用于创建至少一帧中可见的所有表面的3D轨迹。由于仪器尺寸较小，它们通常只覆盖图像的一小部分，导致跟踪精度下降。因此，我们建议增强类权重以改善仪器轨迹。我们评估了对腹腔镜胆囊切除术视频片段的跟踪，发现解剖结构和器械的平均跟踪准确率分别为92.4%和87.4%。此外，我们还评估了从该方法的场景重建中获得的深度图的质量。我们表明，这些伪深度具有与最先进的预训练深度估计器相当的质量。在SCARED数据集中的腹腔镜视频上，该方法预测深度的MAE为2.9 mm，相对误差为9.2%。这些结果表明了使用神经场进行腹腔镜场景的单目3D重建的可行性。 et.al.|[2403.19265](http://arxiv.org/abs/2403.19265)|null|

<p align=right>(<a href=#updated-on-20240416>back to top</a>)</p>

[contributors-shield]: https://img.shields.io/github/contributors/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[contributors-url]: https://github.com/Vincentqyw/cv-arxiv-daily/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[forks-url]: https://github.com/Vincentqyw/cv-arxiv-daily/network/members
[stars-shield]: https://img.shields.io/github/stars/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[stars-url]: https://github.com/Vincentqyw/cv-arxiv-daily/stargazers
[issues-shield]: https://img.shields.io/github/issues/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[issues-url]: https://github.com/Vincentqyw/cv-arxiv-daily/issues

