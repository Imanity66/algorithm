def removenodes(head, target):
    if not head:
        return fake_head
    fakehead = ListNode(0)
    fakehead.next = head
    prevnode,currnode = fakehead, fakehead.next
    while currnode:
        if currnode.val == target:
            prevnode.next = currnode.next
        else:
            prevnode = currnode
    newhead, fakehead.next = fakehead.next, None
    return newhead
