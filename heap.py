# -*- coding: utf-8 -*-
"""
Created on Mon Nov  5 21:29:32 2018

@author: Imanity
"""


heap的优点
找最大最小值时间复杂度 O(nlogn)

store it as an array(0-based index array)
left_node_index = parent_node_index * 2 + 1
right_node_index = parent_node_index * 2 +2


min-heap:子节点小于parent node




#Time O(logn)
# 两个/ , 即去掉小数部分, 也可以写int()
def decrease(arr,i):
    parent = (i - 1)//2
    if parent >= 0 and arr[i] < arr[parent]:
        arr[parent], arr[i] = arr[i], arr[parent]
        decrease(arr, parent)

arr = [0, 1, 5, 6, 8, -1]
sift_up(arr, len(arr) - 1)
print(arr)
[-1, 1, 0, 6, 8, 5]

# Recursion
def heapify(array, index):
    left = index * 2 + 1
    right = index * 2 + 2
    small = index
    if left < len(array) and array[small] > array[left]:
        small = left
    if right < len(array) and array[small] > array[right]:
        small = right
    if small != index:
        array[small], array[index] = array[index], array[small]
        sift_down(array, small)



#时间复杂度 O(n)

自下而上建堆的耗时和自上而下不一样, 不是nlogn
从非叶子节点开始比较
假设总高度是h , 第x层元素的计算量是 2^x * (h - x)
S = 2^(h-1) + 2^(h-2) * 2 + 2^(h-3) * 3 +.... +2*(h-1) + h
错位相减
得到S = n - logn

def build_heap(arr):
    for i in range(len(arr)//2 - 1,-1 ,-1):
        heapify(arr, i)


heapq

heap = []
heappush(heap,item)
item = heappop(heap)# pop the smallest
item = heap[0]
heapify(x)#transform list into a heap, in lieanr time

heapify all element O(n), call pop k times  O(k logn)
time cost O(n + k logn)
import heapq
def kSmallest(array, k):
    if not array:
        return []
    res = []
    heapq.heapify(array)
    for i in range(k):
        res.append(heapq.heappop(array))
    return res



若heap的大小仅有k, 从N个数中找到k个最小值, 要利用max-heap
max-heap通过minheap取负来表示
def kSmallestII(array,k):
    if not array:
        return []
    
    res = [-i for i in array[:k]]
    heapq.heapify(res)

    for i in array[k:]:
        if i < -res[0]:
            heapq.heappop(res)
            heapq.heappush(res, -i)
    return [-i for i in res]
   # for i in range(k,len(array)):
   #     if array[i] < -res[0]:
   #         heapq.heappop(res)
   #         heapq.heappush(res, -array[i])        
   # return [-i for i in res]
   

merge k sorted array
step1: 把每个array的第一项丢进heap
step2:对heap进行pop的时候, push进对应array的下一个值

def mergek(arrays):
    if not arrays:
        return None
    heap = []
    for i in range(len(arrays)):
        if arrays[i]:
            heap.append((arrays[i][0],i,0))#元素,对应array的index,对应element的index
    heapq.heapify(heap)
    res = []
    
    while heap:
        value, array_index, element_index = heapq.heappop(heap)
        res.append(value)
        if element_index < len(arrays[array_index]) - 1:
            heapq.heappush(heap, (arrays[array_index][element_index + 1], array_index, element_index + 1))
    return res
#跑过测试, 是对的