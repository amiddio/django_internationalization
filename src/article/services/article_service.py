from article.models import Article


class ArticleService:

    PAGE_LIMIT = 3

    @staticmethod
    def get_objects(category_slug=None):
        query = Article.objects.all().filter(active=True)\
                   .prefetch_related('translations')\
                   .select_related('category')\
                   .prefetch_related('category__translations')

        if category_slug:
            query = query.filter(category__translations__slug=category_slug)

        return query
