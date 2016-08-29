from django.db import models
from django.db.models import Count
from tag.models import Tag
from django.conf import settings
import urllib.request
from urllib.parse import urlparse
# from bs4 import BeautifulSoup


class LinkVoteCountManager(models.Manager):
    def get_query_set(self):
        return super(LinkVoteCountManager, self).get_query_set().annotate(
            votes=Count('vote')).order_by('-votes')


class Link(models.Model):
    title = models.CharField(max_length=200, unique=True)
    link = models.URLField()
    poster = models.ForeignKey(settings.AUTH_USER_MODEL)
    tags = models.ManyToManyField(Tag)
    description = models.TextField(max_length=500)

    with_votes = LinkVoteCountManager()

    def __str__(self):
        return self.title
    #
    # def desc(self):
    #     link = self.link
    #     page = urllib.request.urlopen(link)
    #     soup = BeautifulSoup(page)
    #     desci = soup.find_all(attrs={'name':"description"})
    #     return desci


class Vote(models.Model):
    voter = models.ForeignKey(settings.AUTH_USER_MODEL)
    link = models.ForeignKey(Link)

    def __str__(self):
        return "%s upvoted %s" % (self.voter.username, self.link.title)



