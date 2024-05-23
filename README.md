[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]

## Updated on 2024.05.23
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
|**2024-05-20**|**AtomGS: Atomizing Gaussian Splatting for High-Fidelity Radiance Field**|3D高斯散射（3DGS）最近通过提供新颖的视图合成和实时渲染速度的卓越能力，推进了辐射场重建。然而，其混合优化和自适应密度控制策略可能导致次优结果；它有时会产生有噪声的几何体和模糊的伪影，这是因为以充分加密较小的高斯为代价优先优化较大的高斯。为了解决这个问题，我们引入了AtomGS，它由原子化增殖和几何引导优化组成。原子化扩散将不同大小的椭球高斯约束为更均匀大小的原子高斯。该策略通过更加强调根据场景细节的致密化来增强具有精细特征的区域的表示。此外，我们提出了一种几何引导优化方法，该方法结合了边缘感知法线损耗。这种优化方法可以有效地平滑平面，同时保留复杂的细节。我们的评估表明，AtomGS在渲染质量方面优于现有的最先进的方法。此外，与其他基于SDF的方法相比，它在几何重建方面实现了有竞争力的精度，并在训练速度上有了显著提高。更多交互式演示可以在我们的网站上找到（\href{https://rongliu-leo.github.io/AtomGS/}{https://rongliu-leo.github.io/AtomGS/}). et.al.|[2405.12369](http://arxiv.org/abs/2405.12369)|null|
|**2024-05-20**|**Fast Generalizable Gaussian Splatting Reconstruction from Multi-View Stereo**|我们提出了MVSGaussian，这是一种从多视图立体（MVS）中导出的新的可推广的3D高斯表示方法，可以有效地重建看不见的场景。具体地说，1）我们利用MVS对几何感知的高斯表示进行编码，并将其解码为高斯参数。2） 为了进一步提高性能，我们提出了一种混合高斯渲染，它集成了一种高效的体绘制设计，用于新颖的视图合成。3） 为了支持特定场景的快速微调，我们引入了一种多视图几何一致聚合策略，以有效地聚合可推广模型生成的点云，作为每个场景优化的初始化。与以前基于NeRF的可推广方法相比，MVSGaussian通常需要对每个图像进行几分钟的微调和几秒钟的渲染，它实现了实时渲染，每个场景的合成质量更好。与普通的3D-GS相比，MVSGaussian以较少的训练计算成本实现了更好的视图合成。在DTU、Real Forward Faceing、NeRF Synthetic以及Tanks and Temples数据集上进行的大量实验验证了MVSGaussian具有令人信服的可推广性、实时渲染速度和快速的逐场景优化，达到了最先进的性能。 et.al.|[2405.12218](http://arxiv.org/abs/2405.12218)|null|
|**2024-05-20**|**CoR-GS: Sparse-View 3D Gaussian Splatting via Co-Regularization**|3D高斯散射（3DGS）创建由3D高斯组成的辐射场来表示场景。由于训练视图稀疏，3DGS很容易出现过拟合，对重建质量产生负面影响。本文介绍了一种改进稀疏视图3DGS的新的协正则化方法。当训练具有相同稀疏场景视图的两个3D高斯辐射场时，我们观察到这两个辐射场表现出\textit｛点不一致｝和\textit｝渲染不一致｝，这两个不一致可以不可监督地预测重建质量，这源于致密化中的采样实现。我们通过评估高斯点表示之间的配准并计算其渲染像素的差异，进一步量化了点不一致和渲染不一致。实证研究表明，这两种分歧与准确重建之间存在负相关，这使我们能够在不获取地面实况信息的情况下识别不准确的重建。基于这项研究，我们提出了CoR-GS，它基于两个分歧来识别和抑制不准确的重建：（\romannumeral1）共同修剪考虑在不准确的位置上表现出高点分歧的高斯算子，并对其进行修剪。（\romannumeral2）伪视图协同正则化认为表现出高度渲染不一致的像素被不准确地渲染并抑制不一致。LLFF、Mip-NeRF360、DTU和Blender的结果表明，CoR-GS有效地正则化了场景几何，重建了紧凑表示，并在稀疏训练视图下实现了最先进的新视图合成质量。 et.al.|[2405.12110](http://arxiv.org/abs/2405.12110)|null|
|**2024-05-20**|**MirrorGaussian: Reflecting 3D Gaussians for Reconstructing Mirror Reflections**|3D Gaussian Splatting展示了照片逼真度和实时新颖视图合成方面的显著进步。然而，它在建模镜面反射方面面临挑战，因为从不同的角度来看，镜面反射表现出显著的外观变化。为了解决这个问题，我们提出了MirrorGaussian，这是第一种基于3D高斯散射的实时渲染镜像场景重建方法。关键见解基于真实世界空间和虚拟镜像空间之间的镜像对称性。我们引入了一种直观的双渲染策略，该策略能够对真实世界的3D高斯和通过在镜像平面上反射前者而获得的镜像对应物进行可微分光栅化。所有3D高斯都是在端到端的框架中与镜像平面联合优化的。MirrorGaussian在有镜像的场景中实现了高质量和实时的渲染，支持场景编辑，如添加新的镜像和对象。在多个数据集上进行的综合实验表明，我们的方法显著优于现有方法，取得了最先进的结果。项目页面：https://mirror-gaussian.github.io/. et.al.|[2405.11921](http://arxiv.org/abs/2405.11921)|null|
|**2024-05-17**|**Photorealistic 3D Urban Scene Reconstruction and Point Cloud Extraction using Google Earth Imagery and Gaussian Splatting**|三维城市场景重建和建模是遥感的一个重要研究领域，在学术界、商业界、工业界和行政管理界有着广泛的应用。视图合成模型的最新进展促进了仅从2D图像进行真实感3D重建。利用Google Earth图像，我们构建了以滑铁卢大学为中心的滑铁卢地区的3D高斯散射模型，并能够根据我们在基准测试中演示的神经辐射场获得远远超过以往3D视图合成结果的视图合成结果。此外，我们使用从3D高斯散射模式中提取的3D点云检索场景的3D几何结构，我们将其与场景的多视图立体密集重建进行了对比，从而通过3D高斯散射重建大规模城市场景的3D几何形状和照片真实感照明 et.al.|[2405.11021](http://arxiv.org/abs/2405.11021)|null|
|**2024-05-17**|**3D Vessel Reconstruction from Sparse-View Dynamic DSA Images via Vessel Probability Guided Attenuation Learning**|数字减影血管造影（DSA）是血管疾病诊断的金标准之一。在造影剂的帮助下，时间分辨的2D DSA图像提供了对血流信息的全面见解，并可用于重建3D血管结构。当前的商业DSA系统通常需要数百个扫描视图来执行重建，从而导致大量的辐射暴露。然而，旨在减少辐射剂量的稀疏视图DSA重建在研究界仍然没有得到充分的探索。动态血流和稀疏视图DSA图像输入不足对3D血管重建任务提出了重大挑战。在这项研究中，我们建议使用时间不可知的船舶概率场来有效地解决这个问题。我们的方法称为血管概率引导的衰减学习，将DSA成像表示为静态和动态衰减场的互补加权组合，其权重来自血管概率场。作为动态掩模，血管概率为适应不同场景类型的静态和动态场提供了适当的梯度。该机制促进了静态背景和动态造影剂流之间的自监督分解，并显著提高了重建质量。我们的模型是通过最小化合成投影和真实捕获的DSA图像之间的视差来训练的。我们进一步采用了两种训练策略来提高重建质量：（1）从粗到细的渐进训练以实现更好的几何结构；（2）时间扰动渲染损失以增强时间一致性。实验结果表明，在三维血管重建和二维视图合成方面都具有优异的质量。 et.al.|[2405.10705](http://arxiv.org/abs/2405.10705)|**[link](https://github.com/Zhentao-Liu/VPAL)**|
|**2024-05-17**|**Toon3D: Seeing Cartoons from a New Perspective**|在这项工作中，我们恢复了非几何一致场景的底层3D结构。我们将分析重点放在卡通和动漫中的手绘图像上。许多漫画是由艺术家在没有3D渲染引擎的情况下创作的，这意味着场景的任何新图像都是手绘的。手绘图像通常是世界的忠实表示，但仅在定性意义上，因为人类很难始终如一地绘制物体或场景的多个视角。然而，人们可以很容易地从不一致的输入中感知3D场景！在这项工作中，我们纠正了2D图形的不一致性，以恢复看似合理的3D结构，从而使新扭曲的图形彼此一致。我们的管道由用户友好的注释工具、相机姿态估计和图像变形组成，以恢复密集结构。我们的方法扭曲图像以服从透视相机模型，使我们对齐的结果能够插入到新颖的视图合成重建方法中，以体验从未绘制过的视点的卡通效果。我们的项目页面是https://toon3d.studio . et.al.|[2405.10320](http://arxiv.org/abs/2405.10320)|null|
|**2024-05-10**|**I3DGS: Improve 3D Gaussian Splatting from Multiple Dimensions**|3D Gaussian Splatting是一种新的三维视图合成方法，与传统的神经渲染技术相比，它可以获得隐含的神经学习渲染结果，但保持更高清晰度的快速渲染速度。但是，对于实际应用来说，在三维高斯散射上仍然很难达到足够快的效率。为了解决这个问题，我们提出了I3DS，一种综合模型性能改进的评估解决方案和实验测试。从原始三维高斯飞溅的多个重要层面或维度，我们进行了2000多种不同的实验，以测试所选择的不同项目和组件如何影响三维高斯飞溅模型的训练效率。在本文中，我们将分享关于如何提高训练、绩效以及模型的不同项目所造成的影响的丰富而有意义的经验和方法。提出了一种特殊但正常的95进制整数压缩和94进制浮点压缩ASCII编解码机制。将记录许多真实有效的实验和测试结果或现象。经过一系列合理的微调，I3DS可以获得比之前更好的性能提升。项目代码以开源形式提供。 et.al.|[2405.06408](http://arxiv.org/abs/2405.06408)|null|
|**2024-05-10**|**MGS-SLAM: Monocular Sparse Tracking and Gaussian Mapping with Depth Smooth Regularization**|本文介绍了一种基于高斯散射的密集视觉同步定位与映射（VSLAM）的新框架。近年来，基于高斯飞溅的SLAM取得了很好的结果，但它依赖于RGB-D输入，跟踪能力较弱。为了解决这些局限性，我们首次将高级稀疏视觉里程计与密集高斯散射场景表示独特地集成在一起，从而消除了对基于高斯散射的SLAM系统典型的深度图的依赖，并增强了跟踪鲁棒性。在这里，稀疏视觉里程计在RGB流中跟踪相机姿势，而高斯散射处理地图重建。这些组件通过多视图立体（MVS）深度估计网络互连。我们提出了一种深度平滑损失来减少估计深度图的负面影响。此外，稀疏视觉里程计和密集高斯图之间的尺度一致性通过稀疏密集调整环（SDAR）得以保持。我们已经在各种合成和真实世界的数据集上评估了我们的系统。我们的姿态估计精度超过了现有方法，并达到了最先进的性能。此外，在新的视图合成保真度方面，它优于以前的单目方法，与利用RGB-D输入的神经SLAM系统的结果相匹配。 et.al.|[2405.06241](http://arxiv.org/abs/2405.06241)|null|
|**2024-05-09**|**FastScene: Text-Driven Fast 3D Indoor Scene Generation via Panoramic Gaussian Splatting**|文本驱动的3D室内场景生成具有广泛的应用，从游戏和智能家居到AR/VR应用。快速高保真的场景生成对于确保用户友好的体验至关重要。然而，现有方法的特点是生成过程漫长，或者需要复杂的手动指定运动参数，这给用户带来了不便。此外，这些方法通常依赖于窄场视点迭代生成，从而影响全局一致性和整体场景质量。为了解决这些问题，我们提出了FastScene，这是一个用于快速、更高质量的3D场景生成的框架，同时保持场景一致性。具体来说，在给定文本提示的情况下，我们生成全景图并估计其深度，因为全景图包含了关于整个场景的信息，并表现出明确的几何约束。为了获得高质量的新颖视图，我们引入了粗略视图合成（CVS）和渐进新颖视图修复（PNVI）策略，以确保场景一致性和视图质量。随后，我们利用多视图投影（MVP）形成透视图，并应用3D高斯散射（3DGS）进行场景重建。综合实验表明，FastScene在生成速度和质量上都优于其他方法，具有更好的场景一致性。值得注意的是，FastScene仅在文本提示的引导下，就可以在15分钟内生成3D场景，这比最先进的方法快至少一个小时，使其成为用户友好的场景生成典范。 et.al.|[2405.05768](http://arxiv.org/abs/2405.05768)|null|

<p align=right>(<a href=#updated-on-20240523>back to top</a>)</p>

## 3D Reconstruction

|Publish Date|Title|Abstract|PDF|Code|
|---|---|---|---|---|
|**2024-05-21**|**S3O: A Dual-Phase Approach for Reconstructing Dynamic Shape and Skeleton of Articulated Objects from Single Monocular Video**|从单一的单目视频中重建动态关节对象具有挑战性，需要从有限的视图中联合估计形状、运动和相机参数。当前的方法通常需要大量的计算资源和训练时间，并需要额外的人工注释，如预定义的参数模型、相机姿势和关键点，这限制了它们的可推广性。我们提出了协同形状和骨架优化（S3O），这是一种新的两阶段方法，它放弃了这些先决条件，并有效地学习包括可见形状和底层骨架在内的参数模型。传统策略通常同时学习所有参数，导致相互依赖性，其中一个错误的预测可能会导致重大错误。相比之下，S3O采用了分阶段的方法：它首先专注于学习粗略的参数模型，然后进行运动学习和细节添加。这种方法大大降低了计算复杂度，并增强了从有限视角重建的鲁棒性，所有这些都不需要额外的注释。为了解决目前单目视频基准三维重建的不足，我们收集了PlanetZoo数据集。我们对标准基准和PlanetZoo数据集的实验评估证实，S3O提供了更准确的3D重建和看似合理的骨架，与最先进的技术相比，训练时间减少了约60%，从而提高了动态对象重建的技术水平。 et.al.|[2405.12607](http://arxiv.org/abs/2405.12607)|null|
|**2024-05-20**|**NPLMV-PS: Neural Point-Light Multi-View Photometric Stereo**|在这项工作中，我们提出了一种新的多视角光度立体（PS）方法。像3D重建中的许多工作一样，我们正在利用神经形状表示和学习的渲染器。然而，我们的工作与最先进的多视图PS方法（如PS NeRF或SuperNormal）不同，我们明确利用每像素强度渲染，而不是主要依赖于估计的法线。我们对点光衰减进行建模，并明确光线跟踪投射阴影，以便最佳地近似每个点的入射辐射。这被用作完全神经材料渲染器的输入，该渲染器使用最少的先验假设，并与曲面联合优化。最后，还可以合并估计的法线和分割图，以最大限度地提高表面精度。我们的方法是最早优于DiLiGenT MV经典方法的方法之一，并以大约400x400的分辨率实现了在大约1.5米距离成像的物体的平均0.2mm倒角距离。此外，我们在低光照场景中显示了对较差法线的鲁棒性，当使用像素渲染而不是估计法线时，实现了0.27mm的倒角距离。 et.al.|[2405.12057](http://arxiv.org/abs/2405.12057)|null|
|**2024-05-17**|**Photorealistic 3D Urban Scene Reconstruction and Point Cloud Extraction using Google Earth Imagery and Gaussian Splatting**|三维城市场景重建和建模是遥感的一个重要研究领域，在学术界、商业界、工业界和行政管理界有着广泛的应用。视图合成模型的最新进展促进了仅从2D图像进行真实感3D重建。利用Google Earth图像，我们构建了以滑铁卢大学为中心的滑铁卢地区的3D高斯散射模型，并能够根据我们在基准测试中演示的神经辐射场获得远远超过以往3D视图合成结果的视图合成结果。此外，我们使用从3D高斯散射模式中提取的3D点云检索场景的3D几何结构，我们将其与场景的多视图立体密集重建进行了对比，从而通过3D高斯散射重建大规模城市场景的3D几何形状和照片真实感照明 et.al.|[2405.11021](http://arxiv.org/abs/2405.11021)|null|
|**2024-05-16**|**Manifold-based Incomplete Multi-view Clustering via Bi-Consistency Guidance**|不完全多视图聚类主要致力于将未标记的数据划分为具有缺失实例的相应类别，由于其在实际应用中的优越性而受到广泛关注。考虑到不完全数据的影响，现有的方法大多试图通过添加额外的项来恢复数据。然而，对于无监督方法，一个简单的恢复策略会导致错误和异常值的积累，这将影响方法的性能。总体而言，以前的方法没有考虑到恢复实例的有效性，或者无法灵活地平衡恢复数据与原始数据之间的差异。为了解决这些问题，我们提出了一种新的方法，称为基于流形的双一致性引导不完全多视图聚类（MIMB），该方法可以灵活地恢复不同视图之间的不完整数据，并试图通过反向正则化实现双一致性引导。特别地，MIMB通过恢复丢失的实例将重建项添加到表示学习中，从而动态地检查潜在的一致性表示。此外，为了保持多个视图之间的一致性信息，MIMB实现了一种具有一致性表示的反向正则化的双一致性引导策略，并提出了一种用于探索恢复数据的隐藏结构的流形嵌入措施。值得注意的是，MIMB旨在平衡不同视图的重要性，并为每个视图引入自适应权重项。最后，设计了一种具有交替迭代优化策略的优化算法用于最终聚类。在6个基准数据集上进行了大量的实验结果，证实了与几个最先进的基线相比，MIMB可以显著获得优越的结果。 et.al.|[2405.10987](http://arxiv.org/abs/2405.10987)|null|
|**2024-05-16**|**CAT3D: Create Anything in 3D with Multi-View Diffusion Models**|3D重建的进步已经实现了高质量的3D捕捉，但需要用户收集数百到数千张图像来创建3D场景。我们介绍了CAT3D，这是一种通过使用多视图扩散模型模拟真实世界的捕捉过程来在3D中创建任何东西的方法。给定任意数量的输入图像和一组目标新颖视点，我们的模型生成场景的高度一致的新颖视图。这些生成的视图可以用作鲁棒3D重建技术的输入，以产生可以从任何视点实时渲染的3D表示。CAT3D可以在一分钟内创建整个3D场景，并且优于现有的单图像和少视图3D场景创建方法。有关结果和交互式演示，请访问我们的项目页面https://cat3d.github.io . et.al.|[2405.10314](http://arxiv.org/abs/2405.10314)|null|
|**2024-05-15**|**Classifying geospatial objects from multiview aerial imagery using semantic meshes**|航空图像越来越多地用于地球科学和自然资源管理，作为劳动密集型地面调查的补充。航空系统可以收集重叠的图像，这些图像从不同的角度提供每个位置的多个视图。然而，大多数预测方法（例如，用于树种分类）使用单个合成的自上而下的“正交镶嵌”图像作为输入，该图像几乎不包含关于对象的垂直方面的信息，并且可能包括处理伪像。我们提出了一种替代方法，直接在原始图像上生成预测，并使用语义网格将这些预测准确映射到地理空间坐标中。这种方法 $\unicode｛x2013｝$作为一个用户友好的开源工具包$\unicode{x2013｝$ 发布，使分析人员能够使用最高质量的数据进行预测，捕捉物体侧面的信息，并利用每个位置的多个视点来增加稳健性。我们在美国西部四个森林点的新基准数据集上证明了这种方法的价值，该数据集包括无人机图像、摄影测量结果、预测的树木位置和人工调查得出的物种分类数据。我们表明，在具有挑战性的跨站点树种分类任务中，相对于正交镶嵌基线，我们提出的多视角方法将分类精度从53%提高到75%。 et.al.|[2405.09544](http://arxiv.org/abs/2405.09544)|null|
|**2024-05-14**|**Dynamic NeRF: A Review**|神经辐射场（NeRF）是一种新的实现高分辨率三维重建和表示的隐式方法。在NeRF的首次研究提出后，NeRF获得了强大的发展动力，并在三维建模、表示和重建领域蓬勃发展。然而，基于NeRF的第一个和随后的大多数研究项目都是静态的，在实际应用中很薄弱。因此，越来越多的研究者对在实际应用或情况下更可行、更有用的动态NeRF的研究产生了兴趣和关注。与静态NeRF相比，动态NeRF的实现更加困难和复杂。但动态在未来更有潜力，甚至是可编辑NeRF的基础。在这篇综述中，我们对Dynamci-NeRF的发展和重要实施原则进行了详细而丰富的阐述。动态NeRF的主要原理和发展分析是从2021年到2023年，包括大多数动态NeRF项目。此外，我们还用丰富多彩、新颖新颖的特殊设计图形和表格，对各种动态的不同特点进行了详细的比较和分析。此外，我们还分析和讨论了实现动态NeRF的关键方法。参考文献的数量很大。陈述和比较是多方面的。通过阅读这篇综述，可以很容易地理解和获得Dynamic NeRF的整个发展历史和大多数主要设计方法或原理。 et.al.|[2405.08609](http://arxiv.org/abs/2405.08609)|null|
|**2024-05-12**|**Hologram: Realtime Holographic Overlays via LiDAR Augmented Reconstruction**|在臭名昭著的《星球大战》系列全息技术的指导下，我提出了一个使用激光雷达增强3D重建创建实时全息覆盖的应用程序。先前的尝试涉及SLAM或NeRF，它们要么需要高度校准的场景，要么产生高昂的计算成本，要么无法渲染动态场景。我提出了3种高保真度重建工具，可以在便携式设备上运行，例如iPhone 14 Pro，它可以实现精确的面部重建。我的系统实现了交互式和沉浸式全息体验，可用于广泛的应用，包括增强现实、远程呈现和娱乐。 et.al.|[2405.07178](http://arxiv.org/abs/2405.07178)|null|
|**2024-05-12**|**CoViews: Adaptive Augmentation Using Cooperative Views for Enhanced Contrastive Learning**|数据扩充在生成有效对比学习所需的高质量正负对方面发挥着关键作用。然而，常见的做法涉及重复使用单个增强策略来生成多个视图，由于视图之间缺乏合作，可能导致训练对效率低下。此外，为了找到最佳的扩充集，许多现有方法需要广泛的监督评估，忽略了模型的演变性质，在整个训练过程中可能需要不同的扩充。其他方法训练可微增广生成器，从而限制了文献中不可微变换函数的使用。在本文中，我们通过提出一个框架来解决这些挑战，该框架用于以最小的计算开销学习用于对比学习的高效自适应数据增强策略。我们的方法在培训期间不断生成新的数据增强策略，并在没有任何监督的情况下产生有效的积极/消极因素。在这个框架内，我们提出了两种方法：\ac｛IndepViews｝，它生成在所有视图中使用的增强策略；\ac{CoViews}，它为每个视图生成依赖的增强策略。这使我们能够学习应用于每个视图的转换之间的依赖关系，并确保应用于不同视图的增强策略相互补充，从而产生更有意义和有区别的表示。通过在多个数据集和对比学习框架上的广泛实验，我们证明了我们的方法始终优于基线解决方案，并且使用依赖于视图的增强策略的训练优于使用跨视图共享的独立策略的训练，展示了其在增强对比学习性能方面的有效性。 et.al.|[2405.07116](http://arxiv.org/abs/2405.07116)|null|
|**2024-05-11**|**TD-NeRF: Novel Truncated Depth Prior for Joint Camera Pose and Neural Radiance Field Optimization**|对精确相机姿态的依赖是神经辐射场（NeRF）模型在3D重建和SLAM任务中广泛部署的一个重要障碍。现有方法引入单目深度先验来联合优化相机姿态和NeRF，未能充分利用深度先验，并忽略了其固有噪声的影响。在本文中，我们提出了截断深度NeRF（TD NeRF），这是一种新的方法，通过联合优化辐射场和相机姿态的可学习参数，可以从未知的相机姿态中训练NeRF。我们的方法通过三个关键进展明确利用了单目深度先验：1）我们提出了一种新的基于截断正态分布的基于深度的射线采样策略，提高了姿态估计的收敛速度和精度；2） 为了规避局部极小值并细化深度几何，我们引入了一种从粗到细的训练策略，该策略逐步提高了深度精度；3） 我们提出了一种更鲁棒的帧间点约束，该约束增强了训练过程中对深度噪声的鲁棒性。在三个数据集上的实验结果表明，TD NeRF在相机姿态和NeRF的联合优化方面取得了卓越的性能，超过了以往的工作，并生成了更准确的深度几何。我们方法的实现已在发布https://github.com/nubot-nudt/TD-NeRF. et.al.|[2405.07027](http://arxiv.org/abs/2405.07027)|**[link](https://github.com/nubot-nudt/td-nerf)**|

<p align=right>(<a href=#updated-on-20240523>back to top</a>)</p>

## Diffusion

|Publish Date|Title|Abstract|PDF|Code|
|---|---|---|---|---|
|**2024-05-21**|**Personalized Residuals for Concept-Driven Text-to-Image Generation**|我们提出了个性化残差和局部注意力引导采样，用于使用文本到图像扩散模型进行高效的概念驱动生成。我们的方法首先通过冻结预训练的文本条件扩散模型的权重并学习模型层的一小部分的低秩残差来表示概念。然后，基于残差的方法直接实现了我们提出的采样技术的应用，该技术仅在通过交叉关注定位概念的区域中应用所学习的残差，并在所有其他区域中应用原始扩散权重。因此，局部采样将概念的学习身份与基础扩散模型的现有生成先验相结合。我们表明，在不使用正则化图像的情况下，个性化残差在单个GPU上有效地在约3分钟内捕获概念的同一性，并且与以前的模型相比，参数更少，并且局部采样允许使用原始模型作为图像大部分的强先验。 et.al.|[2405.12978](http://arxiv.org/abs/2405.12978)|null|
|**2024-05-21**|**Face Adapter for Pre-Trained Diffusion Models with Fine-Grained ID and Attribute Control**|目前的人脸再现和交换方法主要依赖于GAN框架，但最近的重点已经转移到预先训练的扩散模型上，因为它们具有优越的生成能力。然而，训练这些模型是资源密集型的，其结果尚未达到令人满意的性能水平。为了解决这个问题，我们介绍了人脸适配器，这是一种高效的适配器，专为预训练扩散模型的高精度高保真人脸编辑而设计。我们观察到，两个人脸再现/交换任务本质上都涉及目标结构、ID和属性的组合。我们的目标是充分解耦对这些因素的控制，以在一个模型中实现这两项任务。具体来说，我们的方法包括：1）空间条件生成器，提供精确的地标和背景；2） 一种即插即用的身份编码器，通过转换器解码器将人脸嵌入传输到文本空间。3） 集成空间条件和详细属性的属性控制器。与完全微调的面部再现/交换模型相比，Face Adapter在运动控制精度、ID保持能力和生成质量方面实现了相当甚至卓越的性能。此外，Face Adapter与各种StableDiffusion模型无缝集成。 et.al.|[2405.12970](http://arxiv.org/abs/2405.12970)|null|
|**2024-05-21**|**Differential Walk on Spheres**|我们介绍了一种蒙特卡罗方法，用于评估偏微分方程（PDE）解相对于问题参数（如域几何或边界条件）的导数。导数可以在任意点进行评估，而无需执行全局求解或构建体积网格或网格。因此，该方法非常适合于复杂几何的反问题，如PDE约束的形状优化。与其他“漫游球体”（WoS）算法一样，我们的方法在并行化方面微不足道，并且对边界表示（网格、样条曲线、隐式曲面等）不可知，支持大的拓扑变化。我们特别关注筛选泊松方程，它对科学和几何计算中的各种问题进行建模。正如在可微分渲染中一样，我们共同估计关于所有参数的导数——因此，成本不会随着参数计数而显著增长。在实践中，对于基于随机梯度的优化，即使是有噪声的导数估计也表现出快速、稳定的收敛性——正如我们通过热设计、扩散形状和计算机图形学的例子所展示的那样。 et.al.|[2405.12964](http://arxiv.org/abs/2405.12964)|null|
|**2024-05-21**|**Learning the Infinitesimal Generator of Stochastic Diffusion Processes**|我们讨论了随机扩散过程的无穷小生成器的数据驱动学习，这对于理解自然和物理系统的数值模拟至关重要。生成器的无界性质带来了重大挑战，使得希尔伯特-施密特算子的传统分析技术无效。为了克服这一点，我们引入了一种新的基于能量泛函的随机过程框架。我们的方法通过基于能量的风险度量在全部和部分知识环境中集成了物理先验。我们评估了降秩估计器在部分知识环境下再现核希尔伯特空间（RKHS）中的统计性能。值得注意的是，我们的方法提供了独立于状态空间维度的学习边界，并确保了无伪谱估计。此外，我们还阐明了随机扩散的固有能量诱导度量和用于生成器估计的RKHS度量之间的失真如何影响谱学习边界。 et.al.|[2405.12940](http://arxiv.org/abs/2405.12940)|null|
|**2024-05-21**|**Impact of inhomogeneous diffusion on secondary cosmic ray and antiproton local spectra**|最近的 $\gamma$ 射线和中微子观测似乎有利于考虑宇宙射线在整个银河系中的不均匀扩散。在这项研究中，我们研究了空间相关的CR不均匀传播对在地球上探测到的次级CR和反质子通量的影响。在不同的场景之间进行比较，以寻找可能在不久的将来引导我们倾向于一个而不是另一个的潜在特征。我们还研究了非均匀传播对与气体相互作用产生次级CR的影响，以及这种情况对作为暗物质湮灭最终产物产生的反质子和光反核的局部通量的影响。我们的结果表明，考虑非均匀扩散模型可以提高预测的局部反质子通量与B、Be和Li的通量的兼容性，假设这些粒子只有二次起源。此外，我们的模型预测了一个稍微困难的局部反质子光谱，使其与AMS-02的高能测量更兼容。最后，在所考虑的不同传播场景中，暗物质产生的反质子和反核的预测局部通量预计不会发生显著变化。 et.al.|[2405.12918](http://arxiv.org/abs/2405.12918)|null|
|**2024-05-21**|**An Empirical Study and Analysis of Text-to-Image Generation Using Large Language Model-Powered Textual Representation**|忠实的文本到图像生成的一个关键先决条件是对文本输入的准确理解。现有的方法利用CLIP模型的文本编码器来表示输入提示。然而，预先训练的CLIP模型只能以77的最大标记长度对英语进行编码。此外，与大型语言模型（LLM）相比，CLIP的文本编码器的模型容量相对有限，后者提供多语言输入，适应更长的上下文，并实现卓越的文本表示。在本文中，我们研究了LLM作为文本编码器，以提高文本到图像生成中的语言理解。不幸的是，使用LLM从头开始训练文本到图像生成模型需要大量的计算资源和数据。为此，我们引入了一个三阶段的训练管道，该管道将现有的文本到图像模型与LLM有效地集成在一起。具体来说，我们提出了一种轻量级适配器，它能够使用LLM的文本表示快速训练文本到图像模型。大量实验表明，我们的模型不仅支持多语言，而且支持更长的输入上下文，具有卓越的图像生成质量。 et.al.|[2405.12914](http://arxiv.org/abs/2405.12914)|null|
|**2024-05-21**|**Deep HST/UVIS imaging of the candidate dark galaxy CDG-1**|CDG-1是英仙座星团中四个可能的球状星团的紧密组合，是一个几乎没有漫射光的候选暗星系。在这里，我们使用HST/UVISF200LP成像，对任何潜在恒星发射的光度提供了新的限制。未检测到扩散发射，在CDG-1的5英寸尺度上，F200LP的2 $\sigma$上限>28.1 mag/arcsec$^2$。该表面亮度极限对应于球状星团形式的总光度部分的2$\sigma$ 下限>0.5。最有可能的选择，尽管不太可能，是CDG-1是英仙座星系IC312光环中四个球状星团的偶然组合。 et.al.|[2405.12907](http://arxiv.org/abs/2405.12907)|null|
|**2024-05-21**|**Diffusion of brightened dark excitons in a high-angle incommensurate Moiré homobilayer**|在过去的几年里，人们对twistronics领域的兴趣和研究工作激增，特别是在过渡金属二卤代化合物的低角度扭曲双层中。这些新型材料平台已被证明可以承载激子量子发射体的周期性阵列、寿命长的层间激子和奇异的多体态。虽然关于这些异质结构还有很多事情需要了解和理解，但对高角度、不可通约双层领域的探索更少。在大于几度的扭曲角下，这些双层中周期性的存在变得混乱，由于制造技术的限制，使得系统本质上是非周期性的和不可通约的。在这项工作中，我们证明了在扭曲的二硒化钼均双层中出现了明亮的暗层内激子。我们表明，与三极管或激子相比，这种暗激子更有效地扩散穿过激发点，达到大于4微米的扩散长度。温度相关光谱提供了确证，并揭示了一个明亮的暗三极管。我们的结果揭示了这些高角度系统的一些丰富的物理性质。 et.al.|[2405.12901](http://arxiv.org/abs/2405.12901)|null|
|**2024-05-21**|**Diffusion-RSCC: Diffusion Probabilistic Model for Change Captioning in Remote Sensing Images**|遥感图像变化字幕（RSICC）旨在生成类人语言来描述双时间遥感图像对之间的语义变化。它为环境动态和土地管理提供了宝贵的见解。与传统的更改字幕任务不同，RSICC不仅涉及在不同模态中检索相关信息并生成流畅的字幕，还涉及减轻像素级差异对地形更改定位的影响。由于时间跨度长，像素问题降低了生成字幕的准确性。受扩散模型显著生成能力的启发，我们提出了一个RSICC的概率扩散模型来解决上述问题。在训练过程中，我们构造了一个以跨模态特征为条件的噪声预测器，以学习马尔可夫链下从真实字幕分布到标准高斯分布的分布。同时，针对反向过程中的噪声预测器，设计了跨模式融合和叠加自注意模块。在测试阶段，训练有素的噪声预测器有助于估计分布的平均值，并逐步生成变化字幕。在LEVIR-CC数据集上进行的大量实验证明了我们的扩散RSCC及其单个组件的有效性。定量结果显示，在传统和新增强的指标中，与现有方法相比，性能优越。代码和材料将在线提供，网址为https://github.com/Fay-Y/Diffusion-RSCC. et.al.|[2405.12875](http://arxiv.org/abs/2405.12875)|**[link](https://github.com/fay-y/diffusion-rscc)**|
|**2024-05-21**|**High-Field Microscale NMR Spectroscopy with NV Centers in Dipolarly-Coupled Samples**|基于金刚石的量子传感器在快速分子运动平均目标核之间偶极相互作用的情况下，实现了微尺度的高分辨率NMR光谱。然而，在低扩散的样品中，普遍存在的偶极耦合对相关光谱信息的提取提出了挑战。在这项工作中，我们提出了一种协议，该协议能够使用基于氮空位（NV）集成的传感器在高磁场下扫描偶极耦合样品中的核自旋。我们的协议基于射频（RF）和微波（MW）辐射的同步传输，以消除扫描样本中原子核之间的耦合，并从样本的磁化动力学中有效地提取目标能量偏移。此外，该方法被设计为在高磁场下操作，从而导致更大的样品热极化，从而增加NMR信号。我们的方法的精度最终受到样本相干时间的限制，从而能够准确识别固态系统中的相关能量偏移。 et.al.|[2405.12857](http://arxiv.org/abs/2405.12857)|null|

<p align=right>(<a href=#updated-on-20240523>back to top</a>)</p>

## NeRF

|Publish Date|Title|Abstract|PDF|Code|
|---|---|---|---|---|
|**2024-05-21**|**Implicit-ARAP: Efficient Handle-Guided Deformation of High-Resolution Meshes and Neural Fields via Local Patch Meshing**|在这项工作中，我们提出了神经符号距离场的局部补丁网格表示。该技术允许通过仅使用SDF信息及其梯度将平面面片网格投影和变形到标高集曲面上来离散输入SDF的标高集的局部区域。我们的分析表明，这种方法比标准的行进立方体算法更准确地逼近隐式曲面。然后，我们将这种表示应用于手柄引导变形的设置：我们引入了两个不同的管道，它们利用3D神经场来计算在给定约束集下高分辨率网格和神经场的“尽可能刚性”变形。我们对我们的方法和神经场和网格变形的各种基线进行了全面评估，结果表明，这两条管道在结果质量和稳健性方面都取得了令人印象深刻的效率和显著的改进。通过我们的新型流水线，我们引入了一种可扩展的方法来解决高分辨率网格上公认的几何处理问题，并为通过局部面片网格将其他几何任务扩展到隐式曲面领域铺平了道路。 et.al.|[2405.12895](http://arxiv.org/abs/2405.12895)|null|
|**2024-05-16**|**Single-shot volumetric fluorescence imaging with neural fields**|与需要在多个轴向平面上扫描的传统成像方法相比，单次体积荧光（SVF）成像提供了显著的优势，因为它可以在大视场上以高时间分辨率捕获生物过程。现有的SVF成像方法通常需要大的、复杂的点扩展函数（PSF）来满足压缩传感的多路复用要求，这限制了信噪比、分辨率和/或视场。在本文中，我们介绍了QuadraPol-PSF与神经场相结合，这是一种新的SVF成像方法。该方法在后焦平面利用成本效益高的定制偏振器和偏振相机来检测荧光，在紧凑的PSF内有效地编码3D场景，而没有深度模糊。此外，我们提出了一种基于神经场技术的重建算法，该算法解决了用于校正成像系统像差的相位检索方法的不精确性。该算法将实验PSF的准确性与计算生成的检索PSF的长景深相结合。QuadraPol PSF与神经场相结合，可将传统荧光显微镜的采集时间显著缩短约20倍，并可一次性捕获100 mm $^3$ 立方体积。我们通过对沙子表面细菌菌落的全聚焦成像和植物根系形态的可视化，验证了我们的硬件和算法的有效性。我们的方法为推进生物学研究和生态学研究提供了强有力的工具。 et.al.|[2405.10463](http://arxiv.org/abs/2405.10463)|null|
|**2024-05-08**|**${M^2D}$NeRF: Multi-Modal Decomposition NeRF with 3D Feature Fields**|神经场（NeRF）已经成为表示连续3D场景的一种很有前途的方法。然而，NeRF中缺乏语义编码对场景分解提出了重大挑战。为了应对这一挑战，我们提出了一个单一的模型，即多模式分解NeRF（${M^2D}$ NeRF），它能够进行基于文本和基于视觉补丁的编辑。具体来说，我们使用多模态特征提取将来自预训练的视觉和语言模型的教师特征集成到3D语义特征体积中，从而促进一致的3D编辑。为了增强三维特征体积中视觉特征和语言特征之间的一致性，我们引入了多模态相似性约束。我们还引入了一种基于补丁的联合对比损失，这有助于鼓励对象区域在3D特征空间中合并，从而产生更精确的边界。与先前的基于NeRF的方法相比，在各种真实世界场景上的实验显示出在3D场景分解任务中的优越性能。 et.al.|[2405.05010](http://arxiv.org/abs/2405.05010)|null|
|**2024-05-09**|**Radar Fields: Frequency-Space Neural Scene Representations for FMCW Radar**|神经场作为再现和新一代各种户外场景的场景表示，包括自动驾驶汽车和机器人必须处理的场景，已经得到了广泛的研究。虽然存在RGB和激光雷达数据的成功方法，但雷达作为传感模式的神经重建方法在很大程度上尚未被探索。雷达传感器在毫米波长下工作，对雾和雨中的散射具有鲁棒性，因此为主动和被动光学传感技术提供了一种互补的方式。此外，现有的雷达传感器具有很高的成本效益，并广泛应用于户外作业的机器人和车辆中。我们介绍了雷达场——一种为有源雷达成像器设计的神经场景重建方法。我们的方法将一个明确的、基于物理的传感器模型与一个隐含的神经几何和反射模型相结合，直接合成原始雷达测量值并提取场景占用率。所提出的方法不依赖于体绘制。相反，我们在傅立叶频率空间中学习场，并用原始雷达数据进行监督。我们在不同的室外场景中验证了该方法的有效性，包括车辆和基础设施密集的城市场景，以及在毫米波长传感特别有利的恶劣天气场景中。 et.al.|[2405.04662](http://arxiv.org/abs/2405.04662)|null|
|**2024-05-06**|**Neural Graph Mapping for Dense SLAM with Efficient Loop Closure**|现有的基于神经场的SLAM方法通常使用单个单片场作为其场景表示。这阻碍了循环闭合约束的有效结合，并限制了可扩展性。为了解决这些缺点，我们提出了一种神经映射框架，该框架将轻量级神经场锚定到稀疏视觉SLAM系统的姿态图上。我们的方法显示了整合大规模闭环的能力，同时限制了必要的重新融合。此外，我们通过在优化过程中考虑多个环路闭合来验证我们的方法的可扩展性，并证明我们的方法在质量和运行时间方面优于现有的最先进的方法。我们的代码可在https://kth-rpl.github.io/neural_graph_mapping/. et.al.|[2405.03633](http://arxiv.org/abs/2405.03633)|null|
|**2024-05-03**|**Simulation-based Inference of Developmental EEG Maturation with the Spectral Graph Model**|宏观神经活动的光谱内容在整个发育过程中不断演变，但这种成熟与潜在的大脑网络形成和动力学之间的关系尚不清楚。为了深入了解这一过程的机制，我们通过频谱图模型（SGM）的贝叶斯模型反演来评估发育脑电频谱变化，SGM是一种全脑空间频谱活动的简约模型，源于由结构连接体耦合的线性化神经场模型。基于模拟的推理用于从跨越发育期的脑电图频谱中估计年龄变化的SGM参数后验分布。我们发现，这种模型拟合方法通过关键神经参数的神经生物学一致进展准确地捕捉了脑电图频谱的发育成熟：长程耦合、轴突传导速度和兴奋性：抑制性平衡。这些结果表明，在正常发育过程中观察到的大脑活动的光谱成熟得到了功能适应的支持，特别是局部神经动力学的年龄依赖性调节及其在宏观结构网络中的长期耦合。 et.al.|[2405.02524](http://arxiv.org/abs/2405.02524)|null|
|**2024-04-30**|**Lightplane: Highly-Scalable Components for Neural 3D Fields**|当代3D研究，特别是在重建和生成方面，严重依赖2D图像进行输入或监督。然而，这些2D-3D映射的当前设计是内存密集型的，对现有方法构成了显著的瓶颈，并阻碍了新的应用。作为回应，我们为3D神经场提出了一对高度可扩展的组件：Lightplane Render和Splatter，这显著减少了2D-3D映射中的内存使用。这些创新能够以较小的内存和计算成本处理更多、更高分辨率的图像。我们展示了它们在各种应用中的实用性，从有利于图像级损失的单场景优化到实现用于大幅缩放3D重建和生成的多功能管道。代码：\url{https://github.com/facebookresearch/lightplane}. et.al.|[2404.19760](http://arxiv.org/abs/2404.19760)|**[link](https://github.com/facebookresearch/lightplane)**|
|**2024-05-03**|**Object Registration in Neural Fields**|神经场以一种对机器人应用具有巨大前景的方式提供3D几何结构和外观的连续场景表示。解锁机器人中神经领域独特用例的一个功能是对象6-DoF注册。在本文中，我们对最近的Reg-NF神经场配准方法及其在机器人环境中的用例进行了扩展分析。我们展示了使用场景和对象神经场模型确定场景中已知对象的6-DoF姿态的场景。我们展示了如何使用它来更好地表示未完全建模的场景中的对象，并通过将对象神经场模型替换到场景中来生成新的场景。 et.al.|[2404.18381](http://arxiv.org/abs/2404.18381)|null|
|**2024-04-26**|**ArtNeRF: A Stylized Neural Field for 3D-Aware Cartoonized Face Synthesis**|生成视觉模型和神经辐射领域的最新进展极大地促进了3D感知图像合成和风格化任务。然而，以前基于NeRF的工作仅限于单场景风格化，训练模型生成具有任意风格的3D感知卡通人脸仍然没有解决。为了解决这个问题，我们提出了ArtNeRF，这是一种从3D感知GAN中派生出来的新颖的人脸风格化框架。在这个框架中，我们利用表达生成器来合成风格化的人脸，并利用三分支鉴别器模块来提高生成人脸的视觉质量和风格一致性。具体而言，利用基于对比学习的风格编码器来提取风格图像的鲁棒低维嵌入，使生成器能够获得各种风格的知识。为了平滑跨领域迁移学习的训练过程，我们提出了一个自适应风格混合模块，该模块有助于注入风格信息，并允许用户自由调整风格化水平。我们进一步引入了一个神经渲染模块，以实现更高分辨率图像的高效实时渲染。大量实验表明，ArtNeRF在生成具有任意风格的高质量3D感知卡通人脸方面是通用的。 et.al.|[2404.13711](http://arxiv.org/abs/2404.13711)|**[link](https://github.com/silence-tang/artnerf)**|
|**2024-04-19**|**BANF: Band-limited Neural Fields for Levels of Detail Reconstruction**|主要由于其隐含性质，神经场缺乏直接的滤波机制，因为离散信号处理的傅立叶分析不直接适用于这些表示。神经场的有效滤波对于实现下游应用程序中的细节处理水平至关重要，并支持在规则网格上对场进行采样的操作（例如，行进立方体）。试图在频域中分解神经场的现有方法要么采用启发式方法，要么需要对神经场架构进行广泛修改。我们展示了通过一个简单的修改，可以获得低通滤波的神经场，进而展示了如何利用这一点来获得整个信号的频率分解。我们通过研究细节水平重建来证明我们的技术的有效性，并展示了如何有效地计算粗糙的表示。 et.al.|[2404.13024](http://arxiv.org/abs/2404.13024)|null|

<p align=right>(<a href=#updated-on-20240523>back to top</a>)</p>

[contributors-shield]: https://img.shields.io/github/contributors/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[contributors-url]: https://github.com/Vincentqyw/cv-arxiv-daily/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[forks-url]: https://github.com/Vincentqyw/cv-arxiv-daily/network/members
[stars-shield]: https://img.shields.io/github/stars/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[stars-url]: https://github.com/Vincentqyw/cv-arxiv-daily/stargazers
[issues-shield]: https://img.shields.io/github/issues/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[issues-url]: https://github.com/Vincentqyw/cv-arxiv-daily/issues

