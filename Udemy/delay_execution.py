# delays the execution of a function with a @delay(delayInSeconds) decorator

from time import sleep
from functools import wraps

def delay(timer):
    def inner(fn):
        @wraps(fn)
        def wrapper(*args, **kwargs):
            print("Waiting {} seconds before running {}".format(timer, fn.__name__))
            sleep(timer)
            return fn(*args, **kwargs)
        return wrapper
    return inner


@delay(3)
def say_hi():
    print("hi")


say_hi()
