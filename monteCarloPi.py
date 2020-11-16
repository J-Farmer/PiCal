import matplotlib.pyplot as plt
import numpy as np
import time, random, math
import analyzeList as al

def compute(s, n):
    inside = 0

    # set the random seed on the server from that passed by the client
    random.seed(s)
    xArr = []
    yArr = []
    colors = []
    # for all the points requested
    for i in range(n):
        # compute position of the point
        x = random.uniform(-1.0, 1.0)
        y = random.uniform(-1.0, 1.0)
        z = x*x + y*y
        if (z<=1.0):
            inside = inside + 1 # this point is inside the unit circle
            colors.append('blue')
        else:
            colors.append('red')

        xArr.append(x)
        yArr.append(y)
        
    return(inside, xArr, yArr, colors)


pointRange = [10, 100, 1000, 10000]
subplots = [221, 222, 223, 224]
for i, p in zip(pointRange, subplots):
    fig = plt.figure(figsize=(8,8))
    totalPoints = i
    num = 0
    randomSeed = random.randint(0,65535)
    results = compute(randomSeed, totalPoints)
    num += results[0]
    piEst = (4.0 * num) / totalPoints

    print("Estimated Pi: {}".format(piEst))
    percentError = abs((piEst - math.pi) / (math.pi)) * 100
    print("Percent Error: {}%".format(round(percentError, 3)))

    #plt.subplot(p)
    plt.title("Number of Points: {}\nEstimated Pi: {} ({}%)".format(i, piEst, round(percentError, 3)))
    plt.scatter(results[1], results[2], color=results[3])
    plt.axis([-1,1,-1,1])
    print ()
plt.show()

piEstArr = []
percentErrArr = []
bestEst = math.inf
bestIter = 0
for i in range(10, 10010, 10):
    totalPoints = i
    num = 0
    randomSeed = random.randint(0,65535)
    results = compute(randomSeed, totalPoints)
    num += results[0]
    piEst = (4.0 * num) / totalPoints
    
    if(abs(piEst - math.pi) < abs(bestEst-math.pi)):
        bestEst = piEst
        bestIter = i
    piEstArr.append(piEst)

    #print(f"Number of Points: {i}\nEstimated Pi: {piEst}")
    percentError = abs((piEst - math.pi) / (math.pi)) * 100
    #print(f"Percent Error: {percentError}%")
    percentErrArr.append(percentError)

print("Best Estimate: {} at {}". format(bestEst, bestIter))
print("math.pi Value: {}".format(math.pi))
print("Best Percent Error: {}% at {}".format(round(abs(bestEst-math.pi)/math.pi*100,10), bestIter))
print(al.analyzeList(piEstArr))

plt.hlines(math.pi, 0, len(piEstArr)-1, zorder=10)
plt.plot(piEstArr)
plt.show()

plt.plot(percentErrArr)
plt.hlines(0, 0, 1000)
plt.show()

