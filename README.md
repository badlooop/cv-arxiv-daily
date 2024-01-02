[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]

## Updated on 2024.01.02
> Usage instructions: [here](./docs/README.md#usage)

<details>
  <summary>Table of Contents</summary>
  <ol>
    <li><a href=#3d-reconstruction>3D Reconstruction</a></li>
    <li><a href=#diffusion>Diffusion</a></li>
  </ol>
</details>

## 3D Reconstruction

|Publish Date|Title|Abstract|PDF|Code|
|---|---|---|---|---|
|**2023-12-29**|**Informative Rays Selection for Few-Shot Neural Radiance Fields**|神经辐射场（NeRF）最近已成为基于图像的3D重建的一种强大方法，但每个场景的漫长优化限制了其实际应用，尤其是在资源受限的环境中。现有的方法通过减少输入视图的数量并利用复杂的损失或来自其他模态的额外输入来正则化所学习的体积表示来解决这个问题。在本文中，我们提出了KeyNeRF，这是一种简单而有效的方法，通过聚焦关键信息射线，在少镜头场景中训练NeRF。这种射线首先在相机级别通过视图选择算法进行选择，该算法在保证场景覆盖的同时促进基线多样性，然后在像素级别通过基于局部图像熵的概率分布进行采样。我们的方法与最先进的方法相比表现良好，同时需要对现有NeRF代码库进行最小的更改。 et.al.|[2312.17561](http://arxiv.org/abs/2312.17561)|null|
|**2023-12-28**|**Toward Semantic Scene Understanding for Fine-Grained 3D Modeling of Plants**|由于全球人口增长以及对粮食和劳动力短缺的预期，农业机器人是一个活跃的研究领域。机器人可能有助于完成修剪、收割、表型分析和植物建模等任务。然而，农业自动化受到阻碍，因为难以在该领域创建高分辨率3D语义地图，从而实现安全操作和导航。在本文中，我们致力于解决这一问题，并展示了语义和环境先验的使用如何帮助为高粱的目标应用构建准确的3D地图。具体而言，我们1）使用高粱种子作为语义地标来构建视觉同步定位和映射（SLAM）系统，该系统使我们能够平均映射78%的高粱范围，而ORB-SLAM2的映射率为38%；和2）使用种子作为语义特征来改进由机器人手持相机拍摄的图像对完整高粱穗的3D重建。 et.al.|[2312.17110](http://arxiv.org/abs/2312.17110)|null|
|**2023-12-28**|**Geometry-Biased Transformer for Robust Multi-View 3D Human Pose Reconstruction**|我们解决了在遮挡和有限重叠视图下从多个视图估计3D人体姿态的挑战。我们将多视图、单人三维人体姿态重建作为一个回归问题，并提出了一种新的编码器-解码器-转换器架构，用于从多视图二维姿态序列中估计三维姿态。编码器对在不同视图和时间检测到的2D骨骼关节进行细化，通过全局自关注融合多视图和时间信息。我们通过结合有几何偏见的注意力机制来增强编码器，有效地利用视图之间的几何关系。此外，我们使用2D姿势检测器提供的检测分数来基于2D检测的可靠性进一步引导编码器的注意力。解码器随后使用针对每个关节的预定义查询，从这些细化的标记回归3D姿势序列。为了增强我们的方法对看不见的场景的泛化能力，并提高对缺失关节的恢复能力，我们实施了包括场景居中、合成视图和标记丢弃在内的策略。我们在三个基准公共数据集Human3.6M、CMU Panoptic和Occlusion Persons上进行了广泛的实验。我们的结果证明了我们的方法的有效性，特别是在遮挡场景和视图很少的情况下，这对于基于三角测量的方法来说是传统上具有挑战性的场景。 et.al.|[2312.17106](http://arxiv.org/abs/2312.17106)|null|
|**2023-12-28**|**Learning Spatially Collaged Fourier Bases for Implicit Neural Representation**|现有的隐式神经表示（INR）方法可以通过不同频率的傅立叶基的线性组合解释为全局场景表示。然而，这种通用基函数可能会限制不需要特定组件的局部区域的表示能力，从而导致令人不快的伪影。为此，我们引入了一种可学习的空间掩模，它可以有效地将不同的傅立叶基分派到各个区域中。这转化为拼贴傅立叶补丁，从而实现复杂信号的精确表示。综合实验证明，在各种INR任务中，包括图像拟合、视频表示和3D形状表示，所提出的方法的重建质量优于现有基线。我们的方法优于所有其他基线，将图像拟合PSNR提高了3dB以上，并将3D重建提高到98.81 IoU和0.0011倒角距离。 et.al.|[2312.17018](http://arxiv.org/abs/2312.17018)|null|
|**2023-12-27**|**In-Hand 3D Object Reconstruction from a Monocular RGB Video**|我们的工作旨在重建一只手在静态RGB相机前握住并旋转的3D物体。以前的方法使用隐式神经表示从多视图图像中恢复通用手持物体的几何结构，在物体的可见部分取得了令人信服的结果。然而，由于遮挡，这些方法在准确捕捉手-物体接触区域内的形状方面有困难。在本文中，我们提出了一种新的方法，通过结合二维遮挡说明的先验和物理接触约束来处理遮挡下的表面重建。对于前者，我们引入了一个对象阿莫尔完成网络来推断遮挡下对象的二维完全掩模。为了确保预测的2D变形掩模的准确性和视图一致性，我们设计了一种用于变形掩模细化和3D重建的联合优化方法。对于后者，我们对接触区域中的局部几何体施加穿透和吸引约束。我们在HO3D和HOD数据集上评估了我们的方法，并证明它在重建表面质量方面优于最先进的方法，在HO3D上提高了52美元，在HOD上提高了20美元。项目网页：https://east-j.github.io/ihor. et.al.|[2312.16425](http://arxiv.org/abs/2312.16425)|null|
|**2023-12-24**|**SUNDIAL: 3D Satellite Understanding through Direct, Ambient, and Complex Lighting Decomposition**|卫星图像的三维建模在环境科学、城市规划、农业和灾害应对领域至关重要。然而，传统的3D建模技术在遥感环境中面临着独特的挑战，包括大范围区域上有限的多视图基线，不同的直接、环境和复杂照明条件，以及不同捕获之间的时变场景变化。在这项工作中，我们介绍了SUNDIAL，这是一种使用神经辐射场进行卫星图像三维重建的综合方法。在这种单一模型方法中，我们共同学习了卫星场景几何结构、照明组件和太阳方向，并提出了一种二次阴影光线投射技术，以1）使用倾斜的太阳角来渲染阴影，改善场景几何结构，2）实现场景反照率和照明的物理解纠缠，以及3）确定来自直接环境（天空）的照明组件，以及复杂的来源。为了实现这一点，我们将遥感文献中的照明线索和几何先验纳入神经渲染方法，对卫星场景的物理特性进行建模，如阴影、散射天空照明以及植被和水的复杂照明和阴影。我们评估了SUNDIAL相对于现有基于NeRF的卫星场景建模技术的性能，并在具有小基线、稀疏输入和可变照明的具有挑战性的场景中展示了改进的场景和照明解纠缠、新颖的视图和照明渲染以及几何体和太阳方向估计。 et.al.|[2312.16215](http://arxiv.org/abs/2312.16215)|null|
|**2023-12-24**|**A theory of volumetric representations for opaque solids**|我们开发了一种将不透明固体表示为体积模型的理论。从不透明固体作为随机指示函数的随机表示开始，我们证明了可以使用指数体积输运对这种固体进行建模的条件。我们还导出了体积衰减系数的表达式，作为基本指标函数的概率分布的函数。我们将我们的理论推广到考虑固体不同部分的各向同性和各向异性散射，以及将不透明固体表示为隐式表面。我们从第一性原理推导出体积表示，这确保了它满足物理约束，如互易性和可逆性。我们使用我们的理论来解释、比较和纠正以前的体积表示，并提出有意义的扩展，从而提高3D重建任务的性能。 et.al.|[2312.15406](http://arxiv.org/abs/2312.15406)|null|
|**2023-12-23**|**WildScenes: A Benchmark for 2D and 3D Semantic Segmentation in Large-scale Natural Environments**|语义场景理解的最新进展主要得益于城市环境中语义注释的双模（相机和激光雷达）数据集的可用性。然而，自然、非结构化环境也需要这样的注释数据集，以实现应用程序的语义感知，包括保护、搜救、环境监测和农业自动化。因此，我们介绍了WildScenes，这是一个双模态基准数据集，由自然环境中的多个大规模遍历组成，包括高分辨率2D图像和密集3D激光雷达点云中的语义注释，以及精确的6-DoF姿态信息。数据（1）以轨迹为中心，具有精确的定位和全局对齐的点云，（2）校准和同步以支持双模态推理，以及（3）在6个月内包含不同的自然环境，以支持领域适应研究。我们的3D语义标签是通过一个高效的自动化过程获得的，该过程将人工注释的2D标签从多个视图转移到3D点云中，从而避免了在3D中进行昂贵且耗时的人工注释的需要。我们介绍了2D和3D语义分割的基准，并评估了最近的各种深度学习技术，以展示自然环境中语义分割的挑战。我们建议为标准基准和领域自适应基准训练val测试分割，并利用自动分割生成技术来确保类标签分布的平衡。数据、评估脚本和预训练模型将在https://csiro-robotics.github.io/WildScenes. et.al.|[2312.15364](http://arxiv.org/abs/2312.15364)|null|
|**2023-12-22**|**Enhanced Latent Multi-view Subspace Clustering**|潜在多视图子空间聚类已被证明具有理想的聚类性能。然而，原始的潜在表示方法沿着维度方向将来自多个视图的数据矩阵垂直连接到单个矩阵中，以恢复潜在表示矩阵，这可能导致不完整的信息恢复。为了完全恢复潜在空间表示，我们在本文中提出了一种增强的潜在多视图子空间聚类（ELMSC）方法。ELMSC方法包括构建增强数据矩阵，该矩阵增强多视图数据的表示。具体来说，我们将来自不同视图的数据矩阵堆叠到增广矩阵的块对角位置，以利用互补信息。同时，基于不同视图之间的相似性来组合非块对角条目，以获取一致的信息。此外，我们对增广自表示矩阵的非对角块强制执行稀疏正则化，以避免一致性信息的冗余计算。最后，基于交替方向乘法器（ADMM）的框架，提出了一种新的迭代算法来解决ELMSC的优化问题。在真实世界数据集上的大量实验表明，我们提出的ELMSC能够实现比一些现有技术的多视图聚类方法更高的聚类性能。 et.al.|[2312.14763](http://arxiv.org/abs/2312.14763)|**[link](https://github.com/caolei2000/elmsc-code)**|
|**2023-12-22**|**BonnBeetClouds3D: A Dataset Towards Point Cloud-based Organ-level Phenotyping of Sugar Beet Plants under Field Conditions**|未来几十年，农业生产面临着气候变化和可持续性需求带来的严峻挑战，从而减少其对环境的影响。通过机器人的非化学除草，结合自动无人机对作物的监测，以及培育新的、更具弹性的作物品种，在田间管理方面取得了进展，这有助于应对这些挑战。植物性状的分析，即表型分析，是植物育种中的一项重要活动，但它需要大量的体力劳动。通过这篇论文，我们解决了精确表型所需的自动细粒度器官级几何分析的问题。由于该领域的真实世界数据相对较少，我们提出了一个新的数据集，该数据集是使用无人机获取的，该无人机捕捉了包含48个植物品种的真实育种试验的高分辨率图像，因此涵盖了巨大的形态和外观多样性。这使得自主表型的方法能够很好地推广到不同的品种。基于多个视角的重叠高分辨率图像，我们计算了摄影测量密集点云，并为植物、叶子和作为尖端和底部的突出点提供了详细准确的逐点标签。此外，我们还包括德国联邦植物品种办公室的专家对真实植物进行的表型性状测量，从而不仅可以评估分割和关键点检测方面的新方法，还可以直接评估下游任务。所提供的标记点云能够进行细粒度的植物分析，并支持自动表型方法开发的进一步进展，但也能够在表面重建、点云完成和点云的语义解释方面进行进一步研究。 et.al.|[2312.14706](http://arxiv.org/abs/2312.14706)|null|

<p align=right>(<a href=#updated-on-20240102>back to top</a>)</p>

## Diffusion

|Publish Date|Title|Abstract|PDF|Code|
|---|---|---|---|---|
|**2023-12-29**|**Microstructural training and mechanical memory of nanocolloidal soft glasses under cyclic shear**|无序和失衡材料（如玻璃）的一个内在特征是其性质与历史的依赖性。一个重要的例子是流变记忆，其中无序固体根据其力学历史获得特性。在这里，我们使用x射线光子相关光谱（XPCS）和\textit｛原位｝流变仪来表征由于循环剪切而在纳米胶体软玻璃中形成的记忆。在一个循环中，粒子经历由剪切诱导的扩散和应变场组合而成的不可逆位移。在达到稳态之前，这些位移的幅度随着每个循环而减小，在稳态中微观结构已经被训练以实现增强的可逆性。位移类似于随机行走，其中每个循环中的方向独立于先前循环中的那些方向。与这些位移相关的是在每个循环之后残余应力的放大率向稳态值的逐渐演变。这种训练的记忆是通过测量揭示的，在测量中，达到稳定状态后剪切的幅度发生了变化。颗粒位移的大小以及残余应力的变化随着新的应变幅度而非单调变化，在训练幅度附近具有最小值，从而揭示了记忆的微观和宏观特征。 et.al.|[2312.17696](http://arxiv.org/abs/2312.17696)|null|
|**2023-12-29**|**FlowVid: Taming Imperfect Optical Flows for Consistent Video-to-Video Synthesis**|扩散模型已经将图像转换为图像（I2I）合成，并且现在正在渗透到视频中。然而，视频到视频（V2V）合成的发展受到了在视频帧之间保持时间一致性的挑战的阻碍。本文通过联合利用源视频中的空间条件和时间光流线索，提出了一个一致的V2V合成框架。与之前严格遵循光流的方法相反，我们的方法在处理流量估计中的缺陷时利用了其优点。我们通过第一帧的翘曲对光流进行编码，并将其作为扩散模型中的补充参考。这使得我们的视频合成模型能够通过用任何流行的I2I模型编辑第一帧，然后将编辑传播到连续帧来实现。我们的V2V模型FlowVid展示了非凡的特性：（1）灵活性：FlowVid与现有的I2I模型无缝配合，便于进行各种修改，包括风格化、对象交换和本地编辑。（2） 效率：生成30 FPS和512x512分辨率的4秒视频仅需1.5分钟，分别比CoDeF、Rerender和TokenFlow快3.1倍、7.2倍和10.5倍。（3） 高质量：在用户研究中，我们的FlowVid在45.7%的时间内是首选，优于CoDeF（3.5%）、Rerender（10.2%）和TokenFlow（40.4%）。 et.al.|[2312.17681](http://arxiv.org/abs/2312.17681)|null|
|**2023-12-29**|**Data Augmentation for Supervised Graph Outlier Detection with Latent Diffusion Models**|图异常检测是图神经网络领域研究和应用的一项突出任务。它识别出与图中大多数节点存在偏差的异常节点。监督图异常值检测算法面临的基本挑战之一是普遍存在的类不平衡问题，与正常实例相比，异常值实例的稀缺性往往导致性能次优。传统的方法通过在损失函数的估计中重新加权实例来减轻不平衡，将更高的权重分配给异常值，将更低的权重分配给与内值。尽管如此，这些策略分别容易出现过度拟合和拟合不足的情况。最近，生成模型，特别是扩散模型，已经证明了它们在合成高保真图像方面的功效。尽管它们具有非凡的生成质量，但它们在监督图异常值检测的数据增强方面的潜力在很大程度上仍未得到充分挖掘。为了弥补这一差距，我们引入了GODM，这是一种新的数据扩充方法，用于缓解潜在扩散模型监督图异常值检测中的类不平衡。具体来说，我们提出的方法由三个关键组件组成：（1）Variantioal Encoder将图数据中固有的异构信息映射到统一的潜在空间中。（2） 图生成器从潜在空间合成在统计上与真实异常值相似的图数据，并且（3）潜在扩散模型通过迭代去噪来学习真实有机数据的潜在空间分布。在多个数据集上进行的大量实验证实了GODM的有效性和效率。案例研究进一步证明了我们合成数据的生成质量。为了促进可访问性和可再现性，我们将GODM封装到即插即用包中，并在Python包索引（PyPI）处发布。 et.al.|[2312.17679](http://arxiv.org/abs/2312.17679)|**[link](https://github.com/kayzliu/godm)**|
|**2023-12-29**|**Antiferromagnetic behavior in self-bound one-dimensional composite bosons**|利用扩散蒙特卡罗技术计算了含有镱费米子同位素混合物（ $^{173}$Yb，$^{171}$Yb）的自束缚一维液滴的结构。我们只考虑了平衡的设置，其中一种同位素的所有原子都是自旋极化的，而另一个同位素的原子最多可以有三个不同的自旋值，这种差异是实现稳定系统的必要条件。我们的结果表明，这些液滴由连续的“分子”组成，由一个$^｛173｝$Yb和一个$^{171｝$ Y b原子组成。换句话说，我们有多达三种不同类型的复合玻色子，对应于非极化同位素中自旋分量的数量。这些Yb原子的费米子性质使具有相同自旋组成的对相互避开，产生了由另一个分子产生的泡利类空穴，其中至少一个Yb原子具有与其最近邻居不同的自旋。这种有效的排斥类似于不同种类的复合玻色子之间的反铁磁短程相互作用。 et.al.|[2312.17654](http://arxiv.org/abs/2312.17654)|null|
|**2023-12-29**|**On mild solutions to some dissipative SPDEs on $L^p$ spaces with additive noise**|在$\mathbb｛R｝^n$的有界域上的$L^p$空间上，我们建立了一类具有非线性漂移项的随机半线性演化方程的温和意义上的适定性，该非线性漂移项由具有幂增长的实线上的单调函数生成的叠加算子给出。关于圆柱形维纳过程，噪声是加法型的，扩散系数不一定是$\gamma$ -Radonifying型。 et.al.|[2312.17651](http://arxiv.org/abs/2312.17651)|null|
|**2023-12-29**|**Inverse Gertsenshtein effect as a probe of high-frequency gravitational waves**|我们应用反向Gertsenstein效应，即在磁场存在的情况下的引力子-光子转换，来约束高频引力波（HFGWs）。使用现有的天体物理测量，我们计算了16个不同频带的GW能量密度 $\Omega_｛\rm GW｝$的上限。考虑到在$\mathcal｛O｝（10）\，｛\rm-kpc｝$尺度上观测到的场强为$B\sim\mu｛\rm G｝$的星系团磁化，我们估计在$\math｛O}（10^2）\，｝\rm-GHz｝$范围内的HFGW约束为$\Omega_｛\rm-GW｝\lesssim10^｛16｝$，并使用阿塔卡马宇宙学望远镜（ACT）的温度测量。类似地，我们保守地获得$\mathcal｛O｝（10^2）\，｛\rm MHz｝$（$\mathical｛O}（10）\，｝\rm GHz｝$）区域中的$\Omega_｛\rm-GW｝\lesssim10^｛13｝，LOw Frequency ARray（LOFAR）和Murchison Widefield ARray（MWA），以及气球携带的第二代宇宙学、天体物理学和具有引力子诱导光子的漫发射绝对辐射计（ARCADE2）。尽管这些现有的限制都没有低于$\Omega_｛\rm GW｝=1$的临界值，也没有达到$\Omega｛\rmGW｝\smeq1.2\times10^｛-6｝$ 的大爆炸核合成（BBN）界限，但即将推出的平方公里阵列（SKA）可以将灵敏度提高大约10个数量级，并有可能成为HFGWs的现实探针。我们还探索了几项下一代CMB调查，包括原始通货膨胀探测器（PIXIE）、用于光谱偏差和不通货膨胀探测的偏振辐射干涉仪（PRISTINE）和Voyage 2050，这些调查可能会提供对当前BBN范围有竞争力的约束。 et.al.|[2312.17636](http://arxiv.org/abs/2312.17636)|null|
|**2023-12-29**|**Utilizing the Janus MoSSe surface polarization property in complementary metal-oxide-semiconductor field effect transistor design**|Janus过渡金属二硫族化合物（JTMD）因其优异的电子和光学性能而备受关注。JTMD中的额外平面外偶极子可以形成n型和p型欧姆接触，这可以用于器件应用，如pin二极管和光伏电池。在这项研究中，我们利用这一特性来设计n型和p型金属氧化物半导体场效应晶体管（MOSFET）。首先，我们使用密度泛函理论计算来研究三层JTMD-MoSSe中的固有偶极场强度。MoSSe的本征偶极导致金属/MoSSe和MoSSe/金属界面的能带弯曲，导致电子和空穴积累，形成n型和p型欧姆接触区。我们将这一特性结合到基于二维有限元的泊松漂移扩散求解器中进行模拟，在此基础上设计互补MOSFET。我们的结果表明，JTMD可以用于在同一层中制造n和p MOSFET，而不需要任何额外的掺杂。 et.al.|[2312.17594](http://arxiv.org/abs/2312.17594)|null|
|**2023-12-29**|**Leveraging Open-Vocabulary Diffusion to Camouflaged Instance Segmentation**|文本到图像扩散技术已经显示出从文本描述产生高质量图像的非凡能力。这表明视觉域和文本域之间存在很强的相关性。此外，由于开放概念提供了丰富多样的信息，CLIP等文本图像判别模型在文本提示的图像标记方面表现出色。在本文中，我们利用这些技术进步来解决计算机视觉中一个具有挑战性的问题：伪装实例分割。具体来说，我们提出了一种建立在最先进的扩散模型基础上的方法，该模型通过开放词汇来学习伪装对象表示的多尺度文本视觉特征。这种跨域表示在分割伪装对象时是可取的，其中视觉线索是微妙的以将对象与背景区分开，特别是在分割训练中看不到的新对象时。我们还开发了技术支持组件，以有效地融合跨领域特征，并将相关特征引入各自的前景对象。我们在伪装实例分割和通用开放词汇实例分割的几个基准数据集上验证了我们的方法，并将其与现有方法进行了比较。实验结果证实了我们的方法比现有方法的进步。我们将发布我们的代码和预先训练的模型，以支持未来的研究。 et.al.|[2312.17505](http://arxiv.org/abs/2312.17505)|null|
|**2023-12-29**|**Curvature diffusion of planar curves with generalised Neumann boundary conditions inside cones**|我们研究了光滑浸入正平面曲线族 $\alpha:\left[-1,1\right]\times\left[0，T\right）\ to \mathbb｛R｝^｛2｝$ ，它们满足锥内具有广义Neumann边界条件的四阶非线性曲线扩散流。，与锥边界一起包围了与初始曲线和锥边界相同的面积。对于具有适当边界条件的高阶多谐曲线扩散流，可能会得到相同的结果；特别是在六阶情况下，曲率振荡的小条件与曲线扩散完全相同。 et.al.|[2312.17490](http://arxiv.org/abs/2312.17490)|null|
|**2023-12-29**|**Sampling probabilities, diffusions, ancestral graphs, and duality under strong selection**|Wright-Fisher扩散及其对偶祖先图在等位基因频率变化和谱系结构的研究中起着核心作用，它们为采样概率提供了表达式，在某些特殊情况下是显式的，但通常是隐式的，这是推理中的一个关键量。在有限等位基因突变模型下，可能存在父母依赖性突变，我们考虑一个等位基因的选择性优势增长到无穷大，而其他参数保持不变的渐近状态。在这种情况下，我们证明了Wright Fisher扩散可以通过高斯过程或其分量是具有迁移的独立连续状态分支过程的过程来近似，这与Wright Fisher模型的类似结果一致，但采用了不同的方法。虽然第一个过程在平稳性下退化，但后者没有，并为采样概率的前导项提供了一个简单的解析近似。此外，使用另一种基于递归公式的方法，我们对所有剩余项进行表征，以提供采样概率的完全渐近展开。最后，我们研究了条件祖先选择图的块计数过程的速率的渐近行为，并建立了它与扩散之间的渐近对偶关系。 et.al.|[2312.17406](http://arxiv.org/abs/2312.17406)|null|

<p align=right>(<a href=#updated-on-20240102>back to top</a>)</p>

[contributors-shield]: https://img.shields.io/github/contributors/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[contributors-url]: https://github.com/Vincentqyw/cv-arxiv-daily/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[forks-url]: https://github.com/Vincentqyw/cv-arxiv-daily/network/members
[stars-shield]: https://img.shields.io/github/stars/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[stars-url]: https://github.com/Vincentqyw/cv-arxiv-daily/stargazers
[issues-shield]: https://img.shields.io/github/issues/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[issues-url]: https://github.com/Vincentqyw/cv-arxiv-daily/issues

