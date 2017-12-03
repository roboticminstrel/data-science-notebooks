# Education at Digipen

During the four years I was at Digipen, I did a large number of interesting projects that have unfortunately been lost to time. I'll start with the two projects I still have video evidence of. 

## FFT Water:

![alt text](https://github.com/roboticminstrel/data-science-notebooks/blob/master/Digipen/img/water-simulation.png)

<a href='https://www.youtube.com/watch?v=KmKxEwAD2uk'>Video of my water simulation</a>

Implementation: This algorithm is built off the same simulation used in the movie Titanic. The basic idea is fairly simple. Generate a 2^x by 2^x grid of points, these points are the triangle field defining the topography of the water. The 2^x constraint means we can use an FFT to take the n x n point representation of the two dimensional wave into the vector space of n x n waves. There's an equation from oceanography observations that shows the expected wave height and propogation speed based on wind speed and direction, and a given wave's direction and magnitude. The equation I used is:

<img src="https://latex.codecogs.com/gif.latex?P_h(K)&space;=&space;a\frac{e^{-1/(kl)^2}}{k^4}\lvert\hat&space;K&space;\cdot&space;\hat&space;W&space;\rvert&space;e^{-k^2w^2}" title="P_h(K) = a\frac{e^{-1/(kl)^2}}{k^4}\lvert\hat K \cdot \hat W \rvert e^{-k^2w^2}" />

where K is the wave vector, W is the wind vector, k is the wave vector's magnitude, l = v^2/g (the largest wave that can arise at wind speed v) where g is the gravitational constant, and a is a global constant governing wave height. The last e factor is for eliminating waves with small wavelength to improve convergence. 

From there, all you need is a fast fourier transform to get the height field from the wave field:

<img src="https://latex.codecogs.com/gif.latex?h(X,t)&space;=&space;\sum_K\tilde&space;h(K,t)e^{iK\cdot&space;X}" title="h(X,t) = \sum_K\tilde h(K,t)e^{iK\cdot X}" />

For rendering, it's also very helpful to have an equation for surface normals, for lighting, surface reflection, and so on. The equation for the surface normals can be gotten from the gradient of the above equation:

<img src="https://latex.codecogs.com/gif.latex?\nabla&space;h(X,t)&space;=&space;\sum_KiK\tilde&space;h(K,t)e^{iK&space;\cdot&space;X}" title="\nabla h(X,t) = \sum_KiK\tilde h(K,t)e^{iK \cdot X}" />

I chose to use a size of 2^10 (1024 x 1024) for my simulation. I implemented the FFT from scratch. While profiling, the big bottleneck was passing the data from the CPU to the GPU every frame. It still ran comfortably in real time, but given some of the capabilities of modern DirectX versions, if I were to do this project again, I would implement the whole thing on the GPU instead. The entire project was done with C++ on DirectX 8.0.

You can read the rest of the implementation details for the project from the article I got the idea from, <a href='https://www.gamasutra.com/view/feature/131445/deep_water_animation_and_rendering.php'>here</a>. 

While I did this project during my time at Digipen, it wasn't part of a class, and I hadn't formally learned signal processing, or even multivariate calculus, much less pixel shading and the rest of the tech stack I used. This project more than any other showcases my ability to engage with complex technical challenges I haven't been formally prepared for. 

## Solid body physics simulation with stable stacking
