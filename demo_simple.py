import matplotlib.pyplot as plt

###

plt.plot([0, 2], [0, 2], "-")
plt.tight_layout()

plt.xlabel("X-label"); plt.ylabel("Y-label")
plt.tight_layout()

plt.gca().set_aspect(1)

plt.savefig("a.png", bbox_inches="tight")

###

plt.plot([0.2], [0.2], "o")
ann = plt.annotate("Test",
                   xy=(0.2, 0.2), xycoords='data',
                   xytext=(50, 50), textcoords='offset points',
                   arrowprops=dict(arrowstyle="->", shrinkB=10,
                                   connectionstyle="angle3"),
                   size=30
                   )

ann.draggable()

####

plt.imshow([[1,2],[2,3]], interpolation="bilinear")
txt = plt.annotate("test", (1., 1.), (0., 0),
                   arrowprops=dict(arrowstyle="->",
                                   connectionstyle="angle3", lw=2),
                   size=20, ha="center")

from matplotlib.patheffects import withStroke
txt.set_path_effects([withStroke(linewidth=3, foreground="w")])
txt.arrow_patch.set_path_effects([withStroke(linewidth=5, foreground="w")])

####

from mpl_toolkits.axes_grid1.inset_locator import inset_axes

fig = plt.figure(1)
ax = fig.add_subplot(111)
ax.set_aspect(1.)

axins = inset_axes(ax,
                   width="30%", # width = 30% of parent_bbox
                   height=1., # height : 1 inch
                   loc=3)

axins.axis[:].toggle(ticklabels=False)

