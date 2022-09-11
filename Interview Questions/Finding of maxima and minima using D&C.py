# Finding of Maxima and Minima using Divide and Conquer method
# Time Complexity :- O(n)
## function Definition
def findingOfMaximaMinima(arr, start, end):

    ## single element present in an array
    if end == start:
        min = arr[start]
        max = arr[end]
        return min, max
    ## Two elements present in an array
    elif start == end - 1:
        if arr[start] < arr[end]:
            min = arr[start]
            max = arr[end]
        else:
            min = arr[end]
            max = arr[start]
        return min, max
    ## More than Two elements present in an array
    ## Big problem - Divide and Conquer Approach
    else:
        # Divide
        mid = start + (end - start)//2
        minL, maxL = findingOfMaximaMinima(arr, start, mid)
        minR, maxR = findingOfMaximaMinima(arr, mid+1, end)

        # To find the final minima value
        if minL < minR:
            min = minL
        else:
            min = minR
        # To find the final maxima value
        if maxL > maxR:
            max = maxL
        else:
            max = maxR

    return min, max

## Driver code
arr = [70, 50, 45, 10, 12, 15, 75, 29, 37, 57]
start = 0
end = len(arr) - 1

## function calling
min_result, max_result = findingOfMaximaMinima(arr, start, end)
print("The Maximum and Minimum values of an array ", max_result, min_result)



# def findingOfMaximaMinima(arr):
#     min = 0
#     max = float('inf')
#
#     for i in range(len(arr)):
#         if arr[i] > min:
#             min = arr[i]
#         if arr[i] < max:
#             max = arr[i]
#
#     return min, max