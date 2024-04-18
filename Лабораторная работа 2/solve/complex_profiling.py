from test_binary_tree import test_recursive, test_iterative

import matplotlib.pyplot as plt

def plot_results(recursive_time, iterative_time):
    labels = ['Recursive', 'Iterative']
    times = [recursive_time, iterative_time]
    plt.bar(labels, times, color=['blue', 'orange'])
    plt.ylabel('Time (seconds)')
    plt.title('Comparison of Recursive vs Iterative Binary Tree Construction')
    plt.show()

if __name__ == "__main__":
    recursive_time = test_recursive
    iterative_time = test_iterative

    plot_results(recursive_time, iterative_time)
