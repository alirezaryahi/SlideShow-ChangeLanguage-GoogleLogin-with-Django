from django.db import models
from translated_fields import TranslatedField
from django.utils.translation import gettext_lazy as _


# Create your models here.


class Article(models.Model):
    title = TranslatedField(models.CharField(_('title'), max_length=100))
    image = models.ImageField(_('image'), upload_to='images/')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.BooleanField(_('status'), default=False)

    class Meta:
        ordering = ['-created']
        verbose_name = _('Article')
        verbose_name_plural = _('Articles')

    def __str__(self):
        return self.title


class Slider(models.Model):
    article = models.OneToOneField(Article, on_delete=models.CASCADE, verbose_name='article')
    status = models.BooleanField(_('status'), default=False)

    class Meta:
        ordering = ['-article__created']
        verbose_name = _('slideShow')
        verbose_name_plural = _('slideShows')

    def __str__(self):
        return self.article.title
