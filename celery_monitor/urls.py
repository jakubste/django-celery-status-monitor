from django.conf.urls import url

from celery_monitor import views

urlpatterns = [
    url(r'^list/$', views.CeleryHeartBeatListView.as_view(), name='list'),
    url(r'^(?P<label>[\w-]+)/$', views.CeleryHeartBeatDetailView.as_view(), name='detail'),
    url(r'^status/(?P<label>[\w-]+)/$', views.CeleryHeartBeatStatusView.as_view(), name='status'),
]
