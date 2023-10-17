s1 = input("please enter a string")
s2 = input("please enter another string")

if len(s1) != len(s2):
    print("not an anagram")
else:
    for i in s1:
        if i not in s2:
            print("not an anagram")
            break
        else:
            print(f"{s1} and {s2} are anagram")
            break;



