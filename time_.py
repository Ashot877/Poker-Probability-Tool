import time

def time_t(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"function {func.__name__} executed in {end - start:.7f} seconds")
        return result
    return wrapper