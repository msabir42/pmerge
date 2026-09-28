class Node:
    def __init__(self, number):
        self.number = number
        self.next = None


def compare(left: Node, right: Node) -> bool:
    if (left.number > right.number):
        return True
    else:
        return False

def get_size(source: Node) -> int:
    size = 0
    current = source
    while(current):
        size = size + 1
        current = current.next
    return size

def end_traversal(source: Node) -> Node:
    size = get_size(source)
    i = 0
    current = source
    while (i < size):
        if (current.next == None):
            return current
        current = current.next
        i = i + 1
    return current

def set_head(source: Node, head: Node) -> Node:
    head.next = source
    return head

def link(primary:Node, secondary:Node) -> Node:
    end_traversal(primary).next = secondary
    return primary

def create_nodes(numbers :list) -> list:
    nodes = []
    for num in numbers:
        nodes.append(Node(num))
    return nodes