# reads and writes image files and copies it

f = open("python1.jpg",'rb')
data = f.read()

cp = open('python2.jpg', 'wb')
cp.write(data)

f.close()
cp.close()

fr = open('python2.jpg','rb')
image = fr.read()
print(image)