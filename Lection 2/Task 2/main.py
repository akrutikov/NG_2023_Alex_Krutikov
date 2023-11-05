element = input("Enter any elements: ")
values = []
counter = 0

for index in element:
        if index.isdigit() == True:
            values.append(index)
            counter += 1
            
print("=" * 30)            
print("Your numbers: ", values)
print("Number of digits entered: ", counter)