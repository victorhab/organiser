from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home_view, name='home_view'),
    url(r'^login/$', views.login, name='login'),
    url(r'^month/$', views.month_view, name='month_view'),
    url(r'^week/$', views.week_view, name='week_view'),
    url(r'^day/$', views.day_view, name='day_view'),
    url(r'^createevent/$', views.createevent, name='createevent'),
]
