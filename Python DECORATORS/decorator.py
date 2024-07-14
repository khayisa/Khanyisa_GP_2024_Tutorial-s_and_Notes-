 import time

def timer(func): #decorator function will always expect atleast one argument 
    def wrapper(*args,**kwargs):# this tell us allows us to except any number of positional functions and any number of keyword functions 
        start_time = time.time()#start time
        result = func(*args,**kwargs) # call the decorated function 
        end_time = time.time() #end time 
        print(f"Function{func.__name__!r} took:{ end_time - start_time:.4f} sec")
        return result # we always wanna store the decorated function 

    return wrapper


def example_function(n):
    return f"The sum is {sum(range(n))}"

example_function = timer(example_function)

print(example_function(1000000))