from math import *
'''cache efficient sieve'''
def simpleSieve(limit, prime):
    mark = [True for i in xrange(limit+1)]
    p=2
    while(p * p <= limit):
        if mark[p]:
            for i in range(p * 2, n+1, p):
                mark[i] = False
        p+=1
    for i in xrange(2, limit):
        if (mark[i]):
            prime.append(i)

def segmentedSieve(n):
    limit = (floor(sqrt(n))+1)
    prime = []
    simpleSieve(limit, prime)
    low  = limit
    high = 2*limit
    while (low < n):
        if (high >= n): high = n
        mark = [True for i in xrange(limit+1)]
        for i in xrange(len(prime)):
            loLim = (floor(low/prime[i]) * prime[i])
            if loLim < low:
                loLim += prime[i]
            j = lowLim
            while j<high:
                mark[j-low] = False
                j+= prime[i]

        for i in xrange(low, high):
            if (mark[i - low] == true): print(i + "  ")
        low  = low + limit
        high = high + limit
