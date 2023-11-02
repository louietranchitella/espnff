#!/usr/bin/env python3

import matplotlib
import matplotlib.pyplot as plt
import numpy
import pandas

from itertools import count

excel = pandas.read_excel("scorigami.xlsx")
a = excel.to_numpy()
seq2 = count(2)
d = {-1:-1, 0:0, 1:1, 2:2}
for o in a.flatten():
    if o not in d: d[o] = next(seq2)

b = numpy.array([d[x] for x in a.flatten()]).reshape(a.shape)

N = len(d)
cmap = matplotlib.colors.ListedColormap(["black","white", "green", "red"])
bounds = [-1.5, -0.5, 0.5, 1.5, 2.5]
norm = matplotlib.colors.BoundaryNorm(bounds, cmap.N)
fig, ax = plt.subplots()
ax.set_xlabel("Winning Team Score")
ax.xaxis.set_label_position("top")
ax.set_ylabel("Losing Team Score")
ax.yaxis.set_label_position("right")
ax.xaxis.tick_top()
ax.yaxis.tick_right()
img = ax.imshow(a, interpolation='nearest', cmap=cmap, norm=norm)
fig.colorbar(img, cmap=cmap, norm=norm, boundaries=bounds, ticks=[0,1,2], pad = 0.2)
plt.savefig("scorigami.png", dpi=1200)
