from django.forms import CharField, Form, PasswordInput
from django import forms

class RegistrationForm(Form):
    login = CharField(
        label='Логин',
        max_length=100,
        error_messages={'required': 'Укажите логин'})
    password = CharField(
        label='Пароль',
        widget=PasswordInput(),
        error_messages={'required': 'Укажите пароль'})
    password_again = CharField(
        label='Пароль (еще раз)',
        widget=PasswordInput(),
        error_messages={'required': 'Укажите пароль еще раз'})

    # Валидация проходит в этом методе
    def clean(self):
        # Определяем правило валидации
        if self.cleaned_data.get('password') != self.cleaned_data.get('password_again'):
            # Выбрасываем ошибку, если пароли не совпали
            raise forms.ValidationError('Пароли должны совпадать!')
        return self.cleaned_data
