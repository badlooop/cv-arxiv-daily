[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]

## Updated on 2024.12.24
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
|**2024-12-23**|**FaceLift: Single Image to 3D Head with View Generation and GS-LRM**|我们介绍FaceLift，这是一种前馈方法，用于从单张图像中快速、高质量、360度重建头部。我们的管道首先采用多视图潜在扩散模型，该模型从单个面部输入生成一致的头部侧视图和后视图。这些生成的视图然后作为GS-LRM重建器的输入，该重建器使用高斯斑点生成全面的3D表示。为了训练我们的系统，我们使用合成的3D人头作为集合开发了一个多视图渲染数据集。基于扩散的多视图生成器仅在合成头部图像上进行训练，而GS-LRM重建器在Objaverse上进行初始训练，然后对合成头部数据进行微调。FaceLift擅长保护身份并保持视图之间的一致性。尽管FaceLift仅基于合成数据进行训练，但它对现实世界的图像表现出了出色的泛化能力。通过广泛的定性和定量评估，我们表明FaceLift在3D头部重建方面优于最先进的方法，突出了其在现实世界图像上的实用性和鲁棒性。除了单图像重建外，FaceLift还支持4D新颖视图合成的视频输入，并与2D复活技术无缝集成，以实现3D面部动画。项目页面：https://weijielyu.github.io/FaceLift. et.al.|[2412.17812](http://arxiv.org/abs/2412.17812)|null|
|**2024-12-23**|**Editing Implicit and Explicit Representations of Radiance Fields: A Survey**|近年来，神经辐射场（NeRF）通过提供一种新的体积表示法彻底改变了新颖的视图合成，这种表示法结构紧凑，可提供高质量的图像渲染。然而，编辑这些辐射场的方法比NeRF其他方面的许多改进发展得慢。随着受NeRF启发的基于辐射场的替代表示的最新发展，以及文本到图像模型在全球范围内的普及，出现了许多新的机会和策略来提供辐射场编辑。在本文中，我们对文献中NeRF和其他类似辐射场表示的不同编辑方法进行了全面的调查。我们提出了一种新的分类法，用于根据编辑方法对现有作品进行分类，回顾了开创性的模型，反思了辐射场编辑的当前和潜在的新应用，并在编辑选项和性能方面比较了最先进的方法。 et.al.|[2412.17628](http://arxiv.org/abs/2412.17628)|null|
|**2024-12-23**|**Exploring Dynamic Novel View Synthesis Technologies for Cinematography**|新视角合成（NVS）在电影制作中的应用显示出巨大的前景，特别是通过利用神经辐射场（NeRF）和高斯散斑（GS）。这些方法对真实的3D场景进行建模，能够创建由于设置拓扑或昂贵的设备要求而在现实世界中难以捕捉的新镜头。这项创新还提供了电影拍摄的优势，如平滑的相机运动、虚拟重新拍摄、慢动作效果等。本文探讨了动态NVS，旨在促进模型选择过程。我们通过使用各种NVS模型拍摄的短蒙太奇展示了它的潜力。 et.al.|[2412.17532](http://arxiv.org/abs/2412.17532)|null|
|**2024-12-22**|**GeoTexDensifier: Geometry-Texture-Aware Densification for High-Quality Photorealistic 3D Gaussian Splatting**|3D高斯散点（3DGS）因其逼真和高效的渲染性能，最近在3D导航、虚拟现实（VR）和3D模拟等各个领域引起了广泛关注。3DGS的高质量重建依赖于足够的斑点和这些斑点的合理分布，以适应真实的几何表面和纹理细节，这是一个具有挑战性的问题。我们提出了GeoTexDensifier，这是一种新的几何纹理感知致密化策略，用于重建高质量的高斯斑点，更好地符合场景的几何结构和纹理丰富性。具体来说，我们的GeoTexDensifier框架执行了一种辅助的纹理感知致密化方法，在完全纹理化的区域产生更密集的斑点分布，同时在低纹理区域保持稀疏性，以保持高斯点云的质量。同时，在深度比变化验证检查下，几何感知分割策略采用深度和法线先验来指导分割采样，并滤除初始位置远离其目标拟合的实际几何表面的噪声斑点。在相对单目深度先验的帮助下，这种几何感知验证可以有效地减少散射高斯对最终渲染质量的影响，特别是在纹理较弱或没有足够训练视图的区域。纹理感知致密化和几何感知分裂策略完全结合在一起，以获得一组高质量的高斯斑点。我们在各种数据集上实验了我们的GeoTexDensifier框架，并将我们的新视图合成结果与其他最先进的3DGS方法进行了比较，并进行了详细的定量和定性评估，以证明我们的方法在生成更逼真的3DGS模型方面的有效性。 et.al.|[2412.16809](http://arxiv.org/abs/2412.16809)|null|
|**2024-12-21**|**Topology-Aware 3D Gaussian Splatting: Leveraging Persistent Homology for Optimized Structural Integrity**|高斯散斑（GS）已成为表示离散体积辐射场的关键技术。它利用独特的参数化来减轻场景优化中的计算需求。这项工作引入了拓扑感知3D高斯散布（Topology GS），它解决了当前方法中的两个关键局限性：由于初始几何覆盖不完整而损害的像素级结构完整性，以及由于优化过程中拓扑约束不足而导致的特征级完整性不足。为了克服这些局限性，拓扑GS引入了一种新的插值策略，即局部持久沃罗诺伊插值（LPVI），以及一个基于持久条形码的拓扑聚焦正则化项，称为PersLoss。LPVI利用持久同源性来指导自适应插值，在保持拓扑结构的同时增强低曲率区域的点覆盖。PersLoss通过约束渲染图像拓扑特征之间的距离，将渲染图像的视觉感知相似性与地面真实性对齐。对三种新型视图合成基准的综合实验表明，拓扑GS在PSNR、SSIM和LPIPS指标方面优于现有方法，同时保持了高效的内存使用。本研究开创了拓扑与3D-GS的集成，为该领域的未来研究奠定了基础。 et.al.|[2412.16619](http://arxiv.org/abs/2412.16619)|**[link](https://github.com/amadeusstq/topology-gs)**|
|**2024-12-20**|**EGSRAL: An Enhanced 3D Gaussian Splatting based Renderer with Automated Labeling for Large-Scale Driving Scene**|3D高斯散点（3D GS）因其更快的渲染速度和高质量的新颖视图合成而广受欢迎。一些研究人员探索了使用3D GS重建驾驶场景。然而，这些方法通常依赖于各种数据类型，如深度图、3D框和运动物体的轨迹。此外，合成图像缺乏注释限制了它们在下游任务中的直接应用。为了解决这些问题，我们提出了EGSRAL，这是一种基于3D GS的方法，仅依赖于训练图像而不需要额外的注释。EGSRAL增强了3D GS对动态对象和静态背景建模的能力，并引入了一种用于自动标记的新型适配器，基于现有注释生成相应的注释。我们还为vanilla 3D GS提出了一种分组策略，以解决渲染大规模复杂场景时的透视问题。我们的方法在多个数据集上实现了最先进的性能，而无需任何额外的注释。例如，在nuScenes数据集上，PSNR度量达到29.04。此外，我们的自动标签可以显著提高2D/3D检测任务的性能。代码可在以下网址获得https://github.com/jiangxb98/EGSRAL. et.al.|[2412.15550](http://arxiv.org/abs/2412.15550)|**[link](https://github.com/jiangxb98/egsral)**|
|**2024-12-19**|**SolidGS: Consolidating Gaussian Surfel Splatting for Sparse-View Surface Reconstruction**|高斯飞溅在新颖的视图合成和多视图图像的表面重建方面都取得了令人印象深刻的改进。然而，目前的方法仍然难以使用高斯飞溅从稀疏的视图输入图像中重建高质量的表面。在本文中，我们提出了一种名为SolidGS的新方法来解决这个问题。我们观察到，由于几何渲染中高斯函数的特性，重建的几何在多个视图之间可能会严重不一致。这促使我们通过采用更坚实的核函数来整合所有高斯函数，从而有效地提高了曲面重建质量。在几何正则化和单目法线估计的额外帮助下，我们的方法在稀疏视图曲面重建方面取得了比广泛使用的DTU、Tanks和Temples以及LLFF数据集上的所有高斯溅射方法和神经场方法更优越的性能。 et.al.|[2412.15400](http://arxiv.org/abs/2412.15400)|null|
|**2024-12-19**|**EnvGS: Modeling View-Dependent Appearance with Environment Gaussian**|从2D图像重建现实世界场景中的复杂反射对于实现逼真的新颖视图合成至关重要。利用环境贴图对远距离照明的反射进行建模的现有方法往往难以处理高频反射细节，并且无法考虑近场反射。在这项工作中，我们介绍了EnvGS，这是一种新的方法，它采用一组高斯基元作为显式的3D表示来捕获环境的反射。这些环境高斯基元与基础高斯基元相结合，以对整个场景的外观进行建模。为了高效地渲染这些环境高斯基元，我们开发了一种基于光线跟踪的渲染器，该渲染器利用GPU的RT内核进行快速渲染。这使我们能够共同优化模型，以实现高质量的重建，同时保持实时渲染速度。来自多个真实世界和合成数据集的结果表明，我们的方法产生了更详细的反射，在实时新颖视图合成中实现了最佳的渲染质量。 et.al.|[2412.15215](http://arxiv.org/abs/2412.15215)|null|
|**2024-12-20**|**GURecon: Learning Detailed 3D Geometric Uncertainties for Neural Surface Reconstruction**|神经表面表示在新颖的视图合成和3D重建领域取得了显著的成功。然而，在没有地面真实网格的情况下评估3D重建的几何质量仍然是一个重大挑战，因为其基于渲染的优化过程以及外观和几何体与光度损失的纠缠学习。本文提出了一种新的框架，即GURecon，它基于几何一致性为神经曲面建立了一个几何不确定性场。与依赖于基于渲染的测量的现有方法不同，GURecon为重建表面建模了一个连续的3D不确定性场，并通过在线蒸馏方法学习，而无需引入真实的几何信息进行监督。此外，为了减轻光照对几何一致性的干扰，学习并利用解耦场来微调不确定性场。在各种数据集上的实验证明了GURecon在建模3D几何不确定性方面的优越性，以及它对各种神经表面表示的即插即用扩展和对增量重建等下游任务的改进。代码和补充材料可在项目网站上获得：https://zju3dv.github.io/GURecon/. et.al.|[2412.14939](http://arxiv.org/abs/2412.14939)|null|
|**2024-12-19**|**Bright-NeRF:Brightening Neural Radiance Field with Color Restoration from Low-light Raw Images**|神经辐射场（NeRF）在新颖的视图合成中表现出了突出的性能。然而，它们的输入在很大程度上依赖于正常光照条件下的图像采集，这使得在低光照环境中学习准确的场景表示变得具有挑战性，因为图像通常会出现明显的噪声和严重的颜色失真。为了应对这些挑战，我们提出了一种新方法Bright NeRF，它以无监督的方式从多视图低光原始图像中学习增强的高质量辐射场。我们的方法同时实现了颜色恢复、去噪和增强的新颖视图合成。具体来说，我们利用了传感器对光照响应的物理启发模型，并引入了色彩适应损失来限制响应的学习，从而使物体的颜色感知保持一致，而不管光照条件如何。我们进一步利用原始数据的属性来自动显示场景的强度。此外，我们还收集了一个多视图低光原始图像数据集，以推进该领域的研究。实验结果表明，我们提出的方法明显优于现有的2D和3D方法。我们的代码和数据集将公开。 et.al.|[2412.14547](http://arxiv.org/abs/2412.14547)|null|

<p align=right>(<a href=#updated-on-20241224>back to top</a>)</p>

## 3D Reconstruction

|Publish Date|Title|Abstract|PDF|Code|
|---|---|---|---|---|
|**2024-12-23**|**Cross-View Referring Multi-Object Tracking**|参考多目标跟踪（RMOT）是当前跟踪领域的一个重要课题。它的任务形式是引导跟踪器跟踪与语言描述匹配的对象。目前的研究主要集中在单视图下的多目标跟踪，指的是一个视图序列或多个不相关的视图序列。然而，在单一视图中，对象的某些外观很容易不可见，导致对象与语言描述的不正确匹配。在这项工作中，我们提出了一个新的任务，称为交叉视图参考多目标跟踪（CRMOT）。它引入了交叉视图来从多个视图中获取对象的外观，避免了RMOT任务中对象外观不可见的问题。CRMOT是一项更具挑战性的任务，即准确跟踪与语言描述匹配的对象，并保持每个交叉视图中对象的身份一致性。为了推进CRMOT任务，我们构建了一个基于CAMPUS和DIVOTrack数据集的交叉视图参考多目标跟踪基准，称为CRTrack。具体来说，它提供了13个不同的场景和221种语言描述。此外，我们提出了一种端到端的交叉视图参考多目标跟踪方法，称为CRTracker。在CRTrack基准上进行的大量实验验证了我们方法的有效性。数据集和代码可在https://github.com/chen-si-jia/CRMOT. et.al.|[2412.17807](http://arxiv.org/abs/2412.17807)|**[link](https://github.com/chen-si-jia/crmot)**|
|**2024-12-21**|**EasyVis2: A Real Time Multi-view 3D Visualization for Laparoscopic Surgery Training Enhanced by a Deep Neural Network YOLOv8-Pose**|EasyVis2是一个专为腹腔镜手术中的免提实时3D可视化而设计的系统。它包含一个配备有一组微型摄像头的手术套管针，这些摄像头插入体腔以提供扩大的视野和手术过程的3D透视图。YOLOv8-Pose是一种复杂的深度神经网络算法，专门用于估计每个单独相机视图中手术器械的位置和方向。随后，使用跨多个视图的相关2D关键点进行3D手术工具姿态估计。这使得能够渲染覆盖在观察到的背景场景上的手术工具的3D表面模型，以实现实时可视化。在这项研究中，我们解释了为新的手术工具开发训练数据集的过程，以定制YoLOv8姿势，同时最大限度地减少标记工作。进行了广泛的实验，将EasyVis2与原始EasyVis进行了比较，结果表明，在相同数量的相机下，新系统提高了3D重建精度并缩短了计算时间。此外，在真实动物组织上进行的3D渲染实验通过显示虚拟侧视图直观地展示了手术工具和组织之间的距离，表明了未来在真实手术中的潜在应用。 et.al.|[2412.16742](http://arxiv.org/abs/2412.16742)|null|
|**2024-12-21**|**LUCES-MV: A Multi-View Dataset for Near-Field Point Light Source Photometric Stereo**|最近，光度立体（PS）领域最大的改进来自于采用可微分体绘制技术，如NeRF或神经SDF，在DiLiGenT MV基准上实现了0.2mm的令人印象深刻的重建误差。然而，虽然有相当大的环境照明对象数据集，如数字孪生目录（DTS），但只有几个小的光度立体数据集，它们往往缺乏具有挑战性的对象（简单、平滑、无纹理）和实用的小形状因子（近场）光设置。为了解决这个问题，我们提出了LUCES-MV，这是第一个为近场点光源光度立体设计的真实世界多视图数据集。我们的数据集包括15个具有不同材料的物体，每个物体都是在不同的光照条件下从距离相机中心30到40厘米的15个LED阵列中成像的。为了促进透明的端到端评估，我们的数据集不仅提供地面真实法线和地面真实对象网格和姿态，还提供灯光和相机校准图像。我们评估了最先进的近场光度立体算法，强调了它们在不同材料和形状复杂性方面的优势和局限性。LUCES-MV数据集为开发更稳健、准确和可扩展的基于光度立体的真实世界3D重建方法提供了重要的基准。 et.al.|[2412.16737](http://arxiv.org/abs/2412.16737)|null|
|**2024-12-21**|**Context-Aware Outlier Rejection for Robust Multi-View 3D Tracking of Similar Small Birds in An Outdoor Aviary**|本文提出了一种使用多摄像机系统对室外鸟舍中的多只鸟类进行鲁棒3D跟踪的新方法。我们的方法通过利用环境地标进行增强的特征匹配和3D重建，解决了视觉上相似的鸟类及其快速运动的挑战。在我们的方法中，异常值根据其最近的地标被拒绝。这使得精确的3D建模和同时跟踪多只鸟成为可能。通过利用环境背景，我们的方法显著提高了视觉上相似的鸟类之间的区分，这是现有跟踪系统中的一个关键障碍。实验结果证明了我们的方法的有效性，在3D重建过程中消除了20%的异常值，匹配精度为97%。3D建模的这种非凡精度转化为对多只鸟类的稳健可靠跟踪，即使在具有挑战性的室外条件下也是如此。我们的工作不仅推进了计算机视觉领域的发展，而且为研究自然环境中的鸟类行为和运动模式提供了宝贵的工具。我们还提供了一个大型的带注释的数据集，包含80只栖息在四个围栏中的鸟类，持续20小时，为计算机视觉、鸟类学家和生态学家的研究人员提供了丰富的试验平台。代码和数据集链接可在https://github.com/airou-lab/3D_Multi_Bird_Tracking et.al.|[2412.16511](http://arxiv.org/abs/2412.16511)|**[link](https://github.com/airou-lab/3d_multi_bird_tracking)**|
|**2024-12-19**|**Generative Multiview Relighting for 3D Reconstruction under Extreme Illumination Variation**|从不同环境中拍摄的照片中重建物体的几何形状和外观是困难的，因为照明和物体外观在捕获的图像中会有所不同。对于外观强烈依赖于观察方向的镜面反射物体来说，这尤其具有挑战性。一些先前的方法使用每图像嵌入向量来模拟图像之间的外观变化，而另一些方法则使用基于物理的渲染来恢复材质和每图像照明。考虑到输入光照的显著变化，这种方法无法忠实地恢复与视图相关的外观，并且往往会产生大部分漫反射结果。我们提出了一种从不同照明下拍摄的图像重建对象的方法，该方法首先使用多视图重新照明扩散模型在单个参考照明下重新照明图像，然后使用对重新照明图像之间剩余的小不一致性具有鲁棒性的辐射场架构重建对象的几何形状和外观。我们在合成和真实数据集上验证了我们提出的方法，并证明它在从极端光照变化下拍摄的图像重建高保真外观方面大大优于现有技术。此外，我们的方法在恢复视图相关的“闪亮”外观方面特别有效，这些外观无法通过现有方法重建。 et.al.|[2412.15211](http://arxiv.org/abs/2412.15211)|null|
|**2024-12-20**|**GURecon: Learning Detailed 3D Geometric Uncertainties for Neural Surface Reconstruction**|神经表面表示在新颖的视图合成和3D重建领域取得了显著的成功。然而，在没有地面真实网格的情况下评估3D重建的几何质量仍然是一个重大挑战，因为其基于渲染的优化过程以及外观和几何体与光度损失的纠缠学习。本文提出了一种新的框架，即GURecon，它基于几何一致性为神经曲面建立了一个几何不确定性场。与依赖于基于渲染的测量的现有方法不同，GURecon为重建表面建模了一个连续的3D不确定性场，并通过在线蒸馏方法学习，而无需引入真实的几何信息进行监督。此外，为了减轻光照对几何一致性的干扰，学习并利用解耦场来微调不确定性场。在各种数据集上的实验证明了GURecon在建模3D几何不确定性方面的优越性，以及它对各种神经表面表示的即插即用扩展和对增量重建等下游任务的改进。代码和补充材料可在项目网站上获得：https://zju3dv.github.io/GURecon/. et.al.|[2412.14939](http://arxiv.org/abs/2412.14939)|null|
|**2024-12-19**|**Diffusion priors for Bayesian 3D reconstruction from incomplete measurements**|许多逆问题都是不适定的，需要用限制可容许模型类别的先验信息来补充。贝叶斯方法将这些信息编码为先验分布，这些先验分布对模型施加了稀疏性、非负性或平滑性等通用属性。然而，在图像、图形或三维（3D）对象等复杂结构模型的情况下，通用先验分布倾向于支持与现实世界中观察到的模型有很大不同的模型。在这里，我们探索使用扩散模型作为先验，并在贝叶斯框架内与实验数据相结合。我们使用3D点云来表示3D对象，如家居用品或由蛋白质和核酸形成的生物分子复合物。我们训练扩散模型，以中等分辨率生成粗粒度的3D结构，并将其与不完整和有噪声的实验数据相结合。为了证明我们方法的力量，我们专注于从低温电子显微镜（cryo-EM）图像重建生物分子组件，这是结构生物学中一个重要的逆问题。我们发现，使用扩散模型先验的后验采样可以从非常稀疏、低分辨率和部分观测中进行3D重建。 et.al.|[2412.14897](http://arxiv.org/abs/2412.14897)|null|
|**2024-12-19**|**GSRender: Deduplicated Occupancy Prediction via Weakly Supervised 3D Gaussian Splatting**|3D占用感知因其能够提供详细和精确的环境表示而越来越受到关注。以前的弱监督NeRF方法平衡了效率和准确性，由于沿相机光线的采样计数，mIoU变化了5-10个点。最近，实时高斯飞溅在3D重建中得到了广泛的应用，占用预测任务也可以被视为重建任务。因此，我们提出了GSRender，它自然地采用3D高斯散点进行占用预测，简化了采样过程。此外，2D监控的局限性导致沿同一相机光线的重复预测。我们实现了光线补偿（RC）模块，该模块通过补偿相邻帧的特征来缓解这个问题。最后，我们重新设计了损失，以消除相邻帧中动态对象的影响。大量实验表明，我们的方法在RayIoU（+6.0）中实现了SOTA（最先进）结果，同时缩小了与3D监控方法的差距。我们的代码很快就会发布。 et.al.|[2412.14579](http://arxiv.org/abs/2412.14579)|null|
|**2024-12-19**|**Improving Geometry in Sparse-View 3DGS via Reprojection-based DoF Separation**|最近基于学习的多视图立体模型在稀疏视图3D重建中表现出了最先进的性能。然而，直接应用3D高斯散斑（3DGS）作为这些模型之后的改进步骤带来了挑战。我们假设高斯分布中过大的位置自由度（DoFs）会导致几何失真，以牺牲结构保真度为代价来拟合颜色图案。为了解决这个问题，我们提出了基于重投影的DoF分离，这是一种根据不确定性区分位置DoF的方法：图像平面平行DoF和光线对齐DoF。为了独立管理每个DoF，我们引入了一个重新投影过程以及为每个DoF量身定制的约束。通过在各种数据集上的实验，我们证实，分离高斯分布的位置DoF并应用有针对性的约束可以有效地抑制几何伪影，从而产生视觉和几何上都合理的重建结果。 et.al.|[2412.14568](http://arxiv.org/abs/2412.14568)|null|
|**2024-12-19**|**GenHMR: Generative Human Mesh Recovery**|人类网格恢复（HMR）在许多计算机视觉应用中至关重要；从健康到艺术和娱乐。单眼图像的HMR主要通过确定性方法来解决，这些方法为给定的2D图像输出单个预测。然而，由于深度模糊和遮挡，单张图像的HMR是一个不适定问题。概率方法试图通过生成和融合多个合理的3D重建来解决这个问题，但它们的性能往往落后于确定性方法。在本文中，我们介绍了GenHMR，这是一种新的生成框架，它将单眼HMR重新表述为图像条件生成任务，显式地建模和减轻2D到3D映射过程中的不确定性。GenHMR包括两个关键组件：（1）姿势标记器，用于将3D人体姿势转换为潜在空间中的离散标记序列，以及（2）图像条件掩码转换器，用于学习姿势标记的概率分布，以输入图像提示和随机掩码标记序列为条件。在推理过程中，模型从学习到的条件分布中采样，以迭代解码高置信度姿态令牌，从而减少3D重建的不确定性。为了进一步细化重建，提出了一种2D姿态引导细化技术，直接微调潜在空间中的解码姿态标记，这迫使投影的3D身体网格与2D姿态线索对齐。在基准数据集上的实验表明，GenHMR明显优于最先进的方法。项目网站可以在https://m-usamasaleem.github.io/publication/GenHMR/GenHMR.html et.al.|[2412.14444](http://arxiv.org/abs/2412.14444)|null|

<p align=right>(<a href=#updated-on-20241224>back to top</a>)</p>

## Diffusion

|Publish Date|Title|Abstract|PDF|Code|
|---|---|---|---|---|
|**2024-12-23**|**FaceLift: Single Image to 3D Head with View Generation and GS-LRM**|我们介绍FaceLift，这是一种前馈方法，用于从单张图像中快速、高质量、360度重建头部。我们的管道首先采用多视图潜在扩散模型，该模型从单个面部输入生成一致的头部侧视图和后视图。这些生成的视图然后作为GS-LRM重建器的输入，该重建器使用高斯斑点生成全面的3D表示。为了训练我们的系统，我们使用合成的3D人头作为集合开发了一个多视图渲染数据集。基于扩散的多视图生成器仅在合成头部图像上进行训练，而GS-LRM重建器在Objaverse上进行初始训练，然后对合成头部数据进行微调。FaceLift擅长保护身份并保持视图之间的一致性。尽管FaceLift仅基于合成数据进行训练，但它对现实世界的图像表现出了出色的泛化能力。通过广泛的定性和定量评估，我们表明FaceLift在3D头部重建方面优于最先进的方法，突出了其在现实世界图像上的实用性和鲁棒性。除了单图像重建外，FaceLift还支持4D新颖视图合成的视频输入，并与2D复活技术无缝集成，以实现3D面部动画。项目页面：https://weijielyu.github.io/FaceLift. et.al.|[2412.17812](http://arxiv.org/abs/2412.17812)|null|
|**2024-12-23**|**Dora: Sampling and Benchmarking for 3D Shape Variational Auto-Encoders**|最近的3D内容生成管道通常采用变分自编码器（VAE）将形状编码为紧凑的潜在表示，用于基于扩散的生成。然而，在Shape VAE训练中广泛采用的均匀点采样策略往往会导致几何细节的显著损失，限制了形状重建和下游生成任务的质量。我们提出了Dora-VAE，这是一种通过我们提出的锐边采样策略和双交叉注意力机制来增强VAE重建的新方法。通过在训练过程中识别和优先排序具有高几何复杂性的区域，我们的方法显著提高了细粒度形状特征的保留率。这种采样策略和双注意力机制使VAE能够专注于均匀采样方法通常会遗漏的关键几何细节。为了系统地评估VAE重建质量，我们还提出了Dora bench，这是一个通过锐边密度量化形状复杂性的基准，引入了一个新的度量标准，专注于这些显著几何特征的重建精度。在Dora工作台上进行的大量实验表明，Dora VAE的重建质量与最先进的密集XCube VAE相当，同时需要至少小8 $\times$ 的潜在空间（1280对>10000个代码）。我们将发布我们的代码和基准数据集，以促进未来3D形状建模的研究。 et.al.|[2412.17808](http://arxiv.org/abs/2412.17808)|null|
|**2024-12-23**|**Encoding off-shell effects in top pair production in Direct Diffusion networks**|为了达到即将到来的大型强子对撞机在模拟顶级对产生事件时的精确目标，还必须考虑壳外效应。由于它们的计算成本很高，我建议将它们编码在神经网络中。为此，我使用了神经网络的组合，这些神经网络将具有近似壳外效应的事件转换为与完全壳外计算获得的事件相匹配的事件。这被证明在领先顺序下可靠有效地工作。在这里，我讨论了扩展此方法以包括高阶效应的第一步。 et.al.|[2412.17783](http://arxiv.org/abs/2412.17783)|null|
|**2024-12-23**|**PepTune: De Novo Generation of Therapeutic Peptides with Multi-Objective-Guided Discrete Diffusion**|肽疗法是一类主要药物，在糖尿病和癌症等疾病中取得了显著成功，GLP-1受体激动剂等里程碑式的例子彻底改变了2型糖尿病和肥胖症的治疗。尽管取得了成功，但设计满足多种相互冲突的目标的肽，如靶结合亲和力、溶解度和膜通透性，仍然是一个重大挑战。经典的药物开发和基于结构的设计对于此类任务无效，因为它们未能优化对治疗效果至关重要的全局功能特性。现有的生成框架在很大程度上局限于连续空间、无条件输出或单目标指导，使其不适合跨多个属性的离散序列优化。为了解决这个问题，我们提出了PepTune，这是一个多目标离散扩散模型，用于同时生成和优化治疗肽SMILES。PepTune基于掩蔽离散语言模型（MDLM）框架构建，通过状态依赖的掩蔽时间表和基于惩罚的目标确保有效的肽结构。为了指导扩散过程，我们提出了一种基于蒙特卡洛树搜索（MCTS）的策略，该策略平衡了探索和开发，以迭代优化帕累托最优序列。MCTS将基于分类器的奖励与搜索树扩展相结合，克服了梯度估计的挑战和离散空间固有的数据稀疏性。使用PepTune，我们产生了多种化学修饰的肽，这些肽针对多种治疗特性进行了优化，包括靶结合亲和力、膜渗透性、溶解度、溶血性和各种疾病相关靶点的非污染特性。总的来说，我们的结果表明，MCTS引导的离散扩散是离散状态空间中多目标序列设计的一种强大的模块化方法。 et.al.|[2412.17780](http://arxiv.org/abs/2412.17780)|null|
|**2024-12-23**|**Thermal Quench Dynamics of Visons in Gapless Kitaev Spin Liquid**|热淬灭下Kitaev蜂窝模型的弛豫动力学主要由视觉的准随机扩散和成对湮灭所主导，这是一种紧急的间隙通量激发{Z}_2基塔耶夫自旋液体的 $gauge场。扩散能垒以及粘子之间的有效相互作用都是由马约拉纳费米子介导的，马约拉纳费米子是自旋液体的分数准粒子。通过广泛的动力学蒙特卡罗模拟，我们表明热扩散和非局部多视觉相互作用之间的相互作用导致了各种温度相关的动力学行为，从扩散受限和末端速度受限的湮灭到动力学阻止和冻结。值得注意的是，我们发现冻结现象与亚稳态$\sqrt{3}\times\sqrt{3}$vison晶体的形成以及与断裂的$\mathbb相关的超团簇的隐藏粗化密切相关{Z}_3$ 对称。 et.al.|[2412.17774](http://arxiv.org/abs/2412.17774)|null|
|**2024-12-23**|**The Superposition of Diffusion Models Using the Itô Density Estimator**|寒武纪时期易于访问的预训练扩散模型的激增表明，需要一种方法来组合多个不同的预训练的扩散模型，而不会产生重新训练更大的组合模型的巨大计算负担。在本文中，我们提出了一种称为叠加的新框架，在生成阶段组合多个预训练扩散模型的问题。从理论上讲，我们从著名的连续性方程的严格第一性原理中推导出叠加，并设计了两种专为结合SuperDiff中的扩散模型而量身定制的新算法。SuperDiff利用了一种新的可扩展Ito密度估计器来计算扩散SDE的对数似然性，与著名的Hutchinson估计器相比，它不会产生额外的开销。我们证明，SuperDiff可扩展到大型预训练的扩散模型，因为叠加仅通过推理过程中的合成来执行，并且由于它通过自动重新加权方案组合不同的预训练向量场，因此也可以轻松实现。值得注意的是，我们证明了SuperDiff在推理时间内是有效的，并且模仿了传统的组合运算符，如逻辑OR和逻辑and。我们实证证明了使用SuperDiff在CIFAR-10上生成更多样化图像的实用性，使用稳定扩散进行更忠实的快速条件图像编辑，以及改进蛋白质的无条件从头结构设计。https://github.com/necludov/super-diffusion et.al.|[2412.17762](http://arxiv.org/abs/2412.17762)|null|
|**2024-12-23**|**Comprehensive Optimization of Interferometric Diffusing Wave Spectroscopy (iDWS)**|研究表明，光斑波动为无创测量脑血流指数（CBFi）提供了一种方法。虽然传统的扩散相关光谱（DCS）为成年人的CBFi提供了边际的大脑敏感性，但最近出现了新的技术来提高漫射光通量，从而提高大脑敏感性。在这里，我们在独立通道数量、相机占空比和全井容量、入射功率、噪声和伪影抑制以及数据处理方面进一步优化了一种这样的方法，即干涉扩散波光谱法（iDWS）。我们在推车上构建系统，并定义稳定运行的条件。我们显示了中度色素沉着成年人在4-4.5cm源收集器间距处的脉冲CBFi监测（Fitzpatrick 4）。我们还报告了神经重症监护室（神经ICU）的初步临床测量结果。这些结果突破了iDWS CBFi监测性能的界限，超越了之前的报告。 et.al.|[2412.17724](http://arxiv.org/abs/2412.17724)|null|
|**2024-12-23**|**The Cosmological Population of Gamma-Ray Bursts from the Disks of Active Galactic Nuclei**|随着引力波（GW）的发现，活动星系核（AGN）的圆盘已经成为一个有趣的环境，可以容纳一小部分引力波源。AGN盘有利于形成长和短伽马射线暴（GRBs），它们在这些盘中的预期宇宙学发生有可能成为探测和校准其中恒星和致密天体数量及其对GW探测数量的贡献的独立工具。在这项研究中，我们采用蒙特卡洛方法结合极端密集介质中伽马射线暴电磁发射模型，模拟AGN盘中长伽马射线暴和短伽马射线暴的宇宙学发生，同时估计它们在从伽马射线到射频的一系列波长范围内的可检测性。{我们研究了两种极端情况：“未扩散”，即辐射在没有明显散射的情况下逃逸（即如果祖细胞在圆盘内挖掘了一个漏斗），以及“扩散”，其中辐射通过高密度介质传播，可能被散射和吸收。{在扩散的情况下，}我们发现大多数可检测的伽马射线暴可能来自相对较低的红移，以及大型超大质量黑洞（SMBH）质量的最外层区域，即10^{7.5}\rm M_{odot}$。在未扩散的情况下，我们预计会有类似的趋势，但SMBH质量较低的中间区域会做出相当大的贡献。如果扩散不占主导地位，则可检测的发射通常在瞬发γ射线中占主导地位；如果扩散很重要，则X射线余辉占主导地位；然而，主要可观测信号的性质在很大程度上取决于特定的AGN盘模型，因此AGN盘中的GRB也是盘本身结构的潜在探针。 et.al.|[2412.17714](http://arxiv.org/abs/2412.17714)|null|
|**2024-12-23**|**Euclid: Early Release Observations of diffuse stellar structures and globular clusters as probes of the mass assembly of galaxies in the Dorado group**|深入调查揭示了潮汐碎片和相关的致密恒星系统。欧几里得独特的能力组合（空间分辨率、深度和广阔的天空覆盖范围）将使其成为当地宇宙银河考古的突破性工具，将低表面亮度（LSB）科学带入大规模天文调查时代。欧几里得的早期释放观测（ERO）通过包括多拉多星系群中的几个星系的视野证明了这一潜力。在这篇论文中，我们的目标是从这张图像中得出其主要星系的质量组装场景：NGC 1549、NGC 1553和NGC 1546。我们检测内部和外部漫射结构，并识别候选球状星团（GC）。通过分析漫射结构和候选GC的颜色和分布，我们可以对星系的质量组装和合并历史施加约束。结果表明，特征形态、表面亮度、颜色和GC密度分布与经历过不同合并场景的星系一致。我们将NGC 1549归类为一个经历了重大合并的纯椭圆星系。NGC 1553似乎在经历了一系列径向的小星系到中间星系的合并后，最近从晚期星系转变为早期星系。NGC 1546是一个罕见的星系样本，它有一个未受干扰的圆盘和一个突出的弥漫恒星晕，我们推断这是由小合并造成的，然后受到NGC 1553潮汐效应的干扰。最后，我们确定了该ERO观测条件的局限性，特别是可见光中的杂散光和近红外波段的持久性。一旦这些问题得到解决，并且数据处理管道保留了LSB天体的扩展发射，欧几里德广域巡天将允许对当地宇宙的研究扩展到银河系外大部分天空的统计系综。 et.al.|[2412.17672](http://arxiv.org/abs/2412.17672)|null|
|**2024-12-23**|**A Bias-Free Training Paradigm for More General AI-generated Image Detection**|成功的法医检测器可以在监督学习基准测试中产生出色的结果，但很难转移到现实世界的应用中。我们认为，这种限制主要是由于训练数据质量不足。虽然大多数研究都集中在开发新算法上，但对训练数据选择的关注较少，尽管有证据表明，内容、格式或分辨率等虚假相关性会对性能产生强烈影响。一个设计良好的取证检测器应该检测特定于生成器的伪影，而不是反映数据偏差。为此，我们提出了B-Free，这是一种无偏见的训练范式，其中使用稳定扩散模型的条件化过程从真实图像生成虚假图像。这确保了真实图像和虚假图像之间的语义对齐，允许任何差异完全源于人工智能生成引入的微妙伪影。通过基于内容的增强，我们在泛化能力和鲁棒性方面比最先进的检测器有了显著提高，并在27个不同的生成模型（包括FLUX和Stable Diffusion 3.5等最新版本）中获得了更校准的结果。我们的研究结果强调了仔细管理数据集的重要性，强调了进一步研究数据集设计的必要性。代码和数据将在以下网址公开：https://grip-unina.github.io/B-Free/ et.al.|[2412.17671](http://arxiv.org/abs/2412.17671)|null|

<p align=right>(<a href=#updated-on-20241224>back to top</a>)</p>

## NeRF

|Publish Date|Title|Abstract|PDF|Code|
|---|---|---|---|---|
|**2024-12-23**|**S-INF: Towards Realistic Indoor Scene Synthesis via Scene Implicit Neural Field**|基于学习的方法在3D室内场景合成（ISS）中越来越受欢迎，显示出优于传统基于优化的方法的性能。这些基于学习的方法通常使用生成模型在简单但明确的场景表示上对分布进行建模。然而，由于过于简单的显式表示忽略了详细信息，并且缺乏场景内多模态关系的指导，大多数基于学习的方法都难以生成具有逼真对象排列和风格的室内场景。本文介绍了一种新的室内场景合成方法——场景隐式神经场（S-INF），旨在学习多模态关系的有意义表示，以提高室内场景合成的真实感。S-INF假设场景布局通常与对象详细信息有关。它将多模态关系分解为场景布局关系和详细对象关系，然后通过隐式神经场（INF）将它们融合在一起。通过学习专门的场景布局关系并将其投影到S-INF中，我们实现了场景布局的真实生成。此外，S-INF通过可微分渲染捕获密集而详细的对象关系，确保对象之间的风格一致性。通过在基准3D-FRONT数据集上的广泛实验，我们证明了我们的方法在不同类型的ISS下始终达到最先进的性能。 et.al.|[2412.17561](http://arxiv.org/abs/2412.17561)|**[link](https://github.com/zixiliang/s-inf)**|
|**2024-12-22**|**HyperNet Fields: Efficiently Training Hypernetworks without Ground Truth by Learning Weight Trajectories**|为了有效地适应大型模型或训练神经表示的生成模型，超网络引起了人们的兴趣。虽然超级网络工作良好，但训练它们很麻烦，而且通常需要为每个样本进行地面实况优化的权重。然而，获得这些权重中的每一个都是一个需要训练的训练问题，例如，适应权重，甚至是超网络回归的整个神经场。在这项工作中，我们提出了一种训练超网络的方法，而不需要任何每个样本的地面真实值。我们的关键思想是学习一个超网络“场”，并估计网络权重训练的整个轨迹，而不是简单地估计其收敛状态。换句话说，我们向超网络引入了一个额外的输入，即收敛状态，这使它成为一个神经场，对任务网络的整个收敛路径进行建模。这样做的一个关键好处是，在任何收敛状态下，估计权重的梯度都必须与原始任务的梯度相匹配——仅此约束就足以训练超网络场。我们通过个性化图像生成和从图像和点云进行3D形状重建的任务来证明我们的方法的有效性，在没有任何样本地面真实性的情况下展示了具有竞争力的结果。 et.al.|[2412.17040](http://arxiv.org/abs/2412.17040)|null|
|**2024-12-20**|**CCNDF: Curvature Constrained Neural Distance Fields from 3D LiDAR Sequences**|神经距离场（NDF）已成为解决3D计算机视觉和图形下游问题的有力工具。虽然在从各种传感器数据中学习NDF方面取得了重大进展，但需要注意的一个关键方面是在训练过程中对神经场的监督，因为地面真实NDF不适用于大规模户外场景。以往的工作利用各种形式的预期符号距离来指导模型学习。然而，这些方法通常需要更多地关注表面几何形状的关键考虑因素，并且仅限于小规模实施。为此，我们提出了一种利用带符号距离场的二阶导数来改进神经场学习的新方法。我们的方法通过准确估计符号距离来解决局限性，从而更全面地了解底层几何。为了评估我们的方法的有效性，我们对NDF的主要应用领域——测绘和定位任务的流行方法进行了比较评估。我们的结果证明了所提出方法的优越性，突出了其在计算机视觉和图形应用中提高神经距离场能力的潜力。 et.al.|[2412.15909](http://arxiv.org/abs/2412.15909)|null|
|**2024-12-19**|**SolidGS: Consolidating Gaussian Surfel Splatting for Sparse-View Surface Reconstruction**|高斯飞溅在新颖的视图合成和多视图图像的表面重建方面都取得了令人印象深刻的改进。然而，目前的方法仍然难以使用高斯飞溅从稀疏的视图输入图像中重建高质量的表面。在本文中，我们提出了一种名为SolidGS的新方法来解决这个问题。我们观察到，由于几何渲染中高斯函数的特性，重建的几何在多个视图之间可能会严重不一致。这促使我们通过采用更坚实的核函数来整合所有高斯函数，从而有效地提高了曲面重建质量。在几何正则化和单目法线估计的额外帮助下，我们的方法在稀疏视图曲面重建方面取得了比广泛使用的DTU、Tanks和Temples以及LLFF数据集上的所有高斯溅射方法和神经场方法更优越的性能。 et.al.|[2412.15400](http://arxiv.org/abs/2412.15400)|null|
|**2024-12-19**|**LiftRefine: Progressively Refined View Synthesis from 3D Lifting with Volume-Triplane Representations**|我们提出了一种新的视图合成方法，通过从单个或少数视图输入图像合成3D神经场。为了解决图像到3D生成问题的不适定性质，我们设计了一种两阶段方法，该方法涉及重建模型和用于视图合成的扩散模型。我们的重建模型首先将一个或多个输入图像从体积提升到3D空间，作为粗尺度3D表示，然后是三平面作为细尺度3D表示。为了减轻遮挡区域的模糊性，我们的扩散模型会在三个平面的渲染图像中产生缺失细节的幻觉。然后，我们引入了一种新的渐进式细化技术，该技术迭代地应用重建和扩散模型来逐步合成新的视图，提高了3D表示及其渲染的整体质量。实证评估表明，我们的方法在合成SRN-Car数据集、野外CO3D数据集和大规模Objaverse数据集上优于最先进的方法，同时实现了采样效率和多视图一致性。 et.al.|[2412.14464](http://arxiv.org/abs/2412.14464)|null|
|**2024-12-18**|**Level-Set Parameters: Novel Representation for 3D Shape Analysis**|3D形状分析主要集中在点云和网格的传统3D表示上，但这些数据的离散性使得分析容易受到输入分辨率变化的影响。神经场的最新发展从带符号距离函数中引入了水平集参数，作为3D形状的新颖、连续和数值表示，其中形状表面被定义为这些函数的零水平集。这促使我们将形状分析从传统的3D数据扩展到这些新的参数数据。由于水平集参数不是类似欧几里德的点云，我们通过将它们表示为伪正态分布来建立不同形状之间的相关性，并从相应的数据集中预先学习分布。为了进一步探索具有形状变换的水平集参数，我们建议将这些参数的子集设置在旋转和平移上，并使用超网络生成它们。与使用传统数据相比，这简化了与姿势相关的形状分析。我们通过在形状分类（任意姿态）、检索和6D对象姿态估计中的应用，展示了新表示法的前景。本研究中的代码和数据见https://github.com/EnyaHermite/LevelSetParamData. et.al.|[2412.13502](http://arxiv.org/abs/2412.13502)|null|
|**2024-12-13**|**Neural Vector Tomography for Reconstructing a Magnetization Vector Field**|矢量断层重建的离散化技术容易在重建中产生伪影。随着噪声量的增加，这些重建的质量可能会进一步恶化。在这项工作中，我们使用平滑神经场对底层向量场进行建模。由于神经网络中的激活函数可以被选择为平滑的，并且域不再像素化，因此即使在存在噪声的情况下，该模型也能得到高质量的重建。在我们具有潜在的全局连续对称性的情况下，我们发现神经网络比现有技术大大提高了重建的准确性。 et.al.|[2412.09927](http://arxiv.org/abs/2412.09927)|null|
|**2024-12-12**|**PBR-NeRF: Inverse Rendering with Physics-Based Neural Fields**|我们使用基于物理的渲染（PBR）理论的神经辐射场（NeRF）方法来解决3D重建中的不适定逆渲染问题，称为PBR-NeRF。我们的方法解决了大多数NeRF和3D高斯散斑方法的一个关键局限性：它们在不建模场景材质和照明的情况下估计与视图相关的外观。为了解决这一局限性，我们提出了一种能够联合估计场景几何形状、材质和照明的逆渲染（IR）模型。我们的模型建立在最近基于NeRF的IR方法的基础上，但关键是引入了两种新的基于物理的先验，更好地约束了IR估计。我们的先验被严格地表述为直观的损失项，在不影响新颖视图合成质量的情况下实现了最先进的材料估计。我们的方法很容易适应其他需要材料估计的逆渲染和3D重建框架。我们展示了将当前的神经渲染方法扩展到完全建模场景属性的重要性，而不仅仅是几何和视图相关的外观。代码可在以下网址公开获取https://github.com/s3anwu/pbrnerf et.al.|[2412.09680](http://arxiv.org/abs/2412.09680)|**[link](https://github.com/s3anwu/pbrnerf)**|
|**2024-12-12**|**Mixture of neural fields for heterogeneous reconstruction in cryo-EM**|低温电子显微镜（Cryo-EM）是一种用于蛋白质结构测定的实验技术，可以在接近生理环境的情况下对大分子的集合进行成像。虽然最近的进展能够重建单个生物分子复合物的动态构象，但目前的方法并不能充分模拟具有混合构象和成分异质性的样品。特别是，包含多种蛋白质混合物的数据集需要联合推断结构、姿势、组成类别和构象状态以进行3D重建。在这里，我们提出了Hydra，这是一种通过参数化K个神经场之一产生的结构来完全从头计算模拟构象和组成异质性的方法。我们采用了一种新的基于似然的损失函数，并证明了我们的方法在由具有高度构象变异的蛋白质混合物组成的合成数据集上的有效性。我们还在含有不同蛋白质复合物混合物的细胞裂解物的实验数据集上演示了Hydra。Hydra扩展了非均匀重建方法的表现力，从而将冷冻EM的范围扩大到越来越复杂的样本。 et.al.|[2412.09420](http://arxiv.org/abs/2412.09420)|null|
|**2024-12-11**|**From MLP to NeoMLP: Leveraging Self-Attention for Neural Fields**|神经场（NeFs）最近已成为编码各种模态时空信号的最先进方法。尽管NeFs在重建单个信号方面取得了成功，但它们作为下游任务（如分类或分割）中的表示，除了缺乏强大和可扩展的调节机制外，还受到参数空间及其潜在对称性的复杂性的阻碍。在这项工作中，我们从连接主义的原则中汲取灵感，设计了一种基于MLP的新架构，我们称之为NeoMLP。我们从一个被视为图的MLP开始，将其从一个多部分图转换为一个包含输入、隐藏和输出节点的完整图，并配备了高维特征。我们在此图上执行消息传递，并在所有节点之间通过自我关注进行权重共享。NeoMLP具有通过隐藏和输出节点进行调节的内置机制，这些节点充当一组潜在代码，因此，NeoMLP可以直接用作条件神经场。我们通过拟合高分辨率信号（包括多模态视听数据）来证明我们的方法的有效性。此外，我们通过使用单个骨干架构学习特定于实例的潜在代码集来拟合神经表示的数据集，然后将它们用于下游任务，优于最近最先进的方法。源代码开源于https://github.com/mkofinas/neomlp. et.al.|[2412.08731](http://arxiv.org/abs/2412.08731)|**[link](https://github.com/mkofinas/neomlp)**|

<p align=right>(<a href=#updated-on-20241224>back to top</a>)</p>

[contributors-shield]: https://img.shields.io/github/contributors/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[contributors-url]: https://github.com/Vincentqyw/cv-arxiv-daily/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[forks-url]: https://github.com/Vincentqyw/cv-arxiv-daily/network/members
[stars-shield]: https://img.shields.io/github/stars/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[stars-url]: https://github.com/Vincentqyw/cv-arxiv-daily/stargazers
[issues-shield]: https://img.shields.io/github/issues/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[issues-url]: https://github.com/Vincentqyw/cv-arxiv-daily/issues

