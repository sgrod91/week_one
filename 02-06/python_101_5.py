day = int(raw_input('Day (0-6)? '))
if day >= 1 and day < 6:
    print "Go to work"
elif day == 0 or day == 6:
    print "Sleep in"
