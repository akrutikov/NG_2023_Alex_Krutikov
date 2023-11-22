element = input("Enter any elements: ")
number = "1234567890"
values = []
counter = 0

for index in element:
    if index in number:
        values.append(index)
        counter += 1
            
print("=" * 30)            
print("Your numbers: ", values)
print("Number of digits entered: ", counter)