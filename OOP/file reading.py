file_handler = open("MyData.txt" ,'r')
str1 = file_handler.read()
print(str1)
print(type(str1))

file_handler.close()

# modes : r to read
# w to write
# a to append after last saved lines
# r+ to read and write
# w+ to write and read
# a+ to append and read
# z to open the file in exclusive creation mode
