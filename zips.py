from statistics import mean
from itertools import zip_longest

ES = (22,26,18)
MG = (16,20.29,18,14)
RJ = (25,18,22,20,15)
SP = (22,20,21,17,19,21,22)

z = zip(ES, MG, RJ, SP)

print(mean(next(z)))
print(mean(next(z)))
print(mean(next(z)))
print(mean(next(z))) ## will broke because of the different sizes

z = zip_longest(ES, MG, RJ, SP, fillvalue=None)

print(mean(next(z)))
print(mean(next(z)))
print(mean(next(z)))
print(mean(filter(None,(next(z)))))  ## will not broke because of the different sizes