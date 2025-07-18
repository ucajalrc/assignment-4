import random
import time
import copy
from randomizedQuicksort import randomized_quicksort
from deterministicQuicksort import deterministic_quicksort

import sys
sys.setrecursionlimit(1500)  # CAREFUL: Don't set too high!

def benchmark(sort_func, data):
    """
    Tries to run the sort function. If RecursionError occurs, return None.
    """
    arr = copy.deepcopy(data)
    try:
        start = time.perf_counter()
        sort_func(arr)
        end = time.perf_counter()
        return end - start
    except RecursionError:
        return None

if __name__ == "__main__":
    sizes = [100, 500, 1000]  # Use small sizes to avoid RecursionError!
    distributions = {
        "Random": lambda n: [random.randint(0, n) for _ in range(n)],
        "Sorted": lambda n: list(range(n)),
        "Reverse": lambda n: list(range(n, 0, -1)),
        "Repeated": lambda n: [random.choice([1, 2, 3]) for _ in range(n)]
    }

    for n in sizes:
        print(f"\nArray size: {n}")
        for dist_name, gen in distributions.items():
            data = gen(n)
            t_rand = benchmark(randomized_quicksort, data)
            t_det = benchmark(deterministic_quicksort, data)
            t_rand_str = f"{t_rand:.5f}s" if t_rand is not None else "RecursionError"
            t_det_str = f"{t_det:.5f}s" if t_det is not None else "RecursionError"
            print(f"{dist_name:8} | Randomized: {t_rand_str} | Deterministic: {t_det_str}")
