from django.conf.urls import url
from . import views

app_name = '[interface]'

urlpatterns = [
    url(r'^get/$',views.get),
    url(r'^test/$',views.test),
    url(r'^get_data/$',views.get_data),
    url(r'^change_data/(\d*)$',views.change_casestatus),
    # url(r'^get_data2/$',views.get_data2),
]