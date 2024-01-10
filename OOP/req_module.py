import requests
import os
import webbrowser as wb


# url = "https://dimikoj.com/"
#
# res = requests.get(url)
#
# with open("dimik.html","w",encoding=res.encoding) as f:
#     f.write(res.text)
#
# file_path = os.path.realpath("dimik.html")
# print(file_path)
#
# wb.open("file://" + file_path)
# wb.open(url)

# fp = open("test.text","w")
# fp.write("This was created using python")
#
# fp.close()

# for downloading image

img_url = "https://2.bp.blogspot.com/-zED0hpjBOKU/WSrodhLjLMI/AAAAAAAACpk/3Gv5YyxHsjErYphNfzFd37uEmxsBC0XtwCK4B/s1600/Screen%2BShot%2B2017-05-23%2Bat%2B10.48.44%2BPM.png"
r = requests.get(img_url)

with open("pybook.png", "wb") as f:
    f.write(r.content)

fr = open("pybook.png","rb")
show_image = fr.read()
print(show_image)