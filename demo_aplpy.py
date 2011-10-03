import aplpy

gc = aplpy.FITSFigure('2mass_H.fits')
gc.show_grayscale()


import pywcsgrid2
import pyfits

f = pyfits.open("2mass_H.fits")
plt.figure(2)
ax = pywcsgrid2.subplot(111, header=f[0].header)
ax.imshow(f[0].data, vmin=209, vmax=759, cmap="gray", origin="lower")


