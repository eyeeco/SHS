from django import forms
from django.forms import ModelForm

from HOMEWORK.models import Homework, Upload


class HomeworkAdd(ModelForm):
    class Meta:
        model = Homework
        fields = ['title', 'content']


class FileUploadForm(ModelForm):
    def clean(self):
        cleaned_data = super(FileUploadForm, self).clean()
        extension = self.cleaned_data.get('file_field').name.split('.')[-1]
        if extension not in ["pdf"]:
            raise forms.ValidationError('Filetype Error!')
        return cleaned_data

    class Meta:
        model = Upload
        fields = ['file_field']
