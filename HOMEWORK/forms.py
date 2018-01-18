from HOMEWORK.models import Homework
from django.forms import ModelForm


class HomeworkAdd(ModelForm):
    class Meta:
        model = Homework
        fields = ['title', 'content']
