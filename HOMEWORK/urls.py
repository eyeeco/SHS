from django.conf.urls import url, include

from . import views

urlpatterns = [
    # url(r'^$', views.ProjectIndex.as_view(), name='index'),
    url(r'^$', views.HomeworkAdd.as_view(), name='add'),
    url(r'^list/$', views.Uploadlist.as_view(), name='list'),
    url(r'^upload/$', views.UploadAdd.as_view(), name='upload'),
    url(r'^cancel/(?P<uid>.+)$', views.UploadCancel.as_view(),
        name='cancel'),
]
