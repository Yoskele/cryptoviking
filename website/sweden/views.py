from django.shortcuts import render

# Create your views here.
def index(request):
	return render(request, 'index.html')

def Kryptovaluta(request):
	return render(request, 'static/Kryptovaluta.html')

def ExchangeVsHardwareWallet(request):
	return render(request, 'static/Exchange-vs-HardwareWallet.html')


def Stablecoins(request):
	return render(request, 'static/Stablecoins.html')