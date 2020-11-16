import math
import matplotlib.pyplot as plt
previousError = 0
def pi_archimedes(n):
    """
    Calculate n iterations of Archimedes PI recurrence relation
    """
    polygon_edge_length_squared = 2.0
    polygon_sides = 4
    for i in range(n):
        polygon_edge_length_squared = 2 - 2 * math.sqrt(1 - polygon_edge_length_squared / 4)
        polygon_sides *= 2
    return polygon_sides * math.sqrt(polygon_edge_length_squared) / 2, polygon_sides

errorList = []
piList = []
for n in range(16):
    result, sides = pi_archimedes(n)
    piList.append(result)
    error = result - math.pi
    errorList.append(error)
    print("{} iterations: {.10f} Error: {.10f} Sides: {}".format(n, result, error, sides))
    previousError = error

plt.plot(errorList)
plt.plot(piList)
plt.show()
