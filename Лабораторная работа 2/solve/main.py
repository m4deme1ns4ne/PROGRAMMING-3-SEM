from complex_profiling import plot_results, test_recursive, test_iterative


def main():
    recursive_time = test_recursive
    iterative_time = test_iterative

    plot_results(recursive_time, iterative_time)


if __name__ == "__main__":
    main()
