from django.db import models
from tag.models import Tag
from django.conf import settings


class Link(models.Model):
    title = models.CharField(max_length=200, unique=True)
    link = models.URLField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    tags = models.ManyToManyField(Tag)
    description = models.TextField(max_length=500)
    voted = models.BooleanField(default=False)
    upvotes = models.IntegerField(default=0)
    report = models.BooleanField(default=False)

    def __str__(self):
        return self.title




