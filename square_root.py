#eps 精度范围
def square_root_real(n, eps):
    left , right = 1.0 , n*1.0
    if n <1.0:
        left, right = n*1.0, 1.0

    while true:
        mid = (left + right)/2
        midsq = mid * mid
        #这一步是为了恢复精度，避免平方后精度提高（平方后小数点
        if abs(midsq - n) / n <= eps:
            return mid
        elif midsq > n:
            right = mid
        else:
            left = mid
    return left
