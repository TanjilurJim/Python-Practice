import requests

url = "https://github.com/TanjilurJim"

res = requests.get(url)

print(res.text)

# fp = open("test.text","w")
# fp.write("This was created using python")
#
# fp.close()