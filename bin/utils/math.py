
from functools import reduce, lru_cache
from math import gcd
from typing import Dict, Iterable, List, Tuple, TypeVar
from re import compile
from operator import mul
from utils.tuple_list import deep_list_to_tuple
from utils.func import flatten as _flatten

T = TypeVar("T")

def prod(a: Iterable[int | float]):
    return reduce(mul, a) 

def bin_to_int(bin: str):
    return int(bin, 2)

def lcm(a, b):
    return a * b // gcd(a, b)

def lcm_many(args):
    return reduce(lcm, args)

def gcd_many(args):
    return reduce(gcd, args)

def map_int(l: List[str]) -> List[int]:
    return [int(x) for x in l]

def map_float(l: List[str]) -> List[float]:
    return [float(x) for x in l]

INT_REGEX = compile(r'-?\d+')
UINT_REGEX = compile(r'\d+')
def find_ints(s: str) -> List[int]:
    """ Returns all instances of an integer within a string """
    return map_int(INT_REGEX.findall(s))

def find_uints(s: str) -> List[int]:
    """ Returns all instances of a positive integer within a string """
    return map_int(UINT_REGEX.findall(s))

@lru_cache(maxsize=None)
def digits(num, output_len=None) -> Tuple[int]:
    """ Returns the digits of a number as a tuple """
    out = []
    i = 0
    while True:
        out.append(num % 10)
        num //= 10
        i += 1
        if (output_len is not None and i >= output_len) or num == 0:
            break
    if output_len is not None:
        for _ in range(output_len - i):
            out.append(0)
    out.reverse()
    return tuple(out)

def list_to_tuple(func):
    def wrapper(*args, **kwargs):
        args = deep_list_to_tuple(args) # Makes the input immutable so lru_cache doesn't whine
        result = func(*args, **kwargs)
        return result
    return wrapper

@list_to_tuple
@lru_cache
def count_freq(obj: Iterable[T], flatten=False) -> Dict[T, int]:
    """ Counts the frequency of each object in an iterable.\n
        Optional kwarg flatten=True unpacks a multidimensional iterable to count frequency.\n 
        Make sure to define a __eq__ method to count properly
    """
    if flatten:
        obj = _flatten(obj)

    out = {}
    for x in obj:
        if x not in out: 
            out[x] = 0
        out[x] += 1
    return out

def factorial(num: int) -> int:
    """ Returns the factorial of a number"""
    out = num
    for i in range(0, out, -1):
        out *= i
    return out



