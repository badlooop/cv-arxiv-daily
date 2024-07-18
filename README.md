[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]

## Updated on 2024.07.18
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
|**2024-07-16**|**IPA-NeRF: Illusory Poisoning Attack Against Neural Radiance Fields**|神经辐射场（NeRF）代表了计算机视觉的一个重大进步，提供了隐式的基于神经网络的场景表示和新颖的视图合成功能。它的应用涵盖了不同的领域，包括机器人、城市地图、自主导航、虚拟现实/增强现实等，其中一些被认为是高风险的人工智能应用。然而，尽管NeRF被广泛采用，但其稳健性和安全性在很大程度上仍未得到探索。在这项研究中，我们通过引入针对神经辐射场的幻觉中毒攻击（IPA-NeRF）为这一领域做出了贡献。这种攻击涉及在NeRF中嵌入一个隐藏的后门视图，使其在提供指定的后门视图时能够产生预定的输出，即虚幻的输出，同时保持标准输入的正常性能。我们的攻击是专门为在特定位置欺骗用户或下游模型而设计的，同时确保从其他角度无法检测到NeRF中的任何异常。实验结果证明了我们的幻觉中毒攻击的有效性，在指定的视点上成功地呈现了所需的幻觉，而不会影响其他视图。值得注意的是，我们通过仅向训练集引入小扰动来实现这种攻击。代码可以在以下网址找到https://github.com/jiang-wenxiang/IPA-NeRF. et.al.|[2407.11921](http://arxiv.org/abs/2407.11921)|null|
|**2024-07-16**|**Ev-GS: Event-based Gaussian splatting for Efficient and Accurate Radiance Field Rendering**|与传统的基于帧的方法相比，使用事件相机的计算神经形态成像（CNI）具有运动模糊最小和动态范围增强等优点。现有的基于事件的辐射场渲染方法建立在神经辐射场的基础上，计算量大，重建速度慢。受这两个方面的启发，我们介绍了Ev-GS，这是第一个基于CNI的方案，用于从单目事件相机推断3D高斯飞溅，从而实现高效的新颖视图合成。利用3D高斯模型和纯粹的基于事件的监督，Ev-GS克服了检测快速移动物体和照明不足等挑战。实验结果表明，Ev-GS通过渲染具有减少模糊和提高视觉质量的真实视图，优于以基于帧的信号作为输入的方法。此外，与现有方法相比，它展示了具有竞争力的重建质量和减少的计算占用，为高效的CNI信号处理方法铺平了道路。 et.al.|[2407.11343](http://arxiv.org/abs/2407.11343)|null|
|**2024-07-15**|**AirNeRF: 3D Reconstruction of Human with Drone and NeRF for Future Communication Systems**|在快速发展的数字内容创作领域，对快速、方便和自主制作人类详细3D重建方法的需求显著增长。为了满足这一迫切需求，我们的AirNeRF系统为创建逼真的3D人体化身提供了一条创新途径。我们的方法利用神经辐射场（NeRF）和基于无人机的自动视频捕获方法。所获得的数据提供了一种快速准确的方法，可以在我们系统的几个阶段后创建高质量的人体重建。从我们的系统中得出的装配网格被证明是动态人类自由视图合成的良好基础，特别适合游戏和虚拟现实中的沉浸式体验。 et.al.|[2407.10865](http://arxiv.org/abs/2407.10865)|null|
|**2024-07-15**|**Lite2Relight: 3D-aware Single Image Portrait Relighting**|实现逼真的3D视图合成和人物肖像的重新照明是推进AR/VR应用的关键。肖像重新照明的现有方法在泛化和3D一致性方面存在很大局限性，再加上物理现实照明和身份保护的不准确。此外，从单个视图进行个性化很难实现，在测试阶段通常需要多视图图像，或者涉及缓慢的优化过程。本文介绍了Lite2Relight，这是一种新技术，可以预测肖像的3D一致头部姿态，同时以交互速度进行物理上合理的光线编辑。我们的方法独特地扩展了EG3D的生成能力和高效的体积表示，利用光级数据集隐式地分离面部反射率，并在目标HDRI环境图下进行重新照明。通过使用预训练的几何感知编码器和特征对齐模块，我们将输入图像映射到可重新照亮的3D空间中，并利用强大的面部几何形状和反射先验对其进行增强。通过广泛的定量和定性评估，我们表明我们的方法在疗效、照片真实感和实际应用方面优于最先进的方法。这包括生成完整头部的3D一致结果，包括头发、眼睛和表情。Lite2Relight为在各个领域大规模采用照片级真实感肖像编辑铺平了道路，为以前受限制的问题提供了一个强大的交互式解决方案。项目页面：https://vcai.mpi-inf.mpg.de/projects/Lite2Relight/ et.al.|[2407.10487](http://arxiv.org/abs/2407.10487)|null|
|**2024-07-15**|**NGP-RT: Fusing Multi-Level Hash Features with Lightweight Attention for Real-Time Novel View Synthesis**|本文提出了NGP-RT，这是一种提高Instant NGP渲染速度以实现实时新颖视图合成的新方法。作为一种经典的基于NeRF的方法，Instant NGP将隐式特征存储在多级网格或哈希表中，并应用浅MLP将隐性特征转换为显式颜色和密度。虽然它实现了快速的训练速度，但由于隐式多级特征聚合的每点MLP执行，特别是对于实时应用程序，其渲染速度仍有很大的改进空间。为了应对这一挑战，我们提出的NGP-RT显式地将颜色和密度存储为哈希特征，并利用轻量级的注意力机制来消除哈希冲突，而不是使用计算密集型的MLP。在渲染阶段，NGP-RT将预先计算的占用距离网格合并到射线行进策略中，以告知到最近占用体素的距离，从而减少行进点的数量和全局内存访问。实验结果表明，在具有挑战性的Mip-NeRF360数据集上，NGP-RT实现了比以前基于NeRF的方法更好的渲染质量，在单个Nvidia RTX 3090 GPU上实现了108fps的1080p分辨率。我们的方法有望用于需要高效和高质量渲染的基于NeRF的实时应用。 et.al.|[2407.10482](http://arxiv.org/abs/2407.10482)|null|
|**2024-07-14**|**RS-NeRF: Neural Radiance Fields from Rolling Shutter Images**|神经辐射场（NeRF）因其令人印象深刻的新颖视图合成能力而越来越受欢迎。然而，它们的有效性受到大多数相机系统中常见的滚动快门（RS）效应的阻碍。为了解决这个问题，我们提出了RS NeRF，这是一种设计用于使用具有RS失真的输入从新视图合成正常图像的方法。这涉及一个物理模型，该模型复制了RS条件下的图像形成过程，并联合优化了每行图像的NeRF参数和相机外部参数。我们通过深入研究RS特性并开发算法来增强其功能，进一步解决了基本RS NeRF模型的固有缺点。首先，我们根据相机运动先验，实施平滑正则化，以更好地估计轨迹并提高合成质量。我们还通过引入多采样算法来识别和解决vanilla RS模型中的一个基本缺陷。这种新方法通过全面利用每个中间相机姿势的不同行的RGB数据来提高模型的性能。通过严格的实验，我们证明RS NeRF在合成和现实世界场景中都优于以前的方法，证明了其有效纠正RS相关失真的能力。可用代码和数据：https://github.com/MyNiuuu/RS-NeRF et.al.|[2407.10267](http://arxiv.org/abs/2407.10267)|**[link](https://github.com/myniuuu/rs-nerf)**|
|**2024-07-14**|**SpikeGS: 3D Gaussian Splatting from Spike Streams with High-Speed Camera Motion**|新颖视图合成通过从3D场景的多视图图像生成新的2D渲染来发挥关键作用。然而，用传统相机捕捉高速场景往往会导致运动模糊，阻碍3D重建的有效性。为了应对这一挑战，高帧率密集3D重建成为一项至关重要的技术，能够在各个领域对现实世界的物体或场景进行详细和准确的建模，包括虚拟现实或嵌入式人工智能。Spike相机是一种新型的神经形态传感器，能够以超高的时间分辨率连续记录场景，显示出精确3D重建的潜力。尽管有希望，但现有的方法，如将神经辐射场（NeRF）应用于尖峰相机，由于耗时的渲染过程而遇到了挑战。为了解决这个问题，我们首次尝试将3D高斯散斑（3DGS）引入高速捕捉的尖峰相机中，提供3DGS作为密集和连续的视图线索，然后构建SpikeGS。具体来说，为了训练SpikeGS，我们在3DGS的渲染过程与连续尖峰流的瞬时成像和类似曝光的成像过程之间建立了计算方程。此外，我们构建了一个非常轻量级但有效的映射过程，从峰值到即时图像，以支持训练。此外，我们引入了一种新的基于尖峰的3D渲染数据集进行验证。大量实验表明，我们的方法具有高质量的新颖视图渲染，证明了尖峰相机在建模3D场景方面的巨大潜力。 et.al.|[2407.10062](http://arxiv.org/abs/2407.10062)|null|
|**2024-07-12**|**Mixed-View Panorama Synthesis using Geospatially Guided Diffusion**|我们介绍了混合视图全景合成的任务，其目标是在给定一小组输入全景图和该区域的卫星图像的情况下合成一个新的全景图。这与之前仅使用输入全景图（相同视图合成）或输入卫星图像（交叉视图合成）的工作形成鲜明对比。我们认为，混合视图设置是支持全球任意位置全景合成的最自然设置。一个关键的挑战是全景图的空间覆盖是不均匀的，世界许多地区几乎没有全景图。我们介绍了一种利用基于扩散的建模和基于注意力的架构从所有可用的输入图像中提取信息的方法。实验结果证明了我们提出的方法的有效性。特别是，我们的模型可以处理可用全景稀疏或远离我们试图合成的全景位置的情况。 et.al.|[2407.09672](http://arxiv.org/abs/2407.09672)|null|
|**2024-07-12**|**Radiance Fields from Photons**|神经辐射场（NeRF）已成为从多个视点捕获的图像集合中进行高质量视图合成的事实上的方法。然而，在具有挑战性的条件下在野外拍摄图像时，仍然存在许多问题，例如低光照、高动态范围或快速运动导致模糊重建，并产生明显的伪影。在这项工作中，我们引入了量子辐射场，这是一类新的神经辐射场，使用单光子相机（SPC）以单个光子的粒度进行训练。我们开发了理论和实用的计算技术，用于构建辐射场，并从SPC捕获的非常规、随机和高速二进制帧序列中估计密集的相机姿态。我们通过仿真和SPC硬件原型演示了在高速运动、低光照和极端动态范围设置下的高保真重建。 et.al.|[2407.09386](http://arxiv.org/abs/2407.09386)|null|
|**2024-07-17**|**Learning High-Frequency Functions Made Easy with Sinusoidal Positional Encoding**|基于傅里叶特征的位置编码（PE）通常用于机器学习任务，这些任务涉及从低维输入中学习高频特征，如3D视图合成和具有神经切线核的时间序列回归。尽管它们很有效，但现有的PE需要手动、经验性地调整关键的超参数，特别是傅里叶特征，以适应每项独特的任务。此外，PE在高效学习高频函数方面面临挑战，特别是在数据有限的任务中。本文介绍了正弦PE（SPE），旨在有效地学习与真实底层函数紧密对齐的自适应频率特征。我们的实验表明，SPE在不进行超参数调整的情况下，在各种任务中（包括3D视图合成、文本到语音生成和1D回归）始终实现了增强的保真度和更快的训练。SPE的实施是为了直接替代现有的PE。其即插即用的特性使许多任务能够轻松采用SPE并从中受益。 et.al.|[2407.09370](http://arxiv.org/abs/2407.09370)|**[link](https://github.com/zhyuan11/SPE)**|

<p align=right>(<a href=#updated-on-20240718>back to top</a>)</p>

## 3D Reconstruction

|Publish Date|Title|Abstract|PDF|Code|
|---|---|---|---|---|
|**2024-07-16**|**Learning Multi-view Anomaly Detection**|本研究探讨了最近提出的具有挑战性的多视图异常检测（AD）任务。单视图任务会遇到其他视角的盲点，导致样本级预测不准确。因此，我们引入\textbf{M}ulti-\textbf{V}iew\textbf{A}nomaly\textbf{D}etection（\textbf{MVAD}）框架，它从多个视图学习和集成功能。具体来说，我们提出了一个\textbf{M}ulti-\textbf{V}iew\textbf{A}daptive\textbf{S}election（\textbf{MVAS}）算法，用于跨多个视图的特征学习和融合。特征图被划分为邻域注意力窗口，以计算单个视图窗口和所有其他视图之间的语义相关性矩阵，这是针对每个单个视图窗口以及前K个相关性最高的多视图窗口的一种传导注意力机制。调整窗口大小和top-K可以将计算复杂度降至线性。在Real IAD数据集上进行的交叉设置（多类/单类）的广泛实验验证了我们方法的有效性，在样本\textbf{4.1\%} $\uparrow$/image\textbf{1.6\%}$\uparrow$/pixel\textbf{6.7\%}\\uparrow$ 级别中实现了最先进的性能，总共有十个指标，只有\textbf[18M}个参数，GPU内存和训练时间更少。 et.al.|[2407.11935](http://arxiv.org/abs/2407.11935)|null|
|**2024-07-16**|**MVG-Splatting: Multi-View Guided Gaussian Splatting with Adaptive Quantile-Based Geometric Consistency Densification**|在快速发展的3D重建领域，3D高斯散斑（3DGS）和2D高斯散斑技术（2DGS）代表了重大进步。尽管2DGS将3D高斯基元压缩为2D高斯表面以有效提高网格提取质量，但这种压缩可能会导致渲染质量的降低。此外，不可靠的致密化过程和通过不透明度累积计算深度可能会影响网格提取的细节。为了解决这个问题，我们介绍了MVG Splatting，这是一种基于多视图考虑的解决方案。具体来说，我们整合了一种计算法线的优化方法，该方法与图像梯度相结合，有助于纠正原始深度计算中的不一致。此外，利用类似于多视图立体（MVS）中的投影策略，我们提出了一种基于自适应分位数的方法，该方法动态确定由深度图引导的额外致密化水平，从粗到细。实验证据表明，我们的方法不仅解决了由深度差异引起的渲染质量下降的问题，而且还便于使用Marching Cubes算法从密集的高斯点云中直接提取网格。这种方法显著提高了3D重建过程的整体保真度和准确性，确保了几何细节和视觉质量。 et.al.|[2407.11840](http://arxiv.org/abs/2407.11840)|null|
|**2024-07-16**|**MRIo3DS-Net: A Mutually Reinforcing Images to 3D Surface RNN-like framework for model-adaptation indoor 3D reconstruction**|本文首次提出了一种端到端的图像相互增强的3D表面递归神经网络框架，用于模型自适应室内3D重建，其中多视图密集匹配和点云表面优化通过类似RNN的结构相互增强，而不是被视为一个单独的问题。其特点如下：在多视图密集匹配模块中，使用模型自适应策略对基于Transformer的多视图稠密匹配DNN进行微调和优化，使其具有更高的匹配图像特征和细节表达能力；在点云曲面优化模块中，采用模型自适应策略对基于三维隐式场的三维曲面重建网络进行优化，解决了在不知道三维曲面法向量的情况下点云曲面的优化问题。为了从点云改进和精细重建3D表面，提出了平滑损失并将其添加到该模块中；MRIo3DS-Net是一个类似RNN的框架，它利用PCSOM获得的精细优化的3D曲面来递归增强可微翘曲，以优化MVDMM。这种细化导致实现更好的密集匹配结果，更好的密集匹配对递归和相互实现更好的3D表面结果。因此，模型自适应策略可以更好地协调两个网络模块之间的差异，使它们相辅相成，达到更好的效果；为了加速从源域到目标域的迁移学习和训练收敛，使用基于贝叶斯不确定性的多任务损失函数自适应地调整MVDMM和PCSOM两个网络损失函数之间的权重；在这个多任务级联网络框架中，任何模块都可以被任何最先进的网络所取代，以获得更好的3D重建结果。 et.al.|[2407.11431](http://arxiv.org/abs/2407.11431)|null|
|**2024-07-15**|**Evaluating geometric accuracy of NeRF reconstructions compared to SLAM method**|随着神经辐射场（NeRF）实现变得更快、更高效、更准确，它们对现实世界映射任务的适用性变得更加容易。传统上，3D映射或场景重建依赖于昂贵的激光雷达传感。摄影测量可以执行基于图像的3D重建，但计算成本很高，需要极其密集的图像表示来恢复复杂的几何形状和照片真实感。NeRF通过在稀疏图像和姿态数据上训练神经网络来执行3D场景重建，在输入数据较少的情况下实现了优于摄影测量的结果。本文对两种用于估算垂直PVC圆柱体直径的NeRF场景重建进行了评估。其中一个是基于商品iPhone数据进行训练的，另一个是针对机器人来源的图像和姿势进行训练的。这种神经几何在场景噪声和度量精度方面与最先进的激光雷达惯性SLAM进行了比较。 et.al.|[2407.11238](http://arxiv.org/abs/2407.11238)|null|
|**2024-07-15**|**Stationary CT Imaging of Intracranial Hemorrhage with Diffusion Posterior Sampling Reconstruction**|扩散后验采样（DPS）可用于计算机断层扫描（CT）重建，通过利用基于扩散的生成模型进行无条件图像合成，同时匹配CT扫描的观测值（数据）。特别感兴趣的是它在涉及稀疏或有限角度采样的场景中的应用，在这些场景中，传统的重建算法往往是不够的。我们开发了一种DPS算法，用于从基于31个x射线管和曲面探测器的多x射线源阵列（MXA）的固定CT（sCT）便携式脑卒中成像单元进行3D重建。在这种配置中，传统的重建，例如具有Huber边缘保持惩罚的惩罚加权最小二乘法（PWLS），会受到严重的方向性欠采样伪影的影响。所提出的DPS集成了一个作用于图像切片的二维扩散模型，结合sCT数据一致性和体积正则化项，使3D重建对噪声和不完全采样具有鲁棒性。为了减轻DPS的计算负担，使用带有PWLS初始化的随机收缩来减少扩散步骤的数量。验证研究包括模拟具有合成出血的拟人化脑模型和来自sCT试验台的实验数据。在模拟中，与PWLS相比，DPS实现了约130%的定向伪影减少，病变形状恢复率（DICE系数）提高了30%。台式研究表明，京都香谷头部幻影的大脑特征可视化增强。与高度欠采样的sCT系统的传统基于模型的重建相比，所提出的DPS实现了颅内出血和脑形态的改进可视化。 et.al.|[2407.11196](http://arxiv.org/abs/2407.11196)|null|
|**2024-07-15**|**iHuman: Instant Animatable Digital Humans From Monocular Videos**|个性化的3D化身需要数字人的可动画表示。从单眼视频中立即实现这一点，可以为广大用户和大规模应用程序提供可扩展性。在这篇论文中，我们提出了一种快速、简单但有效的方法，用于从单眼视频中创建可动画化的3D数字人。我们的方法利用高斯溅射的效率来模拟3D几何和外观。然而，我们观察到，天真地优化高斯斑点会导致几何不准确，从而导致动画效果不佳。这项工作实现并说明了通过高斯斑点对人体进行精确的3D网格类型建模以实现可动画数字化的需求。这是通过开发一种新型管道来实现的，该管道受益于三个关键方面：（a）表面位移和颜色球面谐波的隐式建模；（b） 将3D高斯图绑定到身体模板的各个三角形面；（c） 一种新的技术来渲染法线，然后进行辅助监督。我们在三个不同的基准数据集上进行了详尽的实验，在有限的时间内展示了我们方法的最新结果。事实上，我们的方法比最接近的竞争对手快一个数量级（就训练时间而言）。同时，我们在姿态变化下实现了卓越的渲染和3D重建性能。 et.al.|[2407.11174](http://arxiv.org/abs/2407.11174)|**[link](https://github.com/pramishp/ihuman)**|
|**2024-07-15**|**AirNeRF: 3D Reconstruction of Human with Drone and NeRF for Future Communication Systems**|在快速发展的数字内容创作领域，对快速、方便和自主制作人类详细3D重建方法的需求显著增长。为了满足这一迫切需求，我们的AirNeRF系统为创建逼真的3D人体化身提供了一条创新途径。我们的方法利用神经辐射场（NeRF）和基于无人机的自动视频捕获方法。所获得的数据提供了一种快速准确的方法，可以在我们系统的几个阶段后创建高质量的人体重建。从我们的系统中得出的装配网格被证明是动态人类自由视图合成的良好基础，特别适合游戏和虚拟现实中的沉浸式体验。 et.al.|[2407.10865](http://arxiv.org/abs/2407.10865)|null|
|**2024-07-15**|**Single-cell 3D genome reconstruction in the haploid setting using rigidity theory**|本文考虑了单细胞数据的三维基因组重建问题，以及这种重建在单倍体生物环境中的独特性。我们考虑多个图模型作为这个问题的表示，并使用图刚性理论的技术来确定可识别性。在生物学上，我们的模型来自Hi-C数据、显微镜数据及其组合。在数学上，我们使用单位球和球体堆积模型，以及由距离和不等式约束组成的模型。在每种情况下，我们都会描述和/或得出关于可实现性和唯一性的新结果。然后，我们提出了一种基于半定规划的3D重建方法，并使用我们的模型将其应用于合成和真实数据集。 et.al.|[2407.10700](http://arxiv.org/abs/2407.10700)|null|
|**2024-07-15**|**Deep Diffusion Image Prior for Efficient OOD Adaptation in 3D Inverse Problems**|最近利用生成扩散先验的逆问题求解器因其卓越的质量而受到了广泛关注。然而，当训练和测试分布之间存在差异时，有必要对先验进行调整。在这项工作中，我们提出了深度扩散图像先验（DDIP），通过引入与深度图像先验的形式连接，推广了SCD的最新自适应方法。在此框架下，我们提出了一种名为D3IP的高效自适应方法，专为3D测量而设计，该方法在实现卓越性能的同时，将DDIP加速了几个数量级。D3IP实现了3D逆求解器的无缝集成，从而实现了连贯的3D重建。此外，我们还表明，元学习技术也可以应用于产生更好的性能。我们证明，我们的方法能够从仅用与训练集大不相同的幻影图像训练的生成先验中解决各种3D重建任务，即使在不可能用金标准数据训练的情况下，也为应用扩散逆求解器开辟了新的机会。代码：https://github.com/HJ-harry/DDIP3D et.al.|[2407.10641](http://arxiv.org/abs/2407.10641)|**[link](https://github.com/hj-harry/ddip3d)**|
|**2024-07-15**|**COSMU: Complete 3D human shape from monocular unconstrained images**|我们提出了一种新的框架，通过利用单眼无约束图像，从给定的目标图像中重建完整的3D人体形状。这项工作的目的是在输入目标中不可见的重建人体区域中再现高质量的细节。所提出的方法解决了从单个图像重建3D人体形状的现有方法的局限性，这些方法无法在被遮挡的身体区域再现形状细节。通过使用从多个相机捕获的多个视图，可以恢复单眼输入的缺失信息。然而，多视图重建方法需要精确校准和配准的图像，这在现实世界中很难获得。给定一个目标RGB图像和一组使用单个相机获取的同一个人的多个未校准和未注册的图像，我们提出了一种生成完整3D人体形状的新框架。我们介绍了一种新的模块，用于生成与目标输入图像配准的人的二维多视图法线图。该模块由基于身体部位的参考选择和基于身体部位注册组成。然后，生成的2D法线图由基于多视图注意力的神经隐式模型进行处理，该模型估计3D形状的隐式表示，确保在观察和遮挡区域中再现细节。大量实验表明，与相关方法相比，在不使用参数模型的情况下，所提出的方法在3D服装人体形状的不可见区域估计了更高质量的细节。 et.al.|[2407.10586](http://arxiv.org/abs/2407.10586)|null|

<p align=right>(<a href=#updated-on-20240718>back to top</a>)</p>

## Diffusion

|Publish Date|Title|Abstract|PDF|Code|
|---|---|---|---|---|
|**2024-07-16**|**Efficient Training with Denoised Neural Weights**|良好的权重初始化是降低深度神经网络（DNN）模型训练成本的有效措施。选择如何初始化参数具有挑战性，可能需要手动调整，这可能很耗时，而且容易出现人为错误。为了克服这些局限性，这项工作朝着构建权重生成器迈出了新的一步，以合成用于初始化的神经权重。我们使用具有生成对抗网络（GAN）的图像到图像翻译任务作为示例，因为易于收集跨越广泛范围的模型权重。具体来说，我们首先收集一个包含各种图像编辑概念及其相应训练权重的数据集，这些权重稍后用于训练权重生成器。为了解决层之间的不同特征和要预测的大量权重，我们将权重划分为大小相等的块，并为每个块分配一个索引。随后，使用概念的文本条件和块索引，用这样的数据集训练扩散模型。通过用我们的扩散模型预测的去噪权重初始化图像翻译模型，训练只需要43.3秒。与从头开始训练（即Pix2pix）相比，我们为新概念实现了15倍的训练时间加速，同时获得了更好的图像生成质量。 et.al.|[2407.11966](http://arxiv.org/abs/2407.11966)|null|
|**2024-07-16**|**UrbanWorld: An Urban World Model for 3D City Generation**|城市作为人类生活最基本的环境，包含着各种各样的物理元素，如建筑物、道路和植被，它们之间存在着复杂的相互联系。打造逼真、交互式的3D城市环境在构建能够感知、决策和在现实世界环境中像人类一样行动的人工智能代理方面发挥着至关重要的作用。然而，创建高保真的3D城市环境通常需要设计师大量的手工劳动，涉及复杂的细节和复杂城市特征的准确表示。因此，如何自动实现这一目标仍然是一个长期的挑战。针对这个问题，我们提出了UrbanWorld，这是第一个生成式城市世界模型，可以自动创建具有灵活控制条件的定制、逼真和交互式的3D城市世界。UrbanWorld在自动制作流程中包含了四个关键阶段：从可公开访问的OSM数据生成3D布局，使用强大的城市多模式大型语言模型（urban MLLM）进行城市场景规划和设计，使用先进的3D扩散技术进行可控的城市资产渲染，最后是MLLM辅助的场景细化。精心打造的高保真3D城市环境为模拟中的通用AI和机器感知系统提供了逼真的反馈和交互。我们正在努力将UrbanWorld作为一个开源和多功能的平台，用于评估和提高人工智能在现实城市环境中的感知、决策和交互能力。 et.al.|[2407.11965](http://arxiv.org/abs/2407.11965)|null|
|**2024-07-16**|**Gated Temporal Diffusion for Stochastic Long-Term Dense Anticipation**|长期行为预测已成为自动驾驶和人机交互等许多应用的重要任务。与短期预期不同，随着长期不确定性的增加，预测未来的更多行动带来了真正的挑战。虽然在预测未来的更多行动方面取得了重大进展，但大多数提出的方法都是在确定性设置中解决任务，而忽略了潜在的不确定性。在本文中，我们提出了一种新的门控时间扩散（GTD）网络，该网络对观测和未来预测的不确定性进行建模。作为生成器，我们引入了门控预期网络（GTAN），以相互表示的方式对视频的观察帧和未观察帧进行建模。一方面，使用过去和未来的相互表示使我们能够共同对观测和未来的模糊性进行建模，另一方面，GTAN可以通过设计来区别对待观测和未观测的部分，并引导它们之间的信息流。我们的模型在随机和确定性设置下的早餐、组装101和50Salads数据集上都取得了最先进的结果。代码：https://github.com/olga-zats/GTDA . et.al.|[2407.11954](http://arxiv.org/abs/2407.11954)|null|
|**2024-07-16**|**Spatiotemporal dynamics of ionic reorganization near biological membrane interfaces**|可兴奋细胞中的电信号涉及通过细胞脂质膜上的离子通道和泵的空间定位离子通量。理解这些局部通量如何扩散的常见方法假设膜和周围的电解质由电容器和电阻器的等效电路组成，这忽略了跨膜离子传输的局部性质、由此产生的离子梯度和电场及其时空弛豫。在这里，我们考虑了一个局部离子泵送穿过脂质膜的模型，并使用理论和模拟来研究电化学信号如何沿膜在平面内外时空传播。局部泵浦产生沿膜具有三种不同缩放机制的远程电场：恒定电势近场区域、中间“单极”区域和远场“双极”区域。在持续泵送时，单极区域以稳定的速度在平面内径向膨胀，这一速度因介电失配和脂质膜的有限厚度而增强。对于生理环境中的无髓鞘脂膜，我们发现其传播速度非常快，为 $\ sim \！40，\mathrm{m/s}$ ，与裸扩散相比，允许更快的离子重组。总之，我们的工作表明，跨膜离子通量在电解质溶液中诱导瞬态长程电场，这可能在生物信号传导中发挥迄今为止未被重视的作用。 et.al.|[2407.11947](http://arxiv.org/abs/2407.11947)|null|
|**2024-07-16**|**Context-Guided Diffusion for Out-of-Distribution Molecular and Protein Design**|生成模型有可能加速发现新型分子疗法和材料的关键步骤。扩散模型最近成为一种强大的方法，擅长无条件样本生成，并在数据驱动的指导下，在其训练领域内进行条件生成。然而，从训练数据之外的高价值区域可靠地采样仍然是一个悬而未决的挑战，目前的方法主要侧重于修改扩散过程本身。在本文中，我们开发了上下文引导扩散（CGD），这是一种简单的即插即用方法，利用未标记的数据和平滑度约束来改进引导扩散模型的分布外泛化。我们证明，这种方法在各种环境中都能带来实质性的性能提升，包括连续、离散和图形结构的扩散过程，并在药物发现、材料科学和蛋白质设计中得到应用。 et.al.|[2407.11942](http://arxiv.org/abs/2407.11942)|**[link](https://github.com/leojklarner/context-guided-diffusion)**|
|**2024-07-16**|**Revisiting primordial magnetic fields through 21-cm physics: Bounds and forecasts**|原始磁场（PMF）可能通过两种机制显著影响21厘米物理：（i）通过双极扩散（AD）和衰减磁流体动力学湍流（DT）对星系间介质（IGM）的磁加热，（ii）通过小尺度增强物质功率谱对恒星形成率密度（SFRD）的影响。在这项分析中，我们将这两种效应整合在一个统一的分析框架内，并根据EDGES观测到的全局21cm信号，使用它来确定近尺度不变非螺旋PMF参数空间的上限。我们的研究结果表明，对这两种效应的联合考虑对当前磁场强度提供了 $B_0\lesssim\matical{O}（10^{-2}）$nG量级的约束，与早期分析相比，这一约束要严格得多。随后，我们探索了在即将到来的SKA Low任务中探测这种磁化21厘米功率谱的前景。对于PMF的相关参数（$B_0$和$n_｛\！_｛B｝｝$）和过量无线电背景（$\neneneba xi$），SNR估计和Fisher预测分析表明，在SKA-Low，可以用相对的$1\sigma$不确定性$\lesssim10\%$和相关的SNR$\gtrsim10$ 来约束这三个参数。这也导致了这三个参数之间可能存在的相关性，从而揭示了所涉及的各种物理过程之间相互作用的有趣趋势。 et.al.|[2407.11923](http://arxiv.org/abs/2407.11923)|null|
|**2024-07-16**|**Energy dependence of the knee in the cosmic ray spectrum across the Milky Way**|在地球上测量的宇宙射线的全粒子光谱在4 PeV左右具有膝盖状的特征。从先验角度来看，尚不清楚这是银河系中太阳邻域特有的局部特征，还是银河系宇宙射线谱的一般属性。我们认为，结合LHAASO的伽马射线和宇宙射线数据表明，膝盖是一个局部特征。为了证明这一点，我们推导了一个局部宇宙射线光谱和成分的模型，该模型与最近LHAASO对所有粒子光谱和膝盖区域平均对数质量的测量结果一致。我们基于该模型计算了漫射伽马射线发射的光谱，发现漫射伽马射线通量的预期光谱形状与LHAASO在10-100TeV能量范围内对漫射伽马射线辐射的测量结果不一致。 et.al.|[2407.11911](http://arxiv.org/abs/2407.11911)|null|
|**2024-07-16**|**Impact of coherent mode coupling on noise performance in elliptical aperture VCSELs for datacom**|我们研究了具有椭圆氧化物孔径的中型多模VCSEL的动态行为，该孔径被选择用于数据通信应用的高输出功率和调制速度之间的最佳权衡，重点研究了它们的相对强度噪声（RIN）性能。我们为各种VCSEL收集的实验结果概述了传输系统带宽内RIN光谱中存在几个峰值，这可能会限制直流调制下的睁眼。在这里，我们首次提出了一个严格的模型来解释这些峰值的起源。特别是，通过时域模式扩展方法解决激光动力学和相关噪声特征，考虑多模竞争、空间空穴燃烧和载流子扩散中的相干效应，光谱RIN峰的频率被分析地描述为横模之间非平凡相互作用的结果。通过PAM2和PAM4调制的动态模拟来解决激光调制性能问题，这清楚地表明了高比特率光互连的潜力。最后，我们通过电磁模拟解决了氧化物孔径纵横比的影响，展示了椭圆率如何影响模态频率失谐和RIN，从而为具有低RIN性能的VCSEL提供了设计指南，并概述了这些器件中大幅改善带宽功率权衡的清晰路线图。 et.al.|[2407.11899](http://arxiv.org/abs/2407.11899)|null|
|**2024-07-16**|**Single Layer Single Gradient Unlearning**|机器学习方法试图修改预训练模型，以消除某些训练样本的影响。除了有效的擦除之外，低计算成本和通用性保留也是非常理想的。现有的忘却方法通常涉及对模型参数的迭代更新，这会带来很高的计算成本。在这项工作中，我们提出了一种只需要一次性梯度计算的高效方法，通过这种方法，我们只修改了单层模型参数。具体来说，我们首先将位于高遗忘重要性和低保留影响帕累托前沿的少数模型层确定为关键层。然后，我们寻找合适的步长，沿着单个关键层的梯度方向迈出一步，同时保持其他层冻结。这种方法具有高度的模块化，可用于以可控的方式同时忘却多个概念。我们在包括CLIP、稳定扩散和VLM在内的各种模型上证明了该方法的有效性和效率，超越了其他最先进的方法。 et.al.|[2407.11867](http://arxiv.org/abs/2407.11867)|null|
|**2024-07-16**|**Navigating Munk's Abyssal Recipes: Reconciling the Paradoxes and Suggesting an Upwelling Mechanism for Bottom Water in a Flat-Bottom Ocean**|Walter Munk的经典著作被称为“深海食谱”，为理解深海上升流引入了一个基础框架。虽然它从理论、实验室和现场的角度激发了对深海过程复杂性的大量研究，但与几十年的直接观测相比，它也面临着挑战。出现了两个特别有趣的悖论：扩散率的二分法和内部下行难题。本研究试图通过在蒙克深海配方的动态框架内检查等周位移速度来解决这些悖论。一个令人宽慰的推论是，似乎不再需要寻求全球平均的底辟扩散率O（1）cm2/s来结束与底水形成速率相关的质量预算。通过箱式模型实验，提出了一种新的侵蚀入侵模型，以阐明平底海洋中深海上升流的机制，并将其比作“树木年轮”的生长。基于该模型，利用生物地球化学示踪剂的观测数据估算了北太平洋深海的平均上升速度。所提出的模型并不试图反驳现有的理论，而是作为对主流理论可能不适用的情况的补充，例如平底地形或非底部强化扩散率的情况。 et.al.|[2407.11864](http://arxiv.org/abs/2407.11864)|null|

<p align=right>(<a href=#updated-on-20240718>back to top</a>)</p>

## NeRF

|Publish Date|Title|Abstract|PDF|Code|
|---|---|---|---|---|
|**2024-07-16**|**Adaptive Environment-Aware Robotic Arm Reaching Based on a Bio-Inspired Neurodynamical Computational Framework**|仿生机器人系统具有自适应学习、可扩展控制和高效信息处理的能力。为这些系统提供实时决策对于应对环境的动态变化至关重要。我们专注于在开放区域使用带有鸟瞰摄像头的机器人六自由度操纵器进行动态目标跟踪，并部署神经动力学计算框架（NeuCF）进行视觉反馈。NeuCF是最近开发的一种基于动态神经场（DNF）和随机最优控制（SOC）理论的仿生目标跟踪模型。它已经过训练，可以在平面上对局部视觉信标进行到达动作，并且可以根据环境的变化（例如，出现了新的目标，或者删除了现有的目标）实时重新定位或生成停止信号。我们在各种目标达成场景下评估了我们的系统。在所有实验中，与基线三次多项式轨迹生成器相比，NeuCF具有较高的末端执行器位置精度，生成了平滑的轨迹，并提供了更短的路径长度。总之，开发的系统提供了一种强大的、动态感知的机器人操纵方法，可以提供实时决策。 et.al.|[2407.11377](http://arxiv.org/abs/2407.11377)|null|
|**2024-07-12**|**Physics-Informed Learning of Characteristic Trajectories for Smoke Reconstruction**|我们通过稀疏视图RGB视频深入研究了烟雾和障碍物的物理信息神经重建，解决了复杂动力学观测有限带来的挑战。现有的基于物理信息的神经网络通常强调短期物理约束，对长期守恒的适当保护探索较少。我们引入了神经特征轨迹场，这是一种利用欧拉神经场隐式建模拉格朗日流体轨迹的新表示方法。这种无拓扑、可自动微分的表示便于在任意帧之间进行高效的流图计算，以及通过自动微分进行高效的速度提取。因此，它实现了涵盖长期保护和短期物理先验的端到端监督。在此基础上，我们提出了基于物理的轨迹学习和集成到基于NeRF的场景重建中。我们通过自我监督的场景分解和无缝集成的边界约束来实现高级障碍物处理。我们的结果展示了克服遮挡不确定性、密度-颜色模糊性和静态-动态纠缠等挑战的能力。代码和示例测试位于\url{https://github.com/19reborn/PICT_smoke}. et.al.|[2407.09679](http://arxiv.org/abs/2407.09679)|null|
|**2024-07-10**|**Neural Localizer Fields for Continuous 3D Human Pose and Shape Estimation**|随着可用训练数据的爆炸性增长，单图像3D人体建模领先于向以数据为中心的范式过渡。成功利用数据规模的关键是设计灵活的模型，这些模型可以从不同研究人员或供应商生产的各种异构数据源进行监督。为此，我们提出了一种简单而强大的范式，用于无缝统一不同的人体姿势和形状相关的任务和数据集。我们的公式侧重于在训练和测试时查询人体体积的任意点并在3D中获得其估计位置的能力。我们通过学习身体点定位器函数的连续神经场来实现这一点，每个函数都是基于不同参数化的3D热图卷积点定位器（检测器）。为了生成参数输出，我们提出了一种高效的后处理步骤，用于将SMPL族身体模型拟合到非参数关节和顶点预测中。通过这种方法，我们可以自然地利用不同注释的数据源，包括网格、2D/3D骨架和密集姿势，而无需在它们之间进行转换，从而训练出大规模的3D人体网格和骨架估计模型，这些模型在3DPW、EMDB和SSP-3D等几个公共基准上的表现远远优于最先进的水平。 et.al.|[2407.07532](http://arxiv.org/abs/2407.07532)|null|
|**2024-07-03**|**Cerebral cortex inspired representation of neural field network**|进化及其智能元素在探索中带来了刺激和挑战。然而，物种如何拥有记忆、检索记忆并保持连续性是根本问题。大多数现象只能由研究人员假设，通过实验验证它们是一个很大的挑战。将大脑视为理想的智能机器并对其进行建模，为计算算法开辟了新的维度。本文提出了一个假设，即类似于大脑皮层的记忆创造。大脑皮层的区域隐含着特定功能的特异性，构成了一维的矢量形式的神经场。整个皮层的神经场相互连接形成了一个网络。这些网络与生存本能、情绪和奖励相关联，构成了对暴露环境的记忆，或者说学习。具有多维控制点的图形工具NURBS被隐式地用于将这些网络表示为一组三次方程。通过数据学习是智能系统的主要模块，本文试图将数据转换为低维模式，而不是实时智能系统的现有绝对形式。 et.al.|[2407.04741](http://arxiv.org/abs/2407.04741)|null|
|**2024-07-01**|**Fast and Efficient: Mask Neural Fields for 3D Scene Segmentation**|理解3D场景是计算机视觉研究中的一个关键挑战，其应用跨越多个领域。最近在将2D视觉语言基础模型提取到神经领域（如NeRF和3DGS）方面取得的进展，使3D场景能够从2D多视图图像中进行开放式词汇分割，而不需要精确的3D注释。然而，虽然有效，但高维CLIP特征的每像素蒸馏会引入模糊性，并需要复杂的正则化策略，从而在训练过程中增加效率。本文介绍了MaskField，它能够在弱监督下利用神经场实现快速高效的3D开放式分词。与以前的方法不同，MaskField提取掩模而不是密集的高维CLIP特征。MaskFields使用神经场作为二进制掩模生成器，并使用SAM生成的掩模对其进行监督，并通过粗略的CLIP特征进行分类。MaskField通过在训练过程中自然引入SAM分割的对象形状而无需额外的正则化来克服模糊的对象边界。通过在训练过程中避免直接处理高维CLIP特征，MaskField与3DGS等显式场景表示特别兼容。我们广泛的实验表明，MaskField不仅超越了现有的最先进的方法，而且实现了非常快的收敛速度，仅需5分钟的训练就超越了以前的方法。我们希望MaskField能够激发对如何训练神经场以从2D模型中理解3D场景的进一步探索。 et.al.|[2407.01220](http://arxiv.org/abs/2407.01220)|null|
|**2024-07-15**|**3D Feature Distillation with Object-Centric Priors**|将自然语言与物理世界联系起来是一个无处不在的话题，在计算机视觉和机器人技术中有着广泛的应用。最近，CLIP等二维视觉语言模型因其在二维图像中具有令人印象深刻的开放词汇基础能力而得到了广泛推广。最近的工作旨在通过特征提取将2D CLIP特征提升到3D，但要么学习特定于场景的神经场，因此缺乏泛化能力，要么专注于需要访问多个摄像头视图的室内房间扫描数据，这在机器人操作场景中是不可行的。此外，相关方法通常在像素级融合特征，并假设所有相机视图都具有相同的信息量。在这项工作中，我们表明这种方法在接地精度和分割清晰度方面都会导致次优的3D特征。为了缓解这一问题，我们提出了一种多视图特征融合策略，该策略采用以对象为中心的先验来消除基于语义信息的无信息视图，并通过实例分割掩码在对象级别融合特征。为了提取我们以对象为中心的3D特征，我们生成了一个大规模的合成多视图数据集，其中包含杂乱的桌面场景，从3300多个独特的对象实例中生成了15k个场景，我们将其公之于众。我们表明，我们的方法在从单视图RGB-D重建3D CLIP特征的同时，提高了接地容量和空间一致性，从而偏离了测试时多个相机视图的假设。最后，我们证明了我们的方法可以推广到新的桌面领域，并可以在不进行微调的情况下重新用于3D实例分割，并证明了它在混乱中的语言引导机器人抓取中的实用性 et.al.|[2406.18742](http://arxiv.org/abs/2406.18742)|null|
|**2024-06-25**|**Masked Generative Extractor for Synergistic Representation and 3D Generation of Point Clouds**|在二维图像生成建模和表示学习领域，掩模生成编码器（MAGE）已经证明了生成建模与表示学习之间的协同潜力。受此启发，我们提出Point MAGE将这一概念扩展到点云数据。具体来说，该框架首先利用矢量量化变分自编码器（VQVAE）重建3D形状的神经场表示，从而学习点补丁的离散语义特征。随后，通过将掩蔽模型与可变掩蔽比相结合，我们实现了生成和表示学习的同步训练。此外，我们的框架与现有的点云自监督学习（SSL）模型无缝集成，从而提高了它们的性能。我们广泛评估了Point MAGE的表示学习和生成能力。在形状分类任务中，Point MAGE在ModelNet40数据集上的准确率达到94.2%，在ScanObjectNN数据集上达到92.9%（+1.3%）。此外，它在少数镜头学习和零件分割任务中取得了最新的性能。实验结果还证实，Point MAGE可以在无条件和有条件的设置下生成详细和高质量的3D形状。 et.al.|[2406.17342](http://arxiv.org/abs/2406.17342)|null|
|**2024-06-17**|**DistillNeRF: Perceiving 3D Scenes from Single-Glance Images by Distilling Neural Fields and Foundation Model Features**|我们提出了DistillNeRF，这是一个自监督学习框架，解决了在自动驾驶中从有限的2D观察中理解3D环境的挑战。我们的方法是一种可推广的前馈模型，它从稀疏的单帧多视图相机输入中预测丰富的神经场景表示，并通过可微渲染进行自我监督训练，以重建RGB、深度或特征图像。我们的第一个见解是通过生成密集的深度和虚拟相机目标进行训练，利用每场景优化的神经辐射场（NeRF），从而帮助我们的模型从稀疏的非重叠图像输入中学习3D几何。其次，为了学习语义丰富的3D表示，我们建议从预先训练的2D基础模型（如CLIP或DINOv2）中提取特征，从而实现各种下游任务，而不需要昂贵的3D人工注释。为了利用这两个见解，我们引入了一种新的模型架构，该架构具有两级提升-飞溅-射击编码器和参数化的稀疏分层体素表示。NuScenes数据集的实验结果表明，DistillNeRF在场景重建、新颖视图合成和深度估计方面明显优于现有的可比自监督方法；并且它允许竞争性的零样本3D语义占用预测，以及通过提取的基础模型特征来理解开放世界场景。演示和代码将在https://distillnerf.github.io/. et.al.|[2406.12095](http://arxiv.org/abs/2406.12095)|null|
|**2024-06-18**|**Effective Rank Analysis and Regularization for Enhanced 3D Gaussian Splatting**|从多视图图像进行3D重建是计算机视觉和图形学中的基本挑战之一。最近，3D高斯散斑（3DGS）已经成为一种有前景的技术，能够实时渲染高质量的3D重建。该方法利用3D高斯表示和基于图块的飞溅技术，绕过了昂贵的神经场查询。尽管3DGS具有潜力，但由于高斯收敛为具有一个主要方差的各向异性高斯，它遇到了挑战，包括针状伪影、次优几何形状和不准确的法线。我们建议使用有效秩分析来检查3D高斯基元的形状统计，并识别高斯真的收敛到有效秩为1的针状形状。为了解决这个问题，我们引入了有效秩作为正则化，它约束了高斯的结构。我们的新正则化方法增强了法线和几何重建，同时减少了针状伪影。该方法可以作为附加模块集成到其他3DGS变体中，在不损害视觉保真度的情况下提高其质量。 et.al.|[2406.11672](http://arxiv.org/abs/2406.11672)|null|
|**2024-06-13**|**Well-posedness and regularity of solutions to neural field problems with dendritic processing**|我们研究了最近提出的神经场模型的解决方案，其中树突被建模为源自体细胞层的垂直纤维连续体。由于电压通过具有非局域源的电缆方程沿树突方向传播，该模型具有各向异性扩散算子和突触耦合的积分项。因此，相应的柯西问题与经典神经场方程明显不同。我们证明了该问题的弱公式具有唯一解，其嵌入估计类似于非线性局部反应扩散方程的嵌入估计。我们的分析依赖于扰动无扩散问题的弱解，即一个标准的神经场，迄今为止还没有研究过弱问题。我们找到了有和没有扩散问题的严格渐近估计，并证明了这两个模型的解在有限时间间隔内以适当的范数保持接近。我们提供了微扰结果的数值证据。 et.al.|[2406.09222](http://arxiv.org/abs/2406.09222)|null|

<p align=right>(<a href=#updated-on-20240718>back to top</a>)</p>

[contributors-shield]: https://img.shields.io/github/contributors/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[contributors-url]: https://github.com/Vincentqyw/cv-arxiv-daily/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[forks-url]: https://github.com/Vincentqyw/cv-arxiv-daily/network/members
[stars-shield]: https://img.shields.io/github/stars/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[stars-url]: https://github.com/Vincentqyw/cv-arxiv-daily/stargazers
[issues-shield]: https://img.shields.io/github/issues/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[issues-url]: https://github.com/Vincentqyw/cv-arxiv-daily/issues

