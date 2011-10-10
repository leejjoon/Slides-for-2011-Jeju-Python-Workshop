if 1:
  import pyfits
  import pywcs
  import numpy as np
  
  f = pyfits.open("2mass_J.fits")
  wcs = pywcs.WCS(f[0].header)

  xy_pix = np.asarray([[f[0].header["CRPIX1"], f[0].header["CRPIX2"]]])
  # xy_pix.shape => (1, 2)
  xy_sky = wcs.wcs_pix2sky(xy_pix, 1)

  x_pix, y_pix = xy_pix[:,0], xy_pix[:,1] # 1-d arrays
  x_sky, y_sky = wcs.wcs_pix2sky(x_pix, y_pix, 1)

  print wcs.wcs_sky2pix(x_sky, y_sky, 1)
