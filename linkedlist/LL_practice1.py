#利用 dummy node
#空间复杂度 O(1)  只创建了merge_head 和curr 
# 注:while loop结束之后只需要接上某一个链表就行,不需要再写循环
class ListNode(object):
    def __init__(self,value):
        self.next = None
        self.val = value
def merge_list(head1,head2):
    if head1.value<=head2.value:
        curr = head1
        head1 = head1.next
    else:
        curr = head2
        head2 = head2.next
    merge_head = curr
    while head1 and head2:
        if head1.value<=head2.value:
            curr.next = head1
            curr = curr.next
            head1 = head1.next
        else:
            curr = head2
            curr = curr.next
            head2 = head2.next
    if head1:
        curr.next = head1
    if head2:
        curr.next = head2
    return merge_head

def print_list(res_head):
    while (res_head!=None):
        res_head = res_head.next
        print(res_head)
node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node1.next = node2
node2.next = node3

node0 = ListNode(0)
node4 = ListNode(4)
node5 = ListNode(5)

node0.next = node4
node4.next = node5
print_list(merge_list(node1,node0))


#找中点
#快慢指针  slow fast pointers
def mid_node(head):
    if head is None:
        return head
    slow, fast = head, head
    count = 0
    while fast:
        count += 1
        if count == 1:
            fast = fast.next
        if count == 2:
            count = 0
            slow = slow.next
            fast = fast.next
    return slow

#reverse a single linkedlist
# ****难****
1->2->3->4
1<-2<-3<-4

def reverse_list(head):
    curr = head
    prev_node = None
    while curr:
        next_node = curr.next
        curr.next = prev_node
        prev_node = curr
        curr = next_node
    return prev_node #这里很tricky, 因为最后一轮curr已经空了,只有prev有值好吧

#print_list(reverse_list(node1))     

