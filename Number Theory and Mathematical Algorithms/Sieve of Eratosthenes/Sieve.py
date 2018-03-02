def SieveOfEratosthenes(n):
    prime = [True for i in xrange(n+1)]
    p=2
    while(p * p <= n):
        if (prime[p] == True):
            for i in range(p * 2, n+1, p):
                prime[i] = False
        p+=1