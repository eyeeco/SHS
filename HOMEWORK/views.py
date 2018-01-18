from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.generic import ListView, CreateView, UpdateView

from HOMEWORK.models import Homework
from HOMEWORK.forms import HomeworkAdd

# Create your views here.
class HomeworkList(ListView):
    model = Homework
    ordering = ['submit_time',]
    template_name = 'Homework/homework_list.html'

    def get_queryset(self):
        return super(HomeworkList, self).get_queryset()


class HomeworkAdd(CreateView):
    model = Homework
    template_name = 'Homework/homework.html'
    form_class = HomeworkAdd

    def form_valid(self, form):
        title = self.request.POST.get('title', None)
        content = self.request.POST.get('editor', None)
        homework = Homework(title=title, content=content)
        homework.save()
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        return 'list'
