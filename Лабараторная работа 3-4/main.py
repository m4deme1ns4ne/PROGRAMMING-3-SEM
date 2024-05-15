from recursive_tree import gen_bin_tree_recursive
from non_recursive_tree import gen_bin_tree_non_recursive
from logger_config import main_logger

def main():
    test_cases = [
        (5, 10),
        (3, 2),
        (4, 1),
        (0, 1),  # Edge case: zero height
        (-1, 10),  # Invalid case: negative height
        (3, 0),  # Invalid case: non-positive root
    ]

    for height, root in test_cases:
        try:
            main_logger.info(f"Testing gen_bin_tree_recursive with height={height}, root={root}")
            tree_recursive = gen_bin_tree_recursive(height, root)
            main_logger.info(f"Result of gen_bin_tree_recursive: {tree_recursive}")
        except Exception as e:
            main_logger.exception(f"Exception occurred: {e}")

        try:
            main_logger.info(f"Testing gen_bin_tree_non_recursive with height={height}, root={root}")
            tree_non_recursive = gen_bin_tree_non_recursive(height, root)
            main_logger.info(f"Result of gen_bin_tree_non_recursive: {tree_non_recursive}")
        except Exception as e:
            main_logger.exception(f"Exception occurred: {e}")

if __name__ == "__main__":
    main()
