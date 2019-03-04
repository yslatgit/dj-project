from django.contrib import admin
from django.conf.urls import url
from learn import views

urlpatterns =  [
    url(r'^index/$',views.index),
    url(r'^page/',views.page),
    url(r'^test/',views.test,name='test_page'),
    url(r'^child/',views.child),
    url(r'^add/',views.db_add),
    url(r'^$',views.default),
    url(r'^select_all/$',views.select_all),
    url(r'^add_user/$',views.add_user),
    url(r'^del_user/(\d*)$',views.delete_user),
]