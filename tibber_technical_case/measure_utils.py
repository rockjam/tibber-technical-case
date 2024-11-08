from datetime import datetime


# measures the time taken by the `func` lambda to execute.
# returns returned value of the `func`, and execution duration in seconds.
def measure_execution_time(func):
    start_time = datetime.now()
    result = func()
    end_time = datetime.now()
    execution_time = (end_time - start_time).total_seconds()
    return result, execution_time
