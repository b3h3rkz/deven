from django.conf.urls import url
from .views import LinksListAPIView, AddLinkAPIView


urlpatterns = [
    url(r'^$', LinksListAPIView.as_view(), name='list'),
    url(r'^add/', AddLinkAPIView.as_view(), name='add-link'),
]
