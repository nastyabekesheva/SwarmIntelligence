# Testing different functions on Genetic Optimizer and Grey Wolf Optimizer

-----

## Table of Contents

- [Harmonic function](#Harmonic-function)
- [Parametric function](#Parametric-function)
- [Easom function](#Easom-function)
- [Ackley function](#Ackley-function)
- [Cross-in-tray function](#Cross-in-tray-function)
- [Eggholder function](#Eggholder-function)
- [Holder functiion](#Holder-function)
- [Schaffer-1 fucntion](#Schaffer-1-fucntion)
- [Schaffer-2 fucntion](#Schaffer-2-fucntion)  


-----


### Harmonic function

$$
f(x) = x^3(3-x)^5\sin(10\pi x),\> x\in[0,3]
$$

**Expected minimum**: $$f(1.15)=-33$$

> Genetic Optimizer plot on each epoch:

![](animated_HARMONIC_GO.gif) 

> Grey Wolf Optimizer plot on each epoch:

![](animated_HARMONIC_GWO.gif)

> Genetic Optimizer fitness trend plot:

![](fitness_trend_HARMONIC_GO.png)

> Grey Wolf Optimizer fitness trend plot:

![](fitness_trend_HARMONIC_GWO.png)

> Genetic Optimizer distance between optimal values on each plot:

![](distances_HARMONIC_GO.png)

> Grey Wolf Optimizer distance between optimal values on each plot:

![](distances_HARMONIC_GWO.png)

-----


### Parametric function

$$
f(x) = -(0.2-x)^5(0.8-x)^12\sin(12\pi x)\sin(9\pi x),\> x\in[0,3]
$$

**Expected minimum**: $$f(3)=1.5\cdot 10^{-6}$$

> Genetic Optimizer plot on each epoch:

![](animated_PARAMETRIC_GO.gif) 

> Grey Wolf Optimizer plot on each epoch:

![](animated_PARAMETRIC_GWO.gif)

> Genetic Optimizer fitness trend plot:

![](fitness_trend_PARAMETRIC_GO.png)

> Grey Wolf Optimizer fitness trend plot:

![](fitness_trend_PARAMETRIC_GWO.png)

> Genetic Optimizer distance between optimal values on each plot:

![](distances_PARAMETRIC_GO.png)

> Grey Wolf Optimizer distance between optimal values on each plot:

![](distances_PARAMETRIC_GWO.png)

### Easom function

$$
f(x, y) = -\cos(x)\cos(y)e^{-(x-\pi)^2-(y-\pi)^2},\> (x,y)\in\[-100,100\]^2
$$

**Expected minimum**: $$f(\pi,\pi)=-1$$

> Genetic Optimizer plot on each epoch:

![](animated_EASOM_GO.gif) 

> Grey Wolf Optimizer plot on each epoch:

![](animated_EASOM_GWO.gif)

> Genetic Optimizer fitness trend plot:

![](fitness_trend_EASOM_GO.png)

> Grey Wolf Optimizer fitness trend plot:

![](fitness_trend_EASOM_GWO.png)

> Genetic Optimizer distance between optimal values on each plot:

![](distances_EASOM_GO.png)

> Grey Wolf Optimizer distance between optimal values on each plot:

![](distances_EASOM_GWO.png)

### Ackley function

$$
f(x, y) = -20e^{-0.2\sqrt{0.5(x^2+y^2)}} - e^{0.5(\cos2\pi x+\cos2\pi y)},\> (x,y)\in\[-5,5\]^2
$$

**Expected minimum**: $$f(0,0)=0$$

> Genetic Optimizer plot on each epoch:

![](animated_ACKLEY_GO.gif) 

> Grey Wolf Optimizer plot on each epoch:

![](animated_ACKLEY_GWO.gif)

> Genetic Optimizer fitness trend plot:

![](fitness_trend_ACKLEY_GO.png)

> Grey Wolf Optimizer fitness trend plot:

![](fitness_trend_ACKLEY_GWO.png)

> Genetic Optimizer distance between optimal values on each plot:

![](distances_ACKLEY_GO.png)

> Grey Wolf Optimizer distance between optimal values on each plot:

![](distances_ACKLEY_GWO.png)

### Cross-in-tray function

$$
f(x, y) = -0.0001\left(\eft|\sin x\sin y e^{\eft|100-\frac{\sqrt{x^2+y^2}}{\pi}\right|}\right|+1\right)0.1,\> (x,y)\in\[-10,10\]^2
$$

**Expected minimum**: $$f(1.34941,1.34941)=−2.06261,\>f(1.34941,-1.34941)=−2.06261,\>f(-1.34941,1.34941)=−2.06261,\>f(-1.34941,-1.34941)=−2.06261$$

> Genetic Optimizer plot on each epoch:

![](animated_CROSS_IN_TRAY_GO.gif) 

> Grey Wolf Optimizer plot on each epoch:

![](animated_CROSS_IN_TRAY_GWO.gif)

> Genetic Optimizer fitness trend plot:

![](fitness_trend_CROSS_IN_TRAY_GO.png)

> Grey Wolf Optimizer fitness trend plot:

![](fitness_trend_CROSS_IN_TRAY_GWO.png)

> Genetic Optimizer distance between optimal values on each plot:

![](distances_CROSS_IN_TRAY_GO.png)

> Grey Wolf Optimizer distance between optimal values on each plot:

![](distances_CROSS_IN_TRAY_GWO.png)

### Eggholder function

$$
f(x, y) = -(y+47)\sin\sqrt{\left|\frac{x}{2}+y+47\right|}-x\sin\sqrt{|x-y-47|},\> (x,y)\in\[-512,512\]^2
$$

**Expected minimum**: $$f(512,404.2319)=−-959.6407$$

> Genetic Optimizer plot on each epoch:

![](animated_EGGHOLDER_GO.gif) 

> Grey Wolf Optimizer plot on each epoch:

![](animated_EGGHOLDER_GWO.gif)

> Genetic Optimizer fitness trend plot:

![](fitness_trend_EGGHOLDER_GO.png)

> Grey Wolf Optimizer fitness trend plot:

![](fitness_trend_EGGHOLDER_GWO.png)

> Genetic Optimizer distance between optimal values on each plot:

![](distances_EGGHOLDER_GO.png)

> Grey Wolf Optimizer distance between optimal values on each plot:

![](distances_EGGHOLDER_GWO.png)
