import random

def setup_data(num_tests, max_height):
    test_cases = []
    for _ in range(num_tests):
        height = random.randint(1, max_height)
        root = random.randint(1, 20)
        test_cases.append((height, root))
    return test_cases

test_cases = setup_data(100, 10)
