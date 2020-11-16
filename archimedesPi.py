import math
import matplotlib.pyplot as plt
import analyzeList as al

previousError = 0
def pi_archimedes(num):
    """
    Calculate n iterations of Archimedes PI recurrence relation
    """
    polygon_edge_length_squared = 2.0
    polygon_sides = 4
    for i in range(num):
        polygon_edge_length_squared = 2 - 2 * math.sqrt(1 - polygon_edge_length_squared / 4)
        polygon_sides *= 2
    return polygon_sides * math.sqrt(polygon_edge_length_squared) / 2, polygon_sides

errorList = []
piList = []
for n in range(16):
    result, sides = pi_archimedes(n)
    piList.append(result)
    error = abs((result - math.pi) / math.pi*100)
    
    errorList.append(error)
    print("{} iterations: {:.10f} Error: {:.10f} Sides: {}".format(n+1, result, error, sides))
    if(abs(error - previousError) < 0.000001):
        break
    previousError = error

#plt.plot(errorList)
plt.hlines(math.pi, 0, len(piList)-1, zorder=10)
plt.plot(piList)
plt.show()

plt.plot(errorList)
plt.show()
print(al.analyzeList(piList))
print(al.analyzeList(errorList))
