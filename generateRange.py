def generateRange(start, stop, numberOfRanges):
    #generate Range sizes
    ranges = []
    rangeSize = []
    length = (stop - start) // numberOfRanges
    for i in range(numberOfRanges):
        rangeSize.append(length)
        
    #handle any surplus values
    surplus = (stop - start) % numberOfRanges
    i = 0
    while(surplus > 0):
        surplus -= 1
        rangeSize[i] += 1
        i = (i+1)%numberOfRanges
        
    #generate lo,hi of range
    lo = start
    hi = 0
    for s in rangeSize:
        hi = (lo + s) - 1
        ranges.append([lo, hi])
        lo = hi + 1

    return ranges

    
