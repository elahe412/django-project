from apps.post.models import Post
from apps.user.models import User

@register.inclusion_tag('user/post_number.html')
def user_posts_count():
    allowed_user = User.objects.get(email='eli@yahoo.com')
    count = len(Post.objects.get(user=allowed_user))
    return count
