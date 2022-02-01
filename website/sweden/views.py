from django.shortcuts import render
from sweden.models import Token, Article
# Create your views here.

def articles(request):
	latest_news = Article.objects.all().order_by('-created_at')[:4]
	crypto_exchanges = Article.objects.all().filter(category='CEX').order_by('-created_at')[:4]
	context = {
		'latest_news':latest_news,
		'crypto_exchanges':crypto_exchanges,
	}
	return render(request, 'statichtml/articles.html', context)


def index(request):
	latest_news = Article.objects.all().order_by('-created_at')[:3]
	context = {
		'latest_news':latest_news,
	}
	return render(request, 'index.html', context)

def Kryptovaluta(request):
	article_container = Article.objects.all().order_by('-created_at')[:3]
	context = {
		'article_container' : article_container
	}
	return render(request, 'statichtml/Kryptovaluta.html', context)

def blockchain(request):
	article_container = Article.objects.all().order_by('-created_at')[:3]
	context = {
		'article_container' : article_container
	}
	return render(request, 'statichtml/Blockchain/blockchain.html', context)
def Kryptoloan(request):
	article_container = Article.objects.all().order_by('-created_at')[:3]
	context = {
		'article_container' : article_container
	}
	return render(request, 'statichtml/Kryptoloan.html', context)

def Kryptoearn(request):
	article_container = Article.objects.all().order_by('-created_at')[:3]
	context = {
		'article_container' : article_container
	}
	return render(request, 'statichtml/KryptoDefi/kryptoearn.html', context)

def kryptovalutaplanbok(request):
	article_container = Article.objects.all().order_by('-created_at')[:3]
	context = {
		'article_container' : article_container
	}
	return render(request, 'statichtml/kryptovalutaplanbok.html', context)

def Stablecoins(request):
	article_container = Article.objects.all().order_by('-created_at')[:3]
	context = {
		'article_container' : article_container
	}
	return render(request, 'statichtml/Stablecoins.html', context)

def NftBase(request):
	article_container = Article.objects.all().order_by('-created_at')[:3]
	context = {
		'article_container' : article_container
	}
	return render(request, 'statichtml/Nft/nftbase.html', context)

def CryptoExchange(request):
	article_container = Article.objects.all().order_by('-created_at')[:3]
	context = {
		'article_container' : article_container
	}
	return render(request, 'statichtml/Crypto-Exchange/Crypto-exchange.html', context)

def MetamaskGuide(request):
	article_container = Article.objects.all().order_by('-created_at')[:3]
	context = {
		'article_container' : article_container
	}
	return render(request, 'statichtml/wallets/Metamask-guide-page.html', context)

def token(request, slug):
	token = Token.objects.get(slug=slug)
	article_container = Article.objects.all().order_by('-created_at')[:3]
	context = {
		'token' : token,
		'article_container':article_container,
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
	# Filter out the news the user already read.
	all_news = Article.objects.all().order_by('-created_at')[:4]
	article_container = []
	for news in all_news:
		if slug != news.slug:
			article_container.append(news)

	context = {
		'article':article,
		'article_container':article_container,
	}
	return render(request, template, context)
