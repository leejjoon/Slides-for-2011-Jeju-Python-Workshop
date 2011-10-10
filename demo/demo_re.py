
test_str = 'circle(19:43:24.2, +04:42:23, 13")'

import re
p_radec = r'[+-]?\d+:\d+:\d+(?:\.\d*)?'
p = re.compile(r"(%s),\s*(%s)" % (p_radec, p_radec))

m = p.search(test_str)
print m.groups()

