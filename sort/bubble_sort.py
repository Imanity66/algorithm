def bubble_sort(list):
    for i in range(len(list)-1,0,-1):
        for j in range(i):
            if(list[j] > list[j+1]):
                #amazing swap
                list[j],list[j+1] = list[j+1],list[j]
# alist=[2,3,1,0,-5,1]
# bubble_sort(alist)
# print alist
