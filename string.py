# -*- coding: utf-8 -*-
"""
Created on Sun Nov 11 23:56:43 2018

@author: Imanity
"""


#char removal, 从字符串里去掉某几个字符
#快慢指针 ， 慢指针本身是个index,直接就是我们要的东西的位置，快指针每次都往后跑一格
#Time:O(n), space:O(n)
def remove(str):
    lst = list(str)
    i, j = 0 , 0
    while j < len(lst):
        if lst[j] not in ['u','n']:
            lst[i] = lst[j]
            i += 1
        j += 1
    return ''.join(lst[:i]) #join可以把一个list 合并成一个字符串

print (remove("student"))


#去掉头尾的空格，中间部分的空格留一个
#Time:O(n), space:O(n)
#法一，指针
def remove_space(str):
    if not str or len(str) == 0:
        return str
    lst = list(str)
    i, j = 0, 0
    while j < len(lst):
        if lst[j] != ' ' or (j != 0 and lst[j-1] != ' '):
            lst[i] = lst[j]
            i += 1
        j += 1
     #屁股有可能有space，要删
    if i > 0 and lst[-1] == ' ':
        i -= 1
    return ''.join(lst[:i])
    
    
#法二  
def remove_space(str):
    if not str or len(str) == 0:
        return str
    lst = []
    for fast in range(len(str)):
        if str[fast] == ' ' and (fast ==0 or str[fast -1 ] == ' '):
            continue
        lst.append(str[fast])
    if len(lst) > 0 and lst[-1] == ' ' :
        lst.pop()
    return ''.join(lst)


#char de-duplication

'aaaabbbbcccdddcc' => 'abcdc'
#法一,指针
def remove_duplicate(str):
    if not str or len(str) < 2:
        return str
    lst = list(str)
    slow, fast = 1, 1
    while fast < len(lst):
        if lst[fast] != lst[slow - 1]:
            lst[slow] = lst[fast]
            slow += 1
        fast += 1
    return '',join(lst[:slow])

#法二
def remove_duplicate(str):
    if not str or len(str) < 2:
        return str
    fast = 0
    lst = []
    while fast < len(str):
        if len(lst) == 0 or lst[-1] != str[fast]:
            lst.append(str[fast])
        fast += 1
    return ''.join(lst)












