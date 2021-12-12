import utils.builtins
import time

def bind_func(instance, func, as_name=None):
    """
    Bind the function *func* to *instance*, with either provided name *as_name*
    or the existing name of *func*. The provided *func* should accept the 
    instance as the first argument, i.e. "self".
    """
    if as_name is None:
        as_name = func.__name__

    bound_method = func.__get__(instance, instance.__class__)
    setattr(instance, as_name, bound_method)
    return bound_method

def immutable_args(func):
    """ Decorator which attempts to make the arguments of a function
        immutable before execution. 

        This is achieved by casting any iterable arg passed to the function
        to a tuple. For example,

        func([1, 2, 3, 4, 5]) -> func((1, 2, 3, 4, 5))
        func([[1,2], [3,4], [5,6]]) -> func(((1,2), (3,4), (5,6)))
    """
    def wrapper(*args, **kwargs):
        args = utils.builtins.deep_iter_to_tuple(args)
        result = func(*args, **kwargs)
        return result
    return wrapper

def timed(debug=False, out=False):
    """ Debugging decorator that times function calls in seconds.

    If *debug* is True, the time taken for the function call will be printed to console

    If *out* is True, the function will return a tuple of (result, time)  
    """
    def inner(func):
        def wrapper(*args, **kwargs):

            t0 = time.time()
            result = func(*args, **kwargs)
            t1 = time.time()
            elapsed = round(t1 - t0, 3)
            if debug:
                print(f"{func.__name__} took {elapsed}s")
            if out:
                return result, elapsed
            return result

        return wrapper
    return inner