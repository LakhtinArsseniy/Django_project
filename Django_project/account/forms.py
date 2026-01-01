from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from account.models import User

class Registration(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class LoginForm(AuthenticationForm):
    pass