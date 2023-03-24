# numpy dient als Bibliothek für große arrays + Matrizen und math. Operationen damit

import numpy as np
import matplotlib.pyplot as plt

# from GGT import ggt

# a = np.arange(15).reshape(3, 5)  # Tabelle in 3 Zeilen 5 Spalten ordnen

x = np.linspace(0, 2 * np.pi, 200)
y = np.sin(x)

fig, ax = plt.subplots()
ax.plot(x, y)
ax.plot(y, x)
plt.show()
