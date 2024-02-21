[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]

## Updated on 2024.02.21
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
|**2024-02-20**|**Improving Robustness for Joint Optimization of Camera Poses and Decomposed Low-Rank Tensorial Radiance Fields**|在本文中，我们提出了一种算法，该算法允许仅使用2D图像作为监督，对由分解的低秩张量表示的相机姿态和场景几何进行联合细化。首先，我们基于1D信号进行了一项试点研究，并将我们的发现与3D场景联系起来，在3D场景中，基于体素的NeRF上的初始关节姿态优化可以很容易地导致次优解。此外，基于频谱分析，我们建议在2D和3D辐射场上应用卷积高斯滤波器，以实现从粗到细的训练计划，从而实现联合相机姿态优化。利用分解后的低秩张量中的分解特性，我们的方法实现了与强力3D卷积等效的效果，只需很少的计算开销。为了进一步提高联合优化的鲁棒性和稳定性，我们还提出了平滑的2D监督、随机缩放的核参数和边缘引导的损失掩模技术。广泛的定量和定性评估表明，我们提出的框架在新的视图合成方面取得了卓越的性能，并实现了快速收敛的优化。 et.al.|[2402.13252](http://arxiv.org/abs/2402.13252)|**[link](https://github.com/nemo1999/joint-tensorf)**|
|**2024-02-20**|**Real-time High-resolution View Synthesis of Complex Scenes with Explicit 3D Visibility Reasoning**|绘制复杂场景的照片逼真的新颖视图图像一直是计算机图形学中的一个长期挑战。近年来，在视图合成领域，在提高渲染质量和加快渲染速度方面取得了很大的研究进展。然而，当使用稀疏视图渲染复杂的动态场景时，由于遮挡问题，渲染质量仍然有限。此外，对于在动态场景中渲染高分辨率图像，渲染速度仍远未达到实时性。在这项工作中，我们提出了一种可推广的视图合成方法，该方法可以从稀疏视图实时渲染复杂静态和动态场景的高分辨率新视图图像。为了解决由输入视图的稀疏性和捕获场景的复杂性引起的遮挡问题，我们引入了一种显式3D可见性推理方法，该方法可以有效地估计采样的3D点对输入视图的可见性。所提出的可见性推理方法是完全可微分的，可以很好地适应体绘制管道，使我们能够在训练网络时只使用多视图图像作为监督，同时细化几何体和纹理。此外，我们管道中的每个模块都经过精心设计，以绕过耗时的MLP查询过程，提高高分辨率图像的渲染质量，使我们能够实时渲染高分辨率的新视图图像。实验结果表明，我们的方法在渲染质量和速度上都优于以前的视图合成方法，尤其是在处理具有稀疏视图的复杂动态场景时。 et.al.|[2402.12886](http://arxiv.org/abs/2402.12886)|null|
|**2024-02-20**|**MVDiffusion++: A Dense High-resolution Multi-view Diffusion Model for Single or Sparse-view 3D Object Reconstruction**|本文提出了一种用于3D对象重建的神经结构MVDiffusion++，该结构在给定一张或几张没有相机姿势的图像的情况下合成对象的密集和高分辨率视图。MVDiffusion++通过两个令人惊讶的简单想法实现了卓越的灵活性和可扩展性：1）“无姿势架构”，其中2D潜在特征之间的标准自关注在任意数量的条件视图和生成视图中学习3D一致性，而无需显式使用相机姿势信息；和2）一种“视图丢弃策略”，在训练期间丢弃大量输出视图，这减少了训练时间内存占用，并在测试时实现了密集和高分辨率的视图合成。我们使用Ob厌恶对象进行训练，使用谷歌扫描对象进行评估，并使用标准的新视图合成和3D重建指标，其中MVDiffusion++显著优于当前的技术状态。我们还通过将MVDiffusion++与文本到图像生成模型相结合，展示了一个文本到3D应用程序示例。 et.al.|[2402.12712](http://arxiv.org/abs/2402.12712)|null|
|**2024-02-19**|**Binary Opacity Grids: Capturing Fine Geometric Detail for Mesh-Based View Synthesis**|虽然基于表面的视图合成算法由于其低计算要求而很有吸引力，但它们往往难以再现薄结构。相比之下，将场景的几何体建模为体积密度场（例如NeRF）的更昂贵的方法擅长于重建精细的几何细节。然而，密度场通常以“模糊”的方式表示几何体，这阻碍了曲面的精确定位。在这项工作中，我们修改了密度场，以鼓励它们向表面会聚，而不影响它们重建薄结构的能力。首先，我们使用离散的不透明度网格表示，而不是连续的密度场，这允许不透明度值在曲面上从零不连续地过渡到一。其次，我们通过每个像素投射多条光线来消除混叠，这允许在不使用半透明体素的情况下对遮挡边界和亚像素结构进行建模。第三，我们最小化不透明度值的二元熵，这通过鼓励不透明度值在训练结束时进行二元化来促进表面几何的提取。最后，我们开发了一种基于融合的网格划分策略，然后进行网格简化和外观模型拟合。与现有的基于网格的方法相比，我们的模型生成的紧凑网格可以在移动设备上实时渲染，并实现显著更高的视图合成质量。 et.al.|[2402.12377](http://arxiv.org/abs/2402.12377)|null|
|**2024-02-15**|**GES: Generalized Exponential Splatting for Efficient Radiance Field Rendering**|3D高斯散射的进步显著加速了3D重建和生成。然而，它可能需要大量的高斯，这会产生大量的内存占用。本文介绍了GES（Generalized Exponential Splatting），这是一种利用广义指数函数（GEF）对3D场景进行建模的新表示，需要更少的粒子来表示场景，因此在效率上显著优于高斯飞溅方法，并具有基于高斯的实用程序的即插即用替换能力。GES在原理性1D设置和逼真的3D场景中都得到了理论和实证验证。它被证明可以更准确地表示具有尖锐边缘的信号，由于其固有的低通特性，这对高斯人来说通常是具有挑战性的。我们的实证分析表明，GEF在拟合自然发生的信号（如正方形、三角形和抛物线信号）方面优于高斯，从而减少了对增加高斯飞溅的内存占用的广泛拆分操作的需要。借助调频损耗，GES在新的视图合成基准中实现了有竞争力的性能，同时所需的内存存储量不到高斯飞溅的一半，并将渲染速度提高了39%。代码可在项目网站上获得https://abdullahamdi.com/ges . et.al.|[2402.10128](http://arxiv.org/abs/2402.10128)|null|
|**2024-02-14**|**PC-NeRF: Parent-Child Neural Radiance Fields Using Sparse LiDAR Frames in Autonomous Driving Environments**|大规模的3D场景重建和新颖的视图合成对于自动驾驶汽车至关重要，尤其是利用时间稀疏的激光雷达帧。然而，传统的显式表示仍然是以无限分辨率表示重建和合成场景的一个重要瓶颈。尽管最近开发的神经辐射场（NeRF）在隐式表示中显示出令人信服的结果，但使用稀疏激光雷达帧进行大规模3D场景重建和新的视图合成的问题仍未得到探索。为了弥补这一差距，我们提出了一种3D场景重建和新的视图合成框架，称为父子神经辐射场（PC NeRF）。该框架基于父NeRF和子NeRF两个模块，实现了分层空间划分和多级场景表示，包括场景、分段和点级别。多级场景表示增强了稀疏激光雷达点云数据的有效利用，并能够快速获取近似体积场景表示。经过大量实验，PC NeRF被证明可以在大规模场景中实现高精度的新型激光雷达视图合成和三维重建。此外，PC NeRF可以有效地处理稀疏激光雷达帧的情况，并在有限的训练时期内表现出较高的部署效率。我们的方法实施和预先培训的模型可在https://github.com/biter0088/pc-nerf. et.al.|[2402.09325](http://arxiv.org/abs/2402.09325)|**[link](https://github.com/biter0088/pc-nerf)**|
|**2024-02-11**|**BioNeRF: Biologically Plausible Neural Radiance Fields for View Synthesis**|本文介绍了BioNeRF，这是一种生物学上合理的架构，它以3D表示对场景进行建模，并通过辐射场合成新的视图。由于NeRF依赖于网络权重来存储场景的三维表示，BioNeRF实现了一种受认知启发的机制，该机制将来自多个来源的输入融合到类似记忆的结构中，提高了存储容量，并提取了更多内在和相关的信息。BioNeRF还模拟了在锥体细胞中观察到的与上下文信息有关的行为，其中记忆作为上下文提供，并与两个后续神经模型的输入相结合，一个负责产生体积密度，另一个负责渲染场景所用的颜色。实验结果表明，BioNeRF在两个数据集（真实世界图像和合成数据）中对人类感知进行编码的质量测量方面优于最先进的结果。 et.al.|[2402.07310](http://arxiv.org/abs/2402.07310)|**[link](https://github.com/leandropassosjr/bionerf)**|
|**2024-02-11**|**3D Gaussian as a New Vision Era: A Survey**|3D高斯散射（3D-GS）已成为计算机图形学领域的一个重大进步，它提供了明确的场景表示和新颖的视图合成，而不依赖于神经网络，如神经辐射场（NeRF）。这项技术在机器人、城市地图、自主导航和虚拟现实/增强现实等领域有着不同的应用。鉴于三维高斯散射的日益普及和研究的不断扩展，本文对过去一年的相关论文进行了全面的综述。我们根据特征和应用对分类法进行了调查，介绍了3D高斯飞溅的理论基础。我们通过这项调查的目标是让新的研究人员熟悉3D高斯飞溅，为该领域的开创性工作提供宝贵的参考，并启发未来的研究方向，正如我们的结论部分所讨论的那样。 et.al.|[2402.07181](http://arxiv.org/abs/2402.07181)|null|
|**2024-02-09**|**NCRF: Neural Contact Radiance Fields for Free-Viewpoint Rendering of Hand-Object Interaction**|在三维计算机视觉中，建模手与物体的交互是一项具有根本挑战性的任务。尽管在该领域已经取得了显著的进展，但现有的方法仍然无法真实地合成手与物体的交互照片，因为手与物体之间的严重相互遮挡导致渲染质量下降，以及手与物体姿态估计不准确。为了应对这些挑战，我们提出了一种新的自由视点渲染框架，即神经接触辐射场（NCRF），以从稀疏的视频集重建手与物体的交互。特别地，所提出的NCRF框架由两个关键组件组成：（a）接触优化字段，该字段从3D查询点预测准确的接触字段，以实现手和物体之间的期望接触。（b） 手对象神经辐射场，用于学习静态规范空间中的隐含手对象表示，与专门设计的手对象运动场相一致，以产生观察到的规范对应关系。我们共同学习这些关键组件，它们在视觉和几何约束下相互帮助和规则化，产生高质量的手对象重建，实现照片逼真的新颖视图合成。在HO3D和DexYCB数据集上进行的大量实验表明，我们的方法在渲染质量和姿态估计精度方面都优于当前最先进的方法。 et.al.|[2402.05532](http://arxiv.org/abs/2402.05532)|null|
|**2024-02-07**|**SPAD : Spatially Aware Multiview Diffusers**|我们提出了SPAD，这是一种从文本提示或单个图像创建一致多视图图像的新方法。为了实现多视图生成，我们通过扩展具有跨视图交互的自注意层来重新调整预训练的2D扩散模型的用途，并在Ob厌恶的高质量子集上对其进行微调。我们发现，先前工作中提出的自我关注的天真扩展（例如MVDream）会导致视图之间的内容复制。因此，我们明确地限制了基于核极几何的跨视图注意力。为了进一步增强3D一致性，我们利用从相机射线导出的Plucker坐标，并将其作为位置编码注入。这使得SPAD能够对3D井中的空间接近度进行推理。与最近只能在固定方位角和仰角下生成视图的工作不同，SPAD提供了完整的相机控制，并在Ob厌恶和谷歌扫描对象数据集中对看不见的对象进行新的视图合成方面取得了最先进的结果。最后，我们证明了使用SPAD的文本到3D生成可以防止多面Janus问题。更多详细信息，请访问我们的网页：https://yashkant.github.io/spad et.al.|[2402.05235](http://arxiv.org/abs/2402.05235)|null|

<p align=right>(<a href=#updated-on-20240221>back to top</a>)</p>

## 3D Reconstruction

|Publish Date|Title|Abstract|PDF|Code|
|---|---|---|---|---|
|**2024-02-20**|**MVDiffusion++: A Dense High-resolution Multi-view Diffusion Model for Single or Sparse-view 3D Object Reconstruction**|本文提出了一种用于3D对象重建的神经结构MVDiffusion++，该结构在给定一张或几张没有相机姿势的图像的情况下合成对象的密集和高分辨率视图。MVDiffusion++通过两个令人惊讶的简单想法实现了卓越的灵活性和可扩展性：1）“无姿势架构”，其中2D潜在特征之间的标准自关注在任意数量的条件视图和生成视图中学习3D一致性，而无需显式使用相机姿势信息；和2）一种“视图丢弃策略”，在训练期间丢弃大量输出视图，这减少了训练时间内存占用，并在测试时实现了密集和高分辨率的视图合成。我们使用Ob厌恶对象进行训练，使用谷歌扫描对象进行评估，并使用标准的新视图合成和3D重建指标，其中MVDiffusion++显著优于当前的技术状态。我们还通过将MVDiffusion++与文本到图像生成模型相结合，展示了一个文本到3D应用程序示例。 et.al.|[2402.12712](http://arxiv.org/abs/2402.12712)|null|
|**2024-02-19**|**Real-time 3D Semantic Scene Perception for Egocentric Robots with Binocular Vision**|在室内移动时感知具有多个对象的三维（3D）场景对于基于视觉的移动机器人至关重要，尤其是对于增强其操作任务而言。在这项工作中，我们为具有双目视觉的以自我为中心的机器人提出了一种具有实例分割、特征匹配和点集配准的端到端流水线，并通过所提出的流水线展示了机器人的抓取能力。首先，我们设计了一种用于单视图3D语义场景分割的基于RGB图像的分割方法，利用2D数据集中的常见对象类，通过相应的深度图将3D点封装到对象实例的点云中。接下来，基于来自先前步骤的RGB图像中的感兴趣对象之间的匹配关键点来提取两个连续分割的点云的3D对应关系。此外，为了了解3D特征分布的空间变化，我们还使用核密度估计（KDE）基于估计的分布对每个3D点对进行加权，这随后在解决点云之间的刚性变换的同时，提供了具有较少中心对应性的鲁棒性。最后，我们在安装了Intel RealSense D435i RGB-D相机的7自由度双臂Baxter机器人上测试了我们提出的管道。结果表明，我们的机器人可以分割感兴趣的对象，在移动时配准多个视图，并抓住目标对象。源代码位于https://github.com/mkhangg/semantic_scene_perception. et.al.|[2402.11872](http://arxiv.org/abs/2402.11872)|null|
|**2024-02-18**|**A Robust Error-Resistant View Selection Method for 3D Reconstruction**|为了解决在运动结构（SFM）视图选择中选择具有小相机基线的视图导致三角测量不确定性增加的问题，本文提出了一种稳健的抗误差视图选择方法。该方法利用基于三角测量的计算来获得抗误差模型，然后用于构建抗误差矩阵。抗误差矩阵中每行的排序结果确定每个视图的候选视图集。通过遍历所有视图的候选视图集，并基于容错矩阵完成缺失的视图，确保了三维重建的完整性。根据重建结果中的平均重投影误差和绝对轨迹误差，将该方法与COLMAP程序中精度最高的穷举方法进行了实验比较。所提出的方法在TUM数据集和DTU数据集上的重投影误差精度平均降低了29.40%，绝对轨迹误差平均降低了5.07%。 et.al.|[2402.11431](http://arxiv.org/abs/2402.11431)|null|
|**2024-02-17**|**Dense Matchers for Dense Tracking**|光流是各种应用的有用输入，包括3D重建、姿态估计、跟踪和运动结构。尽管它很有用，但密集的长期跟踪领域，特别是在宽基线上，尚未得到广泛探索。本文扩展了MFT提出的在对数间隔上组合多个光流的概念。我们展示了MFT与不同光流网络的兼容性，产生的结果超过了它们各自的性能。此外，我们在MFT框架内提出了这些网络的简单而有效的组合。在位置预测精度方面，这种方法被证明与更复杂的非因果方法具有竞争力，突出了MFT在增强长期跟踪应用方面的潜力。 et.al.|[2402.11287](http://arxiv.org/abs/2402.11287)|null|
|**2024-02-17**|**DiffPoint: Single and Multi-view Point Cloud Reconstruction with ViT Based Diffusion Model**|随着二维到三维重建的任务在各种现实场景中获得了极大的关注，能够生成高质量的点云变得至关重要。尽管最近深度学习模型在生成点云方面取得了成功，但由于图像和点云之间的差异，在生成高保真度结果方面仍然存在挑战。虽然视觉变换器（ViT）和扩散模型在各种视觉任务中都显示出了前景，但它们在从图像重建点云方面的优势尚未得到证明。在本文中，我们首先提出了一种称为DiffPoint的简洁而强大的架构，该架构将ViT和扩散模型相结合，用于点云重建任务。在每个扩散步骤，我们将有噪声的点云划分为不规则的斑块。然后，使用将所有输入视为标记（包括时间信息、图像嵌入和噪声补丁）的标准ViT主干，我们训练我们的模型以基于输入图像预测目标点。我们在单视图和多视图重建任务上对DiffPoint进行了评估，并取得了最先进的结果。此外，我们还引入了一个统一灵活的特征融合模块，用于聚合来自单个或多个输入图像的图像特征。此外，我们的工作证明了跨语言和图像应用统一架构以改进3D重建任务的可行性。 et.al.|[2402.11241](http://arxiv.org/abs/2402.11241)|null|
|**2024-02-15**|**Evaluating NeRFs for 3D Plant Geometry Reconstruction in Field Conditions**|我们评估了不同的神经辐射场（NeRF）技术，用于在从室内环境到室外环境的不同环境中重建（3D）植物。传统技术往往难以捕捉植物的复杂细节，这对植物学和农业理解至关重要。我们评估了三种日益复杂的场景，并将结果与使用激光雷达作为地面实况数据获得的点云进行了比较。在最现实的现场场景中，NeRF模型在GPU上进行30分钟的训练，获得了74.65%的F1成绩，突出了NeRF在具有挑战性的环境中的效率和准确性。这些发现不仅证明了NeRF在详细逼真的3D植物建模中的潜力，而且为提高3D重建过程的速度和效率提供了实用的方法。 et.al.|[2402.10344](http://arxiv.org/abs/2402.10344)|null|
|**2024-02-15**|**GES: Generalized Exponential Splatting for Efficient Radiance Field Rendering**|3D高斯散射的进步显著加速了3D重建和生成。然而，它可能需要大量的高斯，这会产生大量的内存占用。本文介绍了GES（Generalized Exponential Splatting），这是一种利用广义指数函数（GEF）对3D场景进行建模的新表示，需要更少的粒子来表示场景，因此在效率上显著优于高斯飞溅方法，并具有基于高斯的实用程序的即插即用替换能力。GES在原理性1D设置和逼真的3D场景中都得到了理论和实证验证。它被证明可以更准确地表示具有尖锐边缘的信号，由于其固有的低通特性，这对高斯人来说通常是具有挑战性的。我们的实证分析表明，GEF在拟合自然发生的信号（如正方形、三角形和抛物线信号）方面优于高斯，从而减少了对增加高斯飞溅的内存占用的广泛拆分操作的需要。借助调频损耗，GES在新的视图合成基准中实现了有竞争力的性能，同时所需的内存存储量不到高斯飞溅的一半，并将渲染速度提高了39%。代码可在项目网站上获得https://abdullahamdi.com/ges . et.al.|[2402.10128](http://arxiv.org/abs/2402.10128)|null|
|**2024-02-14**|**PC-NeRF: Parent-Child Neural Radiance Fields Using Sparse LiDAR Frames in Autonomous Driving Environments**|大规模的3D场景重建和新颖的视图合成对于自动驾驶汽车至关重要，尤其是利用时间稀疏的激光雷达帧。然而，传统的显式表示仍然是以无限分辨率表示重建和合成场景的一个重要瓶颈。尽管最近开发的神经辐射场（NeRF）在隐式表示中显示出令人信服的结果，但使用稀疏激光雷达帧进行大规模3D场景重建和新的视图合成的问题仍未得到探索。为了弥补这一差距，我们提出了一种3D场景重建和新的视图合成框架，称为父子神经辐射场（PC NeRF）。该框架基于父NeRF和子NeRF两个模块，实现了分层空间划分和多级场景表示，包括场景、分段和点级别。多级场景表示增强了稀疏激光雷达点云数据的有效利用，并能够快速获取近似体积场景表示。经过大量实验，PC NeRF被证明可以在大规模场景中实现高精度的新型激光雷达视图合成和三维重建。此外，PC NeRF可以有效地处理稀疏激光雷达帧的情况，并在有限的训练时期内表现出较高的部署效率。我们的方法实施和预先培训的模型可在https://github.com/biter0088/pc-nerf. et.al.|[2402.09325](http://arxiv.org/abs/2402.09325)|**[link](https://github.com/biter0088/pc-nerf)**|
|**2024-02-14**|**DUDF: Differentiable Unsigned Distance Fields with Hyperbolic Scaling**|近年来，人们对训练神经网络来近似无符号距离场（UDF）越来越感兴趣，以在3D重建的背景下表示开放表面。然而，UDF在零水平集上是不可微的，这导致距离和梯度的显著误差，通常导致碎片和不连续的表面。在本文中，我们提出学习无符号距离场的双曲标度，它定义了一个具有不同边界条件的新Eikonal问题。这使得我们的公式能够与最先进的连续可微隐式神经表示网络无缝集成，该网络在文献中广泛应用于表示有符号距离场。我们的方法不仅解决了开放曲面表示的挑战，而且在重建质量和训练性能方面也有显著提高。此外，未锁定字段的可微性允许准确计算基本拓扑属性，如法线方向和曲率，这些属性普遍存在于渲染等下游任务中。通过广泛的实验，我们在各种数据集和竞争基线中验证了我们的方法。结果表明，与以前的方法相比，精度提高，速度提高了一个数量级。 et.al.|[2402.08876](http://arxiv.org/abs/2402.08876)|null|
|**2024-02-13**|**IM-3D: Iterative Multiview Diffusion and Reconstruction for High-Quality 3D Generation**|大多数文本到3D生成器建立在现成的基于数十亿图像训练的文本到图像模型之上。他们使用分数蒸馏采样（SDS）的变体，这是缓慢的，有点不稳定，并且容易出现伪影。一种缓解措施是将2D生成器微调为多视图感知，这可以帮助提取或与重建网络相结合，直接输出3D对象。在本文中，我们进一步探索了文本到三维模型的设计空间。通过考虑视频而不是图像生成器，我们显著改进了多视图生成。结合3D重建算法，通过使用高斯飞溅，可以优化基于图像的鲁棒损失，我们直接从生成的视图中产生高质量的3D输出。我们的新方法IM-3D将2D生成器网络的评估次数减少了10-100x，从而实现了更高效的管道、更好的质量、更少的几何不一致性和更高的可用3D资产收益率。 et.al.|[2402.08682](http://arxiv.org/abs/2402.08682)|null|

<p align=right>(<a href=#updated-on-20240221>back to top</a>)</p>

## Diffusion

|Publish Date|Title|Abstract|PDF|Code|
|---|---|---|---|---|
|**2024-02-20**|**Nonequilibrium fluctuations of chemical reaction networks at criticality: The Schlögl model as paradigmatic case**|化学反应网络可以在外部控制参数（如物种的化学势）变化时发生非平衡相变。我们研究了相关恒化器中的通量，该通量与Schl模型中的熵产生及其临界波动成正比。数值模拟表明，相应的扩散系数在临界点处作为系统大小的函数而发散。在临界点附近，扩散系数遵循标度形式。我们开发了一种基于化学Langevin方程和van Kampen系统尺寸展开的分析方法，该方法在单稳态状态下产生相应的指数。在双稳态状态下，我们依靠两态近似来分析描述临界行为。 et.al.|[2402.13168](http://arxiv.org/abs/2402.13168)|null|
|**2024-02-20**|**Neural Network Diffusion**|扩散模型在图像和视频生成方面取得了显著的成功。在这项工作中，我们证明了扩散模型也可以生成高性能的神经网络参数。我们的方法很简单，利用了一个自动编码器和一个标准的潜在扩散模型。自动编码器提取训练的网络参数的子集的潜在表示。然后训练扩散模型以从随机噪声中合成这些潜在参数表示。然后，它生成新的表示，这些表示通过自动编码器的解码器，解码器的输出可以用作网络参数的新子集。在各种架构和数据集中，我们的扩散过程一致地生成与经过训练的网络具有可比或改进性能的模型，而额外成本最低。值得注意的是，我们根据经验发现，生成的模型与训练的网络表现不同。我们的研究结果鼓励对扩散模型的多用途进行更多的探索。 et.al.|[2402.13144](http://arxiv.org/abs/2402.13144)|**[link](https://github.com/nus-hpc-ai-lab/neural-network-diffusion)**|
|**2024-02-20**|**Ultrafast lattice disordering can be accelerated by electronic collisional forces**|在超快结构相变的普遍情况下，原子运动发生在由快电子绝热决定的缓慢变化的势能面上。然而，这忽略了由电子-晶格碰撞引起的非保守力，这些力可以显著影响原子运动。大多数超快技术只探测平均结构，对随机位移不太敏感，因此无法探测非保守力在相变中所起的作用。在这里，我们证明了VO2的原型绝缘体到金属转变的晶格动力学不能仅用势能来描述。我们使用样品温度来控制在跨越相变的超快光激发之前预先存在的晶格无序，并且我们的超快扩散散射实验表明，在100K和300K的初始温度下，金红石金属的波动特性发展得同样快（120fs）。这表明额外的非保守力是导致晶格无序增加的原因。这些结果强调了需要对Born-Oppenheimer近似之外的超快现象进行更复杂的描述，以及对衍射测量的平均晶胞之外的空间波动进行超快探测。 et.al.|[2402.13133](http://arxiv.org/abs/2402.13133)|null|
|**2024-02-20**|**How accurate are simulations and experiments for the lattice energies of molecular crystals?**|分子晶体在包括制药和有机半导体器件在内的广泛科学领域发挥着核心作用。然而，由于分子间相互作用（如氢键和范德华分散力）的微妙相互作用，它们很难用计算方法准确建模。在这里，通过利用最近的算法发展，我们报道了流行且广泛使用的X23数据集中所有23种分子晶体的第一组扩散蒙特卡罗晶格能。与之前最先进的晶格能预测（在数据集的一个子集上）的比较和对实验升华焓的仔细分析表明，高精度计算方法现在至少与分子晶体晶格能的（计算推导的）实验一样可靠。总的来说，这项工作证明了高级显式相关电子结构方法在复杂凝聚相系统中进行广泛基准研究的可行性，并为实验和模拟之间更紧密的一致性指明了道路。 et.al.|[2402.13059](http://arxiv.org/abs/2402.13059)|null|
|**2024-02-20**|**Excited state-specific CASSCF theory for the torsion of ethylene**|状态特异性完全活性空间自洽场（SS-CASSCF）理论已成为准确预测远离分子平衡的电子激发能表面的一条很有前途的途径。然而，其对光化学感兴趣的化学系统的准确性和实用性尚未完全确定。我们研究了SS-CASSCF理论在乙烯双键旋转中的低洼基态和激发态的性能。我们表明，具有最小（2e，2o）活性空间的特定状态近似提供了与具有更大活性空间的状态平均计算相当的精度，同时优化每个激发态的轨道显著提高了波函数的空间扩散率。然而，价态和里德堡激发中不平衡的后CASSCF动态相关性，或非扩散基集的使用，导致激发态解聚结并消失，在势能面中产生非物理不连续性。我们的发现突出了必须克服的理论挑战，以实现特定状态电子结构理论在计算光化学中的实际应用。 et.al.|[2402.13046](http://arxiv.org/abs/2402.13046)|null|
|**2024-02-20**|**Text-Guided Molecule Generation with Diffusion Language Model**|文本引导的分子生成是一项生成分子以匹配特定文本描述的任务。最近，大多数现有的基于SMILES的分子生成方法都依赖于自回归结构。在这项工作中，我们提出了具有扩散语言模型的文本引导分子生成（TGM-DLM），这是一种利用扩散模型来解决自回归方法局限性的新方法。TGM-DLM使用两阶段扩散生成过程，集体迭代地更新SMILES字符串中的令牌嵌入。第一阶段在文本描述的指导下优化来自随机噪声的嵌入，而第二阶段校正无效的SMILES字符串以形成有效的分子表示。我们证明了TGM-DLM在不需要额外数据资源的情况下优于自回归模型MolT5-Base。我们的发现强调了TGM-DLM在产生具有特定性质的相干和精确分子方面的显著有效性，为药物发现和相关科学领域开辟了新的途径。代码将在以下位置发布：https://github.com/Deno-V/tgm-dlm. et.al.|[2402.13040](http://arxiv.org/abs/2402.13040)|**[link](https://github.com/deno-v/tgm-dlm)**|
|**2024-02-20**|**The Anomalous Long-Ranged Influence of an Inclusion in Momentum-Conserving Active Fluids**|我们发现，放置在微游泳运动员的稀释斯托克斯悬浮液中的夹杂物会引起幂律数密度调制和流动。根据夹杂物是通过外力（例如光学镊子）固定还是自由，它们采取不同的形式。当包裹体保持在适当位置时，远场流体流动为Stokeslet，而微游泳密度衰减为 $1/r^｛2+\ε｝$，$r$为与包裹体的距离，$\ε$是一种异常指数，它取决于夹杂物的对称性，并作为表征对流和扩散效应相对振幅的无量纲数的函数连续变化。角度相关性采用了一种非平凡的形式，它取决于相同的无量纲数。当夹杂物自由移动时，远场流体流动是一个小应力，微流体密度衰减为$1/r^2$ ，具有简单的角度依赖性。这些长程调节介导了我们所表征的夹杂物之间的长程相互作用。 et.al.|[2402.12996](http://arxiv.org/abs/2402.12996)|null|
|**2024-02-20**|**Visual Style Prompting with Swapping Self-Attention**|在文本到图像生成的不断发展的领域中，扩散模型已成为内容创建的强大工具。尽管现有模型具有非凡的能力，但在以一致的风格实现受控生成方面仍然面临挑战，需要昂贵的微调，或者由于内容泄露而导致视觉元素的传输不足。为了应对这些挑战，我们提出了一种新颖的方法，即我们的方法，在保持特定风格元素和细微差别的同时，制作各种各样的图像。在去噪过程中，我们保持原始特征的查询，同时在后期自注意层中与参考特征的查询交换关键字和值。这种方法允许在没有任何微调的情况下进行视觉风格提示，确保生成的图像保持忠实的风格。通过对各种风格和文本提示的广泛评估，我们的方法显示出优于现有方法的优势，最好地反映了参考文献的风格，并确保生成的图像与文本提示最准确地匹配。我们的项目页面可用\ href{https://curryjung.github.io/VisualStylePrompt/在这里 et.al.|[2402.12974](http://arxiv.org/abs/2402.12974)|null|
|**2024-02-20**|**CLIPping the Deception: Adapting Vision-Language Models for Universal Deepfake Detection**|生成对抗性网络（GANs）的最新进展和扩散模型的出现大大简化了高度逼真和可广泛访问的合成内容的生产。因此，迫切需要有效的通用检测机制来减轻deepfakes带来的潜在风险。在本文中，我们探讨了预训练的视觉语言模型（VLM）与最新的通用深度伪造检测自适应方法相结合的有效性。根据之前在该领域的研究，我们仅使用单个数据集（ProGAN）来调整CLIP用于深度伪造检测。然而，与之前的研究不同，以前的研究只依赖CLIP的视觉部分而忽略其文本成分，我们的分析表明，保留文本部分至关重要。因此，我们使用的简单而轻量级的基于提示调整的自适应策略比以前的SOTA方法高出5.01%mAP和6.61%的准确率，同时使用了不到三分之一的训练数据（与720k相比，200k张图像）。为了评估我们提出的模型在现实世界中的适用性，我们对各种场景进行了全面评估。这涉及对来自21个不同数据集的图像进行严格测试，包括基于GAN、基于扩散和商业工具生成的图像。 et.al.|[2402.12927](http://arxiv.org/abs/2402.12927)|null|
|**2024-02-20**|**RealCompo: Dynamic Equilibrium between Realism and Compositionality Improves Text-to-Image Diffusion Models**|扩散模型在文本到图像生成方面取得了显著的进步。然而，现有的模型在面临多对象合成生成时仍然存在许多困难。在本文中，我们提出了一种新的无训练且传输友好的文本到图像生成框架，即RealCompo，旨在利用文本到图像和布局到图像模型的优势，增强生成图像的真实性和合成性。提出了一种直观新颖的均衡器，在去噪过程中动态平衡两个模型的强度，允许在没有额外训练的情况下即插即用地使用任何模型。大量实验表明，我们的RealCompo在多对象合成生成中始终优于最先进的文本到图像模型和布局到图像模型，同时保持生成图像的令人满意的真实性和合成性。代码位于https://github.com/YangLing0818/RealCompo et.al.|[2402.12908](http://arxiv.org/abs/2402.12908)|**[link](https://github.com/yangling0818/realcompo)**|

<p align=right>(<a href=#updated-on-20240221>back to top</a>)</p>

## NeRF

|Publish Date|Title|Abstract|PDF|Code|
|---|---|---|---|---|
|**2024-02-18**|**Pattern Recognition Facilities of Extended Kalman Filtering in Stochastic Neural Fields**|在数学神经科学中，人们特别关注在存在模型不确定性的情况下，由动态神经场（DNF）建模的神经组织中的工作记忆机制。工作记忆设施意味着，由于网络中反复的相互作用，在去除外部刺激后，神经元的活动保持自我维持，并允许系统处理丢失的传感器信息。在我们之前的工作中，我们已经根据传感器提供的不完整数据开发了两种神经膜电位的重建方法。这些方法是在扩展卡尔曼滤波方法中通过使用Euler Maruyama方法和\^{o}-Taylor订单1.5的扩展。它表明\^{o}-Taylor基于EKF的恢复过程比基于Euler Maruyama的替代方案更准确。在传感器信息不完整的情况下，它提高了膜电位重建的质量。本文的目的是研究它们的模式识别功能，即在模型不确定和信息不完整的情况下，模式形成重建的质量。数值实验是以神经组织中出现多个活动区的随机DNF为例提供的。 et.al.|[2402.11551](http://arxiv.org/abs/2402.11551)|null|
|**2024-02-15**|**Reg-NF: Efficient Registration of Implicit Surfaces within Neural Fields**|神经场，即基于坐标的神经网络，最近因隐含地表示场景而广受欢迎。与基于点云等显式表示的经典方法相比，神经场提供了连续的场景表示，能够以紧凑且理想的机器人应用方式表示3D几何结构和外观。然而，有限的现有方法已经研究了通过直接利用这些连续的隐式表示来配准多个神经场。在本文中，我们提出了Reg-NF，这是一种基于神经场的配准，它优化了两个任意神经场之间的相对6-DoF变换，即使这两个场具有不同的比例因子。Reg NF的关键组成部分包括双向配准损失、多视图表面采样和体积符号距离函数（SDF）的利用。我们在一个新的神经场数据集上展示了我们的方法，用于评估配准问题。我们提供了一组详尽的实验和消融研究，以确定我们的方法的性能，同时也讨论了局限性，为研究界在无约束环境中利用神经场的开放挑战提供了未来的方向。 et.al.|[2402.09722](http://arxiv.org/abs/2402.09722)|null|
|**2024-02-12**|**Unsupervised Discovery of Object-Centric Neural Fields**|我们研究从单个图像中推断3D以对象为中心的场景表示。虽然最近的方法在从简单的合成图像中无监督地发现3D对象方面显示出了潜力，但它们未能推广到具有视觉丰富和多样化对象的真实世界场景。这种限制源于它们的对象表示，它将对象的内在属性（如形状和外观）与外在的、以观察者为中心的属性（如3D位置）纠缠在一起。为了解决这一瓶颈，我们提出了以对象为中心的神经场的无监督发现（uOCF）。uOCF专注于学习对象的内在，并分别对外在进行建模。我们的方法显著提高了系统泛化能力，从而能够从稀疏的真实世界图像中无监督地学习高保真的以对象为中心的场景表示。为了评估我们的方法，我们收集了三个新的数据集，包括两个真实的厨房环境。大量实验表明，uOCF能够在无监督的情况下从单个真实图像中发现视觉丰富的对象，从而实现3D对象分割和场景操作等应用。值得注意的是，uOCF演示了对单个真实图像中看不见的物体的零样本泛化。项目页面：https://red-fairy.github.io/uOCF/ et.al.|[2402.07376](http://arxiv.org/abs/2402.07376)|null|
|**2024-02-06**|**Improved Generalization of Weight Space Networks via Augmentations**|在深度权重空间（DWS）中学习，神经网络处理其他神经网络的权重，是一个新兴的研究方向，应用于2D和3D神经领域（INRs、NeRFs），以及对其他类型的神经网络进行推断。不幸的是，权重空间模型往往存在严重的过拟合问题。我们实证分析了这种过拟合的原因，发现一个关键原因是DWS数据集缺乏多样性。虽然给定的对象可以用许多不同的权重配置来表示，但典型的INR训练集无法捕捉表示同一对象的INR之间的可变性。为了解决这一问题，我们探索了在权重空间中增加数据的策略，并提出了一种适用于权重空间的MixUp方法。我们在两个设置中展示了这些方法的有效性。在分类方面，它们可以提高性能，类似于拥有10倍以上的数据。在自我监督的对比学习中，它们在下游分类中产生了5-10%的显著收益。 et.al.|[2402.04081](http://arxiv.org/abs/2402.04081)|null|
|**2024-01-31**|**BlockFusion: Expandable 3D Scene Generation using Latent Tri-plane Extrapolation**|我们介绍了BlockFusion，这是一种基于扩散的模型，它将3D场景生成为单元块，并无缝地合并新的块来扩展场景。BlockFusion使用从完整的3D场景网格中随机裁剪的3D块的数据集进行训练。通过逐块拟合，所有训练块都被转换为混合神经场：具有包含几何特征的三平面，然后是用于解码有符号距离值的多层感知器（MLP）。采用变分自动编码器将三平面压缩到潜在的三平面空间中，在该空间上进行去噪扩散处理。应用于潜在表示的扩散允许高质量和多样化的3D场景生成。要在生成过程中扩展场景，只需附加空块以与当前场景重叠，并外推现有的潜在三平面以填充新块。外推是通过在去噪迭代过程中使用来自重叠三平面的特征样本来调节生成过程来完成的。潜在的三平面外推法产生语义和几何上有意义的过渡，与现有场景和谐融合。2D布局调节机制用于控制场景元素的放置和布置。实验结果表明，BlockFusion能够在室内和室外场景中生成具有前所未有的高质量形状的多样化、几何一致和无边界的大型3D场景。 et.al.|[2401.17053](http://arxiv.org/abs/2401.17053)|null|
|**2024-01-26**|**Learning Neural Radiance Fields of Forest Structure for Scalable and Fine Monitoring**|这项工作利用神经辐射场和遥感技术用于林业应用。在这里，我们展示了神经辐射场为改进森林监测中现有的遥感方法提供了广泛的可能性。我们提出的实验证明了它们的潜力：（1）表达森林三维结构的精细特征，（2）融合可用的遥感模式，（3）改进三维结构衍生的森林指标。总之，这些特性使神经场成为一种有吸引力的计算工具，具有进一步提高森林监测程序的可扩展性和准确性的巨大潜力。 et.al.|[2401.15029](http://arxiv.org/abs/2401.15029)|null|
|**2024-01-25**|**Learning Robust Generalizable Radiance Field with Visibility and Feature Augmented Point Representation**|本文介绍了广义神经辐射场（NeRF）的一种新范式。以前的通用NeRF方法将多视点立体技术与基于图像的神经渲染相结合进行泛化，产生了令人印象深刻的结果，同时存在三个问题。首先，遮挡常常导致不一致的特征匹配。然后，由于采样点和粗略特征聚合的单独过程，它们在几何不连续性和局部尖锐形状中传递失真和伪影。第三，当源视图离目标视图不够近时，它们基于图像的表示会发生严重退化。为了应对挑战，我们提出了第一个基于点而不是基于图像的渲染构建可泛化神经场的范式，我们称之为可泛化神经点场（GPF）。我们的方法通过几何先验显式地建模可见性，并用神经特征增强它们。我们提出了一种新的非均匀对数采样策略，以提高渲染速度和重建质量。此外，我们提出了一种可学习的内核，该内核在空间上增加了用于特征聚合的特征，减轻了几何结构急剧变化的地方的失真。此外，我们的表现很容易被操纵。实验表明，在泛化和微调设置中，我们的模型可以在三个数据集上提供比所有对应模型和基准更好的几何结构、视图一致性和渲染质量，初步证明了可泛化NeRF新范式的潜力。 et.al.|[2401.14354](http://arxiv.org/abs/2401.14354)|null|
|**2024-01-24**|**Unified neural field theory of brain dynamics underlying oscillations in Parkinson's disease and generalized epilepsies**|通过皮质丘脑基底神经节（CTBG）系统的神经场模型，联合探讨了帕金森病（PD）和全身性癫痫的病理同步神经振荡的机制。基底神经节（BG）被近似为一个单一的有效群体，并分析了它们在调节振荡皮质丘脑（CT）动力学中的作用，反之亦然。除了正常的脑电图节律外，模型中还存在4 Hz和20 Hz左右的增强活动，这与PD的特征频率一致。这些节律是由BG和CT人群之间回路中的共振引起的，类似于先前CT模型中潜在的癫痫振荡。多巴胺耗竭被认为削弱了对PD中这些共振的抑制，网络连接解释了在4-8Hz和20Hz左右BG、丘脑和皮层活动之间的显著一致性。丘脑网状核（TRN）和BG的传入和传出连接位点之间的相似性预测低多巴胺对应于强直-阵挛（大发作）癫痫发作的可能性降低，这与实验结果一致。此外，该模型预测，与实验结果相匹配的低多巴胺水平会增加缺席（轻微）癫痫发作的可能性。与其他CTBG建模研究一致，当传入和传出BG与CT系统的连接增强时，表现出对缺席发作活动的抑制。BG被证明在强直-阵挛发作状态附近抑制CTBG系统的活性，从而深入了解BG回路中目前治疗的疗效。TRN的睡眠状态也被发现可以抑制病理性PD活动匹配观察。总的来说，这些发现证明了广泛性癫痫和帕金森病的相干振荡之间有很强的相似性，并为可能的合并症提供了见解。 et.al.|[2401.13467](http://arxiv.org/abs/2401.13467)|null|
|**2024-01-17**|**Reproducibility via neural fields of visual illusions induced by localized stimuli**|本文研究了Billock和Tsou[PNAS，2007]使用Amari型神经场的可控性对初级视皮层（V1）皮层活动进行建模的实验复制，重点关注中央凹或外周视野中的规则漏斗模式。其目的是理解和模拟在这些实验中观察到的视觉现象，强调其非线性性质。这项研究包括设计模拟Billock和Tsou实验中视觉刺激的感官输入。然后从理论和数值上研究这些输入引起的后图像，以确定它们复制实验观察到的视觉效果的能力。这项研究的一个关键方面是研究神经反应的非线性性质所引起的影响。特别是，通过强调兴奋性和抑制性神经元在某些视觉现象出现中的重要性，这项研究表明，这两种类型的神经元活动的相互作用在视觉过程中发挥着重要作用，挑战了后者主要由兴奋性活动单独驱动的假设。 et.al.|[2401.09108](http://arxiv.org/abs/2401.09108)|null|
|**2024-01-12**|**Motion2VecSets: 4D Latent Vector Set Diffusion for Non-rigid Shape Reconstruction and Tracking**|我们介绍了Motion2VecSets，这是一种用于从点云序列进行动态曲面重建的4D扩散模型。虽然现有的最先进的方法已经证明在使用神经场表示重建非刚性对象方面取得了成功，但传统的前馈网络遇到了来自噪声、部分或稀疏点云的模糊观测的挑战。为了应对这些挑战，我们引入了一种扩散模型，该模型通过压缩潜在表示的迭代去噪过程来显式学习非刚性对象的形状和运动分布。当处理模糊输入时，基于扩散的先验能够进行更合理和概率的重建。我们用潜在向量集参数化4D动力学，而不是使用全局潜在。这种新颖的4D表示使我们能够学习局部表面形状和变形模式，从而实现更准确的非线性运动捕捉，并显著提高对看不见的运动和身份的可推广性。对于更具时间连贯性的目标跟踪，我们同步地对变形潜集进行去噪，并在多个帧之间交换信息。为了避免计算开销，我们设计了一个交错的空间和时间注意力块，以沿着空间和时间域交替聚集变形潜伏期。与最先进的方法进行了广泛的比较，证明了我们的Motion2VenSets在从各种不完美的观测进行4D重建方面的优势，特别是在从DeformingThings4D Animals数据集上的稀疏点云重建看不见的个体方面，与CaDex相比，交集优于并集（IoU）提高了19%。更多详细信息，请访问https://vveicao.github.io/projects/Motion2VecSets/. et.al.|[2401.06614](http://arxiv.org/abs/2401.06614)|null|

<p align=right>(<a href=#updated-on-20240221>back to top</a>)</p>

[contributors-shield]: https://img.shields.io/github/contributors/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[contributors-url]: https://github.com/Vincentqyw/cv-arxiv-daily/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[forks-url]: https://github.com/Vincentqyw/cv-arxiv-daily/network/members
[stars-shield]: https://img.shields.io/github/stars/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[stars-url]: https://github.com/Vincentqyw/cv-arxiv-daily/stargazers
[issues-shield]: https://img.shields.io/github/issues/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[issues-url]: https://github.com/Vincentqyw/cv-arxiv-daily/issues

