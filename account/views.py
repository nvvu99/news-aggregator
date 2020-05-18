from .models import User
from .forms import SignupForm, SigninForm, ResetPasswordForm, ChangePasswordForm
from django.views.generic.edit import FormView, CreateView
from django.views.generic.base import RedirectView
from django.views.generic import ListView, DetailView, TemplateView
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.db.models import Q
from django.contrib.auth import login, logout
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
class SigninView(FormView):
    template_name = 'signin.html'
    form_class = SigninForm
    success_url = reverse_lazy('index')

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect(self.success_url)
        return super().get(request, *args, **kwargs)

    def form_valid(self, form):
        user = form.get_user()
        login(self.request, user)
        self.init_session()
        return super().form_valid(form)

    def init_session(self):
        user = self.request.user
        following = [
            {
                'id': category.id,
                'name': category.name,
                'slug': category.slug,
            } for category in user.following.all()
        ]
        leftnav = {
            'nav': [
                {
                    'name': 'Mới nhất',
                    'url': reverse('index'),
                    'icon_class_name': 'fas fa-newspaper',
                },
                {
                    'name': 'Đã lưu',
                    'url': reverse('saved'),
                    'icon_class_name': 'fas fa-bookmark',
                },
                {
                    'name': 'Lịch sử',
                    'url': reverse('history'),
                    'icon_class_name': 'fas fa-history',
                },
            ],
            'following': following,
        }
        self.request.session['leftnav'] = leftnav
        if 'remember_me' not in self.request.POST:
            self.request.session.set_expiry(0)


class SignupView(CreateView):
    template_name = 'signup.html'
    form_class = SignupForm
    success_url = '/account/signin'

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect(self.success_url)
        return super().get(request, *args, **kwargs)


class SignoutView(LoginRequiredMixin, RedirectView):
    login_url = reverse_lazy('signin')

    url = '/account/signin'
    def get(self, request, *args, **kwargs):
        logout(request)
        return super().get(request, *args, **kwargs)


class ResetPasswordView(LoginRequiredMixin, FormView):
    login_url = reverse_lazy('signin')

    template_name = 'reset_password.html'
    form_class = ResetPasswordForm
    success_url = '/account/signin'


class ChangePasswordView(LoginRequiredMixin, FormView):
    login_url = reverse_lazy('signin')

    form_class = ChangePasswordForm
    success_url = reverse_lazy('password_change_done')
    template_name = 'change_password.html'
    
    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs


class AccountDetailView(LoginRequiredMixin, TemplateView):
    login_url = reverse_lazy('signin')
    template_name = 'account.html'


class BaseView(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('signin')

    context_object_name = 'articles'
    template_name = 'index.html'
    paginate_by = 25


class SavedArticleView(BaseView):
    def get_queryset(self):
        return self.request.user.saved_articles.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['feed_header'] = 'Đã lưu'
        return context


class HistoryView(BaseView):
    def get_queryset(self):
        return self.request.user.history.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['feed_header'] = 'Lịch sử'
        return context