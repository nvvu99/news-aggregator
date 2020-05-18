from django.urls import path
from .views import *

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('base', BaseView.as_view(), name='base'),
    path('test', TestView.as_view(), name='test'),
    path('article/<slug:slug>', ArticleDetailView.as_view(), name='single-article'),
    path('category/<slug:slug>', ArticleByCategoryView.as_view(), name='category-articles'),
    path('publisher/<slug:slug>', ArticleByPublisherView.as_view(), name='publisher-articles'),
    # path('contact', contact, name='contact'),
    # path('about', about, name='about'),
]