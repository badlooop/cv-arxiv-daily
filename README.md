[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]

## Updated on 2024.12.12
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
|**2024-12-10**|**From an Image to a Scene: Learning to Imagine the World from a Million 360 Videos**|对物体和场景的三维（3D）理解在人类与世界互动的能力中起着关键作用，一直是计算机视觉、图形学和机器人学的一个活跃研究领域。大规模合成和以对象为中心的3D数据集已被证明在训练对对象有3D理解的模型方面是有效的。然而，由于缺乏大规模数据，将类似的方法应用于现实世界的对象和场景是困难的。视频是现实世界3D数据的潜在来源，但在规模上很难找到同一内容的不同但相应的视图。此外，标准视频具有在拍摄时确定的固定视点。这限制了从各种更多样化和潜在有用的角度访问场景的能力。我们认为，大规模360度视频可以解决这些局限性，提供：来自不同视角的可扩展对应帧。在本文中，我们介绍了360-1M，一个360度视频数据集，以及一个从不同视点按比例高效查找相应帧的过程。我们在360-1M上训练基于扩散的模型Odin。借助迄今为止最大的真实世界多视图数据集，Odin能够自由生成真实世界场景的新颖视图。与之前的方法不同，Odin可以在环境中移动相机，使模型能够推断场景的几何形状和布局。此外，我们在标准新颖视图合成和3D重建基准测试中表现出了改进的性能。 et.al.|[2412.07770](http://arxiv.org/abs/2412.07770)|null|
|**2024-12-10**|**SimVS: Simulating World Inconsistencies for Robust View Synthesis**|新颖的视图合成技术在静态场景中取得了令人印象深刻的结果，但在面对随意捕捉设置固有的不一致性时却举步维艰：变化的照明、场景运动和其他难以明确建模的意外效果。我们提出了一种利用生成视频模型来模拟捕获过程中可能出现的世界不一致的方法。我们使用这个过程以及现有的多视图数据集来创建合成数据，以训练一个多视图协调网络，该网络能够将不一致的观察结果协调成一致的3D场景。我们证明，我们的世界模拟策略在处理现实世界场景变化方面明显优于传统的增强方法，从而在存在各种具有挑战性的不一致的情况下实现了高度精确的静态3D重建。项目页面：https://alextrevithick.github.io/simvs et.al.|[2412.07696](http://arxiv.org/abs/2412.07696)|null|
|**2024-12-10**|**Faster and Better 3D Splatting via Group Training**|3D高斯散斑（3DGS）已成为一种强大的新型视图合成技术，通过其高斯基元表示在高保真场景重建方面表现出卓越的能力。然而，大量基元引起的计算开销对训练效率构成了重大瓶颈。为了克服这一挑战，我们提出了组训练，这是一种简单而有效的策略，可以将高斯基元组织成可管理的组，优化训练效率并提高渲染质量。这种方法与现有的3DGS框架（包括vanilla 3DGS和Mip Splatting）具有通用兼容性，在保持卓越合成质量的同时，始终实现加速训练。广泛的实验表明，我们简单的组训练策略在不同场景下实现了高达30%的收敛速度和更高的渲染质量。 et.al.|[2412.07608](http://arxiv.org/abs/2412.07608)|null|
|**2024-12-10**|**ResGS: Residual Densification of 3D Gaussian for Efficient Detail Recovery**|最近，3D高斯散斑（3D-GS）在新颖的视图合成中占主导地位，实现了高保真度和效率。然而，它往往难以捕捉到丰富的细节和完整的几何形状。我们的分析强调了3D-GS的一个关键局限性，这是由致密化中的固定阈值引起的，该阈值在阈值变化时平衡了几何覆盖与细节恢复。为了解决这个问题，我们引入了一种新的致密化方法，残差分割，该方法添加了一个降尺度高斯作为残差。我们的方法能够自适应地检索细节并补充缺失的几何体，同时实现渐进式细化。为了进一步支持这种方法，我们提出了一个名为ResGS的管道。具体来说，我们整合了一个高斯图像金字塔进行渐进式监督，并实施了一个选择方案，该方案优先考虑粗高斯图像随时间的致密化。大量实验表明，我们的方法达到了SOTA渲染质量。通过将我们的残差分割应用于各种3D-GS变体，可以实现一致的性能改进，强调其在基于3D GS的应用中的多功能性和更广泛的应用潜力。 et.al.|[2412.07494](http://arxiv.org/abs/2412.07494)|null|
|**2024-12-10**|**EventSplat: 3D Gaussian Splatting from Moving Event Cameras for Real-time Rendering**|我们介绍了一种通过高斯散斑在新的视图合成中使用事件相机数据的方法。事件摄像机提供卓越的时间分辨率和高动态范围。利用这些功能，我们可以在快速相机运动的情况下有效地应对新的视图合成挑战。为了初始化优化过程，我们的方法使用事件到视频模型中编码的先验知识。我们还使用样条插值来获得沿事件相机轨迹的高质量姿态。这提高了快速移动相机的重建质量，同时克服了传统上与基于事件的神经辐射场（NeRF）方法相关的计算限制。我们的实验评估表明，我们的结果比现有的基于事件的NeRF方法实现了更高的视觉保真度和更好的性能，同时渲染速度快了一个数量级。 et.al.|[2412.07293](http://arxiv.org/abs/2412.07293)|null|
|**2024-12-09**|**MV-DUSt3R+: Single-Stage Scene Reconstruction from Sparse Views In 2 Seconds**|最近的稀疏多视图场景重建技术，如DUSt3R和MASt3R，不再需要相机校准和相机姿态估计。然而，它们一次只处理一对视图来推断像素对齐的点图。当处理两个以上的视图时，在组合多个容易出错的成对重建之后，通常会进行昂贵的全局优化，这通常无法纠正成对重建错误。为了处理更多的视图、减少错误并缩短推理时间，我们提出了快速单级前馈网络MV-DUSt3R。其核心是多视图解码器块，它们在考虑一个参考视图的同时，在任意数量的视图之间交换信息。为了使我们的方法对参考视图选择具有鲁棒性，我们进一步提出了MV-DUSt3R+，它采用交叉参考视图块来融合不同参考视图选择之间的信息。为了进一步实现新颖的视图合成，我们通过添加和联合训练高斯溅射头来扩展这两种方法。多视图立体重建、多视图姿态估计和新颖视图合成的实验证实，我们的方法在现有技术的基础上有了显著改进。代码将发布。 et.al.|[2412.06974](http://arxiv.org/abs/2412.06974)|null|
|**2024-12-09**|**MAtCha Gaussians: Atlas of Charts for High-Quality Geometry and Photorealism From Sparse Views**|我们提出了一种新的外观模型，该模型同时实现了显式的高质量3D表面网格恢复和稀疏视图样本的逼真新视图合成。我们的核心思想是将底层场景几何网格建模为图表图集，我们使用2D高斯曲面（MAtCha-Gaussians）进行渲染。MAtCha从现成的单目深度估计器中提取高频场景表面细节，并通过高斯表面渲染对其进行细化。高斯表面实时附着在图表上，满足神经体积渲染的真实感和网格模型的清晰几何，即单个模型中两个看似矛盾的目标。MAtCha的核心是一种新的神经变形模型和一种结构损失，它保留了从学习的单眼深度中提取的精细表面细节，同时解决了它们的基本尺度模糊问题。广泛的实验验证结果表明，MAtCha的表面重建和真实感质量与顶级竞争者不相上下，但输入视图数量和计算时间大幅减少。我们相信MAtCha将成为视觉、图形和机器人中任何视觉应用的基础工具，这些应用除了照片级真实感外，还需要显式几何。我们的项目页面如下：https://anttwo.github.io/matcha/ et.al.|[2412.06767](http://arxiv.org/abs/2412.06767)|null|
|**2024-12-09**|**Deblur4DGS: 4D Gaussian Splatting from Blurry Monocular Video**|最近的4D重建方法取得了令人印象深刻的结果，但依赖于清晰的视频作为监督。然而，由于相机抖动和物体移动，视频中经常出现运动模糊，而现有的方法在使用此类视频重建4D模型时会渲染模糊的结果。尽管一些基于NeRF的方法试图解决这个问题，但由于在暴露时间内估计连续动态表示的不准确性，它们很难产生高质量的结果。受最近使用3D高斯散点（3DGS）进行3D运动轨迹建模的工作的鼓舞，我们建议将3DGS作为场景表示方式，并提出了第一个4D高斯散点框架，用于从模糊的单眼视频中重建高质量的4D模型，称为Deblur4DGS。具体来说，我们将曝光时间内的连续动态表示估计转换为曝光时间估计。此外，我们引入了曝光正则化来避免琐碎的解决方案，以及多帧和多分辨率一致性解决方案来减轻伪影。此外，为了更好地表示具有大运动的对象，我们建议使用模糊感知的可变规范高斯分布。除了新颖的视图合成之外，Deblur4DGS还可以应用于从多个角度改善模糊视频，包括去模糊、帧插值和视频稳定。对上述四项任务的广泛实验表明，Deblur4DGS优于最先进的4D重建方法。这些代码可在以下网址获得https://github.com/ZcsrenlongZ/Deblur4DGS. et.al.|[2412.06424](http://arxiv.org/abs/2412.06424)|null|
|**2024-12-07**|**Template-free Articulated Gaussian Splatting for Real-time Reposable Dynamic View Synthesis**|虽然动态场景的新颖视图合成取得了重大进展，但捕获对象的骨架模型并对其重新定位仍然是一项具有挑战性的任务。为了解决这个问题，在本文中，我们提出了一种新的方法，可以自动从视频中发现动态对象的相关骨架模型，而不需要特定于对象的模板。我们的方法利用3D高斯散点和超点来重建动态对象。将超点视为刚性部分，我们可以通过直观的线索发现潜在的骨架模型，并使用运动学模型对其进行优化。此外，应用自适应控制策略来避免冗余超点的出现。大量实验证明了我们的方法在获得可重新定位的3D对象方面的有效性和效率。我们的方法不仅可以实现出色的视觉保真度，还可以实时渲染高分辨率图像。 et.al.|[2412.05570](http://arxiv.org/abs/2412.05570)|null|
|**2024-12-10**|**Extrapolated Urban View Synthesis Benchmark**|真实感模拟器对于以视觉为中心的自动驾驶汽车（AV）的训练和评估至关重要。其核心是新颖视图合成（NVS），这是一种关键能力，可以生成各种看不见的视点，以适应飞行器广泛而连续的姿态分布。辐射场的最新进展，如3D高斯散斑，实现了实时速度的真实感渲染，并已广泛应用于大规模驾驶场景的建模。然而，通常使用具有高度相关的训练和测试视图的插值设置来评估它们的性能。相比之下，外推法（测试视图与训练视图存在较大偏差）仍然没有得到充分探索，限制了可推广仿真技术的进步。为了解决这一差距，我们利用公开可用的AV数据集，包括多个行程、多辆车和多个摄像头，构建了第一个外推城市景观合成（EUVS）基准。同时，我们对不同难度级别的最先进的高斯散布方法进行了定量和定性评估。我们的结果表明，高斯散点法容易对训练视图进行过拟合。此外，在大视图变化下，结合扩散先验和改进几何结构并不能从根本上改善NVS，这突显了对更稳健的方法和大规模训练的需求。我们已经发布了我们的数据，以帮助推进自动驾驶和城市机器人模拟技术。 et.al.|[2412.05256](http://arxiv.org/abs/2412.05256)|**[link](https://github.com/ai4ce/EUVS-Benchmark)**|

<p align=right>(<a href=#updated-on-20241212>back to top</a>)</p>

## 3D Reconstruction

|Publish Date|Title|Abstract|PDF|Code|
|---|---|---|---|---|
|**2024-12-10**|**From an Image to a Scene: Learning to Imagine the World from a Million 360 Videos**|对物体和场景的三维（3D）理解在人类与世界互动的能力中起着关键作用，一直是计算机视觉、图形学和机器人学的一个活跃研究领域。大规模合成和以对象为中心的3D数据集已被证明在训练对对象有3D理解的模型方面是有效的。然而，由于缺乏大规模数据，将类似的方法应用于现实世界的对象和场景是困难的。视频是现实世界3D数据的潜在来源，但在规模上很难找到同一内容的不同但相应的视图。此外，标准视频具有在拍摄时确定的固定视点。这限制了从各种更多样化和潜在有用的角度访问场景的能力。我们认为，大规模360度视频可以解决这些局限性，提供：来自不同视角的可扩展对应帧。在本文中，我们介绍了360-1M，一个360度视频数据集，以及一个从不同视点按比例高效查找相应帧的过程。我们在360-1M上训练基于扩散的模型Odin。借助迄今为止最大的真实世界多视图数据集，Odin能够自由生成真实世界场景的新颖视图。与之前的方法不同，Odin可以在环境中移动相机，使模型能够推断场景的几何形状和布局。此外，我们在标准新颖视图合成和3D重建基准测试中表现出了改进的性能。 et.al.|[2412.07770](http://arxiv.org/abs/2412.07770)|null|
|**2024-12-10**|**LoRA3D: Low-Rank Self-Calibration of 3D Geometric Foundation Models**|新兴的3D几何基础模型，如DUSt3R，为野外3D视觉任务提供了一种有前景的方法。然而，由于问题空间的高维特性和高质量3D数据的稀缺性，这些预训练模型仍然难以推广到许多具有挑战性的情况，例如有限的视图重叠或低光照。为了解决这个问题，我们提出了LoRA3D，这是一种高效的自校准管道，用于 $\textit{specialize}$预训练模型，使用它们自己的多视图预测来定位场景。以稀疏RGB图像为输入，我们利用稳健的优化技术来优化多视图预测，并将其对齐到全局坐标系中。特别是，我们将预测置信度纳入几何优化过程，自动重新加权置信度，以更好地反映点估计的准确性。我们使用校准的置信度为校准视图生成高质量的伪标签，并使用低秩自适应（LoRA）对伪标签数据上的模型进行微调。我们的方法不需要任何外部先验或手动标签。它在$\textbf{单个标准GPU上仅需5分钟}$即可完成自校准过程。每个低级别适配器只需要$\textbf{18MB}$的存储空间。我们在Replica、TUM和Waymo Open数据集中的$\textbf{160多个场景}$上评估了我们的方法，在3D重建、多视图姿态估计和新颖视图渲染方面实现了高达$\textbf{88%的性能改进}$ 。 et.al.|[2412.07746](http://arxiv.org/abs/2412.07746)|null|
|**2024-12-10**|**SimVS: Simulating World Inconsistencies for Robust View Synthesis**|新颖的视图合成技术在静态场景中取得了令人印象深刻的结果，但在面对随意捕捉设置固有的不一致性时却举步维艰：变化的照明、场景运动和其他难以明确建模的意外效果。我们提出了一种利用生成视频模型来模拟捕获过程中可能出现的世界不一致的方法。我们使用这个过程以及现有的多视图数据集来创建合成数据，以训练一个多视图协调网络，该网络能够将不一致的观察结果协调成一致的3D场景。我们证明，我们的世界模拟策略在处理现实世界场景变化方面明显优于传统的增强方法，从而在存在各种具有挑战性的不一致的情况下实现了高度精确的静态3D重建。项目页面：https://alextrevithick.github.io/simvs et.al.|[2412.07696](http://arxiv.org/abs/2412.07696)|null|
|**2024-12-10**|**Image Reconstruction in Cone Beam Computed Tomography Using Controlled Gradient Sparsity**|全变分（TV）正则化是一种用于不适定成像问题的流行重建方法，尤其适用于具有分段常数目标的应用。然而，到目前为止，将电视用于医学锥束计算机X射线断层扫描（CBCT）一直受到限制，主要是因为在临床相关的3D分辨率下计算量很大，并且难以选择正则化参数。这里提出了一种有效的最小化算法，结合基于控制理论的动态参数调整。结果是一种在临床可接受的时间内运行的全自动3D重建方法。投影数据和系统几何形状之上的输入是重建的理想稀疏度。这可以从CT扫描图谱中确定，或者用作易于调整的参数，具有直接的解释。 et.al.|[2412.07465](http://arxiv.org/abs/2412.07465)|null|
|**2024-12-09**|**Generative Densification: Learning to Densify Gaussians for High-Fidelity Generalizable 3D Reconstruction**|广义前馈高斯模型通过利用大型多视图数据集的先验知识，在稀疏视图3D重建方面取得了重大进展。然而，由于高斯模型的数量有限，这些模型往往难以表示高频细节。虽然在每场景3D高斯溅射（3D-GS）优化中使用的致密化策略可以适应前馈模型，但它可能不适合一般场景。在本文中，我们提出了生成致密化，这是一种有效且可推广的方法来致密前馈模型生成的高斯分布。与迭代分割和克隆原始高斯参数的3D-GS致密化策略不同，我们的方法从前馈模型中对特征表示进行上采样，并在一次前向传递中生成相应的精细高斯分布，利用嵌入的先验知识来增强泛化。对象级和场景级重建任务的实验结果表明，我们的方法在相当或更小的模型尺寸下优于最先进的方法，在表示精细细节方面取得了显著的改进。 et.al.|[2412.06234](http://arxiv.org/abs/2412.06234)|null|
|**2024-12-08**|**Doppelgangers++: Improved Visual Disambiguation with Geometric 3D Features**|精确的3D重建经常受到视觉混叠的阻碍，在视觉混叠中，视觉上相似但不同的表面（又名二重身）被错误地匹配。这些伪匹配扭曲了运动结构（SfM）过程，导致模型元素错位和精度降低。之前的努力通过在精心策划的数据集上训练的CNN分类器解决了这个问题，但这些方法很难在不同的现实世界场景中推广，并且可能需要大量的参数调整。在这项工作中，我们提出了Doppelgangers++，这是一种增强doppelganger检测并提高3D重建精度的方法。我们的贡献包括一个多样化的训练数据集，该数据集整合了来自日常场景的地理标记图像，将鲁棒性扩展到基于地标的数据集之外。我们进一步提出了一种基于Transformer的分类器，该分类器利用了MASt3R模型中的3D感知特征，在域内和域外测试中实现了卓越的精确度和召回率。Doppelgangers++无缝集成到标准SfM和MASt3R SfM管道中，在各种场景中提供效率和适应性。为了评估SfM的准确性，我们引入了一种基于地理标签的自动化方法来验证重建模型，从而消除了手动检查的需要。通过大量实验，我们证明Doppelgangers++显著增强了成对视觉消歧，并在复杂和多样化的场景中提高了3D重建质量。 et.al.|[2412.05826](http://arxiv.org/abs/2412.05826)|null|
|**2024-12-06**|**Perturb-and-Revise: Flexible 3D Editing with Generative Trajectories**|随着基于文本的扩散模型的发展，3D重建和基于文本的3D编辑领域取得了显著进步。虽然现有的3D编辑方法擅长修改颜色、纹理和风格，但它们难以应对广泛的几何或外观变化，从而限制了它们的应用。我们提出了扰动和修改，这使得各种NeRF编辑成为可能。首先，我们通过随机初始化来扰动NeRF参数，以创建一个通用的初始化。我们通过分析局部损失景观自动确定扰动幅度。然后，我们通过生成轨迹修改编辑后的NeRF。结合生成过程，我们施加身份保持梯度来细化编辑的NeRF。大量实验表明，Perturb和Revise有助于在3D中灵活、有效和一致地编辑颜色、外观和几何图形。有关360度结果，请访问我们的项目页面：https://susunghong.github.io/Perturb-and-Revise. et.al.|[2412.05279](http://arxiv.org/abs/2412.05279)|null|
|**2024-12-05**|**MetaFormer: High-fidelity Metalens Imaging via Aberration Correcting Transformers**|Metalens是一种新兴的光学系统，具有不可替代的优点，因为它可以以超薄和紧凑的尺寸制造，这显示了医学成像和增强/虚拟现实（AR/VR）等各种应用的巨大前景。尽管其在小型化方面具有优势，但其实用性受到严重像差和失真的限制，这会显著降低图像质量。之前的几项技术试图解决不同类型的像差，但其中大多数主要是为传统的笨重镜头设计的，不足以弥补金属透镜的严重像差。虽然有专门针对金属透镜的像差校正方法，但它们仍然达不到恢复质量。在这项工作中，我们提出了MetaFormer，这是一种用于金属透镜捕获图像的像差校正框架，利用视觉变换器（ViT），在各种图像恢复任务中显示出卓越的恢复性能。具体来说，我们设计了一种多自适应滤波器引导（MAFG），其中多个维纳滤波器通过各种噪声细节平衡来丰富退化的输入图像，从而提高了输出恢复质量。此外，我们引入了一个空间和转置自我注意融合（STAF）模块，该模块聚合了空间自我注意和转置自我注意力模块的特征，以进一步改善像差校正。我们进行了广泛的实验，包括校正畸变图像和视频，以及从退化图像中进行干净的3D重建。所提出的方法明显优于先前的技术。我们进一步制造了一个金属透镜，并通过恢复在野外用制造的金属透镜捕获的图像来验证MetaFormer的实用性。代码和预训练模型可在以下网址获得https://benhenryl.github.io/MetaFormer et.al.|[2412.04591](http://arxiv.org/abs/2412.04591)|null|
|**2024-12-05**|**DualPM: Dual Posed-Canonical Point Maps for 3D Shape and Pose Reconstruction**|数据表示的选择是几何任务中深度学习成功的关键因素。例如，DUSt3R最近引入了视点不变点图的概念，推广了深度预测，并表明可以将静态场景3D重建中的所有关键问题简化为预测这些点图。在本文中，我们为一个非常不同的问题开发了一个类似的概念，即可变形物体的3D形状和姿态的重建。为此，我们引入了双点图（DualPM），其中从{same}图像中提取一对点图，一个将像素与其在物体上的3D位置相关联，另一个将其与静止物体姿势的规范版本相关联。我们还将点图扩展到无模重建，通过自遮挡来获得物体的完整形状。我们表明，3D重建和3D姿态估计简化为双PM的预测。我们实证证明，这种表示是深度网络预测的一个很好的目标；具体来说，我们考虑对马进行建模，表明DualPM可以纯粹在由马的单个模型组成的3D合成数据上进行训练，同时很好地推广到真实图像。有了这个，我们大大改进了以前用于这类对象的3D分析和重建的方法。 et.al.|[2412.04464](http://arxiv.org/abs/2412.04464)|null|
|**2024-12-05**|**Likelihood-Scheduled Score-Based Generative Modeling for Fully 3D PET Image Reconstruction**|使用预训练的基于分数的生成模型（SGMs）进行医学图像重建比其他现有的最先进的深度学习重建方法具有优势，包括提高了对不同扫描仪设置的弹性和先进的图像分布建模。基于SGM的重建最近被应用于模拟正电子发射断层扫描（PET）数据集，与最先进的技术相比，显示出分布外病变的对比度恢复得到了改善。然而，现有的基于SGM从PET数据重建的方法存在重建缓慢、超参数调整繁重和切片不一致效应（在3D中）的问题。在这项工作中，我们提出了一种实用的全3D重建方法，通过将SGM逆扩散过程的可能性与最大似然期望最大化算法的当前迭代相匹配，加速重建并减少关键超参数的数量。使用模拟 $[^{18}$F]DPA-714数据集的低计数重建示例，我们表明我们的方法可以匹配或改进现有最先进的基于SGM的PET重建的NRMSE和SSIM，同时减少重建时间和对超参数调整的需求。我们根据最先进的监督和传统重建算法评估我们的方法。最后，我们首次展示了基于SGM的真实3D PET数据重建的实现，特别是$[^{18}$ F]DPA-714数据，我们在其中集成了垂直预训练的SGM，以消除切片不一致问题。 et.al.|[2412.04339](http://arxiv.org/abs/2412.04339)|null|

<p align=right>(<a href=#updated-on-20241212>back to top</a>)</p>

## Diffusion

|Publish Date|Title|Abstract|PDF|Code|
|---|---|---|---|---|
|**2024-12-10**|**Video Motion Transfer with Diffusion Transformers**|我们提出了DiTFlow，这是一种将参考视频的运动转换为新合成视频的方法，专为扩散变换器（DiT）设计。我们首先使用预训练的DiT处理参考视频，以分析跨帧注意力图，并提取一个称为注意力运动流（AMF）的逐块运动信号。我们通过利用AMF损失优化延迟来生成再现参考视频运动的视频，从而以基于优化、无需训练的方式指导潜在去噪过程。我们还将我们的优化策略应用于变压器位置嵌入，从而增强零样本运动传递能力。我们根据最近发布的方法对DiTFlow进行了评估，在多个指标和人工评估方面都表现出色。 et.al.|[2412.07776](http://arxiv.org/abs/2412.07776)|**[link](https://github.com/ditflow/ditflow)**|
|**2024-12-10**|**Efficient Diversity-Preserving Diffusion Alignment via Gradient-Informed GFlowNets**|虽然人们通常通过收集目标下游任务的数据集来训练大型扩散模型，但通常希望在一些由专家设计或从小规模数据集中学习的奖励函数上对齐和微调预训练的扩散模型。用于微调扩散模型的现有方法通常存在生成样本缺乏多样性、缺乏先验保存和/或微调收敛缓慢的问题。受生成流网络（GFlowNet）最近取得的成功的启发，这是一类用奖励函数的非标准化密度进行采样的概率模型，我们提出了一种新的GFlowNet方法，称为Nabla GFlowNet（缩写为 $\Nabla$-GFlowNet），这是第一种利用奖励梯度中丰富信号的GFlowNet方法，以及一个名为$\nlaba$-DB的目标及其变体残差$\Nabla$ -DB，旨在预先保持扩散对齐。我们证明，我们提出的方法在不同的现实奖励函数上实现了大规模文本条件图像扩散模型Stable Diffusion的快速、多样性和先验保持对齐。 et.al.|[2412.07775](http://arxiv.org/abs/2412.07775)|null|
|**2024-12-10**|**From Slow Bidirectional to Fast Causal Video Generators**|当前的视频扩散模型实现了令人印象深刻的生成质量，但由于双向注意力依赖，在交互式应用程序中举步维艰。生成单个帧需要模型处理整个序列，包括未来。我们通过将预训练的双向扩散变换器调整为动态生成帧的因果变换器来解决这一局限性。为了进一步减少延迟，我们将分布匹配蒸馏（DMD）扩展到视频，将50步扩散模型蒸馏成4步生成器。为了实现稳定和高质量的蒸馏，我们引入了一种基于教师ODE轨迹的学生初始化方案，以及一种非对称蒸馏策略，该策略通过双向教师监督因果学生模型。这种方法有效地减轻了自回归生成中的误差累积，即使在短片段上进行训练，也可以进行长时间的视频合成。得益于KV缓存，我们的模型支持在单个GPU上以9.4 FPS的速度快速流式生成高质量视频。我们的方法还能够以零样本方式实现流式视频到视频的翻译、图像到视频和动态提示。未来，我们将基于开源模型发布代码。 et.al.|[2412.07772](http://arxiv.org/abs/2412.07772)|null|
|**2024-12-10**|**From an Image to a Scene: Learning to Imagine the World from a Million 360 Videos**|对物体和场景的三维（3D）理解在人类与世界互动的能力中起着关键作用，一直是计算机视觉、图形学和机器人学的一个活跃研究领域。大规模合成和以对象为中心的3D数据集已被证明在训练对对象有3D理解的模型方面是有效的。然而，由于缺乏大规模数据，将类似的方法应用于现实世界的对象和场景是困难的。视频是现实世界3D数据的潜在来源，但在规模上很难找到同一内容的不同但相应的视图。此外，标准视频具有在拍摄时确定的固定视点。这限制了从各种更多样化和潜在有用的角度访问场景的能力。我们认为，大规模360度视频可以解决这些局限性，提供：来自不同视角的可扩展对应帧。在本文中，我们介绍了360-1M，一个360度视频数据集，以及一个从不同视点按比例高效查找相应帧的过程。我们在360-1M上训练基于扩散的模型Odin。借助迄今为止最大的真实世界多视图数据集，Odin能够自由生成真实世界场景的新颖视图。与之前的方法不同，Odin可以在环境中移动相机，使模型能够推断场景的几何形状和布局。此外，我们在标准新颖视图合成和3D重建基准测试中表现出了改进的性能。 et.al.|[2412.07770](http://arxiv.org/abs/2412.07770)|null|
|**2024-12-10**|**Make-A-Texture: Fast Shape-Aware Texture Generation in 3 Seconds**|我们提出了Make-A-Texture，这是一个新的框架，可以根据给定3D几何体的文本提示有效地合成高分辨率纹理图。我们的方法通过深度感知修复扩散模型，在自动视图选择算法确定的优化视点序列中，逐步生成跨多个视点一致的纹理。我们的方法的一个显著特点是其卓越的效率，在单个NVIDIA H100 GPU上仅需3.07秒的端到端运行时间内即可实现完整的纹理生成，明显优于现有方法。这种加速是通过扩散模型的优化和专门的反投影方法实现的。此外，我们的方法通过选择性地屏蔽开放表面对象的非正面和内部面，减少了反投影阶段的伪影。实验结果表明，Make-A-Texture的质量与其他最先进的方法相匹配或超过。我们的工作显著提高了纹理生成模型在现实世界3D内容创建中的适用性和实用性，包括交互式创建和文本引导纹理编辑。 et.al.|[2412.07766](http://arxiv.org/abs/2412.07766)|null|
|**2024-12-10**|**Repurposing Pre-trained Video Diffusion Models for Event-based Video Interpolation**|视频帧插值旨在恢复观察帧之间的真实缺失帧，从低帧率视频生成高帧率视频。然而，如果没有额外的引导，帧之间的大运动会使这个问题变得不适定。基于事件的视频帧插值（EVFI）通过使用稀疏、高时间分辨率的事件测量作为运动引导来解决这一挑战。该指南允许EVFI方法显著优于仅帧方法。然而，迄今为止，EVFI方法依赖于有限的成对事件帧训练数据集，严重限制了它们的性能和泛化能力。在这项工作中，我们通过将在互联网规模数据集上训练的预训练视频扩散模型适应EVFI来克服有限的数据挑战。我们在真实世界的EVFI数据集上实验验证了我们的方法，包括我们引入的一种新方法。我们的方法优于现有的方法，并且在相机上的泛化能力远远好于现有的方法。 et.al.|[2412.07761](http://arxiv.org/abs/2412.07761)|null|
|**2024-12-10**|**SynCamMaster: Synchronizing Multi-Camera Video Generation from Diverse Viewpoints**|视频扩散模型的最新进展表明，它在模拟现实世界动态和保持3D一致性方面具有出色的能力。这一进展激励我们研究这些模型的潜力，以确保各种视点之间的动态一致性，这是虚拟拍摄等应用程序非常理想的功能。与专注于4D重建的单个对象的多视图生成的现有方法不同，我们的兴趣在于从任意视点生成开放世界视频，并结合6自由度相机姿势。为了实现这一目标，我们提出了一种即插即用模块，该模块增强了预训练的文本到视频模型，用于多摄像机视频生成，确保不同视点的内容一致。具体来说，我们引入了一个多视图同步模块，以保持这些视点之间的外观和几何一致性。鉴于高质量训练数据的稀缺性，我们设计了一种混合训练方案，该方案利用多摄像头图像和单眼视频来补充虚幻引擎渲染的多摄像头视频。此外，我们的方法能够实现有趣的扩展，例如从新的视角重新渲染视频。我们还发布了一个名为SynCamVideo dataset的多视图同步视频数据集。项目页面：https://jianhongbai.github.io/SynCamMaster/. et.al.|[2412.07760](http://arxiv.org/abs/2412.07760)|**[link](https://github.com/kwaivgi/syncammaster)**|
|**2024-12-10**|**3DTrajMaster: Mastering 3D Trajectory for Multi-Entity Motion in Video Generation**|本文旨在操纵视频生成中的多实体3D运动。先前的可控视频生成方法主要利用2D控制信号来操纵对象运动，并取得了显著的合成效果。然而，2D控制信号在表达物体运动的3D性质方面固有地受到限制。为了克服这个问题，我们引入了3DTrajMaster，这是一种鲁棒控制器，可以在给定用户所需的实体6DoF姿态（位置和旋转）序列的情况下，调节3D空间中的多实体动力学。我们方法的核心是一个即插即用的3D运动接地对象注入器，它通过门控的自我关注机制将多个输入实体与其各自的3D轨迹融合在一起。此外，我们利用注入器架构来保留视频扩散先验，这对泛化能力至关重要。为了减轻视频质量的下降，我们在训练过程中引入了域适配器，并在推理过程中采用了退火采样策略。为了解决缺乏合适训练数据的问题，我们构建了一个360运动数据集，该数据集首先将收集到的3D人类和动物资产与GPT生成的轨迹相关联，然后在不同的3D UE平台上用12个均匀环绕的摄像头捕捉它们的运动。大量实验表明，3DTrajMaster在控制多实体3D运动的精度和泛化方面都达到了新的水平。项目页面：http://fuxiao0719.github.io/projects/3dtrajmaster et.al.|[2412.07759](http://arxiv.org/abs/2412.07759)|null|
|**2024-12-10**|**PortraitTalk: Towards Customizable One-Shot Audio-to-Talking Face Generation**|音频驱动的说话面生成是数字通信中一项具有挑战性的任务。尽管在该领域取得了重大进展，但大多数现有方法都集中在音频嘴唇同步上，往往忽视了视觉质量、定制和泛化等方面，而这些方面对于生成逼真的说话面孔至关重要。为了解决这些局限性，我们引入了一个新颖的、可定制的单次音频驱动的说话脸生成框架，名为PortraitTalk。我们提出的方法利用了一个由两个主要组件组成的潜在扩散框架：IdentityNet和AnimateNet。IdentityNet旨在在生成的视频帧中保持一致的身份特征，而AnimateNet旨在增强时间一致性和运动一致性。该框架还将音频输入与参考图像集成在一起，从而减少了对现有方法中普遍存在的参考风格视频的依赖。PortraitTalk的一个关键创新是通过解耦的交叉注意力机制结合文本提示，这大大扩展了对生成视频的创造性控制。通过广泛的实验，包括新开发的评估指标，我们的模型表现出了优于最先进方法的性能，为生成适用于现实世界应用的可定制逼真说话脸树立了新的标准。 et.al.|[2412.07754](http://arxiv.org/abs/2412.07754)|null|
|**2024-12-10**|**Structural, Electronic, and Li-ion Adsorption Properties of PolyPyGY Explored by First-Principles and Machine Learning Simulations: A New Multi-Ringed 2D Carbon Allotrope**|二维（2D）碳材料因其独特的结构框架和电子行为而被广泛研究，作为能量转换和储存应用的替代品。本研究提出了一种新型的二维碳同素异形体，聚合吡喃石墨烯（PolyPyGY），其特征是具有多孔结构的4、5、6、8和16元环的多环结构。使用第一性原理计算和机器学习技术，我们探索了它的结构、电子、机械、光学和锂离子存储特性。通过密度泛函微扰理论框架评估的振动特性证实了其结构稳定性。此外，在1000 K下的从头计算分子动力学模拟证明了其热弹性，没有观察到键断裂或重构。电子能带结构显示出金属性质，材料表现出各向异性弹性特性，杨氏模量在421至664 GPa之间变化，表明具有良好的机械稳定性。此外，锂扩散研究表明，低能量势垒（0.05-0.9 eV）和高扩散系数（ $>6$times$10$^{-6}$cm$^{2}$ /s），以及1.2 V的稳定开路电压。这些结果突显了PolyPyGY作为锂离子电池高效耐用阳极材料的潜力，具有快速锂离子扩散、稳定嵌入和充放电循环期间性能一致的特点。 et.al.|[2412.07753](http://arxiv.org/abs/2412.07753)|null|

<p align=right>(<a href=#updated-on-20241212>back to top</a>)</p>

## NeRF

|Publish Date|Title|Abstract|PDF|Code|
|---|---|---|---|---|
|**2024-12-08**|**Unsupervised Multi-Parameter Inverse Solving for Reducing Ring Artifacts in 3D X-Ray CBCT**|由于X射线探测器的非理想响应，环形伪影在3D锥束计算机断层扫描（CBCT）中很普遍，严重降低了成像质量和可靠性。当前最先进的（SOTA）环伪影减少（RAR）算法依赖于广泛的成对CT样本进行监督学习。虽然有效，但这些方法并不能完全捕捉到环形伪影的物理特征，导致应用于域外数据时性能明显下降。此外，它们在3D CBCT中的应用受到高内存需求的限制。在这项工作中，我们介绍了\textbf{Riner}，这是一种将3D CBCT RAR表述为多参数逆问题的无监督方法。我们的核心创新是将X射线探测器响应参数化为微分物理模型中的可解变量。通过联合优化神经场以表示无伪影的CT图像，并直接从原始测量值估计响应参数，Riner消除了对外部训练数据的需求。此外，它还可适应不同的CT几何形状，提高了实用性。在模拟和真实数据集上的实证结果表明，Riner在性能上优于现有的SOTA RAR方法。 et.al.|[2412.05853](http://arxiv.org/abs/2412.05853)|null|
|**2024-12-06**|**Physics-informed reduced order model with conditional neural fields**|本研究提出了用于降阶建模（CNF-ROM）框架的条件神经场，以近似参数化偏微分方程（PDE）的解。该方法将用于随时间建模潜在动力学的参数神经ODE（PNODE）与从相应潜在状态重建PDE解的解码器相结合。我们为CNF-ROM引入了一个物理知情学习目标，其中包括两个关键组成部分。首先，该框架使用基于坐标的神经网络通过自动微分计算空间导数并应用时间导数的链式规则来计算和最小化PDE残差。其次，使用近似距离函数（ADF）施加精确的初始和边界条件（IC/BC）[Sukumar和Srivastava，CMAME，2022]。然而，当ADFs的二阶或高阶导数在边界的连接点处变得不稳定时，ADFs引入了一种权衡。为了解决这个问题，我们引入了一个受[Gladstone等人，NeurIPS ML4PS研讨会，2022年]启发的辅助网络。我们的方法通过参数外推和插值、时间外推以及与解析解的比较得到了验证。 et.al.|[2412.05233](http://arxiv.org/abs/2412.05233)|null|
|**2024-12-06**|**Spatially-Adaptive Hash Encodings For Neural Surface Reconstruction**|位置编码是神经场景重建方法的一个常见组成部分，它提供了一种将神经场的学习偏向于更粗糙或更精细表示的方法。当前的神经表面重建方法使用“一刀切”的编码方法，在所有场景中选择一组固定的编码函数，从而产生偏差。当前最先进的表面重建方法利用基于网格的多分辨率哈希编码来恢复高细节几何。我们提出了一种学习方法，通过掩盖以单独网格分辨率存储的特征的贡献，允许网络根据空间选择其编码基础。由此产生的空间自适应方法允许网络在不引入噪声的情况下适应更宽的频率范围。我们在标准基准曲面重建数据集上测试了我们的方法，并在两个基准数据集上实现了最先进的性能。 et.al.|[2412.05179](http://arxiv.org/abs/2412.05179)|null|
|**2024-12-06**|**DNF: Unconditional 4D Generation with Dictionary-based Neural Fields**|虽然通过基于扩散的形状3D生成模型取得了显著成功，但由于物体变形的复杂性，4D生成建模仍然具有挑战性。我们提出了DNF，这是一种用于无条件生成建模的新4D表示，它有效地对具有解纠缠形状和运动的可变形形状进行建模，同时捕获变形对象中的高保真细节。为了实现这一点，我们提出了一种字典学习方法，将4D运动与形状作为神经场进行分离。形状和运动都表示为学习潜在空间，其中每个可变形形状由其形状和运动全局潜在码、形状特定系数向量和共享字典信息表示。这在学习词典中捕获了特定形状的细节和全局共享信息。我们基于字典的表示法很好地平衡了保真度、连续性和压缩性——结合基于变换器的扩散模型，我们的方法能够生成有效、高保真的4D动画。 et.al.|[2412.05161](http://arxiv.org/abs/2412.05161)|null|
|**2024-12-04**|**Theoretical / numerical study of modulated traveling waves in inhibition stabilized networks**|我们证明了实线上神经场方程行波解的线性化稳定性原理。此外，我们提供了行波附近有限维不变中心流形的存在性，这使得研究行波的分叉成为可能。最后，研究了调制行波的光谱特性。提供了计算调制行波的数值方案。然后，我们将这些结果和方法应用于研究抑制稳定状态下的神经场模型。我们展示了行进脉冲的Fold、Hopf和Bodgdanov-Takens分叉。此外，我们继续将调制行进脉冲作为两个神经群体时间尺度比的函数，并展示了调制行进脉冲蜿蜒的数值证据。 et.al.|[2412.03613](http://arxiv.org/abs/2412.03613)|null|
|**2024-12-04**|**Sparse-view Pose Estimation and Reconstruction via Analysis by Generative Synthesis**|推断一组多视图图像背后的3D结构通常需要解决两个相互依赖的任务——精确的3D重建需要精确的相机姿态，预测相机姿态依赖于（隐式或显式）对底层3D进行建模。经典的综合分析框架将这一推断视为一种联合优化，旨在解释观察到的像素，最近的实例通过基于梯度下降的初始姿态估计的姿态细化来学习表达性的3D表示（例如神经场）。然而，给定一组稀疏的观测视图，观测可能无法提供足够的直接证据来获得完整准确的3D。此外，姿势估计中的大误差可能不容易纠正，并可能进一步降低推断的3D。为了在这种具有挑战性的设置中实现稳健的3D重建和姿态估计，我们提出了SparseAGS，这是一种通过以下方式调整这种综合分析方法的方法：a）将基于新视图合成的生成先验与光度目标结合起来，以提高推断的3D的质量，b）明确地推理异常值，并使用基于连续优化策略的离散搜索来纠正它们。我们结合几个现成的姿态估计系统，在真实世界和合成数据集中验证我们的框架作为初始化。我们发现，它显著提高了基础系统的姿态精度，同时产生了高质量的3D重建，其效果优于当前多视图重建基线的结果。 et.al.|[2412.03570](http://arxiv.org/abs/2412.03570)|null|
|**2024-12-04**|**RoDyGS: Robust Dynamic Gaussian Splatting for Casual Videos**|动态视图合成（DVS）近年来取得了显著进展，在降低计算成本的同时实现了高保真渲染。尽管取得了进展，但从休闲视频中优化动态神经场仍然具有挑战性，因为这些视频不提供直接的3D信息，如相机轨迹或底层场景几何形状。在这项工作中，我们介绍了RoDyGS，这是一个用于从休闲视频中动态高斯散布的优化管道。它通过分离动态和静态图元有效地学习场景的运动和底层几何，并通过结合运动和几何正则化项确保学习到的运动和几何在物理上是合理的。我们还介绍了一个全面的基准测试Kubric MRig，它提供了广泛的相机和物体运动以及同时的多视图捕捉，这是以前基准测试中没有的功能。实验结果表明，与现有的无姿态静态神经场相比，所提出的方法明显优于之前的无姿态动态神经场，并实现了具有竞争力的渲染质量。代码和数据可在以下网址公开获取https://rodygs.github.io/. et.al.|[2412.03077](http://arxiv.org/abs/2412.03077)|null|
|**2024-12-04**|**TREND: Unsupervised 3D Representation Learning via Temporal Forecasting for LiDAR Perception**|众所周知，标记LiDAR点云既费时又耗能，这促使最近的无监督3D表示学习方法通过预训练权重来减轻LiDAR感知中的标记负担。几乎所有现有的工作都集中在LiDAR点云的单个帧上，而忽略了时间LiDAR序列，这自然解释了物体运动（及其语义）。相反，我们提出了TREND，即神经场的时间重渲染，通过无监督的方式预测未来的观测来学习3D表示。与遵循传统对比学习或掩码自动编码范式的现有工作不同，TREND通过循环嵌入方案集成了3D预训练的预测，以生成跨时间的3D嵌入，并通过时间神经场来表示3D场景，我们使用可微渲染来计算损失。据我们所知，TREND是第一项关于无监督3D表示学习的时间预测的工作。我们在流行数据集（包括NuScenes、Once和Waymo）上评估TREND在下游3D物体检测任务上的表现。实验结果表明，与之前的SOTA无监督3D预训练方法相比，TREND带来了高达90%的改进，并且通常改善了跨数据集的不同下游模型，这表明时间预测确实为LiDAR感知带来了改善。代码和模型将发布。 et.al.|[2412.03054](http://arxiv.org/abs/2412.03054)|null|
|**2024-12-02**|**CRAYM: Neural Field Optimization via Camera RAY Matching**|我们将相机光线匹配（CRAYM）引入到多视图图像中相机姿态和神经场的联合优化中。被称为特征体积的优化区域可以通过相机光线进行“探测”，以进行新颖的视图合成（NVS）和3D几何重建。匹配相机光线的一个关键原因是，相机光线可以通过特征体积进行参数化，以携带几何和光度信息，而不是像以前的工作那样匹配像素。涉及相机光线和场景渲染的多视图一致性可以自然地整合到联合优化和网络训练中，以施加物理上有意义的约束，提高几何重建和照片级真实感渲染的最终质量。我们通过关注穿过输入图像中关键点的相机光线来制定每条光线的优化和匹配光线的一致性，以提高场景对应的效率和准确性。沿特征体积的累积光线特征提供了一种在错误光线匹配中忽略相干约束的方法。我们通过与最先进的替代方案进行定性和定量比较，证明了CRAYM在NVS和几何重建、过密或稀疏视图设置方面的有效性。 et.al.|[2412.01618](http://arxiv.org/abs/2412.01618)|null|
|**2024-11-29**|**Dynamic Neural Curiosity Enhances Learning Flexibility for Autonomous Goal Discovery**|机器人新目标的自主学习仍然是一个需要解决的复杂问题。在这里，我们提出了一个好奇心影响学习灵活性的模型。为了做到这一点，本文建议通过从Locus Coeruleus去甲肾上腺素系统以及认知持久性和视觉习惯化等各种认知过程中获得灵感，将好奇心和注意力结合起来。我们通过在一组难度不同的物体上模拟机器人手臂来应用我们的方法。机器人首先通过自下而上的注意力，通过带有抑制返回机制的运动牙牙学语，发现新的目标，然后由于好奇心机制中产生的神经活动，开始学习目标。该架构使用动态神经场建模，通过使用多层感知器实现的正向和反向模型来支持目标的学习，例如向不同方向推动物体。采用动态神经场来模拟好奇心、习惯性和持久性，使机器人能够根据对象展示各种学习轨迹。此外，该方法在学习相似目标以及在探索和开发之间不断切换方面表现出有趣的特性。 et.al.|[2412.00152](http://arxiv.org/abs/2412.00152)|**[link](https://github.com/rouzinho/Dynamic-Neural-Curiosity)**|

<p align=right>(<a href=#updated-on-20241212>back to top</a>)</p>

[contributors-shield]: https://img.shields.io/github/contributors/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[contributors-url]: https://github.com/Vincentqyw/cv-arxiv-daily/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[forks-url]: https://github.com/Vincentqyw/cv-arxiv-daily/network/members
[stars-shield]: https://img.shields.io/github/stars/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[stars-url]: https://github.com/Vincentqyw/cv-arxiv-daily/stargazers
[issues-shield]: https://img.shields.io/github/issues/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[issues-url]: https://github.com/Vincentqyw/cv-arxiv-daily/issues

