from django.conf.urls import url, include

from . import views

urlpatterns = [
    url(r'^$', views.property_list, name='list'),
    url(r'^search/', include('haystack.urls')),
    url(r'(?P<pk>\d+)/$', views.property_detail, name='detail'),
]
