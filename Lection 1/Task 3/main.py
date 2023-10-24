perev = input("Enter what you want to convert to degrees Celsius or Fahrenheit? Enter C or F: ")
if perev == 'C' or perev == 'c':
    temp = int(input("Enter the temperature in Сelsius: "))
    print(temp * 9 / 5 + 32, "F")
elif perev == 'F' or perev == 'f':
    temp = int(input("Enter the temperature in Fahrenheit: "))
    print((temp -32) * 5 / 9, "C")
else:
    print("Enter another number")