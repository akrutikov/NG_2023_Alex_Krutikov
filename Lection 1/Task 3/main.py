perev = input("Enter what you want to convert to degrees Celsius or Fahrenheit? Enter C or F: ")
temp = float(input("Enter the temperature: "))
if perev == 'C' or perev == 'c':
    print(temp * 9 / 5 + 32, "F")
elif perev == 'F' or perev == 'f':
    print((temp -32) * 5 / 9, "C")
else:
    print("Enter C (Celsius) or F (Fahrenheit)")