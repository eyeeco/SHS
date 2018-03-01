from django.contrib.auth.mixins import UserPassesTestMixin
from django.views.generic import RedirectView, TemplateView
from django.views.generic import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin

from AUTHENTICATION import USER_IDENTITY_STUDENT
from AUTHENTICATION.models import StudentInfo


class InfoDetailBase(LoginRequiredMixin, DetailView):
    """
    A index view.
    """
    http_method_names = ['get']
    slug_field = 'uid'
    slug_url_kwarg = 'uid'


class StudentInfoDetail(UserPassesTestMixin, InfoDetailBase):

    model = StudentInfo
    fields = '__all__'
    template_name = 'profile.html'
    raise_exception = True

    def test_func(self):
        user = self.request.user
        return user.is_authenticated and \
            user.user_info.identity == USER_IDENTITY_STUDENT
