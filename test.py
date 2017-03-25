import requests
import json

# I'm helping
apiKey = '6ef5c6d1654869455435f792cf9c0712'

url = 'http://api.reimaginebanking.com/customers?key={}'.format(apiKey)
payload = {
    'first_name': 'Peter',
    'last_name': 'Fedrizzi',
    'address': {
        'street_number': '619',
        'street_name': 'West Peter Street',
        'city': 'Peterville',
        'state': 'OH',
        'zip': '44106'
    }
}
# Create a Savings Account
response = requests.post( 
	url, 
	data=json.dumps(payload),
	headers={'content-type':'application/json'},
	)

if response.status_code == 201:
    print('customer created')
