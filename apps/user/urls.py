from django.urls import path
from django.views.generic import TemplateView

from apps.user.views import SignUpUser, LoginUser, SearchResultsView, HomePageView

urlpatterns = [
    path('signup/', SignUpUser.as_view(), name="signup_user"),
    path('login/', LoginUser.as_view(), name="login_user"),
    path('search/', HomePageView.as_view(), name='home'),
    path('results/', SearchResultsView.as_view(), name='search_results'),
    path('home_page/', TemplateView.as_view(template_name='user/home_page.html'), name='home_page'),
    ]
