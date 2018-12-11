def reverse_list(head):
    if head is None or head.next is None:
        return head
    next_node = head.next
    new_head = reverse_list(head.next)
    print("head is",head.val,"head.next is",next_node,"new_head is", new_head.value)
#head是当前层的node
    next_node.next = head
    head.next = None
    return new_head






def reverse(node):
    previous_node = None
    while node is not None:
        next_node = node.next    #把next存下来给最后的node用
        node.next = previous_node  #一开始把0号兄弟指向none  然后把1->0 , 2->1

        previous_node = node   #为下一层循环用
        node = next_node
