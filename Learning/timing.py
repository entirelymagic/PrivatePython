import time


def measure_runtime(func):
    def wrapper(*args, **kwargs):  
        start = time.time()
        func(*args, **kwargs)
        end = time.time()
        runtime = end-start
        print(f"Finished {func.__name__!r} in {runtime:.4f} secs")

        return func
    return wrapper

@measure_runtime
def powers(limit):
    return [x**2 for x in range(limit)]


powers(5000000)
