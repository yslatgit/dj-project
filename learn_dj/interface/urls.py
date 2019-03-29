from django.conf.urls import url
from . import views

app_name = '[interface]'

urlpatterns = [
    url(r'^get/$',views.get),
]