from django.shortcuts import render
from sweden.models import Token
# Create your views here.
def index(request):
	return render(request, 'index.html')

def Kryptovaluta(request):
	return render(request, 'statichtml/Kryptovaluta.html')

def kryptovalutaplanbok(request):
	return render(request, 'statichtml/kryptovalutaplanbok.html')


def Stablecoins(request):
	return render(request, 'statichtml/Stablecoins.html')


def token(request, slug):

	token = Token.objects.get(slug=slug)
	context = {
		'token' : token
	}
	return render(request, 'generichtml/token-page.html', context)