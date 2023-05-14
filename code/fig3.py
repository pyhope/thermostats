import numpy as np
from matplotlib import pyplot as plt
import my_pyplot as mpt
import thermostat as ts
import time

Data = dict()
dt, step = 0.001, 10000000

start_time = time.time()
Data['Nose-Hoover thermostat'] = ts.NH(dt, step, 0.4)
end_time = time.time()
print('Nose-Hoover thermostat: %.2f s' % (end_time - start_time))

start_time = time.time()
Data['Nose-Hoover chain'] = ts.NHchain(dt, step, 0.4, 6)
end_time = time.time()
print('Nose-Hoover chain: %.2f s' % (end_time - start_time))

start_time = time.time()
Data['Stochastic thermostat'] = ts.stochastic(dt, step, 1)
end_time = time.time()
print('Stochastic thermostat: %.2f s' % (end_time - start_time))

fig = plt.figure(figsize=(12, 12))
gs = fig.add_gridspec(2, 2, wspace=0, hspace=0.07)
axes = gs.subplots(sharex=True, sharey=False)
ax_x, ax_p = axes[0, 0], axes[0, 1]
ax_xe, ax_pe  = axes[1, 0], axes[1, 1]
ax_pe.get_shared_y_axes().join(ax_xe, ax_pe)
ax_p.set_yticklabels([])
ax_pe.set_yticklabels([])

x_theory = np.linspace(-4, 4, 1000)
y_theory = 1 / (np.pi * 2) ** 0.5 * np.exp(-0.5 * x_theory**2)
bins = np.linspace(-4, 4, 200)
y_2 = 1 / (np.pi * 2) ** 0.5 * np.exp(-0.5 * np.linspace(-4, 4, 199)**2)

for key, value in Data.items():
    x_array, p_array = value
    x_height, bin_edges = np.histogram(x_array, bins, density=True)
    p_height, bin_edges = np.histogram(p_array, bins, density=True)
    bin_centers = 0.5*(bin_edges[1:] + bin_edges[:-1])
    ax_x.plot(bin_centers, x_height, label = key)
    ax_p.plot(bin_centers, p_height, label = key)
    if key == 'Nose-Hoover chain':
        ax_xe.plot(bin_centers, np.abs(x_height - y_2), c='C1')
        ax_pe.plot(bin_centers, np.abs(p_height - y_2), c='C1')
    elif key == 'Stochastic thermostat':
        ax_xe.plot(bin_centers, np.abs(x_height - y_2), c='C2')
        ax_pe.plot(bin_centers, np.abs(p_height - y_2), c='C2')

for ax in [ax_x, ax_p]:
    ax.plot(x_theory, y_theory, c= 'k', ls = '--', alpha = 0.5, label="Theoretical results")
    ax.set_ylim(0, 0.6)
    mpt.minor(ax)

ax_x.set_ylabel("Density")
ax_xe.set_ylabel("Density error")

ax_x.set_xlabel("x")
ax_p.set_xlabel("p")
ax_xe.set_xlabel("x")
ax_pe.set_xlabel("p")

ax_p.legend(fancybox=False, edgecolor='black', fontsize = 14, loc='upper right')

mpt.savejpg('../compare')

# Nose-Hoover thermostat: 2.59 s
# Nose-Hoover chain: 35.48 s
# Stochastic thermostat: 19.93 s