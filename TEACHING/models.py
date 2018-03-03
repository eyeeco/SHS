from uuid import uuid4
from django.db import models
from django.contrib.auth.models import User


class UploadTeacher(models.Model):
    uid = models.UUIDField(default=uuid4, editable=False, unique=True)
    file_field = models.FileField(upload_to="upload/teacher/%Y/%m/%d")
    submit_time = models.DateTimeField(verbose_name="提交时间",
                                       auto_now_add=True)
    user = models.ForeignKey(User, verbose_name='User',
                             on_delete=models.CASCADE)
