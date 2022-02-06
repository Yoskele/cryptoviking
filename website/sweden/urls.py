from django.contrib import admin
from django.urls import path, include
from .import views
# from django.views.generic import TemplateView
app_name = 'sweden'

urlpatterns = [
	path('', views.index, name='index'),
	path('Kryptovaluta', views.Kryptovaluta, name="Kryptovaluta"),
	path('blockchain', views.blockchain, name="blockchain"),
	path('Stablecoins', views.Stablecoins, name="Stablecoins"),
	path('non-fungible-token', views.NftBase, name="NftBase"),
	path('kryptolan', views.Kryptoloan, name="Kryptoloan"),
	path('tjana-krypto', views.Kryptoearn, name="Kryptoearn"),
	path('kryptovalutaplanbok', views.kryptovalutaplanbok, name="kryptovalutaplanbok"),
	path('metamask-guide', views.MetamaskGuide, name="MetamaskGuide"),
	path('crypto-exchange', views.CryptoExchange, name="CryptoExchange"),
	path('handla/<slug>', views.token, name='token'),
	# Articles Paths but all leads to the same view function.
	path('artiklar', views.articles, name="all-articles"),
	path('nyheter/<slug>', views.article, name="nyheter"),
	path('blockchain/<slug>', views.article, name="blockchain-article"),
	path('crypto-wallet/<slug>', views.article, name="crypto-wallet-article"),
	path('centralized-crypto-exchange/<slug>', views.article, name="centralized-crypto-exchange"),

	# path('robots.txt', TemplateView.as_view(template_name="robots.txt", content_type='text/plain')),

]

