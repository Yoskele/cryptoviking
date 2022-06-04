from rest_framework.response import Response

# Function Based view so we need to import Decorators.
from rest_framework.decorators import api_view

from sweden.models import Article
from .serializers import ArticleSerializer



@api_view(['GET'])
def getApiArticle(request):
	article = Article.objects.all().order_by('-created_at');
	serializer = ArticleSerializer(article, many=True)
	return Response(serializer.data)