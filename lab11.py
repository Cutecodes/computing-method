import numpy as np 
import matplotlib.pyplot as plt 

def dis(x,y,x0,y0,x1,y1):
    return np.abs((y1-y0)*(x-x0)/(x1-x0)+y0-y)

def dis1(x,y,x0,y0,x1,y1):
    return np.abs((y1-y0)*(x-x0)-(x1-x0)*(y-y0))/np.sqrt((y1-y0)**2+(x1-x0)**2)

def TPP(P,begin,end,delta):
    if end-begin==1:
        return [begin,end]
    disArray = [0 for i in range(begin,end+1)]
    maxindex = -1
    maxdis = -1
    for i in range(begin,end+1):
        disArray[i-begin] = dis(i,P[i],begin,P[begin],end,P[end])
        if disArray[i-begin]>maxdis:
            maxdis = disArray[i-begin]
            maxindex = i
    
    ans = []
    if maxdis>delta:
        t1 = TPP(P,begin,maxindex,delta)
        t2 = TPP(P,maxindex,end,delta)
    
        for i in t1:
            ans.append(i)
        ans.append(maxindex)
        for i in t2:
            ans.append(i)
    else:
        ans.append(begin)
        ans.append(end)
    ans = list(set(ans))
    ans.sort()
    return ans
    

def TP(P,delta):
    return TPP(P,0,len(P)-1,delta)

def main():
    delta = 2
    l = 100
    P = []
    x = []
    for i in range(l):
        x.append(i)
        if i ==0:
            P.append(np.random.randint(1, 10))
        else:
            P.append(np.random.randint(P[i-1]-2, P[i-1]+3))
    plt.scatter(x,P,color="red")

    ans = TP(P,delta)
    P2 = [P[i] for i in ans]
    x = ans
    plt.plot(x,P2)
    plt.show()

if __name__ == "__main__":
    main()
    