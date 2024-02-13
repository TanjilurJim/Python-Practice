import sys

print(sys.argv)
print(type(sys.argv))

arguments = sys.argv

# Convert arguments to integers before adding
a = int(arguments[1])
b = int(arguments[2])
print(a+b)
