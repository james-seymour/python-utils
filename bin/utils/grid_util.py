from typing import Iterator, List, Tuple


CARDINAL_OFFSETS = {
    "N": (-1, 0), 
    "E": (1, 0), 
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

def neighbours(pos: Tuple[int, int], offsets=CARDINAL_OFFSETS) -> Iterator[Tuple[int, int]]:
    """ Gives the indices of neighbouring elements as a row, col pair\n
        Does NOT check bounds of indices\n
        Can use offsets=CARDINAL_OFFSETS_EXTENDED for 8 way checking.
    """
    x_i, y_i = pos
    for x_off, y_off in offsets.values():
        yield (x_i + y_off, y_i + x_off)

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

