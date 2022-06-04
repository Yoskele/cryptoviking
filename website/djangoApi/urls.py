from django.urls import path
from djangoApi import views 

urlpatterns = [
	path('articles', views.getApiArticle),
]