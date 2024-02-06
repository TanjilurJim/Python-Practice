def nameandprof(name, profession):
    print(f"My name is {name} and I am a {profession}")

l = []

name = input("What is your name?: ")
l.append(name)
profession = input("What is your profession?: ")
l.append(profession)

nameandprof(*l)

with open("info.txt", 'w+') as f:
    f.write(f"My name is {l[0]} and I am a {l[1]}")
