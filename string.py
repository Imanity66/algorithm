# -*- coding: utf-8 -*-
"""
Created on Sun Nov 11 23:56:43 2018

@author: Imanity
"""

1.
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

2.
#char de-duplication. given a sorted array

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


# leave only two letters in duplicated section
aaabbbccc -> aabbcc
#指针步长改成2就完事了
def remove_duplicate(str):
    if not str or len(str) < 2:
        return str
    lst = list(str)
    slow, fast = 2, 2
    while fast < len(lst):
        if lst[fast] != lst[slow - 2]:
            lst[slow] = lst[fast]
            slow += 1
        fast += 1
    return '',join(lst[:slow])

3.
#Reverse
'I love Yahoo' -> 'Yahoo love I'
注意输入的时候把string先转成list, string  immutable

def reverse_helper(lst, left, right):
    while left < right:
        lst[left], lst[right] = lst[right], lst[left]
        left += 1
        right -= 1
    return lst

def reverse_string(string):
    lst = list(string)
    reverse_helper(lst, 0, len(lst) - 1)
    i = 0
    left = i
    right = i
    while i < len(lst):
        if i == len(lst) - 1 or lst[i+1] == " ":
            right = i  #下一个是空格或者到底right就到某个单词的尾巴
            reverse_helper(lst, left, right)
            left = i + 2  #left跳过space到下一个单词的第一个字母
        i += 1
    return ''.join(lst)


abcdef -> efabcd,reverse(str,k)
1)ef + abcd = efabcd
2)reverse(k, end), reverse(0, k), reverse(0, end)

def reverse(lst, k):
    return reverse_helper(lst[k:(len(lst))], 0, len(lst[k:(len(lst))]) - 1) + reverse_helper(lst[0: k], 0, len(lst[0: k])-1)

a = list('abcdef')
k = 4
print(reverse(a,k))



4.
#substring
Robin-Karp : avg case:O(m+n) , worst case:O(m*n)

char --> int, ord('a') = 97
int --> char, chr(97) = 'a'
class RabinKarp:
    def __init__(self):
        self.base = 26   # base for multiplication
        self.mod = 997  # prime number
        
    def strstr(self, strr ,sub):
        if len(sub) > len(strr):
            return -1
        hay_hash, nhash = 0, 0  #hay_hash对应长  nhash 对应短
        power = 1
        for i in range(len(sub)):#计算sub的哈希值
            power = power * self.base % self.mod if i != 0 else 1
            hay_hash = (hay_hash * self.base + ord(strr[i])) % self.mod
            nhash = (nhash * self.base + ord(needle[i])) % self.mod
        
        for i in range(len(sub), len(strr)):
            if hay_hash = nhash and sub == strr[i - len(sub):i]:
                return i - len(sub)
            hay_hash -= (power * ord(strr[i - len(sub)])) % self.mod
            if hay_hash < 0:
                hay_hash += self.mod
            hay_hash = (hay_hash * self.base + ord(strr[i])) % self.mod
        if hay_hash == nhash and sub == strr[len(strr) - len(sub):]:
            return len(strr) - len(sub)
        return -1




