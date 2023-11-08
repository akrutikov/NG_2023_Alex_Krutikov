num = int(input("Enter your value: "))
count = 1
PrimeNum = []

while count <=  num:
    i = 1
    text = ""
    
    while i <= count:
        if count % i == 0:
            text += str(i) + " "
        i += 1
    if count % 2 != 0 and count % 3 != 0:
        PrimeNum.append(count)
        
    print(count, "|", text)
    count += 1
print("Prime numbers: ", PrimeNum)
        