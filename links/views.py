from django.shortcuts import render
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView
from .models import Link
from .serializers import LinkListModelSerializer, AddLinkModelSerializer
from rest_framework.permissions import IsAuthenticated


class LinksListAPIView(ListAPIView):
    model = Link
    serializer_class = LinkListModelSerializer
    queryset = Link.objects.all()
    permission_classes = (IsAuthenticated,)


class AddLinkAPIView(CreateAPIView):
    model = Link
    serializer_class = AddLinkModelSerializer
    queryset = Link.objects.all()
    permission_classes = (IsAuthenticated,)

