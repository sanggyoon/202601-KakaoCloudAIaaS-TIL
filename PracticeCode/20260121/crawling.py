import requests

url = 'https://www.google.com'
response = requests.get(url)

print(f"헤더 정보: {response.text}")