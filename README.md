# Julia-Orbit
The program is written in Python and was coded in collaboration with Jérôme Côté while completing an undergraduate research project in the summer of 2021.

## How to use the program
To use the program, you need python installed. You also need to install some required packages. Run the following commands to install the required packages:
* pip install tkinter
* pip install time
* pip instal os
* pip install sys
* pip install PIL
* pip install numpy
* pip install datetime

After these were installed, you compile the program in the command line using the command:
* python trajectoireOrbite-GUI.py.

The slider controls the real and imaginary parts of z and the real and imaginary part of c in the complex-valued function $z^2 + c$.

## Explaination of the output
The output of the program is a diagram illustrating the orbit of $z^2 + c$ under a certain number of iterations. The polygonal line in red and the green dots represent the orbit of sequence $z_{n+1} = z_n^2 + c$. The polygonal line in blue represents the averages of $z_1$, $z_2$, $\ldots$, $z_n$. See the picture below.

[<img src="TrajectoireOrbiteVSCesaro-zRe0.0zIm0.02021-05-30_22-58-26.png" width="200"/>](TrajectoireOrbiteVSCesaro-zRe0.0zIm0.02021-05-30_22-58-26.png)
[<img src="TrajectoireOrbiteVSCesaro-zRe0.4286zIm-0.44562021-05-30_23-23-06.png" width="200"/>](TrajectoireOrbiteVSCesaro-zRe0.4286zIm-0.44562021-05-30_23-23-06.png)
[<img src="TrajectoireOrbiteVSCesaro-zRe0.7619zIm-0.4456_cRe-0.4762CIm0.4249_2021-05-30_23-06-15.png" width="200"/>](TrajectoireOrbiteVSCesaro-zRe0.7619zIm-0.4456_cRe-0.4762CIm0.4249_2021-05-30_23-06-15.png)
[<img src="TrajectoireOrbiteVSCesaro2024-01-08_17-01-11.png" width="200"/>](TrajectoireOrbiteVSCesaro2024-01-08_17-01-11.png)

## Research goals
The goal of this project was to study summability methods and its application to the generation of Julia sets and the Mandelbrot set.


