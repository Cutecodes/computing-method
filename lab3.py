import numpy as np 

a = 0
b = 1
delta = 0.5*10e-6

def f(x):
    if x==0:
        return 1
    else:
        return np.sin(x)/x

T = {0:{0:0}}
T[0][0] = 0.5*(b-a)*(f(a)+f(b))
k = 1

while True:
    for i in range(k+1):
        if(i==0):
            sum = 0
            for j in range(2**(k-1)):
                sum += f(a+(2*j+1)*(b-a)*0.5**k)
            
            T[i].setdefault(k-i)

            T[i][k-i] = 0.5*T[0][k-1] + 0.5**k*(b-a)*sum
        else:
            if(k-i==0):
                T[i]={}
            T[i].setdefault(k-i)
            T[i][k-i] = (4**i*T[i-1][k-i+1]-T[i-1][k-i])/(4**i-1)
    if(abs(T[k][0]-T[k-1][0]<delta)):
        print(T[k][0])
        break
    k +=1
