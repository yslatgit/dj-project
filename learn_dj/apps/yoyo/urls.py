#coding:utf-8
from django.conf.urls import url
from .views import Dj15View,Dj16View,Dj27View,Dj28View

app_name = '[yoyo]'

urlpatterns = [
    url('^dj15/(?P<type>\d+)$',Dj15View.as_view(),name='dj15'),
    url('^dj16/$',Dj16View.as_view(),name='dj16'),
    url('^dj27/$',Dj27View.as_view(),name='dj27'),
    url('^dj28/$',Dj28View.as_view(),name='dj28'),
]