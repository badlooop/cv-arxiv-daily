[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]

## Updated on 2023.09.05
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
|**2023-08-24**|**Improving NeRF Quality by Progressive Camera Placement for Unrestricted Navigation in Complex Environments**|神经辐射场（NeRF）极大地改进了用于渲染的新型视图合成和3D重建。NeRF在以对象为中心的重建方面取得了令人印象深刻的结果，但在复杂环境（房间、房屋等）中使用自由视点导航的新颖视图合成的质量往往存在问题。虽然算法改进对新视图合成的质量起着重要作用，但在这项工作中，我们表明，由于优化NeRF本质上是一个数据驱动的过程，因此高质量的数据对重建的最终质量起着根本作用。因此，关键是要选择数据样本——在这种情况下是相机——以最终使优化收敛到一个允许高质量自由视点导航的解决方案。我们的主要贡献是一种算法，该算法有效地提出了新的相机位置，可以在最小的假设下提高视觉质量。我们的解决方案可以用于任何NeRF模型，并且优于基线和类似工作。 et.al.|[2309.00014](http://arxiv.org/abs/2309.00014)|null|
|**2023-08-29**|**Pose-Free Neural Radiance Fields via Implicit Pose Regularization**|无姿态神经辐射场（NeRF）旨在用未经处理的多视图图像训练NeRF，近年来取得了令人印象深刻的成功。大多数现有工作共享一个管道，首先用渲染图像训练粗略的姿态估计器，然后联合优化估计的姿态和神经辐射场。然而，由于姿态估计器仅用渲染图像进行训练，由于真实图像和渲染图像之间的域间隙，姿态估计通常对真实图像有偏差或不准确，导致真实图像的姿态估计鲁棒性差，并且在联合优化中存在进一步的局部最小值。我们设计了IR NeRF，这是一种创新的无姿态NeRF，它引入了隐式姿态正则化来改进未聚焦真实图像的姿态估计器，并提高了真实图像姿态估计的鲁棒性。通过特定场景的2D图像的集合，IR NeRF构建了一个场景码本，该场景码本存储场景特征，并隐式地捕捉特定场景的姿势分布作为先验。因此，根据只有当2D真实图像的估计姿势位于姿势分布内时才可以从场景码本很好地重建2D真实图像这一原理，可以利用场景先验来提高姿势估计的鲁棒性。大量实验表明，IR NeRF实现了卓越的新视图合成，并在多个合成和真实数据集上始终优于最先进的视图合成。 et.al.|[2308.15049](http://arxiv.org/abs/2308.15049)|null|
|**2023-08-28**|**CLNeRF: Continual Learning Meets NeRF**|新颖的视图合成旨在呈现给定一组校准图像的看不见的视图。在实际应用中，场景的覆盖范围、外观或几何结构可能会随着时间的推移而变化，不断捕捉新的图像。有效地整合这种持续的变化是一个公开的挑战。标准NeRF基准测试仅涉及场景覆盖范围的扩展。为了研究其他实际的场景变化，我们提出了一个新的数据集，即跨时间世界（WAT），由外观和几何结构随时间变化的场景组成。我们还提出了一种简单而有效的方法CLNeRF，它将连续学习（CL）引入到神经辐射场（NeRF）中。CLNeRF结合了生成回放和即时神经图形原件（NGP）架构，以有效防止灾难性遗忘，并在新数据到达时有效更新模型。我们还向NGP添加了可训练的外观和几何嵌入，允许单个紧凑模型处理复杂的场景变化。在不需要存储历史图像的情况下，在变化场景的多次扫描上顺序训练的CLNeRF与在一次所有扫描上训练的上界模型性能相当。与其他CL基线相比，CLNeRF在标准基准和WAT上的表现要好得多。源代码和WAT数据集可在https://github.com/IntelLabs/CLNeRF.视频演示可在以下网址获得：https://youtu.be/nLRt6OoDGq0?si=8yD6k-8MMBJInQP et.al.|[2308.14816](http://arxiv.org/abs/2308.14816)|**[link](https://github.com/intellabs/clnerf)**|
|**2023-08-28**|**Flexible Techniques for Differentiable Rendering with 3D Gaussians**|快速、可靠的形状重建是许多计算机视觉应用中的重要组成部分。Neural Radiance Fields证明，真实感的新视图合成是触手可及的，但受到真实场景和对象快速重建性能要求的限制。最近的一些方法建立在替代形状表示的基础上，特别是3D高斯。我们开发了这些渲染器的扩展，例如集成可微分光流、导出防水网格和渲染每光线法线。此外，我们还展示了最近的两种方法是如何相互操作的。这些重建快速、稳健，并且可以在GPU或CPU上轻松执行。有关代码和可视化示例，请参见https://leonidk.github.io/fmb-plus et.al.|[2308.14737](http://arxiv.org/abs/2308.14737)|null|
|**2023-08-27**|**Depth self-supervision for single image novel view synthesis**|在本文中，我们解决了在给定单个帧作为输入的情况下从任意视点生成新图像的问题。虽然在这种设置中操作的现有方法旨在预测目标视图深度图以指导合成，但在没有明确监督此类任务的情况下，我们共同优化了新视图合成和深度估计的框架，以最大限度地释放两者之间的协同作用。具体地，以自监督的方式训练共享深度解码器，以预测在源视图和目标视图中一致的深度图。我们的结果证明了我们的方法在解决这两项任务的挑战方面的有效性，这两项工作允许生成更高质量的图像，并为目标视点提供更准确的深度。 et.al.|[2308.14108](http://arxiv.org/abs/2308.14108)|**[link](https://github.com/johnminelli/twowaysynth)**|
|**2023-08-27**|**Sparse3D: Distilling Multiview-Consistent Diffusion for Object Reconstruction from Sparse Views**|从极其稀疏的视图重建3D对象是一个长期存在且具有挑战性的问题。虽然最近的技术使用图像扩散模型来在新视点生成看似合理的图像，或者使用分数蒸馏采样（SDS）将预先训练的扩散先验提取到3D表示中，但这些方法通常难以同时实现新视点合成（NVS）和几何体的高质量、一致和详细的结果。在这项工作中，我们提出了Sparse3D，这是一种为稀疏视图输入量身定制的新型3D重建方法。我们的方法从多视点一致扩散模型中提取鲁棒先验，以细化神经辐射场。具体来说，我们使用了一个控制器，该控制器利用输入视图中的核线特征，引导预先训练的扩散模型，如稳定扩散，以生成与输入保持3D一致性的新视图图像。通过利用强大的图像扩散模型中的2D先验，我们的集成模型即使在面对开放世界对象时也能始终如一地提供高质量的结果。为了解决传统SDS引入的模糊性，我们引入了类别分数蒸馏采样（C-SDS）来增强细节。我们在CO3DV2上进行了实验，这是一个真实世界对象的多视图数据集。定量和定性评估都表明，我们的方法在NVS和几何重建方面优于以往最先进的工作。 et.al.|[2308.14078](http://arxiv.org/abs/2308.14078)|null|
|**2023-08-24**|**NeO 360: Neural Fields for Sparse View Synthesis of Outdoor Scenes**|最近的隐式神经表示在新的视图合成中显示出了很好的结果。然而，现有的方法需要从许多视图进行昂贵的每场景优化，因此限制了它们在真实世界的无边界城市环境中的应用，在这些环境中，从极少数视图观察到感兴趣的对象或背景。为了缓解这一挑战，我们引入了一种名为NeO360的新方法，用于户外场景稀疏视图合成的神经场。NeO 360是一种可推广的方法，它从单个或几个摆出姿势的RGB图像重建360｛\deg｝场景。我们方法的本质是捕捉复杂的真实世界户外3D场景的分布，并使用可以从任何世界点查询的混合图像条件三平面表示。我们的表示结合了基于体素和鸟瞰图（BEV）的最佳表示，比每种表示都更有效、更具表现力。NeO 360的表示使我们能够从大量无界3D场景中学习，同时在推理过程中从一张图像中提供对新视图和新场景的可推广性。我们在所提出的具有挑战性的360｛\deg｝无界数据集NeRDS 360上演示了我们的方法，并表明NeO 360在新视图合成方面优于最先进的可推广方法，同时还提供编辑和合成功能。项目页面：https://zubair-irshad.github.io/projects/neo360.html et.al.|[2308.12967](http://arxiv.org/abs/2308.12967)|**[link](https://github.com/zubair-irshad/NeO-360)**|
|**2023-08-23**|**ARF-Plus: Controlling Perceptual Factors in Artistic Radiance Fields for 3D Scene Stylization**|辐射场风格转移是一个新兴的领域，由于神经辐射场在三维重建和视图合成中的出色表现，作为三维场景风格化的一种手段，它最近受到了欢迎。我们强调了在辐射场风格转移方面的研究空白，即缺乏足够的感知可控性，这是由2D图像风格转移中的现有概念所驱动的。在本文中，我们提出了ARF Plus，一个对感知因素提供可管理控制的3D神经风格转移框架，以系统地探索3D场景风格化中的感知可控性。提出了四种不同类型的控制——颜色保持控制、（风格模式）比例控制、空间（选择性风格化区域）控制和深度增强控制——并将其集成到该框架中。来自真实世界数据集的定量和定性结果表明，在对3D场景进行风格化时，我们的ARF Plus框架中的四种类型的控件成功地实现了相应的感知控件。这些技术适用于单个样式输入以及场景中多个样式的同时应用。这开启了一个无限可能性的领域，允许对风格化效果进行定制修改，并灵活融合不同风格的优势，最终能够在3D场景中创造新颖而引人注目的风格效果。 et.al.|[2308.12452](http://arxiv.org/abs/2308.12452)|null|
|**2023-08-22**|**Enhancing NeRF akin to Enhancing LLMs: Generalizable NeRF Transformer with Mixture-of-View-Experts**|跨场景可推广的NeRF模型可以直接合成看不见场景的新视图，已成为NeRF领域的一个新焦点。现有的几种尝试依赖于越来越端到端的“神经化”架构，即用变压器等高性能神经网络取代场景表示和/或渲染模块，并将新颖的视图合成转化为前馈推理管道。虽然这些前馈“神经化”架构仍然不能很好地开箱即用地适应不同的场景，但我们建议将它们与来自大型语言模型（LLM）的强大的专家混合（MoE）思想联系起来，该思想通过在更大的整体模型容量和灵活的每实例专业化之间进行平衡，展示了卓越的泛化能力。从最近一种名为GNT的可推广NeRF架构开始，我们首先证明了MoE可以巧妙地插入以增强模型。我们进一步定制了共享的永久专家和几何体感知的一致性损失，以分别增强跨场景一致性和空间平滑性，这对于可推广的视图合成至关重要。我们提出的模型被称为GNT with Mixture-of-View-Experts（GNT-MOVE），在转移到看不见的场景时，实验显示了最先进的结果，表明在零样本和少拍摄设置中都有更好的跨场景泛化。我们的代码可在https://github.com/VITA-Group/GNT-MOVE. et.al.|[2308.11793](http://arxiv.org/abs/2308.11793)|**[link](https://github.com/vita-group/gnt-move)**|
|**2023-08-22**|**IT3D: Improved Text-to-3D Generation with Explicit View Synthesis**|从强大的大型文本到图像扩散模型（LDM）中提取知识，推动了文本到3D技术的最新进展。尽管如此，现有的文本到3D方法经常会遇到诸如过度饱和、细节不足和不切实际的输出等挑战。这项研究提出了一种新的策略，利用显式合成的多视图图像来解决这些问题。我们的方法涉及利用LDM授权的图像到图像管道，以基于粗略3D模型的渲染生成高质量的图像。尽管生成的图像在很大程度上缓解了上述问题，但由于大扩散模型固有的生成性质，诸如视图不一致和显著的内容差异等挑战仍然存在，这给有效利用这些图像带来了巨大的困难。为了克服这一障碍，我们主张将鉴别器与新的扩散GAN双重训练策略相结合，以指导3D模型的训练。对于合并的鉴别器，合成的多视图图像被视为真实数据，而优化的3D模型的渲染则充当假数据。我们进行了一系列全面的实验，证明了我们的方法相对于基线方法的有效性。 et.al.|[2308.11473](http://arxiv.org/abs/2308.11473)|**[link](https://github.com/buaacyw/it3d-text-to-3d)**|

<p align=right>(<a href=#updated-on-20230905>back to top</a>)</p>

## 3D Reconstruction

|Publish Date|Title|Abstract|PDF|Code|
|---|---|---|---|---|
|**2023-09-01**|**Dense Voxel 3D Reconstruction Using a Monocular Event Camera**|事件摄像机是受生物系统启发，专门捕捉亮度变化的传感器。与传统的基于帧的相机相比，这些新兴相机具有许多优势，包括高动态范围、高帧率和极低功耗。由于这些优势，事件摄像机越来越多地应用于各个领域，如帧插值、语义分割、里程计和SLAM。然而，它们在VR应用的3D重建中的应用还没有得到充分的探索。该领域以前的方法主要集中在通过深度图估计进行三维重建。产生密集3D重建的方法通常需要多个相机，而利用单个事件相机的方法只能产生半密集的结果。可以产生密集3D重建的其他单相机方法依赖于创建管道，该管道结合了上述方法或其他现有的运动结构（SfM）或多视图立体（MVS）方法。在本文中，我们提出了一种仅使用单个事件相机来解决密集三维重建的新方法。据我们所知，我们的工作是这方面的第一次尝试。我们的初步结果表明，所提出的方法可以直接产生视觉上可区分的密集三维重建，而不需要像现有方法那样使用管道。此外，我们还使用事件相机模拟器创建了一个合成数据集，其中包含39739$的对象扫描。该数据集将有助于加速该领域的其他相关研究。 et.al.|[2309.00385](http://arxiv.org/abs/2309.00385)|null|
|**2023-09-01**|**On the Localization of Ultrasound Image Slices within Point Distribution Models**|甲状腺疾病最常见的诊断方法是使用高分辨率超声（US）。纵向结节追踪是监测甲状腺病理形态变化的关键诊断方案。然而，由于维持器官的心理3D重建的固有挑战，这项任务给临床医生带来了巨大的认知负荷。因此，我们提出了一个在3D形状表示中自动定位US图像切片的框架，以简化如何进行这种超声诊断。我们提出的方法通过对比度量学习，学习US图像块和个人甲状腺形状的3D表面之间的共同潜在嵌入空间，或统计形状模型（SSM）形式的统计聚合。使用跨模态配准和Procrustes分析，我们利用模型中的特征将US切片配准为甲状腺形状的3D网格表示。我们证明了我们的多模态配准框架可以在患者特定器官的3D表面拓扑结构和SSM的平均形状上定位图像。实验结果表明，在患者特定的3D解剖结构上，切片位置可以在距离地面实况切片位置平均1.2毫米和SSM平均4.6毫米的范围内预测，这证明了其在超声采集期间对切片定位的有用性。代码公开：\href{https://github.com/vuenc/slice-to-shape}{https://github.com/vuenc/slice-to-shape} et.al.|[2309.00372](http://arxiv.org/abs/2309.00372)|null|
|**2023-08-31**|**Efficient Multi-View Graph Clustering with Local and Global Structure Preservation**|基于锚点的多视图图聚类（AMVGC）由于其高效性和跨多个视图捕获互补结构信息的能力而受到广泛关注。直观地说，高质量的锚图对AMVGC的成功起着至关重要的作用。然而，现有的AMVGC方法只考虑单个结构信息，即局部或全局结构，这为学习任务提供了足够的信息。具体地说，过于分散的全局结构导致学习锚不能很好地描述集群划分。相反，具有不适当相似性度量的局部结构会导致潜在的不准确锚分配，最终导致次优聚类性能。为了解决这个问题，我们提出了一种新的基于锚点的多视图图聚类框架，称为具有局部和全局结构保护的高效多视图图集群（EMVGC-LG）。具体而言，设计了一个具有理论保障的统一框架，以获取本地和全球信息。此外，EMVGC-LG还联合优化了锚点构建和图学习，以提高聚类质量。此外，EMVGC-LG继承了现有AMVGC方法在样本数量方面的线性复杂性，这是时间经济的，并且可以很好地随数据大小扩展。大量的实验证明了我们提出的方法的有效性和效率。 et.al.|[2309.00024](http://arxiv.org/abs/2309.00024)|**[link](https://github.com/wy1019/emvgc-lg)**|
|**2023-08-30**|**Autonomous damage assessment of structural columns using low-cost micro aerial vehicles and multi-view computer vision**|结构柱是建筑和桥梁的重要承载构件。柱损坏的早期检测对于评估剩余性能和防止系统级崩溃非常重要。本研究提出了一种创新的基于端到端微型飞行器（MAV）的方法来自动扫描和检查立柱。首先，提出了一种基于MAV的图像自动采集方法。MAV被编程为感应结构柱及其周围环境。在导航过程中，MAV首先检测并接近结构柱。然后，它开始收集每个检测到的列周围多个视点的图像数据。其次，收集的图像将用于评估损坏类型和损坏位置。第三，将通过融合多个摄像机视图的评估结果来确定结构柱的损伤状态。在本研究中，选择钢筋混凝土（RC）柱来证明该方法的有效性。实验结果表明，所提出的基于MAV的检测方法可以有效地从多个视角采集图像，并准确评估RC柱的临界损伤。该方法提高了检查期间的自主权水平。此外，评估结果比现有的2D视觉方法更全面。所提出的检查方法的概念可以扩展到其他结构柱，如桥墩。 et.al.|[2308.16278](http://arxiv.org/abs/2308.16278)|null|
|**2023-08-30**|**Learning Structure-from-Motion with Graph Attention Networks**|在本文中，我们通过使用图注意力网络来解决从运动中学习结构（SfM）的问题。SfM是一个经典的计算机视觉问题，通过迭代最小化重投影误差来解决，称为束调整（BA），从良好的初始化开始。为了获得对BA足够好的初始化，传统方法依赖于一系列子问题（如成对姿态估计、姿态平均或三角测量），这些子问题提供了一个初始解决方案，然后可以使用BA进行细化。在这项工作中，我们通过学习一个模型来替换这些子问题，该模型将在多个视图中检测到的2D关键点作为输入，并输出相应的相机姿势和3D关键点坐标。我们的模型利用图神经网络来学习SfM特定的基元，并表明它可以用于新的和看不见的序列的重建的快速推理。实验结果表明，所提出的模型优于竞争的基于学习的方法，并在具有较低运行时间的同时挑战了COLMAP。 et.al.|[2308.15984](http://arxiv.org/abs/2308.15984)|null|
|**2023-08-29**|**Intensity correlation holography for remote phase sensing and 3D imaging**|全息是一种通过与参考波的干涉组合来测量光学信号波前的既定技术。传统上，全息图的积分时间受到干涉仪相干时间的限制，因此制备远程物体的全息图具有挑战性，尤其是使用弱照明。在这里，我们通过使用强度相关干涉测量法来规避这一限制。尽管单个全息图的曝光时间必须短于干涉仪相干时间，但我们表明，任何数量的随机相移全息图都可以组合成单个强度相关全息图。在原理验证实验中，我们使用该技术在弱照明和无主动相位稳定的情况下，对距离约3m的物体进行相位成像和3D重建。 et.al.|[2308.15619](http://arxiv.org/abs/2308.15619)|null|
|**2023-08-29**|**3D-MuPPET: 3D Multi-Pigeon Pose Estimation and Tracking**|动物姿势跟踪的无标记方法最近得到了发展，但在3D中跟踪大型动物群体的框架和基准仍然缺乏。为了克服文献中的这一空白，我们提出了3D MuPPET，这是一个使用多个视图以交互式速度估计和跟踪多达10只鸽子的3D姿势的框架。我们训练姿势估计器来推断多只鸽子的2D关键点和边界框，然后将关键点三角化为3D。对于对应匹配，我们首先将2D检测与第一帧中的全局身份动态匹配，然后使用2D跟踪器来维护后续帧中跨视图的对应关系。对于均方根误差（RMSE）和正确关键点百分比（PCK），我们实现了与现有技术的3D姿态估计器相当的精度。我们还展示了一个新颖的用例，其中我们的模型用单个鸽子的数据训练，在包含多只鸽子的数据上提供了可比较的结果。这可以简化向新物种的领域转移，因为注释单个动物数据比注释多动物数据劳动密集度低。此外，我们对3D MuPPET的推理速度进行了基准测试，在2D中高达10fps，在3D中高达1.5fps，并进行了定量跟踪评估，这产生了令人鼓舞的结果。最后，我们展示了3D MuPPET在自然环境中也能工作，而无需对附加注释进行模型微调。据我们所知，我们是第一个提出适用于室内和室外环境的2D/3D姿势和轨迹跟踪框架的公司。 et.al.|[2308.15316](http://arxiv.org/abs/2308.15316)|null|
|**2023-08-28**|**R3D3: Dense 3D Reconstruction of Dynamic Scenes from Multiple Cameras**|密集的三维重建和自我运动估计是自动驾驶和机器人技术的关键挑战。与当今部署的复杂、多模态系统相比，多摄像头系统提供了一种更简单、低成本的替代方案。然而，基于相机的复杂动态场景的3D重建已被证明是极其困难的，因为现有的解决方案往往会产生不完整或不连贯的结果。我们提出了R3D3，一种用于密集3D重建和自我运动估计的多摄像机系统。我们的方法在利用来自多个相机的时空信息的几何估计和单目深度细化之间迭代。我们集成了多相机特征相关性和密集束调整算子，以产生稳健的几何深度和姿态估计。为了改进几何深度不可靠的重建，例如对于移动对象或低纹理区域，我们通过深度细化网络引入了可学习的场景先验。我们展示了这种设计能够对具有挑战性的动态户外环境进行密集、一致的3D重建。因此，我们在DDAD和NuScenes基准上实现了最先进的密集深度预测。 et.al.|[2308.14713](http://arxiv.org/abs/2308.14713)|null|
|**2023-08-27**|**Sparse3D: Distilling Multiview-Consistent Diffusion for Object Reconstruction from Sparse Views**|从极其稀疏的视图重建3D对象是一个长期存在且具有挑战性的问题。虽然最近的技术使用图像扩散模型来在新视点生成看似合理的图像，或者使用分数蒸馏采样（SDS）将预先训练的扩散先验提取到3D表示中，但这些方法通常难以同时实现新视点合成（NVS）和几何体的高质量、一致和详细的结果。在这项工作中，我们提出了Sparse3D，这是一种为稀疏视图输入量身定制的新型3D重建方法。我们的方法从多视点一致扩散模型中提取鲁棒先验，以细化神经辐射场。具体来说，我们使用了一个控制器，该控制器利用输入视图中的核线特征，引导预先训练的扩散模型，如稳定扩散，以生成与输入保持3D一致性的新视图图像。通过利用强大的图像扩散模型中的2D先验，我们的集成模型即使在面对开放世界对象时也能始终如一地提供高质量的结果。为了解决传统SDS引入的模糊性，我们引入了类别分数蒸馏采样（C-SDS）来增强细节。我们在CO3DV2上进行了实验，这是一个真实世界对象的多视图数据集。定量和定性评估都表明，我们的方法在NVS和几何重建方面优于以往最先进的工作。 et.al.|[2308.14078](http://arxiv.org/abs/2308.14078)|null|
|**2023-08-27**|**Multi-plane denoising diffusion-based dimensionality expansion for 2D-to-3D reconstruction of microstructures with harmonized sampling**|获得可靠的微观结构数据集是借助集成计算材料工程（ICME）方法进行材料系统设计的关键一步。然而，由于高实验成本或技术限制，获得三维（3D）微观结构数据集通常具有挑战性，而获得二维（2D）显微照片相对更容易。为了解决这个问题，本研究提出了一种使用基于扩散的生成模型（DGM）进行微观结构二维到三维重建的新框架，称为Micro3Diff。具体而言，这种方法仅需要预先训练的DGM来生成2D样本，并且维度扩展（2D到3D）仅在生成过程（即反向扩散过程）中发生。所提出的框架结合了一个称为多平面去噪扩散的新概念，该概念将来自不同平面的噪声样本（即潜在变量）转换为数据结构，同时保持3D空间中的空间连通性。此外，还开发了一个协调的采样过程，以解决在维度扩展过程中DGM的反向马尔可夫链的可能偏差。结合起来，我们证明了Micro3Diff在重建具有连接切片的3D样本方面的可行性，这些切片在形态学上与原始2D图像保持等效。为了验证Micro3Diff的性能，重建了各种类型的微观结构（合成和实验观察），并对生成的样品的质量进行了定性和定量评估。成功的重建结果激发了Micro3Diff在即将到来的ICME应用中的潜在应用，同时在理解和操纵DGM的潜在空间方面取得了突破。 et.al.|[2308.14035](http://arxiv.org/abs/2308.14035)|null|

<p align=right>(<a href=#updated-on-20230905>back to top</a>)</p>

## Diffusion

|Publish Date|Title|Abstract|PDF|Code|
|---|---|---|---|---|
|**2023-09-01**|**Iterative Multi-granular Image Editing using Diffusion Models**|文本引导图像合成的最新进展极大地改变了创造性专业人员生成艺术和美学上令人愉悦的视觉资产的方式。为了充分支持这种创造性的努力，这个过程应该具备以下能力：1）迭代地编辑世代，2）控制所需变化的空间范围（全局、局部或介于两者之间的任何变化）。我们将这种实用的问题设置形式化为迭代多粒度编辑。虽然用于图像合成和编辑的基于扩散的模型已经取得了实质性进展，但它们都是一次性的（即，没有迭代编辑能力），并且不会自然产生多粒度控制（即，覆盖从局部到全局编辑的全谱）。为了克服这些缺点，我们提出了EMILIE：迭代多粒度图像编辑器。EMILIE引入了一种新的潜在迭代策略，该策略重新利用预先训练的扩散模型来促进迭代编辑。这由用于多粒度控制的梯度控制操作来补充。我们引入了一个新的基准数据集来评估我们新提出的设置。我们针对最近最先进的方法进行了详尽的定量和定性评估，以适应我们的任务，从而达到EMILIE的勇气。我们希望我们的工作将引起人们对这一新确定的、务实的问题设置的关注。 et.al.|[2309.00613](http://arxiv.org/abs/2309.00613)|null|
|**2023-09-01**|**Presentation of some elementary properties of Segal-Bargmann space and of unitary Segal-Bargmann transform with applications**|在这项工作中，我们给出了Segal-Bargmann空间的一些基本性质和酉Segal-Bargmann变换的一些性质，并将其应用于由扩散问题或Regeon场论引起的微分算子。 et.al.|[2309.00566](http://arxiv.org/abs/2309.00566)|null|
|**2023-09-01**|**Diffusion limited aggregation, resetting and large deviations of Brownian motion**|分形生长模型通常考虑颗粒在介质中扩散，并且在第一次接触时不可逆地粘附在形成的聚集体上。众所周知的扩散限制聚集（DLA）模型及其推广表明，分形维数对粒子随机运动的性质很敏感。在这里，我们研究了有限寿命布朗粒子形成的结构，即在规定时间内被约束以找到聚集体的粒子，否则这些粒子将被移除。这种运动可以通过具有随机重置的扩散来建模，这是近年来被广泛研究的一类过程。在较短的使用寿命限制内，极少数颗粒能够到达聚集体。因此，生长是由非典型布朗轨迹控制的，根据大偏差原理，这些轨迹几乎是直线移动的。在 $d$维度中，骨料的分形维数从DLA值开始下降，并趋于1，而不是像弹道骨料预期的那样增加到$d$ 。在零寿命极限中，我们恢复了R.Jullien很久以前提出的“尖端聚合”的非平凡模型[J.Phys.A:Math.Gen.192129（1986）]。 et.al.|[2309.00560](http://arxiv.org/abs/2309.00560)|null|
|**2023-09-01**|**Relativistic hydrodynamic fluctuations from an effective action: causality, stability, and the information current**|因果关系是延迟格林函数在相对论的所有惯性系中保持延迟的必要条件，这确保了波动的耗散是洛伦兹不变的概念。对于通过Schwinger-Keldysh形式引入的具有随机波动的一阶BDNK理论，我们表明，强加因果关系和稳定性会导致流体动力学波动的相关函数，这些函数仅在小频率和波数下显示出预期的物理性质，即在一阶方法的预期有效范围内。对于使用信息流构建的Israel和Stewart类型的二阶理论，使得熵产生总是非负的，使用Martin Siggia-Rose方法提出了一个随机公式，其中施加因果关系和稳定性会导致具有所需性质的相关器。我们还展示了如何通过这样的行动来确定格林的职能。我们识别 $\mathbb{Z}_2$ 对称性，类似于Kubo Martin Schwinger对称性，在该对称性下，Martin Siggia-Rose作用是不变的。这种改进的Kubo-Martin-Schwinger对称性为流体动力学系统的有效作用公式提供了新的指导，该系统的动力学不完全受守恒定律的约束。此外，这种对称性确保了详细平衡原理在协变方式下是有效的。我们使用新的对称性来进一步阐明Schwinger Keldysh和Martin Siggia Rose方法之间的联系，在相对论流体力学的二阶理论中建立了这些描述之间的精确联系。最后，利用修正后的Kubo-Martin-Schwinger对称性确定了在一般流体动力学框架下Israel Stewart理论中描述扩散的相应作用。 et.al.|[2309.00512](http://arxiv.org/abs/2309.00512)|null|
|**2023-09-01**|**Schwinger-Keldysh effective field theory for stable and causal relativistic hydrodynamics**|我们构造了稳定的因果有效场论（EFTs）来描述相对论扩散和相对论流体力学中的统计涨落。这些EFT是完全非线性的，包括与背景源的耦合，使我们能够计算包括统计波动影响在内的n点时间有序相关函数。我们构造的EFT分别受到相对论扩散的Maxwell Cattaneo模型和相对论流体力学的M uller Israel Stewart模型的启发，并使用Martin Siggia Rose和Schwinger Keldysh形式推导对称性，这确保了理论中的n点相关函数和相互作用满足适当的波动耗散定理。由于这些EFT通常允许不受低能红外对称性固定的紫外线扇区，我们发现它们同时允许动态KMS对称性的多重实现。我们还评论了在最近提出的相对论流体力学的稳定和因果Bemfica Disconzi-Noronha Kovtun模型中包含统计波动的某些障碍。 et.al.|[2309.00511](http://arxiv.org/abs/2309.00511)|null|
|**2023-09-01**|**How heat propagates in `non-Fermi liquid' $^3$He**|在朗道的费米液体中，传输由准粒子之间的散射控制。正常液体$^3$He符合此图，但仅当T$<0.02$T$_F$时。在这里，我们观察到与标准行为的偏差伴随着费米子-费米子散射时间下降到普朗克时间$\frac｛\hbar｝｛k_BT｝$以下。这种量子液体的热扩散率受基本物理常数和早期在经典液体中观察到的最小值的限制。这意味着液体的集体激发（声音模式）正在携带热量。我们认为，如果热量由2k$_F$流体动力学声音模式携带，那么热导率的振幅和迄今为止无法解释的$T^{1/2}$ 温度依赖性都可以在没有其他可调节参数的情况下找到解释。 et.al.|[2309.00502](http://arxiv.org/abs/2309.00502)|null|
|**2023-09-01**|**VideoGen: A Reference-Guided Latent Diffusion Approach for High Definition Text-to-Video Generation**|在本文中，我们提出了VideoGen，这是一种文本到视频的生成方法，它可以使用参考引导的潜在扩散生成具有高帧保真度和强时间一致性的高清晰度视频。我们利用现成的文本到图像生成模型，例如Stable Diffusion，从文本提示生成具有高内容质量的图像，作为指导视频生成的参考图像。然后，我们引入了一个以参考图像和文本提示为条件的高效级联潜在扩散模块，用于生成潜在视频表示，然后是基于流的时间上采样步骤，以提高时间分辨率。最后，我们通过增强的视频解码器将潜在的视频表示映射到高清晰度视频中。在训练过程中，我们使用地面实况视频的第一帧作为参考图像来训练级联的潜在扩散模块。我们的方法的主要特点包括：文本到图像模型生成的参考图像提高了视觉逼真度；以它为条件，使扩散模型更加关注视频动力学的学习；并且视频解码器在未标记的视频数据上进行训练，从而受益于高质量的容易获得的视频。VideoGen在定性和定量评估方面开创了文本到视频生成的新技术。 et.al.|[2309.00398](http://arxiv.org/abs/2309.00398)|null|
|**2023-09-01**|**Bayesian estimation and reconstruction of marine surface contaminant dispersion**|向海洋环境排放有害物质对公众健康和生态系统都构成重大风险。在此类事件中，必须准确估计来源的释放强度，并根据收集的测量结果重建物质的时空分布。在这项研究中，我们提出了一个综合评估框架来应对这一挑战，该框架可以与传感器网络或移动传感器一起用于环境监测。我们采用基本对流-扩散偏微分方程（PDE）来表示非均匀流场中物理量的一般色散。使用动态瞬态有限元法（FEM）将PDE模型在空间上离散为线性状态空间模型，从而可以将时变色散的表征纳入从传感器测量推断模型状态的问题中。我们还考虑了不完美的传感现象，包括在使用传感器网络时经常遇到的漏检和信号量化。这种复杂的传感器过程将非线性引入贝叶斯估计过程。Rao-Blackellised粒子滤波器（RBPF）被设计为通过利用状态空间模型的线性结构来提供有效的解决方案，而测量模型的非线性可以通过粒子的蒙特卡罗近似来处理。通过模拟波罗的海漏油事件和真实的海洋流量数据，验证了所提出的框架。结果表明，在存在不完美测量的情况下，所开发的时空离散模型和估计方案是有效的。此外，还讨论了参数选择过程，并进行了一些比较研究，以说明所提出的算法与现有方法相比的优势。 et.al.|[2309.00369](http://arxiv.org/abs/2309.00369)|null|
|**2023-09-01**|**Fast Diffusion EM: a diffusion model for blind inverse problems with application to deconvolution**|使用扩散模型来求解逆问题是一个日益增长的研究领域。目前的方法假设退化是已知的，并在恢复质量和多样性方面提供了令人印象深刻的结果。在这项工作中，我们利用这些模型的效率来联合估计退化模型的恢复图像和未知参数。特别地，我们设计了一种基于众所周知的期望最小化（EM）估计方法和扩散模型的算法。我们的方法在使用从扩散模型中提取的样本来近似逆问题的预期对数似然性和估计未知模型参数的最大化步骤之间交替。对于最大化步骤，我们还引入了一种新的基于即插即用去噪器的模糊核正则化。扩散模型运行时间很长，因此我们提供了算法的快速版本。与其他最先进的方法相比，在盲图像去模糊方面的大量实验证明了我们的方法的有效性。 et.al.|[2309.00287](http://arxiv.org/abs/2309.00287)|null|
|**2023-09-01**|**Data-driven Topology Optimization of Channel Flow Problems**|典型的拓扑优化方法需要复杂的迭代计算，无法满足快速计算应用的要求。研究神经网络是为了减少计算优化结果的时间，然而，流体拓扑优化的数据驱动方法很少被讨论。本文旨在介绍一种神经网络结构，该结构避免了耗时的迭代过程，并对Stokes流的拓扑优化具有较强的泛化能力。对已经成功用于固体结构优化问题的不同神经网络方法进行了变异，并针对流体拓扑优化情况进行了检验，包括卷积神经网络（CNN）、条件生成对抗性网络（cGAN）和去噪扩散隐式模型（DDIM）。将所提出的神经网络方法应用于Stokes流的通道流拓扑优化问题。结果表明，我们提出的方法具有较高的像素精度，与传统方法相比，我们的执行时间平均减少了663倍。 et.al.|[2309.00278](http://arxiv.org/abs/2309.00278)|null|

<p align=right>(<a href=#updated-on-20230905>back to top</a>)</p>

## NeRF

|Publish Date|Title|Abstract|PDF|Code|
|---|---|---|---|---|
|**2023-09-01**|**GNFactor: Multi-Task Real Robot Learning with Generalizable Neural Feature Fields**|开发能够在非结构化现实世界环境中通过视觉观察执行各种操作任务的代理是机器人技术中的一个长期问题。为了实现这一目标，机器人需要对场景的3D结构和语义有全面的了解。在这项工作中，我们提出了 $\textbf｛GNFactor｝$，一种用于多任务机器人操作的视觉行为克隆代理，具有$\textbf｛G｝$通用$\textbf｛N｝$eural功能$\textbf｛F｝$字段。GNFactor联合优化了作为重建模块的可推广神经场（GNF）和作为决策模块的感知转换器，利用了共享的深度3D体素表示。为了在3D中结合语义，重建模块利用视觉语言基础模型（$\textit｛例如｝$ ，Stable Diffusion）将丰富的语义信息提取到深度3D体素中。我们在3个真实机器人任务中评估了GNFactor，并在10个RLBench任务中进行了详细的消融，演示次数有限。我们观察到GNFactor在可见和不可见任务中比当前最先进的方法有了实质性的改进，证明了GNFactor强大的泛化能力。我们的项目网站是https://yanjieze.com/GNFactor/。 et.al.|[2308.16891](http://arxiv.org/abs/2308.16891)|**[link](https://github.com/YanjieZe/GNFactor)**|
|**2023-08-30**|**Active Neural Mapping**|我们用不断学习的神经场景表示来解决主动映射的问题，即主动神经映射。关键在于通过有效的代理移动积极找到要探索的目标空间，从而最大限度地减少在以前看不见的环境中飞行中的地图不确定性。在本文中，我们检验了连续学习神经场的权重空间，并从经验上表明，神经变异性，即对随机权重扰动的预测鲁棒性，可以直接用于测量神经映射的瞬时不确定性。结合神经映射中继承的连续几何信息，可以引导agent找到一条可遍历的路径，以逐渐获得环境知识。我们首次提出了一种用于在线场景重建的具有基于坐标的隐式神经表示的主动映射系统。在视觉逼真的Gibson和Matterport3D环境中的实验证明了所提出方法的有效性。 et.al.|[2308.16246](http://arxiv.org/abs/2308.16246)|null|
|**2023-08-29**|**Canonical Factors for Hybrid Neural Fields**|因子特征量提供了一种简单的方法来构建更紧凑、高效和可积分的神经场，但也引入了对真实世界数据不一定有益的偏差。在这项工作中，我们（1）描述了这些架构对轴对准信号的不希望有的偏差——它们可能导致高达2 PSNR的辐射场重建差异——以及（2）探索了学习一组规范化变换如何通过消除这些偏差来改进表示。我们在二维模型问题中证明，同时学习这些变换和场景外观是成功的，效率大大提高。我们使用图像、符号距离和辐射场重建任务验证了最终的架构，我们称之为TILTED，在这些任务中，我们观察到了质量、稳健性、紧凑性和运行时间方面的改进。结果表明，TILTED可以实现比基线大2倍的能力，同时突出神经场评估程序的弱点。 et.al.|[2308.15461](http://arxiv.org/abs/2308.15461)|null|
|**2023-08-30**|**NSF: Neural Surface Fields for Human Modeling from Monocular Depth**|从单眼相机获得个性化的3D可动画化化身在游戏、虚拟试穿、动画和VR/XR等领域有几个现实世界的应用。然而，从这种稀疏的数据中建模动态和细粒度的服装变形是非常具有挑战性的。现有的从深度数据建模3D人类的方法在计算效率、网格一致性以及分辨率和拓扑结构的灵活性方面具有局限性。例如，使用隐式函数重建形状和每帧提取显式网格在计算上是昂贵的，并且不能确保跨帧的连贯网格。此外，在具有离散表面的预先设计的人类模板上预测每个顶点的变形在分辨率和拓扑结构上缺乏灵活性。为了克服这些局限性，我们提出了一种新的方法“关键特征：神经表面场”，用于从单目深度对穿着3D衣服的人类进行建模。NSF仅在基面上定义了一个神经场，该神经场对连续和灵活的位移场进行建模。NSF可以适应不同分辨率和拓扑结构的基面，而无需在推理时进行重新训练。与现有方法相比，我们的方法在保持网格一致性的同时消除了昂贵的每帧表面提取，并且能够在不重新训练的情况下重建任意分辨率的网格。为了促进这方面的研究，我们在项目页面上发布了我们的代码：https://yuxuan-xue.com/nsf. et.al.|[2308.14847](http://arxiv.org/abs/2308.14847)|null|
|**2023-08-28**|**A Transformer-Conditioned Neural Fields Pipeline with Polar Coordinate Representation for Astronomical Radio Interferometric Data Reconstruction**|在射电天文学中，能见度数据是对射电望远镜波信号的测量，被转换成图像，用于观测遥远的天体。然而，由于信号稀疏性和其他因素，这些结果图像通常包含真实源和伪影。获得更干净图像的一种方法是在成像之前将样本重建成致密的形式。不幸的是，现有的可见性重建方法可能会错过频率数据的一些分量，因此模糊的对象边缘和持久的伪影仍然存在于图像中。此外，由于数据偏斜，在不规则可见性样本上的计算开销很高。为了解决这些问题，我们提出了PolarRec，这是一种干涉能见度数据的重建方法，它由具有极坐标表示的变压器条件神经场管道组成。这种表示与望远镜在地球自转时观察天体区域的方式相匹配。我们进一步提出了径向频率损失函数，使用极坐标系中的径向坐标与频率信息进行关联，以帮助重建完整的可见性。我们还根据极坐标系中的角坐标对可见性采样点进行分组，并使用分组作为随后使用Transformer编码器进行编码的粒度。因此，我们的方法可以有效地捕捉可见性数据的固有特征。我们的实验表明，PolarRec通过忠实地重建可见性域中的所有频率分量，显著提高了成像结果，同时显著降低了计算成本。 et.al.|[2308.14610](http://arxiv.org/abs/2308.14610)|null|
|**2023-08-24**|**NeO 360: Neural Fields for Sparse View Synthesis of Outdoor Scenes**|最近的隐式神经表示在新的视图合成中显示出了很好的结果。然而，现有的方法需要从许多视图进行昂贵的每场景优化，因此限制了它们在真实世界的无边界城市环境中的应用，在这些环境中，从极少数视图观察到感兴趣的对象或背景。为了缓解这一挑战，我们引入了一种名为NeO360的新方法，用于户外场景稀疏视图合成的神经场。NeO 360是一种可推广的方法，它从单个或几个摆出姿势的RGB图像重建360｛\deg｝场景。我们方法的本质是捕捉复杂的真实世界户外3D场景的分布，并使用可以从任何世界点查询的混合图像条件三平面表示。我们的表示结合了基于体素和鸟瞰图（BEV）的最佳表示，比每种表示都更有效、更具表现力。NeO 360的表示使我们能够从大量无界3D场景中学习，同时在推理过程中从一张图像中提供对新视图和新场景的可推广性。我们在所提出的具有挑战性的360｛\deg｝无界数据集NeRDS 360上演示了我们的方法，并表明NeO 360在新视图合成方面优于最先进的可推广方法，同时还提供编辑和合成功能。项目页面：https://zubair-irshad.github.io/projects/neo360.html et.al.|[2308.12967](http://arxiv.org/abs/2308.12967)|**[link](https://github.com/zubair-irshad/NeO-360)**|
|**2023-08-23**|**Semantic-Aware Implicit Template Learning via Part Deformation Consistency**|学习隐式模板作为神经场最近在无监督形状对应方面表现出了令人印象深刻的性能。尽管取得了成功，但我们观察到，目前仅依赖几何信息的方法往往会在具有高结构可变性的通用物体形状中学习次优变形。在本文中，我们强调了零件变形一致性的重要性，并提出了一个语义感知的隐式模板学习框架，以实现语义上合理的变形。通过利用自监督特征提取器的语义先验，我们建议使用新的语义感知变形代码进行局部条件调节，并对零件变形、全局变形和全局缩放进行变形一致性正则化。我们的大量实验证明了所提出的方法在各种任务中优于基线：关键点转移、零件标签转移和纹理转移。更有趣的是，我们的框架在更具挑战性的环境下显示出更大的性能提升。我们还提供了定性分析来验证语义感知变形的有效性。代码可在https://github.com/mlvlab/PDC. et.al.|[2308.11916](http://arxiv.org/abs/2308.11916)|null|
|**2023-08-22**|**Approaching human 3D shape perception with neurally mappable models**|人类毫不费力地推断出物体的三维形状。这种能力的基础是什么计算？尽管已经提出了各种计算模型，但它们都没有捕捉到人类在不同视点之间匹配物体形状的能力。在这里，我们询问是否以及如何缩小这一差距。我们从一类相对新颖的计算模型3D神经场开始，它通过深度神经网络（DNN）中的合成封装了经典分析的基本原理。首先，我们发现3D光场网络（3D-LFN）支持与人类完全一致的3D匹配判断，用于类别内比较、强调标准DNN模型的3D失败情况的对抗性定义比较，以及用于无类别结构的算法生成形状的对抗性定义比较。然后，我们通过一系列计算实验研究了3D-LFN实现人类对齐性能的能力来源。在训练过程中暴露于物体的多个视角和多视角学习目标是模型-人对齐背后的主要因素；当使用多视图目标进行训练时，即使是传统的DNN架构也更接近人类行为。最后，我们发现，虽然用多视图学习目标训练的模型能够部分推广到新的对象类别，但它们不能达到人类的一致性。这项工作为理解可神经映射的计算架构中的人形推断提供了基础，并突出了未来工作的重要问题。 et.al.|[2308.11300](http://arxiv.org/abs/2308.11300)|null|
|**2023-08-21**|**Canonical Cortical Field Theories**|我们根据场论，使用放置在皮层表面2D晶格上的神经单元来表征神经元活动的动力学。分析神经元单元的电活动，目的是推导出一个具有简单功能形式的神经场模型，该模型仍然能够预测或重现经验发现。使用神经质量对每个神经单元进行建模，并在连续极限中导出伴随的场论。场论包括耦合的（真实的）克莱因-戈登场，其中模型的预测属于实验结果的范围。这些预测包括从皮层测量的电活动频谱，该频谱是使用能量对神经场本征函数的平分得出的。此外，神经场模型在一组参数内对用于建模每个神经元质量的动力学系统是不变的。具体而言，拓扑等效的动力学系统在连接到晶格中时产生相同的神经场模型；这表明所导出的场可以被解读为典型的皮层场论。我们专门研究了为传入信息的编码（或表示）提供结构的非分散场。进一步阐述随后的神经场理论，包括分散力的影响，对于理解皮层对信息的处理可能具有重要意义。 et.al.|[2308.10645](http://arxiv.org/abs/2308.10645)|null|
|**2023-08-14**|**S3IM: Stochastic Structural SIMilarity and Its Unreasonable Effectiveness for Neural Fields**|最近，神经辐射场（NeRF）通过学习仅使用姿态RGB图像的隐式表示，在渲染给定场景的新视图图像方面取得了巨大成功。NeRF和相关的神经场方法（例如，神经表面表示）通常优化逐点损失并进行逐点预测，其中一个数据点对应于一个像素。不幸的是，这一研究未能使用对远处像素的集体监督，尽管已知图像或场景中的像素可以提供丰富的结构信息。据我们所知，我们是第一个通过一种新的随机结构相似性（S3IM）损失为NeRF和相关神经场方法设计非局部多重训练范式的人，该损失将多个数据点作为一个整体处理，而不是独立处理多个输入。我们的大量实验证明了S3IM在几乎免费改进NeRF和神经表面表示方面的不合理有效性。质量度量的改进对于那些相对困难的任务可能特别显著：例如，TensoRF和DVGO在八个新的视图合成任务中的测试MSE损失意外下降了90%以上；在八个表面重建任务中，NeuS的198%F分数增益和64%的倒角$L_。此外，即使在稀疏输入、损坏图像和动态场景的情况下，S3IM也始终是稳健的。 et.al.|[2308.07032](http://arxiv.org/abs/2308.07032)|**[link](https://github.com/madaoer/s3im_nerf)**|

<p align=right>(<a href=#updated-on-20230905>back to top</a>)</p>

[contributors-shield]: https://img.shields.io/github/contributors/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[contributors-url]: https://github.com/Vincentqyw/cv-arxiv-daily/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[forks-url]: https://github.com/Vincentqyw/cv-arxiv-daily/network/members
[stars-shield]: https://img.shields.io/github/stars/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[stars-url]: https://github.com/Vincentqyw/cv-arxiv-daily/stargazers
[issues-shield]: https://img.shields.io/github/issues/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[issues-url]: https://github.com/Vincentqyw/cv-arxiv-daily/issues

