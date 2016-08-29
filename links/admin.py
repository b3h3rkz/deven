from django.contrib import admin
from .models import Link, Vote


class LinkModelAdmin(admin.ModelAdmin):
    model = Link
    list_display = ['title', 'link', 'description', 'poster']


class  VotesModelAdmin(admin.ModelAdmin):
    model = Vote


admin.site.register(Link, LinkModelAdmin)
admin.site.register(Vote, VotesModelAdmin)
