from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from AUTHENTICATION.models import UserInfo, StudentInfo, TeacherInfo


class LoginForm(AuthenticationForm):
    pass


class StudentUpdateForm(forms.ModelForm):
    name = forms.CharField(
        label='姓名',
        widget=forms.TextInput())
    phone = forms.CharField(
        label='电话',
        widget=forms.TextInput(),
        min_length=11,
        max_length=11)
    email = forms.EmailField(
        label='邮箱')

    class Meta:
        model = StudentInfo
        fields = ['name', 'email', 'phone', 'student_id', 'institute',
                  'description']


class RegisterForm(forms.ModelForm):
    # TODO: Define other fields here
    user_name = forms.CharField(label='用户名', widget=forms.TextInput())
    name = forms.CharField(label='姓名', widget=forms.TextInput())
    password = forms.CharField(
        label='密码',
        widget=forms.PasswordInput(),
        min_length=1,
        max_length=20)
    confirm_password = forms.CharField(
        label='确认密码',
        widget=forms.PasswordInput(),
        min_length=1,
        max_length=20)
    phone = forms.CharField(
        label='电话',
        widget=forms.TextInput(),
        min_length=11,
        max_length=11)
    email = forms.EmailField(
        label='电子邮件')

    class Meta:
        model = UserInfo
        fields = ['email', 'user_name', 'password', 'confirm_password',
                  'name', 'phone']

    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)

    def clean(self):
        cleaned_data = super(RegisterForm, self).clean()
        errors = {}
        username = cleaned_data.get('username')
        try:
            User.objects.get(username=username)
        except User.DoesNotExist:
            pass
        else:
            errors['username'] = ['用户名已存在']
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')
        if password != confirm_password:
            errors['confirm_password'] = [
                '两次输入密码不一致']
        if errors:
            raise forms.ValidationError(errors)
        return cleaned_data


class StudentRegisterForm(RegisterForm):

    class Meta:
        model = StudentInfo
        fields = ['email', 'user_name', 'password', 'confirm_password',
                  'name', 'phone', 'student_id', 'institute', 'education']
