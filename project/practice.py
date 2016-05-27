import numpy as np
from bisect import bisect_left

def phi_at_x( phi, grid, x ):
    index = index_of_grid_at_x( grid, x )
    return phi[ index ]

def index_of_grid_at_x( grid, x ):
    return closest_index( grid, x )
#     return bisect( grid, x )

def closest_index(myList, myNumber):
    """
    Assumes myList is sorted. Returns index of closest value to myNumber.

    If two numbers are equally close, return the index of the smallest number.
    """
    pos = bisect_left(myList, myNumber)
    if pos == 0:
        return 0
    if pos == len(myList):
        return len(myList)
    before = myList[pos - 1]
    after = myList[pos]
    if after - myNumber < myNumber - before:
       return pos
    else:
       return pos - 1

