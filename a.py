from functools import reduce


def maximium(list):
    return reduce(lambda x, acc: acc if acc > x else x, list)
print(maximium([5,4,6,2,7]))