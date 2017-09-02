from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^download/$', views.download, name='download'),
    url(r'^link/(?P<pk>\d+)/result/$', views.result, name='result'),
]
