"""
@File         : test_simul.py
@Author(s)    : Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime  : 2024-05-03 14:57:35
@Email        : cuixuanstephen@gmail.com
@Description  : 
"""

from simul import Particle, ParticleSimulator


def test_evolve():
    particles = [
        Particle(0.3, 0.5, +1),
        Particle(0.0, -0.5, -1),
        Particle(-0.1, -0.4, +3),
    ]
    simulator = ParticleSimulator(particles)
    simulator.evolve(0.1)

    p0, p1, p2 = particles

    def fequal(a, b, eps=1e-5):
        return abs(a - b) < eps

    assert fequal(p0.x, 0.21195175403084765)
    assert fequal(p0.y, 0.4526842112890649)

    assert fequal(p1.x, -0.09936474001850394)
    assert fequal(p1.y, -0.5097767911808465)

    assert fequal(p2.x, 0.1922406058402573)
    assert fequal(p2.y, -0.43237525164531665)
