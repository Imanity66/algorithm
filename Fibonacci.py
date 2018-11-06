import sys
sys.setrecursionlimit(100000)
def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1

    return fib(n-1) + fib(n-2)

def fib(n):
    if n <= 0:
        return 0
    if n ==1:
        return 1
    res = [0,1]
    for i in range(2,n+1):
        res.append(res[i-1]+res[i-2])
    return res[-1]
