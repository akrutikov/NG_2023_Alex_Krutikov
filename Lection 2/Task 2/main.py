element = input("Enter any elements: ").split(" ")
values = []
counter = 0

for index in element:
    if index.isdigit():
        values.append(index)
        counter += 1
            
print("The numbers that you wrote: ", values, "\nNumber of digits entered: ", counter)