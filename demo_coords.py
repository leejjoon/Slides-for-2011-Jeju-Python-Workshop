from coords import Position

p = Position("9:15:54.8 -49:58:24.6", equinox='J2000', system='celestial')
print p.dd()
print p.galactic()

