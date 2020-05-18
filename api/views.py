from django.shortcuts import render
from .serializers import ArticleSerializer
from rest_framework.generics import ListAPIView
from django.db.models import Q
from news.models import Article

# Create your views here.
class ArticlesListAPIView(ListAPIView):
    serializer_class = ArticleSerializer
    # paginator = 5

    def get_queryset(self):
        params = self.request.GET
        query = Q()
        if 'category_id' in params:
            query &= Q(category_id=params['category_id'])
        if 'publisher_id' in params:
            query &= Q(publisher_id=params['publisher_id'])
        
        return Article.objects.filter(query)            