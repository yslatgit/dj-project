"""learn_dj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import include,url
from django.conf.urls.static import static  #部署到服务器时---静态文件的访问-方法2
from django.views.static import serve
from .settings import STATIC_URL

urlpatterns = [
    path('admin/', admin.site.urls),
    # url(r'^$',include('learn.urls')),
    path('learn/',include('learn.urls',namespace='learn')),
    path('interface/',include('interface.urls',namespace='interface')),
    path('bank/',include('bank.urls',namespace='bank')),
    path('yoyo/',include('yoyo.urls',namespace='yoyo')),
    url('^static/(?P<path>.*)$',serve,{'document_root':STATIC_URL},name='static'),
    # url(r'^say$', views.say),
]
# + static(STATIC_URL,document_root='learn/staticfiles') #静态文件路径配置
