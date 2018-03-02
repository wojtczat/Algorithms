def binarySearch(arr, l, r, x):
    while l <= r:
        mid = l + (r - l)/2;
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            l = mid + 1
        else:
            r = mid - 1
    return -1

def lengthOfLIS(nums):
    dp = [0 for i in xrange(len(nums))]
    lenLis = 0;
    for num in nums:
        i = Arrays.binarySearch(dp, 0, lenLis, num)
        if (i < 0): i = -(i + 1)
        dp[i] = num
        if (i == lenLis): lenLis+=1
    return lenLis