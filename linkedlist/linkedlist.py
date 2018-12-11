class ListNode(object):
    def __init__(self,value):
        self.next = next
        self.val = value
    def __eq__(self, other):
        return isinstance(other, ListNode) and self.value == other.value

node1 = ListNode("N")
node2 = ListNode("E")
node1.next = node2

def print_node(head):
    curr = head
    while curr:
        print curr.value
        curr = curr.next
##为什么要用一个current node :引入curr 是为了避免改变head值
def search_by_value(head, value):
    if not head:
        return None
    current_node = head
    while current_node is not None:
        if current_node.val == value:
            return current_node
        current_node = current_node.next
    return None

def search_by_index(head, index):
    if not head or index < 0 :
        return None
    for move_times in range(index):
        head = head.next
        if not head:
            return None
    return head

def add_to_index(head, index,value):
    #head: type node, the first node of the passed singly linked ListNode
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
    insert_place.next , new_node.next = new_node, insert_place.next
    return fake_head.next
