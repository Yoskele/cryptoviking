from django.contrib import admin
from django.urls import path, include
from .import views
# from django.views.generic import TemplateView
app_name = 'sweden'

urlpatterns = [
	path('', views.index, name='index'),
	path('Kryptovaluta', views.Kryptovaluta, name="Kryptovaluta"),
	path('Exchange-Vs-HardwareWallet', views.ExchangeVsHardwareWallet, name="ExchangeVsHardwareWallet"),
	path('Stablecoins', views.Stablecoins, name="Stablecoins"),
	# path('robots.txt', TemplateView.as_view(template_name="robots.txt", content_type='text/plain')),

]