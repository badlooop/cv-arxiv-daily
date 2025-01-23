[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]

## Updated on 2025.01.23
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
|**2025-01-22**|**DWTNeRF: Boosting Few-shot Neural Radiance Fields via Discrete Wavelet Transform**|神经辐射场（NeRF）在新颖的视图合成和3D场景表示方面取得了卓越的性能，但其实际应用受到收敛缓慢和依赖密集训练视图的阻碍。为此，我们提出了DWTNeRF，这是一个基于Instant NGP快速训练哈希编码的统一框架。它与为少镜头NeRF设计的正则化项相结合，后者在稀疏训练视图上运行。我们的DWTNeRF包括一种新颖的离散小波损耗，允许在训练目标中直接对低频进行显式优先级排序，从而减少早期训练阶段少数镜头NeRF对高频的过拟合。我们还引入了一种基于模型的方法，该方法基于多头注意力，与基于INGP的模型兼容，这些模型对架构变化很敏感。在3-shot LLFF基准测试中，DWTNeRF的PSNR、SSIM和LPIPS分别比Vanilla NeRF高出15.07%、24.45%和36.30%。我们的方法鼓励重新思考基于INGP模型的当前少镜头方法。 et.al.|[2501.12637](http://arxiv.org/abs/2501.12637)|null|
|**2025-01-22**|**HAC++: Towards 100X Compression of 3D Gaussian Splatting**|3D高斯散斑（3DGS）已成为一种有前景的新型视图合成框架，具有快速渲染速度和高保真度。然而，大量的高斯分布及其相关属性需要有效的压缩技术。然而，高斯点云（或我们论文中的锚点）的稀疏性和无组织性给压缩带来了挑战。为了实现紧凑的大小，我们提出了HAC++，它利用了无组织锚点和结构化哈希网格之间的关系，利用它们的互信息进行上下文建模。此外，HAC++捕获锚点内的上下文关系，以进一步提高压缩性能。为了促进熵编码，我们利用高斯分布来精确估计每个量化属性的概率，其中提出了一种自适应量化模块来实现这些属性的高精度量化，以提高保真度恢复。此外，我们采用了一种自适应掩蔽策略来消除无效的高斯分布和锚点。总体而言，与vanilla 3DGS相比，HAC++在所有数据集上平均时实现了超过100倍的显著尺寸减小，同时提高了保真度。与脚手架GS相比，它还可以减少20倍以上的尺寸。我们的代码可在https://github.com/YihangChen-ee/HAC-plus. et.al.|[2501.12255](http://arxiv.org/abs/2501.12255)|**[link](https://github.com/yihangchen-ee/hac-plus)**|
|**2025-01-21**|**Survey on Monocular Metric Depth Estimation**|单目深度估计（MDE）是一项基本的计算机视觉任务，支撑着空间理解、3D重建和自动驾驶等应用。虽然基于深度学习的MDE方法可以从单个图像中预测相对深度，但它们缺乏度量尺度信息通常会导致尺度不一致，限制了它们在视觉SLAM、3D重建和新颖视图合成等下游任务中的实用性。单目度量深度估计（MMDE）通过实现精确的场景级深度推断来解决这些挑战。MMDE提高了深度一致性，增强了顺序任务的稳定性，简化了与下游应用程序的集成，并拓宽了实际用例。本文对深度估计技术进行了全面的回顾，重点介绍了从基于几何的方法到最先进的深度学习方法的演变。它强调了标度不可知方法的进步，这对于实现零样本泛化作为MMDE的基础能力至关重要。探讨了零样本MMDE研究的最新进展，重点讨论了模型泛化和场景边界细节丢失等挑战。解决这些问题的创新策略包括无标签数据增强、图像修补、架构优化和生成技术。详细分析后，这些进步表明了对克服现有局限性的重大贡献。最后，本文综合了零样本MMDE的最新发展，确定了尚未解决的挑战，并概述了未来的研究方向。通过提供清晰的路线图和前沿的见解，这项工作旨在加深对MMDE的理解，激发新的应用，并推动技术创新。 et.al.|[2501.11841](http://arxiv.org/abs/2501.11841)|null|
|**2025-01-20**|**See In Detail: Enhancing Sparse-view 3D Gaussian Splatting with Local Depth and Semantic Regularization**|3D高斯散斑（3DGS）在新颖的视图合成中表现出了显著的性能。然而，当输入视图稀疏时，其渲染质量会下降，导致内容失真和细节减少。这种限制阻碍了它的实际应用。为了解决这个问题，我们提出了一种稀疏视图3DGS方法。鉴于稀疏视图渲染固有的不适定性，整合先验信息至关重要。我们提出了一种语义正则化技术，使用从预训练的DINO-ViT模型中提取的特征来确保多视图语义的一致性。此外，我们提出了局部深度正则化，它约束深度值以提高对看不见的视图的泛化能力。我们的方法优于最先进的新颖视图合成方法，在LLFF数据集上实现了高达0.4dB的PSNR改善，同时减少了失真并提高了视觉质量。 et.al.|[2501.11508](http://arxiv.org/abs/2501.11508)|null|
|**2025-01-18**|**Decoupling Appearance Variations with 3D Consistent Features in Gaussian Splatting**|高斯散斑已成为新颖视图合成中一种突出的3D表示，但它仍然存在外观变化，这是由各种因素引起的，如现代相机ISP、一天中的不同时间、天气条件和局部光线变化。这些变化可能会导致渲染图像/视频中的浮动和颜色失真。高斯散斑中最近的外观建模方法要么与渲染过程紧密耦合，阻碍了实时渲染，要么只考虑了轻微的全局变化，在局部光线变化的场景中表现不佳。在本文中，我们提出了DAVIGS，这是一种以即插即用和高效的方式解耦外观变化的方法。通过在图像级别而不是高斯级别转换渲染结果，我们的方法可以在最小的优化时间和内存开销下对外观变化进行建模。此外，我们的方法在3D空间中收集与外观相关的信息来转换渲染图像，从而隐式地建立视图之间的3D一致性。我们在几个外观变体场景上验证了我们的方法，并证明它在不影响渲染速度的情况下，以最少的训练时间和内存使用实现了最先进的渲染质量。此外，它以即插即用的方式为不同的高斯散斑基线提供了性能改进。 et.al.|[2501.10788](http://arxiv.org/abs/2501.10788)|null|
|**2025-01-16**|**CrossModalityDiffusion: Multi-Modal Novel View Synthesis with Unified Intermediate Representation**|地理空间成像利用了来自各种传感方式的数据，如地球观测、合成孔径雷达和激光雷达，从地面无人机到卫星视图。这些异构输入为场景理解提供了重要机会，但在准确解释几何体方面存在挑战，特别是在缺乏精确地面实况数据的情况下。为了解决这个问题，我们提出了CrossModalityDiffusion，这是一个模块化框架，旨在在没有场景几何先验知识的情况下生成不同模态和视点的图像。CrossModalityDiffusion采用特定于模态的编码器，这些编码器拍摄多个输入图像并产生几何感知特征体，这些特征体对相对于其输入相机位置的场景结构进行编码。放置特征体积的空间是统一输入模式的共同基础。这些特征体被重叠，并使用体绘制技术从新的角度渲染成特征图像。渲染的特征图像被用作特定模态扩散模型的调节输入，从而能够合成所需输出模态的新图像。在本文中，我们证明了联合训练不同的模块可以确保框架内所有模态的一致几何理解。我们在合成ShapeNet汽车数据集上验证了CrossModalityDiffusion的能力，证明了它在跨多种成像模态和视角生成准确一致的新视图方面的有效性。 et.al.|[2501.09838](http://arxiv.org/abs/2501.09838)|null|
|**2025-01-14**|**3D Gaussian Splatting with Normal Information for Mesh Extraction and Improved Rendering**|可区分的3D高斯飞溅已成为一种高效灵活的渲染技术，用于从2D视图集合中表示复杂场景，并实现高质量的实时新颖视图合成。然而，它对光度损失的依赖可能会导致重建的几何结构和提取的网格不精确，特别是在具有高曲率或精细细节的区域。我们提出了一种新的正则化方法，该方法使用从高斯估计的带符号距离函数的梯度来提高渲染质量，同时提取表面网格。规范化的常规监督有助于更好的渲染和网格重建，这对于视频生成、动画、AR-VR和游戏中的下游应用至关重要。我们展示了我们的方法在Mip-NeRF360、坦克和神庙以及深度混合等数据集上的有效性。与其他网格提取渲染方法相比，我们的方法在真实感度量上得分更高，而不会影响网格质量。 et.al.|[2501.08370](http://arxiv.org/abs/2501.08370)|null|
|**2025-01-14**|**VINGS-Mono: Visual-Inertial Gaussian Splatting Monocular SLAM in Large Scenes**|VINGS Mono是一个专为大型场景设计的单目（惯性）高斯散斑（GS）SLAM框架。该框架由四个主要组件组成：VIO前端、2D高斯映射、NVS环路闭合和动态擦除器。在VIO前端中，RGB帧通过密集束调整和不确定性估计进行处理，以提取场景几何形状和姿态。基于该输出，映射模块递增地构建和维护2D高斯映射。2D高斯映射的关键组件包括基于样本的光栅化器、分数管理器和姿态细化，它们共同提高了映射速度和定位精度。这使得SLAM系统能够处理多达5000万个高斯椭球的大规模城市环境。为了确保大规模场景中的全局一致性，我们设计了一个环路闭合模块，该模块创新性地利用高斯散点的新颖视图合成（NVS）功能进行环路闭合检测和高斯图的校正。此外，我们提出了一种动态橡皮擦，以解决现实世界户外场景中动态对象不可避免的存在问题。在室内和室外环境中进行的广泛评估表明，我们的方法实现了与视觉惯性里程表相当的定位性能，同时超越了最近的GS/NeRF SLAM方法。在映射和渲染质量方面，它也明显优于所有现有方法。此外，我们开发了一款移动应用程序，并验证了我们的框架可以仅使用智能手机摄像头和低频IMU传感器实时生成高质量的高斯地图。据我们所知，VINGS Mono是第一种能够在室外环境中运行并支持公里级大型场景的单目高斯SLAM方法。 et.al.|[2501.08286](http://arxiv.org/abs/2501.08286)|null|
|**2025-01-13**|**Evaluating Human Perception of Novel View Synthesis: Subjective Quality Assessment of Gaussian Splatting and NeRF in Dynamic Scenes**|高斯散斑（GS）和神经辐射场（NeRF）是两项突破性的技术，它们彻底改变了新视图合成（NVS）领域，通过从一组稀疏视图的图像中合成多个视点，实现了沉浸式真实感渲染和用户体验。NVS的潜在应用，如高质量的虚拟和增强现实、详细的3D建模和逼真的医学器官成像，强调了从人类感知的角度对NVS方法进行质量评估的重要性。尽管之前的一些研究已经探索了NVS技术的主观质量评估，但它们仍然面临着一些挑战，特别是在NVS方法选择、场景覆盖和评估方法方面。为了应对这些挑战，我们进行了两个主观实验，对NVS技术进行质量评估，包括基于GS和基于NeRF的方法，重点关注动态和现实世界的场景。本研究涵盖了360度、正面和单视点视频，同时提供了更丰富、更多的真实场景。同时，这是首次探索NVS方法在具有运动物体的动态场景中的影响。这两种主观实验有助于从人类感知的角度充分理解不同观察路径的影响，并为未来开发全参考和无参考质量指标铺平道路。此外，我们在拟议的数据库上建立了各种最先进的客观指标的综合基准，强调现有方法仍然难以准确捕捉主观质量。这些结果让我们对现有NVS方法的局限性有了一些了解，并可能促进新NVS方法发展。 et.al.|[2501.08072](http://arxiv.org/abs/2501.08072)|null|
|**2025-01-13**|**Motion Tracks: A Unified Representation for Human-Robot Transfer in Few-Shot Imitation Learning**|教机器人自主完成日常任务仍然是一个挑战。模仿学习（IL）是一种强大的方法，通过演示向机器人灌输技能，但受到收集远程操作机器人数据的劳动密集型过程的限制。人类视频提供了一种可扩展的替代方案，但由于缺乏机器人动作标签，仍然很难直接从中训练IL策略。为了解决这个问题，我们建议将动作表示为图像上的短程2D轨迹。这些动作或运动轨迹捕捉人手或机器人末端执行器的预测运动方向。我们实例化了一个名为运动轨迹策略（MT-pi）的IL策略，该策略接收图像观测值并将运动轨迹作为动作输出。通过利用这种统一的跨实施例动作空间，MT-pi在只需几分钟的人类视频和有限的额外机器人演示的情况下，就可以成功完成任务。在测试时，我们从两个相机视图预测运动轨迹，通过多视图合成恢复6DoF轨迹。MT pi在4个现实世界任务中的平均成功率为86.5%，比不利用人类数据或我们的动作空间的最先进的IL基线高出40%，并推广到仅在人类视频中看到的场景。代码和视频可在我们的网站上找到https://portal-cornell.github.io/motion_track_policy/. et.al.|[2501.06994](http://arxiv.org/abs/2501.06994)|null|

<p align=right>(<a href=#updated-on-20250123>back to top</a>)</p>

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

<p align=right>(<a href=#updated-on-20250123>back to top</a>)</p>

## Diffusion

|Publish Date|Title|Abstract|PDF|Code|
|---|---|---|---|---|
|**2025-01-22**|**Accelerate High-Quality Diffusion Models with Inner Loop Feedback**|我们提出了内环反馈（ILF），这是一种加速扩散模型推理的新方法。ILF训练一个轻量级模块，通过在给定时间步长利用所选扩散骨干块的输出来预测去噪过程中的未来特征。这种方法利用了两个关键的直觉；（1） 给定块在相邻时间步的输出是相似的，并且（2）对一个步骤执行部分计算比完全跳过该步骤给模型带来的负担更小。我们的方法非常灵活，因为我们发现反馈模块本身可以简单地成为扩散主干的一个块，所有设置都被复制。它对正向扩散的影响可以通过从零初始化开始学习的缩放因子来缓和。我们使用蒸馏损失来训练这个模块；然而，与之前的一些工作不同，在之前的工作中，完全扩散的主干充当学生，我们的模型冻结了主干，只训练反馈模块。虽然许多优化扩散模型的努力都集中在极少数步骤（1-4步）内实现可接受的图像质量，但我们的重点是匹配最佳情况结果（通常在20步内实现），同时显著减少运行时间。ILF有效地实现了这种平衡，在使用扩散变换器（DiT）进行类到图像生成和使用基于DiT的PixArt alpha和PixArt sigma进行文本到图像生成方面都表现出了强大的性能。ILF 1.7x-1.8x加速的质量通过FID、CLIP评分、CLIP图像质量评估、ImageReward和定性比较得到证实。 et.al.|[2501.13107](http://arxiv.org/abs/2501.13107)|null|
|**2025-01-22**|**Robust Representation Consistency Model via Contrastive Denoising**|鲁棒性对于深度神经网络至关重要，特别是在安全敏感的应用中。为此，随机平滑为证明对抗扰动的鲁棒性提供了理论保证。最近，扩散模型已成功用于随机平滑，以在使用标准分类器进行预测之前净化噪声扰动样本。虽然这些方法在小扰动半径方面表现出色，但与经典方法相比，它们在较大的扰动下很难处理，并且在推理过程中会产生大量的计算开销。为了解决这个问题，我们将像素空间中沿扩散轨迹的生成建模任务重新表述为潜在空间中的判别任务。具体来说，我们使用实例判别来通过对齐时间上相邻的点来实现沿轨迹的一致表示。在基于学习到的表示进行微调后，我们的模型通过单一预测实现了隐式去噪和分类，大大降低了推理成本。我们在各种数据集上进行了广泛的实验，并在推理过程中以最小的计算预算实现了最先进的性能。例如，我们的方法在所有扰动半径上比ImageNet上基于扩散的方法的认证精度平均高出5.3%，在更大的半径上高达11.6%，同时平均降低了85美元的推理成本。代码可在以下网址获得：https://github.com/jiachenlei/rRCM. et.al.|[2501.13094](http://arxiv.org/abs/2501.13094)|**[link](https://github.com/jiachenlei/rrcm)**|
|**2025-01-22**|**Orchid: Image Latent Diffusion for Joint Appearance and Geometry Generation**|扩散模型是图像生成的最先进技术。他们在大型数据集上接受训练，捕捉到用于修复、深度和（表面）法线预测等任务的富有表现力的图像先验。然而，这些模型通常针对一个特定任务进行训练，例如，为颜色、深度和正常预测中的每一个单独建模。这些模型没有利用外观和几何形状之间的内在相关性，通常会导致不一致的预测。在这篇论文中，我们提出了一种新的图像扩散先验，它联合编码了外观和几何形状。我们引入了一个扩散模型Orchid，它包括一个变分自编码器（VAE），用于对潜在空间的颜色、深度和表面法线进行编码，以及一个潜在扩散模型（LDM），用于生成这些联合潜伏。Orchid直接从用户提供的文本生成照片级逼真的彩色图像、相对深度和表面法线，可用于无缝创建图像对齐的部分3D场景。它还可以执行图像条件任务，如联合单眼深度和法线预测，并且在精度上与仅为这些任务设计的最先进方法相媲美。最后，我们的模型学习了一个关节先验，该先验可以用作纠缠外观和几何的许多逆问题的正则化子。例如，我们展示了它在颜色深度法线修复中的有效性，展示了它对从稀疏视图生成3D问题的适用性。 et.al.|[2501.13087](http://arxiv.org/abs/2501.13087)|null|
|**2025-01-22**|**A new cutoff criterion for non-negatively curved chains**|最近，对于所有马尔可夫扩散，截止现象被证明是系统地遵循非负曲率和乘积条件的。该证明主要依赖于carr’e du champ算子满足的经典emph{chain rule}，该算子特定于微分生成器，因此在离散空间上失败。在本文中，我们证明了这个链式规则的近似版本实际上总是成立的，其额外成本取决于所考虑的可观测值的对数Lipschitz正则性。因此，我们推导出了有限空间上非负弯曲链的新截断准则。后者使我们能够以简单和统一的方式恢复通过特定模型参数建立的许多历史截断实例。有象征意义的例子包括超立方体上的随机游走、随机转置、多层上的随机游动，或有界度图上伊辛和硬核模型等流行自旋系统的MCMC采样器。 et.al.|[2501.13079](http://arxiv.org/abs/2501.13079)|null|
|**2025-01-22**|**Robust Body Composition Analysis by Generating 3D CT Volumes from Limited 2D Slices**|身体成分分析为衰老、疾病进展和整体健康状况提供了有价值的见解。由于对辐射暴露的担忧，二维（2D）单层计算机断层扫描（CT）成像已被反复用于身体成分分析。然而，这种方法引入了显著的空间变异性，可能会影响分析的准确性和稳健性。为了缓解这一问题并促进身体成分分析，本文提出了一种使用潜在扩散模型（LDM）从有限数量的2D切片生成3D CT体积的新方法。我们的方法首先使用变分自动编码器将2D切片映射到潜在的表示空间中。然后训练LDM以捕获这些潜在表示的堆栈的3D上下文。为了精确插值中间切片并构建完整的3D体积，我们利用身体部位回归来确定所采集切片之间的空间位置和距离。在内部和公共3D腹部CT数据集上的实验表明，与传统的基于2D的分析相比，所提出的方法显著增强了身体成分分析，错误率从23.3%降低到15.2%。 et.al.|[2501.13071](http://arxiv.org/abs/2501.13071)|null|
|**2025-01-22**|**Beyond the Lungs: Extending the Field of View in Chest CT with Latent Diffusion Models**|人体肺部和其他器官（如肝脏和肾脏）之间的相互联系对于了解肺部疾病的潜在风险和影响以及改善患者护理至关重要。然而，由于成本和辐射剂量的考虑，大多数胸部CT成像研究仅关注肺部。所采集图像中的这种受限视场（FOV）对全面分析提出了挑战，并阻碍了了解肺部疾病对其他器官影响的能力。为了解决这个问题，我们提出了SCOPE（先验编码的空间覆盖优化），这是一种从CT图像中捕获器官间关系并扩展胸部CT图像视场的新方法。我们的方法首先训练一个变分自动编码器（VAE）来单独编码2D轴向CT切片，然后堆叠VAE的潜在表示，形成一个用于训练潜在扩散模型的3D上下文。训练后，我们的方法通过以零样本方式生成新的轴向切片，在z方向上扩展CT图像的FOV。我们在国家肺部筛查试验（NLST）数据集上评估了我们的方法，结果表明，它有效地扩展了视野，将肝脏和肾脏包括在内，而肝脏和肾脏在原始NLST数据采集中没有完全覆盖。对保留的全身数据集的定量结果表明，生成的切片与采集的数据具有高保真度，SSIM为0.81。 et.al.|[2501.13068](http://arxiv.org/abs/2501.13068)|null|
|**2025-01-22**|**Probing the Quantum Nature of Gravity through Diffusion**|自20世纪中叶以来，由于无法获得普朗克尺度，确定引力是否是量子引力的探索一直是物理学家面临的挑战，在普朗克尺度上，潜在的量子引力效应有望变得相关。虽然最近基于纠缠的测试提供了一条更有前景的理论前进道路，但制备和控制大量子态的困难阻碍了实际进展。我们提出了一种替代策略，将焦点从复杂的量子态操纵转移到对探针运动的更简单观察。通过证明经典和局部引力场必须固有地显示随机性才能与量子物质一致地相互作用，我们证明了这种随机性会在探测器的运动中引起可测量的扩散，即使探测器处于经典状态。这种扩散是经典引力与量子物质耦合的独特特征。我们的方法利用了现有的实验技术，只需要精确跟踪探测器的经典质心运动，不需要任何量子态准备，从而将这种方法定位为推进引力量子性质研究的有前景和实用的途径。 et.al.|[2501.13030](http://arxiv.org/abs/2501.13030)|null|
|**2025-01-22**|**eROSITA X-ray Analysis of the PeVatron Candidate Westerlund 1**|目前尚不清楚能量超过1 PeV的宇宙射线中，哪一部分被观测到的银河系PeVatron群体加速。这些源的伽马射线数据通常在强子和轻子发射场景之间退化，这阻碍了它们与宇宙射线种群的直接关联。在这里，我们旨在区分与星团Westerlund 1（Wd 1）相关的PeVatron候选HESS J1646-458的轻子和强子粒子加速场景。我们首先研究了Wd 1的漫射X射线发射，以更好地了解其起源是热的还是非热的。此外，我们还搜索了相关PeVatron候选HESS J1646-458的X射线同步辐射，以对该源的磁场强度和轻子粒子群施加新的约束。我们使用SRG轨道平台上eROSITA的数据对Wd 1和HESS J1646-458的漫射发射进行了光谱分析。对于Wd 1，我们比较了纯热模型和具有热和非热分量的模型。接下来，我们分析了与HESS J1646-458一致的Wd 1周围四个环的光谱，以寻找同步辐射。我们发现，eROSITA数据无法区分Wd 1本身扩散发射的热源和非热源情况。在HESS J1646-458的情况下，我们没有发现同步辐射的证据。我们估计同步加速器通量在Wd 1附近高达40'的置信上限为1.9e-3 keV-1 cm-2 s-1，我们用它来研究源的光谱能量分布。由此，我们得到了HESS J1646-458磁场强度的上限1σ为7 uG。这与文献中先前对完全轻子源情景的估计相一致。纯轻子发射情景、强子和混合情景与我们的结果相一致。 et.al.|[2501.12990](http://arxiv.org/abs/2501.12990)|null|
|**2025-01-22**|**Low-dimensional adaptation of diffusion models: Convergence in total variation**|本文研究了扩散生成模型如何利用（未知）低维结构来加速采样。聚焦于两个主流采样器——去噪扩散隐式模型（DDIM）和去噪扩散概率模型（DDPM）——并假设准确的分数估计，我们证明了它们的迭代复杂度不大于 $k/\varepsilon$的数量级（高达某个对数因子），其中$\varepilon$是总变化距离的精度，$k$ 是目标分布的某个内在维度。我们的结果适用于广泛的目标分布家族，不需要平滑度或对数凹度假设。此外，我们开发了一个下限，表明Ho等人（2020年）和Song等人（2020）引入的系数在促进低维适应方面（接近）必要性。我们的发现为DDIM型采样器对未知低维结构的适应性提供了第一个严格的证据，并在总变分收敛方面改进了最先进的DDPM理论。 et.al.|[2501.12982](http://arxiv.org/abs/2501.12982)|null|
|**2025-01-22**|**LiT: Delving into a Simplified Linear Diffusion Transformer for Image Generation**|在常用的亚二次复杂度模块中，线性注意力受益于简单性和高并行性，使其有望用于图像合成任务。然而，线性注意力的建筑设计和学习策略在这一领域仍然没有得到充分的探索。在本文中，我们为高效的线性扩散变压器提供了一套现成的解决方案。我们的核心贡献包括：（1）使用少量头部简化线性注意力，观察性能的免费午餐效应，而不会增加延迟。（2） 来自完全预训练的扩散变换器的权重继承：使用预训练的传播变换器初始化线性变换器，并加载除与线性注意力相关的参数外的所有参数。（3） 混合知识蒸馏目标：使用预训练的扩散变换器来帮助训练学生线性变换器，不仅监督预测的噪声，还监督反向扩散过程的方差。这些指导方针促成了我们提出的线性扩散变换器（LiT），这是一种高效的文本到图像变换器，可以在笔记本电脑上离线部署。实验表明，类内条件256*256和512*512 ImageNet基准LiT实现了极具竞争力的FID，同时与DiT相比，训练步骤分别减少了80%和77%。LiT还可以与基于Mamba或门控线性注意力的方法相媲美。此外，对于文本到图像的生成，LiT允许快速合成高达1K分辨率的照片级真实感图像。项目页面：https://techmonsterwang.github.io/LiT/. et.al.|[2501.12976](http://arxiv.org/abs/2501.12976)|null|

<p align=right>(<a href=#updated-on-20250123>back to top</a>)</p>

## NeRF

|Publish Date|Title|Abstract|PDF|Code|
|---|---|---|---|---|
|**2025-01-22**|**Retrieval-Augmented Neural Field for HRTF Upsampling and Personalization**|具有密集空间网格的头部相关传递函数（HRTF）是沉浸式双耳音频生成的理想选择，但它们的记录很耗时。尽管HRTF空间上采样在神经场方面取得了显著进展，但仅从几个测量方向（例如3或5个测量方向）进行空间上采样仍然具有挑战性。为了解决这个问题，我们提出了一种检索增强神经场（RANF）。RANF从数据集中检索HRTF接近目标受试者HRTF的受试者。除了声源方向本身之外，检索到的对象在所需方向上的HRTF也被馈送到神经场中。此外，我们提出了一种神经网络，它可以有效地处理多个检索到的主题，灵感来自一种称为变换平均连接的多通道处理技术。我们的实验证实了RANF在SONICOM数据集上的优势，它是2024年听众声学个性化挑战任务2获胜解决方案的关键组成部分。 et.al.|[2501.13017](http://arxiv.org/abs/2501.13017)|null|
|**2025-01-15**|**CityDreamer4D: Compositional Generative Model of Unbounded 4D Cities**|近年来，3D场景生成引起了越来越多的关注，并取得了重大进展。生成4D城市比3D场景更具挑战性，因为存在结构复杂、视觉多样的物体，如建筑物和车辆，并且人类对城市环境中的扭曲更加敏感。为了解决这些问题，我们提出了CityDreamer4D，这是一个专门为生成无界4D城市而定制的组合生成模型。我们的主要见解是1）4D城市生成应该将动态对象（如车辆）与静态场景（如建筑物和道路）分开，2）4D场景中的所有对象都应该由建筑物、车辆和背景材料的不同类型的神经场组成。具体来说，我们提出了交通场景生成器和无边界布局生成器，使用高度紧凑的BEV表示生成动态交通场景和静态城市布局。4D城市中的对象是通过结合面向对象和面向实例的神经场来生成的，用于背景材料、建筑物和车辆。为了适应背景材料和实例的不同特征，神经场采用定制的生成哈希网格和周期性位置嵌入作为场景参数化。此外，我们还为城市生成提供了一套全面的数据集，包括OSM、GoogleEarth和CityTopia。OSM数据集提供了各种真实世界的城市布局，而谷歌地球和CityTopia数据集则提供了大规模、高质量的城市图像，并附有3D实例注释。利用其组合设计，CityDreamer4D支持一系列下游应用程序，如实例编辑、城市风格化和城市模拟，同时在生成逼真的4D城市方面提供最先进的性能。 et.al.|[2501.08983](http://arxiv.org/abs/2501.08983)|**[link](https://github.com/hzxie/CityDreamer4D)**|
|**2025-01-15**|**Score-based 3D molecule generation with neural fields**|我们介绍了一种基于连续原子密度场的3D分子的新表示方法。使用这种表示法，我们提出了一种基于步跳采样的新模型，用于使用神经场在连续空间中无条件生成3D分子。我们的模型FuncMol使用条件神经场将分子场编码为潜码，使用Langevin MCMC从高斯平滑分布中采样噪声码（walk），在一步中对这些样本进行去噪（jump），最后将它们解码为分子场。与大多数方法不同，FuncMol可以在不假设分子结构的情况下进行3D分子的全原子生成，并且可以很好地与分子的大小进行缩放。我们的方法在类药物分子上取得了具有竞争力的结果，并且很容易扩展到大环肽，采样速度至少快一个数量级。该代码可在以下网址获得https://github.com/prescient-design/funcmol. et.al.|[2501.08508](http://arxiv.org/abs/2501.08508)|**[link](https://github.com/prescient-design/funcmol)**|
|**2025-01-10**|**Nonlinear partial differential equations in neuroscience: from modelling to mathematical theory**|许多偏微分方程组已被提出作为大型神经元网络中复杂集体行为的简化表示。在这项调查中，我们简要讨论了它们的推导，然后回顾了为处理这些模型的独特特征而开发的数学方法，这些模型通常是非线性和非局部的。第一部分重点介绍抛物型福克-普朗克方程：非线性噪声泄漏积分和火神经元模型，PDE形式的随机神经场及其在网格单元中的应用，以及基于速率的决策模型。第二部分涉及双曲线输运方程，即自上次排放以来经过的时间模型和基于跳跃的泄漏积分和火灾模型。最后一部分介绍了一些动力学介观模型，特别关注动力学电压电导模型和FitzHugh-Nagumo动力学福克-普朗克系统。 et.al.|[2501.06015](http://arxiv.org/abs/2501.06015)|null|
|**2025-01-10**|**Locality-aware Gaussian Compression for Fast and High-quality Rendering**|我们提出了LocoGS，这是一种局部感知的3D高斯散斑（3DGS）框架，它利用3D高斯的空间相干性对体积场景进行紧凑建模。为此，我们首先分析了3D高斯属性的局部相干性，并提出了一种新的局部感知3D高斯表示，该表示使用具有最小存储要求的神经场表示对局部相干高斯属性进行有效编码。除了新颖的表示方法外，LocoGS还经过精心设计，添加了密集初始化、自适应球面谐波带宽方案和针对不同高斯属性的不同编码方案等附加组件，以最大限度地提高压缩性能。实验结果表明，对于代表性的真实世界3D数据集，我们的方法优于现有的紧凑高斯表示的渲染质量，同时实现了从54.6美元到96.6美元的压缩存储大小，以及从2.1美元到2.4美元的渲染速度。甚至我们的方法也证明了平均渲染速度比最先进的压缩方法高2.4倍，具有相当的压缩性能。 et.al.|[2501.05757](http://arxiv.org/abs/2501.05757)|null|
|**2025-01-08**|**KN-LIO: Geometric Kinematics and Neural Field Coupled LiDAR-Inertial Odometry**|激光雷达惯性测距（LIO）的最新进展推动了大量应用。然而，传统的LIO系统往往更侧重于定位而不是映射，映射主要由稀疏的几何元素组成，这对于下游任务来说并不理想。最近新兴的神经场技术在密集测绘方面具有巨大的潜力，但纯激光雷达测绘很难在高动态车辆上进行。为了缓解这一挑战，我们提出了一种新的解决方案，将几何运动学与神经场紧密耦合，以增强同时状态估计和密集映射能力。我们提出了半耦合和紧耦合的运动学神经LIO（KN-LIO）系统，该系统利用在线SDF解码和迭代误差状态卡尔曼滤波来融合激光和惯性数据。我们的KN-LIO最大限度地减少了信息丢失，提高了状态估计的准确性，同时也适应了异步多LiDAR输入。对各种高动态数据集的评估表明，我们的KN-LIO在姿态估计方面的性能与现有最先进的解决方案相当或更优，并且与纯基于LiDAR的方法相比，提供了更高的密集映射精度。相关代码和数据集将在https://**上提供。 et.al.|[2501.04263](http://arxiv.org/abs/2501.04263)|null|
|**2025-01-06**|**NeuroPMD: Neural Fields for Density Estimation on Product Manifolds**|我们提出了一种新的深度神经网络方法，用于在乘积黎曼流形域上进行密度估计。在我们的方法中，网络直接参数化未知密度函数，并使用惩罚最大似然框架进行训练，惩罚项使用流形微分算子形成。网络架构和估计算法经过精心设计，以应对高维积流形域的挑战，有效地减轻了限制传统核和基展开估计器的维数灾难，并克服了非专用神经网络方法遇到的收敛问题。广泛的模拟和对大脑结构连接数据的实际应用突显了我们的方法相对于竞争对手的明显优势。 et.al.|[2501.02994](http://arxiv.org/abs/2501.02994)|**[link](https://github.com/will-consagra/neuropmd)**|
|**2025-01-03**|**Fusion DeepONet: A Data-Efficient Neural Operator for Geometry-Dependent Hypersonic Flows on Arbitrary Grids**|设计再入飞行器需要准确预测其几何形状周围的高超音速流动。对这种流动的快速预测可以彻底改变车辆设计，特别是对于变形几何形状。我们评估了先进的神经算子模型，如深度算子网络（DeepONet）、参数条件U-Net、傅里叶神经算子（FNO）和MeshGraphNet，目的是解决在有限数据下学习依赖几何的高超音速流场的挑战。具体来说，我们比较了两种网格类型的这些模型的性能：均匀笛卡尔网格和不规则网格。为了训练这些模型，我们使用36个独特的椭圆几何体，使用高阶熵稳定的DGSEM求解器生成高保真模拟，强调了使用稀缺数据集的挑战。我们评估并比较了四种基于算子的模型在预测椭圆体周围高超音速流场方面的有效性。此外，我们开发了一个名为Fusion DeepONet的新框架，该框架利用了神经场概念，并在不同的几何结构中有效地进行了推广。尽管训练数据稀缺，Fusion DeepONet在均匀网格上的性能与参数条件U-Net相当，而在不规则、任意网格上的表现优于MeshGraphNet和vanilla DeepONnet。与U-Net、MeshGraphNet和FNO相比，Fusion DeepONet需要更少的可训练参数，使其计算效率更高。我们还使用奇异值分解分析了Fusion DeepONet模型的基函数。该分析表明，Fusion DeepONet能够有效地推广到看不见的解决方案，并适应不同的几何形状和网格点，证明了其在训练数据有限的情况下的鲁棒性。 et.al.|[2501.01934](http://arxiv.org/abs/2501.01934)|null|
|**2024-12-30**|**Hierarchical Pose Estimation and Mapping with Multi-Scale Neural Feature Fields**|机器人应用需要对场景有全面的了解。近年来，基于神经场的参数化整个环境的方法已经变得流行。由于其连续性和学习场景先验的能力，这些方法很有前景。然而，当处理未知的传感器姿态和连续测量时，在机器人中使用神经场变得具有挑战性。本文主要研究大规模神经隐式SLAM的传感器姿态估计问题。我们从概率的角度研究了隐式映射，并提出了具有相应神经网络架构的分层姿态估计。我们的方法非常适合大规模隐式映射表示。所提出的方法在连续的室外LiDAR扫描上运行，实现了精确的姿态估计，同时保持了短轨迹和长轨迹的稳定映射质量。我们在适合大规模重建的结构化稀疏隐式表示上构建了我们的方法，并使用KITTI和MaiCity数据集对其进行了评估。我们的方法在未知姿态的映射方面优于基线，并实现了最先进的定位精度。 et.al.|[2412.20976](http://arxiv.org/abs/2412.20976)|null|
|**2024-12-26**|**Humans as a Calibration Pattern: Dynamic 3D Scene Reconstruction from Unsynchronized and Uncalibrated Videos**|最近关于动态神经场重建的工作假设输入来自具有已知姿势的同步多视图视频。这些输入约束在现实世界的设置中经常得不到满足，使得这种方法不切实际。我们证明，如果视频捕捉到人体运动，则姿态未知的非同步视频可以生成动态神经场。人类是最常见的动态主体之一，其姿势可以使用最先进的方法进行估计。在有噪声的情况下，估计的人体形状和姿态参数为训练一致的动态神经表示的高度非凸和欠约束问题提供了一个不错的初始化。给定人类的姿势和形状序列，我们估计视频之间的时间偏移，然后通过分析3D关节位置进行相机姿势估计。然后，我们使用多分辨率脊训练动态NeRF，同时细化时间偏移和相机姿态。该设置仍然涉及优化许多参数，因此，我们引入了一种鲁棒的渐进学习策略来稳定该过程。实验表明，我们的方法在具有挑战性的条件下实现了精确的时空校准和高质量的场景重建。 et.al.|[2412.19089](http://arxiv.org/abs/2412.19089)|null|

<p align=right>(<a href=#updated-on-20250123>back to top</a>)</p>

[contributors-shield]: https://img.shields.io/github/contributors/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[contributors-url]: https://github.com/Vincentqyw/cv-arxiv-daily/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[forks-url]: https://github.com/Vincentqyw/cv-arxiv-daily/network/members
[stars-shield]: https://img.shields.io/github/stars/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[stars-url]: https://github.com/Vincentqyw/cv-arxiv-daily/stargazers
[issues-shield]: https://img.shields.io/github/issues/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[issues-url]: https://github.com/Vincentqyw/cv-arxiv-daily/issues

