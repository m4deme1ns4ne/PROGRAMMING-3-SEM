from exceptions import InvalidHeightError, InvalidRootError
from logger_config import gen_bin_tree_logger

def gen_bin_tree_recursive(height=5, root=10):
    gen_bin_tree_logger.debug(f"Called gen_bin_tree_recursive with height={height}, root={root}")
    if height < 0:
        gen_bin_tree_logger.error(f"Invalid height: {height}")
        raise InvalidHeightError(height)
    if root < 1:
        gen_bin_tree_logger.error(f"Invalid root: {root}")
        raise InvalidRootError(root)
    if height == 0:
        return None
    left_child = root * 3 + 1
    right_child = root * 3 - 1
    tree = {
        'value': root,
        'left': gen_bin_tree_recursive(height - 1, left_child),
        'right': gen_bin_tree_recursive(height - 1, right_child)
    }
    gen_bin_tree_logger.debug(f"Generated subtree: {tree}")
    return tree
