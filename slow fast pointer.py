#快慢指针  slow fast pointers
def mid_node(head):
    if head is None:
        return head
    slow,fast = head, head
    count = 0
    while fast is not None:
        count += 1
        if counj == 1:
            fast = fast.next
        if count == 2:
            count = 0
            slow = slow.next
            fast = fast.next
    return slow

def find_mid(head):
    if head is None or head.next is None:
        return head

    slow,fast = head,head
    while fast.next and fast.next.next:
        fast = fast.next.next
        slow = slow.next
    return slow
