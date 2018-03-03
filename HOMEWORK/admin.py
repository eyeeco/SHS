from django.contrib import admin

# Register your models here.
from .models import Homework, Upload


@admin.register(Homework)
class HomeworkAdmin(admin.ModelAdmin):
    pass


@admin.register(Upload)
class UploadAdmin(admin.ModelAdmin):
    pass
