from time import time


def get_rrt(start_time: float):
    end_time = time()
    rtt_time = end_time - start_time
    rtt_time = float("{:.2f}".format(rtt_time * 1000))
    return rtt_time
