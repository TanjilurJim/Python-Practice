from collections import Counter


text = '''Python is an easy programming language. Python syntax
is just like English. That is why it is less complicated than c or Java.
You can write the same task using fewer lines of code in python.'''

words = text.split()

count = Counter(words)

print(count)
print("Three most used words are", count.most_common(3))
