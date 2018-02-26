from uuid import uuid4
from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
from ckeditor_uploader.fields import RichTextUploadingField


class Homework(models.Model):
    title = models.CharField(max_length=100, verbose_name="标题")
    content = RichTextField(blank=True, null=True, verbose_name="内容")
    submit_time = models.DateTimeField(verbose_name="提交时间",
                                       auto_now_add=True)

    def __unicode__(self):
        return self.name


class Upload(models.Model):
    uid = models.UUIDField(default=uuid4, editable=False, unique=True)
    file_field = models.FileField(upload_to="upload/%Y/%m/%d")
    submit_time = models.DateTimeField(verbose_name="提交时间",
                                       auto_now_add=True)
