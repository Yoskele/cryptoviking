from django.shortcuts import render
from sweden.models import Token
# Create your views here.
def index(request):
	return render(request, 'index.html')

def Kryptovaluta(request):
	return render(request, 'statichtml/Kryptovaluta.html')

def Kryptoloan(request):
	return render(request, 'statichtml/Kryptoloan.html')

def Kryptoearn(request):
	return render(request, 'statichtml/KryptoDefi/kryptoearn.html')

def kryptovalutaplanbok(request):
	return render(request, 'statichtml/kryptovalutaplanbok.html')

def Stablecoins(request):
	return render(request, 'statichtml/Stablecoins.html')

def MetamaskGuide(request):
	return render(request, 'statichtml/wallets/Metamask-guide-page.html')

def token(request, slug):
	token = Token.objects.get(slug=slug)
	context = {
		'token' : token
	}
	return render(request, 'generichtml/token-page.html', context)