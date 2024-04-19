[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]

## Updated on 2024.04.19
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
|**2024-04-18**|**AG-NeRF: Attention-guided Neural Radiance Fields for Multi-height Large-scale Outdoor Scene Rendering**|现有的基于神经辐射场（NeRF）的大型户外场景新视图合成方法主要建立在单一海拔上。此外，它们通常需要先验的相机拍摄高度和场景范围，导致在相机高度变化时应用效率低下且不切实际。在这项工作中，我们提出了一个端到端的框架，称为AG-NeRF，并试图通过基于不同高度的场景合成自由视点图像来降低构建良好重建的训练成本。具体而言，为了解决从低空（无人机级）到高空（卫星级）的细节变化问题，开发了一种源图像选择方法和基于注意力的特征融合方法，从多高度图像中提取和融合目标视图的最相关特征，以实现高保真渲染。大量实验表明，AG NeRF在56个Leonard和Transamerica基准上实现了SOTA性能，与最新的BungieNeRF相比，只需要半小时的训练时间就可以达到有竞争力的PSNR。 et.al.|[2404.11897](http://arxiv.org/abs/2404.11897)|null|
|**2024-04-17**|**Factorized Motion Fields for Fast Sparse Input Dynamic View Synthesis**|设计用于快速优化和渲染的动态场景的3D表示是一项具有挑战性的任务。虽然最近的显式表示能够快速学习和渲染动态辐射场，但它们需要一组密集的输入视点。在这项工作中，我们专注于学习具有稀疏输入视点的动态辐射场的快速表示。然而，具有稀疏输入的优化是受约束不足的，并且需要使用运动先验来约束学习。现有的快速动态场景模型没有明确地对运动进行建模，这使得它们很难用运动先验进行约束。我们设计了一个显式运动模型作为因子分解的4D表示，它是快速的，可以利用运动场的时空相关性。然后，我们引入可靠的流先验，包括跨相机的稀疏流先验和相机内的密集流先验的组合，以正则化我们的运动模型。我们的模型快速、紧凑，在具有稀疏输入视点的流行多视图动态场景数据集上实现了非常好的性能。我们模型的源代码可以在我们的项目页面上找到：https://nagabhushansn95.github.io/publications/2024/RF-DeRF.html. et.al.|[2404.11669](http://arxiv.org/abs/2404.11669)|null|
|**2024-04-17**|**InFusion: Inpainting 3D Gaussians via Learning Depth Completion from Diffusion Prior**|3D高斯最近已经成为新颖视图合成的有效表示。这项工作研究了它的可编辑性，特别关注修复任务，该任务旨在用额外的点来补充一组不完整的3D高斯，以实现视觉和谐的渲染。与2D修复相比，修复3D高斯的关键是找出引入点的渲染相关属性，其优化很大程度上得益于它们的初始3D位置。为此，我们建议使用图像条件深度完成模型来指导点初始化，该模型学习基于观察到的图像直接恢复深度图。这样的设计允许我们的模型以与原始深度一致的比例填充深度值，并利用大规模扩散先验的强大可推广性。由于更准确的深度完成，我们的方法被称为InFusion，在各种复杂场景下以足够好的保真度和效率超越了现有的替代方案。我们进一步证明了InFusion在几个实际应用中的有效性，例如使用用户特定纹理或新的对象插入进行修复。 et.al.|[2404.11613](http://arxiv.org/abs/2404.11613)|null|
|**2024-04-18**|**DeblurGS: Gaussian Splatting for Camera Motion Blur**|尽管在从运动模糊图像重建清晰的3D场景方面取得了重大进展，但向现实世界应用的过渡仍然具有挑战性。主要障碍源于严重的模糊，这导致通过“运动结构”获取初始相机姿势的不准确，这是以前的方法经常忽略的一个关键方面。为了应对这一挑战，我们提出了DeblurGS，这是一种从运动模糊图像中优化清晰的3D高斯飞溅的方法，即使在有噪声的相机姿态初始化的情况下也是如此。我们通过利用3D高斯飞溅的卓越重建能力来恢复细粒度的清晰场景。我们的方法估计每个模糊观测的6自由度相机运动，并为优化过程合成相应的模糊渲染。此外，我们提出了高斯密集退火策略，以防止在相机运动仍然不精确的早期训练阶段，在错误的位置产生不精确的高斯。综合实验表明，我们的DeblurGS在真实世界和合成基准数据集以及现场捕捉的模糊智能手机视频的去模糊和新颖视图合成方面实现了最先进的性能。 et.al.|[2404.11358](http://arxiv.org/abs/2404.11358)|null|
|**2024-04-17**|**Novel View Synthesis for Cinematic Anatomy on Mobile and Immersive Displays**|3D解剖的交互式真实感可视化（即电影解剖）用于医学教育，以解释人体结构。目前，它仅限于正面教学场景，演示者需要强大的GPU和对数据集所在的大型存储设备的高速访问。我们展示了通过压缩的3D高斯飞溅使用新颖的视图合成来克服这一限制，并使学生能够在轻量级移动设备和虚拟现实环境中进行电影解剖。我们提出了一种自动方法来寻找一组图像，这些图像可以捕捉数据中所有潜在的可见结构。通过将特写视图与远处的图像混合，飞溅表示可以恢复高达体素分辨率的结构。Mip Splatting的使用可以在焦距增加时实现平滑过渡。即使是GB数据集，最终的可渲染表示通常也可以压缩到70 MB以下，从而可以使用光栅化在低端设备上进行交互式渲染。 et.al.|[2404.11285](http://arxiv.org/abs/2404.11285)|null|
|**2024-04-16**|**Gaussian Opacity Fields: Efficient and Compact Surface Reconstruction in Unbounded Scenes**|最近，3D高斯散射（3DGS）展示了令人印象深刻的新颖视图合成结果，同时允许实时渲染高分辨率图像。然而，由于3D高斯的显式和非连通性，利用3D高斯进行表面重建带来了重大挑战。在这项工作中，我们提出了高斯不透明度场（GOF），这是一种在无界场景中进行高效、高质量和紧凑表面重建的新方法。我们的GOF源于基于射线追踪的三维高斯体绘制，通过识别其水平集，可以直接从三维高斯中提取几何体，而无需像以前的工作中那样采用泊松重建或TSDF融合。我们将高斯的表面法线近似为射线-高斯相交平面的法线，从而可以应用正则化，显著增强几何体。此外，我们开发了一种利用行进四面体的有效几何提取方法，其中四面体网格是从3D高斯图中导出的，从而适应场景的复杂性。我们的评估表明，GOF在表面重建和新视图合成方面超过了现有的基于3DGS的方法。此外，它在质量和速度方面都优于甚至优于神经隐式方法。 et.al.|[2404.10772](http://arxiv.org/abs/2404.10772)|null|
|**2024-04-16**|**AbsGS: Recovering Fine Details for 3D Gaussian Splatting**|3D高斯散射（3D-GS）技术将3D高斯基元与可微分光栅化相耦合，以实现高质量的新颖视图合成结果，同时提供高级实时渲染性能。然而，由于其在3D-GS中的自适应密度控制策略的缺陷，它在包含高频细节的复杂场景中经常出现过度重建问题，导致渲染图像模糊。这个缺陷的根本原因仍然没有得到充分的探讨。在这项工作中，我们对上述伪影的原因进行了全面的分析，即梯度碰撞，它防止了过度重建区域中的大高斯分裂。为了解决这个问题，我们提出了一种新的单向视角空间位置梯度作为致密化的标准。我们的策略有效地识别了过度重建区域中的大高斯，并通过分割来恢复精细细节。我们在各种具有挑战性的数据集上评估了我们提出的方法。实验结果表明，我们的方法在减少或相似的内存消耗的情况下实现了最佳的渲染质量。我们的方法易于实现，并且可以结合到各种最新的基于高斯飞溅的方法中。我们将在正式发布后开放我们的代码源代码。我们的项目页面位于：https://ty424.github.io/AbsGS.github.io/ et.al.|[2404.10484](http://arxiv.org/abs/2404.10484)|null|
|**2024-04-16**|**1st Place Solution for ICCV 2023 OmniObject3D Challenge: Sparse-View Reconstruction**|在本报告中，我们提出了ICCV 2023 OmniObject3D挑战的第一名解决方案：稀疏视图重建。该挑战旨在评估仅使用每个对象的几个姿势图像进行新的视图合成和表面重建的方法。我们使用Pixel NeRF作为基本模型，并应用深度监督以及从粗到细的位置编码。实验证明了该方法在提高稀疏视图重建质量方面的有效性。我们在最终测试中以25.44614的PSNR排名第一。 et.al.|[2404.10441](http://arxiv.org/abs/2404.10441)|null|
|**2024-04-16**|**SRGS: Super-Resolution 3D Gaussian Splatting**|近年来，三维高斯散射（3DGS）作为一种新型的显式三维表示方式而广受欢迎。这种方法依赖于高斯基元的表示能力来提供高质量的渲染。然而，在低分辨率下优化的基元不可避免地表现出稀疏性和纹理缺陷，这对实现高分辨率新视图合成（HRNVS）提出了挑战。为了解决这个问题，我们提出了超分辨率三维高斯散射（SRGS）来在高分辨率（HR）空间中进行优化。利用多个低分辨率（LR）视图的亚像素交叉视图信息，为HR空间中增加的视点引入了亚像素约束。从更多视点累积的梯度将有助于基元的致密化。此外，预训练的2D超分辨率模型与亚像素约束相结合，使这些密集基元能够学习忠实的纹理特征。通常，我们的方法侧重于致密化和纹理学习，以有效地增强基元的表示能力。在实验上，我们的方法仅在具有LR输入的HRNVS上实现了高渲染质量，在Mip NeRF 360和Tanks&Temples等具有挑战性的数据集上优于最先进的方法。相关规范将在验收后发布。 et.al.|[2404.10318](http://arxiv.org/abs/2404.10318)|null|
|**2024-04-15**|**eMotion-GAN: A Motion-based GAN for Photorealistic and Facial Expression Preserving Frontal View Synthesis**|许多现有的面部表情识别（FER）系统在面对头部姿势的变化时会遇到显著的性能下降。已经提出了许多临街化方法来提高这些系统在这种条件下的性能。然而，它们往往会引入不希望的变形，使其不太适合精确的面部表情分析。在本文中，我们提出了eMotion GAN，这是一种新的深度学习方法，用于正面视图合成，同时在运动域中保留面部表情。将头部变化引起的运动视为噪声，将面部表情引起的运动作为相关信息，训练我们的模型以过滤掉噪声运动，从而仅保留与面部表情相关的运动。然后将过滤后的运动映射到中性正面，以生成相应的富有表现力的正面。我们使用几个广泛认可的动态FER数据集进行了广泛的评估，这些数据集包括在强度和方向上表现出不同程度的头部姿势变化的序列。我们的结果证明了我们的方法在显著减少正面和非正面之间的FER性能差距方面的有效性。具体而言，对于较小的姿态变化，我们实现了高达+5\%的FER改进，对于较大的姿态变化则实现了高高达+20\%的改进。代码位于\url{https://github.com/o-ikne/eMotion-GAN.git}. et.al.|[2404.09940](http://arxiv.org/abs/2404.09940)|**[link](https://github.com/o-ikne/emotion-gan)**|

<p align=right>(<a href=#updated-on-20240419>back to top</a>)</p>

## 3D Reconstruction

|Publish Date|Title|Abstract|PDF|Code|
|---|---|---|---|---|
|**2024-04-18**|**6Img-to-3D: Few-Image Large-Scale Outdoor Driving Scene Reconstruction**|当前的3D重建技术难以从少数图像中忠实地推断出无边界的场景。具体而言，现有方法具有高计算要求，需要详细的姿态信息，并且不能可靠地重建被遮挡区域。我们介绍了6Img-to-3D，这是一种用于单镜头图像到3D重建的高效、可扩展的基于转换器的编码器渲染器方法。我们的方法仅从六个面向外部的输入图像中输出3D一致的参数化三平面，用于大规模、无边界的户外驾驶场景。我们通过将收缩的自定义交叉和自关注机制结合起来，实现三平面参数化、可微分体积渲染、场景收缩和图像特征投影，朝着解决现有缺陷迈出了一步。我们展示了在没有全局姿态信息的情况下，来自单个时间戳的六幅环绕视图车辆图像足以在推理时间内重建360 $^｛\circ｝$ 场景，耗时395毫秒。例如，我们的方法允许渲染第三人称图像和鸟瞰图。我们的代码可在https://github.com/continental/6Img-to-3D，更多示例可以在我们的网站上找到https://6Img-to-3D.GitHub.io/. et.al.|[2404.12378](http://arxiv.org/abs/2404.12378)|**[link](https://github.com/continental/6img-to-3d)**|
|**2024-04-17**|**A Subspace-Constrained Tyler's Estimator and its Applications to Structure from Motion**|我们提出了子空间约束泰勒估计器（STE），该估计器设计用于恢复数据集中可能被异常值高度破坏的低维子空间。STE是泰勒M-估计量（TME）和快速中值子空间的一个变体的融合。我们的理论分析表明，在一个常见的内部异常值模型下，STE可以有效地恢复底层子空间，即使与稳健子空间恢复领域的其他方法相比，它包含的内部值较少。我们在运动结构（SfM）的背景下以两种方式应用STE：用于基本矩阵的鲁棒估计和用于去除外围摄像机，增强SfM管道的鲁棒性。数值实验证实了我们的方法在这些应用中的最先进性能。这项研究对鲁棒子空间恢复领域做出了重大贡献，特别是在计算机视觉和三维重建的背景下。 et.al.|[2404.11590](http://arxiv.org/abs/2404.11590)|null|
|**2024-04-17**|**Texture tomography, a versatile framework to study crystalline texture in 3D**|晶体结构是许多技术和生物材料的一个关键组织特征。在这些材料中，特别是分级结构的材料中，纳米成分的优先排列严重影响材料的宏观行为。为了研究具有高空间分辨率和高角度分辨率的局部晶体纹理，我们开发了纹理层析成像（TexTOM）。这种方法允许通过使用晶体系综的全倒数空间来对多晶材料的衍射数据进行建模，并通过取向分布函数来描述每个体素中的纹理。这意味着，它通过测量所有晶体取向的概率来提供局部纹理的3D重建。TexTOM方法解决了与现有模型相关的局限性：它将几个布拉格反射的强度关联起来，从而减少了对称性造成的模糊性。此外，它产生了局部真实空间晶体取向的定量概率分布，而无需对样品结构进行进一步假设。最后，它有效的数学公式使重建比实验的时间尺度更快。在本文中，我们介绍了数学模型、反演策略及其当前的实验实现。我们展示了模拟数据的特征以及从合成的无机模型样品——二氧化硅毒重石生物形态中获得的实验数据。总之，Tex-TOM为重建多晶样品的3D定量纹理信息提供了一个通用的框架。通过这种方式，它为深入了解天然和技术材料的纳米结构组成打开了大门。 et.al.|[2404.11195](http://arxiv.org/abs/2404.11195)|null|
|**2024-04-17**|**REACTO: Reconstructing Articulated Objects from a Single Video**|在本文中，我们解决了从单个视频重建一般关节式3D对象的挑战。采用动态神经辐射场的现有工作已经推进了视频中人类和动物等关节物体的建模，但由于其变形模型的局限性，分段刚性通用关节物体面临挑战。为了解决这一问题，我们提出了准刚性混合蒙皮，这是一种新的变形模型，可以增强每个零件的刚性，同时保持关节的柔性变形。我们的主要见解结合了三种不同的方法：1）用于改进组件建模的增强型骨骼装配系统，2）使用准稀疏蒙皮权重来提高零件刚度和重建保真度，以及3）应用测地线点分配来实现精确运动和无缝变形。正如在真实和合成数据集上所证明的那样，我们的方法在生成一般关节物体的高保真度3D重建方面优于以前的工作。项目页面：https://chaoyuesong.github.io/REACTO. et.al.|[2404.11151](http://arxiv.org/abs/2404.11151)|null|
|**2024-04-16**|**A Concise Tiling Strategy for Preserving Spatial Context in Earth Observation Imagery**|我们提出了一种新的平铺策略，即Flip-n-Slide，它是为在感兴趣对象（OoI）的位置未知且空间上下文可能是类消歧所必需的情况下特定用于大型地球观测卫星图像而开发的。翻转滑动是一种简洁而简约的方法，允许OoI在多个瓦片位置和方向上表示。该策略引入了空间上下文信息的多个视图，而不会在训练集中引入冗余。通过为每个瓦片重叠保持不同的变换排列，我们增强了训练集的可推广性，而不会歪曲真实的数据分布。我们的实验验证了Flip-n-Slide在语义分割任务中的有效性，语义分割是地球物理研究中必要的数据产品。我们发现，Flip-n-Slide在所有评估指标中都优于以前最先进的拼接数据增强例程。对于代表性不足的类，Flip-n-Slide可将精度提高15.8%。 et.al.|[2404.10927](http://arxiv.org/abs/2404.10927)|**[link](https://github.com/elliesch/flipnslide)**|
|**2024-04-16**|**RapidVol: Rapid Reconstruction of 3D Ultrasound Volumes from Sensorless 2D Scans**|二维（2D）徒手超声是最常用的医学成像方式之一，尤其是在妇产科。然而，它只捕获固有的3D解剖结构的2D横截面视图，丢失了有价值的上下文信息。作为需要昂贵且复杂的3D超声扫描仪的替代方案，可以使用机器学习从2D扫描构建3D体积。然而，这通常需要很长的计算时间。在这里，我们提出了RapidVol：一种神经表示框架，用于加快切片到体积的超声重建。我们使用张量秩分解，将典型的三维体积分解为三平面集，并将其存储起来，以及一个小型神经网络。形成完整的三维重建所需的全部内容是一组二维超声扫描，以及它们的真实（或估计）三维位置和方向（姿态）。重建是由真实的胎儿大脑扫描形成的，然后通过请求新的横截面视图进行评估。与之前基于全隐式表示的方法（如神经辐射场）相比，我们的方法速度快3倍以上，准确率高46%，如果给定不准确的姿态，则更稳健。通过从结构先验而不是从头开始重建，进一步加速也是可能的。 et.al.|[2404.10766](http://arxiv.org/abs/2404.10766)|null|
|**2024-04-16**|**PyTorchGeoNodes: Enabling Differentiable Shape Programs for 3D Shape Reconstruction**|我们提出了PyTorchGeoNodes，这是一个可微分模块，用于使用可解释的形状程序从图像中重建3D对象。与传统的CAD模型检索方法相比，使用形状程序进行三维重建可以对重建对象的语义属性进行推理、编辑、低内存占用等。然而，在过去的工作中，形状程序用于三维场景理解的使用在很大程度上被忽视了。作为我们的主要贡献，我们通过引入一个模块来实现基于梯度的优化，例如，将Blender中设计的形状程序转换为高效的PyTorch代码。我们还提供了一种方法，该方法依赖于PyTorchGeoNodes，并受到蒙特卡洛树搜索（MCTS）的启发，以联合优化形状程序的离散和连续参数，并为输入场景重建3D对象。在我们的实验中，我们将我们的算法应用于重建ScanNet数据集中的3D对象，并根据基于CAD模型检索的重建来评估我们的结果。我们的实验表明，我们的重建与输入场景匹配良好，同时能够对重建对象进行语义推理。 et.al.|[2404.10620](http://arxiv.org/abs/2404.10620)|null|
|**2024-04-15**|**CryoMAE: Few-Shot Cryo-EM Particle Picking with Masked Autoencoders**|冷冻电子显微镜（Cryo-EM）是一种以近原子分辨率确定细胞、病毒和蛋白质组装体结构的关键技术。传统的粒子拾取是低温EM中的一个关键步骤，它与手动操作和自动方法对低信噪比（SNR）和不同粒子方向的敏感性作斗争。此外，现有的基于神经网络的方法通常需要大量的标记数据集，这限制了它们的实用性。为了克服这些障碍，我们引入了cryoMAE，这是一种基于少镜头学习的新方法，利用掩模自动编码器（MAE）的能力，能够有效地选择低温EM图像中的单个粒子。与传统的基于神经网络的技术相反，cryoMAE只需要一组最小的正粒子图像进行训练，但在粒子检测方面表现出很高的性能。此外，自交叉相似性损失的实现确保了粒子和背景区域的不同特征，从而增强了cryoMAE的辨别能力。在大规模cryo-EM数据集上的实验表明，cryoMAE优于现有的最先进的（SOTA）方法，将3D重建分辨率提高了22.4%。 et.al.|[2404.10178](http://arxiv.org/abs/2404.10178)|null|
|**2024-04-15**|**Taming Latent Diffusion Model for Neural Radiance Field Inpainting**|神经辐射场（NeRF）是一种用于从多视图图像进行三维重建的表示。尽管最近的一些工作显示，在编辑具有扩散先验的重建NeRF方面取得了初步成功，但他们仍在努力在完全未覆盖的区域合成合理的几何形状。一个主要原因是来自扩散模型的合成内容的高度多样性，这阻碍了辐射场收敛到清晰和确定的几何结构。此外，由于自动编码错误，在真实数据上应用潜在扩散模型通常会产生与图像条件不相干的纹理偏移。像素距离损失的使用进一步强化了这两个问题。为了解决这些问题，我们建议通过每场景定制来调节扩散模型的随机性，并通过掩蔽对抗性训练来减轻纹理偏移。在分析过程中，我们还发现在NeRF修复任务中，常用的像素和感知损失是有害的。通过严格的实验，我们的框架在各种真实世界场景上产生了最先进的NeRF修复结果。项目页面：https://hubert0527.github.io/MALD-NeRF et.al.|[2404.09995](http://arxiv.org/abs/2404.09995)|null|
|**2024-04-15**|**LetsGo: Large-Scale Garage Modeling and Rendering via LiDAR-Assisted Gaussian Primitives**|大型车库是我们日常生活中无处不在但又错综复杂的场景，其特点是颜色单调、图案重复、反光表面和透明的汽车玻璃。用于相机姿态估计和3D重建的传统运动结构（SfM）方法在这些环境中由于较差的对应结构而失败。为了应对这些挑战，本文介绍了LetsGo，这是一种用于大规模车库建模和渲染的激光雷达辅助高斯散射方法。我们开发了一种手持扫描仪Polar，配备了IMU、激光雷达和鱼眼相机，以便于精确的激光雷达和图像数据扫描。有了这个Polar设备，我们展示了一个GarageWorld数据集，该数据集由五个具有不同几何结构的扩展车库场景组成，并将向社区发布该数据集以供进一步研究。我们证明了Polar设备收集的LiDAR点云增强了一套用于车库场景建模和渲染的3D高斯飞溅算法。我们还提出了一种用于3D高斯喷溅算法训练的新型深度正则化器，有效地消除了渲染图像中的浮动伪影，以及一种用于在基于网络的设备上实时查看的轻量级细节级别（LOD）高斯渲染器。此外，我们还探索了一种混合表示，它将传统网格在描绘简单几何体和颜色（例如，墙壁和地面）方面的优势与捕捉复杂细节和高频纹理的现代3D高斯表示相结合。此策略实现了内存性能和渲染质量之间的最佳平衡。在我们的数据集上的实验结果，以及ScanNet++和KITTI-360，证明了我们的方法在渲染质量和资源效率方面的优势。 et.al.|[2404.09748](http://arxiv.org/abs/2404.09748)|null|

<p align=right>(<a href=#updated-on-20240419>back to top</a>)</p>

## Diffusion

|Publish Date|Title|Abstract|PDF|Code|
|---|---|---|---|---|
|**2024-04-18**|**G-HOP: Generative Hand-Object Prior for Interaction Reconstruction and Grasp Synthesis**|我们提出了G-HOP，这是一种基于去噪扩散的手-物体交互生成先验，允许基于物体类别对3D物体和人手进行建模。为了学习能够捕捉这种关节分布的3D空间扩散模型，我们通过骨骼距离场来表示人手，以获得与对象的（潜在）符号距离场对齐的表示。我们表明，这种手对象先验可以作为通用指导，促进其他任务，如从交互剪辑和人类抓握合成中重建。我们相信，我们的模型通过聚合跨越155个类别的七个不同的真实世界交互数据集进行训练，代表了第一种允许联合生成手和物体的方法。我们的经验评估证明了这种联合先验在基于视频的重建和人类抓取合成中的优势，优于当前特定任务的基线。项目网站：https://judyye.github.io/ghop-www et.al.|[2404.12383](http://arxiv.org/abs/2404.12383)|null|
|**2024-04-18**|**Lazy Diffusion Transformer for Interactive Image Editing**|我们介绍了一种新的扩散转换器LazyDiffusion，它可以有效地生成部分图像更新。我们的方法针对交互式图像编辑应用程序，在该应用程序中，从空白画布或图像开始，用户使用二进制掩码和文本提示指定一系列本地化的图像修改。我们的发电机分两个阶段运行。首先，上下文编码器处理当前画布和用户掩码，以生成针对要生成的区域量身定制的紧凑全局上下文。其次，在这种情况下，基于扩散的变换器解码器以“懒惰”的方式合成掩蔽像素，即，它只生成掩蔽区域。这与之前的作品形成了鲜明对比，之前的作品要么重新生成完整的画布，浪费时间和计算，要么将处理限制在遮罩周围的紧密矩形裁剪，完全忽略全局图像上下文。我们的解码器的运行时随掩码大小而缩放，掩码大小通常很小，而我们的编码器引入的开销可以忽略不计。我们证明，在质量和保真度方面，我们的方法与最先进的修复方法具有竞争力，同时为典型的用户交互提供了10倍的加速，其中编辑掩码代表图像的10%。 et.al.|[2404.12382](http://arxiv.org/abs/2404.12382)|null|
|**2024-04-18**|**Learning the Domain Specific Inverse NUFFT for Accelerated Spiral MRI using Diffusion Models**|用于加速MRI的深度学习方法实现了最先进的结果，但在很大程度上忽略了非笛卡尔采样轨迹可能带来的额外加速。为了解决这一差距，我们为多线圈高度欠采样螺旋MRI创建了一种基于生成扩散模型的重建算法。该模型在训练过程中使用条件调节以及基于频率的指导，以确保图像和测量之间的一致性。根据回顾性数据评估，我们在具有超快扫描时间（2D图像为0.02秒）的重建图像中显示出高质量（结构相似性>0.87）。与使用非均匀快速傅立叶变换的传统重建相比，我们使用该算法来识别一组最佳变密度螺旋轨迹，并显示出图像质量的大幅提高。通过将高效的螺旋采样轨迹、多线圈成像和深度学习重建相结合，这些方法可以实现实时3D成像所需的极高加速度因子。 et.al.|[2404.12361](http://arxiv.org/abs/2404.12361)|null|
|**2024-04-18**|**AniClipart: Clipart Animation with Text-to-Video Priors**|剪贴画是一种预先制作的图形艺术形式，它提供了一种方便有效的方式来说明视觉内容。将静态剪贴画图像转换为运动序列的传统工作流程既费力又耗时，涉及许多复杂的步骤，如装配、关键帧动画和中间处理。文本到视频生成的最新进展在解决这一问题方面具有巨大的潜力。然而，直接应用文本到视频生成模型往往难以保留剪贴画图像的视觉特性或生成卡通风格的运动，导致动画效果不令人满意。在本文中，我们介绍了AniClipart，这是一个将静态剪贴画图像转换为由文本到视频先验引导的高质量运动序列的系统。为了生成卡通风格和流畅的运动，我们首先定义了B\'{e}zier在剪贴画图像的关键点上的曲线作为运动正则化的形式。然后，我们通过优化视频分数提取采样（VSDS）损失，将关键点的运动轨迹与所提供的文本提示对齐，该损失对预训练的文本到视频扩散模型中的自然运动的足够知识进行编码。通过可微的“尽可能刚性”形状变形算法，我们的方法可以在保持变形刚性的同时进行端到端优化。实验结果表明，在文本视频对齐、视觉身份保持和运动一致性方面，所提出的AniClipart始终优于现有的图像到视频生成模型。此外，我们还展示了AniClipart的多功能性，通过调整它来生成更广泛的动画格式，例如允许拓扑变化的分层动画。 et.al.|[2404.12347](http://arxiv.org/abs/2404.12347)|null|
|**2024-04-18**|**Customizing Text-to-Image Diffusion with Camera Viewpoint Control**|模型定制将新概念引入到现有的文本到图像模型中，从而能够在新的上下文中生成新概念。然而，这种方法缺乏对对象的精确相机视图控制，用户必须求助于即时工程（例如，添加“俯视图”）来实现粗略视图控制。在这项工作中，我们介绍了一项新任务——为模型定制实现相机视点的显式控制。这使我们能够通过文本提示修改各种背景场景中的对象属性，同时将目标相机姿势作为附加控件。这一新任务在将来自新概念的多视图图像的3D表示与通用的2D文本到图像模型相合并方面提出了重大挑战。为了弥补这一差距，我们建议以新对象的渲染视图相关特征为条件进行2D扩散过程。在训练过程中，我们联合调整2D扩散模块和3D特征预测，以重建对象的外观和几何结构，同时减少对输入多视图图像的过拟合。在遵循输入文本提示和对象的相机姿势的同时，我们的方法在保留自定义对象的身份方面优于现有的图像编辑和模型个性化基线。 et.al.|[2404.12333](http://arxiv.org/abs/2404.12333)|null|
|**2024-04-18**|**Guided Discrete Diffusion for Electronic Health Record Generation**|电子健康记录（EHR）是一个关键的数据源，可用于计算医学的许多应用，例如疾病进展预测、临床试验设计以及健康经济学和结果研究。尽管具有广泛的可用性，但它们的敏感性引起了隐私和保密问题，从而限制了潜在的用例。为了应对这些挑战，我们探索使用生成模型来合成人工但现实的EHR。尽管基于扩散的方法最近在生成其他数据模式方面表现出了最先进的性能，并克服了困扰以前基于GAN的方法的训练不稳定性和模式崩溃问题，但它们在EHR生成中的应用仍有待开发。EHR中表格医疗代码数据的离散性对高质量数据生成提出了挑战，尤其是对连续扩散模型。为此，我们介绍了一种新的表格EHR生成方法EHR-D3PM，该方法能够使用离散扩散模型进行无条件和有条件生成。我们的实验表明，EHR-D3PM在综合保真度和效用指标上显著优于现有的生成基线，同时保持较小的成员脆弱性风险。此外，我们还证明了EHR-D3PM作为一种数据扩充方法是有效的，并在与真实数据相结合时提高了下游任务的性能。 et.al.|[2404.12314](http://arxiv.org/abs/2404.12314)|null|
|**2024-04-18**|**Investigation of Spin-Pumping and -Transport in the Ni80Fe20/Pt/Co Asymmetric Trilayer**|FM1/NM/FM2三层由于其在自旋电子应用中的潜力而引起了人们的广泛关注。因此，对这些三层的自旋输运特性进行彻底的研究是重要的。不对称三层，特别是包括铂（Pt）作为间隔物的三层，研究较少。Pt介导两个FM层之间的交换耦合，从而提供了一个独特的平台来研究通过自旋泵机制在间接交换耦合条件下的自旋输运特性。我们的分析重点是铁磁共振谱的声学模式，通过Ni80Fe20和Co层的不同磁化，可以隔离单个层的共振。导出的Ni80Fe20和Co层的自旋泵浦诱导阻尼揭示了对Pt间隔层厚度的直接依赖性。此外，阻尼参数的加权平均值与声模的自旋泵激阻尼的拟合表明，观测到的FMR谱实际上是两个FM层中磁化的同相进动的结果。提取的有效自旋混合电导随FM/NM界面的变化而变化，特别是在Ni80Fe20/Pt界面为1.72x10^19m^（-2），在Co/Pt界面为4.07x10^19m ^（-2。此外，我们推导出Pt中的自旋扩散长度在1.02和1.55nm之间，并计算了界面自旋透明度和自旋电流密度，突出了Ni80Fe20/Pt和Co/Pt界面之间的显著差异。这一详细的分析增强了我们对Ni80Fe20/Pt/Co三层中自旋输运的理解。它为推进自旋电子器件设计提供了重要的见解，并为未来三层系统的理论研究奠定了基础。 et.al.|[2404.12307](http://arxiv.org/abs/2404.12307)|null|
|**2024-04-18**|**RISE: 3D Perception Makes Real-World Robot Imitation Simple and Effective**|在模仿学习中，精确的机器人操作需要丰富的空间信息。基于图像的策略对固定摄影机的对象位置进行建模，固定摄影机对摄影机视图更改很敏感。利用3D点云的策略通常预测关键帧，而不是连续动作，这在动态和接触丰富的场景中造成了困难。为了有效利用3D感知，我们提出了RISE，这是一种用于真实世界模仿学习的端到端基线，它直接从单视点云预测连续动作。它使用稀疏3D编码器将点云压缩为标记。在添加稀疏位置编码后，使用转换器对令牌进行特征化。最后，通过扩散头将特征解码为机器人动作。RISE针对每个现实世界任务进行了50次演示，大大超过了当前具有代表性的2D和3D策略，在准确性和效率方面都显示出显著优势。实验还表明，与以前的基线相比，RISE对环境变化更为普遍和稳健。项目网站：rise-policy.github.io。 et.al.|[2404.12281](http://arxiv.org/abs/2404.12281)|null|
|**2024-04-18**|**A New Computational Method for Energetic Particle Acceleration and Transport with its Feedback**|我们开发了一种新的计算方法来探索天体物理和太阳物理现象，特别是那些受到非热高能粒子显著影响的现象。这种新方法通过将非热流体压力纳入磁流体动力学（MHD）方程来考虑这些高能粒子的反作用。非热流体的压力是根据帕克输运方程推导的能量粒子分布来评估的，该方程使用随机微分方程求解。我们在HOW-MHD代码（Seo\&Ryu 2023）中实现了这种方法，实现了五阶精度。我们发现，在没有空间扩散的情况下，当包括非热压力时，该方法准确地再现了流体动力冲击管试验中的黎曼解。求解帕克输运方程可以确定绝热指数分别为 $\gamma_｛\rm｛NT｝｝＝4/3$和$\gamma｛\rm{NT｝}＝5/3$ 的相对论性和非相对论性非热流体的压力项。该方法还成功地复制了具有非热压力的磁流体动力学冲击管测试，成功地解决了几个单元内的不连续性。引入非热粒子的空间扩散会导致冲击的边际变化，但会平滑接触的不连续性。重要的是，该方法成功地模拟了通过冲击加速的非热粒子的能谱，其中包括来自非热粒子群的反馈。这些结果表明，当等离子体能量的很大一部分被高能粒子占据时，这种方法对于研究粒子加速度是非常强大的。 et.al.|[2404.12276](http://arxiv.org/abs/2404.12276)|null|
|**2024-04-18**|**Tree-Based Nonlinear Reduced Modeling**|本文研究了基于树库近似的参数偏微分方程的模型降阶问题。对于希尔伯特空间上的偏微分方程，经典方法是公式化的，并且涉及一个单独的线性空间来近似偏微分方程解的集合。在这里，我们开发了依赖于称为库的线性或非线性近似空间集合的简化模型，该模型也可以在一般度量空间上公式化。为了构建库的空间，我们依赖于涉及不同分裂策略的贪婪算法，这导致了基于层次树的表示。我们通过数值例子说明，就可以成功解决的参数偏微分方程而言，所提出的策略具有更广泛的适用性。虽然经典方法对强矫顽力的椭圆问题非常有效，但我们证明了基于树的库方法可以处理弱矫顽力扩散问题、对流扩散问题以及在一般度量空间（如 $L^2$ -Waserstein空间）上提出的输运主导的偏微分方程。 et.al.|[2404.12262](http://arxiv.org/abs/2404.12262)|null|

<p align=right>(<a href=#updated-on-20240419>back to top</a>)</p>

## NeRF

|Publish Date|Title|Abstract|PDF|Code|
|---|---|---|---|---|
|**2024-04-15**|**Efficient and accurate neural field reconstruction using resistive memory**|人类通过将稀疏的观测整合到大规模互连的突触和神经元中来构建空间感知，提供了卓越的并行性和效率。在人工智能中复制这一能力在医学成像、AR/VR和嵌入式人工智能中有着广泛的应用，在这些领域，输入数据往往是稀疏的，计算资源有限。然而，传统的数字计算机信号重构方法面临着软硬件两方面的挑战。在软件方面，传统显式信号表示中的存储效率低下会带来困难。硬件障碍包括冯·诺依曼瓶颈，它限制了CPU和存储器之间的数据传输，以及CMOS电路在支持并行处理方面的局限性。我们提出了一种软硬件协同优化的系统方法，用于从稀疏输入重建信号。在软件方面，我们使用神经场通过神经网络隐式地表示信号，并使用低秩分解和结构化修剪对其进行进一步压缩。在硬件方面，我们设计了一个基于电阻存储器的内存计算（CIM）平台，该平台具有高斯编码器（GE）和MLP处理引擎（PE）。GE利用电阻存储器的内在随机性进行有效的输入编码，而PE通过硬件感知量化（HAQ）电路实现精确的权重映射。我们在基于40nm 256Kb电阻存储器的内存内计算宏上展示了该系统的功效，在不影响3D CT稀疏重建、新视图合成和动态场景新视图合成等任务的重建质量的情况下，实现了巨大的能效和并行性改进。这项工作推进了人工智能驱动的信号恢复技术，为未来高效、稳健的医疗人工智能和3D视觉应用铺平了道路。 et.al.|[2404.09613](http://arxiv.org/abs/2404.09613)|null|
|**2024-04-10**|**Ray-driven Spectral CT Reconstruction Based on Neural Base-Material Fields**|在谱CT重建中，基底材料分解涉及求解大规模非线性积分方程组，这在数学上是高度不适定的。本文提出了一种模型，该模型使用神经场表示来参数化对象的衰减系数，从而避免了线积分离散化过程中像素驱动的投影系数矩阵的复杂计算。介绍了一种基于光线驱动神经场的线积分轻量级离散化方法，提高了离散化过程中积分逼近的精度。将基底材料表示为连续的向量值隐函数，以建立基底材料的神经场参数化模型。然后使用深度学习的自动微分框架来求解神经基底材料场的隐式连续函数。该方法不受重建图像空间分辨率的限制，并且网络具有紧凑和规则的特性。实验验证表明，我们的方法在处理光谱CT重建方面表现得非常好。此外，它还满足了生成高分辨率重建图像的要求。 et.al.|[2404.06991](http://arxiv.org/abs/2404.06991)|null|
|**2024-04-12**|**SpikeNVS: Enhancing Novel View Synthesis from Blurry Images via Spike Camera**|使用神经辐射场（NeRF）和三维高斯散射（3DGS）等神经场方法实现清晰的新视图合成（NVS）的最关键因素之一是训练图像的质量。然而，传统的RGB相机容易受到运动模糊的影响。相比之下，像事件和尖峰相机这样的神经形态相机固有地捕捉更全面的时间信息，这可以作为额外的训练数据提供场景的清晰表示。最近的方法已经探索了集成事件摄像机以提高NVS的质量。事件RGB方法有一些局限性，例如高昂的培训成本和无法在后台有效工作。相反，我们的研究引入了一种新的方法，使用尖峰相机来克服这些限制。通过将尖峰流的纹理重建视为基本事实，我们设计了尖峰纹理（TfS）损失。由于尖峰摄像机依赖于时间积分，而不是事件摄像机使用的时间微分，我们提出的TfS损失保持了可管理的训练成本。它同时处理前景对象和背景。我们还提供了用spike RGB相机系统拍摄的真实世界数据集，以促进未来的研究工作。我们使用合成和真实世界的数据集进行了广泛的实验，以证明我们的设计可以增强NeRF和3DGS的新视图合成。代码和数据集将提供给公众访问。 et.al.|[2404.06710](http://arxiv.org/abs/2404.06710)|null|
|**2024-04-03**|**A Coupled Neural Field Model for the Standard Consolidation Theory**|标准巩固理论指出，位于海马体的短期记忆能够巩固新皮层的长期记忆。换言之，新皮层在海马体的短暂支持下慢慢学习长期记忆，海马体会快速学习不稳定的记忆。然而，目前尚不清楚这些学习率和记忆时间尺度差异背后的神经生物学机制是什么。在这里，我们提出了一种新的标准巩固理论的建模方法，重点关注其潜在的神经生物学机制。除了突触可塑性和棘突频率适应外，我们的模型还结合了齿状回的成年神经发生以及新皮层和海马体之间的大小差异，我们将其与距离依赖性突触可塑性联系起来。我们还考虑了相关大脑区域的相互关联的空间结构，将上述神经生物学机制纳入耦合的神经场框架中，其中每个区域由具有区域内和区域间连接的单独神经场表示。据我们所知，这是将神经场应用于这一过程的首次尝试。使用数值模拟和数学分析，我们探索了在外部输入的海马重放和检索线索的相位交替时，模型的短期和长期动力学。该外部输入可被编码为单个神经场中的多凸点吸引器模式形式的记忆模式。在该模型中，由于海马记忆模式的突起之间的距离较小，海马记忆模式在新皮质记忆模式之前首先被编码。因此，在短时间尺度上检索新皮层中的输入模式需要由海马体的记忆模式提供额外的输入。新皮质记忆模式在较长的时间内逐渐巩固，直到它们的恢复不再需要海马体的支持。在较长的时间内，神经发生对海马神经场的扰动会抹去海马模式，导致记忆模式只在新皮层中唤起的最终状态。因此，我们模型的动力学成功地再现了标准固结理论的主要特征。这表明，海马体的神经发生和距离依赖性突触可塑性，再加上突触抑制和尖峰频率适应，确实是记忆巩固的关键神经生物学过程。 et.al.|[2404.02938](http://arxiv.org/abs/2404.02938)|null|
|**2024-04-03**|**LiDAR4D: Dynamic Neural Fields for Novel Space-time View LiDAR Synthesis**|尽管神经辐射场（NeRFs）在图像新视图合成（NVS）方面取得了成功，但激光雷达NVS在很大程度上仍未被探索。以前的激光雷达NVS方法采用了图像NVS方法的简单转变，同时忽略了激光雷达点云的动态特性和大规模重建问题。有鉴于此，我们提出了LiDAR4D，这是一种用于新的时空LiDAR视图合成的仅限LiDAR的可微分框架。考虑到稀疏性和大规模特征，我们设计了一种结合多平面和网格特征的4D混合表示，以实现从粗到细的有效重建。此外，我们引入了从点云导出的几何约束，以提高时间一致性。对于激光雷达点云的真实合成，我们结合了光线下降概率的全局优化，以保持跨区域模式。在KITTI-360和NuScenes数据集上进行的大量实验证明了我们的方法在实现几何感知和时间一致的动态重建方面的优越性。代码可在https://github.com/ispc-lab/LiDAR4D. et.al.|[2404.02742](http://arxiv.org/abs/2404.02742)|**[link](https://github.com/ispc-lab/lidar4d)**|
|**2024-04-04**|**Vestibular schwannoma growth prediction from longitudinal MRI by time conditioned neural fields**|前庭神经鞘瘤（VS）是一种良性肿瘤，通常通过MRI检查进行积极监测来治疗。为了进一步帮助临床决策并避免过度治疗，基于纵向成像的肿瘤生长的准确预测是非常可取的。在本文中，我们介绍了DeepGrowth，这是一种深度学习方法，它结合了神经场和递归神经网络，用于前瞻性肿瘤生长预测。在所提出的方法中，每个肿瘤都表示为以低维潜在码为条件的有符号距离函数（SDF）。与之前直接在图像空间中进行肿瘤形状预测的研究不同，我们预测潜在代码，然后从中重建未来的形状。为了处理不规则的时间间隔，我们引入了一个基于ConvLSTM的时间条件递归模块和一种新的时间编码策略，使所提出的模型能够输出随时间变化的肿瘤形状。在内部纵向VS数据集上的实验表明，所提出的模型显著提高了性能（ $\ge 1.6\%%$Dice评分和$\ge0.20$mm95\%Hausdorff距离），特别是对于生长或缩小最多的前20%肿瘤（$\ge4.6\%%$Dice评分和$\ge 0.73$ mm95\%Hausdoff距离）。我们的代码可在~\bull获得{https://github.com/cyjdswx/DeepGrowth} et.al.|[2404.02614](http://arxiv.org/abs/2404.02614)|**[link](https://github.com/cyjdswx/deepgrowth)**|
|**2024-04-02**|**NeRFCodec: Neural Feature Compression Meets Neural Radiance Fields for Memory-Efficient Scene Representation**|神经辐射场（NeRF）的出现极大地影响了三维场景建模和新颖的视图合成。作为一种用于三维场景表示的视觉媒体，具有高率失真性能的压缩是一个永恒的目标。受神经压缩和神经场表示进步的启发，我们提出了NeRFCodec，这是一种端到端的NeRF压缩框架，它集成了非线性变换、量化和熵编码，用于高效记忆的场景表示。由于直接在大规模的NeRF特征平面上训练非线性变换是不切实际的，我们发现，当添加特定于内容的参数时，可以使用预先训练的神经2D图像编解码器来压缩特征。具体来说，我们重用神经2D图像编解码器，但修改其编码器和解码器头，同时保持预训练解码器的其他部分冻结。这使我们能够通过监督渲染损失和熵损失来训练整个管道，通过更新特定于内容的参数来实现率失真平衡。在测试时，包含潜在代码、特征解码器头和其他辅助信息的比特流被发送用于通信。实验结果表明，我们的方法优于现有的NeRF压缩方法，能够在0.5MB的内存预算下实现高质量的新视图合成。 et.al.|[2404.02185](http://arxiv.org/abs/2404.02185)|null|
|**2024-04-18**|**NeRF-MAE: Masked AutoEncoders for Self-Supervised 3D Representation Learning for Neural Radiance Fields**|神经领域在计算机视觉和机器人领域表现出色，因为它们能够理解3D视觉世界，如推断语义、几何和动力学。考虑到神经场在从2D图像密集表示3D场景方面的能力，我们提出了一个问题：我们是否可以扩展它们的自监督预训练，特别是使用掩蔽的自动编码器，从姿态RGB图像中生成有效的3D表示。由于将转换器扩展到新型数据模式的惊人成功，我们采用了标准的3D视觉转换器来适应NeRF的独特配方。我们利用NeRF的体积网格作为变压器的密集输入，将其与其他3D表示（如点云）进行对比，在点云中，信息密度可能不均匀，并且表示不规则。由于将掩蔽的自动编码器应用于隐式表示（如NeRF）很困难，我们选择提取通过使用相机轨迹进行采样来规范化跨域场景的显式表示。我们的目标是通过从NeRF的辐射和密度网格中屏蔽随机补丁，并使用标准的3D Swin Transformer来重建屏蔽的补丁。通过这样做，模型可以学习完整场景的语义和空间结构。我们在我们提出的精心策划的姿势RGB数据上对这种表示进行了大规模的预训练，总共超过160万张图像。一旦经过预训练，编码器就用于有效的3D迁移学习。我们针对NeRF的新型自监督预训练NeRF-MAE可扩展性非常好，并提高了在各种具有挑战性的3D任务中的性能。在Front3D和ScanNet数据集上，利用未标记的姿态2D数据进行预训练，NeRF MAE显著优于自监督3D预训练和NeRF场景理解基线，在3D对象检测方面的绝对性能提高超过20%AP50和8%AP25。 et.al.|[2404.01300](http://arxiv.org/abs/2404.01300)|null|
|**2024-04-06**|**Grounding and Enhancing Grid-based Models for Neural Fields**|当代许多研究利用基于网格的模型来表示神经场，但仍然缺乏对基于网格模型的系统分析，阻碍了这些模型的改进。因此，本文介绍了一个基于网格的模型的理论框架。该框架指出，这些模型的逼近和泛化行为是由网格切线核（GTK）决定的，GTK是基于网格的模型的固有性质。所提出的框架有助于对各种基于网格的模型进行一致和系统的分析。此外，引入的框架推动了一种新的基于网格的模型的开发，该模型名为乘法傅立叶自适应网格（MulFAGrid）。数值分析表明，MulFAGrid表现出比其前身更低的泛化界，表明其具有鲁棒的泛化性能。实证研究表明，MulFAGrid在各种任务中都取得了最先进的性能，包括2D图像拟合、3D符号距离场（SDF）重建和新颖的视图合成，表现出了卓越的表示能力。项目网站位于https://sites.google.com/view/cvpr24-2034-submission/home. et.al.|[2403.20002](http://arxiv.org/abs/2403.20002)|null|
|**2024-04-01**|**Efficient 3D Instance Mapping and Localization with Neural Fields**|我们解决了从一系列摆姿势的RGB图像中学习用于3D实例分割的隐式场景表示的问题。为此，我们引入了3DIML，这是一种新的框架，可以有效地学习可以从新的视点渲染的标签字段，以产生视图一致的实例分割掩码。3DIML显著改进了现有的基于隐式场景表示的方法的训练和推理运行时。与现有技术相反，现有技术以自我监督的方式优化神经场，需要复杂的训练过程和损失函数设计，3DIML利用了两阶段过程。第一阶段InstanceMap将前端实例分割模型生成的图像序列的2D分割掩码作为输入，并将图像上的相应掩码与3D标签相关联。然后，在第二阶段InstanceLift中使用这些几乎视图一致的伪标签掩码来监督神经标签字段的训练，该字段对InstanceMap遗漏的区域进行插值并解决歧义。此外，我们介绍了InstanceLoc，它能够在给定训练过的标签字段和现成的图像分割模型的情况下，通过融合两者的输出，实现实例掩码的近实时定位。我们在Replica和ScanNet数据集的序列上评估了3DIML，并证明了在图像序列的温和假设下3DIML的有效性。与现有的质量相当的隐式场景表示方法相比，我们实现了巨大的实际加速，展示了其促进更快、更有效的3D场景理解的潜力。 et.al.|[2403.19797](http://arxiv.org/abs/2403.19797)|null|

<p align=right>(<a href=#updated-on-20240419>back to top</a>)</p>

[contributors-shield]: https://img.shields.io/github/contributors/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[contributors-url]: https://github.com/Vincentqyw/cv-arxiv-daily/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[forks-url]: https://github.com/Vincentqyw/cv-arxiv-daily/network/members
[stars-shield]: https://img.shields.io/github/stars/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[stars-url]: https://github.com/Vincentqyw/cv-arxiv-daily/stargazers
[issues-shield]: https://img.shields.io/github/issues/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[issues-url]: https://github.com/Vincentqyw/cv-arxiv-daily/issues

