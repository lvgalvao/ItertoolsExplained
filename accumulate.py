import operator
from functools import reduce

def accumulate(iterable, func=operator.add, *, initial=None):
    'Return running totals'
    # accumulate([1,2,3,4,5]) --> 1 3 6 10 15
    # accumulate([1,2,3,4,5], initial=100) --> 100 101 103 106 110 115
    # accumulate([1,2,3,4,5], operator.mul) --> 1 2 6 24 120

    it = iter(iterable)
    total = initial
    if initial is None:
        try:
            total = next(it)
        except StopIteration:
            return
    yield total
    for element in it:
        total = func(total, element)
        yield total

if __name__ == '__main__':
    print(list(accumulate([1,2,3,4,5]))) # [1, 3, 6, 10, 15]
    print(reduce(operator.add, accumulate([1,2,3,4,5]))) # 35

    print(list(accumulate([1,2,3,4,5], initial=100)))
    print(list(accumulate([1,2,3,4,5], operator.mul)))