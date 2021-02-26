from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View
from django.views.generic import DetailView, ListView, TemplateView

from apps.mininsta.forms import SignUpForm, LogInForm
from apps.mininsta.models import Post, User


class SignUpUser(View):
    def get(self, request):
        form = SignUpForm()
        return render(request, 'mininsta/signup.html', {'form': form})

    def post(self, request):
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/Thanks/')
        return render(request, 'mininsta/signup.html', {'form': form})


class LoginUser(View):
    def get(self, request):
        form = LogInForm()
        return render(request, 'mininsta/login.html', {'form': form})

    def post(self, request):
        form = LogInForm(request.POST)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/login-welcome/')
        return render(request, 'mininsta/login.html', {'form': form})


class PostsList(ListView):
    model = Post

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     return context


class PostDetail(DetailView):
    model = Post

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     return context


class HomePageView(TemplateView):
    template_name = 'mininsta/home.html'


class SearchResultsView(ListView):
    model = User
    template_name = 'mininsta/search_results.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = User.objects.filter(email__icontains=query)
        return object_list
