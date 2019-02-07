class ListNode(object):
    def __init__(self, val):
        self.value = val
        self.next = None


def print_node(head): #注:传入的是一个节点, 不是index或者value, 所以curr也是节点
    curr = head
    while curr:
        print(curr.value)
        curr = curr.next
            
    

def search_by_index(head, index):
    if not head or index <0:
        return None
    curr = head
    while index > 0 and curr:
        curr = curr.next
        index -= 1
    return curr

def search_by_value(head, val):
    if not head or not val:
        return None
    curr = head
    while curr:
        if curr.value == val:
            return curr
        curr = curr.next
    return None
    

def add_to_index(head, index, value):
    fake_head = ListNode(None)
    fake_head.next = head
    
    insert_position = search_by_index(fake_head, index)
    if insert_position is None:
        return 
    new_node = ListNode(value)
    new_node.next = insert_position.next
    insert_position.next = new_node
    return fake_head.next


node1 = ListNode("D")
node2 = ListNode("O")
node3 = ListNode("T")
node4 = ListNode("A")

node1.next = node2
node2.next = node3
node3.next = node4
new_head = add_to_index(node1,2,"xxx")
print_node(new_head)