import time
from typing import Callable, Any


def measureTime(fn: Callable[..., Any], *args: Any, **kwargs: Any) -> Any:
    """
    Measures the execution time of a function and updates the total execution time.

    :param fn: function to mesure
    :type fn: Callable
    :param args: Positional arguments to be passed to the function
    :type args: Any
    :param kwargs: Keyword arguments to be passed to the function.
    :type kwargs: Any
    :return: The return value of the function being measured.
    :rtype: Any
    """
    startTime = time.time()
    response = fn(*args, **kwargs)
    endTime = time.time()
    totalTime = (endTime - startTime)
    return (response, totalTime)


def measure_performance(func, *args) -> Any:
    start_time = time.time()
    mem_usage = memory_usage((func, args))
    end_time = time.time()

    execution_time = end_time - start_time
    max_memory = max(mem_usage) - min(mem_usage)

    return execution_time, max_memory
