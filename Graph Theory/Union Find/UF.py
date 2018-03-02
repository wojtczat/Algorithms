# Weighted Quick-Union with path compression

def find(p, q):
    return root(p) == root(q)

def root(i):
    while i != ID[i - 1]:
        ID[i - 1] = ID[ID[i - 1] - 1]
        i = ID[i - 1]
    return i

def union(p, q):
    i = root(p )
    j = root(q)
    ID[i - 1] = j


n,k = raw_input().strip().split(' ')
n,k = [int(n),int(k)]
ID = [i + 1 for i in xrange(n)]

for a0 in xrange(k):
    x,y = raw_input().strip().split(' ')
    x,y = [int(x),int(y)]
    union(x, y)

print ID

'''
Sample input
The first line contains two space separated integers, n (the number of integers) and
k (the number of transformations). The following  lines each contain two space separated
integers x and y denoting a transformation from letter x to letter y

10 7
1 3
5 7
3 5
2 6
2 4
8 4
10 9

'''
