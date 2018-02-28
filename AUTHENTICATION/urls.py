from django.conf.urls import url, include
from django.contrib.auth import views as auth_views
from . import views

register_patterns = [
    url(r'^$', views.StudentRegisterView.as_view(), name='index'),
]

info_patterns = [
    url(r'^student/(?P<uid>.+)$', views.StudentInfoDetail.as_view(),
        name='student')
]

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^register/', include(register_patterns, namespace='register')),
    url(r'^login/', views.LoginView.as_view(), name='login'),
    url(r'^logout/', auth_views.LogoutView.as_view(next_page='index'),
        name='logout'),
    url(r'^info/', include(info_patterns, namespace='info'))
]
