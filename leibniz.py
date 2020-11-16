def leibniz(r):
    result = 0.0
    sign = 1.0
    if(type(r) == list):
        #print("Using a list")
        for n in range(r[0], r[1] + 1):
            result += sign/(2.0 * n + 1)
            sign = -sign
        return result
    else:
        #print("Using range")
        for n in range(r+1):
            result += sign / (2.0 * n + 1)
            sign = -sign
        return result

if __name__ == "__main__":
    import matplotlib.pyplot as plt
    import math
    import analyzeList as al
    
    piEstArr = []
    percentErrorArr = []
    previousError = math.inf
    
    for i in range(0, 1000):
        piEst = 4*leibniz(i)
        percentError = abs((piEst - math.pi) / (math.pi)) * 100
        piEstArr.append(piEst)
        percentErrorArr.append(percentError)
#        if(abs(percentError - previousError) < 0.0001):
#            break
        previousError = percentError

    print("Iterations: {}".format(len(piEstArr)))
    print("Best Pi Estimation: {}".format(piEstArr[-1]))
    print("math.pi Value: {}".format(math.pi))
    print("Lowest Percent Error: {}%".format(round(al.analyzeList(percentErrorArr)[1],3)))
    
    print(al.analyzeList(piEstArr))
    
    fig = plt.figure(figsize=(8,8))
    plt.hlines(math.pi, 0, len(piEstArr)-1, zorder=10)
    #plt.scatter(range(0,iterations), piEstArr)
    plt.plot(piEstArr)
    plt.show()
    
    plt.hlines(0, 0, len(piEstArr)-1, zorder=10)
    plt.plot(percentErrorArr)
    plt.show()
    

