import sys
xr = 5

for x in xrange (0,xr):
    spaces = xr - x - 1
    stars = x * 2 + 1
    for y in xrange (0, spaces):
        sys.stdout.write(" ")
    for z in xrange(0, stars):
        sys.stdout.write("*")
    print ""

#easier way

yr = 5

for y in range(o,xr):
    spaces = yr - x - 1
    stars = y * 2 + 1
    print ' ' * spaces + '*' * stars
