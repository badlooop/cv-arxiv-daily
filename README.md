[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]

## Updated on 2024.08.25
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
|**2024-08-22**|**Subsurface Scattering for 3D Gaussian Splatting**|由于表面下复杂的光传输，由散射材料制成的物体的3D重建和重新照明面临着重大挑战。3D高斯散斑以实时速度引入了高质量的新颖视图合成。虽然3D高斯分布有效地近似了物体的表面，但它们无法捕捉到次表面散射的体积特性。我们提出了一个框架，用于在给定多视图OLAT（一次一盏灯）数据的情况下优化物体的形状和辐射传输场。我们的方法将场景分解为一个表示为3D高斯的显式表面，具有空间变化的BRDF和散射分量的隐式体积表示。一个习得的入射光场解释了阴影。我们通过光线追踪可微渲染联合优化所有参数。我们的方法能够以交互速率进行材质编辑、重新照明和新颖的视图合成。我们展示了在合成数据上的成功应用，并介绍了在光台设置中新获取的多视图多光对象数据集。与之前的工作相比，我们在优化和渲染时间的一小部分上实现了可比或更好的结果，同时实现了对材质属性的详细控制。项目页面https://sss.jdihlmann.com/ et.al.|[2408.12282](http://arxiv.org/abs/2408.12282)|null|
|**2024-08-21**|**Robust 3D Gaussian Splatting for Novel View Synthesis in Presence of Distractors**|3D高斯散斑显示了令人印象深刻的新颖视图合成结果；然而，它很容易受到动态对象的影响，这些对象会污染原本静态场景的输入数据，即所谓的干扰。干扰因素对渲染质量有严重影响，因为它们被表示为与视图相关的效果或导致浮动伪影。我们的目标是在3D高斯优化过程中识别并忽略这些干扰物，以获得干净的重建。为此，我们采取了一种自我监督的方法，在优化过程中查看图像残差，以确定可能被干扰物伪造的区域。此外，我们利用预训练的分割网络来提供对象感知，从而更准确地排除干扰因素。通过这种方式，我们获得了干扰物的分割掩模，以便在损失公式中有效地忽略它们。我们证明，我们的方法对各种干扰物具有鲁棒性，并显著提高了干扰物污染场景的渲染质量，与3D高斯散斑相比，PSNR提高了1.86dB。 et.al.|[2408.11697](http://arxiv.org/abs/2408.11697)|**[link](https://github.com/paulungermann/Robust3DGaussians)**|
|**2024-08-21**|**Pano2Room: Novel View Synthesis from a Single Indoor Panorama**|最近的单视图3D生成方法通过利用从广泛的3D对象数据集中提取的知识取得了重大进展。然而，从单个视图合成3D场景仍然存在挑战，主要是由于现实世界环境的复杂性和高质量先验资源的可用性有限。本文介绍了一种名为Pano2Room的新方法，旨在从单张全景图像中自动重建高质量的3D室内场景。这些全景图像可以使用全景RGBD修复器从任何相机在单个位置的捕获中轻松生成。关键思想是首先从输入全景图构建一个初步网格，并在收集照片级逼真的3D一致伪新颖视图的同时，使用全景RGBD修复器迭代地细化该网格。最后，将精细网格转换为三维高斯散斑场，并用收集到的伪新视图进行训练。该管道能够重建现实世界的3D场景，即使在存在大遮挡的情况下也是如此，并有助于合成具有详细几何形状的照片级逼真新颖视图。已经进行了广泛的定性和定量实验，以验证我们的方法在单全景室内新颖合成方面与最先进的方法相比的优越性。我们的代码和数据可在\url上获得{https://github.com/TrickyGo/Pano2Room}. et.al.|[2408.11413](http://arxiv.org/abs/2408.11413)|**[link](https://github.com/trickygo/pano2room)**|
|**2024-08-20**|**TrackNeRF: Bundle Adjusting NeRF from Sparse and Noisy Views via Feature Tracks**|神经辐射场（NeRF）通常需要许多具有精确姿态的图像来进行精确的新颖视图合成，这并不能反映视图稀疏、姿态嘈杂的真实设置。以前用于学习具有稀疏视图和嘈杂姿态的NeRF的解决方案只考虑与成对视图的局部几何一致性。紧跟运动结构（SfM）中的\textit{束调整}，我们引入了TrackNeRF，以实现更全局一致的几何重建和更精确的姿态优化。TrackNeRF引入了\textit{特征轨迹}，即与\textit{same}3D点对应的\textit{1all}可见视图上的连接像素轨迹。通过强制特征轨迹之间的重投影一致性，TrackNeRF明确鼓励整体3D一致性。通过广泛的实验，TrackNeRF在噪声和稀疏视图重建方面树立了新的基准。特别是，TrackNeRF在各种稀疏和嘈杂的视图设置下，在DTU上的PSNR方面比最先进的BARF和SPARF分别提高了 $\sim8$和$\sim1$ 。该代码可在\href处获得{https://tracknerf.github.io/}. et.al.|[2408.10739](http://arxiv.org/abs/2408.10739)|null|
|**2024-08-19**|**Implicit Gaussian Splatting with Efficient Multi-Level Tri-Plane Representation**|高斯散斑（3DGS）极大地推动了照片级真实感新视图合成的最新进展。然而，3DGS数据的显式性质需要相当大的存储要求，这突显了对更高效数据表示的迫切需求。为了解决这个问题，我们提出了隐式高斯散布（IGS），这是一种创新的混合模型，通过多级三平面架构将显式点云与隐式特征嵌入集成在一起。该架构以不同级别的不同分辨率的2D特征网格为特征，促进了连续的空间域表示，并增强了高斯基元之间的空间相关性。在此基础上，我们引入了一种基于水平的渐进训练方案，该方案结合了显式的空间正则化。该方法利用空间相关性来提高IGS表示的渲染质量和紧凑性。此外，考虑到不同层次的熵变化，我们提出了一种针对点云和二维特征网格量身定制的新型压缩管道。大量的实验评估表明，我们的算法只需几MB就可以提供高质量的渲染，有效地平衡了存储效率和渲染保真度，并产生了与最先进技术竞争的结果。 et.al.|[2408.10041](http://arxiv.org/abs/2408.10041)|null|
|**2024-08-20**|**Gaussian in the Dark: Real-Time View Synthesis From Inconsistent Dark Images Using Gaussian Splatting**|3D高斯散斑最近已经成为一种强大的表示方法，可以使用一致的多视图图像作为输入来合成非凡的新颖视图。然而，我们注意到，在场景未完全照亮的黑暗环境中捕获的图像可能会表现出相当大的亮度变化和多视图不一致性，这对3D高斯散斑技术提出了巨大挑战，并严重降低了其性能。为了解决这个问题，我们提出了高斯DK。观察到不一致主要是由相机成像引起的，我们使用一组各向异性3D高斯表示物理世界的一致辐射场，并设计了一个相机响应模块来补偿多视图不一致。我们还引入了一种基于步长的梯度缩放策略，以约束摄像机附近的高斯分布，使其无法分裂和克隆。在我们提出的基准数据集上的实验表明，Gaussian DK可以产生高质量的渲染，没有重影和浮动伪影，并且明显优于现有方法。此外，我们还可以通过控制曝光水平来合成发光图像，以清楚地显示阴影区域的细节。 et.al.|[2408.09130](http://arxiv.org/abs/2408.09130)|**[link](https://github.com/yec22/Gaussian-DK)**|
|**2024-08-16**|**Correspondence-Guided SfM-Free 3D Gaussian Splatting for NVS**|无运动结构（SfM）预处理相机姿态的新型视图合成（NVS）——称为无SfM方法——对于提高快速响应能力和增强对可变操作条件的鲁棒性至关重要。最近的无SfM方法集成了姿态优化，为联合相机姿态估计和NVS设计了端到端的框架。然而，大多数现有的工作依赖于每像素图像损失函数，如L2损失。在无SfM方法中，不准确的初始姿态会导致失准问题，在每像素图像损失函数的约束下，这会导致梯度过大，导致NVS的优化不稳定和收敛性差。在这项研究中，我们提出了一种用于NVS的无对应引导SfM 3D高斯溅射。我们使用目标和渲染结果之间的对应关系来实现更好的像素对齐，从而优化帧之间的相对姿态。然后，我们应用学习到的姿势来优化整个场景。每个2D屏幕空间像素通过近似表面渲染与其相应的3D高斯相关联，以促进梯度反向传播。实验结果强调了与最先进的基线相比，所提出的方法具有更优的性能和时间效率。 et.al.|[2408.08723](http://arxiv.org/abs/2408.08723)|null|
|**2024-08-16**|**GS-ID: Illumination Decomposition on Gaussian Splatting via Diffusion Prior and Parametric Light Source Optimization**|我们提出了GS-ID，这是一种用于高斯散斑照明分解的新框架，实现了逼真的新视图合成和直观的光编辑。光照分解是一个不适定问题，面临三个主要挑战：1）通常缺乏几何和材料的先验知识；2） 复杂的照明条件涉及多个未知光源；以及3）使用多个光源计算表面着色在计算上是昂贵的。为了应对这些挑战，我们首先引入内在扩散先验来估计基于物理的渲染的属性。然后我们将光照分为环境和直接分量进行联合优化。最后，我们采用延迟渲染来减少计算负载。我们的框架使用可学习的环境图和球面高斯（SG）来参数化地表示光源，从而在高斯散斑上实现可控和逼真的重新照明。广泛的实验和应用表明，GS-ID可以产生最先进的照明分解结果，同时实现更好的几何重建和渲染性能。 et.al.|[2408.08524](http://arxiv.org/abs/2408.08524)|**[link](https://github.com/dukang/gs-id)**|
|**2024-08-15**|**MVInpainter: Learning Multi-View Consistent Inpainting to Bridge 2D and 3D Editing**|新视图合成（NVS）和3D生成最近取得了显著的进步。然而，这些作品主要集中在有限的类别或合成的3D资产上，不鼓励在野外场景中推广到具有挑战性的场景，也不能直接用于2D合成。此外，这些方法严重依赖于相机姿态，限制了它们在现实世界中的应用。为了克服这些问题，我们提出了MVInpainter，将3D编辑重新定义为多视图2D修复任务。具体来说，MVInpainter使用参考引导对多视图图像进行部分修复，而不是从头开始艰难地生成一个全新的视图，这大大简化了野外NVS的难度，并利用了未掩盖的线索而不是明确的姿势条件。为了确保交叉视图的一致性，MVInpainter通过来自运动分量的视频先验和来自级联参考键值关注的外观引导进行了增强。此外，MVInpainter结合了狭缝注意力，以聚合来自未遮蔽区域的高级光流特征，从而通过无姿态训练和推理来控制相机运动。在以对象为中心和面向前的数据集上进行的足够的场景级实验验证了MVInpainter的有效性，包括多种任务，如多视图对象删除、合成、插入和替换。项目页面为https://ewrfcas.github.io/MVInpainter/. et.al.|[2408.08000](http://arxiv.org/abs/2408.08000)|null|
|**2024-08-14**|**Progressive Radiance Distillation for Inverse Rendering with Gaussian Splatting**|我们提出了渐进式辐射蒸馏，这是一种逆向渲染方法，使用蒸馏进度图将基于物理的渲染与基于高斯的辐射场渲染相结合。以多视图图像为输入，我们的方法从预训练的辐射场引导开始，并使用图像拟合过程从辐射场中提取基于物理的光和材料参数。蒸馏进度图被初始化为一个较小的值，这有利于辐射场渲染。在早期迭代中，当拟合的光和材料参数远未收敛时，辐射场回退确保了图像损失梯度的完整性，并避免了吸引拟合不足状态的局部最小值。随着拟合参数的收敛，物理模型逐渐接管，蒸馏过程相应增加。在存在未被物理模型建模的光路的情况下，受影响像素的蒸馏过程永远不会结束，学习到的辐射场会留在最终渲染中。通过这种对物理模型限制的设计容差，我们可以防止未建模的颜色分量泄漏到光和材料参数中，从而减轻重新照明伪影。同时，剩余的辐射场补偿了物理模型的局限性，保证了高质量的新颖视图合成。实验结果表明，在新颖的视图合成和重新照明方面，我们的方法在质量上明显优于最先进的技术。渐进式辐射蒸馏的概念不仅限于高斯散射。我们表明，当采用基于网格的逆渲染方法时，它对显著镜面反射的场景也有积极的影响。 et.al.|[2408.07595](http://arxiv.org/abs/2408.07595)|null|

<p align=right>(<a href=#updated-on-20240825>back to top</a>)</p>

## 3D Reconstruction

|Publish Date|Title|Abstract|PDF|Code|
|---|---|---|---|---|
|**2024-08-22**|**Subsurface Scattering for 3D Gaussian Splatting**|由于表面下复杂的光传输，由散射材料制成的物体的3D重建和重新照明面临着重大挑战。3D高斯散斑以实时速度引入了高质量的新颖视图合成。虽然3D高斯分布有效地近似了物体的表面，但它们无法捕捉到次表面散射的体积特性。我们提出了一个框架，用于在给定多视图OLAT（一次一盏灯）数据的情况下优化物体的形状和辐射传输场。我们的方法将场景分解为一个表示为3D高斯的显式表面，具有空间变化的BRDF和散射分量的隐式体积表示。一个习得的入射光场解释了阴影。我们通过光线追踪可微渲染联合优化所有参数。我们的方法能够以交互速率进行材质编辑、重新照明和新颖的视图合成。我们展示了在合成数据上的成功应用，并介绍了在光台设置中新获取的多视图多光对象数据集。与之前的工作相比，我们在优化和渲染时间的一小部分上实现了可比或更好的结果，同时实现了对材质属性的详细控制。项目页面https://sss.jdihlmann.com/ et.al.|[2408.12282](http://arxiv.org/abs/2408.12282)|null|
|**2024-08-22**|**Transientangelo: Few-Viewpoint Surface Reconstruction Using Single-Photon Lidar**|我们考虑使用激光雷达系统的原始测量值进行少视点3D表面重建的问题。激光雷达通过向目标发射光脉冲并记录反射光的光速时间延迟来捕获3D场景几何形状。然而，传统的激光雷达系统不能输出原始的、捕获的背散射光波形；相反，他们将这些数据预处理成3D点云。由于该过程通常不能准确地模拟系统的噪声统计数据，利用空间先验，或结合有关下游任务的信息，因此它最终会丢弃在反向散射光的原始测量中编码的有用信息。在这里，我们建议利用单光子激光雷达系统从多个视点捕获的原始测量值来优化场景的神经表面表示。这些测量包括时间分辨光子计数直方图或瞬态，它们捕获了皮秒时间尺度上背散射光的信息。此外，我们开发了新的正则化策略，提高了对光子噪声的鲁棒性，实现了每像素少至10个光子的精确表面重建。我们的方法在基于深度图、点云或传统激光雷达的少视点3D重建方面优于其他技术，如模拟和捕获的数据所示。 et.al.|[2408.12191](http://arxiv.org/abs/2408.12191)|null|
|**2024-08-22**|**Unsupervised discovery of the shared and private geometry in multi-view data**|现代应用程序通常利用一个研究主题的多个视图。在神经科学领域，人们对跨多个大脑区域的大规模同步记录越来越感兴趣。理解视图之间的关系（例如，记录的每个区域的神经活动）可以揭示关于每个表示的特征和系统的基本原理。然而，现有的表征这种关系的方法要么缺乏捕捉复杂非线性所需的表现力，要么只描述视图之间共享的方差来源，要么丢弃对解释数据至关重要的几何信息。在这里，我们开发了一种基于非线性神经网络的方法，在给定高维视图的成对样本的情况下，解开这些视图背后的低维共享和私有潜在变量，同时保留内在的数据几何。在多个模拟和真实数据集上，我们证明了我们的方法优于竞争方法。使用模拟的外侧膝状体（LGN）和V1神经元群体，我们展示了我们的模型在不同噪声条件下发现可解释的共享和私有结构的能力。在未旋转和相应但随机旋转的MNIST数字的数据集上，我们恢复了旋转视图的私有延迟，该延迟编码旋转角度，而不管数字类别如何，并将角度表示放在一维流形上，而共享延迟编码数字类别，但不编码旋转角度。将我们的方法应用于小鼠在线性轨道上跑步时海马和前额叶皮层的同时神经像素记录，我们发现了一个低维共享的潜在空间，该空间编码了动物的位置。我们提出我们的方法作为一种通用方法，用于根据解纠缠的共享和私有潜在变量，找到配对数据集的简洁和可解释的描述。 et.al.|[2408.12091](http://arxiv.org/abs/2408.12091)|null|
|**2024-08-21**|**Bimodal Visualization of Industrial X-Ray and Neutron Computed Tomography Data**|先进制造技术创造了越来越复杂的物体，其材料成分往往难以用单一形态来表征。我们的合作领域科学家正在超越传统方法，采用X射线和中子计算机断层扫描来获得互补的表示，有望更好地分辨材料边界。然而，使用两种模式会给可视化带来挑战，需要对双峰传递函数进行复杂的调整，或者需要多个视图。我们与无损评估专家一起设计了一种新颖的交互式双峰可视化方法，以创建工业物体的共同配准X射线和中子采集的组合视图。该系统使用X射线和中子值的二元直方图的自动拓扑分割作为起点，提供了一个简单而有效的界面，可以轻松创建、探索和调整双峰可视化。我们提出了一种具有简单刷牙交互的小部件，使用户能够快速纠正分割的直方图结果。我们的半自动化系统使领域专家能够直观地探索大型双峰数据集，而不需要高级分割算法或可视化技术知识。我们使用合成examp演示我们的方法 et.al.|[2408.11957](http://arxiv.org/abs/2408.11957)|null|
|**2024-08-22**|**DeRainGS: Gaussian Splatting for Enhanced Scene Reconstruction in Rainy Environments**|由于能见度降低和视觉感知失真，在恶劣的降雨条件下进行重建带来了重大挑战。这些条件会严重损害几何地图的质量，而几何地图对于从自主规划到环境监测的应用至关重要。为了应对这些挑战，本研究引入了雨天环境中的3D重建（3DRRE）这一新任务，专门用于解决雨天条件下重建3D场景的复杂性。为了对这项任务进行基准测试，我们构建了HydroViews数据集，该数据集包括以不同强度的雨条和雨滴为特征的合成和现实世界场景图像的不同集合。此外，我们提出了DeRainGS，这是第一种专为恶劣雨天环境中的重建而定制的3DGS方法。在各种降雨场景中进行的广泛实验表明，我们的方法提供了最先进的性能，显著优于现有的无遮挡方法。 et.al.|[2408.11540](http://arxiv.org/abs/2408.11540)|null|
|**2024-08-21**|**MeTTA: Single-View to 3D Textured Mesh Reconstruction with Test-Time Adaptation**|从单视图图像重建3D是一个长期存在的挑战。解决这个问题的一种流行方法是基于学习的方法，但处理不熟悉训练数据的测试用例（分布外；OoD）会带来额外的挑战。为了适应测试时间中看不见的样本，我们提出了MeTTA，一种利用生成先验的测试时间自适应（TTA）。我们设计了3D几何、外观和姿势的联合优化，以处理仅使用单视图图像的OoD病例。然而，通过估计的视点在参考图像和3D形状之间的对准可能是错误的，这会导致模糊。为了解决这种模糊性，我们精心设计了可学习的虚拟相机及其自校准。在我们的实验中，我们证明了MeTTA能够有效地处理现有基于学习的3D重建模型在失败情况下的OoD场景，并能够通过基于物理的渲染（PBR）纹理获得逼真的外观。 et.al.|[2408.11465](http://arxiv.org/abs/2408.11465)|null|
|**2024-08-20**|**Learning Part-aware 3D Representations by Fusing 2D Gaussians and Superquadrics**|低级3D表示，如点云、网格、NeRF和3D高斯，通常用于表示3D对象或场景。然而，人类通常将3D对象或场景视为更高层次的部分或结构的组合，而不是点或体素。将3D表示为语义部分有助于进一步理解和应用。我们的目标是解决部分感知的3D重建，将对象或场景解析为语义部分。本文介绍了一种超二次曲面和二维高斯的混合表示，试图从多视图图像输入中挖掘三维结构线索。同时实现了精确的结构化几何重建和高质量的渲染。我们通过将高斯中心附加到网格中的面上，将网格形式的参数超二次曲面合并到二维高斯中。在训练过程中，迭代优化超二次曲线参数，并相应地对高斯曲线进行变形，从而得到高效的混合表示。一方面，这种混合表示继承了超二次曲面表示不同形状图元的优点，支持场景的灵活部分分解。另一方面，2D高斯被用来模拟复杂的纹理和几何细节，确保高质量的渲染和几何重建。重建完全不受监督。我们对DTU和ShapeNet数据集的数据进行了广泛的实验，该方法将场景分解为合理的部分，优于现有的最先进的方法。 et.al.|[2408.10789](http://arxiv.org/abs/2408.10789)|null|
|**2024-08-19**|**MeshFormer: High-Quality Mesh Generation with 3D-Guided Reconstruction Model**|开放世界3D重建模型最近引起了广泛关注。然而，如果没有足够的3D感应偏差，现有的方法通常需要昂贵的训练成本，并且难以提取高质量的3D网格。在这项工作中，我们介绍了MeshFormer，这是一种稀疏视图重建模型，它明确地利用了3D原生结构、输入指导和训练监督。具体来说，我们不是使用三平面表示，而是将特征存储在3D稀疏体素中，并将变换器与3D卷积相结合，以利用显式的3D结构和投影偏差。除了稀疏视图RGB输入外，我们还要求网络接受输入并生成相应的法线图。输入法线图可以通过二维扩散模型进行预测，这大大有助于指导和细化几何体的学习。此外，通过将符号距离函数（SDF）监督与表面渲染相结合，我们可以直接学习生成高质量的网格，而不需要复杂的多阶段训练过程。通过结合这些显式的3D偏差，MeshFormer可以有效地进行训练，并提供具有细粒度几何细节的高质量纹理网格。它还可以与2D扩散模型集成，以实现快速的单图像到3D和文本到3D任务。项目页面：https://meshformer3d.github.io et.al.|[2408.10198](http://arxiv.org/abs/2408.10198)|null|
|**2024-08-19**|**SpaRP: Fast 3D Object Reconstruction and Pose Estimation from Sparse Views**|开放世界3D生成最近引起了相当大的关注。虽然许多单图像到3D的方法产生了视觉上吸引人的结果，但它们往往缺乏足够的可控性，并且往往会产生可能不符合用户期望的幻觉区域。在这篇论文中，我们探索了一个重要的场景，其中输入由单个对象的一个或几个无滤镜的2D图像组成，重叠很少或没有重叠。我们提出了一种新的方法SpaRP来重建3D纹理网格，并估计这些稀疏视图图像的相对相机姿态。SpaRP从2D扩散模型中提取知识，并对其进行微调，以隐式推断稀疏视图之间的3D空间关系。训练扩散模型，以联合预测已知姿态下物体的相机姿态和多视图图像的替代表示，整合来自输入稀疏视图的所有信息。然后利用这些预测来完成3D重建和姿态估计，重建的3D模型可用于进一步细化输入视图的相机姿态。通过在三个数据集上的广泛实验，我们证明我们的方法不仅在3D重建质量和姿态预测精度方面显著优于基线方法，而且表现出很强的效率。为输入视图生成纹理网格和相机姿态只需要大约20秒。项目页面：https://chaoxu.xyz/sparp. et.al.|[2408.10195](http://arxiv.org/abs/2408.10195)|null|
|**2024-08-15**|**Comparative Evaluation of 3D Reconstruction Methods for Object Pose Estimation**|物体姿态估计对于涉及机器人操纵、导航和增强现实的许多工业应用至关重要。当前的可推广对象姿态估计器，即不需要对每个对象进行训练的方法，依赖于精确的3D模型。主要使用CAD模型，这在实践中很难获得。同时，通常可以获取对象的图像。自然地，这导致了一个问题，即从图像重建的3D模型是否足以促进准确的物体姿态估计。我们的目标是通过提出一个新的基准来衡量3D重建质量对姿态估计精度的影响，从而回答这个问题。我们的基准为对象重建提供了校准图像，这些图像与YCB-V数据集的测试图像进行了配准，用于BOP基准格式下的姿态评估。对多种最先进的3D重建和物体姿态估计方法的详细实验表明，现代重建方法产生的几何形状通常足以进行精确的姿态估计。我们的实验得出了有趣的观察结果：（1）测量3D重建质量的标准指标不一定能指示姿态估计的准确性，这表明需要像我们这样的专用基准。（2） 经典的、非基于学习的方法可以与现代基于学习的重建技术相提并论，甚至可以提供更好的重建时间-姿态精度权衡。（3） 重建模型和CAD模型的性能之间仍存在相当大的差距。为了促进缩小这一差距的研究，我们的基准可在https://github.com/VarunBurde/reconstruction_pose_benchmark}. et.al.|[2408.08234](http://arxiv.org/abs/2408.08234)|**[link](https://github.com/varunburde/reconstruction_pose_benchmark)**|

<p align=right>(<a href=#updated-on-20240825>back to top</a>)</p>

## Diffusion

|Publish Date|Title|Abstract|PDF|Code|
|---|---|---|---|---|
|**2024-08-22**|**Very Extended Ionized Gas Discovered around NGC 1068 with the Circumgalactic H $α$ Spectrograph**|我们使用新委托的环银河H$\alpha$光谱仪（\chas）在NGC 1068周围进行了宽视场、超低表面亮度H$\alpha$发射线测绘。NGC 1068以其活跃的星系核而闻名，该星系核在全局上电离了盘和晕中的气体。线状发射的扩散电离气体分布在整个星系盘上，在星系盘之外发现了大尺度的电离细丝，与中心射流的锥角对齐。我们报告说，在NGC 1068周围发现了一条新的电离气体带，甚至超出了已知的外部丝状结构，距离星系20kpc。该带状物的H$\alpha$表面亮度与明亮的碲线大致相同，范围从$[4-16]$R到天空背景连续体上较暗的区域。与之前的延伸发射不同，带状物与中心射流的当前轴没有很好地对齐。它与NGC 1068晕中的任何星系结构或已知潮汐特征无关，尽管它可能起源于晕中未映射的中性原子或分子气体的较大分布。H$\alpha$中带状发射的形态与NGC 1068周围的扩展紫外发射相关。带状星系中的H$\alpha$与紫外线通量比与NGC 5128、NGC 253和M82光晕中的扩展发射线比相当。带状气体中的H$\alpha$ 过量表明是由缓慢冲击或原位恒星形成、光电离和碰撞电离过程的混合物引起的电离。 et.al.|[2408.12597](http://arxiv.org/abs/2408.12597)|null|
|**2024-08-22**|**xGen-VideoSyn-1: High-fidelity Text-to-Video Synthesis with Compressed Representations**|我们提出了xGen-VideoSyn-1，这是一种文本到视频（T2V）生成模型，能够从文本描述中生成逼真的场景。基于OpenAI的Sora等最新进展，我们探索了潜在扩散模型（LDM）架构，并引入了视频变分自动编码器（VidVAE）。VidVAE在空间和时间上压缩视频数据，显著减少了视觉标记的长度以及与生成长序列视频相关的计算需求。为了进一步解决计算成本问题，我们提出了一种分割合并策略，该策略可以保持视频片段之间的时间一致性。我们的扩散变换器（DiT）模型结合了空间和时间自我关注层，能够在不同的时间框架和纵横比下进行稳健的泛化。我们从一开始就设计了一个数据处理管道，并收集了1300多万对高质量的视频文本对。该流程包括多个步骤，如剪切、文本检测、运动估计、美学评分和基于我们内部视频LLM模型的密集字幕。训练VidVAE和DiT模型分别需要大约40天和642个H100天。我们的型号以端到端的方式支持超过14秒的720p视频生成，并展示了与最先进的T2V型号相比的竞争性能。 et.al.|[2408.12590](http://arxiv.org/abs/2408.12590)|null|
|**2024-08-22**|**Real-Time Video Generation with Pyramid Attention Broadcast**|我们提出了金字塔注意力广播（PAB），这是一种实时、高质量、无需训练的基于DiT的视频生成方法。我们的方法建立在观察到扩散过程中的注意力差异呈U形模式的基础上，表明存在显著的冗余。我们通过以金字塔风格向后续步骤广播注意力输出来缓解这种情况。它根据每个注意力的方差对每个注意力应用不同的广播策略，以获得最佳效率。我们进一步引入广播序列并行，以实现更高效的分布式推理。与基线相比，PAB在三个模型中表现出了卓越的结果，实现了高达720p视频的实时生成。我们预计，我们简单而有效的方法将作为一个强大的基线，并促进未来视频生成的研究和应用。 et.al.|[2408.12588](http://arxiv.org/abs/2408.12588)|**[link](https://github.com/nus-hpc-ai-lab/opendit)**|
|**2024-08-22**|**ssProp: Energy-Efficient Training for Convolutional Neural Networks with Scheduled Sparse Back Propagation**|最近，深度学习取得了显著进展，特别是在生成建模方面，如大型语言模型和概率扩散模型。然而，训练这些模型通常涉及大量的计算资源，需要数十亿petaFLOP。这种高资源消耗导致大量能源使用和巨大的碳足迹，引发了严重的环境问题。反向传播（BP）是训练深度学习模型过程中计算费用的主要来源。为了推进节能训练的研究，并允许在任何机器和设备上进行稀疏学习，我们提出了一种通用的节能卷积模块，可以无缝集成到任何深度学习架构中。具体来说，我们在反向过程中引入了具有额外梯度选择调度器的信道稀疏性，这是基于BP通常密集且效率低下的假设，这可能会导致过拟合和高计算消耗。我们的实验表明，我们的方法减少了40%的计算量，同时潜在地提高了模型性能，并在图像分类和生成任务上得到了验证。这种减少可以在大规模人工智能系统的研发阶段实现显著的节能和更低的碳足迹。此外，我们的方法以不同于Dropout的方式减轻了过度拟合，允许它与Dropout结合，以进一步提高模型性能并减少计算资源的使用。广泛的实验验证了我们的方法可以推广到各种数据集和任务，并且与各种深度学习架构和模块兼容。代码可在以下网址公开获取https://github.com/lujiazho/ssProp. et.al.|[2408.12561](http://arxiv.org/abs/2408.12561)|**[link](https://github.com/lujiazho/ssprop)**|
|**2024-08-22**|**Detecting random bifurcations via rigorous enclosures of large deviations rate functions**|这项工作的主要目标是基于有限时间李雅普诺夫指数的大偏差估计，描述扩散中从均匀到非均匀snychronization的转变。这些可以用李雅普诺夫指数来表征，李雅普诺指数是倾斜（Feynman-Kac）半群生成器的主要特征值。通过计算机辅助证明，我们演示了如何确定这些特征值，并研究了李雅普诺夫矩函数的勒让德-芬尼歇尔变换的速率函数。我们将我们的结果应用于两个案例研究：干叉分叉和二维玩具模型，也考虑了向正渐近李雅普诺夫指数的转变。 et.al.|[2408.12556](http://arxiv.org/abs/2408.12556)|null|
|**2024-08-22**|**Neural Fields and Noise-Induced Patterns in Neurons on Large Disordered Networks**|我们研究了随机图上受时空随机强迫的大维神经网络类的模式形成。在耦合和节点动力学的一般条件下，我们证明了该网络具有严格的平均场极限，类似于Wilson Cowan神经场方程。限制系统的状态变量是神经元活动的均值和方差。我们选择平均场方程易于处理的网络，并使用每个神经元上传入白噪声的扩散强度作为控制参数进行分叉分析。我们在皮质被建模为环的系统中找到了图灵分叉的条件，并在二维皮质模型中产生了噪声诱导螺旋波的数值证据。我们提供了数值证据，证明有限尺寸网络的解弱收敛于平均场模型的解。最后，我们证明了大偏差原理，该原理提供了一种评估有限尺寸效应引起的平均场方程偏差可能性的方法。 et.al.|[2408.12540](http://arxiv.org/abs/2408.12540)|null|
|**2024-08-22**|**Spectral eigenfunction decomposition of a Fokker-Planck operator for relativistic heavy-ion collisions**|提出了一种谱解方法来求解先前开发的非平衡统计模型，该模型描述了相对论重离子碰撞中产生的带电强子的部分热化，从而提高了数值解的准确性。粒子的相空间轨迹被视为漂移扩散随机过程，从而得到单粒子概率分布函数的福克-普朗克方程（FPE）。通过适当的涨落耗散关系，从预期的渐近状态中推导出漂移和扩散系数，然后使用谱本征函数分解对得到的FPE进行数值求解。将计算出的含时粒子分布与大型强子对撞机ATLAS和ALICE合作的Pb-Pb数据进行了比较。 et.al.|[2408.12532](http://arxiv.org/abs/2408.12532)|null|
|**2024-08-22**|**Show-o: One Single Transformer to Unify Multimodal Understanding and Generation**|我们提出了一个统一的转换器，即Show-o，它统一了多模态理解和生成。与完全自回归模型不同，Show-o统一了自回归和（离散）扩散建模，以自适应地处理各种和混合模态的输入和输出。统一模型灵活地支持各种视觉语言任务，包括视觉问答、文本到图像生成、文本引导的修复/外推和混合模态生成。在各种基准测试中，它展示了与现有单个模型相当或更优的性能，具有为理解或生成而定制的等效或更多参数。这显著突显了其作为下一代基础模型的潜力。代码和模型发布于https://github.com/showlab/Show-o. et.al.|[2408.12528](http://arxiv.org/abs/2408.12528)|null|
|**2024-08-22**|**FlexEdit: Marrying Free-Shape Masks to VLLM for Flexible Image Editing**|将视觉大语言模型（VLLM）与扩散模型相结合，为基于人类语言指令执行图像编辑任务提供了一种强大的方法。然而，仅靠语言指令往往无法准确传达用户需求，特别是当用户想要在图像的特定区域添加、替换元素时。幸运的是，遮罩可以有效地指示要编辑的确切位置或元素，而它们要求用户在所需的位置精确地绘制形状，这对用户非常不友好。为了解决这个问题，我们提出了FlexEdit，这是一种端到端的图像编辑方法，利用自由形状掩码和语言指令进行灵活编辑。我们的方法采用VLLM来理解图像内容、掩码和用户指令。此外，我们引入了掩模增强适配器（MEA），它将VLLM的嵌入与图像数据融合在一起，确保掩模信息和模型输出嵌入的无缝集成。此外，我们构建了FSMI Edit，这是一个专门为自由形状掩模量身定制的基准，包括8种自由形状掩膜。大量实验表明，我们的方法在基于LLM的图像编辑中达到了最先进的（SOTA）性能，我们的简单提示技术在其有效性方面脱颖而出。代码和数据可以在以下网址找到https://github.com/A-new-b/flex_edit. et.al.|[2408.12429](http://arxiv.org/abs/2408.12429)|**[link](https://github.com/a-new-b/flex_edit)**|
|**2024-08-22**|**4D Diffusion for Dynamic Protein Structure Prediction with Reference Guided Motion Alignment**|蛋白质结构预测对于理解蛋白质的结构-功能关系、推进生物学研究、促进药物开发和实验设计至关重要。虽然深度学习方法和实验性3D蛋白质结构的扩展加速了结构预测，但蛋白质结构的动态性质受到的关注有限。本研究引入了一种创新的4D扩散模型，该模型结合了分子动力学（MD）模拟数据来学习动态蛋白质结构。我们的方法有以下特点：（1）一个统一的扩散模型，能够利用原子分组和侧链二面角预测生成动态蛋白质结构，包括主链和侧链；（2） 参考网络，其通过整合初始3D蛋白质结构的潜在嵌入来增强结构一致性；以及（3）运动对齐模块，旨在提高多个时间步长的时间结构连贯性。据我们所知，这是第一个基于扩散的模型，旨在同时预测多个时间步长的蛋白质轨迹。对基准数据集的验证表明，我们的模型在32个时间步长内预测含有多达256个氨基酸的蛋白质的动态3D结构方面具有很高的准确性，有效地捕捉了稳定状态下的局部灵活性和显著的构象变化。 et.al.|[2408.12419](http://arxiv.org/abs/2408.12419)|null|

<p align=right>(<a href=#updated-on-20240825>back to top</a>)</p>

## NeRF

|Publish Date|Title|Abstract|PDF|Code|
|---|---|---|---|---|
|**2024-08-22**|**Neural Fields and Noise-Induced Patterns in Neurons on Large Disordered Networks**|我们研究了随机图上受时空随机强迫的大维神经网络类的模式形成。在耦合和节点动力学的一般条件下，我们证明了该网络具有严格的平均场极限，类似于Wilson Cowan神经场方程。限制系统的状态变量是神经元活动的均值和方差。我们选择平均场方程易于处理的网络，并使用每个神经元上传入白噪声的扩散强度作为控制参数进行分叉分析。我们在皮质被建模为环的系统中找到了图灵分叉的条件，并在二维皮质模型中产生了噪声诱导螺旋波的数值证据。我们提供了数值证据，证明有限尺寸网络的解弱收敛于平均场模型的解。最后，我们证明了大偏差原理，该原理提供了一种评估有限尺寸效应引起的平均场方程偏差可能性的方法。 et.al.|[2408.12540](http://arxiv.org/abs/2408.12540)|null|
|**2024-08-19**|**Neural Representation of Shape-Dependent Laplacian Eigenfunctions**|拉普拉斯算子的特征函数在数学物理、工程和几何处理中至关重要。通常，这些是通过对域进行离散化并执行特征分解来计算的，将结果与特定的网格联系起来。然而，这种方法不适合连续参数化的形状。我们提出了一种连续参数化形状空间中本征函数的新表示，其中本征函数是连续依赖于形状参数的空间场，由最小狄利克雷能量、单位范数和相互正交性定义。我们用训练为神经场的多层感知器来实现这一点，将形状参数和域位置映射到特征函数值。一个独特的挑战是强制因果关系的相互正交性，其中因果顺序在形状空间中是不同的。因此，我们的训练方法需要三个相互交织的概念：（1）通过在单位范数约束下最小化狄利克雷能量来同时学习n$本征函数；（2） 在反向传播过程中过滤梯度以强制因果正交性，防止早期特征函数受到后期特征函数的影响；（3） 基于特征值对因果排序进行动态排序，以跟踪特征值曲线交叉。我们在形状族分析、不完整形状的特征函数预测、交互式形状操作和计算高维特征函数等问题上展示了我们的方法，这些问题都是传统方法所不能达到的。 et.al.|[2408.10099](http://arxiv.org/abs/2408.10099)|null|
|**2024-08-20**|**Scene123: One Prompt to 3D Scene Generation via Video-Assisted and Consistency-Enhanced MAE**|随着人工智能生成内容（AIGC）的进步，已经开发了各种方法来从单模式或多模式输入生成文本、图像、视频和3D对象，从而有助于模拟类人认知内容的创建。然而，由于确保模型生成的外推视图之间的一致性所涉及的复杂性，从单个输入生成逼真的大规模场景是一个挑战。受益于最新的视频生成模型和隐式神经表示，我们提出了Scene123，这是一种3D场景生成模型，它不仅通过视频生成框架确保了真实性和多样性，还使用隐式神经场与掩模自编码器（MAE）相结合，有效地确保了视图中看不见区域的一致性。具体来说，我们最初会扭曲输入图像（或从文本生成的图像）以模拟相邻的视图，用MAE模型填充不可见的区域。然而，这些填充图像通常无法保持视图一致性，因此我们利用产生的视图来优化神经辐射场，增强几何一致性。此外，为了进一步增强生成视图的细节和纹理保真度，我们对通过视频生成模型从输入图像中导出的图像采用了基于GAN的Loss。大量实验表明，我们的方法可以从单个提示中生成逼真一致的场景。定性和定量结果都表明，我们的方法超越了现有的最先进的方法。我们展示鼓励视频示例https://yiyingyang12.github.io/Scene123.github.io/. et.al.|[2408.05477](http://arxiv.org/abs/2408.05477)|null|
|**2024-08-07**|**Compact 3D Gaussian Splatting for Static and Dynamic Radiance Fields**|3D高斯飞溅（3DGS）最近成为一种替代表示，它利用基于3D高斯的表示并引入了近似的体积渲染，实现了非常快的渲染速度和有前景的图像质量。此外，后续的研究已成功地将3DGS扩展到动态3D场景，展示了其广泛的应用。然而，由于3DGS及其后续方法需要大量的高斯分布来保持渲染图像的高保真度，这需要大量的内存和存储，因此出现了一个重大的缺点。为了解决这个关键问题，我们特别强调两个关键目标：在不牺牲性能的情况下减少高斯点的数量，以及压缩高斯属性，如视图相关的颜色和协方差。为此，我们提出了一种可学习的掩码策略，该策略在保持高性能的同时显著减少了高斯数。此外，我们提出了一种紧凑但有效的视图相关颜色表示方法，即采用基于网格的神经场，而不是依赖球谐函数。最后，我们学习码本，通过残差矢量量化来紧凑地表示几何和时间属性。通过量化和熵编码等模型压缩技术，我们始终表明，与静态场景的3DGS相比，存储空间减少了25倍以上，渲染速度提高了25倍，同时保持了场景表示的质量。对于动态场景，与现有的最先进方法相比，我们的方法实现了超过12倍的存储效率，并保留了高质量的重建。我们的工作为3D场景表示提供了一个全面的框架，实现了高性能、快速训练、紧凑性和实时渲染。我们的项目页面可在https://maincold2.github.io/c3dgs/. et.al.|[2408.03822](http://arxiv.org/abs/2408.03822)|null|
|**2024-08-07**|**PRTGS: Precomputed Radiance Transfer of Gaussian Splats for Real-Time High-Quality Relighting**|我们提出了高斯斑点的预计算辐射转移（PRTGS），这是一种在低频照明环境中用于高斯斑点的实时高质量重新照明方法，通过预计算3D高斯斑点的辐射转移来捕获柔和的阴影和相互反射。现有的研究表明，在动态照明场景中，3D高斯溅射（3DGS）的效率优于神经场。然而，目前基于3DGS的重新照明方法仍然难以实时计算动态光的高质量阴影和间接照明，导致渲染结果不切实际。我们通过预先计算复杂传递函数（如阴影）所需的昂贵传输模拟来解决这个问题，得到的传递函数表示为每个高斯斑点的密集向量集或矩阵集。我们介绍了针对训练和渲染阶段量身定制的不同预计算方法，以及针对3D高斯斑点的独特光线追踪和间接照明预计算技术，以加快训练速度并计算与环境光相关的准确间接照明。实验分析表明，我们的方法在保持有竞争力的训练时间的同时实现了最先进的视觉质量，并允许以1080p分辨率对动态光和相对复杂的场景进行高质量的实时（30+fps）重新照明。 et.al.|[2408.03538](http://arxiv.org/abs/2408.03538)|null|
|**2024-08-01**|**Neural Octahedral Field: Octahedral prior for simultaneous smoothing and sharp edge regularization**|神经隐式表示，将距离函数参数化为坐标神经场，已成为解决无方向点云表面重建的有前景的前沿。为了确保方向一致，现有的方法侧重于正则化距离函数的梯度，例如将其约束为单位范数，最小化其散度，或将其与对应于零特征值的Hessian特征向量对齐。然而，在存在大扫描噪声的情况下，它们往往要么过拟合噪声输入，要么产生过于平滑的重建。在这项工作中，我们建议利用六面体网格中产生的八面体框架的球谐表示，在一种新的神经场变体——八面体场下指导曲面重建。当约束为平滑时，该字段会自动捕捉到几何特征，并在折痕上插值时自然保留锐角。通过同时拟合和平滑隐式几何旁边的八面体场，它的行为类似于双边滤波，从而在保持锐边的同时实现平滑重建。尽管是纯逐点操作，但我们的方法在广泛的实验中表现优于各种传统和神经方法，并且与需要正常和数据先验的方法非常有竞争力。我们的全面实施可在以下网址获得：https://github.com/Ankbzpx/frame-field. et.al.|[2408.00303](http://arxiv.org/abs/2408.00303)|**[link](https://github.com/ankbzpx/frame-field)**|
|**2024-07-30**|**Neural Fields for Continuous Periodic Motion Estimation in 4D Cardiovascular Imaging**|时间分辨三维血流MRI（4D血流MRI）提供了一种独特的非侵入性解决方案，用于可视化和量化主动脉弓等血管中的血流动力学。然而，由于难以获得完整的周期分割，目前大多数动脉4D血流MRI分析方法使用静态动脉壁。为了克服这一局限性，我们提出了一种基于神经场的方法，可以直接估计整个心动周期中连续的周期性壁变形。对于3D+时间成像数据集，我们优化了表示时间依赖速度矢量场（VVF）的隐式神经表示（INR）。ODE求解器用于将VVF集成到变形矢量场（DVF）中，该矢量场可以随着时间的推移使图像、分割掩模或网格变形，从而可视化和量化局部壁运动模式。为了正确反映3D+时间心血管数据的周期性，我们以两种方式施加周期性。首先，通过定期对输入到INR的时间进行编码，从而对VVF进行编码。其次，通过规范DVF。我们证明了这种方法在不同周期模式的合成数据、心电图门控CT和4D血流MRI数据上的有效性。所获得的方法可用于改进4D血流MRI分析。 et.al.|[2407.20728](http://arxiv.org/abs/2407.20728)|null|
|**2024-07-29**|**Aero-Nef: Neural Fields for Rapid Aircraft Aerodynamics Simulations**|本文提出了一种基于隐式神经表示（INR）在网格域上学习稳态流体动力学模拟替代模型的方法。所提出的模型可以直接应用于不同流动条件下的非结构化域，处理非参数3D几何变化，并推广到测试时看不见的形状。基于坐标的公式自然会导致离散化的鲁棒性，从而在计算成本（内存占用和训练时间）和精度之间实现了极好的权衡。该方法在两个工业相关应用中得到了验证：跨音速翼型上二维可压缩流的RANS数据集和三维机翼上表面压力分布的数据集，包括形状、流入条件和控制表面偏转变化。在所考虑的测试用例中，与最先进的图神经网络架构相比，我们的方法实现了三倍多的测试误差，并显著改善了看不见的几何形状的泛化误差。值得注意的是，该方法在RANS跨音速翼型数据集上的推理速度比高保真求解器快五个数量级。代码可在以下网址获得https://gitlab.isae-supaero.fr/gi.catalani/aero-nepf et.al.|[2407.19916](http://arxiv.org/abs/2407.19916)|**[link](https://gitlab.isae-supaero.fr/gi.catalani/aero-nepf)**|
|**2024-07-26**|**ObjectCarver: Semi-automatic segmentation, reconstruction and separation of 3D objects**|隐式神经场在从多幅图像重建3D表面方面取得了显著进展；然而，在分离场景中的单个对象时，他们遇到了挑战。之前的工作试图通过引入一个框架来解决这个问题，该框架为N个对象中的每一个同时训练单独的带符号距离场（SDF），并使用正则化项来防止对象重叠。然而，所有这些方法都需要提供分割掩模，这并不总是容易获得的。我们介绍了我们的方法ObjectCarver，来解决在单个视图中从点击输入中分离对象的问题。给定摆出的多视图图像和一组用户输入点击来提示分割单个对象，我们的方法将场景分解为单独的对象，并为每个对象重建高质量的3D表面。我们引入了一个损失函数，可以防止漂浮物，避免因遮挡而造成不适当的雕刻。此外，我们引入了一种新的场景初始化方法，与之前的方法相比，该方法在保留几何细节的同时显著加快了过程。尽管不需要地面真实掩模或单眼线索，但我们的方法在定性和定量上都优于基线。此外，我们引入了一个新的基准数据集进行评估。 et.al.|[2407.19108](http://arxiv.org/abs/2407.19108)|null|
|**2024-07-24**|**Neural field equations with time-periodic external inputs and some applications to visual processing**|这项工作的目的是为研究视觉处理任务中的闪烁输入提供一个数学框架。当与几何图案结合时，这些输入会影响并诱发有趣的心理物理现象，如麦凯效应和比洛克-邹效应，在这些效应中，受试者感知到通常由闪烁频率调制的特定余像。由于输入的对称破缺结构，经典分叉理论和多尺度分析技术在我们的背景下不是很有效。因此，我们采用了一种基于Amari型神经场控制理论的输入-输出框架的方法。这使我们能够证明，当受到周期性输入的驱动时，动态会收敛到周期性状态。此外，我们研究了在哪些假设下，这些非线性动力学可以有效地线性化，在这种情况下，我们提出了短程兴奋性和远程抑制性神经元相互作用的积分核的精确近似值。最后，对于集中在具有闪烁背景的视野中心的输入，我们直接将余像中出现的虚幻轮廓的宽度与闪烁频率和抑制强度联系起来。 et.al.|[2407.17294](http://arxiv.org/abs/2407.17294)|null|

<p align=right>(<a href=#updated-on-20240825>back to top</a>)</p>

[contributors-shield]: https://img.shields.io/github/contributors/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[contributors-url]: https://github.com/Vincentqyw/cv-arxiv-daily/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[forks-url]: https://github.com/Vincentqyw/cv-arxiv-daily/network/members
[stars-shield]: https://img.shields.io/github/stars/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[stars-url]: https://github.com/Vincentqyw/cv-arxiv-daily/stargazers
[issues-shield]: https://img.shields.io/github/issues/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[issues-url]: https://github.com/Vincentqyw/cv-arxiv-daily/issues

