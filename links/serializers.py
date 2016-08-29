from rest_framework.serializers import ( HyperlinkedIdentityField,
                                         HiddenField,
                                         ModelSerializer,
                                         CurrentUserDefault,)
from django.contrib.auth.models import User
from .models import Link, Vote
from tag.models import Tag


class AddLinkModelSerializer(ModelSerializer):
        poster = HiddenField(default=CurrentUserDefault)
        tags = Tag.objects.all()

        class Meta:
            model = Link
            fields = ['title', 'link', 'poster', 'tags']


class LinkListModelSerializer(ModelSerializer):
    tags = HyperlinkedIdentityField(view_name='tags:detail', lookup_field='pk', many=True)

    class Meta:
        model = Link
        fields = ['id', 'title', 'link', 'description', 'poster', 'tags', 'with_votes']


class UserVotesSerializer(ModelSerializer):
    class Meta:
        model = Vote
        fields = ['voter', 'link']





