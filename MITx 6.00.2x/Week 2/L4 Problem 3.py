def stdDevOfLengths(L):
    """
    L: a list of strings

    returns: float, the standard deviation of the lengths of the strings,
      or NaN if L is empty.
    """
    import math
    N = float(len(L))
    NumL = []
    if N == 0:
        return float('NaN')
    else:
        for l in L:
            NumL.append(len(l))
    Mean = sum(NumL)/N
    sumsigma2 = 0.0
    for num in NumL:
        sumsigma2 += (num - Mean)*(num - Mean)
    return math.sqrt(sumsigma2/N)

L = ['a', 'z', 'p']
print stdDevOfLengths(L)
L = ['apples', 'oranges', 'kiwis', 'pineapples']
print stdDevOfLengths(L)