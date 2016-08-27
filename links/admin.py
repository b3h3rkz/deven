from django.contrib import admin
from .models import Link


class LinkModelAdmin(admin.ModelAdmin):
    model = Link
    list_display = ['title', 'link', 'description', 'upvotes', 'report']


admin.site.register(Link, LinkModelAdmin)
