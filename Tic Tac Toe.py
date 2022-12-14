# array um Feld des Spiels abzustecken

spielfeld = [[" ", " ", " "],
             [" ", " ", " "],
             [" ", " ", " "]]  # spielfeld 0 wäre hier erster Array


# array 0 = erste Zeile

def ausgabe(spielfeld: list[list[str]]):
    print("    A   B   C")
    print("--------------")
    print("1 | " + spielfeld[0][0] + " | " + spielfeld[0][1] + " | " + spielfeld[0][2])
    print("--------------")
    print("2 | " + spielfeld[1][0] + " | " + spielfeld[1][1] + " | " + spielfeld[1][2])
    print("--------------")
    print("3 | " + spielfeld[2][0] + " | " + spielfeld[2][1] + " | " + spielfeld[2][2])
    print("--------------")


# Alternativ für Formatierung; if (spielfeld [0][0] == "") dann print(" ")


def eingabeVerarbeiten(spielfeld: list[list[str]], spieler: str):
    koordinate = input("Gib Koordinate für Spieler " + spieler + " ein")
    if koordinate[0] == "A":
        spalte = 0
    elif koordinate[0] == "B":
        spalte = 1
    else:
        spalte = 2
    zeile = int(koordinate[1]) - 1
    spielfeld[zeile][spalte] = spieler


ausgabe(spielfeld)
eingabeVerarbeiten(spielfeld, "x")
ausgabe(spielfeld)
