[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]

## Updated on 2024.03.07
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
|**2024-03-06**|**DART: Implicit Doppler Tomography for Radar Novel View Synthesis**|仿真对于射频系统设计者来说是一个非常宝贵的工具，它可以实现成像、目标检测、分类和跟踪的各种算法的快速原型设计。然而，模拟真实的雷达扫描是一项具有挑战性的任务，需要场景的准确模型、射频材料特性和相应的雷达合成功能。我们没有明确指定这些模型，而是提出了DART-多普勒辅助雷达层析成像，这是一种受神经辐射场启发的方法，它使用特定于雷达的物理来创建基于反射率和透射率的距离多普勒图像渲染管道。然后，我们通过构建一个定制的数据收集平台，收集一个新的雷达数据集，以及基于激光雷达的定位的准确位置和瞬时速度测量，来评估DART。与最先进的基线相比，DART从所有数据集的新视图合成了优越的雷达距离多普勒图像，此外还可用于生成高质量的断层图像。 et.al.|[2403.03896](http://arxiv.org/abs/2403.03896)|null|
|**2024-03-04**|**DaReNeRF: Direction-aware Representation for Dynamic Scenes**|为了应对建模和重新渲染动态场景的复杂挑战，最近的方法试图使用基于平面的显式表示来简化这些复杂性，克服了与神经辐射场（NeRF）和隐式表示等方法相关的训练时间慢的问题。然而，将4D动态场景直接分解为多个基于2D平面的表示被证明不足以重新渲染具有复杂运动的高保真场景。作为回应，我们提出了一种新的方向感知表示（DaRe）方法，该方法从六个不同的方向捕捉场景动力学。该学习的表示经过逆对偶树复小波变换（DTCWT）以恢复基于平面的信息。DaReNeRF通过融合来自这些恢复平面的向量来计算每个时空点的特征。将DaReNeRF与用于颜色回归的微小MLP相结合，并在训练中利用体积渲染，可以在复杂动态场景的新型视图合成中获得最先进的性能。值得注意的是，为了解决六个实数和六个虚数方向感知小波系数引入的冗余问题，我们引入了一种可训练的掩蔽方法，在不显著降低性能的情况下缓解了存储问题。此外，与现有技术相比，DaReNeRF保持了2倍的训练时间减少，同时提供了卓越的性能。 et.al.|[2403.02265](http://arxiv.org/abs/2403.02265)|null|
|**2024-03-04**|**Depth-Guided Robust and Fast Point Cloud Fusion NeRF for Sparse Input Views**|具有稀疏输入视图的新型视图合成对于AR/VR和自动驾驶等现实世界应用非常重要。最近的方法已经将深度信息集成到用于稀疏输入合成的NeRF中，利用深度先验进行几何和空间理解。然而，大多数现有的作品往往忽略了深度图中的不准确之处，并且时间效率较低。为了解决这些问题，我们提出了一种用于稀疏输入的深度引导鲁棒快速点云融合NeRF。我们将辐射场视为特征的显式体素网格。为每个输入视图构建一个点云，使用矩阵和向量在体素网格内进行特征化。我们累积每个输入视图的点云，以构建整个场景的融合点云。每个体素通过参考整个场景的点云来确定其密度和外观。通过点云融合和体素网格微调，深度值的不精确性可以被其他视图的不精确值细化或替换。此外，我们的方法可以通过有效的向量矩阵分解来实现更快的重建和更大的紧凑性。实验结果强调，与最先进的基线相比，我们的方法具有卓越的性能和时间效率。 et.al.|[2403.02063](http://arxiv.org/abs/2403.02063)|null|
|**2024-03-04**|**DD-VNB: A Depth-based Dual-Loop Framework for Real-time Visually Navigated Bronchoscopy**|支气管镜的实时6自由度定位对于提高干预质量至关重要。然而，当前基于视觉的技术难以在对看不见的数据的泛化和计算速度之间取得平衡。在这项研究中，我们提出了一种用于实时视觉导航支气管镜检查（DD-VNB）的基于深度的双环框架，该框架可以在不需要重新训练的情况下推广到患者病例中。DD-VNB框架集成了两个关键模块：深度估计和双环定位。为了解决患者之间的领域差距，我们提出了一种知识嵌入的深度估计网络，该网络将内窥镜帧映射到深度，通过消除患者特定的纹理来确保泛化。该网络将视图合成知识嵌入到循环对抗性架构中，用于尺度约束的单目深度估计。为了获得实时性能，我们的定位模块将快速自我运动估计网络嵌入深度配准循环中。自我运动推断网络以高频估计支气管镜的姿态变化，而相对于术前3D模型的深度配准周期性地提供绝对姿态。具体而言，将相对姿态变化作为初始猜测输入到配准过程中，以提高其准确性和速度。对来自患者的体模和体内数据的实验证明了我们框架的有效性：1）单目深度估计优于SOTA，2）定位在体模中实现了4.7 $\pm$3.17 mm的绝对跟踪误差（ATE）精度，在患者数据中实现了6.49$\pm$ 3.88 mm的绝对追踪误差，3）帧速率接近视频捕获速度，4）而不需要按情况进行网络再训练。该框架优越的速度和准确性证明了其在实时支气管镜导航方面的临床潜力。 et.al.|[2403.01683](http://arxiv.org/abs/2403.01683)|null|
|**2024-03-02**|**NeRF-VPT: Learning Novel View Representations with Neural Radiance Fields via View Prompt Tuning**|神经辐射场（NeRF）在新视图合成中取得了显著的成功。尽管如此，为新颖的视图生成高质量图像的任务仍然是一个关键的挑战。虽然现有的努力取得了值得称赞的进展，但捕捉复杂的细节、增强纹理和实现卓越的峰值信噪比（PSNR）指标值得进一步关注和进步。在这项工作中，我们提出了NeRF VPT，这是一种用于新视图合成的创新方法，以应对这些挑战。我们提出的NeRF VPT采用级联视图提示调整范式，其中从先前渲染结果中获得的RGB信息作为后续渲染阶段的指导性视觉提示，期望嵌入提示中的先验知识可以促进渲染图像质量的逐步增强。NeRF VPT只需要在每个训练阶段从前一阶段渲染中采样RGB数据作为先验，而不需要依赖额外的指导或复杂的技术。因此，我们的NeRF VPT是即插即用的，可以很容易地集成到现有的方法中。通过在要求苛刻的真实场景基准上对我们的NeRF VPT与几种基于NeRF的方法进行比较分析，如真实合成360、真实前向、副本数据集和用户捕获的数据集，我们证实，与所有最先进的方法相比，我们的NeRF VPT显著提高了基线性能，并能熟练地生成更高质量的新视图图像。此外，NeRF VPT的级联学习引入了对具有稀疏输入的场景的适应性，从而显著提高了稀疏视图新视图合成的准确性。源代码和数据集位于\url{https://github.com/Freedomcls/NeRF-VPT}. et.al.|[2403.01325](http://arxiv.org/abs/2403.01325)|**[link](https://github.com/freedomcls/nerf-vpt)**|
|**2024-03-02**|**Neural Field Classifiers via Target Encoding and Classification Loss**|神经场方法在计算机视觉和计算机图形学中的各种长期任务中取得了巨大进展，包括新颖的视图合成和几何重建。由于现有的神经场方法试图预测一些基于坐标的连续目标值，例如神经辐射场（NeRF）的RGB，所有这些方法都是回归模型，并通过一些回归损失进行优化。然而，对于神经场方法来说，回归模型真的比分类模型更好吗？在这项工作中，我们试图从机器学习的角度来探讨神经领域这个非常基本但被忽视的问题。我们成功地提出了一种新的神经场分类器（NFC）框架，该框架将现有的神经场方法公式化为分类任务，而不是回归任务。所提出的NFC可以通过使用新的目标编码模块和优化分类损失，轻松地将任意神经场回归器（NFR）转换为其分类变体。通过将连续回归目标编码为高维离散编码，我们自然地形成了多标签分类任务。大量的实验证明了NFC在几乎免费的额外计算成本下令人印象深刻的有效性。此外，NFC还显示出对稀疏输入、损坏图像和动态场景的鲁棒性。 et.al.|[2403.01058](http://arxiv.org/abs/2403.01058)|null|
|**2024-02-29**|**ViewFusion: Towards Multi-View Consistency via Interpolated Denoising**|通过扩散模型进行的新型视图合成在生成多样化和高质量图像方面表现出了显著的潜力。然而，在这些主流方法中，图像生成的独立过程导致了在保持多视图一致性方面的挑战。为了解决这一问题，我们引入了ViewFusion，这是一种新颖的无训练算法，可以无缝集成到现有的预训练扩散模型中。我们的方法采用了一种自回归方法，该方法隐式地利用先前生成的视图作为下一个视图生成的上下文，确保了在新视图生成过程中强大的多视图一致性。通过通过插值去噪融合已知视图信息的扩散过程，我们的框架成功地扩展了单视图条件模型，使其在多视图条件设置下工作，而无需任何额外的微调。大量的实验结果证明了ViewFusion在生成一致且详细的新视图方面的有效性。 et.al.|[2402.18842](http://arxiv.org/abs/2402.18842)|**[link](https://github.com/Wi-sc/ViewFusion)**|
|**2024-02-28**|**PolyOculus: Simultaneous Multi-view Image-based Novel View Synthesis**|本文考虑了生成新视图合成（GNVS）的问题，即在给定有限数量的已知视图的情况下生成场景的新颖、合理的视图。在这里，我们提出了一个基于集合的生成模型，该模型可以同时生成多个自洽的新视图，条件是任何数量的已知视图。我们的方法不限于一次生成单个图像，并且可以以零、一个或多个视图为条件。因此，当生成大量视图时，我们的方法不限于低阶自回归生成方法，并且能够更好地在大图像集上保持生成的图像质量。我们在标准NVS数据集上评估了所提出的模型，并表明它优于最先进的基于图像的GNVS基线。此外，我们表明，该模型能够生成没有自然顺序的相机视图集，如循环和双目轨迹，并且在此类任务上显著优于其他方法。 et.al.|[2402.17986](http://arxiv.org/abs/2402.17986)|null|
|**2024-02-27**|**AlignMiF: Geometry-Aligned Multimodal Implicit Field for LiDAR-Camera Joint Synthesis**|神经隐式场已经成为新视图合成中事实上的标准。最近，有一些方法探索在一个领域内融合多个模态，旨在共享不同模态的隐含特征，以提高重建性能。然而，这些模态往往表现出错位行为：对一种模态（如激光雷达）进行优化可能会对另一种模态产生不利影响，如相机性能，反之亦然。在这项工作中，我们对激光雷达相机联合合成的多模式隐场进行了全面分析，揭示了潜在的问题在于不同传感器的错位。此外，我们还介绍了AlignMiF，这是一个几何对齐的多模式隐式场，具有两个拟议的模块：几何感知对齐（GAA）和共享几何初始化（SGI）。这些模块有效地调整了不同模态的粗略几何结构，显著增强了激光雷达和相机数据之间的融合过程。通过在各种数据集和场景中进行广泛的实验，我们证明了我们的方法在促进激光雷达和相机模态之间在统一的神经场中更好地交互方面的有效性。具体而言，我们提出的AlignMiF比最近的隐式融合方法（KITTI-360和Waymo数据集上的图像PSNR分别为+2.01和+3.11）实现了显著的改进，并始终超过单模态性能（在各自的数据集上，激光雷达切角距离分别减少了13.8%和14.2%）。 et.al.|[2402.17483](http://arxiv.org/abs/2402.17483)|**[link](https://github.com/tangtaogo/alignmif)**|
|**2024-02-26**|**GEA: Reconstructing Expressive 3D Gaussian Avatar from Monocular Video**|本文提出了GEA，这是一种基于3D高斯的身体和手的高保真重建来创建富有表现力的3D化身的新方法。关键贡献有两方面。首先，我们设计了一种两阶段姿态估计方法，以从输入图像中获得准确的SMPL-X姿态，从而在训练图像的像素和SMPL-X模型之间提供正确的映射。它使用注意力感知网络和优化方案来对齐图像中估计的SMPL-X身体和真实身体之间的法线和轮廓。其次，我们提出了一种迭代重新初始化策略来处理高斯表示所面临的不平衡聚合和初始化偏差。该策略迭代地重新分布化身的高斯点，通过应用网格划分、重采样和重高斯运算，使其均匀分布在人体表面附近。结果，可以实现更高质量的渲染。大量的实验分析验证了所提出的模型的有效性，表明它在逼真的新视图合成中实现了最先进的性能，同时提供了对人体和手部姿势的细粒度控制。项目页面：https://3d-aigc.github.io/GEA/. et.al.|[2402.16607](http://arxiv.org/abs/2402.16607)|null|

<p align=right>(<a href=#updated-on-20240307>back to top</a>)</p>

## 3D Reconstruction

|Publish Date|Title|Abstract|PDF|Code|
|---|---|---|---|---|
|**2024-03-05**|**Pooling Image Datasets With Multiple Covariate Shift and Imbalance**|小样本量在许多学科中很常见，这就需要在多个机构中汇集大致相似的数据集，以研究图像和疾病结果之间微弱但相关的关联。这种数据通常表现出协变量（即二次非成像数据）的偏移/不平衡。控制这种干扰变量在标准统计分析中很常见，但这些想法并不直接适用于参数过大的模型。因此，最近的工作表明，来自不变表示学习的策略是如何提供一个有意义的起点的，但目前的方法仅限于一次只考虑几个协变量的变化/不平衡。在本文中，我们展示了如何从范畴理论的角度看待这个问题，提供了一个简单有效的解决方案，完全避免了原本需要的复杂的多阶段训练管道。我们通过在真实数据集上进行的大量实验证明了这种方法的有效性。此外，我们讨论了这种形式的公式如何为至少5个以上不同的问题设置提供统一的视角，从自监督学习到3D重建中的匹配问题。 et.al.|[2403.02598](http://arxiv.org/abs/2403.02598)|null|
|**2024-03-04**|**DragTex: Generative Point-Based Texture Editing on 3D Mesh**|最近，使用生成人工智能创建3D纹理网格引起了人们的极大关注。虽然现有方法支持在3D网格上基于文本的生成纹理生成或编辑，但它们往往难以通过更直观的交互来精确控制纹理图像的像素。虽然2D图像可以使用拖动交互进行生成编辑，但将这种类型的方法直接应用于3D网格纹理仍然会导致多个视图之间缺乏局部一致性、错误累积和训练时间长等问题。为了解决这些挑战，我们提出了一种基于生成点的3D网格纹理编辑方法，称为DragTex。该方法利用扩散模型在不同视图之间混合变形轮廓附近区域中的局部不一致纹理，从而实现局部一致的纹理编辑。此外，我们对解码器进行微调，以减少非拖动区域的重建误差，从而减少总体误差积累。此外，我们使用多视图图像来训练LoRA，而不是单独训练每个视图，这显著缩短了训练时间。实验结果表明，我们的方法有效地实现了3D网格上的拖动纹理，并生成了符合拖动交互所需意图的合理纹理。 et.al.|[2403.02217](http://arxiv.org/abs/2403.02217)|null|
|**2024-03-04**|**TripoSR: Fast 3D Object Reconstruction from a Single Image**|本技术报告介绍了TripoSR，这是一种利用变压器架构进行快速前馈3D生成的3D重建模型，可在0.5秒内从单个图像生成3D网格。基于LRM网络架构，TripoSR集成了数据处理、模型设计和训练技术方面的实质性改进。对公共数据集的评估表明，与其他开源替代品相比，TripoSR在数量和质量上都表现出优异的性能。TripoSR是根据麻省理工学院的许可发布的，旨在为研究人员、开发人员和创意人员提供3D生成人工智能的最新进展。 et.al.|[2403.02151](http://arxiv.org/abs/2403.02151)|**[link](https://github.com/vast-ai-research/triposr)**|
|**2024-03-03**|**A Novel Dynamic Light-Section 3D Reconstruction Method for Wide-Range Sensing**|现有的基于检流计的激光扫描系统在多尺度3D重建中的应用具有挑战性，因为难以在高重建精度和宽重建范围之间实现平衡。本文提出了一种新的方法，通过使用多电流计切换相机的视场来同步激光扫描。除了先进的硬件设置外，我们还通过建模动态相机、动态激光器及其组合交互，建立了系统的综合数学模型。然后，我们通过构建误差模型并最小化目标函数，提出了一种高精度、灵活的校准方法。最后，我们通过扫描标准组件来评估所提出的系统的性能。评估结果表明，当测量范围扩展到1100 mm $\times$1300 mm$\imes$ 650 mm时，所提出的三维重建系统的精度达到0.3 mm。在相同的重建精度下，重建范围扩展了25倍，表明所提出的方法同时允许在工业应用中进行高精度和宽范围的3D重建。 et.al.|[2403.01374](http://arxiv.org/abs/2403.01374)|null|
|**2024-03-01**|**G3DR: Generative 3D Reconstruction in ImageNet**|我们介绍了一种新的3D生成方法，即ImageNet中的生成3D重建（G3DR），该方法能够从单个图像中生成各种高质量的3D对象，解决了现有方法的局限性。我们框架的核心是一种新颖的深度正则化技术，它能够生成具有高几何保真度的场景。G3DR还利用预训练的语言视觉模型，如CLIP，实现新视图中的重建，并提高几代人的视觉逼真度。此外，G3DR设计了一种简单但有效的采样程序，以进一步提高世代的质量。G3DR提供基于类或文本条件的多样化且高效的3D资产生成。尽管G3DR很简单，但它能够击败最先进的方法，在感知指标和几何得分方面比它们提高了22%和90%，而只需要一半的训练时间。代码位于https://github.com/preddy5/G3DR et.al.|[2403.00939](http://arxiv.org/abs/2403.00939)|null|
|**2024-03-01**|**DISORF: A Distributed Online NeRF Training and Rendering Framework for Mobile Robots**|我们提出了一个框架DISORF，用于对资源受限的移动机器人和边缘设备捕获的场景进行在线3D重建和可视化。为了解决边缘设备的有限计算能力和潜在的有限网络可用性，我们设计了一个在边缘设备和远程服务器之间有效分配计算的框架。我们利用设备上的SLAM系统生成姿势关键帧，并将其传输到远程服务器，远程服务器可以通过利用NeRF模型在运行时执行高质量的3D重建和可视化。我们发现了在线NeRF训练的一个关键挑战，在该挑战中，天真的图像采样策略可能导致渲染质量的显著下降。我们提出了一种新的移位指数帧采样方法，以解决在线NeRF训练的这一挑战。我们展示了我们的框架在实现未知场景的高质量实时重建和可视化方面的有效性，因为这些场景是从移动机器人和边缘设备中的相机捕获和流式传输的。 et.al.|[2403.00228](http://arxiv.org/abs/2403.00228)|null|
|**2024-03-05**|**VEnvision3D: A Synthetic Perception Dataset for 3D Multi-Task Model Research**|开发统一的多任务基础模型已成为计算机视觉研究中的一个关键挑战。在当前的三维计算机视觉领域，大多数数据集只关注单个任务，这使各种下游任务的并行训练需求变得复杂。在本文中，我们介绍了VEnvision3D，这是一个用于多任务学习的大型3D合成感知数据集，包括深度完成、分割、上采样、位置识别和3D重建。由于每个任务的数据都是在同一环境域中收集的，因此子任务在使用的数据方面是固有的一致性。因此，这样一个独特的属性可以帮助探索多任务模型甚至基础模型的潜力，而无需单独的训练方法。同时，利用虚拟环境可自由编辑的优势，我们实现了一些新颖的设置，如模拟环境的时间变化和在模型表面采样点云。这些特点使我们能够提出几个新的基准。我们还对多任务端到端模型进行了广泛的研究，揭示了新的观察结果、挑战和未来研究的机会。我们的数据集和代码将在接受后开源。 et.al.|[2402.19059](http://arxiv.org/abs/2402.19059)|null|
|**2024-02-29**|**ViewFusion: Towards Multi-View Consistency via Interpolated Denoising**|通过扩散模型进行的新型视图合成在生成多样化和高质量图像方面表现出了显著的潜力。然而，在这些主流方法中，图像生成的独立过程导致了在保持多视图一致性方面的挑战。为了解决这一问题，我们引入了ViewFusion，这是一种新颖的无训练算法，可以无缝集成到现有的预训练扩散模型中。我们的方法采用了一种自回归方法，该方法隐式地利用先前生成的视图作为下一个视图生成的上下文，确保了在新视图生成过程中强大的多视图一致性。通过通过插值去噪融合已知视图信息的扩散过程，我们的框架成功地扩展了单视图条件模型，使其在多视图条件设置下工作，而无需任何额外的微调。大量的实验结果证明了ViewFusion在生成一致且详细的新视图方面的有效性。 et.al.|[2402.18842](http://arxiv.org/abs/2402.18842)|**[link](https://github.com/Wi-sc/ViewFusion)**|
|**2024-02-28**|**The Role of a Neutron Component in the Photospheric Emission of Long-Duration Gamma-Ray Burst Jets**|长时间伽马射线暴（LGRB）被认为是在核心坍塌超新星期间产生的，可能在流出物质中有显著的中子成分。如果存在，中子可以通过降低其不透明度来改变光子在外流中的散射方式，从而使光子比没有中子的情况下更快地解耦。因此，了解这一过程的细节可以让我们探索LGRB的中心引擎，否则它是隐藏的。在这里，我们使用相对论流体动力学模拟和使用蒙特卡罗辐射转移（MCRaT）代码的辐射转移后处理相结合的方法，给出了LGRB喷流的光球发射结果。我们通过改变平衡电子分数 $Y_｛e｝$来控制喷流材料中中子组分的大小，我们发现GRB火球中中子的存在会影响能带参数$\alpha$和$e_｛0｝$，而带有$\beta$参数的图片则不太清楚。特别地，断裂能量$E_{0}$ 被转移到更高的能量。此外，我们发现，增加中子分量的大小也会增加多个视角下流出的总辐射能量。我们的研究结果不仅揭示了LGRB，而且与与双星中子星合并相关的短时间伽马射线爆发有关，因为在这样的系统中可能存在突出的中子成分。 et.al.|[2402.18657](http://arxiv.org/abs/2402.18657)|null|
|**2024-02-27**|**Sora Generates Videos with Stunning Geometrical Consistency**|最近开发的索拉模型[1]在视频生成方面表现出了非凡的能力，引发了关于其模拟真实世界现象能力的激烈讨论。尽管它越来越受欢迎，但缺乏既定的指标来定量评估它对现实世界物理的保真度。在本文中，我们介绍了一种新的基准，该基准基于视频对真实世界物理原理的遵守程度来评估生成视频的质量。我们采用了一种将生成的视频转换为3D模型的方法，利用了3D重建的准确性在很大程度上取决于视频质量的前提。从3D重建的角度来看，我们使用所构建的3D模型所满足的几何约束的保真度作为代理来衡量生成的视频在多大程度上符合真实世界的物理规则。项目页面：https://sora-geometrical-consistency.github.io/ et.al.|[2402.17403](http://arxiv.org/abs/2402.17403)|null|

<p align=right>(<a href=#updated-on-20240307>back to top</a>)</p>

## Diffusion

|Publish Date|Title|Abstract|PDF|Code|
|---|---|---|---|---|
|**2024-03-06**|**3D Diffusion Policy**|模仿学习为教授机器人灵巧技能提供了一种有效的途径；然而，稳健和概括地学习复杂的技能通常需要大量的人类演示。为了解决这一具有挑战性的问题，我们提出了3D扩散策略（DP3），这是一种新颖的视觉模仿学习方法，将3D视觉表示的力量融入到扩散策略中，这是一群条件动作生成模型。DP3的核心设计是利用高效的点编码器从稀疏点云中提取的紧凑的3D视觉表示。在我们涉及72个模拟任务的实验中，DP3仅用10个演示就成功地处理了大多数任务，并以55.3%的相对改进超过了基线。在4个真实的机器人任务中，DP3演示了精确控制，每个任务只演示了40次，成功率高达85%，并在空间、视点、外观和实例等多个方面表现出了出色的泛化能力。有趣的是，在真实的机器人实验中，DP3很少违反安全要求，而基线方法经常这样做，需要人工干预。我们的广泛评估强调了3D表示在现实世界机器人学习中的关键重要性。视频、代码和数据可在https://3d-diffusion-policy.github.io . et.al.|[2403.03954](http://arxiv.org/abs/2403.03954)|**[link](https://github.com/YanjieZe/3D-Diffusion-Policy)**|
|**2024-03-06**|**GUIDE: Guidance-based Incremental Learning with Diffusion Models**|我们介绍了GUIDE，这是一种新颖的持续学习方法，它指导扩散模型在有被遗忘风险的情况下排练样本。现有的生成策略通过从生成模型中随机抽取排练示例来对抗灾难性遗忘。这种方法与采样策略发挥重要作用的基于缓冲区的方法相矛盾。我们建议通过将扩散模型与分类器引导技术相结合来弥补这一差距，以产生专门针对被连续训练的模型遗忘的信息的排练示例。这种方法能够从先前的任务分布中生成样本，这些样本在最近遇到的类的上下文中更有可能被错误分类。我们的实验结果表明，在具有生成重放的持续学习中，GUIDE显著减少了灾难性遗忘，优于传统的随机抽样方法，并超过了最近最先进的方法。 et.al.|[2403.03938](http://arxiv.org/abs/2403.03938)|null|
|**2024-03-06**|**Hierarchical Diffusion Policy for Kinematics-Aware Multi-Task Robotic Manipulation**|本文介绍了一种用于多任务机器人操作的层次代理——层次扩散策略（HDP）。HDP将操纵策略分解为层次结构：高级任务规划代理预测远处的下一个最佳末端效应器姿势（NBP），以及低级目标条件扩散策略生成最佳运动轨迹。因子化策略表示允许HDP处理长期任务规划，同时生成细粒度的低级别操作。为了在满足机器人运动学约束的情况下生成上下文感知的运动轨迹，我们提出了一种新的运动学感知目标条件控制代理——机器人运动学扩散器（RK扩散器）。具体而言，RK扩散器学习生成末端效应器姿势和关节位置轨迹，并通过可微分运动学将精确但不了解运动学的末端效应器姿态扩散器提取为了解运动学但不太准确的关节位置扩散器。从经验上讲，我们表明HDP在模拟和现实世界中都比最先进的方法获得了更高的成功率。 et.al.|[2403.03890](http://arxiv.org/abs/2403.03890)|null|
|**2024-03-06**|**Towards a Schauder theory for fractional viscous Hamilton--Jacobi equations**|我们研究了具有次临界L’evy扩散的粘性Hamilton-Jacobi方程的Lipschitz和Schauder正则性估计的一些结果。借助于Duhamel公式和热核空间导数的 $L^1$ 界，得到了Schauder估计以及光滑解的存在性。我们的结果涵盖了非常普遍的非局部和混合局部非局部扩散，包括强各向异性、非对称、混合阶和谱单侧模型。 et.al.|[2403.03884](http://arxiv.org/abs/2403.03884)|null|
|**2024-03-06**|**Latent Dataset Distillation with Diffusion Models**|传统上，机器学习的有效性依赖于越来越大的数据集的可用性。然而，大型数据集带来了存储挑战，并且包含不具影响力的样本，在训练过程中可以忽略这些样本，而不会影响模型的最终准确性。为了应对这些限制，出现了将数据集上的信息提取为一组浓缩的（合成）样本的概念，即提取数据集。一个关键方面是用于链接原始数据集和合成数据集的选定架构（通常为ConvNet）。然而，如果所采用的模型架构与蒸馏过程中使用的模型不同，则最终精度较低。另一个挑战是生成高分辨率图像，例如128x128及更高分辨率的图像。在本文中，我们提出了具有扩散模型的潜在数据集蒸馏（LD3M），该模型将潜在空间中的扩散与数据集蒸馏相结合，以应对这两个挑战。LD3M结合了一种为数据集提取量身定制的新扩散过程，它改进了学习合成图像的梯度规范。通过调整扩散步骤的数量，LD3M还提供了一种控制速度和精度之间权衡的直接方法。我们在几个ImageNet子集和高分辨率图像（128x128和256x256）中评估了我们的方法。因此，对于每类1张和10张图像，LD3M始终优于最先进的蒸馏技术，分别高达4.8和4.2张。 et.al.|[2403.03881](http://arxiv.org/abs/2403.03881)|null|
|**2024-03-06**|**Convergence rate of the Smoluchowski-Kramers approximation for diffusions with jumps**|本文利用Kolmogorov距离研究了具有跳跃的扩散的Smoluchowski Kramers近似。收敛速度由Malliavin微积分导出。 et.al.|[2403.03877](http://arxiv.org/abs/2403.03877)|null|
|**2024-03-06**|**Accelerating Convergence of Score-Based Diffusion Models, Provably**|基于分数的扩散模型虽然取得了显著的经验性能，但由于采样阶段需要进行广泛的函数评估，因此采样速度往往较低。尽管最近在实践中进行了一系列加速扩散生成建模的活动，但加速技术的理论基础仍然非常有限。在本文中，我们设计了新的无训练算法来加速流行的确定性（即DDIM）和随机性（即DDPM）采样器。我们的加速确定性采样器以 $O（1/{T}^2）$的速率收敛，步骤数为$T$，改进了DDIM采样器的$O（1T）$速率；并且我们的加速随机采样器以$O（1/T）$的速率收敛，优于DDPM采样器的速率$O（1\\sqrt{T}）$。我们算法的设计利用了高阶近似的见解，并与DPM-Solver-2等流行的高阶ODE解算器有着相似的直觉。我们的理论适用于$\ell_2$ 精确的分数估计，并且不要求目标分布的对数凹性或光滑性。 et.al.|[2403.03852](http://arxiv.org/abs/2403.03852)|null|
|**2024-03-06**|**Two 100 TeV neutrinos coincident with the Seyfert galaxy NGC 7469**|2013年，冰立方合作组织宣布探测到一种弥漫的高能天体物理中微子通量。这种通量的起源在很大程度上仍然未知。最重要的单个来源是靠近塞弗特星系NGC 1068的4.2格玛级，光谱指数较低。为了根据其对应物识别来源，IceCube发布了与天体物理起源概率较高的中微子相对应的实时警报。我们在这里报道了两个中微子警报，IC220424A和IC230416A，与塞弗特星系NGC 7469在70 Mpc的距离上的空间重合。我们对这种巧合的偶然概率进行了后验评估，并根据其多波长特性和与NGC 1068的比较，将其作为中微子发射器进行了讨论。为了计算考虑来自特定源群体的中微子发射的偶然巧合，我们使用从包括中微子角不确定性和源距离的似然比导出的测试统计量进行拟合优度测试。我们首先将这个测试应用于AGN源目录，其次仅应用于Seyfert星系目录。我们的后验评估排除了这两个中微子与塞弗特星系NGC 7469在3.3西格玛水平上的偶然重合。为了与未探测到的TeV中微子兼容，该源需要具有硬光谱指数。 et.al.|[2403.03752](http://arxiv.org/abs/2403.03752)|null|
|**2024-03-06**|**Diffusion on language model embeddings for protein sequence generation**|蛋白质设计需要深入了解蛋白质宇宙的内在复杂性。尽管许多努力都倾向于有条件生成或专注于特定的蛋白质家族，但无条件生成的基本任务仍然没有得到充分的探索和低估。在这里，我们探索了这个关键领域，引入了DiMA，这是一个利用来自蛋白质语言模型ESM-2的嵌入的连续扩散来生成氨基酸序列的模型。DiMA超越了领先的解决方案，包括基于自回归变换器和离散扩散模型，我们定量地说明了设计选择对其卓越性能的影响。我们使用各种模式的多个指标广泛评估生成序列的质量、多样性、分布相似性和生物相关性。我们的方法始终如一地产生新的、多样的蛋白质序列，这些序列准确地反映了蛋白质空间固有的结构和功能多样性。这项工作通过为可扩展和高质量的蛋白质序列生成提供强大的框架，推进了蛋白质设计领域，并为条件模型奠定了基础。 et.al.|[2403.03726](http://arxiv.org/abs/2403.03726)|null|
|**2024-03-06**|**Spectral Algorithms on Manifolds through Diffusion**|现有的关于谱算法的研究主要集中在一般的核函数上，而忽略了输入特征空间的固有结构。我们的论文引入了一个新的视角，断言输入数据位于嵌入在高维欧几里得空间中的低维流形内。我们研究了RKHS中谱算法的收敛性能，特别是由热核生成的算法，即扩散空间。结合输入的流形结构，我们使用积分算子技术导出关于广义范数的紧收敛上界，这表明估计量在强意义上收敛到目标函数，这意味着函数本身及其导数同时收敛。这些边界提供了两个显著的优势：首先，它们完全取决于输入流形的内在维度，从而提供更集中的分析。其次，它们能够有效地推导任何k阶导数的收敛速度，所有这些都可以在相同的谱算法的范围内完成。此外，我们建立了极小极大下界，以证明这些结论在特定情况下的渐近最优性。我们的研究证实，谱算法在更广泛的高维近似背景下具有实际意义。 et.al.|[2403.03669](http://arxiv.org/abs/2403.03669)|null|

<p align=right>(<a href=#updated-on-20240307>back to top</a>)</p>

## NeRF

|Publish Date|Title|Abstract|PDF|Code|
|---|---|---|---|---|
|**2024-03-06**|**ProxNF: Neural Field Proximal Training for High-Resolution 4D Dynamic Image Reconstruction**|精确的时空图像重建方法被广泛的生物医学研究领域所需要，但由于数据的不完整性和计算负担而面临挑战。数据不完整性源于增加帧速率和减少采集时间所需的欠采样，而计算负担则源于具有三维空间和扩展时间范围的高分辨率图像的内存占用。神经场是一类新兴的神经网络，充当时空对象的连续表示，以前已经引入它来通过将图像重建重新定义为估计网络参数的问题来解决这些动态成像问题。神经场可以通过利用这些时空对象中潜在的冗余来解决数据不完整和计算负担这两个挑战。这项工作提出了ProxNF，这是一种用于时空图像重建的新的神经场训练方法，利用近端分裂方法将涉及成像算子的计算与网络参数的更新分开。具体而言，ProxNF评估图像域中数据保真度项的（子采样）梯度，并使用完全监督学习方法来更新神经场参数。通过减少内存占用和评估成像算子的计算成本，所提出的ProxNF方法允许重建大的、高分辨率的时空图像。该方法在两项数值研究中得到了证明，这两项研究涉及解剖逼真的动态数值小鼠模型和肿瘤灌注的两室模型的虚拟动态对比增强光声计算机断层扫描成像。 et.al.|[2403.03860](http://arxiv.org/abs/2403.03860)|null|
|**2024-03-05**|**NRDF: Neural Riemannian Distance Fields for Learning Articulated Pose Priors**|忠实地为关节空间建模是一项关键任务，它可以恢复和生成逼真的姿势，而且仍然是一项臭名昭著的挑战。为此，我们引入了神经黎曼距离场（NRDF），这是一种数据驱动的先验，用于建模看似合理的关节空间，表示为高维乘积四元数空间中神经场的零级集。为了仅在正示例上训练NRDF，我们引入了一种新的采样算法，确保测地距离遵循所需的分布，从而产生一种原则性的距离场学习范式。然后，我们设计了一种投影算法，通过自适应步长黎曼优化器将任何随机姿态映射到水平集上，始终遵循关节旋转的乘积流形。NRDF可以通过反向传播和数学类比计算黎曼梯度，与最近的生成模型黎曼流匹配有关。我们在各种下游任务中，即姿态生成、基于图像的姿态估计和求解逆运动学，对照其他姿态先验对NRDF进行了全面评估，突出了NRDF的优越性能。除了人类，NRDF的多功能性还延伸到手和动物姿势，因为它可以有效地代表任何关节。 et.al.|[2403.03122](http://arxiv.org/abs/2403.03122)|null|
|**2024-03-04**|**MagicClay: Sculpting Meshes With Generative Neural Fields**|神经领域的最新发展为形状生成领域带来了非凡的能力，但它们缺乏关键的特性，例如增量控制，这是艺术作品的基本要求。另一方面，三角网格是大多数几何相关任务的选择，提供了高效和直观的控制，但不适用于神经优化。为了支持下游任务，现有技术通常提出两步方法，其中首先使用神经场生成形状，然后提取网格进行进一步处理。相反，在本文中，我们引入了一种混合方法，该方法保持网格和符号距离场（SDF）表示的一致性。使用这种表示，我们介绍了MagicClay——一种艺术家友好的工具，用于根据文本提示雕刻网格区域，同时保持其他区域不变。我们的框架仔细而有效地平衡了形状优化每一步中表示和正则化之间的一致性；依靠网格表示，我们展示了如何以更高的分辨率和更快的速度渲染SDF。此外，我们利用最近在可微网格重建方面的工作，在需要的地方自适应地分配网格中的三角形，如SDF所示。使用一个实现的原型，我们展示了与最先进的生成几何体相比的优越性，以及新颖的一致性控制，首次允许对同一网格进行基于提示的顺序编辑。 et.al.|[2403.02460](http://arxiv.org/abs/2403.02460)|null|
|**2024-03-04**|**Activity estimation via distributed measurements in an orientation sensitive neural fields model of the visual cortex**|本文在可观察性理论的框架下研究了初级视觉皮层（V1）内神经活动的在线估计。我们专注于对超体积活动建模的低维神经场，以描述V1中的活动。我们使用V1上的平均皮层活动作为测量。我们的贡献包括详细说明模型的可观察性奇点，并开发一种混合高增益观测器，该观测器在特定的激励条件下实现实际收敛，同时在生物相关性的情况下保持渐近收敛。该研究强调了模型的非线性性质与其可观测性之间的内在联系。我们还介绍了数值实验，强调了观测者的不同性质。 et.al.|[2403.01906](http://arxiv.org/abs/2403.01906)|null|
|**2024-03-02**|**Neural Field Classifiers via Target Encoding and Classification Loss**|神经场方法在计算机视觉和计算机图形学中的各种长期任务中取得了巨大进展，包括新颖的视图合成和几何重建。由于现有的神经场方法试图预测一些基于坐标的连续目标值，例如神经辐射场（NeRF）的RGB，所有这些方法都是回归模型，并通过一些回归损失进行优化。然而，对于神经场方法来说，回归模型真的比分类模型更好吗？在这项工作中，我们试图从机器学习的角度来探讨神经领域这个非常基本但被忽视的问题。我们成功地提出了一种新的神经场分类器（NFC）框架，该框架将现有的神经场方法公式化为分类任务，而不是回归任务。所提出的NFC可以通过使用新的目标编码模块和优化分类损失，轻松地将任意神经场回归器（NFR）转换为其分类变体。通过将连续回归目标编码为高维离散编码，我们自然地形成了多标签分类任务。大量的实验证明了NFC在几乎免费的额外计算成本下令人印象深刻的有效性。此外，NFC还显示出对稀疏输入、损坏图像和动态场景的鲁棒性。 et.al.|[2403.01058](http://arxiv.org/abs/2403.01058)|null|
|**2024-02-28**|**NERV++: An Enhanced Implicit Neural Video Representation**|神经场，也称为隐式神经表示（INRs），在表示、生成和操作各种数据类型方面表现出了非凡的能力，允许在低内存占用下进行连续的数据重建。尽管应用于视频压缩的INRs很有前景，但仍需要大幅度提高其率失真性能，并且需要大量的参数和长时间的训练迭代来捕捉高频细节，限制了其更广泛的适用性。解决这个问题仍然是一项极具挑战性的任务，这将使INR在压缩任务中更容易访问。我们通过引入视频的神经表示NeRV++朝着解决这些缺点迈出了一步，NeRV++是一种增强的隐式神经视频表示，是对原始NeRV解码器架构的更直接但有效的增强，其特征是夹着上采样块（UB）的可分离conv2d残差块（SCRB），以及用于改进特征表示的双线性插值跳过层。NeRV++允许将视频直接表示为神经网络近似的函数，并显著增强了当前基于INR的视频编解码器之外的表示能力。我们在UVG、MCL-JVC和Bunny数据集上评估了我们的方法，在INRs的视频压缩方面取得了有竞争力的结果。这一成果缩小了与基于自动编码器的视频编码的差距，标志着基于INR的视频压缩研究迈出了重要一步。 et.al.|[2402.18305](http://arxiv.org/abs/2402.18305)|null|
|**2024-02-27**|**NIIRF: Neural IIR Filter Field for HRTF Upsampling and Personalization**|头部相关传递函数（HRTF）对于沉浸式音频是重要的，并且已经研究了它们的空间插值来对有限测量进行上采样。近年来，从声源方向映射到HRTF的神经场（NF）引起了人们的关注。现有的基于NF的方法侧重于从给定的声源方向估计HRTF的幅度，并将该幅度转换为有限脉冲响应（FIR）滤波器。我们提出了神经无限冲激响应滤波器场（NIIRF）方法来估计级联IIR滤波器的系数。IIR滤波器模拟HRTF的模态特性，因此与FIR滤波器相比，需要更少的系数来很好地近似它们。我们发现，我们的方法可以在多个数据集上匹配现有的基于NF的方法的性能，甚至在测量稀疏时优于它们。我们还探索了将NF个性化到受试者的方法，并通过实验发现低秩自适应是有效的。 et.al.|[2402.17907](http://arxiv.org/abs/2402.17907)|**[link](https://github.com/merlresearch/neural-iir-field)**|
|**2024-02-27**|**AlignMiF: Geometry-Aligned Multimodal Implicit Field for LiDAR-Camera Joint Synthesis**|神经隐式场已经成为新视图合成中事实上的标准。最近，有一些方法探索在一个领域内融合多个模态，旨在共享不同模态的隐含特征，以提高重建性能。然而，这些模态往往表现出错位行为：对一种模态（如激光雷达）进行优化可能会对另一种模态产生不利影响，如相机性能，反之亦然。在这项工作中，我们对激光雷达相机联合合成的多模式隐场进行了全面分析，揭示了潜在的问题在于不同传感器的错位。此外，我们还介绍了AlignMiF，这是一个几何对齐的多模式隐式场，具有两个拟议的模块：几何感知对齐（GAA）和共享几何初始化（SGI）。这些模块有效地调整了不同模态的粗略几何结构，显著增强了激光雷达和相机数据之间的融合过程。通过在各种数据集和场景中进行广泛的实验，我们证明了我们的方法在促进激光雷达和相机模态之间在统一的神经场中更好地交互方面的有效性。具体而言，我们提出的AlignMiF比最近的隐式融合方法（KITTI-360和Waymo数据集上的图像PSNR分别为+2.01和+3.11）实现了显著的改进，并始终超过单模态性能（在各自的数据集上，激光雷达切角距离分别减少了13.8%和14.2%）。 et.al.|[2402.17483](http://arxiv.org/abs/2402.17483)|**[link](https://github.com/tangtaogo/alignmif)**|
|**2024-02-26**|**GEM3D: GEnerative Medial Abstractions for 3D Shape Synthesis**|我们介绍了GEM3D——一种新的深度、拓扑感知的三维形状生成模型。我们的方法的关键成分是基于神经骨架的表示，对形状拓扑和几何信息进行编码。通过去噪扩散概率模型，我们的方法首先根据中轴变换（MAT）生成基于骨架的表示，然后通过骨架驱动的神经隐式公式生成曲面。神经隐式考虑了存储在生成的骨架表示中的拓扑和几何信息，以产生与以前的神经场公式相比在拓扑和几何上更准确的曲面。我们讨论了我们的方法在形状合成和点云重建任务中的应用，并对我们的方法进行了定性和定量评估。与最先进的技术相比，我们展示了更忠实的表面重建和多样化的形状生成结果，还涉及从Thingi10K和ShapeNet重建和合成结构复杂的高属形表面的挑战性场景。 et.al.|[2402.16994](http://arxiv.org/abs/2402.16994)|null|
|**2024-02-21**|**Geometry-Informed Neural Networks**|我们引入了几何知情神经网络（GINN）的概念，它包括（i）在几何约束下的学习，（ii）作为适当表示的神经场，以及（iii）为几何任务中经常遇到的不确定系统生成不同的解决方案。值得注意的是，GINN公式不需要训练数据，因此可以被视为纯粹由约束驱动的生成建模。我们添加了一个明确的多样性损失来缓解模式崩溃。我们考虑了几个约束，特别是分量的连通性，我们通过Morse理论将其转化为可微损失。在实验上，我们展示了GINN学习范式在一系列二维和三维场景中的有效性，这些场景的复杂性不断增加。 et.al.|[2402.14009](http://arxiv.org/abs/2402.14009)|null|

<p align=right>(<a href=#updated-on-20240307>back to top</a>)</p>

[contributors-shield]: https://img.shields.io/github/contributors/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[contributors-url]: https://github.com/Vincentqyw/cv-arxiv-daily/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[forks-url]: https://github.com/Vincentqyw/cv-arxiv-daily/network/members
[stars-shield]: https://img.shields.io/github/stars/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[stars-url]: https://github.com/Vincentqyw/cv-arxiv-daily/stargazers
[issues-shield]: https://img.shields.io/github/issues/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[issues-url]: https://github.com/Vincentqyw/cv-arxiv-daily/issues

