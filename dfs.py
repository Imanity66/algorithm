
time:O(2^n), space:O(n)
def subset(num):
    cur = []
    res = []
    backtrack(num, 0, cur, res)
    return res

def backtrack(num, i, cur, res):
    if i == len(num):
        res.append(cur[:])
        return
    cur.append(num[i])
    backtrack(num, i+1, cur, res)
    cur.pop()
    backtrack(num, i+1, cur, res)



def getFactors(n):
    solution = []
    res = []
    getFactorsHelper(n, 2, solution, res)
    res.pop()
    return res
def getFactorsHelper(n, index, solution, res):
    if n == 1:
        res.append(solution[:])
        return
    for i in range(index, n+1):
        solution.append(i)
        getFactorsHelper(n/i, i, solution, res)
        solution.pop()



def generateParentheses(n):
    cur = []
    res = []
    helper(0, 0, n, cur, res)
    return res
def helper(left, right, n, cur, res):
    if left == n and right == n:
        res.add('',join(cur))
        return
    if left < n:
        cur.append("(")
        helper(left+1, right, n, cur, res)
        cur.pop()
    if right < left:
        cur.append(')')
        helper(left, right + 1, n, cur, res)
        cur.pop()
