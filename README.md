[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]

## Updated on 2023.11.11
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
|**2023-11-09**|**Real-Time Neural Rasterization for Large Scenes**|提出了一种新的大场景真实感实时新视图合成方法。现有的神经渲染方法可以生成逼真的结果，但主要适用于小规模场景（<50平方米），在大规模场景（>10000平方米）中存在困难。传统的基于图形的光栅化渲染对于大型场景来说速度很快，但缺乏真实感，并且需要昂贵的手动创建资源。我们的方法结合了两全其美，将中等质量的脚手架网格作为输入，学习神经纹理场和着色器来建模与视图相关的效果，以增强真实感，同时仍然使用标准图形管道进行实时渲染。我们的方法优于现有的神经渲染方法，为大型自动驾驶和无人机场景提供了至少30倍的渲染速度和相当或更好的真实感。我们的工作是第一个实现大型真实世界场景的实时渲染。 et.al.|[2311.05607](http://arxiv.org/abs/2311.05607)|null|
|**2023-11-09**|**Reconstructing Objects in-the-wild for Realistic Sensor Simulation**|从真实世界的数据中重建物体并以新颖的视图渲染它们，对于为机器人训练和测试的模拟带来真实性、多样性和规模至关重要。在这项工作中，我们提出了NeuSim，这是一种新的方法，可以根据在距离和有限视点捕获的稀疏野外数据来估计精确的几何结构和逼真的外观。为了实现这一目标，我们将物体表面表示为神经符号距离函数，并利用激光雷达和相机传感器数据来重建平滑准确的几何体和法线。我们用一种稳健的、受物理启发的反射率表示法对物体外观进行建模，该表示法对野外数据有效。我们的实验表明，NeuSim在具有稀疏训练视图的具有挑战性的场景中具有强大的视图合成性能。此外，我们展示了将NeuSim资产组合到虚拟世界中，并生成用于评估自动驾驶感知模型的真实多传感器数据。 et.al.|[2311.05602](http://arxiv.org/abs/2311.05602)|null|
|**2023-11-09**|**BakedAvatar: Baking Neural Fields for Real-Time Head Avatar Synthesis**|从视频中合成逼真的4D人头头像对于VR/AR、远程呈现和视频游戏应用至关重要。尽管现有的基于神经辐射场（NeRF）的方法实现了高保真度的结果，但计算费用限制了它们在实时应用中的使用。为了克服这一限制，我们引入了BakedAvatar，这是一种用于实时神经头部化身合成的新表示，可部署在标准多边形光栅化管道中。我们的方法从学习的头部等值面中提取可变形的多层网格，并计算与表情、姿势和视图相关的外观，这些外观可以烘焙到静态纹理中，以实现高效的光栅化。因此，我们提出了一种用于神经头化身合成的三阶段流水线，包括学习连续变形、流形和辐射场，提取分层网格和纹理，以及使用差分光栅化微调纹理细节。实验结果表明，我们的表示生成的合成结果质量与其他最先进的方法相当，同时显著减少了所需的推理时间。我们进一步展示了单眼视频中的各种头部化身合成结果，包括视图合成、面部再现、表情编辑和姿势编辑，所有这些都是以交互式帧率进行的。 et.al.|[2311.05521](http://arxiv.org/abs/2311.05521)|null|
|**2023-11-09**|**VoxNeRF: Bridging Voxel Representation and Neural Radiance Fields for Enhanced Indoor View Synthesis**|创建高质量的视图合成对于沉浸式应用程序至关重要，但仍然存在问题，尤其是在室内环境和实时部署中。当前的技术经常需要大量的计算时间来进行训练和渲染，并且由于不充分的几何结构，经常产生不太理想的3D表示。为了克服这一点，我们引入了VoxNeRF，这是一种利用体积表示来提高室内视图合成质量和效率的新方法。首先，VoxNeRF构建结构化的场景几何体，并将其转换为基于体素的表示。我们使用多分辨率哈希网格自适应地捕捉空间特征，有效地管理室内场景的遮挡和复杂几何结构。其次，我们提出了一种独特的体素引导的高效采样技术。这一创新有选择地将计算资源集中在射线段的最相关部分，大大减少了优化时间。我们针对三个公共室内数据集验证了我们的方法，并证明VoxNeRF优于最先进的方法。值得注意的是，它在减少训练和渲染时间的同时实现了这些收益，速度甚至超过了Instant NGP，使技术更接近实时。 et.al.|[2311.05289](http://arxiv.org/abs/2311.05289)|null|
|**2023-11-08**|**VET: Visual Error Tomography for Point Cloud Completion and High-Quality Neural Rendering**|在过去的几年里，深度神经网络为新视图合成的巨大进步打开了大门。这些方法中的许多都是基于通过结构从运动算法获得的（粗略）代理几何结构。这种代理中的小缺陷可以通过神经渲染来修复，但较大的孔洞或缺失部分，通常出现在薄结构或光滑区域，仍然会导致分散注意力的伪影和时间不稳定。在本文中，我们提出了一种新的基于神经渲染的方法来检测和修复这些缺陷。作为代理，我们使用点云，这使我们能够轻松删除异常几何体并填充缺失的几何体，而无需复杂的拓扑操作。我们方法的关键是（i）一个可微分的、基于混合点的渲染器，它可以混合掉多余的点，以及（ii）视觉误差层析成像（VET）的概念，它允许我们提升2D误差图，以识别缺乏几何结构的3D区域，并相应地生成新的点。此外，（iii）通过添加点作为嵌套的环境贴图，我们的方法使我们能够在同一管道中生成高质量的周围环境渲染图。在我们的结果中，我们表明我们的方法可以提高由结构从运动中获得的点云的质量，从而显著提高新视图合成的质量。与点生长技术相比，该方法还可以有效地修复大规模孔洞和缺失的薄结构。渲染质量优于最先进的方法，时间稳定性显著提高，同时可以以实时帧速率进行渲染。 et.al.|[2311.04634](http://arxiv.org/abs/2311.04634)|**[link](https://github.com/lfranke/vet)**|
|**2023-11-08**|**Learning Robust Multi-Scale Representation for Neural Radiance Fields from Unposed Images**|我们介绍了一种改进的计算机视觉中基于神经图像的绘制问题的解决方案。给定一组在火车时刻从自由移动的相机拍摄的图像，所提出的方法可以在测试时刻从一个新颖的视角合成真实的场景图像。本文提出的关键思想是：（i）在神经新视图合成问题中，通过稳健的管道从未处理的日常图像中恢复准确的相机参数同样至关重要；（ii）以不同的分辨率对对象的内容进行建模更为实用，因为在日常的未渲染图像中，相机的剧烈运动极有可能发生。为了结合这些关键思想，我们利用了场景刚性、多尺度神经场景表示和单图像深度预测的基本原理。具体地说，所提出的方法使相机参数在基于神经场的建模框架中是可学习的。通过假设每个视图的深度预测是按比例进行的，我们限制了连续帧之间的相对姿态。根据相对姿态，通过多尺度神经场网络内的基于图神经网络的多运动平均来建模绝对相机姿态估计，从而产生单个损失函数。优化引入的损失函数提供了相机内在的、外在的以及从未聚焦的图像渲染的图像。我们通过例子证明，对于从日常获取的未聚焦多视图图像中精确建模多尺度神经场景表示的统一框架，在场景表示框架内进行精确的相机姿态估计同样重要。如果不考虑相机姿态估计管道中的鲁棒性措施，对多尺度混叠伪影进行建模可能会适得其反。我们在几个基准数据集上进行了大量实验，以证明我们的方法的适用性。 et.al.|[2311.04521](http://arxiv.org/abs/2311.04521)|null|
|**2023-11-07**|**3DiffTection: 3D Object Detection with Geometry-Aware Diffusion Features**|我们提出了3DiffTection，这是一种利用3D感知扩散模型的特征从单个图像中检测3D对象的最先进方法。注释用于3D检测的大规模图像数据是资源密集型且耗时的。最近，预训练的大图像扩散模型已经成为2D感知任务的有效特征提取器。然而，这些特征最初是在成对的文本和图像数据上训练的，这些数据没有针对3D任务进行优化，并且在应用于目标数据时经常表现出域间隙。我们的方法通过两种专门的调整策略弥合了这些差距：几何和语义。对于几何调整，我们通过引入新的核极扭曲算子，对扩散模型进行微调，以在单个图像的条件下执行新的视图合成。这项任务符合两个基本标准：3D感知的必要性和仅依赖于姿势图像数据，这些数据很容易获得（例如，来自视频），不需要手动注释。对于语义细化，我们在具有检测监督的目标数据上进一步训练模型。两个调优阶段都使用ControlNet来保持原始功能的完整性。在最后一步中，我们利用这些增强的功能在多个虚拟视点上进行测试时间预测集成。通过我们的方法，我们获得了为3D检测量身定制的3D感知特征，并擅长识别跨视点对应关系。因此，我们的模型成为了一个强大的3D检测器，大大超过了以前的基准，例如Cube RCNN，这是Omni3D ARkitscene数据集上AP3D单视图3D检测的先例，提高了9.43\%。此外，3DiffTection展示了强大的数据效率和跨领域数据的泛化能力。 et.al.|[2311.04391](http://arxiv.org/abs/2311.04391)|null|
|**2023-11-08**|**UP-NeRF: Unconstrained Pose-Prior-Free Neural Radiance Fields**|神经辐射场（NeRF）实现了具有高保真度的给定图像和相机姿态的新颖视图合成。随后的工作甚至通过联合优化NeRF和相机姿态，成功地消除了姿态先验的必要性。然而，这些作品仅限于相对简单的设置，例如光度一致和无遮挡的图像集合或视频中的图像序列。因此，他们很难处理具有不同照明和瞬态遮挡的无约束图像。在本文中，我们提出了 $\textbf｛UP NeRF｝$（$\textbf｛U｝$不受约束的$\textbf｛P｝$ose先验自由$\textbf｛Ne｝$ural$\textbf｛R｝$adiance$\textFf｝$ields），以在没有相机姿态先验的情况下优化具有无约束图像集合的NeRF。我们通过优化颜色不敏感特征场的代理任务和用于瞬态遮挡器的单独模块来解决这些挑战，以阻止它们对姿态估计的影响。此外，我们引入了一个候选头部，以实现更稳健的姿态估计和瞬态感知深度监督，从而最大限度地减少不正确先验的影响。在具有挑战性的互联网照片集$\textit｛Phototourism｝$ 数据集中，与包括BARF及其变体在内的基线相比，我们的实验验证了我们的方法的优越性能。 et.al.|[2311.03784](http://arxiv.org/abs/2311.03784)|null|
|**2023-11-05**|**MuSHRoom: Multi-Sensor Hybrid Room Dataset for Joint 3D Reconstruction and Novel View Synthesis**|元宇宙技术要求在消费级硬件上对非人类感知（如无人机/机器人/自动汽车导航）和AR/VR等沉浸式技术进行准确、实时和沉浸式建模，同时要求结构准确性和逼真度。然而，在如何在统一的框架中应用几何重建和真实感建模（新颖的视图合成）方面存在知识差距。为了解决这一差距，并促进消费级设备的稳健和沉浸式建模和渲染的发展，首先，我们提出了一个真实世界的多传感器混合房间数据集（MuSHRoom）。我们的数据集提出了令人兴奋的挑战，需要最先进的方法具有成本效益，对噪声数据和设备具有鲁棒性，并且可以联合学习3D重建和新颖的视图合成，而不是将它们视为单独的任务，使其成为现实世界应用的理想选择。其次，我们在数据集上对几个著名的管道进行了基准测试，用于联合三维网格重建和新颖的视图合成。最后，为了进一步提高整体性能，我们提出了一种新的方法，在两个任务之间实现了良好的权衡。我们的数据集和基准测试在促进以稳健且计算高效的端到端方式融合3D重建和高质量渲染的改进方面显示出巨大潜力。 et.al.|[2311.02778](http://arxiv.org/abs/2311.02778)|null|
|**2023-11-05**|**3D-Aware Talking-Head Video Motion Transfer**|会说话的头部视频的运动转移涉及生成具有主题视频的外观和驾驶视频的运动模式的新视频。当前的方法主要依赖于有限数量的主题图像和2D表示，从而忽略了充分利用主题视频中固有的多视图外观特征。在本文中，我们提出了一种新的3D感知会说话的头部视频运动传输网络Head3D，该网络通过递归网络从2D主题帧生成可视觉解释的3D规范头部，从而充分利用主题外观信息。我们方法的一个关键组成部分是一个自监督的3D头部几何学习模块，旨在从2D主题视频帧中预测头部姿势和深度图。该模块便于在规范空间中估计3D头部，然后可以对其进行变换以与驱动视频帧对准。此外，我们使用基于注意力的融合网络将主题帧的背景和其他细节与3D主题头部相结合，以产生合成目标视频。我们在两个公开演讲的头部视频数据集上进行的大量实验表明，Head3D在实际的交叉身份设置中优于2D和3D现有技术，有证据表明它可以很容易地适应姿势可控的新型视图合成任务。 et.al.|[2311.02549](http://arxiv.org/abs/2311.02549)|null|

<p align=right>(<a href=#updated-on-20231111>back to top</a>)</p>

## 3D Reconstruction

|Publish Date|Title|Abstract|PDF|Code|
|---|---|---|---|---|
|**2023-11-09**|**Liquid phase fast electron tomography unravels the true 3D structure of colloidal assemblies**|电子断层扫描已成为研究纳米材料三维（3D）结构的常用工具，包括胶体纳米颗粒组件。然而，电子显微镜技术的性质通常要求在高真空下进行这种表征。因此，通过（湿）胶体化学方法制备的组件需要预处理样品制备，包括溶剂蒸发和在固体基底上沉积（TEM网格）。因此，变化总是强加在实际的纳米颗粒组织上，这在很大程度上是纳米材料性质的原因。因此，我们在此提出在纳米颗粒组件的原始胶体环境中应用（快速）电子断层扫描。为了解决与液体电子断层扫描相关的挑战，我们设计了一种方法，将商业液体原位TEM池中的快速数据采集与专用重建工作流程相结合。我们介绍了这种方法在两个不同系统中的应用，这两个系统举例说明了干燥和真空的影响，这取决于保护配体的性质。包括包封在聚合物壳中的聚苯乙烯封端的Au纳米颗粒的组件的3D重建显示，与干燥的对应物相比，在液体介质中进行的实验的结构不那么紧凑，变形更大。另一方面，对水中自组装Au纳米棒的颗粒间距离的定量分析与之前报道的纳米棒周围配体层的尺寸一致，而纳米棒在类似的干燥组件中接触得更紧密。因此，这项研究强调了开发高分辨率表征工具的重要性，以保护胶体纳米结构的天然环境。 et.al.|[2311.05309](http://arxiv.org/abs/2311.05309)|null|
|**2023-11-09**|**ConRad: Image Constrained Radiance Fields for 3D Generation from a Single Image**|我们提出了一种从单个RGB图像重建3D对象的新方法。我们的方法利用最新的图像生成模型来推断隐藏的3D结构，同时保持对输入图像的忠实。虽然现有的方法在从文本提示生成3D模型方面获得了令人印象深刻的结果，但它们并不能提供一种简单的方法来调节输入RGB数据。这些方法的简单扩展通常会导致输入图像和3D重建之间的外观不正确。我们通过引入图像约束辐射场（ConRad）来解决这些挑战，神经辐射场的一种新变体。ConRad是一种高效的3D表示，它明确地捕捉一个视点中输入图像的外观。我们提出了一种训练算法，该算法利用单个RGB图像和预训练的扩散模型来优化ConRad表示的参数。大量实验表明，ConRad表示可以简化图像细节的保存，同时产生逼真的3D重建。与现有的最先进的基线相比，我们表明，我们的3D重建仍然更忠实于输入，并产生更一致的3D模型，同时在ShapeNet对象基准上展示了显著改进的定量性能。 et.al.|[2311.05230](http://arxiv.org/abs/2311.05230)|null|
|**2023-11-08**|**Implicit Neural Representations for Breathing-compensated Volume Reconstruction in Robotic Ultrasound Aorta Screening**|超声（US）成像由于缺乏非电离辐射和普遍可用性，被广泛用于腹部疾病的诊断和分期。然而，操作员之间的显著可变性和不一致的图像采集阻碍了广泛采用广泛的筛查程序。机器人超声系统已经成为一种很有前途的解决方案，它提供了标准化的采集协议和自动化采集的可能性。此外，这些系统能够通过机器人跟踪访问3D数据，增强体积重建，以改进超声解释和精确的疾病诊断。然而，腹部图像的3D US重建的可解释性可能会受到患者呼吸运动的影响。本研究介绍了一种通过利用隐式神经表示来补偿3D US复合中的呼吸运动的方法。我们的方法采用机器人超声波系统进行自动筛查。为了证明该方法的有效性，我们将我们提出的诊断和监测腹主动脉瘤的方法作为一个有代表性的使用案例进行了评估。我们的实验表明，我们提出的管道有助于强大的自动机器人采集，减轻呼吸运动产生的伪影，并产生更平滑的3D重建，以增强筛查和医学诊断。 et.al.|[2311.04999](http://arxiv.org/abs/2311.04999)|null|
|**2023-11-08**|**LRM: Large Reconstruction Model for Single Image to 3D**|我们提出了第一个大型重建模型（LRM），它可以在5秒内从单个输入图像中预测对象的3D模型。与以前在ShapeNet等小规模数据集上以特定类别的方式训练的许多方法不同，LRM采用了一种高度可扩展的基于变换器的架构，具有5亿个可学习参数，可以直接从输入图像中预测神经辐射场（NeRF）。我们在包含约100万个对象的海量多视图数据上以端到端的方式训练我们的模型，包括Ob厌恶对象的合成渲染和MVImgNet的真实捕捉。这种高容量模型和大规模训练数据的结合使我们的模型能够高度通用，并根据各种测试输入产生高质量的3D重建，包括真实世界的野外捕捉和生成模型的图像。视频演示和可交互的3D网格可以在这个网站上找到：https://yiconghong.me/LRM/. et.al.|[2311.04400](http://arxiv.org/abs/2311.04400)|null|
|**2023-11-07**|**High-fidelity 3D Reconstruction of Plants using Neural Radiance Field**|在精准农业（PA）领域，植物表型的准确重建在优化可持续农业实践方面发挥着关键作用。目前，基于光学传感器的方法在该领域占据主导地位，但对非结构化农业环境中作物和植物的高保真3D重建的需求仍然具有挑战性。最近，神经辐射场（NeRF）的形式出现了一个有前景的发展，这是一种利用神经密度场的新方法。这项技术在各种新颖的视觉合成任务中表现出了令人印象深刻的性能，但在农业背景下仍相对未被探索。在我们的研究中，我们专注于植物表型的两项基本任务：（1）2D新视图图像的合成和（2）作物和植物模型的3D重建。我们探索了神经辐射场的世界，特别是两种SOTA方法：Instant NGP，它擅长以令人印象深刻的训练和推理速度生成高质量图像；Instant NSR，它通过在训练过程中结合符号距离函数（SDF）来改进重建的几何体。特别地，我们提出了一个新的植物表型数据集，包括来自生产环境的真实植物图像。该数据集是第一个旨在全面探索NeRF在农业环境中的优势和局限性的此类举措。我们的实验结果表明，NeRF在合成新视图图像方面表现出了值得称赞的性能，并且能够实现与Reality Capture竞争的重建结果，Reality Capture是一款领先的基于3D多视图立体（MVS）的重建商业软件。然而，我们的研究也强调了NeRF的某些缺点，包括训练速度相对较慢、采样不足时的性能限制，以及在复杂设置中获得几何质量的挑战。 et.al.|[2311.04154](http://arxiv.org/abs/2311.04154)|null|
|**2023-11-07**|**DeepPatent2: A Large-Scale Benchmarking Corpus for Technical Drawing Understanding**|计算机视觉（CV）和自然语言处理的最新进展是通过在实际应用中利用大数据来推动的。然而，这些研究领域仍然受到可用数据集的数量、多功能性和多样性的限制。简历任务，如图像字幕，主要在自然图像上进行，仍然很难在科学和技术文件中经常包含的草图图像上产生准确和有意义的字幕。诸如从2D图像进行3D重建之类的其他任务的推进需要具有多个视点的更大的数据集。我们介绍了DeepPatent2，这是一个大型数据集，提供了从14年的美国外观设计专利文件中提取的超过270万张技术图纸，132890个对象名称和22394个视点。我们通过概念字幕展示了DeepPatent2的实用性。我们进一步提供了我们的数据集的潜在有用性，以促进其他研究领域，如3D图像重建和图像检索。 et.al.|[2311.04098](http://arxiv.org/abs/2311.04098)|**[link](https://github.com/gofigure-lanl/figure-segmentation)**|
|**2023-11-05**|**MuSHRoom: Multi-Sensor Hybrid Room Dataset for Joint 3D Reconstruction and Novel View Synthesis**|元宇宙技术要求在消费级硬件上对非人类感知（如无人机/机器人/自动汽车导航）和AR/VR等沉浸式技术进行准确、实时和沉浸式建模，同时要求结构准确性和逼真度。然而，在如何在统一的框架中应用几何重建和真实感建模（新颖的视图合成）方面存在知识差距。为了解决这一差距，并促进消费级设备的稳健和沉浸式建模和渲染的发展，首先，我们提出了一个真实世界的多传感器混合房间数据集（MuSHRoom）。我们的数据集提出了令人兴奋的挑战，需要最先进的方法具有成本效益，对噪声数据和设备具有鲁棒性，并且可以联合学习3D重建和新颖的视图合成，而不是将它们视为单独的任务，使其成为现实世界应用的理想选择。其次，我们在数据集上对几个著名的管道进行了基准测试，用于联合三维网格重建和新颖的视图合成。最后，为了进一步提高整体性能，我们提出了一种新的方法，在两个任务之间实现了良好的权衡。我们的数据集和基准测试在促进以稳健且计算高效的端到端方式融合3D重建和高质量渲染的改进方面显示出巨大潜力。 et.al.|[2311.02778](http://arxiv.org/abs/2311.02778)|null|
|**2023-11-05**|**Fast Point-cloud to Mesh Reconstruction for Deformable Object Tracking**|我们周围的世界充满了柔软的物体，作为人类，我们从小就学会用灵巧的手来感知和变形。为了使机器人手能够控制软物体，它需要获取变形物体的在线状态反馈。虽然RGB-D相机可以以30Hz的速率收集被遮挡的信息，但后者并不代表连续可跟踪的物体表面。因此，在这项工作中，我们开发了一种方法，可以为不同类别的对象以高于50Hz的速度创建变形点云的变形网格。从点云重建网格在计算机图形学领域的3D重建和4D重建下已经进行了长期的研究，但这两种方法都缺乏机器人应用所需的速度和可推广性。我们的模型是使用点云自动编码器和Real NVP架构设计的。后者是一个具有流形保持性质的连续流神经网络。我们的模型采用模板网格，该网格是处于规范状态的对象的网格，然后使模板网格变形以匹配对象的变形点云。我们的方法可以对六种不同ycb类别的变形以58Hz的速率执行网格重建和跟踪。下游应用的实例可以是用于机械手的控制算法，其需要来自被操纵物体的状态的在线反馈，这将允许以闭环方式进行在线抓取自适应。此外，我们的方法提供的跟踪能力可以帮助以无标记的方法对变形对象进行系统识别。在未来的工作中，我们将把我们的方法扩展到更多类别的物体和现实世界中变形的点云 et.al.|[2311.02749](http://arxiv.org/abs/2311.02749)|null|
|**2023-11-05**|**IPVNet: Learning Implicit Point-Voxel Features for Open-Surface 3D Reconstruction**|三维开放表面（例如非水密网格）的重建是计算机视觉中一个未被充分探索的领域。最近基于学习的内隐技术通过实现任意分辨率的重建，消除了以前的障碍。然而，这种方法通常依赖于区分表面的内部和外部，以便在重建目标时提取零水平集。在开放表面的情况下，这种区别通常会导致人为的表面间隙闭合。然而，真实世界的数据可能包含由显著的表面间隙定义的复杂细节。回归无符号距离场的隐函数在重建这种开放曲面方面显示出了前景。尽管如此，当前的无符号隐式方法依赖于原始数据的离散表示。这不仅将学习过程限制在表示的分辨率上，而且在重建中引入了异常值。为了在不引入异常值的情况下准确重建开放曲面，我们提出了一种基于学习的隐式点体素模型（IPVNet）。IPVNet通过利用原始点云数据及其离散体素对应物来预测三维空间中曲面和查询点之间的无符号距离。在合成和真实世界的公共数据集上进行的实验表明，IPVNet的性能优于现有技术，同时在最终的重建中产生的异常值要少得多。 et.al.|[2311.02552](http://arxiv.org/abs/2311.02552)|**[link](https://github.com/robotic-vision-lab/implicit-point-voxel-features-network)**|
|**2023-11-02**|**CADSim: Robust and Scalable in-the-wild 3D Reconstruction for Controllable Sensor Simulation**|逼真的模拟是实现%自动驾驶汽车安全和可扩展开发的关键。一个核心组件是模拟传感器，以便可以在模拟中测试整个自主系统。传感器模拟包括对具有高质量外观和铰接几何结构的交通参与者（如车辆）进行建模，并实时渲染。自动驾驶行业通常雇佣艺术家来构建这些资产。然而，这是昂贵的，缓慢的，并且可能不能反映现实。相反，根据野外收集的传感器数据自动重建资产将为生成具有良好真实世界覆盖率的多样化大型集合提供更好的途径。然而，由于传感器数据的稀疏性和噪声，目前的重建方法在野外传感器数据中举步维艰。为了解决这些问题，我们提出了CADSim，它通过一小组CAD模型将零件感知对象类先验与可微分渲染相结合，以自动重建具有高质量外观的车辆几何结构，包括铰接车轮。我们的实验表明，与现有方法相比，我们的方法从稀疏数据中恢复了更准确的形状。重要的是，它还能有效地训练和渲染。我们在几个应用中展示了我们重建的车辆，包括对自主感知系统的精确测试。 et.al.|[2311.01447](http://arxiv.org/abs/2311.01447)|null|

<p align=right>(<a href=#updated-on-20231111>back to top</a>)</p>

## Diffusion

|Publish Date|Title|Abstract|PDF|Code|
|---|---|---|---|---|
|**2023-11-09**|**Diffusion-Generative Multi-Fidelity Learning for Physical Simulation**|高保真度代理学习对于物理模拟相关应用非常重要，因为它避免了从头开始运行数值求解器，这是已知的成本高昂的，并且它使用高保真度示例进行训练，并大大降低了数据收集的成本。尽管现有方法多种多样，但它们都构建了一个模型，将输入参数直接映射到解决方案输出。受生成模型最近突破的启发，我们采取了另一种观点，并将解输出视为由随机噪声生成。我们开发了一种基于随机微分方程（SDE）的扩散生成高保真度（DGMF）学习方法，其中生成是一个连续的去噪过程。我们提出了一个条件得分模型，通过输入参数和保真度来控制解的生成。通过附加输入（时间或空间变量），我们的模型可以有效地学习和预测多维解数组。我们的方法自然地统一了离散和连续保真度建模。我们的方法在几个典型应用中的优势为高保真度学习提供了一个很有前途的新方向。 et.al.|[2311.05606](http://arxiv.org/abs/2311.05606)|null|
|**2023-11-09**|**Bayesian Methods for Media Mix Modelling with shape and funnel effects**|近年来，生成人工智能的重大进展凸显了物理启发模型的重要作用，这些模型利用基于基本物理原理的先进数学概念来增强人工智能能力。在这些模型中，基于扩散方程的模型大大提高了图像质量。本研究旨在探索构成气体动力学理论基础的Maxwell-Boltzmann方程和Michaelis-Menten模型在营销组合建模（MMM）应用中的潜在用途。我们建议将这些方程纳入分层贝叶斯模型，以分析广告背景下的消费者行为。这些方程组擅长准确描述复杂系统中的随机动力学，如社交互动和消费者广告互动。 et.al.|[2311.05587](http://arxiv.org/abs/2311.05587)|null|
|**2023-11-09**|**LCM-LoRA: A Universal Stable-Diffusion Acceleration Module**|潜在一致性模型（LCM）在加速文本到图像生成任务方面取得了令人印象深刻的性能，以最少的推理步骤生成高质量的图像。LCM是从预先训练的潜在扩散模型（LDM）中提炼出来的，只需要约32个A100 GPU训练小时。本报告进一步扩展了LCM在两个方面的潜力：首先，通过将LoRA蒸馏应用于包括SD-V1.5、SSD-1B和SDXL在内的稳定扩散模型，我们将LCM的范围扩展到了内存消耗显著减少的更大模型，实现了卓越的图像生成质量。其次，我们将通过LCM蒸馏获得的LoRA参数识别为通用的稳定扩散加速模块，称为LCM-LoRA。LCM-LoRA可以直接插入到各种稳定扩散微调模型或LoRA中，而无需训练，因此代表了适用于各种图像生成任务的通用加速器。与以前的数值PF-ODE求解器（如DDIM、DPM解算器）相比，LCM-LoRA可以看作是一种具有较强泛化能力的插入式神经PF-ODE解算器。项目页面：https://github.com/luosiallen/latent-consistency-model. et.al.|[2311.05556](http://arxiv.org/abs/2311.05556)|**[link](https://github.com/luosiallen/latent-consistency-model)**|
|**2023-11-09**|**Onset of pattern formation for the stochastic Allen-Cahn equation**|我们研究了随机Allen-Cahn方程 $\frac｛\partial u_\eps｝｛\ partial t｝=\frac 12\frac{\partial ^2 u_\eps｝{\ppartial x^2｝-（u_\eps^3-u_\eps）+\sqrt\eps\，\dot W$的解的行为，该方程具有适当大的空间区间$[-L_\eps，L_\eps]$上的Dirichlet边界条件，从同零函数开始，其中$\dot W$$是时空白噪声。我们的主要目标是在小噪声极限下描述相分离的开始，出现$u_\eps$接近$\pm1$的一个或另一个的空间区域。时间尺度和空间结构由适当的高斯过程确定，该过程表现为线性化a-C方程的随机对应物。De Masi等人[Ann.Probab.｛\bf 22｝，（1994），334-371]在一类反应-扩散模型的相关背景下初步研究了这一问题，该模型是加速搅拌过程和$\｛-1，1｝^^｛\mathbb上自旋翻转动力学的叠加{Z}_\eps｝$，其中$\mathbb{Z}_\eps=\mathbb｛Z｝$modulo$\lfloor\eps^{-1}L_\eps\rfloor$ 。 et.al.|[2311.05526](http://arxiv.org/abs/2311.05526)|null|
|**2023-11-09**|**From Stability to Change: The Potential Application of Bifurcation Theory to Opinion Dynamics Considerations**|本研究采用非线性动力学方法，特别是分叉理论，分析网络社区中的社会互动和行为。参考Steven Strogatz等人的关键著作，本文探讨了干草叉、鞍节点和跨临界分叉在社交媒体中的应用，以模拟集体意见转变和趋势扩散。通过将Strogatz对复杂网络和同步的见解与Guckenheimer、Holmes、Kuznetsov和Wiggins的基础理论相结合，该研究考察了小世界网络效应和同步在集体行为中的作用。塞德尔对分叉理论的实践有助于将这些数学概念应用于社会科学研究，旨在揭示数字通信的动力学和信息的快速传播。该研究还涉及使用梅尔尼科夫的方法来分析同宿轨道和异宿轨道的稳定性，以及混沌的发生，反思了理解自然界和社会中复杂系统的更广泛意义。其目标是提供一个模型，捕捉数字生态系统中个人快速而复杂的认知过程，为在线集体观点的演变、时尚的兴起和传播以及数字环境中的行为变化提供新的视角。 et.al.|[2311.05488](http://arxiv.org/abs/2311.05488)|null|
|**2023-11-09**|**Disease Gene Prioritization With Quantum Walks**|疾病基因优先级根据提供的一组种子基因，根据基因或蛋白质与给定疾病的可能相关性，为基因或蛋白质打分。在这里，我们描述了一种新的基于连续时间量子行走的疾病基因优先级算法，该算法使用蛋白质-蛋白质相互作用（PPI）网络的邻接矩阵。我们的算法可以被视为以前被称为扩散核的方法的量子版本，但重要的是，它在预测疾病基因方面具有更高的性能，并且还允许将种子节点自循环编码到潜在的哈密顿量中，这又一次提高了性能。我们通过在七个不同的PPI网络中，将我们提出的方法与三个疾病集的几种众所周知的基因优先排序方法进行比较，证明了它的成功。为了比较这些方法，我们使用交叉验证并检查平均倒数和召回值。我们通过对冠状动脉疾病的预测基因进行富集分析，进一步验证了我们的方法。我们还研究了在种子中添加自循环的影响，并认为它们允许量子行走器对低阶种子节点保持更局部的状态。 et.al.|[2311.05486](http://arxiv.org/abs/2311.05486)|null|
|**2023-11-09**|**Retinal OCT Synthesis with Denoising Diffusion Probabilistic Models for Layer Segmentation**|使用深度学习的现代生物医学图像分析经常遇到注释数据有限的挑战。为了克服这个问题，可以使用深度生成模型来合成真实的生物医学图像。在这方面，我们提出了一种图像合成方法，该方法利用去噪扩散概率模型（DDPM）来自动生成视网膜光学相干断层扫描（OCT）图像。通过提供粗略的层草图，经过训练的DDPM可以生成逼真的乳头周围OCT图像。我们进一步发现，通过知识自适应可以获得更准确的伪标签，这对分割任务大有裨益。通过这一点，我们观察到层分割精度的持续提高，并使用各种神经网络进行了验证。此外，我们发现，仅用合成图像训练的层分割模型可以获得与仅用真实图像训练的模型相当的结果。这些发现证明了DDPM在减少视网膜OCT图像手动注释需求方面的潜力。 et.al.|[2311.05479](http://arxiv.org/abs/2311.05479)|null|
|**2023-11-09**|**Lithium-ion battery performance model including solvent segregation effects**|在开源PyBaMM平台上开发并实现了一个包含共溶剂电解质的锂离子电池模型。锂离子电解质对电池运行至关重要，通常至少含有两种溶剂以满足性能要求。然而，广泛使用的Doyle-Fuller-Newman电池模型假设电解质包括溶解在单一有效溶剂中的盐。这种单一溶剂近似已经被实验证明是错误的，可能会阻碍准确的电池建模。在这里，我们提出了一个双溶剂模型，该模型解决了碳酸亚乙酯（EC）和锂盐在背景线性碳酸盐中的传输。在循环过程中，EC浓度极化与Li+的极化相反，影响局部电解质性质和电池水平的过电位。Li+的浓度梯度可能受到交叉扩散的影响，从而EC梯度增强或阻碍盐通量。一个包括EC传输的合理参数化模型预测，在4.5C放电时的功率损失比其单一溶剂当量多6%，在一千次1C循环后的容量损失约为0.32%。这项工作提供了一种工具来模拟电解质中可能影响降解的更多传输行为，并使有关溶剂化结构相关性能的微观知识能够转移到宏观尺度。 et.al.|[2311.05467](http://arxiv.org/abs/2311.05467)|null|
|**2023-11-09**|**3DStyle-Diffusion: Pursuing Fine-grained Text-driven 3D Stylization with 2D Diffusion Models**|通过文本驱动的风格化创建3D内容对多媒体和图形社区提出了根本性的挑战。跨模态基础模型（例如CLIP）的最新进展使这个问题变得可行。这些方法通常利用CLIP将样式化网格的整体语义与给定的文本提示对齐。然而，仅基于这种语义级别的跨模态监督，实现3D网格中细粒度细节的更可控风格化并非易事。在这项工作中，我们提出了一种新的3DStyle Diffusion模型，该模型可以触发3D网格的细粒度风格化，并具有来自2D Diffusion模式的额外可控外观和几何指导。从技术上讲，3DStyle Diffusion首先使用隐式MLP网络将3D网格的纹理参数化为反射特性和场景照明。同时，以3D网格为条件，实现了每个采样视图的精确深度图。然后，3DStyle Diffusion利用预先训练的可控2D Diffusion模型来指导渲染图像的学习，鼓励每个视图的合成图像在语义上与文本提示对齐，并在几何上与深度图一致。这种方式以端到端的方式优雅地集成了通过隐式MLP网络进行的图像渲染和图像合成的扩散过程，实现了3D网格的高质量细粒度风格化。我们还构建了一个新的数据集，该数据集源于Ob厌恶对象和该任务的评估协议。通过定性和定量实验，我们验证了3DStyle Diffusion的能力。源代码和数据位于\url{https://github.com/yanghb22-fdu/3DStyle-Diffusion-Official}。 et.al.|[2311.05464](http://arxiv.org/abs/2311.05464)|**[link](https://github.com/yanghb22-fdu/3dstyle-diffusion-official)**|
|**2023-11-09**|**ControlStyle: Text-Driven Stylized Image Generation Using Diffusion Priors**|最近，多媒体社区见证了在大规模多模态数据上训练的用于视觉内容创建的扩散模型的兴起，特别是在文本到图像生成领域。在本文中，我们为“风格化”文本到图像模型提出了一项新任务，即文本驱动的风格化图像生成，这进一步增强了内容创建中的可编辑性。在给定输入文本提示和风格图像的情况下，本任务旨在生成既与输入文本提示语义相关又与风格图像对齐的风格化图像。为了实现这一点，我们提出了一种新的扩散模型（ControlStyle），通过使用可训练的调制网络升级预先训练的文本到图像模型，实现更多的文本提示和风格图像条件。此外，还同时引入了扩散风格和内容正则化，以便于学习具有这些扩散先验的调制网络，从而实现高质量的风格化文本到图像生成。大量的实验证明了我们的ControlStyle在产生更视觉愉悦和艺术效果方面的有效性，超过了文本到图像模型和传统风格转换技术的简单组合。 et.al.|[2311.05463](http://arxiv.org/abs/2311.05463)|null|

<p align=right>(<a href=#updated-on-20231111>back to top</a>)</p>

## NeRF

|Publish Date|Title|Abstract|PDF|Code|
|---|---|---|---|---|
|**2023-11-09**|**BakedAvatar: Baking Neural Fields for Real-Time Head Avatar Synthesis**|从视频中合成逼真的4D人头头像对于VR/AR、远程呈现和视频游戏应用至关重要。尽管现有的基于神经辐射场（NeRF）的方法实现了高保真度的结果，但计算费用限制了它们在实时应用中的使用。为了克服这一限制，我们引入了BakedAvatar，这是一种用于实时神经头部化身合成的新表示，可部署在标准多边形光栅化管道中。我们的方法从学习的头部等值面中提取可变形的多层网格，并计算与表情、姿势和视图相关的外观，这些外观可以烘焙到静态纹理中，以实现高效的光栅化。因此，我们提出了一种用于神经头化身合成的三阶段流水线，包括学习连续变形、流形和辐射场，提取分层网格和纹理，以及使用差分光栅化微调纹理细节。实验结果表明，我们的表示生成的合成结果质量与其他最先进的方法相当，同时显著减少了所需的推理时间。我们进一步展示了单眼视频中的各种头部化身合成结果，包括视图合成、面部再现、表情编辑和姿势编辑，所有这些都是以交互式帧率进行的。 et.al.|[2311.05521](http://arxiv.org/abs/2311.05521)|null|
|**2023-11-08**|**Learning Robust Multi-Scale Representation for Neural Radiance Fields from Unposed Images**|我们介绍了一种改进的计算机视觉中基于神经图像的绘制问题的解决方案。给定一组在火车时刻从自由移动的相机拍摄的图像，所提出的方法可以在测试时刻从一个新颖的视角合成真实的场景图像。本文提出的关键思想是：（i）在神经新视图合成问题中，通过稳健的管道从未处理的日常图像中恢复准确的相机参数同样至关重要；（ii）以不同的分辨率对对象的内容进行建模更为实用，因为在日常的未渲染图像中，相机的剧烈运动极有可能发生。为了结合这些关键思想，我们利用了场景刚性、多尺度神经场景表示和单图像深度预测的基本原理。具体地说，所提出的方法使相机参数在基于神经场的建模框架中是可学习的。通过假设每个视图的深度预测是按比例进行的，我们限制了连续帧之间的相对姿态。根据相对姿态，通过多尺度神经场网络内的基于图神经网络的多运动平均来建模绝对相机姿态估计，从而产生单个损失函数。优化引入的损失函数提供了相机内在的、外在的以及从未聚焦的图像渲染的图像。我们通过例子证明，对于从日常获取的未聚焦多视图图像中精确建模多尺度神经场景表示的统一框架，在场景表示框架内进行精确的相机姿态估计同样重要。如果不考虑相机姿态估计管道中的鲁棒性措施，对多尺度混叠伪影进行建模可能会适得其反。我们在几个基准数据集上进行了大量实验，以证明我们的方法的适用性。 et.al.|[2311.04521](http://arxiv.org/abs/2311.04521)|null|
|**2023-11-06**|**Dynamic Neural Fields for Learning Atlases of 4D Fetal MRI Time-series**|我们提出了一种使用神经场快速构建生物医学图像图谱的方法。图谱是生物医学图像分析任务的关键，但传统的深度网络估计方法仍然耗时。在这项初步工作中，我们将特定主题的图谱构建框定为学习可变形时空观测的神经场。我们将我们的方法应用于学习子宫内胎儿动态BOLD MRI时间序列的受试者特异性图谱和运动稳定性。我们的方法产生了胎儿BOLD时间序列的高质量图谱，与现有工作相比，收敛速度更快。虽然我们的方法在解剖重叠方面稍逊于调整良好的基线，但它估计模板的速度要快得多，从而能够快速处理和稳定4D动态MRI采集的大型数据库。代码可在https://github.com/Kidrauh/neural-atlasing et.al.|[2311.02874](http://arxiv.org/abs/2311.02874)|**[link](https://github.com/kidrauh/neural-atlasing)**|
|**2023-11-04**|**LISNeRF Mapping: LiDAR-based Implicit Mapping via Semantic Neural Fields for Large-Scale 3D Scenes**|大规模语义映射对于户外自主代理完成规划和导航等高级任务至关重要。本文提出了一种通过单独的激光雷达测量的隐式表示进行大规模三维语义重建的新方法。我们首先利用基于八叉树的分层结构来存储隐式特征，然后通过浅层多层感知器（MLP）将这些隐式特征解码为语义信息和有符号距离值。我们采用现成的算法来预测点云的语义标签和实例ID。然后，我们使用点云几何的自监督范式和语义和全景标签的伪监督范式来联合优化隐含特征和MLP参数。随后，利用Marching Cubes算法对推理阶段的场景进行细分和可视化。对于内存受限的场景，还开发了一种地图拼接策略，将子地图合并为一个完整的地图。据我们所知，我们的方法是第一个从仅激光雷达的输入中重建语义隐含场景的工作。在SemanticKITTI、SemanticPOSS和nuScenes三个真实世界数据集上的实验证明了与当前最先进的3D映射方法相比，我们的框架的有效性和效率。 et.al.|[2311.02313](http://arxiv.org/abs/2311.02313)|null|
|**2023-11-03**|**EmerNeRF: Emergent Spatial-Temporal Scene Decomposition via Self-Supervision**|我们提出了EmerNeRF，这是一种简单而强大的方法，用于学习动态驾驶场景的时空表示。EmerNeRF以神经领域为基础，通过自举同时捕捉场景几何、外观、运动和语义。EmerNeRF取决于两个核心组件：首先，它将场景分为静态场和动态场。这种分解纯粹来自于自我监督，使我们的模型能够从一般的野外数据源中学习。其次，EmerNeRF将动态场中的感应流场参数化，并使用该流场进一步聚合多帧特征，从而提高动态对象的渲染精度。耦合这三个字段（静态、动态和流）使EmerNeRF能够自我充分地表示高度动态的场景，而不依赖于用于动态对象分割或光流估计的地面实况对象注释或预先训练的模型。我们的方法在传感器模拟中实现了最先进的性能，在重建静态（+2.93 PSNR）和动态（+3.70 PSNR）场景时显著优于以前的方法。此外，为了支持EmerNeRF的语义泛化，我们将2D视觉基础模型特征提升到4D时空中，并解决现代变形金刚中的普遍位置偏差，显著提高了3D感知性能（例如，占用预测准确率平均相对提高37.50%）。最后，我们构建了一个多样化且具有挑战性的120序列数据集，以在极端和高度动态的环境下对神经场进行基准测试。 et.al.|[2311.02077](http://arxiv.org/abs/2311.02077)|null|
|**2023-11-01**|**Neural Field Dynamics Model for Granular Object Piles Manipulation**|我们提出了一个基于学习的颗粒材料操纵动力学模型。受流体动力学中常用的欧拉方法的启发，我们的方法采用了一个全卷积神经网络，该网络对基于密度场的物体堆和推进器表示进行操作，使其能够通过卷积操作利用物体间相互作用的空间局部性以及平移等变性。此外，我们的可微动作渲染模块使模型完全可微，并可以直接与基于梯度的轨迹优化算法集成。我们在模拟和真实世界的实验中用大量的桩操作任务评估了我们的模型，并证明它在精度和计算效率方面显著超过了现有的潜在或基于粒子的方法，并在各种环境和任务中表现出零样本泛化能力。 et.al.|[2311.00802](http://arxiv.org/abs/2311.00802)|null|
|**2023-10-31**|**Latent Field Discovery In Interacting Dynamical Systems With Neural Fields**|交互对象的系统通常在控制其动力学的场效应的影响下进化，然而以前的工作已经从这种效应中抽象出来，并假设系统在真空中进化。在这项工作中，我们专注于发现这些场，并仅从观察到的动力学中推断它们，而不直接观察它们。我们将潜在力场的存在理论化，并提出神经场来学习它们。由于观测到的动力学构成了局部物体相互作用和全局场效应的净效应，最近流行的等变网络不适用，因为它们无法捕捉全局信息。为了解决这一问题，我们建议将局部对象交互（ $\mathrm｛SE｝（n）$ 等变并依赖于相对状态）与外部全局场效应（依赖于绝对状态）区分开来。我们用等变图网络对交互进行建模，并将它们与神经场结合在一个集成场力的新型图网络中。我们的实验表明，我们可以准确地发现带电粒子环境、交通场景和引力n体问题中的潜在场，并有效地利用它们来学习系统和预测未来的轨迹。 et.al.|[2310.20679](http://arxiv.org/abs/2310.20679)|**[link](https://github.com/mkofinas/aether)**|
|**2023-10-30**|**Generative Neural Fields by Mixtures of Neural Implicit Functions**|我们提出了一种新的方法来学习由隐式基网络的线性组合表示的生成神经场。我们的算法通过进行元学习或采用自动解码范式，在潜在空间中以隐式神经表示的形式学习基网络及其系数。所提出的方法通过增加基网络的数量来容易地扩大生成神经场的容量，同时通过加权模型平均来保持推理网络的大小较小。因此，使用该模型对实例进行采样在延迟和内存占用方面是有效的。此外，我们为目标任务定制了去噪扩散概率模型，以对潜在的混合系数进行采样，这使我们的最终模型能够有效地生成看不见的数据。实验表明，我们的方法在图像、体素数据和NeRF场景的不同基准上实现了有竞争力的生成性能，而无需对特定模态和域进行复杂的设计。 et.al.|[2310.19464](http://arxiv.org/abs/2310.19464)|null|
|**2023-10-24**|**LiCROM: Linear-Subspace Continuous Reduced Order Modeling with Neural Fields**|线性降阶建模（ROM）通过使用简化的运动学表示来近似系统的行为，从而简化了复杂的模拟。通常，ROM在使用特定空间离散化创建的输入模拟上进行训练，然后用于使用相同的离散化加速模拟。这种离散化依赖性是有限制的。独立于特定的离散化将提供在训练数据中混合和匹配网格分辨率、连通性和类型（四面体、六面体）的灵活性；以在训练过程中看不到的新颖离散化来加速模拟；以及加速在时间上或参数化地改变离散化的自适应模拟。我们提出了一种灵活的、独立于离散化的降阶建模方法。与传统ROM一样，我们将配置表示为位移场的线性组合。与传统的ROM不同，我们的位移场是从参考域上的每个点到相应位移矢量的连续映射；这些映射被表示为隐式神经场。使用线性连续ROM（LiCROM），我们的训练集可以包括经历多个加载条件的多个几何体，与它们的离散化无关。这为降阶建模的新应用打开了大门。我们现在可以加速在运行时修改几何体的模拟，例如通过切割、打孔，甚至交换整个网格。我们还可以加速对训练中看不见的几何形状的模拟。我们演示了一次性泛化，在单个几何体上进行训练，然后模拟各种看不见的几何体。 et.al.|[2310.15907](http://arxiv.org/abs/2310.15907)|null|
|**2023-10-12**|**S4C: Self-Supervised Semantic Scene Completion with Neural Fields**|三维语义场景理解是计算机视觉中的一个基本挑战。它使移动代理能够自主规划和导航任意环境。SSC将这一挑战形式化为从场景的稀疏观测中联合估计密集的几何结构和语义信息。当前的SSC方法通常基于聚合的激光雷达扫描在3D地面实况上进行训练。这一过程依赖于特殊的传感器和手工注释，这些传感器和注释成本高昂且规模不大。为了克服这个问题，我们的工作提出了第一种称为S4C的SSC自监督方法，该方法不依赖于3D地面实况数据。我们提出的方法可以从单个图像重建场景，并且只依赖于训练期间从现成的图像分割网络生成的视频和伪分割地面实况。与使用离散体素网格的现有方法不同，我们将场景表示为隐式语义场。该公式允许查询相机截锥体内的任何点的占用率和语义类。我们的架构是通过基于渲染的自监督损失进行训练的。尽管如此，我们的方法实现了接近于完全监督的最先进方法的性能。此外，我们的方法表现出强大的泛化能力，可以为遥远的视点合成准确的分割图。 et.al.|[2310.07522](http://arxiv.org/abs/2310.07522)|null|

<p align=right>(<a href=#updated-on-20231111>back to top</a>)</p>

[contributors-shield]: https://img.shields.io/github/contributors/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[contributors-url]: https://github.com/Vincentqyw/cv-arxiv-daily/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[forks-url]: https://github.com/Vincentqyw/cv-arxiv-daily/network/members
[stars-shield]: https://img.shields.io/github/stars/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[stars-url]: https://github.com/Vincentqyw/cv-arxiv-daily/stargazers
[issues-shield]: https://img.shields.io/github/issues/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[issues-url]: https://github.com/Vincentqyw/cv-arxiv-daily/issues

