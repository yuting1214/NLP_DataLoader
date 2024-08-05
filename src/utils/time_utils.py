import time
from typing import Callable, Any

def time_function(func: Callable, *args, **kwargs) -> Any:
    """
    Measures the time a function takes to execute.

    :param func: The function to time.
    :param args: Positional arguments to pass to the function.
    :param kwargs: Keyword arguments to pass to the function.
    :return: The result of the function execution.
    """
    start_time = time.time()
    result = func(*args, **kwargs)
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"Function {func.__name__} took {elapsed_time:.4f} seconds to execute.")
    return result