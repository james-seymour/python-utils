from typing import Dict, Iterable, Tuple

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
 
def deepmap(f, x):
    return [deepmap(f, a) for a in x] if isinstance(x, list) else f(x)

def reverse_dict(d: Dict) -> Dict:
    return {v: k for k, v in d.items()}

def flatten(x):
    if isinstance(x, tuple | list):
        for a in x:
            yield from flatten(a)
    else:
        yield x