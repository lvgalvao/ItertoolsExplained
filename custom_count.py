def count(start, setp=1):
    count = start
    while True:
        yield count
        count += setp

counter = count(1)
print(next(counter)) # 1
print(next(counter)) # 2
print(next(counter)) # 3

for val in counter:
    print(val)