from django.urls import path
from django.views.generic import TemplateView

from apps.post.views import NewPostView
from apps.user.views.views import SignUpUser, SearchResultsView, HomePageView, UserProfile

urlpatterns = [
    path('signup/', SignUpUser.as_view(), name="signup_user"),
    # path('login/', LoginUser.as_view(), name="login_user"),
    path('search/', HomePageView.as_view(), name='home'),
    path('results/', SearchResultsView.as_view(), name='search_results'),
    path('home_page/', TemplateView.as_view(template_name='user/home_page.html'), name='home_page'),
    path('new_post/',NewPostView.as_view(),name='new_post'),
    # path('my_profile/<slug:user_slug>/',TemplateView.as_view(template_name='user/my_profile.html'),name='my_profile')
    # path('my_profile/',UserProfile.as_view(),name='my_profile')
    path('my_profile/<slug:user_slug>/',UserProfile.as_view(),name='my_profile')
    ]
