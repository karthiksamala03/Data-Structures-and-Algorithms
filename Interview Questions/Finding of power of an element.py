## Finding of Power of an element : constraint n>=1
## This is Application of Divide and Conquer
## Time Complexity :- O(log n)

def findingOfPowerOfElement(a, n):
    # small problem
    if n == 1:
        return a
    # Big problem --> Divide and Conquer Approach
    else:
        mid = n // 2
        # recursive call
        b = findingOfPowerOfElement(a, mid)
        r = b * b
    if n % 2 == 0:
        return r
    else:
        return r * a


## Driver code
a = 2
n = 10
result = findingOfPowerOfElement(a, n)
print("The Power of an element is ", result)
