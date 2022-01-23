from django.shortcuts import render
from sweden.models import Token, Article
# Create your views here.

def articles(request):
	latest_news = Article.objects.all().order_by('-created_at')[:3]
	context = {
		'latest_news':latest_news,
	}
	return render(request, 'statichtml/articles.html', context)


def index(request):
	latest_news = Article.objects.all().order_by('-created_at')[:3]
	context = {
		'latest_news':latest_news,
	}
	return render(request, 'index.html', context)

def Kryptovaluta(request):
	return render(request, 'statichtml/Kryptovaluta.html')

def blockchain(request):
	return render(request, 'statichtml/Blockchain/blockchain.html')
def Kryptoloan(request):
	return render(request, 'statichtml/Kryptoloan.html')

def Kryptoearn(request):
	return render(request, 'statichtml/KryptoDefi/kryptoearn.html')

def kryptovalutaplanbok(request):
	return render(request, 'statichtml/kryptovalutaplanbok.html')

def Stablecoins(request):
	return render(request, 'statichtml/Stablecoins.html')

def NftBase(request):
	return render(request, 'statichtml/Nft/nftbase.html')

def CryptoExchange(request):
	return render(request, 'statichtml/Crypto-Exchange/Crypto-exchange.html')

def MetamaskGuide(request):
	return render(request, 'statichtml/wallets/Metamask-guide-page.html')

def token(request, slug):
	token = Token.objects.get(slug=slug)
	context = {
		'token' : token
	}
	return render(request, 'generichtml/token-page.html', context)

def article(request, slug):
	article = Article.objects.get(slug=slug)
	template = ''
	if(article.category == 'CEX'):
		template = 'generichtml/crypto-exchange-detail.html'
	elif(article.category == 'B'):
		template = 'generichtml/blockchain-article.html'
	elif(article.category == 'news'):
		template = 'generichtml/news-article.html'
	else:
		template = 'set-default-template-404'
	context = {
		'article':article,
	}
	return render(request, template, context)
