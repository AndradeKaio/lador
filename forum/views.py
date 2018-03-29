from django.http import HttpResponse

from forum.models import Post


def index(request):
    return HttpResponse("Hello, World!")

# Return the recent posts
# Recently posted
def news(request):
    latest_posts = Post.objects.order_by('post_date')
    output = ', '.join([q.post_text for q in latest_posts])
    return HttpResponse(output)


# Return the hottest post
# More voted
def hot(request):
    pass