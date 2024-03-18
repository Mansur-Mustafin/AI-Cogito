import time
from typing import Callable, Any
from memory_profiler import memory_usage

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
    memory_result = memory_usage((func, args), retval=True)
    end_time = time.time()
    function_result = memory_result[1] 
    memory_usage_result = memory_result[0] 
    execution_time = end_time - start_time
    max_memory = max(memory_usage_result) - min(memory_usage_result)

    return function_result,execution_time, max_memory
