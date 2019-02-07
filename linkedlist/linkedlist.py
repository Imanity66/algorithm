# -*- coding: utf-8 -*-
"""
Created on Sat Oct  13 17:42:51 2018

@author: Imanity
"""



linkedlist 优点
1.versatility and flexibility
In python, the built in list type is a dynamically resizing array. When it exceeds capacitym
a resizing will be triggered. Linkedlist has no such thing
2. Being able to model the linkedlist based relationshi directly.(hierachical structure)



class ListNode(object):
    def __init__(self, val):
        self.value = val
        self.next = None


def print_node(head): #注:传入的是一个节点, 不是index或者value, 所以curr也是节点
    curr = head
    while curr:
        print(curr.value)
        curr = curr.next
            
#以下为调试
node1 = ListNode("D")
node2 = ListNode("O")
node3 = ListNode("T")
node4 = ListNode("A")

node1.next = node2
node2.next = node3
node3.next = node4

print_node(node1)
        
        
##为什么要用current node :引入curr 是为了避免改变head值
def search_by_value(head, val):
    if not head or not val:
        return None
    curr = head
    while curr :
        if curr.value == val:
            return curr
        curr = curr.next
    return None

#print(search_by_value(node1,"O").value)

def search_by_index(head, index):
    if not head or index <0:
        return None
    curr = head
    while index > 0 and curr:
        curr = curr.next
        index -= 1
    return curr
#print(search_by_index(node1,1).value)    #0的话返回D, 1返回T
    

插到index的位置
Eg. h -> e, add f to index1
res: h -> f -> e
关键在于要找到, 插入的点的前面一个点, 然后接上去就完事了
def add_to_index(head, index,value):

#index: type int, the position where you want to insert(starting)
#adding sentinel to remove additional logic branches
#to avoid special case, we can just simply add a dummy node before
#and use it as the new head.
    fake_head = ListNode(None)
    fake_head.next = head
    insert_place = search_by_index(fake_head,index)
    if insert_place is None:
        return
    new_node = ListNode(val)
    new_node.next = insert_position.next
    insert_position.next = new_node
    return fake_head.next

new_head = add_to_index(node1,2,"xxx")
print_node(new_head)