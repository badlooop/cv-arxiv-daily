[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]

## Updated on 2024.08.18
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
|**2024-08-15**|**MVInpainter: Learning Multi-View Consistent Inpainting to Bridge 2D and 3D Editing**|新视图合成（NVS）和3D生成最近取得了显著的进步。然而，这些作品主要集中在有限的类别或合成的3D资产上，不鼓励在野外场景中推广到具有挑战性的场景，也不能直接用于2D合成。此外，这些方法严重依赖于相机姿态，限制了它们在现实世界中的应用。为了克服这些问题，我们提出了MVInpainter，将3D编辑重新定义为多视图2D修复任务。具体来说，MVInpainter使用参考引导对多视图图像进行部分修复，而不是从头开始艰难地生成一个全新的视图，这大大简化了野外NVS的难度，并利用了未掩盖的线索而不是明确的姿势条件。为了确保交叉视图的一致性，MVInpainter通过来自运动分量的视频先验和来自级联参考键值关注的外观引导进行了增强。此外，MVInpainter结合了狭缝注意力，以聚合来自未遮蔽区域的高级光流特征，从而通过无姿态训练和推理来控制相机运动。在以对象为中心和面向前的数据集上进行的足够的场景级实验验证了MVInpainter的有效性，包括多种任务，如多视图对象删除、合成、插入和替换。项目页面为https://ewrfcas.github.io/MVInpainter/. et.al.|[2408.08000](http://arxiv.org/abs/2408.08000)|null|
|**2024-08-14**|**Progressive Radiance Distillation for Inverse Rendering with Gaussian Splatting**|我们提出了渐进式辐射蒸馏，这是一种逆向渲染方法，使用蒸馏进度图将基于物理的渲染与基于高斯的辐射场渲染相结合。以多视图图像为输入，我们的方法从预训练的辐射场引导开始，并使用图像拟合过程从辐射场中提取基于物理的光和材料参数。蒸馏进度图被初始化为一个较小的值，这有利于辐射场渲染。在早期迭代中，当拟合的光和材料参数远未收敛时，辐射场回退确保了图像损失梯度的完整性，并避免了吸引拟合不足状态的局部最小值。随着拟合参数的收敛，物理模型逐渐接管，蒸馏过程相应增加。在存在未被物理模型建模的光路的情况下，受影响像素的蒸馏过程永远不会结束，学习到的辐射场会留在最终渲染中。通过这种对物理模型限制的设计容差，我们可以防止未建模的颜色分量泄漏到光和材料参数中，从而减轻重新照明伪影。同时，剩余的辐射场补偿了物理模型的局限性，保证了高质量的新颖视图合成。实验结果表明，在新颖的视图合成和重新照明方面，我们的方法在质量上明显优于最先进的技术。渐进式辐射蒸馏的概念不仅限于高斯散射。我们表明，当采用基于网格的逆渲染方法时，它对显著镜面反射的场景也有积极的影响。 et.al.|[2408.07595](http://arxiv.org/abs/2408.07595)|null|
|**2024-08-14**|**Rethinking Open-Vocabulary Segmentation of Radiance Fields in 3D Space**|理解场景的3D语义是各种场景（如实体代理）的基本问题。虽然NeRF和3DGS擅长新颖的视图合成，但之前理解其语义的方法仅限于不完整的3D理解：它们的分割结果是2D掩模，它们的监督是基于2D像素的。本文重新审视了问题集，以更好地理解由NeRFs和3DGS建模的场景，如下所示。1） 我们直接监督3D点来训练语言嵌入域。它实现了最先进的精度，而不依赖于多尺度语言嵌入。2） 我们将预训练的语言字段转移到3DGS，在不牺牲训练时间或精度的情况下实现了第一个实时渲染速度。3） 我们介绍了一种3D查询和评估协议，用于同时评估重建的几何和语义。代码、检查点和注释将在线提供。项目页面：https://hyunji12.github.io/Open3DRF et.al.|[2408.07416](http://arxiv.org/abs/2408.07416)|null|
|**2024-08-13**|**SlotLifter: Slot-guided Feature Lifting for Learning Object-centric Radiance Fields**|从复杂的视觉场景中提取以对象为中心的抽象概念的能力是人类级泛化的基础。尽管以对象为中心的学习方法取得了重大进展，但在3D物理世界中学习以对象为核心的表示仍然是一个关键挑战。在这项工作中，我们提出了SlotLifter，这是一种新的以对象为中心的辐射模型，通过缝隙引导的特征提升来共同解决场景重建和分解问题。这种设计将以对象为中心的学习表示和基于图像的渲染方法结合在一起，在四个具有挑战性的合成数据集和四个复杂的现实世界数据集上提供了最先进的场景分解和新颖的视图合成性能，大大优于现有的3D以对象为核心的学习方法。通过广泛的消融研究，我们展示了SlotLifter设计的有效性，揭示了未来潜在方向的关键见解。 et.al.|[2408.06697](http://arxiv.org/abs/2408.06697)|null|
|**2024-08-13**|**ActiveNeRF: Learning Accurate 3D Geometry by Active Pattern Projection**|NeRF在新颖的视图合成方面取得了令人难以置信的成功。然而，隐式几何的精度并不令人满意，因为被动静态环境照明的空间频率较低，无法为精确的几何重建提供足够的信息。在这项工作中，我们提出了ActiveNeRF，这是一种3D几何重建框架，通过使用与相机具有恒定相对姿态的投影仪将高空间频率的图案主动投影到场景上，提高了NeRF的几何质量。我们设计了一个可学习的主动模式渲染管道，该管道联合学习场景几何和主动模式。我们发现，通过添加活动模式并在不同视图之间施加一致性，我们提出的方法在模拟和实际实验中定性和定量地优于最先进的几何重建方法。代码可在以下网址获得https://github.com/hcp16/active_nerf et.al.|[2408.06592](http://arxiv.org/abs/2408.06592)|**[link](https://github.com/hcp16/active_nerf)**|
|**2024-08-12**|**Mipmap-GS: Let Gaussians Deform with Scale-specific Mipmap for Anti-aliasing Rendering**|3D高斯散斑（3DGS）因其卓越的渲染效率和高保真度而在新型视图合成中引起了极大的关注。然而，由于来自单尺度训练的不可调表示，训练过的高斯人会遭受严重的缩放退化。尽管一些方法试图通过后处理技术来解决这个问题，例如对基元的选择性渲染或过滤技术，但高斯分布中不涉及特定于尺度的信息。在本文中，我们提出了一种统一的优化方法，通过自调整原始属性（如颜色、形状和大小）和分布（如位置），使高斯分布适应任意尺度。受mipmap技术的启发，我们为目标尺度设计了伪地面真值，并提出了一种尺度一致性制导损失，将尺度信息注入到3D高斯模型中。我们的方法是一个插件模块，适用于任何3DGS模型来解决放大和缩小混叠问题。大量实验证明了我们方法的有效性。值得注意的是，在NeRF合成数据集上，我们的方法在PSNR方面优于3DGS，放大平均为9.25 dB，缩小平均为10.40 dB。 et.al.|[2408.06286](http://arxiv.org/abs/2408.06286)|**[link](https://github.com/renaissanceee/mipmap-gs)**|
|**2024-08-12**|**FruitNeRF: A Unified Neural Radiance Field based Fruit Counting Framework**|我们介绍FruitNeRF，这是一个统一的新颖水果计数框架，利用最先进的视图合成方法直接在3D中计数任何水果类型。我们的框架采用单目相机拍摄的一组无序的姿势图像，并在每张图像中分割水果。为了使我们的系统独立于水果类型，我们采用了一个基础模型，为任何水果生成二进制分割掩码。利用RGB和语义两种模态，我们训练了一个语义神经辐射场。通过对隐式果园的均匀体积采样，我们得到了纯果点云。通过在提取的点云上应用级联聚类，我们的方法实现了精确的水果计数。神经辐射场的使用比传统方法（如物体跟踪或光流）具有显著优势，因为计数本身被提升到3D中。我们的方法防止了重复计算水果，避免了计算无关的水果。我们使用真实世界和合成数据集来评估我们的方法。真实世界的数据集由三棵手动计数的苹果树、一个具有一行和地面真实水果位置的基准苹果数据集组成，而合成数据集包括各种水果类型，包括苹果、李子、柠檬、梨、桃和芒果。此外，与U-Net相比，我们使用基础模型评估了水果计数的性能。 et.al.|[2408.06190](http://arxiv.org/abs/2408.06190)|**[link](https://github.com/meyerls/fruitnerf)**|
|**2024-08-12**|**Novel View Synthesis from a Single Image with Pretrained Diffusion Guidance**|最近的3D新颖视图合成（NVS）方法仅限于从新视点生成的以单个对象为中心的场景，并且难以应对复杂的环境。它们通常需要大量的3D数据进行训练，除了训练分布之外缺乏泛化能力。相反，无3D方法可以使用预训练的稳定扩散模型生成复杂、狂野场景的文本控制视图，而无需繁琐的微调，但缺乏相机控制。本文介绍了HawkI++，这是一种能够从单个输入图像生成相机控制视点的方法。HawkI++擅长处理复杂多样的场景，无需额外的3D数据或大量训练。它利用广泛可用的预训练NVS模型进行弱制导，将这些知识整合到3D自由视图合成方法中，以有效地实现所需的结果。我们的实验结果表明，HawkI++在定性和定量评估方面都优于现有模型，在各种场景中以所需的相机角度提供高保真度和一致的新颖视图合成。 et.al.|[2408.06157](http://arxiv.org/abs/2408.06157)|null|
|**2024-08-10**|**Visual SLAM with 3D Gaussian Primitives and Depth Priors Enabling Novel View Synthesis**|传统的基于几何的SLAM系统缺乏密集的3D重建能力，因为它们的数据关联通常依赖于特征对应。此外，基于学习的SLAM系统在实时性能和准确性方面往往不足。平衡实时性能和密集的3D重建能力是一个具有挑战性的问题。在本文中，我们提出了一种实时RGB-D SLAM系统，该系统结合了一种新的视图合成技术——3D高斯散点，用于3D场景表示和姿态估计。该技术利用了具有光栅化的3D高斯散斑的实时渲染性能，并允许通过CUDA实现实时可微优化。我们还支持从3D高斯网格重建显式密集3D重建。为了估计精确的相机姿态，我们采用了一种具有逆优化的旋转-平移解耦策略。这涉及通过基于梯度的优化在几次迭代中迭代更新两者。该过程包括可微分地渲染RGB、深度和轮廓图，并更新相机参数，以最小化现有3D高斯图的光度损失、深度几何损失和可见度损失的组合损失。然而，由于3D高斯分布的多视图不一致性，3D高斯散布（3DGS）难以准确表示曲面，这可能会导致相机姿态估计和场景重建的精度降低。为了解决这个问题，我们利用深度先验作为额外的正则化来强制执行几何约束，从而提高了姿态估计和3D重建的精度。我们还提供了关于公共基准数据集的广泛实验结果，以证明我们提出的方法在姿态精度、几何精度和渲染性能方面的有效性。 et.al.|[2408.05635](http://arxiv.org/abs/2408.05635)|null|
|**2024-08-10**|**PRTGaussian: Efficient Relighting Using 3D Gaussians with Precomputed Radiance Transfer**|我们提出了PRTGaussian，这是一种通过将3D高斯和预计算辐射传输（PRT）相结合而实现的实时可照明的新型视图合成方法。通过将可重新点亮的高斯分布拟合到多视图OLAT数据中，我们的方法实现了实时、自由的视点重新点亮。通过基于高阶球谐函数估计辐射传输，我们在捕获详细的再照明效果和保持计算效率之间实现了平衡。我们采用了一个两阶段的过程：在第一阶段，我们从多视图图像中重建对象的粗略几何形状。在第二阶段，我们用获得的点云初始化3D高斯分布，然后同时细化粗糙几何并学习每个高斯分布的光传输。对合成数据集的广泛实验表明，我们的方法可以为一般对象实现快速高质量的重新照明。代码和数据可在https://github.com/zhanglbthu/PRTGaussian. et.al.|[2408.05631](http://arxiv.org/abs/2408.05631)|**[link](https://github.com/zhanglbthu/prtgaussian)**|

<p align=right>(<a href=#updated-on-20240818>back to top</a>)</p>

## 3D Reconstruction

|Publish Date|Title|Abstract|PDF|Code|
|---|---|---|---|---|
|**2024-08-15**|**Comparative Evaluation of 3D Reconstruction Methods for Object Pose Estimation**|物体姿态估计对于涉及机器人操纵、导航和增强现实的许多工业应用至关重要。当前的可推广对象姿态估计器，即不需要对每个对象进行训练的方法，依赖于精确的3D模型。主要使用CAD模型，这在实践中很难获得。同时，通常可以获取对象的图像。自然地，这导致了一个问题，即从图像重建的3D模型是否足以促进准确的物体姿态估计。我们的目标是通过提出一个新的基准来衡量3D重建质量对姿态估计精度的影响，从而回答这个问题。我们的基准为对象重建提供了校准图像，这些图像与YCB-V数据集的测试图像进行了配准，用于BOP基准格式下的姿态评估。对多种最先进的3D重建和物体姿态估计方法的详细实验表明，现代重建方法产生的几何形状通常足以进行精确的姿态估计。我们的实验得出了有趣的观察结果：（1）测量3D重建质量的标准指标不一定能指示姿态估计的准确性，这表明需要像我们这样的专用基准。（2） 经典的、非基于学习的方法可以与现代基于学习的重建技术相提并论，甚至可以提供更好的重建时间-姿态精度权衡。（3） 重建模型和CAD模型的性能之间仍存在相当大的差距。为了促进缩小这一差距的研究，我们的基准可在https://github.com/VarunBurde/reconstruction_pose_benchmark}. et.al.|[2408.08234](http://arxiv.org/abs/2408.08234)|**[link](https://github.com/varunburde/reconstruction_pose_benchmark)**|
|**2024-08-15**|**Single-image coherent reconstruction of objects and humans**|从单眼图像重建对象和人类的现有方法存在严重的网格碰撞和交互遮挡对象的性能限制。本文介绍了一种从单个图像中获得交互对象和人的全局一致3D重建的方法。我们的贡献包括：1）一个优化框架，以碰撞损失为特征，专门用于处理人与物体和人与人之间的交互，确保空间连贯的场景重建；以及2）一种利用图像修复来稳健估计6自由度（DOF）姿态的新技术，特别是对于严重遮挡的物体。值得注意的是，我们提出的方法可以有效地处理来自真实场景的图像，而不需要场景或对象级的3D监控。对现有方法的广泛定性和定量评估表明，在具有多个相互作用的人和物体的场景的最终重建中，碰撞显著减少，场景重建更加连贯。 et.al.|[2408.08086](http://arxiv.org/abs/2408.08086)|null|
|**2024-08-14**|**Rethinking the Key Factors for the Generalization of Remote Sensing Stereo Matching Networks**|立体匹配是三维重建的关键步骤，由于其对遥感图像的强特征表示，已经完全转向深度学习。然而，立体匹配任务的地面实况依赖于昂贵的机载激光雷达数据，因此很难获得足够的样本进行监督学习。为了提高立体匹配网络对不同传感器和场景的跨域数据的泛化能力，本文致力于从三个角度研究关键的训练因素。（1） 对于训练数据集的选择，重要的是选择与测试集具有相似区域目标分布的数据，而不是使用来自同一传感器的数据。（2） 对于模型结构，首选灵活适应不同尺寸特征的级联结构。（3） 对于训练方式，无监督方法比有监督方法具有更好的泛化能力，我们设计了一种无监督的早期停止策略，以预训练的权重为基础，帮助保留最佳模型。我们进行了大量的实验来支持之前的发现，在此基础上，我们提出了一种具有良好泛化性能的无监督立体匹配网络。我们在发布源代码和数据集https://github.com/Elenairene/RKF_RSSM复制结果并鼓励未来的工作。 et.al.|[2408.07613](http://arxiv.org/abs/2408.07613)|null|
|**2024-08-13**|**PBIR-NIE: Glossy Object Capture under Non-Distant Lighting**|光滑物体对自然光照下多视图输入图像的3D重建提出了重大挑战。在本文中，我们介绍了PBIR-NIE，这是一个反向渲染框架，旨在全面捕捉此类对象的几何、材质属性和周围照明。我们提出了一种新颖的视差感知非远距离环境图，作为一种轻量级且高效的照明表示，可以准确地模拟场景的近场背景，这在现实世界的捕捉设置中很常见。此功能使我们的框架能够适应超出标准无限距离环境贴图能力的复杂视差效果。我们的方法通过基于物理的可微渲染来优化底层有符号距离场（SDF），通过神经隐式进化（NIE）无缝连接三角形网格和SDF之间的表面梯度。为了解决可微渲染中高光泽BRDF的复杂性，我们集成了对偶采样算法来减轻蒙特卡洛梯度估计器中的方差。因此，我们的框架在处理光滑物体重建方面表现出强大的能力，在几何、重新照明和材料估计方面表现出卓越的质量。 et.al.|[2408.06878](http://arxiv.org/abs/2408.06878)|null|
|**2024-08-13**|**HDRGS: High Dynamic Range Gaussian Splatting**|近年来，从2D图像重建3D领域取得了长足的进步，特别是在引入神经辐射场（NeRF）技术之后。然而，从2D多曝光低动态范围（LDR）图像重建与现实世界条件更接近的3D高动态范围（HDR）辐射场仍然是一个重大挑战。解决这个问题的方法分为两类：基于网格和基于隐式。使用多层感知器（MLP）的隐式方法面临效率低下、可解性有限和过拟合风险。相反，基于网格的方法需要大量的内存，并且在图像质量和长时间训练方面存在困难。在本文中，我们将高斯散斑（Gaussian Splatting）——一种最新的、高质量的、实时的3D重建技术引入到这个领域。我们进一步开发了高动态范围高斯散斑（HDR-GS）方法，旨在解决上述挑战。该方法通过包含亮度来增强颜色维度，并使用非对称网格进行色调映射，快速准确地将像素辐照度转换为颜色。我们的方法提高了HDR场景恢复的准确性，并集成了一种新颖的从粗到细的策略来加速模型收敛，增强了对稀疏视点和曝光极端的鲁棒性，并防止了局部最优。广泛的测试证实，我们的方法在合成和现实世界场景中都超越了当前最先进的技术。代码将在\url发布{https://github.com/WuJH2001/HDRGS} et.al.|[2408.06543](http://arxiv.org/abs/2408.06543)|**[link](https://github.com/wujh2001/hdrgs)**|
|**2024-08-12**|**3D Reconstruction of Protein Structures from Multi-view AFM Images using Neural Radiance Fields (NeRFs)**|最近在预测3D蛋白质结构的深度学习方面取得的进展显示出了希望，特别是在利用蛋白质序列和冷冻电子显微镜（Cryo-EM）图像等输入时。然而，在预测涉及多种蛋白质的蛋白质复合物（PC）的结构时，这些技术往往不足。在我们的研究中，我们研究了使用原子力显微镜（AFM）结合深度学习来预测PC的3D结构。AFM生成高度图，描绘了各种随机方向的PC，为训练神经网络预测3D结构提供了丰富的信息。然后，我们使用预训练的UpFusion模型（利用条件扩散模型来合成新视图）来训练特定于实例的NeRF模型进行3D重建。UpFusion的性能通过使用AFM图像对3D蛋白质结构进行零样本预测来评估。然而，挑战在于收集实际AFM图像的时间密集性和不切实际性。为了解决这个问题，我们使用了一种虚拟AFM成像过程，通过体绘制技术将“PDB”蛋白质文件转换为多视图2D虚拟AFM图像。我们使用虚拟和实际的多视图AFM图像广泛验证了UpFusion架构。我们的结果包括用不同数量的视图和不同的视图集预测的结构的比较。这种新方法具有通过进一步微调UpFusion网络来提高蛋白质复合物结构预测准确性的巨大潜力。 et.al.|[2408.06244](http://arxiv.org/abs/2408.06244)|null|
|**2024-08-12**|**Developing Smart MAVs for Autonomous Inspection in GPS-denied Constructions**|智能微型飞行器（MAV）通过在施工的各个阶段（包括难以到达的地区）进行高效、高分辨率的监测，改变了基础设施检查。在工业设施和基础设施等GPS不可用的环境中，无人机的传统手动操作是劳动密集型、繁琐且容易出错的。这项研究为在如此复杂和GPS不可用的室内环境中进行智能MAV检查提供了一个创新的框架。该框架具有一个分层感知和规划系统，可以识别感兴趣的区域并优化任务路径。它还提供了一种先进的MAV系统，具有增强的定位和运动规划能力，与神经重建技术集成，可对建筑结构进行全面的3D重建。该框架的有效性在一个4000平方米的室内基础设施中得到了实证验证，该设施的内部长度为80米，宽度为50米，高度为7米。主体结构由柱和墙组成。实验结果表明，我们的MAV系统在自主检测任务中表现出色，在生成和执行扫描路径方面实现了100%的成功率。广泛的实验验证了我们开发的MAV的机动性，在运动规划方面实现了100%的成功率，跟踪误差小于0.1米。此外，使用3D高斯散斑技术的增强重建方法能够从采集的数据中生成高保真渲染模型。总的来说，我们的新方法代表了在基础设施检查中使用机器人技术的重大进步。 et.al.|[2408.06030](http://arxiv.org/abs/2408.06030)|null|
|**2024-08-10**|**Visual SLAM with 3D Gaussian Primitives and Depth Priors Enabling Novel View Synthesis**|传统的基于几何的SLAM系统缺乏密集的3D重建能力，因为它们的数据关联通常依赖于特征对应。此外，基于学习的SLAM系统在实时性能和准确性方面往往不足。平衡实时性能和密集的3D重建能力是一个具有挑战性的问题。在本文中，我们提出了一种实时RGB-D SLAM系统，该系统结合了一种新的视图合成技术——3D高斯散点，用于3D场景表示和姿态估计。该技术利用了具有光栅化的3D高斯散斑的实时渲染性能，并允许通过CUDA实现实时可微优化。我们还支持从3D高斯网格重建显式密集3D重建。为了估计精确的相机姿态，我们采用了一种具有逆优化的旋转-平移解耦策略。这涉及通过基于梯度的优化在几次迭代中迭代更新两者。该过程包括可微分地渲染RGB、深度和轮廓图，并更新相机参数，以最小化现有3D高斯图的光度损失、深度几何损失和可见度损失的组合损失。然而，由于3D高斯分布的多视图不一致性，3D高斯散布（3DGS）难以准确表示曲面，这可能会导致相机姿态估计和场景重建的精度降低。为了解决这个问题，我们利用深度先验作为额外的正则化来强制执行几何约束，从而提高了姿态估计和3D重建的精度。我们还提供了关于公共基准数据集的广泛实验结果，以证明我们提出的方法在姿态精度、几何精度和渲染性能方面的有效性。 et.al.|[2408.05635](http://arxiv.org/abs/2408.05635)|null|
|**2024-08-10**|**CryoBench: Diverse and challenging datasets for the heterogeneity problem in cryo-EM**|低温电子显微镜（Cryo-EM）是一种从成像数据中确定高分辨率3D生物分子结构的强大技术。由于该技术可以捕获动态生物分子复合物，因此越来越多地开发了3D重建方法来解决这种内在的结构异质性。然而，缺乏具有地面实况结构和验证指标的标准化基准限制了该领域的进步。在这里，我们提出了CryoBench，这是一套用于冷冻-EM中异构重建的数据集、指标和性能基准。我们提出了五个数据集，代表了不同的异构来源和难度。这些包括由抗体复合物的简单运动和随机配置以及从分子动力学模拟中取样的数万个结构产生的构象异质性。我们还设计了包含核糖体组装状态混合物和细胞中存在的100种常见复合物组成异质性的数据集。然后，我们对最先进的异构重建工具进行了全面分析，包括神经和非神经方法及其对噪声的敏感性，并提出了定量比较方法的新指标。我们希望这个基准将成为分析低温EM和机器学习社区现有方法和新算法开发的基础资源。 et.al.|[2408.05526](http://arxiv.org/abs/2408.05526)|null|
|**2024-08-10**|**Mesh deformation-based single-view 3D reconstruction of thin eyeglasses frames with differentiable rendering**|在虚拟现实（VR）和增强现实（AR）技术的支持下，3D虚拟眼镜试穿应用正在成为一种新的趋势解决方案，它提供了一种“试穿”选项，可以在舒适的家中选择完美的眼镜。由于缺乏足够的纹理特征、元素薄和严重的自遮挡等独特特征，使用传统的基于深度和图像的方法从单个图像重建眼镜架是极其困难的。在这篇论文中，我们提出了第一个基于网格变形的重建框架，利用先验知识和领域特定知识，从单个RGB图像中恢复高精度的3D全框眼镜模型。具体来说，基于合成眼镜架数据集的构建，我们首先定义了一个具有预定义关键点的特定类别眼镜架模板。然后，给定一个结构薄、纹理特征少的输入眼镜架图像，我们设计了一个关键点检测器和细化器，以从粗到细的方式检测预定义的关键点，从而准确估计相机姿态。之后，使用可微渲染，我们提出了一种新的优化方法，通过在模板网格上逐步执行自由变形（FFD）来生成正确的几何体。我们定义了一系列损失函数，利用固有结构、轮廓、关键点、每像素阴影信息等的约束，增强渲染结果与相应RGB输入之间的一致性。合成数据集和真实图像的实验结果证明了所提出算法的有效性。 et.al.|[2408.05402](http://arxiv.org/abs/2408.05402)|null|

<p align=right>(<a href=#updated-on-20240818>back to top</a>)</p>

## Diffusion

|Publish Date|Title|Abstract|PDF|Code|
|---|---|---|---|---|
|**2024-08-15**|**Understanding the Local Geometry of Generative Model Manifolds**|深度生成模型在训练过程中使用有限数量的样本学习复杂数据流形的连续表示。对于预训练的生成模型，评估所学习流形表示质量的常用方法是使用大量生成和真实样本计算全局度量，如Fr’echet Inception Distance。然而，生成模型的性能在整个学习流形上并不均匀，例如，对于稳定扩散等\textit{基础模型}，生成性能可能会根据被去噪的条件或初始噪声向量而发生显著变化。本文研究了\textit{学习流形的局部几何}与下游生成之间的关系。基于连续分段线性（CPWL）生成器理论，我们使用三个几何描述符——缩放（ $\psi$）、秩（$\nu$）和复杂性（$\delta$ ）——来局部表征预训练的生成模型流形。我们提供了定量和定性证据，表明对于给定的潜在因素，局部描述符与世代美学、人工制品、不确定性甚至记忆有关。最后，我们证明了在局部几何上训练\textit{reward模型}可以控制所学习分布下生成样本的可能性。 et.al.|[2408.08307](http://arxiv.org/abs/2408.08307)|null|
|**2024-08-15**|**Accelerated Image-Aware Generative Diffusion Modeling**|本文提出了一种新的扩散模型的解析构造，其漂移和扩散参数在正向过程中产生指数时间衰减的信噪比。相反，该构造巧妙地使用自动编码器在干净图像的结构上学习扩散系数。所提出的方法显著加速了扩散过程，将所需的扩散时间步长从传统模型中的约1000个减少到200-500个，而不会影响反向时间扩散中的图像质量。与通常使用耗时的多次运行的传统模型不同，我们引入了一个并行数据驱动模型，在模型的单次运行中生成逆时间扩散轨迹。由此产生的集体块序列生成模型消除了基于MCMC的子采样校正的需要，以保护和提高图像质量，从而进一步提高图像生成的速度。总的来说，这些进步产生了一个比传统方法快一个数量级的生成模型，同时保持了生成图像的高保真度和多样性，因此有望在快速图像合成任务中得到广泛应用。 et.al.|[2408.08306](http://arxiv.org/abs/2408.08306)|null|
|**2024-08-15**|**Solutions and stochastic averaging for delay-path-dependent stochastic variational inequalities in infinite dimensions**|在本文中，我们研究了一个非常普遍的随机变分不等式（SVI），它在无限维中具有跳跃、随机系数、延迟和路径依赖性。在非Lipschitz条件下，建立了解的存在性和唯一性的适定性，并得到了时间爆炸SVI强收敛到平均方程的随机平均原理。我们分别在有限维和无限维的一般但具体的例子上说明了我们的结果，这些例子涵盖了具有静电排斥的大类粒子系统、具有跳跃的非线性随机偏微分方程、具有延迟的半线性随机偏微分微分方程（特别是随机反应扩散方程）等。 et.al.|[2408.08277](http://arxiv.org/abs/2408.08277)|null|
|**2024-08-15**|**Derivative-Free Guidance in Continuous and Discrete Diffusion Models with Soft Value-Based Decoding**|扩散模型擅长捕捉图像、分子、DNA、RNA和蛋白质序列的自然设计空间。然而，我们的目标不是仅仅生成自然的设计，而是优化下游的奖励函数，同时保持这些设计空间的自然性。实现这一目标的现有方法通常需要“可微分”的代理模型（\textit{例如}，分类器引导或DPS），或者涉及对扩散模型进行计算上昂贵的微调（\textit{例如}、无分类器引导、基于RL的微调）。在我们的工作中，我们提出了一种应对这些挑战的新方法。我们的算法是一种迭代采样方法，它将软值函数集成到预训练扩散模型的标准推理过程中，软值函数预测了中间噪声状态如何在未来带来高回报。值得注意的是，我们的方法避免了对生成模型进行微调，并消除了构建可微模型的需要。这使我们能够（1）直接利用许多科学领域中常用的不可微特征/奖励反馈，以及（2）以有原则的方式将我们的方法应用于最近的离散扩散模型。最后，我们展示了我们的算法在多个领域的有效性，包括图像生成、分子生成和DNA/RNA序列生成。该代码可在\href处获得{https://github.com/masa-ue/SVDD}{https://github.com/masa-ue/SVDD}. et.al.|[2408.08252](http://arxiv.org/abs/2408.08252)|null|
|**2024-08-15**|**Probing hydrodynamic crossovers with dissipation-assisted operator evolution**|利用人工耗散来抑制纠缠增长，我们绘制了不同U（1）电荷密度的通用相互作用晶格模型中扩散的出现。我们在散射长度设定的尺度上追踪从弹道到扩散传输的交叉，发现直观的结果是，在低密度下，扩散常数的尺度为 $D\propto 1/\rho$ 。我们的数值方法推广了耗散辅助算子进化（DAOE）算法：本着BBGKY层次结构的精神，我们通过非局部算子的集合平均值有效地近似了它们，而不是完全丢弃它们。这大大降低了算子纠缠熵，同时仍然对所有密度尺度上的扩散常数进行了准确的预测。我们进一步构建了输运交叉的最小模型，得到了与我们的数值数据非常吻合的电荷相关函数。我们的结果阐明了守恒密度对流体动力学相关函数的主要贡献，并为低温输运的推广提供了指导。 et.al.|[2408.08249](http://arxiv.org/abs/2408.08249)|null|
|**2024-08-15**|**Not Every Image is Worth a Thousand Words: Quantifying Originality in Stable Diffusion**|这项工作解决了文本到图像（T2I）生成扩散模型中量化原创性的挑战，重点是版权原创性。我们首先通过受控实验评估T2I模型的创新和推广能力，揭示稳定的扩散模型可以有效地用足够多样化的训练数据重建看不见的元素。然后，我们的关键见解是，模型熟悉的、在训练过程中看到的图像元素的概念和组合在模型的潜在空间中得到了更简洁的表示。因此，我们提出了一种利用文本反转的方法，根据模型重建图像所需的标记数量来衡量图像的原创性。我们的方法受到原创性法律定义的启发，旨在评估模型是否可以在不依赖特定提示或模型训练数据的情况下产生原创内容。我们使用预训练的稳定扩散模型和合成数据集来演示我们的方法，显示了标记数量与图像原创性之间的相关性。这项工作有助于理解生成模型中的原创性，并对版权侵权案件产生影响。 et.al.|[2408.08184](http://arxiv.org/abs/2408.08184)|null|
|**2024-08-15**|**Study of non-diffusive thermal behaviors in nanoscale transistors under different heating strategies**|了解声子输运机制并有效捕获温度的时空分布对于缓解电子器件中的热点问题具有重要意义。之前的大多数模拟主要集中在连续加热的稳态问题上，有效的傅里叶定律（EFL）因其简单高效而被广泛应用于实际的多尺度热工程，尽管它仍然遵循扩散规则。然而，非连续加热在电子设备中更为常见，很少有比较研究来估计EFL会产生多大的偏差。为了回答上述问题，在三种加热策略下，即“连续”、“间歇”和“交替”加热，通过声子玻尔兹曼输运方程（BTE）研究了纳米级体或绝缘体上硅（SOI）晶体管中的热传导。准二维或三维热点系统的数值结果表明，EFL不容易准确捕捉微/纳米尺度的热传导，特别是在热点区域附近。不同的加热策略对温升和瞬态散热过程有很大影响。与“间歇”加热相比，“交替”加热的温度变化较小。 et.al.|[2408.08120](http://arxiv.org/abs/2408.08120)|null|
|**2024-08-15**|**Exploring Uncertainty Visualization for Degenerate Tensors in 3D Symmetric Second-Order Tensor Field Ensembles**|对称二阶张量在各种科学和工程领域都是基础的，因为它们可以表示脑组织中的材料应力或扩散过程等特性。近年来，已经引入并改进了几种方法来使用拓扑特征分析这些场，例如退化张量位置，即张量具有重复的特征值或法向曲面。传统上，此类特征的识别仅限于单个张量场。然而，创建集成来解释模拟和测量中的不确定性和可变性已经变得很常见。在这项工作中，我们探索了描述和可视化三维对称二阶张量场系综中退化张量位置的新方法。我们基于张量模式进行考虑，并分析了它在表征退化张量位置的不确定性方面的实用性，然后提出了各种可视化策略来有效地传达退化张量信息。我们展示了合成和模拟数据集的技术。结果表明，对不确定性的不同描述的相互作用可以有效地传达简并张量位置的信息。 et.al.|[2408.08099](http://arxiv.org/abs/2408.08099)|null|
|**2024-08-15**|**Transport and mixing in control volumes through the lens of probability**|推导了一个偏微分方程，该方程控制着从控制体积中随机提取的任意数量的局部流量观测值的联合概率分布的全局演化，并将其应用于涉及不可逆混合的示例。与局部概率密度方法不同，这项工作采用了全局积分的视角，将控制体积视为样本空间。这样做可以使散度定理用于揭示联合概率分布演化方程中不确定或随机边界通量和内部交叉梯度混合的贡献。穿过控制体积边界的平流和扩散分别产生源项和漂移项，而内部混合通常对应于概率密度的符号不定扩散。识别并详细讨论了相应扩散系数为半负定的几种典型情况。全球联合概率视角是可用势能的自然环境，也是将不确定性纳入散装、体积综合、运输和混合模型的自然环境。通过将坐标函数视为可观测值，可以很容易地获得空间中的细粒度信息。通过扩展，该框架可以应用于任意大小的交互控制体积的网络。 et.al.|[2408.08028](http://arxiv.org/abs/2408.08028)|null|
|**2024-08-15**|**Gravitational Lensing Reveals Cool Gas within 10-20 kpc around a Quiescent Galaxy**|虽然与恒星形成星系相比，静止星系的外环星系介质（CGM）中有相当数量的冷气体，但它们的星际气体要少得多。然而，导致星系停止形成恒星并保持静止的过程仍然存在悬而未决的问题。理论表明，与热日冕的动态相互作用阻止了冷气体到达星系，因此预测静止星系CGM的内部区域没有冷气体。然而，由于类星体视线方法缺乏空间信息，人们对CGM的内部区域缺乏了解。我们提出了一种积分场光谱法，使用引力透镜恒星形成星系探测一个巨大的静止星系周围的10-20~kpc（2.4-4.8 R\textsubscript{e}）。我们检测到镁（MgII）的吸收，这意味着大量的冷原子气体（10\text上标{8.4}-10\text上标{0.3}M\text下标{ $\odot$}，T$\sim$ 10\text上标{14}开尔文），其数量与恒星形成星系相当。哈勃成像的透镜建模还揭示了一个与MgII吸收的空间范围一致的重要质量的漫射不对称成分，并偏离了星系的光分布。这项研究证明了星系级引力透镜的力量，它不仅可以探测星系周围的气体，还可以由于引力效应独立探测CGM的质量。 et.al.|[2408.07984](http://arxiv.org/abs/2408.07984)|null|

<p align=right>(<a href=#updated-on-20240818>back to top</a>)</p>

## NeRF

|Publish Date|Title|Abstract|PDF|Code|
|---|---|---|---|---|
|**2024-08-10**|**Scene123: One Prompt to 3D Scene Generation via Video-Assisted and Consistency-Enhanced MAE**|随着人工智能生成内容（AIGC）的进步，已经开发了各种方法来从单模式或多模式输入生成文本、图像、视频和3D对象，从而有助于模拟类人认知内容的创建。然而，由于确保模型生成的外推视图之间的一致性所涉及的复杂性，从单个输入生成逼真的大规模场景是一个挑战。受益于最新的视频生成模型和隐式神经表示，我们提出了Scene123，这是一种3D场景生成模型，它不仅通过视频生成框架确保了真实性和多样性，还使用隐式神经场与掩模自编码器（MAE）相结合，有效地确保了视图中看不见区域的一致性。具体来说，我们最初会扭曲输入图像（或从文本生成的图像）以模拟相邻的视图，用MAE模型填充不可见的区域。然而，这些填充图像通常无法保持视图一致性，因此我们利用产生的视图来优化神经辐射场，增强几何一致性。此外，为了进一步增强生成视图的细节和纹理保真度，我们对通过视频生成模型从输入图像中导出的图像采用了基于GAN的Loss。大量实验表明，我们的方法可以从单个提示中生成逼真一致的场景。定性和定量结果都表明，我们的方法超越了现有的最先进的方法。我们展示鼓励视频示例https://yiyingyang12.github.io/Scene123.github.io/. et.al.|[2408.05477](http://arxiv.org/abs/2408.05477)|null|
|**2024-08-07**|**Compact 3D Gaussian Splatting for Static and Dynamic Radiance Fields**|3D高斯飞溅（3DGS）最近成为一种替代表示，它利用基于3D高斯的表示并引入了近似的体积渲染，实现了非常快的渲染速度和有前景的图像质量。此外，后续的研究已成功地将3DGS扩展到动态3D场景，展示了其广泛的应用。然而，由于3DGS及其后续方法需要大量的高斯分布来保持渲染图像的高保真度，这需要大量的内存和存储，因此出现了一个重大的缺点。为了解决这个关键问题，我们特别强调两个关键目标：在不牺牲性能的情况下减少高斯点的数量，以及压缩高斯属性，如视图相关的颜色和协方差。为此，我们提出了一种可学习的掩码策略，该策略在保持高性能的同时显著减少了高斯数。此外，我们提出了一种紧凑但有效的视图相关颜色表示方法，即采用基于网格的神经场，而不是依赖球谐函数。最后，我们学习码本，通过残差矢量量化来紧凑地表示几何和时间属性。通过量化和熵编码等模型压缩技术，我们始终表明，与静态场景的3DGS相比，存储空间减少了25倍以上，渲染速度提高了25倍，同时保持了场景表示的质量。对于动态场景，与现有的最先进方法相比，我们的方法实现了超过12倍的存储效率，并保留了高质量的重建。我们的工作为3D场景表示提供了一个全面的框架，实现了高性能、快速训练、紧凑性和实时渲染。我们的项目页面可在https://maincold2.github.io/c3dgs/. et.al.|[2408.03822](http://arxiv.org/abs/2408.03822)|null|
|**2024-08-07**|**PRTGS: Precomputed Radiance Transfer of Gaussian Splats for Real-Time High-Quality Relighting**|我们提出了高斯斑点的预计算辐射转移（PRTGS），这是一种在低频照明环境中用于高斯斑点的实时高质量重新照明方法，通过预计算3D高斯斑点的辐射转移来捕获柔和的阴影和相互反射。现有的研究表明，在动态照明场景中，3D高斯溅射（3DGS）的效率优于神经场。然而，目前基于3DGS的重新照明方法仍然难以实时计算动态光的高质量阴影和间接照明，导致渲染结果不切实际。我们通过预先计算复杂传递函数（如阴影）所需的昂贵传输模拟来解决这个问题，得到的传递函数表示为每个高斯斑点的密集向量集或矩阵集。我们介绍了针对训练和渲染阶段量身定制的不同预计算方法，以及针对3D高斯斑点的独特光线追踪和间接照明预计算技术，以加快训练速度并计算与环境光相关的准确间接照明。实验分析表明，我们的方法在保持有竞争力的训练时间的同时实现了最先进的视觉质量，并允许以1080p分辨率对动态光和相对复杂的场景进行高质量的实时（30+fps）重新照明。 et.al.|[2408.03538](http://arxiv.org/abs/2408.03538)|null|
|**2024-08-01**|**Neural Octahedral Field: Octahedral prior for simultaneous smoothing and sharp edge regularization**|神经隐式表示，将距离函数参数化为坐标神经场，已成为解决无方向点云表面重建的有前景的前沿。为了确保方向一致，现有的方法侧重于正则化距离函数的梯度，例如将其约束为单位范数，最小化其散度，或将其与对应于零特征值的Hessian特征向量对齐。然而，在存在大扫描噪声的情况下，它们往往要么过拟合噪声输入，要么产生过于平滑的重建。在这项工作中，我们建议利用六面体网格中产生的八面体框架的球谐表示，在一种新的神经场变体——八面体场下指导曲面重建。当约束为平滑时，该字段会自动捕捉到几何特征，并在折痕上插值时自然保留锐角。通过同时拟合和平滑隐式几何旁边的八面体场，它的行为类似于双边滤波，从而在保持锐边的同时实现平滑重建。尽管是纯逐点操作，但我们的方法在广泛的实验中表现优于各种传统和神经方法，并且与需要正常和数据先验的方法非常有竞争力。我们的全面实施可在以下网址获得：https://github.com/Ankbzpx/frame-field. et.al.|[2408.00303](http://arxiv.org/abs/2408.00303)|**[link](https://github.com/ankbzpx/frame-field)**|
|**2024-07-30**|**Neural Fields for Continuous Periodic Motion Estimation in 4D Cardiovascular Imaging**|时间分辨三维血流MRI（4D血流MRI）提供了一种独特的非侵入性解决方案，用于可视化和量化主动脉弓等血管中的血流动力学。然而，由于难以获得完整的周期分割，目前大多数动脉4D血流MRI分析方法使用静态动脉壁。为了克服这一局限性，我们提出了一种基于神经场的方法，可以直接估计整个心动周期中连续的周期性壁变形。对于3D+时间成像数据集，我们优化了表示时间依赖速度矢量场（VVF）的隐式神经表示（INR）。ODE求解器用于将VVF集成到变形矢量场（DVF）中，该矢量场可以随着时间的推移使图像、分割掩模或网格变形，从而可视化和量化局部壁运动模式。为了正确反映3D+时间心血管数据的周期性，我们以两种方式施加周期性。首先，通过定期对输入到INR的时间进行编码，从而对VVF进行编码。其次，通过规范DVF。我们证明了这种方法在不同周期模式的合成数据、心电图门控CT和4D血流MRI数据上的有效性。所获得的方法可用于改进4D血流MRI分析。 et.al.|[2407.20728](http://arxiv.org/abs/2407.20728)|null|
|**2024-07-29**|**Aero-Nef: Neural Fields for Rapid Aircraft Aerodynamics Simulations**|本文提出了一种基于隐式神经表示（INR）在网格域上学习稳态流体动力学模拟替代模型的方法。所提出的模型可以直接应用于不同流动条件下的非结构化域，处理非参数3D几何变化，并推广到测试时看不见的形状。基于坐标的公式自然会导致离散化的鲁棒性，从而在计算成本（内存占用和训练时间）和精度之间实现了极好的权衡。该方法在两个工业相关应用中得到了验证：跨音速翼型上二维可压缩流的RANS数据集和三维机翼上表面压力分布的数据集，包括形状、流入条件和控制表面偏转变化。在所考虑的测试用例中，与最先进的图神经网络架构相比，我们的方法实现了三倍多的测试误差，并显著改善了看不见的几何形状的泛化误差。值得注意的是，该方法在RANS跨音速翼型数据集上的推理速度比高保真求解器快五个数量级。代码可在以下网址获得https://gitlab.isae-supaero.fr/gi.catalani/aero-nepf et.al.|[2407.19916](http://arxiv.org/abs/2407.19916)|null|
|**2024-07-26**|**ObjectCarver: Semi-automatic segmentation, reconstruction and separation of 3D objects**|隐式神经场在从多幅图像重建3D表面方面取得了显著进展；然而，在分离场景中的单个对象时，他们遇到了挑战。之前的工作试图通过引入一个框架来解决这个问题，该框架为N个对象中的每一个同时训练单独的带符号距离场（SDF），并使用正则化项来防止对象重叠。然而，所有这些方法都需要提供分割掩模，这并不总是容易获得的。我们介绍了我们的方法ObjectCarver，来解决在单个视图中从点击输入中分离对象的问题。给定摆出的多视图图像和一组用户输入点击来提示分割单个对象，我们的方法将场景分解为单独的对象，并为每个对象重建高质量的3D表面。我们引入了一个损失函数，可以防止漂浮物，避免因遮挡而造成不适当的雕刻。此外，我们引入了一种新的场景初始化方法，与之前的方法相比，该方法在保留几何细节的同时显著加快了过程。尽管不需要地面真实掩模或单眼线索，但我们的方法在定性和定量上都优于基线。此外，我们引入了一个新的基准数据集进行评估。 et.al.|[2407.19108](http://arxiv.org/abs/2407.19108)|null|
|**2024-07-24**|**Neural field equations with time-periodic external inputs and some applications to visual processing**|这项工作的目的是为研究视觉处理任务中的闪烁输入提供一个数学框架。当与几何图案结合时，这些输入会影响并诱发有趣的心理物理现象，如麦凯效应和比洛克-邹效应，在这些效应中，受试者感知到通常由闪烁频率调制的特定余像。由于输入的对称破缺结构，经典分叉理论和多尺度分析技术在我们的背景下不是很有效。因此，我们采用了一种基于Amari型神经场控制理论的输入-输出框架的方法。这使我们能够证明，当受到周期性输入的驱动时，动态会收敛到周期性状态。此外，我们研究了在哪些假设下，这些非线性动力学可以有效地线性化，在这种情况下，我们提出了短程兴奋性和远程抑制性神经元相互作用的积分核的精确近似值。最后，对于集中在具有闪烁背景的视野中心的输入，我们直接将余像中出现的虚幻轮廓的宽度与闪烁频率和抑制强度联系起来。 et.al.|[2407.17294](http://arxiv.org/abs/2407.17294)|null|
|**2024-07-23**|**Fluorescence Diffraction Tomography using Explicit Neural Fields**|从荧光图像中求解3D折射率（RI）可以提供有关生物样本的荧光和相位信息。然而，在大体积、高分辨率和反射模式下准确检索部分相干光的相位以重建无标签相位物体的未知RI仍然具有挑战性。为了应对这一挑战，我们开发了具有显式神经场的荧光衍射断层扫描（FDT），可以从散焦荧光散斑图像重建3D RI。使用FDT成功重建3D RI依赖于四个关键组件：粗到细建模、自校准、差分多层渲染模型和部分相干掩模。具体而言，显式表示与粗到细建模有效地集成在一起，以实现高速、高分辨率的重建。此外，我们将多层方程推进到微分多层渲染模型，这使得系统的外部和内部参数能够进行自校准。自校准有助于高精度的正向图像预测和RI重建。部分相干掩模是数字掩模，用于准确有效地解决相干光模型和部分相干光数据之间的差异。FDT成功地从荧光图像中重建了24个z $层上1024$×1024像素的530$×530$×300$μm^3$ 体积的3D培养无标记3D MuSCs管的RI，证明了在体外对体积庞大和异质的生物样本进行高保真3D RI重建。 et.al.|[2407.16657](http://arxiv.org/abs/2407.16657)|null|
|**2024-07-22**|**Iterative approach to reconstructing neural disparity fields from light-field data**|本研究提出了一种神经视差场（NDF），该场基于神经场建立了场景视差的隐式连续表示，并采用迭代方法解决了从光场数据重建NDF的逆问题。NDF能够无缝和精确地表征三维场景中的视差变化，并可以以任何任意分辨率对视差进行离散化，克服了传统视差图容易出现采样误差和插值不准确的局限性。所提出的NDF网络架构利用哈希编码结合多层感知器来捕获纹理级别的详细差异，从而增强其表示复杂场景几何信息的能力。通过利用光场数据中固有的空间角度一致性，开发了一种可微分正向模型，用于从光场数据生成中心视图图像。基于正向模型，建立了一种使用可微传播算子的NDF重建逆问题的优化方案。此外，在优化方案中，采用迭代求解方法重建NDF，该方法不需要训练数据集，适用于各种采集方法捕获的光场数据。实验结果表明，使用所提出的方法可以从光场数据中重建高质量的NDF。NDF可以有效地恢复高分辨率视差，证明了其隐式、连续表示场景视差的能力。 et.al.|[2407.15380](http://arxiv.org/abs/2407.15380)|null|

<p align=right>(<a href=#updated-on-20240818>back to top</a>)</p>

[contributors-shield]: https://img.shields.io/github/contributors/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[contributors-url]: https://github.com/Vincentqyw/cv-arxiv-daily/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[forks-url]: https://github.com/Vincentqyw/cv-arxiv-daily/network/members
[stars-shield]: https://img.shields.io/github/stars/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[stars-url]: https://github.com/Vincentqyw/cv-arxiv-daily/stargazers
[issues-shield]: https://img.shields.io/github/issues/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[issues-url]: https://github.com/Vincentqyw/cv-arxiv-daily/issues

