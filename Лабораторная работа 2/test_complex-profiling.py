from gen_bin_tree_recursive import gen_bin_tree_recursive
from non_gen_bin_tree_recursive import gen_bin_tree_non_recursive
from test_cases import test_cases

import matplotlib.pyplot as plt
import time

def test_function(func, test_cases):
    times = []
    for height, root in test_cases:
        start_time = time.perf_counter()
        func(height, root)
        end_time = time.perf_counter()
        times.append(end_time - start_time)
    return times


recursive_times = test_function(gen_bin_tree_recursive, test_cases)


non_recursive_times = test_function(gen_bin_tree_non_recursive, test_cases)


plt.plot(recursive_times, label='Рекурсивная функция')
plt.plot(non_recursive_times, label='Нерекурсивная функция')
plt.xlabel('Тесты')
plt.ylabel('Время (секунды)')
plt.title('Сравнение эффективности рекурсивной и нерекурсивной реализации')
plt.legend()
plt.show()
