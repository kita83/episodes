from django.conf.urls import url
from django.views.generic import TemplateView

from . import views

app_name = 'feed'
urlpatterns = [
    url(r'$', views.index, name='index'),
    url(r'^signup/?$', views.signup, name='signup'),
    url(r'^login/$', views.login, name='login'),
    url(r'^logout/$', views.logout, name='logout'),
]
