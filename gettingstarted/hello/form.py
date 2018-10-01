from django import forms
from hello import models
from django.forms import ModelForm
from django.contrib.auth.models import User

class LoginForm(forms.Form):
    emid = forms.DecimalField(label="員工編號", required=True, max_digits=50, decimal_places=0)
    password = forms.DecimalField(label="密碼", required=True, max_digits=6, decimal_places=0)

class RegisterForm(forms.Form):
    mId = forms.CharField(label="員工編號", required=True, max_length=7)
    mName = forms.CharField(label="姓名", required=True, max_length = 20)
    mDepartment = forms.CharField(label="部門", required=True, max_length = 20)
    mEmail = forms.EmailField(label="電子信箱", required=True, max_length = 30)
    mPassword = forms.CharField(label="密碼", required=True, max_length=6)
    #mPassword_confirm = forms.CharField(label="密碼確認", required=True, max_length=6)
    
'''
class RegisterForm(forms.Form):
    emid = forms.DecimalField(label="員工編號", required=True, max_digits=50, decimal_places=0)
    name = forms.CharField(label="姓名", required=True, max_length = 20)
    department = forms.CharField(label="部門", required=True, max_length = 20)
    email = forms.CharField(label="電子信箱", required=True, max_length = 30)
    password = forms.DecimalField(label="密碼", required=True, max_digits=6, decimal_places=0)
    password_confirm = forms.DecimalField(label="密碼確認", required=True, max_digits=6, decimal_places=0)
'''
