# -*- coding: utf-8 -*-
"""
Created on Sat Oct 27 23:23:40 2018

@author: Imanity
"""

class TreeNode:
    def__init__(self, x):
        self.val = x
        self.left = None
        self.right = None
##以下三个 time:O(n) space：O(h)
##先序遍历
def preorder_traversal(self, root):
    res = []
    self.helper(root, res)
    return res

def helper (self, root, res):
    if not root:
        return
    res.append(root.val)
    self.helper(root.left, res)
    self.helper(root.right, res)
    
##中序遍历
    
def helper(self, root, res):
    if not root:
        return
    self.helper(root.left, res)
    res.append(root.val)
    self.helper(root.right, res)
    
#后序遍历
def helper(self, root, res):
    if not root:
        return
    self.helper(root.left, res)
    self.helper(root.right, res)
    res.append(root.val)
    
def get_height(root):
    if not root:
        return 0
    left = get_height(root.left)
    right = get_height(root.right)
    return 1 + max(left, right)
#time:O(n) space:O(max(len(q)))
def level(root):
    q = [root]
    next = []
    line = []
    while q:
        head = q.pop(0)
        if head.left:
            next.append(head.left)
        if head.right:
            next.append(head.right)
        line.append(head.val)
        
        if not q:
            print(line)
            if next:
                q = next
                next = []
                line = []
                
def upside_bst(root):
    if not root:
        return root
    if not root.left and not root.right:
        return root
    left_tree = upside_bst(root.left)
    root.left.left = root.right
    root.left.right = root
    root.left = None
    root.right = None
    return left_tree