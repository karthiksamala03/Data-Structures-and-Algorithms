## function Definition
def SearchInSortedMatrix(arr, key):
    ## no of rows
    m = len(arr)
    if m == 0:
        return False
    ## no of columns
    n = len(arr[0])
    left = 0
    right = m*n-1

    ## Binary search implementation
    while left <= right:
        mid = left + (right - left) // 2
        ## extracting mid value from a 2D array
        ## row_number = idx // n
        ## column_number = idx % n
        mid_element = arr[mid // n][mid % n]
        if key == mid_element:
            return True
        if key < mid_element:
            right = mid - 1
        else:
            left = mid + 1
    return False


## Driver code
arr = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
key = 3
## function calling
result = SearchInSortedMatrix(arr, key)
print(result)