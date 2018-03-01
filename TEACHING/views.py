import os
from django.shortcuts import render
from django.shortcuts import redirect
from django.views.generic import ListView, DetailView
from django.conf import settings

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
        name = self.get_object().user_info
        self.object = self.get_object().user_info.user.upload_set.all()
        export_homework(self.object, name)
        return redirect('/Teaching')


class AllHomeworkExport(DetailView):
    model = StudentInfo

    def get(self, request, *args, **kwargs):
        # name = '全部作业'
        temp = {}
        student = StudentInfo.objects.all().order_by('student_id')
        for stu in student:
            homework = stu.user_info.user.upload_set.all()
            temp[stu] = homework
        export_allhomework(temp, student)
        return redirect('/Teaching')
