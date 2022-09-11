## Selection Sort
## Time Complexity :- O(n^2)

## Function Defination
def selectionSort(arr):
    n = len(arr)
    for i in range(n):
        ## to store the index of minimum value
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j

        ## swap the element at i with min_idx
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

    return arr

## Driver code
arr = [50, 38, 45, 79, 19, 27, 29]
result = selectionSort(arr)
print(arr)