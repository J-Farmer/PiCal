from leibniz import leibniz
from generateRange import generateRange
import math

ranges = generateRange(0,100000,5)

piSum = 0
for r in ranges:
    piSum += leibniz(r)

print(4.0 * piSum)
piCalc = 4.0 * piSum
print(f"Percent Error: {((piCalc - math.pi) / (math.pi)) * 100}")

    
