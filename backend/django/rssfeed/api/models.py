from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    url = models.URLField(max_length=2048)
    thumbnail = models.URLField(max_length=2048, blank=True)
    published_date = models.DateTimeField()
    language = models.CharField(max_length=200)

    def __str__(self):
        return self.title
