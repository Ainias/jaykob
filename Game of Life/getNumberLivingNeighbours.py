import numpy as np


def checkValue(value: int, max: int):
    if value >= 0 and value < max:
        return value
    elif value < 0:
        return max + value
    else:
        return value - max


def getNumberLivingNeighbours(gamefield: np.ndarray, y: int, x: int):  # y=Zeile, x=Spalte
    dimy = gamefield.shape[0]
    dimx = gamefield.shape[1]
    sum = 0
    sum += gamefield[checkValue(y - 1, dimy)][checkValue(x - 1, dimx)]
    sum += gamefield[checkValue(y - 1, dimy)][x]
    sum += gamefield[checkValue(y - 1, dimy)][checkValue(x + 1, dimx)]
    sum += gamefield[y][checkValue(x + 1, dimx)]
    sum += gamefield[checkValue(y + 1, dimy)][checkValue(x + 1, dimx)]
    sum += gamefield[checkValue(y + 1, dimy)][x]
    sum += gamefield[checkValue(y + 1, dimy)][checkValue(x - 1, dimx)]
    sum += gamefield[y][checkValue(x - 1, dimx)]
    return sum
