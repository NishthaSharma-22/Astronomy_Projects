"""
This project simulates gravitational waves from binary black hole mergers using general relativity and wave mechanics. 
It generates a time-series graph visualizing the resulting waveform of these cosmic events.
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.constants import G, c, pi

# all constants here:
M_sun = 1.989e30  # mass of the Sun (in kg)
parsec = 3.086e16  # 1 parsec (in meter)
year = 3.154e7  # 1 year (in seconds)

# binary black hole system
M1 = 30 * M_sun  # mass of black hole 1 (in kg)
M2 = 30 * M_sun  # mass of black hole 2 (in kg)
distance = 1e9 * parsec  # distance to the binary system (in meters)


def chirp_mass(M1, M2):
    """Calculate the chirp mass of the binary system."""
    return (M1 * M2) ** (3/5) / (M1 + M2) ** (1/5)

def orbital_frequency(t, M_chirp):
    """Calculate the orbital frequency as a function of time during inspiral."""
    return (5 / (256 * (t))) ** (3/8) * (G * M_chirp / c**3) ** (-5/8)

def gravitational_wave_amplitude(M1, M2, r, f_orb):
    """Compute the amplitude of the gravitational wave."""
    return (4 * G**2 * M1 * M2) / (c**4 * r) * (pi * f_orb)**(2/3)

def gravitational_wave_frequency(f_orb):
    """Gravitational wave frequency is twice the orbital frequency."""
    return 2 * f_orb

def gravitational_wave_strain(t, M1, M2, distance):
    """Compute the strain of the gravitational wave as a function of time."""
    M_chirp = chirp_mass(M1, M2)
    f_orb = orbital_frequency(t, M_chirp)
    amplitude = gravitational_wave_amplitude(M1, M2, distance, f_orb)
    f_gw = gravitational_wave_frequency(f_orb)
    
    return amplitude * np.sin(2 * pi * f_gw * t)

time = np.linspace(1e-4, 0.1, 10000)  # this is the time in seconds before the merger

# to siimulate the gravitational wave strain:
strain = gravitational_wave_strain(time, M1, M2, distance)

plt.figure(figsize=(10, 6))
plt.plot(time, strain)
plt.title("Simulated Gravitational Wave from Binary Black Hole Merger")
plt.xlabel("Time (s)")
plt.ylabel("Strain (h)")
plt.grid(True)
plt.show()
