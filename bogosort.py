"""Idk, I just thought this algorithm was funny"""

import random

# checks if the list is sorted
def isSorted(l):
    for i in range(1, len(l)):
        if l[i - 1] > l[i]:
            return False
    return True


# sorts the list using bogosort
def sort(l):
    count = 0
    while not isSorted(l):
        random.shuffle(l)
        count += 1
    return count


# example list to sort
l = [1, 3, 2, 1, 5, 10, -4, 3]
print(l)
# sort with bogosort
print(sort(l))
print(l)
