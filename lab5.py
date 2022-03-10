import numpy as np 
from matplotlib import pyplot as plt 

def SOR(n,N0,A,b,w,e):
    x = np.zeros((n,1))
    dx = np.zeros((n,1))
    for k in range(1,N0+1):
        for i in range(n):
            S = 0
            for j in range(n):
                S += A[i][j]*x[j]
            dx = w*(b[i]-S)/A[i][i]
            x[i]= x[i] + dx
            
        P0 = 0.0       
        for i in range(n):
            S = 0
            for j in range(n):
                S += A[i][j]*x[j]
            P = b[i]-S
            if abs(P)>abs(P0):
                P0 = P
        
        if abs(P0)<e:
            print("w:",w)

            print("P0:",P0)
            print("k:",k)
            print("x:")
            print(x)
            return
        
    print("经过N0次迭代仍没达到精度要求！")

def main():
    A = np.array([
        [4,-1,0,-1,0,0],
        [-1,4,-1,0,-1,0],
        [0,-1,4,0,0,-1],
        [-1,0,0,4,-1,0],
        [0,-1,0,-1,4,-1],
        [0,0,-1,0,-1,4]
    ])
    e = 1e-5
    b = np.array([[2,1,2,2,1,2]]).T
    w1 = 1.0
    w2 = 1.1
    SOR(6,100,A,b,w1,e)
    print("-----------")
    SOR(6,100,A,b,w2,e)


if __name__ =="__main__":
    main()