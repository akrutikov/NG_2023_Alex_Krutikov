name = input("Enter file name: ")
count ={}
with open(name) as f:
    for symbol in f.read():
        count[symbol] = count.get(symbol, 0) + 1
print (count)