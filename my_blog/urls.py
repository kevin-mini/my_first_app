from django.conf.urls import include, url
from django.contrib import admin 
from .views import Hello,TestHello

urlpatterns = [
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^Hello',Hello,name='hello'),
    url(r'^test',TestHello,name='test'),
]





