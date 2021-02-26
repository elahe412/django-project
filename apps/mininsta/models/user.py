from hashlib import sha256

from django.db import models
from django_extensions.db.fields import AutoSlugField

class User(models.Model):
    email = models.EmailField('Email', unique=True)
    # user_name = models.SlugField( max_length=20, unique=True)
    user_name = AutoSlugField( populate_from=['email'], unique=True)
    password = models.CharField(max_length=50)

    class Meta:
        ordering = ['id']

    def __str__(self):
        return ' {} {}'.format(self.id, self.email)

    def save(self, *args, **kwarg):

        self.password = sha256(self.password.encode()).hexdigest()

        #self.password = '1234'
        super().save()