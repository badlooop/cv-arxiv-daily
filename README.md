[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]

## Updated on 2024.06.11
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
|**2024-06-07**|**Multi-style Neural Radiance Field with AdaIN**|在这项工作中，我们提出了一种结合AdaIN和NeRF的新管道，用于风格化的小说视图合成任务。与以前的工作相比，我们做出了以下贡献：1）我们简化了管道。2） 我们扩展了模型的功能来处理多样式任务。3） 我们修改了模型架构，使其在具有强烈笔触的样式上表现良好。4） 我们在多样式模型上实现了样式插值，使我们能够控制任意两个样式之间的样式以及样式化输出和原始场景之间的样式强度，从而更好地控制样式化强度。 et.al.|[2406.04960](http://arxiv.org/abs/2406.04960)|null|
|**2024-06-06**|**Flash3D: Feed-Forward Generalisable 3D Scene Reconstruction from a Single Image**|在本文中，我们提出了Flash3D，这是一种从单个图像进行场景重建和新颖视图合成的方法，它既非常通用又高效。为了通用性，我们从单目深度估计的“基础”模型开始，并将其扩展到全3D形状和外观重建器。为了提高效率，我们将这种扩展建立在前馈高斯散射的基础上。具体来说，我们在预测的深度预测第一层3D高斯，然后添加在空间上偏移的附加高斯层，使模型能够完成遮挡和截断后的重建。Flash3D非常高效，可以在一天内在单个GPU上进行训练，因此大多数研究人员都可以访问。在RealEstate10k上进行训练和测试时，它取得了最先进的成绩。当转移到像纽约大学这样看不见的数据集时，它的表现大大优于竞争对手。更令人印象深刻的是，当转移到KITTI时，Flash3D实现了比专门在该数据集上训练的方法更好的PSNR。在某些情况下，它甚至优于最近使用多个视图作为输入的方法。代码、模型、演示和更多结果可在https://www.robots.ox.ac.uk/~vgg/research/flash3d/。 et.al.|[2406.04343](http://arxiv.org/abs/2406.04343)|null|
|**2024-06-06**|**Coarse-To-Fine Tensor Trains for Compact Visual Representations**|学习视觉数据的紧凑、高质量和易于优化的表示的能力对于许多应用程序（如新颖的视图合成和3D重建）至关重要。最近的工作表明，在使用张量网络来设计这种紧凑和高质量的表示方面取得了实质性的成功。然而，优化基于张量的表示，特别是高度紧凑的张量列表示的能力仍然缺乏。这阻碍了从业者为视觉数据部署张量网络的全部潜力。为此，我们提出了“延长上采样张量序列（PuTT）”，这是一种以从粗到细的方式学习张量序列表示的新方法。我们的方法涉及延长或“上采样”已学习的张量序列表示，创建一个增量细化的“从粗到细”张量序列。我们沿着三个轴来评估我们的表示：（1）。压缩，（2）。去噪能力，以及（3）。图像完成能力。为了评估这些轴，我们考虑了图像拟合、3D拟合和新视图合成的任务，其中与最先进的基于张量的方法相比，我们的方法显示出改进的性能。有关完整结果，请参阅我们的项目网页：https://sebulo.github.io/PuTT_website/ et.al.|[2406.04332](http://arxiv.org/abs/2406.04332)|**[link](https://github.com/sebulo/PuTT)**|
|**2024-06-06**|**Conv-INR: Convolutional Implicit Neural Representation for Multimodal Visual Signals**|内隐神经表征（INR）最近成为一种很有前途的信号表征范式。通常，INR由多人感知器（MLP）参数化，该感知器将坐标作为输入并生成信号的相应属性。然而，基于MLP的INR面临两个关键问题：i）单独考虑每个坐标，而忽略连接；ii）遭受频谱偏移，从而不能学习高频分量。虽然目标视觉信号通常表现出强烈的局部结构和邻域依赖性，并且高频分量在这些信号中很重要，但这些问题损害了INRs的代表能力。本文提出了第一个完全基于卷积的INR模型Conv-INR。由于卷积的固有属性，Conv-INR可以同时考虑相邻坐标并有效地学习高频分量。与现有的基于MLP的INR相比，Conv INR在不需要主要功能扩展的情况下具有更好的代表能力和可训练性。我们在四项任务上进行了广泛的实验，包括图像拟合、CT/MRI重建和新的视图合成，Conv INR都显著超过了现有的基于MLP的INR，验证了其有效性。最后，我们提出了三种重新参数化方法，它们可以在不引入任何额外推理成本的情况下进一步提高vanilla Conv INR的性能。 et.al.|[2406.04249](http://arxiv.org/abs/2406.04249)|null|
|**2024-06-06**|**Encoding Semantic Priors into the Weights of Implicit Neural Representation**|隐式神经表示（INR）最近成为一种很有前途的信号表示范式，它以坐标为输入并生成相应的信号值。由于这些坐标不包含语义特征，INR没有考虑任何语义信息。然而，语义信息已被证明在许多视觉任务中至关重要，尤其是在视觉信号表示方面。本文提出了一种称为SPW的重新参数化方法，该方法将语义先验编码为INR的权重，从而使INR隐含地包含语义信息，提高其表示能力。具体来说，SPW使用语义神经网络（SNN）来提取目标视觉信号的低级和高级语义信息，并生成语义向量，将其输入到权重生成网络（WGN）中以生成INR模型的权重。最后，INR使用生成的具有语义先验的权重将坐标映射到信号值。训练后，我们只保留生成的权重，同时放弃SNN和WGN，因此SPW在推理中不会引入额外的成本。实验结果表明，SPW可以显著提高各种INR模型在各种任务上的性能，包括图像拟合、CT重建、MRI重建和新视图合成。进一步的实验表明，采用SPW的模型具有较低的权值冗余，学习到了更多新颖的表示，验证了SPW的有效性。 et.al.|[2406.04178](http://arxiv.org/abs/2406.04178)|null|
|**2024-06-06**|**Gear-NeRF: Free-Viewpoint Rendering and Tracking with Motion-aware Spatio-Temporal Sampling**|将神经辐射场（NeRF）扩展到动态场景建模，使其能够实现近照片逼真、自由的视点渲染。尽管这些方法在创造沉浸式体验方面显示出了一些潜力，但有两个缺点限制了它们的普遍性：（i）当计算预算有限时，重建质量显著降低，以及（ii）对底层场景缺乏语义理解。为了解决这些问题，我们介绍了Gear NeRF，它利用了来自强大图像分割模型的语义信息。我们的方法提供了一种学习时空（4D）语义嵌入的原则性方法，在此基础上，我们引入了齿轮的概念，以允许基于其运动程度对场景的动态区域进行分层建模。这种区分使我们能够根据每个区域的运动尺度成比例地调整其时空采样分辨率，从而实现更逼真的动态新颖视图合成。同时，我们的方法几乎免费实现了对感兴趣对象的免费视点跟踪，这是现有基于NeRF的方法尚未实现的功能。实证研究验证了我们方法的有效性，我们在多个具有挑战性的数据集上实现了最先进的渲染和跟踪性能。 et.al.|[2406.03723](http://arxiv.org/abs/2406.03723)|null|
|**2024-06-05**|**Dynamic 3D Gaussian Fields for Urban Areas**|我们提出了一种用于大规模动态城市区域的新型视图合成（NVS）的高效神经3D场景表示。现有作品由于其有限的视觉质量和非交互式渲染速度，不太适合混合现实或闭环模拟等应用。最近，基于光栅化的方法已经以令人印象深刻的速度实现了高质量的NVS。然而，这些方法仅限于小规模、同质的数据，即它们不能处理由于天气、季节和照明而引起的严重外观和几何变化，也不能扩展到具有数千张图像的更大的动态区域。我们提出了4DGF，这是一种神经场景表示，可扩展到大规模动态城市区域，处理异构输入数据，并显著提高渲染速度。我们使用3D高斯作为有效的几何支架，同时依赖神经场作为紧凑灵活的外观模型。我们在全局范围内通过场景图集成场景动力学，同时通过变形在局部范围内建模关节运动。这种分解方法实现了适用于真实世界应用程序的灵活场景合成。在实验中，我们的PSNR超过了最先进的3 dB，渲染速度超过了200倍。 et.al.|[2406.03175](http://arxiv.org/abs/2406.03175)|null|
|**2024-06-05**|**Event3DGS: Event-based 3D Gaussian Splatting for Fast Egomotion**|最近出现的3D高斯飞溅（3DGS）利用了显式基于点的表示的优势，显著提高了新视图合成的渲染速度和质量。然而，在具有高动态运动或具有挑战性照明条件的环境中的3D辐射场渲染在真实世界的机器人任务中仍然存在问题。原因是快速自我运动是现实世界中普遍存在的机器人任务，这会导致运动模糊，导致重建结构中的不准确和伪影。为了缓解这个问题，我们提出了Event3DGS，这是第一种仅从原始事件流中学习高斯飞溅的方法。通过利用事件相机的高时间分辨率和基于点的显式表示，Event3DGS可以在快速自我运动下仅从事件流中重建高保真3D结构。我们的稀疏性感知采样和渐进训练方法可以实现更好的重建质量和一致性。为了进一步提高外观的保真度，我们将运动模糊形成过程明确地纳入可微分光栅化器中，该光栅化器用于有限的模糊RGB图像集来细化外观。在多个数据集上进行的大量实验验证了Event3DGS与现有方法相比具有卓越的渲染质量，训练时间减少了95%以上，渲染速度提高了几个数量级。 et.al.|[2406.02972](http://arxiv.org/abs/2406.02972)|null|
|**2024-06-04**|**WE-GS: An In-the-wild Efficient 3D Gaussian Representation for Unconstrained Photo Collections**|在计算机图形学中，从不受约束的照片集合中进行新颖视图合成（NVS）是一项具有挑战性的工作。近年来，三维高斯散射（3DGS）在静态场景的真实感和实时NVS方面显示出了良好的前景。在3DGS的基础上，我们提出了一种有效的基于点的可微渲染框架，用于从照片集中重建场景。我们的关键创新是基于残差的球面谐波系数传递模块，该模块使3DGS适应不同的照明条件和光度后处理。这个轻量级模块可以预先计算，并确保从渲染图像到3D高斯属性的有效梯度传播。此外，我们观察到，外观编码器和瞬态掩模预测器，这两个来自无约束照片采集的NVS最关键的部分，可以是互利的。我们引入了一个即插即用的轻量级空间注意力模块，以同时预测每个图像的瞬态遮挡物和潜在外观表示。经过训练和预处理，我们的方法与标准3DGS格式和渲染管道保持一致，有助于无缝集成到各种3DGS应用程序中。在不同数据集上的大量实验表明，我们的方法在新视图和外观合成的渲染质量上优于现有方法，具有高收敛性和渲染速度。 et.al.|[2406.02407](http://arxiv.org/abs/2406.02407)|null|
|**2024-06-04**|**Learning Temporally Consistent Video Depth from Video Diffusion Priors**|这项工作解决了视频深度估计的挑战，它不仅期望每帧的准确性，而且更重要的是，期望跨帧的一致性。我们没有直接从头开始开发深度估计器，而是将预测任务重新表述为条件生成问题。这使我们能够利用嵌入现有视频生成模型中的先验知识，从而降低学习难度并增强可推广性。具体来说，我们研究了如何驯服公共的稳定视频扩散（SVD），以使用图像深度和视频深度数据集的混合从输入视频中预测可靠的深度。我们从经验上证实，程序训练策略——首先优化SVD的空间层，然后优化时间层，同时保持空间层冻结——在空间准确性和时间一致性方面产生了最佳结果。我们进一步研究了在任意长视频上进行推理的滑动窗口策略。我们的观察结果表明，效率和性能之间存在权衡，一帧重叠已经产生了有利的结果。大量的实验结果表明，与现有的替代方案相比，我们的方法（称为ChronoDepth）具有优势，特别是在估计深度的时间一致性方面。此外，我们强调了在两个实际应用中更一致的视频深度的好处：深度条件视频生成和新颖的视图合成。我们的项目页面位于https://jhaoshao.github.io/ChronoDepth/. et.al.|[2406.01493](http://arxiv.org/abs/2406.01493)|null|

<p align=right>(<a href=#updated-on-20240611>back to top</a>)</p>

## 3D Reconstruction

|Publish Date|Title|Abstract|PDF|Code|
|---|---|---|---|---|
|**2024-06-07**|**Proton 3D reconstruction with T-odd TMD gluon densities**|我们提出的研究旨在通过观众模型方法计算的自旋相关TMD胶子密度来探测质子的3D胶子含量。我们的形式主义结合了观众质量的基于拟合的调制函数，旨在捕捉宽运动学范围内的纵向动量效应。特别强调时间反转偶数布尔-穆德斯和时间反转奇数西弗斯函数。准确理解这些功能对于进行核子的精确3D分析至关重要，这突出了LHC和EIC社区之间合作的重要性。 et.al.|[2406.04893](http://arxiv.org/abs/2406.04893)|null|
|**2024-06-07**|**3DRealCar: An In-the-wild RGB-D Car Dataset with 360-degree Views**|3D汽车通常用于自动驾驶系统、虚拟/增强现实和游戏。然而，现有的3D汽车数据集要么是合成的，要么是低质量的，这与高质量的真实世界3D汽车数据集中存在显著差距，并限制了它们在实际场景中的应用。在本文中，我们提出了第一个大规模的3D真实汽车数据集，称为3DRealCar，提供了三个独特的特征。（1） \textbf｛High Volume｝：2500辆汽车被3D扫描仪仔细扫描，获得具有真实世界维度的汽车图像和点云；（2） \textbf｛高质量｝：每辆车平均在200个密集、高分辨率的360度RGB-D视图中拍摄，实现高保真3D重建；（3） \textbf｛High Diversity｝：该数据集包含来自100多个品牌的各种汽车，在三种不同的照明条件下收集，包括反射、标准和黑暗。此外，我们为每个实例提供详细的汽车解析地图，以促进汽车解析任务的研究。此外，我们去除了背景点云，并将汽车方向标准化为一个统一的轴，仅在没有背景和可控渲染的汽车上进行重建。我们在3DRealCar中的每个照明条件下使用最先进的方法对3D重建结果进行基准测试。大量实验表明，3DRealCar的标准照明条件部分可以用于生产大量高质量的3D汽车，改善与汽车相关的各种2D和3D任务。值得注意的是，我们的数据集揭示了一个事实，即最近的3D重建方法在反射和黑暗照明条件下重建高质量的3D汽车时面临挑战。\textcolor｛red｝｛\href{https://xiaobiaodu.github.io/3drealcar/}｛我们的数据集在这里可用。｝｝ et.al.|[2406.04875](http://arxiv.org/abs/2406.04875)|null|
|**2024-06-07**|**Normal-guided Detail-Preserving Neural Implicit Functions for High-Fidelity 3D Surface Reconstruction**|神经隐式表示已经成为3D重建的强大范例。然而，尽管它们取得了成功，但现有的方法无法捕捉精细的几何细节和薄结构，尤其是在只有感兴趣对象的稀疏RGB视图可用的情况下。我们假设，当前从RGB或RGBD图像中学习神经隐式表示的方法会产生具有缺失部分和细节的3D表面，因为它们只依赖于0阶微分特性，即3D表面点及其投影，作为监督信号。然而，这样的特性不会捕捉点周围的局部3D几何体，也会忽略点之间的相互作用。本文证明，即使在只有两个RGB（正面和背面）图像可用的情况下，训练具有一阶微分特性的神经表示，即表面法线，也能实现高精度的3D表面重建。给定感兴趣对象的多视图RGB图像，我们首先使用现成的单目深度估计器（如depth Anything模型）生成的深度图的梯度来计算图像空间中的近似表面法线。然后，使用损失函数来训练隐式曲面回归器，该函数强制回归曲面的一阶微分特性与从Depth Anything估计的特性相匹配。我们在广泛的真实和合成数据集上进行的大量实验表明，即使使用两个RGB视图，所提出的方法也能达到前所未有的重建精度。详细的消融研究还表明，基于法线的监督在性能的显著提高中发挥着关键作用，使复杂的几何细节和薄结构的3D重建成为可能，而这些细节和结构以前很难捕捉。 et.al.|[2406.04861](http://arxiv.org/abs/2406.04861)|null|
|**2024-06-06**|**Flash3D: Feed-Forward Generalisable 3D Scene Reconstruction from a Single Image**|在本文中，我们提出了Flash3D，这是一种从单个图像进行场景重建和新颖视图合成的方法，它既非常通用又高效。为了通用性，我们从单目深度估计的“基础”模型开始，并将其扩展到全3D形状和外观重建器。为了提高效率，我们将这种扩展建立在前馈高斯散射的基础上。具体来说，我们在预测的深度预测第一层3D高斯，然后添加在空间上偏移的附加高斯层，使模型能够完成遮挡和截断后的重建。Flash3D非常高效，可以在一天内在单个GPU上进行训练，因此大多数研究人员都可以访问。在RealEstate10k上进行训练和测试时，它取得了最先进的成绩。当转移到像纽约大学这样看不见的数据集时，它的表现大大优于竞争对手。更令人印象深刻的是，当转移到KITTI时，Flash3D实现了比专门在该数据集上训练的方法更好的PSNR。在某些情况下，它甚至优于最近使用多个视图作为输入的方法。代码、模型、演示和更多结果可在https://www.robots.ox.ac.uk/~vgg/research/flash3d/。 et.al.|[2406.04343](http://arxiv.org/abs/2406.04343)|null|
|**2024-06-06**|**Coarse-To-Fine Tensor Trains for Compact Visual Representations**|学习视觉数据的紧凑、高质量和易于优化的表示的能力对于许多应用程序（如新颖的视图合成和3D重建）至关重要。最近的工作表明，在使用张量网络来设计这种紧凑和高质量的表示方面取得了实质性的成功。然而，优化基于张量的表示，特别是高度紧凑的张量列表示的能力仍然缺乏。这阻碍了从业者为视觉数据部署张量网络的全部潜力。为此，我们提出了“延长上采样张量序列（PuTT）”，这是一种以从粗到细的方式学习张量序列表示的新方法。我们的方法涉及延长或“上采样”已学习的张量序列表示，创建一个增量细化的“从粗到细”张量序列。我们沿着三个轴来评估我们的表示：（1）。压缩，（2）。去噪能力，以及（3）。图像完成能力。为了评估这些轴，我们考虑了图像拟合、3D拟合和新视图合成的任务，其中与最先进的基于张量的方法相比，我们的方法显示出改进的性能。有关完整结果，请参阅我们的项目网页：https://sebulo.github.io/PuTT_website/ et.al.|[2406.04332](http://arxiv.org/abs/2406.04332)|**[link](https://github.com/sebulo/PuTT)**|
|**2024-06-06**|**Sparse Multi-baseline SAR Cross-modal 3D Reconstruction of Vehicle Targets**|由于数据稀疏性，多基线SAR三维成像面临着重大挑战。近年来，深度学习技术在提高稀疏SAR三维成像质量方面取得了显著成功。然而，以前的工作通常依赖于全孔径高分辨率雷达图像来监督深度神经网络（DNN）的训练，仅利用雷达数据中的单模态信息。因此，成像性能有限，并且获取多基线SAR的全孔径数据成本高昂，有时在现实应用中不切实际。在本文中，我们提出了一种跨模态重建网络（CMR-Net），该网络将可微分渲染和跨模态监督与光学图像相结合，将车辆目标的高度稀疏的多基线SAR 3D图像重建为视觉结构化和高分辨率的图像。我们精心设计了网络架构和训练策略，以增强网络泛化能力。值得注意的是，仅在模拟数据上训练的CMR-Net在公开的模拟数据集和实际测量数据集上都展示了高分辨率重建能力，优于基于压缩传感和其他基于学习的方法的传统稀疏重建算法。此外，使用光学图像作为监督提供了一种成本效益高的方法来构建训练数据集，降低了方法传播的难度。我们的工作展示了深度学习在多基线SAR三维成像中的广阔前景，并为基于跨模态学习理论的雷达成像研究提供了一条新的途径。 et.al.|[2406.04158](http://arxiv.org/abs/2406.04158)|null|
|**2024-06-06**|**C^2RV: Cross-Regional and Cross-View Learning for Sparse-View CBCT Reconstruction**|锥束计算机断层扫描（CBCT）是一种重要的成像技术，广泛应用于医疗场景，如诊断和术前计划。使用较少的投影视图重建CT，也称为稀疏视图重建，可以减少电离辐射，进一步有利于介入放射学。与传统的平行/扇形束CT的稀疏视图重建相比，CBCT重建更具挑战性，因为基于锥形X射线束的测量过程会增加维数。作为一个二维到三维重建问题，尽管已经引入了隐式神经表示来实现有效的训练，但在以前的工作中只考虑了局部特征，并且平等地处理了不同的视图，导致了空间不一致性和在复杂解剖结构上的较差性能。为此，我们提出了C^2RV，通过利用显式多尺度体积表示来实现3D空间中的跨区域学习。此外，引入了比例-视图交叉注意力模块来自适应地聚合多尺度和多视图特征。大量实验表明，在具有不同解剖结构的数据集上，我们的C^2RV比以前最先进的方法实现了一致和显著的改进。 et.al.|[2406.03902](http://arxiv.org/abs/2406.03902)|**[link](https://github.com/xmed-lab/C2RV-CBCT)**|
|**2024-06-05**|**Ouroboros3D: Image-to-3D Generation via 3D-aware Recursive Diffusion**|现有的单图像到3D的创建方法通常包括两个阶段的过程，首先生成多视图图像，然后使用这些图像进行3D重建。然而，分别训练这两个阶段会导致推理阶段出现显著的数据偏差，从而影响重建结果的质量。我们引入了一个统一的3D生成框架，名为Ouroboros3D，它将基于扩散的多视图图像生成和3D重建集成到递归扩散过程中。在我们的框架中，这两个模块通过自我调节机制进行联合训练，使它们能够适应彼此的特征，从而进行稳健的推理。在多视图去噪过程中，多视图扩散模型使用重建模块在先前时间步长渲染的3D感知映射作为附加条件。具有3D感知反馈的递归扩散框架将整个过程统一起来，并提高了几何一致性。实验表明，我们的框架优于这两个阶段的分离以及在推理阶段将它们结合的现有方法。项目页面：https://costwen.github.io/Ouroboros3D/ et.al.|[2406.03184](http://arxiv.org/abs/2406.03184)|**[link](https://github.com/Costwen/Ouroboros3D)**|
|**2024-06-05**|**CAMEL. II. A 3D Coronal Mass Ejection Catalog Based on Coronal Mass Ejection Automatic Detection with Deep Learning**|日冕物质抛射是地磁风暴的主要驱动因素，可能会造成严重的空间天气影响。CME的自动检测、跟踪和三维（3D）重建对于CME到达的操作预测非常重要。日地关系天文台航天器上的COR1日冕仪促进了广泛的偏振观测，非常适合建立3D CME系统。我们开发了这样一个3D系统，包括四个模块：分类、分割、跟踪和3D重建。我们推广了我们之前预训练的分类模型来对COR1冠状图图像进行分类。随后，由于没有公开可用的CME分割数据集，我们使用大角度和光谱日冕仪C2观测手动注释CME的结构区域。利用基于变换器的模型，我们在CME分割方面取得了最先进的结果。此外，我们对跟踪算法进行了改进，以解决多个CME的分离任务。在最后一个模块中，跟踪结果与偏振比技术相结合，用于开发第一个单视图三维CME目录，而不需要手动掩模注释。我们的方法在自动2D CME目录中提供了更高的精度，并提供了更可靠的CME物理参数，包括3D传播方向和速度。上述3D CME系统可以应用于具有偏振测量能力的任何冠状图数据。 et.al.|[2406.02946](http://arxiv.org/abs/2406.02946)|null|
|**2024-06-04**|**3D-HGS: 3D Half-Gaussian Splatting**|照片真实感三维重建是三维计算机视觉中的一个基本问题。由于最近神经渲染技术的出现，该领域已经取得了相当大的进步。这些技术主要致力于学习3D场景的体积表示，并通过渲染产生的损失函数来细化这些表示。其中，3D高斯散射（3D-GS）已成为一种重要的方法，超过了神经辐射场（NeRFs）。3D-GS使用参数化的3D高斯来建模空间位置和颜色信息，并结合基于瓦片的快速渲染技术。尽管3D高斯核具有卓越的渲染性能和速度，但它在准确表示不连续函数方面存在固有的局限性，尤其是在形状不连续的边缘和角落，以及在颜色不连续的不同纹理上。为了解决这个问题，我们建议使用3D半高斯（3D-HGS）内核，它可以用作即插即用内核。我们的实验证明了它们能够在不影响渲染速度的情况下提高当前3D-GS相关方法的性能，并在各种数据集上实现最先进的渲染性能。 et.al.|[2406.02720](http://arxiv.org/abs/2406.02720)|null|

<p align=right>(<a href=#updated-on-20240611>back to top</a>)</p>

## Diffusion

|Publish Date|Title|Abstract|PDF|Code|
|---|---|---|---|---|
|**2024-06-07**|**DVOS: Self-Supervised Dense-Pattern Video Object Segmentation**|视频对象分割方法主要依赖于大规模像素精确的人类注释数据集来进行模型开发。在密集视频对象分割（DVOS）场景中，每个视频帧包含数百个小的、密集的和部分遮挡的对象。因此，即使是单个帧的劳动密集型手动注释也往往需要数小时，这阻碍了DVOS在许多应用程序中的开发。此外，在图案密集的视频中，跟随大量向不同方向移动的物体会带来额外的挑战。为了应对这些挑战，我们通过多任务学习，利用基于扩散的方法，提出了一种用于DVOS的半自监督时空方法。模拟真实视频的光流并模拟其运动，我们开发了一种方法来合成可用于训练DVOS模型的计算注释视频；通过利用弱标记（计算生成但不精确）数据，进一步提高了模型性能。为了证明所提出方法的实用性和有效性，我们开发了DVOS模型，用于手持和无人机捕捉视频的小麦头部分割，捕捉不同生长阶段不同位置田地中的小麦作物，从抽穗到成熟。尽管只使用了一些手动注释的视频帧，但所提出的方法产生了高性能的模型，在无人机捕获的外部测试集上测试时，Dice得分为0.82。虽然我们展示了所提出的小麦头部分割方法的有效性，但它的应用可以扩展到其他作物或其他领域的DVOS，如群体分析或微观图像分析。 et.al.|[2406.05131](http://arxiv.org/abs/2406.05131)|null|
|**2024-06-07**|**Ohms law lost and regained: observation and impact of zeros and poles**|量子电导及其经典的波模拟，即透射率，是由传输矩阵的本征值之和给出的。扩散介质中的最低传输本征值在电导中的作用可以忽略不计，而且在任何情况下都太小而无法观察到。在这里，我们观察到微波波导中最低的传输本征信道，尽管它比标称噪声电平低几个数量级，并表明传输本征值之间以及传输矩阵的零点和极点之间的全局相关性降低了传输。当样本输出上的能量密度在拓扑传输零点处消失时，或者当纵向速度在与新信道的交叉处精确消失时，传输就会消失。这将电导降低与态密度调制成比例的量。根据对应原理，电导随着通道数随样本宽度的增加而接近欧姆定律。透射矩阵的探索为人们对介观输运和超灵敏检测技术的新理解打开了大门。 et.al.|[2406.05112](http://arxiv.org/abs/2406.05112)|null|
|**2024-06-07**|**Large Generative Graph Models**|大生成模型（LGM），如GPT、稳定扩散、Sora和Suno，是在大量的语言语料库、图像、视频和音频上进行训练的，这些语料库、图像和音频来自许多领域。这种针对各种精心策划的数据的培训模式是生成创造性和明智内容的核心。然而，以前所有的图生成模型（如GraphRNN、MDVAE、MoFlow、GDSS和DiGress）每次都只在一个数据集上进行训练，无法复制LGM在其他领域取得的革命性成功。为了弥补这一关键差距，我们提出了一类新的图生成模型，称为大型图生成模型（LGGM），该模型在来自13个不同领域的大型图语料库（超过5000张图）上进行训练。我们的经验证明，预先训练的LGGM具有优于现有的图生成模型的零样本生成能力。此外，我们预先训练的LGGM可以很容易地使用目标域的图形进行微调，并显示出比直接从头开始训练的LGGM更好的性能，这是现实世界定制的坚实起点。受稳定扩散的启发，我们进一步为LGGM提供了在给定文本提示（文本到图）的情况下生成图的能力，例如网络名称和域的描述（即，“电源1138总线图表示配电系统中的总线网络。”）和网络统计（即，该图的平均程度较低，适合于对社交媒体交互进行建模。”）。这种“文本到图”功能将广泛的世界知识集成到底层语言模型中，为用户提供对生成的图的细粒度控制。我们在发布代码、模型检查点和数据集https://lggm-lg.github.io/. et.al.|[2406.05109](http://arxiv.org/abs/2406.05109)|null|
|**2024-06-07**|**CoNo: Consistency Noise Injection for Tuning-free Long Video Diffusion**|已经提出了调整自由长视频扩散，以通过重用来自预训练的短视频扩散模型的知识而无需再训练来生成具有丰富内容的延长时长视频。然而，大多数工作忽略了细粒度的长期视频一致性建模，导致场景一致性有限（即不合理的对象或背景转换），尤其是在多个文本输入的情况下。为了缓解这种情况，我们提出了称为CoNo的一致性噪声注入，它引入了“回顾”机制来增强不同视频片段之间的细粒度场景转换，并设计了长期一致性正则化，以消除通过噪声预测扩展视频内容时的内容偏移。特别是，“回顾”机制将噪声调度过程分解为三个重要部分，其中一个内部噪声预测部分被注入到两个视频扩展部分中，旨在实现两个视频片段之间的细粒度转换。长期一致性正则化的重点是显式地最小化扩展视频片段的预测噪声与原始视频片段之间的逐像素距离，从而防止突然的场景转换。通过在单文本和多文本提示条件下执行长视频生成，大量实验已经证明了上述策略的有效性。该项目已在中提供https://wxrui182.github.io/CoNo.github.io/. et.al.|[2406.05082](http://arxiv.org/abs/2406.05082)|null|
|**2024-06-07**|**GenHeld: Generating and Editing Handheld Objects**|抓握是一项重要的人类活动，在机器人、计算机视觉和认知科学中已有很长时间的研究。现有的大多数作品都是从以3D或2D物体表示为条件合成手部姿势的角度来研究抓取的。我们提出GenHeld来解决以3D手模型或2D图像为条件合成握持物体的逆问题。给定手的3D模型，GenHeld 3D可以使用称为对象代码的紧凑对象表示从大型数据集中选择看似合理的握持对象。然后定位和定向所选对象，以在不改变手姿势的情况下形成看似合理的抓握。如果只有2D手部图像可用，GenHeld 2D可以编辑此图像以添加或替换持有的对象。GenHeld 2D通过将GenHeld 3D的功能与基于扩散的图像编辑相结合来进行操作。结果和实验表明，我们的性能优于基线，可以在2D和3D中生成看似合理的持有物体。我们的实验表明，我们的方法在3D和2D中都实现了保持对象合成的高质量和合理性。 et.al.|[2406.05059](http://arxiv.org/abs/2406.05059)|**[link](https://github.com/ChaerinMin/GenHeld)**|
|**2024-06-07**|**Digital Twins of the EM Environment: Benchmark for Ray Launching Models**|数字孪生已经成为准确表示电磁（EM）无线环境的一种很有前途的范例。由此产生的现实的虚拟表示有助于全面深入了解传播环境，增强物理通信层面的多层决策过程。本文研究了无线通信传播的数字化，特别强调了实时数字双胞胎基于射线的传播模拟的不可或缺的方面。提出了一个基于射线的传播模拟的基准来评估计算时间，两种城市场景的特征是不同的网格复杂性、单无线链路和多无线链路配置，以及有/无散射的模拟。进行了详尽的经验分析，显示和比较了不同基于射线的解决方案的行为。通过提供标准化的模拟和场景，这项工作为参与实时数字双胞胎的实现和基于射线的传播模型的优化的从业者提供了技术基准。 et.al.|[2406.05042](http://arxiv.org/abs/2406.05042)|null|
|**2024-06-07**|**Efficient 3D Shape Generation via Diffusion Mamba with Bidirectional SSMs**|序列建模的最新进展导致了Mamba体系结构的发展，该体系结构以其选择性状态空间方法而闻名，为有效的长序列处理提供了一条有前途的途径。然而，它在三维形状生成中的应用，特别是在高分辨率下，仍然没有得到充分的探索。具有自注意机制的传统扩散变换器（DiT）尽管具有潜力，但随着输入长度的增加，由于注意操作的三次复杂性，仍面临可扩展性挑战。这种复杂性成为处理高分辨率体素大小时的一个重要障碍。为了应对这一挑战，我们介绍了一种为3D点云生成扩散曼巴（DiM-3D）量身定制的新型扩散架构。该架构放弃了传统的注意力机制，而是利用Mamba架构的固有效率来保持相对于序列长度的线性复杂性。DiM-3D的特点是快速推理时间和显著降低的计算需求，以减少的Gflops进行量化，从而解决了先前模型的关键可扩展性问题。我们在ShapeNet基准上的经验结果表明，DiM-3D在生成高保真度和多样化的3D形状方面实现了最先进的性能。此外，DiM-3D在3D点云完成等任务中显示出卓越的功能。这不仅证明了该模型的可扩展性，还强调了其在生成高级3D形状建模所需的详细、高分辨率体素方面的效率，尤其是在需要高分辨率体元大小的环境中表现出色。通过这些发现，我们展示了扩散曼巴框架在3D形状生成中的卓越可扩展性和效率，为该领域树立了新的标准，并为未来高分辨率3D建模技术的探索铺平了道路。 et.al.|[2406.05038](http://arxiv.org/abs/2406.05038)|null|
|**2024-06-07**|**Linear stability analysis for a system of singular amplitude equations arising in biomorphology**|我们研究了在存在守恒定律的情况下，与对流图灵分岔相关的奇异振幅方程组的指数周期解的线性稳定性，这在现代生物形态学模型、二元流体和其他方面都有出现。由一个复杂的Ginzburg-Landau方程和一个与守恒定律相关的“平均模式”中的奇异对流扩散方程组成，作者之前已经证明了这一点，即在经典的Ginzburg Landau情况下，尽管现在的波幅ε是奇异的，但可以进行常系数线性化稳定性分析，从而为稳定性、作为振幅方程解的指数函数和求解潜在PDE的相关周期模式提供有用的必要条件。在这里，我们通过一个精细的双参数矩阵摄动分析表明，（严格）满足这些必要条件对于Schneider意义上的扩散稳定性也是足够的，从而产生相应的结果，并为潜在PDE提供非线性稳定性。此外，我们还证明了它们可以被解释为沿着通过Darcy型归约近似的非正双曲慢流形的稳定性以及沿着横向平均模的吸引力，并与Hacker Schneider Zimmerman的有限时间近似定理相联系。 et.al.|[2406.05037](http://arxiv.org/abs/2406.05037)|null|
|**2024-06-07**|**Generative diffusion models for synthetic trajectories of heavy and light particles in turbulence**|重颗粒和轻颗粒通常存在于许多自然现象和工业过程中，如不可压缩湍流中的气泡、灰尘和液滴的悬浮液。基于最近使用扩散模型的机器学习方法，该模型成功地在三维湍流中生成了单个示踪剂轨迹，并通过了跨时间尺度的大多数统计基准，我们将该模型扩展到包括重粒子和轻粒子。给定粒子类型（示踪剂、轻粒子或重粒子），该模型可以生成合成的、真实的轨迹，具有正确的加速肥尾分布、异常幂律和与比例相关的局部斜率特性。这项工作为未来探索使用扩散模型为不同的流动配置生成高质量的合成数据集铺平了道路，可能允许在不同设置之间进行插值并适应新的条件。 et.al.|[2406.05008](http://arxiv.org/abs/2406.05008)|null|
|**2024-06-07**|**CityCraft: A Real Crafter for 3D City Generation**|城市场景生成在自动驾驶、智慧城市发展和交通仿真中得到了极大的关注。它有助于增强基础设施规划和监控解决方案。现有的方法采用了两阶段的过程，包括城市布局生成，通常使用变分自动编码器（VAE）、生成对抗性网络（GAN）或变形金刚，然后进行神经渲染。这些技术在渲染的城市场景中往往表现出有限的多样性和明显的伪影。渲染的场景缺乏多样性，类似于训练图像，导致风格单调。此外，这些方法缺乏规划能力，导致生成的场景不太逼真。在本文中，我们介绍了CityCraft，这是一个创新的框架，旨在增强城市场景生成的多样性和质量。我们的方法集成了三个关键阶段：首先，部署扩散变压器（DiT）模型来生成多样化和可控的2D城市布局。随后，基于用户提示和语言指南，利用大型语言模型（LLM）在这些布局中战略性地制定土地使用计划。基于生成的布局和城市规划，我们利用资产检索模块和Blender进行精确的资产放置和场景构建。此外，我们为该领域贡献了两个新的数据集：1）CityCraft OSM数据集，包括城市区域的2D语义布局、相应的卫星图像和详细的注释。2） CityCraft Buildings数据集，以数千种多样的高质量3D建筑资产为特色。CityCraft在生成逼真的3D城市方面实现了最先进的性能。 et.al.|[2406.04983](http://arxiv.org/abs/2406.04983)|null|

<p align=right>(<a href=#updated-on-20240611>back to top</a>)</p>

## NeRF

|Publish Date|Title|Abstract|PDF|Code|
|---|---|---|---|---|
|**2024-06-06**|**ReFiNe: Recursive Field Networks for Cross-modal Multi-scene Representation**|最先进的多形状表示方法（单个模型“打包”多个对象）的常见权衡包括将建模精度与内存和存储进行权衡。我们展示了如何以比以前更高的精度和低内存使用率对表示为连续神经场的多个形状进行编码。我们方法的关键是利用对象自相似性的递归层次公式，从而产生高度压缩和高效的形状潜在空间。由于递归公式，我们的方法支持空间和全局到局部的潜在特征融合，而无需初始化和维护辅助数据结构，同时仍允许连续的字段查询，以实现光线跟踪等应用。在一组不同数据集上的实验中，我们提供了令人信服的定性结果，并展示了每个数据集使用单个网络的最先进的多场景重建和压缩结果。 et.al.|[2406.04309](http://arxiv.org/abs/2406.04309)|null|
|**2024-06-06**|**Vectorized Conditional Neural Fields: A Framework for Solving Time-dependent Parametric Partial Differential Equations**|变压器模型越来越多地用于求解偏微分方程（PDE）。已经提出了几种自适应方法，所有这些方法都存在变压器的典型问题，如二次记忆和时间复杂性。此外，用于PDE求解的所有流行体系结构都缺乏理想代理模型的几个期望性质中的至少一个，例如（i）对训练期间未看到的PDE参数的泛化，（ii）空间和时间零样本超分辨率，（iii）连续时间外推，（iv）对1D、2D和3D PDE的支持，以及（v）对更长时间展开的有效推断。为了解决这些局限性，我们提出了矢量化条件神经场（VCNeFs），它将时间相关偏微分方程的解表示为神经场。然而，与先前的方法相反，对于一组多个时空查询点，VCNeF并行计算它们的解决方案，并通过注意力机制对它们的依赖性进行建模。此外，VCNeF可以根据偏微分方程的初始条件和参数来调节神经场。一组广泛的实验表明，VCNeF与现有的基于ML的代理模型具有竞争力，并且往往优于现有的代理模型。 et.al.|[2406.03919](http://arxiv.org/abs/2406.03919)|**[link](https://github.com/jhagnberger/vcnef)**|
|**2024-06-05**|**Dynamic 3D Gaussian Fields for Urban Areas**|我们提出了一种用于大规模动态城市区域的新型视图合成（NVS）的高效神经3D场景表示。现有作品由于其有限的视觉质量和非交互式渲染速度，不太适合混合现实或闭环模拟等应用。最近，基于光栅化的方法已经以令人印象深刻的速度实现了高质量的NVS。然而，这些方法仅限于小规模、同质的数据，即它们不能处理由于天气、季节和照明而引起的严重外观和几何变化，也不能扩展到具有数千张图像的更大的动态区域。我们提出了4DGF，这是一种神经场景表示，可扩展到大规模动态城市区域，处理异构输入数据，并显著提高渲染速度。我们使用3D高斯作为有效的几何支架，同时依赖神经场作为紧凑灵活的外观模型。我们在全局范围内通过场景图集成场景动力学，同时通过变形在局部范围内建模关节运动。这种分解方法实现了适用于真实世界应用程序的灵活场景合成。在实验中，我们的PSNR超过了最先进的3 dB，渲染速度超过了200倍。 et.al.|[2406.03175](http://arxiv.org/abs/2406.03175)|null|
|**2024-06-04**|**A fast neural emulator for interstellar chemistry**|天体化学模型是解释不同环境中分子和原子物种观测结果的重要工具。然而，这些模型非常耗时，妨碍了对参数空间的彻底探索，导致了不确定性和偏差结果。使用神经网络来模拟天体化学模型的行为是规避这一问题的一种方法，它可以基于真实的天体化学模型提供快速计算。在本文中，我们提出了一个基于条件神经场的天文化学代码Nautilus的快速神经模拟器。由此产生的模型在1到10 $^7$年之间的任意时间内产生了192种物种的丰度。所有物种的不确定性都远低于0.2 dex，而计算时间比Nautilus小10$^4$ 。这将为执行更复杂的正向模型以更好地了解星际介质的物理性质开辟可能性。作为这些模型威力的一个例子，我们对Nautilus预测的电子丰度进行了特征重要性分析。我们发现，在低密度气体中，电子密度与初始硫丰度有关。将初始硫丰度从耗尽的情况增加到宇宙丰度会导致电子密度增加一个数量级。这种增强可能会对恒星形成地点的气体动力学产生潜在影响。 et.al.|[2406.02387](http://arxiv.org/abs/2406.02387)|null|
|**2024-06-05**|**AROMA: Preserving Spatial Structure for Latent PDE Modeling with Local Neural Fields**|我们提出了AROMA（带注意力的注意力降阶模型），这是一个旨在使用局部神经场增强偏微分方程（PDE）建模的框架。我们灵活的编码器-解码器架构可以从各种数据类型中获得空间物理场的平滑潜在表示，包括不规则网格输入和点云。这种多功能性消除了打补丁的需要，并允许高效处理各种几何形状。我们的潜在表示的顺序性质可以在空间上进行解释，并允许使用条件转换器来建模偏微分方程的时间动力学。通过采用基于扩散的公式，与传统的MSE训练相比，我们实现了更大的稳定性，并实现了更长的推广时间。AROMA在模拟1D和2D方程方面的卓越性能突显了我们的方法在捕捉复杂动力学行为方面的有效性。 et.al.|[2406.02176](http://arxiv.org/abs/2406.02176)|null|
|**2024-06-04**|**Activity patterns in ring networks of quadratic integrate-and-fire neurons with synaptic and gap junction coupling**|我们考虑具有非局部突触和间隙连接耦合的二次积分和激发神经元的环形网络。相应的神经场模型支持驻波和行波以及倾斜波等解决方案。我们证明了这些解中的许多都满足自洽方程，当参数变化时，自洽方程可以用来跟随它们。我们对神经场模型进行了数值分叉分析，重点研究了不同间隙结耦合强度的影响。我们的方法通常适用于各种各样的二次积分和激发神经元网络。 et.al.|[2406.01881](http://arxiv.org/abs/2406.01881)|null|
|**2024-06-03**|**Enhancing Dynamic CT Image Reconstruction with Neural Fields Through Explicit Motion Regularizers**|具有高度欠采样数据的动态逆问题的图像重建提出了一个主要挑战：不考虑过程的动力学会导致没有时间规律的不真实运动。已经提出了惩罚时间导数或引入运动模型正则化子的变分方法，以使用基于网格的离散化来关联后续帧并提高图像质量。神经场通过深度神经网络提供了所需时空量的替代参数化，这是一种轻量级、连续且偏向于平滑表示的网络。归纳偏差已被用于增强动态逆问题的时间规律性，从而仅通过最小化数据保真度项来优化神经场。在本文中，我们研究并展示了在2D+时间计算机断层扫描中引入基于显式PDE的运动正则化子，即光流方程，用于优化神经场的好处。我们还将神经场与基于网格的求解器进行了比较，并表明前者的性能优于后者。 et.al.|[2406.01299](http://arxiv.org/abs/2406.01299)|null|
|**2024-06-03**|**Pattern Formation in a Spiking Neural-Field of Renewal Neurons**|阐明神经模式形成背后的神经生理学机制仍然是计算神经科学中的一个突出挑战。在这篇论文中，我们通过考虑更新神经元网络来解决理解神经模式出现的问题，更新神经元是一类公认的尖峰细胞。在热力学极限下，网络的动力学可以精确地用一个偏微分方程和一个非局部微分方程来表示。确定了非局部系统的稳态，并进行了扰动分析，以分析表征图灵不稳定性发生的条件。考虑到突触耦合和外部驱动等神经网络参数，我们用数值方法获得了将异步状态与模式出现分开的分叉线。我们的理论发现为尖峰神经网络中图灵模式的出现提供了一个新的、有见地的视角。从长远来看，我们的形式主义将能够研究神经模式，同时保持微观细胞特性、网络耦合和图灵不稳定性的出现之间的联系。 et.al.|[2406.01167](http://arxiv.org/abs/2406.01167)|null|
|**2024-06-02**|**Representing Animatable Avatar via Factorized Neural Fields**|对于从单眼视频中重建高保真度的人体3D模型，保持一致的大规模体型以及精细匹配的细微皱纹至关重要。本文探讨了以下观察结果，即每帧渲染结果可以分解为与姿势无关的分量和相应的与姿势相关的等价物，以促进帧一致性。通过限制这两个分量的频带，可以进一步改进姿态自适应纹理。详细地说，与姿势无关的输出预计是低频的，而高频信息与姿势相关因素有关。我们通过具有不同频率分量的双分支网络实现了整个输入视频的粗体轮廓和时变的细粒度纹理特征的连贯保存。第一分支以规范空间中的坐标作为输入，而第二分支另外考虑由第一分支输出的特征和每个帧的姿态信息。我们的网络整合了两个分支预测的信息，并利用体积渲染生成照片逼真的3D人体图像。通过实验，我们证明了我们的网络在保留高频细节和确保身体轮廓一致方面超越了基于神经辐射场（NeRF）的最先进方法。 et.al.|[2406.00637](http://arxiv.org/abs/2406.00637)|null|
|**2024-05-31**|**Neural Gaussian Scale-Space Fields**|高斯尺度空间是信号表示和处理的基石，在滤波、多尺度分析、抗混叠等方面都有应用。然而，获得这样的尺度空间是昂贵和繁琐的，特别是对于诸如神经场的连续表示。我们提出了一种有效且轻量级的方法来学习任意信号的全连续、各向异性高斯尺度空间。基于傅立叶特征调制和Lipschitz边界，我们的方法是自监督训练的，即训练不需要任何手动滤波。我们的神经高斯尺度空间场忠实地捕捉各种模态的多尺度表示，并支持多种应用。其中包括图像、几何、光台数据、纹理抗锯齿和多尺度优化。 et.al.|[2405.20980](http://arxiv.org/abs/2405.20980)|null|

<p align=right>(<a href=#updated-on-20240611>back to top</a>)</p>

[contributors-shield]: https://img.shields.io/github/contributors/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[contributors-url]: https://github.com/Vincentqyw/cv-arxiv-daily/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[forks-url]: https://github.com/Vincentqyw/cv-arxiv-daily/network/members
[stars-shield]: https://img.shields.io/github/stars/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[stars-url]: https://github.com/Vincentqyw/cv-arxiv-daily/stargazers
[issues-shield]: https://img.shields.io/github/issues/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[issues-url]: https://github.com/Vincentqyw/cv-arxiv-daily/issues

