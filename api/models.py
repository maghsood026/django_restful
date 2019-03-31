from django.db import models


class Article(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50, blank=False, null=False)
    content = models.CharField(max_length=500)
    author = models.CharField(max_length=32, null=False, blank=False)

    def __str__(self):
        return self.title
