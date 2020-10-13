"""Implement quick sort in Python.
Input a list.
Output a sorted list."""


def quicksort(array):
    pivot = array[len(array) - 1]
    pivot_pos = len(array) - 1
    i = 0
    while i < len(array):
        if pivot < array[i]:
            array[pivot_pos] = array[i]
            array[i] = array[pivot_pos - 1]
            array[pivot_pos - 1] = pivot
            pivot_pos = pivot_pos - 1
        elif array[i] >= pivot:
            pivot_pos = len(array) - 1
            pivot = array[pivot_pos]
            i += 1

        else:
            i += 1

    return array


def quicksortWithLogging(array):
    pivot = array[len(array) - 1]
    pivot_pos = len(array) - 1
    i = 0
    while i < len(array):
        print("i : {} , is ? pivot : {} ?lt ({})th element : {}".format(i, pivot, i, array[i]))
        if pivot < array[i]:
            array[pivot_pos] = array[i]
            print("pos-{} : {}  , pos-{}:  {} ".format(pivot_pos, array[pivot_pos], i, array[i]))
            array[i] = array[pivot_pos - 1]
            print("pos-{} : {}  , pos-{}:  {} ".format(i, array[i], pivot_pos, array[pivot_pos]))
            array[pivot_pos - 1] = pivot
            pivot_pos = pivot_pos - 1
            print(
                "pos-{} : {}  , pivot--> pivot_pos : {} , pivot_val  {} ".format(len(array) - 2, array[len(array) - 2],
                                                                                 pivot_pos, pivot))
            print("array : {} \n".format(array))
        elif array[i] >= pivot:
            print("array[i]:{} >= pivot:{}".format(array[i], pivot))
            pivot_pos = len(array) - 1
            pivot = array[pivot_pos]
            i += 1
            print("\nPivot changed ... i : {} , pivot--> pivot_pos : {} , pivot_val  {} ".format(i, pivot_pos, pivot))
            print("array : {} \n".format(array))
        else:
            i += 1

    return array


# test = [21, 4, 1, 3, 9, 20, 25, 6, 21, 14]
test = [8, 3, 1, 7, 0, 10, 2]
print(quicksortWithLogging(test))
# print(quicksort(test))
