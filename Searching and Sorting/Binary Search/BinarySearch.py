# Iterative Binary Search Function
# Return the location of x in given array if present, otherwise return -1
def binarySearch(arr, l, r, x):
    while l <= r:
        mid = l + (r - l)/2;
        # Check if x is present at mid
        if arr[mid] == x:
            return mid
        # If x is greater, ignore left half
        elif arr[mid] < x:
            l = mid + 1
        # If x is smaller, ignore right half
        else:
            r = mid - 1
    # If the element was not present
    return -1
