def gen_bin_tree_non_recursive(height=5, root=10):
    '''
    Не рекурсивное бинарное дерево
    '''
    if height < 1:
        return None

    tree = {}
    stack = [(root, height, tree)]
    
    while stack:
        node, h, subtree = stack.pop()
        if h > 0:
            subtree['value'] = node
            subtree['left'] = {}
            subtree['right'] = {}
            stack.append((node * 3 - 1, h - 1, subtree['right']))
            stack.append((node * 3 + 1, h - 1, subtree['left']))
        else:
            subtree = None
    
    return tree
