import numpy as np 
from matplotlib import pyplot as plt

def f(x,y):
    return x+y
def Runge_Kutta(y0,x0,x1,h,f):
    yi = y0
    xi = x0
    y = []
    x = []
    while(xi<x1):
        x.append(xi)
        y.append(yi)
        k1 = f(xi,yi)
        k2 = f(xi+h/2,yi+(h*k1)/2)
        k3 = f(xi+h/2,yi+(h*k2)/2)
        k4 = f(xi+h,yi+h*k3)
        yi = yi+h*(k1+2*k2+2*k3+k4)/6
        xi += h
    return x,y

def y(x):
    return -x-1

def main():
    rkx,rky = Runge_Kutta(-1,0,1,0.1,f)
    #x = np.linspace(0,1,100)
    print("精确解:",rkx[-1],y(rkx[-1]))
    print("h=0.1:",rkx[-1],rky[-1])
    ty = []
    for xi in rkx:
        ty.append(y(xi))
    plt.plot(rkx,rky)
    plt.plot(rkx,ty)
    plt.show()
    rky = np.array(rky)
    ty = np.array(ty)
    plt.plot(rkx,rky-ty)
    plt.show()

if __name__=='__main__':
    main()
