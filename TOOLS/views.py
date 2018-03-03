from django.contrib.auth.mixins import UserPassesTestMixin
from django.views.generic import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin

from AUTHENTICATION import USER_IDENTITY_STUDENT
from AUTHENTICATION.models import StudentInfo

import datetime


class InfoDetailBase(DetailView):
    """
    A index view.
    """
    http_method_names = ['get']
    slug_field = 'uid'
    slug_url_kwarg = 'uid'


class StudentInfoDetail(InfoDetailBase):

    model = StudentInfo
    fields = '__all__'
    template_name = 'profile_cover.html'
    raise_exception = True

    def get_context_data(self, **kwargs):
        now = datetime.datetime.now()
        kwargs['now'] = now
        return super(StudentInfoDetail, self).get_context_data(**kwargs)
