[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]

## Updated on 2024.12.10
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
|**2024-12-09**|**MAtCha Gaussians: Atlas of Charts for High-Quality Geometry and Photorealism From Sparse Views**|我们提出了一种新的外观模型，该模型同时实现了显式的高质量3D表面网格恢复和稀疏视图样本的逼真新视图合成。我们的核心思想是将底层场景几何网格建模为图表图集，我们使用2D高斯曲面（MAtCha-Gaussians）进行渲染。MAtCha从现成的单目深度估计器中提取高频场景表面细节，并通过高斯表面渲染对其进行细化。高斯表面实时附着在图表上，满足神经体积渲染的真实感和网格模型的清晰几何，即单个模型中两个看似矛盾的目标。MAtCha的核心是一种新的神经变形模型和一种结构损失，它保留了从学习的单眼深度中提取的精细表面细节，同时解决了它们的基本尺度模糊问题。广泛的实验验证结果表明，MAtCha的表面重建和真实感质量与顶级竞争者不相上下，但输入视图数量和计算时间大幅减少。我们相信MAtCha将成为视觉、图形和机器人中任何视觉应用的基础工具，这些应用除了照片级真实感外，还需要显式几何。我们的项目页面如下：https://anttwo.github.io/matcha/ et.al.|[2412.06767](http://arxiv.org/abs/2412.06767)|null|
|**2024-12-09**|**Deblur4DGS: 4D Gaussian Splatting from Blurry Monocular Video**|最近的4D重建方法取得了令人印象深刻的结果，但依赖于清晰的视频作为监督。然而，由于相机抖动和物体移动，视频中经常出现运动模糊，而现有的方法在使用此类视频重建4D模型时会渲染模糊的结果。尽管一些基于NeRF的方法试图解决这个问题，但由于在暴露时间内估计连续动态表示的不准确性，它们很难产生高质量的结果。受最近使用3D高斯散点（3DGS）进行3D运动轨迹建模的工作的鼓舞，我们建议将3DGS作为场景表示方式，并提出了第一个4D高斯散点框架，用于从模糊的单眼视频中重建高质量的4D模型，称为Deblur4DGS。具体来说，我们将曝光时间内的连续动态表示估计转换为曝光时间估计。此外，我们引入了曝光正则化来避免琐碎的解决方案，以及多帧和多分辨率一致性解决方案来减轻伪影。此外，为了更好地表示具有大运动的对象，我们建议使用模糊感知的可变规范高斯分布。除了新颖的视图合成之外，Deblur4DGS还可以应用于从多个角度改善模糊视频，包括去模糊、帧插值和视频稳定。对上述四项任务的广泛实验表明，Deblur4DGS优于最先进的4D重建方法。这些代码可在以下网址获得https://github.com/ZcsrenlongZ/Deblur4DGS. et.al.|[2412.06424](http://arxiv.org/abs/2412.06424)|null|
|**2024-12-07**|**Template-free Articulated Gaussian Splatting for Real-time Reposable Dynamic View Synthesis**|虽然动态场景的新颖视图合成取得了重大进展，但捕获对象的骨架模型并对其重新定位仍然是一项具有挑战性的任务。为了解决这个问题，在本文中，我们提出了一种新的方法，可以自动从视频中发现动态对象的相关骨架模型，而不需要特定于对象的模板。我们的方法利用3D高斯散点和超点来重建动态对象。将超点视为刚性部分，我们可以通过直观的线索发现潜在的骨架模型，并使用运动学模型对其进行优化。此外，应用自适应控制策略来避免冗余超点的出现。大量实验证明了我们的方法在获得可重新定位的3D对象方面的有效性和效率。我们的方法不仅可以实现出色的视觉保真度，还可以实时渲染高分辨率图像。 et.al.|[2412.05570](http://arxiv.org/abs/2412.05570)|null|
|**2024-12-06**|**Extrapolated Urban View Synthesis Benchmark**|真实感模拟器对于以视觉为中心的自动驾驶汽车（AV）的训练和评估至关重要。其核心是新颖视图合成（NVS），这是一种关键能力，可以生成各种看不见的视点，以适应飞行器广泛而连续的姿态分布。辐射场的最新进展，如3D高斯散斑，实现了实时速度的真实感渲染，并已广泛应用于大规模驾驶场景的建模。然而，通常使用具有高度相关的训练和测试视图的插值设置来评估它们的性能。相比之下，外推法（测试视图与训练视图存在较大偏差）仍然没有得到充分探索，限制了可推广仿真技术的进步。为了解决这一差距，我们利用公开可用的AV数据集，包括多个行程、多辆车和多个摄像头，构建了第一个外推城市景观合成（EUVS）基准。同时，我们对不同难度级别的最先进的高斯散布方法进行了定量和定性评估。我们的结果表明，高斯散点法容易对训练视图进行过拟合。此外，在大视图变化下，结合扩散先验和改进几何结构并不能从根本上改善NVS，这突显了对更稳健的方法和大规模训练的需求。我们已经发布了我们的数据，以帮助推进自动驾驶和城市机器人模拟技术。 et.al.|[2412.05256](http://arxiv.org/abs/2412.05256)|**[link](https://github.com/ai4ce/EUVS-Benchmark)**|
|**2024-12-06**|**Pushing Rendering Boundaries: Hard Gaussian Splatting**|3D高斯散斑（3DGS）以实时渲染的方式展示了令人印象深刻的新颖视图合成（NVS）结果。在训练过程中，它严重依赖于视图空间位置梯度的平均幅度来增长高斯分布，以减少渲染损失。然而，这种平均操作平滑了来自不同视点的位置梯度和来自不同像素的渲染误差，阻碍了许多有缺陷的高斯分布的生长和优化。这会导致某些区域出现强烈的伪影。为了解决这个问题，我们提出了硬高斯散点，称为HGS，它考虑了多视图的显著位置梯度和渲染误差，以生长硬高斯分布，填补3D场景上经典高斯散点的空白，从而获得优异的NVS结果。详细地说，我们提出了位置梯度驱动的HGS，它利用多视图显著位置梯度来发现硬高斯分布。此外，我们提出了渲染误差引导的HGS，它可以识别明显的像素渲染误差和潜在的超大高斯分布，以联合挖掘硬高斯分布。通过生长和优化这些硬高斯分布，我们的方法有助于解决模糊和针状伪影。在各种数据集上的实验表明，我们的方法在保持实时效率的同时实现了最先进的渲染质量。 et.al.|[2412.04826](http://arxiv.org/abs/2412.04826)|null|
|**2024-12-05**|**Sparse Voxels Rasterization: Real-time High-fidelity Radiance Field Rendering**|我们提出了一种高效的辐射场渲染算法，该算法在没有神经网络或3D高斯的情况下，对稀疏体素进行光栅化处理。拟议的系统有两个关键贡献。第一种方法是通过使用动态Morton排序，沿像素射线以正确的深度顺序渲染稀疏体素。这避免了高斯飞溅中常见的爆裂伪影。其次，我们自适应地将稀疏体素适应场景中不同级别的细节，忠实地再现场景细节，同时实现高渲染帧率。我们的方法将之前的无神经体素网格表示提高了4db以上的PSNR和10倍以上的渲染FPS加速，实现了最先进的可比新颖视图合成结果。此外，我们的无神经稀疏体素与基于网格的3D处理算法无缝兼容。通过将TSDF Fusion和Marching Cubes集成到我们的稀疏网格系统中，我们实现了有前景的网格重建精度。 et.al.|[2412.04459](http://arxiv.org/abs/2412.04459)|null|
|**2024-12-05**|**Monocular Dynamic Gaussian Splatting is Fast and Brittle but Smooth Motion Helps**|高斯飞溅方法正在成为一种流行的方法，用于将多视图图像数据转换为允许视图合成的场景表示。特别是，人们对仅使用单眼输入数据实现动态场景的视图合成感兴趣，这是一个不适定且具有挑战性的问题。这一领域的快速工作节奏产生了多篇同时发表的论文，这些论文声称效果最好，但不可能都是真的。在这项工作中，我们组织、基准测试和分析了许多基于高斯飞溅的方法，提供了先前工作所缺乏的苹果对苹果的比较。我们使用多个现有数据集和一个新的指导性合成数据集，旨在隔离影响重建质量的因素。我们系统地将高斯飞溅方法分为特定的运动表示类型，并量化它们的差异如何影响性能。根据经验，我们发现它们在合成数据中的排名顺序是明确的，但现实世界数据的复杂性目前压倒了这些差异。此外，所有基于高斯的方法的快速渲染速度都是以优化中的脆弱性为代价的。我们将我们的实验总结成一系列发现，这些发现有助于在这个生动的问题环境中取得进一步进展。项目网页：https://lynl7130.github.io/MonoDyGauBench.github.io/ et.al.|[2412.04457](http://arxiv.org/abs/2412.04457)|null|
|**2024-12-05**|**DGNS: Deformable Gaussian Splatting and Dynamic Neural Surface for Monocular Dynamic 3D Reconstruction**|单目视频的动态场景重建对于现实世界的应用至关重要。本文通过引入一种混合框架来解决动态新颖视图合成和3D几何重建的双重挑战：可变形高斯散点和动态神经曲面（DGNS），其中两个模块可以相互利用来完成这两项任务。在训练过程中，可变形高斯飞溅模块生成的深度图引导射线采样以实现更快的处理，并在动态神经表面模块内提供深度监督以改善几何重建。同时，动态神经曲面引导高斯基元在曲面周围的分布，提高渲染质量。为了进一步细化深度监控，我们对高斯光栅化得到的深度图引入了深度滤波过程。在公共数据集上进行的广泛实验表明，DGNS在新颖的视图合成和3D重建方面都达到了最先进的性能。 et.al.|[2412.03910](http://arxiv.org/abs/2412.03910)|null|
|**2024-12-05**|**HybridGS: Decoupling Transients and Statics with 2D and 3D Gaussian Splatting**|在以瞬态对象为特征的场景中生成3D高斯散斑（3DGS）的高质量新颖视图渲染具有挑战性。我们提出了一种新的混合表示方法，称为HybridGS，对每张图像中的瞬态对象使用2D高斯，对整个静态场景保持传统的3D高斯。请注意，3DGS本身更适合对假设多视图一致性的静态场景进行建模，但瞬态对象偶尔出现，不符合假设，因此我们将它们建模为来自单个视图的平面对象，用2D高斯表示。我们的小说表现从基本观点一致性的角度对场景进行了分解，使其更加合理。此外，我们提出了一种新的3DGS多视图监管方法，该方法利用来自共视区域的信息，进一步增强了瞬态和静态之间的区别。然后，我们提出了一种简单而有效的多阶段训练策略，以确保在各种设置下进行稳健的训练和高质量的视图合成。在基准数据集上的实验表明，即使在存在干扰元素的情况下，我们在室内和室外场景中也能实现新颖的视图合成。 et.al.|[2412.03844](http://arxiv.org/abs/2412.03844)|null|
|**2024-12-04**|**Sparse-view Pose Estimation and Reconstruction via Analysis by Generative Synthesis**|推断一组多视图图像背后的3D结构通常需要解决两个相互依赖的任务——精确的3D重建需要精确的相机姿态，预测相机姿态依赖于（隐式或显式）对底层3D进行建模。经典的综合分析框架将这一推断视为一种联合优化，旨在解释观察到的像素，最近的实例通过基于梯度下降的初始姿态估计的姿态细化来学习表达性的3D表示（例如神经场）。然而，给定一组稀疏的观测视图，观测可能无法提供足够的直接证据来获得完整准确的3D。此外，姿势估计中的大误差可能不容易纠正，并可能进一步降低推断的3D。为了在这种具有挑战性的设置中实现稳健的3D重建和姿态估计，我们提出了SparseAGS，这是一种通过以下方式调整这种综合分析方法的方法：a）将基于新视图合成的生成先验与光度目标结合起来，以提高推断的3D的质量，b）明确地推理异常值，并使用基于连续优化策略的离散搜索来纠正它们。我们结合几个现成的姿态估计系统，在真实世界和合成数据集中验证我们的框架作为初始化。我们发现，它显著提高了基础系统的姿态精度，同时产生了高质量的3D重建，其效果优于当前多视图重建基线的结果。 et.al.|[2412.03570](http://arxiv.org/abs/2412.03570)|null|

<p align=right>(<a href=#updated-on-20241210>back to top</a>)</p>

## 3D Reconstruction

|Publish Date|Title|Abstract|PDF|Code|
|---|---|---|---|---|
|**2024-12-09**|**Generative Densification: Learning to Densify Gaussians for High-Fidelity Generalizable 3D Reconstruction**|广义前馈高斯模型通过利用大型多视图数据集的先验知识，在稀疏视图3D重建方面取得了重大进展。然而，由于高斯模型的数量有限，这些模型往往难以表示高频细节。虽然在每场景3D高斯溅射（3D-GS）优化中使用的致密化策略可以适应前馈模型，但它可能不适合一般场景。在本文中，我们提出了生成致密化，这是一种有效且可推广的方法来致密前馈模型生成的高斯分布。与迭代分割和克隆原始高斯参数的3D-GS致密化策略不同，我们的方法从前馈模型中对特征表示进行上采样，并在一次前向传递中生成相应的精细高斯分布，利用嵌入的先验知识来增强泛化。对象级和场景级重建任务的实验结果表明，我们的方法在相当或更小的模型尺寸下优于最先进的方法，在表示精细细节方面取得了显著的改进。 et.al.|[2412.06234](http://arxiv.org/abs/2412.06234)|null|
|**2024-12-08**|**Doppelgangers++: Improved Visual Disambiguation with Geometric 3D Features**|精确的3D重建经常受到视觉混叠的阻碍，在视觉混叠中，视觉上相似但不同的表面（又名二重身）被错误地匹配。这些伪匹配扭曲了运动结构（SfM）过程，导致模型元素错位和精度降低。之前的努力通过在精心策划的数据集上训练的CNN分类器解决了这个问题，但这些方法很难在不同的现实世界场景中推广，并且可能需要大量的参数调整。在这项工作中，我们提出了Doppelgangers++，这是一种增强doppelganger检测并提高3D重建精度的方法。我们的贡献包括一个多样化的训练数据集，该数据集整合了来自日常场景的地理标记图像，将鲁棒性扩展到基于地标的数据集之外。我们进一步提出了一种基于Transformer的分类器，该分类器利用了MASt3R模型中的3D感知特征，在域内和域外测试中实现了卓越的精确度和召回率。Doppelgangers++无缝集成到标准SfM和MASt3R SfM管道中，在各种场景中提供效率和适应性。为了评估SfM的准确性，我们引入了一种基于地理标签的自动化方法来验证重建模型，从而消除了手动检查的需要。通过大量实验，我们证明Doppelgangers++显著增强了成对视觉消歧，并在复杂和多样化的场景中提高了3D重建质量。 et.al.|[2412.05826](http://arxiv.org/abs/2412.05826)|null|
|**2024-12-06**|**Perturb-and-Revise: Flexible 3D Editing with Generative Trajectories**|随着基于文本的扩散模型的发展，3D重建和基于文本的3D编辑领域取得了显著进步。虽然现有的3D编辑方法擅长修改颜色、纹理和风格，但它们难以应对广泛的几何或外观变化，从而限制了它们的应用。我们提出了扰动和修改，这使得各种NeRF编辑成为可能。首先，我们通过随机初始化来扰动NeRF参数，以创建一个通用的初始化。我们通过分析局部损失景观自动确定扰动幅度。然后，我们通过生成轨迹修改编辑后的NeRF。结合生成过程，我们施加身份保持梯度来细化编辑的NeRF。大量实验表明，Perturb和Revise有助于在3D中灵活、有效和一致地编辑颜色、外观和几何图形。有关360度结果，请访问我们的项目页面：https://susunghong.github.io/Perturb-and-Revise. et.al.|[2412.05279](http://arxiv.org/abs/2412.05279)|null|
|**2024-12-05**|**MetaFormer: High-fidelity Metalens Imaging via Aberration Correcting Transformers**|Metalens是一种新兴的光学系统，具有不可替代的优点，因为它可以以超薄和紧凑的尺寸制造，这显示了医学成像和增强/虚拟现实（AR/VR）等各种应用的巨大前景。尽管其在小型化方面具有优势，但其实用性受到严重像差和失真的限制，这会显著降低图像质量。之前的几项技术试图解决不同类型的像差，但其中大多数主要是为传统的笨重镜头设计的，不足以弥补金属透镜的严重像差。虽然有专门针对金属透镜的像差校正方法，但它们仍然达不到恢复质量。在这项工作中，我们提出了MetaFormer，这是一种用于金属透镜捕获图像的像差校正框架，利用视觉变换器（ViT），在各种图像恢复任务中显示出卓越的恢复性能。具体来说，我们设计了一种多自适应滤波器引导（MAFG），其中多个维纳滤波器通过各种噪声细节平衡来丰富退化的输入图像，从而提高了输出恢复质量。此外，我们引入了一个空间和转置自我注意融合（STAF）模块，该模块聚合了空间自我注意和转置自我注意力模块的特征，以进一步改善像差校正。我们进行了广泛的实验，包括校正畸变图像和视频，以及从退化图像中进行干净的3D重建。所提出的方法明显优于先前的技术。我们进一步制造了一个金属透镜，并通过恢复在野外用制造的金属透镜捕获的图像来验证MetaFormer的实用性。代码和预训练模型可在以下网址获得https://benhenryl.github.io/MetaFormer et.al.|[2412.04591](http://arxiv.org/abs/2412.04591)|null|
|**2024-12-05**|**DualPM: Dual Posed-Canonical Point Maps for 3D Shape and Pose Reconstruction**|数据表示的选择是几何任务中深度学习成功的关键因素。例如，DUSt3R最近引入了视点不变点图的概念，推广了深度预测，并表明可以将静态场景3D重建中的所有关键问题简化为预测这些点图。在本文中，我们为一个非常不同的问题开发了一个类似的概念，即可变形物体的3D形状和姿态的重建。为此，我们引入了双点图（DualPM），其中从{same}图像中提取一对点图，一个将像素与其在物体上的3D位置相关联，另一个将其与静止物体姿势的规范版本相关联。我们还将点图扩展到无模重建，通过自遮挡来获得物体的完整形状。我们表明，3D重建和3D姿态估计简化为双PM的预测。我们实证证明，这种表示是深度网络预测的一个很好的目标；具体来说，我们考虑对马进行建模，表明DualPM可以纯粹在由马的单个模型组成的3D合成数据上进行训练，同时很好地推广到真实图像。有了这个，我们大大改进了以前用于这类对象的3D分析和重建的方法。 et.al.|[2412.04464](http://arxiv.org/abs/2412.04464)|null|
|**2024-12-05**|**Likelihood-Scheduled Score-Based Generative Modeling for Fully 3D PET Image Reconstruction**|使用预训练的基于分数的生成模型（SGMs）进行医学图像重建比其他现有的最先进的深度学习重建方法具有优势，包括提高了对不同扫描仪设置的弹性和先进的图像分布建模。基于SGM的重建最近被应用于模拟正电子发射断层扫描（PET）数据集，与最先进的技术相比，显示出分布外病变的对比度恢复得到了改善。然而，现有的基于SGM从PET数据重建的方法存在重建缓慢、超参数调整繁重和切片不一致效应（在3D中）的问题。在这项工作中，我们提出了一种实用的全3D重建方法，通过将SGM逆扩散过程的可能性与最大似然期望最大化算法的当前迭代相匹配，加速重建并减少关键超参数的数量。使用模拟 $[^{18}$F]DPA-714数据集的低计数重建示例，我们表明我们的方法可以匹配或改进现有最先进的基于SGM的PET重建的NRMSE和SSIM，同时减少重建时间和对超参数调整的需求。我们根据最先进的监督和传统重建算法评估我们的方法。最后，我们首次展示了基于SGM的真实3D PET数据重建的实现，特别是$[^{18}$ F]DPA-714数据，我们在其中集成了垂直预训练的SGM，以消除切片不一致问题。 et.al.|[2412.04339](http://arxiv.org/abs/2412.04339)|null|
|**2024-12-05**|**CrossSDF: 3D Reconstruction of Thin Structures From Cross-Sections**|从平面横截面重建复杂结构是一个具有挑战性的问题，在医学成像、制造和地形学中具有广泛的应用。由于切片平面之间的数据稀疏性，开箱即用的点云重建方法往往会失败，而当前的定制方法难以重建薄几何结构并保持拓扑连续性。这对于CT和MRI扫描中存在薄血管结构的医学应用非常重要。本文介绍了一种从平面轮廓生成的二维有符号距离中提取三维有符号距离场的新方法。我们的方法通过使用为2D切片内已知几何形状的情况设计的损失，使神经SDF的训练具有轮廓感知能力。我们的结果表明，与现有方法相比，我们有了显著的改进，有效地重建了薄结构，并生成了准确的3D模型，而没有插值伪影或先前方法的过度平滑。 et.al.|[2412.04120](http://arxiv.org/abs/2412.04120)|null|
|**2024-12-05**|**MT3DNet: Multi-Task learning Network for 3D Surgical Scene Reconstruction**|在图像辅助微创手术（MIS）中，理解手术场景对于向外科医生提供实时反馈、技能评估以及通过人机协作程序改善结果至关重要。在此背景下，挑战在于准确检测、分割和估计高分辨率图像中描绘的手术场景的深度，同时以3D重建场景，并提供手术器械的分割以及每个器械的检测标签。为了应对这一挑战，提出了一种新的多任务学习（MTL）网络，用于同时执行这些任务。该方法的一个关键方面涉及通过将对抗性权重更新集成到MTL框架中来克服与同时处理多个任务相关的优化障碍，所提出的MTL模型通过集成分割、深度估计和对象检测来实现3D重建，从而增强了对手术场景的理解，这与缺乏3D功能的现有研究相比是一个重大进步。EndoVis2018基准数据集的综合实验强调了该模型在有效解决所有三项任务方面的熟练程度，证明了所提出技术的有效性。 et.al.|[2412.03928](http://arxiv.org/abs/2412.03928)|null|
|**2024-12-05**|**DGNS: Deformable Gaussian Splatting and Dynamic Neural Surface for Monocular Dynamic 3D Reconstruction**|单目视频的动态场景重建对于现实世界的应用至关重要。本文通过引入一种混合框架来解决动态新颖视图合成和3D几何重建的双重挑战：可变形高斯散点和动态神经曲面（DGNS），其中两个模块可以相互利用来完成这两项任务。在训练过程中，可变形高斯飞溅模块生成的深度图引导射线采样以实现更快的处理，并在动态神经表面模块内提供深度监督以改善几何重建。同时，动态神经曲面引导高斯基元在曲面周围的分布，提高渲染质量。为了进一步细化深度监控，我们对高斯光栅化得到的深度图引入了深度滤波过程。在公共数据集上进行的广泛实验表明，DGNS在新颖的视图合成和3D重建方面都达到了最先进的性能。 et.al.|[2412.03910](http://arxiv.org/abs/2412.03910)|null|
|**2024-12-05**|**4D SlingBAG: spatial-temporal coupled Gaussian ball for large-scale dynamic 3D photoacoustic iterative reconstruction**|大规模动态三维（3D）光声成像（PAI）在临床应用中具有重要意义。在实际实现中，大规模3D实时PAI系统通常利用具有某些角度缺陷的稀疏二维（2D）传感器阵列，需要先进的迭代重建（IR）算法来实现定量PAI并减少重建伪影。然而，对于现有的IR算法，多帧3D重建会导致极高的内存消耗和较长的计算时间，对数据帧之间的时空连续性考虑有限。在这里，我们提出了一种新的方法，称为4D滑动高斯球自适应增长（4D SlingBAG）算法，该算法基于当前基于点云的IR算法滑动高斯球适应性增长（SlingBAG），在IR方法中具有最小的内存消耗。我们的4D SlingBAG方法将时空耦合变形函数应用于点云中的每个高斯球体，从而明确地学习动态3D PA场景的变形特征。这允许有效地表示各种生理过程（如脉动）或外部压力（如血液灌注实验），这些过程有助于动态3D PAI期间血管形态和血流的变化，从而为动态3D PAIs提供高效的IR。仿真实验表明，4D SlingBAG实现了高质量的动态3D PA重建。与对每一帧单独使用SlingBAG算法进行重建相比，我们的方法显著减少了计算时间，并保持了极低的内存消耗。4D SlingBAG项目可以在以下GitHub存储库中找到：\href{https://github.com/JaegerCQ/4D-SlingBAG}{https://github.com/JaegerCQ/4D-SlingBAG}. et.al.|[2412.03898](http://arxiv.org/abs/2412.03898)|**[link](https://github.com/jaegercq/4d-slingbag)**|

<p align=right>(<a href=#updated-on-20241210>back to top</a>)</p>

## Diffusion

|Publish Date|Title|Abstract|PDF|Code|
|---|---|---|---|---|
|**2024-12-09**|**[MASK] is All You Need**|在生成模型中，两种范式在各种应用中越来越受欢迎：基于下一集预测的掩蔽生成模型和基于下一噪声预测的非自回归模型，例如扩散模型。在这项工作中，我们建议使用离散状态模型来连接它们，并探索它们在视觉领域的可扩展性。首先，我们以可扩展的方式在统一的设计空间中对两种类型的模型（包括时间步长独立性、噪声调度、温度、制导强度等）进行逐步分析。其次，我们将典型的判别任务（如图像分割）重新转换为离散状态模型上[MASK]标记的去掩蔽过程。这使我们能够执行各种采样过程，包括通过只训练一次来模拟联合分布的灵活条件采样。所有上述探索都导致了我们名为“离散插值”的框架，与之前在各种基准测试中基于离散状态的方法（如ImageNet256、MS COCO和视频数据集FaceForensics）相比，该框架使我们能够实现最先进或有竞争力的性能。总之，通过在离散状态模型中利用[MASK]，我们可以桥接掩蔽生成和非自回归扩散模型，以及生成和判别任务。 et.al.|[2412.06787](http://arxiv.org/abs/2412.06787)|**[link](https://github.com/CompVis/mask)**|
|**2024-12-09**|**Retrieving Semantics from the Deep: an RAG Solution for Gesture Synthesis**|非言语交流通常包括语义丰富的手势，有助于传达话语的含义。对于能够生成有节奏的节拍手势但难以生成语义上有意义的手势的现有神经系统来说，产生这种语义上的同音手势一直是一个主要挑战。因此，我们提出了RAG手势，这是一种基于扩散的手势生成方法，它利用检索增强生成（RAG）来生成外观自然、语义丰富的手势。我们的神经显式手势生成方法旨在生成基于可解释语言知识的语义手势。我们通过使用显式领域知识从同音手势数据库中检索示例动作来实现这一点。一旦检索到，我们就可以在推理时使用DDIM反转和检索指导将这些语义示例手势注入到基于扩散的手势生成管道中，而不需要任何训练。此外，我们提出了一种指导控制范式，允许用户调节每个检索插入对生成序列的影响程度。我们的比较评估证明了我们的方法与最近的手势生成方法的有效性。我们敦促读者在我们的项目页面上探索结果。 et.al.|[2412.06786](http://arxiv.org/abs/2412.06786)|null|
|**2024-12-09**|**Tactile DreamFusion: Exploiting Tactile Sensing for 3D Generation**|3D生成方法已经显示出由扩散图像先验提供的视觉上引人注目的结果。然而，它们往往无法产生逼真的几何细节，导致表面过于光滑或反照率图中的几何细节烘烤不准确。为了解决这个问题，我们引入了一种新方法，该方法将触摸作为一种额外的方式，以改善生成的3D资产的几何细节。我们设计了一个轻量级的3D纹理场，在视觉和触觉领域的2D扩散模型先验的指导下，合成视觉和触觉纹理。我们将视觉纹理生成条件设定在高分辨率触觉法线上，并使用定制的TextureDreambooth指导基于补丁的触觉纹理细化。我们进一步提出了一个多部分生成管道，使我们能够在不同区域合成不同的纹理。据我们所知，我们是第一个利用高分辨率触觉感知来增强3D生成任务的几何细节的公司。我们在文本到3D和图像到3D设置中评估我们的方法。我们的实验表明，我们的方法提供了定制和逼真的精细几何纹理，同时保持了视觉和触觉两种模式之间的精确对齐。 et.al.|[2412.06785](http://arxiv.org/abs/2412.06785)|**[link](https://github.com/ruihangao/tactiledreamfusion)**|
|**2024-12-09**|**CARP: Visuomotor Policy Learning via Coarse-to-Fine Autoregressive Prediction**|在机器人视觉运动策略学习中，与传统的自回归模型相比，基于扩散的模型在提高动作轨迹生成的准确性方面取得了显著成功。然而，由于多个去噪步骤和复杂约束的有限灵活性，它们效率低下。在本文中，我们介绍了粗到细自回归策略（CARP），这是一种新的视觉运动策略学习范式，将自回归动作生成过程重新定义为粗到细的下一尺度方法。CARP将动作生成分解为两个阶段：首先，动作自动编码器学习整个动作序列的多尺度表示；然后，GPT风格的变换器通过从粗到细的自回归过程来细化序列预测。这种简单直观的方法可以产生高度准确和流畅的操作，与基于扩散的政策的性能相匹配甚至超越，同时保持与自回归政策相当的效率。我们在不同的环境中进行了广泛的评估，包括基于状态和基于图像的模拟基准的单任务和多任务场景，以及现实世界的任务。CARP实现了具有竞争力的成功率，提高了10%，与最先进的策略相比，其推理速度提高了10倍，为机器人任务中的动作生成建立了高性能、高效和灵活的范式。 et.al.|[2412.06782](http://arxiv.org/abs/2412.06782)|null|
|**2024-12-09**|**Around the World in 80 Timesteps: A Generative Approach to Global Visual Geolocation**|全球视觉地理定位可以预测图像在地球上的拍摄位置。由于图像的定位精度各不相同，因此这项任务本身就存在很大程度的模糊性。然而，现有的方法是确定性的，忽略了这一方面。本文旨在缩小传统地理定位与现代生成方法之间的差距。我们提出了第一种基于扩散和黎曼流匹配的生成式地理定位方法，其中去噪过程直接在地球表面进行。我们的模型在三个视觉地理定位基准上达到了最先进的性能：OpenStreetView-5M、YFCC-100M和iNat21。此外，我们引入了概率视觉地理定位的任务，其中模型预测所有可能位置的概率分布，而不是单个点。我们为这项任务引入了新的指标和基线，展示了我们基于扩散的方法的优势。将提供代码和模型。 et.al.|[2412.06781](http://arxiv.org/abs/2412.06781)|null|
|**2024-12-09**|**Diverse Score Distillation**|2D扩散模型的分数蒸馏已被证明是指导3D优化的强大机制，例如支持基于文本的3D生成或单视图重建。然而，现有分数蒸馏公式的一个常见局限性是，尽管底层扩散模型能够生成不同的样本，但（模式寻求）优化的输出在多样性方面受到限制。在这项工作中，受去噪扩散中的采样过程的启发，我们提出了一种分数公式，该公式引导优化遵循随机初始种子定义的生成路径，从而确保多样性。然后，我们提出了一种近似方法，用于优化可能不会精确遵循生成路径的场景（例如，渲染以相互依赖的方式演变的3D表示）。我们展示了我们的“多样性分数蒸馏”（DSD）公式在2D优化、基于文本的3D推理和单视图重建等任务中的应用。我们还根据先前的分数蒸馏公式对DSD进行了实证验证，并表明它在保持保真度的同时显著提高了样本多样性。 et.al.|[2412.06780](http://arxiv.org/abs/2412.06780)|null|
|**2024-12-09**|**Visual Lexicon: Rich Image Features in Language Space**|我们介绍了Visual Lexicon，这是一种新颖的视觉语言，它将丰富的图像信息编码到词汇标记的文本空间中，同时保留了在自然语言中难以传达的复杂视觉细节。与优先考虑高级语义（如CLIP）或像素级重建（如VAE）的传统方法不同，ViLex同时捕获丰富的语义内容和精细的视觉细节，实现了高质量的图像生成和全面的视觉场景理解。通过自监督学习管道，ViLex生成了针对使用冻结文本到图像（T2I）扩散模型重建输入图像而优化的令牌，保留了高保真语义级重建所需的详细信息。作为语言空间中的图像嵌入，ViLex令牌利用了自然语言的组合性，允许它们独立用作“文本令牌”或与自然语言令牌组合，以提示具有视觉和文本输入的预训练T2I模型，反映了我们与视觉语言模型（VLM）的交互方式。实验证明，与文本嵌入相比，ViLex在图像重建中实现了更高的保真度，即使使用单个ViLex标记也是如此。此外，ViLex以零样本、无监督的方式成功执行了各种DreamBooth任务，而无需微调T2I模型。此外，ViLex作为一个强大的视觉编码器，相对于强大的SigLIP基线，在15个基准测试中不断提高视觉语言模型的性能。 et.al.|[2412.06774](http://arxiv.org/abs/2412.06774)|null|
|**2024-12-09**|**Interface dynamics in a degenerate Cahn-Hilliard model for viscoelastic phase separation**|研究表明，与体应力变量交叉扩散耦合的粘弹性相分离简并Cahn-Hilliard模型中的形式化锐界面渐近性导致了经典表面扩散流的非局部低阶对应。扩散界面模型是周-张-E模型的变体，具有Onsager梯度流结构，其秩不足迁移率矩阵反映了应力松弛的ODE特征。在恒定耦合的情况下，我们发现序参数的零水平集的演化近似于所谓的中间表面扩散流。对于单调连接两相的非恒定耦合函数，我们的渐近分析得出了一个三阶家族，其传播算子的行为类似于前导阶负拉普拉斯-贝尔特拉米算子的平方根。在这种情况下，运动尖锐界面的法向速度作为约束椭圆方程中的拉格朗日乘子出现，这是我们推导的核心。约束椭圆问题可以通过变分论元严格求解，并被证明对有效几何演化定律的梯度结构进行了编码。给出了基于双障碍势的中间自由边界问题深淬灭的渐近性。 et.al.|[2412.06762](http://arxiv.org/abs/2412.06762)|null|
|**2024-12-09**|**Speckle imaging with blind source separation and total variation deconvolution**|这项工作涉及强漫射环境中的光学成像。我们考虑光学相干断层扫描中的一个典型设置，其中样品由激光产生并通过显微镜传播的波场集合探测。我们在一个场景中操作，其中照明处于散斑状态，即完全随机。当光在高度异质的介质中深入传播时，就会发生这种情况。最先进的相干技术基于波场的弹道部分，即自由传播并以指数速度衰减的波的分数。在散斑区域，与散射场相比，弹道场可以忽略不计，这排除了相干方法的使用，需要不同的方法。我们提出了一种基于盲源分离和全变分反卷积的策略，以获得具有衍射极限分辨率的图像。源分离使我们能够隔离由不同散射体扩散的场进行成像，而去卷积利用散斑记忆效应来估计这些散射体之间的距离。我们的方法经过数值模拟验证，不仅对离散散射体成像有效，而且对连续物体成像也有效。 et.al.|[2412.06755](http://arxiv.org/abs/2412.06755)|null|
|**2024-12-09**|**InstantRestore: Single-Step Personalized Face Restoration with Shared-Image Attention**|人脸图像恢复旨在增强退化的人脸图像，同时解决各种退化类型、实时处理需求等挑战，最重要的是保护身份特定特征。现有的方法往往难以处理缓慢的处理时间和次优的恢复，特别是在严重退化的情况下，无法准确重建更精细的级别身份细节。为了解决这些问题，我们引入了InstantRestore，这是一个利用单步图像扩散模型和注意力共享机制进行快速和个性化面部恢复的新框架。此外，InstantRestore结合了一种新颖的地标注意力丧失，对齐关键的面部地标以优化注意力图，增强身份保护。在推理时，给定降级的输入和一小部分（~4）参考图像，InstantRestore通过网络执行一次前向传递，以实现近乎实时的性能。与之前依赖于完全扩散过程或每个身份模型调优的方法不同，InstantRestore提供了一种适用于大规模应用程序的可扩展解决方案。大量实验表明，InstantRestore在质量和速度上优于现有方法，使其成为身份保持人脸恢复的有吸引力的选择。 et.al.|[2412.06753](http://arxiv.org/abs/2412.06753)|null|

<p align=right>(<a href=#updated-on-20241210>back to top</a>)</p>

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

<p align=right>(<a href=#updated-on-20241210>back to top</a>)</p>

[contributors-shield]: https://img.shields.io/github/contributors/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[contributors-url]: https://github.com/Vincentqyw/cv-arxiv-daily/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[forks-url]: https://github.com/Vincentqyw/cv-arxiv-daily/network/members
[stars-shield]: https://img.shields.io/github/stars/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[stars-url]: https://github.com/Vincentqyw/cv-arxiv-daily/stargazers
[issues-shield]: https://img.shields.io/github/issues/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[issues-url]: https://github.com/Vincentqyw/cv-arxiv-daily/issues

