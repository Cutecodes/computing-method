import numpy as np 
import matplotlib.pyplot as plt

def liner_LSM(x,y):
    #线性最小二乘法
    tx = x.copy()
    ty = y.copy()   
    t = np.array([[1 for i in range(tx.shape[1])]])
    tx = np.r_[t,tx]
    tx = tx.T
    ty = ty.T
    a = np.dot(np.dot(np.linalg.inv(np.dot(tx.T,tx)),tx.T),ty)
    return a

def main():
    t = np.array([[1,2,4,8,16,32,64]])
    w = np.array([[4.22,4.02,3.85,3.59,3.44,3.02,2.59]])
    
    ln_t = np.log(t)
    ln_w = np.log(w)

    #print(ln_t)
    #print(ln_w)
    a0,a1 = liner_LSM(ln_t,ln_w)
    
    print("c的值为：%.5f"%np.exp(a0))
    print("lambda的值为：%.5f"% a1)
    x = np.linspace(0,5,1000)

    fx = a0 + a1*x

    plt.scatter(ln_t,ln_w,color = "blue",marker = 'o')

    plt.plot(x,fx,color = "blue")
    print("MSE:%.5f"%(np.sum((np.exp(a0 + a1*ln_t)-w)**2)/t.shape[1]))
    plt.show()
    plt.scatter(t,w,color = "blue",marker = 'o')
    x = np.linspace(0.1,65,1000)
    y = np.exp(a0)*x**a1
    plt.plot(x,y,color = "blue")
    plt.show()
    
if __name__ == '__main__':
    main()