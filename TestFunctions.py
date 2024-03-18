import numpy as np
import sys

def harmonic(x):
    return (x**3) * ((3-x)**5) * np.sin(10 * np.pi * x)

def parametric(x):
    return - (0.2-x) ** 5 * (0.8-x) ** 12 * np.sin(12*np.pi * x) * np.sin(9*np.pi * x)

def easom(x, y):
    return -np.cos(x) * np.cos(y) * np.exp(-(x-np.pi) ** 2 -(y-np.pi) ** 2)

def ackley(x, y):
    return -20*np.exp(-0.2 * np.sqrt(0.5*(x**2+y**2))) - np.exp(0.5 * (np.cos(2*np.pi*x)+np.cos(2*np.pi*y))) + np.exp(1) +20

def cross_in_tray(x, y):
    return -0.0001 * (np.abs(np.sin(x)*np.sin(y) * np.exp(np.abs(100-np.sqrt(x**2+y**2)/np.pi)))+1) ** 0.1

def eggholder(x, y):
    return -(y+47)*np.sin(np.sqrt(np.abs(x/2 +y +47))) - x*np.sin(np.sqrt(np.abs(x-y-47)))

def holder(x, y):
    return - np.abs(np.sin(x) * np.cos(y) * np.exp(np.abs(1-np.sqrt(x**2+y**2)/np.pi)))

def schaffer1(x, y):
    return 0.5 + (np.sin(x**2-y**2)**2-0.5) / (1+0.001*(x**2+y**2)) ** 2

def schaffer2(x, y):
    return 0.5 + (np.cos(np.abs(x**2-y**2))**2-0.5) / (1+0.001*(x**2+y**2)) ** 2

def rastrigin2d(x, y):
    return 20+x**2-10*np.cos(2*np.pi*x)+y**2-10*np.cos(2*np.pi*y)

def rastrigin3d(x, y, z):
    return 30+x**2-10*np.cos(3*np.pi*x)+y**2-10*np.cos(3*np.pi*y)+z**2-10*np.cos(3*np.pi*z)

def rosenbrock1(x, y):
    f = (1-x)**2+100*(y-x**2)**2
    if (x-1)**3-y+1>=0 or x+y-2>=0:
        f = sys.maxsize
    
    return f

def rosenbrock2(x, y):
    f = (1-x)**2+100*(y-x**2)**2
    if  x**2+y**2>=2:
        f = sys.maxsize
    
    return f

def mishra_berd(x, y):
    f = np.exp((1 - np.cos(x))**2 * np.sin(y)) + np.exp((1 - np.sin(y))**2 * np.cos(x)) + (x - y)**2
    if (x + 5)**2 + (y - 5)**2 >= 25:
        f = sys.maxsize

    return f

def simionesk(x, y):
    f = 0.1*x*y
    if  x**2+y**2 >= (1-0.2*np.cos(8*np.arctan(x/y)))**2:
        f = sys.maxsize

    return f

def rastrigin10d(*params):
    return 100 + sum([x**2-10*np.cos(2*np.pi*x) for x in params])

def rastrigin30d(*params):
    return 300 + sum([x**2-10*np.cos(2*np.pi*x) for x in params])

def rastrigin50d(*params):
    return 500 + sum([x**2-10*np.cos(2*np.pi*x) for x in params])

def spring(*params):
    f = (params[2]+2)*params[1]*params[0]**2

    if (1 - (params[1]**3*params[2]) / (7.178*params[0]**4)) >= 0:
        f = sys.maxsize
    elif (4*params[1]**2-params[0]*params[2]) / (12.566*(params[1]*params[1]**3) - params[0]**4) + 1 / (5.108*params[0]**2) >= 0:
        f = sys.maxsize
    elif 1 - (140.45*params[0]) / (params[1]**2 *params[2]) >= 0:
        f = sys.maxsize
    elif (params[1]+params[0]) / 1.5 - 1  >= 0:
        f = sys.maxsize

    return f

def reduc(*x):
    f = 0.7854 * x[0] * x[1]**2 * (3.3333 * x[2]**2 + 14.9334 * x[2] - 43.0934) -1.508 * x[0] * (x[5]**2 + x[6]**2) + 7.4777 * (x[5]**3 + x[6]**3) + 0.7854 * (x[3] * x[5]**2 + x[4] * x[6]**2)
    if 27 / (x[0] * x[1]**2 * x[2]) - 1 >= 0:
        f = sys.maxsize
    elif 397.5 / (x[0] * x[1]**2 * x[2]**2) - 1 >= 0:
        f = sys.maxsize
    elif 1.93 * x[3]**3 / (x[1] * x[2] * x[5]**4) - 1 >= 0:
        f = sys.maxsize
    elif 1.0 / (110 * x[5]**3) * np.sqrt((745.0 * x[3] / (x[1] * x[2]))**2 + 16.9 * 10**6) - 1 >= 0:
        f = sys.maxsize
    elif 1.0 / (85 * x[6]**3) * np.sqrt((745.0 * x[4] / (x[1] * x[2]))**2 + 157.5 * 10**6) - 1 >= 0:
        f = sys.maxsize
    elif x[1] * x[2] / 40 - 1 >= 0:
        f = sys.maxsize
    elif 5 * x[1] / x[0] - 1 >= 0:
        f = sys.maxsize
    elif x[0] / (12 * x[1]) - 1 >= 0:
        f = sys.maxsize
    elif (1.5 * x[5] + 1.9) / x[3] - 1 >= 0:
        f = sys.maxsize
    elif (1.1 * x[6] + 1.9) / x[4] - 1 >= 0:
        f = sys.maxsize

    return f

