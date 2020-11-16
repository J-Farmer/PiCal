from leibniz import leibniz
import math
import matplotlib.pyplot as plt

piEst = []
percentError = []
for i in range(10, 100000, 100):
    piCalc = 4*leibniz(i)
    piEst.append(piCalc)
    percentError.append(((piCalc - math.pi) / (math.pi)) * 100)

print(piEst[-1], percentError[-1])

plt.plot(piEst)
plt.show()
plt.plot(percentError)
plt.show()
