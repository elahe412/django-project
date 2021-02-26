from django.db import models
from django.urls import reverse, NoReverseMatch
from django.utils import timezone


class Post(models.Model):
    title = models.CharField(max_length=100, default='', )
    # writer = models.CharField(max_length=100)
    caption = models.TextField(default='')
    publish_date = models.DateTimeField('publish tate', auto_now_add=True)
    # slug = models.SlugField(max_length=100, unique=True, default='')

    class Meta:
        ordering = ['-publish_date']

    def __str__(self):
        return self.caption

    def get_absolute_url(self):
        try:
            return reverse('post_detail', args=(str(self.id)))
        except NoReverseMatch:
            return reverse('404')


