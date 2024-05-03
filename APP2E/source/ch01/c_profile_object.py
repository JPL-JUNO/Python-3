"""
@File         : c_profile_object.py
@Author(s)    : Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime  : 2024-05-03 16:31:15
@Email        : cuixuanstephen@gmail.com
@Description  : 
"""

from simul import benchmark
import cProfile

pr = cProfile.Profile()
pr.enable()
benchmark()
pr.disable()
pr.print_stats()
