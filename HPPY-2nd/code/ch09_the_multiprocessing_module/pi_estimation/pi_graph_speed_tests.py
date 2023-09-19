"""
@Title: 不同核数运行时间比较（线程与进程）
@Author(s): Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime: 2023-09-18 22:46:10
@Description: 
"""

import numpy as np
import matplotlib.pyplot as plt

speeds = [[374.11],
          [374.11, 77.28, 79.74, 62.89],
          [62.05, 37.22, 25.91, 21.57]]
nbr_cores = [[1],
             [1, 2, 4, 8],
             [1, 2, 4, 8]]
labels = np.array(["Serial", "Threads", "Processes"])
plt.figure()
plt.clf()
markers = ['--o', '--x', '-x']
for nc, sp, label, mk in zip(nbr_cores, speeds, labels, markers):
    plt.plot(nc, sp, mk, label=label, linewidth=2)

plt.annotate("Serial and Threads have similar execution time",
             xy=(nbr_cores[0][0] + .2, speeds[0][0] + 10))
plt.xlim(.5, 8.5)
plt.ylim(0, 400)
plt.ylabel("Execution time (seconds) - smaller is better")
plt.xlabel("Number of workers")
plt.title("Time to estimate Pi using objects with 100,000,000\ndart throws in series, threaded and with processes")
plt.legend(framealpha=.8)
# plt.show()
plt.tight_layout()
plt.savefig("09_pi_lists_graph_speed_tests_threaded_processes.png")
