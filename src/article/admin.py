from django.contrib import admin
from parler.admin import TranslatableAdmin

from article.models import Category, Article


@admin.register(Category)
class CategoryAdmin(TranslatableAdmin):
    list_display = ['name', 'slug']

    def get_prepopulated_fields(self, request, obj=None):
        return {'slug': ('name',)}


@admin.register(Article)
class ProductAdmin(TranslatableAdmin):
    list_display = ['name', 'slug', 'active', 'created', 'updated']
    list_filter = ['active', 'created', 'updated']
    list_editable = ['active']

    def get_prepopulated_fields(self, request, obj=None):
        return {'slug': ('name',)}
