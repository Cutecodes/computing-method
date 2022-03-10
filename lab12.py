import numpy as np

def f(x):
    return np.exp(x)+10*x-2

def fx(x):
    return (np.exp(x)-2)/(-10)
def df(x):
    return np.exp(x)+10


def bin(f,a,b,e=5*10e-4):
    while np.abs(a-b)>e:
        mi = (a+b)/2
        if(f(a)*f(mi)<0):
            b = mi
        else:
            a = mi
    return mi

def iter(fx,x0,e=5*10e-4):
    x = x0
    while True:
        xn = fx(x)
        if(np.abs(xn-x)<e):
            break
        x = xn
    return x

def newton(f,df,x0,e=5*10e-4):
    x = x0
    while True:
        if np.abs(df(x)-0.0)<e:
            break
        xn = x - f(x)/df(x)
        if np.abs(x-xn)<e:
            break
        x = xn
    return x
        

def main():
    
    print("二分法解：",bin(f,0,1))
    print("迭代法解：",iter(fx,0))
    print("牛顿法解：",newton(f,df,0))

    
if __name__=='__main__':
    main()
