from itertools import chain

def custom_chain(*iterables):
    # chain('ABC', 'DEF') --> A B C D E F
    for it in iterables:
        for element in it:
            yield element

if __name__ == '__main__':
    my_chained = custom_chain('ABC', 'DEF')
    print(list(my_chained)) # ['A', 'B', 'C', 'D', 'E', 'F']
    chained = chain('ABC', 'DEF')
    print(list(chained)) # ['A', 'B', 'C', 'D', 'E', 'F']