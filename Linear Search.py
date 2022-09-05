## Search for an element, if it's present in an array, return the index of that element
## Suppose searching element is not present in an array, return -1
## Time Complexity :- O(n)
## space Complexity :- O(1)

## function definition
def linearSearch(arr, key):
    n = len(arr)
    for i in range(n):
        if key == arr[i]:
            return i

    return -1


## Driver code
arr = [20, 40, 70, 10, 12, 11, 29, 75, 46]
key = 46
result = linearSearch(arr, key)
print(result)