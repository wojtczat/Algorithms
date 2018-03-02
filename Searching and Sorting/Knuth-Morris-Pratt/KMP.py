def KMPSearch(pat, txt):
    M = len(pat)
    N = len(txt)
    lps = [0]*M
    j = 0 # index for pat[]
    computeLPSArray(pat, M, lps)
    i = 0 # index for txt[]
    while i < N:
        if pat[j] == txt[i]:
            i += 1
            j += 1
        if j == M:
            print "Found pattern at index " + str(i-j)
            j = lps[j-1]
        elif i < N and pat[j] != txt[i]:
            # Do not match lps[0..lps[j-1]] characters, they will match anyway
            if j != 0: j = lps[j-1]
            else: i += 1

def computeLPSArray(pat, M, lps):
    l = 0 # length of the previous longest prefix suffix
    lps[0] # lps[0] is always 0
    i = 1
    while i < M:
        if pat[i]==pat[l]:
            l += 1
            lps[i] = l
            i += 1
        else:
            if l != 0:
                l = lps[l-1]
            else:
                lps[i] = 0
                i += 1
