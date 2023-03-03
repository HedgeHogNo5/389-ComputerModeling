import numpy as np
from Classes import Particle, NewtonsCradle, Pendulum

def test_pendulum():
    # Create a pendulum with length 2 and mass 1
    pendulum = Pendulum(length=2, mass=1)

    # Check that the pendulum has the correct attributes
    assert pendulum.length == 2
    assert pendulum.mass == 1
    assert pendulum.BALL_RADIUS == 2.5
    assert pendulum.NUM_BALLS == 1
    assert isinstance(pendulum.particles_list[0], Particle)
    assert pendulum.particles_list[0].name == 'Ball'
    assert np.allclose(pendulum.particles_list[0].position, [0.0, -2.0, 0.0])
    assert np.allclose(pendulum.particles_list[0].velocity, [0.0, 0.0, 0.0])
    assert np.allclose(pendulum.particles_list[0].acceleration, [0.0, 0.0, 0.0])
    assert pendulum.CHAIN_LENGTH == 10
    assert pendulum.SPACING == 2 * pendulum.BALL_RADIUS
    assert np.allclose(pendulum.g, [0, -9.81, 0])

    # Update the pendulum for 1 second
    pendulum.update(1)

    # Check that the pendulum position and velocity have been updated
    assert np.allclose(pendulum.particles_list[0].position, [0.0, -1.98733019, 0.0], rtol=1e-6)
    assert np.allclose(pendulum.particles_list[0].velocity, [0.19613352, 0.0, 0.0], rtol=1e-6)
