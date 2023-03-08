from functools import wraps
import time


# Round trip time
def get_RTT(func):
    @wraps(func)
    def get_RTT_wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        rtt_time = end_time - start_time
        rtt_time = float("{:.2f}".format(rtt_time * 1000))
        return (result, rtt_time)

    return get_RTT_wrapper
