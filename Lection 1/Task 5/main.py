import math
import cmath

fir = int(input("Enter walue a: "))
sec = int(input("Enter walue b: "))
thi = int(input("Enter walue c: "))

D = sec ** 2 - 4 * fir * thi

print("Discriminant = ", D)
if D > 0:
    xf = ((-sec + math.sqrt(D)) / (2 * fir))
    xs = ((-sec - math.sqrt(D)) / (2 * fir))
    print("x1 = ", xf,  "\nx2 = ", xs)
elif D == 0:
    xf = ((-sec) / (2 * fir))
    print("x1 = ", xf)
elif D < 0:
    xf = ((-sec + cmath.sqrt(D)) / (2 * fir))
    xs = ((-sec - cmath.sqrt(D)) / (2 * fir))
    print("x1 = ", xf,  "\nx2 = ", xs)