from rest_framework.serializers import ModelSerializer, SerializerMethodField
from .models import User


class UserInfo(ModelSerializer):
    votes = SerializerMethodField()

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'votes']

    def get_votes(self, obj):
        user = obj.votes_set
        return user
