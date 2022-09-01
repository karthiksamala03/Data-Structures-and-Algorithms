def ternary_search(arr, key):
    left, right = 0, len(arr)

    while(left <= right):
        mid1 = left + (right - left)//2
        mid2 = right - (left - right)//2

        if key == arr[mid1]:
            return mid1
        elif key == arr[mid2]:
            return mid2
        elif key < arr[mid1]:
            right = mid1 - 1
        elif key > arr[mid2]:
            left = mid2 + 1
        else:
            left = mid1 + 1
            right = mid2 - 1
    return -1

arr = [2, 4, 6, 8, 10]
key = 6
result = ternary_search(arr, key)
print(result)