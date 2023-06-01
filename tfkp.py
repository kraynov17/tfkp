from mpmath import sqrt, pi, mpf, mp, factorial
import time

zap = int(input("Какая точность: "))
start = time.time()
start2 = time.time()

mp.dps = zap + 10
a = mpf(input("Введите a: "))
b = mpf(input("Введите b: "))

if a < b:
    a, b= b, a

def agm(a, b, zap):
    while abs(a - b) > 10 ** (-zap):
        a, b = (a + b) / 2, (a * b) ** 0.5
    return (a + b) / 2


def magm(a, b, zap):
    z = 0
    while abs(a - b) > 10 ** (-zap):
        a, b, z = (a + b) / 2, z + sqrt((a - z) * (b - z)), z - sqrt((a - z) * (b - z))
    return (a + b) / 2

otvet = 2 * pi * magm(a ** 2, b ** 2, zap) / agm(a, b, zap)
end = time.time()
time1 =  (end-start) * 10**3 #мс

def doublefactorial(n):
    if n <= 0:
        return 1
    else:
        return n * doublefactorial(n - 2)
def dfactorial(x):
    a=1
    if n%2==0:
        y = 2
        while y <= n:
            a = a* y
            y = y + 2
        return a
    else:
        y = 3
        while y <= n:
            a = a* y
            y = y + 2
        return a
print("Школьная формула:        ", 2*pi*((a**2+b**2)/2)**0.5)
print("Формула Рамануджана:     ", pi*(3*(a+b)-sqrt((3*a+b)*(a+3*b))))
print("2-ая формула Рамануджана:", pi*(a+b)*(1+(3*((a-b)/(a+b))**2)/(10+sqrt(4-3*((a-b)/(a+b))**2))))
print("Формула с АГС и МАГС:    ", otvet)
n = 1
s = 0
l = 0
k = 0
while abs(l-otvet) > 0.001:
    s += (dfactorial(2*n-1))/((2*n-1)*2**n*factorial(n))*((a-b)/(b+a))**n
    s = s**2
    l = pi*(a+b)*(1+s)
    n += 1
    if n>1000:
        print("Формула Д. Айвори медленнее")
        k = 1
        break
end2 = time.time()
time2 =  (end2-start2) * 10**3 #мс
if k == 0:
    print("Формула Д. Айвори:       ", l)
    if time1 > time2:
        print("Формула Д. Айвори быстрее ", "(", time1, ", ", time2, " (мс))", sep="")
    else:
        print("Формула Д. Айвори медленнее ", "(", time1, " (мс), ", time2, " (мс))", sep="")
