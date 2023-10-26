import cmath

def line():
    print("="*14)
    
print("b^2 - 4 * a * c")
line()
a = int(input("Enter walue a: "))
b = int(input("Enter walue b: "))
c = int(input("Enter walue c: "))
line()
D = b ** 2 - 4 * a * c
print ("Discriminant = ", D)

xf = ((-b + cmath.sqrt(D)) / (2 * a))
xs = ((-b - cmath.sqrt(D)) / (2 * a))
xf = xf.real
xs = xs.real
print("x1 = ", xf,  "\nx2 = ", xs)