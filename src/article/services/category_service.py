from article.models import Category


class CategoryService:

    @staticmethod
    def get_objects():
        return Category.objects.all().prefetch_related('translations')
