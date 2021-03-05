from hashlib import sha256

from django import forms
from django.core.exceptions import ValidationError

from apps.user.models import User


class SignUpForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['email', 'password']


class LogInForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(max_length=50)

    def clean(self):
        cleaned_data = super().clean()
        e_mail = cleaned_data.get('email')
        pass_word = sha256(cleaned_data.get('password').encode()).hexdigest()
        allowed_user = User.objects.get(email='eli@yahoo.com')
        if not e_mail:
            return ValidationError('User Unavailable')
        elif e_mail == allowed_user.email:
            if pass_word != allowed_user.password:
                # if not User.objects.filter(email=e_mail, password=pass_word).exists():
                raise ValidationError('Incorrect Password')
        else:
            return ValidationError('You can not login at this time')
