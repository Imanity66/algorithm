class DoubleListNode:
    def__init__(self,value):
    self.prev = None
    self.next = None
    self.value = None


    #Traverse
    list_node = list_node_1
    while list_node is not None:
        list_node = list_node.next

def search_by_value(head, value):
    if not head or value is None:
        return None
    current_node = head
    while current_node is not None:
        if current_node.val == value:
            return current_node
        current_node = current_node.next
    return None

def search_by_index(hear, index):
    if not head or index < 0 :
        return None
    for move_times in range(index):
        head = head.next
        if not head:
            return None
    return head
#如果直接给 remove_node  可以 O(1)时间remove  但是single list 不行
def remove_from_index(head,index)：
    fake_head = DoubleListNode("Fake Node")
    fake.head.next = head
    head.prev = fake_head
    remove_node = search_by_inedx(head,index)
    if remove_node is None:
        return fake_head.next
        if remove_node.prev is not None:
            remove_node.prev.next = remove_node.next
        if remove_node.next is not None:
            remove_node.next.prev = remove_node.prev
