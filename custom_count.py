def count(first, step=1):
    while True:
        yield first
        first += step

if __name__ == "__main__":
    counter = count(10)
    print(next(counter))
    print(next(counter))
    for val in counter:
        print(val)