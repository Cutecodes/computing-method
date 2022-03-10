import numpy as np 
from matplotlib import pyplot as plt

def f(x,y):
    return x*y**(1/3)
def euler(y0,x0,x1,h,f):
    yi = y0
    xi = x0
    while(xi<=x1):
       yi = yi+h*f(xi,yi)
       xi += h
    return yi

def y(x):
    return ((x**2+2)/3)**(3/2)

def main():
    print("精确解：",y(2))
    print("h=0.1:",euler(1,1,2,0.1,f))
    print("h=0.01:",euler(1,1,2,0.01,f))
    print("h=0.001:",euler(1,1,2,0.001,f))
if __name__=='__main__':
    main()