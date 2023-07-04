# Python Itertools Showcase

Welcome to Python Itertools Showcase! This repository provides clear, concise examples demonstrating the functionalities of Python's itertools library.

## What is itertools?

`itertools` is a Python library that provides a set of convenient iterators, offering fast, memory-efficient tool for creating complex iterations.

An iterator is an object that can be iterated (that is, you can 'traverse' the object, one element at a time).

In Python, an iterator is any object that implements the `__iter__` method (which should return the object itself) and the `__next__` method (which should return the next value from the iterator).

```python
my_list = [1,2,3,4,5]

# Create an iterator using the list
my_iterator = iter(my_list)

# Print elements from iterator
print(next(my_iterator)) # 1
print(next(my_iterator)) # 2
```

All sequence types in Python are iterable:

- lists
- tuples
- strings
- dictionaries
- sets
- bytes
- ...

Sure, let's take a look at how we can build our own version of a for loop in Python using an iterable object. This will help us understand the underlying mechanics of iteration in Python. The built-in for loop in Python internally uses an iterator to iterate over an iterable object.

Here is how we can simulate the behavior of a for loop. Let's take a look at `custom_iterastors.py`

```python
import time

def my_for(iterable, function):
    iterator = iter(iterable)  # Create an iterator object from iterable
    while True:
        try:
            item = next(iterator)  # Get the next item
            time.sleep(1)
        except StopIteration:
            # If StopIteration is raised, break from loop
            break
        else:
            function(item)  # Execute the function with the item
```

Example usage:

```python
if __name__ == '__main__':
    my_list = [1, 2, 3]
    print('My for method')
    
    my_for(my_list, print)  # This will print each element in the list
    time.sleep(1)
    
    print('My for method with lambda')
    time.sleep(1)
    
    my_for(my_list, lambda x: print(x ** 2))  # This will print each element squared
    time.sleep(1)
    
    print('built-in for method')
    time.sleep(1)
    
    my_for(my_list, print)  # This will print each element in the list
    time.sleep(1)
    
    print('built-in for method with lambda')
    time.sleep(1)
    
    for item in my_list:
        (lambda x: print(x ** 2))(item)
        time.sleep(1)
```

## Lazy evaluation

Lazy evaluation, or call-by-need, refers to an evaluation strategy which delays the evaluation of an expression until its value is actually needed. In Python, iterators, generators and certain built-in functions use lazy evaluation.

The main advantage of lazy evaluation is efficiency. By computing values only when they are required, you can potentially save a lot of processing power and memory, especially when working with large data structures.

Here are two examples using Python iterators that demonstrate lazy evaluation:

1. Using range() function: The range() function is a perfect example of lazy evaluation. When you call range(n), Python doesn't immediately generate a list of all numbers from 0 to n-1. Instead, it creates a range object that generates numbers on-the-fly as you loop over them.

```python
for i in range(10**12):  # creating a range of trillion numbers
    if i > 100:  # we are only interested in the first 101 numbers
        break
    print(i)
```

In this example, we create a range of a trillion numbers but only print the first 101. Thanks to lazy evaluation, Python doesn't actually create a trillion numbers, which would take an enormous amount of memory. Instead, it generates each number as we loop through the range.

2. Using Generators: Generators in Python are a type of iterable defined using a function rather than being stored in a data structure. They generate values on the fly as you iterate over them, and hence are an example of lazy evaluation.

```python
def infinite_sequence():
    num = 0
    while True:
        yield num
        num += 1

for i in infinite_sequence():
    if i > 100:  # we are only interested in the first 101 numbers
        break
    print(i)
```

In this example, we define an infinite sequence using a generator function. The function generates an infinite series of numbers, starting from 0. However, because generators use lazy evaluation, only the numbers we loop over are actually generated. As with the range() example, this saves a lot of memory.

Keep in mind, the real benefit of using lazy evaluation comes when dealing with larger datasets or when the computation required to generate each value is intensive.

## Why using Lazy evaluation in Python? 

Lazy evaluation in Python offers several advantages, particularly when working with large amounts of data or complex computations. Here are some key reasons why you might want to use lazy evaluation:

1. Efficiency: Lazy evaluation can be more efficient because it only computes values as they're needed. This can save significant computational resources when working with large data sets or complex functions, as you avoid unnecessary calculations.

2. Memory conservation: In traditional (eager) evaluation, data is generated and stored in memory all at once. For large data sets, this can quickly use up your system's memory and cause your program to slow down or crash. Lazy evaluation, on the other hand, generates data on-the-fly as needed, significantly reducing memory usage.

3. Working with infinite sequences: Lazy evaluation enables you to work with infinite sequences or data streams. Since data is only generated as needed, you can define an infinite sequence (like a sequence of all prime numbers or all Fibonacci numbers) without running out of memory or entering an infinite loop.

Keep in mind that while lazy evaluation has many benefits, it's not always the best choice. It can add complexity to your code and make debugging more challenging because values aren't computed until they're needed. Furthermore, if the entire dataset is needed at once, or multiple times, then lazy evaluation might end up being slower than eager evaluation because of the overhead of generating the data repeatedly. Always consider the specific needs of your project when deciding whether to use lazy evaluation.

## Here are some examples of Python built-in functions that utilize lazy evaluation:

1. `zip()`: is used to combine two or more iterables into a single iterable. It generates a tuple where the first element comes from the first iterable, the second element comes from the second iterable, and so on.

```python
names = ['Alice', 'Bob', 'Charlie']
ages = [25, 30, 35]
combined = zip(names, ages)
for name, age in combined:
    print(f"{name} is {age} years old.")
```

2. `map()`: map() is used to apply a function to all elements in an input list.

```python
numbers = [1, 2, 3, 4]
squares = map(lambda x: x ** 2, numbers)
for square in squares:
    print(square)
```

3. `reversed()`: reversed() is used to reverse the order of elements in an iterable.

```python
numbers = [1, 2, 3, 4]
for number in reversed(numbers):
    print(number)
```

4. `filter()`: filter() is used to filter elements from an iterable.

```python
numbers = [1, 2, 3, 4, 5, 6]
even_numbers = filter(lambda x: x % 2 == 0, numbers)
for even_number in even_numbers:
    print(even_number)
```

Note that in each of these examples, the built-in function doesn't immediately generate all the output. Instead, it creates an iterable that generates the elements on-the-fly as you loop over it. This is an example of lazy evaluation.

## So, What is itertools in python?

`itertools` is a module in Python's standard library that contains several functions that are useful for creating and working with iterators. It offers a set of efficient, looping constructs that are inspired by constructs from APL, Haskell, and SML.

The tools provided by `itertools` are fast and memory efficient. They can be used for a variety of tasks, such as grouping data, creating permutations and combinations, generating infinite sequences, and more.

The functions in `itertools` can be broadly classified into three categories:

1. **Infinite Iterators:** `count`, `cycle`, `repeat` These functions return infinite iterators. For example, `count(10)` returns an iterator that generates consecutive integers starting at 10, `cycle('ABCD')` returns an iterator that repeats the sequence 'ABCD' infinitely.
    
 ```python
import itertools

# count(start, step)
counter = itertools.count(start=10, step=5)
for i in range(5):
    print(next(counter))  # Prints: 10, 15, 20, 25, 30
```
   
2. **Iterators terminating on the shortest input sequence:** `accumulate`, `chain`, `groupby`, `islice`, `starmap`, `tee`, `zip_longest`, etc. These functions create an iterator that returns elements from the input iterable(s) in a specific pattern. For example, `zip_longest('ABCD', 'xy', fillvalue='-')` returns an iterator that generates the tuples ('A', 'x'), ('B', 'y'), ('C', '-'), ('D', '-').

```python
import itertools

# chain(*iterables)
# This function takes several iterables and returns a single iterator that produces the contents of all of them as though they were a single sequence
result = itertools.chain("ABC", "DEF")
for letter in result:
    print(letter)  # Prints: 'A', 'B', 'C', 'D', 'E', 'F'
```
    
3. **Combinatoric generators:** `combinations`, `combinations_with_replacement`, `permutations`, `product` These functions return iterators that generate all possible combinations or permutations of the input iterable(s). For example, `combinations('ABCD', 2)` generates all 2-element combinations of 'ABCD'.

```python
import itertools

# permutations(iterable, r=None)
# This function returns successive r-length permutations of elements in the iterable where r is the length of each permutation.
result = itertools.permutations("AB", 2)
for item in result:
    print(item)  # Prints: ('A', 'B'), ('B', 'A')
```
    
Overall, `itertools` provides a set of powerful tools for creating and working with iterators, making it easier to write efficient code for handling sequences and other iterable objects.

## Cycle

The `itertools.cycle` function in Python returns an iterator that produces elements from the iterable you give it, and saves a copy of the iterable. When the iterable is exhausted, it "cycles" back to the beginning and starts producing elements again. This makes it useful for creating infinite iterators.

Here's a basic example:

```python
import itertools

counter = itertools.cycle('ABC')
for _ in range(10):
    print(next(counter))
```

In this example, `itertools.cycle` is given a string `'ABC'`. It produces an iterator that generates the characters `'A'`, `'B'`, `'C'`, `'A'`, `'B'`, `'C'`, and so on, repeating the sequence indefinitely. The loop in this example only runs 10 times, so it only prints the first 10 elements of the cycle: `'A'`, `'B'`, `'C'`, `'A'`, `'B'`, `'C'`, `'A'`, `'B'`, `'C'`, `'A'`.

It's important to note that `itertools.cycle` does not make a copy of the input iterable, so it can be used with large or infinite iterables without using a lot of memory. However, because it repeats indefinitely, you should be careful to ensure that your program doesn't enter an infinite loop when using it.

## Repeat

The `itertools.repeat` function in Python's itertools module returns an iterator that produces the same value over and over again, indefinitely. If a second parameter, `times`, is given, it will produce the value that number of times, otherwise it will repeat indefinitely.

Here's an example:

```python
import itertools

# Repeat the number 5 three times
for number in itertools.repeat(5, 3):
    print(number)  # Prints: 5, 5, 5
```

In this example, `itertools.repeat` is given the number 5 and the number 3. It returns an iterator that produces the number 5, three times.

Here is an example where `itertools.repeat` is used without the `times` parameter:

```python
import itertools

repeat_10 = itertools.repeat(10)
for _ in range(5):
    print(next(repeat_10))  # Prints: 10, 10, 10, 10, 10
```

In this example, `itertools.repeat` is given only the number 10. It returns an iterator that produces the number 10 indefinitely. The loop in this example only runs 5 times, so it only prints the number 10, five times.

Keep in mind that if the `times` parameter is not provided, `itertools.repeat` will return an infinite iterator. So be careful to ensure that your program doesn't enter an infinite loop when using it.

## Accumulate

The `itertools.accumulate` function in Python is part of the itertools module. It makes an iterator that returns the results of a function which is applied to a sequence of pairwise elements. If the input iterable is empty, the output iterable will also be empty.

By default, the function is operator.add (which performs addition). If no function is specified, it computes the accumulated sum of the elements. If a function is provided, it must be a function of two arguments.

Here's an example with the default behavior:

```python
import itertools

numbers = [1, 2, 3, 4, 5]
result = itertools.accumulate(numbers)

for num in result:
    print(num)
# Output: 1, 3, 6, 10, 15
```

In this example, `accumulate` computes the running total of the numbers in the list. The output is the sequence of partial sums: 1, 1+2=3, 1+2+3=6, 1+2+3+4=10, 1+2+3+4+5=15.

You can also provide a function to `accumulate`. Here's an example with multiplication:

```python
import itertools
import operator

numbers = [1, 2, 3, 4, 5]
result = itertools.accumulate(numbers, operator.mul)

for num in result:
    print(num)
# Output: 1, 2, 6, 24, 120
```

In this example, `accumulate` computes the running product of the numbers in the list using the `operator.mul` function. The output is the sequence of partial products: 1, 1_2=2, 1_2_3=6, 1_2_3_4=24, 1_2_3_4_5=120.

## Product

The `itertools.product` function in Python's itertools module is essentially the equivalent of nested for-loops. It computes the Cartesian product of the input iterables. This results in all possible pairs of elements if given two lists, all possible triples if given three lists, and so forth.

Here is a simple example with two lists:

```python
import itertools

for pair in itertools.product([1, 2, 3], ['a', 'b']):
    print(pair)
# Output: (1, 'a'), (1, 'b'), (2, 'a'), (2, 'b'), (3, 'a'), (3, 'b')
```

In this example, `itertools.product` generates all pairs of numbers and letters.

`itertools.product` can also generate all possible combinations with replacement from a single iterable. Here's an example:

```python
import itertools

for pair in itertools.product('AB', repeat=2):
    print(pair)
# Output: ('A', 'A'), ('A', 'B'), ('B', 'A'), ('B', 'B')
```

In this example, the `repeat=2` argument tells `product` to generate all pairs of elements from the string 'AB', including pairs where the elements are the same.

`itertools.product` can be very useful for generating all possible combinations of values for testing, solving combinatorial problems, and more.

## Permutations

The `itertools.permutations` function in Python's itertools module returns successive r length permutations of elements in the iterable.

A permutation is an arrangement of objects in a specific order. The order of arrangement of the object is very crucial. The number of permutations on a set of n elements is given by n!.

Here is a simple example:

```python
import itertools

for p in itertools.permutations('ABC', 2):
    print(p)
# Output: ('A', 'B'), ('A', 'C'), ('B', 'A'), ('B', 'C'), ('C', 'A'), ('C', 'B')
```

In this example, `itertools.permutations` generates all pairs of letters from the string 'ABC', with the order of the letters taken into account. So ('A', 'B') and ('B', 'A') are considered to be different permutations.

If no length is provided, then `itertools.permutations` defaults to the length of the iterable. Here's an example:

```python
import itertools

for p in itertools.permutations('ABC'):
    print(p)
# Output: ('A', 'B', 'C'), ('A', 'C', 'B'), ('B', 'A', 'C'), ('B', 'C', 'A'), ('C', 'A', 'B'), ('C', 'B', 'A')
```

In this example, `itertools.permutations` generates all permutations of the string 'ABC'. The output includes all possible ways of ordering the three letters.

`itertools.permutations` is useful in scenarios where you want to generate all possible arrangements of elements, such as in certain types of problems in combinatorics or in testing.

## Combinations

The `itertools.combinations` function in Python's itertools module returns successive r-length combinations of elements in the iterable. Combinations are emitted in lexicographic sort order, so if the input iterable is sorted, the combination tuples will be produced in sorted order.

A combination is a selection of items where the order does not matter. This is in contrast to permutations, where the order of the items does matter.

Here's an example of using `itertools.combinations`:

```python
import itertools

for c in itertools.combinations('ABC', 2):
    print(c)
# Output: ('A', 'B'), ('A', 'C'), ('B', 'C')
```

In this example, `itertools.combinations` generates all pairs of letters from the string 'ABC', with the order of the letters not taken into account. So ('A', 'B') and ('B', 'A') are considered to be the same combination and only ('A', 'B') is generated.

If you need to generate all combinations including those with repeated elements, you can use the `itertools.combinations_with_replacement` function:

```python
import itertools

for c in itertools.combinations_with_replacement('ABC', 2):
    print(c)
# Output: ('A', 'A'), ('A', 'B'), ('A', 'C'), ('B', 'B'), ('B', 'C'), ('C', 'C')
```

`itertools.combinations` and `itertools.combinations_with_replacement` can be useful in scenarios where you need to generate all possible selections of elements, such as in certain types of problems in combinatorics or in testing.