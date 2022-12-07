# Größter Gemeinsamer Teiler mit Modulo %
zahl1 = int(input("Zahl 1 angeben ="))  # strg + D für Zeilen kopieren
zahl2 = int(input("Zahl 2 angeben ="))
rest: int = 1
while rest > 0:
    rest = zahl1 % zahl2
    zahl1 = zahl2
    zahl2 = rest
print(zahl1)


# nächstes Mal: Funktionen + Eingabeüberprüfung

def ggt(zahl1: int, zahl2: int):
    #  return ggt(zahl2, zahl1 % zahl2) if (zahl2 > 0) else zahl1
    if zahl2 > 0:
        return ggt(zahl2, zahl1 % zahl2)
    return zahl1


# kurze if Schreibweise: "a" if "Bedingung" else "b"
print(ggt(5, 2))
