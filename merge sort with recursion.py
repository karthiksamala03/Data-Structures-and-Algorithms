## Merge sort
## Time Complexity :- T(n) = 2T(n/2) + O(n)

def mergeprocedure(arr, L, R):
    i = j = k = 0

    while i < len(L) and j < len(R):
        if L[i] < R[j]:
            arr[k] = L[i]
            i += 1
        elif L[i] > R[j]:
            arr[k] = R[j]
            j += 1
        k += 1

    while i < len(L):
        arr[k] = L[i]
        i += 1
        k += 1
    while j < len(R):
        arr[k] = R[j]
        j += 1
        k += 1


def merge_sort(arr):
    # if empty array or single array comes no change required
    if len(arr) <= 1:
        return

    mid = len(arr) // 2

    # Creating Left array
    L = arr[:mid]
    # Creating Right array
    R = arr[mid:]

    # Calling recursively Left and Right arrays
    merge_sort(L)
    merge_sort(R)

    # Sorting data between Left and Right array
    mergeprocedure(arr, L, R)


test_cases = [[12, 11, 13, 5, 6, 7], [], [1], [1, 2, 3, 4, 5], [5, 4, 3, 2, 1]]

for arr in test_cases:
    print("Given arr : ", arr, end='   ,    ')
    # calling merge function
    merge_sort(arr)
    print("Sorted arr : ", arr)
