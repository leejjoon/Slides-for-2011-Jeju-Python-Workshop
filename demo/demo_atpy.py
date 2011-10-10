import atpy
tbl = atpy.Table("test.als", type="daophot")
print tbl.keys()

import matplotlib.pyplot as plt
plt.plot(tbl["XCENTER"], tbl["YCENTER"], ".")

plt.show()
