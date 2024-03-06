[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]

## Updated on 2024.03.06
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
|**2024-03-04**|**DaReNeRF: Direction-aware Representation for Dynamic Scenes**|为了应对建模和重新渲染动态场景的复杂挑战，最近的方法试图使用基于平面的显式表示来简化这些复杂性，克服了与神经辐射场（NeRF）和隐式表示等方法相关的训练时间慢的问题。然而，将4D动态场景直接分解为多个基于2D平面的表示被证明不足以重新渲染具有复杂运动的高保真场景。作为回应，我们提出了一种新的方向感知表示（DaRe）方法，该方法从六个不同的方向捕捉场景动力学。该学习的表示经过逆对偶树复小波变换（DTCWT）以恢复基于平面的信息。DaReNeRF通过融合来自这些恢复平面的向量来计算每个时空点的特征。将DaReNeRF与用于颜色回归的微小MLP相结合，并在训练中利用体积渲染，可以在复杂动态场景的新型视图合成中获得最先进的性能。值得注意的是，为了解决六个实数和六个虚数方向感知小波系数引入的冗余问题，我们引入了一种可训练的掩蔽方法，在不显著降低性能的情况下缓解了存储问题。此外，与现有技术相比，DaReNeRF保持了2倍的训练时间减少，同时提供了卓越的性能。 et.al.|[2403.02265](http://arxiv.org/abs/2403.02265)|null|
|**2024-03-04**|**Depth-Guided Robust and Fast Point Cloud Fusion NeRF for Sparse Input Views**|具有稀疏输入视图的新型视图合成对于AR/VR和自动驾驶等现实世界应用非常重要。最近的方法已经将深度信息集成到用于稀疏输入合成的NeRF中，利用深度先验进行几何和空间理解。然而，大多数现有的作品往往忽略了深度图中的不准确之处，并且时间效率较低。为了解决这些问题，我们提出了一种用于稀疏输入的深度引导鲁棒快速点云融合NeRF。我们将辐射场视为特征的显式体素网格。为每个输入视图构建一个点云，使用矩阵和向量在体素网格内进行特征化。我们累积每个输入视图的点云，以构建整个场景的融合点云。每个体素通过参考整个场景的点云来确定其密度和外观。通过点云融合和体素网格微调，深度值的不精确性可以被其他视图的不精确值细化或替换。此外，我们的方法可以通过有效的向量矩阵分解来实现更快的重建和更大的紧凑性。实验结果强调，与最先进的基线相比，我们的方法具有卓越的性能和时间效率。 et.al.|[2403.02063](http://arxiv.org/abs/2403.02063)|null|
|**2024-03-04**|**DD-VNB: A Depth-based Dual-Loop Framework for Real-time Visually Navigated Bronchoscopy**|支气管镜的实时6自由度定位对于提高干预质量至关重要。然而，当前基于视觉的技术难以在对看不见的数据的泛化和计算速度之间取得平衡。在这项研究中，我们提出了一种用于实时视觉导航支气管镜检查（DD-VNB）的基于深度的双环框架，该框架可以在不需要重新训练的情况下推广到患者病例中。DD-VNB框架集成了两个关键模块：深度估计和双环定位。为了解决患者之间的领域差距，我们提出了一种知识嵌入的深度估计网络，该网络将内窥镜帧映射到深度，通过消除患者特定的纹理来确保泛化。该网络将视图合成知识嵌入到循环对抗性架构中，用于尺度约束的单目深度估计。为了获得实时性能，我们的定位模块将快速自我运动估计网络嵌入深度配准循环中。自我运动推断网络以高频估计支气管镜的姿态变化，而相对于术前3D模型的深度配准周期性地提供绝对姿态。具体而言，将相对姿态变化作为初始猜测输入到配准过程中，以提高其准确性和速度。对来自患者的体模和体内数据的实验证明了我们框架的有效性：1）单目深度估计优于SOTA，2）定位在体模中实现了4.7 $\pm$3.17 mm的绝对跟踪误差（ATE）精度，在患者数据中实现了6.49$\pm$ 3.88 mm的绝对追踪误差，3）帧速率接近视频捕获速度，4）而不需要按情况进行网络再训练。该框架优越的速度和准确性证明了其在实时支气管镜导航方面的临床潜力。 et.al.|[2403.01683](http://arxiv.org/abs/2403.01683)|null|
|**2024-03-02**|**NeRF-VPT: Learning Novel View Representations with Neural Radiance Fields via View Prompt Tuning**|神经辐射场（NeRF）在新视图合成中取得了显著的成功。尽管如此，为新颖的视图生成高质量图像的任务仍然是一个关键的挑战。虽然现有的努力取得了值得称赞的进展，但捕捉复杂的细节、增强纹理和实现卓越的峰值信噪比（PSNR）指标值得进一步关注和进步。在这项工作中，我们提出了NeRF VPT，这是一种用于新视图合成的创新方法，以应对这些挑战。我们提出的NeRF VPT采用级联视图提示调整范式，其中从先前渲染结果中获得的RGB信息作为后续渲染阶段的指导性视觉提示，期望嵌入提示中的先验知识可以促进渲染图像质量的逐步增强。NeRF VPT只需要在每个训练阶段从前一阶段的渲染中采样RGB数据作为先验，而不需要依赖额外的指导或复杂的技术。因此，我们的NeRF VPT是即插即用的，可以很容易地集成到现有的方法中。通过在要求苛刻的真实场景基准上对我们的NeRF VPT与几种基于NeRF的方法进行比较分析，如真实合成360、真实前向、副本数据集和用户捕获的数据集，我们证实，与所有最先进的方法相比，我们的NeRF VPT显著提高了基线性能，并能熟练地生成更高质量的新视图图像。此外，NeRF VPT的级联学习引入了对具有稀疏输入的场景的适应性，从而显著提高了稀疏视图新视图合成的准确性。源代码和数据集位于\url{https://github.com/Freedomcls/NeRF-VPT}. et.al.|[2403.01325](http://arxiv.org/abs/2403.01325)|**[link](https://github.com/freedomcls/nerf-vpt)**|
|**2024-03-02**|**Neural Field Classifiers via Target Encoding and Classification Loss**|神经场方法在计算机视觉和计算机图形学中的各种长期任务中取得了巨大进展，包括新颖的视图合成和几何重建。由于现有的神经场方法试图预测一些基于坐标的连续目标值，例如神经辐射场（NeRF）的RGB，所有这些方法都是回归模型，并通过一些回归损失进行优化。然而，对于神经场方法来说，回归模型真的比分类模型更好吗？在这项工作中，我们试图从机器学习的角度来探讨神经领域这个非常基本但被忽视的问题。我们成功地提出了一种新的神经场分类器（NFC）框架，该框架将现有的神经场方法公式化为分类任务，而不是回归任务。所提出的NFC可以通过使用新的目标编码模块和优化分类损失，轻松地将任意神经场回归器（NFR）转换为其分类变体。通过将连续回归目标编码为高维离散编码，我们自然地形成了多标签分类任务。大量的实验证明了NFC在几乎免费的额外计算成本下令人印象深刻的有效性。此外，NFC还显示出对稀疏输入、损坏图像和动态场景的鲁棒性。 et.al.|[2403.01058](http://arxiv.org/abs/2403.01058)|null|
|**2024-02-29**|**ViewFusion: Towards Multi-View Consistency via Interpolated Denoising**|通过扩散模型进行的新型视图合成在生成多样化和高质量图像方面表现出了显著的潜力。然而，在这些主流方法中，图像生成的独立过程导致了在保持多视图一致性方面的挑战。为了解决这一问题，我们引入了ViewFusion，这是一种新颖的无训练算法，可以无缝集成到现有的预训练扩散模型中。我们的方法采用了一种自回归方法，该方法隐式地利用先前生成的视图作为下一个视图生成的上下文，确保了在新视图生成过程中强大的多视图一致性。通过通过插值去噪融合已知视图信息的扩散过程，我们的框架成功地扩展了单视图条件模型，使其在多视图条件设置下工作，而无需任何额外的微调。大量的实验结果证明了ViewFusion在生成一致且详细的新视图方面的有效性。 et.al.|[2402.18842](http://arxiv.org/abs/2402.18842)|**[link](https://github.com/Wi-sc/ViewFusion)**|
|**2024-02-28**|**PolyOculus: Simultaneous Multi-view Image-based Novel View Synthesis**|本文考虑了生成新视图合成（GNVS）的问题，即在给定有限数量的已知视图的情况下生成场景的新颖、合理的视图。在这里，我们提出了一个基于集合的生成模型，该模型可以同时生成多个自洽的新视图，条件是任何数量的已知视图。我们的方法不限于一次生成单个图像，并且可以以零、一个或多个视图为条件。因此，当生成大量视图时，我们的方法不限于低阶自回归生成方法，并且能够更好地在大图像集上保持生成的图像质量。我们在标准NVS数据集上评估了所提出的模型，并表明它优于最先进的基于图像的GNVS基线。此外，我们表明，该模型能够生成没有自然顺序的相机视图集，如循环和双目轨迹，并且在此类任务上显著优于其他方法。 et.al.|[2402.17986](http://arxiv.org/abs/2402.17986)|null|
|**2024-02-27**|**AlignMiF: Geometry-Aligned Multimodal Implicit Field for LiDAR-Camera Joint Synthesis**|神经隐式场已经成为新视图合成中事实上的标准。最近，有一些方法探索在一个领域内融合多个模态，旨在共享不同模态的隐含特征，以提高重建性能。然而，这些模态往往表现出错位行为：对一种模态（如激光雷达）进行优化可能会对另一种模态产生不利影响，如相机性能，反之亦然。在这项工作中，我们对激光雷达相机联合合成的多模式隐场进行了全面分析，揭示了潜在的问题在于不同传感器的错位。此外，我们还介绍了AlignMiF，这是一个几何对齐的多模式隐式场，具有两个拟议的模块：几何感知对齐（GAA）和共享几何初始化（SGI）。这些模块有效地调整了不同模态的粗略几何结构，显著增强了激光雷达和相机数据之间的融合过程。通过在各种数据集和场景中进行广泛的实验，我们证明了我们的方法在促进激光雷达和相机模态之间在统一的神经场中更好地交互方面的有效性。具体而言，我们提出的AlignMiF比最近的隐式融合方法（KITTI-360和Waymo数据集上的图像PSNR分别为+2.01和+3.11）实现了显著的改进，并始终超过单模态性能（在各自的数据集上，激光雷达切角距离分别减少了13.8%和14.2%）。 et.al.|[2402.17483](http://arxiv.org/abs/2402.17483)|**[link](https://github.com/tangtaogo/alignmif)**|
|**2024-02-26**|**GEA: Reconstructing Expressive 3D Gaussian Avatar from Monocular Video**|本文提出了GEA，这是一种基于3D高斯的身体和手的高保真重建来创建富有表现力的3D化身的新方法。关键贡献有两方面。首先，我们设计了一种两阶段姿态估计方法，以从输入图像中获得准确的SMPL-X姿态，从而在训练图像的像素和SMPL-X模型之间提供正确的映射。它使用注意力感知网络和优化方案来对齐图像中估计的SMPL-X身体和真实身体之间的法线和轮廓。其次，我们提出了一种迭代重新初始化策略来处理高斯表示所面临的不平衡聚合和初始化偏差。该策略迭代地重新分布化身的高斯点，通过应用网格划分、重采样和重高斯运算，使其均匀分布在人体表面附近。结果，可以实现更高质量的渲染。大量的实验分析验证了所提出的模型的有效性，表明它在逼真的新视图合成中实现了最先进的性能，同时提供了对人体和手部姿势的细粒度控制。项目页面：https://3d-aigc.github.io/GEA/. et.al.|[2402.16607](http://arxiv.org/abs/2402.16607)|null|
|**2024-02-26**|**CMC: Few-shot Novel View Synthesis via Cross-view Multiplane Consistency**|神经辐射场（NeRF）由于其连续表示场景的能力，在新颖的视图合成中，特别是在虚拟现实（VR）和增强现实（AR）中，显示出了令人印象深刻的结果。然而，当只有几个输入视图图像可用时，NeRF倾向于过度拟合给定视图，从而使像素的估计深度共享几乎相同的值。与以前通过引入复杂的先验或额外的监督来进行正则化的方法不同，我们提出了一种简单而有效的方法，该方法明确地在输入视图之间建立深度感知一致性，以应对这一挑战。我们的关键见解是，通过强制在不同的输入视图中重复采样相同的空间点，我们能够加强视图之间的相互作用，从而缓解过拟合问题。为了实现这一点，我们在分层表示（\textit｛即｝多平面图像）上建立神经网络，因此可以在多个离散平面上对采样点进行重新采样。此外，为了正则化看不见的目标视图，我们将不同输入视图的渲染颜色和深度约束为相同。尽管简单，但大量的实验表明，与最先进的方法相比，我们提出的方法可以获得更好的合成质量。 et.al.|[2402.16407](http://arxiv.org/abs/2402.16407)|null|

<p align=right>(<a href=#updated-on-20240306>back to top</a>)</p>

## 3D Reconstruction

|Publish Date|Title|Abstract|PDF|Code|
|---|---|---|---|---|
|**2024-03-05**|**Pooling Image Datasets With Multiple Covariate Shift and Imbalance**|小样本量在许多学科中很常见，这就需要在多个机构中汇集大致相似的数据集，以研究图像和疾病结果之间微弱但相关的关联。这种数据通常表现出协变量（即二次非成像数据）的偏移/不平衡。控制这种干扰变量在标准统计分析中很常见，但这些想法并不直接适用于参数过大的模型。因此，最近的工作表明，来自不变表示学习的策略是如何提供一个有意义的起点的，但目前的方法仅限于一次只考虑几个协变量的变化/不平衡。在本文中，我们展示了如何从范畴理论的角度看待这个问题，提供了一个简单有效的解决方案，完全避免了原本需要的复杂的多阶段训练管道。我们通过在真实数据集上进行的大量实验证明了这种方法的有效性。此外，我们讨论了这种形式的公式如何为至少5个以上不同的问题设置提供统一的视角，从自监督学习到3D重建中的匹配问题。 et.al.|[2403.02598](http://arxiv.org/abs/2403.02598)|null|
|**2024-03-04**|**DragTex: Generative Point-Based Texture Editing on 3D Mesh**|最近，使用生成人工智能创建3D纹理网格引起了人们的极大关注。虽然现有方法支持在3D网格上基于文本的生成纹理生成或编辑，但它们往往难以通过更直观的交互来精确控制纹理图像的像素。虽然2D图像可以使用拖动交互进行生成编辑，但将这种类型的方法直接应用于3D网格纹理仍然会导致多个视图之间缺乏局部一致性、错误累积和训练时间长等问题。为了解决这些挑战，我们提出了一种基于生成点的3D网格纹理编辑方法，称为DragTex。该方法利用扩散模型在不同视图之间混合变形轮廓附近区域中的局部不一致纹理，从而实现局部一致的纹理编辑。此外，我们对解码器进行微调，以减少非拖动区域的重建误差，从而减少总体误差积累。此外，我们使用多视图图像来训练LoRA，而不是单独训练每个视图，这显著缩短了训练时间。实验结果表明，我们的方法有效地实现了3D网格上的拖动纹理，并生成了符合拖动交互所需意图的合理纹理。 et.al.|[2403.02217](http://arxiv.org/abs/2403.02217)|null|
|**2024-03-04**|**TripoSR: Fast 3D Object Reconstruction from a Single Image**|本技术报告介绍了TripoSR，这是一种利用变压器架构进行快速前馈3D生成的3D重建模型，可在0.5秒内从单个图像生成3D网格。基于LRM网络架构，TripoSR集成了数据处理、模型设计和训练技术方面的实质性改进。对公共数据集的评估表明，与其他开源替代品相比，TripoSR在数量和质量上都表现出优异的性能。TripoSR是根据麻省理工学院的许可发布的，旨在为研究人员、开发人员和创意人员提供3D生成人工智能的最新进展。 et.al.|[2403.02151](http://arxiv.org/abs/2403.02151)|**[link](https://github.com/vast-ai-research/triposr)**|
|**2024-03-03**|**A Novel Dynamic Light-Section 3D Reconstruction Method for Wide-Range Sensing**|现有的基于检流计的激光扫描系统在多尺度3D重建中的应用具有挑战性，因为难以在高重建精度和宽重建范围之间实现平衡。本文提出了一种新的方法，通过使用多电流计切换相机的视场来同步激光扫描。除了先进的硬件设置外，我们还通过建模动态相机、动态激光器及其组合交互，建立了系统的综合数学模型。然后，我们通过构建误差模型并最小化目标函数，提出了一种高精度、灵活的校准方法。最后，我们通过扫描标准组件来评估所提出的系统的性能。评估结果表明，当测量范围扩展到1100 mm $\times$1300 mm$\imes$ 650 mm时，所提出的三维重建系统的精度达到0.3 mm。在相同的重建精度下，重建范围扩展了25倍，表明所提出的方法同时允许在工业应用中进行高精度和宽范围的3D重建。 et.al.|[2403.01374](http://arxiv.org/abs/2403.01374)|null|
|**2024-03-01**|**G3DR: Generative 3D Reconstruction in ImageNet**|我们介绍了一种新的3D生成方法，即ImageNet中的生成3D重建（G3DR），该方法能够从单个图像中生成各种高质量的3D对象，解决了现有方法的局限性。我们框架的核心是一种新颖的深度正则化技术，该技术能够生成具有高几何保真度的场景。G3DR还利用预训练的语言视觉模型，如CLIP，实现新视图中的重建，并提高几代人的视觉逼真度。此外，G3DR设计了一种简单但有效的采样程序，以进一步提高世代的质量。G3DR提供基于类或文本条件的多样化且高效的3D资产生成。尽管G3DR很简单，但它能够击败最先进的方法，在感知指标和几何得分方面比它们提高了22%和90%，而只需要一半的训练时间。代码位于https://github.com/preddy5/G3DR et.al.|[2403.00939](http://arxiv.org/abs/2403.00939)|null|
|**2024-03-01**|**DISORF: A Distributed Online NeRF Training and Rendering Framework for Mobile Robots**|我们提出了一个框架DISORF，用于对资源受限的移动机器人和边缘设备捕获的场景进行在线3D重建和可视化。为了解决边缘设备的有限计算能力和潜在的有限网络可用性，我们设计了一个在边缘设备和远程服务器之间有效分配计算的框架。我们利用设备上的SLAM系统生成姿势关键帧，并将其传输到远程服务器，远程服务器可以通过利用NeRF模型在运行时执行高质量的3D重建和可视化。我们发现了在线NeRF训练的一个关键挑战，在该挑战中，天真的图像采样策略可能导致渲染质量的显著下降。我们提出了一种新的移位指数帧采样方法，以解决在线NeRF训练的这一挑战。我们展示了我们的框架在实现未知场景的高质量实时重建和可视化方面的有效性，因为这些场景是从移动机器人和边缘设备中的相机捕获和流式传输的。 et.al.|[2403.00228](http://arxiv.org/abs/2403.00228)|null|
|**2024-03-05**|**VEnvision3D: A Synthetic Perception Dataset for 3D Multi-Task Model Research**|开发统一的多任务基础模型已成为计算机视觉研究中的一个关键挑战。在当前的三维计算机视觉领域，大多数数据集只关注单个任务，这使各种下游任务的并行训练需求变得复杂。在本文中，我们介绍了VEnvision3D，这是一个用于多任务学习的大型3D合成感知数据集，包括深度完成、分割、上采样、位置识别和3D重建。由于每个任务的数据都是在同一环境域中收集的，因此子任务在使用的数据方面是固有的一致性。因此，这样一个独特的属性可以帮助探索多任务模型甚至基础模型的潜力，而无需单独的训练方法。同时，利用虚拟环境可自由编辑的优势，我们实现了一些新颖的设置，如模拟环境的时间变化和在模型表面采样点云。这些特点使我们能够提出几个新的基准。我们还对多任务端到端模型进行了广泛的研究，揭示了新的观察结果、挑战和未来研究的机会。我们的数据集和代码将在接受后开源。 et.al.|[2402.19059](http://arxiv.org/abs/2402.19059)|null|
|**2024-02-29**|**ViewFusion: Towards Multi-View Consistency via Interpolated Denoising**|通过扩散模型进行的新型视图合成在生成多样化和高质量图像方面表现出了显著的潜力。然而，在这些主流方法中，图像生成的独立过程导致了在保持多视图一致性方面的挑战。为了解决这一问题，我们引入了ViewFusion，这是一种新颖的无训练算法，可以无缝集成到现有的预训练扩散模型中。我们的方法采用了一种自回归方法，该方法隐式地利用先前生成的视图作为下一个视图生成的上下文，确保了在新视图生成过程中强大的多视图一致性。通过通过插值去噪融合已知视图信息的扩散过程，我们的框架成功地扩展了单视图条件模型，使其在多视图条件设置下工作，而无需任何额外的微调。大量的实验结果证明了ViewFusion在生成一致且详细的新视图方面的有效性。 et.al.|[2402.18842](http://arxiv.org/abs/2402.18842)|**[link](https://github.com/Wi-sc/ViewFusion)**|
|**2024-02-28**|**The Role of a Neutron Component in the Photospheric Emission of Long-Duration Gamma-Ray Burst Jets**|长时间伽马射线暴（LGRB）被认为是在核心坍塌超新星期间产生的，可能在流出物质中有显著的中子成分。如果存在，中子可以通过降低其不透明度来改变光子在外流中的散射方式，从而使光子比没有中子的情况下更快地解耦。因此，了解这一过程的细节可以让我们探索LGRB的中心引擎，否则它是隐藏的。在这里，我们使用相对论流体动力学模拟和使用蒙特卡罗辐射转移（MCRaT）代码的辐射转移后处理相结合的方法，给出了LGRB喷流的光球发射结果。我们通过改变平衡电子分数 $Y_｛e｝$来控制喷流材料中中子组分的大小，我们发现GRB火球中中子的存在会影响能带参数$\alpha$和$e_｛0｝$，而带有$\beta$参数的图片则不太清楚。特别地，断裂能量$E_{0}$ 被转移到更高的能量。此外，我们发现，增加中子分量的大小也会增加多个视角下流出的总辐射能量。我们的研究结果不仅揭示了LGRB，而且与与双星中子星合并相关的短时间伽马射线爆发有关，因为在这样的系统中可能存在突出的中子成分。 et.al.|[2402.18657](http://arxiv.org/abs/2402.18657)|null|
|**2024-02-27**|**Sora Generates Videos with Stunning Geometrical Consistency**|最近开发的索拉模型[1]在视频生成方面表现出了非凡的能力，引发了关于其模拟真实世界现象能力的激烈讨论。尽管它越来越受欢迎，但缺乏既定的指标来定量评估它对现实世界物理的保真度。在本文中，我们介绍了一种新的基准，该基准基于视频对真实世界物理原理的遵守程度来评估生成视频的质量。我们采用了一种将生成的视频转换为3D模型的方法，利用了3D重建的准确性在很大程度上取决于视频质量的前提。从3D重建的角度来看，我们使用所构建的3D模型所满足的几何约束的保真度作为代理来衡量生成的视频在多大程度上符合真实世界的物理规则。项目页面：https://sora-geometrical-consistency.github.io/ et.al.|[2402.17403](http://arxiv.org/abs/2402.17403)|null|

<p align=right>(<a href=#updated-on-20240306>back to top</a>)</p>

## Diffusion

|Publish Date|Title|Abstract|PDF|Code|
|---|---|---|---|---|
|**2024-03-05**|**Moment estimates, exponential integrability, concentration inequalities and exit times estimates on evolving manifolds**|在光滑（不一定是紧）流形 $M$上，配备有完全黎曼度量$g（t）$的$\sf C^1$族和向量域$Z（t）$\sf C^｛1，\infty｝$族，两者都由实区间$[0，t）$索引，其中$t\in（0，\infty]$ ，我们证明了完全演化黎曼流形上扩散的矩估计、指数可积性、集中不等式和退出时间估计。 et.al.|[2403.03209](http://arxiv.org/abs/2403.03209)|null|
|**2024-03-05**|**Scaling Rectified Flow Transformers for High-Resolution Image Synthesis**|扩散模型通过将数据的正向路径反转为噪声来从噪声中创建数据，并已成为图像和视频等高维感知数据的强大生成建模技术。整流流是一种最新的生成模型公式，它将数据和噪声连接在一条直线上。尽管它具有更好的理论性质和概念上的简单性，但它还没有被确定为标准实践。在这项工作中，我们改进了现有的噪声采样技术，通过将整流流模型偏向感知相关的尺度来训练整流流模型。通过一项大规模的研究，我们证明了与已建立的高分辨率文本到图像合成的扩散公式相比，这种方法具有优越的性能。此外，我们提出了一种新的基于转换器的文本到图像生成架构，该架构对两种模式使用单独的权重，并实现图像和文本标记之间的双向信息流，提高了文本理解、排版和人类偏好评级。我们证明，该架构遵循可预测的缩放趋势，并通过各种指标和人工评估将较低的验证损失与改进的文本到图像合成相关联。我们最大的模型优于最先进的模型，我们将公开我们的实验数据、代码和模型权重。 et.al.|[2403.03206](http://arxiv.org/abs/2403.03206)|null|
|**2024-03-05**|**MAGID: An Automated Pipeline for Generating Synthetic Multi-modal Datasets**|缺乏丰富的多模式（文本、图像）会话数据阻碍了多模式交互系统的发展，而LLM需要大量的会话数据。以前的方法通过检索到的图像来增强文本对话，从而带来隐私、多样性和质量限制。在这项工作中，我们介绍\textbf{M}ultimodal\textbf{A}ugmented\textbf{G}enerative\textbf{I}mages\textbf{D}ialogues（MAGID），一个用多样化和高质量的图像增强纯文本对话的框架。随后，应用扩散模型来制作相应的图像，确保与识别的文本对齐。最后，MAGID在图像描述生成模块（文本LLM）和图像质量模块（解决美学、图像-文本匹配和安全问题）之间集成了一个创新的反馈回路，它们协同工作以生成高质量和多模式的对话。我们使用自动化和人工评估，在三个对话数据集上将MAGID与其他SOTA基线进行了比较。我们的结果表明，MAGID与基线相当或更好，在人类评估方面有显著改进，尤其是在图像数据库较小的检索基线方面。 et.al.|[2403.03194](http://arxiv.org/abs/2403.03194)|null|
|**2024-03-05**|**Behavior Generation with Latent Actions**|从标记的数据集对复杂行为进行生成建模一直是决策中的一个长期问题。与语言或图像生成不同，决策需要建模动作——连续值向量，其分布是多模式的，可能来自未评级的来源，其中生成错误可能会在顺序预测中复合。最近一类称为行为变换器（BeT）的模型通过使用k均值聚类来捕获不同模式来离散动作来解决这一问题。然而，k-means难以对高维动作空间或长序列进行缩放，并且缺乏梯度信息，因此BeT在建模长距离动作时会受到影响。在这项工作中，我们提出了矢量量化行为转换器（VQ-BeT），这是一种用于行为生成的通用模型，可处理多模式动作预测、条件生成和部分观察。VQ-BeT通过用分层矢量量化模块标记连续动作来增强BeT。在包括模拟操纵、自动驾驶和机器人在内的七种环境中，VQ-BeT改进了最先进的模型，如BeT和扩散策略。重要的是，我们展示了VQ-BeT在捕获行为模式方面的改进能力，同时将推理速度提高了扩散策略的5倍。可以找到视频和代码https://sjlee.cc/vq-bet et.al.|[2403.03181](http://arxiv.org/abs/2403.03181)|**[link](https://github.com/jayLEE0301/vq_bet_official)**|
|**2024-03-05**|**The Amplitude Equation for the Space-Fractional Swift-Hohenberg Equation**|涉及分数拉普拉斯算子的非局部反应扩散偏微分方程（PDE）已经在各种各样的应用中出现。分析经典局部偏微分方程在不稳定性附近的动力学的一个常见工具是推导局部振幅/调制近似值，该近似值提供了对各种模式形成现象进行分类的局部正规形式。在这项工作中，我们研究了空间分数Swift-Hohhenberg方程的振幅方程。Swift-Hohenberg方程是流体动力学中受模式形成驱动的基本模型问题，并已成为开发推导振幅方程的通用技术的主要偏微分方程之一。我们证明了在第一分岔点附近存在（实）Ginzburg-Landau方程的近似。有趣的是，这个Ginzburg-Landau方程是一个局部PDE，它为物理猜想提供了严格的理由，即适当局部化的不稳定模式可以超越超扩散，并在不稳定附近重新局部化PDE。我们的主要技术贡献是为近似问题提供了一个合适的函数空间设置，然后将残差约束在原始PDE及其振幅方程之间。 et.al.|[2403.03158](http://arxiv.org/abs/2403.03158)|null|
|**2024-03-05**|**On dynamics of gasless combustion in slowly varying periodic media: periodic fronts, their stability and propagation-extinction-diffusion-reignition pattern**|在本文中，我们在一维公式中，在点火温度动力学的假设下，考虑了无气燃烧的经典模型。当固体燃料的初始分布是一个大规模变化的空间周期函数时，我们研究了该模型中火焰前沿的传播。结果表明，在某些参数状态下，该模型支持周期性的行进前沿。推导并研究了火焰前锋速度的一个精确渐近公式。同时还探讨了周期前沿的稳定性，并导出了问题参数的一个临界条件。数值研究还表明，在一定的参数范围内，周期锋的不稳定性导致了传播-消光-扩散-重燃模式。 et.al.|[2403.03144](http://arxiv.org/abs/2403.03144)|null|
|**2024-03-05**|**Enhanced beam-beam modeling to include longitudinal variation during weak-strong simulation**|束流相互作用对环形对撞机的设计和运行提出了重大挑战，严重影响了它们的性能。特别是，在对撞机设计阶段，弱-强模拟方法对于研究单粒子动力学至关重要。本文评估了现有模型在弱-强模拟中的局限性，指出尽管它们准确地解释了弹弓效应引起的能量变化，但未能纳入纵向坐标变化（ $z$-变化）。为了解决这一差距，我们引入了两种新的转换，通过包括$z$-变化和弹弓效应引起的能量变化来增强平田的原始框架。通过严格的数学分析和广泛的弱-强模拟研究，我们验证了这些增强在实现更精确的梁-梁相互作用模拟方面的有效性。我们的结果表明，尽管$z$ -变化构成了一种高阶效应，并且在电子离子对撞机（EIC）的特定设计参数范围内不会显著影响发射度增长率，但改进的模型提供了更高的精度，特别是在涉及束流效应和其他随机扩散过程之间相互作用的情况下，以及在结合真实晶格模型的模拟中。 et.al.|[2403.03137](http://arxiv.org/abs/2403.03137)|null|
|**2024-03-05**|**NaturalSpeech 3: Zero-Shot Speech Synthesis with Factorized Codec and Diffusion Models**|尽管最近的大规模文本到语音（TTS）模型已经取得了显著的进展，但它们在语音质量、相似性和韵律方面仍然存在不足。考虑到语音复杂地包含各种属性（例如，内容、韵律、音色和声学细节），这些属性对生成提出了重大挑战，自然的想法是将语音分解为表示不同属性的各个子空间，并单独生成它们。受此启发，我们提出了NaturalSpeech3，这是一个具有新的因子化扩散模型的TTS系统，以零样本的方式生成自然语音。具体而言，1）我们设计了一种具有因子分解矢量量化（FVQ）的神经编解码器，以将语音波形分解为内容、韵律、音色和声学细节的子空间；2） 我们提出了一个因子分解扩散模型，在每个子空间中按照相应的提示生成属性。利用这种因子分解设计，NaturalSpeech3可以以分而治之的方式有效地对具有解纠缠子空间的复杂语音进行建模。实验表明，NaturalSpeech3在质量、相似性、韵律和可懂度方面优于最先进的TTS系统。此外，我们通过扩展到1B参数和200K小时的训练数据来实现更好的性能。 et.al.|[2403.03100](http://arxiv.org/abs/2403.03100)|null|
|**2024-03-05**|**Proof-of-concept for a nonadditive stochastic model of supercooled liquids**|最近提出的非加性随机模型（NSM）为玻璃成型系统中的扩散现象提供了一种相干的物理解释。该模型呈现了粘度、活化能和温度之间的非指数关系，表征了在过冷液体中观察到的非阿伦尼斯行为。在这项工作中，我们将NSM粘度方程与对应于25种玻璃形成液体的实验温度相关粘度数据进行拟合，并将拟合参数与使用Vogel-Fulcher-Tammann（VFT）、Avramov Milchev（AM）和Mauro Yue-Ellison Gupta-Alan（MYEGA）模型获得的拟合参数进行比较。结果表明，与其他已建立的模型（VFT、AM和MYEGA）相比，NSM为粘度实验数据的建模提供了一个有效的拟合方程，表征了脆性液体中的活化能，为玻璃形成液体的脆性程度提供了可靠的指标。 et.al.|[2403.03041](http://arxiv.org/abs/2403.03041)|null|
|**2024-03-05**|**Global N-body Simulation of Gap Edge Structures Created by Perturbations from a Small Satellite Embedded in Saturn's Rings**|旅行者号和卡西尼号宇宙飞船的观测揭示了土星环间隙结构的各种显著特征，如密度波、尖锐边缘和垂直壁结构。为了在单个模拟中解释这些特征，我们对嵌入卫星的间隙形成进行了高分辨率（N~10^6-10^7）的全球全N体模拟，考虑了所有环形粒子和卫星之间的引力相互作用和非弹性碰撞，而这些特征大多是用不同的理论方法分别研究的：流线模型、一维扩散模型和局部N体模拟。作为一系列论文的第一次尝试，我们在这里重点研究了通过将卫星迁移与将卫星轨道固定在开普勒环形轨道中来分离间隙的形成。我们揭示了引人注目的间隙特征-密度波、尖锐边缘和垂直壁结构-是如何由卫星环和环粒子-粒子相互作用的相互作用同时形成的。特别是，我们提出了一种新的机制来定量解释间隙边缘垂直墙结构的产生。环形粒子之间的非弹性碰撞阻尼了卫星扰动激发的离心率，以提高间隙边缘的表面密度，使其尖锐边缘更加明显。我们发现偏心阻尼过程不可避免地在第二次周期波中最有效地提高了垂直墙结构。粒子-粒子碰撞通常将其横向周转运动转换为垂直运动。由于激发的周转运动在环形边缘附近最大，并且周转运动在第一波中对齐，因此在第二波的间隙边缘转换效率最高，壁高由卫星Hill半径缩放，这与观测结果一致。 et.al.|[2403.03012](http://arxiv.org/abs/2403.03012)|null|

<p align=right>(<a href=#updated-on-20240306>back to top</a>)</p>

## NeRF

|Publish Date|Title|Abstract|PDF|Code|
|---|---|---|---|---|
|**2024-03-05**|**NRDF: Neural Riemannian Distance Fields for Learning Articulated Pose Priors**|忠实地为关节空间建模是一项关键任务，它可以恢复和生成逼真的姿势，而且仍然是一项臭名昭著的挑战。为此，我们引入了神经黎曼距离场（NRDF），这是一种数据驱动的先验，用于建模看似合理的关节空间，表示为高维乘积四元数空间中神经场的零级集。为了仅在正示例上训练NRDF，我们引入了一种新的采样算法，确保测地距离遵循所需的分布，从而产生一种原则性的距离场学习范式。然后，我们设计了一种投影算法，通过自适应步长黎曼优化器将任何随机姿态映射到水平集上，始终遵循关节旋转的乘积流形。NRDF可以通过反向传播和数学类比计算黎曼梯度，与最近的生成模型黎曼流匹配有关。我们在各种下游任务中，即姿态生成、基于图像的姿态估计和求解逆运动学，对照其他姿态先验对NRDF进行了全面评估，突出了NRDF的优越性能。除了人类，NRDF的多功能性还延伸到手和动物姿势，因为它可以有效地代表任何关节。 et.al.|[2403.03122](http://arxiv.org/abs/2403.03122)|null|
|**2024-03-04**|**MagicClay: Sculpting Meshes With Generative Neural Fields**|神经领域的最新发展为形状生成领域带来了非凡的能力，但它们缺乏关键的特性，例如增量控制，这是艺术作品的基本要求。另一方面，三角网格是大多数几何相关任务的选择，提供了高效和直观的控制，但不适用于神经优化。为了支持下游任务，现有技术通常提出两步方法，其中首先使用神经场生成形状，然后提取网格进行进一步处理。相反，在本文中，我们引入了一种混合方法，该方法保持网格和符号距离场（SDF）表示的一致性。使用这种表示，我们介绍了MagicClay——一种艺术家友好的工具，用于根据文本提示雕刻网格区域，同时保持其他区域不变。我们的框架仔细而有效地平衡了形状优化每一步中表示和正则化之间的一致性；依靠网格表示，我们展示了如何以更高的分辨率和更快的速度渲染SDF。此外，我们利用最近在可微网格重建方面的工作，在需要的地方自适应地分配网格中的三角形，如SDF所示。使用一个实现的原型，我们展示了与最先进的生成几何体相比的优越性，以及新颖的一致性控制，首次允许对同一网格进行基于提示的顺序编辑。 et.al.|[2403.02460](http://arxiv.org/abs/2403.02460)|null|
|**2024-03-04**|**Activity estimation via distributed measurements in an orientation sensitive neural fields model of the visual cortex**|本文在可观察性理论的框架下研究了初级视觉皮层（V1）内神经活动的在线估计。我们专注于对超体积活动建模的低维神经场，以描述V1中的活动。我们使用V1上的平均皮层活动作为测量。我们的贡献包括详细说明模型的可观察性奇点，并开发一种混合高增益观测器，该观测器在特定的激励条件下实现实际收敛，同时在生物相关性的情况下保持渐近收敛。该研究强调了模型的非线性性质与其可观测性之间的内在联系。我们还介绍了数值实验，强调了观测者的不同性质。 et.al.|[2403.01906](http://arxiv.org/abs/2403.01906)|null|
|**2024-03-02**|**Neural Field Classifiers via Target Encoding and Classification Loss**|神经场方法在计算机视觉和计算机图形学中的各种长期任务中取得了巨大进展，包括新颖的视图合成和几何重建。由于现有的神经场方法试图预测一些基于坐标的连续目标值，例如神经辐射场（NeRF）的RGB，所有这些方法都是回归模型，并通过一些回归损失进行优化。然而，对于神经场方法来说，回归模型真的比分类模型更好吗？在这项工作中，我们试图从机器学习的角度来探讨神经领域这个非常基本但被忽视的问题。我们成功地提出了一种新的神经场分类器（NFC）框架，该框架将现有的神经场方法公式化为分类任务，而不是回归任务。所提出的NFC可以通过使用新的目标编码模块和优化分类损失，轻松地将任意神经场回归器（NFR）转换为其分类变体。通过将连续回归目标编码为高维离散编码，我们自然地形成了多标签分类任务。大量的实验证明了NFC在几乎免费的额外计算成本下令人印象深刻的有效性。此外，NFC还显示出对稀疏输入、损坏图像和动态场景的鲁棒性。 et.al.|[2403.01058](http://arxiv.org/abs/2403.01058)|null|
|**2024-02-28**|**NERV++: An Enhanced Implicit Neural Video Representation**|神经场，也称为隐式神经表示（INRs），在表示、生成和操作各种数据类型方面表现出了非凡的能力，允许在低内存占用下进行连续的数据重建。尽管前景广阔，但应用于视频压缩的INRs仍需要大幅度提高其率失真性能，并且需要大量的参数和长时间的训练迭代来捕捉高频细节，这限制了其更广泛的适用性。解决这个问题仍然是一项极具挑战性的任务，这将使INR在压缩任务中更容易访问。我们通过引入视频的神经表示NeRV++朝着解决这些缺点迈出了一步，NeRV++是一种增强的隐式神经视频表示，是对原始NeRV解码器架构的更直接但有效的增强，其特征是夹着上采样块（UB）的可分离conv2d残差块（SCRB），以及用于改进特征表示的双线性插值跳过层。NeRV++允许将视频直接表示为神经网络近似的函数，并显著增强了当前基于INR的视频编解码器之外的表示能力。我们在UVG、MCL-JVC和Bunny数据集上评估了我们的方法，在INRs的视频压缩方面取得了有竞争力的结果。这一成果缩小了与基于自动编码器的视频编码的差距，标志着基于INR的视频压缩研究迈出了重要一步。 et.al.|[2402.18305](http://arxiv.org/abs/2402.18305)|null|
|**2024-02-27**|**NIIRF: Neural IIR Filter Field for HRTF Upsampling and Personalization**|头部相关传递函数（HRTF）对于沉浸式音频是重要的，并且已经研究了它们的空间插值来对有限测量进行上采样。近年来，从声源方向映射到HRTF的神经场（NF）引起了人们的关注。现有的基于NF的方法侧重于从给定的声源方向估计HRTF的幅度，并将该幅度转换为有限脉冲响应（FIR）滤波器。我们提出了神经无限冲激响应滤波器场（NIIRF）方法来估计级联IIR滤波器的系数。IIR滤波器模拟HRTF的模态特性，因此与FIR滤波器相比，需要更少的系数来很好地近似它们。我们发现，我们的方法可以在多个数据集上匹配现有的基于NF的方法的性能，甚至在测量稀疏时优于它们。我们还探索了将NF个性化到受试者的方法，并通过实验发现低秩自适应是有效的。 et.al.|[2402.17907](http://arxiv.org/abs/2402.17907)|**[link](https://github.com/merlresearch/neural-iir-field)**|
|**2024-02-27**|**AlignMiF: Geometry-Aligned Multimodal Implicit Field for LiDAR-Camera Joint Synthesis**|神经隐式场已经成为新视图合成中事实上的标准。最近，有一些方法探索在一个领域内融合多个模态，旨在共享不同模态的隐含特征，以提高重建性能。然而，这些模态往往表现出错位行为：对一种模态（如激光雷达）进行优化可能会对另一种模态产生不利影响，如相机性能，反之亦然。在这项工作中，我们对激光雷达相机联合合成的多模式隐场进行了全面分析，揭示了潜在的问题在于不同传感器的错位。此外，我们还介绍了AlignMiF，这是一个几何对齐的多模式隐式场，具有两个拟议的模块：几何感知对齐（GAA）和共享几何初始化（SGI）。这些模块有效地调整了不同模态的粗略几何结构，显著增强了激光雷达和相机数据之间的融合过程。通过在各种数据集和场景中进行广泛的实验，我们证明了我们的方法在促进激光雷达和相机模态之间在统一的神经场中更好地交互方面的有效性。具体而言，我们提出的AlignMiF比最近的隐式融合方法（KITTI-360和Waymo数据集上的图像PSNR分别为+2.01和+3.11）实现了显著的改进，并始终超过单模态性能（在各自的数据集上，激光雷达切角距离分别减少了13.8%和14.2%）。 et.al.|[2402.17483](http://arxiv.org/abs/2402.17483)|**[link](https://github.com/tangtaogo/alignmif)**|
|**2024-02-26**|**GEM3D: GEnerative Medial Abstractions for 3D Shape Synthesis**|我们介绍了GEM3D——一种新的深度、拓扑感知的三维形状生成模型。我们的方法的关键成分是基于神经骨架的表示，对形状拓扑和几何信息进行编码。通过去噪扩散概率模型，我们的方法首先根据中轴变换（MAT）生成基于骨架的表示，然后通过骨架驱动的神经隐式公式生成曲面。神经隐式考虑了存储在生成的骨架表示中的拓扑和几何信息，以产生与以前的神经场公式相比在拓扑和几何上更准确的曲面。我们讨论了我们的方法在形状合成和点云重建任务中的应用，并对我们的方法进行了定性和定量评估。与最先进的技术相比，我们展示了更忠实的表面重建和多样化的形状生成结果，还涉及从Thingi10K和ShapeNet重建和合成结构复杂的高属形表面的挑战性场景。 et.al.|[2402.16994](http://arxiv.org/abs/2402.16994)|null|
|**2024-02-21**|**Geometry-Informed Neural Networks**|我们引入了几何知情神经网络（GINN）的概念，它包括（i）在几何约束下的学习，（ii）作为适当表示的神经场，以及（iii）为几何任务中经常遇到的不确定系统生成不同的解决方案。值得注意的是，GINN公式不需要训练数据，因此可以被视为纯粹由约束驱动的生成建模。我们添加了一个明确的多样性损失来缓解模式崩溃。我们考虑了几个约束，特别是分量的连通性，我们通过Morse理论将其转化为可微损失。在实验上，我们展示了GINN学习范式在一系列二维和三维场景中的有效性，这些场景的复杂性不断增加。 et.al.|[2402.14009](http://arxiv.org/abs/2402.14009)|null|
|**2024-02-18**|**Pattern Recognition Facilities of Extended Kalman Filtering in Stochastic Neural Fields**|在数学神经科学中，人们特别关注在存在模型不确定性的情况下，由动态神经场（DNF）建模的神经组织中的工作记忆机制。工作记忆设施意味着，由于网络中反复的相互作用，在去除外部刺激后，神经元的活动保持自我维持，并允许系统处理丢失的传感器信息。在我们之前的工作中，我们已经根据传感器提供的不完整数据开发了两种神经膜电位的重建方法。这些方法是在扩展卡尔曼滤波方法中通过使用Euler Maruyama方法和\^{o}-Taylor订单1.5的扩展。它表明\^{o}-Taylor基于EKF的恢复过程比基于Euler Maruyama的替代方案更准确。在传感器信息不完整的情况下，它提高了膜电位重建的质量。本文的目的是研究它们的模式识别功能，即在模型不确定和信息不完整的情况下，模式形成重建的质量。数值实验是以神经组织中出现多个活动区的随机DNF为例提供的。 et.al.|[2402.11551](http://arxiv.org/abs/2402.11551)|null|

<p align=right>(<a href=#updated-on-20240306>back to top</a>)</p>

[contributors-shield]: https://img.shields.io/github/contributors/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[contributors-url]: https://github.com/Vincentqyw/cv-arxiv-daily/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[forks-url]: https://github.com/Vincentqyw/cv-arxiv-daily/network/members
[stars-shield]: https://img.shields.io/github/stars/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[stars-url]: https://github.com/Vincentqyw/cv-arxiv-daily/stargazers
[issues-shield]: https://img.shields.io/github/issues/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[issues-url]: https://github.com/Vincentqyw/cv-arxiv-daily/issues

