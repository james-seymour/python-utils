from typing import Iterable, Iterator, List, Tuple


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

def read_input(filename: str) -> List[str]:
    with open(filename) as f:
        return f.readlines()

def read_aoc_input(day: int | str) -> List[str]:
    return read_input(f"day_{day}_input.txt")

def parse_int_to_tuple(lines) -> Tuple[int]:
    return tuple(map(int, (lines)))

def parse_int_to_list(lines) -> List[int]:
    return list(map(int, (lines)))

def zip_data(data: Iterable, window_size = 2) -> Iterator[Tuple]:
    """ Zips a data set into windows\n 
        Default window size is 2, which is equivalent to pairing successive values from the data set 
    """
    windows = [ data[i:] for i in range(window_size) ]
    return zip(*windows)