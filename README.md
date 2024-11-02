[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]

## Updated on 2024.11.02
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
|**2024-10-31**|**No Pose, No Problem: Surprisingly Simple 3D Gaussian Splats from Sparse Unposed Images**|我们介绍了NoPoSplat，这是一种前馈模型，能够从\textit{unfosed}稀疏多视图图像中重建由3D高斯参数化的3D场景。我们的模型仅使用光度损失进行训练，在推理过程中实现了实时3D高斯重建。为了在重建过程中消除对精确姿态输入的需求，我们将一个输入视图的局部相机坐标锚定为规范空间，并训练网络预测该空间内所有视图的高斯基元。这种方法避免了将高斯基元从局部坐标转换到全局坐标系的需要，从而避免了与每帧高斯和姿态估计相关的误差。为了解决尺度模糊问题，我们设计并比较了各种内在嵌入方法，最终选择将相机内在转换为令牌嵌入，并将其与图像令牌连接作为模型的输入，从而实现准确的场景尺度预测。我们利用重建的3D高斯分布进行新的视图合成和姿态估计任务，并提出了一种两阶段粗到细的流水线来进行精确的姿态估计。实验结果表明，与需要姿态的方法相比，我们的无姿态方法可以实现更优的新颖视图合成质量，特别是在输入图像重叠有限的情况下。对于姿态估计，我们的方法在没有地面真实深度或显式匹配损失的情况下进行训练，显著优于最先进的方法，并有了实质性的改进。这项工作在无姿态通用3D重建方面取得了重大进展，并证明了其适用于现实世界场景。代码和训练模型可在以下网址获得https://noposplat.github.io/. et.al.|[2410.24207](http://arxiv.org/abs/2410.24207)|**[link](https://github.com/cvg/NoPoSplat)**|
|**2024-10-31**|**GeoSplatting: Towards Geometry Guided Gaussian Splatting for Physically-based Inverse Rendering**|我们考虑了使用3D高斯散斑（3DGS）表示的基于物理的逆渲染问题。虽然最近的3DGS方法在新视图合成（NVS）方面取得了显著成果，但准确捕捉高保真几何体、物理可解释的材质和照明仍然具有挑战性，因为它需要精确的几何建模来提供精确的表面法线，以及基于物理的渲染（PBR）技术来确保正确的材质和光照解纠缠。以前的3DGS方法诉诸于近似曲面法线，但经常难以处理有噪声的局部几何，导致法线估计不准确和材质光照分解次优。本文介绍了GeoSplatting，这是一种新的混合表示，它通过显式几何引导和可微PBR方程来增强3DGS。具体来说，我们将等值面和3DGS连接在一起，首先从标量场中提取等值面网格，然后将其转换为3DGS点，并以完全可微的方式为它们制定PBR方程。在GeoSplatting中，3DGS基于网格几何，实现了精确的表面法线建模，这有助于使用PBR框架进行材料分解。这种方法进一步保持了3DGS的NVS的效率和质量，同时确保了等值面的精确几何形状。对不同数据集的综合评估表明了GeoSplatting的优越性，在定量和定性方面都始终优于现有方法。 et.al.|[2410.24204](http://arxiv.org/abs/2410.24204)|null|
|**2024-10-31**|**GaussianMarker: Uncertainty-Aware Copyright Protection of 3D Gaussian Splatting**|3D高斯散斑（3DGS）已成为获取3D资产的关键方法。为了保护这些资产的版权，可以应用数字水印技术将所有权信息谨慎地嵌入3DGS模型中。然而，现有的网格、点云和隐式辐射场的水印方法不能直接应用于3DGS模型，因为3DGS模型使用具有不同结构的显式3D高斯分布，不依赖于神经网络。在预训练的3DGS上直接嵌入水印会导致渲染图像明显失真。在我们的工作中，我们提出了一种基于不确定性的方法，该方法限制了模型参数的扰动，以实现3DGS的不可见水印。在消息解码阶段，即使在各种形式的3D和2D失真下，也可以从3D高斯和2D渲染图像中可靠地提取版权消息。我们在Blender、LLFF和MipNeRF-360数据集上进行了广泛的实验，以验证我们提出的方法的有效性，并在消息解码精度和视图合成质量方面展示了最先进的性能。 et.al.|[2410.23718](http://arxiv.org/abs/2410.23718)|null|
|**2024-10-31**|**Epipolar-Free 3D Gaussian Splatting for Generalizable Novel View Synthesis**|广义3D高斯分裂（3DGS）可以以前馈推理的方式从稀疏视图观测中重建新的场景，消除了传统3DGS中对场景特定再训练的需要。然而，现有的方法严重依赖于极线先验，这在复杂的现实世界场景中可能不可靠，特别是在非重叠和遮挡的区域。在本文中，我们提出了eFreeSplat，这是一种基于3DGS的高效前馈模型，用于独立于极线约束的可推广新型视图合成。为了增强具有3D感知的多视图特征提取，我们在大规模数据集上采用了具有跨视图完成预训练的自监督视觉变换器（ViT）。此外，我们引入了一种迭代交叉视图高斯对齐方法，以确保不同视图之间的深度尺度一致。我们的eFreeSplat代表了一种可推广的新颖视图合成的创新方法。与现有的纯无几何方法不同，eFreeSplat更侧重于通过跨视图预训练提供3D先验来实现无极线特征匹配和编码。我们使用RealEstate10K和ACID数据集在宽基线新视图合成任务上评估eFreeSplat。大量实验表明，eFreeSplat超越了依赖极线先验的最先进基线，实现了卓越的几何重建和新颖的视图合成质量。项目页面：https://tatakai1.github.io/efreesplat/. et.al.|[2410.22817](http://arxiv.org/abs/2410.22817)|null|
|**2024-10-29**|**PF3plat: Pose-Free Feed-Forward 3D Gaussian Splatting**|我们考虑了在单个前馈中从非聚焦图像合成新视图的问题。我们的框架利用了3DGS的快速、可扩展性和高质量的3D重建和视图合成功能，我们进一步扩展了它，提供了一种实用的解决方案，放宽了常见的假设，如密集的图像视图、精确的相机姿态和大量的图像重叠。我们通过识别和解决使用像素对齐的3DGS所带来的独特挑战来实现这一目标：不同视图中未对齐的3D高斯分布会导致噪声或稀疏梯度，从而破坏训练的稳定性并阻碍收敛，尤其是在不满足上述假设的情况下。为了减轻这种情况，我们采用预训练的单目深度估计和视觉对应模型来实现3D高斯的粗略对齐。然后，我们引入了轻量级、可学习的模块，从粗对准中细化深度和姿态估计，提高了3D重建的质量和新颖的视图合成。此外，利用精细估计来估计几何置信度得分，该得分评估3D高斯中心的可靠性，并相应地调节高斯参数的预测。对大规模真实世界数据集的广泛评估表明，PF3plat在所有基准测试中都达到了新的最先进水平，并得到了验证我们设计选择的全面消融研究的支持。 et.al.|[2410.22128](http://arxiv.org/abs/2410.22128)|**[link](https://github.com/cvlab-kaist/PF3plat)**|
|**2024-10-29**|**ActiveSplat: High-Fidelity Scene Reconstruction through Active Gaussian Splatting**|我们提出了ActivePlat，这是一个利用高斯飞溅的自主高保真重建系统。该系统利用高效逼真的渲染，为在线映射、视点选择和路径规划建立了一个统一的框架。ActivePlat的关键是一种混合地图表示，它集成了关于环境的密集信息和工作空间的稀疏抽象。因此，该系统利用稀疏拓扑进行高效的视点采样和路径规划，同时利用视图相关的密集预测进行视点选择，以有希望的准确性和完整性促进高效决策。在预算有限的情况下，采用基于拓扑图的分层规划策略来减少重复轨迹并提高局部粒度，确保通过逼真的视图合成进行高保真重建。广泛的实验和消融研究验证了所提出方法在重建精度、数据覆盖率和勘探效率方面的有效性。项目页面：https://li-yuetao.github.io/ActiveSplat/. et.al.|[2410.21955](http://arxiv.org/abs/2410.21955)|null|
|**2024-10-25**|**ArCSEM: Artistic Colorization of SEM Images via Gaussian Splatting**|扫描电子显微镜（SEM）因其分析微观物体表面结构的能力而广为人知，能够捕获高度详细但仅灰度的图像。为了创建更具表现力和逼真的插图，这些图像通常由艺术家在图像编辑软件的支持下手动着色。当扫描对象的多个图像需要着色时，这项任务变得非常费力。我们建议通过使用微观场景的底层3D结构将颜色信息从一个彩色视图传播到所有捕获的图像来促进这一过程。我们探索了几种场景表示技术，实现了SEM场景的高质量彩色新颖视图合成。与之前的工作相比，在获取3D表示时不涉及人工干预或标签。这使艺术家能够为序列的单个或几个视图着色，并自动检索全彩色的场景或视频。项目页面：https://ronly2460.github.io/ArCSEM et.al.|[2410.21310](http://arxiv.org/abs/2410.21310)|null|
|**2024-10-27**|**Normal-GS: 3D Gaussian Splatting with Normal-Involved Rendering**|渲染和重建是计算机视觉和图形学中的一个长期课题。同时实现高渲染质量和精确的几何图形是一个挑战。3D高斯散斑（3DGS）的最新进展实现了实时速度的高保真新颖视图合成。然而，3D高斯基元的噪声和离散特性阻碍了精确的表面估计。由于基于3DGS的方法中法向量和渲染管道之间的根本脱节，之前对3D高斯法线进行正则化的尝试往往会降低渲染质量。因此，我们引入了Normal GS，这是一种将法向量集成到3DGS渲染管道中的新方法。核心思想是使用基于物理的渲染方程对法线和入射光之间的相互作用进行建模。我们的方法将表面颜色重新参数化为法线和设计的集成方向照明矢量（IDIV）的乘积。为了优化内存使用并简化优化，我们采用基于锚点的3DGS来隐式编码本地共享的IDIV。此外，Normal GS利用优化的法线和集成方向编码（IDE）来准确建模镜面反射效果，从而提高渲染质量和曲面法线精度。大量实验表明，Normal GS在获得准确的表面法线并保持实时渲染性能的同时，实现了接近最先进的视觉质量。 et.al.|[2410.20593](http://arxiv.org/abs/2410.20593)|null|
|**2024-10-27**|**GUMBEL-NERF: Representing Unseen Objects as Part-Compositional Neural Radiance Fields**|我们提出了Gumbel-NeRF，这是一种混合了专家（MoE）神经辐射场（NeRF）模型和事后专家选择机制的模型，用于合成看不见物体的新视图。先前的研究表明，MoE结构提供了由许多对象组成的给定大规模场景的高质量表示。然而，我们观察到，当应用于从一个/几个镜头输入对看不见的物体进行新颖的视图合成的任务时，这种MoE-NeRF模型通常会在专家边界附近产生低质量的表示。我们发现，这种恶化主要是由预见专家选择机制引起的，这可能会在专家边界附近的物体形状中留下不自然的不连续性。Gumbel-NeRF采用事后专家选择机制，即使在专家边界附近，也能保证密度场的连续性。使用SRN汽车数据集的实验证明了Gumbel-NeRF在各种图像质量指标方面优于基线。 et.al.|[2410.20306](http://arxiv.org/abs/2410.20306)|null|
|**2024-10-25**|**Evaluation of strategies for efficient rate-distortion NeRF streaming**|神经辐射场（NeRF）通过从稀疏的图像集实现高度逼真和详细的场景重建，彻底改变了3D视觉表示领域。NeRF使用体积函数表示法，将3D点映射到其相应的颜色和不透明度，从而允许从任意视点进行逼真的视图合成。尽管取得了进步，但由于涉及大量数据，NeRF内容的高效流式传输仍然是一个重大挑战。本文研究了两种NeRF流媒体策略的率失真性能：基于像素的流媒体和基于神经网络（NN）参数的流媒体。在前者中，图像被编码并随后在整个网络中传输，而在后者中，相应的NeRF模型参数被编码并传输。这项工作还强调了复杂性和性能之间的权衡，表明基于NN参数的策略通常具有更高的效率，使其适用于一对多的流媒体场景。 et.al.|[2410.19459](http://arxiv.org/abs/2410.19459)|null|

<p align=right>(<a href=#updated-on-20241102>back to top</a>)</p>

## 3D Reconstruction

|Publish Date|Title|Abstract|PDF|Code|
|---|---|---|---|---|
|**2024-10-31**|**No Pose, No Problem: Surprisingly Simple 3D Gaussian Splats from Sparse Unposed Images**|我们介绍了NoPoSplat，这是一种前馈模型，能够从\textit{unfosed}稀疏多视图图像中重建由3D高斯参数化的3D场景。我们的模型仅使用光度损失进行训练，在推理过程中实现了实时3D高斯重建。为了在重建过程中消除对精确姿态输入的需求，我们将一个输入视图的局部相机坐标锚定为规范空间，并训练网络预测该空间内所有视图的高斯基元。这种方法避免了将高斯基元从局部坐标转换到全局坐标系的需要，从而避免了与每帧高斯和姿态估计相关的误差。为了解决尺度模糊问题，我们设计并比较了各种内在嵌入方法，最终选择将相机内在转换为令牌嵌入，并将其与图像令牌连接作为模型的输入，从而实现准确的场景尺度预测。我们利用重建的3D高斯分布进行新的视图合成和姿态估计任务，并提出了一种两阶段粗到细的流水线来进行精确的姿态估计。实验结果表明，与需要姿态的方法相比，我们的无姿态方法可以实现更优的新颖视图合成质量，特别是在输入图像重叠有限的情况下。对于姿态估计，我们的方法在没有地面真实深度或显式匹配损失的情况下进行训练，显著优于最先进的方法，并有了实质性的改进。这项工作在无姿态通用3D重建方面取得了重大进展，并证明了其适用于现实世界场景。代码和训练模型可在以下网址获得https://noposplat.github.io/. et.al.|[2410.24207](http://arxiv.org/abs/2410.24207)|**[link](https://github.com/cvg/NoPoSplat)**|
|**2024-10-31**|**LBurst: Learning-Based Robotic Burst Feature Extraction for 3D Reconstruction in Low Light**|无人机彻底改变了航空成像、测绘和灾难恢复领域。然而，无人机在低光照条件下的部署受到其机载摄像头产生的图像质量的限制。在这篇论文中，我们提出了一种学习架构，通过在突发中寻找特征来改善低光条件下的3D重建。我们的方法通过检测和描述低信噪比图像中的高质量真实特征和较少的虚假特征来增强视觉重建。我们证明，我们的方法能够在毫勒克斯照明下处理具有挑战性的场景，使其朝着夜间和极低光照应用（如地下采矿和搜救行动）的无人机迈出了重要一步。 et.al.|[2410.23522](http://arxiv.org/abs/2410.23522)|null|
|**2024-10-30**|**PointRecon: Online Point-based 3D Reconstruction via Ray-based 2D-3D Matching**|我们提出了一种新的基于点的在线单目RGB视频三维重建方法。我们的模型保持了场景的全局点云表示，随着新图像的观察，不断更新点的特征和3D位置。它用新检测到的点扩展点云，同时仔细删除冗余。新点的点云更新和深度预测是通过一种新的基于射线的2D-3D特征匹配技术实现的，该技术对先前点位置预测中的误差具有鲁棒性。与离线方法相比，我们的方法处理无限长的序列并提供实时更新。此外，点云没有预定义的分辨率或场景大小限制，其统一的全局表示确保了不同视角的视图一致性。在ScanNet数据集上的实验表明，我们的方法在在线MVS方法中达到了最先进的质量。项目页面：https://arthurhero.github.io/projects/pointrecon et.al.|[2410.23245](http://arxiv.org/abs/2410.23245)|null|
|**2024-10-30**|**Geometry Cloak: Preventing TGS-based 3D Reconstruction from Copyrighted Images**|单视图3D重建方法，如三平面高斯散斑（TGS），能够在几秒钟内从单个图像输入生成高质量的3D模型。然而，这种功能引发了人们对潜在滥用的担忧，恶意用户可以利用TGS从受版权保护的图像中创建未经授权的3D模型。为了防止这种侵权行为，我们提出了一种新的图像保护方法，在将图像提供给TGS之前，将不可见的几何扰动（称为“几何斗篷”）嵌入图像中。这些精心制作的扰动编码了一个定制的信息，当TGS尝试对隐形图像进行3D重建时，该信息就会显现出来。与简单地降低输出质量的传统对抗性攻击不同，我们的方法通过生成可识别的定制模式作为水印，迫使TGS以特定的方式失败3D重建。该水印允许版权所有者对从其受保护图像中进行的任何尝试的3D重建主张所有权。大量的实验已经验证了我们的几何斗篷的有效性。我们的项目可在https://qsong2001.github.io/geometry_cloak. et.al.|[2410.22705](http://arxiv.org/abs/2410.22705)|null|
|**2024-10-29**|**Guide3D: A Bi-planar X-ray Dataset for 3D Shape Reconstruction**|血管内手术工具重建是推进血管内工具导航的重要因素，是血管内手术的重要步骤。然而，缺乏公开可用的数据集严重限制了新型机器学习方法的开发和验证。此外，由于需要双平面扫描仪等专用设备，之前的大多数研究都采用了单平面荧光镜技术，因此只能从单一视角捕获数据，大大限制了重建精度。为了弥合这一差距，我们引入了Guide3D，这是一个用于3D重建的双平面X射线数据集。该数据集代表了在现实环境中捕获的高分辨率双平面手动注释荧光镜透视视频的集合。在反映临床环境的模拟环境中验证我们的数据集，证实了它对现实世界应用的适用性。此外，我们提出了一个新的导石形状预测基准，作为未来工作的有力基准。Guide3D不仅通过提供一个推进分割和3D重建技术的平台来满足基本需求，而且有助于开发更准确、更有效的血管内手术干预措施。我们的项目可在https://airvlab.github.io/guide3d/. et.al.|[2410.22224](http://arxiv.org/abs/2410.22224)|null|
|**2024-10-29**|**PF3plat: Pose-Free Feed-Forward 3D Gaussian Splatting**|我们考虑了在单个前馈中从非聚焦图像合成新视图的问题。我们的框架利用了3DGS的快速、可扩展性和高质量的3D重建和视图合成功能，我们进一步扩展了它，提供了一种实用的解决方案，放宽了常见的假设，如密集的图像视图、精确的相机姿态和大量的图像重叠。我们通过识别和解决使用像素对齐的3DGS所带来的独特挑战来实现这一目标：不同视图中未对齐的3D高斯分布会导致噪声或稀疏梯度，从而破坏训练的稳定性并阻碍收敛，尤其是在不满足上述假设的情况下。为了减轻这种情况，我们采用预训练的单目深度估计和视觉对应模型来实现3D高斯的粗略对齐。然后，我们引入了轻量级、可学习的模块，从粗对准中细化深度和姿态估计，提高了3D重建的质量和新颖的视图合成。此外，利用精细估计来估计几何置信度得分，该得分评估3D高斯中心的可靠性，并相应地调节高斯参数的预测。对大规模真实世界数据集的广泛评估表明，PF3plat在所有基准测试中都达到了新的最先进水平，并得到了验证我们设计选择的全面消融研究的支持。 et.al.|[2410.22128](http://arxiv.org/abs/2410.22128)|**[link](https://github.com/cvlab-kaist/PF3plat)**|
|**2024-10-29**|**PrefPaint: Aligning Image Inpainting Diffusion Model with Human Preference**|本文首次尝试通过强化学习框架将图像修复的扩散模型与人类美学标准对齐，显著提高了修复图像的质量和视觉吸引力。具体来说，我们没有直接用成对的图像来测量差异，而是用我们构建的数据集训练了一个奖励模型，该数据集由近51000张标注了人类偏好的图像组成。然后，我们采用强化学习过程来微调预训练的图像修复扩散模型的分布，以获得更高的回报。此外，我们从理论上推导了奖励模型误差的上限，这说明了在整个强化对齐过程中奖励估计的潜在置信度，从而促进了精确的正则化。对修复比较和下游任务（如图像扩展和3D重建）的广泛实验证明了我们方法的有效性，与最先进的方法相比，修复图像与人类偏好的对齐有了显著改善。这项研究不仅推进了图像修复领域的发展，还为基于建模奖励准确性将人类偏好纳入生成模型的迭代细化提供了一个框架，对视觉驱动的人工智能应用程序的设计具有广泛的意义。我们的代码和数据集可在以下网址公开获取https://prefpaint.github.io. et.al.|[2410.21966](http://arxiv.org/abs/2410.21966)|null|
|**2024-10-29**|**SS3DM: Benchmarking Street-View Surface Reconstruction with a Synthetic 3D Mesh Dataset**|为街景场景重建精确的3D表面对于数字娱乐和自动驾驶模拟等应用至关重要。然而，现有的街景数据集，包括KITTI、Waymo和nuScenes，只提供嘈杂的激光雷达点作为重建表面几何评估的地面真实数据。这些几何地面真理通常缺乏评估曲面位置所需的精度，也不提供评估曲面法线的数据。为了克服这些挑战，我们引入了SS3DM数据集，其中包括precist\textbf{S}ynthetic\textbf{S}treet-view\textbf{3D}\textbf{M}esh从CARLA模拟器导出的模型。这些网格模型有助于精确的位置评估，并包括用于评估表面法线的法线向量。为了在真实的驾驶场景中模拟输入数据以进行3D重建，我们在不同的室外场景中虚拟驾驶一辆配备了六个RGB摄像头和五个LiDAR传感器的车辆。利用这一数据集，我们为最先进的表面重建方法建立了一个基准，对相关挑战进行了全面评估。如需更多信息，请访问我们的主页https://ss3dm.top. et.al.|[2410.21739](http://arxiv.org/abs/2410.21739)|null|
|**2024-10-28**|**IndraEye: Infrared Electro-Optical UAV-based Perception Dataset for Robust Downstream Tasks**|深度神经网络（DNN）在电光（EO）相机捕获的光线充足的图像上训练时表现出了卓越的性能，这些图像提供了丰富的纹理细节。然而，在航空感知等关键应用中，DNN必须在所有条件下保持一致的可靠性，包括低光照场景，在这些场景中，光电摄像机往往难以捕捉到足够的细节。此外，由于不同高度和倾斜角度的尺度变化，基于无人机的空中目标检测面临着重大挑战，增加了另一层复杂性。现有的方法通常只解决域偏移时的照明变化或样式变化，但在空间感知中，相关性偏移也会影响DNN性能。本文介绍了IndraEye数据集，这是一个为各种任务设计的多传感器（EO-IR）数据集。它包括5612张图像，145666个实例，涵盖了印度次大陆的多个视角、高度、七种背景和一天中的不同时间。该数据集开辟了几个研究机会，如多模态学习、对象检测和分割的领域自适应，以及探索传感器特定的优缺点。IndraEye旨在通过支持开发更强大、更准确的空中感知系统来推进该领域的发展，特别是在具有挑战性的条件下。IndraEye数据集以对象检测和语义分割任务为基准。数据集和源代码可在https://bit.ly/indraeye. et.al.|[2410.20953](http://arxiv.org/abs/2410.20953)|**[link](https://github.com/Manjuphoenix/IndraEye)**|
|**2024-10-28**|**ODGS: 3D Scene Reconstruction from Omnidirectional Images with 3D Gaussian Splattings**|全向（或360度）图像越来越多地用于3D应用，因为它们允许用单个图像渲染整个场景。基于神经辐射场的现有作品在以自我为中心的视频上展示了成功的3D重建质量，但它们的训练和渲染时间很长。最近，3D高斯散斑因其快速优化和实时渲染而受到关注。然而，由于两个图像域之间的光学特性不同，直接使用透视光栅化器对全向图像进行处理会导致严重失真。在这项工作中，我们提出了ODGS，这是一种用于全向图像的新型光栅化流水线，具有几何解释功能。对于每个高斯分布，我们定义一个与单位球体接触的切平面，该切平面垂直于朝向高斯中心的光线。然后，我们利用透视相机光栅化器将高斯投影到相应的切平面上。投影的高斯图像被转换并组合成全向图像，从而完成全向光栅化过程。这种解释揭示了所提出的管道中的隐含假设，我们通过数学证明进行了验证。整个光栅化过程使用CUDA并行化，实现了比基于NeRF的方法快100倍的优化和渲染速度。我们的综合实验通过在各种数据集上提供最佳的重建和感知质量，突显了ODGS的优越性。此外，漫游数据集的结果表明，即使在重建大型3D场景时，ODGS也能有效地恢复精细细节。源代码可以在我们的项目页面上找到(https://github.com/esw0116/ODGS). et.al.|[2410.20686](http://arxiv.org/abs/2410.20686)|null|

<p align=right>(<a href=#updated-on-20241102>back to top</a>)</p>

## Diffusion

|Publish Date|Title|Abstract|PDF|Code|
|---|---|---|---|---|
|**2024-10-31**|**Bridging Geometric States via Geometric Diffusion Bridge**|精确预测复杂系统中的几何状态演化对于推进量子化学和材料建模等科学领域至关重要。传统的实验和计算方法在环境约束和计算需求方面面临挑战，而当前的深度学习方法在精度和通用性方面仍然不足。在这项工作中，我们介绍了几何扩散桥（GDB），这是一种新的生成建模框架，可以精确地桥接初始和目标几何状态。GDB利用概率方法来演化几何状态分布，采用由Doob的 $h$ -变换的修改版本导出的等变扩散桥来连接几何状态。这种定制的扩散过程由初始和目标几何状态作为固定端点锚定，并由等变过渡核控制。此外，通过使用一系列等变扩散桥，轨迹数据可以在我们的GDB框架中无缝利用，从而更详细、更准确地描述进化动力学。从理论上讲，我们进行了彻底的检查，以确认我们的框架能够保持几何状态的联合分布，并且能够完全模拟潜在的动力学诱导轨迹分布，误差可以忽略不计。对各种现实世界场景的实验评估表明，GDB超越了现有的最先进的方法，为准确弥合几何状态和以更高的准确性和适用性应对关键的科学挑战开辟了一条新途径。 et.al.|[2410.24220](http://arxiv.org/abs/2410.24220)|null|
|**2024-10-31**|**DiffPano: Scalable and Consistent Text to Panorama Generation with Spherical Epipolar-Aware Diffusion**|基于扩散的方法在2D图像或3D对象生成方面取得了显著成就，但由于场景数据集数量有限、3D场景本身的复杂性以及生成一致的多视图图像的困难，3D场景甚至360美元图像的生成仍然受到限制。为了解决这些问题，我们首先建立了一个大规模的全景视频文本数据集，其中包含数百万个连续的全景关键帧，以及相应的全景深度、相机姿态和文本描述。然后，我们提出了一种新的文本驱动全景生成框架，称为DiffPano，以实现可扩展、一致和多样化的全景场景生成。具体来说，得益于稳定扩散的强大生成能力，我们在已建立的全景视频文本数据集上使用LoRA对单视图文本到全景扩散模型进行了微调。我们进一步设计了一个球形极线感知的多视图扩散模型，以确保生成的全景图像的多视图一致性。大量实验表明，DiffPano可以在给定的看不见的文本描述和相机姿态下生成可扩展、一致和多样化的全景图像。 et.al.|[2410.24203](http://arxiv.org/abs/2410.24203)|**[link](https://github.com/zju3dv/diffpano)**|
|**2024-10-31**|**AR-Pro: Counterfactual Explanations for Anomaly Repair with Formal Properties**|异常检测被广泛用于识别关键错误和可疑行为，但目前的方法缺乏可解释性。我们利用现有方法的共同特性和生成模型的最新进展，为异常检测引入反事实解释。给定一个输入，我们生成其反事实作为基于扩散的修复，显示非异常版本应该是什么样子。这种方法的一个关键优点是，它能够对可解释性需求进行独立于领域的形式化规范，为生成和评估解释提供了一个统一的框架。我们展示了我们的异常可解释性框架AR Pro在视觉（MVTec、VisA）和时间序列（SWaT、WADI、HAI）异常数据集上的有效性。用于实验的代码可在以下网址访问：https://github.com/xjiae/arpro. et.al.|[2410.24178](http://arxiv.org/abs/2410.24178)|null|
|**2024-10-31**|**Redefining <Creative> in Dictionary: Towards a Enhanced Semantic Understanding of Creative Generation**|创造力，无论是在人类还是传播模型中，仍然是一个固有的抽象概念；因此，简单地在提示中添加“创造性”并不能使模型产生可靠的语义识别。在这项工作中，我们通过TP2O任务具体化了“创造性”的抽象概念，该任务旨在合并两个不相关的概念，并引入CreTok，将“创造性”重新定义为符号 $\texttt{<CreTok>}$。这种重新定义为概念融合提供了更具体、更通用的表示。这种重新定义是连续发生的，涉及对具有不同概念的文本对进行重复随机抽样，并优化目标和常量提示之间的余弦相似性。这种方法使$\texttt{<CreTok>}$能够学习一种创造性概念融合的方法。大量实验表明，$\texttt{<CreTok>}$所支持的创造力大大超过了最近的SOTA扩散模型，并实现了卓越的创造力生成。CreTok表现出更大的灵活性和更少的时间开销，因为$\texttt{<CreTok>}$ 可以作为任何概念的通用代币，在不进行再培训的情况下促进创意生成。 et.al.|[2410.24160](http://arxiv.org/abs/2410.24160)|null|
|**2024-10-31**|**Scaling Concept With Text-Guided Diffusion Models**|文本引导的传播模型通过从文本描述中生成高保真内容，彻底改变了生成任务。它们还启用了一种编辑范式，在这种范式中，概念可以通过文本条件来替换（例如，从狗到老虎）。在这项工作中，我们探索了一种新的方法：我们可以增强或抑制概念本身，而不是取代一个概念吗？通过实证研究，我们发现了一种趋势，即概念可以在文本引导的扩散模型中分解。利用这一见解，我们引入了ScalingConcept，这是一种简单而有效的方法，可以在实际输入中向上或向下扩展分解的概念，而无需引入新元素。为了系统地评估我们的方法，我们提出了WeakConcept-10数据集，其中的概念并不完美，需要改进。更重要的是，ScalingConcept能够在图像和音频领域实现各种新颖的零样本应用程序，包括规范姿势生成和生成声音突出显示或移除等任务。 et.al.|[2410.24151](http://arxiv.org/abs/2410.24151)|null|
|**2024-10-31**|**Nonlinear Two-Level Schwarz Methods: A Parallel Implementation in FROSch**|由于非线性域分解方法能够改善牛顿法的非线性收敛行为，最近在牛顿法收敛缓慢或根本不收敛的问题中，它们越来越受欢迎。本文介绍了一种基于FROSH（快速鲁棒重叠Schwarz）求解器框架的两级非线性Schwarz求解器的新型并行实现，该框架是桑迪亚Trilinos库的一部分。首先，介绍了两级非线性Schwarz方法的关键概念，包括用于构建第二级的粗略空间的简要概述。接下来，讨论了并行实现，然后是标量非线性扩散问题和具有大变形的二维非线性平面应力Neo-Hooke弹性问题的初步并行结果。 et.al.|[2410.24138](http://arxiv.org/abs/2410.24138)|null|
|**2024-10-31**|**Modeling Brownian Motion as a Timelapse of the Physical, Persistent, Trajectory**|虽然通过假设轨迹的无记忆性和扩散步长将扩散建模为随机游走是很常见的，但这些假设可能会导致重大误差。本文描述了布朗粒子的物理轨迹在多大程度上可以通过随机飞行来描述。对物理轨迹的简单时间推移的分析（使用速度自相关函数在碰撞时间尺度上计算，该函数捕获了溶剂引起的流体动力学和声学效应）给了我们两个观察结果：（i）只有当时间步长比弛豫时间大约200倍时，子采样轨迹才会真正无记忆，（ii）步长分布的方差仍然明显小于2Dt（通常为约2倍）。最后一个事实是由于两种效应的结合：扩散MSD在短时间尺度上具有数学上的超弹道性，子采样轨迹是基础物理轨迹的移动平均值。换句话说，长时间间隔的物理轨迹的MSD渐近地接近2Dt，但子采样步骤的MSD不会，即使相关时间间隔比弛豫时间大几百倍。我讨论了如何在计算方法中最好地解释这种效应。 et.al.|[2410.24137](http://arxiv.org/abs/2410.24137)|null|
|**2024-10-31**|**3D-ViTac: Learning Fine-Grained Manipulation with Visuo-Tactile Sensing**|触觉和视觉感知对于人类与环境进行精细交互都至关重要。为机器人开发类似的多模态传感能力可以显著提高和扩展他们的操作技能。本文介绍了\textbf{3DViTac}，这是一个为灵巧双手操作而设计的多模态传感和学习系统。我们的系统具有配备密集传感单元的触觉传感器，每个传感器的面积为3平方毫米。这些传感器成本低廉且灵活，可提供详细而广泛的物理接触覆盖，有效地补充了视觉信息。为了整合触觉和视觉数据，我们将它们融合到一个统一的3D表示空间中，以保留它们的3D结构和空间关系。然后，多模态表示可以与扩散策略相结合，用于模仿学习。通过具体的硬件实验，我们证明即使是低成本的机器人也可以执行精确的操作，并且显著优于仅凭视觉的策略，特别是在与易碎物品的安全交互和执行涉及手部操作的长期任务方面。我们的项目页面位于\url{https://binghao-huang.github.io/3D-ViTac/}. et.al.|[2410.24091](http://arxiv.org/abs/2410.24091)|null|
|**2024-10-31**|**Deep Chandra Observations of NGC 5728. III: Probing the High-Resolution X-ray Morphology and Multiphase ISM Interactions in the Circumnuclear Region**|我们对附近Seyfert 2星系NGC 5728的260 ks亚弧秒分辨率钱德拉高级CCD成像光谱仪（ACIS-S）观测结果进行了详细的成像分析。我们的研究重点是星系内部约1kpc内明亮而漫射的软X射线发射。通过比较不同能带的X射线发射，我们确定了吸收柱和发射过程中的局部变化。我们观察到在垂直于双锥的方向上有更多的X射线吸收，双锥与星系中内部扭曲的co盘位于同一位置。最内层区域显示出最强的硬X射线发射过量，与哈勃太空望远镜V-H彩色图中观测到的ALMA和尘埃螺旋的CO（2-1）发射在空间上重合。我们检测到与约1kpc的环核恒星形成环相关的软扩展发射，表明kT=0.44keV的热气体。我们推导出了热气质量的测量值，M=7.9x10^5太阳质量，压力，p=2.0x10^-10达因/平方厘米，冷却时间，t=193.2百万。在恒星形成环附近，我们检测到两个具有软X射线光谱和0.3-7keV亮度L~8x10^38erg/s的X射线点源。这些特性表明存在X射线双星。 et.al.|[2410.24061](http://arxiv.org/abs/2410.24061)|null|
|**2024-10-31**|**Understanding Generalizability of Diffusion Models Requires Rethinking the Hidden Gaussian Structure**|在这项工作中，我们通过研究学习到的分数函数的隐藏特性来研究扩散模型的可推广性，这些分数函数本质上是在各种噪声水平上训练的一系列深度去噪器。我们观察到，随着扩散模型从记忆过渡到泛化，它们相应的非线性扩散去噪器表现出越来越强的线性。这一发现使我们研究了非线性扩散模型的线性对应物，它们是一系列经过训练的线性模型，用于匹配非线性扩散去噪器的函数映射。令人惊讶的是，对于以训练数据集的经验均值和协方差为特征的多元高斯分布，这些线性去噪器大约是最佳去噪器。这一发现意味着扩散模型在捕获和利用训练数据集的高斯结构（协方差信息）进行数据生成方面存在归纳偏差。我们实证证明，这种归纳偏差是扩散模型在泛化状态下的一个独特特性，当模型的容量与训练数据集的大小相比相对较小时，这种特性变得越来越明显。在模型被高度高估的情况下，这种归纳偏差会在模型完全记忆其训练数据之前的初始训练阶段出现。我们的研究为理解最近在现实世界扩散模型中观察到的显著强泛化现象提供了至关重要的见解。 et.al.|[2410.24060](http://arxiv.org/abs/2410.24060)|**[link](https://github.com/Morefre/Understanding-Generalizability-of-Diffusion-Models-Requires-Rethinking-the-Hidden-Gaussian-Structure)**|

<p align=right>(<a href=#updated-on-20241102>back to top</a>)</p>

## NeRF

|Publish Date|Title|Abstract|PDF|Code|
|---|---|---|---|---|
|**2024-10-26**|**Neural Fields in Robotics: A Survey**|神经场已经成为计算机视觉和机器人技术中3D场景表示的一种变革性方法，能够从姿势的2D数据中准确推断几何、3D语义和动力学。利用可微分渲染，神经场包括连续隐式和显式神经表示，实现了高保真3D重建、多模态传感器数据的集成和新视点的生成。这项调查探讨了它们在机器人技术中的应用，强调了它们在增强感知、规划和控制方面的潜力。它们的紧凑性、内存效率和可微性，以及与基础模型和生成模型的无缝集成，使其成为实时应用的理想选择，提高了机器人的适应性和决策能力。本文基于200多篇论文，对机器人中的神经场进行了全面的回顾，对各个领域的应用进行了分类，并评估了它们的优势和局限性。首先，我们介绍了四个关键的神经场框架：占用网络、有符号距离场、神经辐射场和高斯散斑。其次，我们详细介绍了神经场在五个主要机器人领域的应用：姿态估计、操纵、导航、物理和自动驾驶，重点介绍了关键工作，并讨论了要点和公开挑战。最后，我们概述了神经场在机器人技术中的局限性，并为未来的研究提出了有前景的方向。项目页面：https://robonerf.github.io et.al.|[2410.20220](http://arxiv.org/abs/2410.20220)|null|
|**2024-10-24**|**3D-Adapter: Geometry-Consistent Multi-View Diffusion for High-Quality 3D Generation**|多视图图像扩散模型显著推进了开放域3D对象生成。然而，大多数现有模型依赖于缺乏固有3D偏差的2D网络架构，导致几何一致性受损。为了应对这一挑战，我们引入了3D Adapter，这是一个插件模块，旨在将3D几何感知注入预训练的图像扩散模型中。我们方法的核心是3D反馈增强的思想：对于采样循环中的每个去噪步骤，3D Adapter将中间的多视图特征解码为连贯的3D表示，然后对渲染的RGBD视图进行重新编码，通过特征添加来增强预训练的基础模型。我们研究了3D Adapter的两种变体：一种是基于高斯飞溅的快速前馈版本，另一种是利用神经场和网格的通用无训练版本。我们广泛的实验表明，3D Adapter不仅大大提高了文本到多视图模型（如Instant3D和Zero123++）的几何质量，而且还使用纯文本到图像的稳定扩散实现了高质量的3D生成。此外，我们通过在文本到3D、图像到3D、文本到纹理和文本到化身任务中呈现高质量的结果，展示了3D适配器的广泛应用潜力。 et.al.|[2410.18974](http://arxiv.org/abs/2410.18974)|**[link](https://github.com/Lakonik/MVEdit)**|
|**2024-10-22**|**Cortical Dynamics of Neural-Connectivity Fields**|皮质组织的宏观研究揭示了振荡活动的普遍性，这反映了神经相互作用的微调。本研究通过将广义振荡动力学纳入先前关于保守或半保守神经场动力学的工作中，扩展了神经场理论。先前的研究在很大程度上假设了神经单元之间的各向同性连接；然而，这项研究表明，广泛的各向异性和波动连接仍然可以维持振荡。使用拉格朗日场方法，我们研究了不同类型的连接、它们的动力学以及与神经场的潜在相互作用。基于这一理论基础，我们推导出了一个框架，该框架通过连接场的概念将Hebbian和非Hebbian学习（即可塑性）纳入神经场的研究中。 et.al.|[2410.16852](http://arxiv.org/abs/2410.16852)|null|
|**2024-10-15**|**Deep vectorised operators for pulsatile hemodynamics estimation in coronary arteries from a steady-state prior**|心血管血流动力学场为冠状动脉疾病提供了有价值的医学决策标志。计算流体动力学（CFD）是体内准确、无创评估这些量的金标准。在这项工作中，我们提出了一种基于机器学习的时间高效替代模型，用于基于稳态先验估计脉动血流动力学。我们引入了深度矢量化算子，这是一种用于在无限维函数空间上进行离散化独立学习的建模框架。基础神经结构是一个以血流动力学边界条件为条件的神经场。重要的是，我们展示了如何将逐点动作的要求放宽到置换等变，从而产生一系列可以通过消息传递和自我关注层进行参数化的模型。我们在从冠状动脉计算机断层扫描血管造影（CCTA）中提取的74条狭窄冠状动脉的数据集上评估了我们的方法，并将患者特异性脉动CFD模拟作为基本事实。我们证明，我们的模型能够准确估计脉动速度和压力，同时不受源域重新采样的影响（离散化独立性）。这表明，深度矢量化算子是冠状动脉及其他动脉心血管血流动力学估计的强大建模工具。 et.al.|[2410.11920](http://arxiv.org/abs/2410.11920)|null|
|**2024-10-07**|**Fast Training of Sinusoidal Neural Fields via Scaling Initialization**|神经场是一种新兴的范式，它将数据表示为由神经网络参数化的连续函数。尽管有许多优点，但神经场通常具有较高的训练成本，这阻碍了更广泛的采用。在本文中，我们关注一个流行的神经场家族，称为正弦神经场（SNF），并研究如何初始化它以最大限度地提高训练速度。我们发现，基于信号传播原理设计的SNF标准初始化方案是次优的。特别是，我们证明，通过简单地将每个权重（最后一层除外）乘以一个常数，我们可以将SNF训练加速10 $\times$。这种方法被称为$\textit{weight scaling}$ ，在各种数据域上持续提供显著的加速，使SNF的训练速度比最近提出的架构更快。为了理解为什么权重缩放效果良好，我们进行了广泛的理论和实证分析，结果表明，权重缩放不仅有效地解决了频谱偏差，而且具有良好的优化轨迹。 et.al.|[2410.04779](http://arxiv.org/abs/2410.04779)|null|
|**2024-10-04**|**End-to-End Reaction Field Energy Modeling via Deep Learning based Voxel-to-voxel Transform**|在计算生物化学和生物物理学中，理解静电相互作用的作用对于阐明生物分子的结构、动力学和功能至关重要。泊松-玻尔兹曼（PB）方程是通过描述带电分子内部和周围的静电势来模拟这些相互作用的基础工具。然而，由于生物分子表面的复杂性和需要考虑可移动离子，求解PB方程带来了重大的计算挑战。虽然求解PB方程的传统数值方法是准确的，但它们的计算成本很高，并且随着系统规模的增加而扩展性较差。为了应对这些挑战，我们引入了PBNeF，这是一种新的机器学习方法，灵感来自基于神经网络的偏微分方程求解器的最新进展。我们的方法将PB方程的输入和边界静电条件转化为可学习的体素表示，使神经场变换器能够预测PB解，进而预测反应场势能。大量实验表明，与传统的PB求解器相比，PBNeF的速度提高了100倍以上，同时保持了与广义玻恩（GB）模型相当的精度。 et.al.|[2410.03927](http://arxiv.org/abs/2410.03927)|null|
|**2024-10-08**|**DressRecon: Freeform 4D Human Reconstruction from Monocular Video**|我们提出了一种从单目视频中重建时间一致的人体模型的方法，重点是极其宽松的衣服或手持物体的交互。之前在人体重建方面的工作要么局限于没有物体交互的紧身衣服，要么需要校准的多视图捕捉或个性化的模板扫描，而大规模收集这些数据成本很高。我们对高质量但灵活的重建的关键见解是，将关于关节体形状的通用人类先验（从大规模训练数据中学习）与视频特定的关节“骨骼袋”变形（通过测试时间优化适合单个视频）仔细结合。我们通过学习一个神经隐式模型来实现这一点，该模型将身体和衣服的变形作为单独的运动模型层来解开。为了捕捉服装的微妙几何形状，我们在优化过程中利用了基于图像的先验，如人体姿势、表面法线和光流。由此产生的神经场可以提取到时间一致的网格中，或进一步优化为显式3D高斯分布，以实现高保真交互式渲染。在具有高度挑战性的服装变形和物体交互的数据集上，DressReston可以产生比现有技术更高保真的3D重建。项目页面：https://jefftan969.github.io/dressrecon/ et.al.|[2409.20563](http://arxiv.org/abs/2409.20563)|null|
|**2024-09-25**|**TalkinNeRF: Animatable Neural Fields for Full-Body Talking Humans**|我们介绍了一种新的框架，该框架从单眼视频中学习全身说话的人的动态神经辐射场（NeRF）。之前的工作只代表身体姿势或面部。然而，人类通过全身进行交流，结合身体姿势、手势和面部表情。在这项工作中，我们提出了TalkinNeRF，这是一个基于NeRF的统一网络，代表了整体4D人体运动。给定一个受试者的单眼视频，我们学习身体、面部和手的相应模块，这些模块结合在一起生成最终结果。为了捕捉复杂的手指关节，我们学习了手的额外变形场。我们的多身份表示能够同时训练多个科目，以及在完全看不见的姿势下进行强大的动画。只要输入一段短视频，它也可以推广到新的身份。我们展示了最先进的性能，用于为全身说话的人类制作动画，具有精细的手部发音和面部表情。 et.al.|[2409.16666](http://arxiv.org/abs/2409.16666)|null|
|**2024-09-24**|**Generative 3D Cardiac Shape Modelling for In-Silico Trials**|我们提出了一种深度学习方法，基于将形状表示为神经有符号距离场的零级集，对合成主动脉形状进行建模和生成，该方法受一系列可训练的嵌入向量的约束，并对每个形状的几何特征进行编码。通过使神经场在采样表面点上消失并强制其空间梯度具有单位范数，在从CT图像重建的主动脉根部网格数据集上训练网络。实证结果表明，我们的模型可以高保真地表示主动脉形状。此外，通过从学习到的嵌入向量中采样，我们可以生成类似于真实患者解剖结构的新形状，可用于计算机模拟试验。 et.al.|[2409.16058](http://arxiv.org/abs/2409.16058)|null|
|**2024-09-21**|**MOSE: Monocular Semantic Reconstruction Using NeRF-Lifted Noisy Priors**|由于缺乏几何指导和不完美的视图相关2D先验，从单眼图像中精确重建密集和语义注释的3D网格仍然是一项具有挑战性的任务。尽管我们已经见证了隐式神经场景表示的最新进展，能够简单地从多视图图像中进行精确的2D渲染，但很少有研究仅使用单眼先验来解决3D场景理解问题。在本文中，我们提出了MOSE，这是一种神经场语义重建方法，可以将推断的图像级噪声先验提升到3D，在3D和2D空间中产生精确的语义和几何。我们方法的关键动机是利用通用类不可知的分段掩码作为指导，在训练过程中促进渲染语义的局部一致性。在语义的帮助下，我们进一步将平滑正则化应用于无纹理区域，以获得更好的几何质量，从而实现几何和语义的互惠互利。在ScanNet数据集上的实验表明，我们的MOSE在3D语义分割、2D语义分割和3D表面重建任务的所有指标上都优于相关基线。 et.al.|[2409.14019](http://arxiv.org/abs/2409.14019)|null|

<p align=right>(<a href=#updated-on-20241102>back to top</a>)</p>

[contributors-shield]: https://img.shields.io/github/contributors/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[contributors-url]: https://github.com/Vincentqyw/cv-arxiv-daily/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[forks-url]: https://github.com/Vincentqyw/cv-arxiv-daily/network/members
[stars-shield]: https://img.shields.io/github/stars/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[stars-url]: https://github.com/Vincentqyw/cv-arxiv-daily/stargazers
[issues-shield]: https://img.shields.io/github/issues/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[issues-url]: https://github.com/Vincentqyw/cv-arxiv-daily/issues

