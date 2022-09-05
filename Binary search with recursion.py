# pre-requisite of binary search : arr must be sorted order
# binary search using Recursion
def binary_search(arr, i, j, key):

    # base case condition
    if j >= i:
        mid = i + (j - i) // 2
        if key == arr[mid]:
            return mid

        # if key is less than mid-value then key must be left side of the array
        elif key < arr[mid]:
            return binary_search(arr, i, mid - 1, key)

        # else right side of the array
        elif key > arr[mid]:
            return binary_search(arr, mid + 1, j, key)

    # if key not found return -1
    else:
        return -1


arr = [10, 20, 30, 40, 50]
key = 20
result = binary_search(arr, 0, len(arr) - 1, key)
print("The key present in the position : ", result)
