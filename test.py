#Uncomment to fix the test case
import random
N=random.randint(1,100)
K=random.randint(1,100)
C = [random.randint(1,1000) for i in range(N)]

def problem2(N, K, C):
    #sort costs decreasing
    C = sorted(C,reverse = True)
    #从大到小
    #variable to store the cost
    remainder= 0
    n = 0
    m = 1
    cost = 0
    remainder = N%K
    if N>K:
        n = int (N/K)
        while n>0:
            cost = cost + m*sum(C[K*(m-1):K*(m-1)+K])
            m = m+1
            n = n-1
            cost = cost + m*sum(C[N-remainder+1:])
    else:
        cost = cost + sum(C)
    return(cost)
random.seed(10)
N=random.randint(1,100)
K=random.randint(1,100)
C = [random.randint(1,1000) for i in range(N)]

print(problem2(N,K,C))
