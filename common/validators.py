from django.core.exceptions import ValidationError


def password_validator(password):
    if len(password) < 6:
        raise ValidationError('password must have at least 6 characters')
