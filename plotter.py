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
img = plt.imshow(a, interpolation='nearest', cmap=cmap, norm=norm)
plt.colorbar(img, cmap=cmap, norm=norm, boundaries=bounds, ticks=[0,1,2])
plt.savefig("scorigami.png")
