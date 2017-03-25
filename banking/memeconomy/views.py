from django.shortcuts import render

# Create your views here.
def index(request):
	return render(request, 'memeconomy/index.html', {})

def profile(request):
	return render(request, 'memeconomy/profile.html', {})