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
