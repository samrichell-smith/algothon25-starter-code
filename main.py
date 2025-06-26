import numpy as np

nInst = 50
maxDollarPosition = 10000

def getMyPosition(prcSoFar):
    nInst, nDays = prcSoFar.shape
    positions = np.zeros(nInst, dtype=int)
    breakout_window = 20

    #no change for first 20 days as this is the data we are getting signals from
    if nDays < breakout_window + 1:
        return positions


    for i in range(nInst):
        recent_prices = prcSoFar[i, -breakout_window-1:-1]
        price_today = prcSoFar[i, -1]

        high = np.max(recent_prices)
        low = np.min(recent_prices)


        #if current price is higher or lower than max or min in last 20 days, buy/put maximum amount
        if price_today > high:
            num_shares = int(maxDollarPosition / price_today)
            positions[i] = num_shares
        elif price_today < low:
            num_shares = int(maxDollarPosition / price_today)
            positions[i] = -num_shares
        else:
            positions[i] = 0

    return positions
