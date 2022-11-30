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


def fibo(zahl: int):
    if zahl == 0 or zahl == 1:  # immer komplette Bedingung hinschreiben - also hier 2* 'zahl =='
        return zahl
    return fibo(zahl - 1) + fibo(zahl - 2)


print(fibo(6))
