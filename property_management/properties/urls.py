from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^properties/$', views.properties, name='properties'),
    #url(r'^properties/(\d+)/$', views.property, name='property'),
]