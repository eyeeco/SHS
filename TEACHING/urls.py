from django.conf.urls import url, include

from . import views

urlpatterns = [
    url(r'^$', views.StudentList.as_view(), name='index'),
    url(r'^export/(?P<uid>.+)$', views.StudentHomeworkExport.as_view(),
        name='export'),
]
