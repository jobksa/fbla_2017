#!python
# log/urls.py
from django.conf.urls import url
from . import views
from .views import employeeDetail

urlpatterns = [
    url(r'^manager/$', views.manager, name='manager'),
    url(r'^manager/build$', views.build, name='build'),
    url(r'^manager/inbox$', views.inbox, name='inbox'),
    url(r'^manager/edit/(?P<pk>\d+)/$', views.employeeDetail.as_view(), name='employeeDetailView'),
    url(r'^manager/inbox/(?P<pk>\d+)/$', views.messageDetail.as_view(), name='contactDetailView'),
    url(r'^manager/reservation/(?P<pk>\d+)/$', views.reserveDetail.as_view(), name='reservetDetailView'),

]
