"""
@File         : c_profile.py
@Author(s)    : Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime  : 2024-05-03 16:27:05
@Email        : cuixuanstephen@gmail.com
@Description  : 
"""

from simul import benchmark

import cProfile

cProfile.run("benchmark()")
