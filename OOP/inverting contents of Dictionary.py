def invert(d):


    new={v:k for k,v in d.items()}





    return new

dict = {}

for i in range(2):
    i= int(input("index"))
    v = input("value")
    dict[i] = v

# print(dict)

print(invert(dict))