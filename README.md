[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]

## Updated on 2024.07.14
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
|**2024-07-11**|**WayveScenes101: A Dataset and Benchmark for Novel View Synthesis in Autonomous Driving**|我们介绍了WayveScenes101，这是一个数据集，旨在帮助社区推进新颖视图合成的最新技术，该数据集侧重于挑战包含许多动态和可变形元素的驾驶场景，这些元素具有不断变化的几何形状和纹理。该数据集包括101个驾驶场景，涵盖了广泛的环境条件和驾驶场景。该数据集旨在对野外驾驶场景中的重建进行基准测试，场景重建方法存在许多固有挑战，包括图像眩光、快速曝光变化和具有显著遮挡的高度动态场景。除了原始图像，我们还包括标准数据格式的COLMAP导出的相机姿态。我们提出了一种评估协议，用于评估与训练视图离轴的手持相机视图上的模型，特别是测试方法的泛化能力。最后，我们为所有场景提供详细的元数据，包括天气、时间和交通状况，以便对场景特征进行详细的模型性能细分。数据集和代码可在https://github.com/wayveai/wayve_scenes. et.al.|[2407.08280](http://arxiv.org/abs/2407.08280)|**[link](https://github.com/wayveai/wayve_scenes)**|
|**2024-07-11**|**GAURA: Generalizable Approach for Unified Restoration and Rendering of Arbitrary Views**|神经渲染方法可以从姿态输入图像中实现场景的接近真实感的图像合成。然而，当图像不完美时，例如在非常低的光照条件下捕获的图像，最先进的方法无法重建高质量的3D场景。最近的方法试图通过在图像形成模型中建模各种退化过程来解决这一局限性；然而，这将它们限制在特定的图像退化上。在本文中，我们提出了一种可推广的神经渲染方法，可以在多种退化情况下进行高保真的新颖视图合成。我们的方法GAURA是基于学习的，不需要任何特定于测试时间场景的优化。它在包括几种降解类型的合成数据集上进行训练。GAURA在低光增强、去噪、去噪和运动去模糊的几个基准测试中表现优于最先进的方法。此外，我们的模型可以使用最少的数据有效地微调到任何新的传入退化。因此，我们展示了两种看不见的退化的适应结果，即去锯齿和去除散焦模糊。代码和视频结果可在vinayak-vg.ithub.io/GAURA上获得。 et.al.|[2407.08221](http://arxiv.org/abs/2407.08221)|null|
|**2024-07-10**|**Geospecific View Generation -- Geometry-Context Aware High-resolution Ground View Inference from Satellite Views**|由于卫星图像和地面图像之间存在显著的视图差距，因此在城市场景中从卫星图像预测逼真的地面视图是一项具有挑战性的任务。我们提出了一种新的管道来应对这一挑战，通过生成地理特定的视图，最大限度地尊重多视图卫星图像中的弱几何和纹理。与现有的从头顶卫星图像的部分语义或几何形状等线索中产生幻觉图像的方法不同，我们的方法通过使用卫星图像中的一组综合信息直接预测地理位置的地面视图图像，从而得到分辨率提高了十倍或更多的地面图像。我们利用一种新的建筑细化方法来减少地面卫星数据中的几何失真，这确保了使用扩散网络为视图合成创造准确的条件。此外，我们提出了一种新的地理特异性先验，它促使扩散模型的分布学习，以尊重更接近预测图像地理位置的图像样本。我们证明，我们的管道是第一个仅基于卫星图像生成接近真实和特定于地球的地面视图的管道。 et.al.|[2407.08061](http://arxiv.org/abs/2407.08061)|null|
|**2024-07-10**|**Generative Image as Action Models**|图像生成扩散模型已经过微调，以解锁图像编辑和新颖的视图合成等新功能。我们能否同样解锁用于视觉运动控制的图像生成模型？我们介绍了GENIMA，这是一种行为克隆代理，可以微调稳定扩散，在RGB图像上“绘制联合动作”作为目标。这些图像被输入控制器，该控制器将视觉目标映射到一系列关节位置。我们在25个RLBench和9个真实操作任务上研究了GENIMA。我们发现，通过将动作提升到图像空间，互联网预训练的扩散模型可以生成优于最先进的视觉运动方法的策略，特别是在对场景扰动的鲁棒性和对新对象的泛化方面。我们的方法也与3D代理竞争，尽管缺乏深度、关键点或运动规划等先验知识。 et.al.|[2407.07875](http://arxiv.org/abs/2407.07875)|null|
|**2024-07-10**|**Controlling Space and Time with Diffusion Models**|我们提出了4DiM，这是一种用于4D新颖视图合成（NVS）的级联扩散模型，以一般场景的一个或多个图像以及一组相机姿态和时间戳为条件。为了克服由于4D训练数据可用性有限而带来的挑战，我们提倡对3D（有相机姿势）、4D（姿势+时间）和视频（时间但没有姿势）数据进行联合训练，并提出了一种新的架构来实现这一点。我们进一步主张使用单目度量深度估计器对SfM姿态数据进行校准，以实现度量尺度相机控制。对于模型评估，我们引入了新的度量来丰富和克服当前评估方案的缺点，与现有的3D NVS扩散模型相比，在保真度和姿态控制方面展示了最先进的结果，同时增加了处理时间动态的能力。4DiM还用于改进全景拼接、姿势调节的视频到视频翻译以及其他一些任务。有关概述，请参阅https://4d-diffusion.github.io et.al.|[2407.07860](http://arxiv.org/abs/2407.07860)|null|
|**2024-07-09**|**Reference-based Controllable Scene Stylization with Gaussian Splatting**|基于内容对齐的参考图像编辑外观的基于参考的场景样式化是一个新兴的研究领域。从预训练的神经辐射场（NeRF）开始，现有的方法通常会学习与给定风格相匹配的新颖外观。尽管它们很有效，但它们固有地存在耗时的体绘制问题，因此对于许多实时应用程序来说是不切实际的。在这项工作中，我们提出了ReGS，它将3D高斯散点（3DGS）应用于基于参考的风格化，以实现实时风格化的视图合成。编辑预训练3DGS的外观具有挑战性，因为它使用离散高斯作为3D表示，将外观与几何体紧密结合。像现有方法那样简单地优化外观通常不足以在给定的参考图像中对连续纹理进行建模。为了应对这一挑战，我们提出了一种新的纹理引导控制机制，该机制自适应地将局部负责的高斯分布调整为新的几何排列，以获得所需的纹理细节。所提出的过程以纹理线索为指导，进行有效的外观编辑，并根据场景深度进行正则化，以保持原始几何结构。通过这些新颖的设计，我们证明ReG可以产生最先进的风格化结果，这些结果尊重参考纹理，同时为自由视图导航提供实时渲染速度。 et.al.|[2407.07220](http://arxiv.org/abs/2407.07220)|null|
|**2024-07-08**|**RRM: Relightable assets using Radiance guided Material extraction**|在过去几年中，在任意光照下合成NeRF已成为一个具有开创性的问题。最近的努力通过提取基于物理的参数来解决这个问题，这些参数可以在任意光照下渲染，但它们在可以处理的场景范围内是有限的，通常是对光滑场景的处理不当。我们提出了RRM，这是一种即使在存在高反射物体的情况下也可以提取场景的材质、几何形状和环境照明的方法。我们的方法包括一个基于物理参数的物理感知辐射场表示，以及一个基于拉普拉斯金字塔的富有表现力的环境光结构。我们证明，我们的贡献在参数检索任务上优于最先进的技术，从而在表面场景上实现了高保真的重新照明和新颖的视图合成。 et.al.|[2407.06397](http://arxiv.org/abs/2407.06397)|null|
|**2024-07-08**|**PanDORA: Casual HDR Radiance Acquisition for Indoor Scenes**|大多数新颖的视图合成方法，如NeRF，都无法捕捉场景的真实高动态范围（HDR）辐射，因为它们通常是在用标准低动态范围（LDR）相机捕获的照片上训练的。虽然以不同曝光捕获多幅图像的传统曝光包围方法最近已被应用于多视图情况，但我们发现这些方法无法捕获室内场景的全部动态范围，其中包括非常明亮的光源。本文介绍了PanDORA：一种全景双观察者辐射采集系统，用于在高动态范围内随意捕捉室内场景。我们提出的系统包括两个固定在便携式三脚架上的360度相机。摄像机同时采集两个360度视频：一个以常规曝光，另一个以非常快的曝光，使用户可以在几分钟内随意地在场景中挥动设备。生成的图像被馈送到基于NeRF的算法，该算法重建场景的完整高动态范围。与之前工作的HDR基线相比，我们的方法在不牺牲视觉质量的情况下重建了室内场景的完整HDR辐射，同时保留了最近类似NeRF的方法的易捕获性。 et.al.|[2407.06150](http://arxiv.org/abs/2407.06150)|null|
|**2024-07-08**|**PerlDiff: Controllable Street View Synthesis Using Perspective-Layout Diffusion Models**|可控生成被认为是解决注释3D数据挑战的一种潜在的重要方法，在自动驾驶数据生产的背景下，这种可控生成的精度变得尤为重要。现有的方法侧重于将各种生成信息整合到控制输入中，利用GLIGEN或ControlNet等框架，在可控生成中产生值得称赞的结果。然而，这种方法本质上将生成性能限制在预定义网络架构的学习能力上。本文探讨了控制信息的集成，并介绍了PerlDiff（透视布局扩散模型），这是一种充分利用透视3D几何信息的有效街景图像生成方法。我们的PerlDiff采用3D几何先验来指导街道视图图像的生成，并在网络学习过程中进行精确的对象级控制，从而产生更稳健和可控的输出。此外，与其他布局控制方法相比，它表现出更优的可控性。实证结果证明，我们的PerlDiff显著提高了NuScenes和KITTI数据集的生成精度。我们的代码和模型可在以下网址公开获取https://github.com/LabShuHangGU/PerlDiff. et.al.|[2407.06109](http://arxiv.org/abs/2407.06109)|**[link](https://github.com/labshuhanggu/perldiff)**|
|**2024-07-08**|**OSN: Infinite Representations of Dynamic 3D Scenes from Monocular Videos**|长期以来，从单眼RGB视频中恢复底层动态3D场景表示一直是一个挑战。现有的工作将这个问题表述为通过添加各种约束（如深度先验和强几何约束）来找到一个最合理的解决方案，忽略了一个动态视频可能对应无限多个3D场景表示的事实。在本文中，我们的目标是学习与输入视频匹配的所有合理的3D场景配置，而不仅仅是推断一个特定的配置。为了实现这一宏伟目标，我们引入了一个名为OSN的新框架。我们方法的关键是一个简单而创新的对象比例网络，以及一个联合优化模块，为每个动态3D对象学习精确的比例范围。这使我们能够对尽可能多的忠实3D场景配置进行采样。大量实验表明，我们的方法超越了所有基线，在多个合成和真实世界数据集上的动态新视图合成中取得了卓越的精度。最值得注意的是，我们的方法在学习细粒度3D场景几何方面具有明显的优势。我们的代码和数据可在https://github.com/vLAR-group/OSN et.al.|[2407.05615](http://arxiv.org/abs/2407.05615)|**[link](https://github.com/vlar-group/osn)**|

<p align=right>(<a href=#updated-on-20240714>back to top</a>)</p>

## 3D Reconstruction

|Publish Date|Title|Abstract|PDF|Code|
|---|---|---|---|---|
|**2024-07-11**|**Determination of five-parameter grain boundary characteristics in nanocrystalline Ni-W by Scanning Precession Electron Diffraction Tomography**|通过实验确定完整的五参数晶界特征对于理解晶界对材料性能的影响、改进相关模型和设计先进合金至关重要。然而，由于其3D特性，实现这一目标通常具有挑战性，特别是在纳米级。在我们的研究中，我们使用扫描进动电子衍射（SPED）断层扫描成功地确定了含有孪晶的退火镍钨合金（NiW）纳米晶针状试样（尖端）的晶界特性。这种面心立方（fcc）材料中退火孪晶的存在导致SPED衍射图案中的共同反射，这对3D晶粒形状断层重建所需的特定取向虚拟暗场（VDF）图像的重建提出了挑战。为了解决这个问题，在重建VDF图像之前，自动后处理步骤会识别和取消选择这些共享反射。结合适当的强度归一化和投影对齐程序，这种方法能够对针状样品体积中包含的单个颗粒进行高保真3D重建。为了探测所得边界特征的准确性，使用3D霍夫变换从3D体素化晶界图中提取了双边界表面法线方向。对于相干Sigma 3边界的子集，对于小于400 nm的边界尺寸，获得了预期的{111}晶界平面法线，角度误差小于3{\textdegree}。这项工作提高了我们精确表征和理解控制材料性能的复杂晶界的能力。 et.al.|[2407.08251](http://arxiv.org/abs/2407.08251)|null|
|**2024-07-11**|**Bayesian uncertainty analysis for underwater 3D reconstruction with neural radiance fields**|神经辐射场（NeRF）是一种深度学习技术，可以使用来自不同观察方向和相机姿态的稀疏2D图像生成3D场景的新视图。SeaThru NeRF是传统NeRF在水下环境中的扩展，光可以被水吸收和散射，它被提出将水下场景的干净外观和几何结构与散射介质的影响分开。由于水下场景的外观和结构质量对于水下基础设施检查等下游任务至关重要，因此应考虑和评估3D重建模型的可靠性。然而，由于缺乏量化自然环境照明下水下场景3D重建中的不确定性的能力，NeRF在无人自主水下导航中的实际部署受到限制。为了解决这个问题，我们在SeaThru NeRF中引入了一个基于贝叶斯射线的空间扰动场D_omega，并进行拉普拉斯近似以获得参数omega的高斯分布N（0，Sigma），其中Sigma的对角元素对应于每个空间位置的不确定性。我们还采用了一种简单的阈值方法来去除水下场景渲染结果中的伪影。数值实验证明了该方法的有效性。 et.al.|[2407.08154](http://arxiv.org/abs/2407.08154)|null|
|**2024-07-11**|**Survey on Fundamental Deep Learning 3D Reconstruction Techniques**|这项调查旨在研究基于基础深度学习（DL）的3D重建技术，这些技术可以生成逼真的3D模型和场景，突出神经辐射场（NeRF）、潜在扩散模型（LDM）和3D高斯散斑。我们剖析了底层算法，评估了它们的优势和权衡，并在这个快速发展的领域预测了未来的研究轨迹。我们全面概述了DL驱动的3D场景重建的基本原理，深入了解了它们的潜在应用和局限性。 et.al.|[2407.08137](http://arxiv.org/abs/2407.08137)|null|
|**2024-07-10**|**RoCap: A Robotic Data Collection Pipeline for the Pose Estimation of Appearance-Changing Objects**|当用户操纵有形物体作为控制器时，物体姿态估计在混合现实交互中起着至关重要的作用。传统的基于视觉的物体姿态估计方法利用3D重建来合成训练数据。然而，这些方法是为具有漫反射颜色的静态对象设计的，对于在操作过程中改变外观的对象效果不佳，例如毛绒玩具等可变形对象、化学烧瓶等透明对象、金属水罐等反射对象和剪刀等铰接对象。为了解决这一局限性，我们提出了Rocap，这是一种机器人管道，可以模拟人类对目标对象的操纵，同时生成标记有地面真实姿态信息的数据。用户首先将目标对象交给机器人手臂，系统以各种6D配置捕获对象的许多图片。该系统通过使用捕获的图像及其根据机器人手臂的关节角度自动计算的地面真实姿态信息来训练模型。我们通过使用收集的数据训练简单的深度学习模型，并将结果与基于3D重建的合成数据训练的模型进行比较，通过定量和定性评估，展示了外观变化物体的姿态估计。这些发现突显了Rocap的潜力。 et.al.|[2407.08081](http://arxiv.org/abs/2407.08081)|null|
|**2024-07-10**|**Chat-Edit-3D: Interactive 3D Scene Editing via Text Prompts**|最近基于视觉语言预训练模型的图像内容操纵工作已有效地扩展到文本驱动的3D场景编辑。然而，现有的3D场景编辑方案仍然存在某些缺点，阻碍了它们的进一步交互设计。这种方案通常遵循固定的输入模式，限制了用户在文本输入方面的灵活性。此外，它们的编辑能力受到单个或几个2D视觉模型的限制，需要复杂的管道设计将这些模型集成到3D重建过程中。为了解决上述问题，我们提出了一种基于对话的3D场景编辑方法，称为CE3D，它以一个大型语言模型为中心，允许用户任意输入文本并解释他们的意图，从而促进相应视觉专家模型的自主调用。此外，我们设计了一种利用哈希图集来表示3D场景视图的方案，该方案将3D场景的编辑转移到2D图集图像上。该设计实现了2D编辑和3D重建过程之间的完全解耦，使CE3D能够灵活地集成各种现有的2D或3D视觉模型，而不需要复杂的融合设计。实验结果表明，CE3D有效地整合了多种视觉模型，实现了多样化的编辑视觉效果，具有很强的场景理解能力和多轮对话能力。该代码可在以下网址获得https://sk-fun.fun/CE3D. et.al.|[2407.06842](http://arxiv.org/abs/2407.06842)|null|
|**2024-07-09**|**Computer vision tasks for intelligent aerospace missions: An overview**|计算机视觉任务对于航空航天任务至关重要，因为它们帮助航天器理解和解释空间环境，例如估计位置和方向、重建3D模型和识别物体，这些任务已被广泛研究以成功执行任务。然而，卡尔曼滤波、运动结构和多视图立体等传统方法不足以处理恶劣条件，导致结果不可靠。近年来，基于深度学习（DL）的感知技术显示出巨大的潜力，并优于传统方法，特别是在对不断变化的环境的鲁棒性方面。为了进一步推进基于DL的航空航天感知，已经提出了各种框架、数据集和策略，表明未来应用的巨大潜力。在这项调查中，我们旨在探索感知任务中使用的有前景的技术，并强调基于DL的航空航天感知的重要性。我们首先概述了航空航天感知，包括近年来开发的经典空间项目、常用传感器和传统感知方法。随后，我们深入研究了航空航天任务中的三个基本感知任务：姿态估计、3D重建和识别，因为它们对后续的决策和控制至关重要。最后，我们讨论了当前研究的局限性和可能性，并对未来的发展进行了展望，包括使用有限数据集的挑战、改进算法的必要性以及多源信息融合的潜在好处。 et.al.|[2407.06513](http://arxiv.org/abs/2407.06513)|null|
|**2024-07-09**|**LuSNAR:A Lunar Segmentation, Navigation and Reconstruction Dataset based on Muti-sensor for Autonomous Exploration**|随着月球探测任务的复杂性，月球需要更高的自主性。环境感知和导航算法是月球车实现自主探索的基础。算法的开发和验证需要高度可靠的数据支持。现有的月球数据集大多针对单一任务，缺乏多样化的场景和高精度的地面实况标签。为了解决这个问题，我们提出了一个多任务、多场景和多标签的月球基准数据集LuSNAR。该数据集可用于全面评估自主感知和导航系统，包括高分辨率立体图像对、全景语义标签、密集深度图、激光雷达点云和漫游车的位置。为了提供更丰富的场景数据，我们基于虚幻引擎构建了9个月球模拟场景。每个场景根据地形起伏和物体密度进行划分。为了验证数据集的可用性，我们评估和分析了语义分割、3D重建和自主导航的算法。实验结果证明，本文提出的数据集可用于自主环境感知和导航等任务的地面验证，并为测试算法度量的可访问性提供了月球基准数据集。我们在以下网址公开提供LuSNAR：https://github.com/autumn999999/LuSNAR-dataset. et.al.|[2407.06512](http://arxiv.org/abs/2407.06512)|**[link](https://github.com/autumn999999/lusnar-dataset)**|
|**2024-07-08**|**Tailor3D: Customized 3D Assets Editing and Generation with Dual-Side Images**|3D AIGC的最新进展表明，它有望直接从文本和图像创建3D对象，从而在动画和产品设计方面节省大量成本。然而，3D资源的详细编辑和定制仍然是一个长期存在的挑战。具体来说，3D生成方法缺乏像2D图像创建方法那样精确地遵循精细详细指令的能力。想象一下，你可以通过3D AIGC获得一个玩具，但带有不需要的配件和服装。为了应对这一挑战，我们提出了一种名为Tailor3D的新型管道，它可以从可编辑的双面图像中快速创建定制的3D资产。我们的目标是模仿裁缝在局部更改对象或执行整体风格转换的能力。与从多个视图创建3D资源不同，使用双面图像消除了编辑单个视图时发生的重叠区域冲突。具体来说，它首先编辑前视图，然后通过多视图扩散生成对象的后视图。之后，它继续编辑后视图。最后，提出了一种双面LRM，将正面和背面的3D特征无缝缝合在一起，类似于裁缝将衣服的正面和背面缝合在一起。双面LRM纠正了前后视图之间不完美的一致性，增强了编辑能力，减轻了内存负担，同时将它们与LoRA Triple Plane Transformer无缝集成到统一的3D表示中。实验结果证明了Tailor3D在各种3D生成和编辑任务中的有效性，包括3D生成填充和样式转换。它为编辑3D资源提供了一种用户友好、高效的解决方案，每个编辑步骤只需几秒钟即可完成。 et.al.|[2407.06191](http://arxiv.org/abs/2407.06191)|null|
|**2024-07-06**|**Incremental Multiview Point Cloud Registration**|本文提出了一种新的多视点云配准方法。与之前通常采用全局方案进行多视图配准的研究不同，我们建议采用增量流水线将扫描逐步对齐到规范坐标系中。具体来说，从基于图像的3D重建中汲取灵感，我们的方法首先通过扫描检索和几何验证构建稀疏扫描图。然后，我们通过初始化、下一次扫描选择和注册、轨道创建和继续以及捆绑调整来执行增量注册。此外，对于无检测器的匹配器，我们引入了Track细化过程。此过程主要构建粗略的多视图配准，并通过调整轨迹上关键点的位置来细化模型。实验证明，在三个基准数据集上，所提出的框架优于现有的多视图配准方法。该代码可在以下网址获得https://github.com/Choyaa/IncreMVR. et.al.|[2407.05021](http://arxiv.org/abs/2407.05021)|null|
|**2024-07-05**|**LaRa: Efficient Large-Baseline Radiance Fields**|辐射场方法实现了逼真的新颖视图合成和几何重建。但它们主要应用于每场景优化或小基线设置。虽然最近的几项工作利用变压器研究了具有大基线的前馈重建，但它们都使用标准的全局注意力机制进行操作，因此忽略了3D重建的局部性质。我们提出了一种在变压器层中统一局部和全局推理的方法，从而提高了质量并加快了收敛速度。我们的模型将场景表示为高斯体积，并将其与图像编码器和组注意力层相结合，以实现高效的前馈重建。实验结果表明，我们的模型在四个GPU上训练了两天，在重建360度辐射场时表现出了高保真度，并对零样本和域外测试表现出了鲁棒性。 et.al.|[2407.04699](http://arxiv.org/abs/2407.04699)|null|

<p align=right>(<a href=#updated-on-20240714>back to top</a>)</p>

## Diffusion

|Publish Date|Title|Abstract|PDF|Code|
|---|---|---|---|---|
|**2024-07-11**|**Video Diffusion Alignment via Reward Gradients**|我们在构建基础视频扩散模型方面取得了重大进展。由于这些模型是使用大规模无监督数据训练的，因此使这些模型适应特定的下游任务变得至关重要。通过监督微调调整这些模型需要收集视频的目标数据集，这既具有挑战性又繁琐。在这项工作中，我们利用预先训练的奖励模型，这些模型是在强大的视觉辨别模型之上通过偏好学习的，以适应视频扩散模型。这些模型包含关于生成的RGB像素的密集梯度信息，这对于在复杂的搜索空间（如视频）中高效学习至关重要。我们证明，将这些奖励模型的梯度反向传播到视频扩散模型可以实现视频扩散模型的计算和采样高效对齐。我们展示了各种奖励模型和视频扩散模型的结果，表明我们的方法在奖励查询和计算方面比之前的无梯度方法更有效地学习。我们的代码、模型权重和更多可视化信息可在https://vader-vid.github.io. et.al.|[2407.08737](http://arxiv.org/abs/2407.08737)|**[link](https://github.com/mihirp1998/vader)**|
|**2024-07-11**|**Live2Diff: Live Stream Translation via Uni-directional Attention in Video Diffusion Models**|大型语言模型在生成文本和音频等流数据方面表现出了显著的功效，这要归功于它们的时间单向注意力机制，该机制模拟了当前令牌和先前令牌之间的相关性。然而，尽管对实时视频处理的需求日益增长，但视频流的探索仍然很少。最先进的视频扩散模型利用双向时间注意力来模拟当前帧和所有周围（即包括未来）帧之间的相关性，这阻碍了它们处理流媒体视频。为了解决这个问题，我们提出了Live2Diff，这是第一次尝试设计一个具有单向时间注意力的视频扩散模型，专门针对直播视频翻译。与之前的工作相比，我们的方法通过将当前帧与其前一帧和一些初始预热帧相关联来确保时间一致性和平滑性，而没有任何未来帧。此外，我们使用了一种高效的去噪方案，该方案具有KV缓存机制和流水线，以促进交互式帧率下的流媒体视频翻译。大量实验证明了所提出的注意力机制和流水线的有效性，在时间平滑度和/或效率方面优于之前的方法。 et.al.|[2407.08701](http://arxiv.org/abs/2407.08701)|null|
|**2024-07-11**|**CAD-Prompted Generative Models: A Pathway to Feasible and Novel Engineering Designs**|文本到图像生成模型越来越多地用于在各种创意领域（如平面设计、用户界面设计和时装设计）的概念生成过程中协助设计师。然而，由于模型在生成可行设计概念的图像方面存在挑战，它们在工程设计中的应用仍然有限。为了解决这个问题，本文介绍了一种通过提示生成可行的CAD图像来提高设计可行性的方法。在这项工作中，通过一个自行车设计任务的案例研究，使用现成的文本到图像模型Stable Diffusion 2.1，研究了这种方法的有用性。在七种不同的生成设置中，使用不同的CAD图像提示权重生成了一组不同的自行车设计，并根据其感知的可行性和新颖性对这些设计进行了评估。结果表明，CAD图像提示成功地帮助文本到图像模型（如Stable Diffusion 2.1）创建了更可行的设计图像。虽然在可行性和新颖性之间存在一般的权衡，但当提示权重保持在0.35左右的较低水平时，设计可行性显著提高，而其新颖性仍与仅由文本提示产生的设计可行性相当。本案例研究的见解为为工程设计过程的不同阶段选择合适的CAD图像提示权重提供了一些指导。当有效利用时，我们的CAD图像提示方法为文本到图像模型在工程设计中的更广泛应用打开了大门。 et.al.|[2407.08675](http://arxiv.org/abs/2407.08675)|null|
|**2024-07-11**|**Controlling the Fidelity and Diversity of Deep Generative Models via Pseudo Density**|我们引入了一种方法，将深度生成模型（如GAN和扩散模型）偏向于生成具有增强保真度或增加多样性的数据。我们的方法涉及通过一种名为伪密度的单个样本的新度量来操纵训练和生成数据的分布，该度量基于真实样本的最近邻信息。我们的方法提供了三种不同的技术来调整深度生成模型的保真度和多样性：1）每个样本的扰动，使单个样本能够朝着更常见或更独特的特征进行精确调整；2） 在模型推断过程中进行重要性抽样，以提高生成数据的保真度或多样性；3） 通过重要性抽样进行微调，引导生成模型学习调整后的分布，从而控制保真度和多样性。此外，我们的微调方法证明了通过最小迭代来提高预训练生成模型的Frechet初始距离（FID）的能力。 et.al.|[2407.08659](http://arxiv.org/abs/2407.08659)|null|
|**2024-07-11**|**Fine-Tuning Stable Diffusion XL for Stylistic Icon Generation: A Comparison of Caption Size**|本文介绍了稳定扩散XL的不同微调方法；这包括推理步骤和针对每个图像的字幕定制以与以商业2D图标训练集的风格生成图像对齐。我们还展示了正确定义“高质量”的重要性，尤其是对于商业使用环境。随着生成式人工智能模型不断得到广泛接受和使用，出现了许多不同的方法来优化和评估它们以用于各种应用。具体来说，文本到图像模型，如Stable Diffusion XL和DALL-E 3，需要不同的评估实践，才能根据特定风格有效地生成高质量的图标。尽管基于某种风格生成的一些图像可能具有较低的FID分数（更好），但我们展示了即使对于光栅化图标，这本身也不是绝对的。虽然FID分数反映了生成的图像与整体训练集的相似性，但CLIP分数衡量的是生成的图像与其文本描述之间的一致性。我们展示了FID分数如何遗漏重要方面，例如图标中最重要的少数像素差异，而CLIP分数则导致对图标质量的误判。CLIP模型对“相似性”的理解是由其自身的训练数据塑造的；这并不能解释我们选择风格中的特征变化。我们的研究结果强调，在生成高质量的商业图标时，需要专门的评估指标和微调方法，这可能会使文本到图像模型在专业设计环境中得到更有效和量身定制的应用。 et.al.|[2407.08513](http://arxiv.org/abs/2407.08513)|null|
|**2024-07-11**|**Latent Conditional Diffusion-based Data Augmentation for Continuous-Time Dynamic Graph Mode**|连续时间动态图（CTDG）精确地模拟了不断发展的现实世界关系，引起了学术界和工业界对动态图学习的浓厚兴趣。然而，现有的CTDG模型面临着噪声和有限历史数据带来的挑战。图形数据增强（GDA）是一种关键的解决方案，但目前的方法主要侧重于静态图形，难以有效地解决CTDG中固有的动态问题。此外，这些方法通常需要大量的领域专业知识来进行参数调整，并且缺乏增强效果的理论保证。为了解决这些问题，我们提出了Conda，这是一种针对CTDG量身定制的基于潜在扩散的新型GDA方法。Conda采用三明治式架构，结合了变分自动编码器（VAE）和条件扩散模型，旨在为目标节点生成增强的历史邻居嵌入。与通过预训练在整个图上训练的传统扩散模型不同，Conda需要目标节点的历史邻居序列嵌入进行训练，从而促进更有针对性的增强。我们将Conda整合到CTDG模型中，并采用交替训练策略来优化性能。在六个广泛使用的真实世界数据集上进行的广泛实验表明，我们的方法在性能上得到了持续的改进，特别是在历史数据有限的情况下。 et.al.|[2407.08500](http://arxiv.org/abs/2407.08500)|null|
|**2024-07-11**|**Killing versus catastrophes in birth-death processes and an application to population genetics**|我们建立了一类具有杀戮的出生-死亡过程的吸收概率与一类具有灾难的出生-死亡率过程的平稳尾部分布之间的联系。证明的主要成分是样本路径的偏移分解、广义的详细平衡条件，以及我们的过程在更简单过程叠加方面的表示。齐格蒙德二元性起着至关重要的作用，它使我们能够颠倒过程之间的关系。我们将我们的结果应用于种群遗传学中的一对祖先过程，即在有限种群设置及其扩散极限下，被杀死的祖先选择图和被修剪的向下祖先选择图。 et.al.|[2407.08478](http://arxiv.org/abs/2407.08478)|null|
|**2024-07-11**|**Propagation and non-reciprocity in time-modulated diffusion through the lens of high-order homogenization**|这里开发的均匀化过程是在具有精细尺度周期性时空调制的层压板上进行的：在前导阶，如果两个参数都被调制，这种调制会在低波长区域产生对流。然而，如果只调制一个参数，这更现实，这个对流项就会消失，并恢复一个具有有效均匀参数的标准扩散方程；这并没有描述从精确色散图中观察到的场的非互易性和传播。这里通过考虑二阶均匀化来纠正这种不一致性，这导致了一个非互易传播项，该项被证明对任何层压板都是非零的，并通过数值模拟进行了验证。同样的方法也适用于在热方程中调制密度的情况，从而产生一个校正的平流项，该项抵消了前导阶而非二阶的非互易性。 et.al.|[2407.08456](http://arxiv.org/abs/2407.08456)|null|
|**2024-07-11**|**A fitted space-time finite element method for an advection-diffusion problem with moving interfaces**|本文提出了一种求解非平稳界面抛物型平流扩散问题的拟合时空有限元方法。跳跃扩散系数导致界面上解的空间梯度不连续。我们用Banach Necas-Babuska定理证明了连续变分问题的适定性。使用伽略金方法和非结构化拟合网格对基于完全离散有限元的方案进行了分析。在适当的全局低但局部高正则性条件下，在离散能量范数中建立最优误差估计。一些数值结果证实了我们的理论结果。 et.al.|[2407.08439](http://arxiv.org/abs/2407.08439)|null|
|**2024-07-11**|**Diff-Tracker: Text-to-Image Diffusion Models are Unsupervised Trackers**|我们介绍了Diff Tracker，这是一种利用预训练的文本到图像扩散模型进行具有挑战性的无监督视觉跟踪任务的新方法。我们的主要想法是利用预先训练的扩散模型中包含的丰富知识，如对图像语义和结构信息的理解，来解决无监督的视觉跟踪问题。为此，我们设计了一个初始提示学习器，通过学习表示目标的提示，使扩散模型能够识别跟踪目标。此外，为了促进提示对目标动作的动态适应，我们提出了一种在线提示更新器。在五个基准数据集上进行的广泛实验证明了我们提出的方法的有效性，该方法也达到了最先进的性能。 et.al.|[2407.08394](http://arxiv.org/abs/2407.08394)|null|

<p align=right>(<a href=#updated-on-20240714>back to top</a>)</p>

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

<p align=right>(<a href=#updated-on-20240714>back to top</a>)</p>

[contributors-shield]: https://img.shields.io/github/contributors/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[contributors-url]: https://github.com/Vincentqyw/cv-arxiv-daily/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[forks-url]: https://github.com/Vincentqyw/cv-arxiv-daily/network/members
[stars-shield]: https://img.shields.io/github/stars/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[stars-url]: https://github.com/Vincentqyw/cv-arxiv-daily/stargazers
[issues-shield]: https://img.shields.io/github/issues/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[issues-url]: https://github.com/Vincentqyw/cv-arxiv-daily/issues

