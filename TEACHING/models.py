from uuid import uuid4
from django.db import models
from django.contrib.auth.models import User

from . import DATA_TYPE
from AUTHENTICATION import PRACTICE_CLASS


class UploadTeacher(models.Model):
    uid = models.UUIDField(default=uuid4, editable=False, unique=True)
    file_field = models.FileField(upload_to="upload/teacher/%Y/%m/%d")
    submit_time = models.DateTimeField(verbose_name="提交时间",
                                       auto_now_add=True)
    user = models.ForeignKey(User, verbose_name='User',
                             on_delete=models.CASCADE)
    data_type = models.IntegerField(verbose_name='资料类型', choices=DATA_TYPE,
                                    default=DATA_TYPE[0][0])
    data_class = models.IntegerField(verbose_name='所属实践班',
                                     choices=PRACTICE_CLASS,
                                     default=PRACTICE_CLASS[0][0])
