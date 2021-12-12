from typing import Iterator, List, Optional, Tuple
from math import ceil, floor

CARDINAL_OFFSETS = {
    "N": (-1, 0), 
    "E": (0, 1), 
    "S": (1, 0), 
    "W": (0, -1) 
}

CARDINAL_OFFSETS_EXTENDED = dict({
    "NE": (-1, 1), 
    "SE": (1, 1), 
    "SW": (1, -1), 
    "NW": (-1, -1)}, 
    **CARDINAL_OFFSETS
)

def int_lines_to_grid(lines: List[str]):
    """ Given a list of strings that each contain integers, return a grid of those integers """
    return [[int(char) for char in line] for line in lines]

def neighbours(pos: Tuple[int, int], grid: Optional[List[List[int]]]=None, extended=False) -> Iterator[Tuple[int, int]]:
    """ Gives the indices of neighbouring elements as a row, col pair in a 2D grid\n
        Optionally give this method your grid to filter all out of bounds indices.\n
        Can use extended=True to include diagonal indices.
    """
    offsets = CARDINAL_OFFSETS
    if extended:
        offsets = CARDINAL_OFFSETS_EXTENDED

    x_i, y_i = pos
    for x_off, y_off in offsets.values():
        new_row = x_i + y_off
        new_col = y_i + x_off

        if grid is None:        
            yield (new_row, new_col)

        if new_row in range(len(grid)) and new_col in range(len(grid[new_row])):
            yield (new_row, new_col)
        
def grid_pos_to_index(grid: List[List], pos: int) -> Tuple[int, int]:
    """ Works with uneven grids """
    count = 0
    for row_i, row in enumerate(grid):
        for col_i, element in enumerate(row):
            if count == pos:
                return row_i, col_i
            count += 1

def index_to_grid_pos(grid: List[List], index: Tuple[int, int]) -> int:
    """ Works with uneven grids """
    count = 0
    for row_i, row in enumerate(grid):
        for col_i, element in enumerate(row):
            if (row_i, col_i) == index:
                return count
            count += 1

def full(n_rows: int, n_cols: int, val) -> List[List[int]]:
    return [[val for _ in range(n_cols)] for _ in range(n_rows)]

def zeros(n_rows: int, n_cols: int):
    """
        Similar to np.zeros but returns a normal python list instead of an array.\n
        To specify a value to fill by, use "full"\n
    """
    return full(n_rows, n_cols, val=0)

def pack(incomplete_grid: List[List], val=0, side="right") -> List[List]:
    """
        Packs an incomplete 2D list (uneven row length) with a value (0 by default)\n
        side={"left", "right", "center} determines the side from which "val" is packed from
    """
    assert side in {"right", "left", "center"}
    max_col = max(*[len(row) for row in incomplete_grid])
    return [__pack_row(row, max_col, val, side) for row in incomplete_grid]

def __pack_row(row, n, val, side):
    match side:
        case "right":
            return row + (n-len(row)) * [val]
        case "left":
            return (n-len(row)) * [val] + row
        case "center":
            d = (n-len(row))/2
            l, r = floor(d), ceil(d) # left-bias
            return l * [val] + row + r * [val]

