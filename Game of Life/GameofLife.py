# Any live cell with fewer than two live neighbours dies, as if by underpopulation.
# Any live cell with two or three live neighbours lives on to the next generation.
# Any live cell with more than three live neighbours dies, as if by overpopulation.
# Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.
import numpy
# 1. Numpy Array 200x200 mit 0 = tote Zelle, 1 = lebende Zelle
import numpy as np
import numpy.typing as npt  # für den Typing Typ von NumPy
import time
from ausgabe import ausgabe
from berechnung import berechnung

fps = 12
dimy = 10
dimx = 100
gamefield = np.around(np.random.rand(dimy, dimx))
# gamefield[3][2] = 1
# gamefield[3][3] = 1
# gamefield[3][4] = 1

# gamefield[1][1] = 1

ausgabe(gamefield)

# for i in range(0, 10, 1):
while 1 == 1:
    time.sleep(1 / fps)
    gamefield = berechnung(gamefield)
    # gamefield = np.random.rand(dimy, dimx)
    # gamefield = np.around(gamefield)  # Runden der random Zahlen
    ausgabe(gamefield)
