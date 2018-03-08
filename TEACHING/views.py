import os
from django.shortcuts import render
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, DeleteView
from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect
from django.http import StreamingHttpResponse

from AUTHENTICATION.models import StudentInfo
from TEACHING.models import UploadTeacher
from TEACHING.utils import export_homework, export_allhomework
from TEACHING.forms import FileUploadForm
from AUTHENTICATION import USER_IDENTITY_STUDENT, USER_IDENTITY_TEACHER


class StudentList(ListView):
    model = StudentInfo
    ordering = ['student_id']
    template_name = 'Teaching/student_list.html'
    paginate_by = 12

    def get_queryset(self):
        user_class = self.request.user.user_info.user_class
        objects = super(StudentList, self).get_queryset().filter(
            user_info__user_class__contains=user_class).order_by('student_id')
        for p in objects:
            p.homework_count = p.user_info.user.upload_set.all().count()
            p.save()
        return objects


class AllHomeworkExport(DetailView):
    model = StudentInfo

    def get(self, request, *args, **kwargs):
        def file_iterator(file, chunk_size=512):
            with open(file, 'rb') as f:
                while True:
                    c = f.read(chunk_size)
                    if c:
                        yield c
                    else:
                        break
        # name = '全部作业'
        temp = {}
        student = StudentInfo.objects.all().order_by('student_id')
        for stu in student:
            homework = stu.user_info.user.upload_set.all()
            temp[stu] = homework
        path = export_allhomework(request, temp, student)
        response = StreamingHttpResponse(
            file_iterator(path))
        response['Content-Type'] = 'application/octet-stream'
        response['Content-Disposition'] = 'attachment;\
            filename="{0}"'.format('all.pdf').encode('utf-8', 'ISO-8859-1')
        return response


class ExportDownload(DetailView):
    slug_field = 'uid'
    slug_url_kwarg = 'uid'
    model = StudentInfo

    def get(self, request, *args, **kwargs):
        student = self.get_object()
        self.object = self.get_object().user_info.user.upload_set.all()
        export_homework(request, self.object, student)

        def file_iterator(file, chunk_size=512):
            with open(file, 'rb') as f:
                while True:
                    c = f.read(chunk_size)
                    if c:
                        yield c
                    else:
                        break
        file_path = str(settings.BASE_DIR) + str(
            settings.TMP_FILES_URL) + '/' + str(
            student.user_info) + '.pdf'
        response = StreamingHttpResponse(file_iterator(file_path))
        response['Content-Type'] = 'application/octet-stream'
        response['Content-Disposition'] = 'attachment;\
            filename="{0}"'.format(
            str(student.user_info) + '_' + str(
                student.student_id) + '.pdf').encode('utf-8', 'ISO-8859-1')
        return response


class UploadHomework(CreateView):
    model = UploadTeacher
    form_class = FileUploadForm

    def post(self, request, *args, **kwargs):
        my_form = FileUploadForm(request.POST, request.FILES)
        if my_form.is_valid():
            # f = my_form.cleaned_data['my_file']
            # handle_uploaded_file(f)
            try:
                file_model = UploadTeacher()
                file_model.file_field = my_form.cleaned_data['file_field']
                file_model.data_type = my_form.cleaned_data['data_type']
                file_model.user = self.request.user
                file_model.data_class = self.request.user.user_info.user_class
                file_model.save()
                return HttpResponseRedirect('/Teaching/homeworklist/1')
            except Exception as e:
                print(str(e))
        return render(request, 'Teaching/homework_add.html', {'form': my_form})

    def get(self, request, *args, **kwargs):
        my_form = FileUploadForm()
        return render(request, 'Teaching/homework_add.html', {'form': my_form})


class HomeworkList(ListView):
    model = UploadTeacher
    ordering = ['submit_time']
    template_name = 'Teaching/homework_list.html'
    paginate_by = 6

    def get_queryset(self):
        objects = super(HomeworkList, self).get_queryset().filter(
            data_class=self.request.user.user_info.user_class)
        return objects


class HomeworkDelete(DeleteView):
    model = UploadTeacher
    success_url = reverse_lazy('Teaching:homeworklist', args=(1,))
    template_name = 'Teaching/homework_list.html'

    def get_object(self):
        return UploadTeacher.objects.get(uid=self.kwargs.get("uid"))


class HomeworkDownload(DetailView):
    model = UploadTeacher
    success_url = reverse_lazy('Teaching:homeworklist', args=(1,))

    def get(self, request, *args, **kwargs):
        def file_iterator(file, chunk_size=512):
            with open(file, 'rb') as f:
                while True:
                    c = f.read(chunk_size)
                    if c:
                        yield c
                    else:
                        break
        file = UploadTeacher.objects.get(uid=self.kwargs.get("uid")).file_field
        response = StreamingHttpResponse(file_iterator(file.path))
        response['Content-Type'] = 'application/octet-stream'
        response['Content-Disposition'] = 'attachment;\
            filename="{0}"'.format(
            file.name.split('/')[-1]).encode('utf-8', 'ISO-8859-1')
        return response
