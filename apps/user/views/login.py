from django.shortcuts import render
from django.views.generic.base import View

from apps.user.forms import LogInForm
from apps.user.models import User


class LoginUser(View):
    def get(self, request):
        form = LogInForm()
        return render(request, 'index.html', {'form': form})

    def post(self, request):
        form = LogInForm(request.POST)
        allowed_user = User.objects.get(email='eli@yahoo.com')
        if form.is_valid():
            form.save()
            return render(request, 'user/my_profile.html', {'user': allowed_user})
        return render(request, 'index.html', {'form': form})
