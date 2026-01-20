from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from account.models import User

class Registration(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True, label="Ім'я")
    last_name = forms.CharField(max_length=30, required=True, label="Прізвище")
    email = forms.EmailField(required=True, label="Email")
    age = forms.IntegerField(label="Вік")
    phone = forms.CharField(max_length=20, label="Телефон")

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'age', 'phone', 'password1', 'password2']

    def clean_age(self):
        age = self.cleaned_data.get('age')
        if age < 12 or age > 18:
            raise forms.ValidationError("Вік повинен бути від 12 до 18 років.")
        return age

    def clean_phone(self):
        phone = self.cleaned_data.get('phone')
        if not phone.startswith("+380") or len(phone) != 13 or not phone[1:].isdigit():
            raise forms.ValidationError("Телефон повинен бути у форматі +380XXXXXXXXX")
        return phone

class LoginForm(AuthenticationForm):
    pass
