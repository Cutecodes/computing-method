import numpy as np
a = np.array([[0,2,0,1],
              [2,2,3,2],
              [4,-3,0,1],
              [6,1,-6,-5]],dtype=np.float)
b = np.array([[0],
              [-2],
              [-7],
              [6]])

def BiCGSTAB(a,b,x,tol=1.0e-5,limit=100):
    r = b - np.dot(a,x)
    r0_hat = r
    rho0 = 1.0
    alpha = 1.0
    w0 = 1.0
    iters = 0
    rho1 = np.dot(np.transpose(r0_hat),r)
    while(True):
        iters = iters + 1
        converged = (np.linalg.norm(r)<tol*np.linalg.norm(b))
        if converged==True or iters>=limit:
            break
        beta = (rho1/rho0)*(alpha/w)
        p = r + 1
        
def CG(A,b,x0,e=1.0e-6,limit=100):
    b = np.dot(A.T,b)
    A = np.dot(A.T,A)
    A = A.copy()
    '''
    l = len(A)
    for i in range(l):
        for j in range(i,l):
            A[i][j] = (A[i][j]+A[j][i])/2
            A[j][i] = A[i][j]
    '''
    k = 0
    r = b-np.dot(A,x0)
    x = x0
    d = r
    dn =[]
    while True:
        if abs(np.linalg.norm(r))<e or k>limit:
            return x,dn
        a = np.dot(r.T,r)/np.dot(np.dot(d.T,A),d)
        x = x + a*d

        ri = b - np.dot(A,x)
        beta = np.dot(ri.T,ri)/np.dot(r.T,r)
        d = ri + beta*d
        dn.append(d)
        r = ri
        k +=1

def main():
    '''
    a = np.array([[9,18,9,-27],
              [18,45,0,-45],
              [9,0,126,9],
              [-27,-45,9,135]])
    b = np.array([[1],
              [2],
              [16],
              [8]])
    '''
    x0 = np.array([[0,0,0,0]]).T
    x,dn = CG(a,b,x0)
    print("方程的解：")
    #print(a)
    print(x)
    #print(np.dot(a,x))
    print("A的共轭方向为：")
    for i in dn:
        print(i)
if __name__=='__main__':
    main()

    
    
         
