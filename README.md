[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]

## Updated on 2024.02.14
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
|**2024-02-11**|**BioNeRF: Biologically Plausible Neural Radiance Fields for View Synthesis**|本文介绍了BioNeRF，这是一种生物学上合理的架构，它以3D表示对场景进行建模，并通过辐射场合成新的视图。由于NeRF依赖于网络权重来存储场景的三维表示，BioNeRF实现了一种受认知启发的机制，该机制将来自多个来源的输入融合到类似记忆的结构中，提高了存储容量，并提取了更多内在和相关的信息。BioNeRF还模拟了在锥体细胞中观察到的与上下文信息有关的行为，其中记忆作为上下文提供，并与两个后续神经模型的输入相结合，一个负责产生体积密度，另一个负责渲染场景所用的颜色。实验结果表明，BioNeRF在两个数据集（真实世界图像和合成数据）中对人类感知进行编码的质量测量方面优于最先进的结果。 et.al.|[2402.07310](http://arxiv.org/abs/2402.07310)|null|
|**2024-02-11**|**3D Gaussian as a New Vision Era: A Survey**|3D高斯散射（3D-GS）已成为计算机图形学领域的一个重大进步，它提供了明确的场景表示和新颖的视图合成，而不依赖于神经网络，如神经辐射场（NeRF）。这项技术在机器人、城市地图、自主导航和虚拟现实/增强现实等领域有着不同的应用。鉴于三维高斯散射的日益流行和研究的不断扩展，本文对过去一年的相关论文进行了全面的综述。我们根据特征和应用对分类法进行了调查，介绍了3D高斯飞溅的理论基础。我们通过这项调查的目标是让新的研究人员熟悉3D高斯飞溅，为该领域的开创性工作提供宝贵的参考，并启发未来的研究方向，正如我们的结论部分所讨论的那样。 et.al.|[2402.07181](http://arxiv.org/abs/2402.07181)|null|
|**2024-02-09**|**NCRF: Neural Contact Radiance Fields for Free-Viewpoint Rendering of Hand-Object Interaction**|在三维计算机视觉中，建模手与物体的交互是一项具有根本挑战性的任务。尽管在该领域已经取得了显著的进展，但现有的方法仍然无法真实地合成手与物体的交互照片，因为手与物体之间的严重相互遮挡导致渲染质量下降，以及手与物体姿态估计不准确。为了应对这些挑战，我们提出了一种新的自由视点渲染框架，即神经接触辐射场（NCRF），以从稀疏的视频集重建手与物体的交互。特别地，所提出的NCRF框架由两个关键组件组成：（a）接触优化字段，该字段从3D查询点预测准确的接触字段，以实现手和物体之间的期望接触。（b） 手对象神经辐射场，用于学习静态规范空间中的隐含手对象表示，与专门设计的手对象运动场相一致，以产生观察到的规范对应关系。我们共同学习这些关键组件，它们在视觉和几何约束下相互帮助和规则化，产生高质量的手对象重建，实现照片逼真的新颖视图合成。在HO3D和DexYCB数据集上进行的大量实验表明，我们的方法在渲染质量和姿态估计精度方面都优于当前最先进的方法。 et.al.|[2402.05532](http://arxiv.org/abs/2402.05532)|null|
|**2024-02-07**|**SPAD : Spatially Aware Multiview Diffusers**|我们提出了SPAD，这是一种从文本提示或单个图像创建一致多视图图像的新方法。为了实现多视图生成，我们通过扩展具有跨视图交互的自注意层来重新调整预训练的2D扩散模型的用途，并在Ob厌恶的高质量子集上对其进行微调。我们发现，先前工作中提出的自我关注的天真扩展（例如MVDream）会导致视图之间的内容复制。因此，我们明确地限制了基于核极几何的跨视图注意力。为了进一步增强3D一致性，我们利用从相机射线导出的Plucker坐标，并将其作为位置编码注入。这使得SPAD能够对3D井中的空间接近度进行推理。与最近只能在固定方位角和仰角下生成视图的工作不同，SPAD提供了完整的相机控制，并在Ob厌恶和谷歌扫描对象数据集中对看不见的对象进行新的视图合成方面取得了最先进的结果。最后，我们证明了使用SPAD的文本到3D生成可以防止多面Janus问题。更多详细信息，请访问我们的网页：https://yashkant.github.io/spad et.al.|[2402.05235](http://arxiv.org/abs/2402.05235)|null|
|**2024-02-06**|**EscherNet: A Generative Model for Scalable View Synthesis**|我们介绍了EscherNet，一个用于视图合成的多视图条件扩散模型。EscherNet学习隐含的和生成的3D表示，再加上专门的相机位置编码，允许对任意数量的参考视图和目标视图之间的相机变换进行精确和连续的相对控制。EscherNet在视图合成方面提供了非凡的通用性、灵活性和可扩展性——尽管它使用固定数量的3个参考视图到3个目标视图进行训练，但它可以在单个消费级GPU上同时生成100多个一致的目标视图。因此，EscherNet不仅解决了零样本新视图合成问题，而且自然地将单图像和多图像3D重建相结合，将这些不同的任务组合成一个单一的、有凝聚力的框架。我们的大量实验表明，即使与专门针对每个问题定制的方法相比，EscherNet也能在多个基准测试中实现最先进的性能。这种非凡的多功能性为设计用于3D视觉的可扩展神经结构开辟了新的方向。项目页面：\url{https://kxhit.github.io/EscherNet}. et.al.|[2402.03908](http://arxiv.org/abs/2402.03908)|null|
|**2024-02-06**|**Rig3DGS: Creating Controllable Portraits from Casual Monocular Videos**|从随意的智能手机视频中创建可控的3D人像是非常可取的，因为它们在AR/VR应用中具有巨大的价值。3D高斯散点（3DGS）的最新发展已经显示出在渲染质量和训练效率方面的改进。然而，要从单个视图捕捉中准确地建模和分解头部运动和面部表情，以实现高质量的渲染，仍然是一个挑战。在本文中，我们介绍了Rig3DGS来应对这一挑战。我们在规范空间中使用一组3D高斯表示整个场景，包括动态主体。使用一组控制信号，如头部姿势和表情，我们将它们转换到具有学习变形的3D空间，以生成所需的渲染。我们的关键创新是一种精心设计的变形方法，该方法以从3D可变形模型导出的可学习先验为指导。这种方法在训练中效率很高，在控制各种捕捉的面部表情、头部位置和视图合成方面也很有效。我们通过大量的定量和定性实验证明了我们所学变形的有效性。项目页面位于http://shahrukhathar.github.io/2024/02/05/Rig3DGS.html et.al.|[2402.03723](http://arxiv.org/abs/2402.03723)|null|
|**2024-02-05**|**Denoising Diffusion via Image-Based Rendering**|生成3D场景是一个具有挑战性的开放问题，需要合成在3D空间中完全一致的看似合理的内容。虽然最近的方法（如神经辐射场）擅长于视图合成和3D重建，但由于缺乏生成能力，它们无法在未观察到的区域合成看似合理的细节。相反，现有的生成方法通常无法重建野外的详细、大规模场景，因为它们使用有限容量的3D场景表示，需要对齐的相机姿势，或者依赖于额外的正则化子。在这项工作中，我们介绍了第一个能够快速、详细地重建和生成真实世界3D场景的扩散模型。为了实现这一目标，我们作出了三点贡献。首先，我们引入了一种新的神经场景表示，即IB平面，它可以有效而准确地表示大型3D场景，并根据需要动态分配更多的容量来捕捉每个图像中可见的细节。其次，我们提出了一种去噪扩散框架来学习这种新颖的3D场景表示的先验知识，仅使用2D图像，而不需要任何额外的监督信号，如掩模或深度。这支持在统一架构中进行3D重建和生成。第三，我们开发了一种原则性方法，通过放弃一些图像的表示，在将基于图像的渲染与扩散模型集成时避免琐碎的3D解决方案。我们在真实图像和合成图像的几个具有挑战性的数据集上评估了该模型，并展示了在生成、新视图合成和3D重建方面的卓越结果。 et.al.|[2402.03445](http://arxiv.org/abs/2402.03445)|null|
|**2024-02-07**|**4D Gaussian Splatting: Towards Efficient Novel View Synthesis for Dynamic Scenes**|我们考虑动态场景的新视图合成（NVS）问题。最近的神经方法已经为静态3D场景实现了异常的NVS结果，但对4D时变场景的扩展仍然是不平凡的。先前的工作通常通过学习规范空间加上隐式或显式变形场来编码动力学，这些变形场在突发运动或捕捉高保真渲染等具有挑战性的场景中很困难。在本文中，我们介绍了4D高斯散射（4DGS），这是一种用各向异性4D XYZT高斯表示动态场景的新方法，其灵感来自于3D高斯散射在静态场景中的成功。我们通过对4D高斯进行时间切片来对每个时间戳的动力学进行建模，4D高斯自然构成动态3D高斯，并可以无缝投影到图像中。作为一种明确的时空表示，4DGS展示了对复杂动力学和精细细节建模的强大能力，尤其是对于具有突然运动的场景。我们在高度优化的CUDA加速框架中进一步实现了我们的时间切片和飞溅技术，在RTX 3090 GPU上实现了高达277 FPS的实时推理渲染速度，在RTX4090 GPU上达到了583 FPS的实时推断渲染速度。对不同运动场景的严格评估显示了4DGS的卓越效率和有效性，它在数量和质量上都始终优于现有方法。 et.al.|[2402.03307](http://arxiv.org/abs/2402.03307)|null|
|**2024-02-05**|**ViewFusion: Learning Composable Diffusion Models for Novel View Synthesis**|深度学习为新视图合成的老问题提供了丰富的新方法，从基于神经辐射场（NeRF）的方法到端到端风格的架构。每种方法都有特定的优势，但在适用性方面也有特定的局限性。这项工作介绍了ViewFusion，这是一种最先进的端到端生成新视图合成方法，具有无与伦比的灵活性。ViewFusion包括同时将扩散去噪步骤应用于场景的任意数量的输入视图，然后将为每个视图获得的噪声梯度与（推断的）像素加权掩码相结合，确保对于目标场景的每个区域，只考虑信息量最大的输入视图。我们的方法通过以下方式解决了以前方法的几个局限性：（1）可在多个场景和对象类中进行训练和推广，（2）在训练和测试时自适应地获取可变数量的无姿态视图，（3）即使在严重不确定的条件下也能生成合理的视图（由于其生成性）——同时生成质量与最先进方法不相上下甚至更好的视图。局限性包括没有生成场景的3D嵌入，导致推理速度相对较慢，并且我们的方法仅在相对较小的数据集NMR上进行测试。代码可用。 et.al.|[2402.02906](http://arxiv.org/abs/2402.02906)|**[link](https://github.com/bronemos/view-fusion)**|
|**2024-02-06**|**GaMeS: Mesh-Based Adapting and Modification of Gaussian Splatting**|近年来，已经引入了一系列基于神经网络的图像渲染方法。例如，广泛研究的神经辐射场（NeRF）依赖于神经网络来表示3D场景，从而允许从少量2D图像中合成逼真的视图。然而，大多数NeRF模型都受到长训练和推理时间的限制。相比之下，高斯散射（GS）是一种新颖的、最先进的技术，用于通过高斯分布近似点对图像像素的贡献来渲染3D场景中的点，从而保证快速训练和快速实时渲染。GS的一个缺点是，由于需要对几十万个高斯分量进行调节，因此缺乏定义明确的方法来进行调节。为了解决这个问题，我们引入了高斯网格飞溅（GaMeS）模型，这是网格和高斯分布的混合，它将所有高斯飞溅物固定在物体表面（网格）上。我们的方法的独特贡献是仅根据高斯飞溅在网格上的位置来定义高斯飞溅，从而允许在动画过程中自动调整位置、比例和旋转。因此，我们在实时生成高质量视图的过程中获得了高质量的渲染图。此外，我们证明，在没有预定义网格的情况下，可以在学习过程中微调初始网格。 et.al.|[2402.01459](http://arxiv.org/abs/2402.01459)|**[link](https://github.com/waczjoan/gaussian-mesh-splatting)**|

<p align=right>(<a href=#updated-on-20240214>back to top</a>)</p>

## 3D Reconstruction

|Publish Date|Title|Abstract|PDF|Code|
|---|---|---|---|---|
|**2024-02-13**|**IM-3D: Iterative Multiview Diffusion and Reconstruction for High-Quality 3D Generation**|大多数文本到3D生成器建立在现成的基于数十亿图像训练的文本到图像模型之上。他们使用分数蒸馏采样（SDS）的变体，这是缓慢的，有点不稳定，并且容易出现伪影。一种缓解措施是将2D生成器微调为多视图感知，这可以帮助提取或与重建网络相结合，直接输出3D对象。在本文中，我们进一步探索了文本到三维模型的设计空间。通过考虑视频而不是图像生成器，我们显著改进了多视图生成。结合3D重建算法，通过使用高斯飞溅，可以优化基于图像的鲁棒损失，我们直接从生成的视图中产生高质量的3D输出。我们的新方法IM-3D将2D生成器网络的评估次数减少了10-100x，从而实现了更高效的管道、更好的质量、更少的几何不一致性和更高的可用3D资产收益率。 et.al.|[2402.08682](http://arxiv.org/abs/2402.08682)|null|
|**2024-02-13**|**Camera Calibration through Geometric Constraints from Rotation and Projection Matrices**|相机校准过程包括估计内在和外在参数，这些参数对于准确执行3D重建、物体跟踪和增强现实等任务至关重要。在这项工作中，我们提出了一种新的基于约束的损失，用于测量内在（焦距： $（f_x，f_y）$和主点：$（p_x，p_y）$）和外在（基线：（$b$），视差：（$d$），平移：$（t_x，t_y，t_z）$，以及旋转特别是俯仰：$（\theta_p）$ ）相机参数。我们的新约束基于相机模型固有的几何特性，包括投影矩阵（消失点、世界原点图像、轴平面）的解剖结构和旋转矩阵的正交性。因此，我们通过多任务学习框架提出了一种新的无监督几何约束损失（UGCL）。我们的方法是一种混合方法，它利用神经网络的学习能力来估计所需的参数以及相机投影矩阵固有的基本数学特性。这种独特的方法不仅增强了模型的可解释性，而且有助于更知情的学习过程。此外，我们还引入了一个新的CVGL相机校准数据集，该数据集具有900多种相机参数配置，包含63600个图像对，这些图像对紧密反映了真实世界的情况。通过在合成数据集和真实世界数据集上进行训练和测试，与最先进的（SOTA）基准相比，我们提出的方法展示了所有参数的改进。代码和更新的数据集可以在这里找到：https://github.com/CVLABLUMS/CVGL-Camera-Calibration et.al.|[2402.08437](http://arxiv.org/abs/2402.08437)|**[link](https://github.com/cvlablums/cvgl-camera-calibration)**|
|**2024-02-09**|**Neural Rendering based Urban Scene Reconstruction for Autonomous Driving**|密集3D重建在自动驾驶中有许多应用，包括自动注释验证、多模式数据增强、为缺乏激光雷达的系统提供地面实况注释，以及提高自动标记的准确性。激光雷达提供了高度准确但稀疏的深度，而相机图像能够估计密集但有噪声的深度，尤其是在远距离。在本文中，我们利用这两种传感器的优势，提出了一种使用神经隐式曲面和辐射场相结合的框架进行多模式3D场景重建的方法。特别是，我们的方法估计密集而准确的3D结构，并基于有符号距离场创建隐式地图表示，该表示可以进一步渲染为RGB图像和深度图。可以从学习的有符号距离场中提取网格，并基于遮挡进行剔除。在使用3D对象检测模型的采样过程中，动态对象被有效地实时过滤。我们展示了具有挑战性的汽车场景的定性和定量结果。 et.al.|[2402.06826](http://arxiv.org/abs/2402.06826)|null|
|**2024-02-07**|**Carousel phase retrieval algorithm for 3D coherent X-ray diffraction imaging**|相干X射线衍射成像（CXDI）是一种独特的技术，通过基于测量的散射强度图执行计算相位重建程序，可以以纳米级分辨率重建2D和3D物体。重建过程可能具有高计算复杂度，并且通常不能在实验期间实时执行。我们提出了一种转盘相位检索算法（CPRA），该算法基于傅立叶切片定理将3D重建问题表示为对应于不同收集角度的投影图像的一组2D重建。为了保持2D重建之间的一致性，我们引入了一种迭代过程，其中每个2D重建都以周期性（旋转）的方式基于相邻的2D重建。2D重建的使用大大减少了计算时间和内存消耗。我们展示了在CPU和GPU计算架构上针对各种空间大小的复杂生物细胞的测试问题的CPRA实现。与传统的CXDI重建算法相比，CPRA在GPU上表现出300倍的速度，在CPU上表现出120倍的速度。CPRA还可以实现更高的重建质量。所实现的速度允许实时对计算上较大的对象进行高分辨率重建。 et.al.|[2402.05283](http://arxiv.org/abs/2402.05283)|**[link](https://github.com/UCSD-CEM/Carousel-Phase-Retrieval-Algorithm)**|
|**2024-02-07**|**Scalable Multi-view Clustering via Explicit Kernel Features Maps**|人们越来越意识到多视图学习是数据科学和机器学习的重要组成部分，这是多视图在现实世界应用中越来越普遍的结果，尤其是在网络环境中。在本文中，我们介绍了一种新的多视图子空间聚类的可扩展性框架。提出了一种有效的优化策略，利用核特征图来减少计算负担，同时保持良好的聚类性能。该算法的可扩展性意味着它可以在几分钟内使用标准机器应用于大规模数据集，包括具有数百万数据点的数据集。我们在不同规模的真实世界基准网络上进行了广泛的实验，以评估我们的算法相对于最先进的多视图子空间聚类方法和属性网络多视图方法的性能。 et.al.|[2402.04794](http://arxiv.org/abs/2402.04794)|null|
|**2024-02-06**|**EscherNet: A Generative Model for Scalable View Synthesis**|我们介绍了EscherNet，一个用于视图合成的多视图条件扩散模型。EscherNet学习隐含的和生成的3D表示，再加上专门的相机位置编码，允许对任意数量的参考视图和目标视图之间的相机变换进行精确和连续的相对控制。EscherNet在视图合成方面提供了非凡的通用性、灵活性和可扩展性——尽管它使用固定数量的3个参考视图到3个目标视图进行训练，但它可以在单个消费级GPU上同时生成100多个一致的目标视图。因此，EscherNet不仅解决了零样本新视图合成问题，而且自然地将单图像和多图像3D重建相结合，将这些不同的任务组合成一个单一的、有凝聚力的框架。我们的大量实验表明，即使与专门针对每个问题定制的方法相比，EscherNet也能在多个基准测试中实现最先进的性能。这种非凡的多功能性为设计用于3D视觉的可扩展神经结构开辟了新的方向。项目页面：\url{https://kxhit.github.io/EscherNet}. et.al.|[2402.03908](http://arxiv.org/abs/2402.03908)|null|
|**2024-02-06**|**Efficient Generation of Hidden Outliers for Improved Outlier Detection**|异常值生成是一种常用的技术，用于解决重要的异常值检测任务。生成具有现实行为的异常值具有挑战性。现有的流行方法往往忽略高维空间中异常值的“多视图”特性。对这一财产进行核算的唯一现有方法在效率和有效性方面不足。我们提出了BISECT，这是一种新的异常值生成方法，可以创建模拟上述属性的真实异常值。为此，BISECT采用了本文中介绍的一个新颖命题，说明如何有效地生成所述现实异常值。我们的方法比当前重建“多个视图”的方法有更好的保证和复杂性。我们使用BISECT生成的合成异常值来有效地增强不同数据集中的异常值检测，用于多种用例。例如，与基线相比，BISECT的过采样将误差减少了3倍。 et.al.|[2402.03846](http://arxiv.org/abs/2402.03846)|**[link](https://github.com/jcribeiro98/bisect)**|
|**2024-02-09**|**MoD-SLAM: Monocular Dense Mapping for Unbounded 3D Scene Reconstruction**|神经隐式表示最近已经在许多领域得到了证明，包括同时定位和映射（SLAM）。目前的神经SLAM在重建有界场景时可以获得理想的结果，但这依赖于RGB-D图像的输入。仅基于RGB图像的基于神经的SLAM无法准确地重建场景的尺度，而且由于跟踪过程中积累的误差，它还存在尺度漂移。为了克服这些限制，我们提出了MoD SLAM，这是一种单目密集映射方法，允许在无界场景中实时进行全局姿态优化和3D重建。通过单目深度估计优化场景重建，并使用闭环检测更新相机姿态，可以在大型场景上进行详细而精确的重建。与以前的工作相比，我们的方法更加健壮、可扩展和通用。我们的实验表明，与现有的神经SLAM方法相比，MoD-SLAM具有更出色的映射性能，尤其是在大型无边界场景中。 et.al.|[2402.03762](http://arxiv.org/abs/2402.03762)|null|
|**2024-02-05**|**Denoising Diffusion via Image-Based Rendering**|生成3D场景是一个具有挑战性的开放问题，需要合成在3D空间中完全一致的看似合理的内容。虽然最近的方法（如神经辐射场）擅长于视图合成和3D重建，但由于缺乏生成能力，它们无法在未观察到的区域合成看似合理的细节。相反，现有的生成方法通常无法重建野外的详细、大规模场景，因为它们使用有限容量的3D场景表示，需要对齐的相机姿势，或者依赖于额外的正则化子。在这项工作中，我们介绍了第一个能够快速、详细地重建和生成真实世界3D场景的扩散模型。为了实现这一目标，我们作出了三点贡献。首先，我们引入了一种新的神经场景表示，即IB平面，它可以有效而准确地表示大型3D场景，并根据需要动态分配更多的容量来捕捉每个图像中可见的细节。其次，我们提出了一种去噪扩散框架来学习这种新颖的3D场景表示的先验知识，仅使用2D图像，而不需要任何额外的监督信号，如掩模或深度。这支持在统一架构中进行3D重建和生成。第三，我们开发了一种原则性方法，通过放弃一些图像的表示，在将基于图像的渲染与扩散模型集成时避免琐碎的3D解决方案。我们在真实图像和合成图像的几个具有挑战性的数据集上评估了该模型，并展示了在生成、新视图合成和3D重建方面的卓越结果。 et.al.|[2402.03445](http://arxiv.org/abs/2402.03445)|null|
|**2024-02-02**|**Di-NeRF: Distributed NeRF for Collaborative Learning with Unknown Relative Poses**|未知环境的协作映射可以比单个机器人更快、更稳健地完成。然而，协作方法需要一个可扩展的分布式范式来处理通信问题。这项工作提出了一种全分布式算法，使一组机器人能够共同优化神经辐射场（NeRF）的参数。该算法涉及每个机器人训练的NeRF参数在网状网络上的通信，在网状网络中，每个机器人训练其NeRF，并且只能访问自己的视觉数据。此外，所有机器人的相对姿态都与模型参数一起进行了联合优化，从而能够使用未知的相对相机姿态进行映射。我们证明了多机器人系统可以受益于从多个NeRF优化的可微分和鲁棒的3D重建。在真实世界和合成数据上的实验证明了所提出的算法的有效性。实验视频和补充材料见项目网站(https://sites.google.com/view/di-nerf/home). et.al.|[2402.01485](http://arxiv.org/abs/2402.01485)|null|

<p align=right>(<a href=#updated-on-20240214>back to top</a>)</p>

## Diffusion

|Publish Date|Title|Abstract|PDF|Code|
|---|---|---|---|---|
|**2024-02-13**|**IM-3D: Iterative Multiview Diffusion and Reconstruction for High-Quality 3D Generation**|大多数文本到3D生成器建立在现成的基于数十亿图像训练的文本到图像模型之上。他们使用分数蒸馏采样（SDS）的变体，这是缓慢的，有点不稳定，并且容易出现伪影。一种缓解措施是将2D生成器微调为多视图感知，这可以帮助提取或与重建网络相结合，直接输出3D对象。在本文中，我们进一步探索了文本到三维模型的设计空间。通过考虑视频而不是图像生成器，我们显著改进了多视图生成。结合3D重建算法，通过使用高斯飞溅，可以优化基于图像的鲁棒损失，我们直接从生成的视图中产生高质量的3D输出。我们的新方法IM-3D将2D生成器网络的评估次数减少了10-100x，从而实现了更高效的管道、更好的质量、更少的几何不一致性和更高的可用3D资产收益率。 et.al.|[2402.08682](http://arxiv.org/abs/2402.08682)|null|
|**2024-02-13**|**Chain Reaction of Ideas: Can Radioactive Decay Predict Technological Innovation?**|这项工作展示了受放射性衰变启发的出生-死亡马尔可夫过程的应用，以捕捉创新过程的动力学。利用Bass扩散模型，我们导出了一个类似Gompertz的函数来解释长期创新趋势。我们的模型的有效性通过引用数据、谷歌趋势和递归神经网络得到了证实，该网络也揭示了短期波动。通过自动机模型进行的进一步分析表明，这些波动可能源于底层物理的固有随机性。 et.al.|[2402.08681](http://arxiv.org/abs/2402.08681)|null|
|**2024-02-13**|**Target Score Matching**|去噪分数匹配通过最小化回归损失来估计目标分布的噪声版本的分数，并被广泛用于训练流行的去噪扩散模型。然而，去噪分数匹配的一个众所周知的限制是，它在低噪声水平下产生对分数的较差估计。这个问题对于物理科学中的问题和已知干净原始目标的分数的蒙特卡罗采样任务特别不利。直观地说，在这种情况下，估计目标的轻微噪声版本的分数应该是一项简单的任务。在本文中，我们解决了这一缺点，并表明利用目标分数的知识确实是可能的。我们提出了目标分数同一性和相应的目标分数匹配回归损失，这使我们能够获得在低噪声水平下承认有利特性的分数估计。 et.al.|[2402.08667](http://arxiv.org/abs/2402.08667)|null|
|**2024-02-13**|**Learning Continuous 3D Words for Text-to-Image Generation**|当前用于图像生成的对扩散模型的控制（例如，通过文本或ControlNet）在识别抽象、连续的属性（如照明方向或非刚性形状变化）方面存在不足。在本文中，我们提出了一种方法，允许文本到图像模型的用户对图像中的几个属性进行细粒度控制。我们通过设计特殊的输入标记集来实现这一点，这些标记集可以以连续的方式进行转换——我们称之为连续的3D单词。例如，这些属性可以表示为滑块，并与文本提示一起应用，以实现对图像生成的细粒度控制。仅在给定单个网格和渲染引擎的情况下，我们展示了我们的方法可以用于对几个3D感知属性提供连续的用户控制，包括一天中的时间照明、鸟翼方向、玩偶空间效果和对象姿势。我们的方法能够同时用多个连续的3D单词和文本描述来调节图像创建，同时不增加生成过程的开销。项目页面：https://ttchengab.github.io/continuous_3d_words et.al.|[2402.08654](http://arxiv.org/abs/2402.08654)|null|
|**2024-02-13**|**Clustering of primordial black holes from quantum diffusion during inflation**|我们研究了在膨胀过程中存在量子扩散的情况下，大的波动是如何在空间上相互关联的。这是通过计算随机- $\delta N$形式的实空间相关函数来实现的。我们首先推导了由局部观测者在充气结束时测量的物理距离的精确描述，改进了以前的工作。我们的方法基于递归算法方法，该方法始终包括体积加权效应。然后我们建议“大体积”近似，在此近似下，仅使用首次通过时间分析即可进行计算，并由此导出随机膨胀中功率谱的新公式。然后，我们研究了曲率扰动的完全两点统计。由于存在指数尾，我们发现大波动的联合分布形式为$P（\zeta_{R_1}，\zeta_{R_2}）=F（R_1，R_2，R）P。这意味着，在尾部，被定义为$P（\zeta_{R_1}>\zeta_｛\rm｛c｝｝，\zeta_2｝>\zeta｛\rm{c｝）/[P（\zeta_{R_1｝>\zeta_｛\rm{c｝｝）P（\zeta_2｝>\zeta_｛\ rm｛c｝）]-1$的缩减相关函数与阈值$\zeta_5｛\rm｛c}｝$无关。这与高斯统计形成对比，在高斯统计中，相同的量随着$\zeta_{\rm{c}}$ 强烈衰减，并表明对于在指数尾中形成的所有结构都存在普遍的聚类轮廓。在中间（即还不是指数）尾部形成的结构可能具有不同的、依赖于模型的行为。 et.al.|[2402.08642](http://arxiv.org/abs/2402.08642)|null|
|**2024-02-13**|**Latent Inversion with Timestep-aware Sampling for Training-free Non-rigid Editing**|文本引导的非刚性编辑涉及对输入图像的复杂编辑，例如改变其周围环境中的运动或构图。由于需要操纵输入结构，现有的方法通常难以保留对象身份和背景，尤其是与稳定扩散相结合时。在这项工作中，我们提出了一种使用稳定扩散进行非刚性编辑的无训练方法，旨在提高身份保存质量而不影响可编辑性。我们的方法包括三个阶段：文本优化、潜在反转和时间步长感知的文本注入采样。受Imagic最近成功的启发，我们采用了他们的文本优化来进行平滑编辑。然后，我们引入潜在反转来保持输入图像的同一性，而不需要额外的模型微调。为了充分利用潜在反转的输入重建能力，我们建议使用时间步长感知的文本注入采样。这通过在早期采样步骤中注入源文本提示，然后在后续采样步骤中转换到目标提示，有效地保留了输入图像的结构。这种战略方法与文本优化无缝协调，便于在不丢失原始身份的情况下对输入进行复杂的非刚性编辑。我们通过大量的实验证明了我们的方法在身份保存、可编辑性和美学质量方面的有效性。 et.al.|[2402.08601](http://arxiv.org/abs/2402.08601)|null|
|**2024-02-13**|**Denoising Diffusion Restoration Tackles Forward and Inverse Problems for the Laplace Operator**|扩散模型已经成为一类很有前途的生成模型，它将噪声输入映射到真实图像。最近，它们被用于生成偏微分方程（PDE）的解。然而，他们仍然难以解决拉普拉斯算子中的反问题，例如泊松方程，因为大幅度的本征值放大了测量噪声。本文提出了一种新的方法，通过使用去噪扩散恢复模型（DDRM）来求解偏微分方程的逆解和正解。DDRM被用于线性逆问题，通过利用线性算子的奇异值分解（SVD）来恢复原始的干净信号。等效地，我们提出了一种通过利用拉普拉斯算子的本征值和本征函数来恢复泊松方程中的解和参数的方法。我们的结果表明，使用去噪扩散恢复显著提高了对解和参数的估计。因此，我们的研究开创了将扩散模型与底层物理原理相结合来解决偏微分方程的先河。 et.al.|[2402.08563](http://arxiv.org/abs/2402.08563)|null|
|**2024-02-13**|**Confronting Reward Overoptimization for Diffusion Models: A Perspective of Inductive and Primacy Biases**|弥合扩散模型和人类偏好之间的差距对于将其融入实际的生成工作流至关重要。虽然优化下游奖励模型已成为一种很有前途的调整策略，但人们担心使用学习的奖励模型进行过度优化的风险，这可能会损害基本事实的性能。在这项工作中，我们通过归纳偏差和首要偏差的视角来面对扩散模型对齐中的奖励过度优化问题。我们首先将当前方法与扩散模型的多步骤去噪过程中固有的时间归纳偏差的差异确定为过度优化的潜在来源。然后，我们惊讶地发现，在我们的批评者模型中，休眠神经元起到了防止过度优化的正则化作用，而活跃神经元反映了这种情况下的首要偏差。受这些观察结果的启发，我们提出了具有临界主动神经元重置的时间扩散策略优化（TDPO-R），这是一种利用中间时间步长的时间诱导偏差的策略梯度算法，以及一种针对主动神经元以抵消首要偏误的新重置策略。经验结果表明，我们的算法在缓解奖励过度优化方面具有卓越的功效。 et.al.|[2402.08552](http://arxiv.org/abs/2402.08552)|null|
|**2024-02-13**|**Branching Interval Partition Diffusions**|我们引入并研究分支区间配分扩散的自然一般性。我们让区间宽度根据一般的实数扩散独立地演化，仅受确保区间的有限寿命并允许连续生成新区间的条件的约束。后者由实值扩散的Pitman-Yor漂移测度和相关的谱正L\’evy过程控制，以对这些漂移及其开始时间进行排序。这概括了Forman、Pal、Rizzolo和Winkel先前关于自相似情况的工作，并提出了一类新的一般Markovian齐次Crump Mode Jagers型分支过程，其特征在其寿命期间扩散变化。 et.al.|[2402.08548](http://arxiv.org/abs/2402.08548)|null|
|**2024-02-13**|**Hyperballistic transport in dense ionized matter under external AC electric fields**|Langevin方程广泛用于等离子体和尘埃等离子体的数值模拟。然而，当系统受到外部AC电场时，通常的白噪声假设变得不成立。这是因为等离子体中为粒子传输提供热浴的带电粒子本身对AC场作出响应，并且热噪声是场相关的且非马尔可夫的。我们通过适当考虑AC场对热浴统计的影响，从理论上研究了在外部AC电场下，浸入作为热浴的带电粒子的稠密等离子体中的标记带电粒子的Langevin传输模型中的粒子扩散率。我们解析地导出了不同初始条件下的含时广义扩散系数 $D（t）$。广义扩散率表现出类似阻尼振荡的行为，具有初始非常大的峰值，其中广义扩散系数相对于无限时间稳态值提高了几个数量级。后者与在没有外部场的情况下的斯托克斯-爱因斯坦扩散率一致。对于初始条件，其中外部场在$t=0$时已经开启，并且系统在直流条件下热化$t\leq 0$，短时行为是超大蒜素的，$MSD\sim t^4$ （其中MSD是均方位移），导致粒子输运的巨大增强。最后，该理论阐明了介质极化对局部洛伦兹场的作用，并允许估计由于周围电荷的极化而产生的有效电荷。 et.al.|[2402.08519](http://arxiv.org/abs/2402.08519)|null|

<p align=right>(<a href=#updated-on-20240214>back to top</a>)</p>

## NeRF

|Publish Date|Title|Abstract|PDF|Code|
|---|---|---|---|---|
|**2024-02-12**|**Unsupervised Discovery of Object-Centric Neural Fields**|我们研究从单个图像中推断3D以对象为中心的场景表示。虽然最近的方法在从简单的合成图像中无监督地发现3D对象方面显示出了潜力，但它们未能推广到具有视觉丰富和多样化对象的真实世界场景。这种限制源于它们的对象表示，它将对象的内在属性（如形状和外观）与外在的、以观察者为中心的属性（如3D位置）纠缠在一起。为了解决这一瓶颈，我们提出了以对象为中心的神经场的无监督发现（uOCF）。uOCF专注于学习对象的内在，并分别对外在进行建模。我们的方法显著提高了系统泛化能力，从而能够从稀疏的真实世界图像中无监督地学习高保真的以对象为中心的场景表示。为了评估我们的方法，我们收集了三个新的数据集，包括两个真实的厨房环境。大量实验表明，uOCF能够在无监督的情况下从单个真实图像中发现视觉丰富的对象，从而实现3D对象分割和场景操作等应用。值得注意的是，uOCF演示了对单个真实图像中看不见的物体的零样本泛化。项目页面：https://red-fairy.github.io/uOCF/ et.al.|[2402.07376](http://arxiv.org/abs/2402.07376)|null|
|**2024-02-06**|**Improved Generalization of Weight Space Networks via Augmentations**|在深度权重空间（DWS）中学习，神经网络处理其他神经网络的权重，是一个新兴的研究方向，应用于2D和3D神经领域（INRs、NeRFs），以及对其他类型的神经网络进行推断。不幸的是，权重空间模型往往存在严重的过拟合问题。我们实证分析了这种过拟合的原因，发现一个关键原因是DWS数据集缺乏多样性。虽然给定的对象可以用许多不同的权重配置来表示，但典型的INR训练集无法捕捉表示同一对象的INR之间的可变性。为了解决这一问题，我们探索了在权重空间中增加数据的策略，并提出了一种适用于权重空间的MixUp方法。我们在两个设置中展示了这些方法的有效性。在分类方面，它们可以提高性能，类似于拥有10倍以上的数据。在自我监督的对比学习中，它们在下游分类中产生了5-10%的显著收益。 et.al.|[2402.04081](http://arxiv.org/abs/2402.04081)|null|
|**2024-01-31**|**BlockFusion: Expandable 3D Scene Generation using Latent Tri-plane Extrapolation**|我们介绍了BlockFusion，这是一种基于扩散的模型，它将3D场景生成为单元块，并无缝地合并新的块来扩展场景。BlockFusion使用从完整的3D场景网格中随机裁剪的3D块的数据集进行训练。通过逐块拟合，所有训练块都被转换为混合神经场：具有包含几何特征的三平面，然后是用于解码有符号距离值的多层感知器（MLP）。采用变分自动编码器将三平面压缩到潜在的三平面空间中，在该空间上进行去噪扩散处理。应用于潜在表示的扩散允许高质量和多样化的3D场景生成。要在生成过程中扩展场景，只需附加空块以与当前场景重叠，并外推现有的潜在三平面以填充新块。外推是通过在去噪迭代过程中使用来自重叠三平面的特征样本来调节生成过程来完成的。潜在的三平面外推法产生语义和几何上有意义的过渡，与现有场景和谐融合。2D布局调节机制用于控制场景元素的放置和布置。实验结果表明，BlockFusion能够在室内和室外场景中生成具有前所未有的高质量形状的多样化、几何一致和无边界的大型3D场景。 et.al.|[2401.17053](http://arxiv.org/abs/2401.17053)|null|
|**2024-01-26**|**Learning Neural Radiance Fields of Forest Structure for Scalable and Fine Monitoring**|这项工作利用神经辐射场和遥感技术用于林业应用。在这里，我们展示了神经辐射场为改进森林监测中现有的遥感方法提供了广泛的可能性。我们提出的实验证明了它们的潜力：（1）表达森林三维结构的精细特征，（2）融合可用的遥感模式，（3）改进三维结构衍生的森林指标。总之，这些特性使神经场成为一种有吸引力的计算工具，具有进一步提高森林监测程序的可扩展性和准确性的巨大潜力。 et.al.|[2401.15029](http://arxiv.org/abs/2401.15029)|null|
|**2024-01-25**|**Learning Robust Generalizable Radiance Field with Visibility and Feature Augmented Point Representation**|本文介绍了广义神经辐射场（NeRF）的一种新范式。以前的通用NeRF方法将多视点立体技术与基于图像的神经渲染相结合进行泛化，产生了令人印象深刻的结果，同时存在三个问题。首先，遮挡常常导致不一致的特征匹配。然后，由于采样点和粗略特征聚合的单独过程，它们在几何不连续性和局部尖锐形状中传递失真和伪影。第三，当源视图离目标视图不够近时，它们基于图像的表示会发生严重退化。为了应对挑战，我们提出了第一个基于点而不是基于图像的渲染构建可泛化神经场的范式，我们称之为可泛化神经点场（GPF）。我们的方法通过几何先验显式地建模可见性，并用神经特征增强它们。我们提出了一种新的非均匀对数采样策略，以提高渲染速度和重建质量。此外，我们提出了一种可学习的内核，该内核在空间上增加了用于特征聚合的特征，减轻了几何结构急剧变化的地方的失真。此外，我们的表现很容易被操纵。实验表明，在泛化和微调设置中，我们的模型可以在三个数据集上提供比所有对应模型和基准更好的几何结构、视图一致性和渲染质量，初步证明了可泛化NeRF新范式的潜力。 et.al.|[2401.14354](http://arxiv.org/abs/2401.14354)|null|
|**2024-01-24**|**Unified neural field theory of brain dynamics underlying oscillations in Parkinson's disease and generalized epilepsies**|通过皮质丘脑基底神经节（CTBG）系统的神经场模型，联合探讨了帕金森病（PD）和全身性癫痫的病理同步神经振荡的机制。基底神经节（BG）被近似为一个单一的有效群体，并分析了它们在调节振荡皮质丘脑（CT）动力学中的作用，反之亦然。除了正常的脑电图节律外，模型中还存在4 Hz和20 Hz左右的增强活动，这与PD的特征频率一致。这些节律是由BG和CT人群之间回路中的共振引起的，类似于先前CT模型中潜在的癫痫振荡。多巴胺耗竭被认为削弱了对PD中这些共振的抑制，网络连接解释了在4-8Hz和20Hz左右BG、丘脑和皮层活动之间的显著一致性。丘脑网状核（TRN）和BG的传入和传出连接位点之间的相似性预测低多巴胺对应于强直-阵挛（大发作）癫痫发作的可能性降低，这与实验结果一致。此外，该模型预测，与实验结果相匹配的低多巴胺水平会增加缺席（轻微）癫痫发作的可能性。与其他CTBG建模研究一致，当传入和传出BG与CT系统的连接增强时，表现出对缺席发作活动的抑制。BG被证明在强直-阵挛发作状态附近抑制CTBG系统的活性，从而深入了解BG回路中目前治疗的疗效。TRN的睡眠状态也被发现可以抑制病理性PD活动匹配观察。总的来说，这些发现证明了广泛性癫痫和帕金森病的相干振荡之间有很强的相似性，并为可能的合并症提供了见解。 et.al.|[2401.13467](http://arxiv.org/abs/2401.13467)|null|
|**2024-01-17**|**Reproducibility via neural fields of visual illusions induced by localized stimuli**|本文研究了Billock和Tsou[PNAS，2007]使用Amari型神经场的可控性对初级视皮层（V1）皮层活动进行建模的实验复制，重点关注中央凹或外周视野中的规则漏斗模式。其目的是理解和模拟在这些实验中观察到的视觉现象，强调其非线性性质。这项研究包括设计模拟Billock和Tsou实验中视觉刺激的感官输入。然后从理论和数值上研究这些输入引起的后图像，以确定它们复制实验观察到的视觉效果的能力。这项研究的一个关键方面是研究神经反应的非线性性质所引起的影响。特别是，通过强调兴奋性和抑制性神经元在某些视觉现象出现中的重要性，这项研究表明，这两种类型的神经元活动的相互作用在视觉过程中发挥着重要作用，挑战了后者主要由兴奋性活动单独驱动的假设。 et.al.|[2401.09108](http://arxiv.org/abs/2401.09108)|null|
|**2024-01-12**|**Motion2VecSets: 4D Latent Vector Set Diffusion for Non-rigid Shape Reconstruction and Tracking**|我们介绍了Motion2VecSets，这是一种用于从点云序列进行动态曲面重建的4D扩散模型。虽然现有的最先进的方法已经证明在使用神经场表示重建非刚性对象方面取得了成功，但传统的前馈网络遇到了来自噪声、部分或稀疏点云的模糊观测的挑战。为了应对这些挑战，我们引入了一种扩散模型，该模型通过压缩潜在表示的迭代去噪过程来显式学习非刚性对象的形状和运动分布。当处理模糊输入时，基于扩散的先验能够进行更合理和概率的重建。我们用潜在向量集参数化4D动力学，而不是使用全局潜在。这种新颖的4D表示使我们能够学习局部表面形状和变形模式，从而实现更准确的非线性运动捕捉，并显著提高对看不见的运动和身份的可推广性。对于更具时间连贯性的目标跟踪，我们同步地对变形潜集进行去噪，并在多个帧之间交换信息。为了避免计算开销，我们设计了一个交错的空间和时间注意力块，以沿着空间和时间域交替聚集变形潜伏期。与最先进的方法进行了广泛的比较，证明了我们的Motion2VenSets在从各种不完美的观测进行4D重建方面的优势，特别是在从DeformingThings4D Animals数据集上的稀疏点云重建看不见的个体方面，与CaDex相比，交集优于并集（IoU）提高了19%。更多详细信息，请访问https://vveicao.github.io/projects/Motion2VecSets/. et.al.|[2401.06614](http://arxiv.org/abs/2401.06614)|null|
|**2024-01-05**|**Denoising Vision Transformers**|我们深入研究了视觉转换器（ViTs）固有的一个细微但重大的挑战：这些模型的特征图显示出网格状的伪影，这对ViTs在下游任务中的性能造成了不利影响。我们的研究将这个基本问题追溯到输入阶段的位置嵌入。为了解决这一问题，我们提出了一种新的噪声模型，该模型普遍适用于所有的ViT。具体来说，噪声模型将ViT输出分解为三个部分：一个没有噪声伪影的语义术语和两个以像素位置为条件的伪影相关术语。这种分解是通过在每幅图像的基础上加强与神经场的交叉视图特征一致性来实现的。这种逐图像优化过程从原始ViT输出中提取无伪影特征，为离线应用程序提供干净的特征。扩大了我们的解决方案的范围，以支持在线功能，我们引入了一种可学习的去噪器，直接从未处理的ViT输出中预测无伪影特征，这显示出对新数据的显著泛化能力，而无需对每张图像进行优化。我们的两阶段方法，称为去噪视觉转换器（DVT），不需要重新训练现有的预先训练的ViT，并且立即适用于任何基于转换器的架构。我们在各种具有代表性的ViT（DINO、MAE、DeiT III、EVA02、CLIP、DINOv2、DINOv2-reg）上评估了我们的方法。广泛的评估表明，我们的DVT在多个数据集（例如+3.84mIoU）的语义和几何任务中持续显著地改进了现有的最先进的通用模型。我们希望我们的研究将鼓励对ViT设计进行重新评估，特别是关于位置嵌入的天真使用。 et.al.|[2401.02957](http://arxiv.org/abs/2401.02957)|null|
|**2024-01-01**|**Deblurring 3D Gaussian Splatting**|最近对辐射场的研究为具有照片级真实感渲染质量的新颖视图合成铺平了坚实的道路。然而，它们通常使用神经网络和体积绘制，这两种方法的训练成本很高，并且由于绘制时间长，阻碍了它们在各种实时应用中的广泛使用。最近，人们提出了一种基于3D高斯散射的方法来对3D场景进行建模，并在实时渲染图像的同时实现了显著的视觉质量。然而，如果训练图像模糊，则渲染质量会严重下降。模糊通常是由于镜头散焦、物体运动和相机抖动而产生的，它不可避免地会干扰干净图像的获取。先前的几项研究试图使用神经场从模糊的输入图像中渲染干净清晰的图像。然而，这些工作中的大多数仅设计用于基于体积渲染的神经辐射场，并不直接适用于基于光栅化的3D高斯散射方法。因此，我们提出了一种新的实时去模糊框架，即去模糊3D高斯散点，使用小型多层感知器（MLP）来操纵每个3D高斯的协方差来对场景模糊度进行建模。虽然去模糊的3D高斯飞溅仍然可以享受实时渲染，但它可以从模糊的图像中重建精细和清晰的细节。在该基准上进行了各种实验，结果显示了我们的去模糊方法的有效性。定性结果可在https://benhenryl.github.io/Deblurring-3D-Gaussian-Splatting/ et.al.|[2401.00834](http://arxiv.org/abs/2401.00834)|null|

<p align=right>(<a href=#updated-on-20240214>back to top</a>)</p>

[contributors-shield]: https://img.shields.io/github/contributors/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[contributors-url]: https://github.com/Vincentqyw/cv-arxiv-daily/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[forks-url]: https://github.com/Vincentqyw/cv-arxiv-daily/network/members
[stars-shield]: https://img.shields.io/github/stars/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[stars-url]: https://github.com/Vincentqyw/cv-arxiv-daily/stargazers
[issues-shield]: https://img.shields.io/github/issues/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[issues-url]: https://github.com/Vincentqyw/cv-arxiv-daily/issues

