"""
@Title: 用 Monte Carlo 来模拟 pi
@Author(s): Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime: 2023-09-18 20:01:53
@Description: 
"""

import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['savefig.dpi'] = 300

np.random.seed(0)
nbr_items = int(1e4)
xs = np.random.uniform(0, 1, nbr_items)
ys = np.random.uniform(0, 1, nbr_items)

# 是否落在单位圆内
estimate_inside_quarter_unit_circle = (xs**2 + ys**2) <= 1

nb_trails_in_quarter_unit_circle = np.sum(estimate_inside_quarter_unit_circle)
pi = (nb_trails_in_quarter_unit_circle * 4) / nbr_items

plt.figure(1, figsize=(8, 8))
plt.clf()
plt.plot(xs[estimate_inside_quarter_unit_circle],
         ys[estimate_inside_quarter_unit_circle], 'bx')
plt.plot(xs[~estimate_inside_quarter_unit_circle],
         ys[~estimate_inside_quarter_unit_circle],
         'g.')

unit_circle_xs = np.arange(0, 1, .001)
unit_circle_ys = np.sin(np.arccos(unit_circle_xs))
plt.plot(unit_circle_xs, unit_circle_ys, linewidth=2, c='k')
plt.axis([0, 1, 0, 1])
plt.yticks([0.0, 1.0])
plt.xticks([0.0, 1.0])
plt.title("Pi estimated as {} using \n{:,} Monte Carlo dart throws".format(
    pi, int(nbr_items))
)
plt.tight_layout()
# plt.show()
plt.savefig("09_pi_plot_monte_carlo_example.png")
