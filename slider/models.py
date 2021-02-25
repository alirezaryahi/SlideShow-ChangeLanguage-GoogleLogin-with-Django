from django.db import models

# Create your models here.


class Article(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=False)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return self.title



class Slider(models.Model):
    article=models.OneToOneField(Article, on_delete=models.CASCADE)
    status = models.BooleanField(default=False)

    class Meta:
        ordering = ['-article__created']

    def __str__(self):
        return self.article.title