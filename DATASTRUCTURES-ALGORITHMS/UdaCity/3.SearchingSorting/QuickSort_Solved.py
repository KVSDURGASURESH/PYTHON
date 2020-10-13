"""Implement quick sort in Python.
Input a list.
Output a sorted list."""


def partition(array, high, low):
    pivot = array[high]
    i = low  # To keep the index of element smaller than pivot
    j = low  # To keep the index of element greater than pivot

    while j < high:
        if array[j] < pivot:
            array[j], array[i] = array[i], array[j]
            i += 1
        j += 1

    array[i], array[high] = array[high], array[i]

    return i


def quickSort(array, low, high):
    if low < high:
        pivot = partition(array, low, high)
        quickSort(array, low, pivot - 1)
        quickSort(array, pivot + 1, high)


test = [21, 4, 1, 3, 9, 20, 25, 6, 21, 14]

# test = [8, 3, 1, 7, 0, 10, 2]
# print(quicksortWithLogging(test))
n = len(test)
quickSort(test, 0, n - 1)
for i in range(n):
    print("%d" % test[i])
