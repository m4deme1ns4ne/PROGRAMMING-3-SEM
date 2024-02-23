#Рекурсивный вариант бинарного дерева
class TreeNode:
    def __init__(self, root):
        self.root = root
        self.left_leaf = None
        self.right_leaf = None

    #Вариант прямого обхода
    def pre_order(self, node):
        if node:
            print(node.value)
            TreeNode.pre_order(node.left)
            TreeNode.pre_order(node.right)


def main():
    local_root = int(input("Input root: "))
    tree = TreeNode(local_root)
    height = int(input("Input height: "))
    for _ in range(height):
        TreeNode.left_leaf = local_root * 2
        TreeNode.right_leaf = local_root + 2
    TreeNode.pre_order(tree)


if __name__ == "__main__":
    main()
