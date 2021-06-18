from django.shortcuts import render

# Create your views here.
def index(request):
	return render(request, 'index.html')

def Kryptovaluta(request):
	return render(request, 'statichtml/Kryptovaluta.html')

def ExchangeVsHardwareWallet(request):
	return render(request, 'statichtml/Exchange-vs-HardwareWallet.html')


def Stablecoins(request):
	return render(request, 'statichtml/Stablecoins.html')