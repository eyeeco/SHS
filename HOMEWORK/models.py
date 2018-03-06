from uuid import uuid4
from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
from ckeditor_uploader.fields import RichTextUploadingField

from AUTHENTICATION import PRACTICE_CLASS


class Upload(models.Model):
    uid = models.UUIDField(default=uuid4, editable=False, unique=True)
    file_field = models.FileField(upload_to="upload/%Y/%m/%d")
    submit_time = models.DateTimeField(verbose_name="提交时间",
                                       auto_now_add=True)
    user = models.ForeignKey(User, verbose_name='User',
                             on_delete=models.CASCADE)
    data_class = models.IntegerField(verbose_name='所属实践班',
                                     choices=PRACTICE_CLASS,
                                     default=PRACTICE_CLASS[1][0])
