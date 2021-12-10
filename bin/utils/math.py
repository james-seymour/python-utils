
from functools import reduce, lru_cache
from math import gcd
from typing import Dict, Iterable, List, Tuple, TypeVar
from re import compile
from operator import mul
from utils.builtins import flatten as _flatten
from utils.func import immutable_args

_T = TypeVar("_T")

def prod(a: Iterable[int | float]):
    return reduce(mul, a) 

def bin_to_int(bin: str):
    return int(bin, 2)

def hex_to_int(hex: str):
    return int(bin, 16)

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


# Can uncomment this out for very big sizes
# @lru_cache()
@immutable_args
def count_freq(obj: Iterable[_T], flatten=False) -> Dict[_T, int]:
    """ Counts the frequency of each object in an iterable.\n
        Requires a definition of __eq__ and __hash__ methods.\n
        Optional kwarg flatten=True unpacks a multidimensional iterable to count frequency.\n 
        Recommended to define a __repr__ to easily display freqs\n
    """
    if flatten:
        obj = _flatten(obj)

    out = {}
    for x in obj:
        if x not in out: 
            out[x] = 0
        out[x] += 1
    return out

@lru_cache(maxsize=256)
def factorial(num: int) -> int:
    """ Returns the factorial of a number"""
    if num == 0 or num == 1:
        return 1
    else:
        return num * factorial(num - 1)

def sum_between_range(min: int, max: int) -> int:
    """ Returns the sum of all integers between min and max"""
    return ((max - min + 1) *  (max + min)) / 2

def sum_to_n(n: int) -> int:
    """ Returns the sum of all integers between 1 and n """
    return (n * (n + 1)) / 2