import os
from django import forms
from HOMEWORK.models import Homework
from django.forms import ModelForm


class HomeworkAdd(ModelForm):
    class Meta:
        model = Homework
        fields = ['title', 'content']

"""
class FileUploadForm(ModelForm):
    def clean(self):
        cleaned_data = super(FileUploadForm, self).clean()
        extension = self.cleaned_data.get('file_field').name.split('.')[1]
        if extension not in ["doc", "docx"]:
            raise forms.ValidationError('Filetype Error!')
        return cleaned_data

    class Meta:
        model = Upload
        fields = ['file_field']
"""
