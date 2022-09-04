## Insertion Sort
## Time Complexity :- O(n^2)

## Function Definition
def insertionSort(arr):
    n = len(arr)

    for i in range(1, n):
        key = arr[i]
        j = i-1
        while ((j >= 0) and (key < arr[j])):
            arr[j+1] = arr[j]
            j = j - 1

        arr[j+1] = key

    return arr

## Driver code
arr = [75, 90, 100, 95, 85, 50, 100, 110, 7]
result = insertionSort(arr)
print(result)
