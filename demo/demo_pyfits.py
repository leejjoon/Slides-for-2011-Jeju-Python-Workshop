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

import matplotlib.pyplot as plt

plt.imshow(d)
plt.show()

