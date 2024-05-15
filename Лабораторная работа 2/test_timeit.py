from gen_bin_tree_recursive import gen_bin_tree_recursive
from non_gen_bin_tree_recursive import gen_bin_tree_non_recursive

import timeit

# Тестирование рекурсивной функции
rec_time = timeit.timeit(str(gen_bin_tree_recursive(5, 10)), globals=globals(), number=1000)
print(f"Рекурсивная функция: {rec_time} секунд")

# Тестирование нерекурсивной функции
non_rec_time = timeit.timeit(str(gen_bin_tree_non_recursive(5, 10)), globals=globals(), number=1000)
print(f"Нерекурсивная функция: {non_rec_time} секунд")
