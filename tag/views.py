from django.shortcuts import render
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView
from rest_framework.permissions import IsAuthenticated
from .models import Tag
from .serializers import TagModelSerializer


class TagListView(ListAPIView):
    model = Tag
    serializer_class = TagModelSerializer
    queryset = Tag.objects.all()
    permission_classes = (IsAuthenticated,)


class CreateTagView(CreateAPIView):
    model = Tag
    serializer_class = TagModelSerializer
    queryset = Tag.objects.all()
    permission_classes = (IsAuthenticated,)


class TagDetailView(RetrieveAPIView):
    model = Tag
    serializer_class = TagModelSerializer
    queryset = Tag.objects.all()
    permission_classes = (IsAuthenticated,)






