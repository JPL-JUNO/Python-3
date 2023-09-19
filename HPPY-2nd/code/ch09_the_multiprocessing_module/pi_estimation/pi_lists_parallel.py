"""
@Title: 在 Python 中使用一个循环来估算 pi
@Author(s): Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime: 2023-09-18 20:15:15
@Description: 
"""

import os
import random
import time

# 在 Python 中使用一个循环来估算 pi


def estimate_nbr_points_in_quarter_circle(nbr_estimates):
    """"""
    print(
        f"Executing estimate_nbr_points_in_quarter_circle "
        f"with {nbr_estimates:,} on pid {os.getpid()}")
    nbr_trails_in_quarter_unit_circle = 0.0
    for _ in range(int(nbr_estimates)):
        x = random.uniform(0, 1)
        y = random.uniform(0, 1)
        is_in_unit_circle = x**2 + y**2 <= 1.0
        nbr_trails_in_quarter_unit_circle += is_in_unit_circle
    return nbr_trails_in_quarter_unit_circle


if __name__ == "__main__":
    # 这些都是命令行参数的解析
    import argparse
    parser = argparse.ArgumentParser(description="Project description")
    parser.add_argument("nbr_workers",
                        type=int,
                        help="Number of workers e.g. 1, 2, 4, 8")
    parser.add_argument("--nbr_samples_in_total", type=int,
                        default=1e8,
                        help="Number of samples in total e.g. 100_000_000")
    parser.add_argument("--processes", action="store_true",
                        default=False, help="True if using Processes, absent (False) for Threads")
    # python 01_pi_lists_parallel.py --nbr_samples_in_total 100000000 --processes 1
    args = parser.parse_args()

    if args.processes:
        print("Using Processes")
        from multiprocessing import Pool
    else:
        print("Using threads")
        from multiprocessing.dummy import Pool

    nbr_samples_in_total = args.nbr_samples_in_total
    nbr_parallel_blocks = args.nbr_workers
    # from multiprocessing import Pool
    # nbr_samples_in_total = 1e4
    # nbr_parallel_blocks = 4

    pool = Pool(processes=nbr_parallel_blocks)
    nbr_samples_per_worker = nbr_samples_in_total / nbr_parallel_blocks
    # 逗号分隔
    print("Making {:,} samples per {} worker".format(
        nbr_samples_in_total, nbr_parallel_blocks
    ))
    nbr_trails_per_process = [nbr_samples_per_worker] * nbr_parallel_blocks
    t1 = time.time()
    # 这个执行的太慢了，没有任何的提速，反而运行速度更加慢
    # 在命令行中运行速度快，但是在交互式窗口中运行不出来，逆天
    nbr_in_quarter_unit_circles = pool.map(estimate_nbr_points_in_quarter_circle,
                                           nbr_trails_per_process)
    pi_estimate = sum(nbr_in_quarter_unit_circles) * \
        4 / float(nbr_samples_in_total)
    print("Estimate pi", pi_estimate)
    print("Delta:", time.time() - t1)
