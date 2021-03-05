# Generated by Django 3.1.7 on 2021-03-02 06:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_remove_user_user_name'),
        ('post', '0002_auto_20210302_0951'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='comment',
            field=models.ManyToManyField(blank=True, max_length=1000, null=True, related_name='post', to='post.Comment'),
        ),
        migrations.AlterField(
            model_name='post',
            name='likes',
            field=models.ManyToManyField(blank=True, null=True, related_name='likes', to='user.User'),
        ),
    ]
