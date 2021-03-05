from django.views.generic import ListView, TemplateView

from apps.user.models import User


class HomePageView(TemplateView):
    template_name = 'user/home.html'


class SearchResultsView(ListView):
    model = User
    template_name = 'user/search_results.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = User.objects.filter(email__icontains=query)
        return object_list
