from django.shortcuts import render, redirect
from .models import Article, Category, Publisher
from account.models import User
from django.views.generic import ListView
from django.views.generic.base import RedirectView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.utils.translation import gettext, gettext_lazy as _
from django.urls import reverse_lazy


class PublisherView(ListView):
    model = Publisher
    context_object_name = 'publishers'


class CategoryListView(ListView):
    model = Category
    context_object_name = 'categories'


class BaseView(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')

    model = Article
    paginate_by = 25
    template_name = 'index.html'
    context_object_name = 'articles'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        page_obj = context.get('page_obj')
        page_number = page_obj.number
        min_page_range = max(1, page_number-2)
        max_page_range = min(min_page_range+4, page_obj.paginator.num_pages)
        page_range = range(min_page_range, max_page_range+1)
        context['page_range'] = page_range
        return context


class IndexView(BaseView):
    extra_context = {
        'title': _('Tin mới nhất'),
        'selected_leftnav_item': _('newest'),
    }

    def get_queryset(self):
        following = self.request.user.following.all()
        query = Q()
        for category in following:
            query |= Q(category_id=category.pk)
        return super().get_queryset().filter(query)


class ArticleByCategoryView(BaseView):
    def get_queryset(self):
        self.selected_category = Category.objects.get(
            slug=self.kwargs.get('slug'))
        return Article.objects.filter(category=self.selected_category)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['selected_leftnav_item'] = 'category-{}'.format(
            self.selected_category.pk)
        context['title'] = self.selected_category.name

        return context


class ArticleByPublisherView(BaseView):
    def get_queryset(self):
        self.selected_publisher = Publisher.objects.get(
            slug=self.kwargs.get('slug'))
        return Article.objects.filter(publisher=self.selected_publisher)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['selected_leftnav_item'] = 'publisher-{}'.format(
            self.selected_publisher.name)
        context['title'] = self.selected_publisher.name
        return context


class ArticleDetailView(RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        article = Article.objects.get(slug=self.kwargs['slug'])
        user = self.request.user
        if user is not None:
            user.history.remove(article)
            user.history.add(article)
        return article.original_url


class SearchArticlesView(BaseView):
    extra_context = {
        'title': _('Tìm kiếm')
    }

    def get(self, request, *args, **kwargs):
        self.search_articles_query = Q(pk=-1)
        if request.GET.get('q') is not None:
            query_params = request.GET.get('q').split()
            search_articles_query_by_title = Q()
            search_articles_query_by_sapo = Q()

            for param in query_params:
                search_articles_query_by_title &= Q(
                    title__icontains=param)
                search_articles_query_by_sapo &= Q(sapo__icontains=param)

            self.search_articles_query = search_articles_query_by_sapo | search_articles_query_by_title
        return super().get(request, *args, **kwargs)

    def get_queryset(self):
        return super().get_queryset().filter(self.search_articles_query)


class TestView(ListView):
    template_name = 'test.html'
