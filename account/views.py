from .models import User
from news.models import Category, Article
from news.views import BaseView
from .forms import *

from django.views import View
from django.views.generic.edit import FormView, CreateView, UpdateView
from django.views.generic.base import RedirectView
from django.views.generic import ListView, DetailView, TemplateView

from django.contrib.auth import login, logout, views as auth_views
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin

from django.http import HttpResponse, HttpResponseNotFound, HttpResponseNotAllowed
from django.shortcuts import redirect
from django.utils.translation import gettext, gettext_lazy as _
from django.urls import reverse_lazy
from django.db.models import Q


class LoginView(FormView):
    template_name = 'login.html'
    form_class = LoginForm
    success_url = reverse_lazy('index')
    extra_context = {
        'title': _('Đăng nhập')
    }

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
        if 'remember_me' not in self.request.POST:
            self.request.session.set_expiry(0)
        else:
            self.request.session.set_expiry(3600 * 24 * 15)  # 15 days


class RegisterView(SuccessMessageMixin, CreateView):
    template_name = 'register.html'
    form_class = RegisterForm
    success_url = reverse_lazy('login')
    success_message = 'Đăng ký thành công. Vui lòng đăng nhập.'
    extra_context = {
        'title': _('Đăng ký')
    }

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect(self.success_url)
        return super().get(request, *args, **kwargs)


class LogoutView(LoginRequiredMixin, RedirectView):
    login_url = reverse_lazy('login')
    url = reverse_lazy('login')

    def get(self, request, *args, **kwargs):
        logout(request)
        return super().get(request, *args, **kwargs)


class PasswordResetView(auth_views.PasswordResetView):
    email_template_name = 'password_reset_email.html'
    subject_template_name = 'password_reset_subject.txt'
    template_name = 'password_reset.html'
    title = _('Khôi phục mật khẩu')


class PasswordResetDoneView(auth_views.PasswordResetDoneView):
    template_name = 'password_reset_done.html'
    title = _('Đã gửi yêu cầu')


class PasswordResetConfirmView(auth_views.PasswordResetConfirmView):
    form_class = SetPasswordForm
    template_name = 'password_reset_confirm.html'
    title = _('Nhập mật khẩu mới')


class PasswordResetCompleteView(auth_views.PasswordResetCompleteView):
    template_name = 'password_reset_complete.html'
    title = _('Đặt lại mật khẩu thành công')


class PasswordChangeView(LoginRequiredMixin, SuccessMessageMixin, FormView):
    login_url = reverse_lazy('login')

    form_class = PasswordChangeForm
    success_url = reverse_lazy('password_change')
    template_name = 'password_change.html'
    success_message = 'Thay đổi mật khẩu thành công. Vui lòng đăng nhập lại.'
    extra_context = {
        'title': _('Thay đổi mật khẩu')
    }

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs


class UserUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    login_url = reverse_lazy('login')
    template_name = 'account.html'
    form_class = UserUpdateForm
    success_url = reverse_lazy('account')
    success_message = "Thay đổi thông tin thành công"
    extra_context = {
        'title': _('Thay đổi thông tin')
    }

    def get_object(self):
        return self.request.user

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs


class SavedArticleView(BaseView):
    extra_context = {
        'title': _('Tin đã lưu'),
        'selected_leftnav_item': 'saved-article',
    }

    def get_queryset(self):
        return self.request.user.saved_articles.all()


class HistoryView(BaseView):
    extra_context = {
        'title': _('Tin đã lưu'),
        'selected_leftnav_item': 'saved-article',
    }
    title = _('Tin đã xem')

    def get_queryset(self):
        return self.request.user.hửstory.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['selected_leftnav_item'] = 'history'
        return context


class TopicOrganizeView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = User
    template_name = 'topic_organize.html'
    form_class = TopicOrganizeForm
    success_url = reverse_lazy('topic_organize')
    success_message = 'Thay đổi thành công'
    extra_context = {
        'title': _('Quản lý chủ đề'),
    }

    def get_object(self, queryset=None):
        return self.request.user

    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super().get_form_kwargs(*args, **kwargs)
        kwargs['user'] = self.request.user
        return kwargs


class TopicAddView(TopicOrganizeView):
    template_name = 'topic_add.html'
    form_class = TopicAddForm
    success_url = reverse_lazy('topic_add')
    extra_context = {
        'title': _('Thêm chủ đề'),
    }


class SaveArticle(LoginRequiredMixin, View):
    login_url = reverse_lazy('login')

    def post(self, request, *args, **kwargs):
        return HttpResponseNotAllowed(['POST'], content='Not allowed!')

    def get(self, request, *args, **kwargs):
        if 'article_id' in request.GET:
            article_id = request.GET['article_id']
            try:
                article = Article.objects.get(pk=article_id)
            except Article.DoesNotExist:
                return HttpResponseNotFound('Article does not exist!')
            else:
                user = request.user
                if (article not in user.saved_articles.all()):
                    user.saved_articles.add(article)
                    return HttpResponse('Save successfully!', status=201)
                else:
                    user.saved_articles.remove(article)
                    return HttpResponse('Unsave successfully!')
        return super().post(request, *args, **kwargs)
