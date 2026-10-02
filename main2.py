import requests

url = "https://www.randomnumberapi.com/api/v1.0/random?min=1&max=100&count=1"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    print("Random Number:", data[0])
else:
    print("Failed to get number.")