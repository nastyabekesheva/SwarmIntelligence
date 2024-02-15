import numpy as np

def harmonic(x):
    return (x**3) * ((3-x)**5) * np.sin(10 * np.pi * x)

def parametric(x):
    return - (0.2-x) ** 5 * (0.8-x) ** 12 * np.sin(12*np.pi * x) * np.sin(9*np.pi * x)

def izum(x, y):
    return -np.cos(x) * np.cos(y) * np.exp(-(x-np.pi) ** 2 -(y-np.pi) ** 2)

def erkli(x, y):
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
