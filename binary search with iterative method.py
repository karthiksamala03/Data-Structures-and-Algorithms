def binary_search(arr, i, j, key):
    for n in range(0,len(arr)):
        if j >= i:
            mid = i + (j - i) // 2
            if key == arr[mid]:
                return mid
            elif key < arr[mid]:
                j = mid-1
            elif key > arr[mid]:
                i = mid+1
        else:
            return -1

arr = [10, 20, 30, 40, 50]
key = 400
result = binary_search(arr, 0, len(arr) - 1, key)
print("The Key present in the position : ", result)
