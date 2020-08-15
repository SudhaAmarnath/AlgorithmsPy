# https://www.hackerrank.com/challenges/computing-the-correlation/problem

def std(X):
    temp=[]
    X_mean=float(sum(X)/len(X))
    for val in X:
        temp.append((val-X_mean)**2)
    return((sum(temp))**0.5)

def cov(X,Y):
    temp=[]
    X_mean=float(sum(X)/len(X))
    Y_mean=float(sum(Y)/len(Y))
    for i,j in zip(X,Y):
        temp.append((i-X_mean)*(j-Y_mean))
    return sum(temp)

def pearson(X,Y):
    
    return(cov(X,Y)/(std(X)*std(Y)))


def main():
    n = int(input())
    M = []
    P = []
    C = []
    for i in range(n):
        marks = input().split()
        marks = [int(a) for a in marks]
        M.append(marks[0])
        P.append(marks[1])
        C.append(marks[2])
    rMP = pearson(M,P)
    rPC = pearson(P,C)
    rCM = pearson(C,M)
    print("%.2f"%rMP)
    print("%.2f"%rPC)
    print("%.2f"%rCM)
    
if(__name__=="__main__"):
    main()
