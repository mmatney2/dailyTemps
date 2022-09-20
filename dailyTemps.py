def dailyTemps(temps):
    res = [0] * len(temps)
    stack = []

    for i, t in enumerate(temps):
        while stack and t > stack[-1][0]:
            stackT, stackInd = stack.pop()
            res[stackInd] = (i - stackInd)
        stack.append([t,i])
    return res
print(dailyTemps([2,3,4,5,6]))