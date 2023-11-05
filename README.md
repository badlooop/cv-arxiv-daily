[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]

## Updated on 2023.11.05
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
|**2023-11-02**|**Novel View Synthesis from a Single RGBD Image for Indoor Scenes**|在本文中，我们提出了一种从单个RGBD（红-绿-蓝深度）输入合成新视图图像的方法。新颖视图合成（NVS）是一项有趣的计算机视觉任务，具有广泛的应用。使用多个图像的方法已经得到了很好的研究，示例性方法包括训练特定场景的神经辐射场（NeRF），或利用多视图立体（MVS）和3D渲染管道。然而，两者都是计算密集型的，或者在不同的场景中不可推广，限制了它们的实用价值。相反，嵌入RGBD图像中的深度信息从单一视角解锁了3D潜力，简化了NVS。紧凑、价格合理的立体相机，甚至智能手机等现代设备中的激光雷达的广泛可用性，使捕捉RGBD图像比以往任何时候都更容易。在我们的方法中，我们将RGBD图像转换为点云，并从不同的角度对其进行渲染，然后将NVS任务公式化为图像翻译问题。我们利用生成对抗性网络对渲染图像进行风格转换，获得了类似于从新视角拍摄的照片的结果。我们探索了使用CycleGAN的无监督学习和使用Pix2Pix的监督学习，并展示了定性结果。我们的方法避开了传统多图像技术的局限性，在NVS中的实际实时应用中具有重要的前景。 et.al.|[2311.01065](http://arxiv.org/abs/2311.01065)|null|
|**2023-11-01**|**Neural Implicit Field Editing Considering Object-environment Interaction**|基于神经隐场的三维场景编辑方法得到了广泛的关注。它在三维编辑任务中取得了优异的效果。然而，现有的方法通常将对象和场景环境之间的交互融合在一起。场景外观（如阴影）的更改无法在渲染视图中显示。在本文中，我们提出了一种对象和场景环境交互感知（OSI感知）系统，这是一种考虑对象和场景-环境交互的新型双流神经渲染系统。为了从混合汤中获得照明条件，该系统采用内分解方法成功地分离了物体与场景环境之间的相互作用。为了研究对象级编辑任务对场景外观的相应变化，我们引入了一种深度图引导的场景修复方法和点匹配策略的阴影渲染方法。大量实验表明，我们的新型流水线在场景编辑任务中产生了合理的外观变化。在新的视图合成任务中，它还实现了具有竞争力的渲染质量。 et.al.|[2311.00425](http://arxiv.org/abs/2311.00425)|null|
|**2023-10-31**|**An Implementation of Multimodal Fusion System for Intelligent Digital Human Generation**|随着人工智能（AI）的快速发展，数字人越来越受到关注，并有望在多个行业实现广泛应用。那么，现有的大多数数字人仍然依赖于设计师的手动建模，这是一个繁琐的过程，而且开发周期很长。因此，面对数字人的崛起，迫切需要一个与人工智能相结合的数字人生成系统来提高开发效率。本文提出了一种多模态融合的智能数字人生成系统的实现方案。具体地，将文本、语音和图像作为输入，并使用大语言模型（LLM）、声纹提取和文本到语音转换技术来合成交互式语音。然后对输入图像进行年龄变换，并选择合适的图像作为驾驶图像。然后，通过数字人驱动、新颖的视图合成和智能着装技术，实现了数字人视频内容的修改和生成。最后，我们通过风格转换、超分辨率和质量评估来增强用户体验。实验结果表明，该系统能够有效地实现数字人的生成。相关代码发布于https://github.com/zyj-2000/CUMT_2D_PhotoSpeaker. et.al.|[2310.20251](http://arxiv.org/abs/2310.20251)|**[link](https://github.com/zyj-2000/cumt_2d_photospeaker)**|
|**2023-10-30**|**CustomNet: Zero-shot Object Customization with Variable-Viewpoints in Text-to-Image Diffusion Models**|将定制对象合并到图像生成中是文本到图像生成的一个有吸引力的特征。然而，现有的基于优化和基于编码器的方法受到诸如耗时优化、身份保存不足和普遍的复制粘贴效应等缺点的阻碍。为了克服这些限制，我们引入了CustomNet，这是一种新的对象定制方法，它将3D新视图合成功能明确地结合到对象定制过程中。这种集成有助于调整空间位置关系和视点，产生不同的输出，同时有效地保持对象身份。此外，我们引入了精细的设计，通过文本描述或特定的用户定义图像实现位置控制和灵活的背景控制，克服了现有3D新颖视图合成方法的局限性。我们进一步利用数据集构建管道，可以更好地处理真实世界的对象和复杂的背景。有了这些设计，我们的方法方便了零样本对象的定制，而无需测试时间优化，可以同时控制视点、位置和背景。因此，我们的CustomNet确保增强身份保护，并产生多样化、和谐的输出。 et.al.|[2310.19784](http://arxiv.org/abs/2310.19784)|null|
|**2023-10-31**|**DynPoint: Dynamic Neural Point For View Synthesis**|神经辐射场的引入极大地提高了单目视频视图合成的有效性。然而，现有算法在处理不受控制或冗长的场景时面临困难，并且需要针对每个新场景的大量训练时间。为了解决这些限制，我们提出了DynPoint，这是一种算法，旨在促进无约束单眼视频的新视图的快速合成。DynPoint不是将整个场景信息编码为潜在表示，而是专注于预测相邻帧之间的显式3D对应关系，以实现信息聚合。具体地，这种对应预测是通过估计帧之间一致的深度和场景流信息来实现的。随后，通过构建分层神经点云，利用所获取的对应关系将信息从多个参考帧聚合到目标帧。所得到的框架使得能够对目标帧的期望视图进行快速且准确的视图合成。所获得的实验结果表明，与先前的方法相比，我们提出的方法大大加快了训练时间，通常是一个数量级，同时产生了可比的结果。此外，我们的方法在处理长持续时间视频时表现出强大的鲁棒性，而无需学习视频内容的规范表示。 et.al.|[2310.18999](http://arxiv.org/abs/2310.18999)|null|
|**2023-10-27**|**ZeroNVS: Zero-Shot 360-Degree View Synthesis from a Single Real Image**|我们介绍了一种3D感知扩散模型ZeroNVS，用于野外场景的单图像新颖视图合成。虽然现有的方法是为具有遮罩背景的单个对象设计的，但我们提出了新的技术来解决具有复杂背景的野外多对象场景带来的挑战。具体来说，我们在捕捉以对象为中心、室内和室外场景的混合数据源上训练生成先验。为了解决深度尺度模糊等数据混合问题，我们提出了一种新的相机条件参数化和归一化方案。此外，我们观察到，在360度场景的提取过程中，分数提取采样（SDS）倾向于截断复杂背景的分布，并提出了“SDS锚定”来提高合成新视图的多样性。我们的模型在零样本设置中的DTU数据集上的LPIPS中设置了新的最先进的结果，甚至优于专门在DTU上训练的方法。我们进一步将具有挑战性的Mip-NeRF 360数据集作为单图像新视图合成的新基准，并在该设置中展示了强大的性能。我们的代码和数据位于http://kylesargent.github.io/zeronvs/ et.al.|[2310.17994](http://arxiv.org/abs/2310.17994)|null|
|**2023-10-27**|**Reconstructive Latent-Space Neural Radiance Fields for Efficient 3D Scene Representations**|神经辐射场（NeRF）已被证明是强大的3D表示，能够对复杂场景进行高质量的新颖视图合成。虽然NeRF已经应用于图形、视觉和机器人，但渲染速度慢和特有的视觉伪影问题阻碍了在许多用例中的采用。在这项工作中，我们研究了将自动编码器（AE）与NeRF相结合，其中潜在特征（而不是颜色）被渲染，然后进行卷积解码。由此产生的潜在空间NeRF可以产生比标准颜色空间NeRF质量更高的新颖视图，因为AE可以校正某些视觉伪影，同时渲染速度快三倍以上。我们的工作与提高NeRF效率的其他技术正交。此外，我们可以通过缩小AE架构来控制效率和图像质量之间的权衡，在性能下降很小的情况下实现13倍以上的渲染速度。我们希望我们的方法能够为下游任务形成高效但高保真的3D场景表示的基础，尤其是在保持可微性很有用的情况下，就像在许多需要持续学习的机器人场景中一样。 et.al.|[2310.17880](http://arxiv.org/abs/2310.17880)|null|
|**2023-10-26**|**LightSpeed: Light and Fast Neural Light Fields on Mobile Devices**|由于计算能力和存储空间有限，移动设备上的实时新视图图像合成是令人望而却步的。在移动设备上使用体积渲染方法（如NeRF及其衍生物）是不合适的，因为体积渲染的计算成本很高。另一方面，神经光场表示的最新进展在移动设备上显示出了有希望的实时视图合成结果。神经光场方法学习从光线表示到像素颜色的直接映射。光线表示的当前选择是分层光线采样或Plucker坐标，忽略了经典的光板（两平面）表示，这是在光场视图之间插值的首选表示。在这项工作中，我们发现使用光板表示是学习神经光场的有效表示。更重要的是，它是一种较低维的光线表示，使我们能够使用训练和渲染速度明显更快的特征网格来学习4D光线空间。尽管主要是为正面视图设计的，但我们表明，光板表示可以使用分而治之的策略进一步扩展到非正面场景。与以前的光场方法相比，我们的方法提供了卓越的渲染质量，并显著改善了渲染质量和速度之间的平衡。 et.al.|[2310.16832](http://arxiv.org/abs/2310.16832)|**[link](https://github.com/lightspeed-r2l/lightspeed)**|
|**2023-10-28**|**PERF: Panoramic Neural Radiance Field from a Single Panorama**|神经辐射场（NeRF）在给定多视点图像的新视点合成方面取得了实质性进展。最近，一些工作试图从具有3D先验的单个图像中训练NeRF。它们主要关注具有少量遮挡的有限视场，这极大地限制了它们在具有大尺寸遮挡的真实世界360度全景场景中的可扩展性。在本文中，我们提出了PERF，这是一种360度新颖的视图合成框架，它从单个全景训练全景神经辐射场。值得注意的是，PERF允许在复杂场景中进行3D漫游，而无需昂贵且乏味的图像采集。为了实现这一目标，我们提出了一种新的协作RGBD修复方法和一种渐进的修复和擦除方法，以将360度2D场景提升为3D场景。具体而言，我们首先预测全景深度图作为给定单个全景的初始化，并使用体绘制重建可见的3D区域。然后，我们在NeRF中引入了一种协作的RGBD修复方法，用于从随机视图中完成RGB图像和深度图，该方法源自RGB稳定扩散模型和单目深度估计器。最后，我们介绍了一种修复和擦除策略，以避免新采样视图和参考视图之间的几何不一致。这两个组件在统一的优化框架中集成到NeRF的学习中，并取得了有希望的结果。在Replica和野外新数据集PERF上进行的大量实验证明了我们的PERF优于最先进的方法。我们的PERF可以广泛用于真实世界的应用，如全景到3D、文本到3D和3D场景风格化应用。项目页面和代码可在https://perf-project.github.io/和https://github.com/perf-project/PeRF. et.al.|[2310.16831](http://arxiv.org/abs/2310.16831)|**[link](https://github.com/perf-project/PeRF)**|
|**2023-10-25**|**Open-NeRF: Towards Open Vocabulary NeRF Decomposition**|在本文中，我们解决了从开放词汇中将神经辐射场（NeRF）分解为对象的挑战，这是三维重建和视图合成中对象操作的关键任务。当前的NeRF分解技术涉及处理开放词汇查询的灵活性和3D分割的准确性之间的权衡。我们提出了开放词汇嵌入式神经辐射场（Open NeRF），它利用了大规模现成的分割模型，如Segment Anything Model（SAM），并引入了一种具有分层嵌入的集成和提取范式，以实现开放词汇查询的灵活性和3D分割的准确性。Open NeRF首先利用大规模基础模型从不同的角度生成分层2D掩模方案。然后，通过跟踪方法将这些建议对齐，并将其集成在3D空间中，随后将其提取到3D领域中。这一过程确保了从不同角度对对象的一致识别和粒度，即使在涉及遮挡和模糊特征的具有挑战性的场景中也是如此。我们的实验结果表明，在开放词汇场景中，所提出的Open NeRF优于最先进的方法，如LERF\cite{LERF}和FFD\cite{FFD}。Open NeRF为NeRF分解提供了一个很有前途的解决方案，以开放词汇查询为指导，在开放世界3D场景中实现机器人和视觉语言交互的新应用。 et.al.|[2310.16383](http://arxiv.org/abs/2310.16383)|null|

<p align=right>(<a href=#updated-on-20231105>back to top</a>)</p>

## 3D Reconstruction

|Publish Date|Title|Abstract|PDF|Code|
|---|---|---|---|---|
|**2023-11-02**|**CADSim: Robust and Scalable in-the-wild 3D Reconstruction for Controllable Sensor Simulation**|逼真的模拟是实现%自动驾驶汽车安全和可扩展开发的关键。一个核心组件是模拟传感器，以便可以在模拟中测试整个自主系统。传感器模拟包括对具有高质量外观和铰接几何结构的交通参与者（如车辆）进行建模，并实时渲染。自动驾驶行业通常雇佣艺术家来构建这些资产。然而，这是昂贵的，缓慢的，并且可能不能反映现实。相反，根据野外收集的传感器数据自动重建资产将为生成具有良好真实世界覆盖率的多样化大型集合提供更好的途径。然而，由于传感器数据的稀疏性和噪声，目前的重建方法在野外传感器数据中举步维艰。为了解决这些问题，我们提出了CADSim，它通过一小组CAD模型将零件感知对象类先验与可微分渲染相结合，以自动重建具有高质量外观的车辆几何结构，包括铰接车轮。我们的实验表明，与现有方法相比，我们的方法从稀疏数据中恢复了更准确的形状。重要的是，它还能有效地训练和渲染。我们在几个应用中展示了我们重建的车辆，包括对自主感知系统的精确测试。 et.al.|[2311.01447](http://arxiv.org/abs/2311.01447)|null|
|**2023-11-02**|**Look at Robot Base Once: Hand-Eye Calibration with Point Clouds of Robot Base Leveraging Learning-Based 3D Vision**|手眼校准作为基于视觉的机器人系统的一项基本任务，旨在估计摄像机坐标系与机器人法兰之间的变换矩阵。大多数手眼校准方法都依赖于外部标记或人类辅助。我们提出了Look at Robot Base Once（LRBO），这是一种新的方法，可以在没有外部校准对象或人类支持的情况下，通过机器人底座来解决手眼校准问题。利用机器人底座的点云，建立了从相机坐标系到机器人底座的变换矩阵，即I=AXB。为此，我们利用基于学习的三维检测和配准算法来估计机器人基座的位置和方向。通过基于地面实况的评估对该方法的稳健性和准确性进行了量化，并将准确性结果与其他基于三维视觉的校准方法进行了比较。为了评估我们方法的可行性，我们在不同的关节配置和实验组中使用低成本的结构光扫描仪进行了实验。根据实验结果，所提出的手眼校准方法实现了0.930mm的平移偏差和0.265度的旋转偏差。此外，3D重建实验显示旋转误差为0.994度，位置误差为1.697毫米。此外，我们的方法具有在1秒内完成的潜力，与其他3D手眼校准方法相比，这是最快的。代码发布于github.com/leihui6/LRBO。 et.al.|[2311.01335](http://arxiv.org/abs/2311.01335)|**[link](https://github.com/leihui6/lrbo)**|
|**2023-11-02**|**Joint 3D Shape and Motion Estimation from Rolling Shutter Light-Field Images**|在本文中，我们提出了一种方法来解决由配备滚动快门传感器的光场相机捕获的单个图像进行场景的3D重建的问题。我们的方法利用了光场中存在的3D信息线索和滚动快门效果提供的运动信息。我们为该传感器的成像过程提出了一个通用模型，并提出了一种两阶段算法，该算法在运动形状束调整估计策略中考虑相机的位置和运动时，最大限度地减少了重新投影误差。因此，我们提供了一个即时三维形状和姿态以及速度传感范例。据我们所知，这是第一次利用这种类型的传感器实现这一目的的研究。我们还提出了一个新的基准数据集，该数据集由显示卷帘效果的不同光场组成，可作为改进评估和跟踪该领域进展的共同基础。我们通过针对不同场景和运动类型进行的几个实验来证明我们的方法的有效性和优势。源代码和数据集可在以下位置公开获取：https://github.com/ICB-Vision-AI/RSLF et.al.|[2311.01292](http://arxiv.org/abs/2311.01292)|null|
|**2023-11-01**|**DEFN: Dual-Encoder Fourier Group Harmonics Network for Three-Dimensional Macular Hole Reconstruction with Stochastic Retinal Defect Augmentation and Dynamic Weight Composition**|黄斑裂孔的空间和定量参数对诊断、手术选择和术后监测至关重要。黄斑的诊断和治疗在很大程度上依赖于空间和定量数据，但这些数据的稀缺阻碍了深度学习技术在有效分割和实时3D重建方面的进展。为了应对这一挑战，我们收集了世界上最大的黄斑裂孔数据集，用于黄斑裂孔增强的视网膜OCT（ROME-3914）和用于视网膜分割的综合档案（CARS-30k），这两个数据集都经过了专业注释。此外，我们还开发了一个创新的3D分割网络，即双编码器FuGH网络（DEFN），它集成了三个创新模块：傅立叶群谐波（FuGH）、简化三维空间注意力（S3DSA）和谐波挤压和激励模块（HSE）。这三个模块协同过滤噪声，降低计算复杂度，强调细节特征，增强网络的表示能力。我们还提出了一种新的数据增强方法，随机视网膜缺陷注入（SRDI）和网络优化策略DynamicWeightCompose（DWC），以进一步提高DEFN的性能。与13个基线相比，我们的DEFN显示出最佳性能。我们还提供精确的3D视网膜重建和定量指标，为眼科医生带来革命性的诊断和治疗决策工具，有望彻底重塑难以治疗的黄斑变性的诊断和处理模式。源代码可在以下位置公开获取：https://github.com/IIPL-HangzhouDianUniversity/DEFN-Pytorch. et.al.|[2311.00483](http://arxiv.org/abs/2311.00483)|**[link](https://github.com/iipl-hangzhoudianziuniversity/defn-pytorch)**|
|**2023-11-01**|**Single-view 3D Scene Reconstruction with High-fidelity Shape and Texture**|由于现有方法的局限性，从单视图图像重建详细的3D场景仍然是一项具有挑战性的任务，这些方法主要关注几何形状恢复，忽略对象外观和精细形状细节。为了应对这些挑战，我们提出了一种新的框架，用于从单视图图像中同时高保真地恢复对象形状和纹理。我们的方法利用所提出的单视图神经隐式形状和辐射场（SSR）表示来利用显式3D形状监督和颜色、深度和表面法线图像的体积渲染。为了克服部分观察下的形状-外观模糊性，我们引入了一个包含3D和2D监督的两阶段学习课程。我们的框架的一个显著特点是能够生成细粒度纹理网格，同时将渲染功能无缝集成到单视图3D重建模型中。这种集成不仅使3D-FRONT和Pix3D数据集上的纹理3D对象重建分别提高了27.7%和11.6%，而且还支持从新视点渲染图像。除了单个对象之外，我们的方法还有助于将对象级表示组合为灵活的场景表示，从而实现整体场景理解和3D场景编辑等应用。我们进行了大量的实验来证明我们的方法的有效性。 et.al.|[2311.00457](http://arxiv.org/abs/2311.00457)|null|
|**2023-10-31**|**Joint Depth Prediction and Semantic Segmentation with Multi-View SAM**|针对单目图像，对联合深度和分割预测的多任务方法进行了深入研究。然而，来自单个视图的预测本质上是有限的，而在许多机器人应用中可以使用多个视图。另一方面，基于视频的全3D方法需要大量的帧来执行重建和分割。通过这项工作，我们提出了一种用于深度预测的多视图立体（MVS）技术，该技术得益于分段任意模型（SAM）丰富的语义特征。这种增强的深度预测反过来又作为我们基于Transformer的语义分割解码器的提示。我们在ScanNet数据集的定量和定性研究中报告了这两项任务的互利性。我们的方法始终优于单任务MVS和分割模型，以及多任务单目方法。 et.al.|[2311.00134](http://arxiv.org/abs/2311.00134)|null|
|**2023-10-31**|**Deep Compressed Learning for 3D Seismic Inversion**|我们考虑了使用极少量震源从叠前数据进行三维地震反演的问题。所提出的解决方案基于压缩感知和机器学习框架的组合，称为压缩学习。该解决方案联合优化了由深度卷积神经网络（DCNN）实现的降维算子和3D反演编码器-解码器。降维是通过学习稀疏二进制传感层来实现的，该层选择可用源的一个子集，然后将所选数据馈送到DCNN以完成回归任务。端到端的学习过程将训练期间使用的地震记录的数量减少了一个数量级，同时保持了与使用整个数据集获得的3D重建质量相当的三维重建质量。 et.al.|[2311.00107](http://arxiv.org/abs/2311.00107)|null|
|**2023-10-31**|**Refined Equivalent Pinhole Model for Large-scale 3D Reconstruction from Spaceborne CCD Imagery**|在这项研究中，我们提出了一个用于线阵电荷耦合器件（CCD）卫星图像的大规模地表重建管道。虽然主流的基于卫星图像的重建方法表现得非常好，但有理函数模型（RFM）受到一些限制。例如，RFM没有严格的物理解释，与针孔成像模型有很大不同；因此，它不能直接应用于基于学习的三维重建网络和计算机视觉中更新颖的重建管道。因此，在本研究中，我们介绍了一种方法，其中RFM等效于针孔相机模型（PCM），这意味着使用针孔相机的内部和外部参数，而不是有理多项式系数参数。然后，我们首次推导出该等效针孔模型的误差公式，证明了图像大小对重建精度的影响。此外，我们提出了一个多项式图像细化模型，通过最小二乘法最小化等效误差。实验使用四个图像数据集进行：WHU-TLC、DFC2019、ISPRS-ZY3和GF7。结果表明，重建精度与图像大小成正比。我们的多项式图像细化模型显著提高了重建的准确性和完整性，并对更大尺度的图像实现了更显著的改进。 et.al.|[2310.20117](http://arxiv.org/abs/2310.20117)|null|
|**2023-10-29**|**3DMiner: Discovering Shapes from Large-Scale Unannotated Image Datasets**|我们介绍了3DMiner——一种从具有挑战性的大规模未标记图像数据集中挖掘3D形状的管道。与其他无监督的3D重建方法不同，我们假设，在一个足够大的数据集中，必须存在形状相似但背景、纹理和视点不同的对象图像。我们的方法利用学习自监督图像表示的最新进展，对具有几何相似形状的图像进行聚类，并找到它们之间的常见图像对应关系。然后，我们利用这些对应关系来获得粗略的相机估计，作为束调整的初始化。最后，对于每个图像聚类，我们应用渐进束调整重建方法来学习表示底层形状的神经占据场。我们表明，该程序对之前步骤中引入的几种类型的错误（例如，错误的相机姿势、包含不同形状的图像等）是稳健的，使我们能够获得野外图像的形状和姿势注释。当使用Pix3D椅子的图像时，我们的方法能够在定量和定性方面产生比最先进的无监督3D重建技术更好的结果。此外，我们还展示了3DMiner如何通过重建LAION-5B数据集中图像中的形状来应用于野外数据。项目页面：https://ttchengab.github.io/3dminerOfficial et.al.|[2310.19188](http://arxiv.org/abs/2310.19188)|null|
|**2023-10-29**|**Towards Generalized Multi-stage Clustering: Multi-view Self-distillation**|现有的多阶段聚类方法从多个视图中独立地学习显著特征，然后执行聚类任务。特别是，多视图集群（MVC）在多视图或多模式场景中引起了很多关注。MVC旨在从多个视图中探索通用语义和伪标签，并以自监督的方式进行聚类。然而，受噪声数据和特征学习不足的限制，这种聚类范式会产生过于自信的伪标签，错误地引导模型产生不准确的预测。因此，希望有一种方法可以在多阶段聚类中纠正这种伪标签错误行为，以避免偏差累积。为了缓解过度自信的伪标签的影响，提高模型的泛化能力，本文提出了一种新的多阶段深度MVC框架，引入多视图自蒸馏（DistilMVC）来提取标签分布的暗知识。具体来说，在不同层次的特征子空间中，我们通过对比学习来探索多个视图的共同语义，并通过最大化视图之间的相互信息来获得伪标签。此外，教师网络负责将伪标签提取到暗知识中，监督学生网络并提高其预测能力以增强鲁棒性。在真实世界的多视图数据集上进行的大量实验表明，我们的方法比最先进的方法具有更好的聚类性能。 et.al.|[2310.18890](http://arxiv.org/abs/2310.18890)|null|

<p align=right>(<a href=#updated-on-20231105>back to top</a>)</p>

## Diffusion

|Publish Date|Title|Abstract|PDF|Code|
|---|---|---|---|---|
|**2023-11-02**|**Time Series Anomaly Detection using Diffusion-based Models**|扩散模型最近被用于图像中的异常检测（AD）。在本文中，我们研究了它们是否也可以用于多变量时间序列（MTS）上的AD。我们测试了两个基于扩散的模型，并将它们与几个强神经基线进行了比较。我们还通过计算ROCK-AUC度量扩展了PA%K协议，该度量对检测阈值和正确检测点的比率K都是不可知的。我们的模型在合成数据集上优于基线，在真实世界的数据集上具有竞争力，说明了基于扩散的方法在多变量时间序列中用于AD的潜力。 et.al.|[2311.01452](http://arxiv.org/abs/2311.01452)|**[link](https://github.com/fbrad/diffusionae)**|
|**2023-11-02**|**Filaments of The Slime Mold Cosmic Web And How They Affect Galaxy Evolution**|我们提出了一种利用IllustrisTNG（TNG100）宇宙学模拟识别宇宙网状细丝的新方法，并研究了细丝对星系的影响。我们比较了Delaunay Tessellation field Estimator（DTFE）和Monte Carlo Physarum Machine（MCPM）在DisPerSE结构识别框架中对宇宙密度场估计的使用。与基于DTFE的重建相比，基于MCPM的重建以更高的保真度识别细丝，发现更多的低突起/扩散细丝，并更好地追踪真实的底层物质分布。使用我们新的细丝目录，我们发现大多数星系位于细丝脊的1.5-2.5 Mpc范围内，比恒星形成率的中值和星系气体分数的中值与最近细丝的距离变化不大。相反，我们引入了细丝线密度，｛\ Sigma｝fil（MCPM），作为局部细丝段每单位长度的总MCPM超密度，并发现该参数是银河系气体供应和猝灭的一个优越预测因子。我们的结果表明，在z<=1的高线密度细丝附近，大多数星系都被猝灭，气体贫乏。在z=0时，log（M*/Msun）>10.5星系的猝灭主要由质量驱动，而低质量星系则受到细丝密度的显著影响。在高线密度细丝中，卫星被强烈淬火，而在z<=0.5时，中心星的恒星形成减少，但气体成分减少。我们讨论了将我们的新细丝识别方法应用于SDSS、DESI、斯巴鲁PFS等星系调查的前景，以阐明大尺度结构对星系形成的影响。 et.al.|[2311.01443](http://arxiv.org/abs/2311.01443)|null|
|**2023-11-02**|**Functional inequalities for a family of infinite-dimensional diffusions with degenerate noise**|对于具有退化噪声的无穷维扩散族，我们在方程的有限维投影上发展了一个修正的 $\Gamma$演算，以产生可以缩放到无穷维的显式函数不等式。$\Gamma$ 算子的选择在我们的上下文中似乎是规范的，因为估计仅取决于诱导控制距离。我们将一般分析应用于许多例子，探索平稳分布的拟不变性和唯一性的含义。 et.al.|[2311.01440](http://arxiv.org/abs/2311.01440)|null|
|**2023-11-02**|**Constrained-Context Conditional Diffusion Models for Imitation Learning**|离线模仿学习（IL）是学习视觉运动技能的一种强大范式，尤其是在高精度操作任务中。然而，IL方法容易产生虚假的相关性——表达模型可能专注于与行动预测无关的干扰因素——因此在现实世界的部署中是脆弱的。先前的方法已经通过探索不同的模型体系结构和动作表示来解决这一挑战。然而，没有人能够在样本效率、对干扰的鲁棒性和解决具有复杂动作空间的高精度操作任务之间取得平衡。为此，我们提出了 $\textbf｛C｝$onstrained-$\textbf{C｝$ontext$\textbf｛C}$conditional$\textbf｛D｝$diffusion$\textbf｛M｝$ model（C3DM），这是一种用于解决6-DoF机器人操纵任务的扩散模型策略，具有高精度和忽略干扰的能力。C3DM的一个关键组成部分是固定步骤，它帮助动作去噪器专注于预测动作周围的任务相关区域，同时忽略上下文中的干扰因素。我们的经验表明，C3DM能够在从桌面操作到工业装备的一系列任务中持续实现高成功率，这些任务需要不同水平的精度和对干扰器的鲁棒性。有关详细信息，请访问https://sites.google.com/view/c3dm-imitation-learning et.al.|[2311.01419](http://arxiv.org/abs/2311.01419)|null|
|**2023-11-02**|**The Blessing of Randomness: SDE Beats ODE in General Diffusion-based Image Editing**|我们提出了一种基于扩散的图像编辑的统一概率公式，其中潜在变量以特定任务的方式进行编辑，并且通常偏离由原始随机或常微分方程（SDE或ODE）引起的相应边缘分布。相反，它定义了相应的SDE或ODE进行编辑。在该公式中，我们证明了随着时间接近零，两个SDE的边缘分布之间的Kullback-Leibler散度逐渐减小，而ODE的边缘分布则保持不变，这表明了SDE在图像编辑中的前景。受其启发，我们为各种任务中广泛使用的ODE基线提供了SDE对应物，包括修复和图像到图像的翻译，其中SDE显示出一致且实质性的改进。此外，我们提出了SDE拖动——一种基于SDE公式的简单而有效的基于点的内容拖动方法。我们建立了一个具有挑战性的基准（称为DragBench），使用开放集的自然、艺术和人工智能生成的图像进行评估。DragBench上的一项用户研究表明，SDE Drag显著优于我们的ODE基线、现有的基于扩散的方法和著名的DragGAN。我们的结果证明了SDE在图像编辑中的优越性和通用性，并突破了基于扩散的编辑方法的界限。 et.al.|[2311.01410](http://arxiv.org/abs/2311.01410)|null|
|**2023-11-02**|**Machine Learning Design of Perovskite Catalytic Properties**|发现有效催化氧还原和析氧反应的新材料对于促进固体氧化物燃料电池和电解槽（SOFC/SOEC）技术的广泛采用至关重要。在这里，我们开发了机器学习（ML）模型来预测对SOFC/SOEC应用至关重要的钙钛矿催化性能，包括氧表面交换、氧扩散率和面积比电阻（ASR）。这些模型基于琐碎的元素特征计算，比基于从头计算衍生特征的最佳模型更准确、速度更快，有可能消除基于描述符的筛选中从头计算的需要。我们的ASR模型能够进行与温度相关的预测，具有经过良好校准的不确定性估计和在线可访问性。时间交叉验证的使用表明，我们的模型在首次发现有前景的新材料之前能够有效地发现这些材料，这表明我们的模型可以做出有意义的预测。使用SHapley加性ExPlanations（SHAP）方法，我们详细讨论了用于ML特性预测的模型特征化的不同方法。最后，我们使用我们的模型筛选了1900多万钙钛矿，以开发一份有前景的廉价、富含地球、稳定和高性能材料的清单，并发现一些顶级材料含有探索较少的元素（如K、Bi、Y、Ni、Cu）的混合物，值得更详细地探索。 et.al.|[2311.01401](http://arxiv.org/abs/2311.01401)|**[link](https://github.com/uw-cmg/asr_model)**|
|**2023-11-02**|**Sim2Real Bilevel Adaptation for Object Surface Classification using Vision-Based Tactile Sensors**|在本文中，我们解决了基于视觉的触觉传感器领域中用于对物体表面进行分类的Sim2Real缺口。我们使用通过DIGIT传感器从未标记的日常物体中随机收集的相对较小的真实世界图像数据集来训练扩散模型，以弥补这一差距。随后，我们使用模拟器通过从YCB模型集中均匀采样物体表面来生成图像。然后使用扩散模型将这些模拟图像转换到真实域中，并自动标记以训练分类器。在这次训练中，我们使用对抗性程序进一步调整了两个领域的特征。我们的评估是在从一组10个3D打印的YCB对象中获得的触觉图像数据集上进行的。结果显示，总准确率为81.9%，与仅在模拟图像上训练的分类器实现的34.7%相比，有了显著提高。这表明了我们方法的有效性。我们在触觉数据的6D物体姿态估计任务中使用分类器进一步验证了我们的方法。 et.al.|[2311.01380](http://arxiv.org/abs/2311.01380)|**[link](https://github.com/hsp-iit/sim2real-surface-classification)**|
|**2023-11-02**|**DP-Mix: Mixup-based Data Augmentation for Differentially Private Learning**|数据增强技术，如简单的图像转换和组合，在提高计算机视觉模型的泛化能力方面非常有效，尤其是在训练数据有限的情况下。然而，由于后者固有的假设，即每个训练图像对学习模型的贡献是有限的，因此这种技术从根本上与差异私人学习方法不兼容。在本文中，我们研究了为什么多样本数据增强技术的幼稚应用，如混合，未能获得良好的性能，并提出了两种新的数据增强技术，专门针对差异私有学习的约束而设计。我们的第一种技术DP-Mix_Self通过对自增强数据执行混合，在一系列数据集和设置中实现了SoTA分类性能。我们的第二种技术DP-Mix_Diff通过将来自预先训练的扩散模型的合成数据结合到混合过程中，进一步提高了性能。我们在https://github.com/wenxuan-Bao/DP-Mix. et.al.|[2311.01295](http://arxiv.org/abs/2311.01295)|**[link](https://github.com/wenxuan-bao/dp-mix)**|
|**2023-11-02**|**Unraveling Diffusion in Fusion Plasma: A Case Study of In Situ Processing and Particle Sorting**|这项工作开始了研究磁约束聚变中某一扩散过程的原位处理能力。这种扩散过程涉及可能逃脱约束的等离子体粒子。这种粒子将大量能量从托卡马克内部燃烧的等离子体携带到分流器，并损坏分流器板。由于颗粒扩散过程的快速变化性质，这项研究需要原位处理。然而，原位处理方法具有挑战性，因为要为扩散计算保留的数据量随着时间的推移而增加，而不像在其他原位处理情况下，要处理的数据量随时间的推移是恒定的。在这里，我们报告了我们为控制内存使用所做的初步努力，同时确保及时完成必要的分析任务。与早期在模拟代码中直接计算相同扩散位移的天真尝试相比，这种原位版本将粒子信息的内存使用量减少了近60%，计算时间减少了约20%。 et.al.|[2311.01288](http://arxiv.org/abs/2311.01288)|null|
|**2023-11-02**|**Layer-adapted meshes for singularly perturbed problems via mesh partial differential equations and a posteriori information**|我们提出了一种新的方法来构造奇异摄动微分方程（SPDE）的层适配网格，该方法基于包含后验解信息的网格偏微分方程（MPDE）。关于SPDE的参数鲁棒数值方法的发展，有许多研究依赖于Bakhvalov的层适配网格。在~\citep{HiMa2021}中，提出了一种新的基于MPDE的方法来构造这些网格的推广。与大多数适用于层的网格方法一样，该文中的算法依赖于SPDE解及其导数的\emph｛先验｝边界的详细推导。在这项工作中，我们扩展了这种方法，使其使用解的后验估计。我们给出了有效实现该方法的详细算法，以及一维和二维两参数反应-对流-扩散问题鲁棒解的数值结果。我们还为一维示例提供了完整的FEniCS代码。 et.al.|[2311.01274](http://arxiv.org/abs/2311.01274)|null|

<p align=right>(<a href=#updated-on-20231105>back to top</a>)</p>

## NeRF

|Publish Date|Title|Abstract|PDF|Code|
|---|---|---|---|---|
|**2023-11-01**|**Neural Field Dynamics Model for Granular Object Piles Manipulation**|我们提出了一个基于学习的颗粒材料操纵动力学模型。受流体动力学中常用的欧拉方法的启发，我们的方法采用了一个全卷积神经网络，该网络对基于密度场的物体堆和推进器表示进行操作，使其能够通过卷积操作利用物体间相互作用的空间局部性以及平移等变性。此外，我们的可微动作渲染模块使模型完全可微，并可以直接与基于梯度的轨迹优化算法集成。我们在模拟和真实世界的实验中用大量的桩操作任务评估了我们的模型，并证明它在精度和计算效率方面显著超过了现有的潜在或基于粒子的方法，并在各种环境和任务中表现出零样本泛化能力。 et.al.|[2311.00802](http://arxiv.org/abs/2311.00802)|null|
|**2023-10-31**|**Latent Field Discovery In Interacting Dynamical Systems With Neural Fields**|交互对象的系统通常在控制其动力学的场效应的影响下进化，然而以前的工作已经从这种效应中抽象出来，并假设系统在真空中进化。在这项工作中，我们专注于发现这些场，并仅从观察到的动力学中推断它们，而不直接观察它们。我们将潜在力场的存在理论化，并提出神经场来学习它们。由于观测到的动力学构成了局部物体相互作用和全局场效应的净效应，最近流行的等变网络不适用，因为它们无法捕捉全局信息。为了解决这一问题，我们建议将局部对象交互（ $\mathrm｛SE｝（n）$ 等变并依赖于相对状态）与外部全局场效应（依赖于绝对状态）区分开来。我们用等变图网络对交互进行建模，并将它们与神经场结合在一个集成场力的新型图网络中。我们的实验表明，我们可以准确地发现带电粒子环境、交通场景和引力n体问题中的潜在场，并有效地利用它们来学习系统和预测未来的轨迹。 et.al.|[2310.20679](http://arxiv.org/abs/2310.20679)|**[link](https://github.com/mkofinas/aether)**|
|**2023-10-30**|**Generative Neural Fields by Mixtures of Neural Implicit Functions**|我们提出了一种新的方法来学习由隐式基网络的线性组合表示的生成神经场。我们的算法通过进行元学习或采用自动解码范式，在潜在空间中以隐式神经表示的形式学习基网络及其系数。所提出的方法通过增加基网络的数量来容易地扩大生成神经场的容量，同时通过加权模型平均来保持推理网络的大小较小。因此，使用该模型对实例进行采样在延迟和内存占用方面是有效的。此外，我们为目标任务定制了去噪扩散概率模型，以对潜在的混合系数进行采样，这使我们的最终模型能够有效地生成看不见的数据。实验表明，我们的方法在图像、体素数据和NeRF场景的不同基准上实现了有竞争力的生成性能，而无需对特定模态和域进行复杂的设计。 et.al.|[2310.19464](http://arxiv.org/abs/2310.19464)|null|
|**2023-10-24**|**LiCROM: Linear-Subspace Continuous Reduced Order Modeling with Neural Fields**|线性降阶建模（ROM）通过使用简化的运动学表示来近似系统的行为，从而简化了复杂的模拟。通常，ROM在使用特定空间离散化创建的输入模拟上进行训练，然后用于使用相同的离散化加速模拟。这种离散化依赖性是有限制的。独立于特定的离散化将提供在训练数据中混合和匹配网格分辨率、连通性和类型（四面体、六面体）的灵活性；以在训练过程中看不到的新颖离散化来加速模拟；以及加速在时间上或参数化地改变离散化的自适应模拟。我们提出了一种灵活的、独立于离散化的降阶建模方法。与传统ROM一样，我们将配置表示为位移场的线性组合。与传统的ROM不同，我们的位移场是从参考域上的每个点到相应位移矢量的连续映射；这些映射被表示为隐式神经场。使用线性连续ROM（LiCROM），我们的训练集可以包括经历多个加载条件的多个几何体，与它们的离散化无关。这为降阶建模的新应用打开了大门。我们现在可以加速在运行时修改几何体的模拟，例如通过切割、打孔，甚至交换整个网格。我们还可以加速对训练中看不见的几何形状的模拟。我们演示了一次性泛化，在单个几何体上进行训练，然后模拟各种看不见的几何体。 et.al.|[2310.15907](http://arxiv.org/abs/2310.15907)|null|
|**2023-10-12**|**S4C: Self-Supervised Semantic Scene Completion with Neural Fields**|三维语义场景理解是计算机视觉中的一个基本挑战。它使移动代理能够自主规划和导航任意环境。SSC将这一挑战形式化为从场景的稀疏观测中联合估计密集的几何结构和语义信息。当前的SSC方法通常基于聚合的激光雷达扫描在3D地面实况上进行训练。这一过程依赖于特殊的传感器和手工注释，这些传感器和注释成本高昂且规模不大。为了克服这个问题，我们的工作提出了第一种称为S4C的SSC自监督方法，该方法不依赖于3D地面实况数据。我们提出的方法可以从单个图像重建场景，并且只依赖于训练期间从现成的图像分割网络生成的视频和伪分割地面实况。与使用离散体素网格的现有方法不同，我们将场景表示为隐式语义场。该公式允许查询相机截锥体内的任何点的占用率和语义类。我们的架构是通过基于渲染的自监督损失进行训练的。尽管如此，我们的方法实现了接近于完全监督的最先进方法的性能。此外，我们的方法表现出强大的泛化能力，可以为遥远的视点合成准确的分割图。 et.al.|[2310.07522](http://arxiv.org/abs/2310.07522)|null|
|**2023-10-07**|**HI-SLAM: Monocular Real-time Dense Mapping with Hybrid Implicit Fields**|在这封信中，我们提出了一个基于神经场的实时单目映射框架，用于精确和密集的同时定位和映射（SLAM）。最近的神经映射框架显示出有希望的结果，但依赖于RGB-D或姿势输入，或者无法实时运行。为了解决这些局限性，我们的方法将密集SLAM与神经隐式场相结合。具体来说，我们的密集SLAM方法运行并行跟踪和全局优化，而基于神经场的映射是基于最新的SLAM估计逐步构建的。为了有效地构造神经场，我们采用了多分辨率网格编码和符号距离函数（SDF）表示。这使我们能够始终保持地图的最新状态，并通过循环关闭立即适应全球更新。为了全局一致性，我们提出了一种有效的基于Sim（3）的姿态图束调整（PGBA）方法来运行在线闭环并减轻姿态和尺度漂移。为了进一步提高深度精度，我们结合了学习的单目深度先验。我们提出了一种新的深度和尺度联合调整（JDSA）模块来解决深度先验中固有的尺度模糊性。对合成和真实世界数据集的广泛评估验证了我们的方法在准确性和地图完整性方面优于现有方法，同时保持了实时性能。 et.al.|[2310.04787](http://arxiv.org/abs/2310.04787)|null|
|**2023-10-05**|**Variational Barycentric Coordinates**|我们提出了一种变分技术来优化广义重心坐标，与现有模型相比，该技术提供了额外的控制。先前的工作使用网格或闭式公式表示重心坐标，在实践中限制了目标函数的选择。相反，我们使用神经场直接参数化连续函数，该函数将多面体内部的任何坐标映射到其重心坐标。这个公式是通过我们对重心坐标的理论表征实现的，这使我们能够构建将有效坐标的整个函数类参数化的神经场。我们使用各种目标函数展示了我们模型的灵活性，包括多重光滑性和变形感知能量；作为补充，我们还提出了数学上合理的方法来测量和最小化目标，如不连续神经场的总变化。我们提供了一个实用的加速策略，对我们的算法进行了彻底的验证，并展示了几个应用。 et.al.|[2310.03861](http://arxiv.org/abs/2310.03861)|null|
|**2023-10-05**|**High-Degrees-of-Freedom Dynamic Neural Fields for Robot Self-Modeling and Motion Planning**|机器人自模型是机器人物理形态的任务不可知表示，在没有经典几何运动学模型的情况下，可用于运动规划任务。特别是，当后者难以设计或机器人的运动学发生意外变化时，人类自由的自我建模是真正自主智能体的必要特征。在这项工作中，我们利用神经场使机器人能够将其运动学自建模为仅从带有相机姿势和配置的2D图像中学习的神经隐式查询模型。这使得比依赖于深度图像或几何知识的现有方法具有更大的适用性。为此，除了课程数据采样策略外，我们还提出了一种新的基于编码器的神经密度场架构，用于高自由度（DOF）条件下的动态对象中心场景。在7自由度机器人测试装置中，学习的自模型实现了机器人工作空间尺寸2%的倒角-L2距离。作为一个示例性的下游应用程序，我们展示了该模型在运动规划任务中的能力。 et.al.|[2310.03624](http://arxiv.org/abs/2310.03624)|null|
|**2023-10-02**|**Neural Processing of Tri-Plane Hybrid Neural Fields**|在用于存储和通信3D数据的神经场的吸引人的特性的驱动下，直接处理它们以解决分类和零件分割等任务的问题已经出现，并在最近的工作中进行了研究。早期的方法使用由在整个数据集上训练的共享网络参数化的神经场，实现了良好的任务性能，但牺牲了重建质量。为了改进后者，后来的方法侧重于参数化为大型多层感知器（MLP）的单个神经场，然而，由于权重空间的高维性、固有的权重空间对称性和对随机初始化的敏感性，这些神经元场的处理具有挑战性。因此，结果明显不如通过处理显式表示（例如点云或网格）所获得的结果。与此同时，混合表示，特别是基于三平面的混合表示，已经成为实现神经场的一种更有效的替代方案，但其直接处理尚未得到研究。在本文中，我们证明了三平面离散数据结构编码了丰富的信息，标准的深度学习机器可以有效地处理这些信息。我们定义了一个广泛的基准，涵盖了一组不同的字段，如占用率、有符号/无符号距离，以及首次定义的辐射字段。在处理具有相同重建质量的字段时，我们实现的任务性能远远优于处理大型MLP的框架，并且首次几乎与处理显式表示的架构不相上下。 et.al.|[2310.01140](http://arxiv.org/abs/2310.01140)|**[link](https://github.com/CVLAB-Unibo/triplane_processing)**|
|**2023-09-27**|**Neural Acoustic Context Field: Rendering Realistic Room Impulse Response With Neural Fields**|房间脉冲响应（RIR）测量声音在环境中的传播，对于合成给定环境下的高保真音频至关重要。一些先前的工作已经提出将RIR表示为声音发射器和接收器位置的神经场函数。然而，这些方法没有充分考虑音频场景的声学特性，导致性能不令人满意。这封信提出了一种新的神经声学上下文场方法，称为NACF，通过利用多个声学上下文（如几何结构、材料特性和空间信息）来参数化音频场景。在RIR的独特性质，即时间不光滑性和单调能量衰减的驱动下，我们设计了一个时间相关模块和多尺度能量衰减准则。实验结果表明，NACF的性能显著优于现有的基于字段的方法。请访问我们的项目页面了解更多定性结果。 et.al.|[2309.15977](http://arxiv.org/abs/2309.15977)|null|

<p align=right>(<a href=#updated-on-20231105>back to top</a>)</p>

[contributors-shield]: https://img.shields.io/github/contributors/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[contributors-url]: https://github.com/Vincentqyw/cv-arxiv-daily/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[forks-url]: https://github.com/Vincentqyw/cv-arxiv-daily/network/members
[stars-shield]: https://img.shields.io/github/stars/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[stars-url]: https://github.com/Vincentqyw/cv-arxiv-daily/stargazers
[issues-shield]: https://img.shields.io/github/issues/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[issues-url]: https://github.com/Vincentqyw/cv-arxiv-daily/issues

