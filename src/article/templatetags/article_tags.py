from django import template

from article.services.article_service import ArticleService

register = template.Library()


@register.inclusion_tag('includes/articles.html')
def last_articles():
    articles = ArticleService.get_objects()[0:5]
    return {'articles': articles, 'hide_pagination': True}
