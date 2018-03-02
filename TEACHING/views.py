import os
from django.shortcuts import render
from django.shortcuts import redirect
from django.views.generic import ListView, DetailView
from django.conf import settings
from django.http import HttpResponse
from django.http import StreamingHttpResponse

from AUTHENTICATION.models import StudentInfo
from TEACHING.utils import export_homework, export_allhomework


class StudentList(ListView):
    model = StudentInfo
    ordering = ['student_id']
    template_name = 'Teaching/student_list.html'
    export_status = False

    def get_queryset(self):
        student_list = StudentInfo.objects.all().order_by('student_id')
        for stu in student_list:
            stu.homework_count = stu.user_info.user.upload_set.all().count()
            if os.path.exists(str(settings.BASE_DIR) + str(
                              settings.TMP_FILES_URL) + '/' + str(
                              stu.user_info) + '.docx'):
                stu.status = True
            else:
                stu.status = False
            stu.save()
        return student_list


class StudentHomeworkExport(DetailView):
    slug_field = 'uid'
    slug_url_kwarg = 'uid'
    model = StudentInfo

    def post(self, request, *args, **kwargs):
        student = self.get_object()
        self.object = self.get_object().user_info.user.upload_set.all()
        export_homework(self.object, student)
        return redirect('/Teaching')


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
        path = export_allhomework(temp, student)
        response = StreamingHttpResponse(file_iterator(str(settings.BASE_DIR) + path))
        response['Content-Type'] = 'application/octet-stream'
        response['Content-Disposition'] = 'attachment;\
            filename="{0}"'.format('all.docx').encode('utf-8', 'ISO-8859-1')
        return response


class ExportDownload(DetailView):
    slug_field = 'uid'
    slug_url_kwarg = 'uid'
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
        student = self.get_object()
        file_path = str(settings.BASE_DIR) + str(
            settings.TMP_FILES_URL) + '/' + str(
            student.user_info) + '.docx'
        response = StreamingHttpResponse(file_iterator(file_path))
        response['Content-Type'] = 'application/octet-stream'
        response['Content-Disposition'] = 'attachment;\
            filename="{0}"'.format(
            str(student.user_info) + '_' + str(
                student.student_id) + '.docx').encode('utf-8', 'ISO-8859-1')
        return response
