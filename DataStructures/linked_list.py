import copy

class Node:
    def __init__(self, val: int, next=None):
        self.val = val
        self.next = next

def traverse_list(head: Node):
    while head:
        print(head.val, end=" ")
        head = head.next
    print()

def insert_node_recur(pos: int, head: Node, val: int) -> Node:
    if not head or pos == 0:
        return Node(val, head)
    head.next = insert_node_recur(pos - 1, head.next, val)
    return head

def insert_node(pos: int, head: Node, val: int) -> Node:
    if pos == 0 or not head:
        return Node(val, head)

    prev = head
    curr = head
    while curr is not None and pos != 0:
        prev = curr
        curr = curr.next
        pos -= 1

    tmp = prev.next
    prev.next = Node(val, tmp)
    return head

def search(head: Node, target: int) -> int:
    cnt = 0
    while head:
        if head.val == target:
            return cnt
        cnt += 1
        head = head.next
    return -1

def delete_node_recur(head: Node, index: int) -> Node:
    if not head:
        return None
    if index == 0:
        return head.next
    head.next = delete_node_recur(head.next, index - 1)
    return head

def delete_node(head: Node, index: int) -> Node:
    if not head:
        return None
    if index == 0:
        return head.next
    prev = curr = head
    while curr and index != 0:
        prev = curr
        curr = curr.next
        index -= 1

    if index == 0:
        prev.next = curr.next if curr else None
    return head


if __name__ == "__main__":
    list_0 = None
    list_1 = Node(5, None)
    list_2 = Node(5, Node(7, Node(10, None)))

    traverse_list(list_0)
    traverse_list(list_1)
    traverse_list(list_2)
    list_3 = insert_node(1, copy.deepcopy(list_2), 32)
    traverse_list(list_3)
    list_4 = insert_node(0, copy.deepcopy(list_2), 50)
    traverse_list(list_4)

    list_5 = insert_node(2, copy.deepcopy(list_0), 100)
    traverse_list(list_5)

    list_6 = insert_node_recur(1, copy.deepcopy(list_2), 32)
    traverse_list(list_6)

    list_7 = insert_node_recur(0, copy.deepcopy(list_2), 50)
    traverse_list(list_7)

    traverse_list(delete_node(copy.deepcopy(list_6), 1))
    traverse_list(delete_node(copy.deepcopy(list_6), 3))

    traverse_list(delete_node_recur(copy.deepcopy(list_6), 1))
    traverse_list(delete_node_recur(copy.deepcopy(list_6), 3))
