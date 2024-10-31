[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]

## Updated on 2024.10.31
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
|**2024-10-30**|**Epipolar-Free 3D Gaussian Splatting for Generalizable Novel View Synthesis**|广义3D高斯分裂（3DGS）可以以前馈推理的方式从稀疏视图观测中重建新的场景，消除了传统3DGS中对场景特定再训练的需要。然而，现有的方法严重依赖于极线先验，这在复杂的现实世界场景中可能不可靠，特别是在非重叠和遮挡的区域。在本文中，我们提出了eFreeSplat，这是一种基于3DGS的高效前馈模型，用于独立于极线约束的可推广新型视图合成。为了增强具有3D感知的多视图特征提取，我们在大规模数据集上采用了具有交叉视图完成预训练的自监督视觉变换器（ViT）。此外，我们引入了一种迭代交叉视图高斯对齐方法，以确保不同视图之间的深度尺度一致。我们的eFreeSplat代表了一种可推广的新颖视图合成的创新方法。与现有的纯无几何方法不同，eFreeSplat更侧重于通过跨视图预训练提供3D先验来实现无极线特征匹配和编码。我们使用RealEstate10K和ACID数据集在宽基线新视图合成任务上评估eFreeSplat。大量实验表明，eFreeSplat超越了依赖极线先验的最先进基线，实现了卓越的几何重建和新颖的视图合成质量。项目页面：https://tatakai1.github.io/efreesplat/. et.al.|[2410.22817](http://arxiv.org/abs/2410.22817)|null|
|**2024-10-29**|**PF3plat: Pose-Free Feed-Forward 3D Gaussian Splatting**|我们考虑了在单个前馈中从非聚焦图像合成新视图的问题。我们的框架利用了3DGS的快速、可扩展性和高质量的3D重建和视图合成功能，我们进一步扩展了它，提供了一种实用的解决方案，放宽了常见的假设，如密集的图像视图、精确的相机姿态和大量的图像重叠。我们通过识别和解决使用像素对齐的3DGS所带来的独特挑战来实现这一目标：不同视图中未对齐的3D高斯分布会导致噪声或稀疏梯度，从而破坏训练的稳定性并阻碍收敛，尤其是在不满足上述假设的情况下。为了减轻这种情况，我们采用预训练的单目深度估计和视觉对应模型来实现3D高斯的粗略对齐。然后，我们引入了轻量级、可学习的模块，从粗对准中细化深度和姿态估计，提高了3D重建的质量和新颖的视图合成。此外，利用精细估计来估计几何置信度得分，该得分评估3D高斯中心的可靠性，并相应地调节高斯参数的预测。对大规模真实世界数据集的广泛评估表明，PF3plat在所有基准测试中都达到了新的最先进水平，并得到了验证我们设计选择的全面消融研究的支持。 et.al.|[2410.22128](http://arxiv.org/abs/2410.22128)|**[link](https://github.com/cvlab-kaist/PF3plat)**|
|**2024-10-29**|**ActiveSplat: High-Fidelity Scene Reconstruction through Active Gaussian Splatting**|我们提出了ActivePlat，这是一个利用高斯飞溅的自主高保真重建系统。该系统利用高效逼真的渲染，为在线映射、视点选择和路径规划建立了一个统一的框架。ActivePlat的关键是一种混合地图表示，它集成了关于环境的密集信息和工作空间的稀疏抽象。因此，该系统利用稀疏拓扑进行高效的视点采样和路径规划，同时利用视图相关的密集预测进行视点选择，以有希望的准确性和完整性促进高效决策。在预算有限的情况下，采用基于拓扑图的分层规划策略来减少重复轨迹并提高局部粒度，确保通过逼真的视图合成进行高保真重建。广泛的实验和消融研究验证了所提出方法在重建精度、数据覆盖率和勘探效率方面的有效性。项目页面：https://li-yuetao.github.io/ActiveSplat/. et.al.|[2410.21955](http://arxiv.org/abs/2410.21955)|null|
|**2024-10-25**|**ArCSEM: Artistic Colorization of SEM Images via Gaussian Splatting**|扫描电子显微镜（SEM）因其分析微观物体表面结构的能力而广为人知，能够捕获高度详细但仅灰度的图像。为了创建更具表现力和逼真的插图，这些图像通常由艺术家在图像编辑软件的支持下手动着色。当扫描对象的多个图像需要着色时，这项任务变得非常费力。我们建议通过使用微观场景的底层3D结构将颜色信息从一个彩色视图传播到所有捕获的图像来促进这一过程。我们探索了几种场景表示技术，实现了SEM场景的高质量彩色新颖视图合成。与之前的工作相比，在获取3D表示时不涉及人工干预或标签。这使艺术家能够为序列的单个或几个视图着色，并自动检索全彩色的场景或视频。项目页面：https://ronly2460.github.io/ArCSEM et.al.|[2410.21310](http://arxiv.org/abs/2410.21310)|null|
|**2024-10-27**|**Normal-GS: 3D Gaussian Splatting with Normal-Involved Rendering**|渲染和重建是计算机视觉和图形学中的一个长期课题。同时实现高渲染质量和精确的几何图形是一个挑战。3D高斯散斑（3DGS）的最新进展实现了实时速度的高保真新颖视图合成。然而，3D高斯基元的噪声和离散特性阻碍了精确的表面估计。由于基于3DGS的方法中法向量和渲染管道之间的根本脱节，之前对3D高斯法线进行正则化的尝试往往会降低渲染质量。因此，我们引入了Normal GS，这是一种将法向量集成到3DGS渲染管道中的新方法。核心思想是使用基于物理的渲染方程对法线和入射光之间的相互作用进行建模。我们的方法将表面颜色重新参数化为法线和设计的集成方向照明矢量（IDIV）的乘积。为了优化内存使用并简化优化，我们采用基于锚点的3DGS来隐式编码本地共享的IDIV。此外，Normal GS利用优化的法线和集成方向编码（IDE）来精确地模拟镜面反射效果，从而提高渲染质量和曲面法线精度。大量实验表明，Normal GS在获得准确的表面法线并保持实时渲染性能的同时，实现了接近最先进的视觉质量。 et.al.|[2410.20593](http://arxiv.org/abs/2410.20593)|null|
|**2024-10-27**|**GUMBEL-NERF: Representing Unseen Objects as Part-Compositional Neural Radiance Fields**|我们提出了Gumbel-NeRF，这是一种混合了专家（MoE）神经辐射场（NeRF）模型和事后专家选择机制的模型，用于合成看不见物体的新视图。先前的研究表明，MoE结构提供了由许多对象组成的给定大规模场景的高质量表示。然而，我们观察到，当应用于从一个/几个镜头输入对看不见的物体进行新颖的视图合成的任务时，这种MoE-NeRF模型通常会在专家边界附近产生低质量的表示。我们发现，这种恶化主要是由预见专家选择机制引起的，这可能会在专家边界附近的物体形状中留下不自然的不连续性。Gumbel-NeRF采用事后专家选择机制，即使在专家边界附近，也能保证密度场的连续性。使用SRN汽车数据集的实验证明了Gumbel-NeRF在各种图像质量指标方面优于基线。 et.al.|[2410.20306](http://arxiv.org/abs/2410.20306)|null|
|**2024-10-25**|**Evaluation of strategies for efficient rate-distortion NeRF streaming**|神经辐射场（NeRF）通过从稀疏的图像集实现高度逼真和详细的场景重建，彻底改变了3D视觉表示领域。NeRF使用体积函数表示法，将3D点映射到其相应的颜色和不透明度，从而允许从任意视点进行逼真的视图合成。尽管取得了进步，但由于涉及大量数据，NeRF内容的高效流式传输仍然是一个重大挑战。本文研究了两种NeRF流媒体策略的率失真性能：基于像素的流媒体和基于神经网络（NN）参数的流媒体。在前者中，图像被编码并随后在整个网络中传输，而在后者中，相应的NeRF模型参数被编码并传输。这项工作还强调了复杂性和性能之间的权衡，表明基于NN参数的策略通常具有更高的效率，使其适用于一对多的流媒体场景。 et.al.|[2410.19459](http://arxiv.org/abs/2410.19459)|null|
|**2024-10-24**|**Where Am I and What Will I See: An Auto-Regressive Model for Spatial Localization and View Prediction**|空间智能是机器在空间和时间的三维空间中感知、推理和行动的能力。大规模自回归模型的最新进展在各种推理任务中表现出了显著的能力。然而，这些模型经常在空间推理的基本方面遇到困难，特别是在回答“我在哪里？”和“我会看到什么？”等问题时。虽然已经进行了一些尝试，但现有的方法通常将它们视为单独的任务，未能捕捉到它们相互关联的性质。在本文中，我们提出了生成空间变换器（GST），这是一种新型的自回归框架，可以同时解决空间定位和视图预测问题。我们的模型同时从单个图像中估计相机姿态，并从新的相机姿态预测视图，有效地弥合了空间感知和视觉预测之间的差距。所提出的创新相机标记化方法使模型能够以自回归的方式学习2D投影的联合分布及其相应的空间视角。这种统一的训练范式表明，姿态估计和新颖视图合成的联合优化首次提高了这两项任务的性能，突出了空间感知和视觉预测之间的内在关系。 et.al.|[2410.18962](http://arxiv.org/abs/2410.18962)|null|
|**2024-10-27**|**Binocular-Guided 3D Gaussian Splatting with View Consistency for Sparse View Synthesis**|稀疏输入的新颖视图合成是3D计算机视觉中一项至关重要但具有挑战性的任务。之前的方法探索了使用神经先验（如深度先验）作为额外监督的3D高斯散斑，与基于NeRF的方法相比，显示出有前景的质量和效率。然而，来自2D预训练模型的神经先验通常是嘈杂和模糊的，这很难精确地指导辐射场的学习。在本文中，我们提出了一种新的方法，通过高斯散斑从稀疏视图合成新视图，该方法不需要外部先验作为监督。我们的关键思想在于探索通过视差引导图像扭曲构建的每对双目图像之间的双目立体一致性所固有的自我监督。为此，我们还引入了高斯不透明度约束，该约束使高斯位置正则化，避免了高斯冗余，以提高从稀疏视图推断3D高斯的鲁棒性和效率。在LLFF、DTU和Blender数据集上进行的广泛实验表明，我们的方法明显优于最先进的方法。 et.al.|[2410.18822](http://arxiv.org/abs/2410.18822)|null|
|**2024-10-23**|**FreeVS: Generative View Synthesis on Free Driving Trajectory**|现有的基于重建的新型驾驶场景视图合成方法侧重于沿自我车辆记录的轨迹合成相机视图。当视点偏离记录的轨迹，相机光线未经训练时，它们的图像渲染性能将严重下降。我们提出了FreeVS，这是一种新颖的完全生成方法，可以在真实驾驶场景中合成自由新轨迹上的相机视图。为了控制生成结果与真实场景的3D一致性和视点姿态的准确性，我们提出了视图先验的伪图像表示来控制生成过程。视点变换模拟应用于伪图像，以模拟相机在每个方向上的运动。一旦经过训练，FreeVS可以应用于任何验证序列，而无需对新轨迹进行重建过程和合成视图。此外，我们提出了两个针对驾驶场景量身定制的具有挑战性的新基准，即新颖的相机合成和新颖的轨迹合成，强调视点的自由度。鉴于新轨迹上没有地面真实图像，我们还建议用3D感知模型评估新轨迹上合成的图像的一致性。在Waymo开放数据集上的实验表明，FreeVS在记录的轨迹和新的轨迹上都具有很强的图像合成性能。项目页面：https://freevs24.github.io/ et.al.|[2410.18079](http://arxiv.org/abs/2410.18079)|null|

<p align=right>(<a href=#updated-on-20241031>back to top</a>)</p>

## 3D Reconstruction

|Publish Date|Title|Abstract|PDF|Code|
|---|---|---|---|---|
|**2024-10-30**|**PointRecon: Online Point-based 3D Reconstruction via Ray-based 2D-3D Matching**|我们提出了一种新的基于点的在线单目RGB视频三维重建方法。我们的模型保持了场景的全局点云表示，随着新图像的观察，不断更新点的特征和3D位置。它用新检测到的点扩展点云，同时仔细删除冗余。新点的点云更新和深度预测是通过一种新的基于射线的2D-3D特征匹配技术实现的，该技术对先前点位置预测中的误差具有鲁棒性。与离线方法相比，我们的方法处理无限长的序列并提供实时更新。此外，点云没有预定义的分辨率或场景大小限制，其统一的全局表示确保了不同视角的视图一致性。在ScanNet数据集上的实验表明，我们的方法在在线MVS方法中达到了最先进的质量。项目页面：https://arthurhero.github.io/projects/pointrecon et.al.|[2410.23245](http://arxiv.org/abs/2410.23245)|null|
|**2024-10-30**|**Geometry Cloak: Preventing TGS-based 3D Reconstruction from Copyrighted Images**|单视图3D重建方法，如三平面高斯散斑（TGS），能够在几秒钟内从单个图像输入生成高质量的3D模型。然而，这种功能引发了人们对潜在滥用的担忧，恶意用户可以利用TGS从受版权保护的图像中创建未经授权的3D模型。为了防止这种侵权行为，我们提出了一种新的图像保护方法，在将图像提供给TGS之前，将不可见的几何扰动（称为“几何斗篷”）嵌入图像中。这些精心制作的扰动编码了一个定制的信息，当TGS尝试对隐形图像进行3D重建时，该信息就会显现出来。与简单地降低输出质量的传统对抗性攻击不同，我们的方法通过生成可识别的定制模式作为水印，迫使TGS以特定的方式失败3D重建。该水印允许版权所有者对从其受保护图像中进行的任何尝试的3D重建主张所有权。大量的实验已经验证了我们的几何斗篷的有效性。我们的项目可在https://qsong2001.github.io/geometry_cloak. et.al.|[2410.22705](http://arxiv.org/abs/2410.22705)|null|
|**2024-10-29**|**Guide3D: A Bi-planar X-ray Dataset for 3D Shape Reconstruction**|血管内手术工具重建是推进血管内工具导航的重要因素，是血管内手术的重要步骤。然而，缺乏公开可用的数据集严重限制了新型机器学习方法的开发和验证。此外，由于需要双平面扫描仪等专用设备，之前的大多数研究都采用了单平面荧光镜技术，因此只能从单一视角捕获数据，大大限制了重建精度。为了弥合这一差距，我们引入了Guide3D，这是一个用于3D重建的双平面X射线数据集。该数据集代表了在现实环境中捕获的高分辨率双平面手动注释荧光镜透视视频的集合。在反映临床环境的模拟环境中验证我们的数据集，证实了它对现实世界应用的适用性。此外，我们提出了一个新的导石形状预测基准，作为未来工作的有力基准。Guide3D不仅通过提供一个推进分割和3D重建技术的平台来满足基本需求，而且有助于开发更准确、更有效的血管内手术干预措施。我们的项目可在https://airvlab.github.io/guide3d/. et.al.|[2410.22224](http://arxiv.org/abs/2410.22224)|null|
|**2024-10-29**|**PF3plat: Pose-Free Feed-Forward 3D Gaussian Splatting**|我们考虑了在单个前馈中从非聚焦图像合成新视图的问题。我们的框架利用了3DGS的快速、可扩展性和高质量的3D重建和视图合成功能，我们进一步扩展了它，提供了一种实用的解决方案，放宽了常见的假设，如密集的图像视图、精确的相机姿态和大量的图像重叠。我们通过识别和解决使用像素对齐的3DGS所带来的独特挑战来实现这一目标：不同视图中未对齐的3D高斯分布会导致噪声或稀疏梯度，从而破坏训练的稳定性并阻碍收敛，尤其是在不满足上述假设的情况下。为了减轻这种情况，我们采用预训练的单目深度估计和视觉对应模型来实现3D高斯的粗略对齐。然后，我们引入了轻量级、可学习的模块，从粗对准中细化深度和姿态估计，提高了3D重建的质量和新颖的视图合成。此外，利用精细估计来估计几何置信度得分，该得分评估3D高斯中心的可靠性，并相应地调节高斯参数的预测。对大规模真实世界数据集的广泛评估表明，PF3plat在所有基准测试中都达到了新的最先进水平，并得到了验证我们设计选择的全面消融研究的支持。 et.al.|[2410.22128](http://arxiv.org/abs/2410.22128)|**[link](https://github.com/cvlab-kaist/PF3plat)**|
|**2024-10-29**|**PrefPaint: Aligning Image Inpainting Diffusion Model with Human Preference**|本文首次尝试通过强化学习框架将图像修复的扩散模型与人类美学标准对齐，显著提高了修复图像的质量和视觉吸引力。具体来说，我们没有直接用成对的图像来测量差异，而是用我们构建的数据集训练了一个奖励模型，该数据集由近51000张标注了人类偏好的图像组成。然后，我们采用强化学习过程来微调预训练的图像修复扩散模型的分布，以获得更高的回报。此外，我们从理论上推导了奖励模型误差的上限，这说明了在整个强化对齐过程中奖励估计的潜在置信度，从而促进了精确的正则化。对修复比较和下游任务（如图像扩展和3D重建）的广泛实验证明了我们方法的有效性，与最先进的方法相比，修复图像与人类偏好的对齐有了显著改善。这项研究不仅推进了图像修复领域的发展，还为基于建模奖励准确性将人类偏好纳入生成模型的迭代细化提供了一个框架，对视觉驱动的人工智能应用程序的设计具有广泛的意义。我们的代码和数据集可在以下网址公开获取https://prefpaint.github.io. et.al.|[2410.21966](http://arxiv.org/abs/2410.21966)|null|
|**2024-10-29**|**SS3DM: Benchmarking Street-View Surface Reconstruction with a Synthetic 3D Mesh Dataset**|为街景场景重建精确的3D表面对于数字娱乐和自动驾驶模拟等应用至关重要。然而，现有的街景数据集，包括KITTI、Waymo和nuScenes，只提供嘈杂的激光雷达点作为重建表面几何评估的地面真实数据。这些几何地面真理通常缺乏评估曲面位置所需的精度，也不提供评估曲面法线的数据。为了克服这些挑战，我们引入了SS3DM数据集，其中包括precist\textbf{S}ynthetic\textbf{S}treet-view\textbf{3D}\textbf{M}esh从CARLA模拟器导出的模型。这些网格模型有助于精确的位置评估，并包括用于评估表面法线的法线向量。为了在真实的驾驶场景中模拟输入数据以进行3D重建，我们在不同的室外场景中虚拟驾驶一辆配备了六个RGB摄像头和五个LiDAR传感器的车辆。利用这一数据集，我们为最先进的表面重建方法建立了一个基准，对相关挑战进行了全面评估。如需更多信息，请访问我们的主页https://ss3dm.top. et.al.|[2410.21739](http://arxiv.org/abs/2410.21739)|null|
|**2024-10-28**|**IndraEye: Infrared Electro-Optical UAV-based Perception Dataset for Robust Downstream Tasks**|深度神经网络（DNN）在电光（EO）相机捕获的光线充足的图像上训练时表现出了卓越的性能，这些图像提供了丰富的纹理细节。然而，在航空感知等关键应用中，DNN必须在所有条件下保持一致的可靠性，包括低光照场景，在这些场景中，光电摄像机往往难以捕捉到足够的细节。此外，由于不同高度和倾斜角度的尺度变化，基于无人机的空中目标检测面临着重大挑战，增加了另一层复杂性。现有的方法通常只解决域偏移时的照明变化或样式变化，但在空间感知中，相关性偏移也会影响DNN性能。本文介绍了IndraEye数据集，这是一个为各种任务设计的多传感器（EO-IR）数据集。它包括5612张图像，145666个实例，涵盖了印度次大陆的多个视角、高度、七种背景和一天中的不同时间。该数据集开辟了几个研究机会，如多模态学习、对象检测和分割的领域自适应，以及探索传感器特定的优缺点。IndraEye旨在通过支持开发更强大、更准确的空中感知系统来推进该领域的发展，特别是在具有挑战性的条件下。IndraEye数据集以对象检测和语义分割任务为基准。数据集和源代码可在https://bit.ly/indraeye. et.al.|[2410.20953](http://arxiv.org/abs/2410.20953)|null|
|**2024-10-28**|**ODGS: 3D Scene Reconstruction from Omnidirectional Images with 3D Gaussian Splattings**|全向（或360度）图像越来越多地用于3D应用，因为它们允许用单个图像渲染整个场景。基于神经辐射场的现有作品在以自我为中心的视频上展示了成功的3D重建质量，但它们的训练和渲染时间很长。最近，3D高斯散斑因其快速优化和实时渲染而受到关注。然而，由于两个图像域之间的光学特性不同，直接使用透视光栅化器对全向图像进行处理会导致严重失真。在这项工作中，我们提出了ODGS，这是一种用于全向图像的新型光栅化流水线，具有几何解释功能。对于每个高斯分布，我们定义一个与单位球体接触的切平面，该切平面垂直于朝向高斯中心的光线。然后，我们利用透视相机光栅化器将高斯投影到相应的切平面上。投影的高斯图像被转换并组合成全向图像，从而完成全向光栅化过程。这种解释揭示了所提出的管道中的隐含假设，我们通过数学证明进行了验证。整个光栅化过程使用CUDA并行化，实现了比基于NeRF的方法快100倍的优化和渲染速度。我们的综合实验通过在各种数据集上提供最佳的重建和感知质量，突显了ODGS的优越性。此外，漫游数据集的结果表明，即使在重建大型3D场景时，ODGS也能有效地恢复精细细节。源代码可以在我们的项目页面上找到(https://github.com/esw0116/ODGS). et.al.|[2410.20686](http://arxiv.org/abs/2410.20686)|null|
|**2024-10-27**|**Neural rendering enables dynamic tomography**|中断X射线计算机断层扫描（X-CT）一直是观察实验过程中材料变形的常用方法。虽然这种方法对于准静态实验是有效的，但在不可中断的动态实验中，永远不可能重建完整的三维断层扫描。在这项工作中，我们提出神经渲染工具可用于推动范式转变，以在动态事件中实现三维重建。首先，我们得出理论结果来支持投影角度的选择。通过合成和实验数据的结合，我们证明神经辐射场可以比传统的重建方法更有效地重建感兴趣的数据模态。最后，我们开发了一个基于样条的变形场时空模型，并证明该模型可以在现实实验中重建晶格样本的时空变形。 et.al.|[2410.20558](http://arxiv.org/abs/2410.20558)|null|
|**2024-10-26**|**Neural Fields in Robotics: A Survey**|神经场已经成为计算机视觉和机器人技术中3D场景表示的一种变革性方法，能够从姿势的2D数据中准确推断几何、3D语义和动力学。利用可微分渲染，神经场包括连续隐式和显式神经表示，实现了高保真3D重建、多模态传感器数据的集成和新视点的生成。这项调查探讨了它们在机器人技术中的应用，强调了它们在增强感知、规划和控制方面的潜力。它们的紧凑性、内存效率和可微性，以及与基础模型和生成模型的无缝集成，使其成为实时应用的理想选择，提高了机器人的适应性和决策能力。本文基于200多篇论文，对机器人中的神经场进行了全面的回顾，对各个领域的应用进行了分类，并评估了它们的优势和局限性。首先，我们介绍了四个关键的神经场框架：占用网络、有符号距离场、神经辐射场和高斯散斑。其次，我们详细介绍了神经场在五个主要机器人领域的应用：姿态估计、操纵、导航、物理和自动驾驶，重点介绍了关键工作，并讨论了要点和公开挑战。最后，我们概述了神经场在机器人技术中的局限性，并为未来的研究提出了有前景的方向。项目页面：https://robonerf.github.io et.al.|[2410.20220](http://arxiv.org/abs/2410.20220)|null|

<p align=right>(<a href=#updated-on-20241031>back to top</a>)</p>

## Diffusion

|Publish Date|Title|Abstract|PDF|Code|
|---|---|---|---|---|
|**2024-10-30**|**ReferEverything: Towards Segmenting Everything We Can Speak of in Videos**|我们提出了REM，这是一个用于分割视频中可以通过自然语言描述的广泛概念的框架。我们的方法利用了互联网规模数据集上的视频传播模型所学习的视觉语言表示。我们方法的一个关键见解是尽可能多地保留生成模型的原始表示，同时在窄域引用对象分割数据集上对其进行微调。因此，尽管我们的框架是在有限类别的对象掩码上训练的，但它可以准确地分割和跟踪稀有和看不见的对象。此外，它可以推广到非对象动态概念，例如海浪在海洋中撞击，正如我们新推出的参考视频处理分割（Ref-VPS）基准所证明的那样。我们的实验表明，REM在域内数据集（如Ref-DAVIS）上的表现与最先进的方法相当，同时在域外数据的区域相似性方面比它们高出12个点，利用了互联网规模预训练的力量。 et.al.|[2410.23287](http://arxiv.org/abs/2410.23287)|null|
|**2024-10-30**|**Provable acceleration for diffusion models under minimal assumptions**|虽然基于分数的扩散模型已经实现了卓越的采样质量，但它们的采样速度往往受到分数函数评估的高计算负担的限制。尽管最近在加速基于分数的采样器方面取得了显著的经验进展，但对加速技术的理论理解在很大程度上仍然有限。为了弥合这一差距，我们提出了一种新的随机采样器无训练加速方案。在最小假设下，即 $L^2$-精确的分数估计和目标分布的有限二阶矩条件下，我们的加速采样器在$\widetilde{O}（d^{5/4}/\sqrt{\varepsilon}）$迭代内的总变化中可证明达到$\varepilon$-精度，从而显著提高了基于标准分数的采样器的$\widetilde{O｝（d/\varepison）$ 迭代复杂性。值得注意的是，我们的收敛理论并不依赖于对目标分布或高阶分数估计保证的限制性假设。 et.al.|[2410.23285](http://arxiv.org/abs/2410.23285)|null|
|**2024-10-30**|**RelationBooth: Towards Relation-Aware Customized Object Generation**|定制图像生成对于根据用户提供的图像提示提供个性化内容至关重要，可以根据个人需求调整大规模文本到图像的扩散模型。然而，现有的模型往往忽视了生成图像中定制对象之间的关系。相反，这项工作通过关注关系感知的定制图像生成来解决这一差距，该生成旨在保留图像提示中的身份，同时保持文本提示中描述的谓词关系。具体来说，我们介绍了RelationsBooth，这是一个通过精心策划的数据集来解开身份和关系学习的框架。我们的训练数据由特定关系的图像、包含身份信息的独立对象图像和指导关系生成的文本提示组成。然后，我们提出了两个关键模块来解决两个主要挑战：生成准确和自然的关系，特别是在需要进行重大姿态调整时，以及在重叠的情况下避免对象混淆。首先，我们引入了一个关键点匹配损失，它有效地指导模型调整与它们的关系密切相关的物体姿态。其次，我们结合了图像提示中的局部特征，以更好地区分对象，防止重叠情况下的混淆。三个基准测试的广泛结果表明，RelationsBooth在生成精确关系的同时，在一组不同的对象和关系中保持对象身份的优越性。源代码和经过训练的模型将向公众开放。 et.al.|[2410.23280](http://arxiv.org/abs/2410.23280)|null|
|**2024-10-30**|**SlowFast-VGen: Slow-Fast Learning for Action-Driven Long Video Generation**|人类被赋予了一个互补的学习系统，它将对一般世界动态的缓慢学习与对新体验的情景记忆的快速存储联系起来。然而，之前的视频生成模型主要侧重于通过对大量数据进行预训练来实现缓慢学习，忽视了对情景记忆存储至关重要的快速学习阶段。这种疏忽导致在生成较长视频时，时间上相距遥远的帧之间存在不一致，因为这些帧超出了模型的上下文窗口。为此，我们介绍了一种用于动作驱动长视频生成的新型双速学习系统SlowFast VGen。我们的方法结合了一个用于世界动态缓慢学习的掩蔽条件视频扩散模型，以及一个基于时间LoRA模块的推理时间快速学习策略。具体而言，快速学习过程基于本地输入和输出更新其时间LoRA参数，从而在其参数中有效地存储情景记忆。我们进一步提出了一种慢速-快速学习循环算法，该算法将内部快速学习循环无缝集成到外部慢速学习循环中，从而能够回忆起之前的多集体验，用于情境感知技能学习。为了促进近似世界模型的缓慢学习，我们收集了一个包含20万个带有语言动作注释的视频的大规模数据集，涵盖了广泛的场景。广泛的实验表明，SlowFast VGen在动作驱动视频生成的各种指标上都优于基线，FVD得分为514，而782，并在较长的视频中保持一致性，平均场景剪切为0.37，而0.89。慢速快速学习循环算法也显著提高了长期规划任务的性能。项目网址：https://slowfast-vgen.github.io et.al.|[2410.23277](http://arxiv.org/abs/2410.23277)|null|
|**2024-10-30**|**Multi-student Diffusion Distillation for Better One-step Generators**|扩散模型以冗长的多步推理过程为代价实现了高质量的样本生成。为了克服这一点，扩散蒸馏技术产生的学生生成器能够在一个步骤中匹配或超越老师。然而，学生模型的推理速度受到教师架构大小的限制，阻碍了计算量大的应用程序的实时生成。在这项工作中，我们引入了多学生蒸馏（MSD），这是一个将条件教师扩散模型蒸馏成多个单步生成器的框架。每个学生生成器负责调节数据的一个子集，从而在相同容量下获得更高的生成质量。MSD训练多个蒸馏学生，允许更小的规模，从而更快的推理。此外，与具有相同架构的单学生蒸馏相比，MSD提供了轻量级的质量提升。我们通过使用分布匹配和对抗性蒸馏技术训练多个相同大小或更小的学生进行单步蒸馏，证明了MSD是有效的。对于较小的学生，MSD通过更快的单步生成推理获得了有竞争力的结果。使用4名相同尺寸的学生，MSD为一步图像生成设置了新的最先进的技术：ImageNet-64x64上的FID 1.20和零样本COCOCO2014上的8.20。 et.al.|[2410.23274](http://arxiv.org/abs/2410.23274)|null|
|**2024-10-30**|**Chapman-Enskog theory for nearly integrable quantum gases**|可积系统具有无限数量的守恒电荷，在流体动力学尺度上由广义流体力学（GHD）描述。当可积性被弱破坏并且探测到足够大的时空尺度时，这种描述就失效了。因此，涌现的流体力学取决于微扰守恒的电荷。我们关注具有守恒粒子数、动量和能量的几乎可积的伽利略不变系统。基于玻尔兹曼碰撞可积性破缺方法，我们用GHD方程补充碰撞项来描述系统的动力学。使用适用于GHD方程的Chapman-Enskog展开来解决大时空尺度的局限性。我们恢复了Navier-Stokes方程，并找到了输运系数：粘度和导热系数，这些系数是通过Chapman-Enskog积分方程的推广给出的。我们还观察到，与标准玻尔兹曼方程相比，准粒子的扩散引入了一个额外的小参数，丰富了展开的结构。 et.al.|[2410.23209](http://arxiv.org/abs/2410.23209)|null|
|**2024-10-30**|**Diffusive shock acceleration of dust grains at supernova remnants**|扩散激波加速（DSA）是一种在天体物理无碰撞激波中使带电粒子达到非常大刚度的突出机制。除了离子和电子，有人提出星际尘埃颗粒也可以通过扩散激波加速来加速，例如在超新星遗迹（SNR）处。考虑到不同大小和成分的星际尘埃颗粒，我们研究了在年轻的信噪比冲击下（在整个自由膨胀和塞多夫-泰勒阶段）颗粒加速的可能性，以及加速颗粒达到的最大能量。我们研究了宇宙射线成分中难熔物种相对于挥发性元素丰度的潜在影响。我们依赖于强冲击下粒子加速度的半解析描述，以及信噪比冲击波动力学的自相似解。为简单起见，考虑在均匀星际介质中膨胀的Ia型热核SNR。我们发现，对于尺寸为5×10^{-7} $cm的较小颗粒，尘埃颗粒以相对论速度加速是可能的，达到洛伦兹因子$\sim 10^{2}$，动能$E_{rm-k}/\text{nuc}\sim 10^ 2$GeV/nuc。我们发现，随后的颗粒溅射可以产生具有足够刚度的核，可以在扩散冲击加速过程中注入。这种情况可以自然地解释银河系宇宙射线成分中难熔元素过多的原因，前提是^{-3}-10^{-2}$ 被信噪比扫过的尘埃颗粒通过DSA通电。 et.al.|[2410.23190](http://arxiv.org/abs/2410.23190)|null|
|**2024-10-30**|**CausalDiff: Causality-Inspired Disentanglement via Diffusion Model for Adversarial Defense**|尽管正在努力保护神经分类器免受对抗性攻击，但它们仍然很脆弱，尤其是面对看不见的攻击。相比之下，人类很难被微妙的操纵所欺骗，因为我们只根据基本因素做出判断。受这一观察的启发，我们试图用基本的标签致病因素来模拟标签生成，并结合标签非致病因素来辅助数据生成。对于一个对抗性的例子，我们的目标是将扰动区分为非致病因素，并仅根据标签致病因素进行预测。具体来说，我们提出了一种因果扩散模型（CausalDiff），该模型将扩散模型应用于条件数据生成，并通过学习新的因果信息瓶颈目标来解开这两种因果因素。根据经验，CausalDiff在各种看不见的攻击上明显优于最先进的防御方法，在CIFAR-10上实现了86.39%（+4.01%）的平均鲁棒性，在CIFAR100上实现了56.25%（+3.13%），在GTSRB（德国交通标志识别基准）上实现了82.62%（+4.93%）。 et.al.|[2410.23091](http://arxiv.org/abs/2410.23091)|null|
|**2024-10-30**|**Controlling Language and Diffusion Models by Transporting Activations**|大型生成模型的能力不断增强，其部署也越来越广泛，这引发了人们对其可靠性、安全性和潜在误用的担忧。为了解决这些问题，最近的工作提出通过引导模型激活来控制模型生成，以有效地诱导或防止生成的输出中出现概念或行为。本文介绍了激活传输（AcT），这是一个由最优传输理论指导的引导激活的通用框架，推广了许多先前的激活引导工作。AcT与模态无关，以可忽略的计算开销提供对模型行为的细粒度控制，同时对模型能力的影响最小。我们通过实验证明了我们的方法的有效性和通用性，解决了大型语言模型（LLM）和文本到图像扩散模型（T2I）中的关键挑战。对于LLM，我们表明AcT可以有效减轻毒性，诱导任意概念，并提高其真实性。在T2I中，我们展示了AcT如何实现细粒度的样式控制和概念否定。 et.al.|[2410.23054](http://arxiv.org/abs/2410.23054)|null|
|**2024-10-30**|**Regularity and stability for the Gibbs conditioning principle on path space via McKean-Vlasov control**|我们考虑一个通过经验分布相互作用的扩散过程系统。假设给定可观测值的经验平均值可以在任何时候观察到，我们推导出了吉布斯条件原理相关版本中最优解的规律性和定量稳定性结果。这些证明依赖于对具有分布约束的McKean Vlasov控制问题的分析。对Hamilton-Jacobi-Bellman方程和扩散过程对数密度的Hessian进行了一些新的估计，这些估计具有独立的意义。 et.al.|[2410.23016](http://arxiv.org/abs/2410.23016)|null|

<p align=right>(<a href=#updated-on-20241031>back to top</a>)</p>

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

<p align=right>(<a href=#updated-on-20241031>back to top</a>)</p>

[contributors-shield]: https://img.shields.io/github/contributors/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[contributors-url]: https://github.com/Vincentqyw/cv-arxiv-daily/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[forks-url]: https://github.com/Vincentqyw/cv-arxiv-daily/network/members
[stars-shield]: https://img.shields.io/github/stars/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[stars-url]: https://github.com/Vincentqyw/cv-arxiv-daily/stargazers
[issues-shield]: https://img.shields.io/github/issues/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[issues-url]: https://github.com/Vincentqyw/cv-arxiv-daily/issues

