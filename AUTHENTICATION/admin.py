from django.contrib import admin

# Register your models here.
from .models import StudentInfo, UserInfo, TeacherInfo


@admin.register(StudentInfo)
class StudentInfoAdmin(admin.ModelAdmin):
    pass


@admin.register(UserInfo)
class UserInfoAdmin(admin.ModelAdmin):
    pass


@admin.register(TeacherInfo)
class TeacherInfoAdmin(admin.ModelAdmin):
    pass
