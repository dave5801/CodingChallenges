def sumPairs(anArray, n):
    pairs = {}
    for i in anArray:
        if i in pairs:
            return True
        else:
            pairs[n-i] = 1
    return False