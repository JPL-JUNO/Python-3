"""
@Title: Estimate Pi Using blocks of serial work on 1 CPU
@Author(s): Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime: 2023-09-19 14:20:17
@Description: 
"""

import time
import sys
import numpy as np
import os


def estimate_nbr_points_in_circle(nbr_samples: int) -> int:
    """
    Calculate the number of points inside the circle
    """
    np.random.seed()
    xs = np.random.uniform(0, 1, nbr_samples)
    ys = np.random.uniform(0, 1, nbr_samples)
    estimate_inside_quarter_unit_circle = (xs * xs + ys * ys) <= 1
    nbr_trails_in_quarter_unit_circle = np.sum(
        estimate_inside_quarter_unit_circle)
    return nbr_trails_in_quarter_unit_circle


if __name__ == "__main__":
    # 输出当前的文件名
    print(os.path.basename(sys.argv[0]))
    nbr_samples_in_total = int(1e8)
    nbr_parallel_blocks = 4
    nbr_samples_per_worker = int(nbr_samples_in_total / nbr_parallel_blocks)
    t1 = time.time()
    nbr_in_circle = 0
    for npb in range(nbr_parallel_blocks):
        nbr_in_circle += estimate_nbr_points_in_circle(nbr_samples_per_worker)
    print("Took {:.2f}s".format(time.time() - t1))
    pi_estimate = float(nbr_in_circle) / nbr_samples_in_total * 4
    print("Estimated pi:", pi_estimate)
    print("Pi:", np.pi)
    print()
