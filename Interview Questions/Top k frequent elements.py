from collections import Counter
import heapq


## Function Definition
def topKFrequentElements(arr, k):
    if k == len(arr):
        return set(arr)

    # Count is a dictionary which contain unique values as a key and frequency
    ## of those unique elements as values
    count = Counter(arr)
    return heapq.nlargest(k, count.keys(), key=count.get)


## Driver code
arr = [1, 1, 1, 1, 2, 2, 2, 3, 3]
k = 2
result = topKFrequentElements(arr, k)
print(f"Top {k} Frequent elements in {arr} are ", result)
