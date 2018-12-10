# -*- coding: utf-8 -*-
"""
Created on Mon Nov  5 21:29:32 2018

@author: Imanity
"""
#Time O(logn)
def sift_up(arr,i):
    parent = (i - 1)/2
    larget = i
    if parent >= 0 and arr[i] < arr[parent]:
        larget = parent
    if larget !=i:
        arr[larger], arr[i] = arr[i], arr[larget]
        sift_up(arr, larger)

arr = [0, 1, 5, 6, 8, 01]
sift_up(arr, len(arr) - 1)
print(arr)
[-1, 1, 0, 6, 8, 5]

def sift_down(array, index):
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

def sift_down(array, index):
    left = index * 2 + 1
    right = index * 2 + 2
    while left < len(array) or right < len(array):
        smaller = index
        if left < len(array) and array[smaller] > array[left]:
            smaller = left
        if right < len(array) and array[smaller] > array[right]:
            smaller = right
        if smaller == index:
            break

        array[index] , array[smaller] = array[smaller], array[index]
        index = smaller
        left = index * 2 + 1
        right = index * 2 + 2

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
