from typing import List


def bubble_sort(list1: List[int]) -> List[int]:
    n = len(list1)
    swapped = None

    for i in range(n-1):
        for j in range(n-i-1):
            if list1[j] > list1[j+1]:
                list1[j], list1[j+1] = list1[j+1], list1[j]
                swapped = True
    if not swapped:
        return list1
    return list1


print(bubble_sort([10, 7, 500]))