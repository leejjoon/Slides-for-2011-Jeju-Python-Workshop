import matplotlib.pyplot as plt

if 1: 

    plt.figure(1)
    ax = plt.subplot(121)
    # draw lines
    l1, = ax.plot([0.1, 0.5, 0.9], [0.5, 0.2, 0.7], "ro-",
                  mec="r", mfc="w", lw=5, mew=3, ms=10, label="Line 1")

    shadow, = ax.plot([0.1, 0.5, 0.9], [0.5, 0.2, 0.7], "ro-",
                      mec="r", mfc="w", lw=5, mew=3, ms=10, label="Line 1")

    ax.set_xlim(0, 1); ax.set_ylim(0, 1)
    
    # offset transform
    import matplotlib.transforms as mtransforms
    ot = mtransforms.offset_copy(l1.get_transform(), ax.figure,
                                 x=4.0, y=-6.0, units='points')

    shadow.set_transform(ot)


    from agg_filter import DropShadowFilter
    gauss = DropShadowFilter(4)

    # adjust zorder of the shadow lines so that it is drawn below the
    # original lines
    shadow.set_zorder(l1.get_zorder()-0.5)
    shadow.set_agg_filter(gauss)

    # shadow.set_rasterized(True) # to support mixed-mode renderers




    ax = plt.subplot(122, aspect=1)
    fracs = [15,30,45, 10]
    explode=(0, 0.05, 0, 0)
    pies = ax.pie(fracs, explode=explode)
    ax.set_frame_on(True)
    
    from agg_filter import LightFilter, FilteredArtistList
    light_filter = LightFilter(9)

    for p in pies[0]:
        p.set_agg_filter(light_filter)
        p.set(ec="none", lw=2)
        p.set_rasterized(True) # to support mixed-mode renderers
        

    gauss = DropShadowFilter(9, offsets=(3,4), alpha=0.7)
    shadow = FilteredArtistList(pies[0], gauss)
    ax.add_artist(shadow)
    shadow.set_zorder(pies[0][0].get_zorder()-0.1)


    plt.show()
    
