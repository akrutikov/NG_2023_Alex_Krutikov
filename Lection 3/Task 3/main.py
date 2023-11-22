import json

keyname = input("Enter key name: ")
fname = input("Enter file name: ")

with open(fname, "r") as file:
    json_f = json.load(file)
    for search in json_f:
        if keyname in json_f[search]:
            print(json_f[search][keyname])
        else:
            print("Not find")