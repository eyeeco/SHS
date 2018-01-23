from uuid import uuid4
from django.db import models
from django.contrib.auth.models import User as _User
# Create your models here.
from . import USER_IDENTITIES, USER_IDENTITY_UNSET
from . import INSTITUTES, EDUCATION_BACK, TEACHER_TITLE


class UserInfo(models.Model):
    user = models.OneToOneField(_User, verbose_name='用户',
                                on_delete=models.CASCADE,
                                related_name='user_info')
    uid = models.UUIDField(default=uuid4, editable=False, unique=True)
    identity = models.IntegerField(verbose_name='身份',
                                   choices=USER_IDENTITIES)
    phone = models.CharField(verbose_name='电话', max_length=20)

    class Meta:
        verbose_name = '用户信息'

    def __str__(self):
        return self.user.first_name


class StudentInfo(UserInfo):
    user_info = models.OneToOneField(UserInfo,
                                     verbose_name='学生信息',
                                     on_delete=models.CASCADE,
                                     parent_link=True,
                                     related_name='student_info')
    student_id = models.CharField(verbose_name='学号', max_length=20)
    institute = models.CharField(verbose_name='学院', max_length=10,
                                 choices=INSTITUTES,
                                 default=INSTITUTES[0][0])
    education = models.IntegerField(verbose_name='年级',
                                    choices=EDUCATION_BACK,
                                    default=EDUCATION_BACK[0][0])

    class Meta:
        verbose_name = '学生信息'


class TeacherInfo(UserInfo):
    user_info = models.OneToOneField(UserInfo,
                                     verbose_name='教师信息',
                                     on_delete=models.CASCADE,
                                     parent_link=True,
                                     related_name='teacher_info')
    teacher_id = models.CharField(verbose_name='教工号', max_length=20)
    Title = models.CharField(verbose_name='职称', choices=TEACHER_TITLE,
                             max_length=10)
