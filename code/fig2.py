import numpy as np
from matplotlib import pyplot as plt
import my_pyplot as mpt
import thermostat as ts

Data = dict()
dt, step = 0.001, 10000000

Data['NH'] = ts.NH(dt, step, 0.4)
Data['NHchain'] = ts.NHchain(dt, step, 0.4, 6)
Data['stochastic'] = ts.stochastic(dt, step, 1)

fig, ax = plt.subplots(figsize=(8, 8))

for key, value in Data.items():
    x_array, p_array = value
    ax.plot(x_array, p_array)
    ax.set_xlabel("$x$")
    ax.set_ylabel("$p$")
    mpt.minor(ax)
    mpt.savejpg('../' + key)
    plt.cla()

    x_height, bin_edges = np.histogram(x_array, np.linspace(-4, 4, 200), density=True)
    bin_centers = 0.5*(bin_edges[1:] + bin_edges[:-1])
    width = bin_centers[1] - bin_centers[0]
    ax.bar(bin_centers, x_height, width = width, alpha=0.7, label = "Simulation results")
    x_theory = np.linspace(-4, 4, 1000)
    y_theory = 1 / (np.pi * 2) ** 0.5 * np.exp(-0.5 * x_theory**2)
    ax.plot(x_theory, y_theory, c='C1', label="Theoretical results")
    ax.set_xlabel("x")
    ax.set_ylabel("Density")
    mpt.legend()
    mpt.savejpg('../' + key + '-x')
    plt.cla()

    p_height, bin_edges = np.histogram(p_array, np.linspace(-4, 4, 200), density=True)
    ax.bar(bin_centers, p_height, width = width, alpha=0.7, label = "Simulation results")
    ax.plot(x_theory, y_theory, c='C1', label="Theoretical results")
    ax.set_xlabel("p")
    ax.set_ylabel("Density")
    mpt.legend()
    mpt.savejpg('../' + key + '-p')
    plt.cla()
