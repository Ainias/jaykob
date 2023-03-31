from clear import clear
import numpy as np


def ausgabe(gamefieldOut: np.ndarray):
    clear()
    for row in gamefieldOut:
        print("")
        for value in row:
            if value == 0:
                print("-", end="")  # end-Parameter: am Ende z.B. ein Leerzeichen dran
            if value == 1:
                print("X", end="")
