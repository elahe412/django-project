from django.contrib import admin

# Register your models here.
from apps.mininsta.models import Post, User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['user_name','email']
    search_fields = ['email']
    #prepopulated_fields={'user_name':['email']}


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    fields = []
    list_display = ['title','publish_date']
    search_fields = []



