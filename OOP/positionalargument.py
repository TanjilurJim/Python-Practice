def nameandprof(name, profession):
    return f"My name is {name} and I am a {profession}\n"

l = []

name = input("What is your name?: ")
l.append(name)
profession = input("What is your profession?: ")
l.append(profession)

r =nameandprof(*l)

with open("info.txt", 'a+') as f:
    f.write(r)
