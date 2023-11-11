text = input("Entrr your text: ")
vowel = "AEIOUYaeiouy"
letter = []
for i in text:
    if i in vowel:
        letter.append(i)
print(letter)