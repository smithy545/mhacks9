import requests, json

apiKey = '6ef5c6d1654869455435f792cf9c0712'
baseUrl = 'http://api.reimaginebanking.com/'

def createCustomer(first_name, last_name, street_number, street_name, city, state, zip):
	payload = {
	    'first_name': first_name,
	    'last_name': last_name,
	    'address': {
	        'street_number': street_number,
	        'street_name': street_name,
	        'city': city,
	        'state': state,
	        'zip': zip
	    }
	}
	url = baseUrl + 'customers?key={}'.format(apiKey)
	response = requests.post( 
		url,
		data=json.dumps(payload),
		headers={'content-type':'application/json'},
	)
	return response.json()

def getCustomer(id):
	url = baseUrl + 'customers/{}?key={}'.format(id, apiKey)
	response = requests.get( 
		url, 
		headers={'accept':'application/json'},
	)
	return response.json()

