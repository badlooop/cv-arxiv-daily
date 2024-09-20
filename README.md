[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]

## Updated on 2024.09.20
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
|**2024-09-18**|**LEMON: Localized Editing with Mesh Optimization and Neural Shaders**|在实际使用案例中，多边形网格编辑可能比生成新网格更快，但对用户来说仍然具有挑战性和耗时性。该问题的现有解决方案往往侧重于单一任务，无论是几何还是新颖的视图合成，这通常会导致网格和视图之间的结果脱节。在这项工作中，我们提出了LEMON，这是一种将神经延迟着色与局部网格优化相结合的网格编辑管道。我们的方法首先识别网格中最重要的顶点进行编辑，利用分割模型专注于这些关键区域。给定对象的多视图图像，我们优化神经着色器和多边形网格，同时从每个视图中提取法线贴图和渲染图像。通过使用这些输出作为条件数据，我们使用文本到图像扩散模型编辑输入图像，并在变形网格的同时迭代更新我们的数据集。该过程产生一个多边形网格，根据给定的文本指令进行编辑，保留初始网格的几何特征，同时关注最重要的区域。我们使用DTU数据集评估我们的管道，证明它比当前最先进的方法更快地生成精细编辑的网格。我们在补充材料中包含了我们的代码和其他结果。 et.al.|[2409.12024](http://arxiv.org/abs/2409.12024)|null|
|**2024-09-18**|**GaussianHeads: End-to-End Learning of Drivable Gaussian Head Avatars from Coarse-to-fine Representations**|人类头部化身的实时渲染是许多计算机图形应用程序的基石，如增强现实、视频游戏和电影等。最近的方法通过在仔细校准的多视图设置中使用计算高效的几何图元来解决这一挑战。尽管它能产生逼真的头部渲染，但它往往无法表示复杂的运动变化，如口腔内部和变化剧烈的头部姿势。我们提出了一种新的方法，可以从多视图图像中实时生成高度动态和可变形的人头化身。我们方法的核心是头部模型的分层表示，可以捕捉面部表情和头部运动的复杂动态。首先，通过从原始输入帧中提取丰富的面部特征，我们学习对模板网格的粗略面部几何形状进行变形。然后，我们在变形表面上初始化3D高斯分布，并逐步细化它们的位置。我们将这种从粗到细的面部化身模型以及头部姿势作为端到端框架中的可学习参数进行训练。这不仅可以通过视频输入实现可控的面部动画，还可以在大运动变化下对具有挑战性的面部表情进行高保真度的新颖视图合成，如舌头变形和精细的牙齿结构。此外，它鼓励学习到的头部化身在推理时对新的面部表情和头部姿势进行泛化。我们通过在不同数据集上与相关方法进行比较，展示了我们的方法的性能，跨越了多个身份的具有挑战性的面部表情序列。我们还通过演示跨身份面部表现转移应用程序，展示了我们方法的潜在应用。 et.al.|[2409.11951](http://arxiv.org/abs/2409.11951)|null|
|**2024-09-18**|**Single-Layer Learnable Activation for Implicit Neural Representation (SL $^{2}$A-INR)**|隐式神经表示（INR）利用神经网络将坐标输入转换为相应的属性，最近在几个视觉相关领域取得了重大进展。然而，INR的性能在很大程度上受到其多层感知器（MLP）架构中使用的非线性激活函数的选择的影响。已经研究了多种非线性；然而，目前的INR在捕获高频分量、不同信号类型和处理逆问题方面存在局限性。我们已经确定，通过引入INR的范式转变，可以大大缓解这些问题。我们发现，在初始层中具有可学习激活的架构可以表示底层信号中的精细细节。具体来说，我们提出了SL$^{2}$A-INR，这是一种具有单层可学习激活函数的INR混合网络，提高了传统基于ReLU的MLP的有效性。我们的方法在多种任务中表现出色，包括图像表示、3D形状重建、修复、单图像超分辨率、CT重建和新颖的视图合成。通过全面的实验，SL$^{2}$ A-INR在INR的准确性、质量和收敛速度方面设定了新的基准。 et.al.|[2409.10836](http://arxiv.org/abs/2409.10836)|null|
|**2024-09-15**|**MesonGS: Post-training Compression of 3D Gaussians via Efficient Attribute Transformation**|3D高斯散斑在新颖的视图合成中表现出卓越的质量和速度。然而，3D高斯分布的巨大文件大小给传输和存储带来了挑战。目前的工作设计了紧凑的模型来取代3D高斯模型的大量体积和属性，以及密集的训练来提取信息。这些努力需要大量的训练时间，为实际部署带来了巨大的障碍。为此，我们提出了MesonGS，一种用于3D高斯训练后压缩的编解码器。最初，我们引入了一种测量标准，该标准考虑了视图相关和视图无关的因素，以评估每个高斯点对渲染输出的影响，从而可以删除不重要的点。随后，我们通过两个变换来降低属性的熵，这两个变换补充了后续的熵编码技术，以提高文件压缩率。更具体地说，我们首先用欧拉角替换旋转四元数；然后，我们对关键属性应用区域自适应分层变换来降低熵。最后，我们采用更细粒度的量化来避免过度的信息丢失。此外，还设计了一个精心设计的微调方案来恢复质量。大量实验表明，MesonGS显著减小了3D高斯分布的大小，同时保持了具有竞争力的质量。 et.al.|[2409.09756](http://arxiv.org/abs/2409.09756)|null|
|**2024-09-13**|**Dense Point Clouds Matter: Dust-GS for Scene Reconstruction from Sparse Viewpoints**|3D高斯散斑（3DGS）在场景合成和新颖的视图合成任务中表现出了卓越的性能。通常，3D高斯基元的初始化依赖于从运动结构（SfM）方法导出的点云。然而，在需要从稀疏视点进行场景重建的场景中，3DGS的有效性受到这些初始点云的质量和输入图像数量有限的严重限制。在这项研究中，我们提出了Dust GS，这是一种专门为克服3DGS在稀疏视点条件下的局限性而设计的新框架。Dust GS引入了一种创新的点云初始化技术，即使在输入数据稀疏的情况下也能保持有效，而不是仅仅依赖SfM。我们的方法利用了一种混合策略，该策略集成了基于深度的自适应掩蔽技术，从而提高了重建场景的准确性和细节。在几个基准数据集上进行的广泛实验表明，Dust GS在稀疏视点的场景中优于传统的3DGS方法，在减少输入图像数量的情况下实现了卓越的场景重建质量。 et.al.|[2409.08613](http://arxiv.org/abs/2409.08613)|null|
|**2024-09-13**|**CSS: Overcoming Pose and Scene Challenges in Crowd-Sourced 3D Gaussian Splatting**|我们介绍了众包散点（CSS），这是一种新颖的3D高斯散点（3DGS）管道，旨在克服使用众包图像进行无姿态场景重建的挑战。从照片集中重建具有历史意义但难以接近的场景的梦想长期以来一直吸引着研究人员。然而，传统的3D技术在缺少相机姿态、有限的视点和不一致的照明方面存在困难。CSS通过稳健的几何先验和先进的照明建模来解决这些挑战，在复杂的现实世界条件下实现高质量的新颖视图合成。我们的方法对现有方法进行了明显的改进，为AR、VR和大规模3D重建中更准确、更灵活的应用铺平了道路。 et.al.|[2409.08562](http://arxiv.org/abs/2409.08562)|null|
|**2024-09-12**|**VI3DRM:Towards meticulous 3D Reconstruction from Sparse Views via Photo-Realistic Novel View Synthesis**|最近，像Zero-1-2-3这样的方法已经专注于基于单视图的3D重建，并取得了显著的成功。然而，他们对未知区域的预测在很大程度上依赖于大规模预训练扩散模型的归纳偏差。尽管后续的工作，如DreamComposer，试图通过结合其他视图使预测更加可控，但由于香草潜在空间中的特征纠缠，包括照明、材料和结构等因素，结果仍然不切实际。为了解决这些问题，我们引入了视觉各向同性3D重建模型（VI3DRM），这是一种基于扩散的稀疏视图3D重建模型，在ID一致和透视解纠缠的3D潜在空间中运行。通过促进语义信息、颜色、材质属性和光照的分离，VI3DRM能够生成与真实照片无法区分的高度逼真的图像。通过利用真实图像和合成图像，我们的方法能够精确构建点图，最终生成纹理精细的网格或点云。在GSO数据集上测试的NVS任务中，VI3DRM明显优于最先进的方法DreamComposer，PSNR为38.61，SSIM为0.929，LPIPS为0.027。代码将在发布后提供。 et.al.|[2409.08207](http://arxiv.org/abs/2409.08207)|null|
|**2024-09-12**|**Thermal3D-GS: Physics-induced 3D Gaussians for Thermal Infrared Novel-view Synthesis**|基于可见光的新型视图合成已经得到了广泛的研究。与可见光成像相比，热红外成像具有全天候成像和强穿透性的优势，为夜间和恶劣天气情况下的重建提供了更多的可能性。然而，热红外成像受到大气传输效应和热传导等物理特性的影响，阻碍了热红外场景中复杂细节的精确重建，表现为合成图像中的漂浮物和模糊边缘特征问题。为了解决这些局限性，本文介绍了一种名为Thermal3D GS的物理诱导3D高斯溅射方法。Thermal3D GS首先使用神经网络对三维介质中的大气传输效应和热传导进行建模。此外，在优化目标中加入了温度一致性约束，以提高热红外图像的重建精度。此外，为了验证我们的方法的有效性，创建了该领域的第一个大规模基准数据集，名为热红外新视图合成数据集（TI-NSD）。该数据集包括20个真实的热红外视频场景，涵盖室内、室外和无人机场景，共6664帧热红外图像数据。基于该数据集，本文实验验证了Thermal3D GS的有效性。结果表明，我们的方法优于基线方法，PSNR提高了3.03 dB，显著解决了基线方法中存在的浮点和模糊边缘特征的问题。我们的数据集和代码库将在\href中发布{https://github.com/mzzcdf/Thermal3DGS}｛\textcolor｛red｝｛Thermal3DGS｝｝。 et.al.|[2409.08042](http://arxiv.org/abs/2409.08042)|**[link](https://github.com/mzzcdf/thermal3dgs)**|
|**2024-09-11**|**Hi3D: Pursuing High-Resolution Image-to-3D Generation with Video Diffusion Models**|尽管在图像到3D的生成方面取得了巨大的进步，但现有的方法仍然难以生成具有高分辨率纹理的多视图一致图像，特别是在缺乏3D感知的2D扩散范式中。在这项工作中，我们提出了高分辨率图像到3D模型（Hi3D），这是一种新的基于视频扩散的范式，将单个图像重新定义为多视图图像，作为3D感知的顺序图像生成（即轨道视频生成）。该方法深入研究了视频扩散模型中潜在的时间一致性知识，该模型在3D生成中很好地推广了多个视图之间的几何一致性。从技术上讲，Hi3D首先为预训练的视频扩散模型赋予3D感知先验（相机姿态条件），从而产生具有低分辨率纹理细节的多视图图像。学习3D感知视频到视频细化器，以进一步放大具有高分辨率纹理细节的多视图图像。这种高分辨率的多视图图像通过3D高斯散点进一步增强了新的视图，最终通过3D重建获得高保真网格。对新颖视图合成和单视图重建的广泛实验表明，我们的Hi3D能够产生具有高度详细纹理的卓越多视图一致性图像。源代码和数据可在\url上获得{https://github.com/yanghb22-fdu/Hi3D-Official}. et.al.|[2409.07452](http://arxiv.org/abs/2409.07452)|**[link](https://github.com/yanghb22-fdu/hi3d-official)**|
|**2024-09-11**|**MVLLaVA: An Intelligent Agent for Unified and Flexible Novel View Synthesis**|本文介绍了MVLLaVA，一种专为新型视图合成任务设计的智能代理。MVLLaVA将多个多视图扩散模型与大型多模态模型LLaVA集成在一起，使其能够高效地处理各种任务。MVLLaVA代表了一个通用和统一的平台，可适应不同的输入类型，包括单个图像、描述性字幕或观看方位角的特定变化，由视点生成的语言指令指导。我们精心制作特定任务的指令模板，随后用于微调LLaVA。因此，MVLLaVA能够根据用户指令生成新颖的视图图像，展示了其在各种任务中的灵活性。通过实验验证了MVLLaVA的有效性，证明了其在应对各种新颖视图合成挑战方面的鲁棒性能和多功能性。 et.al.|[2409.07129](http://arxiv.org/abs/2409.07129)|null|

<p align=right>(<a href=#updated-on-20240920>back to top</a>)</p>

## 3D Reconstruction

|Publish Date|Title|Abstract|PDF|Code|
|---|---|---|---|---|
|**2024-09-17**|**fMRI-3D: A Comprehensive Dataset for Enhancing fMRI-based 3D Reconstruction**|从功能性磁共振成像（fMRI）数据重建3D视觉效果，在我们的会议工作中被称为Recon3DMind，对认知神经科学和计算机视觉都有重要意义。为了推进这项任务，我们展示了fMRI-3D数据集，其中包括来自15名参与者的数据，总共展示了4768个3D对象。该数据集由两个部分组成：fMRI Shape，之前介绍过，可在https://huggingface.co/datasets/Fudan-fMRI/fMRI-Shape，以及fMRI Objaverse，本文提出，可在https://huggingface.co/datasets/Fudan-fMRI/fMRI-Objaverse.fMRI Objaverse包括来自5名受试者的数据，其中4名也是fMRI Shape核心集的一部分，每位受试者查看117个类别的3142个3D对象，所有对象都附有文字说明。这大大增强了数据集的多样性和潜在应用。此外，我们提出了MinD-3D，这是一种新的框架，旨在从fMRI信号中解码3D视觉信息。该框架首先使用神经融合编码器从fMRI数据中提取和聚合特征，然后使用特征桥扩散模型生成视觉特征，最后使用生成变换解码器重建3D对象。我们通过在语义和结构层面设计指标来评估模型性能，从而建立新的基准。此外，我们评估了我们的模型在分布外环境中的有效性，并分析了提取特征的属性和fMRI信号中的视觉ROI。我们的实验表明，MinD-3D不仅能以高语义和空间精度重建3D对象，还能加深我们对人脑如何处理3D视觉信息的理解。项目页面位于：https://jianxgao.github.io/MinD-3D. et.al.|[2409.11315](http://arxiv.org/abs/2409.11315)|null|
|**2024-09-17**|**HGSLoc: 3DGS-based Heuristic Camera Pose Refinement**|视觉定位是指在已知的场景表示中确定相机姿态和方向的过程。这项任务经常因照明变化和视角变化等因素而变得复杂。本文提出了一种新的轻量级即插即用姿态优化框架HGSLoc，该框架将3D重建与启发式细化策略相结合，以实现更高的姿态估计精度。具体来说，我们引入了一个用于3D表示和高保真渲染的显式几何图，允许生成高质量的合成视图以支持精确的视觉定位。与基于NeRF的神经渲染定位方法相比，我们的方法具有更快的渲染速度和更高的定位精度。我们引入了一种启发式细化策略，其高效的优化能力可以快速定位目标节点，同时我们设置了步骤级优化步骤，以提高误差较小的场景中的姿态精度。通过精心设计的启发式函数，它提供了高效的优化能力，能够快速减少粗略定位估计中的误差。与神经网络联合优化策略相比，我们的方法减轻了对复杂神经网络模型的依赖，同时在具有挑战性的环境中表现出对噪声的鲁棒性和更高的定位精度。本文提出的优化框架通过整合3D重建和启发式细化策略的优点，引入了视觉定位的新方法，在多个基准数据集（包括7Scenes和DB数据集）上表现出了强大的性能。 et.al.|[2409.10925](http://arxiv.org/abs/2409.10925)|null|
|**2024-09-15**|**GRIN: Zero-Shot Metric Depth with Pixel-Level Diffusion**|从单个图像进行3D重建是计算机视觉中一个长期存在的问题。基于学习的方法通过利用越来越大的标记和未标记数据集来产生能够跨域生成准确预测的几何先验，从而解决其固有的尺度模糊问题。因此，现有技术的方法在零样本相对和度量深度估计方面表现出令人印象深刻的性能。最近，扩散模型在其学习表示中表现出显著的可扩展性和可推广性。然而，由于这些模型重新利用了最初为图像生成设计的工具，它们只能在密集的地面真实情况下运行，而这对于大多数深度标签来说都是不可用的，尤其是在现实世界中。本文介绍了GRIN，这是一种高效的扩散模型，旨在摄取稀疏的非结构化训练数据。我们使用具有3D几何位置编码的图像特征来全局和局部地调节扩散过程，从而在像素级别生成深度预测。通过对八个室内和室外数据集的综合实验，我们表明，即使在从头开始训练的情况下，GRIN也在零样本度量单目深度估计方面建立了一种新的技术状态。 et.al.|[2409.09896](http://arxiv.org/abs/2409.09896)|null|
|**2024-09-14**|**VSFormer: Mining Correlations in Flexible View Set for Multi-view 3D Shape Understanding**|基于视图的方法在3D形状理解方面表现出了很好的性能。然而，他们往往对视图之间的关系做出强烈的假设，或者间接地学习多视图相关性，这限制了探索视图间相关性的灵活性和目标任务的有效性。为了克服上述问题，本文研究了多视图的灵活组织和显式关联学习。特别是，我们建议将3D形状的不同视图合并到一个置换不变集，称为\emph{View set}，它消除了刚性关系假设，促进了视图之间充分的信息交换和融合。基于此，我们设计了一个灵活的Transformer模型，名为\emph{VSFormer}，以明确地捕获集合中所有元素的成对和高阶相关性。同时，我们从理论上揭示了视图集的笛卡尔积与注意力机制中的相关矩阵之间的自然对应关系，这支持了我们的模型设计。综合实验表明，VSFormer具有更好的灵活性、高效的推理效率和优越的性能。值得注意的是，VSFormer在各种3d识别数据集上达到了最先进的结果，包括ModelNet40、ScanObjectNN和RGBD。它还建立了SHREC'17检索基准的新记录。代码和数据集可在\url上获得{https://github.com/auniquesun/VSFormer}. et.al.|[2409.09254](http://arxiv.org/abs/2409.09254)|**[link](https://github.com/auniquesun/vsformer)**|
|**2024-09-13**|**CSS: Overcoming Pose and Scene Challenges in Crowd-Sourced 3D Gaussian Splatting**|我们介绍了众包散点（CSS），这是一种新颖的3D高斯散点（3DGS）管道，旨在克服使用众包图像进行无姿态场景重建的挑战。从照片集中重建具有历史意义但难以接近的场景的梦想长期以来一直吸引着研究人员。然而，传统的3D技术在缺少相机姿态、有限的视点和不一致的照明方面存在困难。CSS通过稳健的几何先验和先进的照明建模来解决这些挑战，在复杂的现实世界条件下实现高质量的新颖视图合成。我们的方法对现有方法进行了明显的改进，为AR、VR和大规模3D重建中更准确、更灵活的应用铺平了道路。 et.al.|[2409.08562](http://arxiv.org/abs/2409.08562)|null|
|**2024-09-12**|**VI3DRM:Towards meticulous 3D Reconstruction from Sparse Views via Photo-Realistic Novel View Synthesis**|最近，像Zero-1-2-3这样的方法已经专注于基于单视图的3D重建，并取得了显著的成功。然而，他们对未知区域的预测在很大程度上依赖于大规模预训练扩散模型的归纳偏差。尽管后续的工作，如DreamComposer，试图通过结合其他视图使预测更加可控，但由于香草潜在空间中的特征纠缠，包括照明、材料和结构等因素，结果仍然不切实际。为了解决这些问题，我们引入了视觉各向同性3D重建模型（VI3DRM），这是一种基于扩散的稀疏视图3D重建模型，在ID一致和透视解纠缠的3D潜在空间中运行。通过促进语义信息、颜色、材质属性和光照的分离，VI3DRM能够生成与真实照片无法区分的高度逼真的图像。通过利用真实图像和合成图像，我们的方法能够精确构建点图，最终生成纹理精细的网格或点云。在GSO数据集上测试的NVS任务中，VI3DRM明显优于最先进的方法DreamComposer，PSNR为38.61，SSIM为0.929，LPIPS为0.027。代码将在发布后提供。 et.al.|[2409.08207](http://arxiv.org/abs/2409.08207)|null|
|**2024-09-12**|**SPARK: Self-supervised Personalized Real-time Monocular Face Capture**|前馈单目人脸捕捉方法试图从一个人的单幅图像中重建姿势人脸。当前最先进的方法能够通过利用人脸的大型图像数据集，在各种身份、光照条件和姿势下实时回归参数化3D人脸模型。然而，这些方法存在明显的局限性，因为底层参数化人脸模型仅提供人脸形状的粗略估计，从而限制了它们在需要精确3D重建的任务（衰老、人脸交换、数字化妆等）中的实际适用性。本文提出了一种利用受试者的无约束视频集合作为先验信息进行高精度3D人脸捕捉的方法。我们的建议建立在两阶段方法的基础上。我们从重建人的详细3D面部化身开始，从一组视频中捕捉精确的几何形状和外观。然后，我们使用预训练的单眼人脸重建方法中的编码器，用我们的个性化模型替换其解码器，并对视频采集进行迁移学习。使用我们预先估计的图像形成模型，我们可以获得更精确的自我监督目标，从而改善表情和姿势对齐。这使得经过训练的编码器能够从以前看不见的图像中实时有效地回归姿态和表情参数，并与我们的个性化几何模型相结合，产生更准确和高保真的网格推理。通过广泛的定性和定量评估，我们展示了最终模型与最先进的基线相比的优越性，并展示了其对看不见的姿势、表情和光照的泛化能力。 et.al.|[2409.07984](http://arxiv.org/abs/2409.07984)|null|
|**2024-09-12**|**Advancing Depth Anything Model for Unsupervised Monocular Depth Estimation in Endoscopy**|深度估计是3D重建的基石，在微创内窥镜手术中起着至关重要的作用。然而，目前大多数深度估计网络都依赖于传统的卷积神经网络，这些网络在捕获全局信息的能力方面受到限制。基础模型为增强深度估计提供了一条有前景的途径，但目前可用的模型主要是在自然图像上训练的，导致应用于内窥镜图像时性能不佳。在这项工作中，我们为深度任意模型引入了一种新的微调策略，并将其与基于内在的无监督单目深度估计框架相结合。我们的方法包括一种基于随机向量的低秩自适应技术，提高了模型对不同尺度的适应性。此外，我们提出了一种基于深度可分离卷积的残差块，以补偿变换器捕获高频细节（如边缘和纹理）的有限能力。我们在SCARED数据集上的实验结果表明，我们的方法在最小化可训练参数数量的同时实现了最先进的性能。将这种方法应用于微创内窥镜手术可以显著提高这些手术的准确性和安全性。 et.al.|[2409.07723](http://arxiv.org/abs/2409.07723)|null|
|**2024-09-11**|**Hi3D: Pursuing High-Resolution Image-to-3D Generation with Video Diffusion Models**|尽管在图像到3D的生成方面取得了巨大的进步，但现有的方法仍然难以生成具有高分辨率纹理的多视图一致图像，特别是在缺乏3D感知的2D扩散范式中。在这项工作中，我们提出了高分辨率图像到3D模型（Hi3D），这是一种新的基于视频扩散的范式，将单个图像重新定义为多视图图像，作为3D感知的顺序图像生成（即轨道视频生成）。该方法深入研究了视频扩散模型中潜在的时间一致性知识，该模型在3D生成中很好地推广了多个视图之间的几何一致性。从技术上讲，Hi3D首先为预训练的视频扩散模型赋予3D感知先验（相机姿态条件），从而产生具有低分辨率纹理细节的多视图图像。学习3D感知视频到视频细化器，以进一步放大具有高分辨率纹理细节的多视图图像。这种高分辨率的多视图图像通过3D高斯散点进一步增强了新的视图，最终通过3D重建获得高保真网格。对新颖视图合成和单视图重建的广泛实验表明，我们的Hi3D能够产生具有高度详细纹理的卓越多视图一致性图像。源代码和数据可在\url上获得{https://github.com/yanghb22-fdu/Hi3D-Official}. et.al.|[2409.07452](http://arxiv.org/abs/2409.07452)|**[link](https://github.com/yanghb22-fdu/hi3d-official)**|
|**2024-09-11**|**Three-Dimensional, Multimodal Synchrotron Data for Machine Learning Applications**|机器学习技术正越来越多地应用于医学和物理科学中的各种成像方式；然而，开发这些工具时的一个重要问题是高质量培训数据的可用性。在这里，我们展示了一个独特的多峰同步加速器数据集，其中包含一个定制的掺锌沸石13X样品，可用于开发先进的深度学习和数据融合管道。在进行空间分辨X射线衍射计算机断层扫描以表征钠和锌相的均匀分布之前，对掺锌沸石13X碎片进行了多分辨率微X射线计算机断层扫描，以表征其孔隙和特征。控制锌的吸收，以产生一种简单的、空间隔离的两相材料。原始数据和处理后的数据都可以作为一系列Zenodo条目获得。总之，我们提出了一个空间分辨、三维、多模态、多分辨率的数据集，可用于开发机器学习技术。这些技术包括超分辨率、多模态数据融合和3D重建算法的开发。 et.al.|[2409.07322](http://arxiv.org/abs/2409.07322)|null|

<p align=right>(<a href=#updated-on-20240920>back to top</a>)</p>

## Diffusion

|Publish Date|Title|Abstract|PDF|Code|
|---|---|---|---|---|
|**2024-09-18**|**Vista3D: Unravel the 3D Darkside of a Single Image**|我们开始了一项古老的探索：从可见部分的一瞥中揭示物体的隐藏维度。为了解决这个问题，我们提出了Vista3D，这是一个在短短5分钟内实现快速一致的3D生成的框架。Vista3D的核心是一种两阶段方法：粗阶段和细阶段。在粗略阶段，我们使用高斯散斑从单个图像中快速生成初始几何体。在精细阶段，我们直接从学习到的高斯散斑中提取有符号距离函数（SDF），用可微等值面表示对其进行优化。此外，它通过使用具有两个独立隐式函数的解纠缠表示来捕捉对象的可见和模糊方面，从而提高了生成的质量。此外，它通过角扩散先验合成来协调2D扩散先验和3D感知扩散先验的梯度。通过广泛的评估，我们证明Vista3D有效地维持了生成的3D对象的一致性和多样性之间的平衡。演示和代码将在https://github.com/florinshen/Vista3D. et.al.|[2409.12193](http://arxiv.org/abs/2409.12193)|**[link](https://github.com/florinshen/vista3d)**|
|**2024-09-18**|**DynaMo: In-Domain Dynamics Pretraining for Visuo-Motor Control**|模仿学习已被证明是训练复杂视觉运动策略的有力工具。然而，目前的方法通常需要数百到数千名专家演示来处理高维视觉观察。数据效率低下的一个关键原因是，视觉表示主要是对域外数据进行预训练，或者直接通过行为克隆目标进行训练。在这项工作中，我们提出了DynaMo，一种新的领域内自监督学习视觉表示的方法。给定一组专家演示，我们在一系列图像嵌入上共同学习潜在逆动力学模型和正向动力学模型，预测潜在空间中的下一帧，而无需增强、对比采样或获取地面真实动作。重要的是，DynaMo不需要任何域外数据，如互联网数据集或交叉体现数据集。在一组六个模拟和真实环境中，我们发现，与之前的自监督学习目标和预训练表示相比，使用DynaMo学习的表示显著提高了下游的模仿学习性能。使用DynaMo的收益适用于行为转换器、扩散策略、MLP和最近邻等策略类。最后，我们分析了DynaMo的关键组成部分，并衡量了其对下游政策绩效的影响。机器人视频最好在以下位置观看https://dynamo-ssl.github.io et.al.|[2409.12192](http://arxiv.org/abs/2409.12192)|null|
|**2024-09-18**|**Massively Multi-Person 3D Human Motion Forecasting with Scene Context**|预测长期的3D人体运动具有挑战性：人类行为的随机性使得仅从输入序列中生成逼真的人体运动变得困难。关于场景环境和附近人的运动的信息可以极大地帮助生成过程。我们提出了一种场景感知社会变换器模型（SAST）来预测长期（10秒）的人体运动。与之前的模型不同，我们的方法可以对场景中人数差异很大的人和物体之间的交互进行建模。我们将时间卷积编码器-解码器架构与基于Transformer的瓶颈相结合，使我们能够有效地组合运动和场景信息。我们使用去噪扩散模型对条件运动分布进行建模。我们在厨房里的人类数据集上对我们的方法进行了基准测试，该数据集包含1到16个人和29到50个同时可见的对象。在不同指标和用户研究中，我们的模型在真实性和多样性方面优于其他方法。代码可在以下网址获得https://github.com/felixbmuller/SAST. et.al.|[2409.12189](http://arxiv.org/abs/2409.12189)|null|
|**2024-09-18**|**Blind Deconvolution on Graphs: Exact and Stable Recovery**|我们研究了图上的盲解卷积问题，该问题出现在定位网络上扩散的几个源的背景下。虽然观测值是未知图滤波器系数和稀疏输入信号的双线性函数，但对扩散滤波器可逆性的温和要求能够实现有效的凸松弛，从而得到可以用现成求解器解决的线性规划公式。在输入的伯努利-高斯模型下，我们推导出了无噪声环境下足够精确的恢复条件。然后建立稳定的恢复结果，确保即使观测值被少量噪声破坏，估计误差仍然可控。使用合成和真实世界网络数据的数值测试说明了所提出算法的优点、对噪声的鲁棒性以及利用多个信号来帮助（盲）定位扩散源的好处。在基本层面上，本文提出的结果将（空间）时间信号的经典盲解卷积扩展到不规则图域。 et.al.|[2409.12164](http://arxiv.org/abs/2409.12164)|null|
|**2024-09-18**|**MoRAG -- Multi-Fusion Retrieval Augmented Generation for Human Motion**|我们介绍了MoRAG，这是一种新的基于多部分融合的检索增强生成策略，用于基于文本的人体运动生成。该方法通过利用通过改进的运动检索过程获得的额外知识来增强运动扩散模型。通过有效地提示大型语言模型（LLM），我们解决了运动检索中的拼写错误和改写问题。我们的方法利用多部分检索策略来提高跨语言空间的运动检索的泛化能力。我们通过检索到的运动的空间组合来创建不同的样本。此外，通过利用低级、特定于部分的运动信息，我们可以为看不见的文本描述构建运动样本。我们的实验表明，我们的框架可以作为即插即用模块，提高运动扩散模型的性能。代码、预训练模型和示例视频将在以下网址提供：https://motion-rag.github.io/ et.al.|[2409.12140](http://arxiv.org/abs/2409.12140)|null|
|**2024-09-18**|**Brain-Streams: fMRI-to-Image Reconstruction with Multi-modal Guidance**|了解人类如何处理视觉信息是揭示大脑活动潜在机制的关键步骤之一。最近，这种好奇心促使fMRI进行图像重建任务；根据视觉刺激的fMRI数据，它旨在重建相应的视觉刺激。令人惊讶的是，利用潜在扩散模型（LDM）等强大的生成模型，在从视觉数据集中重建高分辨率自然图像等复杂视觉刺激方面显示出了有前景的结果。尽管这些重建具有令人印象深刻的结构保真度，但它们往往缺乏小物体的细节、模糊的形状和语义上的细微差别。因此，除了视觉效果之外，纳入额外的语义知识变得势在必行。鉴于此，我们利用现代LDM如何有效地结合多模态引导（文本引导、视觉引导和图像布局）来生成结构和语义上合理的图像。具体来说，受双流假说的启发，即感知和语义信息在不同的大脑区域进行处理，我们的框架brain streams将来自这些大脑区域的fMRI信号映射到适当的嵌入中。也就是说，通过从语义信息区域提取文本指导和从感知信息区域提取视觉指导，Brain Streams为LDM提供了准确的多模态指导。我们在包含自然图像刺激和fMRI数据的真实fMRI数据集上定量和定性地验证了Brain Streams的重建能力。 et.al.|[2409.12099](http://arxiv.org/abs/2409.12099)|null|
|**2024-09-18**|**Uncovering liquid-substrate fluctuation effects on crystal growth and disordered hyperuniformity of two-dimensional materials**|我们使用与原子长度和扩散时间尺度相关的相场晶体模型研究了二维（2D）晶体在波动表面上的生长。受最近在液体基板上实现大尺寸高质量2D晶体前所未有的快速生长的实验的启发，我们发现了液体表面对微观结构有序性的新影响。我们发现基板波动会产生短程噪声，加速覆盖层的结晶和晶粒生长，超过了独立系统。与液体基质波动的耦合也可以调节局部随机性，导致具有隐藏空间秩序的有趣无序结构，即无序的超均匀性。这些结果揭示了二维晶体在液体表面快速生长的物理机制，并展示了一种合成无序超均匀薄膜结构的新策略。 et.al.|[2409.12090](http://arxiv.org/abs/2409.12090)|null|
|**2024-09-18**|**Denoising diffusion models for high-resolution microscopy image restoration**|显微镜成像的进步使研究人员能够在纳米级水平上可视化结构，从而揭示生物组织的复杂细节。然而，图像噪声、荧光团的光漂白以及生物样本对高光剂量的低耐受性等挑战仍然存在，限制了时间分辨率和实验持续时间。减少激光剂量可以以较低的分辨率和增加的噪声为代价进行更长时间的测量，这阻碍了准确的下游分析。在这里，我们训练了一个去噪扩散概率模型（DDPM），通过在低分辨率信息上调整模型来预测高分辨率图像。此外，DDPM的概率方面允许重复生成图像，这往往会进一步提高信噪比。我们表明，我们的模型在四个高度多样化的数据集上实现了更好或类似于以前性能最好的方法的性能。重要的是，虽然之前的任何方法在某些数据集上都表现出了有竞争力的性能，但不是所有数据集，我们的方法在所有四个数据集中都能始终如一地实现高性能，这表明具有很高的通用性。 et.al.|[2409.12078](http://arxiv.org/abs/2409.12078)|null|
|**2024-09-18**|**LEMON: Localized Editing with Mesh Optimization and Neural Shaders**|在实际使用案例中，多边形网格编辑可能比生成新网格更快，但对用户来说仍然具有挑战性和耗时性。该问题的现有解决方案往往侧重于单一任务，无论是几何还是新颖的视图合成，这通常会导致网格和视图之间的结果脱节。在这项工作中，我们提出了LEMON，这是一种将神经延迟着色与局部网格优化相结合的网格编辑管道。我们的方法首先识别网格中最重要的顶点进行编辑，利用分割模型专注于这些关键区域。给定对象的多视图图像，我们优化神经着色器和多边形网格，同时从每个视图中提取法线贴图和渲染图像。通过使用这些输出作为条件数据，我们使用文本到图像扩散模型编辑输入图像，并在变形网格的同时迭代更新我们的数据集。该过程产生一个多边形网格，根据给定的文本指令进行编辑，保留初始网格的几何特征，同时关注最重要的区域。我们使用DTU数据集评估我们的管道，证明它比当前最先进的方法更快地生成精细编辑的网格。我们在补充材料中包含了我们的代码和其他结果。 et.al.|[2409.12024](http://arxiv.org/abs/2409.12024)|null|
|**2024-09-19**|**On some singularly perturbed elliptic systems modeling partial segregation: uniform Hölder estimates and basic properties of the limits**|我们在一类奇异摄动竞争扩散椭圆系统中证明了统一的H”旧估计，其特殊特征是组分之间的相互作用发生三乘三（三元相互作用）。这些系统与Gross-Pitaevski能量的最小化有关，用于模拟超冷气体和其他多组分液体和气体的三元混合物。 et.al.|[2409.11976](http://arxiv.org/abs/2409.11976)|null|

<p align=right>(<a href=#updated-on-20240920>back to top</a>)</p>

## NeRF

|Publish Date|Title|Abstract|PDF|Code|
|---|---|---|---|---|
|**2024-09-17**|**SplatFields: Neural Gaussian Splats for Sparse 3D and 4D Reconstruction**|从多视图图像中数字化3D静态场景和4D动态事件长期以来一直是计算机视觉和图形学领域的一个挑战。最近，3D高斯散斑（3DGS）已经成为一种实用且可扩展的重建方法，由于其令人印象深刻的重建质量、实时渲染能力以及与广泛使用的可视化工具的兼容性而越来越受欢迎。然而，该方法需要大量的输入视图来实现高质量的场景重建，这引入了一个重大的实际瓶颈。在捕捉动态场景时，这一挑战尤为严峻，因为部署广泛的相机阵列的成本可能高得令人望而却步。在这项工作中，我们发现斑点特征缺乏空间自相关性是导致3DGS技术在稀疏重建环境中性能不佳的因素之一。为了解决这个问题，我们提出了一种优化策略，通过将splat特征建模为相应隐式神经场的输出，有效地正则化splat特征。这导致在各种场景中重建质量的一致提高。我们的方法有效地处理了静态和动态情况，这在不同设置和场景复杂性的广泛测试中得到了证明。 et.al.|[2409.11211](http://arxiv.org/abs/2409.11211)|null|
|**2024-09-17**|**Neural Fields for Adaptive Photoacoustic Computed Tomography**|光声计算机断层扫描（PACT）是一种具有广泛医学应用的非侵入性成像技术。传统的PACT图像重建算法受到组织中声速不均匀（SOS）引起的波前失真的影响，导致图像质量下降。考虑到这些影响可以提高图像质量，但测量SOS分布的实验成本很高。另一种方法是仅使用PA信号对初始压力图像和SOS进行联合重建。现有的关节重建方法存在局限性：计算成本高，无法直接恢复SOS，以及依赖于不准确的简化假设。隐式神经表示或神经场是计算机视觉中的一种新兴技术，用于通过基于坐标的神经网络学习物理场的有效和连续表示。在这项工作中，我们介绍了NF-APACT，这是一种高效的自监督框架，利用神经场来估计SOS，以实现准确和鲁棒的多通道解卷积。我们的方法比现有方法更快、更准确地消除了SOS像差。我们在一个新的数值体模以及实验收集的体模和体内数据上证明了我们的方法的成功。我们的代码和数字幻影可在https://github.com/Lukeli0425/NF-APACT. et.al.|[2409.10876](http://arxiv.org/abs/2409.10876)|**[link](https://github.com/Lukeli0425/NF-APACT)**|
|**2024-09-09**|**Lagrangian Hashing for Compressed Neural Field Representations**|我们提出了拉格朗日散列，这是一种神经场的表示，结合了依赖于欧拉网格（即~InstantNGP）的快速训练NeRF方法的特征，以及使用配备有特征的点作为表示信息的方法（例如3D高斯散点或PointNeRF）。我们通过将基于点的表示合并到InstantNGP表示的分层哈希表的高分辨率层中来实现这一点。由于我们的点具有影响域，我们的表示可以被解释为哈希表中存储的高斯混合。我们提出的损失鼓励我们的高斯人向需要更多代表预算才能充分代表的地区移动。我们的主要发现是，我们的表示允许使用更紧凑的表示来重建信号，而不会影响质量。 et.al.|[2409.05334](http://arxiv.org/abs/2409.05334)|null|
|**2024-09-08**|**Exploring spectropolarimetric inversions using neural fields. Solar chromospheric magnetic field under the weak-field approximation**|全斯托克斯偏振数据集来源于狭缝光谱仪或窄带滤光片图，如今已被常规采集。随着二维光谱偏振仪和允许长时间高质量观测序列的观测技术的出现，数据速率正在增加。在光谱偏振反演中，显然需要通过利用推断物理量的时空相干性来超越传统的逐像素策略。我们探索了神经网络作为时间和空间（也称为神经场）上物理量的连续表示的潜力，用于光谱极化反演。我们已经实现并测试了一个神经场，以在弱场近似（WFA）下执行磁场矢量的推理（也称为物理知情神经网络的方法）。通过使用神经场来描述磁场矢量，我们可以通过假设物理量是坐标的连续函数来在空间和时间域中正则化解。我们研究了Ca II 8542 A谱线的合成和真实观测结果。我们还探讨了其他显式正则化的影响，例如使用外推磁场的信息或色球原纤维的取向。与传统的逐像素反演相比，神经场方法提高了磁场矢量重建的保真度，特别是横向分量。这种隐式正则化是一种提高观测值有效信噪比的方法。虽然它比逐像素WFA估计慢，但这种方法通过减少自由参数的数量并在解决方案中引入时空约束，显示出深度分层反演的巨大潜力。 et.al.|[2409.05156](http://arxiv.org/abs/2409.05156)|null|
|**2024-09-04**|**MDNF: Multi-Diffusion-Nets for Neural Fields on Meshes**|我们提出了一种在三角形网格上表示神经场的新框架，该框架在空间和频率域上都是多分辨率的。受神经傅里叶滤波器组（NFFB）的启发，我们的架构通过将更精细的空间分辨率级别与更高的频带相关联来分解空间和频率域，而将更粗糙的分辨率映射到较低的频率。为了实现几何感知的空间分解，我们利用了多个扩散网络组件，每个组件都与不同的空间分辨率级别相关联。随后，我们应用傅里叶特征映射来鼓励更精细的分辨率水平与更高的频率相关联。最终信号是使用正弦激活的MLP以小波激励的方式组成的，将高频信号聚集在低频信号之上。我们的架构在学习复杂神经场方面具有很高的精度，并且对目标场的不连续性、指数尺度变化和网格修改具有鲁棒性。我们通过将我们的方法应用于不同的神经领域，如合成RGB函数、UV纹理坐标和顶点法线，展示了其有效性，并说明了不同的挑战。为了验证我们的方法，我们将其性能与两种替代方案进行了比较，展示了我们的多分辨率架构的优势。 et.al.|[2409.03034](http://arxiv.org/abs/2409.03034)|null|
|**2024-09-03**|**GraspSplats: Efficient Manipulation with 3D Feature Splatting**|机器人对物体部件进行高效和零样本抓取的能力对于实际应用至关重要，并且随着视觉语言模型（VLM）的最新进展而变得普遍。为了弥合二维到三维表示的差距以支持这种能力，现有的方法依赖于神经场（NeRF），通过可微渲染或基于点的投影方法。然而，我们证明了NeRF由于其隐含性而不适合场景变化，并且基于点的方法对于没有基于渲染的优化的零件定位是不准确的。为了修正这些问题，我们提出了“把握辉煌”。使用深度监督和一种新的参考特征计算方法，GraspSplats在60秒内生成高质量的场景表示。我们进一步验证了基于高斯表示法的优势，表明GraspSplats中的显式和优化几何足以原生支持（1）实时抓取采样和（2）使用点跟踪器进行动态和铰接对象操作。通过在Franka机器人上进行的广泛实验，我们证明了在不同的任务设置下，GraspSplats的表现明显优于现有的方法。特别是，GraspSplats的性能优于基于NeRF的方法，如F3RM和LERF-TOGO，以及2D检测方法。 et.al.|[2409.02084](http://arxiv.org/abs/2409.02084)|null|
|**2024-08-23**|**S4D: Streaming 4D Real-World Reconstruction with Gaussians and 3D Control Points**|最近，使用高斯分布的动态场景重建引起了越来越多的兴趣。主流方法通常采用全局变形场来扭曲规范空间中的3D场景。然而，隐式神经场固有的低频特性往往导致复杂运动的无效表示。此外，它们的结构刚性会阻碍对不同分辨率和持续时间的场景的适应。为了克服这些挑战，我们引入了一种利用离散3D控制点的新方法。该方法对局部射线进行物理建模，并建立一个运动解耦坐标系，该坐标系有效地将传统图形与可学习的流水线相结合，以实现鲁棒且高效的局部6自由度（6-DoF）运动表示。此外，我们还开发了一个广义框架，将我们的控制点与高斯算子结合起来。从初始3D重建开始，我们的工作流程将流式4D真实世界重建分解为四个独立的子模块：3D分割、3D控制点生成、对象运动操纵和残差补偿。我们的实验表明，该方法在Neu3DV和CMU全景数据集上的表现优于现有的最先进的4D高斯散斑技术。我们的方法还显著加速了训练，在单个NVIDIA 4070 GPU上，每帧只需2秒即可优化我们的3D控制点。 et.al.|[2408.13036](http://arxiv.org/abs/2408.13036)|**[link](https://github.com/hebing-sjtu/S4D)**|
|**2024-08-22**|**Neural Fields and Noise-Induced Patterns in Neurons on Large Disordered Networks**|我们研究了随机图上受时空随机强迫的大维神经网络类的模式形成。在耦合和节点动力学的一般条件下，我们证明了该网络具有严格的平均场极限，类似于Wilson Cowan神经场方程。限制系统的状态变量是神经元活动的均值和方差。我们选择平均场方程易于处理的网络，并使用每个神经元上传入白噪声的扩散强度作为控制参数进行分叉分析。我们在皮质被建模为环的系统中找到了图灵分叉的条件，并在二维皮质模型中产生了噪声诱导螺旋波的数值证据。我们提供了数值证据，证明有限尺寸网络的解弱收敛于平均场模型的解。最后，我们证明了大偏差原理，该原理提供了一种评估有限尺寸效应引起的平均场方程偏差可能性的方法。 et.al.|[2408.12540](http://arxiv.org/abs/2408.12540)|null|
|**2024-08-19**|**Neural Representation of Shape-Dependent Laplacian Eigenfunctions**|拉普拉斯算子的特征函数在数学物理、工程和几何处理中至关重要。通常，这些是通过对域进行离散化并执行特征分解来计算的，将结果与特定的网格联系起来。然而，这种方法不适合连续参数化的形状。我们提出了一种连续参数化形状空间中本征函数的新表示，其中本征函数是连续依赖于形状参数的空间场，由最小狄利克雷能量、单位范数和相互正交性定义。我们用训练为神经场的多层感知器来实现这一点，将形状参数和域位置映射到特征函数值。一个独特的挑战是强制因果关系的相互正交性，其中因果顺序在形状空间中是不同的。因此，我们的训练方法需要三个相互交织的概念：（1）通过在单位范数约束下最小化狄利克雷能量来同时学习n$本征函数；（2） 在反向传播过程中过滤梯度以强制因果正交性，防止早期特征函数受到后期特征函数的影响；（3） 基于特征值对因果排序进行动态排序，以跟踪特征值曲线交叉。我们在形状族分析、不完整形状的特征函数预测、交互式形状操作和计算高维特征函数等问题上展示了我们的方法，这些问题都是传统方法所不能达到的。 et.al.|[2408.10099](http://arxiv.org/abs/2408.10099)|null|
|**2024-08-20**|**Scene123: One Prompt to 3D Scene Generation via Video-Assisted and Consistency-Enhanced MAE**|随着人工智能生成内容（AIGC）的进步，已经开发了各种方法来从单模式或多模式输入生成文本、图像、视频和3D对象，从而有助于模拟类人认知内容的创建。然而，由于确保模型生成的外推视图之间的一致性所涉及的复杂性，从单个输入生成逼真的大规模场景是一个挑战。受益于最新的视频生成模型和隐式神经表示，我们提出了Scene123，这是一种3D场景生成模型，它不仅通过视频生成框架确保了真实性和多样性，还使用隐式神经场与掩模自编码器（MAE）相结合，有效地确保了视图中看不见区域的一致性。具体来说，我们最初会扭曲输入图像（或从文本生成的图像）以模拟相邻的视图，用MAE模型填充不可见的区域。然而，这些填充图像通常无法保持视图一致性，因此我们利用产生的视图来优化神经辐射场，增强几何一致性。此外，为了进一步增强生成视图的细节和纹理保真度，我们对通过视频生成模型从输入图像中导出的图像采用了基于GAN的Loss。大量实验表明，我们的方法可以从单个提示中生成逼真一致的场景。定性和定量结果都表明，我们的方法超越了现有的最先进的方法。我们展示鼓励视频示例https://yiyingyang12.github.io/Scene123.github.io/. et.al.|[2408.05477](http://arxiv.org/abs/2408.05477)|null|

<p align=right>(<a href=#updated-on-20240920>back to top</a>)</p>

[contributors-shield]: https://img.shields.io/github/contributors/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[contributors-url]: https://github.com/Vincentqyw/cv-arxiv-daily/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[forks-url]: https://github.com/Vincentqyw/cv-arxiv-daily/network/members
[stars-shield]: https://img.shields.io/github/stars/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[stars-url]: https://github.com/Vincentqyw/cv-arxiv-daily/stargazers
[issues-shield]: https://img.shields.io/github/issues/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[issues-url]: https://github.com/Vincentqyw/cv-arxiv-daily/issues

