import time

global totalTime
totalTime = 0

def measureTime(fn, *args, **kwargs):
    global totalTime
    startTime = time.time()
    response = fn(*args, **kwargs)
    endTime = time.time()
    totalTime += (endTime - startTime)
    return response