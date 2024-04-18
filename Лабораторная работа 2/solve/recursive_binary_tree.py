class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def build_binary_tree(root_value, height):
    if height == 0:
        return None
    root = Node(root_value)
    root.left = build_binary_tree(root_value ** 3, height - 1)
    root.right = build_binary_tree((root_value * 2) - 1, height - 1)
    return root
