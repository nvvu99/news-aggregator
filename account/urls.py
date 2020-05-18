from django.urls import path, include
from .views import *
from django.contrib.auth.views import LoginView

urlpatterns = [
    path('', AccountDetailView.as_view(), name='account'),
    path('signin/', SigninView.as_view(), name='signin'),
    path('signup/', SignupView.as_view(), name='signup'),
    path('resetpassword/', ResetPasswordView.as_view(), name='reset_password'),
    path('changepassword/', ChangePasswordView.as_view(), name='change_password'),
    path('signout/', SignoutView.as_view(), name='signout'),
    path('saved/', SavedArticleView.as_view(), name='saved'),
    path('history/', HistoryView.as_view(), name='history'),
]