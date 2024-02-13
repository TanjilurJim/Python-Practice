# import Student, pickle
#
# with open('students.data','rb') as f:
#
#     for i in range(3):
#         s = pickle.load(f)
#         s.display()

# with open("file.txt",'r') as f:
#     lines = f.readlines()
#     print(lines)
#     for line in lines:
#
#         print(line)

for i in range(5):
    with open('file.txt','a+') as f:
        f.write(f'this is {i} th line \n')


with open('file.txt','r+') as f:
    content = f.read()
    print(content)

