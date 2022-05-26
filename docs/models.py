from django.db import models


class Doc(models.Model):
    image = models.ImageField(blank=True, null=True, default=None)
    title = models.CharField(max_length=100, default=None)
    description = models.TextField(default=None)
    author_1 = models.CharField(max_length=100, default=None)
    author_2 = models.CharField(max_length=100, default=None)
    document = models.FileField(upload_to='documents/', default=None, blank=True, null=True)

    def __str__(self):
        return self.title
