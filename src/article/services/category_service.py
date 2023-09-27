from article.models import Category


class CategoryService:
    """
    Промежуточный слой содержащий бизнес логику категорий статей
    """

    @staticmethod
    def get_objects():
        return Category.objects.all().prefetch_related('translations')
