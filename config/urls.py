# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from rest_framework_jwt.views import obtain_jwt_token

from django.views import defaults as default_views

from deven.users.views import FacebookLogin, TwitterLogin

urlpatterns = [

    # Django Admin, use {% url 'admin:index' %}
    url(settings.ADMIN_URL, include(admin.site.urls)),

    # User management
    url(r'^api/v1/users/', include('deven.users.urls', namespace='users')),
    url(r'^accounts/', include('allauth.urls')),

    #app
    url(r'^api/v1/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^api/accounts/', include('rest_auth.urls')),
    url(r'^api/accounts/registration/', include('rest_auth.registration.urls')), #registration endpoint4
    url(r'^api/accounts/facebook/$', FacebookLogin.as_view(), name='fb_login'),
    url(r'^api/accounts/twitter/$', TwitterLogin.as_view(), name='twitter_login'),
    url(r'^api-token-auth/', obtain_jwt_token),


    # deven local app urls
    url(r'^api/v1/tags/', include('tag.urls', namespace='tags')),
    url(r'^api/v1/links/', include('links.urls', namespace='links')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



if settings.DEBUG:
    # This allows the error pages to be debugged during development, just visit
    # these url in browser to see how these error pages look like.
    urlpatterns += [
        url(r'^400/$', default_views.bad_request, kwargs={'exception': Exception('Bad Request!')}),
        url(r'^403/$', default_views.permission_denied, kwargs={'exception': Exception('Permission Denied')}),
        url(r'^404/$', default_views.page_not_found, kwargs={'exception': Exception('Page not Found')}),
        url(r'^500/$', default_views.server_error),
    ]
