import math

def fulfillment(operation, a, b):
    match operation:
        case "+":
            print(a + b)
        case "-":
            print(a - b)
        case "*":
            print(a * b)
        case "/":
            print(a / b)
        case "degree":
            print(a ** b)
        case "root":
            print(math.sqrt(a))

opera = input("What operation do you want to do?  +, -, *. /, root, degree?: ")
fir = int(input("Enter first walue: "))
sec = int(input("Enter second walue: "))
fulfillment(opera, fir, sec)