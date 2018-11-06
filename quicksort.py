import random
def partition(lst,start,end,p_index):
    lst[p_index], lst[end] = lst[end], lst[p_index]
    store_index = start
    p = lst[end]
    for i in range(start, end):
        if lst[i] < p:
            lst[i] , lst[store_index] = lst[store_index] , lst[i]
            store_index +=1
    lst[store_index], lst[end] = lst[end], lst[store_index]
    return store_index

def quick_sort(lst, start, end):
    if lst is None or len(lst)==0:
        return lst
    if start>= end:
        return
    p_index = random.randrange(start, end+1)
    new_p_index = partition(lst, start, end, p_index)
    quick_sort(lst, start , new_p_index-1)
    quick_sort(lst, new_p_index+1, end)

alist=[28,1,-1,5]
quick_sort(alist,0,len(alist)-1)
print(alist)
