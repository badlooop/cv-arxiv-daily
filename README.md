[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]

## Updated on 2024.07.15
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
|**2024-07-12**|**Radiance Fields from Photons**|神经辐射场（NeRF）已成为从多个视点捕获的图像集合中进行高质量视图合成的事实上的方法。然而，在具有挑战性的条件下在野外拍摄图像时，仍然存在许多问题，例如低光照、高动态范围或快速运动导致模糊重建，并产生明显的伪影。在这项工作中，我们引入了量子辐射场，这是一类新的神经辐射场，使用单光子相机（SPC）以单个光子的粒度进行训练。我们开发了理论和实用的计算技术，用于构建辐射场，并从SPC捕获的非常规、随机和高速二进制帧序列中估计密集的相机姿态。我们通过仿真和SPC硬件原型演示了在高速运动、低光照和极端动态范围设置下的高保真重建。 et.al.|[2407.09386](http://arxiv.org/abs/2407.09386)|null|
|**2024-07-12**|**Learning High-Frequency Functions Made Easy with Sinusoidal Positional Encoding**|基于傅里叶特征的位置编码（PE）通常用于机器学习任务，这些任务涉及从低维输入中学习高频特征，如3D视图合成和具有神经切线核的时间序列回归。尽管它们很有效，但现有的PE需要手动、经验性地调整关键的超参数，特别是傅里叶特征，以适应每项独特的任务。此外，PE在高效学习高频函数方面面临挑战，特别是在数据有限的任务中。本文介绍了正弦PE（SPE），旨在有效地学习与真实底层函数紧密对齐的自适应频率特征。我们的实验表明，SPE在不进行超参数调整的情况下，在各种任务中（包括3D视图合成、文本到语音生成和1D回归）始终实现了增强的保真度和更快的训练。SPE的实施是为了直接替代现有的PE。其即插即用的特性使许多任务能够轻松采用SPE并从中受益。 et.al.|[2407.09370](http://arxiv.org/abs/2407.09370)|null|
|**2024-07-11**|**WayveScenes101: A Dataset and Benchmark for Novel View Synthesis in Autonomous Driving**|我们介绍了WayveScenes101，这是一个数据集，旨在帮助社区推进新颖视图合成的最新技术，该数据集侧重于挑战包含许多动态和可变形元素的驾驶场景，这些元素具有不断变化的几何形状和纹理。该数据集包括101个驾驶场景，涵盖了广泛的环境条件和驾驶场景。该数据集旨在对野外驾驶场景中的重建进行基准测试，场景重建方法存在许多固有挑战，包括图像眩光、快速曝光变化和具有显著遮挡的高度动态场景。除了原始图像，我们还包括标准数据格式的COLMAP导出的相机姿态。我们提出了一种评估协议，用于评估与训练视图离轴的手持相机视图上的模型，特别是测试方法的泛化能力。最后，我们为所有场景提供详细的元数据，包括天气、时间和交通状况，以便对场景特征进行详细的模型性能细分。数据集和代码可在https://github.com/wayveai/wayve_scenes. et.al.|[2407.08280](http://arxiv.org/abs/2407.08280)|**[link](https://github.com/wayveai/wayve_scenes)**|
|**2024-07-11**|**GAURA: Generalizable Approach for Unified Restoration and Rendering of Arbitrary Views**|神经渲染方法可以从姿态输入图像中实现场景的接近真实感的图像合成。然而，当图像不完美时，例如在非常低的光照条件下捕获的图像，最先进的方法无法重建高质量的3D场景。最近的方法试图通过在图像形成模型中建模各种退化过程来解决这一局限性；然而，这将它们限制在特定的图像退化上。在本文中，我们提出了一种可推广的神经渲染方法，可以在多种退化情况下进行高保真的新颖视图合成。我们的方法GAURA是基于学习的，不需要任何特定于测试时间场景的优化。它在包括几种降解类型的合成数据集上进行训练。GAURA在低光增强、去噪、去噪和运动去模糊的几个基准测试中表现优于最先进的方法。此外，我们的模型可以使用最少的数据有效地微调到任何新的传入退化。因此，我们展示了两种看不见的退化的适应结果，即去锯齿和去除散焦模糊。代码和视频结果可在vinayak-vg.ithub.io/GAURA上获得。 et.al.|[2407.08221](http://arxiv.org/abs/2407.08221)|null|
|**2024-07-10**|**Geospecific View Generation -- Geometry-Context Aware High-resolution Ground View Inference from Satellite Views**|由于卫星图像和地面图像之间存在显著的视图差距，因此在城市场景中从卫星图像预测逼真的地面视图是一项具有挑战性的任务。我们提出了一种新的管道来应对这一挑战，通过生成地理特定的视图，最大限度地尊重多视图卫星图像中的弱几何和纹理。与现有的从头顶卫星图像的部分语义或几何形状等线索中产生幻觉图像的方法不同，我们的方法通过使用卫星图像中的一组综合信息直接预测地理位置的地面视图图像，从而得到分辨率提高了十倍或更多的地面图像。我们利用一种新的建筑细化方法来减少地面卫星数据中的几何失真，这确保了使用扩散网络为视图合成创造准确的条件。此外，我们提出了一种新的地理特异性先验，它促使扩散模型的分布学习，以尊重更接近预测图像地理位置的图像样本。我们证明，我们的管道是第一个仅基于卫星图像生成接近真实和特定于地球的地面视图的管道。 et.al.|[2407.08061](http://arxiv.org/abs/2407.08061)|null|
|**2024-07-10**|**Generative Image as Action Models**|图像生成扩散模型已经过微调，以解锁图像编辑和新颖的视图合成等新功能。我们能否同样解锁用于视觉运动控制的图像生成模型？我们介绍了GENIMA，这是一种行为克隆代理，可以微调稳定扩散，在RGB图像上“绘制联合动作”作为目标。这些图像被输入控制器，该控制器将视觉目标映射到一系列关节位置。我们在25个RLBench和9个真实操作任务上研究了GENIMA。我们发现，通过将动作提升到图像空间，互联网预训练的扩散模型可以生成优于最先进的视觉运动方法的策略，特别是在对场景扰动的鲁棒性和对新对象的泛化方面。我们的方法也与3D代理竞争，尽管缺乏深度、关键点或运动规划等先验知识。 et.al.|[2407.07875](http://arxiv.org/abs/2407.07875)|**[link](https://github.com/MohitShridhar/genima)**|
|**2024-07-10**|**Controlling Space and Time with Diffusion Models**|我们提出了4DiM，这是一种用于4D新颖视图合成（NVS）的级联扩散模型，以一般场景的一个或多个图像以及一组相机姿态和时间戳为条件。为了克服由于4D训练数据可用性有限而带来的挑战，我们提倡对3D（有相机姿势）、4D（姿势+时间）和视频（时间但没有姿势）数据进行联合训练，并提出了一种新的架构来实现这一点。我们进一步主张使用单目度量深度估计器对SfM姿态数据进行校准，以实现度量尺度相机控制。对于模型评估，我们引入了新的度量来丰富和克服当前评估方案的缺点，与现有的3D NVS扩散模型相比，在保真度和姿态控制方面展示了最先进的结果，同时增加了处理时间动态的能力。4DiM还用于改进全景拼接、姿势调节的视频到视频翻译以及其他一些任务。有关概述，请参阅https://4d-diffusion.github.io et.al.|[2407.07860](http://arxiv.org/abs/2407.07860)|null|
|**2024-07-09**|**Reference-based Controllable Scene Stylization with Gaussian Splatting**|基于内容对齐的参考图像编辑外观的基于参考的场景样式化是一个新兴的研究领域。从预训练的神经辐射场（NeRF）开始，现有的方法通常会学习与给定风格相匹配的新颖外观。尽管它们很有效，但它们固有地存在耗时的体绘制问题，因此对于许多实时应用程序来说是不切实际的。在这项工作中，我们提出了ReGS，它将3D高斯散点（3DGS）应用于基于参考的风格化，以实现实时风格化的视图合成。编辑预训练3DGS的外观具有挑战性，因为它使用离散高斯作为3D表示，将外观与几何体紧密结合。像现有方法那样简单地优化外观通常不足以在给定的参考图像中对连续纹理进行建模。为了应对这一挑战，我们提出了一种新的纹理引导控制机制，该机制自适应地将局部负责的高斯分布调整为新的几何排列，以获得所需的纹理细节。所提出的过程以纹理线索为指导，进行有效的外观编辑，并根据场景深度进行正则化，以保持原始几何结构。通过这些新颖的设计，我们证明ReG可以产生最先进的风格化结果，这些结果尊重参考纹理，同时为自由视图导航提供实时渲染速度。 et.al.|[2407.07220](http://arxiv.org/abs/2407.07220)|null|
|**2024-07-08**|**RRM: Relightable assets using Radiance guided Material extraction**|在过去几年中，在任意光照下合成NeRF已成为一个具有开创性的问题。最近的努力通过提取基于物理的参数来解决这个问题，这些参数可以在任意光照下渲染，但它们在可以处理的场景范围内是有限的，通常是对光滑场景的处理不当。我们提出了RRM，这是一种即使在存在高反射物体的情况下也可以提取场景的材质、几何形状和环境照明的方法。我们的方法包括一个基于物理参数的物理感知辐射场表示，以及一个基于拉普拉斯金字塔的富有表现力的环境光结构。我们证明，我们的贡献在参数检索任务上优于最先进的技术，从而在表面场景上实现了高保真的重新照明和新颖的视图合成。 et.al.|[2407.06397](http://arxiv.org/abs/2407.06397)|null|
|**2024-07-08**|**PanDORA: Casual HDR Radiance Acquisition for Indoor Scenes**|大多数新颖的视图合成方法，如NeRF，都无法捕捉场景的真实高动态范围（HDR）辐射，因为它们通常是在用标准低动态范围（LDR）相机捕获的照片上训练的。虽然以不同曝光捕获多幅图像的传统曝光包围方法最近已被应用于多视图情况，但我们发现这些方法无法捕获室内场景的全部动态范围，其中包括非常明亮的光源。本文介绍了PanDORA：一种全景双观察者辐射采集系统，用于在高动态范围内随意捕捉室内场景。我们提出的系统包括两个固定在便携式三脚架上的360度相机。摄像机同时采集两个360度视频：一个以常规曝光，另一个以非常快的曝光，使用户可以在几分钟内随意地在场景中挥动设备。生成的图像被馈送到基于NeRF的算法，该算法重建场景的完整高动态范围。与之前工作的HDR基线相比，我们的方法在不牺牲视觉质量的情况下重建了室内场景的完整HDR辐射，同时保留了最近类似NeRF的方法的易捕获性。 et.al.|[2407.06150](http://arxiv.org/abs/2407.06150)|null|

<p align=right>(<a href=#updated-on-20240715>back to top</a>)</p>

## 3D Reconstruction

|Publish Date|Title|Abstract|PDF|Code|
|---|---|---|---|---|
|**2024-07-12**|**MetaFood CVPR 2024 Challenge on Physically Informed 3D Food Reconstruction: Methods and Results**|人们对计算机视觉在营养和饮食监测方面的应用越来越感兴趣，这导致了食品高级3D重建技术的发展。然而，高质量数据的稀缺以及工业界和学术界之间的有限合作限制了这一领域的进展。基于3D重建的最新进展，我们举办了MetaFood研讨会及其对物理知情3D食品重建的挑战。这项挑战的重点是使用可见的棋盘作为尺寸参考，从2D图像重建食品的体积精确3D模型。参与者的任务是为20种不同难度的选定食物重建3D模型：简单、中等和困难。简单级别提供200张图像，中等级别提供30张图像，硬级别仅提供1张图像用于重建。总共有16个团队在最终测试阶段提交了结果。本次挑战中开发的解决方案在3D食品重建方面取得了有希望的结果，在改善饮食评估和营养监测的份量估计方面具有巨大的潜力。有关本次研讨会挑战和数据集访问的更多详细信息，请访问https://sites.google.com/view/cvpr-metafood-2024. et.al.|[2407.09285](http://arxiv.org/abs/2407.09285)|null|
|**2024-07-12**|**URRL-IMVC: Unified and Robust Representation Learning for Incomplete Multi-View Clustering**|不完全多视图聚类（IMVC）旨在对仅部分可用的多视图数据进行聚类。这带来了两个主要挑战：有效利用多视图信息和减轻缺失视图的影响。主流的解决方案采用跨视图对比学习和缺失视图恢复技术。然而，他们要么只关注观点之间的共识而忽视了有价值的补充信息，要么由于缺乏监督而提供不可靠的恢复观点。为了解决这些局限性，我们提出了一种新的不完全多视图聚类的统一鲁棒表示学习（URRL-IMVC）。URRL-IMVC通过整合来自多个视图和相邻样本的信息，直接学习一个统一的嵌入，该嵌入对查看缺失条件具有鲁棒性。首先，为了克服跨视图对比学习的局限性，URRL-IMVC采用了一种基于注意力的自动编码器框架来融合多视图信息并生成统一的嵌入。其次，URRL-IMVC通过KNN插补和数据增强技术直接增强了统一嵌入对视图缺失条件的鲁棒性，消除了显式缺失视图恢复的需要。最后，引入了增量改进以进一步提高整体性能，例如聚类模块和编码器的定制。我们在各种基准数据集上广泛评估了所提出的URRL-IMVC框架，展示了其最先进的性能。此外，还进行了全面的消融研究，以验证我们设计的有效性。 et.al.|[2407.09120](http://arxiv.org/abs/2407.09120)|null|
|**2024-07-11**|**Determination of five-parameter grain boundary characteristics in nanocrystalline Ni-W by Scanning Precession Electron Diffraction Tomography**|通过实验确定完整的五参数晶界特征对于理解晶界对材料性能的影响、改进相关模型和设计先进合金至关重要。然而，由于其3D特性，实现这一目标通常具有挑战性，特别是在纳米级。在我们的研究中，我们使用扫描进动电子衍射（SPED）断层扫描成功地确定了含有孪晶的退火镍钨合金（NiW）纳米晶针状试样（尖端）的晶界特性。这种面心立方（fcc）材料中退火孪晶的存在导致SPED衍射图案中的共同反射，这对3D晶粒形状断层重建所需的特定取向虚拟暗场（VDF）图像的重建提出了挑战。为了解决这个问题，在重建VDF图像之前，自动后处理步骤会识别和取消选择这些共享反射。结合适当的强度归一化和投影对齐程序，这种方法能够对针状样品体积中包含的单个颗粒进行高保真3D重建。为了探测所得边界特征的准确性，使用3D霍夫变换从3D体素化晶界图中提取了双边界表面法线方向。对于相干Sigma 3边界的子集，对于小于400 nm的边界尺寸，获得了预期的{111}晶界平面法线，角度误差小于3{\textdegree}。这项工作提高了我们精确表征和理解控制材料性能的复杂晶界的能力。 et.al.|[2407.08251](http://arxiv.org/abs/2407.08251)|null|
|**2024-07-11**|**Bayesian uncertainty analysis for underwater 3D reconstruction with neural radiance fields**|神经辐射场（NeRF）是一种深度学习技术，可以使用来自不同观察方向和相机姿态的稀疏2D图像生成3D场景的新视图。SeaThru NeRF是传统NeRF在水下环境中的扩展，光可以被水吸收和散射，它被提出将水下场景的干净外观和几何结构与散射介质的影响分开。由于水下场景的外观和结构质量对于水下基础设施检查等下游任务至关重要，因此应考虑和评估3D重建模型的可靠性。然而，由于缺乏量化自然环境照明下水下场景3D重建中的不确定性的能力，NeRF在无人自主水下导航中的实际部署受到限制。为了解决这个问题，我们在SeaThru NeRF中引入了一个基于贝叶斯射线的空间扰动场D_omega，并进行拉普拉斯近似以获得参数omega的高斯分布N（0，Sigma），其中Sigma的对角元素对应于每个空间位置的不确定性。我们还采用了一种简单的阈值方法来去除水下场景渲染结果中的伪影。数值实验证明了该方法的有效性。 et.al.|[2407.08154](http://arxiv.org/abs/2407.08154)|null|
|**2024-07-11**|**Survey on Fundamental Deep Learning 3D Reconstruction Techniques**|这项调查旨在研究基于基础深度学习（DL）的3D重建技术，这些技术可以生成逼真的3D模型和场景，突出神经辐射场（NeRF）、潜在扩散模型（LDM）和3D高斯散斑。我们剖析了底层算法，评估了它们的优势和权衡，并在这个快速发展的领域预测了未来的研究轨迹。我们全面概述了DL驱动的3D场景重建的基本原理，深入了解了它们的潜在应用和局限性。 et.al.|[2407.08137](http://arxiv.org/abs/2407.08137)|null|
|**2024-07-10**|**RoCap: A Robotic Data Collection Pipeline for the Pose Estimation of Appearance-Changing Objects**|当用户操纵有形物体作为控制器时，物体姿态估计在混合现实交互中起着至关重要的作用。传统的基于视觉的物体姿态估计方法利用3D重建来合成训练数据。然而，这些方法是为具有漫反射颜色的静态对象设计的，对于在操作过程中改变外观的对象效果不佳，例如毛绒玩具等可变形对象、化学烧瓶等透明对象、金属水罐等反射对象和剪刀等铰接对象。为了解决这一局限性，我们提出了Rocap，这是一种机器人管道，可以模拟人类对目标对象的操纵，同时生成标记有地面真实姿态信息的数据。用户首先将目标对象交给机器人手臂，系统以各种6D配置捕获对象的许多图片。该系统通过使用捕获的图像及其根据机器人手臂的关节角度自动计算的地面真实姿态信息来训练模型。我们通过使用收集的数据训练简单的深度学习模型，并将结果与基于3D重建的合成数据训练的模型进行比较，通过定量和定性评估，展示了外观变化物体的姿态估计。这些发现突显了Rocap的潜力。 et.al.|[2407.08081](http://arxiv.org/abs/2407.08081)|null|
|**2024-07-10**|**Chat-Edit-3D: Interactive 3D Scene Editing via Text Prompts**|最近基于视觉语言预训练模型的图像内容操纵工作已有效地扩展到文本驱动的3D场景编辑。然而，现有的3D场景编辑方案仍然存在某些缺点，阻碍了它们的进一步交互设计。这种方案通常遵循固定的输入模式，限制了用户在文本输入方面的灵活性。此外，它们的编辑能力受到单个或几个2D视觉模型的限制，需要复杂的管道设计将这些模型集成到3D重建过程中。为了解决上述问题，我们提出了一种基于对话的3D场景编辑方法，称为CE3D，它以一个大型语言模型为中心，允许用户任意输入文本并解释他们的意图，从而促进相应视觉专家模型的自主调用。此外，我们设计了一种利用哈希图集来表示3D场景视图的方案，该方案将3D场景的编辑转移到2D图集图像上。该设计实现了2D编辑和3D重建过程之间的完全解耦，使CE3D能够灵活地集成各种现有的2D或3D视觉模型，而不需要复杂的融合设计。实验结果表明，CE3D有效地整合了多种视觉模型，实现了多样化的编辑视觉效果，具有很强的场景理解能力和多轮对话能力。该代码可在以下网址获得https://sk-fun.fun/CE3D. et.al.|[2407.06842](http://arxiv.org/abs/2407.06842)|null|
|**2024-07-09**|**Computer vision tasks for intelligent aerospace missions: An overview**|计算机视觉任务对于航空航天任务至关重要，因为它们帮助航天器理解和解释空间环境，例如估计位置和方向、重建3D模型和识别物体，这些任务已被广泛研究以成功执行任务。然而，卡尔曼滤波、运动结构和多视图立体等传统方法不足以处理恶劣条件，导致结果不可靠。近年来，基于深度学习（DL）的感知技术显示出巨大的潜力，并优于传统方法，特别是在对不断变化的环境的鲁棒性方面。为了进一步推进基于DL的航空航天感知，已经提出了各种框架、数据集和策略，表明未来应用的巨大潜力。在这项调查中，我们旨在探索感知任务中使用的有前景的技术，并强调基于DL的航空航天感知的重要性。我们首先概述了航空航天感知，包括近年来开发的经典空间项目、常用传感器和传统感知方法。随后，我们深入研究了航空航天任务中的三个基本感知任务：姿态估计、3D重建和识别，因为它们对后续的决策和控制至关重要。最后，我们讨论了当前研究的局限性和可能性，并对未来的发展进行了展望，包括使用有限数据集的挑战、改进算法的必要性以及多源信息融合的潜在好处。 et.al.|[2407.06513](http://arxiv.org/abs/2407.06513)|null|
|**2024-07-09**|**LuSNAR:A Lunar Segmentation, Navigation and Reconstruction Dataset based on Muti-sensor for Autonomous Exploration**|随着月球探测任务的复杂性，月球需要更高的自主性。环境感知和导航算法是月球车实现自主探索的基础。算法的开发和验证需要高度可靠的数据支持。现有的月球数据集大多针对单一任务，缺乏多样化的场景和高精度的地面实况标签。为了解决这个问题，我们提出了一个多任务、多场景和多标签的月球基准数据集LuSNAR。该数据集可用于全面评估自主感知和导航系统，包括高分辨率立体图像对、全景语义标签、密集深度图、激光雷达点云和漫游车的位置。为了提供更丰富的场景数据，我们基于虚幻引擎构建了9个月球模拟场景。每个场景根据地形起伏和物体密度进行划分。为了验证数据集的可用性，我们评估和分析了语义分割、3D重建和自主导航的算法。实验结果证明，本文提出的数据集可用于自主环境感知和导航等任务的地面验证，并为测试算法度量的可访问性提供了月球基准数据集。我们在以下网址公开提供LuSNAR：https://github.com/autumn999999/LuSNAR-dataset. et.al.|[2407.06512](http://arxiv.org/abs/2407.06512)|**[link](https://github.com/autumn999999/lusnar-dataset)**|
|**2024-07-08**|**Tailor3D: Customized 3D Assets Editing and Generation with Dual-Side Images**|3D AIGC的最新进展表明，它有望直接从文本和图像创建3D对象，从而在动画和产品设计方面节省大量成本。然而，3D资源的详细编辑和定制仍然是一个长期存在的挑战。具体来说，3D生成方法缺乏像2D图像创建方法那样精确地遵循精细详细指令的能力。想象一下，你可以通过3D AIGC获得一个玩具，但带有不需要的配件和服装。为了应对这一挑战，我们提出了一种名为Tailor3D的新型管道，它可以从可编辑的双面图像中快速创建定制的3D资产。我们的目标是模仿裁缝在局部更改对象或执行整体风格转换的能力。与从多个视图创建3D资源不同，使用双面图像消除了编辑单个视图时发生的重叠区域冲突。具体来说，它首先编辑前视图，然后通过多视图扩散生成对象的后视图。之后，它继续编辑后视图。最后，提出了一种双面LRM，将正面和背面的3D特征无缝缝合在一起，类似于裁缝将衣服的正面和背面缝合在一起。双面LRM纠正了前后视图之间不完美的一致性，增强了编辑能力，减轻了内存负担，同时将它们与LoRA Triple Plane Transformer无缝集成到统一的3D表示中。实验结果证明了Tailor3D在各种3D生成和编辑任务中的有效性，包括3D生成填充和样式转换。它为编辑3D资源提供了一种用户友好、高效的解决方案，每个编辑步骤只需几秒钟即可完成。 et.al.|[2407.06191](http://arxiv.org/abs/2407.06191)|null|

<p align=right>(<a href=#updated-on-20240715>back to top</a>)</p>

## Diffusion

|Publish Date|Title|Abstract|PDF|Code|
|---|---|---|---|---|
|**2024-07-12**|**A Primitive Model for Predicting Membrane Currents in Excitable Cells Based Only on Ion Diffusion Coefficients**|霍奇金和赫胥黎最初提出的预测轴突等可兴奋细胞电流的经典模型依赖于经验电压门控参数，这些参数量化了钠和钾离子通道中的离子转运。我们提出了一种完全基于公认的离子扩散系数来预测这些电流的原始模型。由于中央钠通道的打开，可兴奋细胞内的变化仅限于半径由钠离子扩散系数决定的生长半球。钠通道在整个计算过程中是开放的，由于耦合的电扩散过程，它会自然地激活和去激活。电流脉冲的特征时间在皮安范围内，随着沟道密度从每平方微米10000个沟道降低到1个沟道，从10 $^{-5}$增加到10$^{1}$ s。在不调用任何门控参数的情况下，将模型预测与从巨型鱿鱼轴突获得的数据进行比较。 et.al.|[2407.09474](http://arxiv.org/abs/2407.09474)|null|
|**2024-07-12**|**Weak Chaos, Anomalous Diffusion, and Weak Ergodicity Breaking in Systems with Delay**|我们证明，如果非线性是从特定类别的函数中选择的，则具有线性瞬时和延迟非线性项的标准延迟系统表现出弱混沌、渐近次扩散行为和弱遍历性破缺。在大的恒定延迟时间的限制下，由于交叉时间呈指数级增长，可能无法观察到异常行为。延迟的周期性调制导致混沌相位的有效维数大大降低，导致迄今为止未知的解类型，并在短时间内发生异常扩散。观测到的异常行为是由函数空间中的非双曲不动点引起的。 et.al.|[2407.09449](http://arxiv.org/abs/2407.09449)|null|
|**2024-07-12**|**Intensive broadband reverberation mapping of Fairall 9 with 1.8 years of daily Swift monitoring**|我们展示了1.8年来Swift对明亮、强变的1型AGN Fairall 9的近乎每日监测。共有575次成功访问，这是迄今为止报告的最大规模的此类活动。紫外/光学范围内的变化具有很好的相关性，在薄盘/灯柱模型预测的方向上，较长波长滞后于较短波长。通过去趋势化改善了相关性；减去UV/光学光曲线的二阶多项式拟合，以消除本研究不感兴趣的长期趋势。广泛的测试表明，使用高阶多项式去趋势可以消除混响时间尺度上过多的内在变异信号。这些数据提供了迄今为止对紫外波段内带间滞后的最清晰检测，表明无论是大圆盘的发射还是宽线区域的漫射连续发射都不能独立解释完整的观测滞后光谱。观察到的X射线通量变化与紫外/光学中的变化相关性较差。此外，将数据细分为四条~160天的光照曲线表明，UV/光学滞后光谱在整个四个周期内高度稳定，但X射线到UV的滞后是不稳定的，从一个周期到下一个周期，幅度甚至方向都发生了显著变化。这表明X射线与紫外线的关系比AGN通常采用的简单再处理模型预测的更复杂。碗模型（灯柱照射和黑体在边缘陡峭的圆盘上的再处理）拟合表明，圆盘在与BLR内边缘一致的距离（~10 lt day）和温度（~8000K）处变厚。 et.al.|[2407.09445](http://arxiv.org/abs/2407.09445)|null|
|**2024-07-12**|**Efficient energy-stable parametric finite element methods for surface diffusion flow and applications in solid-state dewetting**|目前，用于表面扩散流和其他流动的能量稳定参数有限元方法通常仅限于时间上的一阶精度。为几何流设计一种高阶算法，该算法在理论上也可以被证明是能量稳定的，这是一个重大的挑战。受新标量辅助变量方法[F.Huang，J.Shen，Z.Yang，SIAM J.SCI.Comput.，42（2020），pp.A2514-A2536]的启发，我们提出了各向同性/各向异性表面扩散流的新型能量稳定参数有限元近似，在时间上实现了一阶和二阶精度。此外，我们应用这些算法来模拟薄膜的固态脱湿。最后，大量的数值实验验证了我们开发的数值方法的准确性、能量稳定性和效率。这项工作中设计的算法表现出很强的通用性，因为它们可以很容易地扩展到其他高阶时间离散化方法（例如BDFk方案）。同时，这些算法实现了显著的计算效率，并保持了出色的网格质量。更重要的是，该算法可以在理论上证明具有无条件的能量稳定性，能量几乎等于原始能量。 et.al.|[2407.09418](http://arxiv.org/abs/2407.09418)|null|
|**2024-07-12**|**A Numerical Study of WENO Approximations to Sharp Propagating Fronts for Reaction-Diffusion Systems**|各种应用中的许多反应扩散系统都表现出在多个时空尺度上演化的行波解。这些行波解对于理解系统的潜在动力学至关重要。在这项工作中，我们提出了有限差分框架内的六阶加权基本无振荡（WENO）方法来求解反应扩散系统。与经典有限差分方法相比，WENO方法允许我们使用更少的网格点和更大的时间步长。我们的重点是求解具有尖锐前沿的行波解的反应扩散系统。虽然WENO方法在双曲守恒律中很受欢迎，特别是对于具有不连续性的问题，但它可以适用于抛物型方程，如反应扩散系统，以有效地处理尖锐的波前。因此，我们采用了专门为抛物型方程开发的WENO方法。我们考虑了各种反应扩散方程，包括Fisher、Zeldovich、Newell Whitehead Segel、双稳态方程和Lotka-Volterra竞争扩散系统，所有这些方程都产生了具有尖锐波阵面的行波解。本文中的数值例子表明，中心WENO方法比常用的有限差分方法更准确、更高效。我们还对Newell-Whitehead-Segel方程中尖锐传播锋的数值速度进行了分析。总体结果证实，中心WENO方法是高效的，建议用于求解具有尖锐波前的反应扩散方程。 et.al.|[2407.09393](http://arxiv.org/abs/2407.09393)|null|
|**2024-07-12**|**Grain boundaries control lithiation of solid solution substrates in lithium metal batteries**|可持续交通和通信系统的发展需要提高锂电池的能量密度和容量保持率。使用与体心立方锂形成固溶体的基板可以提高无阳极电池的循环稳定性。然而，目前尚不清楚基底微观结构如何影响锂化行为。在这里，我们通过离子和电子显微镜的结合，部署了一种相关的近原子尺度探测方法，以研究Li在Li-Ag扩散偶中的分布作为模型系统。我们发现，超过93.8at.%的Li区域在Ag内以随机的高角度晶界成核，而晶粒内部没有锂化。我们从微观结构中证明了动力学和力学约束在决定锂化过程中的作用，而不是平衡热力学。研究结果表明，晶粒尺寸和晶界特征对于提高中间层/电极的电化学性能至关重要，特别是对于改善锂化动力学，从而减少枝晶形成。 et.al.|[2407.09374](http://arxiv.org/abs/2407.09374)|null|
|**2024-07-12**|**Any-Property-Conditional Molecule Generation with Self-Criticism using Spanning Trees**|生成新分子具有挑战性，大多数表示都会导致生成模型产生许多无效分子。基于生成树的图生成（STGG）是一种有前景的方法，可以确保生成有效的分子，在无条件生成方面优于最先进的SMILES和图扩散模型。在现实世界中，我们希望能够根据一个或多个所需的特性而不是无条件地生成分子。因此，在这项工作中，我们将STGG扩展到多属性条件生成。我们的方法STGG+结合了现代Transformer架构、训练期间对属性的随机掩蔽（允许对属性的任何子集进行调节和无分类器引导）、辅助属性预测损失（允许模型自我批评分子并选择最佳分子）和其他改进。我们证明，STGG+在分布内和分布外条件生成以及奖励最大化方面取得了最先进的性能。 et.al.|[2407.09357](http://arxiv.org/abs/2407.09357)|null|
|**2024-07-12**|**Thermodynamics of Giant Molecular Clouds: The Effects of Dust Grain Size**|尘埃粒度分布（GSD）可能在宇宙中不同的恒星形成环境中存在显著差异，但这种变化对恒星形成的总体影响尚不清楚。这种模糊性是因为GSD与加热/冷却、辐射和化学等过程非线性相互作用而产生的，这些过程具有竞争效应和不同的环境依赖性。在这项研究中，我们研究了GSD变化对巨分子云（GMC）热化学和演化的影响。为了实现这一目标，我们进行了跨越一系列云质量和粒度的辐射尘埃磁流体动力学模拟，这些模拟明确地将尘埃颗粒的动力学纳入了STARFORGE项目的完整物理框架。我们发现粒径的差异显著改变了GMCs的热化学。具体而言，我们表明，在固定的粉尘质量和粉尘与气体比条件下，较大的颗粒会导致较低的粉尘不透明度。这种降低的不透明度允许ISRF光子更深入地穿透，并允许内部辐射场光子更广泛地渗透到云层中，从而导致气体快速加热和恒星形成的抑制。我们发现恒星形成效率对晶粒尺寸高度敏感，当晶粒尺寸从0.1美元增加到10美元时，效率会降低一个数量级。此外，我们注意到，较暖的气体抑制了低质量恒星的形成。此外，由于不透明度的降低，我们观察到更多的气体存在于扩散电离结构中。 et.al.|[2407.09343](http://arxiv.org/abs/2407.09343)|null|
|**2024-07-12**|**PID: Physics-Informed Diffusion Model for Infrared Image Generation**|红外成像技术因其在低能见度条件下的可靠传感能力而受到广泛关注，促使许多研究将丰富的RGB图像转换为红外图像。然而，大多数现有的图像翻译方法将红外图像视为一种风格变化，忽视了潜在的物理规律，这限制了它们的实际应用。为了解决这些问题，我们提出了一种物理信息扩散（PID）模型，用于将RGB图像转换为符合物理定律的红外图像。我们的方法利用了扩散模型的迭代优化，并在训练过程中基于红外定律的先验知识引入了强物理约束。该方法在不增加额外训练参数的情况下，增强了平移红外图像与真实红外域之间的相似性。实验结果表明，PID的性能明显优于现有的最先进的方法。我们的代码可在https://github.com/fangyuanmao/PID. et.al.|[2407.09299](http://arxiv.org/abs/2407.09299)|**[link](https://github.com/fangyuanmao/pid)**|
|**2024-07-12**|**SS-SfP:Neural Inverse Rendering for Self Supervised Shape from (Mixed) Polarization**|我们提出了一种新的基于逆渲染的框架，用于从单视图偏振图像中估计对象和场景的3D形状（每像素表面法线和深度），这个问题通常被称为偏振形状（SfP）。现有的基于物理和基于学习的SfP方法在某些限制下执行，即（a）纯漫反射或纯镜面反射，这在真实表面中很少见，（b）难以获取且受扫描仪分辨率限制的地面真值表面法线可用于直接监督，以及（c）已知的折射率。为了克服这些限制，我们首先学习基于改进的偏振反射模型分离部分偏振的漫反射和镜面反射分量，我们称之为反射线索，然后在偏振数据和估计的反射线索的指导下，通过基于逆渲染的自监督深度学习框架SS-SfP估计混合偏振下的形状。此外，我们还得到了折射率作为非线性最小二乘解。通过广泛的定量和定性评估，我们在完全自我监督的环境中，建立了所提出的框架对DeepSfP数据集中的简单单对象场景和SPW数据集中的复杂野外场景的有效性。据我们所知，这是第一种在完全自监督框架下解决混合极化下SfP问题的基于学习的方法。 et.al.|[2407.09294](http://arxiv.org/abs/2407.09294)|null|

<p align=right>(<a href=#updated-on-20240715>back to top</a>)</p>

## NeRF

|Publish Date|Title|Abstract|PDF|Code|
|---|---|---|---|---|
|**2024-07-10**|**Neural Localizer Fields for Continuous 3D Human Pose and Shape Estimation**|随着可用训练数据的爆炸性增长，单图像3D人体建模领先于向以数据为中心的范式过渡。成功利用数据规模的关键是设计灵活的模型，这些模型可以从不同研究人员或供应商生产的各种异构数据源进行监督。为此，我们提出了一种简单而强大的范式，用于无缝统一不同的人体姿势和形状相关的任务和数据集。我们的公式侧重于在训练和测试时查询人体体积的任意点并在3D中获得其估计位置的能力。我们通过学习身体点定位器函数的连续神经场来实现这一点，每个函数都是基于不同参数化的3D热图卷积点定位器（检测器）。为了生成参数输出，我们提出了一种高效的后处理步骤，用于将SMPL族身体模型拟合到非参数关节和顶点预测中。通过这种方法，我们可以自然地利用不同注释的数据源，包括网格、2D/3D骨架和密集姿势，而无需在它们之间进行转换，从而训练出大规模的3D人体网格和骨架估计模型，这些模型在3DPW、EMDB和SSP-3D等几个公共基准上的表现远远优于最先进的水平。 et.al.|[2407.07532](http://arxiv.org/abs/2407.07532)|null|
|**2024-07-03**|**Cerebral cortex inspired representation of neural field network**|进化及其智能元素在探索中带来了刺激和挑战。然而，物种如何拥有记忆、检索记忆并保持连续性是根本问题。大多数现象只能由研究人员假设，通过实验验证它们是一个很大的挑战。将大脑视为理想的智能机器并对其进行建模，为计算算法开辟了新的维度。本文提出了一个假设，即类似于大脑皮层的记忆创造。大脑皮层的区域隐含着特定功能的特异性，构成了一维的矢量形式的神经场。整个皮层的神经场相互连接形成了一个网络。这些网络与生存本能、情绪和奖励相关联，构成了对暴露环境的记忆，或者说学习。具有多维控制点的图形工具NURBS被隐式地用于将这些网络表示为一组三次方程。通过数据学习是智能系统的主要模块，本文试图将数据转换为低维模式，而不是实时智能系统的现有绝对形式。 et.al.|[2407.04741](http://arxiv.org/abs/2407.04741)|null|
|**2024-07-01**|**Fast and Efficient: Mask Neural Fields for 3D Scene Segmentation**|理解3D场景是计算机视觉研究中的一个关键挑战，其应用跨越多个领域。最近在将2D视觉语言基础模型提取到神经领域（如NeRF和3DGS）方面取得的进展，使3D场景能够从2D多视图图像中进行开放式词汇分割，而不需要精确的3D注释。然而，虽然有效，但高维CLIP特征的每像素蒸馏会引入模糊性，并需要复杂的正则化策略，从而在训练过程中增加效率。本文介绍了MaskField，它能够在弱监督下利用神经场实现快速高效的3D开放式分词。与以前的方法不同，MaskField提取掩模而不是密集的高维CLIP特征。MaskFields使用神经场作为二进制掩模生成器，并使用SAM生成的掩模对其进行监督，并通过粗略的CLIP特征进行分类。MaskField通过在训练过程中自然引入SAM分割的对象形状而无需额外的正则化来克服模糊的对象边界。通过在训练过程中避免直接处理高维CLIP特征，MaskField与3DGS等显式场景表示特别兼容。我们广泛的实验表明，MaskField不仅超越了现有的最先进的方法，而且实现了非常快的收敛速度，仅需5分钟的训练就超越了以前的方法。我们希望MaskField能够激发对如何训练神经场以从2D模型中理解3D场景的进一步探索。 et.al.|[2407.01220](http://arxiv.org/abs/2407.01220)|null|
|**2024-07-01**|**3D Feature Distillation with Object-Centric Priors**|将自然语言与物理世界联系起来是一个无处不在的话题，在计算机视觉和机器人技术中有着广泛的应用。最近，CLIP等二维视觉语言模型因其在二维图像中具有令人印象深刻的开放词汇基础能力而得到了广泛推广。最近的工作旨在通过特征提取将2D CLIP特征提升到3D，但要么学习特定于场景的神经场，因此缺乏泛化能力，要么专注于需要访问多个摄像头视图的室内房间扫描数据，这在机器人操作场景中是不可行的。此外，相关方法通常在像素级融合特征，并假设所有相机视图都具有相同的信息量。在这项工作中，我们表明这种方法在接地精度和分割清晰度方面都会导致次优的3D特征。为了缓解这一问题，我们提出了一种多视图特征融合策略，该策略采用以对象为中心的先验来消除基于语义信息的无信息视图，并通过实例分割掩码在对象级别融合特征。为了提取我们以对象为中心的3D特征，我们生成了一个大规模的合成多视图数据集，其中包含杂乱的桌面场景，从3300多个独特的对象实例中生成了15k个场景，我们将其公之于众。我们表明，我们的方法在从单视图RGB-D重建3D CLIP特征的同时，提高了接地容量和空间一致性，从而偏离了测试时多个相机视图的假设。最后，我们证明了我们的方法可以推广到新的桌面领域，并可以在不进行微调的情况下重新用于3D实例分割，并证明了它在混乱中的语言引导机器人抓取中的实用性 et.al.|[2406.18742](http://arxiv.org/abs/2406.18742)|null|
|**2024-06-25**|**Masked Generative Extractor for Synergistic Representation and 3D Generation of Point Clouds**|在二维图像生成建模和表示学习领域，掩模生成编码器（MAGE）已经证明了生成建模与表示学习之间的协同潜力。受此启发，我们提出Point MAGE将这一概念扩展到点云数据。具体来说，该框架首先利用矢量量化变分自编码器（VQVAE）重建3D形状的神经场表示，从而学习点补丁的离散语义特征。随后，通过将掩蔽模型与可变掩蔽比相结合，我们实现了生成和表示学习的同步训练。此外，我们的框架与现有的点云自监督学习（SSL）模型无缝集成，从而提高了它们的性能。我们广泛评估了Point MAGE的表示学习和生成能力。在形状分类任务中，Point MAGE在ModelNet40数据集上的准确率达到94.2%，在ScanObjectNN数据集上达到92.9%（+1.3%）。此外，它在少数镜头学习和零件分割任务中取得了最新的性能。实验结果还证实，Point MAGE可以在无条件和有条件的设置下生成详细和高质量的3D形状。 et.al.|[2406.17342](http://arxiv.org/abs/2406.17342)|null|
|**2024-06-17**|**DistillNeRF: Perceiving 3D Scenes from Single-Glance Images by Distilling Neural Fields and Foundation Model Features**|我们提出了DistillNeRF，这是一个自监督学习框架，解决了在自动驾驶中从有限的2D观察中理解3D环境的挑战。我们的方法是一种可推广的前馈模型，它从稀疏的单帧多视图相机输入中预测丰富的神经场景表示，并通过可微渲染进行自我监督训练，以重建RGB、深度或特征图像。我们的第一个见解是通过生成密集的深度和虚拟相机目标进行训练，利用每场景优化的神经辐射场（NeRF），从而帮助我们的模型从稀疏的非重叠图像输入中学习3D几何。其次，为了学习语义丰富的3D表示，我们建议从预先训练的2D基础模型（如CLIP或DINOv2）中提取特征，从而实现各种下游任务，而不需要昂贵的3D人工注释。为了利用这两个见解，我们引入了一种新的模型架构，该架构具有两级提升-飞溅-射击编码器和参数化的稀疏分层体素表示。NuScenes数据集的实验结果表明，DistillNeRF在场景重建、新颖视图合成和深度估计方面明显优于现有的可比自监督方法；并且它允许竞争性的零样本3D语义占用预测，以及通过提取的基础模型特征来理解开放世界场景。演示和代码将在https://distillnerf.github.io/. et.al.|[2406.12095](http://arxiv.org/abs/2406.12095)|null|
|**2024-06-18**|**Effective Rank Analysis and Regularization for Enhanced 3D Gaussian Splatting**|从多视图图像进行3D重建是计算机视觉和图形学中的基本挑战之一。最近，3D高斯散斑（3DGS）已经成为一种有前景的技术，能够实时渲染高质量的3D重建。该方法利用3D高斯表示和基于图块的飞溅技术，绕过了昂贵的神经场查询。尽管3DGS具有潜力，但由于高斯收敛为具有一个主要方差的各向异性高斯，它遇到了挑战，包括针状伪影、次优几何形状和不准确的法线。我们建议使用有效秩分析来检查3D高斯基元的形状统计，并识别高斯真的收敛到有效秩为1的针状形状。为了解决这个问题，我们引入了有效秩作为正则化，它约束了高斯的结构。我们的新正则化方法增强了法线和几何重建，同时减少了针状伪影。该方法可以作为附加模块集成到其他3DGS变体中，在不损害视觉保真度的情况下提高其质量。 et.al.|[2406.11672](http://arxiv.org/abs/2406.11672)|null|
|**2024-06-13**|**Well-posedness and regularity of solutions to neural field problems with dendritic processing**|我们研究了最近提出的神经场模型的解决方案，其中树突被建模为源自体细胞层的垂直纤维连续体。由于电压通过具有非局域源的电缆方程沿树突方向传播，该模型具有各向异性扩散算子和突触耦合的积分项。因此，相应的柯西问题与经典神经场方程明显不同。我们证明了该问题的弱公式具有唯一解，其嵌入估计类似于非线性局部反应扩散方程的嵌入估计。我们的分析依赖于扰动无扩散问题的弱解，即一个标准的神经场，迄今为止还没有研究过弱问题。我们找到了有和没有扩散问题的严格渐近估计，并证明了这两个模型的解在有限时间间隔内以适当的范数保持接近。我们提供了微扰结果的数值证据。 et.al.|[2406.09222](http://arxiv.org/abs/2406.09222)|null|
|**2024-06-13**|**Preserving Identity with Variational Score for General-purpose 3D Editing**|我们提出了Piva（用变分分数蒸馏保持身份），这是一种基于优化的新方法，用于编辑基于扩散模型的图像和3D模型。具体来说，我们的方法受到了最近提出的二维图像编辑方法——增量去噪分数（DDS）的启发。我们指出了DDS在2D和3D编辑中的局限性，这会导致细节损失和过饱和。为了解决这个问题，我们提出了一个额外的分数蒸馏术语来强制身份保留。这使得编辑过程更加稳定，逐步优化NeRF模型以匹配目标提示，同时保留关键的输入特性。我们证明了我们的方法在零样本图像和神经场编辑中的有效性。我们的方法成功地改变了视觉属性，添加了微妙和实质性的结构元素，转换了形状，并在标准的2D和3D编辑基准上取得了有竞争力的结果。此外，我们的方法没有施加掩蔽或预训练等约束，使其与各种预训练的扩散模型兼容。这允许进行多功能编辑，而不需要神经场到网格的转换，从而提供更用户友好的体验。 et.al.|[2406.08953](http://arxiv.org/abs/2406.08953)|null|
|**2024-06-12**|**Category-level Neural Field for Reconstruction of Partially Observed Objects in Indoor Environment**|神经隐式表示通过各种成功案例在3D重建中引起了人们的关注。对于场景理解或编辑等进一步的应用，一些作品已经显示出在对象组成重建方面的进展。尽管它们在观测区域表现出色，但在重建部分观测到的物体方面，它们的性能仍然有限。为了更好地处理这个问题，我们引入了类别级神经场，在场景中属于同一类别的对象之间学习有意义的共同3D信息。我们的核心思想是根据观察到的形状对对象进行子分类，以便更好地训练类别级模型。然后，我们利用神经场进行具有挑战性的任务，通过选择和对齐基于射线的不确定性选择的代表性对象来注册部分观察到的对象。在模拟和真实世界数据集上的实验表明，我们的方法改善了几个类别中未观察到的部分的重建。 et.al.|[2406.08176](http://arxiv.org/abs/2406.08176)|**[link](https://github.com/Taekbum/category-nerf-reconstruction-official)**|

<p align=right>(<a href=#updated-on-20240715>back to top</a>)</p>

[contributors-shield]: https://img.shields.io/github/contributors/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[contributors-url]: https://github.com/Vincentqyw/cv-arxiv-daily/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[forks-url]: https://github.com/Vincentqyw/cv-arxiv-daily/network/members
[stars-shield]: https://img.shields.io/github/stars/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[stars-url]: https://github.com/Vincentqyw/cv-arxiv-daily/stargazers
[issues-shield]: https://img.shields.io/github/issues/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[issues-url]: https://github.com/Vincentqyw/cv-arxiv-daily/issues

