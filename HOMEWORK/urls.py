from django.conf.urls import url, include

from . import views

urlpatterns = [
    # url(r'^$', views.HomeworkAdd.as_view(), name='add'),
    url(r'^list/(?P<page>\d+)$', views.Uploadlist.as_view(), name='list'),
    url(r'^upload/$', views.UploadAdd.as_view(), name='upload'),
    url(r'^cancel/(?P<uid>.+)$', views.UploadCancel.as_view(),
        name='cancel'),
    url(r'^download/(?P<uid>.+)$', views.Download.as_view(),
        name='download'),
]
