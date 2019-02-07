# -*- coding: utf-8 -*-
"""
Created on Sat Nov  3 21:21:48 2018

@author: Imanity
"""

class Node(object):
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.left = self.right = None

class BinarySearchTree(object):
    def __init__(self):
        self.__root = None

    def __query(self, root ,key):
        if not 4root:
            return None

        if key < root.key:
            return self.__query(root.left, key)## 只在return的时候用到递归，称为tail recursion  尾递归， 很容易写成while loop
        elif key > root.key:
            return self.__query(root.right, key)
        else:
            return root.value

    def query(self, key):
        return self.__query(self.__root, key)

    #循环写法
    def query(self, key):
        curr = self.__root
        while curr:
            if key < curr.key:
                curr = curr.left
            elif key > curr.key:
                curr = curr.right
            else:
                return curr.value
        return None

    def FindMinimum(root):
        if not root:
            return None
        return FindMinimum(root.left) or root

    def FindMaximum(root):
        if not root:
            return None
        return FindMaximum(root.right) or root


    #从右边开始的中序遍历,可以推广到找第k大的值


    time cost O(h)
    class solution()
        def __init__(self):
            self.count = 2
            self.result = None
        def find_second_largest(self.root):
            self.traverse(root)
            return self.result
        def traverse(root):
            if root is None:
                return
            self.traverse(root.right)
            self.cnt -= 1
            if self.cnt == 0 :
                self.result = root.val
                return
            self.traverse(root.left)





    def FindFirstLargerThanTarget(root, target):
        if not root:
            return None
        if root.value == target: #往右找
            return FindMinimum(root.right)
        elif root.value < target:##往右找
            return FindFirstLargerThanTarget(root.right, target)
        else:
            return FindFirstLargerThanTarget(root.left, target) or root

    def __insert(self, root, key, value):
        ##return the root node of the modified tree after insertion
        if not root:##为空直接插
            return _Node(key, value)
        if root.key == key:
            root.value = value

        elif root.key < key:
            root.right = self.__insert(root.right, key, value)
        else:
            root.left = self.__insert(root.left, key, value)

        return root



    def __deleteMin(self, root):
        if not root.left:
            return root.right

        root.left = self.__deleteMin(root.left)
        return root




    def __delete(self,root,key):
        #return the root node of the modified tree after deletion
        if not root:
            return None

        if root.key < key:
            root.right = self.__delete(root.right, key)

        elif root.key > key:
            root.left = self.__delete(root.left, key)
        else:
            if not root.right:#只有左子树
                return root.left
            if not root.left:#只有右子树
                return root.right

            min_node = FindMinimum(root.right)
            t = root
            root = min_node

            root.right = self.__deleteMin(t.right)
            root.left = t.left
    del delete(self, key):
    self.__root = self.__delete(self.__root, key)
