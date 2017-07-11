# LIS returns length of the longest increasing subsequence in an arr of size n
def lis(arr):
    n = len(arr)
    lis = [1] * n  # Declare the list (array) for LIS and initialize LIS values for all indices
    # Compute optimized LIS values in bottom up manner
    for i in range (1 , n):
        for j in range(0 , i):
            if arr[i] > arr[j] and lis[i]< lis[j] + 1 :
                lis[i] = lis[j]+1
                
    # Pick maximum of all LIS values
    maximum = 0
    for i in range(n):
        maximum = max(maximum , lis[i])
    return maximum
