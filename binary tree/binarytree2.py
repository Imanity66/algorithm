Class 24 recursion on tree
"""
Created on Mon Oct 29 22:21:16 2018

@author: Imanity
"""
#find minimum depth (the number of nodes along the shortest path from the root
#node down to the nearest leaf node

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.total_left = 0
#这个不明白
def change_subtree(node):
    if node is None:
        return 0
    left_total = change_subtree(node.left)
    right_total = change_subtree(node.right)
    node.total_left = left_total
    return 1 + left_total + right_total


global_max = -1
res = None
def node_diff(root):
    if root is None:
        return 0
    left_total = node_diff(root.left)
    right_total = node_diff(root.right)
    global global_max
    global res    
    if abs(left_total - right_total) > global_max:
        global_max = abs(left_total - right_total)
        res = root
    return left_total + right_total + 1

node_diff(root)

class TreeNode:
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None
        
class ResultWrapper:
    def __init__(self):
        self.global_max = -1
        self.solution = None
    
def max_diff_node(root, res):
    if not root:
        return 0
    left_toal = max_diff_node(root.left, res)
    right_toal = max_diff_node(root.right, res)
    if abs(left_toal - right_toal ) > res.global_max:
        res.global_max = abs(left_toal - right_toal)
        res.solution = root
    return left_toal + right_toal + 1

def max_diff(root):
    res = ResultWrapper()
    max_diff_node(root, res)
    return res.solution

def getHeight(root):
    if root is None:
        return 0
    if root.left is None and root.right is None:
        return 1
    left = getHeight(root.left) if root.left else float('inf')
    right = getHeight(root.right) if root.right else float('inf')
    return min(left, right) + 1

def BST(root):
    if root is None:
        return True
    
    min = float('-inf')
    max = float('inf')
    return isBST(root, min, max)

def isBST(root, min, max):
    if root is None:
        return True
    if root.val <= min or root.val >= max:
        return False
    return isBST(root.left,min,root.val) and isBST(root.right,root.val,max)


方法2，中序遍历
list可变, 直接prev = None的话 inorder走一遍他永远是None
和传统中序遍历相比, 多传一个prev, prev是上一个节点的值, 理论上他要比当前节点小

def isValidBST(root):
    prev = [None]
    res = [True]
    inorder(root, prev, res)
    return res[0]

def inorder(root, prev, res):
    if not root:
        return
    inorder(root.left, prev, res)
    if prev[0] and (prev[0] >= root.val):
        res[0] = False
        return 
    prev[0] = root.val
    
    inorder(root.right, prev, res)
    
    
是否平衡二叉树
class Solution(object):
  def isBalanced(self, root):

    if root is None:
      return True
    elif(abs(self.height(root.left) - self.height(root.right)) > 1):
      return False
    else:
      return (self.isBalanced(root.left) and self.isBalanced(root.right))
