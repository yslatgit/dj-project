from django.contrib import admin
from django.conf.urls import url
from . import views

app_name = '[learn]'

urlpatterns =  [
    url(r'^index/$',views.index,name='index'),
    url(r'^page/',views.page),
    url(r'^test/',views.test,name='test_page'),
    url(r'^child/',views.child),
    url(r'^add/',views.db_add),
    url(r'^$',views.default),
    url(r'^select_all/$',views.select_all),
    url(r'^add_user/$',views.add_user),
    url(r'^del_user/(\d*)$',views.delete_user),
    url(r'^ajax/$', views.ajax),
    url(r'^ajax.json1$', views.ajax_action1),
    url(r'^ajax.json2/(.*)$', views.ajax_action2),
    url(r'^say$', views.say),
    url(r'^get/$', views.get),
    url(r'^uploadPic/$', views.uploadPic),
    url(r'^uploadPicHandle/$', views.uploadPicHandle),
    url(r'^citybase/$', views.citybase),
    url(r'^pro/$', views.pro),
    url(r'^city/(\d+)/$', views.city),
    ]