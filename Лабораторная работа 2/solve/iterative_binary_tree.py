class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def build_binary_tree_iterative(root_value, height):
    if height == 0:
        return None
    root = Node(root_value)
    stack = [(root, height)]
    while stack:
        node, h = stack.pop()
        if h > 1:
            node.left = Node(node.value ** 3)
            node.right = Node((node.value * 2) - 1)
            stack.append((node.right, h - 1))
            stack.append((node.left, h - 1))
    return root
