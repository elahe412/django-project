from django.shortcuts import render, redirect
from django.views.generic.base import View
from apps.user.forms import SignUpForm


class SignUpUser(View):
    def get(self, request):
        form = SignUpForm()
        return render(request, 'user/signup.html', {'form': form})

    def post(self, request):
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('my_profile')
        return render(request, 'user/signup.html', {'form': form})
