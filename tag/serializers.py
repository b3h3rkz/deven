from rest_framework.serializers import ModelSerializer, CurrentUserDefault, HiddenField
from django.contrib.auth.models import User
from .models import Tag


class TagModelSerializer(ModelSerializer):
    user = HiddenField(default=CurrentUserDefault())

    class Meta:
        model = Tag
        fields = ['id', 'name', 'user']
