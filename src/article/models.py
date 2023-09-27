from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from parler.models import TranslatableModel, TranslatedFields
from django.db import models


class Category(TranslatableModel):
    """
    Модель категорий статей
    """

    translations = TranslatedFields(
        name=models.CharField(max_length=50),
        slug=models.SlugField(max_length=50, unique=True),
    )

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name


class Article(TranslatableModel):
    """
    Модель статей
    """

    class Status(models.IntegerChoices):
        DRAFT = (0, _('Draft'))
        PUBLISHED = (1, _('Published'))

    translations = TranslatedFields(
        name=models.CharField(max_length=100),
        slug=models.SlugField(max_length=100, unique=True),
        description=models.TextField(),
    )
    active = models.BooleanField(choices=Status.choices, default=Status.DRAFT)
    pub_datetime = models.DateTimeField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name='articles')

    class Meta:
        ordering = ['-pub_datetime']
        indexes = [
            models.Index(fields=['-pub_datetime']),
        ]

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('article:detail', args=[self.slug])
