import pyregion
import pyfits
import matplotlib.pyplot as plt

f = pyfits.open("2mass_H.fits")

ax = plt.subplot(121)
ax.imshow(f[0].data, origin="lower", vmin=253, vmax=274, cmap="gray")

# test.reg
# fk5
# ellipse(283.97689,1.4135677,18.000562",40.999754",27.305575)
reg = pyregion.open("test.reg")
print reg[0].coord_list

reg2 = reg.as_imagecoord(f[0].header)
print reg2[0].coord_list

patches, texts = reg2.get_mpl_patches_texts()
ax.add_patch(patches[0])

msk = reg2.get_mask(shape=f[0].data.shape)
ax2 = plt.subplot(122)
ax2.imshow(msk, origin="lower", cmap="gray")

plt.show()
