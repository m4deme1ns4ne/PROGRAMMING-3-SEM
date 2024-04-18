class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def print_tree_as_dict(root):
    if root is None:
        return {}
    return {
        'value': root.value,
        'left': print_tree_as_dict(root.left),
        'right': print_tree_as_dict(root.right)
    }

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

if __name__ == "__main__":
    # Пример использования
    root_value = 12
    height = 4
    binary_tree_iterative = build_binary_tree_iterative(root_value, height)
    tree_dict_iterative = print_tree_as_dict(binary_tree_iterative)
    print(f"Не рекурсивное бинарное дерево: {tree_dict_iterative}")
