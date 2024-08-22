[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]

## Updated on 2024.08.22
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
|**2024-08-21**|**Robust 3D Gaussian Splatting for Novel View Synthesis in Presence of Distractors**|3D高斯散斑显示了令人印象深刻的新颖视图合成结果；然而，它很容易受到动态对象的影响，这些对象会污染原本静态场景的输入数据，即所谓的干扰。干扰因素对渲染质量有严重影响，因为它们被表示为与视图相关的效果或导致浮动伪影。我们的目标是在3D高斯优化过程中识别并忽略这些干扰物，以获得干净的重建。为此，我们采取了一种自我监督的方法，在优化过程中查看图像残差，以确定可能被干扰物伪造的区域。此外，我们利用预训练的分割网络来提供对象感知，从而更准确地排除干扰因素。通过这种方式，我们获得了干扰物的分割掩模，以便在损失公式中有效地忽略它们。我们证明，我们的方法对各种干扰物具有鲁棒性，并显著提高了干扰物污染场景的渲染质量，与3D高斯散斑相比，PSNR提高了1.86dB。 et.al.|[2408.11697](http://arxiv.org/abs/2408.11697)|**[link](https://github.com/paulungermann/Robust3DGaussians)**|
|**2024-08-21**|**Pano2Room: Novel View Synthesis from a Single Indoor Panorama**|最近的单视图3D生成方法通过利用从广泛的3D对象数据集中提取的知识取得了重大进展。然而，从单个视图合成3D场景仍然存在挑战，主要是由于现实世界环境的复杂性和高质量先验资源的可用性有限。本文介绍了一种名为Pano2Room的新方法，旨在从单张全景图像中自动重建高质量的3D室内场景。这些全景图像可以使用全景RGBD修复器从任何相机在单个位置的捕获中轻松生成。关键思想是首先从输入全景图构建一个初步网格，并在收集照片级逼真的3D一致伪新颖视图的同时，使用全景RGBD修复器迭代地细化该网格。最后，将精细网格转换为三维高斯散斑场，并用收集到的伪新视图进行训练。该管道能够重建现实世界的3D场景，即使在存在大遮挡的情况下也是如此，并有助于合成具有详细几何形状的照片级逼真新颖视图。已经进行了广泛的定性和定量实验，以验证我们的方法在单全景室内新颖合成方面与最先进的方法相比的优越性。我们的代码和数据可在\url上获得{https://github.com/TrickyGo/Pano2Room}. et.al.|[2408.11413](http://arxiv.org/abs/2408.11413)|**[link](https://github.com/trickygo/pano2room)**|
|**2024-08-20**|**TrackNeRF: Bundle Adjusting NeRF from Sparse and Noisy Views via Feature Tracks**|神经辐射场（NeRF）通常需要许多具有精确姿态的图像来进行精确的新颖视图合成，这并不能反映视图稀疏、姿态嘈杂的真实设置。以前用于学习具有稀疏视图和嘈杂姿态的NeRF的解决方案只考虑与成对视图的局部几何一致性。紧跟运动结构（SfM）中的\textit{束调整}，我们引入了TrackNeRF，以实现更全局一致的几何重建和更精确的姿态优化。TrackNeRF引入了\textit{特征轨迹}，即与\textit{same}3D点对应的\textit{1all}可见视图上的连接像素轨迹。通过强制特征轨迹之间的重投影一致性，TrackNeRF明确鼓励整体3D一致性。通过广泛的实验，TrackNeRF在噪声和稀疏视图重建方面树立了新的基准。特别是，TrackNeRF在各种稀疏和嘈杂的视图设置下，在DTU上的PSNR方面比最先进的BARF和SPARF分别提高了 $\sim8$和$\sim1$ 。该代码可在\href处获得{https://tracknerf.github.io/}. et.al.|[2408.10739](http://arxiv.org/abs/2408.10739)|null|
|**2024-08-19**|**Implicit Gaussian Splatting with Efficient Multi-Level Tri-Plane Representation**|高斯散斑（3DGS）极大地推动了照片级真实感新视图合成的最新进展。然而，3DGS数据的显式性质需要相当大的存储要求，这突显了对更高效数据表示的迫切需求。为了解决这个问题，我们提出了隐式高斯散布（IGS），这是一种创新的混合模型，通过多级三平面架构将显式点云与隐式特征嵌入集成在一起。该架构以不同级别的不同分辨率的2D特征网格为特征，促进了连续的空间域表示，并增强了高斯基元之间的空间相关性。在此基础上，我们引入了一种基于水平的渐进训练方案，该方案结合了显式的空间正则化。该方法利用空间相关性来提高IGS表示的渲染质量和紧凑性。此外，考虑到不同层次的熵变化，我们提出了一种针对点云和二维特征网格量身定制的新型压缩管道。大量的实验评估表明，我们的算法只需几MB就可以提供高质量的渲染，有效地平衡了存储效率和渲染保真度，并产生了与最先进技术竞争的结果。 et.al.|[2408.10041](http://arxiv.org/abs/2408.10041)|null|
|**2024-08-20**|**Gaussian in the Dark: Real-Time View Synthesis From Inconsistent Dark Images Using Gaussian Splatting**|3D高斯散斑最近已经成为一种强大的表示方法，可以使用一致的多视图图像作为输入来合成非凡的新颖视图。然而，我们注意到，在场景未完全照亮的黑暗环境中捕获的图像可能会表现出相当大的亮度变化和多视图不一致性，这对3D高斯散斑技术提出了巨大挑战，并严重降低了其性能。为了解决这个问题，我们提出了高斯DK。观察到不一致主要是由相机成像引起的，我们使用一组各向异性3D高斯表示物理世界的一致辐射场，并设计了一个相机响应模块来补偿多视图不一致。我们还引入了一种基于步长的梯度缩放策略，以约束摄像机附近的高斯分布，使其无法分裂和克隆。在我们提出的基准数据集上的实验表明，Gaussian DK可以产生高质量的渲染，没有重影和浮动伪影，并且明显优于现有方法。此外，我们还可以通过控制曝光水平来合成发光图像，以清楚地显示阴影区域的细节。 et.al.|[2408.09130](http://arxiv.org/abs/2408.09130)|**[link](https://github.com/yec22/Gaussian-DK)**|
|**2024-08-16**|**Correspondence-Guided SfM-Free 3D Gaussian Splatting for NVS**|无运动结构（SfM）预处理相机姿态的新型视图合成（NVS）——称为无SfM方法——对于提高快速响应能力和增强对可变操作条件的鲁棒性至关重要。最近的无SfM方法集成了姿态优化，为联合相机姿态估计和NVS设计了端到端的框架。然而，大多数现有的工作依赖于每像素图像损失函数，如L2损失。在无SfM方法中，不准确的初始姿态会导致失准问题，在每像素图像损失函数的约束下，这会导致梯度过大，导致NVS的优化不稳定和收敛性差。在这项研究中，我们提出了一种用于NVS的无对应引导SfM 3D高斯溅射。我们使用目标和渲染结果之间的对应关系来实现更好的像素对齐，从而优化帧之间的相对姿态。然后，我们应用学习到的姿势来优化整个场景。每个2D屏幕空间像素通过近似表面渲染与其相应的3D高斯相关联，以促进梯度反向传播。实验结果强调了与最先进的基线相比，所提出的方法具有更优的性能和时间效率。 et.al.|[2408.08723](http://arxiv.org/abs/2408.08723)|null|
|**2024-08-16**|**GS-ID: Illumination Decomposition on Gaussian Splatting via Diffusion Prior and Parametric Light Source Optimization**|我们提出了GS-ID，这是一种用于高斯散斑照明分解的新框架，实现了逼真的新视图合成和直观的光编辑。光照分解是一个不适定问题，面临三个主要挑战：1）通常缺乏几何和材料的先验知识；2） 复杂的照明条件涉及多个未知光源；以及3）使用多个光源计算表面着色在计算上是昂贵的。为了应对这些挑战，我们首先引入内在扩散先验来估计基于物理的渲染的属性。然后我们将光照分为环境和直接分量进行联合优化。最后，我们采用延迟渲染来减少计算负载。我们的框架使用可学习的环境图和球面高斯（SG）来参数化地表示光源，从而在高斯散斑上实现可控和逼真的重新照明。广泛的实验和应用表明，GS-ID可以产生最先进的照明分解结果，同时实现更好的几何重建和渲染性能。 et.al.|[2408.08524](http://arxiv.org/abs/2408.08524)|**[link](https://github.com/dukang/gs-id)**|
|**2024-08-15**|**MVInpainter: Learning Multi-View Consistent Inpainting to Bridge 2D and 3D Editing**|新视图合成（NVS）和3D生成最近取得了显著的进步。然而，这些作品主要集中在有限的类别或合成的3D资产上，不鼓励在野外场景中推广到具有挑战性的场景，也不能直接用于2D合成。此外，这些方法严重依赖于相机姿态，限制了它们在现实世界中的应用。为了克服这些问题，我们提出了MVInpainter，将3D编辑重新定义为多视图2D修复任务。具体来说，MVInpainter使用参考引导对多视图图像进行部分修复，而不是从头开始艰难地生成一个全新的视图，这大大简化了野外NVS的难度，并利用了未掩盖的线索而不是明确的姿势条件。为了确保交叉视图的一致性，MVInpainter通过来自运动分量的视频先验和来自级联参考键值关注的外观引导进行了增强。此外，MVInpainter结合了狭缝注意力，以聚合来自未遮蔽区域的高级光流特征，从而通过无姿态训练和推理来控制相机运动。在以对象为中心和面向前的数据集上进行的足够的场景级实验验证了MVInpainter的有效性，包括多种任务，如多视图对象删除、合成、插入和替换。项目页面为https://ewrfcas.github.io/MVInpainter/. et.al.|[2408.08000](http://arxiv.org/abs/2408.08000)|null|
|**2024-08-14**|**Progressive Radiance Distillation for Inverse Rendering with Gaussian Splatting**|我们提出了渐进式辐射蒸馏，这是一种逆向渲染方法，使用蒸馏进度图将基于物理的渲染与基于高斯的辐射场渲染相结合。以多视图图像为输入，我们的方法从预训练的辐射场引导开始，并使用图像拟合过程从辐射场中提取基于物理的光和材料参数。蒸馏进度图被初始化为一个较小的值，这有利于辐射场渲染。在早期迭代中，当拟合的光和材料参数远未收敛时，辐射场回退确保了图像损失梯度的完整性，并避免了吸引拟合不足状态的局部最小值。随着拟合参数的收敛，物理模型逐渐接管，蒸馏过程相应增加。在存在未被物理模型建模的光路的情况下，受影响像素的蒸馏过程永远不会结束，学习到的辐射场会留在最终渲染中。通过这种对物理模型限制的设计容差，我们可以防止未建模的颜色分量泄漏到光和材料参数中，从而减轻重新照明伪影。同时，剩余的辐射场补偿了物理模型的局限性，保证了高质量的新颖视图合成。实验结果表明，在新颖的视图合成和重新照明方面，我们的方法在质量上明显优于最先进的技术。渐进式辐射蒸馏的概念不仅限于高斯散射。我们表明，当采用基于网格的逆渲染方法时，它对显著镜面反射的场景也有积极的影响。 et.al.|[2408.07595](http://arxiv.org/abs/2408.07595)|null|
|**2024-08-18**|**Rethinking Open-Vocabulary Segmentation of Radiance Fields in 3D Space**|理解场景的3D语义是各种场景（如实体代理）的基本问题。虽然NeRF和3DGS擅长新颖的视图合成，但之前理解其语义的方法仅限于不完整的3D理解：它们的分割结果是2D掩模，它们的监督是基于2D像素的。本文重新审视了问题集，以更好地理解由NeRFs和3DGS建模的场景，如下所示。1） 我们直接监督3D点来训练语言嵌入域。它实现了最先进的精度，而不依赖于多尺度语言嵌入。2） 我们将预训练的语言字段转移到3DGS，在不牺牲训练时间或精度的情况下实现了第一个实时渲染速度。3） 我们介绍了一种3D查询和评估协议，用于同时评估重建的几何和语义。代码、检查点和注释将在线提供。项目页面：https://hyunji12.github.io/Open3DRF et.al.|[2408.07416](http://arxiv.org/abs/2408.07416)|null|

<p align=right>(<a href=#updated-on-20240822>back to top</a>)</p>

## 3D Reconstruction

|Publish Date|Title|Abstract|PDF|Code|
|---|---|---|---|---|
|**2024-08-21**|**DeRainGS: Gaussian Splatting for Enhanced Scene Reconstruction in Rainy**|由于能见度降低和视觉感知失真，在恶劣的降雨条件下进行重建带来了重大挑战。这些条件会严重损害几何地图的质量，而几何地图对于从自主规划到环境监测的应用至关重要。为了应对这些挑战，本研究引入了雨天环境中的3D重建（3DRRE）这一新任务，专门用于解决雨天条件下重建3D场景的复杂性。为了对这项任务进行基准测试，我们构建了HydroViews数据集，该数据集包括以不同强度的雨条和雨滴为特征的合成和现实世界场景图像的不同集合。此外，我们提出了DeRainGS，这是第一种专为恶劣雨天环境中的重建而定制的3DGS方法。在各种降雨场景中进行的广泛实验表明，我们的方法提供了最先进的性能，大大优于现有的无遮挡方法。 et.al.|[2408.11540](http://arxiv.org/abs/2408.11540)|null|
|**2024-08-21**|**MeTTA: Single-View to 3D Textured Mesh Reconstruction with Test-Time Adaptation**|从单视图图像重建3D是一个长期存在的挑战。解决这个问题的一种流行方法是基于学习的方法，但处理不熟悉训练数据的测试用例（分布外；OoD）会带来额外的挑战。为了适应测试时间中看不见的样本，我们提出了MeTTA，一种利用生成先验的测试时间自适应（TTA）。我们设计了3D几何、外观和姿势的联合优化，以处理仅使用单视图图像的OoD病例。然而，通过估计的视点在参考图像和3D形状之间的对准可能是错误的，这会导致模糊。为了解决这种模糊性，我们精心设计了可学习的虚拟相机及其自校准。在我们的实验中，我们证明了MeTTA能够有效地处理现有基于学习的3D重建模型在失败情况下的OoD场景，并能够通过基于物理的渲染（PBR）纹理获得逼真的外观。 et.al.|[2408.11465](http://arxiv.org/abs/2408.11465)|null|
|**2024-08-20**|**Learning Part-aware 3D Representations by Fusing 2D Gaussians and Superquadrics**|低级3D表示，如点云、网格、NeRF和3D高斯，通常用于表示3D对象或场景。然而，人类通常将3D对象或场景视为更高层次的部分或结构的组合，而不是点或体素。将3D表示为语义部分有助于进一步理解和应用。我们的目标是解决部分感知的3D重建，将对象或场景解析为语义部分。本文介绍了一种超二次曲面和二维高斯的混合表示，试图从多视图图像输入中挖掘三维结构线索。同时实现了精确的结构化几何重建和高质量的渲染。我们通过将高斯中心附加到网格中的面上，将网格形式的参数超二次曲面合并到二维高斯中。在训练过程中，迭代优化超二次曲线参数，并相应地对高斯曲线进行变形，从而得到高效的混合表示。一方面，这种混合表示继承了超二次曲面表示不同形状图元的优点，支持场景的灵活部分分解。另一方面，2D高斯被用来模拟复杂的纹理和几何细节，确保高质量的渲染和几何重建。重建完全不受监督。我们对DTU和ShapeNet数据集的数据进行了广泛的实验，该方法将场景分解为合理的部分，优于现有的最先进的方法。 et.al.|[2408.10789](http://arxiv.org/abs/2408.10789)|null|
|**2024-08-21**|**NeRF-US: Removing Ultrasound Imaging Artifacts from Neural Radiance Fields in the Wild**|在训练基于NeRF的方法时，在超声成像数据中执行3D重建和新颖视图合成（NVS）的当前方法经常面临严重的伪影。由于超声捕获的独特性，当前方法产生的伪影与一般场景中的NeRF漂浮物不同。此外，当在不受控制的环境中随意捕获或获得超声数据时，现有的模型无法产生合理的3D重建，这在临床环境中很常见。因此，现有的重建和NVS方法难以处理超声运动，无法捕捉复杂的细节，也无法对透明和反射表面进行建模。在这项工作中，我们引入了NeRF US，它将边界概率和散射密度的3D几何引导结合到NeRF训练中，同时还利用了传统体绘制之上的超声特定渲染。这些3D先验是通过扩散模型学习的。通过在我们新的“野外超声”数据集上进行的实验，我们观察到了准确、临床合理、无伪影的重建。 et.al.|[2408.10258](http://arxiv.org/abs/2408.10258)|null|
|**2024-08-19**|**MeshFormer: High-Quality Mesh Generation with 3D-Guided Reconstruction Model**|开放世界3D重建模型最近引起了广泛关注。然而，如果没有足够的3D感应偏差，现有的方法通常需要昂贵的训练成本，并且难以提取高质量的3D网格。在这项工作中，我们介绍了MeshFormer，这是一种稀疏视图重建模型，它明确地利用了3D原生结构、输入指导和训练监督。具体来说，我们不是使用三平面表示，而是将特征存储在3D稀疏体素中，并将变换器与3D卷积相结合，以利用显式的3D结构和投影偏差。除了稀疏视图RGB输入外，我们还要求网络接受输入并生成相应的法线图。输入法线图可以通过二维扩散模型进行预测，这大大有助于指导和细化几何体的学习。此外，通过将符号距离函数（SDF）监督与表面渲染相结合，我们可以直接学习生成高质量的网格，而不需要复杂的多阶段训练过程。通过结合这些显式的3D偏差，MeshFormer可以有效地进行训练，并提供具有细粒度几何细节的高质量纹理网格。它还可以与2D扩散模型集成，以实现快速的单图像到3D和文本到3D任务。项目页面：https://meshformer3d.github.io et.al.|[2408.10198](http://arxiv.org/abs/2408.10198)|null|
|**2024-08-19**|**SpaRP: Fast 3D Object Reconstruction and Pose Estimation from Sparse Views**|开放世界3D生成最近引起了相当大的关注。虽然许多单图像到3D的方法产生了视觉上吸引人的结果，但它们往往缺乏足够的可控性，并且往往会产生可能不符合用户期望的幻觉区域。在这篇论文中，我们探索了一个重要的场景，其中输入由单个对象的一个或几个无滤镜的2D图像组成，重叠很少或没有重叠。我们提出了一种新的方法SpaRP来重建3D纹理网格，并估计这些稀疏视图图像的相对相机姿态。SpaRP从2D扩散模型中提取知识，并对其进行微调，以隐式推断稀疏视图之间的3D空间关系。训练扩散模型，以联合预测已知姿态下物体的相机姿态和多视图图像的替代表示，整合来自输入稀疏视图的所有信息。然后利用这些预测来完成3D重建和姿态估计，重建的3D模型可用于进一步细化输入视图的相机姿态。通过在三个数据集上的广泛实验，我们证明我们的方法不仅在3D重建质量和姿态预测精度方面显著优于基线方法，而且表现出很强的效率。为输入视图生成纹理网格和相机姿态只需要大约20秒。项目页面：https://chaoxu.xyz/sparp. et.al.|[2408.10195](http://arxiv.org/abs/2408.10195)|null|
|**2024-08-15**|**Comparative Evaluation of 3D Reconstruction Methods for Object Pose Estimation**|物体姿态估计对于涉及机器人操纵、导航和增强现实的许多工业应用至关重要。当前的可推广对象姿态估计器，即不需要对每个对象进行训练的方法，依赖于精确的3D模型。主要使用CAD模型，这在实践中很难获得。同时，通常可以获取对象的图像。自然地，这导致了一个问题，即从图像重建的3D模型是否足以促进准确的物体姿态估计。我们的目标是通过提出一个新的基准来衡量3D重建质量对姿态估计精度的影响，从而回答这个问题。我们的基准为对象重建提供了校准图像，这些图像与YCB-V数据集的测试图像进行了配准，用于BOP基准格式下的姿态评估。对多种最先进的3D重建和物体姿态估计方法的详细实验表明，现代重建方法产生的几何形状通常足以进行精确的姿态估计。我们的实验得出了有趣的观察结果：（1）测量3D重建质量的标准指标不一定能指示姿态估计的准确性，这表明需要像我们这样的专用基准。（2） 经典的、非基于学习的方法可以与现代基于学习的重建技术相提并论，甚至可以提供更好的重建时间-姿态精度权衡。（3） 重建模型和CAD模型的性能之间仍存在相当大的差距。为了促进缩小这一差距的研究，我们的基准可在https://github.com/VarunBurde/reconstruction_pose_benchmark}. et.al.|[2408.08234](http://arxiv.org/abs/2408.08234)|**[link](https://github.com/varunburde/reconstruction_pose_benchmark)**|
|**2024-08-15**|**Single-image coherent reconstruction of objects and humans**|从单眼图像重建对象和人类的现有方法存在严重的网格碰撞和交互遮挡对象的性能限制。本文介绍了一种从单个图像中获得交互对象和人的全局一致3D重建的方法。我们的贡献包括：1）一个优化框架，以碰撞损失为特征，专门用于处理人与物体和人与人之间的交互，确保空间连贯的场景重建；以及2）一种利用图像修复来稳健估计6自由度（DOF）姿态的新技术，特别是对于严重遮挡的物体。值得注意的是，我们提出的方法可以有效地处理来自真实场景的图像，而不需要场景或对象级的3D监控。对现有方法的广泛定性和定量评估表明，在具有多个相互作用的人和物体的场景的最终重建中，碰撞显著减少，场景重建更加连贯。 et.al.|[2408.08086](http://arxiv.org/abs/2408.08086)|null|
|**2024-08-14**|**Rethinking the Key Factors for the Generalization of Remote Sensing Stereo Matching Networks**|立体匹配是三维重建的关键步骤，由于其对遥感图像的强特征表示，已经完全转向深度学习。然而，立体匹配任务的地面实况依赖于昂贵的机载激光雷达数据，因此很难获得足够的样本进行监督学习。为了提高立体匹配网络对不同传感器和场景的跨域数据的泛化能力，本文致力于从三个角度研究关键的训练因素。（1） 对于训练数据集的选择，重要的是选择与测试集具有相似区域目标分布的数据，而不是使用来自同一传感器的数据。（2） 对于模型结构，首选灵活适应不同尺寸特征的级联结构。（3） 对于训练方式，无监督方法比有监督方法具有更好的泛化能力，我们设计了一种无监督的早期停止策略，以预训练的权重为基础，帮助保留最佳模型。我们进行了大量的实验来支持之前的发现，在此基础上，我们提出了一种具有良好泛化性能的无监督立体匹配网络。我们在发布源代码和数据集https://github.com/Elenairene/RKF_RSSM复制结果并鼓励未来的工作。 et.al.|[2408.07613](http://arxiv.org/abs/2408.07613)|null|
|**2024-08-13**|**PBIR-NIE: Glossy Object Capture under Non-Distant Lighting**|光滑物体对自然光照下多视图输入图像的3D重建提出了重大挑战。在本文中，我们介绍了PBIR-NIE，这是一个反向渲染框架，旨在全面捕捉此类对象的几何、材质属性和周围照明。我们提出了一种新颖的视差感知非远距离环境图，作为一种轻量级且高效的照明表示，可以准确地模拟场景的近场背景，这在现实世界的捕捉设置中很常见。此功能使我们的框架能够适应超出标准无限距离环境贴图能力的复杂视差效果。我们的方法通过基于物理的可微渲染来优化底层有符号距离场（SDF），通过神经隐式进化（NIE）无缝连接三角形网格和SDF之间的表面梯度。为了解决可微渲染中高光泽BRDF的复杂性，我们集成了对偶采样算法来减轻蒙特卡洛梯度估计器中的方差。因此，我们的框架在处理光滑物体重建方面表现出强大的能力，在几何、重新照明和材料估计方面表现出卓越的质量。 et.al.|[2408.06878](http://arxiv.org/abs/2408.06878)|null|

<p align=right>(<a href=#updated-on-20240822>back to top</a>)</p>

## Diffusion

|Publish Date|Title|Abstract|PDF|Code|
|---|---|---|---|---|
|**2024-08-21**|**Pixel Is Not A Barrier: An Effective Evasion Attack for Pixel-Domain Diffusion Models**|扩散模型已经成为高质量图像合成的强大生成模型，许多后续的图像编辑技术都基于它们。然而，基于文本的图像编辑的易用性带来了重大风险，例如欺诈或侵犯知识产权的恶意编辑。以前的工作试图通过添加不可察觉的扰动来保护图像免受基于扩散的编辑。这些方法成本高昂，专门针对流行的潜在扩散模型（LDM），而像素域扩散模型（PDM）在很大程度上尚未得到探索，并且对此类攻击具有鲁棒性。我们的工作通过提出一种新的攻击框架来解决这一差距，该框架具有特征表示攻击损失，利用去噪UNets中的漏洞和潜在的优化策略来增强受保护图像的自然度。大量实验证明了我们的方法在攻击基于PDM的主流编辑方法（如SDEdit）时的有效性，同时保持了对常见防御方法的合理保护保真度和鲁棒性。此外，我们的框架可扩展到LDM，实现了与现有方法相当的性能。 et.al.|[2408.11810](http://arxiv.org/abs/2408.11810)|null|
|**2024-08-21**|**Timeline and Boundary Guided Diffusion Network for Video Shadow Detection**|视频阴影检测（VSD）旨在检测具有帧序列的阴影掩模。现有作品存在时间学习效率低下的问题。此外，很少有研究通过考虑阴影的特征（即边界）来解决VSD问题。受此启发，我们提出了一种用于VSD的时间线和边界引导扩散（TBGDiff）网络，在该网络中，我们共同考虑了过去和未来的时间引导和边界信息。详细地说，我们设计了一个双尺度聚合（DSA）模块，通过重新思考剪辑视频的长期和短期帧的亲和力，更好地理解时间。接下来，我们引入阴影边界感知注意力（SBAA），利用边缘上下文来捕捉阴影的特征。此外，我们是第一个引入VSD扩散模型的人，在该模型中，我们探索了一种时空编码嵌入（STEE），为扩散注入时间引导，以进行阴影检测。受益于这些设计，我们的模型不仅可以捕获时间信息，还可以捕获阴影属性。大量实验表明，我们的方法的性能超过了最先进的方法，验证了我们组件的有效性。我们在\url上发布代码、权重和结果{https://github.com/haipengzhou856/TBGDiff}. et.al.|[2408.11785](http://arxiv.org/abs/2408.11785)|**[link](https://github.com/haipengzhou856/tbgdiff)**|
|**2024-08-21**|**Do We Really Need to Drop Items with Missing Modalities in Multimodal Recommendation?**|通常，在多模式推荐中会删除缺少模式的项目。然而，通过这项工作，我们对这一过程提出了质疑，强调它会进一步破坏任何多模式推荐系统的管道。首先，我们表明，缺乏（一些）模式实际上是多模式推荐中广泛存在的现象。其次，我们提出了一种管道，通过利用机器学习中的传统插补策略，在推荐中插补缺失的多模态特征。然后，在给定推荐数据的图结构的情况下，我们还提出了三种更有效的插补解决方案，利用项目-项目共同购买图和共同交互项目的多模态相似性。我们的方法可以插入文献中任何未经训练的预处理阶段的多模态RS中，通过广泛的实验表明，任何数据预过滤不仅是不必要的，而且对性能有害。 et.al.|[2408.11767](http://arxiv.org/abs/2408.11767)|null|
|**2024-08-21**|**Modeling multiband SEDs and light curves of BL Lacertae using a time-dependent shock-in-jet model**|blazars中快速通量变化的起源是一个长期存在的问题，提出了许多理论模型来解释它。在这项研究中，我们重点研究了BL Lacertae，使用涉及多个轻度相对论性激波的扩散激波加速过程，结合含时辐射传输代码，对其光谱能量分布（SED）和宽带光曲线进行建模。BL Lacertae是2021年7月初全面多波长监测活动的目标。我们使用Swift UVOT在光学紫外频率下、Swift XRT和AstroSat SXT/LAXPC在X射线中以及Fermi LAT在伽马射线中的同时观测，详细研究了该源的宽带光谱和光曲线特征，涵盖了2021年7月至8月期间（MJD 59400至59450）。分数变异性分析表明，伽马射线的来源变化最大，其次是X射线、紫外线和光学。这使我们能够确定伽马射线的最快变化时间大约为几个小时。AstroSat SXT和LAXPC的光曲线表明，X射线的变化大约为几千秒。同时对源的低通量和高通量状态的SED以及多波段光曲线进行建模，可以深入了解粒子加速机制。这是第一个准确捕捉BL Lacertae多波段时间变化的物理模型，包括耀斑期间观察到的小时尺度波动。 et.al.|[2408.11763](http://arxiv.org/abs/2408.11763)|null|
|**2024-08-21**|**JieHua Paintings Style Feature Extracting Model using Stable Diffusion with ControlNet**|本研究提出了一种提取节花风格特征的新方法：利用带有ControlNet的微调稳定扩散模型（FSDMC）来改进艺术家节花的描绘技巧。FSDMC的训练数据基于从互联网上收集的开源杰华艺术家的作品，随后以（原始图像、Canny Edge Features、文本提示）的格式手动构建。通过采用本文确定的最优超参数，观察到FSDMC优于另一种主流风格的传递模型CycleGAN。FSDMC在数据集上实现了3.27的FID，在专家评估方面也超过了CycleGAN。这不仅证明了该模型在提取节花风格特征方面的高效性，而且保留了原始的预训练语义信息。本研究的结果表明，具有适当超参数的FSDMC的应用可以提高稳定扩散模型在传统艺术风格迁移任务领域的效率，特别是在洁华的背景下。 et.al.|[2408.11744](http://arxiv.org/abs/2408.11744)|null|
|**2024-08-21**|**Iterative Object Count Optimization for Text-to-image Diffusion Models**|我们解决了文本到图像模型中的一个持续挑战：准确生成指定数量的对象。当前的模型从图像-文本对中学习，固有地难以计数，因为训练数据无法描绘任何给定对象的所有可能数量的对象。为了解决这个问题，我们建议基于从聚集对象潜力的计数模型中得出的计数损失来优化生成的图像。采用开箱即用的计数模型具有挑战性，原因有两个：第一，该模型需要一个缩放超参数来进行潜在的聚合，该参数根据对象的视点而变化；第二，分类器引导技术需要在有噪声的中间扩散步骤上操作的修改模型。为了应对这些挑战，我们提出了一种迭代在线训练模式，在改变文本条件嵌入和动态调整超参数的同时，提高了推断图像的准确性。我们的方法提供了三个关键优势：（i）它可以考虑基于检测模型的非衍生计数技术，（ii）它是一种零样本即插即用解决方案，有助于计数技术和图像生成方法的快速变化，（iii）优化的计数令牌可以重复使用以生成准确的图像，而无需额外优化。我们评估了各种对象的生成，并显示了准确性的显著提高。项目页面可在https://ozzafar.github.io/count_token. et.al.|[2408.11721](http://arxiv.org/abs/2408.11721)|null|
|**2024-08-21**|**FRAP: Faithful and Realistic Text-to-Image Generation with Adaptive Prompt Weighting**|文本到图像（T2I）扩散模型在给定文本提示的情况下生成高质量图像的能力令人印象深刻。然而，确保提示图像对齐仍然是一个相当大的挑战，即生成与提示语义忠实对齐的图像。最近的研究试图通过优化潜码来提高可信度，这可能会导致潜码失去分布，从而产生不切实际的图像。在本文中，我们提出了FRAP，这是一种简单而有效的方法，基于自适应调整每个令牌的提示权重，以提高提示图像的对齐和生成图像的真实性。我们设计了一种在线算法来自适应地更新每个令牌的权重系数，这是通过最小化一个鼓励对象存在和对象修饰符对绑定的统一目标函数来实现的。通过广泛的评估，我们发现FRAP生成的图像与复杂数据集的提示具有更高的提示图像对齐率，同时与最近的潜在代码优化方法相比具有更低的平均延迟，例如，在COCO受试者数据集上比D&B快4秒。此外，通过对CLIP IQA Real度量的视觉比较和评估，我们表明FRAP不仅可以提高快速图像对齐，还可以生成外观逼真的更真实的图像。我们还探索了将FRAP与快速重写LLM相结合，以恢复其退化的快速图像对齐，我们观察到快速图像对齐和图像质量都有所改善。 et.al.|[2408.11706](http://arxiv.org/abs/2408.11706)|null|
|**2024-08-21**|**The off-equilibrium Kinetic Ising model: The Metric Case**|我们研究了具有非互易最近邻相互作用的动力学伊辛模型的临界行为。有限尺度研究表明，该模型属于伊辛普适性类。我们通过测量熵产生率和研究粗化动力学来表征模型的非平衡行为，粗化动力学显示出超扩散弛豫。粗粒度运动方程与数值结果非常吻合。单环重整化群计算表明，该模型属于模型A的普适性类。 et.al.|[2408.11690](http://arxiv.org/abs/2408.11690)|null|
|**2024-08-21**|**Plug-in estimation of Schrödinger bridges**|我们提出了一种估计两个概率分布之间薛定谔桥的程序。与现有方法不同，我们的方法不需要迭代模拟前向和后向扩散或训练神经网络来拟合未知漂移。相反，我们表明，可以修改从解决源样本和目标样本之间的静态熵最优传输问题中获得的势，以产生定义两个度量之间桥的时变漂移的自然插入估计器。在最小假设下，我们证明了我们的建议（我们称之为emph{Sinkhorn桥}）可以证明地估计薛定谔电桥，其收敛速度取决于目标度量的内在维度。我们的方法结合了采样、理论和统计熵最优输运领域的结果。 et.al.|[2408.11686](http://arxiv.org/abs/2408.11686)|**[link](https://github.com/apooladian/sinkhornbridge)**|
|**2024-08-21**|**Reconstruction of reverberation theory in a diffuse sound field by using reflection orders**|房间声学是基于萨宾的混响理论建立的。然而，在萨宾的理论中，即使满足绝对吸收条件，混响时间也不会达到零。艾林修改了混响理论来解决这一矛盾。然而，埃林的理论在稳态和衰变过程的表述上是不一致的。因此，作者对Sabine的理论（Hanyu，Acoustic Science&Technology 45,32024）进行了修订，采用了与Eyring不同的方法。这一修订后的理论是通过引入“直接声音的混响”的概念构建的。本文提出了一种新的基于反射阶数的混响数学模型。这意味着作者已经提出的修正理论被重建，以包括每个反射阶中的时间能量分布。新的数学模型也使用了“直接声音的混响”的概念，但只描述了没有直接声音的反射声音的混响。这意味着“直接声音的混响”的概念对整个混响过程也至关重要。新模型的混响衰减与已经提出的修正理论一致。新模型与仿真结果具有良好的一致性。 et.al.|[2408.11670](http://arxiv.org/abs/2408.11670)|null|

<p align=right>(<a href=#updated-on-20240822>back to top</a>)</p>

## NeRF

|Publish Date|Title|Abstract|PDF|Code|
|---|---|---|---|---|
|**2024-08-19**|**Neural Representation of Shape-Dependent Laplacian Eigenfunctions**|拉普拉斯算子的特征函数在数学物理、工程和几何处理中至关重要。通常，这些是通过对域进行离散化并执行特征分解来计算的，将结果与特定的网格联系起来。然而，这种方法不适合连续参数化的形状。我们提出了一种连续参数化形状空间中本征函数的新表示，其中本征函数是连续依赖于形状参数的空间场，由最小狄利克雷能量、单位范数和相互正交性定义。我们用训练为神经场的多层感知器来实现这一点，将形状参数和域位置映射到特征函数值。一个独特的挑战是强制因果关系的相互正交性，其中因果顺序在形状空间中是不同的。因此，我们的训练方法需要三个相互交织的概念：（1）通过在单位范数约束下最小化狄利克雷能量来同时学习n$本征函数；（2） 在反向传播过程中过滤梯度以强制因果正交性，防止早期特征函数受到后期特征函数的影响；（3） 基于特征值对因果排序进行动态排序，以跟踪特征值曲线交叉。我们在形状族分析、不完整形状的特征函数预测、交互式形状操作和计算高维特征函数等问题上展示了我们的方法，这些问题都是传统方法所不能达到的。 et.al.|[2408.10099](http://arxiv.org/abs/2408.10099)|null|
|**2024-08-20**|**Scene123: One Prompt to 3D Scene Generation via Video-Assisted and Consistency-Enhanced MAE**|随着人工智能生成内容（AIGC）的进步，已经开发了各种方法来从单模式或多模式输入生成文本、图像、视频和3D对象，从而有助于模拟类人认知内容的创建。然而，由于确保模型生成的外推视图之间的一致性所涉及的复杂性，从单个输入生成逼真的大规模场景是一个挑战。受益于最新的视频生成模型和隐式神经表示，我们提出了Scene123，这是一种3D场景生成模型，它不仅通过视频生成框架确保了真实性和多样性，还使用隐式神经场与掩模自编码器（MAE）相结合，有效地确保了视图中看不见区域的一致性。具体来说，我们最初会扭曲输入图像（或从文本生成的图像）以模拟相邻的视图，用MAE模型填充不可见的区域。然而，这些填充图像通常无法保持视图一致性，因此我们利用产生的视图来优化神经辐射场，增强几何一致性。此外，为了进一步增强生成视图的细节和纹理保真度，我们对通过视频生成模型从输入图像中导出的图像采用了基于GAN的Loss。大量实验表明，我们的方法可以从单个提示中生成逼真一致的场景。定性和定量结果都表明，我们的方法超越了现有的最先进的方法。我们展示鼓励视频示例https://yiyingyang12.github.io/Scene123.github.io/. et.al.|[2408.05477](http://arxiv.org/abs/2408.05477)|null|
|**2024-08-07**|**Compact 3D Gaussian Splatting for Static and Dynamic Radiance Fields**|3D高斯飞溅（3DGS）最近成为一种替代表示，它利用基于3D高斯的表示并引入了近似的体积渲染，实现了非常快的渲染速度和有前景的图像质量。此外，后续的研究已成功地将3DGS扩展到动态3D场景，展示了其广泛的应用。然而，由于3DGS及其后续方法需要大量的高斯分布来保持渲染图像的高保真度，这需要大量的内存和存储，因此出现了一个重大的缺点。为了解决这个关键问题，我们特别强调两个关键目标：在不牺牲性能的情况下减少高斯点的数量，以及压缩高斯属性，如视图相关的颜色和协方差。为此，我们提出了一种可学习的掩码策略，该策略在保持高性能的同时显著减少了高斯数。此外，我们提出了一种紧凑但有效的视图相关颜色表示方法，即采用基于网格的神经场，而不是依赖球谐函数。最后，我们学习码本，通过残差矢量量化来紧凑地表示几何和时间属性。通过量化和熵编码等模型压缩技术，我们始终表明，与静态场景的3DGS相比，存储空间减少了25倍以上，渲染速度提高了25倍，同时保持了场景表示的质量。对于动态场景，与现有的最先进方法相比，我们的方法实现了超过12倍的存储效率，并保留了高质量的重建。我们的工作为3D场景表示提供了一个全面的框架，实现了高性能、快速训练、紧凑性和实时渲染。我们的项目页面可在https://maincold2.github.io/c3dgs/. et.al.|[2408.03822](http://arxiv.org/abs/2408.03822)|null|
|**2024-08-07**|**PRTGS: Precomputed Radiance Transfer of Gaussian Splats for Real-Time High-Quality Relighting**|我们提出了高斯斑点的预计算辐射转移（PRTGS），这是一种在低频照明环境中用于高斯斑点的实时高质量重新照明方法，通过预计算3D高斯斑点的辐射转移来捕获柔和的阴影和相互反射。现有的研究表明，在动态照明场景中，3D高斯溅射（3DGS）的效率优于神经场。然而，目前基于3DGS的重新照明方法仍然难以实时计算动态光的高质量阴影和间接照明，导致渲染结果不切实际。我们通过预先计算复杂传递函数（如阴影）所需的昂贵传输模拟来解决这个问题，得到的传递函数表示为每个高斯斑点的密集向量集或矩阵集。我们介绍了针对训练和渲染阶段量身定制的不同预计算方法，以及针对3D高斯斑点的独特光线追踪和间接照明预计算技术，以加快训练速度并计算与环境光相关的准确间接照明。实验分析表明，我们的方法在保持有竞争力的训练时间的同时实现了最先进的视觉质量，并允许以1080p分辨率对动态光和相对复杂的场景进行高质量的实时（30+fps）重新照明。 et.al.|[2408.03538](http://arxiv.org/abs/2408.03538)|null|
|**2024-08-01**|**Neural Octahedral Field: Octahedral prior for simultaneous smoothing and sharp edge regularization**|神经隐式表示，将距离函数参数化为坐标神经场，已成为解决无方向点云表面重建的有前景的前沿。为了确保方向一致，现有的方法侧重于正则化距离函数的梯度，例如将其约束为单位范数，最小化其散度，或将其与对应于零特征值的Hessian特征向量对齐。然而，在存在大扫描噪声的情况下，它们往往要么过拟合噪声输入，要么产生过于平滑的重建。在这项工作中，我们建议利用六面体网格中产生的八面体框架的球谐表示，在一种新的神经场变体——八面体场下指导曲面重建。当约束为平滑时，该字段会自动捕捉到几何特征，并在折痕上插值时自然保留锐角。通过同时拟合和平滑隐式几何旁边的八面体场，它的行为类似于双边滤波，从而在保持锐边的同时实现平滑重建。尽管是纯逐点操作，但我们的方法在广泛的实验中表现优于各种传统和神经方法，并且与需要正常和数据先验的方法非常有竞争力。我们的全面实施可在以下网址获得：https://github.com/Ankbzpx/frame-field. et.al.|[2408.00303](http://arxiv.org/abs/2408.00303)|**[link](https://github.com/ankbzpx/frame-field)**|
|**2024-07-30**|**Neural Fields for Continuous Periodic Motion Estimation in 4D Cardiovascular Imaging**|时间分辨三维血流MRI（4D血流MRI）提供了一种独特的非侵入性解决方案，用于可视化和量化主动脉弓等血管中的血流动力学。然而，由于难以获得完整的周期分割，目前大多数动脉4D血流MRI分析方法使用静态动脉壁。为了克服这一局限性，我们提出了一种基于神经场的方法，可以直接估计整个心动周期中连续的周期性壁变形。对于3D+时间成像数据集，我们优化了表示时间依赖速度矢量场（VVF）的隐式神经表示（INR）。ODE求解器用于将VVF集成到变形矢量场（DVF）中，该矢量场可以随着时间的推移使图像、分割掩模或网格变形，从而可视化和量化局部壁运动模式。为了正确反映3D+时间心血管数据的周期性，我们以两种方式施加周期性。首先，通过定期对输入到INR的时间进行编码，从而对VVF进行编码。其次，通过规范DVF。我们证明了这种方法在不同周期模式的合成数据、心电图门控CT和4D血流MRI数据上的有效性。所获得的方法可用于改进4D血流MRI分析。 et.al.|[2407.20728](http://arxiv.org/abs/2407.20728)|null|
|**2024-07-29**|**Aero-Nef: Neural Fields for Rapid Aircraft Aerodynamics Simulations**|本文提出了一种基于隐式神经表示（INR）在网格域上学习稳态流体动力学模拟替代模型的方法。所提出的模型可以直接应用于不同流动条件下的非结构化域，处理非参数3D几何变化，并推广到测试时看不见的形状。基于坐标的公式自然会导致离散化的鲁棒性，从而在计算成本（内存占用和训练时间）和精度之间实现了极好的权衡。该方法在两个工业相关应用中得到了验证：跨音速翼型上二维可压缩流的RANS数据集和三维机翼上表面压力分布的数据集，包括形状、流入条件和控制表面偏转变化。在所考虑的测试用例中，与最先进的图神经网络架构相比，我们的方法实现了三倍多的测试误差，并显著改善了看不见的几何形状的泛化误差。值得注意的是，该方法在RANS跨音速翼型数据集上的推理速度比高保真求解器快五个数量级。代码可在以下网址获得https://gitlab.isae-supaero.fr/gi.catalani/aero-nepf et.al.|[2407.19916](http://arxiv.org/abs/2407.19916)|null|
|**2024-07-26**|**ObjectCarver: Semi-automatic segmentation, reconstruction and separation of 3D objects**|隐式神经场在从多幅图像重建3D表面方面取得了显著进展；然而，在分离场景中的单个对象时，他们遇到了挑战。之前的工作试图通过引入一个框架来解决这个问题，该框架为N个对象中的每一个同时训练单独的带符号距离场（SDF），并使用正则化项来防止对象重叠。然而，所有这些方法都需要提供分割掩模，这并不总是容易获得的。我们介绍了我们的方法ObjectCarver，来解决在单个视图中从点击输入中分离对象的问题。给定摆出的多视图图像和一组用户输入点击来提示分割单个对象，我们的方法将场景分解为单独的对象，并为每个对象重建高质量的3D表面。我们引入了一个损失函数，可以防止漂浮物，避免因遮挡而造成不适当的雕刻。此外，我们引入了一种新的场景初始化方法，与之前的方法相比，该方法在保留几何细节的同时显著加快了过程。尽管不需要地面真实掩模或单眼线索，但我们的方法在定性和定量上都优于基线。此外，我们引入了一个新的基准数据集进行评估。 et.al.|[2407.19108](http://arxiv.org/abs/2407.19108)|null|
|**2024-07-24**|**Neural field equations with time-periodic external inputs and some applications to visual processing**|这项工作的目的是为研究视觉处理任务中的闪烁输入提供一个数学框架。当与几何图案结合时，这些输入会影响并诱发有趣的心理物理现象，如麦凯效应和比洛克-邹效应，在这些效应中，受试者感知到通常由闪烁频率调制的特定余像。由于输入的对称破缺结构，经典分叉理论和多尺度分析技术在我们的背景下不是很有效。因此，我们采用了一种基于Amari型神经场控制理论的输入-输出框架的方法。这使我们能够证明，当受到周期性输入的驱动时，动态会收敛到周期性状态。此外，我们研究了在哪些假设下，这些非线性动力学可以有效地线性化，在这种情况下，我们提出了短程兴奋性和远程抑制性神经元相互作用的积分核的精确近似值。最后，对于集中在具有闪烁背景的视野中心的输入，我们直接将余像中出现的虚幻轮廓的宽度与闪烁频率和抑制强度联系起来。 et.al.|[2407.17294](http://arxiv.org/abs/2407.17294)|null|
|**2024-08-19**|**Fluorescence Diffraction Tomography using Explicit Neural Fields**|在同一样本中同时对荧光标记和无标记的相物体进行成像，可以提供不同和互补的信息。大多数多模式荧光相位成像在透射模式下工作，分别或顺序捕获荧光图像和相位图像，这限制了它们在体内的实际应用。在这里，我们开发了具有显式神经场的荧光衍射断层扫描（FDT），从反射模式下捕获的衍射荧光图像中重建相位物体的3D折射率（RI）。使用FDT成功重建3D RI依赖于四个关键组件：从粗到细的结构、自校准、差分多层渲染模型和部分相干掩模。显式表示与粗到细的结构相结合，实现了高速、高分辨率的重建，而差分多层渲染模型实现了荧光照明的自校准，确保了准确的前向图像预测和RI重建。部分相干掩模有效地解决了相干光模型和部分相干光数据之间的差异。FDT成功地从荧光图像中重建了24个z $-层、1024像素、530美元×530美元×300美元×μm^3$ 体积、1024美元×1024像素的3D培养无标记牛肌管的RI，证明了在体外对体积庞大和异质的生物样本进行高分辨率和高精度的3D RI重建。 et.al.|[2407.16657](http://arxiv.org/abs/2407.16657)|null|

<p align=right>(<a href=#updated-on-20240822>back to top</a>)</p>

[contributors-shield]: https://img.shields.io/github/contributors/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[contributors-url]: https://github.com/Vincentqyw/cv-arxiv-daily/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[forks-url]: https://github.com/Vincentqyw/cv-arxiv-daily/network/members
[stars-shield]: https://img.shields.io/github/stars/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[stars-url]: https://github.com/Vincentqyw/cv-arxiv-daily/stargazers
[issues-shield]: https://img.shields.io/github/issues/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[issues-url]: https://github.com/Vincentqyw/cv-arxiv-daily/issues

