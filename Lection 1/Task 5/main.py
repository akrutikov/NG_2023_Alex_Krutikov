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

FirstAnswer = ((-b + cmath.sqrt(D)) / (2 * a))
SecondAnswer = ((-b - cmath.sqrt(D)) / (2 * a))
FirstAnswer = FirstAnswer.real
SecondAnswer = SecondAnswer.real
print("x1 = ", FirstAnswer,  "\nx2 = ", SecondAnswer)