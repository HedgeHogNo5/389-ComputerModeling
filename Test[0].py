import numpy as np
import unittest
from Classes import Pendulum

class TestPendulum(unittest.TestCase):
    def test_update(self):
        length = 1.0
        mass = 1.0
        pendulum = Pendulum(length, mass)

        # simulate the pendulum for 10 seconds
        num_steps = 1000
        deltaT = 0.01
        for i in range(num_steps):
            pendulum.update(deltaT)

        # check that the final position and velocity are reasonable
        final_position = pendulum.particles_list[0].position
        final_velocity = pendulum.particles_list[0].velocity
        self.assertAlmostEqual(np.linalg.norm(final_position - np.array([0.0, -length, 0.0])), length, delta=1e-6)
        self.assertAlmostEqual(np.linalg.norm(final_velocity), 0.0, delta=1e-6)