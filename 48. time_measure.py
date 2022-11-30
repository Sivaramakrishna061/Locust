import inspect
import time
from locust import events
import sys

def decorate_time(func):
    def my_wrapper(*args, **kwargs):
        task_name=sys._getframe(1).f_code.co_name

        # # get task's function name
        # previous_frame = inspect.currentframe().f_back
        # _, _, task_name, _, _ = inspect.getframeinfo(previous_frame)

        start = time.time()
        result = None
        try:
            result = func(*args, **kwargs)
        except Exception as e:
            total = int((time.time() - start) * 1000)
            events.request_failure.fire(request_type="TYPE",
                                        name=task_name,
                                        response_time=total,response_length=0,
                                        exception=e)
        else:
            total = int((time.time() - start) * 1000)
            events.request_success.fire(request_type="TYPE",
                                        name=task_name,
                                        response_time=total,
                                        response_length=0)
        return result

    return my_wrapper
