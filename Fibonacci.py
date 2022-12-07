# für i=0/i=1 f(i)= 1, i>=2 f(i)=f(i-1)+f(i-2)
n: int = 5

n = int(input("Bitte Fibonacci Zahl angeben n="))
fiboLetzt: int = 1
fiboVorletzt: int = 1
endWert: int
for i in range(1, n, 1):  # n wird nicht nochmal durchgegangen (exklusiv)
    endWert = fiboLetzt + fiboVorletzt
    fiboVorletzt = fiboLetzt
    fiboLetzt = endWert
    print(endWert)

    # für i=0 f(i)=0/i=1 f(i)= 1, i>=2 f(i)=f(i-1)+f(i-2)

result = {
    0: 0,
    1: 1
}


def fibo(zahl: int):
    if zahl not in result:  # Überprüfung ob key im Dictionary ist
        # return result[zahl]  # mit if zahl in result muss das hier noch stehen --> hole dir die Zahl direkt aus dem Dictionary
        #  if zahl == 0 or zahl == 1:  # immer komplette Bedingung hinschreiben - also hier 2* 'zahl =='
        # return zahl
        result[zahl] = fibo(zahl - 1) + fibo(zahl - 2)
    return result[zahl]


print(fibo(112))

# Dictionaries für Laufzeitverkürzung
# x = {"key" : "value"} bzw. Befehl für neue Einträge: x["newKey"] = "value"
