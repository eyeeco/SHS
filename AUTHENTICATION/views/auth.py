from django.views.generic import View, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView as _LoginView
from django.views.generic import RedirectView, TemplateView
from django.views.generic import ListView
from django.urls import reverse_lazy, reverse
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.http import HttpResponseRedirect

from AUTHENTICATION import USER_IDENTITY_STUDENT
from AUTHENTICATION.forms import StudentRegisterForm, LoginForm
from TEACHING.models import UploadTeacher


class IndexView(LoginRequiredMixin, RedirectView):
    """
    A index view.
    """
    template_name = 'index.html'
    url = reverse_lazy('auth:index', args=(1,))


class HomeworkListPage(ListView):
    model = UploadTeacher
    ordering = ['submit_time']
    template_name = 'index.html'
    paginate_by = 6

    def get_queryset(self):
        objects = super(HomeworkListPage, self).get_queryset().filter(
            data_class=self.request.user.user_info.user_class).filter(
                data_type=2)
        return objects


class LoginView(_LoginView):
    template_name = 'login.html'
    form_class = LoginForm


class StudentRegisterView(CreateView):
    """
    a view for auth registration
    """
    template_name = 'register.html'
    form_class = StudentRegisterForm
    identity = USER_IDENTITY_STUDENT
    form_post_url = reverse_lazy('auth:register:index')
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        username = form.cleaned_data['username']
        first_name = form.cleaned_data['name']
        password = form.cleaned_data['password']
        email = form.cleaned_data['email']
        user = User.objects.create_user(
            email=email,
            username=username,
            password=password,
            first_name=first_name)
        form.instance.user = user
        form.instance.identity = self.identity
        self.object = form.save()
        login(self.request, user,
              backend='django.contrib.auth.backends.ModelBackend')
        return HttpResponseRedirect(self.get_success_url())
