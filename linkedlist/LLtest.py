# -*- coding: utf-8 -*-
"""
Created on Sat Feb  9 20:14:23 2019

@author: Imanity
"""

class ListNode(object):
    def __init__(self,val):
        self.value = val
        self.next = None

def print_list(head):
    curr = head
    while curr:
        print(curr.value)
        curr = curr.next
        
def remove_vowel(head):
    fake_node = ListNode(None)
    fake_node.next = head
    curr = fake_node
    while curr.next:
        if curr.next.value in("a","e","i","o","u"):
            curr.next = curr.next.next
        else:
            curr = curr.next

    return fake_node.next

node1 = ListNode("a")
node2 = ListNode("b")
node3 = ListNode("c")
node4 = ListNode("d")
node5 = ListNode("e")
node6 = ListNode("f")
node7 = ListNode("g")
node8 = ListNode("8")

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node6
node6.next = node7
node7.next = node8


print_list(remove_vowel(node1))