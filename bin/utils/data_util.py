from typing import Iterable, Iterator, Tuple


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

def read_input(day: int):
    with open(f"day_{day}_input.txt") as f:
        return f.readlines()

def parse_to_tuple(lines):
    return tuple(map(int, (lines)))

def parse_to_list(lines):
    return list(map(int, (lines)))

def zip_data(data: Iterable, window_size = 2) -> Iterator[Tuple]:
    """ Zips a data set into windows\n 
        Default window size is 2, which is equivalent to pairing successive values from the data set 
    """
    windows = [ data[i:] for i in range(window_size) ]
    return zip(*windows)