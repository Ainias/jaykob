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
