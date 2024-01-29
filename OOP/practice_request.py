import requests

url = "https://tanjilurjdot.pythonanywhere.com/"

response = requests.get(url)

print(response.ok)

print(response.status_code)
print(response.reason)