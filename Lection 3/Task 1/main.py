name = input("Enter file name: ")
count ={}
with open(name) as file:
    for symbol in file.read():
        count[symbol] = count.get(symbol, 0) + 1
print (count)