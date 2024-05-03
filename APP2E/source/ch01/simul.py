"""
@File         : simul.py
@Author(s)    : Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime  : 2024-05-03 13:20:00
@Email        : cuixuanstephen@gmail.com
@Description  : 
"""

from typing import List


class Particle:
    def __init__(self, x, y, ang_vel) -> None:
        self.x = x
        self.y = y
        self.ang_vel = ang_vel


class ParticleSimulator:
    def __init__(self, particles: List[Particle]) -> None:
        self.particles = particles

    def evolve(self, dt):
        timestep = 1e-5
        n_steps = int(dt / timestep)
        for i in range(n_steps):
            for p in self.particles:
                # 1. calculate the direction
                norm = (p.x**2 + p.y**2) ** 0.5
                v_x = -p.y / norm
                v_y = -p.x / norm

                # 2. calculate the displacement
                d_x = timestep * p.ang_vel * v_x
                d_y = timestep * p.ang_vel * v_y

                # 3. repeat for all the time steps
                p.x += d_x
                p.y += d_y


from matplotlib import pyplot as plt
from matplotlib import animation


def visualize(simulator: ParticleSimulator):
    X = [p.x for p in simulator.particles]
    Y = [p.y for p in simulator.particles]
    fig = plt.figure()

    ax = plt.subplot(111, aspect="equal")
    (line,) = ax.plot(X, Y)
    # Axis limit
    plt.xlim(-1, 1)
    plt.ylim(-1, 1)

    def init():
        line.set_data([], [])
        return (line,)

    def animate(i):
        simulator.evolve(0.01)
        X = [p.x for p in simulator.particles]
        Y = [p.y for p in simulator.particles]

        line.set_data(X, Y)
        return (line,)

    anim = animation.FuncAnimation(fig, animate, init_func=init, blit=True, interval=10)
    plt.show()


def test_visualize():
    particles = [
        Particle(0.3, 0.5, 1),
        Particle(0.0, -0.5, -1),
        Particle(-0.1, -0.4, 3),
    ]
    simulator = ParticleSimulator(particles=particles)
    visualize(simulator)


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

    assert fequal(p0.x, 0.2102698450356825)
    assert fequal(p0.y, 0.5438635787296997)

    assert fequal(p1.x, -0.0993347660567358)
    assert fequal(p1.y, -0.4900342888538049)

    assert fequal(p2.x, 0.1913585038252641)
    assert fequal(p2.y, -0.3652272210744360)


from random import uniform


def benchmark():
    particles = [
        Particle(uniform(-1.0, 1.0), uniform(-1.0, 1.0), uniform(-1.0, 1.0))
        for i in range(100)
    ]

    simulator = ParticleSimulator(particles)
    simulator.evolve(0.1)


if __name__ == "__main__":
    benchmark()
