import numpy as np
import matplotlib.pyplot as plt

def main():
    #lamda = float(input("please input the lambda:"))
    x0 = float(input("please input the x0:"))

    x = []
    for i in range(20):
        lamda = i*0.2+0.2
        xk = x0
        x.append([xk])
        for j in range(50):
            xk = lamda*xk*(1-xk)
            x[i].append(xk)

    k = [i for i in range(len(x[0]))]
    for i in range(20):
        plt.plot(k,x[i],label = "%s"%(i*0.2+0.2))
    plt.legend(loc='best')
    plt.show()

if __name__ == '__main__':
    main()
