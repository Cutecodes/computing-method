import numpy as np 

import matplotlib.pyplot as plt

def Bezier(p0,p1,p2):
    A = np.array([[1,0,0,0],[0,1,0,0],[1,1,1,1],[0,1,2,3]])
    y = np.array([[p0[1]],[2*(p1[1]-p0[1])],[p2[1]],[2*(p2[1]-p1[1])]])
    x = np.array([[p0[0]],[2*(p1[0]-p0[0])],[p2[0]],[2*(p2[0]-p1[0])]])
    kx = np.dot(np.linalg.inv(A),x)
    ky = np.dot(np.linalg.inv(A),y)
    return kx,ky

def main():
    #lamda = float(input("please input the lambda:"))
    p0 = input("please input the p0:").split()
    p1 = input("please input the p1:").split()
    p2 = input("please input the p2:").split()
    p0 = [float(x) for x in p0]
    p1 = [float(x) for x in p1]
    p2 = [float(x) for x in p2]
    kx,ky = Bezier(p0,p1,p2)
    t = np.linspace(0,1,1000)
    x = []
    y = []
    for ti in t:
        x.append(kx[0]+kx[1]*ti+kx[2]*ti**2+kx[3]*ti**3)
        y.append(ky[0]+ky[1]*ti+ky[2]*ti**2+ky[3]*ti**3)
    plt.scatter(p0[0],p0[1],marker = "o",color = "red",label = "p0")
    plt.scatter(p1[0],p1[1],marker = "o",color = "blue",label = "p1")
    plt.scatter(p2[0],p2[1],marker = "o",color = "green",label = "p2")
    plt.plot(x,y)
    plt.legend(loc='best')
    plt.show()


if __name__ == '__main__':
    main()
