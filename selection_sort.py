def selection_sort(alist):
    for i in range(len(alist)-1,0,-1):
        max_index = 0
        for j in range(i+1):
            if(alist[j] > alist[max_index]):
                max_index = j
        alist[i],alist[max_index] = alist[max_index],alist[i]
