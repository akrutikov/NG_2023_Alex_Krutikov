text = input("Entrr your text: ").lower()
vowel = "aeiouy"
letter = []
for index in text:
    if index in vowel:
        letter.append(index)
print(letter)