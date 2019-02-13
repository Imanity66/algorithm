#像这种第一值就可能被丢掉的情况就要用fake_node
#fakenode另一个作用是一直指向头部, return的时候就可以return它,否则curr已经跑到底了
#去元音
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


node1 = ListNode("b")
node2 = ListNode("i")
node3 = ListNode("e")
node4 = ListNode("b")
node5 = ListNode("i")
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
print_node(remove_vowel(node1))

#判断是否回文
#time O(n) space O(n) create new Linkedlist
#优：不修改input
def deep_copy(list1):
    if list1 is None:
        return None
    fake_node = ListNode(None)
    curr = fake_node
    while list1:
        curr.next = ListNode(list1.value)
        curr = curr.next
        list1 = list1.next
    return fake_node.next

def compare(list1, list2):
    while list1 and list2:
        if list1.value != list2.value:
            return False
       list1 = list1.next
       list2 = list2.next
    return True

list2 = reverse(deep_copy(list1))
return compare(list2,list1)


def reverse_list(head):
    curr = head
    prev_node = None
    while curr:
        next_node = curr.next
        curr.next = prev_node
        prev_node = curr
        curr = next_node
    return prev_node 


#两个链表相加
注:从尾巴开始加, 考虑进位
def add_list(head1,head2):
    new_head1 = reverse_list(head1)
    new_head2 = reverse_list(head2)
    fake_node = ListNode("fake_head")
    curr = fake_node
    carry = 0
    while new_head1 and new_head2:
        temp_sum = new_head1.value + new_head2.value + carry
        carry = temp_sum / 10
        curr.next = ListNode(temp_sum % 10)
        curr = curr.next
        new_head1 = new_head1.next
        new_head2 = new_head2.next
    while new_head1:
        temp_sum = new_head1.value + carry
        carry = temp_sum / 10
        curr.next = ListNode(temp_sum % 10)
        curr = curr.next
        new_head1 = new_head1.next
    while new_head2:
        temp_sum = new_head2.value + carry
        carry = temp_sum / 10
        curr.next = ListNode(temp_sum % 10)
        curr = curr.next
        new_head1 = new_head2.next
    if carry > 0:
        curr.next = ListNode(carry)
    return reverse_list(fake_node.next)

