[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]

## Updated on 2024.11.13
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
|**2024-11-11**|**A Hierarchical Compression Technique for 3D Gaussian Splatting Compression**|3D高斯散斑（GS）在新颖的视图合成中表现出优异的渲染质量和生成速度。然而，大量的数据量给存储和传输带来了挑战，使3D GS压缩成为一项必不可少的技术。当前的3D GS压缩研究主要集中在开发更紧凑的场景表示，例如将显式的3D GS数据转换为隐式形式。相比之下，GS数据本身的压缩几乎并没有得到探索。为了解决这一差距，我们提出了一种分层GS压缩（HGSC）技术。最初，我们根据从全局和局部重要性中得出的重要性得分来修剪不重要的高斯分布，有效地减少了冗余，同时保持了视觉质量。八叉树结构用于压缩3D位置。基于3D GS八叉树，我们采用KD树将3D GS划分为多个块，实现了一种分层属性压缩策略。我们应用最远点采样来选择每个块内的锚基元，并将其他锚基元作为具有不同细节级别（LoD）的非锚基元。锚基元用作跨不同LoD预测非锚基元的参考点，以减少空间冗余。对于锚基元，我们使用区域自适应分层变换来实现各种属性的近无损压缩。对于非锚基元，每个基元都是基于k个最近的锚基元进行预测的。为了进一步最小化预测误差，将重建的LoD和锚基元组合在一起，形成新的锚基元，以预测下一个LoD。与小型场景数据集上最先进的压缩方法相比，我们的方法显著实现了卓越的压缩质量，数据大小大幅减少了4.5倍以上。 et.al.|[2411.06976](http://arxiv.org/abs/2411.06976)|null|
|**2024-11-10**|**Adaptive and Temporally Consistent Gaussian Surfels for Multi-view Dynamic Reconstruction**|3D高斯散点最近在动态场景的新颖视图合成和静态场景的几何重建方面取得了显著成功。在这些进步的基础上，通过全局优化整个序列，开发了用于动态表面重建的早期方法。然而，重建具有显著拓扑变化、出现或消失的物体以及快速运动的动态场景仍然是一个巨大的挑战，特别是对于长序列。为了解决这些问题，我们提出了AT-GS，这是一种通过每帧增量优化从多视图视频中重建高质量动态曲面的新方法。为了避免跨帧的局部最小值，我们引入了一种统一的自适应梯度感知致密化策略，该策略整合了传统克隆和分裂技术的优势。此外，我们通过确保连续帧中曲率图的一致性来减少动态曲面中的时间抖动。我们的方法在动态表面重建中实现了卓越的精度和时间相干性，即使在复杂和具有挑战性的场景中也能提供高保真的时空新颖视图合成。对不同多视图视频数据集的广泛实验证明了我们的方法的有效性，显示出比基线方法明显的优势。项目页面：\url{https://fraunhoferhhi.github.io/AT-GS} et.al.|[2411.06602](http://arxiv.org/abs/2411.06602)|null|
|**2024-11-12**|**SplatFormer: Point Transformer for Robust 3D Gaussian Splatting**|3D高斯散斑（3DGS）最近改变了真实感重建，实现了高视觉保真度和实时性能。然而，当测试视图偏离训练期间使用的相机角度时，渲染质量会显著下降，这对沉浸式自由视点渲染和导航的应用程序构成了重大挑战。在这项工作中，我们对3DGS和相关的新型视图合成方法在非分布（OOD）测试相机场景下进行了全面评估。通过使用合成和真实世界的数据集创建不同的测试用例，我们证明了大多数现有的方法，包括那些结合了各种正则化技术和数据驱动先验的方法，都难以有效地推广到面向对象的视图。为了解决这一局限性，我们引入了SplatFormer，这是第一个专门设计用于操作高斯斑点的点变换器模型。SplatFormer将在有限训练视图下优化的初始3DGS集作为输入，并在一次前向传递中对其进行细化，有效地消除了OOD测试视图中的潜在伪影。据我们所知，这是点变换器直接在3DGS集上的首次成功应用，超越了以前多场景训练方法的局限性，这些方法在推理过程中只能处理有限数量的输入视图。我们的模型显著提高了极端新颖视图下的渲染质量，在这些具有挑战性的场景中实现了最先进的性能，并优于各种3DGS正则化技术、为稀疏视图合成量身定制的多场景模型和基于扩散的框架。 et.al.|[2411.06390](http://arxiv.org/abs/2411.06390)|**[link](https://github.com/ChenYutongTHU/SplatFormer)**|
|**2024-11-10**|**Through the Curved Cover: Synthesizing Cover Aberrated Scenes with Refractive Field**|最近的扩展现实耳机和现场机器人已经采用了覆盖物来保护前置摄像头免受环境危害和坠落。盖子上的表面不规则性会导致光学像差，如模糊和非参数失真。NeRF和3D高斯散斑等新型视图合成方法不适合从具有光学像差的序列进行合成。为了应对这一挑战，我们引入了SynthCover，通过保护罩为下游扩展现实应用实现新颖的视图合成。SynthCover采用折射场来估计覆盖物的几何形状，从而能够对折射光线进行精确的分析计算。在合成场景和真实场景上的实验表明，我们的方法能够准确地模拟通过保护罩看到的场景，与现有方法相比，渲染质量有了显著提高。我们还表明，该模型可以很好地适应各种覆盖几何形状，并使用不同表面曲率的覆盖物捕获合成序列。为了推动对这一问题的进一步研究，我们提供了包含用保护罩光学像差捕获的真实和合成可步行场景的基准数据集。 et.al.|[2411.06365](http://arxiv.org/abs/2411.06365)|null|
|**2024-11-09**|**GaussianSpa: An "Optimizing-Sparsifying" Simplification Framework for Compact and High-Quality 3D Gaussian Splatting**|3D高斯散斑（3DGS）已成为新型视图合成的主流，利用高斯函数的连续聚合来模拟场景几何。然而，3DGS需要大量的内存来存储大量的高斯人，这阻碍了它的实用性。为了应对这一挑战，我们引入了GaussiansSpa，这是一个基于优化的简化框架，用于紧凑和高质量的3DGS。具体来说，我们将简化问题表述为与3DGS训练相关的优化问题。相应地，我们提出了一种高效的“优化稀疏”解决方案，交替解决两个独立的子问题，在训练过程中逐渐将强稀疏性强加到高斯算子上。我们对各种数据集的综合评估表明，GaussianSpa优于现有的最先进方法。值得注意的是，GaussianSpa在真实世界的深度混合数据集上实现了0.9 dB的平均PSNR改善，与普通3DGS相比，Gaussian减少了10倍。我们的项目页面可在https://gaussianspa.github.io/. et.al.|[2411.06019](http://arxiv.org/abs/2411.06019)|null|
|**2024-11-07**|**MVSplat360: Feed-Forward 360 Scene Synthesis from Sparse Views**|我们介绍MVSplat360，这是一种前馈方法，用于仅使用稀疏观测对不同现实世界场景进行360度新颖视图合成（NVS）。由于输入视图之间的最小重叠和提供的视觉信息不足，这种设置本身就不合适，这使得传统方法难以实现高质量的结果。我们的MVSplat360通过有效地将几何感知3D重建与时间一致的视频生成相结合来解决这个问题。具体来说，它重构了一个前馈的3D高斯散斑（3DGS）模型，将特征直接渲染到预训练的稳定视频扩散（SVD）模型的潜在空间中，然后这些特征作为姿态和视觉线索来指导去噪过程，并产生逼真的3D一致视图。我们的模型是端到端可训练的，支持用少至5个稀疏输入视图渲染任意视图。为了评估MVSplat360的性能，我们使用具有挑战性的DL3DV-10K数据集引入了一个新的基准，与最先进的方法相比，MVSplat36在宽扫甚至360度NVS任务中实现了卓越的视觉质量。在现有基准RealEstate10K上的实验也证实了我们模型的有效性。视频结果可在我们的项目页面上查看：https://donydchen.github.io/mvsplat360. et.al.|[2411.04924](http://arxiv.org/abs/2411.04924)|**[link](https://github.com/donydchen/mvsplat360)**|
|**2024-11-07**|**GANESH: Generalizable NeRF for Lensless Imaging**|无透镜成像通过消除传统笨重的透镜系统，为开发超紧凑型相机提供了重要机会。然而，如果没有聚焦元件，传感器的输出不再是直接图像，而是复杂的多路复用场景表示。传统方法试图通过采用可学习的反演和精化模型来解决这一挑战，但这些方法主要是为2D重建而设计的，不能很好地推广到3D重建。我们介绍了GANESH，这是一种新颖的框架，旨在实现多视图无透镜图像的同时细化和新颖的视图合成。与需要特定场景训练的现有方法不同，我们的方法支持即时推理，而无需对每个场景进行再训练。此外，我们的框架允许我们根据特定场景调整模型，从而提高渲染和细化质量。为了促进这一领域的研究，我们还提出了第一个多视图无透镜数据集LenslessScenes。大量实验表明，我们的方法在重建精度和细化质量方面优于当前的方法。代码和视频结果可在https://rakesh-123-cryp.github.io/Rakesh.github.io/ et.al.|[2411.04810](http://arxiv.org/abs/2411.04810)|null|
|**2024-11-06**|**Structure Consistent Gaussian Splatting with Matching Prior for Few-shot Novel View Synthesis**|尽管新型视图合成取得了实质性进展，但现有的方法，无论是基于神经辐射场（NeRF）还是最近的3D高斯散斑（3DGS），在输入变得稀疏时都会出现严重退化。人们已经做出了许多努力来缓解这个问题，但他们仍然难以有效地综合出令人满意的结果，特别是在大型场景中。本文提出了SCGaussian，这是一种使用匹配先验来学习3D一致场景结构的结构一致高斯散点方法。考虑到高斯属性的高度相互依赖性，我们在两个方面优化了场景结构：渲染几何体，更重要的是高斯基元的位置，由于非结构特性，高斯基元在普通3DGS中很难直接受到约束。为了实现这一点，我们提出了一种混合高斯表示法。除了普通的非结构高斯基元外，我们的模型还包括基于光线的高斯基元，这些基元绑定到匹配的光线上，其位置的优化沿光线受到限制。因此，我们可以利用匹配对应关系直接强制这些高斯基元的位置收敛到光线相交的表面点。在面向前方、周围和复杂的大型场景上进行的广泛实验表明，我们的方法具有最先进的性能和高效率。代码可在以下网址获得https://github.com/prstrive/SCGaussian. et.al.|[2411.03637](http://arxiv.org/abs/2411.03637)|**[link](https://github.com/prstrive/scgaussian)**|
|**2024-11-05**|**FewViewGS: Gaussian Splatting with Few View Matching and Multi-stage Training**|随着神经辐射场（NeRF）的引入，以及最近3D高斯散斑的引入，从图像合成新视图的领域得到了快速发展。高斯散斑因其高效性和准确渲染新视图的能力而被广泛采用。虽然高斯散斑在有足够数量的训练图像可用时表现良好，但其非结构化显式表示在输入图像稀疏的情况下往往会过拟合，导致渲染性能不佳。为了解决这个问题，我们提出了一种基于3D高斯的新颖视图合成方法，该方法使用稀疏输入图像，可以从训练图像未覆盖的视点准确地渲染场景。我们提出了一种多阶段训练方案，该方案对新视图施加了基于匹配的一致性约束，而不依赖于预训练的深度估计或扩散模型。这是通过使用可用训练图像的匹配来监督在具有颜色、几何和语义损失的训练帧之间采样的新视图的生成来实现的。此外，我们为3D高斯模型引入了一种局部保持正则化方法，通过保留场景的局部颜色结构来消除渲染伪影。对合成数据集和真实世界数据集的评估表明，与现有的最先进方法相比，我们的方法在少镜头新视图合成方面具有竞争力或优越的性能。 et.al.|[2411.02229](http://arxiv.org/abs/2411.02229)|null|
|**2024-11-03**|**InstantGeoAvatar: Effective Geometry and Appearance Modeling of Animatable Avatars from Monocular Video**|我们提出了InstantGeoAvatar，这是一种从单眼视频中高效学习可设置动画的隐式人类化身的详细3D几何和外观的方法。我们的关键观察是，优化哈希网格编码来表示人类受试者的有符号距离函数（SDF）充满了不稳定性和糟糕的局部最小值。因此，我们提出了一种有原则的几何感知SDF正则化方案，该方案无缝融入体绘制管道，并增加了可忽略的计算开销。我们的正则化方案明显优于之前在哈希网格上训练SDF的方法。我们在短短五分钟的训练时间内，在几何重建和新颖的视图合成方面取得了有竞争力的结果，与之前工作所需的几个小时相比，这是一个显著的减少。InstantGeoAvatar代表了实现虚拟化身交互式重建的重大飞跃。 et.al.|[2411.01512](http://arxiv.org/abs/2411.01512)|**[link](https://github.com/alvaro-budria/InstantGeoAvatar)**|

<p align=right>(<a href=#updated-on-20241113>back to top</a>)</p>

## 3D Reconstruction

|Publish Date|Title|Abstract|PDF|Code|
|---|---|---|---|---|
|**2024-11-12**|**Extreme Rotation Estimation in the Wild**|我们提出了一种技术和基准数据集，用于估计在极端环境中捕获的一对互联网图像之间的相对3D方向，其中图像具有有限或不重叠的视场。之前针对极端旋转估计的工作假设了受约束的3D环境，并通过从全景图中裁剪区域来模拟透视图像。然而，在野外拍摄的真实图像非常多样化，在外观和相机内部都表现出变化。在这项工作中，我们提出了一种基于Transformer的方法来估计极端现实环境中的相对旋转，并贡献了由场景级互联网照片集组装而成的ExtremeLandmarkPairs数据集。我们的评估表明，我们的方法成功地估计了各种极端视图互联网图像对中的相对旋转，优于各种基线，包括专用旋转估计技术和当代3D重建方法。 et.al.|[2411.07096](http://arxiv.org/abs/2411.07096)|null|
|**2024-11-11**|**AV-PedAware: Self-Supervised Audio-Visual Fusion for Dynamic Pedestrian Awareness**|在这项研究中，我们介绍了AV PedAware，这是一种自我监督的视听融合系统，旨在提高机器人应用中的动态行人感知能力。行人意识是许多机器人应用中的关键要求。然而，依赖相机和LIDAR覆盖多个视图的传统方法可能很昂贵，并且容易受到光照、遮挡和天气条件变化等问题的影响。我们提出的解决方案使用低成本的音频和视觉融合来复制人类对3D行人检测的感知。这项研究首次尝试利用视听融合来监测脚步声，以预测附近行人的运动。该系统通过基于激光雷达生成标签的自我监督学习进行训练，使其成为基于激光雷达的行人感知的经济高效的替代方案。AV PedAware以极低的成本实现了与基于激光雷达的系统相当的结果。通过利用注意力机制，它可以处理动态照明和遮挡，克服了传统激光雷达和基于相机的系统的局限性。为了评估我们的方法的有效性，我们收集了一个新的多模式行人检测数据集，并进行了实验，证明该系统即使在极端的视觉条件下，也能仅使用音频和视觉数据提供可靠的3D检测结果。我们将把收集到的数据集和源代码在线提供给社区，以鼓励机器人感知系统领域的进一步发展。 et.al.|[2411.06789](http://arxiv.org/abs/2411.06789)|null|
|**2024-11-10**|**Real-time Deformation-aware Control for Autonomous Robotic Subretinal Injection under iOCT Guidance**|机器人平台提供可重复和精确的工具定位，显著增强视网膜显微手术。这种系统与术中光学相干断层扫描（iOCT）的集成实现了图像引导的机器人干预，允许自主执行高级治疗可能性，例如将治疗剂注射到视网膜下腔。然而，在自主iOCT引导的机器人视网膜下注射中，由于工具-组织相互作用导致的组织变形是一个主要挑战，会影响正确的针头定位，从而影响手术的结果。本文提出了一种在iOCT引导下自主视网膜下注射的新方法，该方法考虑了插入过程中的组织变形。这是通过从密集采样的iOCT B扫描（我们称之为B5扫描）中实时分割和3D重建手术场景来实现的，以监测仪器相对于ILM和RPE之间相对位置处定义的虚拟目标层的定位。我们在离体猪眼睛上的实验表明，与之前的自主插入方法相比，插入深度的动态调整和针头定位的整体精度得到了提高。与之前方法生成视网膜下泡的成功率为35%相比，我们提出的方法在所有实验中都可靠、稳健地创建了视网膜下泡。 et.al.|[2411.06557](http://arxiv.org/abs/2411.06557)|null|
|**2024-11-10**|**A novel algorithm for optimizing bundle adjustment in image sequence alignment**|捆绑调整（BA）模型通常使用非线性最小二乘法进行优化，Levenberg-Marquardt（L-M）算法是典型的选择。然而，尽管L-M算法很有效，但当应用于条件较差的数据集时，它对初始条件的敏感性往往会导致收敛速度较慢，从而激发了对替代优化策略的探索。本文介绍了一种在低温电子断层成像图像序列比对背景下优化BA模型的新算法，该算法利用最优控制理论直接优化一般非线性函数。所提出的最优控制算法（OCA）表现出优异的收敛速度，并有效地缓解了L-M算法中经常观察到的振荡行为。对合成数据集和真实世界数据集进行了广泛的实验，以评估算法的性能。结果表明，与L-M算法相比，OCA实现了更快的收敛。此外，基于二分法的更新过程显著提高了OCA的性能，特别是在初始化不佳的数据集中。这些发现表明，OCA可以大大提高低温电子断层扫描中3D重建的效率。 et.al.|[2411.06343](http://arxiv.org/abs/2411.06343)|null|
|**2024-11-08**|**Benchmarking 3D multi-coil NC-PDNet MRI reconstruction**|深度学习在从欠采样数据中重建MRI方面显示出巨大的前景，但目前还缺乏对其在非笛卡尔欠采样的3D并行成像采集中的性能进行验证的研究。此外，伪影和由此产生的图像质量取决于欠采样模式。为了解决这一未知领域的问题，我们将非笛卡尔原始双网络（NC PDNet）扩展到3D多线圈设置，这是一种最先进的展开神经网络。我们评估了通道特定训练配置与通道无关训练配置的影响，并检查了线圈压缩的效果。最后，我们使用公开的卡尔加里坎皮纳斯数据集，对四种不同的非笛卡尔欠采样模式进行基准测试，加速因子为6。我们的结果表明，在具有不同输入通道数的压缩数据上训练的NC PDNet在1mm各向同性32通道全脑3D重建中实现了42.98 dB的平均PSNR。推理时间为4.95秒，GPU内存使用率为5.49 GB，我们的方法在临床研究应用中具有巨大的潜力。 et.al.|[2411.05883](http://arxiv.org/abs/2411.05883)|null|
|**2024-11-07**|**MVSplat360: Feed-Forward 360 Scene Synthesis from Sparse Views**|我们介绍MVSplat360，这是一种前馈方法，用于仅使用稀疏观测对不同现实世界场景进行360度新颖视图合成（NVS）。由于输入视图之间的最小重叠和提供的视觉信息不足，这种设置本身就不合适，这使得传统方法难以实现高质量的结果。我们的MVSplat360通过有效地将几何感知3D重建与时间一致的视频生成相结合来解决这个问题。具体来说，它重构了一个前馈的3D高斯散斑（3DGS）模型，将特征直接渲染到预训练的稳定视频扩散（SVD）模型的潜在空间中，然后这些特征作为姿态和视觉线索来指导去噪过程，并产生逼真的3D一致视图。我们的模型是端到端可训练的，支持用少至5个稀疏输入视图渲染任意视图。为了评估MVSplat360的性能，我们使用具有挑战性的DL3DV-10K数据集引入了一个新的基准，与最先进的方法相比，MVSplat36在宽扫甚至360度NVS任务中实现了卓越的视觉质量。在现有基准RealEstate10K上的实验也证实了我们模型的有效性。视频结果可在我们的项目页面上查看：https://donydchen.github.io/mvsplat360. et.al.|[2411.04924](http://arxiv.org/abs/2411.04924)|**[link](https://github.com/donydchen/mvsplat360)**|
|**2024-11-07**|**Differentiable Gaussian Representation for Incomplete CT Reconstruction**|不完全计算机断层扫描（CT）通过减少辐射暴露使患者受益。然而，由于问题的不适定性质，从有限的视图或角度重建高保真图像仍然具有挑战性。深度学习重建（DLR）方法在提高图像质量方面显示出了希望，但训练数据多样性和高泛化能力之间的悖论仍未得到解决。在这篇论文中，我们提出了一种新的不完全CT重建的高斯表示法（GRCT），无需使用任何神经网络或全剂量CT数据。具体来说，我们将3D体积建模为一组可学习的高斯分布，这些高斯分布直接从不完整的正弦图中优化。我们的方法可以应用于多个视图和角度，而无需改变架构。此外，我们提出了一种可区分的快速CT重建方法，以实现高效的临床应用。在多个数据集和设置上进行的广泛实验表明，重建质量指标和效率有了显著提高。我们计划以开源的形式发布我们的代码。 et.al.|[2411.04844](http://arxiv.org/abs/2411.04844)|null|
|**2024-11-07**|**GANESH: Generalizable NeRF for Lensless Imaging**|无透镜成像通过消除传统笨重的透镜系统，为开发超紧凑型相机提供了重要机会。然而，如果没有聚焦元件，传感器的输出不再是直接图像，而是复杂的多路复用场景表示。传统方法试图通过采用可学习的反演和精化模型来解决这一挑战，但这些方法主要是为2D重建而设计的，不能很好地推广到3D重建。我们介绍了GANESH，这是一种新颖的框架，旨在实现多视图无透镜图像的同时细化和新颖的视图合成。与需要特定场景训练的现有方法不同，我们的方法支持即时推理，而无需对每个场景进行再训练。此外，我们的框架允许我们根据特定场景调整模型，从而提高渲染和细化质量。为了促进这一领域的研究，我们还提出了第一个多视图无透镜数据集LenslessScenes。大量实验表明，我们的方法在重建精度和细化质量方面优于当前的方法。代码和视频结果可在https://rakesh-123-cryp.github.io/Rakesh.github.io/ et.al.|[2411.04810](http://arxiv.org/abs/2411.04810)|null|
|**2024-11-07**|**Enhancing Bronchoscopy Depth Estimation through Synthetic-to-Real Domain Adaptation**|单眼深度估计在一般成像任务中显示出希望，有助于定位和3D重建。虽然在各个领域都很有效，但由于缺乏标记数据，它在支气管镜图像中的应用受到阻碍，这对监督学习方法的使用提出了挑战。在这项工作中，我们提出了一种迁移学习框架，该框架利用具有深度标签的合成数据进行训练，并调整领域知识以在真实支气管镜数据中进行准确的深度估计。与仅在合成数据上进行训练相比，我们的网络使用域自适应对真实镜头进行了改进的深度预测，验证了我们的方法。 et.al.|[2411.04404](http://arxiv.org/abs/2411.04404)|null|
|**2024-11-06**|**These Maps Are Made by Propagation: Adapting Deep Stereo Networks to Road Scenarios with Decisive Disparity Diffusion**|立体匹配已成为路面3D重建的一种经济高效的解决方案，在提高计算效率和准确性方面受到了广泛关注。本文介绍了决定性视差扩散（D3Stereo），标志着对密集深度特征匹配的首次探索，该匹配将预训练的深度卷积神经网络（DCNN）应用于以前看不见的道路场景。成本量金字塔最初是使用不同层次的学习表示创建的。随后，采用了一种新的递归双边滤波算法来聚合这些成本。D3Stereo的一个关键创新在于其交替的决定性视差扩散策略，其中采用尺度内扩散来完成稀疏视差图像，而尺度间继承为更高分辨率提供了有价值的先验信息。在我们创建的UDTIRI立体和立体道路数据集上进行的广泛实验强调了D3Stereo策略在适应预训练DCNN方面的有效性，以及与专门为路面3D重建设计的所有其他基于显式编程的算法相比的卓越性能。在Middlebury数据集上进行的额外实验，以及在ImageNet数据库上预训练的骨干DCNN，进一步验证了D3Stereo策略在解决一般立体匹配问题方面的多功能性。 et.al.|[2411.03717](http://arxiv.org/abs/2411.03717)|null|

<p align=right>(<a href=#updated-on-20241113>back to top</a>)</p>

## Diffusion

|Publish Date|Title|Abstract|PDF|Code|
|---|---|---|---|---|
|**2024-11-11**|**Score-based generative diffusion with "active" correlated noise sources**|扩散模型通过近似数据集的底层分布并通过从近似分布中采样来合成数据，展现出稳健的生成特性。在这项工作中，我们探索了如果在正向过程中使用具有时间相关性的噪声源（类似于活性物质领域使用的噪声源）来破坏数据，如何调节生成性能。我们的数值和分析实验表明，相应的逆向过程可能表现出更好的生成特性。 et.al.|[2411.07233](http://arxiv.org/abs/2411.07233)|null|
|**2024-11-12**|**Add-it: Training-Free Object Insertion in Images With Pretrained Diffusion Models**|在语义图像编辑中，基于文本指令将对象添加到图像中是一项具有挑战性的任务，需要在保留原始场景和将新对象无缝集成到合适的位置之间取得平衡。尽管付出了巨大的努力，但现有的模型往往难以实现这种平衡，特别是在复杂场景中寻找添加对象的自然位置。我们介绍了Add-it，这是一种无需训练的方法，它扩展了扩散模型的注意力机制，以整合来自三个关键来源的信息：场景图像、文本提示和生成的图像本身。我们的加权扩展注意力机制在确保自然物体放置的同时，保持了结构的一致性和精细的细节。无需特定任务的微调，Add-it在真实和生成的图像插入基准上都取得了最先进的结果，包括我们新构建的“Additing Affordance Benchmark”，用于评估对象放置的合理性，优于监督方法。人工评估表明，在80%以上的情况下，Add it是首选，它还展示了各种自动化指标的改进。 et.al.|[2411.07232](http://arxiv.org/abs/2411.07232)|null|
|**2024-11-11**|**DLCR: A Generative Data Expansion Framework via Diffusion for Clothes-Changing Person Re-ID**|随着生成扩散模型最近表现出的优势，一个悬而未决的研究问题是\textit{这些模型生成的图像是否可用于学习更好的视觉表示}。虽然这种生成数据扩展可能足以完成更简单的视觉任务，但我们探索了它在更困难的辨别任务上的功效：换衣服的人重新识别（CC ReID）。CC ReID旨在匹配出现在非重叠相机中的人，即使他们在相机间换衣服。当前的CC ReID模型不仅受到当前CC ReID数据集中服装多样性有限的限制，而且生成保留重要个人特征的额外数据以进行准确识别是当前的挑战。为了解决这个问题，我们提出了DLCR，这是一种新的数据扩展框架，它利用预训练的扩散和大型语言模型（LLM）来准确生成穿着不同服装的个人的不同图像。我们为五个基准CC ReID数据集（PRCC、CCVID、LaST、VC Clothes和LTCC）生成了额外的数据，\textbf{将他们的服装多样性增加了\boldmath{10 $}x，总共生成了超过\boldmath{210$ }万张图像}。DLCR采用基于扩散的文本引导修复，以使用LLM构建的服装提示为条件，生成仅修改受试者服装的合成数据，同时保留其个人身份特征。随着数据的大量增加，我们引入了两种新策略——渐进学习和测试时间预测细化——分别减少了训练时间，进一步提高了CC ReID的性能。在PRCC数据集上，我们通过使用DLCR生成的数据训练CAL（一种先前的最新技术（SOTA）方法），获得了11.3%的前1名准确率的大幅提高。我们在这里公开发布我们的代码并为每个数据集生成数据：\url{https://github.com/CroitoruAlin/dlcr}. et.al.|[2411.07205](http://arxiv.org/abs/2411.07205)|**[link](https://github.com/croitorualin/dlcr)**|
|**2024-11-11**|**Crossover from inhomogeneous to homogeneous response of a resonantly driven hBN quantum emitter**|我们实验研究了一种固态量子发射器——六方氮化硼（hBN）中的B中心——在短时间内具有寿命有限的相干性，在较长时间内由于光谱扩散而经历不均匀展宽。通过利用共振激光激发中的功率展宽，我们探索了非均匀和均匀展宽区域之间的交叉。在数值模拟的支持下，我们表明线形、计数率、二阶相关性和长时间光子统计从由光谱扩散决定的状态演变为仅由发射器的均匀响应给出的状态，从而得到恢复的洛伦兹形状和泊松光子统计。计数率和线宽的饱和不是在拉比振荡开始时发生的，而是在功率加宽的均匀响应与非均匀线宽相当时发生的。此外，我们在二阶相关性和长时间光子统计中识别出了特定的特征，这些特征可以用基于微米到毫秒时间尺度离散跳跃的微观光谱扩散模型很好地解释。我们的工作对共振激发下B中心的光物理进行了广泛的描述，并且可以很容易地扩展到各种固态量子发射器。 et.al.|[2411.07202](http://arxiv.org/abs/2411.07202)|null|
|**2024-11-11**|**OmniEdit: Building Image Editing Generalist Models Through Specialist Supervision**|通过在自动合成或手动注释的图像编辑对上训练扩散模型，指令引导的图像编辑方法已经显示出巨大的潜力。然而，这些方法离实际的、现实生活中的应用还很远。我们确定了造成这一差距的三个主要挑战。首先，由于有偏见的合成过程，现有模型的编辑技能有限。其次，这些方法使用具有大量噪声和伪影的数据集进行训练。这是由于应用了简单的过滤方法，如CLIP评分。第三，所有这些数据集都局限于单一的低分辨率和固定纵横比，限制了处理现实世界用例的多功能性。本文介绍了omniedit，这是一个全能的编辑器，可以无缝处理任何宽高比的七种不同图像编辑任务。我们的贡献有四方面：（1）通过利用七种不同专业模型的监督来培训omniedit，以确保任务覆盖率。（2） 我们利用基于大型多模态模型（如GPT-4o）提供的分数而不是CLIP分数的重要性抽样来提高数据质量。（3） 我们提出了一种名为EditNet的新编辑架构，以大大提高编辑成功率，（4）我们提供了不同宽高比的图像，以确保我们的模型可以处理任何野外图像。我们策划了一个测试集，其中包含不同纵横比的图像，并附有涵盖不同任务的不同说明。自动评估和人工评估都表明，omniedit可以显著优于所有现有模型。我们的代码、数据集和模型将在\url上提供{https://tiger-ai-lab.github.io/OmniEdit/} et.al.|[2411.07199](http://arxiv.org/abs/2411.07199)|null|
|**2024-11-11**|**Lifetime-Limited and Tunable Emission from Charge-Stabilized Nickel Vacancy Centers in Diamond**|金刚石中带负电荷的镍空位中心（NiV $^-$）是一种有前景的自旋量子比特候选者，具有预测的反转对称性、大的基态自旋轨道分裂以限制声子诱导的退相干和近红外发射。在这里，我们通过磁光光谱实验证实了所提出的NiV缺陷的几何和电子结构。我们对光学性质进行了表征，发现德拜-沃勒因子为0.62。此外，我们在所有金刚石p-i-p结中使用电偏压来设计电荷状态稳定的缺陷。我们测量了一个消失的静态偶极矩，并且没有光谱扩散，这是反演对称性的特征。在偏压下，我们观察到稳定的跃迁，其寿命限制线宽窄至16MHz，并通过二阶斯塔克位移对发射进行方便的频率调谐。总的来说，这项工作为NiV$^-$ 的相干控制及其作为自旋量子比特的使用提供了一条途径，并有助于更全面地理解金刚石缺陷所经历的电荷动力学。 et.al.|[2411.07196](http://arxiv.org/abs/2411.07196)|null|
|**2024-11-11**|**More Expressive Attention with Negative Weights**|我们提出了一种新的注意力机制，称为Cog attention，它使注意力权重为负以增强表现力，这源于两个关键因素：（1）Cog Attntion可以将令牌删除和复制功能从静态OV矩阵转移到动态QK内积，OV矩阵现在更侧重于细化或修改。注意力负责人可以通过分别分配负、正或最小注意力权重来同时删除、复制或保留标记。因此，单个注意力头变得更加灵活和富有表现力。（2） Cog Attention提高了模型对表征崩溃的鲁棒性，当早期的表征被过度压缩到后期的位置时，就会发生表征崩溃，导致同质表征。负权重减少了从早期到后期令牌的有效信息路径，有助于缓解这一问题。我们开发了使用Cog Attention作为注意力模块的Transformer类模型，包括用于语言建模的仅解码器模型和用于图像生成的U-ViT扩散模型。实验表明，与采用传统softmax注意力模块的模型相比，使用Cog Attention的模型表现出更优的性能。我们的方法为重新思考和打破传统softmax注意力的根深蒂固的限制提供了一个有前景的研究方向，例如对非负权重的要求。 et.al.|[2411.07176](http://arxiv.org/abs/2411.07176)|**[link](https://github.com/trestad/cogattn)**|
|**2024-11-11**|**Edify 3D: Scalable High-Quality 3D Asset Generation**|我们介绍Edify 3D，这是一种专为高质量3D资产生成而设计的高级解决方案。我们的方法首先使用扩散模型在多个视点合成所描述对象的RGB和表面法线图像。然后，使用多视图观测来重建对象的形状、纹理和PBR材质。我们的方法可以在运行时间的2分钟内生成具有详细几何形状、干净形状拓扑、高分辨率纹理和材质的高质量3D资产。 et.al.|[2411.07135](http://arxiv.org/abs/2411.07135)|null|
|**2024-11-11**|**Zero-sum Dynkin games under common and independent Poisson constraints**|泊松约束下的零和Dynkin博弈在最近的文献中得到了广泛的研究。在这种游戏中，玩家只允许在泊松过程的事件时间停止。约束可以用两种不同的方式建模：要么两个参与者共享相同的泊松过程（共同约束），要么每个参与者都有自己的泊松过程。在马尔可夫情况下，收益由潜在扩散的一对函数给出，我们给出了充分条件，在这些条件下，公共（分别独立）约束下的博弈解（价值函数和每个玩家的最优停止集）也是独立（分别共同）约束下博弈的解。粗略地说，如果在公共约束下博弈中最大化器和最小化器的停止集是不相交的，那么在公共约束和独立约束下，博弈的解是相同的。然而，在独立约束下的博弈中，停止集不相交的事实不足以保证独立约束下博弈的解也是公共约束下的解。 et.al.|[2411.07134](http://arxiv.org/abs/2411.07134)|null|
|**2024-11-11**|**Edify Image: High-Quality Image Generation with Pixel Space Laplacian Diffusion Models**|我们介绍了Edify Image，这是一个能够以像素完美精度生成逼真图像内容的扩散模型家族。Edify Image利用级联像素空间扩散模型，该模型使用新的拉普拉斯扩散过程训练，其中不同频带的图像信号以不同的速率衰减。Edify Image支持广泛的应用程序，包括文本到图像合成、4K上采样、ControlNets、360 HDR全景生成以及图像定制的微调。 et.al.|[2411.07126](http://arxiv.org/abs/2411.07126)|null|

<p align=right>(<a href=#updated-on-20241113>back to top</a>)</p>

## NeRF

|Publish Date|Title|Abstract|PDF|Code|
|---|---|---|---|---|
|**2024-11-09**|**Epi-NAF: Enhancing Neural Attenuation Fields for Limited-Angle CT with Epipolar Consistency Conditions**|神经场方法最初在逆渲染领域取得了成功，最近已扩展到CT重建，标志着传统技术的范式转变。虽然这些方法在稀疏视图CT重建中提供了最先进的结果，但它们在有限的角度设置中很难实现，在有限的视角范围内捕获输入投影。我们提出了一种基于X射线投影图像中相应极线之间一致性条件的新损失项，旨在规范神经衰减场优化。通过强制执行这些一致性条件，我们的方法Epi NAF将监督从有限角度范围内的输入视图传播到整个锥束CT范围内的预测投影。与基线方法相比，这种损失导致重建的定性和定量改进。 et.al.|[2411.06181](http://arxiv.org/abs/2411.06181)|null|
|**2024-11-07**|**LoFi: Scalable Local Image Reconstruction with Implicit Neural Representation**|神经场或隐式神经表示（INR）因其对图像和3D体积的有效连续表示而在机器学习和信号处理中引起了广泛关注。在这项工作中，我们以INR为基础，引入了一种基于坐标的局部处理框架来解决成像逆问题，称为LoFi（局部场）。与传统的图像重建方法不同，LoFi通过多层感知器（MLP）分别处理每个坐标处的局部信息，在该特定坐标处恢复对象。与INR类似，LoFi可以在任何连续坐标下恢复图像，从而实现多分辨率的图像重建。LoFi在图像重建方面的性能与标准CNN相当或更好，几乎与图像分辨率无关，对分布外数据和内存使用具有出色的泛化能力。值得注意的是，对1024美元×1024美元的图像进行训练只需要3GB的内存，比标准CNN通常需要的内存少20多倍。此外，LoFi的局部设计允许它在小于10个样本的极小数据集上进行训练，而不会过拟合或需要正则化或提前停止。最后，我们使用LoFi作为即插即用框架中的去噪先验，用于解决一般的逆问题，以受益于其连续的图像表示和强大的泛化能力。尽管在低分辨率图像上进行了训练，但LoFi可以用作低维先验，以解决任何分辨率的逆问题。我们通过各种成像方式验证了我们的框架，从低剂量计算机断层扫描到无线电干涉成像。 et.al.|[2411.04995](http://arxiv.org/abs/2411.04995)|null|
|**2024-11-04**|**Physically Based Neural Bidirectional Reflectance Distribution Function**|我们介绍了基于物理的神经双向反射分布函数（PBNBRDF），这是一种基于神经场的材料外观的新颖连续表示。我们的模型准确地重建了真实世界的材料，同时独特地增强了现实BRDF的物理特性，特别是通过重新参数化的亥姆霍兹互易性和通过高效分析积分的能量无源性。我们进行了系统分析，证明了遵守这些物理定律对重建材料的视觉质量的好处。此外，我们通过引入色度强制监督RGB通道的规范来提高神经BRDF的颜色精度。通过在多个测量的真实BRDF数据库上进行定性和定量实验，我们表明，遵守这些物理约束可以使神经场更忠实、更稳定地表示原始数据，并实现更高的渲染质量。 et.al.|[2411.02347](http://arxiv.org/abs/2411.02347)|null|
|**2024-11-01**|**Intensity Field Decomposition for Tissue-Guided Neural Tomography**|锥束计算机断层扫描（CBCT）通常需要数百次X射线投影，这引起了人们对辐射暴露的担忧。虽然稀疏视图重建通过使用更少的投影来减少曝光，但它很难达到令人满意的图像质量。为了应对这一挑战，本文介绍了一种新的稀疏视图CBCT重建方法，该方法为神经场赋予了人体组织正则化的能力。我们的方法被称为组织引导神经断层扫描（TNT），其动机是CBCT中骨骼和软组织之间明显的强度差异。直观地说，分离这些成分可能有助于神经场的学习过程。更确切地说，TNT包括一个异构的四重网络和相应的训练策略。该网络将强度场表示为软组织和硬组织成分及其各自纹理的组合。我们在估计的组织投影的指导下训练网络，从而能够有效地学习网络头所需的模式。大量实验表明，所提出的方法显著改善了稀疏视图CBCT重建，投影数量从10到60不等。与最先进的基于神经渲染的方法相比，我们的方法以更少的投影和更快的收敛实现了相当的重建质量。 et.al.|[2411.00900](http://arxiv.org/abs/2411.00900)|null|
|**2024-10-26**|**Neural Fields in Robotics: A Survey**|神经场已经成为计算机视觉和机器人技术中3D场景表示的一种变革性方法，能够从姿势的2D数据中准确推断几何、3D语义和动力学。利用可微分渲染，神经场包括连续隐式和显式神经表示，实现了高保真3D重建、多模态传感器数据的集成和新视点的生成。这项调查探讨了它们在机器人技术中的应用，强调了它们在增强感知、规划和控制方面的潜力。它们的紧凑性、内存效率和可微性，以及与基础模型和生成模型的无缝集成，使其成为实时应用的理想选择，提高了机器人的适应性和决策能力。本文基于200多篇论文，对机器人中的神经场进行了全面的回顾，对各个领域的应用进行了分类，并评估了它们的优势和局限性。首先，我们介绍了四个关键的神经场框架：占用网络、有符号距离场、神经辐射场和高斯散斑。其次，我们详细介绍了神经场在五个主要机器人领域的应用：姿态估计、操纵、导航、物理和自动驾驶，重点介绍了关键工作，并讨论了要点和公开挑战。最后，我们概述了神经场在机器人技术中的局限性，并为未来的研究提出了有前景的方向。项目页面：https://robonerf.github.io et.al.|[2410.20220](http://arxiv.org/abs/2410.20220)|**[link](https://github.com/zubair-irshad/Awesome-Implicit-NeRF-Robotics)**|
|**2024-10-24**|**3D-Adapter: Geometry-Consistent Multi-View Diffusion for High-Quality 3D Generation**|多视图图像扩散模型显著推进了开放域3D对象生成。然而，大多数现有模型依赖于缺乏固有3D偏差的2D网络架构，导致几何一致性受损。为了应对这一挑战，我们引入了3D Adapter，这是一个插件模块，旨在将3D几何感知注入预训练的图像扩散模型中。我们方法的核心是3D反馈增强的思想：对于采样循环中的每个去噪步骤，3D Adapter将中间的多视图特征解码为连贯的3D表示，然后对渲染的RGBD视图进行重新编码，通过特征添加来增强预训练的基础模型。我们研究了3D Adapter的两种变体：一种是基于高斯飞溅的快速前馈版本，另一种是利用神经场和网格的通用无训练版本。我们广泛的实验表明，3D Adapter不仅大大提高了文本到多视图模型（如Instant3D和Zero123++）的几何质量，而且还使用纯文本到图像的稳定扩散实现了高质量的3D生成。此外，我们通过在文本到3D、图像到3D、文本到纹理和文本到化身任务中呈现高质量的结果，展示了3D适配器的广泛应用潜力。 et.al.|[2410.18974](http://arxiv.org/abs/2410.18974)|**[link](https://github.com/Lakonik/MVEdit)**|
|**2024-10-22**|**Cortical Dynamics of Neural-Connectivity Fields**|皮质组织的宏观研究揭示了振荡活动的普遍性，这反映了神经相互作用的微调。本研究通过将广义振荡动力学纳入先前关于保守或半保守神经场动力学的工作中，扩展了神经场理论。先前的研究在很大程度上假设了神经单元之间的各向同性连接；然而，这项研究表明，广泛的各向异性和波动连接仍然可以维持振荡。使用拉格朗日场方法，我们研究了不同类型的连接、它们的动力学以及与神经场的潜在相互作用。基于这一理论基础，我们推导出了一个框架，该框架通过连接场的概念将Hebbian和非Hebbian学习（即可塑性）纳入神经场的研究中。 et.al.|[2410.16852](http://arxiv.org/abs/2410.16852)|null|
|**2024-10-15**|**Deep vectorised operators for pulsatile hemodynamics estimation in coronary arteries from a steady-state prior**|心血管血流动力学场为冠状动脉疾病提供了有价值的医学决策标志。计算流体动力学（CFD）是体内准确、无创评估这些量的金标准。在这项工作中，我们提出了一种基于机器学习的时间高效替代模型，用于基于稳态先验估计脉动血流动力学。我们引入了深度矢量化算子，这是一种用于在无限维函数空间上进行离散化独立学习的建模框架。基础神经结构是一个以血流动力学边界条件为条件的神经场。重要的是，我们展示了如何将逐点动作的要求放宽到置换等变，从而产生一系列可以通过消息传递和自我关注层进行参数化的模型。我们在从冠状动脉计算机断层扫描血管造影（CCTA）中提取的74条狭窄冠状动脉的数据集上评估了我们的方法，并将患者特异性脉动CFD模拟作为基本事实。我们证明，我们的模型能够准确估计脉动速度和压力，同时不受源域重新采样的影响（离散化独立性）。这表明，深度矢量化算子是冠状动脉及其他动脉心血管血流动力学估计的强大建模工具。 et.al.|[2410.11920](http://arxiv.org/abs/2410.11920)|null|
|**2024-10-07**|**Fast Training of Sinusoidal Neural Fields via Scaling Initialization**|神经场是一种新兴的范式，它将数据表示为由神经网络参数化的连续函数。尽管有许多优点，但神经场通常具有较高的训练成本，这阻碍了更广泛的采用。在本文中，我们关注一个流行的神经场家族，称为正弦神经场（SNF），并研究如何初始化它以最大限度地提高训练速度。我们发现，基于信号传播原理设计的SNF标准初始化方案是次优的。特别是，我们证明，通过简单地将每个权重（最后一层除外）乘以一个常数，我们可以将SNF训练加速10 $\times$。这种方法被称为$\textit{weight scaling}$ ，在各种数据域上持续提供显著的加速，使SNF的训练速度比最近提出的架构更快。为了理解为什么权重缩放效果良好，我们进行了广泛的理论和实证分析，结果表明，权重缩放不仅有效地解决了频谱偏差，而且具有良好的优化轨迹。 et.al.|[2410.04779](http://arxiv.org/abs/2410.04779)|null|
|**2024-10-04**|**End-to-End Reaction Field Energy Modeling via Deep Learning based Voxel-to-voxel Transform**|在计算生物化学和生物物理学中，理解静电相互作用的作用对于阐明生物分子的结构、动力学和功能至关重要。泊松-玻尔兹曼（PB）方程是通过描述带电分子内部和周围的静电势来模拟这些相互作用的基础工具。然而，由于生物分子表面的复杂性和需要考虑可移动离子，求解PB方程带来了重大的计算挑战。虽然求解PB方程的传统数值方法是准确的，但它们的计算成本很高，并且随着系统规模的增加而扩展性较差。为了应对这些挑战，我们引入了PBNeF，这是一种新的机器学习方法，灵感来自基于神经网络的偏微分方程求解器的最新进展。我们的方法将PB方程的输入和边界静电条件转化为可学习的体素表示，使神经场变换器能够预测PB解，进而预测反应场势能。大量实验表明，与传统的PB求解器相比，PBNeF的速度提高了100倍以上，同时保持了与广义玻恩（GB）模型相当的精度。 et.al.|[2410.03927](http://arxiv.org/abs/2410.03927)|null|

<p align=right>(<a href=#updated-on-20241113>back to top</a>)</p>

[contributors-shield]: https://img.shields.io/github/contributors/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[contributors-url]: https://github.com/Vincentqyw/cv-arxiv-daily/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[forks-url]: https://github.com/Vincentqyw/cv-arxiv-daily/network/members
[stars-shield]: https://img.shields.io/github/stars/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[stars-url]: https://github.com/Vincentqyw/cv-arxiv-daily/stargazers
[issues-shield]: https://img.shields.io/github/issues/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[issues-url]: https://github.com/Vincentqyw/cv-arxiv-daily/issues

