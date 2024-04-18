from recursive_binary_tree import build_binary_tree as recursive_build
from iterative_binary_tree import build_binary_tree_iterative as iterative_build

import timeit


def test_recursive(root, height):
    def wrapper():
        return recursive_build(root, height)
    return wrapper

def test_iterative(root, height):
    def wrapper():
        return iterative_build(root, height)
    return wrapper

def measure_time(test_func, setup, number=1000):
    time = timeit.timeit(test_func, setup=setup, number=number)
    return time / number

if __name__ == "__main__":
    root = 12
    height = 4
    recursive_test = test_recursive(root, height)
    iterative_test = test_iterative(root, height)

    recursive_time = measure_time(recursive_test, "from recursive_binary_tree import build_binary_tree")
    iterative_time = measure_time(iterative_test, "from iterative_binary_tree import build_binary_tree_iterative")

    print("Recursive Time:", recursive_time)
    print("Iterative Time:", iterative_time)
