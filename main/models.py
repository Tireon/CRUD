from django.db import models
from django import forms

class Member(models.Model):
    lastname = models.CharField(max_length=20, verbose_name='Фамилия')
    firstname = models.CharField(max_length=20, verbose_name='Имя')
    post = models.CharField(max_length=50, verbose_name='Должность')
    data = models.DateField(max_length=100, verbose_name='Дата приема на работу')
    email = models.CharField(max_length=30, verbose_name='Электронная почта')
    number = models.CharField(max_length=15, verbose_name='Номер телефона')
    status = models.CharField(max_length=15, verbose_name='Статус(активен/уволен)')

class LoginUserForm(forms.Form):
    username = forms.CharField(label = "Логин",
                    widget = forms.TextInput(attrs={'class': 'form-imput'}))
    password = forms.CharField(label = "Пароль",
                    widget = forms.PasswordInput(attrs={'class': 'form-imput'}))