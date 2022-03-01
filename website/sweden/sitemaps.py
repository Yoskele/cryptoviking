from django.contrib.sitemaps import Sitemap 
from django.urls import reverse

# Import the models so we can get the urls.
from .models import Article
# Go to Base urls.py and import the Sitemap.
class StaticViewSitemap(Sitemap):
	priority = 0.5
	changefreq = 'weekly'
	protocol = 'https'

	def items(self):
		return ['sweden:index','sweden:Kryptovaluta']   

	def location(self, item):
		return reverse(item)


class ArticleSitemap(Sitemap):
	changefreq = 'daily'
	priority = 1
	protocol = "https"
	def items(self):
		return Article.objects.all()

	def location(self, item):
		if(item.category == 'CEX'):
			return reverse('sweden:centralized-crypto-exchange', args=[item.slug])
		if(item.category == 'B'):
			return reverse('sweden:blockchain-article', args=[item.slug])
		if(item.category == 'wallet'):
			return reverse('sweden:crypto-wallet-article', args=[item.slug])
		if(item.category == 'news'):
			return reverse('sweden:nyheter', args=[item.slug])
		# if(item.category == 'guest-post'):
		# 	return reverse('sweden:guest-post', args=[item.slug])
		

		