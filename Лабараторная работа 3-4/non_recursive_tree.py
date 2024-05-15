from exceptions import InvalidHeightError, InvalidRootError
from logger_config import gen_bin_tree_logger

def gen_bin_tree_non_recursive(height=5, root=10):
    gen_bin_tree_logger.debug(f"Called gen_bin_tree_non_recursive with height={height}, root={root}")
    if height < 0:
        gen_bin_tree_logger.error(f"Invalid height: {height}")
        raise InvalidHeightError(height)
    if root < 1:
        gen_bin_tree_logger.error(f"Invalid root: {root}")
        raise InvalidRootError(root)
    if height == 0:
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
    gen_bin_tree_logger.debug(f"Generated tree: {tree}")
    return tree
