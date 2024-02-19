import time
from typing import Callable, Any
global totalTime
totalTime = 0

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
def measureTime(fn:Callable[...,Any], *args:Any, **kwargs:Any) -> Any:
    global totalTime
    startTime = time.time()
    response = fn(*args, **kwargs)
    endTime = time.time()
    totalTime += (endTime - startTime)
    return response