"""
@Title: 使用 joblib 进行并行
@Author(s): Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime: 2023-09-19 09:43:06
@Description: 
"""
import time
from joblib import Parallel, delayed
from pi_lists_parallel import estimate_nbr_points_in_quarter_circle

if __name__ == "__main__":
    nbr_samples_in_total = int(1e8)
    nbr_parallel_blocks = 8

    nbr_samples_per_worker = int(nbr_samples_in_total / nbr_parallel_blocks)

    print("Making {:,} samples per {} worker".format(
        nbr_samples_per_worker, nbr_parallel_blocks))
    t1 = time.time()
    # Parallel is a class; we can set parameters such as n_jobs to dictate how many processes
    # will run, along with optional arguments like verbose for debugging information.
    # Other arguments can set time-outs, change between threads or processes,
    # change the backends (which can help speed up certain edge cases), and configure memory mapping.

    # Parallel has a __call__ callable method that takes an iterable.
    nbr_in_quarter_unit_circles = Parallel(
        n_jobs=nbr_parallel_blocks, verbose=1)(delayed(estimate_nbr_points_in_quarter_circle)(nbr_samples_per_worker) for sample_idx in range(nbr_parallel_blocks))
    pi_estimate = sum(nbr_in_quarter_unit_circles) * \
        4 / float(nbr_samples_in_total)
    print("Estimated pi:", pi_estimate)
    print("Delta:", time.time() - t1)


# Making 12,500,000 samples per 8 worker
# [Parallel(n_jobs=8)]: Using backend LokyBackend with 8 concurrent workers.
# Executing estimate_nbr_points_in_quarter_circlewith 12,500,000 on pid 10720
# Executing estimate_nbr_points_in_quarter_circlewith 12,500,000 on pid 9972
# Executing estimate_nbr_points_in_quarter_circlewith 12,500,000 on pid 15472
# Executing estimate_nbr_points_in_quarter_circlewith 12,500,000 on pid 7960
# Executing estimate_nbr_points_in_quarter_circlewith 12,500,000 on pid 14872
# Executing estimate_nbr_points_in_quarter_circlewith 12,500,000 on pid 15744
# Executing estimate_nbr_points_in_quarter_circlewith 12,500,000 on pid 9916
# Executing estimate_nbr_points_in_quarter_circlewith 12,500,000 on pid 13596
# [Parallel(n_jobs=8)]: Done   2 out of   8 | elapsed:   18.9s remaining:   56.9s
# [Parallel(n_jobs=8)]: Done   8 out of   8 | elapsed:   19.1s finished
# Estimated pi: 3.1415548
# Delta: 19.22745704650879
