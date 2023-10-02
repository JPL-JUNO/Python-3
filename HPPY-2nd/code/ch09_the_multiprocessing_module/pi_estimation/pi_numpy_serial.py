"""
@Title: Estimate Pi using 1 large array
@Author(s): Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime: 2023-09-19 14:14:25
@Description: 
"""

import time
from pi_numpy_parallel_worker import estimate_nbr_points_in_quarter_circle
import numpy as np
import sys
import os

nbr_samples_in_total = int(1e8)

t1 = time.time()
nbr_in_circle = estimate_nbr_points_in_quarter_circle(nbr_samples_in_total)

print(os.path.basename(sys.argv[0]))
print("Took {:.2f}s".format(time.time() - t1))
pi_estimate = float(nbr_in_circle) / nbr_samples_in_total * 4
print("Estimated pi:", pi_estimate)
print("Pi:", np.pi)
