from django.conf.urls import url, include

from . import views

urlpatterns = [
    url(r'^profile/(?P<uid>.+)$', views.StudentInfoDetail.as_view(),
        name='profile'),
]
