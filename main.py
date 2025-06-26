import numpy as np

nInst = 50
maxDollarPosition = 10000
currentPos = np.zeros(nInst, dtype=int)  # tracks position over time


def getMyPosition(prcSoFar):
    global currentPos

    nInst, nDays = prcSoFar.shape
    newPos = np.copy(currentPos)
    
    short_window = 5
    long_window = 20
    buffer = 0.015
    posScale = 1

    # not enough data to calculate momentum
    if nDays < long_window:
        return newPos  
    
    for i in range(nInst):
        prices = prcSoFar[i, :]
        price_today = prices[-1]

        if price_today < 1e-6:
            continue  

        short_avg = np.mean(prices[-short_window:])
        long_avg = np.mean(prices[-long_window:])
        num_shares = int(maxDollarPosition * posScale / price_today)

        # Signal decision
        if short_avg > long_avg * (1 + buffer):
            targetPos = num_shares
        elif short_avg < long_avg * (1 - buffer):
            targetPos = -num_shares

        # hold previous position
        else:
            targetPos = currentPos[i]  

        newPos[i] = targetPos

    currentPos = newPos
    return newPos
