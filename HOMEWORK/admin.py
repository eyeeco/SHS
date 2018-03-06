from django.contrib import admin

# Register your models here.
from .models import Upload


@admin.register(Upload)
class UploadAdmin(admin.ModelAdmin):
    pass
