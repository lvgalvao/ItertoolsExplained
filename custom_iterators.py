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

# Example usage:

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
