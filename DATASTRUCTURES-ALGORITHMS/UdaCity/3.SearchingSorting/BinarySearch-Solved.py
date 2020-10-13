"""You're going to write a binary search function.
You should use an iterative approach - meaning
using loops.
Your function should take two inputs:
a Python list to search through, and the value
you're searching for.
Assume the list only has distinct elements,
meaning there are no repeated values, and
elements are in a strictly increasing order.
Return the index of value, or -1 if the value
doesn't exist in the list."""


def binary_search(input_array, value):
    low = 0
    high = len(input_array) - 1
    print("================ evaluating value {}:".format(value))
    while low <= high:
        mid = (high + low) // 2
        print("while - low: {}, mid : {}, high : {}\n".format(low, mid, high))
        if input_array[mid] == value:
            print("present - input_array: {} , low: {}, mid : {}, high : {}\n".format(input_array, low, mid, high))
            return mid
        elif input_array[mid] < value:
            print("right branch - input_array: {} , low: {}, mid : {}, high : {}".format(input_array, low, mid, high))
            low = mid + 1
            print("low: {}, mid : {}, high : {}\n".format(low, mid, high))
        else:
            print("left branch - input_array: {} , low: {}, mid : {}, high : {}".format(input_array, low, mid, high))
            high = mid - 1
            print("low: {}, mid : {}, high : {}\n".format(low, mid, high))
    return -1


test_list = [1, 3, 9, 11, 15, 19, 29]
test_val1 = 25
test_val2 = 15
print(binary_search(test_list, test_val1))
print(binary_search(test_list, test_val2))
