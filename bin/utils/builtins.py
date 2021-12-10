from typing import Callable, Dict, Iterable, Tuple

def tuple_add(x: Tuple[int], y: Tuple[int]) -> Tuple[int]:
    assert len(x) == len(y)
    return tuple(xi + yi for xi, yi in zip(x,y))

def tuple_sub(x: Tuple[int], y: Tuple[int]) -> Tuple[int]:
    assert len(x) == len(y)
    return tuple(xi - yi for xi, yi in zip(x,y))

def tuple_mul(x: Tuple[int], y: Tuple[int]) -> Tuple[int]:
    assert len(x) == len(y)
    return tuple(xi * yi for xi, yi in zip(x,y))

def tuple_scale_mul(k: int, x: Tuple[int]) -> Tuple[int]:
    return tuple(k * xi for xi in x)

def deep_list_to_tuple(x):
    return tuple(map(deep_list_to_tuple, x)) if isinstance(x, (list, tuple)) else x
 
def deepmap(f: Callable, x: Iterable, callable_type: Callable = list) -> Iterable:
    """
    Given a nested iterable, apply a func to each element in that iterable.
    callable_type argument determines how the iterable is returned (e.g. list, tuple)
    """
    return callable_type(deepmap(f, a, callable_type) for a in x) if isinstance(x, Iterable) else f(x)

def dict_map_keys(f: Callable, x: Dict):
    """
        Applies the function f to each key in the dictionary and returns a new dictionary
    """
    return dict(zip(map(f, x.keys()), x.values()))

def dict_map_vals(f: Callable, x: Dict): 
    """
        Applies the function f to each value in the dictionary and returns a new dictionary
    """
    return dict(zip(x.keys(), map(f, x.keys())))

def dict_map_key_vals(key_f: Callable, val_f: Callable, x: Dict):
    """
        Applies the key_f function to all keys in the dictionary\n
        Applies the val_f function to all values in the dictionary\n
        Returns a new dictionary\n
    """
    return dict(zip(map(key_f, x.keys()), map(val_f, x.values())))

def reverse_dict(d: Dict) -> Dict:
    return {v: k for k, v in d.items()}

def flatten(x):
    if isinstance(x, tuple | list):
        for a in x:
            yield from flatten(a)
    else:
        yield x