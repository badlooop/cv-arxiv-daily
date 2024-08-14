[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]

## Updated on 2024.08.14
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
|**2024-08-12**|**Mipmap-GS: Let Gaussians Deform with Scale-specific Mipmap for Anti-aliasing Rendering**|3D高斯散斑（3DGS）因其卓越的渲染效率和高保真度而在新型视图合成中引起了极大的关注。然而，由于来自单尺度训练的不可调表示，训练过的高斯人会遭受严重的缩放退化。尽管一些方法试图通过后处理技术来解决这个问题，例如对基元的选择性渲染或过滤技术，但高斯分布中不涉及特定于尺度的信息。在本文中，我们提出了一种统一的优化方法，通过自调整原始属性（如颜色、形状和大小）和分布（如位置），使高斯分布适应任意尺度。受mipmap技术的启发，我们为目标尺度设计了伪地面真值，并提出了一种尺度一致性制导损失，将尺度信息注入到3D高斯模型中。我们的方法是一个插件模块，适用于任何3DGS模型来解决放大和缩小混叠问题。大量实验证明了我们方法的有效性。值得注意的是，在NeRF合成数据集上，我们的方法在PSNR方面优于3DGS，放大平均为9.25 dB，缩小平均为10.40 dB。 et.al.|[2408.06286](http://arxiv.org/abs/2408.06286)|null|
|**2024-08-12**|**FruitNeRF: A Unified Neural Radiance Field based Fruit Counting Framework**|我们介绍FruitNeRF，这是一个统一的新颖水果计数框架，利用最先进的视图合成方法直接在3D中计数任何水果类型。我们的框架采用单目相机拍摄的一组无序的姿势图像，并在每张图像中分割水果。为了使我们的系统独立于水果类型，我们采用了一个基础模型，为任何水果生成二进制分割掩码。利用RGB和语义两种模态，我们训练了一个语义神经辐射场。通过对隐式果园的均匀体积采样，我们得到了纯果点云。通过在提取的点云上应用级联聚类，我们的方法实现了精确的水果计数。神经辐射场的使用比传统方法（如物体跟踪或光流）具有显著优势，因为计数本身被提升到3D中。我们的方法防止了重复计算水果，避免了计算无关的水果。我们使用真实世界和合成数据集来评估我们的方法。真实世界的数据集由三棵手动计数的苹果树、一个具有一行和地面真实水果位置的基准苹果数据集组成，而合成数据集包括各种水果类型，包括苹果、李子、柠檬、梨、桃和芒果。此外，与U-Net相比，我们使用基础模型评估了水果计数的性能。 et.al.|[2408.06190](http://arxiv.org/abs/2408.06190)|**[link](https://github.com/meyerls/fruitnerf)**|
|**2024-08-12**|**Novel View Synthesis from a Single Image with Pretrained Diffusion Guidance**|最近的3D新颖视图合成（NVS）方法仅限于从新视点生成的以单个对象为中心的场景，并且难以应对复杂的环境。它们通常需要大量的3D数据进行训练，除了训练分布之外缺乏泛化能力。相反，无3D方法可以使用预训练的稳定扩散模型生成复杂、狂野场景的文本控制视图，而无需繁琐的微调，但缺乏相机控制。本文介绍了HawkI++，这是一种能够从单个输入图像生成相机控制视点的方法。HawkI++擅长处理复杂多样的场景，无需额外的3D数据或大量训练。它利用广泛可用的预训练NVS模型进行弱制导，将这些知识整合到3D自由视图合成方法中，以有效地实现所需的结果。我们的实验结果表明，HawkI++在定性和定量评估方面都优于现有模型，在各种场景中以所需的相机角度提供高保真度和一致的新颖视图合成。 et.al.|[2408.06157](http://arxiv.org/abs/2408.06157)|null|
|**2024-08-10**|**Visual SLAM with 3D Gaussian Primitives and Depth Priors Enabling Novel View Synthesis**|传统的基于几何的SLAM系统缺乏密集的3D重建能力，因为它们的数据关联通常依赖于特征对应。此外，基于学习的SLAM系统在实时性能和准确性方面往往不足。平衡实时性能和密集的3D重建能力是一个具有挑战性的问题。在本文中，我们提出了一种实时RGB-D SLAM系统，该系统结合了一种新的视图合成技术——3D高斯散点，用于3D场景表示和姿态估计。该技术利用了具有光栅化的3D高斯散斑的实时渲染性能，并允许通过CUDA实现实时可微优化。我们还支持从3D高斯网格重建显式密集3D重建。为了估计精确的相机姿态，我们采用了一种具有逆优化的旋转-平移解耦策略。这涉及通过基于梯度的优化在几次迭代中迭代更新两者。该过程包括可微分地渲染RGB、深度和轮廓图，并更新相机参数，以最小化现有3D高斯图的光度损失、深度几何损失和可见度损失的组合损失。然而，由于3D高斯分布的多视图不一致性，3D高斯散布（3DGS）难以准确表示曲面，这可能会导致相机姿态估计和场景重建的精度降低。为了解决这个问题，我们利用深度先验作为额外的正则化来强制执行几何约束，从而提高了姿态估计和3D重建的精度。我们还提供了关于公共基准数据集的广泛实验结果，以证明我们提出的方法在姿态精度、几何精度和渲染性能方面的有效性。 et.al.|[2408.05635](http://arxiv.org/abs/2408.05635)|null|
|**2024-08-10**|**PRTGaussian: Efficient Relighting Using 3D Gaussians with Precomputed Radiance Transfer**|我们提出了PRTGaussian，这是一种通过将3D高斯和预计算辐射传输（PRT）相结合而实现的实时可照明的新型视图合成方法。通过将可重新点亮的高斯分布拟合到多视图OLAT数据中，我们的方法实现了实时、自由的视点重新点亮。通过基于高阶球谐函数估计辐射传输，我们在捕获详细的再照明效果和保持计算效率之间实现了平衡。我们采用了一个两阶段的过程：在第一阶段，我们从多视图图像中重建对象的粗略几何形状。在第二阶段，我们用获得的点云初始化3D高斯分布，然后同时细化粗糙几何并学习每个高斯分布的光传输。对合成数据集的广泛实验表明，我们的方法可以为一般对象实现快速高质量的重新照明。代码和数据可在https://github.com/zhanglbthu/PRTGaussian. et.al.|[2408.05631](http://arxiv.org/abs/2408.05631)|**[link](https://github.com/zhanglbthu/prtgaussian)**|
|**2024-08-10**|**Radiance Field Learners As UAV First-Person Viewers**|第一人称视角（FPV）在彻底改变无人机（UAV）的轨迹方面具有巨大的潜力，为复杂建筑结构的导航提供了一条令人振奋的途径。然而，传统的神经辐射场（NeRF）方法面临着每次迭代采样单个点以及需要大量视图进行监督等挑战。无人机视频通过有限的视角和显著的空间尺度变化加剧了这些问题，导致在不同尺度上的细节渲染不足。作为回应，我们引入了FPV NeRF，通过三个关键方面来应对这些挑战：（1）时间一致性。利用时空连续性确保帧之间的无缝一致性；（2） 全球结构。在点采样过程中结合各种全局特征可以保持空间完整性；（3） 本地粒度。采用综合框架和多分辨率监督进行多尺度场景特征表示，解决了无人机视频空间尺度的复杂性。此外，由于公开可用的FPV视频稀缺，我们引入了一种使用NeRF从无人机镜头生成FPV视角的创新视图合成方法，增强了无人机的空间感知。我们的新数据集涵盖了无人机领域从室外到室内的各种轨迹，与传统的NeRF场景有很大不同。通过涵盖内部和外部建筑结构的广泛实验，FPV NeRF展示了对无人机飞行空间的卓越理解，在我们精心策划的无人机数据集中优于最先进的方法。浏览我们的项目页面以获取更多见解：https://fpv-nerf.github.io/. et.al.|[2408.05533](http://arxiv.org/abs/2408.05533)|null|
|**2024-08-09**|**FewShotNeRF: Meta-Learning-based Novel View Synthesis for Rapid Scene-Specific Adaptation**|在这篇论文中，我们通过我们提出的FewShotNeRF方法，解决了用有限的多视图图像生成真实世界对象新视图的挑战。我们的方法利用元学习来获得最佳初始化，促进神经辐射场（NeRF）快速适应特定场景。我们元学习过程的重点是捕捉一个类别中的共享几何体和纹理，并嵌入到权重初始化中。这种方法加快了NeRF的学习过程，并利用位置编码的最新进展来减少将NeRF拟合到场景所需的时间，从而加速了元学习的内环优化。值得注意的是，我们的方法能够对大量3D场景进行元学习，为各种类别建立稳健的3D先验。通过对3D开源数据集中的Common Objects进行广泛评估，我们实证证明了元学习在生成高质量的对象新视图方面的有效性和潜力。 et.al.|[2408.04803](http://arxiv.org/abs/2408.04803)|null|
|**2024-08-08**|**Sampling for View Synthesis: From Local Light Field Fusion to Neural Radiance Fields and Beyond**|捕捉和渲染复杂现实世界场景的新颖视图是计算机图形学和视觉领域的一个长期问题，在增强现实和虚拟现实、沉浸式体验和3D摄影中都有应用。深度学习的出现使这一领域取得了革命性的进步，传统上称为基于图像的渲染。然而，以前的方法需要难以处理的密集视图采样，或者对于用户应该如何采样场景视图以可靠地渲染高质量的新视图提供很少或根本没有指导。局部光场融合提出了一种用于从采样视图的不规则网格进行实际视图合成的算法，该算法首先通过多平面图像场景表示将每个采样视图扩展为局部光场，然后通过混合相邻的局部光场来渲染新的视图。至关重要的是，我们扩展了传统的全光采样理论，得出了一个界限，该界限精确地指定了用户在使用我们的算法时应该对给定场景的视图进行多密集采样。我们实现了奈奎斯特速率视图采样的感知质量，同时使用的视图减少了4000倍。后续的发展为深度学习带来了新的场景表示，特别是神经辐射场，但从少量图像进行稀疏视图合成的问题只会变得越来越重要。我们重申了最近关于稀疏甚至单图像视图合成的一些结果，同时提出了规定采样准则是否适用于新一代基于图像的渲染算法的问题。 et.al.|[2408.04586](http://arxiv.org/abs/2408.04586)|null|
|**2024-08-08**|**Evaluating Modern Approaches in 3D Scene Reconstruction: NeRF vs Gaussian-Based Methods**|本研究探索了神经辐射场（NeRF）和基于高斯的方法在3D场景重建中的能力，将这些现代方法与传统的同步定位和映射（SLAM）系统进行了对比。利用Replica和ScanNet等数据集，我们根据跟踪精度、映射保真度和视图合成来评估性能。研究结果表明，NeRF在视图合成方面表现出色，在从现有数据生成新视角方面提供了独特的能力，尽管处理速度较慢。相反，基于高斯的方法提供了快速的处理和显著的表现力，但缺乏全面的场景完成。通过全局优化和循环闭合技术的增强，NICE-SLAM和SplaTAM等新方法不仅在鲁棒性方面超越了ORB-SLAM2等旧框架，而且在动态和复杂环境中表现出卓越的性能。这种比较分析将理论研究与实际意义联系起来，为各种现实世界应用中鲁棒3D场景重建的未来发展提供了线索。 et.al.|[2408.04268](http://arxiv.org/abs/2408.04268)|null|
|**2024-08-07**|**3iGS: Factorised Tensorial Illumination for 3D Gaussian Splatting**|使用3D高斯作为辐射场的表示，实现了实时渲染速度下的高质量新颖视图合成。然而，选择将每个高斯光束的出射辐射独立地优化为球面谐波会导致不令人满意的视景相关效果。为了应对这些局限性，我们的工作，3D高斯散斑的因子化张量照明，或3iGS，提高了3D高斯散场（3DGS）的渲染质量。3iGS不是优化单个出射辐射参数，而是通过将出射辐射表示为局部照明场和双向反射分布函数（BRDF）特征的函数来增强3DGS视图相关效果。我们通过张量分解表示优化连续入射光照场，同时分别微调每个3D高斯光照场相对于该光照场的BRDF特征。我们的方法显著提高了3DGS的镜面视图相关效果的渲染质量，同时保持了快速的训练和渲染速度。 et.al.|[2408.03753](http://arxiv.org/abs/2408.03753)|null|

<p align=right>(<a href=#updated-on-20240814>back to top</a>)</p>

## 3D Reconstruction

|Publish Date|Title|Abstract|PDF|Code|
|---|---|---|---|---|
|**2024-08-12**|**3D Reconstruction of Protein Structures from Multi-view AFM Images using Neural Radiance Fields (NeRFs)**|最近在预测3D蛋白质结构的深度学习方面取得的进展显示出了希望，特别是在利用蛋白质序列和冷冻电子显微镜（Cryo-EM）图像等输入时。然而，在预测涉及多种蛋白质的蛋白质复合物（PC）的结构时，这些技术往往不足。在我们的研究中，我们研究了使用原子力显微镜（AFM）结合深度学习来预测PC的3D结构。AFM生成高度图，描绘了各种随机方向的PC，为训练神经网络预测3D结构提供了丰富的信息。然后，我们使用预训练的UpFusion模型（利用条件扩散模型来合成新视图）来训练特定于实例的NeRF模型进行3D重建。UpFusion的性能通过使用AFM图像对3D蛋白质结构进行零样本预测来评估。然而，挑战在于收集实际AFM图像的时间密集性和不切实际性。为了解决这个问题，我们使用了一种虚拟AFM成像过程，通过体绘制技术将“PDB”蛋白质文件转换为多视图2D虚拟AFM图像。我们使用虚拟和实际的多视图AFM图像广泛验证了UpFusion架构。我们的结果包括用不同数量的视图和不同的视图集预测的结构的比较。这种新方法具有通过进一步微调UpFusion网络来提高蛋白质复合物结构预测准确性的巨大潜力。 et.al.|[2408.06244](http://arxiv.org/abs/2408.06244)|null|
|**2024-08-12**|**Developing Smart MAVs for Autonomous Inspection in GPS-denied Constructions**|智能微型飞行器（MAV）通过在施工的各个阶段（包括难以到达的地区）进行高效、高分辨率的监测，改变了基础设施检查。在工业设施和基础设施等GPS不可用的环境中，无人机的传统手动操作是劳动密集型、繁琐且容易出错的。这项研究为在如此复杂和GPS不可用的室内环境中进行智能MAV检查提供了一个创新的框架。该框架具有一个分层感知和规划系统，可以识别感兴趣的区域并优化任务路径。它还提供了一种先进的MAV系统，具有增强的定位和运动规划能力，与神经重建技术集成，可对建筑结构进行全面的3D重建。该框架的有效性在一个4000平方米的室内基础设施中得到了实证验证，该设施的内部长度为80米，宽度为50米，高度为7米。主体结构由柱和墙组成。实验结果表明，我们的MAV系统在自主检测任务中表现出色，在生成和执行扫描路径方面实现了100%的成功率。广泛的实验验证了我们开发的MAV的机动性，在运动规划方面实现了100%的成功率，跟踪误差小于0.1米。此外，使用3D高斯散斑技术的增强重建方法能够从采集的数据中生成高保真渲染模型。总的来说，我们的新方法代表了在基础设施检查中使用机器人技术的重大进步。 et.al.|[2408.06030](http://arxiv.org/abs/2408.06030)|null|
|**2024-08-10**|**Visual SLAM with 3D Gaussian Primitives and Depth Priors Enabling Novel View Synthesis**|传统的基于几何的SLAM系统缺乏密集的3D重建能力，因为它们的数据关联通常依赖于特征对应。此外，基于学习的SLAM系统在实时性能和准确性方面往往不足。平衡实时性能和密集的3D重建能力是一个具有挑战性的问题。在本文中，我们提出了一种实时RGB-D SLAM系统，该系统结合了一种新的视图合成技术——3D高斯散点，用于3D场景表示和姿态估计。该技术利用了具有光栅化的3D高斯散斑的实时渲染性能，并允许通过CUDA实现实时可微优化。我们还支持从3D高斯网格重建显式密集3D重建。为了估计精确的相机姿态，我们采用了一种具有逆优化的旋转-平移解耦策略。这涉及通过基于梯度的优化在几次迭代中迭代更新两者。该过程包括可微分地渲染RGB、深度和轮廓图，并更新相机参数，以最小化现有3D高斯图的光度损失、深度几何损失和可见度损失的组合损失。然而，由于3D高斯分布的多视图不一致性，3D高斯散布（3DGS）难以准确表示曲面，这可能会导致相机姿态估计和场景重建的精度降低。为了解决这个问题，我们利用深度先验作为额外的正则化来强制执行几何约束，从而提高了姿态估计和3D重建的精度。我们还提供了关于公共基准数据集的广泛实验结果，以证明我们提出的方法在姿态精度、几何精度和渲染性能方面的有效性。 et.al.|[2408.05635](http://arxiv.org/abs/2408.05635)|null|
|**2024-08-10**|**CryoBench: Diverse and challenging datasets for the heterogeneity problem in cryo-EM**|低温电子显微镜（Cryo-EM）是一种从成像数据中确定高分辨率3D生物分子结构的强大技术。由于该技术可以捕获动态生物分子复合物，因此越来越多地开发了3D重建方法来解决这种内在的结构异质性。然而，缺乏具有地面实况结构和验证指标的标准化基准限制了该领域的进步。在这里，我们提出了CryoBench，这是一套用于冷冻-EM中异构重建的数据集、指标和性能基准。我们提出了五个数据集，代表了不同的异构来源和难度。这些包括由抗体复合物的简单运动和随机配置以及从分子动力学模拟中取样的数万个结构产生的构象异质性。我们还设计了包含核糖体组装状态混合物和细胞中存在的100种常见复合物组成异质性的数据集。然后，我们对最先进的异构重建工具进行了全面分析，包括神经和非神经方法及其对噪声的敏感性，并提出了定量比较方法的新指标。我们希望这个基准将成为分析低温EM和机器学习社区现有方法和新算法开发的基础资源。 et.al.|[2408.05526](http://arxiv.org/abs/2408.05526)|null|
|**2024-08-10**|**Mesh deformation-based single-view 3D reconstruction of thin eyeglasses frames with differentiable rendering**|在虚拟现实（VR）和增强现实（AR）技术的支持下，3D虚拟眼镜试穿应用正在成为一种新的趋势解决方案，它提供了一种“试穿”选项，可以在舒适的家中选择完美的眼镜。由于缺乏足够的纹理特征、元素薄和严重的自遮挡等独特特征，使用传统的基于深度和图像的方法从单个图像重建眼镜架是极其困难的。在这篇论文中，我们提出了第一个基于网格变形的重建框架，利用先验知识和领域特定知识，从单个RGB图像中恢复高精度的3D全框眼镜模型。具体来说，基于合成眼镜架数据集的构建，我们首先定义了一个具有预定义关键点的特定类别眼镜架模板。然后，给定一个结构薄、纹理特征少的输入眼镜架图像，我们设计了一个关键点检测器和细化器，以从粗到细的方式检测预定义的关键点，从而准确估计相机姿态。之后，使用可微渲染，我们提出了一种新的优化方法，通过在模板网格上逐步执行自由变形（FFD）来生成正确的几何体。我们定义了一系列损失函数，利用固有结构、轮廓、关键点、每像素阴影信息等的约束，增强渲染结果与相应RGB输入之间的一致性。合成数据集和真实图像的实验结果证明了所提出算法的有效性。 et.al.|[2408.05402](http://arxiv.org/abs/2408.05402)|null|
|**2024-08-09**|**DG Comics: Semi-Automatically Authoring Graph Comics for Dynamic Graphs**|漫画是一种有效的顺序数据驱动叙事方法，特别是对于动态图——顶点和边随时间变化的图。然而，手动创建这样的漫画目前耗时、复杂且容易出错。本文中，我们提出了DG漫画，这是一种用于动态图形的新颖漫画创作工具，允许用户半自动构建和注释漫画。该工具使用新开发的分层聚类算法来分割动态图的连续快照，同时保持其时间顺序。它还提供了从多个视图中的动态图中提取的关于个人和社区的丰富信息，用户可以在其中探索动态图并选择在漫画中讲述什么。为了进行评估，我们提供了一个示例，并报告了用户研究和专家评审的结果。 et.al.|[2408.04874](http://arxiv.org/abs/2408.04874)|null|
|**2024-08-09**|**Self-augmented Gaussian Splatting with Structure-aware Masks for Sparse-view 3D Reconstruction**|稀疏视图3D重建是计算机视觉领域的一项艰巨挑战，旨在从有限的观察角度构建完整的三维模型。这项任务面临几个困难：1）缺乏一致信息的输入图像数量有限；2） 对输入图像质量的依赖性；以及3）模型参数的实质大小。为了应对这些挑战，我们提出了一种自增强的粗到细高斯飞溅范式，并使用结构感知掩模进行增强，用于稀疏视图3D重建。特别是，我们的方法最初采用粗高斯模型从稀疏视图输入中获得基本的3D表示。随后，我们开发了一个精细的高斯网络，通过3D几何增强和感知视图增强来增强输出的一致性和详细表示。在训练过程中，我们设计了一种结构感知掩蔽策略，以进一步提高模型对稀疏输入和噪声的鲁棒性。在MipNeRF360和OmniObject3D数据集上的实验结果表明，所提出的方法在感知质量和效率方面都实现了稀疏输入视图的最新性能。 et.al.|[2408.04831](http://arxiv.org/abs/2408.04831)|null|
|**2024-08-06**|**LumiGauss: High-Fidelity Outdoor Relighting with 2D Gaussian Splatting**|使用无约束的照片集将照明与几何体解耦是出了名的挑战。解决这个问题将使许多用户受益，因为创建复杂的3D资产需要数天的体力劳动。许多先前的工作都试图解决这个问题，但往往以牺牲输出保真度为代价，这对这些方法的实用性提出了质疑。我们介绍了LumiGauss，这是一种通过2D高斯散斑处理场景和环境照明的3D重建的技术。我们的方法可以产生高质量的场景重建，并在新颖的环境地图下实现逼真的照明合成。我们还提出了一种通过利用球面谐波特性来提高室外场景中常见阴影质量的方法。我们的方法有助于与游戏引擎无缝集成，并支持使用快速预计算的辐射传输。我们在NeRF OSR数据集上验证了我们的方法，证明了其优于基线方法的性能。此外，LumiGauss在应用新的环境地图时可以合成逼真的图像。 et.al.|[2408.04474](http://arxiv.org/abs/2408.04474)|**[link](https://github.com/joaxkal/lumigauss)**|
|**2024-08-08**|**A Review of 3D Reconstruction Techniques for Deformable Tissues in Robotic Surgery**|作为机器人微创手术中一项关键而复杂的任务，使用立体或单眼内窥镜视频重建手术场景具有巨大的临床应用潜力。基于NeRF的技术最近因其隐式重建场景的能力而受到关注。另一方面，基于高斯飞溅的3D-GS显式地使用3D高斯表示场景，并将其投影到2D平面上，以替代NeRF中的复杂体绘制。然而，这些方法在手术场景重建方面面临着挑战，例如推理速度慢、动态场景和手术工具遮挡。这项工作探索和回顾了最先进的（SOTA）方法，讨论了它们的创新和实施原则。此外，我们复制了模型，并对两个数据集进行了测试和评估。测试结果表明，随着这些技术的进步，实现实时、高质量的重建变得可行。 et.al.|[2408.04426](http://arxiv.org/abs/2408.04426)|**[link](https://github.com/epsilon404/surgicalnerf)**|
|**2024-08-07**|**Opening the Black Box of 3D Reconstruction Error Analysis with VECTOR**|从2D图像重建3D场景是一项技术挑战，影响了从地球和行星科学、太空探索到增强现实和虚拟现实的各个领域。通常，重建算法首先识别图像中的共同特征，然后在估计地形形状后最小化重建误差。这个束调整（BA）步骤围绕一个简化的标量值进行优化，该标量值混淆了重建误差的许多可能原因（例如，相机位置和方向的初始估计、照明条件、地形中特征检测的难易程度）。重建误差可能导致不准确的科学推断，或危及探索偏远环境的航天器。为了应对这一挑战，我们提出了VECTOR，这是一种视觉分析工具，可以改善立体重建BA的误差检查。VECTOR为分析人员提供了以前无法获得的特征位置、相机姿态和计算出的3D点的可见性。VECTOR是与美国国家航空航天局喷气推进实验室的Perseverance火星漫游者和Ingenuity火星直升机地形重建团队合作开发的。我们报告了如何使用该工具调试和改进火星2020任务的地形重建。 et.al.|[2408.03503](http://arxiv.org/abs/2408.03503)|**[link](https://github.com/NASA-AMMOS/VECTOR)**|

<p align=right>(<a href=#updated-on-20240814>back to top</a>)</p>

## Diffusion

|Publish Date|Title|Abstract|PDF|Code|
|---|---|---|---|---|
|**2024-08-12**|**The AI Scientist: Towards Fully Automated Open-Ended Scientific Discovery**|通用人工智能面临的重大挑战之一是开发能够进行科学研究和发现新知识的智能体。虽然前沿模型已经被用作人类科学家的辅助工具，例如头脑风暴、编写代码或预测任务，但它们仍然只完成了科学过程的一小部分。本文提出了第一个全自动科学发现的综合框架，使前沿大型语言模型能够独立进行研究并交流其发现。我们介绍《人工智能科学家》，它产生新的研究思路，编写代码，执行实验，将结果可视化，通过撰写一篇完整的科学论文来描述其发现，然后运行一个模拟的评审过程进行评估。原则上，这个过程可以重复，以开放的方式迭代地发展想法，就像人类科学界一样。我们通过将其应用于机器学习的三个不同子领域来展示其多功能性：扩散建模、基于变换器的语言建模和学习动力学。每一个想法都被实施并发展成一篇完整的论文，每篇论文的成本不到15美元。为了评估生成的论文，我们设计并验证了一个自动审阅器，我们证明它在评估论文分数方面达到了接近人类的水平。根据我们的自动审稿人的判断，人工智能科学家可以在顶级机器学习会议上发表超过接受阈值的论文。这种方法标志着机器学习科学发现新时代的开始：将人工智能代理的变革性优势带入人工智能本身的整个研究过程，并使我们更接近一个可以在世界上最具挑战性的问题上释放出无尽的负担得起的创造力和创新的世界。我们的代码开源于https://github.com/SakanaAI/AI-Scientist et.al.|[2408.06292](http://arxiv.org/abs/2408.06292)|**[link](https://github.com/sakanaai/ai-scientist)**|
|**2024-08-12**|**3D Reconstruction of Protein Structures from Multi-view AFM Images using Neural Radiance Fields (NeRFs)**|最近在预测3D蛋白质结构的深度学习方面取得的进展显示出了希望，特别是在利用蛋白质序列和冷冻电子显微镜（Cryo-EM）图像等输入时。然而，在预测涉及多种蛋白质的蛋白质复合物（PC）的结构时，这些技术往往不足。在我们的研究中，我们研究了使用原子力显微镜（AFM）结合深度学习来预测PC的3D结构。AFM生成高度图，描绘了各种随机方向的PC，为训练神经网络预测3D结构提供了丰富的信息。然后，我们使用预训练的UpFusion模型（利用条件扩散模型来合成新视图）来训练特定于实例的NeRF模型进行3D重建。UpFusion的性能通过使用AFM图像对3D蛋白质结构进行零样本预测来评估。然而，挑战在于收集实际AFM图像的时间密集性和不切实际性。为了解决这个问题，我们使用了一种虚拟AFM成像过程，通过体绘制技术将“PDB”蛋白质文件转换为多视图2D虚拟AFM图像。我们使用虚拟和实际的多视图AFM图像广泛验证了UpFusion架构。我们的结果包括用不同数量的视图和不同的视图集预测的结构的比较。这种新方法具有通过进一步微调UpFusion网络来提高蛋白质复合物结构预测准确性的巨大潜力。 et.al.|[2408.06244](http://arxiv.org/abs/2408.06244)|null|
|**2024-08-12**|**Singular limit and convergence rate via projection method in a model for plant-growth dynamics with autotoxicity**|我们研究了一个快速反应扩散系统，该系统模拟了自毒性对植物生长动力学的影响，其中快速反应项基于健康根和暴露根之间的二分法，具体取决于毒性。该模型在[Giannino，Iuorio，Soresina，即将出版]中提出，用于解释仅考虑生物量和毒性的稳定静止空间模式，并对其快速反应（交叉扩散）极限进行了形式化推导和数值研究。本文通过执行涉及能量的自举论证，严格地得到了交叉扩散极限系统，作为具有快速反应项的反应扩散系统的快速反应极限。然后，对交叉扩散系统进行了全面的适定性分析，包括弱解的 $L^\infty_{x，t}$ 界、唯一性、稳定性和正则性。反过来，由于使用逆诺伊曼-拉普拉斯算子的关键思想，这种分析对于建立快速反应极限的收敛速度至关重要。最后，数值实验说明了收敛速度的分析结果。 et.al.|[2408.06177](http://arxiv.org/abs/2408.06177)|null|
|**2024-08-12**|**Novel View Synthesis from a Single Image with Pretrained Diffusion Guidance**|最近的3D新颖视图合成（NVS）方法仅限于从新视点生成的以单个对象为中心的场景，并且难以应对复杂的环境。它们通常需要大量的3D数据进行训练，除了训练分布之外缺乏泛化能力。相反，无3D方法可以使用预训练的稳定扩散模型生成复杂、狂野场景的文本控制视图，而无需繁琐的微调，但缺乏相机控制。本文介绍了HawkI++，这是一种能够从单个输入图像生成相机控制视点的方法。HawkI++擅长处理复杂多样的场景，无需额外的3D数据或大量训练。它利用广泛可用的预训练NVS模型进行弱制导，将这些知识整合到3D自由视图合成方法中，以有效地实现所需的结果。我们的实验结果表明，HawkI++在定性和定量评估方面都优于现有模型，在各种场景中以所需的相机角度提供高保真度和一致的新颖视图合成。 et.al.|[2408.06157](http://arxiv.org/abs/2408.06157)|null|
|**2024-08-12**|**Efficient and Scalable Point Cloud Generation with Sparse Point-Voxel Diffusion Models**|我们提出了一种新颖的点云U-Net扩散架构，用于3D生成建模，能够生成高质量和多样化的3D形状，同时保持快速的生成时间。我们的网络采用双分支架构，将点的高分辨率表示与稀疏体素的计算效率相结合。我们最快的变体在无条件形状生成方面优于所有非扩散生成方法，这是评估点云生成模型最受欢迎的基准，而我们最大的模型在扩散方法中取得了最先进的结果，运行时间约为以前最先进PVD的70%。除了无条件生成之外，我们还进行了广泛的评估，包括对所有类别的ShapeNet进行条件生成，展示了我们的模型对更大数据集的可扩展性，以及隐式生成，它使我们的网络能够在更少的时间步上生成高质量的点云，进一步缩短了生成时间。最后，我们评估了该架构在点云完成和超分辨率方面的性能。我们的模型在所有任务中都表现出色，使其成为点云生成建模的最先进的扩散U-Net。该代码可在以下网址公开获取https://github.com/JohnRomanelis/SPVD.git. et.al.|[2408.06145](http://arxiv.org/abs/2408.06145)|null|
|**2024-08-12**|**CogVideoX: Text-to-Video Diffusion Models with An Expert Transformer**|我们介绍了CogVideoX，这是一种大规模的扩散变换模型，旨在基于文本提示生成视频。为了有效地对视频数据进行建模，我们建议利用3D变分自编码器（VAE）沿空间和时间维度压缩视频。为了改善文本视频对齐，我们提出了一种具有专家自适应LayerNorm的专家变换器，以促进两种模式之间的深度融合。通过采用渐进式训练技术，CogVideoX擅长制作连贯、长时间的视频，其特征是明显的动作。此外，我们开发了一个有效的文本视频数据处理管道，其中包括各种数据预处理策略和视频字幕方法。它显著地提高了CogVideoX的性能，提高了生成质量和语义对齐。结果表明，CogVideoX在多个机器指标和人工评估方面都表现出了最先进的性能。3D Causal VAE和CogVideoX的模型权重均可在https://github.com/THUDM/CogVideo. et.al.|[2408.06072](http://arxiv.org/abs/2408.06072)|**[link](https://github.com/thudm/cogvideo)**|
|**2024-08-12**|**ControlNeXt: Powerful and Efficient Control for Image and Video Generation**|扩散模型在图像和视频生成方面表现出了显著而稳健的能力。为了更好地控制生成的结果，研究人员引入了其他架构，如ControlNet、Adapters和ReferenceNet，以集成调节控制。然而，当前的可控生成方法通常需要大量额外的计算资源，特别是对于视频生成，并且在训练中面临挑战或表现出弱控制。本文提出了ControlNeXt：一种强大而高效的可控图像和视频生成方法。我们首先设计了一个更简单、更高效的架构，与基本模型相比，以最小的额外成本替换了大量的额外分支。这种简洁的结构也使我们的方法能够与其他LoRA权重无缝集成，无需额外训练即可进行风格更改。至于训练，与替代方案相比，我们减少了高达90%的可学习参数。此外，我们提出了另一种称为交叉归一化（CN）的方法来代替零卷积，以实现快速稳定的训练收敛。我们在图像和视频中对不同的基础模型进行了各种实验，证明了我们方法的鲁棒性。 et.al.|[2408.06070](http://arxiv.org/abs/2408.06070)|**[link](https://github.com/dvlab-research/controlnext)**|
|**2024-08-12**|**BooW-VTON: Boosting In-the-Wild Virtual Try-On via Mask-Free Pseudo Data Training**|基于图像的虚拟试穿是生成特定人物逼真试穿图像的一项越来越流行和重要的任务。现有的方法总是采用精确的掩模来去除源图像中的原始服装，从而在基于强大扩散模型的简单和传统试穿场景中实现逼真的合成图像。因此，获得合适的口罩对这些方法的试用性能至关重要。然而，如图1-Top所示，获得精确的修复掩模并不容易，特别是对于包含不同前景遮挡和人物姿势的数据的复杂野外尝试。这种困难通常会导致在更实际和更具挑战性的现实生活场景中表现不佳，如图1-Bottom所示的自拍场景。为此，我们提出了一种新的训练范式，结合高效的数据增强方法，从野生场景中获取大规模的未配对训练数据，从而显著提高了模型的试戴性能，而不需要额外的修复掩模。此外，还设计了一种试戴定位损失，以定位更准确的试戴区域，从而获得更合理的试戴结果。值得注意的是，我们的方法只需要参考布料图像、源姿势图像和源人物图像作为输入，与现有方法相比，更具成本效益和用户友好性。大量的定性和定量实验表明，在如此低的需求投入下，在野外场景中表现优异。 et.al.|[2408.06047](http://arxiv.org/abs/2408.06047)|**[link](https://github.com/little-misfit/boow-vton)**|
|**2024-08-12**|**Gradient flow for a class of diffusion equations with Dirichlet boundary data**|本文给出了一类在有界域上具有恒定非负Dirichlet边界条件的非线性演化方程的变分特征，作为非负测度空间中的梯度流。相关几何形状由Figalli和Gigli引入的修正Wasserstein距离给出，该距离允许通过让边界充当储层来改变质量。我们根据Benamou Brenier的精神，将该距离作为满足连续性方程的非负测度曲线的动作最小化问题给出了一个动态公式。然后，我们将具有Dirichlet边界条件的非线性扩散方程的解表征为最大斜率曲线意义上的内能泛函的度量梯度流。 et.al.|[2408.05987](http://arxiv.org/abs/2408.05987)|null|
|**2024-08-12**|**Diffuse-UDA: Addressing Unsupervised Domain Adaptation in Medical Image Segmentation with Appearance and Structure Aligned Diffusion Models**|3D医学成像中体素级注释的稀缺性和复杂性带来了重大挑战，特别是由于资源丰富的中心的标记数据集和资源较少的中心的未标记数据集之间的领域差距。这种差异影响了医疗保健中人工智能算法的公平性。我们介绍了Diffuse UDA，这是一种利用扩散模型来解决医学图像分割中的无监督域自适应（UDA）问题的新方法。漫反射UDA生成具有目标域特征和各种结构的高质量图像掩模对，从而增强UDA任务。最初，生成目标域样本的伪标签。随后，在两个域的图像标签或图像伪标签对上训练一个包含可变形增强的专门定制的扩散模型。最后，源域标签引导扩散模型为目标域生成图像标签对。对几个基准的综合评估表明，Diffuse UDA的表现优于领先的UDA和半监督策略，其性能接近甚至超过了直接在目标域数据上训练的模型的理论上限。Diffuse UDA为推进医学成像中人工智能系统的开发和部署提供了一条途径，解决了医疗环境之间的差异。这种方法可以探索创新的人工智能驱动的诊断工具，改善结果，节省时间，减少人为错误。 et.al.|[2408.05985](http://arxiv.org/abs/2408.05985)|null|

<p align=right>(<a href=#updated-on-20240814>back to top</a>)</p>

## NeRF

|Publish Date|Title|Abstract|PDF|Code|
|---|---|---|---|---|
|**2024-08-10**|**Scene123: One Prompt to 3D Scene Generation via Video-Assisted and Consistency-Enhanced MAE**|随着人工智能生成内容（AIGC）的进步，已经开发了各种方法来从单模式或多模式输入生成文本、图像、视频和3D对象，从而有助于模拟类人认知内容的创建。然而，由于确保模型生成的外推视图之间的一致性所涉及的复杂性，从单个输入生成逼真的大规模场景是一个挑战。受益于最新的视频生成模型和隐式神经表示，我们提出了Scene123，这是一种3D场景生成模型，它不仅通过视频生成框架确保了真实性和多样性，还使用隐式神经场与掩模自编码器（MAE）相结合，有效地确保了视图中看不见区域的一致性。具体来说，我们最初会扭曲输入图像（或从文本生成的图像）以模拟相邻的视图，用MAE模型填充不可见的区域。然而，这些填充图像通常无法保持视图一致性，因此我们利用产生的视图来优化神经辐射场，增强几何一致性。此外，为了进一步增强生成视图的细节和纹理保真度，我们对通过视频生成模型从输入图像中导出的图像采用了基于GAN的Loss。大量实验表明，我们的方法可以从单个提示中生成逼真一致的场景。定性和定量结果都表明，我们的方法超越了现有的最先进的方法。我们展示鼓励视频示例https://yiyingyang12.github.io/Scene123.github.io/. et.al.|[2408.05477](http://arxiv.org/abs/2408.05477)|null|
|**2024-08-07**|**Compact 3D Gaussian Splatting for Static and Dynamic Radiance Fields**|3D高斯飞溅（3DGS）最近成为一种替代表示，它利用基于3D高斯的表示并引入了近似的体积渲染，实现了非常快的渲染速度和有前景的图像质量。此外，后续的研究已成功地将3DGS扩展到动态3D场景，展示了其广泛的应用。然而，由于3DGS及其后续方法需要大量的高斯分布来保持渲染图像的高保真度，这需要大量的内存和存储，因此出现了一个重大的缺点。为了解决这个关键问题，我们特别强调两个关键目标：在不牺牲性能的情况下减少高斯点的数量，以及压缩高斯属性，如视图相关的颜色和协方差。为此，我们提出了一种可学习的掩码策略，该策略在保持高性能的同时显著减少了高斯数。此外，我们提出了一种紧凑但有效的视图相关颜色表示方法，即采用基于网格的神经场，而不是依赖球谐函数。最后，我们学习码本，通过残差矢量量化来紧凑地表示几何和时间属性。通过量化和熵编码等模型压缩技术，我们始终表明，与静态场景的3DGS相比，存储空间减少了25倍以上，渲染速度提高了25倍，同时保持了场景表示的质量。对于动态场景，与现有的最先进方法相比，我们的方法实现了超过12倍的存储效率，并保留了高质量的重建。我们的工作为3D场景表示提供了一个全面的框架，实现了高性能、快速训练、紧凑性和实时渲染。我们的项目页面可在https://maincold2.github.io/c3dgs/. et.al.|[2408.03822](http://arxiv.org/abs/2408.03822)|null|
|**2024-08-07**|**PRTGS: Precomputed Radiance Transfer of Gaussian Splats for Real-Time High-Quality Relighting**|我们提出了高斯斑点的预计算辐射转移（PRTGS），这是一种在低频照明环境中用于高斯斑点的实时高质量重新照明方法，通过预计算3D高斯斑点的辐射转移来捕获柔和的阴影和相互反射。现有的研究表明，在动态照明场景中，3D高斯溅射（3DGS）的效率优于神经场。然而，目前基于3DGS的重新照明方法仍然难以实时计算动态光的高质量阴影和间接照明，导致渲染结果不切实际。我们通过预先计算复杂传递函数（如阴影）所需的昂贵传输模拟来解决这个问题，得到的传递函数表示为每个高斯斑点的密集向量集或矩阵集。我们介绍了针对训练和渲染阶段量身定制的不同预计算方法，以及针对3D高斯斑点的独特光线追踪和间接照明预计算技术，以加快训练速度并计算与环境光相关的准确间接照明。实验分析表明，我们的方法在保持有竞争力的训练时间的同时实现了最先进的视觉质量，并允许以1080p分辨率对动态光和相对复杂的场景进行高质量的实时（30+fps）重新照明。 et.al.|[2408.03538](http://arxiv.org/abs/2408.03538)|null|
|**2024-08-01**|**Neural Octahedral Field: Octahedral prior for simultaneous smoothing and sharp edge regularization**|神经隐式表示，将距离函数参数化为坐标神经场，已成为解决无方向点云表面重建的有前景的前沿。为了确保方向一致，现有的方法侧重于正则化距离函数的梯度，例如将其约束为单位范数，最小化其散度，或将其与对应于零特征值的Hessian特征向量对齐。然而，在存在大扫描噪声的情况下，它们往往要么过拟合噪声输入，要么产生过于平滑的重建。在这项工作中，我们建议利用六面体网格中产生的八面体框架的球谐表示，在一种新的神经场变体——八面体场下指导曲面重建。当约束为平滑时，该字段会自动捕捉到几何特征，并在折痕上插值时自然保留锐角。通过同时拟合和平滑隐式几何旁边的八面体场，它的行为类似于双边滤波，从而在保持锐边的同时实现平滑重建。尽管是纯逐点操作，但我们的方法在广泛的实验中表现优于各种传统和神经方法，并且与需要正常和数据先验的方法非常有竞争力。我们的全面实施可在以下网址获得：https://github.com/Ankbzpx/frame-field. et.al.|[2408.00303](http://arxiv.org/abs/2408.00303)|**[link](https://github.com/ankbzpx/frame-field)**|
|**2024-07-30**|**Neural Fields for Continuous Periodic Motion Estimation in 4D Cardiovascular Imaging**|时间分辨三维血流MRI（4D血流MRI）提供了一种独特的非侵入性解决方案，用于可视化和量化主动脉弓等血管中的血流动力学。然而，由于难以获得完整的周期分割，目前大多数动脉4D血流MRI分析方法使用静态动脉壁。为了克服这一局限性，我们提出了一种基于神经场的方法，可以直接估计整个心动周期中连续的周期性壁变形。对于3D+时间成像数据集，我们优化了表示时间依赖速度矢量场（VVF）的隐式神经表示（INR）。ODE求解器用于将VVF集成到变形矢量场（DVF）中，该矢量场可以随着时间的推移使图像、分割掩模或网格变形，从而可视化和量化局部壁运动模式。为了正确反映3D+时间心血管数据的周期性，我们以两种方式施加周期性。首先，通过定期对输入到INR的时间进行编码，从而对VVF进行编码。其次，通过规范DVF。我们证明了这种方法在不同周期模式的合成数据、心电图门控CT和4D血流MRI数据上的有效性。所获得的方法可用于改进4D血流MRI分析。 et.al.|[2407.20728](http://arxiv.org/abs/2407.20728)|null|
|**2024-07-29**|**Aero-Nef: Neural Fields for Rapid Aircraft Aerodynamics Simulations**|本文提出了一种基于隐式神经表示（INR）在网格域上学习稳态流体动力学模拟替代模型的方法。所提出的模型可以直接应用于不同流动条件下的非结构化域，处理非参数3D几何变化，并推广到测试时看不见的形状。基于坐标的公式自然会导致离散化的鲁棒性，从而在计算成本（内存占用和训练时间）和精度之间实现了极好的权衡。该方法在两个工业相关应用中得到了验证：跨音速翼型上二维可压缩流的RANS数据集和三维机翼上表面压力分布的数据集，包括形状、流入条件和控制表面偏转变化。在所考虑的测试用例中，与最先进的图神经网络架构相比，我们的方法实现了三倍多的测试误差，并显著改善了看不见的几何形状的泛化误差。值得注意的是，该方法在RANS跨音速翼型数据集上的推理速度比高保真求解器快五个数量级。代码可在以下网址获得https://gitlab.isae-supaero.fr/gi.catalani/aero-nepf et.al.|[2407.19916](http://arxiv.org/abs/2407.19916)|null|
|**2024-07-26**|**ObjectCarver: Semi-automatic segmentation, reconstruction and separation of 3D objects**|隐式神经场在从多幅图像重建3D表面方面取得了显著进展；然而，在分离场景中的单个对象时，他们遇到了挑战。之前的工作试图通过引入一个框架来解决这个问题，该框架为N个对象中的每一个同时训练单独的带符号距离场（SDF），并使用正则化项来防止对象重叠。然而，所有这些方法都需要提供分割掩模，这并不总是容易获得的。我们介绍了我们的方法ObjectCarver，来解决在单个视图中从点击输入中分离对象的问题。给定摆出的多视图图像和一组用户输入点击来提示分割单个对象，我们的方法将场景分解为单独的对象，并为每个对象重建高质量的3D表面。我们引入了一个损失函数，可以防止漂浮物，避免因遮挡而造成不适当的雕刻。此外，我们引入了一种新的场景初始化方法，与之前的方法相比，该方法在保留几何细节的同时显著加快了过程。尽管不需要地面真实掩模或单眼线索，但我们的方法在定性和定量上都优于基线。此外，我们引入了一个新的基准数据集进行评估。 et.al.|[2407.19108](http://arxiv.org/abs/2407.19108)|null|
|**2024-07-24**|**Neural field equations with time-periodic external inputs and some applications to visual processing**|这项工作的目的是为研究视觉处理任务中的闪烁输入提供一个数学框架。当与几何图案结合时，这些输入会影响并诱发有趣的心理物理现象，如麦凯效应和比洛克-邹效应，在这些效应中，受试者感知到通常由闪烁频率调制的特定余像。由于输入的对称破缺结构，经典分叉理论和多尺度分析技术在我们的背景下不是很有效。因此，我们采用了一种基于Amari型神经场控制理论的输入-输出框架的方法。这使我们能够证明，当受到周期性输入的驱动时，动态会收敛到周期性状态。此外，我们研究了在哪些假设下，这些非线性动力学可以有效地线性化，在这种情况下，我们提出了短程兴奋性和远程抑制性神经元相互作用的积分核的精确近似值。最后，对于集中在具有闪烁背景的视野中心的输入，我们直接将余像中出现的虚幻轮廓的宽度与闪烁频率和抑制强度联系起来。 et.al.|[2407.17294](http://arxiv.org/abs/2407.17294)|null|
|**2024-07-23**|**Fluorescence Diffraction Tomography using Explicit Neural Fields**|从荧光图像中求解3D折射率（RI）可以提供有关生物样本的荧光和相位信息。然而，在大体积、高分辨率和反射模式下准确检索部分相干光的相位以重建无标签相位物体的未知RI仍然具有挑战性。为了应对这一挑战，我们开发了具有显式神经场的荧光衍射断层扫描（FDT），可以从散焦荧光散斑图像重建3D RI。使用FDT成功重建3D RI依赖于四个关键组件：粗到细建模、自校准、差分多层渲染模型和部分相干掩模。具体而言，显式表示与粗到细建模有效地集成在一起，以实现高速、高分辨率的重建。此外，我们将多层方程推进到微分多层渲染模型，这使得系统的外部和内部参数能够进行自校准。自校准有助于高精度的正向图像预测和RI重建。部分相干掩模是数字掩模，用于准确有效地解决相干光模型和部分相干光数据之间的差异。FDT成功地从荧光图像中重建了24个z $层上1024$×1024像素的530$×530$×300$μm^3$ 体积的3D培养无标记3D MuSCs管的RI，证明了在体外对体积庞大和异质的生物样本进行高保真3D RI重建。 et.al.|[2407.16657](http://arxiv.org/abs/2407.16657)|null|
|**2024-07-22**|**Iterative approach to reconstructing neural disparity fields from light-field data**|本研究提出了一种神经视差场（NDF），该场基于神经场建立了场景视差的隐式连续表示，并采用迭代方法解决了从光场数据重建NDF的逆问题。NDF能够无缝和精确地表征三维场景中的视差变化，并可以以任何任意分辨率对视差进行离散化，克服了传统视差图容易出现采样误差和插值不准确的局限性。所提出的NDF网络架构利用哈希编码结合多层感知器来捕获纹理级别的详细差异，从而增强其表示复杂场景几何信息的能力。通过利用光场数据中固有的空间角度一致性，开发了一种可微分正向模型，用于从光场数据生成中心视图图像。基于正向模型，建立了一种使用可微传播算子的NDF重建逆问题的优化方案。此外，在优化方案中，采用迭代求解方法重建NDF，该方法不需要训练数据集，适用于各种采集方法捕获的光场数据。实验结果表明，使用所提出的方法可以从光场数据中重建高质量的NDF。NDF可以有效地恢复高分辨率视差，证明了其隐式、连续表示场景视差的能力。 et.al.|[2407.15380](http://arxiv.org/abs/2407.15380)|null|

<p align=right>(<a href=#updated-on-20240814>back to top</a>)</p>

[contributors-shield]: https://img.shields.io/github/contributors/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[contributors-url]: https://github.com/Vincentqyw/cv-arxiv-daily/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[forks-url]: https://github.com/Vincentqyw/cv-arxiv-daily/network/members
[stars-shield]: https://img.shields.io/github/stars/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[stars-url]: https://github.com/Vincentqyw/cv-arxiv-daily/stargazers
[issues-shield]: https://img.shields.io/github/issues/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[issues-url]: https://github.com/Vincentqyw/cv-arxiv-daily/issues

