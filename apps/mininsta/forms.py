from hashlib import sha256

from django import forms
from django.core.exceptions import ValidationError

from apps.mininsta.models import User


class SignUpForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['email', 'password']


class LogInForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['email', 'password']

    def clean(self):
        cleaned_data = super().clean()
        e_mail = cleaned_data.get('email')
        # pass_word = cleaned_data.get('password')
        pass_word = sha256(cleaned_data.get('password').encode()).hexdigest()
        print(pass_word)
        if e_mail:
            user_pass = User.objects.get(email=e_mail).password.encode()
            if pass_word != sha256(user_pass).hexdigest():
                print(pass_word)
                raise ValidationError('Incorrect Password')


