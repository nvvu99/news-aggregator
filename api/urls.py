from django.urls import path
from .views import ArticlesListAPIView


urlpatterns = [
    path('feeds/', ArticlesListAPIView.as_view(), name='feeds-api'),
]