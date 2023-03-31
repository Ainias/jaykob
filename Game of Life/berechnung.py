# Any live cell with fewer than two live neighbours dies, as if by underpopulation.
# Any live cell with two or three live neighbours lives on to the next generation.
# Any live cell with more than three live neighbours dies, as if by overpopulation.
# Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.

import numpy as np
from getNumberLivingNeighbours import getNumberLivingNeighbours

ruleStayLiving = (2, 3)  # 2 oder 3 Nachbarn = lebendig bleiben
ruleGetBorn = (3,)  # 3 Nachbarn = lebendig werden


def berechnung(gamefield: np.ndarray):
    newGamefield = np.copy(gamefield)
    for y in range(0, gamefield.shape[0]):
        for x in range(0, gamefield.shape[1]):
            numNeighbours = getNumberLivingNeighbours(gamefield, y,
                                                      x)  # holen uns hier die Anzahl der lebenden Nachbarn
            if gamefield[y][x] == 0:
                if numNeighbours in ruleGetBorn:
                    newGamefield[y][x] = 1
            else:
                if numNeighbours not in ruleStayLiving:
                    newGamefield[y][x] = 0
    return newGamefield
