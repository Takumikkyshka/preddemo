from django import forms

from .models import Zayavka, User

from django.contrib.auth.forms import UserCreationForm
from django.core.validators import RegexValidator

class CreateUserForm(UserCreationForm):

    username = forms.CharField(min_length=6, label='Имя пользователя')
    phone = forms.CharField(max_length=11, min_length=11, label='Номер телефона', validators=[
        RegexValidator(
            regex = r'^8/d{10}$',
            message = 'Введите номер телефона в формате 8(XXX)-XXX-XX-XX'
        )
    ])
    email = forms.EmailField(label='Электронная почта')
    third_name = forms.CharField(max_length=150, label='Отчество')

    class Meta: 
        model = User
        fields = ['username', 'first_name', 'last_name', 'third_name', 'phone', 'email', 'password1', 'password2']

class CreateZayavkaForm(forms.ModelForm):
    class Meta:
        model = Zayavka
        fields = ['name', 'date', 'payment']
        widgets = {
            'date': forms.DateInput(
                attrs= {'type': 'date'}
            )
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        name_choices = list(self.fields['name'].choices)
        name_choices[0] = ('', 'Выберите помещение')
        self.fields['name'].choices = name_choices

        payment_choices = list(self.fields['payment'].choices)
        payment_choices[0] = ('', 'Выберите способ оплаты')
        self.fields['payment'].choices = payment_choices