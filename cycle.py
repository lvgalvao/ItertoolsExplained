import itertools

counter = itertools.cycle('ABC')
for _ in range(10):
    print(next(counter))
