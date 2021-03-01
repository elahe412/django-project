from django.urls import path

from apps.post.views import PostDetail, PostsList

urlpatterns = [
    path('<int:pk>/', PostDetail.as_view(), name='post_detail'),
    path('posts/', PostsList.as_view(), name='post_list'),
]
