from django.urls import path, include
from .views import *
from django.contrib.auth.views import LoginView

urlpatterns = [
    path('', SigninView.as_view(), name='signin'),
    path('account/', UpdateUserInfoView.as_view(), name='account'),
    path('signin/', SigninView.as_view(), name='signin'),
    path('signup/', SignupView.as_view(), name='signup'),
    path('resetpassword/', ResetPasswordView.as_view(), name='reset_password'),
    path('changepassword/', ChangePasswordView.as_view(), name='change_password'),
    path('signout/', SignoutView.as_view(), name='signout'),
    path('saved/', SavedArticleView.as_view(), name='saved'),
    path('history/', HistoryView.as_view(), name='history'),
    path('addtopic/', AddTopicView.as_view(), name='add_topic'),
    path('organizetopic/', OrganizeTopicView.as_view(), name='organize_topic'),
    path('savearticle/', SaveArticle.as_view(), name='save_article'),
]
