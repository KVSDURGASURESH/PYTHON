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


# with logging
def binary_search_with_logging(input_array, value):
    bp = len(input_array) // 2
    isMatchIndex = bp
    for x in range(bp):
        print("bp_len : {} ; x : {} ; bp_val : {} ".format(bp, x, input_array[bp]))
        print("checking if {} > {}".format(value, input_array[bp]))

        if len(input_array) > 1 and value > input_array[bp]:
            print("In Right Branch  - {} > {} and bp: {}".format(value, input_array[bp], bp))

            input_array = input_array[(bp + 1): len(input_array)]
            print("input_array in if {} ".format(input_array))

            bp = len(input_array) // 2
            isMatchIndex = isMatchIndex + bp
            print("bp_right : {} ; x : {} ; isMatchIndex : {} ".format(input_array[bp], x, isMatchIndex))
            print("checking if {} = {} and len {}".format(value, input_array[bp], len(input_array)))

        elif len(input_array) > 1 and value < input_array[bp]:
            print("In Left Branch - {} < {} and bp: {}".format(value, input_array[bp], bp))
            input_array = input_array[:bp]
            print("input_array in else {} ".format(input_array))

            bp = len(input_array) // 2
            isMatchIndex = isMatchIndex - bp
            print("bp_left : {} ; x : {} ; isMatchIndex : {} ".format(input_array[bp], x, isMatchIndex))
            print("checking if {} = {}".format(value, input_array[bp]))

        elif value == input_array[bp]:
            print("I'm there ; x : {} ; isMatchIndex : {} ".format(x, isMatchIndex))
            return isMatchIndex

        else:
            print("I'm NOT there")
            return 0


def binary_search_old(input_array, value):
    bp = len(input_array) // 2
    isMatchIndex = bp

    for x in range(bp):

        # Right Branch
        if len(input_array) > 1 and value > input_array[bp]:
            input_array = input_array[(bp + 1): len(input_array)]
            bp = len(input_array) // 2

        # Left Branch
        elif len(input_array) > 1 and value < input_array[bp]:
            input_array = input_array[:bp]
            bp = len(input_array) // 2

        # Present
        elif len(input_array) == 1 and value == input_array[bp]:
            return isMatchIndex

        # Not Present
        else:
            return -1


def binary_search(input_array, value):

    for x in range(len(input_array) // 2):
        bp = len(input_array) // 2
        # Right Branch
        if len(input_array) > 1 and value > input_array[bp]:
            input_array = input_array[(bp + 1): len(input_array)]

        # Left Branch
        elif len(input_array) > 1 and value < input_array[bp]:
            input_array = input_array[:bp]

        # Present
        elif len(input_array) == 1 and value == input_array[bp]:
            return bp

        # Not Present
        else:
            return -1


# test_list = [1, 3, 9, 11, 12, 13, 15, 19, 29, 30]
test_list = [1, 3, 9, 11, 15, 19, 29]
test_val1 = 29
# test_val2 = 15
print(binary_search(test_list, test_val1))
# print(binary_search(test_list, test_val1))
# print(binary_search(test_list, test_val2))
