from rest_framework.serializers import ( HyperlinkedIdentityField,
                                         HiddenField,
                                         ModelSerializer,
                                         CurrentUserDefault,)
from django.contrib.auth.models import User
from .models import Link
from tag.models import Tag


class AddLinkModelSerializer(ModelSerializer):
        user = HiddenField(default=CurrentUserDefault)
        tags = Tag.objects.all()

        class Meta:
            model = Link
            fields = ['title', 'link', 'user', 'tags']


class LinkListModelSerializer(ModelSerializer):
    tags = HyperlinkedIdentityField(view_name='tags:detail', lookup_field='pk', many=True)

    class Meta:
        model = Link
        fields = ['id', 'title', 'link', 'description', 'upvotes', 'voted', 'tags']



