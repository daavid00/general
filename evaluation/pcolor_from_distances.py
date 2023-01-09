import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors

norm=plt.Normalize(-2,2)

groups = ["Austin", "CSIRO", "Delft-DARSim", "Delft-DARTS", "LANL", "Melbourne", "Stanford", "Stuttgart"]
colors = ["C0", "C1", "C2", "C3", "C6", "C7", "C8", "C9"]

numGroups = len(groups)
numExps = 5

distances = np.loadtxt("distances.csv", delimiter=",")

cmap = matplotlib.colors.LinearSegmentedColormap.from_list("", ["white","red"])

fig, axs = plt.subplots(1, 2, figsize=(12, 3))

# The calculated distances have the unit of normalized mass times meter.
# Multiply by 8.5, the injected mass of CO2 in g, and 100, to convert to g.cm.
A = 850*distances[:numGroups, :numGroups]
meanA = np.mean(A, axis=0) 
A = A + np.diag(meanA)

axs[0].pcolor(A, cmap=cmap)
axs[0].set_yticks([0.5, 1.5, 2.5, 3.5, 4.5, 5.5, 6.5, 7.5])
axs[0].set_yticklabels(groups)
axs[0].set_xticks([0.5, 1.5, 2.5, 3.5, 4.5, 5.5, 6.5, 7.5])
axs[0].set_xticklabels(groups, rotation=90)
for (i,j), value in np.ndenumerate(A):
    axs[0].text(i+0.5, j+0.5, f'{int(value):03d}', ha='center', va='center')
axs[0].set_title("24 hours")

A = 850*distances[4*numGroups:, 4*numGroups:]
meanA = np.mean(A, axis=0) 
A = A + np.diag(meanA)

axs[1].pcolor(A, cmap=cmap)
axs[1].set_yticks([0.5, 1.5, 2.5, 3.5, 4.5, 5.5, 6.5, 7.5])
axs[1].set_yticklabels(groups)
axs[1].set_xticks([0.5, 1.5, 2.5, 3.5, 4.5, 5.5, 6.5, 7.5])
axs[1].set_xticklabels(groups, rotation=90)
axs[1].tick_params(axis='y', which='both', left=False, right=True, labelleft=False, labelright=True)
for (i,j), value in np.ndenumerate(A):
    axs[1].text(i+0.5, j+0.5, f'{int(value):03d}', ha='center', va='center')
axs[1].set_title("120 hours")

fig.savefig(f"pcolor_distances.png", bbox_inches='tight')
