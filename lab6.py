import numpy as np 
import matplotlib.pyplot as plt

def cond2(x):
    #x = matrix(x)
    eigenvalue,_ = np.linalg.eig(x)
    return eigenvalue.max()/eigenvalue.min()

def fun1():
    ans = []
    xn = []
    for n in range(2,13):
        xn.append(n)
        h = np.zeros((n,n),dtype=np.float)
        for i in range(n):
            for j in range(n):
                h[i][j]=1.0/(i+j+1)
        ans.append(np.log(cond2(h)))
    plt.plot(xn,ans)
    plt.show()
    return ans,xn

def fun2():
    ans = []
    xn = []
    for n in range(2,13):
        xn.append(n)
        h = np.zeros((n,n),dtype=np.float)
        d = np.zeros((n,n),dtype=np.float)
        for i in range(n):
            for j in range(n):
                h[i][j]=1.0/(i+j+1)
                if i==j:
                    d[i][j]=np.sqrt(h[i][j])
        d = np.matrix(d)
        h = np.matmul(np.matmul(d.I,h),d.I)
        ans.append(np.log(cond2(h)))
    plt.plot(xn,ans)
    plt.show()
    return ans,xn
def fun3():
    for n in range(4,13):
        b = np.empty((n,1),dtype=np.float)
        print("n =",n)
        print("b:")
        print(b)
        h = np.zeros((n,n),dtype=np.float)
        d = np.zeros((n,n),dtype=np.float)
        for i in range(n):
            for j in range(n):
                h[i][j]=1.0/(i+j+1)
                if i==j:
                    d[i][j]=np.sqrt(h[i][j])
        h = np.matrix(h)
        h2 = h
        print("x1:")
        print(np.matmul(h.I,b))
        d = np.matrix(d)
        h = np.matmul(np.matmul(d.I,h),d.I)
        print("x2:")
        print(np.matmul(np.matmul(np.matmul(d.I,h.I),d.I),b))
        print("x3:")
        print(np.linalg.solve(h2,b))
        print("*"*30)
def fun4():
    n = int(input("请输入n："))
    b = []
    for i in range(n):
        b.append(float(input()))
    b = np.array(b)
    b = b.reshape(-1,1)
    h = np.zeros((n,n),dtype=np.float)
    d = np.zeros((n,n),dtype=np.float)
    for i in range(n):
        for j in range(n):
            h[i][j]=1.0/(i+j+1)
            if i==j:
               d[i][j]=np.sqrt(h[i][j])
    h = np.matrix(h)
    h2 = h
    print("x1:")
    print(np.matmul(h.I,b))
    d = np.matrix(d)
    h = np.matmul(np.matmul(d.I,h),d.I)
    print("x2:")
    print(np.matmul(np.matmul(np.matmul(d.I,h.I),d.I),b))
    print("x3:")
    print(np.linalg.solve(h2,b))

def main():
    ans1,x = fun1()
    ans2,_ = fun2()
    plt.plot(x,ans1)
    plt.plot(x,ans2)
    plt.show()
    fun3()
    fun4()

if __name__ == "__main__":
    main()