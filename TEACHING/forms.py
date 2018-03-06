from django import forms
from django.forms import ModelForm

from TEACHING.models import UploadTeacher


class FileUploadForm(ModelForm):
    """
    def clean(self):
        cleaned_data = super(FileUploadForm, self).clean()
        extension = self.cleaned_data.get('file_field').name.split('.')[-1]
        if extension not in ["docx"]:
            raise forms.ValidationError('Filetype Error!')
        return cleaned_data
    """
    class Meta:
        model = UploadTeacher
        fields = ['data_type', 'file_field']
