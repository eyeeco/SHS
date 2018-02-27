from django.conf.urls import url, include

from . import views

register_patterns = [
    url(r'^$', views.StudentRegisterView.as_view(), name='index'),
]

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^register/', include(register_patterns, namespace='register')),
]
