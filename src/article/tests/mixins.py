from datetime import datetime

from article.models import Category, Article


class ArticleTestMixin:

    @staticmethod
    def create_category(num=1):
        category = Category()
        category.name = f'category{num} en'
        category.slug = f'category{num}_en'
        category.save()
        category.set_current_language('ru')
        category.name = f'category{num} ru'
        category.slug = f'category{num}_ru'
        category.save()
        category.set_current_language('es')
        category.name = f'category{num} es'
        category.slug = f'category{num}_es'
        category.save()

    @staticmethod
    def create_article(category, num=1):
        article = Article()
        article.name = f'article{num} en'
        article.slug = f'article{num}_en'
        article.description = f'article{num} en description'
        article.active = Article.Status.PUBLISHED
        article.pub_datetime = datetime.now().astimezone().isoformat()
        article.category = category
        article.save()
        article.set_current_language('ru')
        article.name = f'article{num} ru'
        article.slug = f'article{num}_ru'
        article.description = f'article{num} ru description'
        article.save()
        article.set_current_language('es')
        article.name = f'article{num} es'
        article.slug = f'article{num}_es'
        article.description = f'article{num} es description'
        article.save()
