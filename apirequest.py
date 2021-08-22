import requests as rq

base_url = 'http://www.boredapi.com/api/activity/'

payload = {'participants': 1} # same as http://www.boredapi.com/api/activity?participants=1

request = rq.get(base_url, params=payload)
data = request.json()

print('Responce', data)
print('---')
print('Activity:', data['activity'])
print('Type', data['type'])
print('People:', data['participants'])
print('Price', data['price'])
print('Accessibility:', data['accessibility'])
