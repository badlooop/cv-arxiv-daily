[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]

## Updated on 2023.09.28
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
|**2023-09-27**|**P2I-NET: Mapping Camera Pose to Image via Adversarial Learning for New View Synthesis in Real Indoor Environments**|给定室内环境中一个新的 $6DoF$ 相机姿势，我们研究了基于一组参考RGBD视图从该姿势预测视图的挑战性问题。现有的显式或隐式3D几何构造方法在计算上是昂贵的，而那些基于学习的方法主要关注具有规则几何结构的对象类别的孤立视图。与传统的\textit{rend-inpaint}方法不同，我们提出了一种条件生成对抗性神经网络（P2I-NET）来直接从给定的姿态预测新视图。P2I-NET学习环境图像的条件分布，以建立相机姿势与其环境视图之间的对应关系，并通过其架构中的许多创新设计和训练丢失的功能来实现这一点。引入了两个辅助鉴别器约束，用于在潜在特征空间和真实世界姿势空间中增强生成图像的姿势与对应真实世界图像的姿势之间的一致性。此外，引入了深度卷积神经网络（CNN）来进一步增强像素空间中的这种一致性。我们在真实的室内数据集上进行了大量的新视图合成实验。结果表明，与许多基于NeRF的强基线模型相比，P2I-NET具有优越的性能。特别是，我们发现P2I-NET在合成类似质量的图像时比这些竞争对手的技术快40到100倍。此外，我们贡献了一个新的公开可用的室内环境数据集，其中包含22个高分辨率RGBD视频，其中每一帧也有准确的相机姿态参数。 et.al.|[2309.15526](http://arxiv.org/abs/2309.15526)|null|
|**2023-09-26**|**3D Reconstruction with Generalizable Neural Fields using Scene Priors**|由于神经领域的最新进展，高保真3D场景重建得到了实质性的推进。然而，大多数现有的方法为每个单独的场景从头开始训练单独的网络。这是不可扩展的，效率低下，并且在视图有限的情况下无法产生良好的结果。虽然基于学习的多视图立体方法在一定程度上缓解了这一问题，但它们的多视图设置使其扩展和广泛应用的灵活性降低。相反，我们引入了结合场景先验（NFP）的训练可推广神经场。NFP网络将任何单视图RGB-D图像映射为带符号的距离和辐射值。在没有融合模块的情况下，可以通过合并体积空间中的各个帧来重建完整的场景，这提供了更好的灵活性。场景先验可以在大规模数据集上进行训练，从而能够快速适应具有较少视图的新场景的重建。NFP不仅展示了SOTA场景重建的性能和效率，而且还支持单图像新视图合成，这在神经领域还没有得到充分的探索。更多定性结果可在以下网站获得：https://oasisyang.github.io/neural-prior et.al.|[2309.15164](http://arxiv.org/abs/2309.15164)|null|
|**2023-09-25**|**NAS-NeRF: Generative Neural Architecture Search for Neural Radiance Fields**|神经辐射场（NeRF）能够实现高质量的新视图合成，但其高得令人望而却步的计算复杂性限制了可部署性，尤其是在资源受限的平台上。为了实现NeRF的实际使用，质量调整对于降低计算复杂性至关重要，类似于视频游戏中的可调整图形设置。然而，尽管现有的解决方案努力提高效率，但无论场景复杂程度如何，它们都使用一刀切的架构，尽管相同的架构对于简单场景可能不必要地大，但对于复杂场景则不够。因此，随着NeRF越来越广泛地用于3D可视化，需要动态优化NeRF的神经网络组件，以实现计算复杂性和合成质量特定目标之间的平衡。为了解决这一差距，我们引入了NAS NeRF：一种生成神经架构搜索策略，通过优化复杂性和性能之间的权衡，同时遵守计算预算和最低合成质量的限制，专门针对每个场景生成NeRF架构。我们在Blender合成数据集上的实验表明，与基线NeRF相比，所提出的NAS NeRF在GPU上生成的架构可以小5.74 $\times$，FLOP少4.19$\times$，速度快1.93$\times]，而SSIM不会下降。此外，我们还表明，NAS NeRF还可以实现比基线NeRF小23$\times$、FLOP少22$\times$和快4.7$ \times\的架构，平均SSIM下降5.3\%。我们工作的源代码也可在https://saeejithnair.github.io/NAS-NeRF. et.al.|[2309.14293](http://arxiv.org/abs/2309.14293)|null|
|**2023-09-22**|**Deformable 3D Gaussians for High-Fidelity Monocular Dynamic Scene Reconstruction**|隐式神经表示为动态场景重建和渲染开辟了新的途径。尽管如此，最先进的动态神经渲染方法在很大程度上依赖于这些隐含的表示，而这些表示往往难以准确捕捉场景中对象的复杂细节。此外，隐式方法难以在一般动态场景中实现实时渲染，限制了它们在各种任务中的使用。为了解决这些问题，我们提出了一种可变形的3D高斯散射方法，该方法使用显式3D高斯重建场景，并在具有变形场的规范空间中学习高斯，以对单目动态场景进行建模。我们还引入了一种没有额外开销的平滑训练机制，以减轻真实数据集中不准确姿态对时间插值任务平滑性的影响。通过差分高斯光栅化，可变形的三维高斯不仅可以获得更高的渲染质量，而且可以获得实时渲染速度。实验表明，我们的方法在渲染质量和速度方面都显著优于现有方法，非常适合于新视图合成、时间合成和实时渲染等任务。 et.al.|[2309.13101](http://arxiv.org/abs/2309.13101)|null|
|**2023-09-22**|**NeRRF: 3D Reconstruction and View Synthesis for Transparent and Specular Objects with Neural Refractive-Reflective Fields**|神经辐射场（NeRF）已经彻底改变了基于图像的视图合成领域。然而，NeRF使用直线光线，无法处理由折射和反射引起的复杂光路变化。这阻碍了NeRF成功合成透明或镜面物体，而这些物体在现实世界的机器人和A/VR应用中无处不在。本文介绍了折射反射场。以物体轮廓为输入，我们首先利用渐进编码的行进四面体来重建非朗伯物体的几何结构，然后使用菲涅耳项在统一的框架中对物体的折射和反射效应进行建模。同时，为了实现高效、有效的抗混叠，我们提出了一种虚拟锥超采样技术。我们在真实世界和合成数据集的不同形状、背景和菲涅耳项上对我们的方法进行了基准测试。我们还对各种编辑应用程序的渲染结果进行了定性和定量的基准测试，包括材质编辑、对象替换/插入和环境照明估计。代码和数据可在https://github.com/dawning77/NeRRF. et.al.|[2309.13039](http://arxiv.org/abs/2309.13039)|**[link](https://github.com/dawning77/nerrf)**|
|**2023-09-21**|**ORTexME: Occlusion-Robust Human Shape and Pose via Temporal Average Texture and Mesh Encoding**|在单目视频的3D人体形状和姿势估计中，用有限的标记数据训练的模型不能很好地推广到具有遮挡的视频，这在野生视频中很常见。最近的人类神经渲染方法专注于由现成的人形和姿势方法初始化的新颖视图合成，具有校正初始人形的潜力。然而，现有的方法存在一些缺点，例如，在处理遮挡时出错，对不准确的人体分割敏感，以及由于非正则化的不透明度场而导致的无效损失计算。为了解决这些问题，我们引入了ORTexME，这是一种遮挡鲁棒的时间方法，它利用来自输入视频的时间信息来更好地正则化被遮挡的身体部位。虽然我们的ORTexME是基于NeRF的，但为了确定NeRF射线采样的可靠区域，我们利用我们新颖的平均纹理学习方法来学习人的平均外观，并基于平均纹理推断面具。此外，为了指导NeRF中的不透明度场更新以抑制模糊和噪声，我们建议使用人体网格。定量评估表明，我们的方法在具有挑战性的多人3DPW数据集上实现了显著的改进，其中我们的方法实现了1.8P-MPJPE的误差降低。基于SOTA渲染的方法失败了，并在同一数据集上将错误扩大到5.6。 et.al.|[2309.12183](http://arxiv.org/abs/2309.12183)|null|
|**2023-09-21**|**Fast Satellite Tensorial Radiance Field for Multi-date Satellite Imagery of Large Size**|现有的卫星图像NeRF模型速度较慢，必须输入太阳信息，并且在处理大型卫星图像方面存在局限性。作为回应，我们提出了SatensoRF，它显著加快了整个过程，同时为大尺寸卫星图像使用了更少的参数。此外，我们观察到，在神经辐射场中，朗伯表面的普遍假设不符合植物和水生元素。与传统的基于分层MLP的场景表示相比，我们选择了一种针对颜色、体积密度和辅助变量的多尺度张量分解方法来对具有镜面颜色的光场进行建模。此外，为了纠正多日期图像中的不一致性，我们结合了总变化损失来恢复密度张量场，并将该问题视为去噪任务。为了验证我们的方法，我们使用空间网多视图数据集的子集对SatensoRF进行了评估，该数据集包括多日期和单日期多视图RGB图像。我们的结果清楚地表明，SatensoRF在新颖的视图合成性能方面超过了最先进的Sat-NeRF系列。值得注意的是，SatensoRF需要更少的参数进行训练，从而提高训练和推理速度，降低计算需求。 et.al.|[2309.11767](http://arxiv.org/abs/2309.11767)|null|
|**2023-09-20**|**GenLayNeRF: Generalizable Layered Representations with 3D Model Alignment for Multi-Human View Synthesis**|由于复杂的人与人之间的遮挡，多人场景的新视图合成（NVS）带来了挑战。分层表示通过将场景划分为多层辐射场来处理复杂性，然而，它们主要局限于逐场景优化，因此效率低下。可泛化的人体视图合成方法将预先拟合的三维人体网格与图像特征相结合以达到泛化，但它们主要是针对单个人体场景设计的。另一个缺点是依赖于用于3D身体模型的参数预拟合的多步骤优化技术，该3D身体模型在稀疏视图设置中与图像不对准，从而导致合成视图中的幻觉。在这项工作中，我们提出了GenLayNeRF，这是一种可推广的分层场景表示，用于多个人类主体的自由视点渲染，不需要每场景优化和非常稀疏的视图作为输入。我们将场景划分为由3D身体网格锚定的多个人体层。然后，我们通过一个新颖的端到端可训练模块确保身体模型与输入视图的像素级对齐，该模块执行迭代参数校正，并结合多视图特征融合，以产生对齐的3D模型。对于NVS，我们提取逐点图像对齐和人锚定的特征，这些特征使用自注意和交叉注意模块进行关联和融合。我们使用基于注意力的RGB融合模块将低级别的RGB值增强到特征中。为了评估我们的方法，我们构建了两个多人视角合成数据集；DeepMultiSyn和ZJU MultiHuman。结果表明，在没有测试时间优化的情况下，我们提出的方法优于可推广的和非人类的每场景NeRF方法，同时与分层的每场景方法不相上下。 et.al.|[2309.11627](http://arxiv.org/abs/2309.11627)|null|
|**2023-09-23**|**Light Field Diffusion for Single-View Novel View Synthesis**|单视图新视图合成，即基于单个参考图像从新视点生成图像的任务，是计算机视觉中一项重要但具有挑战性的任务。近年来，去噪扩散概率模型（DDPM）由于其强大的高保真度图像生成能力而在该领域流行起来。然而，当前基于扩散的方法直接依赖于相机姿态矩阵作为观看条件，全局地和隐含地引入3D约束。这些方法可能存在从不同角度生成的图像之间的不一致性，特别是在具有复杂纹理和结构的区域中。在这项工作中，我们提出了光场扩散（LFD），这是一种基于条件扩散的单视图新视图合成模型。与以前使用相机姿态矩阵的方法不同，LFD将相机视图信息转换为光场编码，并将其与参考图像相结合。这种设计在扩散模型中引入了局部像素约束，从而促进了更好的多视图一致性。在几个数据集上的实验表明，我们的LFD可以有效地生成高保真图像，即使在复杂的区域也能保持更好的3D一致性。我们的方法可以生成比基于NeRF的模型质量更高的图像，并且我们获得的样本质量与其他基于扩散的模型类似，但只有模型大小的三分之一。 et.al.|[2309.11525](http://arxiv.org/abs/2309.11525)|null|
|**2023-09-21**|**Controllable Dynamic Appearance for Neural 3D Portraits**|神经辐射场（NeRF）的最新进展使得通过控制头部姿势、面部表情和观看方向来重建和恢复动态人像场景成为可能。然而，训练这样的模型假设变形区域的光度一致性，例如，随着头部姿势和面部表情的变化，面部变形时必须均匀照明。即使在工作室环境中，视频各帧之间的这种光度一致性也很难保持，因此，创建的可重影神经肖像在重影过程中容易出现伪影。在这项工作中，我们提出了CoDyNeRF，这是一种能够在真实世界的捕捉条件下创建完全可控的3D肖像的系统。CoDyNeRF通过规范空间中的动态外观模型来学习近似照明相关效果，该模型以预测的表面法线、面部表情和头部姿势变形为条件。表面法线预测是使用3DMM法线来指导的，3DMM法线充当人类头部法线的粗略先验，其中由于头部姿势和面部表情变化引起的刚性和非刚性变形，很难直接预测法线。仅使用智能手机拍摄的受试者短视频进行训练，我们就展示了我们的方法在具有明确的头部姿势和表情控制以及逼真照明效果的人像场景的自由视图合成方面的有效性。项目页面可在此处找到：http://shahrukhathar.github.io/2023/08/22/CoDyNeRF.html et.al.|[2309.11009](http://arxiv.org/abs/2309.11009)|null|

<p align=right>(<a href=#updated-on-20230928>back to top</a>)</p>

## 3D Reconstruction

|Publish Date|Title|Abstract|PDF|Code|
|---|---|---|---|---|
|**2023-09-26**|**3D Reconstruction with Generalizable Neural Fields using Scene Priors**|由于神经领域的最新进展，高保真3D场景重建得到了实质性的推进。然而，大多数现有的方法为每个单独的场景从头开始训练单独的网络。这是不可扩展的，效率低下，并且在视图有限的情况下无法产生良好的结果。虽然基于学习的多视图立体方法在一定程度上缓解了这一问题，但它们的多视图设置使其扩展和广泛应用的灵活性降低。相反，我们引入了结合场景先验（NFP）的训练可推广神经场。NFP网络将任何单视图RGB-D图像映射为带符号的距离和辐射值。在没有融合模块的情况下，可以通过合并体积空间中的各个帧来重建完整的场景，这提供了更好的灵活性。场景先验可以在大规模数据集上进行训练，从而能够快速适应具有较少视图的新场景的重建。NFP不仅展示了SOTA场景重建的性能和效率，而且还支持单图像新视图合成，这在神经领域还没有得到充分的探索。更多定性结果可在以下网站获得：https://oasisyang.github.io/neural-prior et.al.|[2309.15164](http://arxiv.org/abs/2309.15164)|null|
|**2023-09-26**|**Combining optical diffraction tomography with imaging flow cytometry for characterizing morphology, hemoglobin content, and membrane deformability of live red blood cells**|将光学衍射层析成像与成像流式细胞术相结合，可以对红细胞（RBCs）的自然形式的三维（3D）形态和血红蛋白含量进行无标记定量。在微流体通道中流动的RBCs的自旋转已被用于实现3D重建的各种投影方向。然而，这项技术的实用性还没有得到充分的研究。我们提高了估算红细胞旋转角度的准确性，并展示了健康红细胞和戊二醛处理红细胞的3D重建。结果显示，能够量化戊二醛处理产生的红细胞形态、血红蛋白含量和膜波动的变化，证明了检测各种红细胞膜疾病中常见变化的潜力。 et.al.|[2309.15131](http://arxiv.org/abs/2309.15131)|null|
|**2023-09-26**|**PHRIT: Parametric Hand Representation with Implicit Template**|我们提出了PHRIT，这是一种使用隐式模板进行参数化手网格建模的新方法，它结合了参数化网格和隐式表示的优点。我们的方法使用带符号距离场（SDF）和基于零件的形状先验来表示可变形的手部形状，利用变形场来执行变形。该模型通过以无限分辨率变形规范模板来提供高效的高保真手部重建。此外，它是完全可微的，并且可以很容易地用于手建模，因为它可以由骨架和形状潜在代码驱动。我们在多个下游任务上对PHRIT进行了评估，包括骨骼驱动的手部重建、点云形状和单视图3D重建，证明了我们的方法以最先进的性能实现了逼真和身临其境的手部建模。 et.al.|[2309.14916](http://arxiv.org/abs/2309.14916)|null|
|**2023-09-26**|**Unsupervised Reconstruction of 3D Human Pose Interactions From 2D Poses Alone**|由于单目图像中的视角模糊性，当前的无监督2D-3D人体姿态估计（HPE）方法在多人场景中不起作用。因此，我们提出了第一项研究，仅从2D姿势研究无监督多人2D-3D HPE的可行性，重点是重建人类互动。为了解决视角模糊的问题，我们通过预测摄像机相对于受试者骨盆的仰角来扩展先前的工作。这使我们能够将预测的姿势旋转到与地平面齐平的位置，同时获得个体之间3D垂直偏移的估计值。我们的方法包括独立地将每个受试者的2D姿势提升到3D，然后将它们组合到共享的3D坐标系中。然后，在缩放之前，将姿势旋转并偏移预测的仰角。这本身就使我们能够检索到他们姿势的精确3D重建。我们在CHI3D数据集上展示了我们的结果，介绍了它在无监督2D-3D姿态估计中的应用，以及三种新的定量指标，并为未来的研究建立了基准。 et.al.|[2309.14865](http://arxiv.org/abs/2309.14865)|null|
|**2023-09-26**|**Three-dimensional Tracking of a Large Number of High Dynamic Objects from Multiple Views using Current Statistical Model**|从多个视图对多个对象进行三维跟踪有着广泛的应用，特别是在需要研究对象精确轨迹的生物集群行为研究中。然而，当物体彼此相似、频繁机动和大量聚集时，存在显著的时空关联不确定性。针对这种多视图多目标三维跟踪场景，在贝叶斯跟踪的同时重构框架下，提出了一种基于统计模型的卡尔曼粒子滤波器（CSKPF）方法。CSKPF算法通过当前统计模型预测对象的状态，估计对象的状态协方差对重要粒子采样效率的影响，并通过卡尔曼滤波器抑制测量噪声。仿真实验证明，与现有的基于恒速的粒子滤波器（CVPF）方法相比，CSKPF方法可以提高跟踪的完整性、连续性和精度。对果蝇集群的实际实验也证实了CSKPF方法的有效性。 et.al.|[2309.14820](http://arxiv.org/abs/2309.14820)|null|
|**2023-09-26**|**3D Density-Gradient based Edge Detection on Neural Radiance Fields (NeRFs) for Geometric Reconstruction**|从神经辐射场（NeRF）生成几何三维重建是一个非常有趣的问题。然而，基于密度值的准确和完整的重建是具有挑战性的。网络输出取决于输入数据、NeRF网络配置和超参数。因此，密度值的直接使用，例如通过全局密度阈值的过滤，通常需要经验调查。在密度从非物体区域增加到物体区域的假设下，相对值的密度梯度的利用是明显的。由于密度表示与位置相关的参数，因此可以各向异性地处理它，因此对体素化3D密度场的处理是合理的。在这方面，我们处理基于密度梯度的几何3D重建，而梯度来自一阶和二阶导数的3D边缘检测滤波器，即Sobel、Canny和拉普拉斯高斯。梯度依赖于所有方向上的相对相邻密度值，因此与绝对大小无关。因此，梯度滤波器能够提取宽密度范围的边缘，几乎独立于假设和经验调查。我们的方法证明了在物体表面以高几何精度和显著的物体完整性实现几何三维重建的能力。值得注意的是，Canny滤波器有效地消除了间隙，提供了均匀的点密度，并在整个场景的正确性和完整性之间取得了良好的平衡。 et.al.|[2309.14800](http://arxiv.org/abs/2309.14800)|null|
|**2023-09-24**|**Deep learning based workflow for accelerated industrial X-ray Computed Tomography**|X射线计算机断层扫描（XCT）是对添加制造的金属部件进行高分辨率无损表征的重要工具。金属部件的XCT重建可能具有束硬化伪影，如杯状和条纹，这使得对缺陷和缺陷的可靠检测具有挑战性。此外，基于使用分析重建算法的传统工作流程需要大量投影才能准确表征，这导致测量时间更长，并阻碍了XCT用于在线检测。在本文中，我们介绍了一种新的工作流程，该工作流程基于使用两个神经网络，从单一材料金属零件的稀疏视图XCT扫描中获得高质量的加速重建。第一个网络使用完全连接的层实现，有助于减少BH在投影数据中的影响，而无需任何校准或了解组件材料。第二个网络是卷积神经网络，它将低质量的分析三维重建映射为高质量的重建。使用实验数据，我们证明了我们的方法在几种合金中稳健地推广，并适用于一系列稀疏性水平，而无需重新训练网络，从而实现准确快速的工业XCT检查。 et.al.|[2309.14371](http://arxiv.org/abs/2309.14371)|null|
|**2023-09-25**|**A Novel Approach for Effective Multi-View Clustering with Information-Theoretic Perspective**|多视图集群（MVC）是一种流行的技术，用于使用各种数据源来提高集群性能。然而，现有的方法主要侧重于获取一致的信息，而往往忽略了跨多个视图的冗余问题。本研究提出了一种新的方法，称为充分多视图聚类（SUMVC），从信息论的角度考察了多视图聚类框架。我们提出的方法由两部分组成。首先，我们开发了一种简单可靠的多视图聚类方法SCMVC（简单一致多视图聚类），该方法采用变分分析来生成一致信息。其次，我们提出了一个充分的表示下界，以增强视图之间的一致性信息并最大限度地减少不必要的信息。所提出的SUMVC方法为多视图聚类问题提供了一种很有前途的解决方案，并为分析多视图数据提供了一个新的视角。为了验证我们模型的有效性，我们基于贝叶斯错误率进行了理论分析，并在多个多视图数据集上进行了实验，证明了SUMVC的优越性能。 et.al.|[2309.13989](http://arxiv.org/abs/2309.13989)|null|
|**2023-09-24**|**Federated Deep Multi-View Clustering with Global Self-Supervision**|联合多视图集群有可能从分布在多个设备上的数据中学习全局集群模型。在这种情况下，标签信息是未知的，必须保护数据隐私，这导致了两大挑战。首先，不同客户端上的视图通常具有特征异构性，挖掘它们互补的集群信息并非易事。其次，在分布式环境中存储和使用来自多个客户端的数据会导致多视图数据的不完整性。为了应对这些挑战，我们提出了一种新的联邦深度多视图聚类方法，该方法可以从多个客户端挖掘互补的集群结构，同时处理数据的不完整性和隐私问题。具体来说，在服务器环境中，我们提出了样本对齐和数据扩展技术来探索多个视图的互补集群结构。然后，服务器将全局原型和全局伪标签作为全局自监督信息分发给每个客户端。在客户端环境中，多个客户端使用全局自监督信息和深度自动编码器来学习特定于视图的集群分配和嵌入特征，然后将其上传到服务器以细化全局自监督的信息。最后，我们广泛的实验结果表明，我们提出的方法在解决分布式环境中不完整多视图数据的挑战方面表现出优异的性能。 et.al.|[2309.13697](http://arxiv.org/abs/2309.13697)|null|
|**2023-09-23**|**MP-MVS: Multi-Scale Windows PatchMatch and Planar Prior Multi-View Stereo**|在提高基于多视图立体（MVS）的3D重建的准确性方面已经取得了重大进展。然而，具有不稳定光度一致性的无纹理区域通常仍不完全重建。在本文中，我们提出了一种弹性和有效的多视图立体方法（MP-MVS）。我们设计了一个多尺度窗口PatchMatch（mPM）来获得可靠的无纹理区域深度。与其他多尺度方法相比，后者速度更快，可以很容易地扩展到基于PatchMatch的MVS方法。随后，我们通过将采样限制在遥远的区域来改进现有的棋盘采样方案，这可以有效地提高空间传播的效率，同时减少异常值的生成。最后，我们介绍并改进了ACMP的平面先验辅助PatchMatch。我们不依赖光度一致性，而是利用多视图之间的几何一致性信息来选择可靠的三角顶点。该策略可以获得更精确的平面先验模型来校正光度一致性测量。我们的方法已经在ETH3D高分辨率多视图基准上用几种最先进的方法进行了测试。结果表明，我们的方法可以达到最先进的水平。相关代码可访问https://github.com/RongxuanTan/MP-MVS. et.al.|[2309.13294](http://arxiv.org/abs/2309.13294)|**[link](https://github.com/rongxuantan/mp-mvs)**|

<p align=right>(<a href=#updated-on-20230928>back to top</a>)</p>

## Diffusion

|Publish Date|Title|Abstract|PDF|Code|
|---|---|---|---|---|
|**2023-09-27**|**Exploiting the Signal-Leak Bias in Diffusion Models**|大多数扩散模型的推理管道都存在偏差。这种偏差源于信号泄漏，其分布偏离噪声分布，从而在训练和推理过程之间产生差异。我们证明，当模型被调整到特定风格时，这种信号泄漏偏差特别显著，导致次优风格匹配。最近的研究试图避免训练过程中的信号泄漏。相反，我们展示了如何在现有的扩散模型中利用这种信号泄漏偏差，以便对生成的图像进行更多的控制。这使我们能够生成亮度变化更大的图像，以及更好地匹配所需风格或颜色的图像。通过对信号泄漏在空间频率和像素域中的分布进行建模，并将信号泄漏包括在初始潜影中，我们生成的图像更好地匹配预期结果，而无需任何额外的训练。 et.al.|[2309.15842](http://arxiv.org/abs/2309.15842)|null|
|**2023-09-27**|**Show-1: Marrying Pixel and Latent Diffusion Models for Text-to-Video Generation**|在大规模预训练的文本到视频扩散模型（VDM）领域已经取得了重大进展。然而，以前的方法要么只依赖于具有高计算成本的基于像素的VDM，要么依赖于通常难以精确对齐文本视频的基于潜在的VDM。在本文中，我们首次提出了一种混合模型，称为Show-1，它结合了基于像素和基于潜像的VDM，用于文本到视频的生成。我们的模型首先使用基于像素的VDM来产生具有强文本视频相关性的低分辨率视频。之后，我们提出了一种新的专家翻译方法，该方法使用基于潜在的VDM来进一步将低分辨率视频上采样到高分辨率。与潜在的VDM相比，Show-1可以制作精确文本视频对齐的高质量视频；与像素VDM相比，Show-1的效率高得多（推理过程中GPU内存的使用量为15G，而不是72G）。我们还在标准视频生成基准上验证了我们的模型。我们的代码和模型权重可在\url上公开获取{https://github.com/showlab/Show-1}。 et.al.|[2309.15818](http://arxiv.org/abs/2309.15818)|null|
|**2023-09-27**|**Distinguishing between long-transient and asymptotic states in a biological aggregation model**|聚集是许多生物系统共同的新兴特征。因此，理解它们出现的数学模型非常普遍，聚集-扩散方程就是一个典型的例子。本文研究了具有线性扩散的聚集扩散方程。已知该等式支持同时涉及单个和多个聚合的解决方案。然而，数值证据表明，后者，我们称之为“多峰值解”，可能通常是长瞬态解，而不是渐近稳态。我们开发了一种通过能量最小化方法区分长瞬态和渐近稳态的新技术。该技术包括首先使用极限过程和力矩闭合程序来近似我们的研究方程。然后，我们分析了这个近似系统的局部最小能量态，假设这些状态将对应于聚集-扩散方程中的渐近模式。最后，我们通过数值研究验证了我们的假设，表明我们的近似分析技术可以很好地预测一个状态是渐近的还是长瞬态的。总的来说，我们发现除了一些非常特殊的情况外，几乎所有的双峰和多峰解都是瞬态的。我们在数值上证明了这些瞬态可以任意长寿命，这取决于系统的参数。 et.al.|[2309.15810](http://arxiv.org/abs/2309.15810)|null|
|**2023-09-27**|**Emu: Enhancing Image Generation Models Using Photogenic Needles in a Haystack**|使用网络规模的图像-文本对训练文本到图像模型能够从文本生成广泛的视觉概念。然而，这些预先训练的模型在生成高度美观的图像时往往面临挑战。这就产生了在预训练后进行美学调整的需求。在本文中，我们提出了质量调整，以有效地指导预先训练的模型专门生成具有高度视觉吸引力的图像，同时保持视觉概念的通用性。我们的关键见解是，用一组小得惊人但极具视觉吸引力的图像进行监督微调可以显著提高生成质量。我们在价值11亿美元的图像-文本对上预训练了一个潜在扩散模型，并仅用几千张精心选择的高质量图像对其进行微调。与仅经过预训练的模型相比，最终模型Emu的胜率为82.9%$。与最先进的SDXLv1.0相比，在标准PartiPrompts和我们基于文本到图像模型的真实世界使用的开放用户输入基准测试上，Emu在视觉吸引力方面的时间分别为68.4\%%和71.3\%%。此外，我们还表明，质量调整是一种通用方法，对其他架构也有效，包括像素扩散和掩蔽生成变换器模型。 et.al.|[2309.15807](http://arxiv.org/abs/2309.15807)|null|
|**2023-09-27**|**A note on asymptotics of linear dissipative kinetic equations in bounded domains**|我们建立了线性耗散动力学方程（包括时间松弛和Fokker-Planck模型）在有界空间域中的 $L^2$-指数衰减性质，该方程具有可能不守恒质量的一般边界条件。它们在$L^2$中的扩散渐近线也在一般Maxwell边界条件下导出。这些证明只是基于能量估计，以及以前从$L^2$ -次可乘性和相对熵方法中得出的想法。 et.al.|[2309.15758](http://arxiv.org/abs/2309.15758)|null|
|**2023-09-27**|**Statistically self-similar mixing by Gaussian random fields**|我们研究了 $\mathbb｛R｝^d$上空间光滑但时间为白色的不可压缩高斯随机速度场对标量场的被动输运。如果速度场$u$是均匀的、各向同性的，并且在统计上是自相似的，我们导出了一个精确的公式，该公式可以捕捉非扩散混合。对于零扩散率，公式的形状为$\mathbb｛E｝\|\theta_t\|_｛\dot｛H｝^｛-s｝｝^2=\mathrm｛E｝^｝-\lambda\｛d，s｝t｝\|| \theta_0\|_｛\dot｛H}^｛-s｝^2$，其中任何$s\in（0，d/2）$和$\frac｛\lambda_{d，s}｝｛d_1｝：=s（\frac{D_1}-2s)$，其中$\lambda_1/D_1=D$是与$u$产生的随机拉格朗日流相关的顶部李雅普诺夫指数，$D_1$是速度的小尺度剪切率。此外，混合被证明在扩散率上保持$\textit{均匀}$ 。 et.al.|[2309.15744](http://arxiv.org/abs/2309.15744)|null|
|**2023-09-27**|**Factorized Diffusion Architectures for Unsupervised Image Generation and Segmentation**|我们开发了一种神经网络架构，该架构以无监督的方式训练为去噪扩散模型，同时学习生成和分割图像。学习完全由去噪扩散目标驱动，在训练过程中没有任何关于区域的注释或先验知识。神经结构中内置的计算瓶颈鼓励去噪网络将输入划分为多个区域，并行去噪，并将结果组合起来。我们训练的模型生成合成图像，并通过简单检查其内部预测分区来生成这些图像的语义分割。在没有任何微调的情况下，我们直接将我们的无监督模型应用于下游任务，即通过去噪对真实图像进行分割，然后对其进行去噪。实验表明，我们的模型在多个数据集上实现了精确的无监督图像分割和高质量的合成图像生成。 et.al.|[2309.15726](http://arxiv.org/abs/2309.15726)|null|
|**2023-09-27**|**Dynamic Prompt Learning: Addressing Cross-Attention Leakage for Text-Based Image Editing**|大规模的文本到图像生成模型是生成人工智能的突破性发展，扩散模型显示出在输入文本提示后合成令人信服的图像的惊人能力。图像编辑研究的目标是通过修改文本提示，让用户控制生成的图像。当前的图像编辑技术容易受到目标区域之外的区域的意外修改的影响，例如在背景上或在与目标对象具有某种语义或视觉关系的干扰物对象上。根据我们的实验发现，不准确的交叉注意力图是这个问题的根源。基于这一观察，我们提出了动态提示学习（DPL），以迫使跨注意力地图在文本提示中关注正确的名词词。通过用所提出的泄漏修复损失更新文本输入中名词的动态标记，我们实现了对特定对象的细粒度图像编辑，同时防止对其他图像区域的不期望的更改。我们的方法DPL基于公开的Stable Diffusion，在广泛的图像上进行了广泛的评估，并在定量（CLIP评分，Structure Dist）和定性（用户评估）方面始终获得优异的结果。我们展示了Word Swap、prompt Refinement和Attention Re-weighting的改进提示编辑结果，特别是对于复杂的多对象场景。 et.al.|[2309.15664](http://arxiv.org/abs/2309.15664)|**[link](https://github.com/wangkai930418/DPL)**|
|**2023-09-27**|**Direct Sensing of Remote Nuclei: Expanding the Reach of Cross-Effect Dynamic Nuclear Polarization**|动态核极化（DNP）显著提高了核磁共振实验的灵敏度，从而彻底改变了固态核磁共振波谱领域。传统上，交叉效应DNP依赖于双自由基将极化从耦合的电子自旋转移到附近的核自旋，然后通过自旋扩散机制传递到靶核。然而，极化直接转移到遥远的原子核仍然是一个重大挑战，限制了它在各种情况下的适用性。在这项工作中，我们提出了一种新的双自由基设计概念，该概念涉及大小为数百MHz的非常强的电子-电子耦合，这使得能够在超过2.0 nm的更长距离上从电子自旋到核自旋的有效直接极化转移。我们讨论了这种定制的双自由基在传统自旋扩散机制效率低下或需要通过电子-自旋相互作用进行直接核自旋传感的情况下的潜力。我们的研究为扩大固态NMR光谱中交叉效应DNP的范围提供了一条很有前途的途径，并为研究广泛的生物和材料系统开辟了新的机会。我们的研究还提供了对商业上可获得的双自由基的DNP形成时间的见解。 et.al.|[2309.15653](http://arxiv.org/abs/2309.15653)|null|
|**2023-09-27**|**Large deviations for trajectory observables of diffusion processes in dimension $d>1$ in the double limit of large time and small diffusion coefficient**|对于维度$d>1$的扩散过程，可以通过福克-普朗克发生器的Feynman-Kac变形来研究时间窗口$[0，T]$上的轨迹可观察性的统计，该变形可以被解释为欧氏非厄米电磁量子哈密顿量。然后，比较与时间$T$（有限或大）和扩散系数$D$（有限/小）相对应的四种状态是有趣的。（1） 对于有限的$T$和有限的$D$，需要考虑涉及哈密顿量全谱的全时变量子问题。（2） 对于大时间$T\to+\infty$和有限的$D$，只需要考虑量子哈密顿量的基态性质，就可以得到重标累积量的生成函数，并构造相应的正则条件过程。（3） 对于有限的$T$和$D\到0$，只需要考虑满足Hamilton-Jacobi方程的主导经典轨迹及其作用，就像在量子力学的半经典WKB近似中一样。（4） 在双极限$T\to+\infty$和$D\to0$中，轨迹可观测性的$\frac｛T｝｛D｝$大偏差的简化可以通过两阶极限来分析，即从（2）的量子哈密顿的基态性质的极限$D\~0$，或者在（3）的半经典WKB近似中从长经典轨迹$T\的极限到+\infty$。该一般框架在具有旋转不变性的维度$d=2$ 中进行了说明。 et.al.|[2309.15542](http://arxiv.org/abs/2309.15542)|null|

<p align=right>(<a href=#updated-on-20230928>back to top</a>)</p>

## NeRF

|Publish Date|Title|Abstract|PDF|Code|
|---|---|---|---|---|
|**2023-09-27**|**SHACIRA: Scalable HAsh-grid Compression for Implicit Neural Representations**|隐式神经表示（INR）或神经场已成为编码多媒体信号（如图像和辐射场）同时保持高质量的流行框架。最近，Instant NGP提出的可学习特征网格通过用特征向量的多分辨率查找表和更小的神经网络取代大型神经网络，在训练和INR采样方面实现了显著的加速。然而，这些功能网格是以大量内存消耗为代价的，这可能是存储和流应用程序的瓶颈。在这项工作中，我们提出了SHACIRA，这是一个简单而有效的任务无关框架，用于压缩这种特征网格，而不需要额外的事后修剪/量化阶段。我们用量化的潜在权重对特征网格进行重新参数化，并在潜在空间中应用熵正则化，以在各个领域实现高水平的压缩。在由图像、视频和辐射场组成的不同数据集上的定量和定性结果表明，我们的方法优于现有的INR方法，而不需要任何大型数据集或特定领域的启发式方法。我们的项目页面可在http://shacira.github.io。 et.al.|[2309.15848](http://arxiv.org/abs/2309.15848)|null|
|**2023-09-27**|**NeuRBF: A Neural Fields Representation with Adaptive Radial Basis Functions**|我们提出了一种新型的神经场，它使用一般的径向基来表示信号。现有技术的神经领域通常依赖于用于存储局部神经特征的基于网格的表示和用于在连续查询点处插值特征的N维线性核。它们的神经特征的空间位置固定在网格节点上，不能很好地适应目标信号。相反，我们的方法建立在具有灵活内核位置和形状的通用径向基上，这些径向基具有更高的空间自适应性，可以更紧密地拟合目标信号。为了进一步提高径向基函数的信道容量，我们建议将它们与多频率正弦函数组合。该技术将径向基扩展到不同频带的多个傅立叶径向基，而不需要额外的参数，便于细节的表示。此外，通过将自适应径向基与基于网格的径向基相结合，我们的混合组合继承了自适应性和插值平滑性。我们精心设计了加权方案，使径向基有效地适应不同类型的信号。我们在2D图像和3D符号距离场表示上的实验证明了我们的方法比现有技术更高的精度和紧凑性。当应用于神经辐射场重建时，我们的方法实现了最先进的渲染质量，模型大小小，训练速度相当。 et.al.|[2309.15426](http://arxiv.org/abs/2309.15426)|null|
|**2023-09-26**|**3D Reconstruction with Generalizable Neural Fields using Scene Priors**|由于神经领域的最新进展，高保真3D场景重建得到了实质性的推进。然而，大多数现有的方法为每个单独的场景从头开始训练单独的网络。这是不可扩展的，效率低下，并且在视图有限的情况下无法产生良好的结果。虽然基于学习的多视图立体方法在一定程度上缓解了这一问题，但它们的多视图设置使其扩展和广泛应用的灵活性降低。相反，我们引入了结合场景先验（NFP）的训练可推广神经场。NFP网络将任何单视图RGB-D图像映射为带符号的距离和辐射值。在没有融合模块的情况下，可以通过合并体积空间中的各个帧来重建完整的场景，这提供了更好的灵活性。场景先验可以在大规模数据集上进行训练，从而能够快速适应具有较少视图的新场景的重建。NFP不仅展示了SOTA场景重建的性能和效率，而且还支持单图像新视图合成，这在神经领域还没有得到充分的探索。更多定性结果可在以下网站获得：https://oasisyang.github.io/neural-prior et.al.|[2309.15164](http://arxiv.org/abs/2309.15164)|null|
|**2023-09-22**|**NOC: High-Quality Neural Object Cloning with 3D Lifting of Segment Anything**|随着神经领域的发展，从多视图输入重建目标物体的3D模型最近越来越受到社会的关注。现有的方法通常学习整个场景的神经场，而如何在飞行中重建用户指示的特定对象仍在探索之中。考虑到分段任意模型（SAM）在分割任何2D图像方面都显示出了有效性，本文提出了一种新的高质量3D对象重建方法——神经对象克隆（NOC），它从两个方面利用了神经场和SAM的优点。首先，为了将目标对象从场景中分离出来，我们提出了一种新的策略，将SAM的多视图2D分割掩模提升到一个统一的3D变化场中。然后，3D变化场被投影到2D空间中，并生成SAM的新提示。这个过程是迭代的，直到收敛，以将目标对象从场景中分离出来。然后，除了2D掩模之外，我们进一步将SAM编码器的2D特征提升到3D SAM场中，以提高目标对象的重建质量。NOC将SAM的2D掩模和特征提升到3D神经场中，用于高质量的目标对象重建。我们在几个基准数据集上进行了详细的实验，以证明我们的方法的优势。代码将被发布。 et.al.|[2309.12790](http://arxiv.org/abs/2309.12790)|null|
|**2023-09-15**|**Breathing New Life into 3D Assets with Generative Repainting**|基于扩散的文本到图像模型引发了视觉社区、艺术家和内容创作者的巨大关注。这些模型的广泛采用是由于世代质量的显著提高以及对各种模式的有效调节，而不仅仅是文本。然而，将这些2D模型的丰富生成先验提升到3D中是具有挑战性的。最近的工作提出了由扩散模型和神经场的纠缠提供动力的各种管道。我们探索了预训练的2D扩散模型和标准3D神经辐射场作为独立工具的威力，并展示了它们以非学习方式协同工作的能力。这种模块化具有易于部分升级的内在优势，这在这样一个快节奏的领域中成为了一个重要的特性。我们的管道接受任何遗留的可渲染几何体，如纹理或无纹理网格，协调2D生成细化和3D一致性强制工具之间的交互，并以多种格式输出绘制的输入几何体。我们对ShapeNetSem数据集中的广泛对象和类别进行了大规模研究，并从定性和定量两个方面展示了我们方法的优势。项目页面：https://www.obukhov.ai/repainting_3d_assets et.al.|[2309.08523](http://arxiv.org/abs/2309.08523)|**[link](https://github.com/kongdai123/repainting_3d_assets)**|
|**2023-09-14**|**Neural Field Representations of Articulated Objects for Robotic Manipulation Planning**|传统的操作规划方法依赖于环境的显式几何模型来将给定任务公式化为优化问题。然而，从原始传感器输入推断准确的模型本身就是一个难题，尤其是对于铰接物体（例如壁橱、抽屉）。在本文中，我们提出了一种关节对象的神经场表示（NFR），可以直接从图像中进行操作规划。具体来说，在拍摄了一个新的关节物体的几张照片后，我们可以向前模拟它可能的运动，因此，可以直接使用该神经模型进行轨迹优化规划。此外，这种表示可以用于形状重建、语义分割和图像渲染，这在训练和泛化过程中提供了强大的监督信号。我们表明，我们的模型仅在合成图像上训练，能够在模拟和真实图像中为同类看不见的物体提取有意义的表示。此外，我们证明了该表示能够直接从图像中对现实世界中的关节物体进行机器人操作。 et.al.|[2309.07620](http://arxiv.org/abs/2309.07620)|null|
|**2023-09-13**|**Generalizable Neural Fields as Partially Observed Neural Processes**|神经场将信号表示为由神经网络参数化的函数，是传统离散矢量或基于网格的表示的一种很有前途的替代方案。与离散表示相比，神经表示既能很好地扩展分辨率，又是连续的，并且可以是多次可微的。然而，给定我们想要表示的信号数据集，必须为每个信号优化单独的神经场是低效的，并且不能利用信号之间的共享信息或结构。现有的泛化方法将其视为元学习问题，并采用基于梯度的元学习来学习初始化，然后通过测试时间优化对初始化进行微调，或者学习超网络来产生神经场的权重。相反，我们提出了一种新的范式，将神经表征的大规模训练视为部分观察到的神经过程框架的一部分，并利用神经过程算法来解决这一任务。我们证明，这种方法优于最先进的基于梯度的元学习方法和超网络方法。 et.al.|[2309.06660](http://arxiv.org/abs/2309.06660)|null|
|**2023-09-08**|**Single View Refractive Index Tomography with Neural Fields**|折射率层析成像是一个反问题，我们试图从2D投影图像测量中重建场景的3D折射场。折射场本身是不可见的，而是影响光线在空间中传播时路径的连续弯曲。折射场出现在各种各样的科学应用中，从显微镜中的半透明细胞样本到弯曲来自遥远星系的光的暗物质场。这个问题带来了一个独特的挑战，因为折射场直接影响光的路径，使其恢复成为一个非线性问题。此外，与传统的层析成像相比，我们试图通过利用散射在整个介质中的光源的知识，仅从单个视点使用投影图像来恢复折射场。在这项工作中，我们介绍了一种使用基于坐标的神经网络对场景中潜在的连续折射场进行建模的方法。然后，我们使用射线三维空间曲率的显式建模来优化该网络的参数，通过综合分析方法重建折射场。通过在模拟中恢复折射场，并分析光源分布对恢复的影响，证明了我们方法的有效性。然后，我们在模拟暗物质映射问题上测试了我们的方法，在该问题中，我们恢复了真实模拟暗物质分布下的折射场。 et.al.|[2309.04437](http://arxiv.org/abs/2309.04437)|null|
|**2023-09-07**|**BluNF: Blueprint Neural Field**|神经辐射场（NeRF）彻底改变了场景新颖的视图合成，提供了视觉逼真、精确和稳健的隐式重建。虽然最近的方法允许NeRF编辑，例如对象删除、3D形状修改或材料特性操纵，但在这种编辑之前的手动注释使该过程变得乏味。此外，传统的2D交互工具缺乏对3D空间的准确感知，阻碍了对场景的精确操作和编辑。在本文中，我们介绍了一种新的方法，称为蓝图神经场（BluNF），以解决这些编辑问题。BluNF提供了一个强大且用户友好的2D蓝图，实现了直观的场景编辑。通过利用隐式神经表示，BluNF使用先前的语义和深度信息构建场景的蓝图。生成的蓝图可以轻松编辑和操作NeRF表示。我们通过直观的点击和更改机制展示了BluNF的可编辑性，实现了3D操作，如遮罩、外观修改和对象移除。我们的方法对视觉内容创作做出了重大贡献，为该领域的进一步研究铺平了道路。 et.al.|[2309.03933](http://arxiv.org/abs/2309.03933)|null|
|**2023-09-07**|**SimNP: Learning Self-Similarity Priors Between Neural Points**|用于3D对象重建的现有神经场表示要么（1）利用对象级表示，但由于对全局潜在代码的限制而遭受低质量细节，要么（2）能够完美地重建观测，但未能利用对象级先验知识来推断未观察到的区域。我们提出了一种学习类别级自相似性的方法SimNP，它通过将神经点辐射场与类别级自类似性表示相连接，结合了两个世界的优点。我们的贡献是双重的。（1） 我们利用相干点云的概念设计了第一个类别级别的神经点表示。由此产生的神经点辐射场为局部支持的对象区域存储了高级别的细节。（2） 我们了解了如何以无约束和无监督的方式在神经点之间共享信息，这允许在重建过程中根据给定的观测值导出对象的未观察区域。我们表明，SimNP在重建对称的看不见物体区域方面优于以前的方法，超过了建立在类别级或像素对齐辐射场上的方法，同时提供了实例之间的语义对应 et.al.|[2309.03809](http://arxiv.org/abs/2309.03809)|null|

<p align=right>(<a href=#updated-on-20230928>back to top</a>)</p>

[contributors-shield]: https://img.shields.io/github/contributors/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[contributors-url]: https://github.com/Vincentqyw/cv-arxiv-daily/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[forks-url]: https://github.com/Vincentqyw/cv-arxiv-daily/network/members
[stars-shield]: https://img.shields.io/github/stars/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[stars-url]: https://github.com/Vincentqyw/cv-arxiv-daily/stargazers
[issues-shield]: https://img.shields.io/github/issues/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[issues-url]: https://github.com/Vincentqyw/cv-arxiv-daily/issues

