## Ternary Search with recursive method
## Recursive relation: T(n) = T(n/3) + 4c
## substitution method: O(log_3 N)

## Function Definition
def ternary_search(arr, left, right, key):
    while left <= right:
        mid1 = left + (right - left) // 2
        mid2 = right - (right - left) // 2

        if key == arr[mid1]:
            return mid1
        elif key == arr[mid2]:
            return mid2
        elif key < arr[mid1]:
            return ternary_search(arr, left, mid1 - 1, key)
        elif key > arr[mid2]:
            return ternary_search(arr, mid2 + 1, right, key)
        else:
            return ternary_search(arr, mid1 + 1, mid2 - 1, key)
    return -1


arr = [2, 4, 6, 8, 10]
key = 10
left, right = 0, len(arr)
## Function Calling
result = ternary_search(arr, left, right, key)
print(result)
