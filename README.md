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