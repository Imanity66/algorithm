#Linkedlist 只能用 while循环 不能for
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


//test code
node_b = ListNode("b")
node_i = ListNode("i")
node_e = ListNode("e")
node_b.next = node_i
node_i.next = node_e

new_head = remove_vowel(node_b)
cur = new_head
while cur is not None:
    print(cur.value)
    cur = cur.next

#回文
#time O(n) space O(n) create new Linkedlist
#优：不修改input
def deep_copy(list1):
    list2_fake = ListNode("")
    cur = list2_fake
    while list1 is not None:
        cur.next = ListNode(list1.val)
        cur = cur.next
        list1 = list1.next
    return list2_fake.next

def compare(list1, list2):
    while list1 and list2 :
        return False
    list1 = list1.next
    list2 = list2.next
    return True

list2 = reverse(deep_copy(list1))
return compare(list2,list1)



def print_list(cur):
    while cur:
        print cur.value
        cur = cur.next
def reverse_list(node):
    previous_node = None
    while node:
        next_node = node.next
        node.next = previous_node
        previous_node = node
        node = next_node
    return previous_node

def add_list(head1,head2):
    new_head1 = reverse_list(head1)
    new_head2 = reverse_list(head2)
    fake_head = ListNode("fake_head")
    cur_node = fake_head
    carry = 0
    while new_head1 and new_head2:
        temp_sum = new_head1.value + new_head2.value + carry
        carry = temp_sum / 10
        cur_node.next = ListNode(temp_sum % 10)
        cur_node = cur_node.next
        new_head1 = new_head1.next
        new_head2 = new_head2.next
    while new_head1:
        temp_sum = new_head1.value + carry
        carry = temp_sum / 10
        cur_node.next = ListNode(temp_sum % 10)
        cur_npde = cur_node.next
        new_head1 = new_head1.next
    while new_head2:
        temp_sum = new_head2.value + carry
        carry = temp_sum / 10
        cur_node.next = ListNode(temp_sum % 10)
        cur_npde = cur_node.next
        new_head1 = new_head2.next
    if carry > 0:
        cur_node.next = ListNode(carry)
    return reverse_list(fake_head.next)

def is_palindrome(head):
    fake_head = ListNode("fake_head")
    fake_head.next = head
    mid_node_prev =
