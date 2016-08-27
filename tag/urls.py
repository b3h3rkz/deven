from django.conf.urls import url
from .views import TagListView, CreateTagView, TagDetailView


urlpatterns = [
    url(r'^$', CreateTagView.as_view(), name='list'),
    url(r'^add/$', TagListView.as_view(), name='add'),
    url(r'^(?P<pk>[0-9]+)/$', TagDetailView.as_view(), name='detail'),
]
