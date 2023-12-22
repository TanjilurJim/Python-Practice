food = ['pizza','burger','nuggets','pasta']

letter = input("please enter a letter : ")

for i in food:
    if i.startswith(letter):
        print(i)

