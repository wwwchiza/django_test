from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class EditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name')


class RegisterForm(UserCreationForm):
    username = forms.CharField(max_length=254, help_text='Обязательное поле')
    # поле почты проходит валидацию иначе чем CharField
    email = forms.CharField(widget=forms.EmailInput, max_length=254, help_text='Обязательное поле.', required=False)
    # пароль также проходит валидацию и по умолчанию к нему применяются довольно строгие правила
    # но тут указывается тип поля уже с помощью аргумента widget
    password1 = forms.CharField(widget=forms.PasswordInput, max_length=254, help_text='')
    password2 = forms.CharField(widget=forms.PasswordInput, max_length=254, help_text='')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2',)

class LoginForm(forms.Form):
    login = forms.CharField(max_length=254,
                            help_text='')
    password = forms.CharField(widget=forms.PasswordInput)

class SearchForm(forms.Form):
    # required отвечает за то является ли поле обязательным
    search = forms.CharField(required=False,
                             label='', )
