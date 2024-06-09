"""
@File         : simul_dis.py
@Author(s)    : Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime  : 2024-06-10 00:34:19
@Email        : cuixuanstephen@gmail.com
@Description  : 
"""

import dis
from simul import ParticleSimulator

dis.dis(ParticleSimulator.evolve)
