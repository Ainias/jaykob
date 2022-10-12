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
if isNameEmpty:
    print("Du hast einen Namen")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
