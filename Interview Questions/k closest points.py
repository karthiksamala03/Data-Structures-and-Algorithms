from heapq import heappush, heappop
from math import sqrt


def get_distance(x, y):
    return sqrt((x ** 2 + y ** 2))


def kClosestPoints(points, k):
    n = len(points)
    minheap = []
    for i in range(n):
        x = points[i][0]
        y = points[i][1]
        heappush(minheap, (get_distance(x, y), points[i]))

    result = []
    for i in range(k):
        result.append(heappop(minheap)[1])

    return result


## Driver code
points = [[3, 3], [5, -1], [-2, 4]]
k = 2
result = kClosestPoints(points, k)
print("k closest points are ", result)
