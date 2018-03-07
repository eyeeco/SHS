from django.shortcuts import render
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from django.http import StreamingHttpResponse
from django.views.generic import ListView, CreateView, DeleteView, DetailView

from HOMEWORK.models import Upload
from HOMEWORK.forms import FileUploadForm


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
                file_model.data_class = self.request.user.user_info.user_class
                file_model.save()
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


class Download(DetailView):
    model = Upload
    success_url = reverse_lazy('homework:list')

    def get(self, request, *args, **kwargs):
        def file_iterator(file, chunk_size=512):
            with open(file, 'rb') as f:
                while True:
                    c = f.read(chunk_size)
                    if c:
                        yield c
                    else:
                        break
        file = Upload.objects.get(uid=self.kwargs.get("uid")).file_field
        response = StreamingHttpResponse(file_iterator(file.path))
        response['Content-Type'] = 'application/octet-stream'
        response['Content-Disposition'] = 'attachment;\
            filename="{0}"'.format(
            file.name.split('/')[-1]).encode('utf-8', 'ISO-8859-1')
        return response
