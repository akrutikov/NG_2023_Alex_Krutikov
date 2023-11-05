element = input("enter any elements: ")
unique = []

for index in element:
    if index not in unique:
        unique.append(index)
print("Unique elements: ", unique)