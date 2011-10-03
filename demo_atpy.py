import atpy
tbl = atpy.Table("test.als", type="daophot")
print tbl.keys()

plt.plot(tbl["XCENTER"], tbl["YCENTER"], ".")

