from rest_framework import serializers
from sweden.models import Article


class ArticleSerializer(serializers.ModelSerializer):
	# To get the value for search article so we can have the right Slug...
	# Creates an extra field in the API Dashboard so we can grab the value.
	articleCatergoryApi = serializers.CharField(source='get_category_display')
	
	class Meta:
		model = Article
		fields = '__all__'
