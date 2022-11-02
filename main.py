# This is a sample Python script.

# Press Umschalt+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def calculate(input: int):
    if input == 0:
        return None
    return 100 / input


def print_hi(name: str):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Strg+F8 to toggle the breakpoint.
    return True


divider: int = 0
alter: float = 30
name: str = "0"
isNameEmpty: bool = not not divider

# Press the green button in the gutter to run the script.
if isNameEmpty:  # Bedignung
    print("Du hast einen Namen")  # Verzweigung
if alter <= 12:
    print("DU bist ein Kind")
elif alter > 18:  # elseif
    print("Du bist erwachsen")
else:
    print("Du bist ein Teenager")

# Schleifen:
while alter < 12:
    print("DU bist noch nicht alt genug, wie alt bist du wirklich?")
    alter = float(input("Dein Alter "))
    alter += 1  # Kurzschreibweise für inkrementelles Erhöhen (wie Alter=Alter+1)

# Felder/Arrays:
cars = ["Ford", "VW", "BMW"]  # fängt bei Index 0 an! bzw. mit -1 im Index geht er rückwärts durch Klammer
print(cars[-1])
cars.append("Lambo")  # hinzufügen am Ende des Arrays
cars.insert(1, "Ferrari")  # hinzufügen an bestimmter Stelle

# For Loop: #anders als C
for car in cars:  # für jedes Listenelement mache x
    print(car)
print(cars)

for i in range(1, 10, 2):  # range = Funktion #i ist durch "i in..." bereits definiert
    print(i)  # 1=Startwert, 10=Range, 2=Elemente/Steps pro Schritt

# Beispiel: Schleife summiert von 1-10 auf
sum: int = 0
for i in range(1, 11, 1):  # führt nur bis 10.Schritt aus
    print(i)
    sum = sum + i
    print(sum)
    prufen: int = 1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 10
    print(prufen)
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
