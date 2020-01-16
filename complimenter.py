import requests
request_url = 'https://complimentr.com/api'
response = requests.get(request_url)
print(response.json()['compliment'])