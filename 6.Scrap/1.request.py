import requests

url = 'htttps://www.example.com'

response = requests.get(url)

print(response.status_code)
print(response.text)