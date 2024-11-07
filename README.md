[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]

## Updated on 2024.11.07
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
|**2024-11-06**|**Structure Consistent Gaussian Splatting with Matching Prior for Few-shot Novel View Synthesis**|尽管新型视图合成取得了实质性进展，但现有的方法，无论是基于神经辐射场（NeRF）还是最近的3D高斯散斑（3DGS），在输入变得稀疏时都会出现严重退化。人们已经做出了许多努力来缓解这个问题，但他们仍然难以有效地综合出令人满意的结果，特别是在大型场景中。本文提出了SCGaussian，这是一种使用匹配先验来学习3D一致场景结构的结构一致高斯散点方法。考虑到高斯属性的高度相互依赖性，我们在两个方面优化了场景结构：渲染几何体，更重要的是高斯基元的位置，由于非结构特性，高斯基元在普通3DGS中很难直接受到约束。为了实现这一点，我们提出了一种混合高斯表示法。除了普通的非结构高斯基元外，我们的模型还包括基于光线的高斯基元，这些基元绑定到匹配的光线上，其位置的优化沿光线受到限制。因此，我们可以利用匹配对应关系直接强制这些高斯基元的位置收敛到光线相交的表面点。在面向前方、周围和复杂的大型场景上进行的广泛实验表明，我们的方法具有最先进的性能和高效率。代码可在以下网址获得https://github.com/prstrive/SCGaussian. et.al.|[2411.03637](http://arxiv.org/abs/2411.03637)|**[link](https://github.com/prstrive/scgaussian)**|
|**2024-11-05**|**FewViewGS: Gaussian Splatting with Few View Matching and Multi-stage Training**|随着神经辐射场（NeRF）的引入，以及最近3D高斯散斑的引入，从图像合成新视图的领域得到了快速发展。高斯散斑因其高效性和准确渲染新视图的能力而被广泛采用。虽然高斯散斑在有足够数量的训练图像可用时表现良好，但其非结构化显式表示在输入图像稀疏的情况下往往会过拟合，导致渲染性能不佳。为了解决这个问题，我们提出了一种基于3D高斯的新颖视图合成方法，该方法使用稀疏输入图像，可以从训练图像未覆盖的视点准确地渲染场景。我们提出了一种多阶段训练方案，该方案对新视图施加了基于匹配的一致性约束，而不依赖于预训练的深度估计或扩散模型。这是通过使用可用训练图像的匹配来监督在具有颜色、几何和语义损失的训练帧之间采样的新视图的生成来实现的。此外，我们为3D高斯模型引入了一种局部保持正则化方法，通过保留场景的局部颜色结构来消除渲染伪影。对合成数据集和真实世界数据集的评估表明，与现有的最先进方法相比，我们的方法在少镜头新视图合成方面具有竞争力或优越的性能。 et.al.|[2411.02229](http://arxiv.org/abs/2411.02229)|null|
|**2024-11-03**|**InstantGeoAvatar: Effective Geometry and Appearance Modeling of Animatable Avatars from Monocular Video**|我们提出了InstantGeoAvatar，这是一种从单眼视频中高效学习可设置动画的隐式人类化身的详细3D几何和外观的方法。我们的关键观察是，优化哈希网格编码来表示人类受试者的有符号距离函数（SDF）充满了不稳定性和糟糕的局部最小值。因此，我们提出了一种有原则的几何感知SDF正则化方案，该方案无缝融入体绘制管道，并增加了可忽略的计算开销。我们的正则化方案明显优于之前在哈希网格上训练SDF的方法。我们在短短五分钟的训练时间内，在几何重建和新颖的视图合成方面取得了有竞争力的结果，与之前工作所需的几个小时相比，这是一个显著的减少。InstantGeoAvatar代表了实现虚拟化身交互式重建的重大飞跃。 et.al.|[2411.01512](http://arxiv.org/abs/2411.01512)|**[link](https://github.com/alvaro-budria/InstantGeoAvatar)**|
|**2024-11-02**|**AquaFuse: Waterbody Fusion for Physics Guided View Synthesis of Underwater Scenes**|我们介绍了AquaFuse的概念，这是一种基于物理的方法，用于合成水下图像中的水体特性。我们为水体融合制定了一个封闭的解决方案，有助于实现逼真的数据增强和几何一致的水下场景渲染。AquaFuse利用水下光传播的物理特性，将水体从一个场景合成到另一个场景的对象内容。与数据驱动的样式转换不同，AquaFuse保留了输入场景中的深度一致性和对象几何体。我们通过在各种水下场景上的综合实验验证了这一独特功能。我们发现AquaFused图像保留了输入场景94%以上的深度一致性和90-95%的结构相似性。我们还证明，它通过在适应固有水体融合过程的同时保留对象几何形状来生成精确的3D视图合成。AquaFuse为水下成像和机器人视觉应用开辟了一个新的研究方向，即通过几何保持风格转换进行数据增强。 et.al.|[2411.01119](http://arxiv.org/abs/2411.01119)|null|
|**2024-11-01**|**CityGaussianV2: Efficient and Geometrically Accurate Reconstruction for Large-Scale Scenes**|最近，3D高斯散斑（3DGS）彻底改变了辐射场重建，展现了高效高保真的新型视图合成。然而，由于3DGS的非结构化特性，准确表示曲面，特别是在大型和复杂的场景中，仍然是一个重大挑战。在本文中，我们提出了CityGaussianV2，这是一种用于大规模场景重建的新方法，可以解决与几何精度和效率相关的关键挑战。基于二维高斯散斑（2DGS）良好的泛化能力，我们解决了它的收敛性和可扩展性问题。具体而言，我们实现了一种基于分解梯度的致密化和深度回归技术，以消除模糊伪影并加速收敛。为了扩大规模，我们引入了一种伸长滤波器，可以减轻2DGS退化引起的高斯计数爆炸。此外，我们针对并行训练优化了CityGaussian管道，实现了高达10 $times$ 的压缩，至少节省了25%的训练时间，内存使用量减少了50%。我们还建立了大规模场景下的标准几何基准。实验结果表明，我们的方法在视觉质量、几何精度以及存储和训练成本之间取得了良好的平衡。项目页面可在https://dekuliutesla.github.io/CityGaussianV2/. et.al.|[2411.00771](http://arxiv.org/abs/2411.00771)|null|
|**2024-10-31**|**Self-Ensembling Gaussian Splatting for Few-shot Novel View Synthesis**|3D高斯散斑（3DGS）在新颖视图合成（NVS）方面表现出了显著的有效性。然而，当使用稀疏姿态视图进行训练时，3DGS模型往往会过拟合，从而限制了其对更广泛姿态变化的泛化能力。在本文中，我们通过引入自组装高斯散斑（SE-GS）方法来缓解过拟合问题。我们提出了两个高斯散斑模型，分别命名为 $\mathbf{\Sigma}$-模型和$\mathbf{\Delta}$-模式。$\mathbf{\Sigma}$-模型是在推理过程中生成新视图图像的主要模型。在训练阶段，$\mathbf{\Sigma}$-模型通过不确定性感知扰动策略被引导远离特定的局部最优值。我们根据不同训练步骤中新视图渲染的不确定性动态扰动$\mathbf{\Delta}$-模型，从而在不增加额外训练成本的情况下从高斯参数空间中采样出不同的时间模型。通过惩罚$\mathbf{\Sigma}$-模型和时间样本之间的差异，使$\mathbf{\Sigma}$-模式的几何形状正则化。因此，我们的SE-GS对大量高斯散斑模型进行了有效和高效的正则化，从而得到了一个鲁棒的集成，即$\mathbf{\Sigma}$ -模型。在LLFF、Mip-NeRF360、DTU和MVImgNet数据集上的实验结果表明，我们的方法在很少的镜头训练视图下提高了NVS质量，优于现有的最先进方法。代码发布于https://github.com/sailor-z/SE-GS. et.al.|[2411.00144](http://arxiv.org/abs/2411.00144)|null|
|**2024-10-31**|**No Pose, No Problem: Surprisingly Simple 3D Gaussian Splats from Sparse Unposed Images**|我们介绍了NoPoSplat，这是一种前馈模型，能够从\textit{unfosed}稀疏多视图图像中重建由3D高斯参数化的3D场景。我们的模型仅使用光度损失进行训练，在推理过程中实现了实时3D高斯重建。为了在重建过程中消除对精确姿态输入的需求，我们将一个输入视图的局部相机坐标锚定为规范空间，并训练网络预测该空间内所有视图的高斯基元。这种方法避免了将高斯基元从局部坐标转换到全局坐标系的需要，从而避免了与每帧高斯和姿态估计相关的误差。为了解决尺度模糊问题，我们设计并比较了各种内在嵌入方法，最终选择将相机内在转换为令牌嵌入，并将其与图像令牌连接作为模型的输入，从而实现准确的场景尺度预测。我们利用重建的3D高斯分布进行新的视图合成和姿态估计任务，并提出了一种两阶段粗到细的流水线来进行精确的姿态估计。实验结果表明，与需要姿态的方法相比，我们的无姿态方法可以实现更优的新颖视图合成质量，特别是在输入图像重叠有限的情况下。对于姿态估计，我们的方法在没有地面真实深度或显式匹配损失的情况下进行训练，显著优于最先进的方法，并有了实质性的改进。这项工作在无姿态通用3D重建方面取得了重大进展，并证明了其适用于现实世界场景。代码和训练模型可在以下网址获得https://noposplat.github.io/. et.al.|[2410.24207](http://arxiv.org/abs/2410.24207)|**[link](https://github.com/cvg/NoPoSplat)**|
|**2024-11-01**|**GeoSplatting: Towards Geometry Guided Gaussian Splatting for Physically-based Inverse Rendering**|我们考虑了使用3D高斯散斑（3DGS）表示的基于物理的逆渲染问题。虽然最近的3DGS方法在新视图合成（NVS）方面取得了显著成果，但准确捕捉高保真几何体、物理可解释的材质和照明仍然具有挑战性，因为它需要精确的几何建模来提供精确的表面法线，以及基于物理的渲染（PBR）技术来确保正确的材质和光照解纠缠。以前的3DGS方法诉诸于近似曲面法线，但经常难以处理有噪声的局部几何，导致法线估计不准确和材质光照分解次优。本文介绍了GeoSplatting，这是一种新的混合表示，它通过显式几何引导和可微PBR方程来增强3DGS。具体来说，我们将等值面和3DGS连接在一起，首先从标量场中提取等值面网格，然后将其转换为3DGS点，并以完全可微的方式为它们制定PBR方程。在GeoSplatting中，3DGS基于网格几何，实现了精确的表面法线建模，这有助于使用PBR框架进行材料分解。这种方法进一步保持了3DGS的NVS的效率和质量，同时确保了等值面的精确几何形状。对不同数据集的综合评估表明了GeoSplatting的优越性，在定量和定性方面都始终优于现有方法。 et.al.|[2410.24204](http://arxiv.org/abs/2410.24204)|null|
|**2024-10-31**|**GaussianMarker: Uncertainty-Aware Copyright Protection of 3D Gaussian Splatting**|3D高斯散斑（3DGS）已成为获取3D资产的关键方法。为了保护这些资产的版权，可以应用数字水印技术将所有权信息谨慎地嵌入3DGS模型中。然而，现有的网格、点云和隐式辐射场的水印方法不能直接应用于3DGS模型，因为3DGS模型使用具有不同结构的显式3D高斯分布，不依赖于神经网络。在预训练的3DGS上直接嵌入水印会导致渲染图像明显失真。在我们的工作中，我们提出了一种基于不确定性的方法，该方法限制了模型参数的扰动，以实现3DGS的不可见水印。在消息解码阶段，即使在各种形式的3D和2D失真下，也可以从3D高斯和2D渲染图像中可靠地提取版权消息。我们在Blender、LLFF和MipNeRF-360数据集上进行了广泛的实验，以验证我们提出的方法的有效性，并在消息解码精度和视图合成质量方面展示了最先进的性能。 et.al.|[2410.23718](http://arxiv.org/abs/2410.23718)|null|
|**2024-10-31**|**Epipolar-Free 3D Gaussian Splatting for Generalizable Novel View Synthesis**|广义3D高斯分裂（3DGS）可以以前馈推理的方式从稀疏视图观测中重建新的场景，消除了传统3DGS中对场景特定再训练的需要。然而，现有的方法严重依赖于极线先验，这在复杂的现实世界场景中可能不可靠，特别是在非重叠和遮挡的区域。在本文中，我们提出了eFreeSplat，这是一种基于3DGS的高效前馈模型，用于独立于极线约束的可推广新型视图合成。为了增强具有3D感知的多视图特征提取，我们在大规模数据集上采用了具有跨视图完成预训练的自监督视觉变换器（ViT）。此外，我们引入了一种迭代交叉视图高斯对齐方法，以确保不同视图之间的深度尺度一致。我们的eFreeSplat代表了一种可推广的新颖视图合成的创新方法。与现有的纯无几何方法不同，eFreeSplat更侧重于通过跨视图预训练提供3D先验来实现无极线特征匹配和编码。我们使用RealEstate10K和ACID数据集在宽基线新视图合成任务上评估eFreeSplat。大量实验表明，eFreeSplat超越了依赖极线先验的最先进基线，实现了卓越的几何重建和新颖的视图合成质量。项目页面：https://tatakai1.github.io/efreesplat/. et.al.|[2410.22817](http://arxiv.org/abs/2410.22817)|null|

<p align=right>(<a href=#updated-on-20241107>back to top</a>)</p>

## 3D Reconstruction

|Publish Date|Title|Abstract|PDF|Code|
|---|---|---|---|---|
|**2024-11-06**|**These Maps Are Made by Propagation: Adapting Deep Stereo Networks to Road Scenarios with Decisive Disparity Diffusion**|立体匹配已成为路面3D重建的一种经济高效的解决方案，在提高计算效率和准确性方面受到了广泛关注。本文介绍了决定性视差扩散（D3Stereo），标志着对密集深度特征匹配的首次探索，该匹配将预训练的深度卷积神经网络（DCNN）应用于以前看不见的道路场景。成本量金字塔最初是使用不同层次的学习表示创建的。随后，采用了一种新的递归双边滤波算法来聚合这些成本。D3Stereo的一个关键创新在于其交替的决定性视差扩散策略，其中采用尺度内扩散来完成稀疏视差图像，而尺度间继承为更高分辨率提供了有价值的先验信息。在我们创建的UDTIRI立体和立体道路数据集上进行的广泛实验强调了D3Stereo策略在适应预训练DCNN方面的有效性，以及与专门为路面3D重建设计的所有其他基于显式编程的算法相比的卓越性能。在Middlebury数据集上进行的额外实验，以及在ImageNet数据库上预训练的骨干DCNN，进一步验证了D3Stereo策略在解决一般立体匹配问题方面的多功能性。 et.al.|[2411.03717](http://arxiv.org/abs/2411.03717)|null|
|**2024-11-05**|**Exploring Seasonal Variability in the Context of Neural Radiance Fields for 3D Reconstruction on Satellite Imagery**|在这项工作中，研究了应用于卫星图像的神经辐射场（NeRF）的季节预测能力。该研究侧重于卫星数据的利用，探讨了计算机视觉中的一种新方法Sat-NeRF在预测不同月份的季节变化方面的表现。通过综合分析和可视化，该研究考察了该模型捕捉和预测季节变化的能力，突出了具体的挑战和优势。结果展示了太阳方向对预测的影响，揭示了季节过渡中的细微细节，如积雪、颜色准确性和不同景观中的纹理表示。鉴于这些结果，我们提出了Planet NeRF，这是Sat NeRF的扩展，能够通过一组月份嵌入向量来纳入季节变化。比较评估表明，在存在季节变化的情况下，Planet NeRF的表现优于之前的模型。广泛的评估与提出的方法相结合，为该领域的未来研究提供了有前景的途径。 et.al.|[2411.02972](http://arxiv.org/abs/2411.02972)|null|
|**2024-11-05**|**LVI-GS: Tightly-coupled LiDAR-Visual-Inertial SLAM using 3D Gaussian Splatting**|3D高斯散斑（3DGS）在快速渲染和高保真映射方面显示出了其能力。本文介绍了LVI-GS，这是一种与3DGS紧密耦合的LiDAR视觉惯性映射框架，它利用LiDAR和图像传感器的互补特性来捕获3D场景的几何结构和视觉细节。为此，我们从彩色LiDAR点初始化3D高斯分布，并使用可微渲染进行优化。为了实现高保真映射，我们引入了一种基于金字塔的训练方法，以有效学习多级特征，并结合LiDAR测量得出的深度损失来提高几何特征感知。通过精心设计的高斯映射扩展、关键帧选择、线程管理和自定义CUDA加速策略，我们的框架实现了实时照片级逼真映射。进行了数值实验，以评估我们的方法与最先进的3D重建系统相比的优越性能。 et.al.|[2411.02703](http://arxiv.org/abs/2411.02703)|null|
|**2024-11-04**|**MVPaint: Synchronized Multi-View Diffusion for Painting Anything 3D**|纹理是3D资产制作工作流程中的关键步骤，它增强了3D资产的视觉吸引力和多样性。尽管最近在文本到纹理（T2T）生成方面取得了进展，但现有的方法通常会产生次优结果，主要是由于局部不连续性、多个视图之间的不一致性以及它们对UV展开结果的严重依赖。为了应对这些挑战，我们提出了一种名为MVPaint的新一代细化3D纹理框架，该框架可以生成高分辨率、无缝的纹理，同时强调多视图一致性。MVPaint主要由三个关键模块组成。1） 同步多视图生成（SMG）。给定一个3D网格模型，MVPaint首先通过使用SMG模型同时生成多视图图像，这会导致由于缺少观察而导致未涂漆部分的粗糙纹理结果。2） 空间感知3D内绘（S3I）。为了确保完整的3D纹理，我们引入了S3I方法，该方法专门用于有效地对以前未观察到的区域进行纹理处理。3） 紫外线细化（UVR）。此外，MVPaint采用UVR模块来提高UV空间中的纹理质量，该模块首先执行UV空间超分辨率，然后执行空间感知接缝平滑算法，以修正由UV展开引起的空间纹理不连续性。此外，我们分别基于Objaverse数据集和整个GSO数据集中选定的高质量3D网格，建立了两个T2T评估基准：Objaverce T2T基准和GSO T2T基准。大量的实验结果表明，MVPaint超越了现有的最先进的方法。值得注意的是，MVPaint可以生成高保真纹理，同时将Janus问题降至最低，并大大增强了交叉视图的一致性。 et.al.|[2411.02336](http://arxiv.org/abs/2411.02336)|null|
|**2024-11-04**|**Next Best View For Point-Cloud Model Acquisition: Bayesian Approximation and Uncertainty Analysis**|Next Best View问题是机器人学中广泛研究的计算机视觉问题。为了解决这个问题，多年来已经提出了几种方法。最近，一些人提出使用深度学习模型。借助深度学习模型获得的预测自然会有一些不确定性。尽管如此，标准模型不允许对其进行量化。然而，贝叶斯估计理论有助于证明丢弃层允许估计神经网络中的预测不确定性。这项工作将基于点网的神经网络应用于下一最佳视图（PC-NBV）。它将丢弃层整合到模型的架构中，从而允许计算与其预测相关的不确定性估计。这项工作的目的是提高网络正确预测下一个最佳视点的准确性，提出一种使3D重建过程更高效的方法。获得了两个能够分别反映预测误差和准确性的不确定度测量值。通过识别和忽略具有高不确定性的预测，这些方法可以减少模型的误差，并将其准确性从30%提高到80%。还提出了另一种直接使用这些不确定性度量来改进最终预测的方法。然而，它显示出非常残余的改善。 et.al.|[2411.01734](http://arxiv.org/abs/2411.01734)|null|
|**2024-10-31**|**Spherical bias on the 3D reconstruction of the ICM density profile in galaxy clusters**|星系团的X射线观测通常用于推导ICM热力学特性（如密度和温度）的径向分布。然而，观测只允许我们访问投影在天球上的量，因此有必要对ICM的3D分布进行假设。通常，假设为球形几何。本文的目的是确定在簇子结构未被掩盖的情况下，这种近似对簇样本ICM密度径向分布的重建和密度分布的内在散射的偏差。我们使用了98个模拟集群，我们知道这些集群的三维ICM分布来自“三百”项目。对于每个星团，我们通过沿40条不同的视线投影星团来模拟40次不同的观测。我们假设ICM呈球形分布，从每次观测中提取ICM密度分布。然后，对于每条视线，我们考虑了样品上的平均密度分布，并将其与模拟给出的3D密度分布进行了比较。通过考虑观测量和输入量之间的比率，推导出密度分布上的球面偏差。我们还研究了执行相同程序时密度分布的固有散射的偏差。我们发现，对于 $R\lesssim R_{500}$，密度分布$b_n$的偏差小于$10\%$，而对于较大的半径，偏差增加到$\sim 50\%$。对于$R\approxic R_{500}$，内在散射分布的偏差$b_s$达到了$\approxist 100\%$的值。对这两个分析量的偏差在很大程度上取决于对象的形态：对于没有显示大规模子结构的簇，$b_n$和$b_s$都减少了2倍，相反，对于显示大规模子结构化的系统，$b_n$和$b_s$ 都显著增加。[删节] et.al.|[2411.00092](http://arxiv.org/abs/2411.00092)|null|
|**2024-10-31**|**No Pose, No Problem: Surprisingly Simple 3D Gaussian Splats from Sparse Unposed Images**|我们介绍了NoPoSplat，这是一种前馈模型，能够从\textit{unfosed}稀疏多视图图像中重建由3D高斯参数化的3D场景。我们的模型仅使用光度损失进行训练，在推理过程中实现了实时3D高斯重建。为了在重建过程中消除对精确姿态输入的需求，我们将一个输入视图的局部相机坐标锚定为规范空间，并训练网络预测该空间内所有视图的高斯基元。这种方法避免了将高斯基元从局部坐标转换到全局坐标系的需要，从而避免了与每帧高斯和姿态估计相关的误差。为了解决尺度模糊问题，我们设计并比较了各种内在嵌入方法，最终选择将相机内在转换为令牌嵌入，并将其与图像令牌连接作为模型的输入，从而实现准确的场景尺度预测。我们利用重建的3D高斯分布进行新的视图合成和姿态估计任务，并提出了一种两阶段粗到细的流水线来进行精确的姿态估计。实验结果表明，与需要姿态的方法相比，我们的无姿态方法可以实现更优的新颖视图合成质量，特别是在输入图像重叠有限的情况下。对于姿态估计，我们的方法在没有地面真实深度或显式匹配损失的情况下进行训练，显著优于最先进的方法，并有了实质性的改进。这项工作在无姿态通用3D重建方面取得了重大进展，并证明了其适用于现实世界场景。代码和训练模型可在以下网址获得https://noposplat.github.io/. et.al.|[2410.24207](http://arxiv.org/abs/2410.24207)|**[link](https://github.com/cvg/NoPoSplat)**|
|**2024-10-31**|**LBurst: Learning-Based Robotic Burst Feature Extraction for 3D Reconstruction in Low Light**|无人机彻底改变了航空成像、测绘和灾难恢复领域。然而，无人机在低光照条件下的部署受到其机载摄像头产生的图像质量的限制。在这篇论文中，我们提出了一种学习架构，通过在突发中寻找特征来改善低光条件下的3D重建。我们的方法通过检测和描述低信噪比图像中的高质量真实特征和较少的虚假特征来增强视觉重建。我们证明，我们的方法能够在毫勒克斯照明下处理具有挑战性的场景，使其朝着夜间和极低光照应用（如地下采矿和搜救行动）的无人机迈出了重要一步。 et.al.|[2410.23522](http://arxiv.org/abs/2410.23522)|null|
|**2024-10-30**|**PointRecon: Online Point-based 3D Reconstruction via Ray-based 2D-3D Matching**|我们提出了一种新的基于点的在线单目RGB视频三维重建方法。我们的模型保持了场景的全局点云表示，随着新图像的观察，不断更新点的特征和3D位置。它用新检测到的点扩展点云，同时仔细删除冗余。新点的点云更新和深度预测是通过一种新的基于射线的2D-3D特征匹配技术实现的，该技术对先前点位置预测中的误差具有鲁棒性。与离线方法相比，我们的方法处理无限长的序列并提供实时更新。此外，点云没有预定义的分辨率或场景大小限制，其统一的全局表示确保了不同视角的视图一致性。在ScanNet数据集上的实验表明，我们的方法在在线MVS方法中达到了最先进的质量。项目页面：https://arthurhero.github.io/projects/pointrecon et.al.|[2410.23245](http://arxiv.org/abs/2410.23245)|null|
|**2024-10-30**|**Geometry Cloak: Preventing TGS-based 3D Reconstruction from Copyrighted Images**|单视图3D重建方法，如三平面高斯散斑（TGS），能够在几秒钟内从单个图像输入生成高质量的3D模型。然而，这种功能引发了人们对潜在滥用的担忧，恶意用户可以利用TGS从受版权保护的图像中创建未经授权的3D模型。为了防止这种侵权行为，我们提出了一种新的图像保护方法，在将图像提供给TGS之前，将不可见的几何扰动（称为“几何斗篷”）嵌入图像中。这些精心制作的扰动编码了一个定制的信息，当TGS尝试对隐形图像进行3D重建时，该信息就会显现出来。与简单地降低输出质量的传统对抗性攻击不同，我们的方法通过生成可识别的定制模式作为水印，迫使TGS以特定的方式失败3D重建。该水印允许版权所有者对从其受保护图像中进行的任何尝试的3D重建主张所有权。大量的实验已经验证了我们的几何斗篷的有效性。我们的项目可在https://qsong2001.github.io/geometry_cloak. et.al.|[2410.22705](http://arxiv.org/abs/2410.22705)|null|

<p align=right>(<a href=#updated-on-20241107>back to top</a>)</p>

## Diffusion

|Publish Date|Title|Abstract|PDF|Code|
|---|---|---|---|---|
|**2024-11-06**|**Community Forensics: Using Thousands of Generators to Train Fake Image Detectors**|检测人工智能生成的图像的关键挑战之一是发现由以前看不见的生成模型创建的图像。我们认为，训练数据的有限多样性是解决这一问题的主要障碍，我们提出了一个比先前工作更大、更多样化的新数据集。作为创建这个数据集的一部分，我们系统地下载了数千个文本到图像的潜在扩散模型和样本图像。我们还从数十种流行的开源和商业模式中收集图像。由此产生的数据集包含从4803个不同模型中采样的270万张图像。这些图像共同捕获了广泛的场景内容、生成器架构和图像处理设置。利用该数据集，我们研究了伪图像检测器的泛化能力。我们的实验表明，即使这些模型具有相似的架构，检测性能也会随着训练集中模型数量的增加而提高。我们还发现，随着模型多样性的增加，检测性能也会提高，而且我们训练的检测器比在其他数据集上训练的检测器具有更好的泛化能力。 et.al.|[2411.04125](http://arxiv.org/abs/2411.04125)|null|
|**2024-11-06**|**Manifold Diffusion Geometry: Curvature, Tangent Spaces, and Dimension**|我们介绍了一种新的估计器，用于使用扩散几何的工具计算流形数据的曲率、切空间和维数。尽管经典黎曼几何为几何数据分析和机器学习提供了丰富的灵感来源，但历史上很难以统计上表现良好的方式实现这些方法。扩散几何使我们能够开发出精确的黎曼几何方法，至关重要的是，这些方法对噪声和低密度数据也非常鲁棒。我们在这里介绍的方法与现有的理想密集、无噪声数据的最新技术相当，但在存在噪声或稀疏性的情况下明显优于它们。特别是，当添加少量噪声时，我们的维度估计改进了具有挑战性的基准测试中的现有方法。我们的切线空间和标量曲率估计不需要参数选择，并且大大改进了现有技术。 et.al.|[2411.04100](http://arxiv.org/abs/2411.04100)|null|
|**2024-11-06**|**Simulation of solar energetic particle events originated from coronal mass ejection shocks with a data-driven physics-based transport model**|太阳高能粒子（SEP）事件与日冕物质抛射（CME）和/或太阳耀斑有关。SEP穿过日冕和行星际空间到达地球，对航天器和在太空工作的宇航员以及航天器上的电子设备构成辐射危害。由于与每个事件相关的独特磁场配置和太阳喷发运动学特性，利用数据驱动模型对于预测SEP危害至关重要。在这项研究中，我们使用了一个开发的模型，该模型利用光球磁场测量和CME冲击观测作为输入，模拟了与快速CME速度（>700 km/s）相关的几个历史SEP事件。该模型包括一个与CME激波扩散激波加速理论相一致的SEP源项。通过比较SOHO、ACE、STEREO-A和STEREO-B的SEP强度-时间剖面的模拟和观测，可以评估该模型的性能。结果通常与观测结果非常吻合，特别是对于40.0 MeV以下的质子。然而，高能质子出现了差异，特别是在2011年3月7日和2014年2月25日的事件中，模拟往往高估了质子通量。在STEREO-A，2013年4月11日和2011年3月7日SEP事件的模拟质子强度与观测结果相比显示出非常不同的行为，因为弱磁场导致了经度上的有效传输。 et.al.|[2411.04095](http://arxiv.org/abs/2411.04095)|null|
|**2024-11-06**|**A Multi-level Monte Carlo simulation for invariant distribution of Markovian switching Lévy-driven SDEs with super-linearly growth coefficients**|本文研究马尔可夫切换L’evy驱动随机微分方程不变分布的数值近似。通过将驯服的自适应Euler-Maruyama方案与多层蒙特卡洛方法相结合，我们提出了一种适用于具有超线性增长漂移和扩散系数的随机微分方程的近似方案。 et.al.|[2411.04081](http://arxiv.org/abs/2411.04081)|null|
|**2024-11-06**|**The Lorentz Gas in a Mean-Field Potential: Weak Coupling and Diffusive Regime**|我们研究了洛伦兹气体在平均场型外力存在下的扩散标度。在弱耦合状态和扩散时间尺度下，测试粒子定律收敛到满足热方程的概率密度。热方程的扩散系数由格林-库博关系给出。 et.al.|[2411.04076](http://arxiv.org/abs/2411.04076)|null|
|**2024-11-06**|**On a diffuse interface model for diblock copolymers interacting with an electric field**|我们考虑一个扩散界面模型，描述由导电二嵌段共聚物和作为溶剂的均聚物组成的三元体系。由此产生的动力学由共聚物嵌段的两个Cahn-Hilliard-Oono方程建模，考虑了长程相互作用；均聚物的经典Cahn-Hiliard方程和电位移场的麦克斯韦方程。为了确保物理一致性，采用了多相奇异势。首先，我们证明了二维和三维全局弱解的存在性。在常迁移率的情况下，建立了弱解的唯一性，并在一般情况下给出了条件结果。还研究了瞬时正则化和长时间行为，后者在仿射线性电容率的情况下，特别表明解收敛到单个稳态。 et.al.|[2411.04074](http://arxiv.org/abs/2411.04074)|null|
|**2024-11-06**|**Imaging heat transport in suspended diamond nanostructures with integrated spin defect thermometers**|在所有材料中，单晶金刚石的热导率最高，室温下的值超过2000 W/m/K。这源于动量守恒的“正常”声子散射过程主导了动量耗散的“Umklapp”过程，这一特征也表明钻石是实验研究违反傅里叶定律的声子热输运现象的理想平台。在这里，我们引入稀氮空位色心作为原位、高精度的自旋缺陷温度计，以成像从环境条件加热的单晶金刚石微观结构中的温度不均匀性。我们分析了横截面在0.2至2.6μm²范围内的悬臂，观察到横截面与热通量之间的关系与傅里叶定律的预测有所不同。我们依靠基于线性化声子玻尔兹曼输运方程的第一性原理模拟来合理化这种行为，并讨论了制造诱导的杂质如何影响传导。我们的温度成像方法可以应用于任意几何形状的金刚石器件，为探索非常规、非扩散热传输现象铺平了道路。 et.al.|[2411.04065](http://arxiv.org/abs/2411.04065)|null|
|**2024-11-06**|**Space-Time Spectral Element Tensor Network Approach for Time Dependent Convection Diffusion Reaction Equation with Variable Coefficients**|本文提出了一种新的时空Petrov-Galerkin类方法。该方法利用张量训练（TT）和量化张量训练（QTT）的混合公式，专为时变对流扩散反应（CDR）方程的谱元离散化（Q1-SEM）而设计。我们重新制定了谱元离散CDR的组装过程，以提高其与张量运算的兼容性，并为谱元算子引入了低阶张量结构。认识到谱元框架离散算子中固有的带状结构，我们进一步利用CDR的QTT格式来实现更高的速度和压缩。此外，我们提出了一种在TT/QTT框架内将CDR的可变系数集成到全局离散算子中的综合方法。通过一系列数值实验，包括一个半线性示例，证明了所提出方法在存储效率和计算复杂度方面的有效性。 et.al.|[2411.04026](http://arxiv.org/abs/2411.04026)|null|
|**2024-11-06**|**Synomaly Noise and Multi-Stage Diffusion: A Novel Approach for Unsupervised Anomaly Detection in Ultrasound Imaging**|超声（US）成像因其无辐射、经济高效和便携的优点而广泛应用于常规临床实践。然而，美国图像的低再现性和质量，再加上专家级注释的稀缺，使得全监督分割模型的训练具有挑战性。为了解决这些问题，我们提出了一种基于扩散模型的无监督异常检测框架，该模型结合了合成异常（Synomaly）噪声函数和多阶段扩散过程。Synomaly噪声在训练过程中将合成异常引入健康图像，使模型能够有效地学习异常去除。引入多阶段扩散过程来逐步对图像进行去噪，在提高无异常重建质量的同时保留精细细节。生成的高保真反事实健康图像可以进一步增强分割模型的可解释性，并为评估异常程度和支持临床决策提供可靠的基线。值得注意的是，无监督异常检测模型完全在健康图像上训练，消除了对异常训练样本和像素级注释的需要。我们在颈动脉超声、脑MRI和肝脏CT数据集上验证了所提出的方法。实验结果表明，所提出的框架优于现有的最先进的无监督异常检测方法，在美国数据集中实现了与全监督分割模型相当的性能。此外，消融研究强调了超参数选择对Synomaly噪声的重要性，以及多阶段扩散过程在提高模型性能方面的有效性。 et.al.|[2411.04004](http://arxiv.org/abs/2411.04004)|null|
|**2024-11-06**|**ET-SEED: Efficient Trajectory-Level SE(3) Equivariant Diffusion Policy**|模仿学习，例如扩散策略，已被证明在各种机器人操纵任务中是有效的。然而，政策的稳健性和普遍性需要广泛的论证。为了减少对演示的依赖，我们利用空间对称性提出了ET-SEED，这是一种高效的轨迹级SE（3）等变扩散模型，用于在复杂的机器人操纵任务中生成动作序列。此外，之前的等变扩散模型要求马尔可夫过程中的每一步等变，这使得在如此强的约束下学习策略变得困难。我们从理论上扩展了等变马尔可夫核，简化了等变扩散过程的条件，从而以端到端的方式显著提高了轨迹级SE（3）等变扩散策略的训练效率。我们评估了ET-SEED在代表性机器人操纵任务上的表现，包括刚体、关节和可变形物体。实验证明，我们提出的方法具有卓越的数据效率和操作能力，并且仅需几次演示即可推广到看不见的配置。网站：https://et-seed.github.io/ et.al.|[2411.03990](http://arxiv.org/abs/2411.03990)|null|

<p align=right>(<a href=#updated-on-20241107>back to top</a>)</p>

## NeRF

|Publish Date|Title|Abstract|PDF|Code|
|---|---|---|---|---|
|**2024-11-04**|**Physically Based Neural Bidirectional Reflectance Distribution Function**|我们介绍了基于物理的神经双向反射分布函数（PBNBRDF），这是一种基于神经场的材料外观的新颖连续表示。我们的模型准确地重建了真实世界的材料，同时独特地增强了现实BRDF的物理特性，特别是通过重新参数化的亥姆霍兹互易性和通过高效分析积分的能量无源性。我们进行了系统分析，证明了遵守这些物理定律对重建材料的视觉质量的好处。此外，我们通过引入色度强制监督RGB通道的规范来提高神经BRDF的颜色精度。通过在多个测量的真实BRDF数据库上进行定性和定量实验，我们表明，遵守这些物理约束可以使神经场更忠实、更稳定地表示原始数据，并实现更高的渲染质量。 et.al.|[2411.02347](http://arxiv.org/abs/2411.02347)|null|
|**2024-11-01**|**Intensity Field Decomposition for Tissue-Guided Neural Tomography**|锥束计算机断层扫描（CBCT）通常需要数百次X射线投影，这引起了人们对辐射暴露的担忧。虽然稀疏视图重建通过使用更少的投影来减少曝光，但它很难达到令人满意的图像质量。为了应对这一挑战，本文介绍了一种新的稀疏视图CBCT重建方法，该方法为神经场赋予了人体组织正则化的能力。我们的方法被称为组织引导神经断层扫描（TNT），其动机是CBCT中骨骼和软组织之间明显的强度差异。直观地说，分离这些成分可能有助于神经场的学习过程。更确切地说，TNT包括一个异构的四重网络和相应的训练策略。该网络将强度场表示为软组织和硬组织成分及其各自纹理的组合。我们在估计的组织投影的指导下训练网络，从而能够有效地学习网络头所需的模式。大量实验表明，所提出的方法显著改善了稀疏视图CBCT重建，投影数量从10到60不等。与最先进的基于神经渲染的方法相比，我们的方法以更少的投影和更快的收敛实现了相当的重建质量。 et.al.|[2411.00900](http://arxiv.org/abs/2411.00900)|null|
|**2024-10-26**|**Neural Fields in Robotics: A Survey**|神经场已经成为计算机视觉和机器人技术中3D场景表示的一种变革性方法，能够从姿势的2D数据中准确推断几何、3D语义和动力学。利用可微分渲染，神经场包括连续隐式和显式神经表示，实现了高保真3D重建、多模态传感器数据的集成和新视点的生成。这项调查探讨了它们在机器人技术中的应用，强调了它们在增强感知、规划和控制方面的潜力。它们的紧凑性、内存效率和可微性，以及与基础模型和生成模型的无缝集成，使其成为实时应用的理想选择，提高了机器人的适应性和决策能力。本文基于200多篇论文，对机器人中的神经场进行了全面的回顾，对各个领域的应用进行了分类，并评估了它们的优势和局限性。首先，我们介绍了四个关键的神经场框架：占用网络、有符号距离场、神经辐射场和高斯散斑。其次，我们详细介绍了神经场在五个主要机器人领域的应用：姿态估计、操纵、导航、物理和自动驾驶，重点介绍了关键工作，并讨论了要点和公开挑战。最后，我们概述了神经场在机器人技术中的局限性，并为未来的研究提出了有前景的方向。项目页面：https://robonerf.github.io et.al.|[2410.20220](http://arxiv.org/abs/2410.20220)|null|
|**2024-10-24**|**3D-Adapter: Geometry-Consistent Multi-View Diffusion for High-Quality 3D Generation**|多视图图像扩散模型显著推进了开放域3D对象生成。然而，大多数现有模型依赖于缺乏固有3D偏差的2D网络架构，导致几何一致性受损。为了应对这一挑战，我们引入了3D Adapter，这是一个插件模块，旨在将3D几何感知注入预训练的图像扩散模型中。我们方法的核心是3D反馈增强的思想：对于采样循环中的每个去噪步骤，3D Adapter将中间的多视图特征解码为连贯的3D表示，然后对渲染的RGBD视图进行重新编码，通过特征添加来增强预训练的基础模型。我们研究了3D Adapter的两种变体：一种是基于高斯飞溅的快速前馈版本，另一种是利用神经场和网格的通用无训练版本。我们广泛的实验表明，3D Adapter不仅大大提高了文本到多视图模型（如Instant3D和Zero123++）的几何质量，而且还使用纯文本到图像的稳定扩散实现了高质量的3D生成。此外，我们通过在文本到3D、图像到3D、文本到纹理和文本到化身任务中呈现高质量的结果，展示了3D适配器的广泛应用潜力。 et.al.|[2410.18974](http://arxiv.org/abs/2410.18974)|**[link](https://github.com/Lakonik/MVEdit)**|
|**2024-10-22**|**Cortical Dynamics of Neural-Connectivity Fields**|皮质组织的宏观研究揭示了振荡活动的普遍性，这反映了神经相互作用的微调。本研究通过将广义振荡动力学纳入先前关于保守或半保守神经场动力学的工作中，扩展了神经场理论。先前的研究在很大程度上假设了神经单元之间的各向同性连接；然而，这项研究表明，广泛的各向异性和波动连接仍然可以维持振荡。使用拉格朗日场方法，我们研究了不同类型的连接、它们的动力学以及与神经场的潜在相互作用。基于这一理论基础，我们推导出了一个框架，该框架通过连接场的概念将Hebbian和非Hebbian学习（即可塑性）纳入神经场的研究中。 et.al.|[2410.16852](http://arxiv.org/abs/2410.16852)|null|
|**2024-10-15**|**Deep vectorised operators for pulsatile hemodynamics estimation in coronary arteries from a steady-state prior**|心血管血流动力学场为冠状动脉疾病提供了有价值的医学决策标志。计算流体动力学（CFD）是体内准确、无创评估这些量的金标准。在这项工作中，我们提出了一种基于机器学习的时间高效替代模型，用于基于稳态先验估计脉动血流动力学。我们引入了深度矢量化算子，这是一种用于在无限维函数空间上进行离散化独立学习的建模框架。基础神经结构是一个以血流动力学边界条件为条件的神经场。重要的是，我们展示了如何将逐点动作的要求放宽到置换等变，从而产生一系列可以通过消息传递和自我关注层进行参数化的模型。我们在从冠状动脉计算机断层扫描血管造影（CCTA）中提取的74条狭窄冠状动脉的数据集上评估了我们的方法，并将患者特异性脉动CFD模拟作为基本事实。我们证明，我们的模型能够准确估计脉动速度和压力，同时不受源域重新采样的影响（离散化独立性）。这表明，深度矢量化算子是冠状动脉及其他动脉心血管血流动力学估计的强大建模工具。 et.al.|[2410.11920](http://arxiv.org/abs/2410.11920)|null|
|**2024-10-07**|**Fast Training of Sinusoidal Neural Fields via Scaling Initialization**|神经场是一种新兴的范式，它将数据表示为由神经网络参数化的连续函数。尽管有许多优点，但神经场通常具有较高的训练成本，这阻碍了更广泛的采用。在本文中，我们关注一个流行的神经场家族，称为正弦神经场（SNF），并研究如何初始化它以最大限度地提高训练速度。我们发现，基于信号传播原理设计的SNF标准初始化方案是次优的。特别是，我们证明，通过简单地将每个权重（最后一层除外）乘以一个常数，我们可以将SNF训练加速10 $\times$。这种方法被称为$\textit{weight scaling}$ ，在各种数据域上持续提供显著的加速，使SNF的训练速度比最近提出的架构更快。为了理解为什么权重缩放效果良好，我们进行了广泛的理论和实证分析，结果表明，权重缩放不仅有效地解决了频谱偏差，而且具有良好的优化轨迹。 et.al.|[2410.04779](http://arxiv.org/abs/2410.04779)|null|
|**2024-10-04**|**End-to-End Reaction Field Energy Modeling via Deep Learning based Voxel-to-voxel Transform**|在计算生物化学和生物物理学中，理解静电相互作用的作用对于阐明生物分子的结构、动力学和功能至关重要。泊松-玻尔兹曼（PB）方程是通过描述带电分子内部和周围的静电势来模拟这些相互作用的基础工具。然而，由于生物分子表面的复杂性和需要考虑可移动离子，求解PB方程带来了重大的计算挑战。虽然求解PB方程的传统数值方法是准确的，但它们的计算成本很高，并且随着系统规模的增加而扩展性较差。为了应对这些挑战，我们引入了PBNeF，这是一种新的机器学习方法，灵感来自基于神经网络的偏微分方程求解器的最新进展。我们的方法将PB方程的输入和边界静电条件转化为可学习的体素表示，使神经场变换器能够预测PB解，进而预测反应场势能。大量实验表明，与传统的PB求解器相比，PBNeF的速度提高了100倍以上，同时保持了与广义玻恩（GB）模型相当的精度。 et.al.|[2410.03927](http://arxiv.org/abs/2410.03927)|null|
|**2024-10-08**|**DressRecon: Freeform 4D Human Reconstruction from Monocular Video**|我们提出了一种从单目视频中重建时间一致的人体模型的方法，重点是极其宽松的衣服或手持物体的交互。之前在人体重建方面的工作要么局限于没有物体交互的紧身衣服，要么需要校准的多视图捕捉或个性化的模板扫描，而大规模收集这些数据成本很高。我们对高质量但灵活的重建的关键见解是，将关于关节体形状的通用人类先验（从大规模训练数据中学习）与视频特定的关节“骨骼袋”变形（通过测试时间优化适合单个视频）仔细结合。我们通过学习一个神经隐式模型来实现这一点，该模型将身体和衣服的变形作为单独的运动模型层来解开。为了捕捉服装的微妙几何形状，我们在优化过程中利用了基于图像的先验，如人体姿势、表面法线和光流。由此产生的神经场可以提取到时间一致的网格中，或进一步优化为显式3D高斯分布，以实现高保真交互式渲染。在具有高度挑战性的服装变形和物体交互的数据集上，DressReston可以产生比现有技术更高保真的3D重建。项目页面：https://jefftan969.github.io/dressrecon/ et.al.|[2409.20563](http://arxiv.org/abs/2409.20563)|null|
|**2024-09-25**|**TalkinNeRF: Animatable Neural Fields for Full-Body Talking Humans**|我们介绍了一种新的框架，该框架从单眼视频中学习全身说话的人的动态神经辐射场（NeRF）。之前的工作只代表身体姿势或面部。然而，人类通过全身进行交流，结合身体姿势、手势和面部表情。在这项工作中，我们提出了TalkinNeRF，这是一个基于NeRF的统一网络，代表了整体4D人体运动。给定一个受试者的单眼视频，我们学习身体、面部和手的相应模块，这些模块结合在一起生成最终结果。为了捕捉复杂的手指关节，我们学习了手的额外变形场。我们的多身份表示能够同时训练多个科目，以及在完全看不见的姿势下进行强大的动画。只要输入一段短视频，它也可以推广到新的身份。我们展示了最先进的性能，用于为全身说话的人类制作动画，具有精细的手部发音和面部表情。 et.al.|[2409.16666](http://arxiv.org/abs/2409.16666)|null|

<p align=right>(<a href=#updated-on-20241107>back to top</a>)</p>

[contributors-shield]: https://img.shields.io/github/contributors/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[contributors-url]: https://github.com/Vincentqyw/cv-arxiv-daily/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[forks-url]: https://github.com/Vincentqyw/cv-arxiv-daily/network/members
[stars-shield]: https://img.shields.io/github/stars/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[stars-url]: https://github.com/Vincentqyw/cv-arxiv-daily/stargazers
[issues-shield]: https://img.shields.io/github/issues/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[issues-url]: https://github.com/Vincentqyw/cv-arxiv-daily/issues

