vowel = ["a","e","i","o", "u"]

word = input("please enter a word: ")

found= []

for i in word:
    if i in vowel:
        if i not in found:
            found.append(i)

print(found)

for i in found:
    print(i)