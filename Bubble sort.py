## Bubble sort
## Time Complexity = O(n^2)

## Function Defination
def bubbleSort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

## Driver code
arr = [70, 20, 50, 30, 90, 5, 15]
## Function calling
result = bubbleSort(arr)
print(result)
