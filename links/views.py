from django.shortcuts import render
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView
from .models import Link, Vote
from .serializers import LinkListModelSerializer, AddLinkModelSerializer, UserVotesSerializer
from rest_framework.permissions import IsAuthenticated


class LinksListAPIView(ListAPIView):
    model = Link
    serializer_class = LinkListModelSerializer
    queryset = Link.with_votes.all()
    permission_classes = (IsAuthenticated,)


class AddLinkAPIView(CreateAPIView):
    model = Link
    serializer_class = AddLinkModelSerializer
    permission_classes = (IsAuthenticated,)


class UserVotesView(ListAPIView):
    model = Vote
    serializer_class = UserVotesSerializer
    queryset = Vote.objects.all()
