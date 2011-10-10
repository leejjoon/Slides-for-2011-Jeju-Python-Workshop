import numpy as np
import scipy.spatial
import matplotlib.pyplot as plt

xy = np.random.rand(20).reshape((10,2))

ax = plt.subplot(111, aspect=1)
for i, (x1, y1) in enumerate(xy):
    ax.annotate("%d" % i, xy=(x1, y1), va="center", ha="center",
                bbox=dict(boxstyle="round",fc="w"))


class Picker(object):
    def __init__(self, xy):
        self.kdtree = scipy.spatial.KDTree(xy)

    def pick(self):
        pos = plt.ginput()
        print self.kdtree.query(pos[0])

picker = Picker(xy)


print "pick an object by clicking on the figure"
picker.pick()
