from mpmath import sqrt, pi, mpf, mp

zap = int(input("Сколько нужно знаков после запятой?"))

mp.dps = zap + 10

a = mpf(input())
b = mpf(input())

def AGS(a, b, zap):
    while abs(a - b) > 10 ** (-zap):
        a, b = (a + b) / 2, (a * b) ** 0.5

    return (a + b) / 2


def MAGS(a, b, zap):
    z = 0
    while abs(a - b) > 10 ** (-zap):
        a, b, z = (a + b) / 2, z + sqrt((a - z) * (b - z)), z - sqrt((a - z) * (b - z))

    return (a + b) / 2


def calc_pi(zap):
    return AGS(sqrt(2), 1, zap) ** 2 / (MAGS(2, 1, zap) - 1)


def ellipse_perimeter(a, b, zap):
    return 2 * pi * MAGS(a ** 2, b ** 2, zap) / AGS(a, b, zap)


p = ellipse_perimeter(a, b, zap)

print(calc_pi(zap))
print(p)
