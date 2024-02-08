def mini(*val,lowlimit=None):
    if lowlimit is None:
        return min(val)
    else:
        L = [x for x in val if x >= lowlimit]
        return min(L)

print(mini (1,2,3,4,5,6,-5,-10,12, lowlimit = 0))