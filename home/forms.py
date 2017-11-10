# from django.contrib.auth.models import User
# from django import forms
#
#
# class Userform(forms.ModelForm):
#     password = forms.CharField(widget=forms.PasswordInput)
#
#     class Meta:
#         model = User
#         fields = ['username', 'password']

from django import forms
from fpagecse.models import Faculty


class MyFacultyForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = Faculty
        fields = ['faculty_name', 'username', 'password', 'department', 'designation', 'phone', 'email', 'room_no']


# class LoginForm(forms.ModelForm):
#     password = forms.CharField(widget=forms.PasswordInput)
#     class Meta:
#         model = Faculty
#         fields = ['username', 'password']





