import numpy as np
from matplotlib import pyplot as plt
import my_pyplot as mpt
from thermostat import NH

dt, step = 0.0001, 1000000
fig = plt.figure(figsize=(12, 16))
gs = fig.add_gridspec(4, 3, wspace=0.12, hspace=0.2)
axes = gs.subplots(sharex=False, sharey=False)
Q = [0.05 * (i + 1) for i in range(12)]
Q_2D = np.array(Q).reshape(4, 3)

for i, _ in enumerate(Q_2D):
    for j, value in enumerate(_):
        ax = axes[i, j]
        x_array, p_array = NH(dt, step, value)
        ax.plot(x_array, p_array)
        ax.set_title("Q = " + str(np.round(value, 2)), fontsize=14)
        print(value)
        mpt.minor(ax)

for ax in axes[-1, :]:
    ax.set_xlabel("$x$")
for ax in axes[:, 0]:
    ax.set_ylabel("$p$")

mpt.savejpg("../fig1")
