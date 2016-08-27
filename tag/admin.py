from django.contrib import admin
from .models import Tag


class TagModelAdmin(admin.ModelAdmin):
    model = Tag
    list_display = ['id', 'name', 'user', 'created_on']
    search_fields = ['name']

admin.site.register(Tag, TagModelAdmin)
