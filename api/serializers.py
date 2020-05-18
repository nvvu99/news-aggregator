from rest_framework import serializers
from news.models import Article, Category, Publisher


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ('id', 'title', 'thumb', 'slug', 'original_url', 'sapo', 'category', 'publisher', )
        depth = 1