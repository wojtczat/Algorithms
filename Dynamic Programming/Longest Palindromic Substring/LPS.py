def longestPalindromicSubstringManacher(ip):
    """Manacher's algorithm O(n)"""
    s = '$*' + '*'.join(ip) + '*#'
    P = [0] * len(s)
    Mirror,C,R,maxLPS,maxLPSIndex = 0,0,0,0,0
    for i in range(1,len(s)-1):
        Mirror = 2*C - i
        if i < R:
            P[i] =  min(R-i,P[Mirror])
        while s[i + (P[i] + 1)] == s[i - (P[i] + 1)]:
            P[i] += 1
        if i + P[i] > R:
            C = i
            R = i + P[i]
        # Keep track of the index at which the longest palindromic substring occurs
        if P[i] > maxLPS:
            maxLPS = P[i]
            maxLPSIndex = i
    print s[maxLPSIndex - P[maxLPSIndex]: maxLPSIndex + 1 + P[maxLPSIndex]].replace('*','')