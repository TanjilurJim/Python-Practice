import requests

url = "https://github.com/TanjilurJim"

res = requests.get(url)

print(res.text)
