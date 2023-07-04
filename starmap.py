from itertools import starmap
from operator import mul

print(list(starmap(mul, zip([1,2,3], [4,5,6])))) # [4, 10, 18]

print(list(starmap(mul, enumerate([1,2,3,4])))) # [0, 2, 6, 12]

print(list(range(10)))

seq = list(range(10))

print(seq[2])

print(seq[2:7 :2])