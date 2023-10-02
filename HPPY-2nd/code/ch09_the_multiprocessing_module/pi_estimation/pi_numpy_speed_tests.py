"""
@Title: Graph execution time for serial, threaded and processes forms of Pi estimation with numpy
@Author(s): Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime: 2023-09-19 21:19:52
@Description: 
"""

import numpy as np
import matplotlib.pyplot as plt

speeds = [[3.58],
          [3.28, 2.41, 1.81, 1.74],
          [2.99, 1.83, 1.41, 1.24]]
nbr_cores = [[1],
             [1, 2, 4, 8],
             [1, 2, 4, 8]]
labels = np.array(["Serial", "Threads", "Processes"])
plt.figure(1)
plt.clf()

markers = ['-.x', '--x', '-x']
for nc, sp, label, mk in zip(nbr_cores, speeds, labels, markers):
    plt.plot(nc, sp, mk, label=label, linewidth=2)
plt.axis([0.5, 8.5, 0, 4])
plt.legend(framealpha=.8)
plt.ylabel("Execution time (seconds) - smaller is better")
plt.xlabel("Number of workers")
plt.title("Time to estimate Pi using numpy with 100,000,000\ndart throws in series, threaded and with processes")
# plt.show()
plt.tight_layout()
plt.savefig("09_pi_numpy_graph_speed_tests_threaded_processes.png")
