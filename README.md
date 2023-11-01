[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]

## Updated on 2023.11.01
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
|**2023-10-31**|**An Implementation of Multimodal Fusion System for Intelligent Digital Human Generation**|随着人工智能（AI）的快速发展，数字人越来越受到关注，并有望在多个行业实现广泛应用。那么，现有的大多数数字人仍然依赖于设计师的手动建模，这是一个繁琐的过程，而且开发周期很长。因此，面对数字人的崛起，迫切需要一个与人工智能相结合的数字人生成系统来提高开发效率。本文提出了一种多模态融合的智能数字人生成系统的实现方案。具体地，将文本、语音和图像作为输入，并使用大语言模型（LLM）、声纹提取和文本到语音转换技术来合成交互式语音。然后对输入图像进行年龄变换，并选择合适的图像作为驾驶图像。然后，通过数字人驱动、新颖的视图合成和智能着装技术，实现了数字人视频内容的修改和生成。最后，我们通过风格转换、超分辨率和质量评估来增强用户体验。实验结果表明，该系统能够有效地实现数字人的生成。相关代码发布于https://github.com/zyj-2000/CUMT_2D_PhotoSpeaker. et.al.|[2310.20251](http://arxiv.org/abs/2310.20251)|null|
|**2023-10-30**|**CustomNet: Zero-shot Object Customization with Variable-Viewpoints in Text-to-Image Diffusion Models**|将定制对象合并到图像生成中是文本到图像生成的一个有吸引力的特征。然而，现有的基于优化和基于编码器的方法受到诸如耗时优化、身份保存不足和普遍的复制粘贴效应等缺点的阻碍。为了克服这些限制，我们引入了CustomNet，这是一种新的对象定制方法，它将3D新视图合成功能明确地结合到对象定制过程中。这种集成有助于调整空间位置关系和视点，产生不同的输出，同时有效地保持对象身份。此外，我们引入了精细的设计，通过文本描述或特定的用户定义图像实现位置控制和灵活的背景控制，克服了现有3D新颖视图合成方法的局限性。我们进一步利用数据集构建管道，可以更好地处理真实世界的对象和复杂的背景。有了这些设计，我们的方法方便了零样本对象的定制，而无需测试时间优化，可以同时控制视点、位置和背景。因此，我们的CustomNet确保增强身份保护，并产生多样化、和谐的输出。 et.al.|[2310.19784](http://arxiv.org/abs/2310.19784)|null|
|**2023-10-31**|**DynPoint: Dynamic Neural Point For View Synthesis**|神经辐射场的引入极大地提高了单目视频视图合成的有效性。然而，现有算法在处理不受控制或冗长的场景时面临困难，并且需要针对每个新场景的大量训练时间。为了解决这些限制，我们提出了DynPoint，这是一种算法，旨在促进无约束单眼视频的新视图的快速合成。DynPoint不是将整个场景信息编码为潜在表示，而是专注于预测相邻帧之间的显式3D对应关系，以实现信息聚合。具体地，这种对应预测是通过估计帧之间一致的深度和场景流信息来实现的。随后，通过构建分层神经点云，利用所获取的对应关系将信息从多个参考帧聚合到目标帧。所得到的框架使得能够对目标帧的期望视图进行快速且准确的视图合成。所获得的实验结果表明，与先前的方法相比，我们提出的方法大大加快了训练时间，通常是一个数量级，同时产生了可比的结果。此外，我们的方法在处理长持续时间视频时表现出强大的鲁棒性，而无需学习视频内容的规范表示。 et.al.|[2310.18999](http://arxiv.org/abs/2310.18999)|null|
|**2023-10-27**|**ZeroNVS: Zero-Shot 360-Degree View Synthesis from a Single Real Image**|我们介绍了一种3D感知扩散模型ZeroNVS，用于野外场景的单图像新颖视图合成。虽然现有的方法是为具有遮罩背景的单个对象设计的，但我们提出了新的技术来解决具有复杂背景的野外多对象场景带来的挑战。具体来说，我们在捕捉以对象为中心、室内和室外场景的混合数据源上训练生成先验。为了解决深度尺度模糊等数据混合问题，我们提出了一种新的相机条件参数化和归一化方案。此外，我们观察到，在360度场景的提取过程中，分数提取采样（SDS）倾向于截断复杂背景的分布，并提出了“SDS锚定”来提高合成新视图的多样性。我们的模型在零样本设置中的DTU数据集上的LPIPS中设置了新的最先进的结果，甚至优于专门在DTU上训练的方法。我们进一步将具有挑战性的Mip-NeRF 360数据集作为单图像新视图合成的新基准，并在该设置中展示了强大的性能。我们的代码和数据位于http://kylesargent.github.io/zeronvs/ et.al.|[2310.17994](http://arxiv.org/abs/2310.17994)|null|
|**2023-10-27**|**Reconstructive Latent-Space Neural Radiance Fields for Efficient 3D Scene Representations**|神经辐射场（NeRF）已被证明是强大的3D表示，能够对复杂场景进行高质量的新颖视图合成。虽然NeRF已经应用于图形、视觉和机器人，但渲染速度慢和特有的视觉伪影问题阻碍了在许多用例中的采用。在这项工作中，我们研究了将自动编码器（AE）与NeRF相结合，其中潜在特征（而不是颜色）被渲染，然后进行卷积解码。由此产生的潜在空间NeRF可以产生比标准颜色空间NeRF质量更高的新颖视图，因为AE可以校正某些视觉伪影，同时渲染速度快三倍以上。我们的工作与提高NeRF效率的其他技术正交。此外，我们可以通过缩小AE架构来控制效率和图像质量之间的权衡，在性能下降很小的情况下实现13倍以上的渲染速度。我们希望我们的方法能够为下游任务形成高效但高保真的3D场景表示的基础，尤其是在保持可微性很有用的情况下，就像在许多需要持续学习的机器人场景中一样。 et.al.|[2310.17880](http://arxiv.org/abs/2310.17880)|null|
|**2023-10-26**|**LightSpeed: Light and Fast Neural Light Fields on Mobile Devices**|由于计算能力和存储空间有限，移动设备上的实时新视图图像合成是令人望而却步的。在移动设备上使用体积渲染方法（如NeRF及其衍生物）是不合适的，因为体积渲染的计算成本很高。另一方面，神经光场表示的最新进展在移动设备上显示出了有希望的实时视图合成结果。神经光场方法学习从光线表示到像素颜色的直接映射。光线表示的当前选择是分层光线采样或Plucker坐标，忽略了经典的光板（双平面）表示，这是在光场视图之间插值的首选表示。在这项工作中，我们发现使用光板表示是学习神经光场的有效表示。更重要的是，它是一种较低维的光线表示，使我们能够使用训练和渲染速度明显更快的特征网格来学习4D光线空间。尽管主要是为正面视图设计的，但我们表明，光板表示可以使用分而治之的策略进一步扩展到非正面场景。与以前的光场方法相比，我们的方法提供了卓越的渲染质量，并显著改善了渲染质量和速度之间的平衡。 et.al.|[2310.16832](http://arxiv.org/abs/2310.16832)|**[link](https://github.com/lightspeed-r2l/lightspeed)**|
|**2023-10-28**|**PERF: Panoramic Neural Radiance Field from a Single Panorama**|神经辐射场（NeRF）在给定多视点图像的新视点合成方面取得了实质性进展。最近，一些工作试图从具有3D先验的单个图像中训练NeRF。它们主要关注具有少量遮挡的有限视场，这极大地限制了它们在具有大尺寸遮挡的真实世界360度全景场景中的可扩展性。在本文中，我们提出了PERF，这是一种360度新颖的视图合成框架，它从单个全景训练全景神经辐射场。值得注意的是，PERF允许在复杂场景中进行3D漫游，而无需昂贵且乏味的图像采集。为了实现这一目标，我们提出了一种新的协作RGBD修复方法和一种渐进的修复和擦除方法，以将360度2D场景提升为3D场景。具体而言，我们首先预测全景深度图作为给定单个全景的初始化，并使用体绘制重建可见的3D区域。然后，我们在NeRF中引入了一种协作的RGBD修复方法，用于从随机视图中完成RGB图像和深度图，该方法源自RGB稳定扩散模型和单目深度估计器。最后，我们介绍了一种修复和擦除策略，以避免新采样视图和参考视图之间的几何不一致。这两个组件在统一的优化框架中集成到NeRF的学习中，并取得了有希望的结果。在Replica和野外新数据集PERF上进行的大量实验证明了我们的PERF优于最先进的方法。我们的PERF可以广泛用于真实世界的应用，如全景到3D、文本到3D和3D场景风格化应用。项目页面和代码可在https://perf-project.github.io/和https://github.com/perf-project/PeRF. et.al.|[2310.16831](http://arxiv.org/abs/2310.16831)|**[link](https://github.com/perf-project/PeRF)**|
|**2023-10-25**|**Open-NeRF: Towards Open Vocabulary NeRF Decomposition**|在本文中，我们解决了从开放词汇中将神经辐射场（NeRF）分解为对象的挑战，这是三维重建和视图合成中对象操作的关键任务。当前的NeRF分解技术涉及处理开放词汇查询的灵活性和3D分割的准确性之间的权衡。我们提出了开放词汇嵌入式神经辐射场（Open NeRF），它利用了大规模现成的分割模型，如Segment Anything Model（SAM），并引入了一种具有分层嵌入的集成和提取范式，以实现开放词汇查询的灵活性和3D分割的准确性。Open NeRF首先利用大规模基础模型从不同的角度生成分层2D掩模方案。然后，通过跟踪方法将这些建议对齐，并将其集成在3D空间中，随后将其提取到3D领域中。这一过程确保了从不同角度对对象的一致识别和粒度，即使在涉及遮挡和模糊特征的具有挑战性的场景中也是如此。我们的实验结果表明，在开放词汇场景中，所提出的Open NeRF优于最先进的方法，如LERF\cite{LERF}和FFD\cite{FFD}。Open NeRF为NeRF分解提供了一个很有前途的解决方案，以开放词汇查询为指导，在开放世界3D场景中实现机器人和视觉语言交互的新应用。 et.al.|[2310.16383](http://arxiv.org/abs/2310.16383)|null|
|**2023-10-24**|**iNVS: Repurposing Diffusion Inpainters for Novel View Synthesis**|我们提出了一种从单一源图像生成一致新颖视图的方法。我们的方法侧重于最大限度地重用源图像中的可见像素。为了实现这一点，我们使用单目深度估计器，将可见像素从源视图转移到目标视图。从预先训练的2D修复扩散模型开始，我们在大规模Ob厌恶数据集上训练我们的方法来学习3D对象先验。在训练时，我们使用了一种基于核线的新型掩蔽机制来进一步提高我们的方法的质量。这使得我们的框架能够对各种对象执行零样本新颖的视图合成。我们在三个具有挑战性的数据集上评估了我们框架的零样本能力：谷歌扫描对象、光线跟踪多视图和3D中的常见对象。查看我们的网页了解更多详细信息：https://yashkant.github.io/invs/ et.al.|[2310.16167](http://arxiv.org/abs/2310.16167)|null|
|**2023-10-23**|**Relit-NeuLF: Efficient Relighting and Novel View Synthesis via Neural 4D Light Field**|在本文中，我们解决了在光源数量有限的情况下，从多视图图像中同时重新照明和合成复杂场景的新视图的问题。我们提出了一种称为Relit NeuLF的分析综合方法。继最近的神经4D光场网络（NeuLF）之后，Relit NeuLF首先利用两平面光场表示来参数化4D坐标系中的每条光线，从而实现高效的学习和推理。然后，我们以自监督的方式恢复三维场景的空间变化双向反射率分布函数（SVBRDF）。DecomposeNet学习将每条光线映射到其SVBRDF组件：反照率、法线和粗糙度。基于分解的BRDF分量和条件光方向，RenderNet学习合成光线的颜色。为了自我监督SVBRDF分解，我们鼓励使用微平面模型使预测的光线颜色接近基于物理的渲染结果。综合实验表明，该方法在合成数据和真实人脸数据上都是有效的，并且优于最先进的结果。我们在GitHub上公开发布了我们的代码。你可以在这里找到它：https://github.com/oppo-us-research/RelitNeuLF et.al.|[2310.14642](http://arxiv.org/abs/2310.14642)|**[link](https://github.com/oppo-us-research/relitneulf)**|

<p align=right>(<a href=#updated-on-20231101>back to top</a>)</p>

## 3D Reconstruction

|Publish Date|Title|Abstract|PDF|Code|
|---|---|---|---|---|
|**2023-10-31**|**Refined Equivalent Pinhole Model for Large-scale 3D Reconstruction from Spaceborne CCD Imagery**|在这项研究中，我们提出了一个用于线阵电荷耦合器件（CCD）卫星图像的大规模地表重建管道。虽然主流的基于卫星图像的重建方法表现得非常好，但有理函数模型（RFM）受到一些限制。例如，RFM没有严格的物理解释，与针孔成像模型有很大不同；因此，它不能直接应用于基于学习的三维重建网络和计算机视觉中更新颖的重建管道。因此，在本研究中，我们介绍了一种方法，其中RFM等效于针孔相机模型（PCM），这意味着使用针孔相机的内部和外部参数，而不是有理多项式系数参数。然后，我们首次推导出该等效针孔模型的误差公式，证明了图像大小对重建精度的影响。此外，我们提出了一个多项式图像细化模型，通过最小二乘法最小化等效误差。实验使用四个图像数据集进行：WHU-TLC、DFC2019、ISPRS-ZY3和GF7。结果表明，重建精度与图像大小成正比。我们的多项式图像细化模型显著提高了重建的准确性和完整性，并对更大尺度的图像实现了更显著的改进。 et.al.|[2310.20117](http://arxiv.org/abs/2310.20117)|null|
|**2023-10-29**|**3DMiner: Discovering Shapes from Large-Scale Unannotated Image Datasets**|我们介绍了3DMiner——一种从具有挑战性的大规模未标记图像数据集中挖掘3D形状的管道。与其他无监督的3D重建方法不同，我们假设，在一个足够大的数据集中，必须存在形状相似但背景、纹理和视点不同的对象图像。我们的方法利用学习自监督图像表示的最新进展，对具有几何相似形状的图像进行聚类，并找到它们之间的常见图像对应关系。然后，我们利用这些对应关系来获得粗略的相机估计，作为束调整的初始化。最后，对于每个图像聚类，我们应用渐进束调整重建方法来学习表示底层形状的神经占据场。我们表明，该程序对之前步骤中引入的几种类型的错误（例如，错误的相机姿势、包含不同形状的图像等）是稳健的，使我们能够获得野外图像的形状和姿势注释。当使用Pix3D椅子的图像时，我们的方法能够在定量和定性方面产生比最先进的无监督3D重建技术更好的结果。此外，我们还展示了3DMiner如何通过重建LAION-5B数据集中图像中的形状来应用于野外数据。项目页面：https://ttchengab.github.io/3dminerOfficial et.al.|[2310.19188](http://arxiv.org/abs/2310.19188)|null|
|**2023-10-29**|**Towards Generalized Multi-stage Clustering: Multi-view Self-distillation**|现有的多阶段聚类方法从多个视图中独立地学习显著特征，然后执行聚类任务。特别是，多视图集群（MVC）在多视图或多模式场景中引起了很多关注。MVC旨在从多个视图中探索通用语义和伪标签，并以自监督的方式进行聚类。然而，受噪声数据和特征学习不足的限制，这种聚类范式会产生过于自信的伪标签，错误地引导模型产生不准确的预测。因此，希望有一种方法可以在多阶段聚类中纠正这种伪标签错误行为，以避免偏差累积。为了缓解过度自信的伪标签的影响，提高模型的泛化能力，本文提出了一种新的多阶段深度MVC框架，引入多视图自蒸馏（DistilMVC）来提取标签分布的暗知识。具体来说，在不同层次的特征子空间中，我们通过对比学习来探索多个视图的共同语义，并通过最大化视图之间的相互信息来获得伪标签。此外，教师网络负责将伪标签提取到暗知识中，监督学生网络并提高其预测能力以增强鲁棒性。在真实世界的多视图数据集上进行的大量实验表明，我们的方法比最先进的方法具有更好的聚类性能。 et.al.|[2310.18890](http://arxiv.org/abs/2310.18890)|null|
|**2023-10-27**|**Understanding the effect of curvature on the magnetization reversal of three-dimensional nanohelices**|理解三维（3D）纳米结构中几何结构和磁性之间的相互作用对于理解畴壁（DW）形成和钉扎的基本物理具有重要意义。在这里，我们使用聚焦电子束诱导沉积来制备具有随高度增加的螺旋曲率的磁性纳米螺旋。利用电子断层扫描和洛伦兹透射电子显微镜，我们重建了纳米螺旋的三维结构和磁化强度。然后从断层图像重建中量化纳米螺旋的表面曲率、螺旋曲率和扭转。此外，通过使用实验三维重建作为微磁模拟的输入，我们可以揭示表面和螺旋曲率对磁反转机制的影响。因此，我们可以将3D纳米螺旋的磁性行为与其实验结构直接关联起来。这些结果证明了如何利用纳米螺旋中几何形状的控制来稳定DW和控制纳米结构对所施加磁场的响应。 et.al.|[2310.18456](http://arxiv.org/abs/2310.18456)|null|
|**2023-10-25**|**Open-NeRF: Towards Open Vocabulary NeRF Decomposition**|在本文中，我们解决了从开放词汇中将神经辐射场（NeRF）分解为对象的挑战，这是三维重建和视图合成中对象操作的关键任务。当前的NeRF分解技术涉及处理开放词汇查询的灵活性和3D分割的准确性之间的权衡。我们提出了开放词汇嵌入式神经辐射场（Open NeRF），它利用了大规模现成的分割模型，如Segment Anything Model（SAM），并引入了一种具有分层嵌入的集成和提取范式，以实现开放词汇查询的灵活性和3D分割的准确性。Open NeRF首先利用大规模基础模型从不同的角度生成分层2D掩模方案。然后，通过跟踪方法将这些建议对齐，并将其集成在3D空间中，随后将其提取到3D领域中。这一过程确保了从不同角度对对象的一致识别和粒度，即使在涉及遮挡和模糊特征的具有挑战性的场景中也是如此。我们的实验结果表明，在开放词汇场景中，所提出的Open NeRF优于最先进的方法，如LERF\cite{LERF}和FFD\cite{FFD}。Open NeRF为NeRF分解提供了一个很有前途的解决方案，以开放词汇查询为指导，在开放世界3D场景中实现机器人和视觉语言交互的新应用。 et.al.|[2310.16383](http://arxiv.org/abs/2310.16383)|null|
|**2023-10-23**|**Novel-View Acoustic Synthesis from 3D Reconstructed Rooms**|我们研究了将盲音频记录与3D场景信息相结合用于新视图声学合成的好处。给定2-4个麦克风的音频记录以及包含多个未知声源的场景的3D几何形状和材料，我们估计场景中任何地方的声音。我们确定了新观点声学合成的主要挑战是声源定位、分离和去混响。虽然天真地训练端到端网络无法产生高质量的结果，但我们表明，结合从3D重建房间中导出的房间脉冲响应（RIR）使同一网络能够联合处理这些任务。我们的方法优于为单个任务设计的现有方法，证明了它在利用3D视觉信息方面的有效性。在对Matterport3D NVAS数据集的模拟研究中，我们的模型在源定位方面实现了近乎完美的精度，在源分离和去混响方面实现了26.44dB的PSNR和14.23dB的SDR，在新视图声学合成方面实现了25.55dB的PSNR和14.20dB的SDR。代码、预训练模型和视频结果可在项目网页上获得(https://github.com/apple/ml-nvas3d)。 et.al.|[2310.15130](http://arxiv.org/abs/2310.15130)|**[link](https://github.com/apple/ml-nvas3d)**|
|**2023-10-23**|**Interaction-Driven Active 3D Reconstruction with Object Interiors**|我们介绍了一种主动三维重建方法，该方法集成了视觉感知、机器人-物体交互和三维扫描，以恢复目标三维物体的外部和内部，即未暴露的几何形状。与主动视觉中专注于优化相机视点以更好地研究环境的其他工作不同，我们重建的主要特征是分析目标物体各个部分的相互作用性，以及机器人随后进行的部分操作，以实现对遮挡区域的扫描。因此，在完整的几何结构采集的基础上，获得了对目标物体的部分关节的理解。我们的方法由一个内置RGBD传感器的Fetch机器人完全自动操作。它在交互分析和交互驱动的重建之间迭代，一次扫描和重建检测到的可移动零件，其中关节零件检测和网格重建都由神经网络执行。在最后一步中，重建所有剩余的非铰接部件，包括通过先前部件操作暴露并随后扫描的所有内部结构，以完成采集。我们通过定性和定量评估、消融研究、与替代方案的比较以及在真实环境中的实验来证明我们的方法的性能。 et.al.|[2310.14700](http://arxiv.org/abs/2310.14700)|null|
|**2023-10-23**|**VQ-NeRF: Vector Quantization Enhances Implicit Neural Representations**|隐式神经表示的最新进展有助于高保真度的表面重建和真实感的新视图合成。然而，这些方法中固有的计算复杂性是一个巨大的障碍，限制了实际应用中可达到的帧速率和分辨率。针对这一困境，我们提出了VQ-NeRF，这是一种通过矢量量化增强隐式神经表示的有效管道。我们的方法的本质包括将NeRF的采样空间减少到较低的分辨率，然后使用预训练的VAE解码器将其恢复到原始大小，从而有效地缓解渲染过程中遇到的采样时间瓶颈。尽管码本提供了代表性的特征，但由于高压缩率，重建场景的精细纹理细节仍然具有挑战性。为了克服这一限制，我们设计了一种创新的多尺度NeRF采样方案，该方案在压缩和原始尺度上同时优化NeRF模型，以增强网络保存精细细节的能力。此外，我们引入了语义损失函数，以提高三维重建的几何保真度和语义连贯性。大量实验证明了我们的模型在实现渲染质量和效率之间的最佳权衡方面的有效性。对DTU、BlendMVS和H3DS数据集的评估证实了我们方法的卓越性能。 et.al.|[2310.14487](http://arxiv.org/abs/2310.14487)|null|
|**2023-10-22**|**A Quantitative Evaluation of Dense 3D Reconstruction of Sinus Anatomy from Monocular Endoscopic Video**|根据内窥镜视频生成准确的3D重建是对鼻窦解剖结构和手术结果进行纵向无辐射分析的一种很有前途的途径。已经提出了几种单目重建方法，通过从运动类型算法中检索具有结构的相对相机姿态并融合单目深度估计，产生视觉上令人愉快的3D解剖结构。然而，由于底层算法和内窥镜场景的复杂特性，重建管道可能表现不佳或意外失败。此外，获取医疗数据带来了额外的挑战，在定量基准测试这些模型、了解故障案例和确定有助于其准确性的关键组件方面存在困难。在这项工作中，我们对一种自监督的鼻窦重建方法进行了定量分析，该方法使用内窥镜序列与从9个离体标本中采集的光学跟踪和高分辨率计算机断层扫描相结合。我们的结果表明，生成的重建与解剖结构高度一致，在重建和CT分割之间产生0.91mm的平均点到网格误差。然而，在与内窥镜跟踪和导航相关的点对点匹配场景中，我们发现平均目标配准误差为6.58 mm。我们发现，姿态和深度估计的不准确度对该误差的贡献相同，轨迹较短的局部一致序列会产生更准确的重建。这些结果表明，实现相对相机姿态和估计深度与解剖结构之间的全局一致性至关重要。通过这样做，我们可以确保管道的所有组成部分之间的适当协同作用，以改进重建，从而促进这项创新技术的临床应用。 et.al.|[2310.14364](http://arxiv.org/abs/2310.14364)|null|
|**2023-10-20**|**Longer-range Contextualized Masked Autoencoder**|掩模图像建模（MIM）已成为一种很有前途的自监督学习（SSL）策略。MIM预训练通过随机掩蔽一些输入像素并从剩余的像素重建掩蔽的像素，有助于使用编码器-解码器框架来学习强大的表示。然而，由于编码器是用部分像素训练的，MIM预训练可能存在理解长程依赖性的能力低的问题。这种限制可能会阻碍其完全理解多个范围依赖性的能力，导致注意力图中突出显示的区域狭窄，从而可能导致准确性下降。为了减轻这种限制，我们提出了一个自监督学习框架，称为长距离上下文化屏蔽自动编码器（LC-MAE）。LC-MAE有效地利用了对视觉表示的全局上下文理解，同时减少了输入的空间冗余。我们的方法引导编码器从多个视图中的整个像素学习，同时也从稀疏像素学习局部表示。因此，LC-MAE学习了更多的判别表示，导致性能提高，在ImageNet-1K上使用ViT-B以0.6%p的增益实现84.2%的前1级精度。我们将成功归因于增强的预训练方法，奇异值谱和注意力分析证明了这一点。最后，LC-MAE在下游语义分割和细粒度视觉分类任务中实现了显著的性能提升；以及不同的稳健评估指标。我们的代码将公开。 et.al.|[2310.13593](http://arxiv.org/abs/2310.13593)|null|

<p align=right>(<a href=#updated-on-20231101>back to top</a>)</p>

## Diffusion

|Publish Date|Title|Abstract|PDF|Code|
|---|---|---|---|---|
|**2023-10-31**|**SEINE: Short-to-Long Video Diffusion Model for Generative Transition and Prediction**|最近，视频生成已经取得了实质性的进展，并取得了现实的结果。尽管如此，现有的人工智能生成的视频通常是描绘单个场景的非常短的片段（“镜头级别”）。为了提供连贯的长视频（“故事级别”），需要在不同的剪辑之间具有创造性的过渡和预测效果。本文提出了一个短到长视频扩散模型SEINE，该模型侧重于生成转换和预测。目标是生成高质量的长视频，在场景和不同长度的镜头级视频之间进行平滑和创造性的转换。具体来说，我们提出了一个随机掩码视频扩散模型，以基于文本描述自动生成转换。通过提供不同场景的图像作为输入，结合基于文本的控制，我们的模型生成了确保连贯性和视觉质量的过渡视频。此外，该模型可以很容易地扩展到各种任务，例如图像到视频动画和自回归视频预测。为了对这一新的生成任务进行全面评估，我们提出了三个平稳和创造性过渡的评估标准：时间一致性、语义相似性和视频文本语义对齐。大量的实验验证了我们的方法相对于现有的生成转换和预测方法的有效性，从而能够创建故事级的长视频。项目页面：https://vchitect.github.io/SEINE-project/。 et.al.|[2310.20700](http://arxiv.org/abs/2310.20700)|null|
|**2023-10-31**|**Diffusion Reconstruction of Ultrasound Images with Informative Uncertainty**|尽管超声成像在医学上有着广泛的应用，但由于其信噪比低以及多种噪声和伪影来源，它面临着一些挑战。增强超声图像质量涉及到平衡同时存在的因素，如对比度、分辨率和斑点保持。近年来，在基于模型和基于学习的方法方面都取得了进展，以改进超声图像重建。我们从两个世界中汲取精华，提出了一种利用扩散模型进步的混合方法。为此，我们采用去噪扩散恢复模型（DDRM），通过线性直接模型和对先前扩散模型的无监督微调来结合超声物理。我们对模拟、体外和体内数据进行了全面的实验，证明了我们的方法在从单个平面波输入实现高质量图像重建方面的有效性，并与最先进的方法进行了比较。最后，考虑到该方法的随机性，我们深入分析了单样本和多样本重建的统计特性，实验显示了它们的方差的信息性，并提供了一个将这种行为与散斑噪声联系起来的经验模型。代码和数据可在以下网址获得：（验收后）。 et.al.|[2310.20618](http://arxiv.org/abs/2310.20618)|null|
|**2023-10-31**|**Modelling of dust emission of a filament in the Taurus molecular cloud**|尘埃发射是研究恒星形成云的一个重要工具，作为柱密度的示踪剂，并间接通过与云的历史和物理条件有关的尘埃演化。我们以金牛座分子云中的一根细丝为例，研究了扩展云区尘埃发射的辐射传输（RT）模型。我们研究了远红外观测在多大程度上可以用来确定云和尘埃的性质。使用云形状、辐射场和尘埃特性的不同假设，我们将RT模型与赫歇尔对金牛座细丝的观测结果进行了拟合。并与近红外消光的测量结果作了进一步的比较。这些模型用于检验不同云参数和尘埃特性之间的退化。结果表明，假设的云结构和外部辐射场的光谱形状具有显著的相关性。如果这些值被限制在最可能的值，则只有当尘埃远红外（FIR）不透明度相对于漫射介质中的值增加了2-3倍时，才能解释观测结果。然而，即使在覆盖数平方度分子云的模型中，窄范围的FIR波长也只能提供微弱的证据来证明尘埃的空间变化。FIR粉尘排放的分析受到几个不确定性来源的影响。因此，需要对较短波长的观测进行进一步的限制，特别是关于尘埃演变的趋势。 et.al.|[2310.20585](http://arxiv.org/abs/2310.20585)|null|
|**2023-10-31**|**The effect of demographic stochasticity on predatory-prey oscillations**|相互作用的捕食者和猎物种群的生态动力学可以显示出持续的振荡，例如Rosenzweig-MacArthur捕食者-猎物模型所预测的。由于人口规模的有限性，人口统计的随机性改变了这些振荡的幅度和频率。本文提出了一种刻画人口统计随机性对Rosenzweig-MacArthur极限环吸引子影响的方法。我们证明了角布朗运动很好地描述了频率振荡。在分叉点附近，我们得到了角扩散常数的解析近似。该近似值准确地捕捉了人口统计学随机性对参数值的影响。 et.al.|[2310.20575](http://arxiv.org/abs/2310.20575)|null|
|**2023-10-31**|**The very singular solution for the Anisotropic Fast Diffusion Equation and its consequences**|我们构造了各向异性快速扩散方程（AFDE）在合适的良好指数范围内的奇异解（VSS）。VSS是一种从位于一点的无限质量作为初始基准开始，根据相应的方程演化为远离奇点的容许解的解。当初始质量很大时，它有望代表基本解的重要性质。我们在整个空间工作。在这种情况下，我们证明了扩散过程沿着不同的空间方向分布来自初始无限奇异点的质量：对于各向异性质量膨胀，存在一个简单的分配公式，近似为单独的一维VSS解的最小值。这一惊人的事实是特殊解决方案的缩放特性得到改善的结果，它具有强烈的后果。如果我们考虑不同质量的基本解族，我们证明它们与VSS具有相同的通用尾部行为。实际上，它们的尾是渐近收敛于唯一的VSS尾的，所以在空间无穷大处，它们的轮廓有一个VSS分割公式。借助于此分析，我们研究了各向异性FDE的一类非负有限质量解的性质，并证明了在初始尾衰减的自然假设下的全局Harnack原理（GHP）和相对误差的渐近收敛性（ACRE）。 et.al.|[2310.20569](http://arxiv.org/abs/2310.20569)|null|
|**2023-10-31**|**On the structure-viscoelasticity relationship of a dually crosslinked reversible polymer network**|我们进行了平衡Langevin动力学模拟，以了解双向交联可逆聚合物网络的结构-粘弹性关系。交联是通过将正交交联剂（A和B）引入聚合物主链来实现的，其中只允许形成物种内键（A-A或B-B）。我们研究了在无限稀释和链的重叠浓度以上的系统。我们发现，在无限稀释条件下，双交联链比单交联链更紧凑。在有限浓度下，我们还通过系统地改变A单体（x）的相对组成，同时保持交联的总分数不变，探索了弱（A-A）键与强（B-B）键在调节网络的应力松弛行为中的作用。有趣的是，我们发现扩散率以及系统w.r.t.x的应力自相关函数存在非单调趋势。此外，我们发现在平台区的动力学中，应力松弛函数由弱键的强度决定，而应力自相关函数的末端弛豫行为取决于强键的强度。我们还通过对链的对称分布进行额外的模拟，研究了A和B的分布对应力松弛的影响。有趣的是，我们发现在对称情况下，分子间键明显较低，这使其与随机对应物相比具有更快的应力松弛。我们的研究强调了交联单体的组成、分布和键能差异对调节双网络粘弹性的影响。 et.al.|[2310.20553](http://arxiv.org/abs/2310.20553)|null|
|**2023-10-31**|**Semipermeable interfaces and the target problem**|在本章中，我们回顾了我们最近关于界面是半渗透的目标吸收的首次通过时间（FPT）问题的工作。出于教学的原因，我们将重点放在单个布朗粒子在有界域中搜索单个目标上。我们首先写下目标问题的正向扩散方程，并定义各种感兴趣的量，如生存概率、吸收通量和FPT密度。我们还提出了一种基于格林函数和所谓的Dirichlet到Neumann（D-to-N）算子的谱分解的一般求解方法。然后，我们使用基于相遇的方法将该理论扩展到目标内部非马尔可夫吸收的情况。基于相遇的模型考虑了粒子位置的联合概率密度或广义传播子以及吸收前粒子与目标的接触时间。在部分吸收目标内部的情况下，接触时间由称为占据时间的布朗函数给出。最后，我们通过将基于相遇的方法与所谓的弹出布朗运动（BM）相结合，开发了一个更通用的单粒子通过半渗透界面扩散的概率模型。弹出BM将连续几轮的部分吸收BM缝合在一起，这些BM被限制在半渗透界面的内部或外部。终止每一轮的规则是使用部分吸收BM的基于相遇的模型来实现的。我们表明，这导致了可能是重尾的时间相关渗透率。 et.al.|[2310.20532](http://arxiv.org/abs/2310.20532)|null|
|**2023-10-31**|**Structure and Color Gradients of Ultra-diffuse Galaxies in Distant Massive Galaxy Clusters**|我们测量了108个超扩散星系（UDG）的结构参数和径向颜色轮廓，这些星系是从哈勃前沿场（HFF）的六个遥远的大质量星系团中精心挑选出来的，红移范围从0.308到0.545。我们的最佳拟合GALFIT模型显示，HFF UDG的中值S’ersic指数为1.09，这接近于Coma集群中局部UDG的0.86。HFF UDG和Coma UDG的中轴比值分别为0.68和0.74。HFF和Coma UDG之间的结构相似性表明，它们是在不同时间看到的同一类星系，UDG的结构至少在几十亿年内不会改变。通过检查其余帧 $UVJ$和$UVI$图中HFF UDG的分布，我们发现其中很大一部分是恒星形成的。此外，大多数HFF UDG在\，1\，*\，$R_{e，SMA}$区域内显示出较小的$\rm U-V$颜色梯度，HFF UDGs的中值径向颜色轮廓的波动小于0.1\，mag，这与Coma UDGs兼容。我们的结果表明，无论径向距离如何，在小于$\sim$ 4Gyrs的时间内，星团UDG可能以自相似的方式衰减或猝灭。 et.al.|[2310.20530](http://arxiv.org/abs/2310.20530)|null|
|**2023-10-31**|**Truncated stochastically switching processes**|存在着各种各样的混合随机系统，它们将连续过程与某种形式的随机切换机制耦合在一起。在许多情况下，系统根据有限状态马尔可夫链在不同的离散内部状态之间切换，并且连续的动力学取决于当前的内部状态。由此产生的混合随机微分方程（hSDE）可以描述神经元膜电位的演变、基因网络合成的蛋白质浓度或活性粒子的位置。另一类主要的切换系统是具有随机重置的搜索过程，其中扩散或活性粒子的位置以随机的时间序列重置到固定位置。在这种情况下，系统在搜索阶段和重置阶段之间切换，其中重置阶段可以是瞬时的。在本文中，我们研究了当给定时间间隔内切换（或重置）事件的最大数量固定时，随机切换系统的行为是如何修改的。这是因为每次系统切换都会产生额外的能源成本。我们首先证明，在hSDE的情况下，限制切换事件的数量相当于截断粒子传播子的Volterra级数展开。这样的截断显著地修改了由此产生的重整化传播子的矩。然后，我们研究了限制重置事件的数量如何影响对吸收目标的扩散搜索。特别是，截断生存概率的Volterra级数展开，我们分别计算粒子被目标吸收或超过给定重置次数的分裂概率和条件MFPT。 et.al.|[2310.20502](http://arxiv.org/abs/2310.20502)|null|
|**2023-10-31**|**On the Long-time Dynamics and Ergodicity of the Stochastic Nernst-Planck-Navier-Stokes System**|我们考虑了一个电扩散模型，该模型描述了多个离子物种与二维、不可压缩、粘性流体在随机加性噪声下的复杂相互作用。该系统包括离子物质的非局部非线性漂移扩散Nernst-Planck方程和流体在电和时间无关力影响下运动的随机Navier-Stokes方程。在浓度的选择性边界条件下，我们在光滑有界域上建立了该系统全局路径解的存在性和唯一性。我们的研究还研究了长时间离子浓度动力学，并探索了关联马尔可夫半群的Feller性质。在等扩散物种的背景下，在适当的条件下，我们证明了在 $H^2$上支持的不变遍历测度的存在性。然后，我们增强了周期tori上的遍历性结果，并在浓度的初始空间平均值的约束下获得了光滑不变的测度。当噪声迫使足够的模，并且物种的扩散率大时，进一步建立了周期盒和光滑有界域上不变测度的唯一性。最后，在扩散率和价分别为$1$和$1$ 的两个离子物种的情况下，我们研究了马尔可夫转移核到不变测度的收敛速度，并获得了该模型的无条件、唯一的指数遍历性。 et.al.|[2310.20484](http://arxiv.org/abs/2310.20484)|null|

<p align=right>(<a href=#updated-on-20231101>back to top</a>)</p>

## NeRF

|Publish Date|Title|Abstract|PDF|Code|
|---|---|---|---|---|
|**2023-10-31**|**Latent Field Discovery In Interacting Dynamical Systems With Neural Fields**|交互对象的系统通常在控制其动力学的场效应的影响下进化，然而以前的工作已经从这种效应中抽象出来，并假设系统是在真空中进化的。在这项工作中，我们专注于发现这些场，并仅从观察到的动力学中推断它们，而不直接观察它们。我们将潜在力场的存在理论化，并提出神经场来学习它们。由于观测到的动力学构成了局部物体相互作用和全局场效应的净效应，最近流行的等变网络不适用，因为它们无法捕捉全局信息。为了解决这一问题，我们建议将局部对象交互（ $\mathrm｛SE｝（n）$ 等变并依赖于相对状态）与外部全局场效应（依赖于绝对状态）区分开来。我们用等变图网络对交互进行建模，并将它们与神经场结合在一个集成场力的新型图网络中。我们的实验表明，我们可以准确地发现带电粒子环境、交通场景和引力n体问题中的潜在场，并有效地利用它们来学习系统和预测未来的轨迹。 et.al.|[2310.20679](http://arxiv.org/abs/2310.20679)|**[link](https://github.com/mkofinas/aether)**|
|**2023-10-30**|**Generative Neural Fields by Mixtures of Neural Implicit Functions**|我们提出了一种新的方法来学习由隐式基网络的线性组合表示的生成神经场。我们的算法通过进行元学习或采用自动解码范式，在潜在空间中以隐式神经表示的形式学习基网络及其系数。所提出的方法通过增加基网络的数量来容易地扩大生成神经场的容量，同时通过加权模型平均来保持推理网络的大小较小。因此，使用该模型对实例进行采样在延迟和内存占用方面是有效的。此外，我们为目标任务定制了去噪扩散概率模型，以对潜在的混合系数进行采样，这使我们的最终模型能够有效地生成看不见的数据。实验表明，我们的方法在图像、体素数据和NeRF场景的不同基准上实现了有竞争力的生成性能，而无需对特定模态和域进行复杂的设计。 et.al.|[2310.19464](http://arxiv.org/abs/2310.19464)|null|
|**2023-10-24**|**LiCROM: Linear-Subspace Continuous Reduced Order Modeling with Neural Fields**|线性降阶建模（ROM）通过使用简化的运动学表示来近似系统的行为，从而简化了复杂的模拟。通常，ROM在使用特定空间离散化创建的输入模拟上进行训练，然后用于使用相同的离散化加速模拟。这种离散化依赖性是有限制的。独立于特定的离散化将提供在训练数据中混合和匹配网格分辨率、连通性和类型（四面体、六面体）的灵活性；以在训练过程中看不到的新颖离散化来加速模拟；以及加速在时间上或参数化地改变离散化的自适应模拟。我们提出了一种灵活的、独立于离散化的降阶建模方法。与传统ROM一样，我们将配置表示为位移场的线性组合。与传统的ROM不同，我们的位移场是从参考域上的每个点到相应位移矢量的连续映射；这些映射被表示为隐式神经场。使用线性连续ROM（LiCROM），我们的训练集可以包括经历多个加载条件的多个几何体，与它们的离散化无关。这为降阶建模的新应用打开了大门。我们现在可以加速在运行时修改几何体的模拟，例如通过切割、打孔，甚至交换整个网格。我们还可以加速对训练中看不见的几何形状的模拟。我们演示了一次性泛化，在单个几何体上进行训练，然后模拟各种看不见的几何体。 et.al.|[2310.15907](http://arxiv.org/abs/2310.15907)|null|
|**2023-10-12**|**S4C: Self-Supervised Semantic Scene Completion with Neural Fields**|三维语义场景理解是计算机视觉中的一个基本挑战。它使移动代理能够自主规划和导航任意环境。SSC将这一挑战形式化为从场景的稀疏观测中联合估计密集的几何结构和语义信息。当前的SSC方法通常基于聚合的激光雷达扫描在3D地面实况上进行训练。这一过程依赖于特殊的传感器和手工注释，这些传感器和注释成本高昂且规模不大。为了克服这个问题，我们的工作提出了第一种称为S4C的SSC自监督方法，该方法不依赖于3D地面实况数据。我们提出的方法可以从单个图像重建场景，并且只依赖于训练期间从现成的图像分割网络生成的视频和伪分割地面实况。与使用离散体素网格的现有方法不同，我们将场景表示为隐式语义场。该公式允许查询相机截锥体内的任何点的占用率和语义类。我们的架构是通过基于渲染的自监督损失进行训练的。尽管如此，我们的方法实现了接近于完全监督的最先进方法的性能。此外，我们的方法表现出强大的泛化能力，可以为遥远的视点合成准确的分割图。 et.al.|[2310.07522](http://arxiv.org/abs/2310.07522)|null|
|**2023-10-07**|**HI-SLAM: Monocular Real-time Dense Mapping with Hybrid Implicit Fields**|在这封信中，我们提出了一个基于神经场的实时单目映射框架，用于精确和密集的同时定位和映射（SLAM）。最近的神经映射框架显示出有希望的结果，但依赖于RGB-D或姿势输入，或者无法实时运行。为了解决这些局限性，我们的方法将密集SLAM与神经隐式场相结合。具体来说，我们的密集SLAM方法运行并行跟踪和全局优化，而基于神经场的映射是基于最新的SLAM估计逐步构建的。为了有效地构造神经场，我们采用了多分辨率网格编码和符号距离函数（SDF）表示。这使我们能够始终保持地图的最新状态，并通过循环关闭立即适应全球更新。为了全局一致性，我们提出了一种有效的基于Sim（3）的姿态图束调整（PGBA）方法来运行在线闭环并减轻姿态和尺度漂移。为了进一步提高深度精度，我们结合了学习的单目深度先验。我们提出了一种新的深度和尺度联合调整（JDSA）模块来解决深度先验中固有的尺度模糊性。对合成和真实世界数据集的广泛评估验证了我们的方法在准确性和地图完整性方面优于现有方法，同时保持了实时性能。 et.al.|[2310.04787](http://arxiv.org/abs/2310.04787)|null|
|**2023-10-05**|**Variational Barycentric Coordinates**|我们提出了一种变分技术来优化广义重心坐标，与现有模型相比，该技术提供了额外的控制。先前的工作使用网格或闭式公式表示重心坐标，在实践中限制了目标函数的选择。相反，我们使用神经场直接参数化连续函数，该函数将多面体内部的任何坐标映射到其重心坐标。这个公式是通过我们对重心坐标的理论表征实现的，这使我们能够构建将有效坐标的整个函数类参数化的神经场。我们使用各种目标函数展示了我们模型的灵活性，包括多重光滑性和变形感知能量；作为补充，我们还提出了数学上合理的方法来测量和最小化目标，如不连续神经场的总变化。我们提供了一个实用的加速策略，对我们的算法进行了彻底的验证，并展示了几个应用。 et.al.|[2310.03861](http://arxiv.org/abs/2310.03861)|null|
|**2023-10-05**|**High-Degrees-of-Freedom Dynamic Neural Fields for Robot Self-Modeling and Motion Planning**|机器人自模型是机器人物理形态的任务不可知表示，在没有经典几何运动学模型的情况下，可用于运动规划任务。特别是，当后者难以设计或机器人的运动学发生意外变化时，人类自由的自我建模是真正自主智能体的必要特征。在这项工作中，我们利用神经场使机器人能够将其运动学自建模为仅从带有相机姿势和配置的2D图像中学习的神经隐式查询模型。这使得比依赖于深度图像或几何知识的现有方法具有更大的适用性。为此，除了课程数据采样策略外，我们还提出了一种新的基于编码器的神经密度场架构，用于高自由度（DOF）条件下的动态对象中心场景。在7自由度机器人测试装置中，学习的自模型实现了机器人工作空间尺寸2%的倒角-L2距离。作为一个示例性的下游应用程序，我们展示了该模型在运动规划任务中的能力。 et.al.|[2310.03624](http://arxiv.org/abs/2310.03624)|null|
|**2023-10-02**|**Neural Processing of Tri-Plane Hybrid Neural Fields**|在用于存储和通信3D数据的神经场的吸引人的特性的驱动下，直接处理它们以解决分类和零件分割等任务的问题已经出现，并在最近的工作中进行了研究。早期的方法使用由在整个数据集上训练的共享网络参数化的神经场，实现了良好的任务性能，但牺牲了重建质量。为了改进后者，后来的方法侧重于参数化为大型多层感知器（MLP）的单个神经场，然而，由于权重空间的高维性、固有的权重空间对称性和对随机初始化的敏感性，这些神经元场的处理具有挑战性。因此，结果明显不如通过处理显式表示（例如点云或网格）所获得的结果。与此同时，混合表示，特别是基于三平面的混合表示，已经成为实现神经场的一种更有效的替代方案，但其直接处理尚未得到研究。在本文中，我们证明了三平面离散数据结构编码了丰富的信息，标准的深度学习机器可以有效地处理这些信息。我们定义了一个广泛的基准，涵盖了一组不同的字段，如占用率、有符号/无符号距离，以及首次定义的辐射字段。在处理具有相同重建质量的字段时，我们实现的任务性能远远优于处理大型MLP的框架，并且首次几乎与处理显式表示的架构不相上下。 et.al.|[2310.01140](http://arxiv.org/abs/2310.01140)|**[link](https://github.com/CVLAB-Unibo/triplane_processing)**|
|**2023-09-27**|**Neural Acoustic Context Field: Rendering Realistic Room Impulse Response With Neural Fields**|房间脉冲响应（RIR）测量声音在环境中的传播，对于合成给定环境下的高保真音频至关重要。一些先前的工作已经提出将RIR表示为声音发射器和接收器位置的神经场函数。然而，这些方法没有充分考虑音频场景的声学特性，导致性能不令人满意。这封信提出了一种新的神经声学上下文场方法，称为NACF，通过利用多个声学上下文（如几何结构、材料特性和空间信息）来参数化音频场景。在RIR的独特性质，即时间不光滑性和单调能量衰减的驱动下，我们设计了一个时间相关模块和多尺度能量衰减准则。实验结果表明，NACF的性能显著优于现有的基于字段的方法。请访问我们的项目页面了解更多定性结果。 et.al.|[2309.15977](http://arxiv.org/abs/2309.15977)|null|
|**2023-09-27**|**SHACIRA: Scalable HAsh-grid Compression for Implicit Neural Representations**|隐式神经表示（INR）或神经场已成为编码多媒体信号（如图像和辐射场）同时保持高质量的流行框架。最近，Instant NGP提出的可学习特征网格通过用特征向量的多分辨率查找表和更小的神经网络取代大型神经网络，在训练和INR采样方面实现了显著的加速。然而，这些功能网格是以大量内存消耗为代价的，这可能是存储和流应用程序的瓶颈。在这项工作中，我们提出了SHACIRA，这是一个简单而有效的任务无关框架，用于压缩这种特征网格，而不需要额外的事后修剪/量化阶段。我们用量化的潜在权重对特征网格进行重新参数化，并在潜在空间中应用熵正则化，以在各个领域实现高水平的压缩。在由图像、视频和辐射场组成的不同数据集上的定量和定性结果表明，我们的方法优于现有的INR方法，而不需要任何大型数据集或特定领域的启发式方法。我们的项目页面可在http://shacira.github.io。 et.al.|[2309.15848](http://arxiv.org/abs/2309.15848)|null|

<p align=right>(<a href=#updated-on-20231101>back to top</a>)</p>

[contributors-shield]: https://img.shields.io/github/contributors/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[contributors-url]: https://github.com/Vincentqyw/cv-arxiv-daily/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[forks-url]: https://github.com/Vincentqyw/cv-arxiv-daily/network/members
[stars-shield]: https://img.shields.io/github/stars/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[stars-url]: https://github.com/Vincentqyw/cv-arxiv-daily/stargazers
[issues-shield]: https://img.shields.io/github/issues/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[issues-url]: https://github.com/Vincentqyw/cv-arxiv-daily/issues

