#利用 dummy node
#空间复杂度 O(1)  因为没有创建新的node , 只有nead_head 和curr_node 创建了
class ListNode(object):
    def __init__(self,value):
        self.next = None
        self.val = value
def merge_list(head1,head2):
    new_head = ListNode(0)
    curr_node = new_head
    while head1 is not None and head2 is not None:
        if head1.val <= head2.val:
            curr_node.next = head1    #insert node
            head1 = head1.next
        else:
            curr_node.next = head2
            head2 = head2.next
        curr_node = curr_node.next
    if(head1 is not None):
        curr_node.next = head1
    if(head2 is not None):
        curr_node.next = head2
    return new_head.next
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
