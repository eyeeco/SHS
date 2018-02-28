from django.shortcuts import render
from django.views.generic import ListView

from AUTHENTICATION.models import StudentInfo


class StudentList(ListView):
    model = StudentInfo
    ordering = ['student_id']
    template_name = 'Teaching/student_list.html'

    def get_queryset(self):
        student_list = StudentInfo.objects.all().order_by('student_id')
        for stu in student_list:
            stu.homework_count = stu.user_info.user.upload_set.all().count()
        return student_list
