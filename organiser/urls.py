from django.conf.urls import url
from . import views
from django.conf import settings
from django.contrib.auth.views import logout

urlpatterns = [
    url(r'^$', views.home_view, name='home_view'),
    url(r'^login/$', views.auth_login, name='auth_login'),
    url(r'^month/$', views.month_view, name='month_view'),
    url(r'^week/$', views.week_view, name='week_view'),
    url(r'^day/$', views.day_view, name='day_view'),
    url(r'^createevent/$', views.createevent, name='createevent'),
    url(r'^logout/$', logout, {'next_page': settings.LOGOUT_REDIRECT_URL}, name='logout'),
    url(r'^events/$', views.EventView.as_view(), name='events'),
]
