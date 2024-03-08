[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]

## Updated on 2024.03.08
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
|**2024-03-07**|**Finding Waldo: Towards Efficient Exploration of NeRF Scene Space**|近年来，神经辐射场（NeRF）以其卓越的性能迅速成为三维重建和新视图合成的主要方法。尽管人们对NeRF方法非常感兴趣，但NeRF的一个实际用例在很大程度上被忽视了；由NeRF建模的场景空间的探索。在本文中，我们在文献中首次提出并正式定义场景探索框架为NeRF模型输入（即坐标和视角）的有效发现，使用该框架可以呈现符合用户选择标准的新颖视图，我们首先提出了两种基线方法，称为引导随机搜索（GRS）和基于姿态插值的搜索（PIBS）。然后，我们将场景探索视为一个优化问题，并提出了标准不可知的进化引导姿势搜索（EGPS）来进行有效的探索。我们用各种标准（例如显著性最大化、图像质量最大化、照片构图质量改进）测试了所有三种方法，并表明我们的EGPS比其他基线表现得更好。最后，我们强调了场景探索的重点和局限性，并概述了未来研究的方向。 et.al.|[2403.04508](http://arxiv.org/abs/2403.04508)|null|
|**2024-03-07**|**Radiative Gaussian Splatting for Efficient X-ray Novel View Synthesis**|X射线由于其比自然光更强的穿透性而被广泛应用于透射成像。在绘制新视图X射线投影时，现有的主要基于NeRF的方法训练时间长，推理速度慢。在本文中，我们提出了一种基于三维高斯散射的框架，即X-Gaussian，用于X射线新视图合成。首先，受X射线成像各向同性的启发，我们重新设计了一个辐射高斯点云模型。我们的模型在学习预测3D点的辐射强度时排除了视角方向的影响。基于该模型，我们开发了一种具有CUDA实现的可微分辐射光栅化（DRR）。其次，我们定制了一种角度姿态长方体均匀初始化（ACUI）策略，该策略直接使用X射线扫描仪的参数来计算相机信息，然后对包围扫描对象的长方体内的点位置进行均匀采样。实验表明，我们的X-Gaussian比最先进的方法高6.5 dB，同时享受不到15%的训练时间和超过73倍的推理速度。在稀疏视图CT重建中的应用也揭示了该方法的实用价值。代码和模型将在https://github.com/caiyuanhao1998/X-Gaussian . 培训过程可视化的视频演示位于https://www.youtube.com/watch?v=gDVf_Ngeghg . et.al.|[2403.04116](http://arxiv.org/abs/2403.04116)|**[link](https://github.com/caiyuanhao1998/x-gaussian)**|
|**2024-03-06**|**DART: Implicit Doppler Tomography for Radar Novel View Synthesis**|仿真对于射频系统设计者来说是一个非常宝贵的工具，它可以实现成像、目标检测、分类和跟踪的各种算法的快速原型设计。然而，模拟真实的雷达扫描是一项具有挑战性的任务，需要场景的准确模型、射频材料特性和相应的雷达合成功能。我们没有明确指定这些模型，而是提出了DART-多普勒辅助雷达层析成像，这是一种受神经辐射场启发的方法，它使用特定于雷达的物理来创建基于反射率和透射率的距离多普勒图像渲染管道。然后，我们通过构建一个定制的数据收集平台，收集一个新的雷达数据集，以及基于激光雷达的定位的准确位置和瞬时速度测量，来评估DART。与最先进的基线相比，DART从所有数据集的新视图合成了优越的雷达距离多普勒图像，此外还可用于生成高质量的断层图像。 et.al.|[2403.03896](http://arxiv.org/abs/2403.03896)|null|
|**2024-03-04**|**DaReNeRF: Direction-aware Representation for Dynamic Scenes**|为了应对建模和重新渲染动态场景的复杂挑战，最近的方法试图使用基于平面的显式表示来简化这些复杂性，克服了与神经辐射场（NeRF）和隐式表示等方法相关的训练时间慢的问题。然而，将4D动态场景直接分解为多个基于2D平面的表示被证明不足以重新渲染具有复杂运动的高保真场景。作为回应，我们提出了一种新的方向感知表示（DaRe）方法，该方法从六个不同的方向捕捉场景动力学。该学习的表示经过逆对偶树复小波变换（DTCWT）以恢复基于平面的信息。DaReNeRF通过融合来自这些恢复平面的向量来计算每个时空点的特征。将DaReNeRF与用于颜色回归的微小MLP相结合，并在训练中利用体积渲染，可以在复杂动态场景的新型视图合成中获得最先进的性能。值得注意的是，为了解决六个实数和六个虚数方向感知小波系数引入的冗余问题，我们引入了一种可训练的掩蔽方法，在不显著降低性能的情况下缓解了存储问题。此外，与现有技术相比，DaReNeRF保持了2倍的训练时间减少，同时提供了卓越的性能。 et.al.|[2403.02265](http://arxiv.org/abs/2403.02265)|null|
|**2024-03-04**|**Depth-Guided Robust and Fast Point Cloud Fusion NeRF for Sparse Input Views**|具有稀疏输入视图的新型视图合成对于AR/VR和自动驾驶等现实世界应用非常重要。最近的方法已经将深度信息集成到用于稀疏输入合成的NeRF中，利用深度先验进行几何和空间理解。然而，大多数现有的作品往往忽略了深度图中的不准确之处，并且时间效率较低。为了解决这些问题，我们提出了一种用于稀疏输入的深度引导鲁棒快速点云融合NeRF。我们将辐射场视为特征的显式体素网格。为每个输入视图构建一个点云，使用矩阵和向量在体素网格内进行特征化。我们累积每个输入视图的点云，以构建整个场景的融合点云。每个体素通过参考整个场景的点云来确定其密度和外观。通过点云融合和体素网格微调，深度值的不精确性可以被其他视图的不精确值细化或替换。此外，我们的方法可以通过有效的向量矩阵分解来实现更快的重建和更大的紧凑性。实验结果强调，与最先进的基线相比，我们的方法具有卓越的性能和时间效率。 et.al.|[2403.02063](http://arxiv.org/abs/2403.02063)|null|
|**2024-03-04**|**DD-VNB: A Depth-based Dual-Loop Framework for Real-time Visually Navigated Bronchoscopy**|支气管镜的实时6自由度定位对于提高干预质量至关重要。然而，当前基于视觉的技术难以在对看不见的数据的泛化和计算速度之间取得平衡。在这项研究中，我们提出了一种用于实时视觉导航支气管镜检查（DD-VNB）的基于深度的双环框架，该框架可以在不需要重新训练的情况下推广到患者病例中。DD-VNB框架集成了两个关键模块：深度估计和双环定位。为了解决患者之间的领域差距，我们提出了一种知识嵌入的深度估计网络，该网络将内窥镜帧映射到深度，通过消除患者特定的纹理来确保泛化。该网络将视图合成知识嵌入到循环对抗性架构中，用于尺度约束的单目深度估计。为了获得实时性能，我们的定位模块将快速自我运动估计网络嵌入深度配准循环中。自我运动推断网络以高频估计支气管镜的姿态变化，而相对于术前3D模型的深度配准周期性地提供绝对姿态。具体而言，将相对姿态变化作为初始猜测输入到配准过程中，以提高其准确性和速度。对来自患者的体模和体内数据的实验证明了我们框架的有效性：1）单目深度估计优于SOTA，2）定位在体模中实现了4.7 $\pm$3.17 mm的绝对跟踪误差（ATE）精度，在患者数据中实现了6.49$\pm$ 3.88 mm的绝对追踪误差，3）帧速率接近视频捕获速度，4）而不需要按情况进行网络再训练。该框架优越的速度和准确性证明了其在实时支气管镜导航方面的临床潜力。 et.al.|[2403.01683](http://arxiv.org/abs/2403.01683)|null|
|**2024-03-02**|**NeRF-VPT: Learning Novel View Representations with Neural Radiance Fields via View Prompt Tuning**|神经辐射场（NeRF）在新视图合成中取得了显著的成功。尽管如此，为新颖的视图生成高质量图像的任务仍然是一个关键的挑战。虽然现有的努力取得了值得称赞的进展，但捕捉复杂的细节、增强纹理和实现卓越的峰值信噪比（PSNR）指标值得进一步关注和进步。在这项工作中，我们提出了NeRF VPT，这是一种用于新视图合成的创新方法，以应对这些挑战。我们提出的NeRF VPT采用级联视图提示调整范式，其中从先前渲染结果中获得的RGB信息作为后续渲染阶段的指导性视觉提示，期望嵌入提示中的先验知识可以促进渲染图像质量的逐步增强。NeRF VPT只需要在每个训练阶段从前一阶段渲染中采样RGB数据作为先验，而不需要依赖额外的指导或复杂的技术。因此，我们的NeRF VPT是即插即用的，可以很容易地集成到现有的方法中。通过在要求苛刻的真实场景基准上对我们的NeRF VPT与几种基于NeRF的方法进行比较分析，如真实合成360、真实前向、副本数据集和用户捕获的数据集，我们证实，与所有最先进的方法相比，我们的NeRF VPT显著提高了基线性能，并能熟练地生成更高质量的新视图图像。此外，NeRF VPT的级联学习引入了对具有稀疏输入的场景的适应性，从而显著提高了稀疏视图新视图合成的准确性。源代码和数据集位于\url{https://github.com/Freedomcls/NeRF-VPT}. et.al.|[2403.01325](http://arxiv.org/abs/2403.01325)|**[link](https://github.com/freedomcls/nerf-vpt)**|
|**2024-03-02**|**Neural Field Classifiers via Target Encoding and Classification Loss**|神经场方法在计算机视觉和计算机图形学中的各种长期任务中取得了巨大进展，包括新颖的视图合成和几何重建。由于现有的神经场方法试图预测一些基于坐标的连续目标值，例如神经辐射场（NeRF）的RGB，所有这些方法都是回归模型，并通过一些回归损失进行优化。然而，对于神经场方法来说，回归模型真的比分类模型更好吗？在这项工作中，我们试图从机器学习的角度来探讨神经领域这个非常基本但被忽视的问题。我们成功地提出了一种新的神经场分类器（NFC）框架，该框架将现有的神经场方法公式化为分类任务，而不是回归任务。所提出的NFC可以通过使用新的目标编码模块和优化分类损失，轻松地将任意神经场回归器（NFR）转换为其分类变体。通过将连续回归目标编码为高维离散编码，我们自然地形成了多标签分类任务。大量的实验证明了NFC在几乎免费的额外计算成本下令人印象深刻的有效性。此外，NFC还显示出对稀疏输入、损坏图像和动态场景的鲁棒性。 et.al.|[2403.01058](http://arxiv.org/abs/2403.01058)|null|
|**2024-02-29**|**ViewFusion: Towards Multi-View Consistency via Interpolated Denoising**|通过扩散模型进行的新型视图合成在生成多样化和高质量图像方面表现出了显著的潜力。然而，在这些主流方法中，图像生成的独立过程导致了在保持多视图一致性方面的挑战。为了解决这一问题，我们引入了ViewFusion，这是一种新颖的无训练算法，可以无缝集成到现有的预训练扩散模型中。我们的方法采用了一种自回归方法，该方法隐式地利用先前生成的视图作为下一个视图生成的上下文，确保了在新视图生成过程中强大的多视图一致性。通过通过插值去噪融合已知视图信息的扩散过程，我们的框架成功地扩展了单视图条件模型，使其在多视图条件设置下工作，而无需任何额外的微调。大量的实验结果证明了ViewFusion在生成一致且详细的新视图方面的有效性。 et.al.|[2402.18842](http://arxiv.org/abs/2402.18842)|**[link](https://github.com/Wi-sc/ViewFusion)**|
|**2024-02-28**|**PolyOculus: Simultaneous Multi-view Image-based Novel View Synthesis**|本文考虑了生成新视图合成（GNVS）的问题，即在给定有限数量的已知视图的情况下生成场景的新颖、合理的视图。在这里，我们提出了一个基于集合的生成模型，该模型可以同时生成多个自洽的新视图，条件是任何数量的已知视图。我们的方法不限于一次生成单个图像，并且可以以零、一个或多个视图为条件。因此，当生成大量视图时，我们的方法不限于低阶自回归生成方法，并且能够更好地在大图像集上保持生成的图像质量。我们在标准NVS数据集上评估了所提出的模型，并表明它优于最先进的基于图像的GNVS基线。此外，我们表明，该模型能够生成没有自然顺序的相机视图集，如循环和双目轨迹，并且在此类任务上显著优于其他方法。 et.al.|[2402.17986](http://arxiv.org/abs/2402.17986)|null|

<p align=right>(<a href=#updated-on-20240308>back to top</a>)</p>

## 3D Reconstruction

|Publish Date|Title|Abstract|PDF|Code|
|---|---|---|---|---|
|**2024-03-07**|**Efficient LoFTR: Semi-Dense Local Feature Matching with Sparse-Like Speed**|我们提出了一种新的方法来有效地产生图像之间的半密集匹配。先前的无检测器匹配器LoFTR在处理大的视点变化和纹理较差的场景时显示出显著的匹配能力，但效率较低。我们重新审视了它的设计选择，并在效率和准确性方面进行了多项改进。一个关键的观察结果是，由于共享的局部信息，在整个特征图上执行转换是冗余的，因此我们提出了一种具有自适应令牌选择的聚合注意力机制，以提高效率。此外，我们发现LoFTR的精细相关模块存在空间方差，这不利于匹配精度。提出了一种新的两级相关层，以实现精确的亚像素对应，从而提高精度。我们的效率优化模型比LoFTR快$\sim 2.5\倍，甚至可以超过最先进的高效稀疏匹配管道SuperPoint+LightGlue。此外，大量的实验表明，与竞争性的半密集匹配器相比，我们的方法可以实现更高的精度，并具有可观的效率效益。这为大规模或延迟敏感的应用（如图像检索和3D重建）开辟了令人兴奋的前景。项目页面：https://zju3dv.github.io/efficientloftr. et.al.|[2403.04765](http://arxiv.org/abs/2403.04765)|null|
|**2024-03-07**|**Finding Waldo: Towards Efficient Exploration of NeRF Scene Space**|近年来，神经辐射场（NeRF）以其卓越的性能迅速成为三维重建和新视图合成的主要方法。尽管人们对NeRF方法非常感兴趣，但NeRF的一个实际用例在很大程度上被忽视了；由NeRF建模的场景空间的探索。在本文中，我们在文献中首次提出并正式定义场景探索框架为NeRF模型输入（即坐标和视角）的有效发现，使用该框架可以呈现符合用户选择标准的新颖视图，我们首先提出了两种基线方法，称为引导随机搜索（GRS）和基于姿态插值的搜索（PIBS）。然后，我们将场景探索视为一个优化问题，并提出了标准不可知的进化引导姿势搜索（EGPS）来进行有效的探索。我们用各种标准（例如显著性最大化、图像质量最大化、照片构图质量改进）测试了所有三种方法，并表明我们的EGPS比其他基线表现得更好。最后，我们强调了场景探索的重点和局限性，并概述了未来研究的方向。 et.al.|[2403.04508](http://arxiv.org/abs/2403.04508)|null|
|**2024-03-07**|**CN-RMA: Combined Network with Ray Marching Aggregation for 3D Indoors Object Detection from Multi-view Images**|本文介绍了一种从多视角图像中检测三维室内物体的新方法CN-RMA。我们观察到关键挑战是图像和3D对应关系的模糊性，而没有明确的几何结构来提供遮挡信息。为了解决这个问题，CN-RMA利用了3D重建网络和3D对象检测网络的协同作用，其中重建网络提供了粗略的截断有符号距离函数（TSDF），并引导图像特征以端到端的方式正确地投票到3D空间。具体来说，我们通过射线行进将权重与每条射线的采样点相关联，表示图像中像素对相应3D位置的贡献。这样的权重由预测的带符号距离确定，使得图像特征仅投票给重建表面附近的区域。我们的方法在从多视图图像中检测3D对象方面实现了最先进的性能，通过mAP@0.25和mAP@0.5在ScanNet和ARKitScenes数据集上。代码和型号发布于https://github.com/SerCharles/CN-RMA. et.al.|[2403.04198](http://arxiv.org/abs/2403.04198)|null|
|**2024-03-07**|**Radiative Gaussian Splatting for Efficient X-ray Novel View Synthesis**|X射线由于其比自然光更强的穿透性而被广泛应用于透射成像。在绘制新视图X射线投影时，现有的主要基于NeRF的方法训练时间长，推理速度慢。在本文中，我们提出了一种基于三维高斯散射的框架，即X-Gaussian，用于X射线新视图合成。首先，受X射线成像各向同性的启发，我们重新设计了一个辐射高斯点云模型。我们的模型在学习预测3D点的辐射强度时排除了视角方向的影响。基于该模型，我们开发了一种具有CUDA实现的可微分辐射光栅化（DRR）。其次，我们定制了一种角度姿态长方体均匀初始化（ACUI）策略，该策略直接使用X射线扫描仪的参数来计算相机信息，然后对包围扫描对象的长方体内的点位置进行均匀采样。实验表明，我们的X-Gaussian比最先进的方法高6.5 dB，同时享受不到15%的训练时间和超过73倍的推理速度。在稀疏视图CT重建中的应用也揭示了该方法的实用价值。代码和模型将在https://github.com/caiyuanhao1998/X-Gaussian . 培训过程可视化的视频演示位于https://www.youtube.com/watch?v=gDVf_Ngeghg . et.al.|[2403.04116](http://arxiv.org/abs/2403.04116)|**[link](https://github.com/caiyuanhao1998/x-gaussian)**|
|**2024-03-05**|**Pooling Image Datasets With Multiple Covariate Shift and Imbalance**|小样本量在许多学科中很常见，这就需要在多个机构中汇集大致相似的数据集，以研究图像和疾病结果之间微弱但相关的关联。这种数据通常表现出协变量（即二次非成像数据）的偏移/不平衡。控制这种干扰变量在标准统计分析中很常见，但这些想法并不直接适用于参数过大的模型。因此，最近的工作表明，来自不变表示学习的策略是如何提供一个有意义的起点的，但目前的方法仅限于一次只考虑几个协变量的变化/不平衡。在本文中，我们展示了如何从范畴理论的角度看待这个问题，提供了一个简单有效的解决方案，完全避免了原本需要的复杂的多阶段训练管道。我们通过在真实数据集上进行的大量实验证明了这种方法的有效性。此外，我们讨论了这种形式的公式如何为至少5个以上不同的问题设置提供统一的视角，从自监督学习到3D重建中的匹配问题。 et.al.|[2403.02598](http://arxiv.org/abs/2403.02598)|null|
|**2024-03-04**|**DragTex: Generative Point-Based Texture Editing on 3D Mesh**|最近，使用生成人工智能创建3D纹理网格引起了人们的极大关注。虽然现有方法支持在3D网格上基于文本的生成纹理生成或编辑，但它们往往难以通过更直观的交互来精确控制纹理图像的像素。虽然2D图像可以使用拖动交互进行生成编辑，但将这种类型的方法直接应用于3D网格纹理仍然会导致多个视图之间缺乏局部一致性、错误累积和训练时间长等问题。为了解决这些挑战，我们提出了一种基于生成点的3D网格纹理编辑方法，称为DragTex。该方法利用扩散模型在不同视图之间混合变形轮廓附近区域中的局部不一致纹理，从而实现局部一致的纹理编辑。此外，我们对解码器进行微调，以减少非拖动区域的重建误差，从而减少总体误差积累。此外，我们使用多视图图像来训练LoRA，而不是单独训练每个视图，这显著缩短了训练时间。实验结果表明，我们的方法有效地实现了3D网格上的拖动纹理，并生成了符合拖动交互所需意图的合理纹理。 et.al.|[2403.02217](http://arxiv.org/abs/2403.02217)|null|
|**2024-03-04**|**TripoSR: Fast 3D Object Reconstruction from a Single Image**|本技术报告介绍了TripoSR，这是一种利用变压器架构进行快速前馈3D生成的3D重建模型，可在0.5秒内从单个图像生成3D网格。基于LRM网络架构，TripoSR集成了数据处理、模型设计和训练技术方面的实质性改进。对公共数据集的评估表明，与其他开源替代品相比，TripoSR在数量和质量上都表现出优异的性能。TripoSR是根据麻省理工学院的许可发布的，旨在为研究人员、开发人员和创意人员提供3D生成人工智能的最新进展。 et.al.|[2403.02151](http://arxiv.org/abs/2403.02151)|**[link](https://github.com/vast-ai-research/triposr)**|
|**2024-03-03**|**A Novel Dynamic Light-Section 3D Reconstruction Method for Wide-Range Sensing**|现有的基于检流计的激光扫描系统在多尺度3D重建中的应用具有挑战性，因为难以在高重建精度和宽重建范围之间实现平衡。本文提出了一种新的方法，通过使用多电流计切换相机的视场来同步激光扫描。除了先进的硬件设置外，我们还通过建模动态相机、动态激光器及其组合交互，建立了系统的综合数学模型。然后，我们通过构建误差模型并最小化目标函数，提出了一种高精度、灵活的校准方法。最后，我们通过扫描标准组件来评估所提出的系统的性能。评估结果表明，当测量范围扩展到1100 mm $\times$1300 mm$\imes$ 650 mm时，所提出的三维重建系统的精度达到0.3 mm。在相同的重建精度下，重建范围扩展了25倍，表明所提出的方法同时允许在工业应用中进行高精度和宽范围的3D重建。 et.al.|[2403.01374](http://arxiv.org/abs/2403.01374)|null|
|**2024-03-01**|**G3DR: Generative 3D Reconstruction in ImageNet**|我们介绍了一种新的3D生成方法，即ImageNet中的生成3D重建（G3DR），该方法能够从单个图像中生成各种高质量的3D对象，解决了现有方法的局限性。我们框架的核心是一种新颖的深度正则化技术，它能够生成具有高几何保真度的场景。G3DR还利用预训练的语言视觉模型，如CLIP，实现新视图中的重建，并提高几代人的视觉逼真度。此外，G3DR设计了一种简单但有效的采样程序，以进一步提高世代的质量。G3DR提供基于类或文本条件的多样化且高效的3D资产生成。尽管G3DR很简单，但它能够击败最先进的方法，在感知指标和几何得分方面比它们提高了22%和90%，而只需要一半的训练时间。代码位于https://github.com/preddy5/G3DR et.al.|[2403.00939](http://arxiv.org/abs/2403.00939)|null|
|**2024-03-01**|**DISORF: A Distributed Online NeRF Training and Rendering Framework for Mobile Robots**|我们提出了一个框架DISORF，用于对资源受限的移动机器人和边缘设备捕获的场景进行在线3D重建和可视化。为了解决边缘设备的有限计算能力和潜在的有限网络可用性，我们设计了一个在边缘设备和远程服务器之间有效分配计算的框架。我们利用设备上的SLAM系统生成姿势关键帧，并将其传输到远程服务器，远程服务器可以通过利用NeRF模型在运行时执行高质量的3D重建和可视化。我们发现了在线NeRF训练的一个关键挑战，在该挑战中，天真的图像采样策略可能导致渲染质量的显著下降。我们提出了一种新的移位指数帧采样方法，以解决在线NeRF训练的这一挑战。我们展示了我们的框架在实现未知场景的高质量实时重建和可视化方面的有效性，因为这些场景是从移动机器人和边缘设备中的相机捕获和流式传输的。 et.al.|[2403.00228](http://arxiv.org/abs/2403.00228)|null|

<p align=right>(<a href=#updated-on-20240308>back to top</a>)</p>

## Diffusion

|Publish Date|Title|Abstract|PDF|Code|
|---|---|---|---|---|
|**2024-03-07**|**Effects of mechanical stress, chemical potential, and coverage on hydrogen solubility during hydrogen enhanced decohesion of ferritic steel grain boundaries: A first-principles study**|氢增强脱粘（HEDE）是氢脆的许多机制之一，氢脆现象严重影响铁和铁合金等结构材料。晶界（GBs）在这一机制中发挥着关键作用，它们可以提供捕获位点或充当氢扩散途径。H与晶界和其他晶体缺陷的相互作用，以及H在微观结构中的溶解度和分布，取决于浓度、化学势和局部应力。因此，对于HEDE的定量评估，需要将广义溶液能量与内聚强度结合起来，作为氢覆盖率的函数。在这项工作中，我们进行了密度泛函理论计算，以研究H对bcc-Fe中 $\Sigma$5（310）[001]和$\Sigma$3（112）[1$\bar｛1｝$0]对称倾斜GBs的去粘的影响，作为开和闭填充GB结构的例子。提出了一种在GB平面上识别偏析位点的方法。结果表明，在较高的局部浓度下，H导致GB平面的内聚强度显著降低，在$\Sigma$5处比在$\Signa$3GB处明显更明显。有趣的是，与零应力的情况相比，在有限应力下，$\Sigma$3GB对H解更有利，其中$\Sigma$ 5GB更具吸引力。这表明，在某些条件下，微观结构中的应力会导致H重新分布到更强的晶界，这为设计抗H微观结构开辟了一条新的途径。为了总结我们的研究，我们研究了铁素体钢中典型合金元素C、V、Cr和Mn对H溶解度和GBs强度的影响。 et.al.|[2403.04741](http://arxiv.org/abs/2403.04741)|null|
|**2024-03-07**|**Quantum-enhanced joint estimation of phase and phase diffusion**|在存在未知相位扩散噪声的情况下进行精确的相位估计是噪声量子计量学中一项关键但具有挑战性的任务。由于相关噪声的有害影响，这个问题特别令人感兴趣。在这里，我们使用以实验可及性著称的广义Holland-Burnett态来研究相位和相位扩散的联合估计。即使在存在光子损耗的情况下，这些状态也能在单参数相位估计中提供接近最佳状态的性能。我们采用双重方法，通过分析通过双零差测量的联合信息提取和所有探测状态的联合信息可用性。通过我们的分析，我们发现通过使用将所有输入光子引导到平衡分束器的一个端口中所产生的状态，可以获得最高的灵敏度。此外，我们推断，即使在存在中等光子损失的情况下，良好的灵敏度水平也会持续存在，这说明了我们的探针状态在有损条件下的显著弹性。 et.al.|[2403.04722](http://arxiv.org/abs/2403.04722)|null|
|**2024-03-07**|**ObjectCompose: Evaluating Resilience of Vision-Based Models on Object-to-Background Compositional Changes**|考虑到最近基于视觉的模型的大规模多模式训练及其泛化能力，了解其鲁棒性的程度对其在现实世界中的部署至关重要。在这项工作中，我们评估了当前基于视觉的模型对不同对象到背景上下文变化的弹性。大多数稳健性评估方法都引入了合成数据集来诱导对象特征（视点、尺度、颜色）的变化，或者在真实图像上使用图像转换技术（对抗性变化、常见损坏）来模拟分布的变化。最近的工作探索了利用大型语言模型和扩散模型来产生背景变化。然而，这些方法要么缺乏对要进行的更改的控制，要么扭曲了对象语义，使其不适合任务。另一方面，我们的方法可以诱导不同的对象到背景的变化，同时保留对象的原始语义和外观。为了实现这一目标，我们利用文本到图像、图像到文本和图像到分割模型的生成能力，自动生成广泛的对象到背景的变化。我们通过修改文本提示或优化文本到图像模型的延迟和文本嵌入来诱导自然和对抗性背景变化。这使我们能够量化背景上下文在理解深度神经网络的鲁棒性和泛化方面的作用。我们制作了各种版本的标准视觉数据集（ImageNet，COCO），将各种逼真的背景融入图像中，或在背景中引入颜色、纹理和对抗性变化。我们进行了广泛的实验，以分析基于视觉的模型在不同任务中对对象到背景上下文变化的鲁棒性。 et.al.|[2403.04701](http://arxiv.org/abs/2403.04701)|null|
|**2024-03-07**|**Delving into the Trajectory Long-tail Distribution for Muti-object Tracking**|多目标跟踪（MOT）是计算机视觉中的一个关键领域，具有广泛的实际实现。目前的研究主要集中在跟踪算法的发展和后处理技术的增强上。然而，对追踪数据本身的性质缺乏彻底的检查。在这项研究中，我们率先探索了跟踪数据的分布模式，并在现有的MOT数据集中发现了一个明显的长尾分布问题。我们注意到不同行人的轨迹长度分布存在显著的不平衡，我们将这种现象称为“行人轨迹长尾分布”。为了应对这一挑战，我们推出了一种定制策略，旨在减轻这种扭曲分布的影响。具体来说，我们提出了两种数据增强策略，包括针对视点状态设计的静态相机视图数据增强（SVA）和动态相机视图数据扩展（DVA），以及Re-ID的Group Softmax（GS）模块。SVA是回溯和预测尾部类的行人轨迹，DVA是使用扩散模型来改变场景的背景。GS将行人划分为不相关的组，并分别对每组执行softmax操作。我们提出的策略可以集成到许多现有的跟踪系统中，大量的实验验证了我们的方法在减少长尾分布对多目标跟踪性能的影响方面的有效性。代码位于https://github.com/chen-si-jia/Trajectory-Long-tail-Distribution-for-MOT. et.al.|[2403.04700](http://arxiv.org/abs/2403.04700)|**[link](https://github.com/chen-si-jia/Trajectory-Long-tail-Distribution-for-MOT)**|
|**2024-03-07**|**PixArt-Σ: Weak-to-Strong Training of Diffusion Transformer for 4K Text-to-Image Generation**|在本文中，我们介绍了PixArt-\Sigma，一种能够直接生成4K分辨率图像的扩散转换器模型~（DiT）。PixArt-\Sigma比其前身PixArt-\\alpha有了显著的进步，提供了明显更高保真度的图像，并改进了与文本提示的对齐。PixArt-\Sigma的一个关键特征是其训练效率。利用PixArt-\alpha的基础预训练，它通过结合更高质量的数据，从“较弱”的基线演变为“更强”的模型，我们称之为“弱到强训练”。PixArt-\Sigma的进步有两个方面：（1）高质量训练数据：PixArt-\\Sigma融合了高质量的图像数据，并配有更精确、更详细的图像字幕。（2） 高效的令牌压缩：我们在DiT框架内提出了一种新的注意力模块，它可以压缩密钥和值，显著提高效率并促进超高分辨率图像的生成。得益于这些改进，PixArt-\Sigma实现了卓越的图像质量和用户提示遵守能力，其模型大小（0.6B参数）明显小于现有的文本到图像扩散模型，如SDXL（2.6B参数）和SD Cascade（5.1B参数）。此外，PixArt-\Sigma生成4K图像的能力支持高分辨率海报和壁纸的创建，有效地支持电影和游戏等行业高质量视觉内容的生产。 et.al.|[2403.04692](http://arxiv.org/abs/2403.04692)|null|
|**2024-03-07**|**Pix2Gif: Motion-Guided Diffusion for GIF Generation**|我们提出了Pix2Gif，一个用于图像到GIF（视频）生成的运动引导扩散模型。我们通过将任务公式化为由文本和运动幅度提示引导的图像翻译问题来不同地解决这个问题，如预告图所示。为了确保模型遵循运动引导，我们提出了一个新的运动引导扭曲模块，以在空间上变换基于两种类型提示的源图像的特征。此外，我们引入了感知损失，以确保变换后的特征图与目标图像保持在同一空间内，从而确保内容的一致性和连贯性。在模型训练的准备过程中，我们通过从TGIF视频字幕数据集中提取相干图像帧来精心策划数据，该数据集提供了关于受试者时间变化的丰富信息。在预训练之后，我们以零样本的方式将我们的模型应用于许多视频数据集。大量的定性和定量实验证明了我们模型的有效性——它不仅捕捉到了文本中的语义提示，还捕捉到了运动引导中的空间提示。我们使用16xV100 GPU的单个节点来训练所有模型。代码、数据集和模型公开于：https://hiteshk03.github.io/Pix2Gif/. et.al.|[2403.04634](http://arxiv.org/abs/2403.04634)|null|
|**2024-03-07**|**A Domain Translation Framework with an Adversarial Denoising Diffusion Model to Generate Synthetic Datasets of Echocardiography Images**|目前，医学图像领域的翻译操作对研究人员和临床医生提出了很高的要求。除其他功能外，该任务允许生成具有足够高图像质量的新医学图像，使其具有临床相关性。深度学习（DL）架构，特别是深度生成模型，被广泛用于生成图像并将其从一个领域转换到另一个领域。所提出的框架依赖于对抗性去噪扩散模型（DDM）来合成超声心动图图像并执行域转换。与生成对抗性网络（GANs）相反，DDM能够生成具有大多样性的高质量图像样本。如果DDM与GAN相结合，则生成新数据的能力将以更快的采样时间完成。在这项工作中，我们训练了一个与GAN相结合的对抗性DDM，以学习反向去噪过程，依赖于引导图像，确保每个超声心动图图像的相关解剖结构在生成的图像样本上得到保留和表示。对于几种域转换操作，结果验证了这种生成模型能够合成高质量的图像样本：MSE:11.50+/-3.69，PSNR（dB）:30.48+/-0.09，SSIM:0.47+/-0.03。所提出的方法显示出很高的泛化能力，引入了一个框架来创建适合用于临床研究目的的超声心动图图像。 et.al.|[2403.04612](http://arxiv.org/abs/2403.04612)|null|
|**2024-03-07**|**Dynamic critical behavior of the chiral phase transition from the real-time functional renormalization group**|在手性极限条件下，二味QCD二阶手性相变周围复杂的多体动力学可以通过呼吁普遍性来理解。我们提出了实时函数重整化群的一个新公式，该公式描述了同一动力学普适性类中系统的随机流体动力学运动方程，该类对应于Halperin-Hohenberg分类中的模型G。我们的方法保留了具有可逆模式耦合的此类系统的所有相关对称性。我们表明，计算确实产生了动态临界指数的非平凡值 $z=d/2$，其中$d$ 是空间维度的数量。从守恒电荷密度扩散系数对动量和温度的依赖性，我们提取了无量纲的通用标度函数。 et.al.|[2403.04573](http://arxiv.org/abs/2403.04573)|null|
|**2024-03-07**|**Rescaled Mode-Coupling Scheme for the Quantitative Description of Experimentally Observed Colloid Dynamics**|我们使用改进的模式耦合理论（MCT）描述了在模型硬球颗粒的胶体悬浮液中实验观察到的集体动力学。这种重新缩放的MCT能够定量描述这些系统中的波矢量和随时间变化的扩散。通过静态和动态光散射实验确定了类液体结构分散体的中间散射函数。系统的结构和短时动力学可以通过对部分结构因子使用多组分Percus Yevick模拟来定量描述，并基于半解析 $\delta\gamma$ -展开对流体动力学相互作用进行有效的单组分描述。结合最近提出的MCT的经验修改，其中使用在重新缩放的数字密度下的有效结构因子来计算记忆函数，该方案能够在整个可访问的时间和波矢量范围内对集体动力学进行建模，并定量预测长时间自扩散系数和零剪切粘度的体积分数依赖性。这突出了MCT作为定量分析和预测实验观测的实用工具的潜力。 et.al.|[2403.04556](http://arxiv.org/abs/2403.04556)|null|
|**2024-03-07**|**Poisson equation with measure data, reconstruction formula and Doob classes of processes**|我们考虑方程的狄利克雷问题，该方程涉及与对称瞬态正则狄利克雷形式和方程右侧有界Borel测度相关的一般算子。我们引入了一个新的函数空间（取决于形式），它允许我们区分具有扩散测度的解和具有一般Borel测度的解。这个新空间可以根据与底层算子相关的泊松核进行分析表征，或者通过使用与算子自然相关的过程的Doob类（D）的概念进行概率表征。我们还证明了一个重建公式，用carrée du champ算子和与底层形式相关的跳跃测度来描述解在集上的行为，其中解非常大。 et.al.|[2403.04543](http://arxiv.org/abs/2403.04543)|null|

<p align=right>(<a href=#updated-on-20240308>back to top</a>)</p>

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

<p align=right>(<a href=#updated-on-20240308>back to top</a>)</p>

[contributors-shield]: https://img.shields.io/github/contributors/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[contributors-url]: https://github.com/Vincentqyw/cv-arxiv-daily/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[forks-url]: https://github.com/Vincentqyw/cv-arxiv-daily/network/members
[stars-shield]: https://img.shields.io/github/stars/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[stars-url]: https://github.com/Vincentqyw/cv-arxiv-daily/stargazers
[issues-shield]: https://img.shields.io/github/issues/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[issues-url]: https://github.com/Vincentqyw/cv-arxiv-daily/issues

