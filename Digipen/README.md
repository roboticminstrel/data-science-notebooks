# Education at Digipen

Here is a brief tour of some of my projects from my time at Digipen.

## FFT Water:

<img src='https://github.com/roboticminstrel/data-science-notebooks/blob/master/Digipen/img/water-simulation.png' width='600' height='450'>


<a href='https://www.youtube.com/watch?v=KmKxEwAD2uk'>Video of my water simulation</a>

Implementation: This algorithm is built off the same simulation used in the movie Titanic. The basic idea is fairly simple. Generate an n x n grid of points, these points are the triangle field defining the topography of the water. If n is of the form 2^x, it's possible to use the fast fourier transform (FFT) to take the n x n point time domain signal into n x n single point waves in Fourier space. From there, we can determine each individual wave's wave height and propogation speed using a uniform equation, then translate back into Euclidean space to get the geometry for a given time step. There's an equation from oceanography observations that shows the expected wave height and propogation speed based on wind speed and direction, and a given wave's direction and magnitude. The equation I used is:

<img src="https://latex.codecogs.com/gif.latex?P_h(K)&space;=&space;a\frac{e^{-1/(kl)^2}}{k^4}\lvert\hat&space;K&space;\cdot&space;\hat&space;W&space;\rvert&space;e^{-k^2w^2}" title="P_h(K) = a\frac{e^{-1/(kl)^2}}{k^4}\lvert\hat K \cdot \hat W \rvert e^{-k^2w^2}" />

where K is the wave vector, W is the wind vector, k is the wave vector's magnitude, l = v^2/g is the largest wave that can arise at wind speed v at gravity g, and a is a global constant governing wave height. The last e factor is for eliminating waves with small wavelength to improve convergence. 

From there, all you need is a fast fourier transform to get the height field from the wave field:

<img src="https://latex.codecogs.com/gif.latex?h(X,t)&space;=&space;\sum_K\tilde&space;h(K,t)e^{iK\cdot&space;X}" title="h(X,t) = \sum_K\tilde h(K,t)e^{iK\cdot X}" />

For rendering, it's also very helpful to have an equation for surface normals, for lighting, surface reflection, and so on. The equation for the surface normals can be obtained from the gradient of the above equation:

<img src="https://latex.codecogs.com/gif.latex?\nabla&space;h(X,t)&space;=&space;\sum_KiK\tilde&space;h(K,t)e^{iK&space;\cdot&space;X}" title="\nabla h(X,t) = \sum_KiK\tilde h(K,t)e^{iK \cdot X}" />

I chose to use a size of 2^10 (1024 x 1024) for my simulation. I implemented the FFT from scratch. While profiling, I learned that the big bottleneck was passing the data from the CPU to the GPU every frame. It still ran comfortably in real time, but given some of the capabilities of modern versions DirectX, if I were to do this project again, I would just implement the whole thing directly on the GPU. The entire project was done with C++ with DirectX 8.0.

You can read the rest of the implementation details for the project from the article I got the idea from, <a href='https://www.gamasutra.com/view/feature/131445/deep_water_animation_and_rendering.php'>here</a>. 

While I did this project during my time at Digipen, it wasn't part of a class, and I hadn't formally learned signal processing, or even multivariate calculus, much less pixel shading and the rest of the tech stack I used. In preperation for this project, I spent quite some time familiarizing myself with vector calculus, the fourier transform (and the FFT in particular), as well as familiarizing myself with the intricacies of working in a vector space over a field of complex numbers. <a href='https://www.amazon.com/Div-Grad-Curl-All-That/dp/0393925161'>Div Curl and Grad</a> was especially helpful. 

This project more than any other showcases my ability to engage with complex technical challenges I haven't been formally prepared for. 

## Solid body physics simulation with stable stacking
<img src='https://github.com/roboticminstrel/data-science-notebooks/blob/master/Digipen/img/physics-simulation.png' width='600' height='450'>


<a href='https://www.youtube.com/watch?v=_UsPEd9q3m8'>Video of my water simulation</a>

Implementation: This project was an implementation of the contact graph described in <a href="http://physbam.stanford.edu/~fedkiw/papers/stanford2003-01.pdf">Guendelman, E., Bridson, R. and Fedkiw, R., "Nonconvex Rigid Bodies with Stacking", SIGGRAPH 2003, ACM TOG 22, 871-878 (2003)</a>. The physics engine I built with this project handles collision, contact, friction, and stacking for simple convex objects (cubes, and other simple convex primitives). 

Most of the simulation relies on fairly typical equations for finding collision, updating position and velocity, and handling numerical stability issues at a discrete and variable timestep. The one complicated part of the project revolves around stable stacking. Normally, when two objects are found to penetrate, you update position and velocity to keep objects from overlapping each other. The problem comes when you have multiple moving objects in the same scene. If you have 3 objects overlapping, if you update them in the wrong order you won't converge to a stable and physically believable state. 

The solution is basically just to spatially sort objects in the scene, and propogate from the bottom up. Some extra complexity can arise from edge cases with interlocking primitives in more complex arrangements, additional details are in the above paper. 

## Additional Projects:
Every year, we had a collaborative year-long game project working in teams of 3~6. These projects were very useful for learning version control, agile development in a collaborative setting, and how to approach software architecture issues when working with a code base in the 10's of thousands of lines. 

I also implemented a full software 3D rendering system, taking 3D meshes from world space, performing view thrustum culling, transforming into screen space, and then rastorizing the triangles directly to the screen. I implemented a software raytracer handling reflections, and a binary partitioning tree for doing back to front rasterizing without having to use the depth buffer. Most of these are far slower than just using the DirectX or OpenGL implementation, but it was invaluable for getting an in depth understanding of the rendering pipeline, and learning to think of optimizations when working on computationally intense problems. 

One last project of note, was writing a very simple gameboy game in assembly. That was my introduction to assembly language, before learning X86 assembly for occasional inner loop optimization in my C++ projects. 
