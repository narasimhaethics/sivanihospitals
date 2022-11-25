#from django.conf.urls import include,url
from django.urls import include, re_path
from django.contrib import admin
from .import views

urlpatterns = [
    re_path(r'^admin/', admin.site.urls),
    re_path(r'^bot/',views.index,name='index'),


 re_path(r'^searchform/$', views.search_form, name='searchform'),
        re_path(r'^$', views.search, name='search'),

]