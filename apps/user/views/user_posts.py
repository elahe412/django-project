from django.views.generic import ListView

from apps.post.models import Post
from apps.user.models import User


class UserPostsList(ListView):
    template_name = 'user/my_profile.html'

    def get_user_posts(self):
        self.user = User.objects.get(email='eli@yahoo.com')
        return Post.objects.filter(user=self.user)

    def get_posts_number(self):
        return User.post_count
