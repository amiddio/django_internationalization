from article.models import Article


class ArticleService:

    PAGE_LIMIT = 3

    @staticmethod
    def get_objects():
        return Article.objects.all().filter(active=True)\
                   .prefetch_related('translations')\
                   .select_related('category')\
                   .prefetch_related('category__translations')
