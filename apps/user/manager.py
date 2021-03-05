from django.db import models

from apps.post.models import Post
# from apps.user.models import User


class UserPostsManager(models.Manager):
    def user_posts_count(self):
        allowed_user=super().get_queryset().get(email='eli@yahoo.com')
        # allowed_user = User.objects.get(email='eli@yahoo.com')
        count = len(Post.objects.get(user=allowed_user))

        return count


