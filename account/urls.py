from django.urls import path, include
from .views import *
from django.contrib.auth.views import LoginView

urlpatterns = [
    path('my/', UserUpdateView.as_view(), name='profile'),
    path('password-change/', PasswordChangeView.as_view(), name='password_change'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('saved/', SavedArticleView.as_view(), name='saved'),
    path('history/', HistoryView.as_view(), name='history'),
    path('topic-add/', TopicAddView.as_view(), name='topic_add'),
    path('topic-organize/', TopicOrganizeView.as_view(), name='topic_organize'),
    path('article-save/', SaveArticle.as_view(), name='article_save'),
]
