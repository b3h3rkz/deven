from django.db import models
from django.conf import settings


class Tag(models.Model):
    name = models.CharField(max_length=10, unique=True)
    created_on = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL)

    def __str__(self):
        return self.name


