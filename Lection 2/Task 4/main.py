text = input("Entrr your text: ")
vowel = "AEIOUYaeiouy"
letter = []
for index in text:
    if index in vowel:
        letter.append(index)
print(letter)