from .models import User
from news.models import Category, Article
from .forms import *
from django.views import View
from django.views.generic.edit import FormView, CreateView, UpdateView
from django.views.generic.base import RedirectView
from django.views.generic import ListView, DetailView, TemplateView
from django.urls import reverse_lazy
from django.db.models import Q
from django.contrib.auth import login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseNotAllowed
from django.shortcuts import redirect

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
        if 'remember_me' not in self.request.POST:
            self.request.session.set_expiry(0)
        else:
            self.request.session.set_expiry(3600 * 24 * 15) # 15 days


class SignupView(SuccessMessageMixin, CreateView):
    template_name = 'signup.html'
    form_class = SignupForm
    success_url = reverse_lazy('signin')
    success_message = 'Đăng ký thành công. Vui lòng đăng nhập.'

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect(self.success_url)
        return super().get(request, *args, **kwargs)


class SignoutView(LoginRequiredMixin, RedirectView):
    login_url = reverse_lazy('signin')

    url = reverse_lazy('signin')
    def get(self, request, *args, **kwargs):
        logout(request)
        return super().get(request, *args, **kwargs)


class ResetPasswordView(LoginRequiredMixin, FormView):
    login_url = reverse_lazy('signin')

    template_name = 'reset_password.html'
    form_class = ResetPasswordForm
    success_url = '/account/signin'


class ChangePasswordView(LoginRequiredMixin, SuccessMessageMixin, FormView):
    login_url = reverse_lazy('signin')

    form_class = ChangePasswordForm
    success_url = reverse_lazy('change_password')
    template_name = 'change_password.html'
    success_message = 'Thay đổi mật khẩu thành công. Vui lòng đăng nhập lại.'
    
    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs


class UpdateUserInfoView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    login_url = reverse_lazy('signin')
    template_name = 'account.html'
    form_class = UpdateUserInfoForm
    success_url = reverse_lazy('account')
    success_message = "Thay đổi thông tin thành công"

    def get_object(self):
        return self.request.user
    
    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs


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
        context['selected_leftnav_item'] = 'saved-article'
        context['feed_header'] = 'Tin đã lưu'
        return context


class HistoryView(BaseView):
    def get_queryset(self):
        return self.request.user.history.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['selected_leftnav_item'] = 'history'
        context['feed_header'] = 'Tin đã xem'
        return context


class OrganizeTopicView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = User
    template_name = 'organize_topic.html'
    form_class = OrganizeTopicForm
    success_url = reverse_lazy('organize_topic')
    success_message = 'Thay đổi thành công'

    def get_object(self, queryset=None):
        return self.request.user

    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super().get_form_kwargs(*args, **kwargs)
        kwargs['user'] = self.request.user
        return kwargs


class AddTopicView(OrganizeTopicView):
    template_name = 'add_topic.html'
    form_class = AddTopicForm
    success_url = reverse_lazy('add_topic')


class SaveArticle(LoginRequiredMixin, View):
    login_url = reverse_lazy('signin')

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