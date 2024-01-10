import requests
import os
import webbrowser as wb


url = "https://dimikoj.com/"

res = requests.get(url)

with open("dimik.html","w",encoding=res.encoding) as f:
    f.write(res.text)

file_path = os.path.realpath("dimik.html")
print(file_path)

wb.open("file://" + file_path)
wb.open(url)

# fp = open("test.text","w")
# fp.write("This was created using python")
#
# fp.close()