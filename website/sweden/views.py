from django.shortcuts import render
from sweden.models import Token, Article
# Import Pagination to make a list with pages 1.2.3 
from django.core.paginator import Paginator

#impor Telegram bot
import telegram
from django.core.serializers.json import DjangoJSONEncoder
from django.core.serializers import serialize
# from ipware.ip import get_ip
from django.conf import settings

import asyncio
from telegram import Bot



URL=settings.BOT_URL
my_token = settings.BOT_TOKEN
my_chat_id = settings.BOT_CHAT_ID

class LazyEncoder(DjangoJSONEncoder):
    def default(self, obj):
        if isinstance(obj.dict):
            return str(obj)
        return super().default(obj)

def bot(request, msg, chat_id=my_chat_id, token=my_token):
    bot = telegram.Bot(token=token)
    asyncio.run(bot.sendMessage(chat_id=chat_id, text=msg))

def get_vk(request):
	print('Hello')
	req_headers = request.META
	x_forwarded_for_value = req_headers.get('HTTP_X_FORWARDED_FOR')
	if x_forwarded_for_value:
		ip_addr = x_forwarded_for_value.split(',')[-1].strip()
		print('if ip_addr ', ip_addr)
	else:
		ip_addr = req_headers.get('REMOTE_ADDR')
		print('else ip_addr ', ip_addr)
	return ip_addr


def crypto_list(request):
	msg = 'Crpto List page', get_vk(request)
	bot(request,msg)
	article_container = Article.objects.all().order_by('-created_at')[:3]
	context = {
		'article_container' : article_container
	}
	return render(request, 'statichtml/Crypto-list/crypto-list.html', context)

def articles(request):
	# latest_news = Article.objects.all().order_by('-created_at')[:4]
	# Set up Pagination
	paginator = Paginator(Article.objects.all().order_by('-created_at'), 4)
	# Get page number
	page = request.GET.get('sida')
	# Track page number ?page=2
	news = paginator.get_page(page)
	# nums = "a" * news.paginator.num_pages
	crypto_exchanges = Article.objects.all().filter(category='CEX').order_by('-created_at')[:4]
	context = {
		# 'latest_news':latest_news,
		'news':news,
		# 'nums':nums,
		'crypto_exchanges':crypto_exchanges,
	}
	return render(request, 'statichtml/articles.html', context)

def index(request):
	msg = 'Home page', get_vk(request)
	bot(request,msg)
	latest_news = Article.objects.all().order_by('-created_at')[:3]
	newsOne = Article.objects.order_by('-created_at')[0]
	newsSecond = Article.objects.order_by('-created_at')[1]
	newsThird = Article.objects.order_by('-created_at')[2]
	context = {
		'latest_news':latest_news,
		'newsOne':newsOne,
		'newsSecond':newsSecond,
		'newsThird':newsThird,

	}
	return render(request, 'index.html', context)

def Kryptovaluta(request):
	msg = 'Kryptovaluta page', get_vk(request)
	bot(request,msg)
	article_container = Article.objects.all().order_by('-created_at')[:3]
	context = {
		'article_container' : article_container
	}
	return render(request, 'statichtml/Kryptovaluta.html', context)

def blockchain(request):
	msg = 'blockchain page', get_vk(request)
	bot(request,msg)
	article_container = Article.objects.all().order_by('-created_at')[:3]
	context = {
		'article_container' : article_container
	}
	return render(request, 'statichtml/Blockchain/blockchain.html', context)
def Kryptoloan(request):
	msg = 'Crypto Loan page', get_vk(request)
	bot(request,msg)
	article_container = Article.objects.all().order_by('-created_at')[:3]
	context = {
		'article_container' : article_container
	}
	return render(request, 'statichtml/Kryptoloan.html', context)

def Kryptoearn(request):
	msg = 'Staking page', get_vk(request)
	bot(request,msg)
	article_container = Article.objects.all().order_by('-created_at')[:3]
	context = {
		'article_container' : article_container
	}
	return render(request, 'statichtml/KryptoDefi/kryptoearn.html', context)

def kryptovalutaplanbok(request):
	msg = 'crypto Wallet page', get_vk(request)
	bot(request,msg)
	article_container = Article.objects.all().order_by('-created_at')[:3]
	context = {
		'article_container' : article_container
	}
	return render(request, 'statichtml/kryptovalutaplanbok.html', context)

def Stablecoins(request):
	msg = 'Stablecoin page', get_vk(request)
	bot(request,msg)
	article_container = Article.objects.all().order_by('-created_at')[:3]
	context = {
		'article_container' : article_container
	}
	return render(request, 'statichtml/Stablecoins.html', context)

def NftBase(request):
	msg = 'NFt page', get_vk(request)
	bot(request,msg)
	article_container = Article.objects.all().order_by('-created_at')[:3]
	context = {
		'article_container' : article_container
	}
	return render(request, 'statichtml/Nft/nftbase.html', context)

def CryptoExchange(request):
	msg = 'Crypto Exchange page', get_vk(request)
	bot(request,msg)
	article_container = Article.objects.all().order_by('-created_at')[:3]
	context = {
		'article_container' : article_container
	}
	return render(request, 'statichtml/Crypto-Exchange/Crypto-exchange.html', context)

def MetamaskGuide(request):
	msg = 'Metamask page', get_vk(request)
	bot(request,msg)
	article_container = Article.objects.all().order_by('-created_at')[:3]
	context = {
		'article_container' : article_container
	}
	return render(request, 'statichtml/wallets/Metamask-guide-page.html', context)

def token(request, slug):
	msg = 'Token page', get_vk(request)
	bot(request,msg)
	token = Token.objects.get(slug=slug)
	article_container = Article.objects.all().order_by('-created_at')[:3]
	context = {
		'token' : token,
		'article_container':article_container,
	}
	return render(request, 'generichtml/token-page.html', context)

def article(request, slug):
	msg = 'Article page', get_vk(request)
	bot(request,msg)
	article = Article.objects.get(slug=slug)
	template = ''
	if(article.category == 'CEX'):
		template = 'generichtml/crypto-exchange-detail.html'
	elif(article.category == 'B'):
		template = 'generichtml/blockchain-article.html'
	elif(article.category == 'news'):
		template = 'generichtml/news-article.html'
	elif(article.category == 'wallet'):
		template = 'generichtml/crypto-wallet.html'
	elif(article.category == 'G'):
		template = 'generichtml/guest-post.html'
	else:
		template = 'set-default-template-404'
	# Filter out the news the user already read.
	all_news = Article.objects.all().order_by('-created_at')[:4]
	article_container = []
	for news in all_news:
		if slug != news.slug:
			article_container.append(news)
		if len(article_container) >= 4: # Make sure we are only displaying 3 articles.
			article_container.pop(-1) # Deleting last object from the list.

	context = {
		'article':article,
		'article_container':article_container,
	}
	return render(request, template, context)


def cookie(request):
	msg = 'cookie page', get_vk(request)
	bot(request,msg)
	article_container = Article.objects.all().order_by('-created_at')[:3]
	context = {
		'article_container' : article_container
	}
	return render(request, 'statichtml/Cookie-page.html', context)