[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]

## Updated on 2024.09.26
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
|**2024-09-24**|**GSplatLoc: Grounding Keypoint Descriptors into 3D Gaussian Splatting for Improved Visual Localization**|尽管存在各种视觉定位方法，如场景坐标和姿态回归，但这些方法往往难以满足高内存消耗或广泛的优化要求。为了应对这些挑战，我们利用新型视图合成的最新进展，特别是3D高斯散斑（3DGS），来增强定位。3DGS允许通过其空间特征对3D几何和场景外观进行紧凑编码。我们的方法利用了XFeat轻量级关键点检测和描述模型生成的密集描述图。我们建议将这些密集的关键点描述符提取到3DGS中，以提高模型的空间理解能力，从而通过2D-3D对应关系进行更准确的相机姿态预测。在估计初始姿态后，我们使用光度扭曲损失对其进行细化。对流行的室内和室外数据集进行基准测试表明，我们的方法超越了最先进的神经渲染姿势（NRP）方法，包括NeRFMatch和PNeRFLoc。 et.al.|[2409.16502](http://arxiv.org/abs/2409.16502)|null|
|**2024-09-24**|**Semantics-Controlled Gaussian Splatting for Outdoor Scene Reconstruction and Rendering in Virtual Reality**|高斯散点（GS）等3D渲染技术的进步允许在虚拟现实（VR）中进行新颖的视图合成和实时渲染。然而，GS创建的3D环境通常很难编辑。对于场景增强或合并3D资源，按类分割高斯分布是必不可少的。现有的分割方法通常仅限于某些类型的场景，例如“圆形”场景，以确定清晰的对象边界。然而，在非“循环”场景（如大型室外场景）中删除大型物体时，这种方法是无效的。我们提出了语义控制GS（SCGS），这是一种分段驱动的GS方法，能够在不受控制的自然环境中分离大型场景部分。SCGS允许对VR进行场景编辑和提取场景部分。此外，我们引入了一个具有挑战性的室外数据集，克服了“循环”设置。我们在数据集的视觉质量和3D-OVS数据集的分割质量方面都优于最先进的技术。我们进行了一项探索性用户研究，将360度视频、普通GS和VR中的SCGS与固定视点进行了比较。在我们随后的主要研究中，允许用户自由移动，评估普通GS和SCGS。我们的主要研究结果表明，参与者明显更喜欢SCGS而不是普通GS。我们总体上提出了一种创新的方法，在技术和用户体验方面都超越了最先进的水平。 et.al.|[2409.15959](http://arxiv.org/abs/2409.15959)|null|
|**2024-09-24**|**Disentangled Generation and Aggregation for Robust Radiance Fields**|近年来，基于三平面的辐射场的利用引起了人们的关注，因为它能够以高质量的表示和低计算成本有效地分离3D场景。该方法的一个关键要求是精确输入相机姿态。然而，由于三平面的局部更新特性，与之前的联合姿态NeRF优化类似的联合估计很容易导致局部最小值。为此，我们提出了解耦三平面生成模块，将全局特征上下文和平滑度引入三平面学习，从而减轻了局部更新引起的误差。然后，我们提出了解耦平面聚合来减轻相机姿态更新过程中常见的三平面特征聚合引起的纠缠。此外，我们引入了一种两阶段热启动训练策略，以减少由三平面生成器引起的隐式约束。定量和定性结果表明，我们提出的方法在具有噪声或未知相机姿态的新型视图合成中取得了最先进的性能，并实现了高效的优化收敛。项目页面：https://gaohchen.github.io/DiGARR/. et.al.|[2409.15715](http://arxiv.org/abs/2409.15715)|null|
|**2024-09-23**|**AgriNeRF: Neural Radiance Fields for Agriculture in Challenging Lighting Conditions**|神经辐射场（NeRF）在3D场景重建和新颖的视图合成方面显示出巨大的前景。在农业环境中，NeRF可以作为数字双胞胎，为农民提供有关水果检测的关键信息，用于产量估算和其他重要指标。然而，传统的NeRF对具有挑战性的照明条件（如低光、极亮的光和变化的照明）并不稳健。为了解决这些问题，这项工作利用了三种不同的传感器：RGB相机、事件相机和热像仪。我们的RGB场景重建显示，PSNR和SSIM分别提高了+2.06 dB和+8.3%。我们的交叉光谱场景重建使mAP50的下游水果检测提高了+43.0%，mAP50-95提高了+61.1%。额外传感器的集成带来了更强大和信息量更大的NeRF。我们证明，我们的多模态系统在各种树冠覆盖和一天中的不同时间产生了高质量的照片级逼真重建。这项工作的结果是开发了一种有弹性的NeRF，能够在明显退化的情况下表现良好，以及一种用于自动水果检测的学习交叉光谱表示。 et.al.|[2409.15487](http://arxiv.org/abs/2409.15487)|null|
|**2024-09-23**|**SpikeGS: Learning 3D Gaussian Fields from Continuous Spike Stream**|尖峰相机是一种专用的高速视觉传感器，与传统的帧相机相比，它具有高时间分辨率和高动态范围等优点。这些特征为相机在许多计算机视觉任务中提供了显著的优势。然而，基于尖峰相机的3D重建和新型视图合成的任务仍然不发达。尽管有从尖峰流中学习神经辐射场的现有方法，但它们要么在极其嘈杂、低质量的光照条件下缺乏鲁棒性，要么由于神经辐射场中使用的深度全连接神经网络和光线行进渲染策略，计算复杂度很高，难以恢复精细的纹理细节。相比之下，3DGS的最新进展通过将点云表示优化为高斯椭球体实现了高质量的实时渲染。在此基础上，我们介绍了SpikeGS，这是第一种仅从尖峰流中学习3D高斯场的方法。我们设计了一个基于3DGS的可微分尖峰流渲染框架，结合了噪声嵌入和尖峰神经元。通过利用3DGS的多视图一致性和基于图块的多线程并行渲染机制，我们实现了高质量的实时渲染结果。此外，我们引入了一个尖峰渲染损失函数，该函数在不同的光照条件下具有通用性。我们的方法可以从移动尖峰相机捕获的连续尖峰流中重建具有精细纹理细节的视图合成结果，同时在极其嘈杂的低光场景中表现出很高的鲁棒性。在真实和合成数据集上的实验结果表明，我们的方法在渲染质量和速度方面超越了现有的方法。我们的代码将在https://github.com/520jz/SpikeGS. et.al.|[2409.15176](http://arxiv.org/abs/2409.15176)|null|
|**2024-09-23**|**FusionRF: High-Fidelity Satellite Neural Radiance Fields from Multispectral and Panchromatic Acquisitions**|我们介绍了FusionRF，这是一种基于光学未处理卫星图像的新型神经渲染地形重建方法。虽然以前的方法依赖于外部泛色法来融合低分辨率多光谱图像和高分辨率全色图像，但FusionRF直接在没有先验知识的情况下基于光学未处理的采集进行重建。这是通过添加一个锐化内核来实现的，该内核对多光谱图像中的分辨率损失进行建模。此外，新颖的模态嵌入允许模型执行图像融合，这是新颖视图合成的瓶颈。我们在不同位置对WorldView-3卫星的多光谱和全色卫星图像进行了评估，FusionRF在未处理图像的深度重建、渲染清晰的训练和新颖的视图以及保留多光谱信息方面优于之前的最先进方法。 et.al.|[2409.15132](http://arxiv.org/abs/2409.15132)|null|
|**2024-09-23**|**AIM 2024 Sparse Neural Rendering Challenge: Methods and Results**|本文回顾了稀疏神经渲染的挑战，这是与ECCV 2024联合举办的图像处理进展（AIM）研讨会的一部分。本文重点介绍了比赛设置、提出的方法及其各自的结果。该挑战旨在从稀疏图像观测中生成不同场景的新颖相机视图合成。它由两条轨道组成，具有不同程度的稀疏性；Track 1中有3个视图（非常稀疏），Track 2中有9个视图（稀疏）。参与者被要求优化通过峰值信噪比（PSNR）度量测量的地面实况图像的客观保真度。对于这两个轨道，我们使用新引入的稀疏渲染（SpaRe）数据集和流行的DTU MVS数据集。在本次挑战中，5支队伍向Track 1提交了最终成绩，4支队伍向Track2提交了最终结果。提交的模型多种多样，突破了稀疏神经渲染的最新技术。本文详细描述了在挑战中开发的所有模型。 et.al.|[2409.15045](http://arxiv.org/abs/2409.15045)|null|
|**2024-09-23**|**AIM 2024 Sparse Neural Rendering Challenge: Dataset and Benchmark**|可微分和神经渲染的最新发展在各种2D和3D任务中取得了令人印象深刻的突破，例如新颖的视图合成、3D重建。通常，可微分渲染依赖于场景的密集视点覆盖，这样几何体就可以单独从外观观察中消除歧义。当只有少数输入视图可用时，会出现一些挑战，通常称为稀疏或少镜头神经渲染。由于这是一个约束不足的问题，大多数现有方法都引入了正则化的使用，以及各种学习和手工制作的先验。稀疏渲染文献中反复出现的一个问题是缺乏同质、最新的数据集和评估协议。虽然高分辨率数据集是密集重建文献中的标准，但稀疏渲染方法通常使用低分辨率图像进行评估。此外，不同手稿之间的数据分割不一致，测试地面真实图像通常是公开的，这可能会导致过度拟合。在这项工作中，我们提出了稀疏渲染（SpaRe）数据集和基准测试。我们引入了一个遵循DTU MVS数据集设置的新数据集。该数据集由97个基于合成高质量资产的新场景组成。每个场景最多有64个相机视图和7个照明配置，以1600x1200分辨率渲染。我们发布了82个场景的训练分割，以培养可推广的方法，并为验证和测试集提供了一个在线评估平台，其真实图像保持隐藏。我们提出了两种不同的稀疏配置（分别为3幅和9幅输入图像）。这为可重复评估提供了一个强大而方便的工具，并使研究人员能够轻松访问具有最先进绩效评分的公共排行榜。可用网址：https://sparebenchmark.github.io/ et.al.|[2409.15041](http://arxiv.org/abs/2409.15041)|null|
|**2024-09-22**|**MVPGS: Excavating Multi-view Priors for Gaussian Splatting from Sparse Input Views**|最近，神经辐射场（NeRF）的进步促进了少镜头新视图合成（NVS），这是3D视觉应用中的一个重大挑战。尽管多次尝试降低NeRF中的密集输入要求，但它仍然受到耗时的训练和渲染过程的困扰。最近，3D高斯散斑（3DGS）通过显式的基于点的表示实现了实时高质量的渲染。然而，与NeRF类似，由于缺乏约束，它往往会过度拟合训练视图。在本文中，我们提出了\textbf{MVPGS}，这是一种基于3D高斯散斑挖掘多视图先验的少镜头NVS方法。我们利用最近基于学习的多视图立体（MVS）来提高3DGS的几何初始化质量。为了减轻过拟合，我们提出了一种基于计算几何的前向扭曲方法，用于符合场景的额外外观约束。此外，我们为高斯参数引入了视图一致的几何约束，以促进适当的优化收敛，并利用单目深度正则化作为补偿。实验表明，该方法在实时渲染速度方面达到了最先进的性能。项目页面：https://zezeaaa.github.io/projects/MVPGS/ et.al.|[2409.14316](http://arxiv.org/abs/2409.14316)|null|
|**2024-09-19**|**GStex: Per-Primitive Texturing of 2D Gaussian Splatting for Decoupled Appearance and Geometry Modeling**|高斯飞溅在视图合成和场景重建方面表现出了出色的性能。该表示通过优化场景中数千到数百万个2D或3D高斯图元的位置、比例、颜色和不透明度来实现逼真的质量。然而，由于每个高斯基元都编码外观和几何体，因此这些属性是强耦合的——因此，即使场景几何体很简单（例如，对于纹理平面），高保真外观建模也需要大量的高斯基元。我们建议对每个2D高斯基元进行纹理处理，这样即使是单个高斯基元也可以用来捕捉外观细节。通过采用每基元纹理，我们的外观表示与场景几何体的拓扑结构和复杂性无关。我们证明，我们的方法GStex在纹理高斯斑点方面比之前的工作产生了更好的视觉质量。此外，我们证明，与2D高斯散点相比，当减少高斯基元的数量时，我们的解耦能够提高新颖的视图合成性能，并且GStex可用于场景外观编辑和重新纹理化。 et.al.|[2409.12954](http://arxiv.org/abs/2409.12954)|null|

<p align=right>(<a href=#updated-on-20240926>back to top</a>)</p>

## 3D Reconstruction

|Publish Date|Title|Abstract|PDF|Code|
|---|---|---|---|---|
|**2024-09-25**|**Generative Object Insertion in Gaussian Splatting with a Multi-View Diffusion Model**|生成新对象并将其插入到3D内容中是实现多功能场景再现的一种引人注目的方法。现有的方法依赖于SDS优化或单视图修复，往往难以产生高质量的结果。为了解决这个问题，我们提出了一种在高斯散斑表示的3D内容中插入对象的新方法。我们的方法引入了一个名为MVInpainter的多视图扩散模型，该模型基于预训练的稳定视频扩散模型构建，以促进视图一致的对象修复。在MVInpainter中，我们整合了一个基于ControlNet的条件注入模块，以实现受控和更可预测的多视图生成。在生成多视图修复结果后，我们进一步提出了一种掩模感知的3D重建技术，从这些稀疏的修复视图中改进高斯散斑重建。通过利用这些制造技术，我们的方法产生了不同的结果，确保了视图一致和和谐的插入，并产生了更好的物体质量。大量实验表明，我们的方法优于现有方法。 et.al.|[2409.16938](http://arxiv.org/abs/2409.16938)|**[link](https://github.com/jiutongbro/multiview_inpaint)**|
|**2024-09-25**|**Discriminative Anchor Learning for Efficient Multi-view Clustering**|多视图聚类旨在研究视图之间的互补信息并发现底层结构。为了解决现有方法相对较高的计算成本，最近提出了基于锚点的工作。即使具有可接受的聚类性能，这些方法也倾向于将来自多个视图的原始表示映射到基于原始数据集的固定共享图中。然而，大多数研究忽略了学习锚的判别特性，这破坏了所构建模型的表示能力。此外，通过简单地学习共享锚点图而不考虑视图特定锚点的质量，可以忽略跨视图锚点之间的互补信息。本文提出了用于多视图聚类的判别锚学习（DALMC）来处理上述问题。我们根据原始数据集学习区分视图特定的特征表示，并基于这些表示从不同视图构建锚点，从而提高了共享锚点图的质量。将判别特征学习和共识锚图构建集成到一个统一的框架中，相互改进，实现细化。通过正交约束学习来自多个视图的最优锚点和共识锚点图。我们给出了一个迭代算法来处理公式化问题。在不同数据集上的大量实验表明，与其他方法相比，我们的方法具有有效性和效率。 et.al.|[2409.16904](http://arxiv.org/abs/2409.16904)|null|
|**2024-09-25**|**Towards Unified 3D Hair Reconstruction from Single-View Portraits**|由于不同发型之间存在广泛的形状变化，单视图3D头发重建具有挑战性。目前最先进的方法专门用于恢复未编织的3D头发，并且经常将编织风格作为失败案例，因为无论是基于规则还是基于数据，都很难定义复杂发型的先验。我们提出了一种新的策略，通过统一的管道实现各种头发类型的单视图3D重建。为了实现这一目标，我们首先收集了一个大规模的合成多视图头发数据集SynMvHair，其中包含编织和非编织风格的各种3D头发，并学习了两个专门针对头发的扩散先验。然后，我们使用两个专门设计的模块（即视图和像素高斯细化）从先验中优化基于3D高斯的头发。我们的实验表明，通过统一的方法从单视图图像重建编织和非编织的3D头发是可能的，我们的方法在恢复复杂发型方面达到了最先进的性能。值得一提的是，我们的方法对真实图像显示出良好的泛化能力，尽管它从合成数据中学习头发先验。 et.al.|[2409.16863](http://arxiv.org/abs/2409.16863)|null|
|**2024-09-25**|**3DDX: Bone Surface Reconstruction from a Single Standard-Geometry Radiograph via Dual-Face Depth Estimation**|射线照相因其经济实惠和低辐射暴露而广泛应用于骨科。从单个射线照片进行3D重建，即所谓的2D-3D重建，提供了各种临床应用的可能性，但实现临床可行的准确性和计算效率仍然是一个未解决的挑战。与计算机视觉的其他领域不同，X射线成像的独特特性，如射线穿透和固定几何形状，尚未得到充分利用。我们提出了一种新方法，可以同时学习从X射线图像中导出的多个深度图（多个骨骼的前表面和后表面），以进行计算机断层扫描配准。该方法不仅利用了X射线成像的固定几何特性，而且提高了整个表面重建的精度。我们的研究涉及600张CT和2651张X射线图像（每位患者4至5张摆位X射线图像），证明了我们的方法优于传统方法，表面重建误差从4.78毫米减少到1.96毫米。这一显著的精度提高和计算效率的提高表明了我们的方法在临床应用中的潜力。 et.al.|[2409.16702](http://arxiv.org/abs/2409.16702)|null|
|**2024-09-24**|**Frequency-based View Selection in Gaussian Splatting Reconstruction**|三维重建是机器人感知中的一个基本问题。我们研究了主动视图选择的问题，以尽可能少的输入图像进行3D高斯散斑重建。尽管3D高斯散斑在图像渲染和3D重建方面取得了重大进展，但重建的质量受到2D图像选择和通过运动结构（SfM）算法估计相机姿态的强烈影响。目前选择直接依赖于遮挡、深度模糊或神经网络预测的不确定性的视图的方法不足以处理这个问题，并且很难推广到新的场景。通过在频域中对潜在视图进行排序，我们能够在没有地面实况数据的情况下有效地估计新视图的潜在信息增益。通过克服当前对模型架构和效率的限制，我们的方法在视图选择方面取得了最先进的结果，展示了其高效基于图像的3D重建的潜力。 et.al.|[2409.16470](http://arxiv.org/abs/2409.16470)|null|
|**2024-09-24**|**Underground Mapping and Localization Based on Ground-Penetrating Radar**|近年来，基于深度神经网络的三维物体重建越来越受到人们的关注。然而，对地下物体进行3D重建以生成点云图仍然是一个挑战。探地雷达（GPR）是探测和定位植物根系和管道等地下物体最强大、使用最广泛的工具之一，具有成本效益和不断发展的技术。本文介绍了一种基于深度卷积神经网络的抛物线信号检测网络，该网络利用探地雷达传感器的B扫描图像。检测到的关键点可以帮助精确拟合抛物线，用于将原始GPR B扫描图像解释为对象模型的横截面。此外，设计了一个多任务点云网络，可以同时执行点云分割和完成，填充稀疏点云地图。对于未知位置，GPR A扫描数据可用于匹配所构建地图中的相应A扫描数据，精确定位位置以验证模型构建地图的准确性。实验结果证明了我们方法的有效性。 et.al.|[2409.16446](http://arxiv.org/abs/2409.16446)|null|
|**2024-09-24**|**Age of Gossip in Networks with Multiple Views of a Source**|我们考虑网络中的信息版本年龄（AoI），其中节点子集充当感测节点，对通常可以遵循连续分布的源进行采样。源的任何样本都构成了信息的新版本，信息的版本年龄是根据整个网络可用信息的最新版本定义的。我们推导出了节点不同子集之间的平均版本AoI的递归表达式，可用于评估包括任何单个节点在内的任何节点子集的平均版本AoI。我们推导了各种拓扑结构（包括线、环和全连接网络）在网络任何单个节点上的平均AoI的渐近行为。Yates关于网络版本年龄的现有技术结果[ISIT'21]在我们的推导中可以被解释为具有单一源视图的网络，例如通过速率为 $\lambda_{00}$的泊松过程。我们的结果表明，通过分割相同的速率$\lambda_{00}$，将源的单个视图替换为跨多个节点的分布式感知，平均版本AoI性能没有损失。特别地，我们证明，对于全连接和环形网络，平均AoI分别渐近地缩放为$O（\log（n））$和$O（\sqrt{n}）$。更有趣的是，我们表明，对于环形网络，如果感测节点的数量仅随$O（\sqrt{n}）$而不是需要$O（n）$的先前已知结果缩放，则分布式感测在平均AoI上仍然可以实现相同的$O（$sqrt{n}）$渐近性能。我们的结果表明，只要连续非感测节点的最大数量也缩放为$O（\sqrt{n}）$ ，就可以任意选择感测节点。 et.al.|[2409.16285](http://arxiv.org/abs/2409.16285)|null|
|**2024-09-24**|**AIR-Embodied: An Efficient Active 3DGS-based Interaction and Reconstruction Framework with Embodied Large Language Model**|3D重建和神经渲染的最新进展增强了高质量数字资产的创建，但现有的方法很难在不同的对象形状、纹理和遮挡之间进行推广。虽然次优视图（NBV）规划和基于学习的方法提供了解决方案，但它们往往受到预定义标准的限制，无法用人类的常识来管理遮挡。为了解决这些问题，我们提出了AIR Embodied，这是一种新的框架，将嵌入的AI代理与大规模预训练的多模态语言模型集成在一起，以改进主动3DGS重建。AIR Embodied采用了一个三阶段过程：通过多模态提示了解当前的重建状态，通过视点选择和交互动作规划任务，并采用闭环推理来确保准确执行。代理根据计划结果和实际结果之间的差异动态改进其操作。在虚拟和现实世界环境中的实验评估表明，AIR Embodied显著提高了重建效率和质量，为主动3D重建中的挑战提供了一个稳健的解决方案。 et.al.|[2409.16019](http://arxiv.org/abs/2409.16019)|null|
|**2024-09-23**|**Matérn Kernels for Tunable Implicit Surface Reconstruction**|我们建议使用Mat'ern核家族进行可调隐式曲面重建，以最近成功的定向点云三维重建核方法为基础。正如我们所展示的，从理论和实践的角度来看，Mat'ern核都有一些吸引人的特性，使其特别适合曲面重建——优于基于弧余弦核的最先进方法，同时更容易实现、计算更快、可扩展。由于是平稳的，我们证明了Mat'ern核'光谱可以以与傅里叶特征映射相同的方式进行调整，以帮助基于坐标的MLP克服光谱偏差。此外，我们从理论上分析了Mat'ern核与SIREN网络的连接，以及它与以前使用的弧余弦核的关系。最后，基于最近引入的神经核域，我们提出了数据依赖的Mat'ern核，并得出结论，特别是拉普拉斯核（作为Mat'ern家族的一部分）具有极强的竞争力，在无噪声的情况下，其性能几乎与最先进的方法相当，同时训练时间缩短了五倍以上。 et.al.|[2409.15466](http://arxiv.org/abs/2409.15466)|**[link](https://github.com/mweiherer/matern-surface-reconstruction)**|
|**2024-09-23**|**ReLoo: Reconstructing Humans Dressed in Loose Garments from Monocular Video in the Wild**|虽然前几年在从单眼视频中重建人类的3D方面取得了很大进展，但很少有最先进的方法能够处理在关节运动过程中表现出较大非刚性表面变形的宽松服装。这限制了这种方法在穿着标准裤子或T恤的人身上的应用。我们的方法ReLoo克服了这一局限性，从野生视频中的单眼重建了穿着宽松衣服的人的高质量3D模型。为了解决这个问题，我们首先建立了一个分层的神经人体表示，将穿着衣服的人分解为神经内体和外衣。在分层神经表示的基础上，我们进一步为服装层引入了一个可以自由移动的非分层虚拟骨变形模块，这使得非刚性变形的宽松服装能够准确恢复。全局优化通过多层可微体绘制联合优化人体和服装的形状、外观和变形。为了评估ReLoo，我们在多视图捕捉工作室中记录了具有动态变形服装的主题。对现有数据集和我们的新数据集的评估表明，ReLoo在室内数据集和野外视频上都明显优于现有技术。 et.al.|[2409.15269](http://arxiv.org/abs/2409.15269)|null|

<p align=right>(<a href=#updated-on-20240926>back to top</a>)</p>

## Diffusion

|Publish Date|Title|Abstract|PDF|Code|
|---|---|---|---|---|
|**2024-09-25**|**DreamWaltz-G: Expressive 3D Gaussian Avatars from Skeleton-Guided 2D Diffusion**|利用预训练的2D扩散模型和分数蒸馏采样（SDS），最近的方法在文本到3D化身生成方面显示出了有前景的结果。然而，生成能够表现动画的高质量3D化身仍然具有挑战性。在这项工作中，我们提出了DreamWaltz-G，这是一个用于从文本生成可动画3D化身的新颖学习框架。该框架的核心在于骨架引导的分数蒸馏和混合3D高斯化身表示。具体而言，所提出的骨架引导分数蒸馏将来自3D人体模板的骨架控制集成到2D扩散模型中，增强了SDS监督在视图和人体姿势方面的一致性。这有助于生成高质量的化身，缓解多张脸、额外肢体和模糊等问题。所提出的混合3D高斯化身表示建立在高效的3D高斯模型的基础上，结合神经隐式场和参数化3D网格，实现实时渲染、稳定的SDS优化和富有表现力的动画。大量实验表明，DreamWaltz-G在生成和制作3D化身动画方面非常有效，在视觉质量和动画表现力方面都优于现有方法。我们的框架还支持多种应用，包括人类视频重现和多主题场景合成。 et.al.|[2409.17145](http://arxiv.org/abs/2409.17145)|null|
|**2024-09-25**|**Language-oriented Semantic Communication for Image Transmission with Fine-Tuned Diffusion Model**|新兴应用中无处不在的图像传输给有限的无线资源带来了巨大的开销。由于该文本具有用很少的数据传达大量信息的特性，因此传输图像的描述性文本可以减少传输的数据量。在此背景下，本文基于文本2图像生成模型（Gen SC）开发了一种新的语义交流框架。具体而言，发射器将输入图像转换为文本模态数据。然后，文本通过嘈杂的信道传输到接收器。然后，接收器使用接收到的文本生成图像。此外，为了提高噪声信道上文本传输的鲁棒性，我们设计了一种基于变换器的文本传输编解码器模型。此外，我们通过微调扩散模型来获得个性化的知识库，以满足面向任务的传输场景的要求。仿真结果表明，所提出的框架可以实现高感知质量，将传输的数据量减少高达99%，并且在肖像图像传输方面对无线信道噪声具有鲁棒性。 et.al.|[2409.17104](http://arxiv.org/abs/2409.17104)|null|
|**2024-09-25**|**Effects of the internal temperature on vertical mixing and on cloud structures in Ultra Hot Jupiters**|热木星大气中的垂直混合在其大气中云粒子的形成和空间分布中起着至关重要的作用。这会通过云不透明度影响行星的观测光谱，而云不透明度可能受到深层大气中难熔物种的冷捕获程度的影响。我们的目标是分离内部温度对超热木星（UHJ）大气中混合效率的影响以及全球云粒子的空间分布。我们将简化的基于示踪剂的云模型、栅栏辐射传输方案和混合长度理论与Exo-FMS大气环流模型相结合。我们在典型的超高压大气系统参数下运行了五个不同内部温度的模型。我们的结果表明，对流涡旋扩散系数在绝大多数大气中保持较低水平，混合以平流为主。然而，对于较冷的内部温度，一些地区可以在高层大气中显示对流混合。随着内部温度的升高，云层的垂直范围减小。此外，在较冷的情况下，在辐射对流边界（RCB）下方形成全球云层。由于其强烈的辐射，RCB上方的超高压大气中的对流通常受到强烈抑制。与平流混合相比，对流混合在使内部温暖的超热木星中的云粒子保持在高空方面起着次要作用。较高的垂直湍流热通量和潜在温度的平流抑制了较温暖内部的对流。我们的研究结果表明，冷室内上方的孤立高层大气区域可能在罗斯比环流周围的孤立区域表现出强烈的对流混合，使气溶胶能够更好地保留在这些区域。 et.al.|[2409.17101](http://arxiv.org/abs/2409.17101)|null|
|**2024-09-25**|**Ctrl-GenAug: Controllable Generative Augmentation for Medical Sequence Classification**|在医学领域，大规模数据集的有限可用性和劳动密集型的注释过程阻碍了深度模型的性能。基于扩散的生成增强方法为这个问题提供了一个有前景的解决方案，已被证明在推进下游医学识别任务方面是有效的。然而，现有的工作缺乏足够的语义和顺序可操纵性来挑战视频/3D序列生成，并忽视了噪声合成样本的质量控制，导致合成数据库不可靠，严重限制了下游任务的性能。在这项工作中，我们提出了Ctrl-GenAug，这是一种新颖而通用的生成增强框架，可以实现高度语义和顺序的定制序列合成，并抑制不正确合成的样本，以帮助医学序列分类。具体来说，我们首先设计了一个多模态条件引导序列生成器，用于可控地合成诊断促进样本。集成了顺序增强模块，以增强生成样本的时间/立体相干性。然后，我们提出了一种噪声合成数据过滤器，在语义和序列级别抑制不可靠的情况。在3个医学数据集上进行了广泛的实验，使用在3个范式上训练的11个网络，全面分析了Ctrl-GenAug的有效性和普遍性，特别是在代表性不足的高危人群和域外条件下。 et.al.|[2409.17091](http://arxiv.org/abs/2409.17091)|null|
|**2024-09-25**|**Degradation-Guided One-Step Image Super-Resolution with Diffusion Priors**|基于扩散的图像超分辨率（SR）方法通过利用大型预训练的文本到图像扩散模型作为先验，取得了显著的成功。然而，这些方法仍然面临着两个挑战：需要几十个采样步骤才能获得令人满意的结果，这限制了实际场景中的效率，以及忽视了退化模型，而退化模型是解决SR问题的关键辅助信息。在这项工作中，我们引入了一种新的一步SR模型，该模型显著解决了基于扩散的SR方法的效率问题。与现有的微调策略不同，我们设计了一个专门用于SR的退化引导低秩自适应（LoRA）模块，该模块根据低分辨率图像的预估退化信息来校正模型参数。该模块不仅促进了强大的数据依赖或退化依赖的SR模型，而且尽可能地保留了预训练扩散模型的生成先验。此外，我们通过引入在线负样本生成策略来定制一种新的训练管道。结合推理过程中的无分类器引导策略，大大提高了超分辨率结果的感知质量。大量实验表明，与最近最先进的方法相比，所提出的模型具有更高的效率和有效性。 et.al.|[2409.17058](http://arxiv.org/abs/2409.17058)|**[link](https://github.com/arctichare105/s3diff)**|
|**2024-09-25**|**ControlCity: A Multimodal Diffusion Model Based Approach for Accurate Geospatial Data Generation and Urban Morphology Analysis**|志愿者地理信息（VGI）以其种类丰富、数量庞大、更新迅速、来源多样等特点，已成为地理空间数据的重要来源。然而，来自OSM等平台的VGI数据在不同数据类型之间表现出显著的质量异质性，特别是在城市建筑数据方面。为了解决这个问题，我们提出了一种多源地理数据转换解决方案，利用可访问和完整的VGI数据来协助生成城市建筑足迹数据。我们还采用了多模态数据生成框架来提高准确性。首先，我们介绍了一种用于构建“图像-文本元数据构建足迹”数据集的管道，主要基于道路网络数据，并辅以其他多模态数据。然后，我们提出了ControlCity，这是一种基于多模态扩散模型的地理数据转换方法。该方法首先使用预训练的文本到图像模型来对齐文本、元数据和建筑足迹数据。改进的ControlNet进一步整合了道路网络和土地使用图像，生成了精确的建筑足迹数据。在全球22个城市进行的实验表明，ControlCity成功模拟了真实的城市建筑模式，实现了最先进的性能。具体来说，我们的方法实现了平均FID得分50.94，与领先方法相比误差降低了71.01%，MIoU得分为0.36，提高了38.46%。此外，我们的模型在城市形态转移、零样本城市生成和空间数据完整性评估等任务中表现出色。在零样本城市任务中，我们的方法准确预测并生成类似的城市结构，具有较强的泛化能力。这项研究证实了我们的方法在生成城市建筑足迹数据和捕捉复杂城市特征方面的有效性。 et.al.|[2409.17049](http://arxiv.org/abs/2409.17049)|**[link](https://github.com/fangshuoz/controlcity)**|
|**2024-09-25**|**GeoBiked: A Dataset with Geometric Features and Automated Labeling Techniques to Enable Deep Generative Models in Engineering Design**|我们提供了一个数据集，用于在工程设计中启用深度生成模型（DGM），并提出了利用大规模基础模型自动标记数据的方法。GeoBiked包含4355张自行车图像，并附有结构和技术特征注释，用于研究两种自动标记技术：利用图像生成模型中的合并潜在特征（Hyperfeatures）来检测结构图像中的几何对应关系（例如车轮中心的位置），以及为结构图像生成不同的文本描述。GPT-4o是一种视觉语言模型（VLM），被指示分析图像并生成与系统提示一致的各种描述。通过将技术图像表示为扩散超特征，可以绘制它们之间的几何对应关系。通过呈现多个带注释的源图像，提高了看不见样本中几何点的检测精度。GPT-4o具有足够的能力来生成技术图像的准确描述。将这一代人仅仅建立在图像上会导致不同的描述，但会导致幻觉，而将其建立在分类标签上则会限制多样性。将两者都用作输入，可以平衡创造力和准确性。成功使用Hyperfeatures进行几何对应表明，这种方法可用于技术图像中的一般点检测和注释任务。使用VLM用文本描述标记这些图像是可能的，但这取决于模型检测能力、仔细的提示工程和输入信息的选择。在工程设计中应用基础模型在很大程度上尚未得到探索。我们的目标是通过数据集弥合这一差距，探索该领域的训练、微调和调节DGM，并提出引导基础模型处理技术图像的方法。 et.al.|[2409.17045](http://arxiv.org/abs/2409.17045)|null|
|**2024-09-25**|**Cloud technologies, firm growth and industry concentration: Evidence from France**|最近的实证证据表明，数字化与行业集中度之间存在正相关关系。然而，ICT可能并不都是一样的。我们研究了购买云服务对法国公司长期规模增长率的影响。我们的研究结果表明，云服务对公司增长率有积极影响，与大公司相比，小公司获得了更大的利益。这一证据表明，云技术的传播可能有助于减轻数字转型时代的集中度，有利于小型企业的数字化和增长，特别是在提供的云服务更先进的情况下。 et.al.|[2409.17035](http://arxiv.org/abs/2409.17035)|null|
|**2024-09-25**|**Decomposition of Friction Coefficients to Analyze Hydration Effects on a C $_{60}$(OH)$_{\rm n}$**|为了分析水合作用对大分子扩散的影响，使用全原子模型的分子动力学模拟研究了大分子的摩擦系数。在本研究中，引入了一种将分子摩擦系数分解为大分子上每个位点的贡献的方法。该方法应用于环境水中的几种富勒烯。亲水部分（如OH基团）的摩擦系数大于疏水部分（如C基团）的。水合效应不仅取决于官能团的种类，还取决于表面粗糙度。这种方法将有助于解释实验观察到的蛋白质扩散系数的大幅变化，这些变化伴随着构象的变化。 et.al.|[2409.17028](http://arxiv.org/abs/2409.17028)|null|
|**2024-09-25**|**Single Image, Any Face: Generalisable 3D Face Generation**|从单个无约束图像创建3D人脸化身是众多现实世界视觉和图形应用程序的基础任务。尽管在生成模型方面取得了重大进展，但现有的方法要么不太适合人脸设计，要么无法从限制性的训练领域推广到无约束的面部图像。为了解决这些局限性，我们提出了一种新的模型Gen3D Face，该模型在多视图一致扩散框架内生成具有无约束单图像输入的3D人脸。给定特定的输入图像，我们的模型首先生成多视图图像，然后进行神经表面构建。为了以通用的方式整合人脸几何信息，我们使用输入条件网格估计代替地面真实网格以及合成的多视图训练数据。重要的是，我们引入了一种多视图联合生成方案，以提高不同视图之间的外观一致性。据我们所知，这是第一次尝试和基准测试，从单个图像为跨领域的通用人类主体创建逼真的3D人脸化身。大量实验证明，我们的方法在域外单幅图像3D人脸生成和域内设置的顶级竞争方面优于之前的替代方案。 et.al.|[2409.16990](http://arxiv.org/abs/2409.16990)|null|

<p align=right>(<a href=#updated-on-20240926>back to top</a>)</p>

## NeRF

|Publish Date|Title|Abstract|PDF|Code|
|---|---|---|---|---|
|**2024-09-25**|**TalkinNeRF: Animatable Neural Fields for Full-Body Talking Humans**|我们介绍了一种新的框架，该框架从单眼视频中学习全身说话的人的动态神经辐射场（NeRF）。之前的工作只代表身体姿势或面部。然而，人类通过全身进行交流，结合身体姿势、手势和面部表情。在这项工作中，我们提出了TalkinNeRF，这是一个基于NeRF的统一网络，代表了整体4D人体运动。给定一个受试者的单眼视频，我们学习身体、面部和手的相应模块，这些模块结合在一起生成最终结果。为了捕捉复杂的手指关节，我们学习了手的额外变形场。我们的多身份表示能够同时训练多个科目，以及在完全看不见的姿势下进行强大的动画。只要输入一段短视频，它也可以推广到新的身份。我们展示了最先进的性能，用于为全身说话的人类制作动画，具有精细的手部发音和面部表情。 et.al.|[2409.16666](http://arxiv.org/abs/2409.16666)|null|
|**2024-09-24**|**Generative 3D Cardiac Shape Modelling for In-Silico Trials**|我们提出了一种深度学习方法，基于将形状表示为神经有符号距离场的零级集，对合成主动脉形状进行建模和生成，该方法受一系列可训练的嵌入向量的约束，并对每个形状的几何特征进行编码。通过使神经场在采样表面点上消失并强制其空间梯度具有单位范数，在从CT图像重建的主动脉根部网格数据集上训练网络。实证结果表明，我们的模型可以高保真地表示主动脉形状。此外，通过从学习到的嵌入向量中采样，我们可以生成类似于真实患者解剖结构的新形状，可用于计算机模拟试验。 et.al.|[2409.16058](http://arxiv.org/abs/2409.16058)|null|
|**2024-09-21**|**MOSE: Monocular Semantic Reconstruction Using NeRF-Lifted Noisy Priors**|由于缺乏几何指导和不完美的视图相关2D先验，从单眼图像中精确重建密集和语义注释的3D网格仍然是一项具有挑战性的任务。尽管我们已经见证了隐式神经场景表示的最新进展，能够简单地从多视图图像中进行精确的2D渲染，但很少有研究仅使用单眼先验来解决3D场景理解问题。在本文中，我们提出了MOSE，这是一种神经场语义重建方法，可以将推断的图像级噪声先验提升到3D，在3D和2D空间中产生精确的语义和几何。我们方法的关键动机是利用通用类不可知的分段掩码作为指导，在训练过程中促进渲染语义的局部一致性。在语义的帮助下，我们进一步将平滑正则化应用于无纹理区域，以获得更好的几何质量，从而实现几何和语义的互惠互利。在ScanNet数据集上的实验表明，我们的MOSE在3D语义分割、2D语义分割和3D表面重建任务的所有指标上都优于相关基线。 et.al.|[2409.14019](http://arxiv.org/abs/2409.14019)|null|
|**2024-09-17**|**SplatFields: Neural Gaussian Splats for Sparse 3D and 4D Reconstruction**|从多视图图像中数字化3D静态场景和4D动态事件长期以来一直是计算机视觉和图形学领域的一个挑战。最近，3D高斯散斑（3DGS）已经成为一种实用且可扩展的重建方法，由于其令人印象深刻的重建质量、实时渲染能力以及与广泛使用的可视化工具的兼容性而越来越受欢迎。然而，该方法需要大量的输入视图来实现高质量的场景重建，这引入了一个重大的实际瓶颈。在捕捉动态场景时，这一挑战尤为严峻，因为部署广泛的相机阵列的成本可能高得令人望而却步。在这项工作中，我们发现斑点特征缺乏空间自相关性是导致3DGS技术在稀疏重建环境中性能不佳的因素之一。为了解决这个问题，我们提出了一种优化策略，通过将splat特征建模为相应隐式神经场的输出，有效地正则化splat特征。这导致在各种场景中重建质量的一致提高。我们的方法有效地处理了静态和动态情况，这在不同设置和场景复杂性的广泛测试中得到了证明。 et.al.|[2409.11211](http://arxiv.org/abs/2409.11211)|null|
|**2024-09-17**|**Neural Fields for Adaptive Photoacoustic Computed Tomography**|光声计算机断层扫描（PACT）是一种具有广泛医学应用的非侵入性成像技术。传统的PACT图像重建算法受到组织中声速不均匀（SOS）引起的波前失真的影响，导致图像质量下降。考虑到这些影响可以提高图像质量，但测量SOS分布的实验成本很高。另一种方法是仅使用PA信号对初始压力图像和SOS进行联合重建。现有的关节重建方法存在局限性：计算成本高，无法直接恢复SOS，以及依赖于不准确的简化假设。隐式神经表示或神经场是计算机视觉中的一种新兴技术，用于通过基于坐标的神经网络学习物理场的有效和连续表示。在这项工作中，我们介绍了NF-APACT，这是一种高效的自监督框架，利用神经场来估计SOS，以实现准确和鲁棒的多通道解卷积。我们的方法比现有方法更快、更准确地消除了SOS像差。我们在一个新的数值体模以及实验收集的体模和体内数据上证明了我们的方法的成功。我们的代码和数字幻影可在https://github.com/Lukeli0425/NF-APACT. et.al.|[2409.10876](http://arxiv.org/abs/2409.10876)|null|
|**2024-09-09**|**Lagrangian Hashing for Compressed Neural Field Representations**|我们提出了拉格朗日散列，这是一种神经场的表示，结合了依赖于欧拉网格（即~InstantNGP）的快速训练NeRF方法的特征，以及使用配备有特征的点作为表示信息的方法（例如3D高斯散点或PointNeRF）。我们通过将基于点的表示合并到InstantNGP表示的分层哈希表的高分辨率层中来实现这一点。由于我们的点具有影响域，因此我们的表示可以被解释为哈希表中存储的高斯混合。我们提出的损失鼓励我们的高斯人向需要更多代表预算才能充分代表的地区移动。我们的主要发现是，我们的表示允许使用更紧凑的表示来重建信号，而不会影响质量。 et.al.|[2409.05334](http://arxiv.org/abs/2409.05334)|null|
|**2024-09-08**|**Exploring spectropolarimetric inversions using neural fields. Solar chromospheric magnetic field under the weak-field approximation**|全斯托克斯偏振数据集来源于狭缝光谱仪或窄带滤光片图，如今已被常规采集。随着二维光谱偏振仪和允许长时间高质量观测序列的观测技术的出现，数据速率正在增加。在光谱偏振反演中，显然需要通过利用推断物理量的时空相干性来超越传统的逐像素策略。我们探索了神经网络作为时间和空间（也称为神经场）上物理量的连续表示的潜力，用于光谱极化反演。我们已经实现并测试了一个神经场，以在弱场近似（WFA）下执行磁场矢量的推理（也称为物理知情神经网络的方法）。通过使用神经场来描述磁场矢量，我们可以通过假设物理量是坐标的连续函数来在空间和时间域中正则化解。我们研究了Ca II 8542 A谱线的合成和真实观测结果。我们还探讨了其他显式正则化的影响，例如使用外推磁场的信息或色球原纤维的取向。与传统的逐像素反演相比，神经场方法提高了磁场矢量重建的保真度，特别是横向分量。这种隐式正则化是一种提高观测值有效信噪比的方法。虽然它比逐像素WFA估计慢，但这种方法通过减少自由参数的数量并在解决方案中引入时空约束，显示出深度分层反演的巨大潜力。 et.al.|[2409.05156](http://arxiv.org/abs/2409.05156)|**[link](https://github.com/cdiazbas/neural_wfa)**|
|**2024-09-04**|**MDNF: Multi-Diffusion-Nets for Neural Fields on Meshes**|我们提出了一种在三角形网格上表示神经场的新框架，该框架在空间和频率域上都是多分辨率的。受神经傅里叶滤波器组（NFFB）的启发，我们的架构通过将更精细的空间分辨率级别与更高的频带相关联来分解空间和频率域，而将更粗糙的分辨率映射到较低的频率。为了实现几何感知的空间分解，我们利用了多个扩散网络组件，每个组件都与不同的空间分辨率级别相关联。随后，我们应用傅里叶特征映射来鼓励更精细的分辨率水平与更高的频率相关联。最终信号是使用正弦激活的MLP以小波激励的方式组成的，将高频信号聚集在低频信号之上。我们的架构在学习复杂神经场方面具有很高的精度，并且对目标场的不连续性、指数尺度变化和网格修改具有鲁棒性。我们通过将我们的方法应用于不同的神经领域，如合成RGB函数、UV纹理坐标和顶点法线，展示了其有效性，并说明了不同的挑战。为了验证我们的方法，我们将其性能与两种替代方案进行了比较，展示了我们的多分辨率架构的优势。 et.al.|[2409.03034](http://arxiv.org/abs/2409.03034)|null|
|**2024-09-03**|**GraspSplats: Efficient Manipulation with 3D Feature Splatting**|机器人对物体部件进行高效和零样本抓取的能力对于实际应用至关重要，并且随着视觉语言模型（VLM）的最新进展而变得普遍。为了弥合二维到三维表示的差距以支持这种能力，现有的方法依赖于神经场（NeRF），通过可微渲染或基于点的投影方法。然而，我们证明了NeRF由于其隐含性而不适合场景变化，并且基于点的方法对于没有基于渲染的优化的零件定位是不准确的。为了修正这些问题，我们提出了“把握辉煌”。使用深度监督和一种新的参考特征计算方法，GraspSplats在60秒内生成高质量的场景表示。我们进一步验证了基于高斯表示法的优势，表明GraspSplats中的显式和优化几何足以原生支持（1）实时抓取采样和（2）使用点跟踪器进行动态和铰接对象操作。通过在Franka机器人上进行的广泛实验，我们证明了在不同的任务设置下，GraspSplats的表现明显优于现有的方法。特别是，GraspSplats的性能优于基于NeRF的方法，如F3RM和LERF-TOGO，以及2D检测方法。 et.al.|[2409.02084](http://arxiv.org/abs/2409.02084)|null|
|**2024-08-23**|**S4D: Streaming 4D Real-World Reconstruction with Gaussians and 3D Control Points**|最近，使用高斯分布的动态场景重建引起了越来越多的兴趣。主流方法通常采用全局变形场来扭曲规范空间中的3D场景。然而，隐式神经场固有的低频特性往往导致复杂运动的无效表示。此外，它们的结构刚性会阻碍对不同分辨率和持续时间的场景的适应。为了克服这些挑战，我们引入了一种利用离散3D控制点的新方法。该方法对局部射线进行物理建模，并建立一个运动解耦坐标系，该坐标系有效地将传统图形与可学习的流水线相结合，以实现鲁棒且高效的局部6自由度（6-DoF）运动表示。此外，我们还开发了一个广义框架，将我们的控制点与高斯算子结合起来。从初始3D重建开始，我们的工作流程将流式4D真实世界重建分解为四个独立的子模块：3D分割、3D控制点生成、对象运动操纵和残差补偿。我们的实验表明，该方法在Neu3DV和CMU全景数据集上的表现优于现有的最先进的4D高斯散斑技术。我们的方法还显著加速了训练，在单个NVIDIA 4070 GPU上，每帧只需2秒即可优化我们的3D控制点。 et.al.|[2408.13036](http://arxiv.org/abs/2408.13036)|**[link](https://github.com/hebing-sjtu/S4D)**|

<p align=right>(<a href=#updated-on-20240926>back to top</a>)</p>

[contributors-shield]: https://img.shields.io/github/contributors/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[contributors-url]: https://github.com/Vincentqyw/cv-arxiv-daily/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[forks-url]: https://github.com/Vincentqyw/cv-arxiv-daily/network/members
[stars-shield]: https://img.shields.io/github/stars/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[stars-url]: https://github.com/Vincentqyw/cv-arxiv-daily/stargazers
[issues-shield]: https://img.shields.io/github/issues/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[issues-url]: https://github.com/Vincentqyw/cv-arxiv-daily/issues

