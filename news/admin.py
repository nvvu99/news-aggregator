from django.contrib import admin
from .models import Article, Category, Publisher


# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    fields = (
        'name',
        )
    list_display = (
        'id', 
        'name',
        'slug',
        )
    search_fields = (
        'name', 
        )


class ArticleAdmin(admin.ModelAdmin):
    fields = (
        'title',
        'category',
        'sapo',
        'publisher',
        'original_url',
        'thumb',
        'body', 
        'published_date',
        )
    list_display = (
        'id', 
        'title',
        'category_id',
        'sapo',
        'publisher_id',
        'original_url',
        'thumb'
        )
    search_fields = (
        'title',
        )
    list_filter = (
        'category_id',
        'publisher_id',
        'published_date',
        )


class PublisherAdmin(admin.ModelAdmin):
    fields = (
        'name',
        'url',
        )
    list_display = (
        'id',
        'name',
        'slug',
        )
    search_fields = (
        'name',
        )


admin.site.register(Article, ArticleAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Publisher, PublisherAdmin)