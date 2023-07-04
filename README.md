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
    
2. **Iterators terminating on the shortest input sequence:** `accumulate`, `chain`, `groupby`, `islice`, `starmap`, `tee`, `zip_longest`, etc. These functions create an iterator that returns elements from the input iterable(s) in a specific pattern. For example, `zip_longest('ABCD', 'xy', fillvalue='-')` returns an iterator that generates the tuples ('A', 'x'), ('B', 'y'), ('C', '-'), ('D', '-').
    
3. **Combinatoric generators:** `combinations`, `combinations_with_replacement`, `permutations`, `product` These functions return iterators that generate all possible combinations or permutations of the input iterable(s). For example, `combinations('ABCD', 2)` generates all 2-element combinations of 'ABCD'.
    

Overall, `itertools` provides a set of powerful tools for creating and working with iterators, making it easier to write efficient code for handling sequences and other iterable objects.