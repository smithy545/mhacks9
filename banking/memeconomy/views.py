from django.shortcuts import render, redirect
from . import api
from .forms import MemeForm

# Create your views here.
def index(request):
	return render(request, 'memeconomy/index.html', {})

def profile(request):
	return render(request, 'memeconomy/profile.html', {})

def create(request):
	if request.method == 'POST':	

		return render(request, 'memeconomy/meme.html', context)
	return render(request, 'memeconomy/makememe.html', {})

def buy(request, meme_id):

	return redirect(view, meme_id)

def sell(request, meme_id):

	return redirect(view, meme_id)

def view(request, meme_id):
	merchant = api.getMerchant(meme_id)
	if merchant == None:
		return render(request, 'memeconomy/index.html', {'error': 'No such meme.'})

	# do stuff with merchant here

	return render(request, 'memeconomy/meme.html', context)
