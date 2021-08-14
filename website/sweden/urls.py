from django.contrib import admin
from django.urls import path, include
from .import views
# from django.views.generic import TemplateView
app_name = 'sweden'

urlpatterns = [
	path('', views.index, name='index'),
	path('Kryptovaluta', views.Kryptovaluta, name="Kryptovaluta"),
	path('Stablecoins', views.Stablecoins, name="Stablecoins"),
	path('kryptolan', views.Kryptoloan, name="Kryptoloan"),
	path('kryptovalutaplanbok', views.kryptovalutaplanbok, name="kryptovalutaplanbok"),
	path('metamask-guide', views.MetamaskGuide, name="MetamaskGuide"),
	path('handla/<slug>', views.token, name='token'),
	# path('robots.txt', TemplateView.as_view(template_name="robots.txt", content_type='text/plain')),

]

