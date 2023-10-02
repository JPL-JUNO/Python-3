"""
@Title: Estimate Pi using vectorized numpy arrays
@Author(s): Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime: 2023-09-19 10:34:19
@Description: 
"""

import numpy as np
import time
import argparse
import sys
import os


def estimate_nbr_points_in_quarter_circle(nbr_samples: int) -> int:
    """
    Estimate Pi using vectorized numpy arrays
    """
    # 记得为每个进程设置随机数种子
    np.random.seed()
    xs = np.random.uniform(0, 1, nbr_samples)
    ys = np.random.uniform(0, 1, nbr_samples)
    estimate_inside_quarter_unit_circle = (xs * xs + ys * ys) <= 1
    nbr_trails_in_quarter_unit_circle = np.sum(
        estimate_inside_quarter_unit_circle)
    return nbr_trails_in_quarter_unit_circle


# 要被其他文件引入函数，这里加一个主文件判断
if __name__ == '__main__':
    print(os.path.basename(sys.argv[0]))
    parser = argparse.ArgumentParser(
        description="Estimate Pi using vectorized numpy arrays")
    parser.add_argument("nbr_workers", type=int,
                        help="Number of workers e.g. 1, 2, 4, 8")
    parser.add_argument("--nbr_samples_in_total", type=int, default=1e8,
                        help="Number of samples in total e.g. 1000000")
    parser.add_argument("--processes", action="store_true",
                        default=False, help="True if using Processes, absent (False) for Threads")

    args = parser.parse_args()
    if args.processes:
        print("Using Processes")
        from multiprocessing import Pool
    else:
        print("Using Threads")
        from multiprocessing.dummy import Pool
    nbr_samples_in_total = int(args.nbr_samples_in_total)
    nbr_parallel_blocks = int(args.nbr_workers)
    pool = Pool()

    nbr_samples_per_worker = int(nbr_samples_in_total / nbr_parallel_blocks)

    print("Making {} samples per worker".format(nbr_samples_per_worker))
    # confirm we have an integer number of jobs to distribute
    assert nbr_samples_per_worker == int(nbr_samples_per_worker)
    # nbr_samples_per_worker == int(nbr_samples_per_worker)

    map_inputs = [nbr_samples_per_worker] * nbr_parallel_blocks
    t1 = time.time()
    results = pool.map(estimate_nbr_points_in_quarter_circle, map_inputs)
    pool.close()

    print("Dart throws in unit circle per worker:", results)
    print("Took {:.2f}s".format(time.time() - t1))
    nbr_in_circle = sum(results)
    combined_nbr_samples = sum(map_inputs)
    pi_estimate = float(nbr_in_circle) / combined_nbr_samples * 4
    print("Estimated pi", pi_estimate)
    print("Pi", np.pi)
    print()
