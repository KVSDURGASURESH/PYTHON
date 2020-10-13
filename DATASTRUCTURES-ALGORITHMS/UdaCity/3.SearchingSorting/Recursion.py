"""Implement a function recursively to get the desired
Fibonacci sequence value.
Your code should have the same input/output as the
iterative code in the instructions.

example of the sequence:
0,1,1,2,3,5,8,13,21,34..."""


# this is a previous function with recursion
def getFibWithoutRecursion(position):
    if position == 0:
        return 0
    if position == 1:
        return 1
    first = 0
    second = 1
    next = first + second

    for i in range(2, position):
        first = second
        second = next
        next = first + second

    return next


def get_fib(position):
    if position == 0 or position == 1:
        return position
    return get_fib(position - 1) + get_fib(position - 2)




# print("first : {} , second : {}, next : {}, i : {} ".format(first, second, next, i))
# Test cases
# print(getFibWithoutRecursion(9))
# print(getFibWithoutRecursion(11))
# print(getFibWithoutRecursion(0))

print(get_fib(9))
# print(get_fib(11))
# print(get_fib(0))
