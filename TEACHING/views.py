from django.shortcuts import render
from django.shortcuts import redirect
from django.views.generic import ListView, DetailView

from AUTHENTICATION.models import StudentInfo
from TEACHING.utils import export_homework


class StudentList(ListView):
    model = StudentInfo
    ordering = ['student_id']
    template_name = 'Teaching/student_list.html'

    def get_queryset(self):
        student_list = StudentInfo.objects.all().order_by('student_id')
        for stu in student_list:
            stu.homework_count = stu.user_info.user.upload_set.all().count()
            stu.save()
        return student_list


class StudentHomeworkExport(DetailView):
    slug_field = 'uid'
    slug_url_kwarg = 'uid'
    model = StudentInfo

    def post(self, request, *args, **kwargs):
        name = self.get_object().user_info
        self.object = self.get_object().user_info.user.upload_set.all()
        return redirect(export_homework(self.object, name))
