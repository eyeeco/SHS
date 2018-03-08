from django.conf.urls import url, include

from . import views

urlpatterns = [
    url(r'^$', views.StudentList.as_view(), name='index'),
    url(r'^allexport$', views.AllHomeworkExport.as_view(),
        name='allexport'),
    url(r'^download/(?P<uid>.+)$', views.ExportDownload.as_view(),
        name='download'),
    url(r'^addhomework/$', views.UploadHomework.as_view(), name='addhomework'),
    url(r'^homeworklist/(?P<page>\d+)$', views.HomeworkList.as_view(),
        name='homeworklist'),
    url(r'^homeworkdelete/(?P<uid>.+)$', views.HomeworkDelete.as_view(),
        name='homeworkdelete'),
    url(r'^homeworkdownload/(?P<uid>.+)$', views.HomeworkDownload.as_view(),
        name='homeworkdownload'),
]
