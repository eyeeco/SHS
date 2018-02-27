from django.shortcuts import render
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect, HttpResponse
from django.views.generic import ListView, CreateView, DeleteView

from HOMEWORK.models import Homework, Upload
from HOMEWORK.forms import HomeworkAdd, FileUploadForm


class HomeworkList(ListView):
    model = Homework
    ordering = ['submit_time', ]
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


class UploadAdd(CreateView):
    model = Upload
    form_class = FileUploadForm

    def post(self, request, *args, **kwargs):
        my_form = FileUploadForm(request.POST, request.FILES)
        if my_form.is_valid():
            # f = my_form.cleaned_data['my_file']
            # handle_uploaded_file(f)
            try:
                file_model = Upload()
                file_model.file_field = my_form.cleaned_data['file_field']
                file_model.user = self.request.user
                file_model.save()
                print(file_model.file_field.name)
                return HttpResponseRedirect('/Homework/list')
            except Exception as e:
                print(str(e))
        return render(request, 'Homework/upload_add.html', {'form': my_form})

    def get(self, request, *args, **kwargs):
        my_form = FileUploadForm()
        return render(request, 'Homework/upload_add.html', {'form': my_form})


class Uploadlist(ListView):
    model = Upload
    ordering = ['submit_time']
    template_name = 'Homework/upload_list.html'

    def get_queryset(self):
        return super(Uploadlist, self).get_queryset().filter(
            user=self.request.user)


class UploadCancel(DeleteView):
    model = Upload
    success_url = reverse_lazy('homework:list')
    template_name = 'Homework/upload_list.html'
    context_object_name = "Upload_list"

    def get_object(self):
        return Upload.objects.get(uid=self.kwargs.get("uid"))
