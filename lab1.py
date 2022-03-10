import numpy as np 
import matplotlib.pyplot as plt

def lagrange_fun(x,y,tx):
    lx = 0
    for i in range(len(x)):
        temp = 1.0
        for j in range(len(x)):
            if(i!=j):
                temp*=(tx-x[j])/(x[i]-x[j])
        lx += y[i]*temp
    return lx

def main():
    n = int(input("请输入参数n："))
    k = float(input("请输入参数k："))

    x = np.linspace(0,1,n+1)

    fx = np.abs(np.sin(k*np.pi*x))

    x2 = np.linspace(0,1,1000)
    fx2 = np.abs(np.sin(k*np.pi*x2))

    lx = [lagrange_fun(x,fx,i) for i in x2]
    
    plt.subplot(211)
    plt.title("f(x) = |sin(k*pi*x)| ,n = %s , k = %s"%(n,k))
    plt.plot(x2,fx2,color = "blue",label = "$f(x)$")
    plt.plot(x2,lx,color = "green",label = "$L(x)$")

    plt.subplot(212)
    plt.title("e ,n = %s , k = %s"%(n,k))
    plt.plot(x2,fx2-lx,color = "blue",label = "$e$")
    print("MSE:%.5f"%(np.sum(np.power(lx-fx2,2))/len(lx)))
    plt.show()
if __name__ == '__main__':
    while True:
        main()


 
