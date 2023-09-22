"""
@Title: Estimate Pi Using 1 large array
@Author(s): Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime: 2023-09-19 09:29:55
@Description: 
"""

import time
import numpy as np
from pi_lists_parallel import estimate_nbr_points_in_quarter_circle

nbr_samples_in_total = int(1e8)

t1 = time.time()
nbr_in_circle = estimate_nbr_points_in_quarter_circle(nbr_samples_in_total)
print("Took {:.2f}s".format(time.time() - t1))
pi_estimate = nbr_in_circle / nbr_samples_in_total * 4
print("Estimated pi:", pi_estimate)
print("Pi:", np.pi)
