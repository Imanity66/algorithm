# -*- coding: utf-8 -*-
"""
Created on Sat Nov 10 22:03:11 2018

@author: zfy
"""
import numpy as np
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.size = 0

def BST(arr):
    if not arr:
        return None

    # find middle
    mid = int((len(arr)) / 2)

    # make the middle element the root
    root = TreeNode(arr[mid])

    # left subtree of root has all
    # values <arr[mid]
    root.left = BST(arr[:mid])

    # right subtree of root has all
    # values >arr[mid]
    root.right = BST(arr[mid+1:])
    return root

array = list(np.arange(5))
root = BST(array)

#Calculate Number
# Maximum Depth
class Solution:
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        else:
            left_height = self.maxDepth(root.left)
            right_height = self.maxDepth(root.right)
            return max(left_height, right_height) + 1

# Given a binary tree, determine if it is height-balanced.
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True

        elif (abs(self.height(root.left) - self.height(root.right)) > 1):
            return False
        else:
            return (self.isBalanced(root.left) and self.isBalanced(root.right))

    def size(self, root):
        if root is None:
            return 0
        elif (root.left is None and root.right is None):
            return 1
        elif root.right is None:
            return 1 + self.size(root.left)
        elif root.left is None:
            return 1 + self.size(root.right)
        else:
            return 1 + self.size(root.left) + self.size(root.right)


    def get_size(self, root):
        if not root:
            return 0
        left = get_size(root.left)
        right = get_size(root.right)
        return 1 + left + right

    def get_height(root):
        if not root:
            return 0
        left = get_height(root.left)
        right = get_height(root.right)
        return 1 + max(left, right)


    def printTree(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[str]]
        """
        if not root: return [""]
        def getDepth(root):
            if not root:
                return 0
            return 1 + max(getDepth(root.left), getDepth(root.right))
        d = getDepth(root)
        cols = 2 ** d - 1
        self.res = [["" for i in range(cols)] for j in range(d)]
        def helper(root, d, pos):
            self.res[-d - 1][pos] = str(root.val)
            if root.left: helper(root.left, d - 1, pos - 2 ** (d - 1))
            if root.right: helper(root.right, d - 1, pos + 2 ** (d - 1))
        helper(root, d - 1, 2 ** (d - 1) - 1)
        return self.res

    def insert(self, root, node):
        if root.val is None:
            root = node
            root.size = root.size + 1
        else:
            if root.val < node.val:
      #          if root.right is None:
      #              root.right = node
      #              root.size = root.size + 1
      #          else:
                self.insert(root.right, node)
            elif root.val > node.val:
      #          if root.left is None:
     #               root.left = node
     #               root.size = root.size + 1
                self.insert(root.left, node)
        return root

    def remove(self, root, value):
        ''' For deleting the node '''
        if root is None:
            return None

        # if current node's data is less than that of root node, then only search in left subtree else right subtree
        if root.val < value:
            root.right = self.remove(root.right, value)
        elif root.val > value:
            root.left = self.remove(root.left, value)
        else:
            # deleting node with one child
            if root.left is None:
                temp = root.right
                root = None
                return temp
            elif root.right is None:
                temp = root.left
                root = None
                return temp
            elif root.right is None and root.left is None:
                root = None
                return None
            # deleting node with two children
            # first get the inorder successor
            temp = self.minValueNode(root.right)
            root.val = temp.val

            #这样做 左树不变, 自己的key变个数字,然后右树变一下


            root.right = self.remove(root.right, temp.val)
        return root

    def minValueNode(self, root):
        current = root
##直接root.left
        # loop down to find the leftmost leaf
        while(current.left is not None):
            current = current.left

        return current



T = Solution()
root = T.remove(root,2)
print(T.printTree(root))
