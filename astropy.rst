Brief overview of Astronomy-related python modules
==================================================

----

http://goo.gl/rwWhB
===================

----

Incomplete & Biased
===================

----

Don't reinvent the Wheels
=========================

----

Get familiar with Python Standard library
=========================================

- Built-in Types

 - list
 - tuple
 - set
 - dict

- String Services

 - string — Common string operations
 - re — Regular expression operations

- Python Runtime Services

 - sys — System-specific parameters and functions


----


- Numeric and Mathematical Modules

 - itertools — Functions creating iterators for efficient looping
 - functools — Higher order functions and operations on callable objects
 - operator — Standard operators as functions


- File and Directory Access

 - os.path — Common pathname manipulations
 - tempfile — Generate temporary files and directories
 - glob — Unix style pathname pattern expansion
 - shutil — High-level file operations

----

- Data Persistence

 - pickle — Python object serialization
 - sqlite3 — DB-API 2.0 interface for SQLite databases


- Interprocess Communication and Networking

 - subprocess — Subprocess management

----

demo_re.py
----------

.. code-block:: python

    test_str = 'circle(19:43:24.2, +04:42:23, 13")'
     
    import re
    p_radec = r'[+-]?\d+:\d+:\d+(?:\.\d*)?'
    p = re.compile(r"(%s),\s*(%s)" % (p_radec, p_radec))
     
    m = p.search(test_str)
    print m.groups()


----

Editor
======

----

Version Control System
======================

- svn

- Distributed VCS

 - mercurial (Bitbucket)
 - git (github)

----

Working in isolated Python environments
=======================================

- virtualenv : http://www.virtualenv.org
- virtualenvwrapper : http://www.doughellmann.com/projects/virtualenvwrapper/

----

Scipy
=====

Collection of python modules for mathematics, science, and engineering
----------------------------------------------------------------------

- Clustering package (scipy.cluster)
- Constants (scipy.constants)
- Discrete Fourier transforms (scipy.fftpack)
- **Integration and ODEs (scipy.integrate)**
- **Interpolation (scipy.interpolate)**
- Input and output (scipy.io)
- Linear algebra (scipy.linalg)
- Maximum entropy models (scipy.maxentropy)
- Miscellaneous routines (scipy.misc)
- **Multi-dimensional image processing (scipy.ndimage)**
- Orthogonal distance regression (scipy.odr)

----

- **Optimization and root finding (scipy.optimize)**
- Signal processing (scipy.signal)
- Sparse matrices (scipy.sparse)
- **Spatial algorithms and data structures (scipy.spatial)**
- Special functions (scipy.special)
- Statistical functions (scipy.stats)
- C/C++ integration (scipy.weave)


----

demo_kdtree.py
--------------

.. code-block:: python

    import numpy as np
    import scipy.spatial
    import matplotlib.pyplot as plt

    class Picker(object):
        def __init__(self, xy):
            self.kdtree = scipy.spatial.KDTree(xy)
     
        def pick(self):
            print "pick an object"
            pos = plt.ginput()
            return self.kdtree.query(pos[0])
     
    picker = Picker(xy)

----

Scikits
=======

http://scikits.appspot.com/scikits


- simple fitting w/ nmpfit : http://stsdas.stsci.edu/pyraf/stscidocs/pytools_pkg/pytools_api/pytools.nmpfit-module.html



----

Coordinate Conversion
=====================

- Coords: http://stsdas.stsci.edu/astrolib/coords_api/index.html

demo_coords.py
--------------

.. code-block:: python

    from coords import Position
     
    p = Position("9:15:54.8 -49:58:24.6", equinox='J2000', system='celestial')
    print p.dd()
    print p.galactic()

- Python Kapteyn Package: http://www.astro.rug.nl/software/kapteyn/
- pytpm : http://phn.github.com/pytpm/

----

Ascii Table
===========

CSV
---

.. code-block:: python

  import csv

  for row in csv.reader(open("test.csv")):
    print row[0], ":".join(row[1:4]), ":".join(row[4:])

demo_csv.py
-----------

.. code-block:: python

  import csv
  from coords import Position
  for row in csv.reader(open("test.csv")):
    p = Position("%s %s" % (":".join(row[1:4]), ":".join(row[4:])))
    print row[0], p.galactic()

----

ATpy
----

- http://atpy.github.com/

- provides an unified interface for different types of tables

  - FITS tables
  - VO tables
  - HDF5 tables
  - IPAC tables
  - ASCII tables
  - SQL databases

demo_atpy.py
------------

.. code-block:: python

  import atpy
  tbl = atpy.Table("test.als", type="daophot")
  print tbl.keys()

  plt.plot(tbl["XCENTER"], tbl["YCENTER"], ".")

----

- asciitable: http://cxc.harvard.edu/contrib/asciitable/
- idlsave: http://astrofrog.github.com/idlsave/ (also, check scipy.io)
- pyfits: fits table

---

FITS
====

- pyfits: http://www.stsci.edu/resources/software_hardware/pyfits


demo_pyfits.py
--------------

.. code-block:: python

  import pyfits

  f = pyfits.open("2mass_J.fits") 

  f.info()

  # hdu's are accesed using sequence-like interface
  hdu = f[0]

  h = hdu.header # dict-like
  d = hdu.data # numpy array

  print h["CDELT1"], h["CDELT2"]
  h.update("OBSERVER", "Jae-Joon Lee") # for non-existing keys
  
  print d.shape


- pfits: wraps CFITSIO http://pypi.python.org/pypi/pfits

----

World Coordinate System
=======================

- pywcs: https://trac.assembla.com/astrolib and http://stsdas.stsci.edu/astrolib/pywcs/

- wrapper around the wcslib library

demo_wcs.py
-----------

.. code-block:: python

  import pyfits
  import pywcs

  f = pyfits.open("2mass_J.fits")
  wcs = pywcs.WCS(f[0].header)

  xy_pix = np.asarray([[f[0].header["CRPIX1"], f[0].header["CRPIX2"]]])
  # xy_pix.shape => (1, 2)
  xy_sky = wcs.wcs_pix2sky(xy_pix, 1)

  x_pix, y_pix = xy_pix[:,0], xy_pix[:,1] # 1-d arrays
  x_sky, y_sky = wcs.wcs_pix2sky(x_pix, y_pix, 1)

  print wcs.wcs_sky2pix(x_sky, y_sky, 1)

- kapteyn

----

Interface w/ ds9
================

- pyds9: http://hea-www.harvard.edu/saord/ds9/pyds9/

- pysao: http://code.google.com/p/python-sao/

- wrapper around the xpalib library

  - pyds9 : ctypes
  - pysao : pyrex (cython)

.. code-block:: python

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

----

- demo_ds9.py

.. code-block:: python
     
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

----

Region
======

- pyregion: http://leejjoon.github.com/pyregion/

  - Parser for ds9 region files
  - draw regions using Matplotlib
  - spatial filtering

----

demo_pyregion.py
----------------

.. code-block:: python

    import pyregion
    import pyfits
     
    f = pyfits.open("2mass_H.fits")
     
    ax = plt.subplot(121)
    ax.imshow(f[0].data, origin="lower", vmin=253, vmax=274, cmap="gray")
     
    # test.reg
    # fk5
    # ellipse(283.97689,1.4135677,18.000562",40.999754",27.305575)
    reg = pyregion.open("test.reg") # ShapeList
    print reg[0].coord_list
     
    reg2 = reg.as_imagecoord(f[0].header)
    print reg2[0].coord_list
     
    patches, texts = reg2.get_mpl_patches_texts()
    ax.add_patch(patches[0])
     
    ax2 = plt.subplot(122)
    msk = reg2.get_mask(shape=f[0].data.shape)
    ax2.imshow(msk, origin="lower", cmap="gray")

----

Fits Figures
============

- aplpy

  - a toolkit built upon matplotlib
  - easy to use.

- kapteyn

- pywcsgrid2

  - extend the functionality of matplotlib
  - haevily based on mpl_toolkits.axisartist module


----


APLpy vs. pywcsgrid2
--------------------

.. code-block:: python

    import aplpy
     
    gc = aplpy.FITSFigure('2mass_H.fits')
    gc.show_grayscale()
     
     
    import pywcsgrid2
    import pyfits
     
    f = pyfits.open("2mass_H.fits")
    plt.figure(2)
    ax = pywcsgrid2.subplot(111, header=f[0].header)
    ax.imshow(f[0].data, vmin=209, vmax=759, cmap="gray", origin="lower")

----

- pywcsgrid2 : tight integration w/ axes_grid1

.. image:: http://leejjoon.github.com/pywcsgrid2/images/image.jpg
   :height: 500

----

ETC
===

- pyraf
- casa
- ciao (sherpa, etc)

----

Resources
=========

- http://www.scipy.org/Topical_Software
- http://www.astropython.org/resources

work in progress to organize astronomy-related python modules, similar to the IDL Astronomy

- http://astropy.wikispaces.com/ & http://astropy.org/
