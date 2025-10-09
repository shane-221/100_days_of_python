import time

current_time = time.time()

# Write your code below 👇

def speed_calc_decorator(function):
    def wrapper_function ():
        start_time = time.time()
        function()
        end_time =time.time()
        time_taken = end_time-start_time
        print(f"{function.__name__} run speed :{time_taken}")
    return wrapper_function

@speed_calc_decorator
def fast_function():
    for i in range(1000000):
        i * i
fast_function()

@speed_calc_decorator
def slow_function():
    for i in range(10000000):
        i * i
slow_function()