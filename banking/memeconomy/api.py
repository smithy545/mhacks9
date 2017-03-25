import requests, json

apiKey = '6ef5c6d1654869455435f792cf9c0712'
baseUrl = 'http://api.reimaginebanking.com/'

def createCustomer(first_name, last_name, street_number, street_name, city, state, zipCode):
	payload = {
	    'first_name': first_name,
	    'last_name': last_name,
	    'address': {
	        'street_number': street_number,
	        'street_name': street_name,
	        'city': city,
	        'state': state,
	        'zip': zipCode
	    }
	}
	url = baseUrl + 'customers?key={}'.format(apiKey)
	response = requests.post( 
		url,
		data=json.dumps(payload),
		headers={'content-type':'application/json'},
	)
	if response.status_code == 201:
		return response.json()

def updateCustomer(customer_id, street_number, street_name, city, state, zipCode):
	payload = {
	    'address': {
	        'street_number': street_number,
	        'street_name': street_name,
	        'city': city,
	        'state': state,
	        'zip': zipCode
	    }
	}
	url = baseUrl + 'customers/{}?key={}'.format(customer_id, apiKey)
	response = requests.post( 
		url,
		data=json.dumps(payload),
		headers={'content-type':'application/json'},
	)
	if response.status_code == 202:
		return response.json()

def getCustomers():
	url = baseUrl + 'customers?key={}'.format(apiKey)
	response = requests.get( 
		url, 
		headers={'accept':'application/json'},
	)
	if response.status_code == 200:
		return response.json()

def getCustomer(customer_id):
	url = baseUrl + 'customers/{}?key={}'.format(customer_id, apiKey)
	response = requests.get( 
		url, 
		headers={'accept':'application/json'},
	)
	if response.status_code == 200:
		return response.json()

def getAccountCustomer(account_id):
	url = baseUrl + 'accounts/{}/customer?key={}'.format(account_id, apiKey)
	response = requests.get( 
		url, 
		headers={'accept':'application/json'},
	)
	if response.status_code == 200:
		return response.json()

def getBranch(branch_id):
	url = baseUrl + 'branches/{}?key={}'.format(branch_id, apiKey)
	response = requests.get( 
		url, 
		headers={'accept':'application/json'},
	)
	if response.status_code == 200:
		return response.json()

def getBranches():
	url = baseUrl + 'branches?key={}'.format(apiKey)
	response = requests.get( 
		url, 
		headers={'accept':'application/json'},
	)
	if response.status_code == 200:
		return response.json()

def getATM(atm_id):
	url = baseUrl + 'atms/{}?key={}'.format(atm_id, apiKey)
	response = requests.get( 
		url, 
		headers={'accept':'application/json'},
	)
	if response.status_code == 200:
		return response.json()

def getATMs(lat=None, lng=None, rad=None):
	url = baseUrl + 'atms?'
	if lat != None:
		url += 'lat={}&'.format(lat)
	if lng != None:
		url += 'lng={}&'.format(lng)
	if rad != None:
		url += 'rad={}&'.format(rad)
	url += 'key={}'.format(apiKey)
	response = requests.get( 
		url, 
		headers={'accept':'application/json'},
	)
	if response.status_code == 200:
		return response.json()

def getAccount(account_id):
	url = baseUrl + 'atms/{}?key={}'.format(account_id, apiKey)
	response = requests.get( 
		url, 
		headers={'accept':'application/json'},
	)
	if response.status_code == 200:
		return response.json()

def getAccounts(accountType=None):
	url = baseUrl + 'accounts?'
	if accountType != None:
		url += 'type={}&'
	url += 'key={}'.format(apiKey)
	response = requests.get( 
		url, 
		headers={'accept':'application/json'},
	)
	if response.status_code == 200:
		return response.json()

def getCustomerAccounts(customer_id):
	url = baseUrl + 'customers/{}/accounts?key={}'.format(customer_id, apiKey)
	response = requests.get( 
		url, 
		headers={'accept':'application/json'},
	)
	if response.status_code == 200:
		return response.json()

def createCustomerAccount(customer_id, type, nickname, rewards, balance, account_number=None):
	payload = {
	    'type': type,
	    'nickname': nickname,
	    'rewards': rewards,
	    'balance': balance,
	}
	if account_number != None:
		payload['account_number'] = account_number
	url = baseUrl + 'customers/{}/accounts?key={}'.format(customer_id, apiKey)
	response = requests.post( 
		url,
		data=json.dumps(payload),
		headers={'content-type':'application/json'},
	)
	if response.status_code == 201:
		return response.json()

def updateAccount(account_id, nickname, account_number=None):
	payload = {
	    'nickname': nickname
	}

	if account_number != None:
	    payload['account_number'] = account_number
	
	url = baseUrl + 'accounts/{}?key={}'.format(account_d, apiKey)
	response = requests.post( 
		url,
		data=json.dumps(payload),
		headers={'content-type':'application/json'},
	)
	if response.status_code == 202:
		return response.json()

def deleteAccount(account_id):
	url = baseUrl + 'accounts/{}?key={}'.format(account_d, apiKey)
	response = requests.delete( 
		url,
		headers={'accept':'application/json'},
	)
	if response.status_code == 204:
		return response.json()

def getAccountBill(account_id):
	url = baseUrl + 'accounts/{}/bills?key={}'.format(account_id, apiKey)
	response = requests.get( 
		url, 
		headers={'accept':'application/json'},
	)
	if response.status_code == 200:
		return response.json()

def getBill(bill_id):
	url = baseUrl + 'bills/{}?key={}'.format(bill_id, apiKey)
	response = requests.get( 
		url, 
		headers={'accept':'application/json'},
	)
	if response.status_code == 200:
		return response.json()

def getCustomerBills(customer_id):
	url = baseUrl + 'customers/{}/bills?key={}'.format(customer_id, apiKey)
	response = requests.get( 
		url, 
		headers={'accept':'application/json'},
	)
	if response.status_code == 200:
		return response.json()

def createAccountBill(account_id, status, payee, payment_amount, nickname=None, payment_date=None, recurring_date=None):
	payload = {
	    'status': status,
	    'payee': payee,
	    'payment_amount': payment_amount,
	}
	if nickname != None:
		payload['nickname'] = nickname
	if payment_date != None:
		payload['payment_date'] = payment_date
	if recurring_date != None:
		payload['recurring_date'] = recurring_date
	url = baseUrl + 'accounts/{}/bills?key={}'.format(account_id, apiKey)
	response = requests.post( 
		url,
		data=json.dumps(payload),
		headers={'content-type':'application/json'},
	)
	if response.status_code == 201:
		return response.json()

def updateAccountBill(bill_id, status=None, payee=None, payment_amount=None, nickname=None, payment_date=None, recurring_date=None):
	payload = {}
	if nickname != None:
		payload['nickname'] = nickname
	if payment_date != None:
		payload['payment_date'] = payment_date
	if recurring_date != None:
		payload['recurring_date'] = recurring_date
	if status != None:
		payload['status'] = status
	if payee != None:
		payload['payee'] = payee
	if payment_amount != None:
		payload['payment_amount'] = payment_amount
	url = baseUrl + 'bills/{}?key={}'.format(bill_id, apiKey)
	response = requests.put( 
		url,
		data=json.dumps(payload),
		headers={'content-type':'application/json'},
	)
	if response.status_code == 202:
		return response.json()

def deleteBill(bill_id):
	url = baseUrl + 'bills/{}?key={}'.format(bill_id, apiKey)
	response = requests.delete( 
		url, 
		headers={'accept':'application/json'},
	)
	if response.status_code == 204:
		return response.json()

def getAccountDeposits(account_id):
	url = baseUrl + 'accounts/{}/deposits?key={}'.format(account_id, apiKey)
	response = requests.get(
		url,
		headers={'accept':'application/json'}
		)
	if response.status_code == 200:
		return response.json()

def getDeposit(deposit_id):
	url = baseUrl + 'deposits/{}?key={}'.format(deposit_id, apiKey)
	response = requests.get(
		url,
		headers={'accept':'application/json'}
		)
	if response.status_code == 200:
		return response.json()

def createDeposit(account_id, medium, amount, transaction_date=None, description=None):
	payload = {
		'medium': medium,
		'amount':amount
	}
	if transaction_date != None:
		payload['transaction_date'] = transaction_date
	if description != None:
		payload['description'] = description

	url = baseUrl + 'accounts/{}/deposits?key={}'.format(account_id, apiKey)
	response = requests.post(
		url,
		headers={'content-type':'application/json'}
		)
	if response.status_code == 201:
		return response.json()

def updateDeposit(deposit_id, medium=None, amount=None, description=None):
	payload = {}
	if medium != None:
		payload['medium'] = medium
	if amount != None:
		payload['amount'] = amount
	if description != None:
		payload['description'] = description

	url = baseUrl + 'accounts/{}/deposits?key={}'.format(account_id, apiKey)
	response = requests.put(
		url,
		headers={'content-type':'application/json'}
		)
	if response.status_code == 202:
		return response.json()

def deleteDeposit(deposit_id):
	url = baseUrl + 'deposits/{}?key={}'.format(deposit_id, apiKey)
	response = requests.delete(
		url,
		headers={'accept':'application/json'}
		)
	if response.status_code == 204:
		return response.json()

def getAccountLoans(account_id):
	url = baseUrl + 'accounts/{}/loans?key={}'.format(account_id, apiKey)
	response = requests.get(
		url,
		headers={'accept':'application/json'}
		)
	if response.status_code == 200:
		return response.json()

def getLoan(loan_id):
	url = baseUrl + 'loans/{}?key={}'.format(loan_id, apiKey)
	response = requests.get(
		url,
		headers={'accept':'application/json'}
		)
	if response.status_code == 200:
		return response.json()

def deleteLoan(load_id):
	url = baseUrl + 'loans/{}?key={}'.format(loan_id, apiKey)
	response = requests.delete(
		url,
		headers={'accept':'application/json'}
		)
	if response.status_code == 204:
		return response.json()

def createAccountLoan(account_id, loanType, status, credit_score, monthly_payment, amount, description=None):
	payload = {
		'type': loanType,
		'status': status,
		'credit_score': credit_score,
		'monthly_payment': monthly_payment,
		'amount': amount
	}
	if description != None:
		payload['description'] = description

	url = baseUrl + 'accounts/{}/loans?key={}'.format(account_id, apiKey)
	response = requests.post(
		url,
		data=json.dumps(payload),
		headers={'content-type':'application/json'}
		)
	if response.status_code == 201:
		return response.json()

def updateLoan(loan_id, loanType=None, status=None, credit_score=None, monthly_payment=None, amount=None, description=None):
	payload = {}
	if description != None:
		payload['description'] = description
	if loanType != None:
		payload['type'] = loanType
	if status != None:
		payload['status'] = status
	if credit_score != None:
		payload['credit_score'] = credit_score
	if monthly_payment != None:
		payload['monthly_payment'] = monthly_payment
	if amount != None:
		payload['amount'] = amount
	if description != None:
		payload['description'] = description

	url = baseUrl + 'loans/{}?key={}'.format(loan_id, apiKey)
	response = requests.put(
		url,
		data=json.dumps(payload),
		headers={'content-type':'application/json'}
		)
	if response.status_code == 202:
		return response.json()

def getMerchant(merchant_id):
	url = baseUrl + 'merchants/{}?key={}'.format(merchant_id, apiKey)
	response = requests.get( 
		url, 
		headers={'accept':'application/json'},
	)
	if response.status_code == 200:
		return response.json()

def getMerchants(lat=None, lng=None, rad=None):
	url = baseUrl + 'merchants?'
	if lat != None:
		url += 'lat={}&'.format(lat)
	if lng != None:
		url += 'lng={}&'.format(lng)
	if rad != None:
		url += 'rad={}&'.format(rad)
	url += 'key={}'.format(apiKey)
	response = requests.get( 
		url, 
		headers={'accept':'application/json'},
	)
	if response.status_code == 200:
		return response.json()

def createMerchant(name, categories, street_name=None, street_number=None, city=None, state=None, zipCode=None, lat=None, lng=None):
	payload = {
		'name': name,
		'category': categories
	}
	if street_number != None and street_name != None and city != None and state != None and zipCode != None:
		payload['address'] = {
			'street_number': street_number,
			'street_name': street_name,
			'city': city,
			'state': state,
			'zip': zipCode,
		}
	if lat != None and lng != None:
		payload['geocode'] = {
			'lat': lat,
			'lng': lng
		}
	url = baseUrl + 'merchants?key={}'.format(apiKey)
	response = requests.post(
		url,
		data=json.dumps(payload),
		headers={'content-type':'application/json'}
		)
	if response.status_code == 201:
		return response.json()

def updateLoan(merchant_id, name=None, categories=None, street_name=None, street_number=None, city=None, state=None, zipCode=None, lat=None, lng=None):
	payload = {}
	if name != None:
		payload['name'] = name
	if categories != None:
		payload['category'] = categories
	if street_number != None and street_name != None and city != None and state != None and zipCode != None:
		payload['address'] = {
			'street_number': street_number,
			'street_name': street_name,
			'city': city,
			'state': state,
			'zip': zipCode,
		}
	if lat != None and lng != None:
		payload['geocode'] = {
			'lat': lat,
			'lng': lng
		}

	url = baseUrl + 'merchants/{}?key={}'.format(merchant_id, apiKey)
	response = requests.put(
		url,
		data=json.dumps(payload),
		headers={'content-type':'application/json'}
		)
	if response.status_code == 202:
		return response.json()

def getAccountPurchases(account_id):
	url = baseUrl + 'accounts/{}/purchases?key={}'.format(account_id, apiKey)
	response = requests.get(
		url,
		headers={'accept':'application/json'}
		)
	if response.status_code == 200:
		return response.json()

def getAccountMerchantPurchases(account_id, merchant_id):
	url = baseUrl + 'merchants/{}/accounts/{}/purchases?key={}'.format(merchant_id, account_id, apiKey)
	response = requests.get(
		url,
		headers={'accept':'application/json'}
		)
	if response.status_code == 200:
		return response.json()

def getMerchantPurchases(merchant_id):
	url = baseUrl + 'merchants/{}/purchases?key={}'.format(merchant_id, apiKey)
	response = requests.get(
		url,
		headers={'accept':'application/json'}
		)
	if response.status_code == 200:
		return response.json()

def getPurchase(purchase_id):
	url = baseUrl + 'purchases/{}?key={}'.format(purchase_id, apiKey)
	response = requests.get(
		url,
		headers={'accept':'application/json'}
		)
	if response.status_code == 200:
		return response.json()

def createAccountPurchase(account_id, merchant_id, medium, amount, purchase_date=None, description=None):
	payload = {
		'merchant_id': merchant_id,
		'medium': medium,
		'amount': amount
	}
	if purchase_date != None:
		payload['purchase_date'] = purchase_date
	if description != None:
		payload['description'] = description
	url = baseUrl + 'accounts/{}/purchases?key={}'.format(account_id, apiKey)
	response = requests.get(
		url,
		data=json.dumps(payload),
		headers={'content-type':'application/json'}
		)
	if response.status_code == 201:
		return response.json()

def updatePurchase(purchase_id, account_id=None, medium=None, amount=None, description=None):
	payload = {}
	if account_id != None:
		payload['payer_id'] = account_id
	if description != None:
		payload['description'] = description
	if medium != None:
		payload['medium'] = medium
	if amount != None:
		payload['amount'] = amount
	url = baseUrl + 'purchases/{}?key={}'.format(purchase_id, apiKey)
	response = requests.put(
		url,
		data=json.dumps(payload),
		headers={'content-type':'application/json'}
		)
	if response.status_code == 202:
		return response.json()

def deletePurchase(purchase_id):
	url = baseUrl + 'purchases/{}?key={}'.format(purchase_id, apiKey)
	response = requests.delete(
		url,
		headers={'accept':'application/json'}
		)
	if response.status_code == 204:
		return response.json()

def getAccountTransfers(account_id, transferType=None):
	url = baseUrl + 'accounts/{}?'.format(account_id)
	if transferType != None:
		url += 'type={}&'.format(transferType)
	url += 'key={}'.format(apiKey)
	response = requests.get(
		url,
		headers={'accept':'application/json'}
		)
	if response.status_code == 200:
		return response.json()

def getTransfer(transfer_id):
	url = baseUrl + 'transfers/{}?key={}'.format(transfer_id, apiKey)
	response = requests.get(
		url,
		headers={'accept':'application/json'}
		)
	if response.status_code == 200:
		return response.json()

def createTransfer(account_id, medium, payee_id, amount, transaction_date=None, description=None):
	payload = {
		'medium': medium,
		'payee_id': payee_id,
		'amount': amount
	}
	if transaction_date != None:
		payload['transaction_date'] = transaction_date
	if description != None:
		payload['description'] = description

	url = baseUrl + 'accounts/{}/transfers?key={}'.format(account_id, apiKey)
	response = requests.post(
		url,
		data=json.dumps(payload),
		headers={'content-type':'application/json'}
		)
	if response.status_code == 201:
		return response.json()

def updateTransfer(transfer_id, medium=None, payee_id=None, amount=None, description=None):
	payload = {}
	if medium != None:
		payload['medium'] = medium
	if payee_id != None:
		payload['payee_id'] = payee_id
	if amount != None:
		payload['amount'] = amount
	if description != None:
		payload['description'] = description

	url = baseUrl + 'transfers/{}?key={}'.format(transfer_id, apiKey)
	response = requests.put(
		url,
		data=json.dumps(payload),
		headers={'content-type':'application/json'}
		)
	if response.status_code == 202:
		return response.json()

def deleteTransfer(transfer_id):
	url = baseUrl + 'transfers/{}?key={}'.format(transfer_id, apiKey)
	response = requests.delete(
		url,
		headers={'accept':'application/json'}
		)
	if response.status_code == 204:
		return response.json()

def getAccountWithdrawals(account_id):
	url = baseUrl + 'accounts/{}/withdrawals?key={}'.format(account_id, apiKey)
	response = requests.get(
		url,
		headers={'accept':'application/json'}
		)
	if response.status_code == 200:
		return response.json()

def getWithdrawal(withdrawal_id):
	url = baseUrl + 'withdrawals/{}?key={}'.format(withdrawal_id, apiKey)
	response = requests.get(
		url,
		headers={'accept':'application/json'}
		)
	if response.status_code == 200:
		return response.json()

def createWithdrawal(account_id, medium, amount, transaction_date=None, description=None):
	payload = {
		'medium': medium,
		'amount': amount
	}
	if transaction_date != None:
		payload['transaction_date'] = transaction_date
	if description != None:
		payload['description'] = description

	url = baseUrl + 'accounts/{}/withdrawals?key={}'.format(account_id, apiKey)
	response = requests.post(
		url,
		data=json.dumps(payload),
		headers={'content-type':'application/json'}
		)
	if response.status_code == 201:
		return response.json()

def updateWithdrawal(withdrawal_id, medium=None, amount=None, description=None):
	payload = {}
	if medium != None:
		payload['medium'] = medium
	if amount != None:
		payload['amount'] = amount
	if description != None:
		payload['description'] = description

	url = baseUrl + 'withdrawals/{}?key={}'.format(withdrawal_id, apiKey)
	response = requests.put(
		url,
		data=json.dumps(payload),
		headers={'content-type':'application/json'}
		)
	if response.status_code == 202:
		return response.json()

def deleteWithdrawal(withdrawal_id):
	url = baseUrl + 'withdrawals/{}?key={}'.format(withdrawal_id, apiKey)
	response = requests.delete(
		url,
		headers={'accept':'application/json'}
		)
	if response.status_code == 204:
		return response.json()

def getEnterpriseAccounts():
	url = baseUrl + 'enterprise/accounts?key={}'.format(apiKey)
	response = requests.get(
		url,
		headers={'accept':'application/json'}
		)
	if response.status_code == 200:
		return response.json()

def getEnterpriseAccount(account_id):
	url = baseUrl + 'enterprise/accounts/{}?key={}'.format(account_id, apiKey)
	response = requests.get(
		url,
		headers={'accept':'application/json'}
		)
	if response.status_code == 200:
		return response.json()

def getEnterpriseBills():
	url = baseUrl + 'enterprise/bills?key={}'.format(apiKey)
	response = requests.get(
		url,
		headers={'accept':'application/json'}
		)
	if response.status_code == 200:
		return response.json()

def getEnterpriseBill(bill_id):
	url = baseUrl + 'enterprise/bills/{}?key={}'.format(bill_id, apiKey)
	response = requests.get(
		url,
		headers={'accept':'application/json'}
		)
	if response.status_code == 200:
		return response.json()

def getEnterpriseCustomers():
	url = baseUrl + 'enterprise/customers?key={}'.format(apiKey)
	response = requests.get(
		url,
		headers={'accept':'application/json'}
		)
	if response.status_code == 200:
		return response.json()

def getEnterpriseCustomer(customer_id):
	url = baseUrl + 'enterprise/customers/{}?key={}'.format(customer_id, apiKey)
	response = requests.get(
		url,
		headers={'accept':'application/json'}
		)
	if response.status_code == 200:
		return response.json()

def getEnterpriseDeposits():
	url = baseUrl + 'enterprise/deposits?key={}'.format(apiKey)
	response = requests.get(
		url,
		headers={'accept':'application/json'}
		)
	if response.status_code == 200:
		return response.json()

def getEnterpriseDeposit(deposit_id):
	url = baseUrl + 'enterprise/deposits/{}?key={}'.format(deposit_id, apiKey)
	response = requests.get(
		url,
		headers={'accept':'application/json'}
		)
	if response.status_code == 200:
		return response.json()

def getEnterpriseMerchants():
	url = baseUrl + 'enterprise/merchants?key={}'.format(apiKey)
	response = requests.get(
		url,
		headers={'accept':'application/json'}
		)
	if response.status_code == 200:
		return response.json()

def getEnterpriseMerchant(merchant_id):
	url = baseUrl + 'enterprise/merchants/{}?key={}'.format(merchant_id, apiKey)
	response = requests.get(
		url,
		headers={'accept':'application/json'}
		)
	if response.status_code == 200:
		return response.json()

def getEnterpriseTransfers():
	url = baseUrl + 'enterprise/transfers?key={}'.format(apiKey)
	response = requests.get(
		url,
		headers={'accept':'application/json'}
		)
	if response.status_code == 200:
		return response.json()

def getEnterpriseTransfer(transfer_id):
	url = baseUrl + 'enterprise/transfers/{}?key={}'.format(tansfer_id, apiKey)
	response = requests.get(
		url,
		headers={'accept':'application/json'}
		)
	if response.status_code == 200:
		return response.json()

def getEnterpriseWithdrawals():
	url = baseUrl + 'enterprise/withdrawals?key={}'.format(apiKey)
	response = requests.get(
		url,
		headers={'accept':'application/json'}
		)
	if response.status_code == 200:
		return response.json()

def getEnterpriseWithdrawal(withdrawal_id):
	url = baseUrl + 'enterprise/withdrawal/{}?key={}'.format(withdrawal_id, apiKey)
	response = requests.get(
		url,
		headers={'accept':'application/json'}
		)
	if response.status_code == 200:
		return response.json()


