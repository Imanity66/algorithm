def permute(nums):
    perm, res = [], []
    def impl(i):
         if i == len(nums):
             res.append(perm[:])#直接perm是一个reference
             return

        for n in nums:
            if n not in perm:
                perm.append(n)
                impl(i + 1)
                perm.pop()




def permute(nums):
    res = [[]]
    for num in nums:
        res = [perm[:i] + [num] + perm[i:] for perm in res for i in range(len(perm) + 1)]

    return res
