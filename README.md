[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]

## Updated on 2023.12.07
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
|**2023-12-06**|**DreamComposer: Controllable 3D Object Generation via Multi-View Conditions**|利用预先训练的2D大规模生成模型，最近的工作能够从单个野生图像中生成高质量的新视图。然而，由于缺乏来自多个视角的信息，这些作品在生成可控的小说视角方面遇到了困难。在本文中，我们提出了DreamComposer，这是一个灵活且可扩展的框架，可以通过注入多视图条件来增强现有的视图感知扩散模型。具体而言，DreamComposer首先使用视图感知三维提升模块从多个视图中获得对象的三维表示。然后，利用多视图特征融合模块从三维表示中提取目标视图的潜在特征。最后，将从多视图输入中提取的目标视图特征注入到预先训练的扩散模型中。实验表明，DreamComposer与用于零样本新视图合成的最先进的扩散模型兼容，进一步增强了它们以生成具有多视图条件的高保真度新视图图像，为可控3D对象重建和各种其他应用做好了准备。 et.al.|[2312.03611](http://arxiv.org/abs/2312.03611)|null|
|**2023-12-06**|**Artist-Friendly Relightable and Animatable Neural Heads**|创建照片逼真数字化身的一种越来越常见的方法是通过使用体积神经场。当在一组多视图图像上训练时，原始神经辐射场（NeRF）允许静态头部进行令人印象深刻的新颖视图合成，后续方法表明，这些神经表示可以扩展到动态化身。最近，新的变体也超过了神经表示中烘焙照明的常见缺点，表明静态神经化身可以在任何环境中重新发光。在这项工作中，我们同时解决了运动和照明问题，为可重新照明和可动画化的神经头提出了一种新方法。我们的方法建立在一种已验证的动态化身方法的基础上，该方法基于体积基元的混合，结合最近提出的用于可重新照明神经场的轻量级硬件设置，并包括一种新的架构，该架构允许重新照明动态神经化身在任何环境中执行看不见的表情，即使是在近场照明和视点的情况下。 et.al.|[2312.03420](http://arxiv.org/abs/2312.03420)|null|
|**2023-12-06**|**RING-NeRF: A Versatile Architecture based on Residual Implicit Neural Grids**|自引入以来，神经场在三维重建和新视图合成方面变得非常流行。最近的研究集中在加速这一过程，以及提高对观测距离和有限监督视点数量变化的鲁棒性。然而，这些方法往往导致无法轻易结合的专门解决方案。为了解决这个问题，我们引入了一种新的简单但高效的架构，称为RING-NeRF，基于残差隐式神经网格，它提供了对场景和潜在空间之间映射函数的细节级别的控制。与距离感知的前向映射机制和连续的从粗到细的重建过程相关联，我们的多功能架构在以下方面展示了快速训练和最先进的性能：（1）抗混叠渲染，（2）从很少监督的视点的重建质量，以及（3）对于基于SDF的NeRF在没有适当的场景特定初始化的情况下的鲁棒性。我们还证明了我们的架构可以动态添加网格来增加重建的细节，为自适应重建开辟了道路。 et.al.|[2312.03357](http://arxiv.org/abs/2312.03357)|null|
|**2023-12-06**|**Feature 3DGS: Supercharging 3D Gaussian Splatting to Enable Distilled Feature Fields**|近年来，3D场景表示已经获得了巨大的普及。使用神经辐射场的方法适用于传统任务，如新颖的视图合成。近年来，出现了一些工作，旨在将NeRF的功能扩展到视图合成之外，用于语义感知任务，如使用2D基础模型中的3D特征场提取进行编辑和分割。然而，这些方法有两个主要的局限性：（a）它们受到NeRF管道的渲染速度的限制，以及（b）隐式表示的特征场受到连续性伪影的影响，从而降低了特征质量。最近，3D高斯散射在实时辐射场渲染方面表现出了最先进的性能。在这项工作中，我们更进一步：除了辐射场渲染外，我们还通过2D基础模型蒸馏实现了对任意维度语义特征的3D高斯飞溅。这种转换并不简单：天真地将特征字段合并到3DGS框架中会导致扭曲级别的差异。我们建议对架构和培训进行更改，以有效地避免此问题。我们提出的方法是通用的，我们的实验展示了新颖的视图语义分割、语言引导编辑和通过从最先进的2D基础模型（如SAM和CLIP-LSeg）中学习特征字段来分割任何内容。在整个实验中，我们的蒸馏方法能够提供类似或更好的结果，同时训练和渲染速度明显更快。此外，据我们所知，我们是第一个通过利用SAM模型启用点和边界框提示进行辐射场操作的方法。项目网站：https://feature-3dgs.github.io/ et.al.|[2312.03203](http://arxiv.org/abs/2312.03203)|null|
|**2023-12-05**|**HybridNeRF: Efficient Neural Rendering via Adaptive Volumetric Surfaces**|神经辐射场提供了最先进的视图合成质量，但渲染速度往往较慢。一个原因是它们使用体积渲染，因此在渲染时每条光线需要许多采样（和模型查询）。尽管这种表示方式灵活且易于优化，但大多数真实世界的对象都可以使用曲面而不是体积更有效地建模，因此每条射线所需的采样数要少得多。这一观察结果促使表面表示（如符号距离函数）取得了相当大的进展，但这些方法可能难以对半透明和薄结构进行建模。我们提出了一种名为HybridNeRF的方法，该方法通过将大多数对象渲染为曲面，同时对（通常）一小部分具有挑战性的区域进行体积建模，来利用这两种表示的优势。我们针对具有挑战性的Eyeful Tower数据集以及其他常用的视图合成数据集对HybridNeRF进行了评估。与最先进的基线（包括最近基于光栅化的方法）相比，我们将错误率提高了15-30%，同时实现了虚拟现实分辨率（2Kx2K）的实时帧速率（至少36 FPS）。 et.al.|[2312.03160](http://arxiv.org/abs/2312.03160)|null|
|**2023-12-05**|**ReconFusion: 3D Reconstruction with Diffusion Priors**|神经辐射场（NeRFs）等3D重建方法擅长于绘制复杂场景的逼真新颖视图。然而，恢复高质量的NeRF通常需要数十到数百个输入图像，这导致了耗时的捕获过程。我们提出ReconFusion，只使用几张照片来重建真实世界的场景。我们的方法利用扩散先验进行新的视图合成，在合成和多视图数据集上训练，使基于NeRF的3D重建管道在输入图像集捕获的新相机姿态之外的新相机姿势下正则化。我们的方法在欠约束区域中合成逼真的几何体和纹理，同时保留观察到的区域的外观。我们在各种真实世界的数据集上进行了广泛的评估，包括前向和360度场景，证明了与以前的少数视图NeRF重建方法相比，性能有了显著提高。 et.al.|[2312.02981](http://arxiv.org/abs/2312.02981)|null|
|**2023-12-04**|**Calibrated Uncertainties for Neural Radiance Fields**|神经辐射场在新的视图合成方面取得了显著的成果，但仍然缺乏一个关键组成部分：精确测量其预测中的不确定性。概率NeRF方法试图解决这一问题，但它们的输出概率通常没有准确校准，因此无法捕捉模型的真实置信水平。在稀疏视图设置中，校准是一个特别具有挑战性的问题，因为在稀疏视图中，无法获得额外的保留数据来拟合推广到测试分布的校准器。在本文中，我们介绍了从NeRF模型中获得校准不确定性的第一种方法。我们的方法基于稳健有效的度量，从预测后验分布中计算每像素的不确定性。我们提出了两种技术来消除对保留数据的需求。第一种基于补丁采样，包括为每个场景训练两个NeRF模型。第二种是一种新的元校准器，只需要训练一个NeRF模型。我们提出的获得校准不确定性的方法在保持图像质量的同时，在稀疏视图设置中实现了最先进的不确定性。我们进一步证明了我们的方法在视图增强和次优视图选择等应用中的有效性。 et.al.|[2312.02350](http://arxiv.org/abs/2312.02350)|null|
|**2023-12-04**|**Re-Nerfing: Enforcing Geometric Constraints on Neural Radiance Fields through Novel Views Synthesis**|即使在大规模、无边界的场景中，神经辐射场（NeRF）也显示出了非凡的新颖视图合成能力，尽管需要数百个视图或在更稀疏的环境中引入伪影。只要只有很小的视觉重叠，它们的优化就会受到形状辐射模糊的影响。这会导致错误的场景几何体和伪影。在本文中，我们提出了Re-Nerfing，这是一种简单而通用的多阶段方法，利用NeRF自己的观点综合来解决这些局限性。通过Re-Nerfing，我们增加了场景的覆盖范围，并增强了新颖视图的几何一致性，如下所示：首先，我们用可用视图训练NeRF。然后，我们使用优化的NeRF来合成原始视图旁边的伪视图，以模拟立体或三焦点设置。最后，我们用原始视图和伪视图训练第二个NeRF，同时通过新合成的图像实施结构和核约束。在mip-NeRF 360数据集上进行的大量实验表明，在更密集和更稀疏的输入场景中，Re-Nerfing的有效性，为最先进的Zip-NeRF带来了改进，即使在使用所有视图进行训练时也是如此。 et.al.|[2312.02255](http://arxiv.org/abs/2312.02255)|null|
|**2023-12-04**|**GPS-Gaussian: Generalizable Pixel-wise 3D Gaussian Splatting for Real-time Human Novel View Synthesis**|我们提出了一种新的方法，称为GPS高斯，用于实时合成角色的新视图。所提出的方法能够在稀疏视图相机设置下实现2K分辨率的渲染。与需要按主题优化的原始高斯飞溅或神经隐式渲染方法不同，我们引入了在源视图上定义的高斯参数图，并直接回归高斯飞溅特性，用于即时新视图合成，而无需任何微调或优化。为此，我们在大量人体扫描数据上训练我们的高斯参数回归模块，并与深度估计模块一起将2D参数图提升到3D空间。所提出的框架是完全可微分的，在几个数据集上的实验表明，我们的方法优于最先进的方法，同时实现了超高的渲染速度。 et.al.|[2312.02155](http://arxiv.org/abs/2312.02155)|null|
|**2023-12-04**|**Fast View Synthesis of Casual Videos**|由于场景动力学和缺乏视差等挑战，从野外视频中合成新颖的视图是困难的。虽然现有的方法在隐式神经辐射场方面显示出了有希望的结果，但它们的训练和渲染速度很慢。本文重新审视了显式视频表示，以有效地从单目视频中合成高质量的新颖视图。我们分别处理静态和动态视频内容。具体来说，我们使用基于扩展平面的场景表示来构建全局静态场景模型，以合成时间相干的新颖视频。我们的基于平面的场景表示通过球面谐波和位移图来增强，以捕捉与视图相关的效果并对非平面复杂曲面几何体进行建模。为了提高效率，我们选择按帧点云来表示动态内容。虽然这种表示容易出现不一致，但由于运动，轻微的时间不一致在感知上被掩盖了。我们开发了一种快速估计这种混合视频表示并实时渲染新视图的方法。我们的实验表明，我们的方法可以从野外视频中渲染高质量的新视图，其质量与最先进的方法相当，同时在训练和实时渲染方面速度快100倍。 et.al.|[2312.02135](http://arxiv.org/abs/2312.02135)|null|

<p align=right>(<a href=#updated-on-20231207>back to top</a>)</p>

## 3D Reconstruction

|Publish Date|Title|Abstract|PDF|Code|
|---|---|---|---|---|
|**2023-12-06**|**DreamComposer: Controllable 3D Object Generation via Multi-View Conditions**|利用预先训练的2D大规模生成模型，最近的工作能够从单个野生图像中生成高质量的新视图。然而，由于缺乏来自多个视角的信息，这些作品在生成可控的小说视角方面遇到了困难。在本文中，我们提出了DreamComposer，这是一个灵活且可扩展的框架，可以通过注入多视图条件来增强现有的视图感知扩散模型。具体而言，DreamComposer首先使用视图感知三维提升模块从多个视图中获得对象的三维表示。然后，利用多视图特征融合模块从三维表示中提取目标视图的潜在特征。最后，将从多视图输入中提取的目标视图特征注入到预先训练的扩散模型中。实验表明，DreamComposer与用于零样本新视图合成的最先进的扩散模型兼容，进一步增强了它们以生成具有多视图条件的高保真度新视图图像，为可控3D对象重建和各种其他应用做好了准备。 et.al.|[2312.03611](http://arxiv.org/abs/2312.03611)|null|
|**2023-12-06**|**Gaussian-Flow: 4D Reconstruction with Dynamic 3D Gaussian Particle**|我们介绍了高斯流，这是一种新的基于点的方法，用于快速动态场景重建和多视图和单目视频的实时渲染。与因训练和渲染速度缓慢而受到阻碍的流行的基于NeRF的方法相比，我们的方法利用了基于点的3D高斯散射（3DGS）的最新进展。具体而言，提出了一种新的双域变形模型（DDDM）来显式地对每个高斯点的属性变形进行建模，其中通过时域中的多项式拟合和频域中的傅立叶级数拟合来捕获每个属性的时间相关残差。所提出的DDDM能够对长视频镜头中的复杂场景变形进行建模，消除了为每帧训练单独的3DGS的需要，或者引入了额外的隐式神经场来对3D动力学进行建模。此外，离散高斯点的显式变形建模确保了4D场景的超快速训练和渲染，这与为静态3D重建设计的原始3DGS相当。我们提出的方法展示了显著的效率提高，与每帧3DGS建模相比，训练速度快了5倍。此外，定量结果表明，所提出的高斯流在新视图渲染质量方面显著优于以前的主流方法。项目页面：https://nju-3dv.github.io/projects/gaussian-flow et.al.|[2312.03431](http://arxiv.org/abs/2312.03431)|null|
|**2023-12-06**|**Evaluating the point cloud of individual trees generated from images based on Neural Radiance fields (NeRF) method**|树木的三维重建一直是林业精确管理和研究的关键任务。由于树木本身的树枝形态结构复杂，以及树干、树枝和树叶的遮挡，传统的摄影测量方法很难从二维图像中重建完整的三维树木模型。在本研究中，基于各种相机以不同方式收集的树木图像，将神经辐射场（NeRF）方法用于单个树木的重建，并将导出的点云模型与摄影测量重建和激光扫描方法获得的点云进行比较。结果表明，NeRF方法在单株树木三维重建中表现良好，重建成功率较高，在树冠区域重建效果较好，所需图像量较少。与摄影测量重建方法相比，NeRF在重建效率上具有显著优势，适用于复杂场景，但生成的点云往往具有噪声大、分辨率低的特点。从摄影测量点云中提取的树木结构参数（树高和胸径）的精度仍然高于从NeRF点云中导出的精度。该研究结果说明了NeRF方法在个体树木重建方面的巨大潜力，为复杂森林场景的三维重建和可视化提供了新的思路和研究方向。 et.al.|[2312.03372](http://arxiv.org/abs/2312.03372)|null|
|**2023-12-06**|**RING-NeRF: A Versatile Architecture based on Residual Implicit Neural Grids**|自引入以来，神经场在三维重建和新视图合成方面变得非常流行。最近的研究集中在加速这一过程，以及提高对观测距离和有限监督视点数量变化的鲁棒性。然而，这些方法往往导致无法轻易结合的专门解决方案。为了解决这个问题，我们引入了一种新的简单但高效的架构，称为RING-NeRF，基于残差隐式神经网格，它提供了对场景和潜在空间之间映射函数的细节级别的控制。与距离感知的前向映射机制和连续的从粗到细的重建过程相关联，我们的多功能架构在以下方面展示了快速训练和最先进的性能：（1）抗混叠渲染，（2）从很少监督的视点的重建质量，以及（3）对于基于SDF的NeRF在没有适当的场景特定初始化的情况下的鲁棒性。我们还证明了我们的架构可以动态添加网格来增加重建的细节，为自适应重建开辟了道路。 et.al.|[2312.03357](http://arxiv.org/abs/2312.03357)|null|
|**2023-12-06**|**Bile Duct Segmentation Methods Under 3D Slicer Applied to ERCP: Advantages and Disadvantages**|本文对用于3D重建的胆道分割方法进行了评估，该方法在各种关键干预措施中可能非常有用，如使用3D Slicer软件的内镜逆行胰胆管造影（ERCP）。本文对用于3D重建的胆道分割技术进行了评估，通过使用3D Slicer软件，该技术在内镜逆行胰胆管造影（ERCP）等各种关键程序中具有很高的价值。评估了三种不同的方法，即阈值法、洪水填充法和区域增长法的优缺点。该研究涉及10个患者病例，并采用定量指标和定性评估来评估不同分割方法获得的分割结果。结果表明，阈值法几乎是手动的且耗时，而洪水填充法是半自动的且耗时。尽管这两种方法都提高了分割质量，但它们是不可重复的。因此，开发了一种基于区域生长的自动方法来减少分割时间，尽管这是以牺牲质量为代价的。这些发现突出了不同传统分割方法的优缺点，并强调了探索替代方法的必要性，如深度学习，以优化ERCP背景下的胆道分割。 et.al.|[2312.03356](http://arxiv.org/abs/2312.03356)|null|
|**2023-12-05**|**Fully Convolutional Slice-to-Volume Reconstruction for Single-Stack MRI**|在磁共振成像（MRI）中，切片到体积重建（SVR）是指从被运动破坏的2D切片堆中计算重建未知的3D磁共振体积。虽然很有前景，但目前的SVR方法需要多个切片堆栈来进行精确的3D重建，这导致了长扫描，并限制了它们在胎儿功能磁共振成像等时间敏感应用中的使用。在这里，我们提出了一种SVR方法，该方法克服了先前工作的缺点，并在存在极端片间运动的情况下产生了最先进的重建。受最近单视图深度估计方法成功的启发，我们将SVR公式化为单堆栈运动估计任务，并训练全卷积网络来预测给定切片堆栈的运动堆栈，从而产生3D重建作为预测运动的副产品。对成人和胎儿大脑的SVR进行的广泛实验表明，我们的全卷积方法的准确性是以前的SVR方法的两倍。我们的代码可在github.com/seannz/svr上获得。 et.al.|[2312.03102](http://arxiv.org/abs/2312.03102)|null|
|**2023-12-05**|**ReconFusion: 3D Reconstruction with Diffusion Priors**|神经辐射场（NeRFs）等3D重建方法擅长于绘制复杂场景的逼真新颖视图。然而，恢复高质量的NeRF通常需要数十到数百个输入图像，这导致了耗时的捕获过程。我们提出ReconFusion，只使用几张照片来重建真实世界的场景。我们的方法利用扩散先验进行新的视图合成，在合成和多视图数据集上训练，使基于NeRF的3D重建管道在输入图像集捕获的新相机姿态之外的新相机姿势下正则化。我们的方法在欠约束区域中合成逼真的几何体和纹理，同时保留观察到的区域的外观。我们在各种真实世界的数据集上进行了广泛的评估，包括前向和360度场景，证明了与以前的少数视图NeRF重建方法相比，性能有了显著提高。 et.al.|[2312.02981](http://arxiv.org/abs/2312.02981)|null|
|**2023-12-05**|**R3D-SWIN:Use Shifted Window Attention for Single-View 3D Reconstruction**|最近，视觉转换器在各种计算机视觉任务中表现良好，包括体素3D重建。然而，视觉转换器的窗口不是多尺度的，并且窗口之间没有连接，这限制了体素三维重建的准确性。因此，我们提出了一种移位窗口关注体素三维重建网络。据我们所知，这是第一项将移位窗口注意力应用于体素3D重建的工作。在ShapeNet上的实验结果验证了我们的方法在单视图重建中达到了SOTA的精度。 et.al.|[2312.02725](http://arxiv.org/abs/2312.02725)|null|
|**2023-12-05**|**DreaMo: Articulated 3D Reconstruction From A Single Casual Video**|关节式三维重建在各个领域都有着宝贵的应用，但它仍然成本高昂，需要领域专家的大量工作。无模板学习方法的最新进展显示出单目视频的良好效果。然而，这些方法需要全面覆盖输入视频中主题的所有观点，从而限制了其适用于从在线来源随意捕获的视频。在这项工作中，我们研究了从一个随意拍摄的互联网视频中进行的立体形状重建，其中受试者的视野覆盖不完整。我们提出了DreaMo，它在解决具有挑战性的低覆盖区域的同时，通过视图条件扩散先验和几个定制的正则化来联合执行形状重建。此外，我们还引入了一种骨骼生成策略，从学习的神经骨骼和蒙皮权重中创建人类可解释的骨骼。我们对一个以不完全视角覆盖为特征的自行收集的互联网视频集进行了研究。DreaMo在新颖的视图渲染、详细的关节形状重建和骨骼生成方面显示出良好的质量。大量的定性和定量研究验证了每个拟议组件的有效性，并表明由于视图覆盖不完整，现有方法无法解决正确的几何问题。 et.al.|[2312.02617](http://arxiv.org/abs/2312.02617)|null|
|**2023-12-05**|**Prompt2NeRF-PIL: Fast NeRF Generation via Pretrained Implicit Latent**|本文探索了可提示的NeRF生成（例如，文本提示或单个图像提示），用于直接调节和快速生成底层3D场景的NeRF参数，从而在提供具有条件控制的完整3D生成的同时，省去复杂的中间步骤。与之前涉及乏味的逐提示优化的基于扩散CLIP的管道不同，Prompt2NeRF PIL能够利用预先训练的NeRF参数的隐式潜在空间，通过单次前向传递生成各种3D对象。此外，在零样本任务中，我们的实验表明，由我们的方法产生的NeRF用作语义信息初始化，显著加速了现有提示-NeRF方法的推理过程。具体来说，我们将展示我们的方法将文本到NeRF模型DreamFusion的速度和图像到NeRF方法Zero-1-to-3的3D重建速度提高了3到5倍。 et.al.|[2312.02568](http://arxiv.org/abs/2312.02568)|null|

<p align=right>(<a href=#updated-on-20231207>back to top</a>)</p>

## Diffusion

|Publish Date|Title|Abstract|PDF|Code|
|---|---|---|---|---|
|**2023-12-06**|**Relightable Gaussian Codec Avatars**|重新照明的保真度受几何图形和外观表示的限制。对于几何体，网格和体积方法都很难对复杂的结构（如3D头发几何体）进行建模。就外观而言，现有的重新照明模型的保真度有限，而且往往太慢，无法在高分辨率连续环境中实时渲染。在这项工作中，我们提出了可信赖高斯编解码器化身，这是一种构建高保真度可信赖头部化身的方法，可以对其进行动画处理以生成新颖的表情。我们基于3D高斯的几何模型可以捕捉动态人脸序列上的头发和毛孔等3D一致的亚毫米细节。为了以统一的方式支持人类头部的不同材料，如眼睛、皮肤和头发，我们提出了一种基于可学习辐射转移的新型可重新照明外观模型。与漫射组件的全局照明感知球面谐波一起，我们使用球面高斯实现了空间全频反射的实时重新照明。该外观模型可以在点光和连续光照下有效地重新点亮。我们通过引入可重新照明的显式眼睛模型，进一步提高了眼睛反射的保真度，并实现了显式凝视控制。我们的方法在不影响实时性能的情况下优于现有方法。我们还展示了在线消费VR耳机上化身的实时重新照明，展示了我们化身的效率和保真度。 et.al.|[2312.03704](http://arxiv.org/abs/2312.03704)|null|
|**2023-12-06**|**Self-conditioned Image Generation via Generating Representations**|本文提出了一种简单有效的图像生成框架 $\textbf{R}$表示-$\textbf{C}$条件图像$\textbf{G}$生成（RCG），它为类无条件图像生成提供了一个新的基准。RCG不以任何人工注释为条件。相反，它以自监督表示分布为条件，该分布使用预训练的编码器从图像分布映射而来。在生成期间，RCG使用表示扩散模型（RDM）从这种表示分布中进行采样，并使用像素生成器来处理以采样的表示为条件的图像像素。这样的设计在生成过程中提供了实质性的指导，从而产生高质量的图像生成。在ImageNet 256$\times$ 256上测试，RCG实现了3.31的Frechet起始距离（FID）和253.4的起始得分（IS）。这些结果不仅显著提高了类无条件图像生成的技术水平，而且可以与当前类条件图像生成中的领先方法相媲美，弥补了这两项任务之间长期存在的性能差距。代码位于https://github.com/lth14/rcg. et.al.|[2312.03701](http://arxiv.org/abs/2312.03701)|**[link](https://github.com/LTH14/rcg)**|
|**2023-12-06**|**Memory Triggers: Unveiling Memorization in Text-To-Image Generative Models through Word-Level Duplication**|基于扩散的模型，如稳定扩散模型，凭借其产生高质量、高分辨率图像的能力，彻底改变了文本到图像的合成。这些进步促使图像生成和编辑任务取得了重大进展。然而，这些模型也引起了人们的关注，因为它们倾向于记忆并可能复制精确的训练样本，这会带来隐私风险，并导致对抗性攻击。训练数据集中的重复被认为是导致记忆的主要因素，到目前为止，已经对各种形式的记忆进行了研究。本文重点研究了在基于扩散的模型中，特别是在稳定扩散模型中，在推理过程中导致复制的两种不同且未被充分探索的复制类型。我们通过两个案例研究深入研究了这些研究较少的重复现象及其含义，旨在促进在各种应用中更安全、更负责任地使用生成模型。 et.al.|[2312.03692](http://arxiv.org/abs/2312.03692)|null|
|**2023-12-06**|**MatterGen: a generative model for inorganic materials design**|设计具有所需性能的功能材料对于推动储能、催化和碳捕获等领域的技术进步至关重要。生成模型通过在给定所需特性约束的情况下直接生成完全新颖的材料，为材料设计提供了一种新的范式。尽管最近取得了进展，但目前的生成模型在提出稳定晶体方面的成功率很低，或者只能满足一组非常有限的性质约束。在这里，我们介绍了MatterGen，这是一个在元素周期表中生成稳定、多样的无机材料的模型，可以进一步进行微调，以引导生成具有广泛性质限制的材料。为了实现这一点，我们引入了一种新的基于扩散的生成过程，该过程通过逐渐细化原子类型、坐标和周期晶格来产生晶体结构。我们进一步引入了适配器模块，以使用标记的数据集对任何给定的属性约束进行微调。与先前的生成模型相比，MatterGen产生的结构新颖稳定的可能性是现有模型的两倍多，距离局部能量最小值近15倍多。经过微调，MatterGen成功地产生了具有所需化学、对称性以及机械、电子和磁性的稳定新型材料。最后，我们通过提出既具有高磁密度又具有低供应链风险的化学成分的结构，展示了多性能材料的设计能力。我们认为，生成材料的质量和MatterGen能力的广度代表着在创建通用材料设计生成模型方面的重大进步。 et.al.|[2312.03687](http://arxiv.org/abs/2312.03687)|null|
|**2023-12-06**|**Periodic homogenization of a class of weakly coupled systems of linear PDEs**|本文基于概率方法，讨论了一类线性椭圆型和抛物型偏微分方程弱耦合系统的周期均匀化问题。在假设系统具有快速周期振荡系数的情况下，我们首先证明了相关状态切换扩散过程的适当中心和缩放的连续分量弱收敛于布朗运动，其协方差矩阵根据系统的系数给出。然后，通过使用系统解的概率表示和连续映射定理，得到均匀化结果。所给出的结果推广了一个方程的经典椭圆边值问题和经典抛物初值问题的周期均匀化的众所周知的结果。 et.al.|[2312.03680](http://arxiv.org/abs/2312.03680)|null|
|**2023-12-06**|**WarpDiffusion: Efficient Diffusion Model for High-Fidelity Virtual Try-on**|基于图像的虚拟试穿（VITON）旨在将店内服装图像转移到目标人身上。虽然现有的方法侧重于扭曲服装以适应身体姿势，但它们往往忽略了服装皮肤边界周围的合成质量以及扭曲服装上的皱纹和阴影等逼真效果。这些限制大大降低了生成结果的真实性，阻碍了VITON技术的实际应用。利用基于扩散的模型在跨模态图像合成中的显著成功，最近一些基于扩散的方法大胆地解决了这个问题。然而，他们往往要么消耗大量的训练资源，要么难以实现逼真的试穿效果并保留服装细节。对于高效和高保真的VITON，我们提出了WarpDiffusion，它通过一种新颖的信息和局部服装特征注意力机制，将基于翘曲和基于扩散的范式连接起来。具体而言，WarpDiffusion结合了局部纹理关注以减少资源消耗，并使用了一种新型的自动掩模模块，该模块仅有效地保留了扭曲服装的关键区域，而忽略了不现实或错误的部分。值得注意的是，WarpDiffusion可以作为即插即用组件集成到现有的VITON方法中，从而提高其合成质量。在高分辨率VITON基准和野外测试集上进行的大量实验证明了WarpDiffusion的优越性，在质量和数量上都超过了最先进的方法。 et.al.|[2312.03667](http://arxiv.org/abs/2312.03667)|null|
|**2023-12-06**|**TokenCompose: Grounding Diffusion with Token-level Supervision**|我们介绍了TokenCompose，这是一种用于文本到图像生成的潜在扩散模型，它增强了用户指定的文本提示和模型生成的图像之间的一致性。尽管取得了巨大的成功，但潜在扩散模型中的标准去噪过程仅以文本提示为条件，对文本提示和图像内容之间的一致性没有明确的约束，导致合成多个对象类别的结果不令人满意。TokenCompose旨在通过在微调阶段引入图像内容和对象分割图之间的令牌一致性项来改进多类别实例组合。TokenCompose可以直接应用于文本条件扩散模型的现有训练管道，而无需额外的人工标记信息。通过微调Stable Diffusion，该模型在多类别实例组成方面表现出显著改进，并增强了生成图像的真实感。 et.al.|[2312.03626](http://arxiv.org/abs/2312.03626)|null|
|**2023-12-06**|**DreamComposer: Controllable 3D Object Generation via Multi-View Conditions**|利用预先训练的2D大规模生成模型，最近的工作能够从单个野生图像中生成高质量的新视图。然而，由于缺乏来自多个视角的信息，这些作品在生成可控的小说视角方面遇到了困难。在本文中，我们提出了DreamComposer，这是一个灵活且可扩展的框架，可以通过注入多视图条件来增强现有的视图感知扩散模型。具体而言，DreamComposer首先使用视图感知三维提升模块从多个视图中获得对象的三维表示。然后，利用多视图特征融合模块从三维表示中提取目标视图的潜在特征。最后，将从多视图输入中提取的目标视图特征注入到预先训练的扩散模型中。实验表明，DreamComposer与用于零样本新视图合成的最先进的扩散模型兼容，进一步增强了它们以生成具有多视图条件的高保真度新视图图像，为可控3D对象重建和各种其他应用做好了准备。 et.al.|[2312.03611](http://arxiv.org/abs/2312.03611)|null|
|**2023-12-06**|**DiffusionSat: A Generative Foundation Model for Satellite Imagery**|扩散模型在包括图像、语音和视频在内的许多模态上都取得了最先进的结果。然而，现有的模型并不是专门为支持遥感数据而设计的，遥感数据被广泛用于环境监测和作物产量预测等重要应用。卫星图像与自然图像有很大不同——它们可以是多光谱的，在不同时间内不规则地采样——而且现有的基于网络图像的扩散模型不支持它们。此外，遥感数据本质上是时空的，需要基于字幕或图像的传统方法不支持的条件生成任务。在本文中，我们介绍了DiffusionSat，这是迄今为止在公开的大型高分辨率遥感数据集上训练的最大的生成基础模型。由于基于文本的字幕很少用于卫星图像，我们将相关元数据（如地理位置）作为条件信息。我们的方法产生逼真的样本，可用于解决多个生成任务，包括时间生成、给定多光谱输入的超分辨率和绘画。我们的方法优于以前最先进的卫星图像生成方法，是第一个大规模的卫星图像 $\textit｛generative｝$ 基础模型。 et.al.|[2312.03606](http://arxiv.org/abs/2312.03606)|null|
|**2023-12-06**|**MMM: Generative Masked Motion Model**|使用扩散和自回归模型的文本到运动生成的最新进展已经显示出有希望的结果。然而，这些模型经常在实时性能、高保真度和运动编辑性之间进行权衡。为了解决这一差距，我们引入了MMM，这是一种基于掩蔽运动模型的新颖而简单的运动生成范式。MMM由两个关键组件组成：（1）运动标记器，其将3D人类运动转换为潜在空间中的离散标记序列；以及（2）条件掩蔽运动转换器，其学习以预先计算的文本标记为条件来预测随机掩蔽的运动标记。通过在所有方向上关注运动和文本标记，MMM明确地捕捉运动标记之间的固有依赖性以及运动和文本令牌之间的语义映射。在推理过程中，这允许对与细粒度文本描述高度一致的多个运动标记进行并行和迭代解码，从而同时实现高保真度和高速运动生成。此外，MMM具有先天的运动编辑性。通过简单地将掩码标记放置在需要编辑的位置，MMM可以自动填充间隙，同时保证编辑和非编辑部分之间的平滑过渡。在HumanML3D和KIT-ML数据集上进行的大量实验表明，MMM在生成高质量运动方面超越了当前领先的方法（FID得分分别为0.08和0.429），同时提供了高级编辑功能，如身体部位修改、运动中间和长运动序列的合成。此外，MMM在单个中端GPU上比可编辑运动扩散模型快两个数量级。我们的项目页面位于\url{https://exitudio.github.io/mmm-page}。 et.al.|[2312.03596](http://arxiv.org/abs/2312.03596)|null|

<p align=right>(<a href=#updated-on-20231207>back to top</a>)</p>

## NeRF

|Publish Date|Title|Abstract|PDF|Code|
|---|---|---|---|---|
|**2023-12-06**|**Gaussian-Flow: 4D Reconstruction with Dynamic 3D Gaussian Particle**|我们介绍了高斯流，这是一种新的基于点的方法，用于快速动态场景重建和多视图和单目视频的实时渲染。与因训练和渲染速度缓慢而受到阻碍的流行的基于NeRF的方法相比，我们的方法利用了基于点的3D高斯散射（3DGS）的最新进展。具体而言，提出了一种新的双域变形模型（DDDM）来显式地对每个高斯点的属性变形进行建模，其中通过时域中的多项式拟合和频域中的傅立叶级数拟合来捕获每个属性的时间相关残差。所提出的DDDM能够对长视频镜头中的复杂场景变形进行建模，消除了为每帧训练单独的3DGS的需要，或者引入了额外的隐式神经场来对3D动力学进行建模。此外，离散高斯点的显式变形建模确保了4D场景的超快速训练和渲染，这与为静态3D重建设计的原始3DGS相当。我们提出的方法展示了显著的效率提高，与每帧3DGS建模相比，训练速度快了5倍。此外，定量结果表明，所提出的高斯流在新视图渲染质量方面显著优于以前的主流方法。项目页面：https://nju-3dv.github.io/projects/gaussian-flow et.al.|[2312.03431](http://arxiv.org/abs/2312.03431)|null|
|**2023-12-06**|**Artist-Friendly Relightable and Animatable Neural Heads**|创建照片逼真数字化身的一种越来越常见的方法是通过使用体积神经场。当在一组多视图图像上训练时，原始神经辐射场（NeRF）允许静态头部进行令人印象深刻的新颖视图合成，后续方法表明，这些神经表示可以扩展到动态化身。最近，新的变体也超过了神经表示中烘焙照明的常见缺点，表明静态神经化身可以在任何环境中重新发光。在这项工作中，我们同时解决了运动和照明问题，为可重新照明和可动画化的神经头提出了一种新方法。我们的方法建立在一种已验证的动态化身方法的基础上，该方法基于体积基元的混合，结合最近提出的用于可重新照明神经场的轻量级硬件设置，并包括一种新的架构，该架构允许重新照明动态神经化身在任何环境中执行看不见的表情，即使是在近场照明和视点的情况下。 et.al.|[2312.03420](http://arxiv.org/abs/2312.03420)|null|
|**2023-12-06**|**RING-NeRF: A Versatile Architecture based on Residual Implicit Neural Grids**|自引入以来，神经场在三维重建和新视图合成方面变得非常流行。最近的研究集中在加速这一过程，以及提高对观测距离和有限监督视点数量变化的鲁棒性。然而，这些方法往往导致无法轻易结合的专门解决方案。为了解决这个问题，我们引入了一种新的简单但高效的架构，称为RING-NeRF，基于残差隐式神经网格，它提供了对场景和潜在空间之间映射函数的细节级别的控制。与距离感知的前向映射机制和连续的从粗到细的重建过程相关联，我们的多功能架构在以下方面展示了快速训练和最先进的性能：（1）抗混叠渲染，（2）从很少监督的视点的重建质量，以及（3）对于基于SDF的NeRF在没有适当的场景特定初始化的情况下的鲁棒性。我们还证明了我们的架构可以动态添加网格来增加重建的细节，为自适应重建开辟了道路。 et.al.|[2312.03357](http://arxiv.org/abs/2312.03357)|null|
|**2023-12-06**|**Multifractality in critical neural field dynamics**|大脑临界性框架在很大程度上认为大脑动力学是单分形的，尽管实验证据表明大脑表现出显著的多重分形。为了理解多重分形是如何在类临界系统中出现的，我们使用了临界神经振荡的计算模型。我们发现多重分形在同步相变附近出现。这些发现表明，时间动力学的多重分形在神经场的临界点达到峰值，为解释大脑记录中的多重分形提供了一个生成模型。 et.al.|[2312.03219](http://arxiv.org/abs/2312.03219)|null|
|**2023-12-04**|**GaussianHead: Impressive 3D Gaussian-based Head Avatars with Dynamic Hybrid Neural Field**|以前的头部化身方法大多依赖于固定的显式基元（网格、点）或隐式曲面（符号距离函数）和体积神经辐射场，难以在高保真度、训练速度和资源消耗之间取得平衡。混合场最近的流行带来了新的表示，但受到通过固定映射获得的参数化因子的限制。我们提出了GaussianHead：一种基于各向异性三维高斯基元的头部化身算法。我们利用规范高斯来表示动态场景。使用显式“动态”三平面作为参数化头部几何的有效容器，与底层几何和三平面中的因子很好地对齐，我们获得了正则高斯的对齐正则因子。利用微小的MLP，因子被解码为3D高斯基元的不透明度和球面谐波系数。最后，我们使用高效的可微高斯光栅化器进行渲染。我们的方法显著受益于我们基于3D高斯的新表示，并且三平面中底层几何结构和因子的适当对齐变换消除了固定映射引入的偏差。与最先进的技术相比，我们在自我重建、新视图合成和跨身份再现等任务中实现了最佳的视觉效果，同时保持了高渲染效率（每帧0.12秒）。在某些情况下，甚至鼻子周围的毛孔也清晰可见。代码和其他视频可以在项目主页上找到。 et.al.|[2312.01632](http://arxiv.org/abs/2312.01632)|null|
|**2023-11-29**|**Accelerating Neural Field Training via Soft Mining**|我们提出了一种通过有效选择采样位置来加速神经场训练的方法。虽然神经场最近变得很流行，但它通常是通过对训练域进行统一采样或通过手工启发式进行训练的。我们证明，通过基于重要性采样的软挖掘技术可以提高收敛性和最终训练质量：我们不是完全考虑或忽略一个像素，而是用标量来衡量相应的损失。为了实现我们的想法，我们使用Langevin蒙特卡罗采样。我们表明，通过这样做，具有更高误差的区域被更频繁地选择，导致收敛速度提高了2倍以上。本研究的代码和相关资源可在https://ubc-vision.github.io/nf-soft-mining/. et.al.|[2312.00075](http://arxiv.org/abs/2312.00075)|null|
|**2023-11-29**|**Neural Fields with Thermal Activations for Arbitrary-Scale Super-Resolution**|最近的任意尺度单图像超分辨率（ASSR）方法已经使用局部神经场来表示可以以不同速率采样的连续信号。然而，在这样的公式中，场值的逐点查询并不自然地与给定像素的点扩散函数（PSF）匹配。在这项工作中，我们提出了一种设计神经场的新方法，使得可以使用高斯PSF来查询点，该函数在ASSR的分辨率之间移动时起到抗混叠的作用。我们使用从傅立叶理论和热方程导出的新激活函数来实现这一点。这不需要额外的成本：与图像域中的滤波不同，在我们的框架中使用高斯PSF查询点不会影响计算成本。与超网络相结合，我们的方法不仅提供了理论上有保证的抗混叠，而且为ASSR设置了一个新的标准，同时也比以前的方法更具参数效率。 et.al.|[2311.17643](http://arxiv.org/abs/2311.17643)|null|
|**2023-11-28**|**In Search of a Data Transformation That Accelerates Neural Field Training**|神经场是数据表示中一种新兴的范式，它训练神经网络来逼近给定的信号。阻碍其广泛采用的一个关键障碍是编码速度——生成神经场需要神经网络的过拟合，这可能需要大量的SGD步骤才能达到所需的保真度水平。在本文中，我们深入研究了数据转换对神经场训练速度的影响，特别是关注像素位置的排列如何影响SGD的收敛速度。与直觉相反，我们发现随机排列像素位置可以显著加速训练。为了解释这一现象，我们通过PSNR曲线、损失景观和误差模式来检验神经场训练。我们的分析表明，随机像素排列去除了易于拟合的模式，这有助于在早期阶段进行简单的优化，但阻碍了捕捉信号的精细细节。 et.al.|[2311.17094](http://arxiv.org/abs/2311.17094)|null|
|**2023-11-28**|**HumanGaussian: Text-Driven 3D Human Generation with Gaussian Splatting**|根据文本提示生成逼真的三维人体是一项理想但具有挑战性的任务。现有的方法通过分数蒸馏采样（SDS）优化3D表示，如网格或神经场，其存在细节不足或训练时间过长的问题。在本文中，我们提出了一个高效而有效的框架HumanGaussian，它可以生成具有细粒度几何结构和逼真外观的高质量3D人。我们的关键见解是，3D高斯飞溅是一种具有周期性高斯收缩或增长的高效渲染器，其中这种自适应密度控制可以由内在的人体结构自然引导。具体而言，1）我们首先提出了一种结构感知SDS，它可以同时优化人体外观和几何形状。利用RGB和深度空间的多模态得分函数来提取高斯致密化和修剪过程。2） 此外，我们通过将SDS分解为更嘈杂的生成分数和更干净的分类器分数，设计了一种退火的负提示引导，很好地解决了过饱和问题。在仅修剪阶段中，基于高斯大小进一步消除浮动伪影，以增强生成平滑度。大量实验证明了我们的框架具有卓越的效率和竞争力，在不同的场景下呈现了生动的3D人类。项目页面：https://alvinliu0.github.io/projects/humangaussian et.al.|[2311.17061](http://arxiv.org/abs/2311.17061)|null|
|**2023-11-28**|**SplitNeRF: Split Sum Approximation Neural Field for Joint Geometry, Illumination, and Material Estimation**|我们提出了一种新的方法，通过从一组具有固定照明的姿势图像中估计真实世界物体的几何结构、材料特性和环境照明来数字化它们。我们的方法将分割和近似与基于图像的照明结合到神经辐射场（NeRF）管道中，用于基于物理的实时渲染。我们建议使用单个场景特定的MLP来建模场景的照明，该MLP表示任意分辨率的预集成的基于图像的照明。我们通过开发一种基于有效蒙特卡罗采样的新型正则化子来实现预集成照明的精确建模。此外，我们还提出了一种新的方法，通过利用基于蒙特卡罗采样的类似正则化子来监督自遮挡预测。实验结果证明了我们的方法在估计场景几何、材料特性和照明方面的效率和有效性。我们的方法能够在单个NVIDIA A100 GPU中仅经过 ${\sim}1$ 小时的训练后就获得最先进的重新照明质量。 et.al.|[2311.16671](http://arxiv.org/abs/2311.16671)|null|

<p align=right>(<a href=#updated-on-20231207>back to top</a>)</p>

[contributors-shield]: https://img.shields.io/github/contributors/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[contributors-url]: https://github.com/Vincentqyw/cv-arxiv-daily/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[forks-url]: https://github.com/Vincentqyw/cv-arxiv-daily/network/members
[stars-shield]: https://img.shields.io/github/stars/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[stars-url]: https://github.com/Vincentqyw/cv-arxiv-daily/stargazers
[issues-shield]: https://img.shields.io/github/issues/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[issues-url]: https://github.com/Vincentqyw/cv-arxiv-daily/issues

