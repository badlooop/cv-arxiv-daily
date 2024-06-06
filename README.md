[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]

## Updated on 2024.06.06
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
|**2024-06-05**|**Dynamic 3D Gaussian Fields for Urban Areas**|我们提出了一种用于大规模动态城市区域的新型视图合成（NVS）的高效神经3D场景表示。现有作品由于其有限的视觉质量和非交互式渲染速度，不太适合混合现实或闭环模拟等应用。最近，基于光栅化的方法已经以令人印象深刻的速度实现了高质量的NVS。然而，这些方法仅限于小规模、同质的数据，即它们不能处理由于天气、季节和照明而引起的严重外观和几何变化，也不能扩展到具有数千张图像的更大的动态区域。我们提出了4DGF，这是一种神经场景表示，可扩展到大规模动态城市区域，处理异构输入数据，并显著提高渲染速度。我们使用3D高斯作为有效的几何支架，同时依赖神经场作为紧凑灵活的外观模型。我们在全局范围内通过场景图集成场景动力学，同时通过变形在局部范围内建模关节运动。这种分解方法实现了适用于真实世界应用程序的灵活场景合成。在实验中，我们的PSNR超过了最先进的3 dB，渲染速度超过了200倍。 et.al.|[2406.03175](http://arxiv.org/abs/2406.03175)|null|
|**2024-06-05**|**Event3DGS: Event-based 3D Gaussian Splatting for Fast Egomotion**|最近出现的3D高斯飞溅（3DGS）利用了显式基于点的表示的优势，显著提高了新视图合成的渲染速度和质量。然而，在具有高动态运动或具有挑战性照明条件的环境中的3D辐射场渲染在真实世界的机器人任务中仍然存在问题。原因是快速自我运动是现实世界中普遍存在的机器人任务，这会导致运动模糊，导致重建结构中的不准确和伪影。为了缓解这个问题，我们提出了Event3DGS，这是第一种仅从原始事件流中学习高斯飞溅的方法。通过利用事件相机的高时间分辨率和基于点的显式表示，Event3DGS可以在快速自我运动下仅从事件流中重建高保真3D结构。我们的稀疏性感知采样和渐进训练方法可以实现更好的重建质量和一致性。为了进一步提高外观的保真度，我们将运动模糊形成过程明确地纳入可微分光栅化器中，该光栅化器用于有限的模糊RGB图像集来细化外观。在多个数据集上进行的大量实验验证了Event3DGS与现有方法相比具有卓越的渲染质量，训练时间减少了95%以上，渲染速度提高了几个数量级。 et.al.|[2406.02972](http://arxiv.org/abs/2406.02972)|null|
|**2024-06-04**|**WE-GS: An In-the-wild Efficient 3D Gaussian Representation for Unconstrained Photo Collections**|在计算机图形学中，从不受约束的照片集合中进行新颖视图合成（NVS）是一项具有挑战性的工作。近年来，三维高斯散射（3DGS）在静态场景的真实感和实时NVS方面显示出了良好的前景。在3DGS的基础上，我们提出了一种有效的基于点的可微渲染框架，用于从照片集中重建场景。我们的关键创新是基于残差的球面谐波系数传递模块，该模块使3DGS适应不同的照明条件和光度后处理。这个轻量级模块可以预先计算，并确保从渲染图像到3D高斯属性的有效梯度传播。此外，我们观察到，外观编码器和瞬态掩模预测器，这两个来自无约束照片采集的NVS最关键的部分，可以是互利的。我们引入了一个即插即用的轻量级空间注意力模块，以同时预测每个图像的瞬态遮挡物和潜在外观表示。经过训练和预处理，我们的方法与标准3DGS格式和渲染管道保持一致，有助于无缝集成到各种3DGS应用程序中。在不同数据集上的大量实验表明，我们的方法在新视图和外观合成的渲染质量上优于现有方法，具有高收敛性和渲染速度。 et.al.|[2406.02407](http://arxiv.org/abs/2406.02407)|null|
|**2024-06-04**|**Learning Temporally Consistent Video Depth from Video Diffusion Priors**|这项工作解决了视频深度估计的挑战，它不仅期望每帧的准确性，而且更重要的是，期望跨帧的一致性。我们没有直接从头开始开发深度估计器，而是将预测任务重新表述为条件生成问题。这使我们能够利用嵌入现有视频生成模型中的先验知识，从而降低学习难度并增强可推广性。具体来说，我们研究了如何驯服公共的稳定视频扩散（SVD），以使用图像深度和视频深度数据集的混合从输入视频中预测可靠的深度。我们从经验上证实，程序训练策略——首先优化SVD的空间层，然后优化时间层，同时保持空间层冻结——在空间准确性和时间一致性方面产生了最佳结果。我们进一步研究了在任意长视频上进行推理的滑动窗口策略。我们的观察结果表明，效率和性能之间存在权衡，一帧重叠已经产生了有利的结果。大量的实验结果表明，与现有的替代方案相比，我们的方法（称为ChronoDepth）具有优势，特别是在估计深度的时间一致性方面。此外，我们强调了在两个实际应用中更一致的视频深度的好处：深度条件视频生成和新颖的视图合成。我们的项目页面位于https://jhaoshao.github.io/ChronoDepth/. et.al.|[2406.01493](http://arxiv.org/abs/2406.01493)|null|
|**2024-06-03**|**RaDe-GS: Rasterizing Depth in Gaussian Splatting**|高斯散射（GS）已被证明在新的视图合成中非常有效，可以实现高质量和实时的渲染。然而，它在重建详细的3D形状方面的潜力尚未得到充分探索。由于高斯飞溅的离散和非结构化性质，现有方法的形状精度往往有限，这使形状提取变得复杂。虽然最近的技术（如2D GS）试图改进形状重建，但它们经常以降低渲染质量和计算效率的方式重新表述高斯基元。为了解决这些问题，我们的工作引入了一种光栅化方法来渲染一般3D高斯飞溅的深度图和表面法线图。我们的方法不仅显著提高了形状重建的精度，而且保持了高斯散射固有的计算效率。我们的方法在DTU数据集上实现了与NeuraLangelo相当的切角距离误差，并且在Tanks&Temples数据集上获得了与传统高斯飞溅相似的训练和渲染时间。我们的方法是高斯飞溅的一个重大进步，可以直接集成到现有的基于高斯飞溅的方法中。 et.al.|[2406.01467](http://arxiv.org/abs/2406.01467)|null|
|**2024-06-03**|**Self-Calibrating 4D Novel View Synthesis from Monocular Videos Using Gaussian Splatting**|与神经辐射场（NeRF）相比，高斯散射（GS）显著提高了场景重建效率和新视图合成（NVS）精度，尤其是在动态场景中。然而，当前的4D NVS方法，无论是基于GS还是NeRF，主要依赖于COLMAP提供的相机参数，甚至利用COLMAP生成的稀疏点云进行初始化，这也缺乏准确性，并且是耗时的。这有时会导致较差的动态场景表示，尤其是在具有大对象移动或极端相机条件（例如小平移与大旋转相结合）的场景中。一些研究同时优化了相机参数和场景的估计，并通过从现成模型中获得的额外信息（如深度、光流等）进行监督。使用这些未经验证的信息作为基本事实会降低鲁棒性和准确性，这在长单目视频（例如>数百帧）中经常发生。我们提出了一种新的方法，该方法通过相机参数的自校准来学习高保真度4D GS场景表示。它包括提取稳健地表示3D结构的2D点特征，以及将其用于随后的相机参数和3D结构的联合优化，以实现整体4D场景优化。我们在几个标准基准上通过大量的定量和定性实验结果证明了我们方法的准确性和时间效率。结果表明，与最先进的4D新视图合成方法相比，有了显著的改进。源代码将很快在发布https://github.com/fangli333/SC-4DGS. et.al.|[2406.01042](http://arxiv.org/abs/2406.01042)|**[link](https://github.com/fangli333/sc-4dgs)**|
|**2024-06-02**|**Efficient Neural Light Fields (ENeLF) for Mobile Devices**|新颖视图合成（NVS）是计算机视觉和图形学中的一个挑战，它专注于在给定有限的真实输入图像集的情况下，从未观察到的相机姿势生成场景的真实图像。通过使用体积渲染，神经辐射场（NeRF）在渲染质量方面取得了令人印象深刻的效果。然而，由于体积渲染的计算成本高，NeRF及其变体不适合移动设备。神经光场（NeLF）的新兴研究通过直接学习从光线表示到像素颜色的映射，消除了对体积渲染的需求。NeLF已经证明了其实现类似于NeRF的结果的能力，但需要一个更广泛、计算密集的网络，该网络对移动不友好。与现有工作不同，这项研究建立在MobileR2L引入的新型网络架构的基础上，并积极应用压缩技术（信道结构修剪）来生成一个在移动设备上高效运行的模型，该模型具有更低的延迟和更小的尺寸，但性能略有下降。 et.al.|[2406.00598](http://arxiv.org/abs/2406.00598)|null|
|**2024-06-01**|**Bilateral Guided Radiance Field Processing**|神经辐射场（NeRF）利用多视图一致性，在合成新视图合成方面取得了前所未有的性能。在捕捉多个输入时，现代相机中的图像信号处理（ISP）会对其进行独立增强，包括曝光调整、颜色校正、局部色调映射等。这些处理虽然大大提高了图像质量，但往往会打破多视图一致性假设，导致重建的辐射场出现“漂浮物”。为了在不影响视觉美观的情况下解决这一问题，我们的目标是首先在NeRF训练阶段理清ISP的增强，并在完成阶段将用户期望的增强重新应用于重建的辐射场。此外，为了使重新应用的增强在新视图之间保持一致，我们需要在3D空间中执行成像信号处理（即“3D ISP”）。为此，我们采用双边网格，一种局部仿射模型，作为ISP处理的广义表示。具体来说，我们使用辐射场优化每个视图的3D双边网格，以近似每个输入视图的相机管道的效果。为了实现用户可调节的3D精加工，我们建议从给定的单视图编辑中学习低阶4D双边网格，将照片增强提升到整个3D场景。我们展示了我们的方法可以通过有效地去除漂浮物和执行用户修饰的增强来提高新视图合成的视觉质量。源代码和我们的数据位于：https://bilarfpro.github.io. et.al.|[2406.00448](http://arxiv.org/abs/2406.00448)|null|
|**2024-05-31**|**GS-Phong: Meta-Learned 3D Gaussians for Relightable Novel View Synthesis**|三维场景中的照明解耦对于新颖的视图合成和重新照明至关重要。在本文中，我们提出了一种新的方法，使用一组可重新照明的3D高斯点来表示点光源照明的场景。受Blinn Phong模型的启发，我们的方法将场景分解为环境光、漫反射和镜面反射组件，从而能够合成逼真的照明效果。为了便于独立于光照条件的几何信息的分解，我们引入了一种新的基于双层优化的元学习框架。其基本思想是将不同光照位置下的渲染任务视为一个多任务学习问题，我们的元学习方法不仅在不同的视点上，而且在不同的光照位置上推广所学习的高斯几何，从而有效地解决了这一问题。实验结果表明，与现有的自由视点重新照明方法相比，我们的方法在训练效率和渲染质量方面是有效的。 et.al.|[2405.20791](http://arxiv.org/abs/2405.20791)|null|
|**2024-05-31**|**ContextGS: Compact 3D Gaussian Splatting with Anchor Level Context Model**|近年来，三维高斯散射（3DGS）以其快速的渲染速度和高保真度，成为一种很有前途的新型视图合成框架。然而，大量的高斯及其相关属性需要有效的压缩技术。现有的方法主要单独和独立地压缩神经高斯，即同时对所有神经高斯进行编码，对它们的相互作用和空间依赖性几乎没有设计。受上下文模型在图像压缩中的有效性的启发，我们在这项工作中提出了第一个用于3DGS压缩的锚级别的自回归模型。我们将锚划分为不同的级别，并且可以在所有较粗级别中基于已经编码的锚来预测尚未编码的锚，从而实现更准确的建模和更高的编码效率。为了进一步提高熵编码的效率，例如，在没有已经编码的锚的情况下对最粗级别进行编码，我们建议引入低维量化特征作为每个锚的超优先级，该特征可以被有效压缩。我们的工作开创了3DGS表示的锚级别的上下文模型，与普通3DGS相比，尺寸缩小了100多倍，与最新的最先进的作品Scaffold GS相比，缩小了15倍，同时实现了相当甚至更高的渲染质量。 et.al.|[2405.20721](http://arxiv.org/abs/2405.20721)|**[link](https://github.com/wyf0912/contextgs)**|

<p align=right>(<a href=#updated-on-20240606>back to top</a>)</p>

## 3D Reconstruction

|Publish Date|Title|Abstract|PDF|Code|
|---|---|---|---|---|
|**2024-06-05**|**Ouroboros3D: Image-to-3D Generation via 3D-aware Recursive Diffusion**|现有的单图像到3D的创建方法通常包括两个阶段的过程，首先生成多视图图像，然后使用这些图像进行3D重建。然而，分别训练这两个阶段会导致推理阶段出现显著的数据偏差，从而影响重建结果的质量。我们引入了一个统一的3D生成框架，名为Ouroboros3D，它将基于扩散的多视图图像生成和3D重建集成到递归扩散过程中。在我们的框架中，这两个模块通过自我调节机制进行联合训练，使它们能够适应彼此的特征，从而进行稳健的推理。在多视图去噪过程中，多视图扩散模型使用重建模块在先前时间步长渲染的3D感知映射作为附加条件。具有3D感知反馈的递归扩散框架将整个过程统一起来，并提高了几何一致性。实验表明，我们的框架优于这两个阶段的分离以及在推理阶段将它们结合的现有方法。项目页面：https://costwen.github.io/Ouroboros3D/ et.al.|[2406.03184](http://arxiv.org/abs/2406.03184)|null|
|**2024-06-05**|**CAMEL. II. A 3D Coronal Mass Ejection Catalog Based on Coronal Mass Ejection Automatic Detection with Deep Learning**|日冕物质抛射是地磁风暴的主要驱动因素，可能会造成严重的空间天气影响。CME的自动检测、跟踪和三维（3D）重建对于CME到达的操作预测非常重要。日地关系天文台航天器上的COR1日冕仪促进了广泛的偏振观测，非常适合建立3D CME系统。我们开发了这样一个3D系统，包括四个模块：分类、分割、跟踪和3D重建。我们推广了我们之前预训练的分类模型来对COR1冠状图图像进行分类。随后，由于没有公开可用的CME分割数据集，我们使用大角度和光谱日冕仪C2观测手动注释CME的结构区域。利用基于变换器的模型，我们在CME分割方面取得了最先进的结果。此外，我们对跟踪算法进行了改进，以解决多个CME的分离任务。在最后一个模块中，跟踪结果与偏振比技术相结合，用于开发第一个单视图三维CME目录，而不需要手动掩模注释。我们的方法在自动2D CME目录中提供了更高的精度，并提供了更可靠的CME物理参数，包括3D传播方向和速度。上述3D CME系统可以应用于具有偏振测量能力的任何冠状图数据。 et.al.|[2406.02946](http://arxiv.org/abs/2406.02946)|null|
|**2024-06-04**|**3D-HGS: 3D Half-Gaussian Splatting**|照片真实感三维重建是三维计算机视觉中的一个基本问题。由于最近神经渲染技术的出现，该领域已经取得了相当大的进步。这些技术主要致力于学习3D场景的体积表示，并通过渲染产生的损失函数来细化这些表示。其中，3D高斯散射（3D-GS）已成为一种重要的方法，超过了神经辐射场（NeRFs）。3D-GS使用参数化的3D高斯来建模空间位置和颜色信息，并结合基于瓦片的快速渲染技术。尽管3D高斯核具有卓越的渲染性能和速度，但它在准确表示不连续函数方面存在固有的局限性，尤其是在形状不连续的边缘和角落，以及在颜色不连续的不同纹理上。为了解决这个问题，我们建议使用3D半高斯（3D-HGS）内核，它可以用作即插即用内核。我们的实验证明了它们能够在不影响渲染速度的情况下提高当前3D-GS相关方法的性能，并在各种数据集上实现最先进的渲染性能。 et.al.|[2406.02720](http://arxiv.org/abs/2406.02720)|null|
|**2024-06-03**|**MultiPly: Reconstruction of Multiple People from Monocular Video in the Wild**|我们提出了MultiPly，这是一种新颖的框架，可以从野生视频中的单眼重建3D多人。在野外视频中，重建多个自然移动和互动的个体是一项具有挑战性的任务。解决这一问题需要在没有任何受试者先验知识的情况下，对个体进行精确的像素级解纠缠。此外，它还需要从短视频序列中恢复复杂完整的3D人形，这增加了难度。为了应对这些挑战，我们首先定义了整个场景的分层神经表示，由单个人类和背景模型合成。我们通过分层可微体绘制从视频中学习分层神经表示。我们的混合实例分割方法进一步增强了这一学习过程，该方法结合了自监督的3D分割和可提示的2D分割模块，即使在密切的人类互动下也能产生可靠的实例分割监督。引入置信度引导的优化公式来交替优化人体姿势和形状/外观。我们结合了有效的目标，通过光度信息来完善人体姿态，并对人体动力学施加物理上合理的约束，从而实现高保真度的时间一致的3D重建。对我们方法的评估表明，在公开可用的数据集和野生视频中，我们的方法优于现有技术。 et.al.|[2406.01595](http://arxiv.org/abs/2406.01595)|null|
|**2024-06-03**|**Reconstructing and Simulating Dynamic 3D Objects with Mesh-adsorbed Gaussian Splatting**|3D重建和模拟虽然相互关联，但有着不同的目标：重建需要灵活的3D表示，以适应不同的场景，而模拟则需要结构化的表示来有效地建模运动原理。本文介绍了网格吸附高斯散射（MaGS）方法来解决这一难题。MaGS将3D高斯约束为悬停在网格表面上，从而创建相互吸附的网格高斯3D表示，该表示将3D高斯的渲染灵活性与网格的空间连贯性相结合。利用这种表示，我们引入了一个可学习的相对变形场（RDF）来对网格和3D高斯之间的相对位移进行建模，扩展了仅依赖ARAP先验的传统网格驱动变形范式，从而更准确地捕捉每个3D高斯的运动。通过联合优化网格、3D高斯和RDF，MaGS实现了高渲染精度和逼真变形。在D-NeRF和NeRF DS数据集上的大量实验表明，MaGS可以在重建和模拟中产生有竞争力的结果。 et.al.|[2406.01593](http://arxiv.org/abs/2406.01593)|null|
|**2024-06-03**|**Improved Three-Dimensional Reconstructions in Electron Ptychography through Defocus Series Measurements**|对厚标本三维相位重建的ptychography进行了详细分析。我们引入了多焦点ptychography，它结合了4D-STEM散焦系列，以通过更高的过分辨率提高沿光束方向的3D重建质量。将该方法与已建立的多切片ptychography技术进行比较，如常规ptychographic、正则ptychograph和多模式ptychology。此外，我们将多焦点ptychography与另一种方法进行了对比，该方法通过重建的散射矩阵（ $\mathcal{S}$ 矩阵）使用虚拟光学切片，与传统ptychographic相比，该方法提供了更精确的3D结构信息。我们基于模拟和实验数据进行的多次3D重建的结果表明，多焦点ptychography优于其他技术，尤其是在准确重建厚标本的表面和界面区域方面。 et.al.|[2406.01141](http://arxiv.org/abs/2406.01141)|null|
|**2024-06-01**|**Details Enhancement in Unsigned Distance Field Learning for High-fidelity 3D Surface Reconstruction**|虽然有符号距离域（SDF）已被公认用于对水密曲面进行建模，但无符号距离域将范围扩大到包括开放曲面和具有复杂内部结构的模型。尽管UDF具有灵活性，但它们在高保真3D重建中遇到了重大挑战，例如在零水平集的不可微性、难以实现精确的零值、许多局部极小值、消失梯度和零水平集附近的振荡梯度方向。为了应对这些挑战，我们提出了细节增强型UDF（DEUDF）学习，它集成了法线对齐和SIREN网络来捕捉精细的几何细节，自适应加权Eikonal约束来解决目标表面附近的消失梯度，基于无条件MLP的UDF表示来放松非负性约束，以及一种UDF定制的方法来提取具有非恒定等参值的等参表面。这些策略共同稳定了来自无方向点云的学习过程，并提高了UDF的准确性。我们的计算结果表明，DEUDF在重建表面的精度和质量方面都优于现有的UDF学习方法。我们将公开源代码。 et.al.|[2406.00346](http://arxiv.org/abs/2406.00346)|null|
|**2024-06-03**|**Physically Compatible 3D Object Modeling from a Single Image**|我们提出了一个计算框架，将单个图像转换为3D物理对象。图像中物理对象的视觉几何图形由三个正交属性决定：机械特性、外力和静止形状几何图形。现有的单视图3D重建方法往往忽略了这种潜在的组成，假定刚性或忽略外力。因此，重建的物体无法承受现实世界中的物理力，导致不稳定或不希望的变形——偏离了图像中所示的预期设计。我们的优化框架通过在重建过程中嵌入物理兼容性来解决这一问题。我们明确地分解了这三个物理属性，并通过静态平衡将它们联系起来，这是一个硬约束，确保优化的物理形状表现出所需的物理行为。对从Objaverse收集的数据集的评估表明，与现有方法相比，我们的框架始终增强了3D模型的物理真实性。我们的框架的实用性扩展到动态模拟和3D打印的实际应用，在这些应用中，遵守物理兼容性至关重要。 et.al.|[2405.20510](http://arxiv.org/abs/2405.20510)|null|
|**2024-05-30**|**Geometric Characterization of Rat Urinary Bladder Wall During Ex-Vivo Filling Using Micro-Computed Tomography (Micro-CT)**|本研究采用微型计算机断层扫描（micro-CT）来揭示大鼠膀胱壁在各种体外充盈状态下的几何复杂性，与通常理想化的均匀膀胱几何形状形成鲜明对比。通过分辨率在10-20微米之间的精确3D重建，这项研究仔细记录了膀胱在不同填充压力下的形态变化。这些发现说明了与均匀厚度的球形囊状物的理论模型的实质性偏差，特别是在从空隙状态到填充状态的过渡过程中，壁厚和囊状物体积的变化突出了这一点。这些结果对于完善膀胱功能的力学模型至关重要，传统上膀胱功能的机械模型过于简化了膀胱复杂的几何和生物力学行为。此外，这项研究强调了显微CT在深入了解膀胱力学方面的潜力，这对于推进膀胱出口梗阻（BOO）等疾病的治疗策略至关重要，从而增强手术和药物治疗模式。 et.al.|[2405.20454](http://arxiv.org/abs/2405.20454)|null|
|**2024-05-30**|**Learning 3D Robotics Perception using Inductive Priors**|深度学习的最新进展导致了以数据为中心的智能，即人工智能模型释放了吸收大量数据的潜力，并真正擅长执行数字任务，如文本到图像生成、机器-人类对话和图像识别。本文涵盖了利用结构化归纳偏见和先验知识进行学习的主题，以设计方法和算法来释放以原则为中心的智能的潜力。先验知识（简称先验）通常以过去的经验以及对世界如何运作的假设为依据，有助于自主主体更好地进行概括，并根据过去的经验调整其行为。在这篇论文中，我展示了先验知识在三个不同的机器人感知问题中的应用。1.以对象为中心的三维重建，2。决策的愿景和语言，以及3。3D场景理解。为了解决这些具有挑战性的问题，我提出了各种先验知识来源，包括1。来自合成数据的几何和外观先验，2。模块化和语义映射先验和3。语义、结构和上下文先验。我研究了解决机器人三维感知任务的这些先验，并提出了在深度学习模型中有效编码它们的方法。一些先验用于暖启动网络进行迁移学习，另一些则用作硬约束来限制机器人代理的动作空间。虽然经典技术很脆弱，无法推广到看不见的场景，并且以数据为中心的方法需要大量的标记数据，但本文旨在构建智能代理，这些智能代理需要很少的真实世界数据或仅从模拟中获取的数据，以推广到新模拟（即sim2sim）或真实世界看不见环境（即sim2real）中的高度动态和杂乱环境，从而对3D世界进行整体场景理解。 et.al.|[2405.20364](http://arxiv.org/abs/2405.20364)|null|

<p align=right>(<a href=#updated-on-20240606>back to top</a>)</p>

## Diffusion

|Publish Date|Title|Abstract|PDF|Code|
|---|---|---|---|---|
|**2024-06-05**|**Text-to-Events: Synthetic Event Camera Streams from Conditional Text Input**|事件摄像机对于需要具有低延迟和稀疏输出响应的视觉传感器的任务是有利的。然而，由于缺乏用于网络训练的大型标记事件相机数据集，使用事件相机的深度网络算法的开发一直很慢。本文报告了一种通过使用文本到X模型创建新的标记事件数据集的方法，其中X是一个或多个输出模式，在本工作的情况下，是事件。我们提出的文本到事件模型直接从文本提示生成合成事件帧。它使用一个经过训练的自动编码器来生成表示事件摄像机输出的稀疏事件帧。通过将预训练的自动编码器与扩散模型架构相结合，新的文本到事件模型能够生成运动对象的平滑合成事件流。自动编码器首先在不同场景的事件摄像机数据集上进行训练。在与扩散模型的组合训练中，使用了DVS手势数据集。我们证明了该模型可以生成由不同文本语句提示的真实的人类手势事件序列。使用在真实数据集上训练的分类器，生成的序列的分类准确率在42%到92%之间，具体取决于手势组。结果证明了该方法在综合事件数据集方面的能力。 et.al.|[2406.03439](http://arxiv.org/abs/2406.03439)|null|
|**2024-06-05**|**Non-stationary Spatio-Temporal Modeling Using the Stochastic Advection-Diffusion Equation**|我们通过随机偏微分方程（SPDE）构建了灵活的时空模型，其中扩散和平流都可以在空间上变化。通过有限体积法构造的SPDE解的高斯马尔可夫随机场近似进行计算。将新的灵活的不可分离模型与灵活的可分离模型在重建和预测方面进行了比较，并根据均方根误差和连续秩概率得分进行了评估。模拟研究表明，当数据具有扩散和平流等不可分离效应时，不可分离模型表现更好。此外，我们估计了用于模拟挪威Trondheimsfjorden海洋模型输出的替代模型，并模拟了自主潜水器的观测结果。结果表明，在未观测位置的实时预测方面，柔性不可分离模型优于柔性可分离模型。 et.al.|[2406.03400](http://arxiv.org/abs/2406.03400)|null|
|**2024-06-05**|**Reparameterization invariance in approximate Bayesian inference**|贝叶斯神经网络（BNN）中当前的近似后验表现出一个关键的局限性：它们在重新参数化下无法保持不变性，即BNN将不同的后验密度分配给相同函数的不同参数化。这在贝叶斯原理的应用中造成了一个根本缺陷，因为它打破了参数的不确定性与参数化函数的不确定性之间的对应关系。在本文中，我们在越来越流行的线性拉普拉斯近似的背景下研究了这个问题。具体来说，已经观察到线性化的预测可以缓解拉普拉斯近似中常见的拟合不足问题。我们发展了一个新的几何视图的重新参数化，从中我们解释了线性化的成功。此外，我们证明了这些重新参数化不变性可以扩展到使用黎曼扩散过程的原始神经网络预测，给出了近似后验采样的直接算法，这在经验上提高了后验拟合。 et.al.|[2406.03334](http://arxiv.org/abs/2406.03334)|null|
|**2024-06-05**|**UDQL: Bridging The Gap between MSE Loss and The Optimal Value Function in Offline Reinforcement Learning**|在绝大多数离线强化学习（RL）模型中，均方误差（MSE）通常用于估计最优值函数的解，并取得了优异的性能。然而，我们发现它的原理会导致对值函数的高估现象。本文首先从理论上分析了MSE引起的高估现象，给出了高估误差的理论上限。此外，为了解决这一问题，我们提出了一种新的Bellman低估算子来抵消高估现象，然后证明其收缩特性。最后，我们提出了基于低估算子和扩散策略模型的离线RL算法。在D4RL任务上的大量实验结果表明，我们的方法可以优于最先进的离线RL算法，这表明我们的理论分析和低估方法对离线RL任务是有效的。 et.al.|[2406.03324](http://arxiv.org/abs/2406.03324)|null|
|**2024-06-05**|**Text-to-Image Rectified Flow as Plug-and-Play Priors**|大规模扩散模型在生成任务中取得了显著的性能。除了最初的训练应用之外，这些模型已经证明了它们作为多功能即插即用先验的能力。例如，2D扩散模型可以用作优化3D隐式模型的损失函数。整流流是一类新的生成模型，它强制实现了从源分布到目标分布的线性级数，并在各个领域表现出了优异的性能。与基于扩散的方法相比，整流流方法在生成质量和效率方面都有所超越，需要更少的推理步骤。在这项工作中，我们提供了理论和实验证据，证明基于整流流的方法提供了与扩散模型相似的功能，它们也可以作为有效的先验。除了扩散先验的生成能力外，受整流流模型独特的时间对称性的激励，我们方法的一个变体还可以执行图像反演。在实验上，我们校正的基于流量的先验在文本到三维生成中优于它们的扩散对应物——SDS和VSD损失。我们的方法在图像反转和编辑方面也显示出有竞争力的性能。 et.al.|[2406.03293](http://arxiv.org/abs/2406.03293)|**[link](https://github.com/yangxiaofeng/rectified_flow_prior)**|
|**2024-06-05**|**Relative Entropy for the Numerical Diffusive Limit of the Linear Jin-Xin System**|本文讨论了金和辛模型的扩散极限及其渐近保持有限体积格式的逼近问题。在连续水平上，我们通过相对熵方法确定了扩散极限的收敛速度。考虑到半离散近似（空间上离散，时间上连续），我们将该方法应用于该半离散框架，并确定近似解以相同的收敛速度收敛到离散对流扩散极限。 et.al.|[2406.03268](http://arxiv.org/abs/2406.03268)|null|
|**2024-06-05**|**Generative Diffusion Models for Fast Simulations of Particle Collisions at CERN**|在高能物理中，模拟在揭示欧洲核子研究中心大型强子对撞机内粒子碰撞实验的复杂性方面发挥着至关重要的作用。机器学习模拟方法作为传统方法的有前途的替代方法已经引起了人们的关注。虽然现有的方法主要采用变分自动编码器（VAE）或生成对抗性网络（GANs），但最近的进展突出了扩散模型作为最先进的生成机器学习方法的有效性。我们在ALICE实验中首次基于扩散模型对零度热量计（ZDC）进行了模拟，与现有基线相比，实现了最高的保真度。我们对生成时间和模拟质量之间的权衡进行了分析。结果表明，潜在扩散模型由于生成时间快，具有很大的潜力。 et.al.|[2406.03233](http://arxiv.org/abs/2406.03233)|null|
|**2024-06-05**|**Holographic drag force with translational symmetry breaking**|为了研究阻力如何受到平移对称性破坏（TSB）的影响，我们使用了一个全息模型，其中背景度量保持平移对称，而理论中的引力子质量或其他场破坏了这种对称。考虑到参数 $\alpha$来自TSB的渐近AdS$_5$，我们解析计算了阻力。这个参数可以直观地理解为TSB强度的度量，我们预计它的非零值将影响阻力。在这种渐近AdS$_5$背景下，我们将证明$\alpha$的减少会导致阻力的减少。此外，我们还研究了扩散常数，它随着$\alpha$的增加而下降。最终将表明，在较低的$\alpha$或$\mu$ （化学势）值下，横向扩散系数大于纵向扩散系数，并且重夸克的速度对该比率的影响最小。 et.al.|[2406.03220](http://arxiv.org/abs/2406.03220)|null|
|**2024-06-05**|**Searching Priors Makes Text-to-Video Synthesis Better**|视频扩散模型的显著进步为文本到视频（T2V）合成领域带来了实质性进展。然而，现有的T2V合成模型难以准确生成复杂的运动动力学，导致视频真实感降低。一种可能的解决方案是收集大量数据并在此基础上训练模型，但这将非常昂贵。为了缓解这个问题，在本文中，我们将典型的T2V生成过程重新定义为基于搜索的生成管道。我们使用现有的视频作为运动先验数据库，而不是放大模型训练。具体来说，我们将T2V生成过程分为两个步骤：（i）对于给定的提示输入，我们搜索现有的文本视频数据集，以找到具有与提示动作密切匹配的文本标签的视频。我们提出了一种量身定制的搜索算法，该算法强调物体的运动特征。（ii）处理检索到的视频并将其提取为运动先验，以微调预先训练的基本T2V模型，然后使用输入提示生成所需视频。通过利用从搜索视频中收集的先验，我们增强了生成视频运动的真实性。所有操作都可以在单个NVIDIA RTX 4090 GPU上完成。我们通过不同的即时输入，对照最先进的T2V模型验证了我们的方法。该代码将公开。 et.al.|[2406.03215](http://arxiv.org/abs/2406.03215)|null|
|**2024-06-05**|**Ouroboros3D: Image-to-3D Generation via 3D-aware Recursive Diffusion**|现有的单图像到3D的创建方法通常包括两个阶段的过程，首先生成多视图图像，然后使用这些图像进行3D重建。然而，分别训练这两个阶段会导致推理阶段出现显著的数据偏差，从而影响重建结果的质量。我们引入了一个统一的3D生成框架，名为Ouroboros3D，它将基于扩散的多视图图像生成和3D重建集成到递归扩散过程中。在我们的框架中，这两个模块通过自我调节机制进行联合训练，使它们能够适应彼此的特征，从而进行稳健的推理。在多视图去噪过程中，多视图扩散模型使用重建模块在先前时间步长渲染的3D感知映射作为附加条件。具有3D感知反馈的递归扩散框架将整个过程统一起来，并提高了几何一致性。实验表明，我们的框架优于这两个阶段的分离以及在推理阶段将它们结合的现有方法。项目页面：https://costwen.github.io/Ouroboros3D/ et.al.|[2406.03184](http://arxiv.org/abs/2406.03184)|null|

<p align=right>(<a href=#updated-on-20240606>back to top</a>)</p>

## NeRF

|Publish Date|Title|Abstract|PDF|Code|
|---|---|---|---|---|
|**2024-06-05**|**Dynamic 3D Gaussian Fields for Urban Areas**|我们提出了一种用于大规模动态城市区域的新型视图合成（NVS）的高效神经3D场景表示。现有作品由于其有限的视觉质量和非交互式渲染速度，不太适合混合现实或闭环模拟等应用。最近，基于光栅化的方法已经以令人印象深刻的速度实现了高质量的NVS。然而，这些方法仅限于小规模、同质的数据，即它们不能处理由于天气、季节和照明而引起的严重外观和几何变化，也不能扩展到具有数千张图像的更大的动态区域。我们提出了4DGF，这是一种神经场景表示，可扩展到大规模动态城市区域，处理异构输入数据，并显著提高渲染速度。我们使用3D高斯作为有效的几何支架，同时依赖神经场作为紧凑灵活的外观模型。我们在全局范围内通过场景图集成场景动力学，同时通过变形在局部范围内建模关节运动。这种分解方法实现了适用于真实世界应用程序的灵活场景合成。在实验中，我们的PSNR超过了最先进的3 dB，渲染速度超过了200倍。 et.al.|[2406.03175](http://arxiv.org/abs/2406.03175)|null|
|**2024-06-04**|**A fast neural emulator for interstellar chemistry**|天体化学模型是解释不同环境中分子和原子物种观测结果的重要工具。然而，这些模型非常耗时，妨碍了对参数空间的彻底探索，导致了不确定性和偏差结果。使用神经网络来模拟天体化学模型的行为是规避这一问题的一种方法，它可以基于真实的天体化学模型提供快速计算。在本文中，我们提出了一个基于条件神经场的天文化学代码Nautilus的快速神经模拟器。由此产生的模型在1到10 $^7$年之间的任意时间内产生了192种物种的丰度。所有物种的不确定性都远低于0.2 dex，而计算时间比Nautilus小10$^4$ 。这将为执行更复杂的正向模型以更好地了解星际介质的物理性质开辟可能性。作为这些模型威力的一个例子，我们对Nautilus预测的电子丰度进行了特征重要性分析。我们发现，在低密度气体中，电子密度与初始硫丰度有关。将初始硫丰度从耗尽的情况增加到宇宙丰度会导致电子密度增加一个数量级。这种增强可能会对恒星形成地点的气体动力学产生潜在影响。 et.al.|[2406.02387](http://arxiv.org/abs/2406.02387)|null|
|**2024-06-05**|**AROMA: Preserving Spatial Structure for Latent PDE Modeling with Local Neural Fields**|我们提出了AROMA（带注意力的注意力降阶模型），这是一个旨在使用局部神经场增强偏微分方程（PDE）建模的框架。我们灵活的编码器-解码器架构可以从各种数据类型中获得空间物理场的平滑潜在表示，包括不规则网格输入和点云。这种多功能性消除了打补丁的需要，并允许高效处理各种几何形状。我们的潜在表示的顺序性质可以在空间上进行解释，并允许使用条件转换器来建模偏微分方程的时间动力学。通过采用基于扩散的公式，与传统的MSE训练相比，我们实现了更大的稳定性，并实现了更长的推广时间。AROMA在模拟1D和2D方程方面的卓越性能突显了我们的方法在捕捉复杂动力学行为方面的有效性。 et.al.|[2406.02176](http://arxiv.org/abs/2406.02176)|null|
|**2024-06-04**|**Activity patterns in ring networks of quadratic integrate-and-fire neurons with synaptic and gap junction coupling**|我们考虑具有非局部突触和间隙连接耦合的二次积分和激发神经元的环形网络。相应的神经场模型支持驻波和行波以及倾斜波等解决方案。我们证明了这些解中的许多都满足自洽方程，当参数变化时，自洽方程可以用来跟随它们。我们对神经场模型进行了数值分叉分析，重点研究了不同间隙结耦合强度的影响。我们的方法通常适用于各种各样的二次积分和激发神经元网络。 et.al.|[2406.01881](http://arxiv.org/abs/2406.01881)|null|
|**2024-06-03**|**Enhancing Dynamic CT Image Reconstruction with Neural Fields Through Explicit Motion Regularizers**|具有高度欠采样数据的动态逆问题的图像重建提出了一个主要挑战：不考虑过程的动力学会导致没有时间规律的不真实运动。已经提出了惩罚时间导数或引入运动模型正则化子的变分方法，以使用基于网格的离散化来关联后续帧并提高图像质量。神经场通过深度神经网络提供了所需时空量的替代参数化，这是一种轻量级、连续且偏向于平滑表示的网络。归纳偏差已被用于增强动态逆问题的时间规律性，从而仅通过最小化数据保真度项来优化神经场。在本文中，我们研究并展示了在2D+时间计算机断层扫描中引入基于显式PDE的运动正则化子，即光流方程，用于优化神经场的好处。我们还将神经场与基于网格的求解器进行了比较，并表明前者的性能优于后者。 et.al.|[2406.01299](http://arxiv.org/abs/2406.01299)|null|
|**2024-06-03**|**Pattern Formation in a Spiking Neural-Field of Renewal Neurons**|阐明神经模式形成背后的神经生理学机制仍然是计算神经科学中的一个突出挑战。在这篇论文中，我们通过考虑更新神经元网络来解决理解神经模式出现的问题，更新神经元是一类公认的尖峰细胞。在热力学极限下，网络的动力学可以精确地用一个偏微分方程和一个非局部微分方程来表示。确定了非局部系统的稳态，并进行了扰动分析，以分析表征图灵不稳定性发生的条件。考虑到突触耦合和外部驱动等神经网络参数，我们用数值方法获得了将异步状态与模式出现分开的分叉线。我们的理论发现为尖峰神经网络中图灵模式的出现提供了一个新的、有见地的视角。从长远来看，我们的形式主义将能够研究神经模式，同时保持微观细胞特性、网络耦合和图灵不稳定性的出现之间的联系。 et.al.|[2406.01167](http://arxiv.org/abs/2406.01167)|null|
|**2024-06-02**|**Representing Animatable Avatar via Factorized Neural Fields**|对于从单眼视频中重建高保真度的人体3D模型，保持一致的大规模体型以及精细匹配的细微皱纹至关重要。本文探讨了以下观察结果，即每帧渲染结果可以分解为与姿势无关的分量和相应的与姿势相关的等价物，以促进帧一致性。通过限制这两个分量的频带，可以进一步改进姿态自适应纹理。详细地说，与姿势无关的输出预计是低频的，而高频信息与姿势相关因素有关。我们通过具有不同频率分量的双分支网络实现了整个输入视频的粗体轮廓和时变的细粒度纹理特征的连贯保存。第一分支以规范空间中的坐标作为输入，而第二分支另外考虑由第一分支输出的特征和每个帧的姿态信息。我们的网络整合了两个分支预测的信息，并利用体积渲染生成照片逼真的3D人体图像。通过实验，我们证明了我们的网络在保留高频细节和确保身体轮廓一致方面超越了基于神经辐射场（NeRF）的最先进方法。 et.al.|[2406.00637](http://arxiv.org/abs/2406.00637)|null|
|**2024-05-31**|**Neural Gaussian Scale-Space Fields**|高斯尺度空间是信号表示和处理的基石，在滤波、多尺度分析、抗混叠等方面都有应用。然而，获得这样的尺度空间是昂贵和繁琐的，特别是对于诸如神经场的连续表示。我们提出了一种有效且轻量级的方法来学习任意信号的全连续、各向异性高斯尺度空间。基于傅立叶特征调制和Lipschitz边界，我们的方法是自监督训练的，即训练不需要任何手动滤波。我们的神经高斯尺度空间场忠实地捕捉各种模态的多尺度表示，并支持多种应用。其中包括图像、几何、光台数据、纹理抗锯齿和多尺度优化。 et.al.|[2405.20980](http://arxiv.org/abs/2405.20980)|null|
|**2024-05-30**|**Gated Fields: Learning Scene Reconstruction from Gated Videos**|根据时间观测重建户外3D场景是一项挑战，最近在神经领域的工作为其提供了一条新的途径。然而，仅从RGB捕获恢复场景属性（如几何体、外观或辐射）的现有方法在处理光线不足或纹理不足的区域时往往会失败。同样，使用扫描激光雷达传感器恢复场景也很困难，因为它们的角采样率较低，这使得恢复广阔的真实世界场景变得困难。为了解决这些差距，我们介绍了门控场——一种利用主动门控视频序列的神经场景重建方法。为此，我们提出了一种无缝结合时间门控捕获和照明的神经渲染方法。我们的方法利用了门控视频中的内在深度线索，无论环境照明条件如何，都能实现精确而密集的几何重建。我们在昼夜场景中验证了该方法，并发现门控场与RGB和激光雷达重建方法相比是有利的。我们的代码和数据集可在https://light.princeton.edu/gatedfields/. et.al.|[2405.19819](http://arxiv.org/abs/2405.19819)|null|
|**2024-06-04**|**Extreme Compression of Adaptive Neural Images**|隐式神经表示（INRs）和神经场是一种新的信号表示范式，从图像和音频到3D场景和视频。其基本思想是将信号表示为连续且可微分的神经网络。这一思想提供了前所未有的优势，如连续分辨率和存储效率，从而实现了新的压缩技术。然而，将数据表示为神经网络带来了新的挑战。例如，给定一个2D图像作为神经网络，我们如何进一步压缩这样的神经图像？。在这项工作中，我们提出了一种新的压缩神经场的分析，重点是图像。我们还介绍了自适应神经图像（ANI），这是一种有效的神经表示，能够适应不同的推理或传输要求。我们提出的方法可以将神经图像的每像素比特数（bpp）减少4倍，而不会丢失敏感细节或损害保真度。我们之所以能做到这一点，是因为我们成功地实现了4位神经表示。我们的工作为开发压缩神经场提供了一个新的框架。 et.al.|[2405.16807](http://arxiv.org/abs/2405.16807)|null|

<p align=right>(<a href=#updated-on-20240606>back to top</a>)</p>

[contributors-shield]: https://img.shields.io/github/contributors/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[contributors-url]: https://github.com/Vincentqyw/cv-arxiv-daily/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[forks-url]: https://github.com/Vincentqyw/cv-arxiv-daily/network/members
[stars-shield]: https://img.shields.io/github/stars/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[stars-url]: https://github.com/Vincentqyw/cv-arxiv-daily/stargazers
[issues-shield]: https://img.shields.io/github/issues/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[issues-url]: https://github.com/Vincentqyw/cv-arxiv-daily/issues

