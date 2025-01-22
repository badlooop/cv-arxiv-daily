[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]

## Updated on 2025.01.22
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
|**2025-01-21**|**HAC++: Towards 100X Compression of 3D Gaussian Splatting**|3D高斯散斑（3DGS）已成为一种有前景的新型视图合成框架，具有快速渲染速度和高保真度。然而，大量的高斯分布及其相关属性需要有效的压缩技术。然而，高斯点云（或我们论文中的锚点）的稀疏性和无组织性给压缩带来了挑战。为了实现紧凑的大小，我们提出了HAC++，它利用了无组织锚点和结构化哈希网格之间的关系，利用它们的互信息进行上下文建模。此外，HAC++捕获锚点内的上下文关系，以进一步提高压缩性能。为了促进熵编码，我们利用高斯分布来精确估计每个量化属性的概率，其中提出了一种自适应量化模块来实现这些属性的高精度量化，以提高保真度恢复。此外，我们采用了一种自适应掩蔽策略来消除无效的高斯分布和锚点。总体而言，与vanilla 3DGS相比，HAC++在所有数据集上平均时实现了超过100倍的显著尺寸减小，同时提高了保真度。与脚手架GS相比，它还可以减少20倍以上的尺寸。我们的代码可在https://github.com/YihangChen-ee/HAC-plus. et.al.|[2501.12255](http://arxiv.org/abs/2501.12255)|null|
|**2025-01-21**|**Survey on Monocular Metric Depth Estimation**|单目深度估计（MDE）是一项基本的计算机视觉任务，支撑着空间理解、3D重建和自动驾驶等应用。虽然基于深度学习的MDE方法可以从单个图像中预测相对深度，但它们缺乏度量尺度信息通常会导致尺度不一致，限制了它们在视觉SLAM、3D重建和新颖视图合成等下游任务中的实用性。单目度量深度估计（MMDE）通过实现精确的场景级深度推断来解决这些挑战。MMDE提高了深度一致性，增强了顺序任务的稳定性，简化了与下游应用程序的集成，并拓宽了实际用例。本文对深度估计技术进行了全面的回顾，重点介绍了从基于几何的方法到最先进的深度学习方法的演变。它强调了标度不可知方法的进步，这对于实现零样本泛化作为MMDE的基础能力至关重要。探讨了零样本MMDE研究的最新进展，重点讨论了模型泛化和场景边界细节丢失等挑战。解决这些问题的创新策略包括无标签数据增强、图像修补、架构优化和生成技术。详细分析后，这些进步表明了对克服现有局限性的重大贡献。最后，本文综合了零样本MMDE的最新发展，确定了尚未解决的挑战，并概述了未来的研究方向。通过提供清晰的路线图和前沿的见解，这项工作旨在加深对MMDE的理解，激发新的应用，并推动技术创新。 et.al.|[2501.11841](http://arxiv.org/abs/2501.11841)|null|
|**2025-01-20**|**See In Detail: Enhancing Sparse-view 3D Gaussian Splatting with Local Depth and Semantic Regularization**|3D高斯散斑（3DGS）在新颖的视图合成中表现出了显著的性能。然而，当输入视图稀疏时，其渲染质量会下降，导致内容失真和细节减少。这种限制阻碍了它的实际应用。为了解决这个问题，我们提出了一种稀疏视图3DGS方法。鉴于稀疏视图渲染固有的不适定性，整合先验信息至关重要。我们提出了一种语义正则化技术，使用从预训练的DINO-ViT模型中提取的特征来确保多视图语义的一致性。此外，我们提出了局部深度正则化，它约束深度值以提高对看不见的视图的泛化能力。我们的方法优于最先进的新颖视图合成方法，在LLFF数据集上实现了高达0.4dB的PSNR改善，同时减少了失真并提高了视觉质量。 et.al.|[2501.11508](http://arxiv.org/abs/2501.11508)|null|
|**2025-01-18**|**Decoupling Appearance Variations with 3D Consistent Features in Gaussian Splatting**|高斯散斑已成为新颖视图合成中一种突出的3D表示，但它仍然存在外观变化，这是由各种因素引起的，如现代相机ISP、一天中的不同时间、天气条件和局部光线变化。这些变化可能会导致渲染图像/视频中的浮动和颜色失真。高斯散斑中最近的外观建模方法要么与渲染过程紧密耦合，阻碍了实时渲染，要么只考虑了轻微的全局变化，在局部光线变化的场景中表现不佳。在本文中，我们提出了DAVIGS，这是一种以即插即用和高效的方式解耦外观变化的方法。通过在图像级别而不是高斯级别转换渲染结果，我们的方法可以在最小的优化时间和内存开销下对外观变化进行建模。此外，我们的方法在3D空间中收集与外观相关的信息来转换渲染图像，从而隐式地建立视图之间的3D一致性。我们在几个外观变体场景上验证了我们的方法，并证明它在不影响渲染速度的情况下，以最少的训练时间和内存使用实现了最先进的渲染质量。此外，它以即插即用的方式为不同的高斯散斑基线提供了性能改进。 et.al.|[2501.10788](http://arxiv.org/abs/2501.10788)|null|
|**2025-01-16**|**CrossModalityDiffusion: Multi-Modal Novel View Synthesis with Unified Intermediate Representation**|地理空间成像利用了来自各种传感方式的数据，如地球观测、合成孔径雷达和激光雷达，从地面无人机到卫星视图。这些异构输入为场景理解提供了重要机会，但在准确解释几何体方面存在挑战，特别是在缺乏精确地面实况数据的情况下。为了解决这个问题，我们提出了CrossModalityDiffusion，这是一个模块化框架，旨在在没有场景几何先验知识的情况下生成不同模态和视点的图像。CrossModalityDiffusion采用特定于模态的编码器，这些编码器拍摄多个输入图像并产生几何感知特征体，这些特征体对相对于其输入相机位置的场景结构进行编码。放置特征体积的空间是统一输入模式的共同基础。这些特征体被重叠，并使用体绘制技术从新的角度渲染成特征图像。渲染的特征图像被用作特定模态扩散模型的调节输入，从而能够合成所需输出模态的新图像。在本文中，我们证明了联合训练不同的模块可以确保框架内所有模态的一致几何理解。我们在合成ShapeNet汽车数据集上验证了CrossModalityDiffusion的能力，证明了它在跨多种成像模态和视角生成准确一致的新视图方面的有效性。 et.al.|[2501.09838](http://arxiv.org/abs/2501.09838)|null|
|**2025-01-14**|**3D Gaussian Splatting with Normal Information for Mesh Extraction and Improved Rendering**|可区分的3D高斯飞溅已成为一种高效灵活的渲染技术，用于从2D视图集合中表示复杂场景，并实现高质量的实时新颖视图合成。然而，它对光度损失的依赖可能会导致重建的几何结构和提取的网格不精确，特别是在具有高曲率或精细细节的区域。我们提出了一种新的正则化方法，该方法使用从高斯估计的带符号距离函数的梯度来提高渲染质量，同时提取表面网格。规范化的常规监督有助于更好的渲染和网格重建，这对于视频生成、动画、AR-VR和游戏中的下游应用至关重要。我们展示了我们的方法在Mip-NeRF360、坦克和神庙以及深度混合等数据集上的有效性。与其他网格提取渲染方法相比，我们的方法在真实感度量上得分更高，而不会影响网格质量。 et.al.|[2501.08370](http://arxiv.org/abs/2501.08370)|null|
|**2025-01-14**|**VINGS-Mono: Visual-Inertial Gaussian Splatting Monocular SLAM in Large Scenes**|VINGS Mono是一个专为大型场景设计的单目（惯性）高斯散斑（GS）SLAM框架。该框架由四个主要组件组成：VIO前端、2D高斯映射、NVS环路闭合和动态擦除器。在VIO前端中，RGB帧通过密集束调整和不确定性估计进行处理，以提取场景几何形状和姿态。基于该输出，映射模块递增地构建和维护2D高斯映射。2D高斯映射的关键组件包括基于样本的光栅化器、分数管理器和姿态细化，它们共同提高了映射速度和定位精度。这使得SLAM系统能够处理多达5000万个高斯椭球的大规模城市环境。为了确保大规模场景中的全局一致性，我们设计了一个环路闭合模块，该模块创新性地利用高斯散点的新颖视图合成（NVS）功能进行环路闭合检测和高斯图的校正。此外，我们提出了一种动态橡皮擦，以解决现实世界户外场景中动态对象不可避免的存在问题。在室内和室外环境中进行的广泛评估表明，我们的方法实现了与视觉惯性里程表相当的定位性能，同时超越了最近的GS/NeRF SLAM方法。在映射和渲染质量方面，它也明显优于所有现有方法。此外，我们开发了一款移动应用程序，并验证了我们的框架可以仅使用智能手机摄像头和低频IMU传感器实时生成高质量的高斯地图。据我们所知，VINGS Mono是第一种能够在室外环境中运行并支持公里级大型场景的单目高斯SLAM方法。 et.al.|[2501.08286](http://arxiv.org/abs/2501.08286)|null|
|**2025-01-13**|**Evaluating Human Perception of Novel View Synthesis: Subjective Quality Assessment of Gaussian Splatting and NeRF in Dynamic Scenes**|高斯散斑（GS）和神经辐射场（NeRF）是两项突破性的技术，它们彻底改变了新视图合成（NVS）领域，通过从一组稀疏视图的图像中合成多个视点，实现了沉浸式真实感渲染和用户体验。NVS的潜在应用，如高质量的虚拟和增强现实、详细的3D建模和逼真的医学器官成像，强调了从人类感知的角度对NVS方法进行质量评估的重要性。尽管之前的一些研究已经探索了NVS技术的主观质量评估，但它们仍然面临着一些挑战，特别是在NVS方法选择、场景覆盖和评估方法方面。为了应对这些挑战，我们进行了两个主观实验，对NVS技术进行质量评估，包括基于GS和基于NeRF的方法，重点关注动态和现实世界的场景。本研究涵盖了360度、正面和单视点视频，同时提供了更丰富、更多的真实场景。同时，这是首次探索NVS方法在具有运动物体的动态场景中的影响。这两种主观实验有助于从人类感知的角度充分理解不同观察路径的影响，并为未来开发全参考和无参考质量指标铺平道路。此外，我们在拟议的数据库上建立了各种最先进的客观指标的综合基准，强调现有方法仍然难以准确捕捉主观质量。这些结果让我们对现有NVS方法的局限性有了一些了解，并可能促进新NVS方法发展。 et.al.|[2501.08072](http://arxiv.org/abs/2501.08072)|null|
|**2025-01-13**|**Motion Tracks: A Unified Representation for Human-Robot Transfer in Few-Shot Imitation Learning**|教机器人自主完成日常任务仍然是一个挑战。模仿学习（IL）是一种强大的方法，通过演示向机器人灌输技能，但受到收集远程操作机器人数据的劳动密集型过程的限制。人类视频提供了一种可扩展的替代方案，但由于缺乏机器人动作标签，仍然很难直接从中训练IL策略。为了解决这个问题，我们建议将动作表示为图像上的短程2D轨迹。这些动作或运动轨迹捕捉人手或机器人末端执行器的预测运动方向。我们实例化了一个名为运动轨迹策略（MT-pi）的IL策略，该策略接收图像观测值并将运动轨迹作为动作输出。通过利用这种统一的跨实施例动作空间，MT-pi在只需几分钟的人类视频和有限的额外机器人演示的情况下，就可以成功完成任务。在测试时，我们从两个相机视图预测运动轨迹，通过多视图合成恢复6DoF轨迹。MT pi在4个现实世界任务中的平均成功率为86.5%，比不利用人类数据或我们的动作空间的最先进的IL基线高出40%，并推广到仅在人类视频中看到的场景。代码和视频可在我们的网站上找到https://portal-cornell.github.io/motion_track_policy/. et.al.|[2501.06994](http://arxiv.org/abs/2501.06994)|null|
|**2025-01-11**|**MapGS: Generalizable Pretraining and Data Augmentation for Online Mapping via Novel View Synthesis**|在线地图减少了自动驾驶汽车对高清地图的依赖，显著提高了可扩展性。然而，最近的进展往往忽视了跨传感器配置的通用性，导致当模型部署在具有不同摄像头内部和外部的车辆上时，性能下降。随着新型视图合成方法的快速发展，我们研究了这些技术在多大程度上可以用来解决传感器配置泛化挑战。我们提出了一种新的框架，利用高斯飞溅来重建场景，并在目标传感器配置中渲染相机图像。目标配置传感器数据以及映射到目标配置的标签用于训练在线映射模型。我们在nuScenes和Argoverse 2数据集上提出的框架通过有效的数据集增强实现了18%的性能提升，实现了更快的收敛和高效的训练，并且在仅使用25%的原始训练数据时超过了最先进的性能。这实现了数据重用，并减少了对繁琐的数据标记的需求。项目页面位于https://henryzhangzhy.github.io/mapgs. et.al.|[2501.06660](http://arxiv.org/abs/2501.06660)|null|

<p align=right>(<a href=#updated-on-20250122>back to top</a>)</p>

## 3D Reconstruction

|Publish Date|Title|Abstract|PDF|Code|
|---|---|---|---|---|
|**2025-01-21**|**Continuous 3D Perception Model with Persistent State**|我们提出了一个能够解决广泛3D任务的统一框架。我们的方法具有一个有状态的循环模型，该模型随着每次新的观察不断更新其状态表示。给定一系列图像，这种演变状态可用于以在线方式为每个新输入生成度量尺度点图（每像素3D点）。这些点地图位于一个共同的坐标系内，可以累积成一个连贯、密集的场景重建，随着新图像的到来而更新。我们的模型名为CUT3R（用于3D重建的连续更新变换器），它捕获了真实世界场景的丰富先验：它不仅可以从图像观察中预测准确的点图，还可以通过探测虚拟的、未观察到的视图来推断场景中看不见的区域。我们的方法简单但高度灵活，自然地接受不同长度的图像，这些图像可能是视频流或无序的照片集，包含静态和动态内容。我们在各种3D/4D任务中评估我们的方法，并在每项任务中展示具有竞争力或最先进的性能。项目页面：https://cut3r.github.io/ et.al.|[2501.12387](http://arxiv.org/abs/2501.12387)|null|
|**2025-01-21**|**DARB-Splatting: Generalizing Splatting with Decaying Anisotropic Radial Basis Functions**|随着3D高斯散斑技术的出现，基于散斑的3D重建方法越来越受欢迎，可以有效地合成高质量的新颖视图。这些方法通常采用指数族函数，如高斯函数，作为重建核，因为它们具有各向异性、易于投影和光栅化中的可微性。然而，该领域仍然局限于指数族内的变化，使得广义重建核在很大程度上未得到充分探索，部分原因是3D到2D投影中缺乏易积性。因此，我们证明了一类衰减各向异性径向基函数（DARBF）是马氏距离的非负函数，通过近似高斯函数的闭式积分优势来支持飞溅。通过这种新的视角，我们证明了在训练过程中收敛速度提高了34%，各种DARB重建内核的内存消耗减少了15%，同时保持了可比的PSNR、SSIM和LPIPS结果。我们将提供代码。 et.al.|[2501.12369](http://arxiv.org/abs/2501.12369)|null|
|**2025-01-21**|**DynoSAM: Open-Source Smoothing and Mapping Framework for Dynamic SLAM**|传统的视觉同步定位和映射（vSLAM）系统只关注静态场景结构，忽略了环境中的动态元素。虽然这些方法在复杂场景中对精确的视觉里程计有效，但它们丢弃了关于运动物体的关键信息。通过将这些信息整合到动态SLAM框架中，可以估计动态实体的运动，在确保准确定位的同时增强导航。然而，动态SLAM的基本公式仍然是一个开放的挑战，对于SLAM管道内精确运动估计的最佳方法没有达成共识。因此，我们开发了DynoSAM，这是一个动态SLAM的开源框架，可以有效地实现、测试和比较各种动态SLAM优化公式。DynoSAM将静态和动态测量整合到一个使用因子图解决的统一优化问题中，同时估计相机姿态、静态场景、物体运动或姿态以及物体结构。我们在各种模拟和现实数据集上评估DynoSAM，在室内和室外环境中实现了最先进的运动估计，并对现有系统进行了实质性改进。此外，我们还展示了DynoSAM在下游应用中的实用性，包括动态场景的3D重建和轨迹预测，从而展示了推进动态对象感知SLAM系统的潜力。DynoSAM开源于https://github.com/ACFR-RPG/DynOSAM. et.al.|[2501.11893](http://arxiv.org/abs/2501.11893)|null|
|**2025-01-21**|**Survey on Monocular Metric Depth Estimation**|单目深度估计（MDE）是一项基本的计算机视觉任务，支撑着空间理解、3D重建和自动驾驶等应用。虽然基于深度学习的MDE方法可以从单个图像中预测相对深度，但它们缺乏度量尺度信息通常会导致尺度不一致，限制了它们在视觉SLAM、3D重建和新颖视图合成等下游任务中的实用性。单目度量深度估计（MMDE）通过实现精确的场景级深度推断来解决这些挑战。MMDE提高了深度一致性，增强了顺序任务的稳定性，简化了与下游应用程序的集成，并拓宽了实际用例。本文对深度估计技术进行了全面的回顾，重点介绍了从基于几何的方法到最先进的深度学习方法的演变。它强调了标度不可知方法的进步，这对于实现零样本泛化作为MMDE的基础能力至关重要。探讨了零样本MMDE研究的最新进展，重点讨论了模型泛化和场景边界细节丢失等挑战。解决这些问题的创新策略包括无标签数据增强、图像修补、架构优化和生成技术。详细分析后，这些进步表明了对克服现有局限性的重大贡献。最后，本文综合了零样本MMDE的最新发展，确定了尚未解决的挑战，并概述了未来的研究方向。通过提供清晰的路线图和前沿的见解，这项工作旨在加深对MMDE的理解，激发新的应用，并推动技术创新。 et.al.|[2501.11841](http://arxiv.org/abs/2501.11841)|null|
|**2025-01-21**|**Self-Calibrated Epipolar Reconstruction for Assessment of Aneurysms in the Internal Carotid Artery Using In-Silico Biplane Angiograms**|颅内动脉瘤（IA）的治疗依赖于使用双平面视图的血管造影指导。然而，血管重叠和缩短往往会影响治疗的准确流量估计和设备尺寸，从而掩盖关键细节。本研究介绍了一种极线重建方法，利用常规采集的双平面血管造影数据增强颈内动脉（ICA）和动脉瘤圆顶的3D渲染。我们的方法旨在通过克服传统二维成像技术的局限性来改善程序指导。本研究采用ICA动脉瘤的三种3D几何形状来模拟虚拟血管造影。这些血管造影是使用计算流体动力学（CFD）求解器生成的，然后使用锥束几何形状模拟双平面血管造影。通过匹配对比剂位置作为双平面视图之间时间的函数来实现自校准。特征匹配用于在3D中对血管结构进行三角剖分和重建。投影数据用于改进3D估计，包括消除错误结构和椭圆拟合。使用Dice Sorensen系数评估重建的准确性，将3D重建与原始模型进行比较。所提出的极线重建方法在三个测试的动脉瘤模型中得到了很好的推广，Dice-Sorensen系数分别为0.745、0.759和0.654。错误主要是由于部分血管重叠造成的。所有三个体积的平均重建时间约为10秒。所提出的极线重建方法增强了3D可视化，解决了投影诱导血管缩短等挑战。该方法为IA可视化的复杂性提供了一种解决方案，有可能为治疗提供更准确的分析和设备尺寸。 et.al.|[2501.11793](http://arxiv.org/abs/2501.11793)|null|
|**2025-01-20**|**Multi-View Spectral Clustering for Graphs with Multiple View Structures**|尽管聚类具有根本重要性，但到目前为止，许多相关研究仍然基于模糊的基础，导致对各种聚类方法是否或如何相互联系的理解不清。在这项工作中，我们通过提出一个通用的聚类框架，包括一系列看似不同的聚类方法，包括属于广受欢迎的光谱聚类框架的各种方法，为解决此类歧义提供了额外的垫脚石。事实上，所提出的框架的通用性还能够揭示多视图图中尚未探索的领域，这些领域的每个视图可能具有不同的聚类节点。反过来，我们提出了GenClus：一种同时是该框架的实例和谱聚类的推广的方法，同时也与k-means密切相关。这为研究这种特殊类型的多视图图的少数现有方法提供了一种有原则的替代方案。然后，我们进行了深入的实验，证明GenClus在计算效率上比现有方法更高，同时也获得了类似或更好的聚类性能。最后，一个定性的现实案例研究进一步证明了GenClus产生有意义聚类的能力。 et.al.|[2501.11422](http://arxiv.org/abs/2501.11422)|null|
|**2025-01-19**|**RDG-GS: Relative Depth Guidance with Gaussian Splatting for Real-time Sparse-View 3D Rendering**|在保持精度的同时，从稀疏输入有效地合成新视图仍然是3D重建中的一个关键挑战。虽然辐射场和3D高斯散斑等先进技术在密集的视图输入中实现了渲染质量和令人印象深刻的效率，但在应用于稀疏的输入视图时，它们会出现明显的几何重建误差。此外，尽管最近的方法利用单目深度估计来增强几何学习，但它们对单视图估计深度的依赖往往导致不同视点之间的视图不一致问题。因此，这种对绝对深度的依赖可能会导致几何信息的不准确，最终影响高斯斑点场景重建的质量。本文介绍了RDG-GS，这是一种基于3D高斯散布的相对深度制导的稀疏视图3D渲染框架。核心创新在于利用相对深度引导来细化高斯场，将其转向视图一致的空间几何表示，从而能够重建精确的几何结构并捕获复杂的纹理。首先，我们设计了精细的深度先验来校正粗略估计的深度，并将全局和细粒度的场景信息插入到正则高斯模型中。在此基础上，为了解决绝对深度的空间几何不准确问题，我们通过优化深度和图像的空间相关块之间的相似性来提出相对深度制导。此外，我们还通过自适应采样直接处理难以收敛的稀疏区域，以实现快速致密化。在Mip-NeRF360、LLFF、DTU和Blender上进行的广泛实验中，RDG-GS展示了最先进的渲染质量和效率，为现实世界的应用带来了重大进步。 et.al.|[2501.11102](http://arxiv.org/abs/2501.11102)|null|
|**2025-01-19**|**Multi-View Clustering Meets High-Dimensional Mixed Data: A Fusion Regularized Method**|多视图聚类利用多个视图之间一致和互补的信息，提供比分析单视图数据更全面的见解。然而，高维混合多视图数据的异构性和冗余性对现有的聚类技术提出了重大挑战。本文提出了一种新的具有自适应组稀疏性的多视图融合正则化聚类方法，在有效捕获局部特征的同时实现了可靠的聚类。从技术上讲，对于具有不同分布的混合特征的多视图数据，考虑不同的损失或发散度量，并采用集体融合惩罚来获得公共组。此外，利用由组间稀疏性和组内稀疏性组成的非凸组稀疏性来筛选信息特征，从而增强鲁棒性。此外，我们开发了一种有效的近端交替方向乘子方法（ADMM），每个子问题都有一个闭式解。严格证明了该算法全局收敛到Karush-Kuhn-Tucker（KKT）点，同时在一定区域内建立了局部最小点和KKT点之间的等价性。在模拟和真实数据上进行的大量数值实验验证了所提出方法在聚类精度和特征选择方面的优越性能。 et.al.|[2501.10972](http://arxiv.org/abs/2501.10972)|null|
|**2025-01-18**|**PB-NBV: Efficient Projection-Based Next-Best-View Planning Framework for Reconstruction of Unknown Objects**|完全捕获物体的三维（3D）数据在工业和机器人应用中至关重要。下一最佳视图（NBV）规划的任务是根据当前数据计算下一个最佳视点，逐步实现对象的完整3D重建。然而，由于光线投射的广泛使用，许多现有的NBV规划算法会产生巨大的计算成本。具体来说，该框架根据体素结构将不同类型的体素簇重新组合成椭球体。然后，使用基于投影的视点质量评估函数结合全局划分策略从候选视图中选择下一个最佳视点。此过程取代了大量的光线投射，显著提高了计算效率。仿真环境中的对比实验表明，与其他框架相比，我们的框架以较低的计算时间实现了最高的点云覆盖率。真实世界的实验也证实了该框架的效率和可行性。我们的方法将开源，造福社区。 et.al.|[2501.10663](http://arxiv.org/abs/2501.10663)|null|
|**2025-01-17**|**Elucidating the high compliance mechanism by which the urinary bladder fills under low pressures**|膀胱在充盈过程中的高顺应性对其正常功能至关重要，使其能够以最小的透壁压升高来适应显著的体积增加。本研究旨在通过使用三种互补的成像方式分析大鼠从完全排空状态到完全膨胀的离体充盈过程，阐明这一现象背后的物理机制，而无需预处理。使用分辨率为10.8μm的高分辨率显微CT对膀胱腔进行详细的3D重建，显示在填充过程中膀胱体积增加了62倍。对整个膀胱的压力-容积研究描绘了三种机械填充状态：初始的高顺应性阶段、过渡阶段和最终的高压阶段。虽然先前的研究推测小粘膜皱襞（450μm）是高顺应性阶段的原因，但排尿膀胱圆顶的多光子显微镜（MPM）显示，大皱襞比这些皱襞大一个数量级。充气过程中的膀胱成像显示，这些大范围褶皱的扁平化是初始高顺应性阶段体积增加的原因。膀胱腔在充满和排空状态下的3D重建显示了97.13%的高排空效率。MPM成像结果表明，圆顶中的大规模褶皱通过将尿液推向膀胱出口来实现这种高排尿率。这些见解对于膀胱生物力学的计算模型和理解由于膀胱出口梗阻和与年龄相关的功能障碍等病理条件导致的膀胱功能变化至关重要。 et.al.|[2501.10312](http://arxiv.org/abs/2501.10312)|null|

<p align=right>(<a href=#updated-on-20250122>back to top</a>)</p>

## Diffusion

|Publish Date|Title|Abstract|PDF|Code|
|---|---|---|---|---|
|**2025-01-21**|**Towards Affordance-Aware Articulation Synthesis for Rigged Objects**|索具通常用于艺术家的管道中，因为它们可以灵活地适应不同的场景和姿势。然而，将装备阐明为现实的启示意识姿势（例如，遵循背景，尊重物体的物理和个性）仍然很耗时，并且严重依赖于经验丰富的艺术家的人工劳动。本文针对这一新问题，设计了A3Syn。在给定的上下文中，如环境网格和所需姿势的文本提示，A3Syn会合成从互联网上获得的任意和开放域操纵对象的关节参数。由于缺乏训练数据，这项任务极具挑战性，我们对开放域钻机没有做出任何拓扑假设。我们建议使用2D修复扩散模型和几种控制技术来合成上下文启示信息。然后，我们使用可微渲染和语义对应的组合开发了一种高效的骨骼对应对齐。A3Syn具有稳定的收敛性，在几分钟内完成，并在野外物体装备和场景的不同组合上合成了合理的启示。 et.al.|[2501.12393](http://arxiv.org/abs/2501.12393)|null|
|**2025-01-21**|**GPS as a Control Signal for Image Generation**|我们发现，照片元数据中包含的GPS标签为图像生成提供了有用的控制信号。我们训练GPS来成像模型，并将其用于需要精细理解图像在城市中如何变化的任务。特别是，我们训练了一个扩散模型来生成基于GPS和文本的图像。学习模型生成的图像捕捉了不同社区、公园和地标的独特外观。我们还通过分数蒸馏采样从2D GPS中提取3D模型到图像模型，使用GPS条件约束每个视点的重建外观。我们的评估表明，我们的GPS条件模型成功地学习了生成基于位置变化的图像，并且GPS条件改善了估计的3D结构。 et.al.|[2501.12390](http://arxiv.org/abs/2501.12390)|null|
|**2025-01-21**|**Audio Texture Manipulation by Exemplar-Based Analogy**|音频纹理操纵涉及修改声音的感知特性以实现特定的转换，例如添加、删除或替换听觉元素。本文提出了一种基于示例的音频纹理操纵类比模型。我们的方法使用成对的语音示例，而不是基于文本的指令，其中一个片段表示原始声音，另一个片段说明了所需的转换。该模型学习将相同的变换应用于新的输入，从而可以操纵声音纹理。我们构建了一个表示各种编辑任务的四元组数据集，并以自我监督的方式训练了一个潜在扩散模型。我们通过定量评估和感知研究表明，我们的模型优于文本条件基线，并可推广到现实世界、非分布和非语音场景。项目页面：https://berkeley-speech-group.github.io/audio-texture-analogy/ et.al.|[2501.12385](http://arxiv.org/abs/2501.12385)|null|
|**2025-01-21**|**DiffDoctor: Diagnosing Image Diffusion Models Before Treating**|尽管最近取得了进展，但图像扩散模型仍然会产生伪影。一种常见的解决方案是使用质量评估系统来完善已建立的模型，该系统通常对图像的整体进行评级。在这项工作中，我们认为问题的解决始于识别，这就要求模型不仅要意识到图像中缺陷的存在，还要意识到它们的具体位置。受此启发，我们提出了DiffDoctor，这是一个两阶段流水线，可以帮助图像扩散模型生成更少的伪影。具体来说，第一阶段的目标是开发一个强大的伪影检测器，为此，我们收集了超过100万个有缺陷的合成图像的数据集，并建立了一个高效的人在环注释过程，结合了精心设计的类平衡策略。然后，学习伪影检测器参与第二阶段，通过为每次合成分配每像素的置信度图来调整扩散模型。对文本到图像扩散模型的广泛实验证明了我们的伪影检测器的有效性以及我们的诊断然后治疗设计的合理性。 et.al.|[2501.12382](http://arxiv.org/abs/2501.12382)|null|
|**2025-01-21**|**Diffusion-aware Censored Gaussian Processes for Demand Modelling**|由于可用供应有限，从汇总数据推断对产品或服务的真实需求往往具有挑战性，从而导致观察结果被审查并与实际需求相对应，从而无法解释未满足的需求。审查回归模型能够解释由于供应有限而进行审查的影响，但它们没有考虑替代的影响，这可能会导致对类似替代产品或服务的需求增加。本文提出了扩散感知的审查需求模型，该模型将Tobit似然与图扩散过程相结合，以模拟类似产品或服务之间未满足需求转移的潜在过程。我们在GP框架下实例化了这类新模型，并基于用于建模销售、共享单车需求和电动汽车充电需求的模拟和现实数据，展示了其更好地恢复真实需求并产生更准确的样本外预测的能力。 et.al.|[2501.12354](http://arxiv.org/abs/2501.12354)|null|
|**2025-01-21**|**Decoherence of Schrödinger cat states in light of wave/particle duality**|我们质疑将薛定谔猫态解绑为服从Lindblad主方程的系综平均值的标准图像，这是由与环境的不可逆相互作用在局部引起的。我们生成了与特定环境记录相关的纯系统态的自洽集合，对应于Carmichael等人[Phys.Rev.Lett.851855（2000）]首次引入的波粒相关器的功能。本着Carmichael等[Coherent states:Past，Present and Future，pp.75-91，World Scientific（1994）]的精神，我们发现，当“位置”测量了阻尼腔模（一个显式开放的量子系统）的“动量”。强度场相关性可能在很大程度上偏离单调衰减，而腔态的维格纳函数在以光子计数采样连续光电流为条件时显示出量子干涉的对比表现。反过来，条件光电探测事件标志着零差探测器产生的净电荷和谐振器中电磁场振幅的上下文扩散。 et.al.|[2501.12328](http://arxiv.org/abs/2501.12328)|null|
|**2025-01-21**|**The Rouse ring chain with attractive harmonic potential of spherical symmetry**|我们研究了通过包含一个有效的、球对称的、熵性质的吸引势来修改的循环劳斯链的静态和动态性质，该势是环质心的位置向量，是具有n个数的链段的位置向量。它是玻尔兹曼常数乘以绝对温度的乘积，是势的一个参数，其平方与势的强度成反比。结果表明，非常弱的势，N是聚合物环中库恩链段的数量，b是库恩链长，导致聚合物链的剧烈压缩，其惯性半径与自由尺寸相比变得小得多。有序势参数的值是熔体中库恩节段的浓度，聚合物环的本征链段的浓度变得有序，聚合物环的状态可以被视为球形。聚合物环的末端弛豫时间约为在此期间大分子质心的均方位移，这可能导致聚合物链段在进入正常扩散运动模式之前均方位移的时间依赖性出现伪平台。 et.al.|[2501.12324](http://arxiv.org/abs/2501.12324)|null|
|**2025-01-21**|**Regressor-Guided Image Editing Regulates Emotional Response to Reduce Online Engagement**|众所周知，情绪会调节用户的内容消费与在线参与度之间的关系，情绪强度的提高会导致参与度的提高。基于这一认识，我们提出了三种回归器引导的图像编辑方法，旨在减少图像的情感影响。其中包括（i）基于已知影响情绪的全局图像变换的参数优化方法，（ii）针对生成对抗网络的风格潜在空间的优化方法，以及（iii）采用分类器引导和无分类器引导的基于扩散的方法。我们的研究结果表明，这些方法可以有效地改变图像的情感特性，同时保持高视觉质量。基于优化的方法主要调整色调和亮度等低级属性，而基于扩散的方法引入了语义变化，如改变外观或面部表情。值得注意的是，一项行为研究的结果表明，只有基于扩散的方法才能成功地引发观众情绪反应的变化，同时保持高感知图像质量。在未来的工作中，我们将研究这些图像适应对互联网用户行为的影响。 et.al.|[2501.12289](http://arxiv.org/abs/2501.12289)|null|
|**2025-01-21**|**Dynamic Metal-Support Interaction Dictates Cu Nanoparticle Sintering on Al $_2$O$_3$ Surfaces**|纳米颗粒烧结仍然是多相催化中的一个关键挑战。在这项工作中，我们提出了三个Al$_2$O$_3$表面（$\gamma$-Al$_2$O'_3$（100）、$\gamma$-Al$_2$O$_3$（110）和$\alpha$-Al$_2$O$O_3$（0001））上铜纳米粒子的统一深势（DP）模型。使用DP加速模拟，我们揭示了三个表面上引人注目的小面依赖性纳米粒子稳定性和迁移率模式。在800 K下，纳米颗粒在$\alpha$-Al$_2$O$_3$（0001）上的扩散速度比在$\gamma$-Al$_2$O$_3$（100）上快几倍，而基于它们在0 K下的较大结合能，预计会更加缓慢。动态金属-支撑相互作用（MSI）促进了扩散，其中Al原子切换出表面平面以优化与纳米颗粒的接触，并在纳米颗粒移动时松弛回到平面。相比之下，$\gamma$-Al$_2$O$_3$（100）和$\gamma$-Al$_2$O$_3$（110）上的MSI主要由更稳定和定向的Cu-O键主导，这与在这些表面上观察到的有限扩散相一致。我们延长的长期MD模拟为烧结过程提供了定量的见解，表明纳米粒子的分散性（纳米粒子之间的初始距离）强烈影响纳米粒子扩散驱动的聚结。我们观察到，即使初始纳米颗粒间距离增加到30\r{a}，Cu$_{13}$纳米颗粒在800K下也可以在短时间内（10ns）在$\alpha$-Al$_2$O$_3$（0001）上发生聚结，而通过将初始纳米颗粒之间距离从15\r{a}增加到30\ r{a｝，可以显著抑制$\gamma$-Al$_2$O$_3$ （100）上的聚结。这些发现表明，支撑表面的动力学对于理解烧结机理至关重要，并通过设计支撑形态为设计耐烧结催化剂提供指导。 et.al.|[2501.12283](http://arxiv.org/abs/2501.12283)|null|
|**2025-01-21**|**VipDiff: Towards Coherent and Diverse Video Inpainting via Training-free Denoising Diffusion Models**|最近的视频修复方法通过利用光流在图像空间或特征空间中引导像素从参考帧传播，取得了令人鼓舞的改进。然而，当掩模区域太大并且无法找到中心的像素对应关系时，它们会在掩模中心产生严重的伪影。最近，扩散模型在生成多样化和高质量的图像方面表现出了令人印象深刻的性能，并在许多图像修复作品中得到了利用。然而，这些方法不能直接应用于视频，以产生时间连贯的修复结果。在本文中，我们提出了一个名为VipDiff的无训练框架，用于在反向扩散过程中调节扩散模型，以产生时间连贯的修复结果，而不需要任何训练数据或微调预训练的扩散模型。VipDiff以光流为指导，从参考帧中提取有效像素，作为优化随机采样高斯噪声的约束，并将生成的结果用于进一步的像素传播和条件生成。VipDiff还允许在不同的采样噪声上生成不同的视频修复结果。实验表明，VipDiff在时空一致性和保真度方面都可以大大优于最先进的视频修复方法。 et.al.|[2501.12267](http://arxiv.org/abs/2501.12267)|null|

<p align=right>(<a href=#updated-on-20250122>back to top</a>)</p>

## NeRF

|Publish Date|Title|Abstract|PDF|Code|
|---|---|---|---|---|
|**2025-01-15**|**CityDreamer4D: Compositional Generative Model of Unbounded 4D Cities**|近年来，3D场景生成引起了越来越多的关注，并取得了重大进展。生成4D城市比3D场景更具挑战性，因为存在结构复杂、视觉多样的物体，如建筑物和车辆，并且人类对城市环境中的扭曲更加敏感。为了解决这些问题，我们提出了CityDreamer4D，这是一个专门为生成无界4D城市而定制的组合生成模型。我们的主要见解是1）4D城市生成应该将动态对象（如车辆）与静态场景（如建筑物和道路）分开，2）4D场景中的所有对象都应该由建筑物、车辆和背景材料的不同类型的神经场组成。具体来说，我们提出了交通场景生成器和无边界布局生成器，使用高度紧凑的BEV表示生成动态交通场景和静态城市布局。4D城市中的对象是通过结合面向对象和面向实例的神经场来生成的，用于背景材料、建筑物和车辆。为了适应背景材料和实例的不同特征，神经场采用定制的生成哈希网格和周期性位置嵌入作为场景参数化。此外，我们还为城市生成提供了一套全面的数据集，包括OSM、GoogleEarth和CityTopia。OSM数据集提供了各种真实世界的城市布局，而谷歌地球和CityTopia数据集则提供了大规模、高质量的城市图像，并附有3D实例注释。利用其组合设计，CityDreamer4D支持一系列下游应用程序，如实例编辑、城市风格化和城市模拟，同时在生成逼真的4D城市方面提供最先进的性能。 et.al.|[2501.08983](http://arxiv.org/abs/2501.08983)|**[link](https://github.com/hzxie/CityDreamer4D)**|
|**2025-01-15**|**Score-based 3D molecule generation with neural fields**|我们介绍了一种基于连续原子密度场的3D分子的新表示方法。使用这种表示法，我们提出了一种基于步跳采样的新模型，用于使用神经场在连续空间中无条件生成3D分子。我们的模型FuncMol使用条件神经场将分子场编码为潜码，使用Langevin MCMC从高斯平滑分布中采样噪声码（walk），在一步中对这些样本进行去噪（jump），最后将它们解码为分子场。与大多数方法不同，FuncMol可以在不假设分子结构的情况下进行3D分子的全原子生成，并且可以很好地与分子的大小进行缩放。我们的方法在类药物分子上取得了具有竞争力的结果，并且很容易扩展到大环肽，采样速度至少快一个数量级。该代码可在以下网址获得https://github.com/prescient-design/funcmol. et.al.|[2501.08508](http://arxiv.org/abs/2501.08508)|**[link](https://github.com/prescient-design/funcmol)**|
|**2025-01-10**|**Nonlinear partial differential equations in neuroscience: from modelling to mathematical theory**|许多偏微分方程组已被提出作为大型神经元网络中复杂集体行为的简化表示。在这项调查中，我们简要讨论了它们的推导，然后回顾了为处理这些模型的独特特征而开发的数学方法，这些模型通常是非线性和非局部的。第一部分重点介绍抛物型福克-普朗克方程：非线性噪声泄漏积分和火神经元模型，PDE形式的随机神经场及其在网格单元中的应用，以及基于速率的决策模型。第二部分涉及双曲线输运方程，即自上次排放以来经过的时间模型和基于跳跃的泄漏积分和火灾模型。最后一部分介绍了一些动力学介观模型，特别关注动力学电压电导模型和FitzHugh-Nagumo动力学福克-普朗克系统。 et.al.|[2501.06015](http://arxiv.org/abs/2501.06015)|null|
|**2025-01-10**|**Locality-aware Gaussian Compression for Fast and High-quality Rendering**|我们提出了LocoGS，这是一种局部感知的3D高斯散斑（3DGS）框架，它利用3D高斯的空间相干性对体积场景进行紧凑建模。为此，我们首先分析了3D高斯属性的局部相干性，并提出了一种新的局部感知3D高斯表示，该表示使用具有最小存储要求的神经场表示对局部相干高斯属性进行有效编码。除了新颖的表示方法外，LocoGS还经过精心设计，添加了密集初始化、自适应球面谐波带宽方案和针对不同高斯属性的不同编码方案等附加组件，以最大限度地提高压缩性能。实验结果表明，对于代表性的真实世界3D数据集，我们的方法优于现有的紧凑高斯表示的渲染质量，同时实现了从54.6美元到96.6美元的压缩存储大小，以及从2.1美元到2.4美元的渲染速度。甚至我们的方法也证明了平均渲染速度比最先进的压缩方法高2.4倍，具有相当的压缩性能。 et.al.|[2501.05757](http://arxiv.org/abs/2501.05757)|null|
|**2025-01-08**|**KN-LIO: Geometric Kinematics and Neural Field Coupled LiDAR-Inertial Odometry**|激光雷达惯性测距（LIO）的最新进展推动了大量应用。然而，传统的LIO系统往往更侧重于定位而不是映射，映射主要由稀疏的几何元素组成，这对于下游任务来说并不理想。最近新兴的神经场技术在密集测绘方面具有巨大的潜力，但纯激光雷达测绘很难在高动态车辆上进行。为了缓解这一挑战，我们提出了一种新的解决方案，将几何运动学与神经场紧密耦合，以增强同时状态估计和密集映射能力。我们提出了半耦合和紧耦合的运动学神经LIO（KN-LIO）系统，该系统利用在线SDF解码和迭代误差状态卡尔曼滤波来融合激光和惯性数据。我们的KN-LIO最大限度地减少了信息丢失，提高了状态估计的准确性，同时也适应了异步多LiDAR输入。对各种高动态数据集的评估表明，我们的KN-LIO在姿态估计方面的性能与现有最先进的解决方案相当或更优，并且与纯基于LiDAR的方法相比，提供了更高的密集映射精度。相关代码和数据集将在https://**上提供。 et.al.|[2501.04263](http://arxiv.org/abs/2501.04263)|null|
|**2025-01-06**|**NeuroPMD: Neural Fields for Density Estimation on Product Manifolds**|我们提出了一种新的深度神经网络方法，用于在乘积黎曼流形域上进行密度估计。在我们的方法中，网络直接参数化未知密度函数，并使用惩罚最大似然框架进行训练，惩罚项使用流形微分算子形成。网络架构和估计算法经过精心设计，以应对高维积流形域的挑战，有效地减轻了限制传统核和基展开估计器的维数灾难，并克服了非专用神经网络方法遇到的收敛问题。广泛的模拟和对大脑结构连接数据的实际应用突显了我们的方法相对于竞争对手的明显优势。 et.al.|[2501.02994](http://arxiv.org/abs/2501.02994)|**[link](https://github.com/will-consagra/neuropmd)**|
|**2025-01-03**|**Fusion DeepONet: A Data-Efficient Neural Operator for Geometry-Dependent Hypersonic Flows on Arbitrary Grids**|设计再入飞行器需要准确预测其几何形状周围的高超音速流动。对这种流动的快速预测可以彻底改变车辆设计，特别是对于变形几何形状。我们评估了先进的神经算子模型，如深度算子网络（DeepONet）、参数条件U-Net、傅里叶神经算子（FNO）和MeshGraphNet，目的是解决在有限数据下学习依赖几何的高超音速流场的挑战。具体来说，我们比较了两种网格类型的这些模型的性能：均匀笛卡尔网格和不规则网格。为了训练这些模型，我们使用36个独特的椭圆几何体，使用高阶熵稳定的DGSEM求解器生成高保真模拟，强调了使用稀缺数据集的挑战。我们评估并比较了四种基于算子的模型在预测椭圆体周围高超音速流场方面的有效性。此外，我们开发了一个名为Fusion DeepONet的新框架，该框架利用了神经场概念，并在不同的几何结构中有效地进行了推广。尽管训练数据稀缺，Fusion DeepONet在均匀网格上的性能与参数条件U-Net相当，而在不规则、任意网格上的表现优于MeshGraphNet和vanilla DeepONnet。与U-Net、MeshGraphNet和FNO相比，Fusion DeepONet需要更少的可训练参数，使其计算效率更高。我们还使用奇异值分解分析了Fusion DeepONet模型的基函数。该分析表明，Fusion DeepONet能够有效地推广到看不见的解决方案，并适应不同的几何形状和网格点，证明了其在训练数据有限的情况下的鲁棒性。 et.al.|[2501.01934](http://arxiv.org/abs/2501.01934)|null|
|**2024-12-30**|**Hierarchical Pose Estimation and Mapping with Multi-Scale Neural Feature Fields**|机器人应用需要对场景有全面的了解。近年来，基于神经场的参数化整个环境的方法已经变得流行。由于其连续性和学习场景先验的能力，这些方法很有前景。然而，当处理未知的传感器姿态和连续测量时，在机器人中使用神经场变得具有挑战性。本文主要研究大规模神经隐式SLAM的传感器姿态估计问题。我们从概率的角度研究了隐式映射，并提出了具有相应神经网络架构的分层姿态估计。我们的方法非常适合大规模隐式映射表示。所提出的方法在连续的室外LiDAR扫描上运行，实现了精确的姿态估计，同时保持了短轨迹和长轨迹的稳定映射质量。我们在适合大规模重建的结构化稀疏隐式表示上构建了我们的方法，并使用KITTI和MaiCity数据集对其进行了评估。我们的方法在未知姿态的映射方面优于基线，并实现了最先进的定位精度。 et.al.|[2412.20976](http://arxiv.org/abs/2412.20976)|null|
|**2024-12-26**|**Humans as a Calibration Pattern: Dynamic 3D Scene Reconstruction from Unsynchronized and Uncalibrated Videos**|最近关于动态神经场重建的工作假设输入来自具有已知姿势的同步多视图视频。这些输入约束在现实世界的设置中经常得不到满足，使得这种方法不切实际。我们证明，如果视频捕捉到人体运动，则姿态未知的非同步视频可以生成动态神经场。人类是最常见的动态主体之一，其姿势可以使用最先进的方法进行估计。在有噪声的情况下，估计的人体形状和姿态参数为训练一致的动态神经表示的高度非凸和欠约束问题提供了一个不错的初始化。给定人类的姿势和形状序列，我们估计视频之间的时间偏移，然后通过分析3D关节位置进行相机姿势估计。然后，我们使用多分辨率脊训练动态NeRF，同时细化时间偏移和相机姿态。该设置仍然涉及优化许多参数，因此，我们引入了一种鲁棒的渐进学习策略来稳定该过程。实验表明，我们的方法在具有挑战性的条件下实现了精确的时空校准和高质量的场景重建。 et.al.|[2412.19089](http://arxiv.org/abs/2412.19089)|null|
|**2024-12-29**|**PartGen: Part-level 3D Generation and Reconstruction with Multi-View Diffusion Models**|文本或图像到3D生成器和3D扫描仪现在可以生成具有高质量形状和纹理的3D资产。这些资产通常由一个单一的融合表示组成，如隐式神经场、高斯混合或网格，没有任何有用的结构。然而，大多数应用程序和创意工作流程都要求资产由几个可以独立操作的有意义的部分组成。为了解决这一差距，我们引入了PartGen，这是一种新颖的方法，可以从文本、图像或非结构化3D对象生成由有意义的部分组成的3D对象。首先，给定生成或渲染的3D对象的多个视图，多视图扩散模型提取一组合理且视图一致的零件分割，将对象划分为零件。然后，第二个多视图扩散模型分别获取每个部分，填充遮挡，并通过将这些完成的视图馈送到3D重建网络来使用它们进行3D重建。这个完成过程考虑了整个对象的上下文，以确保各部分紧密结合。生成完成模型可以弥补因遮挡而丢失的信息；在极端情况下，它可以根据输入的3D资源产生完全不可见的部分的幻觉。我们在生成的和真实的3D资产上评估了我们的方法，并表明它在很大程度上优于分割和零件提取基线。我们还展示了3D零件编辑等下游应用程序。 et.al.|[2412.18608](http://arxiv.org/abs/2412.18608)|null|

<p align=right>(<a href=#updated-on-20250122>back to top</a>)</p>

[contributors-shield]: https://img.shields.io/github/contributors/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[contributors-url]: https://github.com/Vincentqyw/cv-arxiv-daily/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[forks-url]: https://github.com/Vincentqyw/cv-arxiv-daily/network/members
[stars-shield]: https://img.shields.io/github/stars/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[stars-url]: https://github.com/Vincentqyw/cv-arxiv-daily/stargazers
[issues-shield]: https://img.shields.io/github/issues/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[issues-url]: https://github.com/Vincentqyw/cv-arxiv-daily/issues

