Class 22 Binary Tree
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
 #   if not root:
     if root is None:
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

#if root is size n , then O(n)
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
    curr = []
    while q:
        head = q.pop(0)
        if head.left:
            next.append(head.left)
        if head.right:
            next.append(head.right)
        curr.append(head.val)
        
        if not q:
            print(curr)
            if next:
                q = next
                next = []
                curr = []
def level(root):
    frontier = [root]
    while frontier:
        next = []
        curr = []
        for u in frontier:
            curr.append(u.val)
            if u.left:
                next.append(u.left)
            if u.right:
                next.append(u.right)
        print(curr)
        frontier = next


#做一个分支的就行,用递归
#下面层变化完了之后, 上面层其实还没变, 1的left还是2, 1的right还是3, 然后操作就会把上面的东西翻到最下面
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


Invert a binary tree 左右反一下

def invert(root):
    if nor root:
        return
    invert(root.left)
    invert(root.right)
    root.left, root.right = root.right, root.left
    return
    
给一个排好序的整数序列(list), 把他插成一个balanced BST

def bst(nums, start, last):
    if start > last:
        return None
    mid = (start + last) / 2
    root = TreeNode(nums[mid])
    root.left = bst(nums, start, mid-1)
    root.right = bst(nums, mid+1, last)
    return root
    
    
    
    
    