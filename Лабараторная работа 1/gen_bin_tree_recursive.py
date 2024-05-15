def gen_bin_tree_recursive(height=5, root=10):
    if height < 1:
        return None
    left_child = root * 3 + 1
    right_child = root * 3 - 1
    return {
        'value': root,
        'left': gen_bin_tree_recursive(height - 1, left_child),
        'right': gen_bin_tree_recursive(height - 1, right_child)
    }

tree_recursive = gen_bin_tree_recursive()
print(tree_recursive)
