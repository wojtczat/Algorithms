from math import *

def simpleSieve(limit, prime):
    mark = [True for i in xrange(limit+1)]
    p = 2
    while p*p <= limit:
        if mark[p]:
            i = p*2
            while i <= limit:
                mark[i]=False
                i+=p
        p+=1
    for i in xrange(2, limit):
        if mark[i]:
            prime.append(i)
            
def segmentedSieve(n):
    last = 0
    limit = int((floor(sqrt(n))+1))
    prime = []
    simpleSieve(limit, prime)
    low  = limit
    high = 2*limit
    while low < n:
        if high >= n: 
            high = n
        mark = [True for i in xrange(limit+1)]
        for i in xrange(len(prime)):
            lowLim = int(floor(low/prime[i]) * prime[i])
            if lowLim < low:
                lowLim += prime[i]
            j = lowLim
            while j < high:
                mark[j-low] = False
                j += prime[i]
        for i in xrange(low, high):
            if mark[i - low]: last = i
        low  = low + limit
        high = high + limit
    return last