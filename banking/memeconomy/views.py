from django.shortcuts import render, redirect
from . import api
from .forms import *
from .models import *

# Create your views here.
def index(request):
	return render(request, 'memeconomy/index.html', {})

def profile(request):
	if request.user.id == None:
		return render(request, 'memeconomy/index.html', {'error': 'Please login.'})
	
	trader = Trader.get(user=request.user.id)
	if trader == None:
		form = CustomerForm()
		return render(request, 'memeconomy/profile.html', {'form':form})


	if request.method == 'POST':	
		form = CustomerForm(request.POST)
		if form.is_valid():
			# TODO: do some input validation
			resp = api.createMerchant(form.cleaned_data["memepage"], form.cleaned_data["categories"].split(','))
			if resp != None:
				return redirect('http://localhost:8000/memeconomy/'+str(resp["objectCreated"]["_id"])+'/view')
			return render(request, 'memeconomy/index.html', {'error': 'Error creating meme'})

			trader = Trader.get(user=request.user.id)
			if trader == None:
				customer = createCustomer(first_name, last_name, street_number, street_name, city, state, zipCode)["objectCreated"]
				account = createCustomerAccount(customer_id, type, nickname, rewards, balance, account_number=None)["objectCreated"]

				customer = api.createCustomer()
				account_id = api.getCustomerAccounts(customer_id)
				trader = Trader()
				trader.save()


	form = CustomerForm()


	return render(request, 'memeconomy/profile.html', {'form':form})

def create(request):
	if request.user.id == None:
		return render(request, 'memeconomy/index.html', {'error': 'Please login.'})

	if request.method == 'POST':	
		form = MemeForm(request.POST)
		if form.is_valid():
			# TODO: do some input validation
			resp = api.createMerchant(form.cleaned_data["memepage"], form.cleaned_data["categories"].split(','))
			if resp != None:
				return redirect('http://localhost:8000/memeconomy/'+str(resp["objectCreated"]["_id"])+'/view')
			return render(request, 'memeconomy/index.html', {'error': 'Error creating meme'})

	form = MemeForm()
	return render(request, 'memeconomy/makememe.html', {'form':form})

def buy(request, meme_id):
	if request.user.id == None:
		return render(request, 'memeconomy/index.html', {'error': 'Please login.'})

	return redirect('view', meme_id)

def sell(request, meme_id):
	if request.user.id == None:
		return render(request, 'memeconomy/index.html', {'error': 'Please login.'})

	return redirect('view', meme_id)

def view(request, meme_id):
	if request.user.id == None:
		return render(request, 'memeconomy/index.html', {'error': 'Please login.'})

	merchant = api.getMerchant(meme_id)
	if merchant == None:
		return render(request, 'memeconomy/index.html', {'error': 'No such meme.'})

	purchases = api.getMerchantPurchases(meme_id)
	if purchases == None:
		return render(request, 'memeconomy/index.html', {'error': 'Could not retrieve meme history.'})

	return render(request, 'memeconomy/meme.html', {'merchant': merchant, 'purchases': purchases})

