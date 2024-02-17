[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]

## Updated on 2024.02.17
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

<p align=right>(<a href=#updated-on-20240217>back to top</a>)</p>

## 3D Reconstruction

|Publish Date|Title|Abstract|PDF|Code|
|---|---|---|---|---|
|**2024-02-15**|**GES: Generalized Exponential Splatting for Efficient Radiance Field Rendering**|3D高斯散射的进步显著加速了3D重建和生成。然而，它可能需要大量的高斯，这会产生大量的内存占用。本文介绍了GES（Generalized Exponential Splatting），这是一种利用广义指数函数（GEF）对3D场景进行建模的新表示，需要更少的粒子来表示场景，因此在效率上显著优于高斯飞溅方法，并具有基于高斯的实用程序的即插即用替换能力。GES在原理性1D设置和逼真的3D场景中都得到了理论和实证验证。它被证明可以更准确地表示具有尖锐边缘的信号，由于其固有的低通特性，这对高斯人来说通常是具有挑战性的。我们的实证分析表明，GEF在拟合自然发生的信号（如正方形、三角形和抛物线信号）方面优于高斯，从而减少了对增加高斯飞溅的内存占用的广泛拆分操作的需要。借助调频损耗，GES在新的视图合成基准中实现了有竞争力的性能，同时所需的内存存储量不到高斯飞溅的一半，并将渲染速度提高了39%。代码可在项目网站上获得https://abdullahamdi.com/ges . et.al.|[2402.10128](http://arxiv.org/abs/2402.10128)|null|
|**2024-02-14**|**PC-NeRF: Parent-Child Neural Radiance Fields Using Sparse LiDAR Frames in Autonomous Driving Environments**|大规模的3D场景重建和新颖的视图合成对于自动驾驶汽车至关重要，尤其是利用时间稀疏的激光雷达帧。然而，传统的显式表示仍然是以无限分辨率表示重建和合成场景的一个重要瓶颈。尽管最近开发的神经辐射场（NeRF）在隐式表示中显示出令人信服的结果，但使用稀疏激光雷达帧进行大规模3D场景重建和新的视图合成的问题仍未得到探索。为了弥补这一差距，我们提出了一种3D场景重建和新的视图合成框架，称为父子神经辐射场（PC NeRF）。该框架基于父NeRF和子NeRF两个模块，实现了分层空间划分和多级场景表示，包括场景、分段和点级别。多级场景表示增强了稀疏激光雷达点云数据的有效利用，并能够快速获取近似体积场景表示。经过大量实验，PC NeRF被证明可以在大规模场景中实现高精度的新型激光雷达视图合成和三维重建。此外，PC NeRF可以有效地处理稀疏激光雷达帧的情况，并在有限的训练时期内表现出较高的部署效率。我们的方法实施和预先培训的模型可在https://github.com/biter0088/pc-nerf. et.al.|[2402.09325](http://arxiv.org/abs/2402.09325)|**[link](https://github.com/biter0088/pc-nerf)**|
|**2024-02-14**|**DUDF: Differentiable Unsigned Distance Fields with Hyperbolic Scaling**|近年来，人们对训练神经网络来近似无符号距离场（UDF）越来越感兴趣，以在3D重建的背景下表示开放表面。然而，UDF在零水平集上是不可微的，这导致距离和梯度的显著误差，通常导致碎片和不连续的表面。在本文中，我们提出学习无符号距离场的双曲标度，它定义了一个具有不同边界条件的新Eikonal问题。这使得我们的公式能够与最先进的连续可微隐式神经表示网络无缝集成，该网络在文献中广泛应用于表示有符号距离场。我们的方法不仅解决了开放曲面表示的挑战，而且在重建质量和训练性能方面也有显著提高。此外，未锁定字段的可微性允许准确计算基本拓扑属性，如法线方向和曲率，这些属性普遍存在于渲染等下游任务中。通过广泛的实验，我们在各种数据集和竞争基线中验证了我们的方法。结果表明，与以前的方法相比，精度提高，速度提高了一个数量级。 et.al.|[2402.08876](http://arxiv.org/abs/2402.08876)|null|
|**2024-02-13**|**IM-3D: Iterative Multiview Diffusion and Reconstruction for High-Quality 3D Generation**|大多数文本到3D生成器建立在现成的基于数十亿图像训练的文本到图像模型之上。他们使用分数蒸馏采样（SDS）的变体，这是缓慢的，有点不稳定，并且容易出现伪影。一种缓解措施是将2D生成器微调为多视图感知，这可以帮助提取或与重建网络相结合，直接输出3D对象。在本文中，我们进一步探索了文本到三维模型的设计空间。通过考虑视频而不是图像生成器，我们显著改进了多视图生成。结合3D重建算法，通过使用高斯飞溅，可以优化基于图像的鲁棒损失，我们直接从生成的视图中产生高质量的3D输出。我们的新方法IM-3D将2D生成器网络的评估次数减少了10-100x，从而实现了更高效的管道、更好的质量、更少的几何不一致性和更高的可用3D资产收益率。 et.al.|[2402.08682](http://arxiv.org/abs/2402.08682)|null|
|**2024-02-13**|**Camera Calibration through Geometric Constraints from Rotation and Projection Matrices**|相机校准过程包括估计内在和外在参数，这些参数对于准确执行3D重建、物体跟踪和增强现实等任务至关重要。在这项工作中，我们提出了一种新的基于约束的损失，用于测量内在（焦距： $（f_x，f_y）$和主点：$（p_x，p_y）$）和外在（基线：（$b$），视差：（$d$），平移：$（t_x，t_y，t_z）$，以及旋转特别是俯仰：$（\theta_p）$ ）相机参数。我们的新约束基于相机模型固有的几何特性，包括投影矩阵的解剖结构（消失点、世界原点图像、轴平面）和旋转矩阵的正交性。因此，我们通过多任务学习框架提出了一种新的无监督几何约束损失（UGCL）。我们的方法是一种混合方法，利用神经网络的学习能力来估计所需参数以及相机投影矩阵固有的基本数学特性。这种独特的方法不仅提高了模型的可解释性，还促进了更知情的学习过程。此外，我们还引入了一个新的CVGL相机校准数据集，该数据集具有900多种相机参数配置，包含63600个图像对，这些图像对紧密反映了真实世界的情况。通过在合成数据集和真实世界数据集上进行训练和测试，与最先进的（SOTA）基准相比，我们提出的方法展示了所有参数的改进。代码和更新的数据集可以在这里找到：https://github.com/CVLABLUMS/CVGL-Camera-Calibration et.al.|[2402.08437](http://arxiv.org/abs/2402.08437)|**[link](https://github.com/cvlablums/cvgl-camera-calibration)**|
|**2024-02-09**|**Neural Rendering based Urban Scene Reconstruction for Autonomous Driving**|密集3D重建在自动驾驶中有许多应用，包括自动注释验证、多模式数据增强、为缺乏激光雷达的系统提供地面实况注释，以及提高自动标记的准确性。激光雷达提供了高度准确但稀疏的深度，而相机图像能够估计密集但有噪声的深度，尤其是在远距离。在本文中，我们利用这两种传感器的优势，提出了一种使用神经隐式曲面和辐射场相结合的框架进行多模式3D场景重建的方法。特别是，我们的方法估计密集而准确的3D结构，并基于有符号距离场创建隐式地图表示，该表示可以进一步渲染为RGB图像和深度图。可以从学习的有符号距离场中提取网格，并基于遮挡进行剔除。在使用3D对象检测模型的采样过程中，动态对象被有效地实时过滤。我们展示了具有挑战性的汽车场景的定性和定量结果。 et.al.|[2402.06826](http://arxiv.org/abs/2402.06826)|null|
|**2024-02-07**|**Carousel phase retrieval algorithm for 3D coherent X-ray diffraction imaging**|相干X射线衍射成像（CXDI）是一种独特的技术，通过基于测量的散射强度图执行计算相位重建程序，可以以纳米级分辨率重建2D和3D物体。重建过程可能具有高计算复杂度，并且通常不能在实验期间实时执行。我们提出了一种转盘相位检索算法（CPRA），该算法基于傅立叶切片定理将3D重建问题表示为对应于不同收集角度的投影图像的一组2D重建。为了保持2D重建之间的一致性，我们引入了一种迭代过程，其中每个2D重建都以周期性（旋转）的方式基于相邻的2D重建。2D重建的使用大大减少了计算时间和内存消耗。我们展示了在CPU和GPU计算架构上针对各种空间大小的复杂生物细胞的测试问题的CPRA实现。与传统的CXDI重建算法相比，CPRA在GPU上表现出300倍的速度，在CPU上表现出120倍的速度。CPRA还可以实现更高的重建质量。所实现的速度允许实时对计算上较大的对象进行高分辨率重建。 et.al.|[2402.05283](http://arxiv.org/abs/2402.05283)|**[link](https://github.com/UCSD-CEM/Carousel-Phase-Retrieval-Algorithm)**|
|**2024-02-07**|**Scalable Multi-view Clustering via Explicit Kernel Features Maps**|人们越来越意识到多视图学习是数据科学和机器学习的重要组成部分，这是多视图在现实世界应用中越来越普遍的结果，尤其是在网络环境中。在本文中，我们介绍了一种新的多视图子空间聚类的可扩展性框架。提出了一种有效的优化策略，利用核特征图来减少计算负担，同时保持良好的聚类性能。该算法的可扩展性意味着它可以在几分钟内使用标准机器应用于大规模数据集，包括具有数百万数据点的数据集。我们在不同规模的真实世界基准网络上进行了广泛的实验，以评估我们的算法相对于最先进的多视图子空间聚类方法和属性网络多视图方法的性能。 et.al.|[2402.04794](http://arxiv.org/abs/2402.04794)|null|
|**2024-02-06**|**EscherNet: A Generative Model for Scalable View Synthesis**|我们介绍了EscherNet，一个用于视图合成的多视图条件扩散模型。EscherNet学习隐含的和生成的3D表示，再加上专门的相机位置编码，允许对任意数量的参考视图和目标视图之间的相机变换进行精确和连续的相对控制。EscherNet在视图合成方面提供了非凡的通用性、灵活性和可扩展性——尽管它使用固定数量的3个参考视图到3个目标视图进行训练，但它可以在单个消费级GPU上同时生成100多个一致的目标视图。因此，EscherNet不仅解决了零样本新视图合成问题，而且自然地将单图像和多图像3D重建相结合，将这些不同的任务组合成一个单一的、有凝聚力的框架。我们的大量实验表明，EscherNet在多个基准测试中实现了最先进的性能，即使与专门针对每个单独问题定制的方法相比也是如此。这种非凡的多功能性为设计用于3D视觉的可扩展神经结构开辟了新的方向。项目页面：\url{https://kxhit.github.io/EscherNet}. et.al.|[2402.03908](http://arxiv.org/abs/2402.03908)|null|
|**2024-02-06**|**Efficient Generation of Hidden Outliers for Improved Outlier Detection**|异常值生成是一种常用的技术，用于解决重要的异常值检测任务。生成具有现实行为的异常值具有挑战性。现有的流行方法往往忽略高维空间中异常值的“多视图”特性。对这一财产进行核算的唯一现有方法在效率和有效性方面不足。我们提出了BISECT，这是一种新的异常值生成方法，可以创建模拟上述属性的真实异常值。为此，BISECT采用了本文中介绍的一个新颖命题，说明如何有效地生成所述现实异常值。我们的方法比当前重建“多个视图”的方法有更好的保证和复杂性。我们使用BISECT生成的合成异常值来有效地增强不同数据集中的异常值检测，用于多种用例。例如，与基线相比，BISECT的过采样将误差减少了3倍。 et.al.|[2402.03846](http://arxiv.org/abs/2402.03846)|**[link](https://github.com/jcribeiro98/bisect)**|

<p align=right>(<a href=#updated-on-20240217>back to top</a>)</p>

## Diffusion

|Publish Date|Title|Abstract|PDF|Code|
|---|---|---|---|---|
|**2024-02-15**|**Self-Play Fine-Tuning of Diffusion Models for Text-to-Image Generation**|微调扩散模型仍然是生成人工智能（GenAI）中一个未被充分探索的前沿领域，尤其是与微调大型语言模型（LLM）方面取得的显著进展相比。虽然稳定扩散（SD）和SDXL等尖端扩散模型依赖于监督微调，但在看到一定数量的数据后，它们的性能不可避免地会趋于平稳。最近，强化学习（RL）已被用于微调具有人类偏好数据的扩散模型，但它需要每个文本提示至少两个图像（“赢家”和“输家”图像）。在本文中，我们介绍了一种创新技术，称为扩散模型的自玩微调（SPIN diffusion），其中扩散模型与其早期版本竞争，促进迭代自我完善过程。我们的方法为传统的监督微调和RL策略提供了一种替代方案，显著提高了模型性能和一致性。我们在Pick-a-Pic数据集上的实验表明，SPIN Diffusion从第一次迭代开始，就在人类偏好对齐和视觉吸引力方面优于现有的监督微调方法。通过第二次迭代，它在所有指标上都超过了基于RLHF的方法的性能，用更少的数据实现了这些结果。 et.al.|[2402.10210](http://arxiv.org/abs/2402.10210)|null|
|**2024-02-15**|**Recovering the Pre-Fine-Tuning Weights of Generative Models**|生成建模中的主导范式包括两个步骤：i）在大规模但不安全的数据集上进行预训练，ii）通过微调将预训练的模型与人类价值观相一致。这种做法被认为是安全的，因为目前没有任何方法可以恢复不安全的预微调模型权重。在本文中，我们证明了这种假设往往是错误的。具体来说，我们提出了频谱去调谐，这是一种可以使用一些低秩（LoRA）微调模型来恢复预微调模型的权重的方法。与之前试图恢复预微调功能的攻击相比，我们的方法旨在恢复精确的预微调权重。我们的方法利用这种新的漏洞来对抗大规模模型，如个性化的稳定扩散和对齐的Mistral。 et.al.|[2402.10208](http://arxiv.org/abs/2402.10208)|**[link](https://github.com/eliahuhorwitz/Spectral-DeTuning)**|
|**2024-02-15**|**Rewards-in-Context: Multi-objective Alignment of Foundation Models with Dynamic Preference Adjustment**|我们考虑基础模型与人类偏好的多目标对齐问题，这是迈向有益和无害的人工智能系统的关键一步。然而，使用强化学习（RL）对大型基础模型进行微调通常成本高昂且不稳定，而且人类偏好的多维性、异质性和冲突性进一步使对齐过程复杂化。在本文中，我们引入了上下文中的奖励（RiC），它将基础模型对其即时上下文中的多个奖励的响应作为条件，并对对齐应用监督微调。RiC的显著特征是简单性和自适应性，因为它只需要对单个基础模型进行监督微调，并支持在推理期间对用户偏好进行动态调整。受抽象凸优化问题解析解的启发，我们的动态推理时间调整方法接近多目标的Pareto最优解。经验证据表明，与多目标RL基线相比，我们的方法在调整大型语言模型（LLM）和扩散模型以适应不同奖励方面的有效性，仅需约 $10\%%$ GPU小时。 et.al.|[2402.10207](http://arxiv.org/abs/2402.10207)|null|
|**2024-02-15**|**Radio-astronomical Image Reconstruction with Conditional Denoising Diffusion Model**|从脏无线电图像重建天空模型以进行精确的源定位和通量估计，对于研究高红移下的星系演化至关重要，尤其是在深场中使用阿塔卡马大型毫米阵列（ALMA）等仪器。随着像平方公里阵列（SKA）这样的新项目，人们越来越需要更好的源提取方法。目前的技术，如CLEAN和PyBDSF，往往无法检测到微弱的来源，这突出了对更准确方法的需求。这项研究建议使用随机神经网络直接从脏图像中重建天空模型。这种方法可以精确定位无线电源，并测量具有相关不确定性的无线电源通量，这标志着无线电源特性的潜在改进。我们基于ALMA的Cycle 5.3天线设置，在使用CASA工具simalma模拟的10164幅图像上测试了这种方法。我们将条件去噪扩散概率模型（DDPM）应用于天空模型重建，然后使用Photutils确定源坐标和通量，评估模型在不同水汽水平下的性能。我们的方法在源定位方面表现出色，在低至2的信噪比（SNR）下实现了90%以上的完整性。它在通量估计方面也超过了PyBDSF，准确识别了测试集中96%的源的通量，比CLEAN+PyBDSF的57%有了显著改进。条件DDPM是一种强大的图像到图像翻译工具，可以准确而稳健地描述无线电源，并优于现有方法。虽然这项研究强调了它在射电天文学中的巨大应用潜力，但我们也承认它的使用存在某些局限性，为进一步改进和研究提供了方向。 et.al.|[2402.10204](http://arxiv.org/abs/2402.10204)|**[link](https://github.com/mariiadrozdova/diffusion-for-sources-characterisation)**|
|**2024-02-15**|**Tracer dynamics in polymer networks: generalized Langevin description**|聚合物网络和水凝胶中的示踪剂扩散与生物学和技术相关，同时它也构成了波动、非均质软质中分子动力学的一个有趣的模型过程。在这里，我们基于（马尔可夫）隐式溶剂Langevin模拟，系统地研究了聚合物网络中示踪剂的时间依赖动力学和（非马尔可夫）记忆效应。特别是，我们考虑在规则的四功能珠弹簧聚合物网络中高稀释的球形示踪剂溶质，并控制示踪剂网络Lennard-Jones（LJ）相互作用和聚合物密度。基于对记忆（摩擦）核的分析，我们恢复了预期的长时间输运系数，并证明了短时间示踪剂动力学、聚合物波动和粘弹性响应是如何相互关联的。此外，我们拟合了具有阻尼谐波振荡的示踪剂的特征记忆模式，并确定了LJ贡献、键振动和慢网络弛豫，它们以与LJ吸引力几乎线性的比例进入核。该过程为跟踪器内存提出了一种简化的函数形式，允许对内存内核进行方便的插值和外推。这最终导致了利用广义Langevin方程（GLE）的高效模拟，其中聚合物网络充当具有可调谐强度的额外热浴。 et.al.|[2402.10148](http://arxiv.org/abs/2402.10148)|null|
|**2024-02-15**|**Energy Flux Decomposition in Magnetohydrodynamic Turbulence**|在流体动力学（HD）湍流中，已经导出了跨尺度的能量通量的精确分解，其确定了与涡流拉伸和应变自放大相关的贡献（P.Johnson，Phys.Rev.Lett.，124104501（2020），J.Fluid Mech。922、A3（2021））到跨尺度的能量通量。在这里，我们将该方法扩展到一般的耦合平流-扩散方程，特别是均匀磁流体动力学（MHD）湍流，并表明几个亚通量通过类似于HD中的Betchov关系的运动学约束相互关联。应用于直接数值模拟的数据，这种分解可以识别物理过程，量化它们对能量级联的各自贡献，并通过进一步分解为单尺度和多尺度项来定量评估它们的多尺度性质。我们发现，与HD相比，MHD中的涡旋拉伸被强烈消耗，动能从大尺度转移到小尺度，几乎完全是通过洛伦兹力引起的小规模强应变区域的产生。在大应变区域，电流片通过大规模应变运动拉伸到磁剪切区域。这种磁剪切反过来驱动较小规模的伸展流。磁能从大尺度转移到小尺度，尽管有相当大的反向散射，主要是通过上述高应变区域的电流片变薄，而电流丝拉伸（类似于涡流拉伸）的贡献可以忽略不计。讨论了这些结果对亚网格尺度湍流建模的影响。 et.al.|[2402.10125](http://arxiv.org/abs/2402.10125)|null|
|**2024-02-15**|**A Blob Method for Mean Field Control With Terminal Constraints**|在这项工作中，我们为一类具有源和终端约束的一般平均场控制问题开发了一种新的粒子方法。我们考虑的问题的具体例子包括p-Wasserstein度量的动态公式、障碍物周围的最优运输以及受加速度控制的运输测量。与现有的数值方法不同，我们的粒子方法是无网格的，不需要底层成本函数或终端约束的全局知识。我们方法的一个关键特征是一种通过软的非局部近似来强制终端约束的新方法，其灵感来自最近关于扩散方程的blob方法的工作。在伽玛收敛的意义上，我们证明了我们的粒子近似对连续平均场控制问题解的收敛性。我们的结果的一个副产品是将平均场控制问题的现有离散到连续收敛结果扩展到更一般的状态和测量成本，如在建模障碍物周围的运输时出现的，以及更一般的约束集，包括可控线性时不变系统。最后，我们通过数值实现我们的方法并使用它来计算上面讨论的示例问题的解来得出结论。我们对我们的方法的收敛性进行了详细的数值研究，以及它在采样应用和最优传输图近似中的行为。 et.al.|[2402.10124](http://arxiv.org/abs/2402.10124)|null|
|**2024-02-15**|**Collision efficiency of droplets across diffusive, electrostatic and inertial regimes**|雨滴是由在重力作用下降落的亚毫米液滴碰撞而在云中形成的：较大的液滴比较小的液滴落得更快，并在其路径上收集。关于这种雪崩机制，雾和非降水暖云令人费解的稳定性一直是一个长期存在的问题。如何解释直径约为 $10~｛\rm\mu m｝$的液滴碰撞的概率较低，从而抑制了向越来越大的液滴的级联？在这里，我们回顾了文献中提出的动力学机制，并使用开源蒙特卡罗代码定量研究了布朗扩散、静电和重力引起的液滴碰撞的频率，该代码将所有这些因素都考虑在内。当斯托克斯数大于$1$时，惯性对大液滴的气动力起主导作用。当P’clet数小于$1$时，热扩散在小液滴的气动力上占主导地位。我们表明，存在一个大小范围（对于空气中的水滴，通常为$1-10～｛\rm\mu m｝$ ），对于该范围，惯性和布朗扩散都不显著，从而导致碰撞速率的差距。这种影响尤其重要，因为在碰撞前液滴之间会形成润滑膜，其次是长程空气动力学相互作用。两种不同的机制使消失间隙处的润滑力发散规律化：当间隙与空气的平均自由程相当时，润滑膜中向非连续状态的过渡，以及由于液滴表面的剪切而在液滴内部诱导流动。在惯性主导和扩散主导区域之间的间隙中，偶极-偶极静电相互作用成为控制液滴碰撞效率的主要影响因素。 et.al.|[2402.10117](http://arxiv.org/abs/2402.10117)|null|
|**2024-02-15**|**Quantized Embedding Vectors for Controllable Diffusion Language Models**|提高扩散语言模型（DLM）的可控性、可移植性和推理速度是自然语言生成中的一个关键挑战。尽管最近的研究表明，在使用语言模型生成复杂文本方面取得了显著成功，但内存和计算能力仍然非常苛刻，达不到预期，这自然导致模型的可移植性和不稳定性较低。为了缓解这些问题，提出了许多公认的神经网络量化方法。为了进一步增强其独立部署的可移植性，并提高其通过语言困惑评估的稳定性，我们提出了一种新的方法，称为量化嵌入可控扩散语言模型（QE-CDLM）。QE-CDLM建立在最近成功的可控DLM的基础上，通过量化重塑任务特定嵌入空间。这导致了用于生成任务的基于梯度的控制器，并且获得了更稳定的中间潜变量，这自然带来了加速的收敛以及更好的可控性。此外，采用自适应微调方法来减少可调权重。在五个具有挑战性的细粒度控制任务上的实验结果表明，QE-CDLM在质量和可行性方面优于现有方法，实现了更好的困惑性和轻量级的微调。 et.al.|[2402.10107](http://arxiv.org/abs/2402.10107)|null|
|**2024-02-15**|**Classification Diffusion Models**|一个著名的学习数据分布的方法家族依赖于密度比估计（DRE），其中模型被训练为在数据样本和来自某个参考分布的样本之间 $\textit｛分类｝$。这些技术在简单的低维设置中是成功的，但在复杂的高维数据（如图像）上无法获得良好的结果。一种不同的学习分布的方法是去噪扩散模型（DDM），其中模型被训练为$\textit{去噪}$数据样本。这些方法在图像、视频和音频生成方面实现了最先进的结果。在这项工作中，我们提出了$\textit｛分类-扩散模型｝$ （CDMs），这是一种生成技术，它采用了基于去噪的DDMs形式，同时使用了一个分类器来预测添加到干净信号中的噪声量，类似于DRE方法。我们的方法基于这样的观察，即高斯白噪声的MSE最优去噪器可以用用于预测噪声水平的交叉熵最优分类器的梯度来表示。如我们所示，与DDM相比，CDM实现了更好的去噪结果，并在图像生成中产生了至少相当的FID。CDM还能够进行高效的一步精确似然估计，在使用单步的方法中获得最先进的结果。代码可在项目的网页中找到https://shaharYadin.github.io/CDM/ . et.al.|[2402.10095](http://arxiv.org/abs/2402.10095)|null|

<p align=right>(<a href=#updated-on-20240217>back to top</a>)</p>

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
|**2024-01-17**|**Reproducibility via neural fields of visual illusions induced by localized stimuli**|本文研究了Billock和Tsou[PNAS，2007]使用Amari型神经场的可控性对初级视皮层（V1）的皮层活动进行建模的实验复制，重点关注中央凹或外周视野中的规则漏斗模式。其目的是理解和模拟在这些实验中观察到的视觉现象，强调其非线性性质。这项研究包括设计模拟Billock和Tsou实验中视觉刺激的感官输入。然后从理论和数值上研究这些输入引起的后图像，以确定它们复制实验观察到的视觉效果的能力。这项研究的一个关键方面是研究神经反应的非线性性质所引起的影响。特别是，通过强调兴奋性和抑制性神经元在某些视觉现象出现中的重要性，这项研究表明，这两种类型的神经元活动的相互作用在视觉过程中发挥着重要作用，挑战了后者主要由兴奋性活动单独驱动的假设。 et.al.|[2401.09108](http://arxiv.org/abs/2401.09108)|null|
|**2024-01-12**|**Motion2VecSets: 4D Latent Vector Set Diffusion for Non-rigid Shape Reconstruction and Tracking**|我们介绍了Motion2VecSets，这是一种用于从点云序列进行动态曲面重建的4D扩散模型。虽然现有的最先进的方法已经证明在使用神经场表示重建非刚性对象方面取得了成功，但传统的前馈网络遇到了来自噪声、部分或稀疏点云的模糊观测的挑战。为了应对这些挑战，我们引入了一种扩散模型，该模型通过压缩潜在表示的迭代去噪过程来显式学习非刚性对象的形状和运动分布。当处理模糊输入时，基于扩散的先验能够进行更合理和概率的重建。我们用潜在向量集参数化4D动力学，而不是使用全局潜在。这种新颖的4D表示使我们能够学习局部表面形状和变形模式，从而实现更准确的非线性运动捕捉，并显著提高对看不见的运动和身份的可推广性。对于更具时间连贯性的目标跟踪，我们同步地对变形潜集进行去噪，并在多个帧之间交换信息。为了避免计算开销，我们设计了一个交错的空间和时间注意力块，以沿着空间和时间域交替聚集变形潜伏期。与最先进的方法进行了广泛的比较，证明了我们的Motion2VenSets在从各种不完美的观测进行4D重建方面的优势，特别是在从DeformingThings4D Animals数据集上的稀疏点云重建看不见的个体方面，与CaDex相比，交集优于并集（IoU）提高了19%。更多详细信息，请访问https://vveicao.github.io/projects/Motion2VecSets/. et.al.|[2401.06614](http://arxiv.org/abs/2401.06614)|null|
|**2024-01-05**|**Denoising Vision Transformers**|我们深入研究了视觉转换器（ViTs）固有的一个细微但重大的挑战：这些模型的特征图显示出网格状的伪影，这对ViTs在下游任务中的性能造成了不利影响。我们的研究将这个基本问题追溯到输入阶段的位置嵌入。为了解决这一问题，我们提出了一种新的噪声模型，该模型普遍适用于所有的ViT。具体来说，噪声模型将ViT输出分解为三个部分：一个没有噪声伪影的语义术语和两个以像素位置为条件的伪影相关术语。这种分解是通过在每幅图像的基础上加强与神经场的交叉视图特征一致性来实现的。这种逐图像优化过程从原始ViT输出中提取无伪影特征，为离线应用程序提供干净的特征。扩大了我们的解决方案的范围，以支持在线功能，我们引入了一种可学习的去噪器，直接从未处理的ViT输出中预测无伪影特征，这显示出对新数据的显著泛化能力，而无需对每张图像进行优化。我们的两阶段方法，称为去噪视觉转换器（DVT），不需要重新训练现有的预先训练的ViT，并且立即适用于任何基于转换器的架构。我们在各种具有代表性的ViT（DINO、MAE、DeiT III、EVA02、CLIP、DINOv2、DINOv2-reg）上评估了我们的方法。广泛的评估表明，我们的DVT在多个数据集（例如+3.84mIoU）的语义和几何任务中持续显著地改进了现有的最先进的通用模型。我们希望我们的研究将鼓励对ViT设计进行重新评估，特别是关于位置嵌入的天真使用。 et.al.|[2401.02957](http://arxiv.org/abs/2401.02957)|null|

<p align=right>(<a href=#updated-on-20240217>back to top</a>)</p>

[contributors-shield]: https://img.shields.io/github/contributors/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[contributors-url]: https://github.com/Vincentqyw/cv-arxiv-daily/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[forks-url]: https://github.com/Vincentqyw/cv-arxiv-daily/network/members
[stars-shield]: https://img.shields.io/github/stars/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[stars-url]: https://github.com/Vincentqyw/cv-arxiv-daily/stargazers
[issues-shield]: https://img.shields.io/github/issues/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[issues-url]: https://github.com/Vincentqyw/cv-arxiv-daily/issues

