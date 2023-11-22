num = int(input("Enter your value: "))
count = 1
PrimeNum = []

while count <=  num:
    index = 1
    text = ""
    
    while index <= count:
        if count % index == 0:
            text += str(index) + " "
        index += 1
    if count % 2 != 0 and count % 3 != 0:
        PrimeNum.append(count)
        
    print(count, "|", text)
    count += 1
print("Prime numbers: ", PrimeNum)
        