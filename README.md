[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]

## Updated on 2024.02.20
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
|**2024-02-15**|**GES: Generalized Exponential Splatting for Efficient Radiance Field Rendering**|3D高斯散射的进步显著加速了3D重建和生成。然而，它可能需要大量的高斯，这会产生大量的内存占用。本文介绍了GES（Generalized Exponential Splatting），这是一种利用广义指数函数（GEF）对3D场景进行建模的新表示，需要更少的粒子来表示场景，因此在效率上显著优于高斯飞溅方法，并具有基于高斯的实用程序的即插即用替换能力。GES在原理性1D设置和逼真的3D场景中都得到了理论和实证验证。它被证明可以更准确地表示具有尖锐边缘的信号，由于其固有的低通特性，这对高斯人来说通常是具有挑战性的。我们的实证分析表明，GEF在拟合自然发生的信号（如正方形、三角形和抛物线信号）方面优于高斯，从而减少了对增加高斯飞溅的内存占用的广泛拆分操作的需要。借助调频损耗，GES在新的视图合成基准中实现了有竞争力的性能，同时所需的内存存储量不到高斯飞溅的一半，并将渲染速度提高了39%。代码可在项目网站上获得https://abdullahamdi.com/ges . et.al.|[2402.10128](http://arxiv.org/abs/2402.10128)|null|
|**2024-02-14**|**PC-NeRF: Parent-Child Neural Radiance Fields Using Sparse LiDAR Frames in Autonomous Driving Environments**|大规模的3D场景重建和新颖的视图合成对于自动驾驶汽车至关重要，尤其是利用时间稀疏的激光雷达帧。然而，传统的显式表示仍然是以无限分辨率表示重建和合成场景的一个重要瓶颈。尽管最近开发的神经辐射场（NeRF）在隐式表示中显示出令人信服的结果，但使用稀疏激光雷达帧进行大规模3D场景重建和新的视图合成的问题仍未得到探索。为了弥补这一差距，我们提出了一种3D场景重建和新的视图合成框架，称为父子神经辐射场（PC NeRF）。该框架基于父NeRF和子NeRF两个模块，实现了分层空间划分和多级场景表示，包括场景、分段和点级别。多级场景表示增强了稀疏激光雷达点云数据的有效利用，并能够快速获取近似体积场景表示。经过大量实验，PC NeRF被证明可以在大规模场景中实现高精度的新型激光雷达视图合成和三维重建。此外，PC NeRF可以有效地处理稀疏激光雷达帧的情况，并在有限的训练时期内表现出较高的部署效率。我们的方法实施和预先培训的模型可在https://github.com/biter0088/pc-nerf. et.al.|[2402.09325](http://arxiv.org/abs/2402.09325)|**[link](https://github.com/biter0088/pc-nerf)**|
|**2024-02-11**|**BioNeRF: Biologically Plausible Neural Radiance Fields for View Synthesis**|本文介绍了BioNeRF，这是一种生物学上合理的架构，它以3D表示对场景进行建模，并通过辐射场合成新的视图。由于NeRF依赖于网络权重来存储场景的三维表示，BioNeRF实现了一种受认知启发的机制，该机制将来自多个来源的输入融合到类似记忆的结构中，提高了存储容量，并提取了更多内在和相关的信息。BioNeRF还模拟了在锥体细胞中观察到的与上下文信息有关的行为，其中记忆作为上下文提供，并与两个后续神经模型的输入相结合，一个负责产生体积密度，另一个负责渲染场景所用的颜色。实验结果表明，BioNeRF在两个数据集（真实世界图像和合成数据）中对人类感知进行编码的质量测量方面优于最先进的结果。 et.al.|[2402.07310](http://arxiv.org/abs/2402.07310)|**[link](https://github.com/leandropassosjr/bionerf)**|
|**2024-02-11**|**3D Gaussian as a New Vision Era: A Survey**|3D高斯散射（3D-GS）已成为计算机图形学领域的一个重大进步，它提供了明确的场景表示和新颖的视图合成，而不依赖于神经网络，如神经辐射场（NeRF）。这项技术在机器人、城市地图、自主导航和虚拟现实/增强现实等领域有着不同的应用。鉴于三维高斯散射的日益流行和研究的不断扩展，本文对过去一年的相关论文进行了全面的综述。我们根据特征和应用对分类法进行了调查，介绍了3D高斯飞溅的理论基础。我们通过这项调查的目标是让新的研究人员熟悉3D高斯飞溅，为该领域的开创性工作提供宝贵的参考，并启发未来的研究方向，正如我们的结论部分所讨论的那样。 et.al.|[2402.07181](http://arxiv.org/abs/2402.07181)|null|
|**2024-02-09**|**NCRF: Neural Contact Radiance Fields for Free-Viewpoint Rendering of Hand-Object Interaction**|在三维计算机视觉中，建模手与物体的交互是一项具有根本挑战性的任务。尽管在该领域已经取得了显著的进展，但现有的方法仍然无法真实地合成手与物体的交互照片，因为手与物体之间的严重相互遮挡导致渲染质量下降，以及手与物体姿态估计不准确。为了应对这些挑战，我们提出了一种新的自由视点渲染框架，即神经接触辐射场（NCRF），以从稀疏的视频集重建手与物体的交互。特别地，所提出的NCRF框架由两个关键组件组成：（a）接触优化字段，该字段从3D查询点预测准确的接触字段，以实现手和物体之间的期望接触。（b） 手对象神经辐射场，用于学习静态规范空间中的隐含手对象表示，与专门设计的手对象运动场相一致，以产生观察到的规范对应关系。我们共同学习这些关键组件，它们在视觉和几何约束下相互帮助和规则化，产生高质量的手对象重建，实现照片逼真的新颖视图合成。在HO3D和DexYCB数据集上进行的大量实验表明，我们的方法在渲染质量和姿态估计精度方面都优于当前最先进的方法。 et.al.|[2402.05532](http://arxiv.org/abs/2402.05532)|null|
|**2024-02-07**|**SPAD : Spatially Aware Multiview Diffusers**|我们提出了SPAD，这是一种从文本提示或单个图像创建一致多视图图像的新方法。为了实现多视图生成，我们通过扩展具有跨视图交互的自注意层来重新调整预训练的2D扩散模型的用途，并在Ob厌恶的高质量子集上对其进行微调。我们发现，先前工作中提出的自我关注的天真扩展（例如MVDream）会导致视图之间的内容复制。因此，我们明确地限制了基于核极几何的跨视图注意力。为了进一步增强3D一致性，我们利用从相机射线导出的Plucker坐标，并将其作为位置编码注入。这使得SPAD能够对3D井中的空间接近度进行推理。与最近只能在固定方位角和仰角下生成视图的工作不同，SPAD提供了完整的相机控制，并在Ob厌恶和谷歌扫描对象数据集中对看不见的对象进行新的视图合成方面取得了最先进的结果。最后，我们证明了使用SPAD的文本到3D生成可以防止多面Janus问题。更多详细信息，请访问我们的网页：https://yashkant.github.io/spad et.al.|[2402.05235](http://arxiv.org/abs/2402.05235)|null|
|**2024-02-06**|**EscherNet: A Generative Model for Scalable View Synthesis**|我们介绍了EscherNet，一个用于视图合成的多视图条件扩散模型。EscherNet学习隐含的和生成的3D表示，再加上专门的相机位置编码，允许对任意数量的参考视图和目标视图之间的相机变换进行精确和连续的相对控制。EscherNet在视图合成方面提供了非凡的通用性、灵活性和可扩展性——尽管它使用固定数量的3个参考视图到3个目标视图进行训练，但它可以在单个消费级GPU上同时生成100多个一致的目标视图。因此，EscherNet不仅解决了零样本新视图合成问题，而且自然地将单图像和多图像3D重建相结合，将这些不同的任务组合成一个单一的、有凝聚力的框架。我们的大量实验表明，EscherNet在多个基准测试中实现了最先进的性能，即使与专门针对每个单独问题定制的方法相比也是如此。这种非凡的多功能性为设计用于3D视觉的可扩展神经结构开辟了新的方向。项目页面：\url{https://kxhit.github.io/EscherNet}. et.al.|[2402.03908](http://arxiv.org/abs/2402.03908)|null|
|**2024-02-06**|**Rig3DGS: Creating Controllable Portraits from Casual Monocular Videos**|从随意的智能手机视频中创建可控的3D人像是非常可取的，因为它们在AR/VR应用中具有巨大的价值。3D高斯散点（3DGS）的最新发展已经显示出在渲染质量和训练效率方面的改进。然而，要从单个视图捕捉中准确地建模和分解头部运动和面部表情，以实现高质量的渲染，仍然是一个挑战。在本文中，我们介绍了Rig3DGS来应对这一挑战。我们在规范空间中使用一组3D高斯表示整个场景，包括动态主体。使用一组控制信号，如头部姿势和表情，我们将它们转换到具有学习变形的3D空间，以生成所需的渲染。我们的关键创新是一种精心设计的变形方法，该方法以从3D可变形模型导出的可学习先验为指导。这种方法在训练中效率很高，在控制各种捕捉的面部表情、头部位置和视图合成方面也很有效。我们通过大量的定量和定性实验证明了我们所学变形的有效性。项目页面位于http://shahrukhathar.github.io/2024/02/05/Rig3DGS.html et.al.|[2402.03723](http://arxiv.org/abs/2402.03723)|null|
|**2024-02-05**|**Denoising Diffusion via Image-Based Rendering**|生成3D场景是一个具有挑战性的开放问题，需要合成在3D空间中完全一致的看似合理的内容。虽然最近的方法（如神经辐射场）擅长于视图合成和3D重建，但由于缺乏生成能力，它们无法在未观察到的区域合成看似合理的细节。相反，现有的生成方法通常无法重建野外的详细、大规模场景，因为它们使用有限容量的3D场景表示，需要对齐的相机姿势，或者依赖于额外的正则化子。在这项工作中，我们介绍了第一个能够快速、详细地重建和生成真实世界3D场景的扩散模型。为了实现这一目标，我们作出了三点贡献。首先，我们引入了一种新的神经场景表示，即IB平面，它可以有效而准确地表示大型3D场景，并根据需要动态分配更多的容量来捕捉每个图像中可见的细节。其次，我们提出了一种去噪扩散框架来学习这种新颖的3D场景表示的先验知识，仅使用2D图像，而不需要任何额外的监督信号，如掩模或深度。这支持在统一架构中进行3D重建和生成。第三，我们开发了一种原则性方法，通过放弃一些图像的表示，在将基于图像的渲染与扩散模型集成时避免琐碎的3D解决方案。我们在真实图像和合成图像的几个具有挑战性的数据集上评估了该模型，并展示了在生成、新视图合成和3D重建方面的卓越结果。 et.al.|[2402.03445](http://arxiv.org/abs/2402.03445)|null|
|**2024-02-07**|**4D Gaussian Splatting: Towards Efficient Novel View Synthesis for Dynamic Scenes**|我们考虑动态场景的新视图合成（NVS）问题。最近的神经方法已经为静态3D场景实现了异常的NVS结果，但对4D时变场景的扩展仍然是不平凡的。先前的工作通常通过学习规范空间加上隐式或显式变形场来编码动力学，这些变形场在突发运动或捕捉高保真渲染等具有挑战性的场景中很困难。在本文中，我们介绍了4D高斯散射（4DGS），这是一种用各向异性4D XYZT高斯表示动态场景的新方法，其灵感来自于3D高斯散射在静态场景中的成功。我们通过对4D高斯进行时间切片来对每个时间戳的动力学进行建模，4D高斯自然构成动态3D高斯，并可以无缝投影到图像中。作为一种明确的时空表示，4DGS展示了对复杂动力学和精细细节建模的强大能力，尤其是对于具有突然运动的场景。我们在高度优化的CUDA加速框架中进一步实现了我们的时间切片和飞溅技术，在RTX 3090 GPU上实现了高达277 FPS的实时推理渲染速度，在RTX4090 GPU上达到了583 FPS的实时推断渲染速度。对不同运动场景的严格评估显示了4DGS的卓越效率和有效性，它在数量和质量上都始终优于现有方法。 et.al.|[2402.03307](http://arxiv.org/abs/2402.03307)|null|

<p align=right>(<a href=#updated-on-20240220>back to top</a>)</p>

## 3D Reconstruction

|Publish Date|Title|Abstract|PDF|Code|
|---|---|---|---|---|
|**2024-02-15**|**Evaluating NeRFs for 3D Plant Geometry Reconstruction in Field Conditions**|我们评估了不同的神经辐射场（NeRF）技术，用于在从室内环境到室外环境的不同环境中重建（3D）植物。传统技术往往难以捕捉植物的复杂细节，这对植物学和农业理解至关重要。我们评估了三种日益复杂的场景，并将结果与使用激光雷达作为地面实况数据获得的点云进行了比较。在最现实的现场场景中，NeRF模型在GPU上进行30分钟的训练，获得了74.65%的F1成绩，突出了NeRF在具有挑战性的环境中的效率和准确性。这些发现不仅证明了NeRF在详细逼真的3D植物建模中的潜力，而且为提高3D重建过程的速度和效率提供了实用的方法。 et.al.|[2402.10344](http://arxiv.org/abs/2402.10344)|null|
|**2024-02-15**|**GES: Generalized Exponential Splatting for Efficient Radiance Field Rendering**|3D高斯散射的进步显著加速了3D重建和生成。然而，它可能需要大量的高斯，这会产生大量的内存占用。本文介绍了GES（Generalized Exponential Splatting），这是一种利用广义指数函数（GEF）对3D场景进行建模的新表示，需要更少的粒子来表示场景，因此在效率上显著优于高斯飞溅方法，并具有基于高斯的实用程序的即插即用替换能力。GES在原理性1D设置和逼真的3D场景中都得到了理论和实证验证。它被证明可以更准确地表示具有尖锐边缘的信号，由于其固有的低通特性，这对高斯人来说通常是具有挑战性的。我们的实证分析表明，GEF在拟合自然发生的信号（如正方形、三角形和抛物线信号）方面优于高斯，从而减少了对增加高斯飞溅的内存占用的广泛拆分操作的需要。借助调频损耗，GES在新的视图合成基准中实现了有竞争力的性能，同时所需的内存存储量不到高斯飞溅的一半，并将渲染速度提高了39%。代码可在项目网站上获得https://abdullahamdi.com/ges . et.al.|[2402.10128](http://arxiv.org/abs/2402.10128)|null|
|**2024-02-14**|**PC-NeRF: Parent-Child Neural Radiance Fields Using Sparse LiDAR Frames in Autonomous Driving Environments**|大规模的3D场景重建和新颖的视图合成对于自动驾驶汽车至关重要，尤其是利用时间稀疏的激光雷达帧。然而，传统的显式表示仍然是以无限分辨率表示重建和合成场景的一个重要瓶颈。尽管最近开发的神经辐射场（NeRF）在隐式表示中显示出令人信服的结果，但使用稀疏激光雷达帧进行大规模3D场景重建和新的视图合成的问题仍未得到探索。为了弥补这一差距，我们提出了一种3D场景重建和新的视图合成框架，称为父子神经辐射场（PC NeRF）。该框架基于父NeRF和子NeRF两个模块，实现了分层空间划分和多级场景表示，包括场景、分段和点级别。多级场景表示增强了稀疏激光雷达点云数据的有效利用，并能够快速获取近似体积场景表示。经过大量实验，PC NeRF被证明可以在大规模场景中实现高精度的新型激光雷达视图合成和三维重建。此外，PC NeRF可以有效地处理稀疏激光雷达帧的情况，并在有限的训练时期内表现出较高的部署效率。我们的方法实施和预先培训的模型可在https://github.com/biter0088/pc-nerf. et.al.|[2402.09325](http://arxiv.org/abs/2402.09325)|**[link](https://github.com/biter0088/pc-nerf)**|
|**2024-02-14**|**DUDF: Differentiable Unsigned Distance Fields with Hyperbolic Scaling**|近年来，人们对训练神经网络来近似无符号距离场（UDF）越来越感兴趣，以在3D重建的背景下表示开放表面。然而，UDF在零水平集上是不可微的，这导致距离和梯度的显著误差，通常导致碎片和不连续的表面。在本文中，我们提出学习无符号距离场的双曲标度，它定义了一个具有不同边界条件的新Eikonal问题。这使得我们的公式能够与最先进的连续可微隐式神经表示网络无缝集成，该网络在文献中广泛应用于表示有符号距离场。我们的方法不仅解决了开放曲面表示的挑战，而且在重建质量和训练性能方面也有显著提高。此外，未锁定字段的可微性允许准确计算基本拓扑属性，如法线方向和曲率，这些属性普遍存在于渲染等下游任务中。通过广泛的实验，我们在各种数据集和竞争基线中验证了我们的方法。结果表明，与以前的方法相比，精度提高，速度提高了一个数量级。 et.al.|[2402.08876](http://arxiv.org/abs/2402.08876)|null|
|**2024-02-13**|**IM-3D: Iterative Multiview Diffusion and Reconstruction for High-Quality 3D Generation**|大多数文本到3D生成器建立在现成的基于数十亿图像训练的文本到图像模型之上。他们使用分数蒸馏采样（SDS）的变体，这是缓慢的，有点不稳定，并且容易出现伪影。一种缓解措施是将2D生成器微调为多视图感知，这可以帮助提取或与重建网络相结合，直接输出3D对象。在本文中，我们进一步探索了文本到三维模型的设计空间。通过考虑视频而不是图像生成器，我们显著改进了多视图生成。结合3D重建算法，通过使用高斯飞溅，可以优化基于图像的鲁棒损失，我们直接从生成的视图中产生高质量的3D输出。我们的新方法IM-3D将2D生成器网络的评估次数减少了10-100x，从而实现了更高效的管道、更好的质量、更少的几何不一致性和更高的可用3D资产收益率。 et.al.|[2402.08682](http://arxiv.org/abs/2402.08682)|null|
|**2024-02-13**|**Camera Calibration through Geometric Constraints from Rotation and Projection Matrices**|相机校准过程包括估计内在和外在参数，这些参数对于准确执行3D重建、物体跟踪和增强现实等任务至关重要。在这项工作中，我们提出了一种新的基于约束的损失，用于测量内在（焦距： $（f_x，f_y）$和主点：$（p_x，p_y）$）和外在（基线：（$b$），视差：（$d$），平移：$（t_x，t_y，t_z）$，以及旋转特别是俯仰：$（\theta_p）$ ）相机参数。我们的新约束基于相机模型固有的几何特性，包括投影矩阵（消失点、世界原点图像、轴平面）的解剖结构和旋转矩阵的正交性。因此，我们通过多任务学习框架提出了一种新的无监督几何约束损失（UGCL）。我们的方法是一种混合方法，它利用神经网络的学习能力来估计所需的参数以及相机投影矩阵固有的基本数学特性。这种独特的方法不仅增强了模型的可解释性，而且有助于更知情的学习过程。此外，我们还引入了一个新的CVGL相机校准数据集，该数据集具有900多种相机参数配置，包含63600个图像对，这些图像对紧密反映了真实世界的情况。通过在合成数据集和真实世界数据集上进行训练和测试，与最先进的（SOTA）基准相比，我们提出的方法展示了所有参数的改进。代码和更新的数据集可以在这里找到：https://github.com/CVLABLUMS/CVGL-Camera-Calibration et.al.|[2402.08437](http://arxiv.org/abs/2402.08437)|**[link](https://github.com/cvlablums/cvgl-camera-calibration)**|
|**2024-02-09**|**Neural Rendering based Urban Scene Reconstruction for Autonomous Driving**|密集3D重建在自动驾驶中有许多应用，包括自动注释验证、多模式数据增强、为缺乏激光雷达的系统提供地面实况注释，以及提高自动标记的准确性。激光雷达提供了高度准确但稀疏的深度，而相机图像能够估计密集但有噪声的深度，尤其是在远距离。在本文中，我们利用这两种传感器的优势，提出了一种使用神经隐式曲面和辐射场相结合的框架进行多模式3D场景重建的方法。特别是，我们的方法估计密集而准确的3D结构，并基于有符号距离场创建隐式地图表示，该表示可以进一步渲染为RGB图像和深度图。可以从学习的有符号距离场中提取网格，并基于遮挡进行剔除。在使用3D对象检测模型的采样过程中，动态对象被有效地实时过滤。我们展示了具有挑战性的汽车场景的定性和定量结果。 et.al.|[2402.06826](http://arxiv.org/abs/2402.06826)|null|
|**2024-02-07**|**Carousel phase retrieval algorithm for 3D coherent X-ray diffraction imaging**|相干X射线衍射成像（CXDI）是一种独特的技术，通过基于测量的散射强度图执行计算相位重建程序，可以以纳米级分辨率重建2D和3D物体。重建过程可能具有高计算复杂度，并且通常不能在实验期间实时执行。我们提出了一种转盘相位检索算法（CPRA），该算法基于傅立叶切片定理将3D重建问题表示为对应于不同收集角度的投影图像的一组2D重建。为了保持2D重建之间的一致性，我们引入了一种迭代过程，其中每个2D重建都以周期性（旋转）的方式基于相邻的2D重建。2D重建的使用大大减少了计算时间和内存消耗。我们展示了在CPU和GPU计算架构上针对各种空间大小的复杂生物细胞的测试问题的CPRA实现。与传统的CXDI重建算法相比，CPRA在GPU上表现出300倍的速度，在CPU上表现出120倍的速度。CPRA还可以实现更高的重建质量。所实现的速度允许实时对计算上较大的对象进行高分辨率重建。 et.al.|[2402.05283](http://arxiv.org/abs/2402.05283)|**[link](https://github.com/UCSD-CEM/Carousel-Phase-Retrieval-Algorithm)**|
|**2024-02-07**|**Scalable Multi-view Clustering via Explicit Kernel Features Maps**|人们越来越意识到多视图学习是数据科学和机器学习的重要组成部分，这是多视图在现实世界应用中越来越普遍的结果，尤其是在网络环境中。在本文中，我们介绍了一种新的多视图子空间聚类的可扩展性框架。提出了一种有效的优化策略，利用核特征图来减少计算负担，同时保持良好的聚类性能。该算法的可扩展性意味着它可以在几分钟内使用标准机器应用于大规模数据集，包括具有数百万数据点的数据集。我们在不同规模的真实世界基准网络上进行了广泛的实验，以评估我们的算法相对于最先进的多视图子空间聚类方法和属性网络多视图方法的性能。 et.al.|[2402.04794](http://arxiv.org/abs/2402.04794)|null|
|**2024-02-06**|**EscherNet: A Generative Model for Scalable View Synthesis**|我们介绍了EscherNet，一个用于视图合成的多视图条件扩散模型。EscherNet学习隐含的和生成的3D表示，再加上专门的相机位置编码，允许对任意数量的参考视图和目标视图之间的相机变换进行精确和连续的相对控制。EscherNet在视图合成方面提供了非凡的通用性、灵活性和可扩展性——尽管它使用固定数量的3个参考视图到3个目标视图进行训练，但它可以在单个消费级GPU上同时生成100多个一致的目标视图。因此，EscherNet不仅解决了零样本新视图合成问题，而且自然地将单图像和多图像3D重建相结合，将这些不同的任务组合成一个单一的、有凝聚力的框架。我们的大量实验表明，即使与专门针对每个问题定制的方法相比，EscherNet也能在多个基准测试中实现最先进的性能。这种非凡的多功能性为设计用于3D视觉的可扩展神经结构开辟了新的方向。项目页面：\url{https://kxhit.github.io/EscherNet}. et.al.|[2402.03908](http://arxiv.org/abs/2402.03908)|null|

<p align=right>(<a href=#updated-on-20240220>back to top</a>)</p>

## Diffusion

|Publish Date|Title|Abstract|PDF|Code|
|---|---|---|---|---|
|**2024-02-16**|**Fusion of Diffusion Weighted MRI and Clinical Data for Predicting Functional Outcome after Acute Ischemic Stroke with Deep Contrastive Learning**|中风是一种常见的致残性神经疾病，影响约四分之一的25岁以上成年人口；超过一半的患者在急性中风发作后仍有不良后果，如永久性功能依赖甚至死亡。本研究的目的是研究扩散加权MRI模式与结构化健康档案相结合预测功能结果的有效性，以促进早期干预。提出了一种具有两阶段训练的深度融合学习网络：第一阶段侧重于跨模态表示学习，第二阶段侧重于分类。监督对比学习用于学习区分两类患者与个体模态嵌入和融合多模态嵌入的区别特征。该网络将DWI和ADC图像以及结构化的健康档案数据作为输入。结果是预测患者在中风发作后3个月需要长期护理。通过对3297名患者的数据集进行训练和评估，我们提出的融合模型的AUC、F1得分和准确率分别达到0.87%、0.80%和80.45%，优于整合医学领域成像和结构化数据的现有模型。如果使用包括NIHSS和合并症在内的综合临床变量进行训练，则从图像中获得的准确预测收益并不显著，而是显著的。然而，扩散加权MRI可以取代NIHSS，与其他现成的临床变量相结合，实现可比的准确性水平，以更好地推广。 et.al.|[2402.10894](http://arxiv.org/abs/2402.10894)|null|
|**2024-02-16**|**3D Diffuser Actor: Policy Diffusion with 3D Scene Representations**|我们结合了扩散策略和机器人操作的3D场景表示。扩散策略使用条件扩散模型学习以机器人和环境状态为条件的动作分布。它们最近已经证明优于确定性和替代状态条件下的动作分布学习方法。3D机器人策略使用使用感测深度从单个或多个相机视图聚合的3D场景特征表示。它们已经证明在相机视点上比2D同类产品更好地概括。我们将这两条工作线统一起来，并提出了3D Diffuser Actor，这是一种神经策略架构，在给定语言指令的情况下，构建视觉场景的3D表示，并在其上设置条件，以迭代地消除机器人末端执行器的3D旋转和平移。在每次去噪迭代中，我们的模型将末端效应器姿态估计表示为3D场景标记，并通过使用对其他3D视觉和语言标记的3D相对注意力对其进行特征化来预测每个末端效应器的3D平移和旋转误差。3D扩散器Actor在RLBench上创造了最先进的技术，在多视图设置上比当前SOTA的绝对性能增益高16.3%，在单视图设置上的绝对增益为13.1%。在CALVIN基准测试中，它在零样本不可见场景泛化设置方面优于当前SOTA，能够成功运行0.2个以上任务，相对增加7%。它也适用于现实世界中的一些演示。我们阐述了我们模型的建筑设计选择，如三维场景特征化和三维相对关注度，并表明它们都有助于泛化。我们的研究结果表明，3D场景表示和强大的生成建模是机器人从演示中高效学习的关键。 et.al.|[2402.10885](http://arxiv.org/abs/2402.10885)|null|
|**2024-02-16**|**Electronic Conductivity Measurements in Solid Electrolytes Using an Ion Blocking Microelectrode: Noise Rejection Based on a Median Filter**|介绍了一种电子电导率的测量方法。它结合了两种众所周知的电化学方法：循环伏安法和计时电流法。当达到稳态条件时，这种直流技术使用Hebb/Waggner方法来阻断离子传导，并允许确定固体电解质的电子传导。为了获得短的扩散时间，使用微接触作为离子阻挡电极。然而，由于电解质中的电子传导是并且应该是非常低的，因此电流也非常低，通常为几十纳安。因此，加热系统不可避免地产生使用中值滤波器解决的噪声问题。我们的系统允许在没有任何初步平滑或拟合曲线的情况下确定电导率。还给出了氧离子导体的一些结果 et.al.|[2402.10883](http://arxiv.org/abs/2402.10883)|null|
|**2024-02-16**|**Control Color: Multimodal Diffusion-based Interactive Image Colorization**|尽管存在许多着色方法，但仍存在一些局限性，如缺乏用户交互、局部着色不灵活、颜色渲染不自然、颜色变化不足和颜色溢出。为了解决这些问题，我们引入了控制颜色（CtrlColor），这是一种利用预先训练的稳定扩散（SD）模型的多模式彩色化方法，在高度可控的交互式图像彩色化中提供了很有前途的功能。虽然已经提出了几种基于扩散的方法，但支持多种模态的着色仍然是不平凡的。在这项研究中，我们的目标是在一个统一的框架内解决无条件和有条件的图像着色（文本提示、笔划、样例）问题，并解决颜色溢出和不正确的颜色问题。具体而言，我们提出了一种对用户笔划进行编码的有效方法，以实现精确的局部颜色操作，并采用一种实用的方法来约束与样例相似的颜色分布。除了接受文本提示作为条件外，这些设计还为我们的方法增加了多功能性。我们还引入了一个基于自注意的新模块和一个内容引导的可变形自动编码器，以解决长期存在的颜色溢出和着色不准确的问题。广泛的比较表明，我们的模型在质量和数量上都优于最先进的图像着色方法。 et.al.|[2402.10855](http://arxiv.org/abs/2402.10855)|null|
|**2024-02-16**|**Training Class-Imbalanced Diffusion Model Via Overlap Optimization**|扩散模型最近在高质量图像合成和相关任务方面取得了重大进展。然而，在真实世界数据集上训练的扩散模型通常遵循长尾分布，其尾部类的保真度较差。包括扩散模型在内的深度生成模型偏向于具有丰富训练图像的类。为了解决稀有类和尾部类的合成图像之间观察到的外观重叠问题，我们提出了一种基于对比学习的方法，以最大限度地减少不同类合成图像分布之间的重叠。我们展示了我们的概率对比学习方法的变体可以应用于任何类别的条件扩散模型。对于具有长尾分布的多个数据集，使用我们的损失，我们在图像合成方面显示出显著的改进。大量实验结果表明，对于基于扩散的生成和分类模型，该方法可以有效地处理不平衡数据。我们的代码和数据集将在https://github.com/yanliang3612/DiffROP. et.al.|[2402.10821](http://arxiv.org/abs/2402.10821)|**[link](https://github.com/yanliang3612/diffrop)**|
|**2024-02-16**|**VATr++: Choose Your Words Wisely for Handwritten Text Generation**|近年来，由于采用GANs、Transformers以及初步的扩散模型的基于学习的解决方案的成功，风格手写文本生成（HTG）受到了极大的关注。尽管兴趣激增，但仍有一个关键但研究不足的方面——视觉和文本输入对HTG模型训练的影响及其对性能的后续影响。这项研究深入研究了一种前沿的样式化HTG方法，提出了输入准备和训练正则化的策略，使模型能够获得更好的性能和更好的泛化能力。通过对几个不同的设置和数据集的广泛分析，验证了这些方面。此外，在这项工作中，我们超越了性能优化，解决了HTG研究中的一个重大障碍——缺乏标准化的评估协议。特别是，我们提出了HTG评估协议的标准化，并对现有方法进行了全面的基准测试。通过这样做，我们旨在为HTG战略之间的公平和有意义的比较奠定基础，促进该领域的进展。 et.al.|[2402.10798](http://arxiv.org/abs/2402.10798)|null|
|**2024-02-16**|**Nearly-optimal effective stability estimates around Diophantine tori of Hölder Hamiltonians**|我们证明了H“较老的可微哈密顿系统的解，与拉格朗日量周围半径为 $\rho>0$的小球中的初始条件有关，$（\gamma，\tau）-$丢番图，拟周期环面，在时间$t^｛\text｛stab｝｝\simeq 1/（|\rho|^｛1+\frac｛\ell-1｝｛\tau+1｝|\ln\rho| ^｛\ell-1｝）上是稳定的$，其中$\ell>2d+1，\ell\in\mathbb R$是正则性，$d$是自由度。在有限可微的情况下（对于整数$\ell$），这一结果改进了先前已知的丢番图环面周围的有效稳定界。此外，通过先前基于Anosov-Katok构造的工作，已知对于任何$\varepsilon>0$，都存在一个$C^\ell$-Hamiltonian，其中$\ell\ge3$，允许从$（\gamma，\tau）$-丢番图环面以$t^｛\text｛diff｝｝_n\simeq 1/（|\rho_n|^｛1+\frac｛\ell-1｝｛\tau+1｝+\varepsilon｝）$的顺序扩散的距离$\rho_n\到0$ 的解序列。因此，我们所展示的稳定性估计在任意小的多项式校正下都是最优的。 et.al.|[2402.10764](http://arxiv.org/abs/2402.10764)|null|
|**2024-02-16**|**Revisiting a Core-Jet Laboratory at High Redshift: Analysis of the Radio Jet in the Quasar PKS 2215+020 at z=3.572**|著名的射电类星体PKS 2215+020（J2217+0220）曾被称为红移z=3.572时核心-喷流物理的新实验室，因为它异常扩展的喷流结构可通过超长基线干涉测量（VLBI）观测追踪，距离紧凑的核心约600个投影距离，并有弧秒级射电和X射线喷流的迹象。虽然后来无法证实X射线喷流的存在，但这个活动星系核在其长VLBI喷流的高红移下仍然是独一无二的。在这里，我们分析了1995年至2020年超过25年的1.7至15.4 GHz五个频带的档案多历元VLBI成像数据。我们首次在PKS 2215+020中约束了射流部件的表观固有运动。8 GHz下的亮度分布建模揭示了近0.02 mas/yr的固有运动（中等超光速，显然是光速的两倍），并为内部相对论喷流中的多普勒增强因子提供了Δ=11.5，该喷流与视线倾斜2度以内，伽马=6体洛伦兹因子。这些值使PKS 2215+020符合blazar的条件，在z>3.5的仅约20个物体的小样本中具有相当典型的喷流特性，这些物体迄今为止具有类似的测量结果。根据2GHz VLBI数据，在距离核心约60mas处的扩散和扩展外部发射特征（可能是喷流与周围星系介质相互作用并被周围星系介质减速的地方）与静止一致，尽管根据目前可用的数据不能排除慢运动。 et.al.|[2402.10722](http://arxiv.org/abs/2402.10722)|null|
|**2024-02-16**|**Rethinking Human-like Translation Strategy: Integrating Drift-Diffusion Model with Large Language Models for Machine Translation**|大型语言模型（LLM）在包括机器翻译在内的各种下游任务中显示出了巨大的潜力。然而，先前关于基于LLM的机器翻译的工作主要集中在更好地利用训练数据、演示或预定义的通用知识来提高性能，而缺乏像人类翻译那样的决策考虑。在本文中，我们将Thinker与漂移扩散模型（Thinker DDM）相结合来解决这个问题。然后，我们重新定义了漂移扩散过程，以模仿人类译者在资源受限的情况下的动态决策。我们使用WMT22和CommonMT数据集，在高资源、低资源和常识翻译设置下进行了广泛的实验，其中Thinker DDM在前两种情况下都优于基线。我们还对常识翻译进行了额外的分析和评估，以说明所提出的方法的高效性和有效性。 et.al.|[2402.10699](http://arxiv.org/abs/2402.10699)|null|
|**2024-02-16**|**Decomposition for Enhancing Attention: Improving LLM-based Text-to-SQL through Workflow Paradigm**|大型语言模型的上下文学习在自然语言处理领域取得了显著的成功，而大量的案例研究表明，单步思维链提示方法面临着注意力扩散和在文本到SQL等复杂任务中表现不佳等挑战。为了提高LLM在文本到SQL中的上下文学习能力，提出了一种工作流范式方法，旨在通过分解来提高LLM的注意力和解决问题的范围。具体来说，消除冗余信息的信息确定模块和基于问题分类的全新提示结构大大提高了模型的关注度。此外，包括自我纠正和主动学习模块大大扩展了LLM解决问题的范围，从而提高了基于LLM的方法的上限。在三个数据集上进行的大量实验表明，我们的方法显著优于其他方法。与Spider Dev和Spider Reality数据集的现有基线相比，以及Spider Test数据集的新SOTA结果，实现了约2-3个百分点的改进。我们的代码可在GitHub:\url上获得{https://github.com/FlyingFeather/DEA-SQL}. et.al.|[2402.10671](http://arxiv.org/abs/2402.10671)|null|

<p align=right>(<a href=#updated-on-20240220>back to top</a>)</p>

## NeRF

|Publish Date|Title|Abstract|PDF|Code|
|---|---|---|---|---|
|**2024-02-15**|**Reg-NF: Efficient Registration of Implicit Surfaces within Neural Fields**|神经场，即基于坐标的神经网络，最近因隐含地表示场景而广受欢迎。与基于点云等显式表示的经典方法相比，神经场提供了连续的场景表示，能够以紧凑且理想的机器人应用方式表示3D几何结构和外观。然而，有限的现有方法已经研究了通过直接利用这些连续的隐式表示来配准多个神经场。在本文中，我们提出了Reg-NF，这是一种基于神经场的配准，它优化了两个任意神经场之间的相对6-DoF变换，即使这两个场具有不同的比例因子。Reg NF的关键组成部分包括双向配准损失、多视图表面采样和体积符号距离函数（SDF）的利用。我们在一个新的神经场数据集上展示了我们的方法，用于评估配准问题。我们提供了一组详尽的实验和消融研究，以确定我们的方法的性能，同时也讨论了局限性，为研究界在无约束环境中利用神经场的开放挑战提供了未来的方向。 et.al.|[2402.09722](http://arxiv.org/abs/2402.09722)|null|
|**2024-02-12**|**Unsupervised Discovery of Object-Centric Neural Fields**|我们研究从单个图像中推断3D以对象为中心的场景表示。虽然最近的方法在从简单的合成图像中无监督地发现3D对象方面显示出了潜力，但它们未能推广到具有视觉丰富和多样化对象的真实世界场景。这种限制源于它们的对象表示，它将对象的内在属性（如形状和外观）与外在的、以观察者为中心的属性（如3D位置）纠缠在一起。为了解决这一瓶颈，我们提出了以对象为中心的神经场的无监督发现（uOCF）。uOCF专注于学习对象的内在，并分别对外在进行建模。我们的方法显著提高了系统泛化能力，从而能够从稀疏的真实世界图像中无监督地学习高保真的以对象为中心的场景表示。为了评估我们的方法，我们收集了三个新的数据集，包括两个真实的厨房环境。大量实验表明，uOCF能够在无监督的情况下从单个真实图像中发现视觉丰富的对象，从而实现3D对象分割和场景操作等应用。值得注意的是，uOCF演示了对单个真实图像中看不见的物体的零样本泛化。项目页面：https://red-fairy.github.io/uOCF/ et.al.|[2402.07376](http://arxiv.org/abs/2402.07376)|null|
|**2024-02-06**|**Improved Generalization of Weight Space Networks via Augmentations**|在深度权重空间（DWS）中学习，神经网络处理其他神经网络的权重，是一个新兴的研究方向，应用于2D和3D神经领域（INRs、NeRFs），以及对其他类型的神经网络进行推断。不幸的是，权重空间模型往往存在严重的过拟合问题。我们实证分析了这种过拟合的原因，发现一个关键原因是DWS数据集缺乏多样性。虽然给定的对象可以用许多不同的权重配置来表示，但典型的INR训练集无法捕捉表示同一对象的INR之间的可变性。为了解决这一问题，我们探索了在权重空间中增加数据的策略，并提出了一种适用于权重空间的MixUp方法。我们在两个设置中展示了这些方法的有效性。在分类方面，它们可以提高性能，类似于拥有10倍以上的数据。在自我监督的对比学习中，它们在下游分类中产生了5-10%的显著收益。 et.al.|[2402.04081](http://arxiv.org/abs/2402.04081)|null|
|**2024-01-31**|**BlockFusion: Expandable 3D Scene Generation using Latent Tri-plane Extrapolation**|我们介绍了BlockFusion，这是一种基于扩散的模型，它将3D场景生成为单元块，并无缝地合并新的块来扩展场景。BlockFusion使用从完整的3D场景网格中随机裁剪的3D块的数据集进行训练。通过逐块拟合，所有训练块都被转换为混合神经场：具有包含几何特征的三平面，然后是用于解码有符号距离值的多层感知器（MLP）。采用变分自动编码器将三平面压缩到潜在的三平面空间中，在该空间上进行去噪扩散处理。应用于潜在表示的扩散允许高质量和多样化的3D场景生成。要在生成过程中扩展场景，只需附加空块以与当前场景重叠，并外推现有的潜在三平面以填充新块。外推是通过在去噪迭代过程中使用来自重叠三平面的特征样本来调节生成过程来完成的。潜在的三平面外推法产生语义和几何上有意义的过渡，与现有场景和谐融合。2D布局调节机制用于控制场景元素的放置和布置。实验结果表明，BlockFusion能够在室内和室外场景中生成具有前所未有的高质量形状的多样化、几何一致和无边界的大型3D场景。 et.al.|[2401.17053](http://arxiv.org/abs/2401.17053)|null|
|**2024-01-26**|**Learning Neural Radiance Fields of Forest Structure for Scalable and Fine Monitoring**|这项工作利用神经辐射场和遥感技术用于林业应用。在这里，我们展示了神经辐射场为改进森林监测中现有的遥感方法提供了广泛的可能性。我们提出的实验证明了它们的潜力：（1）表达森林三维结构的精细特征，（2）融合可用的遥感模式，（3）改进三维结构衍生的森林指标。总之，这些特性使神经场成为一种有吸引力的计算工具，具有进一步提高森林监测程序的可扩展性和准确性的巨大潜力。 et.al.|[2401.15029](http://arxiv.org/abs/2401.15029)|null|
|**2024-01-25**|**Learning Robust Generalizable Radiance Field with Visibility and Feature Augmented Point Representation**|本文介绍了广义神经辐射场（NeRF）的一种新范式。以前的通用NeRF方法将多视点立体技术与基于图像的神经渲染相结合进行泛化，产生了令人印象深刻的结果，同时存在三个问题。首先，遮挡常常导致不一致的特征匹配。然后，由于采样点和粗略特征聚合的单独过程，它们在几何不连续性和局部尖锐形状中传递失真和伪影。第三，当源视图离目标视图不够近时，它们基于图像的表示会发生严重退化。为了应对挑战，我们提出了第一个基于点而不是基于图像的渲染构建可泛化神经场的范式，我们称之为可泛化神经点场（GPF）。我们的方法通过几何先验显式地建模可见性，并用神经特征增强它们。我们提出了一种新的非均匀对数采样策略，以提高渲染速度和重建质量。此外，我们提出了一种可学习的内核，该内核在空间上增加了用于特征聚合的特征，减轻了几何结构急剧变化的地方的失真。此外，我们的表现很容易被操纵。实验表明，在泛化和微调设置中，我们的模型可以在三个数据集上提供比所有对应模型和基准更好的几何结构、视图一致性和渲染质量，初步证明了可泛化NeRF新范式的潜力。 et.al.|[2401.14354](http://arxiv.org/abs/2401.14354)|null|
|**2024-01-24**|**Unified neural field theory of brain dynamics underlying oscillations in Parkinson's disease and generalized epilepsies**|通过皮质丘脑基底神经节（CTBG）系统的神经场模型，联合探讨了帕金森病（PD）和全身性癫痫的病理同步神经振荡的机制。基底神经节（BG）被近似为一个单一的有效群体，并分析了它们在调节振荡皮质丘脑（CT）动力学中的作用，反之亦然。除了正常的脑电图节律外，模型中还存在4 Hz和20 Hz左右的增强活动，这与PD的特征频率一致。这些节律是由BG和CT人群之间回路中的共振引起的，类似于先前CT模型中潜在的癫痫振荡。多巴胺耗竭被认为削弱了对PD中这些共振的抑制，网络连接解释了在4-8Hz和20Hz左右BG、丘脑和皮层活动之间的显著一致性。丘脑网状核（TRN）和BG的传入和传出连接位点之间的相似性预测低多巴胺对应于强直-阵挛（大发作）癫痫发作的可能性降低，这与实验结果一致。此外，该模型预测，与实验结果相匹配的低多巴胺水平会增加缺席（轻微）癫痫发作的可能性。与其他CTBG建模研究一致，当传入和传出BG与CT系统的连接增强时，表现出对缺席发作活动的抑制。BG被证明在强直-阵挛发作状态附近抑制CTBG系统的活性，从而深入了解BG回路中目前治疗的疗效。TRN的睡眠状态也被发现可以抑制病理性PD活动匹配观察。总的来说，这些发现证明了广泛性癫痫和帕金森病的相干振荡之间有很强的相似性，并为可能的合并症提供了见解。 et.al.|[2401.13467](http://arxiv.org/abs/2401.13467)|null|
|**2024-01-17**|**Reproducibility via neural fields of visual illusions induced by localized stimuli**|本文研究了Billock和Tsou[PNAS，2007]使用Amari型神经场的可控性对初级视皮层（V1）皮层活动进行建模的实验复制，重点关注中央凹或外周视野中的规则漏斗模式。其目的是理解和模拟在这些实验中观察到的视觉现象，强调其非线性性质。这项研究包括设计模拟Billock和Tsou实验中视觉刺激的感官输入。然后从理论和数值上研究这些输入引起的后图像，以确定它们复制实验观察到的视觉效果的能力。这项研究的一个关键方面是研究神经反应的非线性性质所引起的影响。特别是，通过强调兴奋性和抑制性神经元在某些视觉现象出现中的重要性，这项研究表明，这两种类型的神经元活动的相互作用在视觉过程中发挥着重要作用，挑战了后者主要由兴奋性活动单独驱动的假设。 et.al.|[2401.09108](http://arxiv.org/abs/2401.09108)|null|
|**2024-01-12**|**Motion2VecSets: 4D Latent Vector Set Diffusion for Non-rigid Shape Reconstruction and Tracking**|我们介绍了Motion2VecSets，这是一种用于从点云序列进行动态曲面重建的4D扩散模型。虽然现有的最先进的方法已经证明在使用神经场表示重建非刚性对象方面取得了成功，但传统的前馈网络遇到了来自噪声、部分或稀疏点云的模糊观测的挑战。为了应对这些挑战，我们引入了一种扩散模型，该模型通过压缩潜在表示的迭代去噪过程来显式学习非刚性对象的形状和运动分布。当处理模糊输入时，基于扩散的先验能够进行更合理和概率的重建。我们用潜在向量集参数化4D动力学，而不是使用全局潜在。这种新颖的4D表示使我们能够学习局部表面形状和变形模式，从而实现更准确的非线性运动捕捉，并显著提高对看不见的运动和身份的可推广性。对于更具时间连贯性的目标跟踪，我们同步地对变形潜集进行去噪，并在多个帧之间交换信息。为了避免计算开销，我们设计了一个交错的空间和时间注意力块，以沿着空间和时间域交替聚集变形潜伏期。与最先进的方法进行了广泛的比较，证明了我们的Motion2VenSets在从各种不完美的观测进行4D重建方面的优势，特别是在从DeformingThings4D Animals数据集上的稀疏点云重建看不见的个体方面，与CaDex相比，交集优于并集（IoU）提高了19%。更多详细信息，请访问https://vveicao.github.io/projects/Motion2VecSets/. et.al.|[2401.06614](http://arxiv.org/abs/2401.06614)|null|
|**2024-01-05**|**Denoising Vision Transformers**|我们深入研究了视觉转换器（ViTs）固有的一个细微但重大的挑战：这些模型的特征图显示出网格状的伪影，这对ViTs在下游任务中的性能造成了不利影响。我们的研究将这个基本问题追溯到输入阶段的位置嵌入。为了解决这一问题，我们提出了一种新的噪声模型，该模型普遍适用于所有的ViT。具体来说，噪声模型将ViT输出分解为三个部分：一个没有噪声伪影的语义术语和两个以像素位置为条件的伪影相关术语。这种分解是通过在每幅图像的基础上加强与神经场的交叉视图特征一致性来实现的。这种逐图像优化过程从原始ViT输出中提取无伪影特征，为离线应用程序提供干净的特征。扩大了我们的解决方案的范围，以支持在线功能，我们引入了一种可学习的去噪器，直接从未处理的ViT输出中预测无伪影特征，这显示出对新数据的显著泛化能力，而无需对每张图像进行优化。我们的两阶段方法，称为去噪视觉转换器（DVT），不需要重新训练现有的预先训练的ViT，并且立即适用于任何基于转换器的架构。我们在各种具有代表性的ViT（DINO、MAE、DeiT III、EVA02、CLIP、DINOv2、DINOv2-reg）上评估了我们的方法。广泛的评估表明，我们的DVT在多个数据集（例如+3.84mIoU）的语义和几何任务中持续显著地改进了现有的最先进的通用模型。我们希望我们的研究将鼓励对ViT设计进行重新评估，特别是关于位置嵌入的天真使用。 et.al.|[2401.02957](http://arxiv.org/abs/2401.02957)|null|

<p align=right>(<a href=#updated-on-20240220>back to top</a>)</p>

[contributors-shield]: https://img.shields.io/github/contributors/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[contributors-url]: https://github.com/Vincentqyw/cv-arxiv-daily/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[forks-url]: https://github.com/Vincentqyw/cv-arxiv-daily/network/members
[stars-shield]: https://img.shields.io/github/stars/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[stars-url]: https://github.com/Vincentqyw/cv-arxiv-daily/stargazers
[issues-shield]: https://img.shields.io/github/issues/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[issues-url]: https://github.com/Vincentqyw/cv-arxiv-daily/issues

