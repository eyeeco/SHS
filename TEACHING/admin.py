from django.contrib import admin

# Register your models here.
from .models import UploadTeacher


@admin.register(UploadTeacher)
class UploadTeacherAdmin(admin.ModelAdmin):
    pass
