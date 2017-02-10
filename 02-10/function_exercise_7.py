import matplotlib.pyplot as plot
import math

def f(x):
    return (x * 1.8) + 32

xs = range(-100, 101)
ys = []
for x in xs:
    ys.append(f(x))

plot.plot(xs, ys)
plot.show()
