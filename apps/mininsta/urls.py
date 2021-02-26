from django.urls import path

from apps.mininsta.views import SignUpUser, LoginUser, PostDetail, PostsList, SearchResultsView, HomePageView

urlpatterns = [
    path('signup/', SignUpUser.as_view(), name="signup_user"),
    path('login/', LoginUser.as_view(), name="login_user"),
    # path('post/<slug:slug>/', PostDetail.as_view(), name='post'),
    path('<int:pk>/', PostDetail.as_view(), name='post_detail'),
    path('posts/', PostsList.as_view(), name='post_list'),
    path('search/', HomePageView.as_view(), name='home'),
    path('results/', SearchResultsView.as_view(), name='search_results'),
]
