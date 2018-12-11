def insertion_sort(alist):
    for in range(1,len(alist)):
        cur = alist[i]
        k = i
        while k>0 and cur < alist[k-1]:
            alist[k] = alist[k - 1]
            k-=1
            alist[k] = cur
