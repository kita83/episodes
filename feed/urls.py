import django.contrib.auth.views
from django.conf.urls import url

from . import views

app_name = 'oauth'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^login/$', django.contrib.auth.views.login, {'template_name': 'login.html'}, name='login'),
    url(r'^logout/$', django.contrib.auth.views.login, {'template_name': 'logout.html'}, name='logout'),
]
