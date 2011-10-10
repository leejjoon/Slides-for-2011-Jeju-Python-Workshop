import scipy.spatial
import matplotlib.pyplot as plt
import numpy as np

class Picker(object):
    def __init__(self, xy):
        self.kdtree = scipy.spatial.KDTree(xy)

    def pick(self):
        pos = plt.ginput()
        return self.kdtree.query(pos[0])

import pysao

ds9 = pysao.ds9()

ds9.set("tile")
ds9.set('mode crosshair')

ds9.set("frame 1")
ds9.set("file 2mass_J.fits")
ds9.set("scale zscale")
ds9.set("frame 2")
ds9.set("file 2mass_H.fits")
ds9.set("scale zscale")
ds9.set('lock crosshair wcs')

import atpy
tbl = atpy.Table("2mass_table.xml")

x = tbl["Jmag"]
y = tbl["Jmag"] - tbl["Hmag"]

ax = plt.subplot(111, aspect=1)
ax.scatter(x, y)


picker = Picker(np.asarray([x, y]).transpose())

def panto():
    pos = picker.pick()
    print pos[1]
    row = tbl[pos[1]] 
    ra, dec = row[2], row[3]
    ds9.set('pan to %f %f wcs fk5' % (ra, dec))
    ds9.set('crosshair %f %f wcs fk5' % (ra, dec))
    ds9.set('match frames wcs')
    

print "pick an object in the matplotlib figure."
panto()

print "click on the figure to quit"
plt.ginput()
